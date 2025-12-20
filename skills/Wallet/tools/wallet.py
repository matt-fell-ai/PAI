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
        @staticmethod
        def tip(m): print(f"Tip: {m}")

def show_balance():
    """Displays the sovereign wallet status and compute arbitrage insights."""
    balance_usd = 1240.50
    balance_mor = 450.25
    balance_tao = 12.80
    
    rows = [
        ["USD", f"${balance_usd:.2f}", "Stripe/Bank link"],
        ["MOR", f"{balance_mor:.2f}", "Morpheus Compute Credits"],
        ["TAO", f"{balance_tao:.2f}", "Bittensor Rewards"]
    ]
    
    PAI_UI.panel("PAI Sovereign Wallet Status", title="Wallet: Balance", style="green")
    PAI_UI.table("Asset Allocation", ["Currency", "Balance", "Source"], rows, style="green")
    
    local_savings = 42.15
    print(f"\n[bold blue]Compute Arbitrage:[/bold blue] Running local models saved [bold green]${local_savings:.2f}[/bold green] this month.")

def create_invoice(item: str, amount: str):
    """Generates a simulated invoice for PAI services."""
    PAI_UI.panel(f"Generating Sovereign Invoice for '{item}'...", title="Wallet: Invoice", style="cyan")
    print(f" • [cyan]Action:[/cyan] Creating PDF invoice: INV-2030-{item[:4].upper()}")
    print(f" • [cyan]Amount:[/cyan] ${amount}")
    print("\n[bold green]SUCCESS:[/bold green] Invoice generated and stored in History/reports.")

def main():
    if len(sys.argv) < 2:
        # Default to balance if no command provided
        show_balance()
        return

    cmd = sys.argv[1]
    if cmd == "balance":
        show_balance()
    elif cmd == "invoice":
        if len(sys.argv) < 3:
            print("Usage: wallet invoice <item> [amount]")
            sys.exit(1)
        item = sys.argv[2]
        amount = sys.argv[3] if len(sys.argv) > 3 else "0.00"
        create_invoice(item, amount)
    else:
        # Check if skill-name based call
        if cmd.lower() == "wallet":
            if len(sys.argv) > 2:
                main_args = sys.argv[2:]
                # Recursive call with shifted args
                sys.argv = [sys.argv[0]] + main_args
                main()
            else:
                show_balance()
        else:
            print(f"Unknown command: {cmd}")
            sys.exit(1)

if __name__ == "__main__":
    main()
