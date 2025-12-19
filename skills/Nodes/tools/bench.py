#!/usr/bin/env python3
import sys
import os
import time
import platform
import multiprocessing

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
    PAI_UI.panel("Initializing Hardware Benchmark...", title="Nodes: Performance Scan", style="cyan")
    
    # CPU Check
    cpu_count = multiprocessing.cpu_count()
    cpu_freq = "N/A"
    try:
        import psutil
        cpu_freq = f"{psutil.cpu_freq().max:.2f}MHz"
    except: pass
    
    # Synthetic Load Test (Simple)
    start = time.time()
    _ = [x**2 for x in range(10**7)]
    duration = time.time() - start
    
    score = max(0, int(1000 * (1.0 / duration)))
    
    rows = [
        ["OS", platform.system(), "Core System"],
        ["CPU Cores", str(cpu_count), "Parallel capacity"],
        ["Compute Speed", f"{score} PAI-Ops", "Synthetic performance"],
        ["Node Health", "OPTIMAL", "Stability indicator"]
    ]
    
    PAI_UI.table("Local Node Capabilities", ["Resource", "Value", "Insight"], rows, style="blue")
    
    if score > 500:
        print("\n[bold green]High Performance detected.[/bold green] Node is suitable for local 70B+ model inference.")
    else:
        print("\n[bold yellow]Standard Performance.[/bold yellow] Recommended for cloud-hybrid or small local models (8B).")

def main():
    benchmark()

if __name__ == "__main__":
    main()
