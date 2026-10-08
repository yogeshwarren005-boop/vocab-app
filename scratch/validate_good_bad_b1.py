# -*- coding: utf-8 -*-
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(__file__))

from validate_curate import validate_curated_dict
from curate_good_bad_b1_p1a import CURATED_GOOD_BAD_B1_P1A
from curate_good_bad_b1_p1b import CURATED_GOOD_BAD_B1_P1B
from curate_good_bad_b1_p2a import CURATED_GOOD_BAD_B1_P2A
from curate_good_bad_b1_p2b import CURATED_GOOD_BAD_B1_P2B

all_b1 = {}
all_b1.update(CURATED_GOOD_BAD_B1_P1A)
all_b1.update(CURATED_GOOD_BAD_B1_P1B)
all_b1.update(CURATED_GOOD_BAD_B1_P2A)
all_b1.update(CURATED_GOOD_BAD_B1_P2B)

print(f"Total curated entries in Good & Bad Batch 1: {len(all_b1)}")

ok_1a = validate_curated_dict(CURATED_GOOD_BAD_B1_P1A, "Batch 1 Part 1a (apt 1-32)")
ok_1b = validate_curated_dict(CURATED_GOOD_BAD_B1_P1B, "Batch 1 Part 1b (bas 1-37)")
ok_2a = validate_curated_dict(CURATED_GOOD_BAD_B1_P2A, "Batch 1 Part 2a (bas 38-74)")
ok_2b = validate_curated_dict(CURATED_GOOD_BAD_B1_P2B, "Batch 1 Part 2b (bas 75-111)")

all_ok = ok_1a and ok_1b and ok_2a and ok_2b
print(f"\nOverall Batch 1 Validation: {'PASSED (100% PRISTINE)' if all_ok else 'FAILED'}")
if not all_ok:
    sys.exit(1)
