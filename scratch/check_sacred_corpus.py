import sqlite3, os

c = sqlite3.connect('main app/corpus/citation_corpus.db')
cur = c.cursor()
cluster_dir = r"App database\Latin roots\Cluster Sacred"
words = []
for d in os.listdir(cluster_dir):
    d_path = os.path.join(cluster_dir, d)
    if os.path.isdir(d_path):
        for f in os.listdir(d_path):
            if f.endswith('.md') and not f.startswith(('Dashboard', 'Word Triage')):
                words.append(f[:-3])

print(f"Total words in Cluster Sacred: {len(words)}")
has_quotes = 0
for w in set(words):
    search_w = w.replace('-', ' ')
    cur.execute('SELECT COUNT(*) FROM sentences_fts WHERE sentence MATCH ?', (f'"{search_w}"',))
    cnt = cur.fetchone()[0]
    if cnt > 0:
        has_quotes += 1

print(f"Words with >= 1 quotes in corpus: {has_quotes}/{len(set(words))}")
