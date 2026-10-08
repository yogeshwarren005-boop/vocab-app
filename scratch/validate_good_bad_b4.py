# -*- coding: utf-8 -*-
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(__file__))

from curate_good_bad_b4_p1a import CURATED_GOOD_BAD_B4_P1A
from curate_good_bad_b4_p1b import CURATED_GOOD_BAD_B4_P1B
from curate_good_bad_b4_p2a import CURATED_GOOD_BAD_B4_P2A
from curate_good_bad_b4_p2b import CURATED_GOOD_BAD_B4_P2B
from validate_curate import validate_curated_dict

print(f"Part 1a words: {len(CURATED_GOOD_BAD_B4_P1A)}")
print(f"Part 1b words: {len(CURATED_GOOD_BAD_B4_P1B)}")
print(f"Part 2a words: {len(CURATED_GOOD_BAD_B4_P2A)}")
print(f"Part 2b words: {len(CURATED_GOOD_BAD_B4_P2B)}")

combined = {}
combined.update(CURATED_GOOD_BAD_B4_P1A)
combined.update(CURATED_GOOD_BAD_B4_P1B)
combined.update(CURATED_GOOD_BAD_B4_P2A)
combined.update(CURATED_GOOD_BAD_B4_P2B)

print(f"Total unique words in combined dictionary: {len(combined)}")

# Check against disk directories
base_dir = r"App database/Latin roots/Cluster Good & Bad"
dashboards = ['pecc', 'prav', 'pur', 'suav', 'van']
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

print(f"Total disk words across 5 dashboards: {total_disk}")
if missing:
    print(f"MISSING WORDS ({len(missing)}): {missing}")

extra = [w for w in combined if not any(os.path.exists(os.path.join(base_dir, dirname, f"{w}.md")) for dirname in dir_map.values())]
if extra:
    print(f"EXTRA WORDS ({len(extra)}): {extra}")

ok = validate_curated_dict(combined, "Cluster Good & Bad Batch 4 Complete (142 words across pecc, prav, pur, suav, van)")
if ok and not missing and not extra:
    print("\n🎉 ALL 142 WORDS OF BATCH 4 ARE 100% VALIDATED AND READY TO APPLY!")
else:
    print("\n❌ VALIDATION OR WORD COUNT MISMATCH ENCOUNTERED.")
    sys.exit(1)
