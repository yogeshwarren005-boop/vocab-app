# -*- coding: utf-8 -*-
import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

cluster_path = "App database/Latin roots/Cluster Quantity"
batch1b_dashboards = [
    "Dashboard — numer",
    "Dashboard — larg",
    "Dashboard — tot",
]

words_by_dash = {}
all_words_b1b = []

for d in batch1b_dashboards:
    dpath = os.path.join(cluster_path, d)
    files = sorted([f[:-3] for f in os.listdir(dpath) if f.endswith(".md") and not f.startswith("Dashboard") and not f.startswith("Word Triage")])
    words_by_dash[d] = files
    all_words_b1b.extend(files)

print(f"Total words in Batch 1B: {len(all_words_b1b)}")
for d, ws in words_by_dash.items():
    print(f"{d} ({len(ws)}): {ws}")

with open("scratch/quantity_b1b_words.json", "w", encoding="utf-8") as f:
    json.dump(all_words_b1b, f, ensure_ascii=False, indent=2)

with open("scratch/quantity_b1b_by_dash.json", "w", encoding="utf-8") as f:
    json.dump(words_by_dash, f, ensure_ascii=False, indent=2)
