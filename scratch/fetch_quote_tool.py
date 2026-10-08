# -*- coding: utf-8 -*-
import sqlite3
import json

conn = sqlite3.connect("main app/corpus/citation_corpus.db")
cur = conn.cursor()

def get_sentences(word, limit=5):
    cur.execute("""
        SELECT s.author, s.work, s.sentence 
        FROM sentences_fts f 
        JOIN sentences s ON f.rowid = s.id 
        WHERE f.sentence MATCH ? LIMIT ?
    """, (f'"{word}"', limit))
    return cur.fetchall()

if __name__ == "__main__":
    for word in ['visible', 'vision', 'visionary', 'visit', 'visitant', 'visitation', 'visiting', 'visitor', 'visor', 'vista', 'visual']:
        rows = get_sentences(word, 2)
        print(f"=== {word} ===")
        for r in rows:
            print(f"[{r[0]}] ({r[1]}): {r[2][:120]}")
