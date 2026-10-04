# -*- coding: utf-8 -*-
"""
Applies curate_sleep_batch4_cub to Dashboard — cub.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

from curate_sleep_batch4_cub import data_cub

target_dir = r"App database/Latin roots/Cluster Sleep, Rest & Stillness/Dashboard — cub"

updated_count = 0
for fname in os.listdir(target_dir):
    if not fname.endswith('.md') or fname.startswith('Dashboard') or fname.startswith('Word Triage'):
        continue

    word_key = fname[:-3]
    if word_key not in data_cub:
        matching = [k for k in data_cub if k.lower() == word_key.lower()]
        if matching:
            word_key = matching[0]
        else:
            print(f"Missing from data_cub: {fname}")
            continue

    entry = data_cub[word_key]
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
