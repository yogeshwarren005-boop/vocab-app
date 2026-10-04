import os, sys
sys.stdout.reconfigure(encoding="utf-8")

latin_root_dir = r"App database\Latin roots"
clusters = [d for d in os.listdir(latin_root_dir) if os.path.isdir(os.path.join(latin_root_dir, d))]

print(f"Total clusters in Latin roots: {len(clusters)}")
total_dashboards = 0
total_words = 0

for c in sorted(clusters):
    c_path = os.path.join(latin_root_dir, c)
    dashboards = [d for d in os.listdir(c_path) if os.path.isdir(os.path.join(c_path, d)) and d.startswith("Dashboard — ")]
    c_words = 0
    for d in dashboards:
        d_path = os.path.join(c_path, d)
        words = [f for f in os.listdir(d_path) if f.endswith(".md") and not f.startswith("Dashboard — ")]
        c_words += len(words)
    total_dashboards += len(dashboards)
    total_words += c_words
    print(f"Cluster: {c} | {len(dashboards)} dashboards | {c_words} words")

print(f"\nTOTAL: {len(clusters)} clusters | {total_dashboards} dashboards | {total_words} words")
