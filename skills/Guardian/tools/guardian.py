#!/usr/bin/env python3
import os
import sys
import subprocess
import re

PAI_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

def check_secrets():
    print("Scanning for potential secrets...")
    # Very basic regex for common secret patterns (just for demo)
    patterns = [
        r"sk-[a-zA-Z0-9]{48}", # OpenAI
        r"AIza[0-9A-Za-z-_]{35}", # Google
        r"\"[a-zA-Z0-9]{40}\"" # Generic hex-like
    ]
    found = False
    for root, dirs, files in os.walk(PAI_ROOT):
        if ".git" in root: continue
        for f in files:
            if f.endswith(".md") or f.endswith(".py") or f.endswith(".sh"):
                path = os.path.join(root, f)
                with open(path, 'r', errors='ignore') as content:
                    text = content.read()
                    for p in patterns:
                        if re.search(p, text):
                            print(f" [!] Potential secret found in {path}")
                            found = True
    if not found:
        print(" [OK] No secrets detected.")

def check_paths():
    print("Checking for hardcoded home paths (should use ${PAI_DIR})...")
    # Search for things like /Users/ or /home/
    found = False
    for root, dirs, files in os.walk(PAI_ROOT):
        if ".git" in root or "History" in root: continue
        for f in files:
            if f.endswith(".md") or f.endswith(".py") or f.endswith(".ts"):
                path = os.path.join(root, f)
                with open(path, 'r', errors='ignore') as content:
                    text = content.read()
                    if "/Users/" in text or "/home/" in text:
                        if "${PAI_DIR}" not in text:
                             print(f" [!] Hardcoded path found in {path}")
                             found = True
    if not found:
        print(" [OK] Paths are standardized.")

def main():
    if len(sys.argv) < 2:
        print("Usage: guardian <command>")
        print("Commands: check, secure")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "check" or cmd == "secure":
        check_secrets()
        check_paths()
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()
