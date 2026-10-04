import json, sys

sys.stdout.reconfigure(encoding="utf-8")

with open('scratch/speed_batch4_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

words_trem = [
    'entremets', 'extreme', 'extremely', 'extremeness', 'extremism', 
    'extremist', 'extremity', 'extremum', 'trema', 'trematoda', 
    'trematode', 'tremble', 'trembler', 'trembling', 'tremella', 
    'tremellaceae', 'tremellales', 'tremendous', 'tremendously', 
    'tremolite', 'tremolo', 'tremor', 'tremulous', 'tremulously'
]

for w in words_trem:
    info = data.get(w, {})
    print(f"=== {w} ===")
    for d in info.get('defs', [])[:2]:
        print(f"  [{d['source']}] {d['def'][:100]}")
    print(f"  quotes found: {len(info.get('quotes', []))}")
