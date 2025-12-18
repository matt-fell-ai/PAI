#!/usr/bin/env python3
import os
import sys

PAI_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SKILLS_DIR = os.path.join(PAI_ROOT, "skills")

def sideload_skill(skill_name):
    skill_path = os.path.join(SKILLS_DIR, skill_name)
    if not os.path.exists(skill_path):
        print(f"Error: Skill '{skill_name}' not found.")
        return

    print(f"--- Sideloading Skill: {skill_name} ---")
    print(f"Loading from: {skill_path}")
    print("\n[CONTEXT START]")
    
    # Read SKILL.md
    skill_md = os.path.join(skill_path, "SKILL.md")
    if os.path.exists(skill_md):
        with open(skill_md, 'r') as f:
            lines = f.readlines()
            # Only include the first 50 lines or key sections
            print("".join(lines[:50]))
            if len(lines) > 50:
                print("... [truncated for efficiency]")

    # List Tools
    tools_dir = os.path.join(skill_path, "tools")
    if os.path.exists(tools_dir):
        print("\nAVAILABLE TOOLS:")
        for t in os.listdir(tools_dir):
            print(f" - {t}")
            
    print("\n[CONTEXT END]")

def main():
    if len(sys.argv) < 3:
        print("Usage: sideload skill <skill_name>")
        sys.exit(1)
    
    if sys.argv[1] == "skill":
        sideload_skill(sys.argv[2])
    else:
        print("Unsupported command.")

if __name__ == "__main__":
    main()
