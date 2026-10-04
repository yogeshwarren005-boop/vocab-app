import subprocess, sys
sys.stdout.reconfigure(encoding="utf-8")

targets = [
    ("Dashboard — lax", "laxness.md"),
    ("Dashboard — lax", "relaxation.md"),
    ("Dashboard — solut", "irresoluteness.md"),
    ("Dashboard — solut", "resoluteness.md"),
    ("Dashboard — ars", "coarseness.md")
]

for d, f in targets:
    proc = subprocess.run(['node', 'main app/scripts/audit-latin-roots.mjs', f'App database/Latin roots/Cluster Action & State/{d}'], capture_output=True, text=True, encoding='utf-8')
    lines = proc.stdout.splitlines()
    print(f"=== {d}/{f} ===")
    recording = False
    for line in lines:
        if f"❌ {f}" in line:
            recording = True
            print(line)
        elif recording:
            if line.startswith("❌ ") or line.startswith("==="):
                break
            print(line)
