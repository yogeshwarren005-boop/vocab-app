# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

p_cur = r"App database\Latin roots\Cluster Movement & Speed\Dashboard — cur"
p_curs = r"App database\Latin roots\Cluster Movement & Speed\Dashboard — curs"
p_curr = r"App database\Latin roots\Cluster Movement & Speed\Dashboard — curr"

grafted = 0

def graft_word(src_dir, fname):
    global grafted
    src_path = os.path.join(src_dir, fname)
    target_path = os.path.join(p_cur, fname)
    
    if not os.path.exists(target_path):
        print(f"Target does not exist: {target_path}")
        return
    
    with open(src_path, "r", encoding="utf-8") as f:
        src_content = f.read()
    
    with open(target_path, "r", encoding="utf-8") as f:
        target_content = f.read()
    
    # Extract book and quote callouts from source
    src_book_idx = src_content.find("> [!book]")
    if src_book_idx == -1:
        print(f"No book callout in src: {fname}")
        return
    src_body = src_content[src_book_idx:]
    
    # In target, keep everything before > [!book]
    target_book_idx = target_content.find("> [!book]")
    if target_book_idx == -1:
        print(f"No book callout in target: {fname}")
        return
    target_prefix = target_content[:target_book_idx]
    
    new_content = target_prefix + src_body
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    grafted += 1

# Graft curs files
for f in os.listdir(p_curs):
    if f.endswith(".md") and not f.startswith("Dashboard") and not f.startswith("Word Triage"):
        graft_word(p_curs, f)

# Graft curr files
for f in os.listdir(p_curr):
    if f.endswith(".md") and not f.startswith("Dashboard") and not f.startswith("Word Triage"):
        graft_word(p_curr, f)

print(f"Successfully grafted {grafted} notes into Dashboard — cur.")
