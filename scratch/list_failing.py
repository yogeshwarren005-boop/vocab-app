import subprocess, sys

sys.stdout.reconfigure(encoding="utf-8")

cmd = ['node', 'main app/scripts/audit-latin-roots.mjs', 'App database/Latin roots/Cluster Motion/Dashboard — ven']
p = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')

fails = {}
current_file = None

for line in p.stdout.splitlines():
    if line.startswith('❌ '):
        current_file = line.replace('❌ ', '').replace(':', '').strip()
        fails[current_file] = []
    elif line.startswith('   - ') and current_file:
        fails[current_file].append(line.strip())

print(f"Total failing words: {len(fails)}")
for word, errs in fails.items():
    print(f"{word}: {errs}")
