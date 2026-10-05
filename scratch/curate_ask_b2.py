# -*- coding: utf-8 -*-
"""
curate_ask_b2.py
Master dataset for Batch 2 of Cluster Asking & Seeking (82 words):
- Dashboard — rog (40 words)
- Dashboard — pris (42 words)

All 82 words curated with:
- Active descriptive primary definitions (>= 25 chars, no circular formulas)
- Specialized / domain secondary definitions (>= 25 chars)
- Exactly 3 distinct authentic literary/historical quotations with target word bolded
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

from curate_ask_b2_part1 import rog_part1
from curate_ask_b2_part2 import rog_part2
from curate_ask_b2_part3 import pris_part1
from curate_ask_b2_part4 import pris_part2

data_ask_b2 = {}
data_ask_b2.update(rog_part1)
data_ask_b2.update(rog_part2)
data_ask_b2.update(pris_part1)
data_ask_b2.update(pris_part2)

if __name__ == "__main__":
    print(f"Total curated words in data_ask_b2: {len(data_ask_b2)}")
