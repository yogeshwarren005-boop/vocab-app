# -*- coding: utf-8 -*-
"""
Unified dataset for Law, Justice & Feudal Batch 1 (77 words):
- Dashboard — arbitr (18 words)
- Dashboard — crim (46 words)
- Dashboard — damn (8 words)
- Dashboard — fisc (5 words)
Total: 77 words
"""
import sys
import os

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("scratch"))

import law_part1_arbitr as p1
import law_part2_crim as p2
import law_part3_damn_fisc as p3

data_law_b1 = {}
data_law_b1.update(p1.data_arbitr)
data_law_b1.update(p2.data_crim)
data_law_b1.update(p3.data_damn_fisc)

if __name__ == "__main__":
    print(f"Total curated words: {len(data_law_b1)}")
    assert len(data_law_b1) == 77, f"Expected 77 words, got {len(data_law_b1)}"
    print("Verification of curate_law_b1 passed successfully!")
