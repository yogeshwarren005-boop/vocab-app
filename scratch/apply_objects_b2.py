# -*- coding: utf-8 -*-
"""
Applies curate_objects_b2 to:
- Dashboard — circul (14 words)
- Dashboard — curv (24 words)
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.curate_objects_b2 import data_objects_b2

targets = [
    r"App database/Latin roots/Cluster Objects & Forms/Dashboard — circul",
    r"App database/Latin roots/Cluster Objects & Forms/Dashboard — curv"
]

count = 0
for target_dir in targets:
    if not os.path.exists(target_dir):
        print(f"Directory not found: {target_dir}")
        continue

    files = [f for f in os.listdir(target_dir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]
    for fname in files:
        word_key = fname[:-3]
        if word_key not in data_objects_b2:
            matching = [k for k in data_objects_b2 if k.lower() == word_key.lower()]
            if matching:
                word_key = matching[0]
            else:
                print(f"Word key not found in data: {word_key} (in {target_dir})")
                continue

        entry = data_objects_b2[word_key]
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

        count += 1
        print(f"Updated: {fname}")

print(f"\nTotal files updated: {count}")
