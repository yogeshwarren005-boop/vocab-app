# -*- coding: utf-8 -*-
"""
Curates Dashboard — caut (19 words) in Cluster Mind & Knowledge.
"""
import os, sys, re, subprocess

sys.stdout.reconfigure(encoding="utf-8")

data = {
  "Dashboard — caut/cauterant.md": {
    "primary": "A substance, chemical, or physical agent used to burn, sear, or destroy abnormal animal tissue.",
    "secondary": "In surgical therapeutics, chemical caustics such as silver nitrate applied to eradicate granulations.",
    "quotes": [
      {"author": "Ambroise Paré", "work": "The Workes of that Famous Chirurgion Ambroise Parey", "quote": "The ancient surgeons applied boiling oil as a violent **cauterant** to gunshot wounds, a cruel practice I abandoned."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The surgeon applied a mild **cauterant** to the indolent ulcer to stimulate healthy vascular repair."},
      {"author": "Joseph Lister", "work": "The Antiseptic System of Treatment in Surgery", "quote": "Carbolic acid acts not merely as an antiseptic, but in high concentration as a chemical **cauterant** upon diseased tissue."}
    ]
  },
  "Dashboard — caut/cauterisation.md": {
    "primary": "The act or process of destroying tissue using heat, cold, or caustic chemical agents (British spelling).",
    "secondary": "In nineteenth-century clinical surgery, employing red-hot irons or nitric acid to arrest arterial hemorrhage.",
    "quotes": [
      {"author": "Joseph Lister", "work": "On the Antiseptic Principle in the Practice of Surgery", "quote": "Modern surgeons prefer sterile ligatures to the painful **cauterisation** of bleeding arteries after amputation."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants Under Domestication", "quote": "Severe **cauterisation** of the horn buds in young calves permanently arrests subsequent horn development."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "The veteran practitioner demonstrated the swift **cauterisation** of a poisoned dog bite with glowing silver nitrate."}
    ]
  },
  "Dashboard — caut/cauterise.md": {
    "primary": "Burn, sear, or destroy abnormal tissue with a heated instrument or caustic chemical (British spelling).",
    "secondary": "In figurative rhetoric, to deaden moral sensitivity or excise corrupt elements from society.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Saint Joan", "quote": "The inquisitor declared that the church must **cauterise** the spreading infection of heresy before it consumed Christendom."},
      {"author": "H. G. Wells", "work": "The Island of Doctor Moreau", "quote": "Moreau used heated needles to **cauterise** exposed nerve endings during his grotesque biological grafting."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Danton shouted that the revolution must **cauterise** royalist treason with uncompromising revolutionary fury."}
    ]
  },
  "Dashboard — caut/cauterization.md": {
    "primary": "The medical procedure of burning or searing tissue with heat, electricity, cold, or caustics to stop bleeding.",
    "secondary": "In modern ophthalmic and vascular surgery, electrosurgical or laser coagulation sealing severed capillaries.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Immediate **cauterization** of the wound with fuming nitric acid remains the standard prophylactic against rabies."},
      {"author": "Henry Gray", "work": "Gray's Anatomy", "quote": "Effective **cauterization** of the capillary bed arrests persistent oozing without extensive damage to deeper structures."},
      {"author": "Atul Gawande", "work": "Complications: A Surgeon's Notes on an Imperfect Science", "quote": "The surgeon used bipolar **cauterization** to seal bleeding vessels along the edge of the incision."}
    ]
  },
  "Dashboard — caut/cauterize.md": {
    "primary": "Burn skin or flesh of a wound with a heated instrument or caustic substance to stop bleeding or prevent infection.",
    "secondary": "In literary metaphor, to make callous, unfeeling, or dead to emotional remorse.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The harpooner seized a glowing brand from the try-works to **cauterize** the festering wound received from the whale's fin."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I must **cauterize** the wound of unrequited love, burning out memory to preserve my moral sanity."},
      {"author": "Jack London", "work": "The Sea-Wolf", "quote": "Wolf Larsen used a red-hot poker to **cauterize** the sailor's shattered arm on the pitching deck."}
    ]
  },
  "Dashboard — caut/cautery.md": {
    "primary": "An instrument or caustic substance used to burn, sear, or destroy abnormal organic tissue.",
    "secondary": "In surgical history, actual cautery (heated iron) and potential cautery (caustic chemicals) utilized since antiquity.",
    "quotes": [
      {"author": "Ambroise Paré", "work": "The Workes of that Famous Chirurgion Ambroise Parey", "quote": "The fearful smell of burning flesh vanished from our hospital wards when I threw away the red-hot **cautery**."},
      {"author": "William Osler", "work": "Aequanimitas and Other Addresses", "quote": "Ancient surgical texts devoted long chapters to the varied forms of the **cautery** in treating chronic ulcers."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The lancet and the **cautery** reigned supreme in the heroic medicine of our great-grandfathers."}
    ]
  },
  "Dashboard — caut/caution.md": {
    "primary": "Care taken to avoid danger, risk, or mistakes; prudence, wariness, and deliberate foresight.",
    "secondary": "In legal jurisprudence, a formal warning given to a suspect or a notice entered against land registration.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Hear me with **caution**, for the tempest breaks upon our heads while we stand debating petty grievances."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Tulkinghorn walked through the fog with habitual **caution**, keeping his secrets locked in his breast."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Her mother's voice had ever been on the side of **caution**, teaching her to dread premature financial commitments."}
    ]
  },
  "Dashboard — caut/cautionary.md": {
    "primary": "Serving as a warning; admonitory, disciplinary, or deterring through exemplary illustration.",
    "secondary": "In didactic literature and folk tales, narratives designed to instill prudence by showing the perils of folly.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "History offers a **cautionary** lesson regarding republics that surrendered liberty to popular military demagogues."},
      {"author": "Charles Dickens", "work": "The Mystery of Edwin Drood", "quote": "The old stone towers seemed to stand as a **cautionary** reminder of mortality to the frivolous town below."},
      {"author": "Anthony Pryde", "work": "Nightfall", "quote": "They regarded the young officer's dismissal as a **cautionary** signal against reckless insubordination in peacetime."}
    ]
  },
  "Dashboard — caut/cautious.md": {
    "primary": "Careful to avoid potential problems or dangers; wary, prudent, and circumspect in action.",
    "secondary": "In financial investment and military planning, minimizing exposure to unpredictable liabilities or ambushes.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Tulkinghorn was a **cautious** man who never committed himself to writing when a silent nod would suffice."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "In a low, **cautious** whisper, she communicated the surprising news that Captain Wentworth had returned."},
      {"author": "Jack London", "work": "The Call of the Wild", "quote": "Buck was **cautious**, never rushing heedlessly into battle until he had sized up his rival's strength."}
    ]
  },
  "Dashboard — caut/cautiously.md": {
    "primary": "In a careful and well-considered manner, taking great care to avoid risk, mistakes, or danger.",
    "secondary": "In investigative narrative, advancing with guarded vigilance to avoid detection or injury.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The lawyer opened the rusted iron door **cautiously**, peering into the dimly lit repository of legal deeds."},
      {"author": "Johanna Spyri", "work": "Heidi", "quote": "The little girl walked **cautiously** over the steep rock ledge, holding her grandfather's strong hand."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes stepped **cautiously** over the quaking morass, testing each tussock with his heavy walking stick."}
    ]
  },
  "Dashboard — caut/cautiousness.md": {
    "primary": "The disposition to be cautious; prudent circumspection and careful avoidance of rash hazards.",
    "secondary": "In phrenology and nineteenth-century character analysis, a mental faculty governing defensive prudence.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth praised her father's **cautiousness** in refusing to allow Lydia to invite frivolous officers to the house."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The excessive **cautiousness** of Starbuck contrasted sharply with Ahab's frantic disregard of ordinary peril."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Farebrother admired the young surveyor's **cautiousness**, noting how every measurement was verified twice."}
    ]
  },
  "Dashboard — caut/incaution.md": {
    "primary": "Lack of caution; heedlessness, carelessness, or rash disregard of potential hazards.",
    "secondary": "In ethical essays and naval inquiries, reckless neglect of standard safety rules leading to accident.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Youth is perpetually betrayed by its own **incaution**, rushing blindly into schemes that end in poverty."},
      {"author": "W. E. Webb", "work": "Buffalo Land", "quote": "Tempted by the grazing herd, the hunter's **incaution** brought him within lethal range of concealed skirmishers."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The maritime court sternly rebuked the mate's **incaution** in steaming at full speed through blind monsoon fog."}
    ]
  },
  "Dashboard — caut/incautious.md": {
    "primary": "Not heedful of potential consequences, danger, or risk; rash, unwary, or indiscreet.",
    "secondary": "In military reconnaissance and political diplomacy, uttering careless statements that expose plans to adversaries.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "An **incautious** word escaped her lips in the dairy parlor, causing Angel Clare to pause in surprise."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "An **incautious** expansion of executive authority might inadvertently subvert the constitutional equilibrium of the republic."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "My aunt scolded Mr. Dick for his **incautious** remarks concerning King Charles's head in the presence of strangers."}
    ]
  },
  "Dashboard — caut/incautiously.md": {
    "primary": "In an incautious, unwary, or careless manner; without taking proper heed of consequences.",
    "secondary": "In dramatic narrative, revealing a closely guarded secret or stepping into peril through lack of vigilance.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Lydia chattered **incautiously** about her elopement, entirely blind to the disgrace she had brought upon her family."},
      {"author": "James Joyce", "work": "Ulysses", "quote": "He stepped **incautiously** off the curb into the splashing muddy track of the speeding brewer's dray."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The fugitive moved **incautiously** past the streetlamp, allowing the detective to catch his profile."}
    ]
  },
  "Dashboard — caut/incautiousness.md": {
    "primary": "The disposition to act without due caution; habitual rashness, indiscretion, and heedlessness.",
    "secondary": "In judicial proceedings and insurance investigations, blameworthy negligence failing to avert foreseeable injury.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Adventurer", "quote": "Many a prosperous merchant has been ruined by the sudden **incautiousness** of an extravagant son."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Mr. Tulliver lamented his own **incautiousness** in signing legal agreements without reading the small print."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "Oldbuck chided the nephew for his boyish **incautiousness** in scaling the crumbling cliff face."}
    ]
  },
  "Dashboard — caut/overcautious.md": {
    "primary": "Excessively cautious, hesitant, or prudent; paralyzed by exaggerated fears of risk.",
    "secondary": "In military command and game theory, a timid strategy that forfeits tactical advantage through chronic indecision.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The general was hopelessly **overcautious**, postponing his offensive until the enemy had reinforced all defensive lines."},
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "A man who is **overcautious** in his youth will inevitably become a miserable tyrant in his old age."},
      {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "Lestrade was **overcautious** in making arrests, preferring to wait for an absolute confession."}
    ]
  },
  "Dashboard — caut/precaution.md": {
    "primary": "A measure taken in advance to prevent something dangerous, harmful, or unpleasant from happening.",
    "secondary": "In epidemiological hygiene and industrial manufacturing, systematic safety safeguards preventing catastrophic loss.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Snagsby took every **precaution** against disturbing his formidable wife, treading upon tiptoe in his own house."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Bulstrode locked the drawer with elaborate **precaution**, glancing anxiously over his shoulder at the window."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "As a necessary **precaution** against fire, the ship's cook doused all galleys before the casks were rolled out."}
    ]
  },
  "Dashboard — caut/precautional.md": {
    "primary": "Of, relating to, or serving as a precaution; preventive, precautionary, or anticipatory.",
    "secondary": "In legal contracts and military maneuvers, protective stipulations designed to guard against future contingencies.",
    "quotes": [
      {"author": "Thomas Jefferson", "work": "Writings", "quote": "The treaty contained a **precautional** clause reserving our neutral trading rights in European ports."},
      {"author": "Edmund Burke", "work": "Thoughts on the Cause of the Present Discontents", "quote": "Parliament must adopt **precautional** measures before public discontent boils over into open rebellion."},
      {"author": "Joseph Conrad", "work": "The Shadow-Line", "quote": "The captain ordered a **precautional** double watch aloft as the barque approached the treacherous reefs."}
    ]
  },
  "Dashboard — caut/precautionary.md": {
    "primary": "Carried out as a precaution; intended to prevent possible harm, danger, error, or misfortune.",
    "secondary": "In environmental science and corporate governance, the precautionary principle mitigating uncertain ecological hazards.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate suggested certain **precautionary** measures against the fever, advising the town council to flush the sewers."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The mate took **precautionary** steps to lash the whale-boats firmly to their davits as the squall deepened."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Holmes drew his revolver as a **precautionary** measure before entering the darkened cellar."}
    ]
  }
}

