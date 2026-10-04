# -*- coding: utf-8 -*-
"""
Applies curate_war_milit and curate_war_pac to:
1. Dashboard — milit in Cluster War
2. Dashboard — pac in Cluster War
3. (Syncs pact to Dashboard — pact in Cluster Law)
"""
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

from curate_war_milit import data_war_milit
from curate_war_pac import data_war_pac

batch2_data = {}
batch2_data.update(data_war_milit)
batch2_data.update(data_war_pac)

targets = [
    r"App database/Latin roots/Cluster War/Dashboard — milit",
    r"App database/Latin roots/Cluster War/Dashboard — pac",
    r"App database/Latin roots/Cluster Law/Dashboard — pact"
]

updated_count = 0
for target_dir in targets:
    if not os.path.exists(target_dir):
        print(f"Directory not found: {target_dir}")
        continue

    files = [f for f in os.listdir(target_dir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]
    for fname in files:
        word_key = fname[:-3]
        if word_key not in batch2_data:
            matching = [k for k in batch2_data if k.lower() == word_key.lower()]
            if matching:
                word_key = matching[0]
            else:
                continue

        entry = batch2_data[word_key]
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
