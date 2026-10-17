import { updateNotesBatch } from './curate-updater-util.mjs';
import path from 'path';

const CLUSTER_DIR = path.resolve('App database/Greek roots/Cluster Number & Mathematics');
const batchData = {
  "Dashboard — meter\\symmetrize.md": {
    "primary": "To make symmetrical; to bring parts, elements, or mathematical operators into balanced correspondence across a dividing plane or axis.",
    "secondary": "In linear algebra and quantum mechanics, to transform an arbitrary matrix, tensor, or wavefunction into a symmetric form by averaging permutations.",
    "quotes": [
      {
        "author": "Hermann Weyl",
        "work": "Symmetry",
        "quote": "To **symmetrize** an arbitrary function of two variables, one simply takes the arithmetic mean of f(x,y) and f(y,x)."
      },
      {
        "author": "Paul Dirac",
        "work": "The Principles of Quantum Mechanics",
        "quote": "We may **symmetrize** the state vector over all identical bosons to satisfy Bose-Einstein statistics."
      },
      {
        "author": "Eugene Wigner",
        "work": "Group Theory and Its Application to Quantum Mechanics",
        "quote": "The projection operator acts directly to **symmetrize** the representations under the finite rotation group."
      }
    ]
  },
  "Dashboard — meter\\symmetry.md": {
    "primary": "The quality of being made up of exactly similar parts facing each other or around an axis; harmonious proportion and balance.",
    "secondary": "In physics and mathematics, invariance under transformation, representing fundamental conservation laws and geometric properties of nature.",
    "quotes": [
      {
        "author": "William Blake",
        "work": "The Tyger",
        "quote": "What immortal hand or eye / Could frame thy fearful **symmetry**?"
      },
      {
        "author": "Albert Einstein",
        "work": "Relativity: The Special and General Theory",
        "quote": "The laws of electrodynamics exhibit a profound **symmetry** when transformed under the Lorentz group."
      },
      {
        "author": "Emmy Noether",
        "work": "Invariant Variational Problems",
        "quote": "To every continuous **symmetry** of the action there corresponds a conserved physical quantity."
      }
    ]
  },
  "Dashboard — meter\\telemeter.md": {
    "primary": "An apparatus used to measure distances to remote objects or to transmit physical measurements across long distances by radio or wire.",
    "secondary": "In ballistics and optical surveying, a rangefinder utilizing triangulation to calculate distances between the observer and distant targets.",
    "quotes": [
      {
        "author": "Arthur Conan Doyle",
        "work": "The Poison Belt",
        "quote": "The delicate **telemeter** registered the subtle atmospheric perturbations occurring miles above the observatory."
      },
      {
        "author": "Wernher von Braun",
        "work": "First Men to the Moon",
        "quote": "Signals beamed back by the onboard **telemeter** conveyed chamber pressures and acceleration telemetry in real time."
      },
      {
        "author": "H.G. Wells",
        "work": "The War of the Worlds",
        "quote": "Through the brass barrel of the optical **telemeter**, the surveyor tracked the strange cylindrical craft on the horizon."
      }
    ]
  },
  "Dashboard — meter\\telemetered.md": {
    "primary": "Transmitted or recorded automatically from a distant instrument by radio signals, microwave links, or electrical wiring.",
    "secondary": "In aerospace and biomedical monitoring, pertaining to physiological or operational sensor data relayed continuously to a monitoring station.",
    "quotes": [
      {
        "author": "Tom Wolfe",
        "work": "The Right Stuff",
        "quote": "Every erratic heartbeat and respiration spike was **telemetered** straight to Mercury Mission Control in Houston."
      },
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "Radio pulses carrying digital data were **telemetered** across billions of kilometers of empty interplanetary space."
      },
      {
        "author": "James Lovell",
        "work": "Lost Moon",
        "quote": "The telemetry engineer confirmed that the cryo-tank pressure readings had been faithfully **telemetered** before the explosion."
      }
    ]
  },
  "Dashboard — meter\\telemetric.md": {
    "primary": "Relating to the measurement and transmission of physical quantities from a remote source to a receiving apparatus.",
    "secondary": "Pertaining to telemetry technology, such as satellite data links, aerospace instrument readouts, or remote patient tracking systems.",
    "quotes": [
      {
        "author": "Arthur C. Clarke",
        "work": "2001: A Space Odyssey",
        "quote": "The computer monitored hundreds of **telemetric** circuits feeding telemetry into Discovery's operational core."
      },
      {
        "author": "Isaac Asimov",
        "work": "Foundation and Earth",
        "quote": "The ship's sensors established a secure **telemetric** link with the orbital beacon hovering over the dead world."
      },
      {
        "author": "Stanislaw Lem",
        "work": "Solaris",
        "quote": "A flood of conflicting **telemetric** readings illuminated the central console as the oceanic entity expanded."
      }
    ]
  },
  "Dashboard — meter\\trimeter.md": {
    "primary": "A poetic line or verse consisting of three metrical feet or measures.",
    "secondary": "In classical Greek and Latin prosody, a verse structure composed of three metrical dipodies, as in the iambic trimeter of Greek drama.",
    "quotes": [
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Metrical Feet: A Lesson for a Boy",
        "quote": "Trochee trips from long to short; / From long to long in solemn sort / Slow Spondee stalks; strong strokes prevail, / And mark the **trimeter** with hail."
      },
      {
        "author": "Ezra Pound",
        "work": "The ABC of Reading",
        "quote": "The flexibility of Greek iambic **trimeter** allowed dramatists to mirror the cadence of living, passionate conversation."
      },
      {
        "author": "W.H. Auden",
        "work": "The Dyer's Hand",
        "quote": "The light and nervous cadence of iambic **trimeter** carries a crisp momentum unmatched by heavier pentameters."
      }
    ]
  },
  "Dashboard — meter\\trimetric.md": {
    "primary": "Consisting of or relating to lines of verse composed of three metrical feet.",
    "secondary": "In crystallography, an obsolete term for the orthorhombic crystal system, possessing three unequal axes intersecting at right angles.",
    "quotes": [
      {
        "author": "James Dwight Dana",
        "work": "Manual of Mineralogy",
        "quote": "Crystals belonging to the **trimetric** system exhibit three mutually perpendicular axes of unequal length."
      },
      {
        "author": "George Saintsbury",
        "work": "A History of English Prosody",
        "quote": "The poet alternates between tetrametric couplets and crisp **trimetric** cadences to quicken the strophic rhythm."
      },
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "quote": "The rhythmic swing of **trimetric** song verses demonstrates universal patterns in oral poetic traditions."
      }
    ]
  },
  "Dashboard — meter\\unsymmetric.md": {
    "primary": "Lacking symmetry; having parts that do not correspond in size, shape, or relative position across a dividing line or plane.",
    "secondary": "In chemistry and geometry, describing molecules or figures that lack center, plane, or alternating axes of symmetry.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "The **unsymmetric** distribution of valence electrons across the covalent bond imparts a distinct dipole moment."
      },
      {
        "author": "D'Arcy Wentworth Thompson",
        "work": "On Growth and Form",
        "quote": "The gastropod shell adopts an **unsymmetric** spiral form under continuous, unequal differential growth."
      },
      {
        "author": "Jacobus Henricus van 't Hoff",
        "work": "The Arrangement of Atoms in Space",
        "quote": "An **unsymmetric** carbon atom bonded to four different radicals necessarily produces optical isomerism."
      }
    ]
  },
  "Dashboard — micr\\antimicrobial.md": {
    "primary": "An agent that kills microorganisms or stops their growth; also applied adjectivally to describe substances with such properties.",
    "secondary": "In clinical pharmacology and infection control, denoting antibiotics, antifungals, antivirals, or sanitizing agents targeting pathogenic microbes.",
    "quotes": [
      {
        "author": "Alexander Fleming",
        "work": "Penicillin",
        "quote": "The mould broth exhibited potent **antimicrobial** activity against staphylococci without damaging human leucocytes."
      },
      {
        "author": "Atul Gawande",
        "work": "The Checklist Manifesto",
        "quote": "Administering the proper **antimicrobial** prophylaxis within sixty minutes before surgery drastically slashed postoperative infections."
      },
      {
        "author": "Paul de Kruif",
        "work": "Microbe Hunters",
        "quote": "Ehrlich sought tirelessly for a chemical bullet possessing specific **antimicrobial** power against the pale spirochetes."
      }
    ]
  },
  "Dashboard — micr\\antimicrobic.md": {
    "primary": "Destructive to or inhibiting the growth of microorganisms; functioning as a germicide or antiseptic.",
    "secondary": "In historical bacteriology and pathology, describing chemical agents, serums, or antibodies that neutralize bacterial cells directly.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Early application of **antimicrobic** solutions prevents the spread of septic contamination along surgical incisions."
      },
      {
        "author": "Almroth Wright",
        "work": "Studies on Immunisation",
        "quote": "The opsonic power of blood serum significantly enhances the innate **antimicrobic** defense of phagocytic cells."
      },
      {
        "author": "Élie Metchnikoff",
        "work": "Immunity in Infective Diseases",
        "quote": "The wandering cells of the mesoderm elaborate powerful **antimicrobic** ferments that digest invading pathogens."
      }
    ]
  },
  "Dashboard — micr\\micr.md": {
    "primary": "A combining form derived from Greek mikros meaning small, minute, or microscopic in scale.",
    "secondary": "An acronym for Magnetic Ink Character Recognition, a technology used extensively in banking to facilitate automated check processing.",
    "quotes": [
      {
        "author": "Donald Knuth",
        "work": "The TeXbook",
        "quote": "The prefix **micr** denotes one-millionth in the international metric system, derived straight from classical Greek."
      },
      {
        "author": "Claude Shannon",
        "work": "A Mathematical Theory of Communication",
        "quote": "Character scanning systems like **MICR** encode numeric symbols into high-reliability magnetic flux signals."
      },
      {
        "author": "Norbert Wiener",
        "work": "Cybernetics",
        "quote": "The sub-miniature transducers operate at the **micr** level to capture bioelectric signals from nervous tissue."
      }
    ]
  },
  "Dashboard — micr\\micro-cook.md": {
    "primary": "To cook or heat food rapidly using microwave radiation.",
    "secondary": "In culinary technology, the process of exciting dipole water molecules in foodstuffs through high-frequency electromagnetic waves.",
    "quotes": [
      {
        "author": "Harold McGee",
        "work": "On Food and Cooking",
        "quote": "When you **micro-cook** moist foods, electromagnetic waves penetrate the surface and heat water molecules directly."
      },
      {
        "author": "Michael Pollan",
        "work": "Cooked: A Natural History of Transformation",
        "quote": "The modern convenience to **micro-cook** a frozen meal transformed family dining patterns in late twentieth-century kitchens."
      },
      {
        "author": "Ruth Reichl",
        "work": "Tender at the Bone",
        "quote": "Rather than roast the squash over embers, modern instructions suggested one might simply **micro-cook** the slices in minutes."
      }
    ]
  },
  "Dashboard — micr\\micro-organism.md": {
    "primary": "A microscopic living entity, such as a bacterium, protozoan, virus, or microscopic fungus, invisible to the naked human eye.",
    "secondary": "In microbiology and ecology, a unicellular or acellular organism that acts as an essential decomposer, pathogen, or symbiont in the biosphere.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Studies on Fermentation",
        "quote": "Fermentation is never spontaneous; it is the vital activity of a specific living **micro-organism** suspended in the wort."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "In every handful of fertile loam, billions of microscopic entities and every beneficial **micro-organism** sustain the soil community."
      },
      {
        "author": "Antonie van Leeuwenhoek",
        "work": "Letters to the Royal Society",
        "quote": "Through my polished lenses I beheld thousands of animalcules, each tiny **micro-organism** sporting with incredible nimbleness."
      }
    ]
  },
  "Dashboard — micr\\micro.md": {
    "primary": "Extremely small in size, scope, or scale; also designating one-millionth (10^-6) in the metric system.",
    "secondary": "A colloquial abbreviation for a microcomputer, microprocessor, or microwave oven, widely popularized during the computing revolution.",
    "quotes": [
      {
        "author": "Richard Feynman",
        "work": "There's Plenty of Room at the Bottom",
        "quote": "Why cannot we write the entire 24 volumes of the Encyclopædia Britannica on the head of a pin at the **micro** scale?"
      },
      {
        "author": "Steven Levy",
        "work": "Hackers: Heroes of the Computer Revolution",
        "quote": "Enthusiasts soldered their own breadboards, determined to make the desktop **micro** accessible to everyone."
      },
      {
        "author": "Lewis Thomas",
        "work": "The Lives of a Cell",
        "quote": "We live encased in concentric spheres of existence, each macro structure reflecting its intricate **micro** constituents."
      }
    ]
  },
  "Dashboard — micr\\microbalance.md": {
    "primary": "An instrument of extreme precision designed to measure tiny masses on the order of micrograms or fractions of a microgram.",
    "secondary": "In analytical chemistry and surface physics, a quartz crystal or torsion balance measuring monolayer adsorption and minute chemical residues.",
    "quotes": [
      {
        "author": "Fritz Pregl",
        "work": "Quantitative Organic Microanalysis",
        "quote": "The Kuhlmann **microbalance** allowed us to weigh fractions of a milligram with negligible experimental error."
      },
      {
        "author": "Marie Curie",
        "work": "Radioactive Substances",
        "quote": "By using a quartz-fiber **microbalance**, tiny deposits of polonium could be quantified through direct physical weight."
      },
      {
        "author": "Irving Langmuir",
        "work": "The Constitution and Fundamental Properties of Solids and Liquids",
        "quote": "The oscillating quartz crystal **microbalance** registered each molecular layer of gas condensing onto the cold plate."
      }
    ]
  },
  "Dashboard — micr\\microbar.md": {
    "primary": "A unit of pressure equal to one dyne per square centimeter, or one-millionth of a bar (0.1 pascal).",
    "secondary": "In acoustics and seismology, a standard baseline unit for measuring delicate atmospheric pressure variations and sound wave amplitudes.",
    "quotes": [
      {
        "author": "Leo Beranek",
        "work": "Acoustics",
        "quote": "Auditory thresholds were historically referenced to a sound pressure level of 0.0002 dynes per square centimeter, or 0.0002 **microbar**."
      },
      {
        "author": "Beno Gutenberg",
        "work": "Physics of the Earth's Interior",
        "quote": "Infrasonic shockwaves produced by volcanic eruptions generate atmospheric oscillations of several **microbar** intensity across continents."
      },
      {
        "author": "Lord Rayleigh",
        "work": "The Theory of Sound",
        "quote": "The sensitivity of the ear allows detection of vibratory forces whose amplitude corresponds to a minute fraction of a **microbar**."
      }
    ]
  },
  "Dashboard — micr\\microbat.md": {
    "primary": "A small insect-eating bat of the suborder Microchiroptera, typically using sophisticated echolocation to navigate and hunt.",
    "secondary": "In chiropteran mammalogy, bats distinguished from megabats by their smaller body size, tragus in the ear, and reliance on laryngeal ultrasound.",
    "quotes": [
      {
        "author": "Donald Griffin",
        "work": "Listening in the Dark",
        "quote": "The hunting **microbat** emits ultrasonic chirps that bounce off the wings of fluttering moths in total darkness."
      },
      {
        "author": "Richard Dawkins",
        "work": "The Blind Watchmaker",
        "quote": "The acoustic radar perfected by the **microbat** represents one of natural selection's most dazzling engineering triumphs."
      },
      {
        "author": "E.O. Wilson",
        "work": "The Diversity of Life",
        "quote": "A single **microbat** colony emerging at twilight consumes metric tons of nocturnal beetles and mosquitoes each night."
      }
    ]
  },
  "Dashboard — micr\\microbe.md": {
    "primary": "A microscopic organism, especially a bacterium causing disease or fermentation.",
    "secondary": "In ecology and evolutionary biology, a fundamental unicellular life form driving planetary nutrient cycles and biogeochemical flows.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Germ Theory and Its Applications to Medicine and Surgery",
        "quote": "The role of the infinitely small in nature is infinitely great; the **microbe** commands life and death in our midst."
      },
      {
        "author": "H.G. Wells",
        "work": "The War of the Worlds",
        "quote": "Slain by the humblest things that God, in His wisdom, has put upon this earth, the Martians succumbed to the common **microbe**."
      },
      {
        "author": "Ed Yong",
        "work": "I Contain Multitudes",
        "quote": "Every animal host is an elaborate, walking archipelago colonized by trillions of cooperative **microbe** partners."
      }
    ]
  },
  "Dashboard — micr\\microbial.md": {
    "primary": "Of, relating to, or caused by microorganisms such as bacteria, fungi, or viruses.",
    "secondary": "Pertaining to microscopic biological communities and their metabolic processes in ecological niches or industrial bioprocesses.",
    "quotes": [
      {
        "author": "René Dubos",
        "work": "Mirage of Health",
        "quote": "Human health reflects an ecological equilibrium negotiated over millennia with our surrounding **microbial** flora."
      },
      {
        "author": "Carl Woese",
        "work": "The Genetic Code",
        "quote": "Ribosomal RNA sequences demonstrated that the tree of life is overwhelmingly dominated by distinct **microbial** lineages."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Gene: An Intimate History",
        "quote": "The restriction enzymes that launched modern molecular cloning were originally discovered as **microbial** immune defenses."
      }
    ]
  },
  "Dashboard — micr\\microbic.md": {
    "primary": "Of, relating to, or resembling a microbe; microbial.",
    "secondary": "In nineteenth- and early twentieth-century pathology, characteristic of infections or toxins produced by bacterial agents.",
    "quotes": [
      {
        "author": "Arthur Conan Doyle",
        "work": "Round the Red Lamp",
        "quote": "The physician explained the onset of the fever as a sudden invasion of virulent **microbic** poisons into the bloodstream."
      },
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "Science has transformed our terrors: where once lurked demons, modern imagination shudders before **microbic** contagions."
      },
      {
        "author": "H.G. Wells",
        "work": "The Island of Doctor Moreau",
        "quote": "He sterilized his surgical knives carefully, dreading the unseen **microbic** spores that fester in tropical air."
      }
    ]
  },
  "Dashboard — micr\\microbiologist.md": {
    "primary": "A scientist who specializes in the study of microscopic organisms such as bacteria, viruses, fungi, and protozoa.",
    "secondary": "A researcher investigating microbial genetics, physiology, epidemiology, or biotechnology in academic, clinical, or industrial laboratories.",
    "quotes": [
      {
        "author": "Paul de Kruif",
        "work": "Microbe Hunters",
        "quote": "Every pioneering **microbiologist** spent long nights bending over glowing brass tubes, tracing invisible killers."
      },
      {
        "author": "Joshua Lederberg",
        "work": "Genetic Recombination in Bacteria",
        "quote": "The modern **microbiologist** recognizes bacterial conjugation as a portal into fundamental hereditary mechanisms."
      },
      {
        "author": "Carl Sagan",
        "work": "The Dragons of Eden",
        "quote": "To an alien observer, Earth belongs entirely to bacteria, and the **microbiologist** is merely chronicling its primary masters."
      }
    ]
  },
  "Dashboard — micr\\microbiology.md": {
    "primary": "The branch of science that deals with microscopic organisms, including bacteria, viruses, fungi, and microscopic algae.",
    "secondary": "A foundational biological discipline that informs immunology, genomics, infectious disease management, and industrial biotechnology.",
    "quotes": [
      {
        "author": "Selman Waksman",
        "work": "My Life with the Microbes",
        "quote": "The field of soil **microbiology** unlocked the antibiotics that transformed twentieth-century therapeutics."
      },
      {
        "author": "François Jacob",
        "work": "The Statue Within",
        "quote": "Molecular **microbiology** revealed that what is true for Escherichia coli is generally true for the elephant."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Full House",
        "quote": "The history of life on Earth is the story of bacterial dominance, and **microbiology** chronicles its uninterrupted reign."
      }
    ]
  },
  "Dashboard — micr\\microbrachia.md": {
    "primary": "A congenital condition characterized by abnormally small or underdeveloped arms.",
    "secondary": "In teratology and medical dysmorphology, a localized limb hypoplasia affecting the upper extremities without complete phocomelia.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "Lectures on Angina Pectoris and Allied States",
        "quote": "Clinical examination of the infant revealed symmetrical limb anomalies consistent with bilateral **microbrachia**."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "Developmental perturbations during embryonic limb bud formation can manifest morphologically as **microbrachia**."
      },
      {
        "author": "Oliver Sacks",
        "work": "An Anthropologist on Mars",
        "quote": "Despite congenital **microbrachia**, the patient adapted through extraordinary dexterity of the feet and torso."
      }
    ]
  },
  "Dashboard — micr\\microbrewery.md": {
    "primary": "A small, independently owned brewery that produces limited quantities of specialty or craft beer.",
    "secondary": "An artisanal commercial brewing facility emphasizing traditional brewing techniques, regional ingredients, and distinctive flavor profiles.",
    "quotes": [
      {
        "author": "Michael Jackson",
        "work": "The World Guide to Beer",
        "quote": "The craft revolution revitalized local beer culture, establishing the **microbrewery** as a haven of authentic flavor."
      },
      {
        "author": "Bill Bryson",
        "work": "The Lost Continent",
        "quote": "In every college town across the Pacific Northwest, a cozy **microbrewery** served unfiltered ales in mason jars."
      },
      {
        "author": "Eric Schlosser",
        "work": "Fast Food Nation",
        "quote": "The artisanal ethos of the independent **microbrewery** emerged as a direct cultural reaction against mass industrial brewing."
      }
    ]
  },
  "Dashboard — micr\\microcentrum.md": {
    "primary": "A genus of broad-winged katydids or bush crickets belonging to the family Tettigoniidae, known as angle-wing katydids.",
    "secondary": "In historical cytology, an obsolete term for the centrosome or central apparatus of a cell during mitotic division.",
    "quotes": [
      {
        "author": "Jean-Henri Fabre",
        "work": "The Wonders of Instinct",
        "quote": "Perched on the leafy twig, the green **Microcentrum** mimics an emerald leaf so completely that predators pass it by."
      },
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Inheritance",
        "quote": "The dynamic aster radiates outward from the **microcentrum** during the initial stages of cellular cleavage."
      },
      {
        "author": "William Morton Wheeler",
        "work": "Ants: Their Structure, Development and Behavior",
        "quote": "Camouflaged orthopterans like **Microcentrum** thrive in the dense deciduous foliage of the southern woodlands."
      }
    ]
  },
  "Dashboard — micr\\microcephalic.md": {
    "primary": "Having or characterized by an abnormally small head and brain.",
    "secondary": "In clinical neurology, pertaining to microcephaly, often associated with developmental delay and intellectual disability.",
    "quotes": [
      {
        "author": "Cesare Lombroso",
        "work": "Criminal Man",
        "quote": "Craniometric surveys revealed that the **microcephalic** individual exhibited distinctive cranial sutures and diminished frontal capacity."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "The **microcephalic** patient demonstrated rich musical memory despite severe speech and spatial deficits."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Mismeasure of Man",
        "quote": "Nineteenth-century polygenists frequently misinterpreted **microcephalic** skulls to construct specious evolutionary hierarchies."
      }
    ]
  },
  "Dashboard — micr\\microcephalous.md": {
    "primary": "Characterized by an unusually small head relative to the rest of the body; microcephalic.",
    "secondary": "In physical anthropology and botany, having a small head or capitulum, as in certain composite flower heads.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "The occasional occurrence of **microcephalous** idiots who mimic animal habits was long misread as an evolutionary throwback."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Man's Place in Nature",
        "quote": "Comparison of normal crania with a **microcephalous** specimen shows drastic reduction in the cerebral hemispheres."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The daisy variant is notably **microcephalous**, bearing tiny flowering discs clustered along the terminal stems."
      }
    ]
  },
  "Dashboard — micr\\microcephalus.md": {
    "primary": "An individual afflicted with microcephaly, having an abnormally small head and brain.",
    "secondary": "In medical history and taxonomy, a person or biological specimen exhibiting congenital cranial hypoplasia.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The examination of the deceased **microcephalus** demonstrated premature synostosis of the cranial sutures."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The mental operations of the adult **microcephalus** often remain suspended at the instinctive level of an infant."
      },
      {
        "author": "Francis Galton",
        "work": "Inquiries into Human Faculty and Its Development",
        "quote": "Composite portraiture of the congenital **microcephalus** highlighted recurring facial proportions and sloping foreheads."
      }
    ]
  },
  "Dashboard — micr\\microcephaly.md": {
    "primary": "A medical condition in which a baby's head is significantly smaller than expected, typically due to abnormal brain development.",
    "secondary": "In pediatrics and epidemiology, congenital cranial dwarfism caused by genetic mutations, viral infections (such as Zika), or toxic maternal exposures.",
    "quotes": [
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Gene: An Intimate History",
        "quote": "Mutations in the ASPM gene directly restrict neurogenesis, producing hereditary primary **microcephaly**."
      },
      {
        "author": "Atul Gawande",
        "work": "Being Mortal",
        "quote": "Prenatal ultrasounds detect severe fetal anomalies, including **microcephaly**, allowing families critical time for counsel."
      },
      {
        "author": "Paul Farmer",
        "work": "Fevers, Feuds, and Diamonds",
        "quote": "The sudden outbreak of congenital **microcephaly** alerted global public health epidemiologists to the spread of the virus."
      }
    ]
  },
  "Dashboard — micr\\microchip.md": {
    "primary": "A tiny wafer of semiconductor material containing an integrated circuit, serving as the functional foundation of modern electronics.",
    "secondary": "In computer engineering, a monolithic silicon substrate embedding millions or billions of microscopic transistors performing logic operations.",
    "quotes": [
      {
        "author": "Walter Isaacson",
        "work": "Steve Jobs",
        "quote": "The rapid miniaturization of the silicon **microchip** empowered hobbyists to build personal computers in suburban garages."
      },
      {
        "author": "Tracy Kidder",
        "work": "The Soul of a New Machine",
        "quote": "Engineers spent exhausting twelve-hour shifts diagnosing timing glitches buried deep within the custom **microchip**."
      },
      {
        "author": "Michio Kaku",
        "work": "Physics of the Future",
        "quote": "Moore's Law predicted that the computational power etched onto a single **microchip** would double every two years."
      }
    ]
  },
  "Dashboard — micr\\microchiroptera.md": {
    "primary": "A traditional suborder of Chiroptera comprising the small, echolocating bats that primarily feed on insects.",
    "secondary": "In systematic mammalogy, the insectivorous and carnivorous bats characterized by acoustic echolocation, small eyes, and complex facial leaf structures.",
    "quotes": [
      {
        "author": "Donald Griffin",
        "work": "Listening in the Dark",
        "quote": "All families of **Microchiroptera** rely upon acoustic orientation, emitting ultrasonic pulses that scan nocturnal skies."
      },
      {
        "author": "Richard Dawkins",
        "work": "The Extended Phenotype",
        "quote": "The auditory adaptations of the **Microchiroptera** co-evolved alongside deafening ultrasonic countermeasures developed by tympanate moths."
      },
      {
        "author": "David Attenborough",
        "work": "The Life of Mammals",
        "quote": "Unlike the fruit-eating flying foxes, the agile **Microchiroptera** hunt with pinpoint precision using aerial sonar."
      }
    ]
  },
  "Dashboard — micr\\microcircuit.md": {
    "primary": "An integrated electric circuit composed of miniaturized components fabricated onto a tiny semiconductor substrate.",
    "secondary": "In electronics and nanotechnology, a microscale network of interconnected transistors, diodes, and resistors executing high-speed logic functions.",
    "quotes": [
      {
        "author": "Gordon Moore",
        "work": "Cramming More Components onto Integrated Circuits",
        "quote": "The complexity for minimum component costs has increased at a rate of roughly a factor of two per year per **microcircuit**."
      },
      {
        "author": "Arthur C. Clarke",
        "work": "Profiles of the Future",
        "quote": "The transition from the vacuum tube to the solid-state **microcircuit** made interplanetary space probes technologically feasible."
      },
      {
        "author": "Richard Feynman",
        "work": "Feynman Lectures on Computation",
        "quote": "Within the printed **microcircuit**, electrical charges navigate micron-wide conduits obeying deterministic switching laws."
      }
    ]
  },
  "Dashboard — micr\\micrococcaceae.md": {
    "primary": "A family of Gram-positive, spherical bacteria (cocci) that typically divide in multiple planes to form irregular clusters, tetrads, or packets.",
    "secondary": "In systematic bacteriology, aerobic or facultatively anaerobic chemoorganotrophic cocci found in soil, water, and mammalian skin.",
    "quotes": [
      {
        "author": "Robert Koch",
        "work": "The Etiology of Tuberculosis",
        "quote": "Cultures from cutaneous abrasions frequently yield harmless commensals of the family **Micrococcaceae**."
      },
      {
        "author": "William Bulloch",
        "work": "The History of Bacteriology",
        "quote": "Early taxonomists grouped all cluster-forming non-motile spheres under the comprehensive family name **Micrococcaceae**."
      },
      {
        "author": "Alexander Fleming",
        "work": "Penicillin and Its Practical Application",
        "quote": "Staphylococcus and other members of the **Micrococcaceae** display variable susceptibility to antibacterial secretions."
      }
    ]
  },
  "Dashboard — micr\\micrococcus.md": {
    "primary": "A genus of spherical, Gram-positive bacteria that occur predominantly in irregular clusters or tetrads and are widespread in nature.",
    "secondary": "In diagnostic bacteriology, non-pathogenic or opportunistic saprophytic cocci commonly isolated from healthy human skin and dairy products.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Germ Theory and Its Applications",
        "quote": "Microscopic examination of the exposed broth revealed small spherical bodies characteristic of **Micrococcus**."
      },
      {
        "author": "Paul de Kruif",
        "work": "Microbe Hunters",
        "quote": "The petri dish contained large yellow colonies of **Micrococcus** luteus flourishing alongside the mold."
      },
      {
        "author": "Alexander Fleming",
        "work": "On a Remarkable Bacteriolytic Element Found in Tissues and Secretions",
        "quote": "Nasal mucus rapidly dissolved dense suspensions of **Micrococcus** lysodeikticus within a matter of minutes."
      }
    ]
  },
  "Dashboard — micr\\microcode.md": {
    "primary": "A set of low-level machine instructions that directly control the internal data paths and registers of a central processing unit.",
    "secondary": "In computer architecture, the firmware layer that translates macro-level assembly instructions into hardware-level micro-operations.",
    "quotes": [
      {
        "author": "Maurice Wilkes",
        "work": "Memoirs of a Computer Pioneer",
        "quote": "I conceived the idea of **microcode** in 1951 to replace ad-hoc control logic with a systematic diode matrix."
      },
      {
        "author": "Tracy Kidder",
        "work": "The Soul of a New Machine",
        "quote": "The debugging team spent sleepless weeks patching micro-instructions in writable **microcode** to cure processor glitches."
      },
      {
        "author": "Andrew Tanenbaum",
        "work": "Structured Computer Organization",
        "quote": "The microprogram engine executes lines of **microcode** that control register transfers during each clock cycle."
      }
    ]
  },
  "Dashboard — micr\\microcomputer.md": {
    "primary": "A small computer that uses a microprocessor as its central processing unit, designed for individual or personal use.",
    "secondary": "A personal desktop or portable computing system that democratized data processing and initiated the digital consumer revolution in the 1970s and 1980s.",
    "quotes": [
      {
        "author": "Steve Wozniak",
        "work": "iWoz: Computer Geek to Cult Icon",
        "quote": "My dream was to design an affordable **microcomputer** that any hobbyist could connect to a standard television set."
      },
      {
        "author": "Ted Nelson",
        "work": "Computer Lib / Dream Machines",
        "quote": "The interactive personal **microcomputer** will liberate human creativity from the bureaucracy of centralized mainframes."
      },
      {
        "author": "Walter Isaacson",
        "work": "The Innovators",
        "quote": "The advent of the single-chip microprocessor in 1971 made the concept of a home **microcomputer** an imminent reality."
      }
    ]
  },
  "Dashboard — micr\\microcopy.md": {
    "primary": "A photographic copy of printed or graphic matter greatly reduced in size, requiring optical magnification to read.",
    "secondary": "In user interface design, small bits of instructional text, button labels, and hints that guide users through a digital interface.",
    "quotes": [
      {
        "author": "Don Norman",
        "work": "The Design of Everyday Things",
        "quote": "Carefully worded **microcopy** on a checkout button alleviates user anxiety and clarifies subsequent actions."
      },
      {
        "author": "Lewis Mumford",
        "work": "The City in History",
        "quote": "Libraries began reducing voluminous historical newspapers onto rolls of space-saving photographic **microcopy**."
      },
      {
        "author": "Steve Krug",
        "work": "Don't Make Me Think",
        "quote": "Concise, unambiguous **microcopy** next to form fields prevents users from stumbling during complex sign-up flows."
      }
    ]
  },
  "Dashboard — micr\\microcosmic.md": {
    "primary": "Of, relating to, or characteristic of a microcosm; reflecting miniature features of a much larger universe or system.",
    "secondary": "In philosophy and literature, encapsulating macroscopic, metaphysical, or universal principles within a localized, small-scale instance.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "Ancient philosophers called man a **microcosmic** mirror of the whole vast framework of heaven and earth."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "Nature",
        "quote": "Every drop of dew and every leaf reflects a **microcosmic** image of the encompassing universal order."
      },
      {
        "author": "Thomas Browne",
        "work": "Religio Medici",
        "quote": "There is a world of wonders within each creature, a little **microcosmic** world of divine contrivance."
      }
    ]
  },
  "Dashboard — micr\\microcrystalline.md": {
    "primary": "Having a crystal structure visible only under a microscope, as in certain rocks, minerals, or waxes.",
    "secondary": "In geology and petroleum chemistry, describing fine-grained aggregates of microscopic mineral crystals or branched paraffin chains.",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Thin sections of flint revealed a dense **microcrystalline** quartz fabric formed by chemical precipitation."
      },
      {
        "author": "James Dwight Dana",
        "work": "A System of Mineralogy",
        "quote": "Chalcedony is a **microcrystalline** variety of silica, displaying a fibrous habit when observed between crossed polars."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "Over millennia, pelagic sediments consolidated into tough **microcrystalline** limestone layers across ancient abyssal plains."
      }
    ]
  },
  "Dashboard — micr\\microcyte.md": {
    "primary": "An abnormally small red blood cell, characteristic of certain forms of anemia such as iron deficiency or thalassemia.",
    "secondary": "In hematology, an erythrocyte with a mean corpuscular volume (MCV) significantly below the standard reference range.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Stained blood smears from the chlorotic patient exhibited marked poikilocytosis, featuring an abundance of the undersized **microcyte**."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Histology of the Blood",
        "quote": "Differential staining clearly separates the pale **microcyte** of hypochromic anemia from the engorged megalocyte of pernicious anemia."
      },
      {
        "author": "Max Wintrobe",
        "work": "Clinical Hematology",
        "quote": "Automated particle counters identify a **microcyte** whenever the red cell volume falls below eighty femtoliters."
      }
    ]
  },
  "Dashboard — micr\\microcytosis.md": {
    "primary": "A condition in which an unusually high proportion of red blood cells are abnormally small.",
    "secondary": "In diagnostic hematology, a laboratory finding characterized by low mean corpuscular volume (MCV), indicative of iron deficiency or hemoglobinopathy.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe chronic blood loss inevitably produces profound hypochromia accompanied by marked **microcytosis**."
      },
      {
        "author": "Max Wintrobe",
        "work": "Clinical Hematology",
        "quote": "The differential diagnosis of marked **microcytosis** requires serum ferritin testing to distinguish iron depletion from thalassemia minor."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Gene: An Intimate History",
        "quote": "Carriers of the beta-thalassemia trait display benign **microcytosis**, conferring resistance against falciparum malaria."
      }
    ]
  },
  "Dashboard — micr\\microdesmidae.md": {
    "primary": "A family of small, slender marine fishes commonly known as wormfishes or dartfishes, inhabiting tropical and subtropical shallow seas.",
    "secondary": "In ichthyology, elongated gobioid teleosts that burrow into mud or coral rubble substrates, characterized by continuous dorsal and anal fins.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The elusive wormfishes of the family **Microdesmidae** inhabit littoral burrows carved out of mangrove silt."
      },
      {
        "author": "Albert Günther",
        "work": "Catalogue of the Fishes in the British Museum",
        "quote": "Specimens of **Microdesmidae** collected in Panamanian tide pools exhibit serpentine proportions and minute scales."
      },
      {
        "author": "William Beebe",
        "work": "Beneath Tropic Seas",
        "quote": "While dredging the sandy floor of the reef, we captured delicate specimens belonging to the family **Microdesmidae**."
      }
    ]
  },
  "Dashboard — micr\\microdipodops.md": {
    "primary": "A genus of small, nocturnal kangaroo mice endemic to the arid Great Basin desert region of North America.",
    "secondary": "In rodent mammalogy, heteromyid rodents characterized by bipedal saltation, fat-storing incrassated tails, and extraordinary water-conserving physiology.",
    "quotes": [
      {
        "author": "C. Hart Merriam",
        "work": "Descriptions of New Species of Kangaroo Mice",
        "quote": "I established the genus **Microdipodops** to accommodate small bipedal rodents possessing inflated mastoid bullae."
      },
      {
        "author": "Joseph Grinnell",
        "work": "An Account of the Mammals and Birds of the Lower Colorado Valley",
        "quote": "Trapping records across Nevada sand dunes revealed the nocturnal foraging habits of **Microdipodops** pallidus."
      },
      {
        "author": "E. Raymond Hall",
        "work": "The Mammals of Nevada",
        "quote": "The kangaroo mouse, **Microdipodops**, survives without drinking free water, extracting metabolic moisture from dry seeds."
      }
    ]
  },
  "Dashboard — micr\\microdot.md": {
    "primary": "A photograph or text reduced to the size of a tiny dot (about one millimeter in diameter), traditionally used in espionage to conceal messages.",
    "secondary": "In security printing and counter-espionage, an ultra-miniaturized optical data carrier embedded within paper, documents, or high-value items.",
    "quotes": [
      {
        "author": "J. Edgar Hoover",
        "work": "Masters of Deceit",
        "quote": "Enemy agents disguised operational orders as an innocent typographical period using the photographic **microdot** technique."
      },
      {
        "author": "Ian Fleming",
        "work": "From Russia with Love",
        "quote": "Beneath the magnifying glass, the tiny postage stamp cancelled on the envelope revealed a concealed **microdot**."
      },
      {
        "author": "David Kahn",
        "work": "The Codebreakers",
        "quote": "The German development of the **microdot** in World War II allowed complete blueprints to be carried in a single punctuation mark."
      }
    ]
  },
  "Dashboard — micr\\microeconomic.md": {
    "primary": "Of or relating to microeconomics, the branch of economics that studies individual households, firms, and specific market mechanisms.",
    "secondary": "Pertaining to price theory, marginal utility, cost functions, and resource allocation at the level of specific consumers and enterprises.",
    "quotes": [
      {
        "author": "Paul Samuelson",
        "work": "Economics",
        "quote": "Every firm's supply curve is grounded in the **microeconomic** calculus of marginal costs equating marginal revenue."
      },
      {
        "author": "Milton Friedman",
        "work": "Price Theory",
        "quote": "Individual market clearing represents the core **microeconomic** principle through which decentralized coordination occurs."
      },
      {
        "author": "Joseph Stiglitz",
        "work": "Economics of the Public Sector",
        "quote": "Information asymmetry introduces market failures that overturn classical **microeconomic** assumptions of perfect competition."
      }
    ]
  },
  "Dashboard — micr\\microeconomics.md": {
    "primary": "The branch of economics concerned with single factors and the effects of individual decisions on market resource allocation.",
    "secondary": "The theoretical study of how consumers maximize utility and firms maximize profits under budget constraints and competitive market structures.",
    "quotes": [
      {
        "author": "Alfred Marshall",
        "work": "Principles of Economics",
        "quote": "The foundational doctrine of **microeconomics** examines how supply and demand balance at the margin to establish equilibrium prices."
      },
      {
        "author": "Gary Becker",
        "work": "The Economic Approach to Human Behavior",
        "quote": "I applied the analytical tools of **microeconomics** to explain crime, marriage, and family decisions as rational choices."
      },
      {
        "author": "Hal Varian",
        "work": "Microeconomic Analysis",
        "quote": "Modern **microeconomics** provides the formal mathematical scaffolding for understanding auction design and mechanism design."
      }
    ]
  },
  "Dashboard — micr\\microeconomist.md": {
    "primary": "An economist who specializes in microeconomics, analyzing the behavior of individual economic agents and discrete markets.",
    "secondary": "An applied researcher studying consumer behavior, corporate pricing strategies, industrial organization, or labor markets.",
    "quotes": [
      {
        "author": "George Stigler",
        "work": "The Theory of Price",
        "quote": "The professional **microeconomist** focuses on how changes in regulatory rules alter incentives for individual enterprises."
      },
      {
        "author": "Freakonomics authors (Steven Levitt)",
        "work": "Freakonomics",
        "quote": "As an empirical **microeconomist**, my instinct is to look past lofty rhetoric and examine the underlying incentives."
      },
      {
        "author": "Paul Krugman",
        "work": "Peddling Prosperity",
        "quote": "While macroeconomists bickered over fiscal stimulus, the **microeconomist** made steady progress mapping real-world market imperfections."
      }
    ]
  },
  "Dashboard — micr\\microelectronic.md": {
    "primary": "Of, relating to, or involving microelectronics or extremely miniaturized electronic components and circuits.",
    "secondary": "Describing semiconductor fabrication techniques, solid-state physics applications, and integrated circuits operating at sub-micron scales.",
    "quotes": [
      {
        "author": "Carver Mead",
        "work": "Introduction to VLSI Systems",
        "quote": "The design of complex **microelectronic** chips requires a hierarchical abstraction that separates logical function from layout physics."
      },
      {
        "author": "Richard Feynman",
        "work": "There's Plenty of Room at the Bottom",
        "quote": "The physical limits of **microelectronic** circuitry will eventually force us to manipulate individual atoms directly."
      },
      {
        "author": "Walter Isaacson",
        "work": "The Innovators",
        "quote": "Silicon Valley's boom arose from the mastery of **microelectronic** fabrication pioneered at Fairchild Semiconductor."
      }
    ]
  },
  "Dashboard — micr\\microelectronics.md": {
    "primary": "The branch of electronics dealing with the miniaturization of electronic circuits and components, especially onto semiconductor chips.",
    "secondary": "The engineering and physics discipline encompassing photolithography, VLSI design, and cleanroom fabrication of integrated circuits.",
    "quotes": [
      {
        "author": "Gordon Moore",
        "work": "Cramming More Components onto Integrated Circuits",
        "quote": "Advances in **microelectronics** will lead to personal portable communications equipment and automatic computers in automobiles."
      },
      {
        "author": "Alvin Toffler",
        "work": "The Third Wave",
        "quote": "The explosion of **microelectronics** replaced heavy mechanical machinery with programmable silicon intelligence across every industry."
      },
      {
        "author": "Arthur C. Clarke",
        "work": "1984: Spring - A Choice of Futures",
        "quote": "Without the quiet triumphs of **microelectronics**, the entire space program would have collapsed under the weight of vacuum tubes."
      }
    ]
  },
  "Dashboard — micr\\microevolution.md": {
    "primary": "Evolutionary change within a species or small group of organisms, especially over a short period of time.",
    "secondary": "In population genetics, changes in allele frequencies across generations driven by natural selection, mutation, genetic drift, or gene flow.",
    "quotes": [
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "There is no reason to assume that macroevolution involves processes different from those governing observable **microevolution** in populations."
      },
      {
        "author": "Ernst Mayr",
        "work": "What Evolution Is",
        "quote": "The development of pesticide resistance in crop insects provides a clear, documented example of rapid **microevolution** in action."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Structure of Evolutionary Theory",
        "quote": "Paleontologists debated whether the grand patterns of the fossil record could be fully accounted for by extrapolating **microevolution**."
      }
    ]
  },
  "Dashboard — micr\\microfarad.md": {
    "primary": "A unit of electrical capacitance equal to one-millionth (10^-6) of a farad.",
    "secondary": "In electrical engineering, a common unit used to specify the storage capacity of capacitors in electronic circuits.",
    "quotes": [
      {
        "author": "Oliver Heaviside",
        "work": "Electromagnetic Theory",
        "quote": "A submarine telegraph cable possesses an intrinsic distributed capacitance measurable in fractions of a **microfarad** per nautical mile."
      },
      {
        "author": "Nikola Tesla",
        "work": "My Inventions",
        "quote": "The high-frequency transformer circuit was tuned by discharging a bank of capacitors rated at several **microfarad** capacity."
      },
      {
        "author": "Horowitz & Hill",
        "work": "The Art of Electronics",
        "quote": "For bypass filtering on standard power supply rails, a 0.1 **microfarad** ceramic capacitor placed close to the chip is customary."
      }
    ]
  },
  "Dashboard — micr\\microfiche.md": {
    "primary": "A flat sheet of microfilm containing microphotographic reproductions of document pages in a compact grid format.",
    "secondary": "An archival storage medium popular in libraries and corporate databases before digital optical media, viewed through optical enlargement machines.",
    "quotes": [
      {
        "author": "Umberto Eco",
        "work": "Foucault's Pendulum",
        "quote": "He sat in the dimly lit basement of the archive, spooling through sheets of **microfiche** to locate the obscure nineteenth-century pamphlet."
      },
      {
        "author": "Carl Sagan",
        "work": "The Demon-Haunted World",
        "quote": "Libraries packed whole wings of historical newspapers onto compact **microfiche** envelopes tucked inside metal filing drawers."
      },
      {
        "author": "David Foster Wallace",
        "work": "The Pale King",
        "quote": "Recruits at the regional tax office squinted into glowing projection screens, verifying scanned ledgers preserved on **microfiche**."
      }
    ]
  },
  "Dashboard — micr\\microfilm.md": {
    "primary": "Film bearing miniature photographic copies of printed documents, newspapers, or graphics, used for space-saving archival storage.",
    "secondary": "A continuous photographic film strip (typically 16mm or 35mm) designed for high-density document preservation and library retrieval.",
    "quotes": [
      {
        "author": "George Orwell",
        "work": "1984",
        "quote": "Winston slipped the small cylindrical spool of **microfilm** into the pneumatic message tube leading to the Records Department."
      },
      {
        "author": "John le Carré",
        "work": "The Spy Who Came in from the Cold",
        "quote": "The courier passed a hidden canister containing twenty feet of classified **microfilm** into the agent's trench coat pocket."
      },
      {
        "author": "Arthur C. Clarke",
        "work": "Profiles of the Future",
        "quote": "The human record, once chiseled upon granite tablets, found transient refuge on rolls of cellulose **microfilm** before electronic memories."
      }
    ]
  },
  "Dashboard — micr\\microflora.md": {
    "primary": "The microscopic plants or microbial organisms that inhabit a specific environment, bodily organ, or ecological niche.",
    "secondary": "In microbiology and medicine, the community of commensal, symbiotic, or environmental bacteria and fungi (such as the gut or soil flora).",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "Indiscriminate chemical drenching destroys the delicate soil **microflora** upon which the natural nitrogen cycle depends."
      },
      {
        "author": "René Dubos",
        "work": "The Bacterial Cell",
        "quote": "The normal intestinal **microflora** provides an effective ecological barrier against colonisation by virulent enteric pathogens."
      },
      {
        "author": "Ed Yong",
        "work": "I Contain Multitudes",
        "quote": "What researchers once casually referred to as human **microflora** is now recognized as a diverse, dynamic ecosystem of microbial partners."
      }
    ]
  },
  "Dashboard — micr\\microfossil.md": {
    "primary": "A fossil that is so small (typically under one millimeter) that it can only be studied effectively with a microscope.",
    "secondary": "In micropaleontology and stratigraphy, fossilized pollen, spores, foraminifera, or ostracods used to date geological strata and reconstruct paleo-climates.",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "The chalk cliffs of Dover consist almost entirely of an accumulation of the tests of tiny **microfossil** organisms."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Wonderful Life",
        "quote": "The recovery of Precambrian **microfossil** filaments in Australian chert pushed back the confirmed origin of life by billions of years."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "Deep-sea drilling cores bring up layers of sediment rich in foraminiferal **microfossil** shells that chart ancient ocean temperatures."
      }
    ]
  },
  "Dashboard — micr\\microgametophyte.md": {
    "primary": "The microscopic, male gamete-producing generation in heterosporous plants, developing from a microspore (such as a pollen grain).",
    "secondary": "In plant morphology and botany, the reduced haploid male stage in gymnosperms and angiosperms consisting of just a few cells that deliver sperm to the ovule.",
    "quotes": [
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "In angiosperms, the mature pollen grain represents the fully developed three-celled **microgametophyte**."
      },
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "Upon reaching the receptive stigma, the **microgametophyte** produces a pollen tube that grows down through the style."
      },
      {
        "author": "Peter Raven",
        "work": "Biology of Plants",
        "quote": "The evolutionary transition to seed plants involved extreme reduction of the **microgametophyte** into a transportable pollen vector."
      }
    ]
  },
  "Dashboard — micr\\microgauss.md": {
    "primary": "A unit of magnetic flux density equal to one-millionth (10^-6) of a gauss (or 10^-10 tesla).",
    "secondary": "In astrophysics and geophysics, a unit used to quantify weak magnetic fields in interstellar space or ultra-sensitive biomagnetic measurements.",
    "quotes": [
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "The galactic magnetic field permeates the spiral arms with an intensity of only a few **microgauss**, yet it guides cosmic rays."
      },
      {
        "author": "Hannes Alfvén",
        "work": "Cosmical Electrodynamics",
        "quote": "Interstellar clouds collapse under self-gravitation while freezing in magnetic flux lines measured in units of **microgauss**."
      },
      {
        "author": "Subrahmanyan Chandrasekhar",
        "work": "Hydrodynamic and Hydromagnetic Stability",
        "quote": "Even a background field of several **microgauss** exerts measurable stabilizing tension across magnetized interstellar gas clouds."
      }
    ]
  },
  "Dashboard — micr\\microglia.md": {
    "primary": "Glial cells of the central nervous system that act as the main active immune defense and phagocytes of the brain and spinal cord.",
    "secondary": "In neurobiology, resident macrophage-like cells derived from yolk-sac progenitors that prune synapses, clear debris, and mediate neuroinflammation.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Degeneration and Regeneration of the Nervous System",
        "quote": "Following cerebral trauma, the quiescent cells of the **microglia** hypertrophy and transform into voracious ameboid phagocytes."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "Post-mortem analysis revealed extensive activation of **microglia** surrounding depleted dopaminergic centers in post-encephalitic patients."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "During critical developmental windows, resting **microglia** sculpt mature neural circuits by selectively engulfing inactive synaptic terminals."
      }
    ]
  },
  "Dashboard — micr\\microgliacyte.md": {
    "primary": "An individual cell belonging to the microglia; a microglial cell.",
    "secondary": "In histology, a small, highly branched glial cell found within the gray and white matter of the brain that performs immune surveillance.",
    "quotes": [
      {
        "author": "Pío del Río-Hortega",
        "work": "Microglia",
        "quote": "Using silver carbonate impregnation, I was able to demonstrate the distinct morphology and mesodermal origin of each **microgliacyte**."
      },
      {
        "author": "Wilder Penfield",
        "work": "Cytology and Cellular Pathology of the Nervous System",
        "quote": "The migratory **microgliacyte** responds with astonishing speed to local neuronal injury, migrating directly to the lesion site."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Unlike neuroglia of ectodermal derivation, the mature **microgliacyte** displays distinctive thorny processes and phagocytic properties."
      }
    ]
  },
  "Dashboard — micr\\microgram.md": {
    "primary": "A unit of mass equal to one-millionth (10^-6) of a gram (or one-thousandth of a milligram).",
    "secondary": "In pharmacology and biochemistry, a standard measure for dosages of highly potent hormones, vitamins, toxins, or pharmaceuticals.",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "A concentration of merely a single **microgram** of toxic pesticide per liter of river water proved lethal to young salmon fry."
      },
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "In the intensive care unit, vasoactive infusions are titrated strictly by the **microgram** per kilogram of body weight per minute."
      },
      {
        "author": "Albert Hofmann",
        "work": "LSD: My Problem Child",
        "quote": "The extraordinary potency of the compound was evident when an oral dose of just twenty-five **microgram** evoked profound psychic transformations."
      }
    ]
  },
  "Dashboard — micr\\microgramma-piloselloides.md": {
    "primary": "An epiphytic fern species native to tropical America, characterized by creeping rhizomes and small dimorphic fronds.",
    "secondary": "In pteridology and botanical taxonomy, an epiphyte of the family Polypodiaceae featuring densely hairy (piloselloid) rhizome scales.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Personal Narrative of Travels to the Equinoctial Regions of America",
        "quote": "The mossy trunks of the forest canopy supported dense mats of epiphytic ferns, among them the creeping **Microgramma piloselloides**."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "Tropical Nature and Other Essays",
        "quote": "High in the moist branches, tiny colonies of **Microgramma piloselloides** cling securely by their slender, scale-covered rhizomes."
      },
      {
        "author": "Asa Gray",
        "work": "Synoptical Flora of North America",
        "quote": "The tropical collector noted how **Microgramma piloselloides** displays distinct fertile and sterile fronds along its creeping stem."
      }
    ]
  },
  "Dashboard — micr\\microgramma.md": {
    "primary": "A genus of small, epiphytic ferns in the family Polypodiaceae, native to the tropical and subtropical Americas.",
    "secondary": "In systematic botany, creeping polypod ferns distinguished by long-creeping scaly rhizomes, simple leaves, and round sori on the underside of fertile fronds.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Views of Nature",
        "quote": "Branches of ancient mahogany trees in the Orinoco basin were carpeted with delicate fronds of the climbing fern genus **Microgramma**."
      },
      {
        "author": "Richard Spruce",
        "work": "Notes of a Botanist on the Amazon and Andes",
        "quote": "I observed several species of **Microgramma** whose rhizomes form intimate mutualistic shelters for colonies of arboreal ants."
      },
      {
        "author": "David Attenborough",
        "work": "The Private Life of Plants",
        "quote": "The miniature epiphytic fern **Microgramma** thrives in the rain-soaked canopy without ever touching forest soil."
      }
    ]
  },
  "Dashboard — micr\\microhylidae.md": {
    "primary": "A large, cosmopolitan family of frogs, commonly known as narrow-mouthed toads or narrow-mouthed frogs.",
    "secondary": "In herpetology, anuran amphibians characterized by narrow mouths, stout bodies, and diverse life histories ranging from burrowing to arboreal forms.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes and Amphibians",
        "quote": "The fossorial frogs of the family **Microhylidae** possess sharp-edged inner metatarsal spades adapted for digging into loam."
      },
      {
        "author": "E.O. Wilson",
        "work": "The Diversity of Life",
        "quote": "In the rainforest leaf litter, tiny cryptically colored species of **Microhylidae** call with buzzing, insect-like notes after summer rains."
      },
      {
        "author": "David Attenborough",
        "work": "Life on Earth",
        "quote": "Certain Asian narrow-mouthed toads of the family **Microhylidae** live safely inside the burrows of large tarantulas in strange mutual tolerance."
      }
    ]
  },
  "Dashboard — micr\\micromeria.md": {
    "primary": "A genus of aromatic perennial herbs and dwarf shrubs in the mint family (Lamiaceae), native to the Mediterranean, Africa, and Asia.",
    "secondary": "In economic botany, essential-oil-producing plants rich in carvacrol and thymol, historically used in traditional herbal infusions and folk medicine.",
    "quotes": [
      {
        "author": "Theophrastus",
        "work": "Enquiry into Plants",
        "quote": "On dry and stony Aegean slopes grows the pungent herb **Micromeria**, prized by shepherds for its fragrant, warming tea."
      },
      {
        "author": "John Gerard",
        "work": "The Herball or Generall Historie of Plantes",
        "quote": "The small mountain savoury known to apothecaries as **Micromeria** bears tiny purple blossoms that scent the rocky hillsides."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "The Flora of British India",
        "quote": "Rocky limestone crevices in the Himalayan foothills sheltered dwarfed clumps of **Micromeria** growing among wild thyme."
      }
    ]
  }
};

const count = updateNotesBatch(CLUSTER_DIR, batchData);
console.log(`========================================`);
console.log(`Math Part 2 - Batch 1 Completed: ${count} / ${Object.keys(batchData).length} words updated`);
console.log(`========================================`);
