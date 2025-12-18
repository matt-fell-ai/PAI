#!/usr/bin/env python3
import os
import sys
from datetime import datetime, timedelta

PAI_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
HISTORY_DIR = os.path.join(PAI_ROOT, "History")

def get_files_for_period(days=1):
    files = []
    cutoff = datetime.now() - timedelta(days=days)
    
    # We search in Sessions, Learnings, and Execution
    search_dirs = [
        os.path.join(HISTORY_DIR, "Sessions"),
        os.path.join(HISTORY_DIR, "Learnings"),
        os.path.join(HISTORY_DIR, "Execution", "Features")
    ]
    
    for base_dir in search_dirs:
        if not os.path.exists(base_dir):
            continue
        for root, dirs, filenames in os.walk(base_dir):
            for f in filenames:
                if f.endswith(".md"):
                    path = os.path.join(root, f)
                    mtime = datetime.fromtimestamp(os.path.getmtime(path))
                    if mtime > cutoff:
                        files.append(path)
    return files

def daily_synthesis():
    print(f"--- Daily Synthesis Report ({datetime.now().strftime('%Y-%m-%d')}) ---")
    files = get_files_for_period(1)
    if not files:
        print("No recent history found to synthesize.")
        return

    print(f"Found {len(files)} recent history entries.")
    print("\n--- CONTENT PREVIEW ---")
    for f in files:
        print(f"\n>> Source: {os.path.basename(f)}")
        with open(f, 'r') as content:
            # Read first 500 chars for preview
            print(content.read(500) + "...")

    print("\n--- NEXT STEPS ---")
    print("Agent: Please apply the 'summarize' and 'extract_wisdom' Fabric patterns to the content above to generate the final briefing.")

def main():
    if len(sys.argv) < 2:
        print("Usage: synthesis <command>")
        print("Commands: daily, weekly")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "daily":
        daily_synthesis()
    elif cmd == "weekly":
        files = get_files_for_period(7)
        print(f"Weekly report found {len(files)} entries. (Logic similar to daily)")
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()
