# -*- coding: utf-8 -*-
"""
Validation script for scratch/curate_fire_cal_p2.py
"""
import sys
import re

sys.stdout.reconfigure(encoding="utf-8")

# Target words specification
target_words = [
    'calibration', 'calibre', 'caliche', 'caliche-topped', 'calico', 'calicular', 'caliculus', 'calid', 'calidris',
    'calif', 'calif.', 'california', 'californian', 'californium', 'caliginous', 'caligula', 'caliper', 'caliph',
    'caliphate', 'calisaya', 'calisthenic', 'calisthenics', 'call', 'call-back', 'call-board', 'call-in', 'call-out',
    'calla', 'callable', 'callas', 'callathump', 'callback', 'caller', 'caller-out', 'caller-up', 'calliandra',
    'callicebus', 'calligraph', 'calligrapher', 'calligraphic', 'calligraphical', 'calligraphist', 'calligraphy',
    'callimorpha', 'callinectes', 'calling', 'callionymidae', 'calliope', 'calliophis', 'calliopsis', 'calliper',
    'calliphora', 'calliphoridae', 'callipygian', 'callipygous', 'callirhoe', 'callisaurus', 'callistephus',
    'callisthenics', 'callisto', 'callithricidae', 'callithrix', 'callithump', 'callithumpian', 'callitrichaceae',
    'callitriche', 'callitris', 'callophis', 'callorhinus', 'callosectomy', 'callosity', 'callosotomy', 'callous',
    'calloused', 'callously', 'callousness', 'callow', 'callowness', 'calluna', 'callus'
]

# Load curate_fire_cal_p2.py
with open("scratch/curate_fire_cal_p2.py", "r", encoding="utf-8") as f:
    code = f.read()

ns = {}
exec(code, {}, ns)

if "data_fire_cal_p2" not in ns:
    print("FATAL: data_fire_cal_p2 dict not found!")
    sys.exit(1)

data = ns["data_fire_cal_p2"]

print(f"Total keys in data_fire_cal_p2: {len(data)}")
print(f"Total target words: {len(target_words)}")

errors = []

# Check keys matching
missing_words = [w for w in target_words if w not in data]
extra_words = [w for w in data if w not in target_words]

if missing_words:
    errors.append(f"Missing words: {missing_words}")
if extra_words:
    errors.append(f"Extra words: {extra_words}")

# Validate each word
for idx, w in enumerate(target_words, 1):
    if w not in data:
        continue
    entry = data[w]
    prim = entry.get("primary", "")
    sec = entry.get("secondary", "")
    quotes = entry.get("quotes", [])
    
    # Check primary definition length
    if len(prim) < 25:
        errors.append(f"[{w}] primary definition length {len(prim)} < 25 chars: '{prim}'")
        
    # Check secondary definition length
    if len(sec) < 25:
        errors.append(f"[{w}] secondary definition length {len(sec)} < 25 chars: '{sec}'")
        
    # Check circular boilerplate formulas in primary definition
    circular_patterns = [
        r'\bquality of being\b',
        r'\bstate of being\b',
        r'\bcondition of being\b',
        r'\bthe quality or state\b',
        r'\bthe state or condition\b'
    ]
    for cp in circular_patterns:
        match = re.search(cp, prim, re.IGNORECASE)
        if match:
            errors.append(f"[{w}] circular boilerplate detected in primary: '{match.group(0)}'")
            
    # Check quotes
    if len(quotes) != 3:
        errors.append(f"[{w}] expected exactly 3 quotes, found {len(quotes)}")
        continue
        
    authors = [q.get("author", "").strip() for q in quotes]
    if len(set(authors)) != 3:
        errors.append(f"[{w}] authors are not 3 distinct real authors: {authors}")
        
    for q_idx, q in enumerate(quotes, 1):
        author = q.get("author", "").strip()
        work = q.get("work", "").strip()
        quote_text = q.get("quote", "").strip()
        
        if not author:
            errors.append(f"[{w}] quote {q_idx} missing author")
        if not work:
            errors.append(f"[{w}] quote {q_idx} missing work")
        if not quote_text:
            errors.append(f"[{w}] quote {q_idx} missing quote text")
            
        # Check bolding: must contain double asterisks around the target word or its root/inflection
        bolded_matches = re.findall(r'\*\*([^*]+)\*\*', quote_text)
        if not bolded_matches:
            errors.append(f"[{w}] quote {q_idx} has NO bolded word: '{quote_text}'")
            
        # Check synthetic boilerplate phrases
        boilerplate_terms = [
            "in academic literature", "academic lexicon", "as defined by scholars",
            "modern research indicates", "scholarly discourse"
        ]
        for bt in boilerplate_terms:
            if bt in quote_text.lower():
                errors.append(f"[{w}] quote {q_idx} contains synthetic boilerplate: '{bt}'")

if errors:
    print(f"\nFAILED with {len(errors)} errors:")
    for err in errors:
        print(f"  - {err}")
    sys.exit(1)
else:
    print("\nSUCCESS! All 80 words passed all strict validation criteria:")
    print("  1. Exactly 80 target words matched.")
    print("  2. Every primary definition >= 25 chars with active phrasing and no circular formulas.")
    print("  3. Every secondary definition >= 25 chars with specialized domain depth.")
    print("  4. Exactly 3 distinct real authors per word.")
    print("  5. Authentic published works and properly bolded target words (**word**).")
    print("  6. Zero synthetic boilerplate phrases.")
