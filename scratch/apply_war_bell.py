# -*- coding: utf-8 -*-
"""
Applies curate_bell_part1 and curate_bell_part2 to Dashboard — bell in Cluster War.
"""
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

from curate_bell_part1 import data_bell_part1
from curate_bell_part2 import data_bell_part2

all_bell_data = {}
all_bell_data.update(data_bell_part1)
all_bell_data.update(data_bell_part2)

target_dir = r"App database/Latin roots/Cluster War/Dashboard — bell"

updated_count = 0
files = [f for f in os.listdir(target_dir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]
for fname in files:
    word_key = fname[:-3]
    if word_key not in all_bell_data:
        matching = [k for k in all_bell_data if k.lower() == word_key.lower()]
        if matching:
            word_key = matching[0]
        else:
            print(f"Word not found in data: {fname}")
            continue

    entry = all_bell_data[word_key]
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
    print(f"Updated {fname} in Dashboard — bell")

print(f"\nTotal updated: {updated_count}")
