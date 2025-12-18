#!/usr/bin/env python3
import os
import sys

def generate_mermaid(logic_type, description):
    print(f"--- Visionary: Generating {logic_type} Diagram ---")
    
    if logic_type == "sketch":
        # Placeholder for simple architecture sketch
        print("graph TD")
        print(f"    User --> |request| App")
        print(f"    App --> |query| DB[(Database)]")
        print(f"    App --> |process| Logic[{description}]")
    elif logic_type == "seq":
        print("sequenceDiagram")
        print(f"    participant User")
        print(f"    participant PAI")
        print(f"    User->>PAI: {description}")
        print(f"    PAI-->>User: Visual Result")
    else:
        print(f"graph TD\n    Start --> {description}")

    print("\n[TIP] Copy the code above into any Mermaid-compatible viewer (GitHub, Notion, Obsidian).")

def main():
    if len(sys.argv) < 3:
        print("Usage: visionary <type> <description>")
        print("Types: sketch, seq, mermaid")
        sys.exit(1)

    logic_type = sys.argv[1]
    description = " ".join(sys.argv[2:])
    generate_mermaid(logic_type, description)

if __name__ == "__main__":
    main()
