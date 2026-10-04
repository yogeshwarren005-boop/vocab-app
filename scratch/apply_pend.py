# -*- coding: utf-8 -*-
"""
Apply curation to Dashboard — pend (63 words)
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.curate_pend_p1 import data_pend_p1
from scratch.curate_pend_p2 import data_pend_p2

curated_pend = {**data_pend_p1, **data_pend_p2}

pend_dir = r"App database/Latin roots/Cluster Weight/Dashboard — pend"

files = [f for f in os.listdir(pend_dir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]

count = 0
for fname in files:
    word_key = fname[:-3]
    if word_key not in curated_pend:
        matching = [k for k in curated_pend if k.lower() == word_key.lower()]
        if matching:
            word_key = matching[0]
        else:
            print(f"Word key not found in data: {word_key}")
            continue

    entry = curated_pend[word_key]
    file_path = os.path.join(pend_dir, fname)

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    book_pos = content.find("> [!book]")
    if book_pos == -1:
        print(f"Missing > [!book] in {file_path}")
        continue

    prefix = content[:book_pos]

    lines = [
        "> [!book] 📖 Definitions & Semantic Range",
        f"> 1. **Primary Definition (Lexical / Standard Consensus)**: {entry['primary']}",
        f"> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {entry['secondary']}",
        "",
        "> [!quote] 💬 Contextual Usage & Authentic Quotations"
    ]

    for q in entry["quotes"]:
        lines.append(f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{q['quote']}\"*")

    new_content = prefix + "\n".join(lines) + "\n"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    count += 1

print(f"Successfully applied curation to {count} files in Dashboard — pend.")
