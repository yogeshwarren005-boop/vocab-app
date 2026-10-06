# -*- coding: utf-8 -*-
"""
curate_thought_b2.py
Combines Part 1 (65 words) and Part 2 (66 words) for Dashboard — log (131 words total).
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.curate_thought_b2_p1 import data_thought_b2_p1
from scratch.curate_thought_b2_p2 import data_thought_b2_p2

data_thought_b2 = {}
data_thought_b2.update(data_thought_b2_p1)
data_thought_b2.update(data_thought_b2_p2)

if __name__ == "__main__":
    print(f"Total words in data_thought_b2: {len(data_thought_b2)}")
