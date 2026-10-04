# -*- coding: utf-8 -*-
"""
Applies curate_sacred_batch4 to Dashboard — sanct in Cluster Sacred (20 words).
"""
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

from curate_sacred_batch4 import data_sacred_b4

cluster_dir = r"App database/Latin roots/Cluster Sacred"
dashboards = [
    "Dashboard — sanct"
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
        if word_key not in data_sacred_b4:
            matching = [k for k in data_sacred_b4 if k.lower() == word_key.lower()]
            if matching:
                word_key = matching[0]
            else:
                print(f"Word key not found in data_sacred_b4: {fname} in {d}")
                continue

        entry = data_sacred_b4[word_key]
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

print(f"Batch 4 Applied: Successfully updated {updated_count}/{len(data_sacred_b4)} notes across sanct.")
