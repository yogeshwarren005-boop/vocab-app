# -*- coding: utf-8 -*-
"""
Combines Part 3a1 (32 words) and Part 3a2 (31 words) for Cluster Life Batch 3 Part 3a (63 words in nat).
"""

from curate_life_b3_p3a1 import CURATED_LIFE_B3_P3A1
from curate_life_b3_p3a2 import CURATED_LIFE_B3_P3A2

CURATED_LIFE_B3_P3A = {}
CURATED_LIFE_B3_P3A.update(CURATED_LIFE_B3_P3A1)
CURATED_LIFE_B3_P3A.update(CURATED_LIFE_B3_P3A2)

if __name__ == "__main__":
    from validate_curate import validate_curated_dict
    validate_curated_dict(CURATED_LIFE_B3_P3A, "Life Batch 3 Part 3a Total (63 words)")
