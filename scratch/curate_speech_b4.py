# -*- coding: utf-8 -*-
"""
Master data dictionary for Speech Batch 4 (106 words across 4 dashboards, 84 distinct headwords):
- Dashboard — lingu (21 words)
- Dashboard — loqu (25 words)
- Dashboard — nom (34 words)
- Dashboard — nomin (26 words)
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.append(".")

from scratch.part1_lingu import part1_lingu
from scratch.part2_loqu import part2_loqu
from scratch.part3_nom_a import part3_nom_a
from scratch.part4_nom_b import part4_nom_b

data_speech_b4 = {}
data_speech_b4.update(part1_lingu)
data_speech_b4.update(part2_loqu)
data_speech_b4.update(part3_nom_a)
data_speech_b4.update(part4_nom_b)

if __name__ == "__main__":
    print(f"Total entries in data_speech_b4: {len(data_speech_b4)}")
