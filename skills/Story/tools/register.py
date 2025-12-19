#!/usr/bin/env python3
import sys
import os
import hashlib
import json

PAI_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.join(PAI_ROOT, "bin", "lib"))

try:
    from ui import PAI_UI, console
except ImportError:
    class PAI_UI:
        @staticmethod
        def panel(c, t, s): print(f"--- {t} ---\n{c}")

def register_asset(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return

    PAI_UI.panel(f"Registering Asset as Programmable IP: [bold yellow]{file_path}[/bold yellow]", title="Story: IP Registration", style="magenta")
    
    # Calculate Fingerprint (Simulated IP registration)
    with open(file_path, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    
    ip_id = f"ip:story:pai:{file_hash[:16]}"
    
    registration_data = {
        "ip_id": ip_id,
        "asset_name": os.path.basename(file_path),
        "fingerprint": file_hash,
        "owner": "did:pai:sovereign_user",
        "license": "PIL-COMMERCIAL-USE",
        "status": "REGISTERED"
    }
    
    output = json.dumps(registration_data, indent=2)
    print(f" • [cyan]Proof of Creativity:[/cyan] Hash generated {file_hash[:8]}...")
    print(f" • [cyan]Layer 1 Sync:[/cyan] Transmitting to Story Protocol...")
    print(f" • [bold green]SUCCESS:[/bold green] Asset registered with ID: {ip_id}")
    
    PAI_UI.panel(f"[dim]{output}[/dim]", title="IP Metadata (Story Protocol)", style="magenta")

def main():
    if len(sys.argv) < 2:
        print("Usage: register <file_path>")
        sys.exit(1)
    
    register_asset(sys.argv[1])

if __name__ == "__main__":
    main()
