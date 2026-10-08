# -*- coding: utf-8 -*-
"""
Curated data for Food Batch 3:
- Dashboard — pom (30 words)
- Dashboard — sati (50 words)
Total: 80 words
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.food_part1_pom import data_pom
from scratch.food_part2_sati import data_sati_p1
from scratch.food_part3_sati import data_sati_p2

data_food_b3 = {}
data_food_b3.update(data_pom)
data_food_b3.update(data_sati_p1)
data_food_b3.update(data_sati_p2)

if __name__ == "__main__":
    print(f"Total entries in data_food_b3: {len(data_food_b3)}")
