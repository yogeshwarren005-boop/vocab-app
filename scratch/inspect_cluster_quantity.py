# -*- coding: utf-8 -*-
import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

cluster_path = "App database/Latin roots/Cluster Quantity"
dashboards = sorted([d for d in os.listdir(cluster_path) if os.path.isdir(os.path.join(cluster_path, d)) and d.startswith("Dashboard")])

total_files = 0
dash_breakdown = []

for d in dashboards:
    dpath = os.path.join(cluster_path, d)
    files = sorted([f[:-3] for f in os.listdir(dpath) if f.endswith(".md") and not f.startswith("Dashboard") and not f.startswith("Word Triage")])
    total_files += len(files)
    dash_breakdown.append({
        "dashboard": d,
        "count": len(files),
        "sample": files[:5]
    })

print(f"Cluster Quantity: {total_files} words across {len(dashboards)} dashboards:\n")
for item in dash_breakdown:
    print(f"- {item['dashboard']}: {item['count']} words ({', '.join(item['sample'])}...)")

with open("scratch/quantity_dashboards.json", "w", encoding="utf-8") as f:
    json.dump(dash_breakdown, f, ensure_ascii=False, indent=2)
