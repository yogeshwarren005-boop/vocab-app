import sqlite3

vin_words = ['alvine', 'asvina', 'asvins', 'convince', 'convinced', 'convincible', 'convincing', 'convincingly', 'convincingness', 'corvine', 'divination', 'divinatory', 'divine', 'divinely', 'diviner', 'divinity', 'evince', 'invincibility', 'invincible', 'invincibly', 'province', 'provincial', 'provincialism', 'provincially', 'unconvinced', 'unconvincing', 'unconvincingly', 'vinaceous', 'vinaigrette', 'vinca', 'vincetoxicum', 'vincible', 'vincristine', 'vine', 'vinegar', 'vinegariness', 'vinegarish', 'vinegarishness', 'vinegarroon', 'vinegarweed', 'vinegary', 'vinery', 'vineyard', 'viniculture', 'vinifera', 'vinification', 'vinify', 'vino', 'vinogradoff', 'vinology', 'vinous', 'vinson', 'vintage', 'vintager', 'vintner', 'viny', 'vinyl', 'vinylbenzene', 'vinylite']
vor_words = ['aphidivorous', 'carnivore', 'carnivorous', 'detritivore', 'divorce', 'divorced', 'divorcee', 'divorcement', 'equivorous', 'frugivore', 'herbivore', 'herbivorous', 'insectivore', 'insectivorous', 'omnivore', 'omnivorous', 'panivorous', 'phytivorous', 'piscivore', 'piscivorous', 'pupivorous', 'voracious', 'voraciously', 'voraciousness', 'voracity', 'vorarephile', 'vorarephilia', 'vortex', 'vorticella']

all_words = vin_words + vor_words
conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cur = conn.cursor()

found = {}
low = []
for w in all_words:
    clean_w = w.replace('-', ' ')
    try:
        cur.execute('SELECT count(distinct s.author) FROM sentences s JOIN sentences_fts f ON s.id = f.rowid WHERE f.sentence MATCH ?', (f'"{clean_w}"',))
        cnt = cur.fetchone()[0]
        found[w] = cnt
        if cnt < 3:
            low.append((w, cnt))
    except Exception as e:
        low.append((w, str(e)))

print(f"Total: {len(all_words)}")
print(f">=3 authors in DB: {len(all_words) - len(low)}")
print(f"<3 authors in DB: {len(low)}")
for w, c in low:
    print(f"  {w}: {c}")
