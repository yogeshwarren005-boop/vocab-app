# -*- coding: utf-8 -*-
"""
Applies curate_sacred_batch4 and curate_sacred_batch5 to Dashboard — san in Cluster Sacred (68 words).
"""
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

from curate_sacred_batch4 import data_sacred_b4
from curate_sacred_batch5 import data_sacred_b5

# Merge both datasets
combined_san = {}
combined_san.update(data_sacred_b4)
combined_san.update(data_sacred_b5)

target_dir = r"App database/Latin roots/Cluster Sacred/Dashboard — san"
if not os.path.exists(target_dir):
    print(f"Directory not found: {target_dir}")
    sys.exit(1)

files = [f for f in os.listdir(target_dir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]
updated_count = 0

for fname in files:
    word_key = fname[:-3]
    if word_key not in combined_san:
        matching = [k for k in combined_san if k.lower() == word_key.lower()]
        if matching:
            word_key = matching[0]
        else:
            print(f"Word key not found in combined_san: {fname}")
            continue

    entry = combined_san[word_key]
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
        quote_text = q['quote'].strip().strip('"').strip('“').strip('”')
        lines.append(f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{quote_text}\"*")

    lines.append("")

    new_content = prefix + "\n".join(lines) + "\n"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    updated_count += 1

print(f"Batch 5 Applied: Successfully updated {updated_count}/{len(files)} notes in Dashboard — san.")
