# -*- coding: utf-8 -*-
"""
Sync Dashboard — graph in Cluster Writing (58 words) from pristine Greek roots.
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

latin_graph_dir = r"App database/Latin roots/Cluster Writing/Dashboard — graph"
greek_dir = r"App database/Greek roots"

# Index all Greek root files
greek_files_map = {}
for root, dirs, files in os.walk(greek_dir):
    for f in files:
        if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage'):
            greek_files_map[f.lower()] = os.path.join(root, f)

latin_files = [f for f in os.listdir(latin_graph_dir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]

count = 0
for fname in latin_files:
    fl = fname.lower()
    latin_path = os.path.join(latin_graph_dir, fname)

    with open(latin_path, "r", encoding="utf-8") as f:
        latin_content = f.read()

    book_pos = latin_content.find("> [!book]")
    if book_pos == -1:
        print(f"Missing > [!book] in {latin_path}")
        continue
    prefix = latin_content[:book_pos]

    if fl in greek_files_map:
        greek_path = greek_files_map[fl]
        with open(greek_path, "r", encoding="utf-8") as f:
            greek_content = f.read()
        g_book_pos = greek_content.find("> [!book]")
        if g_book_pos == -1:
            print(f"Missing > [!book] in Greek file {greek_path}")
            continue
        curated_body = greek_content[g_book_pos:]
        new_content = prefix + curated_body
        with open(latin_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1
    else:
        print(f"Not in Greek: {fname}")

print(f"Successfully synced {count} files in Dashboard — graph.")
