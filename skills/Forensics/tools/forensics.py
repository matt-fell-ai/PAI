#!/usr/bin/env python3
import os
import sys
import json
from datetime import datetime

PAI_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
RAW_LOGS_DIR = os.path.join(PAI_ROOT, "History", "Raw-Outputs")

def get_latest_log():
    if not os.path.exists(RAW_LOGS_DIR):
        return None
    
    all_logs = []
    for root, dirs, files in os.walk(RAW_LOGS_DIR):
        for f in files:
            if f.endswith(".jsonl"):
                all_logs.append(os.path.join(root, f))
    
    if not all_logs:
        return None
    return max(all_logs, key=os.path.getmtime)

def analyze_failures():
    log_file = get_latest_log()
    if not log_file:
        print("No execution logs found to analyze.")
        return

    print(f"Analyzing log: {os.path.basename(log_file)}")
    failures = []
    with open(log_file, 'r') as f:
        for line in f:
            try:
                entry = json.loads(line)
                # Check for common failure indicators in tool outputs
                output = str(entry.get("output", ""))
                if "Error" in output or "failed" in output or "exit code: 1" in output:
                    failures.append(entry)
            except json.JSONDecodeError:
                continue

    if not failures:
        print("No obvious failures detected in the latest session.")
        return

    print(f"\nDetected {len(failures)} failure events:")
    for i, fail in enumerate(failures[-5:]): # Show last 5
        print(f"\n[{i+1}] Tool: {fail.get('tool')}")
        print(f"    Command: {fail.get('input', {}).get('command', 'N/A')}")
        print(f"    Error Snippet: {str(fail.get('output'))[:200]}...")

    print("\n--- FORENSICS INSIGHT ---")
    # Simple logic to check for repeated tool failures
    tool_counts = {}
    for fail in failures:
        t = fail.get('tool')
        tool_counts[t] = tool_counts.get(t, 0) + 1
    
    for tool, count in tool_counts.items():
        if count > 2:
            print(f" [!] REPEATED FAILURE: The tool '{tool}' failed {count} times. Consider checking its configuration or prompt constraints.")

def main():
    if len(sys.argv) < 2:
        print("Usage: forensics <command>")
        print("Commands: debug")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "debug":
        analyze_failures()
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()
