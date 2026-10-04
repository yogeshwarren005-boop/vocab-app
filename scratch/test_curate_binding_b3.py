# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding="utf-8")
sys.path.append(".")

from scratch.curate_binding_b3 import data_binding_b3

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

lig_words = ['alligator', 'alligatored', 'alligatorfish', 'alligatoridae', 'colligate', 'colligation', 'coreligionist', 'diligence', 'diligent', 'diligently', 'disoblige', 'disobliging', 'eligibility', 'eligible', 'ineligibility', 'ineligible', 'irreligion', 'irreligionist', 'irreligious', 'irreligiousness', 'ligament', 'ligan', 'ligand', 'ligate', 'ligation', 'ligature', 'liger', 'ligne', 'ligneous', 'lignify', 'lignin', 'lignite', 'lignosae', 'lignum', 'ligularia', 'ligule', 'liguria', 'ligustrum', 'nonobligatory', 'obligate', 'obligated', 'obligation', 'obligational', 'obligato', 'obligatorily', 'obligatory', 'oblige', 'obliged', 'obliger', 'obliging', 'obligingly', 'obligingness', 'oligarch', 'oligarchic', 'oligarchical', 'oligarchy', 'religion', 'religionism', 'religionist', 'religiosity', 'religious', 'religiousism', 'religiously', 'religiousness', 'unobligated', 'unobliging']
strict_words = ['constrict', 'constricted', 'constricting', 'constriction', 'constrictive', 'constrictor', 'derestrict', 'district', 'nonrestrictive', 'restrict', 'restricted', 'restricting', 'restriction', 'restrictive', 'restrictively', 'restrictiveness', 'strict', 'strictly', 'strictness', 'stricture', 'unconstricted', 'unrestricted', 'unrestrictive']
string_words = ['astringe', 'astringence', 'astringency', 'astringent', 'constringe', 'nonastringent', 'string', 'stringency', 'stringent', 'stringently', 'stringer', 'strings', 'stringy', 'stringybark', 'substring', 'superstring', 'unstring']

req_words = set(lig_words + strict_words + string_words)

print(f"Total entries in data_binding_b3: {len(data_binding_b3)}")

diff = req_words - set(data_binding_b3.keys())
if diff:
    print(f"Missing words: {diff}")
    sys.exit(1)

extra = set(data_binding_b3.keys()) - req_words
if extra:
    print(f"Extra words: {extra}")
    sys.exit(1)

issues = 0
for word, data in data_binding_b3.items():
    p = data.get("primary", "").strip()
    s = data.get("secondary", "").strip()
    qs = data.get("quotes", [])
    
    if len(p) < 25:
        print(f"[{word}] Primary too short: {len(p)} ('{p}')")
        issues += 1
    if circular_re.search(p):
        print(f"[{word}] Primary circular boilerplate: {p}")
        issues += 1
        
    if len(s) < 25:
        print(f"[{word}] Secondary too short: {len(s)} ('{s}')")
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
    print("ALL 106 ENTRIES IN curate_binding_b3.py VALIDATED WITH ZERO ISSUES!")
else:
    print(f"TOTAL ISSUES: {issues}")
    sys.exit(1)
