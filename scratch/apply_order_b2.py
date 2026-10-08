import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from curate_order_b2_p1 import data_order_b2_p1
from curate_order_b2_p2 import data_order_b2_p2

all_data = {**data_order_b2_p1, **data_order_b2_p2}
cluster_dir = r"App database/Latin roots/Cluster Order"
dashboards = [
    "Dashboard — sequ",
    "Dashboard — termin",
    "Dashboard — ord"
]

updated_count = 0

for db in dashboards:
    db_path = os.path.join(cluster_dir, db)
    files = [f for f in os.listdir(db_path) if f.endswith(".md") and not f.startswith(("Dashboard —", "Word Triage —"))]
    for filename in sorted(files):
        word_key = filename[:-3].lower().strip()
        if word_key not in all_data:
            print(f"WARNING: {word_key} not found in all_data!")
            continue

        item = all_data[word_key]
        file_path = os.path.join(db_path, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Find position of > [!book]
        book_pos = content.find("> [!book]")
        if book_pos == -1:
            print(f"ERROR: > [!book] not found in {file_path}")
            continue

        prefix = content[:book_pos]

        # Construct new definitions and quotes block
        q_lines = []
        for q in item["quotes"]:
            author = q["author"]
            work = q["work"]
            quote_text = q["quote"]
            q_lines.append(f"> - 📜 **{author} (*{work}*):** *\"{quote_text}\"*")

        new_body = (
            f"> [!book] 📖 Definitions & Semantic Range\n"
            f"> 1. **Primary Definition (Lexical / Standard Consensus)**: {item['primary']}\n"
            f"> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {item['secondary']}\n"
            f"\n"
            f"> [!quote] 💬 Contextual Usage & Authentic Quotations\n"
            + "\n".join(q_lines) + "\n"
        )

        full_new_content = prefix + new_body
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(full_new_content)

        updated_count += 1

print(f"Successfully updated {updated_count} files across 3 dashboards in Cluster Order Batch 2.")
