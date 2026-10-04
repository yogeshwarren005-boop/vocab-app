import os, sys

sys.stdout.reconfigure(encoding="utf-8")

curated_clusters = [
    r"App database\Latin roots\Cluster Action",
    r"App database\Latin roots\Cluster Action & State",
    r"App database\Latin roots\Cluster Motion"
]

curated_words = {}
for c in curated_clusters:
    for root, dirs, files in os.walk(c):
        for f in files:
            if f.endswith(".md") and not f.startswith("Dashboard — "):
                curated_words[f] = os.path.join(root, f)

print(f"Total pristine notes in already curated clusters: {len(curated_words)}")

speed_dir = r"App database\Latin roots\Cluster Movement & Speed"
speed_dashboards = [d for d in os.listdir(speed_dir) if os.path.isdir(os.path.join(speed_dir, d)) and d.startswith("Dashboard — ")]

total_matches = 0
for d in speed_dashboards:
    d_path = os.path.join(speed_dir, d)
    words = [f for f in os.listdir(d_path) if f.endswith(".md") and not f.startswith("Dashboard — ")]
    matches = [w for w in words if w in curated_words]
    if matches:
        print(f"  {d}: {len(matches)} / {len(words)} matches")
        total_matches += len(matches)

print(f"\nTotal graftable matches across Cluster Movement & Speed: {total_matches}")
