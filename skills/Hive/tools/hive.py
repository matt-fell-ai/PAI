#!/usr/bin/env python3
import sys
import os
import json
import time
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

BLACKBOARD_FILE = os.path.join(PAI_ROOT, "History", "hive_blackboard.json")

def load_blackboard():
    if os.path.exists(BLACKBOARD_FILE):
        with open(BLACKBOARD_FILE, "r") as f:
            return json.load(f)
    return {"task": "", "status": "Initializing", "contributions": []}

def save_blackboard(data):
    os.makedirs(os.path.dirname(BLACKBOARD_FILE), exist_ok=True)
    with open(BLACKBOARD_FILE, "w") as f:
        json.dump(data, f, indent=2)

def agent_worker(agent_id, skill, command, args):
    # Simulated agent contribution
    time.sleep(2)
    contribution = {
        "agent_id": agent_id,
        "skill": skill,
        "contribution": f"Executed {skill}:{command} with results for task.",
        "timestamp": time.time()
    }
    return contribution

def orchestrate(task):
    PAI_UI.panel(f"Initializing Hive for task: [bold cyan]{task}[/bold cyan]", title="Hive: Orchestrator", style="yellow")
    
    bb = {"task": task, "status": "In Progress", "contributions": []}
    save_blackboard(bb)
    
    # We spawn 3 parallel agents
    agents = [
        (1, "Ghost", "recon", [task]),
        (2, "Alpha", "leads", [task]),
        (3, "Counsel", "audit", [task])
    ]
    
    with multiprocessing.Pool(processes=3) as pool:
        results = pool.starmap(agent_worker, agents)
    
    bb["contributions"] = results
    bb["status"] = "Completed"
    save_blackboard(bb)
    
    rows = []
    for c in results:
        rows.append([f"Agent {c['agent_id']}", c['skill'], c['contribution']])
    
    PAI_UI.table("Hive Contribution Summary", ["Agent", "Skill", "Result"], rows, style="yellow")
    print("\n[bold green]Hive task completed. Blackboard updated.[/bold green]")

def main():
    if len(sys.argv) < 2:
        print("Usage: orchestrate <task>")
        sys.exit(1)
    
    orchestrate(" ".join(sys.argv[1:]))

if __name__ == "__main__":
    main()
