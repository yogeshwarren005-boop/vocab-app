# -*- coding: utf-8 -*-
"""
apply_botany_b4.py
Applies curate_botany_b4 (Part 1 + Part 2) to Dashboard — rad (102 words) in Cluster Botany, Minerals & Elements
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.append(".")

from scratch.curate_botany_b4_p1 import data_botany_b4_p1
from scratch.curate_botany_b4_p2 import data_botany_b4_p2

data_botany_b4 = {}
data_botany_b4.update(data_botany_b4_p1)
data_botany_b4.update(data_botany_b4_p2)

print(f"Total curated entries in Batch 4: {len(data_botany_b4)}")

target_dir = r"App database/Latin roots/Cluster Botany, Minerals & Elements/Dashboard — rad"
print(f"\nProcessing directory: {target_dir}")
files = [f for f in os.listdir(target_dir) if f.endswith('.md') and not f.startswith(('Dashboard', 'Word Triage', 'Cluster', 'Semantic Field'))]
dir_updated = 0

for fname in sorted(files):
    word_key = fname[:-3]
    if word_key not in data_botany_b4:
        matching = [k for k in data_botany_b4 if k.lower() == word_key.lower()]
        if matching:
            word_key = matching[0]
        else:
            print(f"  [ERROR] Word key not found in data: {word_key}")
            continue

    entry = data_botany_b4[word_key]
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

print(f"\nTotal updated in Dashboard — rad: {dir_updated} / {len(files)} files.")
