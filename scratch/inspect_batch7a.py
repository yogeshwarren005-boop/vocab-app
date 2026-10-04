import json

d = json.load(open('scratch/speed_batch7_raw.json', encoding='utf-8'))
words_7a = [
    'desalinate', 'desalination', 'desalinisation', 'desalinise', 'desalinization', 'desalinize', 'desalt',
    'disallow', 'insalubrious', 'insalubriousness', 'insalubrity', 'resale', 'salaah', 'salaam', 'salaat',
    'salability', 'salable', 'salableness', 'salacious', 'salaciously', 'salaciousness', 'salacity', 'salad',
    'salade', 'saladin', 'salafism', 'salah', 'salai', 'salal', 'salamander', 'salamandra', 'salamandridae',
    'salamandriform', 'salami', 'salaried', 'salary'
]

for w in words_7a:
    qs = d.get(w, {}).get('quotes', [])
    defs = d.get(w, {}).get('defs', [])
    print(f"{w} (defs={len(defs)}, quotes={len(qs)}):")
    for q in qs[:2]:
        print(f"  - {q['author']} ({q['work']}): {q['sentence'][:80]}...")
