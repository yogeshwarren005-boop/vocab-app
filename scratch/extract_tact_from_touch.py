import os, re, json

tact_dir = 'App database/Latin roots/Cluster Touch/Dashboard — tact'
files = [f for f in os.listdir(tact_dir) if f.endswith('.md') and not f.startswith(('Dashboard', 'Word'))]
tact_data = {}
for f in sorted(files):
    w = f[:-3].lower()
    with open(os.path.join(tact_dir, f), 'r', encoding='utf-8') as fp:
        c = fp.read()
    pMatch = re.search(r'1\.\s*\*\*([^*]+)\*\*:\s*([^\r\n]+)', c)
    sMatch = re.search(r'2\.\s*\*\*([^*]+)\*\*:\s*([^\r\n]+)', c)
    qSection = c.split('> [!quote]')[1] if '> [!quote]' in c else ''
    qLines = [l.strip() for l in qSection.split('\n') if l.strip().startswith('>') and '📜' in l]
    quotes = []
    for q in qLines:
        colon_idx = q.find(':**')
        if colon_idx != -1:
            header = q[:colon_idx+3]
            body = q[colon_idx+3:].strip()
            m = re.search(r'📜\s*\*\*([^*]+?)\s*(?:\(\*([^*]+?)\*\):?\*\*|\*\*\s*\(\*([^*]+?)\*\):?)', header)
            q_clean = body.strip('*').strip('"').strip()
            if m:
                quotes.append({'author': m.group(1).strip(), 'work': (m.group(2) or m.group(3)).strip(), 'quote': q_clean})
    tact_data[w] = {
        'primary': pMatch.group(2).strip() if pMatch else '',
        'secondary': sMatch.group(2).strip() if sMatch else '',
        'quotes': quotes
    }

print(f'Extracted {len(tact_data)} tact words.')
with open('scratch/tact_from_touch.json', 'w', encoding='utf-8') as out:
    json.dump(tact_data, out, indent=2, ensure_ascii=False)
