# -*- coding: utf-8 -*-
"""
curate_thought_b1.py
Combines Part 1 (54 words) and Part 2 (53 words) for Batch 1 of Cluster Thought (107 words total).
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.curate_thought_b1_p1 import data_thought_b1_p1
from scratch.curate_thought_b1_p2 import data_thought_b1_p2

data_thought_b1 = {}
data_thought_b1.update(data_thought_b1_p1)
data_thought_b1.update(data_thought_b1_p2)

if __name__ == "__main__":
    print(f"Total words in Thought Batch 1: {len(data_thought_b1)}")
