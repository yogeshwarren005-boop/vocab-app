import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
target = 'App database/Latin roots/Cluster Greek-Latin Hybrid'
dashboards = sorted([d for d in os.listdir(target) if os.path.isdir(os.path.join(target, d)) and d.startswith('Dashboard — ')])
tot = 0
for d in dashboards:
    files = [f for f in os.listdir(os.path.join(target, d)) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]
    print(f'{d}: {len(files)} files')
    tot += len(files)
print(f'Total words in Cluster Greek-Latin Hybrid: {tot}')
