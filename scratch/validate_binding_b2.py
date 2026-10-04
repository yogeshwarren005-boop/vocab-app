import re
import sys
from scratch.curate_binding_b2 import data_binding_b2

issues = []

for word, data in data_binding_b2.items():
    p = data.get("primary", "")
    s = data.get("secondary", "")
    quotes = data.get("quotes", [])
    
    if len(p) < 25:
        issues.append(f"{word}: primary too short ({len(p)})")
    if re.search(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', p, re.IGNORECASE):
        issues.append(f"{word}: primary circular formula")
        
    if len(s) < 25:
        issues.append(f"{word}: secondary too short ({len(s)})")
    if re.search(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', s, re.IGNORECASE):
        issues.append(f"{word}: secondary circular formula")
        
    p_tokens = set(re.findall(r'\w+', p.lower()))
    s_tokens = set(re.findall(r'\w+', s.lower()))
    intersect = p_tokens & s_tokens
    union = p_tokens | s_tokens
    jaccard = len(intersect) / max(len(union), 1)
    if jaccard >= 0.70:
        issues.append(f"{word}: Jaccard overlap too high ({jaccard:.2f})")
        
    if len(quotes) != 3:
        issues.append(f"{word}: quotes count != 3 ({len(quotes)})")
        
    authors = []
    for i, q in enumerate(quotes):
        auth = q.get("author", "")
        wrk = q.get("work", "")
        txt = q.get("quote", "")
        authors.append(auth)
        if len(auth) < 3:
            issues.append(f"{word}: short author '{auth}'")
        if len(wrk) < 2:
            issues.append(f"{word}: short work '{wrk}'")
        if not re.search(r'\*\*[^*]+\*\*', txt):
            issues.append(f"{word}: quote {i} missing bold target word: {txt[:50]}")
            
    if len(set(authors)) < len(quotes):
        issues.append(f"{word}: duplicate author in quotes: {authors}")

if issues:
    print(f"FAILED with {len(issues)} issues:")
    for iss in issues:
        print("  -", iss)
    sys.exit(1)
else:
    print("ALL 58 WORDS PASSED STRICT CRITERIA VALIDATION!")
