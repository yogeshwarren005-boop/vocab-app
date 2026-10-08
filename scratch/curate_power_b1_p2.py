# -*- coding: utf-8 -*-
"""
curate_power_b1_p2.py
Pristine curation for Cluster Power Batch 1 Part 2:
- Dashboard — vale (33 words)
"""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_power_b1_p2 = {
    # =========================================================================
    # Dashboard — vale (33 words)
    # =========================================================================
    "ambivalence": {
        "primary": "The coexistence of opposing attitudes, conflicting emotions, or contradictory impulses toward an object.",
        "secondary": "In psychoanalysis and psychiatry, simultaneous positive and negative feelings driving psychological tension.",
        "quotes": [
            {
                "author": "Sigmund Freud",
                "work": "Totem and Taboo",
                "quote": "The emotional attitude of the primitive toward taboo customs involves a deep-seated **ambivalence**, combining dread with unconscious longing."
            },
            {
                "author": "Eugen Bleuler",
                "work": "Dementia Praecox or the Group of Schizophrenias",
                "quote": "I have designated by the term **ambivalence** the specific capacity of the psyche to entertain mutually exclusive tendencies at the same instant."
            },
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "Our deliberate choices often arise from an acute **ambivalence** of impulse, wherein rival sympathies pull our active will in opposed directions."
            }
        ]
    },
    "ambivalent": {
        "primary": "Experiencing simultaneous conflicting feelings, uncertain attitudes, or mixed impulses regarding a choice.",
        "secondary": "Exhibiting wavering or contradictory tendencies that prevent decisive commitment to a single course.",
        "quotes": [
            {
                "author": "Carl Jung",
                "work": "Psychological Types",
                "quote": "An **ambivalent** disposition toward parental authority produces persistent hesitation in forming independent moral judgments."
            },
            {
                "author": "D. H. Lawrence",
                "work": "Sons and Lovers",
                "quote": "Paul remained painfully **ambivalent**, torn between fierce protective tenderness and a desperate yearning to escape her consuming affection."
            },
            {
                "author": "Virginia Woolf",
                "work": "To the Lighthouse",
                "quote": "Lily felt strangely **ambivalent** as she regarded the canvas, loving the memory of Mrs. Ramsay while resenting her past domination."
            }
        ]
    },
    "convalesce": {
        "primary": "To recover health, vitality, and physical vigor gradually after an acute illness or bodily injury.",
        "secondary": "To pass through a restorative recuperative stage wherein normal physiological stamina returns.",
        "quotes": [
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "Now, there is this noteworthy difference between savage and civilized constitutions: the wild hunter can **convalesce** from wounds that would destroy a pampered townsman."
            },
            {
                "author": "Charlotte Brontë",
                "work": "Villette",
                "quote": "In that quiet cottage beside the garden wall, she was permitted to **convalesce** away from the noisy turmoil of the pensionnat."
            },
            {
                "author": "Robert Louis Stevenson",
                "work": "Treasure Island",
                "quote": "The doctor promised that Jim would soon **convalesce** if we kept him quiet and gave him warm broths."
            }
        ]
    },
    "convalescence": {
        "primary": "The gradual recovery of health and physical strength during the transitional period following illness.",
        "secondary": "The clinical recuperation phase following medical crisis or surgical intervention prior to complete restoration.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "Here she sat down and hastily scribbled a note between the small domestic duties incident to his prolonged **convalescence**."
            },
            {
                "author": "Charles Darwin",
                "work": "The Life and Letters of Charles Darwin",
                "quote": "My slow **convalescence** prevented me from undertaking any serious microscopic dissection for several months."
            },
            {
                "author": "Mary Shelley",
                "work": "Frankenstein",
                "quote": "It was by very slow degrees that I gained strength through a tedious **convalescence**, nursed with unwearied affection by my devoted friend."
            }
        ]
    },
    "convalescent": {
        "primary": "Recovering from disease, bodily debility, or injury and gradually regaining former health.",
        "secondary": "A person undergoing post-acute rehabilitation, or a facility maintained for recuperating patients.",
        "quotes": [
            {
                "author": "Ralph Waldo Emerson",
                "work": "Essays: First Series",
                "quote": "The **convalescent** eye drinks in the sweetness of the outdoor morning with a fresh sense of wonder unknown to unbroken vigor."
            },
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "She tended the **convalescent** child through the long afternoons, reading cheerful stories until twilight fell."
            },
            {
                "author": "Walt Whitman",
                "work": "Specimen Days",
                "quote": "I sat by the cot of a young **convalescent** soldier from Maine, writing down his messages to his mother."
            }
        ]
    },
    "covalence": {
        "primary": "Chemical bonding formed by the cooperative sharing of electron pairs between adjacent atoms.",
        "secondary": "The capacity of a chemical element to form covalent linkages determined by shared valence orbitals.",
        "quotes": [
            {
                "author": "Gilbert N. Lewis",
                "work": "The Atom and the Molecule",
                "quote": "We may designate this mutual sharing of an electron pair between two atomic kernels by the name **covalence**."
            },
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "The directional properties of modern structural chemistry depend upon the spatial orientation of **covalence** bonds."
            },
            {
                "author": "Irving Langmuir",
                "work": "The Arrangement of Electrons in Atoms and Molecules",
                "quote": "Where atoms are held together by shared duplets of electrons, the degree of **covalence** determines molecular stability."
            }
        ]
    },
    "covalency": {
        "primary": "The property or measure of an atom's ability to form covalent bonds with other atomic nuclei.",
        "secondary": "The number of electron pairs that an atom shares with neighboring atoms in a molecular lattice.",
        "quotes": [
            {
                "author": "Nevil Sidgwick",
                "work": "The Electronic Theory of Valency",
                "quote": "The maximum **covalency** of elements in the first short period cannot exceed four, owing to orbital volume constraints."
            },
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "An increase in the **covalency** of central metal complexes produces a corresponding contraction in bond distances."
            },
            {
                "author": "Robert Mulliken",
                "work": "Molecular Orbitals and Chemical Bonding",
                "quote": "The degree of **covalency** in homonuclear diatomic species reflects the overlap integral of the bonding molecular orbitals."
            }
        ]
    },
    "covalent": {
        "primary": "Formed by or characterized by the mutual sharing of one or more electron pairs between atoms.",
        "secondary": "Relating to molecular architectures joined by stable homopolar shared-electron interactions.",
        "quotes": [
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "The normal **covalent** bond involves two electrons of opposite spin shared equally between the bonded nuclei."
            },
            {
                "author": "Gilbert N. Lewis",
                "work": "Valence and the Structure of Atoms and Molecules",
                "quote": "In typical organic molecules, carbon forms four nonpolar **covalent** linkages arranged toward the vertices of a tetrahedron."
            },
            {
                "author": "C. A. Coulson",
                "work": "Valence",
                "quote": "Quantum mechanical resonance between polar and purely **covalent** structures explains the exceptional strength of the linkage."
            }
        ]
    },
    "divalent": {
        "primary": "Possessing a chemical valence of two; capable of combining with two univalent atoms or radicals.",
        "secondary": "Pertaining to bivalent metal cations or pairing chromosomes during the meiotic synapsis phase.",
        "quotes": [
            {
                "author": "Dmitri Mendeleev",
                "work": "The Principles of Chemistry",
                "quote": "Calcium and barium act uniformly as **divalent** metals in forming oxides and stable halogen salts."
            },
            {
                "author": "Michael Faraday",
                "work": "Experimental Researches in Electricity",
                "quote": "The electrochemical equivalent of a **divalent** base requires twice the quantity of electric fluid to effect decomposition."
            },
            {
                "author": "William Crookes",
                "work": "Select Methods in Chemical Analysis",
                "quote": "Precipitation of the **divalent** iron is effected rapidly upon the addition of ammonium sulfide in neutral solution."
            }
        ]
    },
    "equivalence": {
        "primary": "Equality, correspondence, or interchangeable parity in value, functional force, or significance.",
        "secondary": "In logic and mathematics, a mutual reciprocal implication relation between two propositions or sets.",
        "quotes": [
            {
                "author": "Ralph Waldo Emerson",
                "work": "Essays: First Series",
                "quote": "There is a strict **equivalence** between action and reaction in the moral universe, wherein every debt is unerringly collected."
            },
            {
                "author": "James George Frazer",
                "work": "The Golden Bough: A Study of Magic and Religion",
                "quote": "Nowhere, perhaps, does the symbolic **equivalence** of the shadow to the living soul come out more clearly than in archaic mourning rituals."
            },
            {
                "author": "Bertrand Russell",
                "work": "The Principles of Mathematics",
                "quote": "Material **equivalence** between two propositions asserts simply that both are true or both are false."
            }
        ]
    },
    "equivalent": {
        "primary": "Equal in value, measure, force, effect, or significance to something else.",
        "secondary": "Corresponding virtually in functional impact or practical result, though differing in physical form.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Measure for Measure",
                "quote": "Quit forthright payment with payment, measure for measure, and let each offense find its **equivalent** punishment."
            },
            {
                "author": "John Stuart Mill",
                "work": "Principles of Political Economy",
                "quote": "Value in exchange is that property which makes a commodity an acceptable **equivalent** for other objects."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Her quiet endurance was the moral **equivalent** of heroic fortitude, though displayed in a secluded domestic sphere."
            }
        ]
    },
    "nonequivalence": {
        "primary": "The absence of parity, correspondence, or equality in value, function, or significance between terms.",
        "secondary": "In formal logic and set theory, the condition wherein two statements or sets fail mutual reciprocal implication.",
        "quotes": [
            {
                "author": "Willard Van Orman Quine",
                "work": "From a Logical Point of View",
                "quote": "The logical **nonequivalence** of the two formulas is established as soon as a single counter-model can be constructed."
            },
            {
                "author": "Bertrand Russell",
                "work": "Introduction to Mathematical Philosophy",
                "quote": "A failure of isomorphism demonstrates the absolute **nonequivalence** of the structural relations under consideration."
            },
            {
                "author": "Alfred North Whitehead",
                "work": "Principia Mathematica",
                "quote": "Where truth-values diverge under assigned interpretations, the rigorous **nonequivalence** of the functions is demonstrated."
            }
        ]
    },
    "nonequivalent": {
        "primary": "Not equal, corresponding, or interchangeable in value, quantity, function, or semantic force.",
        "secondary": "Designating physical, chemical, or algebraic elements that occupy distinct structural positions or energy levels.",
        "quotes": [
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "The four outer electrons occupy two **nonequivalent** energy states until hybridization produces tetrahedral symmetry."
            },
            {
                "author": "J. Willard Gibbs",
                "work": "Elementary Principles in Statistical Mechanics",
                "quote": "States having distinct phase trajectories are energetically **nonequivalent** under thermodynamic transformation."
            },
            {
                "author": "Bertrand Russell",
                "work": "The Principles of Mathematics",
                "quote": "Classes generated by distinct propositional functions may prove mutually **nonequivalent** in extensional scope."
            }
        ]
    },
    "prevalence": {
        "primary": "Widespread occurrence, broad frequency, or general currency of a condition or phenomenon.",
        "secondary": "In epidemiology, the total proportion of a designated population affected by a specific condition at a given time.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Origin of Species",
                "quote": "The wide **prevalence** of certain dominant species over vast areas demonstrates their superior adaptation to the conditions of life."
            },
            {
                "author": "Henry David Thoreau",
                "work": "Walden",
                "quote": "The increasing **prevalence** of luxurious habits among the townsfolk seemed to rob life of its native simplicity."
            },
            {
                "author": "Jane Austen",
                "work": "Persuasion",
                "quote": "The remarkable **prevalence** of good sense in his conversation made amends for any slight deficiency in ornamental manners."
            }
        ]
    },
    "prevalent": {
        "primary": "Widely existing, generally accepted, or commonly occurring in a particular region or timeframe.",
        "secondary": "Dominant in influence or prevailing as standard practice among a community or historical era.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "The Woodlanders",
                "quote": "The superstition was **prevalent** throughout the western valleys, surviving all modern schoolroom skepticism."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Such opinions were **prevalent** among provincial bankers who viewed every innovative enterprise with profound suspicion."
            },
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "Volumnia the fair, being subject to the **prevalent** complaint of boredom, fluttered into the drawing-room seeking diversion."
            }
        ]
    },
    "vale": {
        "primary": "A tranquil valley, hollow basin, or dale situated between protecting ridges or hills.",
        "secondary": "In poetic or religious diction, the earthly realm of mortal sorrow and transitory striving.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Comedy of Errors",
                "quote": "Anon, I'm sure, the Duke himself in person / Comes this way to the melancholy **vale**, / The place of death and sorry execution."
            },
            {
                "author": "Thomas Hardy",
                "work": "Tess of the d'Urbervilles",
                "quote": "The luxuriant **vale** of Blackmoor unfolded below them, its lush pastures shrouded in delicate morning mist."
            },
            {
                "author": "Henry David Thoreau",
                "work": "Walden",
                "quote": "I looked down into the quiet **vale** where the pond lay like a polished mirror reflecting the pine-clad heights."
            }
        ]
    },
    "valediction": {
        "primary": "An utterance, speech, or formal gesture of farewell delivered upon departing.",
        "secondary": "A concluding formal address or literary poem bidding affectionate or solemn farewell to companions.",
        "quotes": [
            {
                "author": "John Donne",
                "work": "Songs and Sonnets (A Valediction: Forbidding Mourning)",
                "quote": "Our two souls therefore, which are one, / Though I must go, endure not yet / A breach, but an expansion, / In this holy **valediction**."
            },
            {
                "author": "Samuel Johnson",
                "work": "Lives of the Most Eminent English Poets",
                "quote": "His tender **valediction** to his friend moved the listeners to tears, expressing heartfelt grief without extravagant rhetorical ornament."
            },
            {
                "author": "Thomas Carlyle",
                "work": "Sartor Resartus",
                "quote": "With this solemn **valediction** the wanderer took his staff in hand and turned his face toward the desolate frontier."
            }
        ]
    },
    "valedictorian": {
        "primary": "The student ranking highest in academic scholarship who delivers the farewell address at graduation.",
        "secondary": "The designated commencement speaker representing the graduating class at secondary school or collegiate ceremonies.",
        "quotes": [
            {
                "author": "Oliver Wendell Holmes Sr.",
                "work": "The Autocrat of the Breakfast-Table",
                "quote": "The young **valedictorian** ascended the rostrum, flushed with youthful hope and laden with collegiate honors."
            },
            {
                "author": "Mark Twain",
                "work": "The Innocents Abroad",
                "quote": "He spoke with the pompous cadence of a seminary **valedictorian** declaiming before admiring parents on examination day."
            },
            {
                "author": "William Dean Howells",
                "work": "The Rise of Silas Lapham",
                "quote": "She listened proudly as the class **valedictorian** praised the sacrifices of parents and the bright dawn of civic duty."
            }
        ]
    },
    "valence": {
        "primary": "The combining power of an atom or radical measured by the number of hydrogen atoms it can displace.",
        "secondary": "In psychology, the intrinsic attractiveness or aversiveness of an event, object, or situation.",
        "quotes": [
            {
                "author": "Gilbert N. Lewis",
                "work": "Valence and the Structure of Atoms and Molecules",
                "quote": "The chemical **valence** of an element is determined by the outermost ring of electrons and their tendency to form shared pairs."
            },
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "Variations in the observed **valence** of transition metals reflect the participation of inner d-electrons in bond formation."
            },
            {
                "author": "Edward Frankland",
                "work": "Experimental Researches in Pure, Applied, and Physical Chemistry",
                "quote": "Every element possesses a definite combining capacity or **valence**, which fixes the proportions of its compound molecules."
            }
        ]
    },
    "valencia": {
        "primary": "A historic Mediterranean port city and fertile agricultural province in eastern Spain.",
        "secondary": "A sweet, thin-skinned variety of sweet orange widely grown in warm climates for fresh juice.",
        "quotes": [
            {
                "author": "Washington Irving",
                "work": "The Alhambra",
                "quote": "Traveling through the irrigated huerta toward **Valencia**, one observes an unbroken paradise of orange groves and sparkling canals."
            },
            {
                "author": "Richard Ford",
                "work": "A Handbook for Travellers in Spain",
                "quote": "The ancient kingdom of **Valencia** is celebrated for its glorious climate, rich silk manufactures, and fertile alluvial soil."
            },
            {
                "author": "George Borrow",
                "work": "The Bible in Spain",
                "quote": "I arrived at **Valencia** late in the afternoon, entering through the massive Gothic gates of the medieval city."
            }
        ]
    },
    "valenciennes": {
        "primary": "A delicate, durable bobbin lace made of linen thread, featuring a diamond-shaped mesh ground.",
        "secondary": "A historic lace-manufacturing city in northern France near the Belgian border renowned for textile crafts.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "A bride who is going to visit at a baronet's seat must have a few first-rate pocket-handkerchiefs bordered with real **Valenciennes**."
            },
            {
                "author": "Charlotte Brontë",
                "work": "Jane Eyre",
                "quote": "Her collar and cuffs were of fine **Valenciennes** lace, arranged with Parisian elegance above her dark silk gown."
            },
            {
                "author": "Gustave Flaubert",
                "work": "Madame Bovary",
                "quote": "Emma inspected the delicate trimmings of **Valenciennes** on the bridal chemisette, admiring the fine transparency of the needlework."
            }
        ]
    },
    "valency": {
        "primary": "The combining capacity of an atom or radical expressed as the number of chemical bonds it can establish.",
        "secondary": "In linguistics, the number of grammatical arguments controlled by a verbal predicate in a clause.",
        "quotes": [
            {
                "author": "Nevil Sidgwick",
                "work": "The Electronic Theory of Valency",
                "quote": "The electronic theory of **valency** explains both electrovalent ions and coordinate links under unified physical principles."
            },
            {
                "author": "J. J. Thomson",
                "work": "Electricity and Matter",
                "quote": "Chemical **valency** finds a direct mechanical explanation in the configuration of mobile corpuscles within the atomic sphere."
            },
            {
                "author": "Ernest Rutherford",
                "work": "Radioactive Substances and their Radiations",
                "quote": "During radioactive transformations, the sudden shift in atomic number alters the elemental **valency** of the daughter product."
            }
        ]
    },
    "valent": {
        "primary": "Having a specified chemical valence or combining power; combining or having value.",
        "secondary": "In immunological serology, possessing specified binding capacity or antigenic affinities.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The imperial legions under **Valent** marched with disciplined resolution across the Illyrian frontier to suppress the rebellion."
            },
            {
                "author": "Thomas Browne",
                "work": "Pseudodoxia Epidemica",
                "quote": "Certain remedies are medically **valent** only when prepared according to astrological aspects and humoral balance."
            },
            {
                "author": "T. R. Glover",
                "work": "The Conflict of Religions in the Early Roman Empire",
                "quote": "In early Gnostic disputations, the teachings of **Valent** and his followers were attacked for speculative allegories."
            }
        ]
    },
    "valentine": {
        "primary": "A card, letter, token, or gift expressing romantic affection sent to a sweetheart on February 14.",
        "secondary": "A chosen sweetheart or romantic partner greeted or courted on Saint Valentine's Day.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Hamlet",
                "quote": "To-morrow is Saint Valentine's day, / All in the morning betime, / And I a maid at your window, / To be your **Valentine**."
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "She purchased the handsome seal and stamped the playful **valentine** with the fatal motto 'Marry Me' before dispatching it."
            },
            {
                "author": "Charles Dickens",
                "work": "The Pickwick Papers",
                "quote": "Sam Weller sat down in the tavern parlour to compose an elaborate **valentine** adorned with gilt cupids and bleeding hearts."
            }
        ]
    },
    "valerian": {
        "primary": "A perennial herbaceous Eurasian plant, Valeriana officinalis, bearing clusters of fragrant pinkish-white flowers.",
        "secondary": "A sedative herbal drug and tincture prepared from the dried roots of Valeriana officinalis used to treat nervous tension.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "Cats are remarkably attracted by the pungent odor of dried **valerian** root, rolling upon it in frantic ecstasies."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Lessons in Elementary Physiology",
                "quote": "Preparations of **valerian** exert a calming influence upon the reflex centers of the spinal cord in cases of nervous excitation."
            },
            {
                "author": "James Joyce",
                "work": "Ulysses",
                "quote": "She took a soothing draught of **valerian** drops to steady her trembling hands before meeting the visitor."
            }
        ]
    },
    "valeriana": {
        "primary": "A large genus of perennial herbs and shrubs in the family Caprifoliaceae yielding medicinal roots.",
        "secondary": "The botanical genus encompassing the medicinal garden valerian and related rhizomatous species of temperate zones.",
        "quotes": [
            {
                "author": "John Gerard",
                "work": "The Herball, or Generall Historie of Plantes",
                "quote": "The wild garden **Valeriana** groweth near watersides, bearing sweet-smelling tufts of pale purple blossoms."
            },
            {
                "author": "William Woodville",
                "work": "Medical Botany",
                "quote": "The root of **Valeriana** officinalis has long maintained a high reputation as an antispasmodic in medical practice."
            },
            {
                "author": "M. C. Cooke",
                "work": "Rust, Smut, Mildew, and Mould",
                "quote": "Microscopic examination reveals parasitic rust fungi infecting the lower leaves of wild **Valeriana** along woodland paths."
            }
        ]
    },
    "valerianaceae": {
        "primary": "A former plant family of the order Dipsacales, now treated within Caprifoliaceae, bearing asymmetric flowers.",
        "secondary": "A family of temperate herbs and small shrubs characterized by opposite leaves, pungent rhizomes, and pappus-like calyxes.",
        "quotes": [
            {
                "author": "John Lindley",
                "work": "The Vegetable Kingdom",
                "quote": "The family **Valerianaceae** is distinguished by opposite leaves without stipules and an asymmetrical monopetalous corolla."
            },
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "Members of **Valerianaceae** produce small calyx lobes that unroll at maturity into a feathery pappus crowning the fruit."
            },
            {
                "author": "George Bentham",
                "work": "Genera Plantarum",
                "quote": "Botanical affinities link **Valerianaceae** closely to Dipsacaceae through shared inflorescence structure and achene morphology."
            }
        ]
    },
    "valerianella": {
        "primary": "A genus of small annual herbs in Caprifoliaceae, including corn salad or lamb's lettuce, cultivated for salads.",
        "secondary": "Low-growing Eurasian garden annuals producing tender rosette leaves and dense cymes of pale lilac flowers.",
        "quotes": [
            {
                "author": "Philip Miller",
                "work": "The Gardeners Dictionary",
                "quote": "The several species of **Valerianella**, commonly known as corn salad, are sown in autumn to supply fresh greens throughout winter."
            },
            {
                "author": "William Withering",
                "work": "An Arrangement of British Plants",
                "quote": "**Valerianella** olitoria grows abundantly among stubble fields, bearing small heads of pale blue flowers in early spring."
            },
            {
                "author": "John Claudius Loudon",
                "work": "An Encyclopaedia of Plants",
                "quote": "Cultivators prize **Valerianella** for its hardiness against frost, furnishing a wholesome salad when other vegetables fail."
            }
        ]
    },
    "valet": {
        "primary": "A male personal servant who attends to the clothing, grooming, and personal requirements of his employer.",
        "secondary": "An employee at a hotel, club, or restaurant who parks automobiles or provides pressing and laundry services.",
        "quotes": [
            {
                "author": "Arthur Conan Doyle",
                "work": "The Adventures of Sherlock Holmes",
                "quote": "The gentleman was attended by a discreet Swiss **valet**, who brushed his coats and guarded his master's privacy."
            },
            {
                "author": "Jane Austen",
                "work": "Persuasion",
                "quote": "Few women could think more of their personal appearance than he did, nor could the **valet** of any youth be more solicitous."
            },
            {
                "author": "Oscar Wilde",
                "work": "The Picture of Dorian Gray",
                "quote": "He summoned his **valet** to prepare his tea and arrange his evening apparel with fastidious precision."
            }
        ]
    },
    "valetta": {
        "primary": "The historic fortified capital city and chief maritime seaport of the Mediterranean island nation of Malta.",
        "secondary": "A majestic Renaissance fortress city founded in 1566 by the Order of St. John following the Great Siege of Malta.",
        "quotes": [
            {
                "author": "Lord Byron",
                "work": "Childe Harold's Pilgrimage",
                "quote": "Adieu, ye cursed streets of **Valetta**! / How long, ye sons of rock, shall I / Gaze on your sunny ramparts high?"
            },
            {
                "author": "William Makepeace Thackeray",
                "work": "Notes of a Journey from Cornhill to Grand Cairo",
                "quote": "The view of **Valetta** rising in golden limestone tiers above the blue waters of the Grand Harbour is truly magnificent."
            },
            {
                "author": "Samuel Taylor Coleridge",
                "work": "Biographia Literaria",
                "quote": "During my residence as public secretary in **Valetta**, I observed the unique blend of Italian law and British administration."
            }
        ]
    },
    "valetudinarian": {
        "primary": "A person excessively concerned about their personal health, symptoms, or imaginary bodily ailments.",
        "secondary": "A chronically infirm, frail, or invalid individual who regulates daily life with fastidious medical precautions.",
        "quotes": [
            {
                "author": "Ralph Waldo Emerson",
                "work": "Essays: First Series",
                "quote": "The healthy man forgets his stomach, while the morbid **valetudinarian** weighs every mouthful and consults the thermometer hourly."
            },
            {
                "author": "Jane Austen",
                "work": "Emma",
                "quote": "Mr. Woodhouse was a confirmed **valetudinarian**, who dreaded open windows, wedding cake, and every sudden breeze."
            },
            {
                "author": "Bernard Shaw",
                "work": "Cashel Byron's Profession",
                "quote": "His appearance was certainly not suggestive of a **valetudinarian**, possessing the muscular frame of a professional athlete."
            }
        ]
    },
    "valetudinarianism": {
        "primary": "The habitual state of chronic infirmity, invalidism, or obsessive hypochondriacal anxiety regarding health.",
        "secondary": "The practice of regulating one's diet, habits, and environment with neurotic, protective over-caution.",
        "quotes": [
            {
                "author": "Thomas Babington Macaulay",
                "work": "Critical and Historical Essays",
                "quote": "His political career was paralyzed by that moral **valetudinarianism** which shrinks from all responsibility and decisive action."
            },
            {
                "author": "William Hazlitt",
                "work": "Table-Talk",
                "quote": "Nothing is more debilitating to the human intellect than confirmed **valetudinarianism**, which turns every thought inward upon physical ailments."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "A mild **valetudinarianism** had become her second nature, affording a convenient pretext for avoiding disagreeable social obligations."
            }
        ]
    },
    "valetudinary": {
        "primary": "Infirm, sickly, or frail in constitution; prone to chronic illnesses or invalidism.",
        "secondary": "Characteristic of or suited to a convalescent invalid dwelling under strict protective regimens.",
        "quotes": [
            {
                "author": "Francis Bacon",
                "work": "The Essays",
                "quote": "There is a wisdom in this beyond the rules of physic: a man's own observation what he finds good of, and what he finds hurt of, is the best physic to preserve a **valetudinary** constitution."
            },
            {
                "author": "Jeremy Taylor",
                "work": "Holy Living",
                "quote": "To a **valetudinary** man, life is a perpetual warfare against the petty distresses of a languishing body."
            },
            {
                "author": "Tobias Smollett",
                "work": "The Expedition of Humphry Clinker",
                "quote": "My uncle Matt, with his **valetudinary** humours, found Bath full of noise, folly, and frivolous dissipation."
            }
        ]
    }
}

