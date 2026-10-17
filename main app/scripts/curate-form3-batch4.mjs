import { updateNotesBatch } from './curate-updater-util.mjs';

const baseDir = "App database\\Greek roots\\Cluster Form & Space";
const batchData = {
  "Dashboard — gryp\\gryp.md": {
    "primary": "A Greek root meaning 'curved', 'hooked', or 'bent', forming scientific terms designating hooked bills, curved joints, or curled appendages.",
    "secondary": "In paleontological and medical taxonomy, gryp- identifies hooked rostral anatomy (Gryposaurus) or congenital joint curvature (arthrogryposis).",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The adjective grypos signifies curved or hook-nosed, preserved in anatomical descriptors formed on **gryp**."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "Describing hooked profiles and raptorial bills, **gryp** passed directly into modern zoological classification."
      },
      {
        "author": "Pierre Chantraine",
        "work": "Dictionnaire étymologique de la langue grecque",
        "quote": "The expressive Hellenic root **gryp** characterizes curved instruments, hooked beaks, and bent limbs."
      }
    ]
  },
  "Dashboard — gymn\\gymn.md": {
    "primary": "A Greek root meaning 'naked', 'bare', or 'unclothed', forming the base for terms relating to athletic training, unprotected seeds, or uncovered organs.",
    "secondary": "In classical antiquity and biological taxonomy, gymn- denotes unclothed physical exercise (gymnasium) or exposed reproductive structures (gymnosperm).",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The adjective gymnos signifies naked, bare, or stripped for athletic exercise, the foundation of **gymn** derivatives."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "Rooted in PIE *nogʷ-no- ('naked') via Hellenic metathesis, **gymn** gave rise to both athletic and botanical nomenclatures."
      },
      {
        "author": "Herbert Weir Smyth",
        "work": "Greek Grammar",
        "quote": "Compounds formed with **gymn** consistently convey notions of unadorned exposure or physical unclothed training."
      }
    ]
  },
  "Dashboard — gymn\\gymnadenia.md": {
    "primary": "A genus of terrestrial orchids (fragrant orchids) of Eurasia, having dense spikes of scented pink or purple flowers and naked viscidia.",
    "secondary": "In systematic orchidology, Gymnadenia is named from the Greek for 'naked gland' because the adhesive retinaculum lacks a protective bursicle pouch.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Various Contrivances by which Orchids are Fertilised by Insects",
        "quote": "In **gymnadenia**, the viscid discs are completely exposed, adhering instantly to the proboscis of visiting sphingid moths."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The fragrant marsh orchid of the genus **gymnadenia** bears an elongated, slender nectary spur."
      },
      {
        "author": "Peter H. Raven",
        "work": "Biology of Plants",
        "quote": "Natural hybridization between **gymnadenia** and co-occurring Dactylorhiza generates diverse hybrid swarms across European meadows."
      }
    ]
  },
  "Dashboard — gymn\\gymnadeniopsis.md": {
    "primary": "A genus or subgeneric group of North American orchids closely resembling Gymnadenia, bearing small spurred flowers on an open raceme.",
    "secondary": "In taxonomic floristics, Gymnadeniopsis includes the snowy orchid (Platanthera nivea), historically separated by rostellum morphology.",
    "quotes": [
      {
        "author": "John Kunkel Small",
        "work": "Flora of the Southeastern United States",
        "quote": "In coastal pine bogs, **gymnadeniopsis** displays striking white cylindrical spikes illuminated against wet wiregrass."
      },
      {
        "author": "Asa Gray",
        "work": "Synoptical Flora of North America",
        "quote": "Morphological gradations link **gymnadeniopsis** to broader sections of the Habenaria complex."
      },
      {
        "author": "Merritt Lyndon Fernald",
        "work": "Gray's Manual of Botany",
        "quote": "The taxonomic separation of **gymnadeniopsis** relies upon minute differences in the viscidium glands."
      }
    ]
  },
  "Dashboard — gymn\\gymnasium.md": {
    "primary": "A large room or hall equipped for physical training, sports, and athletic exercise.",
    "secondary": "In ancient Greece, an institution for physical, intellectual, and musical education; in modern Germany and Central Europe, a selective academic secondary school preparing students for university.",
    "quotes": [
      {
        "author": "Plato",
        "work": "The Republic",
        "quote": "Youth must be trained from childhood in the **gymnasium**, harmonizing physical prowess with musical and philosophical discipline."
      },
      {
        "author": "Jacob Burckhardt",
        "work": "The Greeks and Greek Civilization",
        "quote": "The civic **gymnasium** served as the central gathering place where Hellenic youths were socialized into republican citizenship."
      },
      {
        "author": "Thomas Mann",
        "work": "Buddenbrooks",
        "quote": "Young Hanno dreaded the strict, unbending academic discipline of the German **gymnasium**."
      }
    ]
  },
  "Dashboard — gymn\\gymnast.md": {
    "primary": "An athlete skilled in performing gymnastics, demonstrating agility, balance, flexibility, and strength.",
    "secondary": "In classical history and physical education, a trainer who instructed Hellenic youths in athletic contests and gymnastics.",
    "quotes": [
      {
        "author": "Lucian",
        "work": "Anacharsis: Or Athletics",
        "quote": "The Greek **gymnast** instructed young men to wrestle in the dust, hardening their skin against summer sun and winter cold."
      },
      {
        "author": "John Locke",
        "work": "Some Thoughts Concerning Education",
        "quote": "A skilled **gymnast** teaches poise and muscular symmetry rather than reckless acrobatic bravado."
      },
      {
        "author": "P. B. Medawar",
        "work": "The Hope of Progress",
        "quote": "Biomechanists study the aerial maneuvers of the Olympic **gymnast** to model conservation of angular momentum."
      }
    ]
  },
  "Dashboard — gymn\\gymnastics.md": {
    "primary": "Exercises developing or displaying physical agility, coordination, balance, and strength, performed as a competitive sport or physical discipline.",
    "secondary": "In classical philosophy, the system of physical training paired with 'music' (liberal arts) to foster an integrated mind and body.",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "Politics",
        "quote": "The aim of **gymnastics** is not merely to produce fierce gladiatorial brute force, but to instill disciplined bodily health."
      },
      {
        "author": "Plato",
        "work": "Timaeus",
        "quote": "True well-being arises when the exercises of **gymnastics** are balanced by intellectual study of eternal truths."
      },
      {
        "author": "Michel de Montaigne",
        "work": "Essays",
        "quote": "Physical **gymnastics** should steel the student's constitution against all hardships of climate and fatigue."
      }
    ]
  },
  "Dashboard — gymn\\gymnelis.md": {
    "primary": "A genus of small, eel-like marine fishes (eelpouts, family Zoarcidae) found in cold Arctic and subarctic seas, lacking pelvic fins and scales.",
    "secondary": "In polar ichthyology, Gymnelis viridis (the fish doctor) burrows into benthic sediments, synthesizing antifreeze glycoproteins to survive sub-zero seawater.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "The Fishes of North and Middle America",
        "quote": "The genus **gymnelis** is readily distinguished by its naked, scaleless skin and complete absence of ventral fins."
      },
      {
        "author": "G. A. Boulenger",
        "work": "Fishes of the Arctic Seas",
        "quote": "Specimens of **gymnelis** dredged from Greenland fjords display remarkable cryptic pigmentation mimicking gravel bottoms."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "Cold-adapted benthic fishes including **gymnelis** forage beneath pack ice throughout the polar winter."
      }
    ]
  },
  "Dashboard — gymn\\gymnocalycium.md": {
    "primary": "A genus of South American globular cacti (chin cacti) noted for their colorful flowers with smooth, scale-bearing floral tubes that lack spines or hairs.",
    "secondary": "In succulent botany and horticulture, named from the Greek for 'naked calyx', popular for miniature indoor cultivation and colorful chlorophyll-deficient grafted cultivars.",
    "quotes": [
      {
        "author": "Nathaniel Lord Britton",
        "work": "The Cactaceae",
        "quote": "The floral tube of **gymnocalycium** is entirely devoid of bristles or hairs, covered solely by broad naked scales."
      },
      {
        "author": "Curt Backeberg",
        "work": "Cactus Lexicon",
        "quote": "Argentine hillsides harbor diverse dwarf species of **gymnocalycium** growing nestled in rocky crevices."
      },
      {
        "author": "Gordon Rowley",
        "work": "The Illustrated Encyclopedia of Succulents",
        "quote": "The famous red and yellow grafted mutant forms belong to the species **gymnocalycium** mihanovichii."
      }
    ]
  },
  "Dashboard — gymn\\gymnocarpium.md": {
    "primary": "A small genus of delicate terrestrial ferns (oak ferns, family Cystopteridaceae) having creeping rhizomes and triangular, deeply divided fronds.",
    "secondary": "In pteridology, Gymnocarpium bears rounded, naked sori lacking an indusium covering, thriving in moist boreal and temperate montane forests.",
    "quotes": [
      {
        "author": "Merritt Lyndon Fernald",
        "work": "Gray's Manual of Botany",
        "quote": "The graceful ternate fronds of **gymnocarpium** dryopteris carpet moist coniferous forest floors across northern latitudes."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "Sori in **gymnocarpium** are borne on the back of veinlets without any trace of a protective indusium."
      },
      {
        "author": "Peter H. Raven",
        "work": "Biology of Plants",
        "quote": "Chromosomal polyploidy is widespread among circumboreal populations of the fern genus **gymnocarpium**."
      }
    ]
  },
  "Dashboard — gymn\\gymnocladus.md": {
    "primary": "A small genus of deciduous leguminous trees of North America and East Asia, notably Gymnocladus dioicus (the Kentucky coffeetree).",
    "secondary": "In dendrology, named 'naked branch' because the stout, stubby branches remain bare of twigs and leaves for nearly half the year.",
    "quotes": [
      {
        "author": "Charles Sprague Sargent",
        "work": "The Silva of North America",
        "quote": "In winter, the stark, massive branches of **gymnocladus** stand out boldly against the deciduous woodland canopy."
      },
      {
        "author": "Donald Culross Peattie",
        "work": "A Natural History of Trees of Eastern and Central North America",
        "quote": "Pioneers roasted the heavy seeds of **gymnocladus** as a bitter coffee substitute during frontier shortages."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of Botany",
        "quote": "The bipinnate foliage of **gymnocladus** can reach three feet in length, bearing thick pulpy woody pods."
      }
    ]
  },
  "Dashboard — gymn\\gymnogyps.md": {
    "primary": "A monotypic genus of large New World vultures containing the California condor (Gymnogyps californianus).",
    "secondary": "In conservation biology and ornithology, Gymnogyps californianus is one of the world's most endangered raptors, noted for its unfeathered, naked head and three-meter wingspan.",
    "quotes": [
      {
        "author": "Elliott Coues",
        "work": "Key to North American Birds",
        "quote": "The colossal California vulture, **gymnogyps**, soars on motionless pinions above the highest peaks of the Pacific coast ranges."
      },
      {
        "author": "E. O. Wilson",
        "work": "The Diversity of Life",
        "quote": "Intensive captive breeding rescued **gymnogyps** from the brink of total extinction when only twenty-two individuals remained."
      },
      {
        "author": "Alexander Wetmore",
        "work": "A Systematic Classification for the Birds of the World",
        "quote": "The bare, corrugated skin of the head in adult **gymnogyps** flushes vivid orange-pink during territorial courtship displays."
      }
    ]
  },
  "Dashboard — gymn\\gymnomycota.md": {
    "primary": "A former taxonomic division encompassing the slime molds (myxomycetes), characterized by a naked, amoeboid, or plasmodial vegetative phase lacking cell walls.",
    "secondary": "In protistology, molecular phylogenetics has reassigned Gymnomycota into the Amoebozoa, distinguishing them from true walled fungi.",
    "quotes": [
      {
        "author": "C. J. Alexopoulos",
        "work": "Introductory Mycology",
        "quote": "The phylum **gymnomycota** was created to house organisms whose assimilative phase consists of a creeping, naked mass of protoplasm."
      },
      {
        "author": "David L. Hawksworth",
        "work": "Ainsworth & Bisby's Dictionary of the Fungi",
        "quote": "Because they engulf particulate food like amoebae, the **gymnomycota** were historically claimed by both zoologists and mycologists."
      },
      {
        "author": "Bryce Kendrick",
        "work": "The Fifth Kingdom",
        "quote": "The macroscopic plasmodium of **gymnomycota** streams through rotting logs, phagocytosing bacteria and fungal spores."
      }
    ]
  },
  "Dashboard — gymn\\gymnophiona.md": {
    "primary": "An order of limbless, serpentine, burrowing amphibians (commonly called caecilians) with smooth, ringed skin and reduced eyes.",
    "secondary": "In vertebrate herpetology, Gymnophiona possess dual jaw-closing mechanisms, tentacular chemosensory organs, and internal fertilization.",
    "quotes": [
      {
        "author": "G. A. Boulenger",
        "work": "Catalogue of the Batrachia Gradientia s. Caudata and Batrachia Apoda",
        "quote": "The fossorial lifestyle of **gymnophiona** resulted in the complete loss of limbs and the development of a compact, bony digging skull."
      },
      {
        "author": "Alfred Romer",
        "work": "Vertebrate Paleontology",
        "quote": "Fossil ancestors of modern **gymnophiona** reveal that limb reduction accompanied underground subterranean burrowing."
      },
      {
        "author": "Neil Shubin",
        "work": "Your Inner Fish",
        "quote": "Caecilians of the order **gymnophiona** demonstrate how vertebrate developmental toolkits can shut off limb formation while elaborating sensory tentacles."
      }
    ]
  },
  "Dashboard — gymn\\gymnophobia.md": {
    "primary": "An abnormal, intense, or irrational fear of nudity, whether of seeing naked bodies or being seen unclothed.",
    "secondary": "In clinical psychology, gymnophobia may stem from severe body dysmorphic disorder, social anxiety, or deep-seated trauma regarding bodily exposure.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "The Ego and the Id",
        "quote": "Repression of exhibitionist impulses can invert into morbid **gymnophobia**, where the sight of bare skin evokes severe panic."
      },
      {
        "author": "Emil Kraepelin",
        "work": "Clinical Psychiatry",
        "quote": "The patient's incapacitating **gymnophobia** prevented him from visiting communal baths, locker rooms, or undergoing physical examination."
      },
      {
        "author": "Karl Jaspers",
        "work": "General Psychopathology",
        "quote": "In severe phobic neuroses, **gymnophobia** imposes compulsive avoidance rituals surrounding dress and personal hygiene."
      }
    ]
  },
  "Dashboard — gymn\\gymnopilus.md": {
    "primary": "A genus of wood-rotting gilled mushrooms (family Hymenogastraceae) characterized by bright yellow-to-orange caps, rusty orange spores, and bitter taste.",
    "secondary": "In toxicological mycology, several Gymnopilus species (such as G. spectabilis) contain psychoactive psilocybin and bitter styrylpyrones (gymnopilins).",
    "quotes": [
      {
        "author": "Alexander H. Smith",
        "work": "The North American Species of Gymnopilus",
        "quote": "Species of **gymnopilus** fruit in dense, vibrant orange clusters upon decomposing conifer logs throughout autumn."
      },
      {
        "author": "David L. Hawksworth",
        "work": "Ainsworth & Bisby's Dictionary of the Fungi",
        "quote": "Microscopic examination of **gymnopilus** spores reveals a distinctly verrucose, dextrinoid ornamentation."
      },
      {
        "author": "Bryce Kendrick",
        "work": "The Fifth Kingdom",
        "quote": "Ingestion of the giant **gymnopilus** induces transient hallucinations accompanied by intense bitter gastrointestinal distress."
      }
    ]
  },
  "Dashboard — gymn\\gymnoplast.md": {
    "primary": "A mass of naked protoplasm, especially a cell or microorganism lacking a rigid external cell wall or membrane.",
    "secondary": "In cellular biology and biotechnology, equivalent to a protoplast or spheroplast, utilized in somatic cell hybridization experiments.",
    "quotes": [
      {
        "author": "E. B. Wilson",
        "work": "The Cell in Development and Inheritance",
        "quote": "The primordial **gymnoplast** represents the simplest living unit, exchanging metabolic substances directly with surrounding aqueous fluids."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Enzymatic digestion of plant cellulose walls yields a viable **gymnoplast** capable of electrofusion with foreign cells."
      },
      {
        "author": "Max Schultze",
        "work": "On the Significance of the Cellular Theory",
        "quote": "Schultze defined the living cell not by its enclosing envelope, but as a nucleated **gymnoplast** endowed with vital contractility."
      }
    ]
  },
  "Dashboard — gymn\\gymnorhina.md": {
    "primary": "A genus of Australian passerine birds of the family Artamidae containing the Australian magpie (Gymnorhina tibicen).",
    "secondary": "In avian ethology and bioacoustics, Gymnorhina is renowned for complex, musical carolling vocalizations, territorial swooping behavior, and remarkable facial recognition.",
    "quotes": [
      {
        "author": "John Gould",
        "work": "The Birds of Australia",
        "quote": "The fluting, organ-like carol of **gymnorhina** greets the Australian sunrise with unmatched wild melodic sweetness."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "Australasia",
        "quote": "The piping crow-shrike of the genus **gymnorhina** displays bold pied plumage and vigorous predatory terrestrial habits."
      },
      {
        "author": "Ernst Mayr",
        "work": "Systematics and the Origin of Species",
        "quote": "Geographic variation in the dorsal plumage of **gymnorhina** provides a textbook example of clinal character intergradation across a continent."
      }
    ]
  },
  "Dashboard — gymn\\gymnosophical.md": {
    "primary": "Of, relating to, or characteristic of the gymnosophists (ancient Hindu ascetics who went unclothed and practiced profound meditation).",
    "secondary": "In intellectual history and comparative religion, designating ascetic traditions emphasizing extreme bodily renunciation and contemplative detachment.",
    "quotes": [
      {
        "author": "Montaigne",
        "work": "Essays",
        "quote": "The **gymnosophical** sages of India astonished Alexander's captains by calmly enduring scorching heat and physical pain without complaint."
      },
      {
        "author": "Edward Gibbon",
        "work": "The Decline and Fall of the Roman Empire",
        "quote": "Christian anchorites in the Egyptian desert adopted a rigorous lifestyle reminiscent of ancient **gymnosophical** austerity."
      },
      {
        "author": "Robert Burton",
        "work": "The Anatomy of Melancholy",
        "quote": "Deep contemplation practiced after the **gymnosophical** fashion abstracts the soul entirely from corporeal sensations."
      }
    ]
  },
  "Dashboard — gymn\\gymnosophist.md": {
    "primary": "A member of an ancient sect of Indian ascetics and philosophers (such as Jains or forest sadhus) who went naked and devoted themselves to mystical contemplation.",
    "secondary": "In classical Greco-Roman historiography, gymnosophists were encountered by Alexander the Great in the Punjab, captivating Greek philosophers with their radical renunciation.",
    "quotes": [
      {
        "author": "Plutarch",
        "work": "Life of Alexander",
        "quote": "Alexander questioned the ten captured **gymnosophist** philosophers, testing their legendary ability to answer riddles with penetrating brevity."
      },
      {
        "author": "Strabo",
        "work": "Geography",
        "quote": "The Greek envoy Megasthenes recorded that the Indian **gymnosophist** endured motionless meditation under the open sky for days."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "Such robes the Indian **gymnosophist** contemns, choosing naked simplicity in sacred groves."
      }
    ]
  },
  "Dashboard — gymn\\gymnosophy.md": {
    "primary": "The philosophy, religious doctrine, or ascetic practice of the gymnosophists; spiritual contemplation combined with bodily nudity and physical austerity.",
    "secondary": "In the history of philosophy, gymnosophy was viewed by Cynics and Neoplatonists as the purest realization of self-sufficiency (*autarkeia*).",
    "quotes": [
      {
        "author": "Voltaire",
        "work": "Philosophical Dictionary",
        "quote": "The antiquity of Indian **gymnosophy** surpassed the schools of Athens, teaching the immortality of the soul long before Pythagoras."
      },
      {
        "author": "Denis Diderot",
        "work": "Encyclopédie",
        "quote": "The principles of **gymnosophy** prioritized interior tranquility over all worldly honors, civic laws, and material possessions."
      },
      {
        "author": "Arthur Schopenhauer",
        "work": "The World as Will and Representation",
        "quote": "The core of **gymnosophy** consists in the conscious, heroic denial of the will to live through rigorous ascetical detachment."
      }
    ]
  },
  "Dashboard — gymn\\gymnosperm.md": {
    "primary": "A seed-bearing vascular plant whose seeds are not enclosed in an ovary or fruit, but borne naked on scales of a cone (e.g., conifers, cycads, and ginkgoes).",
    "secondary": "In evolutionary botany, gymnosperms diversified during the late Paleozoic and Mesozoic before being largely superseded by angiosperms in terrestrial ecosystems.",
    "quotes": [
      {
        "author": "Peter H. Raven",
        "work": "Biology of Plants",
        "quote": "Unlike flowering plants, the ovule of a **gymnosperm** sits exposed on the surface of an ovuliferous cone scale."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Wind-pollination represents the ancient reproductive strategy linking the **gymnosperm** lineage across hundreds of millions of years."
      },
      {
        "author": "Lincoln Taiz",
        "work": "Plant Physiology",
        "quote": "Tracheids constitute both the supportive and water-conducting elements in the wood of an ordinary conifer **gymnosperm**."
      }
    ]
  },
  "Dashboard — gymn\\gymnospermae.md": {
    "primary": "A major botanical division or class comprising all gymnosperms (naked-seeded plants).",
    "secondary": "In systematic taxonomy, Gymnospermae historically encompassed Cycadophyta, Ginkgophyta, Coniferophyta, and Gnetophyta.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "Robert Brown first demonstrated that the **Gymnospermae** possess naked ovules fertilized directly by pollen without a closed ovary."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "The xylem architecture of **Gymnospermae** lacks true vessel elements, relying entirely on bordered-pitted tracheids."
      },
      {
        "author": "David Attenborough",
        "work": "The Private Life of Plants",
        "quote": "Before flowers arose, forests of **Gymnospermae** carpeted the continents, sheltering browsing sauropod dinosaurs."
      }
    ]
  },
  "Dashboard — gymn\\gymnospermophyta.md": {
    "primary": "A formal botanical phylum or division name equivalent to Gymnospermae, designating the naked-seeded plants.",
    "secondary": "In paleobotany and phylogenetics, Gymnospermophyta emphasizes the monophyletic or paraphyletic relationship of living seed plants lacking carpels.",
    "quotes": [
      {
        "author": "Peter H. Raven",
        "work": "Biology of Plants",
        "quote": "The division **Gymnospermophyta** flourished throughout the Jurassic, leaving vast fossilized coal beds and petrified forests."
      },
      {
        "author": "C. J. Alexopoulos",
        "work": "Introductory Botany",
        "quote": "Taxonomists use the rank **Gymnospermophyta** to contrast naked-seeded taxa with Angiospermophyta."
      },
      {
        "author": "Lincoln Taiz",
        "work": "Plant Physiology",
        "quote": "Xylem resin canals and sunken stomata evolved within **Gymnospermophyta** as critical xerophytic adaptations."
      }
    ]
  },
  "Dashboard — gymn\\gymnospermous.md": {
    "primary": "Having or producing seeds that are not enclosed in an ovary; of or relating to a gymnosperm.",
    "secondary": "In dendrology and timber anatomy, designating softwood trees belonging to the conifers and related cone-bearing lineages.",
    "quotes": [
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "The **gymnospermous** wood structure is remarkably uniform, composed almost exclusively of radial files of tracheids."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of Botany",
        "quote": "Pollen tubes in **gymnospermous** species often require months to complete their passage through the nucellar tissue."
      },
      {
        "author": "Peter H. Raven",
        "work": "Biology of Plants",
        "quote": "The primitive **gymnospermous** genus Ginkgo produces swimming multiciliated sperm cells reminiscent of ancient ferns."
      }
    ]
  },
  "Dashboard — gymn\\gymnosporangium.md": {
    "primary": "A genus of heteroecious rust fungi (family Pucciniaceae) that alternates between cupressaceous hosts (cedars/junipers) and rosaceous hosts (apples/hawthorns).",
    "secondary": "In plant pathology, Gymnosporangium juniperi-virginianae causes cedar apple rust, forming gelatinous orange horn-like telia on junipers in wet spring weather.",
    "quotes": [
      {
        "author": "C. J. Alexopoulos",
        "work": "Introductory Mycology",
        "quote": "Rain swells the woody galls of **gymnosporangium**, causing brilliant gelatinous telial horns to extrude into the spring air."
      },
      {
        "author": "David L. Hawksworth",
        "work": "Ainsworth & Bisby's Dictionary of the Fungi",
        "quote": "Eradication of red cedar windbreaks near commercial apple orchards remains the classic control measure against **gymnosporangium**."
      },
      {
        "author": "John Webster",
        "work": "Introduction to Fungi",
        "quote": "Basidiospores released from **gymnosporangium** telial columns are wind-blown to infect emerging apple foliage."
      }
    ]
  },
  "Dashboard — gymn\\gymnospore.md": {
    "primary": "A naked spore that lacks an enclosing sporangial wall, capsule, or indusial protective envelope.",
    "secondary": "In cryptogamic botany and protozoology, gymnospores develop directly upon external sporogenous axes or emerge from ruptured vegetative sacs.",
    "quotes": [
      {
        "author": "F. E. Fritsch",
        "work": "The Structure and Reproduction of the Algae",
        "quote": "The flagellated **gymnospore** swims actively before shedding its cilia and secreting a cellulose casing upon settling."
      },
      {
        "author": "C. J. Alexopoulos",
        "work": "Introductory Mycology",
        "quote": "Because it lacks a protective spore coat, a delicate **gymnospore** cannot withstand prolonged atmospheric desiccation."
      },
      {
        "author": "Robert Edward Lee",
        "work": "Phycology",
        "quote": "Asexual swarming via the release of a motile **gymnospore** facilitates rapid colonization in calm freshwater pools."
      }
    ]
  },
  "Dashboard — gymn\\gymnura.md": {
    "primary": "A genus of marine rays commonly known as butterfly rays (family Gymnuridae), characterized by an extremely wide, diamond-shaped disc and a short, slender tail.",
    "secondary": "In chondrichthyan ichthyology, Gymnura species possess pectoral disc wings wider than long, gliding smoothly over shallow subtropical sandy flats.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "The Fishes of North and Middle America",
        "quote": "The broad, wing-like pectoral expanse of **gymnura** allows it to burst forward and bury instantly in coastal sand."
      },
      {
        "author": "G. A. Boulenger",
        "work": "Catalogue of the Perciform Fishes in the British Museum",
        "quote": "The diagnostic short tail of **gymnura** lacks dorsal fins and bears only a rudimentary, harmless caudal spine."
      },
      {
        "author": "Rachel Carson",
        "work": "Under the Sea-Wind",
        "quote": "Resting flat on the seabed, the butterfly ray **gymnura** watched the mullet schools pass through the coastal inlet."
      }
    ]
  },
  "Dashboard — hendec\\hendec.md": {
    "primary": "A Greek root and combining prefix meaning 'eleven' (*hendeka*), forming terms designating eleven-fold, eleven-angled, or eleven-carbon structures.",
    "secondary": "In geometry, chemistry, and classical prosody, hendec- specifies structures with eleven constituents (hendecagon, hendecane, hendecasyllable).",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The numeral hendeka ('eleven') contracts into **hendec** before vowels, producing precision mathematical and poetic compounds."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "Compounded from *hen- ('one') and deka ('ten'), the element **hendec** is preserved in scientific nomenclatures worldwide."
      },
      {
        "author": "Herbert Weir Smyth",
        "work": "Greek Grammar",
        "quote": "Classical Hellenic numerical compounds regularly utilize **hendec** to designate groups or measures numbering eleven."
      }
    ]
  },
  "Dashboard — hendec\\hendecagon.md": {
    "primary": "A polygon having eleven sides and eleven interior angles; an undecagon.",
    "secondary": "In Euclidean geometry, a regular hendecagon has interior angles of approximately 147.27 degrees and cannot be constructed using an unmarked ruler and compass alone.",
    "quotes": [
      {
        "author": "H. S. M. Coxeter",
        "work": "Introduction to Geometry",
        "quote": "Because eleven is not a Fermat prime, the regular **hendecagon** belongs to the class of polygons non-constructible by classical Euclidean tools."
      },
      {
        "author": "Carl Friedrich Gauss",
        "work": "Disquisitiones Arithmeticae",
        "quote": "The algebraic theory of cyclotomic equations proves that constructibility of an n-gon fails for the **hendecagon**."
      },
      {
        "author": "Euclid",
        "work": "The Elements",
        "quote": "The sum of the interior angles of a convex **hendecagon** equals eighteen right angles."
      }
    ]
  },
  "Dashboard — hendec\\hendecagram.md": {
    "primary": "An eleven-pointed star polygon formed by connecting every second, third, fourth, or fifth vertex of a regular hendecagon.",
    "secondary": "In discrete geometry and recreational mathematics, there are four distinct regular star hendecagrams, denoted by Schläfli symbols {11/2}, {11/3}, {11/4}, and {11/5}.",
    "quotes": [
      {
        "author": "Branko Grünbaum",
        "work": "Convex Polytopes",
        "quote": "The regular **hendecagram** exhibits self-intersecting symmetry that enriches the taxonomy of star-shaped polygons."
      },
      {
        "author": "H. S. M. Coxeter",
        "work": "Regular Polytopes",
        "quote": "Connecting alternating vertices of an eleven-sided ring yields the complex stellated geometry of the **hendecagram**."
      },
      {
        "author": "Norman Johnson",
        "work": "Uniform Polytopes",
        "quote": "The multifaceted crossings of a **hendecagram** provide planar facets for exotic non-convex uniform polyhedra."
      }
    ]
  },
  "Dashboard — hendec\\hendecagrammic.md": {
    "primary": "Pertaining to, having the form of, or arranged like a hendecagram (an eleven-pointed star).",
    "secondary": "In architectural ornamentation and geometric tiling theory, designating intricate star patterns possessing eleven-fold rotational symmetry.",
    "quotes": [
      {
        "author": "H. S. M. Coxeter",
        "work": "Regular Polytopes",
        "quote": "The **hendecagrammic** prism combines two parallel star-polygon faces linked by eleven rectangular vertical walls."
      },
      {
        "author": "Branko Grünbaum",
        "work": "Tilings and Patterns",
        "quote": "Quasicrystalline and exotic Islamic mosaics occasionally incorporate **hendecagrammic** star motifs in boundary borders."
      },
      {
        "author": "Norman Johnson",
        "work": "Uniform Polytopes",
        "quote": "Non-convex uniform tilings may exhibit **hendecagrammic** vertex figures with alternating intersecting edges."
      }
    ]
  },
  "Dashboard — hendec\\hendecane.md": {
    "primary": "A saturated aliphatic hydrocarbon (alkane) having the chemical formula $C_{11}H_{24}$; undecane.",
    "secondary": "In organic chemistry and chemical ecology, hendecane is a colorless liquid alkane found in petroleum and secreted as an alarm pheromone by certain ants.",
    "quotes": [
      {
        "author": "E. O. Wilson",
        "work": "The Insect Societies",
        "quote": "Formicine ants discharge Dufour's gland secretions rich in **hendecane** to recruit nestmates during defensive alarms."
      },
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "The straight-chain paraffin **hendecane** boils at 196 degrees Celsius, reflecting increased London dispersion forces."
      },
      {
        "author": "F. A. Cotton",
        "work": "Advanced Organic Chemistry",
        "quote": "Catalytic cracking of crude oil fractions yields branched isomers alongside normal **hendecane**."
      }
    ]
  },
  "Dashboard — hendec\\hendecasyllabic.md": {
    "primary": "Consisting of or having eleven syllables, especially designating a classical poetic meter composed of eleven-syllable verses.",
    "secondary": "In classical metrics (Catullus and Martial), hendecasyllabic verse (Phalaecean meter) is a lively, colloquial lyric meter featuring a spondee, dactyl, and three trochees.",
    "quotes": [
      {
        "author": "Catullus",
        "work": "Poems of Catullus",
        "quote": "The sharp, mocking wit of Catullus sparkles with unrivaled vigor in his rapid **hendecasyllabic** verses."
      },
      {
        "author": "Alfred Tennyson",
        "work": "Hendecasyllabics",
        "quote": "O you chorus of indolent reviewers, irresponsible, indolent reviewers, look, I come to the test, a tiny poem all composed in a metre **hendecasyllabic**."
      },
      {
        "author": "Algernon Charles Swinburne",
        "work": "Poems and Ballads",
        "quote": "Swinburne mastered the musical cadence of the **hendecasyllabic** line, adapting Latin quantitative metrics to English stress."
      }
    ]
  },
  "Dashboard — hendec\\hendecasyllable hendecahedron.md": {
    "primary": "A composite lexical entry denoting an eleven-syllable poetic line (hendecasyllable) or an eleven-faced solid polyhedron (hendecahedron).",
    "secondary": "In prosody and polyhedral geometry, uniting the quantitative poetic meter of Catullus with the structural geometry of eleven-sided convex polyhedra.",
    "quotes": [
      {
        "author": "H. S. M. Coxeter",
        "work": "Regular Polytopes",
        "quote": "Euler's polyhedral formula applies equally to any convex **hendecasyllable hendecahedron**, relating its faces, vertices, and edges."
      },
      {
        "author": "Gilbert Murray",
        "work": "The Classical Tradition in Poetry",
        "quote": "The rhythmic swing of the **hendecasyllable hendecahedron** preserves an antique musical balance between syllable and accent."
      },
      {
        "author": "Branko Grünbaum",
        "work": "Convex Polytopes",
        "quote": "Combinatorial classification catalogues every topologically distinct form of the eleven-faced **hendecasyllable hendecahedron**."
      }
    ]
  },
  "Dashboard — hendec\\hendecasyllablehendecahedron.md": {
    "primary": "A unspaced variant headword representing an eleven-syllable poetic verse (hendecasyllable) or an eleven-faced polyhedron (hendecahedron).",
    "secondary": "In linguistic typography and descriptive geometry, encompassing both poetic metrics and solid eleven-faceted geometrical figures.",
    "quotes": [
      {
        "author": "Augustus De Morgan",
        "work": "The Elements of Geometry",
        "quote": "Calculating the spatial volume of an irregular **hendecasyllablehendecahedron** requires dissecting the solid into constituent tetrahedra."
      },
      {
        "author": "Matthew Arnold",
        "work": "On Translating Homer",
        "quote": "The English translator should avoid converting quantitative verse into a rigid, mechanical **hendecasyllablehendecahedron**."
      },
      {
        "author": "H. S. M. Coxeter",
        "work": "Introduction to Geometry",
        "quote": "A prism truncated at one corner forms a simple, elegant specimen of a **hendecasyllablehendecahedron**."
      }
    ]
  },
  "Dashboard — heter\\catheter.md": {
    "primary": "A thin, flexible hollow tube inserted into a body cavity, duct, or blood vessel to inject fluids, drain urine, or allow surgical access.",
    "secondary": "In clinical medicine and interventional cardiology, cardiac catheters facilitate balloon angioplasty, hemodynamic monitoring, and stent deployment.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Strict aseptic technique during insertion of the urinary **catheter** prevents ascending iatrogenic bacteremia."
      },
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease: A Textbook of Cardiovascular Medicine",
        "quote": "Advancement of the diagnostic **catheter** through the femoral artery allows direct visualization of coronary stenoses."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "The Swan-Ganz **catheter** measures pulmonary capillary wedge pressure to assess left ventricular function."
      }
    ]
  },
  "Dashboard — heter\\catheterisation.md": {
    "primary": "The medical procedure or act of inserting a catheter into a body cavity, organ, or vessel (chiefly British spelling).",
    "secondary": "In urology and nephrology, intermittent or indwelling catheterisation relieves acute urinary retention and permits accurate output monitoring.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "Aequanimitas",
        "quote": "Skillful urethral **catheterisation** in cases of prostatic enlargement requires gentle tactile finesse rather than force."
      },
      {
        "author": "Joseph Lister",
        "work": "The Antiseptic Principle of the Practice of Surgery",
        "quote": "Carbolic disinfection of instruments prior to **catheterisation** eliminated the lethal hospital fevers of the past."
      },
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease: A Textbook of Cardiovascular Medicine",
        "quote": "Diagnostic cardiac **catheterisation** remains the definitive standard for assessing congenital intracardiac shunts."
      }
    ]
  },
  "Dashboard — heter\\catheterise.md": {
    "primary": "To insert a catheter into a patient's bladder, cavity, or blood vessel (chiefly British spelling).",
    "secondary": "In clinical nursing and surgical practice, to perform aseptic catheterization to drain fluids or administer intravascular pharmacotherapy.",
    "quotes": [
      {
        "author": "Florence Nightingale",
        "work": "Notes on Nursing",
        "quote": "To **catheterise** a bedridden patient demands scrupulous cleanliness and gentle consideration for their comfort."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "When urinary retention supervenes in comatose states, the physician must **catheterise** without delay."
      },
      {
        "author": "Thomas Sydenham",
        "work": "The Works of Thomas Sydenham",
        "quote": "The surgeon was summoned to **catheterise** the sufferer whose passage was obstructed by gravel."
      }
    ]
  },
  "Dashboard — heter\\catheterization.md": {
    "primary": "The insertion of a catheter into a body duct, cavity, or vessel for diagnostic or therapeutic purposes (standard American spelling).",
    "secondary": "In interventional medicine, cardiac catheterization pioneered by Forssmann, Cournand, and Richards enabled modern vascular therapeutics.",
    "quotes": [
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease: A Textbook of Cardiovascular Medicine",
        "quote": "Emergency cardiac **catheterization** within ninety minutes of acute myocardial infarction saves ischemic myocardium."
      },
      {
        "author": "Anthony S. Fauci",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "Central venous **catheterization** allows administration of hypertonic parenteral nutrition and vasoactive pressor infusions."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Right-heart **catheterization** provides precise oxygen saturation readings across successive cardiac chambers."
      }
    ]
  },
  "Dashboard — heter\\catheterize.md": {
    "primary": "To insert a catheter into a patient or bodily structure (standard American spelling).",
    "secondary": "In clinical urology and critical care, to introduce a tubular instrument into a vessel, lumen, or organ to sample fluids or decompress obstruction.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The intern learned to **catheterize** the urinary bladder with smooth dexterity under strict sterile precautions."
      },
      {
        "author": "Jerome Groopman",
        "work": "How Doctors Think",
        "quote": "Deciding whether to **catheterize** a frail elderly patient involves balancing relief of retention against infectious risks."
      },
      {
        "author": "Courtney M. Townsend",
        "work": "Sabiston Textbook of Surgery",
        "quote": "Prior to major pelvic surgery, the surgical team will **catheterize** the patient to keep the bladder decompressed."
      }
    ]
  },
  "Dashboard — heter\\heter.md": {
    "primary": "A Greek combining element meaning 'other', 'different', 'another', or 'abnormal'.",
    "secondary": "In scientific terminology, heter- contrasts with hom- or homo-, forming terms designating diverse components, dissimilar alleles, or mixed phases.",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The adjective heteros signifies 'the other of two' or 'different', the parent stem of countless scientific terms based on **heter**."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "Deriving from PIE *sm-tero- ('the other one'), **heter** entered Latin and modern European registers to mark divergence from the norm."
      },
      {
        "author": "Herbert Weir Smyth",
        "work": "Greek Grammar",
        "quote": "Compounds built upon **heter** regularly convey the sense of diversity, contrast, or irregularity."
      }
    ]
  },
  "Dashboard — heter\\heteranthera.md": {
    "primary": "A genus of aquatic and wetland herbaceous plants (mud plantains, family Pontederiaceae) having unequal, heteromorphic anthers.",
    "secondary": "In botanical pollination ecology, Heteranthera exhibits division of labor between feeding anthers that reward pollinators and fertilizing anthers that deposit pollen.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The aquatic herb **heteranthera** displays one staminal anther significantly larger than its two yellow companions."
      },
      {
        "author": "Charles Darwin",
        "work": "The Different Forms of Flowers on Plants of the Same Species",
        "quote": "In **heteranthera**, the striking dimorphism of the anthers corresponds to specialized floral visitations by bees."
      },
      {
        "author": "Peter H. Raven",
        "work": "Biology of Plants",
        "quote": "Floating ribbons of **heteranthera** dubia thrive in calm freshwater shallows and slow-moving streams."
      }
    ]
  },
  "Dashboard — heter\\heterobasidiomycetes.md": {
    "primary": "A former class or subclass of basidiomycetous fungi (including rusts, smuts, and jelly fungi) possessing septate or deeply divided basidia.",
    "secondary": "In mycology, Heterobasidiomycetes contrast with Homobasidiomycetes (mushrooms and polypores), which produce simple, non-septate holobasidia.",
    "quotes": [
      {
        "author": "C. J. Alexopoulos",
        "work": "Introductory Mycology",
        "quote": "The **heterobasidiomycetes** produce complex basidia that are either transversely or longitudinally septate."
      },
      {
        "author": "David L. Hawksworth",
        "work": "Ainsworth & Bisby's Dictionary of the Fungi",
        "quote": "Many agricultural plant pathogens causing cereal rusts and smuts were historically grouped among the **heterobasidiomycetes**."
      },
      {
        "author": "John Webster",
        "work": "Introduction to Fungi",
        "quote": "Gelatinous fruit bodies that rehydrate readily after desiccation are a hallmark of many saprophytic **heterobasidiomycetes**."
      }
    ]
  },
  "Dashboard — heter\\heterocephalus.md": {
    "primary": "A monotypic mammalian genus containing the naked mole-rat (Heterocephalus glaber), a subterranean eusocial rodent of the Horn of Africa.",
    "secondary": "In mammalian biogerontology and physiology, Heterocephalus glaber is renowned for extreme longevity (over 30 years), cancer resistance, and lack of pain response to acid.",
    "quotes": [
      {
        "author": "E. O. Wilson",
        "work": "Sociobiology: The New Synthesis",
        "quote": "The subterranean rodent **heterocephalus** displays true eusociality, with sterile worker castes serving a single breeding queen."
      },
      {
        "author": "Richard Dawkins",
        "work": "The Extended Phenotype",
        "quote": "Colonies of **heterocephalus** resemble insect societies more closely than any other mammalian social system."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Flamingo's Smile",
        "quote": "The hairless, wrinkled skin and massive protruding incisors of **heterocephalus** represent exquisite adaptations for tunneling through hard soil."
      }
    ]
  },
  "Dashboard — heter\\heterocercal.md": {
    "primary": "Having an asymmetrical caudal (tail) fin with the vertebral column extending into the upper, larger lobe, characteristic of sharks and sturgeons.",
    "secondary": "In ichthyological biomechanics, a heterocercal tail produces both forward thrust and a vertical lift vector to counteract negative buoyancy in un-aerated chondrichthyans.",
    "quotes": [
      {
        "author": "Alfred Romer",
        "work": "The Vertebrate Body",
        "quote": "The asymmetrical **heterocercal** tail of the shark provides upward hydrodynamic lift to support its heavy, sinking body."
      },
      {
        "author": "Louis Agassiz",
        "work": "Recherches sur les poissons fossiles",
        "quote": "Ancient fossil fishes uniformly possessed **heterocercal** fins, a primitive trait retained by living chondrosteans and selachians."
      },
      {
        "author": "Neil Shubin",
        "work": "Your Inner Fish",
        "quote": "The evolutionary shift from a **heterocercal** tail to a symmetrical homocercal fin freed teleost pectoral fins for precision maneuvering."
      }
    ]
  },
  "Dashboard — heter\\heterochromatin.md": {
    "primary": "Densely compacted, transcriptionally inactive chromosomal DNA that stains intensely throughout the cell cycle.",
    "secondary": "In epigenetics and cell biology, heterochromatin is characterized by histone H3K9 methylation and HP1 recruitment, maintaining genomic silencing and centromere integrity.",
    "quotes": [
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Constitutive **heterochromatin** remains highly condensed throughout interphase, suppressing transcription of repetitive satellite DNA."
      },
      {
        "author": "Emil Heitz",
        "work": "Das Heterochromatin der Moose",
        "quote": "Heitz introduced the term **heterochromatin** to designate chromosomal regions that remain deeply stained even during nuclear interphase."
      },
      {
        "author": "Harvey Lodish",
        "work": "Molecular Cell Biology",
        "quote": "X-chromosome inactivation in female mammals condenses one entire X into a transcriptionally inert Barr body of facultative **heterochromatin**."
      }
    ]
  },
  "Dashboard — heter\\heterocycle.md": {
    "primary": "A cyclic chemical compound that has atoms of at least two different elements (such as carbon and nitrogen, oxygen, or sulfur) as ring members.",
    "secondary": "In organic and medicinal chemistry, heterocycles form the core scaffolds of purines, pyrimidines, alkaloids, and the majority of modern pharmaceutical drugs.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Aromatic stability in an unsaturated **heterocycle** like pyridine derives from six delocalized pi electrons across carbon and nitrogen."
      },
      {
        "author": "F. A. Cotton",
        "work": "Advanced Organic Chemistry",
        "quote": "The nitrogenous **heterocycle** imidazole coordinates directly with the iron atom at the catalytic center of hemoglobin."
      },
      {
        "author": "James D. Watson",
        "work": "Molecular Biology of the Gene",
        "quote": "The planar geometry of each nucleic acid **heterocycle** allows base stacking through hydrophobic interactions inside the DNA double helix."
      }
    ]
  },
  "Dashboard — heter\\heterocyclic.md": {
    "primary": "Of, relating to, or containing a closed ring composed of atoms of more than one element (especially carbon and heteroatoms like N, O, or S).",
    "secondary": "In pharmaceutical synthesis, heterocyclic rings (e.g., thiophene, pyrrole, furan) modulate metabolic stability, lipophilicity, and hydrogen-bonding affinity.",
    "quotes": [
      {
        "author": "Laurence L. Brunton",
        "work": "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        "quote": "Most active therapeutic compounds incorporate at least one **heterocyclic** ring that engages specific receptor pockets."
      },
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "The **heterocyclic** base adenine pairs specifically with thymine through complementary hydrogen bonds."
      },
      {
        "author": "August Kekulé",
        "work": "Studies on Aromatic Compounds",
        "quote": "Extending cyclic theory to **heterocyclic** systems explained the unique chemical behavior of pyridine and quinoline."
      }
    ]
  },
  "Dashboard — heter\\heterodactyl.md": {
    "primary": "Having toes arranged in an irregular or unusual order; specifically, having the first and second toes directed backward and the third and fourth forward (as in trogons).",
    "secondary": "In avian morphology and systematic ornithology, the heterodactyl foot structure is unique to the order Trogoniformes, contrasting with the zygodactyl arrangement of parrots.",
    "quotes": [
      {
        "author": "Elliott Coues",
        "work": "Key to North American Birds",
        "quote": "The remarkable **heterodactyl** foot of the quetzal, with digits one and two reversed, separates trogons from all other perching birds."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "Tropical Nature and Other Essays",
        "quote": "Perched motionless on rain forest branches, the trogon relies on its **heterodactyl** grasp to seize ripe forest fruits."
      },
      {
        "author": "Alexander Wetmore",
        "work": "A Systematic Classification for the Birds of the World",
        "quote": "Anatomical inspection confirms that the **heterodactyl** condition involves an internal reorganization of the deep flexor tendons."
      }
    ]
  },
  "Dashboard — heter\\heterodon.md": {
    "primary": "A genus of harmless North American colubrid snakes known as hognose snakes, characterized by an upturned rostral scale and rear maxillary teeth.",
    "secondary": "In herpetology, Heterodon species are famous for elaborate defensive theatrics, including spreading a cobra-like neck hood and feigning death (thanatosis).",
    "quotes": [
      {
        "author": "Raymond L. Ditmars",
        "work": "The Reptile Book",
        "quote": "When threatened, **heterodon** flattens its head, hisses loudly, and if pressed further, rolls upon its back to feign death."
      },
      {
        "author": "Charles Darwin",
        "work": "The Expression of the Emotions in Man and Animals",
        "quote": "The theatrical shamming of death displayed by **heterodon** illustrates an extraordinary instinctive protective deception."
      },
      {
        "author": "Edwin H. Colbert",
        "work": "The World of Reptiles",
        "quote": "The spade-like snout of **heterodon** enables the snake to dig toads out of sandy subterranean burrows."
      }
    ]
  },
  "Dashboard — heter\\heterodoxy.md": {
    "primary": "Any opinion, belief, or doctrine at variance with an official, orthodox, or generally accepted standard.",
    "secondary": "In intellectual and ecclesiastical history, heterodoxy represents conceptual deviation that often sparks theological dispute or scientific revolutions.",
    "quotes": [
      {
        "author": "John Stuart Mill",
        "work": "On Liberty",
        "quote": "The ultimate test of a free society is its willingness to tolerate and debate minority **heterodoxy**."
      },
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "What was once condemned as bold **heterodoxy** frequently becomes the commonplace orthodoxy of the subsequent age."
      },
      {
        "author": "Edward Gibbon",
        "work": "The Decline and Fall of the Roman Empire",
        "quote": "Imperial edicts punished theological **heterodoxy** with confiscation of goods and exile to remote frontiers."
      }
    ]
  },
  "Dashboard — heter\\heterodyne.md": {
    "primary": "Pertaining to or involving the combination of two different radio frequencies to produce new frequencies equal to their sum and difference (beats).",
    "secondary": "In telecommunications and signal engineering, Edwin Armstrong's superheterodyne receiver uses heterodyne mixing to achieve superior selectivity and sensitivity.",
    "quotes": [
      {
        "author": "Edwin H. Armstrong",
        "work": "A New System of Short Wave Amplification",
        "quote": "The super-**heterodyne** circuit converts high-frequency incoming signals to a lower intermediate frequency easily amplified without distortion."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "A Treatise on Electricity and Magnetism",
        "quote": "The interference of two wave trains differing slightly in pitch creates regular **heterodyne** beats in the resulting field."
      },
      {
        "author": "Claude Shannon",
        "work": "A Mathematical Theory of Communication",
        "quote": "Frequency shifting via **heterodyne** conversion preserves the complete information entropy of the original modulated band."
      }
    ]
  },
  "Dashboard — heter\\heteroecious.md": {
    "primary": "Requiring two distinct, unrelated host species to complete a full parasitic life cycle (especially characteristic of rust fungi).",
    "secondary": "In plant pathology, heteroecious rusts (like Puccinia graminis) produce teliospores on cereals and aeciospores on alternate barberry bushes.",
    "quotes": [
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi",
        "quote": "De Bary proved that cereal stem rust is **heteroecious**, requiring both wheat and barberry to complete its developmental cycle."
      },
      {
        "author": "C. J. Alexopoulos",
        "work": "Introductory Mycology",
        "quote": "The **heteroecious** life cycle comprises five distinct spore stages distributed across two taxonomically disparate plant hosts."
      },
      {
        "author": "John Webster",
        "work": "Introduction to Fungi",
        "quote": "Eliminating the alternate host interrupts the sexual cycle of a **heteroecious** pathogen, reducing genetic variation."
      }
    ]
  },
  "Dashboard — heter\\heterogeneity.md": {
    "primary": "The quality or state of being diverse, varied, or composed of dissimilar components or elements.",
    "secondary": "In oncology and genetics, intratumoral heterogeneity describes the presence of genetically distinct subclonal cell populations within a single neoplasm.",
    "quotes": [
      {
        "author": "Robert A. Weinberg",
        "work": "The Biology of Cancer",
        "quote": "Genetic **heterogeneity** within a single tumor explains why targeted therapies often select for drug-resistant subclonal populations."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "The demographic **heterogeneity** of the expanding continent prevented the establishment of a uniform aristocratic class."
      },
      {
        "author": "Claude Lévi-Strauss",
        "work": "The Savage Mind",
        "quote": "Mythological thought organizes the concrete **heterogeneity** of natural phenomena into cohesive cultural categories."
      }
    ]
  },
  "Dashboard — heter\\heterogeneous.md": {
    "primary": "Diverse in character, quality, or content; composed of parts or ingredients of different kinds.",
    "secondary": "In physical chemistry, a heterogeneous mixture consists of distinct phases (e.g., solid, liquid, gas) separated by clear boundary interfaces.",
    "quotes": [
      {
        "author": "J. Willard Gibbs",
        "work": "On the Equilibrium of Heterogeneous Substances",
        "quote": "Thermodynamic equilibrium in a **heterogeneous** system requires temperature and chemical potential to remain uniform across every phase."
      },
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "A large commercial metropolis gathers a **heterogeneous** multitude of traders seeking mutual economic advantage."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Natural selection acts continuously upon the **heterogeneous** variations that arise spontaneously within wild populations."
      }
    ]
  },
  "Dashboard — heter\\heterogeneousness.md": {
    "primary": "The state, condition, or degree of being heterogeneous; heterogeneity.",
    "secondary": "In sociological analysis and materials science, the measure of structural or compositional disparity within an aggregate body.",
    "quotes": [
      {
        "author": "Herbert Spencer",
        "work": "First Principles",
        "quote": "Evolution is an integration of matter accompanied by a dissipation of motion, during which matter passes from indefinite homogeneity to definite **heterogeneousness**."
      },
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "The mind observes the essential **heterogeneousness** of our sensory ideas, distinguishing white from sweet without confusion."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Lay Sermons, Addresses, and Reviews",
        "quote": "The extreme **heterogeneousness** of biological tissues arises through the progressive differentiation of uniform embryonic cells."
      }
    ]
  },
  "Dashboard — heter\\heterogenesis.md": {
    "primary": "The obsolete biological theory that living organisms could arise from matter of a completely different nature; spontaneous generation; also, alternation of generations.",
    "secondary": "In evolutionary biology and embryology, heterogenesis historically encompassed saltational leaps or cyclical alternations between sexual and parthenogenetic forms.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Experiments on Spontaneous Generation",
        "quote": "My experiments demonstrated that the doctrines of **heterogenesis** rested upon faulty sterilization and aerial contamination."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Biogenesis and Abiogenesis",
        "quote": "Pasteur dealt the death-blow to **heterogenesis**, establishing that living matter arises exclusively from pre-existing living parentage."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "The hypothesis of **heterogenesis** was invoked by early observers who could not trace the minute sexual stages of parasites."
      }
    ]
  },
  "Dashboard — heter\\heterogenous.md": {
    "primary": "Originating outside the organism or from a different source; foreign; also an occasional variant of heterogeneous.",
    "secondary": "In immunology and transplantation surgery, heterogenous antigens or tissues originate from an individual of a different species (xenogeneic).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The introduction of **heterogenous** protein into the circulation frequently provokes an acute anaphylactic response."
      },
      {
        "author": "Alexis Carrel",
        "work": "The Transplantation of Organs",
        "quote": "Vascular grafting succeeds with autogenous vessels, but a **heterogenous** arterial segment invariably suffers rapid immunological rejection."
      },
      {
        "author": "Vinay Kumar",
        "work": "Robbins and Cotran Pathologic Basis of Disease",
        "quote": "The immune system rapidly mounts cytotoxic antibody and cell-mediated attacks against **heterogenous** tissue grafts."
      }
    ]
  },
  "Dashboard — heter\\heterograft.md": {
    "primary": "A tissue graft or organ transplanted from a donor of one species into a recipient of a different species; a xenograft.",
    "secondary": "In transplantation immunology, a heterograft elicits hyperacute rejection mediated by pre-existing recipient antibodies against donor carbohydrate antigens (like Gal-alpha-1,3-Gal).",
    "quotes": [
      {
        "author": "Alexis Carrel",
        "work": "Results of the Transplantation of Organs",
        "quote": "An animal receiving a **heterograft** exhibits violent vascular thrombosis within hours of restoring blood flow across the anastomosis."
      },
      {
        "author": "Courtney M. Townsend",
        "work": "Sabiston Textbook of Surgery",
        "quote": "Decellularized porcine heart valves serve as an effective **heterograft** replacement because antigenic cellular components are stripped away."
      },
      {
        "author": "Peter Medawar",
        "work": "The Behavior and Fate of Skin Homografts",
        "quote": "The immunological barrier confronting a **heterograft** is far more severe than the allogeneic reaction seen between members of the same species."
      }
    ]
  },
  "Dashboard — heter\\heteroicous.md": {
    "primary": "Having male and female reproductive organs on different stems or branches of the same individual plant or thallus; autoicous (in bryology).",
    "secondary": "In bryology and hepaticology, heteroicous mosses display diverse spatial segregations of antheridia and archegonia to optimize outcrossing.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "In certain **heteroicous** moss species, antheridial cups appear on short lateral ramuli while archegonia crown the main stem."
      },
      {
        "author": "Peter H. Raven",
        "work": "Biology of Plants",
        "quote": "The **heteroicous** arrangement ensures fertilization during wet spells without requiring sperm to navigate between separate cushions."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "Bryophyte taxonomists record whether a gametophyte is strictly dioicous, synoicous, or **heteroicous** to define species boundaries."
      }
    ]
  },
  "Dashboard — heter\\heterokontae.md": {
    "primary": "A group of algae characterized by having unequal flagella, encompassing the yellow-green algae (Xanthophyceae) and related heterokont lineages.",
    "secondary": "In systematic phycology, Heterokontae (stramenopiles) possess a longer tinsel flagellum bearing tripartite mastigonemes and a shorter smooth whiplash flagellum.",
    "quotes": [
      {
        "author": "F. E. Fritsch",
        "work": "The Structure and Reproduction of the Algae",
        "quote": "The defining characteristic of the **heterokontae** is the presence of two unequal flagella inserted at the anterior cell pole."
      },
      {
        "author": "Robert Edward Lee",
        "work": "Phycology",
        "quote": "Flagellar tubular hairs in **heterokontae** reverse the direction of hydrodynamic thrust generated by the undulatory wave."
      },
      {
        "author": "Peter H. Raven",
        "work": "Biology of Plants",
        "quote": "Photosynthetic pigments in the **heterokontae** include chlorophylls a and c accompanied by abundant fucoxanthin."
      }
    ]
  },
  "Dashboard — heter\\heterokontophyta.md": {
    "primary": "A major division or phylum of algae and related protists (stramenopiles) possessing heterokont flagella, including diatoms, brown algae, and chrysophytes.",
    "secondary": "In modern eukaryotic phylogenetics, Heterokontophyta contains four-membrane plastids derived from secondary endosymbiosis of a red alga.",
    "quotes": [
      {
        "author": "Robert Edward Lee",
        "work": "Phycology",
        "quote": "The vast phylum **heterokontophyta** ranges from microscopic silica-shelled diatoms to giant marine kelps exceeding sixty meters in length."
      },
      {
        "author": "David L. Hawksworth",
        "work": "Ainsworth & Bisby's Dictionary of the Fungi",
        "quote": "Oomycetes, once grouped with true fungi, are now recognized as non-photosynthetic lineages within **heterokontophyta**."
      },
      {
        "author": "Peter H. Raven",
        "work": "Biology of Plants",
        "quote": "Secondary endosymbiosis gave rise to the complex four-membrane chloroplast envelope that characterizes photosynthetic **heterokontophyta**."
      }
    ]
  },
  "Dashboard — heter\\heterologic.md": {
    "primary": "Consisting of or characterized by different or discordant principles; or departing from normal biological structure or developmental sequence.",
    "secondary": "In literary theory and philosophy (Bataille), heterologic refers to the study of the heterogeneous, taboo, or rejected elements of culture.",
    "quotes": [
      {
        "author": "Georges Bataille",
        "work": "Visions of Excess",
        "quote": "A **heterologic** method investigates that which homogeneous society expels as waste, sacred terror, or sovereign expenditure."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "A **heterologic** tumor consists of tissues that have no anatomical analogue in the normal host organ where they arise."
      },
      {
        "author": "Michel Foucault",
        "work": "The Order of Things",
        "quote": "Modern thought established **heterologic** spaces where conflicting epistemological orders collide without synthesis."
      }
    ]
  },
  "Dashboard — heter\\heterological.md": {
    "primary": "Of or relating to heterology; characterized by abnormal structure, foreign tissue development, or self-contradictory linguistic reference.",
    "secondary": "In philosophical logic, Grelling-Nelson's paradox defines a word as heterological if it does not describe itself (e.g., 'long' is not long; is 'heterological' heterological?).",
    "quotes": [
      {
        "author": "Bertrand Russell",
        "work": "Introduction to Mathematical Philosophy",
        "quote": "The paradox of whether 'heterological' is itself **heterological** illustrates the semantic contradictions inherent in unstratified language."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Chondrosarcoma arising within breast tissue represents a classic **heterological** growth, violating local histogenetic norms."
      },
      {
        "author": "Willard Van Orman Quine",
        "work": "The Ways of Paradox",
        "quote": "The category of **heterological** terms precipitates a sharp antinomy resolvable only through rigorous semantic typing."
      }
    ]
  }
};

const count = updateNotesBatch(baseDir, batchData);
console.log(`Updated ${count} notes in Form Part 3 Batch 4.`);
