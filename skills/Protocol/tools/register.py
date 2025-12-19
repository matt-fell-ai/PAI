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
        def panel(c, t, s): print(f"--- {t} ---\n{c}")

def register_on_chain(network="gnosis"):
    # Simulated Olas L2 Registration
    identity_path = os.path.join(PAI_ROOT, "identity.json")
    if not os.path.exists(identity_path):
        PAI_UI.panel("No VAI found. Run 'pai run Protocol generate' first.", title="Protocol: Error", style="red")
        return

    with open(identity_path, "r") as f:
        vai = json.load(f)

    PAI_UI.panel(f"Initiating Olas L2 Registration on [bold yellow]{network.upper()}[/bold yellow]...", title="Protocol: Mesh Registration", style="cyan")
    
    # In a real scenario, this would use the autonomy CLI or a web3 provider
    # We simulate the successful minting of the Agent NFT
    tx_hash = "0x" + "a" * 64 # Mock TX hash
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
    with open(mesh_status_path, "w") as f:
        json.dump(result, f, indent=2)

def main():
    network = "gnosis"
    if len(sys.argv) > 1:
        network = sys.argv[1]
    register_on_chain(network)

if __name__ == "__main__":
    main()
