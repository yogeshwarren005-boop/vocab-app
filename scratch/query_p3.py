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
    words_p3 = ['vinegary', 'vinery', 'vineyard', 'viniculture', 'vinifera', 'vinification', 'vinify', 'vino', 'vinogradoff', 'vinology', 'vinous', 'vinson', 'vintage', 'vintager', 'vintner', 'viny', 'vinyl', 'vinylbenzene', 'vinylite']
    query_words(words_p3)
