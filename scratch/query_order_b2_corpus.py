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

sequ_words = ['consequence', 'consequent', 'consequential', 'consequentially', 'consequently', 'disequilibrium', 'inconsequence', 'inconsequent', 'inconsequential', 'inconsequentially', 'inconsequently', 'non sequitur', 'obsequious', 'obsequiously', 'obsequiousness', 'sequel', 'sequela', 'sequella', 'sequenator', 'sequence', 'sequencer', 'sequent', 'sequential', 'sequentially', 'sequester', 'sequestered', 'sequestrate', 'sequestration', 'sequin', 'sequined', 'sequoia', 'sequoiadendron', 'sequoya', 'sequoyah', 'subsequence', 'subsequent', 'subsequently', 'subsequentness']
termin_words = ['conterminous', 'coterminous', 'coterminously', 'determinable', 'determinant', 'determinate', 'determinateness', 'determination', 'determinative', 'determine', 'determined', 'determinedly', 'determiner', 'determining', 'determinism', 'determinist', 'deterministic', 'exterminable', 'exterminate', 'exterminated', 'extermination', 'exterminator', 'indeterminable', 'indeterminate', 'indeterminateness', 'indetermination', 'inexterminable', 'interminable', 'interminably', 'predetermination', 'predetermine', 'predetermined', 'redetermination', 'redetermine', 'subterminal', 'terminable', 'terminal', 'terminally', 'terminate', 'terminated', 'termination', 'terminative', 'terminator', 'terminological', 'terminology', 'terminus', 'undeterminable', 'undetermined']
ord_words = ['bipolar disorder', 'coordinate', 'coordinated', 'coordinately', 'coordinating', 'coordination', 'coordinative', 'coordinator', 'disorder', 'disordered', 'disorderliness', 'disorderly', 'exordium', 'extraordinaire', 'extraordinarily', 'extraordinariness', 'extraordinary', 'incoordination', 'inordinate', 'inordinately', 'inordinateness', 'insubordinate', 'insubordination', 'ordain', 'ordained', 'ordainer', 'ordeal', 'order', 'order-chenopodiales', 'ordered', 'orderer', 'ordering', 'orderliness', 'orderly', 'ordinal', 'ordinance', 'ordinand', 'ordinarily', 'ordinariness', 'ordinary', 'ordinate', 'ordination', 'ordnance', 'ordovician', 'ordure', 'preordain', 'preordained', 'preordination', 'reorder', 'reordering', 'suborder', 'subordinate', 'subordinateness', 'subordinating', 'subordination', 'subordinative', 'superorder', 'superordinate', 'superordination', 'uncoordinated', 'unordered']

query_words(sequ_words + termin_words, "scratch/order_b2_p1_corpus.json")
query_words(ord_words, "scratch/order_b2_p2_corpus.json")

conn.close()
