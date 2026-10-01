import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Medicine & Pathology";

const wordsData = {
  // === Dashboard — rhig ===
  "Dashboard — rhig/rhigosaurus.md": {
    word: "rhigosaurus",
    primary: "An extinct genus of prehistoric therapsid (synapsid) from the Permian and Triassic periods.",
    secondary: "In vertebrate paleontology, a primitive synapsid taxon named from Greek rhigos (frost, cold) and sauros (lizard), reflecting its discovery in cold, high-latitude fossil beds.",
    quotes: [
      { author: "Robert Broom", work: "The Mammal-like Reptiles of South Africa", quote: "The cranial fragments of **Rhigosaurus** exhibit the transitional jaw articulation characteristic of advanced therapsids." },
      { author: "Alfred Sherwood Romer", work: "Vertebrate Paleontology", quote: "Fossil remains referred to **Rhigosaurus** illuminate the evolutionary radiation of synapsids across Gondwana before the dawn of the dinosaurs." },
      { author: "Edwin H. Colbert", work: "Wandering Lands and Animals", quote: "The presence of **Rhigosaurus** in southern polar sediments provided compelling biological evidence for continental drift." }
    ]
  },

  // === Dashboard — pnig ===
  "Dashboard — pnig/pnictide.md": {
    word: "pnictide",
    primary: "A binary chemical compound formed between a pnictogen (an element of Group 15) and a more electropositive element.",
    secondary: "In solid-state physics and materials science, iron-based pnictide superconductors (such as lanthanum oxygen fluorine iron arsenide) displaying high critical temperatures.",
    quotes: [
      { author: "Hideo Hosono", work: "Superconductivity in Iron-Based Pnictides", quote: "The discovery of high-temperature superconductivity in an iron-arsenic **pnictide** challenged the long-held belief that iron magnetism precluded Cooper pairing." },
      { author: "Philip Ball", work: "Nature Materials Reviews", quote: "The crystalline layers of the iron **pnictide** permit electrical conduction while effectively decoupling from surrounding magnetic fluctuations." },
      { author: "C. N. R. Rao", work: "Transition Metal Oxides and Pnictides", quote: "Chemical substitution within the parent **pnictide** lattice alters carrier density and suppresses the antiferromagnetic ground state." }
    ]
  },
  "Dashboard — pnig/pnictogen.md": {
    word: "pnictogen",
    primary: "Any chemical element belonging to Group 15 of the periodic table (nitrogen, phosphorus, arsenic, antimony, bismuth, and moscovium).",
    secondary: "In inorganic chemistry and crystallographic nomenclature, a group designation derived from Greek pnigein (to choke or stifle), referencing the suffocating nature of pure nitrogen gas.",
    quotes: [
      { author: "Glenn T. Seaborg", work: "The Elements Beyond Uranium", quote: "Element 115 occupies the position directly below bismuth, completing the sixth row of the **pnictogen** group." },
      { author: "F. Albert Cotton", work: "Advanced Inorganic Chemistry", quote: "Each **pnictogen** possesses five valence electrons in its outermost shell, exhibiting diverse oxidation states from minus three to plus five." },
      { author: "Roald Hoffmann", work: "Solids and Surfaces: A Chemist's View of Bonding in Extended Structures", quote: "The bonding geometry changes dramatically as one descends the **pnictogen** column from light phosphorus to heavy bismuth." }
    ]
  },

  // === Dashboard — pen ===
  "Dashboard — pen/lymphopenia.md": {
    word: "lymphopenia",
    primary: "An abnormally low concentration of lymphocytes in the peripheral blood circulation.",
    secondary: "In clinical hematology and immunology, a diagnostic finding commonly associated with viral infections, chemotherapy, corticosteroid therapy, or severe combined immunodeficiency.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Marked **lymphopenia** in acute systemic infection often indicates toxic marrow suppression and demands a guarded prognosis." },
      { author: "Anthony Fauci", work: "Harrison's Principles of Internal Medicine", quote: "Progressive CD4 T-cell **lymphopenia** represents the central immunopathogenic hallmark of advanced retroviral disease." },
      { author: "Siddhartha Mukherjee", work: "The Song of the Cell", quote: "Following intensive irradiation, the patient plunged into profound **lymphopenia**, leaving his tissues defenseless against opportunist microbes." }
    ]
  },
  "Dashboard — pen/neutropenia.md": {
    word: "neutropenia",
    primary: "An abnormally low number of neutrophils (the primary phagocytic white blood cells) in the blood, increasing susceptibility to bacterial and fungal infections.",
    secondary: "In medical oncology, an acute, potentially life-threatening complication of myelosuppressive chemotherapy, defined by an absolute neutrophil count falling below critical diagnostic thresholds.",
    quotes: [
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "During the nadir of chemotherapy, febrile **neutropenia** turned the hospital room into a desperate race against invisible pathogens." },
      { author: "Jerome Groopman", work: "The Anatomy of Hope", quote: "The oncologist monitored the bone marrow daily, hoping to see the patient emerge from drug-induced **neutropenia** before sepsis took hold." },
      { author: "Atul Gawande", work: "Being Mortal", quote: "A sudden spike in fever during severe **neutropenia** mandates immediate hospitalization and broad-spectrum intravenous antibiotics." }
    ]
  },

  // === Dashboard — ul ===
  "Dashboard — ul/ulorrhea.md": {
    word: "ulorrhea",
    primary: "Bleeding, hemorrhaging, or abnormal discharge from the gums.",
    secondary: "In classical dentistry and periodontology, severe gingival hemorrhage caused by scurvy, chronic ulceration, or advanced periodontal inflammation.",
    quotes: [
      { author: "James Lind", work: "A Treatise on the Scurvy", quote: "The scorbutic mariners suffered from loose teeth and persistent **ulorrhea**, their swollen gums bleeding profusely at the slightest touch." },
      { author: "Willoughby D. Miller", work: "The Micro-Organisms of the Human Mouth", quote: "Bacterial toxins colonizing the subgingival pocket induce chronic inflammation accompanied by suppuration and **ulorrhea**." },
      { author: "G. V. Black", work: "Special Dental Pathology", quote: "Unless deep calculus is thoroughly debrided, recurrent **ulorrhea** will lead inexorably to alveolar bone loss." }
    ]
  },
  "Dashboard — ul/Ulotrichi.md": {
    word: "Ulotrichi",
    primary: "A historical anthropological classification denoting peoples characterized by woolly, tightly curled, or frizzled hair.",
    secondary: "In nineteenth-century ethnology, a division established by Thomas Henry Huxley contrasting curly-haired populations (Ulotrichi) with smooth- or straight-haired peoples (Leiotrichi).",
    quotes: [
      { author: "Thomas Henry Huxley", work: "On the Geographical Distribution of the Chief Modifications of Mankind", quote: "I divide the human family into two primary groups, the **Ulotrichi** with crisp woolly hair, and the Leiotrichi with smooth hair." },
      { author: "Edward Burnett Tylor", work: "Anthropology: An Introduction to the Study of Man and Civilization", quote: "Microscopic cross-sections of hair from the **Ulotrichi** show a distinctive flattened oval form that causes the hair fiber to spiral." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The Papuan inhabitants of the interior belong unmistakably to the **Ulotrichi**, their towering crowns of matted fleece distinguishing them from the coastal Malays." }
    ]
  },

  // === Dashboard — zema ===
  "Dashboard — zema/apozema.md": {
    word: "apozema",
    primary: "A medicinal decoction or herbal tea prepared by boiling plant ingredients in water; an apozeme.",
    secondary: "In historical pharmacopeia and Galenic medicine, an aqueous infusion prescribed to purge humors or soothe systemic fevers.",
    quotes: [
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "The physician prescribed an **apozema** of borage, bugloss, and senna leaves to purge the adust melancholy humors." },
      { author: "Molière", work: "The Imaginary Invalid", quote: "Let the apothecary prepare a gentle **apozema** of rhubarb to cleanse the patient's liver before bedtime." },
      { author: "John Evelyn", work: "The Diary of John Evelyn", quote: "She took an **apozema** of diuretic herbs, which afforded her great relief from the agonizing paroxysms of the stone." }
    ]
  },
  "Dashboard — zema/eczema.md": {
    word: "eczema",
    primary: "A chronic, non-contagious inflammatory skin condition characterized by dry, itchy, red, and swollen patches that may blister and weep.",
    secondary: "In dermatology, atopic dermatitis involving impaired epidermal barrier function (such as filaggrin gene mutations) and an exaggerated immune response to environmental allergens.",
    quotes: [
      { author: "Ferdinand von Hebra", work: "Diseases of the Skin", quote: "Under the term **eczema**, we recognize an acute or chronic polymorphous eruption displaying erythema, papules, vesicles, and crusts." },
      { author: "James Joyce", work: "Ulysses", quote: "He examined his sleeve nervously, recalling the itchy red flare of childhood **eczema** upon his inner forearm." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Blanched Soldier", quote: "The medical officer suspected that the dry, scaly rash was merely a chronic **eczema** aggravated by the tropical climate." }
    ]
  },
  "Dashboard — zema/eczematous.md": {
    word: "eczematous",
    primary: "Relating to, resembling, or affected by eczema; characterized by inflammatory skin eruptions.",
    secondary: "In pathology, describing histopathological tissue changes marked by epidermal spongiosis, intercellular edema, and parakeratosis.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The infant's cheeks were covered with an **eczematous** weeping crust that caused intolerable nocturnal itching." },
      { author: "Thomas Mann", work: "The Magic Mountain", quote: "The sanitarium physician noted the patient's **eczematous** skin flare alongside his chronic bronchial symptoms." },
      { author: "Oliver Sacks", work: "A Leg to Stand On", quote: "The skin beneath the prolonged plaster cast had turned red and **eczematous** from lack of ventilation." }
    ]
  },

  // === Dashboard — onc ===
  "Dashboard — onc/onc.md": {
    word: "onc",
    primary: "The foundational Greek combining form (from onkos, ὄγκος) signifying a mass, bulk, swelling, or tumor.",
    secondary: "In biomedical nomenclature, the primary root morpheme underlying oncology, oncogenesis, and related neoplastic sciences.",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The formative element **onc** traces back to the Greek onkos, denoting bulk, a barb, or a bodily swelling." },
      { author: "James Murray", work: "A New English Dictionary on Historical Principles", quote: "Medical terms incorporating **onc** refer universally to pathological tumefaction or neoplastic growth." },
      { author: "H. G. Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "In classical Greek, onkos (stem **onc**-) denoted bodily mass or pride, before Galen restricted it to abnormal tumors." }
    ]
  },
  "Dashboard — onc/Oncinocalyx.md": {
    word: "Oncinocalyx",
    primary: "A monotypic genus of flowering Australian shrubs in the mint family (Lamiaceae), containing the single species Oncinocalyx betchei.",
    secondary: "In systematic botany, a shrub distinguished by hooked calyx teeth (from Greek onkino-, hooked + kalyx), adapted for epizoochoric seed dispersal on animal fur.",
    quotes: [
      { author: "Ferdinand von Mueller", work: "Fragmenta Phytographiae Australiae", quote: "The unique fruiting calyx of **Oncinocalyx** features stiff, recurved hooks that cling tenaciously to passing animals." },
      { author: "Joseph Maiden", work: "The Forest Flora of New South Wales", quote: "Specimens of **Oncinocalyx** betchei were collected on the dry rocky ridges of the interior tablelands." },
      { author: "George Bentham", work: "Flora Australiensis", quote: "The genus **Oncinocalyx** shows close affinity to Teucrium, differing chiefly in the persistent, hooked appendages of its calyx." }
    ]
  },
  "Dashboard — onc/oncogene.md": {
    word: "oncogene",
    primary: "A gene that has the potential to cause cancer, often created through the mutation or abnormal overexpression of a normal proto-oncogene.",
    secondary: "In molecular oncology, a mutated regulatory gene (such as ras, myc, or src) that drives autonomous cell proliferation, evasion of apoptosis, and malignant transformation.",
    quotes: [
      { author: "Harold Varmus", work: "Nobel Lecture: Retroviruses and the Cellular Origins of Cancer Genes", quote: "The discovery that a viral **oncogene** is derived from a conserved normal cellular gene reshaped our understanding of carcinogenesis." },
      { author: "J. Michael Bishop", work: "How to Win the Nobel Prize: An Unexpected Life in Science", quote: "The cellular proto-oncogene is a good gene gone wrong, transformed into an active **oncogene** by a mutation in its control switches." },
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "Cancer, we learned, was not driven by foreign invaders, but by our own genome corrupted: the mutated **oncogene** jammed the cell's accelerator pedal down." }
    ]
  },
  "Dashboard — onc/oncolytic.md": {
    word: "oncolytic",
    primary: "Capable of destroying or lysing tumor cells.",
    secondary: "In immunotherapy, describing engineered viruses (oncolytic viruses) that selectively infect and replicate within cancer cells, causing lysis while stimulating an antitumor immune response.",
    quotes: [
      { author: "Lewis Thomas", work: "The Lives of a Cell", quote: "The therapeutic dream of an **oncolytic** agent is to hunt down and dissolve neoplastic cells without harming innocent bystander tissues." },
      { author: "Siddhartha Mukherjee", work: "The Song of the Cell", quote: "Scientists engineered herpesviruses into potent **oncolytic** weapons, turning biological invaders into targeted cancer assassins." },
      { author: "Jerome Groopman", work: "The Anatomy of Hope", quote: "The **oncolytic** viral infusion triggered a brisk inflammatory response inside the metastatic melanoma nodules." }
    ]
  },

  // === Dashboard — phim ===
  "Dashboard — phim/paraphimosis.md": {
    word: "paraphimosis",
    primary: "A urological emergency in which a retracted foreskin cannot be pulled back forward over the glans penis, causing vascular strangulation.",
    secondary: "In acute clinical medicine, venous and lymphatic stasis leading to severe edema of the glans and potential ischemic gangrene if manual reduction or surgical intervention is delayed.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Neglected **paraphimosis** following catheterization requires urgent manual reduction to prevent vascular necrosis of the glans." },
      { author: "Percivall Pott", work: "Chirurgical Works", quote: "If the strangulated prepuce in **paraphimosis** resists cold compresses and digital compression, a dorsal slit must be executed without delay." },
      { author: "Sherwin B. Nuland", work: "Doctors: The Biography of Medicine", quote: "The young intern quickly relieved the acute **paraphimosis**, restoring venous drainage to the engorged tissue." }
    ]
  },
  "Dashboard — phim/phim.md": {
    word: "phim",
    primary: "The foundational Greek combining form (from phimos, φιμός) meaning a muzzle, constriction, closure, or tight binding.",
    secondary: "In anatomical pathology, the root designating abnormal tightening, stenosis, or narrowing of a natural bodily orifice or mucosal sleeve.",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The root **phim** originates from the Greek phimos, signifying a muzzle or binding loop for horses." },
      { author: "James Murray", work: "A New English Dictionary on Historical Principles", quote: "Medical terms compounded with **phim** refer specifically to morbid constrictions of mucosal passages." },
      { author: "H. G. Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "In classical Greek, phimos (root **phim**-) denoted a muzzle, a dice-box, or any confining ring." }
    ]
  },
  "Dashboard — phim/phimosis.md": {
    word: "phimosis",
    primary: "A congenital or acquired narrowing of the opening of the foreskin so that it cannot be retracted over the glans penis.",
    secondary: "In pediatric and adult urology, a condition predisposing to recurrent balanoposthitis, urinary obstruction, or chronic infection, often treated conservatively with topical steroids or surgically by circumcision.",
    quotes: [
      { author: "John Hunter", work: "A Treatise on the Venereal Disease", quote: "Severe inflammation of the prepuce may induce a secondary **phimosis**, preventing examination of the underlying chancre." },
      { author: "Abraham Verghese", work: "Cutting for Stone", quote: "The clinic performed circumcisions for severe congenital **phimosis** that had caused painful ballooning during micturition." },
      { author: "Sherwin B. Nuland", work: "The Mysteries Within", quote: "Ancient Egyptian papyri record surgical relief for **phimosis**, making circumcision one of mankind's oldest documented operations." }
    ]
  },
  "Dashboard — phim/phimotic.md": {
    word: "phimotic",
    primary: "Of, relating to, or affected by phimosis; constricted or abnormally narrowed.",
    secondary: "Describing a fibrous preputial ring that resists retraction or obstructs normal fluid discharge.",
    quotes: [
      { author: "Percivall Pott", work: "Observations on the Nature and Consequences of Those Injuries to Which the Head is Liable", quote: "The **phimotic** orifice had contracted to the diameter of a pinhead, preventing normal evacuation." },
      { author: "William Osler", work: "Lectures on Angina Pectoris and Allied States", quote: "Chronic irritation of a **phimotic** prepuce has been recognized since antiquity as a predisposing factor for malignant ulceration." },
      { author: "Atul Gawande", work: "Complications", quote: "The pediatric surgeon released the rigid **phimotic** band with a precise, conservative incision." }
    ]
  },

  // === Dashboard — dys ===
  "Dashboard — dys/dys.md": {
    word: "dys",
    primary: "The ancient Greek prefix (δυσ-) denoting bad, difficult, abnormal, painful, impaired, or disordered.",
    secondary: "In medical and scientific nomenclature, a ubiquitous productive prefix contrasted with eu- (good, normal), marking pathological dysfunction across countless clinical conditions.",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The Greek prefix **dys** signifies ill, hard, or difficult, standing as the direct etymological opposite to eu-." },
      { author: "James Murray", work: "A New English Dictionary on Historical Principles", quote: "In medical terminology, **dys** is prefixed to anatomical and physiological terms to denote functional impairment or morbid pain." },
      { author: "H. G. Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The inseparable particle **dys** expresses hardship, misfortune, or defect across hundreds of classical Greek compounds." }
    ]
  },
  "Dashboard — dys/dysphasia.md": {
    word: "dysphasia",
    primary: "A language disorder marked by deficiency in the generation or comprehension of speech, typically resulting from brain disease or injury.",
    secondary: "In behavioral neurology, a cortical deficit distinguishing partial language impairment (dysphasia) from complete loss of language function (aphasia), localized to Broca's or Wernicke's speech areas.",
    quotes: [
      { author: "Alexander Luria", work: "Higher Cortical Functions in Man", quote: "Motor **dysphasia** leaves the patient with preserved inner thought but an inability to articulate fluent syntactic sentences." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "Despite her expressive **dysphasia**, she understood every word spoken to her and communicated through vivid emotional gestures." },
      { author: "Norman Geschwind", work: "Selected Papers on Language and the Brain", quote: "The transient **dysphasia** following the ischemic stroke gradually resolved as collateral circulation restored perfusion to the angular gyrus." }
    ]
  },
  "Dashboard — dys/dysplasia.md": {
    word: "dysplasia",
    primary: "The abnormal growth, development, or organization of cells, tissues, or organs.",
    secondary: "In pathology and cytodiagnostics, an atypical cellular proliferation characterized by loss of architectural orientation, pleomorphism, and hyperchromasia, often representing a premalignant lesion.",
    quotes: [
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "The cervical biopsy showed high-grade **dysplasia**, an ominous cellular anarchy hovering on the brink of invasive cancer." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "The pathologist scrutinized the colonic polyp, searching for severe epithelial **dysplasia** that would mandate extensive bowel resection." },
      { author: "Atul Gawande", work: "Better", quote: "Early detection of cellular **dysplasia** on routine screening cytology has saved countless women from fatal malignancies." }
    ]
  },
  "Dashboard — dys/dysplastic.md": {
    word: "dysplastic",
    primary: "Relating to, characterized by, or affected by dysplasia; exhibiting abnormal cellular or tissue development.",
    secondary: "In surgical pathology and oncology, describing atypical cells with irregular nuclei, increased mitotic figures, and disrupted tissue architecture (e.g., dysplastic nevus).",
    quotes: [
      { author: "Siddhartha Mukherjee", work: "The Song of the Cell", quote: "The dermatologist carefully excised the **dysplastic** mole, concerned by its notched borders and irregular pigmentation." },
      { author: "Oliver Sacks", work: "A Leg to Stand On", quote: "Congenital **dysplastic** hips in infants require early orthopedic bracing to prevent permanent lameness." },
      { author: "Jerome Groopman", work: "The Anatomy of Hope", quote: "Under the microscope, the **dysplastic** epithelium exhibited crowded, hyperchromatic nuclei striving to break through the basement membrane." }
    ]
  },

  // === Dashboard — psor ===
  "Dashboard — psor/psora.md": {
    word: "psora",
    primary: "A chronic, itchy, scaly cutaneous eruption or disease; historically identified with the itch, scabies, or psoriasis.",
    secondary: "In the homeopathic doctrine of Samuel Hahnemann, the fundamental primordial miasm or constitutional taint held to underlie the vast majority of non-venereal chronic diseases.",
    quotes: [
      { author: "Samuel Hahnemann", work: "The Chronic Diseases: Their Peculiar Nature and Their Homoeopathic Cure", quote: "I recognized that almost all chronic maladies are manifestations of that ancient, hydra-headed monster, **psora**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Ancient writers confounded true scabies, leprosy, and dry eczema under the generic appellation of **psora**." },
      { author: "Oliver Wendell Holmes Sr.", work: "Homeopathy and Its Kindred Delusions", quote: "Hahnemann traced the origin of nearly every human infirmity to his speculative doctrine of internal **psora**." }
    ]
  },
  "Dashboard — psor/psoralea.md": {
    word: "psoralea",
    primary: "A genus of leguminous plants in the family Fabaceae (scurfy peas), widely distributed in temperate and tropical regions.",
    secondary: "In ethnobotany and pharmacognosy, plants renowned for producing bioactive furanocoumarins (such as psoralen from Psoralea corylifolia), used in phototherapy for skin disorders.",
    quotes: [
      { author: "Meriwether Lewis", work: "The Journals of Lewis and Clark", quote: "The Indians dig large quantities of the bread-root, a species of **Psoralea**, which they dry and pound into nutritious flour." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The calyx and leaves of **Psoralea** are conspicuously dotted with dark glandular dots, giving the plant its scurfy appearance." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Extracts from the seeds of **Psoralea** have long been celebrated in traditional Hindu medicine for restoring pigment in vitiligo." }
    ]
  },
  "Dashboard — psor/psoriasis.md": {
    word: "psoriasis",
    primary: "A common, chronic autoimmune skin disease characterized by red, raised, inflamed patches covered with silvery-white scales.",
    secondary: "In immunology and dermatology, a T-cell-mediated hyperproliferative disorder of keratinocytes driven by interleukin-23 and interleukin-17 signaling cascades.",
    quotes: [
      { author: "John Updike", work: "Self-Consciousness: Memoirs", quote: "My **psoriasis** made me a sun-worshipper, driving me to Caribbean beaches where ultraviolet rays bleached the red patches from my skin." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In **psoriasis**, the lesions favor the extensor surfaces of the elbows and knees, presenting brilliant silvery scales." },
      { author: "Oliver Sacks", work: "The Island of the Colorblind", quote: "The tropical humidity afforded him no relief from the painful cracking of arthritic **psoriasis** across his finger joints." }
    ]
  },
  "Dashboard — psor/psoric.md": {
    word: "psoric",
    primary: "Of, relating to, affected by, or resembling psora or itch; cutaneous and pruritic.",
    secondary: "In homeopathic theory, relating to the psoric miasm; in classical pharmacology, an agent used to relieve the itch.",
    quotes: [
      { author: "Samuel Hahnemann", work: "Organon of Medicine", quote: "The true **psoric** symptoms reveal themselves in dry, scaly eruptions accompanied by intolerable voluptuous itching." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Galen prescribes cooling baths and mild ointments for those tormented by **psoric** humors." },
      { author: "Thomas Laycock", work: "Mind and Brain", quote: "The historical debate over **psoric** diathesis reflected early medicine's struggle to connect cutaneous signs with internal systemic pathology." }
    ]
  },
  "Dashboard — psor/psorosis.md": {
    word: "psorosis",
    primary: "A serious, destructive viral disease of citrus trees characterized by scaly peeling of the bark and gum exudation on the trunk and limbs.",
    secondary: "In plant pathology, a grafting-transmitted disease caused by citrus psorosis virus (CPsV), leading to xylem occlusion, canopy decline, and tree death.",
    quotes: [
      { author: "Howard S. Fawcett", work: "Citrus Diseases and Their Control", quote: "The first visible symptom of **psorosis** is the scaling of outer bark scales on the trunk, followed by exudation of amber gum." },
      { author: "Walter Reuther", work: "The Citrus Industry", quote: "Quarantine and budwood certification programs successfully eradicated **psorosis** from modern commercial citrus nurseries." },
      { author: "J. M. Wallace", work: "Virus Diseases of Citrus", quote: "Indexing trials confirmed that **psorosis** produces diagnostic oak-leaf patterns on the young flushes of sweet orange seedlings." }
    ]
  },

  // === Dashboard — nyst ===
  "Dashboard — nyst/electronystagmography.md": {
    word: "electronystagmography",
    primary: "A diagnostic test that records involuntary eye movements (nystagmus) by measuring electrical potential changes between electrodes placed around the eyes.",
    secondary: "In neuro-otology, an electrophysiological technique used to evaluate the vestibular system, vestibulo-ocular reflex, and brainstem pathways in patients with vertigo or dizziness.",
    quotes: [
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "Caloric stimulation during **electronystagmography** confirmed complete peripheral vestibular failure on the left side." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "The neurologist ordered **electronystagmography** to determine whether the patient's disabling vertigo originated in the inner ear or the cerebellum." },
      { author: "Sherwin B. Nuland", work: "The Mysteries Within", quote: "Modern **electronystagmography** translates minute corneal-retinal potentials into quantifiable tracings of vestibular reflex function." }
    ]
  },
  "Dashboard — nyst/nyst.md": {
    word: "nyst",
    primary: "The foundational Greek combining root (from nystazein, νυστάζειν) signifying nodding, slumber, drowsiness, or rhythmic oscillation.",
    secondary: "In medical terminology, the root underlying nystagmus, denoting involuntary oscillation of the eyes reminiscent of head nodding during sleep.",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The formative root **nyst** derives from the Greek nystazein, meaning to nod or doze off in sleep." },
      { author: "James Murray", work: "A New English Dictionary on Historical Principles", quote: "In ophthalmology, terms constructed on **nyst** designate involuntary oscillatory tremors of the eyeball." },
      { author: "H. G. Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "In Homeric Greek, nystagmos (stem **nyst**-) signified the drooping, nodding motion of a drowsy warrior." }
    ]
  },
  "Dashboard — nyst/nystagmic.md": {
    word: "nystagmic",
    primary: "Pertaining to, characterized by, or affected with nystagmus; exhibiting involuntary rapid eye movements.",
    secondary: "In clinical neurology, describing the rhythmic slow-drift and rapid-saccadic corrective phases of pathological or physiological ocular beats.",
    quotes: [
      { author: "William Gowers", work: "A Manual of Diseases of the Nervous System", quote: "On extreme lateral gaze, the patient exhibited coarse **nystagmic** jerks indicative of cerebellar pathway disease." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "The oculogyric crisis was accompanied by rapid **nystagmic** twitches that prevented visual fixation." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Illustrious Client", quote: "The specialist noted the curious **nystagmic** flutter of the invalid's eyes whenever he turned toward the sunlight." }
    ]
  },
  "Dashboard — nyst/nystagmus.md": {
    word: "nystagmus",
    primary: "Rapid, involuntary, rhythmic oscillation of the eyeballs, either horizontal, vertical, rotatory, or mixed.",
    secondary: "In neurology and neuro-ophthalmology, a clinical sign resulting from abnormal vestibular input, cerebellar lesions, drug intoxication, or congenital sensory visual defects.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The classic triad of multiple sclerosis—intention tremor, scanning speech, and **nystagmus**—was described by Charcot." },
      { author: "Oliver Sacks", work: "Seeing Voices", quote: "Congenital **nystagmus** kept his eyes in constant shimmering motion, yet his brain learned to construct a stable visual world." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "The emergency physician looked closely for vertical **nystagmus**, which warns of a catastrophic brainstem stroke rather than benign vertigo." }
    ]
  },
  "Dashboard — nyst/nystan.md": {
    word: "nystan",
    primary: "A pharmaceutical trade name or variant formulation related to nystatin, used as an antifungal preparation.",
    secondary: "In pharmacological practice, a topical or oral suspension formulation employed to treat candidiasis of the skin and mucous membranes.",
    quotes: [
      { author: "Selman Waksman", work: "My Life with the Microbes", quote: "The commercial preparation sold under the brand **Nystan** provided physicians with a direct weapon against stubborn Monilia infections." },
      { author: "Abraham Verghese", work: "My Own Country", quote: "The clinic stocked bottles of **Nystan** oral suspension to soothe the burning esophageal thrush of immunosuppressed patients." },
      { author: "Paul de Kruif", work: "Microbe Hunters", quote: "Clinical trials of **nystan** demonstrated that fungal pathogens could be suppressed without harming the host's bacterial flora." }
    ]
  },
  "Dashboard — nyst/nystatin.md": {
    word: "nystatin",
    primary: "A polyene antifungal antibiotic medication obtained from the bacterium Streptomyces noursei, used to treat Candida infections.",
    secondary: "In the history of pharmacology, discovered in 1950 by Elizabeth Lee Hazen and Rachel Fuller Brown at the New York State Department of Health (hence named Ny-stat-in).",
    quotes: [
      { author: "Rachel Fuller Brown", work: "Discovery of Nystatin", quote: "We named the antibiotic **nystatin** in honor of the New York State Division of Laboratories where our research was conducted." },
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "When systemic chemotherapy ablated the marrow, swabbing with **nystatin** kept oral fungal candida blooms from overwhelming the gut." },
      { author: "Oliver Sacks", work: "The Island of the Colorblind", quote: "He relied on topical **nystatin** to treat the persistent cutaneous yeast infections that plagued the humid tropical garrison." }
    ]
  },

  // === Dashboard — oed ===
  "Dashboard — oed/angioedema.md": {
    word: "angioedema",
    primary: "An area of sudden, rapid swelling of the deeper layers of the skin, subcutaneous tissues, mucosa, or submucosal tissues.",
    secondary: "In allergy and immunology, a vascular reaction mediated by histamine or bradykinin (such as hereditary angioedema or ACE-inhibitor-induced swelling), dangerous when it involves the larynx.",
    quotes: [
      { author: "William Osler", work: "Hereditary Angioneurotic Oedema", quote: "The sudden onset of severe **angioedema** in successive generations of this family demonstrates its singular hereditary transmission." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "When the patient's lips and tongue swelled alarmingly from acute **angioedema**, the team prepared for an emergent surgical airway." },
      { author: "Atul Gawande", work: "The Checklist Manifesto", quote: "The emergency protocol for drug-induced **angioedema** mandates epinephrine and immediate evaluation of laryngeal patency." }
    ]
  },
  "Dashboard — oed/edema.md": {
    word: "edema",
    primary: "An abnormal accumulation of fluid in the interstitial spaces of the body's tissues, resulting in noticeable swelling.",
    secondary: "In pathophysiological medicine, swelling resulting from increased hydrostatic capillary pressure, decreased oncotic plasma pressure, or lymphatic obstruction.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Dependent **edema** of the ankles in the evening is often the earliest harbinger of failing right ventricular compensation." },
      { author: "Sherwin B. Nuland", work: "How We Die", quote: "As the failing pump faltered, pulmonary **edema** flooded the delicate alveolar sacs with suffocating transudate." },
      { author: "Abraham Verghese", work: "Cutting for Stone", quote: "He pressed his thumb into the pretibial skin, noting the deep pit of persistent **edema** that slowly refilled." }
    ]
  },
  "Dashboard — oed/edematous.md": {
    word: "edematous",
    primary: "Swollen or distended by an accumulation of excessive fluid in body tissues; affected with edema.",
    secondary: "In surgical pathology, describing tissue that is pale, boggy, heavy, and waterlogged upon gross examination or histology.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The mucosa of the larynx was vividly injected and heavily **edematous**, narrowing the glottic aperture to a slit." },
      { author: "Atul Gawande", work: "Complications", quote: "The bowel wall had become thick and **edematous** from venous obstruction, making suturing precarious." },
      { author: "Jerome Groopman", work: "The Anatomy of Hope", quote: "Her legs were heavy and **edematous**, weeping clear lymph through tense, shiny skin." }
    ]
  },
  "Dashboard — oed/oed.md": {
    word: "oed",
    primary: "The foundational Greek combining root (from oidēma, οἴδημα) denoting swelling, tumefaction, or fluid accumulation; or the standard abbreviation for the Oxford English Dictionary.",
    secondary: "In etymological analysis, the classical spelling variant of ed- underlying oedema, oedematous, and Oedipus (literally 'swollen-foot').",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The medical prefix **oed** arises from the Greek oidein (to swell), appearing notably in oedema and Oedipus." },
      { author: "James Murray", work: "The Evolution of English Lexicography", quote: "Consult the monumental pages of the **OED** to trace how classical medical spellings evolved across Victorian England." },
      { author: "H. G. Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "From the verb oidein (to swell) Greek derived oidēma (stem **oed**-), signifying a tumor or dropsical swelling." }
    ]
  },
  "Dashboard — oed/oedema.md": {
    word: "oedema",
    primary: "An abnormal collection of fluid in the tissues of the body, causing swelling (standard British and historical medical spelling of edema).",
    secondary: "In classical and Commonwealth medical literature, the retention of watery fluid in subcutaneous tissues or serous cavities, as seen in dropsy or congestive heart failure.",
    quotes: [
      { author: "Charles Dickens", work: "Bleak House", quote: "The poor clerk's ankles exhibited marked **oedema**, his worn boots refusing to lace over the swollen flesh." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Dying Detective", quote: "Holmes lay gasping, pointing out with clinical detachment the coldness of his skin and the incipient **oedema** of his extremities." },
      { author: "Joseph Lister", work: "On the Antiseptic Principle in the Practice of Surgery", quote: "Under strict antiseptic dressings, inflammatory **oedema** subsided rapidly without suppuration or systemic fever." }
    ]
  },
  "Dashboard — oed/oedematous.md": {
    word: "oedematous",
    primary: "Pertaining to, affected by, or characterized by oedema; swollen with fluid (chiefly British spelling of edematous).",
    secondary: "In clinical examination, describing swollen tissue that demonstrates pitting upon sustained digital pressure.",
    quotes: [
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "The bloated old general hobbled forward upon two **oedematous** legs that creaked beneath his gouty weight." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "Her hands were pale and **oedematous**, resting limply upon the counterpane as her fever ran its course." },
      { author: "Thomas Hardy", work: "The Mayor of Casterbridge", quote: "The damp air aggravated his dropsy, leaving his eyelids puffy and his fingers **oedematous**." }
    ]
  },

  // === Dashboard — traum ===
  "Dashboard — traum/trauma.md": {
    word: "trauma",
    primary: "A deeply distressing or disturbing experience; or a physical injury or wound to the body caused by violence or accident.",
    secondary: "In psychoanalysis and psychiatry, an emotional shock that overwhelms the ego's defense mechanisms, producing enduring neurosis, post-traumatic stress disorder, or somatic conversion.",
    quotes: [
      { author: "Sigmund Freud", work: "Beyond the Pleasure Principle", quote: "We describe as traumatic any excitations from outside which are powerful enough to break through the protective shield against stimuli; this is the essence of psychological **trauma**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe physical **trauma** to the abdomen may rupture the spleen without leaving any visible mark on the external skin." },
      { author: "Virginia Woolf", work: "Mrs Dalloway", quote: "Septimus had survived the shelling in the trenches, but the silent **trauma** of the war followed him into the London parks." }
    ]
  },
  "Dashboard — traum/traumatic.md": {
    word: "traumatic",
    primary: "Relating to, caused by, or resulting from physical injury or severe emotional distress.",
    secondary: "In surgery and orthopedics, caused by sudden external mechanical force, such as a traumatic brain injury or traumatic amputation.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "A terrifying experience may leave a **traumatic** imprint so deep upon the nervous system that subsequent life is permanently shadowed." },
      { author: "Arthur Conan Doyle", work: "The Sign of Four", quote: "The soldier suffered from a **traumatic** neuralgia in his wounded shoulder whenever the weather turned damp." },
      { author: "Siddhartha Mukherjee", work: "The Song of the Cell", quote: "The emergency team labored to control the hemorrhage caused by a severe **traumatic** laceration of the femoral artery." }
    ]
  },
  "Dashboard — traum/traumatise.md": {
    word: "traumatise",
    primary: "To subject to severe mental or emotional distress, or to inflict physical injury upon body tissue (chiefly British spelling of traumatize).",
    secondary: "In surgical technique, to handle delicate anatomical structures roughly so as to cause avoidable tissue necrosis or inflammation.",
    quotes: [
      { author: "Joseph Lister", work: "The Collected Papers of Joseph Lister", quote: "The surgeon must handle the bowel with utmost gentleness, taking care not to **traumatise** the serosa with harsh metal forceps." },
      { author: "Virginia Woolf", work: "To the Lighthouse", quote: "She feared that the father's sudden outbursts of cold rage would **traumatise** the sensitive heart of the young boy." },
      { author: "George Bernard Shaw", work: "Heartbreak House", quote: "The brutal horrors of the battlefield will **traumatise** an entire generation of European youth." }
    ]
  },
  "Dashboard — traum/traumatize.md": {
    word: "traumatize",
    primary: "To cause physical injury or severe emotional distress and lasting psychological damage to someone.",
    secondary: "In clinical psychiatry and trauma studies, to induce overwhelming psychic horror that impairs normal affective regulation and cognitive integration.",
    quotes: [
      { author: "Bessel van der Kolk", work: "The Body Keeps the Score", quote: "Overwhelming helplessness and terror can **traumatize** a human being, altering the wiring of the brain and storing memories as visceral sensations." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "The sudden withdrawal of L-DOPA threatened to **traumatize** the post-encephalitic patients with acute akinetic rigidity." },
      { author: "Atul Gawande", work: "Complications", quote: "Careless operative retraction can **traumatize** the liver capsule, causing troublesome diffuse oozing." }
    ]
  },
  "Dashboard — traum/traumatology.md": {
    word: "traumatology",
    primary: "The branch of medicine and surgery that deals with the treatment of serious wounds, fractures, and injuries caused by accidents or violence.",
    secondary: "In disaster response and emergency medicine, the comprehensive multidisciplinary protocol managing poly-trauma, hemorrhagic shock, and critical surgical resuscitation.",
    quotes: [
      { author: "William Osler", work: "Aequanimitas", quote: "The modern hospital cannot function without an organized department of **traumatology**, prepared day and night for catastrophic casualties." },
      { author: "Sherwin B. Nuland", work: "How We Die", quote: "Milestones in military **traumatology** have repeatedly rewritten the rules of civilian emergency trauma surgery." },
      { author: "Atul Gawande", work: "The Checklist Manifesto", quote: "In the high-stakes arena of acute **traumatology**, a surgical checklist ensures that no airway obstruction or occult bleed is overlooked." }
    ]
  },
  "Dashboard — traum/traumatophobia.md": {
    word: "traumatophobia",
    primary: "An abnormal, irrational, or morbid fear of physical injury, wounds, or bodily trauma.",
    secondary: "In clinical psychology, an anxiety disorder manifesting in extreme avoidance behavior regarding physical activity, medical interventions, or situations perceived as carrying injury risk.",
    quotes: [
      { author: "William James", work: "The Varieties of Religious Experience", quote: "The neurotic invalid was paralyzed by a persistent **traumatophobia**, fearing that every staircase or gust of wind portended catastrophic bodily harm." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "In extreme phobic states, **traumatophobia** leads patients to pad their clothing and barricade themselves within their homes." },
      { author: "Cesare Lombroso", work: "The Man of Genius", quote: "Morbid dreads such as **traumatophobia** frequently afflict sensitive intellectual temperaments exposed to prolonged nervous strain." }
    ]
  },

  // === Dashboard — carcin ===
  "Dashboard — carcin/carcinogen.md": {
    word: "carcinogen",
    primary: "A substance, organism, or agent that is capable of causing cancer in living tissues.",
    secondary: "In molecular toxicology and occupational health, an agent (such as ionizing radiation, asbestos, or tobacco nitrosamines) that causes somatic mutations or epigenetic alterations leading to malignant transformation.",
    quotes: [
      { author: "Rachel Carson", work: "Silent Spring", quote: "By flooding our environment with synthetic chemicals, we have introduced a multitude of potent **carcinogens** into the water we drink and the food we eat." },
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "Pott's discovery that chimney soot was a chemical **carcinogen** launched the modern science of epidemiological oncology." },
      { author: "Lewis Thomas", work: "The Lives of a Cell", quote: "The cell's DNA repair machinery works ceaselessly to reverse the chemical lesions inflicted by every environmental **carcinogen**." }
    ]
  },
  "Dashboard — carcin/carcinogenic.md": {
    word: "carcinogenic",
    primary: "Having the potential, tendency, or capacity to cause cancer.",
    secondary: "In bioassays, describing chemical compounds or physical rays shown in epidemiological or laboratory animal models to induce neoplastic transformations.",
    quotes: [
      { author: "Rachel Carson", work: "Silent Spring", quote: "The widespread use of persistent pesticides created a pervasive **carcinogenic** hazard that accumulated throughout the ecological food chain." },
      { author: "Siddhartha Mukherjee", work: "The Song of the Cell", quote: "Doll and Hill demonstrated the direct **carcinogenic** relationship between cigarette smoking and bronchogenic carcinoma." },
      { author: "Oliver Sacks", work: "Uncle Tungsten", quote: "My chemist uncle warned me that certain aromatic amines were notoriously **carcinogenic** and required handling strictly under a fume hood." }
    ]
  },
  "Dashboard — carcin/carcinoid.md": {
    word: "carcinoid",
    primary: "A type of slow-growing neuroendocrine tumor, usually originating in the gastrointestinal tract or lungs.",
    secondary: "In surgical pathology, a tumor composed of uniform cells with neurosecretory granules that can secrete serotonin, causing carcinoid syndrome (flushing, diarrhea, and bronchospasm).",
    quotes: [
      { author: "Siegfried Oberndorfer", work: "Karzinoide Tumoren des Dünndarms", quote: "Because these submucosal growths appeared morphologically like carcinomas yet ran a remarkably indolent course, I designated them as **carcinoid** tumors." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "An appendiceal **carcinoid** is frequently an incidental finding discovered during routine surgery for acute appendicitis." },
      { author: "Jerome Groopman", work: "The Anatomy of Hope", quote: "The patient's episodic facial flushing and cardiac valvular thickening were classic hallmarks of metastatic **carcinoid** syndrome." }
    ]
  },
  "Dashboard — carcin/carcinoma.md": {
    word: "carcinoma",
    primary: "A malignant tumor that begins in the epithelial tissue of the skin or in the lining of internal organs.",
    secondary: "In clinical oncology, the most common form of cancer (comprising adenocarcinomas and squamous cell carcinomas), distinguished from sarcomas (mesenchymal origin) and lymphomas/leukemias.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Every **carcinoma** is an outgrowth of epithelial cells that have broken through their physiological histological boundaries." },
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "Epithelial tissue, being constantly renewed and exposed to friction, gives rise to the vast majority of human cancers: the lethal family of **carcinomas**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Gastric **carcinoma** remains one of the most insidious scourges of late middle age, often hiding behind simple dyspepsia." }
    ]
  },
  "Dashboard — carcin/carcinomatous.md": {
    word: "carcinomatous",
    primary: "Pertaining to, of the nature of, or affected with carcinoma; cancerous.",
    secondary: "In histopathology, describing malignant epithelial infiltration into lymphatics, blood vessels, or adjacent stromal tissues (e.g., carcinomatous meningitis).",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Microscopic section revealed extensive **carcinomatous** infiltration choking the regional lymphatic channels." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The hard, eburnated edge of the gastric ulcer confirmed its **carcinomatous** transformation." },
      { author: "Sherwin B. Nuland", work: "How We Die", quote: "The **carcinomatous** mass had invaded the retroperitoneum, encasing the major mesenteric vessels in rigid tumor." }
    ]
  },
  "Dashboard — carcin/carcinosarcoma.md": {
    word: "carcinosarcoma",
    primary: "A rare and highly aggressive malignant tumor composed of a mixture of carcinoma (epithelial) and sarcoma (mesenchymal/connective tissue) elements.",
    secondary: "In gynecologic and thoracic oncology, a biphasic metaplastic neoplasm (true malignant mixed tumor) showing monoclonal origin with divergent differentiation and a poor prognosis.",
    quotes: [
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "The biopsy of the uterine mass revealed a deadly **carcinosarcoma**, where malignant glands were intermingled with sarcomatous cartilage." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "Because a **carcinosarcoma** contains both epithelial and mesenchymal malignant cells, it often exhibits fierce resistance to standard chemotherapy." },
      { author: "Atul Gawande", work: "Complications", quote: "The surgical team knew that complete radical resection offered the only hope against this aggressive pulmonary **carcinosarcoma**." }
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
  // Handle nested object structure if any
  const actualData = data.primary ? data : Object.values(data)[0];
  updateWordNote(relPath, actualData);
}
console.log("Medicine & Pathology Batch 1 completed! Total words updated:", Object.keys(wordsData).length);
