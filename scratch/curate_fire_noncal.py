# -*- coding: utf-8 -*-
"""
Combined Curated Fire, Heat & Ash (non-cal):
- Part 1: ard (17), ciner (7), crem (10) -> 34 words
- Part 2: ferv (19), flam (30) -> 49 words
- Part 3: gelat (8), tep (11), torr (9), volcan (5) -> 33 words
Total: 116 words
"""
import sys
import os

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("scratch"))

import fire_part1 as p1
import fire_part2 as p2
import fire_part3 as p3

data_fire_noncal = {}
data_fire_noncal.update(p1.data_part1)
data_fire_noncal.update(p2.data_part2)
data_fire_noncal.update(p3.data_part3)

if __name__ == "__main__":
    print(f"Total curated non-cal fire words: {len(data_fire_noncal)}")
    assert len(data_fire_noncal) == 116, f"Expected 116 words, got {len(data_fire_noncal)}"
    print("Verification successful!")
