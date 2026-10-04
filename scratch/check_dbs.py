import os
import sqlite3
import json

dict_conn = sqlite3.connect('main app/corpus/local_dictionary.db')
print("Dictionary tables:", dict_conn.execute("SELECT name, sql FROM sqlite_master WHERE type='table'").fetchall())

corpus_conn = sqlite3.connect('main app/corpus/citation_corpus.db')
print("Corpus tables:", corpus_conn.execute("SELECT name, sql FROM sqlite_master WHERE type='table'").fetchall())
