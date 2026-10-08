# -*- coding: utf-8 -*-
"""
Master curated data for Food Batch 2 (Dashboard — al, 114 words):
- curate_food_b2_p1 (38 words)
- curate_food_b2_p2a (19 words)
- curate_food_b2_p2b (19 words)
- curate_food_b2_p3a (19 words)
- curate_food_b2_p3b (19 words)
Total: 114 words
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.curate_food_b2_p1 import data_food_b2_p1
from scratch.curate_food_b2_p2a import data_food_b2_p2a
from scratch.curate_food_b2_p2b import data_food_b2_p2b
from scratch.curate_food_b2_p3a import data_food_b2_p3a
from scratch.curate_food_b2_p3b import data_food_b2_p3b

data_food_b2 = {}
data_food_b2.update(data_food_b2_p1)
data_food_b2.update(data_food_b2_p2a)
data_food_b2.update(data_food_b2_p2b)
data_food_b2.update(data_food_b2_p3a)
data_food_b2.update(data_food_b2_p3b)

if __name__ == "__main__":
    print(f"Total entries in data_food_b2: {len(data_food_b2)}")
