import json, sys

sys.stdout.reconfigure(encoding="utf-8")

with open('scratch/speed_batch2_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

words_2b = [
    'vibrational', 'vibrato', 'vibrator', 'vibratory', 'vibrio', 
    'vibrion', 'vibrionic', 'vibrissa', 'nonvolatile', 'nonvolatilisable', 
    'nonvolatilizable', 'volaille', 'volans', 'volant', 'volar', 
    'volary', 'volatile', 'volatilisable', 'volatilise', 'volatilised', 
    'volatility', 'volatilizable', 'volatilize', 'volatilized'
]

for w in words_2b:
    info = data.get(w, {})
    print(f"=== {w} ===")
    for d in info.get('defs', [])[:2]:
        print(f"  [{d['source']}] {d['def'][:100]}")
    print(f"  quotes found: {len(info.get('quotes', []))}")
