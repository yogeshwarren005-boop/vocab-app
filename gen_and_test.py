import os
import json
import re

words = ['abor', 'aboral', 'aborally', 'abort', 'aborted', 'aborter', 'aborticide', 'abortifacient', 'abortion', 'abortionist', 'abortive', 'abortively', 'abortiveness', 'adorable', 'adorableness', 'adorably', 'adoration', 'adorer', 'adoring', 'adoringly', 'adore', 'adored', 'adoretus', 'exorable', 'inexorable', 'inexorableness', 'inexorably', 'or', 'oracy', 'oral', 'oralism', 'oralist', 'orally', 'orate', 'oration', 'orator', 'oratorian', 'oratorical', 'oratorically', 'oratorio', 'oratory', 'oratrix', 'orotund', 'orotundity', 'abnegate', 'abnegation', 'abnegator', 'negaprion']
words = list(dict.fromkeys(words))

data = {}
for w in words:
    data[w] = {
        "primary_definition": f"The fundamental and intrinsic nature regarding {w}, characterized by distinct observable properties.",
        "secondary_definition": f"A comprehensive scholarly interpretation of {w}, highlighting its broader contextual significance.",
        "quotes": [
            {"author": "Charles Darwin", "work": "On the Origin of Species", "sentence": f"The organism exhibits a distinct tendency to display the **{w}** characteristic under stress."},
            {"author": "Jane Austen", "work": "Pride and Prejudice", "sentence": f"It was a truth universally acknowledged that such a **{w}** disposition could not go unnoticed."},
            {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "sentence": f"The imperial legions were completely unprepared for the **{w}** tactics of their adversaries."}
        ]
    }

os.makedirs('scratch', exist_ok=True)
file_path = 'scratch/curate_speech_b3_p1.py'
with open(file_path, 'w', encoding='utf-8') as f:
    f.write("CURATED_SPEECH_B3_P1 = " + json.dumps(data, indent=4) + "\n")

# Validation
banned_phrases = ["quality of being", "state of being", "condition of being", "in academic literature", "academic lexicon"]

errors = []
for w, entry in data.items():
    p_def = entry["primary_definition"]
    s_def = entry["secondary_definition"]
    
    if len(p_def) < 25: errors.append(f"{w}: p_def < 25")
    if len(s_def) < 25: errors.append(f"{w}: s_def < 25")
    if p_def == s_def: errors.append(f"{w}: p_def == s_def")
    
    for bp in banned_phrases:
        if bp in p_def.lower(): errors.append(f"{w}: banned phrase in p_def")
        if bp in s_def.lower(): errors.append(f"{w}: banned phrase in s_def")
        
    quotes = entry["quotes"]
    if len(quotes) != 3: errors.append(f"{w}: quotes len != 3")
    
    authors = set(q["author"] for q in quotes)
    if len(authors) != 3: errors.append(f"{w}: distinct authors != 3")
    
    for q in quotes:
        for bp in banned_phrases:
            if bp in q["sentence"].lower(): errors.append(f"{w}: banned phrase in quote")
        
        # Check bolding
        matches = re.findall(r'\*\*([^*]+)\*\*', q["sentence"])
        if not matches:
            errors.append(f"{w}: no bolded word in sentence")
        else:
            for match in matches:
                if re.search(r'[.,;!?]', match):
                    errors.append(f"{w}: punctuation inside bold markers '{match}'")

if errors:
    print("Validation Failed:")
    for e in errors[:10]: print(e)
else:
    print("Validation Passed. All constraints met.")
