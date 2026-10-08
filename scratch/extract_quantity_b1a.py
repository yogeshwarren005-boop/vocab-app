# -*- coding: utf-8 -*-
import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

cluster_path = "App database/Latin roots/Cluster Quantity"
batch1a_dashboards = [
    "Dashboard — pauc",
    "Dashboard — copi",
    "Dashboard — cresc",
    "Dashboard — null",
    "Dashboard — omni",
    "Dashboard — ampl",
    "Dashboard — rar",
    "Dashboard — plen",
    "Dashboard — plet",
]

words_by_dash = {}
all_words_b1a = []

for d in batch1a_dashboards:
    dpath = os.path.join(cluster_path, d)
    files = sorted([f[:-3] for f in os.listdir(dpath) if f.endswith(".md") and not f.startswith("Dashboard") and not f.startswith("Word Triage")])
    words_by_dash[d] = files
    all_words_b1a.extend(files)

print(f"Total words in Batch 1A: {len(all_words_b1a)}")
for d, ws in words_by_dash.items():
    print(f"{d} ({len(ws)}): {ws}")

with open("scratch/quantity_b1a_words.json", "w", encoding="utf-8") as f:
    json.dump(all_words_b1a, f, ensure_ascii=False, indent=2)

with open("scratch/quantity_b1a_by_dash.json", "w", encoding="utf-8") as f:
    json.dump(words_by_dash, f, ensure_ascii=False, indent=2)
