# -*- coding: utf-8 -*-
import os, glob, re, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")

db_path = os.path.join("main app", "corpus", "citation_corpus.db")
con = sqlite3.connect(db_path)
cur = con.cursor()

def test_dashboard(dpath):
    files = glob.glob(dpath + "/*.md")
    words = [os.path.splitext(os.path.basename(f))[0] for f in files if not os.path.basename(f).startswith(("Dashboard", "Word Triage", "Cluster", "Semantic"))]
    full_hits = 0
    partial_hits = 0
    zero_hits = 0
    missing = []
    for w in words:
        q_word = re.sub(r'[^a-zA-Z0-9]', '', w)
        res = []
        if q_word:
            try:
                matches = cur.execute("""
                    SELECT s.author, s.work, s.sentence 
                    FROM sentences_fts f
                    JOIN sentences s ON f.rowid = s.id
                    WHERE sentences_fts MATCH ?
                    LIMIT 1000;
                """, (f'"{q_word}"',)).fetchall()
                pat = re.compile(rf'\b{re.escape(w)}\b', re.IGNORECASE)
                seen_authors = set()
                for r in matches:
                    if r[0] not in seen_authors and pat.search(r[2]):
                        seen_authors.add(r[0])
                        res.append(r)
                    if len(res) >= 3:
                        break
            except Exception:
                pass
        if len(res) == 3:
            full_hits += 1
        elif len(res) > 0:
            partial_hits += 1
            missing.append((w, len(res)))
        else:
            zero_hits += 1
            missing.append((w, 0))
    dname = os.path.basename(dpath)
    print(f"{dname}: {len(words)} words -> {full_hits} full 3-quotes, {partial_hits} partial (1-2), {zero_hits} zero")
    if missing:
        print(f"   Missing/Partial: {missing}")

for d in ['Dashboard — avid', 'Dashboard — furi', 'Dashboard — miser', 'Dashboard — ridi', 'Dashboard — horr', 'Dashboard — jubil']:
    test_dashboard("App database/Latin roots/Cluster Emotion/" + d)
