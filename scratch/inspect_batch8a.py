import json

d = json.load(open('scratch/speed_batch8_raw.json', encoding='utf-8'))
words_8a = [
    'accuracy', 'accurate', 'accurately', 'co-occurrence', 'concur', 'cooccur', 'cur', 'curability',
    'curable', 'curableness', 'curacao', 'curacoa', 'curacy', 'curandera', 'curandero', 'curare',
    'curassow', 'curate', 'curative', 'curator', 'curatorial', 'curatorship', 'curaçao', 'curculionidae',
    'curcuma', 'cure-all', 'cure', 'cured', 'curet', 'curettage', 'curette', 'curettement',
    'curia', 'curie', 'curietherapy', 'curing', 'curio', 'curiosa'
]

for w in words_8a:
    qs = d.get(w, {}).get('quotes', [])
    defs = d.get(w, {}).get('defs', [])
    print(f"{w} (defs={len(defs)}, quotes={len(qs)}):")
    for q in qs[:2]:
        print(f"  - {q['author']} ({q['work']}): {q['sentence'][:80]}...")
