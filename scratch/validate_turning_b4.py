# -*- coding: utf-8 -*-
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(__file__))

from validate_curate import validate_curated_dict
from curate_turning_b4_p1a import CURATED_TURNING_B4_P1A
from curate_turning_b4_p1b import CURATED_TURNING_B4_P1B
from curate_turning_b4_p2a import CURATED_TURNING_B4_P2A
from curate_turning_b4_p2b import CURATED_TURNING_B4_P2B

all_b4 = {}
all_b4.update(CURATED_TURNING_B4_P1A)
all_b4.update(CURATED_TURNING_B4_P1B)
all_b4.update(CURATED_TURNING_B4_P2A)
all_b4.update(CURATED_TURNING_B4_P2B)

print(f"Total curated entries in Turning Batch 4: {len(all_b4)}")

ok_1a = validate_curated_dict(CURATED_TURNING_B4_P1A, "Batch 4 Part 1a (vers 36-64)")
ok_1b = validate_curated_dict(CURATED_TURNING_B4_P1B, "Batch 4 Part 1b (vers 65-93)")
ok_2a = validate_curated_dict(CURATED_TURNING_B4_P2A, "Batch 4 Part 2a (vert 1-45)")
ok_2b = validate_curated_dict(CURATED_TURNING_B4_P2B, "Batch 4 Part 2b (vert 46-91)")

all_ok = ok_1a and ok_1b and ok_2a and ok_2b
print(f"\nOverall Batch 4 Validation: {'PASSED (100% PRISTINE)' if all_ok else 'FAILED'}")
if not all_ok:
    sys.exit(1)
