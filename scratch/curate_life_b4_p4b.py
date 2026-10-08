# -*- coding: utf-8 -*-
"""
Curated dictionary for Cluster Life Batch 4 Part 4b:
Dashboard — gen (99 words: genocide to unregenerated)
Combines Part 4b1 (50 words) and Part 4b2 (49 words).
"""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from curate_life_b4_p4b1 import CURATED_LIFE_B4_P4B1
from curate_life_b4_p4b2 import CURATED_LIFE_B4_P4B2

CURATED_LIFE_B4_P4B = {}
CURATED_LIFE_B4_P4B.update(CURATED_LIFE_B4_P4B1)
CURATED_LIFE_B4_P4B.update(CURATED_LIFE_B4_P4B2)

if __name__ == "__main__":
    from validate_curate import validate_curated_dict
    validate_curated_dict(CURATED_LIFE_B4_P4B, "Life Batch 4 Part 4b (99 words)")
