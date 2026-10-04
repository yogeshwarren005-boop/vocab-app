import json

d = json.load(open('scratch/speed_batch7_raw.json', encoding='utf-8'))
words_7c = [
    'salishan', 'saliva', 'salivary', 'salivate', 'salivation', 'salix', 'sallet', 'sallow',
    'sallowness', 'sally', 'salmacis', 'salmagundi', 'salmi', 'salmo', 'salmon', 'salmonberry',
    'salmonella', 'salmonellosis', 'salmonid', 'salmonidae', 'salmwood', 'salol', 'salome',
    'salomon', 'salon', 'salonica', 'salonika', 'saloon', 'salsa', 'salsify', 'salsilla',
    'salsola', 'salt', 'salt-cured', 'saltate'
]

for w in words_7c:
    qs = d.get(w, {}).get('quotes', [])
    defs = d.get(w, {}).get('defs', [])
    print(f"{w} (defs={len(defs)}, quotes={len(qs)}):")
    for q in qs[:2]:
        print(f"  - {q['author']} ({q['work']}): {q['sentence'][:80]}...")
