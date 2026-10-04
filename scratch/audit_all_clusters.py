import os, sys, subprocess, json
sys.stdout.reconfigure(encoding="utf-8")

latin_root_dir = r"App database\Latin roots"
clusters = [d for d in os.listdir(latin_root_dir) if os.path.isdir(os.path.join(latin_root_dir, d))]

results = []

for c in sorted(clusters):
    c_path = os.path.join(latin_root_dir, c)
    dashboards = [d for d in os.listdir(c_path) if os.path.isdir(os.path.join(c_path, d)) and d.startswith("Dashboard — ")]
    if not dashboards:
        continue
    
    # Run audit on this cluster
    proc = subprocess.run(
        ["node", "main app/scripts/audit-latin-roots.mjs", c_path],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )
    
    total = 0
    problem = 0
    pristine = 0
    verdict = "UNKNOWN"
    
    for line in proc.stdout.splitlines():
        if line.startswith("Total words audited:"):
            total = int(line.split(":")[1].strip())
        elif line.startswith("Problem words:"):
            problem = int(line.split(":")[1].strip())
        elif line.startswith("Pristine words:"):
            pristine = int(line.split(":")[1].strip())
        elif line.startswith("Audit Verdict:"):
            verdict = line.split(":")[1].strip()
    
    res = {
        "cluster": c,
        "dashboards": len(dashboards),
        "total": total,
        "pristine": pristine,
        "problem": problem,
        "verdict": verdict
    }
    results.append(res)
    print(f"[{c}] Total: {total} | Pristine: {pristine} | Problem: {problem} | Verdict: {verdict}")

with open("scratch/clusters_audit_summary.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print("\nSummary saved to scratch/clusters_audit_summary.json")
