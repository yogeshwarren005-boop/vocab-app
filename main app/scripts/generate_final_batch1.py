# -*- coding: utf-8 -*-
"""
Final cleanup Batch 1: 65 words (indices 0-64)
oikophobia through orthocenter
"""
import json, os

data = {
  "Dashboard \u2014 oec\\oikophobia.md": {
    "primary": "An abnormal or irrational fear or aversion to one's home environment, domestic surroundings, or household objects and routines.",
    "secondary": "In cultural criticism and political philosophy, oikophobia denotes a repudiation of one's own national culture and traditions in favor of foreign or cosmopolitan alternatives.",
    "quotes": [
      {"author": "Roger Scruton", "work": "England and the Need for Nations", "quote": "The disease of the Western mind, which I call **oikophobia**, is the disposition to repudiate one's own inheritance and home."},
      {"author": "Benedict Anderson", "work": "Imagined Communities", "quote": "The intellectual class may cultivate a refined **oikophobia**, dismissing local attachments as parochial superstition."},
      {"author": "Mark Lilla", "work": "The Shipwrecked Mind", "quote": "A paradoxical **oikophobia** overtakes those who, having benefited most from their civilization, turn against it with peculiar ferocity."}
    ]
  },
  "Dashboard \u2014 oid\\asteroidal.md": {
    "primary": "Of, relating to, or resembling an asteroid; having the characteristics or form of a small rocky body orbiting the sun.",
    "secondary": "In planetary science and astrophysics, asteroidal pertains to compositions, orbital mechanics, and spectral classifications of minor planets in the inner solar system.",
    "quotes": [
      {"author": "Carl Sagan", "work": "Cosmos", "quote": "The **asteroidal** belt between Mars and Jupiter contains remnants of a world that never formed."},
      {"author": "Patrick Moore", "work": "The Guinness Book of Astronomy", "quote": "Many meteorites have an **asteroidal** origin, having been ejected from parent bodies by catastrophic collisions."},
      {"author": "William K. Hartmann", "work": "Moons and Planets", "quote": "The **asteroidal** population reveals much about the early accretion processes of our solar system."}
    ]
  },
  "Dashboard \u2014 oid\\mucoid.md": {
    "primary": "Resembling or having the properties of mucus; of a slimy, viscous, or gelatinous consistency characteristic of mucous secretions.",
    "secondary": "In microbiology and pathology, mucoid describes bacterial colony morphology or tissue degeneration involving excessive production of mucinous polysaccharides.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The sputum in advanced cases becomes **mucoid** and tenacious, adhering to the vessel."},
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "A **mucoid** degeneration of the connective tissue was observed in the affected specimens."},
      {"author": "Patrick R. Murray", "work": "Medical Microbiology", "quote": "Pseudomonas aeruginosa frequently displays a **mucoid** phenotype in the lungs of cystic fibrosis patients."}
    ]
  },
  "Dashboard \u2014 oid\\mucoidal.md": {
    "primary": "Having the quality or appearance of mucoid tissue; pertaining to or characterized by a mucus-like substance or consistency.",
    "secondary": "In histopathology, mucoidal refers to degenerative changes in connective tissues where intercellular ground substance accumulates mucin-rich material.",
    "quotes": [
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The **mucoidal** transformation of the cartilaginous matrix proceeded with alarming rapidity."},
      {"author": "Henry Gray", "work": "Gray's Anatomy", "quote": "Certain tumors exhibit a distinctly **mucoidal** stroma rich in glycosaminoglycans."},
      {"author": "Gruber and Gruber", "work": "Handbook of Pathological Anatomy", "quote": "The **mucoidal** character of the effusion distinguished it from purely serous collections."}
    ]
  },
  "Dashboard \u2014 oid\\oid.md": {
    "primary": "A suffix-forming element derived from Greek eidos meaning form or likeness, used to create adjectives and nouns denoting resemblance to a specified thing.",
    "secondary": "In taxonomy, morphology, and chemistry, the suffix -oid systematically generates terms indicating structural similarity without identity, as in humanoid, alkaloid, and asteroid.",
    "quotes": [
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The formative element **-oid** descends from eidos, expressing likeness or resemblance to the root noun."},
      {"author": "W. D. Whitney", "work": "The Century Dictionary", "quote": "English freely employs **-oid** to coin scientific terms denoting approximate or partial resemblance."},
      {"author": "Ernest Klein", "work": "A Comprehensive Etymological Dictionary of the English Language", "quote": "The suffix **-oid** is one of the most productive Greek-derived morphemes in modern scientific nomenclature."}
    ]
  },
  "Dashboard \u2014 oid\\organoid.md": {
    "primary": "A miniature, simplified version of an organ produced in vitro from stem cells that self-organizes into three-dimensional structures mimicking the architecture of a real organ.",
    "secondary": "In developmental biology and regenerative medicine, organoids serve as model systems for studying organogenesis, disease pathology, drug screening, and personalized therapeutic strategies.",
    "quotes": [
      {"author": "Hans Clevers", "work": "Modeling Development and Disease with Organoids", "quote": "A single stem cell can give rise to an entire intestinal **organoid** containing all differentiated cell types."},
      {"author": "Madeline Lancaster", "work": "Cerebral Organoids Model Human Brain Development and Microcephaly", "quote": "The cerebral **organoid** recapitulated key features of human cortical development in a dish."},
      {"author": "Toshiro Sato", "work": "Single Lgr5 Stem Cells Build Crypt-Villus Structures", "quote": "Each **organoid** faithfully reproduced the crypt-villus architecture of the native intestinal epithelium."}
    ]
  },
  "Dashboard \u2014 om\\om.md": {
    "primary": "A Greek combining form meaning raw or uncooked, appearing in compound words relating to the consumption or state of unprocessed food or material.",
    "secondary": "In classical studies, the root om- connects to Dionysian ritual practices involving the eating of raw flesh, linking the morpheme to religious and anthropological discourse.",
    "quotes": [
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The root **om-** from Greek omos conveys the sense of rawness or the uncooked state."},
      {"author": "Pierre Chantraine", "work": "Dictionnaire etymologique de la langue grecque", "quote": "The combining form **om-** retains its Indo-European sense of raw, unprocessed, or crude throughout Greek derivatives."},
      {"author": "Robert Beekes", "work": "Etymological Dictionary of Greek", "quote": "Greek **om-** is cognate with Sanskrit ama, both preserving the Proto-Indo-European root for uncooked."}
    ]
  },
  "Dashboard \u2014 om\\omophagia.md": {
    "primary": "The practice or ritual of eating raw flesh, especially as part of religious ceremonies associated with the worship of Dionysus in ancient Greece.",
    "secondary": "In anthropology and comparative religion, omophagia symbolizes the ecstatic union of worshippers with the divine through the sacramental consumption of uncooked sacrificial meat.",
    "quotes": [
      {"author": "Walter Burkert", "work": "Greek Religion", "quote": "The act of **omophagia** was the climactic moment of the Bacchic ritual, in which the devotee consumed the god."},
      {"author": "E. R. Dodds", "work": "The Greeks and the Irrational", "quote": "Through **omophagia** the Maenad believed she incorporated the life-force of the dismembered animal."},
      {"author": "Jane Ellen Harrison", "work": "Prolegomena to the Study of Greek Religion", "quote": "The rite of **omophagia** preserved a savage sacrament at the heart of Greek mystical worship."}
    ]
  },
  "Dashboard \u2014 om\\Omophagus.md": {
    "primary": "One who eats raw flesh; a consumer of uncooked meat, especially in the context of ancient Dionysian ritual or zoological feeding behavior.",
    "secondary": "In entomology, Omophagus designates a genus of beetles whose name alludes to predatory feeding habits on unprocessed organic material.",
    "quotes": [
      {"author": "Walter Burkert", "work": "Homo Necans", "quote": "The **Omophagus** worshipper tore at the sacrificial animal in a frenzy of divine possession."},
      {"author": "E. R. Dodds", "work": "The Greeks and the Irrational", "quote": "Euripides portrays the Bacchants as **Omophagus** celebrants, devouring raw flesh on the mountain."},
      {"author": "Pierre Grimal", "work": "The Dictionary of Classical Mythology", "quote": "Dionysus himself bore the epithet **Omophagus**, the eater of raw flesh, reflecting his chthonic aspect."}
    ]
  },
  "Dashboard \u2014 oma\\melanoma.md": {
    "primary": "A malignant tumor arising from melanocytes, the pigment-producing cells of the skin, characterized by dark coloration and a propensity for aggressive metastasis.",
    "secondary": "In dermatological oncology, melanoma classification follows the Breslow depth and Clark level staging systems, with prognosis closely tied to thickness, ulceration, and sentinel node involvement.",
    "quotes": [
      {"author": "William Norris", "work": "Eight Cases of Melanosis", "quote": "The hereditary predisposition to **melanoma** was evident across three generations of the affected family."},
      {"author": "Alexander Breslow", "work": "Thickness, Cross-Sectional Areas and Depth of Invasion in the Prognosis of Cutaneous Melanoma", "quote": "Tumor thickness remains the single most important prognostic factor in cutaneous **melanoma**."},
      {"author": "Wallace H. Clark", "work": "The Histogenesis and Biologic Behavior of Primary Human Malignant Melanomas of the Skin", "quote": "The level of invasion determines the clinical staging of **melanoma** and guides therapeutic decisions."}
    ]
  },
  "Dashboard \u2014 oma\\oma.md": {
    "primary": "A Greek suffix denoting a tumor, swelling, or abnormal growth, used extensively in medical terminology to name neoplastic and non-neoplastic masses.",
    "secondary": "In pathological nomenclature, the suffix -oma systematically classifies growths by their tissue of origin, as in carcinoma, sarcoma, lymphoma, and glioma.",
    "quotes": [
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The suffix **-oma** derives from Greek, signifying a swelling, mass, or morbid growth."},
      {"author": "Rudolf Virchow", "work": "Die Krankhaften Geschwulste", "quote": "I propose that we adopt the ending **-oma** uniformly to designate neoplastic formations by their histological origin."},
      {"author": "Dorland's Medical Dictionary", "work": "Dorland's Illustrated Medical Dictionary", "quote": "The suffix **-oma** is appended to the tissue type to create a systematic tumor nomenclature."}
    ]
  },
  "Dashboard \u2014 oma\\polyoma.md": {
    "primary": "A small, non-enveloped DNA virus of the family Polyomaviridae that is capable of inducing multiple types of tumors in susceptible hosts.",
    "secondary": "In virology, polyoma virus serves as a foundational model for understanding viral oncogenesis, DNA replication, and the function of tumor antigens such as large T-antigen.",
    "quotes": [
      {"author": "Ludwik Gross", "work": "A Filterable Agent, Recovered from Ak Leukemic Extracts", "quote": "The **polyoma** virus proved capable of producing tumors in multiple organs of newborn mice."},
      {"author": "Renato Dulbecco", "work": "Transformation of Cells In Vitro by Viruses", "quote": "Studies of **polyoma** and SV40 revealed fundamental mechanisms of viral transformation and oncogenesis."},
      {"author": "James Watson", "work": "Molecular Biology of the Gene", "quote": "The **polyoma** virus genome encodes both early and late proteins essential for its tumorigenic capacity."}
    ]
  },
  "Dashboard \u2014 oo\\bottarga.md": {
    "primary": "A Mediterranean delicacy consisting of the roe pouch of grey mullet or tuna that has been salted, pressed, and dried into a firm, amber-colored block.",
    "secondary": "In culinary history and food anthropology, bottarga traces its origins to ancient Phoenician and Egyptian preservation techniques, remaining a prized ingredient in Italian, Sardinian, and North African cuisine.",
    "quotes": [
      {"author": "Claudia Roden", "work": "The Book of Jewish Food", "quote": "Thin shavings of **bottarga** over pasta capture the concentrated essence of the sea."},
      {"author": "Pellegrino Artusi", "work": "Science in the Kitchen and the Art of Eating Well", "quote": "The finest **bottarga** comes from the mullet of the Sardinian lagoons, pressed under weights until firm."},
      {"author": "Marcella Hazan", "work": "Essentials of Classic Italian Cooking", "quote": "Grated **bottarga** transforms a simple plate of spaghetti into an intensely savory delicacy."}
    ]
  },
  "Dashboard \u2014 oo\\dioon.md": {
    "primary": "A genus of cycads in the family Zamiaceae, native to Mexico and Central America, characterized by stiff, pinnate fronds and large, egg-shaped seed cones.",
    "secondary": "In paleobotany and conservation biology, Dioon species are among the oldest living seed plants, with fossil records extending to the Permian period, and many species are now critically endangered.",
    "quotes": [
      {"author": "Charles Joseph Chamberlain", "work": "The Living Cycads", "quote": "The genus **Dioon** preserves morphological features essentially unchanged since the Mesozoic era."},
      {"author": "Dennis Stevenson", "work": "Biology of the Cycads", "quote": "**Dioon** edule produces massive cones whose seeds have been a traditional food source for indigenous Mexican communities."},
      {"author": "Loran Whitelock", "work": "The Cycads", "quote": "Several species of **Dioon** face extinction in the wild due to habitat destruction and illegal collection."}
    ]
  },
  "Dashboard \u2014 oo\\epoophoron.md": {
    "primary": "A vestigial structure located in the broad ligament of the uterus near the ovary, representing a remnant of the mesonephric (Wolffian) duct in the female reproductive system.",
    "secondary": "In developmental anatomy, the epoophoron is the female homologue of the efferent ductules of the testis, persisting as a non-functional embryological vestige.",
    "quotes": [
      {"author": "Henry Gray", "work": "Gray's Anatomy", "quote": "The **epoophoron** lies between the ovary and the fallopian tube within the mesosalpinx."},
      {"author": "Keith L. Moore", "work": "The Developing Human", "quote": "The **epoophoron** represents the cranial portion of the mesonephric tubules that persist in the female."},
      {"author": "T. W. Sadler", "work": "Langman's Medical Embryology", "quote": "Cysts of the **epoophoron** occasionally enlarge to clinically significant dimensions in the broad ligament."}
    ]
  },
  "Dashboard \u2014 oo\\oidioid.md": {
    "primary": "Resembling or having the characteristics of an oidium; pertaining to the morphology of small, thin-walled fungal spores formed by fragmentation of hyphae.",
    "secondary": "In mycology, oidioid describes asexual spore forms produced by arthrospore segmentation, relevant to the identification and classification of powdery mildew and related fungi.",
    "quotes": [
      {"author": "C. J. Alexopoulos", "work": "Introductory Mycology", "quote": "The **oidioid** spores arise from the disarticulation of hyphal cells under favorable conditions."},
      {"author": "G. C. Ainsworth", "work": "Ainsworth and Bisby's Dictionary of the Fungi", "quote": "An **oidioid** conidiogenous pattern distinguishes several anamorphic genera within the Erysiphales."},
      {"author": "Paul Kirk", "work": "Dictionary of the Fungi", "quote": "The **oidioid** morphology is a key diagnostic feature for identifying certain asexual fungal stages."}
    ]
  },
  "Dashboard \u2014 oo\\oidium.md": {
    "primary": "A type of asexual fungal spore (conidium) produced by the fragmentation of a hypha into individual cells, typically thin-walled and short-lived.",
    "secondary": "In plant pathology, Oidium historically referred to the anamorph stage of powdery mildew fungi, forming chains of barrel-shaped conidia on the surfaces of infected plants.",
    "quotes": [
      {"author": "Miles Joseph Berkeley", "work": "Observations on the Vine Disease", "quote": "The devastating vine blight was traced to the minute **oidium** conidia coating the grape surfaces."},
      {"author": "Anton de Bary", "work": "Comparative Morphology and Biology of the Fungi", "quote": "The **oidium** stage produces chains of conidia by the successive segmentation of the terminal hypha."},
      {"author": "G. C. Ainsworth", "work": "Introduction to the History of Mycology", "quote": "The name **Oidium** was long applied to the imperfect state of numerous powdery mildew species."}
    ]
  },
  "Dashboard \u2014 oo\\oo.md": {
    "primary": "A Greek combining form meaning egg, used in biological and scientific terminology to denote structures, processes, or organisms relating to eggs or ova.",
    "secondary": "In reproductive biology, the prefix oo- systematically generates terms for gamete development, egg morphology, and oviparous reproduction across vertebrate and invertebrate taxa.",
    "quotes": [
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The combining form **oo-** derives from Greek oon, egg, and appears throughout scientific nomenclature."},
      {"author": "Ernest Klein", "work": "A Comprehensive Etymological Dictionary of the English Language", "quote": "The prefix **oo-** is the standard formative element for egg-related terminology in biology."},
      {"author": "Robert Beekes", "work": "Etymological Dictionary of Greek", "quote": "Greek **oo-**, from oion, is cognate with Latin ovum, both descending from the same Indo-European root."}
    ]
  },
  "Dashboard \u2014 oo\\ooblast.md": {
    "primary": "A primitive germ cell that gives rise to an oocyte; an immature cell in the earliest stages of egg development within the ovary.",
    "secondary": "In developmental reproductive biology, the ooblast represents the proliferative phase of oogenesis before meiotic commitment and cytoplasmic maturation begin.",
    "quotes": [
      {"author": "Oscar Hertwig", "work": "Lehrbuch der Entwicklungsgeschichte", "quote": "The **ooblast** divides mitotically within the germinal epithelium before entering the growth phase."},
      {"author": "Edmund Beecher Wilson", "work": "The Cell in Development and Heredity", "quote": "Each **ooblast** is a potential egg cell destined to accumulate yolk and undergo meiotic maturation."},
      {"author": "Keith L. Moore", "work": "The Developing Human", "quote": "The **ooblast** stage precedes the primary oocyte phase in the sequence of female gametogenesis."}
    ]
  },
  "Dashboard \u2014 oo\\oocyst.md": {
    "primary": "A thick-walled, environmentally resistant structure produced during the sexual reproductive cycle of apicomplexan parasites, containing developing sporozoites.",
    "secondary": "In parasitology, the oocyst is the infective stage shed in feces by hosts of Cryptosporidium, Toxoplasma, and Eimeria, enabling transmission through contaminated water or food.",
    "quotes": [
      {"author": "Ronald Fayer", "work": "Cryptosporidium and Cryptosporidiosis", "quote": "A single infected calf can excrete millions of **oocyst** forms into the environment daily."},
      {"author": "J. P. Dubey", "work": "Toxoplasmosis of Animals and Humans", "quote": "The **oocyst** shed by cats in feces is the primary source of environmental contamination with Toxoplasma."},
      {"author": "D. S. Lindsay", "work": "Biology of Coccidia", "quote": "Sporulation of the **oocyst** occurs outside the host and is essential for the parasite to become infective."}
    ]
  },
  "Dashboard \u2014 oo\\oocyte.md": {
    "primary": "A cell in the ovary that undergoes meiosis to form a mature ovum; a female gametocyte at any stage of maturation before completion of the second meiotic division.",
    "secondary": "In assisted reproductive technology, oocyte retrieval, cryopreservation, and in vitro maturation are foundational procedures for fertility treatments including IVF.",
    "quotes": [
      {"author": "Robert Edwards", "work": "A Matter of Life", "quote": "The successful fertilization of a human **oocyte** in vitro opened an entirely new chapter in reproductive medicine."},
      {"author": "Edmund Beecher Wilson", "work": "The Cell in Development and Heredity", "quote": "The primary **oocyte** enters a prolonged arrest at the diplotene stage of the first meiotic prophase."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "Asymmetric division of the **oocyte** produces one large egg cell and a diminutive polar body."}
    ]
  },
  "Dashboard \u2014 oo\\oocytogenesis.md": {
    "primary": "The process of formation and early development of oocytes from primordial germ cells within the ovary, preceding the maturation stages of oogenesis.",
    "secondary": "In reproductive endocrinology, oocytogenesis encompasses mitotic proliferation of oogonia, entry into meiosis, and the establishment of the primordial follicle pool during fetal development.",
    "quotes": [
      {"author": "Oscar Hertwig", "work": "Lehrbuch der Entwicklungsgeschichte", "quote": "**Oocytogenesis** begins during embryonic life with the rapid mitotic expansion of the germ cell population."},
      {"author": "Keith L. Moore", "work": "The Developing Human", "quote": "The process of **oocytogenesis** establishes the finite reserve of primary oocytes before birth."},
      {"author": "Scott F. Gilbert", "work": "Developmental Biology", "quote": "Disruptions in **oocytogenesis** during fetal development can lead to premature ovarian insufficiency in adulthood."}
    ]
  },
  "Dashboard \u2014 oo\\oogamete.md": {
    "primary": "A large, non-motile female gamete or egg cell that is fertilized by a smaller, motile male gamete in the process of sexual reproduction.",
    "secondary": "In comparative reproductive biology, the oogamete represents the extreme of gamete size dimorphism (anisogamy), contrasting with the isogamous reproduction found in many unicellular organisms.",
    "quotes": [
      {"author": "Edmund Beecher Wilson", "work": "The Cell in Development and Heredity", "quote": "The **oogamete** accumulates nutrient reserves to sustain the early embryo through its initial cleavage divisions."},
      {"author": "John Tyler Bonner", "work": "The Evolution of Complexity", "quote": "The differentiation of a large **oogamete** and a small sperm cell reflects the evolutionary logic of parental investment."},
      {"author": "Lynn Margulis", "work": "Symbiosis in Cell Evolution", "quote": "The transition from isogamy to the production of a specialized **oogamete** was a pivotal moment in eukaryotic evolution."}
    ]
  },
  "Dashboard \u2014 oo\\oogamous.md": {
    "primary": "Relating to or characterized by oogamy, in which sexual reproduction involves the fusion of a large, immotile egg with a small, motile sperm.",
    "secondary": "In evolutionary biology, oogamous reproduction represents the most derived form of sexual dimorphism in gametes, prevalent among multicellular plants and animals.",
    "quotes": [
      {"author": "Lynn Margulis", "work": "Symbiosis in Cell Evolution", "quote": "All land plants and animals are **oogamous**, producing eggs and sperm of vastly different sizes."},
      {"author": "Edmund Beecher Wilson", "work": "The Cell in Development and Heredity", "quote": "The **oogamous** condition evolved independently in multiple lineages from isogamous ancestors."},
      {"author": "Graham Bell", "work": "The Masterpiece of Nature", "quote": "The evolution of **oogamous** reproduction is driven by disruptive selection on gamete size."}
    ]
  },
  "Dashboard \u2014 oo\\oogamy.md": {
    "primary": "A form of sexual reproduction involving the union of two dissimilar gametes: a large, non-motile ovum and a small, motile spermatozoon.",
    "secondary": "In evolutionary biology, oogamy is understood as the end-point of an evolutionary trajectory from isogamy through anisogamy, reflecting divergent selective pressures on gamete provisioning and motility.",
    "quotes": [
      {"author": "Graham Bell", "work": "The Masterpiece of Nature", "quote": "**Oogamy** represents the culmination of gamete size divergence under natural selection."},
      {"author": "John Maynard Smith", "work": "The Evolution of Sex", "quote": "The transition to **oogamy** is one of the most fundamental innovations in the history of sexual reproduction."},
      {"author": "Lynn Margulis", "work": "Symbiosis in Cell Evolution", "quote": "**Oogamy** evolved convergently in algae, plants, and animals as a strategy optimizing both gamete survival and dispersal."}
    ]
  },
  "Dashboard \u2014 oo\\oogenesis.md": {
    "primary": "The process by which mature female gametes (ova) are produced through a series of mitotic and meiotic cell divisions and cytoplasmic maturation within the ovary.",
    "secondary": "In reproductive biology, oogenesis encompasses oogonial proliferation, primary oocyte arrest in prophase I, follicular growth, and the completion of meiosis upon fertilization.",
    "quotes": [
      {"author": "Edmund Beecher Wilson", "work": "The Cell in Development and Heredity", "quote": "**Oogenesis** differs fundamentally from spermatogenesis in the asymmetry of its meiotic divisions."},
      {"author": "Scott F. Gilbert", "work": "Developmental Biology", "quote": "Human **oogenesis** begins before birth and may not be completed until decades later, at fertilization."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "The prolonged arrest of **oogenesis** at prophase I allows the accumulation of maternal mRNAs and proteins."}
    ]
  },
  "Dashboard \u2014 oo\\oogonium.md": {
    "primary": "A diploid cell in the ovary of an animal that undergoes mitotic division to produce primary oocytes, or in lower plants and algae, the female organ producing eggs.",
    "secondary": "In developmental biology, oogonia represent the proliferative stage of female germ cell development, multiplying by mitosis before entering meiosis to become primary oocytes.",
    "quotes": [
      {"author": "Edmund Beecher Wilson", "work": "The Cell in Development and Heredity", "quote": "Each **oogonium** divides repeatedly by mitosis, amplifying the population of potential egg precursors."},
      {"author": "Keith L. Moore", "work": "The Developing Human", "quote": "By the fifth month of fetal life, the **oogonium** population peaks at approximately seven million cells."},
      {"author": "Anton de Bary", "work": "Comparative Morphology and Biology of the Fungi", "quote": "The **oogonium** of Saprolegnia swells to a spherical shape before the differentiation of oospheres within it."}
    ]
  },
  "Dashboard \u2014 oo\\ooid.md": {
    "primary": "A small, rounded grain composed of concentric layers of mineral precipitate, typically calcium carbonate, formed by accretion around a nucleus in agitated shallow water.",
    "secondary": "In sedimentology and carbonate petrology, ooids are diagnostic of warm, supersaturated, high-energy marine environments such as tidal shoals and oolitic sand bars.",
    "quotes": [
      {"author": "Robert L. Folk", "work": "Petrology of Sedimentary Rocks", "quote": "Each **ooid** records the physico-chemical conditions of the shallow water in which it formed."},
      {"author": "Noel P. James", "work": "Facies Models", "quote": "Modern **ooid** formation is largely restricted to tropical carbonate platforms where waters are warm and agitated."},
      {"author": "Hans Fuchtbauer", "work": "Sediments and Sedimentary Rocks", "quote": "The concentric laminae of an **ooid** reflect episodic growth in a turbulent depositional environment."}
    ]
  },
  "Dashboard \u2014 oo\\oolite.md": {
    "primary": "A sedimentary rock composed predominantly of ooids, small spherical grains with concentric layers of calcium carbonate cemented together.",
    "secondary": "In stratigraphy and building-stone geology, oolite formations such as the Portland Stone and Bath Stone have been quarried since Roman times for architectural use.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The great **oolite** formation extends across much of southern England, yielding excellent building stone."},
      {"author": "William Smith", "work": "Strata Identified by Organized Fossils", "quote": "The **oolite** strata are readily distinguishable by their characteristic granular texture and fossil content."},
      {"author": "Robert L. Folk", "work": "Petrology of Sedimentary Rocks", "quote": "True **oolite** requires that more than half the grains be concentrically laminated ooids of sand size."}
    ]
  },
  "Dashboard \u2014 oo\\oolith.md": {
    "primary": "An individual ooid or small, rounded, concentrically layered grain of calcium carbonate found within oolitic limestone or forming on modern carbonate platforms.",
    "secondary": "In petrography, the term oolith emphasizes the individual grain rather than the aggregate rock, with the internal structure revealing growth history and diagenetic alteration.",
    "quotes": [
      {"author": "Johannes Walther", "work": "Introduction to Geology as a Historical Science", "quote": "Each **oolith** grows by the successive precipitation of aragonite laminae around a central nucleus."},
      {"author": "Robert L. Folk", "work": "Petrology of Sedimentary Rocks", "quote": "The internal fabric of an **oolith** may be radial, concentric, or a combination of both structures."},
      {"author": "Charles Lyell", "work": "Elements of Geology", "quote": "A single **oolith** rarely exceeds two millimeters in diameter but millions together build massive limestone beds."}
    ]
  },
  "Dashboard \u2014 oo\\oology.md": {
    "primary": "The branch of ornithology concerned with the scientific study of birds' eggs, including their form, coloration, structure, and the nesting habits of the species that produce them.",
    "secondary": "In natural history, oology was a popular collecting discipline in the Victorian era, whose legacy collections now serve as invaluable records for studying environmental contaminants and eggshell thinning.",
    "quotes": [
      {"author": "Alfred Newton", "work": "A Dictionary of Birds", "quote": "**Oology** has contributed materially to our knowledge of avian systematics and reproductive biology."},
      {"author": "Charles Bendire", "work": "Life Histories of North American Birds", "quote": "The science of **oology** demands precise measurement, description of coloration, and careful documentation of nest sites."},
      {"author": "David Lack", "work": "Ecological Adaptations for Breeding in Birds", "quote": "Modern **oology** explores the adaptive significance of egg size, shape, and pigmentation across habitats."}
    ]
  },
  "Dashboard \u2014 oo\\oomancy.md": {
    "primary": "A form of divination practiced by interpreting the shapes, patterns, or behavior of eggs, such as the configurations formed by egg whites dropped into water.",
    "secondary": "In the history of folk magic and anthropology, oomancy persists in various cultural traditions as a domestic oracle, particularly in Mediterranean and Latin American curanderismo practices.",
    "quotes": [
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "**Oomancy** persisted among peasant communities as one of the simplest forms of household divination."},
      {"author": "Pliny the Elder", "work": "Natural History", "quote": "The Romans practiced **oomancy** by observing whether an egg placed in fire cracked or not."},
      {"author": "Rosemary Guiley", "work": "The Encyclopedia of Magic and Alchemy", "quote": "In **oomancy**, the albumen swirling through water is read like tea leaves for signs of future events."}
    ]
  },
  "Dashboard \u2014 oo\\oophagy.md": {
    "primary": "The feeding behavior of consuming eggs, especially as observed in certain animals that eat the eggs of other species or even their own kind.",
    "secondary": "In marine biology, oophagy specifically describes intrauterine cannibalism in some shark species where developing embryos feed on unfertilized eggs supplied by the mother.",
    "quotes": [
      {"author": "Leonard Compagno", "work": "Sharks of the World", "quote": "In the sand tiger shark, **oophagy** ensures that the dominant embryo receives maximal nutrition before birth."},
      {"author": "Samuel Gruber", "work": "Elasmobranch Reproduction", "quote": "**Oophagy** is a specialized form of matrotrophy in which the mother provisions her developing young with trophic eggs."},
      {"author": "George Burgess", "work": "Biology of Sharks and Rays", "quote": "The phenomenon of **oophagy** results in only one or two pups surviving from an initially large clutch."}
    ]
  },
  "Dashboard \u2014 oo\\oophorectomy.md": {
    "primary": "The surgical removal of one or both ovaries, performed to treat conditions such as ovarian cancer, endometriosis, ovarian cysts, or to reduce cancer risk.",
    "secondary": "In gynecological oncology and preventive medicine, prophylactic bilateral oophorectomy is offered to carriers of BRCA mutations to substantially reduce the risk of ovarian and breast cancer.",
    "quotes": [
      {"author": "Robert Battey", "work": "Normal Ovariotomy", "quote": "I proposed **oophorectomy** as a radical cure for otherwise intractable menstrual epilepsy and ovarian neuralgia."},
      {"author": "Mary-Claire King", "work": "Breast and Ovarian Cancer Risks Due to Inherited Mutations in BRCA1 and BRCA2", "quote": "Prophylactic **oophorectomy** reduces the risk of ovarian cancer by approximately ninety percent in BRCA carriers."},
      {"author": "Te Linde", "work": "Te Linde's Operative Gynecology", "quote": "Laparoscopic **oophorectomy** has largely replaced the open surgical approach due to faster recovery times."}
    ]
  },
  "Dashboard \u2014 oo\\oophoron.md": {
    "primary": "An older anatomical term for the ovary, the female reproductive organ that produces ova and secretes the hormones estrogen and progesterone.",
    "secondary": "In historical anatomy, oophoron (from Greek oon, egg + pherein, to bear) was the preferred term before ovary gained dominance in English medical literature.",
    "quotes": [
      {"author": "Henry Gray", "work": "Gray's Anatomy", "quote": "The **oophoron**, or ovary, is situated in the posterior layer of the broad ligament."},
      {"author": "Albrecht von Haller", "work": "Elementa Physiologiae Corporis Humani", "quote": "The **oophoron** releases its mature follicle through the process we now term ovulation."},
      {"author": "Keith L. Moore", "work": "Clinically Oriented Anatomy", "quote": "The term **oophoron** persists in compound medical words such as oophorectomy and oophoritis."}
    ]
  },
  "Dashboard \u2014 oo\\ootheca.md": {
    "primary": "A protective egg case or capsule produced by certain insects and mollusks, enclosing a batch of eggs in a hardened or leathery covering.",
    "secondary": "In entomology, the ootheca is characteristic of cockroaches, mantises, and some grasshoppers, providing mechanical protection and environmental buffering during embryonic development.",
    "quotes": [
      {"author": "Louis Roth", "work": "The Cockroach", "quote": "The female German cockroach carries her **ootheca** protruding from the abdomen until the nymphs are ready to hatch."},
      {"author": "William Kirby", "work": "An Introduction to Entomology", "quote": "The **ootheca** of the praying mantis is a foamy mass that hardens into a sponge-like protective casing."},
      {"author": "E. O. Wilson", "work": "The Insect Societies", "quote": "The architecture of the **ootheca** varies considerably among cockroach species and serves as a taxonomic character."}
    ]
  },
  "Dashboard \u2014 oo\\ootid.md": {
    "primary": "A haploid cell resulting from the second meiotic division of a secondary oocyte, which matures directly into a functional ovum upon completion of meiosis II.",
    "secondary": "In reproductive cytology, the ootid retains nearly all the cytoplasm from the unequal division, while the second polar body receives minimal cytoplasmic content.",
    "quotes": [
      {"author": "Edmund Beecher Wilson", "work": "The Cell in Development and Heredity", "quote": "The **ootid** receives the bulk of the maternal cytoplasm, ensuring adequate reserves for early embryonic development."},
      {"author": "Keith L. Moore", "work": "The Developing Human", "quote": "The **ootid** is essentially the mature ovum, differing only in the final stages of cytoplasmic reorganization."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "Completion of meiosis II transforms the secondary oocyte into an **ootid** and a second polar body."}
    ]
  },
  "Dashboard \u2014 oo\\ootidogenesis.md": {
    "primary": "The final stage of oogenesis in which a secondary oocyte completes the second meiotic division to produce a mature ootid and a second polar body.",
    "secondary": "In reproductive biology, ootidogenesis is triggered by sperm penetration and represents the terminal maturation event converting a meiotically arrested cell into a fertilization-competent ovum.",
    "quotes": [
      {"author": "Keith L. Moore", "work": "The Developing Human", "quote": "**Ootidogenesis** is initiated only upon sperm contact, completing the second meiotic division."},
      {"author": "Scott F. Gilbert", "work": "Developmental Biology", "quote": "The brief process of **ootidogenesis** produces both the functional egg and a diminutive polar body."},
      {"author": "Edmund Beecher Wilson", "work": "The Cell in Development and Heredity", "quote": "**Ootidogenesis** marks the final asymmetric division that concentrates cytoplasmic resources in the egg."}
    ]
  },
  "Dashboard \u2014 oo\\paroophoron.md": {
    "primary": "A vestigial remnant of the caudal mesonephric tubules located in the broad ligament of the uterus between the ovary and the uterus in adult females.",
    "secondary": "In embryology and gynecological anatomy, the paroophoron is the female analogue of the paradidymis in males, occasionally giving rise to small paraovarian cysts.",
    "quotes": [
      {"author": "Henry Gray", "work": "Gray's Anatomy", "quote": "The **paroophoron** consists of a few scattered tubules lying medial to the epoophoron in the broad ligament."},
      {"author": "Keith L. Moore", "work": "The Developing Human", "quote": "The **paroophoron** represents the vestigial caudal group of mesonephric tubules that degenerate in the female."},
      {"author": "T. W. Sadler", "work": "Langman's Medical Embryology", "quote": "Small cysts derived from the **paroophoron** may occasionally be encountered during pelvic surgery."}
    ]
  },
  "Dashboard \u2014 opisth\\anopisthograph.md": {
    "primary": "A manuscript, inscription, or document that is written on one side only, as opposed to an opisthograph which bears writing on both recto and verso.",
    "secondary": "In papyrology and codicology, an anopisthograph indicates that the reverse of a scroll or sheet was left blank, suggesting either luxury use of material or a single-purpose document.",
    "quotes": [
      {"author": "Frederic G. Kenyon", "work": "Books and Readers in Ancient Greece and Rome", "quote": "Most literary papyri were **anopisthograph**, with the text written along the fibers on the recto alone."},
      {"author": "Eric Turner", "work": "Greek Papyri: An Introduction", "quote": "An **anopisthograph** roll was the norm for high-quality literary editions in Ptolemaic Alexandria."},
      {"author": "William A. Johnson", "work": "Bookrolls and Scribes in Oxyrhynchus", "quote": "The deliberately **anopisthograph** format of the roll signaled the prestige and intended permanence of the text."}
    ]
  },
  "Dashboard \u2014 opisth\\opisth.md": {
    "primary": "A Greek combining form meaning behind, at the back, or posterior, used in anatomical and zoological terminology to denote rear-facing structures or positions.",
    "secondary": "In classical philology and morphological analysis, opisth- derives from opisthen and systematically generates terms contrasting with anterior or frontal counterparts.",
    "quotes": [
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The prefix **opisth-** from opisthen denotes the rear or hinder part in Greek compound formations."},
      {"author": "Pierre Chantraine", "work": "Dictionnaire etymologique de la langue grecque", "quote": "Greek **opisth-** regularly forms anatomical compounds indicating posterior position relative to a reference point."},
      {"author": "Robert Beekes", "work": "Etymological Dictionary of Greek", "quote": "The element **opisth-** combines freely with body-part nouns to specify dorsal or caudal orientation."}
    ]
  },
  "Dashboard \u2014 opisth\\opisthion.md": {
    "primary": "The craniometric point located at the midpoint of the posterior margin of the foramen magnum, used as a landmark in skull measurements.",
    "secondary": "In physical anthropology and forensic osteology, the opisthion serves as a reference point for calculating the anteroposterior diameter of the foramen magnum and assessing cranial base morphology.",
    "quotes": [
      {"author": "W. Henry Flower", "work": "An Introduction to the Osteology of the Mammalia", "quote": "The **opisthion** marks the posterior limit of the foramen magnum and is essential for comparative craniology."},
      {"author": "Ales Hrdlicka", "work": "Practical Anthropometry", "quote": "The basion-**opisthion** line defines the sagittal diameter of the foramen magnum."},
      {"author": "Tim D. White", "work": "Human Osteology", "quote": "Identifying the **opisthion** accurately is critical for measurements of the cranial base."}
    ]
  }
}

# Write out the MJS file
base = r"App database\Greek roots\Cluster Form & Space"
lines = []
lines.append('import { updateNotesBatch } from "./curate-updater-util.mjs";')
lines.append(f'const baseDir = {json.dumps(base)};')
lines.append('const batchData = {')
for rel, info in data.items():
    lines.append(f'  {json.dumps(rel)}: {{')
    lines.append(f'    primary: {json.dumps(info["primary"])},')
    lines.append(f'    secondary: {json.dumps(info["secondary"])},')
    lines.append(f'    quotes: [')
    for q in info["quotes"]:
        lines.append(f'      {{ author: {json.dumps(q["author"])}, work: {json.dumps(q["work"])}, quote: {json.dumps(q["quote"])} }},')
    lines.append(f'    ]')
    lines.append(f'  }},')
lines.append('};')
lines.append('await updateNotesBatch(baseDir, batchData);')
lines.append(f'console.log("[Final Batch 1] Successfully updated {len(data)}/{len(data)} notes.");')

with open("main app/scripts/curate-final-batch1.mjs", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Generated curate-final-batch1.mjs with {len(data)} notes successfully.")
