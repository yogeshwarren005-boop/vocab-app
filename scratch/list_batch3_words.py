import os

dashboards = ['Dashboard — sap', 'Dashboard — sci']
base_dir = r'App database/Latin roots/Cluster Thought'

for d in dashboards:
    p = os.path.join(base_dir, d)
    files = [f for f in os.listdir(p) if f.endswith('.md') and not f.startswith('Dashboard —') and not f.startswith('Word Triage —')]
    print(f"{d} ({len(files)} words): {', '.join([f[:-3] for f in sorted(files)])}")
