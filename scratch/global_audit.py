import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

target_dir = r"App database/Latin roots"

known_banned = [
    "In specialized and domain usage, denoting specific qualities",
    "In technical and systematic terminology, the action",
    "In functional and operational contexts, an agent",
    "The clinical presentation of",
    "Every pathological manifestation of",
    "The gradual evolutionary modification of",
    "In academic literature,",
    "Academic Lexicon",
    "Classic Author"
]

circular_re = re.compile(r"\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b", re.I)
p_def_re = re.compile(r"1\.\s*\*\*([^*]+)\*\*:\s*([^\r\n]+)")
s_def_re = re.compile(r"2\.\s*\*\*([^*]+)\*\*:\s*([^\r\n]+)")
auth_re = re.compile(r"📜\s*\*\*([^*]+?)\s*(?:\(\*([^*]+?)\*\):?\*\*|\*\*\s*\(\*([^*]+?)\*\):?)")
colon_re = re.compile(r":\*\*\s*(.+)$")

clusters = [d for d in os.listdir(target_dir) if os.path.isdir(os.path.join(target_dir, d)) and d.startswith("Cluster")]
clusters.sort()

cluster_stats = {}
total_words = 0
total_pristine = 0
total_problems = 0

for c in clusters:
    c_path = os.path.join(target_dir, c)
    c_words = 0
    c_problems = 0
    dashboards = {}
    for root, dirs, files in os.walk(c_path):
        d_name = os.path.basename(root)
        for f in files:
            if not f.endswith(".md"):
                continue
            if f.startswith("Dashboard —") or f.startswith("Word Triage") or f.startswith("Cluster") or f.startswith("Semantic Field"):
                continue
            word_path = os.path.join(root, f)
            c_words += 1
            with open(word_path, "r", encoding="utf-8", errors="ignore") as fp:
                content = fp.read()
            
            issues = []
            if not content.startswith("---"):
                issues.append("fm")
            if "> [!status]" not in content:
                issues.append("status")
            if "> [!book]" not in content:
                issues.append("book")
            if "apple-toggle-css" not in content or "apple-c" not in content:
                issues.append("toggle")
            
            p_m = p_def_re.search(content)
            s_m = s_def_re.search(content)
            if not p_m:
                issues.append("no_p_def")
            else:
                p_text = p_m.group(2).strip()
                if len(p_text) < 25:
                    issues.append("p_def_short")
                if circular_re.search(p_text):
                    issues.append("p_def_circ")
            
            if not s_m:
                issues.append("no_s_def")
            else:
                s_text = s_m.group(2).strip()
                if len(s_text) < 25:
                    issues.append("s_def_short")
                if circular_re.search(s_text):
                    issues.append("s_def_circ")
                
            if p_m and s_m:
                p_tokens = set(re.findall(r"\w+", p_m.group(2).lower()))
                s_tokens = set(re.findall(r"\w+", s_m.group(2).lower()))
                intersect = p_tokens & s_tokens
                union = p_tokens | s_tokens
                jaccard = len(intersect) / max(len(union), 1)
                if jaccard >= 0.70:
                    issues.append("jaccard")
                
            for b in known_banned:
                if b in content:
                    issues.append("banned")
                
            quote_parts = content.split("> [!quote]")
            if len(quote_parts) < 2:
                issues.append("no_quote")
            else:
                qlines = [l.strip() for l in quote_parts[1].split("\n") if l.strip().startswith(">") and "📜" in l]
                if len(qlines) != 3:
                    issues.append(f"quote_count_{len(qlines)}")
                authors = []
                for ql in qlines:
                    am = auth_re.search(ql)
                    if not am:
                        issues.append("quote_auth_fmt")
                    else:
                        auth = am.group(1).strip()
                        work = (am.group(2) or am.group(3) or "").strip()
                        authors.append(auth)
                        if len(auth) < 3 or len(work) < 2:
                            issues.append("short_auth")
                    col_m = colon_re.search(ql)
                    qbody = col_m.group(1) if col_m else ql
                    if "**" not in qbody:
                        issues.append("no_bold")
                if len(set(authors)) < len(qlines):
                    issues.append("dup_auth")
                    
            if issues:
                c_problems += 1
                dashboards[d_name] = dashboards.get(d_name, 0) + 1
                
    total_words += c_words
    total_problems += c_problems
    pristine_words = c_words - c_problems
    total_pristine += pristine_words
    cluster_stats[c] = {
        "total": c_words,
        "pristine": pristine_words,
        "problems": c_problems,
        "failed_dashboards": len(dashboards)
    }

print(f"GLOBAL STATUS: Total words: {total_words}, Pristine: {total_pristine} ({(total_pristine/total_words)*100:.2f}%), Problems: {total_problems}")
print("\n=== CLUSTER BREAKDOWN ===")
for c, st in cluster_stats.items():
    if st["problems"] == 0:
        icon = "PASS (100% PRISTINE)"
    else:
        icon = f"FAIL: {st['problems']} issues across {st['failed_dashboards']} dashboards"
    print(f"{c:40}: {st['pristine']:4d}/{st['total']:4d} | {icon}")
