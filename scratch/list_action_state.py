import os, sys, subprocess
sys.stdout.reconfigure(encoding="utf-8")

c_path = r"App database\Latin roots\Cluster Action & State"
dashboards = [d for d in os.listdir(c_path) if os.path.isdir(os.path.join(c_path, d)) and d.startswith("Dashboard — ")]

print(f"Cluster Action & State: {len(dashboards)} dashboards")

for d in sorted(dashboards):
    d_path = os.path.join(c_path, d)
    words = [f for f in os.listdir(d_path) if f.endswith(".md") and not f.startswith("Dashboard — ")]
    print(f"  {d}: {len(words)} words")
