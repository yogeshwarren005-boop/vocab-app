import sqlite3
import re
import json

words = [
    'compost', 'expostulate', 'expostulation', 'impost', 'imposter', 'impostor', 'imposture',
    'post', 'postage', 'postal', 'postcard', 'postcava', 'postcode', 'posted', 'poster',
    'posterboard', 'posterior', 'posteriority', 'posterity', 'postern', 'postexilic',
    'postgraduate', 'posthumous', 'posthumously', 'postiche', 'postictal', 'postilion',
    'postillion', 'postimpressionist', 'postindustrial', 'posting', 'postlude', 'postman',
    'postmark', 'postmaster', 'postmenopausal', 'postmeridian', 'postmillennial', 'postmistress',
    'postmodern', 'postmodernism', 'postmodernist', 'postmortal', 'postmortem', 'postnatal',
    'postnuptial', 'postoperative', 'postoperatively', 'postpone', 'postponement', 'postponer',
    'postscript', 'postulant', 'postulant', 'postulate', 'postulation', 'postulational', 'postulator',
    'postum', 'postural', 'posture', 'posturer', 'posturing', 'preposterous', 'preposterously'
]

conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cur = conn.cursor()

corpus_results = {}
for w in words:
    corpus_results[w] = []
    try:
        cur.execute('SELECT s.author, s.work, s.sentence FROM sentences s JOIN sentences_fts f ON s.id = f.rowid WHERE f.sentence MATCH ? LIMIT 100', (f'"{w}"',))
        rows = cur.fetchall()
        seen = set()
        pattern = re.compile(rf'\b({re.escape(w)}[a-z]*)\b', re.IGNORECASE)
        for auth, work, sent in rows:
            if not auth or 'Classic Author' in auth or 'Academic Lexicon' in auth:
                continue
            if auth in seen:
                continue
            if pattern.search(sent):
                bolded = pattern.sub(r'**\1**', sent)
                corpus_results[w].append({'author': auth, 'work': work, 'quote': bolded})
                seen.add(auth)
                if len(corpus_results[w]) >= 3:
                    break
    except Exception as e:
        pass

with open('scratch/corpus_post_hits.json', 'w', encoding='utf-8') as f:
    json.dump(corpus_results, f, indent=2, ensure_ascii=False)

for w in sorted(set(words)):
    hits = corpus_results.get(w, [])
    print(f"{w}: {len(hits)} hits -> {[q['author'] for q in hits]}")
