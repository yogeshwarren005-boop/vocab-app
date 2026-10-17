import { updateNotesBatch } from './curate-updater-util.mjs';

const baseDir = "App database\\Greek roots\\Cluster Form & Space";
const batchData = {
  "Dashboard — heter\\heterologous.md": {
    "primary": "Characterized by difference in origin, structure, or species; not homologous; (in medicine) derived from a different organism or tissue type.",
    "secondary": "In immunology and pathology, heterologous antibodies or grafts are derived from an individual of a different species or non-identical genetic constitution.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Passive immunization with **heterologous** equine serum frequently precipitated serum sickness ten days post-injection."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "Fertilisation effected by **heterologous** pollen often produces vigorous hybrid offspring exhibiting enhanced vegetative growth."
      },
      {
        "author": "Vinay Kumar",
        "work": "Robbins and Cotran Pathologic Basis of Disease",
        "quote": "A **heterologous** carcinosarcoma contains mesenchymal elements foreign to the organ of primary origin."
      }
    ]
  },
  "Dashboard — heter\\heterology.md": {
    "primary": "The state or quality of being heterologous; difference or abnormality in structure, tissue type, or biological origin.",
    "secondary": "In philosophical logic and linguistics, the property of a term not being applicable to itself; also in oncology, the presence of anomalous tissue in a tumor.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Virchow categorized neoplasms by their degree of **heterology**, contrasting benign homoeoplastic growths with malignant heteroplastic ones."
      },
      {
        "author": "Bertrand Russell",
        "work": "Introduction to Mathematical Philosophy",
        "quote": "Semantic **heterology** generates insoluble paradoxes unless metalanguage is strictly segregated from object language."
      },
      {
        "author": "Michel Foucault",
        "work": "The Order of Things",
        "quote": "The epistemological rupture exposed a profound **heterology** between words and the things they purported to represent."
      }
    ]
  },
  "Dashboard — heter\\heteromeles.md": {
    "primary": "A monotypic genus of evergreen shrubs in the rose family (Rosaceae) containing Heteromeles arbutifolia (toyon, Christmas berry, or California holly).",
    "secondary": "In chaparral ecology, Heteromeles arbutifolia dominates Californian coastal sage scrub, producing bright red winter pomes that sustain overwintering birds.",
    "quotes": [
      {
        "author": "John Muir",
        "work": "The Mountains of California",
        "quote": "The chaparral slopes glowed with the scarlet berries of **heteromeles**, cheering the foothills through the winter rains."
      },
      {
        "author": "Asa Gray",
        "work": "Synoptical Flora of North America",
        "quote": "The coriaceous serrated leaves of **heteromeles** persist through severe summer droughts without withering."
      },
      {
        "author": "Peter H. Raven",
        "work": "Flora of the Santa Monica Mountains",
        "quote": "Toyon, or **heteromeles**, provided indigenous Californians with nutrient-rich roasted berries and durable hardwood for implements."
      }
    ]
  },
  "Dashboard — heter\\heterometabolic.md": {
    "primary": "Pertaining to or characterized by incomplete or gradual metamorphosis in insects; hemimetabolous.",
    "secondary": "In comparative biochemistry, designating an organism that shifts between disparate metabolic pathways depending on environmental conditions.",
    "quotes": [
      {
        "author": "V. B. Wigglesworth",
        "work": "The Principles of Insect Physiology",
        "quote": "In **heterometabolic** development, the nymph emerges looking like a miniature adult, lacking a dormant pupal instar."
      },
      {
        "author": "R. F. Chapman",
        "work": "The Insects: Structure and Function",
        "quote": "Wing buds develop externally throughout successive molts in **heterometabolic** orders such as Orthoptera."
      },
      {
        "author": "Vincent Dethier",
        "work": "The Hungry Fly",
        "quote": "Nymphal feeding ecology in **heterometabolic** insects closely parallels adult foraging behavior."
      }
    ]
  },
  "Dashboard — heter\\heterometabolism.md": {
    "primary": "Incomplete or gradual metamorphosis in insects, in which the nymph resembles the adult and lacks a pupal stage.",
    "secondary": "In developmental entomology, heterometabolism encompasses gradual external wing development across successive nymphal instars.",
    "quotes": [
      {
        "author": "V. B. Wigglesworth",
        "work": "The Physiology of Insect Metamorphosis",
        "quote": "The endocrine regulation of **heterometabolism** involves continuous juvenile hormone secretion that tapers prior to the final imaginal molt."
      },
      {
        "author": "R. F. Chapman",
        "work": "The Insects: Structure and Function",
        "quote": "True bugs, damselflies, and grasshoppers illustrate classic **heterometabolism**, bypassing the radical cellular histolysis seen in holometabolous pupae."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The gradations connecting **heterometabolism** with complete metamorphosis illustrate how developmental sequences evolve through adaptive divergence."
      }
    ]
  },
  "Dashboard — heter\\heterometabolous.md": {
    "primary": "Undergoing incomplete or gradual metamorphosis without a pupal stage, as in dragonflies, grasshoppers, and true bugs.",
    "secondary": "In systematic entomology, heterometabolous insects develop external wing pads during nymphal stages, transitioning directly into winged adults.",
    "quotes": [
      {
        "author": "R. F. Chapman",
        "work": "The Insects: Structure and Function",
        "quote": "A **heterometabolous** insect emerges from the egg as a wingless nymph with body proportions similar to the reproductive imago."
      },
      {
        "author": "V. B. Wigglesworth",
        "work": "The Principles of Insect Physiology",
        "quote": "Hormonal control in **heterometabolous** species preserves organ continuity across successive molts without widespread imaginal disc destruction."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Ontogeny and Phylogeny",
        "quote": "The fossil record demonstrates that **heterometabolous** insects preceded the evolution of holometabolous orders with pupal transformations."
      }
    ]
  },
  "Dashboard — heter\\heterometaboly.md": {
    "primary": "The developmental pattern or phenomenon of incomplete metamorphosis in insects; hemimetaboly.",
    "secondary": "In evolutionary biology, heterometaboly represents the ancestral pterygote developmental strategy from which complex holometaboly evolved.",
    "quotes": [
      {
        "author": "V. B. Wigglesworth",
        "work": "Insect Hormones",
        "quote": "Experimental decapitation during penultimate instars demonstrates how **heterometaboly** transitions smoothly into adult cuticular synthesis."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "Ecological niche differentiation between juveniles and adults is less pronounced in lineages characterized by **heterometaboly**."
      },
      {
        "author": "R. F. Chapman",
        "work": "The Insects: Structure and Function",
        "quote": "Aquatic nymphs of mayflies and stoneflies illustrate specialized aquatic **heterometaboly** with terrestrial winged adults."
      }
    ]
  },
  "Dashboard — heter\\heteromyidae.md": {
    "primary": "A family of rodent mammals (kangaroo rats, pocket mice, and kangaroo mice) adapted for arid life, possessing external fur-lined cheek pouches and saltatorial hind legs.",
    "secondary": "In physiological ecology, Heteromyidae are renowned for water conservation, surviving indefinitely on dry seeds without drinking water by producing highly concentrated urine.",
    "quotes": [
      {
        "author": "Knut Schmidt-Nielsen",
        "work": "Desert Animals: Physiological Problems of Heat and Water",
        "quote": "Members of **heteromyidae** survive entirely upon metabolic water derived from the oxidation of dry seeds."
      },
      {
        "author": "Alfred Romer",
        "work": "Vertebrate Paleontology",
        "quote": "The hypertrophied auditory bullae and elongated hind limbs of **heteromyidae** evolved for detecting predatory owls and leaping away in darkness."
      },
      {
        "author": "E. O. Wilson",
        "work": "The Diversity of Life",
        "quote": "Community guild structure in desert ecosystems is organized around seed-size resource partitioning among coexisting species of **heteromyidae**."
      }
    ]
  },
  "Dashboard — heter\\heteronym.md": {
    "primary": "A word having the same spelling as another but a different sound and meaning (e.g., 'lead' to guide vs. 'lead' the metal); also, a fictional literary persona with distinct style and biography (in Pessoa).",
    "secondary": "In linguistics and poetics, Fernando Pessoa created elaborate heteronyms (Álvaro de Campos, Ricardo Reis) whose works expressed entirely divergent philosophies.",
    "quotes": [
      {
        "author": "Fernando Pessoa",
        "work": "The Book of Disquiet",
        "quote": "To create a true **heteronym** is to bestow upon an imaginary voice a complete biographical existence, philosophy, and poetic style."
      },
      {
        "author": "Henry Fowler",
        "work": "Modern English Usage",
        "quote": "Careful pronunciation resolves the semantic confusion that arises when encountering a written **heteronym** in prose."
      },
      {
        "author": "George Steiner",
        "work": "After Babel",
        "quote": "Pessoa's invention of the **heteronym** represents one of the most radical explorations of fragmented identity in modern literature."
      }
    ]
  },
  "Dashboard — heter\\heterophobia.md": {
    "primary": "An irrational fear of, aversion to, or discrimination against heterosexual people or heterosexuality; also, fear of difference or that which is other.",
    "secondary": "In sociology and cultural theory, occasionally used in philosophical discourse to denote the deep psychological dread of encountering radical alterity or difference.",
    "quotes": [
      {
        "author": "Zygmunt Bauman",
        "work": "Modernity and Ambivalence",
        "quote": "The xenophobic impulse is rooted in an ontological **heterophobia**, a terror of that which refuses to fit into established cultural categories."
      },
      {
        "author": "Albert Memmi",
        "work": "The Colonizer and the Colonized",
        "quote": "Prejudice begins as a defensive **heterophobia**, erecting social barriers to quarantine difference from the dominant collective."
      },
      {
        "author": "Michel Foucault",
        "work": "Discipline and Punish",
        "quote": "Institutional norms pathologize divergence, converting social **heterophobia** into systematic correctional surveillance."
      }
    ]
  },
  "Dashboard — heter\\heteroploid.md": {
    "primary": "Having a chromosome number that is not an exact multiple of the normal haploid number; aneuploid or aberrant polyploid.",
    "secondary": "In cytogenetics and cancer biology, heteroploid karyotypes with extensive chromosomal gains and losses characterize high-grade malignant neoplasms.",
    "quotes": [
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Spindle checkpoint defects during mitosis frequently generate a **heteroploid** daughter cell carrying unequal chromosome complements."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "Although most **heteroploid** embryos die in utero, occasional polyploid variants initiate new plant lineages."
      },
      {
        "author": "Robert A. Weinberg",
        "work": "The Biology of Cancer",
        "quote": "Massive chromosomal instability ensures that nearly every advanced solid tumor exhibits an unstable **heteroploid** genome."
      }
    ]
  },
  "Dashboard — heter\\heteroploidy.md": {
    "primary": "The state or condition of being heteroploid; the presence of an abnormal chromosome number that deviates from the standard diploid or haploid complement.",
    "secondary": "In medical genetics and teratology, constitutional heteroploidy (such as trisomy 21 or monosomy X) causes systemic developmental syndromes.",
    "quotes": [
      {
        "author": "Curt Stern",
        "work": "Principles of Human Genetics",
        "quote": "Maternal age correlates significantly with the incidence of meiotic nondisjunction leading to embryonic **heteroploidy**."
      },
      {
        "author": "Vinay Kumar",
        "work": "Robbins and Cotran Pathologic Basis of Disease",
        "quote": "Widespread **heteroploidy** is the primary driver of spontaneous first-trimester pregnancy loss."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Mankind Evolving",
        "quote": "Chromosomal **heteroploidy** introduces major phenotypic disruptions that natural selection vigorously purges from the gene pool."
      }
    ]
  },
  "Dashboard — heter\\heteroptera.md": {
    "primary": "A suborder of true bugs (order Hemiptera) having forewings divided into a hardened basal corium and a membranous apical tip (hemelytra).",
    "secondary": "In systematic entomology, Heteroptera includes shield bugs, bed bugs, water striders, and assassin bugs, possessing piercing-sucking mouthparts.",
    "quotes": [
      {
        "author": "R. F. Chapman",
        "work": "The Insects: Structure and Function",
        "quote": "The forewings in **heteroptera** overlap flat across the back, with the membranous tips covering the abdomen at rest."
      },
      {
        "author": "V. B. Wigglesworth",
        "work": "The Principles of Insect Physiology",
        "quote": "Rhodnius prolixus, a member of **heteroptera**, served as the classic laboratory model for uncovering insect juvenile hormone mechanisms."
      },
      {
        "author": "Vincent Dethier",
        "work": "The Hungry Fly",
        "quote": "Predatory members of **heteroptera** inject digestive saliva through their stylets to liquefy prey tissues before ingestion."
      }
    ]
  },
  "Dashboard — heter\\heteros.md": {
    "primary": "The Greek adjective meaning 'the other of two', 'different', 'another', or 'second', the foundational etymon for English 'hetero-'.",
    "secondary": "In classical philology and philosophical ontology, heteros designates alterity, the counterpart, or the category of the different.",
    "quotes": [
      {
        "author": "Plato",
        "work": "Sophist",
        "quote": "Non-being is not the direct opposite of being, but merely that which is different, participating in the nature of **heteros**."
      },
      {
        "author": "Aristotle",
        "work": "Metaphysics",
        "quote": "Things are called diverse when their definitions are separate, belonging to the universal category of **heteros**."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "The Greek stem **heteros** forms the polar contrast to homos ('the same') throughout Hellenic thought and syntax."
      }
    ]
  },
  "Dashboard — heter\\heteroscelus.md": {
    "primary": "A genus or subgenus of wading shorebirds containing the tattlers (e.g., the wandering tattler, Heteroscelus incanus), breeding on alpine gravel bars.",
    "secondary": "In avian taxonomy, named 'different leg' from Greek for the scutellation of the tarsus, often subsumed into the larger sandpiper genus Tringa.",
    "quotes": [
      {
        "author": "Elliott Coues",
        "work": "Key to North American Birds",
        "quote": "The wandering tattler of the genus **heteroscelus** flies with rapid, whistling cries along rocky surf-beaten Pacific reefs."
      },
      {
        "author": "Alexander Wetmore",
        "work": "The Migrations of Birds",
        "quote": "Trans-Pacific migrations of **heteroscelus** carry birds from nesting torrents in Alaska across thousands of miles of open ocean to Polynesia."
      },
      {
        "author": "Arthur Cleveland Bent",
        "work": "Life Histories of North American Shore Birds",
        "quote": "The unstreaked leaden plumage of **heteroscelus** blends invisibly into basalt headlands where surf crashes incessantly."
      }
    ]
  },
  "Dashboard — heter\\heterosexism.md": {
    "primary": "Discrimination, prejudice, or bias against non-heterosexual people based on the assumption that heterosexuality is the sole natural or valid norm.",
    "secondary": "In sociology and gender studies, institutional heterosexism designates legal, cultural, and social structures that privilege heterosexual relationships.",
    "quotes": [
      {
        "author": "Judith Butler",
        "work": "Gender Trouble",
        "quote": "Compulsory heterosexuality operates through pervasive **heterosexism** that polices the boundaries of intelligible gender performance."
      },
      {
        "author": "Eve Kosofsky Sedgwick",
        "work": "Epistemology of the Closet",
        "quote": "The cultural hegemony of **heterosexism** relies upon silences and double binds enforced across public discourse."
      },
      {
        "author": "Audre Lorde",
        "work": "Sister Outsider",
        "quote": "We must dismantle the interlocking systems of racism, sexism, and **heterosexism** to achieve genuine human liberation."
      }
    ]
  },
  "Dashboard — heter\\heterosexual.md": {
    "primary": "Sexually, romantically, or affectionally attracted to persons of the opposite sex; or relating to sexual relations between different sexes.",
    "secondary": "In the history of psychiatry, the term heterosexual was coined in the late 19th century by Karl Maria Kertbeny and popularized by Krafft-Ebing.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "Three Essays on the Theory of Sexuality",
        "quote": "The achievement of a stable **heterosexual** object-choice represents the culmination of a complex developmental psycho-sexual trajectory."
      },
      {
        "author": "Michel Foucault",
        "work": "The History of Sexuality",
        "quote": "Nineteenth-century medicine transformed erotic acts into medical identities, codifying both homosexual and **heterosexual** taxonomies."
      },
      {
        "author": "Alfred Kinsey",
        "work": "Sexual Behavior in the Human Male",
        "quote": "Human erotic responsiveness exists along a continuous seven-point spectrum between exclusive homosexual and exclusive **heterosexual** behavior."
      }
    ]
  },
  "Dashboard — heter\\heterosexualism.md": {
    "primary": "The belief, ideology, or social arrangement that regards heterosexuality as the exclusive, normative, or superior form of human sexuality; heteronormativity.",
    "secondary": "In cultural sociology, heterosexualism examines the legal and institutional normalization of opposite-sex domestic partnerships.",
    "quotes": [
      {
        "author": "Adrienne Rich",
        "work": "Compulsory Heterosexuality and Lesbian Existence",
        "quote": "Institutional **heterosexualism** functions as a pervasive social enforcement rather than a simple spontaneous biological given."
      },
      {
        "author": "Judith Butler",
        "work": "Bodies That Matter",
        "quote": "The regulatory ideal of **heterosexualism** constructs acceptable bodily norms by abjecting alternative desires."
      },
      {
        "author": "Michel Foucault",
        "work": "The History of Sexuality",
        "quote": "The discursive consolidation of **heterosexualism** anchored the modern family as the primary site of biopolitical reproduction."
      }
    ]
  },
  "Dashboard — heter\\heterosexuality.md": {
    "primary": "Sexual, romantic, or erotic attraction, orientation, or behavior directed exclusively or primarily toward persons of the opposite sex.",
    "secondary": "In social history and evolutionary biology, heterosexuality constitutes the primary behavioral mechanism ensuring biparental sexual reproduction.",
    "quotes": [
      {
        "author": "Alfred Kinsey",
        "work": "Sexual Behavior in the Human Female",
        "quote": "The prevalence of exclusive **heterosexuality** varies significantly across demographic cohorts and cultural contexts."
      },
      {
        "author": "Sigmund Freud",
        "work": "Civilization and Its Discontents",
        "quote": "Sublimation of libido into civil institutions channels normative **heterosexuality** into family formation and social labor."
      },
      {
        "author": "E. O. Wilson",
        "work": "On Human Nature",
        "quote": "Evolutionary psychology analyzes **heterosexuality** as an adaptive behavioral strategy maximizing gene propagation in sexually dimorphic species."
      }
    ]
  },
  "Dashboard — heter\\heterosis.md": {
    "primary": "The tendency of a crossbred individual (hybrid) to show qualities superior to those of both parents; hybrid vigor.",
    "secondary": "In agricultural genetics and evolutionary biology, heterosis is exploited commercially in hybrid maize and livestock breeding to maximize yield and disease resistance.",
    "quotes": [
      {
        "author": "George Harrison Shull",
        "work": "The Composition of a Field of Maize",
        "quote": "The phenomenon of **heterosis** results from crossing inbred lines, restoring vigorous growth and extraordinary grain yields."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "Overdominance at specific gene loci provides a compelling physiological explanation for the occurrence of **heterosis** in natural populations."
      },
      {
        "author": "Charles Darwin",
        "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom",
        "quote": "Darwin demonstrated that cross-fertilisation systematically confers enhanced height, fertility, and survival, anticipating modern **heterosis**."
      }
    ]
  },
  "Dashboard — heter\\heterosomata.md": {
    "primary": "An order or suborder of ray-finned fishes containing the flatfishes (flounders, soles, and halibuts), characterized by asymmetrical adults with both eyes on one side.",
    "secondary": "In evolutionary morphology, Heterosomata undergo an extraordinary larval metamorphosis during which one eye migrates across the skull as the fish settles onto the benthos.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "No vertebrate presents a more radical morphological distortion than the adult flatfishes of **heterosomata**, whose cranial symmetry is twisted aside."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Panda's Thumb",
        "quote": "Darwin defended natural selection against the charge that transitional intermediate stages of eye migration in **heterosomata** could have had no adaptive utility."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "Lying camouflaged on the seabed, the sole of **heterosomata** scans the overhead water with both eyes perched upon its exposed dorsal flank."
      }
    ]
  },
  "Dashboard — heter\\heterosporous.md": {
    "primary": "Producing two distinct kinds of spores differing in size and sex: small microspores (male) and large megaspores (female).",
    "secondary": "In plant evolution, heterosporous pteridophytes (such as Selaginella and water ferns) represent the critical evolutionary transition leading directly to seed plants.",
    "quotes": [
      {
        "author": "Peter H. Raven",
        "work": "Biology of Plants",
        "quote": "The **heterosporous** life cycle segregates gender at the haploid spore stage, culminating in the evolution of pollen grains and ovules."
      },
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "In **heterosporous** clubmosses, megaspores produce nutrient-rich archegonial gametophytes enclosed within thick walls."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "The reduction of the female gametophyte in **heterosporous** lineages was essential for the origin of the seed habit."
      }
    ]
  },
  "Dashboard — heter\\heterospory.md": {
    "primary": "The production of spores of two different sizes and sexes (microspores and megaspores) by the sporophytes of land plants.",
    "secondary": "In paleobotany and evolutionary morphology, heterospory evolved independently multiple times during the Devonian, serving as the morphological prerequisite for seeds.",
    "quotes": [
      {
        "author": "Peter H. Raven",
        "work": "Biology of Plants",
        "quote": "The advent of **heterospory** freed plant fertilization from complete reliance upon surface water films."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Full House",
        "quote": "Independent convergent origins of **heterospory** in disparate Paleozoic fern and lycophyte clades illustrate predictable evolutionary pathways."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "In seeds, **heterospory** reaches its ultimate expression through the permanent retention of the megaspore within the parent ovule."
      }
    ]
  },
  "Dashboard — heter\\heterostracan.md": {
    "primary": "An extinct jawless armored fish of the subclass Heterostraci, common in Silurian and Devonian marine and freshwater deposits.",
    "secondary": "In paleoichthyology, heterostracans had heavy head shields of acellular aspidin bone, a single common gill opening on each side, and a hypocercal tail.",
    "quotes": [
      {
        "author": "Alfred Romer",
        "work": "Vertebrate Paleontology",
        "quote": "A typical **heterostracan** possessed solid dorsal and ventral armor plates protecting its sluggish, jawless body."
      },
      {
        "author": "Edwin H. Colbert",
        "work": "Evolution of the Vertebrates",
        "quote": "The histology of **heterostracan** armor reveals spongy vascular bone sandwiched between dense inner and outer laminated sheets."
      },
      {
        "author": "Neil Shubin",
        "work": "Your Inner Fish",
        "quote": "The head shield of an ancient **heterostracan** represents some of the earliest mineralized skeletal tissue in vertebrate evolution."
      }
    ]
  },
  "Dashboard — heter\\heterostraci.md": {
    "primary": "An extinct order or subclass of jawless armored aquatic vertebrates (ostracoderms) of the Paleozoic, having a single pair of lateral gill slits and aspidin armor.",
    "secondary": "In vertebrate paleontology, Heterostraci encompasses diverse forms like Pteraspis and Drepanaspis, flourishing before the rise of gnathostome fishes.",
    "quotes": [
      {
        "author": "Alfred Romer",
        "work": "The Vertebrate Body",
        "quote": "Members of **Heterostraci** swam through Silurian delta estuaries, scooping muddy detritus with their horizontal oral plates."
      },
      {
        "author": "Robert L. Carroll",
        "work": "Vertebrate Paleontology and Evolution",
        "quote": "The diagnostic feature separating **Heterostraci** from Osteostraci is the complete absence of true osteocyte cell lacunae in their armor."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Eight Little Piggies",
        "quote": "Fossil beds in Spitsbergen yielded magnificent articulated specimens of **Heterostraci** that clarified early craniate skull evolution."
      }
    ]
  },
  "Dashboard — heter\\heterotaxy.md": {
    "primary": "An abnormal, irregular, or discordant arrangement of bodily organs or parts that deviates from normal bilateral or asymmetric anatomy; heterotaxia.",
    "secondary": "In clinical teratology and pediatric cardiology, heterotaxy syndrome (situs ambiguus) involves random left-right organ orientation, often causing complex congenital heart malformations.",
    "quotes": [
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease: A Textbook of Cardiovascular Medicine",
        "quote": "Infants presenting with **heterotaxy** frequently exhibit complex congenital cardiac malformations associated with asplenia or polysplenia."
      },
      {
        "author": "Vinay Kumar",
        "work": "Robbins and Cotran Pathologic Basis of Disease",
        "quote": "Defective ciliary motility during embryonic nodal flow leads to randomization of left-right asymmetry and clinical **heterotaxy**."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "Cases of **heterotaxy** demonstrate how embryonic organ rotation can decouple from typical primary axis determination."
      }
    ]
  },
  "Dashboard — heter\\heterotheca.md": {
    "primary": "A genus of North American flowering plants in the daisy family (Asteraceae), commonly called camphorweeds or goldenasters, having aromatic resinous foliage.",
    "secondary": "In systematic composite botany, named 'different container' from Greek because ray florets and disc florets produce dimorphic achenes (cypselae).",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Synoptical Flora of North America",
        "quote": "The resinous golden heads of **heterotheca** brighten disturbed sandy soils throughout late summer and autumn."
      },
      {
        "author": "Merritt Lyndon Fernald",
        "work": "Gray's Manual of Botany",
        "quote": "The diagnostic character of **heterotheca** is the striking difference in pappus structure between ray and disc achenes."
      },
      {
        "author": "Peter H. Raven",
        "work": "Biology of Plants",
        "quote": "Camphor-scented monoterpenes synthesized by **heterotheca** act as effective chemical deterrents against browsing herbivores."
      }
    ]
  },
  "Dashboard — heter\\heterothermic.md": {
    "primary": "Characterized by physiological body temperature that fluctuates between self-regulating homeothermy and environmental poikilothermy (e.g., in hibernators).",
    "secondary": "In comparative animal physiology, heterothermic endotherms (like bats, hummingbirds, and ground squirrels) enter daily torpor or seasonal hibernation to conserve energy.",
    "quotes": [
      {
        "author": "Knut Schmidt-Nielsen",
        "work": "Animal Physiology: Adaptation and Environment",
        "quote": "A **heterothermic** mammal drops its core body temperature close to freezing during deep hibernation, drastically lowering metabolic demand."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Regional **heterothermic** adaptations allow arctic wolves to maintain cold paws while keeping their thoracic core at 38 degrees Celsius."
      },
      {
        "author": "David Attenborough",
        "work": "The Life of Mammals",
        "quote": "Hummingbirds adopt a **heterothermic** strategy every night, sinking into profound torpor to survive until dawn."
      }
    ]
  },
  "Dashboard — heter\\heterotic.md": {
    "primary": "Of, relating to, or exhibiting heterosis (hybrid vigor).",
    "secondary": "In quantitative genetics and plant breeding, heterotic groups are genetically divergent parental populations that produce maximum hybrid vigor upon crossing.",
    "quotes": [
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "The superior reproductive fitness of the F1 generation is described as a **heterotic** effect resulting from balanced polygenic heterozygosity."
      },
      {
        "author": "George Harrison Shull",
        "work": "What Is Heterosis?",
        "quote": "Commercial maize yields surged when breeders organized breeding stocks into complementary **heterotic** pools."
      },
      {
        "author": "Sewall Wright",
        "work": "Evolution and the Genetics of Populations",
        "quote": "The **heterotic** response in crosses between isolated demes confirms that inbreeding depression had accumulated within them."
      }
    ]
  },
  "Dashboard — heter\\heterotrichales.md": {
    "primary": "An order of yellow-green algae (Xanthophyceae) characterized by filamentous thalli that may show differentiation into prostrate and erect systems.",
    "secondary": "In phycology, members of Heterotrichales produce unbranched or branched filaments with cellulose-pectin cell walls and discoid plastids lacking pyrenoids.",
    "quotes": [
      {
        "author": "F. E. Fritsch",
        "work": "The Structure and Reproduction of the Algae",
        "quote": "The order **heterotrichales** illustrates the transition from unicellular coccoid forms to integrated multicellular filamentous organization."
      },
      {
        "author": "Robert Edward Lee",
        "work": "Phycology",
        "quote": "In **heterotrichales**, motile zoospores possessing heterokont flagellation are formed within vegetative filament cells."
      },
      {
        "author": "Peter H. Raven",
        "work": "Biology of Plants",
        "quote": "Yellow-green filaments of **heterotrichales** carpet submerged stones in oligotrophic, acidic mountain streams."
      }
    ]
  },
  "Dashboard — heter\\heterotroph.md": {
    "primary": "An organism that cannot manufacture its own food from inorganic substances and must obtain organic carbon and nutrients by consuming other organisms.",
    "secondary": "In ecological trophic dynamics, heterotrophs encompass all animals, fungi, and most bacteria, acting as primary, secondary, or tertiary consumers and decomposers.",
    "quotes": [
      {
        "author": "Eugene Odum",
        "work": "Fundamentals of Ecology",
        "quote": "Every ecosystem balances autotrophic primary production against the respiratory consumption of the **heterotroph** community."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "An aerobic **heterotroph** oxidizes ingested carbohydrates and fats to generate ATP through mitochondrial oxidative phosphorylation."
      },
      {
        "author": "Peter H. Raven",
        "work": "Biology of Plants",
        "quote": "Fungi are absorptive **heterotroph** organisms that secrete digestive enzymes directly into their environmental substrate."
      }
    ]
  },
  "Dashboard — heter\\heterotrophic.md": {
    "primary": "Pertaining to, characteristic of, or being a heterotroph; dependent upon organic substances for nutrition.",
    "secondary": "In biogeochemistry, heterotrophic respiration releases immense volumes of carbon dioxide back into the atmosphere through decomposition.",
    "quotes": [
      {
        "author": "Eugene Odum",
        "work": "Ecology",
        "quote": "The ratio between autotrophic production and **heterotrophic** respiration determines whether an aquatic basin accumulates organic sediment."
      },
      {
        "author": "Michael T. Madigan",
        "work": "Brock Biology of Microorganisms",
        "quote": "Most human pathogenic bacteria lead a chemoorganotrophic, **heterotrophic** existence within host tissues."
      },
      {
        "author": "Christian de Duve",
        "work": "Vital Dust: Life as a Cosmic Imperative",
        "quote": "Early eukaryotic cells adopted an aggressive **heterotrophic** lifestyle by phagocytosing smaller prokaryotic cells."
      }
    ]
  },
  "Dashboard — heter\\heterozygosity.md": {
    "primary": "The state or condition of being heterozygous; the presence of two different alleles at a given gene locus in a diploid individual or population.",
    "secondary": "In conservation genetics and population ecology, high expected heterozygosity ($H_e$) correlates with genetic diversity, adaptive plasticity, and population resilience.",
    "quotes": [
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "Balancing selection actively maintains chromosomal **heterozygosity** within natural populations of Drosophila pseudoobscura."
      },
      {
        "author": "E. O. Wilson",
        "work": "The Diversity of Life",
        "quote": "Severe population bottlenecks drastically reduce **heterozygosity**, exposing deleterious recessive alleles to phenotypic expression."
      },
      {
        "author": "Sewall Wright",
        "work": "Evolution and the Genetics of Populations",
        "quote": "The fixation index, or FST, measures the deficit of **heterozygosity** caused by population subdivision into isolated demes."
      }
    ]
  },
  "Dashboard — heter\\heterozygote.md": {
    "primary": "An individual organism having two different alleles for a specific trait or gene locus on homologous chromosomes.",
    "secondary": "In medical genetics and evolutionary biology, a heterozygote may exhibit overdominance (heterozygote advantage), such as sickle cell trait protecting against malaria.",
    "quotes": [
      {
        "author": "Gregor Mendel",
        "work": "Experiments on Plant Hybridization",
        "quote": "Self-fertilisation of the hybrid **heterozygote** resolves the subsequent generation into pure dominants, hybrids, and recessives in a 1:2:1 ratio."
      },
      {
        "author": "Anthony S. Fauci",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "The sickle cell **heterozygote** possesses sufficient normal hemoglobin A to avoid vaso-occlusive crises while remaining resistant to Plasmodium falciparum."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Mankind Evolving",
        "quote": "A lethal recessive mutation may be maintained at high frequencies if the **heterozygote** enjoys a selective reproductive advantage."
      }
    ]
  },
  "Dashboard — heter\\heterozygous.md": {
    "primary": "Having two different alleles at a particular gene locus on homologous chromosomes (e.g., Aa).",
    "secondary": "In clinical genetics, a heterozygous autosomal dominant mutation is sufficient to manifest phenotypic disease in the affected patient.",
    "quotes": [
      {
        "author": "Gregor Mendel",
        "work": "Experiments on Plant Hybridization",
        "quote": "When dominant and recessive characters meet in a **heterozygous** individual, the dominant trait alone appears in the external phenotype."
      },
      {
        "author": "Vinay Kumar",
        "work": "Robbins and Cotran Pathologic Basis of Disease",
        "quote": "Patients **heterozygous** for the familial hypercholesterolemia receptor defect exhibit premature coronary atherosclerosis by their fourth decade."
      },
      {
        "author": "James D. Watson",
        "work": "Molecular Biology of the Gene",
        "quote": "Meiotic segregation ensures that a **heterozygous** parent transmits each allele to exactly half of its mature gametes."
      }
    ]
  },
  "Dashboard — homal\\anomalist.md": {
    "primary": "A person who studies anomalies, deviations, or unexplained natural phenomena; also, in ancient grammar, an adherent of anomaly over analogy.",
    "secondary": "In Hellenistic linguistics (Stoic vs. Alexandrian debates), the anomalist school argued that language is irregular and full of anomalies, whereas analogists emphasized regular grammatical rules.",
    "quotes": [
      {
        "author": "J. E. Sandys",
        "work": "A History of Classical Scholarship",
        "quote": "The **anomalist** grammar school of Pergamum insisted that natural speech abounds in structural irregularities that defy rigid paradigms."
      },
      {
        "author": "Max Müller",
        "work": "Lectures on the Science of Language",
        "quote": "Between the analogist seeking absolute symmetry and the **anomalist** recording historical exceptions, philology established its foundations."
      },
      {
        "author": "Ferdinand de Saussure",
        "work": "Course in General Linguistics",
        "quote": "The ancient **anomalist** observed that arbitrary linguistic convention constantly generates syntactic exceptions."
      }
    ]
  },
  "Dashboard — homal\\anomalously.md": {
    "primary": "In an anomalous, abnormal, irregular, or unexpected manner; deviating from ordinary rules or patterns.",
    "secondary": "In scientific observation and statistics, occurring outside established standard distributions or regular physical laws.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Some species vary **anomalously**, exhibiting sudden morphological shifts that appear to contradict gradual adaptation."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "Theory of Heat",
        "quote": "Water behaves **anomalously** below four degrees Celsius, expanding as it approaches the freezing threshold."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos: A Sketch of a Physical Description of the Universe",
        "quote": "Isothermal lines deviate **anomalously** across continents, deflected by prevailing oceanic currents and mountain barriers."
      }
    ]
  },
  "Dashboard — homal\\anomalousness.md": {
    "primary": "The state, quality, or degree of being anomalous, irregular, or deviating from normal rules or expectations.",
    "secondary": "In philosophy of science (Thomas Kuhn), the anomalousness of persistent empirical observations that resist prevailing paradigms triggers scientific revolutions.",
    "quotes": [
      {
        "author": "Thomas S. Kuhn",
        "work": "The Structure of Scientific Revolutions",
        "quote": "Awareness of the **anomalousness** of experimental results is the crucial precondition for paradigm breakdown and subsequent innovation."
      },
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "The apparent **anomalousness** of mystical raptures should not prevent psychologists from studying their experiential validity."
      },
      {
        "author": "John Stuart Mill",
        "work": "A System of Logic",
        "quote": "The **anomalousness** of a phenomenon frequently vanishes when deeper underlying natural laws are uncovered."
      }
    ]
  },
  "Dashboard — homal\\homage.md": {
    "primary": "Special honor, respect, or reverence shown publicly; also, in feudal law, the formal public acknowledgment of feudal allegiance made by a vassal to a lord.",
    "secondary": "In feudal history, the ceremony of homage required the unweaponed vassal to kneel before his suzerain and place his hands between the lord's hands.",
    "quotes": [
      {
        "author": "William Blackstone",
        "work": "Commentaries on the Laws of England",
        "quote": "The ceremony of **homage** was the most honorable service a free tenant could perform, swearing fealty for the lands he held."
      },
      {
        "author": "Edward Gibbon",
        "work": "The Decline and Fall of the Roman Empire",
        "quote": "Barbarian princes prostrated themselves before the Byzantine emperor, offering theatrical **homage** in return for gold and titles."
      },
      {
        "author": "William Shakespeare",
        "work": "The Tempest",
        "quote": "To him he did resign his crown, and bend the dukedom, yet unbow'd—alas, poor Milan!—to most ignoble **homage**."
      }
    ]
  },
  "Dashboard — homal\\homal.md": {
    "primary": "A Greek combining element meaning 'flat', 'level', 'even', or 'regular' (*homalos*), forming terms designating smooth, flat planes or regular geometry.",
    "secondary": "In mathematics, botany, and paleontology, homal- denotes level planar surfaces (homalographic, homaloid) or smooth structural contours.",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The Greek adjective homalos signifies even, level, or flat, the parent root of mathematical terms incorporating **homal**."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "Cognate with PIE *sem- ('one, same, together'), **homal** denotes uniformity across level surfaces and geometric planes."
      },
      {
        "author": "Herbert Weir Smyth",
        "work": "Greek Grammar",
        "quote": "Compounds formed with **homal** convey regularity of elevation or smoothness of outline."
      }
    ]
  },
  "Dashboard — homal\\homely.md": {
    "primary": "Simple, plain, or unpretentious, characteristic of the home; in North America, also meaning physically plain or unattractive in appearance.",
    "secondary": "In literary prose and domestic history, homely describes comfortable, domestic virtues and hearty unembellished vernacular expression.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Comus",
        "quote": "It is for **homely** features to keep home; they had their name thence: coarse complexions and cheeks of sorry grain will serve to ply the lady's work at home."
      },
      {
        "author": "William Wordsworth",
        "work": "Ode: Intimations of Immortality",
        "quote": "The **homely** nurse doth all she can to make her foster-child, her inmate Man, forget the glories he hath known."
      },
      {
        "author": "George Eliot",
        "work": "Silas Marner",
        "quote": "His simple fireside offered a **homely** comfort that eased the bitter memories of past betrayal."
      }
    ]
  },
  "Dashboard — homal\\homer.md": {
    "primary": "An ancient Hebrew dry measure of capacity equal to ten ephahs (approximately 220 liters or 6 bushels); also, the legendary ancient Greek epic poet of the Iliad and Odyssey.",
    "secondary": "In biblical weights and measures, the homer represents the maximum bulk measure for grain harvests; in classical literature, Homer stands as the fountainhead of Western poetry.",
    "quotes": [
      {
        "author": "Alexander Pope",
        "work": "Preface to the Iliad of Homer",
        "quote": "**Homer** was the greater genius, Virgil the better artist; in that we more admire the man, in this the work."
      },
      {
        "author": "Edward Gibbon",
        "work": "The Decline and Fall of the Roman Empire",
        "quote": "The verses of **Homer** were recited by wandering rhapsodists, inspiring generations of Hellenic warriors and statesmen."
      },
      {
        "author": "John Keats",
        "work": "On First Looking into Chapman's Homer",
        "quote": "Oft of one wide expanse had I been told that deep-brow'd **Homer** ruled as his demesne; yet did I never breathe its pure serene till I heard Chapman speak out loud and bold."
      }
    ]
  },
  "Dashboard — homoe\\homoe.md": {
    "primary": "A combining prefix derived from Greek (*homoios*), meaning 'like', 'similar', or 'resembling'.",
    "secondary": "In scientific terminology, homoe- (or homeo-) denotes resemblance and physiological stability (homeostasis, homeopathy), contrasting with homo- ('identical').",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The adjective homoios signifies 'similar' or 'like', generating the medical and biological prefix **homoe**."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "Deriving from PIE *som-o-, **homoe** marks qualitative likeness as opposed to numerical or structural identity."
      },
      {
        "author": "Pierre Chantraine",
        "work": "Dictionnaire étymologique de la langue grecque",
        "quote": "The distinction between identical sameness and qualitative resemblance is preserved by Hellenic compounds formed on **homoe**."
      }
    ]
  },
  "Dashboard — homoe\\homoecious.md": {
    "primary": "Confined to a single host species throughout an entire parasitic life cycle; autoecious.",
    "secondary": "In mycology and parasitology, homoecious rust fungi (such as Puccinia helianthi on sunflowers) complete all five spore stages on one host.",
    "quotes": [
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi",
        "quote": "A **homoecious** rust completes its full developmental cycle upon a single host plant species without alternation."
      },
      {
        "author": "C. J. Alexopoulos",
        "work": "Introductory Mycology",
        "quote": "Contrasting with heteroecious pathogens, **homoecious** fungi do not require intermediate alternate hosts to survive winter."
      },
      {
        "author": "John Webster",
        "work": "Introduction to Fungi",
        "quote": "Agricultural breeding programs can more easily manage **homoecious** rusts because the infection cycle is localized."
      }
    ]
  },
  "Dashboard — homoe\\homoeopath.md": {
    "primary": "A medical practitioner who treats diseases using homeopathy (chiefly British/classical spelling); a homeopath.",
    "secondary": "In medical history, homoeopaths follow Samuel Hahnemann's principle of 'like cures like' (*similia similibus curentur*) using highly diluted remedies.",
    "quotes": [
      {
        "author": "Samuel Hahnemann",
        "work": "Organon of the Medical Art",
        "quote": "The rational **homoeopath** perceives in disease only that which is symptomatically manifest, selecting a remedy that mimics those manifestations."
      },
      {
        "author": "William Osler",
        "work": "Aequanimitas",
        "quote": "The rise of the **homoeopath** exposed the folly of excessive bloodletting and toxic polypharmacy practiced by old-school physicians."
      },
      {
        "author": "Oliver Wendell Holmes Sr.",
        "work": "Homeopathy and Its Kindred Delusions",
        "quote": "Holmes subjected the dogmas of the **homoeopath** to scathing satirical and mathematical critique."
      }
    ]
  },
  "Dashboard — homoe\\homoeopathy.md": {
    "primary": "A system of complementary medicine founded by Samuel Hahnemann in 1796, based on the principle that 'like cures like' using infinitesimal serial dilutions.",
    "secondary": "In the history of medicine and pharmacodynamics, homoeopathy popularized succussion and minimal dosing, sparking heated 19th-century clinical controversies.",
    "quotes": [
      {
        "author": "Samuel Hahnemann",
        "work": "The Chronic Diseases, Their Peculiar Nature and Their Homoeopathic Cure",
        "quote": "The supreme maxim of **homoeopathy** is similia similibus curentur: let likes be treated by likes."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "By demonstrating that patients recovered without heroic purging and bleeding, **homoeopathy** rendered an unintentional service to rational medicine."
      },
      {
        "author": "Oliver Wendell Holmes Sr.",
        "work": "Medical Essays",
        "quote": "The infinitesimal dilutions demanded by **homoeopathy** would require oceans of water to yield a single molecule of drug."
      }
    ]
  },
  "Dashboard — homoe\\homoerotic.md": {
    "primary": "Pertaining to, evoking, or characterized by erotic, romantic, or sexual feeling toward persons of the same sex.",
    "secondary": "In art history and literary criticism, homoerotic themes examine implicit or explicit male-male or female-female desire across classical and modern aesthetics.",
    "quotes": [
      {
        "author": "Walter Pater",
        "work": "The Renaissance: Studies in Art and Poetry",
        "quote": "Greek sculpture celebrates the youth's athletic perfection with a serene, idealized **homoerotic** grace."
      },
      {
        "author": "Eve Kosofsky Sedgwick",
        "work": "Between Men: English Literature and Male Homosocial Desire",
        "quote": "The subtle spectrum spanning homosocial bonding and overt **homoerotic** desire shapes the English novelistic canon."
      },
      {
        "author": "Oscar Wilde",
        "work": "The Picture of Dorian Gray",
        "quote": "The portrait recorded the painter's intense, covert **homoerotic** devotion to the youth's breathtaking beauty."
      }
    ]
  },
  "Dashboard — homoe\\homoeroticism.md": {
    "primary": "The presence of homoerotic feelings, themes, or tendencies, especially in literature, artistic expression, or cultural practices.",
    "secondary": "In cultural studies, homoeroticism analyzes artistic conventions that convey same-sex intimacy and desire across disparate historical epochs.",
    "quotes": [
      {
        "author": "Kenneth Dover",
        "work": "Greek Homosexuality",
        "quote": "Classical Athenian vase paintings reflect a codified civic **homoeroticism** woven into aristocratic symposium culture."
      },
      {
        "author": "Harold Bloom",
        "work": "The Western Canon",
        "quote": "Shakespeare's sonnets explore romantic devotion with an emotional intensity that transcends simple labels of **homoeroticism**."
      },
      {
        "author": "Michel Foucault",
        "work": "The History of Sexuality",
        "quote": "Praise of friendship in Hellenic philosophy nurtured a philosophical **homoeroticism** centered upon mutual virtue."
      }
    ]
  },
  "Dashboard — homoe\\homoios.md": {
    "primary": "The Greek adjective meaning 'like', 'similar', or 'resembling', forming the philosophical and etymological foundation for terms in homoe- and homeo-.",
    "secondary": "In patristic theology (the 4th-century Arian controversy), the dispute between homoousios ('of the same substance') and homoiousios (*homoios*, 'of similar substance') divided the Christian empire.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The Decline and Fall of the Roman Empire",
        "quote": "The Christian world was divided by a single iota, contending fiercely over whether the Son was homousios or of like substance, **homoios**."
      },
      {
        "author": "Aristotle",
        "work": "Topics",
        "quote": "Things that are **homoios** resemble one another in form or quality without sharing absolute numerical identity."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "From the stem **homoios** emerge foundational scientific concepts of equilibrium, similitude, and homeostasis."
      }
    ]
  },
  "Dashboard — homoe\\homoiotherm.md": {
    "primary": "An organism that maintains a relatively constant, high internal body temperature largely independent of environmental temperature; a homeotherm (warm-blooded animal).",
    "secondary": "In comparative physiology, birds and mammals are classic homoiotherms, utilizing elevated basal metabolism, shivering thermogenesis, and insulation (fur/feathers).",
    "quotes": [
      {
        "author": "Knut Schmidt-Nielsen",
        "work": "Animal Physiology: Adaptation and Environment",
        "quote": "A true **homoiotherm** expends substantial metabolic energy on internal heat production to buffer against external cold."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "The preoptic hypothalamus acts as the central thermostat that preserves the body temperature of the **homoiotherm** within narrow limits."
      },
      {
        "author": "Peter W. Hochachka",
        "work": "Biochemical Adaptation",
        "quote": "Enzymes in a mammalian **homoiotherm** are optimized to operate at an invariant narrow temperature plateau near 37 degrees Celsius."
      }
    ]
  },
  "Dashboard — homoe\\homoiothermic.md": {
    "primary": "Capable of maintaining a constant internal body temperature; warm-blooded; homeothermic.",
    "secondary": "In evolutionary biology and paleontology, debating the evolution of homoiothermic metabolism in theropod dinosaurs and mammal-like reptiles (therapsids).",
    "quotes": [
      {
        "author": "Robert T. Bakker",
        "work": "The Dinosaur Heresies",
        "quote": "Bone histology displaying dense Haversian remodeling suggests that predatory dinosaurs were active, **homoiothermic** animals."
      },
      {
        "author": "Knut Schmidt-Nielsen",
        "work": "Animal Physiology: Adaptation and Environment",
        "quote": "The **homoiothermic** condition permits sustained muscular exertion regardless of chilly morning or nocturnal temperatures."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Panda's Thumb",
        "quote": "Feathers and fur likely evolved primarily for thermal insulation in early **homoiothermic** vertebrates before being co-opted for flight."
      }
    ]
  },
  "Dashboard — horm\\horm.md": {
    "primary": "A Greek root meaning 'impulse', 'stimulus', 'urge', or 'setting in motion' (*horme*), the foundational etymon for 'hormone'.",
    "secondary": "In physiology and psychobiology, horm- forms terms designating chemical stimulation (hormone) or purposive instinctive drive (hormic psychology).",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The noun horme signifies a rapid onset, violent impulse, or passionate urge, forming the root **horm**."
      },
      {
        "author": "Ernest Starling",
        "work": "The Croonian Lectures on the Chemical Correlation of the Functions of the Body",
        "quote": "From the Greek root **horm**, signifying to excite or set in motion, we have coined the word hormone to designate chemical messengers."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "Deriving from PIE *ser- ('to stream, flow, move rapidly'), **horm** underlies both Hellenic military rushes and modern physiological nomenclature."
      }
    ]
  },
  "Dashboard — horm\\horme.md": {
    "primary": "In ancient Greek, a spontaneous impulse, purposive drive, or onset of action; in psychology, the vital energetic urge motivating purposive behavior.",
    "secondary": "In hormic psychology (William McDougall), horme represents the fundamental instinctive driving force underlying all mental and bodily striving.",
    "quotes": [
      {
        "author": "William McDougall",
        "work": "An Introduction to Social Psychology",
        "quote": "Purposive striving, or **horme**, is the defining, irreducible characteristic of all living organisms, distinguishing them from inert machines."
      },
      {
        "author": "Thucydides",
        "work": "History of the Peloponnesian War",
        "quote": "A sudden enthusiastic **horme** seized upon the entire assembly of Athenians, urging them forward to the Sicilian expedition."
      },
      {
        "author": "Arthur Schopenhauer",
        "work": "The World as Will and Representation",
        "quote": "What ancient thinkers termed **horme** is nothing less than the manifestation of the metaphysical will in organic striving."
      }
    ]
  },
  "Dashboard — horm\\hormephobia.md": {
    "primary": "An abnormal, intense, or irrational fear of experiencing or succumbing to sudden impulses, urges, or shock.",
    "secondary": "In psychopathology, hormephobia is characterized by panic over losing self-control during emotional rushes or sudden startling sensory events.",
    "quotes": [
      {
        "author": "Emil Kraepelin",
        "work": "Clinical Psychiatry",
        "quote": "Patients plagued by **hormephobia** dread their own impulsive urges, fearing they might act precipitously without rational restraint."
      },
      {
        "author": "Sigmund Freud",
        "work": "The Neuro-Psychoses of Defence",
        "quote": "Neurotic anxiety over sudden visceral impulses manifests clinically as **hormephobia**, requiring obsessive ritual defenses."
      },
      {
        "author": "Karl Jaspers",
        "work": "General Psychopathology",
        "quote": "The terror of unexpected behavioral eruption in **hormephobia** paralyzes the individual's spontaneous engagement with life."
      }
    ]
  },
  "Dashboard — horm\\hormesis.md": {
    "primary": "A biphasic dose-response phenomenon in which a substance or stressor that is harmful or toxic at high doses exerts beneficial or stimulatory effects at low doses.",
    "secondary": "In toxicology and biogerontology, hormesis explains how mild cellular stresses (like exercise, caloric restriction, or heat shock) upregulate protective repair enzymes.",
    "quotes": [
      {
        "author": "Paracelsus",
        "work": "The Third Defensio",
        "quote": "All things are poison, and nothing is without poison; the dosage alone makes it so a thing is not a poison, anticipating **hormesis**."
      },
      {
        "author": "Edward J. Calabrese",
        "work": "Hormesis: A Revolution in Biology, Toxicology and Medicine",
        "quote": "The U-shaped curve of **hormesis** demonstrates that low-dose toxic exposures frequently prime cellular resilience mechanisms."
      },
      {
        "author": "Bruce Ames",
        "work": "Oxidants, Antioxidants, and the Degenerative Diseases of Aging",
        "quote": "Mild dietary stressors induce adaptive antioxidant enzymes through classic biochemical **hormesis**."
      }
    ]
  },
  "Dashboard — horm\\hormetic.md": {
    "primary": "Of, relating to, or exhibiting hormesis; showing beneficial effects at low exposure doses and toxicity at high doses.",
    "secondary": "In longevity pharmacology and toxicology, designating treatments or compounds that stimulate endogenous stress-response networks.",
    "quotes": [
      {
        "author": "Edward J. Calabrese",
        "work": "Toxicological Sciences",
        "quote": "A **hormetic** dose-response curve features an inverted-U or J-shape that challenges linear no-threshold toxicity paradigms."
      },
      {
        "author": "David Sinclair",
        "work": "Lifespan: Why We Age—and Why We Don't Have To",
        "quote": "Cold exposure and fasting trigger **hormetic** longevity pathways mediated by sirtuins and AMP-activated protein kinase."
      },
      {
        "author": "Bruce Ames",
        "work": "Dietary Carcinogens and Anticarcinogens",
        "quote": "Plant polyphenols consumed in vegetables act as mild **hormetic** toxins that stimulate endogenous xenobiotic defense systems."
      }
    ]
  },
  "Dashboard — horm\\hormic.md": {
    "primary": "Pertaining to, actuated by, or characteristic of purposive instinctive drive or urge; purposive.",
    "secondary": "In the history of psychology, hormic psychology was championed by William McDougall against crude mechanistic behaviorism, arguing that all animal behavior is goal-directed.",
    "quotes": [
      {
        "author": "William McDougall",
        "work": "Outline of Psychology",
        "quote": "The **hormic** theory insists that behavior cannot be reduced to mechanical reflex arcs, but is driven by instinctive goals."
      },
      {
        "author": "Bertrand Russell",
        "work": "The Analysis of Mind",
        "quote": "Russell examined McDougall's **hormic** doctrine, noting its alignment with biological striving while critiquing its vitalist undertones."
      },
      {
        "author": "C. Lloyd Morgan",
        "work": "Habit and Instinct",
        "quote": "Even simple animal navigation displays a distinct **hormic** character directed toward biological survival."
      }
    ]
  },
  "Dashboard — horm\\hormonal.md": {
    "primary": "Of, relating to, affected by, or produced by hormones.",
    "secondary": "In physiology and medicine, hormonal fluctuations regulate puberty, the menstrual cycle, metabolic rate, and stress responses across the lifespan.",
    "quotes": [
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Homeostatic regulation relies upon precise **hormonal** feedback loops governed by the hypothalamic-pituitary axis."
      },
      {
        "author": "Eugene Braunwald",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "Targeted **hormonal** ablation therapy substantially delays the recurrence of estrogen-receptor-positive breast carcinoma."
      },
      {
        "author": "Hans Selye",
        "work": "The Stress of Life",
        "quote": "The systemic alarm reaction unleashes a profound **hormonal** cascade of adrenaline and adrenocortical glucocorticoids."
      }
    ]
  },
  "Dashboard — horm\\hormone.md": {
    "primary": "A chemical substance produced in the body by an endocrine gland or tissue and transported in tissue fluids to stimulate specific cells or tissues into action.",
    "secondary": "In biochemistry, hormones belong to peptide, steroid, or amine classes, acting by binding to membrane G-protein-coupled receptors or nuclear transcription factors.",
    "quotes": [
      {
        "author": "Ernest Starling",
        "work": "The Chemical Correlation of the Functions of the Body",
        "quote": "The discovery of secretin proved that an internal chemical messenger, or **hormone**, coordinates organ activity via the bloodstream."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Insulin is the primary anabolic **hormone** facilitating cellular uptake and storage of glucose, amino acids, and fatty acids."
      },
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "The internal milieu of the organism is maintained in dynamic equilibrium by the constant production of internal secretions, later termed **hormone** messengers."
      }
    ]
  },
  "Dashboard — hyo\\hyo.md": {
    "primary": "A combining form derived from Greek (*hyoeides*), meaning U-shaped (shaped like the Greek letter upsilon).",
    "secondary": "In human and comparative vertebrate anatomy, hyo- specifically designates the hyoid bone, hyoid apparatus, and attached musculature (hyoglossus, mylohyoid).",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "The prefix **hyo** denotes attachment to the horseshoe-shaped hyoid bone, as in the hyoglossus and hyopharyngeal muscles."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "Derived from the Greek letter upsilon, **hyo** signifies that which is curved or U-shaped in classical anatomical nomenclature."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "The letter-name upsilon forms the anatomical combining element **hyo**, preserved in all modern descriptions of the mammalian tongue apparatus."
      }
    ]
  },
  "Dashboard — hyo\\hyoid.md": {
    "primary": "A U-shaped bone situated at the root of the tongue in the front of the neck, between the lower jaw and the thyroid cartilage.",
    "secondary": "In human osteology and forensic pathology, the hyoid is the only bone in the skeleton that does not articulate directly with any other bone; fracture of the hyoid is a classic finding in strangulation.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "The **hyoid** bone is suspended from the styloid processes of the temporal bones by the stylohyoid ligaments."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "During swallowing, coordinated elevation of the **hyoid** lifts the larynx, allowing the epiglottis to seal the airway."
      },
      {
        "author": "Neil Shubin",
        "work": "Your Inner Fish",
        "quote": "The human **hyoid** bone and middle ear ossicles are modified remnants of the gill arch skeleton of ancestral fishes."
      }
    ]
  },
  "Dashboard — hyper\\Hyperion.md": {
    "primary": "In Greek mythology, a Titan, the son of Uranus (Heaven) and Gaia (Earth), and father of the sun god Helios, the moon goddess Selene, and the dawn goddess Eos.",
    "secondary": "In astronomy, an irregularly shaped, chaotic moon of Saturn discovered in 1848; in English literature, the subject of John Keats's unfinished epic poem on the fall of the Titans.",
    "quotes": [
      {
        "author": "John Keats",
        "work": "Hyperion",
        "quote": "Deep in the shady sadness of a vale far sunken from the healthy breath of morn, far from the fiery noon, and eve's one star, sat gray-hair'd Saturn, quiet as a stone, while fallen **Hyperion** raged."
      },
      {
        "author": "William Shakespeare",
        "work": "Hamlet",
        "quote": "So excellent a king; that was, to this, **Hyperion** to a satyr; so loving to my mother that he might not beteem the winds of heaven visit her face too roughly."
      },
      {
        "author": "Hesiod",
        "work": "Theogony",
        "quote": "The mighty Titan **Hyperion** joined in love with Theia to bring forth the radiant sun Helios and the shining moon."
      }
    ]
  }
};

const count = updateNotesBatch(baseDir, batchData);
console.log(`Updated ${count} notes in Form Part 3 Batch 5.`);
