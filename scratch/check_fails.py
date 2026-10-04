import subprocess, sys

sys.stdout.reconfigure(encoding="utf-8")

cmd = ['node', 'main app/scripts/audit-latin-roots.mjs', 'App database/Latin roots/Cluster Motion/Dashboard — ven']
p = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')

fails = []
current_file = None
current_errors = []

for line in p.stdout.splitlines():
    if line.startswith('❌ '):
        if current_file:
            fails.append((current_file, current_errors))
        current_file = line.replace('❌ ', '').strip()
        current_errors = []
    elif line.startswith('   - ') and current_file:
        current_errors.append(line.strip())

if current_file:
    fails.append((current_file, current_errors))

print(f"Total failing files: {len(fails)}")
for f, errs in fails:
    print(f"\n{f}:")
    for e in errs:
        print(f"  {e}")
