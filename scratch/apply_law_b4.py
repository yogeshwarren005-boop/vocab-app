# -*- coding: utf-8 -*-
"""
Applies curate_law_b4 data to:
- Dashboard — merces (20 words)
- Dashboard — sanc (19 words)
- Dashboard — vic (63 words)
Total: 102 words.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from curate_law_b4 import data_law_b4

cluster_dir = r"App database/Latin roots/Cluster Law, Justice & Feudal"
dashboards = [
    "Dashboard — merces",
    "Dashboard — sanc",
    "Dashboard — vic"
]

updated_count = 0
for d in dashboards:
    target_dir = os.path.join(cluster_dir, d)
    if not os.path.exists(target_dir):
        print(f"Directory not found: {target_dir}")
        continue

    files = [f for f in os.listdir(target_dir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]
    print(f"Processing {len(files)} files in {d}...")

    for fname in sorted(files):
        word_key = fname[:-3]
        if word_key not in data_law_b4:
            matching = [k for k in data_law_b4 if k.lower() == word_key.lower()]
            if matching:
                word_key = matching[0]
            else:
                print(f"❌ Word key not found in data_law_b4: {fname} in {d}")
                continue

        entry = data_law_b4[word_key]
        file_path = os.path.join(target_dir, fname)

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        book_pos = content.find("> [!book]")
        if book_pos == -1:
            print(f"❌ Missing > [!book] in {file_path}")
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

print(f"\nSuccessfully applied updates to {updated_count} word notes across merces, sanc, and vic.")
