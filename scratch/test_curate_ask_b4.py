# -*- coding: utf-8 -*-
"""
Full validation script for curate_ask_b4.py:
Audits all 108 words according to all audit criteria.
"""
import sys
import re

sys.stdout.reconfigure(encoding="utf-8")
sys.path.append(".")

from scratch.curate_ask_b4 import data_ask_b4
from scratch.validator import validate_entry

expected_words = [
    'appreciable', 'appreciably', 'appreciate', 'appreciated', 'appreciation',
    'appreciative', 'appreciatively', 'appreciativeness', 'appreciator', 'deprecate',
    'deprecating', 'deprecation', 'deprecative', 'deprecatively', 'deprecatory',
    'depreciate', 'depreciating', 'depreciation', 'depreciative', 'depreciator',
    'depreciatory', 'imprecate', 'imprecation', 'imprecise', 'imprecisely',
    'impreciseness', 'imprecision', 'inappreciable', 'precambrian', 'precancerous',
    'precarious', 'precariously', 'precariousness', 'precast', 'precative',
    'precatory', 'precaution', 'precautional', 'precautionary', 'precava',
    'precede', 'precedence', 'precedency', 'precedent', 'precedented',
    'precedentedly', 'precedential', 'preceding', 'precentor', 'precentorship',
    'precept', 'preceptor', 'preceptorship', 'precess', 'precession',
    'precinct', 'preciosity', 'precious', 'preciously', 'preciousness',
    'precipice', 'precipitance', 'precipitancy', 'precipitant', 'precipitate',
    'precipitately', 'precipitateness', 'precipitating', 'precipitation', 'precipitator',
    'precipitin', 'precipitous', 'precipitously', 'precipitousness', 'precis',
    'precise', 'precisely', 'preciseness', 'precision', 'preclinical',
    'preclude', 'preclusion', 'preclusive', 'precocial', 'precocious',
    'precociously', 'precociousness', 'precocity', 'precognition', 'precognitive',
    'preconceive', 'preconceived', 'preconception', 'preconcerted', 'precondition',
    'preconditioned', 'precook', 'precooked', 'precooled', 'precordial',
    'precordium', 'precursor', 'precursory', 'unappreciated', 'unappreciative',
    'unappreciatively', 'unprecedented', 'unprecedentedly'
]

print(f"Total entries in data_ask_b4: {len(data_ask_b4)}")
assert len(data_ask_b4) == 108

issues = 0
for w in expected_words:
    if w not in data_ask_b4:
        print(f"Missing expected word: {w}")
        issues += 1

for word, data in data_ask_b4.items():
    entry_issues = validate_entry(word, data)
    if entry_issues:
        print(f"[{word}] Issues: {entry_issues}")
        issues += len(entry_issues)

if issues == 0:
    print("ALL 108 WORDS IN data_ask_b4 ARE 100% VALIDATED WITH ZERO ISSUES!")
else:
    print(f"TOTAL ISSUES: {issues}")
    sys.exit(1)
