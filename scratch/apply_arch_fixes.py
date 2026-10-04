# -*- coding: utf-8 -*-
"""
Apply 4 arch fixes
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.curate_arch_fixes import data_arch_fixes

latin_arch_dir = r"App database/Latin roots/Cluster General/Dashboard — arch"

for word_key, entry in data_arch_fixes.items():
    file_path = os.path.join(latin_arch_dir, f"{word_key}.md")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    book_pos = content.find("> [!book]")
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
    print(f"Updated {word_key}.md")
