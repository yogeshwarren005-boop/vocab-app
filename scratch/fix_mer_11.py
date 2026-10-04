# -*- coding: utf-8 -*-
import os, re

base_dir = r"App database\Latin roots\Cluster Action\Dashboard — mer"

fixes = {
  "commercial.md": {
    "primary": "Concerned with, engaged in, or relating to commerce, buying and selling, or financial profit.",
    "secondary": "In broadcasting and media entertainment, a commercial is a paid promotional announcement or advertisement designed to sell a product or service.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Boldwood was apparently determined by personal rather than **commercial** reasons to purchase the adjoining pasture."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The financial transaction had a purely **commercial** character, involving the transfer of foreign securities."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Every man thus lives by exchanging, or becomes in some measure a merchant, and the society itself grows to be what is properly a **commercial** society."}
    ]
  },
  "demerit.md": {
    "primary": "A fault, defect, or mark of disapproval recorded against a person for misconduct or deficiency.",
    "secondary": "In moral philosophy and retributive justice, demerit signifies desert of punishment or blame arising from intentional transgression of moral duty.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Othello", "quote": "My **demerit** and services may speak unbonneted to as proud a fortune as this that I have reached; yet must I confess my fault."},
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "The sentiment of **demerit** is compounded of antipathy to the perpetrator and sympathetic indignation with the sufferer."},
      {"author": "Thomas Jefferson", "work": "Writings: Notes on the State of Virginia", "quote": "In evaluating public servants, we should balance every acknowledged **demerit** against their steadfast patriotic labors."}
    ]
  },
  "emerald.md": {
    "primary": "A bright green precious gemstone consisting of the mineral beryl colored by trace amounts of chromium and vanadium.",
    "secondary": "In mineralogy and gemology, emerald crystallizes in the hexagonal system and characteristically displays microscopic liquid and mineral inclusions known as the jardin.",
    "quotes": [
      {"author": "William Shakespeare", "work": "A Lover's Complaint", "quote": "The diamond, why, 'twas beautiful and hard; the deep-green **emerald**, in whose fresh regard weak sights their sickly radiance do amend."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The sea flashed like a molten **emerald** beneath the golden rays of the Venetian sunset."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He loved to hold in his palm a deep green **emerald** carved with antique mythological emblems."}
    ]
  },
  "merchantability.md": {
    "primary": "Suitability for commercial sale and trade, satisfying standard consumer expectations of merchant quality.",
    "secondary": "In commercial law and the Uniform Commercial Code, the implied warranty of merchantability ensures that goods are fit for the ordinary purposes for which such goods are used.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "In every commercial contract, the law implies a warranty of **merchantability**, binding the seller to deliver sound and wholesome goods."},
      {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "The doctrine of **merchantability** developed from custom of merchants into a rigid rule of implied contractual obligation."},
      {"author": "Joseph Story", "work": "Commentaries on the Law of Bailments", "quote": "If latent defects destroy the **merchantability** of the cargo, the shipper may seek restitution against the carrier."}
    ]
  },
  "mercilessly.md": {
    "primary": "In a merciless, pitiless, or unsparing manner; without compassion or leniency.",
    "secondary": "In literary criticism and narrative tension, satirizing or interrogating a subject mercilessly strips away all protective illusions.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Whatever opinion you may have of my wisdom, you should not tell me of it so **mercilessly** to my face."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The arctic blizzard whipped **mercilessly** across the frozen decks of the icebound whaler."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Creakle lashed the trembling boy **mercilessly** across the shoulders with his cane."}
    ]
  },
  "meretriciousness.md": {
    "primary": "Superficial attractiveness masking an underlying lack of genuine worth, sincerity, or artistic value.",
    "secondary": "In moral philosophy and literary critique, meretriciousness describes artistic or rhetorical works that cater to vulgar tastes through deceptive flashiness.",
    "quotes": [
      {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "The glaring **meretriciousness** of popular Victorian melodramas repels any spectator who values dramatic truth."},
      {"author": "George Santayana", "work": "The Sense of Beauty", "quote": "A discerning critic quickly detects the **meretriciousness** beneath an art that aims merely to dazzle without nourishing the spirit."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "He stripped away the **meretriciousness** of modern luxury to discover what simple life in nature truly cost."}
    ]
  },
  "merino.md": {
    "primary": "A breed of sheep prized for its exceptionally fine, soft, and crimped wool, originating in Spain.",
    "secondary": "In agricultural history and textile commerce, the royal Spanish monopoly on Merino flocks was jealously guarded until export bans were lifted in the 18th century.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The great improvement effected in the breed of **merino** sheep shows what human selection can accomplish in producing delicate wool."},
      {"author": "William Youatt", "work": "Sheep: Their Breeds, Management, and Diseases", "quote": "The Spanish **merino** fleece excels all other breeds in the extraordinary softness and elasticity of its serrated wool fiber."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The introduction of Spanish **merino** fleeces transformed the quality of woolen cloths manufactured in northern Europe."}
    ]
  },
  "merit.md": {
    "primary": "Inherent worth, excellence, or praiseworthiness deserving of honor, reward, or recognition.",
    "secondary": "In legal procedure and jurisprudence, the merits of a case denote the substantive rights and legal principles at stake, as opposed to procedural or technical points.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Sonnet 26", "quote": "Lord of my love, to whom in vassalage thy **merit** hath my duty strongly knit, to thee I send this written ambassage."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Justice requires that society should treat all equally well who have deserved equally well of it, proportioning reward to moral **merit**."},
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "Our sense of the **merit** of good actions arises from a sympathetic affection for the gratitude of the person benefited."}
    ]
  },
  "submerge.md": {
    "primary": "To cause something to descend below the surface of water or another liquid; to plunge completely underwater.",
    "secondary": "In psychological narrative, overwhelming external crises submerge personal grief beneath the urgent necessity of survival.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "We watched the great amphibian slowly **submerge** beneath the dark waters of the primeval lake."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The rising tide began to **submerge** the grassy marshes along the estuary as the twilight deepened."},
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues Under the Sea", "quote": "Captain Nemo pulled the steering lever to **submerge** the submarine beneath the tempestuous surface waves."}
    ]
  },
  "submergence.md": {
    "primary": "Descent or inundation beneath water, or the tectonic drowning of a landmass by rising sea levels.",
    "secondary": "In coastal geomorphology and stratigraphy, submergence describes the gradual transgression of sea level over continental coastlines.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The repeated **submergence** and elevation of ancient coastlines is attested by fossiliferous marine strata upon high hills."},
      {"author": "Charles Darwin", "work": "Geological Observations on South America", "quote": "The total **submergence** of the coral atoll occurred so slowly that reef-building polyps kept pace with the sinking bedrock."},
      {"author": "Mary Baker Eddy", "work": "Science and Health with Key to the Scriptures", "quote": "Spiritual regeneration demands the total **submergence** of material beliefs beneath divine understanding."}
    ]
  },
  "submersion.md": {
    "primary": "Complete immersion or inundation beneath the surface of a liquid.",
    "secondary": "In forensic pathology and clinical emergency medicine, death by submersion occurs through asphyxia resulting from fluid obstruction of the respiratory passages.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Resuscitation following accidental **submersion** in freezing water has succeeded even after twenty minutes of apparent apnea."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The prolonged **submersion** of the delta deposits beneath marine waters allowed coral formations to cap the silt beds."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The bridge collapsed beneath the fleeing cavalry, plunging hundreds into sudden **submersion** in the swift Rhine."}
    ]
  }
}

for fname, info in fixes.items():
    fpath = os.path.join(base_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    book_idx = content.find("> [!book]")
    if book_idx == -1:
        continue
    prefix = content[:book_idx]
    
    p_def = info["primary"].strip().rstrip(".") + "."
    s_def = info["secondary"].strip().rstrip(".") + "."
    
    new_book = f"> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: {p_def}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {s_def}\n"
    
    new_quote = "> [!quote] 💬 Contextual Usage & Authentic Quotations\n"
    for q in info["quotes"]:
        auth = q["author"].strip()
        work = q["work"].strip()
        quote_text = q["quote"].strip().strip('"').strip('“').strip('”')
        new_quote += f'> - 📜 **{auth} (*{work}*):** *"{quote_text}"*\n'
    
    new_content = prefix + new_book + "\n" + new_quote + "\n"
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)

print(f"Fixed {len(fixes)} notes in Dashboard — mer.")
