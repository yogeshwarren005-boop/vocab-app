import os
import re
import sqlite3

base_dir = r'App database/Latin roots/Cluster Thought'
dashboards = ['Dashboard — cern', 'Dashboard — cogit', 'Dashboard — estim', 'Dashboard — opin', 'Dashboard — scrup']

corpus_conn = sqlite3.connect(r'main app/corpus/citation_corpus.db')
corpus_cur = corpus_conn.cursor()

dict_conn = sqlite3.connect(r'main app/corpus/local_dictionary.db')
dict_cur = dict_conn.cursor()

def search_corpus(word):
    # Try exact match first
    corpus_cur.execute('''
        SELECT s.author, s.work, s.sentence 
        FROM sentences s 
        JOIN sentences_fts f ON s.id = f.rowid 
        WHERE sentences_fts MATCH ? 
        LIMIT 30
    ''', (f'"{word}"',))
    res = corpus_cur.fetchall()
    return res

words_data = {}
for d in dashboards:
    p = os.path.join(base_dir, d)
    files = sorted([f for f in os.listdir(p) if f.endswith('.md') and not f.startswith('Dashboard —') and not f.startswith('Word Triage —')])
    for f in files:
        w = f[:-3].lower()
        file_path = os.path.join(p, f)
        with open(file_path, 'r', encoding='utf-8') as fin:
            content = fin.read()
        
        # Existing quotes in file
        existing_quotes = []
        for line in content.splitlines():
            line = line.strip()
            if line.startswith('>') and '📜' in line:
                m = re.search(r'📜\s*\*\*([^*]+?)\s*(?:\(\*([^*]+?)\*\):?\*\*|\*\*\s*\(\*([^*]+?)\*\):?)\s*(.+)$', line)
                if m:
                    author = m.group(1).strip()
                    work = (m.group(2) or m.group(3) or '').strip()
                    quote = m.group(4).strip()
                    existing_quotes.append({'author': author, 'work': work, 'quote': quote})
        
        # Dictionary definitions
        dict_cur.execute('SELECT source, definition FROM dictionary_entries WHERE word = ? ORDER BY sense_number', (w,))
        dict_defs = [row[1] for row in dict_cur.fetchall()]

        # Corpus quotes
        corpus_quotes = search_corpus(w)

        words_data[w] = {
            'dashboard': d,
            'existing_quotes': existing_quotes,
            'dict_defs': dict_defs,
            'corpus_quotes_count': len(corpus_quotes)
        }

for w, info in words_data.items():
    print(f"{w} ({info['dashboard']}): {len(info['existing_quotes'])} existing quotes | {info['corpus_quotes_count']} corpus matches | {len(info['dict_defs'])} dict defs")
