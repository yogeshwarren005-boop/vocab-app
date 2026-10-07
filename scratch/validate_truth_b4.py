# -*- coding: utf-8 -*-
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from validate_curate import validate_curated_dict
from curate_truth_b4_p1a import CURATED_TRUTH_P4_1A
from curate_truth_b4_p1b import CURATED_TRUTH_P4_1B
from curate_truth_b4_p2a import CURATED_TRUTH_P4_2A
from curate_truth_b4_p2b import CURATED_TRUTH_P4_2B

all_curated = {}
all_curated.update(CURATED_TRUTH_P4_1A)
all_curated.update(CURATED_TRUTH_P4_1B)
all_curated.update(CURATED_TRUTH_P4_2A)
all_curated.update(CURATED_TRUTH_P4_2B)

print(f"Total curated words in Truth Batch 4: {len(all_curated)}")

base_path = 'App database/Latin roots/Cluster Truth, Deception & Error'
ver_dir = [d for d in os.listdir(base_path) if d.endswith('ver')][0]
p = os.path.join(base_path, ver_dir)
all_words = sorted([f[:-3] for f in os.listdir(p) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')])
b4_words = all_words[160:]

print(f"Target Batch 4 words count from directory: {len(b4_words)}")

missing = set(b4_words) - set(all_curated.keys())
print(f"Missing curated for Batch 4: {len(missing)}")
if missing:
    print(f"  Missing: {sorted(list(missing))}")

ok1 = validate_curated_dict(CURATED_TRUTH_P4_1A, "Batch 4 Part 1a (ver 161-200)")
ok2 = validate_curated_dict(CURATED_TRUTH_P4_1B, "Batch 4 Part 1b (ver 201-240)")
ok3 = validate_curated_dict(CURATED_TRUTH_P4_2A, "Batch 4 Part 2a (ver 241-280)")
ok4 = validate_curated_dict(CURATED_TRUTH_P4_2B, "Batch 4 Part 2b (ver 281-321)")
ok_all = validate_curated_dict(all_curated, "Batch 4 Full (161 words)")

if ok1 and ok2 and ok3 and ok4 and ok_all and len(missing) == 0:
    print("\nALL 161 WORDS OF TRUTH BATCH 4 PASSED VALIDATION WITH 100% PRISTINE INTEGRITY!")
else:
    print("\nVALIDATION FAILED!")
    sys.exit(1)
