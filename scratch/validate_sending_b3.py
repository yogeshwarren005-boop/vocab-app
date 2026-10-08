# -*- coding: utf-8 -*-
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(__file__))

from validate_curate import validate_curated_dict
from curate_sending_b3_p3a import CURATED_SENDING_B3_P3A
from curate_sending_b3_p3b import CURATED_SENDING_B3_P3B

ok_3a = validate_curated_dict(CURATED_SENDING_B3_P3A, "Sending Batch 3 Part 3a (miss)")
ok_3b = validate_curated_dict(CURATED_SENDING_B3_P3B, "Sending Batch 3 Part 3b (tract)")

if ok_3a and ok_3b:
    print(f"\n✅ ALL 160 WORDS IN SENDING BATCH 3 PASSED VALIDATION PERFECTLY!")
    sys.exit(0)
else:
    print(f"\n❌ VALIDATION FAILED!")
    sys.exit(1)
