# -*- coding: utf-8 -*-
"""
curate_botany_b1.py
Combines Cluster Botany Batch 1 Part 1 (55 words) and Part 2 (54 words)
Total: 109 words across 12 dashboards
"""
import sys
import re

sys.stdout.reconfigure(encoding="utf-8")
sys.path.append(".")

from scratch.curate_botany_b1_p1 import data_botany_b1_p1
from scratch.curate_botany_b1_p2 import data_botany_b1_p2

data_botany_b1 = {}
data_botany_b1.update(data_botany_b1_p1)
data_botany_b1.update(data_botany_b1_p2)

def validate_all(data):
    circular_pattern = re.compile(
        r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b',
        re.IGNORECASE
    )
    errors = []
    
    for word, entry in data.items():
        primary = entry.get("primary", "")
        secondary = entry.get("secondary", "")
        quotes = entry.get("quotes", [])
        
        # Check lengths
        if len(primary) < 25:
            errors.append(f"[{word}] Primary definition too short (<25 chars): '{primary}'")
        if len(secondary) < 25:
            errors.append(f"[{word}] Secondary definition too short (<25 chars): '{secondary}'")
            
        # Check circular
        if circular_pattern.search(primary):
            errors.append(f"[{word}] Primary definition contains circular boilerplate formula: '{primary}'")
        if circular_pattern.search(secondary):
            errors.append(f"[{word}] Secondary definition contains circular boilerplate formula: '{secondary}'")
            
        # Check overlap
        p_tokens = set(re.findall(r'[a-zA-Z]{3,}', primary.lower()))
        s_tokens = set(re.findall(r'[a-zA-Z]{3,}', secondary.lower()))
        if p_tokens and s_tokens:
            intersection = p_tokens.intersection(s_tokens)
            union = p_tokens.union(s_tokens)
            jaccard = len(intersection) / len(union)
            if jaccard >= 0.70:
                errors.append(f"[{word}] Jaccard overlap between definitions too high: {jaccard:.2f}")
                
        # Check quotes
        if len(quotes) != 3:
            errors.append(f"[{word}] Quotes count != 3 (found {len(quotes)})")
            
        authors = [q.get("author", "").strip() for q in quotes]
        if len(set(authors)) != 3:
            errors.append(f"[{word}] Authors not distinct: {authors}")
            
        for i, q in enumerate(quotes):
            text = q.get("quote", "")
            if "**" not in text:
                errors.append(f"[{word}] Quote {i+1} missing bold target word: '{text}'")
                
    return errors

if __name__ == "__main__":
    print(f"Total words in data_botany_b1: {len(data_botany_b1)}")
    errs = validate_all(data_botany_b1)
    if errs:
        print(f"\n❌ VALIDATION FAILED with {len(errs)} errors:")
        for e in errs:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("\n✅ ALL 109 words in Cluster Botany Batch 1 PASSED local pre-audit validation!")
