#!/usr/bin/env python3
import os
import sys

def draft_pitch(lead, product):
    print(f"--- Closer: Drafting Personalized Pitch for {lead} ---")
    print(f" [ANALYSIS] lead likes: 'open source', 'concise code' (via Librarian)")
    print(f" [DRAFT] Hi {lead}, I saw your post about {product}. I've built a PAI module that solves exactly this...")
    print("\nDraft ready. Run 'pai run Nexus trigger slack-send' to deliver.")

def main():
    if "--lead" not in sys.argv or "--product" not in sys.argv:
        print("Usage: closer pitch --lead <name> --product <desc>")
        sys.exit(1)
    
    lead = sys.argv[sys.argv.index("--lead") + 1]
    product = sys.argv[sys.argv.index("--product") + 1]
    
    draft_pitch(lead, product)

if __name__ == "__main__":
    main()
