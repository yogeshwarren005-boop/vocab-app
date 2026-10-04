# -*- coding: utf-8 -*-
"""
Applies curate_giving_batch3_em to Dashboard — em.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

from curate_giving_batch3_em import data_em

target_dir = r"App database/Latin roots/Cluster Giving & Receiving/Dashboard — em"

updated_count = 0
for fname in os.listdir(target_dir):
    if not fname.endswith('.md') or fname.startswith('Dashboard') or fname.startswith('Word Triage'):
        continue

    word_key = fname[:-3]
    if word_key not in data_em:
        matching = [k for k in data_em if k.lower() == word_key.lower()]
        if matching:
            word_key = matching[0]
        else:
            print(f"Missing from data_em: {fname}")
            continue

    entry = data_em[word_key]
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
