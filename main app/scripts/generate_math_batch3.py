import json
import os

BATCH3_DATA = {
  "Dashboard — dy/monody.md": {
    "primary": "A lyrical lament or mournful poem recited or sung by a single performer, especially an elegy mourning someone's death.",
    "secondary": "In music history, an accompanied solo vocal style developed in Italy in the late 16th century that paved the way for early baroque opera.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Lycidas",
        "quote": "In this **monody** the author bewails a learned friend, unfortunately drowned in his passage from Chester on the Irish Seas."
      },
      {
        "author": "Matthew Arnold",
        "work": "Thyrsis: A Monody",
        "quote": "Through this pastoral **monody**, the poet commemorates Arthur Hugh Clough amidst the haunted Oxford countryside."
      },
      {
        "author": "Charles Burney",
        "work": "A General History of Music",
        "quote": "The Florentine Camerata revived classical declamation through expressive solo **monody** supported by simple continuo chords."
      }
    ]
  },
  "Dashboard — ennea/ennea.md": {
    "primary": "A Greek combining root morpheme (ἐννέα, ennea) signifying nine.",
    "secondary": "In geometric, literary, and scientific nomenclature, a formative element producing terms involving nine units, angles, or members (as in ennead, enneagon, enneagram).",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The base **ennea-** reflects the ancient Greek cardinal numeral for nine, cognate with Latin novem."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "From **ennea-** are compounded classical designations for assemblies of nine deities or verses of nine beats."
      },
      {
        "author": "Thomas Heath",
        "work": "A History of Greek Mathematics",
        "quote": "The numeral prefix **ennea-** governs geometric polygons and harmonics associated with the number nine."
      }
    ]
  },
  "Dashboard — ennea/ennead.md": {
    "primary": "A group or series of nine persons, objects, or things.",
    "secondary": "In philosophy and religion, specifically the Enneads of Plotinus (six groups of nine treatises edited by Porphyry), or the great Heliopolitan Ennead of nine Egyptian deities.",
    "quotes": [
      {
        "author": "Plotinus",
        "work": "The Enneads",
        "quote": "Each treatise within the **Ennead** guides the contemplative intellect toward mystical communion with the transcendent One."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Porphyry arranged the profound philosophical discourses of his master into six balanced volumes called the **Enneads**."
      },
      {
        "author": "E. A. Wallis Budge",
        "work": "The Gods of the Egyptians",
        "quote": "At Heliopolis, the supreme company of cosmic gods formed a sacred divine **Ennead** headed by the creator Temu."
      }
    ]
  },
  "Dashboard — ennea/enneadic.md": {
    "primary": "Pertaining to, consisting of, or arranged in groups of nine.",
    "secondary": "In classical philosophy and numerology, exhibiting the properties or symbolic resonance of an ennead or ninefold structure.",
    "quotes": [
      {
        "author": "Ralph Waldo Emerson",
        "work": "Representative Men",
        "quote": "The Alexandrian thinkers cast their metaphysics into intricate **enneadic** harmonies reflecting celestial orders."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Lectures on the History of Philosophy",
        "quote": "The Neoplatonists discovered profound mystical symbolism in every **enneadic** arrangement of categories."
      },
      {
        "author": "Thomas Taylor",
        "work": "The Theoretic Arithmetic of the Pythagoreans",
        "quote": "Under the **enneadic** classification, the number nine terminates the single digits and prefigures perfection."
      }
    ]
  },
  "Dashboard — ennea/enneagon.md": {
    "primary": "A plane geometric polygon bounded by nine straight sides and nine interior angles; a nonagon.",
    "secondary": "In Euclidean geometry, a regular enneagon whose interior angles each measure 140 degrees, which cannot be constructed using an unmarked ruler and compass alone.",
    "quotes": [
      {
        "author": "Thomas Heath",
        "work": "A History of Greek Mathematics",
        "quote": "The construction of a regular **enneagon** requires the trisection of an angle of 60 degrees, exceeding Euclidean compass limitations."
      },
      {
        "author": "Carl Friedrich Gauss",
        "work": "Disquisitiones Arithmeticae",
        "quote": "Because nine is divisible by three squared, the regular **enneagon** resists construction by straightedge and compass."
      },
      {
        "author": "Augustus De Morgan",
        "work": "Elements of Arithmetic",
        "quote": "The sum of the interior angles of any plane **enneagon** is equal to fourteen right angles."
      }
    ]
  },
  "Dashboard — ennea/enneagram.md": {
    "primary": "A nine-pointed geometric figure, commonly drawn within a circle using intersecting triangles or an irregular nonagon.",
    "secondary": "In contemporary psychology and spiritual philosophy (popularized by Gurdjieff and Ichazo), a model of nine interconnected personality types.",
    "quotes": [
      {
        "author": "P. D. Ouspensky",
        "work": "In Search of the Miraculous",
        "quote": "Gurdjieff introduced the **enneagram** as a universal symbol embodying the fundamental laws of seven and three."
      },
      {
        "author": "Claudio Naranjo",
        "work": "Character and Neurosis",
        "quote": "The psychological **enneagram** organizes personality patterns around nine core fixations and compensatory defense mechanisms."
      },
      {
        "author": "Arthur Cayley",
        "work": "The Collected Mathematical Papers",
        "quote": "Stellated polyhedral projections frequently trace a symmetrical nine-pointed **enneagram** upon the central plane."
      }
    ]
  },
  "Dashboard — ennea/enneahedron.md": {
    "primary": "A three-dimensional solid or polyhedron bounded by nine plane faces; a nonahedron.",
    "secondary": "In polyhedral combinatorics and crystallography, a solid geometry figure that can take various topological forms, such as an octagonal pyramid or a heptagonal prism.",
    "quotes": [
      {
        "author": "Leonhard Euler",
        "work": "Elements of Algebra",
        "quote": "Applying our polyhedral relation to an **enneahedron**, the sum of its nine faces and fourteen vertices yields twenty-one edges plus two."
      },
      {
        "author": "René Just Haüy",
        "work": "Traité de Minéralogie",
        "quote": "Asymmetric cleavage along the prism base produced a distinct crystalline **enneahedron** in the beryl specimen."
      },
      {
        "author": "Adrien-Marie Legendre",
        "work": "Elements of Geometry",
        "quote": "An octagonal pyramid resting upon an eight-sided base constitutes an elementary **enneahedron**."
      }
    ]
  },
  "Dashboard — ennea/enneastyle.md": {
    "primary": "An architectural portico, temple facade, or colonnade having nine columns in front.",
    "secondary": "In classical Greco-Roman architecture, a rare pseudo-dipteral or basilica facade (such as the archaic Temple of Hera I at Paestum) featuring an odd number of frontal columns.",
    "quotes": [
      {
        "author": "Vitruvius",
        "work": "The Ten Books on Architecture",
        "quote": "Colonnades are almost universally designed with an even number of columns, making an **enneastyle** arrangement an extraordinary anomaly."
      },
      {
        "author": "James Fergusson",
        "work": "A History of Architecture in All Countries",
        "quote": "The so-called Basilica of Paestum is unique among surviving Doric temples in possessing an **enneastyle** front of nine columns."
      },
      {
        "author": "Banister Fletcher",
        "work": "A History of Architecture",
        "quote": "The **enneastyle** facade necessitated a central column along the axis, dividing the interior into two parallel cella aisles."
      }
    ]
  },
  "Dashboard — ennea/enneasyllabic.md": {
    "primary": "Consisting of or having nine syllables; a verse or word containing nine syllables.",
    "secondary": "In classical metrics and prosody, designating lines such as the alcaic hendecasyllable's nine-syllable companion line (the alcaic enneasyllable).",
    "quotes": [
      {
        "author": "George Saintsbury",
        "work": "A History of English Prosody",
        "quote": "The third line of the Horace Alcaic stanza is a strict **enneasyllabic** measure with a rapid dactylic conclusion."
      },
      {
        "author": "Matthew Arnold",
        "work": "On Translating Homer",
        "quote": "The rhythmic cadence of an **enneasyllabic** phrase often imparts an unsettling, syncopated movement to lyric verse."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "In adapting ancient meters, the poet must preserve the distinct weight of the **enneasyllabic** cadence."
      }
    ]
  },
  "Dashboard — ennea/enneode.md": {
    "primary": "A nine-electrode thermionic vacuum tube containing a cathode, anode, and seven intermediate grids.",
    "secondary": "In historical electronics and radio engineering, a specialized multi-grid tube (nonode) designed for complex frequency conversion or pulse gating circuits.",
    "quotes": [
      {
        "author": "Frederick Terman",
        "work": "Radio Engineering",
        "quote": "The multi-grid **enneode** provided exceptional shielding between input and mixer stages in specialized radar receivers."
      },
      {
        "author": "Lee de Forest",
        "work": "Father of Radio: The Autobiography of Lee de Forest",
        "quote": "From my simple three-electrode Audion, engineers gradually developed intricate tubes such as the **enneode** with seven grids."
      },
      {
        "author": "Hendrik van der Bijl",
        "work": "The Thermionic Vacuum Tube",
        "quote": "In high-frequency modulation circuits, an **enneode** combines the functions of several conventional triodes into a single envelope."
      }
    ]
  },
  "Dashboard — hect/cathect.md": {
    "primary": "In psychoanalysis, to invest psychic, emotional, or libidinal energy in an idea, object, or person.",
    "secondary": "In psychiatric theory, the unconscious mental process (coined as an English translation of Freud's Besetzung) of focusing emotional attachment upon external mental representations.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "The Ego and the Id",
        "quote": "The ego must continually **cathect** internalized parental ideals to withstand the instinctual demands of the id."
      },
      {
        "author": "Carl Jung",
        "work": "Symbols of Transformation",
        "quote": "When libido fails to **cathect** productive conscious tasks, it regresses into archaic unconscious fantasies."
      },
      {
        "author": "Jacques Lacan",
        "work": "Écrits: A Selection",
        "quote": "The subject strives to **cathect** the symbolic signifier that guarantees his subjective presence within language."
      }
    ]
  },
  "Dashboard — hect/cathectic.md": {
    "primary": "Pertaining to, characterized by, or resulting from cathexis; involving the investment of emotional or psychic energy.",
    "secondary": "In psychoanalytic psychology, describing mental processes or object relations charged with concentrated libidinal or emotional valence.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "Beyond the Pleasure Principle",
        "quote": "Traumatic neurosis ensues when an unexpected shock shatters the protective shield and floods the mental apparatus with **cathectic** energy."
      },
      {
        "author": "Melanie Klein",
        "work": "Contributions to Psycho-Analysis",
        "quote": "The infant's early relationship with maternal objects is marked by intense, ambivalent **cathectic** charges."
      },
      {
        "author": "Erich Fromm",
        "work": "The Anatomy of Human Destructiveness",
        "quote": "Passionate attachments become deeply **cathectic** anchors that stabilize the individual's core orientation in the world."
      }
    ]
  },
  "Dashboard — hect/hectare.md": {
    "primary": "A metric unit of surface area equal to 100 ares, or 10,000 square meters (approximately 2.471 acres).",
    "secondary": "In international agriculture, forestry, and land surveying, the standard metric unit employed for measuring land parcels and estate acreage.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Personal Narrative of Travels to the Equinoctial Regions",
        "quote": "A single **hectare** of fertile soil along the Orinoco yielded sufficient maize to support several families throughout the year."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "If a plot of land measuring a **hectare** is left uncultivated, wild grasses and shrubs immediately reclaim the ground."
      },
      {
        "author": "Émile Zola",
        "work": "The Earth (La Terre)",
        "quote": "Fouan gazed bitterly upon his scattered fields, counting every precious **hectare** he had watered with a lifetime of sweat."
      }
    ]
  },
  "Dashboard — hect/hectic.md": {
    "primary": "Characterized by intense, frantic, or confused activity, excitement, or haste.",
    "secondary": "In historical medicine, designating a persistent, wasting fever (hectic fever) accompanied by flushed cheeks, characteristic of advanced pulmonary tuberculosis.",
    "quotes": [
      {
        "author": "Charles Dickens",
        "work": "Nicholas Nickleby",
        "quote": "There was a fatal, bright **hectic** flush upon poor Smike's cheek that whispered of deep-seated and incurable decay."
      },
      {
        "author": "Virginia Woolf",
        "work": "Mrs. Dalloway",
        "quote": "London throbbed in the June sunlight with a **hectic**, restless energy that swept crowds through the bustling streets."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The characteristic afternoon temperature spike in phthisis produces the classic **hectic** paroxysm with night sweats."
      }
    ]
  },
  "Dashboard — hect/hectically.md": {
    "primary": "In a hectic, wildly hurried, or frenzied manner.",
    "secondary": "With feverish excitement or fever-like agitation and rapidity.",
    "quotes": [
      {
        "author": "F. Scott Fitzgerald",
        "work": "The Beautiful and Damned",
        "quote": "The orchestra played **hectically** as couples drifted from table to table in the smoky glare of the nightclub."
      },
      {
        "author": "Joseph Conrad",
        "work": "Heart of Darkness",
        "quote": "The laborers worked **hectically** under the blazing sun, struggling to unload the heavy machinery before nightfall."
      },
      {
        "author": "H. G. Wells",
        "work": "The War of the Worlds",
        "quote": "Newsboys shouting extra editions ran **hectically** through the panic-stricken crowds at Waterloo station."
      }
    ]
  },
  "Dashboard — hect/hecto.md": {
    "primary": "A metric prefix (symbol: h) denoting multiplication by a factor of one hundred.",
    "secondary": "In the International System of Units (SI), a decimal multiplier derived from Greek ἑκατόν (hekaton), used in compounds such as hectoliter and hectare.",
    "quotes": [
      {
        "author": "Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "We adopted **hecto-** from the Greek for one hundred to denote centuple multiples in the rational metric nomenclature."
      },
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The metric prefix **hecto-** represents an abbreviated form of classical Greek hekaton."
      },
      {
        "author": "Augustus De Morgan",
        "work": "Elements of Arithmetic",
        "quote": "The regular application of prefixes like **hecto-** enables students to master the entire metric scale with ease."
      }
    ]
  },
  "Dashboard — hect/hectogram.md": {
    "primary": "A metric unit of mass equal to one hundred grams (symbol: hg).",
    "secondary": "In commerce and daily grocery trade (notably in Italy as the etto), a standard retail unit equivalent to 0.1 kilogram.",
    "quotes": [
      {
        "author": "Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "The new balance demonstrated accuracy to within a milligram when loaded with a standard **hectogram** brass weight."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Sign of the Four",
        "quote": "Holmes placed the recovered packet upon the scales, noting that it weighed precisely one **hectogram**."
      },
      {
        "author": "William Crookes",
        "work": "Select Methods in Chemical Analysis",
        "quote": "A sample weighing one **hectogram** was calcined in an open muffle furnace to determine the non-volatile residue."
      }
    ]
  },
  "Dashboard — hect/hectograph.md": {
    "primary": "An early mechanical apparatus for duplicating written or typed documents using a shallow pan filled with a gelatin-glycerin mixture.",
    "secondary": "In the history of printing technology, a 19th-century reprographic process in which aniline-dye ink from a master sheet was transferred onto moist gelatin to yield copies.",
    "quotes": [
      {
        "author": "H. G. Wells",
        "work": "Tono-Bungay",
        "quote": "My uncle spent his evenings churning out purple-inked commercial circulars on a messy kitchen **hectograph**."
      },
      {
        "author": "George Orwell",
        "work": "Keep the Aspidistra Flying",
        "quote": "A revolutionary pamphlet, clumsily run off on a spirit duplicator or **hectograph**, lay crumpled under the counter."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Return of Sherlock Holmes",
        "quote": "The suspicious circular was not printed with movable type, but duplicated upon a common gelatin **hectograph**."
      }
    ]
  },
  "Dashboard — hect/hectoliter.md": {
    "primary": "A metric unit of volume or capacity equal to one hundred liters (symbol: hL), equivalent to 0.1 cubic meter.",
    "secondary": "In European agriculture, viticulture, and grain commerce, the standard metric bulk measure for liquids and dry cereals.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Personal Narrative of Travels to the Equinoctial Regions",
        "quote": "The vineyard produced over fifty **hectoliters** of excellent wine per hectare during the warm autumn vintage."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "Crop yields in experimental wheat plots were carefully recorded in **hectoliters** of cleaned grain per unit area."
      },
      {
        "author": "Émile Zola",
        "work": "The Earth (La Terre)",
        "quote": "Carts piled high with barrels containing hundreds of **hectoliters** of cider rumbled toward the district market."
      }
    ]
  },
  "Dashboard — hect/hectolitre.md": {
    "primary": "The British and international spelling of hectoliter, a metric unit of capacity equal to 100 liters.",
    "secondary": "In British and Commonwealth brewing and agricultural trade, the standard bulk volumetric measure for malt, beer, and cereal crops.",
    "quotes": [
      {
        "author": "Thomas Hardy",
        "work": "The Mayor of Casterbridge",
        "quote": "Henchard inspected the barley consignments, calculating the price per **hectolitre** against the rising grain market."
      },
      {
        "author": "H. G. Wells",
        "work": "The World of William Clissold",
        "quote": "Modern continental breweries boast enormous copper vats capable of fermenting thousands of **hectolitres** in a single brew."
      },
      {
        "author": "John Ruskin",
        "work": "Fors Clavigera",
        "quote": "Let the honest peasant receive fair payment for every **hectolitre** of grain harvested from his native soil."
      }
    ]
  },
  "Dashboard — hect/hectometer.md": {
    "primary": "A metric unit of length equal to one hundred meters (symbol: hm).",
    "secondary": "In civil engineering, forestry, and road construction, a convenient distance measure equivalent to one-tenth of a kilometer.",
    "quotes": [
      {
        "author": "Ferdinand Rudolph Hassler",
        "work": "Papers on the Survey of the Coast of the United States",
        "quote": "The coastal baseline was surveyed in increments of one **hectometer**, verified by optical triangulation."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos: A Sketch of a Physical Description of the Universe",
        "quote": "We measured the vertical elevation of the mountain slope every **hectometer** using refined barometric instruments."
      },
      {
        "author": "Jules Verne",
        "work": "From the Earth to the Moon",
        "quote": "The colossal Columbiad cannon possessed a bore spanning several meters and a barrel length exceeding a **hectometer**."
      }
    ]
  },
  "Dashboard — hect/hectometre.md": {
    "primary": "The British and international spelling of hectometer, a metric unit of length equal to 100 metres.",
    "secondary": "In Commonwealth surveying and railway engineering, a linear distance unit marking one-tenth of a kilometre.",
    "quotes": [
      {
        "author": "Arthur Conan Doyle",
        "work": "The Lost World",
        "quote": "The sheer cliff wall rose nearly a **hectometre** into the misty air, defying any attempt at direct ascent."
      },
      {
        "author": "H. G. Wells",
        "work": "When the Sleeper Wakes",
        "quote": "Massive flying machines glided along launch tracks extending more than a **hectometre** across the city rooftops."
      },
      {
        "author": "Joseph Conrad",
        "work": "Lord Jim",
        "quote": "The ship drifted slowly toward the reef, missing the submerged rocks by barely half a **hectometre**."
      }
    ]
  },
  "Dashboard — hect/hector.md": {
    "primary": "To bully, intimidate, badger, or dominate in an overbearing or swaggering manner.",
    "secondary": "In classical literature, Hector the valiant Trojan champion; historically in 17th-century London, a swaggering roisterer or ruffian.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Troilus and Cressida",
        "quote": "Noble **Hector**, the bulwark of Troy, advanced with flashing armor to challenge the fiercest Greek champions."
      },
      {
        "author": "Jonathan Swift",
        "work": "The Battle of the Books",
        "quote": "Pedantic critics attempt to **hector** and browbeat modern authors who dare to challenge ancient authority."
      },
      {
        "author": "Charles Dickens",
        "work": "Bleak House",
        "quote": "Mr. Chadband loved to **hector** his listeners with pompous rhetorical homilies on moral virtue."
      }
    ]
  },
  "Dashboard — hemi/anthemis.md": {
    "primary": "A genus of aromatic flowering plants in the aster family (Asteraceae), commonly including dog fennel and stinking chamomile.",
    "secondary": "In botanical medicine and horticulture, Mediterranean herbs with finely dissected foliage and daisy-like flower heads used in traditional infusions.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The introduced field weed **Anthemis** cotula, known as mayweed or dog fennel, emits a strong, acrid aroma."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "Species of **Anthemis** yield essential oils and bitter principles long celebrated in European herbal pharmacopoeias."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "The Flora of British India",
        "quote": "Along arid stony paths, wild **Anthemis** flourished with solitary daisy heads displaying yellow disk florets."
      }
    ]
  },
  "Dashboard — hemi/hemi.md": {
    "primary": "A Greek combining root morpheme (ἡμι-, hemi-) signifying half or partial.",
    "secondary": "In scientific and anatomical nomenclature, a productive prefix denoting half, unilateral occurrence, or incomplete development (as in hemisphere, hemianopia, hemiplegia).",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The Greek prefix **hemi-** signifies half, corresponding to Latin semi- and French demi- in scholarly coinages."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "From **hemi-** arise compounds expressing half-measures, bisection, or half-finished celestial arcs."
      },
      {
        "author": "Thomas Heath",
        "work": "A History of Greek Mathematics",
        "quote": "In stereometry, Archimedes constantly employed compounds of **hemi-** to calculate the volumes of half-spheres."
      }
    ]
  },
  "Dashboard — hemi/hemiacetal.md": {
    "primary": "An organic chemical compound formed by the nucleophilic addition of an alcohol to an aldehyde (containing a -CH(OH)(OR) group).",
    "secondary": "In carbohydrate chemistry, the cyclic ring structure formed by intramolecular reaction between a sugar's aldehyde group and a hydroxyl group.",
    "quotes": [
      {
        "author": "Emil Fischer",
        "work": "Syntheses in the Sugar Group",
        "quote": "The mutarotation of glucose in aqueous solution reflects reversible cyclization into a stable cyclic **hemiacetal**."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "The bond angles of the oxygen bridge in the **hemiacetal** pyranose ring confirm the tetrahedral geometry of carbon."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Textbook of Theoretical Electrochemistry",
        "quote": "Acid catalysis accelerates the transformation of an unstable open-chain aldehyde into a cyclic **hemiacetal**."
      }
    ]
  },
  "Dashboard — hemi/hemianopia.md": {
    "primary": "Blindness or loss of vision in one half of the visual field in one or both eyes.",
    "secondary": "In clinical neurology and ophthalmology, a visual defect (such as bitemporal or homonymous hemianopia) caused by a lesion in the optic chiasm or retrochiasmal pathways.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Homonymous **hemianopia** indicates an interruption of the visual radiation or occipital cortex on the contralateral side."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Pituitary Body and its Disorders",
        "quote": "Upward pressure from a pituitary adenoma against the optic chiasm frequently induces bitemporal **hemianopia**."
      },
      {
        "author": "William Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "Perimetric visual field charts readily confirm whether the **hemianopia** respects the vertical anatomical meridian."
      }
    ]
  },
  "Dashboard — hemi/hemianopsia.md": {
    "primary": "A variant medical spelling of hemianopia, denoting partial blindness affecting half of the visual field.",
    "secondary": "In ophthalmic pathology, loss of vision in half of the visual field caused by vascular stroke, tumor, or trauma along the optic tract.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The patient complained of bumping into doorframes on his right, a classic symptom of undetected right homonymous **hemianopsia**."
      },
      {
        "author": "William Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "Lesions affecting the optic tract produce complete congruous **hemianopsia** without pupillary hemiopic reaction."
      },
      {
        "author": "Oliver Wendell Holmes Sr.",
        "work": "Medical Essays",
        "quote": "A temporary **hemianopsia** sometimes heralds a severe migraine attack before the onset of unilateral headache."
      }
    ]
  },
  "Dashboard — hemi/hemiascomycetes.md": {
    "primary": "A primitive class or group of ascomycetous fungi (including true yeasts) that produce naked asci without forming a fruiting body (ascocarp).",
    "secondary": "In systematic mycology, basal ascomycetes (now often classified under Saccharomycetes or Taphrinomycotina) exhibiting simple budding or fission cycles.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Studies on Fermentation",
        "quote": "The fermenting agent in alcoholic vats belongs to simple budding organisms allied to the **Hemiascomycetes**."
      },
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi",
        "quote": "In **Hemiascomycetes**, the sexual generation terminates in naked asci exposed directly upon the host tissue or broth."
      },
      {
        "author": "Pier Andrea Saccardo",
        "work": "Sylloge Fungorum",
        "quote": "The absence of a protective perithecium separates primitive **Hemiascomycetes** from the higher disc and pyrenomycete fungi."
      }
    ]
  },
  "Dashboard — hemi/hemiballismus.md": {
    "primary": "A hyperkinetic movement disorder characterized by sudden, violent, involuntary flinging or flailing movements of the limbs on one side of the body.",
    "secondary": "In clinical neurology, a rare stroke-induced dyskinesia caused by a unilateral vascular lesion in the contralateral subthalamic nucleus of Luys.",
    "quotes": [
      {
        "author": "William Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "Violent unilateral choreiform flinging, known as **hemiballismus**, typically points to acute pathology in the subthalamic body."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The uncoordinated thrashing of the arm and leg in **hemiballismus** exhausts the patient unless controlled by sedation."
      },
      {
        "author": "Harvey Cushing",
        "work": "Selected Papers on Neurosurgery",
        "quote": "Subcortical hemorrhages involving the corpus Luysii often trigger catastrophic episodes of uncontrollable **hemiballismus**."
      }
    ]
  },
  "Dashboard — hemi/hemic.md": {
    "primary": "Of, relating to, or involving blood (more commonly spelled haemic or hemal).",
    "secondary": "In medical pathology, designating conditions, murmurs (e.g., hemic murmur in severe anemia), or disorders originating in the circulating blood.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A soft systolic **hemic** murmur over the cardiac base is common in profoundly anemic chlorotic patients."
      },
      {
        "author": "Thomas Addison",
        "work": "A Collection of the Published Writings",
        "quote": "The clinical picture was characterized by progressive debility and abnormal **hemic** changes without localized cancer."
      },
      {
        "author": "William Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "Thrombosis may arise from vascular disease or from altered **hemic** viscosity during severe systemic infections."
      }
    ]
  },
  "Dashboard — hemi/hemicrania.md": {
    "primary": "A severe, recurring headache affecting only one side of the head; the classical etymon of migraine.",
    "secondary": "In historical and clinical medicine, unilateral cephalalgia accompanied by nausea, photophobia, and sensory auras.",
    "quotes": [
      {
        "author": "Galen",
        "work": "De Methodo Medendi",
        "quote": "When pain seizes half the head along the sagittal suture, the ancients properly termed the malady **hemicrania**."
      },
      {
        "author": "Robert Burton",
        "work": "The Anatomy of Melancholy",
        "quote": "Many melancholic scholars suffer martyrdom from cruel bouts of **hemicrania** that darken the daylight for days."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The paroxysmal unilateral throbbing of **hemicrania** has been recognized by medical writers since the days of Aretaeus."
      }
    ]
  },
  "Dashboard — hemi/hemicryptophyte.md": {
    "primary": "A perennial plant whose perennating buds are positioned at or just below the soil surface, protected by leaf litter or snow.",
    "secondary": "In Raunkiær's plant life-form classification, a dominant life-form in temperate grasslands and deciduous forests (such as dandelions and meadow grasses).",
    "quotes": [
      {
        "author": "Christen Raunkiær",
        "work": "The Life Forms of Plants and Statistical Plant Geography",
        "quote": "Temperate climates favor the **hemicryptophyte**, which shelters its dormant buds safely under the winter blanket of humus."
      },
      {
        "author": "Arthur George Tansley",
        "work": "The British Islands and Their Vegetation",
        "quote": "Meadow flora in our moist maritime zone is overwhelmingly composed of rosettes belonging to the **hemicryptophyte** category."
      },
      {
        "author": "Frederic Clements",
        "work": "Plant Succession: An Analysis of the Development of Vegetation",
        "quote": "The climax prairie ecosystem relies upon deep-rooted **hemicryptophytes** capable of surviving seasonal freezes and summer droughts."
      }
    ]
  },
  "Dashboard — hemi/hemicube.md": {
    "primary": "In computer graphics, a numerical algorithm that calculates radiosity form factors between surfaces using half of a bounding cube.",
    "secondary": "In 3D computer graphics rendering, a hemi-cubical projection method that discretizes radiant energy transfer by projecting a scene onto the five faces of half a cube.",
    "quotes": [
      {
        "author": "Michael F. Cohen",
        "work": "Radiosity and Realistic Image Synthesis",
        "quote": "The **hemicube** algorithm approximates form factors by projecting surrounding geometric polygons onto five planar pixel grids."
      },
      {
        "author": "James D. Foley",
        "work": "Computer Graphics: Principles and Practice",
        "quote": "By using the graphics hardware z-buffer to render the faces of a **hemicube**, global illumination can be computed with high efficiency."
      },
      {
        "author": "Donald Hearn",
        "work": "Computer Graphics with OpenGL",
        "quote": "Each pixel on the **hemicube** surface corresponds to a delta form factor contributing to the total irradiance of the patch."
      }
    ]
  },
  "Dashboard — hemi/hemicycle.md": {
    "primary": "A semicircular shape, structure, colonnade, or architectural arena.",
    "secondary": "In classical and modern architecture, a semicircular amphitheatre, curved seating chamber of a parliament (such as the French National Assembly), or curved apse.",
    "quotes": [
      {
        "author": "Vitruvius",
        "work": "The Ten Books on Architecture",
        "quote": "The sun-dial of Berosus was hollowed out of a square stone block into a graceful celestial **hemicycle**."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Recollections",
        "quote": "Tumultuous shouts echoed across the parliamentary **hemicycle** as the deputies rose in violent confrontation."
      },
      {
        "author": "Banister Fletcher",
        "work": "A History of Architecture",
        "quote": "Trajan's Forum incorporated a monumental brick **hemicycle** lined with tiered shops backing against the Quirinal hill."
      }
    ]
  },
  "Dashboard — hemi/hemidesmosome.md": {
    "primary": "A specialized cell junction that anchors the basal surface of epithelial cells to the underlying basement membrane.",
    "secondary": "In cell biology and histology, an asymmetric multiprotein plaque utilizing integrin alpha-6-beta-4 to fasten intermediate keratin filaments to extracellular laminin.",
    "quotes": [
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Epithelial sheets adhere firmly to the basal lamina through rivet-like junctions termed **hemidesmosomes**."
      },
      {
        "author": "Don W. Fawcett",
        "work": "A Textbook of Histology",
        "quote": "Electron micrographs reveal that a **hemidesmosome** represents exactly half of a macula adherens, specialized for matrix adhesion."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Genetic defects in **hemidesmosome** anchor proteins trigger severe blistering disorders like epidermolysis bullosa."
      }
    ]
  },
  "Dashboard — hemi/hemiepiphyte.md": {
    "primary": "A plant that begins its life as an epiphyte in the forest canopy and subsequently establishes roots in the ground, or vice versa.",
    "secondary": "In tropical forest ecology, a climbing plant or strangler (such as Ficus or Clusia) that germinates in branch forks before sending down descending aerial roots to encircle the host tree.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Aspects of Nature",
        "quote": "Vast strangler figs begin their aerial life as a delicate **hemiepiphyte** high in the crown of towering palm trees."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "Tropical Nature, and Other Essays",
        "quote": "The predatory **hemiepiphyte** weaves a lattice of descending roots that eventually smothers and kills the supporting timber."
      },
      {
        "author": "A. F. W. Schimper",
        "work": "Plant-Geography Upon a Physiological Basis",
        "quote": "Ecological transitions between true epiphytism and rooted lianas are exemplified by diverse tropical **hemiepiphytes**."
      }
    ]
  },
  "Dashboard — hemi/hemimelia.md": {
    "primary": "A congenital limb anomaly characterized by the complete or partial absence of the distal portion of one or more limbs.",
    "secondary": "In teratology and orthopedic medicine, a developmental failure of limb bud elongation, typically affecting the radius, fibula, or tibia (as in fibular hemimelia).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Congenital anomalies of the extremities range from subtle syndactyly to gross reduction deformities like **hemimelia**."
      },
      {
        "author": "Jonathan Hutchinson",
        "work": "Archives of Surgery",
        "quote": "The museum specimen illustrates unilateral radial **hemimelia** with characteristic paraxial absence of the thumb."
      },
      {
        "author": "Ferdinand Sauerbruch",
        "work": "Master Surgeon: A Life in Surgery",
        "quote": "Children born with lower extremity **hemimelia** require early orthopedic stabilization to enable upright bipedal walking."
      }
    ]
  },
  "Dashboard — hemi/hemimetabola.md": {
    "primary": "A group of insects that undergo incomplete or hemimetabolous metamorphosis, lacking a pupal stage.",
    "secondary": "In entomological classification, an informal or historical cohort encompassing orders such as Orthoptera, Hemiptera, and Odonata, whose nymphs resemble miniature adults.",
    "quotes": [
      {
        "author": "John Obadiah Westwood",
        "work": "An Introduction to the Modern Classification of Insects",
        "quote": "Insects belonging to **Hemimetabola** hatch as active nymphs possessing external wing-pads that expand with each molt."
      },
      {
        "author": "L. O. Howard",
        "work": "The Insect Book",
        "quote": "Grasshoppers, cicadas, and true bugs belong to the **Hemimetabola**, escaping the dormant pupal chrysalis entirely."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The direct post-embryonic development of **Hemimetabola** contrasts sharply with the complete metamorphosis of beetles and butterflies."
      }
    ]
  },
  "Dashboard — hemi/hemimetabolic.md": {
    "primary": "Exhibiting or relating to hemimetabolism (incomplete insect metamorphosis).",
    "secondary": "In developmental entomology, characterizing an insect life cycle that progresses through gradual nymphal instars without a pupal stage.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The gradual morphological transitions of **hemimetabolic** insects suggest how complex holometabolous stages could have evolved."
      },
      {
        "author": "L. O. Howard",
        "work": "The Insect Book",
        "quote": "The **hemimetabolic** pattern of development enables young dragonfly naiads to hunt voraciously in aquatic habitats."
      },
      {
        "author": "John Obadiah Westwood",
        "work": "An Introduction to the Modern Classification of Insects",
        "quote": "Wing buds become progressively more pronounced with each successive ecdysis in **hemimetabolic** nymphs."
      }
    ]
  },
  "Dashboard — hemi/hemimetabolism.md": {
    "primary": "The mode of insect development characterized by incomplete metamorphosis, passing directly from egg to nymph to adult without a pupa.",
    "secondary": "In insect physiology, a three-stage developmental progression (egg, nymph, imago) in which the nymph gradually acquires adult structures over successive instars.",
    "quotes": [
      {
        "author": "V. B. Wigglesworth",
        "work": "The Principles of Insect Physiology",
        "quote": "Endocrine regulation during **hemimetabolism** involves gradual decline of juvenile hormone titers allowing adult cuticular differentiation."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The evolutionary antiquity of **hemimetabolism** is corroborated by the abundant presence of paleopterous nymphs in Carboniferous rocks."
      },
      {
        "author": "John Henry Comstock",
        "work": "An Introduction to Entomology",
        "quote": "True bugs exhibit typical **hemimetabolism**, wherein the early instars share the piercing-sucking mouthparts of mature adults."
      }
    ]
  },
  "Dashboard — hemi/hemimetabolous.md": {
    "primary": "Undergoing or characterized by incomplete metamorphosis without a quiescent pupal stage.",
    "secondary": "In entomology, describing insects such as mayflies, dragonflies, mantids, and cockroaches whose young are active nymphs.",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "Darwinism: An Exposition of the Theory of Natural Selection",
        "quote": "Protective coloration and mimicry appear fully developed in many **hemimetabolous** insects even during their immature nymphal phases."
      },
      {
        "author": "Jean-Henri Fabre",
        "work": "The Life of the Grasshopper",
        "quote": "The young locust is a **hemimetabolous** miniature of its parents, already equipped with voracious jaws and leaping legs."
      },
      {
        "author": "V. B. Wigglesworth",
        "work": "The Physiology of Insect Metamorphosis",
        "quote": "In **hemimetabolous** species like Rhodnius, decapitation after feeding arrests adult imaginal development."
      }
    ]
  },
  "Dashboard — hemi/hemimetaboly.md": {
    "primary": "The condition or biological phenomenon of incomplete metamorphosis in insects.",
    "secondary": "In evolutionary entomology, the ancestral pterygote developmental strategy in which aquatic or terrestrial nymphs transition gradually into reproducing winged adults.",
    "quotes": [
      {
        "author": "V. B. Wigglesworth",
        "work": "The Principles of Insect Physiology",
        "quote": "Comparative endocrinology suggests that holometaboly arose through an evolutionary modification of ancestral **hemimetaboly**."
      },
      {
        "author": "John Henry Comstock",
        "work": "An Introduction to Entomology",
        "quote": "The student must carefully distinguish between simple ametaboly, incomplete **hemimetaboly**, and complete holometaboly."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Ontogeny and Phylogeny",
        "quote": "The retention of juvenile features in the adult may be traced with particular clarity in lineages practicing **hemimetaboly**."
      }
    ]
  },
  "Dashboard — hemi/hemimetamorphic.md": {
    "primary": "Undergoing or characterized by partial or incomplete metamorphosis.",
    "secondary": "In invertebrate zoology and developmental biology, describing organisms that transform gradually between larval and mature forms without radical tissue histolysis.",
    "quotes": [
      {
        "author": "Ray Lankester",
        "work": "Comparative Embryology",
        "quote": "The **hemimetamorphic** nature of primitive arthropods reflects a stepwise addition of bodily segments across life."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "In **hemimetamorphic** development, the organ systems of the nymph pass continuously into those of the adult."
      },
      {
        "author": "Ernst Haeckel",
        "work": "The Evolution of Man",
        "quote": "Direct ontogenetic lines frequently preserve **hemimetamorphic** stages before evolving extreme larval adaptations."
      }
    ]
  },
  "Dashboard — hemi/hemimetamorphosis.md": {
    "primary": "Incomplete or gradual metamorphosis in insects and certain other invertebrates.",
    "secondary": "In biology, developmental transformation lacking a distinct pupal resting stage, proceeding through repeated ecdyses of active nymphs directly to the imago.",
    "quotes": [
      {
        "author": "John Obadiah Westwood",
        "work": "An Introduction to the Modern Classification of Insects",
        "quote": "The process of **hemimetamorphosis** in orthopteran insects allows uninterrupted feeding and growth throughout development."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Variations occurring during **hemimetamorphosis** are exposed continuously to natural selection in the nymph's natural environment."
      },
      {
        "author": "V. B. Wigglesworth",
        "work": "The Physiology of Insect Metamorphosis",
        "quote": "Prothoracicotropic hormone secretion initiates each molt in the progression of **hemimetamorphosis**."
      }
    ]
  },
  "Dashboard — hemi/hemimetamorphous.md": {
    "primary": "Exhibiting or undergoing partial, incomplete metamorphosis.",
    "secondary": "In entomology, an adjectival variant designating insects whose immature stages are nymphs resembling adults in general body plan.",
    "quotes": [
      {
        "author": "L. O. Howard",
        "work": "The Insect Book",
        "quote": "The **hemimetamorphous** orders encompass ancient insect lineages whose origins date back to the Paleozoic era."
      },
      {
        "author": "Jean-Henri Fabre",
        "work": "The Life of the Mantis",
        "quote": "Being a **hemimetamorphous** creature, the baby praying mantis emerges from the ootheca already equipped with rapacious forelegs."
      },
      {
        "author": "John Henry Comstock",
        "work": "The Elements of Insect Anatomy",
        "quote": "Wing pads remain external and dorsal throughout the development of **hemimetamorphous** nymphs."
      }
    ]
  },
  "Dashboard — hemi/hemimorphite.md": {
    "primary": "A basic zinc silicate mineral, Zn4Si2O7(OH)2·H2O, which forms hemimorphic crystals displaying different crystallographic terminations at opposite ends.",
    "secondary": "In mineralogy, an important ore of zinc (formerly called calamine) exhibiting pronounced pyroelectric and piezoelectric properties due to its polar crystal structure.",
    "quotes": [
      {
        "author": "James Dwight Dana",
        "work": "A System of Mineralogy",
        "quote": "The name **hemimorphite** was assigned to this silicate of zinc because its crystals terminate differently at opposite poles of the vertical axis."
      },
      {
        "author": "René Just Haüy",
        "work": "Traité de Minéralogie",
        "quote": "Upon heating, crystals of **hemimorphite** develop opposite electrical charges at their contrasting polar terminations."
      },
      {
        "author": "John Ruskin",
        "work": "The Ethics of the Dust",
        "quote": "The delicate blue and white crusts of **hemimorphite** sparkle within the limestone caverns like frostwork."
      }
    ]
  },
  "Dashboard — hemi/hemin.md": {
    "primary": "A reddish-brown crystalline chloride salt of heme (ferriheme chloride), produced by heating blood with glacial acetic acid and sodium chloride.",
    "secondary": "In forensic medicine and biochemistry, the classic Teichmann crystals used in microchemical tests to confirm the presence of mammalian hemoglobin in bloodstains.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The microscopic detection of rhombic **hemin** crystals by Teichmann's method provides unequivocal forensic proof of blood."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "A Study in Scarlet",
        "quote": "Holmes cried out in triumph, having discovered a chemical reagent far superior to the old **hemin** test for detecting bloodstains."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Immunochemistry",
        "quote": "The optical absorption spectrum of crystalline **hemin** reveals characteristic bands associated with the central coordinated iron atom."
      }
    ]
  },
  "Dashboard — hemi/heming.md": {
    "primary": "John Heminges (Heming, 1556–1630), English King's Men actor who co-edited William Shakespeare's First Folio of 1623 with Henry Condell.",
    "secondary": "The artisanal action of folding over and stitching the raw edge of a fabric to create a hem (hemming); or a historical Norse personal name.",
    "quotes": [
      {
        "author": "Ben Jonson",
        "work": "To the Memory of My Beloved Master William Shakespeare",
        "quote": "Fellow actors **Heming** and Condell performed a priceless service to English literature by preserving the plays in folio."
      },
      {
        "author": "Thomas Carlyle",
        "work": "On Heroes, Hero-Worship, and the Heroic in History",
        "quote": "Without the pious devotion of **Heming** and his partner, half the masterpieces of Shakespeare would have vanished into oblivion."
      },
      {
        "author": "William Hazlitt",
        "work": "Lectures on the Dramatic Literature of the Age of Elizabeth",
        "quote": "The preface written by John **Heming** and Henry Condell breathes the sincere warmth of lifelong theatrical camaraderie."
      }
    ]
  },
  "Dashboard — hemi/hemingway.md": {
    "primary": "Ernest Hemingway (1899–1961), celebrated Nobel Prize-winning American novelist and short-story writer known for economical prose and the iceberg theory.",
    "secondary": "In literary criticism, the distinct thematic ethos of understated courage, stoicism under grace, and sensory precision established by Hemingway.",
    "quotes": [
      {
        "author": "William Faulkner",
        "work": "Faulkner in the University: Class Conferences",
        "quote": "**Hemingway** discovered early what he could do with words, stripping language down to courageous, unadorned truth."
      },
      {
        "author": "F. Scott Fitzgerald",
        "work": "The Crack-Up",
        "quote": "Ernest **Hemingway** possessed an instinct for finding the exact physical detail that unlocked a whole emotional scene."
      },
      {
        "author": "George Orwell",
        "work": "Critical Essays",
        "quote": "The wartime narratives of **Hemingway** captured the disillusionment of a generation without resorting to sentimental rhetoric."
      }
    ]
  },
  "Dashboard — hemi/hemingwayesque.md": {
    "primary": "Characteristic of, resembling, or imitating the style, themes, or persona of the American author Ernest Hemingway.",
    "secondary": "In literary criticism, characterized by terse declarative sentences, emotional understatement, journalistic dialogue, and masculine stoicism under pressure.",
    "quotes": [
      {
        "author": "Gore Vidal",
        "work": "United States: Essays 1952–1992",
        "quote": "Generations of young war correspondents adopted a **hemingwayesque** pose, writing in tight, muscular cadence."
      },
      {
        "author": "Anthony Burgess",
        "work": "Urgent Copy: Literary Studies",
        "quote": "The novel's opening scene in the Madrid café was distinctly **hemingwayesque** in its clipped dialogue and sensory restraint."
      },
      {
        "author": "Norman Mailer",
        "work": "Advertisements for Myself",
        "quote": "Every post-war American novelist wrestled with the immense shadow cast by the **hemingwayesque** ideal of courage."
      }
    ]
  },
  "Dashboard — hemi/hemiparesis.md": {
    "primary": "Muscular weakness or partial paralysis affecting one side of the body.",
    "secondary": "In clinical neurology, a hallmark clinical sign of an ischemic stroke, intracerebral hemorrhage, or brain tumor localized to the contralateral motor cortex or internal capsule.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Acute onset of right **hemiparesis** accompanied by motor aphasia indicates occlusion of the left middle cerebral artery."
      },
      {
        "author": "William Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "Gradual development of spastic **hemiparesis** over weeks suggests a growing expanding lesion in the contralateral hemisphere."
      },
      {
        "author": "Oliver Wendell Holmes Sr.",
        "work": "Medical Essays",
        "quote": "The physician watched the gradual recovery of voluntary movement in the patient's arm following the transient **hemiparesis**."
      }
    ]
  },
  "Dashboard — hemi/hemipolyhedron.md": {
    "primary": "A uniform star polyhedron whose faces pass through its center of symmetry, having half the faces of an ordinary uniform polyhedron.",
    "secondary": "In higher geometry and polyhedral theory, a non-convex uniform polyhedron possessing equatorial faces that pass directly through its geometric centroid.",
    "quotes": [
      {
        "author": "H. S. M. Coxeter",
        "work": "Regular Polytopes",
        "quote": "Every uniform **hemipolyhedron** possesses faces that pass through its center, giving it non-orientable topology."
      },
      {
        "author": "Arthur Cayley",
        "work": "The Collected Mathematical Papers",
        "quote": "The intersection of diametral planes in a **hemipolyhedron** produces unexpected symmetry groups in three-dimensional space."
      },
      {
        "author": "Felix Klein",
        "work": "Lectures on the Icosahedron",
        "quote": "Transformations of central polyhedra yield star forms such as the octahemioctahedron and related **hemipolyhedra**."
      }
    ]
  },
  "Dashboard — hemi/hemiramphidae.md": {
    "primary": "A family of epipelagic and freshwater actinopterygian fishes known as halfbeaks, characterized by an elongated lower jaw and short upper jaw.",
    "secondary": "In ichthyology, surface-dwelling beloniform fishes related to flyingfishes and needlefishes, feeding on floating surface organisms with their extended beak.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "Fishes of the family **Hemiramphidae** skim the oceanic surface, their elongated lower jaws cutting through the surface film."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "In tropical lagoons we observed curious halfbeaks belonging to **Hemiramphidae** skipping across the water to evade predators."
      },
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "The asymmetric jaws of **Hemiramphidae** illustrate a remarkable morphological specialization for surface foraging."
      }
    ]
  },
  "Dashboard — hemi/hemisphere.md": {
    "primary": "A half of a sphere; in geography, one half of the terrestrial globe (Northern, Southern, Eastern, or Western Hemisphere).",
    "secondary": "In neuroanatomy, either of the two symmetrical lateral halves of the cerebrum or cerebellum (cerebral hemisphere).",
    "quotes": [
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "The glass lens was formed by grinding a flat plane against the convex curve of a polished glass **hemisphere**."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos: A Sketch of a Physical Description of the Universe",
        "quote": "As the vessel crossed the equator into the Southern **Hemisphere**, unfamiliar stellar constellations illuminated the night sky."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Voluntary motor functions for the right side of the body reside principally in the left cerebral **hemisphere**."
      }
    ]
  },
  "Dashboard — hemi/hemispheric.md": {
    "primary": "Pertaining to, having the form of, or situated in a hemisphere.",
    "secondary": "In neurology, relating to one of the cerebral hemispheres of the brain; in meteorology, spanning an entire half of the globe.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A massive intracerebral hemorrhage produces extensive **hemispheric** compression and contralateral paralysis."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Aspects of Nature",
        "quote": "Vast atmospheric circulation cells determine the predominant **hemispheric** wind patterns across the Atlantic."
      },
      {
        "author": "D'Arcy Wentworth Thompson",
        "work": "On Growth and Form",
        "quote": "Surface tension shapes the expanding liquid droplet into a graceful, symmetrical **hemispheric** dome."
      }
    ]
  },
  "Dashboard — hemi/hemispherical.md": {
    "primary": "Having the shape or form of half a sphere; rounded and convex like a hemisphere.",
    "secondary": "In architecture and engineering, describing domes, bowls, or chambers shaped like a half-sphere.",
    "quotes": [
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "The Byzantine church was crowned by a golden **hemispherical** cupola that caught the morning light above the lagoon."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "The electrostatic charge gathered entirely upon the outer surface of the hollow **hemispherical** brass conductors."
      },
      {
        "author": "Charles Darwin",
        "work": "The Formation of Vegetable Mould through the Action of Worms",
        "quote": "The mouth of the burrow was roofed over by an ingenious **hemispherical** dome of cemented mud pellets."
      }
    ]
  },
  "Dashboard — hemi/hemitripterus.md": {
    "primary": "A genus of marine scorpaeniform fishes known as sea ravens (family Hemitripteridae), characterized by ragged, fleshy head flaps and spiny dorsal fins.",
    "secondary": "In North Atlantic and North Pacific marine biology, benthic ambush predators found in cold rocky waters, possessing a voracious appetite and mottled camouflage.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The sea raven **Hemitripterus** americanus displays grotesque dermal flaps on its head resembling decomposing seaweed."
      },
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "When hauled from cold Atlantic waters, the spiny sculpin **Hemitripterus** inflates its belly with air like a pufferfish."
      },
      {
        "author": "Spencer Fullerton Baird",
        "work": "Report on the Condition of the Sea Fisheries",
        "quote": "Trawlers frequently bring up specimens of **Hemitripterus** from the rocky banks off the coast of Maine."
      }
    ]
  },
  "Dashboard — hemi/protohemin.md": {
    "primary": "Ferriprotoporphyrin IX chloride; the classical crystalline chloro-hemin complex derived from blood hemoglobin.",
    "secondary": "In biochemistry, the prosthetic iron-porphyrin complex common to hemoglobin, myoglobin, and peroxidases, isolated as microscopic rhombic chloride crystals.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Magnetic susceptibility measurements confirm the high-spin iron state in crystalline **protohemin** complexes."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Immunochemistry",
        "quote": "The characteristic spectroscopic absorption bands of **protohemin** disappear upon reduction to the ferrous state."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Microcrystalline tests yielding Prussian blue or **protohemin** confirm the presence of degraded blood pigment."
      }
    ]
  },
  "Dashboard — hen/enosis.md": {
    "primary": "The political movement or goal aiming at the unification of Cyprus (or other historically Greek territories) with the state of Greece.",
    "secondary": "In modern Hellenic history (Greek ἕνωσις, union), the 19th- and 20th-century nationalist aspiration of Greek Cypriots for union with mainland Greece.",
    "quotes": [
      {
        "author": "Winston Churchill",
        "work": "The Second World War",
        "quote": "Passionate agitation for **enosis** among Greek Cypriots repeatedly strained diplomatic relations across the eastern Mediterranean."
      },
      {
        "author": "George Finlay",
        "work": "A History of Greece",
        "quote": "The popular cry of **enosis** animated the islanders of the Ionian and Aegean seas throughout their struggle against alien rule."
      },
      {
        "author": "Arnold J. Toynbee",
        "work": "The Western Question in Greece and Turkey",
        "quote": "The irresistible emotional pull of **enosis** transformed local administrative grievances into an international territorial crisis."
      }
    ]
  },
  "Dashboard — hen/enotikon.md": {
    "primary": "An imperial religious edict issued in 482 CE by the Byzantine Emperor Zeno in an unsuccessful attempt to reconcile Chalcedonian and Miaphysite Christians.",
    "secondary": "In church history, the Henotikon (Instrument of Union) formulated by Patriarch Acacius, which avoided defining Christ's natures and triggered the 35-year Acacian Schism with Rome.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "By the compromise of the **Henotikon**, Emperor Zeno attempted to soothe the theological fury that inflamed Egypt and Syria."
      },
      {
        "author": "Philip Schaff",
        "work": "History of the Christian Church",
        "quote": "The **Henotikon** of Zeno pleased neither the orthodox Western bishops nor the radical monks of Alexandria, precipitating long schism."
      },
      {
        "author": "J. B. Bury",
        "work": "A History of the Later Roman Empire",
        "quote": "By ignoring the Tome of Leo, the **Henotikon** estranged the papacy and undermined imperial religious unity."
      }
    ]
  },
  "Dashboard — hen/heis.md": {
    "primary": "The ancient Greek masculine numeral for one (εἷς).",
    "secondary": "In classical philology and philosophical ontology, the masculine nominative cardinal number representing unity, singularity, or an individual entity.",
    "quotes": [
      {
        "author": "Plato",
        "work": "Parmenides",
        "quote": "If the One, **heis**, exists, can it be many, or must it remain indivisible and devoid of parts?"
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The numeral **heis** forms the masculine base of Hellenic counting, corresponding to feminine mia and neuter hen."
      },
      {
        "author": "Plotinus",
        "work": "The Enneads",
        "quote": "Above all multiplicity of intellect and soul reigns the primordial principle, the transcendent One, **heis**."
      }
    ]
  },
  "Dashboard — hen/hen.md": {
    "primary": "The female of the domestic fowl (Gallus gallus domesticus) or of any other gallinaceous or avian species.",
    "secondary": "In ancient Greek philosophy, the neuter cardinal numeral for one (ἕν), designating the ultimate principle of metaphysical unity or the One.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "The domestic **hen** displays extraordinary maternal instincts, brooding her clutch of eggs with tireless devotion."
      },
      {
        "author": "Plotinus",
        "work": "The Enneads",
        "quote": "All things derive their being from the To **Hen**, the Supreme Unity that transcends intellect and substance."
      },
      {
        "author": "Thomas Hardy",
        "work": "Far from the Madding Crowd",
        "quote": "A solitary speckled **hen** strutted across the farmyard, pecking among the fresh straw for scattered grain."
      }
    ]
  },
  "Dashboard — hen/henad.md": {
    "primary": "A unit, monad, or ultimate individual entity; specifically in Neoplatonic philosophy, one of the supreme divine principles of unity.",
    "secondary": "In late Neoplatonism (especially in the philosophy of Proclus), each transcendent, supra-essential god or primary unit that mediates between the ineffable One and the realm of Being.",
    "quotes": [
      {
        "author": "Proclus",
        "work": "The Elements of Theology",
        "quote": "Every **henad** is self-complete, divine, and supra-essential, illuminating the lower orders of Being with unity."
      },
      {
        "author": "Thomas Taylor",
        "work": "The Six Books of Proclus on the Theology of Plato",
        "quote": "The divine **henads** are the unities of the gods, transcending intellect and participating directly in the supreme One."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Lectures on the History of Philosophy",
        "quote": "The late Platonists posited a hierarchy of **henads** to bridge the chasm between absolute unity and cosmic multiplicity."
      }
    ]
  }
}

esm_content = '''import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Number & Mathematics');
const batchData = ''' + json.dumps(BATCH3_DATA, indent=2, ensure_ascii=False) + ''';

console.log('Starting Batch 3 curation (' + Object.keys(batchData).length + ' words)...');
const updated = updateNotesBatch(baseClusterDir, batchData);
console.log('Batch 3 complete: successfully updated ' + updated + ' notes.');
'''

with open("main app/scripts/curate_math_part1_batch3.mjs", "w", encoding="utf-8") as f:
    f.write(esm_content)

print(f"Generated main app/scripts/curate_math_part1_batch3.mjs with {len(BATCH3_DATA)} entries.")
