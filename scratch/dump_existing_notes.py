# -*- coding: utf-8 -*-
import os
import sys
import re
import json

base = r"App database/Latin roots/Cluster Time"
roots = ["cras", "di", "ev", "nov", "saecul", "simul"]

all_words = {}

for r in roots:
    d = os.path.join(base, f"Dashboard — {r}")
    files = [
        f for f in os.listdir(d)
        if f.endswith(".md")
        and not f.startswith(("Dashboard", "Word Triage", "Cluster", "Semantic"))
    ]
    for fn in sorted(files):
        w = fn[:-3]
        fp = os.path.join(d, fn)
        with open(fp, "r", encoding="utf-8") as f:
            txt = f.read()

        pMatch = re.search(r"1\.\s*\*\*([^*]+)\*\*:\s*([^\r\n]+)", txt)
        sMatch = re.search(r"2\.\s*\*\*([^*]+)\*\*:\s*([^\r\n]+)", txt)
        p = pMatch[2].strip() if pMatch else ""
        s = sMatch[2].strip() if sMatch else ""

        qsec = txt.split("> [!quote]")[1] if "> [!quote]" in txt else ""
        quote_lines = [
            l.strip()
            for l in qsec.split("\n")
            if l.strip().startswith(">") and "📜" in l
        ]

        parsed_quotes = []
        for ql in quote_lines:
            authMatch = re.search(
                r"📜\s*\*\*([^*]+?)\s*(?:\(\*([^*]+?)\*\):?\*\*|\*\*\s*\(\*([^*]+?)\*\):?)",
                ql,
            )
            colonMatch = re.search(r":\*\*\s*(.+)$", ql)
            author = authMatch[1].strip() if authMatch else "Unknown"
            work = (
                (authMatch[2] or authMatch[3] or "").strip()
                if authMatch
                else "Unknown"
            )
            quote_text = colonMatch[1].strip() if colonMatch else ql
            parsed_quotes.append({
                "author": author,
                "work": work,
                "quote_text": quote_text,
                "line": ql,
            })

        all_words[w] = {
            "root": r,
            "primary": p,
            "secondary": s,
            "quotes_count": len(parsed_quotes),
            "quotes": parsed_quotes,
        }

with open("scratch/existing_notes_dump.json", "w", encoding="utf-8") as f:
    json.dump(all_words, f, indent=2, ensure_ascii=False)

three_q = [w for w, info in all_words.items() if info["quotes_count"] == 3]
one_q = [w for w, info in all_words.items() if info["quotes_count"] == 1]
other_q = [w for w, info in all_words.items() if info["quotes_count"] not in (1, 3)]

print(f"Total words dumped: {len(all_words)}")
print(f"Words with 3 quotes ({len(three_q)}): {three_q}")
print(f"Words with 1 quote ({len(one_q)}): {one_q}")
print(f"Words with other quotes ({len(other_q)}): {other_q}")
