# -*- coding: utf-8 -*-
import json
import re

with open("scratch/existing_notes_dump.json", "r", encoding="utf-8") as f:
    all_words = json.load(f)

knownBannedPhrases = [
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

circular_re = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.IGNORECASE)

print(f"{'Word':20} | {'Def OK?':8} | {'Quotes OK?':10} | Issues")
print("-" * 60)

for w, info in all_words.items():
    issues = []
    p = info["primary"]
    s = info["secondary"]
    
    if len(p) < 25:
        issues.append(f"Primary short ({len(p)})")
    if circular_re.search(p):
        issues.append("Primary circular")
    if len(s) < 25:
        issues.append(f"Secondary short ({len(s)})")
    if circular_re.search(s):
        issues.append("Secondary circular")
    if p.lower() == s.lower():
        issues.append("Duplicate def")
        
    pTokens = set(re.findall(r'\w+', p.lower()))
    sTokens = set(re.findall(r'\w+', s.lower()))
    if pTokens and sTokens:
        jaccard = len(pTokens & sTokens) / max(len(pTokens | sTokens), 1)
        if jaccard >= 0.70:
            issues.append(f"Jaccard {jaccard:.2f}")

    # quotes
    qs = info["quotes"]
    if len(qs) != 3:
        issues.append(f"Quotes count {len(qs)}")
    else:
        auths = [q["author"] for q in qs]
        if len(set(auths)) < 3:
            issues.append(f"Duplicate auth ({auths})")
        for q in qs:
            for b in knownBannedPhrases:
                if b in q["author"] or b in q["work"] or b in q["quote_text"]:
                    issues.append(f"Banned: {b}")
            if "**" not in q["quote_text"]:
                issues.append(f"Not bolded in quote by {q['author']}")

    def_ok = "PASS" if not [i for i in issues if "Primary" in i or "Secondary" in i or "Duplicate def" in i or "Jaccard" in i] else "FAIL"
    q_ok = "PASS" if not [i for i in issues if "Quote" in i or "auth" in i or "bolded" in i or "Banned" in i] else "FAIL"
    
    if issues:
        print(f"{w:20} | {def_ok:8} | {q_ok:10} | {', '.join(issues)}")
