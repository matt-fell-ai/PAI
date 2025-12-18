#!/usr/bin/env python3
import os
import sys
import subprocess

def validate(target):
    print(f"--- Engine: Validating Asset '{target}' ---")
    
    gates = [
        ("Lint Check", ["python3", "-m", "py_compile", target] if target.endswith(".py") else None),
        ("Security Scan", ["grep", "-r", "sk-", target]), # Simple secret check
        ("Complexity Gate", ["wc", "-l", target]) # Placeholder for complexity analysis
    ]
    
    all_passed = True
    for name, cmd in gates:
        if cmd:
            print(f" Running {name}...", end=" ", flush=True)
            # Grep logic inverted: if it finds a secret, it fails
            if "Security" in name:
                res = subprocess.run(cmd, capture_output=True)
                if res.returncode == 0:
                    print("❌ FAIL (Secret Detected)")
                    all_passed = False
                else:
                    print("✅ PASS")
            else:
                res = subprocess.run(cmd, capture_output=True)
                if res.returncode == 0:
                    print("✅ PASS")
                else:
                    print("❌ FAIL")
                    all_passed = False

    if all_passed:
        print("\n[RESULT] Verification Successful. Asset is ready for Main.")
    else:
        print("\n[RESULT] Verification FAILED. Fix issues before proceeding.")

def main():
    if len(sys.argv) < 3 or sys.argv[1] != "validate":
        print("Usage: engine validate <file>")
        sys.exit(1)
    validate(sys.argv[2])

if __name__ == "__main__":
    main()
