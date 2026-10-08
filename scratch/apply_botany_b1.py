# -*- coding: utf-8 -*-
"""
apply_botany_b1.py
Applies curate_botany_b1 to the 12 dashboards (109 words) in Cluster Botany, Minerals & Elements:
- Dashboard — herbi (2 words)
- Dashboard — spuma (2 words)
- Dashboard — horti (4 words)
- Dashboard — stann (5 words)
- Dashboard — pulver (8 words)
- Dashboard — natr (9 words)
- Dashboard — silic (9 words)
- Dashboard — argent (10 words)
- Dashboard — radic (13 words)
- Dashboard — vitr (13 words)
- Dashboard — xyl (14 words)
- Dashboard — arbor (20 words)
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.append(".")

from scratch.curate_botany_b1 import data_botany_b1

dashboards = [
    "Dashboard — herbi",
    "Dashboard — spuma",
    "Dashboard — horti",
    "Dashboard — stann",
    "Dashboard — pulver",
    "Dashboard — natr",
    "Dashboard — silic",
    "Dashboard — argent",
    "Dashboard — radic",
    "Dashboard — vitr",
    "Dashboard — xyl",
    "Dashboard — arbor"
]

base_dir = r"App database/Latin roots/Cluster Botany, Minerals & Elements"
total_updated = 0

for d in dashboards:
    target_dir = os.path.join(base_dir, d)
    print(f"\nProcessing directory: {target_dir}")
    files = [f for f in os.listdir(target_dir) if f.endswith('.md') and not f.startswith(('Dashboard', 'Word Triage', 'Cluster', 'Semantic Field'))]
    dir_updated = 0

    for fname in sorted(files):
        word_key = fname[:-3]
        if word_key not in data_botany_b1:
            matching = [k for k in data_botany_b1 if k.lower() == word_key.lower()]
            if matching:
                word_key = matching[0]
            else:
                print(f"  [ERROR] Word key not found in data: {word_key}")
                continue

        entry = data_botany_b1[word_key]
        file_path = os.path.join(target_dir, fname)

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        book_pos = content.find("> [!book]")
        if book_pos == -1:
            print(f"  [ERROR] Missing > [!book] in {file_path}")
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

        dir_updated += 1
        print(f"  Updated: {fname}")

    print(f"Directory {d}: {dir_updated} / {len(files)} files updated.")
    total_updated += dir_updated

print(f"\nTotal updated across Batch 1: {total_updated} files.")
