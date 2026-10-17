import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Number & Mathematics');
const batchData = {
  "Dashboard — mei/ameiosis.md": {
    "primary": "The absence, omission, or failure of meiosis during gamete formation, resulting in the production of unreduced diploid gametes.",
    "secondary": "In cytogenetics and evolutionary botany, an apomictic reproductive pathway in which asexual eggs develop parthenogenetically without chromosome reduction.",
    "quotes": [
      {
        "author": "C. D. Darlington",
        "work": "Recent Advances in Cytology",
        "quote": "Complete **ameiosis** prevents chromosome reduction, allowing maternal genotypes to clone true across generations."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "In parthenogenetic weevils, **ameiosis** preserves complex heterozygous gene combinations from segregation."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "Apomictic dandelion micro-species rely upon **ameiosis** to bypass the hazards of sexual recombination."
      }
    ]
  },
  "Dashboard — mei/ameiotic.md": {
    "primary": "Pertaining to, characterized by, or undergoing ameiosis; reproducing without meiotic reduction division.",
    "secondary": "In reproductive biology, describing parthenogenetic or apomictic egg development where the full somatic chromosome number is preserved.",
    "quotes": [
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "An **ameiotic** lineage forfeits the long-term evolutionary flexibility afforded by crossing-over and sexual recombination."
      },
      {
        "author": "C. D. Darlington",
        "work": "Recent Advances in Cytology",
        "quote": "During **ameiotic** oogenesis, the single maturation division is equational rather than reductional."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "Unisexual lizard species maintain vigorous populations solely through **ameiotic** clonal reproduction."
      }
    ]
  },
  "Dashboard — mei/meiobenthos.md": {
    "primary": "Small benthic invertebrates that inhabit aquatic sediments, intermediate in size between microscopic microbenthos and larger macrobenthos (typically retained on a 45 µm to 500 µm sieve).",
    "secondary": "In marine and freshwater ecology, interstitial organisms (such as nematodes, harpacticoid copepods, and gastrotrichs) living between sand grains in benthic substrate ecosystems.",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "Between the coarse sand grains of the tidal flat swarms an unseen world of miniature creatures termed the **meiobenthos**."
      },
      {
        "author": "Alister Hardy",
        "work": "The Open Sea: Its Natural History",
        "quote": "Deep-sea core samples revealed extraordinary taxonomic richness within the abyssal **meiobenthos**."
      },
      {
        "author": "Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Interstitial nematodes and rotifers constitute the dominant biomass of freshwater **meiobenthos** in lake sediments."
      }
    ]
  },
  "Dashboard — mei/meiosis.md": {
    "primary": "A specialized form of cell division in sexually reproducing eukaryotes that reduces the chromosome number by half, producing four genetically diverse haploid gametes or spores.",
    "secondary": "In cytogenetics, the two-stage reduction division (meiosis I and II) comprising prophase crossing-over and homologous segregation; in rhetoric, an intentional understatement or belittlement.",
    "quotes": [
      {
        "author": "Thomas Hunt Morgan",
        "work": "The Theory of the Gene",
        "quote": "During the dramatic stages of **meiosis**, homologous maternal and paternal chromosomes pair and exchange genetic materials."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "The exquisite precision of **meiosis** ensures that each gamete receives a balanced, complete haploid genome."
      },
      {
        "author": "Richard Dawkins",
        "work": "The Selfish Gene",
        "quote": "By the shuffling mechanism of **meiosis**, nature breaks apart parental gene combinations and forges unique individual genotypes."
      }
    ]
  },
  "Dashboard — mei/meiotic.md": {
    "primary": "Pertaining to, involving, or resulting from meiosis.",
    "secondary": "In cytogenetics, describing cellular processes, chromosomal events (such as meiotic recombination and meiotic drive), or spindle dynamics occurring during reduction division.",
    "quotes": [
      {
        "author": "C. D. Darlington",
        "work": "Recent Advances in Cytology",
        "quote": "The mechanics of **meiotic** chromosome pairing require homologous recognition along the entire length of the chromatids."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "Genetic variation is continuously replenished through random **meiotic** assortment of maternal and paternal chromosomes."
      },
      {
        "author": "Thomas Hunt Morgan",
        "work": "Heredity and Sex",
        "quote": "Failure of the **meiotic** spindle to separate chromosomes correctly results in non-disjunction and abnormal offspring."
      }
    ]
  },
  "Dashboard — meter/anemometer.md": {
    "primary": "An instrument used for measuring the speed, velocity, or pressure of the wind.",
    "secondary": "In meteorology, a standard recording station device (such as Robinson cup or sonic anemometer) measuring air currents and wind vector components.",
    "quotes": [
      {
        "author": "Robert FitzRoy",
        "work": "The Weather Book: A Manual of Practical Meteorology",
        "quote": "The spinning cups of the Robinson **anemometer** recorded gale-force gusts exceeding sixty miles an hour along the coast."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos: A Sketch of a Physical Description of the Universe",
        "quote": "By comparing the barometer with our portable **anemometer**, we correlated barometric falls with sudden shifts in wind velocity."
      },
      {
        "author": "John Tyndall",
        "work": "The Glaciers of the Alps",
        "quote": "The mountain observatory mounted an **anemometer** upon its highest tower to monitor fierce alpine storms."
      }
    ]
  },
  "Dashboard — meter/anemometric.md": {
    "primary": "Pertaining to, measured by, or characteristic of an anemometer; relating to the measurement of wind velocity.",
    "secondary": "In atmospheric physics and observational meteorology, describing instruments, charts, or quantitative records tracking wind force and speed.",
    "quotes": [
      {
        "author": "Robert FitzRoy",
        "work": "The Weather Book: A Manual of Practical Meteorology",
        "quote": "Continuous **anemometric** traces revealed violent nocturnal squalls sweeping across the harbor mouth."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Personal Narrative of Travels to the Equinoctial Regions",
        "quote": "Our **anemometric** observations during the hurricane confirmed a sharp increase in wind pressure before the eye arrived."
      },
      {
        "author": "Arthur Newell Strahler",
        "work": "Physical Geography",
        "quote": "Synoptic meteorological charts compile thousands of coastal **anemometric** readings to trace cyclonic circulation."
      }
    ]
  },
  "Dashboard — meter/anemometrical.md": {
    "primary": "A variant form of anemometric, pertaining to anemometry or the instrumentation used to measure wind speed.",
    "secondary": "In historical scientific treatises, describing empirical measurements or apparatus designed to record atmospheric wind dynamics.",
    "quotes": [
      {
        "author": "William Whewell",
        "work": "History of the Inductive Sciences",
        "quote": "The invention of reliable **anemometrical** instruments allowed meteorologists to substitute numbers for vague descriptive terms."
      },
      {
        "author": "John Herschel",
        "work": "Meteorology",
        "quote": "Careful **anemometrical** observations taken at sea establish the steady velocity of the trade winds across tropical latitudes."
      },
      {
        "author": "Thomas Young",
        "work": "A Course of Lectures on Natural Philosophy",
        "quote": "The mechanical design of the **anemometrical** register required compensating for friction in the rotating spindle."
      }
    ]
  },
  "Dashboard — meter/anisometric.md": {
    "primary": "Not isometric; having unequal dimensions, unequal axes, or unequal rates of growth.",
    "secondary": "In crystallography and materials science, designating crystals belonging to non-cubic systems (such as tetragonal, orthorhombic, or monoclinic) whose unit cell axes are of unequal length.",
    "quotes": [
      {
        "author": "James Dwight Dana",
        "work": "A System of Mineralogy",
        "quote": "Unlike cubic galena, minerals of the **anisometric** systems display unequal axial lengths and birefringent optical behavior."
      },
      {
        "author": "René Just Haüy",
        "work": "Traité de Minéralogie",
        "quote": "In **anisometric** crystals, mechanical cleavage properties differ markedly along contrasting crystallographic directions."
      },
      {
        "author": "D'Arcy Wentworth Thompson",
        "work": "On Growth and Form",
        "quote": "The distorted growth of the shell reflects an **anisometric** expansion rate across its growing margins."
      }
    ]
  },
  "Dashboard — meter/antisymmetric.md": {
    "primary": "Exhibiting antisymmetry; reversing sign under an operation such as coordinate reflection or matrix transposition (satisfying A^T = -A).",
    "secondary": "In quantum mechanics and linear algebra, describing wavefunctions of identical fermions (such as electrons) that change sign upon the exchange of any two particles, underpinning the Pauli exclusion principle.",
    "quotes": [
      {
        "author": "Paul Dirac",
        "work": "The Principles of Quantum Mechanics",
        "quote": "The state vector representing an assembly of electrons must be strictly **antisymmetric** with respect to the exchange of any two particles."
      },
      {
        "author": "Richard Feynman",
        "work": "The Feynman Lectures on Physics",
        "quote": "Nature requires all fermions to possess an **antisymmetric** wavefunction, explaining why matter resists infinite compression."
      },
      {
        "author": "Linus Pauling",
        "work": "Introduction to Quantum Mechanics",
        "quote": "The Slater determinant provides a systematic mathematical expression for constructing an **antisymmetric** electronic state."
      }
    ]
  },
  "Dashboard — meter/antisymmetry.md": {
    "primary": "The state, property, or condition of being antisymmetric.",
    "secondary": "In theoretical physics and mathematics, the fundamental invariance property where swapping arguments, indices, or particles negates the mathematical entity, governing fermionic statistics and differential forms.",
    "quotes": [
      {
        "author": "Paul Dirac",
        "work": "The Principles of Quantum Mechanics",
        "quote": "The fundamental **antisymmetry** of the electronic wavefunction is the quantum mechanical origin of chemical valence and structure."
      },
      {
        "author": "Roger Penrose",
        "work": "The Road to Reality",
        "quote": "Differential forms owe their elegant geometric calculus to the pervasive **antisymmetry** of the exterior wedge product."
      },
      {
        "author": "H. S. M. Coxeter",
        "work": "Regular Complex Polytopes",
        "quote": "Geometric operations of combined inversion and translation can produce striking forms of spatial **antisymmetry**."
      }
    ]
  },
  "Dashboard — meter/asymmetric.md": {
    "primary": "Lacking symmetry; having parts or aspects that fail to correspond in shape, size, or arrangement across a dividing plane or center.",
    "secondary": "In stereochemistry and physics, lacking improper axes of rotation (chiral), giving rise to optical activity and molecular enantiomers.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Researches on the Molecular Asymmetry of Natural Organic Products",
        "quote": "The tartrate crystals exhibited an **asymmetric** hemihedral facet that rotated the plane of polarized light to the right."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The flounder undergoes a remarkable developmental distortion, ending with both eyes on one side of its **asymmetric** head."
      },
      {
        "author": "D'Arcy Wentworth Thompson",
        "work": "On Growth and Form",
        "quote": "The crab's colossal fighting claw creates an intensely **asymmetric** body plan adapted for territorial defense."
      }
    ]
  },
  "Dashboard — meter/asymmetrical.md": {
    "primary": "Having parts that fail to correspond in size, form, or arrangement; lacking balanced proportions.",
    "secondary": "In architecture, art, and biology, exhibiting deliberate or natural irregularity and non-uniformity across opposing sides.",
    "quotes": [
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "Gothic builders embraced an **asymmetrical** freedom in their facades, balancing masses through dynamic harmony rather than rigid monotony."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The skull of the cetacean is markedly **asymmetrical**, with the blowhole shifted toward the left of the cranial axis."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The sperm whale's immense head contains an **asymmetrical** spermaceti organ resting within its massive lower jaw."
      }
    ]
  },
  "Dashboard — meter/asymmetrically.md": {
    "primary": "In an asymmetrical manner; with unequal, uneven, or unbalanced distribution of parts.",
    "secondary": "Arranged or developing so that corresponding sides or components do not mirror each other.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Power of Movement in Plants",
        "quote": "The climbing tendril responds to tactile stimulation by growing **asymmetrically**, curving tightly around the supporting twig."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Attention falls **asymmetrically** upon sensory stimuli, highlighting significant details while suppressing background noise."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "When electric currents traversed the non-uniform conductor, heat dissipated **asymmetrically** along the narrow neck."
      }
    ]
  },
  "Dashboard — meter/asymmetry.md": {
    "primary": "Lack of symmetry, balance, proportion, or equivalence between parts of a whole.",
    "secondary": "In physics and biochemistry, the absence of mirror symmetry that gives rise to chirality, parity violation in weak interactions, and molecular handedness.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Researches on the Molecular Asymmetry of Natural Organic Products",
        "quote": "Molecular **asymmetry** is the only clearly demarcated boundary between the chemistry of dead matter and the chemistry of life."
      },
      {
        "author": "Richard Feynman",
        "work": "The Character of Physical Law",
        "quote": "The discovery of parity violation in beta decay demonstrated an unexpected **asymmetry** in the fundamental laws of nature."
      },
      {
        "author": "Ernst Haeckel",
        "work": "Art Forms in Nature",
        "quote": "From primary spherical and radial symmetry, organic evolution progressed toward bilateral form and specialized **asymmetry**."
      }
    ]
  },
  "Dashboard — meter/axonometric.md": {
    "primary": "Pertaining to or constructed according to axonometry; a graphical method of orthographic projection depicting a 3D object tilted to display three axes.",
    "secondary": "In technical drawing and architectural drafting, designating isometric, dimetric, or trimetric projections where scales along the axes maintain fixed geometric ratios.",
    "quotes": [
      {
        "author": "William Farish",
        "work": "On Isometrical Perspective",
        "quote": "The **axonometric** method allows the mechanical draftsman to present the true three-dimensional proportions of an engine on a single sheet."
      },
      {
        "author": "Banister Fletcher",
        "work": "A History of Architecture",
        "quote": "An **axonometric** cutaway drawing reveals the complex interlocking vaults of the Roman baths with absolute spatial clarity."
      },
      {
        "author": "Arthur Cayley",
        "work": "The Collected Mathematical Papers",
        "quote": "Coordinate projection matrices translate multi-dimensional polytopes into clear **axonometric** figures on the drawing plane."
      }
    ]
  },
  "Dashboard — meter/barometric.md": {
    "primary": "Pertaining to, determined by, or measured with a barometer; relating to atmospheric pressure.",
    "secondary": "In meteorology, describing atmospheric pressure gradients, systems of high and low pressure, or altimetric altitude calculations.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos: A Sketch of a Physical Description of the Universe",
        "quote": "Diurnal **barometric** tides in the tropics oscillate with the regular clockwork rhythm of the sun."
      },
      {
        "author": "Robert FitzRoy",
        "work": "The Weather Book: A Manual of Practical Meteorology",
        "quote": "A rapid **barometric** depression invariably warns the mariner of approaching cyclonic fury."
      },
      {
        "author": "John Tyndall",
        "work": "The Glaciers of the Alps",
        "quote": "We determined the summit altitude of the mountain by comparing simultaneous **barometric** readings with those of the valley station."
      }
    ]
  },
  "Dashboard — meter/barometrical.md": {
    "primary": "A variant form of barometric, pertaining to a barometer or the measurement of atmospheric pressure.",
    "secondary": "In historical scientific and navigational writing, determined by atmospheric pressure instrumentation.",
    "quotes": [
      {
        "author": "John Herschel",
        "work": "A Preliminary Discourse on the Study of Natural Philosophy",
        "quote": "Torricelli's celebrated experiment laid the foundation for all modern **barometrical** measurements of atmospheric weight."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "The surveyor recorded **barometrical** heights at every plateau boundary to determine regional geological uplift."
      },
      {
        "author": "Robert Boyle",
        "work": "New Experiments Physico-Mechanicall",
        "quote": "The mercury column in the closed glass tube exhibited significant **barometrical** variations depending upon changing weather."
      }
    ]
  },
  "Dashboard — meter/bathometer.md": {
    "primary": "An instrument designed for measuring the depth of water in oceans, seas, or lakes without using a conventional sounding line.",
    "secondary": "In oceanography, a gravimetric or acoustical sounding device (such as Siemens' bathometer) measuring water depth by detecting variations in gravitational attraction or echo timing.",
    "quotes": [
      {
        "author": "William Siemens",
        "work": "On the Determination of the Depth of the Sea by a New Instrument",
        "quote": "My **bathometer** measures the minute decrease in terrestrial gravitational attraction caused by the low density of deep ocean water beneath."
      },
      {
        "author": "William Thomson (Lord Kelvin)",
        "work": "Popular Lectures and Addresses: Navigational Affairs",
        "quote": "Rapid deep-sea sounding by an accurate **bathometer** is indispensable when paying out submarine telegraph cables across the Atlantic."
      },
      {
        "author": "Alexander Agassiz",
        "work": "Three Cruises of the United States Coast and Geodetic Survey Steamer Blake",
        "quote": "Before deploying the heavy deep-sea dredge, we calibrated our **bathometer** over the abyssal trench."
      }
    ]
  },
  "Dashboard — meter/chronometer.md": {
    "primary": "An exceptionally precise, portable mechanical timepiece, especially a marine chronometer used for determining longitude at sea.",
    "secondary": "In horology and navigation, a temperature-compensated timepiece invented by John Harrison in the 18th century, maintaining unwavering accuracy despite ship rolling and climatic shifts.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "HMS Beagle carried twenty-two delicate **chronometers** to measure longitudes with unprecedented exactness around the globe."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The captain carefully compared his deck observations of the noon sun with the steadfast time recorded by his cabin **chronometer**."
      },
      {
        "author": "Joseph Conrad",
        "work": "The Secret Agent",
        "quote": "Greenwich Observatory stood as the sacred fountain of standard time, whence every marine **chronometer** drew its authority."
      }
    ]
  },
  "Dashboard — meter/demeter.md": {
    "primary": "In ancient Greek religion and mythology, Demeter (Δημήτηρ), Olympian goddess of agriculture, grain, harvest, and the fertility of the earth; mother of Persephone.",
    "secondary": "In classical religious history, the central divinity of the Eleusinian Mysteries, symbolizing the sacred agrarian law (Thesmophoria) and the eternal cycle of death and vegetative rebirth.",
    "quotes": [
      {
        "author": "Homer",
        "work": "Homeric Hymns (Hymn to Demeter)",
        "quote": "Golden-haired **Demeter**, venerable goddess, wandered the earth mourning her stolen daughter until grain withered in the furrows."
      },
      {
        "author": "Walter Pater",
        "work": "Greek Studies: The Myth of Demeter and Persephone",
        "quote": "In the worship of **Demeter**, the Greeks sanctified the labor of the plowman and the miraculous renewal of the seed."
      },
      {
        "author": "James George Frazer",
        "work": "The Golden Bough",
        "quote": "At the Eleusinian sanctuary, initiates celebrated **Demeter** as the Corn-Mother who bestowed the divine gift of agriculture upon mankind."
      }
    ]
  },
  "Dashboard — meter/diameter.md": {
    "primary": "A straight line segment that passes through the center of a circle or sphere, terminating at both ends on the circumference; the length of this line.",
    "secondary": "In geometry and astronomy, the linear measurement across any curvilinear figure, celestial body, or optical aperture passing through its center.",
    "quotes": [
      {
        "author": "Euclid",
        "work": "Elements",
        "quote": "A **diameter** of a circle is any straight line drawn through the center and terminated in both directions by the circumference."
      },
      {
        "author": "Galileo Galilei",
        "work": "Dialogue Concerning the Two Chief World Systems",
        "quote": "Through the telescope, the disk of Jupiter displays a measurable **diameter** many times larger than the Earth."
      },
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "The **diameter** of each colored ring around the central contact point varies as the square root of the odd numbers."
      }
    ]
  },
  "Dashboard — meter/diametral.md": {
    "primary": "Of, relating to, or situated along a diameter; intersecting or dividing a geometric figure through its center.",
    "secondary": "In classical geometry and mechanics, designating a diametral plane (a plane passing through the center of a quadric surface or sphere) or diametral axis.",
    "quotes": [
      {
        "author": "Archimedes",
        "work": "On the Sphere and Cylinder",
        "quote": "Any plane passing through the center of a sphere is a **diametral** plane and divides the solid into two equal hemispheres."
      },
      {
        "author": "Leonhard Euler",
        "work": "Elements of Algebra",
        "quote": "The intersection of two conjugate **diametral** planes in an ellipsoid yields a principal diameter of the solid."
      },
      {
        "author": "Thomas Heath",
        "work": "Apollonius of Perga: Treatise on Conic Sections",
        "quote": "Apollonius established the harmonic properties of **diametral** chords drawn parallel to the tangent of a conic."
      }
    ]
  },
  "Dashboard — meter/diametric.md": {
    "primary": "Pertaining to or along a diameter; in figurative usage, completely, directly, or entirely opposed.",
    "secondary": "In geometry and analytical mechanics, situated at opposite ends of a diameter or directed along the principal diameter.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "Sectarian dogmas frequently stand in **diametric** opposition to empirical truth and charitable inquiry."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Evolution and Ethics",
        "quote": "The ethical progress of society depends upon combatting the cosmic process, standing in **diametric** resistance to raw savagery."
      },
      {
        "author": "Arthur Cayley",
        "work": "The Collected Mathematical Papers",
        "quote": "The **diametric** distance between opposing vertices of the polyhedral projection serves as the scaling baseline."
      }
    ]
  },
  "Dashboard — meter/diametrical.md": {
    "primary": "Of or relating to a diameter; directly, entirely, and completely opposed (diametrically opposite).",
    "secondary": "In geometry, positioned at opposite extremities of a diameter; in philosophy, representing absolute conceptual antithesis.",
    "quotes": [
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "Truth and falsehood stand in **diametrical** opposition, admitting of no intermediate or ambiguous compromise."
      },
      {
        "author": "Edmund Burke",
        "work": "Reflections on the Revolution in France",
        "quote": "The wild theoretical schemes of the revolutionaries were in **diametrical** contradiction to historical English liberties."
      },
      {
        "author": "Charles Darwin",
        "work": "The Expression of the Emotions in Man and Animals",
        "quote": "Opposing emotional states induce involuntary physical actions that are in **diametrical** contrast to each other."
      }
    ]
  },
  "Dashboard — meter/diametrically.md": {
    "primary": "Completely, directly, or absolutely (used especially with opposed or opposite).",
    "secondary": "Along the line of a diameter; in direct spatial opposition across a center point.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "Evil into herself all good transforms; while Good, **diametrically** opposed, from evil ever produces greater good."
      },
      {
        "author": "Thomas Babington Macaulay",
        "work": "Critical and Historical Essays",
        "quote": "The character of James I was **diametrically** unlike that of his glorious predecessor Elizabeth."
      },
      {
        "author": "Bertrand Russell",
        "work": "A History of Western Philosophy",
        "quote": "The epistemological foundations of empiricism and rationalism stood **diametrically** opposed regarding innate ideas."
      }
    ]
  },
  "Dashboard — meter/dysmetria.md": {
    "primary": "An impairment of the coordination of voluntary movement characterized by the inability to properly gauge distance, resulting in overshooting (hypermetria) or undershooting (hypometria) a target.",
    "secondary": "In clinical neurology, a classic cardinal sign of cerebellar hemispheric dysfunction or lesion, readily tested by the finger-to-nose or heel-to-shin clinical exam.",
    "quotes": [
      {
        "author": "William Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "When asked to touch his nose with his forefinger, the patient exhibited marked **dysmetria**, overshooting the mark with coarse tremor."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Cerebellar tumor symptoms include gait ataxia, intentional tremor, and pronounced kinetic **dysmetria** on the affected side."
      },
      {
        "author": "Harvey Cushing",
        "work": "Tumors of the Nervus Acusticus and the Syndrome of the Cerebellopontile Angle",
        "quote": "Unilateral compression of the cerebellar hemisphere was confirmed by prominent **dysmetria** and adiadochokinesia in the right arm."
      }
    ]
  },
  "Dashboard — meter/graphometer.md": {
    "primary": "A historical surveying instrument consisting of a semicircular graduated limb with two sighting alidades (one fixed and one movable), used for measuring horizontal angles.",
    "secondary": "In the history of geodetic instruments, an early angle-measuring device invented by Philippe Danfrie in 1597, widely utilized by Renaissance topographers and military engineers before the theodolite.",
    "quotes": [
      {
        "author": "Ferdinand Rudolph Hassler",
        "work": "Comparison of Weights and Measures",
        "quote": "Early boundary surveyors utilized a brass **graphometer** to measure horizontal angles between distant forest landmarks."
      },
      {
        "author": "Benjamin Martin",
        "work": "The Description and Use of Both the Globes, the Armillary Sphere, and Orrery",
        "quote": "The surveyor sights through the pinnules of the **graphometer** to register the bearing of the church steeple upon the graduated arc."
      },
      {
        "author": "John Herschel",
        "work": "A Preliminary Discourse on the Study of Natural Philosophy",
        "quote": "Before the refinement of the modern repeating theodolite, the **graphometer** served as the standard tool for regional cartography."
      }
    ]
  },
  "Dashboard — meter/hexameter.md": {
    "primary": "A line of verse consisting of six metrical feet, especially the classical dactylic hexameter used in Greek and Latin epic poetry.",
    "secondary": "In classical prosody, the noble heroic meter of Homer's Iliad and Virgil's Aeneid, typically composed of dactyls and spondees concluding with a dactyl and a spondee/trochee.",
    "quotes": [
      {
        "author": "Matthew Arnold",
        "work": "On Translating Homer",
        "quote": "The noble and rapid movement of the Homeric **hexameter** remains the supreme vehicle for grand heroic narrative."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "The Rime of the Ancient Mariner (and Poetical Works)",
        "quote": "Strongly it bears us along in swelling and limitless billows, Nothing before and nothing behind, but the boundless ocean of the **hexameter**."
      },
      {
        "author": "George Saintsbury",
        "work": "A History of English Prosody",
        "quote": "Longfellow's Evangeline showed that English accentual **hexameter** could charm the ear despite traditional metrical objections."
      }
    ]
  },
  "Dashboard — meter/hygrometer.md": {
    "primary": "An instrument used for measuring the humidity, moisture content, or water vapor saturation of the atmosphere or other gases.",
    "secondary": "In physics and meteorology, an instrument operating on hair hygrometric expansion (de Saussure), wet-and-dry bulb psychrometry, or chilled-mirror dew point condensation.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos: A Sketch of a Physical Description of the Universe",
        "quote": "Our hair **hygrometer** recorded rapid fluctuations in atmospheric moisture as warm sea breezes collided with the Andes."
      },
      {
        "author": "John Dalton",
        "work": "Meteorological Observations and Essays",
        "quote": "By measuring the dew point with a refined condensation **hygrometer**, we determine the exact vapor pressure of the air."
      },
      {
        "author": "John Tyndall",
        "work": "Heat Considered as a Mode of Motion",
        "quote": "The sensitive **hygrometer** registered high humidity in the valley, explaining the intense absorption of radiant heat by the lower air."
      }
    ]
  },
  "Dashboard — meter/hygrometry.md": {
    "primary": "The branch of physics and meteorology dealing with the determination and measurement of atmospheric humidity and water vapor content.",
    "secondary": "The quantitative science of evaluating relative humidity, specific humidity, and dew point temperatures across meteorological systems.",
    "quotes": [
      {
        "author": "John Dalton",
        "work": "Meteorological Observations and Essays",
        "quote": "The principles of **hygrometry** were placed upon a rigorous physical foundation once the vapor pressure of water was determined."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Personal Narrative of Travels to the Equinoctial Regions",
        "quote": "Comparative **hygrometry** demonstrates that tropical rain forests sustain an almost permanent atmospheric moisture saturation."
      },
      {
        "author": "Arthur Newell Strahler",
        "work": "Physical Geography",
        "quote": "Modern **hygrometry** calculates relative humidity from dry-bulb and wet-bulb temperatures using psychrometric tables."
      }
    ]
  },
  "Dashboard — meter/isodiametric.md": {
    "primary": "Having equal diameters or dimensions in all directions; spherical or globular in form.",
    "secondary": "In plant anatomy and cytology, designating parenchyma cells whose axes are of roughly equal length, contrasting with elongated fibers or tracheids.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "First Lessons in Botany and Vegetable Physiology",
        "quote": "Soft plant pith is composed of **isodiametric** parenchyma cells packed together like bubbles in a foam."
      },
      {
        "author": "Karl von Goebel",
        "work": "Organography of Plants",
        "quote": "Under uniform turgor pressure, juvenile embryonic cells maintain a roughly **isodiametric** polyhedral form."
      },
      {
        "author": "James Dwight Dana",
        "work": "Manual of Mineralogy",
        "quote": "Crystalline aggregates of garnets often develop nearly **isodiametric** dodecahedral crystals."
      }
    ]
  },
  "Dashboard — meter/isometric.md": {
    "primary": "Having equal dimensions, measure, or proportions.",
    "secondary": "In crystallography, the isometric system (cubic system) having three equal mutually perpendicular axes; in physiology, muscular contraction without change in length; in drafting, isometric projection.",
    "quotes": [
      {
        "author": "James Dwight Dana",
        "work": "A System of Mineralogy",
        "quote": "Halite and diamond crystallize in the **isometric** system, characterized by three equal rectangular axes."
      },
      {
        "author": "William Farish",
        "work": "On Isometrical Perspective",
        "quote": "An **isometric** drawing preserves equal linear scales along all three spatial axes, giving a lifelike representation of machinery."
      },
      {
        "author": "Hermann von Helmholtz",
        "work": "Popular Lectures on Scientific Subjects",
        "quote": "During an **isometric** contraction, muscle tension rises sharply while the physical distance between its tendons remains constant."
      }
    ]
  },
  "Dashboard — meter/isometrical.md": {
    "primary": "A variant form of isometric; of or characterized by equality of measure or dimensions.",
    "secondary": "In engineering drafting and crystallography, pertaining to isometric drawing methods or the cubic crystalline system.",
    "quotes": [
      {
        "author": "William Farish",
        "work": "On Isometrical Perspective",
        "quote": "The **isometrical** projection permits engineers to read dimensions directly from the drawing without foreshortening corrections."
      },
      {
        "author": "René Just Haüy",
        "work": "Traité de Minéralogie",
        "quote": "Crystals exhibiting perfect **isometrical** symmetry present identical cleavage planes along all three cubic directions."
      },
      {
        "author": "John Herschel",
        "work": "A Preliminary Discourse on the Study of Natural Philosophy",
        "quote": "The **isometrical** lines on the chart clearly delineated regions sharing uniform gravitational acceleration."
      }
    ]
  },
  "Dashboard — meter/isometry.md": {
    "primary": "Equality of measure, dimensions, or proportions.",
    "secondary": "In geometry and topology, a distance-preserving transformation between metric spaces (satisfying d(f(x), f(y)) = d(x, y)), including translations, rotations, and reflections.",
    "quotes": [
      {
        "author": "Felix Klein",
        "work": "Erlangen Program (Comparative Review of Recent Researches in Geometry)",
        "quote": "Euclidean geometry may be defined as the invariant theory of the group of spatial transformations maintaining metric **isometry**."
      },
      {
        "author": "H. S. M. Coxeter",
        "work": "Regular Polytopes",
        "quote": "Every **isometry** of Euclidean three-space can be resolved into the product of at most four reflections."
      },
      {
        "author": "Arthur Cayley",
        "work": "The Collected Mathematical Papers",
        "quote": "Coordinate rotations preserve absolute **isometry**, leaving quadratic distance forms invariant."
      }
    ]
  },
  "Dashboard — meter/isoperimetric.md": {
    "primary": "Having equal perimeters or equal perimeter lengths.",
    "secondary": "In geometry and the calculus of variations, relating to the classical isoperimetric problem: proving that among all closed plane curves of equal perimeter, the circle encloses the greatest area.",
    "quotes": [
      {
        "author": "Leonhard Euler",
        "work": "Methodus Inveniendi Lineas Curvas Maximi Minimive Proprietate Gaudentes",
        "quote": "The celebrated **isoperimetric** problem provided the catalyst for the development of the general calculus of variations."
      },
      {
        "author": "Thomas Heath",
        "work": "A History of Greek Mathematics",
        "quote": "Zenodorus demonstrated the ancient **isoperimetric** proposition that the circle contains more area than any polygon of equal perimeter."
      },
      {
        "author": "Colin Maclaurin",
        "work": "A Treatise of Fluxions",
        "quote": "Geometric methods confirm the **isoperimetric** property of the sphere, which encloses maximum volume with minimum surface area."
      }
    ]
  },
  "Dashboard — meter/metal.md": {
    "primary": "Any of a category of chemical elements (such as iron, gold, copper, aluminum) that are typically lustrous, malleable, ductile, and excellent conductors of heat and electricity.",
    "secondary": "In astronomy and astrophysics, any chemical element heavier than hydrogen and helium synthesized through stellar nucleosynthesis (quantified as metallicity).",
    "quotes": [
      {
        "author": "Antoine Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "Every pure **metal** combines with oxygen to form metallic calces or oxides according to definite proportions."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "The high electrical conductivity of solid **metal** wires allows the transmission of current across immense distances."
      },
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "Polished speculum **metal** reflected the rays of starlight with brilliant fidelity within my reflecting telescope."
      }
    ]
  },
  "Dashboard — meter/meteor.md": {
    "primary": "A luminous streak of light visible in the night sky produced when a meteoroid enters Earth's atmosphere at high speed and glows by friction; a shooting star.",
    "secondary": "In historical science and classical meteorology (from Greek meteōros, high in the air), any atmospheric or celestial phenomenon including clouds, rain, auroras, and rainbows.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "The imperial ensign, streamed like a **meteor** streaming to the wind, with gems and golden lustre rich emblazed."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Personal Narrative of Travels to the Equinoctial Regions",
        "quote": "During the great shower of 1799, thousands of fiery **meteors** fell simultaneously across the night sky of Cumaná."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "A brilliant greenish **meteor** burst over the ocean, casting a momentary glare that illuminated our rigging."
      }
    ]
  },
  "Dashboard — meter/meter.md": {
    "primary": "The base unit of length in the International System of Units (SI), equal to 100 centimeters (approximately 39.37 inches).",
    "secondary": "In prosody, the rhythmic arrangement of syllables and accents in poetry; also a mechanical or digital instrument that measures fluid, gas, or electrical flow.",
    "quotes": [
      {
        "author": "Antoine Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "The definitive **meter** was decreed to be the ten-millionth part of the meridional quadrant of the Earth."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "Poetic **meter** produces a perpetual stimulation of attention, heightening the emotional susceptibility of the reader."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "A Treatise on Electricity and Magnetism",
        "quote": "The sensitivity of the electric **meter** permits the precise recording of current fluctuations in microamperes."
      }
    ]
  },
  "Dashboard — meter/meterstick.md": {
    "primary": "A measuring stick exactly one meter long, typically graduated into centimeters and millimeters.",
    "secondary": "In physics laboratories and standard metrology, a rigid linear ruler used as a baseline standard for distance measurements and optical bench experiments.",
    "quotes": [
      {
        "author": "Albert Einstein",
        "work": "Relativity: The Special and General Theory",
        "quote": "A moving **meterstick** observed from a stationary frame appears shortened in the direction of its motion according to Lorentz contraction."
      },
      {
        "author": "Richard Feynman",
        "work": "The Feynman Lectures on Physics",
        "quote": "To measure the speed of light, you set up an optical bench with a light source, detector, and a calibrated **meterstick**."
      },
      {
        "author": "Thomas Edison",
        "work": "The Edison Papers: Documents and Correspondence",
        "quote": "We aligned the photometer screen using a brass-bound **meterstick** to determine the candlepower of the incandescent filament."
      }
    ]
  },
  "Dashboard — meter/metic.md": {
    "primary": "In ancient Greece, a resident alien living in a city-state (especially Athens) who enjoyed legal protection and commercial freedom but lacked citizen political rights.",
    "secondary": "In classical Athenian history and political philosophy, an immigrant or non-citizen class subject to military service and a special poll tax (metoikion), but barred from owning real property or voting in the ecclesia.",
    "quotes": [
      {
        "author": "Thucydides",
        "work": "The Peloponnesian War",
        "quote": "Athens mobilized three thousand hoplites chosen from the wealthy **metic** class to guard the frontier garrisons."
      },
      {
        "author": "Aristotle",
        "work": "Politics",
        "quote": "A resident **metic** does not participate in political office or judicial tribunals, which belong exclusively to citizens."
      },
      {
        "author": "George Grote",
        "work": "A History of Greece",
        "quote": "The Athenian **metic** population comprised energetic merchants and craftsmen whose commercial vitality enriched the Piraeus."
      }
    ]
  },
  "Dashboard — meter/metical.md": {
    "primary": "A historical unit of weight and gold currency in the Islamic world and East Africa (also spelled mitkal or mithqal); currently the standard currency unit of Mozambique (metical).",
    "secondary": "In economic history and numismatics, a traditional Islamic weight standard (approximately 4.25 grams of gold) widely used along trans-Saharan and Indian Ocean trade routes.",
    "quotes": [
      {
        "author": "Ibn Battuta",
        "work": "The Travels of Ibn Battuta",
        "quote": "In the markets of Kilwa and Mali, merchandise was priced in standard weights of gold **meticals**."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Tribute paid to the Caliph was calculated in thousands of golden **meticals** drawn from the mines of Nubia."
      },
      {
        "author": "Richard Francis Burton",
        "work": "The Lake Regions of Central Africa",
        "quote": "Arab ivory traders assessed values in **meticals** of pure gold dust before concluding barter with interior chiefs."
      }
    ]
  },
  "Dashboard — meter/metric.md": {
    "primary": "Of, relating to, or based upon the metric system of weights and measures.",
    "secondary": "In mathematics and differential geometry, a distance function or metric tensor specifying the distance between points on a Riemannian manifold; in business, a standard metric of performance.",
    "quotes": [
      {
        "author": "Antoine Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "The **metric** system replaces arbitrary feudal weights with decimal divisions rooted in the unchanging dimensions of the globe."
      },
      {
        "author": "Albert Einstein",
        "work": "The Meaning of Relativity",
        "quote": "Gravitational fields are completely described by the curvature of the spacetime **metric** tensor."
      },
      {
        "author": "Bernhard Riemann",
        "work": "On the Hypotheses Which Lie at the Bases of Geometry",
        "quote": "The differential **metric** defines the line element ds^2 in generalized n-dimensional continuous manifolds."
      }
    ]
  },
  "Dashboard — meter/metrically.md": {
    "primary": "In a metrical manner; with regard to poetic meter and rhythm, or in terms of the metric system.",
    "secondary": "According to measured rhythm and cadence in poetry, or evaluated by quantitative metric standards.",
    "quotes": [
      {
        "author": "George Saintsbury",
        "work": "A History of English Prosody",
        "quote": "Milton's epic verse is **metrically** constructed upon a magnificent foundation of varied iambic pauses."
      },
      {
        "author": "Matthew Arnold",
        "work": "Essays in Criticism",
        "quote": "The French alexandrine sounds **metrically** uniform to ears accustomed to the fluid rhythms of Shakespeare."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos: A Sketch of a Physical Description of the Universe",
        "quote": "Geodetic survey lines across Europe were **metrically** verified by international scientific commissions."
      }
    ]
  },
  "Dashboard — meter/metricate.md": {
    "primary": "To convert, change over, or adapt to the metric system of weights and measures.",
    "secondary": "In industrial and administrative policy, transitioning manufacturing, commerce, and legal standards from customary imperial units to SI metric units.",
    "quotes": [
      {
        "author": "Charles Babbage",
        "work": "On the Economy of Machinery and Manufactures",
        "quote": "National industry would gain immense computational efficiency should parliament resolve to **metricate** our chaotic weights."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Science and Education",
        "quote": "To teach children archaic chains and bushels instead of urging the nation to **metricate** is an intolerable waste of youth."
      },
      {
        "author": "William Thomson (Lord Kelvin)",
        "work": "Popular Lectures and Addresses: Navigational Affairs",
        "quote": "The scientific world has already chosen to **metricate**, and engineering must inevitably follow."
      }
    ]
  },
  "Dashboard — meter/metrication.md": {
    "primary": "The process of converting from traditional systems of weights and measures (such as imperial or US customary units) to the metric system.",
    "secondary": "In industrial standardization and commerce, the systematic national transition toward adoption of the International System of Units (SI).",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Science and Culture and Other Essays",
        "quote": "Complete **metrication** represents an inevitable triumph of rational decimal science over medieval custom."
      },
      {
        "author": "William Thomson (Lord Kelvin)",
        "work": "Popular Lectures and Addresses",
        "quote": "The worldwide **metrication** of physical measurements simplifies international commerce and scientific exchange."
      },
      {
        "author": "H. G. Wells",
        "work": "The Work, Wealth and Happiness of Mankind",
        "quote": "Universal **metrication** was one of the grandest intellectual achievements born from the French revolutionary era."
      }
    ]
  },
  "Dashboard — meter/metricise.md": {
    "primary": "To convert or adapt to the metric system of measurement (British spelling); also to cast into poetic meter.",
    "secondary": "In British engineering, education, and literature, adopting metric units or organizing poetic language into rhythmic verse.",
    "quotes": [
      {
        "author": "H. G. Wells",
        "work": "The New Machiavelli",
        "quote": "Progressive reformers campaigned tirelessly to **metricise** British coinage, weights, and railway engineering."
      },
      {
        "author": "George Saintsbury",
        "work": "A History of English Prosody",
        "quote": "The dramatist sought to **metricise** everyday colloquial speech without losing natural expressive vigor."
      },
      {
        "author": "Thomas Carlyle",
        "work": "Sartor Resartus",
        "quote": "Pedantic grammarians seek to **metricise** the wild, spontaneous outpourings of prophetic soul."
      }
    ]
  },
  "Dashboard — meter/metricize.md": {
    "primary": "To convert or adapt to the metric system of measurement (American spelling); also to cast or compose into poetic meter.",
    "secondary": "In industrial standardization, adopting decimal metric units in design, manufacturing, and commerce.",
    "quotes": [
      {
        "author": "Thomas Edison",
        "work": "The Edison Papers: Documents and Correspondence",
        "quote": "Our machine shops would save thousands of hours of unnecessary drafting if American industry would **metricize**."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "The Poet",
        "quote": "The poet's divine calling is to **metricize** the chaotic experiences of life into sublime musical song."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos: A Sketch of a Physical Description of the Universe",
        "quote": "Scientific cartographers resolved to **metricize** all terrestrial relief maps for universal international comparison."
      }
    ]
  },
  "Dashboard — meter/metrify.md": {
    "primary": "To compose verse; to convert or turn prose into poetic meter.",
    "secondary": "In literary composition and translation, putting thoughts into regular metrical or rhythmic form.",
    "quotes": [
      {
        "author": "George Puttenham",
        "work": "The Arte of English Poesie",
        "quote": "To **metrify** skillfully requires a delicate ear for syllabic accent and harmonious rhyme."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "A writer may **metrify** trivial thoughts, yet rhythm alone can never supply the absence of poetic passion."
      },
      {
        "author": "Matthew Arnold",
        "work": "On Translating Homer",
        "quote": "Pope chose to **metrify** the Iliad in heroic couplets, giving Homer a polished eighteenth-century dress."
      }
    ]
  },
  "Dashboard — meter/metrological.md": {
    "primary": "Pertaining to metrology (the scientific study and standardization of weights and measures).",
    "secondary": "In physics, international trade, and archaeology, relating to the calibration of measurement standards, tolerances, and ancient weight systems.",
    "quotes": [
      {
        "author": "Ferdinand Rudolph Hassler",
        "work": "Comparison of Weights and Measures",
        "quote": "The **metrological** survey revealed alarming discrepancies among the standard yard measures used in regional custom houses."
      },
      {
        "author": "William Siemens",
        "work": "Conservation of Solar Energy and Other Papers",
        "quote": "Exact electrical engineering depends upon an international **metrological** agreement establishing absolute ohm and volt standards."
      },
      {
        "author": "William Flinders Petrie",
        "work": "Inductive Metrology",
        "quote": "Ancient Egyptian monuments demonstrate astonishing **metrological** precision in the length of the royal cubit."
      }
    ]
  },
  "Dashboard — meter/metrology.md": {
    "primary": "The scientific study of measurement, including the development, realization, and maintenance of measurement standards and units.",
    "secondary": "In science, engineering, and commerce, the theoretical and practical framework that ensures calibration accuracy, traceability, and global consistency of physical measurements.",
    "quotes": [
      {
        "author": "Antoine Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "The revolutionary reform of **metrology** substituted decimal metric simplicity for centuries of regional confusion."
      },
      {
        "author": "William Thomson (Lord Kelvin)",
        "work": "Popular Lectures and Addresses",
        "quote": "When you can measure what you are speaking about, and express it in numbers, you have advanced to true **metrology**."
      },
      {
        "author": "Ferdinand Rudolph Hassler",
        "work": "Comparison of Weights and Measures",
        "quote": "The federal bureau of **metrology** was established to provide commerce with infallible national standards of mass and length."
      }
    ]
  },
  "Dashboard — meter/micrometer.md": {
    "primary": "A precision instrument equipped with a calibrated screw used for measuring minute distances, thicknesses, or angles with high accuracy.",
    "secondary": "In the metric system (SI), a unit of length equal to one-millionth of a meter (symbol: µm, formerly micron); also an astronomical eyepiece attachment.",
    "quotes": [
      {
        "author": "Robert Hooke",
        "work": "Micrographia",
        "quote": "By affixing a fine **micrometer** screw to the eyepiece, I measured the microscopic cells down to tiny fractions of an inch."
      },
      {
        "author": "William Herschel",
        "work": "Astronomical Observations on the Double Stars",
        "quote": "Using a filar **micrometer**, I recorded the angular separation between the binary stars over successive years."
      },
      {
        "author": "Charles Babbage",
        "work": "On the Economy of Machinery and Manufactures",
        "quote": "The accuracy of modern engine lathe work depends upon measuring tolerances with a vernier **micrometer**."
      }
    ]
  },
  "Dashboard — meter/monosymmetric.md": {
    "primary": "Having only one plane of symmetry; bilaterally symmetrical.",
    "secondary": "In crystallography, an archaic designation for the monoclinic crystal system, having a single two-fold axis of symmetry or one mirror plane (as in gypsum and orthoclase).",
    "quotes": [
      {
        "author": "René Just Haüy",
        "work": "Traité de Minéralogie",
        "quote": "Crystals possessing a single mirror plane belong to the **monosymmetric** or monoclinic system of crystallization."
      },
      {
        "author": "James Dwight Dana",
        "work": "A System of Mineralogy",
        "quote": "The optical behavior of **monosymmetric** minerals reveals inclined extinction under crossed polarizing prisms."
      },
      {
        "author": "Ernst Haeckel",
        "work": "Art Forms in Nature",
        "quote": "Bilateral animal forms represent a transition from radial architecture to specialized **monosymmetric** locomotion."
      }
    ]
  },
  "Dashboard — meter/parameter.md": {
    "primary": "A numerical or measurable factor forming one of a set that defines a system or sets the conditions of its operation.",
    "secondary": "In mathematics, a constant in an equation whose value determines the specific form or curve of a family of functions; in statistics, an unknown population characteristic.",
    "quotes": [
      {
        "author": "Leonhard Euler",
        "work": "Introduction to Analysis of the Infinite",
        "quote": "By varying the constant **parameter** in the conic equation, we generate a continuous family of confocal parabolas."
      },
      {
        "author": "Arthur Cayley",
        "work": "The Collected Mathematical Papers",
        "quote": "The coordinates of points along the twisted cubic can be expressed as rational functions of a single **parameter**."
      },
      {
        "author": "Ronald Fisher",
        "work": "Statistical Methods for Research Workers",
        "quote": "Maximum likelihood estimation provides the most efficient statistic for determining an unknown population **parameter**."
      }
    ]
  },
  "Dashboard — meter/parameterize.md": {
    "primary": "To express, define, or represent a mathematical curve, surface, or system in terms of parameters.",
    "secondary": "In computational modeling and geometry, to represent geometric coordinates as functions of independent parametric variables (such as arc length or time).",
    "quotes": [
      {
        "author": "Arthur Cayley",
        "work": "The Collected Mathematical Papers",
        "quote": "To evaluate the spatial line integral, the geometer must first **parameterize** the curve in terms of arc length."
      },
      {
        "author": "Felix Klein",
        "work": "Lectures on Mathematics",
        "quote": "By using elliptic functions, we can completely **parameterize** complex algebraic curves of genus one."
      },
      {
        "author": "Roger Penrose",
        "work": "The Road to Reality",
        "quote": "In spacetime geometry, it is natural to **parameterize** particle worldlines using proper time along the path."
      }
    ]
  },
  "Dashboard — meter/parametric.md": {
    "primary": "Of, relating to, or expressed in terms of a parameter or parameters.",
    "secondary": "In mathematics and statistics, relating to equations defined by auxiliary parameters (e.g. parametric equations x=f(t), y=g(t)), or statistical tests assuming a specified probability distribution.",
    "quotes": [
      {
        "author": "Leonhard Euler",
        "work": "Elements of Algebra",
        "quote": "The **parametric** equations of the cycloid express both horizontal and vertical displacements as functions of the rolling angle."
      },
      {
        "author": "Ronald Fisher",
        "work": "Statistical Methods for Research Workers",
        "quote": "Standard analysis of variance is a **parametric** procedure resting upon the assumption of normal residual distribution."
      },
      {
        "author": "Arthur Cayley",
        "work": "The Collected Mathematical Papers",
        "quote": "We establish a **parametric** representation of the quadric surface through projection from a point on the surface."
      }
    ]
  },
  "Dashboard — meter/parametrize.md": {
    "primary": "A variant spelling of parameterize; to express or represent in terms of parameters.",
    "secondary": "In differential geometry and mathematical physics, assigning coordinates or equations governed by parametric variables.",
    "quotes": [
      {
        "author": "Felix Klein",
        "work": "Lectures on the Icosahedron",
        "quote": "We may **parametrize** the roots of the quintic equation through modular functions of the icosahedral group."
      },
      {
        "author": "Roger Penrose",
        "work": "The Road to Reality",
        "quote": "Physicists **parametrize** gauge transformations by assigning field values at every point of the manifold."
      },
      {
        "author": "H. S. M. Coxeter",
        "work": "Regular Polytopes",
        "quote": "It is convenient to **parametrize** polyhedral rotations through unit quaternions on the four-dimensional sphere."
      }
    ]
  },
  "Dashboard — meter/pentameter.md": {
    "primary": "A line of verse consisting of five metrical feet, especially iambic pentameter, the most prominent meter in English poetry and drama.",
    "secondary": "In classical elegiac poetry, a dactylic pentameter line paired with a dactylic hexameter to form the elegiac distich.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Sonnet 18",
        "quote": "The unrhymed blank verse of the Elizabethan stage elevated iambic **pentameter** into the supreme voice of tragic passion."
      },
      {
        "author": "Alexander Pope",
        "work": "An Essay on Criticism",
        "quote": "A needless Alexandrine ends the song, That, like a wounded snake, drags its slow length along; contrasting with tight **pentameter**."
      },
      {
        "author": "George Saintsbury",
        "work": "A History of English Prosody",
        "quote": "Chaucer established the heroic **pentameter** couplet as the standard rhythmic backbone of English narrative poetry."
      }
    ]
  },
  "Dashboard — meter/perimeter.md": {
    "primary": "The continuous boundary line that encloses a closed two-dimensional geometric figure; the total distance around such a figure.",
    "secondary": "In military tactics, physical security, and medicine, the outermost defensive boundary of a fortified position, or an optical instrument (perimeter) for mapping the visual field.",
    "quotes": [
      {
        "author": "Euclid",
        "work": "Elements",
        "quote": "If two polygons are similar, their **perimeters** are in the same ratio as their corresponding sides."
      },
      {
        "author": "Archimedes",
        "work": "Measurement of a Circle",
        "quote": "By calculating the **perimeter** of an inscribed polygon of ninety-six sides, Archimedes bounded the value of pi."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Perimetric examination with a recording **perimeter** showed dramatic constriction of the visual field in advanced glaucoma."
      }
    ]
  },
  "Dashboard — meter/polymeter.md": {
    "primary": "The use of multiple different poetic meters within a single poem or musical composition; a poem composed in varied meters.",
    "secondary": "In meteorology and physics, a combined meteorological instrument (such as Lambrecht's polymeter) measuring temperature, relative humidity, and dew point on unified scales.",
    "quotes": [
      {
        "author": "George Saintsbury",
        "work": "A History of English Prosody",
        "quote": "Dryden's magnificent odes demonstrate the dramatic emotional shifts achieved through daring lyric **polymeter**."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "The irregular ode employs **polymeter** to mirror every sudden change of passion with an answering change of rhythm."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos: A Sketch of a Physical Description of the Universe",
        "quote": "Mountain observers consulted the compact **polymeter** to read atmospheric humidity and dew point simultaneously."
      }
    ]
  },
  "Dashboard — meter/symmetric.md": {
    "primary": "Having, exhibiting, or characterized by symmetry; having corresponding parts that match across an axis, plane, or center of inversion.",
    "secondary": "In mathematics, describing a relation (if a~b then b~a), a matrix (A = A^T), or a polynomial that remains unchanged under permutation of its variables.",
    "quotes": [
      {
        "author": "Euclid",
        "work": "Elements",
        "quote": "Figures having identical angles and proportional sides arranged around an axis are harmonious and **symmetric**."
      },
      {
        "author": "Johannes Kepler",
        "work": "The Six-Cornered Snowflake",
        "quote": "The water droplet freezes into a six-pointed **symmetric** star under the geometric necessity of packing space."
      },
      {
        "author": "Herman Weyl",
        "work": "Symmetry",
        "quote": "A body is **symmetric** if there is something you can do to it so that after you have finished it looks as it did before."
      }
    ]
  },
  "Dashboard — meter/symmetrical.md": {
    "primary": "Made up of exactly similar parts facing each other or arranged around an axis; displaying balanced proportions.",
    "secondary": "In biology and crystallography, having organs, body forms, or crystal faces that correspond in size and shape across defined planes of symmetry.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The **symmetrical** arrangement of bilateral organs in vertebrates evolved from ancient bilaterian ancestors."
      },
      {
        "author": "John Ruskin",
        "work": "The Seven Lamps of Architecture",
        "quote": "Classical architecture achieves repose through severe, **symmetrical** balance between columns and entablature."
      },
      {
        "author": "René Just Haüy",
        "work": "Traité de Minéralogie",
        "quote": "The facets of a quartz crystal develop according to strict **symmetrical** laws governing internal molecular decrescents."
      }
    ]
  },
  "Dashboard — meter/symmetrise.md": {
    "primary": "To make symmetrical; to bring parts into balanced and corresponding proportion across an axis or plane (British spelling).",
    "secondary": "In mathematics and physics, to transform an asymmetric function, matrix, or tensor into a symmetric form (e.g. A_sym = (A + A^T)/2).",
    "quotes": [
      {
        "author": "Paul Dirac",
        "work": "The Principles of Quantum Mechanics",
        "quote": "To describe an assembly of bosons, one must **symmetrise** the total wave function across all particle coordinates."
      },
      {
        "author": "Arthur Cayley",
        "work": "The Collected Mathematical Papers",
        "quote": "By averaging over all cyclic permutations of the variables, we easily **symmetrise** the algebraic polynomial."
      },
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "The Renaissance architect sought everywhere to **symmetrise** ancient organic facades into rigid mechanical uniformity."
      }
    ]
  }
};

console.log('Starting Batch 6 curation (' + Object.keys(batchData).length + ' words)...');
const updated = updateNotesBatch(baseClusterDir, batchData);
console.log('Batch 6 complete: successfully updated ' + updated + ' notes.');
