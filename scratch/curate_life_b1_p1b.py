# -*- coding: utf-8 -*-
"""
Combines Part 1b1 (36 words) and Part 1b2 (35 words) for Cluster Life Batch 1 Part 1b (71 words in vit).
"""

from curate_life_b1_p1b1 import CURATED_LIFE_B1_P1B1
from curate_life_b1_p1b2 import CURATED_LIFE_B1_P1B2

CURATED_LIFE_B1_P1B = {}
CURATED_LIFE_B1_P1B.update(CURATED_LIFE_B1_P1B1)
CURATED_LIFE_B1_P1B.update(CURATED_LIFE_B1_P1B2)

if __name__ == "__main__":
    from validate_curate import validate_curated_dict
    validate_curated_dict(CURATED_LIFE_B1_P1B, "Life Batch 1 Part 1b Total (71 words)")
