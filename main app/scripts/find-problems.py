import os
import re
import json

base_dir = r"App database\Greek roots\Cluster Light & Vision"

problems = []

for root, dirs, files in os.walk(base_dir):
    for f in files:
        if (
            f.endswith(".md")
            and not f.startswith("Dashboard —")
            and not f.startswith("Word Triage —")
            and not f.startswith("Cluster")
            and not f.startswith("Semantic Field")
        ):
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, base_dir).replace("\\", "/")
            with open(full_path, "r", encoding="utf-8") as file:
                content = file.read()

            issues = []
            status_pos = content.find("> [!status]")
            book_pos = content.find("> [!book]")
            if status_pos == -1:
                issues.append("Missing [!status] block")
            if book_pos == -1:
                issues.append("Missing [!book] block")
            if status_pos != -1 and book_pos != -1 and status_pos > book_pos:
                issues.append("Status block is below [!book]")

            p_match = re.search(r"1\.\s*\*\*([^*]+)\*\*:\s*([^\r\n]+)", content)
            s_match = re.search(r"2\.\s*\*\*([^*]+)\*\*:\s*([^\r\n]+)", content)
            if not p_match:
                issues.append("Missing Primary Definition")
            if not s_match:
                issues.append("Missing Secondary Definition")
            if p_match and s_match:
                if p_match.group(2).strip().lower() == s_match.group(2).strip().lower():
                    issues.append("Duplicate Definition")

            if "> [!quote]" not in content:
                issues.append("Missing [!quote] section")
            else:
                quote_section = content.split("> [!quote]")[1]
                quote_lines = [
                    l for l in quote_section.split("\n")
                    if re.match(r"^(?:>\s*)?-\s*📜", l.strip())
                ]
                if len(quote_lines) < 3:
                    issues.append(f"Only {len(quote_lines)} quotes")

                authors = []
                has_placeholder = False
                for line in quote_lines:
                    if "Academic Lexicon" in line:
                        has_placeholder = True
                    auth_match = re.search(r"-\s*📜\s*\*\*([^*(:]+)", line)
                    if auth_match:
                        authors.append(auth_match.group(1).strip())

                if has_placeholder:
                    issues.append("Placeholder author")
                if len(set(authors)) < len(quote_lines):
                    issues.append(f"Duplicate authors: {authors}")

            if issues:
                problems.append({"file": rel_path, "issues": issues})

with open("main app/scripts/light-remaining-problems.json", "r", encoding="utf-8") as f:
    remaining_list = [p.replace("\\", "/") for p in json.load(f)]

print(f"Total problems found by audit: {len(problems)}")
print(f"In light-remaining-problems.json: {len(remaining_list)}")

prob_files = {p["file"] for p in problems}
rem_files = set(remaining_list)

extra_problems = [p for p in problems if p["file"] not in rem_files]
print(f"Problems NOT in light-remaining-problems.json ({len(extra_problems)}):")
for p in extra_problems:
    print(f"  {p['file']}: {p['issues']}")
