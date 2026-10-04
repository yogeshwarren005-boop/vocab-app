# -*- coding: utf-8 -*-
"""
Applies curate_binding_b3 to:
- Dashboard — lig (66 words)
- Dashboard — strict (23 words)
- Dashboard — string (17 words)
Total: 106 words
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.append(".")

from scratch.curate_binding_b3 import data_binding_b3

targets = [
    r"App database/Latin roots/Cluster Binding/Dashboard — lig",
    r"App database/Latin roots/Cluster Binding/Dashboard — strict",
    r"App database/Latin roots/Cluster Binding/Dashboard — string"
]

total_updated = 0
total_files = 0

for target_dir in targets:
    if not os.path.exists(target_dir):
        print(f"Directory not found: {target_dir}")
        continue
        
    files = [f for f in os.listdir(target_dir) if f.endswith('.md') and not f.startswith(('Dashboard', 'Word Triage', 'Cluster', 'Semantic Field'))]
    print(f"\nProcessing {target_dir} ({len(files)} files)...")
    
    dir_updated = 0
    for fname in sorted(files):
        total_files += 1
        word_key = fname[:-3]
        if word_key not in data_binding_b3:
            matching = [k for k in data_binding_b3 if k.lower() == word_key.lower()]
            if matching:
                word_key = matching[0]
            else:
                print(f"  ❌ Word key not found in data: {word_key}")
                continue

        entry = data_binding_b3[word_key]
        file_path = os.path.join(target_dir, fname)

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        book_pos = content.find("> [!book]")
        if book_pos == -1:
            print(f"  ❌ Missing > [!book] in {file_path}")
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
        total_updated += 1
        print(f"  ✅ Updated: {fname}")
        
    print(f"Finished {target_dir}: {dir_updated} / {len(files)} updated.")

print(f"\n========================================")
print(f"TOTAL FILES UPDATED: {total_updated} / {total_files}")
print(f"========================================")
