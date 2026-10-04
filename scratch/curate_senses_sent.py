# -*- coding: utf-8 -*-
"""
Curated definitions and authentic citations for Dashboard — sent (79 words).
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.part1_sent import batch1
from scratch.part2_sent import batch2
from scratch.part3_sent import batch3
from scratch.part4_sent import batch4

data_senses_sent = {}
data_senses_sent.update(batch1)
data_senses_sent.update(batch2)
data_senses_sent.update(batch3)
data_senses_sent.update(batch4)

if __name__ == "__main__":
    print(f"Total curated words in data_senses_sent: {len(data_senses_sent)}")
