import os, glob

base_dir = r"App database\Latin roots\Cluster Action & State"
dashboards = ["Dashboard — deb", "Dashboard — ult"]

for d in dashboards:
    dpath = os.path.join(base_dir, d)
    files = [f for f in os.listdir(dpath) if f.endswith(".md") and not f.startswith("Dashboard —")]
    print(f"{d}: {len(files)} words")
    print("Sample:", files[:10])
