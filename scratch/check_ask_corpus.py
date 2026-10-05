import sqlite3
import json

c_conn = sqlite3.connect("main app/corpus/citation_corpus.db")
c_cur = c_conn.cursor()

words = [
    # plor (16)
    'deplorable', 'deplorably', 'deplore', 'exploration', 'explorative', 'exploratory', 'explore', 'explorer', 'implore', 'imploring', 'imploringly', 'nonexplorative', 'nonexploratory', 'unexplorative', 'unexploratory', 'unexplored',
    # postul (7)
    'expostulate', 'expostulation', 'postulant', 'postulate', 'postulation', 'postulational', 'postulator',
    # quer (16)
    'conquer', 'conquerable', 'conquering', 'conqueror', 'equerry', 'quercitron', 'quercus', 'querier', 'quern', 'querulous', 'querulously', 'querulousness', 'query', 'reconquer', 'unconquerable', 'unconquered',
    # scit (2)
    'adscititious', 'plebiscite',
    # scrut (9)
    'inscrutability', 'inscrutable', 'inscrutably', 'scrutineer', 'scrutinise', 'scrutinizer', 'scrutinize', 'scrutiniser', 'scrutiny',
    # stud (14)
    'stud', 'student', 'studentship', 'studied', 'studio', 'studious', 'studiously', 'studiousness', 'study', 'studying', 'understudied', 'understudy', 'unstudied', 'unstudious',
    # vestig (8)
    'investigate', 'investigating', 'investigation', 'investigative', 'investigator', 'investigatory', 'vestige', 'vestigial'
]

no_match = []
match_dict = {}

for w in words:
    try:
        c_cur.execute("""
            SELECT s.author, s.work, s.sentence
            FROM sentences_fts f
            JOIN sentences s ON f.rowid = s.id
            WHERE sentences_fts MATCH ?
            LIMIT 40
        """, (f'"{w}"',))
        rows = c_cur.fetchall()
        quotes = [{"author": r[0], "work": r[1], "sentence": r[2]} for r in rows if r[0] not in ('Academic Lexicon', 'Classic Author')]
        
        # Deduplicate by author
        seen = set()
        unique_quotes = []
        for q in quotes:
            if q["author"] not in seen:
                seen.add(q["author"])
                unique_quotes.append(q)
                
        match_dict[w] = unique_quotes
        if len(unique_quotes) < 3:
            no_match.append((w, len(unique_quotes)))
    except Exception as e:
        no_match.append((w, str(e)))

print(f"Total words: {len(words)}")
print(f"Words with < 3 distinct authors in DB: {len(no_match)}")
for w, cnt in no_match:
    print(f"  {w}: {cnt}")

with open("scratch/ask_b1_corpus_matches.json", "w", encoding="utf-8") as f:
    json.dump(match_dict, f, indent=2)
