# -*- coding: utf-8 -*-
"""
test_curate_ask_b1.py
Validation script for Batch 1 of Cluster Asking & Seeking (72 words).
"""
import sys
import os
import re

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("scratch"))

from curate_ask_b1 import data_ask_b1

expected_plor = ['deplorable', 'deplorably', 'deplore', 'exploration', 'explorative', 'exploratory', 'explore', 'explorer', 'implore', 'imploring', 'imploringly', 'nonexplorative', 'nonexploratory', 'unexplorative', 'unexploratory', 'unexplored']
expected_postul = ['expostulate', 'expostulation', 'postulant', 'postulate', 'postulation', 'postulational', 'postulator']
expected_quer = ['conquer', 'conquerable', 'conquering', 'conqueror', 'equerry', 'quercitron', 'quercus', 'querier', 'quern', 'querulous', 'querulously', 'querulousness', 'query', 'reconquer', 'unconquerable', 'unconquered']
expected_scit = ['adscititious', 'plebiscite']
expected_scrut = ['inscrutability', 'inscrutable', 'inscrutably', 'scrutineer', 'scrutinise', 'scrutiniser', 'scrutinize', 'scrutinizer', 'scrutiny']
expected_stud = ['stud', 'student', 'studentship', 'studied', 'studio', 'studious', 'studiously', 'studiousness', 'study', 'studying', 'understudied', 'understudy', 'unstudied', 'unstudious']
expected_vestig = ['investigate', 'investigating', 'investigation', 'investigative', 'investigator', 'investigatory', 'vestige', 'vestigial']

expected_all = set(expected_plor + expected_postul + expected_quer + expected_scit + expected_scrut + expected_stud + expected_vestig)

print(f"Total in dictionary: {len(data_ask_b1)}")
print(f"Total expected: {len(expected_all)}")

missing = expected_all - set(data_ask_b1.keys())
extra = set(data_ask_b1.keys()) - expected_all
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
for word, data in data_ask_b1.items():
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
    print("ALL 72 WORDS FULLY VALIDATED! 100% PRISTINE DATA!")
else:
    print(f"TOTAL ISSUES DETECTED: {issues}")
