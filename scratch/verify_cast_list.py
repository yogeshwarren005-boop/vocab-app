import os
import glob

files = glob.glob("App database/Latin roots/Cluster Virtue/Dashboard — cast/*.md")
words = [os.path.basename(f)[:-3] for f in files if not os.path.basename(f).startswith(("Dashboard", "Word Triage", "Cluster", "Semantic Field"))]
print(f"Total words found: {len(words)}")
print(sorted(words))

req_words = ['cast', 'castanea', 'castanets', 'castanopsis', 'castanospermum', 'castaway', 'caste', 'casteless', 'castellated', 'caster', 'castigate', 'castigation', 'castile', 'castilian', 'castilla', 'castilleia', 'castilleja', 'castillian', 'casting', 'castle', 'castled', 'castling', 'castor', 'castoridae', 'castoroides', 'castrate', 'castrated', 'castration', 'castrato', 'castries', 'castro', 'castroism', 'miscast', 'overcast', 'overcasting', 'precast', 'recast', 'recasting', 'uncastrated']

diff1 = set(req_words) - set(words)
diff2 = set(words) - set(req_words)
print("Difference (req - found):", diff1)
print("Difference (found - req):", diff2)
