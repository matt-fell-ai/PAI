#!/usr/bin/env python3
import sys
import os
import hashlib
import json
import time

PAI_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.join(PAI_ROOT, "bin", "lib"))

try:
    from ui import PAI_UI, console
except ImportError:
    class PAI_UI:
        @staticmethod
        def panel(c, t, s): print(f"--- {t} ---\n{c}")

def generate_vai():
    # VAI: Verified Agent Identity (DID-compatible)
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

def main():
    generate_vai()

if __name__ == "__main__":
    main()
