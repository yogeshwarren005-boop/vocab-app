# -*- coding: utf-8 -*-
"""
Apply curate_arc_rem and curate_general_b1 to Dashboard — arc
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.curate_general_b1 import data_general_b1
from scratch.curate_arc_rem import data_arc_rem

combined_arc = {**data_general_b1, **data_arc_rem}

arc_dir = r"App database/Latin roots/Cluster General/Dashboard — arc"

files = [f for f in os.listdir(arc_dir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]

count = 0
for fname in files:
    word_key = fname[:-3]
    if word_key not in combined_arc:
        matching = [k for k in combined_arc if k.lower() == word_key.lower()]
        if matching:
            word_key = matching[0]
        else:
            print(f"Word key not found in data: {word_key}")
            continue

    entry = combined_arc[word_key]
    file_path = os.path.join(arc_dir, fname)

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

print(f"Successfully applied curation to {count} files in Dashboard — arc.")
