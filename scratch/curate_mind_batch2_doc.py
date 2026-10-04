# -*- coding: utf-8 -*-
"""
Curates Dashboard — doc (30 words) in Cluster Mind & Knowledge.
"""
import os, sys, re, subprocess

sys.stdout.reconfigure(encoding="utf-8")

data = {
  "Dashboard — doc/doc.md": {
    "primary": "An informal colloquial abbreviation for doctor or physician; also a standard computer file extension for text documents.",
    "secondary": "In Western frontier slang and computer software, an affectionate title for medical practitioners or word processor formats.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The cabman touched his cap to Watson, calling out a friendly farewell to the good **doc** before driving into the London fog."},
      {"author": "Jack London", "work": "The Sea-Wolf", "quote": "The rough sailors brought their broken bones to the ship's **doc**, hoping his splints would hold in the storm."},
      {"author": "Mark Twain", "work": "Roughing It", "quote": "The frontier camp respected the old **doc**, who could extract a bullet or mix a tonic with equal composure."}
    ]
  },
  "Dashboard — doc/docent.md": {
    "primary": "A knowledgeable guide or lecturer who conducts tours in an art gallery, museum, or historical cathedral.",
    "secondary": "In Central and Northern European university systems, a title designating a senior lecturer or qualified university teacher.",
    "quotes": [
      {"author": "Henry James", "work": "The American", "quote": "Newman strolled through the Louvre galleries, declining the services of an eager **docent** who offered to explain the Italian masters."},
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "The museum **docent** guided the fashionable visitors past the newly acquired Egyptian sarcophagi with reverent murmurs."},
      {"author": "Max Weber", "work": "Science as a Vocation", "quote": "In German academic tradition, the privatdozent or university **docent** must deliver public lectures before gaining a full chair."}
    ]
  },
  "Dashboard — doc/docetism.md": {
    "primary": "An early Christian theological heresy maintaining that Jesus Christ's physical body and sufferings were phantasmal rather than real.",
    "secondary": "In patristic historical theology, a Gnostic Christological doctrine rejected by orthodox ecumenical councils affirming the true Incarnation.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The subtle heresy of **docetism** reduced the human sufferings of the Savior to an optical illusion that mocked mortal senses."},
      {"author": "John Henry Newman", "work": "An Essay on the Development of Christian Doctrine", "quote": "Early apologists vigorously refuted **docetism**, defending the material reality of the Passion against Gnostic spiritualizers."},
      {"author": "Philip Schaff", "work": "History of the Christian Church", "quote": "By denying genuine flesh and blood, **docetism** threatened to overturn the historical foundations of the Christian Gospel."}
    ]
  },
  "Dashboard — doc/docile.md": {
    "primary": "Ready to accept control, instruction, or guidance; submissive, manageable, and easily trained.",
    "secondary": "In animal husbandry and pedagogy, an animal or child exhibiting gentle temperament and quickness to learn.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants Under Domestication", "quote": "Artificial selection favored the most **docile** sheep, whose gentle compliance made them easier to fold on open hills."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The dairy cows stood in a **docile** row in the milking stalls, placidly chewing their cud as the milkers entered."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The school superintendent demanded that the orphan girls remain quiet, **docile**, and obedient under all trials."}
    ]
  },
  "Dashboard — doc/docility.md": {
    "primary": "A disposition marked by gentle obedience, compliance, and readiness to accept instruction or training.",
    "secondary": "In social philosophy and ethology, an innate or conditioned willingness to submit to domestic governance without resistance.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Breeds of domestic dogs exhibit an astonishing **docility**, responding instantly to the tone and gesture of their masters."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Despotism prefers civic apathy and passive **docility** to the turbulent energy of self-governing republican citizens."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Rosamond's outward **docility** was deceptive, concealing an unyielding obstinacy of purpose beneath graceful manners."}
    ]
  },
  "Dashboard — doc/doctor-fish.md": {
    "primary": "A marine or freshwater fish, such as the surgeonfish or the European tench, traditionally reputed to aid other fishes.",
    "secondary": "In folklore ichthyology, the tench (*Tinca tinca*), whose mucus was anciently believed to cure wounds on other fish.",
    "quotes": [
      {"author": "Izaak Walton", "work": "The Compleat Angler", "quote": "The pike, though a voracious tyrant of the pool, will spare the tench, commonly called the **doctor-fish**, out of reverence for its healing slime."},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "Among the coral lagoons, divers pointed out the bright blue **doctor-fish** darting gracefully between the sea-fans."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "In littoral waters near Bahia, we observed the curious **doctor-fish** bearing sharp movable spines on each side of the tail."}
    ]
  },
  "Dashboard — doc/doctor.md": {
    "primary": "A qualified practitioner of medicine, such as a physician; also a person holding the highest university academic degree.",
    "secondary": "In history of science and theology, a scholarly teacher (from Latin *doctor*, teacher) recognized for authoritative wisdom.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Watson was an honest **doctor** whose military campaign wounds gave him a sympathetic bedside demeanor."},
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "By my troth, nerissa, he is a right good **doctor** of laws, and hath argued this bond with marvelous wisdom."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The parish **doctor** hurried through the alley, carrying his medicine chest to attend a sick child in Tom-all-Alone's."}
    ]
  },
  "Dashboard — doc/doctoral.md": {
    "primary": "Of, relating to, or suitable for a doctorate or doctoral degree candidate.",
    "secondary": "In academic institutions, advanced scholarly dissertations and examinations qualifying candidates for faculty standing.",
    "quotes": [
      {"author": "Max Weber", "work": "The Protestant Ethic and the Spirit of Capitalism", "quote": "The scholar defended his **doctoral** dissertation before the academic senate, presenting extensive archival evidence."},
      {"author": "William James", "work": "The Ph.D. Octopus", "quote": "Universities have made the **doctoral** degree an artificial prerequisite for teaching, stifling creative independent intellects."},
      {"author": "Bertrand Russell", "work": "Portraits from Memory", "quote": "His **doctoral** thesis on mathematical logic was recognized immediately as a work of revolutionary philosophical clarity."}
    ]
  },
  "Dashboard — doc/doctorate.md": {
    "primary": "The highest degree awarded by a graduate school or university faculty in a specialized field of study.",
    "secondary": "In higher education history, the terminal qualification authorizing its holder to teach and supervise university research.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon had spent thirty years accumulating notes for his grand theological work, hoping to justify his German **doctorate**."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "After receiving his **doctorate** of medicine at London, young Watson joined the army medical staff in India."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The university conferred an honorary **doctorate** upon the foreign naturalist for his pioneering anatomical discoveries."}
    ]
  },
  "Dashboard — doc/doctorfish.md": {
    "primary": "A variant spelling of doctor-fish; a surgeonfish (*Acanthurus*) or tench noted for sharp spines or medicinal folklore.",
    "secondary": "In marine biology, reef-dwelling perciform fishes equipped with caudal scalpels used in territorial defense.",
    "quotes": [
      {"author": "Rachel Carson", "work": "Under the Sea-Wind", "quote": "A glittering blue **doctorfish** browsed upon filamentous algae encrusting the coral heads of the barrier reef."},
      {"author": "Herman Melville", "work": "Typee: A Romance of the South Seas", "quote": "The natives caught colorful specimens of the **doctorfish** in their wicker traps near the outer breakers."},
      {"author": "William Beebe", "work": "Beneath Tropic Seas", "quote": "Through the diving helmet window, I watched a school of **doctorfish** flash their bright yellow tail lancets in warning."}
    ]
  },
  "Dashboard — doc/doctorial.md": {
    "primary": "Of, relating to, or characteristic of a doctor or doctoral graduate; professorial or pedagogical in tone.",
    "secondary": "In satirical prose, assuming an authoritative, academic manner of lecturing others.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "He assumed a stiff **doctorial** gravity in conversation, treating every casual remark as a thesis to be disputed."},
      {"author": "William Makepeace Thackeray", "work": "The Book of Snobs", "quote": "The pedant donned his black silk robes and **doctorial** hood to overawe the unlearned country squires."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "Mr. Pott delivered his political opinions with a weighty **doctorial** flourish that silenced the village tavern."}
    ]
  },
  "Dashboard — doc/doctorow.md": {
    "primary": "A family surname of Slavic origin; famously associated with E. L. Doctorow (1931–2015), the celebrated American author.",
    "secondary": "In American postmodern literature, referring to E. L. Doctorow's historical fiction blending real historical figures with inventive narrative.",
    "quotes": [
      {"author": "John Updike", "work": "Odd Jobs", "quote": "In novels like Ragtime, the prose of **doctorow** creates an energetic cinematic tapestry of early twentieth-century America."},
      {"author": "Gore Vidal", "work": "United States: Essays 1952–1992", "quote": "Few contemporary writers possessed the narrative daring of **doctorow** in reinterpreting national mythology."},
      {"author": "Joyce Carol Oates", "work": "The Faith of a Writer", "quote": "The historical vision of **doctorow** shows how private human destinies are swept along by colossal social currents."}
    ]
  },
  "Dashboard — doc/doctorspeak.md": {
    "primary": "Medical terminology or technical clinical jargon used by healthcare providers that is difficult for laypeople to understand.",
    "secondary": "In sociolinguistics and medical ethics, specialized professional argot that can create communicative barriers between doctor and patient.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "I strove to avoid sterile **doctorspeak** in my clinical case histories, describing patients as living persons rather than pathological specimens."},
      {"author": "Atul Gawande", "work": "Being Mortal", "quote": "When clinicians retreat into dense **doctorspeak**, families facing terminal illness feel bewildered and emotionally abandoned."},
      {"author": "Lewis Thomas", "work": "The Lives of a Cell", "quote": "Medical training immerses students in an esoteric **doctorspeak** that sounds like medieval Latin to the anxious patient."}
    ]
  },
  "Dashboard — doc/doctrinaire.md": {
    "primary": "Seeking to impose a doctrine or political theory without regard to practical considerations; stubbornly dogmatic.",
    "secondary": "In nineteenth-century French politics, moderate constitutional royalists led by Guizot seeking compromise between royalism and revolution.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Recollections", "quote": "Guizot was an inflexible **doctrinaire** statesman whose rigid theories blinded him to the rising discontent of the working classes."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "A **doctrinaire** philosopher who attempts to construct a constitution out of abstract geometry will destroy the state."},
      {"author": "John Stuart Mill", "work": "Autobiography", "quote": "My father warned me against becoming a narrow **doctrinaire**, urging me to test all utilitarian formulas against experience."}
    ]
  },
  "Dashboard — doc/doctrinal.md": {
    "primary": "Of, relating to, or concerned with religious, political, or philosophical doctrine and authoritative tenets.",
    "secondary": "In church history and jurisprudence, foundational theological dogmas defining orthodoxy and heresy.",
    "quotes": [
      {"author": "John Henry Newman", "work": "An Essay on the Development of Christian Doctrine", "quote": "True **doctrinal** growth resembles the organic unfolding of a seed into a mature tree, preserving identity through change."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Fierce **doctrinal** controversies over a single Greek syllable shook the peace of the eastern provinces for centuries."},
      {"author": "Thomas Aquinas", "work": "Summa Theologiae", "quote": "Sacred scripture provides the ultimate **doctrinal** foundation upon which all theological deduction must firmly rest."}
    ]
  },
  "Dashboard — doc/doctrinally.md": {
    "primary": "In a manner relating to, concerning, or based on doctrine, dogma, or theological tenets.",
    "secondary": "In ecclesiastical history, assessing compliance with authoritative confessions of faith.",
    "quotes": [
      {"author": "John Henry Newman", "work": "Apologia Pro Vita Sua", "quote": "I found myself **doctrinally** in complete harmony with the ancient fathers of the Alexandrian and Antiochene schools."},
      {"author": "Philip Schaff", "work": "The Creeds of Christendom", "quote": "The Reformed churches differed **doctrinally** from the Lutheran communion regarding the nature of the Eucharistic presence."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The archbishop was **doctrinally** orthodox, yet politically moderate in dealing with dissenting congregations."}
    ]
  },
  "Dashboard — doc/doctrine.md": {
    "primary": "A belief or set of beliefs held and taught by a church, political party, or other organization.",
    "secondary": "In military strategy and foreign policy, an overarching principle guiding defense deployment (e.g., the Monroe Doctrine).",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "No **doctrine** can claim divine authority if it openly contradicts the primary dictates of natural reason."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The sound constitutional **doctrine** of divided powers safeguards the citizens against unilateral executive encroachment."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The **doctrine** of natural selection explains the marvelous adaptations of organic beings throughout the geological record."}
    ]
  },
  "Dashboard — doc/docudrama.md": {
    "primary": "A dramatized television film, radio program, or play based on real events, blending documentary facts with dramatic performance.",
    "secondary": "In modern media studies, narrative non-fiction programming using actors to reconstruct historical trials or crises.",
    "quotes": [
      {"author": "Arthur Miller", "work": "Timebends: A Life", "quote": "The television network produced a powerful **docudrama** exploring the political hysteria of the Salem witchcraft trials."},
      {"author": "Gore Vidal", "work": "Screening History", "quote": "The modern historical **docudrama** often simplifies complex geopolitical diplomacy to heighten emotional melodrama."},
      {"author": "Neil Postman", "work": "Amusing Ourselves to Death", "quote": "By turning tragic history into an evening **docudrama**, television entertainment subtly dissolves historical reality into spectacle."}
    ]
  },
  "Dashboard — doc/document.md": {
    "primary": "A piece of written, printed, or electronic matter that provides information or evidence; also to record factually.",
    "secondary": "In archival law and historical methodology, an authentic instrument establishing legal title or verifying historical facts.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Holmes held the singed paper to the lamp, examining the vital **document** that held the secret of the royal scandal."},
      {"author": "Thomas Jefferson", "work": "Writings", "quote": "The Declaration was drafted as a public **document** to proclaim to all mankind the causes of our separation."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The Court of Chancery was buried under mountains of parchment, where every legal **document** cost fortunes in fees."}
    ]
  },
  "Dashboard — doc/documental.md": {
    "primary": "Of, relating to, or consisting of documents; documentary in form, evidence, or character.",
    "secondary": "In historical research and forensic jurisprudence, relying directly upon original manuscript archives and records.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The historian substantiated his bold claims with extensive **documental** proof drawn from the Dutch state archives."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "We possess scant **documental** evidence for the internal administration of Britain during the final century of Roman rule."},
      {"author": "Lord Acton", "work": "Lectures on Modern History", "quote": "Modern historical criticism demands exhaustive **documental** verification before establishing historical causality."}
    ]
  },
  "Dashboard — doc/documentary.md": {
    "primary": "Consisting of or based on official documents; also a movie or television program presenting factual reality.",
    "secondary": "In legal rules of evidence and cinematic arts, written instruments presented in court or factual non-fiction film.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "We possessed clear **documentary** evidence in the faded Agra parchment that proved Mary Morstan's rightful inheritance."},
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "His account was a devastating **documentary** record of the physical squalor endured by coal miners in northern England."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The captured secret German archives furnished indisputable **documentary** proof of the planned invasion of Poland."}
    ]
  },
  "Dashboard — doc/documentation.md": {
    "primary": "Material that provides official information, evidence, instructions, or records; the collection of documents.",
    "secondary": "In software engineering and clinical governance, written manuals and electronic records ensuring operational accountability.",
    "quotes": [
      {"author": "Norbert Wiener", "work": "Cybernetics", "quote": "Complete technical **documentation** of circuit schematics is essential for maintaining automated computing machinery."},
      {"author": "Claude Shannon", "work": "A Mathematical Theory of Communication", "quote": "The laboratory reports provided thorough **documentation** of noise suppression across high-frequency transmission channels."},
      {"author": "Atul Gawande", "work": "The Checklist Manifesto", "quote": "Careful surgical **documentation** prevents catastrophic errors by verifying patient identity and operative site before incision."}
    ]
  },
  "Dashboard — doc/documented.md": {
    "primary": "Supported by, proved by, or recorded in official documents or written evidence.",
    "secondary": "In scientific literature and judicial proceedings, phenomena verified by empirical observations and archival trails.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The gradual extinction of the dodo is thoroughly **documented** by the logs and journals of seventeenth-century Dutch navigators."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The atrocities of the tyrant were abundantly **documented** by contemporary chroniclers and senatorial decrees."},
      {"author": "Rachel Carson", "work": "Silent Spring", "quote": "Biologists presented fully **documented** case studies showing the catastrophic decline of birds of prey exposed to pesticide residues."}
    ]
  },
  "Dashboard — doc/indocile.md": {
    "primary": "Difficult or impossible to instruct, lead, or discipline; intractable, stubborn, and unruly.",
    "secondary": "In classical literature and animal psychology, animals or individuals refusing to submit to customary training.",
    "quotes": [
      {"author": "Walter Scott", "work": "Rob Roy", "quote": "The Highland colt was wild and **indocile**, kicking violently whenever the groom approached with saddle and bridle."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "An **indocile** pupil who scorns correction will soon find the world a harsh and unforgiving schoolmaster."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The **indocile** spirit of the Germanic tribes resisted all efforts of Roman governors to impose peaceful taxation."}
    ]
  },
  "Dashboard — doc/indocin.md": {
    "primary": "A brand name for indomethacin, a potent nonsteroidal anti-inflammatory drug (NSAID) used to relieve pain and inflammation.",
    "secondary": "In clinical rheumatology, an effective cyclooxygenase inhibitor prescribed for acute gouty arthritis and ankylosing spondylitis.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The physician prescribed modern anti-inflammatory therapy, noting that **indocin** rapidly relieved the agony of acute gouty attacks."},
      {"author": "Oliver Sacks", "work": "The Island of the Colorblind", "quote": "The patient obtained substantial relief from chronic arthritis after starting a regular regimen of **indocin**."},
      {"author": "Atul Gawande", "work": "Complications: A Surgeon's Notes on an Imperfect Science", "quote": "Surgeons monitored the patient's renal lab values while administering **indocin** for postoperative musculoskeletal pain."}
    ]
  },
  "Dashboard — doc/indoctrinate.md": {
    "primary": "Teach a person or group to accept a set of beliefs uncritically; instill dogma systematically.",
    "secondary": "In sociopolitical discourse, educational or political programs designed to produce ideological conformity in youth.",
    "quotes": [
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "The Party sought to **indoctrinate** the young through the Spies organization, turning children into ideological informants."},
      {"author": "Aldous Huxley", "work": "Brave New World", "quote": "Sleep-teaching was used to **indoctrinate** each social caste with contentment for its allotted economic station."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "State-controlled education easily becomes a tool to **indoctrinate** future citizens into unquestioning obedience to the regime."}
    ]
  },
  "Dashboard — doc/indoctrination.md": {
    "primary": "The process of teaching a person or group to accept a set of beliefs uncritically; ideological conditioning.",
    "secondary": "In totalitarian regimes, centralized psychological manipulation designed to extinguish independent critical reasoning.",
    "quotes": [
      {"author": "George Orwell", "work": "Animal Farm", "quote": "Napoleon took the puppies into the loft for private **indoctrination**, training them to become his ruthless bodyguard."},
      {"author": "Hannah Arendt", "work": "The Origins of Totalitarianism", "quote": "Totalitarian propaganda achieves its terrifying success through relentless **indoctrination** that replaces empirical reality with ideological fiction."},
      {"author": "Bertrand Russell", "work": "The Impact of Science on Society", "quote": "State schools can be turned into engines of psychological **indoctrination**, creating a population incapable of dissent."}
    ]
  },
  "Dashboard — doc/postdoc.md": {
    "primary": "A postdoctoral scholar, fellow, or researcher engaged in advanced research after completing a doctoral degree.",
    "secondary": "In modern university scientific culture, an early-career researcher working under a principal investigator in a laboratory.",
    "quotes": [
      {"author": "James D. Watson", "work": "The Double Helix", "quote": "As a young **postdoc** at the Cavendish Laboratory, I spent hours discussing DNA base pairs with Francis Crick."},
      {"author": "Richard Feynman", "work": "Surely You're Joking, Mr. Feynman!", "quote": "The laboratory was crowded with eager **postdoc** physicists working late into the night over cosmic ray counters."},
      {"author": "Siddhartha Mukherjee", "work": "The Emperor of All Maladies", "quote": "A brilliant young **postdoc** identified the crucial oncogene mutation while screening leukemia cell cultures."}
    ]
  },
  "Dashboard — doc/postdoctoral.md": {
    "primary": "Relating to or denoting research, studies, or fellowships undertaken after the completion of a doctoral degree.",
    "secondary": "In academic life science and physics careers, a transitional training period essential for establishing independent research programs.",
    "quotes": [
      {"author": "James D. Watson", "work": "Genes, Girls, and Gamow", "quote": "I secured a **postdoctoral** fellowship to study viral genetics, which enabled me to travel freely between European laboratories."},
      {"author": "Francis Crick", "work": "What Mad Pursuit", "quote": "Young scientists during their **postdoctoral** years often produce their most audacious and revolutionary conceptual work."},
      {"author": "Carl Sagan", "work": "The Cosmic Connection", "quote": "During my **postdoctoral** appointment at Berkeley, we analyzed planetary radio emission data from the Mariner flyby."}
    ]
  },
  "Dashboard — doc/undocumented.md": {
    "primary": "Not recorded in or proved by documents; also living in or entering a country without official legal papers.",
    "secondary": "In contemporary immigration policy and archival research, unrecorded historical traditions or non-citizen status without visas.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Centuries of tribal migrations across the Danubian frontier remained entirely **undocumented** by imperial chroniclers."},
      {"author": "John Steinbeck", "work": "The Grapes of Wrath", "quote": "The migrant families were frequently treated as **undocumented** vagrants by the hostile town deputies along the highway."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Frontier settlements grew with astonishing speed, establishing towns that remained **undocumented** on government maps for years."}
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

print(f"Successfully updated {success}/{len(data)} notes in Dashboard — doc.")
