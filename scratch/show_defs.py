import json

with open("scratch/target_24_corpus.json", "r", encoding="utf-8") as f:
    d = json.load(f)

for w in ['altace', 'antacid', 'astacidae', 'astacura', 'astacus', 'attacapa', 'attacapan', 'cotacachi', 'setaceous', 'tacamahac', 'tacca', 'taccaceae', 'taciturnly', 'taco', 'tacoma', 'taconite', 'benedictive', 'unpredicted']:
    print(f"=== {w} ===")
    for src, df in d[w]['defs']:
        print(f"  [{src}] {df}")
