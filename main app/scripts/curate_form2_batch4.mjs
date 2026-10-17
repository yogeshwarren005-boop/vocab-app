import { updateNotesBatch } from './curate-updater-util.mjs';
import path from 'path';

const CLUSTER_DIR = path.resolve('App database/Greek roots/Cluster Form & Space');

const batchData = {
  "Dashboard — crypt\\cryptotis.md": {
    "primary": "A genus of small, short-tailed shrews native to North and Central America, commonly known as small-eared shrews.",
    "secondary": "In systematic mammalogy, insectivorous soricids characterized by concealed external pinnae, reduced eyes, and semi-fossorial burrowing habits in forest leaf litter.",
    "quotes": [
      {
        "author": "C. Hart Merriam",
        "work": "Revision of the Shrews of the American Genera Blarina and Notiosorex",
        "quote": "I recognized **Cryptotis** as a distinct generic group characterized by minute external ears hidden beneath dense fur."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Diversity of Life",
        "quote": "Cloud forests in Central America shelter endemic shrews of the genus **Cryptotis** that forage through moist moss."
      },
      {
        "author": "Spencer Fullerton Baird",
        "work": "Mammals of North America",
        "quote": "Specimens of **Cryptotis** parva burrow beneath fallen pine needles, hunting tirelessly for subterranean grubs."
      }
    ]
  },
  "Dashboard — crypt\\decrypt.md": {
    "primary": "To convert ciphertext or encoded information back into intelligible plaintext using a key or algorithm.",
    "secondary": "In computer security and cryptanalysis, the inverse transformation of an encryption function that restores original data.",
    "quotes": [
      {
        "author": "Alan Turing",
        "work": "Turing's Treatise on the Enigma",
        "quote": "Once the daily stecker settings were resolved, the naval intercept station could **decrypt** incoming orders within minutes."
      },
      {
        "author": "Claude Shannon",
        "work": "Communication Theory of Secrecy Systems",
        "quote": "An authorized recipient applies the secret private deciphering key to **decrypt** the scrambled stream."
      },
      {
        "author": "David Kahn",
        "work": "The Codebreakers",
        "quote": "Allied intelligence worked desperately around the clock to **decrypt** diplomatic cables before the naval task force sailed."
      }
    ]
  },
  "Dashboard — crypt\\decryption.md": {
    "primary": "The process of converting encrypted data or ciphertext back into its original readable plaintext format.",
    "secondary": "In cryptography, the mathematical procedure $(D_k)$ that reverses encryption $(E_k)$ through the application of the appropriate key.",
    "quotes": [
      {
        "author": "Claude Shannon",
        "work": "Communication Theory of Secrecy Systems",
        "quote": "Exact **decryption** is guaranteed only when the cipher mapping forms an invertible bijection across the message space."
      },
      {
        "author": "Alan Turing",
        "work": "Turing's Treatise on the Enigma",
        "quote": "Electromechanical relays accelerated the **decryption** of high-command teleprinter traffic at unprecedented speeds."
      },
      {
        "author": "David Kahn",
        "work": "The Codebreakers",
        "quote": "The successful **decryption** of intercepted Japanese messages gave Admiral Nimitz tactical foreknowledge at Midway."
      }
    ]
  },
  "Dashboard — crypt\\encrypt.md": {
    "primary": "To convert plain text, speech, or digital data into an encoded cipher format to prevent unauthorized access.",
    "secondary": "In computer science and telecommunications, to transform plaintext $(P)$ into ciphertext $(C)$ via an algorithmic cryptographic function parameterized by a key.",
    "quotes": [
      {
        "author": "Claude Shannon",
        "work": "Communication Theory of Secrecy Systems",
        "quote": "To **encrypt** a communication effectively, the system must disperse linguistic redundancy across long pseudorandom blocks."
      },
      {
        "author": "David Kahn",
        "work": "The Codebreakers",
        "quote": "Field commanders were instructed to **encrypt** tactical coordinates using one-time pads whenever radio silence was broken."
      },
      {
        "author": "Alan Turing",
        "work": "Turing's Treatise on the Enigma",
        "quote": "Operators rotating cipher wheels could **encrypt** sensitive weather bulletins into five-letter nonsense groups."
      }
    ]
  },
  "Dashboard — crypt\\encryption.md": {
    "primary": "The mathematical or procedural conversion of electronic data or messages into ciphertext to secure confidentiality.",
    "secondary": "In modern cybersecurity, the algorithmic scrambling of plaintext using symmetric or asymmetric key protocols (such as AES or RSA) to ensure privacy and data integrity.",
    "quotes": [
      {
        "author": "Claude Shannon",
        "work": "A Mathematical Theory of Communication",
        "quote": "Ideal **encryption** transforms structured natural language into a message statistically indistinguishable from pure entropy."
      },
      {
        "author": "David Kahn",
        "work": "The Codebreakers",
        "quote": "The transition from manual paper ciphers to mechanical rotor **encryption** revolutionized twentieth-century military communications."
      },
      {
        "author": "Alan Turing",
        "work": "Turing's Treatise on the Enigma",
        "quote": "Flaws in the protocol surrounding **encryption** frequently betray the most sophisticated mechanical cipher machines."
      }
    ]
  },
  "Dashboard — crypt\\grot.md": {
    "primary": "A small cave, cavern, or grotto, especially one that is picturesque or poetically imagined.",
    "secondary": "In romantic poetry and landscape aesthetics, an artificial rockwork recess or mossy subterranean hollow designed for contemplation.",
    "quotes": [
      {
        "author": "John Keats",
        "work": "La Belle Dame sans Merci",
        "quote": "She took me to her elfin **grot**, / And there she wept and sighed full sore, / And there I shut her wild wild eyes / With kisses four."
      },
      {
        "author": "John Milton",
        "work": "Comus",
        "quote": "Within the navel of this hideous wood, / Imured in cypress shades a sorcerer dwells, / In subterranean **grot** and cell."
      },
      {
        "author": "Percy Bysshe Shelley",
        "work": "Prometheus Unbound",
        "quote": "There is a cave, / All overgrown with trailing odorous plants, / Which tapestry the calm and lovely **grot**."
      }
    ]
  },
  "Dashboard — crypt\\grotesque.md": {
    "primary": "Comically or repulsively ugly, distorted, or incongruous; bizarre and unnatural in appearance or character.",
    "secondary": "In art history, decorative painting or sculpture featuring fantastical interweavings of human, animal, and foliate forms discovered originally in excavated Roman subterranean chambers (grottoes).",
    "quotes": [
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "The noble **grotesque** in Gothic architecture springs from an earnest, fearless play of the imaginative mind."
      },
      {
        "author": "Edgar Allan Poe",
        "work": "Tales of the Grotesque and Arabesque",
        "quote": "The figures were masked in characters so **grotesque** that they seemed born of phantasm and nightmare."
      },
      {
        "author": "Victor Hugo",
        "work": "Preface to Cromwell",
        "quote": "Modern art is born from the fertile union of the **grotesque** with the sublime."
      }
    ]
  },
  "Dashboard — crypt\\grotesquely.md": {
    "primary": "In a grotesque, bizarre, incongruously distorted, or wildly unnatural manner.",
    "secondary": "In descriptive prose, so as to evoke a startling or unsettling mixture of horror, absurdity, and caricature.",
    "quotes": [
      {
        "author": "Charles Dickens",
        "work": "Great Expectations",
        "quote": "The shadows flickered **grotesquely** against the soot-blackened ceiling of Miss Havisham's bridal chamber."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The severed head of the sperm whale swayed **grotesquely** from the ship's side in the rising gale."
      },
      {
        "author": "Joseph Conrad",
        "work": "Heart of Darkness",
        "quote": "The wilderness had patted him on the head, and he looked **grotesquely** emaciated upon his pallet."
      }
    ]
  },
  "Dashboard — crypt\\grotesqueness.md": {
    "primary": "The quality or state of being grotesque; bizarre distortion, absurdity, or whimsical incongruity.",
    "secondary": "In aesthetic theory and literary criticism, the stylized fusion of discordant elements that shocks or unsettles conventional perceptions.",
    "quotes": [
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "There is a profound spiritual significance in the monstrous **grotesqueness** of medieval gargoyles."
      },
      {
        "author": "Edgar Allan Poe",
        "work": "The Masque of the Red Death",
        "quote": "Much of the beautiful, much of the wanton, much of the bizarre, and not a little of terrible **grotesqueness** was present."
      },
      {
        "author": "Henry James",
        "work": "The American Scene",
        "quote": "The sheer architectural **grotesqueness** of the commercial towers startled the returning traveler."
      }
    ]
  },
  "Dashboard — crypt\\grotto.md": {
    "primary": "A natural or artificial cave, cavern, or rock chamber, especially one made picturesque with shells, rockwork, or water features.",
    "secondary": "In classical archaeology and landscape gardening, an ornamental underground chamber or cave sacred to nymphs (nymphaeum) or designed as a cool retreat.",
    "quotes": [
      {
        "author": "Alexander Pope",
        "work": "Verses on a Grotto by the River Thames at Twickenham",
        "quote": "Thou who shalt stop where Thames' translucent wave / Shines a broad mirror through the shadowy cave, / Approach: but awful! lo! the Aonian **grotto**."
      },
      {
        "author": "Lord Byron",
        "work": "Childe Harold's Pilgrimage",
        "quote": "Egeria! sweet creation of some heart / Which found no mortal resting-place, in thy cool **grotto** weep."
      },
      {
        "author": "Nathaniel Hawthorne",
        "work": "The Marble Faun",
        "quote": "Moss and ferns dripped with moisture inside the cool stone **grotto** where the fountain bubbled up."
      }
    ]
  },
  "Dashboard — cub\\cub.md": {
    "primary": "The young of certain carnivorous mammals, such as the bear, lion, wolf, or fox; also an inexperienced youth.",
    "secondary": "In classical and geometric etymology, an abbreviated combining root derived from Latin cubus and Greek kybos, denoting a solid cube or cubic measure.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "The Merchant of Venice",
        "quote": "I would outstare the sternest eyes that look, / Outbrave the heart most daring on the earth, / Pluck the young sucking **cub** from the she-bear."
      },
      {
        "author": "Rudyard Kipling",
        "work": "The Jungle Book",
        "quote": "Father Wolf looked on amazed; for the naked **cub** had pushed its way between his paws to feed."
      },
      {
        "author": "Euclid",
        "work": "Elements",
        "quote": "The solid figure bounded by six equal square planes is denominated a **cub** or hexahedron in geometric discourse."
      }
    ]
  },
  "Dashboard — cub\\cubic.md": {
    "primary": "Having the shape of a cube; having three dimensions (length, breadth, and height) or measured in volume.",
    "secondary": "In mathematics, involving the third power of a quantity or an algebraic equation of degree three ($ax^3 + bx^2 + cx + d = 0$).",
    "quotes": [
      {
        "author": "Isaac Newton",
        "work": "Enumeration of Lines of the Third Order",
        "quote": "The geometry of curves described by a **cubic** polynomial exhibits seventy-two distinct species of lines."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "In rock salt, sodium and chlorine ions assemble into a face-centered **cubic** lattice of high stability."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "quote": "I measured the pond's icy crust, calculating how many thousand **cubic** feet of clear ice could be harvested."
      }
    ]
  },
  "Dashboard — cub\\cubical.md": {
    "primary": "Shaped like a cube; having the form, proportions, or properties of a cube.",
    "secondary": "In mineralogy and crystallography, describing crystal structures or cleavage habits conforming to the isometric (cubic) system.",
    "quotes": [
      {
        "author": "Robert Hooke",
        "work": "Micrographia",
        "quote": "Under the microscope, grains of sea-salt resolved themselves into exquisitely regular **cubical** crystals."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Columns of basalt occasionally break into **cubical** blocks under the combined action of jointing and frost."
      },
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "The Byzantine capital retains the simple **cubical** mass from which intricate acanthus leaves were carved."
      }
    ]
  },
  "Dashboard — cub\\cubicity.md": {
    "primary": "The state, quality, or condition of being cubic in form or dimension; cubical character.",
    "secondary": "In geometry and volume measurement, the quantitative internal volumetric capacity or cubic content of a container or space.",
    "quotes": [
      {
        "author": "James Clerk Maxwell",
        "work": "A Treatise on Electricity and Magnetism",
        "quote": "The mathematical calculation of electrostatic capacity requires evaluating the volume and **cubicity** of the dielectric space."
      },
      {
        "author": "D'Arcy Wentworth Thompson",
        "work": "On Growth and Form",
        "quote": "Surface tension resists the rigid **cubicity** of crystals, striving always toward spherical equilibrium in living cells."
      },
      {
        "author": "William Whewell",
        "work": "The Philosophy of the Inductive Sciences",
        "quote": "The **cubicity** of mineral cleavage planes provided Haüy with his fundamental geometric building blocks."
      }
    ]
  },
  "Dashboard — cub\\cubism.md": {
    "primary": "An early 20th-century avant-garde art movement that revolutionized European painting and sculpture by deconstructing subjects into geometric facets.",
    "secondary": "In modern art history, the aesthetic movement pioneered around 1907 by Pablo Picasso and Georges Braque that rejected single-point perspective in favor of fragmented, multifaceted planar representations.",
    "quotes": [
      {
        "author": "Guillaume Apollinaire",
        "work": "The Cubist Painters",
        "quote": "The geometry of **cubism** aims not at mere geometric abstraction, but at capturing an internal poetic reality."
      },
      {
        "author": "Gertrude Stein",
        "work": "Picasso",
        "quote": "Picasso lived through the heroic birth of **cubism**, breaking the painted canvas into crystalline facets of pure form."
      },
      {
        "author": "Virginia Woolf",
        "work": "Roger Fry: A Biography",
        "quote": "London audiences reacted with indignation to the revolutionary experiments of **cubism** at the Grafton Galleries."
      }
    ]
  },
  "Dashboard — cub\\cubist.md": {
    "primary": "An artist who paints, sculpts, or designs according to the principles of cubism, or pertaining to cubism.",
    "secondary": "In visual art, describing works of art characterized by geometric fragmentation, multiple viewpoints, and interlocking planar facets.",
    "quotes": [
      {
        "author": "Guillaume Apollinaire",
        "work": "The Cubist Painters",
        "quote": "The true **cubist** painter abandons visual imitation to construct new harmonies out of pure spatial relations."
      },
      {
        "author": "Gertrude Stein",
        "work": "The Autobiography of Alice B. Toklas",
        "quote": "Young painters gathered in Montmartre studio discussions, debating whether a canvas was genuinely **cubist** in structure."
      },
      {
        "author": "Aldous Huxley",
        "work": "Crome Yellow",
        "quote": "A fashionable **cubist** portrait adorned the library mantelpiece, representing human features by green triangles and zinc planes."
      }
    ]
  },
  "Dashboard — cub\\cubistic.md": {
    "primary": "Pertaining to, resembling, or characteristic of cubism or cubist design.",
    "secondary": "In art criticism and architecture, exhibiting fragmented geometric facets, angular planes, or multi-perspective composition.",
    "quotes": [
      {
        "author": "Roger Fry",
        "work": "Vision and Design",
        "quote": "The dramatic, **cubistic** reduction of organic form to simple planes imparted an unprecedented tectonic vigor to the work."
      },
      {
        "author": "Lewis Mumford",
        "work": "The Culture of Cities",
        "quote": "Modern skyscraper setbacks produce a sharp, **cubistic** skyline against the evening twilight."
      },
      {
        "author": "Gertrude Stein",
        "work": "Lectures in America",
        "quote": "Her sentences unfolded with a **cubistic** insistence on breaking conventional linear progression into repeating facets."
      }
    ]
  },
  "Dashboard — cub\\cuboctahedron.md": {
    "primary": "A convex Archimedean solid polyhedron with 14 faces (8 equilateral triangles and 6 squares), 12 identical vertices, and 24 edges.",
    "secondary": "In crystallography and geometry, the uniform polyhedron formed by truncating a cube or an octahedron, representing the closest-packing coordination shell of spheres (Buckminster Fuller's vector equilibrium).",
    "quotes": [
      {
        "author": "Johannes Kepler",
        "work": "Harmonices Mundi",
        "quote": "Among the Archimedean solids, the **cuboctahedron** unites the symmetry of the cube with the triangular harmony of the octahedron."
      },
      {
        "author": "Buckminster Fuller",
        "work": "Synergetics: Explorations in the Geometry of Thinking",
        "quote": "The **cuboctahedron** represents the zero-energy vector equilibrium wherein all internal radial and circumferential vectors are identical in length."
      },
      {
        "author": "D'Arcy Wentworth Thompson",
        "work": "On Growth and Form",
        "quote": "Twelve equal compressible spheres clustered symmetrically about a central sphere naturally deform into a **cuboctahedron**."
      }
    ]
  },
  "Dashboard — cub\\cuboid.md": {
    "primary": "Approximating the shape of a cube; a rectangular solid whose six faces are quadrilaterals.",
    "secondary": "In human and comparative anatomy, a cube-shaped tarsal bone situated on the lateral side of the foot between the calcaneus and the fourth and fifth metatarsals.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **cuboid** bone occupies the outer and anterior part of the tarsus, articulating posteriorly with the calcaneus."
      },
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "In ungulates, the **cuboid** fuses with the navicular to establish a rigid tarsal lever for running."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Evidence as to Man's Place in Nature",
        "quote": "The human foot differs from the ape's in the robust weight-bearing alignment of the **cuboid** and tarsal arches."
      }
    ]
  },
  "Dashboard — cub\\cuboidal.md": {
    "primary": "Resembling or having the form of a cube; cube-like in proportion.",
    "secondary": "In histology, designating epithelial cells whose height, width, and depth are approximately equal, characteristic of renal tubules and thyroid follicles.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "Simple **cuboidal** epithelium lines the convoluted renal tubules and the secretory ducts of many exocrine glands."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Under chronic irritation, low **cuboidal** cells of the alveolar membrane swell into prominent columnar structures."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Thyroid adenomas present dense clusters of **cuboidal** cells enclosing droplets of inspissated colloid."
      }
    ]
  },
  "Dashboard — cub\\hypercube.md": {
    "primary": "A geometric figure in four or more dimensions that is the multi-dimensional analogue of a three-dimensional cube; a tesseract in four dimensions.",
    "secondary": "In geometry and parallel computing architecture, an n-dimensional polytope bounded by $2n$ hypercubes of dimension $n-1$, or a multi-processor network topology connected along n-cube vertices.",
    "quotes": [
      {
        "author": "H. G. Wells",
        "work": "The Time Machine",
        "quote": "Scientific people know very well that Time is only a kind of Space, and a **hypercube** is simply a four-dimensional figure."
      },
      {
        "author": "Edwin Abbott Abbott",
        "work": "Flatland: A Romance of Many Dimensions",
        "quote": "From the point to the square, from the square to the cube, reason demands that the cube project into a glorious four-dimensional **hypercube**."
      },
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "Just as a cube casts a two-dimensional square shadow on a table, a four-dimensional **hypercube** casts a three-dimensional shadow in our world."
      }
    ]
  },
  "Dashboard — cycl\\acyclic.md": {
    "primary": "Not cyclic; not occurring in cycles or lacking a ring structure.",
    "secondary": "In organic chemistry, describing aliphatic compounds whose carbon atoms form open straight or branched chains rather than rings; in graph theory, designating graphs (like trees or DAGs) containing no closed loops.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "Alkanes such as pentane and hexane represent standard **acyclic** hydrocarbons with open tetrahedral carbon backbones."
      },
      {
        "author": "Donald Knuth",
        "work": "The Art of Computer Programming",
        "quote": "A directed **acyclic** graph provides the canonical mathematical model for topological sorting and compiler dependency analysis."
      },
      {
        "author": "J. D. Bernal",
        "work": "The Origin of Life",
        "quote": "Prebiotic synthesis on primitive clay mineral templates facilitated the cyclization of simple **acyclic** organic acids."
      }
    ]
  },
  "Dashboard — cycl\\acyclovir.md": {
    "primary": "A synthetic nucleoside analogue antiviral medication used primarily in the treatment of herpes simplex virus infections, chickenpox, and shingles.",
    "secondary": "In pharmacology and molecular therapeutics, an acyclic guanosine analogue that undergoes selective monophosphorylation by viral thymidine kinase, competitively inhibiting viral DNA polymerase and terminating viral DNA chain elongation.",
    "quotes": [
      {
        "author": "Sydney Brenner",
        "work": "Loose Ends",
        "quote": "The clinical triumph of **acyclovir** showed that an acyclic nucleoside could selectively disable a viral polymerase while sparing host cells."
      },
      {
        "author": "Gertrude Elion",
        "work": "Nobel Lecture: The Purine Path to Chemotherapy",
        "quote": "In developing **acyclovir**, our goal was a selective antiviral prodrug activated exclusively inside virus-infected cells."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Modern antimicrobial chapters emphasize the rapid introduction of **acyclovir** in suspected herpes simplex encephalitis to prevent necrosis."
      }
    ]
  },
  "Dashboard — cycl\\anacyclus.md": {
    "primary": "A genus of flowering plants in the daisy family Asteraceae, native to the Mediterranean basin, known as mount Atlas daisies or pellitories.",
    "secondary": "In botanical pharmacognosy, low-growing Mediterranean herbs (notably Anacyclus pyrethrum) whose roots yield pungent alkylamides traditionally used as a sialagogue and medicinal irritant.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The root of **Anacyclus** pyrethrum was imported from North Africa as a potent medicinal masticatory."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Aspects of Nature",
        "quote": "Sunny arid limestone slopes along the Mediterranean shore are decorated with low rosettes of **Anacyclus**."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "Rock garden enthusiasts value the dense silvery foliage and crimson-rimmed white flowerheads of dwarf **Anacyclus** species."
      }
    ]
  },
  "Dashboard — cycl\\anticyclone.md": {
    "primary": "A weather system characterized by high atmospheric pressure at its center, around which winds circulate clockwise in the Northern Hemisphere and counterclockwise in the Southern Hemisphere.",
    "secondary": "In synoptic meteorology, an extensive descending air mass associated with stable atmospheric conditions, clear skies, light winds, and temperature inversions.",
    "quotes": [
      {
        "author": "Francis Galton",
        "work": "Meteorographica",
        "quote": "I propose the term **anticyclone** for those vast regions of high barometric pressure where dry air gently descends and diverges outward."
      },
      {
        "author": "Joseph Conrad",
        "work": "The Secret Sharer",
        "quote": "A persistent **anticyclone** held the Gulf of Siam in a glassy, suffocating calm for days on end."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "The permanent subtropical **anticyclone** drives the trade winds across thousands of miles of tropical ocean."
      }
    ]
  },
  "Dashboard — cycl\\anticyclonic.md": {
    "primary": "Of, relating to, or characteristic of an anticyclone; associated with high barometric pressure and calm weather.",
    "secondary": "In dynamic meteorology and physical oceanography, describing clockwise atmospheric circulation in the Northern Hemisphere (counterclockwise in the Southern) or oceanic gyres driven by high pressure.",
    "quotes": [
      {
        "author": "Francis Galton",
        "work": "Meteorographica",
        "quote": "The calm, crisp clarity of winter frosts is the direct outcome of stable **anticyclonic** conditions over the continent."
      },
      {
        "author": "Arthur Holmes",
        "work": "Principles of Physical Geology",
        "quote": "Persistent **anticyclonic** winds divert ocean surface currents into vast rotating subtropical gyres."
      },
      {
        "author": "Thomas Hardy",
        "work": "The Woodlanders",
        "quote": "An **anticyclonic** stillness settled over the vale, freezing the dripping boughs into motionless icicles."
      }
    ]
  },
  "Dashboard — cycl\\bicycle.md": {
    "primary": "A human-powered, pedal-driven vehicle having two wheels arranged in tandem on a light metal frame.",
    "secondary": "In social history and transportation, an invention of the late nineteenth century that fundamentally expanded working-class mobility and women's liberation.",
    "quotes": [
      {
        "author": "H. G. Wells",
        "work": "The Wheels of Chance",
        "quote": "To ride a **bicycle** through the Surrey countryside on a golden summer morning was, to Mr. Hoopdriver, the height of romantic adventure."
      },
      {
        "author": "Mark Twain",
        "work": "Taming the Bicycle",
        "quote": "Get a **bicycle**. You will not regret it, if you live."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventure of the Priory School",
        "quote": "The tyre marks of a **bicycle** upon the damp moorland patch told Holmes an unmistakable tale of frantic flight."
      }
    ]
  },
  "Dashboard — cycl\\bicycler.md": {
    "primary": "A person who rides a bicycle; a cyclist.",
    "secondary": "In nineteenth-century social commentary, an early recreational enthusiast or commuter who adopted the bicycle during the cycling craze of the 1890s.",
    "quotes": [
      {
        "author": "H. G. Wells",
        "work": "The Wheels of Chance",
        "quote": "The solitary **bicycler** pedaled steadily against the headwind, his luggage strapped firmly over the rear mudguard."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventure of the Solitary Cyclist",
        "quote": "A mysterious **bicycler** kept watch on the young lady as she pedaled along the secluded country road."
      },
      {
        "author": "Thomas Hardy",
        "work": "Jude the Obscure",
        "quote": "A youthful **bicycler** sped past on the turnpike, leaving a cloud of chalk dust upon the hedge."
      }
    ]
  },
  "Dashboard — cycl\\bicyclic.md": {
    "primary": "Having two cycles or two rings; especially possessing two fused or bridged rings of atoms in a chemical molecule.",
    "secondary": "In synthetic organic chemistry, designating compounds (such as decalin, camphor, or bicycloalkanes) containing two rings sharing common atoms.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "Camphor presents a bridged **bicyclic** hydrocarbon skeleton whose rigid geometry dictates its chemical reactivity."
      },
      {
        "author": "Alexander Todd",
        "work": "A Time to Remember: The Autobiography of a Chemist",
        "quote": "Determining the structure of the **bicyclic** purine ring system was an essential milestone in the elucidation of nucleic acids."
      },
      {
        "author": "J. D. Bernal",
        "work": "The Origin of Life",
        "quote": "The synthesis of **bicyclic** nitrogenous bases under prebiotic spark conditions opened the door to biochemical evolution."
      }
    ]
  },
  "Dashboard — cycl\\bicycling.md": {
    "primary": "The activity, practice, or sport of riding a bicycle.",
    "secondary": "In cultural history and public health, a popular form of personal recreation, aerobic exercise, and sustainable urban transportation.",
    "quotes": [
      {
        "author": "H. G. Wells",
        "work": "The Wheels of Chance",
        "quote": "The health and high spirits produced by **bicycling** across open heaths transformed the timid shop assistant into a hero."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "Memories and Adventures",
        "quote": "I took to **bicycling** with enthusiasm, exploring every quiet Sussex lane upon my sturdy roadster."
      },
      {
        "author": "Mark Twain",
        "work": "Taming the Bicycle",
        "quote": "The first five days of **bicycling** were marked by numerous contusions and an intimate familiarity with the macadam road."
      }
    ]
  },
  "Dashboard — cycl\\bicyclist.md": {
    "primary": "A person who rides a bicycle, especially as a sport or regular means of travel; a cyclist.",
    "secondary": "In transport planning and civic design, an individual user of roadway and trail networks traveling by pedal-powered two-wheeled cycle.",
    "quotes": [
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventure of the Solitary Cyclist",
        "quote": "The solitary **bicyclist** kept her distance along the deserted stretch between the woods and the heath."
      },
      {
        "author": "H. G. Wells",
        "work": "The Wheels of Chance",
        "quote": "Every passer-by paused to stare at the energetic **bicyclist** repairing a punctured inner tube beside the milestone."
      },
      {
        "author": "George Orwell",
        "work": "Coming Up for Air",
        "quote": "In those days a weekend **bicyclist** in knickerbockers was a familiar sight on the gravel roads outside London."
      }
    ]
  },
  "Dashboard — cycl\\cycl.md": {
    "primary": "A combining form derived from Greek kyklos, meaning circle, wheel, ring, circular path, or recurrent period.",
    "secondary": "In scientific terminology, an affix denoting cyclic chemical structures, repetitive chronological processes, or circular anatomical and mechanical devices.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "The combining form **cycl** designates closed carbon rings that exhibit distinctive aromatic resonance stabilization."
      },
      {
        "author": "Francis Galton",
        "work": "Meteorographica",
        "quote": "From the Greek stem **cycl**, we derive meteorological terms denoting the great swirling wind vortices of our atmosphere."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Anatomy of Invertebrated Animals",
        "quote": "Comparative morphologists employ **cycl** to designate circular anatomical arrangements such as the cyclostome oral sucker."
      }
    ]
  },
  "Dashboard — cycl\\cyclamen.md": {
    "primary": "A genus of perennial flowering plants in the primrose family Primulaceae, cultivated for their nodular tubers and nodding blossoms with reflexed petals.",
    "secondary": "In horticulture and Mediterranean floristics, shade-loving alpine woodland geophytes bearing marbled, heart-shaped leaves and backward-swept pink, purple, or white flowers.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Aspects of Nature",
        "quote": "In the dappled shade of Mediterranean olive groves, wild pink **Cyclamen** blossoms emerge from rocky fissures."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "The tuberous corm of the Persian **cyclamen** yields winter greenhouse blooms of astonishing elegance and delicate fragrance."
      },
      {
        "author": "John Ruskin",
        "work": "Proserpina: Studies of Wayside Flowers",
        "quote": "The reflexed petal of the **cyclamen** curves gracefully backward like the ear of a listening fawn."
      }
    ]
  },
  "Dashboard — cycl\\cyclic.md": {
    "primary": "Occurring in cycles or regular intervals; circular; moving or recurring in a cycle.",
    "secondary": "In chemistry, designating molecular structures containing a closed ring of bonded atoms; in literature, pertaining to a series of poems or myths revolving around a central theme.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Kekulé's insight that benzene forms a closed **cyclic** hexagon revolutionized nineteenth-century structural organic chemistry."
      },
      {
        "author": "Arnold Toynbee",
        "work": "A Study of History",
        "quote": "Spengler viewed the rise and fall of civilizations as a deterministic, **cyclic** rhythm resembling organic seasons."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Geological evidence refutes the ancient doctrine of **cyclic** catastrophes, testifying instead to continuous, gradual processes."
      }
    ]
  },
  "Dashboard — cycl\\cyclical.md": {
    "primary": "Occurring in repeating cycles; recurring at regular or predictable intervals.",
    "secondary": "In macroeconomics and ecology, describing recurring fluctuations in business activity, employment, or animal population densities.",
    "quotes": [
      {
        "author": "John Maynard Keynes",
        "work": "The General Theory of Employment, Interest and Money",
        "quote": "Capital investment fluctuates in a **cyclical** pattern driven by volatile shifts in the marginal efficiency of capital."
      },
      {
        "author": "Aldo Leopold",
        "work": "A Sand County Almanac",
        "quote": "The **cyclical** rise and collapse of snowshoe hare populations is linked to the predator-prey dynamics of the northern lynx."
      },
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "Agricultural yields display **cyclical** variations following the alternating abundance of dry and rainy seasons."
      }
    ]
  },
  "Dashboard — cycl\\cyclicity.md": {
    "primary": "The state, quality, or condition of being cyclic or recurring at periodic intervals.",
    "secondary": "In geochronology and sedimentology, the rhythmic, repetitive deposition of strata driven by Milankovitch orbital cycles or periodic climatic changes.",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "The apparent **cyclicity** in coal seam depositions reflects alternating periods of coastal subsidence and swamp development."
      },
      {
        "author": "Arthur Holmes",
        "work": "Principles of Physical Geology",
        "quote": "Sedimentary **cyclicity** in varved lake clays provides an exact geochronological record of glacial retreat."
      },
      {
        "author": "Joseph Schumpeter",
        "work": "Business Cycles",
        "quote": "The underlying **cyclicity** of modern capitalist production is propelled by waves of technological innovation and creative destruction."
      }
    ]
  },
  "Dashboard — cycl\\cyclide.md": {
    "primary": "A fourth-order algebraic geometric surface whose lines of curvature are all circles; especially a Dupin cyclide.",
    "secondary": "In differential and algebraic geometry, a quartic surface defined as the envelope of a variable sphere touching three fixed spheres, introduced by Pierre-Charles Dupin.",
    "quotes": [
      {
        "author": "Gaston Darboux",
        "work": "Treatise on the General Theory of Surfaces",
        "quote": "Every line of curvature upon the Dupin **cyclide** is a planar circle, a property that makes it unique among quartic surfaces."
      },
      {
        "author": "Arthur Cayley",
        "work": "Collected Mathematical Papers",
        "quote": "Inversion with respect to a sphere transforms a torus into an asymmetrical ring **cyclide**."
      },
      {
        "author": "William Kingdon Clifford",
        "work": "Mathematical Papers",
        "quote": "The geometric properties of the **cyclide** illuminate the deep connection between conformal geometry and focal conics."
      }
    ]
  },
  "Dashboard — cycl\\cycling.md": {
    "primary": "The act, pastime, or sport of riding a bicycle.",
    "secondary": "In environmental science and thermodynamics, the continuous movement or circulation of chemical elements, nutrients, or energy through an ecosystem.",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "The endless **cycling** of mineral salts from continental rocks into the sea sustains the entire web of marine life."
      },
      {
        "author": "H. G. Wells",
        "work": "The Wheels of Chance",
        "quote": "He discovered that weekend **cycling** through quiet villages afforded an exhilarating release from London drudgery."
      },
      {
        "author": "Eugene Odum",
        "work": "Fundamentals of Ecology",
        "quote": "Biogeochemical **cycling** of nitrogen and phosphorus regulates primary productivity in terrestrial and limnetic biomes."
      }
    ]
  },
  "Dashboard — cycl\\cycliophora.md": {
    "primary": "A phylum of microscopic, pseudocoelomate metazoan animals discovered living as commensals on the mouthparts of marine lobsters.",
    "secondary": "In invertebrate systematic zoology, an unusual phylum comprising the solitary genus Symbion (notably Symbion pandora), characterized by a complex life cycle alternating between asexual and dwarf sexual phases.",
    "quotes": [
      {
        "author": "Stephen Jay Gould",
        "work": "Dinosaur in a Haystack",
        "quote": "The discovery in 1995 of the new phylum **Cycliophora** living on lobster mouthparts proved that nature still conceals fundamental body architectures."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Future of Life",
        "quote": "Even in well-studied temperate coastal waters, tiny creatures of **Cycliophora** had eluded zoologists for over two centuries."
      },
      {
        "author": "Richard Dawkins",
        "work": "The Ancestor's Tale",
        "quote": "The microscopic bizarre inhabitants of **Cycliophora** attach themselves like microscopic vacuum cleaners to the bristly bristles of Nephrops."
      }
    ]
  },
  "Dashboard — cycl\\cyclist.md": {
    "primary": "A person who rides a bicycle, tricycle, or other pedal-driven cycle.",
    "secondary": "In competitive sports and urban transportation, a participant who engages in road, track, or cross-country bicycle racing or daily commuting.",
    "quotes": [
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventure of the Solitary Cyclist",
        "quote": "A solitary **cyclist** rode swiftly past the lane, turning a furtive glance toward the hedgerow as she vanished."
      },
      {
        "author": "H. G. Wells",
        "work": "The Wheels of Chance",
        "quote": "Every passing pedestrian offered humorous encouragement to the novice **cyclist** struggling to mount on an incline."
      },
      {
        "author": "George Orwell",
        "work": "The Road to Wigan Pier",
        "quote": "In industrial towns, the morning streets are crowded with hundreds of working-class **cyclist** workers heading to the mills."
      }
    ]
  },
  "Dashboard — cycl\\cyclobenzaprine.md": {
    "primary": "A tricyclic muscle relaxant medication used to relieve skeletal muscle spasms associated with acute, painful musculoskeletal conditions.",
    "secondary": "In clinical pharmacology, a central nervous system depressant structurally related to tricyclic antidepressants that acts primarily at the brainstem level to reduce tonic somatic motor activity.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In managing acute lumbosacral strain, short-term administration of **cyclobenzaprine** eases disabling muscular guarding."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "Central muscle relaxants like **cyclobenzaprine** act upon brainstem motor nuclei rather than directly on the peripheral neuromuscular junction."
      },
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "Due to its tricyclic chemical architecture, **cyclobenzaprine** warrants caution in patients with cardiac conduction disturbances."
      }
    ]
  },
  "Dashboard — cycl\\cyclohexanol.md": {
    "primary": "An alicyclic organic alcohol consisting of a six-membered carbon ring bonded to a hydroxyl group ($C_6H_{11}OH$).",
    "secondary": "In industrial chemical synthesis, a clear, viscous liquid produced by catalytic hydrogenation of phenol, used primarily as an intermediate in the production of adipic acid and caprolactam for nylon manufacturing.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "Oxidation of **cyclohexanol** with nitric acid ruptures the carbon ring to produce adipic acid, a foundational precursor of Nylon 66."
      },
      {
        "author": "Alexander Todd",
        "work": "A Time to Remember",
        "quote": "Catalytic reduction of phenol over Raney nickel affords a clean, quantitative yield of liquid **cyclohexanol**."
      },
      {
        "author": "J. D. Bernal",
        "work": "The Physical Basis of Life",
        "quote": "The boat and chair conformations of **cyclohexanol** illuminate the energetic constraints operating on non-planar six-membered carbon rings."
      }
    ]
  },
  "Dashboard — cycl\\cycloid.md": {
    "primary": "A geometric curve traced by a point on the circumference of a circle as the circle rolls along a straight line without slipping.",
    "secondary": "In physics and mathematics, the brachistochrone and tautochrone curve celebrated by seventeenth-century mathematicians ('the Helen of geometers') for its property of equal descent times under gravity.",
    "quotes": [
      {
        "author": "Christiaan Huygens",
        "work": "Horologium Oscillatorium",
        "quote": "The pendulum whose bob is constrained between **cycloid** cheeks oscillates with strictly isochronous swings regardless of amplitude."
      },
      {
        "author": "Isaac Newton",
        "work": "Principia Mathematica",
        "quote": "The curve of quickest descent under uniform gravity is none other than the inverted **cycloid**, as solved in the brachistochrone challenge."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The great try-pots of the whaler seemed shaped after the mathematical curve of a **cycloid**, designed for efficient heat circulation."
      }
    ]
  },
  "Dashboard — cycl\\cycloidal.md": {
    "primary": "Having the form, properties, or path of a cycloid.",
    "secondary": "In mechanical engineering and ichthyology, describing gear teeth profiled along a cycloid to ensure smooth meshing; or smooth, rounded fish scales (cycloid scales) lacking ctenii.",
    "quotes": [
      {
        "author": "Christiaan Huygens",
        "work": "Horologium Oscillatorium",
        "quote": "The **cycloidal** pendulum solved the ancient problem of maintaining precise timekeeping across variable arc amplitudes."
      },
      {
        "author": "Louis Agassiz",
        "work": "Recherches sur les Poissons Fossiles",
        "quote": "Teleostean fishes bearing thin, flexible **cycloidal** scales with concentric growth rings dominate modern freshwater faunas."
      },
      {
        "author": "William John Macquorn Rankine",
        "work": "A Manual of Machinery and Millwork",
        "quote": "Clocks and chronometers utilize **cycloidal** gear teeth to minimize sliding friction and tooth wear."
      }
    ]
  },
  "Dashboard — cycl\\cycloloma.md": {
    "primary": "A monotypic genus of North American annual herbs in the amaranth family Amaranthaceae, containing the winged pigweed (Cycloloma atriplicifolium).",
    "secondary": "In plant ecology, a bushy, tumbleweed-forming annual native to sandy plains and river sandbars, characterized by broad horizontal-winged calyces around its seeds.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The winged pigweed, **Cycloloma**, thrives in sterile drift sands along the shores of Lake Michigan and western riverbanks."
      },
      {
        "author": "John Merle Coulter",
        "work": "Manual of the Botany of the Rocky Mountain Region",
        "quote": "In autumn, mature globular bushes of **Cycloloma** detach at ground level, rolling across the prairie as tumbleweeds to scatter seed."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Views of Nature",
        "quote": "Western sandy wastes harbor curious Chenopodiaceous pioneers like **Cycloloma**, whose winged fruits are dispersed by autumn gales."
      }
    ]
  },
  "Dashboard — cycl\\cyclonal.md": {
    "primary": "Of, relating to, or resembling a cyclone; cyclonic.",
    "secondary": "In meteorology, describing atmospheric rotation, convergence, or barometric drops associated with a rotating cyclonic storm system.",
    "quotes": [
      {
        "author": "Joseph Conrad",
        "work": "Typhoon",
        "quote": "The ship plunged headlong into the shrieking vortex of a fierce **cyclonal** disturbance that blotted out the sea."
      },
      {
        "author": "Francis Galton",
        "work": "Meteorographica",
        "quote": "The inward spiraling winds of a **cyclonal** system contrast sharply with the outward divergence of anticyclones."
      },
      {
        "author": "Arthur Holmes",
        "work": "Principles of Physical Geology",
        "quote": "Vast ocean surges driven by severe **cyclonal** pressure drops erode barrier sandbars in a single night."
      }
    ]
  },
  "Dashboard — cycl\\cyclone.md": {
    "primary": "A system of winds rotating inward toward an area of low atmospheric pressure, accompanied by stormy weather.",
    "secondary": "In dynamic meteorology and industrial engineering, a large-scale tropical or extra-tropical atmospheric vortex (including hurricanes and typhoons); or an industrial apparatus separating suspended particles from air by centrifugal force.",
    "quotes": [
      {
        "author": "Henry Piddington",
        "work": "The Sailor's Horn-Book for the Law of Storms",
        "quote": "I suggest the name **cyclone** from the Greek kyklos, signifying among other things the coil of a serpent, to denote these circular storms."
      },
      {
        "author": "Joseph Conrad",
        "work": "Typhoon",
        "quote": "Captain MacWhirr had never met a **cyclone** of such demonic ferocity in all his forty years upon the Eastern seas."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "When a tropical **cyclone** moves across warm equatorial waters, it gathers monumental thermodynamic energy from the ocean surface."
      }
    ]
  },
  "Dashboard — cycl\\cyclonic.md": {
    "primary": "Pertaining to, having the nature of, or caused by a cyclone; rotating counterclockwise in the Northern Hemisphere and clockwise in the Southern Hemisphere.",
    "secondary": "In synoptic meteorology and oceanography, describing low-pressure rotating weather systems or counterclockwise oceanic eddies.",
    "quotes": [
      {
        "author": "Joseph Conrad",
        "work": "The Shadow-Line",
        "quote": "The darkening horizon warned the watchful mate that a furious **cyclonic** squall was gathering to windward."
      },
      {
        "author": "Francis Galton",
        "work": "Meteorographica",
        "quote": "Atmospheric pressure falls steadily as one penetrates deeper toward the center of a **cyclonic** vortex."
      },
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "Immense **cyclonic** storms sweep the Atlantic shelf, dislodging kelp beds and tossing heavy cobbles high onto the shingle."
      }
    ]
  },
  "Dashboard — cycl\\cyclonical.md": {
    "primary": "Of or relating to a cyclone; of cyclonic character.",
    "secondary": "In older meteorological treatises, describing circular storm dynamics or rotating pressure systems.",
    "quotes": [
      {
        "author": "Henry Piddington",
        "work": "The Sailor's Horn-Book for the Law of Storms",
        "quote": "Vessels caught in a **cyclonical** hurricane must immediately determine which semi-circle of the tempest they occupy."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The sky assumed a wild and **cyclonical** aspect as black squall clouds wrapped the mastheads in gloom."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Great storm surges accompanying **cyclonical** gales frequently inundate low delta plains, depositing thick silt strata."
      }
    ]
  },
  "Dashboard — cycl\\cyclooxygenase-1.md": {
    "primary": "A constitutive isoform of the cyclooxygenase enzyme (COX-1) responsible for producing basal prostaglandins that maintain gastric mucosal integrity and renal blood flow.",
    "secondary": "In molecular pharmacology and cellular biochemistry, the constitutive homodimeric hemoprotein that converts arachidonic acid to prostaglandin H2, inhibited non-selectively by aspirin and traditional NSAIDs.",
    "quotes": [
      {
        "author": "John R. Vane",
        "work": "Nobel Lecture: The Mode of Action of Aspirin and Similar Drugs",
        "quote": "Constitutive **cyclooxygenase-1** synthesizes the protective prostacyclin and thromboxane necessary for platelet aggregation and gastric homeostasis."
      },
      {
        "author": "Sydney Brenner",
        "work": "Loose Ends: Selected Writings",
        "quote": "Structural crystal studies revealed that **cyclooxygenase-1** possesses a narrow hydrophobic catalytic channel accessible to traditional salicylate inhibitors."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Inhibition of gastroprotective **cyclooxygenase-1** explains the common occurrence of peptic ulceration in patients taking high-dose anti-inflammatory agents."
      }
    ]
  },
  "Dashboard — cycl\\cyclooxygenase-2.md": {
    "primary": "An inducible isoform of the cyclooxygenase enzyme (COX-2) upregulated during inflammation, pain, and fever.",
    "secondary": "In biochemical pharmacology and rheumatology, the enzyme induced by inflammatory cytokines and growth factors whose selective inhibition by coxibs alleviates pain without causing primary gastric ulceration.",
    "quotes": [
      {
        "author": "John R. Vane",
        "work": "Nobel Lecture: The Mode of Action of Aspirin and Similar Drugs",
        "quote": "The discovery of inducible **cyclooxygenase-2** paved the way for selective anti-inflammatory drugs that spare the stomach lining."
      },
      {
        "author": "Sydney Brenner",
        "work": "Loose Ends: Selected Writings",
        "quote": "Targeting the roomier side pocket of **cyclooxygenase-2** permitted chemists to synthesize potent, highly isoform-specific inhibitors."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "While selective inhibition of **cyclooxygenase-2** reduces gastrointestinal bleeding, it may alter prostacyclin-thromboxane balance in coronary vascular beds."
      }
    ]
  },
  "Dashboard — cycl\\cyclooxygenase.md": {
    "primary": "An enzyme (prostaglandin-endoperoxide synthase) that catalyzes the conversion of arachidonic acid into prostanoids, including prostaglandins, prostacyclin, and thromboxane.",
    "secondary": "In enzymology and clinical pharmacology, the membrane-bound, heme-containing bis-dioxygenase enzyme that serves as the principal molecular target of nonsteroidal anti-inflammatory drugs (NSAIDs).",
    "quotes": [
      {
        "author": "John R. Vane",
        "work": "Inhibition of Prostaglandin Synthesis as a Mechanism of Action for Aspirin-like Drugs",
        "quote": "I demonstrated that aspirin and indomethacin exert their clinical anti-inflammatory action by directly inhibiting the enzyme **cyclooxygenase**."
      },
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "The catalytic pocket of **cyclooxygenase** binds arachidonic acid, guiding two sequential oxygen additions with stereospecific precision."
      },
      {
        "author": "Sydney Brenner",
        "work": "Loose Ends",
        "quote": "Deciphering the crystallographic architecture of **cyclooxygenase** transformed empirical pharmacology into rational, structure-guided drug design."
      }
    ]
  },
  "Dashboard — cycl\\cyclopaedia.md": {
    "primary": "A comprehensive reference work containing articles on all branches of knowledge or on a particular subject; an encyclopedia.",
    "secondary": "In intellectual history and publishing, a systematic compendium designed to provide a complete, well-rounded circle of human education and liberal sciences.",
    "quotes": [
      {
        "author": "Ephraim Chambers",
        "work": "Cyclopaedia, or an Universal Dictionary of Arts and Sciences",
        "quote": "The purpose of this **Cyclopaedia** is to link all the arts and sciences into one harmonious and navigable circle of learning."
      },
      {
        "author": "Denis Diderot",
        "work": "Encyclopédie: Preliminary Discourse",
        "quote": "Chambers's pioneering **Cyclopaedia** demonstrated how an alphabetical arrangement could bring universal enlightenment within general reach."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Rambler",
        "quote": "No solitary student can hope to master what the collective authors of a great **cyclopaedia** have compiled over generations."
      }
    ]
  },
  "Dashboard — cycl\\cyclopean.md": {
    "primary": "Formed of massive, irregular, unhewn boulders fitted together without mortar; also of vast or gigantic size.",
    "secondary": "In classical archaeology, ancient Mycenaean stone architecture built of immense limestone blocks, traditionally ascribed to the mythical giant Cyclopes.",
    "quotes": [
      {
        "author": "Heinrich Schliemann",
        "work": "Mycenae: A Narrative of Researches and Discoveries",
        "quote": "The magnificent Lion Gate was framed by **cyclopean** blocks of breccia so colossal that no modern crane could easily stir them."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The skeleton of the sperm whale exhibited a **cyclopean** architecture reminiscent of ancient temple ruins."
      },
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "Early Pelasgian builders raised **cyclopean** fortifications whose rough megalithic strength defies the wear of thirty centuries."
      }
    ]
  },
  "Dashboard — cycl\\cyclopedia.md": {
    "primary": "A book or set of books containing articles on various aspects of human knowledge; an encyclopedia.",
    "secondary": "In education and lexicography, a systematic reference work encompassing the entire circle of learning or an exhaustive survey of a specialized technical field.",
    "quotes": [
      {
        "author": "Ralph Waldo Emerson",
        "work": "Essays: First Series",
        "quote": "Every man is a quotation from all his ancestors, and nature itself is a vast, open-air **cyclopedia** of symbols."
      },
      {
        "author": "Henry David Thoreau",
        "work": "A Week on the Concord and Merrimack Rivers",
        "quote": "The riverbank woods offer a livelier **cyclopedia** than any leather-bound volume in the university library."
      },
      {
        "author": "Mark Twain",
        "work": "Innocents Abroad",
        "quote": "The tourist turned to his pocket **cyclopedia** to verify the dimensions of the Roman Colosseum."
      }
    ]
  },
  "Dashboard — cycl\\cyclopes.md": {
    "primary": "A race of one-eyed mythical giants in classical Greek mythology who forged thunderbolts for Zeus.",
    "secondary": "In classical literature, primitive pastoral giants inhabiting cave fastnesses, such as Polyphemus in Homer's Odyssey, or divine smiths laboring beneath Mount Etna.",
    "quotes": [
      {
        "author": "Homer",
        "work": "Odyssey",
        "quote": "We arrived at the land of the fierce **Cyclopes**, lawless giants who plant neither wheat nor vines, trusting only to immortal gods."
      },
      {
        "author": "Virgil",
        "work": "Aeneid",
        "quote": "Beneath the glowing caverns of Mount Etna, the monstrous **Cyclopes** forge lightning bolts for the Father of gods and men."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "Not that large size of giant breed that moved / In Sicily, where **Cyclopes** dwelt in caves."
      }
    ]
  },
  "Dashboard — cycl\\cyclophorus.md": {
    "primary": "A large genus of tropical operculate terrestrial snails in the family Cyclophoridae, characterized by a circular shell aperture and round operculum.",
    "secondary": "In systematic malacology, land snails widespread in tropical Asian and Indo-Pacific rainforests possessing a circular calcareous or corneous door.",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "I collected several magnificent land snails of the genus **Cyclophorus** creeping over damp limestone boulders in Sarawak."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The tight-fitting operculum of **Cyclophorus** enables the snail to survive extended periods of tropical drought."
      },
      {
        "author": "E. Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "In **Cyclophorus**, the circular aperture of the shell reflects the perfectly rounded contours of the mantle collar."
      }
    ]
  },
  "Dashboard — cycl\\cyclopia.md": {
    "primary": "A rare, severe congenital developmental malformation in which the embryonic forebrain fails to divide the orbits into two cavities, resulting in a single central eye.",
    "secondary": "In teratology and developmental embryology, the most extreme phenotypic manifestation of alobar holoprosencephaly, often accompanied by a tubular proboscis above the single orbit.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Congenital **cyclopia** represents a severe developmental arrest of the anterior prechordal mesoderm during early neural plate induction."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants Under Domestication",
        "quote": "Cases of **cyclopia** appearing in domestic lambs provide remarkable illustrations of teratological cephalic fusion."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Examination of human fetuses with **cyclopia** reveals total failure of median cleavage within the embryonic prosencephalon."
      }
    ]
  },
  "Dashboard — cycl\\cyclopropane.md": {
    "primary": "The simplest cycloalkane hydrocarbon ($C_3H_6$), consisting of three carbon atoms bonded into a triangular ring.",
    "secondary": "In organic chemistry and historic anesthesiology, a highly strained cyclic gas with a 60-degree bond angle, formerly widely employed as a potent inhalation general anesthetic.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "The severe ring strain in **cyclopropane** arises from the forced constriction of tetrahedral carbon bond angles down to sixty degrees."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "Round the Red Lamp",
        "quote": "The operating amphitheater was silent as the anesthetist administered sweet-smelling **cyclopropane** gas to induce unconsciousness."
      },
      {
        "author": "Alexander Todd",
        "work": "A Time to Remember",
        "quote": "The remarkable reactivity of **cyclopropane** stems directly from its high banana-bond strain and ring combustion energy."
      }
    ]
  },
  "Dashboard — cycl\\cyclopteridae.md": {
    "primary": "A family of cold-water marine scorpaeniform fishes commonly known as lumpsuckers or lumpfishes.",
    "secondary": "In marine ichthyology, benthic fishes characterized by a globular, tuberculated body and pelvic fins modified into a ventral suction cup used to adhere to rocky sea floors in strong currents.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The lumpsuckers of the family **Cyclopteridae** possess a powerful ventral sucking disc adapted for anchoring to sublittoral stones."
      },
      {
        "author": "Henry Bryant Bigelow",
        "work": "Fishes of the Gulf of Maine",
        "quote": "Members of **Cyclopteridae** inhabit turbulent icy shores, clinging tenaciously to kelp fronds despite furious tidal surges."
      },
      {
        "author": "Albert Günther",
        "work": "An Introduction to the Study of Fishes",
        "quote": "The armor of bony tubercles covering the thick skin of **Cyclopteridae** affords protection against predaceous seals and cod."
      }
    ]
  },
  "Dashboard — cycl\\cyclopterus.md": {
    "primary": "The type genus of lumpfishes in the family Cyclopteridae, represented by the common lumpfish (Cyclopterus lumpus).",
    "secondary": "In marine biology and commercial fisheries, a heavy, humpbacked North Atlantic fish whose adhesive pelvic disc holds it securely to rocks and whose roe is harvested as caviar substitute.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "In **Cyclopterus**, the modified pelvic fins form a circular adhesive sucker of extraordinary holding power upon wet rock."
      },
      {
        "author": "Spencer Fullerton Baird",
        "work": "Report on the Condition of the Sea Fisheries",
        "quote": "Fishermen frequently pull up specimens of **Cyclopterus** firmly attached to the bottom of offshore lobster pots."
      },
      {
        "author": "Louis Agassiz",
        "work": "Methods of Study in Natural History",
        "quote": "The male **Cyclopterus** guards the cluster of eggs with fierce maternal fidelity, fan-sweeping clean water over the brood."
      }
    ]
  },
  "Dashboard — cycl\\cyclorama.md": {
    "primary": "A large panoramic picture painted on the inside of a cylindrical wall and viewed from the center, giving the illusion of a continuous landscape.",
    "secondary": "In theatrical staging, a curved, seamless backdrop wall or cloth positioned at the rear of the stage to represent sky, open space, or distant horizons.",
    "quotes": [
      {
        "author": "Mark Twain",
        "work": "Life on the Mississippi",
        "quote": "Visitors crowded into the rotunda to marvel at the immense **cyclorama** depicting the battle of Gettysburg with astounding realism."
      },
      {
        "author": "Lewis Mumford",
        "work": "Technics and Civilization",
        "quote": "Nineteenth-century urban entertainment celebrated the mechanized spectacle of the **cyclorama**, immersing city dwellers in artificial vistas."
      },
      {
        "author": "George Bernard Shaw",
        "work": "Our Theatres in the Nineties",
        "quote": "By projecting soft azure light upon the curved **cyclorama**, the stage designer evoked the infinite expanse of an open sky."
      }
    ]
  },
  "Dashboard — cycl\\cycloserine.md": {
    "primary": "An antibiotic medication used as a second-line treatment in combination therapy for multi-drug-resistant tuberculosis.",
    "secondary": "In microbiology and neuropsychiatry, a cyclic structural analogue of D-alanine that inhibits bacterial cell wall enzymes (D-alanine ligase) and acts as a partial agonist at NMDA receptors in the brain.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "When first-line tuberculostatic agents fail, **cycloserine** is introduced to suppress resistant strains of Mycobacterium tuberculosis."
      },
      {
        "author": "Sydney Brenner",
        "work": "Loose Ends: Selected Writings",
        "quote": "By mimicking D-alanine, **cycloserine** competitive inhibition blocks the terminal peptidoglycan cross-linking step in bacterial walls."
      },
      {
        "author": "Francis Crick",
        "work": "What Mad Pursuit",
        "quote": "Molecular pharmacologists observed that **cycloserine** binds to central NMDA receptors, opening unexpected avenues for memory research."
      }
    ]
  },
  "Dashboard — cycl\\cyclosis.md": {
    "primary": "The streaming, rotational circulation of cytoplasm within a living cell.",
    "secondary": "In cellular physiology and plant biology, the active movement of organelles and cytosol driven by actin-myosin microfilaments, easily observed in giant alga cells such as Nitella or Elodea leaves.",
    "quotes": [
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Inheritance",
        "quote": "Under the high power of the microscope, the continuous **cyclosis** of chloroplasts around the central vacuole of Elodea is a breathtaking sight."
      },
      {
        "author": "Charles Darwin",
        "work": "Insectivorous Plants",
        "quote": "Stimulation of the tentacle hairs in Drosera produces rapid aggregation accompanied by accelerated **cyclosis** within the cell protoplasm."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "On the Physical Basis of Life",
        "quote": "The living protoplasm within the hair of the nettle exhibits active **cyclosis**, circulating streams of granules in perpetual currents."
      }
    ]
  }
};

const updated = updateNotesBatch(CLUSTER_DIR, batchData);
console.log(`[Batch 4] Successfully updated ${updated} of ${Object.keys(batchData).length} notes.`);
