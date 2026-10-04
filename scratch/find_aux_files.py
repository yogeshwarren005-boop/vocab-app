import os, sys

sys.stdout.reconfigure(encoding="utf-8")

speed_dir = r"App database\Latin roots\Cluster Movement & Speed"
aux_files = []

for root, dirs, files in os.walk(speed_dir):
    for f in files:
        if f.endswith(".md"):
            if f.startswith("Dashboard — ") or f.startswith("Word Triage") or "Triage" in f:
                aux_files.append((f, os.path.join(root, f)))

print(f"Found {len(aux_files)} auxiliary notes:")
for f, path in aux_files:
    print(f"  {f} in {os.path.dirname(path)}")
