import glob, os, sqlite3, re

con_dict = sqlite3.connect('main app/corpus/local_dictionary.db')
cur_dict = con_dict.cursor()

con_corp = sqlite3.connect('main app/corpus/citation_corpus.db')
cur_corp = con_corp.cursor()

files = glob.glob(r'App database\Latin roots\Cluster Action\Dashboard — act\*.md')
words = []
for f in files:
    name = os.path.basename(f)
    if not name.startswith('Dashboard') and not name.startswith('Word Triage'):
        words.append(name.replace('.md', ''))

print(f"Total words in Dashboard — act: {len(words)}")

has_def1 = 0
has_def2 = 0
has_corp_3 = 0
has_corp_1_2 = 0
has_corp_0 = 0

needs_citations = []
needs_definitions = []

for w in words:
    # 1. Definitions
    clean_w = w.lower().strip()
    defs = cur_dict.execute("SELECT source, definition FROM dictionary_entries WHERE word = ?", (clean_w,)).fetchall()
    if not defs:
        # try without hyphen
        defs = cur_dict.execute("SELECT source, definition FROM dictionary_entries WHERE word = ?", (clean_w.replace('-', ' '),)).fetchall()
    if not defs:
        # try singular
        if clean_w.endswith('s') and len(clean_w) > 3:
            defs = cur_dict.execute("SELECT source, definition FROM dictionary_entries WHERE word = ?", (clean_w[:-1],)).fetchall()
            
    if defs:
        has_def1 += 1
        if len(defs) >= 2:
            has_def2 += 1
    else:
        needs_definitions.append(w)
        
    # 2. Citations
    q_word = re.sub(r'[^a-zA-Z0-9]', '', clean_w)
    pat = re.compile(rf'\b({re.escape(clean_w)})\b', re.IGNORECASE)
    auths = []
    if q_word:
        rows = cur_corp.execute("""
            SELECT s.author, s.work, s.sentence
            FROM sentences_fts f
            JOIN sentences s ON f.rowid = s.id
            WHERE sentences_fts MATCH ?
            LIMIT 100
        """, (f'"{q_word}"',)).fetchall()
        
        seen_auths = set()
        for a, work, sent in rows:
            if a not in seen_auths and pat.search(sent) and 35 <= len(sent) <= 400:
                seen_auths.add(a)
                auths.append((a, work, sent))
                if len(auths) >= 3:
                    break
                    
    if len(auths) >= 3:
        has_corp_3 += 1
    elif len(auths) > 0:
        has_corp_1_2 += 1
        needs_citations.append((w, len(auths)))
    else:
        has_corp_0 += 1
        needs_citations.append((w, 0))

print("\n--- Summary ---")
print(f"Words with >= 1 definition in local_dictionary: {has_def1}/{len(words)}")
print(f"Words with >= 2 definitions in local_dictionary: {has_def2}/{len(words)}")
print(f"Words needing definition lookups (MCP/CRW): {len(needs_definitions)}")
print(f"Words with >= 3 corpus authors: {has_corp_3}/{len(words)}")
print(f"Words with 1-2 corpus authors: {has_corp_1_2}/{len(words)}")
print(f"Words with 0 corpus authors: {has_corp_0}/{len(words)}")
print(f"Words needing citation lookups (MCP/CRW): {len(needs_citations)}")

if needs_definitions:
    print(f"\nSample words needing definitions: {needs_definitions[:10]}")
