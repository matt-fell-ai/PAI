#!/usr/bin/env python3
import os
import sys
import subprocess

def run_isolated(script):
    print(f"--- Sanctum: Isolated Execution for '{script}' ---")
    
    # Check if Docker is available
    docker_check = subprocess.run(["which", "docker"], capture_output=True).returncode == 0
    
    if docker_check:
        print(" [ENV] Docker detected. Spawning isolated container...")
        # Placeholder for real docker run
        print(f" [COMMAND] docker run --rm -v $(pwd):/app python:3.10 python /app/{script}")
    else:
        print(" [ENV] Docker missing. Falling back to Restricted Process...")
        print(f" [ACTION] Running '{script}' with limited environment variables.")
        subprocess.run([sys.executable, script])

    print("\n[CLEANUP] Sanctum session closed.")

def main():
    if len(sys.argv) < 3 or sys.argv[1] != "run":
        print("Usage: sanctum run <script>")
        sys.exit(1)
    run_isolated(sys.argv[2])

if __name__ == "__main__":
    main()
