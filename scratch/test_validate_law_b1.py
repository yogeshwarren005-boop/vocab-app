import sys
import os
import re

sys.path.insert(0, os.path.abspath("scratch"))
from curate_law_b1 import data_law_b1

knownBannedPhrases = [
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

errors = []

for word, entry in data_law_b1.items():
    p = entry.get('primary', '').strip()
    s = entry.get('secondary', '').strip()
    quotes = entry.get('quotes', [])
    
    if len(p) < 25:
        errors.append(f"{word}: primary too short ({len(p)})")
    if re.search(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', p, re.I):
        errors.append(f"{word}: primary contains circular boilerplate formula")
        
    if len(s) < 25:
        errors.append(f"{word}: secondary too short ({len(s)})")
    if re.search(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', s, re.I):
        errors.append(f"{word}: secondary contains circular boilerplate formula")
        
    if p.lower() == s.lower():
        errors.append(f"{word}: duplicate definitions")
    else:
        p_toks = set(re.findall(r'\w+', p.lower()))
        s_toks = set(re.findall(r'\w+', s.lower()))
        jaccard = len(p_toks & s_toks) / max(len(p_toks | s_toks), 1)
        if jaccard >= 0.70:
            errors.append(f"{word}: jaccard overlap too high ({jaccard:.2f})")
            
    if len(quotes) != 3:
        errors.append(f"{word}: expected 3 quotes, got {len(quotes)}")
        
    authors = []
    for idx, q in enumerate(quotes):
        auth = q.get('author', '').strip()
        work = q.get('work', '').strip()
        quote = q.get('quote', '').strip()
        authors.append(auth)
        
        if len(auth) < 3:
            errors.append(f"{word} q{idx}: author too short ({auth})")
        if len(work) < 2:
            errors.append(f"{word} q{idx}: work too short ({work})")
            
        if '**' not in quote:
            errors.append(f"{word} q{idx}: no bolding in quote")
            
        full_line = f"> - 📜 **{auth} (*{work}*):** *\"{quote}\"*"
        for b in knownBannedPhrases:
            if b in full_line or b in p or b in s:
                errors.append(f"{word}: banned phrase '{b}'")
                
    if len(set(authors)) < len(quotes):
        errors.append(f"{word}: duplicate authors ({authors})")

if errors:
    print(f"Validation FAILED with {len(errors)} errors:")
    for e in errors:
        print("  -", e)
    sys.exit(1)
else:
    print("ALL 77 WORDS PASSED VALIDATION PERFECTLY!")
