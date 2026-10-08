# -*- coding: utf-8 -*-
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(__file__))

from validate_curate import validate_curated_dict
from curate_turning_b2_p1a import CURATED_TURNING_B2_P1A
from curate_turning_b2_p1b import CURATED_TURNING_B2_P1B
from curate_turning_b2_p2a import CURATED_TURNING_B2_P2A
from curate_turning_b2_p2b import CURATED_TURNING_B2_P2B

all_b2 = {}
all_b2.update(CURATED_TURNING_B2_P1A)
all_b2.update(CURATED_TURNING_B2_P1B)
all_b2.update(CURATED_TURNING_B2_P2A)
all_b2.update(CURATED_TURNING_B2_P2B)

print(f"Total curated entries in Turning Batch 2: {len(all_b2)}")

ok_1a = validate_curated_dict(CURATED_TURNING_B2_P1A, "Batch 2 Part 1a (flect 29, torqu 2, tors 2)")
ok_1b = validate_curated_dict(CURATED_TURNING_B2_P1B, "Batch 2 Part 1b (flex 29, rot 1-10)")
ok_2a = validate_curated_dict(CURATED_TURNING_B2_P2A, "Batch 2 Part 2a (rot 11-44, orb 1-5)")
ok_2b = validate_curated_dict(CURATED_TURNING_B2_P2B, "Batch 2 Part 2b (orb 6-15, trop 1-33)")

all_ok = ok_1a and ok_1b and ok_2a and ok_2b
print(f"\nOverall Batch 2 Validation: {'PASSED (100% PRISTINE)' if all_ok else 'FAILED'}")
if not all_ok:
    sys.exit(1)
