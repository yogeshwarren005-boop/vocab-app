import json, sys

sys.stdout.reconfigure(encoding="utf-8")

with open('scratch/speed_batch3_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

words_3c = [
    'repercuss', 'repercussion', 'succuss', 'succussion',
    'circumvolve', 'convolve', 'convolvulaceae', 'convolvulus', 'devolve', 
    'devolvement', 'disinvolve', 'evolve', 'involve', 'involved', 
    'involvement', 'revolve', 'revolved', 'revolver', 'uninvolved', 
    'volva', 'volvaria', 'volvariaceae', 'volvariella', 'volvocaceae', 
    'volvocales', 'volvox', 'volvulus'
]

for w in words_3c:
    info = data.get(w, {})
    print(f"=== {w} ===")
    for d in info.get('defs', [])[:2]:
        print(f"  [{d['source']}] {d['def'][:100]}")
    print(f"  quotes found: {len(info.get('quotes', []))}")
