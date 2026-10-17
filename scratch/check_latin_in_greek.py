import os

# Check roots in Greek roots that might be Latin
greek_dir = 'App database/Greek roots'

latin_stems_known = {
    'dec': 'Latin decem (ten)',
    'cent': 'Latin centum (hundred)',
    'mill': 'Latin mille (thousand)',
    'sci': 'Latin scire (to know)',
    'pass': 'Latin pati/passus (to suffer)',
    'pat': 'Latin patere (to be open) or pati (to suffer)',
    'not': 'Latin notare (to mark/note)',
    'ser': 'Latin serere (to bind/join) or serum',
    'ap': 'Latin apis (bee) or aptus (fit)',
    'cub': 'Latin cubare (to lie down)',
    'nect': 'Latin nectere (to bind)',
    'pel': 'Latin pellere (to drive)',
    'trit': 'Latin terere/tritus (to rub/wear)',
    'pan': 'Latin panis (bread) - Greek pan means all',
    'stell': 'Latin stella (star) - Greek stellein means to send',
    'par': 'Latin parare (to prepare) or par (equal) or parere (to bear)',
    'mit': 'Latin mittere (to send)',
    'mis': 'Latin mittere/missus (to send)',
    'ger': 'Latin gerere (to carry/bear) - Greek geras means old age',
    'ten': 'Latin tenere (to hold) - Greek teinein means to stretch (ten-)',
    'lab': 'Latin labi/lapsus (to slip) or labium (lip)',
    'leg': 'Latin lex/legis (law) or legere (to read) - Greek legein means to speak',
    'or': 'Latin orare (to speak) or os/oris (mouth) - Greek oros means mountain',
    'stat': 'Latin stare/status (to stand) - Greek histanai/stasis',
    'clin': 'Latin clinare (to lean) / Greek klinein',
    'bas': 'Greek basis (step/base) / Latin bassus (low)',
    'taur': 'Greek tauros / Latin taurus (bull - cognates)'
}

for cluster in os.listdir(greek_dir):
    c_path = os.path.join(greek_dir, cluster)
    if not os.path.isdir(c_path) or not cluster.startswith('Cluster '):
        continue
    for d in os.listdir(c_path):
        d_path = os.path.join(c_path, d)
        if not os.path.isdir(d_path):
            continue
        clean_name = d.replace('Dashboard — ', '').replace('Dashboard - ', '').replace('Dashboard \u2014 ', '').strip().lower()
        if clean_name in latin_stems_known:
            words = [f[:-3] for f in os.listdir(d_path) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]
            print(f"Greek Root folder: {d:25} in {cluster:30} | {latin_stems_known[clean_name]} | Words: {len(words)}")
