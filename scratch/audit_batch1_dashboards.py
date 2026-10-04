import subprocess, sys
sys.stdout.reconfigure(encoding="utf-8")

dashboards = ['Dashboard — licent', 'Dashboard — oscul', 'Dashboard — iter', 'Dashboard — torp', 'Dashboard — unct', 'Dashboard — ira', 'Dashboard — joc']
all_pass = True

for d in dashboards:
    proc = subprocess.run(['node', 'main app/scripts/audit-latin-roots.mjs', f'App database/Latin roots/Cluster Action & State/{d}'], capture_output=True, text=True, encoding='utf-8')
    lines = proc.stdout.splitlines()
    verdict = [l for l in lines if 'Audit Verdict:' in l]
    v_str = verdict[0] if verdict else "No verdict"
    print(f'{d}: {v_str}')
    if 'FAIL' in proc.stdout:
        all_pass = False
        for l in lines:
            if l.startswith('❌ '):
                print('  ' + l)

if all_pass:
    print('\n🎉 ALL 7 DASHBOARDS PASSED 100% PRISTINE!')
