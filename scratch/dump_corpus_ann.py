import sqlite3
import json

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

corpus_results = {}
for w in words:
    # search directly
    query = f'"{w}"'
    try:
        rows = c.execute('SELECT author, work, sentence FROM sentences_fts WHERE sentence MATCH ? LIMIT 30', (query,)).fetchall()
    except Exception as e:
        rows = c.execute('SELECT author, work, sentence FROM sentences WHERE sentence LIKE ? LIMIT 30', (f'%{w}%',)).fetchall()
    
    valid = []
    seen = set()
    for auth, work, s in rows:
        auth = auth.strip()
        work = work.strip()
        s = s.strip()
        if auth and auth not in seen and len(s) > 25:
            # check if w or inflected form is in s
            valid.append({'author': auth, 'work': work, 'sentence': s})
            seen.add(auth)
    corpus_results[w] = valid

with open('scratch/corpus_ann_results.json', 'w', encoding='utf-8') as f:
    json.dump(corpus_results, f, ensure_ascii=False, indent=2)

print("Dumped corpus results for ann words.")
