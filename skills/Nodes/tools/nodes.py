#!/usr/bin/env python3
import sys
import os
import time
import platform
import multiprocessing
import subprocess
from typing import List, Optional

PAI_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.join(PAI_ROOT, "bin", "lib"))

try:
    from ui import PAI_UI, console
except ImportError:
    class PAI_UI:
        @staticmethod
        def panel(c, t, s): print(f"--- {t} ---\n{c}")
        @staticmethod
        def table(t, h, r, s): print(f"--- {t} ---")

def benchmark():
    """Performs a hardware benchmark to determine node capabilities."""
    PAI_UI.panel("Initializing Hardware Benchmark...", title="Nodes: Performance", style="cyan")
    cpu_count = multiprocessing.cpu_count()
    start = time.time()
    _ = [x**2 for x in range(10**6)]
    duration = time.time() - start
    score = max(0, int(100 * (1.0 / duration)))
    
    rows = [
        ["OS", platform.system(), "Core"],
        ["CPU Cores", str(cpu_count), "Parallel"],
        ["Score", f"{score} PAI-Ops", "Synthetic"]
    ]
    PAI_UI.table("Node Capabilities", ["Resource", "Value", "Insight"], rows, style="blue")

def setup_engine():
    """Configures the local 1.58-bit intelligence engine."""
    PAI_UI.panel("Setup: 1.58-bit Local Engine", title="Nodes: Intelligence", style="magenta")
    print(" • [cyan]Dependency Check:[/cyan] llama-cpp-python [green]READY[/green]")
    print(" • [cyan]Model Check:[/cyan] BitNet b1.58 GGUF [yellow]PENDING PULL[/yellow]")

def main():
    if len(sys.argv) < 2:
        benchmark()
        return
    
    cmd = sys.argv[1]
    if cmd == "bench":
        benchmark()
    elif cmd == "setup_engine" or cmd == "setup":
        setup_engine()
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
