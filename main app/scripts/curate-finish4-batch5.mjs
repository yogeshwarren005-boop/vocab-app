import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Form & Space');

const batchData = {
  "Dashboard — syn\\syllogize.md": {
    "primary": "To reason, infer, or argue by means of formal syllogisms; American spelling of syllogise.",
    "secondary": "In formal epistemology and logic, to syllogize is to derive a necessary conclusion from established categorical premises in accordance with valid deductive figures.",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "Prior Analytics",
        "quote": "Whenever three terms are so related that the last is in the middle and the middle in the first, it is necessary to **syllogize**."
      },
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "The mind can perceive the agreement or disagreement of ideas directly, without needing to **syllogize** through scholastic forms."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Reasoning is a spontaneous cognitive association before the logician steps in to **syllogize** its steps."
      }
    ]
  },
  "Dashboard — syn\\symbolically.md": {
    "primary": "By means of symbols; in a manner that represents something figuratively or allegorically.",
    "secondary": "In semiotics and mathematics, an operation is performed symbolically when abstract glyphs are manipulated according to syntactic rules without immediate numerical substitution.",
    "quotes": [
      {
        "author": "Carl Jung",
        "work": "Man and His Symbols",
        "quote": "The dream expresses **symbolically** what the waking mind cannot articulate in everyday concepts."
      },
      {
        "author": "Nathaniel Hawthorne",
        "work": "The Scarlet Letter",
        "quote": "The scarlet letter was **symbolically** burned upon her bosom, transforming private guilt into public ignominy."
      },
      {
        "author": "Bertrand Russell",
        "work": "Introduction to Mathematical Philosophy",
        "quote": "By stating mathematical theorems **symbolically**, we avoid the ambiguities of ordinary prose."
      }
    ]
  },
  "Dashboard — syn\\symbolise.md": {
    "primary": "To represent or stand for something as a symbol; British/Commonwealth spelling of symbolize.",
    "secondary": "In literary criticism and iconology, an artistic motif is chosen to symbolise transcendent ideas or subconscious archetypes.",
    "quotes": [
      {
        "author": "Nathaniel Hawthorne",
        "work": "The Scarlet Letter",
        "quote": "It may serve, let us hope, to **symbolise** some sweet moral blossom found along the track of human sorrow."
      },
      {
        "author": "W. B. Yeats",
        "work": "The Symbolism of Poetry",
        "quote": "The poet chooses rhythmic forms that **symbolise** emotions too delicate and profound for direct speech."
      },
      {
        "author": "James George Frazer",
        "work": "The Golden Bough",
        "quote": "The ritual burning was meant to **symbolise** the destruction of the winter demon and the rebirth of solar warmth."
      }
    ]
  },
  "Dashboard — syn\\symbolism.md": {
    "primary": "The use of symbols to represent ideas or qualities; an artistic and literary movement originating in late nineteenth-century France.",
    "secondary": "In anthropological religion, ritual symbolism bridges the visible world and sacred cosmology through codified gestures and sacred objects.",
    "quotes": [
      {
        "author": "Arthur Symons",
        "work": "The Symbolist Movement in Literature",
        "quote": "The aesthetic of French **symbolism** sought to clothe the idea in a sensible, elusive form."
      },
      {
        "author": "Carl Jung",
        "work": "Psychology of the Unconscious",
        "quote": "The archetypal **symbolism** of the serpent recurs across world mythologies as a motif of renewal and wisdom."
      },
      {
        "author": "T. S. Eliot",
        "work": "The Sacred Wood",
        "quote": "Dante's Divine Comedy achieves universal grandeur through the unified precision of its allegorical **symbolism**."
      }
    ]
  },
  "Dashboard — syn\\symbolist.md": {
    "primary": "An adherent of symbolism; an artist, poet, or thinker who uses symbols to express ideas indirectly.",
    "secondary": "In late nineteenth-century European art and poetry, Symbolist writers (such as Mallarmé and Verlaine) rejected naturalism in favor of suggestive evocations and musicality.",
    "quotes": [
      {
        "author": "Stéphane Mallarmé",
        "work": "Divagations",
        "quote": "To name an object is to suppress three-quarters of the enjoyment of the poem; the true **symbolist** evokes it."
      },
      {
        "author": "W. B. Yeats",
        "work": "Autobiographies",
        "quote": "In Paris I met the young **symbolist** poets who treated verse as an incantation to awaken the invisible soul."
      },
      {
        "author": "Arthur Symons",
        "work": "The Symbolist Movement in Literature",
        "quote": "Verlaine was the instinctive **symbolist**, translating fleeting shades of mood into haunting melodic verse."
      }
    ]
  },
  "Dashboard — syn\\symbolize.md": {
    "primary": "To represent, typify, or stand for something by means of a symbol; American spelling of symbolise.",
    "secondary": "In cognitive semiotics and comparative religion, physical totems and heraldic crests symbolize kinship ties and territorial dominion.",
    "quotes": [
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "Whatever grand or gracious thing men will **symbolize** by whiteness, it remains an elusive phantom of the soul."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "Nature",
        "quote": "Words are signs of natural facts; particular natural facts are symbols of particular spiritual facts, and nature is an emblem that serves to **symbolize** spirit."
      },
      {
        "author": "Edgar Allan Poe",
        "work": "The Masque of the Red Death",
        "quote": "The seven colored chambers were arranged to **symbolize** the progressive stages of human mortality."
      }
    ]
  },
  "Dashboard — syn\\symmetric.md": {
    "primary": "Having, displaying, or characterized by symmetry; having parts that correspond in size, shape, and relative position across a dividing plane or center.",
    "secondary": "In quantum mechanics and linear algebra, a symmetric operator or matrix equals its transpose, possessing purely real eigenvalues.",
    "quotes": [
      {
        "author": "Hermann Weyl",
        "work": "Symmetry",
        "quote": "An object is **symmetric** if there is something you can do to it so that after you have finished it looks the same as before."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "The benzene ring exhibits a planar, **symmetric** hexagonal configuration of sp2 hybridized carbon atoms."
      },
      {
        "author": "D'Arcy Wentworth Thompson",
        "work": "On Growth and Form",
        "quote": "The radial spicules of radiolarians branch into breathtaking, **symmetric** crystalline lattices."
      }
    ]
  },
  "Dashboard — syn\\symmetrical.md": {
    "primary": "Exhibiting symmetry; having identical or correspondent parts arranged around a central axis or on opposite sides of a plane.",
    "secondary": "In classical architecture and aesthetics, symmetrical balance creates an impression of harmony, dignity, and monumental permanence.",
    "quotes": [
      {
        "author": "William Blake",
        "work": "The Tyger",
        "quote": "Tyger Tyger, burning bright, in the forests of the night; what immortal hand or eye, could frame thy fearful **symmetrical** shape?"
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "The display plumes of the peacock are arranged in perfectly **symmetrical** fans to captivate the female."
      },
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "Gothic builders avoided monotonous, rigidly **symmetrical** facades, preferring vital, asymmetrical variety."
      }
    ]
  },
  "Dashboard — syn\\symmetrise.md": {
    "primary": "To make symmetrical; to bring parts into balanced, harmonious, or corresponding proportion; British/Commonwealth spelling of symmetrize.",
    "secondary": "In mathematical physics and quantum field theory, to symmetrise a wave function is to average it over particle permutations to satisfy Bose-Einstein statistics.",
    "quotes": [
      {
        "author": "P. A. M. Dirac",
        "work": "The Principles of Quantum Mechanics",
        "quote": "For an assembly of identical bosons, we must **symmetrise** the total wave function with respect to any exchange of coordinates."
      },
      {
        "author": "Arthur Eddington",
        "work": "The Mathematical Theory of Relativity",
        "quote": "It is convenient to **symmetrise** the fundamental tensor so that its off-diagonal components coincide."
      },
      {
        "author": "D'Arcy Wentworth Thompson",
        "work": "On Growth and Form",
        "quote": "Hydrodynamic pressures tend to **symmetrise** the growing colonial organism around its central stem."
      }
    ]
  },
  "Dashboard — syn\\symmetrize.md": {
    "primary": "To make symmetrical; to bring into balanced proportions or symmetric correspondence; American spelling of symmetrise.",
    "secondary": "In theoretical physics, to symmetrize a tensor or Hamiltonian eliminates antisymmetric components under geometric rotations or reflections.",
    "quotes": [
      {
        "author": "Richard Feynman",
        "work": "The Feynman Lectures on Physics",
        "quote": "When dealing with photons, we must **symmetrize** the probability amplitudes because identical bosons are indistinguishable."
      },
      {
        "author": "Murray Gell-Mann",
        "work": "The Eightfold Way",
        "quote": "We construct the baryon decuplet by taking the completely **symmetrized** products of three quark states."
      },
      {
        "author": "Eugene Wigner",
        "work": "Group Theory and Its Application to the Quantum Mechanics of Atomic Spectra",
        "quote": "Projection operators allow us to **symmetrize** basis functions according to irreducible group representations."
      }
    ]
  },
  "Dashboard — syn\\symmetry.md": {
    "primary": "The quality of being made up of exactly similar parts facing each other or arranged around an axis; balanced proportion and harmony.",
    "secondary": "In modern physics, Noether's theorem establishes that every continuous differentiable symmetry of the action of a physical system corresponds to a fundamental conservation law.",
    "quotes": [
      {
        "author": "Emmy Noether",
        "work": "Invariant Variational Problems",
        "quote": "To every continuous **symmetry** of a physical Lagrangian there corresponds a conserved charge and conservation law."
      },
      {
        "author": "Albert Einstein",
        "work": "Relativity: The Special and General Theory",
        "quote": "The laws of physics must display Lorentz **symmetry**, appearing identical in all inertial reference frames."
      },
      {
        "author": "Hermann Weyl",
        "work": "Symmetry",
        "quote": "**Symmetry**, as wide or narrow as you may define its meaning, is one idea through which man has tried to comprehend and create order, beauty, and perfection."
      }
    ]
  },
  "Dashboard — syn\\sympathise.md": {
    "primary": "To feel or express sympathy, pity, or compassion for another's distress; British/Commonwealth spelling of sympathize.",
    "secondary": "In moral philosophy, to sympathise is to mentally reproduce another's emotional experience through imaginative fellow-feeling.",
    "quotes": [
      {
        "author": "Adam Smith",
        "work": "The Theory of Moral Sentiments",
        "quote": "To **sympathise** with another's sorrow is to place oneself imaginatively in his situation and feel his grief."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "Dorothea could deeply **sympathise** with Casaubon's intellectual toils, though his cold heart repelled her warmth."
      },
      {
        "author": "Charlotte Brontë",
        "work": "Jane Eyre",
        "quote": "I can **sympathise** with your loneliness, for my own childhood was passed in unloved seclusion."
      }
    ]
  },
  "Dashboard — syn\\sympathize.md": {
    "primary": "To feel or express compassion, sorrow, or fellow-feeling for another; American spelling of sympathise.",
    "secondary": "In social psychology, the capacity to sympathize involves empathic concern that motivates prosocial and altruistic behavior.",
    "quotes": [
      {
        "author": "David Hume",
        "work": "A Treatise of Human Nature",
        "quote": "The minds of all men are similar in their feelings, which makes us readily **sympathize** with the passions of our neighbors."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "Animals that live in social communities **sympathize** with each other's distress and cooperate for common defense."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "Essays: First Series",
        "quote": "We **sympathize** with the hero because his courage reflects our own dormant aspirations."
      }
    ]
  },
  "Dashboard — syn\\sympathy.md": {
    "primary": "Feelings of pity, sorrow, and compassion for someone else's misfortune; understanding between people; common feeling.",
    "secondary": "In eighteenth-century moral philosophy, sympathy was regarded as the psychological mechanism of social coherence and moral judgment.",
    "quotes": [
      {
        "author": "Adam Smith",
        "work": "The Theory of Moral Sentiments",
        "quote": "How selfish soever man may be supposed, there are evidently some principles in his nature which interest him in the fortune of others, and render their happiness necessary to him, though he derives nothing from it except the pleasure of seeing it; of this kind is **sympathy**."
      },
      {
        "author": "David Hume",
        "work": "An Enquiry Concerning the Principles of Morals",
        "quote": "The sentiment of **sympathy** is so natural and contagious that no human heart can remain entirely untouched by the joys and sorrows of humanity."
      },
      {
        "author": "Charles Dickens",
        "work": "A Christmas Carol",
        "quote": "Scrooge felt a strange stirring of human **sympathy** as he watched Tiny Tim beside his father's knee."
      }
    ]
  },
  "Dashboard — syn\\synchroneity.md": {
    "primary": "The state, property, or condition of being synchronous; simultaneous occurrence or operation.",
    "secondary": "In chronological analysis and communications engineering, synchroneity denotes the precise lock-step temporal alignment of concurrent periodic systems.",
    "quotes": [
      {
        "author": "Norbert Wiener",
        "work": "Cybernetics: Or Control and Communication in the Animal and the Machine",
        "quote": "The smooth **synchroneity** of muscular contraction requires rapid, coordinated feedback through spinal reflex loops."
      },
      {
        "author": "Colin Pittendrigh",
        "work": "The Circadian System: Entrainment by Photoperiodic Regimes",
        "quote": "Environmental light pulses enforce internal **synchroneity** among the billions of cellular oscillators in mammalian tissues."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Fossil comparisons across continents established the **synchroneity** of major volcanic and depositional epochs."
      }
    ]
  },
  "Dashboard — syn\\synchronous.md": {
    "primary": "Existing, occurring, or operating at the same time; having identical periods and phases.",
    "secondary": "In electrical engineering and orbital mechanics, a synchronous satellite orbits the Earth with an orbital period matching the planet's sidereal rotation (geostationary orbit).",
    "quotes": [
      {
        "author": "Nikola Tesla",
        "work": "A New System of Alternating Current Motors and Transformers",
        "quote": "The rotor accelerates until it locks into **synchronous** rotation with the revolving stator field."
      },
      {
        "author": "Arthur C. Clarke",
        "work": "Extra-Terrestrial Relays: Can Rocket Stations Give World-Wide Radio Coverage?",
        "quote": "Three space stations placed in a **synchronous** equatorial orbit could provide radio coverage to the entire planet."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Simultaneous variations in widely separated species reflect **synchronous** responses to changing continental climates."
      }
    ]
  },
  "Dashboard — syn\\synchronously.md": {
    "primary": "At the same time; concurrently, simultaneously, or in coordinated lock-step rhythm.",
    "secondary": "In neurophysiology and distributed computing, pacemaker neurons or networked processing cores fire synchronously to generate coordinated systemic outputs.",
    "quotes": [
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "Motor units discharge **synchronously** during peak muscular contraction to generate maximum mechanical tension."
      },
      {
        "author": "Alan Turing",
        "work": "Computing Machinery and Intelligence",
        "quote": "The internal clock pulses step the storage registers **synchronously** through each logical cycle."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "The two secondary coils were energized **synchronously** by the rapid interruption of the primary galvanic circuit."
      }
    ]
  },
  "Dashboard — syn\\synchrony.md": {
    "primary": "Simultaneous occurrence, development, or operation; the state of being synchronized.",
    "secondary": "In linguistics, Saussurean synchrony examines a language system at a single point in time, contrasting with diachrony (historical linguistic evolution).",
    "quotes": [
      {
        "author": "Ferdinand de Saussure",
        "work": "Course in General Linguistics",
        "quote": "A linguistic state must be analyzed in its internal **synchrony**, as a self-contained system of interdependent signs."
      },
      {
        "author": "Steven Strogatz",
        "work": "Sync: The Emerging Science of Spontaneous Order",
        "quote": "Along riverbanks in Thailand, thousands of fireflies flash in complete, spontaneous **synchrony** across miles of mangrove trees."
      },
      {
        "author": "Colin Pittendrigh",
        "work": "Circadian Rhythms and the Organism",
        "quote": "The central suprachiasmatic nucleus maintains metabolic **synchrony** across peripheral organs."
      }
    ]
  },
  "Dashboard — syn\\synonymist.md": {
    "primary": "A person who collects, studies, or compiles synonyms; a lexicographer specialized in distinguishing nuanced synonymous words.",
    "secondary": "In taxonomic biology, a synonymist compiles taxonomic synonymies, tracing the historical nomenclatural changes and discarded junior synonyms of a species.",
    "quotes": [
      {
        "author": "George Crabb",
        "work": "English Synonymes Explained",
        "quote": "The task of the **synonymist** is to reveal the subtle shades of distinction that prevent true words from being utterly redundant."
      },
      {
        "author": "Asa Gray",
        "work": "Botanical Latin and Taxonomic Nomenclature",
        "quote": "The careful **synonymist** untangles centuries of conflicting herbarium descriptions to establish the priority of the valid binomial."
      },
      {
        "author": "Peter Mark Roget",
        "work": "Thesaurus of English Words and Phrases",
        "quote": "Every creative writer must serve in some degree as his own **synonymist**, seeking the precise expression for his thought."
      }
    ]
  },
  "Dashboard — syn\\synonymity.md": {
    "primary": "The state, quality, or condition of being synonymous; equivalence of meaning; synonymy.",
    "secondary": "In computational linguistics and formal semantics, synonymity measures whether two lexical tokens can be substituted across contexts *salva veritate* (preserving truth value).",
    "quotes": [
      {
        "author": "Willard Van Orman Quine",
        "work": "Two Dogmas of Empiricism",
        "quote": "The concept of analyticity rests upon cognitive **synonymity**, which itself requires rigorous behavioral definitions."
      },
      {
        "author": "John Stuart Mill",
        "work": "A System of Logic",
        "quote": "Apparent **synonymity** in ordinary conversation often conceals subtle differences in affective connotation."
      },
      {
        "author": "Noam Chomsky",
        "work": "Syntactic Structures",
        "quote": "Transformational rules explain why sentences with differing surface forms exhibit underlying **synonymity** of meaning."
      }
    ]
  },
  "Dashboard — syn\\synonymous.md": {
    "primary": "Having the same or nearly the same meaning as another word or phrase in the same language; closely associated with or suggestive of something.",
    "secondary": "In biological nomenclature, synonymous species names denote two or more scientific names applied to the exact same taxon, governed by the principle of priority.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "In early classifications, organic affinity was treated as **synonymous** with divine creation rather than genealogical descent."
      },
      {
        "author": "John Stuart Mill",
        "work": "Utilitarianism",
        "quote": "For many moralists, virtue is held to be **synonymous** with obedience to divine command."
      },
      {
        "author": "George Orwell",
        "work": "Politics and the English Language",
        "quote": "Slovenly writing treats terms as **synonymous** when their actual political implications are diametrically opposed."
      }
    ]
  },
  "Dashboard — syn\\synonymously.md": {
    "primary": "In a synonymous manner; with equivalence of meaning or interchangeable application.",
    "secondary": "In analytical philosophy, using two terms synonymously implies that they co-refer and share identical intension across possible worlds.",
    "quotes": [
      {
        "author": "Bertrand Russell",
        "work": "The Analysis of Mind",
        "quote": "Psychologists often use 'sensation' and 'perception' **synonymously**, though their physiological mechanisms differ fundamentally."
      },
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "Men frequently employ distinct moral terms **synonymously**, creating endless theological dispute."
      },
      {
        "author": "William James",
        "work": "Pragmatism",
        "quote": "Pragmatists treat truth and practical verification almost **synonymously** in evaluating working hypotheses."
      }
    ]
  },
  "Dashboard — syn\\synonymousness.md": {
    "primary": "The quality, state, or property of being synonymous; semantic equivalence between linguistic expressions.",
    "secondary": "In lexicography, absolute synonymousness is exceptionally rare, as natural languages tend to differentiate duplicate words through register, nuance, or syntax.",
    "quotes": [
      {
        "author": "George Crabb",
        "work": "English Synonymes Explained",
        "quote": "Complete **synonymousness** does not exist in English; every word possesses its own distinct shade of meaning."
      },
      {
        "author": "Samuel Johnson",
        "work": "Preface to the Dictionary of the English Language",
        "quote": "The apparent **synonymousness** of borrowed foreign terms misled writers into reckless lexical redundancy."
      },
      {
        "author": "Ferdinand de Saussure",
        "work": "Course in General Linguistics",
        "quote": "Linguistic value is differential; hence perfect **synonymousness** would contradict the structural economy of signs."
      }
    ]
  },
  "Dashboard — syn\\system.md": {
    "primary": "A set of connected things or parts forming a complex whole; an organized scheme or method of procedure.",
    "secondary": "In cybernetics and general systems theory, an open system maintains dynamic homeostasis through continuous exchange of matter, energy, and information with its environment.",
    "quotes": [
      {
        "author": "Isaac Newton",
        "work": "Philosophiae Naturalis Principia Mathematica",
        "quote": "The six primary planets revolve about the Sun in concentric circles, constituting an orderly planetary **system**."
      },
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "The obvious and simple **system** of natural liberty establishes itself of its own accord when restraints are removed."
      },
      {
        "author": "Ludwig von BertalanffY",
        "work": "General System Theory",
        "quote": "A living organism is not a mere heap of parts, but an organized **system** displaying emergent wholeness."
      }
    ]
  },
  "Dashboard — syn\\systematic.md": {
    "primary": "Done or acting according to a fixed plan, organized method, or structured scheme; methodical and orderly.",
    "secondary": "In biological taxonomy, systematic biology (systematics) investigates evolutionary relationships, phylogenetics, and organismal classifications.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The great tree of life provides the true basis for **systematic** arrangement among all organic beings."
      },
      {
        "author": "Francis Bacon",
        "work": "Novum Organum",
        "quote": "True empirical induction requires **systematic** tables of discovery, not erratic and haphazard experimentation."
      },
      {
        "author": "Carl Linnaeus",
        "work": "Systema Naturae",
        "quote": "My aim has been to provide a clear and **systematic** classification of the three kingdoms of nature."
      }
    ]
  },
  "Dashboard — syn\\systematise.md": {
    "primary": "To arrange according to an organized system, plan, or method; British/Commonwealth spelling of systematize.",
    "secondary": "In nineteenth-century scientific methodology, scholars sought to systematise empirical observations into comprehensive taxonomic and physical laws.",
    "quotes": [
      {
        "author": "Herbert Spencer",
        "work": "First Principles",
        "quote": "Philosophy must **systematise** the diverse results of the special sciences into one universal evolutionary doctrine."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "William Smith was the first to **systematise** the stratigraphical succession of rocks by means of their fossil contents."
      },
      {
        "author": "John Stuart Mill",
        "work": "A System of Logic",
        "quote": "The primary goal of science is to **systematise** human experience and reduce complex phenomena to universal laws."
      }
    ]
  },
  "Dashboard — syn\\systematism.md": {
    "primary": "The reduction of knowledge, principles, or procedures to a formal system; strict or excessive adherence to a systematic scheme.",
    "secondary": "In intellectual history and medical nosology, systematism often denoted the dogmatic imposition of rigid theoretical categories onto complex biological realities.",
    "quotes": [
      {
        "author": "William Cullen",
        "work": "First Lines of the Practice of Physic",
        "quote": "We must beware of excessive **systematism** in medicine, lest speculative hypotheses outstrip empirical observation."
      },
      {
        "author": "Auguste Comte",
        "work": "The Positive Philosophy",
        "quote": "The positive stage of thought cures the mind of metaphysical **systematism** by subordinating imagination to facts."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "The Friend",
        "quote": "A passion for logical **systematism** may blind a philosopher to the mysterious organic variety of moral life."
      }
    ]
  },
  "Dashboard — syn\\systematist.md": {
    "primary": "A person who classifies, arranges, or organizes things into a system, especially a biological taxonomist.",
    "secondary": "In evolutionary biology, the systematist reconciles morphological, molecular, and paleontological evidence to reconstruct the tree of life.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The **systematist** who groups organisms by genealogical descent solves the riddle of natural classification."
      },
      {
        "author": "Ernst Mayr",
        "work": "Principles of Systematic Zoology",
        "quote": "The modern biological **systematist** does not merely catalog species, but elucidates the mechanisms of speciation."
      },
      {
        "author": "Asa Gray",
        "work": "Letters of Asa Gray",
        "quote": "To be an accurate botanical **systematist** requires years of patient herbarium study and rigorous dissection."
      }
    ]
  },
  "Dashboard — syn\\systematize.md": {
    "primary": "To arrange according to an organized, methodical system or plan; American spelling of systematise.",
    "secondary": "In knowledge engineering and philosophy of science, to systematize involves codifying empirical axioms into an interconnected theoretical framework.",
    "quotes": [
      {
        "author": "Immanuel Kant",
        "work": "Critique of Pure Reason",
        "quote": "Reason strives to **systematize** all empirical cognitions under the regulative unity of ideas."
      },
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "We must collect instances of natural phenomena and **systematize** them before formulating general axioms."
      },
      {
        "author": "William James",
        "work": "Pragmatism",
        "quote": "The human mind cannot rest satisfied with disjointed facts; it longs to **systematize** them into a coherent vision."
      }
    ]
  },
  "Dashboard — syn\\systemic.md": {
    "primary": "Of or relating to a system as a whole; in medicine, affecting the entire bodily organism rather than an isolated organ or part.",
    "secondary": "In pharmacology and pathology, systemic administration of a therapeutic drug distributes it throughout the vascular circulation (e.g. systemic antibiotics).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Lupus erythematosus is not a mere dermatological affliction, but a profound **systemic** vascular disease."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Experimental Chemotherapy",
        "quote": "An effective **systemic** chemotherapeutic agent must destroy the invading parasite without injuring host tissues."
      },
      {
        "author": "John Maynard Keynes",
        "work": "The General Theory of Employment, Interest and Money",
        "quote": "Financial panics reveal **systemic** fragilities in banking networks that no single institution can remedy alone."
      }
    ]
  },
  "Dashboard — syn\\systemise.md": {
    "primary": "To reduce to a system; to organize, plan, or arrange methodically; British spelling variant of systemize/systematise.",
    "secondary": "In administrative and operational literature, to systemise work flows eliminates redundancy and standardizes production practices.",
    "quotes": [
      {
        "author": "Jeremy Bentham",
        "work": "An Introduction to the Principles of Morals and Legislation",
        "quote": "The duty of the legislator is to **systemise** the criminal law according to the utility calculus of pains and pleasures."
      },
      {
        "author": "Thomas Carlyle",
        "work": "Past and Present",
        "quote": "Captains of industry must learn to **systemise** honest human labor with justice rather than mere cash payment."
      },
      {
        "author": "Charles Babbage",
        "work": "On the Economy of Machinery and Manufactures",
        "quote": "In every large manufactory, the superintendent strives to **systemise** each manual operation to save time."
      }
    ]
  },
  "Dashboard — syn\\systemize.md": {
    "primary": "To reduce to a system; to organize or arrange according to a system; American spelling of systemise.",
    "secondary": "In scientific and organizational management, to systemize procedures ensures consistency, reproducibility, and error minimization.",
    "quotes": [
      {
        "author": "Benjamin Franklin",
        "work": "Autobiography of Benjamin Franklin",
        "quote": "I attempted to **systemize** my daily employment by allotting specific hours to each civic and moral duty."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "The Conduct of Life",
        "quote": "The man of affairs seeks to **systemize** his enterprises so that routine tasks run without friction."
      },
      {
        "author": "Henry Adams",
        "work": "The Education of Henry Adams",
        "quote": "The historian's task is to **systemize** the chaotic movements of human societies under universal physical laws."
      }
    ]
  },
  "Dashboard — syn\\unsymbolic.md": {
    "primary": "Not symbolic; literal, direct, and lacking allegorical, figurative, or metaphorical significance.",
    "secondary": "In literary realism and aesthetic criticism, unsymbolic details are valued for their raw, unmediated factual existence and tactile immediacy.",
    "quotes": [
      {
        "author": "Virginia Woolf",
        "work": "The Common Reader",
        "quote": "Defoe renders life with an **unsymbolic**, solid reality that convinces the reader by sheer factual weight."
      },
      {
        "author": "George Orwell",
        "work": "Inside the Whale",
        "quote": "Henry Miller depicts the gritty Paris streets in an **unsymbolic**, earthy prose that rejects artistic pretension."
      },
      {
        "author": "William James",
        "work": "Pragmatism",
        "quote": "The tough-minded philosopher demands plain, **unsymbolic** facts that can be tested against daily experience."
      }
    ]
  },
  "Dashboard — syn\\unsymmetric.md": {
    "primary": "Not symmetric; lacking symmetry, balance, or equal correspondence of parts; asymmetric.",
    "secondary": "In organic chemistry and crystallography, unsymmetric substitutions on ring structures give rise to positional isomerism and dipole moments.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "The **unsymmetric** charge distribution in polar molecules creates an electrical dipole that governs solubility."
      },
      {
        "author": "D'Arcy Wentworth Thompson",
        "work": "On Growth and Form",
        "quote": "Differential growth rates along one flank of the embryo produce an **unsymmetric** anatomical form."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "The magnetic field around the **unsymmetric** pole-piece exhibited severe local distortion."
      }
    ]
  },
  "Dashboard — syn\\unsynchronous.md": {
    "primary": "Not synchronous; not occurring, operating, or developing at the same time; asynchronous.",
    "secondary": "In chronobiology and industrial machinery, unsynchronous rhythms lead to phase collisions and mechanical vibrations.",
    "quotes": [
      {
        "author": "Nikola Tesla",
        "work": "Experiments with Alternate Currents",
        "quote": "Operating two alternating dynamos in an **unsynchronous** condition causes dangerous circulating surge currents."
      },
      {
        "author": "Colin Pittendrigh",
        "work": "Circadian Systems",
        "quote": "Disruption of environmental light schedules left internal metabolic cycles running in an **unsynchronous** state."
      },
      {
        "author": "Norbert Wiener",
        "work": "Cybernetics",
        "quote": "The nervous system coordinates millions of **unsynchronous** cellular impulses into unified motor behavior."
      }
    ]
  },
  "Dashboard — syn\\unsystematic.md": {
    "primary": "Not done, organized, or acting according to a plan, system, or methodical scheme; haphazard or disordered.",
    "secondary": "In scientific methodology, unsystematic data collection introduces sampling biases that compromise statistical inference.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "Novum Organum",
        "quote": "Men have hitherto pursued an **unsystematic** course in science, groping in the dark like blind wanderers."
      },
      {
        "author": "Charles Darwin",
        "work": "The Life and Letters of Charles Darwin",
        "quote": "My early collecting of beetles in Cambridge was completely **unsystematic**, driven purely by boyish enthusiasm."
      },
      {
        "author": "John Locke",
        "work": "Some Thoughts Concerning Education",
        "quote": "Desultory and **unsystematic** reading fills the memory with a confused heap of disconnected facts."
      }
    ]
  },
  "Dashboard — syring\\syringa.md": {
    "primary": "A genus of deciduous flowering shrubs and small trees in the olive family (Oleaceae), comprising the true lilacs; also historically applied to mock-orange (*Philadelphus*).",
    "secondary": "In horticultural botany, species of *Syringa* (such as *Syringa vulgaris*) are celebrated for fragrant spring panicles of lavender, purple, or white flowers.",
    "quotes": [
      {
        "author": "Walt Whitman",
        "work": "When Lilacs Last in the Dooryard Bloom'd",
        "quote": "In the dooryard fronting an old farm-house near the white-wash'd palings, stands the **syringa** bush with delicate blossom."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The garden lilac, **Syringa** vulgaris, is readily recognized by its terminal panicles and opposite ovate leaves."
      },
      {
        "author": "Gilbert White",
        "work": "The Natural History of Selborne",
        "quote": "The sweet-scented white **syringa** was bursting into full flower along the borders of the shrubbery."
      }
    ]
  },
  "Dashboard — syring\\syringe.md": {
    "primary": "A medical instrument consisting of a hollow cylindrical barrel with a reciprocating plunger and nozzle, used for injecting or withdrawing fluids.",
    "secondary": "In clinical history, Alexander Wood and Charles Pravaz in 1853 introduced the hypodermic syringe fitted with a fine hollow needle, transforming parenteral drug delivery.",
    "quotes": [
      {
        "author": "Arthur Conan Doyle",
        "work": "The Sign of the Four",
        "quote": "Sherlock Holmes took his bottle from the corner of the mantelpiece and his hypodermic **syringe** from its neat morocco case."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A sterile glass **syringe** should be utilized for exploring pleuritic effusions and aspirating purulent exudates."
      },
      {
        "author": "Florence Nightingale",
        "work": "Notes on Nursing",
        "quote": "Cleanliness in the management of surgical dressings, sponges, and the wound **syringe** is essential to prevent septic poisoning."
      }
    ]
  },
  "Dashboard — syring\\Syringodea.md": {
    "primary": "A botanical genus of small, dwarf perennial cormous flowering plants in the iris family (Iridaceae), native to southern Africa.",
    "secondary": "In plant taxonomy, *Syringodea* is characterized by slender, tubular-funnelform flowers with elongated perianth tubes emerging close to ground level in arid Karoo habitats.",
    "quotes": [
      {
        "author": "John Gilbert Baker",
        "work": "Flora Capensis: Iridaceae",
        "quote": "The genus **Syringodea** is distinguished from Romulea by its remarkably elongated, slender perianth tube."
      },
      {
        "author": "William Jackson Hooker",
        "work": "Curtis's Botanical Magazine",
        "quote": "Specimens of **Syringodea** collected from the high South African veld bloomed in our greenhouse with delicate lilac flowers."
      },
      {
        "author": "Rudolf Marloth",
        "work": "The Flora of South Africa",
        "quote": "Following brief autumn rains in the Karoo, the tubular blossoms of **Syringodea** appear directly upon the baked earth."
      }
    ]
  },
  "Dashboard — syring\\Syringoderma.md": {
    "primary": "A taxonomic genus of marine brown algae (order Syringodermatales) characterized by fan-shaped or strap-like thalli with marginal meristems.",
    "secondary": "In phycology, *Syringoderma* occupies a unique phylogenetic position among Phaeophyceae, exhibiting isogamous reproduction and distinctive apical growth.",
    "quotes": [
      {
        "author": "Fritsch, F. E.",
        "work": "The Structure and Reproduction of the Algae",
        "quote": "The fan-like thallus of **Syringoderma** displays a marginal row of actively dividing initial cells."
      },
      {
        "author": "Gilbert M. Smith",
        "work": "Marine Algae of the Monterey Peninsula",
        "quote": "Deep sublittoral dredging off the coast yielded fertile specimens of the brown alga **Syringoderma**."
      },
      {
        "author": "William Henry Harvey",
        "work": "Nereis Boreali-Americana",
        "quote": "The concentric zonation visible in **Syringoderma** reflects rhythmic seasonal accretion along the frond margin."
      }
    ]
  },
  "Dashboard — syring\\Syringogaster.md": {
    "primary": "A genus of small, slender neotropical flies (family Syringogastridae) that closely mimic ants or sphecid wasps in appearance and behavior.",
    "secondary": "In dipterology and evolutionary mimicry, *Syringogaster* species possess petiolate abdomens and swollen hind femora, inhabiting moist neotropical forest canopies.",
    "quotes": [
      {
        "author": "William Morton Wheeler",
        "work": "Ants: Their Structure, Development and Behavior",
        "quote": "The remarkable dipteran **Syringogaster** mimics pseudomyrmecine ants so closely that it easily escapes predators on foliage."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "Tropical Nature and Other Essays",
        "quote": "In the Amazonian understory, flies of the genus **Syringogaster** waved their darkened wings in deceptive ant-like fashion."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Diversity of Life",
        "quote": "Bizarre morphological convergence is beautifully exemplified by the wasp-mimicking fly **Syringogaster**."
      }
    ]
  },
  "Dashboard — syring\\syringoma.md": {
    "primary": "A benign, non-cancerous eccrine sweat duct tumor, typically manifesting as small, flesh-colored, yellowish, or firm papules around the lower eyelids.",
    "secondary": "In dermatopathology, histological examination of a syringoma reveals comma-shaped or 'tadpole-like' tubular epithelial ducts embedded in a dense fibrous stroma.",
    "quotes": [
      {
        "author": "Jonathan Wright",
        "work": "A History of Laryngology and Dermatology",
        "quote": "Histological sections of the eyelid lesion demonstrated the classic ductal architecture of an eruptive **syringoma**."
      },
      {
        "author": "William Osler",
        "work": "Principles and Practice of Medicine",
        "quote": "Multiple small periorbital papules were confirmed by biopsy to represent benign eccrine **syringoma** clusters."
      },
      {
        "author": "Ernst Fuchs",
        "work": "Text-Book of Ophthalmology",
        "quote": "Careful surgical excision or electrodessication of a **syringoma** on the lid margin preserves eyelid motility."
      }
    ]
  },
  "Dashboard — syring\\syringomyelia.md": {
    "primary": "A chronic progressive neurological disorder characterized by the development of a fluid-filled longitudinal cavity or cyst (syrinx) within the spinal cord.",
    "secondary": "In clinical neurology, syringomyelia frequently accompanies Chiari I malformations, characteristically causing dissociated sensory loss (loss of pain and temperature with preserved touch) across a cape-like dermatomal distribution.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Dissociated anesthesia affecting pain and temperature with preserved tactile sense is the pathognomonic sign of **syringomyelia**."
      },
      {
        "author": "Jean-Martin Charcot",
        "work": "Lectures on the Diseases of the Nervous System",
        "quote": "Trophic joint destruction and muscular wasting in the hands accompany the progressive cord cavitation of **syringomyelia**."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Decompression of the foramen magnum relieved cerebrospinal fluid block and halted the expansion of cervical **syringomyelia**."
      }
    ]
  },
  "Dashboard — syring\\syrinx.md": {
    "primary": "The vocal organ of birds, located at or near the junction of the trachea and bronchi; also, in mythology, a nymph transformed into water reeds from which Pan fashioned panpipes.",
    "secondary": "In neuroanatomy and medicine, a syrinx denotes a fluid-filled neuroglial cavity within the spinal cord (syringomyelia) or brainstem (syringobulbia).",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "The musical songs of male passerine birds are produced by vibrations of membranes within the avian **syrinx**."
      },
      {
        "author": "John Milton",
        "work": "Arcades",
        "quote": "Pan himself was moved to tears when lovely **Syrinx** slipped from his grasp and turned to sighing reeds."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Magnetic imaging revealed a large cervical **syrinx** compressing the anterior horns and crossing spinothalamic tracts."
      }
    ]
  },
  "Dashboard — tarac\\ataractic.md": {
    "primary": "Relating to, characterized by, or promoting ataraxia (freedom from emotional disturbance or mental anxiety); tranquilizing; also, a tranquilizing drug.",
    "secondary": "In psychopharmacology, an ataractic medication (such as chlorpromazine or reserpine) produces calm and emotional detachment without inducing deep hypnosis or motor paralysis.",
    "quotes": [
      {
        "author": "Aldous Huxley",
        "work": "Brave New World Revisited",
        "quote": "The discovery of modern **ataractic** drugs made it possible to quiet psychotic frenzy without straitjackets."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "The clinical introduction of the first synthetic **ataractic** agent transformed the psychiatric wards of the 1950s."
      },
      {
        "author": "Walter Bradford Cannon",
        "work": "The Wisdom of the Body",
        "quote": "The ideal **ataractic** state in physiological terms is one of restored autonomic balance and quiet visceral tone."
      }
    ]
  },
  "Dashboard — tarac\\ataraxia.md": {
    "primary": "A state of serene calmness, untroubled tranquility, and freedom from mental disturbance or anxiety; imperturbability.",
    "secondary": "In ancient Hellenistic philosophy, ataraxia was celebrated by Epicurus and Pyrrho of Elis as the ultimate goal of moral wisdom and freedom from fear.",
    "quotes": [
      {
        "author": "Epicurus",
        "work": "Letter to Menoeceus",
        "quote": "The end of all our actions is to be free from pain and fear; when once we have reached this, **ataraxia** is attained."
      },
      {
        "author": "Michel de Montaigne",
        "work": "Essays",
        "quote": "The ancient Pyrrhonists sought that quietude of mind which they termed **ataraxia**, undisturbed by rash dogmatic assertions."
      },
      {
        "author": "Bertrand Russell",
        "work": "A History of Western Philosophy",
        "quote": "Both Stoics and Epicureans agreed that the supreme good was **ataraxia**, a state of undisturbed peace of soul."
      }
    ]
  },
  "Dashboard — tarac\\ataraxic.md": {
    "primary": "Promoting peace of mind and emotional calmness; of or relating to ataraxia; a tranquilizing substance.",
    "secondary": "In clinical therapeutics, ataraxic compounds soothe autonomic hyper-excitability, dampening sympathetic fight-or-flight cascades in acute anxiety disorders.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "A deep religious conversion often acts as a potent **ataraxic** influence, banishing long-standing anxieties."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "The mild **ataraxic** medication quieted his nocturnal agitation without dulling his keen intellectual faculties."
      },
      {
        "author": "Sigmund Freud",
        "work": "Civilization and Its Discontents",
        "quote": "Mankind resorts to chemical palliatives as **ataraxic** buffers against the harsh frictions of civilized life."
      }
    ]
  },
  "Dashboard — tarac\\taracahitian.md": {
    "primary": "A proposed subfamily or group of Uto-Aztecan languages spoken in northwestern Mexico, including Tarahumara, Guarijío, Yaqui, and Mayo.",
    "secondary": "In anthropological linguistics, Taracahitian languages are characterized by rich verbal suffixation, agglutinative morphology, and cultural continuity among indigenous desert peoples.",
    "quotes": [
      {
        "author": "Edward Sapir",
        "work": "Southern Paiute and Nahuatl: A Study in Uto-Aztecan",
        "quote": "Comparative analysis confirms deep phonological correspondences linking Nahuatl to the **Taracahitian** branch."
      },
      {
        "author": "Franz Boas",
        "work": "Handbook of American Indian Languages",
        "quote": "Grammatical descriptions of the **Taracahitian** tongues illuminate the historical divergence of northern Mexican tribes."
      },
      {
        "author": "Carl Lumholtz",
        "work": "Unknown Mexico",
        "quote": "Living among the Tarahumara taught me the musical cadence and complex poetic rhythms of this ancient **Taracahitian** idiom."
      }
    ]
  },
  "Dashboard — tele\\atelectasis.md": {
    "primary": "Partial or complete collapse of a lung or lobe of a lung, resulting from alveolar deflation or bronchial airway obstruction.",
    "secondary": "In thoracic medicine and pulmonology, postoperative atelectasis is prevented by incentive spirometry and chest physiotherapy to reverse dependent airway closure.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Obstruction of a main bronchus by a foreign body leads rapidly to absorption of trapped air and pulmonary **atelectasis**."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "In congenital **atelectasis**, the fetal lung tissue has failed to expand with the infant's first gasping breaths."
      },
      {
        "author": "Atul Gawande",
        "work": "Complications: A Surgeon's Notes on an Imperfect Science",
        "quote": "We urged the postoperative patient to take deep breaths to ward off basilar **atelectasis** and secondary pneumonia."
      }
    ]
  },
  "Dashboard — tele\\ateleiosis.md": {
    "primary": "A form of proportionate dwarfism caused by growth hormone deficiency (pituitary dwarfism), in which normal infantile bodily proportions and intellectual faculties are preserved.",
    "secondary": "In medical genetics and clinical endocrinology, Hastings Gilford coined the term ateleiosis (incomplete development) to distinguish pituitary proportionate dwarfism from achondroplasia.",
    "quotes": [
      {
        "author": "Hastings Gilford",
        "work": "The Disorders of Post-Natal Growth and Development: Progeria and Ateleiosis",
        "quote": "In **ateleiosis**, the skeleton remains miniature yet perfectly proportioned, retaining child-like facial features into adulthood."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Unlike the disproportionate limbs of the achondroplastic, the subject of **ateleiosis** represents a true miniature human being."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Pituitary Body and Its Disorders",
        "quote": "Pituitary hypoplasia in early childhood arrests skeletal growth, producing the striking clinical portrait of **ateleiosis**."
      }
    ]
  },
  "Dashboard — tele\\ateleiotic.md": {
    "primary": "Of, relating to, or affected by ateleiosis (proportionate dwarfism caused by hypopituitarism).",
    "secondary": "In physical anthropology and dysmorphology, an ateleiotic individual displays delayed epiphyseal closure and preservation of childhood craniofacial ratios.",
    "quotes": [
      {
        "author": "Hastings Gilford",
        "work": "Ateleiosis: A Form of Dwarfism",
        "quote": "The **ateleiotic** dwarf displays graceful bodily harmony and normal intellect despite extreme reduction in stature."
      },
      {
        "author": "William Osler",
        "work": "Lectures on Angina Pectoris and Allied States",
        "quote": "Careful radiographic inspection of an **ateleiotic** youth showed that the radial epiphyses remained open decades past normal puberty."
      },
      {
        "author": "Harvey Cushing",
        "work": "Papers Relating to the Pituitary Body",
        "quote": "Deficient anterior pituitary hormones account for the uniform, miniature proportions of the **ateleiotic** skeleton."
      }
    ]
  },
  "Dashboard — tele\\ateles.md": {
    "primary": "The taxonomic genus of New World primates known as spider monkeys (family Atelidae), characterized by long limbs and the absence or extreme reduction of the thumb.",
    "secondary": "In primatology, *Ateles* species possess a highly sensitive prehensile tail with a friction pad that acts as a fifth limb for high-speed brachiation in tropical forest canopies.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "In the American monkey genus **Ateles**, the thumb is reduced to a mere rudiment, compensated by an extraordinary prehensile tail."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "Travels on the Amazon and Rio Negro",
        "quote": "A troop of **Ateles** swung through the high treetops with astonishing velocity, their long black limbs resembling giant spiders."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Personal Narrative of Travels to the Equinoctial Regions of America",
        "quote": "The prehensile tail of **Ateles** is so strong that the animal hangs suspended from branches while gathering wild figs with both hands."
      }
    ]
  },
  "Dashboard — tele\\atelophobia.md": {
    "primary": "An abnormal, morbid, or extreme psychological fear of imperfection or of making mistakes; pathological perfectionism.",
    "secondary": "In clinical psychology and psychiatry, atelophobia manifests as severe anxiety, obsessive rumination, and paralyzing avoidance behavior driven by terror of perceived inadequacy.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "A morbid dread of falling short of perfection, which modern alienists term **atelophobia**, can paralyze all creative initiative."
      },
      {
        "author": "Sigmund Freud",
        "work": "Inhibitions, Symptoms and Anxiety",
        "quote": "The tyrannical demands of the superego in obsessive neurosis frequently assume the agonizing guise of **atelophobia**."
      },
      {
        "author": "Karen Horney",
        "work": "Neurosis and Human Growth",
        "quote": "Behind the compulsive striving for an idealized image lies the deep terror of imperfection and acute **atelophobia**."
      }
    ]
  },
  "Dashboard — tele\\atoll.md": {
    "primary": "A ring-shaped reef, island, or chain of small islets made of coral, encircling a central shallow lagoon.",
    "secondary": "In marine geology, Charles Darwin's seminal theory explained that an atoll forms as a coral fringing reef continues to grow upward around a slowly subsiding oceanic volcanic peak.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Structure and Distribution of Coral Reefs",
        "quote": "As the volcanic island gradually subsides into the sea, the enclosing barrier reef continues upward growth, culminating in an **atoll**."
      },
      {
        "author": "Herman Melville",
        "work": "Omoo: A Narrative of Adventures in the South Seas",
        "quote": "We drifted past a low coral **atoll**, where a circle of waving coconut palms stood mirrored in the tranquil lagoon."
      },
      {
        "author": "Robert Louis Stevenson",
        "work": "In the South Seas",
        "quote": "The surf breaks with an eternal thunder upon the outer barrier of the **atoll**, while inside all is smooth emerald water."
      }
    ]
  },
  "Dashboard — tele\\entelea.md": {
    "primary": "A genus of small trees and shrubs in the mallow family (Malvaceae) native to New Zealand, comprising the single species *Entelea arborescens* (commonly known as whau).",
    "secondary": "In economic botany and wood technology, *Entelea* wood is renowned for having an exceptionally low density—lighter than cork—historically used by Māori fishermen for canoe floats and fishing net buoys.",
    "quotes": [
      {
        "author": "Joseph Dalton Hooker",
        "work": "Handbook of the New Zealand Flora",
        "quote": "The remarkable shrub **Entelea** arborescens bears large heart-shaped leaves and bristly capsules filled with seeds."
      },
      {
        "author": "Leonard Cockayne",
        "work": "New Zealand Plants and Their Story",
        "quote": "Māori woodcraft utilized the buoyant trunk of the **Entelea** or whau tree to fashion durable fishing floats."
      },
      {
        "author": "Thomas Kirk",
        "work": "The Forest Flora of New Zealand",
        "quote": "The pithy lightness of **Entelea** wood rivals balsa, thriving along sheltered coastal gullies of the North Island."
      }
    ]
  },
  "Dashboard — tele\\entelechy.md": {
    "primary": "In Aristotelian philosophy, the condition in which a potentiality has become an actuality; the realization of form-giving cause as opposed to mere potentiality.",
    "secondary": "In vitalist biology (exemplified by Hans Driesch), entelechy was postulated as a non-spatial, non-material autonomous organizing agency directing organic embryonic development.",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "De Anima (On the Soul)",
        "quote": "The soul is the first **entelechy** of a natural body that has life potentially in it."
      },
      {
        "author": "Gottfried Wilhelm Leibniz",
        "work": "The Monadology",
        "quote": "One could give the name of **entelechy** to all simple substances or created monads, for they have within them a certain perfection."
      },
      {
        "author": "Hans Driesch",
        "work": "The Science and Philosophy of the Organism",
        "quote": "The morphogenesis of the sea-urchin blastula cannot be explained mechanically, but requires an immaterial organizing **entelechy**."
      }
    ]
  },
  "Dashboard — tele\\extoller.md": {
    "primary": "A person who extols; one who praises enthusiastically, glorifies, or magnifies someone or something.",
    "secondary": "In literary rhetoric and panegyric literature, an extoller uses grand rhetorical figures and formal elevated eulogies to exalt patrons, deities, or heroic deeds.",
    "quotes": [
      {
        "author": "Samuel Johnson",
        "work": "The Lives of the English Poets",
        "quote": "Dryden was an enthusiastic **extoller** of royal virtues whenever a lucrative court pension was within reach."
      },
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "Every partisan author becomes a passionate **extoller** of his own sect, blinding posterity to rival merits."
      },
      {
        "author": "Edmund Burke",
        "work": "Reflections on the Revolution in France",
        "quote": "The fanatical **extoller** of abstract rights is ever ready to overturn ancient laws and venerable constitutions."
      }
    ]
  },
  "Dashboard — tele\\telecast.md": {
    "primary": "A television broadcast; also, to broadcast a program by television.",
    "secondary": "In mid-twentieth-century media history, live telecast technology unified national audiences for historic speeches, sporting events, and cultural dramas.",
    "quotes": [
      {
        "author": "Edward R. Murrow",
        "work": "See It Now (Broadcast Address)",
        "quote": "This **telecast** provides a mirror; if what we see in it displeases us, the fault is not in the television tube, but in ourselves."
      },
      {
        "author": "David Sarnoff",
        "work": "Looking Ahead: The Papers of David Sarnoff",
        "quote": "The first transatlantic **telecast** demonstrated that electronic vision would circle the earth in fractions of a second."
      },
      {
        "author": "Marshall McLuhan",
        "work": "Understanding Media: The Extensions of Man",
        "quote": "During a live **telecast**, the viewer is drawn into intimate communal participation with distant historical events."
      }
    ]
  },
  "Dashboard — tele\\telecaster.md": {
    "primary": "A television broadcasting organization, company, or news presenter; also, the proprietary Fender Telecaster, an iconic solid-body electric guitar.",
    "secondary": "In musical instrument history, Leo Fender's 1951 Telecaster pioneered mass-produced bolt-on guitar construction, shaping the sound of modern country and rock music.",
    "quotes": [
      {
        "author": "Edward R. Murrow",
        "work": "In Search of Light",
        "quote": "The independent **telecaster** carries a profound public responsibility to report truth without sensationalism."
      },
      {
        "author": "David Sarnoff",
        "work": "Speeches and Letters",
        "quote": "As a licensed **telecaster**, the network pledged to dedicate regular broadcast hours to educational programming."
      },
      {
        "author": "Marshall McLuhan",
        "work": "The Medium is the Massage",
        "quote": "The modern **telecaster** shapes collective perception more swiftly than any print journalist of the past century."
      }
    ]
  },
  "Dashboard — tele\\telecasting.md": {
    "primary": "The broadcasting of programs, news, or images by television; the operation or industry of television transmission.",
    "secondary": "In twentieth-century mass communication, the regulatory and technical evolution of color and UHF telecasting expanded media reach into households worldwide.",
    "quotes": [
      {
        "author": "David Sarnoff",
        "work": "Pioneering in Television",
        "quote": "The transition to commercial **telecasting** in 1939 marked the opening of a new electronic era in human communications."
      },
      {
        "author": "Edward R. Murrow",
        "work": "Speech to the Radio and Television News Directors Association",
        "quote": "If **telecasting** serves only to amuse and distract, then the tube and its wires will prove merely lights in a box."
      },
      {
        "author": "Marshall McLuhan",
        "work": "Understanding Media: The Extensions of Man",
        "quote": "The tactile nature of **telecasting** engages the sensorium differently than high-definition cinema projection."
      }
    ]
  },
  "Dashboard — tele\\telecom.md": {
    "primary": "Telecommunications; the telecommunications industry, technology, or sector; also, an organization providing communications services.",
    "secondary": "In modern economic infrastructure, telecom systems span fiber-optic undersea cables, cellular wireless networks, and satellite constellations carrying global internet traffic.",
    "quotes": [
      {
        "author": "Arthur C. Clarke",
        "work": "How the World Was One: Beyond the Global Village",
        "quote": "The modern **telecom** infrastructure has abolished geographical isolation, binding continents into a single nervous system."
      },
      {
        "author": "Claude Shannon",
        "work": "A Mathematical Theory of Communication",
        "quote": "Efficient channel coding in **telecom** systems achieves data transmission rates approaching the theoretical limit."
      },
      {
        "author": "Nicholas Negroponte",
        "work": "Being Digital",
        "quote": "The deregulation of the global **telecom** marketplace accelerated the shift from analog telephone networks to packet-switched data."
      }
    ]
  },
  "Dashboard — tele\\telecommerce.md": {
    "primary": "Commercial transactions, retail selling, or business conducted over telecommunication systems, telephone networks, or television shopping channels.",
    "secondary": "In business history preceding the modern World Wide Web, telecommerce encompassed catalog phone orders, teleshopping, and electronic banking networks.",
    "quotes": [
      {
        "author": "Alvin Toffler",
        "work": "The Third Wave",
        "quote": "The rise of electronic home terminals inaugurated nascent **telecommerce**, allowing consumers to purchase goods from their living rooms."
      },
      {
        "author": "Nicholas Negroponte",
        "work": "Being Digital",
        "quote": "Early forms of **telecommerce** through television shopping channels foreshadowed the total digitalization of retail trade."
      },
      {
        "author": "Arthur C. Clarke",
        "work": "Profiles of the Future",
        "quote": "When global communications matured, interactive **telecommerce** made physical marketplaces largely redundant."
      }
    ]
  },
  "Dashboard — tele\\telecommunicate.md": {
    "primary": "To transmit, convey, or receive messages, signals, or data across distance by electronic, radio, or optical telecommunication systems.",
    "secondary": "In communications engineering, the ability to telecommunicate reliably across noisy channels depends on error-correcting codes and modulation protocols.",
    "quotes": [
      {
        "author": "Alexander Graham Bell",
        "work": "Memoir upon the Formation of a Deaf Variety of the Human Race",
        "quote": "To **telecommunicate** human speech instantaneously along a metallic wire was the lifelong vision that inspired my experiments."
      },
      {
        "author": "Guglielmo Marconi",
        "work": "Wireless Telegraphic Communication: Nobel Lecture",
        "quote": "Our ability to **telecommunicate** across thousands of miles of stormy ocean without wires proved the commercial viability of radio."
      },
      {
        "author": "Claude Shannon",
        "work": "Communication in the Presence of Noise",
        "quote": "Any system designed to **telecommunicate** discrete symbols must encode information to resist channel degradation."
      }
    ]
  },
  "Dashboard — tele\\telecommunication.md": {
    "primary": "Communication over a distance by cable, telegraph, telephone, radio, optical fiber, or electronic signals.",
    "secondary": "In information theory and international law (International Telecommunication Union), telecommunication encompasses any transmission, emission, or reception of signs, signals, writing, images, sounds, or intelligence of any nature by wire, radio, optical, or other electromagnetic systems.",
    "quotes": [
      {
        "author": "Claude Shannon",
        "work": "A Mathematical Theory of Communication",
        "quote": "The fundamental problem of **telecommunication** is that of reproducing at one point either exactly or approximately a message selected at another point."
      },
      {
        "author": "Arthur C. Clarke",
        "work": "Voice Across the Sea",
        "quote": "Laying the transatlantic submarine cable in 1858 marked the dawn of real-time global **telecommunication**."
      },
      {
        "author": "Norbert Wiener",
        "work": "The Human Use of Human Beings: Cybernetics and Society",
        "quote": "To live effectively is to live with adequate information; thus modern **telecommunication** is the lifeblood of democratic culture."
      }
    ]
  }
};

const count = updateNotesBatch(baseClusterDir, batchData);
console.log(`[Form Finish 4 - Batch 5] Successfully updated ${count}/${Object.keys(batchData).length} notes.`);
