# -*- coding: utf-8 -*-
"""
Apply curation data to Markdown notes in:
- App database/Latin roots/Cluster Virtue/Dashboard — dext
- App database/Latin roots/Cluster Virtue/Dashboard — dign
- App database/Latin roots/Cluster Virtue/Dashboard — integ
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

from scratch.curate_virtue_dext_dign_integ import data_virtue_dext_dign_integ

dashboards = [
    r"App database/Latin roots/Cluster Virtue/Dashboard — dext",
    r"App database/Latin roots/Cluster Virtue/Dashboard — dign",
    r"App database/Latin roots/Cluster Virtue/Dashboard — integ"
]

total_applied = 0

for dash_dir in dashboards:
    dash_name = os.path.basename(dash_dir)
    print(f"Processing {dash_name}...")
    files = [f for f in os.listdir(dash_dir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]
    
    for fname in sorted(files):
        word = fname[:-3].lower()
        if word not in data_virtue_dext_dign_integ:
            print(f"  WARNING: Word {word} ({fname}) not found in curation data!")
            continue
            
        file_path = os.path.join(dash_dir, fname)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        book_pos = content.find("> [!book]")
        if book_pos == -1:
            print(f"  ERROR: Missing > [!book] in {file_path}")
            continue
            
        prefix = content[:book_pos]
        entry = data_virtue_dext_dign_integ[word]
        
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
            
        total_applied += 1

print(f"\nSuccessfully applied curation to {total_applied} word notes across all 3 dashboards.")
