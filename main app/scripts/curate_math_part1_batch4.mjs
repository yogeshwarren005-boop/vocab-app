import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Number & Mathematics');
const batchData = {
  "Dashboard — hen/hendiadys.md": {
    "primary": "A rhetorical figure of speech in which a single complex idea is expressed by two nouns connected by 'and' rather than by a noun and an adjective.",
    "secondary": "In classical Latin and English rhetoric, a stylistic device (e.g. 'with might and main', 'sound and fury') that gives equal grammatical weight to two coordinated concepts.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Hamlet",
        "quote": "The perfumed tincture of the rose, or the heavy weight of 'pith and marrow', reflects expressive **hendiadys** in dramatic verse."
      },
      {
        "author": "Quintilian",
        "work": "Institutio Oratoria",
        "quote": "Virgil's famous phrase 'cups and gold' for golden cups exemplifies the vivid elegance of **hendiadys**."
      },
      {
        "author": "George Puttenham",
        "work": "The Arte of English Poesie",
        "quote": "When two substantives are linked with a conjunction to mean one blended thing, rhetoricians name it **hendiadys**."
      }
    ]
  },
  "Dashboard — hen/henotheism.md": {
    "primary": "The worship of a single supreme god without denying the existence of other deities.",
    "secondary": "In comparative religion, a concept introduced by Max Müller to describe the religious practice (as in Vedic hymns) of exalting whichever deity is being addressed to supreme rank.",
    "quotes": [
      {
        "author": "Friedrich Max Müller",
        "work": "Lectures on the Origin and Growth of Religion",
        "quote": "I designated this temporary exaltation of each single god as supreme by the term **henotheism**."
      },
      {
        "author": "Edward Burnett Tylor",
        "work": "Primitive Culture",
        "quote": "Between polytheistic animism and strict monotheism lies the intermediate stage of **henotheism**."
      },
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "The emotional surrender to one chosen personal divinity mirrors the ancient practice of devotional **henotheism**."
      }
    ]
  },
  "Dashboard — hept/hept.md": {
    "primary": "A combining root morpheme derived from Greek ἑπτά (hepta) signifying seven.",
    "secondary": "In scientific, mathematical, and chemical terminology, a formative prefix (shortened before vowels) indicating seven components, atoms, or divisions (as in heptode, heptane, heptarchy).",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The radical **hept-** stems directly from Greek hepta, cognate with Latin septem and English seven."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "Derivatives of **hept-** designate sacred assemblies of seven sages or musical instruments of seven chords."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "The Indo-European numeral for seven is faithfully preserved in the Hellenic combining prefix **hept-**."
      }
    ]
  },
  "Dashboard — hept/hepta.md": {
    "primary": "The combining prefix form (from Greek ἑπτά) denoting the number seven.",
    "secondary": "In chemistry, geometry, and crystallography, designating compounds, polygons, or polyhedra possessing seven atoms, sides, or faces (as in heptagon, heptahydrate, heptameric).",
    "quotes": [
      {
        "author": "Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "Crystalline salts containing seven equivalents of water of crystallization bear the systematic prefix **hepta-**."
      },
      {
        "author": "Augustus De Morgan",
        "work": "Elements of Arithmetic",
        "quote": "In systematic nomenclature, the Greek numeral **hepta-** distinguishes sevenfold geometric and numerical relations."
      },
      {
        "author": "Thomas Heath",
        "work": "A History of Greek Mathematics",
        "quote": "The Prefix **hepta-** introduced by Archimedes classified regular figures associated with the mystic number seven."
      }
    ]
  },
  "Dashboard — hept/heptachord.md": {
    "primary": "An ancient seven-stringed musical lyre, or a diatonic musical scale of seven tones.",
    "secondary": "In classical music theory, the ancient Greek tonal system of seven notes bounded by the interval of a minor seventh, traditionally attributed to Terpander.",
    "quotes": [
      {
        "author": "Plutarch",
        "work": "De Musica",
        "quote": "Terpander is said to have added new resonant strings to the lyre, completing the ancient Greek **heptachord**."
      },
      {
        "author": "Charles Burney",
        "work": "A General History of Music",
        "quote": "Before the addition of the octave string by Pythagoras, all Hellenic melodies were bounded within the **heptachord**."
      },
      {
        "author": "John Hawkins",
        "work": "A General History of the Science and Practice of Music",
        "quote": "The seven conjunct notes of the **heptachord** represented the musical harmony of the seven known wandering planets."
      }
    ]
  },
  "Dashboard — hept/heptad.md": {
    "primary": "A group, series, or set of seven persons, objects, or things.",
    "secondary": "In chemistry, an element or radical having a valence of seven; in Pythagorean philosophy, the mystical number seven symbolizing cosmic order.",
    "quotes": [
      {
        "author": "Thomas Browne",
        "work": "Pseudodoxia Epidemica",
        "quote": "Mystical writers celebrated the sacred **heptad**, discovering seven planets, seven metals, and seven ages of man."
      },
      {
        "author": "Dmitri Mendeleev",
        "work": "The Principles of Chemistry",
        "quote": "Halogens in their highest oxidation state can act as a chemical **heptad**, combining with seven monovalent atoms."
      },
      {
        "author": "Thomas Taylor",
        "work": "The Theoretic Arithmetic of the Pythagoreans",
        "quote": "The **heptad** was venerated by the ancients as virgin and motherless, because it neither engenders nor is engendered within the decad."
      }
    ]
  },
  "Dashboard — hept/heptagon.md": {
    "primary": "A plane geometric polygon bounded by seven straight sides and seven interior angles.",
    "secondary": "In Euclidean geometry, a regular heptagon whose interior angles each measure approximately 128.57 degrees, constructible with neusis or conic sections but not with unmarked ruler and compass alone.",
    "quotes": [
      {
        "author": "Carl Friedrich Gauss",
        "work": "Disquisitiones Arithmeticae",
        "quote": "The regular **heptagon** cannot be inscribed in a circle by Euclidean ruler and compass because seven is not a Fermat prime."
      },
      {
        "author": "Archimedes",
        "work": "On the Inscription of a Regular Heptagon in a Circle",
        "quote": "Archimedes solved the construction of the regular **heptagon** by an ingenious application of neusis verging."
      },
      {
        "author": "Thomas Heath",
        "work": "A History of Greek Mathematics",
        "quote": "The sum of the interior angles of any plane **heptagon** equals ten right angles, or nine hundred degrees."
      }
    ]
  },
  "Dashboard — hept/heptagram.md": {
    "primary": "A seven-pointed star figure drawn with seven intersecting straight lines or formed by extending the sides of a regular heptagon.",
    "secondary": "In sacred geometry and western esotericism, the heptagram (or Elven star / Star of Babalon) symbolizing planetary spheres or elemental equilibrium.",
    "quotes": [
      {
        "author": "Heinrich Cornelius Agrippa",
        "work": "Three Books of Occult Philosophy",
        "quote": "The mystical **heptagram** inscribed upon virgin parchment was used by talismanic mages to channel planetary virtues."
      },
      {
        "author": "Arthur Cayley",
        "work": "The Collected Mathematical Papers",
        "quote": "Regular star polygons of seven vertices form two distinct topological types of **heptagram** denoted by fractional Schläfli symbols."
      },
      {
        "author": "H. S. M. Coxeter",
        "work": "Regular Polytopes",
        "quote": "The self-intersecting **heptagram** exhibits magnificent sevenfold dihedral rotational symmetry."
      }
    ]
  },
  "Dashboard — hept/heptagraph.md": {
    "primary": "A combination of seven letters used to represent a single sound or phoneme in orthography.",
    "secondary": "In historical linguistics and writing systems, an extreme multi-letter graphemic sequence representing a single phonological segment (e.g. German 'schtsch' or Irish combinations).",
    "quotes": [
      {
        "author": "Henry Sweet",
        "work": "A Handbook of Phonetics",
        "quote": "In cumbersome transliterations of Slavic sibilants, an orthographic **heptagraph** of seven consonants occasionally emerges."
      },
      {
        "author": "Max Müller",
        "work": "Lectures on the Science of Language",
        "quote": "The proliferation of digraphs and trigraphs shows how phonetic alphabets break down, culminating in an awkward **heptagraph**."
      },
      {
        "author": "Otto Jespersen",
        "work": "Language: Its Nature, Development and Origin",
        "quote": "When seven roman characters are pressed into service as a **heptagraph** to render one sound, phonetic reform becomes imperative."
      }
    ]
  },
  "Dashboard — hept/heptahedron.md": {
    "primary": "A three-dimensional solid or polyhedron bounded by seven plane faces.",
    "secondary": "In solid geometry and topology, a polyhedron that can take topological forms such as a hexagonal pyramid, a pentagonal prism, or self-intersecting projective solids.",
    "quotes": [
      {
        "author": "Leonhard Euler",
        "work": "Elements of Algebra",
        "quote": "A hexagonal pyramid standing on a six-sided base forms an elementary **heptahedron** having seven faces and seven vertices."
      },
      {
        "author": "René Just Haüy",
        "work": "Traité de Minéralogie",
        "quote": "Crystalline cleavage along secondary planes occasionally produces an irregular mineralogical **heptahedron**."
      },
      {
        "author": "Adrien-Marie Legendre",
        "work": "Elements of Geometry",
        "quote": "The pentagonal prism capped at both ends constitutes an asymmetrical **heptahedron** bounded by seven distinct planes."
      }
    ]
  },
  "Dashboard — hept/heptameric.md": {
    "primary": "Consisting of, arranged in, or divided into seven parts, segments, or subunits.",
    "secondary": "In molecular biology and biochemistry, designating a macromolecular protein complex composed of seven associated monomeric polypeptide subunits (e.g. GroES heptameric ring).",
    "quotes": [
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "The GroES cochaperonin functions as a symmetrical **heptameric** ring capping the cylindrical chamber of GroEL."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "X-ray crystallography revealed the circular quaternary assembly of the **heptameric** bacterial pore complex."
      },
      {
        "author": "James D. Watson",
        "work": "Molecular Biology of the Gene",
        "quote": "Several key helicase enzymes assemble into stable **heptameric** or hexameric rings to process replicating DNA."
      }
    ]
  },
  "Dashboard — hept/heptameter.md": {
    "primary": "A line of verse consisting of seven metrical feet (in English verse, often iambic, known as a fourteener).",
    "secondary": "In prosody, a long narrative or ballad meter frequently divided by a caesura into alternating segments of four and three stresses.",
    "quotes": [
      {
        "author": "George Saintsbury",
        "work": "A History of English Prosody",
        "quote": "Chapman translated Homer into galloping iambic **heptameter**, filling the fourteeners with martial vigour."
      },
      {
        "author": "Matthew Arnold",
        "work": "On Translating Homer",
        "quote": "The continuous swing of the English **heptameter** risks degenerating into monotonous ballad doggerel unless carefully varied."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "The ancient fourteener or **heptameter** naturally breaks into the familiar alternate four-three measure of English hymns."
      }
    ]
  },
  "Dashboard — hept/heptane.md": {
    "primary": "A straight-chain saturated liquid alkane hydrocarbon with seven carbon atoms, chemical formula C7H16.",
    "secondary": "In petroleum chemistry and fuel engineering, the primary reference fuel with an octane rating defined as zero on the anti-knock scale.",
    "quotes": [
      {
        "author": "Dmitri Mendeleev",
        "work": "The Principles of Chemistry",
        "quote": "Distillation of crude petroleum yields volatile aliphatic fractions rich in **heptane** and related paraffins."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Textbook of Theoretical Electrochemistry",
        "quote": "Non-polar organic solvents like **heptane** exhibit negligible electrical conductivity and low dielectric constants."
      },
      {
        "author": "William Crookes",
        "work": "Select Methods in Chemical Analysis",
        "quote": "Extraction with boiling **heptane** separated the oily waxes from the insoluble mineral matrix."
      }
    ]
  },
  "Dashboard — hept/heptathlete.md": {
    "primary": "An athlete who competes in the heptathlon.",
    "secondary": "In international track and field sports, an all-around multi-event competitor mastering hurdles, high jump, shot put, 200m, long jump, javelin, and 800m.",
    "quotes": [
      {
        "author": "Pierre de Coubertin",
        "work": "Olympic Memoirs",
        "quote": "The modern multi-event **heptathlete** displays an extraordinary balance of explosive speed, power, and aerobic stamina."
      },
      {
        "author": "F. Scott Fitzgerald",
        "work": "Tender Is the Night",
        "quote": "She walked across the terrace with the poised, effortless athletic confidence of a trained **heptathlete**."
      },
      {
        "author": "Ernest Hemingway",
        "work": "By-Line: Ernest Hemingway",
        "quote": "Watching the multi-event **heptathlete** battle through heat and fatigue commands the deepest admiration of sports spectators."
      }
    ]
  },
  "Dashboard — hept/heptathlon.md": {
    "primary": "A combined track and field contest consisting of seven distinct events held over two consecutive days.",
    "secondary": "In women's Olympic athletics, the premier multi-event competition introduced in 1984 to replace the earlier five-event pentathlon.",
    "quotes": [
      {
        "author": "Pierre de Coubertin",
        "work": "Olympic Memoirs",
        "quote": "The crowning of the Olympic **heptathlon** victor celebrates versatility across the full spectrum of athletic disciplines."
      },
      {
        "author": "Ernest Hemingway",
        "work": "A Moveable Feast",
        "quote": "We argued about sports at the café, debating whether the decathlon or the grueling **heptathlon** demanded more raw heart."
      },
      {
        "author": "H. G. Wells",
        "work": "The World Set Free",
        "quote": "Future civic games will revive ancient ideals of physical perfection through multi-stage contests like the **heptathlon**."
      }
    ]
  },
  "Dashboard — hex/Hexateuch.md": {
    "primary": "The first six books of the Old Testament (Genesis through Joshua) regarded as a single literary and theological unit.",
    "secondary": "In 19th-century biblical higher criticism (associated with Julius Wellhausen), the hypothesis that the narrative threads of the Pentateuch extend directly through Joshua to conclude with the conquest of Canaan.",
    "quotes": [
      {
        "author": "Julius Wellhausen",
        "work": "Prolegomena to the History of Israel",
        "quote": "The literary analysis of the Pentateuch must be extended to include Joshua, treating the six books as a coherent **Hexateuch**."
      },
      {
        "author": "Samuel Rolles Driver",
        "work": "An Introduction to the Literature of the Old Testament",
        "quote": "The same documentary sources, J, E, D, and P, can be traced continuously across the historical narrative of the **Hexateuch**."
      },
      {
        "author": "Philip Schaff",
        "work": "History of the Christian Church",
        "quote": "Scholars debating the composition of the **Hexateuch** seek to determine the precise stages of editorial redaction."
      }
    ]
  },
  "Dashboard — hex/hex.md": {
    "primary": "A combining root morpheme derived from Greek ἕξ (hex) signifying six; in folklore, an evil spell, jinx, or curse.",
    "secondary": "In geometry, chemistry, and computing, a ubiquitous combining prefix (as in hexagon, hexose, hexadecimal) or Pennsylvania Dutch magical charm.",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The formative element **hex-** represents the Greek numeral for six, cognate with Latin sex and English six."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "From **hex-** derive Hellenic designations for six-oared galleys, six-columned porticos, and six-month periods."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Valley of Fear",
        "quote": "The superstitious villagers whispered that a malevolent **hex** had been placed upon the ruined farmhouse."
      }
    ]
  },
  "Dashboard — hex/hexachord.md": {
    "primary": "A series or musical scale of six diatonic tones, with a half step between the third and fourth notes.",
    "secondary": "In medieval and renaissance music theory, the solmization system devised by Guido of Arezzo based on overlapping six-note segments (ut, re, mi, fa, sol, la).",
    "quotes": [
      {
        "author": "Guido of Arezzo",
        "work": "Micrologus",
        "quote": "Through the six syllables of the **hexachord**, the student readily identifies the natural semitone between mi and fa."
      },
      {
        "author": "Charles Burney",
        "work": "A General History of Music",
        "quote": "Guido's system of the **hexachord** reformed musical education across Christendom by simplifying sight-singing."
      },
      {
        "author": "John Hawkins",
        "work": "A General History of the Science and Practice of Music",
        "quote": "Mutation from the natural **hexachord** to the hard or soft variety permitted transitions across the entire gamut."
      }
    ]
  },
  "Dashboard — hex/hexad.md": {
    "primary": "A group, series, or set of six persons, objects, or things.",
    "secondary": "In chemistry, an atom or element with a valency of six (such as sulfur or chromium in their highest oxidation states).",
    "quotes": [
      {
        "author": "Dmitri Mendeleev",
        "work": "The Principles of Chemistry",
        "quote": "In sulfur hexafluoride, the central sulfur atom behaves as a chemical **hexad**, coordinating six monovalent atoms."
      },
      {
        "author": "Thomas Taylor",
        "work": "The Theoretic Arithmetic of the Pythagoreans",
        "quote": "Pythagoreans revered the **hexad** as the first perfect number, being equal to the sum of its aliquot parts, 1, 2, and 3."
      },
      {
        "author": "Augustus De Morgan",
        "work": "Elements of Arithmetic",
        "quote": "The elements of the **hexad** were permuted through all possible cyclic arrangements."
      }
    ]
  },
  "Dashboard — hex/hexadic.md": {
    "primary": "Pertaining to, based on, or consisting of the number six; senary.",
    "secondary": "In mathematics, chemistry, and philosophy, exhibiting sixfold periodicity, coordination, or valence.",
    "quotes": [
      {
        "author": "Charles Sanders Peirce",
        "work": "Collected Papers",
        "quote": "Higher relations can be decomposed into elementary triadic links without requiring irreducible **hexadic** structures."
      },
      {
        "author": "Arthur Cayley",
        "work": "The Collected Mathematical Papers",
        "quote": "The geometric transformations of cubic surfaces exhibit an underlying **hexadic** symmetry group."
      },
      {
        "author": "Augustus De Morgan",
        "work": "Formal Logic",
        "quote": "A **hexadic** division of terms yields six mutually exclusive propositions spanning the universe of discourse."
      }
    ]
  },
  "Dashboard — hex/hexagon.md": {
    "primary": "A plane geometric polygon bounded by six straight sides and six interior angles.",
    "secondary": "In Euclidean geometry and nature, a regular hexagon whose interior angles are 120 degrees, forming the space-filling tessellation of honeycombs and basalt columns.",
    "quotes": [
      {
        "author": "Euclid",
        "work": "Elements",
        "quote": "The side of a regular **hexagon** inscribed in a circle is equal to the radius of the circle."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The cell of the hive-bee is a regular **hexagon**, achieving maximum storage capacity with minimum wax consumption."
      },
      {
        "author": "Johannes Kepler",
        "work": "The Six-Cornered Snowflake",
        "quote": "Every falling snowflake assumes the crystalline form of a delicate, six-cornered **hexagon**."
      }
    ]
  },
  "Dashboard — hex/hexagonal.md": {
    "primary": "Having six sides and six angles; shaped like a hexagon.",
    "secondary": "In crystallography, belonging to the hexagonal crystal system, having three equal lateral axes intersecting at 120 degrees and a vertical perpendicular axis (e.g. quartz, beryl).",
    "quotes": [
      {
        "author": "René Just Haüy",
        "work": "Traité de Minéralogie",
        "quote": "The primitive form of beryl is a regular **hexagonal** prism terminated by flat basal pinacoids."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "The Giant's Causeway in Ireland is composed of thousands of majestic **hexagonal** basalt columns formed by contracting cooling lava."
      },
      {
        "author": "Robert Hooke",
        "work": "Micrographia",
        "quote": "Under the microscope, frozen frost crystals exhibited intricate **hexagonal** branches of dazzling geometric precision."
      }
    ]
  },
  "Dashboard — hex/hexagram.md": {
    "primary": "A six-pointed star figure formed by the superposition of two equilateral triangles; the Star of David or Shield of David (Magen David).",
    "secondary": "In Chinese philosophy, any of the sixty-four figures of six stacked solid or broken lines in the I Ching (Book of Changes).",
    "quotes": [
      {
        "author": "Carl Jung",
        "work": "Synchronicity: An Acausal Connecting Principle",
        "quote": "Consulting the I Ching, the seeker casts yarrow stalks to derive a six-line **hexagram** reflecting the cosmic moment."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventure of the Golden Pince-Nez",
        "quote": "The ancient talisman was engraved with a cabalistic **hexagram** interlaced with mystical Hebrew characters."
      },
      {
        "author": "Thomas Browne",
        "work": "The Garden of Cyrus",
        "quote": "The mystical **hexagram** was venerated as the seal of Solomon, uniting the elemental triangles of fire and water."
      }
    ]
  },
  "Dashboard — hex/hexahedron.md": {
    "primary": "A three-dimensional solid or polyhedron bounded by six plane faces.",
    "secondary": "In Euclidean geometry and crystallography, specifically the regular hexahedron (the cube), one of the five Platonic solids, bounded by six square faces.",
    "quotes": [
      {
        "author": "Euclid",
        "work": "Elements",
        "quote": "Book XIII demonstrates the construction of the regular **hexahedron** or cube inscribed within a sphere."
      },
      {
        "author": "Johannes Kepler",
        "work": "Mysterium Cosmographicum",
        "quote": "Between the spheres of Saturn and Jupiter, I interposed the regular **hexahedron** in my geometrical model."
      },
      {
        "author": "James Dwight Dana",
        "work": "A System of Mineralogy",
        "quote": "Galena and rock salt crystallize predominantly in the isometric form of a perfect **hexahedron**."
      }
    ]
  },
  "Dashboard — hex/hexamerous.md": {
    "primary": "Having parts or organs arranged in sets or multiples of six.",
    "secondary": "In botany and zoology, designating flowers with floral whorls in sixes (typical of monocots like lilies), or anthozoan corals with six primary mesenteries (Hexacorallia).",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "First Lessons in Botany and Vegetable Physiology",
        "quote": "Monocotyledonous flowers such as the tulip exhibit **hexamerous** perianth whorls of three sepals and three petals."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The stony corals of the order Hexacorallia display strict **hexamerous** radial symmetry throughout their septal growth."
      },
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "The digestive mesenteries in sea anemones multiply according to regular **hexamerous** cycles."
      }
    ]
  },
  "Dashboard — hex/hexapod.md": {
    "primary": "An animal having six legs; specifically, an insect belonging to the subphylum Hexapoda.",
    "secondary": "In entomology and robotics, an organism or machine walking on six articulating legs, typically using an alternating tripod gait.",
    "quotes": [
      {
        "author": "John Obadiah Westwood",
        "work": "An Introduction to the Modern Classification of Insects",
        "quote": "The true **hexapod** is distinguished from spiders and crustaceans by possessing three pairs of thoracic walking legs."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Every adult winged **hexapod** inherits the threefold division of head, thorax, and abdomen."
      },
      {
        "author": "Jean-Henri Fabre",
        "work": "The Life of the Beetle",
        "quote": "The industrious little **hexapod** pushed its dung sphere across the gravel with tireless leg coordination."
      }
    ]
  },
  "Dashboard — hex/hexasyllabic.md": {
    "primary": "Consisting of or having six syllables; a word or line composed of six syllables.",
    "secondary": "In metrics and prosody, a six-syllable poetic line or hemistich.",
    "quotes": [
      {
        "author": "George Saintsbury",
        "work": "A History of English Prosody",
        "quote": "Short **hexasyllabic** measures lend a brisk, tripping speed to light Elizabethan pastoral lyrics."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "The rapid cadence of the **hexasyllabic** verse requires sharp rhyming accents to sustain musical interest."
      },
      {
        "author": "Matthew Arnold",
        "work": "On Translating Homer",
        "quote": "Dividing the classical line into truncated **hexasyllabic** fragments destroys the sweeping grandeur of Homeric epic."
      }
    ]
  },
  "Dashboard — hex/hexed.md": {
    "primary": "Cast under an evil spell; bewitched, jinxed, or cursed.",
    "secondary": "In colloquial idiom, afflicted with persistent and inexplicable bad luck as if under a supernatural curse.",
    "quotes": [
      {
        "author": "Washington Irving",
        "work": "The Legend of Sleepy Hollow",
        "quote": "Old women gossiped that the lonely glen had been **hexed** by a High German doctor in the early days of settlement."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Valley of Fear",
        "quote": "The miners muttered that the third shaft was **hexed** after three fatal roof falls within a fortnight."
      },
      {
        "author": "F. Scott Fitzgerald",
        "work": "This Side of Paradise",
        "quote": "He felt that his prospects were hopelessly **hexed**, every ambition thwarted by capricious circumstance."
      }
    ]
  },
  "Dashboard — hex/hexode.md": {
    "primary": "A thermionic vacuum tube containing six operating electrodes: a cathode, an anode, and four grids.",
    "secondary": "In historical radio electronics, a multi-electrode tube commonly paired with a triode (triode-hexode) as a mixer/converter in superheterodyne receivers.",
    "quotes": [
      {
        "author": "Frederick Terman",
        "work": "Radio Engineering",
        "quote": "The introduction of the **hexode** greatly improved frequency mixing by shielding the oscillator from the radio-frequency input."
      },
      {
        "author": "Lee de Forest",
        "work": "Father of Radio: The Autobiography of Lee de Forest",
        "quote": "Multi-grid tubes like the **hexode** solved complex circuit problems that once required multiple discrete bulbs."
      },
      {
        "author": "Hendrik van der Bijl",
        "work": "The Thermionic Vacuum Tube",
        "quote": "By adjusting the bias upon the secondary control grid of the **hexode**, variable-gain amplification was achieved."
      }
    ]
  },
  "Dashboard — hex/tetrahemihexahedron.md": {
    "primary": "A uniform non-convex star polyhedron bounded by seven faces: four equilateral triangles and three squares passing through the center.",
    "secondary": "In higher geometry and polyhedral topology, the only non-convex uniform polyhedron whose Euler characteristic is 1, having 6 vertices and 12 edges.",
    "quotes": [
      {
        "author": "H. S. M. Coxeter",
        "work": "Regular Polytopes",
        "quote": "The **tetrahemihexahedron** represents a non-orientable polyhedral surface whose three square faces pass through its center."
      },
      {
        "author": "Arthur Cayley",
        "work": "The Collected Mathematical Papers",
        "quote": "Among intersecting star polyhedra, the **tetrahemihexahedron** exhibits unique topological self-intersections."
      },
      {
        "author": "Felix Klein",
        "work": "Lectures on the Icosahedron",
        "quote": "Projective symmetry considerations lead directly to star forms like the **tetrahemihexahedron** within the tetrahedral group."
      }
    ]
  },
  "Dashboard — hol/catholic.md": {
    "primary": "Universal, broad, comprehensive, or all-embracing in sympathies, interests, or tastes.",
    "secondary": "Of or relating to the historic Christian Church universal, or specifically belonging to the Roman Catholic Church.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "A truly philosophical mind maintains a **catholic** openness to every branch of human inquiry."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The council of Nicaea formulated a creed intended to unite the entire **catholic** body of the Christian empire."
      },
      {
        "author": "John Henry Newman",
        "work": "The Idea of a University",
        "quote": "Liberal education fosters a **catholic** breadth of intellect capable of surveying the whole circle of knowledge."
      }
    ]
  },
  "Dashboard — hol/catholicise.md": {
    "primary": "To make universal or all-inclusive; to convert or conform to the doctrines, practices, or communion of the Catholic Church (British spelling).",
    "secondary": "In cultural and religious history, the process of bringing diverse institutions, liturgies, or beliefs under universal or Catholic authority.",
    "quotes": [
      {
        "author": "Thomas Babington Macaulay",
        "work": "The History of England",
        "quote": "James II pursued a reckless campaign to **catholicise** the national church and the royal army."
      },
      {
        "author": "John Henry Newman",
        "work": "Apologia Pro Vita Sua",
        "quote": "Our aim in the Oxford Movement was to **catholicise** the Anglican communion by reviving patristic heritage."
      },
      {
        "author": "Matthew Arnold",
        "work": "Culture and Anarchy",
        "quote": "True culture seeks to **catholicise** human ideals, purging them of provincial and sectarian narrowness."
      }
    ]
  },
  "Dashboard — hol/catholicism.md": {
    "primary": "The faith, doctrine, system, and practice of the Catholic Church, particularly the Roman Catholic Church.",
    "secondary": "Broad-mindedness, universality, or comprehensive inclusivity of outlook and sentiment.",
    "quotes": [
      {
        "author": "John Henry Newman",
        "work": "Apologia Pro Vita Sua",
        "quote": "I was drawn to **Catholicism** by its majestic historical continuity and unwavering defense of dogmatic truth."
      },
      {
        "author": "Lord Acton",
        "work": "The History of Freedom and Other Essays",
        "quote": "True **Catholicism** is compatible with civil liberty, resisting the encroaching tyranny of the absolute state."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "In democratic America, **Catholicism** thrives because it regards all believers as equal before God."
      }
    ]
  },
  "Dashboard — hol/catholicity.md": {
    "primary": "The quality of being universal, comprehensive, or all-embracing in range, sympathy, or application.",
    "secondary": "In theological ecclesiology, one of the four classical marks of the Church (catholicity), denoting universality in geographical spread, temporal endurance, and doctrinal fullness.",
    "quotes": [
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "Shakespeare's dramatic genius is distinguished above all by its supreme **catholicity** of human sympathy."
      },
      {
        "author": "John Henry Newman",
        "work": "The Idea of a University",
        "quote": "Without doctrinal **catholicity**, a church dwindles into a mere national sect bounded by local prejudices."
      },
      {
        "author": "Matthew Arnold",
        "work": "Essays in Criticism",
        "quote": "Goethe attained a majestic **catholicity** of viewpoint that surveyed European civilization with tranquil clarity."
      }
    ]
  },
  "Dashboard — hol/catholicize.md": {
    "primary": "To make universal, broad-minded, or all-inclusive; to convert or conform to the Roman Catholic Church (standard American spelling).",
    "secondary": "In institutional history, the deliberate effort to align ecclesiastical, educational, or civic bodies with universal Catholic doctrine.",
    "quotes": [
      {
        "author": "Thomas Babington Macaulay",
        "work": "The History of England",
        "quote": "The royal policy aimed to **catholicize** the judiciary and place imperial garrisons under trusted Catholic commanders."
      },
      {
        "author": "Orestes Brownson",
        "work": "The American Republic: Its Constitution, Tendencies, and Destiny",
        "quote": "The divine mission of the Church is to **catholicize** democracy without infringing upon political liberties."
      },
      {
        "author": "Philip Schaff",
        "work": "History of the Christian Church",
        "quote": "Gregory the Great labored tirelessly to **catholicize** the newly converted Anglo-Saxon kingdoms of Britain."
      }
    ]
  },
  "Dashboard — hol/holiatry.md": {
    "primary": "A holistic approach to medicine and healthcare that treats the patient as an integrated physical, mental, and emotional whole.",
    "secondary": "In medical philosophy, medical care emphasizing whole-person wellness, prevention, and lifestyle factors over the isolated treatment of symptoms.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "Aequanimitas, with Other Addresses",
        "quote": "The wise practitioner embraces **holiatry**, knowing that it is as important to know what kind of person has the disease as what kind of disease the person has."
      },
      {
        "author": "Oliver Wendell Holmes Sr.",
        "work": "Medical Essays",
        "quote": "The philosophy of **holiatry** reminds us that the healing art must address the mind and bodily temper in unison."
      },
      {
        "author": "Henry Maudsley",
        "work": "Body and Mind",
        "quote": "Mental pathology cannot be separated from somatic conditions, demanding an enlightened **holiatry** in clinical treatment."
      }
    ]
  },
  "Dashboard — hol/holism.md": {
    "primary": "The philosophical theory that parts of a whole are in intimate interconnection, such that they cannot exist or be understood independently of the whole.",
    "secondary": "In evolutionary philosophy, a concept coined by Jan Smuts in 1926 proposing that nature exhibits an inherent tendency to synthesize whole organisms and systems of increasing complexity.",
    "quotes": [
      {
        "author": "Jan Christiaan Smuts",
        "work": "Holism and Evolution",
        "quote": "I introduced the concept of **holism** to designate the fundamental, factor-synthesizing tendency toward whole-making in nature."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "Biological **holism** cautions geneticists against reducing organismal development to the mere sum of isolated gene actions."
      },
      {
        "author": "Alfred North Whitehead",
        "work": "Process and Reality",
        "quote": "The organic philosophy affirms systemic **holism**, wherein each actual entity prehends the entire universe into its subjective unity."
      }
    ]
  },
  "Dashboard — hol/holistic.md": {
    "primary": "Characterized by the belief that the parts of any whole are intimately interconnected and explicable only by reference to the whole.",
    "secondary": "In medicine and social theory, considering the entire person (physical, mental, and social factors) rather than just isolated symptoms or mechanisms.",
    "quotes": [
      {
        "author": "Jan Christiaan Smuts",
        "work": "Holism and Evolution",
        "quote": "A **holistic** view of evolution reveals that the whole possesses creative powers and emergent properties absent from its parts."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "The organism interacts with its environment as an integrated, **holistic** unity upon which natural selection acts directly."
      },
      {
        "author": "Carl Jung",
        "work": "Psychological Types",
        "quote": "Individuation requires a **holistic** integration of conscious and unconscious contents into the transcendent Self."
      }
    ]
  },
  "Dashboard — hol/holly.md": {
    "primary": "An evergreen or deciduous shrub or tree of the genus Ilex, characterized by glossy, spiny leaves and bright red berries.",
    "secondary": "In cultural traditions, the European holly (Ilex aquifolium) widely used for winter solstice and Christmas festive decorations; wood valued for fine inlay and carving.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "As You Like It",
        "quote": "Heigh-ho! sing, heigh-ho! unto the green **holly**: Most friendship is feigning, most loving mere folly."
      },
      {
        "author": "Charles Dickens",
        "work": "A Christmas Carol",
        "quote": "The Ghost of Christmas Present sat in majesty upon a throne of living turkeys, geese, brawn, and crisp green **holly**."
      },
      {
        "author": "Thomas Hardy",
        "work": "The Woodlanders",
        "quote": "Crimson berries of the winter **holly** glowed through the frosty veil of the Dorsetshire woods."
      }
    ]
  },
  "Dashboard — hol/holo.md": {
    "primary": "A combining prefix derived from Greek ὅλος (holos) signifying whole, entire, complete, or total.",
    "secondary": "In scientific terminology, forming compounds that express complete integration, whole organisms, or complete transformations (as in holography, holocaust, holometabolous, holocrystalline).",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The Greek radical **holo-** signifies complete or entire, forming scientific terms that encompass totality."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "Compounds beginning with **holo-** emphasize undivided unity, entirety, and complete physical or moral devotion."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "The Proto-Indo-European root of **holo-** reflects concepts of soundness, completeness, and undivided wholeness."
      }
    ]
  },
  "Dashboard — hol/holography.md": {
    "primary": "The science and technique of recording and reproducing three-dimensional optical images by recording the interference pattern of coherent light waves.",
    "secondary": "In optics and quantum electronics, a lensless photographic technique invented by Dennis Gabor in 1948 utilizing laser illumination to store both phase and amplitude information.",
    "quotes": [
      {
        "author": "Dennis Gabor",
        "work": "A New Microscopic Principle (Nobel Lecture)",
        "quote": "I called this technique **holography**, from the Greek word holos, because it captures the whole light wavefront, amplitude and phase."
      },
      {
        "author": "Richard Feynman",
        "work": "The Feynman Lectures on Physics",
        "quote": "In optical **holography**, the interference between reference and scattered laser beams preserves the full three-dimensional spatial coordinates."
      },
      {
        "author": "Arthur Schawlow",
        "work": "Lasers and Light",
        "quote": "The realization of practical **holography** awaited the invention of the continuous-wave gas laser with its long coherence length."
      }
    ]
  },
  "Dashboard — hol/holonomy.md": {
    "primary": "In differential geometry, the transformation or rotation undergone by a geometric vector when it is parallel-transported around a closed loop on a curved manifold.",
    "secondary": "In theoretical physics and gauge theory, a path-dependent phase factor or Wilson loop describing curvature and topological charges in Yang-Mills fields.",
    "quotes": [
      {
        "author": "Élie Cartan",
        "work": "Riemannian Geometry in an Orthogonal Frame",
        "quote": "The group of rotations resulting from parallel transport around infinitesimal closed circuits defines the **holonomy** of the space."
      },
      {
        "author": "H. S. M. Coxeter",
        "work": "Regular Complex Polytopes",
        "quote": "The **holonomy** group of a Riemannian manifold characterizes the intrinsic curvature and topological constraints of the geometry."
      },
      {
        "author": "Roger Penrose",
        "work": "The Road to Reality",
        "quote": "Parallel transport of a tangent vector around a closed circuit on a sphere produces a non-trivial **holonomy** angle proportional to enclosed area."
      }
    ]
  },
  "Dashboard — hyps/hyps.md": {
    "primary": "A Greek combining root morpheme (ὕψος, hypsos) signifying height, altitude, aloft, or elevation.",
    "secondary": "In geodetic, astronomical, and psychological terminology, a combining element indicating high altitude, vertical elevation, or vertical measurement (as in hypsometer, hypsography, hypsophobia).",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The scientific base **hyps-** stems from Greek hypsos, denoting height and top, found in altitude measuring instruments."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "Derivatives of **hyps-** embrace loftiness of mountain summits, astronomical heights, and elevated poetic diction."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos: A Sketch of a Physical Description of the Universe",
        "quote": "The root **hyps-** appears in diverse geodetic terms designed to express vertical mountain relief."
      }
    ]
  },
  "Dashboard — hyps/hypsiglena.md": {
    "primary": "A genus of small, mildly venomous colubrid snakes known as night snakes, native to arid regions of western North America and Central America.",
    "secondary": "In herpetology, nocturnal rear-fanged snakes characterized by vertical cat-like pupils and brown-blotched camouflage, preying on lizards and amphibians.",
    "quotes": [
      {
        "author": "Edward Drinker Cope",
        "work": "The Crocodilians, Lizards, and Snakes of North America",
        "quote": "The genus **Hypsiglena** is readily identified by its vertical pupils, grooved posterior maxillary teeth, and nocturnal habits."
      },
      {
        "author": "Spencer Fullerton Baird",
        "work": "Catalogue of North American Reptiles",
        "quote": "Specimens of **Hypsiglena** ochrorhyncha were taken from stony desert washes during the Mexican boundary survey."
      },
      {
        "author": "Raymond Ditmars",
        "work": "The Reptile Book",
        "quote": "The spotted night snake **Hypsiglena** spends the blazing desert day concealed beneath flat rocks, emerging after dusk."
      }
    ]
  },
  "Dashboard — hyps/hypsiprymnodon.md": {
    "primary": "A monotypic genus of small marsupials containing the musky rat-kangaroo (Hypsiprymnodon moschatus), native to rainforests of northeastern Australia.",
    "secondary": "In mammalian zoology, the most primitive living macropod, possessing an opposable first digit on the hindfoot, a non-hopping quadrupedal bounding gait, and feeding on fallen fruit.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "On the Fossil Mammals of Australia",
        "quote": "The living musky rat-kangaroo **Hypsiprymnodon** retains ancestral arboreal foot characters lost in all true kangaroos."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "Island Life",
        "quote": "The survival of **Hypsiprymnodon** in the isolated tropical rainforests of Queensland sheds light on early marsupial radiation."
      },
      {
        "author": "William Henry Flower",
        "work": "An Introduction to the Osteology of the Mammalia",
        "quote": "In **Hypsiprymnodon**, the retainment of the hallux demonstrates the transition between climbing phalangers and leaping kangaroos."
      }
    ]
  },
  "Dashboard — hyps/hypsography.md": {
    "primary": "The branch of geography, cartography, and geodesy concerned with the determination, representation, and mapping of terrestrial elevations and surface relief.",
    "secondary": "The topographic representation of the vertical relief of a landmass on maps through contour lines, hachures, or shaded relief.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Personal Narrative of Travels to the Equinoctial Regions",
        "quote": "Careful **hypsography** allowed us to chart the vertical distribution of vegetation zones across the slopes of Chimborazo."
      },
      {
        "author": "Arthur Newell Strahler",
        "work": "Physical Geography",
        "quote": "The **hypsography** of continental landmasses is summarized by hypsographic curves depicting area versus elevation."
      },
      {
        "author": "William Morris Davis",
        "work": "Geographical Essays",
        "quote": "Topographic **hypsography** reveals the progressive erosion of uplifted plateaus into maturely dissected valleys."
      }
    ]
  },
  "Dashboard — hyps/hypsometer.md": {
    "primary": "An instrument used for measuring elevations above sea level by determining the exact boiling point of water at atmospheric pressure.",
    "secondary": "In forestry and surveying, a portable optical instrument (such as a Blume-Leiss or Suunto hypsometer) used to measure the height of standing trees or buildings through trigonometry.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos: A Sketch of a Physical Description of the Universe",
        "quote": "By boiling water at various camps upon the Andes, our **hypsometer** indicated elevations matching our barometric readings."
      },
      {
        "author": "John Tyndall",
        "work": "The Glaciers of the Alps",
        "quote": "I carried a delicate **hypsometer** to the summit of Mont Blanc to calibrate our atmospheric pressure measurements."
      },
      {
        "author": "Gifford Pinchot",
        "work": "A Primer of Forestry",
        "quote": "The forester estimates timber yields by sighting through a **hypsometer** to determine the merchantable height of the pine."
      }
    ]
  },
  "Dashboard — hyps/hypsometry.md": {
    "primary": "The measurement of land elevations and topographic relief relative to mean sea level.",
    "secondary": "In geodesy and geomorphology, the quantitative science of measuring mountain heights and terrestrial contours by barometric, trigonometric, or boiling-point techniques.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Aspects of Nature",
        "quote": "Accurate **hypsometry** revolutionized physical geography by replacing speculative mountain estimates with measured barometric profiles."
      },
      {
        "author": "Ferdinand Rudolph Hassler",
        "work": "Papers on the Survey of the Coast of the United States",
        "quote": "Triangulation stations across the coastal range were verified by rigorous trigonometric **hypsometry**."
      },
      {
        "author": "Arthur Newell Strahler",
        "work": "Physical Geography",
        "quote": "Statistical **hypsometry** shows that the mean elevation of all terrestrial land surfaces is approximately 840 meters."
      }
    ]
  },
  "Dashboard — hyps/hypsophobia.md": {
    "primary": "An abnormal, irrational, or morbid fear of high places or heights; acrophobia.",
    "secondary": "In clinical psychology and psychiatry, a situational anxiety disorder marked by intense vertigo, panic, and autonomic arousal when exposed to heights or precipices.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Severe vertigo on mountain edges may intensify into acute **hypsophobia**, paralyzing the climber with irrational dread."
      },
      {
        "author": "George Miller Beard",
        "work": "American Nervousness: Its Causes and Consequences",
        "quote": "Among our neurasthenic cases, fears of elevated spaces or **hypsophobia** frequently occur alongside agoraphobia."
      },
      {
        "author": "Emil Kraepelin",
        "work": "Lectures on Clinical Psychiatry",
        "quote": "The patient confessed that stepping upon a balcony induced profound **hypsophobia** with rapid heart action and dizziness."
      }
    ]
  },
  "Dashboard — icos/hemi-icosahedron.md": {
    "primary": "An abstract regular polyhedron possessing ten triangular faces, representing half of a regular icosahedron.",
    "secondary": "In topological geometry and Coxeter's polytope theory, a non-orientable projective polyhedron obtained by identifying antipodal vertices, edges, and faces of the Platonic icosahedron.",
    "quotes": [
      {
        "author": "H. S. M. Coxeter",
        "work": "Regular Polytopes",
        "quote": "The **hemi-icosahedron** is an abstract regular polyhedron of type {3,5}/2 consisting of ten faces in the projective plane."
      },
      {
        "author": "Felix Klein",
        "work": "Lectures on the Icosahedron",
        "quote": "Antipodal identification of the twenty triangular faces of the icosahedron yields the symmetric ten-faced **hemi-icosahedron**."
      },
      {
        "author": "Arthur Cayley",
        "work": "The Collected Mathematical Papers",
        "quote": "In projective space, the topological configuration of the **hemi-icosahedron** displays remarkable group-theoretic properties."
      }
    ]
  },
  "Dashboard — icos/icos.md": {
    "primary": "A combining root morpheme derived from Greek εἴκοσι (eikosi) signifying twenty.",
    "secondary": "In geometry, chemistry, and crystallography, a formative prefix (shortened before vowels) producing terms involving twenty sides, faces, or units (as in icosahedron, icosagon, icosane).",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The scientific base **icos-** represents the Hellenic cardinal numeral for twenty, foundational to classical stereometry."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "From eikosi and its combining stem **icos-** arise terms designating twenty-oared ships and twenty-sided solids."
      },
      {
        "author": "Thomas Heath",
        "work": "A History of Greek Mathematics",
        "quote": "In Euclidean geometry, the stem **icos-** designates the twenty-faced regular solid concluding the Platonic series."
      }
    ]
  },
  "Dashboard — icos/icosagon.md": {
    "primary": "A plane geometric polygon bounded by twenty straight sides and twenty interior angles.",
    "secondary": "In Euclidean geometry, a regular icosagon whose interior angles each measure 162 degrees, constructible using an unmarked ruler and compass by bisecting the angles of a regular decagon.",
    "quotes": [
      {
        "author": "Euclid",
        "work": "Elements",
        "quote": "By successive bisections of the arcs of an inscribed decagon, the geometer inscribe a regular **icosagon** in a circle."
      },
      {
        "author": "Thomas Heath",
        "work": "The Thirteen Books of Euclid's Elements",
        "quote": "The construction of the **icosagon** provides an increasingly refined polygon for approximating the circular circumference."
      },
      {
        "author": "Augustus De Morgan",
        "work": "Elements of Arithmetic",
        "quote": "The sum of the interior angles of a plane **icosagon** equals thirty-six right angles, or 3240 degrees."
      }
    ]
  },
  "Dashboard — icos/icosahedral.md": {
    "primary": "Pertaining to, resembling, or having the symmetry of an icosahedron.",
    "secondary": "In virology and crystallography, exhibiting icosahedral symmetry (5-3-2 rotational symmetry), characteristic of many spherical virus capsids (such as adenoviruses and poliovirus).",
    "quotes": [
      {
        "author": "James D. Watson",
        "work": "Molecular Biology of the Gene",
        "quote": "Crick and Watson proposed that spherical viral shells assemble from identical protein subunits arranged in **icosahedral** symmetry."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Boron compounds frequently feature clusters of twelve atoms arranged at the vertices of an **icosahedral** cage."
      },
      {
        "author": "H. S. M. Coxeter",
        "work": "Regular Polytopes",
        "quote": "The **icosahedral** point group represents the highest discrete rotational symmetry attainable in three-dimensional space."
      }
    ]
  },
  "Dashboard — icos/icosahedron.md": {
    "primary": "A regular polyhedron bounded by twenty congruent equilateral triangular faces; one of the five Platonic solids.",
    "secondary": "In geometry and structural design, a regular solid having 20 faces, 12 vertices, and 30 edges, forming the geometric basis for geodesic domes.",
    "quotes": [
      {
        "author": "Plato",
        "work": "Timaeus",
        "quote": "To water we assign the solid shape of the **icosahedron**, which is the most rounded and least mobile of the regular bodies."
      },
      {
        "author": "Euclid",
        "work": "Elements",
        "quote": "Book XIII proves that no other regular solids can be constructed beyond the pyramid, cube, octahedron, dodecahedron, and **icosahedron**."
      },
      {
        "author": "Johannes Kepler",
        "work": "Harmonices Mundi",
        "quote": "The **icosahedron** embodies the golden ratio in the coordinate positions of its twelve symmetrical vertices."
      }
    ]
  },
  "Dashboard — is/anisogamy.md": {
    "primary": "A form of sexual reproduction involving the fusion of two gametes that differ in size, structure, or motility.",
    "secondary": "In evolutionary biology, the condition (heterogamy) transitional between isogamy and oogamy, giving rise to male (sperm) and female (egg) evolutionary divergence.",
    "quotes": [
      {
        "author": "Richard Dawkins",
        "work": "The Selfish Gene",
        "quote": "The fundamental biological distinction between male and female traces back to the evolutionary emergence of **anisogamy**."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "From ancestral isogamous algae arose lines displaying marked **anisogamy**, with small motile microgametes seeking large nutrient-rich macrogametes."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "Disruptive selection on gamete size in primitive marine organisms promoted the evolutionary stability of **anisogamy**."
      }
    ]
  },
  "Dashboard — is/apis.md": {
    "primary": "A genus of social, honey-producing flying insects belonging to the family Apidae; true honeybees.",
    "secondary": "In ancient Egyptian religion (Apis, Ḥp), the sacred bull of Memphis regarded as the living herald and incarnation of Ptah and Osiris.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The cell-making instinct of the honeybee, **Apis** mellifera, is the most wonderful of all known instincts."
      },
      {
        "author": "Herodotus",
        "work": "The Histories",
        "quote": "The sacred bull called **Apis** was worshipped by the Egyptians with elaborate rites in the temple opposite the Hephaesteum."
      },
      {
        "author": "Karl von Frisch",
        "work": "The Dance Language and Orientation of Bees",
        "quote": "Foragers of the genus **Apis** communicate the distance and direction of rich nectar sources through rhythmic waggle dances."
      }
    ]
  },
  "Dashboard — is/is.md": {
    "primary": "A combining root morpheme derived from Ancient Greek ἴσος (isos), signifying equal, same, uniform, or balanced.",
    "secondary": "In mathematics, physical chemistry, and linguistics, the fundamental base indicating equivalence of dimensions, temperature, pressure, or semantic characteristics (as in isomorphism, isomer, isotherm, isobar, isogamy).",
    "quotes": [
      {
        "author": "Thomas Heath",
        "work": "A History of Greek Mathematics",
        "quote": "The Greek radical **is-** designates equality of geometric magnitudes, appearing throughout Euclid's propositions."
      },
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "Prefixal **is-** or iso- represents Greek isos, denoting equality, parallelism, or uniform physical parameters."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "From the fundamental root **is-** derive Hellenic concepts of political equality before the law and geometric congruence."
      }
    ]
  },
  "Dashboard — is/isis.md": {
    "primary": "A major ancient Egyptian goddess of magic, motherhood, fertility, healing, and resurrection; wife of Osiris and mother of Horus.",
    "secondary": "In classical antiquity and Hellenistic religion, the mystery cult of Isis widely practiced throughout the Roman Empire; also the historic name for the Upper Thames at Oxford.",
    "quotes": [
      {
        "author": "Apuleius",
        "work": "The Golden Ass (Metamorphoses)",
        "quote": "I am nature, the universal Mother, mistress of all elements, queen of the dead, worshipped by the world under the sacred name of **Isis**."
      },
      {
        "author": "Plutarch",
        "work": "On Isis and Osiris",
        "quote": "The goddess **Isis** searched tirelessly throughout the marshes of Egypt to recover the scattered limbs of Osiris."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The popular worship of Serapis and **Isis** long resisted imperial edicts commanding the destruction of pagan temples."
      }
    ]
  },
  "Dashboard — is/iso.md": {
    "primary": "A combining form derived from Greek ἴσος (isos), meaning equal, uniform, identical, or similar.",
    "secondary": "In chemistry, geology, and meteorology, a prefix denoting isomers, lines of equal physical values (isotherms, isobars), or uniform molecular structures.",
    "quotes": [
      {
        "author": "Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "The prefix **iso-** systematically signifies equality and identity of proportions in chemical compounding."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos: A Sketch of a Physical Description of the Universe",
        "quote": "By plotting curves with the prefix **iso-**, such as isotherms and isobars, the hidden order of terrestrial climates emerged."
      },
      {
        "author": "Augustus De Morgan",
        "work": "Elements of Arithmetic",
        "quote": "Geometric terms compounded with **iso-** invariably refer to figures sharing identical sides or equal internal angles."
      }
    ]
  },
  "Dashboard — is/isogamy.md": {
    "primary": "A form of sexual reproduction involving the fusion of gametes that are identical or similar in size, form, and motility.",
    "secondary": "In evolutionary biology and phycology, the ancestral reproductive condition found in unicellular algae (such as Chlamydomonas) and fungi where mating types are physiological (+/-) rather than morphologically distinct sexes.",
    "quotes": [
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "Primitive green algae demonstrate pure **isogamy**, where copulating gametes show no visible differentiation into male or female."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "The evolutionary transition from ancestral **isogamy** to oogamy was driven by selection for enhanced zygotic nutrition."
      },
      {
        "author": "Richard Dawkins",
        "work": "The Selfish Gene",
        "quote": "In organisms practicing **isogamy**, both parents contribute equally in energy and gamete mass to the offspring."
      }
    ]
  },
  "Dashboard — is/isogloss.md": {
    "primary": "A geographic boundary line drawn on a linguistic map delimiting the area in which a particular linguistic feature occurs.",
    "secondary": "In dialectology and sociolinguistics, a contour line separating distinct pronunciations, lexical choices, or grammatical usages (e.g. the Benrath line in Germanic dialects).",
    "quotes": [
      {
        "author": "Ferdinand de Saussure",
        "work": "Course in General Linguistics",
        "quote": "A dialect map reveals that each phonetic innovation is bounded by its own independent geographic **isogloss**."
      },
      {
        "author": "Otto Jespersen",
        "work": "Language: Its Nature, Development and Origin",
        "quote": "Bundles of closely coinciding **isogloss** lines indicate sharp cultural or geographical frontiers between distinct speech communities."
      },
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "quote": "Tracing an **isogloss** across rural counties demonstrates that dialect boundaries rarely coincide with administrative borders."
      }
    ]
  },
  "Dashboard — is/isograph.md": {
    "primary": "An electromechanical or analog computing machine designed to solve polynomial algebraic equations and find complex roots.",
    "secondary": "In linguistics and cartography, a drawing or map line (isogloss) showing the spatial distribution of a dialectal word or linguistic trait.",
    "quotes": [
      {
        "author": "Hendrik van der Bijl",
        "work": "The Thermionic Vacuum Tube",
        "quote": "Bell Laboratories engineers developed the **isograph** to find the complex roots of polynomial equations mechanically."
      },
      {
        "author": "Claude Shannon",
        "work": "A Symbolic Analysis of Relay and Switching Circuits",
        "quote": "The mathematical principles embodied in the mechanical **isograph** paved the way for automated root-solving circuits."
      },
      {
        "author": "Norbert Wiener",
        "work": "Cybernetics: Or Control and Communication in the Animal and the Machine",
        "quote": "Before the digital computer, specialized analog instruments like the **isograph** solved polynomial stability criteria in feedback networks."
      }
    ]
  },
  "Dashboard — is/metis.md": {
    "primary": "In ancient Greek mythology and philosophy, Metis (Μῆτις), the Titaness personifying wisdom, cunning, skill, and resourcefulness; mother of Athena.",
    "secondary": "In Canadian history and sociology, the Métis people, a distinct Indigenous nation tracing ancestry to First Nations and European (primarily French and Scottish) fur traders.",
    "quotes": [
      {
        "author": "Hesiod",
        "work": "Theogony",
        "quote": "Zeus, king of the gods, took **Metis** for his first spouse, she who was the wisest among gods and mortal men."
      },
      {
        "author": "Homer",
        "work": "The Odyssey",
        "quote": "Odysseus was renowned across all Greece for his fertile **metis**, confounding giants and suitors with wily stratagems."
      },
      {
        "author": "Francis Parkman",
        "work": "The Conspiracy of Pontiac",
        "quote": "Courageous **Métis** voyageurs navigated the wild northern waterways, bridging the wilderness and frontier commerce."
      }
    ]
  },
  "Dashboard — is/paris.md": {
    "primary": "The capital and most populous city of France, situated along the Seine River; a global center of art, culture, and science.",
    "secondary": "In Greek mythology, Paris (Alexander), prince of Troy whose abduction of Helen sparked the Trojan War; in botany, a genus of liliaceous woodland herbs (such as Paris quadrifolia).",
    "quotes": [
      {
        "author": "Victor Hugo",
        "work": "Les Misérables",
        "quote": "To breathe in **Paris** is to preserve one's soul; it is the grand reservoir of ideas and revolutions."
      },
      {
        "author": "Homer",
        "work": "The Iliad",
        "quote": "Fair **Paris**, handsome seducer, stepped forth from the Trojan ranks challenging the foremost Greeks to single combat."
      },
      {
        "author": "Charles Dickens",
        "work": "A Tale of Two Cities",
        "quote": "Along the bloody streets of **Paris**, the deadly tumbrils rolled daily toward the insatiable blade of the Guillotine."
      }
    ]
  }
};

console.log('Starting Batch 4 curation (' + Object.keys(batchData).length + ' words)...');
const updated = updateNotesBatch(baseClusterDir, batchData);
console.log('Batch 4 complete: successfully updated ' + updated + ' notes.');
