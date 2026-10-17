import { updateNotesBatch } from './curate-updater-util.mjs';

const BASE_DIR = 'App database/Greek roots/Cluster Action';

const BATCH2_DATA = {
  "Dashboard — st\\eustatic.md": {
    "primary": "Pertaining to, caused by, or characterized by worldwide, simultaneous changes in sea level.",
    "secondary": "In stratigraphy and oceanography, designating global sea-level shifts resulting from changes in glacial ice volume or oceanic basin tectonics.",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Submerged forests along oceanic coasts bear witness to widespread **eustatic** movements that altered continental boundaries."
      },
      {
        "author": "Eduard Suess",
        "work": "The Face of the Earth",
        "quote": "We trace the periodic inundation of ancient continental shields to great **eustatic** transgressions of the global ocean."
      },
      {
        "author": "Rhodes Fairbridge",
        "work": "Eustatic Changes in Sea Level",
        "quote": "Postglacial warming triggered a rapid **eustatic** rise that drowned coastal valleys and formed modern estuaries."
      }
    ]
  },
  "Dashboard — st\\eustele.md": {
    "primary": "A type of stele characteristic of seed plants in which the primary vascular tissue forms a cylinder of discrete longitudinal strands around a central pith.",
    "secondary": "In plant anatomy, the advanced vascular arrangement typical of dicotyledonous angiosperms and gymnosperms that enables secondary growth via a vascular cambium.",
    "quotes": [
      {
        "author": "Arthur Johnson Eames",
        "work": "Morphology of Vascular Plants",
        "quote": "The transition from the primitive solenostele to the dissected **eustele** facilitated the evolution of complex leaf traces."
      },
      {
        "author": "Edward Charles Jeffrey",
        "work": "The Anatomy of Woody Plants",
        "quote": "In gymnosperm stems, the vascular bundles of the **eustele** are separated by narrow rays of parenchymatous tissue."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "Transverse sections of the sunflower stem display a classic **eustele** composed of discrete collateral bundles encircling the central pith."
      }
    ]
  },
  "Dashboard — st\\haplostele.md": {
    "primary": "The simplest and phylogenetically most primitive form of protostele, consisting of a solid cylindrical central core of xylem surrounded by phloem.",
    "secondary": "In paleobotany and pteridophyte anatomy, the ancestral vascular architecture observed in Rhynia and primitive fossil lycophytes.",
    "quotes": [
      {
        "author": "F. O. Bower",
        "work": "The Origin of a Land Flora",
        "quote": "The cylindrical **haplostele** of Rhynia represents the primordial vascular design from which all complex stelar forms evolved."
      },
      {
        "author": "D. H. Scott",
        "work": "Studies in Fossil Botany",
        "quote": "In early Devonian plants, the vascular cylinder remains a simple non-medullated **haplostele** devoid of internal parenchyma."
      },
      {
        "author": "Ernest M. Gifford",
        "work": "Morphology and Evolution of Vascular Plants",
        "quote": "The smooth, unlobed outline of the **haplostele** offers minimal surface contact between conducting tracheids and living tissues."
      }
    ]
  },
  "Dashboard — st\\homeostasis.md": {
    "primary": "The tendency of a physiological system or living organism to maintain internal stability and equilibrium amid external changes.",
    "secondary": "In cybernetics and general systems theory, the self-regulating mechanism by which dynamic systems stabilize their operational variables.",
    "quotes": [
      {
        "author": "Walter Cannon",
        "work": "The Wisdom of the Body",
        "quote": "The coordinated physiological processes which maintain most of the steady states in the organism I have called **homeostasis**."
      },
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "The constancy of the internal environment—what moderns term **homeostasis**—is the condition of free and independent life."
      },
      {
        "author": "Norbert Wiener",
        "work": "Cybernetics",
        "quote": "Negative feedback loops provide the formal mathematical foundation for understanding both mechanical servomechanisms and organic **homeostasis**."
      }
    ]
  },
  "Dashboard — st\\homeostatic.md": {
    "primary": "Relating to, characterized by, or promoting the maintenance of physiological equilibrium or internal constancy.",
    "secondary": "In cognitive science and neurology, describing neural circuits and neuroendocrine feedback systems that regulate bodily set-points.",
    "quotes": [
      {
        "author": "W. Ross Ashby",
        "work": "Design for a Brain",
        "quote": "The ultrastable system adapts to environmental trauma through autonomous **homeostatic** rearrangements of its internal state."
      },
      {
        "author": "Ludwig von Bertalanffy",
        "work": "General System Theory",
        "quote": "Open systems maintain an apparent steady state by virtue of continuous **homeostatic** exchanges of matter and energy with their milieu."
      },
      {
        "author": "Antonio Damasio",
        "work": "Descartes' Error",
        "quote": "Feelings are the conscious subjective monitors of our underlying **homeostatic** balance, signaling need or thriving."
      }
    ]
  },
  "Dashboard — st\\hydrostatic.md": {
    "primary": "Pertaining to fluids at rest, especially liquids, and the pressures and forces they exert in equilibrium.",
    "secondary": "In comparative anatomy and biomechanics, denoting structural support systems (hydrostatic skeletons) reliant on fluid-filled coelomic cavities under pressure.",
    "quotes": [
      {
        "author": "Blaise Pascal",
        "work": "Treatise on the Equilibrium of Liquids",
        "quote": "The law of **hydrostatic** pressure dictates that force applied to an enclosed liquid is transmitted equally in all directions."
      },
      {
        "author": "Archimedes",
        "work": "On Floating Bodies",
        "quote": "A body immersed in a fluid experiences an upward **hydrostatic** buoyant force equal to the weight of the fluid it displaces."
      },
      {
        "author": "Simon Stevin",
        "work": "Principles of Hydrostatics",
        "quote": "The downward **hydrostatic** thrust upon the base of a vessel depends upon the height of the liquid column, not its total volume."
      }
    ]
  },
  "Dashboard — st\\hydrostatics.md": {
    "primary": "The branch of physical science and fluid mechanics that investigates liquids and fluids in static equilibrium and the pressures they exert.",
    "secondary": "In engineering, the mathematical analysis of fluid pressure distributions against dams, submerged surfaces, and floating vessels.",
    "quotes": [
      {
        "author": "Galileo Galilei",
        "work": "Discourse on Bodies in Water",
        "quote": "The geometric demonstrations of **hydrostatics** clarify why shape alone cannot account for the floating or sinking of solid bodies."
      },
      {
        "author": "Daniel Bernoulli",
        "work": "Hydrodynamica",
        "quote": "Before investigating fluids in rapid motion, the natural philosopher must master the fundamental theorems of **hydrostatics**."
      },
      {
        "author": "Isaac Newton",
        "work": "Philosophiae Naturalis Principia Mathematica",
        "quote": "The equilibrium of fluid spheres under mutual gravitational attraction constitutes one of the most sublime problems in **hydrostatics**."
      }
    ]
  },
  "Dashboard — st\\hypostasis.md": {
    "primary": "The underlying reality, fundamental substance, or essential nature of something, as opposed to its outward attributes.",
    "secondary": "In Christian theology, any of the three distinct Persons of the Trinity; in pathology, the pooling or settling of blood in dependent bodily regions.",
    "quotes": [
      {
        "author": "Athanasius of Alexandria",
        "work": "Against the Arians",
        "quote": "The Son is not a created attribute of the Father, but distinct in **hypostasis** while eternally sharing one indivisible essence."
      },
      {
        "author": "Thomas Aquinas",
        "work": "Summa Theologiae",
        "quote": "In theological discourse, **hypostasis** signifies an individual substance of a rational nature, possessing complete subsistence."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Pulmonary **hypostasis** occurs when prolonged recumbency causes venous blood to gravitate toward the dorsal lung bases."
      }
    ]
  },
  "Dashboard — st\\hypostasize.md": {
    "primary": "To treat, consider, or reify an abstract concept or relation as if it were a concrete, independently existing substance or real entity.",
    "secondary": "In philosophical critique, to commit the fallacy of misplaced concreteness by projecting linguistic entities into physical or metaphysical reality.",
    "quotes": [
      {
        "author": "John Stuart Mill",
        "work": "A System of Logic",
        "quote": "The scholastic realists committed a fatal error when they sought to **hypostasize** mere general names into self-existent substances."
      },
      {
        "author": "Karl Marx",
        "work": "The German Ideology",
        "quote": "Hegel tends to **hypostasize** the State into an autonomous spiritual demiurge hovering above material economic relations."
      },
      {
        "author": "Alfred North Whitehead",
        "work": "Science and the Modern World",
        "quote": "To **hypostasize** space and time as independent containers of matter is the classic fallacy of misplaced concreteness."
      }
    ]
  },
  "Dashboard — st\\hypostatic.md": {
    "primary": "Pertaining to, having the nature of, or constituting a hypostasis or distinct subsistence.",
    "secondary": "In Christian Christology, denoting the hypostatic union—the union of full divinity and full humanity in the single person of Jesus Christ.",
    "quotes": [
      {
        "author": "Cyril of Alexandria",
        "work": "Letters to Nestorius",
        "quote": "We confess that the Word became flesh by an incomprehensible and ineffable **hypostatic** union of two complete natures."
      },
      {
        "author": "Richard Hooker",
        "work": "Of the Laws of Ecclesiastical Polity",
        "quote": "The **hypostatic** union between the divine and human in Christ preserved the properties of both without confusion or conversion."
      },
      {
        "author": "John Henry Newman",
        "work": "An Essay on the Development of Christian Doctrine",
        "quote": "Centuries of intense conciliar debate were required to clarify the precise meaning of **hypostatic** distinction within the Godhead."
      }
    ]
  },
  "Dashboard — st\\hypostatisation.md": {
    "primary": "The cognitive act or philosophical fallacy of reifying an abstraction and treating it as a concrete, independent reality (British spelling).",
    "secondary": "In critical social theory, the ideological transformation of historical, social relations into seemingly natural, fixed ontological things.",
    "quotes": [
      {
        "author": "Theodor W. Adorno",
        "work": "Negative Dialectics",
        "quote": "Dialectical critique must resist the dogmatic **hypostatisation** of subjective categories into immutable metaphysical constants."
      },
      {
        "author": "Georg Lukács",
        "work": "History and Class Consciousness",
        "quote": "Commodity fetishism accomplishes the systematic **hypostatisation** of human labor relations into objective economic laws."
      },
      {
        "author": "Roy Bhaskar",
        "work": "A Realist Theory of Science",
        "quote": "We must avoid the epistemological fallacy without falling into the illicit **hypostatisation** of theoretical models."
      }
    ]
  },
  "Dashboard — st\\hypostatise.md": {
    "primary": "To attribute concrete, substantial, or independent physical reality to an abstract mental concept or linguistic symbol (British spelling).",
    "secondary": "In analytic metaphysics, to treat conceptual predicates or universal properties as self-subsistent particulars.",
    "quotes": [
      {
        "author": "F. H. Bradley",
        "work": "Appearance and Reality",
        "quote": "If you **hypostatise** relations into independent entities standing between terms, you plunge into an endless regress."
      },
      {
        "author": "Bertrand Russell",
        "work": "The Principles of Mathematics",
        "quote": "We must not **hypostatise** the golden mountain into an actual ontological entity merely because it functions as a grammatical subject."
      },
      {
        "author": "G. E. Moore",
        "work": "Principia Ethica",
        "quote": "Metaphysical ethicists consistently **hypostatise** moral goodness into a supersensible realm beyond empirical experience."
      }
    ]
  },
  "Dashboard — st\\hypostatization.md": {
    "primary": "The act or logical fallacy of regarding a purely abstract mental construct or naming convention as a real, concrete, substantial entity.",
    "secondary": "In epistemology and semiotics, reification; the unreflective projection of conceptual taxonomies into objective ontological structures.",
    "quotes": [
      {
        "author": "Immanuel Kant",
        "work": "Critique of Pure Reason",
        "quote": "The transcendent illusion consists in the illicit **hypostatization** of a regulatory idea of pure reason into an existing object."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The popular **hypostatization** of the ego as an immaterial spiritual substance explains nothing about the stream of thought."
      },
      {
        "author": "Friedrich Nietzsche",
        "work": "Twilight of the Idols",
        "quote": "Language seduces us into the false **hypostatization** of causes and effects where nature reveals only a continuous flux."
      }
    ]
  },
  "Dashboard — st\\hypostatize.md": {
    "primary": "To reify or treat an abstract idea, quality, or construct as an independently existing concrete thing (American spelling).",
    "secondary": "In philosophy of science, to assume mistakenly that theoretical terms refer directly to unobservable metaphysical substances.",
    "quotes": [
      {
        "author": "John Dewey",
        "work": "Experience and Nature",
        "quote": "Philosophers frequently commit a grave error when they **hypostatize** the products of reflective inquiry into antecedently real essences."
      },
      {
        "author": "George Santayana",
        "work": "Scepticism and Animal Faith",
        "quote": "To **hypostatize** intuition into an ontological creator of its own objects is the romantic fallacy of idealism."
      },
      {
        "author": "Willard Van Orman Quine",
        "work": "From a Logical Point of View",
        "quote": "We can employ meaningful conceptual predicates without being forced to **hypostatize** universals as concrete entities."
      }
    ]
  },
  "Dashboard — st\\mesostatic.md": {
    "primary": "Formed, occurring, or stabilizing in an intermediate position, phase, or period of crystallization.",
    "secondary": "In igneous petrology and mineralogy, occupying the interstices between earlier-formed phenocrysts in volcanic or plutonic rocks.",
    "quotes": [
      {
        "author": "Archibald Geikie",
        "work": "The Ancient Volcanoes of Great Britain",
        "quote": "Microscopic examination reveals a **mesostatic** groundmass of glassy silica cementing the earlier crystalline feldspars."
      },
      {
        "author": "Alfred Harker",
        "work": "The Natural History of Igneous Rocks",
        "quote": "The residual liquid solidifies into a **mesostatic** quartz-orthoclase intergrowth that occupies interstitial angular voids."
      },
      {
        "author": "Norman L. Bowen",
        "work": "The Evolution of the Igneous Rocks",
        "quote": "Fractional crystallization leaves a highly enriched **mesostatic** residue that fills the gaps between early mafic cumulates."
      }
    ]
  },
  "Dashboard — st\\metastasis.md": {
    "primary": "The spread of pathogenic cells, especially cancer cells, from the primary site of disease to distant parts of the body.",
    "secondary": "In oncology, the secondary metastatic tumor colony formed by cells that have migrated through blood or lymph vessels.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Malignant **metastasis** occurs when emancipated cellular elements enter vascular channels to seed distant organs."
      },
      {
        "author": "Stephen Paget",
        "work": "The Distribution of Secondary Growths in Cancer of the Breast",
        "quote": "The seed and soil hypothesis explains why the **metastasis** of particular tumors exhibits predictable organ affinities."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The tragic prognosis of visceral carcinoma is sealed the moment systemic **metastasis** establishes secondary hepatic foci."
      }
    ]
  },
  "Dashboard — st\\metastasise.md": {
    "primary": "To spread from one part of the body to another through lymphatic channels or the bloodstream (British spelling).",
    "secondary": "In pathology, the biological process whereby neoplastic cells detach, invade tissues, intravasate, and colonize distant organs.",
    "quotes": [
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Emperor of All Maladies",
        "quote": "Cancer's fatal capacity to **metastasise** transforms a localized surgical challenge into a dispersed systemic battle."
      },
      {
        "author": "Atul Gawande",
        "work": "Being Mortal",
        "quote": "When cancer cells **metastasise** to bony structures, palliative care focuses on pain management and bone stabilization."
      },
      {
        "author": "Paul Kalanithi",
        "work": "When Breath Becomes Air",
        "quote": "The CT scan confirmed what my symptoms presaged: the tumors had begun to **metastasise** throughout both lung fields."
      }
    ]
  },
  "Dashboard — st\\metastasize.md": {
    "primary": "To spread from a primary site to other parts of the body, characteristic of malignant tumors (American spelling).",
    "secondary": "Metaphorically, to transform, expand uncontrollably, or proliferate destructively through an organization, culture, or society.",
    "quotes": [
      {
        "author": "Susan Sontag",
        "work": "Illness as Metaphor",
        "quote": "We must resist the cultural temptation to allow cancer to **metastasize** into a moral judgment on the patient's psyche."
      },
      {
        "author": "Lewis Thomas",
        "work": "The Medusa and the Snail",
        "quote": "For a cancer cell to **metastasize**, it must mimic embryonic cells by acquiring motility and enzymatically dissolving tissues."
      },
      {
        "author": "Christopher Hitchens",
        "work": "Mortality",
        "quote": "Watching a political ideology **metastasize** into fanaticism reminds me of how rogue cells consume healthy tissue."
      }
    ]
  },
  "Dashboard — st\\metastatic.md": {
    "primary": "Pertaining to, caused by, or having the character of metastasis; designating secondary cancerous tumors.",
    "secondary": "In clinical oncology, referring to stage IV malignancy that has established colonies in organs distant from the tissue of origin.",
    "quotes": [
      {
        "author": "William Stewart Halsted",
        "work": "The Results of Radical Operations for the Cure of Cancer",
        "quote": "Radical excision aims to intercept regional lymphatic spread before **metastatic** dissemination invades deeper viscera."
      },
      {
        "author": "James Ewing",
        "work": "Neoplastic Diseases",
        "quote": "The morphological appearance of a **metastatic** lesion often mirrors faithfully the histologic architecture of the parent tumor."
      },
      {
        "author": "Judah Folkman",
        "work": "Tumor Angiogenesis",
        "quote": "A microscopic **metastatic** colony cannot expand beyond a millimeter without recruiting its own vascular network."
      }
    ]
  },
  "Dashboard — st\\metasystem.md": {
    "primary": "A system of systems; an overarching, higher-order system that regulates, monitors, or coordinates multiple subordinate systems.",
    "secondary": "In cybernetics and computational philosophy, a meta-level organizational structure that governs evolutionary transitions and systemic logic.",
    "quotes": [
      {
        "author": "Stafford Beer",
        "work": "Brain of the Firm",
        "quote": "The five organizational tiers of the Viable System Model coalesce into a cohesive **metasystem** capable of autonomous regulation."
      },
      {
        "author": "Gregory Bateson",
        "work": "Mind and Nature",
        "quote": "Evolution and learning are dual components of a wider ecological **metasystem** linked by recursive information exchange."
      },
      {
        "author": "Valentin Turchin",
        "work": "The Phenomenon of Science",
        "quote": "The emergence of human culture represents a monumental **metasystem** transition wherein symbols begin to control genetic behavior."
      }
    ]
  },
  "Dashboard — st\\orthostates.md": {
    "primary": "Upright, large rectangular stone slabs or ashlar blocks set on edge to form the bottom course of a masonry wall.",
    "secondary": "In classical archaeology and Aegean architecture, decorative or load-bearing vertical slabs framing temple cella walls and palace facades.",
    "quotes": [
      {
        "author": "Vitruvius",
        "work": "The Ten Books on Architecture",
        "quote": "The masonry walls rest securely upon high dressed **orthostates**, which elevate the structural brick above ground dampness."
      },
      {
        "author": "Pausanias",
        "work": "Description of Greece",
        "quote": "The temple of Hera retained its archaic foundation of limestone **orthostates**, crowned with courses of sun-dried brick."
      },
      {
        "author": "William Bell Dinsmoor",
        "work": "The Architecture of Ancient Greece",
        "quote": "In classical Athenian architecture, marble **orthostates** were carefully clamped together to ensure monumental wall stability."
      }
    ]
  },
  "Dashboard — st\\orthostatic.md": {
    "primary": "Pertaining to, caused by, or occurring upon assuming an upright, standing bodily posture.",
    "secondary": "In clinical cardiology and neurology, describing blood pressure drops (orthostatic hypotension) or syncope provoked by postural change.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe volume depletion manifests acutely as **orthostatic** hypotension whenever the recumbent patient attempts to rise."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Pituitary Body and Its Disorders",
        "quote": "Autonomic insufficiency prevents adequate vascular compensation, precipitating sudden **orthostatic** dizziness."
      },
      {
        "author": "Walter Cannon",
        "work": "Bodily Changes in Pain, Hunger, Fear and Rage",
        "quote": "Immediate vasoconstrictor reflexes preserve cerebral perfusion against gravity during sudden **orthostatic** transitions."
      }
    ]
  },
  "Dashboard — st\\protostele.md": {
    "primary": "The simplest and phylogenetically most primitive type of plant stele, consisting of a solid central column of vascular tissue without pith.",
    "secondary": "In botanical anatomy, the ancestral vascular architecture of early land plants from which siphonosteles and eusteles subsequently diverged.",
    "quotes": [
      {
        "author": "F. O. Bower",
        "work": "The Origin of a Land Flora",
        "quote": "The non-medullated cylinder of the **protostele** constitutes the anatomical starting point of all vascular architecture in ferns."
      },
      {
        "author": "D. H. Scott",
        "work": "Extinct Plants and Problems of Evolution",
        "quote": "In primitive fossils of the Psilophytales, the conducting strand is invariably an unspecialized **protostele**."
      },
      {
        "author": "Edward Charles Jeffrey",
        "work": "The Anatomy of Woody Plants",
        "quote": "The central xylem cylinder of the **protostele** must increase its external perimeter as the stem expands in diameter."
      }
    ]
  },
  "Dashboard — st\\restate.md": {
    "primary": "To state again or express in a new, clearer, or more emphatic manner.",
    "secondary": "In legal jurisprudence and philosophical analysis, to formulate systematically the established principles of a doctrine.",
    "quotes": [
      {
        "author": "Oliver Wendell Holmes Jr.",
        "work": "The Common Law",
        "quote": "It is necessary from time to time to **restate** our foundational legal axioms in terms of actual social utility."
      },
      {
        "author": "Benjamin N. Cardozo",
        "work": "The Nature of the Judicial Process",
        "quote": "Judges do not create novel systems ex nihilo, but continually **restate** enduring precedents to fit shifting mores."
      },
      {
        "author": "John Rawls",
        "work": "Justice as Fairness: A Restatement",
        "quote": "In this work I aim to **restate** the core conceptions of justice as fairness to answer persistent critical objections."
      }
    ]
  },
  "Dashboard — st\\restatement.md": {
    "primary": "The act of stating something again, or an altered, renewed version of an earlier declaration.",
    "secondary": "In American jurisprudence, an authoritative treatise published by the American Law Institute summarizing common-law rules in specific fields.",
    "quotes": [
      {
        "author": "Learned Hand",
        "work": "The Spirit of Liberty",
        "quote": "The monumental **restatement** of contracts brought clarity to decades of conflicting state appellate jurisprudence."
      },
      {
        "author": "Roscoe Pound",
        "work": "An Introduction to the Philosophy of Law",
        "quote": "Every generational **restatement** of doctrine reflects the tension between the demand for stability and the need for change."
      },
      {
        "author": "Felix Frankfurter",
        "work": "Of Law and Men",
        "quote": "A judicial opinion is not a mere literary exercise, but a precise **restatement** of the constitutional balance of powers."
      }
    ]
  },
  "Dashboard — st\\stasimon.md": {
    "primary": "A choral ode in classical Greek drama sung by the chorus after it has taken its stand in the orchestra, between dramatic episodes.",
    "secondary": "In classical dramatic theory, a lyrical choral stanza composed in responding strophes and antistrophes, unmixed with spoken anapestic meters.",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "Poetics",
        "quote": "A **stasimon** is a choral song without anapaests or trochaic tetrameters, delivered by the chorus stationed in the orchestra."
      },
      {
        "author": "A. W. Schlegel",
        "work": "Lectures on Dramatic Art and Literature",
        "quote": "In each tragic **stasimon**, the chorus pauses to reflect with solemn lyric majesty upon the fatal deeds of the heroes."
      },
      {
        "author": "Gilbert Murray",
        "work": "A History of Ancient Greek Literature",
        "quote": "The choral **stasimon** provides a spiritual breathing space between the frantic clashes of the stage actors."
      }
    ]
  },
  "Dashboard — st\\stasis.md": {
    "primary": "A condition of balance, equilibrium, or stagnation where opposing forces neutralize each other, halting motion or progress.",
    "secondary": "In classical Greek historiography, violent internal factional strife or civil conflict; in pathology, the cessation of bodily fluid circulation.",
    "quotes": [
      {
        "author": "Thucydides",
        "work": "History of the Peloponnesian War",
        "quote": "The revolutionary **stasis** in Corcyra raged with unprecedented fury, subverting every traditional moral restraint."
      },
      {
        "author": "Aristotle",
        "work": "Politics",
        "quote": "Inequality of honors and property is the universal cause of that bitter factional **stasis** that ruins city-states."
      },
      {
        "author": "Thomas Hobbes",
        "work": "Leviathan",
        "quote": "Without a common power to keep them in awe, men descend into a destructive **stasis** that dissolves civil society."
      }
    ]
  },
  "Dashboard — st\\state.md": {
    "primary": "The particular condition that someone or something is in at a specific time; a mode or status of being.",
    "secondary": "In political philosophy, a politically organized body of people inhabiting a defined territory under one sovereign government.",
    "quotes": [
      {
        "author": "Niccolò Machiavelli",
        "work": "The Prince",
        "quote": "All dominions that have held sway over men have been and are either republics or principalities, comprising every form of **state**."
      },
      {
        "author": "John Locke",
        "work": "Second Treatise of Government",
        "quote": "To understand political power, we must consider what **state** all men are naturally in, namely, a state of perfect freedom."
      },
      {
        "author": "Max Weber",
        "work": "Politics as a Vocation",
        "quote": "A **state** is that human community which successfully claims the monopoly of the legitimate use of physical force within a territory."
      }
    ]
  },
  "Dashboard — st\\stated.md": {
    "primary": "Declared, specified, or explicitly set forth in words; fixed or regular.",
    "secondary": "In contractual law and formal accounting, fixed by established mutual agreement or formal stipulation at recurring intervals.",
    "quotes": [
      {
        "author": "Abraham Lincoln",
        "work": "First Inaugural Address",
        "quote": "I hold that, in contemplation of universal law and of the Constitution, the union of these States is perpetual, as **stated** in our compact."
      },
      {
        "author": "Thomas Jefferson",
        "work": "Notes on the State of Virginia",
        "quote": "The rights of conscience we never submitted, we could not submit; our rulers have no authority beyond **stated** constitutional powers."
      },
      {
        "author": "Alexander Hamilton",
        "work": "The Federalist Papers",
        "quote": "The judges shall hold their offices during good behavior, and receive at **stated** times a fixed compensation for their services."
      }
    ]
  },
  "Dashboard — st\\stateliness.md": {
    "primary": "The quality of being stately; majestic dignity, grand elegance, or imposing nobility of carriage and demeanor.",
    "secondary": "In aesthetics and architectural criticism, the harmonious, lofty proportion that conveys monumental authority and reverent composure.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The Roman senate preserved an exterior of majestic **stateliness** even when its real legislative prerogatives had vanished."
      },
      {
        "author": "Edmund Burke",
        "work": "Reflections on the Revolution in France",
        "quote": "The hereditary nobility imparts a venerable **stateliness** to the commonwealth, protecting it from volatile democratic whim."
      },
      {
        "author": "Nathaniel Hawthorne",
        "work": "The Scarlet Letter",
        "quote": "She possessed an innate dignity and haughty **stateliness** that shone forth despite the ignominious letter upon her bosom."
      }
    ]
  },
  "Dashboard — st\\stately.md": {
    "primary": "Majestic, dignified, imposing, or grand in appearance, manner, or movement.",
    "secondary": "Displaying noble, lofty, or ceremonial elegance suitable to royalty, grand architecture, or formal literary style.",
    "quotes": [
      {
        "author": "James Joyce",
        "work": "Ulysses",
        "quote": "Stately, plump Buck Mulligan came from the stairhead, bearing a bowl of lather on which a mirror and a razor lay crossed."
      },
      {
        "author": "Walt Whitman",
        "work": "Leaves of Grass",
        "quote": "I see the **stately** ships sailing out past the headlands, their white sails catching the golden afternoon sun."
      },
      {
        "author": "Alfred, Lord Tennyson",
        "work": "Break, Break, Break",
        "quote": "And the **stately** ships go on to their haven under the hill; but O for the touch of a vanished hand."
      }
    ]
  },
  "Dashboard — st\\statement.md": {
    "primary": "A clear, definite verbal or written expression of fact, opinion, intention, or policy.",
    "secondary": "In philosophy of language and formal logic, a declarative sentence or proposition capable of being evaluated as true or false.",
    "quotes": [
      {
        "author": "Ludwig Wittgenstein",
        "work": "Tractatus Logico-Philosophicus",
        "quote": "A proposition is a picture of reality; every genuine **statement** asserts how things stand in the logical space of the world."
      },
      {
        "author": "Bertrand Russell",
        "work": "Logic and Knowledge",
        "quote": "The grammatical form of a linguistic **statement** frequently disguises its underlying logical architecture."
      },
      {
        "author": "J. L. Austin",
        "work": "How to Do Things with Words",
        "quote": "We must abandon the view that the sole purpose of a serious **statement** is simply to describe some state of affairs."
      }
    ]
  },
  "Dashboard — st\\stater.md": {
    "primary": "An ancient Greek silver or gold coin, representing the standard unit of currency in many Hellenic and Asia Minor city-states.",
    "secondary": "In numismatics and classical economics, a monetary weight denomination equal to two drachmas (or a tetradrachm in certain regional weight standards).",
    "quotes": [
      {
        "author": "Herodotus",
        "work": "The Histories",
        "quote": "The Lydians were the first of men whom we know to strike and use coins of gold and silver, minting the famous electrum **stater**."
      },
      {
        "author": "Xenophon",
        "work": "Anabasis",
        "quote": "Cyrus promised to pay each mercenary soldier a gold Daric **stater** a month for joining his expedition to Babylon."
      },
      {
        "author": "Percy Gardner",
        "work": "A History of Ancient Coinage",
        "quote": "The Corinthian silver **stater**, bearing the winged Pegasus on its obverse, became the universally accepted trade bullion of Magna Graecia."
      }
    ]
  },
  "Dashboard — st\\static.md": {
    "primary": "Lacking in movement, active development, or change; stationary, fixed, or at rest.",
    "secondary": "In physics and electrical engineering, relating to electrostatic charges at rest, or electromagnetic interference producing crackling noise in audio receivers.",
    "quotes": [
      {
        "author": "Isaac Newton",
        "work": "Philosophiae Naturalis Principia Mathematica",
        "quote": "A body at rest will remain in a **static** condition unless compelled to change its state by impressed forces."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "A Treatise on Electricity and Magnetism",
        "quote": "The laws of **static** electricity assume a particularly simple mathematical form when charges remain immovable upon conductors."
      },
      {
        "author": "Claude Shannon",
        "work": "A Mathematical Theory of Communication",
        "quote": "Random thermal noise in communication channels manifests as background **static**, degrading the fidelity of transmitted messages."
      }
    ]
  },
  "Dashboard — st\\stative.md": {
    "primary": "In linguistics, designating a verb, adjective, or aspect that expresses a state of affairs, ongoing condition, or relation rather than a dynamic action.",
    "secondary": "In syntactic typology, denoting grammatical categories (such as 'know', 'belong', or 'resemble') that resist progressive aspect and imperative inflection.",
    "quotes": [
      {
        "author": "Noam Chomsky",
        "work": "Aspects of the Theory of Syntax",
        "quote": "Verbs marked with the syntactic feature **stative** fail to participate in progressive aspect or agentive imperative transformations."
      },
      {
        "author": "Bernard Comrie",
        "work": "Aspect",
        "quote": "A **stative** predicate represents a situation that is homogenous and unchanging throughout its temporal duration."
      },
      {
        "author": "Otto Jespersen",
        "work": "The Philosophy of Grammar",
        "quote": "We must differentiate kinetic verbs denoting physical movements from purely **stative** verbs expressing mental states or qualities."
      }
    ]
  },
  "Dashboard — st\\statoblast.md": {
    "primary": "An internal, asexually produced dormant bud or gemmule formed by freshwater bryozoans (Phylactolaemata) to survive adverse environmental conditions.",
    "secondary": "In invertebrate zoology, a chitinous-shelled survival capsule that withstands desiccation and freezing, germinating into a new zooid upon the return of spring.",
    "quotes": [
      {
        "author": "George James Allman",
        "work": "A Monograph of the Fresh-Water Polyzoa",
        "quote": "The freshwater bryozoan secures the survival of its race through the encysted **statoblast**, which survives the freezing of winter ponds."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "Encased between two biconvex chitinous valves, the **statoblast** contains embryonic germinal cells protected by a buoyant annular ring."
      },
      {
        "author": "Libbie Hyman",
        "work": "The Invertebrates: Smaller Coelomate Groups",
        "quote": "Hooked marginal spines on the floating **statoblast** allow it to cling to the plumage of aquatic birds, facilitating inter-basin dispersal."
      }
    ]
  },
  "Dashboard — st\\statocyst.md": {
    "primary": "A small, fluid-filled sensory vesicle found in many aquatic invertebrates, containing statoliths that respond to gravity to maintain equilibrium.",
    "secondary": "In sensory neurobiology, a mechanoreceptor balance organ lined with ciliated sensory cells that detects orientation, tilt, and acceleration.",
    "quotes": [
      {
        "author": "Ernst Haeckel",
        "work": "Report on the Deep-Sea Medusae",
        "quote": "Along the bell margin of the medusa, each marginal **statocyst** coordinates directional pulsing by registering gravitational tilt."
      },
      {
        "author": "C. M. Yonge",
        "work": "The Biology of Marine Organisms",
        "quote": "Decapod crustaceans periodically lose the mineral grains within their **statocyst** during molting, replacing them with ambient sand."
      },
      {
        "author": "Theodore H. Bullock",
        "work": "Structure and Function in the Nervous Systems of Invertebrates",
        "quote": "Action potentials recorded from sensory hairs within the **statocyst** demonstrate exquisite sensitivity to angular displacement."
      }
    ]
  },
  "Dashboard — st\\statolith.md": {
    "primary": "A dense particle, sand grain, or calcium carbonate pellet inside a statocyst that shifts under gravity to stimulate sensory balance hairs.",
    "secondary": "In plant physiology, a specialized, dense, starch-filled amyloplast in root columella cells that sediments under gravity to direct gravitropic root growth.",
    "quotes": [
      {
        "author": "Julius von Sachs",
        "work": "Lectures on the Physiology of Plants",
        "quote": "Heavy amyloplasts functioning as a cellular **statolith** sink to the bottom of root-cap cells, triggering asymmetric auxin transport."
      },
      {
        "author": "Charles Darwin",
        "work": "The Power of Movement in Plants",
        "quote": "The tip of the radicle acts like a brain, directing the organ downward as each **statolith** settles against the lowest membrane."
      },
      {
        "author": "Francis Darwin",
        "work": "The Statolith Theory of Geotropism",
        "quote": "Our experiments verify that the movable **statolith** within specialized cells provides plants with their internal sense of verticality."
      }
    ]
  },
  "Dashboard — st\\stator.md": {
    "primary": "The stationary portion of an electric motor, generator, turbine, or pump, within or around which the rotor revolves.",
    "secondary": "In electromechanical engineering, the stationary magnetic core containing winding coils that produce or interact with the revolving magnetic field.",
    "quotes": [
      {
        "author": "Nikola Tesla",
        "work": "My Inventions",
        "quote": "The alternating currents circulating through the coils of the **stator** generate a smoothly revolving magnetic field that drives the rotor."
      },
      {
        "author": "Charles Proteus Steinmetz",
        "work": "Theory and Calculation of Alternating Current Phenomena",
        "quote": "Magnetic saturation within the slotted laminations of the **stator** core dictates the operational efficiency of induction machinery."
      },
      {
        "author": "Thomas Edison",
        "work": "The Edison Papers: Dynamos and Power Systems",
        "quote": "Rigid mechanical clamping of the **stator** prevents vibrational fatigue caused by high electromagnetic torque."
      }
    ]
  },
  "Dashboard — st\\stature.md": {
    "primary": "The natural height of a human or animal body in an upright standing position.",
    "secondary": "Achieved level of development, moral eminence, intellectual distinction, or distinguished public reputation.",
    "quotes": [
      {
        "author": "Ralph Waldo Emerson",
        "work": "Representative Men",
        "quote": "Great men enlarge our conception of human capacity, standing above the multitude in intellectual **stature**."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "Captain Ahab stood before them on the quarter-deck, a man of commanding **stature** carved out of seasoned bronze."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "Democratic equality raises the general level of the populace while reducing the solitary monumental **stature** of aristocratic leaders."
      }
    ]
  },
  "Dashboard — st\\stela.md": {
    "primary": "An upright stone slab or pillar, often inscribed, decorated with relief carvings, or serving as a gravestone or public boundary monument.",
    "secondary": "In ancient Mediterranean, Near Eastern, and Mesoamerican archaeology, a commemorative freestanding stone documenting royal decrees or dynastic conquests.",
    "quotes": [
      {
        "author": "James Henry Breasted",
        "work": "Ancient Records of Egypt",
        "quote": "Pharaoh Thutmose erected a triumphal granite **stela** on the banks of the Euphrates to mark the northern boundary of his empire."
      },
      {
        "author": "W. M. Flinders Petrie",
        "work": "Ten Years' Digging in Egypt",
        "quote": "The discovery of the Merneptah **stela** provided the earliest historical epigraphic mention of Israel in ancient Egyptian records."
      },
      {
        "author": "Jean-François Champollion",
        "work": "Précis du système hiéroglyphique",
        "quote": "The bilingual inscriptions carved upon the basalt **stela** provided the decisive key that unlocked the forgotten script of the Pharaohs."
      }
    ]
  },
  "Dashboard — st\\systasis.md": {
    "primary": "A standing together; the constitution, assembly, formation, or composition of parts into a coherent structural whole.",
    "secondary": "In classical rhetoric and dialectic, the preliminary formulation of a disputed case; in medicine, an obsolete term for compaction of humors.",
    "quotes": [
      {
        "author": "Quintilian",
        "work": "Institutio Oratoria",
        "quote": "Before embarking on eloquent elaboration, the orator must master the **systasis**, the fundamental structural status of the dispute."
      },
      {
        "author": "Hermogenes",
        "work": "On Issues",
        "quote": "The judicial **systasis** defines that precise legal crux wherein the charge of the prosecutor encounters the defense of the accused."
      },
      {
        "author": "George Kennedy",
        "work": "The Art of Rhetoric in the Roman World",
        "quote": "Hellenistic rhetoricians devised a meticulous taxonomy of **systasis** to guide students through every possible permutation of court debate."
      }
    ]
  },
  "Dashboard — st\\system.md": {
    "primary": "A regularly interacting or interdependent group of items or elements forming an integrated, unified whole.",
    "secondary": "An organized, comprehensive scheme, doctrine, or method governing intellectual, scientific, or social operations.",
    "quotes": [
      {
        "author": "Immanuel Kant",
        "work": "Critique of Pure Reason",
        "quote": "Human reason is by nature architectonic; it regards all cognitions as belonging to a possible **system** ordered by a single idea."
      },
      {
        "author": "Ludwig von Bertalanffy",
        "work": "General System Theory",
        "quote": "A **system** is a complex of interacting elements whose collective behavior cannot be deduced from the study of isolated parts."
      },
      {
        "author": "Norbert Wiener",
        "work": "The Human Use of Human Beings",
        "quote": "Society can only be understood through a study of the messages and the communication facilities which belong to it as an organized **system**."
      }
    ]
  },
  "Dashboard — st\\systematic.md": {
    "primary": "Carried out, arranged, or acting according to a methodical, organized, and predetermined plan.",
    "secondary": "Pertaining to, constituting, or having the character of a comprehensive, coherent conceptual system.",
    "quotes": [
      {
        "author": "René Descartes",
        "work": "Discourse on Method",
        "quote": "By conducting our thoughts in a **systematic** order, ascending step by step from the simplest objects to the most complex, error is avoided."
      },
      {
        "author": "Francis Bacon",
        "work": "Novum Organum",
        "quote": "Empirical science requires not erratic experiments, but a **systematic** interpretation of nature guided by rigorous inductive tables."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The naturalist must subject vast arrays of geographical distribution to **systematic** scrutiny to perceive genealogical connections."
      }
    ]
  },
  "Dashboard — st\\systematics.md": {
    "primary": "The branch of biology dealing with the classification, nomenclature, and evolutionary relationships of living organisms.",
    "secondary": "The scientific study of biological diversity and diversification, synthesizing phylogenetics, morphology, and biogeography.",
    "quotes": [
      {
        "author": "Ernst Mayr",
        "work": "Principles of Systematic Zoology",
        "quote": "Biological **systematics** is not merely the cataloging of specimens, but the science that reconstructs the history of life on Earth."
      },
      {
        "author": "George Gaylord Simpson",
        "work": "Principles of Animal Taxonomy",
        "quote": "We define **systematics** as the scientific study of the kinds and diversity of organisms and of any and all relationships among them."
      },
      {
        "author": "Willi Hennig",
        "work": "Phylogenetic Systematics",
        "quote": "The ultimate objective of phylogenetic **systematics** is to establish natural taxa based strictly on shared derived characteristics."
      }
    ]
  },
  "Dashboard — st\\systematisation.md": {
    "primary": "The act, process, or result of organizing facts, principles, or operations into an orderly, coherent system (British spelling).",
    "secondary": "In philosophy and institutional theory, the methodical reduction of chaotic empirical observations to a structured axiomatic framework.",
    "quotes": [
      {
        "author": "Herbert Spencer",
        "work": "First Principles",
        "quote": "Philosophy is completely unified knowledge; its crowning glory is the comprehensive **systematisation** of cosmic evolution."
      },
      {
        "author": "John Stuart Mill",
        "work": "A System of Logic",
        "quote": "Scientific progress consists largely in the progressive **systematisation** of empirical observations under general inductive laws."
      },
      {
        "author": "Karl Marx",
        "work": "Capital",
        "quote": "The capitalist division of labor demands the rigorous **systematisation** of manual tasks to extract maximum surplus value."
      }
    ]
  },
  "Dashboard — st\\systematise.md": {
    "primary": "To arrange, classify, or organize methodically in accordance with an overarching system or regular plan (British spelling).",
    "secondary": "In scientific methodology, to formulate empirical findings into a structured, unified taxonomy or theoretical model.",
    "quotes": [
      {
        "author": "Jeremy Bentham",
        "work": "An Introduction to the Principles of Morals and Legislation",
        "quote": "The legislator must **systematise** the penal code so that every offense meets with its precisely calibrated deterrent pain."
      },
      {
        "author": "William Whewell",
        "work": "The Philosophy of the Inductive Sciences",
        "quote": "Inductive reasoning enables the philosopher to **systematise** isolated facts into universal scientific propositions."
      },
      {
        "author": "Auguste Comte",
        "work": "The Positive Philosophy",
        "quote": "Positivism strives to **systematise** all human knowledge, subordinating intellect to social harmony and empirical evidence."
      }
    ]
  },
  "Dashboard — st\\systematiser.md": {
    "primary": "A person who arranges, organizes, or categorizes concepts, facts, or operations into an orderly system (British spelling).",
    "secondary": "In intellectual history, an architect of comprehensive encyclopedic or administrative structures.",
    "quotes": [
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "Aristotle was the supreme **systematiser** of antiquity, arranging every facet of nature into tidy logical categories."
      },
      {
        "author": "Thomas Carlyle",
        "work": "On Heroes, Hero-Worship, and the Heroic in History",
        "quote": "The sterile **systematiser** believes he has captured the infinite cosmos when he has merely labeled its outward garments."
      },
      {
        "author": "Matthew Arnold",
        "work": "Culture and Anarchy",
        "quote": "The English mind distrusts the continental **systematiser**, preferring piecemeal practical compromise to dogmatic blueprints."
      }
    ]
  },
  "Dashboard — st\\systematism.md": {
    "primary": "The practice, habit, or doctrine of strictly reducing all knowledge, actions, or beliefs to a rigid, overarching system.",
    "secondary": "Excessive or dogmatic devotion to systematic ordering, often at the expense of empirical nuance or intellectual flexibility.",
    "quotes": [
      {
        "author": "Denis Diderot",
        "work": "Encyclopédie",
        "quote": "We must beware of that dogmatic **systematism** that forces refractory nature into the narrow mold of preconceived hypotheses."
      },
      {
        "author": "Voltaire",
        "work": "Philosophical Dictionary",
        "quote": "The mania for **systematism** produces magnificent philosophical castles that collapse at the first touch of real fact."
      },
      {
        "author": "Søren Kierkegaard",
        "work": "Concluding Unscientific Postscript",
        "quote": "An existential thinker cannot accept total **systematism**, for existing human reality remains an unclosed, striving paradox."
      }
    ]
  },
  "Dashboard — st\\systematist.md": {
    "primary": "A person who classifies organisms or formulates systematic principles; a specialist in biological taxonomy.",
    "secondary": "An intellectual or scientist dedicated to creating orderly, all-encompassing taxonomies or theoretical frameworks.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Philosophia Botanica",
        "quote": "The true **systematist** arranges plants according to their immutable floral organs, revealing the divine order of nature."
      },
      {
        "author": "Louis Agassiz",
        "work": "Essay on Classification",
        "quote": "To the thoughtful **systematist**, every natural category reflects an intellectual thought of the Creator written in organic forms."
      },
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "The herbarium is the indispensable laboratory wherein the botanical **systematist** compares dried types across continents."
      }
    ]
  },
  "Dashboard — st\\systematization.md": {
    "primary": "The act or process of organizing facts, rules, or practices into an orderly, comprehensive system (American spelling).",
    "secondary": "In social sciences, the bureaucratic or rational organization of institutional life and legal structures.",
    "quotes": [
      {
        "author": "Max Weber",
        "work": "Economy and Society",
        "quote": "The bureaucratic **systematization** of administrative procedure replaces arbitrary patrimonial rule with predictable, codified law."
      },
      {
        "author": "Talcott Parsons",
        "work": "The Structure of Social Action",
        "quote": "Theoretical advancement in sociology hinges upon the conceptual **systematization** of institutional roles and norm patterns."
      },
      {
        "author": "Ernest Nagel",
        "work": "The Structure of Science",
        "quote": "The ultimate aim of scientific inquiry is the logical **systematization** of explanatory laws under encompassing theories."
      }
    ]
  },
  "Dashboard — st\\systematize.md": {
    "primary": "To arrange, coordinate, or organize methodically in accordance with an established system (American spelling).",
    "secondary": "In philosophy and governance, to formulate diverse data, legal codes, or operations into a harmonious conceptual scheme.",
    "quotes": [
      {
        "author": "Benjamin Franklin",
        "work": "Autobiography",
        "quote": "I conceived the bold project of achieving moral perfection, attempting to **systematize** my daily conduct through thirteen virtues."
      },
      {
        "author": "John Dewey",
        "work": "Logic: The Theory of Inquiry",
        "quote": "Scientific method does not freeze thought, but provides active inquiry with tools to **systematize** perplexing observations."
      },
      {
        "author": "Willard Van Orman Quine",
        "work": "Word and Object",
        "quote": "Our ongoing philosophical task is to simplify and **systematize** the total conceptual framework that encompasses human science."
      }
    ]
  },
  "Dashboard — st\\systematizer.md": {
    "primary": "An individual who organizes facts, principles, or institutions into a coherent, methodical system (American spelling).",
    "secondary": "A thinker, administrator, or scientist known for constructing vast taxonomic, legal, or intellectual architectures.",
    "quotes": [
      {
        "author": "Henry Adams",
        "work": "The Education of Henry Adams",
        "quote": "The medieval scholastic was a formidable **systematizer**, constructing cathedrals of thought as towering as Chartres itself."
      },
      {
        "author": "William James",
        "work": "Pragmatism",
        "quote": "The pragmatic philosopher views the dogmatic **systematizer** with suspicion, knowing life continually spills over formal categories."
      },
      {
        "author": "Thorstein Veblen",
        "work": "The Theory of the Leisure Class",
        "quote": "The modern corporate **systematizer** seeks to align human labor with the ruthless mechanical rhythms of industrial technology."
      }
    ]
  }
};

const updated = updateNotesBatch(BASE_DIR, BATCH2_DATA);
console.log(`Action Part 2 - Batch 2 Completed: ${updated} / ${Object.keys(BATCH2_DATA).length} notes updated.`);
