# -*- coding: utf-8 -*-
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from validate_curate import validate_curated_dict
from curate_truth_b3_p1a import CURATED_TRUTH_P3_1A
from curate_truth_b3_p1b import CURATED_TRUTH_P3_1B
from curate_truth_b3_p2a import CURATED_TRUTH_P3_2A
from curate_truth_b3_p2b import CURATED_TRUTH_P3_2B

all_curated = {}
all_curated.update(CURATED_TRUTH_P3_1A)
all_curated.update(CURATED_TRUTH_P3_1B)
all_curated.update(CURATED_TRUTH_P3_2A)
all_curated.update(CURATED_TRUTH_P3_2B)

print(f"Total curated words in Truth Batch 3: {len(all_curated)}")

base_path = 'App database/Latin roots/Cluster Truth, Deception & Error'
ver_dir = [d for d in os.listdir(base_path) if d.endswith('ver')][0]
p = os.path.join(base_path, ver_dir)
all_words = sorted([f[:-3] for f in os.listdir(p) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')])
b3_words = all_words[:160]

missing = set(b3_words) - set(all_curated.keys())
print(f"Missing curated for Batch 3: {len(missing)}")
if missing:
    print(f"  Missing: {sorted(list(missing))}")

ok1 = validate_curated_dict(CURATED_TRUTH_P3_1A, "Batch 3 Part 1a (ver 1-40)")
ok2 = validate_curated_dict(CURATED_TRUTH_P3_1B, "Batch 3 Part 1b (ver 41-80)")
ok3 = validate_curated_dict(CURATED_TRUTH_P3_2A, "Batch 3 Part 2a (ver 81-120)")
ok4 = validate_curated_dict(CURATED_TRUTH_P3_2B, "Batch 3 Part 2b (ver 121-160)")
ok_all = validate_curated_dict(all_curated, "Batch 3 Full (160 words)")

if ok1 and ok2 and ok3 and ok4 and ok_all and len(missing) == 0:
    print("\nALL 160 WORDS OF TRUTH BATCH 3 PASSED VALIDATION WITH 100% PRISTINE INTEGRITY!")
else:
    print("\nVALIDATION FAILED!")
    sys.exit(1)
