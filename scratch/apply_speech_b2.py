# -*- coding: utf-8 -*-
"""
Applies curate_speech_b2 to:
- App database/Latin roots/Cluster Speech/Dashboard — cit (65 words)
- App database/Latin roots/Cluster Speech/Dashboard — nunci (17 words)
Total: 82 words.
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.append(".")

from scratch.curate_speech_b2 import data_speech_b2

target_dirs = [
    r"App database/Latin roots/Cluster Speech/Dashboard — cit",
    r"App database/Latin roots/Cluster Speech/Dashboard — nunci"
]

total_updated = 0

for target_dir in target_dirs:
    print(f"\nProcessing directory: {target_dir}")
    files = [f for f in os.listdir(target_dir) if f.endswith('.md') and not f.startswith(('Dashboard', 'Word Triage', 'Cluster', 'Semantic Field'))]
    dir_updated = 0
    
    for fname in sorted(files):
        word_key = fname[:-3]
        if word_key not in data_speech_b2:
            matching = [k for k in data_speech_b2 if k.lower() == word_key.lower()]
            if matching:
                word_key = matching[0]
            else:
                print(f"  [ERROR] Word key not found in data: {word_key}")
                continue

        entry = data_speech_b2[word_key]
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

    print(f"Directory total: {dir_updated} / {len(files)} files updated.")
    total_updated += dir_updated

print(f"\n========================================")
print(f"Grand Total Updated: {total_updated} / 82 files")
print(f"========================================")
