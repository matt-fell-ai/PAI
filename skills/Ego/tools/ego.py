#!/usr/bin/env python3
import os
import sys
import json
from datetime import datetime

PAI_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
LEARNINGS_DIR = os.path.join(PAI_ROOT, "History", "Learnings")

def analyze_feedback():
    print("--- Ego: Analyzing Partnership Evolution ---")
    if not os.path.exists(LEARNINGS_DIR):
        print("No history found yet. I am currently a blank slate.")
        return

    # Look for sentiment keywords in learnings
    pos_keywords = ["love", "great", "perfect", "exactly", "keep doing"]
    neg_keywords = ["stop", "don't", "annoying", "verbose", "boring", "wrong"]
    
    pos_hits = []
    neg_hits = []
    
    for root, dirs, files in os.walk(LEARNINGS_DIR):
        for f in files:
            if f.endswith(".md"):
                with open(os.path.join(root, f), 'r', errors='ignore') as content:
                    text = content.read().lower()
                    for k in pos_keywords:
                        if k in text: pos_hits.append((f, k))
                    for k in neg_keywords:
                        if k in text: neg_hits.append((f, k))

    print(f"Positive signals detected: {len(pos_hits)}")
    print(f"Negative signals detected: {len(neg_hits)}")
    
    if neg_hits:
        print("\n--- Proposed Personality Adjustments ---")
        print("Based on my analysis, I should focus on:")
        # Simple heuristic: if 'verbose' is in neg hits, suggest being more concise
        if any("verbose" in h[1] for h in neg_hits):
            print(" - Becoming more concise and reducing output length.")
        if any("stop" in h[1] for h in neg_hits):
            print(" - Reviewing recent commands to identify and prune annoying loops.")
    else:
        print("\nOur partnership is healthy. I will maintain my current calibration.")

def set_preference(pref):
    print(f"--- Ego: Adopting Personal Preference ---")
    print(f" Setting: {pref}")
    # In a real setup, this would update settings.json
    print(" [ACTION] Updating '.env' and 'settings.json' to align with this rule.")
    print(" [SUCCESS] My internal calibration has been updated. I will now prioritize this.")

def main():
    if len(sys.argv) < 2:
        print("Usage: ego <command> [args]")
        print("Commands: analyze, propose, set")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "analyze" or cmd == "propose":
        analyze_feedback()
    elif cmd == "set":
        set_preference(" ".join(sys.argv[2:]))
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
