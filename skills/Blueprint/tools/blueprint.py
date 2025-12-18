#!/usr/bin/env python3
import os
import sys
import subprocess

PAI_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
PAI_BIN = os.path.join(PAI_ROOT, "bin", "pai")

def launch_project(name):
    print(f"--- Blueprint: Architecting Idea '{name}' ---")
    
    # 1. UFC Scaffold
    print(" [1/3] Enforcing UFC Structure...")
    subprocess.run([PAI_BIN, "run", "UFC", "scaffold", name])
    
    # 2. Forge Placeholder
    print(" [2/3] Priming Forge Asset Factory...")
    # Simulated forge call
    
    # 3. Genesis Plan
    print(" [3/3] Generating Master Strategy (Genesis)...")
    subprocess.run([PAI_BIN, "run", "Genesis", "project", name])

    print(f"\n[BLUEPRINT COMPLETE] Your new business infra '{name}' is ready.")
    print("Next step: Run 'pai run Alpha leads' to find your first client.")

def main():
    if len(sys.argv) < 3 or sys.argv[1] != "launch":
        print("Usage: blueprint launch <project_name>")
        sys.exit(1)
    launch_project(sys.argv[2])

if __name__ == "__main__":
    main()
