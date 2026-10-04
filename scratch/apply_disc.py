# -*- coding: utf-8 -*-
"""
Applies curated definitions and quotes to all 154 files in Dashboard — disc.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

from curate_mind_batch9_disc_part1 import data_part1
from curate_mind_batch9_disc_part2 import data_part2
from curate_mind_batch9_disc_part3 import data_part3

all_data = {}
all_data.update(data_part1)
all_data.update(data_part2)
all_data.update(data_part3)

print(f"Total words loaded for Dashboard — disc: {len(all_data)}")

target_dir = r"App database/Latin roots/Cluster Mind & Knowledge/Dashboard — disc"

updated_count = 0
missing_words = []

for word_key, entry in all_data.items():
    file_path = os.path.join(target_dir, f"{word_key}.md")
    if not os.path.exists(file_path):
        candidates = [f for f in os.listdir(target_dir) if f.lower() == f"{word_key.lower()}.md"]
        if candidates:
            file_path = os.path.join(target_dir, candidates[0])
        else:
            missing_words.append(word_key)
            print(f"File not found: {word_key}.md")
            continue

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
if missing_words:
    print(f"Missing words ({len(missing_words)}): {missing_words}")
