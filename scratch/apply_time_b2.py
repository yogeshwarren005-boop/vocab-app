# -*- coding: utf-8 -*-
"""
apply_time_b2.py
Applies curated definitions and quotations to all 74 words in:
App database/Latin roots/Cluster Time/Dashboard — ann
"""

import os
import sys
from curate_time_b2 import data_time_b2

sys.stdout.reconfigure(encoding="utf-8")

target_dir = r"App database\Latin roots\Cluster Time\Dashboard — ann"
updated_count = 0
missing_files = []

for word, info in data_time_b2.items():
    file_path = os.path.join(target_dir, f"{word}.md")
    if not os.path.exists(file_path):
        missing_files.append(file_path)
        continue
    
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
    
    updated_count += 1

print(f"Update Summary:")
print(f"  Successfully updated: {updated_count}/{len(data_time_b2)} word files.")
if missing_files:
    print(f"  Missing files: {missing_files}")
