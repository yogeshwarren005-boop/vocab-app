# -*- coding: utf-8 -*-
"""
Curated dictionary for Cluster Life Batch 5 Part 5a:
Dashboard — sen (106 words: absence to senega)
Combines Part 5a1 (53 words) and Part 5a2 (53 words).
"""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from curate_life_b5_p5a1 import CURATED_LIFE_B5_P5A1
from curate_life_b5_p5a2 import CURATED_LIFE_B5_P5A2

CURATED_LIFE_B5_P5A = {}
CURATED_LIFE_B5_P5A.update(CURATED_LIFE_B5_P5A1)
CURATED_LIFE_B5_P5A.update(CURATED_LIFE_B5_P5A2)

if __name__ == "__main__":
    from validate_curate import validate_curated_dict
    validate_curated_dict(CURATED_LIFE_B5_P5A, "Life Batch 5 Part 5a (106 words)")
