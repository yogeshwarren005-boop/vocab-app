# -*- coding: utf-8 -*-
"""
Curated dictionary for Cluster Life Batch 5 Part 5b:
Dashboard — sen (105 words: senegal to unsentimentally)
Combines Part 5b1 (53 words) and Part 5b2 (52 words).
"""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from curate_life_b5_p5b1 import CURATED_LIFE_B5_P5B1
from curate_life_b5_p5b2 import CURATED_LIFE_B5_P5B2

CURATED_LIFE_B5_P5B = {}
CURATED_LIFE_B5_P5B.update(CURATED_LIFE_B5_P5B1)
CURATED_LIFE_B5_P5B.update(CURATED_LIFE_B5_P5B2)

if __name__ == "__main__":
    from validate_curate import validate_curated_dict
    validate_curated_dict(CURATED_LIFE_B5_P5B, "Life Batch 5 Part 5b (105 words)")
