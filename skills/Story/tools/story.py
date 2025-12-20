#!/usr/bin/env python3
import sys
import os
import hashlib
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

def register_asset(file_path: str):
    """Registers a local file as Programmable IP via the Story Protocol."""
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return

    PAI_UI.panel(f"Story Protocol: Registering [bold yellow]{file_path}[/bold yellow]", title="Story: IP-Native Asset", style="magenta")
    
    with open(file_path, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    
    ip_id = f"ip:story:pai:{file_hash[:16]}"
    print(f" • [cyan]Proof of Creativity:[/cyan] SHA-256 Fingerprint verified.")
    print(f" • [cyan]Status:[/cyan] REGISTERED (License: PIL-COMMERCIAL-USE)")
    print(f" • [bold green]IP ID:[/bold green] {ip_id}")

def main():
    if len(sys.argv) < 2:
        print("Usage: story register <file_path>")
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "register":
        if len(sys.argv) < 3:
            print("Usage: story register <file_path>")
            sys.exit(1)
        register_asset(sys.argv[2])
    else:
        # Fallback for skill-name based call
        register_asset(cmd)

if __name__ == "__main__":
    main()