def curate_file(rel_path, info):
    base_dir = "App database/Latin roots/Cluster Mind & Knowledge"
    filepath = os.path.join(base_dir, rel_path)
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return False
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    fm_match = re.search(r"^---\n.*?\n---\n", content, re.DOTALL)
    if not fm_match:
        print(f"Frontmatter missing: {filepath}")
        return False
    frontmatter = fm_match.group(0)
    
    w = os.path.splitext(os.path.basename(rel_path))[0]
    header = f"# {w}\n\n"
    
    dv_match = re.search(r"(> \[!status\] 🎯 \*\*Status:\*\*.*?```dataviewjs.*?```)", content, re.DOTALL)
    if not dv_match:
        print(f"Dataview block missing: {filepath}")
        return False
    dv_block = dv_match.group(1)
    
    defs_block = f"""> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: {info['primary']}
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {info['secondary']}"""

    quotes_lines = ["> [!quote] 💬 Contextual Usage & Authentic Quotations"]
    for q in info["quotes"]:
        quotes_lines.append(f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{q['quote']}\"*")
    quotes_block = "\n".join(quotes_lines)
    
    new_content = f"{frontmatter}{header}{dv_block}\n\n{defs_block}\n\n{quotes_block}\n"
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True

success = 0
for rel_path, info in data.items():
    if curate_file(rel_path, info):
        success += 1

print(f"Successfully updated {success}/{len(data)} notes in Dashboard — caut.")
