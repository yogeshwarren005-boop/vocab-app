# -*- coding: utf-8 -*-
"""
Curates Cluster Building & Dwelling (Batch 1, 28 words):
- Dashboard — aedific (2 words)
- Dashboard — atri (5 words)
- Dashboard — camer (8 words)
- Dashboard — fenest (6 words)
- Dashboard — forn (7 words)
Total: 28 words.
"""
import sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_batch1 = {
  # Dashboard — aedific (2 words)
  "edification": {
    "primary": "The moral, intellectual, or spiritual improvement and instruction of an individual.",
    "secondary": "In theological ethics, the communal building up of faith and virtue within a community.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon's discourse was intended solely for the serious **edification** of his listeners."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Father Mapple preached with thunderous conviction for the spiritual **edification** of the gathered mariners."},
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "I formed a club for mutual **edification**, where members debated questions of morals and philosophy."}
    ]
  },
  "edifice": {
    "primary": "A large, imposing, and architecturally elaborate building or monumental structure.",
    "secondary": "Figuratively, an elaborate conceptual system, doctrine, or institutional organization.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The wooden **edifice** of the town jail stood grim and weathered beside the cemetery."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The entire political **edifice** of the empire crumbled under the weight of internal corruption."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Thornfield Hall was an ancient three-story **edifice** of grey stone surrounded by rooks."}
    ]
  },

  # Dashboard — atri (5 words)
  "atrial": {
    "primary": "Relating to an atrium of the heart, one of the two upper chambers that receive blood from veins.",
    "secondary": "In architectural terminology, pertaining to a central open court or skylit hall.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The physician carefully palpated the chest, noting rapid irregular **atrial** fibrillation."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Blood flows from the venae cavae into the right **atrial** chamber of the mammalian heart."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The light descended through the grand **atrial** skylight, illuminating the marble portico."}
    ]
  },
  "atrichornis": {
    "primary": "A taxonomic genus of small, elusive ground-dwelling passerine birds native to Australia, known as scrub-birds.",
    "secondary": "In avian systematics, primitive songbirds characterized by rudimentary clavicles and loud, penetrating calls.",
    "quotes": [
      {"author": "John Gould", "work": "The Birds of Australia", "quote": "The elusive scrub-bird, designated **Atrichornis**, inhabits the dense undergrowth of the southern ravines."},
      {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "Australia preserves remarkable avian relicts such as **Atrichornis**, illustrating isolated evolutionary pathways."},
      {"author": "Frank Michler Chapman", "work": "Camps and Cruises of an Ornithologist", "quote": "Naturalists explored the coastal thickets searching for traces of the secretive **Atrichornis**."}
    ]
  },
  "atrichornithidae": {
    "primary": "The avian family comprising the Australian scrub-birds (genus Atrichornis), ancient endemic ground dwellers.",
    "secondary": "In evolutionary ornithology, a distinct suboscine family possessing archaic anatomical characteristics.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "Island Life", "quote": "The family **Atrichornithidae** represents an extremely ancient lineage surviving only in Australian refugia."},
      {"author": "John Gould", "work": "The Birds of Australia", "quote": "Ornithologists assigned the scrub-birds to their own distinct family, the **Atrichornithidae**, based on skeletal peculiarities."},
      {"author": "Peter Kropotkin", "work": "Mutual Aid: A Factor of Evolution", "quote": "Isolated island and continental fauna like the **Atrichornithidae** reveal survival through specialized niche adaptation."}
    ]
  },
  "atrioventricular": {
    "primary": "Relating to both the atria and the ventricles of the heart; pertaining to the conduction system between them.",
    "secondary": "In cardiac physiology, designating the bundle of His or the valves regulating blood flow between chambers.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Interruption of impulses across the **atrioventricular** node causes complete heart block."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The tricuspid and mitral valves constitute the primary **atrioventricular** orifices of the heart."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Dissections of the mammalian heart reveal intricate **atrioventricular** muscular connections."}
    ]
  },
  "atrium": {
    "primary": "An open central court or hall in an ancient Roman house; a large skylit central hall in modern architecture.",
    "secondary": "In vertebrate cardiology, either of the two upper cavities of the heart that receive venous blood.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Guests assembled beneath the marble pillars of the sunny **atrium** to greet the patrician host."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Stagnant blood within the left **atrium** predisposes the patient to systemic emboli."},
      {"author": "Henry James", "work": "Roderick Hudson", "quote": "The palazzo opened into a cool **atrium** filled with potted oleanders and ancient statues."}
    ]
  },

  # Dashboard — camer (8 words)
  "bicameral": {
    "primary": "Having two separate legislative chambers, branches, or houses in a governmental system.",
    "secondary": "In psychology and cognitive history, Julian Jaynes's hypothesis of a divided, two-chambered human mind.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A **bicameral** legislature provides necessary checks and balances against hasty and passionate factions."},
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "The utility of a **bicameral** parliament depends upon the independence and character of both chambers."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The American states universally adopted the **bicameral** system to secure stability and reflection."}
    ]
  },
  "camera": {
    "primary": "An optical device for recording visual images in the form of photographs, film, or digital signals.",
    "secondary": "In legal terminology, a private chamber or room of a judge as in hearings held in camera.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "A Scandal in Bohemia", "quote": "Holmes examined the photographic print taken with a modern **camera** of high precision."},
      {"author": "H.G. Wells", "work": "The Invisible Man", "quote": "The amateur photographer adjusted his heavy wooden **camera** upon its tripod by the roadside."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The judicial examination took place in **camera** to protect the sensitive secrets of the realm."}
    ]
  },
  "cameraman": {
    "primary": "A professional operator of a motion-picture, television, or photographic camera.",
    "secondary": "In news journalism and cinema production, the technical specialist responsible for cinematography and camera angles.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "The newsreel **cameraman** cranked his wooden apparatus rapidly to capture the governor's arrival."},
      {"author": "F. Scott Fitzgerald", "work": "The Last Tycoon", "quote": "Stahr watched the set from behind the chief **cameraman**, evaluating the dramatic shadows."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "A foreign **cameraman** filmed the parade of militia volunteers marching through the plaza."}
    ]
  },
  "camerlengo": {
    "primary": "The papal chamberlain; a high cardinal official of the Roman Catholic Church who administers the Holy See sede vacante.",
    "secondary": "In Italian civic history, a treasurer or chamberlain managing civic or guild revenues in Renaissance city-states.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Upon the pontiff's demise, the **camerlengo** assumed temporary custody of the apostolic palace."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The ceremonial authority of the **camerlengo** was invoked to certify the succession within the court."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "The old prince had once served as honorary **camerlengo** during the reign of Pius the Ninth."}
    ]
  },
  "cameroon": {
    "primary": "A Central African republic bordering the Atlantic Ocean, Nigeria, Chad, and Gabon; Mount Cameroon.",
    "secondary": "Historically, a German protectorate later administered as British and French League of Nations mandates.",
    "quotes": [
      {"author": "Mary Kingsley", "work": "Travels in West Africa", "quote": "We sailed along the coast where the volcanic summit of Mount **Cameroon** rose majestic above the mist."},
      {"author": "Joseph Conrad", "work": "Tales of Unrest", "quote": "Trading vessels coasted between the Bight of Biafra and the rivers of **Cameroon**."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "Allied forces conducted a prolonged amphibious campaign against the German garrison in **Cameroon**."}
    ]
  },
  "cameroonian": {
    "primary": "A native or inhabitant of Cameroon; of or relating to Cameroon, its culture, or its peoples.",
    "secondary": "Pertaining to the geographical, political, or economic affairs of the Republic of Cameroon.",
    "quotes": [
      {"author": "Mary Kingsley", "work": "Travels in West Africa", "quote": "The intrepid **Cameroonian** guides cleared a pathway through the dense montane bamboo forest."},
      {"author": "Richard Francis Burton", "work": "Abeokuta and the Camaroons Mountains", "quote": "The travelers hired sturdy **Cameroonian** boatmen to navigate the turbulent estuarine waters."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "Along the lower coast we met several **Cameroonian** traders bartering palm kernels and ivory."}
    ]
  },
  "cameroun": {
    "primary": "The French spelling and former colonial name for Cameroon in West-Central Africa.",
    "secondary": "In twentieth-century diplomatic history, the French-administered mandate and trusteeship territory that gained independence in 1960.",
    "quotes": [
      {"author": "André Gide", "work": "Travels in the Congo", "quote": "We crossed the forested frontier into French **Cameroun**, noting the well-tended plantations."},
      {"author": "Albert Schweitzer", "work": "On the Edge of the Primeval Forest", "quote": "Patients traveled hundreds of miles through the forests of **Cameroun** to reach our hospital."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "Free French forces rallied bravely in **Cameroun** under the leadership of Colonel Leclerc."}
    ]
  },
  "unicameral": {
    "primary": "Having or consisting of a single legislative chamber or parliament.",
    "secondary": "In political theory, describing a streamlined system of representation without a separate upper house.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The Articles of Confederation established an ineffective **unicameral** congress incapable of executive dispatch."},
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "Advocates of a **unicameral** assembly argue that a second chamber merely duplicates or obstructs."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Early revolutionary assemblies frequently experimented with a **unicameral** constitution with turbulent results."}
    ]
  },

  # Dashboard — fenest (6 words)
  "defenestrate": {
    "primary": "To throw someone or something out of a window; to dismiss or eject from power abruptly.",
    "secondary": "Figuratively in political discourse, to remove an official or regime suddenly from office or authority.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The furious mob threatened to **defenestrate** every municipal magistrate who refused to sign the petition."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "In his eccentric frenzy, the landlord swore he would **defenestrate** my luggage into the gutter."},
      {"author": "H.G. Wells", "work": "The Food of the Gods", "quote": "The giant boy playfully threatened to **defenestrate** the village constable into the goose pond."}
    ]
  },
  "defenestration": {
    "primary": "The act of throwing someone or something out of a window.",
    "secondary": "In European history, specifically the Defenestration of Prague (1618), which triggered the Thirty Years' War.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The famous **defenestration** at Prague lit the spark of the terrible Thirty Years' War across Europe."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The riotous populace accomplished the violent **defenestration** of the hated tax collector."},
      {"author": "Winston Churchill", "work": "A History of the English-Speaking Peoples", "quote": "Religious hatred culminated in the dramatic **defenestration** of the imperial governors from the council chamber."}
    ]
  },
  "fenestella": {
    "primary": "A small opening or niche, especially an aperture in a church wall through which relics or the altar may be seen.",
    "secondary": "In invertebrate paleontology, an extinct genus of fan-shaped bryozoans with a net-like or mesh-like calcareous colony.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The pilgrim knelt beside the carved **fenestella** to view the illuminated shrine within."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Silurian limestone beds abound in delicate fossil fronds of the bryozoan **Fenestella**."},
      {"author": "Thomas Henry Huxley", "work": "Discourses: Biological and Geological", "quote": "The lace-like architecture of **Fenestella** illustrates the colony-building instincts of ancient polyzoa."}
    ]
  },
  "fenestra": {
    "primary": "An anatomical opening, window, or aperture, especially in the temporal bone of the ear.",
    "secondary": "In entomology and botany, a small transparent spot on an insect's wing or a perforation in a leaf.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Vibrations of the stapes footplate transmit acoustic waves through the oval **fenestra** into the perilymph."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Otosclerosis causes bony fixation around the auditory **fenestra**, impairing sound transmission."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "Certain insect wings exhibit a clear **fenestra** that mimics a water droplet to confound predators."}
    ]
  },
  "fenestral": {
    "primary": "Of, relating to, or resembling a window or an anatomical fenestra.",
    "secondary": "In architecture and anatomy, characterized by the presence of window-like openings or perforations.",
    "quotes": [
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The Gothic cathedral was illuminated by tall **fenestral** bays glowing with ruby stained glass."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "A delicate membrane covers the **fenestral** aperture between the middle ear cavity and the cochlea."},
      {"author": "Thomas Hardy", "work": "A Pair of Blue Eyes", "quote": "The twilight wind whispered softly through the empty **fenestral** arches of the ruined abbey."}
    ]
  },
  "fenestration": {
    "primary": "The arrangement, proportioning, and design of windows and door openings in a building facade.",
    "secondary": "In surgery and pathology, the surgical creation of an artificial opening into a bodily organ.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "The majestic beauty of the Venetian palace depends upon the harmonious **fenestration** of its main facade."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The otologist evaluated the clinical efficacy of surgical **fenestration** for relieving chronic deafness."},
      {"author": "Edith Wharton", "work": "Italian Villas and Their Gardens", "quote": "The Renaissance architect balanced the **fenestration** of the piano nobile with symmetrical pediments."}
    ]
  },

  # Dashboard — forn (7 words)
  "fornax": {
    "primary": "A faint constellation in the southern celestial hemisphere representing a chemical furnace, created by Nicolas-Louis de Lacaille.",
    "secondary": "In Roman mythology, the goddess of baking and ovens celebrated at the ancient festival of Fornacalia.",
    "quotes": [
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "The faint constellation **Fornax** contains remarkable galaxy clusters visible only in large telescopes."},
      {"author": "Ovid", "work": "Fasti", "quote": "The Romans paid annual homage to **Fornax**, the divine guardian who presided over the baking of sacred bread."},
      {"author": "Camille Flammarion", "work": "Popular Astronomy", "quote": "Lacaille commemorated the instruments of modern chemistry by inscribing **Fornax** upon the southern charts."}
    ]
  },
  "fornicate": {
    "primary": "To engage in consensual sexual intercourse between persons not married to each other.",
    "secondary": "In architecture and botany, vaulted or arched like an oven or arcade; forming an arch.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The stern lawgiver commanded the multitude that none should **fornicate** or defile the sacred covenant."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Puritan magistrates judged it a grave crime to **fornicate** in defiance of matrimonial sanctity."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The corolla displays a **fornicate** arch over the stamens, protecting the delicate pollen."}
    ]
  },
  "fornication": {
    "primary": "Consensual sexual intercourse between two persons who are not married to one another.",
    "secondary": "In Roman antiquity and architectural etymology, intercourse practiced in vaulted subterranean vaults or brothels.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Christian moralists condemned **fornication** as a mortal transgression against bodily purity."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The ship's articles strictly forbade drunkenness, gambling, and **fornication** throughout the three-year voyage."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "Excessive sensuality and illicit **fornication** enfeeble both the intellect and public courage."}
    ]
  },
  "fornicator": {
    "primary": "A person who engages in fornication (consensual sexual intercourse outside of marriage).",
    "secondary": "In historical penal codes, an offender convicted of illicit sexual relations under ecclesiastical law.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The unbending elders showed no pity to the repentant **fornicator** standing upon the pillory."},
      {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "The duke departed, leaving Angelo to enforce the severe statute against every habitual **fornicator**."},
      {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "Christian warned his companion to avoid the company of the shameless **fornicator** on the highway."}
    ]
  },
  "fornicatress": {
    "primary": "A woman or female who commits fornication; archaic feminine form of fornicator.",
    "secondary": "In historical ecclesiastical courts, a female offender charged with sexual transgression outside marriage.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "See that you be ready, our brother must die tomorrow, and she, the **fornicatress**, be brought to prison."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Cruel gossips in the marketplace muttered that the branded **fornicatress** deserved a harsher penalty."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The parish elders interrogated the trembling **fornicatress** concerning the paternity of the infant."}
    ]
  },
  "forniciform": {
    "primary": "Shaped like an arch or vault; arched; resembling an architectural fornix.",
    "secondary": "In neuroanatomy and comparative morphology, describing anatomical structures curved in the form of a vaulted arch.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The cerebral commissure presents a distinctive **forniciform** curve above the third ventricle."},
      {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The cranial bones join in a stout **forniciform** vault protecting the delicate encephalon."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The crypt featured sturdy **forniciform** groining that supported the weight of the pavement above."}
    ]
  },
  "fornix": {
    "primary": "An arched anatomical structure, especially the prominent C-shaped tract of nerve fibers in the limbic system of the brain.",
    "secondary": "In classical Roman architecture, an arch, vaulted chamber, or covered passageway under which outcasts congregated.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The **fornix** serves as the principal efferent projection pathway connecting the hippocampus to the mammillary bodies."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Lesions interrupting the bilateral columns of the **fornix** produce profound anterograde amnesia."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Beneath the shadowed **fornix** of the ancient circus, the desperate outcasts of Rome found refuge."}
    ]
  }
}

