import sqlite3

words = ['cast', 'castanea', 'castanets', 'castanopsis', 'castanospermum', 'castaway', 'caste', 'casteless', 'castellated', 'caster', 'castigate', 'castigation', 'castile', 'castilian', 'castilla', 'castilleia', 'castilleja', 'castillian', 'casting', 'castle', 'castled', 'castling', 'castor', 'castoridae', 'castoroides', 'castrate', 'castrated', 'castration', 'castrato', 'castries', 'castro', 'castroism', 'miscast', 'overcast', 'overcasting', 'precast', 'recast', 'recasting', 'uncastrated']

c_conn = sqlite3.connect("main app/corpus/citation_corpus.db")
c_cur = c_conn.cursor()

found = {}
for w in words:
    c_cur.execute('''
        SELECT s.author, s.work, s.sentence
        FROM sentences_fts f
        JOIN sentences s ON f.rowid = s.id
        WHERE sentences_fts MATCH ?
    ''', (f'"{w}"',))
    rows = c_cur.fetchall()
    found[w] = rows

for w, rows in found.items():
    authors = set(r[0] for r in rows)
    print(f"{w}: {len(rows)} sentences, {len(authors)} distinct authors: {list(authors)[:5]}")

c_conn.close()
