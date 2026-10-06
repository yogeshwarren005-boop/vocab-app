# -*- coding: utf-8 -*-
"""
curate_thought_b4.py
Combines Part 1 (38 words) and Part 2 (39 words) for Dashboard — sci.
Total: 77 words.
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.curate_thought_b4_p1 import data_thought_b4_p1
from scratch.curate_thought_b4_p2 import data_thought_b4_p2

data_thought_b4 = {}
data_thought_b4.update(data_thought_b4_p1)
data_thought_b4.update(data_thought_b4_p2)

if __name__ == "__main__":
    print(f"Total words in data_thought_b4: {len(data_thought_b4)}")
