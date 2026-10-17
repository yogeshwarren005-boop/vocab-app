import os, glob, sqlite3, re
from nltk.corpus import wordnet

con = sqlite3.connect("main app/corpus/citation_corpus.db")
cur = con.cursor()

action_files = glob.glob(r"App database\Latin roots\Cluster Action\Dashboard — act\*.md")
print(f"Found {len(action_files)} files in Dashboard — act")

words = [os.path.basename(f).replace('.md', '') for f in action_files]

wordnet_hits = 0
corpus_3_hits = 0
corpus_1_hit = 0
corpus_0_hits = 0

for w in words:
    syns = wordnet.synsets(w.replace('-', '_').lower())
    if syns:
        wordnet_hits += 1
    
    q_word = re.sub(r'[^a-zA-Z0-9]', '', w)
    rows = cur.execute("SELECT COUNT(DISTINCT s.author) FROM sentences_fts f JOIN sentences s ON f.rowid = s.id WHERE sentences_fts MATCH ?", (f'"{q_word}"',)).fetchone()[0]
    if rows >= 3:
        corpus_3_hits += 1
    elif rows >= 1:
        corpus_1_hit += 1
    else:
        corpus_0_hits += 1

print(f"WordNet hits: {wordnet_hits}/{len(words)} ({wordnet_hits/len(words)*100:.1f}%)")
print(f"Corpus >=3 authors: {corpus_3_hits}/{len(words)} ({corpus_3_hits/len(words)*100:.1f}%)")
print(f"Corpus 1-2 authors: {corpus_1_hit}/{len(words)} ({corpus_1_hit/len(words)*100:.1f}%)")
print(f"Corpus 0 authors: {corpus_0_hits}/{len(words)} ({corpus_0_hits/len(words)*100:.1f}%)")
