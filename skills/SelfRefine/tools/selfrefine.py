#!/usr/bin/env python3
import os
import sys

PAI_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SKILLS_DIR = os.path.join(PAI_ROOT, "skills")

def audit_skills():
    print("--- SelfRefine: Skill System Audit ---")
    skills = [s for s in os.listdir(SKILLS_DIR) if os.path.isdir(os.path.join(SKILLS_DIR, s))]
    
    issues = []
    for skill in skills:
        skill_path = os.path.join(SKILLS_DIR, skill)
        # Check for SKILL.md
        if not os.path.exists(os.path.join(skill_path, "SKILL.md")):
            issues.append(f" [!] {skill}: Missing SKILL.md (Claude Code won't find it)")
        
        # Check for tools/
        if not os.path.exists(os.path.join(skill_path, "tools")):
            issues.append(f" [!] {skill}: Missing tools/ directory")
        
        # Check for workflows/
        if not os.path.exists(os.path.join(skill_path, "workflows")):
            issues.append(f" [?] {skill}: Missing workflows/ (Recommended for structure)")

    if not issues:
        print(" [OK] All skills follow canonical PAI structure.")
    else:
        for issue in issues:
            print(issue)

def suggest_improvements():
    print("\n--- Improvement Suggestions ---")
    print("1. Migration: Move TS-based hooks to use 'pai' CLI bridge for universal access.")
    print("2. Documentation: Add 'USE WHEN' triggers to any community skills lacking them.")
    print("3. Performance: The 'Guardian' skill could be parallelized using the Task tool.")

def main():
    if len(sys.argv) < 2:
        print("Usage: selfrefine <command>")
        print("Commands: audit, suggest")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "audit":
        audit_skills()
    elif cmd == "suggest":
        suggest_improvements()
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()
