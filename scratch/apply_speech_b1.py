# -*- coding: utf-8 -*-
"""
Applies curate_speech_b1 to all 7 dashboards in Cluster Speech:
1. Dashboard — articul (17 words)
2. Dashboard — claim (16 words)
3. Dashboard — clam (23 words)
4. Dashboard — fari (2 words)
5. Dashboard — garrul (7 words)
6. Dashboard — orat (12 words)
7. Dashboard — suad (6 words)
Total: 83 words
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scratch.curate_speech_b1 import data_speech_b1

targets = [
    r"App database/Latin roots/Cluster Speech/Dashboard — articul",
    r"App database/Latin roots/Cluster Speech/Dashboard — claim",
    r"App database/Latin roots/Cluster Speech/Dashboard — clam",
    r"App database/Latin roots/Cluster Speech/Dashboard — fari",
    r"App database/Latin roots/Cluster Speech/Dashboard — garrul",
    r"App database/Latin roots/Cluster Speech/Dashboard — orat",
    r"App database/Latin roots/Cluster Speech/Dashboard — suad"
]

total_updated = 0

for target_dir in targets:
    if not os.path.exists(target_dir):
        print(f"Directory not found: {target_dir}")
        continue

    files = [f for f in os.listdir(target_dir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]
    dir_updated = 0
    for fname in files:
        word_key = fname[:-3]
        if word_key not in data_speech_b1:
            matching = [k for k in data_speech_b1 if k.lower() == word_key.lower()]
            if matching:
                word_key = matching[0]
            else:
                continue

        entry = data_speech_b1[word_key]
        file_path = os.path.join(target_dir, fname)

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        book_pos = content.find("> [!book]")
        if book_pos == -1:
            print(f"Missing > [!book] in {file_path}")
            continue

        prefix = content[:book_pos].rstrip()

        lines = [
            prefix,
            "",
            "> [!book] 📖 Definitions & Semantic Range",
            f"> 1. **Primary Definition (Lexical / Standard Consensus)**: {entry['primary']}",
            f"> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {entry['secondary']}",
            "",
            "> [!quote] 💬 Contextual Usage & Authentic Quotations"
        ]

        for q in entry["quotes"]:
            lines.append(f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{q['quote']}\"*")

        lines.append("")  # trailing newline

        new_content = "\n".join(lines)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        dir_updated += 1
        total_updated += 1

    print(f"Updated {dir_updated} notes in {os.path.basename(target_dir)}")

print(f"\nSuccessfully applied updates to {total_updated} / 83 notes across all 7 dashboards.")
