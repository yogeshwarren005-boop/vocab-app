# -*- coding: utf-8 -*-
"""
curate_anatomy_b2.py
Combines Part 1 (50 words) and Part 2 (51 words) for Batch 2 of Cluster Anatomy & Clinical Medicine (101 words total).
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.curate_anatomy_b2_p1 import data_anatomy_b2_p1
from scratch.curate_anatomy_b2_p2 import data_anatomy_b2_p2

data_anatomy_b2 = {}
data_anatomy_b2.update(data_anatomy_b2_p1)
data_anatomy_b2.update(data_anatomy_b2_p2)

if __name__ == "__main__":
    print(f"Total words in Batch 2: {len(data_anatomy_b2)}")
