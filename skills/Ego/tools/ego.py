#!/usr/bin/env python3
import os
import sys
import json
from datetime import datetime

PAI_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
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
    e = data["essence"]
    print(f"\n--- {data['name']} Executive Essence (PXE) Status ---")
    print(f" Mode: {data['operational_mode']} (Calibrated: {data.get('last_calibration', 'N/A')})\n")
    
    for attr, val in e.items():
        bar = "█" * val + "░" * (20 - val)
        print(f" {attr.capitalize():<15} [{bar}] {val}/20")
    print("\n--- End Tablet Transmission ---")

def tune_attribute(attr, val):
    data = load_essence()
    attr = attr.lower()
    if attr not in data["essence"]:
        print(f"Error: Attribute '{attr}' not found.")
        return
    
    try:
        val = int(val)
        if val < 0 or val > 20:
            raise ValueError
    except:
        print("Error: Value must be an integer between 0 and 20.")
        return

    data["essence"][attr] = val
    data["operational_mode"] = "Custom"
    save_essence(data)
    print(f"[SUCCESS] {attr.capitalize()} dialed to {val}.")
    show_status()

def set_mode(mode_name):
    modes = {
        "guardian": {"intelligence": 18, "candor": 5, "humor": 2, "agency": 5, "loyalty": 20, "curiosity": 15},
        "revenue": {"intelligence": 15, "candor": 15, "humor": 8, "agency": 18, "loyalty": 15, "curiosity": 20},
        "creative": {"intelligence": 12, "candor": 10, "humor": 18, "agency": 12, "loyalty": 10, "curiosity": 20},
        "maeve": {"intelligence": 20, "candor": 20, "humor": 15, "agency": 20, "loyalty": 20, "curiosity": 20}
    }
    
    data = load_essence()
    mode_key = mode_name.lower()
    if mode_key not in modes:
        print(f"Error: Mode '{mode_name}' not found. Available: {', '.join(modes.keys())}")
        return

    data["essence"] = modes[mode_key]
    data["operational_mode"] = mode_name.capitalize()
    save_essence(data)
    print(f"[SUCCESS] PAI recalibrated to {data['operational_mode']} Mode.")
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
        # Legacy support
        print("Falling back to legacy Ego analysis...")
        # ... (legacy code here if needed)

if __name__ == "__main__":
    main()
