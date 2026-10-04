import json, sys

sys.stdout.reconfigure(encoding="utf-8")

with open('scratch/speed_batch2_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

words_2a = [
    'collapsable', 'collapse', 'collapsible', 'elapse', 'elapsed', 
    'illapse', 'lapse', 'lapsed', 'lapsing', 'noncollapsable', 
    'noncollapsible', 'prelapsarian', 'prolapse', 'prolapsus', 'relapse', 
    'relapsing', 'vibraharp', 'vibramycin', 'vibrancy', 'vibrant', 
    'vibraphone', 'vibraphonist', 'vibrate', 'vibration'
]

for w in words_2a:
    info = data.get(w, {})
    print(f"=== {w} ===")
    for d in info.get('defs', [])[:2]:
        print(f"  [{d['source']}] {d['def'][:100]}")
    print(f"  quotes found: {len(info.get('quotes', []))}")
