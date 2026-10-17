import nltk
from nltk.corpus import gutenberg, wordnet
import re

print("NLTK Gutenberg loaded successfully.")
print("Files in Gutenberg:", len(gutenberg.fileids()))

def test_word(word):
    print(f"\n--- Testing word: {word} ---")
    syns = wordnet.synsets(word)
    if syns:
        print(f"WordNet Synsets ({len(syns)}):")
        for s in syns[:2]:
            print(f"  [{s.pos()}] {s.definition()}")
            if s.examples():
                print(f"    Examples: {s.examples()[:2]}")
    else:
        print("No direct WordNet synset.")

    pattern = re.compile(rf'\b({re.escape(word)})\b', re.IGNORECASE)
    matches = 0
    for fid in gutenberg.fileids():
        text = gutenberg.raw(fid)
        for m in pattern.finditer(text):
            matches += 1
            if matches <= 2:
                # get sentence context
                s_start = max(0, m.start() - 100)
                s_end = min(len(text), m.end() + 100)
                snip = " ".join(text[s_start:s_end].split())
                print(f"  Gutenberg ({fid}): ...{snip}...")
    print(f"Total Gutenberg matches: {matches}")

test_word("abundant")
test_word("action")
test_word("solitary")
