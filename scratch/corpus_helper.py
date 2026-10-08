# -*- coding: utf-8 -*-
import sqlite3
import json
import re

def get_corpus_and_dict_data(word_list):
    c_conn = sqlite3.connect("main app/corpus/citation_corpus.db")
    c_cur = c_conn.cursor()
    d_conn = sqlite3.connect("main app/corpus/local_dictionary.db")
    d_cur = d_conn.cursor()

    results = {}
    for word in word_list:
        # dict entries
        d_cur.execute("SELECT definition FROM dictionary_entries WHERE word = ? ORDER BY sense_number ASC", (word,))
        defs = [r[0].strip() for r in d_cur.fetchall()]

        # citations
        # clean punctuation for fts query
        clean_word = re.sub(r'[^a-zA-Z0-9]', '', word)
        quotes = []
        try:
            c_cur.execute('''
                SELECT s.author, s.work, s.sentence
                FROM sentences_fts f
                JOIN sentences s ON f.rowid = s.id
                WHERE sentences_fts MATCH ?
                LIMIT 30
            ''', (f'"{clean_word}"',))
            rows = c_cur.fetchall()
            seen_authors = set()
            for auth, work, sent in rows:
                if auth not in seen_authors:
                    seen_authors.add(auth)
                    quotes.append({"author": auth, "work": work, "sentence": sent})
        except Exception:
            pass

        results[word] = {
            "definitions": defs,
            "quotes": quotes
        }

    c_conn.close()
    d_conn.close()
    return results

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    words = json.load(open("scratch/number_b2_words.json", encoding="utf-8"))[:48]
    data = get_corpus_and_dict_data(words)
    with_quotes = [w for w, v in data.items() if len(v["quotes"]) >= 3]
    partial_quotes = [w for w, v in data.items() if 0 < len(v["quotes"]) < 3]
    no_quotes = [w for w, v in data.items() if len(v["quotes"]) == 0]
    print(f"Words with >=3 authors: {len(with_quotes)}")
    print(f"Words with 1-2 authors: {len(partial_quotes)}")
    print(f"Words with 0 authors: {len(no_quotes)}")
