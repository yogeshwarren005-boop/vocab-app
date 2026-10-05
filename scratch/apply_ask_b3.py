# -*- coding: utf-8 -*-
"""
apply_ask_b3.py
Applies curated data from curate_ask_b3 to:
App database/Latin roots/Cluster Asking & Seeking/Dashboard — pet (127 words)
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("scratch"))

from scratch.curate_ask_b3 import data_ask_b3

target_dir = r"App database/Latin roots/Cluster Asking & Seeking/Dashboard — pet"

if not os.path.exists(target_dir):
    print(f"Directory not found: {target_dir}")
    sys.exit(1)

files = [
    f
    for f in os.listdir(target_dir)
    if f.endswith(".md")
    and not f.startswith("Dashboard")
    and not f.startswith("Word Triage")
    and not f.startswith("Cluster")
    and not f.startswith("Semantic")
]

total_updated = 0
missing_words = []

for fname in sorted(files):
    word_key = fname[:-3]
    if word_key not in data_ask_b3:
        # try case insensitive match
        matching = [k for k in data_ask_b3 if k.lower() == word_key.lower()]
        if matching:
            word_key = matching[0]
        else:
            missing_words.append(word_key)
            continue

    entry = data_ask_b3[word_key]
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

    total_updated += 1

print(f"\nUpdated {total_updated} / {len(files)} notes in {os.path.basename(target_dir)}.")
if missing_words:
    print(f"Missing words ({len(missing_words)}): {missing_words}")
else:
    print("All notes matched and updated successfully!")
