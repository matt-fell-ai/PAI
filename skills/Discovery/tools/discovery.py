#!/usr/bin/env python3
import os
import sys
import subprocess

PAI_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.join(PAI_ROOT, "bin", "lib"))

try:
    from ui import PAI_UI, console
except ImportError:
    class PAI_UI:
        @staticmethod
        def table(t, c, r, s): print(f"--- {t} ---")

def scan_env():
    essential_bins = ["git", "python3", "bun", "gh", "curl", "docker", "npm", "uv", "go"]
    
    rows = []
    for bin_name in essential_bins:
        path = subprocess.run(["which", bin_name], capture_output=True, text=True).stdout.strip()
        status = "[green]FOUND[/green]" if path else "[red]MISSING[/red]"
        rows.append([bin_name, status, path or "-"])

    PAI_UI.table("Environment Scan: Tool Inventory", ["Binary", "Status", "Path"], rows, style="blue")

def main():
    if len(sys.argv) < 2:
        print("Usage: discovery <command>")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "scan":
        scan_env()
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
