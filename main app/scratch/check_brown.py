import nltk, re
from nltk.corpus import brown, webtext, gutenberg

test_words = ['deactivate', 'interactive', 'proactive', 'reactive', 'redact', 'reenact', 'overreact', 'hyperactivity']

print("Searching NLTK corpora for test words...")
for w in test_words:
    pat = re.compile(rf'\b({re.escape(w)})\b', re.IGNORECASE)
    hits = []
    # search brown
    for cat in brown.categories():
        for sent in brown.sents(categories=cat):
            s_text = " ".join(sent)
            if pat.search(s_text):
                hits.append(("Brown Corpus (" + cat + ")", s_text))
                if len(hits) >= 3:
                    break
        if len(hits) >= 3:
            break
            
    print(f"Word '{w}': {len(hits)} hits in Brown")
    for src, s in hits[:2]:
        print(f"   [{src}] {s[:100]}...")
