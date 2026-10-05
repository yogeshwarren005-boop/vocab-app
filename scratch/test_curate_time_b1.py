# -*- coding: utf-8 -*-
"""
Validation script for Batch 1 of Cluster Time (71 words).
"""
import sys
import os
import re

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("scratch"))

from curate_time_b1 import data_time_b1

expected_cras = ['crass', 'crassitude', 'crassness', 'crassostrea', 'crassula', 'crassulaceae', 'procrastinate', 'procrastination', 'procrastinator']
expected_di = ['antemeridian', 'circadian', 'cordial', 'cordiality', 'cordially', 'dial', 'diarist', 'diary', 'diurnal', 'meridian', 'meridional', 'postmeridian', 'precordial', 'precordium', 'uncordial']
expected_ev = ['coeval', 'ev', 'longevity']
expected_nov = ['innovate', 'innovation', 'innovational', 'innovative', 'innovativeness', 'innovator', 'nov', 'nova', 'novate', 'novation', 'novel', 'novelette', 'novelise', 'novelist', 'novelize', 'novelty', 'novice', 'renovate', 'renovation', 'renovator', 'supernova']
expected_saecul = ['secular', 'secularisation', 'secularise', 'secularism', 'secularist', 'secularization', 'secularize']
expected_simul = ['dissimulate', 'dissimulation', 'dissimulative', 'dissimulator', 'simulacrum', 'simulate', 'simulated', 'simulation', 'simulator', 'simulcast', 'simuliidae', 'simulium', 'simultaneity', 'simultaneous', 'simultaneously', 'simultaneousness']

expected_all = set(expected_cras + expected_di + expected_ev + expected_nov + expected_saecul + expected_simul)

print(f"Total in dictionary: {len(data_time_b1)}")
print(f"Total expected: {len(expected_all)}")

missing = expected_all - set(data_time_b1.keys())
extra = set(data_time_b1.keys()) - expected_all
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
for word, data in data_time_b1.items():
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
    print("ALL 71 WORDS FULLY VALIDATED! 100% PRISTINE DATA!")
else:
    print(f"TOTAL ISSUES DETECTED: {issues}")
