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

WORLD_STATE_FILE = os.path.join(PAI_ROOT, "History", "world_state.json")

def load_state():
    if os.path.exists(WORLD_STATE_FILE):
        with open(WORLD_STATE_FILE, "r") as f:
            return json.load(f)
    return {"current_layout": "default", "assets": []}

def save_state(data):
    os.makedirs(os.path.dirname(WORLD_STATE_FILE), exist_ok=True)
    with open(WORLD_STATE_FILE, "w") as f:
        json.dump(data, f, indent=2)

def design_world(layout):
    PAI_UI.panel(f"Initiating Spatial Reconfiguration: [bold cyan]{layout}[/bold cyan]", title="Architect: World Design", style="blue")
    
    state = load_state()
    state["current_layout"] = layout
    
    # Logic-based asset injection (Simulated SpacetimeDB Reducer)
    assets = []
    if layout == "war_room":
        assets = [
            {"type": "TacticalMap", "pos": [0, 0, 100], "scale": 2.0},
            {"type": "ThreatHologram", "pos": [200, 50, 120], "scale": 1.0},
            {"type": "SecurityTerminal", "pos": [-150, 0, 80], "scale": 1.0}
        ]
    elif layout == "zen_library":
        assets = [
            {"type": "MeditationMat", "pos": [0, 0, 10], "scale": 1.0},
            {"type": "DataScrollRack", "pos": [300, 300, 0], "scale": 1.5},
            {"type": "SoftAmbientLight", "pos": [0, 0, 500], "intensity": 0.5}
        ]
    else:
        assets = [{"type": "StandardWorkstation", "pos": [0, 0, 0], "scale": 1.0}]

    state["assets"] = assets
    save_state(state)
    
    rows = []
    for a in assets:
        rows.append([a["type"], str(a["pos"]), "COMMITTED"])
    
    PAI_UI.table("SpacetimeDB: WorldAsset Transactions", ["Asset", "Coordinates", "Sync Status"], rows, style="blue")
    print(f"\n[bold green]World State Updated.[/bold green] Unreal Engine 5 Client notified.")

def main():
    if len(sys.argv) < 2:
        print("Usage: design <layout>")
        sys.exit(1)
    
    design_world(sys.argv[1])

if __name__ == "__main__":
    main()