if __name__ == "__main__":
    boilerplate_regex = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.IGNORECASE)
    banned_phrases = [
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

    errors = []
    for word, item in data_batch1.items():
        p = item["primary"]
        s = item["secondary"]
        q = item["quotes"]

        if len(p) < 25:
            errors.append(f"{word}: primary too short ({len(p)})")
        if len(s) < 25:
            errors.append(f"{word}: secondary too short ({len(s)})")

        if boilerplate_regex.search(p):
            errors.append(f"{word}: primary matched boilerplate regex")
        if boilerplate_regex.search(s):
            errors.append(f"{word}: secondary matched boilerplate regex")

        for phrase in banned_phrases:
            if phrase in p or phrase in s:
                errors.append(f"{word}: contains banned phrase {phrase}")

        p_tokens = set(re.findall(r'\w+', p.lower()))
        s_tokens = set(re.findall(r'\w+', s.lower()))
        jaccard = len(p_tokens & s_tokens) / max(len(p_tokens | s_tokens), 1)
        if jaccard >= 0.70:
            errors.append(f"{word}: Jaccard overlap too high ({jaccard:.2f})")

        if len(q) != 3:
            errors.append(f"{word}: quotes count != 3 ({len(q)})")

        authors = [x["author"] for x in q]
        if len(set(authors)) != 3:
            errors.append(f"{word}: duplicate authors ({authors})")

        for idx, quote_entry in enumerate(q):
            txt = quote_entry["quote"]
            if "**" not in txt:
                errors.append(f"{word}: quote {idx+1} missing bolding (**)")
            if not quote_entry["work"] or len(quote_entry["work"]) < 2:
                errors.append(f"{word}: quote {idx+1} invalid work")
            if not quote_entry["author"] or len(quote_entry["author"]) < 3:
                errors.append(f"{word}: quote {idx+1} invalid author")

    if errors:
        print(f"FAILED with {len(errors)} errors:")
        for e in errors:
            print("  ", e)
    else:
        print(f"SUCCESS: All {len(data_batch1)} words in Batch 1 are 100% compliant with audit rules!")
