# -*- coding: utf-8 -*-
"""
Merges data_aud, data_son, data_clar into scratch/curate_senses_b2.py
"""
import sys
import re

from scratch.data_aud import data_aud
from scratch.data_son import data_son
from scratch.data_clar import data_clar

data = {}
data.update(data_aud)
data.update(data_son)
data.update(data_clar)

words_aud = ['acaudal', 'acaudate', 'alauda', 'alaudidae', 'audacious', 'audaciously', 'audaciousness', 'audacity', 'audad', 'auden', 'audenesque', 'audibility', 'audible', 'audibleness', 'audibly', 'audience', 'audile', 'audio', 'audio-lingual', 'audiocassette', 'audiogram', 'audiology', 'audiometer', 'audiometric', 'audiometry', 'audiotape', 'audiovisual', 'audit', 'audition', 'auditive', 'auditor', 'auditorium', 'auditory', 'audubon', 'inaudibility', 'inaudible', 'inaudibleness', 'inaudibly']
words_son = ['consonance', 'consonant', 'consonantal', 'consonate', 'dissonance', 'dissonant', 'dissonate', 'nonresonant', 'resonance', 'resonant', 'resonate', 'resonating', 'resonator', 'son', 'sonant', 'sonar', 'sonic', 'sonnet', 'sonneteer', 'sonority', 'sonorous', 'sonorously', 'sonorousness', 'subsonic', 'supersonic', 'ultrasonic', 'unison']
words_clar = ['clarence', 'claret', 'clarification', 'clarify', 'clarifying', 'clarinet', 'clarinetist', 'clarinettist', 'clarion', 'clarity', 'claro', 'clary', 'declarable', 'declaration', 'declarative', 'declaratory', 'declare', 'declared', 'declarer', 'undeclared']

expected = set(words_aud + words_son + words_clar)
print(f"Total words in data: {len(data)}")
assert len(data) == 85, f"Expected 85 words, got {len(data)}"
assert set(data.keys()) == expected, f"Difference: {expected ^ set(data.keys())}"

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

circular_re = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.IGNORECASE)

issues = []
for w in sorted(expected):
    ent = data[w]
    p = ent['primary'].strip()
    s = ent['secondary'].strip()
    quotes = ent['quotes']
    
    if len(p) < 25:
        issues.append(f"{w}: Primary def too short ({len(p)})")
    if circular_re.search(p):
        issues.append(f"{w}: Primary circular boilerplate")
        
    if len(s) < 25:
        issues.append(f"{w}: Secondary def too short ({len(s)})")
    if circular_re.search(s):
        issues.append(f"{w}: Secondary circular boilerplate")
        
    if p.lower() == s.lower():
        issues.append(f"{w}: Duplicate definition")
        
    # Jaccard
    p_tokens = set(re.findall(r'\w+', p.lower()))
    s_tokens = set(re.findall(r'\w+', s.lower()))
    jaccard = len(p_tokens & s_tokens) / max(len(p_tokens | s_tokens), 1)
    if jaccard >= 0.70:
        issues.append(f"{w}: High Jaccard overlap ({jaccard:.2f})")
        
    if len(quotes) != 3:
        issues.append(f"{w}: Expected 3 quotes, found {len(quotes)}")
        
    auths = []
    for q in quotes:
        a = q['author'].strip()
        work = q['work'].strip()
        quote = q['quote'].strip()
        auths.append(a)
        if len(a) < 3:
            issues.append(f"{w}: Short author: {a}")
        if len(work) < 2:
            issues.append(f"{w}: Short work: {work}")
        if '**' not in quote:
            issues.append(f"{w}: Word not bolded: {quote[:40]}")
        line = f"> - 📜 **{a} (*{work}*):** *\"{quote}\"*"
        for b in banned:
            if b in line or b in p or b in s:
                issues.append(f"{w}: Contains banned phrase: {b}")
                
    if len(set(auths)) < len(quotes):
        issues.append(f"{w}: Duplicate authors: {auths}")

if issues:
    print(f"Found {len(issues)} issues:")
    for i in issues:
        print("  -", i)
    sys.exit(1)
else:
    print("ALL 85 ENTRIES ARE 100% VALID!")

# Write scratch/curate_senses_b2.py
import json

out_lines = [
    "# -*- coding: utf-8 -*-",
    '"""',
    "Curated definitions and authentic quotations for Cluster Senses & Perception Batch 2 (85 words):",
    "- Dashboard — aud (38 words)",
    "- Dashboard — son (27 words)",
    "- Dashboard — clar (20 words)",
    '"""',
    "import sys",
    "",
    'sys.stdout.reconfigure(encoding="utf-8")',
    "",
    "data_senses_b2 = {"
]

for idx, w in enumerate(sorted(expected)):
    ent = data[w]
    comma = "," if idx < len(expected) - 1 else ""
    out_lines.append(f"  {json.dumps(w, ensure_ascii=False)}: {{")
    out_lines.append(f"    \"primary\": {json.dumps(ent['primary'], ensure_ascii=False)},")
    out_lines.append(f"    \"secondary\": {json.dumps(ent['secondary'], ensure_ascii=False)},")
    out_lines.append("    \"quotes\": [")
    for q_idx, q in enumerate(ent["quotes"]):
        q_comma = "," if q_idx < len(ent["quotes"]) - 1 else ""
        out_lines.append(f"      {{\"author\": {json.dumps(q['author'], ensure_ascii=False)}, \"work\": {json.dumps(q['work'], ensure_ascii=False)}, \"quote\": {json.dumps(q['quote'], ensure_ascii=False)}}}{q_comma}")
    out_lines.append("    ]")
    out_lines.append(f"  }}{comma}")

out_lines.append("}")
out_lines.append("")

with open("scratch/curate_senses_b2.py", "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))

print("Wrote scratch/curate_senses_b2.py successfully!")
