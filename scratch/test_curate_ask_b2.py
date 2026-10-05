# -*- coding: utf-8 -*-
"""
test_curate_ask_b2.py
Full audit test for curate_ask_b2.py (82 words across rog and pris).
"""
import sys
import os
import re

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("scratch"))

from curate_ask_b2 import data_ask_b2

expected_rog = [
    'abrogate', 'abrogation', 'abrogator', 'acrogen', 'acrogenic', 'acrogenous',
    'anterograde', 'arrogance', 'arrogant', 'arrogantly', 'arrogate', 'arrogation',
    'arrogator', 'derogate', 'derogation', 'derogative', 'derogatory', 'erogenous',
    'interrogate', 'interrogation', 'interrogative', 'interrogatively', 'interrogator',
    'interrogatory', 'prerogative', 'prorogation', 'prorogue', 'rogaine', 'rogation',
    'rogers', 'roget', 'rogue', 'roguery', 'roguish', 'roguishly', 'roguishness',
    'subrogate', 'subrogation', 'supererogatory', 'surrogate'
]

expected_pris = [
    'apprisal', 'apprise', 'comprise', 'enterprise', 'enterpriser', 'enterprising',
    'enterprisingly', 'enterprisingness', 'imprison', 'imprisoned', 'imprisonment',
    'nonenterprising', 'priscoan', 'prise', 'prism', 'prismatic', 'prismatoid',
    'prismoid', 'prison', 'prison-breaking', 'prisonbreak', 'prisoner', 'prisonlike',
    'prissily', 'prissy', 'pristidae', 'pristine', 'pristis', 'reprisal', 'reprise',
    'surprisal', 'surprise', 'surprised', 'surprisedly', 'surpriser', 'surprising',
    'surprisingly', 'surprisingness', 'unenterprising', 'unimprisoned', 'unsurprised',
    'unsurprising'
]

expected_all = set(expected_rog + expected_pris)

print(f"Total in dictionary: {len(data_ask_b2)}")
print(f"Total expected: {len(expected_all)}")

missing = expected_all - set(data_ask_b2.keys())
extra = set(data_ask_b2.keys()) - expected_all
if missing:
    print(f"MISSING WORDS: {missing}")
if extra:
    print(f"EXTRA WORDS: {extra}")

banned = [
  'In specialized and domain usage, denoting specific qualities',
  'In technical and systematic terminology, the action',
  'In functional and operational contexts, an agent',
  'The clinical presentation of',
  'Every pathological manifestation of',
  'The gradual evolutionary modification of',
  'In academic literature,',
  'Academic Lexicon',
  'Classic Author'
]

circular_re = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.IGNORECASE)

issues = 0
for word, data in data_ask_b2.items():
    p = data.get("primary", "").strip()
    s = data.get("secondary", "").strip()
    qs = data.get("quotes", [])
    
    if len(p) < 25:
        print(f"[{word}] Primary too short ({len(p)}): {p}")
        issues += 1
    if circular_re.search(p):
        print(f"[{word}] Primary circular boilerplate: {p}")
        issues += 1
        
    if len(s) < 25:
        print(f"[{word}] Secondary too short ({len(s)}): {s}")
        issues += 1
    if circular_re.search(s):
        print(f"[{word}] Secondary circular boilerplate: {s}")
        issues += 1
        
    if p.lower() == s.lower():
        print(f"[{word}] Duplicate definitions: {p}")
        issues += 1
        
    p_tokens = set(re.findall(r'\w+', p.lower()))
    s_tokens = set(re.findall(r'\w+', s.lower()))
    if p_tokens and s_tokens:
        overlap = len(p_tokens & s_tokens) / max(len(p_tokens | s_tokens), 1)
        if overlap >= 0.70:
            print(f"[{word}] Definitions too similar (Jaccard {overlap:.2f})")
            issues += 1
            
    for b in banned:
        if b in p or b in s:
            print(f"[{word}] Contains banned phrase in def: {b}")
            issues += 1
            
    if len(qs) != 3:
        print(f"[{word}] Expected 3 quotes, got {len(qs)}")
        issues += 1
        
    authors = []
    for i, q in enumerate(qs):
        auth = q.get("author", "").strip()
        work = q.get("work", "").strip()
        quote = q.get("quote", "").strip()
        
        authors.append(auth)
        if len(auth) < 3:
            print(f"[{word}] Quote {i+1} author too short: {auth}")
            issues += 1
        if len(work) < 2:
            print(f"[{word}] Quote {i+1} work too short: {work}")
            issues += 1
        if "**" not in quote:
            print(f"[{word}] Quote {i+1} target word not bolded: {quote}")
            issues += 1
            
        for b in banned:
            if b in auth or b in work or b in quote:
                print(f"[{word}] Quote {i+1} contains banned phrase: {b}")
                issues += 1
                
    if len(set(authors)) < len(authors):
        print(f"[{word}] Duplicate author in quotes: {authors}")
        issues += 1

if issues == 0:
    print("ALL 82 WORDS FULLY VALIDATED! 100% PRISTINE DATA!")
else:
    print(f"TOTAL ISSUES DETECTED: {issues}")
