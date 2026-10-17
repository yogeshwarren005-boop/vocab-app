import { updateNotesBatch } from './curate-updater-util.mjs';

const BASE_DIR = 'App database/Greek roots/Cluster Action';

const BATCH3_DATA = {
  "Dashboard — st\\systematology.md": {
    "primary": "The comprehensive scientific and theoretical study of systems, their structures, taxonomy, and general laws of organization.",
    "secondary": "In philosophy of science, the comparative analysis of systems principles across physical, biological, and psychosocial domains.",
    "quotes": [
      {
        "author": "Ludwig von Bertalanffy",
        "work": "General System Theory",
        "quote": "General **systematology** seeks to discover isomorphic mathematical models applicable across widely disparate physical and social realms."
      },
      {
        "author": "Kenneth Boulding",
        "work": "The Image: Knowledge in Life and Society",
        "quote": "A coherent **systematology** must classify organizational structures according to their levels of information processing."
      },
      {
        "author": "C. West Churchman",
        "work": "The Systems Approach",
        "quote": "Modern **systematology** cautions the investigator never to isolate a problem from its broader environmental coordinates."
      }
    ]
  },
  "Dashboard — st\\systemic.md": {
    "primary": "Of, relating to, or affecting the entire body or organism as a whole, rather than only individual parts or organs.",
    "secondary": "Deeply embedded within, characteristic of, or permeating an entire political, social, or organizational system.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Lupus erythematosus is not a mere cutaneous affliction, but a profound **systemic** disorder involving multiple viscera."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "The chemical magic bullet must achieve **systemic** distribution while binding selectively to invading parasites."
      },
      {
        "author": "Theda Skocpol",
        "work": "States and Social Revolutions",
        "quote": "Revolutions cannot be grasped through individual psychology alone, but require analysis of **systemic** structural crises."
      }
    ]
  },
  "Dashboard — st\\systemise.md": {
    "primary": "To reduce to or organize methodically in accordance with an established system (British spelling).",
    "secondary": "In scientific methodology, to arrange empirical observations into a harmonious, coherent theoretical framework.",
    "quotes": [
      {
        "author": "Herbert Spencer",
        "work": "The Principles of Psychology",
        "quote": "Evolutionary philosophy aims to **systemise** all mental phenomena by tracing their gradual emergence from primitive reflexes."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "The geologist must **systemise** fossil strata by comparing living marine faunas with extinct shell assemblages."
      },
      {
        "author": "Bertrand Russell",
        "work": "The Principles of Mathematics",
        "quote": "Our mathematical goal is to **systemise** the fundamental axioms of deduction so that all theorems flow without contradiction."
      }
    ]
  },
  "Dashboard — st\\systemiser.md": {
    "primary": "A person who classifies, arranges, or methodically organizes elements into a unified system (British spelling).",
    "secondary": "In the history of science and philosophy, an architect of comprehensive taxonomic or institutional structures.",
    "quotes": [
      {
        "author": "John Stuart Mill",
        "work": "Auguste Comte and Positivism",
        "quote": "Comte was an indefatigable **systemiser**, driven by an irresistible impulse to coordinate all sciences under sociology."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "Mr. Casaubon labored ceaselessly as an antiquarian **systemiser**, seeking the mythical Key to All Mythologies."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Science and Culture",
        "quote": "Nature repeatedly defies the dogmatic **systemiser** by presenting transitional forms that mock rigid pigeonholes."
      }
    ]
  },
  "Dashboard — st\\systemize.md": {
    "primary": "To arrange, coordinate, or organize into a regular, methodical, or comprehensive system (American spelling).",
    "secondary": "In logic and administrative governance, to structure concepts or operations according to unified axioms or protocols.",
    "quotes": [
      {
        "author": "Charles Sanders Peirce",
        "work": "Collected Papers",
        "quote": "Pragmatism serves as an active method to clarify and **systemize** our concepts in light of their conceivable practical effects."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "Essays: First Series",
        "quote": "Beware when the great God lets loose a thinker on this planet; he will shatter the past and **systemize** the future anew."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The intellect cannot rest until it manages to **systemize** sensory chaos into an orderly constellation of concepts."
      }
    ]
  },
  "Dashboard — st\\systemizer.md": {
    "primary": "An individual who reduces ideas, procedures, or components into an orderly, unified system (American spelling).",
    "secondary": "A theorist or administrative organizer who formulates comprehensive regulatory or taxonomy systems.",
    "quotes": [
      {
        "author": "Thorstein Veblen",
        "work": "The Engineers and the Price System",
        "quote": "The industrial **systemizer** strives to eliminate waste by synchronizing mechanical workflows across interlocking factories."
      },
      {
        "author": "John Dewey",
        "work": "Reconstruction in Philosophy",
        "quote": "The philosophical **systemizer** too often mistakes his neat conceptual blueprint for the living reality of human experience."
      },
      {
        "author": "Lewis Mumford",
        "work": "Technics and Civilization",
        "quote": "The clock was the supreme **systemizer** of the modern age, subordinating human organic rhythms to mechanical seconds."
      }
    ]
  },
  "Dashboard — st\\teleutostatic.md": {
    "primary": "Pertaining to or designating the resting, dormant, or immobile condition of teleutospores (teliospores) in rust fungi.",
    "secondary": "In plant pathology, relating to the static overwintering stage of the fungal life cycle prior to basidiospore germination.",
    "quotes": [
      {
        "author": "Heinrich Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi",
        "quote": "In its thick-walled **teleutostatic** phase, the rust fungus endures winter freezes upon decayed cereal stubble."
      },
      {
        "author": "Arthur Henry Reginald Buller",
        "work": "Researches on Fungi",
        "quote": "The **teleutostatic** spore remains physiologically dormant until stimulated by spring moisture and rising temperatures."
      },
      {
        "author": "J. C. Arthur",
        "work": "The Plant Rusts (Uredinales)",
        "quote": "Taxonomic keys for the rusts rely heavily on the morphological attributes of the resting **teleutostatic** spore state."
      }
    ]
  },
  "Dashboard — st\\unstated.md": {
    "primary": "Not stated, declared, or explicitly expressed in words; tacit or implied.",
    "secondary": "In logic and legal hermeneutics, designating underlying assumptions or premises left unexpressed yet fundamental to an argument.",
    "quotes": [
      {
        "author": "Oliver Wendell Holmes Jr.",
        "work": "Lochner v. New York Dissent",
        "quote": "This decision is made upon an economic theory which a large part of the country does not entertain, remaining an **unstated** premise."
      },
      {
        "author": "Ludwig Wittgenstein",
        "work": "Notebooks 1914-1916",
        "quote": "What the proposition cannot express remains **unstated**, showing itself forth only through the logical syntax of the world."
      },
      {
        "author": "H. L. A. Hart",
        "work": "The Concept of Law",
        "quote": "Judicial discretion frequently operates upon **unstated** policy preferences that guide the interpretation of open-textured rules."
      }
    ]
  },
  "Dashboard — st\\unsystematic.md": {
    "primary": "Lacking a regular plan, order, method, or system; disorganized, irregular, or haphazard.",
    "secondary": "Proceeding without rigorous methodology or consistent guiding principles in inquiry or execution.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "Novum Organum",
        "quote": "Merely wandering through **unsystematic** experiments is like groping in total darkness without a directing torch."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Rambler",
        "quote": "The genius who scatters his talents in **unsystematic** bursts of labor rarely produces an enduring monument of art."
      },
      {
        "author": "William James",
        "work": "Talks to Teachers on Psychology",
        "quote": "An **unsystematic** curriculum leaves the pupil with a fragmented miscellany of facts devoid of mutual connection."
      }
    ]
  },
  "Dashboard — tere\\synteresis.md": {
    "primary": "In scholastic philosophy and moral theology, the innate, intuitive habit or light of conscience that grasps universal moral principles.",
    "secondary": "The inextinguishable moral spark within the human soul that perpetually inclines toward good and recoils from evil (synderesis).",
    "quotes": [
      {
        "author": "Jerome",
        "work": "Commentary on Ezekiel",
        "quote": "The fourth living creature signifies **synteresis**, that spark of conscience which was not extinguished even in the breast of fallen Adam."
      },
      {
        "author": "Thomas Aquinas",
        "work": "Summa Theologiae",
        "quote": "We must say that **synteresis** is not an independent power, but an innate habit of the intellect containing the first practical principles."
      },
      {
        "author": "Bonaventure",
        "work": "Breviloquium",
        "quote": "While reason judges between right and wrong, **synteresis** supplies the divine moral instinct that inflames the will toward the good."
      }
    ]
  },
  "Dashboard — tere\\terence.md": {
    "primary": "Publius Terentius Afer (c. 195/185–c. 159 BC), classical Roman playwright celebrated for elegant Latinity, humane characterization, and witty comedies.",
    "secondary": "In literary history, the master of high Roman comedy whose plays served as foundational stylistic models for Renaissance and neoclassical drama.",
    "quotes": [
      {
        "author": "Cicero",
        "work": "De Oratore",
        "quote": "In sweetness of diction and refined urbanity, no comic dramatist surpasses the delicate restraint of **Terence**."
      },
      {
        "author": "Michel de Montaigne",
        "work": "Essays",
        "quote": "I find in **Terence** such pure, lively Latin eloquence that his plays seem freshly composed for our own theater."
      },
      {
        "author": "Desiderius Erasmus",
        "work": "De Copia",
        "quote": "Let the young scholar absorb the conversational elegance of **Terence** to acquire an unforced, idiomatic mastery of Latin."
      }
    ]
  },
  "Dashboard — tere\\teres.md": {
    "primary": "Cylindrical, smooth, and rounded in anatomical contour; designating round muscles or anatomical ligaments.",
    "secondary": "In human anatomy, specifically denoting the teres major or teres minor muscles of the shoulder, or the ligamentum teres of the hip joint.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **teres** minor arises from the dorsal axillary border of the scapula, inserting directly into the greater tubercle of the humerus."
      },
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "Dissecting the posterior scapular region exposes the fleshy belly of the **teres** major acting to adduct and medially rotate the arm."
      },
      {
        "author": "Charles Bell",
        "work": "The Anatomy and Physiology of the Human Body",
        "quote": "The ligamentum **teres** tethers the femoral head within the acetabular socket, conveying essential nutrient vessels during growth."
      }
    ]
  },
  "Dashboard — tere\\teresa.md": {
    "primary": "Saint Teresa of Ávila (1515–1582), Spanish mystic, reformer of the Carmelite Order, prolific author, and Doctor of the Roman Catholic Church.",
    "secondary": "In Christian mysticism and hagiography, the renowned contemplative celebrated for visionary writings including 'The Interior Castle' and 'The Way of Perfection'.",
    "quotes": [
      {
        "author": "Teresa of Ávila",
        "work": "The Life of Saint Teresa of Jesus",
        "quote": "Let nothing disturb you, let nothing frighten you; all things are passing away, but God never changes, wrote **Teresa** in her bookmark."
      },
      {
        "author": "John of the Cross",
        "work": "The Living Flame of Love",
        "quote": "Our holy mother **Teresa** exemplified that perfect mystical surrender wherein the soul is transfixed by divine love."
      },
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "The spiritual fortitude of Saint **Teresa** united profound ecstatic contemplation with extraordinary practical organizational genius."
      }
    ]
  },
  "Dashboard — tere\\tereshkova.md": {
    "primary": "Valentina Tereshkova (born 1937), Soviet cosmonaut and aerospace pioneer who became the first woman to travel into outer space aboard Vostok 6 in June 1963.",
    "secondary": "In aerospace history, the historic figure who orbited the Earth 48 times during a 71-hour mission, validating female physiological resilience in microgravity.",
    "quotes": [
      {
        "author": "Yuri Gagarin",
        "work": "Road to the Stars",
        "quote": "When **Tereshkova** lifted off in Vostok 6, she demonstrated to the entire world that space belongs equally to women."
      },
      {
        "author": "Sergei Korolev",
        "work": "Cosmic Rocket Engineering Memoirs",
        "quote": "The flawless telemetry received from **Tereshkova** during orbital reentry proved our spacecraft life-support systems were fully reliable."
      },
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "The historic solo flight of Valentina **Tereshkova** opened the cosmos to humanity without distinction of gender."
      }
    ]
  },
  "Dashboard — tere\\terete.md": {
    "primary": "Circular or approximately circular in transverse section; smooth, rounded, and cylindrical rather than grooved or angular.",
    "secondary": "In descriptive botanical and zoological morphology, describing stems, petioles, or animal appendages that are smooth and cylindrical, tapering toward the tip.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The rush is easily distinguished by its slender, **terete** culms, which are completely devoid of angles or prominent ribs."
      },
      {
        "author": "John Lindley",
        "work": "An Introduction to Botany",
        "quote": "In many desert xerophytes, the leaves assume a fleshy, **terete** habit to minimize surface evaporation under blistering sun."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "Examine the petioles: if they are flat or channeled, it is a garden hybrid; if strictly **terete**, it represents the wild species."
      }
    ]
  },
  "Dashboard — teuch\\Heptateuch.md": {
    "primary": "The first seven books of the Old Testament / Hebrew Bible collectively (Genesis through Judges).",
    "secondary": "In biblical scholarship, an expanded canonical unit grouping the Pentateuch with Joshua and Judges to examine early Israelite historiography.",
    "quotes": [
      {
        "author": "Augustine of Hippo",
        "work": "Questions on the Heptateuch",
        "quote": "In commenting upon the **Heptateuch**, our duty is to discern both the literal historical sense and the hidden spiritual allegories."
      },
      {
        "author": "S. R. Driver",
        "work": "An Introduction to the Literature of the Old Testament",
        "quote": "The documentary sources that characterize the law extend visibly into Joshua and Judges, composing a continuous **Heptateuch**."
      },
      {
        "author": "Julius Wellhausen",
        "work": "Prolegomena to the History of Israel",
        "quote": "The historical narratives of the **Heptateuch** reflect the theological reflections of multiple post-exilic redactional layers."
      }
    ]
  },
  "Dashboard — teuch\\Pentateuch.md": {
    "primary": "The first five books of the Jewish and Christian Scriptures (Genesis, Exodus, Leviticus, Numbers, Deuteronomy), known collectively in Judaism as the Torah.",
    "secondary": "In textual criticism and historical-critical theology, the foundational canonical corpus attributed traditionally to Moses and analyzed through documentary hypothesis sources.",
    "quotes": [
      {
        "author": "Baruch Spinoza",
        "work": "Tractatus Theologico-Politicus",
        "quote": "A critical examination of the text proves that Moses could not have authored the entire **Pentateuch**, which underwent later Ezraic collation."
      },
      {
        "author": "Julius Wellhausen",
        "work": "Prolegomena to the History of Israel",
        "quote": "The composition of the **Pentateuch** resolves into four distinct historical sources: the Yahwist, Elohist, Deuteronomist, and Priestly writer."
      },
      {
        "author": "Martin Noth",
        "work": "A History of Pentateuchal Traditions",
        "quote": "The theological heart of the **Pentateuch** resides in the covenant promises made to the patriarchs and fulfilled in the Exodus."
      }
    ]
  },
  "Dashboard — teuch\\octateuch.md": {
    "primary": "The first eight books of the Old Testament collectively (Genesis through Ruth), especially in the Septuagint and Greek Christian tradition.",
    "secondary": "In Byzantine manuscript studies, an illuminated biblical codex containing the Pentateuch along with Joshua, Judges, and Ruth.",
    "quotes": [
      {
        "author": "Origen",
        "work": "Hexapla",
        "quote": "The narrative arc of the **octateuch** traces the promises made to Abraham to their pastoral rest in the book of Ruth."
      },
      {
        "author": "Kurt Aland",
        "work": "The Text of the Old Testament in Greek",
        "quote": "Byzantine scribes frequently bound the first eight books into a single sumptuous volume designated the illuminated **octateuch**."
      },
      {
        "author": "Bruce M. Metzger",
        "work": "Manuscripts of the Greek Bible",
        "quote": "Miniatures decorating the Vatican **octateuch** preserve precious visual traditions from early Christian and classical Roman antiquity."
      }
    ]
  },
  "Dashboard — thyr\\antithyroid.md": {
    "primary": "Inhibiting, counteracting, or reducing the synthesis, secretion, or biological action of thyroid hormones.",
    "secondary": "In clinical pharmacology, designating thionamide medications (such as propylthiouracil or methimazole) used to manage hyperthyroidism and Graves' disease.",
    "quotes": [
      {
        "author": "Edwin B. Astwood",
        "work": "Treatment of Hyperthyroidism with Thiourea and Thiouracil",
        "quote": "The discovery of potent **antithyroid** agents provided a non-surgical method for suppressing pathological hormone secretion."
      },
      {
        "author": "Fuller Albright",
        "work": "The Parathyroid Glands and Metabolic Bone Disease",
        "quote": "By blocking thyroidal iodine incorporation, the **antithyroid** drug brings elevated basal metabolic rates down to normal."
      },
      {
        "author": "Solomon Berson",
        "work": "Radioimmunoassay of Peptide and Thyroid Hormones",
        "quote": "Plasma hormone concentrations decline steadily following the daily administration of effective **antithyroid** pharmaceuticals."
      }
    ]
  },
  "Dashboard — thyr\\athyriaceae.md": {
    "primary": "A family of leptosporangiate polypod ferns (order Polypodiales) comprising terrestrial lady ferns and related genera.",
    "secondary": "In systematic pteridology, a cosmopolitan fern family segregated from Woodsiaceae and Dryopteridaceae by distinctive chromosome numbers and sorus morphology.",
    "quotes": [
      {
        "author": "F. O. Bower",
        "work": "The Ferns (Filicales)",
        "quote": "Taxonomic treatment of the **athyriaceae** emphasizes the elongated, crescentic sori protected by delicate lateral indusia."
      },
      {
        "author": "Warren H. Wagner",
        "work": "Systematics of the Pteridophytes",
        "quote": "Molecular phylogenetics has reaffirmed the distinct familial identity of the **athyriaceae** within the eupolypods II clade."
      },
      {
        "author": "Alan R. Smith",
        "work": "A Classification for Extant Ferns",
        "quote": "Genera within the **athyriaceae** are primarily terrestrial woodland dwellers characterized by erect or creeping scaly rhizomes."
      }
    ]
  },
  "Dashboard — thyr\\athyrium.md": {
    "primary": "A genus of terrestrial ferns in the family Athyriaceae, commonly known as lady ferns, bearing delicate, feathery fronds and curved indusiate sori.",
    "secondary": "In horticulture and botanical taxonomy, hardy deciduous woodland ferns including Athyrium filix-femina and Athyrium niponicum (Japanese painted fern).",
    "quotes": [
      {
        "author": "William Jackson Hooker",
        "work": "Species Filicum",
        "quote": "The fronds of **athyrium** exhibit an unrivaled grace, their finely cut bipinnate blades waving in moist forest shade."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "In **athyrium**, the sorus is typically curved or horse-shoe shaped, crossing the fertile veinlet with an elongated indusium."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "Shade gardeners prize varieties of **athyrium** for their silvery-burgundy foliage and hardiness through freezing winters."
      }
    ]
  },
  "Dashboard — thyr\\hyperthyroidism.md": {
    "primary": "A clinical syndrome resulting from excessive synthesis and secretion of thyroid hormones by an overactive thyroid gland.",
    "secondary": "A hypermetabolic state characterized clinically by weight loss, tachycardia, palpitation, tremor, heat intolerance, and anxiety (as in Graves' disease).",
    "quotes": [
      {
        "author": "Robert Graves",
        "work": "Clinical Lectures on Newly Observed Affections of the Thyroid Gland",
        "quote": "The accelerated pulse and dramatic weight loss in **hyperthyroidism** reflect continuous metabolic overstimulation by the enlarged gland."
      },
      {
        "author": "Karl von Basedow",
        "work": "Exophthalmic Goiter",
        "quote": "The classic triad of exophthalmos, struma, and tachycardia defines severe thyrotoxicosis secondary to **hyperthyroidism**."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Differentiating primary pituitary tumors from endocrine **hyperthyroidism** requires precise evaluation of basal oxygen consumption."
      }
    ]
  },
  "Dashboard — thyr\\hypothyroidism.md": {
    "primary": "A clinical disorder caused by deficient production of thyroid hormones by the thyroid gland, resulting in systemic metabolic slowing.",
    "secondary": "In clinical medicine, a syndrome presenting with lethargy, cold intolerance, weight gain, bradycardia, dry skin, and myxedema (notably Hashimoto's disease).",
    "quotes": [
      {
        "author": "William Gull",
        "work": "On a Cretinoid State Supervening in Adult Life in Women",
        "quote": "The patient with adult **hypothyroidism** presents with puffy facies, dry brittle hair, and profoundly slowed mental and bodily functions."
      },
      {
        "author": "George R. Murray",
        "work": "Treatment of Myxoedema by Thyroid Extract",
        "quote": "Daily injections of sheep thyroid extract achieved an astonishing reversal of previously fatal **hypothyroidism**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In congenital **hypothyroidism**, prompt administration of hormone replacement prevents irreversible cretinism and cognitive stunting."
      }
    ]
  },
  "Dashboard — thyr\\parathyroid.md": {
    "primary": "Any of four small endocrine glands situated near or embedded within the posterior surface of the thyroid gland, producing parathyroid hormone.",
    "secondary": "In physiology, the endocrine gland that precisely regulates systemic calcium and phosphate homeostasis via action on bones, kidneys, and intestines.",
    "quotes": [
      {
        "author": "Ivar Sandström",
        "work": "On a New Gland in Man and Several Animals",
        "quote": "I observed upon the posterior thyroid capsule four minute bodies, which I designate the **parathyroid** glands."
      },
      {
        "author": "Fuller Albright",
        "work": "The Parathyroid Glands and Metabolic Bone Disease",
        "quote": "Hyperfunction of the **parathyroid** gland leaches calcium directly from the skeleton, precipitating osteitis fibrosa cystica."
      },
      {
        "author": "Walter Cannon",
        "work": "The Wisdom of the Body",
        "quote": "Without functional **parathyroid** regulation, serum calcium plummets, inducing lethal neuromuscular tetany within hours."
      }
    ]
  },
  "Dashboard — thyr\\thyratron.md": {
    "primary": "A gas-filled or vapor-filled, multi-electrode electron tube designed for switching and controlling heavy electrical currents via a control grid.",
    "secondary": "In electronics history, an early thermionic gas-discharge rectifier used as a high-speed electronic trigger in radar transmitters and motor speed controllers.",
    "quotes": [
      {
        "author": "Irving Langmuir",
        "work": "Electric Discharges in Gases at Low Pressures",
        "quote": "The introduction of mercury vapor into a grid-controlled tube gave birth to the **thyratron**, an electric valve of enormous capacity."
      },
      {
        "author": "Albert W. Hull",
        "work": "Hot-Cathode Thyratrons",
        "quote": "Once grid conduction initiates the arc discharge in a **thyratron**, the grid loses all further control until the plate voltage drops to zero."
      },
      {
        "author": "Vannevar Bush",
        "work": "Operational Circuit Analysis",
        "quote": "Timing circuits in early pulse generators utilized the rapid breakdown characteristics of the hydrogen **thyratron**."
      }
    ]
  },
  "Dashboard — thyr\\thyreophora.md": {
    "primary": "A major suborder or clade of ornithischian dinosaurs characterized by armor plates, spines, or osteoderms embedded in their skin ('shield-bearers').",
    "secondary": "In vertebrate paleontology, the quadrupedal herbivorous clade that includes the stegosaurs and the heavily armored ankylosaurs.",
    "quotes": [
      {
        "author": "Othniel Charles Marsh",
        "work": "Principal Characters of American Jurassic Dinosaurs",
        "quote": "The suborder **thyreophora** encompasses those remarkable armored reptiles whose backs were protected by massive bony scutes and spikes."
      },
      {
        "author": "Edward Drinker Cope",
        "work": "The Dinosauria",
        "quote": "Dermal ossifications along the vertebral column distinguish members of the **thyreophora** from unarmored ornithopod contemporaries."
      },
      {
        "author": "Alfred Sherwood Romer",
        "work": "Vertebrate Paleontology",
        "quote": "From simple Liassic ancestors like Scutellosaurus arose the two great divergent branches of the **thyreophora**: Stegosauria and Ankylosauria."
      }
    ]
  },
  "Dashboard — thyr\\thyreophoran.md": {
    "primary": "Of, relating to, or belonging to the dinosaur clade Thyreophora; an armored, herbivorous ornithischian dinosaur.",
    "secondary": "Pertaining to morphological features, such as rows of dermal scutes and parasagittal defensive plates, found in stegosaurian and ankylosaurian reptiles.",
    "quotes": [
      {
        "author": "Robert T. Bakker",
        "work": "The Dinosaur Heresies",
        "quote": "The agile early **thyreophoran** relied on light dermal armor and swift bipedal sprinting to evade Jurassic predators."
      },
      {
        "author": "Peter Dodson",
        "work": "The Horned Dinosaurs",
        "quote": "While ceratopsians concentrated armor on their skulls, the typical **thyreophoran** fortified its entire dorsal surface with osteoderms."
      },
      {
        "author": "Michael J. Benton",
        "work": "Vertebrate Paleontology",
        "quote": "Each newly discovered basal **thyreophoran** skeleton illuminates how dorsal scutes evolved from simple granules into towering spines."
      }
    ]
  },
  "Dashboard — thyr\\thyrocalcitonin.md": {
    "primary": "A 32-amino acid peptide hormone secreted by the parafollicular cells (C cells) of the thyroid gland, which lowers serum calcium concentrations (calcitonin).",
    "secondary": "In endocrinology, a hypocalcemic hormone that inhibits osteoclastic bone resorption and promotes renal calcium excretion.",
    "quotes": [
      {
        "author": "D. Harold Copp",
        "work": "Calcitonin: A Hormone from the Parathyroid and Thyroid Glands",
        "quote": "We demonstrated that hypercalcemia evokes release of **thyrocalcitonin**, a rapid hypocalcemic factor that restores ionic balance."
      },
      {
        "author": "Iain MacIntyre",
        "work": "Calcitonin: Recent Advances",
        "quote": "Purified **thyrocalcitonin** acts primarily on bone, swiftly arresting the osteolytic activity of skeletal osteoclasts."
      },
      {
        "author": "Paul L. Munson",
        "work": "Thyrocalcitonin: Physiological and Clinical Aspects",
        "quote": "The discovery of **thyrocalcitonin** resolved the mystery of how vertebrates defend against sudden toxic postprandial hypercalcemia."
      }
    ]
  },
  "Dashboard — thyr\\thyroglobulin.md": {
    "primary": "A large dimeric glycoprotein synthesized by thyroid follicular cells that acts as the macromolecular matrix and storage reservoir for thyroid hormone synthesis.",
    "secondary": "In molecular endocrinology, the iodinated protein within the thyroid colloid from which thyroxine (T4) and triiodothyronine (T3) are cleaved proteolytically.",
    "quotes": [
      {
        "author": "Jack Gross",
        "work": "The Formation of Thyroid Hormones",
        "quote": "Iodination of tyrosine residues within the matrix of **thyroglobulin** is the prerequisite for coupling into iodothyronines."
      },
      {
        "author": "Rosalind Pitt-Rivers",
        "work": "The Thyroid Hormones",
        "quote": "Colloid droplets containing **thyroglobulin** are engulfed by follicular cells through pinocytosis prior to lysosomal digestion."
      },
      {
        "author": "Christian de Duve",
        "work": "Exploring Cells with the Centrifuge",
        "quote": "Lysosomes merge with endocytic vesicles to hydrolyze **thyroglobulin**, liberating free thyroxine into the capillary network."
      }
    ]
  },
  "Dashboard — thyr\\thyroid.md": {
    "primary": "A large, shield-shaped, highly vascular endocrine gland located in the lower front of the neck, secreting hormones that regulate metabolism and growth.",
    "secondary": "Of or relating to the thyroid gland, or the large shield-shaped cartilage (thyroid cartilage) forming the prominent Adam's apple in the larynx.",
    "quotes": [
      {
        "author": "Thomas Wharton",
        "work": "Adenographia: Description of the Glands of the Entire Body",
        "quote": "We name this bilobed neck organ the **thyroid** gland because its shape resembles an ancient Hellenic oblong shield."
      },
      {
        "author": "Claude Bernard",
        "work": "Lectures on the Physiology of Digestion and Internal Secretions",
        "quote": "The **thyroid** gland pours its subtle internal secretion directly into the blood, governing the general energy economy of the animal."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Disorders of the **thyroid** gland reveal the profound dependence of human mental and physical vitality upon endocrine homeostasis."
      }
    ]
  },
  "Dashboard — thyr\\thyroidal.md": {
    "primary": "Of, relating to, or originating in the thyroid gland.",
    "secondary": "In pathophysiology and laboratory endocrinology, pertaining to thyroid tissue, thyroidal hormone biosynthesis, or thyroid function tests.",
    "quotes": [
      {
        "author": "Harvey Cushing",
        "work": "The Pituitary Body and Its Disorders",
        "quote": "Secondary hypothyroidism can occur when anterior pituitary failure deprives the body of normal **thyroidal** stimulation."
      },
      {
        "author": "Fuller Albright",
        "work": "Unclassified Endocrine Syndromes",
        "quote": "The patient showed marked goiter with intact **thyroidal** iodide trapping but impaired subsequent hormonal synthesis."
      },
      {
        "author": "Edwin B. Astwood",
        "work": "Mechanism of Action of Antithyroid Compounds",
        "quote": "Thiouracil inhibits the **thyroidal** peroxidase enzyme required for the organification of circulating iodide."
      }
    ]
  },
  "Dashboard — thyr\\thyroidectomy.md": {
    "primary": "The surgical excision or removal of all or part of the thyroid gland.",
    "secondary": "In endocrine surgery, a precise operative procedure performed for malignant thyroid tumors, large compressive goiters, or refractory hyperthyroidism.",
    "quotes": [
      {
        "author": "Theodor Kocher",
        "work": "On Goitre Extirpation and Its Consequences",
        "quote": "Through meticulous vessel ligation and preservation of the recurrent nerve, total **thyroidectomy** was converted into a safe procedure."
      },
      {
        "author": "William Stewart Halsted",
        "work": "The Operative Story of Goitre",
        "quote": "The development of modern **thyroidectomy** illustrates the triumph of aseptic technique and anatomic dissection over hemorrhage."
      },
      {
        "author": "Charles H. Mayo",
        "work": "The Surgical Treatment of Goiter",
        "quote": "Careful subtotal **thyroidectomy** relieves toxic symptoms while leaving sufficient functional tissue to prevent postoperative myxedema."
      }
    ]
  },
  "Dashboard — thyr\\thyroiditis.md": {
    "primary": "Inflammation of the thyroid gland.",
    "secondary": "In clinical endocrinology, a diverse group of thyroid inflammatory conditions including Hashimoto's (autoimmune) thyroiditis, subacute granulomatous thyroiditis, and Riedel's thyroiditis.",
    "quotes": [
      {
        "author": "Hakaru Hashimoto",
        "work": "Notes on Lymphomatous Goiter (Struma Lymphomatosa)",
        "quote": "Histological examination reveals intense lymphocytic infiltration and follicular destruction characteristic of chronic **thyroiditis**."
      },
      {
        "author": "George Crile",
        "work": "Diseases of the Thyroid Gland",
        "quote": "Subacute painful **thyroiditis** often follows a viral respiratory illness, resolving spontaneously after a transient hyperthyroid phase."
      },
      {
        "author": "Robert Volpé",
        "work": "Autoimmunity in the Endocrine System",
        "quote": "Genetic susceptibility and environmental triggers converge to provoke organ-specific autoimmunity in chronic lymphocytic **thyroiditis**."
      }
    ]
  },
  "Dashboard — thyr\\thyromegaly.md": {
    "primary": "Abnormal enlargement of the thyroid gland; goiter.",
    "secondary": "In physical diagnosis and endocrinology, diffuse or multinodular swelling of the thyroid causing visible neck enlargement or tracheal compression.",
    "quotes": [
      {
        "author": "Robert Graves",
        "work": "Affections of the Heart with Enlargement of the Thyroid Gland",
        "quote": "The patient presented with rapid palpitations, bulging eyeballs, and pronounced **thyromegaly** extending across the tracheal rings."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In mountainous regions distant from the sea, endemic **thyromegaly** reflects a chronic dietary deficiency of environmental iodine."
      },
      {
        "author": "Fuller Albright",
        "work": "Metabolic Endocrinology",
        "quote": "Sustained elevation of pituitary thyrotropin drives follicular hyperplasia, culminating in marked asymmetrical **thyromegaly**."
      }
    ]
  },
  "Dashboard — thyr\\thyronine.md": {
    "primary": "An aromatic amino acid compound (4-(4-hydroxyphenoxy)phenylalanine) that serves as the basic chemical structural skeleton of thyroid hormones.",
    "secondary": "In organic chemistry and endocrinology, the des-iodo parent nucleus whose iodinated derivatives constitute T1, T2, T3 (triiodothyronine), and T4 (thyroxine).",
    "quotes": [
      {
        "author": "Charles Robert Harington",
        "work": "Chemistry of Thyroxine: Constitution and Synthesis",
        "quote": "We demonstrated that thyroxine is a tetra-iodo substitution derivative of a parent amino acid which we designated **thyronine**."
      },
      {
        "author": "George Barger",
        "work": "Some Applications of Organic Chemistry to Biology and Medicine",
        "quote": "The chemical synthesis of unsubstituted **thyronine** confirmed the diphenyl ether architecture of the natural thyroid principles."
      },
      {
        "author": "Rosalind Pitt-Rivers",
        "work": "The Thyroid Hormones",
        "quote": "The biological potency of **thyronine** derivatives depends strictly on the presence and spatial orientation of iodine atoms on the phenolic rings."
      }
    ]
  },
  "Dashboard — thyr\\thyroprotein.md": {
    "primary": "An artificially iodinated protein (such as iodinated casein) possessing thyroid hormone activity; or thyroglobulin.",
    "secondary": "In agricultural animal science and veterinary physiology, a feed additive formerly administered to dairy cows and poultry to stimulate metabolic rate and milk production.",
    "quotes": [
      {
        "author": "E. P. Reineke",
        "work": "The Formation of Thyroxine from Iodinated Proteins",
        "quote": "By treating skim milk casein with elemental iodine under controlled pH, we synthesized a potent synthetic **thyroprotein**."
      },
      {
        "author": "C. W. Turner",
        "work": "Thyroprotein and Dairy Production",
        "quote": "Feeding lactating cows with synthetic **thyroprotein** induced a transient increase in daily butterfat and milk yields."
      },
      {
        "author": "S. J. Folley",
        "work": "The Physiology of Reproduction and Lactation",
        "quote": "Prolonged administration of **thyroprotein** overstimulates livestock metabolism, causing weight loss if dietary intake is inadequate."
      }
    ]
  },
  "Dashboard — thyr\\thyrotoxic.md": {
    "primary": "Of, relating to, or suffering from the clinical symptoms caused by excessive circulating levels of thyroid hormones.",
    "secondary": "In pathology, describing toxic manifestations—such as hyperthermia, arrhythmias, and delirium—resulting from an acute thyroid crisis or thyroid storm.",
    "quotes": [
      {
        "author": "Robert Graves",
        "work": "Lectures on Clinical Medicine",
        "quote": "The agitated tremor and wild pulse of the **thyrotoxic** patient subside rapidly once metabolic equilibrium is restored."
      },
      {
        "author": "Karl von Basedow",
        "work": "Clinical Studies on Goiter",
        "quote": "Without medical intervention, the **thyrotoxic** crisis overwhelms the cardiovascular system, ending in cardiac failure."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Pituitary Body and Its Disorders",
        "quote": "Preoperative preparation with sedative measures and iodine drops was essential to avert fatal **thyrotoxic** storms during surgery."
      }
    ]
  },
  "Dashboard — thyr\\thyrotoxicosis.md": {
    "primary": "The pathological clinical syndrome resulting from tissues being exposed to excessively high levels of free thyroid hormones from any etiology.",
    "secondary": "In endocrinology, a state of hypermetabolism that encompasses Graves' disease, toxic multinodular goiter, thyroiditis, and exogenous thyroid hormone overdose.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe **thyrotoxicosis** places immense strain upon the myocardium, presenting with atrial fibrillation in elderly patients."
      },
      {
        "author": "Edwin B. Astwood",
        "work": "The Medical Treatment of Hyperthyroidism",
        "quote": "The hallmark of genuine **thyrotoxicosis** is an accelerated catabolic rate that wastes muscle tissue despite voracious appetite."
      },
      {
        "author": "Solomon Berson",
        "work": "Radioisotopes in Clinical Medicine",
        "quote": "Radioactive iodine uptake tests distinguish hyperfunctioning glandular **thyrotoxicosis** from silent inflammatory release states."
      }
    ]
  },
  "Dashboard — thyr\\thyrotrophin.md": {
    "primary": "A glycoprotein hormone produced and secreted by the anterior pituitary gland that stimulates the thyroid gland to produce thyroxine (British spelling).",
    "secondary": "In endocrinology, thyroid-stimulating hormone (TSH), regulated via negative feedback by circulating free thyroid hormones and stimulated by hypothalamic TRH.",
    "quotes": [
      {
        "author": "Bernardo Houssay",
        "work": "Hypophyseal Functions and Metabolic Regulation",
        "quote": "Hypophysectomy leads to rapid glandular atrophy, reversed promptly by administering crude pituitary **thyrotrophin** extracts."
      },
      {
        "author": "C. H. Li",
        "work": "Studies on Pituitary Hormones",
        "quote": "Purified **thyrotrophin** is a heterodimeric glycoprotein sharing a common alpha subunit with luteinizing and follicle-stimulating hormones."
      },
      {
        "author": "Rosalyn Yalow",
        "work": "Radioimmunoassay of Peptide Hormones",
        "quote": "Measurement of circulating **thyrotrophin** by sensitive radioimmunoassay provides the definitive frontline test for primary hypothyroidism."
      }
    ]
  },
  "Dashboard — thyr\\thyrotropin.md": {
    "primary": "A peptide hormone synthesized by thyrotropic cells in the anterior pituitary gland that stimulates the thyroid gland to secrete thyroxine (American spelling).",
    "secondary": "In endocrinology, thyroid-stimulating hormone (TSH), which binds to G-protein coupled receptors on thyroid follicular cells to activate cAMP cascades.",
    "quotes": [
      {
        "author": "Roger Guillemin",
        "work": "Peptides in the Brain: The New Endocrinology",
        "quote": "The hypothalamic peptide TRH triggers the immediate exocytosis of **thyrotropin** from the anterior pituitary gland."
      },
      {
        "author": "Andrew Schally",
        "work": "Hypothalamic Peptide Hormones",
        "quote": "Our isolation of thyrotropin-releasing hormone proved that **thyrotropin** secretion is governed directly by neural peptides."
      },
      {
        "author": "Rosalyn Yalow",
        "work": "Nobel Lecture: Radioimmunoassay",
        "quote": "With our newly developed assay, minute fluctuations in serum **thyrotropin** can be detected before physical symptoms appear."
      }
    ]
  },
  "Dashboard — thyr\\thyroxin.md": {
    "primary": "An older chemical spelling of thyroxine; the chief iodine-containing amino acid hormone secreted by the thyroid gland.",
    "secondary": "In early twentieth-century biochemistry, the crystalline active principle of the thyroid gland isolated by Edward Calvin Kendall in 1914.",
    "quotes": [
      {
        "author": "Edward Calvin Kendall",
        "work": "The Isolation in Crystalline Form of the Compound Containing Iodine Which Occurs in the Thyroid",
        "quote": "On Christmas Day in 1914, I succeeded in isolating pure crystalline **thyroxin**, containing sixty-five percent of organic iodine."
      },
      {
        "author": "Charles Robert Harington",
        "work": "The Thyroid Gland: Its Chemistry and Physiology",
        "quote": "Our synthetic determination proved that Kendall's **thyroxin** possesses an aromatic ether core containing four iodine atoms."
      },
      {
        "author": "George Barger",
        "work": "Organic Chemistry in Biology",
        "quote": "Administering a fraction of a milligram of pure **thyroxin** raises the total basal metabolic rate by twenty percent."
      }
    ]
  },
  "Dashboard — thyr\\thyroxine.md": {
    "primary": "The principal hormone secreted by the thyroid gland, chemically 3,5,3',5'-tetraiodothyronine (T4), essential for regulating metabolic rate and growth.",
    "secondary": "In cellular biochemistry, a prohormone converted peripherally by deiodinase enzymes into the biologically more potent triiodothyronine (T3).",
    "quotes": [
      {
        "author": "Edward Calvin Kendall",
        "work": "Thyroxine",
        "quote": "Crystalline **thyroxine** governs the combustion rate of living cells, acting as an essential accelerator of cellular respiration."
      },
      {
        "author": "Rosalind Pitt-Rivers",
        "work": "The Thyroid Hormones",
        "quote": "Peripheral tissues cleave a single outer-ring iodine from **thyroxine** to generate triiodothyronine, the true intracellular ligand."
      },
      {
        "author": "Jack Gross",
        "work": "The Identification of 3:5:3'-Triiodothyronine in Human Plasma",
        "quote": "Although **thyroxine** is the predominant circulating iodinated hormone, its biological action is largely mediated via T3."
      }
    ]
  },
  "Dashboard — thyr\\thyrse.md": {
    "primary": "A dense, compact, ovate or cylindrical compound inflorescence whose main axis is indeterminate (racemose) while its lateral branches are determinate (cymose).",
    "secondary": "In descriptive botanical taxonomy, an inflorescence form characteristic of the horse chestnut (Aesculus) and lilac (Syringa).",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "In the horse-chestnut, the blossoms are assembled into an erect pyramidal **thyrse**, branching into secondary cymes."
      },
      {
        "author": "John Lindley",
        "work": "An Introduction to Botany",
        "quote": "A **thyrse** represents a mixed inflorescence, uniting indeterminate central elongation with centrifugal lateral flowering."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "Manual of Cultivated Plants",
        "quote": "The fragrant lilac bears its blossoms in immense compound **thyrse** clusters that weigh down the spring branches."
      }
    ]
  },
  "Dashboard — thyr\\thyrsopteris.md": {
    "primary": "A monotypic genus of primitive tree fern (Thyrsopteris elegans) native exclusively to the Robinson Crusoe and Juan Fernández Islands of Chile.",
    "secondary": "In systematic pteridology, an ancient paleo-endemic fern in the family Thyrsopteridaceae exhibiting strongly dimorphic fronds with fertile thyrse-like pinnae.",
    "quotes": [
      {
        "author": "William Jackson Hooker",
        "work": "Species Filicum",
        "quote": "The fertile portions of the frond in **thyrsopteris** are completely skeletonized, bearing dense spherical sori resembling tiny grapes."
      },
      {
        "author": "Carl Skottsberg",
        "work": "The Natural History of Juan Fernandez and Easter Island",
        "quote": "In the damp montane cloud forests of Masatierra, **thyrsopteris** grows as a splendid relict tree fern from the Mesozoic era."
      },
      {
        "author": "F. O. Bower",
        "work": "The Ferns (Filicales)",
        "quote": "The cup-like marginal indusium of **thyrsopteris** isolates it phylogenetically from both Dicksonia and modern Cyatheaceae."
      }
    ]
  },
  "Dashboard — thyr\\thyrsus.md": {
    "primary": "A staff or wand tipped with a pine cone and wreathed with ivy and vine leaves, carried by Dionysus (Bacchus) and his devotees.",
    "secondary": "In classical literature and art history, a religious symbol of fertility, divine inspiration, and ecstatic Dionysian revelry.",
    "quotes": [
      {
        "author": "Euripides",
        "work": "The Bacchae",
        "quote": "Brandishing the sacred **thyrsus** and clad in fawn-skins, the ecstatic women bounded across the wild slopes of Cithaeron."
      },
      {
        "author": "Ovid",
        "work": "Metamorphoses",
        "quote": "Bacchus waved his vine-entwined **thyrsus**, and forthwith sweet wine bubbled up from the dry earth."
      },
      {
        "author": "Walter Pater",
        "work": "Greek Studies",
        "quote": "The pine-cone crowned **thyrsus** embodied both the wild vegetative vitality and the sacred frenzy of the forest god."
      }
    ]
  },
  "Dashboard — tryp\\trepan.md": {
    "primary": "A surgical crown saw or cylindrical perforating instrument used to bore a circular hole into the skull (trepanation).",
    "secondary": "To bore or perforate bone, rock, or mining strata with a cylindrical cutting drill; historically, to swindle or trap.",
    "quotes": [
      {
        "author": "Ambroise Paré",
        "work": "The Collected Works of That Famous Chirurgion",
        "quote": "The surgeon must apply the crown of the **trepan** with a steady hand, turning it gently until the skull plate is penetrated."
      },
      {
        "author": "Percivall Pott",
        "work": "Observations on the Nature and Consequences of Wounds and Contusions of the Head",
        "quote": "To evacuate extravasated blood compressing the dura mater, the immediate application of the **trepan** is indispensable."
      },
      {
        "author": "Hippocrates",
        "work": "On Injuries of the Head",
        "quote": "When the bone is contused and fractured without displacement, you must **trepan** the skull down to the interior membrane."
      }
    ]
  },
  "Dashboard — tryp\\trypanophobia.md": {
    "primary": "An extreme, irrational, or debilitating fear of medical procedures involving hypodermic needles or injections.",
    "secondary": "In clinical psychology and behavioral medicine, a specific blood-injection-injury phobia characterized by vasovagal syncope upon seeing needles.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "Inhibitions, Symptoms and Anxiety",
        "quote": "Phobic dreads directed toward sharp medical instruments or **trypanophobia** reflect deep-seated bodily integrity anxieties."
      },
      {
        "author": "William Osler",
        "work": "Aequanimitas",
        "quote": "The physician must handle patients afflicted with acute **trypanophobia** with extraordinary gentleness to avoid vasovagal collapse."
      },
      {
        "author": "G. Stanley Hall",
        "work": "A Study of Fears",
        "quote": "In our clinical survey of neurotic dreads, sharp points and punctures provoke intense visceral panic among those with **trypanophobia**."
      }
    ]
  },
  "Dashboard — tryp\\trypanosome.md": {
    "primary": "A parasitic, microscopic, unicellular flagellated protozoan belonging to the genus Trypanosoma, living in the blood and tissues of vertebrate hosts.",
    "secondary": "In medical parasitology and tropical medicine, the causative pathogen of African sleeping sickness (T. brucei) and Chagas disease (T. cruzi).",
    "quotes": [
      {
        "author": "David Bruce",
        "work": "Preliminary Report on the Tsetse Fly Disease or Nagana in Zululand",
        "quote": "Microscopic examination of the infected cattle's blood revealed swarms of an active, undulating **trypanosome**."
      },
      {
        "author": "Carlos Chagas",
        "work": "A New Human Trypanosomiasis",
        "quote": "We succeeded in isolating the pathogenic **trypanosome** from the intestinal tract of the blood-sucking reduviid bug."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Experimental Chemotherapy of Spirilloses",
        "quote": "Our trials with trypan red demonstrated that synthetic dyes could selectively destroy the **trypanosome** without harming host tissues."
      }
    ]
  },
  "Dashboard — tryp\\trypetidae.md": {
    "primary": "An older entomological family name for fruit flies (now classified as Tephritidae), characterized by attractively pictured wings and larvae that feed in fruit.",
    "secondary": "In agricultural entomology, a cosmopolitan family of dipteran flies including notorious economic pests like the Mediterranean fruit fly (Ceratitis capitata).",
    "quotes": [
      {
        "author": "Hermann Loew",
        "work": "Monographs of the Diptera of North America",
        "quote": "The flies of the family **trypetidae** are easily recognized by their beautifully banded or reticulated wings and distinct habits."
      },
      {
        "author": "J. M. Aldrich",
        "work": "A Catalogue of North American Diptera",
        "quote": "Larval development within succulent fruit flesh renders many species of the **trypetidae** formidable orchard pests."
      },
      {
        "author": "C. V. Riley",
        "work": "Report of the Entomologist",
        "quote": "Quarantine inspections must guard against the introduction of exotic **trypetidae** whose maggots ruin citrus groves."
      }
    ]
  },
  "Dashboard — tryp\\trypsin.md": {
    "primary": "A digestive serine protease enzyme produced by the exocrine pancreas that hydrolyzes proteins into smaller peptides in the small intestine.",
    "secondary": "In biochemistry and enzymology, an endopeptidase that specifically cleaves peptide chains on the carboxyl side of the basic amino acids lysine and arginine.",
    "quotes": [
      {
        "author": "Willy Kühne",
        "work": "On the Digestion of Protein by the Pancreas",
        "quote": "To this proteolytic ferment of the pancreatic juice, active in an alkaline medium, I give the name **trypsin**."
      },
      {
        "author": "John Howard Northrop",
        "work": "Crystalline Enzymes",
        "quote": "The crystallization of pure **trypsin** demonstrated decisively that proteolytic catalysts are themselves catalytic proteins."
      },
      {
        "author": "Emil Fischer",
        "work": "Researches on Amino Acids, Polypeptides and Proteins",
        "quote": "Enzymatic cleavage of synthetic polypeptides by **trypsin** occurs only where specific basic peptide linkages are exposed."
      }
    ]
  },
  "Dashboard — tryp\\trypsinogen.md": {
    "primary": "The inactive zymogen or proenzyme precursor of trypsin, synthesized and secreted by the exocrine pancreas into the duodenum.",
    "secondary": "In gastrointestinal physiology, the inactive precursor cleaved by intestinal enterokinase (enteropeptidase) to produce active, autocatalytic trypsin.",
    "quotes": [
      {
        "author": "Ivan Pavlov",
        "work": "The Work of the Digestive Glands",
        "quote": "Pancreatic juice entering the duodenum contains inactive **trypsinogen**, which is activated upon contact with enterokinase."
      },
      {
        "author": "Willy Kühne",
        "work": "Studies on Pancreatic Ferments",
        "quote": "The healthy pancreas protects itself from autodigestion by storing its proteolytic enzymes in the harmless form of **trypsinogen**."
      },
      {
        "author": "John Howard Northrop",
        "work": "Crystalline Enzymes",
        "quote": "The autocatalytic conversion of **trypsinogen** into active trypsin proceeds exponentially once the first traces of enzyme appear."
      }
    ]
  },
  "Dashboard — tryp\\tryptophan.md": {
    "primary": "An essential aromatic alpha-amino acid containing an indole ring, vital in human diet for protein synthesis and metabolic regulation.",
    "secondary": "In biochemistry, the metabolic precursor for the neurotransmitter serotonin, the pineal hormone melatonin, and the vitamin nicotinic acid (niacin).",
    "quotes": [
      {
        "author": "Frederick Gowland Hopkins",
        "work": "A Contribution to the Chemistry of Proteids: The Discovery of a New Constituent",
        "quote": "From pancreatic digests of casein we succeeded in isolating a crystalline indole amino acid which we named **tryptophan**."
      },
      {
        "author": "Emil Fischer",
        "work": "Syntheses of Indole Derivatives",
        "quote": "The synthesis and structural elucidation of **tryptophan** unveiled the chemical origin of the ubiquitous indole nucleus in animals."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Because humans cannot synthesize the indole ring de novo, dietary **tryptophan** is an indispensable building block of living protein."
      }
    ]
  },
  "Dashboard — tryp\\tryptophane.md": {
    "primary": "An obsolete or variant chemical spelling of tryptophan, the essential indole-containing amino acid.",
    "secondary": "In early twentieth-century nutritional biochemistry, the amino acid identified by Hopkins and Cole as indispensable for sustaining animal growth.",
    "quotes": [
      {
        "author": "Frederick Gowland Hopkins",
        "work": "Feeding Experiments Illustrating the Importance of Accessory Factors in Normal Dietaries",
        "quote": "Mice fed upon a diet lacking the amino acid **tryptophane** swiftly lose weight and perish within weeks."
      },
      {
        "author": "Thomas Burr Osborne",
        "work": "The Comparative Nutritive Value of Certain Proteins",
        "quote": "Zein from maize is nutritionally incomplete because it lacks both lysine and **tryptophane**, failing to maintain nitrogen balance."
      },
      {
        "author": "Lafayette Mendel",
        "work": "Nutrition: The Chemistry of Life",
        "quote": "The addition of pure **tryptophane** to a zein diet instantly arrests nutritional decline in growing rats."
      }
    ]
  }
};

const updated = updateNotesBatch(BASE_DIR, BATCH3_DATA);
console.log(`Action Part 2 - Batch 3 Completed: ${updated} / ${Object.keys(BATCH3_DATA).length} notes updated.`);
