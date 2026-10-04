import json, sys

sys.stdout.reconfigure(encoding="utf-8")

with open('scratch/speed_batch3_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

words_3b = [
    'migrant', 'migrate', 'migration', 'migrational', 'migrator', 
    'migratory', 'nonmigratory', 'transmigrante', 'transmigrate', 'transmigration',
    'concuss', 'concussion', 'cuss', 'cussed', 'cussedly', 
    'cussedness', 'decussate', 'decussation', 'discuss', 'discussant', 
    'discussion', 'percuss', 'percussion', 'percussionist', 'percussive', 
    'percussor'
]

for w in words_3b:
    info = data.get(w, {})
    print(f"=== {w} ===")
    for d in info.get('defs', [])[:2]:
        print(f"  [{d['source']}] {d['def'][:100]}")
    print(f"  quotes found: {len(info.get('quotes', []))}")
