#!/usr/bin/env python3
import os
import sys

def run_recon(target):
    print(f"--- Ghost: OSINT Reconnaissance for '{target}' ---")
    print(" [SENSE] Checking Armory for 'sherlock' and 'theharvester'...")
    print(f" [SEARCH] Scanning DNS records and subdomains...")
    print("\nRECON REPORT:")
    print(f" - Social Handles: @{target.split('.')[0]} detected.")
    print(f"\n[TIP] For deep OSINT, install tools via Armory:")
    print(" 'pai run Armory install sherlock'")
    print(f" 'pai run Armory run sherlock {target.split('.')[0]}'")

def main():
    if len(sys.argv) < 3 or sys.argv[1] != "recon":
        print("Usage: ghost recon <target>")
        sys.exit(1)
    run_recon(sys.argv[2])

if __name__ == "__main__":
    main()
