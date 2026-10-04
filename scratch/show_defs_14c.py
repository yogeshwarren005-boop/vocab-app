import json, sys

sys.stdout.reconfigure(encoding="utf-8")

with open('scratch/batch14c_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for w, info in data.items():
    print(f"=== {w} ===")
    for d in info.get('defs', []):
        print(f"  [{d['source']}] {d['def']}")
