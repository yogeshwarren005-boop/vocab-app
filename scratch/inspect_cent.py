# -*- coding: utf-8 -*-
import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, 'scratch')
from corpus_helper import get_corpus_and_dict_data

target_dir = r"App database/Latin roots/Cluster Quantity/Dashboard — cent"
words = sorted([f[:-3] for f in os.listdir(target_dir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')])

print(f"Total words in Dashboard — cent: {len(words)}")

with open("scratch/quantity_b3_cent_words.json", "w", encoding="utf-8") as f:
    json.dump(words, f, indent=2, ensure_ascii=False)

data = get_corpus_and_dict_data(words)

existing = {}
for w in words:
    fp = os.path.join(target_dir, f"{w}.md")
    if not os.path.exists(fp):
        continue
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()
    quote_matches = re.findall(r'> -\s*📜\s*\*\*([^*]+)\s*\(\*([^*]+)\*\):\*\*\s*"(.*?)"', content)
    quotes = []
    for auth, work, sent in quote_matches:
        quotes.append({"author": auth.strip(), "work": work.strip(), "sentence": sent.strip()})
    
    def1_m = re.search(r'1\.\s*\*\*Primary Meaning\*\*:\s*([^\n]+)', content)
    def2_m = re.search(r'2\.\s*\*\*Secondary Meaning\*\*:\s*([^\n]+)', content)
    d1 = def1_m.group(1).strip() if def1_m else ""
    d2 = def2_m.group(1).strip() if def2_m else ""

    existing[w] = {
        "quotes": quotes,
        "d1": d1,
        "d2": d2,
        "corpus_quotes": data.get(w, {}).get("quotes", []),
        "dict_defs": data.get(w, {}).get("definitions", [])
    }

with open("scratch/cent_details.json", "w", encoding="utf-8") as f:
    json.dump(existing, f, ensure_ascii=False, indent=2)

with_quotes = [w for w, v in existing.items() if len(v["quotes"]) >= 3 or len(v["corpus_quotes"]) >= 3]
print(f"Cent details saved. Words with >=3 quotes (existing or corpus): {len(with_quotes)} / {len(words)}")
