import os, subprocess, json

latin_dir = r"App database\Latin roots"
clusters = sorted([d for d in os.listdir(latin_dir) if os.path.isdir(os.path.join(latin_dir, d)) and d.startswith("Cluster")])

results = {}
for idx, c in enumerate(clusters, 1):
    c_path = os.path.join(latin_dir, c)
    cmd = ["node", "main app/scripts/audit-latin-roots.mjs", c_path]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        out = res.stdout
        is_pass = "100% PRISTINE (PASS)" in out
        
        # Parse total words and problems
        total = 0
        problems = 0
        for line in out.splitlines():
            if "Total words audited:" in line:
                total = int(line.split(":")[-1].strip())
            elif "Problem words:" in line:
                problems = int(line.split(":")[-1].strip())
        
        results[c] = {
            "index": idx,
            "pass": is_pass,
            "total": total,
            "problems": problems
        }
        status_str = "PASS" if is_pass else f"FAIL ({problems}/{total})"
        print(f"[{idx:02d}/{len(clusters):02d}] {c}: {status_str}")
    except Exception as e:
        print(f"[{idx:02d}/{len(clusters):02d}] {c}: ERROR {e}")
        results[c] = {"index": idx, "pass": False, "error": str(e)}

with open("scratch/all_clusters_audit.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print("\nAudit summary saved to scratch/all_clusters_audit.json")
