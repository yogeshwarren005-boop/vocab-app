# -*- coding: utf-8 -*-
"""
Master data dictionary for Law Batch 4:
- Dashboard — merces (20 words)
- Dashboard — sanc (19 words)
- Dashboard — vic (63 words)
Total: 102 words.
"""
import sys
sys.stdout.reconfigure(encoding="utf-8")

from parts.data_merces import data_merces
from parts.data_sanc import data_sanc
from parts.data_vic_p1 import data_vic_p1
from parts.data_vic_p2 import data_vic_p2
from parts.data_vic_p3 import data_vic_p3

data_law_b4 = {}
data_law_b4.update(data_merces)
data_law_b4.update(data_sanc)
data_law_b4.update(data_vic_p1)
data_law_b4.update(data_vic_p2)
data_law_b4.update(data_vic_p3)

if __name__ == "__main__":
    print(f"Total curated words in data_law_b4: {len(data_law_b4)}")
    assert len(data_law_b4) == 102, f"Expected 102 words, got {len(data_law_b4)}"
    print("Verification successful: exactly 102 words compiled.")
