# -*- coding: utf-8 -*-
"""
curate_time_b1.py
Unified dataset for Cluster Time Batch 1 (71 words):
- Dashboard — cras (9 words)
- Dashboard — di (15 words)
- Dashboard — ev (3 words)
- Dashboard — nov (21 words)
- Dashboard — saecul (7 words)
- Dashboard — simul (16 words)
Total: 71 words
"""
import sys
import os

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("scratch"))

import time_part1_cras_di_ev as p1
import time_part2_nov_saecul as p2
import time_part3_simul as p3

data_time_b1 = {}
data_time_b1.update(p1.data_cras_di_ev)
data_time_b1.update(p2.data_nov_saecul)
data_time_b1.update(p3.data_simul)

if __name__ == "__main__":
    print(f"Total curated words in data_time_b1: {len(data_time_b1)}")
    assert len(data_time_b1) == 71, f"Expected 71 words, got {len(data_time_b1)}"
    print("Verification of curate_time_b1 passed successfully!")
