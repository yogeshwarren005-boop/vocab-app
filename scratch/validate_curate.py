import re, sys
sys.stdout.reconfigure(encoding='utf-8')


CIRCULAR_REGEX = re.compile(
    r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b',
    re.IGNORECASE
)
BANNED_PHRASES = [
    "in academic literature",
    "academic lexicon",
    "morphological & etymological survey",
    "designates the state",
    "designates the quality"
]

def validate_curated_dict(curated_dict, name="Batch"):
    errors = 0
    total = len(curated_dict)
    for word, data in curated_dict.items():
        w_errs = []
        etym = data.get("etymology", "")
        p_def = data.get("primary_definition", "")
        s_def = data.get("secondary_definition", "")
        quotes = data.get("quotes", [])

        if len(etym) < 20:
            w_errs.append(f"Etymology too short: {len(etym)}")
        if len(p_def) < 25:
            w_errs.append(f"Primary def too short: {len(p_def)}")
        if len(s_def) < 25:
            w_errs.append(f"Secondary def too short: {len(s_def)}")
        if p_def.strip() == s_def.strip():
            w_errs.append("Primary and secondary defs are identical")
        
        if CIRCULAR_REGEX.search(p_def):
            w_errs.append("Primary def circular")
        if CIRCULAR_REGEX.search(s_def):
            w_errs.append("Secondary def circular")

        for bp in BANNED_PHRASES:
            if bp in p_def.lower() or bp in s_def.lower() or bp in etym.lower():
                w_errs.append(f"Banned phrase '{bp}' in defs/etym")

        if len(quotes) != 3:
            w_errs.append(f"Expected 3 quotes, got {len(quotes)}")
        else:
            authors = []
            for i, q in enumerate(quotes):
                a = q.get("author", "").strip()
                wrk = q.get("work", "").strip()
                s = q.get("sentence", "").strip()
                authors.append(a)
                if not a or not wrk or not s:
                    w_errs.append(f"Quote {i+1} missing fields")
                
                # Check target word bolded: **word** or **Word**
                # Clean word for matching: handle hyphens
                clean_w = word.replace('-', r'[-\s]?')
                bold_pat = re.compile(rf'\*\*{clean_w}[a-z]*\*\*', re.IGNORECASE)
                if not bold_pat.search(s):
                    # Check if exact word without regex trick
                    if f"**{word}**" not in s and f"**{word.capitalize()}**" not in s and f"**{word.upper()}**" not in s:
                        w_errs.append(f"Target word '{word}' not bolded in quote {i+1}: {s[:60]}...")

                for bp in BANNED_PHRASES:
                    if bp in s.lower() or bp in a.lower():
                        w_errs.append(f"Banned phrase '{bp}' in quote {i+1}")

            if len(set(authors)) != 3:
                w_errs.append(f"Duplicate authors: {authors}")

        if w_errs:
            errors += 1
            print(f"❌ {word}:")
            for e in w_errs:
                print(f"   - {e}")

    print(f"\n[{name}] Total: {total}, Errors: {errors}, Passed: {total - errors} ({((total-errors)/total)*100:.1f}%)")
    return errors == 0

if __name__ == "__main__":
    from curate_body_b4_p1a import CURATED_P1A
    from curate_body_b4_p1b import CURATED_P1B
    from curate_body_b4_p2a import CURATED_P2A
    from curate_body_b4_p2b import CURATED_P2B
    ok_1a = validate_curated_dict(CURATED_P1A, "Body Batch 4 Part 1a (lab 1-34)")
    ok_1b = validate_curated_dict(CURATED_P1B, "Body Batch 4 Part 1b (lab 35-67)")
    ok_2a = validate_curated_dict(CURATED_P2A, "Body Batch 4 Part 2a (man 1-47)")
    ok_2b = validate_curated_dict(CURATED_P2B, "Body Batch 4 Part 2b (pod_foot 1-24)")
    if ok_1a and ok_1b and ok_2a and ok_2b:
        print("\nAll 138 words of Batch 4 (lab + man + pod_foot) PASSED validation!")



