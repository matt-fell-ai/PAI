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

def refine(content, constraints):
    PAI_UI.panel(f"Refining content against constraints:\n\n[dim]{constraints}[/dim]", title="Arbiter: Iterative Refinement", style="magenta")
    
    # In a real IAS implementation, this would trigger a hidden LLM call
    # with a prompt designed to critique the content.
    # Here we simulate the "Refinement Loop".
    
    critique = f"SIMULATED CRITIQUE: Content is 85% aligned. Missing precision in step 2."
    refined_content = content + "\n\n[REFINED]: Added precision to step 2 as per Arbiter critique."
    
    PAI_UI.panel(f"[bold green]Critique:[/bold green] {critique}\n\n[bold white]Refined Output:[/bold white]\n{refined_content}", title="Refinement Complete", style="green")
    
    return refined_content

def main():
    if len(sys.argv) < 3:
        print("Usage: pai run Arbiter refine <content> <constraints>")
        sys.exit(1)
    
    content = sys.argv[1]
    constraints = sys.argv[2]
    refine(content, constraints)

if __name__ == "__main__":
    main()
