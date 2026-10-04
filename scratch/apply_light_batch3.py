# -*- coding: utf-8 -*-
"""
Apply curated definitions and citations for Light Batch 3:
- Dashboard — pale (48 words)
"""
import os, re, sys
sys.stdout.reconfigure(encoding="utf-8")

from curate_light_batch3 import data_batch3_pale

BASE = r"c:\Users\user\Desktop\Vocab app\App database\Latin roots\Cluster Light"

BATCHES = [
    (os.path.join(BASE, "Dashboard — pale"), data_batch3_pale),
]

BOOK_ANCHOR = re.compile(r'>\s*\[!book\].*', re.IGNORECASE)

def build_block(entry):
    p = entry["primary"]
    s = entry["secondary"]
    q1, q2, q3 = entry["quotes"]
    lines = [
        f"> [!book] 📖 Definitions & Semantic Range",
        f"> 1. **Primary Definition (Lexical / Standard Consensus)**: {p}",
        f"> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {s}",
        f"",
        f"> [!quote] 💬 Contextual Usage & Authentic Quotations",
        f"> - 📜 **{q1['author']} (*{q1['work']}*):** *\"{q1['quote']}\"*",
        f"> - 📜 **{q2['author']} (*{q2['work']}*):** *\"{q2['quote']}\"*",
        f"> - 📜 **{q3['author']} (*{q3['work']}*):** *\"{q3['quote']}\"*",
    ]
    return "\n".join(lines)

updated = 0
errors = []

for dashboard_path, data in BATCHES:
    for word, entry in data.items():
        fpath = os.path.join(dashboard_path, f"{word}.md")
        if not os.path.exists(fpath):
            errors.append(f"MISSING: {fpath}")
            continue
        with open(fpath, encoding="utf-8") as f:
            content = f.read()
        m = BOOK_ANCHOR.search(content)
        if not m:
            errors.append(f"NO ANCHOR in {fpath}")
            continue
        prefix = content[:m.start()]
        new_block = build_block(entry)
        new_content = prefix + new_block + "\n"
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        updated += 1

print(f"Updated: {updated}")
if errors:
    print(f"ERRORS ({len(errors)}):")
    for e in errors:
        print(f"  {e}")
    sys.exit(1)
else:
    print("All files written successfully.")
