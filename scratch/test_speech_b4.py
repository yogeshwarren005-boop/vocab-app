# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding="utf-8")
sys.path.append(".")

from scratch.curate_speech_b4 import data_speech_b4

expected_dirs = [
    r"App database/Latin roots/Cluster Speech/Dashboard — lingu",
    r"App database/Latin roots/Cluster Speech/Dashboard — loqu",
    r"App database/Latin roots/Cluster Speech/Dashboard — nom",
    r"App database/Latin roots/Cluster Speech/Dashboard — nomin"
]

import os

files_by_dir = {}
all_words = set()
for d in expected_dirs:
    flist = [f[:-3] for f in os.listdir(d) if f.endswith('.md') and not f.startswith(('Dashboard', 'Word Triage', 'Cluster', 'Semantic Field'))]
    files_by_dir[d] = flist
    all_words.update(flist)

print(f"Total files across 4 dashboards: {sum(len(v) for v in files_by_dir.values())}")
print(f"Total unique words across 4 dashboards: {len(all_words)}")
print(f"Total words in data_speech_b4: {len(data_speech_b4)}")

missing = all_words - set(data_speech_b4.keys())
if missing:
    print(f"MISSING WORDS: {missing}")

extra = set(data_speech_b4.keys()) - all_words
if extra:
    print(f"EXTRA WORDS: {extra}")

# Now validate each entry in data_speech_b4
issues = []
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

for w, entry in data_speech_b4.items():
    p = entry.get('primary', '')
    s = entry.get('secondary', '')
    q = entry.get('quotes', [])

    if len(p) < 25:
        issues.append(f"{w}: primary < 25 chars ({len(p)})")
    if len(s) < 25:
        issues.append(f"{w}: secondary < 25 chars ({len(s)})")

    if re.search(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', p, re.I):
        issues.append(f"{w}: primary has boilerplate quality/state of being")
    if re.search(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', s, re.I):
        issues.append(f"{w}: secondary has boilerplate quality/state of being")

    # Jaccard overlap
    pTokens = set(re.findall(r'\w+', p.lower()))
    sTokens = set(re.findall(r'\w+', s.lower()))
    intersect = pTokens & sTokens
    union = pTokens | sTokens
    jaccard = len(intersect) / max(len(union), 1)
    if jaccard >= 0.70:
        issues.append(f"{w}: primary & secondary jaccard >= 0.70 ({jaccard:.2f})")

    # Quotes
    if len(q) != 3:
        issues.append(f"{w}: quotes count != 3 ({len(q)})")

    authors = []
    for idx, quote in enumerate(q):
        auth = quote.get('author', '').strip()
        work = quote.get('work', '').strip()
        txt = quote.get('quote', '').strip()

        authors.append(auth)
        if len(auth) < 3:
            issues.append(f"{w} q{idx+1}: author too short ({auth})")
        if len(work) < 2:
            issues.append(f"{w} q{idx+1}: work too short ({work})")
        if '**' not in txt:
            issues.append(f"{w} q{idx+1}: quote missing bold '**' target word")
        
        # Check banned phrases
        for b in banned:
            if b.lower() in txt.lower():
                issues.append(f"{w} q{idx+1}: quote has banned phrase {b}")

    if len(set(authors)) != len(authors):
        issues.append(f"{w}: duplicate author in quotes: {authors}")

if issues:
    print(f"\nFound {len(issues)} issues:")
    for i in issues:
        print("  -", i)
else:
    print("\nALL 84 ENTRIES FULLY VALIDATED! ZERO ISSUES!")
