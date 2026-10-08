# -*- coding: utf-8 -*-
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.append(".")

from scratch.curate_sight_b4 import data_sight_b4

target_dir = r"App database/Latin roots/Cluster Sight/Dashboard — spec"

all_dir_words = [f[:-3] for f in os.listdir(target_dir) if f.endswith('.md') and not f.startswith(('Dashboard', 'Word Triage', 'Cluster', 'Semantic Field'))]

print(f"Total files on disk in Dashboard — spec: {len(all_dir_words)}")
print(f"Total words in data_sight_b4: {len(data_sight_b4)}")

missing_in_data = [w for w in all_dir_words if w not in data_sight_b4]
if missing_in_data:
    print(f"MISSING IN DATA: {missing_in_data}")
else:
    print("All disk words are present in data_sight_b4!")

circular_pat = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.IGNORECASE)

errors = []
for w in all_dir_words:
    if w not in data_sight_b4:
        continue
    d = data_sight_b4[w]
    p_len = len(d['primary'])
    s_len = len(d['secondary'])
    if p_len < 25:
        errors.append(f"{w}: primary too short ({p_len})")
    if s_len < 25:
        errors.append(f"{w}: secondary too short ({s_len})")
    if circular_pat.search(d['primary']):
        errors.append(f"{w}: primary has circular definition: {d['primary']}")
    if circular_pat.search(d['secondary']):
        errors.append(f"{w}: secondary has circular definition: {d['secondary']}")
    if len(d['quotes']) != 3:
        errors.append(f"{w}: quotes count != 3 ({len(d['quotes'])})")
    authors = set(q['author'] for q in d['quotes'])
    if len(authors) != 3:
        errors.append(f"{w}: authors not distinct ({authors})")
    for q in d['quotes']:
        if '**' not in q['quote']:
            errors.append(f"{w}: missing bolding in quote: {q}")

if errors:
    print(f"FOUND {len(errors)} ERRORS:")
    for e in errors:
        print(" ", e)
else:
    print("ALL 130 WORDS IN SIGHT BATCH 4 PASSED VALIDATION PERFECTLY!")
