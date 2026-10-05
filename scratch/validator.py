import re

def validate_entry(word, data):
    issues = []
    # Primary def
    p = data.get("primary", "")
    if len(p) < 25:
        issues.append(f"Primary definition too short ({len(p)} chars)")
    if re.search(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', p, re.IGNORECASE):
        issues.append("Primary definition contains circular boilerplate formula")
    
    # Secondary def
    s = data.get("secondary", "")
    if len(s) < 25:
        issues.append(f"Secondary definition too short ({len(s)} chars)")
    if re.search(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', s, re.IGNORECASE):
        issues.append("Secondary definition contains circular boilerplate formula")
    
    if p.strip().lower() == s.strip().lower():
        issues.append("Duplicate definition (p == s)")
    else:
        p_toks = set(re.findall(r'\w+', p.lower()))
        s_toks = set(re.findall(r'\w+', s.lower()))
        inter = p_toks.intersection(s_toks)
        union = p_toks.union(s_toks)
        jacc = len(inter) / max(len(union), 1)
        if jacc >= 0.70:
            issues.append(f"Definitions excessively similar (Jaccard = {jacc:.2f})")
    
    # Quotes
    quotes = data.get("quotes", [])
    if len(quotes) != 3:
        issues.append(f"Expected exactly 3 quotes, found {len(quotes)}")
    
    authors = []
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
    
    for q in quotes:
        auth = q.get("author", "").strip()
        work = q.get("work", "").strip()
        quote = q.get("quote", "").strip()
        authors.append(auth)
        
        if len(auth) < 3:
            issues.append(f"Suspiciously short author: '{auth}'")
        if len(work) < 2:
            issues.append(f"Suspiciously short work: '{work}'")
            
        full_line = f'> - 📜 **{auth} (*{work}*):** *"{quote}"*'
        for b in banned:
            if b in full_line or b in p or b in s:
                issues.append(f"Contains banned phrase: '{b}'")
        
        if '**' not in quote:
            issues.append(f"Target word not bolded in quote: '{quote[:40]}...'")
    
    if len(set(authors)) < len(quotes):
        issues.append(f"Duplicate authors: {authors}")
        
    return issues
