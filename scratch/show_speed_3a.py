import json, sys

sys.stdout.reconfigure(encoding="utf-8")

with open('scratch/speed_batch3_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

words_3a = [
    'ambulacral', 'ambulacrum', 'ambulance', 'ambulant', 'ambulate', 
    'ambulation', 'ambulatory', 'ambulette', 'circumambulate', 'perambulate', 
    'perambulating', 'perambulation', 'perambulator', 'somnambulant', 'somnambulate', 
    'somnambulation', 'somnambulism', 'somnambulist', 'emigrant', 'emigrate', 
    'emigration', 'emigre', 'emigree', 'immigrant', 'immigrate', 
    'immigration', 'migraine'
]

for w in words_3a:
    info = data.get(w, {})
    print(f"=== {w} ===")
    for d in info.get('defs', [])[:2]:
        print(f"  [{d['source']}] {d['def'][:100]}")
    print(f"  quotes found: {len(info.get('quotes', []))}")
