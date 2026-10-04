# -*- coding: utf-8 -*-
"""
Syncs all 65 words in Dashboard — not (Cluster Writing)
from Dashboard — nosc (Cluster Mind & Knowledge).
Preserves frontmatter of Dashboard — not.
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

src_dir = r"App database/Latin roots/Cluster Mind & Knowledge/Dashboard — nosc"
dst_dir = r"App database/Latin roots/Cluster Writing/Dashboard — not"

files = [f for f in os.listdir(dst_dir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]

count = 0
for fname in sorted(files):
    src_file = os.path.join(src_dir, fname)
    dst_file = os.path.join(dst_dir, fname)

    if not os.path.exists(src_file):
        print(f"Source file not found: {src_file}")
        continue

    with open(src_file, "r", encoding="utf-8") as f:
        src_content = f.read()

    with open(dst_file, "r", encoding="utf-8") as f:
        dst_content = f.read()

    src_book_pos = src_content.find("> [!book]")
    dst_book_pos = dst_content.find("> [!book]")

    if src_book_pos == -1 or dst_book_pos == -1:
        print(f"Missing > [!book] in {fname}")
        continue

    # Keep destination frontmatter/header, take book + quote content from source
    dst_prefix = dst_content[:dst_book_pos]
    src_body = src_content[src_book_pos:]

    new_content = dst_prefix + src_body

    with open(dst_file, "w", encoding="utf-8") as f:
        f.write(new_content)

    count += 1
    print(f"Synced: {fname}")

print(f"\nTotal files synced: {count}")
