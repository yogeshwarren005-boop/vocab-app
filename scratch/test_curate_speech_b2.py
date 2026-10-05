# -*- coding: utf-8 -*-
"""
Validation script for curate_speech_b2.py
"""
import sys
import re

sys.stdout.reconfigure(encoding="utf-8")
sys.path.append(".")

from scratch.curate_speech_b2 import data_speech_b2

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

expected_cit = ['ascites', 'ascitic', 'citadel', 'citation', 'cite', 'citellus', 'citified', 'citify', 'citizen', 'citizenry', 'citizenship', 'citlaltepetl', 'citole', 'citrange', 'citrate', 'citric', 'citrin', 'citrine', 'citron', 'citroncirus', 'citronwood', 'citrous', 'citrulline', 'citrullus', 'citrus', 'cittern', 'city', 'city-born', 'city-bred', 'city-like', 'city-state', 'cityfied', 'cityscape', 'citywide', 'excitability', 'excitable', 'excitableness', 'excitant', 'excitation', 'excitative', 'excitatory', 'excite', 'excited', 'excitedly', 'excitement', 'exciting', 'excitingly', 'incitation', 'incite', 'incitement', 'inciter', 'incitive', 'noncitizen', 'occitan', 'overexcited', 'recital', 'recitalist', 'recitation', 'recitative', 'recite', 'reciter', 'unexcitable', 'unexcited', 'unexciting', 'unexcitingly']
expected_nunci = ['annunciate', 'annunciation', 'annunciator', 'annunciatory', 'denunciation', 'denunciative', 'denunciatory', 'enunciate', 'enunciation', 'internuncio', 'mispronunciation', 'nuncio', 'pronunciamento', 'pronunciation', 'renunciant', 'renunciation', 'renunciative']

expected_all = expected_cit + expected_nunci

print(f"Total entries in curate_speech_b2: {len(data_speech_b2)}")

issues = 0

for w in expected_all:
    if w not in data_speech_b2:
        print(f"Missing expected word: {w}")
        issues += 1

for word, data in data_speech_b2.items():
    p = data.get("primary", "").strip()
    s = data.get("secondary", "").strip()
    qs = data.get("quotes", [])
    
    if len(p) < 25:
        print(f"[{word}] Primary too short: {len(p)}")
        issues += 1
    if circular_re.search(p):
        print(f"[{word}] Primary circular boilerplate: {p}")
        issues += 1
        
    if len(s) < 25:
        print(f"[{word}] Secondary too short: {len(s)}")
        issues += 1
    if circular_re.search(s):
        print(f"[{word}] Secondary circular boilerplate: {s}")
        issues += 1
        
    if p.lower() == s.lower():
        print(f"[{word}] Duplicate definitions")
        issues += 1
        
    p_tok = set(re.findall(r'\w+', p.lower()))
    s_tok = set(re.findall(r'\w+', s.lower()))
    jaccard = len(p_tok & s_tok) / max(len(p_tok | s_tok), 1)
    if jaccard >= 0.70:
        print(f"[{word}] High Jaccard overlap: {jaccard:.2f}")
        issues += 1
        
    if len(qs) != 3:
        print(f"[{word}] Expected 3 quotes, got {len(qs)}")
        issues += 1
        
    authors = []
    for i, q in enumerate(qs):
        auth = q.get("author", "").strip()
        work = q.get("work", "").strip()
        text = q.get("quote", "").strip()
        authors.append(auth)
        
        if len(auth) < 3:
            print(f"[{word}] Short author: {auth}")
            issues += 1
        if len(work) < 2:
            print(f"[{word}] Short work: {work}")
            issues += 1
        if not re.search(r'\*\*[^*]+\*\*', text):
            print(f"[{word}] Quote {i} missing bold target: {text}")
            issues += 1
            
        full_line = f"> - 📜 **{auth} (*{work}*):** *\"{text}\"*"
        for b in banned:
            if b in full_line or b in p or b in s:
                print(f"[{word}] Contains banned phrase: {b}")
                issues += 1

    if len(set(authors)) < len(qs):
        print(f"[{word}] Duplicate author: {authors}")
        issues += 1

if issues == 0:
    print(f"ALL {len(data_speech_b2)} ENTRIES IN curate_speech_b2.py VALIDATED WITH ZERO ISSUES!")
else:
    print(f"TOTAL ISSUES: {issues}")
    sys.exit(1)
