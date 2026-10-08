# -*- coding: utf-8 -*-
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, 'scratch')
from corpus_helper import get_corpus_and_dict_data

words = json.load(open('scratch/quantity_b2_magn_words.json', encoding='utf-8'))
data = get_corpus_and_dict_data(words)

cluster_path = "App database/Latin roots/Cluster Quantity/Dashboard — magn"

existing = {}
for w in words:
    fp = os.path.join(cluster_path, f"{w}.md")
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
        "corpus_quotes": data.get(w, {}).get("quotes", [])
    }

with open("scratch/magn_details.json", "w", encoding="utf-8") as f:
    json.dump(existing, f, ensure_ascii=False, indent=2)

print(f"Extracted details for {len(existing)} words in magn.")
