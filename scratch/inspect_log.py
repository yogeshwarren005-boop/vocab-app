import os, json, sys
sys.stdout.reconfigure(encoding='utf-8')

p = r'App database/Latin roots/Cluster Thought/Dashboard — log'
files = sorted([f for f in os.listdir(p) if f.endswith('.md') and not f.startswith('Dashboard —') and not f.startswith('Word Triage —')])

print(f"Total words in Dashboard — log: {len(files)}")
print(', '.join([f[:-3] for f in files]))
