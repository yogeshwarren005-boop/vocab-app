# -*- coding: utf-8 -*-
"""
Curated dictionary for Cluster Life Batch 4 Part 4a:
Dashboard — gen (99 words: antigen to genoa)
Combines Part 4a1 (50 words) and Part 4a2 (49 words).
"""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from curate_life_b4_p4a1 import CURATED_LIFE_B4_P4A1
from curate_life_b4_p4a2 import CURATED_LIFE_B4_P4A2

CURATED_LIFE_B4_P4A = {}
CURATED_LIFE_B4_P4A.update(CURATED_LIFE_B4_P4A1)
CURATED_LIFE_B4_P4A.update(CURATED_LIFE_B4_P4A2)

if __name__ == "__main__":
    from validate_curate import validate_curated_dict
    validate_curated_dict(CURATED_LIFE_B4_P4A, "Life Batch 4 Part 4a (99 words)")
