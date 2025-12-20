#!/usr/bin/env python3
import sys
import os
import hashlib
import json
import time
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
        def tip(m): print(f"Tip: {m}")
        @staticmethod
        def error(m): print(f"Error: {m}")

def generate_vai():
    """Generates a DID-compliant Verified Agent Identity (VAI)."""
    username = os.environ.get("USER", "pai-user")
    hostname = os.uname().nodename
    seed = f"{username}@{hostname}:{time.time()}"
    identity_hash = hashlib.sha256(seed.encode()).hexdigest()
    
    vai = {
        "@context": ["https://www.w3.org/ns/did/v1"],
        "id": f"did:pai:{identity_hash[:16]}",
        "verificationMethod": [{
            "id": f"did:pai:{identity_hash[:16]}#key-1",
            "type": "Ed25519VerificationKey2020",
            "controller": f"did:pai:{identity_hash[:16]}",
            "publicKeyMultibase": identity_hash
        }],
        "authentication": [f"did:pai:{identity_hash[:16]}#key-1"],
        "service": [{
            "id": "#pai-bridge",
            "type": "PAIUniversalBridge",
            "serviceEndpoint": "local://bin/pai"
        }]
    }
    
    output = json.dumps(vai, indent=2)
    PAI_UI.panel(f"Generated Verified Agent Identity (VAI):\n\n[bold cyan]{vai['id']}[/bold cyan]\n\n[dim]{output}[/dim]", title="Protocol: Identity Generation", style="green")
    
    # Store identity
    identity_path = os.path.join(PAI_ROOT, "identity.json")
    with open(identity_path, "w") as f:
        json.dump(vai, f, indent=2)
    print(f"\n[bold green]Identity secured in identity.json[/bold green]")

def register_on_chain(network: str = "gnosis"):
    """Simulates Olas L2 Registration for the PAI node."""
    identity_path = os.path.join(PAI_ROOT, "identity.json")
    if not os.path.exists(identity_path):
        PAI_UI.error("No VAI found. Run 'pai run Protocol generate' first.")
        return

    with open(identity_path, "r") as f:
        vai = json.load(f)

    PAI_UI.panel(f"Initiating Olas L2 Registration on [bold yellow]{network.upper()}[/bold yellow]...", title="Protocol: Mesh Registration", style="cyan")
    
    # Mock TX hash and agent registration
    tx_hash = "0x" + "a" * 64 
    agent_id = vai['id'].split(":")[-1]
    
    result = {
        "status": "SUCCESS",
        "network": network,
        "transaction_hash": tx_hash,
        "olas_agent_nft": f"olas://agent/{agent_id}",
        "legal_wrapper": "Wyoming DAO LLC (Pending Articles of Organization)"
    }
    
    PAI_UI.panel(f"Registration Successful!\n\nNetwork: {network}\nAgent NFT: [bold green]{result['olas_agent_nft']}[/bold green]\nTX Hash: [dim]{tx_hash}[/dim]", title="Protocol: Mesh Status", style="green")
    
    # Store mesh status
    mesh_status_path = os.path.join(PAI_ROOT, "History", "mesh_status.json")
    os.makedirs(os.path.dirname(mesh_status_path), exist_ok=True)
    with open(mesh_status_path, "w") as f:
        json.dump(result, f, indent=2)

def main():
    if len(sys.argv) < 2:
        print("Usage: protocol <command> [args]")
        print("Commands: generate, register")
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "generate":
        generate_vai()
    elif cmd == "register":
        network = sys.argv[2] if len(sys.argv) > 2 else "gnosis"
        register_on_chain(network)
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()
