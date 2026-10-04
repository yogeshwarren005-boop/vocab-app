import os, sys

sys.stdout.reconfigure(encoding="utf-8")

sal_dir = r"App database\Latin roots\Cluster Movement & Speed\Dashboard — sal"
sal_words = {f for f in os.listdir(sal_dir) if f.endswith(".md") and not f.startswith(("Dashboard", "Word Triage"))}
print(f"Total words in Dashboard — sal: {len(sal_words)}")

# check against Cluster Motion / Dashboard — sult
sult_dir = r"App database\Latin roots\Cluster Motion\Dashboard — sult"
if os.path.exists(sult_dir):
    sult_words = {f for f in os.listdir(sult_dir) if f.endswith(".md") and not f.startswith(("Dashboard", "Word Triage"))}
    print(f"Total words in Dashboard — sult: {len(sult_words)}")
    common = sal_words.intersection(sult_words)
    print(f"Overlap between sal and sult: {len(common)} words")
    print(common)
