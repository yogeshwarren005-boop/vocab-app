# -*- coding: utf-8 -*-
"""
Assembles all 95 words in Batch 2 of Cluster Law, Justice & Feudal:
- Dashboard — judic (23 words)
- Dashboard — juris (7 words)
- Dashboard — just (34 words)
- Dashboard — legat (12 words)
- Dashboard — senat (5 words)
- Dashboard — statut (3 words)
- Dashboard — vindic (11 words)
Total: 23 + 7 + 34 + 12 + 5 + 3 + 11 = 95 words.
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.part_judic import part_judic
from scratch.part_juris import part_juris
from scratch.part_just import part_just
from scratch.part_legat import part_legat
from scratch.part_senat import part_senat
from scratch.part_statut import part_statut
from scratch.part_vindic import part_vindic

data_law_b2 = {}
data_law_b2.update(part_judic)
data_law_b2.update(part_juris)
data_law_b2.update(part_just)
data_law_b2.update(part_legat)
data_law_b2.update(part_senat)
data_law_b2.update(part_statut)
data_law_b2.update(part_vindic)

if __name__ == "__main__":
    print(f"Total entries in data_law_b2: {len(data_law_b2)}")
