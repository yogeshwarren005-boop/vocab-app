import json

d = json.load(open('scratch/speed_batch8_raw.json', encoding='utf-8'))
words_8b = [
    'curiosity', 'curious', 'curiously', 'curiousness', 'curitiba', 'curium', 'curl', 'curled',
    'curler', 'curlew', 'curlicue', 'curliness', 'curling', 'curly-coated', 'curly-grained',
    'curly-haired', 'curly-heads', 'curly-leafed', 'curly-leaved', 'curly', 'curmudgeon',
    'curmudgeonly', 'curt', 'curtail', 'curtailment', 'curtain', 'curtained', 'curtainless',
    'curtal', 'curtilage', 'curtis', 'curtisia', 'curtiss', 'curtly', 'curtness', 'curtsey',
    'curtsy', 'inaccuracy'
]

for w in words_8b:
    qs = d.get(w, {}).get('quotes', [])
    defs = d.get(w, {}).get('defs', [])
    print(f"{w} (defs={len(defs)}, quotes={len(qs)}):")
    for q in qs[:2]:
        print(f"  - {q['author']} ({q['work']}): {q['sentence'][:80]}...")
