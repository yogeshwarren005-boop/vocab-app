# -*- coding: utf-8 -*-
"""
Apply curated definitions and citations to Cluster War: Dashboard — arm (74 words)
Using clean format:
> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: ...
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ...

> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **Author (*Work*):** *"Quote with **word** bolded"*
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.curate_arm_part1 import data_arm_part1
from scratch.curate_arm_part2 import data_arm_part2

curated_data = {**data_arm_part1, **data_arm_part2}

arm_dir = r"App database/Latin roots/Cluster War/Dashboard — arm"

files = [f for f in os.listdir(arm_dir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]

count = 0
for fname in files:
    word_key = fname[:-3]
    if word_key not in curated_data:
        matching = [k for k in curated_data if k.lower() == word_key.lower()]
        if matching:
            word_key = matching[0]
        else:
            print(f"Word key not found: {word_key}")
            continue

    entry = curated_data[word_key]
    file_path = os.path.join(arm_dir, fname)

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

print(f"Successfully applied clean curation to {count} files in Dashboard — arm.")
