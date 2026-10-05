# -*- coding: utf-8 -*-
"""
curate_ask_b3.py
Unified master dataset for Asking & Seeking Batch 3: Dashboard — pet (127 words).
"""
import sys
import os

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("scratch"))

from scratch.pet_part1 import pet_part1
from scratch.pet_part2 import pet_part2
from scratch.pet_part3 import pet_part3
from scratch.pet_part4 import pet_part4

data_ask_b3 = {}
data_ask_b3.update(pet_part1)
data_ask_b3.update(pet_part2)
data_ask_b3.update(pet_part3)
data_ask_b3.update(pet_part4)

if __name__ == "__main__":
    print(f"Total curated words in data_ask_b3: {len(data_ask_b3)}")
    assert len(data_ask_b3) == 127, f"Expected 127 words, got {len(data_ask_b3)}"
    print("Verification of curate_ask_b3 count passed successfully!")
