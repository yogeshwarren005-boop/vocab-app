# -*- coding: utf-8 -*-
"""
Applies curate_food_b1 to all 8 dashboards in Food Batch 1:
- bib (6 words)
- coct (5 words)
- coqu (6 words)
- ed (34 words)
- lact (29 words)
- mell (15 words)
- pan (9 words)
- pota (6 words)
Total: 110 words.
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.append(".")

from scratch.curate_food_b1 import data_food_b1

target_dirs = [
    r"App database/Latin roots/Cluster Food, Eating & Drink/Dashboard — bib",
    r"App database/Latin roots/Cluster Food, Eating & Drink/Dashboard — coct",
    r"App database/Latin roots/Cluster Food, Eating & Drink/Dashboard — coqu",
    r"App database/Latin roots/Cluster Food, Eating & Drink/Dashboard — ed",
    r"App database/Latin roots/Cluster Food, Eating & Drink/Dashboard — lact",
    r"App database/Latin roots/Cluster Food, Eating & Drink/Dashboard — mell",
    r"App database/Latin roots/Cluster Food, Eating & Drink/Dashboard — pan",
    r"App database/Latin roots/Cluster Food, Eating & Drink/Dashboard — pota"
]

total_updated = 0

for target_dir in target_dirs:
    print(f"\nProcessing directory: {target_dir}")
    files = [f for f in os.listdir(target_dir) if f.endswith('.md') and not f.startswith(('Dashboard', 'Word Triage', 'Cluster', 'Semantic Field'))]
    dir_updated = 0
    
    for fname in sorted(files):
        word_key = fname[:-3]
        if word_key not in data_food_b1:
            matching = [k for k in data_food_b1 if k.lower() == word_key.lower()]
            if matching:
                word_key = matching[0]
            else:
                print(f"  [ERROR] Word key not found in data: {word_key}")
                continue

        entry = data_food_b1[word_key]
        file_path = os.path.join(target_dir, fname)

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        book_pos = content.find("> [!book]")
        if book_pos == -1:
            print(f"  [ERROR] Missing > [!book] in {file_path}")
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

        dir_updated += 1
        print(f"  Updated: {fname}")

    print(f"Directory total: {dir_updated} / {len(files)} files updated.")
    total_updated += dir_updated

print(f"\nFinished! Total updated across all directories: {total_updated} files.")
