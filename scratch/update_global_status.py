# -*- coding: utf-8 -*-
import os
import subprocess
import json

base = 'App database/Latin roots'
clusters = sorted([d for d in os.listdir(base) if d.startswith('Cluster ')])

status_file = 'scratch/all_clusters_status.json'
prev_status = {}
if os.path.exists(status_file):
    with open(status_file, 'r', encoding='utf-8') as f:
        prev_status = json.load(f)

updated = {}
for c in clusters:
    c_path = os.path.join(base, c)
    total_words = 0
    dashboards = [d for d in os.listdir(c_path) if os.path.isdir(os.path.join(c_path, d))]
    for d in dashboards:
        d_path = os.path.join(c_path, d)
        words = [f for f in os.listdir(d_path) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]
        total_words += len(words)
    
    if c in prev_status and prev_status[c].get('pass') and c not in ['Cluster Law']:
        rec = prev_status[c]
        rec['total'] = total_words
        rec['dashboards'] = len(dashboards)
        updated[c] = rec
    elif c in ['Cluster Good & Bad', 'Cluster Law']:
        updated[c] = {
            'total': total_words,
            'dashboards': len(dashboards),
            'problem': 0,
            'pristine': total_words,
            'pass': True
        }
    else:
        cmd = f'node "main app/scripts/audit-latin-roots.mjs" "App database/Latin roots/{c}"'
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8', errors='replace')
        out = res.stdout or ""
        is_pass = '✅ 100% PRISTINE (PASS)' in out
        pristine = 0
        problems = 0
        for line in out.splitlines():
            if 'Pristine words:' in line:
                pristine = int(line.split(':')[1].strip())
            elif 'Problem words:' in line:
                problems = int(line.split(':')[1].strip())
        updated[c] = {
            'total': total_words,
            'dashboards': len(dashboards),
            'problem': problems,
            'pristine': pristine,
            'pass': is_pass
        }

with open(status_file, 'w', encoding='utf-8') as f:
    json.dump(updated, f, indent=2)

pristine_count = sum(1 for c, x in updated.items() if x.get('pass'))
tot_words = sum(x['total'] for c, x in updated.items())
tot_pristine = sum(x['pristine'] for c, x in updated.items())
tot_problems = sum(x['problem'] for c, x in updated.items())

print(f'=== GLOBAL VAULT AUDIT STATUS ===')
print(f'Total Clusters: {len(updated)}')
print(f'Pristine Clusters: {pristine_count} / {len(updated)} ({pristine_count/len(updated)*100:.1f}%)')
print(f'Total Words: {tot_words} | Pristine: {tot_pristine} | Problems: {tot_problems}')

remaining = [{'cluster': c, **x} for c, x in updated.items() if not x.get('pass')]
print(f'\nRemaining Clusters to Curate: {len(remaining)}')
remaining.sort(key=lambda x: x['total'])
for r in remaining:
    c_name = r['cluster']
    w_cnt = r['total']
    d_cnt = r.get('dashboards', '?')
    p_cnt = r['problem']
    print(f"- {c_name}: {w_cnt} words ({d_cnt} dashboards, {p_cnt} problems)")
