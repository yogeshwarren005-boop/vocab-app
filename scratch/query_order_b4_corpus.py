import sqlite3
import json
import re

db_path = r"main app/corpus/citation_corpus.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

def query_words(word_list, output_file):
    results = {}
    found_3 = 0
    for w in word_list:
        clean_w = w.replace('-', ' ')
        query = f'"{clean_w}"'
        try:
            cur.execute("""
                SELECT s.author, s.work, s.sentence 
                FROM sentences_fts f 
                JOIN sentences s ON f.rowid = s.id 
                WHERE f.sentence MATCH ? LIMIT 300
            """, (query,))
            rows = cur.fetchall()
        except Exception as e:
            rows = []

        seen = set()
        dedup = []
        pattern = re.compile(rf'\b{re.escape(clean_w)}\b', re.IGNORECASE)
        for a, wrk, st in rows:
            if a not in seen:
                seen.add(a)
                m = pattern.search(st)
                if m:
                    start, end = m.span()
                    bolded = st[:start] + f"**{st[start:end]}**" + st[end:]
                else:
                    bolded = st
                dedup.append({"author": a, "work": wrk, "sentence": bolded})
        results[w] = dedup
        if len(dedup) >= 3:
            found_3 += 1

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"{output_file}: {len(word_list)} words, {found_3} have >= 3 distinct authors.")

p1_words = ['affinal', 'affine', 'affined', 'affinity', 'confine', 'confined', 'confinement', 'confines', 'confining', 'definable', 'define', 'defined', 'defining', 'definite', 'definitely', 'definiteness', 'definition', 'definitive', 'fin', 'finable', 'finagle', 'finagler', 'final', 'finale', 'finalisation', 'finalise', 'finalist', 'finality', 'finalization', 'finalize', 'finally', 'finance', 'finances', 'financial', 'financially', 'financier', 'financing', 'fincen', 'finch', 'fine', 'fine-grained', 'fine-leafed', 'fine-leaved', 'fine-looking', 'fine-textured', 'fine-tooth', 'fine-toothed', 'fine-tune', 'fineable', 'finedraw', 'finely', 'fineness', 'finer', 'finery', 'finespun', 'finesse']
p2_words = ['finial', 'finical', 'finicky', 'finis', 'finish', 'finished', 'finisher', 'finishing', 'finite', 'finitely', 'finiteness', 'finitude', 'finland', 'finn', 'finnan', 'finnbogadottir', 'finnic', 'finnish', 'finno-ugrian', 'finno-ugric', 'finno-ugric-speaking', 'finocchio', 'indefinable', 'indefinite', 'indefinitely', 'indefiniteness', 'indefinity', 'infinite', 'infinitely', 'infiniteness', 'infinitesimal', 'infinitival', 'infinitive', 'infinitude', 'infinity', 'nonfinancial', 'overrefine', 'overrefined', 'overrefinement', 'redefine', 'redefinition', 'refinance', 'refine', 'refined', 'refinement', 'refiner', 'refinery', 'refining', 'refinish', 'refinisher', 'superfine', 'unconfined', 'undefinable', 'undefined', 'unfinished', 'unrefined']

query_words(p1_words, "scratch/order_b4_p1_corpus.json")
query_words(p2_words, "scratch/order_b4_p2_corpus.json")

conn.close()
