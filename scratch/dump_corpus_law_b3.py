import sqlite3
import json

w_dict = ['addict', 'addicted', 'addiction', 'addictive', 'contradict', 'contradiction', 'contradictorily', 'contradictoriness', 'contradictory', 'dictamnus', 'dictaphone', 'dictate', 'dictated', 'dictation', 'dictator', 'dictatorial', 'dictatorially', 'dictatorship', 'diction', 'dictionary', 'dictostylium', 'dictum', 'dictyophera', 'dictyoptera', 'dictyopteran', 'dictyosome', 'edict', 'indict', 'indictability', 'indictable', 'indiction', 'indictment', 'interdict', 'interdiction', 'nonaddictive', 'predict', 'predictability', 'predictable', 'predictably', 'prediction', 'predictive', 'predictor', 'unaddicted', 'unpredictability', 'unpredictable', 'unpredictably', 'unpredictive']
w_domin = ['abdominal', 'abdominocentesis', 'abdominoplasty', 'abdominous', 'abdominousness', 'abdominovesical', 'condominium', 'dominance', 'dominant', 'dominate', 'dominated', 'dominating', 'domination', 'dominatrix', 'domine', 'dominee', 'domineer', 'domineering', 'domineeringly', 'domineeringness', 'dominic', 'dominica', 'dominical', 'dominican', 'dominick', 'dominicus', 'dominie', 'dominion', 'dominique', 'domino', 'dominoes', 'dominos', 'dominus', 'predominance', 'predominant', 'predominantly', 'predominate', 'predomination', 'subdominant']

conn = sqlite3.connect("main app/corpus/citation_corpus.db")
cur = conn.cursor()

corpus_data = {}
for w in w_dict + w_domin:
    cur.execute("""
        SELECT distinct s.author, s.work, s.sentence
        FROM sentences_fts f
        JOIN sentences s ON f.rowid = s.id
        WHERE sentences_fts MATCH ?
    """, (f'"{w}"',))
    rows = cur.fetchall()
    by_auth = {}
    for a, wk, sent in rows:
        if a not in by_auth:
            by_auth[a] = {"work": wk, "sentence": sent}
    corpus_data[w] = by_auth

print(f"Total words: {len(corpus_data)}")
available_3 = {w: data for w, data in corpus_data.items() if len(data) >= 3}
print(f"Words with >= 3 distinct authors: {len(available_3)}")
for w in sorted(available_3.keys()):
    print(f"  {w}: {len(available_3[w])} authors -> {list(available_3[w].keys())[:4]}")

with open("scratch/corpus_law_b3_matches.json", "w", encoding="utf-8") as f:
    json.dump(corpus_data, f, ensure_ascii=False, indent=2)

conn.close()
