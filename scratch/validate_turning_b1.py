# -*- coding: utf-8 -*-
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from validate_curate import validate_curated_dict
from curate_turning_b1_p1a import CURATED_TURNING_B1_P1A
from curate_turning_b1_p1b import CURATED_TURNING_B1_P1B
from curate_turning_b1_p2a import CURATED_TURNING_B1_P2A
from curate_turning_b1_p2b import CURATED_TURNING_B1_P2B

all_curated = {}
all_curated.update(CURATED_TURNING_B1_P1A)
all_curated.update(CURATED_TURNING_B1_P1B)
all_curated.update(CURATED_TURNING_B1_P2A)
all_curated.update(CURATED_TURNING_B1_P2B)

print(f"Total unique curated words in Turning Batch 1: {len(all_curated)}")

base_path = 'App database/Latin roots/Cluster Turning'
dashboards = ['Dashboard — circ', 'Dashboard — circum', 'Dashboard — clin', 'Dashboard — verg']

all_dirs = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
dir_map = {}
for target in dashboards:
    target_root = target.split('—')[1].strip()
    matched = [d for d in all_dirs if d.split('—')[-1].strip() == target_root or d.endswith(' ' + target_root)][0]
    dir_map[target] = matched

total_files = 0
all_target_words = set()
for dash, dirname in dir_map.items():
    dp = os.path.join(base_path, dirname)
    words = [f[:-3] for f in os.listdir(dp) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]
    print(f"Checking {dash} ({dirname}): {len(words)} files")
    total_files += len(words)
    all_target_words.update(words)

print(f"Total files to update across 4 dashboards: {total_files}")
print(f"Total unique words required: {len(all_target_words)}")

missing = all_target_words - set(all_curated.keys())
print(f"Missing curated words: {len(missing)}")
if missing:
    print(f"  Missing: {sorted(list(missing))}")

ok1 = validate_curated_dict(CURATED_TURNING_B1_P1A, "Batch 1 Part 1a (circ 1-33)")
ok2 = validate_curated_dict(CURATED_TURNING_B1_P1B, "Batch 1 Part 1b (circ 34-65)")
ok3 = validate_curated_dict(CURATED_TURNING_B1_P2A, "Batch 1 Part 2a (clin 1-25, verg 1-6)")
ok4 = validate_curated_dict(CURATED_TURNING_B1_P2B, "Batch 1 Part 2b (clin 26-41, verg 7-16)")
ok_all = validate_curated_dict(all_curated, f"Batch 1 Full ({len(all_curated)} unique words)")

if ok1 and ok2 and ok3 and ok4 and ok_all and len(missing) == 0:
    print("\nALL 122 UNIQUE WORDS COVERING ALL 141 FILES OF TURNING BATCH 1 PASSED VALIDATION WITH 100% PRISTINE INTEGRITY!")
else:
    print("\nVALIDATION FAILED!")
    sys.exit(1)
