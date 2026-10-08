# -*- coding: utf-8 -*-
"""
curate_sight_b3.py
Merges curate_sight_b3_p1 (55 words) and curate_sight_b3_p2 (53 words).
Total: 108 words across:
- Dashboard — spect (62 words)
- Dashboard — spic (46 words)
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.append(".")

from scratch.curate_sight_b3_p1 import data_sight_b3_p1
from scratch.curate_sight_b3_p2 import data_sight_b3_p2

data_sight_b3 = {}
data_sight_b3.update(data_sight_b3_p1)
data_sight_b3.update(data_sight_b3_p2)

if __name__ == "__main__":
    print(f"Total words in data_sight_b3: {len(data_sight_b3)}")
