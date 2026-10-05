import sqlite3

words = [
    'anna', 'annaba', 'annalist', 'annalistic', 'annals', 'annam', 'annamese', 'annamite',
    'annapolis', 'annapurna', 'anne', 'anneal', 'annealing', 'annelid', 'annelida', 'annelidan',
    'annex', 'annexa', 'annexal', 'annexation', 'annexational', 'annexe', 'anniellidae',
    'annihilate', 'annihilated', 'annihilating', 'annihilation', 'annihilative', 'annihilator',
    'anniversary', 'annon', 'annona', 'annonaceae', 'annotate', 'annotating', 'annotation',
    'annotator', 'announce', 'announced', 'announcement', 'announcer', 'annoy', 'annoyance',
    'annoyed', 'annoyer', 'annoying', 'annoyingly', 'annual', 'annually', 'annualry',
    'annuitant', 'annuity', 'annul', 'annular', 'annulate', 'annulated', 'annulet',
    'annulment', 'annulus', 'annum', 'annunciate', 'annunciation', 'annunciator',
    'annunciatory', 'inanna', 'per annum', 'semiannual', 'semiannually', 'superannuate',
    'superannuated', 'superannuation', 'susanna', 'unannealed', 'unannounced'
]

conn = sqlite3.connect('main app/corpus/citation_corpus.db')
c = conn.cursor()

found = {}
missing = []

for w in words:
    query = f'"{w}"'
    try:
        rows = c.execute('SELECT author, work, sentence FROM sentences_fts WHERE sentence MATCH ? LIMIT 20', (query,)).fetchall()
    except Exception as e:
        rows = c.execute('SELECT author, work, sentence FROM sentences WHERE sentence LIKE ? LIMIT 20', (f'%{w}%',)).fetchall()
    
    valid = []
    seen_auth = set()
    for auth, work, sent in rows:
        auth_clean = auth.strip()
        if auth_clean and auth_clean not in seen_auth and len(sent) > 20:
            valid.append((auth_clean, work.strip(), sent.strip()))
            seen_auth.add(auth_clean)
    found[w] = len(valid)
    if len(valid) < 3:
        missing.append((w, len(valid)))

print(f"Total words: {len(words)}")
print(f"Words with >= 3 quotes in corpus: {len(words) - len(missing)}")
print(f"Words with < 3 quotes in corpus: {len(missing)}")
for w, cnt in missing:
    print(f"  {w}: {cnt}")
