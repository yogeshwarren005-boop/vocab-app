import os
import json
import subprocess

with open("scratch/fac_remaining_107.json", "r", encoding="utf-8") as f:
    remaining = json.load(f)

cluster_dir = r"App database\Latin roots\Cluster Action"
other_dashboards = [d for d in os.listdir(cluster_dir) if d.startswith("Dashboard — ") and d != "Dashboard — fac"]

graftable = {}

for fname in remaining:
    found = []
    for d in other_dashboards:
        other_path = os.path.join(cluster_dir, d, fname)
        if os.path.exists(other_path):
            found.append(other_path)
    if found:
        graftable[fname] = found

print(f"Remaining {len(remaining)} words: {len(graftable)} found in sibling dashboards!")
for k, v in graftable.items():
    print(f"  {k} -> {v}")
