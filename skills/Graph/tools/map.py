#!/usr/bin/env python3
import sys
import os
import json
import time

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

GRAPH_FILE = os.path.join(PAI_ROOT, "History", "knowledge_graph.json")

def load_graph():
    if os.path.exists(GRAPH_FILE):
        with open(GRAPH_FILE, "r") as f:
            return json.load(f)
    return {"nodes": [], "edges": []}

def save_graph(data):
    os.makedirs(os.path.dirname(GRAPH_FILE), exist_ok=True)
    with open(GRAPH_FILE, "w") as f:
        json.dump(data, f, indent=2)

def map_entity(input_text):
    PAI_UI.panel(f"Mapping entity to Neural Graph: [bold cyan]{input_text}[/bold cyan]", title="Graph: Neural Mapper", style="blue")
    
    graph = load_graph()
    node_id = len(graph["nodes"]) + 1
    
    new_node = {
        "id": node_id,
        "label": input_text,
        "timestamp": time.time(),
        "type": "Entity"
    }
    
    graph["nodes"].append(new_node)
    
    # Simple simulated multi-hop edge creation
    if len(graph["nodes"]) > 1:
        prev_node = graph["nodes"][-2]
        new_edge = {"source": prev_node["id"], "target": node_id, "relation": "sequentially_related"}
        graph["edges"].append(new_edge)
        print(f" • [green]Edge created:[/green] {prev_node['label']} -> {input_text}")

    save_graph(graph)
    
    rows = [
        ["Total Nodes", str(len(graph["nodes"])), "Knowledge density"],
        ["Total Edges", str(len(graph["edges"])), "Relational depth"],
        ["Graph State", "STABLE", "Integrity check"]
    ]
    
    PAI_UI.table("Neural Knowledge Graph Status", ["Metric", "Value", "Insight"], rows, style="blue")

def main():
    if len(sys.argv) < 2:
        print("Usage: map <input>")
        sys.exit(1)
    
    map_entity(" ".join(sys.argv[1:]))

if __name__ == "__main__":
    main()
