import os

p = r"App database\Latin roots\Cluster Motion\Dashboard — mot"
files = sorted([f for f in os.listdir(p) if f.endswith('.md') and not f.startswith(('Dashboard', 'Word Triage'))])
print(f"Total words: {len(files)}")
print(files)
