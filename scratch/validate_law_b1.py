# -*- coding: utf-8 -*-
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(__file__))

from curate_law_b1_p1a import CURATED_LAW_B1_P1A
from curate_law_b1_p1b import CURATED_LAW_B1_P1B
from validate_curate import validate_curated_dict

print(f"Part 1a words: {len(CURATED_LAW_B1_P1A)}")
print(f"Part 1b words: {len(CURATED_LAW_B1_P1B)}")

combined = {}
combined.update(CURATED_LAW_B1_P1A)
combined.update(CURATED_LAW_B1_P1B)

print(f"Total unique words in combined dictionary: {len(combined)}")

# Check against disk directories
base_dir = r"App database/Latin roots/Cluster Law"
dashboards = ['jud', 'jur', 'lic', 'litig']
all_dirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
dir_map = {}
for root in dashboards:
    matched = [d for d in all_dirs if d.split('—')[-1].strip() == root or d.endswith(' ' + root)][0]
    dir_map[root] = matched

total_disk = 0
missing = []
for root, dirname in dir_map.items():
    dp = os.path.join(base_dir, dirname)
    disk_words = sorted([f[:-3] for f in os.listdir(dp) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')])
    total_disk += len(disk_words)
    for w in disk_words:
        if w not in combined:
            missing.append((dirname, w))

print(f"Total disk words across 4 dashboards: {total_disk}")
if missing:
    print(f"MISSING WORDS ({len(missing)}): {missing}")

extra = [w for w in combined if not any(os.path.exists(os.path.join(base_dir, dirname, f"{w}.md")) for dirname in dir_map.values())]
if extra:
    print(f"EXTRA WORDS ({len(extra)}): {extra}")

ok = validate_curated_dict(combined, "Cluster Law Batch 1 Complete (142 words across jud, jur, lic, litig)")
if ok and not missing and not extra:
    print("\n🎉 ALL 142 WORDS OF CLUSTER LAW BATCH 1 ARE 100% VALIDATED AND READY TO APPLY!")
else:
    print("\n❌ VALIDATION OR WORD COUNT MISMATCH ENCOUNTERED.")
    sys.exit(1)
