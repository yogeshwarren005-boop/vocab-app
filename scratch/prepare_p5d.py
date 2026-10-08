# -*- coding: utf-8 -*-
import json
import os
import re

with open('scratch/p5d_corpus_data.json', 'r', encoding='utf-8') as f:
    corpus_data = json.load(f)

dirpath = 'App database/Latin roots/Cluster Number & Measure/Dashboard — dec'
words = json.load(open('scratch/number_b5_words.json', encoding='utf-8'))[186:]

def extract_existing_md(word):
    fp = os.path.join(dirpath, f"{word}.md")
    if not os.path.exists(fp):
        return None
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    # extract quotes
    quote_matches = re.findall(r'> -\s*📜\s*\*\*([^*]+)\s*\(\*([^*]+)\*\):\*\*\s*"(.*?)"', content)
    quotes = []
    for auth, work, sent in quote_matches:
        auth = auth.strip()
        work = work.strip()
        sent = sent.strip()
        if "Academic Lexicon" not in auth and "Lexicon" not in auth:
            quotes.append({"author": auth, "work": work, "sentence": sent})

    # extract definitions
    def1_m = re.search(r'1\.\s*\*\*Primary Meaning\*\*:\s*([^\n]+)', content)
    def2_m = re.search(r'2\.\s*\*\*Secondary Meaning\*\*:\s*([^\n]+)', content)
    d1 = def1_m.group(1).strip() if def1_m else ""
    d2 = def2_m.group(1).strip() if def2_m else ""

    return {
        "quotes": quotes,
        "d1": d1,
        "d2": d2
    }

summary = {}
for w in words:
    cd = corpus_data.get(w, {})
    c_quotes = cd.get("quotes", [])
    c_defs = cd.get("definitions", [])
    md_info = extract_existing_md(w) or {}
    md_quotes = md_info.get("quotes", [])
    summary[w] = {
        "c_quotes_count": len(c_quotes),
        "md_quotes_count": len(md_quotes),
        "c_defs": c_defs[:2],
        "md_d1": md_info.get("d1", ""),
        "md_d2": md_info.get("d2", ""),
        "corpus_authors": [q["author"] for q in c_quotes[:5]],
        "md_authors": [q["author"] for q in md_quotes]
    }

with open('scratch/p5d_summary.json', 'w', encoding='utf-8') as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)

print("Saved scratch/p5d_summary.json")
