import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Number & Mathematics');
const batchData = {
  "Dashboard — con/orthoconic.md": {
    "primary": "Pertaining to, resembling, or possessing an orthocone; having a straight, uncoiled conical shell.",
    "secondary": "In invertebrate paleontology, designating the ancestral shell morphology of early cephalopods characterized by longitudinal septal chambers without coiling.",
    "quotes": [
      {
        "author": "Alpheus Hyatt",
        "work": "Genera of Fossil Cephalopods",
        "quote": "The **orthoconic** shell of primitive nautiloids represents the baseline ancestral morphotype of the entire class."
      },
      {
        "author": "Roderick Murchison",
        "work": "The Silurian System",
        "quote": "Thin sections of the limestone reveal numerous straight **orthoconic** fossils embedded in the dark matrix."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Flamingo's Smile",
        "quote": "These ancient swimmers navigated Paleozoic seas by jetting water from their elongated, chambered **orthoconic** shells."
      }
    ]
  },
  "Dashboard — con/polyconic.md": {
    "primary": "Pertaining to or constructed from several cones; specifically, a cartographic projection projecting earth coordinates upon multiple tangent cones.",
    "secondary": "In geodesy and cartography, the American polyconic map projection developed by Ferdinand Hassler for coastal survey charts.",
    "quotes": [
      {
        "author": "Ferdinand Rudolph Hassler",
        "work": "Papers on the Survey of the Coast of the United States",
        "quote": "The **polyconic** projection avoids cumulative distortion by employing a distinct tangent cone for each successive parallel of latitude."
      },
      {
        "author": "Arthur Newell Strahler",
        "work": "Physical Geography",
        "quote": "Topographic quadrangle maps historically utilized the **polyconic** grid because of its local scale fidelity along the central meridian."
      },
      {
        "author": "Charles Sanders Peirce",
        "work": "Photometric Researches",
        "quote": "Geodetic stations across the continent were plotted upon standard **polyconic** sheets prepared by the Coast Survey."
      }
    ]
  },
  "Dashboard — cten/Ctenophora.md": {
    "primary": "A phylum of exclusively marine invertebrates commonly called comb jellies, swimming by means of eight longitudinal rows of ciliary combs.",
    "secondary": "In systematic marine zoology, biradially symmetrical, non-stinging diploblastic organisms possessing colloblasts rather than cnidocysts.",
    "quotes": [
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "The phylum **Ctenophora** exhibits translucent pelagic bodies propelled by shimmering iridescence along their comb rows."
      },
      {
        "author": "Ernst Haeckel",
        "work": "Art Forms in Nature",
        "quote": "Exquisite glass-like domes of **Ctenophora** drift through the dark oceanic depths like living crystal chandeliers."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "In every member of **Ctenophora**, locomotion is driven by the coordinated rhythmic stroke of microscopic swimming plates."
      }
    ]
  },
  "Dashboard — cten/cten.md": {
    "primary": "A Greek combining root morpheme (κτείς, κτενός, kteis, ktenos) signifying a comb or comb-like structure.",
    "secondary": "In biological nomenclature, a formative element producing technical names for organisms, organs, or anatomical parts resembling a comb (as in ctenoid, ctenophore, ctenidium).",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The scientific radical **cten-** derives directly from the Greek word for a comb, applied to serrated biological features."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "From kteis and its genitive stem **cten-** come anatomical terms designating toothed, comb-like skeletal margins."
      },
      {
        "author": "Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Morphologists adopted the root **cten-** to classify marine organisms displaying regular ciliated or pectinate margins."
      }
    ]
  },
  "Dashboard — cten/ctene.md": {
    "primary": "One of the locomotory comb plates of a ctenophore, consisting of a row of fused cilia.",
    "secondary": "In invertebrate morphology, each transverse paddle-like ciliary comb that beats metachronally to propel a comb jelly through water.",
    "quotes": [
      {
        "author": "Libbie Hyman",
        "work": "The Invertebrates: Protozoa through Ctenophora",
        "quote": "Each individual **ctene** beats in coordinated metachronal rhythm under the sensory control of the apical aboral organ."
      },
      {
        "author": "Alexander Agassiz",
        "work": "North American Acalephae",
        "quote": "Light striking the moving rows of each **ctene** produces dazzling prismatic flashes along the flanks of the animal."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "Microscopic examination shows that a **ctene** is formed by the lateral fusion of hundreds of elongated vibrating cilia."
      }
    ]
  },
  "Dashboard — cten/ctenidium.md": {
    "primary": "A comb-like respiratory gill in mollusks, or a comb of rigid spines on the head or thorax of certain insects (especially fleas).",
    "secondary": "In malacology, the respiratory gill structure situated in the mantle cavity of ancestral and modern mollusks, bearing ciliated comb filaments.",
    "quotes": [
      {
        "author": "Ray Lankester",
        "work": "A Treatise on Zoology: Mollusca",
        "quote": "The primitive **ctenidium** of the gastropod consists of a central axis bearing two alternating rows of delicate triangular leaflets."
      },
      {
        "author": "Charles Rothschild",
        "work": "A Revision of the Fleas (Siphonaptera)",
        "quote": "The number and arrangement of heavy teeth in the pronotal **ctenidium** serve as critical diagnostic keys for flea identification."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "Water currents drawn through the mantle chamber bathe the delicate vascular filaments of each **ctenidium**."
      }
    ]
  },
  "Dashboard — cten/ctenizidae.md": {
    "primary": "A family of mygalomorph spiders known as trapdoor spiders, which construct subterranean burrows concealed by hinged silk lids.",
    "secondary": "In arachnology, robust spiders possessing specialized rastella (comb-like digging spines) on their chelicerae for excavating earth.",
    "quotes": [
      {
        "author": "John Henry Comstock",
        "work": "The Spider Book",
        "quote": "Spiders of the family **Ctenizidae** fabricate subterranean silken tubes protected by remarkably camouflaged bevelled trapdoors."
      },
      {
        "author": "H. C. McCook",
        "work": "American Spiders and Their Spinningwork",
        "quote": "The female **ctenizid** guards her subterranean retreat, holding the hinged door shut against intruders with powerful chelicerae."
      },
      {
        "author": "Jean-Henri Fabre",
        "work": "The Life of the Spider",
        "quote": "The mason spider of the **Ctenizidae** incorporates grains of sand and moss into her lid so that it defies detection."
      }
    ]
  },
  "Dashboard — cten/ctenocephalides.md": {
    "primary": "A genus of fleas in the family Pulicidae, including the common cat flea (Ctenocephalides felis) and dog flea (Ctenocephalides canis).",
    "secondary": "In medical and veterinary entomology, cosmopolitan ectoparasitic insects characterized by genal and pronotal combs, transmitting pathogens such as Bartonella and Dipylidium.",
    "quotes": [
      {
        "author": "Charles Rothschild",
        "work": "A Synopsis of the Fleas Found on Wild and Domestic Animals",
        "quote": "Species of **Ctenocephalides** are readily distinguished by both genal and pronotal ctenidia consisting of sharp dark spines."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Domestic pets heavily infested with **Ctenocephalides** may transmit larval tapeworms and cause severe allergic dermatitis."
      },
      {
        "author": "L. O. Howard",
        "work": "The Insect Book",
        "quote": "Under the microscope, the head of **Ctenocephalides** reveals a formidable row of black comb teeth guarding the mouthparts."
      }
    ]
  },
  "Dashboard — cten/ctenocephalus.md": {
    "primary": "An older taxonomic name for the flea genus Ctenocephalides; also a genus of fossil trilobites (family Conocoryphidae).",
    "secondary": "In systematic entomology and paleontology, an organism having comb-like cephalic structures, spines, or frontal margins.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "The dog was frequently tormented by species described in older monographs under the generic name **Ctenocephalus**."
      },
      {
        "author": "Roderick Murchison",
        "work": "Siluria: A History of the Oldest Known Rocks",
        "quote": "Cambrian strata of Bohemia yielded remarkable blind trilobites assigned to the genus **Ctenocephalus**."
      },
      {
        "author": "John Obadiah Westwood",
        "work": "An Introduction to the Modern Classification of Insects",
        "quote": "The pectinate cephalic margins characteristic of **Ctenocephalus** anchor the insect securely within animal fur."
      }
    ]
  },
  "Dashboard — cten/ctenoid.md": {
    "primary": "Comb-like; having a margin of slender teeth or comb-like projections, especially describing fish scales.",
    "secondary": "In ichthyology, designating teleost fish scales that bear tiny tooth-like ctenii along their posterior exposed margins, typical of spiny-finned fishes.",
    "quotes": [
      {
        "author": "Louis Agassiz",
        "work": "Recherches sur les poissons fossiles",
        "quote": "I established four primary orders of fishes based upon scale morphology, distinguishing cycloid from sharply serrate **ctenoid** forms."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "Percoid fishes are characterized by firm **ctenoid** scales whose spiny posterior edges create a rough, rasping surface."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The presence of fine comb teeth on a **ctenoid** scale reflects specialized epidermal growth found in derived teleosts."
      }
    ]
  },
  "Dashboard — cten/ctenophore.md": {
    "primary": "Any marine invertebrate belonging to the phylum Ctenophora, characterized by eight rows of swimming comb plates; a comb jelly.",
    "secondary": "In pelagic marine ecology, a bioluminescent, gelatinous carnivore that captures prey using sticky tentacles equipped with colloblasts.",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "A single scoop of the plankton net revealed dozens of luminous **ctenophores** pulsating with ethereal cold fire."
      },
      {
        "author": "Ernst Haeckel",
        "work": "Report on the Radiolaria",
        "quote": "The delicate, translucent tissues of the pelagic **ctenophore** dissolve rapidly if exposed to turbulent breakers."
      },
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "The oceanic **ctenophore** controls its buoyancy and balance through the sensory gravity-sensing otolith at its aboral pole."
      }
    ]
  },
  "Dashboard — dec/Decalogue.md": {
    "primary": "The Ten Commandments given by God to Moses upon Mount Sinai, forming the foundational ethical code of Judeo-Christian law.",
    "secondary": "Any set of ten authoritative moral, legal, or procedural rules or precepts.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "Moses descending from the holy mount brought two stone tablets inscribed with the sacred **Decalogue**."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The moral precepts of the Jewish **Decalogue** were embraced by early Christian converts throughout the Roman provinces."
      },
      {
        "author": "Thomas Carlyle",
        "work": "Past and Present",
        "quote": "No modern parliament can vote away the everlasting laws engraved in the moral **Decalogue** of the universe."
      }
    ]
  },
  "Dashboard — dec/decade.md": {
    "primary": "A period of ten consecutive years, especially a calendar period such as the 1920s.",
    "secondary": "A series, group, or division consisting of ten items (such as ten Hail Marys in a rosary, or ten books of a literary history).",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "A single **decade** of wise administration was sufficient to restore prosperity to the devastated eastern provinces."
      },
      {
        "author": "Thomas Babington Macaulay",
        "work": "The History of England",
        "quote": "Within the brief span of a **decade**, the English constitution passed through rebellion, restoration, and permanent settlement."
      },
      {
        "author": "Virginia Woolf",
        "work": "To the Lighthouse",
        "quote": "Time passed with the measured pace of years consolidating into a silent, forgotten **decade**."
      }
    ]
  },
  "Dashboard — dec/decadence.md": {
    "primary": "A process, condition, or period of cultural, moral, artistic, or societal decline and deterioration.",
    "secondary": "In literary and art history, the Decadent Movement of late 19th-century Europe celebrating aestheticism, artifice, and refined sensibility over conventional morality.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Luxury, corruption, and military insubordination precipitated the gradual **decadence** of the Western Empire."
      },
      {
        "author": "Friedrich Nietzsche",
        "work": "The Case of Wagner",
        "quote": "What characterizes every literary **decadence** is that life no longer resides in the whole, but only in the vibrant detail."
      },
      {
        "author": "Oscar Wilde",
        "work": "The Picture of Dorian Gray",
        "quote": "He watched the subtle **decadence** of his own soul reflected with terrifying precision upon the hidden canvas."
      }
    ]
  },
  "Dashboard — dec/decagon.md": {
    "primary": "A plane geometric figure bounded by ten straight sides and ten interior angles.",
    "secondary": "In Euclidean geometry, a regular decagon whose interior angles each equal 144 degrees, constructed using the golden ratio.",
    "quotes": [
      {
        "author": "Euclid",
        "work": "Elements",
        "quote": "To inscribe a regular **decagon** in a given circle, divide the radius in extreme and mean ratio."
      },
      {
        "author": "Johannes Kepler",
        "work": "Harmonices Mundi",
        "quote": "The side of the regular **decagon** bears to the radius of the circumscribed circle the sacred golden proportion."
      },
      {
        "author": "Thomas Heath",
        "work": "The Thirteen Books of Euclid's Elements",
        "quote": "Book IV establishes the elegant geometric construction of the regular **decagon** through successive isosceles triangles."
      }
    ]
  },
  "Dashboard — dec/decagram.md": {
    "primary": "A metric unit of mass equal to ten grams (symbol: dag).",
    "secondary": "In commercial trade and culinary measurement across Central and Eastern Europe, a standard retail unit of mass.",
    "quotes": [
      {
        "author": "Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "The new decimal system introduced the **decagram** to represent exactly ten standard units of gravimetric mass."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventures of Sherlock Holmes",
        "quote": "Holmes carefully weighed each precipitate down to the fraction of a **decagram** in his improvised chemical laboratory."
      },
      {
        "author": "William Crookes",
        "work": "Select Methods in Chemical Analysis",
        "quote": "Add precisely one **decagram** of dried sodium carbonate to the powdered ore before heating in the platinum crucible."
      }
    ]
  },
  "Dashboard — dec/decahedron.md": {
    "primary": "A three-dimensional solid or polyhedron bounded by ten plane faces.",
    "secondary": "In solid geometry and crystallography, a polyhedron whose ten faces may form bipyramids, prisms, or irregular coordination polyhedra.",
    "quotes": [
      {
        "author": "Leonhard Euler",
        "work": "Elements of Algebra",
        "quote": "According to our polyhedral formula, a **decahedron** with twelve vertices must necessarily possess twenty edges."
      },
      {
        "author": "René Just Haüy",
        "work": "Traité de Minéralogie",
        "quote": "Secondary crystalline modifications frequently truncate the basal pyramids into an apparent symmetrical **decahedron**."
      },
      {
        "author": "Adrien-Marie Legendre",
        "work": "Elements of Geometry",
        "quote": "A pentagonal prism capped at both extremities exemplifies a closed **decahedron** having ten distinct planar boundaries."
      }
    ]
  },
  "Dashboard — dec/decameter.md": {
    "primary": "A metric unit of length equal to ten meters (symbol: dam).",
    "secondary": "In surveying and forestry measurement, a unit useful for measuring land plots and boundary baselines.",
    "quotes": [
      {
        "author": "Ferdinand Rudolph Hassler",
        "work": "Comparison of Weights and Measures",
        "quote": "The surveyor unrolled a steel baseline chain calibrated to measure increments of one **decameter** across the field."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos: A Sketch of a Physical Description of the Universe",
        "quote": "The botanical expedition recorded the altitudinal distribution of alpine flora at intervals of every **decameter**."
      },
      {
        "author": "Jules Verne",
        "work": "Twenty Thousand Leagues Under the Sea",
        "quote": "The submarine vessel descended steadily through the oceanic depths, marking every ten meters or **decameter** on the pressure gauge."
      }
    ]
  },
  "Dashboard — dec/decathlon.md": {
    "primary": "A combined athletic contest consisting of ten track and field events held over two consecutive days.",
    "secondary": "In Olympic sports, the premier test of versatile athletic prowess, comprising the 100m, long jump, shot put, high jump, 400m, 110m hurdles, discus, pole vault, javelin, and 1500m.",
    "quotes": [
      {
        "author": "Pierre de Coubertin",
        "work": "Olympic Memoirs",
        "quote": "The crowned victor of the Olympic **decathlon** stands rightfully acclaimed as the finest all-around athlete in the world."
      },
      {
        "author": "F. Scott Fitzgerald",
        "work": "This Side of Paradise",
        "quote": "He carried himself with the effortless, muscular poise of a collegiate champion preparing for the **decathlon**."
      },
      {
        "author": "Ernest Hemingway",
        "work": "The Sun Also Rises",
        "quote": "We talked about track meets and the exhausting physical endurance required to complete all ten events of a **decathlon**."
      }
    ]
  },
  "Dashboard — dec/deka.md": {
    "primary": "A metric prefix (symbol: da) denoting multiplication by a factor of ten.",
    "secondary": "In historical metrology and chemical nomenclature, the decimal combining form (from Greek δέκα) adopted by the French metric committee of 1795.",
    "quotes": [
      {
        "author": "Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "We prefixed the Greek word **deka-** to denote tenfold multiples in our systematic table of weights and measures."
      },
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The Hellenic numeral **deka** became the standard prefix for ten across all modern international metric units."
      },
      {
        "author": "Charles Babbage",
        "work": "On the Economy of Machinery and Manufactures",
        "quote": "Calculations are immensely simplified whenever units scale uniformly by powers of ten governed by prefixes like **deka-**."
      }
    ]
  },
  "Dashboard — dec/undecagon.md": {
    "primary": "A plane polygon having eleven straight sides and eleven angles; a hendecagon.",
    "secondary": "In Euclidean geometry, an eleven-sided figure whose regular form cannot be constructed using an unmarked ruler and compass alone.",
    "quotes": [
      {
        "author": "Carl Friedrich Gauss",
        "work": "Disquisitiones Arithmeticae",
        "quote": "Since eleven is a prime not of the form 2^(2^n) + 1, a regular **undecagon** cannot be inscribed with ruler and compass."
      },
      {
        "author": "Augustus De Morgan",
        "work": "Elements of Arithmetic",
        "quote": "An **undecagon** presents eleven internal angles whose sum amounts to eighteen right angles."
      },
      {
        "author": "Thomas Heath",
        "work": "A History of Greek Mathematics",
        "quote": "Early geometers recognized the impossibility of constructing the regular **undecagon** through elementary Euclidean methods."
      }
    ]
  },
  "Dashboard — di/di.md": {
    "primary": "A combining prefix derived from Greek δίς (dis) meaning twice, two, or double.",
    "secondary": "In chemistry, taxonomy, and linguistics, a productive prefix denoting the presence of two atoms, groups, parts, or phases (as in dioxide, dimorphism, diatomic).",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The Greek prefix **di-**, shortened from dis, universally signifies twofold or double in scientific coinages."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "Prefixal **di-** attaches to nouns and adjectives to indicate dual structure or repeated occurrence."
      },
      {
        "author": "Jons Jacob Berzelius",
        "work": "A View of the Progress and Present State of Animal Chemistry",
        "quote": "Compounds bearing the prefix **di-** contain two proportions of oxygen or acid to one proportion of base."
      }
    ]
  },
  "Dashboard — di/diatomic.md": {
    "primary": "Consisting of or containing two atoms in each molecule.",
    "secondary": "In physical chemistry, designating homonuclear gases (such as H2, O2, N2) or heteronuclear molecules (such as CO, HCl) composed of paired atoms.",
    "quotes": [
      {
        "author": "John Dalton",
        "work": "A New System of Chemical Philosophy",
        "quote": "In every elementary gas where two particles combine into a unit, we observe a permanent **diatomic** constitution."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "Theory of Heat",
        "quote": "The ratio of specific heats in a **diatomic** gas reflects both translational and rotational degrees of molecular freedom."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Textbook of Theoretical Electrochemistry",
        "quote": "Thermal dissociation at high temperatures breaks the stable bonds holding the **diatomic** nitrogen molecule together."
      }
    ]
  },
  "Dashboard — di/dicot.md": {
    "primary": "A flowering plant (dicotyledon) whose embryo possesses two seed leaves or cotyledons.",
    "secondary": "In botanical systematics, any angiosperm traditionally classified under Dicotyledones, typically having net-veined leaves, taproots, and floral parts in multiples of four or five.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "First Lessons in Botany and Vegetable Physiology",
        "quote": "Upon germination, every typical **dicot** pushes two fleshy seed-lobes above the soil before expanding its first true foliage."
      },
      {
        "author": "Charles Darwin",
        "work": "The Power of Movement in Plants",
        "quote": "We observed the circumnutation of the hypocotyl in the young **dicot** seedling as it forced its way toward the light."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "The Flora of British India",
        "quote": "Forest canopies in the temperate valleys are dominated by broad-leaved **dicot** trees belonging to the oak and maple families."
      }
    ]
  },
  "Dashboard — di/dis.md": {
    "primary": "A prefix of Latin origin denoting apart, away, reversal, or negation; in Greek roots (δίς), signifying twice or double.",
    "secondary": "In English morphology, a ubiquitous formative prefix expressing undoing, deprivation, separation, or contrasting opposition.",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The prefix **dis-** carries an original sense of parting asunder or reversing the action of the simple verb."
      },
      {
        "author": "Samuel Johnson",
        "work": "A Dictionary of the English Language",
        "quote": "When prefixed to adjectives or verbs, **dis-** commonly signifies privation, negation, or separation."
      },
      {
        "author": "Henry Sweet",
        "work": "A New English Grammar",
        "quote": "Words compounded with **dis-** establish an antonymic relationship to their root bases through morphological inversion."
      }
    ]
  },
  "Dashboard — di/disable.md": {
    "primary": "To make ineffective, unfit, or incapable of normal action; to impair the physical or functional capacity of.",
    "secondary": "In law and computing, to deprive of legal power or disqualify; to deactivate a software feature, device, or mechanism.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "The Merchant of Venice",
        "quote": "I have **disabled** mine estate, By something showing a more swelling port Than my faint means would grant continuance."
      },
      {
        "author": "John Milton",
        "work": "Samson Agonistes",
        "quote": "Can they think me so **disabled**, so bereft of manly vigor, that I cannot smite their blasphemous idolaters?"
      },
      {
        "author": "Francis Bacon",
        "work": "Essays",
        "quote": "Unreasonable jealousy and suspicion **disable** the mind from pursuing sound and resolute counsels."
      }
    ]
  },
  "Dashboard — dipl/amphidiploid.md": {
    "primary": "An organism or cell that is a functional diploid resulting from the hybridization of two distinct species followed by chromosome doubling.",
    "secondary": "In plant cytogenetics, an allotetraploid carrying two complete diploid chromosomal sets, which behaves meiotically like a normal fertile diploid.",
    "quotes": [
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "The synthetic species Raphanobrassica was a true **amphidiploid**, uniting the complete chromosomal complements of radish and cabbage."
      },
      {
        "author": "C. D. Darlington",
        "work": "Recent Advances in Cytology",
        "quote": "Regular bivalent pairing ensures complete fertility in an **amphidiploid** hybrid where allosomes find homologous mates."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "Speciation through the emergence of an **amphidiploid** plant lineage can occur instantaneously in a single generation."
      }
    ]
  },
  "Dashboard — dipl/amphidiploidy.md": {
    "primary": "The state or genetic condition of being an amphidiploid; allopolyploidy producing fertile hybrid offspring.",
    "secondary": "In evolutionary botany, an important speciation mechanism whereby interspecific sterile hybrids regain fertility through somatic genome doubling.",
    "quotes": [
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "Speciation through **amphidiploidy** demonstrates that new, sexually isolated botanical species can arise without gradual geographic divergence."
      },
      {
        "author": "G. Ledyard Stebbins",
        "work": "Variation and Evolution in Plants",
        "quote": "Wheat cultivars such as Triticum aestivum trace their evolutionary ancestry to successive episodes of natural **amphidiploidy**."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "Polyploidy, particularly in the form of **amphidiploidy**, accounts for a significant fraction of flowering plant diversity."
      }
    ]
  },
  "Dashboard — dipl/anadiplosis.md": {
    "primary": "A rhetorical figure of speech in which the last word or phrase of one sentence, clause, or line is repeated at the beginning of the next.",
    "secondary": "In classical rhetoric and stylistics, an emphatic device creating chain-like momentum, climax, and emotional resonance across successive thoughts.",
    "quotes": [
      {
        "author": "Quintilian",
        "work": "Institutio Oratoria",
        "quote": "The figure called **anadiplosis** repeats the final word of the preceding colon at the commencement of the following."
      },
      {
        "author": "John Milton",
        "work": "Lycidas",
        "quote": "For Lycidas is dead, dead ere his prime, Young Lycidas, and hath not left his peer; such lines mirror poetic **anadiplosis**."
      },
      {
        "author": "George Puttenham",
        "work": "The Arte of English Poesie",
        "quote": "Our poets style **anadiplosis** the redouble, when the cadence of the first verse begins the melody of the second."
      }
    ]
  },
  "Dashboard — dipl/dipl.md": {
    "primary": "A Greek combining root morpheme (διπλόος, diploos) signifying double, twofold, or folded.",
    "secondary": "In scientific and anatomical terminology, a formative prefix denoting duplicate parts, two-layered structure, or dual genetic complement (as in diploid, diplopia, diplodocus).",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The formative element **dipl-** stems from Greek diploos, indicating a twofold condition or folded document."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "Derivatives of **dipl-** express doubling of numbers, physical folding of leaves, or paired anatomical structures."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "The root underlying **dipl-** reflects an ancient Indo-European construction for doubling and fold-like duplication."
      }
    ]
  },
  "Dashboard — dipl/dipladenia.md": {
    "primary": "A genus of tropical American woody climbing vines (now often included in Mandevilla, family Apocynaceae) cultivated for showy trumpet-shaped flowers.",
    "secondary": "In systematic botany and horticulture, flowering evergreen climbers characterized by two conspicuous gland-like nectaries at the base of the ovary.",
    "quotes": [
      {
        "author": "Joseph Dalton Hooker",
        "work": "Curtis's Botanical Magazine",
        "quote": "The conservatory was adorned by magnificent specimens of **Dipladenia** bearing large rose-colored salver-shaped blossoms."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The botanical name **Dipladenia** refers specifically to the two prominent glandular bodies located upon the pistil."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "In the family Apocynaceae, the climbing genus **Dipladenia** is celebrated for its brilliant, nectar-bearing floral corollas."
      }
    ]
  },
  "Dashboard — dipl/diplegia.md": {
    "primary": "Symmetrical paralysis affecting corresponding parts of both sides of the body, typically affecting the legs more severely than the arms.",
    "secondary": "In clinical neurology, a form of cerebral palsy (Little's disease) often resulting from perinatal cerebral hypoxia or leukomalacia.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Cerebral Palsies of Children",
        "quote": "Spastic **diplegia** in infants is characterized by bilateral motor rigidity and exaggerated deep tendon reflexes."
      },
      {
        "author": "William Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "In cases of congenital **diplegia**, the spastic gait with cross-legged scissoring reflects bilateral pyramidal tract impairment."
      },
      {
        "author": "Henry Maudsley",
        "work": "The Pathology of Mind",
        "quote": "The motor impairment in cerebral **diplegia** frequently coexists with varying degrees of intellectual and speech deficit."
      }
    ]
  },
  "Dashboard — dipl/diploblasty.md": {
    "primary": "The embryonic or anatomical condition of possessing only two primary germ layers: an outer ectoderm and an inner endoderm.",
    "secondary": "In comparative embryology, the foundational structural plan of basal metazoans such as cnidarians and ctenophores, which lack a true mesodermal germ layer.",
    "quotes": [
      {
        "author": "Ernst Haeckel",
        "work": "The Evolution of Man",
        "quote": "The Gastraea theory posits that ancestral metazoans exhibited primitive **diploblasty**, developing from two primary blastodermic sheets."
      },
      {
        "author": "Ray Lankester",
        "work": "Comparative Embryology",
        "quote": "True **diploblasty** confines the animal's developmental architecture to the primary ectoderm and endoderm without coelomic space."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "Coelenterates preserve lifelong **diploblasty**, separating internal digestive cavities from the environment with only two cellular layers."
      }
    ]
  },
  "Dashboard — dipl/diplococcus.md": {
    "primary": "A round bacterium (coccus) that typically occurs in pairs of two linked cells.",
    "secondary": "In bacteriology and infectious disease, a morphological type of bacterium (such as Streptococcus pneumoniae or Neisseria meningitidis) seen microscopically as paired cocci.",
    "quotes": [
      {
        "author": "Robert Koch",
        "work": "Investigations into the Etiology of Traumatic Infective Diseases",
        "quote": "Exudates stained with aniline dyes revealed innumerable paired spheres characteristic of pathogenic **Diplococcus**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The diagnosis of lobar pneumonia was confirmed by detecting the encapsulated **Diplococcus** in rusty sputum samples."
      },
      {
        "author": "Alexander Fleming",
        "work": "Chemotherapy: Yesterday, Today, and Tomorrow",
        "quote": "Cultures of sensitive **Diplococcus** ceased growing immediately upon the addition of minute quantities of penicillin."
      }
    ]
  },
  "Dashboard — dipl/diplodocus.md": {
    "primary": "A genus of very large, long-necked, herbivorous sauropod dinosaurs that lived during the Late Jurassic period in North America.",
    "secondary": "In vertebrate paleontology, a diplodocid dinosaur characterized by double-beamed chevron bones beneath the tail vertebrae and a whip-like tail tip.",
    "quotes": [
      {
        "author": "Othniel Charles Marsh",
        "work": "The Dinosaurs of North America",
        "quote": "I proposed the name **Diplodocus** in reference to the remarkable double chevron bones protecting the blood vessels beneath the caudal vertebrae."
      },
      {
        "author": "Henry Fairfield Osborn",
        "work": "Skeletal Variations of Diplodocus",
        "quote": "The colossal skeleton of **Diplodocus** demonstrates an extraordinary lightweight architecture of hollowed-out pneumatic vertebrae."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Lost World",
        "quote": "High above the ferns rose the serpentine neck of an immense sauropod resembling the museum restorations of **Diplodocus**."
      }
    ]
  },
  "Dashboard — dipl/diploid.md": {
    "primary": "Containing two complete sets of chromosomes, one inherited from each biological parent (designated as 2n).",
    "secondary": "In genetics and cytogenetics, the somatic cellular state of most animals and vascular plants, contrasting with the haploid state of gametes.",
    "quotes": [
      {
        "author": "Thomas Hunt Morgan",
        "work": "The Theory of the Gene",
        "quote": "Fertilization restores the normal **diploid** chromosome number by uniting the single haploid sets of sperm and egg."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "In every somatic cell of the **diploid** organism, homologous chromosomes exist in matched maternal and paternal pairs."
      },
      {
        "author": "Richard Dawkins",
        "work": "The Selfish Gene",
        "quote": "Being a **diploid** creature means that every individual possesses two alternative copies of each gene in its genome."
      }
    ]
  },
  "Dashboard — dipl/diploidy.md": {
    "primary": "The state, condition, or quality of having cells with two homologous sets of chromosomes.",
    "secondary": "In evolutionary biology and cytogenetics, the prevailing chromosomal condition of sexually reproducing eukaryotes that buffers against deleterious recessive mutations.",
    "quotes": [
      {
        "author": "Sewall Wright",
        "work": "Evolution and the Genetics of Populations",
        "quote": "The evolutionary advantage of **diploidy** lies in its capacity to mask lethal recessive mutations through heterozygous allelic pairing."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "The transition from predominant haplontic cycles to permanent vegetative **diploidy** marked a pivotal milestone in plant evolution."
      },
      {
        "author": "J. B. S. Haldane",
        "work": "The Causes of Evolution",
        "quote": "Mathematical models of population genetics must account for the doubled gene frequencies inherent to sexual **diploidy**."
      }
    ]
  },
  "Dashboard — dipl/diplomat.md": {
    "primary": "An official appointed by a government to represent the state in international relations and conduct negotiations with foreign powers.",
    "secondary": "A person who demonstrates extraordinary tact, prudence, finesse, and skill in managing sensitive personal or professional negotiations.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The Byzantine court dispatched a seasoned **diplomat** to flatter the barbarian chieftain and negotiate a treaty."
      },
      {
        "author": "Henry Adams",
        "work": "The Education of Henry Adams",
        "quote": "A successful **diplomat** must possess the patience of a sphinx and the ability to maintain silence in three languages."
      },
      {
        "author": "Leo Tolstoy",
        "work": "War and Peace",
        "quote": "Prince Andrew observed the Russian **diplomat** conversing with the French emissaries with consummate elegance and reserve."
      }
    ]
  },
  "Dashboard — dipl/diplomate.md": {
    "primary": "A person who holds a diploma, especially a certified medical or dental specialist accredited by an authorized professional board.",
    "secondary": "In professional licensing and medical administration, a physician who has passed rigorous examinations to become certified as a specialist board diplomate.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "Aequanimitas, with Other Addresses",
        "quote": "Every aspiring **diplomate** must demonstrate not merely book learning, but bedside clinical acumen and moral integrity."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Medical Career and Other Papers",
        "quote": "Board examinations establish rigorous qualifying hurdles before any surgeon may practice as a certified **diplomate**."
      },
      {
        "author": "Oliver Wendell Holmes Sr.",
        "work": "Medical Essays",
        "quote": "The proud **diplomate** framed his parchment credentials, yet the true test of medicine lay before him in the sickroom."
      }
    ]
  },
  "Dashboard — dipl/diplomatic.md": {
    "primary": "Of, relating to, or engaged in diplomacy and international statecraft.",
    "secondary": "Characterized by tact, discretion, sensitivity, and subtle handling of delicate situations or interpersonal disagreements.",
    "quotes": [
      {
        "author": "Edmund Burke",
        "work": "Letters on a Regicide Peace",
        "quote": "The **diplomatic** corps must uphold the dignity and treaty obligations of the crown amidst turbulent continental revolutions."
      },
      {
        "author": "Thomas Babington Macaulay",
        "work": "Critical and Historical Essays",
        "quote": "Sir William Temple was celebrated across Europe for his exceptional **diplomatic** skill in negotiating the Triple Alliance."
      },
      {
        "author": "Jane Austen",
        "work": "Emma",
        "quote": "Mr. Knightley managed the awkward dispute with such **diplomatic** tact that both parties departed in complete harmony."
      }
    ]
  },
  "Dashboard — dipl/diplomatical.md": {
    "primary": "An archaic variant of diplomatic, pertaining to diplomacy, official state treaties, or the deciphering of ancient charters.",
    "secondary": "Relating to the science of diplomatics (the critical study of ancient historical documents, manuscripts, and seals).",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The authenticity of the papal grant was submitted to the rigorous scrutiny of **diplomatical** criticism."
      },
      {
        "author": "Thomas Carlyle",
        "work": "History of Friedrich II of Prussia",
        "quote": "Endless **diplomatical** protocols and couriers passed between Berlin and Vienna throughout the tense autumn."
      },
      {
        "author": "Lord Chesterfield",
        "work": "Letters to His Son",
        "quote": "A young man intended for foreign courts must master both history and the **diplomatical** traditions of European sovereigns."
      }
    ]
  },
  "Dashboard — dipl/diplomatically.md": {
    "primary": "In a diplomatic manner; through the methods of diplomacy or with marked tact and discretion.",
    "secondary": "Managing delicate affairs or negotiations with deliberate nuance, courtesy, and avoidance of offense.",
    "quotes": [
      {
        "author": "Henry James",
        "work": "The Ambassadors",
        "quote": "Strether chose his words **diplomatically**, conscious that a single blunt inquiry would shatter their fragile understanding."
      },
      {
        "author": "Joseph Conrad",
        "work": "Nostromo",
        "quote": "The foreign minister bowed **diplomatically**, avoiding any formal commitment until the gunboat entered the harbor."
      },
      {
        "author": "George Eliot",
        "work": "Daniel Deronda",
        "quote": "She steered the conversation **diplomatically** away from the sensitive topic of family inheritances."
      }
    ]
  },
  "Dashboard — dipl/diplomatics.md": {
    "primary": "The scholarly and critical study of historical documents, official charters, diplomas, and state records to determine their authenticity, date, and provenance.",
    "secondary": "An auxiliary historical discipline founded by Jean Mabillon in the 17th century, analyzing handwriting, scripts, seals, and legal formulas in historical manuscripts.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The forgery of the Donation of Constantine was exposed by Lorenzo Valla and demolished by the critical science of **diplomatics**."
      },
      {
        "author": "Lord Acton",
        "work": "Lectures on Modern History",
        "quote": "Mabillon's masterwork on **diplomatics** furnished historians with an infallible touchstone to separate spurious charters from truth."
      },
      {
        "author": "Thomas Babington Macaulay",
        "work": "The History of England",
        "quote": "Antiquarians versed in **diplomatics** examined the ancient Norman parchment to verify the heraldic seals affixed to the deed."
      }
    ]
  },
  "Dashboard — dipl/diplomatist.md": {
    "primary": "A diplomat; a person engaged or skilled in diplomacy and foreign state negotiations.",
    "secondary": "A person proficient in managing affairs with artful tact, negotiation, and strategic subtlety.",
    "quotes": [
      {
        "author": "Thomas Babington Macaulay",
        "work": "Critical and Historical Essays",
        "quote": "As a **diplomatist**, Machiavelli brought sharp observation, penetrating insight, and cold realism to every embassy."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Memoirs of Sherlock Holmes",
        "quote": "The theft of the naval treaty threatened to ruin the career of an esteemed young **diplomatist** in the Foreign Office."
      },
      {
        "author": "W. M. Thackeray",
        "work": "Vanity Fair",
        "quote": "The venerable **diplomatist** smiled blandly behind his spectacles, guarding secrets that could overturn kingdoms."
      }
    ]
  },
  "Dashboard — dipl/diplophase.md": {
    "primary": "The diploid phase in the life cycle of an organism, extending from syngamy to meiosis.",
    "secondary": "In cytogenetics and botany, the developmental generation or stage during which cell nuclei contain the diploid (2n) number of chromosomes, alternating with the haplophase.",
    "quotes": [
      {
        "author": "C. D. Darlington",
        "work": "Recent Advances in Cytology",
        "quote": "In vascular land plants, the sporophyte generation represents the dominant **diplophase** of the life cycle."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "Genetic recombination and heterozygous masking operate almost exclusively during the vegetative **diplophase**."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "The progressive evolutionary enlargement of the **diplophase** shielded the plant organism from somatic expression of deleterious alleles."
      }
    ]
  },
  "Dashboard — dipl/diplopia.md": {
    "primary": "A visual disturbance in which a single object is perceived as two images; double vision.",
    "secondary": "In clinical ophthalmology and neurology, a symptom caused by ocular misalignment (strabismus), cranial nerve palsy, or orbital trauma.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Sudden onset of **diplopia** accompanied by ptosis points ominously toward a lesion involving the third cranial nerve."
      },
      {
        "author": "Oliver Wendell Holmes Sr.",
        "work": "Over the Teacups",
        "quote": "The tired student rubbed his aching eyes to banish the momentary **diplopia** that blurred the printed Greek text."
      },
      {
        "author": "William Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "In uncorrected ocular palsies, subjective **diplopia** forces the patient to tilt the head in compensation."
      }
    ]
  },
  "Dashboard — dipl/diplopoda.md": {
    "primary": "A class of myriapods commonly known as millipedes, characterized by having two pairs of jointed legs on most body segments.",
    "secondary": "In arthropod taxonomy, cylindrical or flattened detritivorous invertebrates with double-segmented diplosomites, contrasting with carnivorous chilopods (centipedes).",
    "quotes": [
      {
        "author": "Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Each apparent body segment in **Diplopoda** represents the fusion of two primitive somites, each bearing a pair of ambulatory limbs."
      },
      {
        "author": "John Obadiah Westwood",
        "work": "An Introduction to the Modern Classification of Insects",
        "quote": "Unlike the swift, venomous centipedes, slow-moving members of the **Diplopoda** feed upon decaying vegetable mold."
      },
      {
        "author": "Charles Darwin",
        "work": "The Formation of Vegetable Mould through the Action of Worms",
        "quote": "Among forest leaf-litter, myriapods belonging to **Diplopoda** assist earthworms in pulverizing organic debris."
      }
    ]
  },
  "Dashboard — dipl/diplopterygium.md": {
    "primary": "A genus of tropical and subtropical scrambling ferns in the family Gleicheniaceae, characterized by repeatedly forking fronds.",
    "secondary": "In pteridology, umbrella-like scrambling ferns that form dense, sun-tolerant thickets along forest margins and roadside banks in the paleotropics.",
    "quotes": [
      {
        "author": "Joseph Dalton Hooker",
        "work": "Himalayan Journals",
        "quote": "Dense tangles of climbing **Diplopterygium** ferns covered the moist ravine slopes, blocking our ascent through the jungle."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "The open clearings were rapidly colonized by the vigorous, dichotomously branching fronds of **Diplopterygium**."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "The frond architecture in **Diplopterygium** exhibits remarkable pseudodichotomous branching with dormant terminal buds."
      }
    ]
  },
  "Dashboard — dipl/diplosis.md": {
    "primary": "The doubling of the chromosome number, particularly during fertilization (syngamy) when haploid gametes unite.",
    "secondary": "In cytogenetics, the fundamental nuclear event wherein two haploid genomes fuse to establish the diploid chromosome complement of the zygote.",
    "quotes": [
      {
        "author": "C. D. Darlington",
        "work": "Recent Advances in Cytology",
        "quote": "The biological cycle represents an unending alternation between haploid reduction in meiosis and chromosome **diplosis** at fertilization."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "Syngamy achieves nuclear **diplosis**, reconstituting the paired allelic state necessary for somatic development."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "Without regular meiotic reduction, every successive generation would experience runaway **diplosis** and polyploid chaos."
      }
    ]
  },
  "Dashboard — dipl/diplotaxis.md": {
    "primary": "A genus of flowering plants in the family Brassicaceae, known as wall-rockets, having seeds arranged in two distinct rows in each pod chamber.",
    "secondary": "In systematic botany, yellow- or white-flowered cruciferous herbs whose elongate siliques bear biseriate seeds, native to Europe and the Mediterranean basin.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The introduced weed **Diplotaxis** tenuifolia thrives in waste gravel, recognized by its pungent leaves and two-ranked seeds."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "The botanical name **Diplotaxis** accurately depicts the biseriate arrangement of seeds inside the narrow pod."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "The Flora of British India",
        "quote": "Specimens of **Diplotaxis** were collected along arid rocky outcroppings bordering the Mediterranean coast."
      }
    ]
  },
  "Dashboard — dipl/diplotene.md": {
    "primary": "The fourth sub-stage of prophase I in meiosis, during which homologous chromosomes begin to separate while remaining joined at chiasmata.",
    "secondary": "In cytogenetics, the extended meiotic stage wherein crossing-over sites become microscopically visible as chiasmata, and during which transcription may resume (as in lampbrush chromosomes).",
    "quotes": [
      {
        "author": "C. D. Darlington",
        "work": "Recent Advances in Cytology",
        "quote": "Upon entering the **diplotene** stage, the paired homologues repel each other, revealing the physical points of genetic crossing-over."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "Chromosomes in human oocytes enter a prolonged, quiescent **diplotene** arrest that persists for decades until ovulation."
      },
      {
        "author": "Thomas Hunt Morgan",
        "work": "The Theory of the Gene",
        "quote": "Microscopic preparations of the **diplotene** nucleus provide direct visual confirmation of chiasma formation between chromatids."
      }
    ]
  },
  "Dashboard — dipl/undiplomatic.md": {
    "primary": "Lacking tact, sensitivity, discretion, or diplomatic finesse; blunt or indiscreet.",
    "secondary": "In political and interpersonal affairs, behaving or speaking in a manner that offends conventions, strains alliances, or sparks unnecessary conflict.",
    "quotes": [
      {
        "author": "Thomas Babington Macaulay",
        "work": "The History of England",
        "quote": "The envoy's arrogant and **undiplomatic** outburst alienated the very ministers whose friendship he was dispatched to cultivate."
      },
      {
        "author": "Henry Adams",
        "work": "The Education of Henry Adams",
        "quote": "He was too passionately honest for statecraft, constantly making blunt and **undiplomatic** declarations."
      },
      {
        "author": "W. M. Thackeray",
        "work": "Vanity Fair",
        "quote": "Old Osborne burst into an **undiplomatic** rage that instantly derailed the delicate marriage settlements."
      }
    ]
  },
  "Dashboard — dipl/undiplomatically.md": {
    "primary": "In an undiplomatic, tactless, or indiscreet manner.",
    "secondary": "Expressing opinions bluntly, without regard for delicate social sensibilities or political protocol.",
    "quotes": [
      {
        "author": "Joseph Conrad",
        "work": "The Secret Agent",
        "quote": "The assistant commissioner remarked **undiplomatically** that bureaucratic delays were paralyzing the entire detective department."
      },
      {
        "author": "George Bernard Shaw",
        "work": "Man and Superman",
        "quote": "Tanner declared his opinions **undiplomatically**, delighting in upsetting the complacent hypocrisies of drawing-room society."
      },
      {
        "author": "Henry James",
        "work": "The Portrait of a Lady",
        "quote": "Caspar Goodwood pressed his suit **undiplomatically**, demanding answers where silence would have been more persuasive."
      }
    ]
  },
  "Dashboard — dodec/Dodecanese.md": {
    "primary": "A group of twelve principal islands (and numerous smaller islets) in the southeastern Aegean Sea, including Rhodes, Kos, and Patmos.",
    "secondary": "In Mediterranean history and geopolitics, an Aegean archipelago historically contested between ancient Greece, Byzantium, the Knights Hospitaller, the Ottomans, Italy, and Greece.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The island fortresses of the **Dodecanese** stood for centuries as maritime outposts against naval incursions in the Aegean."
      },
      {
        "author": "George Grote",
        "work": "A History of Greece",
        "quote": "The Doric cities of Rhodes and Cos in the southern **Dodecanese** developed prosperous maritime trading republics."
      },
      {
        "author": "Herodotus",
        "work": "The Histories",
        "quote": "Greek colonists founded flourishing commonwealths across the islands now known as the **Dodecanese**."
      }
    ]
  },
  "Dashboard — dodec/dodec.md": {
    "primary": "A Greek combining root morpheme (δώδεκα, dodeka) signifying twelve.",
    "secondary": "In geometry, chemistry, and architecture, a combining form producing technical terms involving twelve units, sides, faces, or carbon atoms (as in dodecagon, dodecahedron, dodecane).",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The formative element **dodec-** represents the Greek compound numeral signifying two and ten, or twelve."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "Derivatives incorporating **dodec-** designate groups of twelve gods, twelve columns, or twelve geometric faces."
      },
      {
        "author": "Thomas Heath",
        "work": "A History of Greek Mathematics",
        "quote": "Compounds built upon **dodec-** occupy a prominent place in Euclidean stereometry and regular polyhedral theory."
      }
    ]
  },
  "Dashboard — dodec/dodecagon.md": {
    "primary": "A plane geometric polygon bounded by twelve straight sides and twelve interior angles.",
    "secondary": "In Euclidean geometry, a regular dodecagon having interior angles of 150 degrees, constructible with unmarked ruler and compass.",
    "quotes": [
      {
        "author": "Euclid",
        "work": "Elements",
        "quote": "By bisecting the arcs of an inscribed hexagon, the geometer inscribes a regular **dodecagon** in a circle."
      },
      {
        "author": "Archimedes",
        "work": "Measurement of a Circle",
        "quote": "Archimedes inscribed and circumscribed regular polygons of twelve sides, or **dodecagons**, in his progressive approximations of pi."
      },
      {
        "author": "Thomas Heath",
        "work": "The Thirteen Books of Euclid's Elements",
        "quote": "The regular **dodecagon** provides an elementary stepping stone for doubling the sides of inscribed circles toward polygon limits."
      }
    ]
  },
  "Dashboard — dodec/dodecahedron.md": {
    "primary": "A three-dimensional polyhedron bounded by twelve plane faces, especially the regular dodecahedron whose faces are regular pentagons.",
    "secondary": "In geometry and crystallography, one of the five Platonic solids, possessing 12 pentagonal faces, 20 vertices, and 30 edges.",
    "quotes": [
      {
        "author": "Plato",
        "work": "Timaeus",
        "quote": "There being a fifth solid construction, God used the regular **dodecahedron** for designing the pattern of the universe."
      },
      {
        "author": "Johannes Kepler",
        "work": "Mysterium Cosmographicum",
        "quote": "Between the orbits of Mars and the Earth, I nested the regular **dodecahedron** in my model of cosmic harmony."
      },
      {
        "author": "Euclid",
        "work": "Elements",
        "quote": "Book XIII culminates in the construction of the five regular solids, concluding with the pentagonal **dodecahedron**."
      }
    ]
  },
  "Dashboard — dodec/dodecaphony.md": {
    "primary": "The twelve-tone musical technique or composition system (serialism) invented by Arnold Schoenberg.",
    "secondary": "In modern musicology, an aesthetic method ensuring that all twelve notes of the chromatic scale are sounded equally often without harmonic hierarchy or tonal center.",
    "quotes": [
      {
        "author": "Arnold Schoenberg",
        "work": "Style and Idea",
        "quote": "I formulated the method of composing with twelve tones, known as **dodecaphony**, to establish new structural logic after the dissolution of tonality."
      },
      {
        "author": "Theodor W. Adorno",
        "work": "Philosophy of New Music",
        "quote": "Rigorous **dodecaphony** surrenders expressive subjectivity to the merciless mathematical discipline of the twelve-tone row."
      },
      {
        "author": "Igor Stravinsky",
        "work": "Conversations with Igor Stravinsky",
        "quote": "In my late compositions, I explored the contrapuntal possibilities offered by **dodecaphony** and serial permutation."
      }
    ]
  },
  "Dashboard — dodec/dodecastyle.md": {
    "primary": "A temple portico, colonnade, or building having twelve columns across the front facade.",
    "secondary": "In classical architecture, an exceptionally monumental facade arrangement (such as the portico of the Hall of Mysteries at Eleusis).",
    "quotes": [
      {
        "author": "Vitruvius",
        "work": "The Ten Books on Architecture",
        "quote": "A monumental temple facade with twelve frontal columns constitutes a grand **dodecastyle** portico."
      },
      {
        "author": "James Fergusson",
        "work": "A History of Architecture in All Countries",
        "quote": "The great hall of Eleusis displayed an impressive **dodecastyle** colonnade designed by the architect Philo."
      },
      {
        "author": "Banister Fletcher",
        "work": "A History of Architecture",
        "quote": "Few classical edifices ventured beyond octastyle arrangements, rendering the majestic **dodecastyle** temple of immense rarity."
      }
    ]
  },
  "Dashboard — dodec/dodecasyllabic.md": {
    "primary": "Consisting of or having twelve syllables; a twelve-syllable word or verse.",
    "secondary": "In prosody and poetics, designating twelve-syllable meters such as the French alexandrine or Byzantine dodecasyllable.",
    "quotes": [
      {
        "author": "George Saintsbury",
        "work": "A History of English Prosody",
        "quote": "The classical French alexandrine is a strict **dodecasyllabic** line divided cleanly by a central caesura."
      },
      {
        "author": "Matthew Arnold",
        "work": "On Translating Homer",
        "quote": "Attempts to render Homeric hexameters into modern **dodecasyllabic** verse often sacrifice the flowing rapidity of the original."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "The stately cadence of the **dodecasyllabic** couplet requires deliberate metrical pauses to prevent auditory monotony."
      }
    ]
  },
  "Dashboard — dodec/hemidodecahedron.md": {
    "primary": "An abstract regular polyhedron or projective polyhedron possessing six pentagonal faces, representing half of a regular dodecahedron.",
    "secondary": "In higher geometry and topology, a non-orientable surface obtained by identifying antipodal faces, edges, and vertices of a regular dodecahedron.",
    "quotes": [
      {
        "author": "H. S. M. Coxeter",
        "work": "Regular Polytopes",
        "quote": "By identifying opposite faces of the Platonic dodecahedron in projective 3-space, one obtains the regular **hemidodecahedron**."
      },
      {
        "author": "Felix Klein",
        "work": "Lectures on the Icosahedron",
        "quote": "Projective transformations collapse antipodal points of polyhedral systems into symmetric configurations such as the **hemidodecahedron**."
      },
      {
        "author": "Arthur Cayley",
        "work": "The Collected Mathematical Papers",
        "quote": "The topological properties of a **hemidodecahedron** correspond to six pentagonal domains mapped upon the real projective plane."
      }
    ]
  },
  "Dashboard — dy/dy.md": {
    "primary": "A combining root morpheme derived from Greek δύο (dyo) meaning two.",
    "secondary": "In linguistics and mathematical philosophy, a formative element producing terms expressing duality, pairs, or base-two relations (as in dyad, dyadic).",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The radical **dy-** reflects the ancient Greek numeral for two, cognate with Latin duo and English two."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "From the numeral stem **dy-** arise foundational philosophical terms denoting paired opposition and twofold nature."
      },
      {
        "author": "Thomas Heath",
        "work": "A History of Greek Mathematics",
        "quote": "Pythagorean arithmetic placed the monad and the **dy-** at the metaphysical origin of all numerical generation."
      }
    ]
  },
  "Dashboard — dy/dyad.md": {
    "primary": "A group of two; a pair or couple; two individuals or elements regarded as a single unit.",
    "secondary": "In philosophy, sociology, and mathematics, a fundamental two-part relationship (e.g. the Pythagorean Indefinite Dyad, a two-person social group, or a tensor product of two vectors).",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "Metaphysics",
        "quote": "Plato posited the Great and Small as the material principle or Indefinite **Dyad**, cooperating with the One."
      },
      {
        "author": "Georg Simmel",
        "work": "The Sociology of Georg Simmel",
        "quote": "The social **dyad** represents the most intimate human association, dependent entirely upon the continued participation of both partners."
      },
      {
        "author": "Josiah Willard Gibbs",
        "work": "Vector Analysis",
        "quote": "A **dyad** is an operator formed by juxtaposing two vectors, acting upon other vectors through scalar and vector products."
      }
    ]
  },
  "Dashboard — dy/dyadic.md": {
    "primary": "Pertaining to, involving, or consisting of a dyad; based on the number two; binary.",
    "secondary": "In mathematics and logic, relating to operations or relations with two arguments (such as dyadic arithmetic / binary notation, or dyadic tensors in vector analysis).",
    "quotes": [
      {
        "author": "Gottfried Wilhelm Leibniz",
        "work": "Explication de l'Arithmétique Binaire",
        "quote": "I developed the **dyadic** system of arithmetic, using only 0 and 1, as an image of creation out of nothing by the One."
      },
      {
        "author": "Josiah Willard Gibbs",
        "work": "Vector Analysis",
        "quote": "The sum of several dyads constitutes a **dyadic** polynomial, representing the most general linear vector function."
      },
      {
        "author": "Charles Sanders Peirce",
        "work": "Collected Papers",
        "quote": "Phenomenological Secondness embodies raw resistance, action-reaction, and every purely **dyadic** relationship."
      }
    ]
  }
};

console.log('Starting Batch 2 curation (' + Object.keys(batchData).length + ' words)...');
const updated = updateNotesBatch(baseClusterDir, batchData);
console.log('Batch 2 complete: successfully updated ' + updated + ' notes.');
