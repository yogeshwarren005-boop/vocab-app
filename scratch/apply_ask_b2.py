# -*- coding: utf-8 -*-
"""
apply_ask_b2.py
Applies curated definitions and quotations to all 82 words in:
- Dashboard — rog (40 words)
- Dashboard — pris (42 words)
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("scratch"))

from curate_ask_b2 import data_ask_b2

dashboards = [
    ("Dashboard — rog", r"App database\Latin roots\Cluster Asking & Seeking\Dashboard — rog"),
    ("Dashboard — pris", r"App database\Latin roots\Cluster Asking & Seeking\Dashboard — pris"),
]

total_updated = 0
missing_files = []

for db_name, target_dir in dashboards:
    db_updated = 0
    files = [
        f for f in os.listdir(target_dir)
        if f.endswith(".md")
        and not f.startswith("Dashboard")
        and not f.startswith("Word Triage")
        and not f.startswith("Cluster")
        and not f.startswith("Semantic")
    ]
    
    for fname in sorted(files):
        word_key = fname[:-3]
        if word_key not in data_ask_b2:
            missing_files.append((db_name, word_key))
            continue
        
        info = data_ask_b2[word_key]
        file_path = os.path.join(target_dir, fname)
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        book_idx = content.find("> [!book]")
        if book_idx == -1:
            print(f"Error: Missing > [!book] callout in {file_path}")
            continue
        
        prefix = content[:book_idx]
        
        p_def = info["primary"].strip().rstrip(".") + "."
        s_def = info["secondary"].strip().rstrip(".") + "."
        
        new_book = (
            "> [!book] 📖 Definitions & Semantic Range\n"
            f"> 1. **Primary Definition (Lexical / Standard Consensus)**: {p_def}\n"
            f"> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {s_def}\n"
        )
        
        new_quotes = "> [!quote] 💬 Contextual Usage & Authentic Quotations\n"
        for q in info["quotes"]:
            auth = q["author"].strip()
            work = q["work"].strip()
            quote_text = q["quote"].strip().strip('"').strip('“').strip('”')
            new_quotes += f'> - 📜 **{auth} (*{work}*):** *"{quote_text}"*\n'
        
        new_content = prefix + new_book + "\n" + new_quotes + "\n"
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        
        db_updated += 1
        total_updated += 1
        
    print(f"Updated {db_updated}/{len(files)} files in {db_name}")

print(f"\nTotal updated across both dashboards: {total_updated}/82")
if missing_files:
    print(f"Missing files ({len(missing_files)}): {missing_files}")
else:
    print("All 82 files successfully updated!")
