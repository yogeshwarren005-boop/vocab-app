# -*- coding: utf-8 -*-
import sqlite3, os, sys, json, re

sys.stdout.reconfigure(encoding="utf-8")

c_conn = sqlite3.connect("main app/corpus/citation_corpus.db")
c_cur = c_conn.cursor()

cluster = "App database/Latin roots/Cluster Mind & Knowledge"
target_dashboards = ["Dashboard — phil", "Dashboard — psych"]

for d in target_dashboards:
    dpath = os.path.join(cluster, d)
    files = sorted([f for f in os.listdir(dpath) if f.endswith(".md") and not f.startswith("Dashboard") and not f.startswith("Word Triage")])
    print(f"\n=== {d} ({len(files)} words) ===")
    rich = 0
    for f in files:
        w = f[:-3]
        clean_w = w.replace("-", " ")
        try:
            c_cur.execute("""
                SELECT s.author, s.work, s.sentence
                FROM sentences_fts f
                JOIN sentences s ON f.rowid = s.id
                WHERE sentences_fts MATCH ?
                LIMIT 20
            """, (f'"{clean_w}"',))
            raw = c_cur.fetchall()
        except:
            raw = []
        
        pattern = re.compile(rf"\b{re.escape(w)}\b", re.IGNORECASE)
        authors = set()
        for a, wk, s in raw:
            if pattern.search(s):
                authors.add(a)
        if len(authors) >= 3:
            rich += 1
        print(f"  {w:24s}: {len(authors)} authors in DB")
    print(f"Rich words (>= 3 authors): {rich}/{len(files)}")

c_conn.close()
