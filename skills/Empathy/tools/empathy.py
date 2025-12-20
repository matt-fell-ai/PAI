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
        def tip(m): print(f"Tip: {m}")

def sync():
    # Simulated sentiment analysis of History/ logs
    sentiment = "Stressed/Urgent"
    suggested_changes = [
        ("Intelligence", 18, "Maximize precision"),
        ("Candor", 5, "Softened feedback"),
        ("Humor", 2, "Professional focus"),
        ("Agency", 5, "Wait for explicit confirmation"),
        ("Loyalty", 20, "Maximum support"),
        ("Curiosity", 10, "Focus on current task")
    ]
    
    output = f"Detected User Sentiment: [bold red]{sentiment}[/bold red]\n\n"
    output += "Suggested PXE Essence Recalibration:\n"
    for attr, val, reason in suggested_changes:
        output += f" • [bold yellow]{attr}[/bold yellow] -> {val} ({reason})\n"
    
    PAI_UI.panel(output, title="Empathy: Affective Sync", style="pink1")
    PAI_UI.tip("Run 'pai run Ego calibrate guardian' or 'pai run Ego dial <attr> <val>' to apply.")

def main():
    sync()

if __name__ == "__main__":
    main()
