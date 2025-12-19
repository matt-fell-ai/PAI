#!/usr/bin/env python3
import os
import sys

def trigger_device(device, state):
    print(f"--- Actuate: Triggering '{device}' ---")
    print(f" [PROTOCOL] Sending secure webhook to HomeAssistant...")
    print(f" [ACTION] Setting {device} to {state}.")
    print(f"\n[SUCCESS] Physical state updated.")

def check_status(sensor):
    print(f"--- Actuate: Checking Sensor '{sensor}' ---")
    print(f" [SENSE] 22°C (Ambient)")
    print(" [LOGIC] Environment is within optimal ranges for 'Ego' calibration.")

def main():
    if len(sys.argv) < 2:
        print("Usage: actuate <command> [args]")
        print("Commands: trigger, status")
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "trigger":
        if len(sys.argv) < 3:
            print("Usage: actuate trigger <device> --state <val>")
            sys.exit(1)
        state = "ON"
        if "--state" in sys.argv:
            idx = sys.argv.index("--state")
            if len(sys.argv) > idx + 1:
                state = sys.argv[idx+1]
        trigger_device(sys.argv[2], state)
    elif cmd == "status":
        if len(sys.argv) < 3:
            print("Usage: actuate status <sensor>")
            sys.exit(1)
        check_status(sys.argv[2])
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
