import os, json, sys
sys.stdout.reconfigure(encoding='utf-8')

base = r'App database/Latin roots/Cluster Thought'
for d in ['Dashboard — mens', 'Dashboard — ment']:
    p = os.path.join(base, d)
    files = sorted([f for f in os.listdir(p) if f.endswith('.md') and not f.startswith('Dashboard —') and not f.startswith('Word Triage —')])
    print(f"=== {d} ({len(files)} words) ===")
    for f in files:
        with open(os.path.join(p, f), 'r', encoding='utf-8') as fin:
            c = fin.read()
        lines = [l.strip() for l in c.splitlines() if l.strip().startswith('1.') or l.strip().startswith('2.') or '📜' in l]
        print(f"--- {f} ---")
        for l in lines[:4]:
            print("  ", l[:120])
