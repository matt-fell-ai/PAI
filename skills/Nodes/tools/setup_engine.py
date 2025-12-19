#!/usr/bin/env python3
import sys
import os
import subprocess

PAI_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.join(PAI_ROOT, "bin", "lib"))

try:
    from ui import PAI_UI, console
except ImportError:
    class PAI_UI:
        @staticmethod
        def panel(c, t, s): print(f"--- {t} ---\n{c}")

def setup_engine():
    PAI_UI.panel("Initializing Sovereign Intelligence Engine Setup...", title="Nodes: 1.58-bit Engine", style="cyan")
    
    print("[bold white]1. Checking Dependencies (gcc, cmake)...[/bold white]")
    # Check for cmake
    try:
        subprocess.run(["cmake", "--version"], capture_output=True, check=True)
        print("✅ cmake found")
    except:
        print("❌ cmake not found. Please install: sudo apt install cmake")
        return

    print("\n[bold white]2. Preparing llama.cpp integration...[/bold white]")
    print("Due to high build times, this process should be run in a dedicated terminal.")
    print("Command: [bold yellow]pip install llama-cpp-python --prefer-binary[/bold yellow]")
    
    print("\n[bold white]3. Downloading BitNet b1.58 GGUF...[/bold white]")
    # Mock download logic
    model_dir = os.path.join(PAI_ROOT, "models")
    os.makedirs(model_dir, exist_ok=True)
    print(f"Target directory: {model_dir}")
    print("Recommended Model: [bold green]microsoft/bitnet-b1.58-2B-4T-GGUF[/bold green]")
    
    PAI_UI.panel("To complete setup, run the following commands manually:\n\n1. pip install llama-cpp-python\n2. pai run Nodes pull_model bitnet-b1.58-2b", title="Next Steps", style="blue")

def main():
    setup_engine()

if __name__ == "__main__":
    main()
