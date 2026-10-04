import sqlite3

c_conn = sqlite3.connect("main app/corpus/citation_corpus.db")
c_cur = c_conn.cursor()

words = ['cast', 'castanea', 'castanets', 'castanopsis', 'castanospermum', 'castaway', 'caste', 'casteless', 'castellated', 'caster', 'castigate', 'castigation', 'castile', 'castilian', 'castilla', 'castilleia', 'castilleja', 'castillian', 'casting', 'castle', 'castled', 'castling', 'castor', 'castoridae', 'castoroides', 'castrate', 'castrated', 'castration', 'castrato', 'castries', 'castro', 'castroism', 'miscast', 'overcast', 'overcasting', 'precast', 'recast', 'recasting', 'uncastrated']

missing = []
for w in words:
    c_cur.execute('''
        SELECT count(distinct s.author)
        FROM sentences_fts f
        JOIN sentences s ON f.rowid = s.id
        WHERE sentences_fts MATCH ?
    ''', (f'"{w}"',))
    num_authors = c_cur.fetchone()[0]
    print(f'{w}: {num_authors} authors')
    if num_authors < 3:
        missing.append((w, num_authors))

print('Words with < 3 authors:', missing)
c_conn.close()
