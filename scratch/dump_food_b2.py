import sqlite3
import json

words = ['agal', 'al', 'alacritous', 'alacrity', 'albedo', 'albescent', 'albite', 'albitic', 'alible', 'aliment', 'alimentary', 'alimentation', 'alimentative', 'alimony', 'allocution', 'anal', 'animal', 'animalise', 'animalism', 'animalistic', 'animality', 'animalize', 'anticlerical', 'archival', 'auroral', 'bifocals', 'caldera', 'calor', 'cataloger', 'catalogue', 'cataloguer', 'coal', 'coalesce', 'coalesced', 'coalescence', 'coalescency', 'coalescent', 'coalescing', 'coalition', 'colloquialism', 'comal', 'comical', 'comicality', 'comically', 'contextual', 'contextualism', 'contextually', 'coral', 'cordial', 'cordiality', 'cordially', 'coxalgic', 'craniofacial', 'criminal', 'criminalise', 'criminalism', 'criminality', 'criminalize', 'criminally', 'criminalness', 'deal', 'dealer', 'dealership', 'dealing', 'dealings', 'decriminalise', 'decriminalize', 'dial', 'irreality', 'misdeal', 'opal', 'opalise', 'opalize', 'orally', 'oratorical', 'palliate', 'palliating', 'palliation', 'palliative', 'postal', 'preanal', 'precordial', 'real', 'realisation', 'realise', 'realism', 'realist', 'realistic', 'reality', 'realization', 'realize', 'really', 'realness', 'reseal', 'seal', 'sealant', 'sealed', 'sealer', 'sealing', 'senatorial', 'septennial', 'supracostal', 'surreal', 'tegmental', 'textural', 'uncordial', 'underseal', 'undersealed', 'unreal', 'unrealism', 'unrealistic', 'unreality', 'unseal', 'unsealed']

c_conn = sqlite3.connect('main app/corpus/citation_corpus.db')
c_cur = c_conn.cursor()

d_conn = sqlite3.connect('main app/corpus/local_dictionary.db')
d_cur = d_conn.cursor()

dict_data = {}
for w in words:
    d_cur.execute("SELECT definition FROM dictionary_entries WHERE word = ?", (w,))
    rows = d_cur.fetchall()
    dict_data[w] = [r[0] for r in rows]

corpus_quotes = {}
for w in words:
    c_cur.execute("""
        SELECT s.author, s.work, s.sentence
        FROM sentences_fts f
        JOIN sentences s ON f.rowid = s.id
        WHERE sentences_fts MATCH ?
        LIMIT 20
    """, (f'"{w}"',))
    rows = c_cur.fetchall()
    by_auth = {}
    for a, wrk, st in rows:
        if a not in by_auth:
            by_auth[a] = {"work": wrk, "sentence": st}
    corpus_quotes[w] = by_auth

with open("scratch/food_b2_dict.json", "w", encoding="utf-8") as f:
    json.dump(dict_data, f, indent=2)

with open("scratch/food_b2_corpus.json", "w", encoding="utf-8") as f:
    json.dump(corpus_quotes, f, indent=2)

print("Dumped dict & corpus data for all 114 words.")
