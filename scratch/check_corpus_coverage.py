import sqlite3

w_dict = ['addict', 'addicted', 'addiction', 'addictive', 'contradict', 'contradiction', 'contradictorily', 'contradictoriness', 'contradictory', 'dictamnus', 'dictaphone', 'dictate', 'dictated', 'dictation', 'dictator', 'dictatorial', 'dictatorially', 'dictatorship', 'diction', 'dictionary', 'dictostylium', 'dictum', 'dictyophera', 'dictyoptera', 'dictyopteran', 'dictyosome', 'edict', 'indict', 'indictability', 'indictable', 'indiction', 'indictment', 'interdict', 'interdiction', 'nonaddictive', 'predict', 'predictability', 'predictable', 'predictably', 'prediction', 'predictive', 'predictor', 'unaddicted', 'unpredictability', 'unpredictable', 'unpredictably', 'unpredictive']
w_domin = ['abdominal', 'abdominocentesis', 'abdominoplasty', 'abdominous', 'abdominousness', 'abdominovesical', 'condominium', 'dominance', 'dominant', 'dominate', 'dominated', 'dominating', 'domination', 'dominatrix', 'domine', 'dominee', 'domineer', 'domineering', 'domineeringly', 'domineeringness', 'dominic', 'dominica', 'dominical', 'dominican', 'dominick', 'dominicus', 'dominie', 'dominion', 'dominique', 'domino', 'dominoes', 'dominos', 'dominus', 'predominance', 'predominant', 'predominantly', 'predominate', 'predomination', 'subdominant']

all_words = w_dict + w_domin
conn = sqlite3.connect("main app/corpus/citation_corpus.db")
cur = conn.cursor()

found = {}
for w in all_words:
    cur.execute("""
        SELECT count(distinct s.author)
        FROM sentences_fts f
        JOIN sentences s ON f.rowid = s.id
        WHERE sentences_fts MATCH ?
    """, (f'"{w}"',))
    cnt = cur.fetchone()[0]
    found[w] = cnt

low = {k: v for k, v in found.items() if v < 3}
print(f"Total words: {len(all_words)}")
print(f"Words with >= 3 distinct authors in corpus: {len(all_words) - len(low)}")
print(f"Words with < 3 authors in corpus: {len(low)}")
for k, v in sorted(low.items(), key=lambda x: x[1]):
    print(f"  {k}: {v} distinct authors")
conn.close()
