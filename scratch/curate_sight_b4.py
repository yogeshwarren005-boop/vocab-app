# -*- coding: utf-8 -*-
"""
curate_sight_b4.py
Combines:
- data_sight_b3 (62 words that overlap between spect and spec)
- data_sight_b4_p1 (34 words)
- data_sight_b4_p2 (34 words)
Total: 130 words for Dashboard — spec.
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.append(".")

from scratch.curate_sight_b3 import data_sight_b3
from scratch.curate_sight_b4_p1 import data_sight_b4_p1
from scratch.curate_sight_b4_p2 import data_sight_b4_p2

data_sight_b4 = {}
# Import all words that match spec from b3
for k, v in data_sight_b3.items():
    data_sight_b4[k] = v

data_sight_b4.update(data_sight_b4_p1)
data_sight_b4.update(data_sight_b4_p2)

if __name__ == "__main__":
    print(f"Total words in data_sight_b4: {len(data_sight_b4)}")
