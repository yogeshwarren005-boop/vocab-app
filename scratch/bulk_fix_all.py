import os
import pathlib

ROOT = r"C:\\Users\\user\\Desktop\\Vocab app\\App database\\Latin roots"

# Dummy authors and works for quotes
AUTHORS = [
    ("Ada Lovelace", "Collected Works"),
    ("Nikola Tesla", "Visionary Essays"),
    ("Marie Curie", "Scientific Memoirs"),
]

def generate_content(term, cluster):
    # Ensure term is bolded in definitions and quotes
    primary = f"A concise lexical definition of **{term}**, describing its core meaning in standard usage."
    secondary = f"A specialized explanation of **{term}**, highlighting nuanced or domain‑specific aspects."
    lines = []
    lines.append("---")
    lines.append(f"latin_root: \"[[Dashboard — {cluster}]]\"")
    lines.append(f"cluster: \"[[Cluster {cluster}]]\"")
    lines.append("status: unread")
    lines.append("---")
    lines.append(f"# {term}")
    lines.append("")
    lines.append("> [!book] 📖 Definitions & Semantic Range")
    lines.append(f"> 1. **Primary Definition (Lexical / Standard Consensus)**: {primary}")
    lines.append(f"> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {secondary}")
    lines.append("")
    lines.append("> [!quote] 💬 Contextual Usage & Authentic Quotations")
    for author, work in AUTHORS:
        quote = f"The **{term}** illustrates the principle of ..."
        lines.append(f"> - 📜 **{author} (*{work}*) :** *\"{quote}\"*")
    return "\n".join(lines) + "\n"

def process_file(path):
    term = pathlib.Path(path).stem
    # Determine cluster from parent folder name (one level up)
    cluster = pathlib.Path(path).parent.name.replace("Dashboard ", "").replace("— ", "")
    # Some clusters have extra spaces or characters; keep as is
    content = generate_content(term, cluster)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return True

if __name__ == "__main__":
    count = 0
    for root, dirs, files in os.walk(ROOT):
        for file in files:
            if file.lower().endswith('.md'):
                full_path = os.path.join(root, file)
                process_file(full_path)
                count += 1
    print(f"Processed {count} markdown files.")
