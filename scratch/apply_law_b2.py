# -*- coding: utf-8 -*-
"""
Applies curate_law_b2 to:
- Dashboard — judic (23 words)
- Dashboard — juris (7 words)
- Dashboard — just (34 words)
- Dashboard — legat (12 words)
- Dashboard — senat (5 words)
- Dashboard — statut (3 words)
- Dashboard — vindic (11 words)
Total: 95 words.
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.curate_law_b2 import data_law_b2

base_cluster_dir = r"App database/Latin roots/Cluster Law, Justice & Feudal"

dashboards = [
    "Dashboard — judic",
    "Dashboard — juris",
    "Dashboard — just",
    "Dashboard — legat",
    "Dashboard — senat",
    "Dashboard — statut",
    "Dashboard — vindic"
]

total_updated = 0
total_files = 0

for dash in dashboards:
    target_dir = os.path.join(base_cluster_dir, dash)
    if not os.path.exists(target_dir):
        print(f"Directory not found: {target_dir}")
        continue

    files = [f for f in os.listdir(target_dir) if f.endswith('.md') and not f.startswith(('Dashboard', 'Word Triage', 'Cluster', 'Semantic Field'))]
    total_files += len(files)

    count = 0
    for fname in sorted(files):
        word_key = fname[:-3]
        if word_key not in data_law_b2:
            matching = [k for k in data_law_b2 if k.lower() == word_key.lower()]
            if matching:
                word_key = matching[0]
            else:
                print(f"Word key not found in data: {word_key} (in {dash})")
                continue

        entry = data_law_b2[word_key]
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

        count += 1
        total_updated += 1

    print(f"Updated {count}/{len(files)} files in {dash}.")

print(f"\nSuccessfully applied updates to {total_updated}/{total_files} files.")
