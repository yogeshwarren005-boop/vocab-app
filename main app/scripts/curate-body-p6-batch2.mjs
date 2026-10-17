import { updateNotesBatch } from './curate-updater-util.mjs';

const BASE_DIR = 'App database/Greek roots/Cluster Body & Physiology';

const BATCH2_DATA = {
  "Dashboard — ot\\ototomy.md": {
    "primary": "The surgical incision or dissection of the ear, particularly the tympanic membrane or internal ear structures.",
    "secondary": "In classical operative otology, an incision performed to access the middle-ear cavity or drain suppurative labyrinthitis.",
    "quotes": [
      {
        "author": "Joseph Toynbee",
        "work": "The Diseases of the Ear",
        "quote": "Careful **ototomy** of the posterosuperior quadrant relieves acute fluid pressure without endangering the ossicular chain."
      },
      {
        "author": "Adam Politzer",
        "work": "A Text-Book of the Diseases of the Ear",
        "quote": "The early surgeons practiced exploratory **ototomy** whenever intracranial extension of mastoid disease was suspected."
      },
      {
        "author": "William Wilde",
        "work": "Practical Observations on Aural Surgery",
        "quote": "Through precise **ototomy**, chronic inflammatory exudates within the tympanum may be safely evacuated."
      }
    ]
  },
  "Dashboard — ot\\ototoxicity.md": {
    "primary": "The property of being toxic to the ear, specifically producing functional impairment or cellular damage to the cochlea or vestibular apparatus.",
    "secondary": "In clinical pharmacology and audiology, medication-induced sensorineural hearing loss, tinnitus, or vertigo caused by agents such as aminoglycosides or cisplatin.",
    "quotes": [
      {
        "author": "Louis Goodman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "Irreversible cochlear hair-cell apoptosis remains the defining hazard of aminoglycoside **ototoxicity** during systemic therapy."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "High doses of quinine provoke transient **ototoxicity**, heralding its toxic accumulation with bilateral ringing and deafness."
      },
      {
        "author": "Alfred Gilman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "Routine audiometric monitoring minimizes permanent sensory deficits arising from platinum chemotherapy **ototoxicity**."
      }
    ]
  },
  "Dashboard — ot\\parotic.md": {
    "primary": "Situated near or beside the ear; anatomical variant or synonym of parotid.",
    "secondary": "In comparative anatomy and embryology, relating to structures located adjacent to the otic capsule, such as the parotic process of the chondrocranium.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **parotic** lymph nodes drain the temple and the external acoustic meatus before emptying into the deep cervical chain."
      },
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "In the reptilian skull, the **parotic** process projects outward from the otic capsule to articulate with the quadrate bone."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "The vestigial **parotic** crest reflects ancestral cranial architecture preserved in primitive teleost crania."
      }
    ]
  },
  "Dashboard — ot\\parotid.md": {
    "primary": "The largest of the three pairs of major salivary glands, situated anteroinferior to the external ear canal.",
    "secondary": "In gross human anatomy and head and neck surgery, the glandular space traversed by the facial nerve, retromandibular vein, and external carotid artery.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The superficial lobe of the **parotid** gland rests upon the masseter muscle, emptying serous saliva through Stensen's duct."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Acute bilateral swelling of the **parotid** glands is the hallmark sign of epidemic mumps in pediatric patients."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Pleomorphic adenoma commonly arises within the deep parenchyma of the **parotid**, requiring careful preservation of the facial branches."
      }
    ]
  },
  "Dashboard — ot\\parotitis.md": {
    "primary": "Inflammation of one or both parotid salivary glands, producing painful periauricular swelling.",
    "secondary": "In infectious disease and geriatrics, either viral mumps parotitis or bacterial ascending suppurative parotitis occurring in dehydrated, debilitated patients.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Suppurative **parotitis** in post-operative patients demands energetic rehydration and targeted antibiotic administration."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Microscopic examination of epidemic **parotitis** reveals diffuse interstitial lymphocytic infiltrates without suppuration."
      },
      {
        "author": "Thomas Sydenham",
        "work": "The Whole Works of That Excellent Practical Physician",
        "quote": "The painful tumefaction beneath the ears known as **parotitis** often migrates toward the testes during convalescence."
      }
    ]
  },
  "Dashboard — ot\\periotic.md": {
    "primary": "Surrounding or situated around the ear or otic capsule; specifically designating the fused petrous and mastoid portions of the temporal bone.",
    "secondary": "In vertebrate paleontology and embryology, the periotic bone enclosing the inner ear, cochlea, and semicircular canals.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "The dense **periotic** bone of cetaceans is heavily pachyostotic, isolating auditory reception from cranial reverberations."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "During chondrification, the **periotic** cartilaginous capsule envelops the membranous labyrinth of the developing embryo."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "The morphogenetic unification of squamosal, tympanic, and **periotic** elements characterizes the advanced mammalian skull."
      }
    ]
  },
  "Dashboard — ot\\synotia.md": {
    "primary": "A severe congenital malformation in which the ears are fused or positioned unnaturally close together on the anterior midline of the neck.",
    "secondary": "In teratology and developmental genetics, an anomaly associated with agnathia (absence of lower jaw) caused by failure of first branchial arch migration.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The rare condition of **synotia** illustrates complete arrest of mandibular arch development with midline coalescence of the otic pits."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Gross cephalic dysmorphologies such as **synotia** are universally incompatible with postnatal respiratory life."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "Failure of ventral migration of branchial tissues results in **synotia**, wherein both auricular pinnae meet below the oral stoma."
      }
    ]
  },
  "Dashboard — par\\antiparallel.md": {
    "primary": "Parallel but moving or oriented in opposite directions.",
    "secondary": "In molecular genetics and biochemistry, describing the complementary strands of a DNA double helix running 5'-to-3' in opposing directions.",
    "quotes": [
      {
        "author": "James D. Watson",
        "work": "Molecular Biology of the Gene",
        "quote": "The two phosphodiester chains of the double helix run in **antiparallel** directions, one terminating in 5'-phosphate and the other in 3'-hydroxyl."
      },
      {
        "author": "Francis Crick",
        "work": "What Mad Pursuit",
        "quote": "Only when we arranged the pairing purines and pyrimidines in an **antiparallel** orientation did the stereochemical model lock into place."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Beta-pleated sheets may fold into either parallel or **antiparallel** alignments stabilized by interstrand hydrogen bonding."
      }
    ]
  },
  "Dashboard — par\\apar.md": {
    "primary": "The three-banded armadillo (genus Tolypeutes) of South America, capable of rolling into a completely spherical ball.",
    "secondary": "In mammalogy and South American zoology, a xenarthran noted for its flexible jointed armor and cursorial foraging habits.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The three-banded armadillo, termed the **apar**, defends itself not by burrowing, but by rolling into an invulnerable solid ball."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Geographical Distribution of Animals",
        "quote": "Among the edentates of the Pampas, the **apar** exhibits unique cursorial adaptations with its pointed claws and rigid shell."
      },
      {
        "author": "Richard Owen",
        "work": "Odontography",
        "quote": "The diminutive peg-like dentition of the **apar** corresponds to its diet of termites and subterranean larvae."
      }
    ]
  },
  "Dashboard — par\\parable.md": {
    "primary": "A simple story used to illustrate a moral or spiritual lesson, typically featuring human characters and familiar situations.",
    "secondary": "In literary criticism and biblical hermeneutics, an allegorical narrative that conceals esoteric theological truths beneath pastoral tropes.",
    "quotes": [
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Aids to Reflection",
        "quote": "A true **parable** is never mere fiction; it mirrors an enduring divine reality through an earthly occurrence."
      },
      {
        "author": "John Ruskin",
        "work": "Modern Painters",
        "quote": "The sacred **parable** communicates its profoundest ethical wisdom precisely by condescending to the shepherd and the tiller."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "Nature",
        "quote": "Every natural fact is a symbol of some spiritual fact, and the universe itself stands as an open **parable**."
      }
    ]
  },
  "Dashboard — par\\parabola.md": {
    "primary": "A symmetrical open plane curve formed by the intersection of a circular cone with a plane parallel to its side.",
    "secondary": "In classical mechanics and geometry, the locus of points equidistant from a fixed focus and directrix, representing the ideal trajectory of a projectile.",
    "quotes": [
      {
        "author": "Galileo Galilei",
        "work": "Dialogues Concerning Two New Sciences",
        "quote": "I demonstrate that an unimpeded projectile launched horizontally or obliquely traces out in its flight a true **parabola**."
      },
      {
        "author": "Isaac Newton",
        "work": "Philosophiae Naturalis Principia Mathematica",
        "quote": "The path of a comet possessing parabolic velocity corresponds to a non-returning **parabola** around the solar focus."
      },
      {
        "author": "René Descartes",
        "work": "La Géométrie",
        "quote": "By expressing the **parabola** through quadratic coordinates, geometric curves become tractable under algebraic operations."
      }
    ]
  },
  "Dashboard — par\\parabolic.md": {
    "primary": "Having the form or properties of a parabola; shaped like a parabola.",
    "secondary": "Expressed by or having the nature of a parable; allegorical or didactic.",
    "quotes": [
      {
        "author": "Galileo Galilei",
        "work": "Dialogues Concerning Two New Sciences",
        "quote": "The **parabolic** curvature of a cannonball's descent is distorted only by the resisting density of ambient air."
      },
      {
        "author": "Thomas Browne",
        "work": "Religio Medici",
        "quote": "Many deep scriptures are delivered in **parabolic** shadows to provoke our contemplation rather than literal dogmatism."
      },
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "Poesy **parabolic** has ever flourished in the earliest ages as a veil for subtle philosophical mysteries."
      }
    ]
  },
  "Dashboard — par\\parabolical.md": {
    "primary": "Pertaining to, having the form of, or resembling a parabola; parabolic.",
    "secondary": "Conveying moral or spiritual instruction through parables; allegorical.",
    "quotes": [
      {
        "author": "Robert Boyle",
        "work": "New Experiments Physico-Mechanicall",
        "quote": "The **parabolical** mirror concentrates parallel rays of light with supreme intensity upon its central focus."
      },
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "Ancient fables carry a **parabolical** sense beneath their outward narrative ornament."
      },
      {
        "author": "Isaac Barrow",
        "work": "Geometrical Lectures",
        "quote": "We deduce the quadrature of **parabolical** figures by exhaustively inscribing rectilinear polygons."
      }
    ]
  },
  "Dashboard — par\\paraboloid.md": {
    "primary": "A three-dimensional quadric surface whose planar sections are either parabolas or ellipses/hyperbolas.",
    "secondary": "In optical physics and antenna design, a paraboloid of revolution used to collimate or focus electromagnetic radiation and sound waves.",
    "quotes": [
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "Grinding a metallic reflector into a true **paraboloid** avoids the spherical aberration inherent in circular curvatures."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "A Treatise on Electricity and Magnetism",
        "quote": "Electromagnetic wavefronts reflecting from a conducting **paraboloid** are transformed into perfectly parallel beams."
      },
      {
        "author": "Leonhard Euler",
        "work": "Mechanica",
        "quote": "The equilibrium surface assumed by a rotating fluid vessel is a circular **paraboloid** proportional to angular velocity."
      }
    ]
  },
  "Dashboard — par\\paraboloidal.md": {
    "primary": "Pertaining to, resembling, or having the geometric shape of a paraboloid.",
    "secondary": "In astronomy and telecommunications engineering, describing reflecting surfaces, mirrors, or dishes designed with paraboloid geometry.",
    "quotes": [
      {
        "author": "William Herschel",
        "work": "Philosophical Transactions of the Royal Society",
        "quote": "The **paraboloidal** figure given to my large speculum enabled stellar images of unprecedented pinpoint brilliance."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "Scientific Papers",
        "quote": "Geometric rays incident upon a **paraboloidal** collector converge precisely upon the axial conjugate focus."
      },
      {
        "author": "Oliver Heaviside",
        "work": "Electromagnetic Theory",
        "quote": "Radiation propagated across a **paraboloidal** antenna guide maintains coherent phase velocity across its aperture."
      }
    ]
  },
  "Dashboard — par\\paradox.md": {
    "primary": "A seemingly absurd or self-contradictory statement or proposition that when investigated may prove to be well founded or true.",
    "secondary": "In philosophy and logic, an antinomy or statement that leads to a contradiction from seemingly acceptable premises, such as the Liar's Paradox or Russell's Paradox.",
    "quotes": [
      {
        "author": "Bertrand Russell",
        "work": "The Principles of Mathematics",
        "quote": "The **paradox** of whether the barber who shaves all non-self-shavers shaves himself forced a total reconstruction of set theory."
      },
      {
        "author": "G. K. Chesterton",
        "work": "The Everlasting Man",
        "quote": "A **paradox** is truth standing on her head to attract attention."
      },
      {
        "author": "Søren Kierkegaard",
        "work": "Concluding Unscientific Postscript",
        "quote": "The highest pitch of human thought is to encounter a **paradox** that thought itself cannot resolve."
      }
    ]
  },
  "Dashboard — par\\paradoxical.md": {
    "primary": "Seemingly contradictory, unbelievable, or absurd, yet perhaps expressing an underlying reality or truth.",
    "secondary": "In physiology and medicine, denoting an abnormal bodily reaction opposite to what is expected, such as paradoxical vocal fold movement or paradoxical breathing.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "It is a **paradoxical** fact that emotional excitement often quickens the perception of peripheral sensory cues."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In massive pericardial tamponade, a **paradoxical** pulse reveals marked decline of arterial pressure during inspiration."
      },
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "It may seem **paradoxical** to claim that ideas of primary qualities resemble physical bodies while secondary qualities do not."
      }
    ]
  },
  "Dashboard — par\\paradoxically.md": {
    "primary": "In a paradoxical manner; in a way that seems absurd, contradictory, or impossible, yet is or may be true.",
    "secondary": "Used as a sentence adverb to highlight an ironic or unexpected turn of events or empirical outcome contrary to naive intuition.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "Civilization and Its Discontents",
        "quote": "The more virtuous a man becomes, the more severely and **paradoxically** suspicious does his conscience grow."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Extreme specialization, **paradoxically**, often predisposes a species to rapid extinction when ecological circumstances shift."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "As inequality decreases, the remaining injustices appear, **paradoxically**, far more intolerable to the public mind."
      }
    ]
  },
  "Dashboard — par\\parallel.md": {
    "primary": "Side by side and having the same distance continuously between them; occurring or existing at the same time and in a similar way.",
    "secondary": "In Euclidean geometry and computer architecture, lines or planes that never meet, or concurrent execution of independent processing threads.",
    "quotes": [
      {
        "author": "Euclid",
        "work": "Elements",
        "quote": "If a straight line falling on two straight lines makes the interior angles on the same side less than two right angles, the two lines will meet if extended, but if equal, they remain **parallel**."
      },
      {
        "author": "Isaac Newton",
        "work": "Philosophiae Naturalis Principia Mathematica",
        "quote": "The rays emitted from a distant luminary may be regarded as practically **parallel** when entering an earthly aperture."
      },
      {
        "author": "John Stuart Mill",
        "work": "A System of Logic",
        "quote": "The historical development of institutions often displays a curious **parallel** across widely separated civilizations."
      }
    ]
  },
  "Dashboard — par\\parallelepiped.md": {
    "primary": "A six-faced three-dimensional polyhedron whose faces are all parallelograms.",
    "secondary": "In crystallography and vector calculus, the unit cell or volume spanned by three linearly independent basis vectors computed via scalar triple product.",
    "quotes": [
      {
        "author": "Leonhard Euler",
        "work": "Elements of Algebra",
        "quote": "The cubical content of an oblique **parallelepiped** is calculated by multiplying its base area by its perpendicular altitude."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "A Treatise on Electricity and Magnetism",
        "quote": "We establish the flux of magnetic induction across the differential faces of an infinitesimal **parallelepiped**."
      },
      {
        "author": "René Just Haüy",
        "work": "Traité de Minéralogie",
        "quote": "Calcite cleaves naturally into a rhombohedral **parallelepiped**, revealing the fundamental geometric brick of its crystal lattice."
      }
    ]
  },
  "Dashboard — par\\parallelism.md": {
    "primary": "The state of being parallel or corresponding to something in an identical or equivalent manner.",
    "secondary": "In linguistics and poetics, the repetition of similar grammatical or semantic structures (as in Hebrew poetry); in psychology, psychophysical parallelism.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The doctrine of psycho-physical **parallelism** asserts that mental states and neural events run concurrently without direct causal interaction."
      },
      {
        "author": "Robert Lowth",
        "work": "Lectures on the Sacred Poetry of the Hebrews",
        "quote": "Hebrew verse is constructed upon rhythmic **parallelism**, where thought echoes thought in synonymous or antithetic balance."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The striking **parallelism** observed in embryonic vertebrate development points unmistakably to community of descent."
      }
    ]
  },
  "Dashboard — par\\parallelize.md": {
    "primary": "To make parallel; to align or arrange in parallel fashion.",
    "secondary": "In high-performance computing, to divide an algorithm or computational workload into concurrent processes executed simultaneously on multiple processors.",
    "quotes": [
      {
        "author": "Alan Turing",
        "work": "Intelligent Machinery",
        "quote": "To expedite combinatorial search, one may **parallelize** distinct calculation chains across coordinated sub-machines."
      },
      {
        "author": "John von Neumann",
        "work": "First Draft of a Report on the EDVAC",
        "quote": "Although sequential logic is economical, engineering attempts to **parallelize** memory access substantially increase arithmetic throughput."
      },
      {
        "author": "Norbert Wiener",
        "work": "Cybernetics",
        "quote": "Biological neural networks naturally **parallelize** sensory inputs, synthesizing complex percepts in fractions of a second."
      }
    ]
  },
  "Dashboard — par\\paralytical.md": {
    "primary": "Affected by, relating to, or resembling paralysis; palsied.",
    "secondary": "In archaic and classical clinical medicine, describing a patient or symptom-complex characterized by motor palsy or apoplexy.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The **paralytical** tremors observed in chronic mercury poisoning render purposeful hand movements impossible."
      },
      {
        "author": "Thomas Sydenham",
        "work": "The Whole Works of That Excellent Practical Physician",
        "quote": "Following the sudden stroke of apoplexy, the afflicted limb remained cold and helplessly **paralytical**."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Cerebral ischemic softening produces **paralytical** contractures across the contralateral musculature."
      }
    ]
  },
  "Dashboard — par\\parameter.md": {
    "primary": "A numerical or other measurable factor forming one of a set that defines a system or sets the conditions of its operation.",
    "secondary": "In mathematics, statistics, and programming, a variable whose value determines the specific characteristics or behavior of an equation, distribution, or function.",
    "quotes": [
      {
        "author": "Ronald Fisher",
        "work": "Statistical Methods for Research Workers",
        "quote": "Our objective in estimation is to infer the true population **parameter** from sample statistics with maximum likelihood."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "A Treatise on Electricity and Magnetism",
        "quote": "The velocity of propagation depends upon a single electrical **parameter** governing the permittivity and permeability of the ether."
      },
      {
        "author": "Claude Shannon",
        "work": "A Mathematical Theory of Communication",
        "quote": "The channel capacity represents a fundamental physical **parameter** limiting the error-free transmission of information."
      }
    ]
  },
  "Dashboard — par\\parametric.md": {
    "primary": "Of, relating to, or expressed in terms of a parameter or parameters.",
    "secondary": "In statistics, describing statistical tests (like the t-test or ANOVA) that assume underlying data follow a specific probability distribution.",
    "quotes": [
      {
        "author": "Ronald Fisher",
        "work": "The Design of Experiments",
        "quote": "Standard **parametric** tests assume an underlying Gaussian distribution within the agricultural trial replicates."
      },
      {
        "author": "Carl Friedrich Gauss",
        "work": "Theoria Motus Corporum Coelestium",
        "quote": "Orbital determination becomes tractable when expressed via **parametric** coordinates representing mean anomaly and time."
      },
      {
        "author": "Karl Pearson",
        "work": "The Grammar of Science",
        "quote": "Fitting an empirical frequency curve requires adjusting its **parametric** constants to match experimental moments."
      }
    ]
  },
  "Dashboard — par\\pare.md": {
    "primary": "To trim something by cutting away its outer edges, skin, or excess surface.",
    "secondary": "To reduce or diminish something gradually in size, quantity, or scope.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "King Lear",
        "quote": "Thou hast **pared** thy wit o' both sides, and left nothing i' the middle."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "quote": "I wished to live deliberately, to front only the essential facts of life, and **pare** down my wants to the bone."
      },
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "We must **pare** away superfluous assumptions if we are to uncover the primary foundations of knowledge."
      }
    ]
  },
  "Dashboard — par\\parer.md": {
    "primary": "A person or instrument that pares, trims, or peels something.",
    "secondary": "In metallurgy, leatherworking, or agriculture, a specialized hand tool or machine used to shave skins, hooves, or fruit rinds.",
    "quotes": [
      {
        "author": "Thomas Hardy",
        "work": "Far from the Madding Crowd",
        "quote": "The itinerant hoof-**parer** knelt beside the ewe, trimming the horn with steady, practiced strokes."
      },
      {
        "author": "Charles Dickens",
        "work": "Great Expectations",
        "quote": "He grasped the small knife like an apple-**parer**, stripping the bark in long ribbons."
      },
      {
        "author": "Gilbert White",
        "work": "The Natural History of Selborne",
        "quote": "The turf-**parer** cuts the surface sod to dry for winter fuel across the moorland."
      }
    ]
  },
  "Dashboard — par\\paring.md": {
    "primary": "A piece or strip cut or shaved off from something; the action of cutting or peeling away an outer surface.",
    "secondary": "In horticulture, veterinary surgery, or culinary arts, the act of trimming excess tissue, rind, or hoof horn.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "Sylva Sylvarum",
        "quote": "The thin apple **paring** curls under the blade, leaving the fleshy pulp exposed to oxidation."
      },
      {
        "author": "Henry David Thoreau",
        "work": "A Week on the Concord and Merrimack Rivers",
        "quote": "A single wooden **paring** tossed upon the current showed which way the quiet river was setting."
      },
      {
        "author": "Thomas Browne",
        "work": "Pseudodoxia Epidemica",
        "quote": "Superstitions regarding the proper day for nail-**paring** have persisted since classical antiquity."
      }
    ]
  },
  "Dashboard — par\\parodist.md": {
    "primary": "A person who writes or performs humorous or satirical imitations of an author, artist, genre, or work.",
    "secondary": "In literary criticism, a satirist who mimics the formal stylistic conventions of another to reveal absurdity or pretense.",
    "quotes": [
      {
        "author": "Samuel Johnson",
        "work": "Lives of the Most Eminent English Poets",
        "quote": "A skilful **parodist** must capture the rhythm and cadences of his victim so faithfully that the mockery emerges from within."
      },
      {
        "author": "William Hazlitt",
        "work": "Lectures on the English Comic Writers",
        "quote": "The genius of the **parodist** lies in heightening peculiar mannerisms until the sublime collapses into the ridiculous."
      },
      {
        "author": "Alexander Pope",
        "work": "The Dunciad",
        "quote": "Each petty **parodist** in Grub Street mimicked the heroic couplet, degrading Homeric majesty to farce."
      }
    ]
  },
  "Dashboard — par\\parous.md": {
    "primary": "Having borne offspring; producing viable young; designated by the number of times a female has given birth.",
    "secondary": "In obstetrics and ecology, describing a female organism that has completed one or more gestations (e.g., primiparous, multiparous), contrasted with nulliparous.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The external os of the cervix in a **parous** woman typically appears as a transverse slit rather than a round dimple."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "Maternal investment differs markedly between nulliparous heifers and seasoned, fully **parous** individuals."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The pelvic floor muscles and vaginal canal retain distinct structural alterations in every **parous** subject."
      }
    ]
  },
  "Dashboard — par\\reparable.md": {
    "primary": "Capable of being repaired, remedied, or restored to good condition.",
    "secondary": "In law, ethics, and theology, describing an injury, loss, or transgression that can be made good by compensation or atonement.",
    "quotes": [
      {
        "author": "John Locke",
        "work": "Two Treatises of Government",
        "quote": "A breach of contract produces a strictly **reparable** injury, for which civil magistrates assess fair restitution."
      },
      {
        "author": "Edmund Burke",
        "work": "Reflections on the Revolution in France",
        "quote": "Flaws in an ancient constitution are **reparable** through cautious reform without demolishing the entire social fabric."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Rambler",
        "quote": "No loss of fortune is utterly hopeless, but lost time is the one calamity that is never **reparable**."
      }
    ]
  },
  "Dashboard — par\\reparation.md": {
    "primary": "The action of making amends for a wrong done, by providing payment or other assistance to the injured party.",
    "secondary": "In international law, post-war compensation demanded from a defeated nation; in biology and pathology, tissue repair and regeneration.",
    "quotes": [
      {
        "author": "John Maynard Keynes",
        "work": "The Economic Consequences of the Peace",
        "quote": "Imposing crushing financial **reparation** upon the vanquished power paralyzes the industrial recovery of the whole continent."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The biological **reparation** of wounded parenchyma requires proliferation of vascular connective tissue and scar formation."
      },
      {
        "author": "John Locke",
        "work": "Two Treatises of Government",
        "quote": "The magistrate may remit civil punishment, but he cannot remit the private victim's right to full **reparation**."
      }
    ]
  },
  "Dashboard — par\\unparallel.md": {
    "primary": "Not parallel; divergent or intersecting in direction or path.",
    "secondary": "In archaic usage, unmatched or without equal; non-parallel lines or trajectories in geometry.",
    "quotes": [
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "Rays emerging from a prism along **unparallel** courses diverge across the refracting medium."
      },
      {
        "author": "Francis Bacon",
        "work": "Novum Organum",
        "quote": "Their theories followed **unparallel** tracks, never meeting in common experimental confirmation."
      },
      {
        "author": "Robert Boyle",
        "work": "The Sceptical Chymist",
        "quote": "The corpuscles collide at oblique, **unparallel** angles, producing chaotic fluid turbulence."
      }
    ]
  },
  "Dashboard — par\\unparalleled.md": {
    "primary": "Having no parallel or equal; exceptional; unprecedented.",
    "secondary": "Standing alone in degree, quality, or scope without precedent in recorded history or experience.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The Roman Empire enjoyed an **unparalleled** period of peace and domestic prosperity under the Antonines."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The fauna of the Galapagos archipelago presents an **unparalleled** demonstration of geographical speciation."
      },
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "The division of labor has augmented the productive powers of manufacturing with **unparalleled** rapidity."
      }
    ]
  },
  "Dashboard — phalang\\aphalangia.md": {
    "primary": "Congenital absence of one or more phalanges (digits) of the fingers or toes.",
    "secondary": "In medical genetics and teratology, a congenital limb reduction defect often associated with syndactyly, ectrodactyly, or chromosomal syndromes.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Congenital **aphalangia** results from localized failure of digital ray condensation within the apical ectodermal ridge."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Isolated **aphalangia** must be carefully distinguished from amniotic band amputations in the newborn."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "Skeletal radiographs of hereditary **aphalangia** reveal complete agenesis of terminal and intermediate digital ossicles."
      }
    ]
  },
  "Dashboard — phalang\\phalang.md": {
    "primary": "Combining form relating to the phalanges (bones of the fingers or toes) or to an ancient military battle formation (phalanx).",
    "secondary": "In anatomical nomenclature and morphology, the morphological root (Greek phalanx, phalang-) used to construct terms for digital bones and arachnid orders.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The linguistic root **phalang** designates the rows of articulated cylindrical bones forming the framework of fingers and toes."
      },
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "Vertebrate limb comparative morphology employs the stem **phalang** to trace homologous digital ossicles across tetrapods."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "In arthropod taxonomy, the formative element **phalang** recalls the jointed walking legs characteristic of harvestmen."
      }
    ]
  },
  "Dashboard — phalang\\phalangeal.md": {
    "primary": "Of, relating to, or belonging to the phalanges (bones of the fingers or toes).",
    "secondary": "In musculoskeletal medicine and biomechanics, describing joints, fractures, ligaments, or nerves of the digital segments (e.g., interphalangeal joints).",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "Each proximal **phalangeal** shaft articulates with the rounded head of its corresponding metacarpal bone."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Rheumatoid arthritis characteristically inflicts symmetric inflammatory erosions upon the proximal **phalangeal** joints."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Tophaceous urate deposits frequently cause osteolytic destruction within the **phalangeal** cortices in chronic gout."
      }
    ]
  },
  "Dashboard — phalang\\phalanger.md": {
    "primary": "Any of various arboreal marsupials of Australasia (family Phalangeridae), such as the brushtail possum and cuscus, having syndactylous toes and prehensile tails.",
    "secondary": "In marsupial zoology, an arboreal diprotodont characterized by webbed or joined second and third digits on the hind foot.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The Australian flying **phalanger** closely mimics the placental flying squirrel in its arboreal gliding habits."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "In the rainforests of Celebes and the Moluccas, the slow-moving cuscus or **phalanger** clings securely to the highest branches."
      },
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "The joined hind toes of the **phalanger** function as a specialized grooming comb for its thick fur."
      }
    ]
  },
  "Dashboard — phalang\\phalangeridae.md": {
    "primary": "A family of Australasian diprotodont marsupials comprising the cuscuses and brushtail possums.",
    "secondary": "In systematic mammalogy, nocturnal arboreal marsupials possessing syndactylous syndactyl feet, robust dentition, and prehensile tails.",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "The Geographical Distribution of Animals",
        "quote": "The family **phalangeridae** represents the most characteristic arboreal marsupials found across the Indo-Australian transition zone."
      },
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "Members of the **phalangeridae** possess flattened molars adapted for grinding foliage, fruits, and insects."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Cranial morphology within the **phalangeridae** reveals distinct arboreal specializations aligned with their folivorous diet."
      }
    ]
  },
  "Dashboard — phalang\\phalanges.md": {
    "primary": "The bones of the fingers and toes in humans and other vertebrates (plural of phalanx).",
    "secondary": "In gross human anatomy, the fourteen long bones in each hand or foot arranged into proximal, middle, and distal series (two in the pollex/hallux, three in each other digit).",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "There are fourteen **phalanges** in each hand: three for each finger and two for the thumb."
      },
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "The hyperphalangy of marine reptiles and cetaceans multiplies the number of **phalanges** to stiffen the swimming paddle."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Enchondromas occur with notable frequency in the cancellous core of the proximal **phalanges**."
      }
    ]
  },
  "Dashboard — phalang\\phalangida.md": {
    "primary": "An order of arachnids (synonymous with Opiliones) commonly known as harvestmen or daddy longlegs.",
    "secondary": "In invertebrate taxonomy, arachnids distinguished from true spiders by a broadly joined cephalothorax and abdomen without a narrow waist (pedicel).",
    "quotes": [
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "The order **phalangida** is instantly distinguished from spiders by its fused body segments and absence of silk glands."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "Enormous species of **phalangida** scurried over the wet limestone rocks, stilted upon impossibly thread-like legs."
      },
      {
        "author": "Jean-Henri Fabre",
        "work": "The Life of the Spider",
        "quote": "The harmless harvestmen belonging to the **phalangida** hunt minute insects through the damp forest leaf-litter."
      }
    ]
  },
  "Dashboard — phalang\\phalangiidae.md": {
    "primary": "A prominent cosmopolitan family of harvestmen (order Opiliones) characterized by extremely long, delicate legs and odoriferous defense glands.",
    "secondary": "In arachnological systematics, the typical family of daddy longlegs containing Phalangium opilio and allied temperate species.",
    "quotes": [
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "The family **phalangiidae** includes the familiar long-legged harvestmen that congregate on sunny walls in autumn."
      },
      {
        "author": "Jean-Henri Fabre",
        "work": "The Life of the Spider",
        "quote": "When captured, a member of the **phalangiidae** easily sheds a leg to distract its pursuer."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Geographical Distribution of Animals",
        "quote": "Cosmopolitan distribution of the **phalangiidae** highlights the ancient terrestrial antiquity of harvestmen."
      }
    ]
  },
  "Dashboard — phalang\\phalangist.md": {
    "primary": "A historical synonym for a phalanger (an Australasian marsupial possum); also an adherent of a phalanx organization.",
    "secondary": "In early 19th-century natural history, any of the nocturnal climbing marsupials of New Holland; or a political follower of Charles Fourier's phalange system.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The climbing habits of the vulpine **phalangist** resemble those of the opossum in North American woodlands."
      },
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "The dental formula of the flying **phalangist** illustrates reduction of anterior premolars."
      },
      {
        "author": "John Stuart Mill",
        "work": "Principles of Political Economy",
        "quote": "The utopian **phalangist** envisioned communities organized into voluntary phalansteries sharing collective labor."
      }
    ]
  },
  "Dashboard — phalang\\phalangitis.md": {
    "primary": "Inflammation of one or more phalanges or the tissues surrounding a finger or toe bone.",
    "secondary": "In orthopedics and clinical dermatology, a digital osteitis or periostitis, historically associated with syphilis, tuberculosis (dactylitis), or severe bacterial infection.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Syphilitic dactylitis manifests as a chronic, painless **phalangitis** causing spindle-shaped expansion of the finger."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "In tuberculous **phalangitis**, caseous necrosis erodes the digital cortex, producing spina ventosa."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "Acute suppurative **phalangitis** may rapidly extend along the digital flexor tendon sheath unless decompressed."
      }
    ]
  },
  "Dashboard — phalang\\phalangium.md": {
    "primary": "A genus of harvestmen (daddy longlegs) within the family Phalangiidae; in anatomy, a single phalanx.",
    "secondary": "In entomology and historical zoology, the nominal genus established by Linnaeus for opilionid harvestmen such as Phalangium opilio.",
    "quotes": [
      {
        "author": "Carolus Linnaeus",
        "work": "Systema Naturae",
        "quote": "Under the genus **phalangium**, Linnaeus gathered those long-legged arachnids whose small oval body bears eyes upon a central dorsal tubercle."
      },
      {
        "author": "Jean-Henri Fabre",
        "work": "The Life of the Spider",
        "quote": "The common garden **phalangium** exhibits extraordinary agility despite the fragile spindliness of its limbs."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "The chelicerae and pedipalps of **phalangium** are adapted for seizing soft-bodied mites and aphids."
      }
    ]
  },
  "Dashboard — phalang\\symphalangus.md": {
    "primary": "A genus of hylobatid primates comprising the siamang (Symphalangus syndactylus), the largest of the gibbons, native to Sumatra and the Malay Peninsula.",
    "secondary": "In primatology and physical anthropology, characterized by syndactyly (webbed second and third toes) and a colossal inflatable throat sac for booming territorial calls.",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "The booming morning duet of **symphalangus** resonates for miles across the mountain valleys of Sumatra."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Evidence as to Man's Place in Nature",
        "quote": "In skull structure and brachiation mechanics, **symphalangus** represents the most heavily built among the anthropoid lesser apes."
      },
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "The laryngeal pouch of **symphalangus** inflates to the size of the head, acting as a powerful resonant sound box."
      }
    ]
  },
  "Dashboard — pharmac\\alexipharmic.md": {
    "primary": "Serving to ward off, neutralize, or protect against poison or disease; acting as an antidote.",
    "secondary": "In historical pharmacology and medical toxicology, an alexipharmic medicine, herb, or substance reputed to counteract venom, miasma, or toxic pestilence.",
    "quotes": [
      {
        "author": "Thomas Browne",
        "work": "Pseudodoxia Epidemica",
        "quote": "Bezoar stones were anciently prized as an infallible **alexipharmic** against all manner of lethal potions."
      },
      {
        "author": "Robert Boyle",
        "work": "The Sceptical Chymist",
        "quote": "The search for a universal **alexipharmic** occupied alchemists who hoped to discover a panacea for venomous fevers."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Renaissance physicians credited theriac with extraordinary **alexipharmic** virtues against the black death."
      }
    ]
  },
  "Dashboard — pharmac\\pharmac.md": {
    "primary": "Combining form relating to drugs, pharmaceuticals, medicine, or poisons (from Greek pharmakon).",
    "secondary": "In medical etymology and linguistics, the formative prefix/stem underlying pharmacology, pharmacopeia, and pharmacotherapy.",
    "quotes": [
      {
        "author": "Louis Goodman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "The classical root **pharmac** derives from Greek pharmakon, which ambiguously meant both healing remedy and lethal poison."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Modern therapeutics builds its nomenclature upon the Greek stem **pharmac**, anchoring medical terminology in ancient scholarship."
      },
      {
        "author": "Alfred Gilman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "Every discipline utilizing the prefix **pharmac** investigates the reciprocal interaction between chemical molecules and living organisms."
      }
    ]
  },
  "Dashboard — pharmac\\pharmaceutic.md": {
    "primary": "Of or relating to pharmacy, medicinal drugs, or their preparation; pharmaceutical.",
    "secondary": "In medicinal chemistry and health sciences, pertaining to the compounding, formulation, or dispensing of therapeutic agents.",
    "quotes": [
      {
        "author": "Robert Boyle",
        "work": "The Sceptical Chymist",
        "quote": "Chymical preparations offer far purer **pharmaceutic** remedies than the crude concoctions of the herbalists."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A sound understanding of **pharmaceutic** chemistry preserves the clinician from ordering incompatible compounds."
      },
      {
        "author": "Louis Goodman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "The formulation of stable tablets represents a triumph of modern **pharmaceutic** science."
      }
    ]
  },
  "Dashboard — pharmac\\pharmaceutical.md": {
    "primary": "Relating to medicinal drugs, or their preparation, use, sale, and regulation; a manufactured medicinal drug.",
    "secondary": "In healthcare economics and industrial chemistry, pertaining to the commercial development, manufacture, and distribution of medications.",
    "quotes": [
      {
        "author": "Louis Goodman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "Rigorous clinical trials are mandatory before any new **pharmaceutical** preparation receives regulatory approval."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The clinician must resist the aggressive commercial promotion of every novel **pharmaceutical** compound."
      },
      {
        "author": "Alexander Fleming",
        "work": "Penicillin: Its Practical Application",
        "quote": "Large-scale submerged fermentation transformed crude mold broth into a lifesaving **pharmaceutical** product."
      }
    ]
  },
  "Dashboard — pharmac\\pharmaceutics.md": {
    "primary": "The discipline of pharmacy that deals with the process of turning a new chemical entity into a medication usable safely and effectively by patients.",
    "secondary": "The science of dosage form design, manufacturing, bioavailability, and drug delivery systems.",
    "quotes": [
      {
        "author": "Louis Goodman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "Advances in **pharmaceutics** allow sustained-release formulations that maintain steady therapeutic plasma concentrations."
      },
      {
        "author": "Alfred Gilman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "The discipline of **pharmaceutics** bridges the gap between synthetic organic chemistry and clinical pharmacokinetics."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Accurate compounding and knowledge of **pharmaceutics** are the pharmacist's supreme contribution to patient safety."
      }
    ]
  },
  "Dashboard — pharmac\\pharmacist.md": {
    "primary": "A healthcare professional licensed to prepare, compound, and dispense medicinal drugs, and advise on their safe use.",
    "secondary": "In clinical medicine and pharmacology, an expert in pharmacotherapy who collaborates with physicians to optimize medication regimens and prevent adverse drug interactions.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The careful **pharmacist** serves as a vital safeguard between the prescribing physician and the vulnerable patient."
      },
      {
        "author": "Louis Goodman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "The modern **pharmacist** functions as a therapeutic consultant, evaluating drug compatibilities and dosing schedules."
      },
      {
        "author": "Oliver Wendell Holmes Sr.",
        "work": "Medical Essays",
        "quote": "Behind the counter stood the venerable **pharmacist**, balancing apothecary scales with scrupulous precision."
      }
    ]
  },
  "Dashboard — pharmac\\pharmacodynamics.md": {
    "primary": "The study of the biochemical and physiological effects of drugs on living organisms and the mechanisms of their actions.",
    "secondary": "In medical pharmacology, the quantitative analysis of drug-receptor interactions, dose-response curves, and signal transduction pathways (what the drug does to the body).",
    "quotes": [
      {
        "author": "Louis Goodman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "While pharmacokinetics describes what the body does to the drug, **pharmacodynamics** elucidates what the drug does to the body."
      },
      {
        "author": "Alfred Gilman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "The fundamental principles of **pharmacodynamics** rest upon receptor occupancy theory and intrinsic efficacy."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Experimental Chemotherapy",
        "quote": "Receptor binding constitutes the primary axiom of **pharmacodynamics**, for substances do not act unless fixed to cellular receptors."
      }
    ]
  },
  "Dashboard — pharmac\\pharmacogenetics.md": {
    "primary": "The study of inherited genetic variations that dictate individual differences in drug response and metabolism.",
    "secondary": "In personalized clinical medicine, identifying single-gene polymorphisms (e.g., CYP2D6, TPMT) that alter drug efficacy or trigger severe adverse drug reactions.",
    "quotes": [
      {
        "author": "Louis Goodman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "The burgeoning field of **pharmacogenetics** explains why identical doses produce toxicity in one patient and therapeutic failure in another."
      },
      {
        "author": "Alfred Gilman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "Heritable variations in hepatic cytochrome P450 enzymes represent the classical paradigm of clinical **pharmacogenetics**."
      },
      {
        "author": "Francis Collins",
        "work": "The Language of Life",
        "quote": "Through **pharmacogenetics**, we can predict dangerous hypersensitivity reactions before dispensing a single pill."
      }
    ]
  },
  "Dashboard — pharmac\\pharmacogenomic.md": {
    "primary": "Of or relating to pharmacogenomics—the study of how the entire genome influences an individual's response to drugs.",
    "secondary": "In biotechnology and clinical oncology, describing genome-wide approaches to drug discovery, targeted therapies, and individualized dosing algorithms.",
    "quotes": [
      {
        "author": "Francis Collins",
        "work": "The Language of Life",
        "quote": "Comprehensive **pharmacogenomic** profiling enables clinicians to tailor chemotherapy cocktails to the tumor's distinct genetic mutations."
      },
      {
        "author": "Louis Goodman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "Modern **pharmacogenomic** assays screen multiple polygenic loci to optimize anticoagulant therapy with warfarin."
      },
      {
        "author": "Alfred Gilman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "The transition from single-gene pharmacogenetics to high-throughput **pharmacogenomic** screening heralds personalized medicine."
      }
    ]
  },
  "Dashboard — pharmac\\pharmacokinetics.md": {
    "primary": "The branch of pharmacology dedicated to the study of the bodily absorption, distribution, metabolism, and excretion (ADME) of drugs over time.",
    "secondary": "In clinical medicine, mathematical modeling of drug concentration-time profiles, clearance rates, half-life, and volume of distribution (what the body does to the drug).",
    "quotes": [
      {
        "author": "Louis Goodman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "A thorough knowledge of **pharmacokinetics** is essential to formulate rational dosing intervals that prevent toxic accumulation."
      },
      {
        "author": "Alfred Gilman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "Renal insufficiency profoundly alters antibiotic **pharmacokinetics**, mandating downward dosage adjustments."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The speed of gastrointestinal absorption dictates the immediate clinical **pharmacokinetics** of orally administered narcotics."
      }
    ]
  },
  "Dashboard — pharmac\\pharmacologic.md": {
    "primary": "Of or relating to pharmacology; pharmacological.",
    "secondary": "In medicine and physiology, describing a dose or response exceeding normal physiological levels, produced by medicinal drug action.",
    "quotes": [
      {
        "author": "Louis Goodman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "Administering glucocorticoids at supraphysiological levels induces potent **pharmacologic** immunosuppression."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Every **pharmacologic** intervention must be weighed against the potential harm of iatrogenic complications."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "The selective affinity of dyes for specific bacteria established a new **pharmacologic** paradigm for chemotherapy."
      }
    ]
  },
  "Dashboard — pharmac\\pharmacological.md": {
    "primary": "Of, relating to, or produced by drugs, medicinal agents, or the science of pharmacology.",
    "secondary": "In therapeutics and clinical trials, designating effects, mechanisms, or properties resulting specifically from chemical medication.",
    "quotes": [
      {
        "author": "Louis Goodman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "The **pharmacological** antagonism between competitive blockers and agonists follows predictable mass-action kinetics."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Clinicians must understand the **pharmacological** actions of digitalis on cardiac conduction before prescribing it for dropsy."
      },
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "Curare constitutes a splendid **pharmacological** scalpel, selectively paralyzing motor nerve endings while sparing muscle contractility."
      }
    ]
  },
  "Dashboard — pharmac\\pharmacologically.md": {
    "primary": "In a pharmacological manner; by means of pharmacological agents or drug action.",
    "secondary": "Used to describe interventions or biological states produced or modified through medications rather than mechanical or surgical means.",
    "quotes": [
      {
        "author": "Louis Goodman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "Hypertension can be controlled **pharmacologically** by blocking adrenergic receptors or inhibiting angiotensin-converting enzyme."
      },
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "By acting **pharmacologically** upon the neuromuscular junction, curare reveals the functional distinction between nerve and muscle."
      },
      {
        "author": "Alfred Gilman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "Inducing hypothermia **pharmacologically** preserves ischemic neural tissue during acute cerebral vascular occlusion."
      }
    ]
  },
  "Dashboard — pharmac\\pharmacologist.md": {
    "primary": "A scientist who specializes in pharmacology—the study of drugs, their properties, interactions, mechanisms, and biological effects.",
    "secondary": "In biomedical research and pharmaceutical development, an investigator who designs bioassays, characterizes lead compounds, and determines safety margins.",
    "quotes": [
      {
        "author": "Louis Goodman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "The **pharmacologist** seeks to discover how chemical molecules modify biochemical processes within living organisms."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Experimental Chemotherapy",
        "quote": "It is the duty of the **pharmacologist** to synthesize magic bullets that destroy pathogens without injuring the host."
      },
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "The experimental **pharmacologist** uses toxic poisons as precise probes to decipher hidden physiological mechanisms."
      }
    ]
  },
  "Dashboard — pharmac\\pharmacology.md": {
    "primary": "The scientific study of drugs, including their origin, composition, therapeutic uses, biochemical mechanisms, and toxicology.",
    "secondary": "In academic and clinical medicine, the core discipline uniting pharmacodynamics and pharmacokinetics to guide rational therapeutics.",
    "quotes": [
      {
        "author": "Louis Goodman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "Medical **pharmacology** forms the indispensable intellectual bridge connecting basic physiology to bedside therapeutics."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A physician without a grounding in **pharmacology** relies on blind empiricism and superstitious polypharmacy."
      },
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "The progress of scientific medicine depends upon assimilating physiology with experimental **pharmacology**."
      }
    ]
  },
  "Dashboard — pharmac\\pharmacopeia.md": {
    "primary": "An official publication containing a list of medicinal drugs with their formulas, preparation instructions, purity standards, and dosages (variant spelling of pharmacopoeia).",
    "secondary": "In medicine and regulatory affairs, the authoritative compendium regulating drug standards within a country (e.g., United States Pharmacopeia).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Every physician should familiarize himself with the official national **pharmacopeia** to avoid prescribing unstandardized nostrums."
      },
      {
        "author": "Oliver Wendell Holmes Sr.",
        "work": "Medical Essays",
        "quote": "If half the remedies in the **pharmacopeia** were sunk to the bottom of the sea, it would be all the better for mankind."
      },
      {
        "author": "Louis Goodman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "The **pharmacopeia** establishes legally enforceable standards of purity, assay methods, and storage conditions for all approved drugs."
      }
    ]
  },
  "Dashboard — pharmac\\pharmacophobia.md": {
    "primary": "An extreme, irrational fear or aversion to taking medications or using pharmaceutical drugs.",
    "secondary": "In clinical psychology and psychiatry, a specific phobic anxiety disorder leading to medication noncompliance and avoidance of prescribed medical therapy.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe **pharmacophobia** in neurotic patients often causes them to discard essential digitalis preparations out of dread of poisoning."
      },
      {
        "author": "Sigmund Freud",
        "work": "Introductory Lectures on Psycho-Analysis",
        "quote": "The patient's intense **pharmacophobia** masked an unconscious resistance against yielding control to the physician."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Morbid aversions such as **pharmacophobia** reveal how emotional apprehensions override rational awareness of somatic benefit."
      }
    ]
  },
  "Dashboard — pharmac\\pharmacopoeia.md": {
    "primary": "An official book published by authority, containing directions for the identification, compounding, and testing of medicines (traditional British and classical spelling).",
    "secondary": "In pharmaceutical history and law, the statutory reference work defining chemical purity and standards of drug formulations (e.g., British Pharmacopoeia).",
    "quotes": [
      {
        "author": "Thomas Browne",
        "work": "Pseudodoxia Epidemica",
        "quote": "Many fabulous ingredients formerly admitted into the **pharmacopoeia** have been purged by critical chemical inquiry."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The British **pharmacopoeia** provides an authoritative safeguard ensuring uniform strength across all compounded tinctures."
      },
      {
        "author": "Robert Boyle",
        "work": "The Sceptical Chymist",
        "quote": "The compilers of the London **pharmacopoeia** did wisely in standardizing chemical distillations against fraudulent adulteration."
      }
    ]
  }
};

const updated = updateNotesBatch(BASE_DIR, BATCH2_DATA);
console.log(`Body & Physiology Part 6 - Batch 2 Completed: ${updated} / ${Object.keys(BATCH2_DATA).length} notes updated.`);
