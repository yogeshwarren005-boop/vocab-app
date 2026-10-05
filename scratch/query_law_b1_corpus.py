import sqlite3
import json

conn = sqlite3.connect('main app/corpus/citation_corpus.db')
c = conn.cursor()

words = [
    # arbitr (18)
    'arbitrable', 'arbitrage', 'arbitrager', 'arbitrageur', 'arbitral', 'arbitrament', 'arbitrarily', 'arbitrariness', 'arbitrary', 'arbitrate', 'arbitration', 'arbitrational', 'arbitrative', 'arbitrator', 'arbitrement', 'nonarbitrable', 'nonarbitrary', 'unarbitrary',
    # crim (46)
    'crime', 'crimea', 'criminal', 'criminalisation', 'criminalise', 'criminalism', 'criminality', 'criminalization', 'criminalize', 'criminally', 'criminalness', 'criminate', 'criminative', 'criminatory', 'criminological', 'criminologist', 'criminology', 'crimson', 'crimson-magenta', 'crimson-purple', 'crimson-yellow', 'decriminalisation', 'decriminalise', 'decriminalization', 'decriminalize', 'discriminable', 'discriminate', 'discriminating', 'discrimination', 'discriminative', 'discriminator', 'discriminatory', 'encrimson', 'incriminate', 'incriminating', 'incriminatingly', 'incrimination', 'incriminatory', 'indiscriminate', 'indiscriminately', 'indiscriminating', 'recriminate', 'recrimination', 'recriminative', 'recriminatory', 'undiscriminating',
    # damn (8)
    'damn', 'damnable', 'damnably', 'damnation', 'damnatory', 'damned', 'damnify', 'damning',
    # fisc (5)
    'confiscate', 'confiscation', 'fisc', 'fiscal', 'fiscally'
]

print(f"Total target words: {len(words)}")

corpus_hits = {}
for w in words:
    term = w.replace('-', ' ')
    search_q = f'"{term}"'
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
        if auth not in by_author and 30 < len(sent) < 400:
            by_author[auth] = {'work': work, 'sentence': sent}
    corpus_hits[w] = by_author

with open('scratch/corpus_hits_law_b1.json', 'w', encoding='utf-8') as f:
    json.dump(corpus_hits, f, ensure_ascii=False, indent=2)

counts = {w: len(corpus_hits[w]) for w in words}
print(f"Words with >= 3 distinct authors in corpus: {sum(1 for c in counts.values() if c >= 3)} / {len(words)}")
need_quotes = [w for w, count in counts.items() if count < 3]
print(f"Words with < 3 authors in corpus ({len(need_quotes)}):")
for w in need_quotes:
    print(f"  {w:20}: {counts[w]} authors")
