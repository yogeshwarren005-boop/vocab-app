# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import re
from scratch.curate_speech_b1_articul import data_articul
from scratch.curate_speech_b1_claim import data_claim
from scratch.curate_speech_b1_clam import data_clam
from scratch.curate_speech_b1_rest import data_fari, data_garrul, data_orat, data_suad

all_datasets = {
    'articul': data_articul,
    'claim': data_claim,
    'clam': data_clam,
    'fari': data_fari,
    'garrul': data_garrul,
    'orat': data_orat,
    'suad': data_suad
}

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

total_words = 0
all_issues = []

for dname, data in all_datasets.items():
    print(f"Checking {dname}: {len(data)} words")
    total_words += len(data)
    for word, entry in data.items():
        p = entry['primary'].strip()
        s = entry['secondary'].strip()
        quotes = entry['quotes']
        
        # 1. Primary
        if len(p) < 25:
            all_issues.append(f"[{word}] Primary definition too short ({len(p)} chars)")
        if re.search(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', p, re.I):
            all_issues.append(f"[{word}] Primary definition circular formula: {p}")
            
        # 2. Secondary
        if len(s) < 25:
            all_issues.append(f"[{word}] Secondary definition too short ({len(s)} chars)")
        if re.search(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', s, re.I):
            all_issues.append(f"[{word}] Secondary definition circular formula: {s}")
            
        # 3. Jaccard / duplicate
        if p.lower() == s.lower():
            all_issues.append(f"[{word}] Duplicate Definition")
        else:
            pTokens = set(re.findall(r'\w+', p.lower()))
            sTokens = set(re.findall(r'\w+', s.lower()))
            intersect = pTokens.intersection(sTokens)
            union = pTokens.union(sTokens)
            jaccard = len(intersect) / max(len(union), 1)
            if jaccard >= 0.70:
                all_issues.append(f"[{word}] Definitions excessively similar ({jaccard:.2f})")
                
        # 4. Banned phrases
        for phrase in knownBannedPhrases:
            if phrase.lower() in p.lower() or phrase.lower() in s.lower():
                all_issues.append(f"[{word}] Banned phrase in definition: {phrase}")
                
        # 5. Quotes
        if len(quotes) != 3:
            all_issues.append(f"[{word}] Expected 3 quotes, found {len(quotes)}")
        authors = []
        for q in quotes:
            a = q.get('author', '').strip()
            w = q.get('work', '').strip()
            text = q.get('quote', '').strip()
            authors.append(a)
            if len(a) < 3 or len(w) < 2:
                all_issues.append(f"[{word}] Suspicious author/work: {a} / {w}")
            if '**' not in text:
                all_issues.append(f"[{word}] Target word not bolded in quote: {text[:40]}")
            for phrase in knownBannedPhrases:
                if phrase.lower() in a.lower() or phrase.lower() in w.lower() or phrase.lower() in text.lower():
                    all_issues.append(f"[{word}] Banned phrase in quote: {phrase}")
        if len(set(authors)) < len(quotes):
            all_issues.append(f"[{word}] Duplicate author in quotes: {authors}")

print(f"\nTotal words checked: {total_words}")
if all_issues:
    print(f"Found {len(all_issues)} issues:")
    for iss in all_issues:
        print("  ❌", iss)
else:
    print("✅ All 83 words passed all audit rules cleanly!")
