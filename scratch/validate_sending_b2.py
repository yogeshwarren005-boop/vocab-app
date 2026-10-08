# -*- coding: utf-8 -*-
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(__file__))

from validate_curate import validate_curated_dict
from curate_sending_b2_p2a import CURATED_SENDING_B2_P2A
from curate_sending_b2_p2b import CURATED_SENDING_B2_P2B

ok_2a = validate_curated_dict(CURATED_SENDING_B2_P2A, "Sending Batch 2 Part 2a (ject)")
ok_2b = validate_curated_dict(CURATED_SENDING_B2_P2B, "Sending Batch 2 Part 2b (fus)")

if ok_2a and ok_2b:
    print(f"\n✅ ALL 138 WORDS IN SENDING BATCH 2 PASSED VALIDATION PERFECTLY!")
    sys.exit(0)
else:
    print(f"\n❌ VALIDATION FAILED!")
    sys.exit(1)
