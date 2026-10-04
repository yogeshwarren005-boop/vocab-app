import json

d = json.load(open('scratch/speed_batch6_raw.json', encoding='utf-8'))
words_6b = [
    'leveling', 'leveller', 'lever', 'leverage', 'leveraging', 'leveret', 'levi', "levi's", 'levi-strauss',
    'leviathan', 'levirate', 'levis', 'levisticum', 'levitate', 'levitation', 'levite', 'levitical',
    'leviticus', 'levitra', 'levity', 'levodopa', 'levorotary', 'levorotation', 'levorotatory', 'levulose',
    'levy', 'relevance', 'relevancy', 'relevant', 'relevantly'
]

for w in words_6b:
    qs = d.get(w, {}).get('quotes', [])
    defs = d.get(w, {}).get('defs', [])
    print(f"{w} (defs={len(defs)}, quotes={len(qs)}):")
    for q in qs[:2]:
        print(f"  - {q['author']} ({q['work']}): {q['sentence'][:80]}...")
