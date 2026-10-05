import os, glob

words = [
    'anna', 'annaba', 'annalist', 'annalistic', 'annals', 'annam', 'annamese', 'annamite',
    'annapolis', 'annapurna', 'anne', 'anneal', 'annealing', 'annelid', 'annelida', 'annelidan',
    'annex', 'annexa', 'annexal', 'annexation', 'annexational', 'annexe', 'anniellidae',
    'annihilate', 'annihilated', 'annihilating', 'annihilation', 'annihilative', 'annihilator',
    'anniversary', 'annon', 'annona', 'annonaceae', 'annotate', 'annotating', 'annotation',
    'annotator', 'announce', 'announced', 'announcement', 'announcer', 'annoy', 'annoyance',
    'annoyed', 'annoyer', 'annoying', 'annoyingly', 'annual', 'annually', 'annualry',
    'annuitant', 'annuity', 'annul', 'annular', 'annulate', 'annulated', 'annulet',
    'annulment', 'annulus', 'annum', 'annunciate', 'annunciation', 'annunciator',
    'annunciatory', 'inanna', 'per annum', 'semiannual', 'semiannually', 'superannuate',
    'superannuated', 'superannuation', 'susanna', 'unannealed', 'unannounced'
]

print("Total words in list:", len(words))

dash_dir = r"App database\Latin roots\Cluster Time\Dashboard — ann"
existing_files = [os.path.splitext(f)[0] for f in os.listdir(dash_dir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]

print("Total markdown word files in directory:", len(existing_files))

diff1 = set(words) - set(existing_files)
diff2 = set(existing_files) - set(words)
print("In words but not in dir:", diff1)
print("In dir but not in words:", diff2)
