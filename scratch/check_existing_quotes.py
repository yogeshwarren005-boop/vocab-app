import os
import re
import json

words = [
    'compost', 'expostulate', 'expostulation', 'impost', 'imposter', 'impostor', 'imposture',
    'post', 'postage', 'postal', 'postcard', 'postcava', 'postcode', 'posted', 'poster',
    'posterboard', 'posterior', 'posteriority', 'posterity', 'postern', 'postexilic',
    'postgraduate', 'posthumous', 'posthumously', 'postiche', 'postictal', 'postilion',
    'postillion', 'postimpressionist', 'postindustrial', 'posting', 'postlude', 'postman',
    'postmark', 'postmaster', 'postmenopausal', 'postmeridian', 'postmillennial', 'postmistress',
    'postmodern', 'postmodernism', 'postmodernist', 'postmortal', 'postmortem', 'postnatal',
    'postnuptial', 'postoperative', 'postoperatively', 'postpone', 'postponement', 'postponer',
    'postscript', 'postulant', 'postulate', 'postulation', 'postulational', 'postulator',
    'postum', 'postural', 'posture', 'posturer', 'posturing', 'preposterous', 'preposterously'
]

d = r'App database\Latin roots\Cluster Time\Dashboard — post'
existing_quotes = {}
for w in words:
    p = os.path.join(d, f'{w}.md')
    quotes = []
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('> - 📜') or line.startswith('- 📜'):
                    m = re.search(r'📜\s*\*\*([^*]+)\s*\(\*([^*]+)\*\):\*\*\s*\"?(.*?)\"?$', line)
                    if m:
                        auth = m.group(1).strip()
                        work = m.group(2).strip()
                        q_text = m.group(3).strip().strip('"')
                        if auth not in ['Academic Lexicon', 'Classic Author']:
                            quotes.append({'author': auth, 'work': work, 'quote': q_text})
    existing_quotes[w] = quotes

with open('scratch/existing_post_quotes.json', 'w', encoding='utf-8') as f:
    json.dump(existing_quotes, f, indent=2, ensure_ascii=False)

for w in words:
    q_list = existing_quotes[w]
    authors = [q['author'] for q in q_list]
    print(f"{w}: {len(q_list)} real quotes -> {authors}")
