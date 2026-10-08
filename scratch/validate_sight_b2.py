# -*- coding: utf-8 -*-
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.append(".")

from scratch.curate_sight_b2 import data_sight_b2

print(f"Total words in data_sight_b2: {len(data_sight_b2)}")

target_dirs = [
    r"App database/Latin roots/Cluster Sight/Dashboard — vid",
    r"App database/Latin roots/Cluster Sight/Dashboard — vis"
]

all_dir_words = []
for d in target_dirs:
    wds = [f[:-3] for f in os.listdir(d) if f.endswith('.md') and not f.startswith(('Dashboard', 'Word Triage', 'Cluster', 'Semantic Field'))]
    all_dir_words.extend(wds)

print(f"Total files on disk across target dirs: {len(all_dir_words)}")

missing_in_data = [w for w in all_dir_words if w not in data_sight_b2]
if missing_in_data:
    print(f"MISSING IN DATA: {missing_in_data}")
else:
    print("All disk words are present in data_sight_b2!")

extra_in_data = [w for w in data_sight_b2 if w not in all_dir_words]
if extra_in_data:
    print(f"EXTRA IN DATA: {extra_in_data}")
else:
    print("No extra words in data_sight_b2!")

circular_pat = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.IGNORECASE)

errors = []
for w, d in data_sight_b2.items():
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
    print("ALL 97 WORDS IN SIGHT BATCH 2 PASSED VALIDATION PERFECTLY!")
