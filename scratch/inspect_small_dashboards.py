import os, sys
sys.stdout.reconfigure(encoding="utf-8")

c_path = r"App database\Latin roots\Cluster Action & State"
small_dashboards = ["Dashboard — licent", "Dashboard — oscul", "Dashboard — iter", "Dashboard — torp", "Dashboard — unct", "Dashboard — ira", "Dashboard — joc"]

for d in small_dashboards:
    d_path = os.path.join(c_path, d)
    words = [f for f in os.listdir(d_path) if f.endswith(".md") and not f.startswith("Dashboard — ")]
    print(f"=== {d} ({len(words)} words) ===")
    print(", ".join(sorted(words)))
