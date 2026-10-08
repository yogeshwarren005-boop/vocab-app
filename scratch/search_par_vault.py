import os, sys, json, re

with open('scratch/par_still_needed.json', 'r', encoding='utf-8') as f:
    needed = set(json.load(f))

vault_root = 'App database/Latin roots'
found_more = {}
for root, dirs, files in os.walk(vault_root):
    if 'Cluster Separation & Loosening' in root or '03_Reference_and_Rules' in root:
        continue
    for f in files:
        if f.endswith('.md'):
            w = f[:-3].lower()
            if w in needed and w not in found_more:
                found_more[w] = os.path.join(root, f)

print(f'Found {len(found_more)} candidates in vault')

banned_phrases = [
    'In specialized and domain usage, denoting specific qualities',
    'In technical and systematic terminology, the action',
    'In functional and operational contexts, an agent',
    'The clinical presentation of',
    'Every pathological manifestation of',
    'The gradual evolutionary modification of',
    'In academic literature,',
    'Academic Lexicon',
    'Classic Author'
]

valid_more = {}
for w, p in found_more.items():
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    quotes = re.findall(r'> - 📜 \*\*([^*]+)\s+\(\*([^*]+)\*\):\*\*\s+\*\"([^\"]+)\"\*', c)
    if len(quotes) != 3:
        continue
    authors = [q[0].strip() for q in quotes]
    if len(set(authors)) != 3:
        continue
    bold_all = True
    for a, work, qtext in quotes:
        if not re.search(r'\*\*' + re.escape(w) + r'[a-z]*\*\*', qtext, re.IGNORECASE):
            bold_all = False
            break
    if not bold_all:
        continue
    if any(bp in c for bp in banned_phrases):
        continue
    valid_more[w] = p

print(f'Valid pristine in vault: {len(valid_more)}')
still_needed_after = needed - set(valid_more.keys())
print(f'Truly needed after vault search: {len(still_needed_after)}')

with open('scratch/par_vault_more.json', 'w', encoding='utf-8') as f:
    json.dump(valid_more, f, indent=2)
with open('scratch/par_final_needed.json', 'w', encoding='utf-8') as f:
    json.dump(sorted(list(still_needed_after)), f, indent=2)
