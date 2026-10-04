import sqlite3

conn = sqlite3.connect("main app/corpus/citation_corpus.db")
c = conn.cursor()

test_words = ["facial", "facile", "facilitate", "facility", "facsimile", "faculty", "magnificent", "manufacture", "office", "official"]
for w in test_words:
    c.execute("SELECT count(*) FROM sentences WHERE word_stem = ? OR sentence LIKE ?", (w, f"%{w}%"))
    cnt = c.fetchone()[0]
    print(f"{w}: {cnt} hits")

conn.close()
