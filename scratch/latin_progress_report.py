import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

base = r"App database/Latin roots"
clusters = sorted([d for d in os.listdir(base) if os.path.isdir(os.path.join(base, d)) and d.startswith("Cluster")])

results = []
for c in clusters:
    cp = os.path.join(base, c)
    total_words = 0
    for root, dirs, files in os.walk(cp):
        for f in files:
            if f.endswith(".md") and not f.startswith("Dashboard") and not f.startswith("Word Triage"):
                total_words += 1
    
    cmd = ["node", "main app/scripts/audit-latin-roots.mjs", cp]
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    is_pass = "✅ 100% PRISTINE (PASS)" in proc.stdout
    results.append({"cluster": c, "words": total_words, "pass": is_pass})

passed = [r for r in results if r["pass"]]
failed = [r for r in results if not r["pass"]]

total_words = sum(r["words"] for r in results)
passed_words = sum(r["words"] for r in passed)

print(f"TOTAL_CLUSTERS: {len(results)}")
print(f"PASSED_CLUSTERS: {len(passed)}")
print(f"PENDING_CLUSTERS: {len(failed)}")
print(f"TOTAL_WORDS: {total_words}")
print(f"PASSED_WORDS: {passed_words} ({passed_words/total_words*100:.2f}%)")

print("\n--- PASSED CLUSTERS ---")
for r in passed:
    print(f"  [PASS] {r['cluster']} ({r['words']} words)")

print("\n--- PENDING CLUSTERS (sorted by size) ---")
failed.sort(key=lambda x: x["words"])
for r in failed:
    print(f"  [PENDING] {r['cluster']} ({r['words']} words)")
