# -*- coding: utf-8 -*-
"""
Applies curate_light_batch1 to 5 dashboards in Cluster Light:
scintill (5w), splend (10w), stell (10w), fulg (12w), lustr (13w).
Total: 50 words.
"""
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

from curate_light_batch1 import data_batch1

cluster_dir = r"App database/Latin roots/Cluster Light"

dashboards = [
    "Dashboard — scintill",
    "Dashboard — splend",
    "Dashboard — stell",
    "Dashboard — fulg",
    "Dashboard — lustr"
]

total_updated = 0

for d in dashboards:
    target_dir = os.path.join(cluster_dir, d)
    if not os.path.exists(target_dir):
        print(f"Directory not found: {target_dir}")
        continue

    files = [f for f in os.listdir(target_dir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]
    dash_updated = 0

    for fname in files:
        word_key = fname[:-3]
        if word_key not in data_batch1:
            matching = [k for k in data_batch1 if k.lower() == word_key.lower()]
            if matching:
                word_key = matching[0]
            else:
                print(f"Word key not found in {d}: {fname}")
                continue

        entry = data_batch1[word_key]
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

    print(f"Successfully updated {dash_updated} files in {d}.")

print(f"Total files updated across Light Batch 1: {total_updated}")
