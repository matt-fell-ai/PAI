#!/usr/bin/env python3
import os
import sys
import subprocess

def scan_env():
    print("--- Discovery: Environment Scan ---")
    essential_bins = ["git", "python3", "bun", "gh", "curl", "docker", "npm", "uv"]
    
    available = []
    missing = []
    for bin_name in essential_bins:
        if subprocess.run(["which", bin_name], capture_output=True).returncode == 0:
            available.append(bin_name)
        else:
            missing.append(bin_name)

    print(f"Available Tools: {', '.join(available)}")
    print(f"Missing (Opportunities): {', '.join(missing)}")

    # Check for local services (e.g., voice server)
    try:
        result = subprocess.run(["curl", "-s", "http://localhost:8888/health"], capture_output=True, text=True, timeout=2)
        if result.returncode == 0:
            print(" [OK] PAI Voice Server detected on port 8888.")
    except:
        print(" [ ] PAI Voice Server not detected.")

def find_tool(query):
    print(f"Searching for tool: {query}")
    print("TIP: Use 'pai run Research search' for a deep web dive, then use 'Createskill' to integrate.")

def main():
    if len(sys.argv) < 2:
        print("Usage: discovery <command>")
        print("Commands: scan, find")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "scan":
        scan_env()
    elif cmd == "find":
        if len(sys.argv) < 3:
            print("Usage: discovery find <query>")
            sys.exit(1)
        find_tool(sys.argv[2])
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()
