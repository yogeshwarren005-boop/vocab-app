# -*- coding: utf-8 -*-
"""
curate_sight_b2.py
Merges curate_sight_b2_p1 (48 words) and curate_sight_b2_p2 (49 words).
Total: 97 words across:
- Dashboard — vid (39 words)
- Dashboard — vis (58 words)
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.append(".")

from scratch.curate_sight_b2_p1 import data_sight_b2_p1
from scratch.curate_sight_b2_p2 import data_sight_b2_p2

data_sight_b2 = {}
data_sight_b2.update(data_sight_b2_p1)
data_sight_b2.update(data_sight_b2_p2)

if __name__ == "__main__":
    print(f"Total words in data_sight_b2: {len(data_sight_b2)}")
