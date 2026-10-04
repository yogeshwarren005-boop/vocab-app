import json, sys

sys.stdout.reconfigure(encoding="utf-8")

with open('scratch/speed_batch1_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for w, info in data.items():
    print(f"=== {w} ===")
    for d in info.get('defs', [])[:2]:
        print(f"  [{d['source']}] {d['def'][:100]}")
    print(f"  quotes found: {len(info.get('quotes', []))}")
