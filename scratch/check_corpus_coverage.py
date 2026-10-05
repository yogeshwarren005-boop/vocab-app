import sqlite3
import re

cit_words = ['ascites', 'ascitic', 'citadel', 'citation', 'cite', 'citellus', 'citified', 'citify', 'citizen', 'citizenry', 'citizenship', 'citlaltepetl', 'citole', 'citrange', 'citrate', 'citric', 'citrin', 'citrine', 'citron', 'citroncirus', 'citronwood', 'citrous', 'citrulline', 'citrullus', 'citrus', 'cittern', 'city', 'city-born', 'city-bred', 'city-like', 'city-state', 'cityfied', 'cityscape', 'citywide', 'excitability', 'excitable', 'excitableness', 'excitant', 'excitation', 'excitative', 'excitatory', 'excite', 'excited', 'excitedly', 'excitement', 'exciting', 'excitingly', 'incitation', 'incite', 'incitement', 'inciter', 'incitive', 'noncitizen', 'occitan', 'overexcited', 'recital', 'recitalist', 'recitation', 'recitative', 'recite', 'reciter', 'unexcitable', 'unexcited', 'unexciting', 'unexcitingly']
nunci_words = ['annunciate', 'annunciation', 'annunciator', 'annunciatory', 'denunciation', 'denunciative', 'denunciatory', 'enunciate', 'enunciation', 'internuncio', 'mispronunciation', 'nuncio', 'pronunciamento', 'pronunciation', 'renunciant', 'renunciation', 'renunciative']
all_words = cit_words + nunci_words

conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cur = conn.cursor()

found = {}
missing = []
for w in all_words:
    clean_w = w.replace('-', ' ')
    try:
        cur.execute('SELECT count(distinct s.author) FROM sentences s JOIN sentences_fts f ON s.id = f.rowid WHERE f.sentence MATCH ?', (f'"{clean_w}"',))
        cnt = cur.fetchone()[0]
        found[w] = cnt
        if cnt < 3:
            missing.append((w, cnt))
    except Exception as e:
        missing.append((w, str(e)))

print(f"Total words: {len(all_words)}")
print(f"Words with >= 3 distinct authors in corpus db: {len(all_words) - len(missing)}")
print(f"Words with < 3 authors: {len(missing)}")
for m in missing:
    print(" ", m)
