import os, subprocess, sys
sys.stdout.reconfigure(encoding='utf-8')

root_dir = 'App database/Latin roots'
clusters = sorted([d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d)) and d.startswith('Cluster')])
print(f"Total clusters: {len(clusters)}")

failing = []
pristine = []

for c in clusters:
    c_path = os.path.join(root_dir, c)
    res = subprocess.run(
        ['node', 'main app/scripts/audit-latin-roots.mjs', c_path],
        capture_output=True, text=True, encoding='utf-8', errors='replace'
    )
    if '✅ 100% PRISTINE' in res.stdout:
        pristine.append(c)
        print(f"✅ {c}")
    else:
        # extract problem count
        lines = res.stdout.splitlines()
        prob_line = [l for l in lines if 'Problem words:' in l]
        tot_line = [l for l in lines if 'Total words audited:' in l]
        prob_str = prob_line[0] if prob_line else "unknown"
        tot_str = tot_line[0] if tot_line else "unknown"
        failing.append((c, tot_str, prob_str))
        print(f"❌ {c} ({tot_str}, {prob_str})")

print(f"\nPristine clusters: {len(pristine)} / {len(clusters)}")
print(f"Failing clusters: {len(failing)} / {len(clusters)}")
for f in failing:
    print(f)
