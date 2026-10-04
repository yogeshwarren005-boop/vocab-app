import os, sys

sys.stdout.reconfigure(encoding="utf-8")

speed_dir = r"App database\Latin roots\Cluster Movement & Speed"
dashboards = [d for d in os.listdir(speed_dir) if os.path.isdir(os.path.join(speed_dir, d)) and d.startswith("Dashboard — ")]

all_dash_words = {}
for d in dashboards:
    d_path = os.path.join(speed_dir, d)
    words = {f for f in os.listdir(d_path) if f.endswith(".md") and not f.startswith("Dashboard — ")}
    all_dash_words[d] = words

print("Checking pairwise overlaps within Cluster Movement & Speed:")
for i in range(len(dashboards)):
    for j in range(i + 1, len(dashboards)):
        d1, d2 = dashboards[i], dashboards[j]
        common = all_dash_words[d1].intersection(all_dash_words[d2])
        if common:
            print(f"  {d1} <-> {d2}: {len(common)} words")
            if len(common) <= 5:
                print(f"    {common}")
