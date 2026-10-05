import sqlite3, json, sys

sys.stdout.reconfigure(encoding="utf-8")

words_by_root = {
    'judic': ['adjudicate', 'adjudication', 'adjudicative', 'adjudicator', 'adjudicatory', 'extrajudicial', 'injudicious', 'injudiciously', 'injudiciousness', 'judicable', 'judicatory', 'judicature', 'judicial', 'judicially', 'judiciary', 'judicious', 'judiciously', 'judiciousness', 'prejudice', 'prejudiced', 'prejudicial', 'prejudicious', 'unprejudiced'],
    'juris': ['jurisdiction', 'jurisdictional', 'jurisprudence', 'jurisprudential', 'jurisprudentially', 'jurist', 'juristic'],
    'just': ['adjust', 'adjustable', 'adjusted', 'adjuster', 'adjustive', 'adjustment', 'adjustor', 'injustice', 'just', 'justice', 'justiciar', 'justiciary', 'justifiable', 'justifiably', 'justification', 'justificative', 'justificatory', 'justified', 'justifiedly', 'justifier', 'justify', 'justinian', 'justly', 'justness', 'readjust', 'readjustment', 'unadjustable', 'unadjusted', 'unjust', 'unjustifiable', 'unjustifiably', 'unjustified', 'unjustly', 'unjustness'],
    'legat': ['allegation', 'delegate', 'delegating', 'delegation', 'legate', 'legatee', 'legateship', 'legation', 'legato', 'relegate', 'relegating', 'relegation'],
    'senat': ['arsenate', 'senate', 'senator', 'senatorial', 'senatorship'],
    'statut': ['statute', 'statutorily', 'statutory'],
    'vindic': ['revindicate', 'unvindictive', 'vindicable', 'vindicate', 'vindicated', 'vindication', 'vindicator', 'vindicatory', 'vindictive', 'vindictively', 'vindictiveness']
}

all_words = []
for k, v in words_by_root.items():
    all_words.extend(v)

print('Total words:', len(all_words))
assert len(all_words) == 95

dict_conn = sqlite3.connect('main app/corpus/local_dictionary.db')
dict_cur = dict_conn.cursor()
corpus_conn = sqlite3.connect('main app/corpus/citation_corpus.db')
corpus_cur = corpus_conn.cursor()

results = {}
for w in all_words:
    dict_cur.execute('SELECT source, definition FROM dictionary_entries WHERE word = ? COLLATE NOCASE', (w,))
    defs = dict_cur.fetchall()
    
    search_term = w.replace('-', ' ')
    quotes = []
    try:
        corpus_cur.execute('''
            SELECT s.author, s.work, s.sentence 
            FROM sentences_fts f
            JOIN sentences s ON f.rowid = s.id
            WHERE f.sentence MATCH ? LIMIT 40
        ''', (f'"{search_term}"',))
        quotes = corpus_cur.fetchall()
    except Exception as e:
        pass
    
    distinct_quotes = []
    seen_authors = set()
    for q in quotes:
        auth, work, sent = q[0], q[1], q[2]
        if auth not in seen_authors:
            seen_authors.add(auth)
            distinct_quotes.append({'author': auth, 'work': work, 'sentence': sent})
            
    results[w] = {
        'defs': [{'source': d[0], 'def': d[1]} for d in defs],
        'quotes': distinct_quotes
    }

with open('scratch/law_batch2_raw.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

low_quote_words = [w for w, r in results.items() if len(r['quotes']) < 3]
print('Words with < 3 distinct quotes in citation_corpus:', len(low_quote_words))
print('Low quote words:', low_quote_words)
