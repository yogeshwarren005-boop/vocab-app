import sqlite3

def query_words(word_list):
    conn = sqlite3.connect('main app/corpus/citation_corpus.db')
    cur = conn.cursor()
    for w in word_list:
        clean = w.replace('-', ' ')
        try:
            cur.execute('SELECT distinct s.author, s.work, s.sentence FROM sentences s JOIN sentences_fts f ON s.id = f.rowid WHERE f.sentence MATCH ? LIMIT 8', (f'"{clean}"',))
            rows = cur.fetchall()
            print(f"=== {w} ({len(rows)} hits) ===")
            for a, wk, sen in rows[:3]:
                print(f"  {a} | {wk} | {sen[:120]}")
        except Exception as e:
            print(f"=== {w} (ERROR: {e}) ===")

if __name__ == "__main__":
    words_vor = ['aphidivorous', 'carnivore', 'carnivorous', 'detritivore', 'divorce', 'divorced', 'divorcee', 'divorcement', 'equivorous', 'frugivore', 'herbivore', 'herbivorous', 'insectivore', 'insectivorous', 'omnivore', 'omnivorous', 'panivorous', 'phytivorous', 'piscivore', 'piscivorous', 'pupivorous', 'voracious', 'voraciously', 'voraciousness', 'voracity', 'vorarephile', 'vorarephilia', 'vortex', 'vorticella']
    query_words(words_vor)
