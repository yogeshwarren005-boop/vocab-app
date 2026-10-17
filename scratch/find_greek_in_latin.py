import os, json

# Comprehensive list of well-known Greek roots
greek_roots_lexicon = {
    'acro', 'actin', 'aer', 'aesthet', 'agon', 'agora', 'agro', 'alg', 'all', 'allo',
    'amphi', 'anemo', 'anth', 'anthrop', 'arch', 'archae', 'arct', 'arist', 'arithm',
    'aster', 'astr', 'athl', 'auto', 'aux', 'bar', 'bas', 'bath', 'bibl', 'bio',
    'blast', 'brachi', 'brachy', 'bront', 'cac', 'cal', 'calli', 'cardi', 'carp',
    'cephal', 'chemo', 'chir', 'chlor', 'chrom', 'chron', 'chrys', 'cine', 'clast',
    'clin', 'coel', 'cosm', 'crani', 'crat', 'crit', 'cryo', 'crypt', 'cyan', 'cycl',
    'cyn', 'cyst', 'cyt', 'dactyl', 'dec', 'dem', 'dendr', 'derm', 'dia', 'din',
    'dox', 'drom', 'dynam', 'dys', 'eco', 'ect', 'endo', 'entom', 'eo', 'ep', 'epi',
    'erg', 'erythr', 'eth', 'ethn', 'etym', 'eu', 'galact', 'gam', 'gastr', 'ge',
    'gen', 'geo', 'ger', 'gloss', 'glot', 'glyph', 'gnos', 'gno', 'gon', 'gram',
    'graph', 'gyn', 'gyro', 'haem', 'hal', 'hect', 'heli', 'helminth', 'hepar',
    'hepat', 'hept', 'hetero', 'hier', 'hipp', 'hist', 'hod', 'holo', 'hom', 'homeo',
    'homo', 'hydr', 'hygr', 'hymn', 'hyper', 'hypn', 'hypo', 'hyster', 'iatr',
    'ichthy', 'icon', 'id', 'idio', 'iso', 'kilo', 'kine', 'kudo', 'lab', 'lamp',
    'laryng', 'lep', 'lepid', 'lepto', 'leuc', 'leuk', 'lex', 'lip', 'lith', 'log',
    'lysis', 'lyt', 'macr', 'macro', 'mania', 'meg', 'mega', 'megal', 'melan', 'mer',
    'meso', 'meta', 'metr', 'micr', 'micro', 'miso', 'mnem', 'mon', 'morph', 'my',
    'myc', 'myo', 'myri', 'myth', 'narc', 'naut', 'necr', 'neo', 'nephr', 'neur',
    'nom', 'noo', 'nos', 'nost', 'nyct', 'odont', 'odyn', 'oec', 'oen', 'oligo',
    'onoma', 'onym', 'onto', 'oo', 'ophthalm', 'opt', 'or', 'organ', 'ornith', 'oro',
    'ortho', 'osm', 'oste', 'osteo', 'ot', 'oxy', 'pachy', 'paed', 'palaeo', 'paleo',
    'pan', 'pant', 'par', 'para', 'path', 'ped', 'pent', 'pept', 'peri', 'petr',
    'phag', 'phan', 'pharmac', 'phem', 'phen', 'phil', 'phleb', 'phob', 'phon',
    'phor', 'phos', 'phot', 'phren', 'phyl', 'phyll', 'phys', 'phyt', 'plag',
    'plan', 'plas', 'plast', 'platy', 'pleg', 'pleio', 'pleur', 'pneum', 'pneumon',
    'pod', 'pogon', 'poli', 'polm', 'poly', 'potam', 'pragm', 'prax', 'presby',
    'pro', 'prot', 'proto', 'pseud', 'pseudo', 'psych', 'pter', 'ptil', 'ptych',
    'pyr', 'pyret', 'pyro', 'rhin', 'rhiz', 'rhod', 'rhomb', 'rhythm', 'sarc',
    'saur', 'scaph', 'schis', 'schiz', 'sci', 'scia', 'scler', 'scop', 'scoto',
    'seism', 'sema', 'seme', 'semi', 'sep', 'siphon', 'sit', 'som', 'somat',
    'soph', 'spasm', 'sperm', 'spermat', 'sphen', 'spher', 'sphygm', 'spir',
    'splanch', 'splen', 'spor', 'stal', 'stat', 'steat', 'steg', 'sten', 'stere',
    'steth', 'sthen', 'stich', 'stigm', 'stich', 'stom', 'stomat', 'strat', 'strep',
    'strob', 'styl', 'sym', 'syn', 'tachy', 'tact', 'taur', 'tauto', 'tax', 'techn',
    'tele', 'tel', 'teleo', 'ten', 'tetr', 'thalass', 'thanat', 'the', 'theatr',
    'thec', 'theo', 'therap', 'therm', 'thes', 'thet', 'thigmo', 'thorac', 'thromb',
    'thym', 'thyr', 'toc', 'tom', 'ton', 'top', 'tox', 'trach', 'traumat', 'trep',
    'tri', 'trib', 'trich', 'troch', 'trop', 'troph', 'typ', 'typh', 'ur', 'uran',
    'xen', 'xer', 'xiph', 'xyl', 'ze', 'zel', 'zo', 'zoon', 'zyg', 'zym'
}

latin_dir = 'App database/Latin roots'
misplaced_greek = []

for cluster in os.listdir(latin_dir):
    c_path = os.path.join(latin_dir, cluster)
    if not os.path.isdir(c_path) or not cluster.startswith('Cluster '):
        continue
    for d in os.listdir(c_path):
        d_path = os.path.join(c_path, d)
        if not os.path.isdir(d_path):
            continue
        clean_name = d.replace('Dashboard — ', '').replace('Dashboard - ', '').replace('Dashboard \u2014 ', '').strip().lower()
        if clean_name in greek_roots_lexicon:
            words = [f for f in os.listdir(d_path) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]
            misplaced_greek.append({
                'cluster': cluster,
                'folder': d,
                'root': clean_name,
                'word_count': len(words),
                'sample_words': [w[:-3] for w in words[:5]]
            })

print(f"Total suspected Greek roots inside Latin roots: {len(misplaced_greek)}")
total_words = sum(m['word_count'] for m in misplaced_greek)
print(f"Total words in these roots: {total_words}")
print(json.dumps(misplaced_greek[:20], indent=2))
