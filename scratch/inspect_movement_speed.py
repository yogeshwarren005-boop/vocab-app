import os, sys

sys.stdout.reconfigure(encoding="utf-8")

cluster_dir = r"App database\Latin roots\Cluster Movement & Speed"
if not os.path.exists(cluster_dir):
    print(f"Directory not found: {cluster_dir}")
    sys.exit(1)

dashboards = [d for d in os.listdir(cluster_dir) if os.path.isdir(os.path.join(cluster_dir, d)) and d.startswith("Dashboard — ")]
dashboards.sort()

total_words = 0
dash_counts = []

for d in dashboards:
    d_path = os.path.join(cluster_dir, d)
    words = [f for f in os.listdir(d_path) if f.endswith(".md") and not f.startswith("Dashboard — ")]
    dash_counts.append((d, len(words)))
    total_words += len(words)

print(f"Cluster Movement & Speed: {len(dashboards)} dashboards, {total_words} total words.\n")
for d, c in dash_counts:
    print(f"  {d}: {c} words")
