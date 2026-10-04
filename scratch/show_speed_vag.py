import json, sys

sys.stdout.reconfigure(encoding="utf-8")

with open('scratch/speed_batch4_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

words_vag = [
    'divagate', 'divagation', 'extravagance', 'extravagancy', 'extravagant', 
    'extravagantly', 'extravaganza', 'invaginate', 'invagination', 'vagabond', 
    'vagabondage', 'vagal', 'vagary', 'vagile', 'vagina', 
    'vaginal', 'vaginismus', 'vaginitis', 'vaginocele', 'vagrancy', 
    'vagrant', 'vague', 'vaguely', 'vagueness', 'vagus'
]

for w in words_vag:
    info = data.get(w, {})
    print(f"=== {w} ===")
    for d in info.get('defs', [])[:2]:
        print(f"  [{d['source']}] {d['def'][:100]}")
    print(f"  quotes found: {len(info.get('quotes', []))}")
