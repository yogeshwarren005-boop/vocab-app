# -*- coding: utf-8 -*-
"""
Apply curation to Dashboard — anti (109 words):
- 43 words synced from pristine Greek roots
- 33 words from curate_anti_p1
- 33 words from curate_anti_p2
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.curate_anti_p1 import data_anti_p1
from scratch.curate_anti_p2 import data_anti_p2

custom_anti = {**data_anti_p1, **data_anti_p2}

latin_anti_dir = r"App database/Latin roots/Cluster General/Dashboard — anti"
greek_dir = r"App database/Greek roots"

# Index all Greek root files
greek_files_map = {}
for root, dirs, files in os.walk(greek_dir):
    for f in files:
        if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage'):
            greek_files_map[f.lower()] = os.path.join(root, f)

latin_files = [f for f in os.listdir(latin_anti_dir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]

count = 0
for fname in latin_files:
    fl = fname.lower()
    latin_path = os.path.join(latin_anti_dir, fname)

    with open(latin_path, "r", encoding="utf-8") as f:
        latin_content = f.read()

    book_pos = latin_content.find("> [!book]")
    if book_pos == -1:
        print(f"Missing > [!book] in {latin_path}")
        continue
    prefix = latin_content[:book_pos]

    word_key = fname[:-3]

    # Prioritize custom curation if present (so modern words get customized accurate definitions)
    if word_key in custom_anti or fl[:-3] in custom_anti:
        entry = custom_anti.get(word_key) or custom_anti.get(fl[:-3])
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
        with open(latin_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1
    elif fl in greek_files_map:
        # Extract callouts from Greek file
        greek_path = greek_files_map[fl]
        with open(greek_path, "r", encoding="utf-8") as f:
            greek_content = f.read()
        g_book_pos = greek_content.find("> [!book]")
        if g_book_pos == -1:
            print(f"Missing > [!book] in Greek file {greek_path}")
            continue
        curated_body = greek_content[g_book_pos:]
        new_content = prefix + curated_body
        with open(latin_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1
    else:
        print(f"Unmatched and not in custom: {fname}")

print(f"Successfully processed {count} files in Dashboard — anti.")
