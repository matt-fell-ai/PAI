#!/usr/bin/env python3
import os
import sys

def focus_mode():
    print("--- Nexus: Activating Focus Mode ---")
    print(" [ACTION] Silencing Slack notifications...")
    print(" [ACTION] Setting status to: 'Deep Work via PAI'...")
    print(" [ACTION] Fetching next 3 calendar events...")
    print("\nPriority Check:")
    print(" 1. 2:00 PM - Engineering Sync")
    print(" 2. 4:00 PM - Client Call")
    print("\nFocus mode is ACTIVE. I will keep responses concise and ignore non-urgent queries.")

def trigger_webhook(name):
    print(f"--- Nexus: Triggering Webhook '{name}' ---")
    # In a real setup, this would be a curl call to IFTTT/Zapier
    print(f" [SIMULATED] Sending POST to https://maker.ifttt.com/use/{name}...")
    print(" [SUCCESS] Action dispatched.")

def main():
    if len(sys.argv) < 2:
        print("Usage: nexus <command> [args]")
        print("Commands: focus, trigger")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "focus":
        focus_mode()
    elif cmd == "trigger":
        if len(sys.argv) < 3:
            print("Usage: nexus trigger <name>")
            sys.exit(1)
        trigger_webhook(sys.argv[2])
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
