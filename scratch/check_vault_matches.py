import os, json, re

base = r'App database/Latin roots/Cluster Separation & Loosening'
def get_words(folder):
    files = os.listdir(os.path.join(base, folder))
    return {f[:-3].lower() for f in files if f.endswith('.md') and not (f.startswith('Dashboard') or f.startswith('Word Triage') or f.startswith('Cluster') or f.startswith('Semantic Field'))}

div_w = get_words('Dashboard — div')
part_w = get_words('Dashboard — part')
par_w = get_words('Dashboard — par')

all_words = div_w | part_w | par_w
print(f'Total unique words in div, part, par: {len(all_words)}')

vault_root = 'App database/Latin roots'
found_in_vault = {}
for root, dirs, files in os.walk(vault_root):
    if 'Cluster Separation & Loosening' in root or '03_Reference_and_Rules' in root:
        continue
    for f in files:
        if f.endswith('.md'):
            w = f[:-3].lower()
            if w in all_words and w not in found_in_vault:
                found_in_vault[w] = os.path.join(root, f)

print(f'Total candidates found across vault: {len(found_in_vault)}')

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

valid_curated = {}
for w, p in found_in_vault.items():
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # check quotes
    quotes = re.findall(r'> - 📜 \*\*([^*]+)\s+\(\*([^*]+)\*\):\*\*\s+\*\"([^\"]+)\"\*', content)
    if len(quotes) != 3:
        continue
    authors = [q[0].strip() for q in quotes]
    if len(set(authors)) != 3:
        continue
    
    # check bold target
    bold_all = True
    for a, work, qtext in quotes:
        if not re.search(r'\*\*' + re.escape(w) + r'[a-z]*\*\*', qtext, re.IGNORECASE):
            bold_all = False
            break
    if not bold_all:
        continue
    
    if any(bp in content for bp in banned_phrases):
        continue
    
    valid_curated[w] = p

print(f'Valid pristine matches: {len(valid_curated)}')
missing = all_words - set(valid_curated.keys())
print(f'Remaining words needing curation: {len(missing)}')
with open('scratch/separation_rem_needed.json', 'w', encoding='utf-8') as f:
    json.dump(sorted(list(missing)), f, indent=2)
with open('scratch/separation_vault_matches.json', 'w', encoding='utf-8') as f:
    json.dump(valid_curated, f, indent=2)
