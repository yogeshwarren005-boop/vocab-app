# -*- coding: utf-8 -*-
import os
import sqlite3
import json
import re

base_path = 'App database/Latin roots/Cluster Law'
dashboards = ['jud', 'jur', 'leg', 'lic', 'litig', 'mand', 'pact', 'pen_punish', 'poen', 'spond', 'test', 'test_witness']

all_dirs = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
dir_map = {}
for root in dashboards:
    matched = [d for d in all_dirs if d.split('—')[-1].strip() == root or d.endswith(' ' + root)][0]
    dir_map[root] = matched

print('Matched directories:', dir_map)

words_by_root = {}
total_words = 0
for root, dirname in dir_map.items():
    dp = os.path.join(base_path, dirname)
    words = sorted([f[:-3] for f in os.listdir(dp) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')])
    print(f"{dirname}: {len(words)} words")
    words_by_root[root] = words
    total_words += len(words)

print(f"Total words in Cluster Law: {total_words}")

# Save the word lists to a json
with open('scratch/law_words.json', 'w', encoding='utf-8') as f:
    json.dump({
        'dir_map': dir_map,
        'words_by_root': words_by_root
    }, f, indent=2, ensure_ascii=False)

print("Saved words to scratch/law_words.json")
