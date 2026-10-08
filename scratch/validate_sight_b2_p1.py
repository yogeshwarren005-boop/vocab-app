# -*- coding: utf-8 -*-
import re
import sys
sys.path.append(".")
from scratch.curate_sight_b2_p1 import data_sight_b2_p1

print(f"Count: {len(data_sight_b2_p1)}")
circular_pat = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.IGNORECASE)

errors = []
for w, d in data_sight_b2_p1.items():
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
    print("ALL 48 WORDS IN P1 PASSED VALIDATION PERFECTLY!")
