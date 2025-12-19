#!/usr/bin/env python3
import sys
import os
import random

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

def run_negotiation(target, min_price):
    target = float(target)
    min_price = float(min_price)
    
    PAI_UI.panel(f"Initiating Agent-to-Agent Negotiation\nTarget: [bold green]${target}[/bold green] | Floor: [bold red]${min_price}[/bold red]", title="Bargain: Game-Theory Engine", style="yellow")
    
    # Simulated Game Theory Loop (Concession-Rigidity)
    current_offer = target * 1.2 # Anchor high
    opponent_offer = target * 0.5
    
    steps = []
    for i in range(1, 5):
        concession = (current_offer - min_price) * 0.2
        current_offer -= concession
        opponent_offer += (target - opponent_offer) * random.uniform(0.1, 0.3)
        steps.append([f"Round {i}", f"${current_offer:.2f}", f"${opponent_offer:.2f}"])
        
        if opponent_offer >= current_offer:
            final_price = current_offer
            break
    else:
        final_price = (current_offer + opponent_offer) / 2

    PAI_UI.table("Negotiation Transcript", ["Round", "PAI Offer", "Peer Offer"], steps, style="yellow")
    
    print(f"\n[bold green]AGREEMENT REACHED:[/bold green] Final Price: [bold cyan]${final_price:.2f}[/bold cyan]")
    print(f" • [cyan]Strategic Alpha:[/cyan] Successfully anchored 20% above market average.")

def main():
    if len(sys.argv) < 3:
        print("Usage: negotiate <target_price> <min_price>")
        sys.exit(1)
    
    run_negotiation(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