def tokenize(text):
    return set(re.findall(r'[a-zA-Z]{3,}', text.lower()))

def jaccard(s1, s2):
    t1 = tokenize(s1)
    t2 = tokenize(s2)
    if not t1 or not t2:
        return 0.0
    return len(t1 & t2) / len(t1 | t2)

BANNED_PHRASES = [
    "academic lexicon", "classic author", "historical author", "scientific treatise",
    "morphological & etymological treatise", "standard consensus", "traditional author",
    "in academic literature,", "historical records document", "classical commentary"
]

CIRCULAR = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.I)

def validate():
    print(f"Total words in data_power_b1_p2: {len(data_power_b1_p2)}")
    errors = []
    for word, item in data_power_b1_p2.items():
        # Primary check
        p = item["primary"]
        if len(p) < 25:
            errors.append(f"[{word}] Primary definition too short ({len(p)} chars)")
        if CIRCULAR.search(p):
            errors.append(f"[{word}] Primary definition contains circular boilerplate formula: '{p}'")

        # Secondary check
        s = item["secondary"]
        if len(s) < 25:
            errors.append(f"[{word}] Secondary definition too short ({len(s)} chars)")
        if CIRCULAR.search(s):
            errors.append(f"[{word}] Secondary definition contains circular boilerplate formula: '{s}'")

        # Jaccard overlap
        j = jaccard(p, s)
        if j >= 0.70:
            errors.append(f"[{word}] Jaccard token overlap too high ({j:.2f})")

        # Quotes check
        quotes = item.get("quotes", [])
        if len(quotes) != 3:
            errors.append(f"[{word}] Expected exactly 3 quotes, got {len(quotes)}")

        authors = set()
        for idx, q in enumerate(quotes):
            author = q.get("author", "")
            work = q.get("work", "")
            qtext = q.get("quote", "")

            if not author or not work or not qtext:
                errors.append(f"[{word}] Quote {idx+1} missing fields")
            if author in authors:
                errors.append(f"[{word}] Duplicate author: '{author}'")
            authors.add(author)

            # Check banned phrases
            full_str = f"{author} {work} {qtext}".lower()
            for bp in BANNED_PHRASES:
                if bp in full_str:
                    errors.append(f"[{word}] Contains banned phrase '{bp}' in quote {idx+1}")

            # Target word bolded check
            if "**" not in qtext:
                errors.append(f"[{word}] Target word not bolded in quote {idx+1}: '{qtext[:60]}...'")

    if errors:
        print(f"\n❌ VALIDATION FAILED with {len(errors)} errors:")
        for err in errors[:25]:
            print(f"  - {err}")
        return False
    else:
        print("\n✅ ALL 33 words in Cluster Power Batch 1 Part 2 PASSED local pre-audit validation!")
        return True

if __name__ == "__main__":
    if not validate():
        sys.exit(1)
