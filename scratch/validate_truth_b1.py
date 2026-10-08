import re, sys
sys.stdout.reconfigure(encoding='utf-8')

from validate_curate import validate_curated_dict
from curate_truth_b1_p1a import CURATED_TRUTH_P1A
from curate_truth_b1_p1b1 import CURATED_TRUTH_P1B1
from curate_truth_b1_p1b2 import CURATED_TRUTH_P1B2

ok_1a = validate_curated_dict(CURATED_TRUTH_P1A, "Truth Batch 1 Part 1a (calumn + cert: 43 words)")
ok_1b1 = validate_curated_dict(CURATED_TRUTH_P1B1, "Truth Batch 1 Part 1b-1 (crypt: 50 words)")
ok_1b2 = validate_curated_dict(CURATED_TRUTH_P1B2, "Truth Batch 1 Part 1b-2 (err: 25 words)")

if ok_1a and ok_1b1 and ok_1b2:
    print("\nAll 118 words of Truth Batch 1 (calumn, cert, crypt, err) PASSED validation!")

