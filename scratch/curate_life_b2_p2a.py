# -*- coding: utf-8 -*-
"""
Combines Part 2a1 (45 words) and Part 2a2 (45 words) for Cluster Life Batch 2 Part 2a (90 words in hal).
"""

from curate_life_b2_p2a1 import CURATED_LIFE_B2_P2A1
from curate_life_b2_p2a2 import CURATED_LIFE_B2_P2A2

CURATED_LIFE_B2_P2A = {}
CURATED_LIFE_B2_P2A.update(CURATED_LIFE_B2_P2A1)
CURATED_LIFE_B2_P2A.update(CURATED_LIFE_B2_P2A2)

if __name__ == "__main__":
    from validate_curate import validate_curated_dict
    validate_curated_dict(CURATED_LIFE_B2_P2A, "Life Batch 2 Part 2a Total (90 words)")
