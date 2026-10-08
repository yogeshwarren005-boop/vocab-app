# -*- coding: utf-8 -*-
"""
Validation suite for data_food_b1
"""
import sys, re

sys.stdout.reconfigure(encoding="utf-8")

def validate_food_data(data):
    banned_phrases = [
        "In specialized and domain usage, denoting specific qualities",
        "In technical and systematic terminology, the action",
        "In functional and operational contexts, an agent",
        "The clinical presentation of",
        "Every pathological manifestation of",
        "The gradual evolutionary modification of",
        "In academic literature,",
        "Academic Lexicon",
        "Classic Author"
    ]
    
    circular_pattern = re.compile(
        r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b',
        re.I
    )

    errors = []
    
    for word, entry in data.items():
        # Check primary
        p = entry.get("primary", "").strip()
        if len(p) < 25:
            errors.append(f"{word}: Primary definition too short ({len(p)} chars)")
        if circular_pattern.search(p):
            errors.append(f"{word}: Primary definition contains circular boilerplate formula")
        for bp in banned_phrases:
            if bp in p:
                errors.append(f"{word}: Primary contains banned phrase '{bp}'")
                
        # Check secondary
        s = entry.get("secondary", "").strip()
        if len(s) < 25:
            errors.append(f"{word}: Secondary definition too short ({len(s)} chars)")
        if circular_pattern.search(s):
            errors.append(f"{word}: Secondary definition contains circular boilerplate formula")
        for bp in banned_phrases:
            if bp in s:
                errors.append(f"{word}: Secondary contains banned phrase '{bp}'")
                
        # Similarity check
        pTokens = set(re.findall(r'\w+', p.lower()))
        sTokens = set(re.findall(r'\w+', s.lower()))
        intersect = pTokens.intersection(sTokens)
        union = pTokens.union(sTokens)
        jaccard = len(intersect) / max(len(union), 1)
        if jaccard >= 0.70:
            errors.append(f"{word}: Definitions excessively similar (Jaccard = {jaccard:.2f})")
            
        # Quotes check
        quotes = entry.get("quotes", [])
        if len(quotes) != 3:
            errors.append(f"{word}: Expected exactly 3 quotes, found {len(quotes)}")
            
        authors = []
        for idx, q in enumerate(quotes):
            auth = q.get("author", "").strip()
            work = q.get("work", "").strip()
            quote_text = q.get("quote", "").strip()
            
            if len(auth) < 3:
                errors.append(f"{word} quote {idx+1}: Author too short ('{auth}')")
            if len(work) < 2:
                errors.append(f"{word} quote {idx+1}: Work too short ('{work}')")
            authors.append(auth)
            
            for bp in banned_phrases:
                if bp in auth or bp in work or bp in quote_text:
                    errors.append(f"{word} quote {idx+1}: Contains banned phrase '{bp}'")
                    
            # Check bolding in quote
            if "**" not in quote_text:
                errors.append(f"{word} quote {idx+1}: Target word not bolded in quote")
                
            # Check citation line formatting as parsed by audit script
            qLine = f"> - 📜 **{auth} (*{work}*):** *\"{quote_text}\"*"
            authMatch = re.search(r'📜\s*\*\*([^*]+?)\s*(?:\(\*([^*]+?)\*\):?\*\*|\*\*\s*\(\*([^*]+?)\*\):?)', qLine)
            if not authMatch:
                errors.append(f"{word} quote {idx+1}: Malformed citation format: {qLine[:60]}")
            colonMatch = re.search(r':\*\*\s*(.+)$', qLine)
            if not colonMatch:
                errors.append(f"{word} quote {idx+1}: Colon match failed: {qLine[:60]}")
            else:
                quoteBody = colonMatch.group(1)
                if "**" not in quoteBody:
                    errors.append(f"{word} quote {idx+1}: Audit check failed - bold missing in quoteBody")
                    
        unique_authors = set(authors)
        if len(unique_authors) < len(quotes):
            errors.append(f"{word}: Duplicate authors in quotes ({', '.join(authors)})")
            
    return errors
