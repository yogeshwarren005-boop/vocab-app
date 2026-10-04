import os, subprocess, json, sys

sys.stdout.reconfigure(encoding="utf-8")

out = subprocess.run(
    ['node', 'main app/scripts/audit-latin-roots.mjs', 'App database/Latin roots/Cluster Movement & Speed/Dashboard — cur'],
    capture_output=True,
    encoding='utf-8'
).stdout

failed_files = [line.replace('❌ ', '').replace('.md:', '') for line in out.splitlines() if line.startswith('❌')]
print(f"Total unshared failed: {len(failed_files)}")
print(failed_files)

with open('scratch/cur_unshared_words.json', 'w', encoding='utf-8') as f:
    json.dump(failed_files, f, ensure_ascii=False, indent=2)
