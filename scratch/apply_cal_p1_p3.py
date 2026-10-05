import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

import scratch.curate_fire_cal_p1 as p1
import scratch.curate_fire_cal_p3 as p3

data_all = {}
data_all.update(p1.data_fire_cal_p1)
data_all.update(p3.data_fire_cal_p3)

target_dir = r"App database/Latin roots/Cluster Fire, Heat & Ash/Dashboard — cal"
files = [f for f in os.listdir(target_dir) if f.endswith(".md") and not f.startswith("Dashboard") and not f.startswith("Word Triage")]

count = 0
for fname in files:
    word_key = fname[:-3]
    if word_key not in data_all:
        continue

    entry = data_all[word_key]
    file_path = os.path.join(target_dir, fname)

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    book_pos = content.find("> [!book]")
    if book_pos == -1:
        print(f"Missing > [!book] in {file_path}")
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

    count += 1

print(f"Successfully updated {count} files in Dashboard — cal (p1 + p3).")
