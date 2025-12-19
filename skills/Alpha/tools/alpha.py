#!/usr/bin/env python3
import os
import sys

PAI_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.join(PAI_ROOT, "bin", "lib"))

try:
    from ui import PAI_UI, console
except ImportError:
    class PAI_UI:
        @staticmethod
        def table(t, c, r, s): print(f"--- {t} ---")
        @staticmethod
        def panel(c, t, s): print(f"--- {t} ---\n{c}")

def find_leads(query):
    rows = [
        ["Upwork", f"Need {query} expert for internal tool", "[bold red]HOT[/bold red]"],
        ["Twitter", f"Why is there no good {query} for Mac?", "[bold yellow]WARM[/bold yellow]"],
        ["LinkedIn", f"Staff Engineer looking for {query} solutions", "[bold blue]COLD[/bold blue]"]
    ]
    PAI_UI.table(f"Target Leads: {query}", ["Source", "Description", "Heat"], rows, style="orange3")

def scan_trends(category):
    content = f"""
[bold cyan]Metric:[/bold cyan] Developer Interest
[bold cyan]Growth:[/bold cyan] +25% WoW
[bold cyan]Sentiment:[/bold cyan] [green]Strong Positive[/green]

[dim]Current market saturation is LOW for open-source alternatives in this niche.[/dim]
"""
    PAI_UI.panel(content, title=f"Trend Analysis: {category}", style="orange3")

def main():
    if len(sys.argv) < 3:
        print("Usage: alpha <command> <query>")
        sys.exit(1)
    
    cmd = sys.argv[1]
    query = sys.argv[2]
    
    if cmd == "leads":
        find_leads(query)
    elif cmd == "trends":
        scan_trends(query)
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
