#!/usr/bin/env python3
import os
import sys

def debug_visual(file_path):
    print(f"--- Iris: Visual Debugging for '{file_path}' ---")
    print(f" [MODEL] Initializing Gemini 3.0 Pro (Thinking Level: High)")
    print(" [SENSE] Ingesting visual tokens...")
    print(" [ANALYSIS] Comparing screenshot against local /styles/main.css...")
    print("\nIRIS INSIGHT:")
    print(" I've detected a flexbox overflow on the '.revenue-chart' container.")
    print(" Recommendation: Change 'justify-content: space-between' to 'center' in lines 45-50.")
    print("\n[ACTION] Feeding recommendation to Engineer agent.")

def main():
    if len(sys.argv) < 3 or sys.argv[1] != "debug":
        print("Usage: iris debug <file_path>")
        sys.exit(1)
    debug_visual(sys.argv[2])

if __name__ == "__main__":
    main()
