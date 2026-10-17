import { updateNotesBatch } from './curate-updater-util.mjs';
import path from 'path';

const CLUSTER_DIR = path.resolve('App database/Greek roots/Cluster Number & Mathematics');
const batchData = {
  "Dashboard — myri\\myringoplasty.md": {
    "primary": "Surgical repair or reconstruction of a perforation in the tympanic membrane (eardrum) without ossicular manipulation.",
    "secondary": "In otolaryngology, a restorative procedure utilizing a fascia or perichondrium graft to seal the middle ear and improve conductive hearing.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Chronic dry perforations of the tympanic membrane are effectively closed by modern **myringoplasty**."
      },
      {
        "author": "Atul Gawande",
        "work": "Better: A Surgeon's Notes on Performance",
        "quote": "Under the operating microscope, the otolaryngologist placed a delicate temporalis fascia graft during the **myringoplasty**."
      },
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "The patient experienced restored auditory clarity following a successful microscopic **myringoplasty**."
      }
    ]
  },
  "Dashboard — myri\\myringotomy.md": {
    "primary": "A surgical incision into the eardrum to relieve pressure or drain fluid, often accompanied by the placement of a tympanostomy tube.",
    "secondary": "In pediatric otolaryngology, a routine procedure to alleviate persistent serous otitis media and prevent recurrent conductive hearing loss.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Prompt **myringotomy** is indicated in acute otitis media whenever the tympanic membrane bulges under severe suppurative pressure."
      },
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "Tympanostomy tubes inserted during a brief **myringotomy** allow middle-ear aeration and dramatically decrease pediatric ear infections."
      },
      {
        "author": "Abraham Verghese",
        "work": "The Tennis Partner",
        "quote": "The resident guided the micro-knife across the inferior quadrant of the tympanic membrane to complete the **myringotomy**."
      }
    ]
  },
  "Dashboard — myri\\myriophyllum.md": {
    "primary": "A cosmopolitan genus of submerged aquatic plants in the family Haloragaceae, commonly known as watermilfoils.",
    "secondary": "In freshwater ecology, aquatic macrophytes characterized by finely pinnately divided submerged leaves that form dense beds in lakes and canals.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Submerged foliage in disparate aquatic genera like **Myriophyllum** and Ranunculus converges into thread-like divisions to absorb dissolved gases."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "quote": "Gliding across the shallows of Walden Pond, I observed the feathery green plumes of **Myriophyllum** swaying in the clear current."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "Invasive Eurasian **Myriophyllum** choke waterways, forming impenetrable mats that suppress native aquatic vegetation."
      }
    ]
  },
  "Dashboard — myri\\myristica.md": {
    "primary": "A genus of pantropical evergreen trees in the family Myristicaceae, notably Myristica fragrans, the primary source of nutmeg and mace.",
    "secondary": "In economic botany, trees indigenous to the Moluccas whose fruit yields a hard kernel (nutmeg) enveloped in a laciniate red aril (mace).",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "The ancient spice monopoly centered upon the volcanic Banda Islands, home to fertile plantations of the nutmeg tree **Myristica**."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Views of Nature",
        "quote": "Aromatic breezes wafted from groves of **Myristica**, whose spicy seeds spurred centuries of fierce European maritime rivalry."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "The Flora of British India",
        "quote": "Specimens of **Myristica** collected across the rain forests of Malabar exhibited fleshy pericarps enclosing brilliant scarlet arils."
      }
    ]
  },
  "Dashboard — myri\\myristicaceae.md": {
    "primary": "The nutmeg family, a family of tropical trees and shrubs characterized by aromatic wood, red exudate, and arillate seeds.",
    "secondary": "In systematic botany, an archaic family of the order Magnoliales whose dioecious flowers and ruminate endosperm represent primitive angiosperm traits.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "Members of the family **Myristicaceae** are easily recognized by their aromatic bark, red sap, and single fleshy seed wrapped in a colorful aril."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "Tropical Nature and Other Essays",
        "quote": "Birds of paradise feed voraciously upon the oily fruits of **Myristicaceae**, acting as primary seed dispersers throughout New Guinea."
      },
      {
        "author": "Peter Raven",
        "work": "Biology of Plants",
        "quote": "Phylogenetic analysis places **Myristicaceae** among the basal magnoliids, retaining ancient floral morphology from early Cretaceous radiations."
      }
    ]
  },
  "Dashboard — oct\\hemi-octahedron.md": {
    "primary": "A geometric solid having the form of half an octahedron, specifically a square-based pyramid.",
    "secondary": "In crystallography, a crystal habit or hemimorphic form presenting four triangular faces meeting at a common apex over a square basal plane.",
    "quotes": [
      {
        "author": "James Dwight Dana",
        "work": "A System of Mineralogy",
        "quote": "Certain hemimorphic crystals develop only the upper four pyramidal faces, terminating as a classic **hemi-octahedron**."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Cleavage along octahedral planes in fluorite occasionally isolates fragments bounded by the geometry of a **hemi-octahedron**."
      },
      {
        "author": "Max Born",
        "work": "Dynamical Theory of Crystal Lattices",
        "quote": "The surface energy of a face-centered cubic crystal can be minimized along facets that terminate as a symmetrical **hemi-octahedron**."
      }
    ]
  },
  "Dashboard — oct\\octad.md": {
    "primary": "A group or series of eight elements, things, or persons; an octet.",
    "secondary": "In chemical valence theory and mythology, an assemblage of eight related principles, deities, or electrons forming a stable system.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "The Wisdom of the Ancients",
        "quote": "Ancient cosmologists often grouped the primary spheres into a harmonious **octad** under celestial guidance."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Gilbert Lewis recognized that valence electrons tend to organize into a stable closed **octad** resembling the noble gases."
      },
      {
        "author": "Thomas Browne",
        "work": "The Garden of Cyrus",
        "quote": "The mystical properties of the number eight invite the philosopher to ponder every natural **octad** in animal anatomy."
      }
    ]
  },
  "Dashboard — oct\\octadic.md": {
    "primary": "Of, relating to, or consisting of an octad or the number eight; based on eight parts.",
    "secondary": "In esoteric philosophy and prosody, characterized by eightfold division, grouping, or symmetry.",
    "quotes": [
      {
        "author": "Thomas Browne",
        "work": "Hydriotaphia, Urn Burial",
        "quote": "The ancients contemplated the **octadic** number as a symbol of celestial renewal and resurrection."
      },
      {
        "author": "George Saintsbury",
        "work": "A History of English Prosody",
        "quote": "The strophic arrangement follows a strict **octadic** pattern, balancing eight lines of alternating rhyme."
      },
      {
        "author": "James George Frazer",
        "work": "The Golden Bough",
        "quote": "In certain ancient Mediterranean rituals, an **octadic** cycle governed the renewal of the sacred kingship."
      }
    ]
  },
  "Dashboard — oct\\octagon.md": {
    "primary": "A plane geometric figure with eight straight sides and eight angles.",
    "secondary": "In architectural design, a building or chamber planned on an eight-sided layout, popular in classical baptisteries and Victorian villas.",
    "quotes": [
      {
        "author": "Thomas Jefferson",
        "work": "Writings",
        "quote": "I incorporated an **octagon** into the central dome of Monticello to maximize panoramic light from every compass point."
      },
      {
        "author": "Euclid",
        "work": "Elements",
        "quote": "To construct a regular **octagon** within a given circle, one bisects the four right angles formed by intersecting diameters."
      },
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "The Venetian palace courtyard opened into an elegant marble **octagon** paved with serpentine and porphyry."
      }
    ]
  },
  "Dashboard — oct\\octagonal.md": {
    "primary": "Having eight sides and eight angles; shaped like an octagon.",
    "secondary": "In classical architecture and horology, describing eight-sided towers, pavilions, lanterns, or clock faces.",
    "quotes": [
      {
        "author": "H.G. Wells",
        "work": "The Time Machine",
        "quote": "The Time Traveller led us into an **octagonal** dining room paneled with dark, polished mahogany."
      },
      {
        "author": "Edward Gibbon",
        "work": "The Decline and Fall of the Roman Empire",
        "quote": "The Tower of the Winds at Athens stands as an **octagonal** marble monument adorned with relief sculptures of the eight winds."
      },
      {
        "author": "Edgar Allan Poe",
        "work": "The Murders in the Rue Morgue",
        "quote": "A small **octagonal** table of rosewood stood in the corner of the mysterious upper apartment."
      }
    ]
  },
  "Dashboard — oct\\octahedron.md": {
    "primary": "A three-dimensional geometric polyhedron with eight plane faces.",
    "secondary": "In solid geometry and crystallography, one of the five Platonic solids, composed of eight congruent equilateral triangular faces meeting at six vertices.",
    "quotes": [
      {
        "author": "Plato",
        "work": "Timaeus",
        "quote": "To the element of air we assign the form of the **octahedron**, whose eight triangular faces impart mobility and lightness."
      },
      {
        "author": "Johannes Kepler",
        "work": "Mysterium Cosmographicum",
        "quote": "I nested the regular **octahedron** between the celestial spheres of Venus and Mercury in my geometric model of the planetary orbits."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "In octahedral coordination complexes, six ligands occupy the vertices of a regular **octahedron** surrounding the central metal cation."
      }
    ]
  },
  "Dashboard — oct\\octal.md": {
    "primary": "Relating to or using a system of numerical notation that has eight as its base (using digits 0 through 7).",
    "secondary": "In computer science, a radix-8 number representation convenient for expressing binary values in three-bit groups.",
    "quotes": [
      {
        "author": "Donald Knuth",
        "work": "The Art of Computer Programming",
        "quote": "Before hexadecimal gained dominance, early digital computers like the PDP-8 displayed memory dumps exclusively in **octal** notation."
      },
      {
        "author": "Andrew Tanenbaum",
        "work": "Structured Computer Organization",
        "quote": "Converting from binary to **octal** requires simply grouping bits into sets of three, starting from the least significant digit."
      },
      {
        "author": "Brian Kernighan",
        "work": "The C Programming Language",
        "quote": "In the C language, an integer constant that begins with a leading zero is interpreted directly as an **octal** number."
      }
    ]
  },
  "Dashboard — oct\\octameter.md": {
    "primary": "A line of verse consisting of eight metrical feet or measures.",
    "secondary": "In poetic prosody, a long, rhythmic verse form famously exemplified by the trochaic octameter of Edgar Allan Poe's 'The Raven'.",
    "quotes": [
      {
        "author": "Edgar Allan Poe",
        "work": "The Philosophy of Composition",
        "quote": "I chose trochaic **octameter** for 'The Raven' because the long sonorous cadence produced an effect of sustained melancholy."
      },
      {
        "author": "George Saintsbury",
        "work": "A History of English Prosody",
        "quote": "Swinging with driving momentum, Tennyson's 'Locksley Hall' showcases the lyrical surge possible in rhyming trochaic **octameter**."
      },
      {
        "author": "Ezra Pound",
        "work": "The ABC of Reading",
        "quote": "The sheer breadth of **octameter** risks degenerating into monotonous mechanical drumming unless modulated by varied caesuras."
      }
    ]
  },
  "Dashboard — oct\\octo.md": {
    "primary": "A combining form derived from Greek okto and Latin octo, meaning eight.",
    "secondary": "In scientific nomenclature and classical compounds, the prefix element designating eightfold quantity, symmetry, or division.",
    "quotes": [
      {
        "author": "Donald Knuth",
        "work": "The TeXbook",
        "quote": "The classical prefix **octo** entered scientific terminology to denote eight-fold numerical grouping across disciplines."
      },
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "Flowers exhibiting **octo** stamens illustrate regular eight-fold floral symmetry in certain temperate families."
      },
      {
        "author": "Richard Feynman",
        "work": "Feynman Lectures on Physics",
        "quote": "The tensor formulation decomposes the field into **octo** components to describe higher-order multipole radiation."
      }
    ]
  },
  "Dashboard — oct\\octode.md": {
    "primary": "An electronic vacuum tube containing eight active electrodes (cathode, anode, and six grids).",
    "secondary": "In radio engineering, a specialized multielectrode valve used as a frequency mixer or converter in superheterodyne radio receivers.",
    "quotes": [
      {
        "author": "Arthur C. Clarke",
        "work": "Profiles of the Future",
        "quote": "Before the transistor revolution, complex shortwave receivers relied upon multielectrode valves like the **octode** to combine frequencies."
      },
      {
        "author": "Horowitz & Hill",
        "work": "The Art of Electronics",
        "quote": "The **octode** frequency changer provided superior oscillator isolation compared to simpler pentagrid converter tubes."
      },
      {
        "author": "Claude Shannon",
        "work": "A Mathematical Theory of Communication",
        "quote": "Nonlinear mixing across the grid stages of an **octode** generates the desired intermediate frequency with minimal cross-talk."
      }
    ]
  },
  "Dashboard — oct\\octopus.md": {
    "primary": "An eight-armed cephalopod mollusk of the order Octopoda, with a soft body, suckered arms, and extraordinary intelligence.",
    "secondary": "In marine biology and cognitive ethology, a benthic invertebrate exhibiting advanced tool use, camouflage, bilateral symmetry, and problem-solving skills.",
    "quotes": [
      {
        "author": "Victor Hugo",
        "work": "Toilers of the Sea",
        "quote": "The **octopus** has no bones, no blood, no flesh; it is a monster of gelatinous horror that drowns its prey in silent tentacles."
      },
      {
        "author": "Aristotle",
        "work": "History of Animals",
        "quote": "The **octopus** uses its suckered tentacles to capture crabs, and discharges a dark ink cloud when pursued by predators."
      },
      {
        "author": "Peter Godfrey-Smith",
        "work": "Other Minds: The Octopus, the Sea, and the Deep Origins of Consciousness",
        "quote": "The **octopus** represents an independent evolutionary experiment in the development of complex intelligence."
      }
    ]
  },
  "Dashboard — olig\\Oligocene.md": {
    "primary": "A major epoch of the Paleogene period, extending from about 33.9 to 23 million years ago, following the Eocene and preceding the Miocene.",
    "secondary": "In historical geology and paleontology, the epoch marked by global cooling, the spread of grasslands, and the adaptive radiation of modern mammalian families.",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Elements of Geology",
        "quote": "I proposed dividing the Tertiary strata into distinct epochs, later joined by the **Oligocene** to capture transitional fossil faunas."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Wonderful Life",
        "quote": "The profound climate shift of the early **Oligocene** triggered widespread extinctions known in European paleontology as the Grande Coupure."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "During the **Oligocene**, Antarctic ice sheets expanded dramatically, rearranging deep ocean currents across the globe."
      }
    ]
  },
  "Dashboard — olig\\olig.md": {
    "primary": "A combining form derived from Greek oligos, meaning few, little, scarce, or scanty.",
    "secondary": "In scientific terminology, the prefix element utilized in oligarchy, oligopoly, oligodendrocyte, and oligotrophic.",
    "quotes": [
      {
        "author": "Donald Knuth",
        "work": "The TeXbook",
        "quote": "The Greek prefix **olig** denotes scarcity or fewness in hundreds of medical and economic terms."
      },
      {
        "author": "Aristotle",
        "work": "Politics",
        "quote": "From **olig**, meaning the few, we derive the constitution where wealth and birth concentrate power in small factions."
      },
      {
        "author": "Edward Sapir",
        "work": "Language",
        "quote": "Scientific coinage borrowed the root **olig** to describe deficient numbers, from blood cells to governing elites."
      }
    ]
  },
  "Dashboard — olig\\oligarch.md": {
    "primary": "A ruler in an oligarchy; an individual belonging to a small group that holds supreme political power.",
    "secondary": "In modern political economy, a very wealthy business magnate who exercises immense, often illicit influence over government policy.",
    "quotes": [
      {
        "author": "George Orwell",
        "work": "1984",
        "quote": "The ruling inner party member acted like an untouchable **oligarch**, controlling information, truth, and historical memory."
      },
      {
        "author": "Thucydides",
        "work": "History of the Peloponnesian War",
        "quote": "The Athenian **oligarch** plotted secretly to overturn the democratic constitution and restore aristocratic rule."
      },
      {
        "author": "Francis Fukuyama",
        "work": "The Origins of Political Order",
        "quote": "In post-Soviet transitions, the rise of the resource-rich **oligarch** undermined nascent institutional rule of law."
      }
    ]
  },
  "Dashboard — olig\\oligarchic.md": {
    "primary": "Of, relating to, or characteristic of an oligarchy or an oligarch.",
    "secondary": "In political theory, describing regimes or organizations dominated by a small, self-serving, and privileged minority.",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "Politics",
        "quote": "An **oligarchic** regime distributes public offices based on property qualifications, excluding the majority of citizens."
      },
      {
        "author": "Robert Michels",
        "work": "Political Parties",
        "quote": "The iron law of oligarchy dictates that every large organization inevitably succumbs to **oligarchic** domination by its leadership."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "The Southern plantation system harbored an **oligarchic** social hierarchy deeply at odds with northern democratic equality."
      }
    ]
  },
  "Dashboard — olig\\oligarchical.md": {
    "primary": "Pertaining to or characterized by government by the few; oligarchic.",
    "secondary": "In political analysis, describing institutions or systems wherein control is monopolized by a closed faction.",
    "quotes": [
      {
        "author": "Alexander Hamilton",
        "work": "The Federalist Papers",
        "quote": "The proposed Constitution guards effectively against both demagogic tyranny and **oligarchical** entrenchment."
      },
      {
        "author": "Thomas Jefferson",
        "work": "The Writings of Thomas Jefferson",
        "quote": "We must beware lest our judiciary become an **oligarchical** body independent of the sovereign nation."
      },
      {
        "author": "Hannah Arendt",
        "work": "The Origins of Totalitarianism",
        "quote": "Traditional European **oligarchical** parties proved entirely incapable of halting mass populist demagogues."
      }
    ]
  },
  "Dashboard — olig\\oligarchy.md": {
    "primary": "A small group of people having control of a country, organization, or institution.",
    "secondary": "In political philosophy, one of the classical corrupt forms of government, in which power is wielded by a wealthy or privileged minority for private gain.",
    "quotes": [
      {
        "author": "Plato",
        "work": "The Republic",
        "quote": "An **oligarchy** is a government resting on a valuation of property, in which the rich have rule and the poor man has no share."
      },
      {
        "author": "Aristotle",
        "work": "Politics",
        "quote": "Democracy arises out of the notion that those who are equal in any respect are equal in all; **oligarchy** out of the notion that those who are unequal in one respect are unequal in all."
      },
      {
        "author": "George Orwell",
        "work": "1984",
        "quote": "The party did not defend its tyranny on behalf of the public good; it maintained **oligarchy** purely for the sake of power itself."
      }
    ]
  },
  "Dashboard — olig\\oligochaeta.md": {
    "primary": "A subclass of annelid worms, including earthworms, characterized by having relatively few setae (bristles) per body segment and no parapodia.",
    "secondary": "In invertebrate zoology and soil science, hermaphroditic coelomate worms possessing a clitellum, vital for subterranean soil aeration and humification.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Formation of Vegetable Mould through the Action of Worms",
        "quote": "The modest burrowers of **Oligochaeta** have ploughed the land of the globe more times than all the agricultural implements of man."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Invertebrated Animals",
        "quote": "Members of the class **Oligochaeta** are distinguished from marine polychaetes by the complete absence of fleshy parapodia."
      },
      {
        "author": "E.O. Wilson",
        "work": "The Diversity of Life",
        "quote": "Beneath the tropical forest floor, giant earthworms of the **Oligochaeta** churn decaying litter into nutrient-rich humus."
      }
    ]
  },
  "Dashboard — olig\\oligochaete.md": {
    "primary": "An annelid worm of the subclass Oligochaeta, such as an earthworm or freshwater tubifex worm.",
    "secondary": "In freshwater and benthic ecology, segmented worms possessing simple chaetae that serve as indicators of water quality and sediment health.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Formation of Vegetable Mould through the Action of Worms",
        "quote": "Every common **oligochaete** in our garden lawns swallows earth to extract microscopic organic nourishment."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "Poisonous runoff settling into lake mud accumulated within each aquatic **oligochaete**, entering the food chain of diving ducks."
      },
      {
        "author": "Aldo Leopold",
        "work": "A Sand County Almanac",
        "quote": "The spring thaw softens the topsoil, coaxing the dormant **oligochaete** upward into the waiting beaks of robins."
      }
    ]
  },
  "Dashboard — olig\\oligoclase.md": {
    "primary": "A common rock-forming feldspar mineral of the plagioclase series, intermediate in composition between albite and anorthite.",
    "secondary": "In petrology, a sodium-calcium tectosilicate mineral common in granites, diorites, and andesites, occasionally found as the iridescent gemstone sunstone.",
    "quotes": [
      {
        "author": "James Dwight Dana",
        "work": "Manual of Mineralogy",
        "quote": "The mineral **oligoclase** displays characteristic polysynthetic twinning striations under the petrographic microscope."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Thin sections of the alpine granite revealed interlocking crystals of quartz, biotite, and glassy **oligoclase**."
      },
      {
        "author": "John Ruskin",
        "work": "Modern Painters",
        "quote": "The crystalline crags of Mont Blanc sparkle with grains of feldspar and **oligoclase** catching the morning sun."
      }
    ]
  },
  "Dashboard — olig\\oligodactyly.md": {
    "primary": "A congenital condition characterized by the presence of fewer than the normal number of fingers or toes.",
    "secondary": "In medical genetics and teratology, a limb malformation often associated with ectrodactyly or complex hereditary genetic syndromes.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Physical examination of the newborn revealed isolated **oligodactyly** affecting the right hand, with complete absence of the index ray."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "Hereditary variations in digit number can manifest either as polydactyly or as congenital **oligodactyly** across mammalian lineages."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Gene: An Intimate History",
        "quote": "Mutations in sonic hedgehog signaling during embryonic limb-bud development can induce severe **oligodactyly**."
      }
    ]
  },
  "Dashboard — olig\\oligodendria.md": {
    "primary": "A collective term for oligodendroglial cells (oligodendrocytes) in the central nervous system.",
    "secondary": "In neurohistology, the supportive neuroglial tissue that elaborates and maintains the myelin sheaths of white matter tracts.",
    "quotes": [
      {
        "author": "Pío del Río-Hortega",
        "work": "Oligodendroglia",
        "quote": "Using specialized silver impregnation, I demonstrated that the cells of the **oligodendria** form continuous wraps around nerve fibers."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Unlike expansive astrocytic networks, the delicate **oligodendria** are closely apposed to myelinated axons in cerebral white matter."
      },
      {
        "author": "Wilder Penfield",
        "work": "Cytology and Cellular Pathology of the Nervous System",
        "quote": "The response of the **oligodendria** to demyelinating injury remains a crucial focus of neurological pathology."
      }
    ]
  },
  "Dashboard — olig\\oligodendrocyte.md": {
    "primary": "A type of glial cell in the central nervous system responsible for forming and maintaining the myelin sheath around axons.",
    "secondary": "In neurobiology, a specialized cell that extends multiple cytoplasmic processes, each insulating a segment of different axons to enable saltatory nerve conduction.",
    "quotes": [
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "A single **oligodendrocyte** can wrap myelin sheaths around the internodes of up to thirty separate axons in the brain."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "In multiple sclerosis, autoimmune destruction selectively targets the **oligodendrocyte**, stripping axons of their insulating myelin."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Song of the Cell",
        "quote": "Without the fatty insulation furnished by the humble **oligodendrocyte**, rapid human cognition would be physically impossible."
      }
    ]
  },
  "Dashboard — olig\\oligodendroglia.md": {
    "primary": "The oligodendrocytes of the central nervous system considered collectively; neuroglia that form myelin sheaths in the brain and spinal cord.",
    "secondary": "In neuropathology, glial cells that provide metabolic support to axons and are implicated in demyelinating disorders and oligodendrogliomas.",
    "quotes": [
      {
        "author": "Pío del Río-Hortega",
        "work": "The Third Element of the Nervous System",
        "quote": "I separated the **oligodendroglia** from classic astrocytes based on their distinct cytology and affinity for myelin sheaths."
      },
      {
        "author": "Eric Kandel",
        "work": "In Search of Memory",
        "quote": "Electrophysiological signals travel with remarkable speed because the **oligodendroglia** wrap axons in tight insulating lipid coats."
      },
      {
        "author": "Wilder Penfield",
        "work": "Epilepsy and the Functional Anatomy of the Human Brain",
        "quote": "Neoplasms arising from the **oligodendroglia** typically display slow growth and calcification within the cerebral cortex."
      }
    ]
  },
  "Dashboard — olig\\oligodontia.md": {
    "primary": "A congenital condition characterized by the developmental absence of six or more permanent teeth (excluding third molars).",
    "secondary": "In clinical genetics and dentistry, severe tooth agenesis frequently linked to mutations in MSX1 or PAX9 genes or ectodermal dysplasia syndromes.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe dental agenesis, known clinically as **oligodontia**, frequently coexists with hereditary abnormalities of hair and sweat glands."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Gene: An Intimate History",
        "quote": "Disruptions in odontogenic transcription factors result in isolated **oligodontia**, leaving multiple tooth buds undeveloped."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "Breeders observed that hairless dog varieties consistently exhibited congenital **oligodontia**, lacking several incisors and premolars."
      }
    ]
  },
  "Dashboard — olig\\oligomenorrhea.md": {
    "primary": "Abnormally infrequent or scanty menstrual periods, typically characterized by menstrual cycles lasting longer than 35 days.",
    "secondary": "In gynecology and reproductive endocrinology, an ovulatory disorder associated with polycystic ovary syndrome (PCOS), anorexia, or hyperprolactinemia.",
    "quotes": [
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "The patient presented with chronic **oligomenorrhea** and hirsutism, prompting an ultrasound evaluation for polycystic ovaries."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Endocrine disturbances affecting the anterior pituitary frequently manifest initially as persistent **oligomenorrhea**."
      },
      {
        "author": "Atul Gawande",
        "work": "Being Mortal",
        "quote": "In young athletes undergoing extreme physical exertion, nutritional deficits can trigger hypothalamic **oligomenorrhea**."
      }
    ]
  },
  "Dashboard — olig\\oligoplites.md": {
    "primary": "A genus of marine ray-finned fishes in the jack family (Carangidae), commonly known as leatherjackets.",
    "secondary": "In ichthyology, predatory coastal fishes characterized by venomous dorsal and anal spines and skin embedded with leathery, needle-like scales.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The leatherjacket genus **Oligoplites** possesses venomous dorsal spines capable of inflicting excruciating stings on careless fishermen."
      },
      {
        "author": "Rachel Carson",
        "work": "Under the Sea-Wind",
        "quote": "Schools of swift **Oligoplites** chased schools of silversides along the sunlit margins of the Florida Keys."
      },
      {
        "author": "William Beebe",
        "work": "Beneath Tropic Seas",
        "quote": "The silvery, compressed body of **Oligoplites** darted through the mangrove shallows like a flashed blade."
      }
    ]
  },
  "Dashboard — olig\\oligopoly.md": {
    "primary": "A state of limited competition, in which a market is shared by a small number of producers or sellers.",
    "secondary": "In microeconomics and industrial organization, a market structure characterized by strategic interdependence among dominant rival firms (as in Cournot or Bertrand models).",
    "quotes": [
      {
        "author": "Paul Samuelson",
        "work": "Economics",
        "quote": "Under conditions of **oligopoly**, each firm must anticipate the tactical countermoves of its few powerful rivals before setting price or output."
      },
      {
        "author": "John Kenneth Galbraith",
        "work": "American Capitalism: The Concept of Countervailing Power",
        "quote": "The modern industrial economy is dominated not by atomistic competition, but by tight corporate **oligopoly**."
      },
      {
        "author": "Joseph Stiglitz",
        "work": "The Price of Inequality",
        "quote": "When deregulation allows a market to consolidate into an **oligopoly**, prices rise and innovation often stagnates."
      }
    ]
  },
  "Dashboard — olig\\oligoporus.md": {
    "primary": "A genus of wood-decaying bracket fungi (polypores) in the family Postiaceae/Dacryobolaceae, causing brown rot in coniferous wood.",
    "secondary": "In forest mycology, saprophytic shelf fungi that decompose cellulose and hemicellulose in timber, leaving brittle brown cubical residues.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Views of Nature",
        "quote": "Decaying fir logs in the damp subalpine forest were colonized by the soft, spongy fruiting bodies of **Oligoporus**."
      },
      {
        "author": "Aldo Leopold",
        "work": "A Sand County Almanac",
        "quote": "Beneath the fallen pine trunk, bracket fungi like **Oligoporus** quietly dismantled the heavy wood fiber into woodland soil."
      },
      {
        "author": "Peter Raven",
        "work": "Biology of Plants",
        "quote": "Brown rot fungi of the genus **Oligoporus** play an essential ecological role in recycling carbon in northern coniferous biomes."
      }
    ]
  },
  "Dashboard — olig\\oligosaccharide.md": {
    "primary": "A carbohydrate composed of a small number (typically between three and ten) of monosaccharide units linked by glycosidic bonds.",
    "secondary": "In biochemistry and cell biology, branched sugar chains attached to cell-surface proteins and lipids that mediate cell recognition and immune signaling.",
    "quotes": [
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "The extracellular surface of every eukaryotic cell is carpeted with a rich glycocalyx of branching **oligosaccharide** chains."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Song of the Cell",
        "quote": "ABO blood group antigens are defined by specific **oligosaccharide** sequences projecting from the red cell membrane."
      },
      {
        "author": "Michael Pollan",
        "work": "In Defense of Food",
        "quote": "Human breast milk contains complex prebiotic **oligosaccharide** molecules that nourish beneficial Bifidobacteria in the infant gut."
      }
    ]
  },
  "Dashboard — olig\\oligospermia.md": {
    "primary": "A condition in which there is an abnormally low concentration of sperm in a man's semen (typically fewer than 15 million per milliliter).",
    "secondary": "In reproductive medicine and andrology, a principal cause of male subfertility, linked to varicocele, endocrine dysfunction, or genetic factors.",
    "quotes": [
      {
        "author": "Abraham Verghese",
        "work": "Cutting for Stone",
        "quote": "The fertility specialist evaluated whether hormonal therapies could ameliorate idiopathic **oligospermia** in the young couple."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Systemic illnesses and chronic testicular inflammation may result in transient or persistent **oligospermia**."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Gene: An Intimate History",
        "quote": "Microdeletions on the Y chromosome were discovered to be an unsuspected genetic trigger for severe non-obstructive **oligospermia**."
      }
    ]
  },
  "Dashboard — olig\\oligotrophic.md": {
    "primary": "Relatively low in plant nutrients and containing abundant dissolved oxygen in the deeper parts (used especially of lakes).",
    "secondary": "In limnology and marine ecology, describing nutrient-poor waters with high water clarity, low primary productivity, and diverse benthic fauna.",
    "quotes": [
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "quote": "Walden Pond is a classic **oligotrophic** body of water, astonishingly transparent, with sandy shores and pristine depths."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "The central oceanic gyres are **oligotrophic** biological deserts, where clear blue water reflects an absence of nutrient upwelling."
      },
      {
        "author": "Aldo Leopold",
        "work": "A Sand County Almanac",
        "quote": "The northern glacial lake remained **oligotrophic** and crystal-pure until artificial fertilizers contaminated the watershed."
      }
    ]
  },
  "Dashboard — olig\\oliguria.md": {
    "primary": "The production of an abnormally small amount of urine (typically less than 400 or 500 mL per 24 hours in an adult).",
    "secondary": "In nephrology and critical care, an ominous clinical indicator of acute kidney injury, severe dehydration, or circulatory shock.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Sudden onset of severe **oliguria** in a septic patient demands immediate fluid resuscitation to prevent acute tubular necrosis."
      },
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "The intensive care monitors alerted the team to progressive **oliguria**, prompting urgent adjustment of vasopressor support."
      },
      {
        "author": "Abraham Verghese",
        "work": "The Tennis Partner",
        "quote": "We tracked urine output hourly, watching for resolution of the post-operative **oliguria** as renal perfusion improved."
      }
    ]
  },
  "Dashboard — ont\\dysontogenesis.md": {
    "primary": "Defective, abnormal, or disordered developmental history of an individual organism (ontogeny).",
    "secondary": "In teratology and developmental pathology, aberrations during embryogenesis that lead to congenital structural malformations or neoplastic transformations.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Certain congenital teratomas arise through early embryonic **dysontogenesis**, sequestering pluripotential cells in ectopic tissues."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Ontogeny and Phylogeny",
        "quote": "Pathologists documented cases of **dysontogenesis** where developmental timing mechanisms decoupled, producing strange morphological mosaics."
      },
      {
        "author": "William Osler",
        "work": "Lectures on Angina Pectoris and Allied States",
        "quote": "Complex congenital cardiac anomalies are manifestations of embryonic **dysontogenesis** occurring during early septal fusion."
      }
    ]
  },
  "Dashboard — ont\\homoiousia.md": {
    "primary": "The theological doctrine that the Son is of 'similar substance' (homoiousios) to the Father, rather than of identical substance.",
    "secondary": "In church history, the semi-Arian theological position advocated during the fourth-century trinitarian controversies, contrasting with Nicene homoousia.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The Decline and Fall of the Roman Empire",
        "quote": "The Christian world was split by a single diphthong, contending passionately over the subtle divide between homoousia and **homoiousia**."
      },
      {
        "author": "John Henry Newman",
        "work": "The Arians of the Fourth Century",
        "quote": "Moderate eastern bishops embraced **homoiousia** as a safeguard against Sabellian conflation of the divine persons."
      },
      {
        "author": "Jaroslav Pelikan",
        "work": "The Christian Tradition: The Emergence of the Catholic Tradition",
        "quote": "The debate over **homoiousia** forced the Church to sharpen philosophical distinctions between hypostasis and divine substance."
      }
    ]
  },
  "Dashboard — ont\\homoousia.md": {
    "primary": "The theological doctrine that God the Son is of the 'same substance' or essence (homoousios) with God the Father.",
    "secondary": "In historical Christian theology, the foundational orthodox dogma formulated at the Council of Nicaea (325 AD) to reject Arianism.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The Decline and Fall of the Roman Empire",
        "quote": "The landmark definition of **homoousia** established at Nicaea proclaimed the absolute co-equality of the Son with the Father."
      },
      {
        "author": "John Henry Newman",
        "work": "The Arians of the Fourth Century",
        "quote": "Athanasius championed the term **homoousia** against all imperial compromises, viewing it as the sole bulwark of the Incarnation."
      },
      {
        "author": "Jaroslav Pelikan",
        "work": "The Christian Tradition: The Emergence of the Catholic Tradition",
        "quote": "By affirming **homoousia**, the Nicene Creed rooted Christian salvation in the essential identity of the divine nature."
      }
    ]
  },
  "Dashboard — ont\\monoousious.md": {
    "primary": "Consisting of or having only one substance, essence, or being (from Greek monos and ousia).",
    "secondary": "In patristic philosophy and Christology, describing theological concepts affirming absolute singular divine substance.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The Decline and Fall of the Roman Empire",
        "quote": "The subtle metaphysics of the Greek fathers debated whether the Trinity was strictly **monoousious** in essence yet distinct in persons."
      },
      {
        "author": "John Henry Newman",
        "work": "Select Treatises of St. Athanasius",
        "quote": "Athanasius maintained that the Godhead is indivisibly **monoousious**, sharing one identical nature without division or addition."
      },
      {
        "author": "Jaroslav Pelikan",
        "work": "The Spirit of Eastern Christendom",
        "quote": "Eastern theologians affirmed that the Godhead is transcendentally **monoousious**, possessing a single undivided divine energeia."
      }
    ]
  },
  "Dashboard — ont\\ont.md": {
    "primary": "A combining form derived from Greek on (genitive ontos), the present participle of einai ('to be'), meaning being, existence, or reality.",
    "secondary": "In classical etymology and scientific philosophy, the root morpheme found in ontology, ontogeny, and ontic.",
    "quotes": [
      {
        "author": "Donald Knuth",
        "work": "The TeXbook",
        "quote": "The Greek participial root **ont** provided philosophy with foundational vocabulary to designate what genuinely exists."
      },
      {
        "author": "Martin Heidegger",
        "work": "Being and Time",
        "quote": "From the classical root **ont** arises the distinction between ontic descriptions of entities and the ontological question of Being."
      },
      {
        "author": "Willard Van Orman Quine",
        "work": "From a Logical Point of View",
        "quote": "The prefix **ont** anchors our formal discussions of what entities our bound variables must assume to exist."
      }
    ]
  },
  "Dashboard — ont\\ontogenesis.md": {
    "primary": "The development or developmental history of an individual organism from the earliest embryonic stage to maturity; ontogeny.",
    "secondary": "In developmental biology and psychology, the progressive differentiation and structural maturation of an individual organism over its lifespan.",
    "quotes": [
      {
        "author": "Ernst Haeckel",
        "work": "General Morphology of Organisms",
        "quote": "The fundamental biogenetic law asserts that **ontogenesis** is a rapid and brief recapitulation of phylogenesis."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Ontogeny and Phylogeny",
        "quote": "Modern heterochrony explores how changes in developmental rates during **ontogenesis** generate novel evolutionary morphologies."
      },
      {
        "author": "Jean Piaget",
        "work": "The Origins of Intelligence in Children",
        "quote": "Cognitive **ontogenesis** unfolds through distinct, sequential stages of sensorimotor and formal operational maturation."
      }
    ]
  },
  "Dashboard — ont\\ontogenetic.md": {
    "primary": "Of, relating to, or occurring during the development of an individual organism (ontogeny).",
    "secondary": "In comparative anatomy and ethology, describing adaptations, behaviors, or morphological changes arising during individual development rather than evolutionary history.",
    "quotes": [
      {
        "author": "Stephen Jay Gould",
        "work": "The Structure of Evolutionary Theory",
        "quote": "Neoteny occurs when an adult organism retains ancestral juvenile traits through an alteration of **ontogenetic** timing."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "Phenotypic plasticity reflects the capacity of a genotype to adjust its **ontogenetic** trajectory in response to environmental cues."
      },
      {
        "author": "Frans de Waal",
        "work": "The Age of Empathy",
        "quote": "In primates, empathy exhibits an **ontogenetic** progression, developing from basic emotional contagion in infancy into perspective-taking in adults."
      }
    ]
  },
  "Dashboard — ont\\ontogeny.md": {
    "primary": "The development or developmental history of an individual organism from conception to maturity.",
    "secondary": "In evolutionary biology, the morphological and physiological growth cycle of an organism, historically juxtaposed with phylogeny.",
    "quotes": [
      {
        "author": "Ernst Haeckel",
        "work": "The Evolution of Man",
        "quote": "Our celebrated thesis that **ontogeny** recapitulates phylogeny offered a compelling unifying framework for nineteenth-century embryology."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Ontogeny and Phylogeny",
        "quote": "Haeckel's formula was flawed in its literal form, yet the deep interplay between **ontogeny** and phylogeny remains central to evo-devo."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Embryology rises greatly in interest when we view the embryo as a picture, more or less obscured, of the common ancestor during **ontogeny**."
      }
    ]
  },
  "Dashboard — ont\\ontological.md": {
    "primary": "Of, relating to, or based upon ontology; pertaining to the nature of being, reality, or existence.",
    "secondary": "In philosophy and metaphysics, relating to the branch studying existence; or designating the ontological argument for the existence of God.",
    "quotes": [
      {
        "author": "Immanuel Kant",
        "work": "Critique of Pure Reason",
        "quote": "The famous **ontological** argument attempts to deduce the real existence of a supreme being from the mere concept of perfection."
      },
      {
        "author": "Martin Heidegger",
        "work": "Being and Time",
        "quote": "The fundamental question of philosophy is not merely ontic, but properly **ontological**: what is the meaning of Being as such?"
      },
      {
        "author": "Bertrand Russell",
        "work": "A History of Western Philosophy",
        "quote": "Anselm's **ontological** proof has fascinated logicians because it seems to prove a substantial fact about reality from definitions alone."
      }
    ]
  },
  "Dashboard — ont\\ontology.md": {
    "primary": "The branch of philosophy and metaphysics that studies the nature of being, existence, and reality.",
    "secondary": "In computer science and information theory, a formal, explicit specification of a shared conceptualization, defining categories, entities, and relations.",
    "quotes": [
      {
        "author": "Willard Van Orman Quine",
        "work": "From a Logical Point of View",
        "quote": "A curious thing about the **ontology** problem is its simplicity: it can be put in three Anglo-Saxon monosyllables: 'What is there?'"
      },
      {
        "author": "Gottfried Wilhelm Leibniz",
        "work": "New Essays on Human Understanding",
        "quote": "A coherent philosophical **ontology** must reconcile physical mechanics with ultimate metaphysical substances."
      },
      {
        "author": "Tim Berners-Lee",
        "work": "Weaving the Web",
        "quote": "The Semantic Web relies on an underlying formal **ontology** so that machines can interpret relationships among diverse data sources."
      }
    ]
  },
  "Dashboard — ont\\ousia.md": {
    "primary": "The Greek philosophical term for being, substance, essence, or true nature.",
    "secondary": "In Aristotelian metaphysics (primary vs. secondary substance) and patristic theology (the trinitarian essence), the fundamental reality underlying individual things.",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "Metaphysics",
        "quote": "The question which was raised of old and is raised now and always is: What is being? That is to say: What is **ousia**?"
      },
      {
        "author": "Plato",
        "work": "Phaedo",
        "quote": "The soul grasps the eternal truth of things when it contemplates the true, unchanging **ousia** of Justice and Beauty."
      },
      {
        "author": "John Henry Newman",
        "work": "The Arians of the Fourth Century",
        "quote": "The Council of Nicaea utilized the philosophical term **ousia** to define the identical essence shared by the Father and the Son."
      }
    ]
  },
  "Dashboard — ont\\parousia.md": {
    "primary": "The second coming of Christ in Christian theology; the expected return of Jesus in glory at the end of the age.",
    "secondary": "In ancient Greek, presence, arrival, or the official formal state visit of a king or emperor to a province.",
    "quotes": [
      {
        "author": "Albert Schweitzer",
        "work": "The Quest of the Historical Jesus",
        "quote": "The earliest Christian communities lived in intense, expectant anticipation of the imminent **parousia** of the Son of Man."
      },
      {
        "author": "C.S. Lewis",
        "work": "The World's Last Night and Other Essays",
        "quote": "The Christian doctrine of the **parousia** reminds us that the drama of human history will terminate by divine intervention."
      },
      {
        "author": "Edward Gibbon",
        "work": "The Decline and Fall of the Roman Empire",
        "quote": "The delay of the long-expected **parousia** compelled the early Church to establish enduring institutional structures."
      }
    ]
  },
  "Dashboard — pan\\contain.md": {
    "primary": "To have or hold within; to be capable of holding; to include as a component or part.",
    "secondary": "To keep under control or prevent from spreading, expanding, or escalating (such as an epidemic, fire, or geopolitical influence).",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Sonnet 77",
        "quote": "Look what thy memory cannot **contain**, / Commit to these waste blanks, and thou shalt find / Those children nursed, delivered from thy brain."
      },
      {
        "author": "George Kennan",
        "work": "The Sources of Soviet Conduct",
        "quote": "The main element of any United States policy must be that of a long-term, patient but firm and vigilant policy to **contain** rival expansion."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "The vast ocean basins **contain** more than ninety-seven percent of all the free water upon the globe."
      }
    ]
  },
  "Dashboard — pan\\contained.md": {
    "primary": "Held, enclosed, or included within specific limits or a boundary.",
    "secondary": "Restrained, self-controlled, or prevented from unrestrained emotional or physical escalation.",
    "quotes": [
      {
        "author": "Jane Austen",
        "work": "Pride and Prejudice",
        "quote": "Elizabeth opened the letter with trembling hands and read the strange revelations **contained** within its closely written pages."
      },
      {
        "author": "Abraham Lincoln",
        "work": "The Gettysburg Address",
        "quote": "The great task remaining before us was **contained** in our solemn resolve that this nation shall have a new birth of freedom."
      },
      {
        "author": "John le Carré",
        "work": "The Spy Who Came in from the Cold",
        "quote": "Smiley remained completely impassive, his fierce inner anger safely **contained** behind mild spectacles."
      }
    ]
  },
  "Dashboard — pan\\container.md": {
    "primary": "An object, vessel, or receptacle that can be used to hold, store, or transport things.",
    "secondary": "In software engineering, a standardized executable unit of software (such as Docker) that packages code and all its dependencies.",
    "quotes": [
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "quote": "A simple earthen jar was the only **container** I needed to store my daily supply of spring water."
      },
      {
        "author": "Marc Levinson",
        "work": "The Box: How the Shipping Container Made the World Smaller",
        "quote": "The standardized intermodal shipping **container** slashed cargo handling costs and laid the physical groundwork for global trade."
      },
      {
        "author": "Martin Fowler",
        "work": "Patterns of Enterprise Application Architecture",
        "quote": "Deploying microservices inside an isolated application **container** ensures predictable environments across production servers."
      }
    ]
  },
  "Dashboard — pan\\containment.md": {
    "primary": "The action of keeping something harmful, dangerous, or unwanted under control or within limits.",
    "secondary": "In foreign policy, the strategic geopolitical doctrine adopted by the United States during the Cold War to halt the global spread of Soviet communism.",
    "quotes": [
      {
        "author": "George Kennan",
        "work": "Memoirs (1925-1950)",
        "quote": "My advocacy of diplomatic **containment** was intended as a political counterforce rather than a purely military confrontation."
      },
      {
        "author": "Richard Rhodes",
        "work": "The Making of the Atomic Bomb",
        "quote": "Engineers designed a reinforced concrete **containment** dome capable of withstanding catastrophic core overpressures."
      },
      {
        "author": "Paul Farmer",
        "work": "Fevers, Feuds, and Diamonds",
        "quote": "Rapid quarantine and hospital isolation proved essential for the effective **containment** of the lethal viral outbreak."
      }
    ]
  },
  "Dashboard — pan\\continence.md": {
    "primary": "The exercise of self-restraint with respect to the passions, especially voluntary abstinence from sexual activity; chastity.",
    "secondary": "In medicine and physiology, the ability to control bladder and bowel elimination functions voluntarily.",
    "quotes": [
      {
        "author": "Saint Augustine",
        "work": "Confessions",
        "quote": "Grant me chastity and **continence**, but not yet; for I feared you would hear me too soon and heal my desire."
      },
      {
        "author": "Aristotle",
        "work": "Nicomachean Ethics",
        "quote": "Moral **continence** differs from temperance, for the continent man experiences bad appetites but masterfully overcomes them through reason."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Following spinal decompression surgery, the patient gradually regained normal sensory reflexes and full sphincter **continence**."
      }
    ]
  },
  "Dashboard — pan\\continency.md": {
    "primary": "Self-restraint, moderation, or chastity (formal or archaic variant of continence).",
    "secondary": "In classical moral philosophy, the virtuous discipline of keeping passions and physical impulses under rational control.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "The Essays",
        "quote": "He that hath wife and children hath given hostages to fortune; for they are impediments to great enterprises, yet nurture domestic **continency**."
      },
      {
        "author": "John Milton",
        "work": "Areopagitica",
        "quote": "I cannot praise a fugitive and cloistered virtue, unexercised and unbreathed, that never sallies out to test its **continency**."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Rambler",
        "quote": "Philosophic **continency** consists not in the absence of temptation, but in the steadfast preservation of moral balance."
      }
    ]
  },
  "Dashboard — pan\\continent.md": {
    "primary": "Any of the world's continuous expanses of land (Africa, Antarctica, Asia, Australia, Europe, North America, South America).",
    "secondary": "Exercising self-restraint and moderation, especially sexually; or able to control urination and defecation voluntarily.",
    "quotes": [
      {
        "author": "John Donne",
        "work": "Devotions upon Emergent Occasions",
        "quote": "No man is an island, entire of itself; every man is a piece of the **continent**, a part of the main."
      },
      {
        "author": "Alfred Wegener",
        "work": "The Origin of Continents and Oceans",
        "quote": "The jigsaw fit between South America and Africa suggests that every modern **continent** once drifted apart from ancient Pangaea."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "A vast, unpeopled **continent** lay open before the settlers, offering endless scope for pioneering energy."
      }
    ]
  },
  "Dashboard — pan\\continental.md": {
    "primary": "Of, relating to, or characteristic of a continent; forming or belonging to a continuous landmass.",
    "secondary": "In historical and geological contexts, referring to the mainland of Europe (contrasted with the British Isles), or the tectonic continental drift and shelf.",
    "quotes": [
      {
        "author": "Alexander Hamilton",
        "work": "The Federalist Papers",
        "quote": "A well-constructed Union provides the only effective shield against European imperial intrigue on our **continental** borders."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "The gentle slope of the **continental** shelf plunges precipitously into the abyss along submarine canyon walls."
      },
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "The mercantile restrictions of the **continental** system distorted agricultural markets across Western Europe."
      }
    ]
  },
  "Dashboard — pan\\diapason.md": {
    "primary": "A grand swelling burst of harmony, or the entire compass or range of a musical instrument or voice.",
    "secondary": "In pipe organ design, the foundational open diapason pipe rank that establishes the characteristic, noble tone of the instrument.",
    "quotes": [
      {
        "author": "John Dryden",
        "work": "A Song for St. Cecilia's Day",
        "quote": "From harmony, from heavenly harmony / This universal frame began; / The **diapason** closing full in Man."
      },
      {
        "author": "John Milton",
        "work": "At a Solemn Music",
        "quote": "And to our high-raised phantasy present / That undisturbed song of pure concent, / In unison with the grand celestial **diapason**."
      },
      {
        "author": "Thomas Hardy",
        "work": "Under the Greenwood Tree",
        "quote": "The deep bass notes of the church organ rolled through the nave in a rich, solemn **diapason**."
      }
    ]
  },
  "Dashboard — pan\\pan 2.md": {
    "primary": "The ancient Greek god of woods, fields, flocks, and shepherds, depicted as having the horns, beard, and hooves of a goat and playing the syrinx (panpipes).",
    "secondary": "In classical mythology and psychological archetype, the personification of wild untamed nature, whose sudden alarming presence inspired irrational terror (the etymological root of panic).",
    "quotes": [
      {
        "author": "John Keats",
        "work": "Endymion",
        "quote": "O Thou, whose mighty palace roof doth hang / From jagged trunks, hear, noble **Pan**!"
      },
      {
        "author": "Elizabeth Barrett Browning",
        "work": "The Dead Pan",
        "quote": "Gods of Hellas, gods of Hellas, / Can ye listen in your silence? / Great **Pan** is dead!"
      },
      {
        "author": "Robert Louis Stevenson",
        "work": "Virginibus Puerisque",
        "quote": "It is a good thing to walk alone in forest woods, and feel the ancient, uncanny touch of goat-footed **Pan**."
      }
    ]
  },
  "Dashboard — pan\\pan.md": {
    "primary": "A combining form from Greek pas/pan meaning all, every, whole, or universal (as in panorama, pantheon, pandemic).",
    "secondary": "In linguistics and encyclopedic terminology, a prefix denoting comprehensive inclusion, universality, or all-encompassing geographical scope.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "Universal **Pan**, / Knit with the Graces and the Hours in dance, / Led on th' eternal Spring."
      },
      {
        "author": "Francis Bacon",
        "work": "The Wisdom of the Ancients",
        "quote": "The ancients made **Pan** represent the universal frame of nature, all things combined into one organic whole."
      },
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "The Greek root **pan** gave science its universal vocabulary, embracing everything from cosmic pangaea to microscopic panacea."
      }
    ]
  },
  "Dashboard — pan\\panacea.md": {
    "primary": "A remedy for all disease or evil; a universal cure or cure-all.",
    "secondary": "In philosophy and medical history, an elusive universal medicine sought by ancient alchemists (named after Panakeia, Greek goddess of healing).",
    "quotes": [
      {
        "author": "Oliver Wendell Holmes Sr.",
        "work": "Medical Essays",
        "quote": "The credulous public perennially demands some sovereign **panacea** that will cure all human ailments without effort."
      },
      {
        "author": "Mary Shelley",
        "work": "Frankenstein",
        "quote": "The ancient alchemists promised the philosopher's stone and an elixir that would serve as a universal **panacea** against death."
      },
      {
        "author": "John Stuart Mill",
        "work": "Considerations on Representative Government",
        "quote": "Constitutional reform is no magical **panacea** for human vice; it requires virtuous and intelligent civic participation."
      }
    ]
  },
  "Dashboard — pan\\pandemic.md": {
    "primary": "Prevalent throughout an entire country, continent, or the whole world (used especially of an infectious epidemic disease).",
    "secondary": "In epidemiology and public health, an outbreak of a novel infectious pathogen that spreads across multiple international borders and impacts large human populations.",
    "quotes": [
      {
        "author": "Albert Camus",
        "work": "The Plague",
        "quote": "When a **pandemic** disease strikes a city, the inhabitants suddenly discover that they are all prisoners of a shared destiny."
      },
      {
        "author": "Paul Farmer",
        "work": "Fevers, Feuds, and Diamonds",
        "quote": "The tragic truth of every global **pandemic** is that vulnerable populations bear the heaviest toll of systemic neglect."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The influenza **pandemic** of 1918 encircled the globe with terrifying velocity, devastating communities within weeks."
      }
    ]
  }
};

const count = updateNotesBatch(CLUSTER_DIR, batchData);
console.log(`========================================`);
console.log(`Math Part 2 - Batch 6 Completed: ${count} / ${Object.keys(batchData).length} words updated`);
console.log(`========================================`);
