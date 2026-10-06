# -*- coding: utf-8 -*-
"""
curate_anatomy_b3.py
Combines Part 1 (55 words) and Part 2 (60 words) for Batch 3 of Cluster Anatomy & Clinical Medicine (115 words total).
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.curate_anatomy_b3_p1 import data_anatomy_b3_p1
from scratch.curate_anatomy_b3_p2 import data_anatomy_b3_p2

data_anatomy_b3 = {}
data_anatomy_b3.update(data_anatomy_b3_p1)
data_anatomy_b3.update(data_anatomy_b3_p2)

if __name__ == "__main__":
    print(f"Total words in Batch 3: {len(data_anatomy_b3)}")
