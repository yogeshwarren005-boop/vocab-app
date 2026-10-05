# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding="utf-8")
sys.path.append(".")

from scratch.curate_speech_b3 import data_speech_b3

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

expected_dict = ['addict', 'addicted', 'addiction', 'addictive', 'benediction', 'benedictive', 'contradict', 'contradiction', 'contradictorily', 'contradictoriness', 'contradictory', 'dictamnus', 'dictaphone', 'dictate', 'dictated', 'dictation', 'dictator', 'dictatorial', 'dictatorially', 'dictatorship', 'diction', 'dictionary', 'dictostylium', 'dictum', 'dictyophera', 'dictyoptera', 'dictyopteran', 'dictyosome', 'edict', 'indict', 'indictability', 'indictable', 'indiction', 'indictment', 'interdict', 'interdiction', 'nonaddictive', 'predict', 'predictability', 'predictable', 'predictably', 'prediction', 'predictive', 'predictor', 'unaddicted', 'unpredictability', 'unpredictable', 'unpredictably', 'unpredicted', 'unpredictive']
expected_tac = ['altace', 'antacid', 'astacidae', 'astacura', 'astacus', 'attacapa', 'attacapan', 'contact', 'cotacachi', 'intact', 'intactness', 'protactinium', 'setaceous', 'tacamahac', 'tacca', 'taccaceae', 'tacit', 'tacitly', 'taciturn', 'taciturnity', 'taciturnly', 'tacitus', 'taco', 'tacoma', 'taconite', 'tact', 'tactful', 'tactfully', 'tactfulness', 'tactic', 'tactical', 'tactically', 'tactician', 'tactics', 'tactile', 'tactility', 'tactless', 'tactlessly', 'tactlessness', 'tactual', 'tactually', 'untactful']

expected_all = expected_dict + expected_tac

print(f"Total entries in curate_speech_b3: {len(data_speech_b3)}")

issues = 0

for w in expected_all:
    if w not in data_speech_b3:
        print(f"Missing expected word: {w}")
        issues += 1

for word, data in data_speech_b3.items():
    p = data.get("primary", "").strip()
    s = data.get("secondary", "").strip()
    qs = data.get("quotes", [])
    
    if len(p) < 25:
        print(f"[{word}] Primary too short: {len(p)}")
        issues += 1
    if circular_re.search(p):
        print(f"[{word}] Primary circular boilerplate: {p}")
        issues += 1
        
    if len(s) < 25:
        print(f"[{word}] Secondary too short: {len(s)}")
        issues += 1
    if circular_re.search(s):
        print(f"[{word}] Secondary circular boilerplate: {s}")
        issues += 1
        
    if p.lower() == s.lower():
        print(f"[{word}] Duplicate definitions")
        issues += 1
        
    # Token Jaccard check
    pTokens = set(re.findall(r'\w+', p.lower()))
    sTokens = set(re.findall(r'\w+', s.lower()))
    intersect = pTokens & sTokens
    union = pTokens | sTokens
    jaccard = len(intersect) / max(len(union), 1)
    if jaccard >= 0.70:
        print(f"[{word}] Definitions excessively similar (Jaccard: {jaccard:.2f})")
        issues += 1
        
    for phrase in banned:
        if phrase in p or phrase in s:
            print(f"[{word}] Contains banned phrase in defs: {phrase}")
            issues += 1

    if len(qs) != 3:
        print(f"[{word}] Expected 3 quotes, found {len(qs)}")
        issues += 1
        
    authors = []
    for q in qs:
        author = q.get("author", "").strip()
        work = q.get("work", "").strip()
        quote = q.get("quote", "").strip()
        
        authors.append(author)
        if len(author) < 3 or len(work) < 2:
            print(f"[{word}] Suspicious author/work: {author} / {work}")
            issues += 1
            
        for phrase in banned:
            if phrase in quote or phrase in author or phrase in work:
                print(f"[{word}] Contains banned phrase in quote: {phrase}")
                issues += 1
                
        if "**" not in quote:
            print(f"[{word}] Word not bolded in quote: {quote}")
            issues += 1
            
    if len(set(authors)) < len(qs):
        print(f"[{word}] Duplicate author: {authors}")
        issues += 1

print(f"Validation completed with {issues} issues.")
if issues == 0:
    print("ALL 92 WORDS ARE 100% PRISTINE!")
