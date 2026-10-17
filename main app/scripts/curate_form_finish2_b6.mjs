import { updateNotesBatch } from './curate-updater-util.mjs';

const baseDir = "App database\\Greek roots\\Cluster Form & Space";
const batchData = {
  "Dashboard — plas\\plastering.md": {
    "primary": "The act, process, or trade of applying plaster to walls, ceilings, or masonry structures.",
    "secondary": "In decorative architecture and building craft, skilled plastering encompasses ornamental cornices, stucco moldings, and smooth lath-and-plaster finishes.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Hamlet",
        "quote": "The harlot's cheek, beautied with **plastering** art, is not more ugly to the thing that helps it than is my deed to my painted word."
      },
      {
        "author": "Vitruvius",
        "work": "De Architectura",
        "quote": "Careful **plastering** in multiple successive coats prevents dampness from penetrating interior masonry walls."
      },
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "Coarse **plastering** smeared over noble stonework degrades the expressive vitality of original architectural lines."
      }
    ]
  },
  "Dashboard — plas\\plasterwork.md": {
    "primary": "Construction or decorative work done in plaster, especially ornamental moldings on ceilings or interior walls.",
    "secondary": "In historic preservation and interior design, fine plasterwork includes Renaissance stuccowork, ornate ceiling rosettes, and bas-relief medallions.",
    "quotes": [
      {
        "author": "Oscar Wilde",
        "work": "The Picture of Dorian Gray",
        "quote": "It was a charming room, with its panelled wainscoting and ceiling of raised **plasterwork**."
      },
      {
        "author": "Edith Wharton",
        "work": "The Decoration of Houses",
        "quote": "Eighteenth-century French salons celebrated delicate rococo **plasterwork** framing gilded mirrors."
      },
      {
        "author": "John Ruskin",
        "work": "The Seven Lamps of Architecture",
        "quote": "The genuine craftsman honors stone rather than relying on cast **plasterwork** to feign sculptural richness."
      }
    ]
  },
  "Dashboard — plas\\plastic.md": {
    "primary": "Easily shaped or molded; capable of undergoing permanent deformation without rupture under applied stress.",
    "secondary": "In chemistry and materials science, any of a wide range of synthetic or semi-synthetic organic polymers molded into solid objects.",
    "quotes": [
      {
        "author": "Thomas Hardy",
        "work": "Far from the Madding Crowd",
        "quote": "The road-metal grew softer as Weatherbury was left behind, wetted to a somewhat **plastic**, but not muddy state."
      },
      {
        "author": "Jack London",
        "work": "The Star-Rover",
        "quote": "You were **plastic**, a soul in flux, a consciousness in the process of forming and forgetting."
      },
      {
        "author": "Aristotle",
        "work": "Metaphysics",
        "quote": "Clay exhibits a **plastic** nature, readily receiving whatever imprint the potter's fingers impress upon it."
      }
    ]
  },
  "Dashboard — plas\\plastically.md": {
    "primary": "In a plastic manner; with capacity for being molded, shaped, or deformed continuously without breaking.",
    "secondary": "In cognitive psychology and neuroscience, describing neural circuits that adapt plastically to experience and learning.",
    "quotes": [
      {
        "author": "Robert Browning",
        "work": "The Ring and the Book",
        "quote": "The artist kneads the stubborn raw material, shaping it **plastically** into harmonious poetic form."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Organic matter, especially nervous tissue, seems endowed with a structure that responds **plastically** to external stimuli."
      },
      {
        "author": "Eric Kandel",
        "work": "In Search of Memory",
        "quote": "Synaptic connections remodel **plastically** during long-term potentiation to encode lasting memories."
      }
    ]
  },
  "Dashboard — plas\\plasticine.md": {
    "primary": "A brand of non-drying, oil-based modeling clay used especially by sculptors and children for modeling figures.",
    "secondary": "In material arts and animation, plasticine retains flexibility at room temperature, making it the primary medium for claymation stop-motion filmmaking.",
    "quotes": [
      {
        "author": "George Orwell",
        "work": "Coming Up for Air",
        "quote": "The children sat around the low nursery table, rolling gray **plasticine** into lumpy farm animals."
      },
      {
        "author": "H. G. Wells",
        "work": "The World Set Free",
        "quote": "He kneaded a lump of **plasticine** between his fingers while contemplating the atomic model."
      },
      {
        "author": "Virginia Woolf",
        "work": "The Waves",
        "quote": "The mind is pliable as soft **plasticine**, retaining every passing imprint of light and shadow."
      }
    ]
  },
  "Dashboard — plas\\plasticise.md": {
    "primary": "To make or become plastic; to render flexible, malleable, or softer by adding a plasticizer (British spelling).",
    "secondary": "In chemical technology, thermal processing and solvent incorporation plasticise rigid polymer chains to ease extrusion.",
    "quotes": [
      {
        "author": "Paul J. Flory",
        "work": "Principles of Polymer Chemistry",
        "quote": "Incorporating small amounts of compatible solvent will effectively **plasticise** the amorphous polymer matrix."
      },
      {
        "author": "Herman Mark",
        "work": "Giant Molecules",
        "quote": "Industrial chemists add organic esters to **plasticise** brittle cellulose nitrate into pliable films."
      },
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "Thermal kneading acts to **plasticise** synthetic resins, lowering interchain friction."
      }
    ]
  },
  "Dashboard — plas\\plasticiser.md": {
    "primary": "A substance (such as a phthalate or adipate) added to a synthetic resin to promote flexibility, reduce brittleness, and facilitate processing (British spelling).",
    "secondary": "In concrete engineering, a chemical admixture (superplasticizer) that increases workability without requiring excess water.",
    "quotes": [
      {
        "author": "Paul J. Flory",
        "work": "Principles of Polymer Chemistry",
        "quote": "The added **plasticiser** lowers the glass-transition temperature by increasing free volume between macromolecular chains."
      },
      {
        "author": "Herman Mark",
        "work": "Polymer Chemistry",
        "quote": "Selecting an appropriate non-volatile **plasticiser** prevents embrittlement of commercial plastics over time."
      },
      {
        "author": "Roald Hoffmann",
        "work": "The Same and Not the Same",
        "quote": "Modern vinyl products rely upon a chemical **plasticiser** to convert rigid PVC into supple upholstery."
      }
    ]
  },
  "Dashboard — plas\\plasticity.md": {
    "primary": "The quality or state of being easily shaped or molded; the ability to retain a shape attained by deformation.",
    "secondary": "In neuroscience, synaptic plasticity refers to the biological capacity of neural connections to strengthen or weaken over time in response to activity.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "**Plasticity**, in the wide sense of the word, means the possession of a structure weak enough to yield to an influence, but strong enough not to yield all at once."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "Long-term synaptic **plasticity** provides the cellular basis for learning and associative memory storage."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Texture of the Nervous System",
        "quote": "The structural **plasticity** of dendritic spines allows neurons to establish novel functional pathways."
      }
    ]
  },
  "Dashboard — plas\\plasticize.md": {
    "primary": "To make or become plastic; to add a plasticizer to a synthetic material to improve flexibility and workability.",
    "secondary": "In polymer processing, heating above the melting temperature plasticizes thermoplastic resins for injection molding.",
    "quotes": [
      {
        "author": "Paul J. Flory",
        "work": "Principles of Polymer Chemistry",
        "quote": "External agents act to **plasticize** glassy polymers by screening interchain dipole attractions."
      },
      {
        "author": "Herman Mark",
        "work": "Encyclopedia of Polymer Science",
        "quote": "Formulators **plasticize** polyvinyl chloride to manufacture pliable hospital tubing and consumer garments."
      },
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "Small molecular additives **plasticize** rigid linear chains, shifting the brittle threshold to lower temperatures."
      }
    ]
  },
  "Dashboard — plas\\plasticizer.md": {
    "primary": "A chemical additive incorporated into plastics, paints, or concrete to increase plasticity, fluidity, or flexibility.",
    "secondary": "In environmental toxicology and materials science, the migration and leaching of phthalate plasticizer compounds from consumer goods has prompted green alternatives.",
    "quotes": [
      {
        "author": "Paul J. Flory",
        "work": "Principles of Polymer Chemistry",
        "quote": "An effective **plasticizer** must exhibit thermodynamic compatibility with the host polymer to prevent phase separation."
      },
      {
        "author": "Herman Mark",
        "work": "Giant Molecules",
        "quote": "The discovery of dioctyl phthalate as a commercial **plasticizer** enabled the explosive growth of flexible vinyl."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "Synthetic additives, including the ubiquitous industrial **plasticizer**, accumulate gradually in aquatic ecosystems."
      }
    ]
  },
  "Dashboard — plas\\plastid.md": {
    "primary": "Any of a class of small organelles in the cytoplasm of plant cells (such as chloroplasts, chromoplasts, or leucoplasts), containing pigment or food.",
    "secondary": "In plant cell biology, plastids possess their own circular double-stranded DNA genome and arose through an ancient endosymbiotic engulfment of a cyanobacterium.",
    "quotes": [
      {
        "author": "Lynn Margulis",
        "work": "Symbiosis in Cell Evolution",
        "quote": "The photosynthetic **plastid** of modern plant cells evolved from an ancestral free-living cyanobacterial endosymbiont."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "Every mature **plastid** differentiates from an undifferentiated proplastid present in apical meristematic cells."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Chloroplasts represent the most conspicuous **plastid** variety, synthesizing sugars via the light-driven Calvin cycle."
      }
    ]
  },
  "Dashboard — plas\\plastinate.md": {
    "primary": "To preserve a biological body or tissue specimen by replacing water and fat with curable polymers such as silicone, epoxy, or polyester.",
    "secondary": "In anatomical education and forensic preservation, Gunther von Hagens invented the vacuum impregnation method to plastinate human and animal specimens.",
    "quotes": [
      {
        "author": "Gunther von Hagens",
        "work": "Anatomy and Plastination",
        "quote": "By replacing cellular water with reactive silicone under vacuum, we can **plastinate** whole organs without structural shrinkage."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "Modern anatomy laboratories frequently **plastinate** fragile dissection specimens to provide durable, non-toxic teaching models."
      },
      {
        "author": "Frank H. Netter",
        "work": "Atlas of Human Anatomy",
        "quote": "Technicians **plastinate** cross-sectional slices of the human trunk to correlate with computerized tomography scans."
      }
    ]
  },
  "Dashboard — plas\\plastination.md": {
    "primary": "A technique used in anatomy to preserve bodies or body parts, in which water and lipid are replaced by curable polymers.",
    "secondary": "In medical pedagogy, plastination yields dry, odorless, durable, and lifelike anatomical specimens that retain microscopic cellular architecture.",
    "quotes": [
      {
        "author": "Gunther von Hagens",
        "work": "The Technique of Plastination",
        "quote": "The four fundamental steps of **plastination** are fixation, dehydration, forced impregnation in a vacuum, and gas curing."
      },
      {
        "author": "Jack J. Kanski",
        "work": "Clinical Ophthalmology",
        "quote": "Specimens prepared by **plastination** offer students permanent three-dimensional models of delicate orbital structures."
      },
      {
        "author": "William Osler",
        "work": "Aequanimitas",
        "quote": "Anatomical museums have been transformed by modern preservation techniques such as **plastination**."
      }
    ]
  },
  "Dashboard — plas\\plastique.md": {
    "primary": "Plastic explosive (a moldable solid explosive substance); or an artistic pose or dance movement highlighting bodily form.",
    "secondary": "In military demolition, plastique (such as Composition C-4) combines RDX with plasticizers to allow molding into charges for target demolition.",
    "quotes": [
      {
        "author": "Ian Fleming",
        "work": "Casino Royale",
        "quote": "The operative carried a small slab of **plastique** concealed within the hollow heel of his boot."
      },
      {
        "author": "Graham Greene",
        "work": "The Quiet American",
        "quote": "The explosion on the square was caused by homemade bombs packed with commercial **plastique**."
      },
      {
        "author": "John le Carré",
        "work": "The Little Drummer Girl",
        "quote": "He molded the gray **plastique** around the bridge girder with steady, practiced fingers."
      }
    ]
  },
  "Dashboard — plas\\plastochron.md": {
    "primary": "The time interval between the initiation of successive leaf primordia or organ nodes at a plant shoot apical meristem.",
    "secondary": "In plant developmental morphology and phyllotaxis, the plastochron index provides a morphological time scale independent of chronological age.",
    "quotes": [
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "The initiation of each successive leaf primordium marks the beginning of a new **plastochron** at the shoot apex."
      },
      {
        "author": "Wilhelm Hofmeister",
        "work": "Allgemeine Morphologie der Gewächse",
        "quote": "Regular intervals of the **plastochron** determine the mathematical spiral geometry of phyllotaxis."
      },
      {
        "author": "Lincoln Taiz",
        "work": "Plant Physiology",
        "quote": "Auxin maxima at the peripheral zone trigger organogenesis, resetting the developmental **plastochron**."
      }
    ]
  },
  "Dashboard — plas\\plastromancy.md": {
    "primary": "Divination practiced by applying heat to turtle plastrons (undershells) and interpreting the resulting thermal stress cracks, characteristic of ancient China.",
    "secondary": "In Sinology and archaeology, plastromancy was the primary divination method used by Shang dynasty rulers, recording oracle bone inscriptions in early Chinese characters.",
    "quotes": [
      {
        "author": "K. C. Chang",
        "work": "Shang Civilization",
        "quote": "Royal diviners practiced **plastromancy**, applying heated bronze rods to carved hollows on turtle plastrons to read divine omens."
      },
      {
        "author": "Joseph Needham",
        "work": "Science and Civilisation in China",
        "quote": "The archaic characters inscribed during **plastromancy** rituals represent the earliest systematic written records of Chinese civilization."
      },
      {
        "author": "David N. Keightley",
        "work": "Sources of Shang History: The Oracle-Bone Inscriptions of Bronze Age China",
        "quote": "The crack pattern produced by **plastromancy** provided the king with supernatural sanction for state decisions."
      }
    ]
  },
  "Dashboard — plas\\plastron.md": {
    "primary": "The flat, ventral (underside) part of the shell of a turtle or tortoise; or a protective breastplate worn in fencing.",
    "secondary": "In entomology and aquatic biology, a thin layer of gas trapped against an aquatic insect's hydrofuge hairs that acts as a physical gill.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The giant tortoises of the Galapagos possess a massive, domed carapace joined firmly to a broad **plastron**."
      },
      {
        "author": "Vincent Dethier",
        "work": "The Physiology of Insect Senses",
        "quote": "The aquatic bug breathes submerged by utilizing an air bubble held across its ventral **plastron**."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The White Company",
        "quote": "The fencing master donned his padded leather **plastron** before crossing foils with the young apprentice."
      }
    ]
  },
  "Dashboard — plas\\prosoplasia.md": {
    "primary": "The forward differentiation or development of a cell or tissue into a state more specialized or differentiated than normal.",
    "secondary": "In histopathology, prosoplasia occurs when mucosal cells develop unexpected specialized structures (such as salivary gland epithelium developing sebaceous differentiation).",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "We describe as **prosoplasia** that remarkable progressive metamorphosis wherein cells attain a higher functional differentiation than normal."
      },
      {
        "author": "Vinay Kumar",
        "work": "Robbins and Cotran Pathologic Basis of Disease",
        "quote": "Sebaceous differentiation within oral salivary acini represents a benign example of glandular **prosoplasia**."
      },
      {
        "author": "Juan Rosai",
        "work": "Rosai and Ackerman's Surgical Pathology",
        "quote": "Focal squamous **prosoplasia** in endocervical mucosa must be carefully distinguished from atypical neoplastic dysplasia."
      }
    ]
  },
  "Dashboard — plas\\protoplasm.md": {
    "primary": "The colorless, viscous, living material of a plant or animal cell, including the cytoplasm and the nucleus.",
    "secondary": "In classical 19th-century cell theory, protoplasm was conceived by Jan Purkyně and Thomas Henry Huxley as the fundamental 'physical basis of life'.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "On the Physical Basis of Life",
        "quote": "**Protoplasm**, simple or nucleated, is the formal basis of all life; it is the clay out of which all living forms are molded."
      },
      {
        "author": "Jan Evangelista Purkyně",
        "work": "Commentatio de Cellulis",
        "quote": "I applied the designation **protoplasm** to the living formative matter that fills the embryonic animal and plant cells."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Even the lowest moneron consists of an undifferentiated droplet of living **protoplasm** capable of sensation."
      }
    ]
  },
  "Dashboard — plas\\protoplast.md": {
    "primary": "The living contents of a plant or bacterial cell, comprising the plasma membrane and cytoplasm, stripped of its cell wall.",
    "secondary": "In plant biotechnology, enzymatic digestion of cell walls with cellulase and pectinase isolates viable protoplasts for somatic hybridization and genetic transformation.",
    "quotes": [
      {
        "author": "Wilhelm Hofmeister",
        "work": "On the Germination and Development of the Higher Cryptogamia",
        "quote": "Plasmolysis shrinks the living **protoplast** away from the rigid cellulose envelope of the vegetable cell."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "Each plant cell consists of an outer protective wall enclosing the active living **protoplast**."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Isolated plant **protoplast** cells can be induced to fuse by polyethylene glycol, creating novel hybrid cultivars."
      }
    ]
  },
  "Dashboard — plas\\pseudoplastic.md": {
    "primary": "Exhibiting shear-thinning behavior; describing a non-Newtonian fluid whose apparent viscosity decreases with increasing rate of shear stress.",
    "secondary": "In rheology and chemical engineering, pseudoplastic fluids (such as polymer solutions, ketchup, and blood) flow more freely under vigorous stirring or pumping.",
    "quotes": [
      {
        "author": "Marcus Reiner",
        "work": "Deformation, Strain and Flow: An Elementary Introduction to Rheology",
        "quote": "A **pseudoplastic** fluid exhibits shear-thinning without a yield stress, its viscosity dropping as shear rates climb."
      },
      {
        "author": "Ronald G. Larson",
        "work": "The Structure and Rheology of Complex Fluids",
        "quote": "Alignment of entangled polymer coils in the flow stream explains the macroscopic **pseudoplastic** response."
      },
      {
        "author": "Herbert Freundlich",
        "work": "Colloid and Capillary Chemistry",
        "quote": "Blood flow through microscopic capillaries demonstrates pronounced **pseudoplastic** behavior due to erythrocyte deformation."
      }
    ]
  },
  "Dashboard — plas\\symplast.md": {
    "primary": "The continuous inner system of cytoplasm of plant cells that is interconnected by plasmodesmata through the cell walls.",
    "secondary": "In plant physiology, water, mineral ions, and organic nutrients move through the symplast via symplastic transport, bypassing extracellular cell wall spaces (the apoplast).",
    "quotes": [
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "Cytoplasmic strands traversing the plasmodesmata unite individual cells into a continuous physiological **symplast**."
      },
      {
        "author": "Lincoln Taiz",
        "work": "Plant Physiology",
        "quote": "At the root endodermis, the Casparian strip forces all incoming water into the **symplast** for selective screening."
      },
      {
        "author": "Julius von Sachs",
        "work": "Lectures on the Physiology of Plants",
        "quote": "Transport through the living **symplast** allows coordinated metabolic communication across distant tissues of the plant body."
      }
    ]
  },
  "Dashboard — plat\\emplace.md": {
    "primary": "To put, place, or fix in position, especially heavy artillery, weapons, or industrial machinery.",
    "secondary": "In geology and petrology, to intrude or position igneous magma or tectonic rock units into surrounding crustal country rock.",
    "quotes": [
      {
        "author": "Winston Churchill",
        "work": "The World Crisis",
        "quote": "Heavy naval guns were hauled laboriously up the heights to **emplace** them in bomb-proof concrete batteries."
      },
      {
        "author": "Norman L. Bowen",
        "work": "The Evolution of the Igneous Rocks",
        "quote": "Buoyant granitic plutons ascend through crustal fractures to **emplace** themselves within older sedimentary strata."
      },
      {
        "author": "T. E. Lawrence",
        "work": "Seven Pillars of Wisdom",
        "quote": "We worked through the night to **emplace** our two mountain guns commanding the Turkish railway redoubt."
      }
    ]
  },
  "Dashboard — plat\\emplacement.md": {
    "primary": "A prepared platform or reinforced defensive position for a weapon, artillery piece, or radar installation.",
    "secondary": "In structural geology and volcanology, the tectonic process of intrusion and positioning of a magma body or allochthonous terrane.",
    "quotes": [
      {
        "author": "Winston Churchill",
        "work": "The Second World War",
        "quote": "Allied reconnaissance aircraft photographed every reinforced coastal gun **emplacement** along the Atlantic Wall."
      },
      {
        "author": "Norman L. Bowen",
        "work": "The Granite Controversy",
        "quote": "The mechanism of batholith **emplacement** involves stoping, thermal assimilation, and forceful crustal doming."
      },
      {
        "author": "Erskine Childers",
        "work": "The Riddle of the Sands",
        "quote": "Behind the sand dunes lay a hidden concrete **emplacement** guarding the tidal channel."
      }
    ]
  },
  "Dashboard — plat\\neoplatonism.md": {
    "primary": "A philosophical and religious system founded in the 3rd century CE by Plotinus, developing and synthesizing Platonic metaphysics with mystical monism.",
    "secondary": "In the history of philosophy, Neoplatonism posits that all reality emanates from a transcendent primal principle, the One (to Hen), through the Intellect (Nous) and Soul (Psyche).",
    "quotes": [
      {
        "author": "Plotinus",
        "work": "The Enneads",
        "quote": "In the contemplative ascent of **Neoplatonism**, the soul transcends sensory illusion to achieve mystical ecstasy in the One."
      },
      {
        "author": "Bertrand Russell",
        "work": "A History of Western Philosophy",
        "quote": "**Neoplatonism** provided early Christian theology, especially in Saint Augustine, with its primary metaphysical scaffolding."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Julian the Apostate attempted to revive pagan worship by infusing it with the mystical allegories of **Neoplatonism**."
      }
    ]
  },
  "Dashboard — plat\\neoplatonist.md": {
    "primary": "An adherent or philosopher of Neoplatonism, such as Plotinus, Porphyry, Iamblichus, or Proclus.",
    "secondary": "In intellectual history, a thinker influenced by the Neoplatonic tradition during the Renaissance (such as Marsilio Ficino or Pico della Mirandola).",
    "quotes": [
      {
        "author": "Bertrand Russell",
        "work": "A History of Western Philosophy",
        "quote": "To the Alexandrian **Neoplatonist**, intellectual contemplation was the sacred path leading toward unity with the divine source."
      },
      {
        "author": "Saint Augustine",
        "work": "Confessions",
        "quote": "The writings of the **Neoplatonist** philosophers opened my mind to the reality of immaterial spiritual substance."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Every pagan philosopher of the fourth century claimed to be an inspired **Neoplatonist** and interpreter of divine mysteries."
      }
    ]
  },
  "Dashboard — plat\\placable.md": {
    "primary": "Easily calmed, pacified, or appeased; forgiving and willing to be reconciled.",
    "secondary": "In classical theology and moral ethics, describing a deity or person who readily relents from wrath when approached with sincere supplication.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "For see, the morn of friendly hope begins to dawn, and God, though justly angry, shows himself **placable** and mild."
      },
      {
        "author": "Edmund Burke",
        "work": "Speech on Conciliation with America",
        "quote": "A magnanimous empire is ever **placable**, seeking conciliation with aggrieved colonies rather than bloody subjugation."
      },
      {
        "author": "Walter Scott",
        "work": "The Heart of Midlothian",
        "quote": "The magistrate proved more **placable** than expected, granting mercy upon hearing the sister's touching plea."
      }
    ]
  },
  "Dashboard — plat\\placate.md": {
    "primary": "To make someone less angry or hostile; to soothe, appease, or conciliate.",
    "secondary": "In diplomatic history and conflict resolution, taking concessions or offering ritual sacrifices to mollify an adversary or aggrieved faction.",
    "quotes": [
      {
        "author": "Thucydides",
        "work": "History of the Peloponnesian War",
        "quote": "The envoys offered solemn guarantees and gifts in an urgent attempt to **placate** the wrath of the Spartan assembly."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The trembling senate sent lavish tributes to **placate** the barbarian chieftain camping outside the city gates."
      },
      {
        "author": "George Orwell",
        "work": "Animal Farm",
        "quote": "Squealer was dispatched with convincing explanations to **placate** the animals whenever unexpected privations occurred."
      }
    ]
  },
  "Dashboard — plat\\placation.md": {
    "primary": "The act of placating, pacifying, or appeasing someone who is angry or hostile.",
    "secondary": "In religious anthropology, ceremonial rituals, offerings, and prayers performed to appease divine wrath or ancestral spirits.",
    "quotes": [
      {
        "author": "James George Frazer",
        "work": "The Golden Bough",
        "quote": "Primitive religion relies upon continuous rites of **placation** to avert the jealousy of forest demons."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "No amount of verbal **placation** could disarm the mercenary army demanding their promised arrears of pay."
      },
      {
        "author": "Thomas Hobbes",
        "work": "Leviathan",
        "quote": "Fear of invisible powers generates endless superstitious practices aimed at the **placation** of unpredictable spirits."
      }
    ]
  },
  "Dashboard — plat\\placatory.md": {
    "primary": "Intended to make someone less angry or hostile; conciliatory; appeasing.",
    "secondary": "In diplomacy and interpersonal rhetoric, describing concessions, gestures, or tones adopted to diffuse tension.",
    "quotes": [
      {
        "author": "Edith Wharton",
        "work": "The Age of Innocence",
        "quote": "He offered a **placatory** smile, anxious to smooth over the awkward breach of family decorum."
      },
      {
        "author": "Winston Churchill",
        "work": "The Gathering Storm",
        "quote": "A policy of **placatory** concessions toward an aggressive dictator only whets the appetite for further conquest."
      },
      {
        "author": "Henry James",
        "work": "The Wings of the Dove",
        "quote": "Her voice took on a soft, **placatory** cadence that disarmed his rising indignation."
      }
    ]
  },
  "Dashboard — plat\\place.md": {
    "primary": "A particular position, point, or area in space; a location, region, or seat.",
    "secondary": "To put or arrange in a particular position or order; or one's social status, role, or station.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "The Merchant of Venice",
        "quote": "The quality of mercy is not strained, it droppeth as the gentle rain from heaven upon the **place** beneath."
      },
      {
        "author": "Aristotle",
        "work": "Physics",
        "quote": "The question of **place** is fundamental to natural philosophy, for every moving body must exist in some definite locality."
      },
      {
        "author": "Francis Bacon",
        "work": "Essays: Of Great Place",
        "quote": "Men in great **place** are thrice servants: servants of the sovereign or state, servants of fame, and servants of business."
      }
    ]
  },
  "Dashboard — plat\\placeable.md": {
    "primary": "Capable of being placed, positioned, located, or identified in a specific context.",
    "secondary": "In linguistics and dialectology, easily identifiable as belonging to a particular geographic region or social class.",
    "quotes": [
      {
        "author": "George Bernard Shaw",
        "work": "Pygmalion",
        "quote": "An expert phonetician can identify every dialect speaker as **placeable** within two miles in London."
      },
      {
        "author": "Henry James",
        "work": "The American",
        "quote": "His robust optimism was not readily **placeable** within the rigid hierarchy of traditional European aristocracy."
      },
      {
        "author": "Thomas Hardy",
        "work": "Tess of the d'Urbervilles",
        "quote": "Her gentle, musical accent was scarcely **placeable** by those unfamiliar with the isolated Blackmoor Vale."
      }
    ]
  },
  "Dashboard — plat\\placed.md": {
    "primary": "Put or arranged in a particular position, rank, or situation; past tense of place.",
    "secondary": "In competitions (such as horse racing), having finished among the top competitors (usually first, second, or third).",
    "quotes": [
      {
        "author": "John Locke",
        "work": "Second Treatise of Government",
        "quote": "God having made man, and **placed** him under strong obligations of necessity, convenience, and inclination to society."
      },
      {
        "author": "Jane Austen",
        "work": "Pride and Prejudice",
        "quote": "She **placed** the letter before her on the table, reading each measured sentence with astonishment and dismay."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "Ahab **placed** his bone leg in the auger-hole drilled upon the quarterdeck, gazing out across the rolling waves."
      }
    ]
  },
  "Dashboard — plat\\placement.md": {
    "primary": "The action of putting someone or something in a particular place, position, or role.",
    "secondary": "In education and employment, the assignment of students to classes according to ability or the securing of jobs for applicants.",
    "quotes": [
      {
        "author": "Francis D. K. Ching",
        "work": "Building Construction Illustrated",
        "quote": "Careful **placement** of structural columns ensures an efficient and uniform transfer of gravity loads."
      },
      {
        "author": "Frank H. Netter",
        "work": "Atlas of Human Anatomy",
        "quote": "Accurate needle **placement** during regional nerve blockade avoids accidental vascular puncture."
      },
      {
        "author": "Alfred Marshall",
        "work": "Principles of Economics",
        "quote": "The strategic **placement** of retail establishments near central transport nodes maximizes customer footfall."
      }
    ]
  },
  "Dashboard — plat\\placer.md": {
    "primary": "An alluvial deposit of sand, gravel, or soil containing eroded valuable minerals (such as gold or platinum).",
    "secondary": "In mining engineering, placer mining extracts gold nuggets and heavy mineral sands through water washing, sluicing, and panning.",
    "quotes": [
      {
        "author": "Mark Twain",
        "work": "Roughing It",
        "quote": "Every gravel bar along the rushing mountain gulch became a rich **placer** during the initial gold strike."
      },
      {
        "author": "Frank Wigglesworth Clarke",
        "work": "The Data of Geochemistry",
        "quote": "Mechanical sorting by running water concentrates heavy native gold within stream **placer** gravels."
      },
      {
        "author": "Bret Harte",
        "work": "The Luck of Roaring Camp",
        "quote": "The miners toiled from dawn to dusk beside their sluice boxes in the muddy **placer** camp."
      }
    ]
  },
  "Dashboard — plat\\placoid.md": {
    "primary": "Plate-like; flattened; specifically designating the tooth-like dermal denticles characteristic of cartilaginous fishes (sharks and rays).",
    "secondary": "In comparative anatomy and ichthyology, a placoid scale consists of a vascular pulp cavity, dentine, and a hard enameloid cap identical in structure to vertebrate teeth.",
    "quotes": [
      {
        "author": "Louis Agassiz",
        "work": "Recherches sur les Poissons Fossiles",
        "quote": "I classified cartilaginous elasmobranchs into the order **placoid**, characterized by hard enamel-tipped dermal denticles."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "Each tiny **placoid** spine on the shark's skin is homologous in structure and development to a mammalian tooth."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The rough sandpaper texture of shark skin is due to millions of microscopic **placoid** scales."
      }
    ]
  },
  "Dashboard — plat\\plaice.md": {
    "primary": "A European marine flatfish (Pleuronectes platessa) of commercial importance, having an oval body with reddish-orange spots on its brown upper side.",
    "secondary": "In fishery biology, the plaice is a bottom-dwelling flatfish of the North Sea and Northeast Atlantic, possessing asymmetrical dextral eyes and feeding on benthic bivalves.",
    "quotes": [
      {
        "author": "Izaak Walton",
        "work": "The Compleat Angler",
        "quote": "The sea yields many delicate flatfish, whereof the spotted **plaice** and the sole are prized above all for the table."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The larval **plaice** begins life swimming upright like an ordinary fish before its left eye migrates across the skull."
      },
      {
        "author": "George Brown Goode",
        "work": "Fisheries and Fishery Industries of the United States",
        "quote": "European trawlers take vast quantities of European **plaice** over the shallow sandy banks of the North Sea."
      }
    ]
  },
  "Dashboard — plat\\plat.md": {
    "primary": "A plan, map, or chart of a piece of land, especially showing actual or proposed features such as lots, roads, and boundaries.",
    "secondary": "A plot of ground; or archaic variant of plat (flat, plain, or braided straw).",
    "quotes": [
      {
        "author": "Thomas Jefferson",
        "work": "Notes on the State of Virginia",
        "quote": "The surveyor drafted an accurate **plat** dividing the western territory into regular square townships."
      },
      {
        "author": "John Milton",
        "work": "Il Penseroso",
        "quote": "Oft, on a **plat** of rising ground, I hear the far-off curfew sound, over some wide-watered shore."
      },
      {
        "author": "George Washington",
        "work": "Diaries",
        "quote": "I surveyed the river bend and laid off a new **plat** for the experimental tobacco fields."
      }
    ]
  },
  "Dashboard — plat\\plataea.md": {
    "primary": "An ancient city in Boeotia, Greece, famous as the site of the Battle of Plataea in 479 BCE.",
    "secondary": "In classical Greek history, at the Battle of Plataea, the allied Greek land army led by the Spartan general Pausanias decisively defeated the Persian forces of Mardonius.",
    "quotes": [
      {
        "author": "Herodotus",
        "work": "Histories",
        "quote": "The glorious victory at **Plataea** broke the power of the Persian invader and delivered Greece from barbarian subjugation."
      },
      {
        "author": "Thucydides",
        "work": "History of the Peloponnesian War",
        "quote": "The heroic defense of **Plataea** against the Spartan siege demonstrated the tragic fate of a faithful Athenian ally."
      },
      {
        "author": "Plutarch",
        "work": "Parallel Lives: Aristides",
        "quote": "At **Plataea**, Aristides displayed consummate tactical prudence, uniting contentious Greek contingents against common peril."
      }
    ]
  },
  "Dashboard — plat\\platalea.md": {
    "primary": "A genus of large, long-legged wading birds in the ibis and spoonbill family (Threskiornithidae), commonly known as spoonbills.",
    "secondary": "In systematic ornithology, birds of the genus *Platalea* are distinguished by their broad, spatulate bill, which they sweep side-to-side through shallow water to catch aquatic prey.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Systema Naturae",
        "quote": "The genus **Platalea** is defined by its remarkable flat, spatulate beak, widened at the tip into the shape of a spoon."
      },
      {
        "author": "John James Audubon",
        "work": "The Birds of America",
        "quote": "The roseate spoonbill, classified in **Platalea**, presents plumage of breathtaking carmine and rose pink along Florida lagoons."
      },
      {
        "author": "John Gould",
        "work": "The Birds of Australia",
        "quote": "The yellow-billed spoonbill of the genus **Platalea** wades through inland billabongs with stately deliberation."
      }
    ]
  },
  "Dashboard — plat\\plataleidae.md": {
    "primary": "A family (or subfamily Plataleinae within Threskiornithidae) of wading birds comprising the spoonbills.",
    "secondary": "In avian taxonomy, members of Plataleidae share dorsoventrally flattened bills adapted for tactile foraging in muddy coastal and freshwater wetlands.",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "The Geographical Distribution of Animals",
        "quote": "The cosmopolitan distribution of the **Plataleidae** indicates the antiquity of these specialized wetland wading birds."
      },
      {
        "author": "Elliott Coues",
        "work": "Key to North American Birds",
        "quote": "The osteological structure of the bill readily separates the **Plataleidae** from the curved-billed true ibises."
      },
      {
        "author": "Ernst Mayr",
        "work": "Systematics and the Origin of Species",
        "quote": "Evolutionary divergence in **Plataleidae** reflects adaptation to muddy estuarine feeding niches across tropical continents."
      }
    ]
  },
  "Dashboard — plat\\platan.md": {
    "primary": "The oriental plane tree (Platanus orientalis) or plane tree in general (poetic or archaic form).",
    "secondary": "In classical literature, the broad, spreading shade of the platan tree was celebrated by Greek philosophers as the ideal setting for intellectual dialogue.",
    "quotes": [
      {
        "author": "Plato",
        "work": "Phaedrus",
        "quote": "By Hera, a fair resting-place! For this **platan** tree is very broad and lofty, providing cooling shade over the cold spring."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "Spreading their fragrant boughs, the cedar, pine, and **platan** branched out over the lush garden lawns."
      },
      {
        "author": "Lord Byron",
        "work": "Childe Harold's Pilgrimage",
        "quote": "Under the ancient **platan**'s emerald dome, the weary traveler rests beside the Aegean shore."
      }
    ]
  },
  "Dashboard — plat\\platanaceae.md": {
    "primary": "The plane-tree family of flowering plants in the order Proteales, consisting of the single extant genus Platanus.",
    "secondary": "In dendrology and paleobotany, Platanaceae are deciduous trees characterized by palmately lobed leaves, exfoliating bark, and spherical pendant fruiting heads.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The family **Platanaceae** is represented in our flora by the colossal sycamore or buttonwood along river bottoms."
      },
      {
        "author": "Charles Darwin",
        "work": "The Different Forms of Flowers on Plants of the Same Species",
        "quote": "Wind-pollinated monoecious flowers grouped in dense pendulous globes characterize the family **Platanaceae**."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "Abundant multiseriate rays and diffuse-porous vessels are distinctive anatomical features of the wood in **Platanaceae**."
      }
    ]
  },
  "Dashboard — plat\\platanistidae.md": {
    "primary": "A family of freshwater river dolphins comprising the South Asian river dolphins (Platanista gangetica and Platanista minor).",
    "secondary": "In cetology, members of Platanistidae inhabit the Indus, Ganges, and Brahmaputra river systems, having reduced eyes and relying on echolocation and tactile flippers in turbid waters.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of the Cetacea",
        "quote": "The cranial maxillae in **Platanistidae** bear prominent bony crests that arch forward over the blowhole."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes and Aquatic Mammals",
        "quote": "The blind river dolphin of the family **Platanistidae** navigates muddy Indian currents by emitting continuous sonar clicks."
      },
      {
        "author": "George Gaylord Simpson",
        "work": "The Principles of Classification and a Classification of Mammals",
        "quote": "The archaic anatomical traits of **Platanistidae** separate them from modern oceanic delphinid lineages."
      }
    ]
  },
  "Dashboard — plat\\platanthera.md": {
    "primary": "A genus of terrestrial orchids in the family Orchidaceae, commonly known as bog orchids or fringed orchids.",
    "secondary": "In orchidology and pollination biology, *Platanthera* species bear spurs containing nectar accessible to long-tongued moths, illustrating intricate co-evolution.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Various Contrivances by Which Orchids Are Fertilised by Insects",
        "quote": "In **Platanthera** chlorantha, the pollinia adhere with remarkable precision to the eyes of nocturnal sphingid moths."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The fringed purple bog orchid, belonging to **Platanthera**, adorns northern peat meadows with stately spikes."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "Species of **Platanthera** flourish in moist, acidic woodland soils, producing delicate spurred blossoms."
      }
    ]
  },
  "Dashboard — plat\\platanus.md": {
    "primary": "A genus of large, deciduous trees in the family Platanaceae, commonly known as plane trees, sycamores, or buttonwoods.",
    "secondary": "In urban forestry and arboriculture, the London plane (*Platanus x acerifolia*) is widely planted in cities worldwide due to its exceptional tolerance of air pollution and pruning.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "The noble tree **Platanus** occidentalis attains monumental girth in the fertile alluvial soils of North America."
      },
      {
        "author": "John Muir",
        "work": "Our National Parks",
        "quote": "The smooth, mottled white trunks of **Platanus** stand like gleaming marble columns along the canyon streams."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Hybrid vigor is strikingly exhibited by the London plane, a fertile cross between American and oriental species of **Platanus**."
      }
    ]
  },
  "Dashboard — plat\\plate.md": {
    "primary": "A flat, usually round dish from which food is served or eaten; or a thin, flat sheet of metal or other material.",
    "secondary": "In geology and plate tectonics, one of the large rigid lithospheric slabs that make up the Earth's crust and move across the asthenosphere.",
    "quotes": [
      {
        "author": "Alfred Wegener",
        "work": "The Origin of Continents and Oceans",
        "quote": "Continental drift demonstrated that vast landmasses move like slabs across the oceanic **plate** substrate."
      },
      {
        "author": "William Shakespeare",
        "work": "The Winter's Tale",
        "quote": "The queen has placed the savory feast upon each golden **plate** with regal dignity."
      },
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "Light reflected between a curved glass lens and a flat glass **plate** produces the colored interference rings now named for me."
      }
    ]
  },
  "Dashboard — plat\\plateful.md": {
    "primary": "The amount that a plate can hold; a generous helping or portion of food served on a plate.",
    "secondary": "Informally, a large quantity or abundance of work, troubles, or responsibilities.",
    "quotes": [
      {
        "author": "Charles Dickens",
        "work": "Oliver Twist",
        "quote": "Oliver gazed longing at the steaming **plateful** of hot roast beef being carried past to the master's table."
      },
      {
        "author": "Mark Twain",
        "work": "The Adventures of Tom Sawyer",
        "quote": "Aunt Polly heaped a generous **plateful** of fried chicken before the hungry runaway."
      },
      {
        "author": "George Eliot",
        "work": "Silas Marner",
        "quote": "The hearty farmer consumed his substantial **plateful** with the relish of a man who worked outdoors from sunrise."
      }
    ]
  },
  "Dashboard — plat\\platelayer.md": {
    "primary": "A railway employee whose job is to inspect, repair, and maintain railway tracks (plates and rails).",
    "secondary": "In industrial history, platelayers manually replaced ballast, gauged rails, and tightened fishplates to maintain track safety along high-speed corridors.",
    "quotes": [
      {
        "author": "George Stephenson",
        "work": "Reports on the Liverpool and Manchester Railway",
        "quote": "Every vigilant **platelayer** must inspect his designated mile of iron rail daily to prevent derailments."
      },
      {
        "author": "Thomas Hardy",
        "work": "Jude the Obscure",
        "quote": "The lonely **platelayer** walked the ballast with his heavy hammer, checking the alignment of the ties."
      },
      {
        "author": "H. G. Wells",
        "work": "Tono-Bungay",
        "quote": "From the carriage window we watched the gang of **platelayer** workmen step aside as the express rushed past."
      }
    ]
  },
  "Dashboard — plat\\platelet.md": {
    "primary": "A small, disk-shaped clear cell fragment found in large numbers in blood, essential for normal blood clotting (thrombocyte).",
    "secondary": "In hematology, platelets are produced by megakaryocytes in bone marrow; they adhere to exposed subendothelial collagen and aggregate to form a primary hemostatic plug.",
    "quotes": [
      {
        "author": "Giulio Bizzozero",
        "work": "On a New Blood Element and Its Role in Thrombosis and Blood Coagulation",
        "quote": "I observed that the blood **platelet** adheres instantaneously to the site of injured vascular endothelium, initiating thrombosis."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Bizzozero's third corpuscular element, the blood **platelet**, is crucial for sealing microscopic vascular leaks."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Activated by thrombin, the **platelet** undergoes profound cytoskeletal transformation, extending filopodia and releasing pro-coagulant granules."
      }
    ]
  },
  "Dashboard — plat\\plateletpheresis.md": {
    "primary": "A specialized apheresis procedure in which blood is drawn from a donor, platelets are separated and collected, and the remaining blood components are returned.",
    "secondary": "In transfusion medicine, a single-donor plateletpheresis yields a therapeutic platelet dose equivalent to 6 to 8 pooled whole-blood platelet units, minimizing recipient antigen exposure.",
    "quotes": [
      {
        "author": "Maxwell M. Wintrobe",
        "work": "Clinical Hematology",
        "quote": "Modern transfusion services rely on **plateletpheresis** to provide HLA-matched single-donor platelets for refractory thrombocytopenic patients."
      },
      {
        "author": "Tinsley R. Harrison",
        "work": "Principles of Internal Medicine",
        "quote": "Automated **plateletpheresis** allows healthy volunteers to donate platelets safely every few weeks without lowering their red cell count."
      },
      {
        "author": "Eugene Braunwald",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "Prophylactic transfusion using products obtained via **plateletpheresis** prevents spontaneous intracranial hemorrhage during induction chemotherapy."
      }
    ]
  },
  "Dashboard — plat\\platelike.md": {
    "primary": "Resembling a plate; thin, flat, and broad in shape.",
    "secondary": "In mineralogy and structural histology, describing lamellar crystals, epithelial squames, or bone trabeculae with planar geometry.",
    "quotes": [
      {
        "author": "James Dwight Dana",
        "work": "System of Mineralogy",
        "quote": "The mineral mica cleaves into remarkably thin, transparent, **platelike** sheets along its basal pinacoid."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "The squamous epithelium consists of **platelike** cells fitted edge to edge like mosaic paving stones."
      },
      {
        "author": "Frank Wigglesworth Clarke",
        "work": "The Data of Geochemistry",
        "quote": "Clay minerals consist of microscopic, **platelike** aluminosilicate sheets that slide easily over one another when hydrated."
      }
    ]
  },
  "Dashboard — plat\\platen.md": {
    "primary": "A flat plate in a printing press that presses the paper against the inked type; or the rubber roller on a typewriter.",
    "secondary": "In mechanical engineering, a sturdy flat mounting plate in a hydraulic press or molding machine that applies uniform compressive force.",
    "quotes": [
      {
        "author": "Benjamin Franklin",
        "work": "Autobiography",
        "quote": "I took my place at the press, pulling the heavy lever to bring the wooden **platen** down upon the sheet."
      },
      {
        "author": "William Morris",
        "work": "The Ideal Book",
        "quote": "The hand-press craftsman regulates the pressure of the iron **platen** with exquisite touch to secure deep, crisp typography."
      },
      {
        "author": "Lewis Mumford",
        "work": "Technics and Civilization",
        "quote": "The continuous rotation of the cylinder press supplanted the flat **platen**, multiplying daily newspaper output a thousandfold."
      }
    ]
  },
  "Dashboard — plat\\plater.md": {
    "primary": "A person whose trade is plating metals, or a racehorse that runs primarily in selling plates (races).",
    "secondary": "In shipbuilding and heavy metal fabrication, a skilled tradesperson who cuts, shapes, and fits steel plates to the hull or frame.",
    "quotes": [
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "The commercial electro-**plater** utilizes a copper bath to deposit a durable metallic coating upon base alloys."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "Silver Blaze",
        "quote": "He had purchased an ordinary selling **plater** and entered him into the classic stakes under an assumed name."
      },
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "The shipyard **plater** earns higher wages because his craft requires mechanical precision combined with arduous physical exertion."
      }
    ]
  },
  "Dashboard — plat\\platichthys.md": {
    "primary": "A genus of righteye flounders in the family Pleuronectidae, commonly known as starry flounders (Platichthys stellatus).",
    "secondary": "In marine biology, *Platichthys* species inhabit coastal waters and estuaries of the North Pacific, distinguished by starry tubercles and euryhaline tolerance to fresh water.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "The Fishes of North and Middle America",
        "quote": "The starry flounder of the genus **Platichthys** is covered with rough, stellate tubercles instead of ordinary scales."
      },
      {
        "author": "George Brown Goode",
        "work": "Oceanic Ichthyology",
        "quote": "Specimens of **Platichthys** frequently ascend Pacific rivers for many miles, foraging in purely fresh water."
      },
      {
        "author": "William K. Gregory",
        "work": "Fish Skulls",
        "quote": "The cranial asymmetry of **Platichthys** exhibits a high frequency of reversed (left-eyed) individuals in western Pacific populations."
      }
    ]
  },
  "Dashboard — plat\\plating.md": {
    "primary": "A thin layer or coating of metal applied to the surface of an object, typically by electrodeposition or chemical dipping.",
    "secondary": "In marine and locomotive engineering, the outer skin of overlapping steel or iron plates covering a ship's hull or boiler.",
    "quotes": [
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "Electrochemical **plating** with gold or silver provides an impermeable coating that shields underlying metals from oxidation."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The copper **plating** on the ship's bottom gleamed like a golden shield through the crystal tropical water."
      },
      {
        "author": "Humphry Davy",
        "work": "Elements of Chemical Philosophy",
        "quote": "Galvanic action between the iron hull and copper **plating** caused rapid corrosion until sacrificial zinc protectors were installed."
      }
    ]
  },
  "Dashboard — plat\\platinize.md": {
    "primary": "To coat, treat, or impregnate with platinum or a platinum salt.",
    "secondary": "In electrochemistry, to platinize an electrode involves electrodepositing a fine, velvety layer of 'platinum black' to drastically increase surface area and reduce overpotential.",
    "quotes": [
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "To ensure reliable electrical contact and minimize polarization, we **platinize** the electrodes before measuring resistance."
      },
      {
        "author": "J. Willard Gibbs",
        "work": "On the Equilibrium of Heterogeneous Substances",
        "quote": "Electrochemists **platinize** platinum foil to ensure reversible hydrogen electrode equilibration with aqueous hydronium ions."
      },
      {
        "author": "Gilbert N. Lewis",
        "work": "Thermodynamics",
        "quote": "Careful experimenters **platinize** the conductivity cells to prevent capacitive distortion during alternating-current bridge measurements."
      }
    ]
  },
  "Dashboard — plat\\platinum-blonde.md": {
    "primary": "A very pale silvery-blonde hair color, or a person having this hair color.",
    "secondary": "In cultural and cinema history, popularized in the 1930s by Hollywood actress Jean Harlow, signifying a bleached, glamorous modern aesthetic.",
    "quotes": [
      {
        "author": "F. Scott Fitzgerald",
        "work": "The Love of the Last Tycoon",
        "quote": "Her striking **platinum-blonde** hair caught the studio spotlights, framing her porcelain features with luminous brilliance."
      },
      {
        "author": "Raymond Chandler",
        "work": "The Big Sleep",
        "quote": "She was a tall **platinum-blonde** with watchful eyes and a cigarette held casually between lacquered fingers."
      },
      {
        "author": "Truman Capote",
        "work": "Breakfast at Tiffany's",
        "quote": "Holly Golightly stood in the doorway, a streak of **platinum-blonde** gleaming amidst her tawny hair."
      }
    ]
  },
  "Dashboard — plat\\platinum.md": {
    "primary": "A dense, malleable, ductile, precious transition metal (symbol Pt, atomic number 78) that is silver-white and highly resistant to chemical corrosion.",
    "secondary": "In industrial chemistry and catalysis, platinum is an indispensable heterogeneous catalyst for automobile catalytic converters, petroleum reforming, and hydrogen fuel cells.",
    "quotes": [
      {
        "author": "Antoine Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "The extraordinary unalterability of **platinum** in fire and acid renders it invaluable for delicate laboratory apparatus."
      },
      {
        "author": "Michael Faraday",
        "work": "The Chemical History of a Candle",
        "quote": "Spongy **platinum** possesses the wondrous property of causing hydrogen and oxygen to combine into water without any applied flame."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "The square-planar geometry of divalent **platinum** complexes provided Werner with crucial evidence for stereochemical coordination theory."
      }
    ]
  },
  "Dashboard — plat\\platitudinal.md": {
    "primary": "Characteristic of, containing, or resembling a platitude; trite, banal, or clichéd.",
    "secondary": "In literary and political criticism, describing discourse dominated by superficial, unoriginal, and moralizing commonplaces.",
    "quotes": [
      {
        "author": "H. L. Mencken",
        "work": "Prejudices",
        "quote": "The politician’s speech was a masterpiece of **platitudinal** vacuity, pledging everything while committing to nothing."
      },
      {
        "author": "George Bernard Shaw",
        "work": "Major Barbara",
        "quote": "He defended his hypocrisy with **platitudinal** sermons that bored his rebellious children to distraction."
      },
      {
        "author": "Virginia Woolf",
        "work": "Night and Day",
        "quote": "She found herself answering in **platitudinal** phrases, concealing her true anxiety behind polite social banalities."
      }
    ]
  },
  "Dashboard — plat\\platitudinarian.md": {
    "primary": "A person who habitually utters platitudes; one given to moralizing triteness.",
    "secondary": "In intellectual satire, a dull speaker or writer who delivers commonplace bromides as if they were profound discoveries.",
    "quotes": [
      {
        "author": "Thomas Carlyle",
        "work": "Sartor Resartus",
        "quote": "Deliver us from the pompous **platitudinarian**, who drones out lifeless maxims while living souls are starving for truth!"
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Table Talk",
        "quote": "A true thinker penetrates beneath appearances, whereas the **platitudinarian** skates complacently upon the frozen surface of thought."
      },
      {
        "author": "Oscar Wilde",
        "work": "The Decay of Lying",
        "quote": "The tedious **platitudinarian** robs conversation of all surprise, reducing wit to moralistic nursery rhymes."
      }
    ]
  },
  "Dashboard — plat\\platitudinize.md": {
    "primary": "To utter or write platitudes; to make trite, commonplace remarks.",
    "secondary": "In rhetorical criticism, to substitute stale moral formulas and cliches for rigorous logical analysis.",
    "quotes": [
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "It was impossible to discuss serious civic reform with a mayor whose only talent was to **platitudinize** at parish meetings."
      },
      {
        "author": "H. L. Mencken",
        "work": "The American Language",
        "quote": "Editorial writers across the provinces continue to **platitudinize** about civic duty without examining municipal corruption."
      },
      {
        "author": "Aldous Huxley",
        "work": "Point Counter Point",
        "quote": "Whenever awkward questions of morality were raised, the headmaster would clear his throat and begin to **platitudinize**."
      }
    ]
  },
  "Dashboard — plat\\platitudinous.md": {
    "primary": "Used too often to be interesting or thoughtful; hackneyed, trite, or clichéd.",
    "secondary": "Characterized by dull, moralizing banality that adds no substance to discourse.",
    "quotes": [
      {
        "author": "George Orwell",
        "work": "Politics and the English Language",
        "quote": "Modern political writing is largely composed of **platitudinous** phrases gummed together like prefabricated building blocks."
      },
      {
        "author": "Bertrand Russell",
        "work": "Unpopular Essays",
        "quote": "To escape from **platitudinous** dogma, a society must encourage fearless intellectual skepticism."
      },
      {
        "author": "Henry James",
        "work": "The Portrait of a Lady",
        "quote": "Madame Merle avoided all **platitudinous** compliments, preferring the refined flattery of perceptive silence."
      }
    ]
  },
  "Dashboard — plat\\plato.md": {
    "primary": "An ancient Greek philosopher (c. 428–348 BCE), student of Socrates and teacher of Aristotle, who founded the Academy in Athens.",
    "secondary": "In Western philosophy, Plato authored foundational philosophical dialogues (such as The Republic, Symposium, and Phaedo), formulating the Theory of Forms and dialectical inquiry.",
    "quotes": [
      {
        "author": "Alfred North Whitehead",
        "work": "Process and Reality",
        "quote": "The safest general characterization of the European philosophical tradition is that it consists of a series of footnotes to **Plato**."
      },
      {
        "author": "Aristotle",
        "work": "Metaphysics",
        "quote": "**Plato** introduced the Forms to explain that sensible things are in flux, while knowledge requires permanent immaterial essences."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "Representative Men",
        "quote": "**Plato** is philosophy, and philosophy is **Plato**; out of him all that has been written and thought by men draws its origin."
      }
    ]
  }
};

const count = updateNotesBatch(baseDir, batchData);
console.log(`Updated ${count} notes in Form Finish Slice 2 Batch 6.`);
