# -*- coding: utf-8 -*-
"""
curate_sight_b1.py
Combines Part 1 (45 words) and Part 2 (44 words) for Sight Batch 1 (89 words total).
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.curate_sight_b1_p1 import data_sight_b1_p1
from scratch.curate_sight_b1_p2 import data_sight_b1_p2

data_sight_b1 = {}
data_sight_b1.update(data_sight_b1_p1)
data_sight_b1.update(data_sight_b1_p2)

if __name__ == "__main__":
    print(f"Total words in data_sight_b1: {len(data_sight_b1)}")
