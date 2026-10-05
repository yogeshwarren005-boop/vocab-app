# -*- coding: utf-8 -*-
"""
Verification test script for scratch/curate_fire_cal_p1.py
"""
import sys, re

sys.stdout.reconfigure(encoding="utf-8")

from scratch.curate_fire_cal_p1 import data_fire_cal_p1

expected_words = [
    'alcalescent', 'calaba', 'calabash', 'calabazilla', 'calabria', 'calabura', 'caladenia', 'caladium', 'calais', 'calamagrostis',
    'calamari', 'calamary', 'calamine', 'calamint', 'calamintha', 'calamitous', 'calamity', 'calamus', 'calan', 'calando',
    'calandrinia', 'calanthe', 'calapooya', 'calapuya', 'calash', 'calc-tufa', 'calcaneal', 'calcaneus', 'calcareous', 'calced',
    'calcedony', 'calceiform', 'calceolaria', 'calceolate', 'calceus', 'calcic', 'calcicolous', 'calciferol', 'calciferous', 'calcific',
    'calcification', 'calcifugous', 'calcify', 'calcimine', 'calcination', 'calcine', 'calcite', 'calcitic', 'calcitonin', 'calcium',
    'calcium-cyanamide', 'calculable', 'calculate', 'calculated', 'calculating', 'calculatingly', 'calculation', 'calculative', 'calculator', 'calculous',
    'calculus', 'calcutta', 'calcuttan', 'calean', 'caleche', 'caledonia', 'calefacient', 'calefaction', 'calefactive', 'calefactory',
    'calendar', 'calender', 'calendered', 'calendric', 'calendrical', 'calendula', 'cali', 'caliber', 'calibrate', 'calibrated'
]

errors = []

print(f"Checking {len(expected_words)} words in data_fire_cal_p1...")

if len(data_fire_cal_p1) != 80:
    errors.append(f"Expected 80 words in data_fire_cal_p1, found {len(data_fire_cal_p1)}")

for w in expected_words:
    if w not in data_fire_cal_p1:
        errors.append(f"Missing word: {w}")
        continue
    
    entry = data_fire_cal_p1[w]
    prim = entry.get("primary", "")
    sec = entry.get("secondary", "")
    quotes = entry.get("quotes", [])
    
    # 1. Length check
    if len(prim) < 25:
        errors.append(f"[{w}] primary definition too short (<25 chars): {len(prim)}")
    if len(sec) < 25:
        errors.append(f"[{w}] secondary definition too short (<25 chars): {len(sec)}")
        
    # 2. Circular boilerplate checks
    circular_patterns = [
        r"quality of being", r"state of being", r"condition of being",
        r"the act of being", r"the fact of being"
    ]
    for cp in circular_patterns:
        if re.search(cp, prim, re.IGNORECASE):
            errors.append(f"[{w}] primary contains circular formula: '{cp}'")
            
    # 3. Quotes count and format
    if len(quotes) != 3:
        errors.append(f"[{w}] quotes count is {len(quotes)}, expected 3")
        
    authors = []
    synthetic_phrases = ["in academic literature", "academic lexicon", "morphological & etymological"]
    
    for idx, q in enumerate(quotes):
        auth = q.get("author", "").strip()
        work = q.get("work", "").strip()
        quote_text = q.get("quote", "").strip()
        
        if not auth or not work or not quote_text:
            errors.append(f"[{w}] quote {idx} missing author, work, or quote text")
            
        authors.append(auth)
        
        # Check synthetic boilerplate
        for sp in synthetic_phrases:
            if sp in quote_text.lower() or sp in auth.lower():
                errors.append(f"[{w}] quote {idx} contains synthetic phrase '{sp}'")
                
        # Check bolding of target word or inflected form
        if "**" not in quote_text:
            errors.append(f"[{w}] quote {idx} has NO bolded word: {quote_text}")
        else:
            bolded_matches = re.findall(r"\*\*([^*]+)\*\*", quote_text)
            # Check if any bolded match is related to target word
            w_clean = w.replace("-", "").lower()
            matched = False
            for bm in bolded_matches:
                bm_clean = bm.replace("-", "").lower()
                # Check root or stem overlap
                if w_clean[:4] in bm_clean or bm_clean[:4] in w_clean:
                    matched = True
                    break
            if not matched:
                errors.append(f"[{w}] quote {idx} bolded word '{bolded_matches}' does not match target word")
                
    # Check 3 distinct authors
    if len(set(authors)) != 3:
        errors.append(f"[{w}] authors are not distinct: {authors}")

if errors:
    print(f"FAILED with {len(errors)} errors:")
    for e in errors:
        print(" -", e)
    sys.exit(1)
else:
    print("ALL 80 ENTRIES PASSED VALIDATION PERFECTLY!")
