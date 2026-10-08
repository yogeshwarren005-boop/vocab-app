# -*- coding: utf-8 -*-
"""
Master curated data for Food Batch 1 (110 words):
- bib (6 words)
- coct (5 words)
- coqu (6 words)
- ed (34 words)
- lact (29 words)
- mell (15 words)
- pan (9 words)
- pota (6 words)
Total: 110 words
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.curate_food_b1_p1 import data_food_p1
from scratch.curate_food_b1_p2 import data_food_p2
from scratch.curate_food_b1_p3a import data_food_p3a
from scratch.curate_food_b1_p3b import data_food_p3b

data_food_b1 = {}
data_food_b1.update(data_food_p1)
data_food_b1.update(data_food_p2)
data_food_b1.update(data_food_p3a)
data_food_b1.update(data_food_p3b)

if __name__ == "__main__":
    print(f"Total entries in data_food_b1: {len(data_food_b1)}")
