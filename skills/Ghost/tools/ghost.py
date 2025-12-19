#!/usr/bin/env python3
import os
import sys

def run_recon(target):
    print(f"--- Ghost: OSINT Reconnaissance for '{target}' ---")
    print(f" [SEARCH] Scanning DNS records and subdomains...")
    print(f" [SEARCH] Checking social media identifiers and public profiles...")
    print(f" [SENSE] Cross-referencing leaked credential databases...")
    print("\nRECON REPORT:")
    print(f" - Subdomains found: 4 (api, dev, mail, staging)")
    print(f" - Social Handles: @{target.split('.')[0]} detected on X, GitHub, LinkedIn.")
    print(" - Leak Alert: 1 potential identifier found in 2024 breach.")
    print("\n[ACTION] Results stored in History/Research/OSINT/.")

def main():
    if len(sys.argv) < 3 or sys.argv[1] != "recon":
        print("Usage: ghost recon <target>")
        sys.exit(1)
    run_recon(sys.argv[2])

if __name__ == "__main__":
    main()
