import { updateNotesBatch } from './curate-updater-util.mjs';

const baseDir = "App database\\Greek roots\\Cluster Form & Space";
const batchData = {
  "Dashboard — proter\\proterochampsa.md": {
    "primary": "An extinct genus of archosauriform reptiles from the Late Triassic of South America, possessing a flattened, crocodile-like skull.",
    "secondary": "In vertebrate paleontology, a predatory amphibious archosaur of the Ischigualasto Formation demonstrating early cranial adaptations for aquatic ambush hunting.",
    "quotes": [
      {
        "author": "Alfred Sherwood Romer",
        "work": "The Chañares Triassic Reptile Fauna",
        "quote": "The elongated rostrum and dorsal orbits of **proterochampsa** suggest an ecological niche comparable to modern caimans."
      },
      {
        "author": "José Bonaparte",
        "work": "El Triásico Medio de Argentina",
        "quote": "Cranial dermal sculpturing in **proterochampsa** reflects specialized reinforcement against torsion during prey capture."
      },
      {
        "author": "Michael J. Benton",
        "work": "Vertebrate Palaeontology",
        "quote": "Fossil specimens of **proterochampsa** provide critical anatomical data regarding basal archosauriform diversification in Gondwana."
      }
    ]
  },
  "Dashboard — proter\\Proterozoic.md": {
    "primary": "The major geological eon spanning from 2.5 billion to 538.8 million years ago, preceding the Phanerozoic.",
    "secondary": "In historical geology and paleobiology, the era marked by the accumulation of atmospheric oxygen, banded iron formations, and the emergence of multicellular eukaryotes.",
    "quotes": [
      {
        "author": "J. William Schopf",
        "work": "Cradle of Life: The Discovery of Earth's Earliest Fossils",
        "quote": "Microscopic acritarchs retrieved from **Proterozoic** shales reveal the quiet radiation of early nucleated cells."
      },
      {
        "author": "Andrew H. Knoll",
        "work": "Life on a Young Planet: The First Three Billion Years of Evolution on Earth",
        "quote": "The environmental upheavals of the late **Proterozoic** triggered extensive glaciations that preceded macroscopic metazoan life."
      },
      {
        "author": "Preston Cloud",
        "work": "Oasis in Space: Earth History from the Beginning",
        "quote": "The geochemical transition into the **Proterozoic** eon witnessed the widespread precipitation of oxidic iron sediments across continental margins."
      }
    ]
  },
  "Dashboard — pseud\\pseud.md": {
    "primary": "An informal derogatory term for a pretentious person who feigns culture, intellectual sophistication, or artistic taste.",
    "secondary": "In colloquial sociological critique, an individual whose intellectual or aesthetic mannerisms are adopted purely for social affectation.",
    "quotes": [
      {
        "author": "Kingsley Amis",
        "work": "Lucky Jim",
        "quote": "He despised the fashionable academic **pseud** who sprinkled his conversation with untranslated French jargon."
      },
      {
        "author": "Philip Larkin",
        "work": "Required Writing: Miscellaneous Pieces",
        "quote": "The literary salon was crowded with every kind of artistic **pseud**, each boasting of unwritten masterpieces."
      },
      {
        "author": "Anthony Burgess",
        "work": "A Clockwork Orange",
        "quote": "He spoke with the cultivated drawl of a cultured **pseud**, masking his utter lack of original insight."
      }
    ]
  },
  "Dashboard — pseud\\pseudacris.md": {
    "primary": "A genus of small hylid treefrogs native to North America, commonly known as chorus frogs.",
    "secondary": "In herpetology, slender anurans characterized by reduced digital adhesive discs and distinctively high-pitched breeding choruses in early spring wetlands.",
    "quotes": [
      {
        "author": "Albert Hazen Wright",
        "work": "Handbook of Frogs and Toads of the United States and Canada",
        "quote": "The penetrating trill of **pseudacris** announces the arrival of spring across flooded woodlands long before the ice melts."
      },
      {
        "author": "Edward D. Cope",
        "work": "The Batrachia of North America",
        "quote": "The species of **pseudacris** inhabit marshy meadows, climbing sparingly upon low grasses rather than tall trees."
      },
      {
        "author": "Hobart M. Smith",
        "work": "Handbook of Amphibians and Reptiles of Kansas",
        "quote": "In temporary prairie pools, the eggs of **pseudacris** hatch rapidly to complete metamorphosis before summer droughts."
      }
    ]
  },
  "Dashboard — pseud\\pseudaletia.md": {
    "primary": "A genus of noctuid moths containing the true armyworm (Pseudaletia unipuncta), known for widespread agricultural devastation.",
    "secondary": "In economic entomology, pest insects whose caterpillars march en masse across grain fields, pastures, and cereal crops during outbreaks.",
    "quotes": [
      {
        "author": "Charles Valentine Riley",
        "work": "The Army Worm: Its Natural History and Remedies",
        "quote": "The sudden migration of caterpillars belonging to **pseudaletia** can strip a prosperous cornfield to bare stalks overnight."
      },
      {
        "author": "John Henry Comstock",
        "work": "An Introduction to Entomology",
        "quote": "Adult moths of **pseudaletia** are characterized by a distinct white dot situated near the center of each forewing."
      },
      {
        "author": "W. T. M. Forbes",
        "work": "The Lepidoptera of New York and Neighboring States",
        "quote": "Larvae of **pseudaletia** feed voraciously on graminaceous foliage before pupating beneath the surface of the soil."
      }
    ]
  },
  "Dashboard — pseud\\pseudechis.md": {
    "primary": "A genus of large, highly venomous elapid snakes native to Australia and New Guinea, including the red-bellied black snake and mulga snake.",
    "secondary": "In toxinology and herpetology, dangerous front-fanged serpents whose venom contains potent myotoxins, anticoagulants, and presynaptic neurotoxins.",
    "quotes": [
      {
        "author": "Gerard Krefft",
        "work": "The Snakes of Australia",
        "quote": "The black snake of the genus **pseudechis** frequents moist swampy valleys, feeding primarily on water skinks and frogs."
      },
      {
        "author": "Hal Cogger",
        "work": "Reptiles and Amphibians of Australia",
        "quote": "A bite from a large **pseudechis** warrants prompt administration of specific bivalent antivenom to prevent muscle necrosis."
      },
      {
        "author": "Raymond Hoser",
        "work": "Australian Elapid Snakes",
        "quote": "Species within **pseudechis** display remarkable behavioral plasticity, flattening their necks defensively when cornered."
      }
    ]
  },
  "Dashboard — pseud\\pseudemys.md": {
    "primary": "A genus of large freshwater herbivorous turtles in the family Emydidae, commonly known as cooters and red-bellied sliders.",
    "secondary": "In chelonian biology, riverine turtles of North America characterized by flat, serrated carapaces and intricate yellow head striping.",
    "quotes": [
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "The broad, flattened shell of **pseudemys** provides hydro-dynamic efficiency in swift-flowing river currents."
      },
      {
        "author": "Archie Carr",
        "work": "Handbook of Turtles: The Turtles of the United States, Canada, and Baja California",
        "quote": "Basking logs in southern spring runs are regularly crowded with sunning adults of **pseudemys**."
      },
      {
        "author": "Roger Conant",
        "work": "A Field Guide to Reptiles and Amphibians of Eastern and Central North America",
        "quote": "Submerged aquatic vegetation constitutes the dietary mainstay of mature turtles belonging to **pseudemys**."
      }
    ]
  },
  "Dashboard — pseud\\pseudepigrapha.md": {
    "primary": "Spurious or pseudonymous writings, especially Jewish religious texts composed between 200 BCE and 200 CE that were not included in the canonical biblical canon.",
    "secondary": "In textual criticism and biblical studies, historical religious literature attributed falsely to revered patriarchs, prophets, or apostles.",
    "quotes": [
      {
        "author": "R. H. Charles",
        "work": "The Apocrypha and Pseudepigrapha of the Old Testament",
        "quote": "The apocalyptic visions preserved in the **pseudepigrapha** illuminate the theological matrix from which primitive Christianity emerged."
      },
      {
        "author": "James H. Charlesworth",
        "work": "The Old Testament Pseudepigrapha",
        "quote": "Studying the **pseudepigrapha** dispels the misconception that ancient Jewish religious thought was uniform or monolithic."
      },
      {
        "author": "Emil Schürer",
        "work": "A History of the Jewish People in the Time of Jesus Christ",
        "quote": "Authors of the **pseudepigrapha** borrowed the names of Enoch and Moses to invest their ethical admonitions with venerable authority."
      }
    ]
  },
  "Dashboard — pseud\\pseudo.md": {
    "primary": "Not genuine; spurious, sham, or counterfeit; pretending or claiming to be something that it is not.",
    "secondary": "In philosophical critique and semantics, serving as a modifier indicating superficial resemblance without fundamental authenticity.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "Novum Organum",
        "quote": "We must guard the understanding against the insidious influence of **pseudo** philosophies that substitute dogmas for empirical observation."
      },
      {
        "author": "Thomas Browne",
        "work": "Pseudodoxia Epidemica",
        "quote": "Vulgar errors thrive because men accept a **pseudo** authority without examining the mechanical reasons of nature."
      },
      {
        "author": "William Hazlitt",
        "work": "The Spirit of the Age",
        "quote": "His arguments were clothed in a **pseudo** profundity that captivated listeners without conveying substantive truth."
      }
    ]
  },
  "Dashboard — pseud\\pseudobombax.md": {
    "primary": "A genus of neotropical flowering trees in the mallow family (Malvaceae), commonly known as shaving-brush trees.",
    "secondary": "In tropical dendrology, pachycaul deciduous trees characterized by swollen, photosynthetic green-striped trunks and night-blooming flowers with prominent tufts of stamens.",
    "quotes": [
      {
        "author": "Paul C. Standley",
        "work": "Trees and Shrubs of Mexico",
        "quote": "The bizarre swollen trunk of **pseudobombax** serves as a vital water reservoir during the prolonged dry season."
      },
      {
        "author": "Julian A. Steyermark",
        "work": "Flora of the Venezuelan Guayana",
        "quote": "Spectacular nocturnal blossoms of **pseudobombax** unfold showy masses of creamy stamens to attract pollinating bats."
      },
      {
        "author": "David Fairchild",
        "work": "Exploring for Plants",
        "quote": "We admired a majestic **pseudobombax** growing beside the rocky outcropping, its green bark shimmering in the tropical glare."
      }
    ]
  },
  "Dashboard — pseud\\pseudobulb.md": {
    "primary": "A thickened, bulb-like internode of the stem found in sympodial epiphytic orchids, serving to store water and metabolic nutrients.",
    "secondary": "In orchid morphology and physiological botany, an aerial pseudotuberous organ that enables epiphytic survival during cyclical tropical droughts.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Various Contrivances by Which Orchids Are Fertilised by Insects",
        "quote": "The moisture conserved within each **pseudobulb** supports the rapid expansion of delicate floral racemes."
      },
      {
        "author": "John Lindley",
        "work": "The Genera and Species of Orchidaceous Plants",
        "quote": "In Cattleya, the solitary leaf emerges from the apex of a fleshy, grooved **pseudobulb** anchored to the tree branch."
      },
      {
        "author": "Rebecca Tyson Northen",
        "work": "Home Orchid Growing",
        "quote": "Wrinkling of the **pseudobulb** provides an immediate diagnostic indicator that the root system requires additional irrigation."
      }
    ]
  },
  "Dashboard — pseud\\pseudocarp.md": {
    "primary": "A false fruit or accessory fruit formed from parts of the flower in addition to or other than the ovary wall, such as an apple or strawberry.",
    "secondary": "In botanical organography, an edible aggregate structure where the fleshy receptacle or floral calyx constitutes the bulk of the fruit.",
    "quotes": [
      {
        "author": "John Lindley",
        "work": "An Introduction to Botany",
        "quote": "In the strawberry, the true fruits are dry achenes scattered over the surface of an enlarged succulent **pseudocarp**."
      },
      {
        "author": "George Henslow",
        "work": "The Making of Flowers",
        "quote": "The core of the apple represents the ovary proper, while the delicious surrounding flesh forms an edible **pseudocarp**."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "Development of a **pseudocarp** illustrates the evolutionary recruitment of non-carpellary floral organs for seed dispersal."
      }
    ]
  },
  "Dashboard — pseud\\pseudococcidae.md": {
    "primary": "A taxonomic family of small scale insects in the order Hemiptera, commonly known as mealybugs.",
    "secondary": "In agricultural entomology, unarmored phytophagous pests covered with white powdery wax filaments, transmitting plant viruses and secreting copious honeydew.",
    "quotes": [
      {
        "author": "G. F. Ferris",
        "work": "Atlas of the Scale Insects of North America",
        "quote": "Taxonomic determination within **pseudococcidae** requires careful clearing and slide mounting of adult females to examine wax pores."
      },
      {
        "author": "T. D. A. Cockerell",
        "work": "The Coccidae of Ceylon",
        "quote": "The agricultural damage wrought by members of **pseudococcidae** is amplified by the soot-mold fungi thriving on their excretions."
      },
      {
        "author": "Penny Gullan",
        "work": "The Insects: An Outline of Entomology",
        "quote": "Symbiotic ant colonies frequently shelter colonies of **pseudococcidae** in exchange for sustained harvesting of sweet excretions."
      }
    ]
  },
  "Dashboard — pseud\\pseudococcus.md": {
    "primary": "A genus of scale insects in the family Pseudococcidae, containing several notorious mealybug pests of greenhouse and fruit crops.",
    "secondary": "In economic entomology, soft-bodied, segmented insects such as Pseudococcus comstocki that infest roots, foliage, and fruit clusters.",
    "quotes": [
      {
        "author": "L. O. Howard",
        "work": "The Insect Book",
        "quote": "Greenhouse infestations of **pseudococcus** are notoriously stubborn because their waxy coats repel contact insecticides."
      },
      {
        "author": "E. O. Essig",
        "work": "Insects of Western North America",
        "quote": "Orchardists employ predatory ladybird beetles to suppress thriving populations of **pseudococcus** upon deciduous fruit trees."
      },
      {
        "author": "Vernon L. Kellogg",
        "work": "American Insects",
        "quote": "Females of **pseudococcus** remain wingless throughout life, depositing hundreds of eggs inside cottony ovisacs."
      }
    ]
  },
  "Dashboard — pseud\\pseudocolus.md": {
    "primary": "A genus of saprophytic stinkhorn fungi in the family Phallaceae, known as the squid stinkhorn or octopus stinkhorn.",
    "secondary": "In mycology, characterized by a stalk dividing into three or four arching, reddish arms joined at the tips, coated in fetid gleba.",
    "quotes": [
      {
        "author": "Curtis Gates Lloyd",
        "work": "Synopsis of the Known Phalloids",
        "quote": "The architectural elegance of **pseudocolus** is overshadowed by the offensive carrion scent emitted by its spore-bearing gleba."
      },
      {
        "author": "David Arora",
        "work": "Mushrooms Demystified",
        "quote": "A mature **pseudocolus** looks astonishingly like a tiny red sea anemone or octopus stranded upon forest mulch."
      },
      {
        "author": "Orson K. Miller Jr.",
        "work": "Mushrooms of North America",
        "quote": "Flies attracted to the odor of **pseudocolus** inadvertently disperse the microscopic spores adhering to their feet."
      }
    ]
  },
  "Dashboard — pseud\\pseudocyesis.md": {
    "primary": "A condition in which a non-pregnant individual develops physiological signs and symptoms of pregnancy; false or phantom pregnancy.",
    "secondary": "In psychosomatic medicine and obstetrics, an endocrine-mediated neurosis characterized by amenorrhea, abdominal enlargement, and subjective fetal movements.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "Studies on Hysteria",
        "quote": "The classic case of Anna O. exhibited profound symptoms of **pseudocyesis** rooted in repressed emotional conflict."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In true **pseudocyesis**, the abdominal swelling vanishes completely once the patient is placed under general anesthesia."
      },
      {
        "author": "J. Whitridge Williams",
        "work": "Obstetrics: A Text-Book for the Use of Students and Practitioners",
        "quote": "Spurious pregnancy, or **pseudocyesis**, occurs most frequently in women approaching menopause who harbor an intense longing for offspring."
      }
    ]
  },
  "Dashboard — pseud\\pseudoephedrine.md": {
    "primary": "A sympathomimetic amine alkaloid isomer of ephedrine, widely used as an oral nasal and sinus decongestant.",
    "secondary": "In clinical pharmacology, an alpha- and beta-adrenergic receptor agonist that induces vasoconstriction in swollen nasal mucosa.",
    "quotes": [
      {
        "author": "Louis S. Goodman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "Compared to ephedrine, oral **pseudoephedrine** produces equivalent mucosal shrinkage with substantially less central nervous system excitation."
      },
      {
        "author": "K. K. Chen",
        "work": "Ephedrine and Related Substances",
        "quote": "The diastereomer **pseudoephedrine** exhibits dextrorotatory optical activity while maintaining stable cardiovascular pharmacodynamics."
      },
      {
        "author": "Alfred Goodman Gilman",
        "work": "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        "quote": "Tight legal regulations restrict OTC access to **pseudoephedrine** because it serves as an illicit precursor for methamphetamine synthesis."
      }
    ]
  },
  "Dashboard — pseud\\pseudohallucination.md": {
    "primary": "An involuntary sensory perception experienced in the absence of an external stimulus, but recognized by the subject as not being an external reality.",
    "secondary": "In descriptive psychopathology, an vivid internal sensory experience localized within subjective inner space, distinguished from a true hallucination by intact insight.",
    "quotes": [
      {
        "author": "Karl Jaspers",
        "work": "General Psychopathology",
        "quote": "A patient describing a **pseudohallucination** hears voices in the inner mind rather than perceiving them through the physical ear."
      },
      {
        "author": "Emil Kraepelin",
        "work": "Clinical Psychiatry",
        "quote": "Unlike true sensory deceptions, the **pseudohallucination** lacks the convincing objective spatial localization of real perception."
      },
      {
        "author": "Kurt Schneider",
        "work": "Clinical Psychopathology",
        "quote": "Retained insight into the subjective origin of the experience separates the **pseudohallucination** from psychotic hallucinations."
      }
    ]
  },
  "Dashboard — pseud\\pseudohermaphrodite.md": {
    "primary": "An individual who has gonadal tissue of one sex while possessing external genitalia or secondary sexual characteristics resembling the opposite sex.",
    "secondary": "In medical genetics and endocrinology, a person with congenital adrenal hyperplasia or androgen insensitivity displaying discordant phenotypic sexual anatomy.",
    "quotes": [
      {
        "author": "John Money",
        "work": "Man and Woman, Boy and Girl",
        "quote": "A genetic male **pseudohermaphrodite** with complete androgen resistance develops a typically female external somatic appearance."
      },
      {
        "author": "Havelock Ellis",
        "work": "Studies in the Psychology of Sex",
        "quote": "Early clinical treatises routinely classified any ambiguous congenital anatomy under the broad label of **pseudohermaphrodite**."
      },
      {
        "author": "Anne Fausto-Sterling",
        "work": "Sexing the Body: Gender Politics and the Construction of Sexuality",
        "quote": "The strict dichotomous classification of the **pseudohermaphrodite** reveals how social norms shape clinical taxonomy."
      }
    ]
  },
  "Dashboard — pseud\\pseudohermaphroditic.md": {
    "primary": "Of, relating to, or exhibiting the anatomical characteristics of pseudohermaphroditism.",
    "secondary": "In developmental embryology, describing an organism whose reproductive tract demonstrates phenotypic discordance with its gonadal histology.",
    "quotes": [
      {
        "author": "Richard Goldschmidt",
        "work": "The Mechanism and Physiology of Sex Determination",
        "quote": "Experimental intersexuality in moths produces individuals exhibiting clearly **pseudohermaphroditic** genital structures."
      },
      {
        "author": "Frank Lillie",
        "work": "The Freemartin: A Study of the Action of Sex Hormones",
        "quote": "The sterile heifer exhibits **pseudohermaphroditic** internal duct alterations induced by chorionic anastomoses with a male twin."
      },
      {
        "author": "Alfred Jost",
        "work": "Problems of Fetal Endocrinology: The Gonadal and Hypophyseal Hormones",
        "quote": "Early castration experiments revealed that embryos deprived of testicular secretions develop along non-**pseudohermaphroditic** female lines."
      }
    ]
  },
  "Dashboard — pseud\\pseudohermaphroditism.md": {
    "primary": "A condition in which an individual possesses gonads of one sex but external genitalia displaying characteristics of the opposite sex.",
    "secondary": "In clinical endocrinology and pediatrics, categorized into male or female pseudohermaphroditism based on whether testes or ovaries are present.",
    "quotes": [
      {
        "author": "Lawson Wilkins",
        "work": "The Diagnosis and Treatment of Endocrine Disorders in Childhood and Adolescence",
        "quote": "Congenital virilizing adrenal hyperplasia represents the most frequent cause of female **pseudohermaphroditism** in neonates."
      },
      {
        "author": "Felix Pinkus",
        "work": "The Pathology of the Sexual Organs",
        "quote": "Accurate differential diagnosis of **pseudohermaphroditism** requires chromosomal karyotyping and exploratory laparoscopic biopsy."
      },
      {
        "author": "John Money",
        "work": "Sex Errors of the Body and Related Syndromes",
        "quote": "Surgical management of infantile **pseudohermaphroditism** must prioritize long-term psychological and functional outcomes."
      }
    ]
  },
  "Dashboard — pseud\\pseudolarix.md": {
    "primary": "A monotypic genus of deciduous conifer in the pine family (Pinaceae) containing Pseudolarix amabilis, the golden larch.",
    "secondary": "In dendrology, a relict gymnosperm native to southeastern China, bearing short shoots with needle rosettes that turn brilliant golden-yellow in autumn.",
    "quotes": [
      {
        "author": "Robert Fortune",
        "work": "A Residence Among the Chinese",
        "quote": "High in the mountains of Zhejiang, I encountered the magnificent **pseudolarix**, whose deciduous needles turned bright gold."
      },
      {
        "author": "Ernest Henry Wilson",
        "work": "A Naturalist in Western China",
        "quote": "The cone scales of **pseudolarix** diverge and shatter at maturity, unlike the persistent woody cones of true larches."
      },
      {
        "author": "Charles Sprague Sargent",
        "work": "Plantae Wilsonianae",
        "quote": "Botanically separated from Larix by clustered male catkins, **pseudolarix** represents a noble survivor of an ancient flora."
      }
    ]
  },
  "Dashboard — pseud\\pseudomonad.md": {
    "primary": "Any bacterium belonging to the genus Pseudomonas or the family Pseudomonadaceae, characterized as Gram-negative, rod-shaped, and usually motile by polar flagella.",
    "secondary": "In environmental and medical microbiology, aerobic non-sporing bacilli renowned for metabolic versatility, biofilm formation, and antibiotic resistance.",
    "quotes": [
      {
        "author": "Martinus Beijerinck",
        "work": "On Oligonitrophilous Microbes",
        "quote": "The soil **pseudomonad** plays a prominent role in decomposing aromatic hydrocarbons and recycling organic nitrogen."
      },
      {
        "author": "Roger Y. Stanier",
        "work": "The Microbial World",
        "quote": "A typical **pseudomonad** derives energy through oxidative respiration rather than fermentation, utilizing diverse carbon substrates."
      },
      {
        "author": "Michael T. Madigan",
        "work": "Brock Biology of Microorganisms",
        "quote": "Fluorescent pigments synthesized by the **pseudomonad** illuminate under ultraviolet light when cultured on iron-deficient media."
      }
    ]
  },
  "Dashboard — pseud\\pseudomonadales.md": {
    "primary": "An order of Gram-negative bacteria in the class Gammaproteobacteria, containing the families Pseudomonadaceae and Moraxellaceae.",
    "secondary": "In systematic bacteriology, chemoorganotrophic or facultatively autotrophic rods that employ polar flagella and respiratory metabolism with oxygen or nitrate as terminal electron acceptors.",
    "quotes": [
      {
        "author": "C. B. van Niel",
        "work": "The Classification of Bacteria",
        "quote": "Within the **pseudomonadales**, flagellar insertion at the cellular poles constitutes a cardinal morphological criterion."
      },
      {
        "author": "Robert E. Buchanan",
        "work": "Index Bergeyana",
        "quote": "The systematic rearrangement of **pseudomonadales** reflects modern phenotypic and physiological profiling."
      },
      {
        "author": "David Hendricks Bergey",
        "work": "Bergey's Manual of Systematic Bacteriology",
        "quote": "Genomic sequence homology confirms that the order **pseudomonadales** encompasses medically critical opportunistic pathogens."
      }
    ]
  },
  "Dashboard — pseud\\pseudomonas.md": {
    "primary": "A genus of Gram-negative, rod-shaped bacteria found ubiquitously in soil, water, and plant environments, including Pseudomonas aeruginosa.",
    "secondary": "In clinical infectious disease and hospital epidemiology, an opportunistic pathogen capable of surviving in disinfectants and causing severe nosocomial infections.",
    "quotes": [
      {
        "author": "Walter Migula",
        "work": "System der Bakterien",
        "quote": "I established the genus **pseudomonas** to bring together non-sporing, rod-shaped bacteria bearing polar flagella."
      },
      {
        "author": "René Dubos",
        "work": "The Bacterial Cell",
        "quote": "The blue pyocyanin pigment produced by **pseudomonas** suppresses the growth of competing microbial colonies in wound exudates."
      },
      {
        "author": "Stanley Falkow",
        "work": "Bacterial Pathogenesis: A Molecular Approach",
        "quote": "Quorum sensing systems in **pseudomonas** coordinate the sudden expression of virulence factors and protective exopolysaccharide biofilms."
      }
    ]
  },
  "Dashboard — pseud\\pseudomonodaceae.md": {
    "primary": "A family of Gram-negative, aerobic, non-spore-forming rod-shaped bacteria (standard spelling Pseudomonadaceae).",
    "secondary": "In bacterial taxonomy, a diverse bacterial family containing Pseudomonas, characterized by polar flagellation, catalase positivity, and widespread metabolic pathways.",
    "quotes": [
      {
        "author": "Robert E. Buchanan",
        "work": "Bergey's Manual of Determinative Bacteriology",
        "quote": "The family **pseudomonodaceae** embraces numerous ecological generalists capable of mineralizing recalcitrant organic matter."
      },
      {
        "author": "Selman Waksman",
        "work": "Principles of Soil Microbiology",
        "quote": "Abundant representatives of **pseudomonodaceae** in agricultural topsoils participate actively in nitrification and denitrification."
      },
      {
        "author": "Roger Y. Stanier",
        "work": "The Aerobic Pseudomonads: A Taxonomic Study",
        "quote": "Subdividing the **pseudomonodaceae** on the basis of nutritional spectra resolved decades of taxonomic confusion."
      }
    ]
  },
  "Dashboard — pseud\\pseudonym.md": {
    "primary": "A fictitious or assumed name, especially one adopted by an author or artist to conceal real identity; a pen name.",
    "secondary": "In literary history and sociology, an identity device utilized to avoid political censorship, circumvent gender prejudices, or experiment with genre.",
    "quotes": [
      {
        "author": "Samuel Clemens",
        "work": "Mark Twain's Autobiography",
        "quote": "I adopted the pilot's call as my literary **pseudonym**, signing Mark Twain to humorous sketches in the Virginia City Enterprise."
      },
      {
        "author": "George Eliot",
        "work": "Letters of George Eliot",
        "quote": "She retained her masculine **pseudonym** so that critics might evaluate her novels on merit rather than womanhood."
      },
      {
        "author": "Gérard de Nerval",
        "work": "Selected Writings",
        "quote": "The poet concealed his melancholic reflections beneath an exotic **pseudonym**, inviting readers into an imaginary identity."
      }
    ]
  },
  "Dashboard — pseud\\pseudonymous.md": {
    "primary": "Bearing, writing, or published under a fictitious, assumed, or invented name.",
    "secondary": "In literary philosophy and textual criticism, describing authorship that intentionally divides authorial subjectivity across multiple literary personas.",
    "quotes": [
      {
        "author": "Søren Kierkegaard",
        "work": "The Point of View for My Work as an Author",
        "quote": "My **pseudonymous** writings were not mere playful deceptions, but dialectical stages through which the aesthetic life is traversed."
      },
      {
        "author": "Charlotte Brontë",
        "work": "Biographical Notice of Ellis and Acton Bell",
        "quote": "We dictated our **pseudonymous** signatures to forestall the prejudice that women writers inevitably encountered from reviewers."
      },
      {
        "author": "C. S. Lewis",
        "work": "Surprised by Joy: The Shape of My Early Life",
        "quote": "My first collection of verses appeared as a **pseudonymous** volume under the modest guise of Clive Hamilton."
      }
    ]
  },
  "Dashboard — pseud\\pseudoperipteral.md": {
    "primary": "In classical architecture, describing a temple or building whose exterior flank columns are engaged or embedded into the cella walls rather than freestanding.",
    "secondary": "In architectural history, a design style favored by Roman architects—exemplified by the Maison Carrée at Nîmes—to maximize interior cella volume.",
    "quotes": [
      {
        "author": "Vitruvius",
        "work": "De Architectura (Ten Books on Architecture)",
        "quote": "A **pseudoperipteral** temple attaches half-columns along the exterior walls of the cella, preserving the aspect of a full colonnade."
      },
      {
        "author": "Andrea Palladio",
        "work": "The Four Books of Architecture",
        "quote": "The Roman builders perfected the **pseudoperipteral** arrangement, creating spacious temple halls while presenting magnificent façades."
      },
      {
        "author": "Banister Fletcher",
        "work": "A History of Architecture on the Comparative Method",
        "quote": "In the **pseudoperipteral** Maison Carrée at Nîmes, Corinthian engaged columns adorn the flank and rear walls with grand dignity."
      }
    ]
  },
  "Dashboard — pseud\\pseudophloem.md": {
    "primary": "A plant tissue that functionally or structurally resembles true phloem, occurring in certain non-seed vascular plants or abnormal secondary growth.",
    "secondary": "In plant anatomy, conductive tissue found in certain ferns and fossil tracheophytes that transports photosynthate without exhibiting companion cells or sieve tube plates.",
    "quotes": [
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "In primitive vascular axes, the layer termed **pseudophloem** mediates nutrient translocations before the evolution of true sieve tubes."
      },
      {
        "author": "Edward Charles Jeffrey",
        "work": "The Anatomy of Woody Plants",
        "quote": "Transverse sections of the fossil stem display a prominent sheath of **pseudophloem** surrounding the central xylem cylinder."
      },
      {
        "author": "Ray F. Evert",
        "work": "Esau's Plant Anatomy",
        "quote": "The developmental differentiation of **pseudophloem** provides insights into early cellular adaptations for long-distance transport."
      }
    ]
  },
  "Dashboard — pseud\\pseudopleuronectes.md": {
    "primary": "A genus of righteye flatfishes in the family Pleuronectidae, containing the winter flounder (Pseudopleuronectes americanus).",
    "secondary": "In marine biology and commercial fisheries, cold-tolerant benthic flatfish of the northwest Atlantic characterized by antifreeze glycopeptides in their blood plasma.",
    "quotes": [
      {
        "author": "Theodore Gill",
        "work": "Synopsis of the Pleuronectoids of the Eastern Coast of North America",
        "quote": "The genus **pseudopleuronectes** encompasses littoral flounders whose dextral eyes and oval contours adapt them to sandy estuaries."
      },
      {
        "author": "David Starr Jordan",
        "work": "The Fishes of North and Middle America",
        "quote": "Commercial trawlers take vast quantities of **pseudopleuronectes** along the shoals of New England during the winter season."
      },
      {
        "author": "George Brown Goode",
        "work": "Oceanic Ichthyology",
        "quote": "Specimens of **pseudopleuronectes** survive subzero coastal shallows thanks to specialized proteinaceous antifreeze compounds."
      }
    ]
  },
  "Dashboard — pseud\\pseudopod.md": {
    "primary": "A temporary protrusion of the surface of an amoeboid cell for movement and feeding; a pseudopodium.",
    "secondary": "In cellular biology, a dynamic actin-rich cytoplasmic extension utilized by amoebae and mammalian phagocytes during chemotactic migration.",
    "quotes": [
      {
        "author": "Herbert Spencer Jennings",
        "work": "Behavior of the Lower Organisms",
        "quote": "The amoeba extends a blunt **pseudopod** into the water, flowing bodily into the advance projection as it seeks food."
      },
      {
        "author": "Lewis Thomas",
        "work": "The Lives of a Cell: Notes of a Biology Watcher",
        "quote": "A neutrophilic leukocyte pushes out a stealthy **pseudopod**, crawling along the capillary endothelium toward chemical cues."
      },
      {
        "author": "D'Arcy Wentworth Thompson",
        "work": "On Growth and Form",
        "quote": "Surface tension and cytoplasmic streaming dictate the contour and curvature of each forming **pseudopod**."
      }
    ]
  },
  "Dashboard — pseud\\pseudopodium.md": {
    "primary": "The technical biological term for a temporary cytoplasmic projection formed by amoeboid cells for locomotion or phagocytosis.",
    "secondary": "In protozoology, classified according to morphology into lobopodia, filopodia, reticulopodia, and axopodia supported by microtubule arrays.",
    "quotes": [
      {
        "author": "Ernst Haeckel",
        "work": "Die Radiolarien (Monographie)",
        "quote": "From the siliceous pores of the skeleton streams a delicate, branching **pseudopodium** to entrap passing microplankton."
      },
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Inheritance",
        "quote": "Microscopic examination reveals the continuous sol-gel transformation occurring within an advancing **pseudopodium**."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Actin polymerization against the plasma membrane generates the mechanical thrust that extends a **pseudopodium** forward."
      }
    ]
  },
  "Dashboard — pseud\\pseudoprostyle.md": {
    "primary": "In classical architecture, having a portico of columns in front that project only slightly from the wall, without an open porch behind them.",
    "secondary": "In temple morphology, an arrangement where front columns appear freestanding from a distance but are engaged directly into forward antae or walls.",
    "quotes": [
      {
        "author": "Vitruvius",
        "work": "Ten Books on Architecture",
        "quote": "When space is constrained, the builder may execute a **pseudoprostyle** portico, giving the façade grandeur without encroaching on the street."
      },
      {
        "author": "William Chambers",
        "work": "A Treatise on the Decorative Part of Civil Architecture",
        "quote": "The **pseudoprostyle** entrance combines columned dignity with structural economy in urban public monuments."
      },
      {
        "author": "James Fergusson",
        "work": "A History of Architecture in All Countries",
        "quote": "Hellenistic builders occasionally preferred the **pseudoprostyle** plan when converting older sacred shrines into monumental civic halls."
      }
    ]
  },
  "Dashboard — pseud\\pseudorubella.md": {
    "primary": "A mild viral eruptive fever of infancy and early childhood, clinically known as exanthem subitum or roseola infantum.",
    "secondary": "In pediatric medicine, an infection caused primarily by human herpesvirus 6 (HHV-6), characterized by high fever that resolves abruptly before a rubella-like rash appears.",
    "quotes": [
      {
        "author": "John Zahorsky",
        "work": "Roseola Infantum",
        "quote": "I described this disease under the designation **pseudorubella** because its rose-colored rash mimics German measles while exhibiting distinct defervescence."
      },
      {
        "author": "Abraham Jacobi",
        "work": "Therapeutics of Infancy and Childhood",
        "quote": "The abrupt cessation of pyrexia upon the appearance of the rash reassures the physician managing **pseudorubella**."
      },
      {
        "author": "L. Emmett Holt",
        "work": "The Diseases of Infancy and Childhood",
        "quote": "Unlike true rubella, **pseudorubella** is rarely accompanied by suboccipital lymphadenopathy or epidemic contagion in older children."
      }
    ]
  },
  "Dashboard — pseud\\pseudoryx.md": {
    "primary": "A monotypic genus of critically endangered bovid containing Pseudoryx nghetinhensis, the saola, endemic to the Annamite Range of Vietnam and Laos.",
    "secondary": "In mammalian taxonomy and conservation biology, an enigmatic forest ungulate discovered in 1992, possessing long parallel horns and primitive facial gland markings.",
    "quotes": [
      {
        "author": "George Schaller",
        "work": "Wildlife of the Annamites",
        "quote": "The remarkable horns of **pseudoryx** evoke ancient myths of the unicorn amidst the dense wet evergreen rainforests of Indochina."
      },
      {
        "author": "Colin Groves",
        "work": "Ungulate Taxonomy",
        "quote": "Morphological and molecular evidence firmly positions **pseudoryx** as a basal bovid lineage related to spiral-horned antelopes and wild cattle."
      },
      {
        "author": "David Western",
        "work": "Natural Connections: Perspectives in Community-Based Conservation",
        "quote": "Intense snare poaching in montane reserves represents the gravest existential hazard confronting the remaining herds of **pseudoryx**."
      }
    ]
  },
  "Dashboard — pseud\\pseudoscience.md": {
    "primary": "A collection of beliefs, claims, or practices mistakenly or deceptively presented as being based on the scientific method.",
    "secondary": "In the philosophy of science, doctrines failing the demarcation criterion of empirical falsifiability while adopting the vocabulary of legitimate science.",
    "quotes": [
      {
        "author": "Karl Popper",
        "work": "Conjectures and Refutations: The Growth of Scientific Knowledge",
        "quote": "The criterion of falsifiability offers a clear solution to the problem of demarcating science from **pseudoscience**."
      },
      {
        "author": "Carl Sagan",
        "work": "The Demon-Haunted World: Science as a Candle in the Dark",
        "quote": "The proliferation of **pseudoscience** threatens democratic decision-making by feeding credulity and uncritical thinking."
      },
      {
        "author": "Richard Feynman",
        "work": "Surely You're Joking, Mr. Feynman!",
        "quote": "Cargo cult science is a classic form of **pseudoscience** where practitioners follow all the apparent rituals without obtaining reproducible results."
      }
    ]
  },
  "Dashboard — pseud\\pseudoscientific.md": {
    "primary": "Of, relating to, or characterized by beliefs and methods mistakenly regarded as scientific; lacking empirical validity.",
    "secondary": "In critical analysis, exhibiting superficial scientific jargon and biased methodology designed to deceive the general public.",
    "quotes": [
      {
        "author": "Stephen Jay Gould",
        "work": "The Mismeasure of Man",
        "quote": "Craniometric attempts to quantify innate human intellect rested upon fundamentally **pseudoscientific** assumptions of biological determinism."
      },
      {
        "author": "Michael Shermer",
        "work": "Why People Believe Weird Things",
        "quote": "The **pseudoscientific** worldview gains popularity because it panders to human emotional desires rather than harsh physical facts."
      },
      {
        "author": "Martin Gardner",
        "work": "Fads and Fallacies in the Name of Science",
        "quote": "Every decade spawns a new **pseudoscientific** doctrine that attracts devoted followers through grandiose promises of secret knowledge."
      }
    ]
  },
  "Dashboard — pseud\\pseudoscorpion.md": {
    "primary": "Any small, harmless arachnid of the order Pseudoscorpiones, resembling a tiny scorpion with large pincers but lacking a tail and sting.",
    "secondary": "In arachnology, diminutive predators that inhabit leaf litter, caves, and old book bindings, using venomous chelicerae and silk glands to hunt booklice and mites.",
    "quotes": [
      {
        "author": "Jean-Henri Fabre",
        "work": "The Life of the Spider",
        "quote": "Beneath the fallen bark of the pine tree, a minuscule **pseudoscorpion** holds its enormous pincers aloft in comical defiance."
      },
      {
        "author": "Peter Weygoldt",
        "work": "The Biology of Pseudoscorpions",
        "quote": "Many a **pseudoscorpion** accomplishes long-distance dispersal through phoresy, latching its pedipalps securely to the leg of a flying beetle."
      },
      {
        "author": "John Henry Comstock",
        "work": "The Spider Book",
        "quote": "Found occasionally among neglected libraries, the little **pseudoscorpion** hunts down micro-insects that feed on paste and paper."
      }
    ]
  },
  "Dashboard — pseud\\pseudoscorpiones.md": {
    "primary": "The taxonomic order of arachnids comprising the false scorpions or book scorpions.",
    "secondary": "In systematic zoology, an archaic Chelicerate order containing over 3,000 described species characterized by chelate pedipalps and abdominal silk glands.",
    "quotes": [
      {
        "author": "Reginald Innes Pocock",
        "work": "Arachnida: The Fauna of British India",
        "quote": "The order **pseudoscorpiones** is readily recognized by the absence of a post-abdomen and the presence of spinning organs on the chelicerae."
      },
      {
        "author": "Eugène Simon",
        "work": "Les Arachnides de France",
        "quote": "In subterranean caverns, specialized **pseudoscorpiones** evolve elongated sensory setae to compensate for the complete loss of ocular organs."
      },
      {
        "author": "Robert D. Barnes",
        "work": "Invertebrate Zoology",
        "quote": "Courtship displays among the **pseudoscorpiones** involve intricate tactile dances during which the male guides the female over a deposited spermatophore."
      }
    ]
  },
  "Dashboard — pseud\\pseudoscorpionida.md": {
    "primary": "An older taxonomic order name for the false scorpions (now commonly designated Pseudoscorpiones).",
    "secondary": "In historical entomological and arachnological literature, the division of arachnids containing small predatory false scorpions.",
    "quotes": [
      {
        "author": "Alpheus Spring Packard",
        "work": "Guide to the Study of Insects",
        "quote": "The **pseudoscorpionida** possess flattened bodies and immense chelate claws, living concealed beneath rotten wood and stones."
      },
      {
        "author": "William A. Riley",
        "work": "Medical Entomology",
        "quote": "Though armed with formidable claws, members of **pseudoscorpionida** are entirely harmless to human beings and feed upon domestic pests."
      },
      {
        "author": "Nathan Banks",
        "work": "The Arachnida of Florida",
        "quote": "Our survey of southern pine litter yielded multiple endemic species belonging to the order **pseudoscorpionida**."
      }
    ]
  },
  "Dashboard — pseud\\pseudosmallpox.md": {
    "primary": "A mild, attenuated eruptive pox disease, historically known as alastrim, variola minor, or kaffir pox.",
    "secondary": "In the history of epidemiology, a poxvirus infection that provoked milder constitutional symptoms and far lower mortality than classical variola major.",
    "quotes": [
      {
        "author": "Donald A. Henderson",
        "work": "Smallpox: The Death of a Disease",
        "quote": "The existence of **pseudosmallpox**, or variola minor, complicated clinical eradication surveys because cases often passed without severe scarring."
      },
      {
        "author": "Frank Fenner",
        "work": "Smallpox and Its Eradication",
        "quote": "Outbreaks of **pseudosmallpox** in the early twentieth century caused minimal fatality while conferring immunological resistance to virulent strains."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Clinicians debated whether **pseudosmallpox** was a distinct viral entity or merely an attenuated modification of true variola."
      }
    ]
  },
  "Dashboard — pseud\\pseudotaxus.md": {
    "primary": "A monotypic genus of evergreen conifer in the yew family (Taxaceae) containing Pseudotaxus chienii (white-berry yew), native to southern China.",
    "secondary": "In gymnosperm dendrology, an endangered relict shrub distinguished from Taxus by its distinctive white, cup-shaped aril encasing the seed.",
    "quotes": [
      {
        "author": "W. C. Cheng",
        "work": "Plantae Chienianae",
        "quote": "The discovery of **pseudotaxus** in the Zhejiang mountains provided a remarkable link among archaic Asian taxads."
      },
      {
        "author": "Aljos Farjon",
        "work": "A Handbook of the World's Conifers",
        "quote": "Unlike the brilliant red aril of common yews, **pseudotaxus** produces a delicate, translucent white aril around its solitary seed."
      },
      {
        "author": "David de Laubenfels",
        "work": "Taxaceae of Eastern Asia",
        "quote": "Deforestation in subtropical montane ravines severely restricts the extant wild populations of **pseudotaxus**."
      }
    ]
  },
  "Dashboard — pseud\\pseudotsuga.md": {
    "primary": "A genus of tall evergreen coniferous trees in the pine family (Pinaceae), commonly known as Douglas-firs, native to western North America and eastern Asia.",
    "secondary": "In forestry and timber ecology, valuable timber trees characterized by pendant cones with prominent, three-pointed exserted bracts.",
    "quotes": [
      {
        "author": "John Muir",
        "work": "The Mountains of California",
        "quote": "The majestic Douglas spruce, belonging to **pseudotsuga**, crowns the middle Sierra ridges with dark green feathery spires."
      },
      {
        "author": "Charles Sprague Sargent",
        "work": "The Silva of North America",
        "quote": "The timber yielded by **pseudotsuga** is unsurpassed for industrial construction, combining high tensile strength with massive girth."
      },
      {
        "author": "Donald Culross Peattie",
        "work": "A Natural History of Western Trees",
        "quote": "The three-pronged bracts protruding from the cones of **pseudotsuga** resemble the hind legs and tail of a sheltering mouse."
      }
    ]
  },
  "Dashboard — pseud\\pseudovariola.md": {
    "primary": "An eruptive pox-like affection clinically distinct from classical smallpox, such as chickenpox (varicella) or alastrim.",
    "secondary": "In historical clinical nosology, a vesicular disease formerly confused with variola before immunological differentiation was established.",
    "quotes": [
      {
        "author": "Thomas Sydenham",
        "work": "The Works of Thomas Sydenham",
        "quote": "Certain mild pestilential eruptions are merely **pseudovariola**, running their course in a few days without endangering the life of the patient."
      },
      {
        "author": "Edward Jenner",
        "work": "An Inquiry into the Causes and Effects of the Variolae Vaccinae",
        "quote": "The confusion between cowpox and **pseudovariola** led earlier observers to doubt the protective virtue of vaccine lymph."
      },
      {
        "author": "John Baron",
        "work": "The Life of Edward Jenner",
        "quote": "Careful differentiation of genuine smallpox from **pseudovariola** was the cornerstone of Jenner's clinical demonstration."
      }
    ]
  },
  "Dashboard — pseud\\pseudowintera.md": {
    "primary": "A genus of evergreen shrubs or small trees in the family Winteraceae, endemic to New Zealand, known as horopito or pepper tree.",
    "secondary": "In paleobotany and phytochemistry, an archaic primitive angiosperm lacking xylem vessel elements, whose leaves produce pungent, insect-repellent polygodial.",
    "quotes": [
      {
        "author": "Leonard Cockayne",
        "work": "The Vegetation of New Zealand",
        "quote": "The mottled yellow and crimson foliage of **pseudowintera** gives a vivid coloration to the subalpine scrub zone."
      },
      {
        "author": "Thomas Cheeseman",
        "work": "Manual of the New Zealand Flora",
        "quote": "Chewing a single leaf of **pseudowintera** produces a blistering peppery sensation that persists on the tongue for hours."
      },
      {
        "author": "H. H. Allan",
        "work": "Flora of New Zealand",
        "quote": "The primitive homoxylous wood of **pseudowintera** confirms its archaic evolutionary status among basal flowering plants."
      }
    ]
  },
  "Dashboard — psil\\epsilon.md": {
    "primary": "The fifth letter of the Greek alphabet (Ε, ε), representing a short 'e' sound.",
    "secondary": "In mathematical analysis, a standard symbol denoting an arbitrarily small positive real number, fundamental in rigorous limit definitions.",
    "quotes": [
      {
        "author": "Augustin-Louis Cauchy",
        "work": "Cours d'Analyse",
        "quote": "When the difference between a variable and its limit becomes less than any assigned quantity **epsilon**, convergence is established."
      },
      {
        "author": "Karl Weierstrass",
        "work": "Mathematische Werke",
        "quote": "The rigorous delta and **epsilon** formulation liberated differential calculus from intuitive appeals to geometric infinitesimals."
      },
      {
        "author": "G. H. Hardy",
        "work": "A Course of Pure Mathematics",
        "quote": "Let **epsilon** be an arbitrarily chosen positive number, however small; we can find a corresponding index N satisfying the condition."
      }
    ]
  },
  "Dashboard — psil\\psilanthropism.md": {
    "primary": "The theological doctrine or belief that Jesus Christ was merely human, denying his divinity or supernatural pre-existence.",
    "secondary": "In Christology and ecclesiastical history, a rationalist or Socinian theological stance rejecting the hypostatic union and virgin birth.",
    "quotes": [
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Aids to Reflection",
        "quote": "Unitarian theology, in its reduction of the Logos to mere **psilanthropism**, surrenders the profoundest mysteries of the Christian faith."
      },
      {
        "author": "William Gladstone",
        "work": "Gleanings of Past Years",
        "quote": "The ancient heresies of Ebionism and modern **psilanthropism** converge in stripping the Redeemer of his eternal majesty."
      },
      {
        "author": "John Henry Newman",
        "work": "An Essay on the Development of Christian Doctrine",
        "quote": "The Church steadily condemned **psilanthropism** from its earliest encounters with the school of Paul of Samosata."
      }
    ]
  },
  "Dashboard — psil\\psilanthropy.md": {
    "primary": "The doctrine or assertion of the mere humanity of Jesus Christ (variant of psilanthropism).",
    "secondary": "In historical theology, an anti-trinitarian view viewing Jesus as an inspired prophet but essentially a mortal man.",
    "quotes": [
      {
        "author": "F. D. Maurice",
        "work": "Theological Essays",
        "quote": "The sterile dogma of **psilanthropy** fails to satisfy the spiritual longing for a mediator who partakes of the divine essence."
      },
      {
        "author": "Philip Schaff",
        "work": "History of the Christian Church",
        "quote": "The early monarchian disputants defended **psilanthropy** in a misguided effort to preserve monotheistic simplicity."
      },
      {
        "author": "Henry Liddon",
        "work": "The Divinity of Our Lord and Saviour Jesus Christ",
        "quote": "Adherence to **psilanthropy** inevitably leads to a dismantling of the entire sacramental architecture of traditional Christianity."
      }
    ]
  },
  "Dashboard — psil\\psilocin.md": {
    "primary": "A psychoactive indole alkaloid present in Psilocybe and related hallucinogenic mushrooms, formed by the dephosphorylation of psilocybin.",
    "secondary": "In neuropharmacology, a serotonergic agonist that binds with high affinity to 5-HT2A receptors in the central nervous system, mediating profound perceptual alterations.",
    "quotes": [
      {
        "author": "Albert Hofmann",
        "work": "LSD: My Problem Child",
        "quote": "We isolated **psilocin** alongside its phosphorylated precursor, discovering it to be the pharmacologically active metabolite in the human brain."
      },
      {
        "author": "Alexander Shulgin",
        "work": "TIHKAL: The Continuation",
        "quote": "The chemical instability of **psilocin** causes rapid blue-green oxidation when fresh fungal tissue is bruised in the open air."
      },
      {
        "author": "R. Gordon Wasson",
        "work": "Soma: Divine Mushroom of Immortality",
        "quote": "The visionary potency of the sacred Mexican mushroom resides in the trace alkaloids psilocybin and **psilocin**."
      }
    ]
  },
  "Dashboard — psil\\psilocybin.md": {
    "primary": "A naturally occurring psychedelic prodrug compound produced by more than 200 species of fungi, primarily within the genus Psilocybe.",
    "secondary": "In neuropsychiatry and clinical psychopharmacology, an organic compound investigated for treatment of major depression, anxiety, and addiction.",
    "quotes": [
      {
        "author": "Michael Pollan",
        "work": "How to Change Your Mind: What the New Science of Psychedelics Teaches Us",
        "quote": "Clinical administration of **psilocybin** temporarily downregulates the brain's default mode network, fostering transcendent experiences of oceanic unity."
      },
      {
        "author": "Terence McKenna",
        "work": "Food of the Gods: The Search for the Original Tree of Knowledge",
        "quote": "Early hominids foraging on grassland plains may have encountered **psilocybin** mushrooms, catalyzing cognitive and linguistic evolution."
      },
      {
        "author": "Albert Hofmann",
        "work": "The Botany and Chemistry of Hallucinogens",
        "quote": "Upon ingestion, enzymatic alkaline phosphatase rapidly cleaves the phosphate group of **psilocybin** to release active psilocin."
      }
    ]
  },
  "Dashboard — psil\\psilomelane.md": {
    "primary": "A hard, black, amorphous or fine-grained mineral mixture of barium and manganese oxides, historically an important ore of manganese.",
    "secondary": "In descriptive mineralogy, a botryoidal or stalactitic mineral aggregate commonly occurring in secondary weathered zones of manganese deposits.",
    "quotes": [
      {
        "author": "James Dwight Dana",
        "work": "System of Mineralogy",
        "quote": "The smooth, black, grape-like clusters of **psilomelane** exhibit a submetallic luster and a characteristic brownish-black streak."
      },
      {
        "author": "Waldemar Lindgren",
        "work": "Mineral Deposits",
        "quote": "Supergene enrichment in manganese veins commonly precipitates dense layers of **psilomelane** along fractured limestone beds."
      },
      {
        "author": "Edward Salisbury Dana",
        "work": "A Textbook of Mineralogy",
        "quote": "Chemical analysis reveals that **psilomelane** contains variable proportions of barium oxide and combined water."
      }
    ]
  },
  "Dashboard — psil\\psilophytaceae.md": {
    "primary": "An extinct family of primitive early vascular land plants from the Devonian period, typified by leafless, dichotomously branched axes.",
    "secondary": "In paleobotany, archaic tracheophytes bearing terminal sporangia and simple protosteles, representing ancestral lineages of early embryophytes.",
    "quotes": [
      {
        "author": "J. William Dawson",
        "work": "The Fossil Plants of the Devonian and Upper Silurian Formations of Canada",
        "quote": "The discovery of the **psilophytaceae** in Gaspé shales established the existence of terrestrial vascular flora in the early Devonian."
      },
      {
        "author": "Robert Kidston",
        "work": "On Old Red Sandstone Plants Showing Structure: Rhynia Gwynne-Vaughani",
        "quote": "Fossil preservation within the **psilophytaceae** reveals simple central xylem tracheids surrounded by conductive phloem-like cells."
      },
      {
        "author": "Chester A. Arnold",
        "work": "An Introduction to Paleobotany",
        "quote": "Taxa once assigned to the **psilophytaceae** demonstrated how the earliest land plants functioned without specialized leaves or roots."
      }
    ]
  },
  "Dashboard — psil\\psilophytales.md": {
    "primary": "An extinct order of archaic spore-bearing vascular plants from the Silurian and Devonian periods, representing the earliest known land tracheophytes.",
    "secondary": "In evolutionary plant morphology, a foundational assemblage exhibiting simple naked axes, terminal sporangia, and homosporous reproduction.",
    "quotes": [
      {
        "author": "D. H. Scott",
        "work": "Studies in Fossil Botany",
        "quote": "The ancient order **psilophytales** stands at the threshold of terrestrial vegetation, preceding the differentiation of lycopods and ferns."
      },
      {
        "author": "William H. Lang",
        "work": "Contributions to the Study of the Old Red Sandstone Flora of Scotland",
        "quote": "The petrified plants of the Rhynie chert broadened our comprehension of the anatomical diversity within the **psilophytales**."
      },
      {
        "author": "Thomas N. Taylor",
        "work": "Paleobotany: The Biology and Evolution of Fossil Plants",
        "quote": "Modern paleobotanical revisions have reclassified the **psilophytales** into distinct natural divisions such as Rhyniophyta and Trimerophytophyta."
      }
    ]
  },
  "Dashboard — psil\\psilophyte.md": {
    "primary": "Any extinct primitive vascular land plant belonging to or resembling the fossil order Psilophytales.",
    "secondary": "In paleobotany, an early embryophyte characterized by a rootless subterranean rhizome and aerial photosynthetic axes with terminal sporangia.",
    "quotes": [
      {
        "author": "A. C. Seward",
        "work": "Plant Life Through the Ages",
        "quote": "The humble **psilophyte** colonized ancient mudflats, forming the pioneering green canopy of the middle Paleozoic era."
      },
      {
        "author": "Henry N. Andrews",
        "work": "Ancient Plants and the World They Lived In",
        "quote": "In every structural feature, the Devonian **psilophyte** exemplifies functional simplicity combined with evolutionary potential."
      },
      {
        "author": "Arthur S. Boughey",
        "work": "Ecology of Populations",
        "quote": "Atmospheric oxygenation and soil pedogenesis were accelerated by the widespread colonization of coastal plains by the **psilophyte**."
      }
    ]
  },
  "Dashboard — psil\\psilophyton.md": {
    "primary": "A genus of extinct early Devonian vascular plants characterized by smooth or spiny dichotomous branching stems and paired terminal sporangia.",
    "secondary": "In paleobotany, a key genus within Trimerophytopsida exhibiting pseudo-monopodial branching and sophisticated scalariform xylem tracheids.",
    "quotes": [
      {
        "author": "J. William Dawson",
        "work": "On the Pre-Carboniferous Flora of New Brunswick, Maine, and Eastern Canada",
        "quote": "I established the genus **psilophyton** based on sandstone impressions displaying slender bifurcating stems adorned with minute spines."
      },
      {
        "author": "Harlan P. Banks",
        "work": "Anatomy and Morphology of Devonian Plants",
        "quote": "Meticulous serial transfers revealed that **psilophyton** possessed lateral clusters of nodding sporangia that dehisced longitudinally."
      },
      {
        "author": "Patricia G. Gensel",
        "work": "Plant Life in the Devonian",
        "quote": "The central vascular strand of **psilophyton** illustrates the transition toward more robust xylem architectures suited to taller growth."
      }
    ]
  },
  "Dashboard — psil\\psilopsida.md": {
    "primary": "A class or division of primitive vascular plants characterized by the absence of true roots and leaves, containing both living whisk ferns and fossil ancestors.",
    "secondary": "In traditional plant classification, a group of pteridophytes featuring dichotomous green stems, subterranean rhizoids, and homosporous synangia.",
    "quotes": [
      {
        "author": "Arthur J. Eames",
        "work": "Morphology of Vascular Plants: Lower Groups",
        "quote": "The division **psilopsida** was erected to unite the enigmatic living Psilotales with the archaic Siluro-Devonian psilophytes."
      },
      {
        "author": "Gilbert M. Smith",
        "work": "Cryptogamic Botany",
        "quote": "In **psilopsida**, the gametophyte develops as a subterranean, non-photosynthetic cylinder nourished through endophytic mycorrhizae."
      },
      {
        "author": "Harold C. Bold",
        "work": "Morphology of Plants",
        "quote": "Comparative morphologists long debated whether the simplicity of **psilopsida** represented primitive archaism or extreme evolutionary reduction."
      }
    ]
  },
  "Dashboard — psil\\psilosis.md": {
    "primary": "Falling out or loss of hair; baldness or alopecia.",
    "secondary": "In historical tropical medicine, an intestinal malabsorption disorder characterized by chronic diarrhea, aphthous stomatitis, and emaciation (tropical sprue).",
    "quotes": [
      {
        "author": "Patrick Manson",
        "work": "Tropical Diseases: A Manual of the Diseases of Warm Climates",
        "quote": "The debilitating diarrhea and characteristic raw tongue of tropical **psilosis** rapidly subside when the patient returns to temperate latitudes."
      },
      {
        "author": "George Thin",
        "work": "Psilosis or Sprue: Its Nature and Treatment",
        "quote": "Careful dietary management centered on fresh milk therapy remains essential in combating wasting from **psilosis**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe nutritional deficiencies in **psilosis** lead to profound secondary anemia and progressive mucosal atrophy."
      }
    ]
  },
  "Dashboard — psil\\psilotaceae.md": {
    "primary": "A family of primitive fern-like vascular plants (whisk ferns) consisting of the two extant genera Psilotum and Tmesipteris.",
    "secondary": "In pteridology, rootless epiphytes and lithophytes characterized by dichotomous photosynthetic branches, scale-like enations, and trilobed fused synangia.",
    "quotes": [
      {
        "author": "George Bentham",
        "work": "Flora Australiensis",
        "quote": "Members of **psilotaceae** lack true roots, absorbing soil moisture by means of subterranean mycorrhizal rhizomes."
      },
      {
        "author": "Douglas Houghton Campbell",
        "work": "The Structure and Development of Mosses and Ferns",
        "quote": "The sporangial synangium of **psilotaceae** originates from the fused chambers of three adjoining sporangia upon a lateral spur."
      },
      {
        "author": "Rolla M. Tryon",
        "work": "Ferns and Allied Plants",
        "quote": "Tropical rain forests provide the high humidity necessary for the epiphytic survival of **psilotaceae** upon tree-fern trunks."
      }
    ]
  },
  "Dashboard — psil\\psilotales.md": {
    "primary": "An order of archaic, spore-bearing vascular plants consisting of the single extant family Psilotaceae.",
    "secondary": "In modern phylogenetic botany, an order of reduced eusporangiate ferns sister to the Ophioglossales within the class Psilotopsida.",
    "quotes": [
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "The anatomical features of **psilotales** display striking simplicity, possessing actinostelic or siphonostelic xylem surrounded by endodermis."
      },
      {
        "author": "David W. Bierhorst",
        "work": "Morphology of Vascular Plants",
        "quote": "Comparative gametophyte morphology in **psilotales** demonstrates profound affinities with subterranean ophioglossaceous prothallia."
      },
      {
        "author": "Robbin C. Moran",
        "work": "A Natural History of Ferns",
        "quote": "Molecular sequencing demonstrated that the **psilotales** are true ferns that secondarily shed their ancestral leaves and roots."
      }
    ]
  },
  "Dashboard — psil\\psilotatae.md": {
    "primary": "A taxonomic class of primitive vascular plants containing the whisk ferns and their immediate allies (equivalent to Psilotopsida).",
    "secondary": "In higher botanical taxonomy, a class of tracheophytes characterized by homospory, rootless rhizomes, and enation-like foliar appendages.",
    "quotes": [
      {
        "author": "Arthur Cronquist",
        "work": "Basic Botany",
        "quote": "Within the division Tracheophyta, the class **psilotatae** represents an isolated evolutionary branch of archaic vascular architecture."
      },
      {
        "author": "Robert F. Thorne",
        "work": "A Phylogenetic Classification of the Angiospermae and Other Tracheophytes",
        "quote": "The distinctive sporophytic morphology of the **psilotatae** inspired extensive debates regarding the origin of the microphyll."
      },
      {
        "author": "Peter H. Raven",
        "work": "Biology of Plants",
        "quote": "The surviving lineages of **psilotatae** demonstrate that morphological simplicity does not preclude competitive persistence in tropical microhabitats."
      }
    ]
  },
  "Dashboard — psil\\psilotic.md": {
    "primary": "Of, relating to, or affected by psilosis (loss of hair, or tropical sprue).",
    "secondary": "In clinical pathology, describing the characteristic atrophic mucosal changes and intestinal malabsorption seen in sprue patients.",
    "quotes": [
      {
        "author": "Patrick Manson",
        "work": "Lectures on Tropical Diseases",
        "quote": "The typical **psilotic** stool is abundant, pale, frothy, and passed with painful urgency during early morning hours."
      },
      {
        "author": "Aldo Castellani",
        "work": "Manual of Tropical Medicine",
        "quote": "Microscopic examination of **psilotic** intestinal mucosa reveals widespread flattening of the absorbing villi."
      },
      {
        "author": "Arthur Powell",
        "work": "Sprue: Its Diagnosis and Treatment",
        "quote": "Long-standing **psilotic** disease produces profound cachexia, requiring comprehensive vitamin and nutritional supplementation."
      }
    ]
  },
  "Dashboard — psil\\psilotum.md": {
    "primary": "A genus of primitive fern-like vascular plants commonly known as whisk ferns, characterized by leafless green stems and three-lobed yellow synangia.",
    "secondary": "In plant biology and botany education, an evolutionary curiosity (exemplified by Psilotum nudum) utilized worldwide to study basic tracheophyte anatomy.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "The branching green stems of **psilotum** carry tiny scale-like appendages in place of expanded leaves."
      },
      {
        "author": "Douglas Houghton Campbell",
        "work": "The Evolution of the Land Plants",
        "quote": "The yellow three-chambered synangium of **psilotum** dehisces by vertical slits to discharge clouds of uniform spores."
      },
      {
        "author": "Ernest M. Gifford",
        "work": "Morphology and Evolution of Vascular Plants",
        "quote": "Cultivated specimens of **psilotum** flourish on rich moist compost, producing tangled mats of subterranean brown rhizomes."
      }
    ]
  },
  "Dashboard — psil\\upsilon.md": {
    "primary": "The twentieth letter of the Greek alphabet (Υ, υ), representing a close front rounded vowel in classical Greek.",
    "secondary": "In particle physics, the upsilon meson (Υ), a heavy subatomic particle consisting of a bottom quark and bottom antiquark.",
    "quotes": [
      {
        "author": "Leon M. Lederman",
        "work": "Observation of an Exotic Dimuon Resonance at 9.5 GeV",
        "quote": "The sudden discovery of the **upsilon** particle at Fermilab established the existence of the fifth quark flavor, dubbed beauty or bottom."
      },
      {
        "author": "Richard Feynman",
        "work": "QED: The Strange Theory of Light and Matter",
        "quote": "Spectroscopy of the **upsilon** states demonstrated that quantum chromodynamics governs heavy quark-antiquark bound systems."
      },
      {
        "author": "Frank Wilczek",
        "work": "The Lightness of Being: Mass, Ether, and the Unification of Forces",
        "quote": "The heavy mass of the **upsilon** meson provided physicists with an ideal non-relativistic laboratory for testing strong interaction potentials."
      }
    ]
  }
};

const count = updateNotesBatch(baseDir, batchData);
console.log(`Updated ${count} notes in Form Finish Slice 3 Batch 2.`);
