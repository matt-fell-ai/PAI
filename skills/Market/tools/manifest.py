#!/usr/bin/env python3
import sys
import os
import json

PAI_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.join(PAI_ROOT, "bin", "lib"))

try:
    from ui import PAI_UI, console
except ImportError:
    class PAI_UI:
        @staticmethod
        def table(t, h, r, s): print(f"--- {t} ---")

def list_services():
    skills_dir = os.path.join(PAI_ROOT, "skills")
    services = []
    
    # ACP (Agentic Commerce Protocol) Manifest Generation
    for skill in os.listdir(skills_dir):
        skill_path = os.path.join(skills_dir, skill)
        if os.path.isdir(skill_path):
            tools_dir = os.path.join(skill_path, "tools")
            if os.path.exists(tools_dir):
                for tool in os.listdir(tools_dir):
                    if tool.endswith(".py") or tool.endswith(".sh"):
                        services.append([
                            f"[bold yellow]{skill}[/bold yellow]",
                            tool.replace(".py", "").replace(".sh", ""),
                            "0.001 MOR/req", # Standardized micro-pricing
                            "AVAILABLE"
                        ])
    
    PAI_UI.table("Agentic Commerce Manifest (ACP-Ready)", ["Skill", "Tool", "Price (Est)", "Status"], services, style="magenta")
    
    # Export Manifest
    manifest = {
        "version": "1.0.0",
        "protocol": "ACP",
        "services": [{"skill": s[0], "tool": s[1], "price": s[2]} for s in services]
    }
    with open(os.path.join(PAI_ROOT, "acp-manifest.json"), "w") as f:
        json.dump(manifest, f, indent=2)

def main():
    list_services()

if __name__ == "__main__":
    main()
