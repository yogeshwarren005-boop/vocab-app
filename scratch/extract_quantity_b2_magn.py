# -*- coding: utf-8 -*-
import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

cluster_path = "App database/Latin roots/Cluster Quantity"
magn_dir = os.path.join(cluster_path, "Dashboard — magn")
magn_words = sorted([f[:-3] for f in os.listdir(magn_dir) if f.endswith(".md") and not f.startswith("Dashboard") and not f.startswith("Word Triage")])

print(f"Total words in magn: {len(magn_words)}")
print(magn_words)

with open("scratch/quantity_b2_magn_words.json", "w", encoding="utf-8") as f:
    json.dump(magn_words, f, ensure_ascii=False, indent=2)
