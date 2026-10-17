import json
import os
import subprocess

data = {
  "Dashboard \u2014 met\\metal.md": {
    "primary": "Any of a category of electropositive chemical elements typically characterized by metallic luster, malleability, ductility, and high electrical and thermal conductivity.",
    "secondary": "In astrophysics and stellar nucleosynthesis, any chemical element heavier than hydrogen and helium contained within stars or the interstellar medium.",
    "quotes": [
      {"author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "The combustion of a **metal** in oxygen produces a calx or metallic oxide while absorbing a portion of the atmospheric air."},
      {"author": "Georgius Agricola", "work": "De Re Metallica", "quote": "The miner must possess a deep understanding of veins and rocks before attempting to extract precious **metal** from the subterranean depths."},
      {"author": "Subrahmanyan Chandrasekhar", "work": "An Introduction to the Study of Stellar Structure", "quote": "Stellar evolution models trace how successive burning phases enrich the galactic interstellar gas with heavy **metal** abundance."}
    ]
  },
  "Dashboard \u2014 met\\metalogic.md": {
    "primary": "The branch of philosophical logic that investigates the formal properties, consistency, completeness, and decidability of logical systems and formal languages.",
    "secondary": "In mathematical foundations and proof theory, metalogic evaluates deductive systems from an external, meta-linguistic standpoint rather than operating within the syntax.",
    "quotes": [
      {"author": "Alfred Tarski", "work": "Logic, Semantics, Metamathematics", "quote": "The semantic definition of truth requires a rigorous separation between the object language and the **metalogic** used to analyze it."},
      {"author": "Kurt Gödel", "work": "On Formally Undecidable Propositions", "quote": "Our mathematical demonstration belongs to **metalogic**, proving that axiomatic arithmetic cannot demonstrate its own internal consistency."},
      {"author": "Willard Van Orman Quine", "work": "Philosophy of Logic", "quote": "Questions concerning the completeness and decidability of formal quantificational systems form the very core of **metalogic**."}
    ]
  },
  "Dashboard \u2014 met\\metaphase.md": {
    "primary": "The intermediate stage of eukaryotic mitosis and meiosis during which duplicated chromosomes condense and align along the equatorial spindle plate.",
    "secondary": "In clinical cytogenetics and karyotyping, cell division is artificially arrested at metaphase with colchicine to visualize and photograph chromosome morphology.",
    "quotes": [
      {"author": "Walther Flemming", "work": "Zellsubstanz, Kern und Zelltheilung", "quote": "During **metaphase**, the nuclear threads congregate in the equatorial plane of the achromatin spindle prior to cleavage."},
      {"author": "Edmund Beecher Wilson", "work": "The Cell in Development and Heredity", "quote": "The precise alignment of paired chromosomes along the equatorial plate in **metaphase** ensures equitable distribution of hereditary determinants."},
      {"author": "Theodosius Dobzhansky", "work": "Genetics and the Origin of Species", "quote": "Cytological inspection of Drosophila salivary gland squashes at **metaphase** unveils chromosomal inversions and translocations with clarity."}
    ]
  },
  "Dashboard \u2014 met\\metaphysically.md": {
    "primary": "In a metaphysical manner; relating to fundamental ontological inquiries concerning reality, being, and transcendent first principles.",
    "secondary": "In critical philosophy and epistemology, describing reasoning that moves beyond empirical observation to investigate the a priori conditions of experience.",
    "quotes": [
      {"author": "Immanuel Kant", "work": "Critique of Pure Reason", "quote": "Space is not an empirical concept, but a necessary representation that must be understood **metaphysically** as an a priori intuition."},
      {"author": "Aristotle", "work": "Metaphysics", "quote": "To inquire into substance **metaphysically** is to seek the primary cause by which being is defined as being."},
      {"author": "René Descartes", "work": "Meditations on First Philosophy", "quote": "Having doubted all sensory testimony, I found myself compelled to establish the certainty of my own existence **metaphysically**."}
    ]
  },
  "Dashboard \u2014 met\\metaphysics.md": {
    "primary": "The foundational branch of philosophy that examines the essential nature of reality, being, existence, time, and the relation between mind and matter.",
    "secondary": "In intellectual history, named after Aristotle's treatises compiled 'after the physics' (ta meta ta physika), focusing on ontology and first causes.",
    "quotes": [
      {"author": "Aristotle", "work": "Metaphysics", "quote": "All men by nature desire to know, and the highest wisdom is that first philosophy which later commentators designated **metaphysics**."},
      {"author": "Immanuel Kant", "work": "Prolegomena to Any Future Metaphysics", "quote": "My purpose is to convince all who find it worth while to consider whether such a thing as **metaphysics** be even possible."},
      {"author": "Martin Heidegger", "work": "Being and Time", "quote": "Western philosophy from Plato onward has forgotten the central question of being, transforming fundamental ontology into classical **metaphysics**."}
    ]
  },
  "Dashboard \u2014 met\\meteor.md": {
    "primary": "A streak of light produced in the night sky when an interplanetary meteoroid vaporizes due to friction upon entering Earth's upper atmosphere; a shooting star.",
    "secondary": "In historical science and atmospheric physics, historically designated any atmospheric phenomenon, categorized into hydrometeors, lithometeors, and electrometeors.",
    "quotes": [
      {"author": "Aristotle", "work": "Meteorology", "quote": "We must treat of the upper atmosphere and investigate the fiery exhalations that appear to our eyes as a blazing **meteor**."},
      {"author": "Fred Whipple", "work": "Earth, Moon, and Planets", "quote": "High-altitude photography reveals that a bright **meteor** leaves an ionized luminous trail lingering in the mesosphere for many seconds."},
      {"author": "Carl Sagan", "work": "Cosmos", "quote": "Every burning **meteor** falling through the night reminds us of our planet's continual communion with the debris of the solar system."}
    ]
  },
  "Dashboard \u2014 met\\meteoroid.md": {
    "primary": "A small rocky or metallic body traveling through interplanetary space, ranging in size from a microscopic grain of cosmic dust to a small asteroid.",
    "secondary": "In planetary astronomy, a meteoroid becomes a meteor when incandescently entering a planetary atmosphere, and a meteorite if surviving impact on the planetary surface.",
    "quotes": [
      {"author": "Fred Whipple", "work": "The Mystery of Comets", "quote": "A fragile cometary **meteoroid** disintegrates rapidly into dust upon skimming the tenuous outer layers of Earth's atmosphere."},
      {"author": "Eugene Shoemaker", "work": "Asteroid and Comet Impacts on the Earth", "quote": "The kinetic energy released when a high-density nickel-iron **meteoroid** impacts the lunar surface excavates a crater many times its own diameter."},
      {"author": "Harold Urey", "work": "The Planets: Their Origin and Development", "quote": "Isotopic ratios in primitive chondritic material suggest that each ancient **meteoroid** preserves primordial solar nebula condensates."}
    ]
  },
  "Dashboard \u2014 met\\meter.md": {
    "primary": "The base unit of length in the International System of Units (SI), defined as the distance traveled by light in vacuum in 1/299,792,458 of a second.",
    "secondary": "In poetry and prosody, the rhythmic arrangement of syllables in a line of verse, organized into metrical feet according to stress or quantity.",
    "quotes": [
      {"author": "Max Planck", "work": "The Theory of Heat Radiation", "quote": "Universal physical constants allow us to define natural units of length, displacing the arbitrary platinum-iridium **meter** prototype bar."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The purpose of poetic **meter** is to harmonize the emotional excitement of the poet with disciplined rhythmic form."},
      {"author": "John Dryden", "work": "An Essay of Dramatic Poesy", "quote": "Rhyme and regular **meter** lend an elevated majesty to dramatic dialogue that loose prose cannot achieve."}
    ]
  },
  "Dashboard \u2014 met\\method.md": {
    "primary": "A systematic, organized procedure, technique, or established mode of inquiry used to perform an operation, achieve a goal, or discover truth.",
    "secondary": "In epistemology and scientific philosophy, the structured dialectical or empirical procedure employed to establish valid knowledge and test hypotheses.",
    "quotes": [
      {"author": "René Descartes", "work": "Discourse on Method", "quote": "I formed the resolution to employ my **method** constantly, dividing each difficulty into as many parts as possible to resolve it."},
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "Our **method** of discovering the sciences leaves little to the acuteness and strength of individual wits, placing all intellects nearly on a level."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Inductive reasoning provides the foundational **method** through which universal physical laws are inferred from particular observations."}
    ]
  },
  "Dashboard \u2014 met\\methodical.md": {
    "primary": "Characterized by, performed with, or adhering to systematic order, deliberate procedure, and regularity.",
    "secondary": "In psychology and behavioral analysis, describing cognitive habits and work practices that prioritize deliberate planning over spontaneous action.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "By **methodical** selection, breeders have created distinct varieties of domestic animals within an astonishingly brief period."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of Four", "quote": "Sherlock Holmes pursued his investigation with **methodical** calm, measuring footprints in the soft soil with extraordinary precision."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Forming **methodical** habits early in life relieves the conscious will from the burden of constantly deciding minor daily routines."}
    ]
  },
  "Dashboard \u2014 met\\methodically.md": {
    "primary": "In a methodical, orderly, and systematic manner; following a deliberate and disciplined procedure step by step.",
    "secondary": "In experimental science and forensic investigation, executing protocols methodically eliminates confounding variables and ensures reproducible conclusions.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "The scientific investigator proceeds **methodically**, verifying each observation before venturing to synthesize a general hypothesis."},
      {"author": "Edgar Allan Poe", "work": "The Murders in the Rue Morgue", "quote": "Dupin examined the sealed apartment **methodically**, testing every shutter and latch until he discovered the hidden spring."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "I proceeded **methodically** through every class of liquid conductors, recording the precise electric currents generated under uniform conditions."}
    ]
  },
  "Dashboard \u2014 met\\methodism.md": {
    "primary": "Rigid or systematic adherence to a particular method, routine, or set of formal procedural rules.",
    "secondary": "In ecclesiastical history, the Christian Protestant evangelical movement founded in 18th-century England by John and Charles Wesley, emphasizing personal holiness and structured piety.",
    "quotes": [
      {"author": "John Wesley", "work": "The Journal of John Wesley", "quote": "Our detractors mockingly named our pursuit of holiness **methodism**, yet we gladly embrace regular discipline in following Christ."},
      {"author": "George Whitefield", "work": "Sermons on Various Subjects", "quote": "The true spirit of **methodism** consists not in external forms or party names, but in a heart transformed by regenerating grace."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "Whatever faults critics find in early **methodism**, it stirred the stagnant spiritual waters of eighteenth-century English life."}
    ]
  },
  "Dashboard \u2014 met\\methodist.md": {
    "primary": "A person who acts according to a strict method; historically, an ancient medical practitioner belonging to the Methodic school of Asclepiades.",
    "secondary": "In religious history, an adherent or member of the Methodist Christian denomination, characterized by structured prayer, class meetings, and evangelical outreach.",
    "quotes": [
      {"author": "John Wesley", "work": "A Plain Account of the People Called Methodists", "quote": "A **methodist** is one who lives according to the method laid down in the Holy Scriptures, loving the Lord with all his heart."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The strict morals and rigorous discipline of the **methodist** societies contributed visibly to the industry and sobriety of the common people."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "Dinah Morris, the gentle **methodist** preacher, spoke with an earnest simplicity that moved the villagers to tears on the green."}
    ]
  },
  "Dashboard \u2014 met\\metic.md": {
    "primary": "A resident alien in an ancient Greek city-state (notably classical Athens) who enjoyed civil liberties and legal protection but possessed no citizen franchise.",
    "secondary": "In classical Athenian law and economic sociology, metics engaged extensively in overseas commerce and craft production, paying a specialized poll tax (metoikion).",
    "quotes": [
      {"author": "Aristotle", "work": "Politics", "quote": "A citizen is not a citizen simply by dwelling in a place, for resident aliens classed as a **metic** share the domicile but lack political office."},
      {"author": "Lysias", "work": "Against Eratosthenes", "quote": "My father Cephalus lived thirty years in Athens as a loyal **metic**, manufacturing shields and honoring the democratic laws of the city."},
      {"author": "Demosthenes", "work": "Against Neaera", "quote": "The law strictly forbids any **metic** from contracting a sacred marriage reserved exclusively for Athenian citizens."}
    ]
  },
  "Dashboard \u2014 met\\metical.md": {
    "primary": "Pertaining to, characteristic of, or resembling a metic or resident alien in classical Greek society.",
    "secondary": "In classical legal history and epigraphy, describing the distinct judicial status, tax burdens, and property restrictions imposed on alien residents in Greek poleis.",
    "quotes": [
      {"author": "George Grote", "work": "A History of Greece", "quote": "The Athenian state maintained a flourishing economy largely through the industrious labor of its **metical** population."},
      {"author": "M. I. Finley", "work": "The Ancient Economy", "quote": "The **metical** status imposed distinct fiscal duties, including the metoikion tax and exclusion from agricultural land ownership."},
      {"author": "A. H. M. Jones", "work": "Athenian Democracy", "quote": "Legal cases involving **metical** litigants were adjudicated before the polemarch, reflecting their distinct judicial category in the republic."}
    ]
  },
  "Dashboard \u2014 met\\micrometeor.md": {
    "primary": "A microscopic or submillimeter extraterrestrial particle that enters the upper atmosphere, vaporizing to create a faint, transient ionization trail.",
    "secondary": "In upper-atmospheric physics and aeronomy, micrometeors supply metallic ions that influence the electrical conductivity and chemical composition of the mesosphere.",
    "quotes": [
      {"author": "Fred Whipple", "work": "The Mystery of Comets", "quote": "Radar tracking detects the ionization column produced as each interplanetary **micrometeor** disintegrates high above the stratosphere."},
      {"author": "James Van Allen", "work": "Origins of Magnetospheric Physics", "quote": "Rocket sensors deployed during meteor showers recorded an influx of charged particles originating from **micrometeor** ablation."},
      {"author": "Carl Sagan", "work": "The Cosmic Connection", "quote": "Countless dust grains from pulverized comets burn away as a faint **micrometeor**, gently seeding our atmosphere with extraterrestrial minerals."}
    ]
  },
  "Dashboard \u2014 met\\micrometeoric.md": {
    "primary": "Pertaining to, caused by, or consisting of microscopic meteoroids or extraterrestrial dust particles.",
    "secondary": "In space exploration and lunar geology, describing the ongoing surface abrasion, cratering, and soil gardening of airless planetary bodies by cosmic dust impacts.",
    "quotes": [
      {"author": "Eugene Shoemaker", "work": "Geology of the Moon", "quote": "The powdery texture of the lunar regolith results from billions of years of continuous **micrometeoric** bombardment upon basaltic bedrock."},
      {"author": "Harold Urey", "work": "The Planets: Their Origin and Development", "quote": "Glassy spherules discovered in lunar dust samples provide physical evidence of intense melting caused by **micrometeoric** velocity impacts."},
      {"author": "Wernher von Braun", "work": "The Mars Project", "quote": "Long-duration interplanetary spacecraft require multi-layered shielding to guard sensitive propellant tanks against **micrometeoric** puncture."}
    ]
  },
  "Dashboard \u2014 met\\unmethodical.md": {
    "primary": "Lacking systematic order, plan, or method; disorganized, haphazard, or irregular in operation.",
    "secondary": "In administrative theory and literary criticism, describing thought processes or research efforts that proceed without deliberate structural coherence.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "His reading was vast but **unmethodical**, gathering jewels of wisdom without arranging them into an orderly cabinet of knowledge."},
      {"author": "John Stuart Mill", "work": "Autobiography", "quote": "An **unmethodical** course of study leaves the youthful intellect prone to confusing rhetorical assertion with demonstrated proof."},
      {"author": "Walter Bagehot", "work": "The English Constitution", "quote": "The English constitution may appear chaotic and **unmethodical** to theoretical jurists, yet it functions with astonishing practical vitality."}
    ]
  },
  "Dashboard \u2014 morph\\allomorph.md": {
    "primary": "Any of two or more alternative phonetic manifestations or realizations of a single morpheme in a particular linguistic context.",
    "secondary": "In crystallography and mineralogy, any of the diverse crystalline forms assumed by a single chemical substance without altering its elemental identity.",
    "quotes": [
      {"author": "Leonard Bloomfield", "work": "Language", "quote": "The plural suffix in English exhibits phonologically conditioned variants, each functioning as an **allomorph** of the underlying plural morpheme."},
      {"author": "Noam Chomsky", "work": "The Morphophonemics of Modern Hebrew", "quote": "Morphophonemic transformation rules map abstract lexical entries into the specific **allomorph** appropriate to its phonological environment."},
      {"author": "Edward Sapir", "work": "Language: An Introduction to the Study of Speech", "quote": "Grammatical unity often underlies phonetic divergence, where each distinct **allomorph** preserves the original functional value."}
    ]
  },
  "Dashboard \u2014 morph\\allomorphic.md": {
    "primary": "Pertaining to, functioning as, or characterized by an allomorph.",
    "secondary": "In descriptive linguistics, describing positional variation in word stems or affixes governed by surrounding phonemes, stress, or morphological categories.",
    "quotes": [
      {"author": "Roman Jakobson", "work": "Selected Writings", "quote": "Phonological assimilation explains many instances of **allomorphic** alternation across Indo-European verbal inflection paradigms."},
      {"author": "Zellig Harris", "work": "Methods in Structural Linguistics", "quote": "By grouping complementary phonetic variants together, we establish the **allomorphic** distribution of the grammatical markers."},
      {"author": "Charles F. Hockett", "work": "A Course in Modern Linguistics", "quote": "The morpheme exists as an abstract linguistic unit whose concrete **allomorphic** expressions depend on syntactic context."}
    ]
  },
  "Dashboard \u2014 morph\\amorpha.md": {
    "primary": "A taxonomic genus of deciduous shrubs in the pea family Fabaceae native to North America, commonly known as false indigo or leadplant.",
    "secondary": "In systematic botany, *Amorpha* is distinguished from all other legumes by having flowers reduced to a single petal (the banner), lacking the keel and wings.",
    "quotes": [
      {"author": "Carl Linnaeus", "work": "Species Plantarum", "quote": "We establish the genus **Amorpha**, noting that its anomalous corolla possesses only a single standard petal."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Along river banks of the Mississippi valley, **Amorpha** fruticosa forms dense thickets with its pinnate leaves and violet spikes."},
      {"author": "John Torrey", "work": "A Flora of North America", "quote": "Prairie leadplant, classed under **Amorpha**, thrives in dry gravelly soil, where its deep roots resist summer droughts."}
    ]
  },
  "Dashboard \u2014 morph\\amorphophallus.md": {
    "primary": "A taxonomic genus of tropical and subtropical tuberous plants in the family Araceae, famous for colossal inflorescences that emit powerful odors of decaying flesh.",
    "secondary": "In reproductive botanical ecology, *Amorphophallus titanum* (the titan arum) employs thermogenesis to vaporize volatile dimethyl oligosulfides, attracting pollinating carrion flies.",
    "quotes": [
      {"author": "Odoardo Beccari", "work": "Wanderings in the Great Forests of Borneo", "quote": "In the rainforests of Sumatra, I encountered the titanic spadix of **Amorphophallus**, whose magnificent stature astounded the botanical world."},
      {"author": "David Attenborough", "work": "The Private Life of Plants", "quote": "The monstrous inflorescence of **Amorphophallus** generates internal heat, dispersing foul carrion odors that summon sweat bees from miles away."},
      {"author": "Peter Boyce", "work": "The Araceae of Malesia", "quote": "The massive subterranean corm of **Amorphophallus** stores sufficient starch reserves to fuel the rapid unfurling of its monumental flower."}
    ]
  },
  "Dashboard \u2014 morph\\amorphous.md": {
    "primary": "Lacking a definite shape, form, or organized physical structure; shapeless or unclassifiable.",
    "secondary": "In solid-state physics and crystallography, designating non-crystalline solids (such as glass and vitreous silica) whose atoms lack long-range periodic order.",
    "quotes": [
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "Certain precipitated minerals remain an **amorphous** mass until prolonged digestion permits regular crystal facets to appear."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Rapid cooling of molten sulfur produces an **amorphous** and elastic substance that gradually hardens into crystalline rhombic sulfur."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Igneous glass quenched by seawater forms an **amorphous** basaltic crust lacking visible mineral grains."}
    ]
  },
  "Dashboard \u2014 morph\\anamorph.md": {
    "primary": "The asexual, mitosporic, or imperfect reproductive form or morph of a fungus, reproducing primarily via conidia or other vegetative propagules.",
    "secondary": "In systematic mycology, anamorphs often historically carried independent generic names before molecular phylogenetics connected them to their sexual teleomorphs.",
    "quotes": [
      {"author": "C. V. Subramanian", "work": "Hyphomycetes", "quote": "The conidiogenesis observed in this **anamorph** allows rapid propagation during favorable humid seasons without genetic recombination."},
      {"author": "Bryce Kendrick", "work": "The Whole Fungus", "quote": "Mycologists must coordinate binomial nomenclature to recognize when an **anamorph** corresponds to a known sexual ascomycete."},
      {"author": "John Webster", "work": "Introduction to Fungi", "quote": "In many fungal pathogens, the **anamorph** is the only stage encountered in clinical infections, making conidial morphology vital for diagnosis."}
    ]
  },
  "Dashboard \u2014 morph\\anamorphic.md": {
    "primary": "Pertaining to, producing, or characterized by distorted optical projection, unequal lateral magnification, or transformative morphological change.",
    "secondary": "In widescreen cinematography and optical lens design, describing cylindrical lenses that optically compress an image horizontally onto standard film for subsequent optical decompression.",
    "quotes": [
      {"author": "Henri Chrétien", "work": "Hypergonar Anamorphic Optics", "quote": "By introducing cylindrical lenses into the optical train, our **anamorphic** system captures a panoramic field of view on standard film stock."},
      {"author": "David Bordwell", "work": "The Classical Hollywood Cinema", "quote": "The adoption of **anamorphic** widescreen formats in the 1950s revolutionized cinematic framing, demanding new approaches to narrative staging."},
      {"author": "Erwin Panofsky", "work": "Perspective as Symbolic Form", "quote": "Renaissance artists mastered **anamorphic** projection, hiding subtle political and allegorical meanings within apparently distorted murals."}
    ]
  },
  "Dashboard \u2014 morph\\anamorphism.md": {
    "primary": "Metamorphism occurring in deep zones of the Earth's crust characterized by intense heat and confining pressure, leading to rock compaction and mineral recrystallization.",
    "secondary": "In structural petrology, anamorphism contrasts with katamorphism (weathering and disintegration near the surface), forming dense metamorphic schists and gneisses.",
    "quotes": [
      {"author": "Charles Richard Van Hise", "work": "A Treatise on Metamorphism", "quote": "Deep within the crust, **anamorphism** transforms porous sediments into crystalline schists through recrystallization under immense lithostatic load."},
      {"author": "Reginald Aldworth Daly", "work": "Igneous Rocks and the Depths of the Earth", "quote": "Thermal metamorphism associated with batholithic intrusions demonstrates the powerful mineralogical reconstitutions typical of **anamorphism**."},
      {"author": "Alfred Harker", "work": "Metamorphism", "quote": "The stress conditions driving **anamorphism** produce foliation and the growth of dense, high-pressure porphyroblasts like garnet and kyanite."}
    ]
  },
  "Dashboard \u2014 morph\\anamorphosis.md": {
    "primary": "A distorted projection or drawing that appears deformed until viewed from a specific oblique angle or through a specialized optical device like a curved mirror.",
    "secondary": "In evolutionary biology and entomology, the gradual post-embryonic addition of body segments during successive molts without sudden metamorphic changes.",
    "quotes": [
      {"author": "Jurgis Baltrušaitis", "work": "Anamorphic Art", "quote": "Holbein's famous skull in 'The Ambassadors' is an iconic instance of perspective **anamorphosis**, requiring the viewer to stand at the canvas edge."},
      {"author": "Erwin Panofsky", "work": "Studies in Iconology", "quote": "The mathematical play of **anamorphosis** intrigued Baroque intellectuals as a metaphor for the relativity of sensory perception."},
      {"author": "Albrecht Dürer", "work": "The Painter's Manual", "quote": "Through geometric construction of perspective grids, one can create an intentional **anamorphosis** that resolves into clarity from a single viewpoint."}
    ]
  },
  "Dashboard \u2014 morph\\anthropomorphic.md": {
    "primary": "Attributing human characteristics, emotions, intentions, or bodily forms to non-human entities, deities, animals, or inanimate objects.",
    "secondary": "In comparative mythology and cognitive anthropology, analyzing how cultural religions project human bodily faculties and social structures onto celestial gods.",
    "quotes": [
      {"author": "Xenophanes", "work": "Fragments", "quote": "Mortals deem that the gods are begotten as they are, fashioning divine forms with **anthropomorphic** faces, garments, and voices."},
      {"author": "David Hume", "work": "The Natural History of Religion", "quote": "There is a universal tendency among mankind to conceive all beings like themselves, giving rise to **anthropomorphic** polytheism."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "We must avoid careless **anthropomorphic** interpretations, yet animal expressions often share common physiological origins with human emotion."}
    ]
  },
  "Dashboard \u2014 morph\\anthropomorphise.md": {
    "primary": "To ascribe human characteristics, emotions, motivations, or intentions to animals, inanimate things, or abstract concepts (variant British spelling).",
    "secondary": "In behavioral ethology, warning researchers against anthropomorphising non-human actions to avoid cognitive projection and biased interpretations.",
    "quotes": [
      {"author": "Frans de Waal", "work": "Are We Smart Enough to Know How Smart Animals Are?", "quote": "While we should not anthropomorphise uncritically, denying all shared cognitive mechanisms between humans and apes is equally unscientific."},
      {"author": "Konrad Lorenz", "work": "King Solomon's Ring", "quote": "The romantic tendency to **anthropomorphise** animal companions frequently blinds the owner to their authentic biological needs."},
      {"author": "Jane Goodall", "work": "In the Shadow of Man", "quote": "Early critics warned that to **anthropomorphise** the chimpanzees by naming them was unscientific, yet their individual personalities proved undeniable."}
    ]
  },
  "Dashboard \u2014 morph\\anthropomorphism.md": {
    "primary": "The attribution of human traits, emotions, intentions, or physiological behaviors to non-human entities such as animals, deities, or natural forces.",
    "secondary": "In philosophy of science and cognitive ethology, anthropomorphism serves as an innate cognitive heuristic for social prediction that can distort objective analysis.",
    "quotes": [
      {"author": "Ludwig Feuerbach", "work": "The Essence of Christianity", "quote": "The secret of theology is anthropology: religious **anthropomorphism** simply projects the idealized essence of human nature into the heavens."},
      {"author": "Edward Westermarck", "work": "The Origin and Development of the Moral Ideas", "quote": "Primitive taboos reflect widespread **anthropomorphism**, treating trees and rocks as sentient agents capable of deliberate malice."},
      {"author": "B. F. Skinner", "work": "About Behaviorism", "quote": "Behaviorism seeks to purge psychological science of lingering **anthropomorphism**, explaining actions through contingencies of reinforcement."}
    ]
  },
  "Dashboard \u2014 morph\\anthropomorphize.md": {
    "primary": "To interpret, represent, or characterize non-human beings, objects, or phenomena as possessing human attributes or emotional states.",
    "secondary": "In artificial intelligence and human-computer interaction, observers tend to anthropomorphize conversational models, falsely inferring subjective empathy.",
    "quotes": [
      {"author": "Frans de Waal", "work": "Chimpanzee Politics", "quote": "When we observe a primate reconciliation embrace, to **anthropomorphize** may actually provide a more parsimonious evolutionary hypothesis than radical behaviorism."},
      {"author": "Douglas Hofstadter", "work": "Gödel, Escher, Bach", "quote": "We readily **anthropomorphize** complex computer programs because our brains are hardwired to attribute intentionality to patterned responses."},
      {"author": "E. O. Wilson", "work": "Sociobiology: The New Synthesis", "quote": "Field entomologists must resist the temptation to **anthropomorphize** ant colonies as little human kingdoms governed by conscious monarchs."}
    ]
  },
  "Dashboard \u2014 morph\\anthropomorphous.md": {
    "primary": "Having human form, shape, or resemblance; exhibiting bodily features resembling those of human beings.",
    "secondary": "In comparative anatomy and primatology, historically applied to higher apes (*Hominoidea*) whose skeletal morphology and facial muscles closely resemble humans.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "The structural differences between man and the highest **anthropomorphous** apes are smaller than those between the gorilla and the lower monkeys."},
      {"author": "Richard Owen", "work": "On the Characters of the Class Mammalia", "quote": "The cranial proportions and bipedal poise of modern man distinguish him decisively from the most **anthropomorphous** troglodytes."},
      {"author": "Georges Cuvier", "work": "The Animal Kingdom", "quote": "Naturalists have often debated the classification of the orangutan, noting its astonishingly **anthropomorphous** facial structure."}
    ]
  },
  "Dashboard \u2014 morph\\apomorphine.md": {
    "primary": "A dopamine receptor agonist derived chemically by heating morphine with concentrated hydrochloric acid, traditionally utilized as a rapid-acting emetic.",
    "secondary": "In clinical neurology and movement disorder therapeutics, apomorphine is administered as a subcutaneous rescue medication for sudden 'off' freezing episodes in Parkinson's disease.",
    "quotes": [
      {"author": "Arvid Carlsson", "work": "Brain Dopamine and Movement Disorders", "quote": "Early pharmacological experiments demonstrated that **apomorphine** acts directly on central dopamine receptors, reversing reserpine-induced akinesia."},
      {"author": "Louis S. Goodman", "work": "Goodman & Gilman's The Pharmacological Basis of Therapeutics", "quote": "Subcutaneous administration of **apomorphine** provides rapid relief for severe hypomobility episodes in Parkinsonian patients unresponsive to oral levodopa."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "The dramatic awakening of frozen post-encephalitic patients foreshadowed modern dopamine therapies, including the targeted use of **apomorphine**."}
    ]
  },
  "Dashboard \u2014 morph\\apomorphy.md": {
    "primary": "An evolutionary novelty or derived character state that evolved in an ancestral lineage and distinguishes a clade from other taxa.",
    "secondary": "In phylogenetic systematics (cladistics), an apomorphy shared among multiple descendant lineages (synapomorphy) provides the sole valid basis for defining monophyletic groups.",
    "quotes": [
      {"author": "Willi Hennig", "work": "Phylogenetic Systematics", "quote": "Only the shared derived character state, or synapomorphy derived from an ancestral **apomorphy**, demonstrates genuine evolutionary relationship."},
      {"author": "Ernst Mayr", "work": "Principles of Systematic Zoology", "quote": "The cladistic method insists that primitive traits be segregated from an **apomorphy** when constructing phylogenetic trees."},
      {"author": "Douglas Futuyma", "work": "Evolutionary Biology", "quote": "The presence of feathers in birds represents an **apomorphy** inherited from their theropod dinosaur ancestors."}
    ]
  },
  "Dashboard \u2014 morph\\autapomorphy.md": {
    "primary": "A distinctive derived character state or evolutionary trait unique to a single terminal evolutionary lineage or species.",
    "secondary": "In cladistics, an autapomorphy distinguishes a taxon from its closest relatives but is uninformative for resolving branching relationships within a clade.",
    "quotes": [
      {"author": "Willi Hennig", "work": "Phylogenetic Systematics", "quote": "An **autapomorphy** establishes the diagnostic identity of a single monophyletic group, but sheds no light on sister-group relationships."},
      {"author": "Edward O. Wiley", "work": "Phylogenetics: The Theory and Practice of Phylogenetic Systematics", "quote": "Because an **autapomorphy** is restricted to a single terminal taxon, cladistic algorithms exclude it when calculating parsimony trees."},
      {"author": "Colin Patterson", "work": "Molecules and Morphology in Evolution", "quote": "The unique chin morphology of Homo sapiens stands as an anatomical **autapomorphy** setting modern humans apart from archaic hominins."}
    ]
  },
  "Dashboard \u2014 morph\\automorphism.md": {
    "primary": "An isomorphism of a mathematical object, graph, or algebraic structure onto itself that preserves all internal operations and relational configurations.",
    "secondary": "In abstract algebra and Galois theory, the collection of all automorphisms of a field extension forms the Galois group, encoding symmetries of polynomial roots.",
    "quotes": [
      {"author": "Évariste Galois", "work": "Memoir on the Conditions for Solvability of Equations by Radicals", "quote": "The permutations of the roots of an algebraic equation that preserve rational relations correspond to the group of an **automorphism**."},
      {"author": "Felix Klein", "work": "Elementary Mathematics from an Advanced Standpoint", "quote": "In modern geometry, each transformation group may be viewed as an **automorphism** acting upon a space to reveal its fundamental invariants."},
      {"author": "Saunders Mac Lane", "work": "Categories for the Working Mathematician", "quote": "An **automorphism** in a category is simply an endomorphism that is simultaneously an isomorphism, having an inverse within the same hom-set."}
    ]
  },
  "Dashboard \u2014 morph\\catamorphism.md": {
    "primary": "In category theory and theoretical computer science, the unique homomorphism from an initial algebra to another algebra; a generalized fold operation.",
    "secondary": "In functional programming language design, catamorphisms provide structured, non-recursive abstractions for decomposing and aggregating algebraic data types like lists and trees.",
    "quotes": [
      {"author": "Erik Meijer", "work": "Functional Programming with Bananas, Lenses, Envelopes and Barbed Wire", "quote": "A **catamorphism** formalizes structural recursion on inductive datatypes, replacing ad hoc recursive loops with formal algebraic folds."},
      {"author": "Philip Wadler", "work": "Theorems for Free!", "quote": "Because every datatype with an initial algebra possesses a unique **catamorphism**, programs can be transformed and optimized automatically."},
      {"author": "Benjamin C. Pierce", "work": "Basic Category Theory for Computer Scientists", "quote": "The universal property of the initial algebra guarantees that for any target algebra there is one and only one **catamorphism**."}
    ]
  },
  "Dashboard \u2014 morph\\dimorphic.md": {
    "primary": "Occurring in, characterized by, or displaying two distinct physical forms, colors, shapes, or life-cycle phases within the same species or substance.",
    "secondary": "In evolutionary biology and physical anthropology, sexually dimorphic traits (such as body mass or plumage) reflect sexual selection and mating competition.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man, and Selection in Relation to Sex", "quote": "Many bird species are strikingly **dimorphic**, the male bearing brilliant nuptial plumage while the female remains cryptically colored."},
      {"author": "Ernst Mayr", "work": "Animal Species and Evolution", "quote": "A population may remain stably **dimorphic** when disruptive selection favors two distinct feeding morphs within a single habitat."},
      {"author": "Theodosius Dobzhansky", "work": "Genetics of the Evolutionary Process", "quote": "Chromosomal inversions often maintain a **dimorphic** genetic polymorphism that provides adaptive flexibility across changing seasons."}
    ]
  },
  "Dashboard \u2014 morph\\dimorphism.md": {
    "primary": "The existence within a single species, population, or chemical substance of two distinctly different forms, colors, or structural variants.",
    "secondary": "In medical mycology, dimorphism refers to fungi (such as *Blastomyces dermatitidis*) that grow as filamentous molds at 25°C but transition into pathogenic yeasts at 37°C in host tissues.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "Heterostylous **dimorphism** in primroses ensures cross-pollination by matching the anther heights of one form to the stigma heights of the other."},
      {"author": "Ronald Fisher", "work": "The Genetical Theory of Natural Selection", "quote": "Balanced **dimorphism** can be stably maintained in a population whenever each morph enjoys a selective advantage when rare."},
      {"author": "John Webster", "work": "Introduction to Fungi", "quote": "Thermal **dimorphism** is crucial for fungal pathogenesis, enabling saprophytic mold spores to germinate as invasive yeast cells inside human lungs."}
    ]
  },
  "Dashboard \u2014 morph\\dimorphous.md": {
    "primary": "Having, appearing in, or characterized by two different forms, crystalline structures, or morphological phases.",
    "secondary": "In mineralogy and crystallographic chemistry, describing substances (such as calcium carbonate, forming calcite and aragonite) that crystallize into two distinct crystal systems.",
    "quotes": [
      {"author": "René Just Haüy", "work": "Traité de minéralogie", "quote": "Substances that are chemically identical yet crystallize under two incompatible geometric forms are termed **dimorphous**."},
      {"author": "J. D. Dana", "work": "A System of Mineralogy", "quote": "Carbon provides the supreme example of a **dimorphous** element, manifesting as soft graphite and adamantine diamond."},
      {"author": "Eilhard Mitscherlich", "work": "Sur la relation qui existe entre la forme cristalline et les proportions chimiques", "quote": "Sulfur cooling from fusion forms needle-like monoclinic prisms, proving that a single body can be truly **dimorphous**."}
    ]
  },
  "Dashboard \u2014 morph\\dysmorphic.md": {
    "primary": "Having an abnormal, malformed, or atypical anatomical structure or physical development.",
    "secondary": "In clinical genetics and pediatrics, dysmorphic facial and skeletal features serve as crucial phenotypic markers for diagnosing underlying chromosomal anomalies or genetic syndromes.",
    "quotes": [
      {"author": "David W. Smith", "work": "Recognizable Patterns of Human Malformation", "quote": "A thorough clinical evaluation for minor **dysmorphic** features often yields the first clue toward identifying rare congenital syndromes."},
      {"author": "Robert Gorlin", "work": "Syndromes of the Head and Neck", "quote": "Craniofacial dysmorphologists categorize abnormal calvarial contours as **dysmorphic** developments secondary to premature suture fusion."},
      {"author": "John M. Opitz", "work": "The Developmental Field Concept in Clinical Genetics", "quote": "When multiple **dysmorphic** signs cluster in a newborn, we evaluate whether they stem from a single localized developmental field disruption."}
    ]
  },
  "Dashboard \u2014 morph\\dysmorphophobia.md": {
    "primary": "An obsessive, distressing psychiatric preoccupation with an imagined or grossly exaggerated defect in one's physical appearance; body dysmorphic disorder.",
    "secondary": "In clinical psychiatry and psychopathology, dysmorphophobia is characterized by persistent anxiety, compulsive mirror inspection or avoidance, and severe social withdrawal.",
    "quotes": [
      {"author": "Emil Kraepelin", "work": "Psychiatry: A Text-Book for Students and Physicians", "quote": "Patients afflicted by **dysmorphophobia** obsess unceasingly over imagined facial blemishes, begging physicians for surgical correction."},
      {"author": "Pierre Janet", "work": "Les Névroses", "quote": "The psychic torment of **dysmorphophobia** arises not from actual physical asymmetry, but from deep-seated obsessional ideas of personal unworthiness."},
      {"author": "Aaron T. Beck", "work": "Cognitive Therapy of Depression", "quote": "Cognitive restructuring helps patients with **dysmorphophobia** challenge their distorted self-evaluations and catastrophic appraisals of minor imperfections."}
    ]
  },
  "Dashboard \u2014 morph\\ectomorph.md": {
    "primary": "An individual having a somatotype characterized by a lean, slender body build with light bone structure, narrow shoulders, and low muscle and fat development.",
    "secondary": "In constitutional psychology and somatotyping, William Sheldon postulated that an ectomorph typically demonstrates a cerebrotonic, reflective, and introverted temperament.",
    "quotes": [
      {"author": "William H. Sheldon", "work": "The Varieties of Human Physique", "quote": "The typical **ectomorph** is distinguished by linear fragility, long delicate limbs, and a minimal accumulation of subcutaneous fat."},
      {"author": "Gordon Allport", "work": "Personality: A Psychological Interpretation", "quote": "Sheldon's description of the **ectomorph** links physical linearity with intellectual sensitivity and a preference for solitary contemplation."},
      {"author": "Hans Eysenck", "work": "The Structure of Human Personality", "quote": "Empirical correlations between an **ectomorph** somatotype and introversion prove modest, yet the typology remains historically influential."}
    ]
  },
  "Dashboard \u2014 morph\\ectomorphic.md": {
    "primary": "Pertaining to, having the physical characteristics of, or classified as an ectomorph; slender and light-framed in build.",
    "secondary": "In human biology and sports physiology, an ectomorphic morphology confers superior thermoregulatory heat dissipation due to a high surface-area-to-mass ratio.",
    "quotes": [
      {"author": "William H. Sheldon", "work": "The Varieties of Temperament", "quote": "Individuals with predominantly **ectomorphic** builds frequently display quick reflexes and an aversion to noisy social gatherings."},
      {"author": "J. M. Tanner", "work": "Foetus into Man", "quote": "During the adolescent growth spurt, children with an **ectomorphic** growth pattern experience rapid limb lengthening before gaining trunk breadth."},
      {"author": "Raymond Cattell", "work": "Description and Measurement of Personality", "quote": "Anthropometric measurements categorize the subject as distinctly **ectomorphic**, matching his high scores in cognitive absorption."}
    ]
  },
  "Dashboard \u2014 morph\\ectomorphy.md": {
    "primary": "The somatotypic condition, degree, or property of being slender, light-boned, and physically linear.",
    "secondary": "In anthropometric somatotyping (such as the Heath-Carter method), ectomorphy represents the third numerical rating, calculated from height divided by the cube root of weight.",
    "quotes": [
      {"author": "William H. Sheldon", "work": "Atlas of Men", "quote": "The third component, **ectomorphy**, measures the relative predominance of linearity and fragility in the human bodily constitution."},
      {"author": "J. M. Tanner", "work": "The Physique of the Olympic Athlete", "quote": "High-jumpers and marathon runners exhibit high scores in **ectomorphy**, reflecting the biomechanical efficiency of long, light limbs."},
      {"author": "Barbara Heath", "work": "A Modified Somatotype Method", "quote": "In our modified system, the rating of **ectomorphy** is derived objectively from height-to-weight ponderal ratios."}
    ]
  },
  "Dashboard \u2014 morph\\enantiomorph.md": {
    "primary": "Either of a pair of physical objects, crystals, or molecular structures that are non-superimposable mirror images of each other; a chiral counterpart.",
    "secondary": "In stereochemistry, enantiomorphs (enantiomers) share identical melting points and scalar physical properties, but rotate plane-polarized light in equal and opposite directions.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Researches on the Molecular Asymmetry of Natural Organic Products", "quote": "I separated the crystals of sodium ammonium tartrate by hand into two distinct piles, each crystal being the **enantiomorph** of the other."},
      {"author": "Jacobus Henricus van 't Hoff", "work": "The Arrangement of Atoms in Space", "quote": "When a central carbon atom is bonded to four different chemical radicals, two spatial configurations result, each an **enantiomorph** of its mate."},
      {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "The asymmetrical spatial binding of an **enantiomorph** to an enzyme receptor explains why optical isomers often have vastly different pharmacological effects."}
    ]
  },
  "Dashboard \u2014 morph\\enantiomorphic.md": {
    "primary": "Pertaining to, existing as, or characterized by non-superimposable mirror-image forms; chiral.",
    "secondary": "In crystallography and mineralogy, describing crystals whose hemihedral facets lack a plane of symmetry, causing them to rotate the plane of polarized light.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Studies on Molecular Dissymmetry", "quote": "The mechanical separation of **enantiomorphic** tartaric crystals demonstrated for the first time the molecular basis of optical activity."},
      {"author": "Lord Kelvin", "work": "Baltimore Lectures on Molecular Dynamics and the Wave Theory of Light", "quote": "I call any geometrical figure chiral, or **enantiomorphic**, if its image in a plane mirror cannot be brought into coincidence with itself."},
      {"author": "J. D. Bernal", "work": "The Structure of Crystals", "quote": "Quartz forms twin **enantiomorphic** crystal varieties, designated right-handed and left-handed according to their optical rotation."}
    ]
  },
  "Dashboard \u2014 morph\\enantiomorphism.md": {
    "primary": "The condition, quality, or phenomenon of existing as non-superimposable mirror-image structures; structural chirality.",
    "secondary": "In organic chemistry and pharmaceutical sciences, enantiomorphism dictates chiral drug interactions, where one enantiomer may be therapeutically active while its mirror form is inactive or toxic.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Researches on Molecular Dimorphism", "quote": "All living processes produce asymmetric compounds, proving that molecular **enantiomorphism** is fundamentally linked to biological synthesis."},
      {"author": "Jacobus Henricus van 't Hoff", "work": "Chemistry in Space", "quote": "The tetrahedral geometry of the carbon atom provides the foundational mechanical explanation for stereochemical **enantiomorphism**."},
      {"author": "Paul Groth", "work": "Physikalische Krystallographie", "quote": "Optical activity in crystals without center of symmetry is an immediate consequence of structural **enantiomorphism** in the lattice."}
    ]
  },
  "Dashboard \u2014 morph\\endomorph.md": {
    "primary": "An individual having a somatotype characterized by a round, soft body build with a predominance of adipose tissue and prominent digestive organs.",
    "secondary": "In constitutional psychology and somatotyping, William Sheldon linked the endomorph physical type to a viscerotonic, genial, and comfort-seeking temperament.",
    "quotes": [
      {"author": "William H. Sheldon", "work": "The Varieties of Human Physique", "quote": "The **endomorph** displays a physique dominated by digestive viscera, with soft spherical contours and high buoyant density."},
      {"author": "Gordon Allport", "work": "Pattern and Growth in Personality", "quote": "Sheldon's typology suggests that the typical **endomorph** seeks social warmth, affection, and conviviality."},
      {"author": "Hans Eysenck", "work": "Dimensions of Personality", "quote": "Factor analysis of constitutional data demonstrates that the **endomorph** profile clusters consistently around measures of somatic adiposity."}
    ]
  },
  "Dashboard \u2014 morph\\endomorphic.md": {
    "primary": "Pertaining to, having the physical characteristics of, or classified as an endomorph; possessing rounded contours and relatively high body fat.",
    "secondary": "In metamorphic petrology and geology, describing mineralogical changes produced within an igneous magma body through assimilation of surrounding host rocks.",
    "quotes": [
      {"author": "William H. Sheldon", "work": "The Varieties of Temperament", "quote": "Physical examinations revealed prominent **endomorphic** traits, accompanied by a relaxed posture and deep visceral respiration."},
      {"author": "Reginald Aldworth Daly", "work": "Igneous Rocks and Their Origin", "quote": "The border zone of the granitic batholith exhibits **endomorphic** modification where shale country rock was ingested and melted."},
      {"author": "Alfred Harker", "work": "The Natural History of Igneous Rocks", "quote": "We differentiate exomorphic effects in the invaded strata from internal **endomorphic** alterations within the igneous margin."}
    ]
  },
  "Dashboard \u2014 morph\\endomorphy.md": {
    "primary": "The somatotypic condition, property, or degree of being soft, rounded, and having a predominance of digestive viscera and subcutaneous adiposity.",
    "secondary": "In anthropometric somatotyping (Heath-Carter system), endomorphy is the first component rating, calculated from triceps, subscapular, and supraspinale skinfold thicknesses.",
    "quotes": [
      {"author": "William H. Sheldon", "work": "Atlas of Men", "quote": "A high rating in **endomorphy** reflects the structural dominance of the digestive organs derived from the embryonic endoderm."},
      {"author": "J. M. Tanner", "work": "Growth at Adolescence", "quote": "During puberty, females typically exhibit an increase in **endomorphy**, depositing subcutaneous fat across pelvic and femoral regions."},
      {"author": "Barbara Heath", "work": "Somatotyping: Development and Applications", "quote": "In our anthropometric formulation, **endomorphy** is derived objectively from calibrated skinfold caliper measurements."}
    ]
  },
  "Dashboard \u2014 morph\\epimorphic.md": {
    "primary": "Pertaining to, undergoing, or characterized by epimorphosis; describing biological regeneration that proceeds by cell proliferation and blastema formation.",
    "secondary": "In mathematical category theory, describing an epimorphism, which is a right-cancellative morphism generalizing surjective functions between algebraic structures.",
    "quotes": [
      {"author": "Thomas Hunt Morgan", "work": "Regeneration", "quote": "In **epimorphic** regeneration, the lost limb is restored by active proliferation of new embryonic cells at the cut surface."},
      {"author": "Saunders Mac Lane", "work": "Categories for the Working Mathematician", "quote": "A morphism f is said to be **epimorphic** if it can be cancelled on the right: whenever g after f equals h after f, g equals h."},
      {"author": "Lewis Wolpert", "work": "Principles of Development", "quote": "Urodele amphibians utilize an **epimorphic** regenerative process, forming a specialized blastema that dedifferentiates local tissues."}
    ]
  },
  "Dashboard \u2014 morph\\epimorphism.md": {
    "primary": "In category theory and abstract algebra, a morphism that is right-cancellative with respect to composition, generalizing the concept of a surjective (onto) mapping.",
    "secondary": "In developmental and regenerative biology, epimorphism (epimorphosis) denotes the regeneration of a severed animal appendage through the growth of an undifferentiated blastema.",
    "quotes": [
      {"author": "Saunders Mac Lane", "work": "Homology", "quote": "In any abelian category, every monic morphism is a kernel and every **epimorphism** is a cokernel of some arrow."},
      {"author": "Alexander Grothendieck", "work": "Éléments de géométrie algébrique", "quote": "The canonical projection from a ring onto its quotient by a radical ideal provides the archetype of an **epimorphism**."},
      {"author": "Thomas Hunt Morgan", "work": "Regeneration", "quote": "We distinguish morphallaxis, where the whole piece remodels, from **epimorphism**, where new tissue sprouts from the wound margin."}
    ]
  },
  "Dashboard \u2014 morph\\geomorphologic.md": {
    "primary": "Pertaining to, dealing with, or relating to the origin, physical evolution, and spatial arrangement of topographic landforms on the surface of the Earth.",
    "secondary": "In earth science, geomorphologic analyses evaluate how fluvial, glacial, aeolian, and tectonic forces sculpt regional terrain over geological timescales.",
    "quotes": [
      {"author": "William Morris Davis", "work": "Geographical Essays", "quote": "The **geomorphologic** cycle describes the progressive reduction of uplifted highlands through youth, maturity, and peneplain senescence."},
      {"author": "G. K. Gilbert", "work": "Report on the Geology of the Henry Mountains", "quote": "The balance between rock resistance and stream erosion governs every major **geomorphologic** boundary in the arid plateau."},
      {"author": "Arthur Holmes", "work": "Principles of Physical Geology", "quote": "Glacial retreat left striking **geomorphologic** monuments, including moraines, drumlins, and deeply incised U-shaped valleys."}
    ]
  },
  "Dashboard \u2014 morph\\geomorphological.md": {
    "primary": "Pertaining to geomorphology; concerned with the physical configuration and sculpting mechanisms of planetary surface landforms.",
    "secondary": "In geotechnical engineering and coastal management, geomorphological field surveys assess slope stability, sediment transport dynamics, and flood hazards.",
    "quotes": [
      {"author": "William Morris Davis", "work": "The Geographical Cycle", "quote": "A complete **geomorphological** description of any landscape requires an account of structure, process, and developmental stage."},
      {"author": "Ralph Alger Bagnold", "work": "The Physics of Blown Sand and Desert Dunes", "quote": "Field measurements reveal that crescentic barchan dunes migrate as coherent **geomorphological** units across rocky desert plains."},
      {"author": "Richard Chorley", "work": "Physical Geography: A Systems Approach", "quote": "Modern hydrology analyzes the drainage basin as an integrated open **geomorphological** system operating in dynamic equilibrium."}
    ]
  },
  "Dashboard \u2014 morph\\geomorphology.md": {
    "primary": "The scientific discipline that studies the origin, evolution, classification, and dynamic processes shaping the landforms and topography of the Earth and other planets.",
    "secondary": "In contemporary earth system science, geomorphology integrates quantitative fluid mechanics, radiometric dating, and digital elevation modeling to quantify erosion rates.",
    "quotes": [
      {"author": "William Morris Davis", "work": "Geographical Essays", "quote": "The science of **geomorphology** seeks not merely to catalog mountain peaks and river valleys, but to reconstruct their evolutionary history."},
      {"author": "G. K. Gilbert", "work": "The Transportation of Debris by Running Water", "quote": "Experimental flume studies laid the physical foundation for modern quantitative **geomorphology**, measuring bedload transport mechanics."},
      {"author": "Arthur Holmes", "work": "Principles of Physical Geology", "quote": "Tectonic uplift and denudation represent the opposing prime movers whose eternal interaction forms the subject matter of **geomorphology**."}
    ]
  },
  "Dashboard \u2014 morph\\hemimetamorphic.md": {
    "primary": "Characterized by, undergoing, or exhibiting incomplete or partial metamorphosis, wherein immature nymphs develop gradually into adults without a pupal stage.",
    "secondary": "In entomology and invertebrate zoology, hemimetamorphic insects (including dragonflies, grasshoppers, and true bugs) possess nymphal instars with external wing pads.",
    "quotes": [
      {"author": "John Lubbock", "work": "On the Origin and Metamorphoses of Insects", "quote": "In **hemimetamorphic** insects, the nymph emerges from the egg resembling a miniature adult, acquiring wings progressively through successive molts."},
      {"author": "Alpheus Spring Packard", "work": "A Text-Book of Entomology", "quote": "The evolutionary transition from ancient ametabolous hexapods proceeded through intermediate **hemimetamorphic** ancestral orders."},
      {"author": "Vincent Dethier", "work": "The Physiology of Insect Senses", "quote": "Sensory receptors on the antennae of **hemimetamorphic** nymphs mature in synchrony with somatic cuticle expansion."}
    ]
  },
  "Dashboard \u2014 morph\\hemimetamorphosis.md": {
    "primary": "Incomplete, partial, or gradual metamorphosis in insects, characterized by three developmental stages: egg, nymph, and adult, without an intervening pupal resting phase.",
    "secondary": "In evolutionary biology, hemimetamorphosis represents the ancestral winged insect developmental mode, contrasted with holometabolous complete metamorphosis.",
    "quotes": [
      {"author": "John Lubbock", "work": "On the Origin and Metamorphoses of Insects", "quote": "The simplicity of **hemimetamorphosis** suggests that complete pupal transformation was a later evolutionary innovation to exploit diverse seasonal niches."},
      {"author": "Reginald Punnett", "work": "Mendelism", "quote": "Breeding experiments on insects undergoing **hemimetamorphosis** trace how morphological variations persist smoothly across nymphal instars."},
      {"author": "Vincent Dethier", "work": "To Know a Fly", "quote": "Unlike flies that rebuild their anatomy inside a puparium, grasshoppers undergo **hemimetamorphosis**, keeping the same basic plan from hatch to maturity."}
    ]
  },
  "Dashboard \u2014 morph\\hemimetamorphous.md": {
    "primary": "Undergoing or characterized by hemimetamorphosis; displaying incomplete metamorphosis from nymph to adult.",
    "secondary": "In systematic entomology, describing insects whose immature forms share the general morphology, compound eyes, and often dietary habits of the reproductive adults.",
    "quotes": [
      {"author": "Thomas Say", "work": "American Entomology", "quote": "The cicadas and leafhoppers constitute a prominent **hemimetamorphous** group whose immature stages feed upon subterranean root sap."},
      {"author": "John Lawrence LeConte", "work": "The Rhynchophora of America North of Mexico", "quote": "While weevils undergo complete pupation, true bugs are **hemimetamorphous**, lacking a quiescent pupal stage."},
      {"author": "Alpheus Spring Packard", "work": "Guide to the Study of Insects", "quote": "In every **hemimetamorphous** species, the rudiments of wings appear externally on the meso- and metathorax during later nymphal stages."}
    ]
  },
  "Dashboard \u2014 morph\\hemimorphic.md": {
    "primary": "Having dissimilar ends or opposite extremities differently developed; in crystallography, describing a crystal whose opposite ends terminate in faces of different forms due to lacking a center of symmetry.",
    "secondary": "In solid-state physics and mineralogy, hemimorphic crystal classes exhibit polar axes that generate spontaneous piezoelectric and pyroelectric charges under thermal or mechanical stress.",
    "quotes": [
      {"author": "René Just Haüy", "work": "Traité de cristallographie", "quote": "A crystal is designated **hemimorphic** when its two opposite extremities are terminated by geometric facets belonging to different crystallographic forms."},
      {"author": "Paul Groth", "work": "Physikalische Krystallographie", "quote": "Because tourmaline crystals are **hemimorphic**, temperature changes induce electric polarity with opposite charges gathering at either pole."},
      {"author": "William Henry Bragg", "work": "X Rays and Crystal Structure", "quote": "X-ray diffraction demonstrates that the absence of an inversion center in a **hemimorphic** space group accounts for its polar electrical behavior."}
    ]
  },
  "Dashboard \u2014 morph\\hemimorphite.md": {
    "primary": "A hydrous zinc silicate mineral [Zn4Si2O7(OH)2·H2O], an important ore of zinc characterized by hemimorphic polar crystals possessing piezoelectric and pyroelectric properties.",
    "secondary": "In economic geology and mineralogy, hemimorphite (historically called calamine) commonly occurs as a secondary oxidation product in the weathered gossans of zinc-lead deposits.",
    "quotes": [
      {"author": "J. D. Dana", "work": "A System of Mineralogy", "quote": "The mineral **hemimorphite** was named in reference to the hemimorphic development of its prismatic crystals, terminating differently at opposite ends."},
      {"author": "René Just Haüy", "work": "Tableau comparatif des résultats de la cristallographie", "quote": "When heated, crystalline **hemimorphite** readily attracts light ash particles, exhibiting powerful pyroelectric charge separation."},
      {"author": "William L. Bragg", "work": "Atomic Structure of Minerals", "quote": "Crystal structure analysis shows that **hemimorphite** consists of tetrahedral zinc and silicon groups linked with water molecules along polar c-axes."}
    ]
  },
  "Dashboard \u2014 morph\\holomorph.md": {
    "primary": "In abstract group theory, the semidirect product of a group with its full automorphism group, representing the maximal permutation group in which the original group is normal.",
    "secondary": "In mycology and fungal taxonomy, the complete fungus in all its reproductive stages and morphological expressions, encompassing both the teleomorph (sexual) and any anamorphs (asexual).",
    "quotes": [
      {"author": "William Burnside", "work": "Theory of Groups of Finite Order", "quote": "The **holomorph** of a group G is the group formed by compounding the operations of G with all its possible automorphisms."},
      {"author": "Bryce Kendrick", "work": "The Whole Fungus", "quote": "Under international botanical rules, the term **holomorph** denotes the entire organism across all its pleomorphic vegetative and reproductive forms."},
      {"author": "John Webster", "work": "Introduction to Fungi", "quote": "Molecular sequencing techniques now permit mycologists to unify isolated conidial morphs under a single recognized **holomorph** name."}
    ]
  },
  "Dashboard \u2014 morph\\holomorphic.md": {
    "primary": "In complex analysis, describing a complex-valued function of one or more complex variables that is complex-differentiable at every point throughout an open domain.",
    "secondary": "In geometric function theory, every holomorphic function is infinitely differentiable, analytic (equal to its Taylor series), and defines a conformal mapping where its derivative is non-zero.",
    "quotes": [
      {"author": "Augustin-Louis Cauchy", "work": "Mémoire sur les intégrales définies", "quote": "If a function of a complex variable is **holomorphic** throughout a simply connected domain, its contour integral around any closed loop vanishes."},
      {"author": "Bernhard Riemann", "work": "Grundlagen für eine allgemeine Theorie der Functionen einer veränderlichen complexen Grösse", "quote": "A complex function is **holomorphic** if and only if its real and imaginary parts satisfy the Cauchy-Riemann partial differential equations."},
      {"author": "Lars Ahlfors", "work": "Complex Analysis", "quote": "The remarkable rigidity of a **holomorphic** function implies that its values in an open set are completely determined by its behavior in an arbitrarily small neighborhood."}
    ]
  },
  "Dashboard \u2014 morph\\holomorphism.md": {
    "primary": "The mathematical condition, property, or quality of being holomorphic; complex differentiability and analyticity throughout a domain.",
    "secondary": "In complex differential geometry and several complex variables, holomorphism preserves complex structure across Kähler manifolds and complex vector bundles.",
    "quotes": [
      {"author": "Lars Ahlfors", "work": "Conformal Invariants", "quote": "The preservation of infinitesimal angles under conformal mapping is an immediate geometric manifestation of **holomorphism**."},
      {"author": "Kunihiko Kodaira", "work": "Complex Manifolds and Deformation of Complex Structures", "quote": "Deformation theory examines how families of complex structures vary smoothly while preserving internal **holomorphism**."},
      {"author": "Saunders Mac Lane", "work": "Mathematics: Form and Function", "quote": "The step from real differentiability to **holomorphism** represents one of the most fruitful conceptual syntheses in mathematical analysis."}
    ]
  }
}

base_dir = r"App database\Greek roots\Cluster Form & Space"
mjs_path = r"main app\scripts\curate_form_finish_b2.mjs"

content = f"""import {{ updateNotesBatch }} from './curate-updater-util.mjs';

const baseDir = {json.dumps(base_dir)};
const batchData = {json.dumps(data, indent=2, ensure_ascii=False)};

const count = updateNotesBatch(baseDir, batchData);
console.log(`Updated ${{count}} notes in Finish Slice 1 Batch 2.`);
"""

with open(mjs_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Generated {mjs_path} with {len(data)} words.")
res = subprocess.run(["node", mjs_path], capture_output=True, text=True)
print("Node output:", res.stdout)
if res.stderr:
    print("Node error:", res.stderr)
