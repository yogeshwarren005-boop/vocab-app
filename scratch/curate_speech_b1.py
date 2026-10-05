# -*- coding: utf-8 -*-
"""
Master curated dictionary for Speech Batch 1 (83 words across 7 dashboards):
- articul (17 words)
- claim (16 words)
- clam (23 words)
- fari (2 words)
- garrul (7 words)
- orat (12 words)
- suad (6 words)
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scratch.curate_speech_b1_articul import data_articul
from scratch.curate_speech_b1_claim import data_claim
from scratch.curate_speech_b1_clam import data_clam
from scratch.curate_speech_b1_rest import data_fari, data_garrul, data_orat, data_suad

data_speech_b1 = {}
data_speech_b1.update(data_articul)
data_speech_b1.update(data_claim)
data_speech_b1.update(data_clam)
data_speech_b1.update(data_fari)
data_speech_b1.update(data_garrul)
data_speech_b1.update(data_orat)
data_speech_b1.update(data_suad)

if __name__ == "__main__":
    print(f"Loaded data_speech_b1 with {len(data_speech_b1)} curated words.")
