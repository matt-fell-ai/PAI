#!/usr/bin/env python3
import asyncio
import sys
import os
import json
from datetime import datetime
from typing import Dict, Any, Optional

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
        @staticmethod
        def error(m): print(f"Error: {m}")
        @staticmethod
        def tip(m): print(f"Tip: {m}")

ESSENCE_FILE = os.path.join(PAI_ROOT, "essence.json")
MEMORY_FILE = os.path.join(PAI_ROOT, "History", "ego_memory.json")

def load_essence():
    if os.path.exists(ESSENCE_FILE):
        with open(ESSENCE_FILE, 'r') as f:
            return json.load(f)
    return {"name": "PAI", "essence": {k: 10 for k in ["intelligence", "candor", "humor", "agency", "loyalty", "curiosity"]}, "operational_mode": "Standard"}

def save_essence(data):
    data["last_calibration"] = datetime.now().isoformat()
    with open(ESSENCE_FILE, 'w') as f:
        json.dump(data, f, indent=2)

async def morph_attribute(data, attr, target):
    current = data["essence"].get(attr, 10)
    if current == target: return
    step = 1 if target > current else -1
    while current != target:
        current += step
        data["essence"][attr] = current
        await asyncio.sleep(0.02)

async def recalibrate(context: str):
    """The 1000x Ego-Stream recalibration logic."""
    PAI_UI.panel(f"Recalibrating for context: [bold cyan]{context}[/bold cyan]", title="Ego: Meta-Cognition", style="magenta")
    
    modes = {
        "negotiation": {"intelligence": 18, "candor": 15, "humor": 2, "agency": 18, "loyalty": 10, "curiosity": 5},
        "brainstorming": {"intelligence": 12, "candor": 10, "humor": 18, "agency": 10, "loyalty": 15, "curiosity": 20},
        "emergency": {"intelligence": 20, "candor": 5, "humor": 0, "agency": 20, "loyalty": 20, "curiosity": 10},
        "standard": {"intelligence": 10, "candor": 10, "humor": 10, "agency": 10, "loyalty": 10, "curiosity": 10}
    }
    
    target = modes.get(context.lower(), modes["standard"])
    data = load_essence()
    
    tasks = [morph_attribute(data, attr, val) for attr, val in target.items()]
    await asyncio.gather(*tasks)
    
    data["operational_mode"] = f"Optimized-{context.capitalize()}"
    save_essence(data)
    PAI_UI.essence_bars(data)

def tune_attribute(attr: str, val: str):
    data = load_essence()
    if attr.lower() not in data["essence"]:
        PAI_UI.error(f"Attribute '{attr}' not found.")
        return
    data["essence"][attr.lower()] = int(val)
    data["operational_mode"] = "Custom"
    save_essence(data)
    PAI_UI.tip(f"{attr.capitalize()} set to {val}.")
    PAI_UI.essence_bars(data)

async def async_main():
    if len(sys.argv) < 2:
        print("Usage: ego status | ego dial <attr> <val> | ego recalibrate <context>")
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "status":
        PAI_UI.essence_bars(load_essence())
    elif cmd == "dial":
        if len(sys.argv) < 4:
            print("Usage: ego dial <attr> <val>")
            sys.exit(1)
        tune_attribute(sys.argv[2], sys.argv[3])
    elif cmd == "recalibrate":
        context = sys.argv[2] if len(sys.argv) > 2 else "standard"
        await recalibrate(context)
    elif cmd == "calibrate": # Legacy alias
        context = sys.argv[2] if len(sys.argv) > 2 else "standard"
        await recalibrate(context)
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    asyncio.run(async_main())
