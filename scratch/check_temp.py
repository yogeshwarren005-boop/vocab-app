# -*- coding: utf-8 -*-
"""
Validation script for scratch/data_temp.json
Ensures all 86 words of Dashboard — temp pass 100% of the mandatory specifications.
"""
import os
import sys
import json
import re

sys.stdout.reconfigure(encoding="utf-8")

TARGET_WORDS = [
    'attemper', 'attempt', 'attempted', 'attempter', 'contemplate', 'contemplation',
    'contemplative', 'contemplativeness', 'contemporaneity', 'contemporaneous',
    'contemporaneously', 'contemporaneousness', 'contemporaries', 'contemporary',
    'contemporise', 'contemporize', 'contempt', 'contemptibility', 'contemptible',
    'contemptibly', 'contemptuous', 'contemptuously', 'contemptuousness', 'distemper',
    'extemporaneous', 'extemporaneously', 'extemporarily', 'extemporary', 'extempore',
    'extemporisation', 'extemporise', 'extemporization', 'extemporize', 'intemperance',
    'intemperate', 'intemperately', 'intemperateness', 'temp', 'temper', 'tempera',
    'temperament', 'temperamental', 'temperamentally', 'temperance', 'temperate',
    'temperately', 'temperateness', 'temperature', 'tempered', 'tempering', 'tempest',
    'tempest-swept', 'tempest-tossed', 'tempest-tost', 'tempestuous', 'tempestuousness',
    'templar', 'template', 'temple', 'templet', 'templetonia', 'tempo', 'temporal',
    'temporalis', 'temporality', 'temporally', 'temporalty', 'temporarily',
    'temporariness', 'temporary', 'temporise', 'temporiser', 'temporize', 'temporizer',
    'tempra', 'tempt', 'temptable', 'temptation', 'tempter', 'tempting', 'temptingly',
    'temptingness', 'temptress', 'tempura', 'untempered', 'untempting'
]

knownBannedPhrases = [
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

circular_re = re.compile(
    r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b',
    re.IGNORECASE
)

DATA_PATH = os.path.join("scratch", "data_temp.json")

def validate_temp_data():
    if not os.path.exists(DATA_PATH):
        print(f"ERROR: {DATA_PATH} does not exist.")
        sys.exit(1)

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    errors = []

    # Check key count
    if len(data) != len(TARGET_WORDS):
        errors.append(f"Expected {len(TARGET_WORDS)} entries, found {len(data)}")

    # Check all target words are present as keys with .md suffix
    for word in TARGET_WORDS:
        key = f"{word}.md"
        if key not in data:
            errors.append(f"Missing key: {key}")
            continue

        entry = data[key]
        p = entry.get("primary", "").strip()
        s = entry.get("secondary", "").strip()
        quotes = entry.get("quotes", [])

        # 1. Primary definition checks
        if len(p) < 25:
            errors.append(f"[{word}] Primary definition too short ({len(p)} < 25): '{p}'")
        if circular_re.search(p):
            errors.append(f"[{word}] Primary definition contains circular boilerplate formula: '{p}'")

        # 2. Secondary definition checks
        if len(s) < 25:
            errors.append(f"[{word}] Secondary definition too short ({len(s)} < 25): '{s}'")
        if circular_re.search(s):
            errors.append(f"[{word}] Secondary definition contains circular boilerplate formula: '{s}'")

        # 3. Jaccard token overlap between primary and secondary
        p_tokens = set(re.findall(r'\w+', p.lower()))
        s_tokens = set(re.findall(r'\w+', s.lower()))
        union_tokens = p_tokens | s_tokens
        jaccard = len(p_tokens & s_tokens) / max(len(union_tokens), 1)
        if jaccard >= 0.70:
            errors.append(f"[{word}] Jaccard overlap between primary and secondary is too high ({jaccard:.2f} >= 0.70)")

        # 4. Quotes checks: exactly 3 distinct quotations
        if len(quotes) != 3:
            errors.append(f"[{word}] Expected exactly 3 quotes, found {len(quotes)}")

        authors = []
        for i, q in enumerate(quotes):
            author = q.get("author", "").strip()
            work = q.get("work", "").strip()
            quote_text = q.get("quote", "").strip()
            authors.append(author)

            if len(author) < 3:
                errors.append(f"[{word}] Quote #{i+1} author too short ({len(author)} < 3): '{author}'")
            if len(work) < 2:
                errors.append(f"[{word}] Quote #{i+1} work too short ({len(work)} < 2): '{work}'")
            if "**" not in quote_text:
                errors.append(f"[{word}] Quote #{i+1} missing bolded target word (**...**): '{quote_text}'")

            # Check banned boilerplate phrases
            for phrase in knownBannedPhrases:
                if phrase.lower() in quote_text.lower() or phrase.lower() in author.lower() or phrase.lower() in work.lower():
                    errors.append(f"[{word}] Quote #{i+1} contains banned boilerplate phrase: '{phrase}'")
                if phrase.lower() in p.lower():
                    errors.append(f"[{word}] Primary definition contains banned phrase: '{phrase}'")
                if phrase.lower() in s.lower():
                    errors.append(f"[{word}] Secondary definition contains banned phrase: '{phrase}'")

        # Exactly 3 distinct real authors
        if len(set(authors)) != 3:
            errors.append(f"[{word}] Authors are not 3 distinct names: {authors}")

    if errors:
        print(f"FAILED: {len(errors)} errors found:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print(f"SUCCESS: All {len(TARGET_WORDS)} words passed all curation validation checks 100%!")

if __name__ == "__main__":
    validate_temp_data()
