# -*- coding: utf-8 -*-
"""
Validation script for curate_food_b4.py
"""
import sys
import re

sys.stdout.reconfigure(encoding="utf-8")
sys.path.append(".")

from scratch.curate_food_b4 import data_food_b4

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

expected_vin = ['alvine', 'asvina', 'asvins', 'convince', 'convinced', 'convincible', 'convincing', 'convincingly', 'convincingness', 'corvine', 'divination', 'divinatory', 'divine', 'divinely', 'diviner', 'divinity', 'evince', 'invincibility', 'invincible', 'invincibly', 'province', 'provincial', 'provincialism', 'provincially', 'unconvinced', 'unconvincing', 'unconvincingly', 'vinaceous', 'vinaigrette', 'vinca', 'vincetoxicum', 'vincible', 'vincristine', 'vine', 'vinegar', 'vinegariness', 'vinegarish', 'vinegarishness', 'vinegarroon', 'vinegarweed', 'vinegary', 'vinery', 'vineyard', 'viniculture', 'vinifera', 'vinification', 'vinify', 'vino', 'vinogradoff', 'vinology', 'vinous', 'vinson', 'vintage', 'vintager', 'vintner', 'viny', 'vinyl', 'vinylbenzene', 'vinylite']
expected_vor = ['aphidivorous', 'carnivore', 'carnivorous', 'detritivore', 'divorce', 'divorced', 'divorcee', 'divorcement', 'equivorous', 'frugivore', 'herbivore', 'herbivorous', 'insectivore', 'insectivorous', 'omnivore', 'omnivorous', 'panivorous', 'phytivorous', 'piscivore', 'piscivorous', 'pupivorous', 'voracious', 'voraciously', 'voraciousness', 'voracity', 'vorarephile', 'vorarephilia', 'vortex', 'vorticella']

expected_all = expected_vin + expected_vor

print(f"Total entries in curate_food_b4: {len(data_food_b4)}")

issues = 0

for w in expected_all:
    if w not in data_food_b4:
        print(f"Missing expected word: {w}")
        issues += 1

for word, data in data_food_b4.items():
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
        
    # Jaccard check
    p_tokens = set(re.findall(r'\w+', p.lower()))
    s_tokens = set(re.findall(r'\w+', s.lower()))
    inter = p_tokens.intersection(s_tokens)
    union = p_tokens.union(s_tokens)
    jaccard = len(inter) / max(len(union), 1)
    if jaccard >= 0.70:
        print(f"[{word}] High Jaccard similarity: {jaccard:.2f}")
        issues += 1
        
    # Check quotes count
    if len(qs) != 3:
        print(f"[{word}] Quotes count != 3: {len(qs)}")
        issues += 1
        
    authors = []
    for i, q in enumerate(qs):
        auth = q.get("author", "").strip()
        work = q.get("work", "").strip()
        quote = q.get("quote", "").strip()
        authors.append(auth)
        
        if len(auth) < 3:
            print(f"[{word}] Author too short: '{auth}'")
            issues += 1
        if len(work) < 2:
            print(f"[{word}] Work title too short: '{work}'")
            issues += 1
        if not quote.startswith("**") and "**" not in quote:
            print(f"[{word}] Target word not bolded in quote {i}: {quote[:60]}")
            issues += 1
            
        full_line = f"> - 📜 **{auth} (*{work}*):** *\"{quote}\"*"
        for b in banned:
            if b in full_line:
                print(f"[{word}] Contains banned phrase '{b}' in quote line")
                issues += 1
                
    if len(set(authors)) != len(authors):
        print(f"[{word}] Duplicate authors: {authors}")
        issues += 1

print(f"\nValidation completed. Total issues: {issues}")
if issues == 0:
    print("ALL 88 WORDS PASSED PRE-VALIDATION CHECK!")
