#!/usr/bin/env python3
import os
import sys

def scaffold_project(name):
    print(f"--- UFC: Scaffolding Project '{name}' ---")
    dirs = ["Knowledge", "Methodology", "Tools", "Tasks"]
    project_path = os.path.join(os.getcwd(), name.replace(" ", "_"))
    
    try:
        os.makedirs(project_path, exist_ok=True)
        for d in dirs:
            os.makedirs(os.path.join(project_path, d), exist_ok=True)
            # Create a placeholder index
            with open(os.path.join(project_path, d, "README.md"), 'w') as f:
                f.write(f"# {d}\nProject: {name}")
        
        # Create master CONTEXT.md
        with open(os.path.join(project_path, "CONTEXT.md"), 'w') as f:
            f.write(f"# {name} - Single Source of Truth\n\n## Methodology\nLinked to CORE/Methodology.md")
            
        print(f"\nScaffold complete at: {project_path}")
        print("Hierarchy established: Knowledge, Methodology, Tools, Tasks.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) < 3 or sys.argv[1] != "scaffold":
        print("Usage: ufc scaffold <project_name>")
        sys.exit(1)
    scaffold_project(sys.argv[2])

if __name__ == "__main__":
    main()
