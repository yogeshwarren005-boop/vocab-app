import sqlite3

words = ['agal', 'al', 'alacritous', 'alacrity', 'albedo', 'albescent', 'albite', 'albitic', 'alible', 'aliment', 'alimentary', 'alimentation', 'alimentative', 'alimony', 'allocution', 'anal', 'animal', 'animalise', 'animalism', 'animalistic', 'animality', 'animalize', 'anticlerical', 'archival', 'auroral', 'bifocals', 'caldera', 'calor', 'cataloger', 'catalogue', 'cataloguer', 'coal', 'coalesce', 'coalesced', 'coalescence', 'coalescency', 'coalescent', 'coalescing', 'coalition', 'colloquialism', 'comal', 'comical', 'comicality', 'comically', 'contextual', 'contextualism', 'contextually', 'coral', 'cordial', 'cordiality', 'cordially', 'coxalgic', 'craniofacial', 'criminal', 'criminalise', 'criminalism', 'criminality', 'criminalize', 'criminally', 'criminalness', 'deal', 'dealer', 'dealership', 'dealing', 'dealings', 'decriminalise', 'decriminalize', 'dial', 'irreality', 'misdeal', 'opal', 'opalise', 'opalize', 'orally', 'oratorical', 'palliate', 'palliating', 'palliation', 'palliative', 'postal', 'preanal', 'precordial', 'real', 'realisation', 'realise', 'realism', 'realist', 'realistic', 'reality', 'realization', 'realize', 'really', 'realness', 'reseal', 'seal', 'sealant', 'sealed', 'sealer', 'sealing', 'senatorial', 'septennial', 'supracostal', 'surreal', 'tegmental', 'textural', 'uncordial', 'underseal', 'undersealed', 'unreal', 'unrealism', 'unrealistic', 'unreality', 'unseal', 'unsealed']

c_conn = sqlite3.connect('main app/corpus/citation_corpus.db')
c_cur = c_conn.cursor()

d_conn = sqlite3.connect('main app/corpus/local_dictionary.db')
d_cur = d_conn.cursor()

print(f"Total words: {len(words)}")

corpus_counts = {}
for w in words:
    c_cur.execute('''
        SELECT count(distinct s.author)
        FROM sentences_fts f
        JOIN sentences s ON f.rowid = s.id
        WHERE sentences_fts MATCH ?
    ''', (f'"{w}"',))
    cnt = c_cur.fetchone()[0]
    corpus_counts[w] = cnt

low_corpus = [w for w, c in corpus_counts.items() if c < 3]
print(f"Words with < 3 distinct authors in corpus: {len(low_corpus)}")
print(low_corpus)
