import sqlite3
import json

words = ['agnomen', 'bilingual', 'bilingualism', 'bilingualist', 'bilingually', 'colloquial', 'colloquialism', 'colloquially', 'colloquium', 'colloquy', 'denominate', 'denomination', 'denominational', 'denominationalism', 'denominationally', 'denominator', 'eloquence', 'eloquent', 'eloquently', 'extralinguistic', 'grandiloquence', 'grandiloquent', 'grandiloquently', 'ignominious', 'ignominiously', 'ignominiousness', 'ignominy', 'ineloquently', 'interdenominational', 'interlingua', 'intralinguistic', 'lingua', 'lingual', 'lingually', 'lingualumina', 'linguica', 'linguine', 'linguini', 'linguist', 'linguistic', 'linguistically', 'linguistics', 'lingulate', 'loquacious', 'loquaciously', 'loquaciousness', 'loquacity', 'loquat', 'noma', 'nomad', 'nomadic', 'nome', 'nomenclature', 'nomenklatura', 'nomia', 'nominal', 'nominalism', 'nominalist', 'nominalistic', 'nominally', 'nominate', 'nominated', 'nomination', 'nominative', 'nominator', 'nominee', 'nomogram', 'nomograph', 'nomothetic', 'nondenominational', 'nonlinguistic', 'nonnomadic', 'obloquy', 'prenominal', 'pronominal', 'soliloquise', 'soliloquize', 'soliloquy', 'somniloquent', 'somniloquism', 'somniloquist', 'somniloquy', 'sublingual', 'undenominational']

conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cur = conn.cursor()

corpus_data = {}
for w in words:
    cur.execute('''
        SELECT s.author, s.work, s.sentence
        FROM sentences_fts f
        JOIN sentences s ON f.rowid = s.id
        WHERE sentences_fts MATCH ?
    ''', (f'"{w}"',))
    rows = cur.fetchall()
    seen_authors = set()
    dedup = []
    for auth, work, sent in rows:
        if auth not in seen_authors and 25 < len(sent) < 350:
            seen_authors.add(auth)
            dedup.append({'author': auth, 'work': work, 'quote': sent})
    if dedup:
        corpus_data[w] = dedup

print(f"Words with corpus hits: {len(corpus_data)}")
for w, hits in sorted(corpus_data.items()):
    print(f"  {w}: {len(hits)} hits")

with open('scratch/speech_b4_corpus_hits.json', 'w', encoding='utf-8') as f:
    json.dump(corpus_data, f, ensure_ascii=False, indent=2)
conn.close()
