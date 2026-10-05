# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")
from curate_time_b2 import data_time_b2
from validator import validate_entry

all_issues = {}

expected_words = [
    'anna', 'annaba', 'annalist', 'annalistic', 'annals', 'annam', 'annamese', 'annamite',
    'annapolis', 'annapurna', 'anne', 'anneal', 'annealing', 'annelid', 'annelida', 'annelidan',
    'annex', 'annexa', 'annexal', 'annexation', 'annexational', 'annexe', 'anniellidae',
    'annihilate', 'annihilated', 'annihilating', 'annihilation', 'annihilative', 'annihilator',
    'anniversary', 'annon', 'annona', 'annonaceae', 'annotate', 'annotating', 'annotation',
    'annotator', 'announce', 'announced', 'announcement', 'announcer', 'annoy', 'annoyance',
    'annoyed', 'annoyer', 'annoying', 'annoyingly', 'annual', 'annually', 'annualry',
    'annuitant', 'annuity', 'annul', 'annular', 'annulate', 'annulated', 'annulet',
    'annulment', 'annulus', 'annum', 'annunciate', 'annunciation', 'annunciator',
    'annunciatory', 'inanna', 'per annum', 'semiannual', 'semiannually', 'superannuate',
    'superannuated', 'superannuation', 'susanna', 'unannealed', 'unannounced'
]

print(f"Total words in dataset: {len(data_time_b2)}")
print(f"Expected words count: {len(expected_words)}")

missing = set(expected_words) - set(data_time_b2.keys())
extra = set(data_time_b2.keys()) - set(expected_words)
if missing:
    print(f"MISSING WORDS: {missing}")
if extra:
    print(f"EXTRA WORDS: {extra}")

for w in expected_words:
    if w in data_time_b2:
        entry = data_time_b2[w]
        issues = validate_entry(w, entry)
        if issues:
            all_issues[w] = issues

if all_issues:
    print(f"VALIDATION FAILED on {len(all_issues)} words:")
    for w, iss in all_issues.items():
        print(f"❌ {w}:")
        for i in iss:
            print(f"   - {i}")
else:
    print("ALL 74 WORDS PASSED PRE-VALIDATION!")
