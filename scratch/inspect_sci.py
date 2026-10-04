import os, json, sys
sys.stdout.reconfigure(encoding='utf-8')

p = r'App database/Latin roots/Cluster Thought/Dashboard — sci'
files = sorted([f for f in os.listdir(p) if f.endswith('.md') and not f.startswith('Dashboard —') and not f.startswith('Word Triage —')])

print(f"Total words in Dashboard — sci: {len(files)}")
for f in files:
    with open(os.path.join(p, f), 'r', encoding='utf-8') as fin:
        c = fin.read()
    lines = [l.strip() for l in c.splitlines() if l.strip().startswith('1.') or l.strip().startswith('2.') or '📜' in l]
    print(f"=== {f} ({len([l for l in lines if '📜' in l])} quotes) ===")
    for l in lines[:3]:
        print("  ", l[:120])
