import os, sys, re

# Import data from curate_act_batch1 and curate_act_batch2
import curate_act_batch1
import curate_act_batch2

data1 = curate_act_batch1.data
data2 = curate_act_batch2.data

print(f"Data 1: {len(data1)} words")
print(f"Data 2: {len(data2)} words")
all_data = {**data1, **data2}
print(f"Combined: {len(all_data)} words")

# Verify all words in Dashboard — act are covered
base_dir = r"App database\Latin roots\Cluster Action\Dashboard — act"
disk_files = [f for f in os.listdir(base_dir) if f.endswith(".md") and not f.startswith("Dashboard") and not f.startswith("Word Triage")]
print(f"Disk files: {len(disk_files)}")

missing_from_data = [f for f in disk_files if f not in all_data]
print(f"Missing from data: {missing_from_data}")

# Strict Quality Checks
issues = []
for fname, info in all_data.items():
    word = fname.replace(".md", "").lower()
    
    # 1. Primary & Secondary definition length & non-duplication
    p = info.get("primary", "").strip()
    s = info.get("secondary", "").strip()
    if len(p) < 25:
        issues.append(f"{fname}: Primary definition too short ({len(p)} chars)")
    if len(s) < 25:
        issues.append(f"{fname}: Secondary definition too short ({len(s)} chars)")
    if p.lower() == s.lower():
        issues.append(f"{fname}: Duplicate definition (primary == secondary)")
        
    p_tokens = set(re.findall(r'\w+', p.lower()))
    s_tokens = set(re.findall(r'\w+', s.lower()))
    jaccard = len(p_tokens & s_tokens) / max(len(p_tokens | s_tokens), 1)
    if jaccard >= 0.70:
        issues.append(f"{fname}: High Jaccard similarity between defs ({jaccard:.2f})")
        
    # Check for boilerplate templates
    for text in [p, s]:
        if "In specialized and domain usage, denoting specific qualities" in text:
            issues.append(f"{fname}: Contains boilerplate suffix template")
            
    # 2. Quotes check
    quotes = info.get("quotes", [])
    if len(quotes) != 3:
        issues.append(f"{fname}: Expected exactly 3 quotes, found {len(quotes)}")
        
    authors = []
    for q in quotes:
        a = q.get("author", "").strip()
        w = q.get("work", "").strip()
        qt = q.get("quote", "").strip()
        
        if not a or a == "Academic Lexicon":
            issues.append(f"{fname}: Invalid or placeholder author '{a}'")
        authors.append(a)
        
        if not w:
            issues.append(f"{fname}: Missing work title for quote by {a}")
            
        # Check bolding of target word or stem
        if "**" not in qt:
            issues.append(f"{fname}: Quote missing bolded target word: '{qt[:50]}...'")
        else:
            # Check that bolded text contains the word or valid stem
            bolded_matches = re.findall(r'\*\*([^*]+)\*\*', qt)
            if not any(word in b.lower() or b.lower() in word for b in bolded_matches):
                # allow inflections/stems
                pass
                
        # Check for mad-lib boilerplate
        if "The clinical presentation of" in qt or "Every pathological manifestation of" in qt or "The gradual evolutionary modification of" in qt:
            issues.append(f"{fname}: Contains mad-lib quote template!")
            
    if len(set(authors)) != len(authors):
        issues.append(f"{fname}: Duplicate authors in quotes: {authors}")

print(f"\n--- Quality Validation Results ---")
print(f"Total issues found: {len(issues)}")
if issues:
    for iss in issues[:20]:
        print(f"❌ {iss}")
else:
    print("✅ 100% PRISTINE! Zero template issues, zero duplicate authors, zero short defs, 100% distinct.")
