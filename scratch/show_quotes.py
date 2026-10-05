import json

with open("scratch/target_24_corpus.json", "r", encoding="utf-8") as f:
    d = json.load(f)

for w in ['benediction', 'tacit', 'tacitly', 'taciturn', 'taciturnity', 'tacitus']:
    print(f"=== {w} ===")
    for q in d[w]['quotes']:
        print(f"  {q['author']} ({q['work']}): {q['sentence'][:100]}...")
