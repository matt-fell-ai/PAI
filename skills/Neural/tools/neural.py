#!/usr/bin/env python3
import os
import sys
import math
from collections import Counter

PAI_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
HISTORY_DIR = os.path.join(PAI_ROOT, "History")

def tokenize(text):
    return text.lower().split()

def search(query):
    print(f"--- Neural: Semantic Retrieval for '{query}' ---")
    
    query_tokens = tokenize(query)
    # Weights for conceptual matching (simulated embedding)
    concept_map = {
        "state": ["store", "reducer", "context", "history", "flow"],
        "auth": ["security", "oauth", "jwt", "login", "vault"],
        "api": ["rest", "endpoint", "request", "augment", "connector"]
    }
    
    expanded_query = list(query_tokens)
    for q in query_tokens:
        if q in concept_map:
            expanded_query.extend(concept_map[q])

    results = []
    for root, dirs, files in os.walk(PAI_ROOT):
        if any(d in root for d in [".git", "node_modules", ".claude"]):
            continue
        for f in files:
            if f.endswith(".md") or f.endswith(".py"):
                path = os.path.join(root, f)
                try:
                    with open(path, 'r', errors='ignore') as content:
                        text = content.read().lower()
                        # Simple TF-IDF like scoring
                        score = 0
                        for token in expanded_query:
                            count = text.count(token)
                            if count > 0:
                                score += (1 + math.log(count))
                        
                        if score > 0:
                            results.append((score, path))
                except:
                    continue

    results.sort(key=lambda x: x[0], reverse=True)
    
    if not results:
        print("No conceptual matches found.")
    else:
        for score, path in results[:5]:
            rel_path = os.path.relpath(path, PAI_ROOT)
            print(f" [IQ Score: {score:.2f}] {rel_path}")

def main():
    if len(sys.argv) < 3 or sys.argv[1] != "search":
        print("Usage: neural search <query>")
        sys.exit(1)
    search(" ".join(sys.argv[2:]))

if __name__ == "__main__":
    main()
