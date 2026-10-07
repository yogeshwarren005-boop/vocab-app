# -*- coding: utf-8 -*-
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from validate_curate import validate_curated_dict
from curate_truth_b2_p1a import CURATED_TRUTH_P2A1
from curate_truth_b2_p1b import CURATED_TRUTH_P2B
from curate_truth_b2_p2 import CURATED_TRUTH_P2_PROB

all_curated = {}
all_curated.update(CURATED_TRUTH_P2A1)
all_curated.update(CURATED_TRUTH_P2B)
all_curated.update(CURATED_TRUTH_P2_PROB)

print(f"Total unique curated words loaded: {len(all_curated)}")

base_dir = r"App database/Latin roots/Cluster Truth, Deception & Error"
actual_dirs = [d for d in os.listdir(base_dir) if any(k in d for k in ['fal', 'fall', 'fals', 'prob'])]

total_files_to_write = 0
for d in sorted(actual_dirs):
    d_path = os.path.join(base_dir, d)
    words = [f[:-3] for f in os.listdir(d_path) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]
    missing = set(words) - set(all_curated.keys())
    print(f"{d}: {len(words)} files (missing curated: {len(missing)})")
    if missing:
        print(f"  Missing: {sorted(list(missing))}")
    total_files_to_write += len(words)

print(f"\nTotal files across all 4 dashboards: {total_files_to_write}")

ok1 = validate_curated_dict(CURATED_TRUTH_P2A1, "Batch 2 Part 1a (fal 1-33)")
ok2 = validate_curated_dict(CURATED_TRUTH_P2B, "Batch 2 Part 1b (fal 34-65)")
ok3 = validate_curated_dict(CURATED_TRUTH_P2_PROB, "Batch 2 Part 2 (prob 1-39)")
ok_all = validate_curated_dict(all_curated, "Batch 2 Full (104 unique words)")

if ok1 and ok2 and ok3 and ok_all:
    print("\nALL 104 CURATED WORDS PASSED VALIDATION WITH 100% PRISTINE INTEGRITY!")
else:
    print("\nVALIDATION FAILED!")
    sys.exit(1)
