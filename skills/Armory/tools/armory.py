#!/usr/bin/env python3
import os
import sys
import subprocess
import json

PAI_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARMORY_DIR = os.path.join(PAI_ROOT, "armory")

# Tool Manifest
TOOLS = {
    "sherlock": {
        "repo": "https://github.com/sherlock-project/sherlock.git",
        "install": "pip3 install -r requirements.txt",
        "exec": "python3 sherlock/sherlock",
        "type": "git"
    },
    "nuclei": {
        "repo": "https://github.com/projectdiscovery/nuclei",
        "install": "go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest",
        "exec": "nuclei",
        "type": "go"
    },
    "ffuf": {
        "repo": "https://github.com/ffuf/ffuf",
        "install": "go install github.com/ffuf/ffuf/v2@latest",
        "exec": "ffuf",
        "type": "go"
    },
    "lynis": {
        "repo": "https://github.com/CISOfy/lynis.git",
        "install": "chmod +x lynis/lynis",
        "exec": "./lynis/lynis",
        "type": "git"
    },
    "theharvester": {
        "repo": "https://github.com/laramies/theHarvester.git",
        "install": "pip3 install -r requirements.txt",
        "exec": "python3 theHarvester/theHarvester.py",
        "type": "git"
    }
}

def install_tool(tool_name):
    tool_name = tool_name.lower()
    if tool_name not in TOOLS:
        print(f"Error: Tool '{tool_name}' not in Armory manifest.")
        return False

    os.makedirs(ARMORY_DIR, exist_ok=True)
    tool_info = TOOLS[tool_name]
    print(f"--- Armory: Installing '{tool_name}' ---")

    try:
        if tool_info["type"] == "git":
            target_path = os.path.join(ARMORY_DIR, tool_name)
            if not os.path.exists(target_path):
                print(f" [GIT] Cloning {tool_info['repo']}...")
                subprocess.run(["git", "clone", tool_info["repo"], target_path], check=True)
            
            print(f" [INSTALL] Running setup: {tool_info['install']}")
            # Run install in the tool directory
            subprocess.run(tool_info["install"], shell=True, cwd=target_path)
            
        elif tool_info["type"] == "go":
            print(f" [GO] Installing {tool_name}...")
            subprocess.run(tool_info["install"], shell=True)
            
        print(f"\n[SUCCESS] '{tool_name}' is now in your Armory.")
        return True
    except Exception as e:
        print(f"Error installing tool: {e}")
        return False

def list_tools():
    print("--- PAI Armory Manifest ---")
    for name, info in TOOLS.items():
        installed = "[Installed]" if os.path.exists(os.path.join(ARMORY_DIR, name)) else "[Not Installed]"
        print(f" - {name:<15} {installed:<15} ({info['repo']})")

def run_tool(tool_name, args):
    tool_name = tool_name.lower()
    if tool_name not in TOOLS:
        print(f"Error: Tool '{tool_name}' not in Armory manifest.")
        return

    tool_info = TOOLS[tool_name]
    target_path = os.path.join(ARMORY_DIR, tool_name)
    
    print(f"--- Armory: Executing '{tool_name}' ---")
    
    # Check if installed
    if tool_info["type"] == "git" and not os.path.exists(target_path):
        print(f" [!] Tool '{tool_name}' is not installed. Run 'pai run Armory install {tool_name}' first.")
        return

    full_cmd = f"{tool_info['exec']} {' '.join(args)}"
    print(f" [EXEC] {full_cmd}")
    
    try:
        subprocess.run(full_cmd, shell=True, cwd=target_path if tool_info["type"]=="git" else None)
    except Exception as e:
        print(f"Error executing tool: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: armory <command> [args]")
        print("Commands: install, list, run")
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    if cmd == "install":
        if len(sys.argv) < 3:
            print("Usage: armory install <tool_name>")
            sys.exit(1)
        install_tool(sys.argv[2])
    elif cmd == "list":
        list_tools()
    elif cmd == "run":
        if len(sys.argv) < 3:
            print("Usage: armory run <tool_name> [args]")
            sys.exit(1)
        run_tool(sys.argv[2], sys.argv[3:])
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
