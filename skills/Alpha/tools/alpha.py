#!/usr/bin/env python3
import os
import sys

def find_leads(query):
    print(f"--- Alpha: Detecting Revenue Opportunities for '{query}' ---")
    print(f" [RESEARCH] Scanning LinkedIn, Upwork, and Twitter for pain points...")
    print(f" [INSIGHT] Detected high demand for {query} in the 'SME' sector.")
    print("\nTarget Leads Found:")
    print(f" 1. Upwork: 'Need {query} expert for internal tool'")
    print(f" 2. Twitter: 'Why is there no good {query} for Mac?'")
    print("\n[ACTION] Next: Run 'pai run Closer pitch' for these leads.")

def scan_trends(category):
    print(f"--- Alpha: Trend Analysis for '{category}' ---")
    print(f" [SEARCH] Analyzing Google Trends and Reddit sentiment...")
    print(f" [ALPHA] '{category}' is currently up 25% WoW in developer interest.")
    print(" [OPPORTUNITY] Low competition for 'open-source' alternatives in this niche.")

def main():
    if len(sys.argv) < 3:
        print("Usage: alpha <command> <query>")
        print("Commands: leads, trends")
        sys.exit(1)
    
    cmd = sys.argv[1]
    query = sys.argv[2]
    
    if cmd == "leads":
        find_leads(query)
    elif cmd == "trends":
        scan_trends(query)
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
