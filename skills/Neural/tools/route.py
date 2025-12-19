#!/usr/bin/env python3
import sys
import os
import json

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

def route(query):
    PAI_UI.panel(f"Analyzing query for semantic routing:\n\n[bold white]{query}[/bold white]", title="Neural: Semantic Router", style="blue")
    
    # Load all skill descriptions
    skills_dir = os.path.join(PAI_ROOT, "skills")
    manifest = []
    for skill in os.listdir(skills_dir):
        agents_md = os.path.join(skills_dir, skill, "agents.md")
        if os.path.exists(agents_md):
            with open(agents_md, "r") as f:
                manifest.append({"skill": skill, "description": f.read()})
    
    # Simple keyword-based ranking simulation (in place of real embeddings)
    ranked = []
    keywords = query.lower().split()
    for item in manifest:
        score = sum(1 for word in keywords if word in item["description"].lower())
        if score > 0:
            ranked.append((score, item["skill"]))
    
    ranked.sort(reverse=True)
    top_5 = [skill for score, skill in ranked[:5]]
    
    # If no matches, provide default core set
    if not top_5:
        top_5 = ["Memory", "Librarian", "Oracle", "Ego", "UFC"]

    rows = [[f"[bold yellow]{s}[/bold yellow]"] for s in top_5]
    PAI_UI.table("Activated Skills (IAS Strategy)", ["Skill"], rows, style="green")
    
    return top_5

def main():
    if len(sys.argv) < 2:
        print("Usage: pai run Neural route <query>")
        sys.exit(1)
    
    query = " ".join(sys.argv[1:])
    route(query)

if __name__ == "__main__":
    main()
