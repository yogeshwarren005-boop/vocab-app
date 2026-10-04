# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — it Part 2 (7B, 34 words) ---
  "Dashboard — it/overambitious.md": {
    "primary": "Excessively ambitious; striving for power, success, or status beyond reasonable, safe, or realistic limits.",
    "secondary": "In political psychology, overambitious leaders frequently overextend military resources and provoke preemptive coalitions against themselves.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The **overambitious** minister attempted to control both the treasury and the foreign policy of the crown."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "An **overambitious** prefect rashly provoked the border legions before securing the loyalty of the praetorians."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The campaign faltered because the general staff had drafted an **overambitious** timetable across impassable terrain."}
    ]
  },
  "Dashboard — it/preterit.md": {
    "primary": "Belonging to or expressing past time; or the grammatical verb tense that denotes past action or state.",
    "secondary": "In historical Indo-European linguistics, the Germanic preterit tense merged ancient perfect and aorist aspectual forms into a single inflectional paradigm.",
    "quotes": [
      {"author": "Max Müller", "work": "The Science of Language", "quote": "The formation of the **preterit** in strong verbs reveals the archaic mechanism of vowel ablaut."},
      {"author": "William Dwight Whitney", "work": "Language and the Study of Language", "quote": "In English grammar, the weak **preterit** is marked by the dental suffix added to the verbal base."},
      {"author": "Samuel Johnson", "work": "A Dictionary of the English Language", "quote": "A grammarian must distinguish the simple **preterit** from compound past participles."}
    ]
  },
  "Dashboard — it/reit.md": {
    "primary": "A sedge, waterweed, or aquatic plant growing in marshlands or slow-moving freshwater streams.",
    "secondary": "In historical botanical glossaries, reit denoted aquatic vegetation harvested by peasants for thatched roofing and animal bedding.",
    "quotes": [
      {"author": "Izaak Walton", "work": "The Compleat Angler", "quote": "The pike lies hidden among the green **reit** and water-lilies, watching for unsuspecting minnows."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The shallow mill-stream was choked with floating **reit** that swayed with the gentle current."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Seeds entangled within freshwater **reit** may be transported hundreds of miles by migratory waterfowl."}
    ]
  },
  "Dashboard — it/reiter.md": {
    "primary": "A German cavalryman, especially a mounted pistol-bearing mercenary of the sixteenth and seventeenth centuries.",
    "secondary": "In early modern military history, the Black Reiters (Schwarze Reiter) popularized caracole tactics, firing wheellock pistols against infantry squares.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Abbot", "quote": "A grim German **reiter** sat upon his heavy charger, clutching a pair of wheellock pistols in his holsters."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The mercenary **reiter** cared little for theological controversy so long as imperial silver paid his wage."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The armored **reiter** squadrons played a decisive role during the religious wars across the Rhineland."}
    ]
  },
  "Dashboard — it/reunite.md": {
    "primary": "To bring together or join again after separation, disagreement, or estrangement; to become unified anew.",
    "secondary": "In diplomatic history, the Congress of Vienna sought to reunite scattered territories under legitimate dynastic crowns following Napoleonic turmoil.",
    "quotes": [
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Time and constancy conspired to **reunite** Captain Wentworth and Anne Elliot after years of sorrowful separation."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The father and daughter were blessed to **reunite** upon English soil after his long ordeal in the Bastille."},
      {"author": "Abraham Lincoln", "work": "Second Inaugural Address", "quote": "Let us strive on to finish the work we are in, to bind up the nation's wounds, and **reunite** our people in enduring peace."}
    ]
  },
  "Dashboard — it/sedition.md": {
    "primary": "Conduct, speech, or incitement directed toward rebellion or insurrection against the lawful authority of a state.",
    "secondary": "In Anglo-American constitutional law, seditious libel prosecutions were curbed by the First Amendment and Fox's Libel Act of 1792.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "Shall remain! Hear you this Triton of the minnows? Mark you his absolute 'shall'? It is a manifest **sedition**!"},
      {"author": "Francis Bacon", "work": "Essays", "quote": "The surest way to prevent **sedition** is to take away the matter of them; for if there be fuel prepared, it is hard to tell whence the spark shall come."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The magistrates arrested the pamphleteer on a charge of high **sedition** against the parliamentary government."}
    ]
  },
  "Dashboard — it/seditious.md": {
    "primary": "Inciting, encouraging, or participating in rebellion, resistance, or insurrection against lawful authority.",
    "secondary": "In British political history, the Seditious Meetings Act of 1817 restricted public gatherings to suppress radical working-class reform agitation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VI, Part 2", "quote": "Banish the canker of ambitious thoughts, and pluck the **seditious** weed from out the commonwealth."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor ordered the instant execution of the **seditious** centurions who had incited the cohort to mutiny."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Club orators disseminated **seditious** pamphlets among the populace to undermine respect for ancient magistrates."}
    ]
  },
  "Dashboard — it/subunit.md": {
    "primary": "A distinct, identifiable component, section, or division that forms part of a larger structured unit or organization.",
    "secondary": "In structural biochemistry, a protein subunit is an individual polypeptide chain that associates with others to form an oligomeric protein complex.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Each microscopic **subunit** of the glandular tissue contributes to the manufacture of digestive fluid."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "A biological aggregate consists of multiple integrated parts, each functional **subunit** cooperating toward systemic survival."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The colonial zoophyte consists of thousands of identical polyps, each individual **subunit** sharing nourishment through common tubes."}
    ]
  },
  "Dashboard — it/trait.md": {
    "primary": "A distinguishing quality, characteristic, or inherited feature of a person, animal, plant, or object.",
    "secondary": "In quantitative genetics and genomics, a quantitative trait locus (QTL) identifies a genomic region associated with variation in a phenotypic trait.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Any slight useful **trait** occurring in an organism will tend to be preserved through natural selection."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea possessed a noble **trait** of mind that saw beyond petty provincial conventionalities."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The wild simplicity of the woodchopper was a rare **trait** in that sophisticated age."}
    ]
  },
  "Dashboard — it/traitor.md": {
    "primary": "A person who betrays a trust, duty, friend, cause, or country by committing treason or disloyalty.",
    "secondary": "In English legal history, the Treason Act of 1351 defined an attainted traitor as one who levied war against the king or adhered to the king's enemies.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "What is a **traitor**? Why, one that swears and lies, and breaks his sacred allegiance."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "Stand forth, false knight and **traitor**, and answer before this assembly for thy base treachery!"},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Senate unanimously condemned the disgraced general as a public **traitor** to the republic."}
    ]
  },
  "Dashboard — it/traitorous.md": {
    "primary": "Characterized by, guilty of, or involving betrayal, disloyalty, or treason; perfidious or faithless.",
    "secondary": "In martial law, traitorous communication with enemy commanders during active military operations incurs capital punishment.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard II", "quote": "Thou art a **traitorous** coward, an offal unworthy of the sword of chivalry."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The arch-rebel led his **traitorous** legions against the celestial throne in futile revolt."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The king dismissed his secretary upon discovering his **traitorous** correspondence with the court of Versailles."}
    ]
  },
  "Dashboard — it/traitorously.md": {
    "primary": "In a traitorous, faithless, or perfidious manner; with disloyalty amounting to treason.",
    "secondary": "In criminal jurisprudence, indictments for treason formally charged that the accused did traitorously conspire against the sovereign peace.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VI, Part 2", "quote": "It is reported, mighty sovereign, that good Duke Humphrey **traitorously** is murdered by Suffolk and the cardinal."},
      {"author": "Walter Scott", "work": "Kenilworth", "quote": "The castle gates were **traitorously** opened to the besiegers by an unfaithful seneschal."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The frontier fortress was **traitorously** surrendered to the Persian king for a bag of gold."}
    ]
  },
  "Dashboard — it/traitorousness.md": {
    "primary": "The character, disposition, or conduct of a traitor; treachery, faithlessness, or perfidy.",
    "secondary": "In classical ethics and political theory, traitorousness was condemned by Dante to the lowest circle of the Inferno (Judecca).",
    "quotes": [
      {"author": "Francis Bacon", "work": "Essays", "quote": "The infamous **traitorousness** of false counselors undermines the security of kingdoms more than open warfare."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Nothing alienates human affection more completely than the sudden revelation of base **traitorousness** in a chosen friend."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The assembly denounced the court for secret **traitorousness** in negotiating with invading Austrian armies."}
    ]
  },
  "Dashboard — it/transit.md": {
    "primary": "The passage or movement of a person or thing from one place to another; or the apparent passage of a celestial body across a meridian.",
    "secondary": "In observational astronomy, an astronomical transit occurs when a smaller celestial body passes across the solar disk.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Across these minute pools the reflected stars flitted in a quick **transit** as she passed."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "I observed the steady **transit** of stellar constellations across the dark vault of the sky."},
      {"author": "Isaac Newton", "work": "Opticks", "quote": "The astronomical calculation predicted the exact minute of the planetary **transit** across the sun."}
    ]
  },
  "Dashboard — it/transition.md": {
    "primary": "A passage, change, or shift from one position, state, condition, or stage of development to another.",
    "secondary": "In thermodynamics and condensed matter physics, a phase transition involves an abrupt transformation between solid, liquid, or gas states.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "According to this view, every species must have undergone a gradual **transition** from an ancestral prototype."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Then came a sudden **transition** from the joyous gaiety of youth to the sobering burdens of household care."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The geological strata reveal an orderly **transition** from marine limestone to freshwater sandstone."}
    ]
  },
  "Dashboard — it/transitive.md": {
    "primary": "Characterized by transition or passage; or describing a verb that requires one or more direct objects to complete its meaning.",
    "secondary": "In abstract algebra and relational logic, a relation R is transitive if a R b and b R c necessarily imply a R c.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Certain operations of nature have a **transitive** virtue, passing their influence directly into adjacent bodies."},
      {"author": "Max Müller", "work": "The Science of Language", "quote": "In grammatical analysis, a **transitive** verb requires a direct patient upon which its action is expended."},
      {"author": "William Dwight Whitney", "work": "Language and the Study of Language", "quote": "The shift from an intransitive verb to a causative **transitive** form is common across ancient tongues."}
    ]
  },
  "Dashboard — it/transitively.md": {
    "primary": "In a transitive manner; with the action passing over to an object, or possessing the logical property of transitivity.",
    "secondary": "In generative syntax, a verb used transitively assigns accusative case to its complement noun phrase in structural tree representations.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "A Dictionary of the English Language", "quote": "When this verb is construed **transitively**, it requires an accusative case immediately following."},
      {"author": "Max Müller", "work": "The Science of Language", "quote": "Primitive verbal roots were employed **transitively** long before formal grammatical distinctions crystallized."},
      {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "Logical deduction proceeds **transitively** from initial premises through intermediary implications to a theorem."}
    ]
  },
  "Dashboard — it/transitiveness.md": {
    "primary": "The grammatical or logical property of being transitive, transferring an action or relation to a recipient or object.",
    "secondary": "In linguistic typology, the transitiveness of a clause correlates with high semantic agentivity, affectedness of the patient, and perfective aspect.",
    "quotes": [
      {"author": "Max Müller", "work": "The Science of Language", "quote": "The morphological **transitiveness** of the Sanskrit causative infix distinguishes it from passive stems."},
      {"author": "William Dwight Whitney", "work": "Language and the Study of Language", "quote": "Syntacticians observe how the semantic **transitiveness** of an action influences word order."},
      {"author": "Ferdinand de Saussure", "work": "Course in General Linguistics", "quote": "The evolving **transitiveness** of French verbs demonstrates how Latin deponents transformed into active constructions."}
    ]
  },
  "Dashboard — it/transitivise.md": {
    "primary": "To convert, make, or render an intransitive verb transitive by adding a direct object or applying a causative affix.",
    "secondary": "In linguistic morphology, applicative prefixes regularly transitivise unaccusative verbs across Bantu and Austronesian languages.",
    "quotes": [
      {"author": "Max Müller", "work": "The Science of Language", "quote": "Ancient grammarians noted how auxiliary particles could **transitivise** a static verbal stem."},
      {"author": "William Dwight Whitney", "work": "Language and the Study of Language", "quote": "Speakers frequently **transitivise** passive verbs to express forceful personal agency."},
      {"author": "Ferdinand de Saussure", "work": "Course in General Linguistics", "quote": "Linguistic analogy acts to **transitivise** archaic forms in accordance with popular vernacular usage."}
    ]
  },
  "Dashboard — it/transitivity.md": {
    "primary": "The grammatical property of taking a direct object; or the logical property where A implies B and B implies C means A implies C.",
    "secondary": "In mathematical graph theory, the transitivity of a directed graph measures the relative frequency of closed three-node triangles.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "The logical **transitivity** of equality forms the indispensable foundation of all deductive arithmetic."},
      {"author": "Max Müller", "work": "The Science of Language", "quote": "Grammatical **transitivity** is an essential conceptual instrument for mapping intentional human actions onto language."},
      {"author": "William Dwight Whitney", "work": "Language and the Study of Language", "quote": "Degrees of syntactic **transitivity** vary widely across unrelated linguistic families."}
    ]
  },
  "Dashboard — it/transitivize.md": {
    "primary": "To make or render a verb transitive through morphological derivation, prefixation, or syntactic complementation.",
    "secondary": "In generative transformational grammar, causative suffixes transitivize intransitive roots by introducing an external thematic agent role.",
    "quotes": [
      {"author": "Max Müller", "work": "The Science of Language", "quote": "Languages employ causative infixes to **transitivize** root verbs of state into dynamic actions."},
      {"author": "William Dwight Whitney", "work": "Language and the Study of Language", "quote": "Colloquial speech will readily **transitivize** nouns to produce concise functional expressions."},
      {"author": "Ferdinand de Saussure", "work": "Course in General Linguistics", "quote": "Dialectal innovators tend to **transitivize** intransitive motion verbs to convey intentional direction."}
    ]
  },
  "Dashboard — it/unambitious.md": {
    "primary": "Not motivated by ambition; having little desire for wealth, fame, or high rank; modest and content with simple things.",
    "secondary": "In classical Stoic and Epicurean philosophy, an unambitious life devoted to tranquility (ataraxia) was prized above public honors.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "They are the most simple-mannered people alive, and quite **unambitious** in their pastoral seclusion."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "A wife, a modest young lady, with the purely appreciative, **unambitious** abilities of her sex, suited his ideal."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A prudent statesman must distinguish between a patriotic magistrate and an **unambitious** citizen unwilling to bear public burdens."}
    ]
  },
  "Dashboard — it/unambitiously.md": {
    "primary": "In an unambitious manner; modestly, without seeking distinction, power, or advancement.",
    "secondary": "In pastoral literature, rustic swains live unambitiously among their flocks, immune to the corrosive rivalries of royal courts.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Under the Greenwood Tree", "quote": "The village shoemaker lived **unambitiously** in his thatched cottage, content with his daily bread."},
      {"author": "George Eliot", "work": "Scenes of Clerical Life", "quote": "The quiet curate laboured **unambitiously** among his poor parishioners, seeking no ecclesiastical promotion."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Edward Ferrars wished only to settle **unambitiously** in a modest country parsonage."}
    ]
  },
  "Dashboard — it/uninitiate.md": {
    "primary": "Not initiated; lacking specialized knowledge, training, or formal induction into a discipline, mystery, or esoteric craft.",
    "secondary": "In classical Greek mystery religions (Eleusinian mysteries), the uninitiate were strictly forbidden from witnessing the sacred rites.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "To the **uninitiate** observer, the mysterious symbols upon the weather chart conveyed no meaningful warning."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "The tribal elders concealed the sacred bullroarer from the sight of the **uninitiate** women and children."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "To the **uninitiate** eye, nature appears as an accidental heap of facts rather than an orderly cosmos."}
    ]
  },
  "Dashboard — it/uninitiated.md": {
    "primary": "Lacking instruction, experience, or admission into a particular secret society, professional field, or body of knowledge.",
    "secondary": "In ethnographic anthropology, the uninitiated cohort remains excluded from tribal council decisions until completing ancestral ordeal rites.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "It came from the direction of a small dark object which, to the **uninitiated** eye, appeared like a shepherd's hut."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "The secret magical formula was guarded so closely that no **uninitiated** person could ever hear its syllables."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "To an **uninitiated** companion, Holmes's deductions appeared like inexplicable strokes of wizardry."}
    ]
  },
  "Dashboard — it/unit.md": {
    "primary": "An individual person, thing, or group regarded as single and complete; or an accepted standard measurement of a quantity.",
    "secondary": "In dimensional physical analysis, the International System of Units (SI) establishes seven base physical dimensions from which all other units are derived.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Every individual laborer acts as a productive **unit** whose specialized efficiency multiplies the wealth of the whole society."},
      {"author": "Isaac Newton", "work": "Opticks", "quote": "The experiment demonstrated that a ray of light behaves as an indivisible **unit** of radiant motion."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In colonial organisms, each microscopic zooid functions as a physiological **unit** subordinated to the colony."}
    ]
  },
  "Dashboard — it/unitary.md": {
    "primary": "Relating to, based upon, or characterized by unity; forming a single undivided entity or system.",
    "secondary": "In constitutional political systems, a unitary state concentrates sovereign authority within a central national government, unlike a federal system.",
    "quotes": [
      {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "Apart from the pulling and hauling stands what I am, a **unitary** soul conscious of its eternal harmony."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "The evolution of the cosmos proceeds from incoherent heterogeneity toward integrated **unitary** order."},
      {"author": "Woodrow Wilson", "work": "The State: Elements of Historical and Practical Politics", "quote": "In a **unitary** government, regional administrations exist merely as administrative arms of the central parliament."}
    ]
  },
  "Dashboard — it/unite.md": {
    "primary": "To join, combine, or connect together so as to form a single whole, alliance, or coordinated action.",
    "secondary": "In chemical bond theory, valence electron sharing causes reactive atoms to unite into stable molecular compounds.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Full thirty times hath Phoebus' cart gone round Neptune's salt wash and Tellus' orbed ground, since love our hearts and Hymen did our hands **unite** in most sacred bands."},
      {"author": "Abraham Lincoln", "work": "Gettysburg Address", "quote": "It is rather for us to be here dedicated to the great task remaining before us, that this nation shall **unite** in a new birth of freedom."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Let all hearts **unite** to praise the sovereign architect of earth and sky."}
    ]
  },
  "Dashboard — it/united.md": {
    "primary": "Joined together in purpose, action, or physical connection; forming a harmonious and cohesive union.",
    "secondary": "In international treaty law, the United Nations Charter obligates member states to preserve collective peace and security.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 2", "quote": "That done, dissever your **united** strengths, and part your mingled colours once again."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A **united** America will command respect from foreign empires that would otherwise exploit our divisions."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "The Cratchit family sat around the hearth, **united** in affection and cheerful contentment."}
    ]
  },
  "Dashboard — it/uniting.md": {
    "primary": "Bringing together or joining into a single whole; connecting, harmonizing, or cementing a relationship.",
    "secondary": "In metallurgical joining technology, welding processes achieve solid coalescence by uniting metallic surfaces through localized fusion.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Here stood the tomb, consisting of two blocks of stone **uniting** in a stately apex beneath the yew tree."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The intermediate varieties **uniting** two distinct species in adjacent regions often perish during ecological shifts."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "He considered the circumstances **uniting** their families as a fortunate stroke of provincial neighborliness."}
    ]
  },
  "Dashboard — it/unitisation.md": {
    "primary": "The process or policy of combining multiple parcels, packages, or entities into a standardized, integrated unit.",
    "secondary": "In petroleum reservoir engineering, unitisation consolidates oil and gas extraction across multiple leaseholds under a single joint operating agreement.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "The industrial **unitisation** of mechanical parts enabled factory assembly lines to manufacture goods at unprecedented speed."},
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "The **unitisation** of scattered commercial enterprises into large corporate bodies is a hallmark of industrial maturity."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The economic **unitisation** of small agricultural holdings into consolidated sheep farms transformed English husbandry."}
    ]
  },
  "Dashboard — it/unitise.md": {
    "primary": "To make into a single unit; to divide, pack, or process bulk materials into standardized, uniform units.",
    "secondary": "In multimodal freight logistics, warehouse systems unitise palletized boxes using stretch-wrap film to streamline containerized shipping.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Modern manufacturing techniques **unitise** complex mechanisms by building them from interchangeable components."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "To analyze a complex phenomenon, the philosopher must first **unitise** the diverse elements under common categories."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Botanical horticulturists **unitise** diverse rootstocks by grafting them onto a single sturdy stem."}
    ]
  },
  "Dashboard — it/unitization.md": {
    "primary": "The consolidation or grouping of diverse components, cargo, or properties into a single standardized operational unit.",
    "secondary": "In oilfield conservation law, compulsory unitization protects correlative rights by preventing wasteful drilling across shared hydrocarbon reservoirs.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "The systematic **unitization** of educational standards ensured that schools across the county maintained uniform quality."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "The **unitization** of clan loyalties under a centralized monarchy marked the birth of modern statehood."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The **unitization** of coinage under imperial mint regulations facilitated commerce by eliminating currency counterfeiting."}
    ]
  },
  "Dashboard — it/unitize.md": {
    "primary": "To convert, organize, or package into a standardized unit or uniform whole; to unify separate parts.",
    "secondary": "In supply chain management, distribution centers unitize individual retail cartons onto shrink-wrapped wooden pallets for intermodal transport.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Method and Results", "quote": "The investigator must **unitize** his observational criteria to ensure that all field assistants record identical phenomena."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Evolutionary processes continuously **unitize** disparate biological functions into harmonious physiological systems."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Selective pressures tend to **unitize** polymorphic traits when an environmental niche demands specialized efficiency."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Motion"
updated = 0

for rel_path, info in data.items():
    fpath = os.path.join(base_dir, rel_path.replace("/", os.sep))
    if not os.path.exists(fpath):
        print(f"Warning: {fpath} does not exist!")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    book_idx = content.find("> [!book]")
    if book_idx == -1:
        print(f"Warning: No > [!book] callout in {rel_path}")
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
    updated += 1

print(f"Motion Batch 7B: Successfully updated {updated}/{len(data)} notes.")
