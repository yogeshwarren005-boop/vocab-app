import subprocess
import json

proc = subprocess.run(
    ["node", "main app/scripts/audit-latin-roots.mjs", "App database/Latin roots/Cluster Action/Dashboard — fac"],
    capture_output=True,
    text=True,
    encoding="utf-8"
)

failing = []
for line in proc.stdout.splitlines():
    if line.startswith("❌ "):
        fname = line[2:].split(":")[0].strip()
        failing.append(fname)

print(f"Total remaining problem words: {len(failing)}")
with open("scratch/fac_remaining_107.json", "w", encoding="utf-8") as f:
    json.dump(failing, f, indent=2)

print("Batch 2 targets (next 50):")
print(failing[:50])
print(f"Batch 3 targets ({len(failing) - 50}):")
print(failing[50:])
