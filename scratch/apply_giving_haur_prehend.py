# -*- coding: utf-8 -*-
"""
Applies curate_giving_batch1_haur_prehend to Dashboard — haur and Dashboard — prehend.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

from curate_giving_batch1_haur_prehend import data_haur_prehend

cluster_dir = r"App database/Latin roots/Cluster Giving & Receiving"
dashboards = [
    "Dashboard — haur",
    "Dashboard — prehend"
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
        if word_key not in data_haur_prehend:
            matching = [k for k in data_haur_prehend if k.lower() == word_key.lower()]
            if matching:
                word_key = matching[0]
            else:
                print(f"Word key not found in data_haur_prehend: {fname} in {d}")
                continue

        entry = data_haur_prehend[word_key]
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

        lines.append("")

        new_content = prefix + "\n".join(lines)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        updated_count += 1

print(f"Successfully updated {updated_count} files across haur and prehend.")
