# -*- coding: utf-8 -*-
"""
Combines Part 1a1 (46 words) and Part 1a2 (41 words) for Cluster Life Batch 1 Part 1a (87 words).
"""

from curate_life_b1_p1a1 import CURATED_LIFE_B1_P1A1
from curate_life_b1_p1a2 import CURATED_LIFE_B1_P1A2

CURATED_LIFE_B1_P1A = {}
CURATED_LIFE_B1_P1A.update(CURATED_LIFE_B1_P1A1)
CURATED_LIFE_B1_P1A.update(CURATED_LIFE_B1_P1A2)

if __name__ == "__main__":
    from validate_curate import validate_curated_dict
    validate_curated_dict(CURATED_LIFE_B1_P1A, "Life Batch 1 Part 1a Total (87 words)")
