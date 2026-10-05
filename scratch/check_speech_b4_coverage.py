import sqlite3

words = ['agnomen', 'bilingual', 'bilingualism', 'bilingualist', 'bilingually', 'colloquial', 'colloquialism', 'colloquially', 'colloquium', 'colloquy', 'denominate', 'denomination', 'denominational', 'denominationalism', 'denominationally', 'denominator', 'eloquence', 'eloquent', 'eloquently', 'extralinguistic', 'grandiloquence', 'grandiloquent', 'grandiloquently', 'ignominious', 'ignominiously', 'ignominiousness', 'ignominy', 'ineloquently', 'interdenominational', 'interlingua', 'intralinguistic', 'lingua', 'lingual', 'lingually', 'lingualumina', 'linguica', 'linguine', 'linguini', 'linguist', 'linguistic', 'linguistically', 'linguistics', 'lingulate', 'loquacious', 'loquaciously', 'loquaciousness', 'loquacity', 'loquat', 'noma', 'nomad', 'nomadic', 'nome', 'nomenclature', 'nomenklatura', 'nomia', 'nominal', 'nominalism', 'nominalist', 'nominalistic', 'nominally', 'nominate', 'nominated', 'nomination', 'nominative', 'nominator', 'nominee', 'nomogram', 'nomograph', 'nomothetic', 'nondenominational', 'nonlinguistic', 'nonnomadic', 'obloquy', 'prenominal', 'pronominal', 'soliloquise', 'soliloquize', 'soliloquy', 'somniloquent', 'somniloquism', 'somniloquist', 'somniloquy', 'sublingual', 'undenominational']

conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cur = conn.cursor()

found = {}
for w in words:
    cur.execute('''
        SELECT count(distinct s.author)
        FROM sentences_fts f
        JOIN sentences s ON f.rowid = s.id
        WHERE sentences_fts MATCH ?
    ''', (f'"{w}"',))
    cnt = cur.fetchone()[0]
    found[w] = cnt

low = {k: v for k, v in found.items() if v < 3}
print(f"Total words: {len(words)}")
print(f"Words with >= 3 distinct authors in corpus: {len(words) - len(low)}")
print(f"Words with < 3 authors in corpus: {len(low)}")
for k, v in sorted(low.items(), key=lambda x: x[1]):
    print(f"  {k}: {v} distinct authors")
conn.close()
