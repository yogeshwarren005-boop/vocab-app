import json, sys

sys.stdout.reconfigure(encoding="utf-8")

with open('scratch/speed_batch4_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

words_vi = [
    'devi', 'deviance', 'deviant', 'deviate', 'deviation', 
    'devious', 'deviously', 'deviousness', 'obviate', 'obviating', 
    'obviation', 'obvious', 'obviously', 'obviousness', 'previous', 
    'previously', 'trivia', 'trivial', 'trivialise', 'triviality', 
    'trivialize', 'trivially', 'unobvious', 'vi', 'via'
]

for w in words_vi:
    info = data.get(w, {})
    print(f"=== {w} ===")
    for d in info.get('defs', [])[:2]:
        print(f"  [{d['source']}] {d['def'][:100]}")
    print(f"  quotes found: {len(info.get('quotes', []))}")
