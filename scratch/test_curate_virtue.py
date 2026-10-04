# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding="utf-8")

from scratch.curate_virtue_opt_rob_virt import data_virtue_opt_rob_virt

expected_opt = ['adopt', 'adoptable', 'adopted', 'adoptee', 'adopter', 'adoption', 'adoptive', 'apoptosis', 'co-opt', 'co-optation', 'co-option', 'diopter', 'dioptre', 'exopterygota', 'opt', 'optative', 'optez', 'optic', 'optical', 'optically', 'optician', 'optics', 'optimal', 'optimally', 'optimisation', 'optimise', 'optimism', 'optimist', 'optimistic', 'optimistically', 'optimization', 'optimize', 'optimum', 'option', 'optional', 'optionally', 'optometrist', 'optometry', 'unadoptable']

expected_rob = ['acrobat', 'acrobates', 'acrobatic', 'acrobatics', 'agrobacterium', 'agrobiologic', 'agrobiological', 'agrobiology', 'arroba', 'corroborant', 'corroborate', 'corroboration', 'corroborative', 'corroboratory', 'disrobe', 'enrobe', 'rob', 'robalo', 'robaxin', 'robber', 'robbery', 'robe', 'robe-de-chambre', 'robed', 'robert', 'roberts', 'robertson', 'robeson', 'robespierre', 'robin', 'robinia', 'robinson', 'robitussin', 'roble', 'roborant', 'robot', 'robotic', 'robotics', 'robotlike', 'robust', 'robustious', 'robustly', 'robustness']

expected_virt = ['virtu', 'virtual', 'virtuality', 'virtually', 'virtue', 'virtuosity', 'virtuoso', 'virtuous', 'virtuously', 'virtuousness']

expected_all = set(expected_opt + expected_rob + expected_virt)

print(f"Total in dictionary: {len(data_virtue_opt_rob_virt)}")
print(f"Total expected: {len(expected_all)}")

missing = expected_all - set(data_virtue_opt_rob_virt.keys())
extra = set(data_virtue_opt_rob_virt.keys()) - expected_all
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
for word, data in data_virtue_opt_rob_virt.items():
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

if issues == 0 and not missing and not extra:
    print("SUCCESS: ALL 92 ENTRIES VALIDATED WITH ZERO ISSUES!")
else:
    print(f"TOTAL ISSUES: {issues}")
    sys.exit(1)
