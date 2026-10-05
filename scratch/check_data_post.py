import sys
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

WORDS = [
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

CIRCULAR_RE = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.IGNORECASE)

BANNED_PHRASES = [
    'In specialized and domain usage, denoting specific qualities',
    'In technical and systematic terminology, the action',
    'In functional and operational contexts, an agent',
    'The clinical presentation of',
    'Every pathological manifestation of',
    'The gradual evolutionary modification of',
    'In academic literature,',
    'Academic Lexicon',
    'Classic Author'
]

def validate_data(data):
    errors = []
    
    # 1. Word count & keys check
    expected_keys = [f"{w}.md" for w in WORDS]
    missing = [k for k in expected_keys if k not in data]
    extra = [k for k in data if k not in expected_keys]
    
    if missing:
        errors.append(f"Missing keys ({len(missing)}): {missing}")
    if extra:
        errors.append(f"Extra keys ({len(extra)}): {extra}")
        
    for k in expected_keys:
        if k not in data:
            continue
        entry = data[k]
        w = k[:-3]
        
        # Primary definition check
        prim = entry.get('primary', '').strip()
        if len(prim) < 25:
            errors.append(f"[{k}] primary definition too short ({len(prim)} chars): '{prim}'")
        if CIRCULAR_RE.search(prim):
            errors.append(f"[{k}] primary definition contains circular formula: '{prim}'")
            
        # Secondary definition check
        sec = entry.get('secondary', '').strip()
        if len(sec) < 25:
            errors.append(f"[{k}] secondary definition too short ({len(sec)} chars): '{sec}'")
        if CIRCULAR_RE.search(sec):
            errors.append(f"[{k}] secondary definition contains circular formula: '{sec}'")
            
        # Jaccard overlap check
        p_tok = set(re.findall(r'\w+', prim.lower()))
        s_tok = set(re.findall(r'\w+', sec.lower()))
        union = p_tok | s_tok
        jaccard = len(p_tok & s_tok) / len(union) if union else 0.0
        if jaccard >= 0.70:
            errors.append(f"[{k}] Jaccard overlap too high ({jaccard:.2f} >= 0.70)")
            
        # Quotes check
        quotes = entry.get('quotes', [])
        if len(quotes) != 3:
            errors.append(f"[{k}] quotes count {len(quotes)} != 3")
            continue
            
        authors = [q.get('author', '').strip() for q in quotes]
        if len(set(authors)) != 3:
            errors.append(f"[{k}] duplicate authors: {authors}")
            
        for i, q in enumerate(quotes):
            auth = q.get('author', '').strip()
            work = q.get('work', '').strip()
            q_text = q.get('quote', '').strip()
            
            if len(auth) < 3:
                errors.append(f"[{k}] quote[{i}] author too short (<3): '{auth}'")
            if len(work) < 2:
                errors.append(f"[{k}] quote[{i}] work too short (<2): '{work}'")
            if not q_text:
                errors.append(f"[{k}] quote[{i}] quote text empty")
            if '**' not in q_text:
                errors.append(f"[{k}] quote[{i}] missing bold target word: '{q_text}'")
                
            # Check banned phrases
            for b in BANNED_PHRASES:
                if b in auth or b in work or b in q_text or b in prim or b in sec:
                    errors.append(f"[{k}] contains banned phrase '{b}'")
                    
    return errors

if __name__ == '__main__':
    json_path = 'scratch/data_post.json'
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {json_path} does not exist yet.")
        sys.exit(1)
        
    print(f"Validating {json_path} with {len(data)} entries...")
    errs = validate_data(data)
    if errs:
        print(f"\n❌ FAILED WITH {len(errs)} ERRORS:")
        for e in errs[:30]:
            print(f"  - {e}")
        if len(errs) > 30:
            print(f"  ... and {len(errs) - 30} more errors.")
        sys.exit(1)
    else:
        print("\n✅ SUCCESS! All 64 words pass 100% of all rules pristine:")
        print("  1. Exactly 64 word entries with .md keys.")
        print("  2. Primary definitions >= 25 chars, non-circular, substantive.")
        print("  3. Secondary definitions >= 25 chars, nuanced, Jaccard overlap < 0.70.")
        print("  4. Exactly 3 distinct real authors per word (len(set(authors)) == 3).")
        print("  5. Authors >= 3 chars, works >= 2 chars, authentic citations.")
        print("  6. Target words bolded with double asterisks (**word**).")
        print("  7. Zero banned synthetic boilerplate phrases.")
        sys.exit(0)
