import sqlite3
import json

c_conn = sqlite3.connect('main app/corpus/citation_corpus.db')
c_cur = c_conn.cursor()

rog_words = ['abrogate', 'abrogation', 'abrogator', 'acrogen', 'acrogenic', 'acrogenous', 'anterograde', 'arrogance', 'arrogant', 'arrogantly', 'arrogate', 'arrogation', 'arrogator', 'derogate', 'derogation', 'derogative', 'derogatory', 'erogenous', 'interrogate', 'interrogation', 'interrogative', 'interrogatively', 'interrogator', 'interrogatory', 'prerogative', 'prorogation', 'prorogue', 'rogaine', 'rogation', 'rogers', 'roget', 'rogue', 'roguery', 'roguish', 'roguishly', 'roguishness', 'subrogate', 'subrogation', 'supererogatory', 'surrogate']

pris_words = ['apprisal', 'apprise', 'comprise', 'enterprise', 'enterpriser', 'enterprising', 'enterprisingly', 'enterprisingness', 'imprison', 'imprisoned', 'imprisonment', 'nonenterprising', 'priscoan', 'prise', 'prism', 'prismatic', 'prismatoid', 'prismoid', 'prison', 'prison-breaking', 'prisonbreak', 'prisoner', 'prisonlike', 'prissily', 'prissy', 'pristidae', 'pristine', 'pristis', 'reprisal', 'reprise', 'surprisal', 'surprise', 'surprised', 'surprisedly', 'surpriser', 'surprising', 'surprisingly', 'surprisingness', 'unenterprising', 'unimprisoned', 'unsurprised', 'unsurprising']

all_words = rog_words + pris_words

have_3 = []
under_3 = []
results = {}

for w in all_words:
    try:
        c_cur.execute('''
            SELECT s.author, s.work, s.sentence
            FROM sentences_fts f
            JOIN sentences s ON f.rowid = s.id
            WHERE sentences_fts MATCH ?
            LIMIT 50
        ''', (f'"{w}"',))
        rows = c_cur.fetchall()
        seen = set()
        unique = []
        for r in rows:
            if r[0] not in seen and r[0] not in ('Academic Lexicon', 'Classic Author') and len(r[0]) >= 3 and len(r[1]) >= 2:
                seen.add(r[0])
                unique.append({"author": r[0], "work": r[1], "sentence": r[2]})
        results[w] = unique
        if len(unique) >= 3:
            have_3.append((w, len(unique)))
        else:
            under_3.append((w, len(unique)))
    except Exception as e:
        under_3.append((w, str(e)))

print('Words with >= 3 distinct authors in corpus:', len(have_3))
print('Words with < 3 distinct authors in corpus:', len(under_3))
print('Under 3 list:', under_3)

with open('scratch/ask_b2_corpus.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)
