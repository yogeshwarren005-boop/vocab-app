# -*- coding: utf-8 -*-
"""
Applies curate_war_b1a to:
1. Dashboard — flict
2. Dashboard — host
3. Dashboard — pugn
4. Dashboard — victor (and syncs to Dashboard — vic in Law, Justice & Feudal)
"""
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

from curate_war_b1a import data_war_b1a

targets = [
    r"App database/Latin roots/Cluster War/Dashboard — flict",
    r"App database/Latin roots/Cluster War/Dashboard — host",
    r"App database/Latin roots/Cluster War/Dashboard — pugn",
    r"App database/Latin roots/Cluster War/Dashboard — victor",
    r"App database/Latin roots/Cluster Law, Justice & Feudal/Dashboard — vic"
]

updated_count = 0
for target_dir in targets:
    if not os.path.exists(target_dir):
        print(f"Directory not found: {target_dir}")
        continue

    files = [f for f in os.listdir(target_dir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]
    for fname in files:
        word_key = fname[:-3]
        if word_key not in data_war_b1a:
            matching = [k for k in data_war_b1a if k.lower() == word_key.lower()]
            if matching:
                word_key = matching[0]
            else:
                continue

        entry = data_war_b1a[word_key]
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

        updated_count += 1
        print(f"Updated {fname} in {os.path.basename(target_dir)}")

print(f"\nTotal updated: {updated_count}")
