# -*- coding: utf-8 -*-
"""
curate_thought_b3.py
Combines Part 1 (38 words: mens 30, scrup 8) and Part 2 (44 words: sap 44).
Total: 82 words.
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.curate_thought_b3_p1 import data_thought_b3_p1
from scratch.curate_thought_b3_p2 import data_thought_b3_p2

data_thought_b3 = {}
data_thought_b3.update(data_thought_b3_p1)
data_thought_b3.update(data_thought_b3_p2)

if __name__ == "__main__":
    print(f"Total words in data_thought_b3: {len(data_thought_b3)}")
