import sqlite3
import json

conn = sqlite3.connect('main app/corpus/citation_corpus.db')
c = conn.cursor()

words = [
    'acardia', 'arda', 'ardea', 'ardeb', 'ardeidae', 'ardennes', 'ardent', 'ardently', 'ardisia', 'ardor', 'ardour', 'ards', 'arduous', 'arduously', 'arduousness', 'eardrop', 'eardrum',
    'cineraria', 'cinerarium', 'cinerary', 'cinereous', 'incinerate', 'incineration', 'incinerator',
    'cremains', 'cremate', 'cremation', 'crematorium', 'crematory', 'cremona', 'decrement', 'excrement', 'increment', 'incremental',
    'conferva', 'defervesce', 'defervescence', 'defervescent', 'effervesce', 'effervescence', 'effervescent', 'effervescing', 'fervency', 'fervent', 'fervently', 'fervescent', 'fervid', 'fervidly', 'fervidness', 'fervor', 'fervour', 'noneffervescent', 'perfervid',
    'flambeau', 'flame', 'flame-colored', 'flame-coloured', 'flame-flower', 'flame-orange', 'flame-out', 'flame-retardant', 'flamefish', 'flameflower', 'flamen', 'flamenco', 'flameproof', 'flamethrower', 'flaming', 'flamingo', 'flaminius', 'flammability', 'flammable', 'flammulina', 'inflame', 'inflamed', 'inflaming', 'inflammability', 'inflammable', 'inflammation', 'inflammatory', 'nonflammable', 'noninflammatory', 'proinflammatory',
    'congelation', 'gelatin', 'gelatine', 'gelatinise', 'gelatinize', 'gelatinlike', 'gelatinous', 'gelatinousness',
    'antepartum', 'antepenult', 'antepenultima', 'antepenultimate', 'tepal', 'tepee', 'tepic', 'tepid', 'tepidity', 'tepidly', 'tepidness',
    'torr', 'torrefaction', 'torrent', 'torrential', 'torreon', 'torreya', 'torricelli', 'torrid', 'torridity',
    'volcanic', 'volcanically', 'volcanism', 'volcano', 'volcanology'
]

print(f"Total words: {len(words)}")

corpus_results = {}
for w in words:
    # search clean token
    search_q = f'"{w}"' if '-' not in w else f'"{w.replace("-", " ")}"'
    try:
        c.execute('''
            SELECT s.author, s.work, s.sentence
            FROM sentences_fts f
            JOIN sentences s ON f.rowid = s.id
            WHERE sentences_fts MATCH ?
        ''', (search_q,))
        rows = c.fetchall()
    except Exception as e:
        rows = []
    by_author = {}
    for auth, work, sent in rows:
        if auth not in by_author and 25 < len(sent) < 400:
            by_author[auth] = {'work': work, 'sentence': sent}
    corpus_results[w] = by_author

with open('scratch/corpus_hits_fire_noncal.json', 'w', encoding='utf-8') as f:
    json.dump(corpus_results, f, ensure_ascii=False, indent=2)

print('Done searching DB!')
counts = {w: len(corpus_results[w]) for w in words}
print(f"Words with >= 3 authors in corpus: {sum(1 for c in counts.values() if c >= 3)} / {len(words)}")
for w in words:
    if counts[w] < 3:
        print(f"  {w:20}: {counts[w]} authors")
