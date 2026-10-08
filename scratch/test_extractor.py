import json, re

with open('scratch/separation_vault_matches.json', 'r', encoding='utf-8') as f:
    matches = json.load(f)

print(f'Total matched words: {len(matches)}')

success_count = 0
for w, p in matches.items():
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()

    p_def = re.search(r'1\.\s+\*\*Primary Definition[^*]*\*\*:\s*([^\n\r]+)', c)
    s_def = re.search(r'2\.\s+\*\*Secondary[^*]*\*\*:\s*([^\n\r]+)', c)
    quotes = re.findall(r'> - 📜 \*\*([^*]+)\s+\(\*([^*]+)\*\):\*\*\s+\*\"([^\"]+)\"\*', c)

    if not p_def or not s_def or len(quotes) != 3:
        print(f"FAILED on {w}: p_def={bool(p_def)}, s_def={bool(s_def)}, quotes={len(quotes)}")
    else:
        success_count += 1

print(f'Successfully extracted pristine info for {success_count} / {len(matches)} matched words!')
