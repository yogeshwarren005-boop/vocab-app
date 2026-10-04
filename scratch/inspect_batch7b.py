import json

d = json.load(open('scratch/speed_batch7_raw.json', encoding='utf-8'))
words_7b = [
    'salat', 'sale', 'saleable', 'salem', 'saleratus', 'salerno', 'saleroom', 'sales', 'salesclerk',
    'salesgirl', 'saleslady', 'salesman', 'salesmanship', 'salesperson', 'salesroom', 'saleswoman',
    'salian', 'salicaceae', 'salicales', 'salicornia', 'salicylate', 'salience', 'saliency', 'salient',
    'salientia', 'salientian', 'saliferous', 'salim', 'salina', 'salinate', 'saline', 'salinger',
    'salinity', 'salinometer', 'salisbury', 'salish'
]

for w in words_7b:
    qs = d.get(w, {}).get('quotes', [])
    defs = d.get(w, {}).get('defs', [])
    print(f"{w} (defs={len(defs)}, quotes={len(qs)}):")
    for q in qs[:2]:
        print(f"  - {q['author']} ({q['work']}): {q['sentence'][:80]}...")
