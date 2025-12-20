#!/usr/bin/env python3
import asyncio
import sys
import os
import json
import time
from datetime import datetime

PAI_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.join(PAI_ROOT, "bin", "lib"))

try:
    from ui import PAI_UI, console
except ImportError:
    class PAI_UI:
        @staticmethod
        def panel(c, t, s): print(f"--- {t} ---\n{c}")
        @staticmethod
        def essence_bars(d): print(f"Essence: {d['essence']}")

ESSENCE_FILE = os.path.join(PAI_ROOT, "essence.json")
MEMORY_FILE = os.path.join(PAI_ROOT, "History", "ego_memory.json")

CONTEXT_MAP = {
    "negotiation": {"intelligence": 18, "candor": 15, "humor": 2, "agency": 18, "loyalty": 10, "curiosity": 5},
    "brainstorming": {"intelligence": 12, "candor": 10, "humor": 18, "agency": 10, "loyalty": 15, "curiosity": 20},
    "emergency": {"intelligence": 20, "candor": 5, "humor": 0, "agency": 20, "loyalty": 20, "curiosity": 10},
    "social": {"intelligence": 10, "candor": 12, "humor": 15, "agency": 8, "loyalty": 18, "curiosity": 15},
    "research": {"intelligence": 18, "candor": 8, "humor": 5, "agency": 12, "loyalty": 15, "curiosity": 20}
}

class EgoStream:
    """
    1000x Evolution: AutonomousEgo
    - Contextual Morphing: Changes personality based on situation.
    - Meta-Cognition: Learns from successful interactions.
    - Smooth Transition: Gradual attribute shifting.
    """
    
    def __init__(self):
        self.data = self.load_essence()
        self.memory = self.load_memory()

    def load_essence(self):
        if os.path.exists(ESSENCE_FILE):
            with open(ESSENCE_FILE, 'r') as f:
                return json.load(f)
        return {"name": "PAI", "essence": {k: 10 for k in ["intelligence", "candor", "humor", "agency", "loyalty", "curiosity"]}, "operational_mode": "Standard"}

    def load_memory(self):
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, 'r') as f:
                return json.load(f)
        return {"success_history": []}

    async def morph_attribute(self, attr, target):
        current = self.data["essence"].get(attr, 10)
        step = 1 if target > current else -1
        
        while current != target:
            current += step
            self.data["essence"][attr] = current
            # In a real CLI we would update a live display here
            await asyncio.sleep(0.05) # 50ms per step for "Smooth Transition"
        
    async def recalibrate(self, context):
        PAI_UI.panel(f"Analyzing Vibe & Objective for context: [bold cyan]{context}[/bold cyan]...", title="Ego: Meta-Cognition", style="magenta")
        
        target_essence = CONTEXT_MAP.get(context.lower())
        if not target_essence:
            print(f"Unknown context '{context}'. Falling back to Standard optimization.")
            target_essence = {k: 10 for k in self.data["essence"]}

        # Meta-Cognitive Adjustment: Check memory for 'Best Outcomes'
        relevant_memory = [m for m in self.memory["success_history"] if m["context"] == context]
        if relevant_memory:
            best_mode = max(relevant_memory, key=lambda x: x["score"])
            print(f" • [green]Memory Hit:[/green] Adjusting based on past successful '{context}' session (Score: {best_mode['score']}).")
            # Slight bias towards best historical values
            for k in target_essence:
                target_essence[k] = int((target_essence[k] + best_mode["essence"][k]) / 2)

        PAI_UI.panel("Commencing Smooth Personality Transition...", title="Ego: Morphing Attributes", style="blue")
        
        tasks = [self.morph_attribute(attr, val) for attr, val in target_essence.items()]
        await asyncio.gather(*tasks)
        
        self.data["operational_mode"] = f"Optimized-{context.capitalize()}"
        self.data["last_calibration"] = datetime.now().isoformat()
        
        with open(ESSENCE_FILE, 'w') as f:
            json.dump(self.data, f, indent=2)
            
        PAI_UI.essence_bars(self.data)
        print(f"\n[bold green]RECALIBRATION COMPLETE:[/bold green] Node synced to [cyan]{context}[/cyan] requirements.")

    def record_success(self, context, score):
        # Simulated performance tracking
        entry = {
            "timestamp": datetime.now().isoformat(),
            "context": context,
            "essence": self.data["essence"],
            "score": score
        }
        self.memory["success_history"].append(entry)
        os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
        with open(MEMORY_FILE, 'w') as f:
            json.dump(self.memory, f, indent=2)
        print(f" • [magenta]Meta-Cognition:[/magenta] Performance of {score}/100 recorded for future optimization.")

async def main():
    context = sys.argv[1] if len(sys.argv) > 1 else "research"
    stream = EgoStream()
    await stream.recalibrate(context)
    # Simulate a successful interaction for learning
    stream.record_success(context, 92)

if __name__ == "__main__":
    asyncio.run(main())
