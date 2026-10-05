import sqlite3
import re

dur_words = ['corduroy', 'corduroys', 'dura', 'durability', 'durable', 'durables', 'durabolin', 'dural', 'duralumin', 'duramen', 'durance', 'durango', 'durant', 'durante', 'duration', 'durative', 'durazzo', 'durer', 'duress', 'durian', 'during', 'durio', 'durion', 'durmast', 'durra', 'durrell', 'durres', 'durum', 'endurable', 'endurance', 'endure', 'enduring', 'enduringly', 'enduringness', 'extradural', 'indurate', 'induration', 'obduracy', 'obdurate', 'obdurately', 'perdurability', 'perdurable', 'subdural', 'unendurable']
prim_words = ['imprimatur', 'prim', 'prima', 'prima donna', 'primacy', 'primaeval', 'primal', 'primality', 'primaquine', 'primarily', 'primary', 'primate', 'primates', 'primateship', 'primatology', 'primaxin', 'prime', 'primed', 'primer', 'primeval', 'primidone', 'primigravida', 'priming', 'primipara', 'primiparous', 'primitive', 'primitively', 'primitiveness', 'primitivism', 'primly', 'primness', 'primo', 'primogenitor', 'primogeniture', 'primordial', 'primordium', 'primrose', 'primula', 'primulaceae', 'primulales', 'primus', 'reprimand']

conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cur = conn.cursor()

corpus_data = {}

for w in dur_words + prim_words:
    corpus_data[w] = []
    # Try exact match first
    try:
        cur.execute('SELECT s.author, s.work, s.sentence FROM sentences s JOIN sentences_fts f ON s.id = f.rowid WHERE f.sentence MATCH ? LIMIT 50', (f'"{w}"',))
        rows = cur.fetchall()
        seen_authors = set()
        for auth, work, sent in rows:
            if not auth or auth == "Classic Author" or auth == "Academic Lexicon":
                continue
            if auth in seen_authors:
                continue
            # check if w or w's root is in sent
            # bold the word in sent
            pattern = re.compile(rf'\b({re.escape(w)}[a-z]*)\b', re.IGNORECASE)
            if pattern.search(sent):
                bolded = pattern.sub(r'**\1**', sent)
                corpus_data[w].append({"author": auth, "work": work, "quote": bolded})
                seen_authors.add(auth)
                if len(corpus_data[w]) >= 3:
                    break
    except Exception as e:
        pass

has_3 = [w for w, q in corpus_data.items() if len(q) >= 3]
has_1_2 = [w for w, q in corpus_data.items() if 1 <= len(q) < 3]
has_0 = [w for w, q in corpus_data.items() if len(q) == 0]

print(f"Has 3 corpus quotes: {len(has_3)} -> {has_3}")
print(f"Has 1-2 corpus quotes: {len(has_1_2)} -> {has_1_2}")
print(f"Has 0 corpus quotes: {len(has_0)} -> {has_0}")
