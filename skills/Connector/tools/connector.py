#!/usr/bin/env python3
import os
import sys
import subprocess

def check_github_notifications():
    print("Checking GitHub Notifications...")
    try:
        result = subprocess.run(["gh", "api", "notifications"], capture_output=True, text=True)
        if result.returncode == 0:
            notifications = result.stdout
            if not notifications or notifications == "[]":
                print("No new notifications.")
            else:
                print(notifications)
        else:
            print("Error: Could not fetch notifications. Are you logged in to 'gh'?")
    except FileNotFoundError:
        print("Error: 'gh' command not found.")

def main():
    if len(sys.argv) < 2:
        print("Usage: connector <command>")
        print("Commands: check, sync, schedule (placeholder)")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "check":
        check_github_notifications()
    elif cmd == "sync":
        print("Syncing with remote... (Running git push/pull)")
        subprocess.run(["git", "pull"])
        subprocess.run(["git", "push"])
    elif cmd == "schedule":
        print("Schedule functionality requires Google/Outlook API setup.")
        print(f"Proposed: {' '.join(sys.argv[2:])}")
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()
