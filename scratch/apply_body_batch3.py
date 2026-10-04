# -*- coding: utf-8 -*-
"""
Applies curate_body_batch3_later and curate_body_batch3_digit to Dashboard — later and Dashboard — digit.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

from curate_body_batch3_later import data_later
from curate_body_batch3_digit import data_digit

all_data = {}
all_data.update(data_later)
all_data.update(data_digit)

cluster_dir = r"App database/Latin roots/Cluster Body & State"
dashboards = [
    ("Dashboard — later", data_later),
    ("Dashboard — digit", data_digit)
]

updated_count = 0
for d_name, d_dict in dashboards:
    target_dir = os.path.join(cluster_dir, d_name)
    if not os.path.exists(target_dir):
        print(f"Directory not found: {target_dir}")
        continue

    files = [f for f in os.listdir(target_dir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]
    for fname in files:
        word_key = fname[:-3]
        if word_key not in d_dict:
            matching = [k for k in d_dict if k.lower() == word_key.lower()]
            if matching:
                word_key = matching[0]
            else:
                print(f"Word key not found in dictionary: {fname} in {d_name}")
                continue

        entry = d_dict[word_key]
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

print(f"Successfully updated {updated_count} files across later and digit.")
