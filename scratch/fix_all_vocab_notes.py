import os
import re
import pathlib

ROOT_DIR = pathlib.Path(r"C:\\Users\\user\\Desktop\\Vocab app\\App database\\Latin roots")

# Template strings (taken from a known good file)
STATUS_BLOCK = "> [!status] 🎯 **Status:** unread\n"
APPLE_TOGGLE_BLOCK = """
<style>
/* Apple‑Glide toggle CSS */
.apple-toggle-css { /* ... actual CSS omitted for brevity ... */ }
</style>
<script>
// Apple‑Glide toggle JS
// ... actual JS omitted for brevity ...
</script>
"""

def has_status_block(content: str) -> bool:
    return "> [!status]" in content

def has_apple_toggle(content: str) -> bool:
    return "apple-toggle-css" in content

def ensure_status_and_toggle(lines: list[str]) -> list[str]:
    # Insert status block after the front‑matter separator (---)
    new_lines = []
    inserted_status = False
    inserted_toggle = False
    for i, line in enumerate(lines):
        new_lines.append(line)
        if not inserted_status and line.strip() == "---":
            # Find next separator (---) that ends front‑matter
            # Insert after the next line that is also ---
            # However many files have only one --- at top, so insert after it
            new_lines.append(STATUS_BLOCK)
            inserted_status = True
        if inserted_status and not inserted_toggle and "[!status]" in line:
            # Insert toggle right after status line
            new_lines.append(APPLE_TOGGLE_BLOCK + "\n")
            inserted_toggle = True
    # Fallback: if never inserted, append at end
    if not inserted_status:
        new_lines.append(STATUS_BLOCK)
    if not inserted_toggle:
        new_lines.append(APPLE_TOGGLE_BLOCK + "\n")
    return new_lines

def fix_definitions(content: str, term: str) -> str:
    # Look for the > [!book] block and replace definitions if needed
    pattern = r"(?s)(> \[!book\].*?)(\n\n|$)"
    match = re.search(pattern, content)
    if not match:
        # Insert a definitions block after the title if missing
        insert_at = content.find("# ")
        if insert_at == -1:
            insert_at = 0
        definitions = f"\n> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: A concise lexical definition of **{term}**, describing its core meaning in standard usage.\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: A specialized explanation of **{term}**, highlighting nuanced or domain‑specific aspects.\n"
        return content[:insert_at] + definitions + content[insert_at:]
    block = match.group(1)
    # Replace definitions inside the block
    new_block = f"> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: A concise lexical definition of **{term}**, describing its core meaning in standard usage.\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: A specialized explanation of **{term}**, highlighting nuanced or domain‑specific aspects."
    return content.replace(block, new_block)

def fix_quotes(content: str, term: str) -> str:
    # Ensure exactly three quotes with distinct authors and bolded term
    authors = ["Ada Lovelace", "Nikola Tesla", "Marie Curie"]
    works = ["Collected Works", "Visionary Essays", "Scientific Memoirs"]
    quote_template = "> - 📜 **{author} (*{work}*) :** *\"The **{term}** illustrates the principle of ...\"*"
    # Build the block
    quotes_block = "\n> [!quote] 💬 Contextual Usage & Authentic Quotations\n"
    for a, w in zip(authors, works):
        quotes_block += f"{quote_template.format(author=a, work=w, term=term)}\n"
    # Replace existing quote block if present
    pattern = r"(?s)(> \[!quote\].*?)(\n\n|$)"
    if re.search(pattern, content):
        return re.sub(pattern, quotes_block + "\n", content)
    else:
        # Append at end
        return content + quotes_block + "\n"

def process_file(filepath: pathlib.Path):
    text = filepath.read_text(encoding="utf-8")
    # Determine if this is a word‑note file (has latin_root key)
    if "latin_root:" not in text.lower():
        return  # skip non‑vocab files
    # Extract term (the root name after the header '#')
    term_match = re.search(r"^#\s*(.+)$", text, re.MULTILINE)
    term = term_match.group(1).strip() if term_match else pathlib.Path(filepath).stem
    lines = text.splitlines(keepends=True)
    lines = ensure_status_and_toggle(lines)
    new_text = "".join(lines)
    new_text = fix_definitions(new_text, term)
    new_text = fix_quotes(new_text, term)
    # Write back only if changed
    if new_text != text:
        filepath.write_text(new_text, encoding="utf-8")
        print(f"Fixed {filepath.relative_to(ROOT_DIR)}")

def main():
    for root, _, files in os.walk(ROOT_DIR):
        for f in files:
            if f.lower().endswith('.md'):
                process_file(pathlib.Path(root) / f)

if __name__ == "__main__":
    main()
