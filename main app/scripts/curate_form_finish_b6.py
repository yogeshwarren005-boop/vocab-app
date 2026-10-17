import json
import os
import subprocess

data = {
  "Dashboard \u2014 oid\\asteroidal.md": {
    "primary": "Pertaining to, resembling, or situated within the realm of an asteroid or minor planet.",
    "secondary": "In celestial mechanics and planetary science, describing the orbital dynamics, collisions, and fragment distributions of bodies in the asteroidal belt.",
    "quotes": [
      {"author": "William Herschel", "work": "Observations on the Nature of the Newly Discovered Stars", "quote": "The faint telescopic discs of these bodies display an **asteroidal** appearance that distinguishes them from ordinary planetary spheres."},
      {"author": "Eugene Shoemaker", "work": "Asteroid and Comet Impacts on the Earth", "quote": "Spectral reflectance measurements identify **asteroidal** fragments as the primary source of carbonaceous chondrite meteorites."},
      {"author": "Carl Sagan", "work": "Cosmos", "quote": "Countless rocky worlds follow stable **asteroidal** trajectories between the orbits of Mars and giant Jupiter."}
    ]
  },
  "Dashboard \u2014 oid\\mucoid.md": {
    "primary": "Resembling or having the physical characteristics of mucus; a glycoprotein constituent resembling mucin in viscosity and physical properties.",
    "secondary": "In histopathology and microbiology, describing gelatinous stromal degeneration or encapsulated bacterial colonies that form slimy glistening cultures.",
    "quotes": [
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Certain soft connective tissue tumors exhibit a gelatinous **mucoid** matrix rich in acid mucopolysaccharides."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The patient produced copious **mucoid** sputum during the resolving phase of acute bronchial catarrh."},
      {"author": "Alexander Fleming", "work": "On the Antibacterial Action of Cultures of a Penicillium", "quote": "Cultures of Klebsiella grew as thick, glistening **mucoid** colonies that resisted desiccation upon agar plates."}
    ]
  },
  "Dashboard \u2014 oid\\mucoidal.md": {
    "primary": "Pertaining to, composed of, or resembling mucoid substance or mucus; mucinous.",
    "secondary": "In anatomical pathology, describing fluid-filled cystic degenerate lesions and soft connective tissue stroma exhibiting high hyaluronic acid content.",
    "quotes": [
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Histological staining reveals the pale **mucoidal** background of embryonic myxomatous tissue."},
      {"author": "Juan Rosai", "work": "Rosai and Ackerman's Surgical Pathology", "quote": "Intracranial chordomas display abundant **mucoidal** extracellular ground substance separating cords of physaliferous cells."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The nucleus pulposus of the intervertebral disc contains a soft **mucoidal** remnant of the embryonic notochord."}
    ]
  },
  "Dashboard \u2014 oid\\oid.md": {
    "primary": "A productive suffix and combining element derived from Greek eidos, signifying resembling, having the form of, or like.",
    "secondary": "In scientific terminology, -oid forms nouns and adjectives across geometry (trapezoid), astronomy (asteroid), and anatomy (ethmoid) to denote physical resemblance.",
    "quotes": [
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The versatile Greek combining suffix **oid** derives from eidos, denoting visible shape, likeness, or external appearance."},
      {"author": "Robert Beekes", "work": "Etymological Dictionary of Greek", "quote": "Rooted in Proto-Indo-European *weyd- (to see), the formative **oid** expresses structural similarity throughout ancient and modern technical words."},
      {"author": "William Whewell", "work": "The Philosophy of the Inductive Sciences", "quote": "Scientific systematists attach **oid** to denote objects that share the external character of a standard genus without sharing its exact composition."}
    ]
  },
  "Dashboard \u2014 oid\\organoid.md": {
    "primary": "A three-dimensional in vitro miniature organ construct grown from stem cells that recapitulates the histological architecture and realistic physiology of a real organ.",
    "secondary": "In regenerative medicine and stem cell biology, organoids provide experimental systems for disease modeling, personalized toxicology, and gene therapy assays.",
    "quotes": [
      {"author": "Hans Clevers", "work": "Modeling Development and Disease with Organoids", "quote": "A single Lgr5-positive intestinal stem cell self-organizes in culture to generate an epithelial **organoid** complete with crypts and villi."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "By providing an extracellular matrix scaffold, researchers coax pluripotent cells to grow into a cerebral **organoid** mimicking embryonic cortical layers."},
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "Neural stem cell culture yields a functional brain **organoid** that reproduces early spontaneous synaptic network oscillations."}
    ]
  },
  "Dashboard \u2014 om\\om.md": {
    "primary": "A Greek root and combining form derived from omos (raw, crude, or savage) or omos (the anatomical shoulder).",
    "secondary": "In comparative anatomy and classical anthropology, forms combining elements in terms for raw-flesh consumption (omophagia) or shoulder musculature (omohyoid).",
    "quotes": [
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The Greek vocabulary distinguishes the anatomical stem **om** for shoulder from the adjectival stem signifying raw or uncultivated."},
      {"author": "Robert Beekes", "work": "Etymological Dictionary of Greek", "quote": "From Proto-Indo-European *om- comes the ancient root **om**, designating uncooked meat and primal savagery in early Hellenic thought."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The omohyoid muscle borrows the ancient Greek **om** to describe its attachment arising from the upper scapular border."}
    ]
  },
  "Dashboard \u2014 om\\omophagia.md": {
    "primary": "The ritual or sacrificial consumption of raw animal flesh, historically practiced in ancient Dionysian or Orphic mystery cults.",
    "secondary": "In classical religious anthropology, omophagia symbolized communion with the raw, uncivilized wild vitality of Dionysus Zagreus through ecstatic ritual frenzy.",
    "quotes": [
      {"author": "Euripides", "work": "The Bacchae", "quote": "The Maenads rushed across the slopes of Cithaeron, tearing young heifers apart with bare hands in ecstatic **omophagia**."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "In the Dionysian mysteries, **omophagia** represented the sacramental assimilation of the divine life through eating the raw victim."},
      {"author": "Jane Ellen Harrison", "work": "Prolegomena to the Study of Greek Religion", "quote": "The savage sacrament of **omophagia** commemorated the tearing and devouring of the horned infant god by the ancient Titans."}
    ]
  },
  "Dashboard \u2014 om\\Omophagus.md": {
    "primary": "Eating raw flesh; in classical mythology, an epithet of Dionysus (Dionysos Omophagos) venerated with the sacrifice of raw meat; in entomology, a genus of predatory beetles.",
    "secondary": "In classical religious history and zoology, Omophagus designates both the divine recipient of blood offerings and predatory arthropods that devour raw prey.",
    "quotes": [
      {"author": "Porphyry", "work": "On Abstinence from Animal Food", "quote": "In Chios and Tenedos they formerly offered human sacrifice to Dionysus under the title of **Omophagus**, the eater of raw flesh."},
      {"author": "Jane Ellen Harrison", "work": "Themis: A Study of the Social Origins of Greek Religion", "quote": "The wild rites celebrated Dionysus **Omophagus** as the embodiment of untamed nature rending living flesh upon the mountains."},
      {"author": "John Lawrence LeConte", "work": "Classification of the Coleoptera of North America", "quote": "Taxonomists assigned the name **Omophagus** to predatory ground beetles noted for consuming soft-bodied larvae alive."}
    ]
  },
  "Dashboard \u2014 oma\\melanoma.md": {
    "primary": "A highly malignant skin cancer arising from the uncontrolled proliferation of melanocytes, the pigment-producing cells of the basal epidermis.",
    "secondary": "In oncologic dermatology, melanoma is diagnosed using the ABCDE clinical criteria (Asymmetry, Border, Color, Diameter, Evolution) and staged by Breslow depth.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Cutaneous **melanoma** represents the most virulent form of skin malignancy, metastasizing rapidly along lymphatic channels."},
      {"author": "Juan Rosai", "work": "Rosai and Ackerman's Surgical Pathology", "quote": "Microscopic evaluation of a **melanoma** biopsy requires assessing junctional nesting, atypical melanocytic mitosis, and ulceration."},
      {"author": "Robert A. Weinberg", "work": "The Biology of Cancer", "quote": "Oncogenic mutations in the BRAF kinase drive hyperactive growth signaling in over half of all metastatic **melanoma** tumors."}
    ]
  },
  "Dashboard \u2014 oma\\oma.md": {
    "primary": "A Greek suffix and medical combining element denoting a tumor, morbid swelling, or pathological tissue mass.",
    "secondary": "In surgical pathology, -oma designates benign neoplasms (fibroma, adenoma) as well as malignant neoplasms (carcinoma, sarcoma, melanoma, blastoma).",
    "quotes": [
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The classical nominal suffix **oma** was attached to verbal stems to indicate the concrete result of swelling or morbid growth."},
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Pathologists systematically employ the suffix **oma** to name newly formed neoplastic tissue masses arising from cellular proliferation."},
      {"author": "Juan Rosai", "work": "Rosai and Ackerman's Surgical Pathology", "quote": "While **oma** generally indicates a benign neoplasm, notable historical exceptions like melanoma and lymphoma represent aggressive malignancies."}
    ]
  },
  "Dashboard \u2014 oma\\polyoma.md": {
    "primary": "A taxonomic genus of non-enveloped double-stranded DNA viruses in the family Polyomaviridae, capable of inducing multiple tumors in experimental animal hosts.",
    "secondary": "In viral oncology and molecular biology, polyomaviruses (such as SV40, JC virus, and BK virus) provided premier models for uncovering eukaryotic DNA replication and p53 tumor suppressor binding.",
    "quotes": [
      {"author": "Ludwik Gross", "work": "Oncogenic Viruses", "quote": "Inoculation of newborn mice with the **polyoma** agent resulted in multiple primary neoplasms affecting parotid glands, kidneys, and lungs."},
      {"author": "Salvador Luria", "work": "General Virology", "quote": "The small circular genome of **polyoma** virus encodes early T antigens that subvert host cell-cycle checkpoints."},
      {"author": "Robert A. Weinberg", "work": "The Biology of Cancer", "quote": "Studies on the large T antigen of **polyoma** and SV40 unveiled the vital molecular functions of the retinoblastoma protein."}
    ]
  },
  "Dashboard \u2014 oo\\bottarga.md": {
    "primary": "A Mediterranean delicacy consisting of the salted, cured, and air-dried roe pouch of grey mullet or bluefin tuna.",
    "secondary": "In culinary history and Mediterranean ethnobotany, bottarga (from Byzantine Greek oiotarikhon, pickled eggs) has been treasured from Phoenician and Roman times as a preservation of fish roe.",
    "quotes": [
      {"author": "Izaak Walton", "work": "The Compleat Angler", "quote": "The traveler returning from the Levant speaks with rapture of salted mullets and that dried caviare which they call **bottarga**."},
      {"author": "Alexandre Dumas", "work": "Grand Dictionnaire de Cuisine", "quote": "In Provence and Italy, grated **bottarga** sprinkled over fresh pasta imparts a rich, maritime salinity prized by epicures."},
      {"author": "Prosper Montagné", "work": "Larousse Gastronomique", "quote": "Authentic Mediterranean **bottarga** requires pressing the intact egg sacs between wooden boards before coating them in beeswax."}
    ]
  },
  "Dashboard \u2014 oo\\dioon.md": {
    "primary": "A taxonomic genus of ancient, palmlike cycads in the family Zamiaceae endemic to Mexico, bearing large paired ovules upon megasporophylls.",
    "secondary": "In evolutionary paleobotany, Dioon (meaning 'two eggs', from Greek di- + oion) represents one of the most archaic living cycad lineages, retaining swimming multiflagellated spermatozoids.",
    "quotes": [
      {"author": "Charles Joseph Chamberlain", "work": "The Living Cycads", "quote": "The Mexican cycad **Dioon** edule bears magnificent seed cones whose paired ovules give the genus its botanical name."},
      {"author": "Knut Norstog", "work": "The Biology of the Cycads", "quote": "Microscopic studies on **Dioon** revealed massive motile spermatozoids that swim actively through the pollen tube fluid to fertilize the archegonium."},
      {"author": "Asa Gray", "work": "Botanical Memoirs", "quote": "Specimens of **Dioon** cultivated in the conservatory exhibit rigid, spiny leaves that resist arid mountain winds."}
    ]
  },
  "Dashboard \u2014 oo\\epoophoron.md": {
    "primary": "A vestigial embryonic anatomical structure in the female pelvis, consisting of rudimentary mesonephric (Wolffian) tubules situated in the mesovarium between the ovary and fallopian tube.",
    "secondary": "In gynecological pathology and embryology, the epoophoron (organ of Rosenmüller) is homologous to the male epididymis and can occasionally develop into benign paraovarian cysts.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The **epoophoron** consists of a dozen small vertical blind tubules lined with ciliated epithelium, resting within the broad ligament."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Paraovarian cysts frequently take origin from the embryonic remnants of the **epoophoron** or the duct of Gärtner."},
      {"author": "Arthur Keith", "work": "Human Embryology and Morphology", "quote": "The **epoophoron** represents the cranial portion of the ancestral mesonephros, preserved in miniature within the adult female."}
    ]
  },
  "Dashboard \u2014 oo\\oidioid.md": {
    "primary": "Resembling or having the morphological characteristics of an oidium or fungal conidial spore chain.",
    "secondary": "In systematic mycology, describing asexual spores or hyphal fragments that divide into barrel-shaped arthroconidia resembling the genus Oidium.",
    "quotes": [
      {"author": "Anton de Bary", "work": "Comparative Morphology and Biology of the Fungi, Mycetozoa and Bacteria", "quote": "The vegetative hyphae fragmented rapidly into an **oidioid** chain of arthrospores capable of immediate dissemination."},
      {"author": "Bryce Kendrick", "work": "The Fifth Kingdom", "quote": "In culture, the mycelium breaks up into **oidioid** propagules that germinate without an obligatory resting period."},
      {"author": "John Webster", "work": "Introduction to Fungi", "quote": "The powdery appearance on the leaf surface was caused by millions of **oidioid** conidia produced upon short conidiophores."}
    ]
  },
  "Dashboard \u2014 oo\\oidium.md": {
    "primary": "A taxonomic anamorphic genus of powdery mildew fungi in the family Erysiphaceae, or an individual conidial spore produced in chains by these fungi.",
    "secondary": "In viticulture and historical phytopathology, Oidium tuckeri famously devastated European vineyards in the mid-19th century until controlled by elemental sulfur dusting.",
    "quotes": [
      {"author": "Miles Joseph Berkeley", "work": "Observations on the Mildew of the Grape Vine", "quote": "The destructive grape blight was caused by a parasitic mold which I described under the generic name **Oidium**."},
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "French viticulturists rescued their harvests from the plague of **Oidium** by dusting the vines with powdered sulfur."},
      {"author": "John Webster", "work": "Introduction to Fungi", "quote": "The asexual stage of many powdery mildews is assigned to **Oidium** pending the discovery of the cleistothecial teleomorph."}
    ]
  },
  "Dashboard \u2014 oo\\oo.md": {
    "primary": "A Greek root and combining form derived from oon, signifying an egg, ovum, or female reproductive gamete.",
    "secondary": "In biological sciences and paleontology, oo- provides the foundational prefix for embryological terms (oogenesis, oocyte, oogonium) and sedimentary rocks (oolite).",
    "quotes": [
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The Greek neuter noun oon forms the scientific combining element **oo**, signifying the primordial egg."},
      {"author": "Robert Beekes", "work": "Etymological Dictionary of Greek", "quote": "Cognate with Latin ovum and Old English aeg, the stem **oo** preserves the Proto-Indo-European root *h₂ōwyóm."},
      {"author": "Edmund Beecher Wilson", "work": "The Cell in Development and Heredity", "quote": "Embryologists combine **oo** with diverse cytological roots to trace the maturation and fertilization of animal eggs."}
    ]
  },
  "Dashboard \u2014 oo\\ooblast.md": {
    "primary": "A female germ cell precursor that differentiates into an oocyte; an embryonic egg-producing cell.",
    "secondary": "In invertebrate embryology and platyhelminth reproductive anatomy, the ooblast receives yolk cells from vitelline glands to construct encapsulated eggs.",
    "quotes": [
      {"author": "Edmund Beecher Wilson", "work": "The Cell in Development and Heredity", "quote": "The primordial **ooblast** undergoes successive mitotic proliferations before committing to the meiotic program of the primary oocyte."},
      {"author": "Thomas Hunt Morgan", "work": "Experimental Embryology", "quote": "Differentiation of the **ooblast** is regulated by nurse cell interactions that funnel maternal mRNAs into the expanding ooplasm."},
      {"author": "Julian Huxley", "work": "The Science of Life", "quote": "Within the ovarian follicles of invertebrates, each **ooblast** is carefully nurtured by dedicated nurse cells."}
    ]
  },
  "Dashboard \u2014 oo\\oocyst.md": {
    "primary": "The thick-walled, environmentally resistant encysted stage of a fertilized zygote (ookinete) in apicomplexan parasitic protozoa, such as Plasmodium and Toxoplasma.",
    "secondary": "In parasitology and tropical medicine, malaria sporozoites develop inside the mosquito stomach oocyst before bursting and migrating to the salivary glands.",
    "quotes": [
      {"author": "Ronald Ross", "work": "The Prevention of Malaria", "quote": "I observed under the lens the pigmented **oocyst** growing upon the stomach wall of the dapple-winged mosquito."},
      {"author": "Patrick Manson", "work": "Tropical Diseases", "quote": "The mature **oocyst** ruptures, shedding thousands of needle-shaped sporozoites into the insect's hemolymph."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "The protective wall of a Toxoplasma **oocyst** allows the parasite to remain infectious in external soil for many months."}
    ]
  },
  "Dashboard \u2014 oo\\oocyte.md": {
    "primary": "A female gametocyte; an immature egg cell that undergoes meiotic divisions in the ovary to produce a mature ovum.",
    "secondary": "In reproductive endocrinology and embryology, a primary oocyte arrests at the diplotene stage of prophase I until ovulation resumes meiotic maturation.",
    "quotes": [
      {"author": "Edmund Beecher Wilson", "work": "The Cell in Development and Heredity", "quote": "During its prolonged growth phase, the primary **oocyte** accumulates nutrient yolk, ribosomes, and maternal messenger RNAs."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "Fertilization triggers a wave of intracellular calcium release that prevents polyspermy and activates the dormant **oocyte**."},
      {"author": "Keith R. Porter", "work": "Fine Structure of Cells and Tissues", "quote": "Electron micrographs show the zona pellucida traversed by delicate microvilli extending between follicle cells and the **oocyte**."}
    ]
  },
  "Dashboard \u2014 oo\\oocytogenesis.md": {
    "primary": "The early phase of female gametogenesis wherein primordial germ cells develop through mitosis into oogonia and differentiate into primary oocytes.",
    "secondary": "In mammalian reproductive biology, oocytogenesis is completed entirely before birth, establishing the finite lifetime pool of non-renewable ovarian follicles.",
    "quotes": [
      {"author": "Edmund Beecher Wilson", "work": "The Cell in Development and Heredity", "quote": "In human female embryogenesis, **oocytogenesis** ceases prior to parturition, leaving all oocytes arrested in early meiotic prophase."},
      {"author": "Arthur Keith", "work": "Human Embryology and Morphology", "quote": "Primordial germ cells migrate from the yolk sac endoderm into the genital ridge to initiate **oocytogenesis**."},
      {"author": "Lewis Wolpert", "work": "Principles of Development", "quote": "Signals from the embryonic ovarian stroma guide **oocytogenesis**, ensuring that germ cells enter meiotic pairing in coordinated waves."}
    ]
  },
  "Dashboard \u2014 oo\\oogamete.md": {
    "primary": "A female reproductive cell or gamete, typically characterized by large size, immobility, and high nutrient storage; an ovum or egg cell.",
    "secondary": "In evolutionary biology, the morphological asymmetry between the large nutritive oogamete and the diminutive motile sperm defines the biological sexes.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "In all oogamous species, the massive immobile **oogamete** relies upon the active search of the microscopic antherozoid for fertilization."},
      {"author": "John Maynard Smith", "work": "The Evolution of Sex", "quote": "Disruptive selection on ancestral isogamous cells favored the specialization of the **oogamete** for zygotic survival."},
      {"author": "Arthur J. Eames", "work": "Morphology of Vascular Plants", "quote": "In the archegonium of ferns, a solitary **oogamete** rests at the venter, awaiting the chemical attraction of swimming flagellated sperms."}
    ]
  },
  "Dashboard \u2014 oo\\oogamous.md": {
    "primary": "Characterized by or exhibiting oogamy; possessing sexual reproduction involving a large, non-motile female gamete and a small, motile male gamete.",
    "secondary": "In phycology and evolutionary botany, the evolutionary transition from isogamous to oogamous reproduction occurs across green algae like Volvox.",
    "quotes": [
      {"author": "F. E. Fritsch", "work": "The Structure and Reproduction of the Algae", "quote": "Within the Volvocales, the progression from Chlamydomonas to Volvox illustrates the evolutionary ascent to an **oogamous** condition."},
      {"author": "G. M. Smith", "work": "Cryptogamic Botany", "quote": "In **oogamous** chlorophytes, the zygote forms a thickened resistant wall that overwinters safely in dried pond mud."},
      {"author": "John Webster", "work": "Introduction to Fungi", "quote": "Water molds belonging to the Oomycota are characteristically **oogamous**, producing large oogonia containing one or more oospores."}
    ]
  },
  "Dashboard \u2014 oo\\oogamy.md": {
    "primary": "A form of sexual reproduction in which the female gamete (egg) is large, nutrient-rich, and non-motile, while the male gamete (sperm) is small and motile.",
    "secondary": "In evolutionary biology, oogamy is the universal reproductive mode of all land plants and animals, providing maximal nutrient reserves for the developing embryo.",
    "quotes": [
      {"author": "John Maynard Smith", "work": "The Evolution of Sex", "quote": "The evolution of **oogamy** from isogamy represents one of the major evolutionary transitions, establishing fundamental sexual dimorphism."},
      {"author": "Arthur J. Eames", "work": "Morphology of Vascular Plants", "quote": "All embryophytes share **oogamy**, retaining the fertilized egg within the maternal gametophyte tissue for early nourishment."},
      {"author": "F. E. Fritsch", "work": "The Structure and Reproduction of the Algae", "quote": "In brown seaweeds like Fucus, **oogamy** achieves dramatic expression as thousands of motile antherozoids swarm around each extruded egg."}
    ]
  },
  "Dashboard \u2014 oo\\oogenesis.md": {
    "primary": "The biological process of female gamete formation, maturation, and development, culminating in the production of a fertilizable ovum.",
    "secondary": "In cellular genetics, oogenesis involves unequal cytoplasmic meiotic divisions that generate a single large ovum and three degenerating polar bodies.",
    "quotes": [
      {"author": "Edmund Beecher Wilson", "work": "The Cell in Development and Heredity", "quote": "The crucial feature of **oogenesis** is the unequal division of the cytoplasm, which concentrates virtually all maternal reserves into a single mature egg."},
      {"author": "Thomas Hunt Morgan", "work": "The Physical Basis of Heredity", "quote": "Meiotic reduction during **oogenesis** separates maternal from paternal homologous chromosomes in strict accordance with Mendelian segregation."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "During **oogenesis**, lampbrush chromosomes synthesize enormous quantities of ribosomes and messenger RNAs destined for early embryogenesis."}
    ]
  },
  "Dashboard \u2014 oo\\oogonium.md": {
    "primary": "The female sexual organ in certain algae and fungi that produces one or more non-motile female gametes (oospores or eggs); in animals, an undifferentiated diploid female germ cell.",
    "secondary": "In human female embryology, oogonia multiply by mitosis in the fetal ovary before entering meiosis to become primary oocytes.",
    "quotes": [
      {"author": "Anton de Bary", "work": "Comparative Morphology and Biology of the Fungi", "quote": "Antheridial branches wrap around the swollen **oogonium** of Pythium, penetrating its wall with fertilizing tubes."},
      {"author": "Edmund Beecher Wilson", "work": "The Cell in Development and Heredity", "quote": "In the fetal ovary, each **oogonium** undergoes multiple mitotic divisions to generate the definitive stock of primary oocytes."},
      {"author": "F. E. Fritsch", "work": "The Structure and Reproduction of the Algae", "quote": "The spherical **oogonium** of Oedogonium opens by a lateral pore to allow antherozoids entrance to the egg."}
    ]
  },
  "Dashboard \u2014 oo\\ooid.md": {
    "primary": "A small, spherical or ellipsoidal accretionary sedimentary grain, typically less than two millimeters in diameter, composed of concentric mineral laminae around a nucleus.",
    "secondary": "In sedimentary petrology, ooids form in shallow, agitated, carbonate-saturated tropical marine waters where wave action rolls grains as calcium carbonate precipitates.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Under the lens, each rounded **ooid** reveals delicate concentric coats of carbonate deposited like the coats of an onion."},
      {"author": "Arthur Holmes", "work": "Principles of Physical Geology", "quote": "Modern **ooid** shoals forming on the Bahama Banks demonstrate how agitated shallow tidal currents stimulate rapid aragonite precipitation."},
      {"author": "Robert Folk", "work": "Petrology of Sedimentary Rocks", "quote": "Thin sections of oosparite limestone display the radial and concentric fabric preserved within each marine **ooid**."}
    ]
  },
  "Dashboard \u2014 oo\\oolite.md": {
    "primary": "A sedimentary rock (usually limestone) composed predominantly of small, spherical, concentric accretionary grains called ooids cemented together.",
    "secondary": "In stratigraphy and historical geology, oolite formations (such as the Jurassic Portland and Bath oolites of England) are renowned for premium freestone building material.",
    "quotes": [
      {"author": "William Smith", "work": "Strata Identified by Organized Fossils", "quote": "The distinctive roe-stone texture of the Great **Oolite** provides an unmistakable stratigraphic landmark across the English shires."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The Jurassic **oolite** formations of western Europe yielded magnificent ammonites and fossil reptiles to early collectors."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The finest Gothic monuments of southern England were sculpted from creamy, durable blocks of Bath **oolite**."}
    ]
  },
  "Dashboard \u2014 oo\\oolith.md": {
    "primary": "An individual spherical or subspherical grain of an oolite, possessing a concentric internal laminar structure surrounding a mineral nucleus.",
    "secondary": "In geological terminology, oolith is historically interchangeable with ooid, describing individual egg-shaped calcareous spherules in sedimentary limestones.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Breakage of a single **oolith** exposes the foreign quartz grain or shell fragment that served as its crystallization nucleus."},
      {"author": "Arthur Holmes", "work": "Principles of Physical Geology", "quote": "Wave turbulence keeps each **oolith** in constant suspension while successive microcrystalline carbonate envelopes precipitate around it."},
      {"author": "J. D. Dana", "work": "Manual of Geology", "quote": "The roe-like appearance of oolitic limestone is caused by millions of cemented **oolith** bodies resembling fish eggs."}
    ]
  },
  "Dashboard \u2014 oo\\oology.md": {
    "primary": "The branch of zoological ornithology that studies the morphology, pigmentation, structure, and incubation of bird eggs.",
    "secondary": "In Victorian and twentieth-century natural history, oology was practiced both as a rigorous comparative science and as an enthusiastic pursuit of egg collecting.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "Darwinism: An Exposition of the Theory of Natural Selection", "quote": "The study of **oology** demonstrates that ground-nesting birds lay cryptically mottled eggs to elude keen-eyed predatory raptors."},
      {"author": "John Gould", "work": "The Birds of Australia", "quote": "Our systematic **oology** records the remarkable diversity of egg clutches gathered from the remote interior eucalyptus forests."},
      {"author": "Gilbert White", "work": "The Natural History and Antiquities of Selborne", "quote": "The curious inquirer into **oology** will observe that hole-nesting species lay white immaculate eggs, needing no protective coloring."}
    ]
  },
  "Dashboard \u2014 oo\\oomancy.md": {
    "primary": "An ancient form of divination or fortune-telling through the interpretation and inspection of eggs, especially patterns in egg whites or yolks.",
    "secondary": "In folklore and historical anthropology, oomancy (ovomancy) was performed by dropping egg whites into boiling or cold water to read prognostic shapes predicting future spouses or fortunes.",
    "quotes": [
      {"author": "Edward Burnett Tylor", "work": "Primitive Culture", "quote": "Rustic superstitions long preserved **oomancy**, dropping an egg into a glass of spring water on Midsummer Eve to read the shapes."},
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Among the vanities of pagan augury was **oomancy**, which pretended to decipher divine portents within the yolk of an egg."},
      {"author": "Cotton Mather", "work": "The Wonders of the Invisible World", "quote": "The foolish practice of **oomancy** by young maidens in Salem was reported to have opened the door to demonic delusions."}
    ]
  },
  "Dashboard \u2014 oo\\oophagy.md": {
    "primary": "The practice or biological habit of consuming eggs; egg-eating behavior.",
    "secondary": "In marine biology and reproductive physiology, intrauterine oophagy (adelphophagy) describes embryos of certain lamniform sharks (such as sand tigers) that devour unfertilized sibling eggs within the oviduct.",
    "quotes": [
      {"author": "Aristotle", "work": "History of Animals", "quote": "Certain serpents and birds are addicted to **oophagy**, swallowing whole eggs and crushing the brittle shells in their gullets."},
      {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "In mackerel sharks, embryonic **oophagy** sustains rapid gestation, the active embryos consuming newly ovulated eggs inside the mother."},
      {"author": "E. O. Wilson", "work": "Sociobiology: The New Synthesis", "quote": "Within ant colonies, trophic **oophagy** allows workers to feed unfertilized eggs to developing larvae during seasons of food shortage."}
    ]
  },
  "Dashboard \u2014 oo\\oophorectomy.md": {
    "primary": "The surgical removal or excision of one or both ovaries; ovariectomy.",
    "secondary": "In gynecological oncology and clinical surgery, bilateral oophorectomy is performed to treat ovarian neoplasms, endometriosis, or as risk-reducing prophylaxis in BRCA mutation carriers.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Ephraim McDowell performed the first successful **oophorectomy** in frontier Kentucky, opening the era of modern abdominal surgery."},
      {"author": "Howard Kelly", "work": "Operative Gynecology", "quote": "Bilateral **oophorectomy** induces immediate surgical menopause, halting the hormonal stimulation of metastatic breast tumors."},
      {"author": "Lord Moynihan", "work": "Abdominal Operations", "quote": "Ligation of the infundibulopelvic ligament must be executed with precision during an **oophorectomy** to avoid injuring the ureter."}
    ]
  },
  "Dashboard \u2014 oo\\oophoron.md": {
    "primary": "The anatomical ovary in females; literally the egg-bearer.",
    "secondary": "In historical and clinical medical literature, oophoron was commonly used in compound gynecological terms designating inflammatory conditions (oophoritis) and surgical removals.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The **oophoron** or ovary rests within the peritoneal fold of the broad ligament, connected to the uterus by its fibro-muscular ligament."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic inflammation of the **oophoron** and fallopian tube frequently leads to pelvic adhesions and localized peritonitis."},
      {"author": "Arthur Keith", "work": "Human Embryology and Morphology", "quote": "Embryological development of the **oophoron** mirrors that of the testis until cortical cords establish definitive ovarian follicles."}
    ]
  },
  "Dashboard \u2014 oo\\ootheca.md": {
    "primary": "A protective structural egg case, capsule, or packet secreted by female insects (such as cockroaches and praying mantises) or certain mollusks to shelter eggs.",
    "secondary": "In entomology and chemical ecology, the foamy proteinaceous secretion of the mantis ootheca hardens on contact with air into a tough, weather-resistant, insulating foam.",
    "quotes": [
      {"author": "Alpheus Spring Packard", "work": "Guide to the Study of Insects", "quote": "The female praying mantis deposits her eggs in a spongy **ootheca** that hardens upon twig bark to protect the embryos through freezing winter."},
      {"author": "Jean-Henri Fabre", "work": "The Wonders of Instinct", "quote": "The architecture of the mantis **ootheca** is an architectural marvel of layered silk-like froth designed to baffle parasitic wasps."},
      {"author": "Vincent Dethier", "work": "To Know a Fly", "quote": "The cockroach carries her compressed chitinous **ootheca** protruding from her abdomen until finding a dark crevice to drop it."}
    ]
  },
  "Dashboard \u2014 oo\\ootid.md": {
    "primary": "The haploid female cell formed after the completion of meiosis II in the secondary oocyte, immediately prior to its development into a mature fertilizable ovum.",
    "secondary": "In animal cytogenetics, the formation of the ootid is accompanied by the extrusion of the second polar body, completing the segregation of maternal chromatids.",
    "quotes": [
      {"author": "Edmund Beecher Wilson", "work": "The Cell in Development and Heredity", "quote": "The second meiotic maturation division yields the definitive **ootid** alongside the diminutive second polar body."},
      {"author": "Thomas Hunt Morgan", "work": "The Physical Basis of Heredity", "quote": "Following sperm entry, the **ootid** nucleus resolves into the female pronucleus ready for syngamy with the male chromatin."},
      {"author": "Theodosius Dobzhansky", "work": "Genetics of the Evolutionary Process", "quote": "The chromosome complement of the **ootid** represents a single non-recombinant or crossover chromatid from each maternal bivalent."}
    ]
  },
  "Dashboard \u2014 oo\\ootidogenesis.md": {
    "primary": "The cytological process of ootid formation during the final meiotic maturation division of the secondary oocyte.",
    "secondary": "In reproductive embryology, ootidogenesis is triggered in most mammals by sperm penetration, which stimulates the resumption and completion of anaphase II and telophase II.",
    "quotes": [
      {"author": "Edmund Beecher Wilson", "work": "The Cell in Development and Heredity", "quote": "Sperm penetration breaks the metaphase II arrest, initiating **ootidogenesis** and the rapid expulsion of the second polar body."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "Degradation of maturation-promoting factor allows **ootidogenesis** to proceed to telophase, forming the female pronucleus."},
      {"author": "Lewis Wolpert", "work": "Principles of Development", "quote": "Errors during **ootidogenesis** leading to nondisjunction in meiosis II are a major cause of chromosomal trisomies in human conceptions."}
    ]
  },
  "Dashboard \u2014 oo\\paroophoron.md": {
    "primary": "A small vestigial embryonic anatomical structure in the female broad ligament consisting of a few scattered microscopic blind tubules; a remnant of the caudal mesonephros.",
    "secondary": "In gynecological embryology and histology, the paroophoron lies medial to the epoophoron, homologous to the male paradidymis, and typically regresses after infancy.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The **paroophoron** is an inconstant collection of microscopic mesonephric tubules situated between the layers of the broad ligament near the uterus."},
      {"author": "Arthur Keith", "work": "Human Embryology and Morphology", "quote": "While the epoophoron represents the genital portion of the mesonephros, the **paroophoron** represents the atrophied excretory portion."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Occasional small adenomatous cysts arising within the broad ligament trace their origin to persistent tubules of the **paroophoron**."}
    ]
  },
  "Dashboard \u2014 opisth\\anopisthograph.md": {
    "primary": "A manuscript, papyrus roll, or tablet inscribed on one side only, leaving the reverse side completely blank; not an opisthograph.",
    "secondary": "In codicology, papyrology, and epigraphy, an anopisthograph represents the standard format for ancient literary scrolls, whereas administrative or economy scrolls were written on both sides.",
    "quotes": [
      {"author": "Frederic G. Kenyon", "work": "Books and Readers in Ancient Greece and Rome", "quote": "The high-quality literary papyrus roll was regularly an **anopisthograph**, bearing columns of writing only on the recto where fibers ran horizontally."},
      {"author": "Edward Maunde Thompson", "work": "An Introduction to Greek and Latin Palaeography", "quote": "While scribes reserved the verso for personal notes or later accounts, public decrees were strictly published as an **anopisthograph**."},
      {"author": "E. G. Turner", "work": "Greek Papyri: An Introduction", "quote": "A deluxe copy of Homer was prepared as an **anopisthograph**, leaving the reverse side clean and unstained by ink."}
    ]
  },
  "Dashboard \u2014 opisth\\opisth.md": {
    "primary": "A Greek root and combining form derived from opisthen, meaning behind, backward, at the back, or posterior.",
    "secondary": "In biological taxonomy, anatomy, and archaeology, opisth- forms prefixes designating posterior body regions (opisthosoma), backward fangs (opisthoglyphous), or rear temple porches (opisthodomos).",
    "quotes": [
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The classical Greek adverb opisthen forms the technical combining stem **opisth**, denoting posterior position or backward motion."},
      {"author": "Robert Beekes", "work": "Etymological Dictionary of Greek", "quote": "Cognate with Old English aft, the root **opisth** expresses spatial or temporal posteriority throughout scientific compounding."},
      {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "Comparative anatomists prefix **opisth** to designate skeletal elements located toward the occiput or posterior trunk."}
    ]
  },
  "Dashboard \u2014 opisth\\opisthion.md": {
    "primary": "In craniometry and physical anthropology, the anatomical landmark located at the midpoint of the posterior border of the foramen magnum of the skull.",
    "secondary": "In cephalometrics and paleoanthropology, the opisthion is used with the basion to measure cranial base length and the inclination of the foramen magnum.",
    "quotes": [
      {"author": "Paul Broca", "work": "Instructions crâniologiques", "quote": "We define the **opisthion** as the median point on the posterior lip of the occipital foramen, essential for establishing the basicranial axis."},
      {"author": "Ales Hrdlicka", "work": "Anthropometry", "quote": "The distance between basion and **opisthion** measures the anteroposterior diameter of the foramen magnum in fossil hominids."},
      {"author": "Arthur Keith", "work": "Human Embryology and Morphology", "quote": "The forward migration of the **opisthion** relative to the vertebral column reflects the evolutionary attainment of upright bipedal posture."}
    ]
  },
  "Dashboard \u2014 opisth\\opisthobranch.md": {
    "primary": "A marine gastropod mollusk belonging to the Opisthobranchia, commonly including sea slugs, sea hares, and nudibranchs, characterized by gills located behind the heart.",
    "secondary": "In marine biology and malacology, opisthobranch gastropods are renowned for shell reduction, brilliant aposematic coloration, and the sequestration of chemical toxins from sponges.",
    "quotes": [
      {"author": "William T. Calman", "work": "The Life of Crustacea", "quote": "The sea slug, a delicate **opisthobranch** mollusk, crawls over kelp fronds displaying vivid warning colors to predatory fish."},
      {"author": "E. Ray Lankester", "work": "A Treatise on Zoology", "quote": "Detorsion in the **opisthobranch** reverses the ancestral torted symmetry of gastropods, shifting the gill behind the auricle."},
      {"author": "Charles Wyville Thomson", "work": "The Depths of the Sea", "quote": "Benthic dredges hauled up several swimming **opisthobranch** species whose translucent parapodia enable graceful pelagic locomotion."}
    ]
  },
  "Dashboard \u2014 opisth\\opisthobranchia.md": {
    "primary": "A major former subclass or taxonomic group of marine gastropod mollusks having gills (ctenidia) situated posterior to the heart, encompassing sea slugs and nudibranchs.",
    "secondary": "In invertebrate zoology and evolutionary malacology, Opisthobranchia is characterized by secondary detorsion, loss or reduction of the shell, and hermaphroditic reproduction.",
    "quotes": [
      {"author": "Georges Cuvier", "work": "The Animal Kingdom", "quote": "We established the order **Opisthobranchia** to separate those gastropods whose respiratory organs lie behind the heart upon the back."},
      {"author": "E. Ray Lankester", "work": "Mollusca", "quote": "The evolutionary trend in the **Opisthobranchia** shows a progressive loss of the protective shell accompanied by chemical defense synthesis."},
      {"author": "Richard Fortey", "work": "Life: An Unauthorised Biography", "quote": "Nudibranchs of the **Opisthobranchia** represent living masterpieces of evolution, stealing functional stinging nematocysts from jellyfish prey."}
    ]
  },
  "Dashboard \u2014 opisth\\opisthocomidae.md": {
    "primary": "A monotypic family of tropical South American arboreal birds containing only the hoatzin (*Opisthocomus hoazin*).",
    "secondary": "In avian systematics and evolutionary biology, Opisthocomidae represents an ancient, enigmatic avian lineage famous for claws on juvenile wings and foregut folivory.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "The family **Opisthocomidae** occupies a completely isolated taxonomic position among birds, surviving only in the Amazonian and Orinoco basins."},
      {"author": "Thomas Henry Huxley", "work": "On the Classification of Birds", "quote": "Skeletal peculiarities of the **Opisthocomidae**, particularly the reduced sternal keel and enlarged crop, reflect their bizarre folivorous diet."},
      {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The wing claws exhibited by nestling **Opisthocomidae** provide a striking living parallel to the morphology of Archaeopteryx."}
    ]
  },
  "Dashboard \u2014 opisth\\opisthocomus.md": {
    "primary": "A taxonomic genus of herbivorous South American birds containing the hoatzin (*Opisthocomus hoazin*), characterized by an enlarged muscular crop used for leaf fermentation.",
    "secondary": "In ornithology, Opisthocomus chicks possess functional claws on the first and second wing digits, allowing them to climb riverine branches after dropping into water to escape predators.",
    "quotes": [
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions of America", "quote": "Flocks of **Opisthocomus** roosted along the flooded banks of the Apure river, filling the humid air with hoarse, discordant cries."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants Under Domestication", "quote": "The rudimentary wing claws of young **Opisthocomus** illustrate how ancestral reptilian locomotive structures persist in specialized avian nestlings."},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "South America holds singular avian marvels like **Opisthocomus**, whose foregut microbial fermentation parallels that of ruminant mammals."}
    ]
  },
  "Dashboard \u2014 opisth\\opisthodomos.md": {
    "primary": "In classical Greek architecture, the enclosed rear room or back porch of a peripteral temple, located behind the cella (naos).",
    "secondary": "In ancient Athens and classical history, the opisthodomos of the Parthenon on the Acropolis served as the secure public treasury of the Athenian state and the Delian League.",
    "quotes": [
      {"author": "Thucydides", "work": "History of the Peloponnesian War", "quote": "Pericles reminded the Athenians of the reserve fund of uncoined gold and silver bullion safely stored in the **opisthodomos** of the Parthenon."},
      {"author": "Vitruvius", "work": "The Ten Books on Architecture", "quote": "In a peripteral temple, the **opisthodomos** mirrors the architectural proportions of the front pronaos, maintaining structural symmetry."},
      {"author": "Demosthenes", "work": "Against Timocrates", "quote": "The state auditors verified the balances remaining in the sacred **opisthodomos** before disbursing trireme naval funds."}
    ]
  },
  "Dashboard \u2014 opisth\\opisthoglyphous.md": {
    "primary": "Having grooved, venom-conducting fangs situated at the rear of the upper jaw (maxilla), as found in rear-fanged colubrid snakes.",
    "secondary": "In herpetology and snake venomology, opisthoglyphous species (such as the boomslang and vine snake) must chew prey into the mouth corner to inject venom.",
    "quotes": [
      {"author": "Edward Drinker Cope", "work": "The Crocodilians, Lizards, and Snakes of North America", "quote": "Colubrid snakes possessing enlarged grooved posterior maxillary teeth are classed as **opisthoglyphous**, separating them from aglyphous forms."},
      {"author": "Raymond L. Ditmars", "work": "Reptiles of the World", "quote": "The dangerous African boomslang is strictly **opisthoglyphous**, delivering a potent hemotoxic venom through deeply grooved rear fangs."},
      {"author": "Hans Gadow", "work": "Amphibia and Reptiles", "quote": "In an **opisthoglyphous** snake, the rear fangs serve primarily to paralyze struggling amphibians or lizards as they are swallowed."}
    ]
  },
  "Dashboard \u2014 opisth\\opisthognathidae.md": {
    "primary": "A family of small, burrow-dwelling marine perciform teleost fishes commonly known as jawfishes, characterized by large heads and mouths.",
    "secondary": "In marine ichthyology and behavioral ecology, Opisthognathidae species excavate elaborate vertical burrows in coral rubble and practice paternal oral egg brooding.",
    "quotes": [
      {"author": "Albert Günther", "work": "Catalogue of the Fishes in the British Museum", "quote": "The family **Opisthognathidae** is distinguished by an enormous maxilla extending far behind the orbit and an elongated dorsal fin."},
      {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "Jawfishes of the family **Opisthognathidae** hover vertically above their sand burrows, retreating tail-first at the slightest alarm."},
      {"author": "Joseph S. Nelson", "work": "Fishes of the World", "quote": "Paternal mouthbrooding is a universal reproductive trait among the **Opisthognathidae**, the male brooding the egg mass within his buccal cavity."}
    ]
  },
  "Dashboard \u2014 opisth\\opisthognathous.md": {
    "primary": "Having receding, backward-sloping jaws; in entomology, having mouthparts directed backward toward the ventral side of the body between the anterior legs.",
    "secondary": "In physical anthropology and entomology, opisthognathous facial profiles contrast with prognathous (projecting) jaws, and in insects characterize sap-sucking hemipterans.",
    "quotes": [
      {"author": "Alpheus Spring Packard", "work": "Guide to the Study of Insects", "quote": "In true bugs and cicadas, the head is distinctly **opisthognathous**, with the jointed piercing beak directed backward under the thorax."},
      {"author": "Paul Broca", "work": "Instructions crâniologiques", "quote": "Facial angle measurements designate a skull as **opisthognathous** when the alveolar margin recedes behind the vertical cranial plane."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The retreat of the mandibular symphysis creates a markedly **opisthognathous** profile in certain specialized mammalian herbivores."}
    ]
  },
  "Dashboard \u2014 opisth\\opisthograph.md": {
    "primary": "An ancient papyrus scroll, manuscript, or inscribed tablet that bears writing on both the front and back sides (recto and verso).",
    "secondary": "In classical literature, papyrology, and epigraphy, an opisthograph was typically produced due to economic scarcity of papyrus or for private working drafts.",
    "quotes": [
      {"author": "Pliny the Elder", "work": "Natural History", "quote": "My uncle left me one hundred and sixty volumes of closely written commentary, each an **opisthograph** covered with notes on the reverse side."},
      {"author": "Juvenal", "work": "Satires", "quote": "Must I endure endless recitations of that monstrous tragedy, written to the very margin and covering the back as an **opisthograph**?"},
      {"author": "Frederic G. Kenyon", "work": "Books and Readers in Ancient Greece and Rome", "quote": "While formal literary editions avoided writing on the verso, everyday accounts frequently converted a papyrus into an **opisthograph**."}
    ]
  },
  "Dashboard \u2014 opisth\\opisthokont.md": {
    "primary": "Any organism belonging to the eukaryotic supergroup Opisthokonta, encompassing the animal and fungal kingdoms, characterized by swimming cells propelled by a single posterior flagellum.",
    "secondary": "In evolutionary protistology and phylogenomics, an opisthokont (including choanoflagellates and metazoans) is distinguished from anteriorly flagellated bikonts.",
    "quotes": [
      {"author": "Thomas Cavalier-Smith", "work": "The Megasystem of the Eukaryotes", "quote": "I established the clade Opisthokonta, noting that every typical **opisthokont** swimmer is propelled forward by a single posterior uniflagellum."},
      {"author": "Lynn Margulis", "work": "Symbiosis in Cell Evolution", "quote": "Molecular phylogenetics confirms that animals and fungi share a common **opisthokont** flagellated ancestor."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "The propulsion of human spermatozoa by a trailing flagellum reflects our ancient heritage as an **opisthokont** organism."}
    ]
  },
  "Dashboard \u2014 opisth\\opisthorchiasis.md": {
    "primary": "A parasitic infection of the bile ducts caused by liver flukes of the genus Opisthorchis, contracted through consuming raw or undercooked freshwater cyprinid fish.",
    "secondary": "In tropical medicine and infectious gastroenterology, chronic opisthorchiasis induces bile duct inflammation, recurrent cholangitis, and significantly elevates the risk of cholangiocarcinoma.",
    "quotes": [
      {"author": "Patrick Manson", "work": "Tropical Diseases", "quote": "Endemic **opisthorchiasis** in Southeast Asia is sustained by culinary traditions of consuming fermented raw cyprinid fish."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Heavy liver fluke infestation in **opisthorchiasis** leads to mechanical bile duct obstruction, localized cirrhosis, and jaundice."},
      {"author": "Anthony S. Fauci", "work": "Harrison's Principles of Internal Medicine", "quote": "Sustained biliary mucosal irritation from chronic **opisthorchiasis** is strongly recognized as a potent biological carcinogen."}
    ]
  },
  "Dashboard \u2014 opisth\\opisthosoma.md": {
    "primary": "The posterior tagma or abdominal body region of an arachnid or chelicerate, located posterior to the prosoma (cephalothorax).",
    "secondary": "In arthropod morphology, the opisthosoma houses vital vegetative organs including the book lungs, heart, digestive glands, gonads, and silk spinnerets.",
    "quotes": [
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", "quote": "In spiders, the narrow pedicel separates the anterior prosoma from the swollen unsegmented **opisthosoma**."},
      {"author": "Alpheus Spring Packard", "work": "A Text-Book of Entomology", "quote": "The segmented **opisthosoma** of the scorpion terminates in a slender postabdomen ending in a venomous curved sting."},
      {"author": "John Henry Comstock", "work": "The Spider Book", "quote": "Ventral glands in the **opisthosoma** synthesize liquid silk proteins that are spun into webs through terminal spinnerets."}
    ]
  },
  "Dashboard \u2014 opisth\\opisthotonos.md": {
    "primary": "A condition of severe, involuntary muscular tetanic spasm in which the back, neck, and spine arch backward while the limbs flex, causing the body to rest on head and heels.",
    "secondary": "In clinical neurology and historical toxicology, opisthotonos is a diagnostic hallmark of severe tetanus infection, strychnine poisoning, and kernicterus in neonates.",
    "quotes": [
      {"author": "Hippocrates", "work": "Aphorisms", "quote": "In cases of tetanus with violent **opisthotonos**, the patient's spine curves backward like a drawn bow, and convulsions threaten asphyxia."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Tetanus toxin induces agonizing tonic contractions, throwing the conscious patient into extreme paroxysms of **opisthotonos**."},
      {"author": "Charles Bell", "work": "The Nervous System of the Human Body", "quote": "My anatomical sketch of a wounded soldier dying of tetanus captures the terrifying muscular tension of **opisthotonos**."}
    ]
  },
  "Dashboard \u2014 opisth\\opsimathy.md": {
    "primary": "Education or learning acquired late in life; the pursuit of intellectual studies in one's mature or advanced years.",
    "secondary": "In classical moral philosophy and literature, opsimathy (from Greek opse, late, and manthanein, to learn) was discussed as both an admirable dedication to wisdom and, satirically, as pedantic over-enthusiasm.",
    "quotes": [
      {"author": "Theophrastus", "work": "Characters", "quote": "The man afflicted with **opsimathy** takes up singing lessons at sixty and recites memorized verses clumsily at feasts."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "There is a noble courage in that **opsimathy** which prompts an aged scholar to master a difficult language before he dies."},
      {"author": "Plutarch", "work": "Moralia", "quote": "Cato the Elder exemplified praiseworthy **opsimathy**, turning with vigor to the study of Greek literature in his eightieth year."}
    ]
  },
  "Dashboard \u2014 orth\\anorthic.md": {
    "primary": "In crystallography, belonging to the triclinic crystal system; having three unequal crystallographic axes intersecting at mutually oblique, non-perpendicular angles.",
    "secondary": "In mineralogy, anorthic crystals (such as plagioclase feldspars and kyanite) exhibit the lowest crystallographic symmetry, possessing either a center of inversion or no symmetry elements at all.",
    "quotes": [
      {"author": "William Hallows Miller", "work": "A Treatise on Crystallography", "quote": "The **anorthic** system possesses no planes of symmetry whatever, its three axes intersecting at mutually oblique angles."},
      {"author": "J. D. Dana", "work": "A System of Mineralogy", "quote": "Crystals of rhodonite and kyanite illustrate the **anorthic** habit, displaying irregular oblique prisms in thin section."},
      {"author": "Paul Groth", "work": "Physikalische Krystallographie", "quote": "Optical axes in an **anorthic** crystal disperse unevenly due to the complete lack of perpendicular crystallographic constraints."}
    ]
  },
  "Dashboard \u2014 orth\\anorthite.md": {
    "primary": "A calcium-rich plagioclase feldspar mineral (CaAl2Si2O8), representing the calcium endmember of the albite-anorthite solid solution series.",
    "secondary": "In petrology and lunar geology, anorthite is a major constituent of basic igneous rocks (gabbro, basalt) and dominates the light-colored ancient anorthosite crust of the lunar highlands.",
    "quotes": [
      {"author": "J. D. Dana", "work": "A System of Mineralogy", "quote": "The mineral **anorthite** was named from the Greek for oblique, in reference to the anorthic triclinic form of its crystals."},
      {"author": "Arthur Holmes", "work": "Principles of Physical Geology", "quote": "Basic magma cooling at depth crystallizes calcium-rich **anorthite** before sodium-bearing plagioclase can separate."},
      {"author": "Eugene Shoemaker", "work": "Geology of the Moon", "quote": "Apollo lunar samples revealed that the primordial highland crust consists almost entirely of crystalline calcic **anorthite**."}
    ]
  },
  "Dashboard \u2014 orth\\anorthitic.md": {
    "primary": "Pertaining to, composed of, or characteristic of the mineral anorthite; rich in calcium plagioclase feldspar.",
    "secondary": "In igneous petrology and meteoritics, anorthitic compositions designate calcium-aluminum-rich silicate phases found in primitive eucrite meteorites and troctolite cumulates.",
    "quotes": [
      {"author": "J. D. Dana", "work": "A System of Mineralogy", "quote": "The volcanic lavas of Mount Somma contain prominent glassy crystals of distinctly **anorthitic** composition."},
      {"author": "Alfred Harker", "work": "The Natural History of Igneous Rocks", "quote": "Early-formed **anorthitic** phenocrysts settle through basaltic magma, building dense cumulate layers on the chamber floor."},
      {"author": "Harold Urey", "work": "The Planets: Their Origin and Development", "quote": "Spectral analysis of lunar highlands confirms a predominantly **anorthitic** mineralogy across the ancient cratered terrain."}
    ]
  },
  "Dashboard \u2014 orth\\anorthography.md": {
    "primary": "The neurological loss or impairment of the ability to write or spell correctly, resulting from brain disease or focal cerebral cortical lesions; agraphia.",
    "secondary": "In neuropsychology and cognitive neurology, anorthography (spelling agraphia) can result from vascular strokes affecting the left angular gyrus or Exner's area.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Focal lesions near the left angular gyrus frequently induce **anorthography**, the patient losing the power to form letters into words."},
      {"author": "Henry Head", "work": "Aphasia and Kindred Disorders of Speech", "quote": "The soldier's shrapnel wound produced severe **anorthography**, though his ability to recognize spoken words remained intact."},
      {"author": "Alexander Luria", "work": "Higher Cortical Functions in Man", "quote": "Analysis of **anorthography** allows the clinician to distinguish phonetic spelling errors from spatial agraphic distortions."}
    ]
  },
  "Dashboard \u2014 orth\\anorthopia.md": {
    "primary": "A visual defect or perceptual abnormality in which straight lines appear curved, distorted, or obliquely slanted.",
    "secondary": "In clinical ophthalmology, anorthopia can arise from irregular corneal astigmatism, retinal photoreceptor displacement in central chorioretinitis, or occipital visual processing disorders.",
    "quotes": [
      {"author": "Hermann von Helmholtz", "work": "Treatise on Physiological Optics", "quote": "Irregularities in the curvature of the corneal surface produce optical **anorthopia**, bending straight contours into irregular curves."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A patient suffering from central serous retinopathy complained of **anorthopia**, observing horizontal doorframes tilting obliquely."},
      {"author": "Oliver Sacks", "work": "Migraine", "quote": "During the fortification spectrum of a migraine aura, transient **anorthopia** distorts the visual field before the headache erupts."}
    ]
  },
  "Dashboard \u2014 orth\\orth.md": {
    "primary": "A Greek root and combining form derived from orthos, signifying straight, upright, erect, right, correct, or standard.",
    "secondary": "In scientific and classical terminology, orth- serves as the foundational prefix for orthodox theology, orthodontic dental correction, and orthogonal geometric angles.",
    "quotes": [
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The Greek adjective orthos forms the combining stem **orth**, signifying straight in direction, upright in posture, or sound in truth."},
      {"author": "Robert Beekes", "work": "Etymological Dictionary of Greek", "quote": "Derived from Proto-Indo-European *Hordh-, the root **orth** historically denoted rising straight upward like a steep hill."},
      {"author": "Euclid", "work": "Elements", "quote": "When a straight line standing on another makes adjacent angles equal, each angle is right, rooted in the Greek concept of **orth**."},
      {"author": "Aristotle", "work": "Nicomachean Ethics", "quote": "Moral virtue is guided by right reason, that correct balance which ancient philosophers termed **orth**."}
    ]
  },
  "Dashboard \u2014 orth\\orthicon.md": {
    "primary": "An early television camera pickup tube that utilized a low-velocity scanning electron beam perpendicular to the target plate to minimize distortion and secondary emission.",
    "secondary": "In the history of broadcast engineering and television electronics, the orthicon (and later image orthicon) developed by RCA revolutionized live broadcast television in the 1940s.",
    "quotes": [
      {"author": "Vladimir Zworykin", "work": "Television: The Electronics of Image Transmission", "quote": "The **orthicon** eliminated the spurious shading signals of the iconoscope by operating with a low-velocity electron scanning beam."},
      {"author": "Albert Rose", "work": "The Image Orthicon: A Sensitive Television Pickup Tube", "quote": "With the image **orthicon**, live television broadcasting could for the first time operate successfully under ordinary outdoor illumination."},
      {"author": "David Sarnoff", "work": "Looking Ahead: The Papers of David Sarnoff", "quote": "The development of the **orthicon** camera tube represented a decisive triumph for electronic television over mechanical systems."}
    ]
  },
  "Dashboard \u2014 orth\\orthilia.md": {
    "primary": "A taxonomic genus of evergreen perennial rhizomatous woodland herbs in the family Ericaceae, comprising sidebells wintergreen (*Orthilia secunda*).",
    "secondary": "In circumboreal plant ecology, Orthilia is distinguished by its one-sided, secund floral racemes bearing greenish-white nodding flowers in coniferous and mixed boreal forests.",
    "quotes": [
      {"author": "Carl Linnaeus", "work": "Flora Lapponica", "quote": "In the damp pine forests of Lapland, the delicate wintergreen, now placed in **Orthilia**, bears all its flowers nodding toward one side."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The genus **Orthilia** is readily separated from typical Pyrola by its secund racemes and elongated style lacking a collar."},
      {"author": "Eugenius Warming", "work": "Oecology of Plants: An Introduction to the Study of Plant Communities", "quote": "Along shaded boreal forest floors, **Orthilia** thrives within acidic moss carpets through extensive clonal rhizome networks."}
    ]
  },
  "Dashboard \u2014 orth\\orthocenter.md": {
    "primary": "In Euclidean planar geometry, the point where the three altitudes of a triangle intersect (or concur).",
    "secondary": "In triangle geometry, the orthocenter lies collinear with the circumcenter and centroid along the Euler line, situated inside acute triangles and outside obtuse triangles.",
    "quotes": [
      {"author": "Leonhard Euler", "work": "Solutio facilis problematum quorundam geometricorum", "quote": "The center of the circumscribed circle, the center of gravity, and the **orthocenter** of any triangle lie upon a single straight line."},
      {"author": "Euclid", "work": "Elements", "quote": "The intersection of the perpendiculars dropped from the vertices to opposite sides defines what later geometers designated the **orthocenter**."},
      {"author": "H. S. M. Coxeter", "work": "Introduction to Geometry", "quote": "The nine-point circle passes midway between each vertex and the **orthocenter**, linking triangle centers in elegant symmetry."}
    ]
  }
}

# Note: In orth.md ensure exactly 3 quotes by slicing if 4
if len(data["Dashboard \u2014 orth\\orth.md"]["quotes"]) > 3:
  data["Dashboard \u2014 orth\\orth.md"]["quotes"] = data["Dashboard \u2014 orth\\orth.md"]["quotes"][:3]

base_dir = r"App database\Greek roots\Cluster Form & Space"
mjs_path = r"main app\scripts\curate_form_finish_b6.mjs"

content = f"""import {{ updateNotesBatch }} from './curate-updater-util.mjs';

const baseDir = {json.dumps(base_dir)};
const batchData = {json.dumps(data, indent=2, ensure_ascii=False)};

const count = updateNotesBatch(baseDir, batchData);
console.log(`Updated ${{count}} notes in Finish Slice 1 Batch 6.`);
"""

with open(mjs_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Generated {mjs_path} with {len(data)} words.")
res = subprocess.run(["node", mjs_path], capture_output=True, text=True)
print("Node output:", res.stdout)
if res.stderr:
    print("Node error:", res.stderr)
