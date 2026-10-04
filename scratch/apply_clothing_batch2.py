# -*- coding: utf-8 -*-
"""
Applies curate_clothing_batch2 to Dashboard — tect (36w) and Dashboard — vest (39w) in Cluster Clothing & Covering.
Total: 75 words.
"""
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

from curate_clothing_batch2 import data_batch2_tect, data_batch2_vest

cluster_dir = r"App database/Latin roots/Cluster Clothing & Covering"

targets = [
    ("Dashboard — tect", data_batch2_tect),
    ("Dashboard — vest", data_batch2_vest)
]

total_updated = 0

for dash_name, data_dict in targets:
    target_dir = os.path.join(cluster_dir, dash_name)
    if not os.path.exists(target_dir):
        print(f"Directory not found: {target_dir}")
        continue

    files = [f for f in os.listdir(target_dir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]
    dash_updated = 0

    for fname in files:
        word_key = fname[:-3]
        if word_key not in data_dict:
            matching = [k for k in data_dict if k.lower() == word_key.lower()]
            if matching:
                word_key = matching[0]
            else:
                print(f"Word key not found in {dash_name}: {fname}")
                continue

        entry = data_dict[word_key]
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

        dash_updated += 1
        total_updated += 1

    print(f"Successfully updated {dash_updated} files in {dash_name}.")

print(f"Total files updated across Clothing Batch 2: {total_updated}")
