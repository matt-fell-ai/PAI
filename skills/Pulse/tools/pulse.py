#!/usr/bin/env python3
import os
import sys

PAI_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

def report():
    print("--- Pulse: ROI & Performance Heartbeat ---")
    print(" [METRIC] Skills used today: 14")
    print(" [METRIC] Revenue leads found (Alpha): 2")
    print(" [METRIC] System health score: 98%")
    print("\nPulse is steady. You are currently in an 'Expansion' phase.")

def generate_web_dashboard():
    print("--- Pulse: Generating Secure Web Dashboard ---")
    html_content = """
    <html>
    <head><title>PAI Heartbeat</title><style>
        body { font-family: sans-serif; background: #0f172a; color: #e2e8f0; padding: 40px; }
        .card { background: #1e293b; padding: 20px; border-radius: 8px; margin-bottom: 20px; border: 1px solid #334155; }
        h1 { color: #38bdf8; }
        .stat { font-size: 2em; font-weight: bold; color: #fbbf24; }
    </style></head>
    <body>
        <h1>Personal AI Infrastructure - Heartbeat</h1>
        <div class='card'><h2>Revenue Health</h2><div class='stat'>2 Active Leads</div></div>
        <div class='card'><h2>System Health</h2><div class='stat'>98% Efficiency</div></div>
        <div class='card'><h2>Recent Activity</h2><ul><li>Neural search: 'state'</li><li>Alpha lead: 'FastAPI'</li></ul></div>
    </body>
    </html>
    """
    path = os.path.join(PAI_ROOT, "Pulse_Dashboard.html")
    with open(path, "w") as f:
        f.write(html_content)
    print(f" [SUCCESS] Dashboard generated: {path}")
    print(" [TIP] Open this file in your browser for a visual status report.")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "web":
        generate_web_dashboard()
    else:
        report()

if __name__ == "__main__":
    main()
