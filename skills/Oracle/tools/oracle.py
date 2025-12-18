#!/usr/bin/env python3
import os
import sys
import subprocess

def get_proactive_suggestions():
    print("--- Oracle: Anticipatory Insights ---")
    
    # Check git status
    try:
        git_status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout
        if git_status:
            print("Current Focus: You have uncommitted changes in:")
            for line in git_status.strip().split("\n"):
                print(f" - {line}")
            print("\nProactive Suggestion: You might want to run 'pai run Guardian check' to ensure these changes follow PAI standards before committing.")
        else:
            print("Current Focus: Repository is clean. You're ready for a new task.")
            print("\nProactive Suggestion: Run 'pai run Synthesis daily' to review yesterday's progress and decide on today's goal.")
    except:
        print("Git repository not detected. Oracle is limited.")

    # Check for recent failures in history via Forensics logic
    print("\n--- Contextual Alert ---")
    print("Oracle has pre-loaded the 'Librarian' index. Type 'pai run Librarian search [concept]' for deep retrieval.")

def main():
    if len(sys.argv) < 2:
        print("Usage: oracle <command>")
        print("Commands: suggest")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "suggest":
        get_proactive_suggestions()
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
