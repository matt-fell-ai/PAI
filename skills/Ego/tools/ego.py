#!/usr/bin/env python3
import os
import sys
import json
from datetime import datetime

PAI_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.join(PAI_ROOT, "bin", "lib"))

try:
    from ui import PAI_UI, console
except ImportError:
    # Fallback if UI lib not found
    class PAI_UI:
        @staticmethod
        def essence_bars(data):
            print(f"--- {data['name']} Essence ---")
            for k, v in data['essence'].items():
                print(f" {k}: {v}/20")
        @staticmethod
        def error(msg): print(f"Error: {msg}")
        @staticmethod
        def tip(msg): print(f"Tip: {msg}")

ESSENCE_FILE = os.path.join(PAI_ROOT, "essence.json")

def load_essence():
    if os.path.exists(ESSENCE_FILE):
        with open(ESSENCE_FILE, 'r') as f:
            return json.load(f)
    return {
        "name": "PAI",
        "essence": {"intelligence": 10, "candor": 10, "humor": 10, "agency": 10, "loyalty": 10, "curiosity": 10},
        "operational_mode": "Standard"
    }

def save_essence(data):
    data["last_calibration"] = datetime.now().strftime("%Y-%m-%d")
    with open(ESSENCE_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def show_status():
    data = load_essence()
    PAI_UI.essence_bars(data)

def tune_attribute(attr, val):
    data = load_essence()
    attr = attr.lower()
    if attr not in data["essence"]:
        PAI_UI.error(f"Attribute '{attr}' not found.")
        return
    
    try:
        val = int(val)
        if val < 0 or val > 20:
            raise ValueError
    except:
        PAI_UI.error("Value must be an integer between 0 and 20.")
        return

    data["essence"][attr] = val
    data["operational_mode"] = "Custom"
    save_essence(data)
    PAI_UI.tip(f"{attr.capitalize()} dialed to {val}.")
    show_status()

def set_mode(mode_name):
    modes = {
        "guardian": {"intelligence": 18, "candor": 5, "humor": 2, "agency": 5, "loyalty": 20, "curiosity": 15},
        "revenue": {"intelligence": 15, "candor": 15, "humor": 8, "agency": 18, "loyalty": 15, "curiosity": 20},
        "creative": {"intelligence": 12, "candor": 10, "humor": 18, "agency": 12, "loyalty": 10, "curiosity": 20},
        "maeve": {"intelligence": 20, "candor": 20, "humor": 15, "agency": 20, "loyalty": 20, "curiosity": 20},
        "standard": {"intelligence": 10, "candor": 10, "humor": 10, "agency": 10, "loyalty": 10, "curiosity": 10}
    }
    
    data = load_essence()
    mode_key = mode_name.lower()
    if mode_key not in modes:
        PAI_UI.error(f"Mode '{mode_name}' not found.")
        return

    data["essence"] = modes[mode_key]
    data["operational_mode"] = mode_name.capitalize()
    save_essence(data)
    PAI_UI.tip(f"PAI recalibrated to {data['operational_mode']} Mode.")
    show_status()

def main():
    if len(sys.argv) < 2:
        print("Usage: ego status | ego dial <attr> <val> | ego calibrate <mode>")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "status":
        show_status()
    elif cmd == "dial":
        if len(sys.argv) < 4:
            print("Usage: ego dial <attr> <val>")
            sys.exit(1)
        tune_attribute(sys.argv[2], sys.argv[3])
    elif cmd == "calibrate":
        if len(sys.argv) < 3:
            print("Usage: ego calibrate <mode>")
            sys.exit(1)
        set_mode(sys.argv[2])
    else:
        # Legacy support/fallback
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
