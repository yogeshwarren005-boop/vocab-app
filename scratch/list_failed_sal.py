import subprocess, sys

sys.stdout.reconfigure(encoding="utf-8")

out = subprocess.run(
    ['node', 'main app/scripts/audit-latin-roots.mjs', 'App database/Latin roots/Cluster Movement & Speed/Dashboard — sal'],
    capture_output=True,
    encoding='utf-8'
).stdout

failed = [line for line in out.splitlines() if line.startswith('❌')]
print(f"Failed count: {len(failed)}")
for f in failed:
    print(f)
