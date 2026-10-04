import json

d = json.load(open('scratch/speed_batch7_raw.json', encoding='utf-8'))
words_7d = [
    'saltation', 'saltbox', 'saltbush', 'saltcellar', 'salted', 'salter', 'saltine', 'saltiness',
    'salting', 'saltire', 'saltish', 'saltlike', 'saltpan', 'saltpeter', 'saltpetre', 'saltshaker',
    'saltwater', 'saltworks', 'saltwort', 'salty', 'salubrious', 'salubriousness', 'salubrity',
    'saluki', 'salutary', 'salutation', 'salutatorian', 'salutatory', 'salute', 'saluter', 'salyut',
    'unsalable', 'unsalaried', 'unsaleable', 'unsalted'
]

for w in words_7d:
    qs = d.get(w, {}).get('quotes', [])
    defs = d.get(w, {}).get('defs', [])
    print(f"{w} (defs={len(defs)}, quotes={len(qs)}):")
    for q in qs[:2]:
        print(f"  - {q['author']} ({q['work']}): {q['sentence'][:80]}...")
