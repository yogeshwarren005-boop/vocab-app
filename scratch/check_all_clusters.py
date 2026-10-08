# -*- coding: utf-8 -*-
import os
import subprocess
import json

base_path = "App database/Latin roots"
clusters = sorted([d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d)) and d.startswith("Cluster")])

results = []

for c in clusters:
    c_path = os.path.join(base_path, c)
    # count total md files excluding Dashboard and Word Triage
    total_words = 0
    dashboards = [d for d in os.listdir(c_path) if os.path.isdir(os.path.join(c_path, d)) and d.startswith("Dashboard")]
    for d in dashboards:
        d_path = os.path.join(c_path, d)
        files = [f for f in os.listdir(d_path) if f.endswith(".md") and not f.startswith("Dashboard") and not f.startswith("Word Triage")]
        total_words += len(files)
    results.append({"cluster": c, "dashboards": len(dashboards), "words": total_words})

results.sort(key=lambda x: x["words"])

with open("scratch/cluster_sizes.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"Total clusters: {len(results)}")
for r in results:
    print(f"{r['cluster']}: {r['words']} words ({r['dashboards']} dashboards)")
