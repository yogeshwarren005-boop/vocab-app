# -*- coding: utf-8 -*-
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(__file__))

from validate_curate import validate_curated_dict
from curate_sending_b1_p1a import CURATED_SENDING_B1_P1A
from curate_sending_b1_p1b import CURATED_SENDING_B1_P1B

ok_1a = validate_curated_dict(CURATED_SENDING_B1_P1A, "Sending Batch 1 Part 1a (trud, jac, riv)")
ok_1b = validate_curated_dict(CURATED_SENDING_B1_P1B, "Sending Batch 1 Part 1b (trus)")

if ok_1a and ok_1b:
    print(f"\n✅ ALL 117 WORDS IN SENDING BATCH 1 PASSED VALIDATION PERFECTLY!")
    sys.exit(0)
else:
    print(f"\n❌ VALIDATION FAILED!")
    sys.exit(1)
