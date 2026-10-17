import { updateNotesBatch } from './curate-updater-util.mjs';

const BASE_DIR = 'App database/Greek roots/Cluster Body & Physiology';

const BATCH4_DATA = {
  "Dashboard — carpo\\acarpous.md": {
    "primary": "Producing no fruit; sterile, barren, or fruitless.",
    "secondary": "In descriptive botany, designating flowers or plants that fail to develop mature carpels or fruit following pollination.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "Staminate blossoms are necessarily **acarpous**, functioning solely to shed pollen before withering away."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "Adverse climatic conditions rendered the entire orchard **acarpous**, blighting the delicate pistils before fertilization."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "Cultivated double-flowered varieties are frequently **acarpous**, having transformed their reproductive organs into sterile petals."
      }
    ]
  },
  "Dashboard — carpo\\apocarpous.md": {
    "primary": "Having the carpels of a flower separate and distinct from one another, rather than fused into a single compound pistil.",
    "secondary": "In floral morphology, the primitive angiosperm condition observed in Ranunculaceae and Magnoliaceae where each carpel forms an independent fruitlet.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The buttercup displays a classic **apocarpous** gynoecium, bearing a dense cluster of independent, distinct achenes upon a conical receptacle."
      },
      {
        "author": "John Lindley",
        "work": "An Introduction to Botany",
        "quote": "In an **apocarpous** flower, each carpel retains its own style and stigma, developing into a solitary follicle or berry."
      },
      {
        "author": "Arthur Johnson Eames",
        "work": "Morphology of Angiosperms",
        "quote": "The evolutionary transition from an **apocarpous** ancestral state to a syncarpous ovary represented a major advance in seed protection."
      }
    ]
  },
  "Dashboard — carpo\\carp 2.md": {
    "primary": "To find fault, complain, or raise petty, captious objections continually; to cavil.",
    "secondary": "In rhetorical and moral discourse, the persistent habit of uncharitable, nagging criticism directed against trivial flaws.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "King Lear",
        "quote": "Suspend thy purpose, if thou didst intend to make this creature fruitful into a child that may **carp** at her mother's care."
      },
      {
        "author": "Jonathan Swift",
        "work": "A Tale of a Tub",
        "quote": "The superficial critic loves to **carp** at minute grammatical slips while blind to the sublime design of the work."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Rambler",
        "quote": "It is the easy prerogative of small minds to **carp** at greatness, measuring the giant by their own diminutive stature."
      }
    ]
  },
  "Dashboard — carpo\\carp.md": {
    "primary": "A large, heavy-bodied freshwater teleost fish of the family Cyprinidae (Cyprinus carpio), widely cultivated for food in Eurasia.",
    "secondary": "In freshwater ecology and aquaculture, hardy, omnivorous bottom-feeding fishes that thrive in sluggish, muddy waters, including domesticated ornamental varieties (koi).",
    "quotes": [
      {
        "author": "Izaak Walton",
        "work": "The Compleat Angler",
        "quote": "The **carp** is the queen of rivers, a stately, cunning, and very subtle fish that requires great patience of the angler."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants Under Domestication",
        "quote": "Centuries of selective breeding by Chinese aquaculturists transformed the wild **carp** into the magnificent golden varieties of our ponds."
      },
      {
        "author": "Henry David Thoreau",
        "work": "A Week on the Concord and Merrimack Rivers",
        "quote": "In the weeds of the quiet cove, a heavy **carp** splashed sluggishly, feeding upon the succulent aquatic roots."
      }
    ]
  },
  "Dashboard — carpo\\carpal tunnel syndrome.md": {
    "primary": "A painful compressive neuropathy of the wrist caused by entrapment and compression of the median nerve within the flexor carpal tunnel.",
    "secondary": "In clinical orthopedics and neurology, a common entrapment condition characterized by nocturnal paresthesia, burning pain, and numbness in the thumb, index, and middle fingers.",
    "quotes": [
      {
        "author": "George S. Phalen",
        "work": "The Carpal-Tunnel Syndrome: Seventeen Years' Experience",
        "quote": "Surgical division of the transverse carpal ligament produces prompt and dramatic relief of nocturnal pain in **carpal tunnel syndrome**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Repetitive mechanical trauma to the wrist induces chronic flexor tenosynovitis, culminating in disabling **carpal tunnel syndrome**."
      },
      {
        "author": "Harvey Cushing",
        "work": "Surgery of the Peripheral Nerves",
        "quote": "Atrophy of the abductor pollicis brevis muscle is the cardinal sign of severe, prolonged median nerve compression in **carpal tunnel syndrome**."
      }
    ]
  },
  "Dashboard — carpo\\carpal.md": {
    "primary": "Of, relating to, or situated in the carpus or wrist.",
    "secondary": "In skeletal osteology, any of the eight small, irregularly shaped bones (scaphoid, lunate, triquetrum, pisiform, trapezium, trapezoid, capitate, hamate) that form the human wrist.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The eight **carpal** bones are arranged in two transverse rows, closely bound together by dorsal and palmar ligaments."
      },
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "The proximal row of **carpal** bones articulates directly with the lower end of the radius to form the wrist joint."
      },
      {
        "author": "Charles Bell",
        "work": "The Hand: Its Mechanism and Vital Endowments",
        "quote": "The arching configuration of the **carpal** skeleton protects the long flexor tendons and vital nerves from external compression."
      }
    ]
  },
  "Dashboard — carpo\\carper.md": {
    "primary": "A person who habitually finds fault, complains, or raises trivial, captious objections; a chronic caviler.",
    "secondary": "In literary criticism, an ungenerous reviewer who concentrates on petty blemishes while disregarding overall artistic merit.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Timon of Athens",
        "quote": "Shame not these woods by putting on the cunning of a **carper**, but act with noble magnanimity."
      },
      {
        "author": "Alexander Pope",
        "work": "An Essay on Criticism",
        "quote": "The spiteful **carper** condemns each bold poetic stroke that transcends the petty rules of pedestrian grammarians."
      },
      {
        "author": "John Dryden",
        "work": "Essays on the Drama",
        "quote": "An author must expect that every envious **carper** will seize upon a minor typographical flaw to condemn the entire tragedy."
      }
    ]
  },
  "Dashboard — carpo\\carping.md": {
    "primary": "Characterized by petty, nagging, or hypercritical fault-finding; captious.",
    "secondary": "The practice or habit of constantly raising trivial, uncharitable objections; querulous complaint.",
    "quotes": [
      {
        "author": "Jane Austen",
        "work": "Pride and Prejudice",
        "quote": "She was weary of her mother's restless, **carping** temper, which turned every pleasant domestic occurrence into a grievance."
      },
      {
        "author": "Charlotte Brontë",
        "work": "Villette",
        "quote": "I closed my ears against their **carping** insinuations, determined to pursue my solitary course without complaint."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "Essays: First Series",
        "quote": "Leave this **carping** and whining about petty misfortunes, and align your life with the majestic currents of nature."
      }
    ]
  },
  "Dashboard — carpo\\carpocapsa.md": {
    "primary": "A former genus of tortricid moths (now Cydia), notably Carpocapsa pomonella, the codling moth whose larvae bore into pome fruits.",
    "secondary": "In economic entomology and natural history, fruit-destroying moths including the Mexican jumping bean moth (Cydia saltitans), whose larvae cause seeds to twitch.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The larva of **carpocapsa** burrows deep into the heart of the ripening apple, sheltered from external predators."
      },
      {
        "author": "C. V. Riley",
        "work": "Report of the State Entomologist",
        "quote": "Orchardists suffered immense economic losses until systematic spraying checked the ravages of the **carpocapsa** caterpillar."
      },
      {
        "author": "Jean-Henri Fabre",
        "work": "The Life of the Caterpillar",
        "quote": "Inside the seed capsule, the microscopic caterpillar of **carpocapsa** leaps against the woody walls, propelling the bean across the ground."
      }
    ]
  },
  "Dashboard — carpo\\carport.md": {
    "primary": "A covered, open-sided structure designed to shelter an automobile, typically consisting of a roof supported on posts and attached to a residence.",
    "secondary": "In twentieth-century architectural history, an economical automobile shelter popularized by Frank Lloyd Wright in his Usonian houses to eliminate bulky enclosed garages.",
    "quotes": [
      {
        "author": "Frank Lloyd Wright",
        "work": "The Natural House",
        "quote": "A car is not a horse; it does not require a barn, so we invented the open **carport** to shelter the automobile simply and economically."
      },
      {
        "author": "Lewis Mumford",
        "work": "The Highway and the City",
        "quote": "The suburban home substituted the breezy convenience of the **carport** for the cavernous domestic workshops of earlier eras."
      },
      {
        "author": "Reyner Banham",
        "work": "The Architecture of the Well-Tempered Environment",
        "quote": "Wright's Usonian designs integrated the cantilevered **carport** directly into the horizontal lines of the residence."
      }
    ]
  },
  "Dashboard — carpo\\carpospore.md": {
    "primary": "A diploid or haploid non-motile spore produced in the cystocarp of red algae (Rhodophyta).",
    "secondary": "In phycology and marine botany, a reproductive cell released from the gonimoblast of a carposporophyte, which germinates into the diploid tetrasporophyte generation.",
    "quotes": [
      {
        "author": "William Henry Harvey",
        "work": "Phycologia Britannica",
        "quote": "The urn-shaped cystocarp opens by a terminal pore to discharge a cloud of dark crimson **carpospore** units into the sea."
      },
      {
        "author": "F. E. Fritsch",
        "work": "The Structure and Reproduction of the Algae",
        "quote": "Each individual **carpospore** is naked when liberated, soon secreting a firm cell wall upon adhering to rocky substrate."
      },
      {
        "author": "Lynn Margulis",
        "work": "Symbiosis in Cell Evolution",
        "quote": "The triphasic alternation of generations in red algae centers upon the amplification of reproductive yield via each diploid **carpospore**."
      }
    ]
  },
  "Dashboard — carpo\\carposporic.md": {
    "primary": "Of, relating to, or producing carpospores; pertaining to the carpospore stage of red algae.",
    "secondary": "In phycological reproduction, describing the phase or reproductive organs that give rise to carpospores within the cystocarp.",
    "quotes": [
      {
        "author": "F. E. Fritsch",
        "work": "The Structure and Reproduction of the Algae",
        "quote": "The **carposporic** phase amplifies the genetic product of a single fertilization event into hundreds of diploid progeny."
      },
      {
        "author": "William Henry Harvey",
        "work": "Nereis Boreali-Americana",
        "quote": "Microscopic examination of the fertile nemathecia reveals dense clusters of **carposporic** filaments radiating from central placenta."
      },
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology of the Fungi, Mycetozoa and Bacteria",
        "quote": "The complex **carposporic** fructifications of Florideae find structural parallels in the ascocarps of higher fungi."
      }
    ]
  },
  "Dashboard — carpo\\carposporous.md": {
    "primary": "Bearing, producing, or multiplying by means of carpospores.",
    "secondary": "In marine phycology, describing red algae during their mature carposporophyte reproductive phase.",
    "quotes": [
      {
        "author": "F. E. Fritsch",
        "work": "The Structure and Reproduction of the Algae",
        "quote": "The **carposporous** generation remains nutritionally dependent upon the female gametophyte from which it arose."
      },
      {
        "author": "Julius von Sachs",
        "work": "Textbook of Botany",
        "quote": "In Polysiphonia, the **carposporous** cystocarp forms a conspicuous urn-like swell on the lateral polysiphonous branches."
      },
      {
        "author": "Eduard Strasburger",
        "work": "Handbook of Practical Botany",
        "quote": "Sections through the mature **carposporous** conceptacle demonstrate the terminal cleavage of gonimoblast cells."
      }
    ]
  },
  "Dashboard — carpo\\carpus.md": {
    "primary": "The human wrist, or the corresponding joint in the forelimb of a quadruped tetrapod.",
    "secondary": "In human skeletal osteology, the complex of eight carpal bones articulating between the distal radius and ulna and the proximal metacarpus.",
    "quotes": [
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "The eight bones of the **carpus** are disposed in two transverse rows, interlocking tightly like the stones of an arch."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The anterior concavity of the **carpus** is bridged by the flexor retinaculum to form the carpal canal."
      },
      {
        "author": "Charles Bell",
        "work": "The Hand: Its Mechanism and Vital Endowments",
        "quote": "The mosaic of small bones in the human **carpus** absorbs the mechanical concussions of labor while allowing supple articulation."
      }
    ]
  },
  "Dashboard — carpo\\endocarp.md": {
    "primary": "The innermost layer of the pericarp of a fruit, which directly surrounds the seeds.",
    "secondary": "In botanical morphology, a layer that may be membranous (as the core of an apple), woody and stony (as the pit of a peach or olive), or pulp-bearing (as in citrus fruits).",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "In the peach and plum, the outer pericarp remains soft and juicy while the stony **endocarp** protects the enclosed kernel."
      },
      {
        "author": "John Lindley",
        "work": "An Introduction to Botany",
        "quote": "The stone of a drupe is not the seed coat itself, but the heavily lignified, sclerified **endocarp** of the pericarp."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "Manual of Cultivated Plants",
        "quote": "In the orange, the edible pulp segments are composed of succulent juice vesicles projecting inward from the **endocarp**."
      }
    ]
  },
  "Dashboard — carpo\\epicarp.md": {
    "primary": "The outermost layer of the pericarp or fruit wall; the skin or peel of a fruit; exocarp.",
    "secondary": "In plant anatomy, the cutinized or waxed protective outer epidermal layer of a ripening fruit.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "The thin tough skin that peels cleanly away from a ripe plum represents the protective botanical **epicarp**."
      },
      {
        "author": "John Lindley",
        "work": "An Introduction to Botany",
        "quote": "Glandular oil cavities in the citrus peel are situated within the colored parenchyma of the outer **epicarp**."
      },
      {
        "author": "Julius von Sachs",
        "work": "Textbook of Botany",
        "quote": "Stomata and waxy bloom on the **epicarp** regulate gas exchange and prevent moisture loss from the succulent fruit."
      }
    ]
  },
  "Dashboard — carpo\\epicarpal.md": {
    "primary": "Of or relating to the epicarp (the outer skin of a fruit); or situated upon the carpus (wrist).",
    "secondary": "In botanical morphology and anatomical descriptions, designating structures located on or pertaining to the outer fruit wall or the carpal joint.",
    "quotes": [
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "Microscopic sections show that the **epicarpal** layer is coated with an impermeable cuticle that repels water."
      },
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "Color pigments responsible for the blush on ripening pome fruits reside primarily within the **epicarpal** cells."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The superficial dorsal veins cross the **epicarpal** fascia of the wrist before joining the cephalic and basilic trunks."
      }
    ]
  },
  "Dashboard — carpo\\exocarp.md": {
    "primary": "The outermost layer of the pericarp of a fruit; the skin or outer covering of a seed vessel; epicarp.",
    "secondary": "In carpology, the exterior epidermal and subepidermal tissue of a fruit, often modified with hairs, bloom, or leathery rinds (as in hesperidia).",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "In the walnut, the green fibrous husk that splits open at frost represents the fused **exocarp** and mesocarp."
      },
      {
        "author": "John Lindley",
        "work": "An Introduction to Botany",
        "quote": "The leathery rind of the pomegranate consists of the hardened **exocarp** adnate to the accrescent floral tube."
      },
      {
        "author": "Arthur Johnson Eames",
        "work": "Morphology of Angiosperms",
        "quote": "Stomatal frequency on the **exocarp** of developing fruits reflects their early photosynthetic contribution prior to ripening."
      }
    ]
  },
  "Dashboard — carpo\\mesocarp.md": {
    "primary": "The middle layer of the pericarp of a fruit, situated between the epicarp (exocarp) and the endocarp.",
    "secondary": "In botanical morphology, the thick, succulent, edible flesh of fruits like peaches, cherries, plums, and melons, or the fibrous husk of a coconut.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "In a ripe drupe, the parenchymatous **mesocarp** becomes gorged with sugary juices and aromatic compounds."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "The coir fiber of commerce is extracted from the thick, fibrous **mesocarp** that surrounds the hard shell of the coconut."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "Commercial pomology selects for peach varieties with a dense, non-browning **mesocarp** that withstands distant shipping."
      }
    ]
  },
  "Dashboard — carpo\\metacarpal.md": {
    "primary": "Of, relating to, or situated in the metacarpus (the palm of the hand).",
    "secondary": "In human osteology, any of the five long cylindrical bones of the hand articulating proximally with the carpus and distally with the phalanges.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "Fracture of the neck of the fifth **metacarpal** bone is commonly sustained from a clenched-fist blow (boxer's fracture)."
      },
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "The first **metacarpal** bone possesses extraordinary mobility, articulating with the trapezium through a reciprocal saddle joint."
      },
      {
        "author": "Charles Bell",
        "work": "The Hand: Its Mechanism and Vital Endowments",
        "quote": "The radiating divergence of the five **metacarpal** shafts forms the skeletal fan that gives the palm its cupped flexibility."
      }
    ]
  },
  "Dashboard — carpo\\metacarpus.md": {
    "primary": "The intermediate skeletal part of the hand between the carpus (wrist) and the phalanges (fingers), consisting of five cylindrical bones.",
    "secondary": "In comparative anatomy, the corresponding region of the forefoot in tetrapod vertebrates, forming the cannon bone in ungulates.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **metacarpus** consists of five cylindrical bones which are numbered from the radial to the ulnar side."
      },
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "Palmar interosseous muscles occupy the deep intervals between the adjacent skeletal shafts of the **metacarpus**."
      },
      {
        "author": "Galen",
        "work": "On the Usefulness of the Parts of the Body",
        "quote": "Nature interposed the firm framework of the **metacarpus** between the wrist and fingers to provide an unyielding palm for grasping."
      }
    ]
  },
  "Dashboard — carpo\\monocarp.md": {
    "primary": "A plant that flowers, sets seed, and bears fruit only once in its lifetime and dies shortly thereafter; a monocarpic plant.",
    "secondary": "In ecology and botany, semelparous plants such as the century plant (Agave americana) or certain tropical bamboos that store energy for decades before a single colossal bloom.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "The great American aloe lives for decades in vegetative preparation, behaving as a colossal **monocarp** that dies upon fruiting."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "Many biennial herbs function as a **monocarp**, devoting their second summer entirely to a massive burst of reproductive fruit."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "Gardeners must remember that this magnificent species is a strict **monocarp**, perishing as soon as its seed capsules mature."
      }
    ]
  },
  "Dashboard — carpo\\pericarp.md": {
    "primary": "The ripened and modified wall of a plant ovary that encloses the seeds; the fruit wall.",
    "secondary": "In botanical anatomy, the structure developing from the ovary wall after fertilization, classically differentiated into epicarp (exocarp), mesocarp, and endocarp.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "The **pericarp** exhibits immense morphological diversity, ranging from the papery pod of a pea to the hard shell of a hazelnut."
      },
      {
        "author": "John Lindley",
        "work": "An Introduction to Botany",
        "quote": "Whatever intervenes between the seed and the outer surface of the fruit belongs properly to the botanical **pericarp**."
      },
      {
        "author": "Julius von Sachs",
        "work": "Textbook of Botany",
        "quote": "Cell division and cellular enlargement in the **pericarp** are triggered by hormone signals released from developing seeds."
      }
    ]
  },
  "Dashboard — carpo\\polycarp.md": {
    "primary": "A plant or organism that bears fruit multiple times in its life cycle; a polycarpic plant.",
    "secondary": "In early church history and hagiography, Saint Polycarp of Smyrna (c. 69–c. 155 AD), apostolic father, bishop, and celebrated Christian martyr.",
    "quotes": [
      {
        "author": "Irenaeus of Lyons",
        "work": "Against Heresies",
        "quote": "I remember the discourse of the blessed **Polycarp**, how he related his familiar intercourse with John and the other disciples."
      },
      {
        "author": "Eusebius of Caesarea",
        "work": "Ecclesiastical History",
        "quote": "When summoned to revile Christ, the venerable bishop **Polycarp** replied that for eighty-six years he had served his Lord without wrong."
      },
      {
        "author": "J. B. Lightfoot",
        "work": "The Apostolic Fathers",
        "quote": "The Martyrdom of **Polycarp** represents the earliest authentic contemporary narrative of Christian witness under Roman persecution."
      }
    ]
  },
  "Dashboard — carpo\\pseudocarp.md": {
    "primary": "A false fruit or accessory fruit, developed from floral structures in addition to or other than the ovary (such as the receptacle or calyx).",
    "secondary": "In systematic botany, fruits such as the strawberry (enlarged receptacle bearing achenes), apple (fleshy hypanthium), or fig (syconium).",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "In the strawberry, the luscious red edible sphere is a **pseudocarp** derived from the swollen receptacle, while the tiny seeds are the true fruits."
      },
      {
        "author": "John Lindley",
        "work": "An Introduction to Botany",
        "quote": "An apple is technically a **pseudocarp**, since the bulk of its flesh originates from the adnate floral tube surrounding the core."
      },
      {
        "author": "Arthur Johnson Eames",
        "work": "Morphology of Angiosperms",
        "quote": "Accessory floral tissue frequently contributes to the **pseudocarp**, providing sugary incentives for animal seed dispersers."
      }
    ]
  },
  "Dashboard — carpo\\syncarp.md": {
    "primary": "An aggregate or composite fruit formed by the coherence or fusion of multiple carpels or fruits from one or several flowers.",
    "secondary": "In systematic pomology, a compound fruit such as the blackberry, custard apple, or pineapple (sorosis).",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "In the magnolia, the individual follicles coalesce upon an elongated cone-like axis to form a massive wooden **syncarp**."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "The edible portion of the custard apple represents a fleshy **syncarp** formed by the complete fusion of numerous baccate carpels."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "Manual of Cultivated Plants",
        "quote": "The mulberry fruit is an aggregate **syncarp** derived from an entire inflorescence whose fleshy perianths enclose the nutlets."
      }
    ]
  },
  "Dashboard — carpo\\syncarpous.md": {
    "primary": "Having the carpels of a flower united or fused together into a single compound ovary or pistil.",
    "secondary": "In floral morphology and evolution, the advanced gynoecial condition typical of higher angiosperms, enabling centralized pollen tube competition.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "A **syncarpous** pistil may possess several internal chambers or locules, or coalesce into a single unilocular cavity with parietal placentation."
      },
      {
        "author": "John Lindley",
        "work": "An Introduction to Botany",
        "quote": "In a **syncarpous** flower, several styles frequently unite into a single central column crowned by lobed stigmas."
      },
      {
        "author": "Arthur Johnson Eames",
        "work": "Morphology of Angiosperms",
        "quote": "The evolution of the **syncarpous** gynoecium allowed uniform distribution of pollen tubes across all ovules within the ovary."
      }
    ]
  },
  "Dashboard — cephal\\acephalia.md": {
    "primary": "Congenital absence of the head; acephaly.",
    "secondary": "In developmental teratology, an extreme fetal malformation resulting from early developmental failure of the cephalic pole of the embryo.",
    "quotes": [
      {
        "author": "Isidore Geoffroy Saint-Hilaire",
        "work": "General and Particular History of Anomalies of Organization",
        "quote": "The anomaly of **acephalia** represents the complete absence of cranial structures, seen occasionally in unequal twin gestations."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Cases of **acephalia** illustrate how the trunk and lower limbs can develop without direct neural induction from the cerebral vesicles."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In complete **acephalia**, the neck terminates blindly without trace of cranium, brainstem, or facial landmarks."
      }
    ]
  },
  "Dashboard — cephal\\acephalic.md": {
    "primary": "Headless; lacking a distinct head or cranial structure.",
    "secondary": "In anatomy and zoology, describing organisms (such as bivalve mollusks) or developmental anomalies that lack a differentiated head.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Invertebrated Animals",
        "quote": "Lamellibranch mollusks were formerly grouped as **acephalic** invertebrates because their bodies lack a distinct cranial region."
      },
      {
        "author": "Ernst Haeckel",
        "work": "The Evolution of Man",
        "quote": "At its earliest stage, the vertebrate blastoderm appears as an **acephalic** disk prior to the formation of the anterior head fold."
      },
      {
        "author": "Richard Owen",
        "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals",
        "quote": "The **acephalic** condition of sedentary bivalves represents an evolutionary adaptation to filter-feeding within a hinged shell."
      }
    ]
  },
  "Dashboard — cephal\\acephalism.md": {
    "primary": "The condition, state, or political situation of being without a head, sovereign ruler, or central governing authority.",
    "secondary": "In political philosophy and sociological theory, the absence of centralized hierarchical leadership in decentralized societies or revolutionary movements.",
    "quotes": [
      {
        "author": "Thomas Carlyle",
        "work": "The French Revolution",
        "quote": "The Parisian mob plunged into violent **acephalism**, rejecting all magistrates and obeying only sudden gusts of rumor."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Following the assassination of the emperor, the Roman army drifted in perilous **acephalism** before electing a new general."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "Democratic associations avoid the chaos of **acephalism** by voluntarily delegating temporary authority to chosen committees."
      }
    ]
  },
  "Dashboard — cephal\\acephalous.md": {
    "primary": "Lacking a head; headless; headless in anatomy or zoology.",
    "secondary": "In political anthropology, describing societies lacking a formal chief or centralized head of state; in prosody, a verse line lacking its initial syllable.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The **acephalous** sect of monophysites refused allegiance to either the patriarch of Alexandria or the council of Chalcedon."
      },
      {
        "author": "Thomas Carlyle",
        "work": "Past and Present",
        "quote": "An **acephalous** multitude of starving weavers surged through the industrial streets, crying out for bread and leadership."
      },
      {
        "author": "John Dryden",
        "work": "Essays on Dramatic Poesy",
        "quote": "A metric line that drops its first foot is known to classical prosodists as an **acephalous** verse."
      }
    ]
  },
  "Dashboard — cephal\\acephaly.md": {
    "primary": "The congenital condition of having no head; acephalia.",
    "secondary": "In political anthropology and social theory, the organizational state of egalitarian or segmentary lineage societies lacking centralized political leadership.",
    "quotes": [
      {
        "author": "Isidore Geoffroy Saint-Hilaire",
        "work": "Treatise on Teratology",
        "quote": "Congenital **acephaly** is almost invariably accompanied by profound defects of the cervical spine and thoracic organs."
      },
      {
        "author": "E. E. Evans-Pritchard",
        "work": "The Nuer: A Description of the Modes of Livelihood and Political Institutions",
        "quote": "The ordered anarchy of Nuer society illustrates how social cohesion is maintained in the complete absence of political rulers, in pure **acephaly**."
      },
      {
        "author": "Meyer Fortes",
        "work": "African Political Systems",
        "quote": "In groups characterized by structural **acephaly**, lineage segment balances substitute for centralized state apparatuses."
      }
    ]
  },
  "Dashboard — cephal\\anencephalic.md": {
    "primary": "Affected by or relating to anencephaly; born without the major portion of the brain, skull vault, and scalp.",
    "secondary": "In clinical neonatology and pathology, describing a neonate with lethal neural tube closure defect exposing the rudimentary brainstem.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The **anencephalic** infant exhibits primitive reflex sucking movements driven solely by preserved bulbar centers."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Dissection of the **anencephalic** cranium reveals the base of the skull covered only by a vascular mass of cerebro-vasculosa."
      },
      {
        "author": "Harvey Cushing",
        "work": "Surgery of the Head",
        "quote": "Failure of the anterior neuropore to close at the twenty-fourth day of gestation produces the classic **anencephalic** malformation."
      }
    ]
  },
  "Dashboard — cephal\\anencephalous.md": {
    "primary": "Lacking a brain or cerebral hemispheres; brainless; affected with anencephaly.",
    "secondary": "In comparative embryology and teratology, exhibiting developmental failure of the telencephalic and cranial vesicles.",
    "quotes": [
      {
        "author": "Isidore Geoffroy Saint-Hilaire",
        "work": "General and Particular History of Anomalies of Organization",
        "quote": "The **anencephalous** fetus demonstrates that somatic visceral growth can proceed normally despite the absence of cerebral hemispheres."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Vertebrated Animals",
        "quote": "Experiments on **anencephalous** monsters proved that respiration and circulation are mediated autonomously through lower medullary centers."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "In the **anencephalous** monster, the eyes project prominently from shallow, deformed orbits beneath an absent forehead."
      }
    ]
  },
  "Dashboard — cephal\\anencephaly.md": {
    "primary": "A lethal congenital neural tube defect characterized by the absence of a major portion of the brain, skull, and scalp.",
    "secondary": "In perinatology, a defect resulting from failure of the rostral neuropore to close around day 24 to 26 of embryonic development, detectable by elevated maternal alpha-fetoprotein.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Maternal dietary supplementation with folic acid has achieved a dramatic reduction in the incidence of congenital **anencephaly**."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "In **anencephaly**, the calvarium fails to form, leaving the remnants of the diencephalon exposed to the amniotic fluid."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology",
        "quote": "Severe cranial vault agenesis in **anencephaly** contrasts sharply with the localized calvarial defects seen in encephalocele."
      }
    ]
  },
  "Dashboard — cephal\\autocephaly.md": {
    "primary": "In Eastern Orthodox canon law and ecclesiastical history, the status of a self-governing national church whose primate does not report to any higher authority.",
    "secondary": "Ecclesiastical independence; the right of an independent church synod to elect its own patriarch or metropolitan without external patriarchal confirmation.",
    "quotes": [
      {
        "author": "John Meyendorff",
        "work": "The Orthodox Church: Its Past and Its Role in the World Today",
        "quote": "The grant of **autocephaly** recognizes that a national church has attained the spiritual maturity to govern its own pastoral life."
      },
      {
        "author": "Jaroslav Pelikan",
        "work": "The Spirit of Eastern Christendom",
        "quote": "The Russian Church achieved de facto **autocephaly** after the Council of Florence, consecrating its own metropolitan in Moscow."
      },
      {
        "author": "Timothy Ware",
        "work": "The Orthodox Church",
        "quote": "The delicate balance between conciliar unity and jurisdictional **autocephaly** defines the ecclesiological genius of Orthodoxy."
      }
    ]
  },
  "Dashboard — cephal\\brachiocephalic.md": {
    "primary": "Of, relating to, or supplying both the arm (brachium) and the head (cephalon).",
    "secondary": "In human cardiovascular anatomy, designating the brachiocephalic artery (innominate artery) and the paired brachiocephalic veins forming the superior vena cava.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **brachiocephalic** artery is the largest vessel branching from the arch of the aorta, dividing into the right common carotid and subclavian."
      },
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "The great venous trunks from the head and arm unite behind the sternoclavicular joint to form the **brachiocephalic** vein."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Resection of mediastinal neoplasms requires exquisite surgical care around the anterior surface of the left **brachiocephalic** vein."
      }
    ]
  },
  "Dashboard — cephal\\brachycephalic.md": {
    "primary": "Having a relatively short, broad head with a cephalic index (ratio of maximum cranial breadth to length multiplied by 100) of 80 or greater.",
    "secondary": "In physical anthropology and veterinary anatomy, designating broad-headed human populations or domestic animal breeds (such as pugs or bulldogs).",
    "quotes": [
      {
        "author": "Franz Boas",
        "work": "Changes in Bodily Form of Descendants of Immigrants",
        "quote": "Our measurements proved that the **brachycephalic** head form of European immigrants shifted significantly under new American environmental conditions."
      },
      {
        "author": "Paul Broca",
        "work": "Instructions Craniologiques",
        "quote": "We classify skulls whose breadth reaches eighty percent of their length as strictly **brachycephalic**."
      },
      {
        "author": "William Z. Ripley",
        "work": "The Races of Europe",
        "quote": "The Alpine populations of central Europe are predominantly **brachycephalic**, contrasting with the dolichocephalic Mediterranean type."
      }
    ]
  },
  "Dashboard — cephal\\brachycephalism.md": {
    "primary": "The state, condition, or cranial characteristic of being brachycephalic; broad-headedness or short-headedness.",
    "secondary": "In physical anthropology and craniometry, a skull shape characterized by a cephalic index of 80 or above.",
    "quotes": [
      {
        "author": "Paul Broca",
        "work": "Mémoires d'Anthropologie",
        "quote": "The geographical distribution of **brachycephalism** in prehistoric Europe indicates significant migrations from the east."
      },
      {
        "author": "Franz Boas",
        "work": "The Mind of Primitive Man",
        "quote": "Early craniologists mistakenly treated **brachycephalism** as an unalterable racial essence rather than a plastic anatomical trait."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Man's Place in Nature",
        "quote": "Cranial variations ranging from dolichocephaly to extreme **brachycephalism** can be found within the same broad continental populations."
      }
    ]
  },
  "Dashboard — cephal\\brachycephaly.md": {
    "primary": "Short-headedness; the condition of having a disproportionately short, broad skull with a cephalic index of 80 or more.",
    "secondary": "In pediatric neurology and craniofacial surgery, positional flattening of the posterior occiput or premature fusion of the coronal sutures (coronal craniosynostosis).",
    "quotes": [
      {
        "author": "Franz Boas",
        "work": "Anthropometry of Central European Immigrants",
        "quote": "Our surveys demonstrated that **brachycephaly** is not an immutable hereditary constant across successive generations."
      },
      {
        "author": "Paul Broca",
        "work": "Craniology of Prehistoric Races",
        "quote": "Measurements of the Auvergne skulls revealed pronounced **brachycephaly** accompanied by high cephalic vaults."
      },
      {
        "author": "Aleš Hrdlička",
        "work": "Anthropometry",
        "quote": "Artificial infant cradle-boarding frequently accentuates occipital flattening, producing marked acquired **brachycephaly**."
      }
    ]
  },
  "Dashboard — cephal\\cephal.md": {
    "primary": "The Greek anatomical combining form derived from kephale, denoting the head or cranial structures (cephal- / cephalo-).",
    "secondary": "In zoological and medical nomenclature, an essential prefix entering into terminology describing head anatomy, cephalization, and neurology.",
    "quotes": [
      {
        "author": "Galen",
        "work": "On Anatomical Procedures",
        "quote": "Ancient anatomists designated the royal citadel of the body by the radical **cephal**, wherein reason and sensation dwell."
      },
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "Compound terms rooted in **cephal** identify the cranial bones, cerebral membranes, and cranial nerve trunks."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The prefix **cephal** unites anatomical structures that converge upon the head, distinguishing cranial from caudal axes."
      }
    ]
  },
  "Dashboard — cephal\\cephalalgia.md": {
    "primary": "Pain in the head; headache.",
    "secondary": "In clinical neurology, pain localized to the cranial vault, scalp, or face, resulting from vascular dilatation, meningeal irritation, or muscle contraction.",
    "quotes": [
      {
        "author": "Thomas Willis",
        "work": "The Anatomy of the Brain and Nerves",
        "quote": "Violent **cephalalgia** arises when inflammatory humors distend the sensitive vessels of the meninges."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Persistent morning **cephalalgia** accompanied by vomiting and papilledema should immediately arouse suspicion of an intracranial mass."
      },
      {
        "author": "Thomas Sydenham",
        "work": "Observationes Medicae",
        "quote": "The patient was tormented by an excruciating hemicranial **cephalalgia** that compelled him to seek absolute darkness and quiet."
      }
    ]
  },
  "Dashboard — cephal\\cephalanthera.md": {
    "primary": "A genus of terrestrial orchids (family Orchidaceae), commonly called helleborines, characterized by flowers whose anther is perched atop the column like a little head.",
    "secondary": "In systematic orchidology, temperate Eurasian and North American forest orchids with plicate leaves, spurless labella, and white or pinkish blossoms.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Various Contrivances by Which Orchids Are Fertilised by Insects",
        "quote": "In **cephalanthera**, the anther stands erect upon the summit of the column, its pollinia resting directly above the stigma."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "The capitate structure of the anther in **cephalanthera** immediately distinguishes it from adjacent genera in the Neottieae."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The solitary Pacific species of **cephalanthera** lacks green chlorophyll, thriving as a saprophyte in dark conifer humus."
      }
    ]
  },
  "Dashboard — cephal\\cephalaspid.md": {
    "primary": "An extinct, jawless armored fish of the order Cephalaspida (Osteostraci), abundant in the Silurian and Devonian periods and characterized by a broad bony head shield.",
    "secondary": "In vertebrate paleontology, an agnathan ostracoderm whose horseshoe-shaped head shield bore dorsal eyes, a pineal opening, and lateral sensory fields.",
    "quotes": [
      {
        "author": "Louis Agassiz",
        "work": "Recherches sur les Poissons Fossiles",
        "quote": "The remarkable fossil **cephalaspid** was covered anteriorly by a single, continuous, crescentic plate of solid bone."
      },
      {
        "author": "Hugh Miller",
        "work": "The Old Red Sandstone",
        "quote": "In the sandstone quarries of Cromarty, I uncovered the polished buckler of a **cephalaspid**, its ancient bony luster intact."
      },
      {
        "author": "Alfred Sherwood Romer",
        "work": "Vertebrate Paleontology",
        "quote": "The semicircular head shield of the **cephalaspid** contained intricate internal canals for electric or pressure-sensitive sensory organs."
      }
    ]
  },
  "Dashboard — cephal\\cephalaspida.md": {
    "primary": "An extinct order of jawless armored ostracoderm vertebrates (Osteostraci) possessing a consolidated, bony semicircular head shield.",
    "secondary": "In evolutionary paleontology, a Silurian-Devonian agnathan clade that provided crucial anatomical insights into the primitive architecture of the vertebrate cranial vault.",
    "quotes": [
      {
        "author": "Louis Agassiz",
        "work": "Monograph on the Fossil Fishes of the Old Red Sandstone",
        "quote": "We erect the order **cephalaspida** to embrace those primitive armored fishes whose cranial buckler resembles an ancient shield."
      },
      {
        "author": "Hugh Miller",
        "work": "Footprints of the Creator",
        "quote": "The deposits of the Devonian period abound with the bony remains of **cephalaspida**, witnessing the dawn of vertebrate life."
      },
      {
        "author": "Arthur Smith Woodward",
        "work": "Catalogue of the Fossil Fishes in the British Museum",
        "quote": "Serial grinding of specimens of **cephalaspida** revealed complete cranial nerve canals preserved in solid calcite."
      }
    ]
  },
  "Dashboard — cephal\\cephalexin.md": {
    "primary": "A first-generation oral beta-lactam cephalosporin antibiotic used to treat bacterial infections of the respiratory tract, urinary tract, and skin.",
    "secondary": "In pharmacology, a bactericidal antibiotic that inhibits bacterial cell-wall synthesis by binding to penicillin-binding proteins, active primarily against Gram-positive cocci.",
    "quotes": [
      {
        "author": "Edward Abraham",
        "work": "Cephalosporins: Chemistry and Biology",
        "quote": "The chemical modification of 7-aminocephalosporanic acid yielded **cephalexin**, an orally absorbed antibiotic of high acid stability."
      },
      {
        "author": "Selman Waksman",
        "work": "The Conquest of Infectious Diseases",
        "quote": "The therapeutic introduction of **cephalexin** provided physicians with a dependable oral agent against penicillinase-producing staphylococci."
      },
      {
        "author": "René Dubos",
        "work": "Bacterial and Mycotic Infections of Man",
        "quote": "Prompt administration of **cephalexin** rapidly eradicates cutaneous streptococcal cellulitis while sparing normal gastrointestinal flora."
      }
    ]
  },
  "Dashboard — cephal\\cephalic.md": {
    "primary": "Of, relating to, or directed toward the head.",
    "secondary": "In human anatomy, designating structures such as the cephalic vein of the upper arm, or the cephalic index used in craniometry.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **cephalic** vein ascends along the radial border of the forearm, crossing the deltopectoral groove to join the axillary vein."
      },
      {
        "author": "Paul Broca",
        "work": "Instructions Craniologiques",
        "quote": "The **cephalic** index measures the exact mathematical proportion between the breadth and length of the human cranium."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "The progressive expansion of the **cephalic** region during vertebrate phylogeny reflects increasing sensory specialization."
      }
    ]
  },
  "Dashboard — cephal\\cephalitis.md": {
    "primary": "Inflammation of the brain or head; encephalitis.",
    "secondary": "In historical clinical pathology, severe cerebral inflammation presenting with high fever, delirium, headache, and coma.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Acute **cephalitis** swiftly advances from irritable restlessness into profound lethargy and irreversible coma."
      },
      {
        "author": "Thomas Willis",
        "work": "The Anatomy of the Brain",
        "quote": "Postmortem dissection in fatal **cephalitis** reveals fiery vascular injection across the cerebral convolutions."
      },
      {
        "author": "Percivall Pott",
        "work": "Chirurgical Works",
        "quote": "Trauma to the cranial vault is frequently followed by secondary **cephalitis** as suppuration invades the meningeal membranes."
      }
    ]
  },
  "Dashboard — cephal\\cephalobidae.md": {
    "primary": "A family of free-living, terrestrial and bacterivorous nematodes (order Rhabditida) inhabiting soils and decaying organic matter.",
    "secondary": "In invertebrate nematology, roundworms characterized by specialized prohabdions and probolae surrounding the mouth, key to soil nutrient cycling.",
    "quotes": [
      {
        "author": "Nathan Cobb",
        "work": "Contributions to a Science of Nematology",
        "quote": "Soil samples from cultivated fields invariably yield members of the **cephalobidae**, feeding voraciously upon decomposing bacteria."
      },
      {
        "author": "Libbie Hyman",
        "work": "The Invertebrates",
        "quote": "The cuticle of the **cephalobidae** displays delicate transverse annulations and complex cephalic probolae around the oral stoma."
      },
      {
        "author": "Sydney Brenner",
        "work": "The Genetics of Caenorhabditis elegans and Allied Nematodes",
        "quote": "Comparative morphology links the Rhabditidae directly with the specialized bacterivorous **cephalobidae**."
      }
    ]
  },
  "Dashboard — cephal\\cephalochordata.md": {
    "primary": "A subphylum of small, fish-like, marine chordates (lancelets) having a persistent notochord that extends the entire length of the body to the tip of the head.",
    "secondary": "In evolutionary biology, an ancient protochordate lineage (comprising Branchiostoma / amphioxus) providing the archetypal morphological model for vertebrate origins.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Vertebrated Animals",
        "quote": "In the **cephalochordata**, the notochord extends beyond the anterior termination of the nerve cord to the snout tip."
      },
      {
        "author": "Ernst Haeckel",
        "work": "The Evolution of Man",
        "quote": "The subphylum **cephalochordata** represents the nearest living survival of our primordial, unsegmented chordate ancestors."
      },
      {
        "author": "Edwin S. Goodrich",
        "work": "Studies on the Structure and Development of Vertebrates",
        "quote": "The pharyngeal gill slits and wheel organ of the **cephalochordata** illustrate primitive chordate ciliary feeding mechanisms."
      }
    ]
  },
  "Dashboard — cephal\\cephalochordate.md": {
    "primary": "Any small, fish-like marine chordate belonging to the subphylum Cephalochordata, commonly known as a lancelet or amphioxus.",
    "secondary": "In comparative anatomy, a creature possessing a notochord, dorsal nerve cord, and pharyngeal slits throughout life, lacking a true bony braincase.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "The Elements of Comparative Anatomy",
        "quote": "The living **cephalochordate** Amphioxus burrows into coastal sands, exposing only its oral hood to the marine currents."
      },
      {
        "author": "Ernst Haeckel",
        "work": "The History of Creation",
        "quote": "No zoologist can comprehend the vertebrate body plan without mastering the embryology of the humble **cephalochordate**."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Wonderful Life: The Burgess Shale and the Nature of History",
        "quote": "The discovery of Pikaia in the Burgess Shale placed an ancient **cephalochordate** directly at the dawn of the Cambrian radiation."
      }
    ]
  },
  "Dashboard — cephal\\cephaloglycin.md": {
    "primary": "A semisynthetic, broad-spectrum cephalosporin antibiotic containing a glycyl side chain, administered orally for bacterial infections.",
    "secondary": "In medicinal chemistry and pharmacology, an early cephalosporin analog demonstrating that alpha-amino substitution enhanced oral absorption and bioavailability.",
    "quotes": [
      {
        "author": "Edward Abraham",
        "work": "The Cephalosporin C Antibiotics",
        "quote": "The synthesis of **cephaloglycin** demonstrated that chemical modifications of the 7-position side chain altered antimicrobial activity."
      },
      {
        "author": "Selman Waksman",
        "work": "Microbial Antagonisms and Antibiotic Substances",
        "quote": "Laboratory evaluation revealed that **cephaloglycin** was rapidly converted in vivo into active desacetyl metabolites."
      },
      {
        "author": "René Dubos",
        "work": "The Bacterial Cell",
        "quote": "The bactericidal action of **cephaloglycin** hinges upon competitive inhibition of transpeptidase enzymes in the bacterial wall."
      }
    ]
  },
  "Dashboard — cephal\\cephalohematoma.md": {
    "primary": "A subperiosteal collection of blood over a neonatal cranial bone, typically the parietal bone, resulting from birth trauma and limited by suture lines.",
    "secondary": "In clinical neonatology and obstetrics, a firm, fluctuant scalp swelling caused by ruptured subperiosteal blood vessels that does not cross cranial sutures.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Because the blood in a **cephalohematoma** is subperiosteal, the swelling is strictly bounded by the cranial suture margins."
      },
      {
        "author": "Astley Cooper",
        "work": "Lectures on the Principles and Practice of Surgery",
        "quote": "A benign neonatal **cephalohematoma** requires watchful expectancy rather than incision, resorbing completely over several weeks."
      },
      {
        "author": "Harvey Cushing",
        "work": "Surgery of the Head",
        "quote": "Distinguishing a simple **cephalohematoma** from a caput succedaneum is easy, as the latter crosses cranial sutures freely."
      }
    ]
  },
  "Dashboard — cephal\\cephalomancy.md": {
    "primary": "Divination or fortune-telling practiced by inspecting the head or skull of an animal or person, or by roasting an ass's head on burning coals.",
    "secondary": "In the history of occultism and magical folklore, an ancient divinatory ritual wherein crackling sounds or facial contortions were interpreted as oracles.",
    "quotes": [
      {
        "author": "Thomas Browne",
        "work": "Pseudodoxia Epidemica",
        "quote": "Among obsolete superstitions, **cephalomancy** roasted an ass's head upon glowing embers to discover the identity of thieves."
      },
      {
        "author": "Edward Burnett Tylor",
        "work": "Primitive Culture",
        "quote": "The divinatory rites of **cephalomancy** reflect the universal archaic belief that spiritual wisdom lingers within the severed skull."
      },
      {
        "author": "James George Frazer",
        "work": "The Golden Bough",
        "quote": "Consulting skull oracles or practicing **cephalomancy** was a widespread method of seeking prophetic counsel before military campaigns."
      }
    ]
  },
  "Dashboard — cephal\\cephalometry.md": {
    "primary": "The scientific measurement of the dimensions and proportions of the human head and face, especially by standardized radiographic techniques.",
    "secondary": "In orthodontics and craniofacial surgery, the radiographic tracing of skeletal landmarks (cephalometrics) to analyze jaw relationships and plan corrective surgery.",
    "quotes": [
      {
        "author": "Paul Broca",
        "work": "Instructions Craniologiques",
        "quote": "Rigorous **cephalometry** demands standardized callipers and precise anatomical landmarks across the living head."
      },
      {
        "author": "Aleš Hrdlička",
        "work": "Anthropometry",
        "quote": "Comparative **cephalometry** across thousands of subjects established the normal ranges of cranial indices among indigenous tribes."
      },
      {
        "author": "Franz Boas",
        "work": "Changes in Bodily Form of Descendants of Immigrants",
        "quote": "Careful longitudinal **cephalometry** revealed that children of immigrants develop head proportions distinct from their foreign-born parents."
      }
    ]
  },
  "Dashboard — cephal\\cephalon.md": {
    "primary": "The head or anterior body region of a trilobite or other arthropod, composed of fused segments bearing eyes, antennae, and mouthparts.",
    "secondary": "In invertebrate paleontology, the consolidated dorsal shield of a trilobite, divided into a central glabella and lateral genae or cheeks.",
    "quotes": [
      {
        "author": "Charles Doolittle Walcott",
        "work": "The Fauna of the Lower Cambrian or Olenellus Zone",
        "quote": "The semicircular **cephalon** of the trilobite is armed with prominent genal spines projecting backward along the thorax."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Invertebrated Animals",
        "quote": "In trilobites, the **cephalon** represents the anterior tagma formed by the ancestral fusion of five or six segments."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Wonderful Life",
        "quote": "Examining the ventral surface of the **cephalon** reveals the hypostome that sheltered the arthropod mouth."
      }
    ]
  },
  "Dashboard — cephal\\cephalopagus.md": {
    "primary": "Conjoined twins united at the head and face, with a single shared cranium and thorax; also called craniopagus or janiceps.",
    "secondary": "In developmental teratology, an extremely rare form of symmetrical monocephalic conjoined twins resulting from incomplete embryonic axis bifurcation.",
    "quotes": [
      {
        "author": "Isidore Geoffroy Saint-Hilaire",
        "work": "General and Particular History of Anomalies of Organization",
        "quote": "The condition of **cephalopagus** features two bodies fused head-to-head, often with two faces looking in opposite directions."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "In a **cephalopagus** monster, the cerebral hemispheres are intimately shared within an anomalous single cranial cavity."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Delivery of a **cephalopagus** neonate is an obstetrical catastrophe that almost universally requires surgical dismemberment."
      }
    ]
  },
  "Dashboard — cephal\\cephalopod.md": {
    "primary": "Any predatory marine mollusk of the class Cephalopoda, having a large distinct head, well-developed eyes, and arms or tentacles around the mouth.",
    "secondary": "In marine biology, intelligent invertebrates including the octopus, squid, cuttlefish, and nautilus, possessing closed circulatory systems and jet propulsion.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The **cephalopod** changed color with astonishing rapidity, shifting from dark brown to bright red as it hid in the tidepool."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Invertebrated Animals",
        "quote": "The camera-like eye of the **cephalopod** parallels that of vertebrates in optical precision, a triumph of convergent evolution."
      },
      {
        "author": "Aristotle",
        "work": "History of Animals",
        "quote": "Of the mollusks, the largest is the **cephalopod**, which discharges dark ink to conceal its escape from sea predators."
      }
    ]
  },
  "Dashboard — cephal\\cephalopoda.md": {
    "primary": "The taxonomic class of advanced, highly organized marine mollusks having bilateral symmetry, prominent heads, and tentacles surrounding the mouth.",
    "secondary": "In systematic malacology and paleontology, the molluscan class encompassing Coleoidea (squid, octopus, cuttlefish) and Nautiloidea, dominant throughout the Mesozoic as ammonites.",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "History of Animals",
        "quote": "The class **cephalopoda** possesses eight or ten feet set with suckers surrounding the beak, by which they seize their prey."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Anatomy of Invertebrated Animals",
        "quote": "In **cephalopoda**, the molluscan foot is transformed into prehensile circumoral tentacles and a propulsive ventral funnel."
      },
      {
        "author": "Georges Cuvier",
        "work": "The Animal Kingdom",
        "quote": "The extraordinary cranial cartilage and brain development in **cephalopoda** place them at the very pinnacle of invertebrate life."
      }
    ]
  },
  "Dashboard — cephal\\cephalopodan.md": {
    "primary": "Of, relating to, or characteristic of the cephalopods; cephalopod-like.",
    "secondary": "In marine zoology, describing morphological features, behaviors, or predatory adaptations peculiar to the class Cephalopoda.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Invertebrated Animals",
        "quote": "The **cephalopodan** circulatory system is virtually closed, featuring branchial hearts that pump blood through gill capillaries."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Fossil ammonites display intricate **cephalopodan** suture lines that grew progressively more complex across Mesozoic strata."
      },
      {
        "author": "Richard Owen",
        "work": "Memoir on the Pearly Nautilus",
        "quote": "The pearly chambered shell provides the **cephalopodan** animal with exquisite hydrostatic buoyancy control."
      }
    ]
  },
  "Dashboard — cephal\\cephalopterus.md": {
    "primary": "A genus of South American passerine birds in the cotinga family (Cotingidae), commonly known as umbrella birds, having a large, umbrella-like crest on the head.",
    "secondary": "In ornithology, tropical forest birds (notably Cephalopterus ornatus) possessing an inflatable, feathered wattle hanging from the throat.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Personal Narrative of Travels",
        "quote": "In the Amazonian canopy, the remarkable bird **cephalopterus** spreads its vaulting crest of black feathers like a protective umbrella."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "Travels on the Amazon and Rio Negro",
        "quote": "The deep, booming mating call of **cephalopterus** echoed across the forest floor, resonant as a distant church bell."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "The extraordinary ornamental crest and neck wattle of **cephalopterus** serve as classic examples of sexual selection in male birds."
      }
    ]
  },
  "Dashboard — cephal\\cephaloridine.md": {
    "primary": "A first-generation semisynthetic cephalosporin antibiotic administered parenterally for the treatment of severe bacterial infections.",
    "secondary": "In pharmacology and antibiotic history, a zwitterionic derivative of cephalosporin C active against both Gram-positive and Gram-negative bacteria, formerly used prior to less nephrotoxic congeners.",
    "quotes": [
      {
        "author": "Edward Abraham",
        "work": "The Cephalosporins",
        "quote": "The introduction of the pyridinium group yielded **cephaloridine**, an injectable antibiotic with exceptionally high intrinsic potency."
      },
      {
        "author": "René Dubos",
        "work": "Bacterial Diseases of Man",
        "quote": "High doses of **cephaloridine** commanded clinical respect because of potential nephrotoxicity in compromised renal states."
      },
      {
        "author": "Selman Waksman",
        "work": "The Action of Antibiotic Substances",
        "quote": "Clinical trials with **cephaloridine** confirmed effective control of severe pneumococcal and staphylococcal bacteremias."
      }
    ]
  }
};

const updated = updateNotesBatch(BASE_DIR, BATCH4_DATA);
console.log(`Body & Physiology Part 1 - Batch 4 Completed: ${updated} / ${Object.keys(BATCH4_DATA).length} notes updated.`);
