# -*- coding: utf-8 -*-
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

cluster_path = "App database/Latin roots/Cluster Quantity"
words = json.load(open('scratch/quantity_b1a_words.json', encoding='utf-8'))[:48]

def find_file(word):
    for root, dirs, files in os.walk(cluster_path):
        if f"{word}.md" in files:
            return os.path.join(root, f"{word}.md")
    return None

details = {}
for w in words:
    fp = find_file(w)
    if not fp:
        details[w] = {"found": False}
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

    details[w] = {
        "found": True,
        "path": fp,
        "quotes": quotes,
        "d1": d1,
        "d2": d2
    }

with open("scratch/part1aa_existing.json", "w", encoding="utf-8") as f:
    json.dump(details, f, ensure_ascii=False, indent=2)

print(f"Extracted details for {len(details)} words in Part 1Aa.")
