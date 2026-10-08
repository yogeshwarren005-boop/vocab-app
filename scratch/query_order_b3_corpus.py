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

rect_words = ['correct', 'correctable', 'corrected', 'correction', 'correctional', 'corrections', 'correctitude', 'corrective', 'correctly', 'correctness', 'direct', 'directed', 'directing', 'direction', 'directional', 'directionality', 'directionless', 'directive', 'directiveness', 'directivity', 'directly', 'directness', 'director', 'directorate', 'directorship', 'directory', 'erect', 'erectile', 'erecting', 'erection', 'erectly', 'erectness', 'incorrect', 'incorrectly', 'incorrectness', 'indirect', 'indirection', 'indirectly', 'indirectness', 'insurrection', 'insurrectional', 'insurrectionary', 'insurrectionism', 'insurrectionist', 'misdirect', 'misdirection', 'rectal', 'rectangle', 'rectangular', 'rectangularity', 'rectifiable', 'rectification', 'rectified', 'rectifier', 'rectify', 'rectilineal', 'rectilinear', 'rectitude', 'recto', 'rectocele', 'rectoplasty', 'rector', 'rectorate', 'rectorship', 'rectory', 'rectosigmoid', 'rectum', 'rectus', 'redirect', 'resurrect', 'resurrection', 'subdirectory', 'uncorrectable', 'uncorrected', 'undirected', 'unerect']
medi_words = ['comedian', 'comedienne', 'immediacy', 'immediate', 'immediately', 'immediateness', 'intermediary', 'intermediate', 'intermediately', 'intermediation', 'intermediator', 'irremediable', 'media', 'mediacy', 'mediaeval', 'medial', 'medially', 'median', 'mediant', 'mediastinum', 'mediate', 'mediated', 'mediateness', 'mediation', 'mediator', 'mediatorial', 'mediatory', 'mediatrix', 'medic', 'medicago', 'medicaid', 'medical', 'medically', 'medicament', 'medicare', 'medicate', 'medication', 'medicative', 'medici', 'medicinal', 'medicinally', 'medicine', 'medick', 'medico', 'medicolegal', 'mediety', 'medieval', 'medina', 'medinilla', 'mediocre', 'mediocrity', 'meditate', 'meditation', 'meditative', 'meditatively', 'meditativeness', 'mediterranean', 'medium', 'medium-dry', 'medium-large', 'medium-size', 'medium-sized', 'nonmedicinal', 'premedical', 'premeditate', 'premeditated', 'premeditation', 'remediable', 'remedial', 'remediate', 'remediation', 'submediant', 'unmediated', 'unmedical', 'unmedicative', 'unmedicinal', 'unpremeditated']

query_words(rect_words, "scratch/order_b3_p1_corpus.json")
query_words(medi_words, "scratch/order_b3_p2_corpus.json")

conn.close()
