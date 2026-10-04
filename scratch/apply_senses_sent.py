# -*- coding: utf-8 -*-
"""
Applies curate_senses_sent to:
App database/Latin roots/Cluster Senses & Perception/Dashboard — sent
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.curate_senses_sent import data_senses_sent

target_dir = r"App database/Latin roots/Cluster Senses & Perception/Dashboard — sent"

count = 0
files = [f for f in os.listdir(target_dir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]

for fname in sorted(files):
    word_key = fname[:-3]
    if word_key not in data_senses_sent:
        print(f"Word key not found in data: {word_key}")
        continue

    entry = data_senses_sent[word_key]
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
