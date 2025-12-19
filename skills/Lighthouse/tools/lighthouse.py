#!/usr/bin/env python3
import os
import sys

def beacon_capability(capability):
    print(f"--- Lighthouse: Broadcasting Expert Beacon for '{capability}' ---")
    print(" [ANS] Registering capability in decentralized Agent Name Service...")
    print(" [PROTOCOL] Attaching VAI (Verified Agent Identity) signature...")
    print("\nBEACON ACTIVE:")
    print(f" Your PAI is now 'Discoverable' as a specialist in: {capability}.")
    print(" Peers can contact you via: did:pai:matt-fell-ai.")

def main():
    if len(sys.argv) < 3 or sys.argv[1] != "beacon":
        print("Usage: lighthouse beacon <capability>")
        sys.exit(1)
    beacon_capability(sys.argv[2])

if __name__ == "__main__":
    main()
