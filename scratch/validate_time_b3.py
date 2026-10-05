import sys, re
sys.stdout.reconfigure(encoding='utf-8')
from scratch.curate_time_b3 import data_time_b3

dur_expected = ['corduroy', 'corduroys', 'dura', 'durability', 'durable', 'durables', 'durabolin', 'dural', 'duralumin', 'duramen', 'durance', 'durango', 'durant', 'durante', 'duration', 'durative', 'durazzo', 'durer', 'duress', 'durian', 'during', 'durio', 'durion', 'durmast', 'durra', 'durrell', 'durres', 'durum', 'endurable', 'endurance', 'endure', 'enduring', 'enduringly', 'enduringness', 'extradural', 'indurate', 'induration', 'obduracy', 'obdurate', 'obdurately', 'perdurability', 'perdurable', 'subdural', 'unendurable']
prim_expected = ['imprimatur', 'prim', 'prima', 'prima donna', 'primacy', 'primaeval', 'primal', 'primality', 'primaquine', 'primarily', 'primary', 'primate', 'primates', 'primateship', 'primatology', 'primaxin', 'prime', 'primed', 'primer', 'primeval', 'primidone', 'primigravida', 'priming', 'primipara', 'primiparous', 'primitive', 'primitively', 'primitiveness', 'primitivism', 'primly', 'primness', 'primo', 'primogenitor', 'primogeniture', 'primordial', 'primordium', 'primrose', 'primula', 'primulaceae', 'primulales', 'primus', 'reprimand']

all_expected = dur_expected + prim_expected
print(f'Total expected: {len(all_expected)}, In data: {len(data_time_b3)}')
missing = [w for w in all_expected if w not in data_time_b3]
print(f'Missing words: {missing}')

banned_phrases = [
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

errors = []
for w, d in data_time_b3.items():
    p = d.get('primary', '')
    s = d.get('secondary', '')
    q = d.get('quotes', [])
    
    if len(p) < 25:
        errors.append(f'{w}: Primary too short ({len(p)})')
    if len(s) < 25:
        errors.append(f'{w}: Secondary too short ({len(s)})')
    if re.search(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', p, re.I):
        errors.append(f'{w}: Primary has circular formula')
    if re.search(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', s, re.I):
        errors.append(f'{w}: Secondary has circular formula')
    
    p_tok = set(re.findall(r'\w+', p.lower()))
    s_tok = set(re.findall(r'\w+', s.lower()))
    jaccard = len(p_tok & s_tok) / max(len(p_tok | s_tok), 1)
    if jaccard >= 0.7:
        errors.append(f'{w}: Jaccard too high ({jaccard:.2f})')
        
    if len(q) != 3:
        errors.append(f'{w}: Quotes count {len(q)} != 3')
    
    auths = [item['author'] for item in q]
    if len(set(auths)) != 3:
        errors.append(f'{w}: Authors not distinct: {auths}')
        
    for item in q:
        quote_text = item.get('quote', '')
        auth_name = item.get('author', '')
        if '**' not in quote_text:
            errors.append(f'{w}: Target word not bolded in quote by {auth_name}')
        for b in banned_phrases:
            if b in quote_text or b in auth_name or b in item.get('work', '') or b in p or b in s:
                errors.append(f'{w}: Contains banned phrase {b}')

print(f'Total validation errors: {len(errors)}')
for e in errors:
    print('  -', e)
