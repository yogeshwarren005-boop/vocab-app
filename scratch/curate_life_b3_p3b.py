# -*- coding: utf-8 -*-
"""
Combines Part 3b1 (31 words) and Part 3b2 (31 words) for Cluster Life Batch 3 Part 3b (62 words in nat).
"""

from curate_life_b3_p3b1 import CURATED_LIFE_B3_P3B1
from curate_life_b3_p3b2 import CURATED_LIFE_B3_P3B2

CURATED_LIFE_B3_P3B = {}
CURATED_LIFE_B3_P3B.update(CURATED_LIFE_B3_P3B1)
CURATED_LIFE_B3_P3B.update(CURATED_LIFE_B3_P3B2)

if __name__ == "__main__":
    from validate_curate import validate_curated_dict
    validate_curated_dict(CURATED_LIFE_B3_P3B, "Life Batch 3 Part 3b Total (62 words)")
