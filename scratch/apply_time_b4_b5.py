# -*- coding: utf-8 -*-
"""
Applies curation data from scratch/curate_time_b4_b5.py to both:
- App database/Latin roots/Cluster Time/Dashboard — post
- App database/Latin roots/Cluster Time/Dashboard — temp
"""
import os
import sys
from curate_time_b4_b5 import data_time_b4_b5

post_dir = r"App database\Latin roots\Cluster Time\Dashboard — post"
temp_dir = r"App database\Latin roots\Cluster Time\Dashboard — temp"

updated_post = 0
updated_temp = 0
not_found = []

for fname, info in data_time_b4_b5.items():
    p_path = os.path.join(post_dir, fname)
    t_path = os.path.join(temp_dir, fname)
    
    target_path = None
    is_post = False
    if os.path.exists(p_path):
        target_path = p_path
        is_post = True
    elif os.path.exists(t_path):
        target_path = t_path
        is_post = False
    else:
        not_found.append(fname)
        continue
        
    with open(target_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    book_idx = content.find("> [!book]")
    if book_idx == -1:
        print(f"Warning: No > [!book] found in {target_path}")
        continue
        
    prefix = content[:book_idx]
    
    p_def = info["primary"].strip().rstrip(".") + "."
    s_def = info["secondary"].strip().rstrip(".") + "."
    
    new_book = (
        "> [!book] 📖 Definitions & Semantic Range\n"
        f"> 1. **Primary Definition (Lexical / Standard Consensus)**: {p_def}\n"
        f"> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {s_def}\n"
    )
    
    new_quote = "> [!quote] 💬 Contextual Usage & Authentic Quotations\n"
    for q in info["quotes"]:
        auth = q["author"].strip()
        work = q["work"].strip()
        quote_text = q["quote"].strip().strip('"').strip('“').strip('”')
        new_quote += f'> - 📜 **{auth} (*{work}*):** *"{quote_text}"*\n'
        
    new_content = prefix + new_book + "\n" + new_quote + "\n"
    
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    if is_post:
        updated_post += 1
    else:
        updated_temp += 1

print(f"Update Summary:")
print(f"  Dashboard — post updated: {updated_post} files")
print(f"  Dashboard — temp updated: {updated_temp} files")
print(f"  Total updated: {updated_post + updated_temp} / {len(data_time_b4_b5)}")
if not_found:
    print(f"  Not found ({len(not_found)}): {not_found}")
