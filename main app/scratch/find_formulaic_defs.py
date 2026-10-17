import glob, os, re

files = glob.glob(r'App database\Latin roots\Cluster Action\Dashboard — act\*.md')

re_patterns = [
    r'\bquality of being\b',
    r'\bstate of being\b',
    r'\bcondition of being\b',
    r'\bthe act of \w+ing\b',
    r'\bthe process of \w+ing\b'
]

flagged = []
for f in files:
    name = os.path.basename(f)
    if name.startswith('Dashboard') or name.startswith('Word Triage'):
        continue
    w = name.replace('.md', '')
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    pMatch = re.search(r'1\.\s*\*\*([^*]+)\*\*:\s*([^\r\n]+)', c)
    sMatch = re.search(r'2\.\s*\*\*([^*]+)\*\*:\s*([^\r\n]+)', c)
    p = pMatch.group(2).strip() if pMatch else ''
    s = sMatch.group(2).strip() if sMatch else ''
    
    for pat in re_patterns:
        if re.search(pat, p, re.IGNORECASE):
            flagged.append((w, 'Primary', p))
        if re.search(pat, s, re.IGNORECASE):
            flagged.append((w, 'Secondary', s))

print(f"Total entries with simple 'quality/state/act of' patterns: {len(flagged)}")
for w, which, defn in flagged:
    print(f"  {w} [{which}]: {defn}")
