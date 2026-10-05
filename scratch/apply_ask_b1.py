# -*- coding: utf-8 -*-
"""
apply_ask_b1.py
Apply curated Batch 1 of Cluster Asking & Seeking (72 words) across 7 dashboards:
- Dashboard — plor (16 words)
- Dashboard — postul (7 words)
- Dashboard — quer (16 words)
- Dashboard — scit (2 words)
- Dashboard — scrut (9 words)
- Dashboard — stud (14 words)
- Dashboard — vestig (8 words)
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("scratch"))

from curate_ask_b1 import data_ask_b1

dashboards = [
    "Dashboard — plor",
    "Dashboard — postul",
    "Dashboard — quer",
    "Dashboard — scit",
    "Dashboard — scrut",
    "Dashboard — stud",
    "Dashboard — vestig",
]

base_dir = r"App database/Latin roots/Cluster Asking & Seeking"

total_updated = 0
missing_words = []

for db in dashboards:
    target_dir = os.path.join(base_dir, db)
    if not os.path.exists(target_dir):
        print(f"Directory not found: {target_dir}")
        continue

    files = [
        f
        for f in os.listdir(target_dir)
        if f.endswith(".md")
        and not f.startswith("Dashboard")
        and not f.startswith("Word Triage")
        and not f.startswith("Cluster")
        and not f.startswith("Semantic")
    ]
    db_updated = 0

    for fname in sorted(files):
        word_key = fname[:-3]
        if word_key not in data_ask_b1:
            missing_words.append((db, word_key))
            continue

        entry = data_ask_b1[word_key]
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
            "> [!quote] 💬 Contextual Usage & Authentic Quotations",
        ]

        for q in entry["quotes"]:
            lines.append(
                f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{q['quote']}\"*"
            )

        new_content = prefix + "\n".join(lines) + "\n"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        db_updated += 1
        total_updated += 1

    print(f"Updated {db_updated}/{len(files)} files in {db}")

print(f"\nTotal updated across all 7 dashboards: {total_updated}")
if missing_words:
    print(f"Missing words ({len(missing_words)}): {missing_words}")
else:
    print("All 72 words across all 7 dashboards successfully matched and updated!")
