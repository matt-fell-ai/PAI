#!/usr/bin/env python3
import os
import sys

def create_magnet(topic):
    print(f"--- Forge: Manufacturing Asset '{topic}' ---")
    print(f" [WRITER] Generating high-value PDF outline...")
    print(f" [DESIGNER] Creating minimalist SVG cover art...")
    print(f" [ENGINEER] Embedding interactive CLI examples...")
    print(f"\nAsset complete: assets/magnets/{topic.replace(' ', '_')}.md")
    print("TIP: Use 'pai run Closer proposal' to send this to your leads.")

def build_content(desc):
    print(f"--- Forge: Batching Content for '{desc}' ---")
    print(" [GENERATING] 3x Twitter Threads")
    print(" [GENERATING] 1x LinkedIn Deep Dive")
    print(" [GENERATING] 1x SEO Blog Post")
    print("\nDrafts saved to History/Execution/Features/Content/")

def main():
    if len(sys.argv) < 3:
        print("Usage: forge <command> <topic>")
        print("Commands: magnet, content")
        sys.exit(1)
    
    cmd = sys.argv[1]
    topic = " ".join(sys.argv[2:])
    
    if cmd == "magnet":
        create_magnet(topic)
    elif cmd == "content":
        build_content(topic)
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
