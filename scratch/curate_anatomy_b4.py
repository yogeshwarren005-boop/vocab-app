# -*- coding: utf-8 -*-
"""
curate_anatomy_b4.py
Combines Part 1 (38 words) and Part 2 (37 words) for Batch 4 of Cluster Anatomy & Clinical Medicine (Dashboard — ren: 75 words total).
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.curate_anatomy_b4_p1 import data_anatomy_b4_p1
from scratch.curate_anatomy_b4_p2 import data_anatomy_b4_p2

data_anatomy_b4 = {}
data_anatomy_b4.update(data_anatomy_b4_p1)
data_anatomy_b4.update(data_anatomy_b4_p2)

if __name__ == "__main__":
    print(f"Total words in Batch 4: {len(data_anatomy_b4)}")
