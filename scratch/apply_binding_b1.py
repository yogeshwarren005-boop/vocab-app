# -*- coding: utf-8 -*-
"""
Applies curate_binding_b1 to markdown files across:
- Dashboard — cing (2 words)
- Dashboard — copul (6 words)
- Dashboard — fix (31 words)
- Dashboard — haer (2 words)
- Dashboard — junct (20 words)
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.curate_binding_b1 import data_binding_b1

target_dirs = [
    r"App database/Latin roots/Cluster Binding/Dashboard — cing",
    r"App database/Latin roots/Cluster Binding/Dashboard — copul",
    r"App database/Latin roots/Cluster Binding/Dashboard — fix",
    r"App database/Latin roots/Cluster Binding/Dashboard — haer",
    r"App database/Latin roots/Cluster Binding/Dashboard — junct"
]

count = 0
for target_dir in target_dirs:
    if not os.path.exists(target_dir):
        print(f"Directory not found: {target_dir}")
        continue

    files = [
        f for f in os.listdir(target_dir)
        if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')
    ]

    for fname in files:
        word_key = fname[:-3].lower().strip()
        matching_key = None
        for k in data_binding_b1:
            if k.lower().strip() == word_key:
                matching_key = k
                break

        if not matching_key:
            print(f"Skipping {fname} (not in data_binding_b1)")
            continue

        entry = data_binding_b1[matching_key]
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
        print(f"Updated: {fname} in {os.path.basename(target_dir)}")

print(f"\nTotal files updated: {count}")
