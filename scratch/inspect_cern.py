import os, json, sys
sys.stdout.reconfigure(encoding='utf-8')

p = r'App database/Latin roots/Cluster Thought/Dashboard — cern'
files = sorted([f for f in os.listdir(p) if f.endswith('.md') and not f.startswith('Dashboard —') and not f.startswith('Word Triage —')])

for f in files:
    with open(os.path.join(p, f), 'r', encoding='utf-8') as fin:
        c = fin.read()
    print(f"=== {f} ===")
    lines = c.splitlines()
    for l in lines:
        if l.strip().startswith('1.') or l.strip().startswith('2.') or '📜' in l:
            print("  ", l.strip()[:140])
