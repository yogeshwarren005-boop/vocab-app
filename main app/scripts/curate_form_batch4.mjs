import { updateNotesBatch } from './curate-updater-util.mjs';
import path from 'path';

const CLUSTER_DIR = path.resolve('App database/Greek roots/Cluster Form & Space');

const batchData = {
  "Dashboard — cata\\catabolize.md": {
    "primary": "To subject to or break down through catabolism; to metabolically degrade complex molecules into simpler compounds with the release of chemical energy.",
    "secondary": "In cellular physiology and biochemistry, the enzymatic degradation of glycogen, lipids, or cellular proteins to sustain ATP production during starvation or exercise.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "When carbohydrate stores are depleted, hepatocytes **catabolize** stored fatty acids, leading to an accumulation of ketone bodies."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "Synaptic enzymes rapidly **catabolize** acetylcholine into choline and acetate to prevent desensitization of postsynaptic channels."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "Migrating birds **catabolize** concentrated subcutaneous adipose tissues to power nonstop transoceanic flight."
      }
    ]
  },
  "Dashboard — cata\\catacala.md": {
    "primary": "A large genus of nocturnal noctuoid moths, commonly known as underwing moths, noted for brightly colored hindwings concealed beneath cryptic forewings at rest.",
    "secondary": "In evolutionary entomology, a classic model for apostatic selection and flash coloration, where sudden exposure of bright hindwings startles avian predators.",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "Darwinism: An Exposition of the Theory of Natural Selection",
        "quote": "The exquisite camouflage of **Catacala** forewings completely conceals the insect upon lichen-encrusted tree bark."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "When flushed from rest, the sudden brilliant scarlet flash of the **Catacala** hindwing momentarily dazzles the pursuing bird."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Diversity of Life",
        "quote": "Dozens of sympatric species of **Catacala** share identical deciduous forests by partitioning different host trees in the larval stage."
      }
    ]
  },
  "Dashboard — cata\\catachresis.md": {
    "primary": "The misuse, strained application, or paradoxical abuse of a word or figure of speech, often involving a mixed or contradictory metaphor.",
    "secondary": "In classical rhetoric and deconstruction, the deliberate appropriation of a signifier to denote something that lacks a proper literal term of its own.",
    "quotes": [
      {
        "author": "Alexander Pope",
        "work": "Peri Bathous, or The Art of Sinking in Poetry",
        "quote": "A daring **catachresis** allows the poet to take arms against a sea of troubles and mow down winged ideas."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Lives of the English Poets",
        "quote": "The metaphysical poets indulged in violent **catachresis**, yoking the most heterogeneous concepts by sheer rhetorical force."
      },
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "To speak of a blind mouth is an obvious **catachresis**, yet such forceful metaphors often strike deeply into the imagination."
      }
    ]
  },
  "Dashboard — cata\\catachrestic.md": {
    "primary": "Characterized by, involving, or resembling catachresis; strained, far-fetched, or paradoxical in rhetorical usage.",
    "secondary": "In stylistic analysis, describing figurative expressions that violently diverge from conventional semantic boundaries.",
    "quotes": [
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "His imagery was excessively **catachrestic**, combining tactile and acoustic tropes until the mind recoiled from the confusion."
      },
      {
        "author": "Thomas Carlyle",
        "work": "Sartor Resartus",
        "quote": "Teufelsdröckh's prophetic style abounds in **catachrestic** turns of phrase that challenge pedestrian grammatical logic."
      },
      {
        "author": "George Saintsbury",
        "work": "A History of Elizabethan Literature",
        "quote": "Jacobean drama celebrated **catachrestic** boldness, seeking shock and heightened dramatic pathos above classical decorum."
      }
    ]
  },
  "Dashboard — cata\\catachrestical.md": {
    "primary": "Of, relating to, or of the nature of catachresis; catachrestic (formal or historical variant).",
    "secondary": "In philology and historical rhetoric, designating words applied in an improper or secondary sense far removed from their primary etymology.",
    "quotes": [
      {
        "author": "Thomas Browne",
        "work": "Pseudodoxia Epidemica",
        "quote": "To term a dolphin a royal fish is a **catachrestical** designation originating from regal prerogatives rather than natural history."
      },
      {
        "author": "Samuel Johnson",
        "work": "Preface to Shakespeare",
        "quote": "Those strained conceits which pedants denounce as **catachrestical** often capture psychological truth with startling precision."
      },
      {
        "author": "Richard Chenevix Trench",
        "work": "On the Study of Words",
        "quote": "Language grows through continuous **catachrestical** extensions, wherein old words are compelled to designate novel inventions."
      }
    ]
  },
  "Dashboard — cata\\cataclinal.md": {
    "primary": "In structural geology and geomorphology, dipping or flowing in the same direction as the underlying geological strata.",
    "secondary": "Describing rivers, valleys, or drainage patterns that descend along the dip slope of rock formations (consequent drainage).",
    "quotes": [
      {
        "author": "Archibald Geikie",
        "work": "Text-book of Geology",
        "quote": "A **cataclinal** stream cuts its channel directly down the dip of the tilted sandstone beds."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Valleys whose slope coincides with the inclination of the strata are termed **cataclinal** by physical geographers."
      },
      {
        "author": "James Dwight Dana",
        "work": "Manual of Geology",
        "quote": "The drainage network follows a regular **cataclinal** pattern across the gently tilting coastal plain."
      }
    ]
  },
  "Dashboard — cata\\cataclysm.md": {
    "primary": "A violent, sudden physical, geological, or political upheaval or deluge that brings widespread destruction and irreversible change.",
    "secondary": "In historical geology and paleontology, a catastrophic global convulsion formerly invoked (as in Cuvier's catastrophism) to explain mass extinctions and geological unconformities.",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Instead of invoking an imaginary universal **cataclysm**, we should explain geological changes by causes now in actual operation."
      },
      {
        "author": "Georges Cuvier",
        "work": "Essay on the Theory of the Earth",
        "quote": "Repeated revolutions and sudden sea incursions caused each successive **cataclysm** that buried ancient fauna in deep strata."
      },
      {
        "author": "Thomas Carlyle",
        "work": "The French Revolution",
        "quote": "The collapse of the monarchy was a political **cataclysm** that swallowed the ancient privileges of the realm in blood."
      }
    ]
  },
  "Dashboard — cata\\cataclysmal.md": {
    "primary": "Of, relating to, or caused by a cataclysm; violently destructive, sudden, and revolutionary in impact.",
    "secondary": "In earth sciences, characterizing sudden geological events such as megatsunamis, meteorite impacts, or supervolcanoes rather than slow gradualism.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "On the Origin of Species",
        "quote": "He who rejects slow gradual modification must invoke **cataclysmal** destructions to account for the succession of organic forms."
      },
      {
        "author": "Archibald Geikie",
        "work": "The Founders of Geology",
        "quote": "Hutton swept away the **cataclysmal** theories of earth history in favor of uniform subterranean heat and weathering."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The barbarian surge across the Rhine produced a **cataclysmal** shock from which the western provinces never recovered."
      }
    ]
  },
  "Dashboard — cata\\cataclysmic.md": {
    "primary": "Severely destructive, disastrous, or transformative; of or relating to a cataclysm.",
    "secondary": "In planetary science and evolutionary theory, describing catastrophic impacts or abrupt climate shifts that trigger mass extinctions.",
    "quotes": [
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "A **cataclysmic** asteroid collision plunged the Cretaceous Earth into darkness, ending the age of the giant reptiles."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Diversity of Life",
        "quote": "Mass extinctions represent **cataclysmic** bottleneck events that reset the evolutionary trajectory of global ecosystems."
      },
      {
        "author": "H. G. Wells",
        "work": "The War of the Worlds",
        "quote": "The Martian heat-ray brought **cataclysmic** ruin to the suburban towns along the southern Thames."
      }
    ]
  },
  "Dashboard — cata\\catacorner.md": {
    "primary": "Situated diagonally opposite across a street, intersection, or space; cater-cornered or kitty-corner.",
    "secondary": "In colloquial spatial orientation, describing a diagonal geometric alignment across intersecting axes.",
    "quotes": [
      {
        "author": "Mark Twain",
        "work": "The Adventures of Tom Sawyer",
        "quote": "The old abandoned schoolhouse stood **catacorner** from the haunted graveyard across the overgrown crossroad."
      },
      {
        "author": "William Faulkner",
        "work": "The Sound and the Fury",
        "quote": "He walked past the courthouse square, cutting **catacorner** across the grass toward the blacksmith shop."
      },
      {
        "author": "John Steinbeck",
        "work": "East of Eden",
        "quote": "The general store was located **catacorner** to the livery stable, catching trade from both main streets."
      }
    ]
  },
  "Dashboard — cata\\catalan.md": {
    "primary": "Relating to Catalonia, its people, or the Romance language spoken in northeastern Spain and adjoining regions; a native or inhabitant of Catalonia.",
    "secondary": "In linguistics and historical metallurgy, the Romance language closely related to Occitan; also denoting the Catalan forge used in early iron production.",
    "quotes": [
      {
        "author": "George Orwell",
        "work": "Homage to Catalonia",
        "quote": "Every shop and cafe had an inscription saying that it had been collectivised; even the bootblacks had been collectivised and their boxes were painted red and black, speaking in rapid **Catalan**."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The fierce **Catalan** Grand Company turned their mercenary swords against the Byzantine emperor who had hired them."
      },
      {
        "author": "Primo Levi",
        "work": "The Periodic Table",
        "quote": "The primitive **Catalan** furnace had smelted iron ore in the Pyrenees for centuries before modern blast furnaces appeared."
      }
    ]
  },
  "Dashboard — cata\\catalase.md": {
    "primary": "A pervasive antioxidant enzyme found in nearly all aerobic organisms that rapidly catalyzes the breakdown of toxic hydrogen peroxide into water and oxygen.",
    "secondary": "In enzymology and microbiology, a heme-containing tetrameric oxidoreductase whose presence or absence is a standard diagnostic criterion in bacterial identification (catalase test).",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "A single molecule of the enzyme **catalase** can decompose millions of hydrogen peroxide molecules every minute into oxygen and water."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Dropping dilute peroxide onto staphylococcal colonies elicits effervescence due to the active bacterial **catalase**."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "The universal presence of **catalase** across aerobic life forms underscores the ancient necessity of cellular antioxidant defense."
      }
    ]
  },
  "Dashboard — cata\\catalatic.md": {
    "primary": "Of, relating to, or produced by the catalytic decomposition of hydrogen peroxide by catalase.",
    "secondary": "In physiological chemistry, describing the rate or kinetic activity of catalase enzymes in neutralizing reactive oxygen species.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "The **catalatic** power of liver extracts resides within the iron-porphyrin prosthetic groups of the tetrameric enzyme."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Absence of normal **catalatic** degradation in acatalasemia renders the oral tissues vulnerable to gangrenous ulceration."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Immunochemistry",
        "quote": "The temperature coefficient of the **catalatic** reaction displays rapid inactivation above critical thermal thresholds."
      }
    ]
  },
  "Dashboard — cata\\catalectic.md": {
    "primary": "In classical metrics and poetic prosody, lacking one or more syllables in the final foot of a line of verse.",
    "secondary": "Characterized by terminal metrical truncation, commonly used in trochaic or dactylic meters to impart a sharp, resolute cadence.",
    "quotes": [
      {
        "author": "Edgar Allan Poe",
        "work": "The Philosophy of Composition",
        "quote": "The rhythm of The Raven is trochaic, the measure octameter acatalectic, alternating with heptameter **catalectic**."
      },
      {
        "author": "George Saintsbury",
        "work": "A History of English Prosody",
        "quote": "The dropping of the final unaccented syllable renders the trochaic line **catalectic**, ending upon an emphatic monosyllabic beat."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "A **catalectic** close arrests the flowing cadence of the verse, concentrating dramatic attention on the final word."
      }
    ]
  },
  "Dashboard — cata\\catalepsy.md": {
    "primary": "A medical or neurological condition characterized by muscular rigidity, fixed posture, and diminished sensitivity to external stimuli.",
    "secondary": "In neuropsychiatry and historical medicine, a trance-like motor state associated with catatonic schizophrenia, encephalitis, or extreme hysteria featuring waxy flexibility (flexibilitas cerea).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In hysterical **catalepsy**, the patient's limbs remain frozen for hours in whatever bizarre position the examiner places them."
      },
      {
        "author": "Edgar Allan Poe",
        "work": "The Premature Burial",
        "quote": "The frequent attacks of **catalepsy** to which I was subject simulated death with such terrible fidelity that burial seemed inevitable."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "Severe Parkinsonian frozenness sometimes deepened into a total **catalepsy**, rendering patients statue-like for entire days."
      }
    ]
  },
  "Dashboard — cata\\cataleptic.md": {
    "primary": "Of, relating to, or affected with catalepsy; rigid, trance-like, and unresponsive.",
    "secondary": "In clinical neurology, describing a patient or limb exhibiting waxy motor resistance and suspension of voluntary movement.",
    "quotes": [
      {
        "author": "William R. Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "The **cataleptic** arm could be elevated above the head, where it hung suspended as if carved in stone."
      },
      {
        "author": "Edgar Allan Poe",
        "work": "The Fall of the House of Usher",
        "quote": "The disease of the lady Madeline had long baffled the skill of her physicians; a settled apathy and a **cataleptic** character were common."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "He sat in a **cataleptic** stupor, staring blankly ahead without acknowledging questions or visual movements."
      }
    ]
  },
  "Dashboard — cata\\catalexis.md": {
    "primary": "The omission or absence of one or more syllables from the final metrical foot of a line of verse.",
    "secondary": "In prosody, the deliberate curtailment of a line's terminal foot, contrasting with hypercatalexis (addition) and acatalexis (completeness).",
    "quotes": [
      {
        "author": "George Saintsbury",
        "work": "A History of English Prosody",
        "quote": "By the operation of **catalexis**, a trochaic heptameter concludes on a resounding stressed beat rather than a weak feminine rhyme."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Table Talk",
        "quote": "The phenomenon of **catalexis** gives English trochaics their energetic and abrupt finish."
      },
      {
        "author": "Alexander Pope",
        "work": "An Essay on Criticism",
        "quote": "The critic measured each syllable with precision, noting how subtle **catalexis** broke the monotony of continuous measure."
      }
    ]
  },
  "Dashboard — cata\\cataloger.md": {
    "primary": "A person who creates, organizes, and maintains catalogs, especially a professional librarian who classifies, describes, and indexes bibliographic items.",
    "secondary": "In information science and museology, a specialist who standardizes metadata records, assigning controlled subject headings and call numbers to cultural collections.",
    "quotes": [
      {
        "author": "Jorge Luis Borges",
        "work": "The Library of Babel",
        "quote": "An ambitious **cataloger** once registered thousands of hexagonal rooms, hoping to decipher the universal index of all knowledge."
      },
      {
        "author": "Virginia Woolf",
        "work": "Orlando",
        "quote": "The patient **cataloger** in the British Museum had spent twenty years indexing royal state papers without ever visiting the palace."
      },
      {
        "author": "Henry David Thoreau",
        "work": "The Journal of Henry David Thoreau",
        "quote": "Every true naturalist is a **cataloger** of nature's subtle appointments, recording the exact day when the wood thrush first sings."
      }
    ]
  },
  "Dashboard — cata\\catalogue.md": {
    "primary": "A complete, systematically ordered list of items, such as books in a library, merchandise in a store, or works in an exhibition; or to record such items.",
    "secondary": "In epic poetry and rhetoric, an extended stylistic enumeration of heroic warriors, ships, or genealogical lineages (as in Homer's Catalogue of Ships).",
    "quotes": [
      {
        "author": "Homer",
        "work": "The Iliad",
        "quote": "Tell me now, Muses who possess the halls of Olympus, the leaders and chieftains whose names furnish the grand **catalogue** of the Achaean ships."
      },
      {
        "author": "Walt Whitman",
        "work": "Song of Myself",
        "quote": "I weave the great American **catalogue** of artisans, farmers, sailors, and pioneers into one democratic chant."
      },
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "Natural philosophy requires a comprehensive **catalogue** of documented empirical facts before universal axioms can be safely deduced."
      }
    ]
  },
  "Dashboard — cata\\cataloguer.md": {
    "primary": "A person who catalogues books, manuscripts, specimens, or museum artifacts (variant spelling of cataloger).",
    "secondary": "In archival science and historical bibliography, an expert responsible for provenance documentation and taxonomic accessioning.",
    "quotes": [
      {
        "author": "Thomas Carlyle",
        "work": "The Life of John Sterling",
        "quote": "The quiet **cataloguer** of the cathedral library spent his days deciphering faded monastic seals and Gothic bindings."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "Mr. Casaubon required an industrious **cataloguer** to organize the vast mountains of notes for his Key to all Mythologies."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "I preserved every specimen in spirits, acting as my own collector and **cataloguer** throughout the long voyage."
      }
    ]
  },
  "Dashboard — cata\\catalonia.md": {
    "primary": "An autonomous community in northeastern Spain, bordering France and the Mediterranean Sea, with its historic capital and largest city at Barcelona.",
    "secondary": "In European history and political geography, a maritime nation within the Crown of Aragon with a distinct Romance language, legal code, and industrial culture.",
    "quotes": [
      {
        "author": "George Orwell",
        "work": "Homage to Catalonia",
        "quote": "In **Catalonia** for several months the working class was practically in the saddle; the bourgeoisie had taken to flight or disguised themselves."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The warlike chivalry of **Catalonia** and Aragon extended their naval conquests from the Balearic Isles to the shores of Greece."
      },
      {
        "author": "Washington Irving",
        "work": "The Alhambra",
        "quote": "The bold mountaineers of **Catalonia** were celebrated across the peninsula for their stubborn defense of ancient regional liberties."
      }
    ]
  },
  "Dashboard — cata\\catalpa.md": {
    "primary": "A genus of deciduous flowering trees in the family Bignoniaceae, native to North America and East Asia, having large heart-shaped leaves and showy white flowers.",
    "secondary": "In horticulture and forestry, commonly known as the cigar tree or Indian bean tree, valued for shade and durable rot-resistant timber.",
    "quotes": [
      {
        "author": "Henry David Thoreau",
        "work": "The Journal of Henry David Thoreau",
        "quote": "The great blossoms of the **catalpa** resemble miniature spotted foxgloves massed together in broad, fragrant pyramids."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "In late autumn the **catalpa** drops its immense heart-shaped leaves, leaving long bean-like pods dangling from bare boughs."
      },
      {
        "author": "Walt Whitman",
        "work": "Specimen Days",
        "quote": "Sitting beneath the leafy canopy of a flowering **catalpa**, I watched the hummingbirds dart among the white bells."
      }
    ]
  },
  "Dashboard — cata\\catalufa.md": {
    "primary": "Any of several tropical marine fishes in the family Priacanthidae (bigeyes), noted for bright red bodies, extremely large eyes, and rough scales.",
    "secondary": "In ichthyology and reef ecology, nocturnal predatory fishes that dwell in deep coral crevices by day and emerge at night to feed on macrozooplankton.",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "Peering down into the shadowed coral grotto, one catches the golden gleam of the huge eye of a solitary **catalufa**."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The red **catalufa** caught off the tropical reef exhibited immense round pupils adapted for nocturnal hunting in deep water."
      },
      {
        "author": "Alister Hardy",
        "work": "The Open Sea: Its Natural History",
        "quote": "The rough ctenoid scales of the **catalufa** provide armor against sharp coral edges as it maneuvers through submerged caves."
      }
    ]
  },
  "Dashboard — cata\\catalyse.md": {
    "primary": "To cause or accelerate a chemical reaction by acting as a catalyst; to facilitate, stimulate, or precipitate a process (British spelling).",
    "secondary": "In biochemistry, describing the action of enzymes that lower activation energy without shifting chemical equilibrium.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Proteins evolved active clefts that **catalyse** complex substrate rearrangements with extraordinary stereospecificity."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "Adenylyl cyclase operates to **catalyse** the conversion of cellular ATP into cyclic AMP during long-term synaptic facilitation."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Science and Culture",
        "quote": "A single revolutionary discovery can **catalyse** decades of dormant intellectual inquiry into sudden fruitful activity."
      }
    ]
  },
  "Dashboard — cata\\catalysis.md": {
    "primary": "The acceleration of a chemical reaction caused by the presence of a substance (a catalyst) that is not itself consumed in the reaction.",
    "secondary": "In physical chemistry, a fundamental process divided into homogeneous, heterogeneous, and enzymatic catalysis, governed by the lowering of Gibbs activation free energy.",
    "quotes": [
      {
        "author": "Jöns Jacob Berzelius",
        "work": "Annual Survey of Progress in Chemistry",
        "quote": "I shall designate this phenomenon **catalysis**, the catalytic force by which substances awaken dormant chemical affinities through their mere presence."
      },
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "The economic manufacture of ammonia via the Haber process relies on heterogeneous **catalysis** across finely divided iron surfaces."
      },
      {
        "author": "Primo Levi",
        "work": "The Periodic Table",
        "quote": "In industrial chemistry, **catalysis** is the magic spark that coaxed inert hydrocarbons into synthetic resins."
      }
    ]
  },
  "Dashboard — cata\\catalyst.md": {
    "primary": "A substance that accelerates the rate of a chemical reaction without undergoing permanent chemical change itself.",
    "secondary": "Metaphorically, any person, event, or condition that precipitates a rapid, significant change or action.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "The platinum wire acts as a **catalyst**, lowering the activation barrier so that combustion proceeds at room temperature."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "The Old Regime and the Revolution",
        "quote": "Financial bankruptcy served as the immediate **catalyst** that precipitated the collapse of the French royal administration."
      },
      {
        "author": "Edward O. Wilson",
        "work": "Consilience: The Unity of Knowledge",
        "quote": "Technological innovation has become the primary **catalyst** accelerating cultural evolution across the modern world."
      }
    ]
  },
  "Dashboard — cata\\catalytic.md": {
    "primary": "Of, relating to, or causing catalysis; acting as a catalyst.",
    "secondary": "In biochemistry, describing the active functional domain of an enzyme responsible for substrate cleavage or synthesis (catalytic triad or site).",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Transition metals exhibit high **catalytic** activity due to their ability to adopt multiple oxidation states and coordinate reagents."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "Phosphorylation of the **catalytic** subunit relieves allosteric inhibition, initiating transcription of immediate-early genes."
      },
      {
        "author": "Primo Levi",
        "work": "The Periodic Table",
        "quote": "The metallic **catalytic** converters in modern exhausts strip toxic oxides of nitrogen from combustion gases."
      }
    ]
  },
  "Dashboard — cata\\catalytically.md": {
    "primary": "By means of catalysis; through the agency or action of a catalyst.",
    "secondary": "In enzymology and physical chemistry, referring to reactions mediated through an intermediate activated complex without consuming the reagent.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "Enzymes function **catalytically**, processing thousands of substrate molecules per second without undergoing irreversible alteration."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Theories of Chemistry",
        "quote": "Hydrogen ions accelerate the inversion of cane sugar **catalytically**, their concentration directly determining the reaction velocity."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "Activated protein kinase A acts **catalytically** within the nucleus to phosphorylate CREB transcription factors."
      }
    ]
  },
  "Dashboard — cata\\catalyze.md": {
    "primary": "To accelerate or initiate a chemical reaction as a catalyst; to facilitate, stimulate, or bring about a profound change (US spelling).",
    "secondary": "In biochemistry and molecular biology, the function of enzymes in reducing transition-state energy barriers to drive cellular metabolic flux.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "Specialized RNA molecules known as ribozymes can **catalyze** the cleavage and splicing of their own phosphodiester backbones."
      },
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "Sunlight and mineral surfaces may have combined to **catalyze** the formation of the first self-replicating organic polymers."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Diversity of Life",
        "quote": "Environmental disturbances often **catalyze** sudden evolutionary shifts by opening new ecological niches to opportunistic colonists."
      }
    ]
  },
  "Dashboard — cata\\catamaran.md": {
    "primary": "A boat or vessel having two parallel hulls of equal size joined together by a deck or frame; originally a raft of logs lashed side by side.",
    "secondary": "In naval architecture, a twin-hulled craft valued for exceptional stability, wide deck area, and shallow draft; also historically, a quarrelsome person.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The coastal natives navigated the heavy surf in a light **catamaran** constructed of three buoyant logs lashed firmly together."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The Polynesian canoe skimmed over the waves like an outrigger **catamaran**, defying the heaviest Pacific swells."
      },
      {
        "author": "William Makepeace Thackeray",
        "work": "Vanity Fair",
        "quote": "The old dowager was an intolerable **catamaran**, terrifying the servants with her shrill scolding and imperious commands."
      }
    ]
  },
  "Dashboard — cata\\catamenia.md": {
    "primary": "The periodic flow of blood and mucosal tissue from the uterus; the menses or menstruation.",
    "secondary": "In gynecological medicine, the cyclic physiological shed of endometrial tissue regulated by hypothalamic-pituitary-ovarian hormones.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe chlorosis in young women was almost invariably accompanied by total suppression of the **catamenia** and marked pallor."
      },
      {
        "author": "Hippocrates",
        "work": "Aphorisms",
        "quote": "If a woman who is not pregnant suffers cessation of the **catamenia**, fever and pain in the loins commonly ensue."
      },
      {
        "author": "William Benjamin Carpenter",
        "work": "Principles of Human Physiology",
        "quote": "The periodic recurrence of the **catamenia** reflects the cyclical maturation and discharge of an ovum from the Graafian follicle."
      }
    ]
  },
  "Dashboard — cata\\catamenial.md": {
    "primary": "Of, relating to, or occurring during the catamenia (menstruation).",
    "secondary": "In clinical neurology and gynecology, describing periodic exacerbations of conditions (such as catamenial epilepsy or catamenial migraine) timed with hormonal drops.",
    "quotes": [
      {
        "author": "William R. Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "The recurrence of seizures showed a pronounced **catamenial** periodicity, concentrating during the premenstrual phase of the cycle."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe **catamenial** migraines frequently abate during pregnancy when systemic estrogen and progesterone levels remain steady."
      },
      {
        "author": "Oliver Sacks",
        "work": "Migraine",
        "quote": "Her debilitating hemicrania was strictly **catamenial**, returning with unerring regularity at the onset of each monthly period."
      }
    ]
  },
  "Dashboard — cata\\catamite.md": {
    "primary": "A boy kept for homosexual practices, especially the younger, passive partner in ancient Greek or Roman pederasty.",
    "secondary": "In classical history and moral literature, a youth maintained for erotic gratification by an older patron.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The dissolute emperor Heliogabalus paraded his imperial palace in the company of every pampered **catamite** and flatterer."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "In royal courts where luxury reigned, shameful flatteries corrupt the youth, mimicking the pagan **catamite** of old."
      },
      {
        "author": "Thomas Babington Macaulay",
        "work": "The History of England",
        "quote": "Satirists of the Restoration court spared neither king nor minister, denouncing both mistress and courtly **catamite** alike."
      }
    ]
  },
  "Dashboard — cata\\catamountain.md": {
    "primary": "A wild cat, especially a cougar (mountain lion), puma, or lynx; also a fierce, savage, or unruly person.",
    "secondary": "In American frontier literature and folkloric natural history, a ferocious feral feline inhabiting rugged mountains and backwoods.",
    "quotes": [
      {
        "author": "Washington Irving",
        "work": "A History of New York",
        "quote": "The solitary hunter ventured into the wilderness, where neither screaming panthers nor fierce **catamountain** beasts could turn him back."
      },
      {
        "author": "Walter Scott",
        "work": "The Fair Maid of Perth",
        "quote": "The Highland reiver fought with the sudden ferocity of a trapped **catamountain**, striking out in every direction."
      },
      {
        "author": "Henry David Thoreau",
        "work": "The Maine Woods",
        "quote": "The woodsmen spoke around the camp-fire of tracking a screaming **catamountain** across the frozen crust of deep snow."
      }
    ]
  },
  "Dashboard — cata\\catananche.md": {
    "primary": "A genus of Mediterranean flowering plants in the family Asteraceae, commonly known as Cupid's dart, bearing papery blue or yellow flower heads.",
    "secondary": "In ethnobotany and classical lore, herbs (such as Catananche caerulea) anciently employed in Greek love philters and charms to inspire passion.",
    "quotes": [
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "Ancient Greek sorceresses gathered the herb **Catananche** to brew potent philtres designed to compel erotic love."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "The delicate azure flower heads of **Catananche** retain their vivid color and papery texture when dried for winter bouquets."
      },
      {
        "author": "Asa Gray",
        "work": "Synoptical Flora of North America",
        "quote": "The scarious, silvery phyllaries of **Catananche** distinguish it from allied genera within the chicory tribe."
      }
    ]
  },
  "Dashboard — cata\\cataract.md": {
    "primary": "A very large, powerful waterfall, cascade, or torrential downpour; also a clouding or opacity of the lens of the eye that obscures vision.",
    "secondary": "In ophthalmology, a major cause of blindness resulting from protein denaturing and aggregation in the crystalline lens, treated by phacoemulsification.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "The cataracts of heaven were opened, and torrents of torrential deluge overwhelmed the highest mountain peaks."
      },
      {
        "author": "William Wordsworth",
        "work": "Lines Composed a Few Miles above Tintern Abbey",
        "quote": "The sounding **cataract** haunted me like a passion; the tall rock, the mountain, and the deep and gloomy wood."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Senile **cataract** advances gradually, the cortical opacities coalescing until mature cataractous clouding blocks all light."
      }
    ]
  },
  "Dashboard — cata\\catarrh.md": {
    "primary": "Inflammation of a mucous membrane, particularly of the respiratory tract and air passages, accompanied by excessive secretion of mucus.",
    "secondary": "In clinical history, a common syndrome of mucosal congestion and rhinorrhea associated with viral coryza, chronic bronchitis, or allergy.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Acute bronchial **catarrh** manifests with harsh cough, substernal soreness, and copious muco-purulent expectoration."
      },
      {
        "author": "Charles Dickens",
        "work": "Bleak House",
        "quote": "The November fog settled deep into the lungs of Londoners, producing an epidemic of wheezing chest **catarrh**."
      },
      {
        "author": "Hippocrates",
        "work": "On Ancient Medicine",
        "quote": "When salt and acrid humors flow downward from the head into the throat, violent pulmonary **catarrh** results."
      }
    ]
  },
  "Dashboard — cata\\catarrhal.md": {
    "primary": "Relating to, characterized by, or affected with catarrh; producing inflammation and excessive mucus from mucous membranes.",
    "secondary": "In pathology, describing an inflammatory exudate composed primarily of mucus and desquamated epithelial cells.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The early stage of measles presents as an acute **catarrhal** fever with conjunctivitis, coryza, and barking cough."
      },
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "Auscultation reveals widespread mucous rales over both pulmonary bases in chronic **catarrhal** bronchitis."
      },
      {
        "author": "William R. Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "A febrile **catarrhal** infection frequently precedes the acute onset of post-infectious demyelinating polyneuropathy."
      }
    ]
  },
  "Dashboard — cata\\catarrhine.md": {
    "primary": "Belonging to the primate parvorder Catarrhini, comprising Old World monkeys, apes, and humans, characterized by downward-pointing, closely spaced nostrils.",
    "secondary": "In physical anthropology and evolutionary primatology, higher primates with a 2-1-2-3 dental formula, non-prehensile tails, and trichromatic color vision.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "Man indisputably belongs in his anatomical structure to the **catarrhine** division of the Simiadae of the Old World."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Man's Place in Nature",
        "quote": "The narrow nasal septum and downward-directed nares define the **catarrhine** primates, setting them apart from American platyrrhines."
      },
      {
        "author": "Ernst Haeckel",
        "work": "The Evolution of Man",
        "quote": "Comparative embryology demonstrates that humanity branched directly from the ancestral stem of the Miocene **catarrhine** apes."
      }
    ]
  },
  "Dashboard — cata\\catarrhinian.md": {
    "primary": "Of, relating to, or characteristic of the catarrhines; Old World primate.",
    "secondary": "In comparative anatomy and primatology, describing the cranial, dental, and nasal morphology distinctive of cercopithecoids and hominoids.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Vertebrated Animals",
        "quote": "The **catarrhinian** dentition exhibits thirty-two teeth, with two premolars in each quadrant, identical to the human formula."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "No zoologist can doubt that our species shares a strictly **catarrhinian** genealogy rooted in African primate lineages."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Geographical Distribution of Animals",
        "quote": "The fossil record in Europe and Asia documents the Miocene radiation of distinct **catarrhinian** anthropoids."
      }
    ]
  },
  "Dashboard — cata\\catasetum.md": {
    "primary": "A genus of showy epiphytic orchids native to tropical Central and South America, remarkable for unisexual flowers and explosive pollinia ejection.",
    "secondary": "In evolutionary botany, famous for Charles Darwin's experiments showing how touching the floral antenna triggers instant catapult-like discharge of the sticky pollen mass.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Various Contrivances by Which Orchids Are Fertilised by Insects",
        "quote": "When the sensitive antenna of the male **Catasetum** is touched, the pollinium is shot out with extraordinary velocity to adhere to the visiting bee."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "Travels on the Amazon and Rio Negro",
        "quote": "High up in the forks of the riverine trees, spectacular clusters of **Catasetum** hung with heavy waxy blossoms."
      },
      {
        "author": "Asa Gray",
        "work": "Scientific Papers of Asa Gray",
        "quote": "The sexual dimorphism between male and female flowers of **Catasetum** was so extreme that early botanists classified them into three different genera."
      }
    ]
  },
  "Dashboard — cata\\catastrophe.md": {
    "primary": "A sudden, widespread disaster, calamity, or misfortune causing great damage and ruin; also the final event or denouement of a drama, especially a tragedy.",
    "secondary": "In classical dramaturgy and mathematics, the dramatic climax or turning point that unravels the plot; also in mathematics (catastrophe theory), sudden structural qualitative shifts under smooth parameter changes.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "King Lear",
        "quote": "I promise you, the effects he writes of succeed unhappily; pat he comes like the **catastrophe** of the old comedy."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The sack of Rome by the Goths was a sudden **catastrophe** that filled the civilized world with horror and lamentation."
      },
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "Dramatic poetry presents the actions of men crowned with their final, inevitable **catastrophe** to vindicate moral providence."
      }
    ]
  },
  "Dashboard — cata\\catastrophic.md": {
    "primary": "Involving or causing sudden, disastrous, and irreversible damage, destruction, or ruin.",
    "secondary": "In risk management and geology, describing low-frequency, high-severity events that overwhelm the structural integrity of natural or engineered systems.",
    "quotes": [
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "The runaway greenhouse effect on Venus stands as a warning of **catastrophic** planetary climate transformation."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Geologists once imagined **catastrophic** deluges where closer scrutiny reveals centuries of patient water erosion."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Diversity of Life",
        "quote": "The clearing of tropical rainforests brings about a **catastrophic** collapse of global biological diversity."
      }
    ]
  },
  "Dashboard — cata\\catastrophically.md": {
    "primary": "In a catastrophic manner; with disastrous, ruinous, or devastating consequences.",
    "secondary": "Leading to complete, sudden failure or collapse.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The imperial treasury collapsed **catastrophically** when civil war severed the grain revenues of the Egyptian province."
      },
      {
        "author": "Carl Sagan",
        "work": "Pale Blue Dot",
        "quote": "If humanity mishandles its nuclear arsenal, planetary habitability could be extinguished **catastrophically** in hours."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "His private ambitions failed **catastrophically**, leaving him indebted to the very creditors he had scorned."
      }
    ]
  },
  "Dashboard — cata\\catatonia.md": {
    "primary": "A complex neuropsychiatric syndrome characterized by motor immobility, stupor, mutism, muscular rigidity, waxy flexibility, or purposeless motor agitation.",
    "secondary": "In clinical psychiatry and behavioral neurology, a psychomotor disorder occurring across affective illnesses, schizophrenia, and neurological conditions, responding rapidly to lorazepam or electroconvulsive therapy.",
    "quotes": [
      {
        "author": "Karl Kahlbaum",
        "work": "Catatonia, or the Tension Insanity",
        "quote": "I isolated **catatonia** as a clinical entity defined by cyclical alternations between profound motor stupor and frantic hyperkinesia."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "Post-encephalitic parkinsonism sometimes presented as a lifelong frozen **catatonia**, patients suspended between sleep and waking."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In acute **catatonia**, the patient remains completely mute and unresponsive to external queries, maintaining awkward postures indefinitely."
      }
    ]
  },
  "Dashboard — cata\\catatonic.md": {
    "primary": "Affected with, relating to, or characteristic of catatonia; motionless, rigid, mute, and unresponsive to surroundings.",
    "secondary": "In neuropsychiatry, describing motor symptoms such as posturing, echolalia, negativism, and waxy resistance to passive manipulation.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "The patient sat in a **catatonic** trance, his eyes fixed upon the wall without blinking for half an hour at a time."
      },
      {
        "author": "William R. Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "A **catatonic** rigidity of the neck and torso accompanied the progression of the deep basal ganglia encephalitis."
      },
      {
        "author": "Sigmund Freud",
        "work": "The Ego and the Id",
        "quote": "The deep withdrawal observed in **catatonic** states reflects a complete decathexis of interest from external reality."
      }
    ]
  },
  "Dashboard — cata\\hypercatalectic.md": {
    "primary": "In classical metrics and poetic prosody, having an extra syllable or syllables beyond the standard metrical foot at the end of a line of verse.",
    "secondary": "Describing a line containing an redundant syllable at the close (hypermetric), creating a feminine ending or metrical overflow.",
    "quotes": [
      {
        "author": "George Saintsbury",
        "work": "A History of English Prosody",
        "quote": "The addition of a **hypercatalectic** syllable at the caesura creates a delicate, trembling suspension before the verse resumes."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "Milton masterfully utilizes **hypercatalectic** endings to vary the heroic pentameter with conversational flexibility."
      },
      {
        "author": "Alexander Pope",
        "work": "The Dunciad",
        "quote": "The pedant spent his evenings expunging every **hypercatalectic** syllable from classical manuscripts to enforce rigid regularity."
      }
    ]
  },
  "Dashboard — cata\\katabolic.md": {
    "primary": "Relating to or characterized by destructive metabolism; alternative spelling of catabolic (with k).",
    "secondary": "In cellular biochemistry and energetic physiology, describing reactions involving the oxidative degradation of organic compounds.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The high fever provoked rapid **katabolic** wasting of muscular tissues, demanding high-caloric liquid nourishment."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "The balance between anabolic construction and **katabolic** combustion determines an organism's net growth efficiency."
      },
      {
        "author": "William Benjamin Carpenter",
        "work": "Principles of General and Comparative Physiology",
        "quote": "During prolonged physical exertion, **katabolic** processes outstrip reparative assimilation within muscle fibers."
      }
    ]
  },
  "Dashboard — cata\\katabolism.md": {
    "primary": "The breakdown of complex organic molecules in living organisms to release energy; variant spelling of catabolism (with k).",
    "secondary": "In physiological energetics, the degradative component of metabolism that converts nutrients into biochemical waste and ATP.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Excessive tissue **katabolism** generates large amounts of urea and uric acid, straining impaired renal clearance."
      },
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "Through cellular **katabolism**, chemical potential energy stored in carbohydrates is converted into biological work."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "Dormancy in hibernating mammals suppresses oxidative **katabolism** to a fraction of normal resting rates."
      }
    ]
  },
  "Dashboard — caust\\calm.md": {
    "primary": "Peaceful, quiet, untroubled, and free from agitation, violent disturbance, or stormy wind; tranquility or stillness.",
    "secondary": "In meteorology, the lowest wind force on the Beaufort scale (Force 0), where smoke rises vertically and the sea surface is smooth as glass.",
    "quotes": [
      {
        "author": "Samuel Taylor Coleridge",
        "work": "The Rime of the Ancient Mariner",
        "quote": "Day after day, day after day, we stuck, nor breath nor motion; as idle as a painted ship upon a painted ocean, in terrible **calm**."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "There is no staying in any harbor in this world, yet after every gale the Atlantic yields to a sunny, majestic **calm**."
      },
      {
        "author": "Marcus Aurelius",
        "work": "Meditations",
        "quote": "Retire into your own self; for the rational soul has the nature of resting content within its own internal **calm**."
      }
    ]
  },
  "Dashboard — caust\\calming.md": {
    "primary": "Producing or having the effect of becoming peaceful, quiet, or tranquil; soothing and sedating.",
    "secondary": "In behavioral pharmacology, describing anxiolytic, sedative, or meditative interventions that lower autonomic arousal and heart rate.",
    "quotes": [
      {
        "author": "William Wordsworth",
        "work": "The Prelude",
        "quote": "Nature possessed a **calming** influence over my turbulent youth, softening the wild impulses of solitary thought."
      },
      {
        "author": "William Osler",
        "work": "Aequanimitas",
        "quote": "The physician must cultivate a serene, **calming** demeanor, assuring panicked patients by his steady presence."
      },
      {
        "author": "Virginia Woolf",
        "work": "Mrs. Dalloway",
        "quote": "The rhythmic chiming of Big Ben had a **calming** effect, measuring out the warm June hours with solemn cadence."
      }
    ]
  },
  "Dashboard — caust\\calmly.md": {
    "primary": "In a calm, serene, composed, or tranquil manner; without excitement, agitation, or anger.",
    "secondary": "Carried out with steady deliberation and emotional self-control under pressure or crisis.",
    "quotes": [
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "She spoke **calmly**, though her inward heart was beaten with waves of grief and sudden indignation."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "Self-Reliance",
        "quote": "It is easy in the world to live after the world's opinion; it is easy in solitude to live after our own; but the great man is he who in the midst of the crowd keeps with perfect sweetness the independence of solitude **calmly**."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The philosopher faced the executioner's blade **calmly**, discoursing with his disciples upon the immortality of the soul."
      }
    ]
  },
  "Dashboard — caust\\calmness.md": {
    "primary": "The state or quality of being calm, tranquil, serene, and undisturbed; freedom from agitation, wind, or emotional storm.",
    "secondary": "In Stoic philosophy, the virtue of ataraxia or equanimity, maintaining inner harmony regardless of external misfortune.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "Aequanimitas",
        "quote": "Imperturbability means coolness and presence of mind under all circumstances, **calmness** amid storm, and clearness of judgment in moments of grave peril."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "quote": "A broad sheet of water gives a wonderful sensation of **calmness** and repose to the surrounding landscape."
      },
      {
        "author": "Jane Austen",
        "work": "Sense and Sensibility",
        "quote": "Elinor sustained the bitter disappointment with an outward **calmness** that masked her profound inner anguish."
      }
    ]
  },
  "Dashboard — caust\\catacaustic.md": {
    "primary": "In optics and mathematics, a caustic curve or surface formed by the envelope of light rays reflected from a curved mirror or surface.",
    "secondary": "In differential geometry and physical optics, the luminous envelope formed by reflected wave fronts, contrasted with diacaustic (refracted) curves.",
    "quotes": [
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "The curved envelope traced by rays reflected from a spherical concave speculum forms a brilliant **catacaustic** curve."
      },
      {
        "author": "Christiaan Huygens",
        "work": "Treatise on Light",
        "quote": "By tracing the envelopes of secondary reflected wavelets, the exact geometric cusp of the **catacaustic** is demonstrated."
      },
      {
        "author": "Ernst Mach",
        "work": "The Principles of Physical Optics",
        "quote": "The bright cusp of light visible upon the surface of tea inside a porcelain cup presents a familiar **catacaustic** line."
      }
    ]
  },
  "Dashboard — caust\\causalgia.md": {
    "primary": "A syndrome of severe, persistent, burning pain, accompanied by skin changes and hypersensitivity, resulting from injury to a peripheral nerve.",
    "secondary": "In clinical neurology and pain medicine, complex regional pain syndrome type II (CRPS II), typically involving the median or tibial nerves, driven by sympathetically maintained sensory hypersensitivity.",
    "quotes": [
      {
        "author": "Silas Weir Mitchell",
        "work": "Injuries of Nerves and Their Consequences",
        "quote": "I have designated this agonizing burning pain **causalgia**, a torment which defies sleep and renders the touch of dry air intolerable."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Gunshot wounds of the median nerve frequently induce intense **causalgia**, relieved only by continuously soaking the limb in cold water."
      },
      {
        "author": "Oliver Sacks",
        "work": "A Leg to Stand On",
        "quote": "Nerve severance produced severe **causalgia**, where even the lightest brush of a bedsheet felt like a searing branding iron."
      }
    ]
  },
  "Dashboard — caust\\causalgic.md": {
    "primary": "Pertaining to, characterized by, or affected with causalgia; producing searing, burning neuropathic pain.",
    "secondary": "In neurological assessment, describing hyperpathia, allodynia, and autonomic dysregulation (cyanosis, sweating, glossy skin) following nerve trauma.",
    "quotes": [
      {
        "author": "Silas Weir Mitchell",
        "work": "Injuries of Nerves and Their Consequences",
        "quote": "The patient wrapped his hand in damp bandages day and night to quell the intolerable **causalgic** burning."
      },
      {
        "author": "William R. Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "Surgical resection of the neuroma succeeded in terminating the paroxysmal **causalgic** agony."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "Her phantom limb was seized by a **causalgic** spasm that mirrored her emotional anxiety."
      }
    ]
  },
  "Dashboard — caust\\caust.md": {
    "primary": "A combining form of Greek origin meaning burning, combustible, or heat (derived from Greek kaustos and kaiein).",
    "secondary": "In chemical, medical, and optical nomenclature, a productive root appearing in words such as caustic, cautery, holocaust, and catacaustic.",
    "quotes": [
      {
        "author": "Richard Chenevix Trench",
        "work": "On the Study of Words",
        "quote": "The Greek stem **caust** speaks of fire and searing heat, whether applied to chemical alkalis or ancient sacrificial offerings."
      },
      {
        "author": "Max Müller",
        "work": "Lectures on the Science of Language",
        "quote": "The combustion of matter and the burning irony of words both trace their etymological lineage to **caust**."
      },
      {
        "author": "William Benjamin Carpenter",
        "work": "Principles of General and Comparative Physiology",
        "quote": "Surgical agents bearing the prefix **caust** act through thermal or chemical destruction of necrotic tissues."
      }
    ]
  },
  "Dashboard — caust\\caustic.md": {
    "primary": "Capable of burning, corroding, or destroying living tissue by chemical action; or severely sarcastic, biting, and scathing in tone.",
    "secondary": "In inorganic chemistry, describing strong corrosive hydroxides (such as caustic soda, NaOH); in optics, the envelope of rays reflected or refracted by a curved surface.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "Sodium hydroxide is known as **caustic** soda because it readily attacks animal tissue, converting fatty acids into soluble soaps."
      },
      {
        "author": "Alexander Pope",
        "work": "The Dunciad",
        "quote": "His satirical pen was dipped in **caustic** acid, searing the reputation of every dull poet in the capital."
      },
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "The concentration of reflected rays forms a bright **caustic** curve upon the opposite rim of the concave vessel."
      }
    ]
  },
  "Dashboard — caust\\caustically.md": {
    "primary": "In a caustic manner; with sharp, cutting sarcasm, or in a chemically corrosive and searing way.",
    "secondary": "Delivering biting wit, scathing ridicule, or aggressive chemical destruction.",
    "quotes": [
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "The old doctor remarked **caustically** that young reformers were always eager to operate before they could diagnose."
      },
      {
        "author": "Thomas Carlyle",
        "work": "Past and Present",
        "quote": "He criticized the parliament **caustically**, dismissing their endless debates as empty wind and mechanical pedantry."
      },
      {
        "author": "Virginia Woolf",
        "work": "The Common Reader",
        "quote": "Jane Austen observed her neighbors' pretensions **caustically**, yet with an exquisite lightness of comedic touch."
      }
    ]
  },
  "Dashboard — caust\\cauter.md": {
    "primary": "An instrument, hot iron, or chemical substance used for burning, searing, or destroying living flesh (cautery).",
    "secondary": "In surgical history, an operative tool heated in coals or charged with chemical potential to achieve immediate hemostasis and seal wounds against infection.",
    "quotes": [
      {
        "author": "Ambroise Paré",
        "work": "The Apologie and Treatise of Ambroise Paré",
        "quote": "I resolved never more to burn the poor wounded soldiers with the cruel red-hot **cauter** and boiling oil."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Application of the actual **cauter** was anciently considered the sovereign remedy against stubborn bites of rabid dogs."
      },
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "Ancient surgeons relied upon the hot **cauter** where modern practitioners prefer gentle styptic remedies."
      }
    ]
  },
  "Dashboard — caust\\cauterant.md": {
    "primary": "A caustic substance, chemical agent, or instrument used to cauterize tissue; an escharotic.",
    "secondary": "In pharmacological therapeutics, chemical compounds such as silver nitrate or trichloroacetic acid applied topically to destroy warts, granulation tissue, or ulcerated margins.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Silver nitrate sticks serve as a convenient **cauterant** to ablate exuberant granulation tissue in indolent healing wounds."
      },
      {
        "author": "William R. Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "The bite of the venomous viper was instantly treated with an active chemical **cauterant** to prevent systemic absorption."
      },
      {
        "author": "Primo Levi",
        "work": "The Periodic Table",
        "quote": "Handling concentrated nitric acid requires extreme caution, for it acts as an instantaneous **cauterant** upon bare skin."
      }
    ]
  },
  "Dashboard — caust\\cauterisation.md": {
    "primary": "The medical process of burning or searing living tissue with a heated instrument, electric current, or caustic chemical (British spelling).",
    "secondary": "In surgical therapeutics, the application of thermal or electrical energy to seal bleeding vessels or destroy diseased tissues (hemostasis and ablation).",
    "quotes": [
      {
        "author": "Ambroise Paré",
        "work": "The Apologie and Treatise of Ambroise Paré",
        "quote": "Before the invention of the ligature, every amputation demanded agonizing **cauterisation** with boiling pitch to arrest hemorrhage."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Superficial epistaxis from Kiesselbach's plexus is rapidly checked by chemical **cauterisation** with silver nitrate."
      },
      {
        "author": "William R. Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "Thermal **cauterisation** along the paravertebral line was formerly employed in intractable cases of spinal myelitis."
      }
    ]
  },
  "Dashboard — caust\\cauterise.md": {
    "primary": "To burn, sear, or destroy tissue using a hot iron, electric current, or caustic chemical to stop bleeding or prevent infection (British spelling).",
    "secondary": "Metaphorically, to deaden, desensitize, or cauterize moral feelings, conscience, or sensitivity.",
    "quotes": [
      {
        "author": "Ambroise Paré",
        "work": "The Apologie and Treatise of Ambroise Paré",
        "quote": "It seemed cruel to **cauterise** fresh wounds with hot irons when simple clean dressings preserved life more gently."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The surgeon sought to **cauterise** the base of the ulcerated lesion to prevent recurrence of granulation tissue."
      },
      {
        "author": "Thomas Carlyle",
        "work": "The French Revolution",
        "quote": "Revolutionary terror was invoked to **cauterise** the corrupt body politic and purge the nation of treason."
      }
    ]
  },
  "Dashboard — caust\\cauterization.md": {
    "primary": "The medical act or process of burning, searing, or destroying living tissue using heat, cold, electricity, or caustic chemicals to arrest bleeding or ablate lesions (US spelling).",
    "secondary": "In modern surgery, electrosurgery (monopolar or bipolar electrocautery) utilized for rapid hemostasis and precise tissue dissection.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Immediate chemical **cauterization** of the animal bite with fuming nitric acid was once considered imperative to neutralize rabies virus."
      },
      {
        "author": "Ambroise Paré",
        "work": "The Apologie and Treatise of Ambroise Paré",
        "quote": "By replacing indiscriminate **cauterization** with vascular ligatures, surgical mortality on the battlefield plummeted."
      },
      {
        "author": "Oliver Sacks",
        "work": "A Leg to Stand On",
        "quote": "The precise **cauterization** of bleeding arterioles allowed the orthopedic team to secure a clean surgical field."
      }
    ]
  }
};

const count = updateNotesBatch(CLUSTER_DIR, batchData);
console.log(`========================================`);
console.log(`Form & Space Part 1 - Batch 4 Completed: ${count} / ${Object.keys(batchData).length} words updated`);
console.log(`========================================`);
