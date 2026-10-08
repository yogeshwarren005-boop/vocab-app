# -*- coding: utf-8 -*-
"""
Master curated data for Batch 4 of Cluster Food, Eating & Drink (88 words):
- Dashboard — vin (59 words): part1_vin (20) + part2_vin (20) + part3_vin (19)
- Dashboard — vor (29 words): part4_vor (29)

Total: 88 words.
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.part1_vin import part1_vin
from scratch.part2_vin import part2_vin
from scratch.part3_vin import part3_vin
from scratch.part4_vor import part4_vor

data_food_b4 = {}
data_food_b4.update(part1_vin)
data_food_b4.update(part2_vin)
data_food_b4.update(part3_vin)
data_food_b4.update(part4_vor)

if __name__ == "__main__":
    print(f"Total entries in data_food_b4: {len(data_food_b4)}")
