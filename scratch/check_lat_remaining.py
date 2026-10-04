import sqlite3, json, sys

words = [
  'dilatation', 'interrelatedness', 'oblateness', 'oblation', 'prelate', 'prelature', 'prolate', 'relate', 'related', 'relatedness', 'relatiative', 'relation', 'relational', 'relations', 'relationship', 'relative-in-law', 'relative', 'relatively', 'relativise', 'relativism', 'relativistic', 'relativistically', 'relativity', 'relativize', 'relatum', 'retranslate', 'superlative', 'superlatively', 'tralatitious', 'translatable', 'translate', 'translation', 'translational', 'translator', 'uncorrelated', 'unlatched', 'unrelated', 'unrelatedness', 'untranslatable'
]

dict_db = sqlite3.connect('main app/corpus/local_dictionary.db')
dict_cur = dict_db.cursor()

corpus_db = sqlite3.connect('main app/corpus/citation_corpus.db')
corpus_cur = corpus_db.cursor()

missing_sentences = []
for w in words:
    dict_cur.execute('SELECT definition FROM definitions WHERE word = ?', (w,))
    defs = [r[0] for r in dict_cur.fetchall()]
    
    clean_w = w.replace('-', ' ')
    corpus_cur.execute('SELECT author, work, sentence FROM sentences_fts WHERE sentence MATCH ? LIMIT 10', (f'"{clean_w}"',))
    sents = corpus_cur.fetchall()
    print(f'{w}: {len(defs)} defs, {len(sents)} sentences')
    if len(sents) < 3:
        missing_sentences.append(w)

print('Words with < 3 sentences:', missing_sentences)
