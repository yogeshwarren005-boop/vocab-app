import json

d = json.load(open('scratch/speed_batch6_raw.json', encoding='utf-8'))
words_6a = [
    'alleviant', 'alleviate', 'alleviated', 'alleviation', 'alleviative', 'alleviator', 'alleviatory',
    'elevate', 'elevated', 'elevation', 'elevator', 'eleven', 'eleven-plus', 'eleven-sided', 'eleventh',
    'irrelevance', 'irrelevancy', 'irrelevant', 'irrelevantly', 'lev', 'levallorphan', 'levant', 'levanter',
    'levantine', 'levator', 'levee', 'level', 'level-headed', 'leveler', 'levelheaded'
]

for w in words_6a:
    qs = d.get(w, {}).get('quotes', [])
    defs = d.get(w, {}).get('defs', [])
    print(f"{w} (defs={len(defs)}, quotes={len(qs)}):")
    for q in qs[:2]:
        print(f"  - {q['author']} ({q['work']}): {q['sentence'][:80]}...")
