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
        @staticmethod
        def table(t, h, r, s): print(f"--- {t} ---")

def audit(target):
    # Simulated high-speed risk audit
    risks = [
        {"area": "Privacy", "level": "HIGH", "detail": "Data sharing with third-party aggregators detected in telemetry strings."},
        {"area": "Liability", "level": "MEDIUM", "detail": "Indemnification clause is overly broad; user assumes total project risk."},
        {"area": "Intellectual Property", "level": "LOW", "detail": "License ambiguity in vendor dependencies."},
        {"area": "Compliance", "level": "INFO", "detail": "GDPR-ready structures detected."}
    ]
    
    rows = []
    for r in risks:
        color = "red" if r["level"] == "HIGH" else "yellow" if r["level"] == "MEDIUM" else "green" if r["level"] == "LOW" else "blue"
        rows.append([r["area"], f"[{color}]{r['level']}[/{color}]", r["detail"]])
    
    PAI_UI.panel(f"Auditing target: [bold cyan]{target}[/bold cyan]", title="Counsel: Risk Audit", style="blue")
    PAI_UI.table("Risk Assessment Matrix", ["Area", "Severity", "Insight"], rows, style="red")

def main():
    if len(sys.argv) < 2:
        print("Usage: audit <target>")
        sys.exit(1)
    
    audit(sys.argv[1])

if __name__ == "__main__":
    main()
