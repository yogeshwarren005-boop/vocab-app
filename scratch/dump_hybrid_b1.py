import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

target_root = 'App database/Latin roots/Cluster Greek-Latin Hybrid'
dashboards = [
    'Dashboard — hier',     # 19
    'Dashboard — scop',     # 27
    'Dashboard — cosm',     # 31
    'Dashboard — nom_law',  # 34
    'Dashboard — theo',     # 38
]

words_by_dash = {}
all_words = []
for d in dashboards:
    p = os.path.join(target_root, d)
    files = sorted([f[:-3] for f in os.listdir(p) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')])
    words_by_dash[d] = files
    all_words.extend(files)
    print(f"{d}: {len(files)} words")

print(f"Total Batch 1 words: {len(all_words)}")
json.dump({"by_dashboard": words_by_dash, "words": all_words}, open('scratch/hybrid_b1_words.json', 'w', encoding='utf-8'), indent=2)
