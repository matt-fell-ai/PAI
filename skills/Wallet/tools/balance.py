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
        @staticmethod
        def table(t, h, r, s): print(f"--- {t} ---")

def show_balance():
    # Simulated Sovereign Wallet
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
    
    # Compute Arbitrage Insight
    local_savings = 42.15
    print(f"\n[bold blue]Compute Arbitrage:[/bold blue] Running local models saved [bold green]${local_savings:.2f}[/bold green] this month.")

def main():
    show_balance()

if __name__ == "__main__":
    main()
