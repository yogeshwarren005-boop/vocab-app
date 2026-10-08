import sqlite3

c_conn = sqlite3.connect('main app/corpus/citation_corpus.db')
c_cur = c_conn.cursor()

words = [
    'bib', 'bibulous', 'imbibe', 'imbiber', 'imbibing', 'imbibition',
    'cocteau', 'concoct', 'concoction', 'decoct', 'decoction',
    'coquet', 'coquetry', 'coquette', 'coquettish', 'coquettishly', 'coquille',
    'abed', 'aged', 'agedness', 'agreed', 'antiquated', 'complicated', 'complicatedness', 'deed', 'ed', 'edibility', 'edible', 'edibleness', 'fenestrated', 'indeed', 'inedible', 'misdeed', 'nonaged', 'overaged', 'posted', 'reed', 'reedy', 'reseed', 'seabed', 'seed', 'seeded', 'seeder', 'seediness', 'seedy', 'tunicated', 'unaged', 'uncomplicated', 'unseeded', 'unveiled', 'veiled',
    'ablactate', 'ablactation', 'extragalactic', 'galactic', 'intergalactic', 'lactaid', 'lactalbumin', 'lactarius', 'lactase', 'lactate', 'lactating', 'lactation', 'lacteal', 'lactescent', 'lactic', 'lactiferous', 'lactifuge', 'lactobacillaceae', 'lactobacillus', 'lactobacteriaceae', 'lactoflavin', 'lactogen', 'lactogenic', 'lactophrys', 'lactoprotein', 'lactose', 'lactosuria', 'lactuca', 'prolactin',
    'mellaril', 'melliferous', 'mellification', 'mellifluent', 'mellifluous', 'mellisonant', 'mellisugent', 'mellivora', 'mellon', 'mellow', 'mellowed', 'mellowing', 'mellowingly', 'mellowly', 'mellowness',
    'companion', 'companionship', 'empanada', 'pan', 'panic', 'panification', 'panivorous', 'pannier', 'pantry',
    'potable', 'potage', 'potash', 'potassium', 'potation', 'potato'
]

print("Total words:", len(words))
coverage = {}
for w in words:
    try:
        c_cur.execute("""
            SELECT s.author, s.work, s.sentence
            FROM sentences_fts f
            JOIN sentences s ON f.rowid = s.id
            WHERE sentences_fts MATCH ?
            LIMIT 50
        """, (f'"{w}"',))
        rows = c_cur.fetchall()
        authors = set(r[0] for r in rows if r[0] and r[0].strip() and r[0] not in ['Academic Lexicon', 'Classic Author'])
        coverage[w] = len(authors)
    except Exception as e:
        coverage[w] = 0

has_3 = [w for w, c in coverage.items() if c >= 3]
less_3 = [w for w, c in coverage.items() if c < 3]
print(f"Words with >= 3 authors in corpus: {len(has_3)}")
print(f"Words with < 3 authors in corpus: {len(less_3)}")
print("Under-covered words:", [(w, coverage[w]) for w in less_3])
