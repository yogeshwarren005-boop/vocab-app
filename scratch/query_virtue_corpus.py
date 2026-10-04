import sqlite3
import json

conn = sqlite3.connect("main app/corpus/citation_corpus.db")
c = conn.cursor()

words = [
    # Dashboard — dext (20 words)
    'ambidexterity', 'ambidextrous', 'ambidextrousness', 'dexter', 'dexterity',
    'dexterous', 'dexterously', 'dextral', 'dextrality', 'dextrin',
    'dextrocardia', 'dextroglucose', 'dextrorotary', 'dextrorotation', 'dextrorotatory',
    'dextrorsal', 'dextrorse', 'dextrose', 'dextrous', 'dextrously',
    # Dashboard — dign (11 words)
    'condign', 'dignified', 'dignify', 'dignifying', 'dignitary',
    'dignity', 'indignant', 'indignantly', 'indignation', 'indignity',
    'undignified',
    # Dashboard — integ (21 words)
    'disintegrable', 'disintegrate', 'disintegration', 'disintegrative', 'integer',
    'integral', 'integrality', 'integrally', 'integrate', 'integrated',
    'integrating', 'integration', 'integrative', 'integrator', 'integrity',
    'integument', 'integumental', 'integumentary', 'nonintegrated', 'reintegrate',
    'unintegrated'
]

corpus_results = {}
for w in words:
    c.execute("""
        SELECT s.author, s.work, s.sentence
        FROM sentences_fts f
        JOIN sentences s ON f.rowid = s.id
        WHERE sentences_fts MATCH ?
    """, (f'"{w}"',))
    rows = c.fetchall()
    by_author = {}
    for auth, work, sent in rows:
        if auth not in by_author and len(sent) < 350 and len(sent) > 25:
            by_author[auth] = {"work": work, "sentence": sent}
    corpus_results[w] = by_author

print(f"Summary of corpus results for {len(words)} words:")
for w in words:
    auth_cnt = len(corpus_results[w])
    print(f"  {w:18}: {auth_cnt} unique authors available")

with open("scratch/corpus_hits_virtue.json", "w", encoding="utf-8") as f:
    json.dump(corpus_results, f, ensure_ascii=False, indent=2)
