# -*- coding: utf-8 -*-
"""
Applies curate_animal_batch2 to Dashboard — leon, Dashboard — formi, Dashboard — plum, Dashboard — urs.
"""
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

from curate_animal_batch2 import data_animal_b2

cluster_dir = r"App database/Latin roots/Cluster Animal Adjectives & Biological"
dashboards = [
    "Dashboard — leon",
    "Dashboard — formi",
    "Dashboard — plum",
    "Dashboard — urs"
]

updated_count = 0
for d in dashboards:
    target_dir = os.path.join(cluster_dir, d)
    if not os.path.exists(target_dir):
        print(f"Directory not found: {target_dir}")
        continue

    files = [f for f in os.listdir(target_dir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]
    for fname in files:
        word_key = fname[:-3]
        if word_key not in data_animal_b2:
            matching = [k for k in data_animal_b2 if k.lower() == word_key.lower()]
            if matching:
                word_key = matching[0]
            else:
                print(f"Word key not found in data_animal_b2: {fname} in {d}")
                continue

        entry = data_animal_b2[word_key]
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

        new_content = prefix + "\n".join(lines) + "\n"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        updated_count += 1
        print(f"Updated {fname} in {d}")

print(f"\nTotal updated: {updated_count}")
