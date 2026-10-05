# -*- coding: utf-8 -*-
"""
Master data file for Cluster Speech - Batch 3 (92 words):
- Dashboard — dict (50 words):
  - 47 words from dict_law (part1_dict: 24, part2_dict: 23)
  - 3 words from extra_curated_24: 'benediction', 'benedictive', 'unpredicted'
- Dashboard — tac (42 words):
  - 21 words from tact_from_touch.json
  - 21 words from extra_curated_24: 'altace', 'antacid', 'astacidae', 'astacura', 'astacus',
    'attacapa', 'attacapan', 'cotacachi', 'setaceous', 'tacamahac', 'tacca', 'taccaceae',
    'tacit', 'tacitly', 'taciturn', 'taciturnity', 'taciturnly', 'tacitus', 'taco', 'tacoma', 'taconite'

Total: 92 words.
"""
import sys
import os
import json
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scratch.part1_dict_law import part1_dict
from scratch.part2_dict_law import part2_dict
from scratch.curate_extra_24 import extra_curated_24

tact_json_path = Path(__file__).parent / "tact_from_touch.json"
with open(tact_json_path, "r", encoding="utf-8") as f:
    tact_21 = json.load(f)

data_speech_b3 = {}

# 1. Populate dict words (50)
for k, v in part1_dict.items():
    data_speech_b3[k] = v

for k, v in part2_dict.items():
    data_speech_b3[k] = v

for k in ['benediction', 'benedictive', 'unpredicted']:
    data_speech_b3[k] = extra_curated_24[k]

# 2. Populate tac words (42)
for k, v in tact_21.items():
    data_speech_b3[k] = v

tac_non_tact = [
    'altace', 'antacid', 'astacidae', 'astacura', 'astacus',
    'attacapa', 'attacapan', 'cotacachi', 'setaceous', 'tacamahac',
    'tacca', 'taccaceae', 'tacit', 'tacitly', 'taciturn',
    'taciturnity', 'taciturnly', 'tacitus', 'taco', 'tacoma', 'taconite'
]

for k in tac_non_tact:
    data_speech_b3[k] = extra_curated_24[k]

if __name__ == "__main__":
    print(f"Total entries in data_speech_b3: {len(data_speech_b3)}")
