#!/usr/bin/env python3
import os
import sys

PAI_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SKILLS_DIR = os.path.join(PAI_ROOT, "skills")

def get_help(skill_name):
    print(f"--- Manual: Guided Walkthrough for '{skill_name}' ---")
    skill_path = os.path.join(SKILLS_DIR, skill_name)
    if not os.path.exists(skill_path):
        print(f"Error: Skill '{skill_name}' not found.")
        return

    skill_md = os.path.join(skill_path, "SKILL.md")
    if os.path.exists(skill_md):
        with open(skill_md, 'r') as f:
            print(f.read())
    else:
        print("Detailed guide not found for this skill. Try 'pai info [skill]'.")

def how_to(query):
    print(f"--- Manual: Custom 'How-To' for '{query}' ---")
    print(" [SYNTHESIZING] Scanning internal tools and history via Neural...")
    # Placeholder for semantic synthesis
    print(f"\n1. Run 'pai run Discovery scan' to verify your local environment.")
    print(f"2. Use 'pai run Alpha leads {query}' to identify initial opportunities.")
    print(f"3. Document your progress in 'History/' so I can learn from your style.")

def main():
    if len(sys.argv) < 2:
        print("Usage: manual help <skill> | manual how-to <query>")
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "help":
        if len(sys.argv) < 3:
            print("Please specify a skill.")
        else:
            get_help(sys.argv[2])
    elif cmd == "how-to":
        how_to(" ".join(sys.argv[2:]))
    else:
        print("Unknown manual command.")

if __name__ == "__main__":
    main()
