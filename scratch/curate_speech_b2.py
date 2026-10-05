# -*- coding: utf-8 -*-
"""
Master curated data for Batch 2 of Cluster Speech (82 words):
- Dashboard — cit (65 words): part1_cit (22) + part2_cit (22) + part3_cit (21)
- Dashboard — nunci (17 words): part4_nunci (17)

Total: 82 words.
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.part1_cit import part1_cit
from scratch.part2_cit import part2_cit
from scratch.part3_cit import part3_cit
from scratch.part4_nunci import part4_nunci

data_speech_b2 = {}
data_speech_b2.update(part1_cit)
data_speech_b2.update(part2_cit)
data_speech_b2.update(part3_cit)
data_speech_b2.update(part4_nunci)

if __name__ == "__main__":
    print(f"Total entries in data_speech_b2: {len(data_speech_b2)}")
