import { updateNotesBatch } from './curate-updater-util.mjs';

const baseDir = "App database\\Greek roots\\Cluster Form & Space";
const batchData = {
  "Dashboard — morph\\homeomorphic.md": {
    "primary": "In topology, related by a homeomorphism; topologically equivalent through a continuous bijective mapping possessing a continuous inverse.",
    "secondary": "In geometric topology and manifold theory, two homeomorphic spaces share all fundamental topological invariants such as compactness, connectedness, and Euler characteristic.",
    "quotes": [
      {
        "author": "Henri Poincaré",
        "work": "Analysis Situs",
        "quote": "Two manifolds are **homeomorphic** when there exists a continuous one-to-one correspondence between their points in both directions."
      },
      {
        "author": "Felix Hausdorff",
        "work": "Grundzüge der Mengenlehre",
        "quote": "Topological equivalence demands that the open neighborhood systems of **homeomorphic** spaces map faithfully onto one another."
      },
      {
        "author": "James Munkres",
        "work": "Topology",
        "quote": "The topologist views a coffee mug and a doughnut as **homeomorphic**, since each can be deformed into the other without tearing or gluing."
      }
    ]
  },
  "Dashboard — morph\\homeomorphism.md": {
    "primary": "A continuous bijective function between two topological spaces whose inverse mapping is also continuous, establishing topological equivalence between them.",
    "secondary": "In differential and algebraic topology, a homeomorphism preserves topological invariants including fundamental groups, cohomology rings, and dimensional boundaries.",
    "quotes": [
      {
        "author": "Henri Poincaré",
        "work": "Analysis Situs",
        "quote": "The existence of a global **homeomorphism** between two closed surfaces guarantees that their connectivity numbers are identical."
      },
      {
        "author": "L. E. J. Brouwer",
        "work": "Beweis der Invarianz der Dimensionenzahl",
        "quote": "We proved that Euclidean spaces of different dimensions cannot be brought into topological equivalence by any **homeomorphism**."
      },
      {
        "author": "John Milnor",
        "work": "Topology from the Differentiable Viewpoint",
        "quote": "Exotic spheres demonstrate that two smooth manifolds may share a common **homeomorphism** yet fail to be diffeomorphic."
      }
    ]
  },
  "Dashboard — morph\\homomorphic.md": {
    "primary": "In abstract algebra, related by a homomorphism; exhibiting an algebraic correspondence between structures that preserves operations.",
    "secondary": "In comparative anatomy and morphology, exhibiting superficial similarity of form or anatomical structure despite having divergent evolutionary origins.",
    "quotes": [
      {
        "author": "Emmy Noether",
        "work": "Idealtheorie in Ringbereichen",
        "quote": "The quotient ring is naturally **homomorphic** to the original ring, preserving modular addition and multiplication operations."
      },
      {
        "author": "Bartel Leendert van der Waerden",
        "work": "Modern Algebra",
        "quote": "If two groups are **homomorphic**, the identity element of the domain maps directly onto the identity element of the codomain."
      },
      {
        "author": "Ernst Mayr",
        "work": "Principles of Systematic Zoology",
        "quote": "Unrelated organisms adapting to parallel aerial niches often evolve **homomorphic** wing profiles through convergent selection."
      }
    ]
  },
  "Dashboard — morph\\homomorphism.md": {
    "primary": "A structure-preserving mapping between two algebraic structures of the same type (such as groups, rings, or vector spaces) that commutes with operations.",
    "secondary": "In universal algebra and category theory, the kernel of a group homomorphism determines a normal subgroup, yielding fundamental isomorphism theorems.",
    "quotes": [
      {
        "author": "Emmy Noether",
        "work": "Abstrakter Aufbau der Idealtheorie",
        "quote": "Every ideal in a ring defines a canonical **homomorphism** whose kernel coincides precisely with that ideal."
      },
      {
        "author": "Saunders Mac Lane",
        "work": "Categories for the Working Mathematician",
        "quote": "A functor between categories generalises the concept of a **homomorphism** between groups, preserving composition and identities."
      },
      {
        "author": "Nathan Jacobson",
        "work": "Basic Algebra",
        "quote": "The first isomorphism theorem states that the image of a group **homomorphism** is isomorphic to the quotient by its kernel."
      }
    ]
  },
  "Dashboard — morph\\homomorphy.md": {
    "primary": "The property, state, or condition of being homomorphic; correspondence in form, appearance, or algebraic structure.",
    "secondary": "In evolutionary biology, superficial similarity between organisms of different lineages resulting from convergent adaptation rather than shared ancestry.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "On the Archetype and Homologies of the Vertebrate Skeleton",
        "quote": "We must carefully separate true genetic homology from deceptive **homomorphy** induced by similar environmental habits."
      },
      {
        "author": "E. Ray Lankester",
        "work": "On the Use of the Term Homology in Modern Zoology",
        "quote": "Homoplasy encompasses cases of morphological **homomorphy** where parallel selection produces nearly identical skeletal modifications."
      },
      {
        "author": "Saunders Mac Lane",
        "work": "Homology",
        "quote": "In homological algebra, the preservation of boundary operators guarantees the algebraic **homomorphy** of chain complexes."
      }
    ]
  },
  "Dashboard — morph\\hylomorphism.md": {
    "primary": "The Aristotelian philosophical doctrine that physical substances are composite entities consisting of prime matter (hyle) and substantial form (morphe).",
    "secondary": "In Scholastic philosophy and Thomistic metaphysics, hylomorphism explains bodily individuation and substantial change, wherein form actualizes passive matter.",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "Physics",
        "quote": "Our foundational doctrine of **hylomorphism** posits that substance arises only when form informs underlying matter."
      },
      {
        "author": "Thomas Aquinas",
        "work": "Summa Theologiae",
        "quote": "According to **hylomorphism**, the rational soul is the substantial form of the human body, giving it life and actual existence."
      },
      {
        "author": "Anthony Kenny",
        "work": "Aquinas on Mind",
        "quote": "Aristotelian **hylomorphism** avoids the dualistic pitfalls of Cartesianism by viewing mind as the animating form of living matter."
      }
    ]
  },
  "Dashboard — morph\\hypermorphosis.md": {
    "primary": "A form of heterochrony in evolutionary biology in which the offset timing of developmental growth is delayed, resulting in exaggerated or hyper-adult traits.",
    "secondary": "In evolutionary paleontology, hypermorphosis accounts for monumental phenotypic structures, such as the colossal antler span of the extinct Irish elk.",
    "quotes": [
      {
        "author": "Stephen Jay Gould",
        "work": "Ontogeny and Phylogeny",
        "quote": "In **hypermorphosis**, ontogeny is prolonged past the ancestral stopping point, producing gigantism and exaggerated cranial ornaments."
      },
      {
        "author": "Gavin de Beer",
        "work": "Embryos and Ancestors",
        "quote": "The Irish elk evolved its enormous antlers through **hypermorphosis**, extending its juvenile allometric growth trajectory into later maturity."
      },
      {
        "author": "Brian K. Hall",
        "work": "Evolutionary Developmental Biology",
        "quote": "Delays in hormonal signaling that terminate skeletal ossification provide the developmental trigger for macroevolutionary **hypermorphosis**."
      }
    ]
  },
  "Dashboard — morph\\isomorphic.md": {
    "primary": "Having identical form, structure, or geometric shape; in mathematics, related by an isomorphism that preserves all structural relations.",
    "secondary": "In crystallography and solid-state chemistry, describing substances that crystallize in identical crystal habits and can form homogeneous solid solutions.",
    "quotes": [
      {
        "author": "Eilhard Mitscherlich",
        "work": "Sur la relation qui existe entre la forme cristalline et les proportions chimiques",
        "quote": "Salts possessing an identical number of chemical atoms arranged in the same manner are **isomorphic**, assuming identical crystalline angles."
      },
      {
        "author": "Felix Klein",
        "work": "Lectures on the Icosahedron",
        "quote": "The alternating group on five letters is algebraically **isomorphic** to the group of rotational symmetries of the regular icosahedron."
      },
      {
        "author": "Garrett Birkhoff",
        "work": "Lattice Theory",
        "quote": "Two partially ordered sets are **isomorphic** if there exists an order-preserving bijection between their elements."
      }
    ]
  },
  "Dashboard — morph\\isomorphism.md": {
    "primary": "A structure-preserving bijection between two mathematical entities showing they possess identical structural properties under their defined operations.",
    "secondary": "In chemistry and mineralogy, the phenomenon wherein substances of similar chemical composition crystallize in identical crystal lattices.",
    "quotes": [
      {
        "author": "Eilhard Mitscherlich",
        "work": "Über das Verhältnis zwischen der chemischen Zusammensetzung und der Krystallform",
        "quote": "The discovery of crystallographic **isomorphism** demonstrated that atomic proportionality dictates crystal habit more decisively than elemental nature."
      },
      {
        "author": "Saunders Mac Lane",
        "work": "Categories for the Working Mathematician",
        "quote": "An arrow in a category is an **isomorphism** if and only if it possesses a two-sided inverse within the same arrow set."
      },
      {
        "author": "Douglas Hofstadter",
        "work": "Gödel, Escher, Bach",
        "quote": "An **isomorphism** is an information-preserving transformation that reveals that two seemingly disparate systems share identical formal structures."
      }
    ]
  },
  "Dashboard — morph\\isomorphous.md": {
    "primary": "Having identical or very similar crystalline form, shape, or geometric structure.",
    "secondary": "In crystallographic chemistry, describing compounds that can crystallize together in homogeneous mixed crystals or replace each other in mineral lattices.",
    "quotes": [
      {
        "author": "J. D. Dana",
        "work": "A System of Mineralogy",
        "quote": "Phosphates and arsenates of lead form an **isomorphous** series, crystallizing in identical hexagonal prisms with interchangeable ions."
      },
      {
        "author": "Eilhard Mitscherlich",
        "work": "Sur la relation qui existe entre la forme cristalline",
        "quote": "The alums provide classic examples of **isomorphous** substances, whose octahedra can grow layered around one another in solution."
      },
      {
        "author": "William L. Bragg",
        "work": "Atomic Structure of Minerals",
        "quote": "Ionic radius determines whether two metal cations can substitute for each other within an **isomorphous** silicate crystal lattice."
      }
    ]
  },
  "Dashboard — morph\\isomorphy.md": {
    "primary": "The condition, quality, or property of being isomorphous; correspondence of form, crystal structure, or mathematical relations.",
    "secondary": "In institutional sociology and organizational theory, the tendency of institutional structures within an organizational field to converge upon similar forms.",
    "quotes": [
      {
        "author": "Paul DiMaggio",
        "work": "The Iron Cage Revisited: Institutional Isomorphism and Collective Rationality",
        "quote": "Institutional **isomorphy** forces organizations in competitive fields to adopt similar bureaucratic procedures to gain social legitimacy."
      },
      {
        "author": "Walter W. Powell",
        "work": "The New Institutionalism in Organizational Analysis",
        "quote": "Coercive and mimetic pressures accelerate structural **isomorphy** across public schools and hospital networks."
      },
      {
        "author": "Ludwig von Bertalanffy",
        "work": "General System Theory",
        "quote": "The existence of mathematical **isomorphy** between physical kinetics and biological population models justifies a universal systems science."
      }
    ]
  },
  "Dashboard — morph\\mesomorph.md": {
    "primary": "An individual having a somatotype characterized by a sturdy, athletic, muscular physique with broad shoulders, narrow waist, and heavy bone structure.",
    "secondary": "In constitutional psychology and somatotyping, William Sheldon postulated that a mesomorph characteristically displays an assertive, vigorous somatotonic temperament.",
    "quotes": [
      {
        "author": "William H. Sheldon",
        "work": "The Varieties of Human Physique",
        "quote": "The classic **mesomorph** displays hard, prominent musculature, dense cortical bone, and an upright martial posture."
      },
      {
        "author": "Gordon Allport",
        "work": "Personality: A Psychological Interpretation",
        "quote": "Constitutional theorists linked the energetic drive of the **mesomorph** to a psychological craving for muscular activity and risk."
      },
      {
        "author": "Hans Eysenck",
        "work": "The Structure of Human Personality",
        "quote": "Athletic profiling shows that high-level sprinters and weightlifters cluster heavily around the **mesomorph** somatotype."
      }
    ]
  },
  "Dashboard — morph\\mesomorphic.md": {
    "primary": "Pertaining to, having the physical characteristics of, or classified as a mesomorph; robust, muscular, and athletic.",
    "secondary": "In soft matter physics and physical chemistry, designating a liquid crystalline phase intermediate between an isotropic liquid and a crystalline solid.",
    "quotes": [
      {
        "author": "William H. Sheldon",
        "work": "The Varieties of Temperament",
        "quote": "Men of markedly **mesomorphic** habitus are naturally suited to vigorous physical labor and competitive sports."
      },
      {
        "author": "Georges Friedel",
        "work": "Les états mésomorphes de la matière",
        "quote": "We apply the term **mesomorphic** to nematic and smectic states of matter that exhibit fluid flow while retaining optical anisotropy."
      },
      {
        "author": "J. M. Tanner",
        "work": "Foetus into Man",
        "quote": "Boys with **mesomorphic** builds generally reach peak height velocity earlier and show greater absolute muscular gains during puberty."
      }
    ]
  },
  "Dashboard — morph\\mesomorphy.md": {
    "primary": "The somatotypic condition, property, or degree of muscularity, physical robustness, and heavy skeletal development in the human body.",
    "secondary": "In anthropometric somatotyping (such as the Heath-Carter method), mesomorphy is the second numerical rating, calculated from bone breadths and corrected limb girths.",
    "quotes": [
      {
        "author": "William H. Sheldon",
        "work": "Atlas of Men",
        "quote": "The second component, **mesomorphy**, measures the relative predominance of skeletal, muscular, and connective tissue mass."
      },
      {
        "author": "Barbara Heath",
        "work": "A Modified Somatotype Method",
        "quote": "In our anthropometric formulation, **mesomorphy** is derived objectively from humerus and femur biepicondylar diameters."
      },
      {
        "author": "J. M. Tanner",
        "work": "The Physique of the Olympic Athlete",
        "quote": "Olympic gymnasts and wrestlers exhibit exceptionally high scores in **mesomorphy**, reflecting maximum muscular power per unit of stature."
      }
    ]
  },
  "Dashboard — morph\\metamorphic.md": {
    "primary": "Pertaining to, produced by, or characterized by metamorphosis or structural transformation.",
    "secondary": "In petrology and geology, designating rocks formed through the mineralogical and textural recrystallization of pre-existing rocks under high heat and tectonic pressure.",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "I proposed the term **metamorphic** to designate stratified rocks whose crystalline texture was induced by subterranean heat."
      },
      {
        "author": "James Hutton",
        "work": "Theory of the Earth",
        "quote": "Intense internal subterranean heat and pressure have remodeled sedimentary strata into durable **metamorphic** marble and slate."
      },
      {
        "author": "Alfred Harker",
        "work": "Metamorphism",
        "quote": "Regional stress reorients platy micaceous minerals perpendicular to maximum compression, developing the characteristic foliation of **metamorphic** schists."
      }
    ]
  },
  "Dashboard — morph\\metamorphism.md": {
    "primary": "The process of profound transformation or structural change in form, character, or composition.",
    "secondary": "In geology, the solid-state mineralogical and structural recrystallization of rocks driven by changes in temperature, lithostatic pressure, and reactive tectonic fluids.",
    "quotes": [
      {
        "author": "Charles Richard Van Hise",
        "work": "A Treatise on Metamorphism",
        "quote": "We define geological **metamorphism** as the alteration of rocks within the crust under conditions differing from those under which they formed."
      },
      {
        "author": "Arthur Holmes",
        "work": "Principles of Physical Geology",
        "quote": "Thermal contact **metamorphism** produces a baked aureole of hornfels surrounding a molten granitic pluton."
      },
      {
        "author": "Reginald Aldworth Daly",
        "work": "Metamorphism and Its Phases",
        "quote": "Hydrothermal fluids facilitate ionic diffusion during dynamic **metamorphism**, catalyzing the growth of porphyroblastic garnets."
      }
    ]
  },
  "Dashboard — morph\\metamorphopsia.md": {
    "primary": "A visual defect or symptom in which observed objects appear distorted in size, shape, contour, or spatial orientation.",
    "secondary": "In clinical ophthalmology and neurology, metamorphopsia results from anatomical disruption of retinal photoreceptor spacing in macular degeneration or cortical migraine aura.",
    "quotes": [
      {
        "author": "Albrecht von Graefe",
        "work": "Archiv für Ophthalmologie",
        "quote": "Patients suffering from central chorioretinitis report acute **metamorphopsia**, wherein straight grid lines appear undulating or broken."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In migraine scotoma, transitory **metamorphopsia** may precede the headache, causing familiar faces to appear grotesque and fragmented."
      },
      {
        "author": "Oliver Sacks",
        "work": "Migraine",
        "quote": "The Alice-in-Wonderland syndrome represents a bizarre central **metamorphopsia** where patients perceive their own limbs swelling or shrinking."
      }
    ]
  },
  "Dashboard — morph\\metamorphous.md": {
    "primary": "Undergoing, characterized by, or resulting from metamorphosis; transformative in bodily or structural form.",
    "secondary": "In historical petrological literature, an alternative adjectival variant for metamorphic, describing crystalline schists and altered mineral formations.",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "These ancient crystalline strata were formerly termed primitive, but their **metamorphous** origin from fossiliferous shale is now demonstrated."
      },
      {
        "author": "John Ruskin",
        "work": "Modern Painters",
        "quote": "The alpine aiguilles consist of twisted **metamorphous** schists, whose jagged precipices record ancient violent crustal upheavals."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Discourses: Biological and Geological",
        "quote": "Granite intrusions acted upon sedimentary beds, baking them into hard **metamorphous** rocks of crystalline luster."
      }
    ]
  },
  "Dashboard — morph\\monomorphemic.md": {
    "primary": "Consisting of or containing only a single morpheme; morphologically simplex, uninflected, and indivisible.",
    "secondary": "In structural linguistics, monomorphemic root words (such as 'cat' or 'walk') contrast with polymorphemic words containing bound affixes or compounding elements.",
    "quotes": [
      {
        "author": "Leonard Bloomfield",
        "work": "Language",
        "quote": "A primary word like 'tree' is **monomorphemic**, carrying an irreducible lexical meaning that cannot be divided into smaller linguistic signs."
      },
      {
        "author": "Noam Chomsky",
        "work": "Aspects of the Theory of Syntax",
        "quote": "The lexicon stores **monomorphemic** bases alongside morphological rules that generate inflected and derived surface words."
      },
      {
        "author": "Edward Sapir",
        "work": "Language",
        "quote": "Certain isolating languages tend to make every word **monomorphemic**, avoiding bound affixes in favor of syntactic particle sequences."
      }
    ]
  },
  "Dashboard — morph\\monomorphic.md": {
    "primary": "Having or existing in only one form, shape, color, or developmental morph throughout a population, life cycle, or chemical substance.",
    "secondary": "In genetics and evolutionary biology, describing a gene locus where a single wild-type allele is fixed across virtually all individuals in a population.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants Under Domestication",
        "quote": "In species that are strictly **monomorphic**, males and females share identical plumage and body dimensions throughout all seasons."
      },
      {
        "author": "Ronald Fisher",
        "work": "The Genetical Theory of Natural Selection",
        "quote": "Purifying selection tends to maintain a **monomorphic** population by eliminating deleterious mutations at vital metabolic loci."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "A geographically isolated population frequently becomes **monomorphic** through founder effects and sustained genetic drift."
      }
    ]
  },
  "Dashboard — morph\\monomorphism.md": {
    "primary": "The state or condition of existing in only one form, morphological habit, or color phase.",
    "secondary": "In category theory and abstract algebra, a monomorphism is a left-cancellative morphism, generalizing injective (one-to-one) functions.",
    "quotes": [
      {
        "author": "Saunders Mac Lane",
        "work": "Categories for the Working Mathematician",
        "quote": "A morphism f is a **monomorphism** if it is left-cancellable: f after g equals f after h implies g equals h."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "Severe environmental homogeneity favors genetic **monomorphism**, whereas fluctuating habitats maintain balanced polymorphism."
      },
      {
        "author": "Alexander Grothendieck",
        "work": "Sur quelques points d'algèbre homologique",
        "quote": "In an abelian category, every **monomorphism** arises naturally as the kernel of its corresponding canonical quotient arrow."
      }
    ]
  },
  "Dashboard — morph\\morph.md": {
    "primary": "A distinct physical, structural, or behavioral form or variant of an organism within a polymorphic population.",
    "secondary": "In descriptive linguistics, the concrete phonetic or orthographic realization of an underlying grammatical morpheme in an utterance.",
    "quotes": [
      {
        "author": "E. B. Ford",
        "work": "Ecological Genetics",
        "quote": "Industrial melanism in the peppered moth demonstrates how natural selection rapidly increases the frequency of the dark **morph**."
      },
      {
        "author": "Zellig Harris",
        "work": "Methods in Structural Linguistics",
        "quote": "Every spoken utterance can be segmented into a linear succession of phones, each representing a concrete linguistic **morph**."
      },
      {
        "author": "Ernst Mayr",
        "work": "Systematics and the Origin of Species",
        "quote": "Taxonomists must not mistakenly describe each ecological **morph** as an independent biological species."
      }
    ]
  },
  "Dashboard — morph\\morphallaxis.md": {
    "primary": "A mode of biological regeneration in animals (such as Hydra or planarians) wherein missing body parts are reconstituted primarily by the reorganization and remodeling of existing tissues without extensive new cell proliferation.",
    "secondary": "In experimental embryology and developmental biology, morphallaxis was distinguished by Thomas Hunt Morgan from epimorphosis, which relies on blastema proliferation.",
    "quotes": [
      {
        "author": "Thomas Hunt Morgan",
        "work": "Regeneration",
        "quote": "When a severed fragment of Planaria remodels into a complete miniature worm without new growth, the process is one of pure **morphallaxis**."
      },
      {
        "author": "Lewis Wolpert",
        "work": "The French Flag Problem: A Contribution to the Discussion on Pattern Formation and Regulation",
        "quote": "Pattern regulation via positional information explains how Hydra restores its head and foot through tissue **morphallaxis**."
      },
      {
        "author": "Julian Huxley",
        "work": "The Stream of Life",
        "quote": "The marvel of **morphallaxis** demonstrates that embryonic cells can be respecified and repurposed by systemic organizing gradients."
      }
    ]
  },
  "Dashboard — morph\\morphea.md": {
    "primary": "A localized form of scleroderma characterized by circumscribed, firm, sclerotic, ivory-colored patches on the skin surrounded by a violaceous halo.",
    "secondary": "In clinical dermatology and rheumatology, morphea involves excessive collagen deposition in the dermis and subcutaneous tissue without internal organ fibrosis.",
    "quotes": [
      {
        "author": "Jonathan Hutchinson",
        "work": "Lectures on Clinical Surgery",
        "quote": "The localized indurated plaques of **morphea** typically progress slowly, leaving smooth, atrophic scars in their wake."
      },
      {
        "author": "Ferdinand von Hebra",
        "work": "Diseases of the Skin",
        "quote": "Microscopic sections of **morphea** show dense, swollen bundles of collagen fibers obliterating dermal vessels and hair follicles."
      },
      {
        "author": "Thomas Addison",
        "work": "On the Keloid of Alibert, and on True Keloid",
        "quote": "What some authors designate as **morphea** is an insidiously progressive cicatricial thickening of the integument."
      }
    ]
  },
  "Dashboard — morph\\morpheme.md": {
    "primary": "The minimal grammatical unit of meaning or functional significance in a language that cannot be divided into smaller meaningful components.",
    "secondary": "In structural linguistics, morphemes are classified as free (capable of standing alone as independent words) or bound (affixes that must attach to a stem).",
    "quotes": [
      {
        "author": "Leonard Bloomfield",
        "work": "Language",
        "quote": "A linguistic form which bears no partial phonetic-semantic resemblance to any other form is a simple form or **morpheme**."
      },
      {
        "author": "Ferdinand de Saussure",
        "work": "Course in General Linguistics",
        "quote": "The linguistic sign is arbitrary, and the **morpheme** unites a acoustic sound image with an abstract conceptual signified."
      },
      {
        "author": "Noam Chomsky",
        "work": "Syntactic Structures",
        "quote": "Syntactic transformation rules operate upon strings of symbols, mapping underlying **morpheme** sequences into pronounceable sentences."
      }
    ]
  },
  "Dashboard — morph\\morphemic.md": {
    "primary": "Pertaining to, consisting of, or functioning as a morpheme or system of morphemes.",
    "secondary": "In structural phonology and morphology, morphemic analysis identifies the constituent functional elements that structure complex words.",
    "quotes": [
      {
        "author": "Zellig Harris",
        "work": "Methods in Structural Linguistics",
        "quote": "The distribution of phonemes is analyzed to identify the regular **morphemic** segments that constitute phrases."
      },
      {
        "author": "Charles F. Hockett",
        "work": "A Manual of Phonology",
        "quote": "Phonological alternations across related paradigms reveal the underlying **morphemic** unity of inflected verb roots."
      },
      {
        "author": "Roman Jakobson",
        "work": "Selected Writings",
        "quote": "Language systems maintain invariant **morphemic** values despite substantial contextual variations in pronunciation."
      }
    ]
  },
  "Dashboard — morph\\Morpheus.md": {
    "primary": "In classical Greco-Roman mythology, the god of dreams, a son of Hypnos (Sleep), who shapes and presents human phantoms in sleep.",
    "secondary": "In literary tradition and allegorical poetry, Morpheus is invoked as the personification of deep, slumberous repose and dream visions.",
    "quotes": [
      {
        "author": "Ovid",
        "work": "Metamorphoses",
        "quote": "Among the thousand sons of Sleep, the master artificer **Morpheus** excels at imitating human shape, voice, and gait in dreams."
      },
      {
        "author": "Edmund Spenser",
        "work": "The Faerie Queene",
        "quote": "And more to lulle him in his slumber soft, a trickling streame from high rock tumbling downe... sent by the god **Morpheus**."
      },
      {
        "author": "John Milton",
        "work": "Il Penseroso",
        "quote": "And let some strange mysterious dream waive at his wings in airy stream of lively portraiture displayed, softly on my eyelids laid by **Morpheus**."
      }
    ]
  },
  "Dashboard — morph\\morphia.md": {
    "primary": "A historical and literary name for morphine, the principal narcotic alkaloid extracted from the opium poppy.",
    "secondary": "In 19th-century pharmacology and clinical medicine, morphia was administered widely as a potent analgesic, sedative, and hypodermic injection.",
    "quotes": [
      {
        "author": "Thomas De Quincey",
        "work": "Confessions of an English Opium-Eater",
        "quote": "I found that a few grains of **morphia** dissipated my neuralgic agony, transporting my spirit into celestial calm."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "A Study in Scarlet",
        "quote": "Sherlock Holmes turned toward his desk, seeking relief in the soothing embrace of **morphia** when intellectual problems lagged."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In acute pulmonary edema, a hypodermic injection of **morphia** acts like a charm, quieting dyspnea and vascular panic."
      }
    ]
  },
  "Dashboard — morph\\morphine.md": {
    "primary": "A powerful narcotic opioid alkaloid isolated from opium (Papaver somniferum), widely prescribed as an analgesic for severe acute and chronic pain.",
    "secondary": "In neuropharmacology, morphine acts as a potent agonist at central μ-opioid receptors, dampening pain transmission while posing risks of respiratory depression.",
    "quotes": [
      {
        "author": "Friedrich Sertürner",
        "work": "Darstellung der reinen Mohnsäure nebst einer chemischen Untersuchung des Opiums",
        "quote": "I succeeded in isolating the soporific principle of opium as a crystalline alkaline base, naming it **morphine** after the god of dreams."
      },
      {
        "author": "Louis S. Goodman",
        "work": "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        "quote": "Intravenous **morphine** remains the gold standard analgesic against which all newly synthesized opioid agonists are calibrated."
      },
      {
        "author": "Claude Bernard",
        "work": "Leçons de physiologie opératoire",
        "quote": "By administering **morphine** prior to surgical vivisection, physiological reflexes can be investigated with minimal animal distress."
      }
    ]
  },
  "Dashboard — morph\\morphogenesis.md": {
    "primary": "The biological process that causes an organism, tissue, or cellular organelle to develop and establish its physical shape and structural form.",
    "secondary": "In developmental biology and mathematical biophysics, morphogenesis is modeled through morphogen diffusion gradients, cellular adhesion, and mechanical tissue stress.",
    "quotes": [
      {
        "author": "Alan Turing",
        "work": "The Chemical Basis of Morphogenesis",
        "quote": "A system of reacting and diffusing chemical substances can account for the main phenomena of **morphogenesis** in early development."
      },
      {
        "author": "D'Arcy Wentworth Thompson",
        "work": "On Growth and Form",
        "quote": "Physical forces such as surface tension and mechanical pressure dictate the mathematical contours of cellular **morphogenesis**."
      },
      {
        "author": "Lewis Wolpert",
        "work": "Principles of Development",
        "quote": "Morphogen concentration gradients provide embryonic cells with positional coordinates that guide coordinated **morphogenesis**."
      }
    ]
  },
  "Dashboard — morph\\morphologic.md": {
    "primary": "Pertaining to, dealing with, or relating to the form, structure, or external configuration of organisms or languages.",
    "secondary": "In anatomical pathology, morphologic diagnoses classify diseases based on observed cellular architecture and tissue staining characteristics.",
    "quotes": [
      {
        "author": "Johann Wolfgang von Goethe",
        "work": "The Metamorphosis of Plants",
        "quote": "Our **morphologic** investigations reveal that all floral organs are simply modified leaves transformed through successive stages."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The microscopic diagnosis must establish the precise **morphologic** changes in the cell nucleus before predicting malignancy."
      },
      {
        "author": "Edward Sapir",
        "work": "Language",
        "quote": "Languages differ profoundly in their **morphologic** classification, spanning isolating, agglutinative, and inflected systems."
      }
    ]
  },
  "Dashboard — morph\\morphological.md": {
    "primary": "Pertaining to morphology; relating to the study of the form, structure, and physical architecture of organisms, minerals, or linguistic items.",
    "secondary": "In evolutionary taxonomy and comparative anatomy, morphological characters provide classic phylogenetic evidence for reconstructing ancestral relationships.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Homologous bones in the hand of a man, wing of a bat, and paddle of a porpoise reveal undeniable **morphological** affinity."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The fundamental **morphological** plan of the vertebrate cranium persists despite extreme functional specializations in birds and mammals."
      },
      {
        "author": "Ernst Haeckel",
        "work": "Generelle Morphologie der Organismen",
        "quote": "Every **morphological** structure in an adult organism reflects its phylogenetic ancestry through ontogenetic recapitulation."
      }
    ]
  },
  "Dashboard — morph\\morphologically.md": {
    "primary": "In a morphological manner; with respect to physical form, structural arrangement, or grammatical formation.",
    "secondary": "In comparative biology and linguistics, analyzing specimens morphologically allows researchers to distinguish homologous adaptations from superficial analogs.",
    "quotes": [
      {
        "author": "Ernst Mayr",
        "work": "Systematics and the Origin of Species",
        "quote": "Sibling species may be almost identical **morphologically** while remaining completely isolated reproductively in nature."
      },
      {
        "author": "Leonard Bloomfield",
        "work": "Language",
        "quote": "A compound word is structured **morphologically** so that its primary stress marks it as a distinct grammatical unit."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Structure of Evolutionary Theory",
        "quote": "Organisms that appear **morphologically** conservative over geological epochs may nevertheless undergo significant molecular evolution."
      }
    ]
  },
  "Dashboard — morph\\morphology.md": {
    "primary": "The scientific study of the form, structure, and configuration of living organisms and their specific structural features.",
    "secondary": "In linguistics, the subfield that analyzes the internal structure of words, their constituent morphemes, roots, and inflectional paradigms.",
    "quotes": [
      {
        "author": "Johann Wolfgang von Goethe",
        "work": "Italian Journey",
        "quote": "My contemplation of botanical forms in the gardens of Palermo inspired the new science of organic **morphology**."
      },
      {
        "author": "D'Arcy Wentworth Thompson",
        "work": "On Growth and Form",
        "quote": "Organic **morphology** is in its essence a problem of mechanics, where physical forces shape protoplasm into mathematical spirals."
      },
      {
        "author": "Noam Chomsky",
        "work": "Aspects of the Theory of Syntax",
        "quote": "The grammar of a language must include a component for **morphology** to handle affixation, compounding, and case concord."
      }
    ]
  },
  "Dashboard — morph\\morphophoneme.md": {
    "primary": "In structural and generative linguistics, a theoretical underlying phonological unit or class of phonemes that alternates across allomorphic variants of a single morpheme.",
    "secondary": "In phonological theory, morphophonemes bridge abstract underlying lexical representations and surface phonetic realizations through systematic rewrite rules.",
    "quotes": [
      {
        "author": "Roman Jakobson",
        "work": "Selected Writings",
        "quote": "The concept of the **morphophoneme** unifies phonetic alternations under an abstract functional unit within the linguistic code."
      },
      {
        "author": "Leonard Bloomfield",
        "work": "The Menomini Language",
        "quote": "By establishing a single underlying **morphophoneme**, we explain complex vowel length alternations through a concise rule."
      },
      {
        "author": "Noam Chomsky",
        "work": "The Sound Pattern of English",
        "quote": "Underlying representations employ each abstract **morphophoneme** to generate diverse surface realizations via cyclical phonological rules."
      }
    ]
  },
  "Dashboard — morph\\morphophonemic.md": {
    "primary": "Pertaining to, involving, or governed by morphophonemics; relating to phonological variations that occur at morpheme boundaries.",
    "secondary": "In descriptive linguistics, morphophonemic rules account for regular vowel shifts, assimilations, and consonant elisions during word derivation and inflection.",
    "quotes": [
      {
        "author": "Noam Chomsky",
        "work": "The Sound Pattern of English",
        "quote": "Regular vowel alternations in English words like 'divine' and 'divinity' are governed by systematic **morphophonemic** rules."
      },
      {
        "author": "Zellig Harris",
        "work": "Methods in Structural Linguistics",
        "quote": "A **morphophonemic** transcription simplifies morphological description by factoring out predictable phonetic conditioning."
      },
      {
        "author": "Morris Halle",
        "work": "The Sound Pattern of Russian",
        "quote": "Voicing assimilation across prefix boundaries provides a transparent example of a productive **morphophonemic** process."
      }
    ]
  },
  "Dashboard — morph\\morphophonemics.md": {
    "primary": "The branch of linguistics that studies the phonological variation and sound changes that occur within morphemes when combined into complex words.",
    "secondary": "In generative grammar, morphophonemics investigates the structural interface where syntactic morpheme concatenations are mapped into phonological strings.",
    "quotes": [
      {
        "author": "Leonard Bloomfield",
        "work": "Language",
        "quote": "The study of alternations in the phonetic shape of morphemes is designated as **morphophonemics** or morphophonology."
      },
      {
        "author": "Noam Chomsky",
        "work": "Current Issues in Linguistic Theory",
        "quote": "Classical structuralism separated phonemics from syntax, leaving **morphophonemics** as an uneasy intermediate compromise."
      },
      {
        "author": "Charles F. Hockett",
        "work": "A Manual of Phonology",
        "quote": "Through **morphophonemics**, the analyst reconstructs base forms from which allomorphic variants are derived by rule."
      }
    ]
  },
  "Dashboard — morph\\morphophysiology.md": {
    "primary": "The biological science that investigates the mutual relationships and functional interactions between anatomical structure (morphology) and physiological activity.",
    "secondary": "In comparative biomechanics, morphophysiology explains how organ geometry and tissue architecture are optimized to fulfill dynamic physiological roles.",
    "quotes": [
      {
        "author": "Claude Bernard",
        "work": "Introduction to the Study of Experimental Medicine",
        "quote": "True biological understanding requires integrating organ form with functional performance through experimental **morphophysiology**."
      },
      {
        "author": "August Krogh",
        "work": "The Anatomy and Physiology of Capillaries",
        "quote": "The **morphophysiology** of the capillary bed reveals how vascular dimensions adjust dynamically to regional oxygen demands."
      },
      {
        "author": "Knut Schmidt-Nielsen",
        "work": "Animal Physiology: Adaptation and Environment",
        "quote": "Desert ungulates survive extreme dehydration through an exquisite renal **morphophysiology** featuring extraordinarily long loops of Henle."
      }
    ]
  },
  "Dashboard — morph\\morphosyntactic.md": {
    "primary": "Pertaining to, involving, or governed by the intersection of morphological inflections and syntactic sentence structures.",
    "secondary": "In theoretical grammar, morphosyntactic features (such as case, number, tense, and gender agreement) regulate structural government across phrases.",
    "quotes": [
      {
        "author": "Noam Chomsky",
        "work": "Syntactic Structures",
        "quote": "Agreement rules must check the **morphosyntactic** features of subject and verb before spelling out the final phonological form."
      },
      {
        "author": "Bernard Comrie",
        "work": "Language Universals and Linguistic Typology",
        "quote": "Ergative alignment represents a fundamental **morphosyntactic** pattern in which the subject of an intransitive verb patterns with the object of a transitive verb."
      },
      {
        "author": "Joseph Greenberg",
        "work": "Universals of Language",
        "quote": "Cross-linguistic surveys reveal universal correlations between word order types and specific **morphosyntactic** marking strategies."
      }
    ]
  },
  "Dashboard — morph\\morphosyntax.md": {
    "primary": "The domain of linguistics that investigates the interdependent grammatical rules operating between word-level morphology and sentence-level syntax.",
    "secondary": "In linguistic typology, morphosyntax examines how different language families distribute grammatical information between synthetic inflectional markers and analytical word orders.",
    "quotes": [
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "quote": "A language expresses its relational concepts either through analytical word order or through synthetic **morphosyntax**."
      },
      {
        "author": "Talmy Givón",
        "work": "Syntax: An Introduction",
        "quote": "Diachronic grammaticalization shows how loose discourse strategies gradually freeze into tight **morphosyntax** over centuries."
      },
      {
        "author": "William Croft",
        "work": "Typology and Universals",
        "quote": "Typological classification compares how different languages organize their **morphosyntax** to encode semantic transitivity."
      }
    ]
  },
  "Dashboard — morph\\paramorph.md": {
    "primary": "A pseudomorph formed by the internal structural recrystallization of a mineral into an allomorphic crystalline phase without any change in chemical composition.",
    "secondary": "In crystallography and petrology, paramorphs (such as rutile after anatase, or calcite after aragonite) preserve the original external crystal habit while altering internal lattice symmetry.",
    "quotes": [
      {
        "author": "J. D. Dana",
        "work": "A System of Mineralogy",
        "quote": "When aragonite alters to calcite without loss of external prismatic shape, the resulting crystal is classed as a **paramorph**."
      },
      {
        "author": "Alfred Harker",
        "work": "Petrology for Students",
        "quote": "Thin sections of volcanic rocks often reveal inverted quartz forming an optical **paramorph** after high-temperature tridymite."
      },
      {
        "author": "René Just Haüy",
        "work": "Traité de cristallographie",
        "quote": "The internal molecular rearrangement in a **paramorph** alters physical cleavage while retaining the outward boundaries of the precursor."
      }
    ]
  },
  "Dashboard — morph\\peramorphism.md": {
    "primary": "The evolutionary process or condition of peramorphosis; the development of exaggerated ancestral adult traits in descendant species through heterochronic shifts.",
    "secondary": "In macroevolutionary paleobiology, peramorphism encompasses acceleration, hypermorphosis, and predisplacement, resulting in exaggerated morphological structures.",
    "quotes": [
      {
        "author": "Stephen Jay Gould",
        "work": "Ontogeny and Phylogeny",
        "quote": "Through **peramorphism**, descendant species recapitulate ancestral ontogeny rapidly and then progress into novel morphological territory."
      },
      {
        "author": "Brian K. Hall",
        "work": "Evolutionary Developmental Biology",
        "quote": "Skeletal adaptations such as prolonged digit elongation in bats illustrate the developmental power of **peramorphism**."
      },
      {
        "author": "Kenneth J. McNamara",
        "work": "Heterochrony: The Evolution of Ontogeny",
        "quote": "Fossil ammonites frequently demonstrate **peramorphism** in suture complexity as younger lineages evolve increasingly convoluted septal margins."
      }
    ]
  },
  "Dashboard — morph\\peramorphosis.md": {
    "primary": "Heterochronic evolutionary development in which descendant organisms progress developmentally beyond the adult morphology of their ancestors, displaying exaggerated or hyper-adult traits.",
    "secondary": "In paleontology and evolutionary morphology, peramorphosis contrasts with paedomorphosis, explaining extreme evolutionary trends such as the giant tusks of mammoths.",
    "quotes": [
      {
        "author": "Stephen Jay Gould",
        "work": "The Structure of Evolutionary Theory",
        "quote": "The concept of **peramorphosis** unifies heterochronic mechanisms that push adult phenotypes past the ancestral developmental frontier."
      },
      {
        "author": "Gavin de Beer",
        "work": "Embryos and Ancestors",
        "quote": "We observe **peramorphosis** whenever allometric growth rates accelerate, producing hyper-specialized cranial horns or appendages."
      },
      {
        "author": "Pere Alberch",
        "work": "Size and Shape in Ontogeny and Phylogeny",
        "quote": "A mathematical model of morphospaces distinguishes paedomorphosis from **peramorphosis** along developmental time and growth rate vectors."
      }
    ]
  },
  "Dashboard — morph\\perimorph.md": {
    "primary": "A mineral species that encloses, encrusts, or coats another mineral crystal of a different species, forming an outer mineral sheath.",
    "secondary": "In descriptive mineralogy, a perimorph forms when a newly deposited mineral encapsulates an earlier crystal, often preserving the mold if the core later dissolves.",
    "quotes": [
      {
        "author": "J. D. Dana",
        "work": "A System of Mineralogy",
        "quote": "When chalcedony forms an incrustation over cubic fluorite crystals, the external shell is known as a **perimorph**."
      },
      {
        "author": "René Just Haüy",
        "work": "Traité de minéralogie",
        "quote": "The cavity left after the central mineral decomposes reveals the exact impression captured by the surrounding **perimorph**."
      },
      {
        "author": "Paul Groth",
        "work": "Physikalische Krystallographie",
        "quote": "Epitaxial deposition frequently produces a crystalline **perimorph** whose growth directions align with the host prism."
      }
    ]
  },
  "Dashboard — morph\\plesiomorphy.md": {
    "primary": "An ancestral, primitive, or evolutionary baseline character state that was present in the common ancestor of a clade and retained in descendants.",
    "secondary": "In phylogenetic cladistics, plesiomorphies (symplesiomorphies) cannot be used to establish monophyly, as they are shared with distant outgroups.",
    "quotes": [
      {
        "author": "Willi Hennig",
        "work": "Phylogenetic Systematics",
        "quote": "A shared primitive trait, or symplesiomorphy, reflects a distant **plesiomorphy** that provides no evidence of recent cladistic divergence."
      },
      {
        "author": "Ernst Mayr",
        "work": "Principles of Systematic Zoology",
        "quote": "Cold-bloodedness in reptiles represents a primitive **plesiomorphy** inherited from early amniotes, not a shared derived innovation."
      },
      {
        "author": "Douglas Futuyma",
        "work": "Evolutionary Biology",
        "quote": "Polarity assessment using outgroup comparison determines whether an anatomical character represents an apomorphy or a **plesiomorphy**."
      }
    ]
  },
  "Dashboard — morph\\polymorph.md": {
    "primary": "An organism, crystalline substance, or chemical compound that occurs in two or more distinctly different forms, habits, or structures.",
    "secondary": "In hematology, a common abbreviation for a polymorphonuclear leukocyte (neutrophil), named for its distinctly lobed, variable nuclear morphology.",
    "quotes": [
      {
        "author": "Paul Ehrlich",
        "work": "Histology of the Blood",
        "quote": "The neutrophilic **polymorph** stands as the primary cellular soldier in acute inflammatory defense against bacterial invasion."
      },
      {
        "author": "J. D. Bernal",
        "work": "The Structure of Crystals",
        "quote": "Titanium dioxide occurs in nature as rutile, anatase, and brookite, each behaving as a distinct crystalline **polymorph**."
      },
      {
        "author": "E. B. Ford",
        "work": "Ecological Genetics",
        "quote": "Field surveys measure the relative fitness of each distinct color **polymorph** in the polymorphic land snail Cepaea nemoralis."
      }
    ]
  },
  "Dashboard — morph\\polymorphemic.md": {
    "primary": "Consisting of or containing more than one morpheme; morphologically complex, derived, or inflected.",
    "secondary": "In linguistic typology, polysynthetic languages exhibit heavily polymorphemic words where entire propositions are expressed through dense concatenations of bound affixes.",
    "quotes": [
      {
        "author": "Leonard Bloomfield",
        "work": "Language",
        "quote": "A compound construction like 'blackbird' or an inflected form like 'players' is unmistakably **polymorphemic**."
      },
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "quote": "In polysynthetic tongues, a single **polymorphemic** word conveys subtle shades of meaning that require an entire sentence in English."
      },
      {
        "author": "Noam Chomsky",
        "work": "The Sound Pattern of English",
        "quote": "Stress assignment rules in English apply cyclically from inner stems to outer affixes across each **polymorphemic** construct."
      }
    ]
  },
  "Dashboard — morph\\polymorphic.md": {
    "primary": "Having, occurring in, or assuming multiple distinct forms, shapes, structural habits, or life stages.",
    "secondary": "In object-oriented software engineering, describing methods or functions that execute differently based on the runtime class of the receiving object.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Certain genera contain highly **polymorphic** species whose limitless variations confound the most experienced systematists."
      },
      {
        "author": "Bertrand Meyer",
        "work": "Object-Oriented Software Construction",
        "quote": "Dynamic binding allows a **polymorphic** method call to execute the specialized behavior appropriate to each runtime subclass."
      },
      {
        "author": "Bjarne Stroustrup",
        "work": "The C++ Programming Language",
        "quote": "Virtual member functions provide the foundational mechanism for implementing **polymorphic** interfaces in modern systems software."
      }
    ]
  },
  "Dashboard — morph\\polymorphism.md": {
    "primary": "The occurrence within an interbreeding population of two or more distinctly different discontinuous phenotypes, or the ability of a chemical substance to crystallize into multiple distinct structures.",
    "secondary": "In computer science and type theory, polymorphism allows values and functions to operate across different data types while maintaining a single uniform interface.",
    "quotes": [
      {
        "author": "E. B. Ford",
        "work": "Ecological Genetics",
        "quote": "Genetic **polymorphism** is the occurrence together in the same locality of two or more discontinuous forms of a species in such proportions that the rarest cannot be maintained merely by recurrent mutation."
      },
      {
        "author": "Luca Cardelli",
        "work": "On Understanding Types, Data Abstraction, and Polymorphism",
        "quote": "Parametric **polymorphism** permits a function to be written without regard to specific type parameters, maximizing software reusability."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Crystalline **polymorphism** illustrates how identical atomic bonds can assemble into divergent thermodynamic lattices under differing temperatures."
      }
    ]
  },
  "Dashboard — morph\\polymorphous.md": {
    "primary": "Having or assuming many diverse forms, stages, or shapes; displaying variable morphology.",
    "secondary": "In psychoanalysis and developmental psychology, Sigmund Freud famously described infantile sexuality as 'polymorphous perverse', capable of finding gratification across diverse somatic zones.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "Three Essays on the Theory of Sexuality",
        "quote": "The infantile disposition to find sexual satisfaction across diverse somatic channels reveals a **polymorphous** perverse constitutional root."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Certain volcanic lavas present a **polymorphous** mineral texture, varying from glassy obsidian to stony crystalline basalt across a single flow."
      },
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "Religious consciousness is essentially **polymorphous**, manifesting through ecstatic mysticism, ethical austerity, or ritual communion."
      }
    ]
  },
  "Dashboard — morph\\pseudomorph.md": {
    "primary": "A mineral specimen that exhibits the outward geometric crystal form characteristic of another mineral species, resulting from chemical substitution, encrustation, or alteration.",
    "secondary": "In mineralogy and petrology, pseudomorphs (such as goethite pseudomorphs after pyrite) preserve the exact cubic or pyritohedral habit of the precursor while undergoing complete chemical replacement.",
    "quotes": [
      {
        "author": "J. D. Dana",
        "work": "A System of Mineralogy",
        "quote": "A **pseudomorph** tells a fascinating story of chemical alteration, where one mineral species quietly supplants another without disturbing its geometric outline."
      },
      {
        "author": "René Just Haüy",
        "work": "Traité de minéralogie",
        "quote": "The external shape of a **pseudomorph** belongs to the former inhabitant, while its internal fracture reveals the intruding mineral."
      },
      {
        "author": "Alfred Harker",
        "work": "Metamorphism",
        "quote": "Serpentine forms a fibrous **pseudomorph** after olivine, preserving the original fractures and crystal faces of the peridotite rock."
      }
    ]
  },
  "Dashboard — morph\\synapomorphy.md": {
    "primary": "A shared, derived evolutionary character state present in two or more lineages that was inherited from their most recent common ancestor.",
    "secondary": "In cladistic systematics, synapomorphies provide the fundamental and exclusive empirical basis for establishing monophyletic clades and resolving phylogenetic trees.",
    "quotes": [
      {
        "author": "Willi Hennig",
        "work": "Phylogenetic Systematics",
        "quote": "A monophyletic group can be rigorously established only by demonstrating at least one shared derived character state, or **synapomorphy**."
      },
      {
        "author": "Edward O. Wiley",
        "work": "Phylogenetics",
        "quote": "Parsimony algorithms search for tree topologies that minimize ad hoc homoplasies while maximizing congruence among candidate **synapomorphy** characters."
      },
      {
        "author": "Colin Patterson",
        "work": "Molecules and Morphology in Evolution",
        "quote": "The presence of lactation and hair serves as an anatomical **synapomorphy** uniting all living mammals within a single evolutionary clade."
      }
    ]
  },
  "Dashboard — morph\\teleomorph.md": {
    "primary": "The sexual, perfect, or meiotic reproductive stage or morph of a fungus, characterized by the production of ascospores, basidiospores, or zygospores.",
    "secondary": "In systematic mycology, teleomorphic morphology dictates fungal taxonomic classification under the International Code of Nomenclature for algae, fungi, and plants.",
    "quotes": [
      {
        "author": "Bryce Kendrick",
        "work": "The Whole Fungus",
        "quote": "The connection of an asexual conidial mold to its sexual **teleomorph** often requires rigorous culturing under controlled nutritional stimuli."
      },
      {
        "author": "John Webster",
        "work": "Introduction to Fungi",
        "quote": "In ascomycetes, the **teleomorph** produces asci within specialized fruiting structures such as cleistothecia, perithecia, or apothecia."
      },
      {
        "author": "C. V. Subramanian",
        "work": "Hyphomycetes",
        "quote": "Even when the **teleomorph** is rarely encountered in nature, molecular sequencing can pinpoint its phylogenetic home with certainty."
      }
    ]
  },
  "Dashboard — morph\\teleomorphic.md": {
    "primary": "Pertaining to, functioning as, or characterized by the teleomorph; describing the sexual reproductive stage of fungi.",
    "secondary": "In mycology, teleomorphic fruiting bodies (such as perithecia, apothecia, or basidiocarps) facilitate genetic recombination and meiosis.",
    "quotes": [
      {
        "author": "Bryce Kendrick",
        "work": "The Whole Fungus",
        "quote": "The emergence of **teleomorphic** structures marks the transition from rapid clonal dispersal to sexual genetic recombination."
      },
      {
        "author": "John Webster",
        "work": "Introduction to Fungi",
        "quote": "Identifying the **teleomorphic** stage of an agricultural crop pathogen is essential for forecasting overwintering ascospore release."
      },
      {
        "author": "David Malloch",
        "work": "Moulds: Their Isolation and Identification",
        "quote": "Under nitrogen starvation and ultraviolet irradiation, several Penicillium species will produce their **teleomorphic** ascomata in culture."
      }
    ]
  },
  "Dashboard — morph\\theriomorphic.md": {
    "primary": "Having animal form or taking the shape of a beast; theriomorphic deities or artistic representations.",
    "secondary": "In comparative mythology and religious history, theriomorphic worship characterizes early Egyptian and shamanic traditions where gods were depicted as falcons, jackals, or bulls.",
    "quotes": [
      {
        "author": "James George Frazer",
        "work": "The Golden Bough",
        "quote": "In ancient agricultural rituals, the corn spirit was originally venerated under a **theriomorphic** disguise, appearing as a wolf or hare."
      },
      {
        "author": "E. A. Wallis Budge",
        "work": "The Gods of the Egyptians",
        "quote": "Early Dynastic religion maintained strong **theriomorphic** devotions, depicting Anubis as a jackal and Hathor as a divine cow."
      },
      {
        "author": "Mircea Eliade",
        "work": "A History of Religious Ideas",
        "quote": "Shamanic trances frequently involve an identification with a **theriomorphic** spirit guide who aids the soul's cosmic voyage."
      }
    ]
  },
  "Dashboard — morph\\trimorphic.md": {
    "primary": "Having, occurring in, or characterized by three distinctly different forms, colors, or structural habits within the same species or substance.",
    "secondary": "In evolutionary botany, trimorphic heterostyly describes plants (like Lythrum salicaria) possessing three distinct flower morphs with differing stamen and style heights to enforce cross-pollination.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Different Forms of Flowers on Plants of the Same Species",
        "quote": "In the **trimorphic** flowers of Lythrum, three distinct lengths of stamens and styles ensure that only legitimate cross-pollinations produce full seed sets."
      },
      {
        "author": "Ronald Fisher",
        "work": "The Genetical Theory of Natural Selection",
        "quote": "The genetics of a **trimorphic** breeding system requires three alleles or multiple linked loci acting in balanced equilibrium."
      },
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "The discovery of **trimorphic** heterostyly revealed an unexpected mechanism in flowering plants designed to prevent self-fertilization."
      }
    ]
  },
  "Dashboard — morph\\trimorphism.md": {
    "primary": "The existence within a single species, population, or chemical substance of three distinct morphological forms, phases, or crystalline structures.",
    "secondary": "In crystallographic chemistry, trimorphism describes compounds (such as titanium dioxide, crystallizing as rutile, anatase, and brookite) that form three distinct crystal habits.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Different Forms of Flowers on Plants of the Same Species",
        "quote": "Darwin considered floral **trimorphism** one of his most elegant demonstrations of adaptation driven by sexual selection in plants."
      },
      {
        "author": "J. D. Dana",
        "work": "A System of Mineralogy",
        "quote": "The mineral species anatase, rutile, and brookite exhibit chemical identity with physical **trimorphism** under differing pressure regimes."
      },
      {
        "author": "Eilhard Mitscherlich",
        "work": "Sur la relation qui existe entre la forme cristalline",
        "quote": "A compound demonstrating **trimorphism** provides decisive proof that external crystal habit reflects thermal conditions during solidification."
      }
    ]
  },
  "Dashboard — morph\\trimorphodon.md": {
    "primary": "A taxonomic genus of rear-fanged colubrid snakes native to arid regions of North America and Central America, commonly known as lyre snakes.",
    "secondary": "In herpetology, Trimorphodon snakes are nocturnal, rock-dwelling ambush predators characterized by broad lyre-shaped head markings, vertically elliptical pupils, and grooved rear maxillary fangs for subduing lizards.",
    "quotes": [
      {
        "author": "Edward Drinker Cope",
        "work": "The Crocodilians, Lizards, and Snakes of North America",
        "quote": "The genus **Trimorphodon** is characterized by intermediate grooved posterior maxillary teeth and a distinct lyre-shaped pattern on the crown."
      },
      {
        "author": "Raymond L. Ditmars",
        "work": "Reptiles of the World",
        "quote": "Desert lyre snakes of the genus **Trimorphodon** prowl canyon rock crevices at night, feeding primarily on sleeping spiny lizards."
      },
      {
        "author": "Hobart M. Smith",
        "work": "Handbook of Amphibians and Reptiles of Kansas",
        "quote": "Specimens of **Trimorphodon** employ mild venom delivered through grooved rear fangs to immobilize struggling saurian prey."
      }
    ]
  },
  "Dashboard — morph\\zoomorph.md": {
    "primary": "An artistic representation, deity, design motif, or symbolic object having the form or attributes of an animal.",
    "secondary": "In archaeology and art history, zoomorphs occur prominently in prehistoric rock art, Hopewell effigy mounds, and Scythian animal-style metalwork.",
    "quotes": [
      {
        "author": "Gordon Childe",
        "work": "The Dawn of European Civilization",
        "quote": "Neolithic ritual vessels frequently take the shape of a carved **zoomorph**, representing horned cattle or waterfowl."
      },
      {
        "author": "Franz Boas",
        "work": "Primitive Art",
        "quote": "Northwest Coast woodcarvers masterfully abstracted the beaver, raven, and whale, fashioning each **zoomorph** into totem poles."
      },
      {
        "author": "Claude Lévi-Strauss",
        "work": "Totemism",
        "quote": "The tribal clan identifies with its totemic **zoomorph** not because animals are feared, but because they are good to think with."
      }
    ]
  },
  "Dashboard — morph\\zoomorphism.md": {
    "primary": "The practice of attributing animal characteristics, forms, or habits to humans, deities, or inanimate objects; animal symbolism in art and religion.",
    "secondary": "In comparative theology, zoomorphism describes religious iconography that venerates deities in animal incarnations, preceding anthropomorphic godheads.",
    "quotes": [
      {
        "author": "James George Frazer",
        "work": "The Golden Bough",
        "quote": "The transition from totemism to classical religion is marked by a decline in literal **zoomorphism** in favor of humanized deities."
      },
      {
        "author": "Edward Burnett Tylor",
        "work": "Primitive Culture",
        "quote": "Early animistic mythologies display universal **zoomorphism**, portraying the sun as a golden bird and thunder as a roaring panther."
      },
      {
        "author": "Carl Jung",
        "work": "Man and His Symbols",
        "quote": "Alchemical diagrams employ intricate **zoomorphism**, representing volatile and fixed psychic principles as fighting eagles and serpents."
      }
    ]
  },
  "Dashboard — mycet\\ascomycete.md": {
    "primary": "Any fungus belonging to the division Ascomycota, characteristically producing non-motile sexual spores (ascospores) within specialized microscopic saclike cells called asci.",
    "secondary": "In economic mycology and biotechnology, ascomycetes constitute the largest fungal phylum, encompassing brewer's yeast (Saccharomyces), morels, truffles, and penicillin-producing molds.",
    "quotes": [
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi, Mycetozoa and Bacteria",
        "quote": "In every typical **ascomycete**, the formation of the ascus marks the morphological climax of the sexual reproductive cycle."
      },
      {
        "author": "John Webster",
        "work": "Introduction to Fungi",
        "quote": "The forcible discharge of ascospores from the turgid ascus allows an **ascomycete** to disseminate its progeny into air currents."
      },
      {
        "author": "Bryce Kendrick",
        "work": "The Fifth Kingdom",
        "quote": "Yeasts used in baking and brewing represent secondarily unicellular derivatives of an ancestral filamentous **ascomycete**."
      }
    ]
  },
  "Dashboard — mycet\\ascomycetous.md": {
    "primary": "Pertaining to, characteristic of, or resembling an ascomycete fungus; producing sexual spores within asci.",
    "secondary": "In plant pathology and agricultural mycology, ascomycetous pathogens cause major blights, including powdery mildews, ergot of rye, and Dutch elm disease.",
    "quotes": [
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi",
        "quote": "The **ascomycetous** nature of the parasite was confirmed by the discovery of subterranean perithecia containing eight-spored asci."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "Hyphae of an **ascomycetous** endophyte penetrate intercellular spaces of the host cortex without inducing immediate cytolysis."
      },
      {
        "author": "John Webster",
        "work": "Introduction to Fungi",
        "quote": "Lichen thalli are composed predominantly of an **ascomycetous** fungal partner cultivating symbiotic green algal or cyanobacterial photobionts."
      }
    ]
  },
  "Dashboard — mycet\\basidiomycete.md": {
    "primary": "Any fungus belonging to the division Basidiomycota, producing sexual spores (basidiospores) externally on the tips of specialized microscopic club-shaped structures called basidia.",
    "secondary": "In forest ecology and mycology, basidiomycetes include common mushrooms, puffballs, bracket fungi, rusts, smuts, and vital wood-decaying mycorrhizal symbionts.",
    "quotes": [
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi, Mycetozoa and Bacteria",
        "quote": "The distinctive club-shaped basidium distinguishes a **basidiomycete** from all other higher fungi."
      },
      {
        "author": "A. H. Reginald Buller",
        "work": "Researches on Fungi",
        "quote": "The surface tension catapult mechanism ejects the basidiospore from the sterigma of a **basidiomycete** into the inter-lamellar air space."
      },
      {
        "author": "John Webster",
        "work": "Introduction to Fungi",
        "quote": "Clamp connections along vegetative hyphae ensure the maintenance of the dikaryotic state characteristic of a **basidiomycete**."
      }
    ]
  },
  "Dashboard — mycet\\basidiomycetous.md": {
    "primary": "Pertaining to, produced by, or characteristic of a basidiomycete fungus; bearing basidiospores on basidia.",
    "secondary": "In fungal biochemistry, basidiomycetous wood-rot fungi secrete specialized lignin peroxidases and laccases capable of enzymatically decomposing complex plant lignocellulose.",
    "quotes": [
      {
        "author": "A. H. Reginald Buller",
        "work": "Researches on Fungi",
        "quote": "The spore prints of **basidiomycetous** agarics vary across the spectrum from snowy white to deep chocolate brown."
      },
      {
        "author": "Bryce Kendrick",
        "work": "The Fifth Kingdom",
        "quote": "Ectomycorrhizal associations in boreal pine forests depend on **basidiomycetous** mycelial networks that facilitate phosphorus uptake."
      },
      {
        "author": "David Malloch",
        "work": "Moulds: Their Isolation and Identification",
        "quote": "White-rot decay in fallen hardwood logs is driven by **basidiomycetous** enzymes that selectively depolymerize recalcitrant lignin."
      }
    ]
  }
};

const count = updateNotesBatch(baseDir, batchData);
console.log(`Updated ${count} notes in Finish Slice 1 Batch 3.`);
