# -*- coding: utf-8 -*-
"""
apply_can_dog.py
Applies curate_can_dog to Dashboard — can_dog (164 words) in Cluster Animal & Plant.
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.append(".")

from scratch.curate_can_dog import data_can_dog

target_dir = r"App database/Latin roots/Cluster Animal & Plant/Dashboard — can_dog"
print(f"\nProcessing directory: {target_dir}")

files = [f for f in os.listdir(target_dir) if f.endswith('.md') and not f.startswith(('Dashboard', 'Word Triage', 'Cluster', 'Semantic Field'))]
dir_updated = 0

for fname in sorted(files):
    word_key = fname[:-3]
    if word_key not in data_can_dog:
        matching = [k for k in data_can_dog if k.lower() == word_key.lower()]
        if matching:
            word_key = matching[0]
        else:
            print(f"  [ERROR] Word key not found in data: {word_key}")
            continue

    entry = data_can_dog[word_key]
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

print(f"\nDirectory Dashboard — can_dog: {dir_updated} / {len(files)} files updated.")
