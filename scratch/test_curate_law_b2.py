# -*- coding: utf-8 -*-
"""
Validation script for Batch 2 of Cluster Law, Justice & Feudal (95 words).
"""
import sys
import re

sys.stdout.reconfigure(encoding="utf-8")

from scratch.curate_law_b2 import data_law_b2

expected_judic = ['adjudicate', 'adjudication', 'adjudicative', 'adjudicator', 'adjudicatory', 'extrajudicial', 'injudicious', 'injudiciously', 'injudiciousness', 'judicable', 'judicatory', 'judicature', 'judicial', 'judicially', 'judiciary', 'judicious', 'judiciously', 'judiciousness', 'prejudice', 'prejudiced', 'prejudicial', 'prejudicious', 'unprejudiced']
expected_juris = ['jurisdiction', 'jurisdictional', 'jurisprudence', 'jurisprudential', 'jurisprudentially', 'jurist', 'juristic']
expected_just = ['adjust', 'adjustable', 'adjusted', 'adjuster', 'adjustive', 'adjustment', 'adjustor', 'injustice', 'just', 'justice', 'justiciar', 'justiciary', 'justifiable', 'justifiably', 'justification', 'justificative', 'justificatory', 'justified', 'justifiedly', 'justifier', 'justify', 'justinian', 'justly', 'justness', 'readjust', 'readjustment', 'unadjustable', 'unadjusted', 'unjust', 'unjustifiable', 'unjustifiably', 'unjustified', 'unjustly', 'unjustness']
expected_legat = ['allegation', 'delegate', 'delegating', 'delegation', 'legate', 'legatee', 'legateship', 'legation', 'legato', 'relegate', 'relegating', 'relegation']
expected_senat = ['arsenate', 'senate', 'senator', 'senatorial', 'senatorship']
expected_statut = ['statute', 'statutorily', 'statutory']
expected_vindic = ['revindicate', 'unvindictive', 'vindicable', 'vindicate', 'vindicated', 'vindication', 'vindicator', 'vindicatory', 'vindictive', 'vindictively', 'vindictiveness']

expected_all = set(expected_judic + expected_juris + expected_just + expected_legat + expected_senat + expected_statut + expected_vindic)

print(f"Total in dictionary: {len(data_law_b2)}")
print(f"Total expected: {len(expected_all)}")

missing = expected_all - set(data_law_b2.keys())
extra = set(data_law_b2.keys()) - expected_all
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
for word, data in data_law_b2.items():
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
            
        bold_match = re.search(r'\*\*([^*]+)\*\*', text)
        if not bold_match:
            print(f"[{word}] Quote {i} missing bold target: {text}")
            issues += 1
        else:
            bold_term = bold_match.group(1).lower()
            # verify bold_term relates to word stem
            
        full_line = f"> - 📜 **{auth} (*{work}*):** *\"{text}\"*"
        for b in banned:
            if b in full_line or b in p or b in s:
                print(f"[{word}] Contains banned phrase: {b}")
                issues += 1

    if len(set(authors)) < len(qs):
        print(f"[{word}] Duplicate author: {authors}")
        issues += 1

print(f"\nValidation completed with {issues} issues.")
if issues == 0 and not missing and not extra:
    print("ALL 95 WORDS ARE PRISTINE!")
