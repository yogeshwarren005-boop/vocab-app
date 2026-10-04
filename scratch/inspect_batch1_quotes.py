import os, json, re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/thought_batch1_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for w, item in data.items():
    if w.startswith('word triage'): continue
    content = item['file_content']
    q_section = content.split('> [!quote]')[-1] if '> [!quote]' in content else ''
    quotes = [l.strip() for l in q_section.splitlines() if l.strip().startswith('>') and '📜' in l]
    print(f"=== {w} ({item['dashboard']}) [{len(quotes)} quotes in file] ===")
    for q in quotes:
        print("  ", q[:120])
