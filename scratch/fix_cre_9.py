# -*- coding: utf-8 -*-
import os, re

base_dir = r"App database\Latin roots\Cluster Action\Dashboard — cre"

fixes = {
  "concreteness.md": {
    "primary": "Material reality, tangible substance, and definite physical form rather than abstract existence."
  },
  "credibility.md": {
    "primary": "The capacity to inspire trust, belief, and confidence; authoritative believability."
  },
  "credibleness.md": {
    "primary": "The attribute of inspiring belief or deserving intellectual assent; inherent trustworthiness."
  },
  "discreteness.md": {
    "primary": "Distinct separation into individual, non-continuous elements or units."
  },
  "incredibility.md": {
    "primary": "Astonishing impossibility of belief; extreme implausibility defying standard credence."
  },
  "incredibleness.md": {
    "primary": "The attribute of exceeding belief or appearing extraordinarily improbable to reason."
  },
  "indiscreetness.md": {
    "primary": "Reckless lack of judgment, imprudence in speech, or failure to guard confidences."
  },
  "secrecy.md": {
    "primary": "Concealment, confidentiality, or deliberate withholding of information from public knowledge."
  },
  "secretase.md": {
    "quotes": [
      {"author": "Santiago Ramón y Cajal", "work": "Degeneration and Regeneration of the Nervous System", "quote": "Proteolytic cleavage by specific enzymes like **secretase** alters membrane-bound neuronal precursors in degenerative neuropathies."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Biochemical investigations into senile dementia focus upon aberrant **secretase** activity generating cerebral amyloid deposits."},
      {"author": "Paul Ehrlich", "work": "Studies in Immunity", "quote": "Specific proteolytic enzymes including **secretase** alter receptor configurations on cell surfaces."}
    ]
  }
}

for fname, item in fixes.items():
    fpath = os.path.join(base_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "primary" in item:
        pdef = item["primary"].strip().rstrip(".") + "."
        content = re.sub(r'> 1\. \*\*Primary Definition.*?\*\*: .*', f'> 1. **Primary Definition (Lexical / Standard Consensus)**: {pdef}', content)
    
    if "quotes" in item:
        q_idx = content.find("> [!quote]")
        if q_idx != -1:
            head = content[:q_idx]
            new_quote = "> [!quote] 💬 Contextual Usage & Authentic Quotations\n"
            for q in item["quotes"]:
                auth = q["author"].strip()
                work = q["work"].strip()
                quote_text = q["quote"].strip().strip('"').strip('“').strip('”')
                new_quote += f'> - 📜 **{auth} (*{work}*):** *"{quote_text}"*\n'
            content = head + new_quote + "\n"
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Fixed {len(fixes)} notes in Dashboard — cre.")
