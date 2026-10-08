# -*- coding: utf-8 -*-
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(__file__))

from validate_curate import validate_curated_dict
from curate_turning_b3_p1a import CURATED_TURNING_B3_P1A
from curate_turning_b3_p1b import CURATED_TURNING_B3_P1B
from curate_turning_b3_p2a import CURATED_TURNING_B3_P2A
from curate_turning_b3_p2b import CURATED_TURNING_B3_P2B

all_b3 = {}
all_b3.update(CURATED_TURNING_B3_P1A)
all_b3.update(CURATED_TURNING_B3_P1B)
all_b3.update(CURATED_TURNING_B3_P2A)
all_b3.update(CURATED_TURNING_B3_P2B)

print(f"Total curated entries in Turning Batch 3: {len(all_b3)}")

ok_1a = validate_curated_dict(CURATED_TURNING_B3_P1A, "Batch 3 Part 1a (mut 1-36)")
ok_1b = validate_curated_dict(CURATED_TURNING_B3_P1B, "Batch 3 Part 1b (mut 37-73)")
ok_2a = validate_curated_dict(CURATED_TURNING_B3_P2A, "Batch 3 Part 2a (tort 1-40)")
ok_2b = validate_curated_dict(CURATED_TURNING_B3_P2B, "Batch 3 Part 2b (vers 1-35)")

all_ok = ok_1a and ok_1b and ok_2a and ok_2b
print(f"\nOverall Batch 3 Validation: {'PASSED (100% PRISTINE)' if all_ok else 'FAILED'}")
if not all_ok:
    sys.exit(1)
