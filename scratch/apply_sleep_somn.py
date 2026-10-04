# -*- coding: utf-8 -*-
"""
Applies curate_sleep_batch2_somn to Dashboard — somn.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

from curate_sleep_batch2_somn import data_somn

target_dir = r"App database/Latin roots/Cluster Sleep, Rest & Stillness/Dashboard — somn"

updated_count = 0
for fname in os.listdir(target_dir):
    if not fname.endswith('.md') or fname.startswith('Dashboard') or fname.startswith('Word Triage'):
        continue

    word_key = fname[:-3]
    if word_key not in data_somn:
        matching = [k for k in data_somn if k.lower() == word_key.lower()]
        if matching:
            word_key = matching[0]
        else:
            print(f"Missing from data_somn: {fname}")
            continue

    entry = data_somn[word_key]
    file_path = os.path.join(target_dir, fname)

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

    lines.append("")

    new_content = prefix + "\n".join(lines)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    updated_count += 1

print(f"Successfully updated {updated_count} files in {target_dir}")
