#!/usr/bin/env python3
import os
import sys
import re

PAI_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
HISTORY_DIR = os.path.join(PAI_ROOT, "History")

def search(query):
    print(f"--- Librarian: Searching Knowledge Base for '{query}' ---")
    
    # Simple semantic mapping (placeholders for a vector store)
    synonyms = {
        "auth": ["authentication", "login", "oauth", "jwt", "security"],
        "api": ["endpoint", "rest", "request", "server"],
        "ui": ["frontend", "css", "html", "design", "layout"]
    }
    
    keywords = [query.lower()]
    for key, vals in synonyms.items():
        if key in query.lower():
            keywords.extend(vals)
    
    results = []
    for root, dirs, files in os.walk(PAI_ROOT):
        # Skip noisy dirs
        if any(d in root for d in [".git", "node_modules", ".claude"]):
            continue
            
        for f in files:
            if f.endswith(".md") or f.endswith(".py") or f.endswith(".ts"):
                path = os.path.join(root, f)
                try:
                    with open(path, 'r', errors='ignore') as content:
                        text = content.read().lower()
                        score = sum(1 for k in keywords if k in text)
                        if score > 0:
                            results.append((score, path))
                except:
                    continue

    results.sort(key=lambda x: x[0], reverse=True)
    
    if not results:
        print("No relevant context found.")
    else:
        for score, path in results[:5]: # Top 5
            rel_path = os.path.relpath(path, PAI_ROOT)
            print(f" [Score: {score}] {rel_path}")

def main():
    if len(sys.argv) < 3 or sys.argv[1] != "search":
        print("Usage: librarian search <query>")
        sys.exit(1)
    
    search(" ".join(sys.argv[2:]))

if __name__ == "__main__":
    main()
