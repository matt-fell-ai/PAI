#!/usr/bin/env python3
import sys
import os
import json
from typing import List, Optional

PAI_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.join(PAI_ROOT, "bin", "lib"))

try:
    from ui import PAI_UI, console
except ImportError:
    class PAI_UI:
        @staticmethod
        def panel(c, t, s): print(f"--- {t} ---\n{c}")
        @staticmethod
        def table(t, h, r, s): print(f"--- {t} ---")

def list_services():
    """Generates the ACP (Agentic Commerce Protocol) Manifest."""
    skills_dir = os.path.join(PAI_ROOT, "skills")
    services = []
    
    # Identify available PAI services for the agentic economy
    for skill in sorted(os.listdir(skills_dir)):
        skill_path = os.path.join(skills_dir, skill)
        if os.path.isdir(skill_path):
            tools_dir = os.path.join(skill_path, "tools")
            if os.path.exists(tools_dir):
                for tool in os.listdir(tools_dir):
                    if tool.endswith(".py") or tool.endswith(".sh"):
                        tool_name = tool.replace(".py", "").replace(".sh", "")
                        services.append([f"[bold yellow]{skill}[/bold yellow]", tool_name, "0.001 MOR", "READY"])
    
    PAI_UI.table("Market: ACP Service Manifest", ["Skill", "Tool", "Price", "Status"], services, style="magenta")
    
    # Export Manifest
    manifest_path = os.path.join(PAI_ROOT, "acp-manifest.json")
    with open(manifest_path, "w") as f:
        json.dump({"version": "2.0.0", "services": services}, f, indent=2)
    print(f"\n[bold green]SUCCESS:[/bold green] ACP Manifest exported to acp-manifest.json")

def main():
    if len(sys.argv) < 2:
        list_services()
        return
    
    cmd = sys.argv[1]
    if cmd == "manifest" or cmd == "list":
        list_services()
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
