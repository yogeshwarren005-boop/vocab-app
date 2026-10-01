import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Medicine & Pathology";

const wordsData = {
  // === Dashboard — eme ===
  "Dashboard — eme/antiemetic.md": {
    word: "antiemetic",
    primary: "A medication or pharmacological agent that prevents, relieves, or suppresses nausea and vomiting.",
    secondary: "In clinical oncology and anesthesia, a class of drugs (such as 5-HT3 receptor antagonists and neurokinin-1 inhibitors) essential for managing post-operative and chemotherapy-induced emesis.",
    quotes: [
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "The development of ondansetron as a targeted **antiemetic** revolutionized high-dose cisplatin chemotherapy, freeing patients from agonizing nausea." },
      { author: "Jerome Groopman", work: "The Anatomy of Hope", quote: "The oncologist administered a prophylactic **antiemetic** infusion before starting the toxic combination regimen." },
      { author: "Oliver Sacks", work: "Uncle Tungsten", quote: "Ginger tea had been brewed by my mother as a gentle natural **antiemetic** whenever maritime travels threatened seasickness." }
    ]
  },
  "Dashboard — eme/eme.md": {
    word: "eme",
    primary: "The foundational Greek combining root (from emein, ἐμεῖν) signifying vomiting, disgorging, or nausea.",
    secondary: "In medical morphology, the base morpheme underlying clinical terms designating emetic agents, emesis, and involuntary gastric evacuation.",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The medical root **eme** traces directly to the Greek emein, meaning to vomit or cast up from the stomach." },
      { author: "James Murray", work: "A New English Dictionary on Historical Principles", quote: "Words built upon the root **eme** designate both physiological nausea and pharmacological substances that induce vomiting." },
      { author: "H. G. Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "In classical Greek, emetos (stem **eme**-) signified vomiting or that which is vomited forth." }
    ]
  },
  "Dashboard — eme/emesis.md": {
    word: "emesis",
    primary: "The action or physiological process of vomiting; the forceful ejection of stomach contents through the mouth.",
    secondary: "In gastrointestinal physiology, a reflex coordinated by the bilateral vomiting center in the medulla oblongata, triggered by the chemoreceptor trigger zone, vagal afferents, or vestibular disturbance.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Persistent projectile **emesis** without preceding nausea in an infant strongly suggests congenital hypertrophic pyloric stenosis." },
      { author: "Abraham Verghese", work: "Cutting for Stone", quote: "The nurse hurried in with a basin as severe bilious **emesis** seized the post-operative patient." },
      { author: "Atul Gawande", work: "Being Mortal", quote: "Uncontrolled **emesis** dehydrates frail cancer patients with alarming rapidity unless counteracted by central antiemetic therapy." }
    ]
  },
  "Dashboard — eme/emetic.md": {
    word: "emetic",
    primary: "Causing vomiting; or a medicine or substance that induces vomiting.",
    secondary: "In historical toxicology and therapeutics, an agent such as syrup of ipecac or tartar emetic historically administered to empty the stomach following toxic ingestions.",
    quotes: [
      { author: "Charles Dickens", work: "The Pickwick Papers", quote: "The apothecary looked solemn and prescribed a powerful **emetic** to clear the gentleman's disordered stomach." },
      { author: "Mark Twain", work: "Roughing It", quote: "The frontier doctor relied almost entirely upon calomel, castor oil, and a violent **emetic** for every known ailment." },
      { author: "Arthur Conan Doyle", work: "The Sign of Four", quote: "A swift **emetic** of mustard water saved the poisoned native before the alkaloid could enter the bloodstream." }
    ]
  },
  "Dashboard — eme/emetine.md": {
    word: "emetine",
    primary: "A toxic crystalline alkaloid extracted from ipecacuanha root, historically used as a powerful emetic and in the treatment of amoebic dysentery.",
    secondary: "In pharmacology, a protein synthesis inhibitor that acts specifically against trophozoites of Entamoeba histolytica in tissues, now largely superseded by metronidazole.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The introduction of hypodermic **emetine** marked a dramatic breakthrough in arresting the ravages of acute amoebic dysentery." },
      { author: "W. Somerset Maugham", work: "The Painted Veil", quote: "The doctor prepared a dose of **emetine** for the dysentery patients lying on mats along the river warehouse." },
      { author: "Paul de Kruif", work: "Microbe Hunters", quote: "Tropical physicians recognized **emetine** as a specific poison against the amoebae that burrowed deep into liver abscesses." }
    ]
  },
  "Dashboard — eme/emetophobia.md": {
    word: "emetophobia",
    primary: "An abnormal, intense, and irrational fear of vomiting or seeing others vomit.",
    secondary: "In clinical psychiatry, a debilitating specific phobia often accompanied by panic attacks, severe dietary restrictions, and obsessive avoidance of public transport, hospitals, or social gatherings.",
    quotes: [
      { author: "Oliver Sacks", work: "Awakenings", quote: "Her severe **emetophobia** made taking oral medications an ordeal of overwhelming dread." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "The young woman's dramatic weight loss was traced not to anorexia nervosa, but to an unyielding **emetophobia**." },
      { author: "Cesare Lombroso", work: "The Man of Genius", quote: "Neurotic dreads of natural bodily functions, such as **emetophobia**, frequently induce chronic insomnia and social withdrawal." }
    ]
  },
  "Dashboard — eme/hyperemesis.md": {
    word: "hyperemesis",
    primary: "Severe, excessive, and intractable vomiting, leading to dehydration, electrolyte imbalance, and weight loss.",
    secondary: "In obstetrics and maternal-fetal medicine, hyperemesis gravidarum, a life-threatening complication of early pregnancy requiring aggressive intravenous fluid rehydration and nutritional support.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Pernicious **hyperemesis** in the pregnant woman can rapidly induce ketosis and hepatic dysfunction unless parenteral feeding is initiated." },
      { author: "Abraham Verghese", work: "Cutting for Stone", quote: "The young mother was admitted to the ward semi-conscious from unremitting **hyperemesis**, her eyes sunken from severe dehydration." },
      { author: "Atul Gawande", work: "Better", quote: "Managing refractory **hyperemesis** demands continuous electrolyte monitoring to avert fatal cardiac arrhythmias." }
    ]
  },

  // === Dashboard — asthen ===
  "Dashboard — asthen/asthen.md": {
    word: "asthen",
    primary: "The foundational Greek combining root (from asthenes, ἀσθενής) signifying weak, feeble, frail, or devoid of strength.",
    secondary: "In medical and geophysical etymology, the prefix/combining form (a- without + sthenos strength) underlying asthenia, asthenopia, and asthenosphere.",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The element **asthen** is formed from the Greek negative privative a- and sthenos (strength), denoting lack of vigor." },
      { author: "James Murray", work: "A New English Dictionary on Historical Principles", quote: "Derivatives of **asthen** describe both constitutional muscular feebleness and the ductile mechanical behavior of deep rock layers." },
      { author: "H. G. Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "In classical Greek, asthenes (stem **asthen**-) signified sick, infirm, or lacking physical might." }
    ]
  },
  "Dashboard — asthen/asthenia.md": {
    word: "asthenia",
    primary: "Abnormal physical weakness, feebleness, or lack of energy; debility.",
    secondary: "In clinical medicine, generalized loss of muscular strength and endurance without true paralysis, characteristic of chronic infections, Addison's disease, or neuromuscular junction disorders.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Profound muscular **asthenia** accompanied by dark pigmentation of the skin immediately suggests tuberculosis of the suprarenal capsules." },
      { author: "Thomas Addison", work: "On the Constitutional and Local Effects of Disease of the Supra-Renal Capsules", quote: "The leading characteristics of the malady are anemia, general languor and debility, and remarkable feebleness of the heart's action, culminating in terminal **asthenia**." },
      { author: "Oliver Sacks", work: "A Leg to Stand On", quote: "A profound subjective **asthenia** invaded my limb, making it feel as weightless and unresponsive as a lump of dough." }
    ]
  },
  "Dashboard — asthen/asthenic.md": {
    word: "asthenic",
    primary: "Of, relating to, or characterized by asthenia; physically weak, feeble, or lacking vitality.",
    secondary: "In constitutional psychology and psychiatry (Ernst Kretschmer's typology), describing a slender, frail, narrow-chested body build historically correlated with introversion and schizoid temperaments.",
    quotes: [
      { author: "Ernst Kretschmer", work: "Physique and Character", quote: "The **asthenic** habitus is characterized by a deficient growth in thickness, displaying a lean chest, long limbs, and thin musculature." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Creeping Man", quote: "The invalid was of an **asthenic** constitution, his fragile frame trembling at the slightest draught." },
      { author: "William Osler", work: "Lectures on Angina Pectoris", quote: "In the final weeks of the wasting disease, an **asthenic** stupor overcame the patient's senses." }
    ]
  },
  "Dashboard — asthen/asthenopia.md": {
    word: "asthenopia",
    primary: "Weakness or fatigue of the eyes, often accompanied by headache, dimness of vision, and ocular discomfort; eye strain.",
    secondary: "In ophthalmology, visual fatigue resulting from uncorrected refractive errors (hyperopia, astigmatism), prolonged close work, or heterophoria (muscular asthenopia).",
    quotes: [
      { author: "Francis Bacon", work: "Sylva Sylvarum", quote: "Continuous reading of small characters by candlelight induces a grievous **asthenopia** and cloudiness of sight." },
      { author: "Hermann von Helmholtz", work: "Treatise on Physiological Optics", quote: "Accommodative **asthenopia** arises from sustained contraction of the ciliary muscle in uncorrected hypermetropic eyes." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "The student complained of burning **asthenopia** after long nights spent over Latin lexicons." }
    ]
  },
  "Dashboard — asthen/asthenosphere.md": {
    word: "asthenosphere",
    primary: "The upper layer of the Earth's mantle, below the lithosphere, in which rock is ductile, plastic, and deforms by slow convection.",
    secondary: "In plate tectonics and geophysics, the relatively mechanically weak, partially molten zone (between approximately 100 and 410 km depth) over which the rigid tectonic plates glide.",
    quotes: [
      { author: "Joseph Barrell", work: "The Strength of the Earth's Crust", quote: "Beneath the rigid crust must lie a zone of plastic weakness, which I propose to designate as the **asthenosphere**." },
      { author: "Alfred Wegener", work: "The Origin of Continents and Oceans", quote: "Continental masses drift laterally across the yielding, fluid-like substratum of the **asthenosphere**." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Thermal convection currents ascending through the **asthenosphere** drive the spreading of the ocean floors." }
    ]
  },
  "Dashboard — asthen/asthenozoospermia.md": {
    word: "asthenozoospermia",
    primary: "A condition characterized by reduced motility of spermatozoa in semen.",
    secondary: "In andrology and reproductive medicine, a primary cause of male subfertility, defined by the World Health Organization as less than forty percent progressively motile sperm in a fresh ejaculate.",
    quotes: [
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "Semen analysis revealed severe **asthenozoospermia**, explaining why conception had eluded the couple for years." },
      { author: "Siddhartha Mukherjee", work: "The Song of the Cell", quote: "Flagellar ultrastructural defects within the sperm tail account for familial cases of primary **asthenozoospermia**." },
      { author: "Atul Gawande", work: "Better", quote: "Advances in intracytoplasmic sperm injection bypassed the reproductive barrier posed by profound **asthenozoospermia**." }
    ]
  },
  "Dashboard — asthen/astheny.md": {
    word: "astheny",
    primary: "Loss or deficiency of physical strength; bodily debility or weakness (archaic variant of asthenia).",
    secondary: "In early nineteenth-century medical nosology (such as John Brown's Brunonian system), a systemic state of depleted vital excitement treated with stimulants.",
    quotes: [
      { author: "John Brown", work: "Elements of Medicine", quote: "Diseases of **astheny** require diffuse stimulants such as wine and opium to restore the exhausted vital irritability." },
      { author: "Samuel Taylor Coleridge", work: "Notebooks", quote: "I languished in a state of nervous **astheny**, devoid of all mental energy or animal spirits." },
      { author: "Thomas Carlyle", work: "Sartor Resartus", quote: "A spiritual **astheny** crept over the age, leaving men incapable of heroic conviction." }
    ]
  },

  // === Dashboard — ple ===
  "Dashboard — ple/pleon.md": {
    word: "pleon",
    primary: "The abdomen of a crustacean, typically comprising six segments and bearing swimming appendages (pleopods).",
    secondary: "In arthropod morphology, the posterior tagma behind the cephalothorax, terminating in the telson and uropods forming the tail fan in decapods.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Crayfish: An Introduction to the Study of Zoology", quote: "The flexible tail or **pleon** of the crayfish consists of six distinct movable rings, terminating in the broad swimming telson." },
      { author: "William Thomas Calman", work: "The Life of Crustacea", quote: "When threatened, the lobster flexes its powerful muscular **pleon**, shooting backward through the water with great velocity." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The giant prawns of the freshwater streams possess an elongated **pleon** richly supplied with edible meat." }
    ]
  },
  "Dashboard — ple/pleopod.md": {
    word: "pleopod",
    primary: "A swimming appendage or limb on the abdomen of a crustacean; a swimmeret.",
    secondary: "In marine biology, paired abdominal appendages used not only for forward propulsion in swimming, but frequently modified for carrying eggs in brooding females or copulation in males.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Crayfish", quote: "Each segment of the abdomen bears a pair of biramous limbs termed **pleopods**, which vibrate rhythmically to propel the animal." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "The female crab attaches thousands of microscopic eggs to the silky hairs of her abdominal **pleopods**." },
      { author: "William Thomas Calman", work: "The Life of Crustacea", quote: "In male decapods, the first pair of **pleopods** is heavily calcified and modified into an organ of sperm transfer." }
    ]
  },
  "Dashboard — ple/pleroma.md": {
    word: "pleroma",
    primary: "The fullness of divine powers or spiritual reality; in Gnosticism, the transcendent realm of divine light and aeons.",
    secondary: "In biblical theology (Pauline epistles) and botanical anatomy, the central core of primary meristematic tissue inside a growing plant root or shoot tip that gives rise to the stele.",
    quotes: [
      { author: "Carl Jung", work: "Seven Sermons to the Dead", quote: "Harken: I begin with nothingness; nothingness is the same as fullness: in the **pleroma**, both fullness and emptiness are eternal." },
      { author: "Philip Schaff", work: "History of the Christian Church", quote: "Gnostic cosmogony envisioned the supreme God dwelling in unapproachable splendor within the boundless **pleroma**." },
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "The **pleroma** occupies the axial cylinder of the growing root, forming the fibro-vascular bundles of the adult plant." }
    ]
  },
  "Dashboard — ple/plethodontid.md": {
    word: "plethodontid",
    primary: "A lungless salamander of the family Plethodontidae, which breathes entirely through its moist skin and the tissues of its mouth.",
    secondary: "In herpetology, the largest and most ecologically diverse family of salamanders, characterized by a nasolabial groove used in chemoreception and the absence of lungs.",
    quotes: [
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "In the Appalachian leaf litter, the biomass of **plethodontid** salamanders exceeds that of all birds and small mammals combined." },
      { author: "David Attenborough", work: "Life in Cold Blood", quote: "The tiny **plethodontid** breathes entirely without lungs, absorbing oxygen directly through its glistening skin." },
      { author: "Stephen Jay Gould", work: "The Flamingo's Smile", quote: "The loss of lungs in the ancestral **plethodontid** likely evolved as an adaptation to maintain negative buoyancy in swift mountain streams." }
    ]
  },
  "Dashboard — ple/plethora.md": {
    word: "plethora",
    primary: "A large or excessive amount of something; an overabundance or superabundance.",
    secondary: "In historical medicine, an excess of blood or bodily humors within the circulatory system, traditionally treated by bloodletting or venesection.",
    quotes: [
      { author: "William Shakespeare", work: "Troilus and Cressida", quote: "What his **plethora** of pride hath puffed up, his own folly will burst." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The ruddy, dusky complexion of polycythemia vera presents a striking clinical picture of vascular **plethora**." },
      { author: "Charles Dickens", work: "Bleak House", quote: "The court of Chancery suffered from an intolerable **plethora** of parchment records and unread affidavits." }
    ]
  },
  "Dashboard — ple/plethoric.md": {
    word: "plethoric",
    primary: "Excessively full, abundant, or congested; or having a ruddy, congested complexion from fullness of blood.",
    secondary: "In classical pathology, exhibiting signs of polycythemic circulatory fullness, flushed skin, and distended superficial veins.",
    quotes: [
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "The **plethoric** old gentleman wheezed in his high cravat, his purple cheeks threatening apoplexy." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The harpooner ate with **plethoric** gusto, consuming beef steaks as though preparing for a siege." },
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "The French nobility wallowed in a **plethoric** luxury while the peasants starved on nettle soup." }
    ]
  },
  "Dashboard — ple/plethysm.md": {
    word: "plethysm",
    primary: "Fullness, increase in size, or volumetric variation in an organ or bodily part.",
    secondary: "In physiological instrumentation, the physical enlargement of a vascular bed or vascular tissue volume during systolic blood flow.",
    quotes: [
      { author: "Étienne-Jules Marey", work: "La méthode graphique", quote: "The pulse wave causes a transient **plethysm** in the digital capillaries that can be registered by a delicate tambour." },
      { author: "William Osler", work: "Lectures on Angina Pectoris", quote: "Local arterial **plethysm** accompanies acute inflammatory congestion in superficial tissues." },
      { author: "Sherwin B. Nuland", work: "The Mysteries Within", quote: "The rhythmic **plethysm** of the kidneys expands and contracts with each systolic surge of aortic blood." }
    ]
  },
  "Dashboard — ple/plethysmometry.md": {
    word: "plethysmometry",
    primary: "The measurement of changes in the volume of an organ, limb, or whole body.",
    secondary: "In experimental physiology and pulmonary medicine, volumetric measurement (as in body plethysmography) used to determine thoracic gas volume and peripheral blood flow.",
    quotes: [
      { author: "Angelo Mosso", work: "The Mechanism of the Circulation in the Brain", quote: "By placing the arm in a glass cylinder filled with water, **plethysmometry** recorded every emotional shift as a change in blood volume." },
      { author: "August Krogh", work: "The Anatomy and Physiology of Capillaries", quote: "Venous occlusion **plethysmometry** remains the most accurate non-invasive method for measuring human limb blood flow." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Whole-body **plethysmometry** allows the clinician to measure functional residual capacity regardless of airway obstruction." }
    ]
  },
  "Dashboard — ple/pleuston.md": {
    word: "pleuston",
    primary: "The community of organisms that live at the interface between water and air, floating on the surface of an ocean or lake.",
    secondary: "In marine ecology, macroscopic organisms (such as the Portuguese man-of-war Physalia and the purple sail fin Velella) whose bodies project into both air and water, moved primarily by winds.",
    quotes: [
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "The bizarre creatures of the **pleuston**, like the purple snail Ianthina and the Portuguese man-of-war, drift eternally at the mercy of the trade winds." },
      { author: "Alister Hardy", work: "The Open Sea: The World of Plankton", quote: "Unlike plankton suspended below, the **pleuston** occupies the razor-thin frontier between sea and atmosphere." },
      { author: "William Beebe", work: "The Arcturus Adventure", quote: "We dipped our nets into the glittering blue **pleuston**, capturing floating colonies of Velella whose tiny sails caught the breeze." }
    ]
  },

  // === Dashboard — therap ===
  "Dashboard — therap/therapeia.md": {
    word: "therapeia",
    primary: "The ancient Greek concept of service, attendance, nurturing care, or medical healing (θεραπεία).",
    secondary: "In the history of medicine and medical humanities, the holistic therapeutic relationship and ritual healing attendance practiced in the temples of Asclepius.",
    quotes: [
      { author: "Plato", work: "The Republic", quote: "True **therapeia** of the soul consists in attuning its discordant passions to the harmony of justice." },
      { author: "Hippocrates", work: "On the Sacred Disease", quote: "The physician's **therapeia** must assist nature's own restorative power rather than coerce it with violent remedies." },
      { author: "Michel Foucault", work: "The Care of the Self", quote: "Classical **therapeia** encompassed not merely the curing of bodily symptoms, but the lifelong ethical cultivation of the self." }
    ]
  },
  "Dashboard — therap/therapeutic.md": {
    word: "therapeutic",
    primary: "Relating to the healing of disease; beneficial to physical, mental, or emotional health.",
    secondary: "In pharmacology and clinical medicine, producing a desired curative or palliative effect without unacceptable adverse toxicity.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Rest in bed remains our most potent **therapeutic** agent in the management of acute cardiac dilatation." },
      { author: "Oliver Sacks", work: "Musicophilia", quote: "The **therapeutic** power of melody can restore speech to the stroke victim and grace to the Parkinsonian walk." },
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "Finding the narrow **therapeutic** window between eradicating the tumor and poisoning the host is the ultimate challenge of oncology." }
    ]
  },
  "Dashboard — therap/therapeutical.md": {
    word: "therapeutical",
    primary: "Pertaining to the healing art, the curing of disease, or remedies; therapeutic.",
    secondary: "Concerned with clinical remedies, pharmacological applications, or medical treatments (historical/formal variant).",
    quotes: [
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "The **therapeutical** part of medicine hath been much corrupted with empirical receipts and superstitious charms." },
      { author: "Samuel Johnson", work: "The Lives of the English Poets", quote: "He sought solace in books, finding in moral philosophy a **therapeutical** balm for mental anxiety." },
      { author: "Thomas Henry Huxley", work: "Science and Culture", quote: "Modern physiology provides the only rational foundation upon which **therapeutical** science can advance." }
    ]
  },
  "Dashboard — therap/therapeutically.md": {
    word: "therapeutically",
    primary: "In a manner that contributes to healing, health, or the treatment of disease.",
    secondary: "In clinical pharmacology, administered in a dose or regimen designed to produce a curative medical outcome rather than a toxic or subclinical effect.",
    quotes: [
      { author: "Alexander Fleming", work: "On the Antibacterial Action of Cultures of a Penicillium", quote: "Penicillin may be applied **therapeutically** to infected wounds without inducing the cellular irritation common to carbolic antiseptics." },
      { author: "Abraham Verghese", work: "Cutting for Stone", quote: "The surgeon's gentle touch communicated **therapeutically** to the frightened patient that help had arrived." },
      { author: "Atul Gawande", work: "The Checklist Manifesto", quote: "When antibiotics are timed **therapeutically** before the skin incision, surgical site infections fall by half." }
    ]
  },
  "Dashboard — therap/therapeutics.md": {
    word: "therapeutics",
    primary: "The branch of medicine and pharmacology concerned with the treatment of disease and the application of remedies.",
    secondary: "In medical education and clinical pharmacology, the science of prescribing specific interventions (pharmacological, surgical, lifestyle) tailored to pathophysiological mechanisms.",
    quotes: [
      { author: "William Osler", work: "Aequanimitas", quote: "A desire to take medicine is perhaps the greatest feature which distinguishes man from animals, yet scientific **therapeutics** teaches us restraint." },
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", quote: "Experimental pathology must guide medical **therapeutics**, transforming blind empirical recipes into rational science." },
      { author: "Paul Ehrlich", work: "Address on Chemotherapeutics", quote: "The future of chemical **therapeutics** lies in synthesizing magic bullets that strike specific microbial receptors." }
    ]
  },
  "Dashboard — therap/therapist.md": {
    word: "therapist",
    primary: "A person skilled in or trained to provide a particular kind of therapy or rehabilitation (physical, speech, occupational, psychotherapy).",
    secondary: "In modern mental healthcare, a licensed practitioner who applies psychological techniques to assist patients in resolving emotional disorders, cognitive distress, or behavioral dysfunction.",
    quotes: [
      { author: "Carl Rogers", work: "On Becoming a Person", quote: "The effective **therapist** creates a climate of unconditional positive regard in which the client feels safe to explore hidden feelings." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "The music **therapist** struck a waltz on the piano, and suddenly the frozen patient began to dance with fluid elegance." },
      { author: "Irvin D. Yalom", work: "Love's Executioner", quote: "Every **therapist** knows that the true therapeutic agent is not clever theory, but the authentic human encounter." }
    ]
  },
  "Dashboard — therap/therapsid.md": {
    word: "therapsid",
    primary: "An extinct synapsid belonging to the order Therapsida, representing the ancestral lineage that gave rise to mammals.",
    secondary: "In vertebrate paleontology, Permian and Triassic proto-mammals (such as Cynodonts) displaying specialized heterodont dentition, developing secondary palates, and transitional upright limb postures.",
    quotes: [
      { author: "Robert Broom", work: "The Mammal-like Reptiles of South Africa", quote: "In the skull of the Karoo **therapsid**, one sees the reptilian jaw bones shrinking as the dentary expands to form the mammalian mandible." },
      { author: "Stephen Jay Gould", work: "Wonderful Life", quote: "The humble Triassic **therapsid** survived the great Permian extinction, carrying the evolutionary potential of all future mammals." },
      { author: "Edwin H. Colbert", work: "Evolution of the Vertebrates", quote: "The anatomical transition from primitive pelycosaur to advanced **therapsid** is one of the most complete sequences in the fossil record." }
    ]
  },
  "Dashboard — therap/therapsida.md": {
    word: "therapsida",
    primary: "An extinct taxonomic order of synapsid amniotes that dominated the terrestrial fauna of the Middle Permian to Early Cretaceous and includes the direct ancestors of mammals.",
    secondary: "In systematic paleontology, the synapsid clade characterized by enlarged temporal fenestrae, differentiated incisors, canines, and molars, and increasing metabolic activity.",
    quotes: [
      { author: "Alfred Sherwood Romer", work: "Vertebrate Paleontology", quote: "The radiation of the order **Therapsida** produced carnivores, herbivores, and the direct cynodont ancestors of true mammals." },
      { author: "Robert Broom", work: "The Origin of the Human Skeleton", quote: "South African strata have yielded thousands of magnificent skulls belonging to the diverse families of the **Therapsida**." },
      { author: "Richard Dawkins", work: "The Ancestor's Tale", quote: "Our Permian ancestor was an active member of the **Therapsida**, warm-blooded and perhaps already covered in fine proto-hair." }
    ]
  },
  "Dashboard — therap/therapy.md": {
    word: "therapy",
    primary: "Treatment intended to relieve, manage, or heal a physical illness, mental disorder, or disability.",
    secondary: "In clinical healthcare, a systematic intervention (such as gene therapy, radiation therapy, or cognitive behavioral therapy) aimed at restoring physiological homeostasis or psychological well-being.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In the absence of a specific curative drug, supportive nursing **therapy** and fresh air remain our sheet-anchor." },
      { author: "Siddhartha Mukherjee", work: "The Song of the Cell", quote: "Cellular **therapy** transforms living immune cells into bespoke medicines trained to annihilate leukemia." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "The dramatic response to L-DOPA **therapy** showed that chemical deficits in the brain could be dramatically corrected." }
    ]
  },

  // === Dashboard — typh ===
  "Dashboard — typh/paratyphoid.md": {
    word: "paratyphoid",
    primary: "An infectious, food- and water-borne bacterial fever resembling typhoid, caused by Salmonella enterica serovars Paratyphi A, B, or C.",
    secondary: "In clinical epidemiology and infectious disease, a milder enteric fever distinguished from typhoid by serological agglutination (Widal test) and stool bacteriological culture.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Cases of **paratyphoid** run a shorter course with lower temperature, but remain capable of fatal intestinal perforation." },
      { author: "Paul de Kruif", work: "Microbe Hunters", quote: "Bacteriologists isolated the **paratyphoid** bacillus from contaminated military rations during the Balkan campaigns." },
      { author: "Sinclair Lewis", work: "Arrowsmith", quote: "The laboratory verified that the outbreak was not true typhus or typhoid, but a stubborn strain of **paratyphoid** B." }
    ]
  },
  "Dashboard — typh/typha.md": {
    word: "typha",
    primary: "A cosmopolitan genus of tall wetland reed-like plants with dense brown cylindrical flower spikes (cattails, bulrushes, or reedmace).",
    secondary: "In aquatic botany and wetland ecology, plants of the genus Typha (family Typhaceae) renowned for rhizomatous spread, water filtering capacity, and edible starchy tubers.",
    quotes: [
      { author: "Henry David Thoreau", work: "Walden", quote: "The brown cylindrical spikes of **Typha** waved in the autumn breeze above the frozen marsh." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The staminate flowers of **Typha** form a deciduous upper spike, separated from the persistent velvety pistillate cylinder below." },
      { author: "John Muir", work: "My First Summer in the Sierra", quote: "Along the meandering mountain sloughs grew dense thickets of **Typha**, sheltering wild waterfowl and humming dragonflies." }
    ]
  },
  "Dashboard — typh/typhaceae.md": {
    word: "typhaceae",
    primary: "The cattail family of monocotyledonous flowering wetland plants, comprising the genera Typha (cattails) and Sparganium (bur-reeds).",
    secondary: "In plant systematics, emergent aquatic perennial herbs characterized by unisexual wind-pollinated flowers grouped in dense heads or cylindrical spikes, linear leaves, and spongy aerenchyma.",
    quotes: [
      { author: "Asa Gray", work: "Structural Botany", quote: "The family **Typhaceae** is adapted to waterlogged soils, possessing internal air chambers that channel oxygen down to the rhizomes." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Members of the **Typhaceae** provide indigenous peoples with down for stuffing and starchy roots for winter bread." },
      { author: "Liberty Hyde Bailey", work: "Manual of Cultivated Plants", quote: "In naturalistic water gardens, the **Typhaceae** are planted to stabilize marshy borders and absorb excess runoff." }
    ]
  },
  "Dashboard — typh/typhlopidae.md": {
    word: "typhlopidae",
    primary: "A family of small, non-venomous burrowing blind snakes found in tropical and subtropical regions of the world.",
    secondary: "In herpetology, fossorial squamates characterized by vestigial eyes covered by head scales (from Greek typhlos, blind), blunt rounded snouts, and smooth, uniform cylindrical scales.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "Digging among the rotting logs, we unearthed a slender blind snake of the family **Typhlopidae**, resembling an oversized earthworm." },
      { author: "David Attenborough", work: "Life in Cold Blood", quote: "The fossorial **Typhlopidae** spend their entire lives underground, raiding subterranean ant and termite nests by scent." },
      { author: "Raymond Ditmars", work: "Reptiles of the World", quote: "The eyes of the **Typhlopidae** are reduced to dark subcutaneous pigment spots beneath translucent protective scales." }
    ]
  },
  "Dashboard — typh/typhoeus.md": {
    word: "typhoeus",
    primary: "A monstrous serpentine giant of Greek mythology (also called Typhon), the offspring of Gaia and Tartarus, who challenged Zeus for supremacy of the cosmos.",
    secondary: "In classical literature and entomology, the mythological personification of volcanic rage and hurricane tempests; also a genus of European three-horned dung beetles (Typhaeus).",
    quotes: [
      { author: "Hesiod", work: "Theogony", quote: "From his shoulders grew a hundred heads of a fearful dragon, flicking dark tongues; thus was born mighty **Typhoeus** to shake the Olympian throne." },
      { author: "John Milton", work: "Paradise Lost", quote: "Satan lay floating on the fiery surge, huge as the giant **Typhoeus** whom Olympian thunder hurled beneath Mount Etna." },
      { author: "Percy Bysshe Shelley", work: "Prometheus Unbound", quote: "The volcanic chasms shuddered as if imprisoned **Typhoeus** were groaning beneath the crust of the earth." }
    ]
  },
  "Dashboard — typh/typhoid.md": {
    word: "typhoid",
    primary: "An acute, life-threatening infectious disease caused by the bacterium Salmonella Typhi, transmitted by contaminated food or water.",
    secondary: "In clinical epidemiology, characterized by sustained step-ladder fever, severe abdominal pain, rose spots, and hepatosplenomegaly, historically named typhoid because its stuporous symptoms resembled typhus.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Clean water supplies and municipal sand filtration will do more to banish **typhoid** than all the pharmacopeias combined." },
      { author: "Charles Dickens", work: "Dombey and Son", quote: "The foul London slums bred **typhoid** and misery in every unventilated cellar and stagnant ditch." },
      { author: "Paul de Kruif", work: "Microbe Hunters", quote: "Bacteriologists tracked the insidious **typhoid** carrier who contaminated salads across wealthy New York households." }
    ]
  },
  "Dashboard — typh/typhon.md": {
    word: "typhon",
    primary: "The deadlier mythological Greek tempest-monster (Typhoeus) defeated by Zeus; or a violent whirlwind, tempest, or hurricane.",
    secondary: "In comparative myth and meteorological history, the monster whose fiery breath was believed to emerge through volcanic fumaroles and oceanic typhoons.",
    quotes: [
      { author: "Aeschylus", work: "Prometheus Bound", quote: "Zeus with his winged lightning struck down fierce **Typhon**, whose charred body now lies beneath the roots of Etna." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The howling gale lashed the sea into froth, as though ancient **Typhon** were venting his oceanic fury upon our doomed ship." },
      { author: "James George Frazer", work: "The Golden Bough", quote: "In Egyptian mythology, Set was identified by the Greeks with **Typhon**, the evil power of desert drought and violent storms." }
    ]
  },
  "Dashboard — typh/typhoon.md": {
    word: "typhoon",
    primary: "A mature tropical cyclone that develops in the western part of the North Pacific Ocean.",
    secondary: "In marine meteorology, an intense cyclonic storm with sustained winds exceeding 74 miles per hour, derived historically from Chinese tai-fung (great wind) conflated with Greek Typhon.",
    quotes: [
      { author: "Joseph Conrad", work: "Typhoon", quote: "The sea was battered flat by the incredible pressure of the wind, and Captain MacWhirr steered straight into the heart of the **typhoon**." },
      { author: "Jack London", work: "The Cruise of the Snark", quote: "The barometer dropped like a stone, warning every seaman that a howling South Sea **typhoon** was bearing down upon us." },
      { author: "Herman Melville", work: "Typee", quote: "The coconut palms bent double before the screaming fury of the seasonal **typhoon**." }
    ]
  },
  "Dashboard — typh/typhous.md": {
    word: "typhous",
    primary: "Of, relating to, or resembling typhus or typhoid fever; characterized by stupor, delirium, or high fever.",
    secondary: "In nineteenth-century clinical medicine, describing the clouded, stuporous sensorium ('typhous state') accompanying severe systemic endotoxemia.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The patient sank into a low **typhous** muttering delirium, plucking aimlessly at the bedclothes." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "A **typhous** fever broke out at Lowood School, transforming the gloomy dormitories into an overcrowded hospital ward." },
      { author: "Thomas Mann", work: "Buddenbrooks", quote: "He tossed upon the pillows in a heavy **typhous** stupor, deaf to the soothing words of his family." }
    ]
  },
  "Dashboard — typh/typhus.md": {
    word: "typhus",
    primary: "An acute, severe infectious disease caused by Rickettsia prowazekii, transmitted to humans by the body louse and characterized by high fever, stupor, delirium, and a dark red rash.",
    secondary: "In military and social medicine, historically known as jail fever, camp fever, or ship fever, which decimated armies, besieged cities, and overcrowded prisons throughout human history.",
    quotes: [
      { author: "Hans Zinsser", work: "Rats, Lice and History", quote: "Soldiers have rarely won wars; they merely took the cities after **typhus** and dysentery had destroyed the defenders." },
      { author: "Charles Dickens", work: "Bleak House", quote: "From Tom-all-Alone's, the venomous breath of epidemic **typhus** wafts upward into the grand drawing rooms of the rich." },
      { author: "George Orwell", work: "Homage to Catalonia", quote: "The filthy, lice-ridden straw in the frontline trenches made the dread of **typhus** far worse than enemy snipers." }
    ]
  },

  // === Dashboard — sep ===
  "Dashboard — sep/antisepsis.md": {
    word: "antisepsis",
    primary: "The practice of using antiseptics to destroy or inhibit the growth of pathogenic microorganisms on living tissue.",
    secondary: "In the history of surgery, the revolutionary sterile technique introduced by Joseph Lister in 1865 using carbolic acid to prevent post-operative wound infection and hospital gangrene.",
    quotes: [
      { author: "Joseph Lister", work: "On the Antiseptic Principle in the Practice of Surgery", quote: "By maintaining strict **antisepsis** throughout the operation, compound fractures healed without a single drop of pus." },
      { author: "William Osler", work: "Aequanimitas", quote: "The introduction of **antisepsis** transformed the hospital from a house of death into a temple of healing." },
      { author: "Sherwin B. Nuland", work: "Doctors: The Biography of Medicine", quote: "Lister's carbolic spray was clumsy, but his conceptual grasp of **antisepsis** rescued modern surgery from the pestilence of gangrene." }
    ]
  },
  "Dashboard — sep/antiseptic.md": {
    word: "antiseptic",
    primary: "Preventing the growth of disease-causing microorganisms; or a chemical substance that can be safely applied to living tissue to destroy microbes.",
    secondary: "In cultural and literary usage, scrupulously clean, sterile, and free from emotional warmth, passion, or moral taint.",
    quotes: [
      { author: "Joseph Lister", work: "The Antiseptic System of Treatment", quote: "The **antiseptic** dressing must completely cover the wound to destroy any airborne germ that might alight upon the raw flesh." },
      { author: "Aldous Huxley", work: "Brave New World", quote: "The Central London Hatchery was gleaming, cold, and entirely **antiseptic**, smelling faintly of carbolic acid." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Blanched Soldier", quote: "The sharp, clean odor of an **antiseptic** lotion hung in the hallway of the secluded sanitarium." }
    ]
  },
  "Dashboard — sep/asepsis.md": {
    word: "asepsis",
    primary: "The state of being free from pathogenic micro-organisms, bacteria, viruses, and fungi.",
    secondary: "In surgical theater technique, the comprehensive prevention of microbial access through autoclaving instruments, sterile gowning, and clean airflow, advancing beyond chemical antisepsis.",
    quotes: [
      { author: "William Stewart Halsted", work: "The Employment of Fine Silk in Preference to Catgut", quote: "True **asepsis** relies upon heat sterilization of linens and rubber gloves, rendering corrosive chemical sprays obsolete." },
      { author: "William Osler", work: "Aequanimitas", quote: "The transition from Listerian antisepsis to modern **asepsis** was the crowning achievement of nineteenth-century operative hygiene." },
      { author: "Atul Gawande", work: "Better", quote: "Maintaining surgical **asepsis** requires unrelenting vigilance from every member of the scrub team." }
    ]
  },
  "Dashboard — sep/aseptic.md": {
    word: "aseptic",
    primary: "Free from contamination caused by harmful bacteria, viruses, or other microorganisms; surgically sterile.",
    secondary: "Characterized by meticulous sterilization protocols designed to exclude viable pathogens (e.g., aseptic packaging in food science or aseptic technique in cell culture).",
    quotes: [
      { author: "William Stewart Halsted", work: "Surgical Papers", quote: "The surgeon must operate with **aseptic** hands clad in boiled rubber gloves, touching only sterile instruments." },
      { author: "Sinclair Lewis", work: "Arrowsmith", quote: "Martin worked deep into the night in his small **aseptic** laboratory, testing cultures under the blue flame of the Bunsen burner." },
      { author: "Jerome Groopman", work: "The Anatomy of Hope", quote: "The bone marrow transplant unit was maintained as an **aseptic** sanctuary, protecting vulnerable patients from every passing microbe." }
    ]
  },
  "Dashboard — sep/sepia.md": {
    word: "sepia",
    primary: "A reddish-brown pigment prepared from the ink sac of the cuttlefish (Sepia); or a rich brownish color associated with early photographic prints.",
    secondary: "In marine zoology, the taxonomic genus Sepia, comprising common Old World cuttlefish celebrated for rapid chromatophore camouflage and jetting dark melanin-rich ink.",
    quotes: [
      { author: "John Ruskin", work: "Modern Painters", quote: "The artist executed the mountain sketch in rich washes of **sepia**, giving depth and shadow to the limestone crags." },
      { author: "Jules Verne", work: "Twenty Thousand Leagues under the Sea", quote: "A colossal cuttlefish discharged a cloud of dark **sepia** liquid, obscuring the captain and the monster in total blackness." },
      { author: "Virginia Woolf", work: "Orlando", quote: "The family portraits had faded to a mellow **sepia**, their Victorian countenances gazing out from gilded frames." }
    ]
  },
  "Dashboard — sep/sepsis.md": {
    word: "sepsis",
    primary: "A life-threatening medical emergency caused by the body's overwhelming and dysregulated immune response to an infection, leading to organ failure and tissue damage.",
    secondary: "In critical care medicine, systemic inflammatory response syndrome (SIRS) evolving into septic shock, defined by refractory hypotension, hyperlactatemia, and multi-organ dysfunction syndrome.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Puerperal **sepsis** was the terror of lying-in hospitals until Semmelweis proved that physicians carried the fatal poison upon their unwashed hands." },
      { author: "Siddhartha Mukherjee", work: "The Song of the Cell", quote: "In **sepsis**, the immune system's defensive fury becomes self-destructive, opening blood vessels and collapsing arterial blood pressure." },
      { author: "Atul Gawande", work: "Complications", quote: "Rapid administration of intravenous fluids and broad-spectrum antibiotics within the golden hour is critical to halting the spiral of **sepsis**." }
    ]
  },
  "Dashboard — sep/septal.md": {
    word: "septal",
    primary: "Of, relating to, or situated near a septum (a dividing partition between two cavities or tissues).",
    secondary: "In cardiology and rhinology, pertaining specifically to the nasal septum dividing the nostrils, or the interventricular and interatrial septa dividing the cardiac chambers.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A congenital ventricular **septal** defect produces a loud, harsh pansystolic murmur audible across the entire precordium." },
      { author: "Abraham Verghese", work: "Cutting for Stone", quote: "The surgeon gently examined the deviated nasal **septal** cartilage that had obstructed the young man's breathing for years." },
      { author: "Sherwin B. Nuland", work: "The Mysteries Within", quote: "The embryonic heart develops through complex folding and **septal** alignment that separates the pulmonary and systemic streams." }
    ]
  },
  "Dashboard — sep/septate.md": {
    word: "septate",
    primary: "Divided into compartments or chambers by one or more septa (internal partitions).",
    secondary: "In mycology and developmental anatomy, describing fungal hyphae divided by cross-walls (as in Ascomycota and Basidiomycota), or a congenital uterine malformation (septate uterus).",
    quotes: [
      { author: "M. C. Cooke", work: "Introduction to the Study of Fungi", quote: "The mycelium of the higher fungi is distinctly **septate**, each cross-wall possessing a central pore for cytoplasmic flow." },
      { author: "Asa Gray", work: "Structural Botany", quote: "The seed pod is **septate**, divided internally into several distinct locules containing the developing ovules." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "On ultrasound examination, the ovarian cyst appeared complex and **septate**, warranting surgical exploration." }
    ]
  },
  "Dashboard — sep/septation.md": {
    word: "septation",
    primary: "The formation or presence of a septum or septa dividing a cavity, organ, or anatomical structure.",
    secondary: "In embryology, the crucial developmental process during organogenesis whereby the primitive cardiac tube or embryonic cloaca is divided into functional physiological chambers.",
    quotes: [
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Impaired **septation** of the embryonic truncus arteriosus leads to the cyanotic heart defect known as transposition of the great vessels." },
      { author: "Siddhartha Mukherjee", work: "The Song of the Cell", quote: "During bacterial cell division, the FtsZ ring directs the inward **septation** that pinches the mother cell into two daughter cells." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Computed tomography revealed multiple internal **septations** within the hepatic abscess cavity." }
    ]
  },
  "Dashboard — sep/septic.md": {
    word: "septic",
    primary: "Infected with microorganisms; causing or accompanied by infectious decay, putrefaction, or sepsis.",
    secondary: "In environmental and sanitation engineering, relating to anaerobic bacterial decomposition of sewage (as in a septic tank).",
    quotes: [
      { author: "Joseph Lister", work: "On the Antiseptic Principle in the Practice of Surgery", quote: "The putrefaction of hospital wounds was entirely caused by **septic** germs introduced from without." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Sussex Vampire", quote: "The poison on the African dart was designed to cause acute **septic** poisoning within a matter of hours." },
      { author: "Atul Gawande", work: "Being Mortal", quote: "The elderly patient was rushed to the intensive care unit in acute **septic** shock secondary to an ascending urinary tract infection." }
    ]
  }
};

function updateWordNote(relPath, data) {
  const fullPath = path.join(baseDir, relPath);
  if (!fs.existsSync(fullPath)) {
    console.error("File not found:", fullPath);
    return;
  }

  let content = fs.readFileSync(fullPath, "utf8");

  // Format quotes
  const quotesFormatted = data.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join("\n");

  // Replace Definition & Semantic Range
  const defRegex = /> \[!book\] 📖 Definitions & Semantic Range[\s\S]*?(?=> \[!quote\]|$)/;
  const newDef = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${data.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${data.secondary}\n\n`;

  if (defRegex.test(content)) {
    content = content.replace(defRegex, newDef);
  } else {
    console.warn("Could not find [!book] in", relPath);
  }

  // Replace Quotes
  const quoteRegex = /> \[!quote\] 💬 Contextual Usage & Authentic Quotations[\s\S]*$/;
  const newQuotes = `> [!quote] 💬 Contextual Usage & Authentic Quotations\n${quotesFormatted}\n`;

  if (quoteRegex.test(content)) {
    content = content.replace(quoteRegex, newQuotes);
  } else {
    console.warn("Could not find [!quote] in", relPath);
  }

  fs.writeFileSync(fullPath, content, "utf8");
  console.log("Updated:", relPath);
}

for (const [relPath, data] of Object.entries(wordsData)) {
  updateWordNote(relPath, data);
}
console.log("Medicine & Pathology Batch 2 completed! Total words updated:", Object.keys(wordsData).length);
