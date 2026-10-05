import sqlite3
import sys

dur_words = ['corduroy', 'corduroys', 'dura', 'durability', 'durable', 'durables', 'durabolin', 'dural', 'duralumin', 'duramen', 'durance', 'durango', 'durant', 'durante', 'duration', 'durative', 'durazzo', 'durer', 'duress', 'durian', 'during', 'durio', 'durion', 'durmast', 'durra', 'durrell', 'durres', 'durum', 'endurable', 'endurance', 'endure', 'enduring', 'enduringly', 'enduringness', 'extradural', 'indurate', 'induration', 'obduracy', 'obdurate', 'obdurately', 'perdurability', 'perdurable', 'subdural', 'unendurable']
prim_words = ['imprimatur', 'prim', 'prima', 'prima donna', 'primacy', 'primaeval', 'primal', 'primality', 'primaquine', 'primarily', 'primary', 'primate', 'primates', 'primateship', 'primatology', 'primaxin', 'prime', 'primed', 'primer', 'primeval', 'primidone', 'primigravida', 'priming', 'primipara', 'primiparous', 'primitive', 'primitively', 'primitiveness', 'primitivism', 'primly', 'primness', 'primo', 'primogenitor', 'primogeniture', 'primordial', 'primordium', 'primrose', 'primula', 'primulaceae', 'primulales', 'primus', 'reprimand']

conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cur = conn.cursor()

low_hit_words = []
for w in dur_words + prim_words:
    try:
        cur.execute('SELECT COUNT(DISTINCT s.author) FROM sentences s JOIN sentences_fts f ON s.id = f.rowid WHERE f.sentence MATCH ?', (f'"{w}"',))
        cnt = cur.fetchone()[0]
        if cnt < 3:
            low_hit_words.append((w, cnt))
    except Exception as e:
        low_hit_words.append((w, str(e)))

print(f"Total words: {len(dur_words + prim_words)}")
print(f"Total low hits (<3 distinct authors): {len(low_hit_words)}")
for w, cnt in low_hit_words:
    print(f"  {w}: {cnt}")
