# -*- coding: utf-8 -*-
"""
Combines Part 2b1 (47 words) and Part 2b2 (47 words) for Cluster Life Batch 2 Part 2b (94 words in spir).
"""

from curate_life_b2_p2b1 import CURATED_LIFE_B2_P2B1
from curate_life_b2_p2b2 import CURATED_LIFE_B2_P2B2

CURATED_LIFE_B2_P2B = {}
CURATED_LIFE_B2_P2B.update(CURATED_LIFE_B2_P2B1)
CURATED_LIFE_B2_P2B.update(CURATED_LIFE_B2_P2B2)

if __name__ == "__main__":
    from validate_curate import validate_curated_dict
    validate_curated_dict(CURATED_LIFE_B2_P2B, "Life Batch 2 Part 2b Total (94 words)")
