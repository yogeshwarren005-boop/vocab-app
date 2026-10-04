import sqlite3

c_conn = sqlite3.connect("main app/corpus/citation_corpus.db")
c_cur = c_conn.cursor()

words = [
    'ambidexterity', 'ambidextrous', 'ambidextrousness', 'dexter', 'dexterity',
    'dexterous', 'dexterously', 'dextral', 'dextrality', 'dextrin',
    'dextrocardia', 'dextroglucose', 'dextrorotary', 'dextrorotation', 'dextrorotatory',
    'dextrorsal', 'dextrorse', 'dextrose', 'dextrous', 'dextrously',
    'condign', 'dignified', 'dignify', 'dignifying', 'dignitary',
    'dignity', 'indignant', 'indignantly', 'indignation', 'indignity',
    'undignified',
    'disintegrable', 'disintegrate', 'disintegration', 'disintegrative', 'integer',
    'integral', 'integrality', 'integrally', 'integrate', 'integrated',
    'integrating', 'integration', 'integrative', 'integrator', 'integrity',
    'integument', 'integumental', 'integumentary', 'nonintegrated', 'reintegrate',
    'unintegrated'
]

low = []
for w in words:
    c_cur.execute("""
        SELECT count(distinct s.author)
        FROM sentences_fts f
        JOIN sentences s ON f.rowid = s.id
        WHERE sentences_fts MATCH ?
    """, (f'"{w}"',))
    cnt = c_cur.fetchone()[0]
    if cnt < 3:
        low.append((w, cnt))

print(f"Words with < 3 distinct authors in corpus: {len(low)}")
for w, cnt in low:
    print(f"  {w}: {cnt}")
