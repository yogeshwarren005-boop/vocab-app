# -*- coding: utf-8 -*-
"""
Master curated dataset for Batch 1 of Cluster Anatomy & Clinical Medicine:
- Dashboard — adip
- Dashboard — aur_ear
- Dashboard — cervic
- Dashboard — dent
- Dashboard — front
- Dashboard — lacrim
- Dashboard — maxill
- Dashboard — ocul
Total: 132 words (full coverage).
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.curate_anatomy_b1_p1a import data_anatomy_p1a
from scratch.curate_anatomy_b1_p1b import data_anatomy_p1b
from scratch.curate_anatomy_b1_p1c import data_anatomy_p1c
from scratch.curate_anatomy_b1_p1d import data_anatomy_p1d
from scratch.curate_anatomy_b1_supp1 import data_anatomy_supp1
from scratch.curate_anatomy_b1_supp2 import data_anatomy_supp2

data_anatomy_b1 = {}
data_anatomy_b1.update(data_anatomy_p1a)
data_anatomy_b1.update(data_anatomy_p1b)
data_anatomy_b1.update(data_anatomy_p1c)
data_anatomy_b1.update(data_anatomy_p1d)
data_anatomy_b1.update(data_anatomy_supp1)
data_anatomy_b1.update(data_anatomy_supp2)

if __name__ == "__main__":
    print(f"Total entries in data_anatomy_b1: {len(data_anatomy_b1)}")
