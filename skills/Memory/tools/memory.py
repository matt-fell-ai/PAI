#!/usr/bin/env python3
import os
import sys
import json
import time
from datetime import datetime

# Path resolution: find PAI_DIR or fallback to parent of 'bin'
PAI_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
MEMORY_FILE = os.path.join(PAI_ROOT, "memory.json")

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r') as f:
            return json.load(f)
    return []

def save_memory(data):
    with open(MEMORY_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def store(fact):
    memory = load_memory()
    entry = {
        "id": int(time.time()),
        "timestamp": datetime.now().isoformat(),
        "content": fact
    }
    memory.append(entry)
    save_memory(memory)
    print(f"Stored: {fact}")

def search(query):
    memory = load_memory()
    results = [m for m in memory if query.lower() in m["content"].lower()]
    if not results:
        print(f"No results found for '{query}'.")
    for r in results:
        print(f"[{r['timestamp']}] {r['content']}")

def list_all():
    memory = load_memory()
    if not memory:
        print("Memory is empty.")
    for r in memory:
        print(f"[{r['timestamp']}] {r['content']}")

def main():
    if len(sys.argv) < 2:
        print("Usage: memory <command> [args]")
        print("Commands: store, search, list")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "store":
        if len(sys.argv) < 3:
            print("Usage: memory store <fact>")
            sys.exit(1)
        store(" ".join(sys.argv[2:]))
    elif cmd == "search":
        if len(sys.argv) < 3:
            print("Usage: memory search <query>")
            sys.exit(1)
        search(sys.argv[2])
    elif cmd == "list":
        list_all()
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()
