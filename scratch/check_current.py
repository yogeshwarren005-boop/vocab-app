import os
import re
import json
import sqlite3

TARGET_WORDS = [
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

def analyze():
    print(f"Total target words: {len(TARGET_WORDS)}")
    existing = {}
    for w in TARGET_WORDS:
        p = os.path.join(d, f"{w}.md")
        if not os.path.exists(p):
            print(f"MISSING FILE: {p}")
            continue
        with open(p, 'r', encoding='utf-8') as f:
            text = f.read()
        
        m_prim = re.search(r'1\.\s*\*\*Primary Definition[^\*]*\*\*:\s*([^\n\r]+)', text)
        prim = m_prim.group(1).strip() if m_prim else ''
        
        m_sec = re.search(r'2\.\s*\*\*Secondary[^\*]*\*\*:\s*([^\n\r]+)', text)
        sec = m_sec.group(1).strip() if m_sec else ''
        
        quotes = []
        for line in text.splitlines():
            line = line.strip()
            if line.startswith('- 📜') or line.startswith('-📜'):
                # - 📜 **Author (*Work*):** *"Quote"*
                m_q = re.search(r'\*\*([^*]+)\s*\(\*([^*]+)\*\):\*\*\s*\"?(.*?)\"?$', line)
                if m_q:
                    quotes.append({
                        'author': m_q.group(1).strip(),
                        'work': m_q.group(2).strip(),
                        'quote': m_q.group(3).strip().strip('"')
                    })
        existing[w] = {
            'primary': prim,
            'secondary': sec,
            'quotes': quotes
        }
    
    print(f"Loaded {len(existing)} word entries from disk.")
    
    # Check compliance of current disk files
    issues = []
    for w, entry in existing.items():
        w_issues = []
        if len(entry['primary']) < 25:
            w_issues.append(f"primary len {len(entry['primary'])} < 25")
        if len(entry['sec' if 'sec' in entry else 'secondary']) < 25:
            w_issues.append(f"secondary len {len(entry['secondary'])} < 25")
        
        # Jaccard
        tokens1 = set(re.findall(r'\w+', entry['primary'].lower()))
        tokens2 = set(re.findall(r'\w+', entry['secondary'].lower()))
        union = tokens1 | tokens2
        overlap = len(tokens1 & tokens2) / len(union) if union else 0
        if overlap >= 0.70:
            w_issues.append(f"Jaccard overlap {overlap:.2f} >= 0.70")
            
        quotes = entry['quotes']
        if len(quotes) != 3:
            w_issues.append(f"quotes count {len(quotes)} != 3")
        authors = [q['author'] for q in quotes]
        if len(set(authors)) != len(quotes):
            w_issues.append(f"repeated authors: {authors}")
        for i, q in enumerate(quotes):
            if len(q['author']) < 3:
                w_issues.append(f"q[{i}] author too short: '{q['author']}'")
            if len(q['work']) < 2:
                w_issues.append(f"q[{i}] work too short: '{q['work']}'")
            if '**' not in q['quote']:
                w_issues.append(f"q[{i}] missing bold target word: {q['quote'][:40]}...")
        if w_issues:
            issues.append((w, w_issues))
            
    print(f"\nFiles with issues currently: {len(issues)} / {len(TARGET_WORDS)}")
    for w, iss in issues[:15]:
        print(f"  {w}: {'; '.join(iss)}")

if __name__ == '__main__':
    analyze()
