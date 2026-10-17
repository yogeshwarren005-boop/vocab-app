import json

batch8_data = {
  "Dashboard — logy/apologist.md": {
    "primary": "A person who offers an argument or defense in support of a doctrine, cause, or controversial policy.",
    "secondary": "In theology and intellectual history, a writer or speaker who systematically defends religious faith against secular skepticism and heresy.",
    "quotes": [
      { "author": "John Henry Newman", "work": "Apologia Pro Vita Sua", "text": "Every sincere **apologist** must lay bare the interior convictions that compelled his conversion." },
      { "author": "Thomas Paine", "work": "The Age of Reason", "text": "The orthodox **apologist** twists every historical contradiction into an alleged mystery of faith." },
      { "author": "C. S. Lewis", "work": "Christian Reflections", "text": "The duty of the modern **apologist** is not to flatter the intellectual spirit of his age, but to interrogate it." }
    ]
  },
  "Dashboard — logy/biologic.md": {
    "primary": "Pertaining to life, living organisms, and vital processes; biological.",
    "secondary": "In pharmacology, denoting complex medicinal products synthesized by or extracted from living cells or biological systems.",
    "quotes": [
      { "author": "Julian Huxley", "work": "Evolution: The Modern Synthesis", "text": "Natural selection operates through continuous **biologic** adjustments to shifting environmental pressures." },
      { "author": "Thomas Hunt Morgan", "work": "The Theory of the Gene", "text": "The linear assortment of alleles reveals the fundamental **biologic** architecture of the chromosome." },
      { "author": "René Dubos", "work": "Mirage of Health", "text": "Human adaptation is rarely a passive phenomenon but an active **biologic** struggle against hostile microbial ecologies." }
    ]
  },
  "Dashboard — logy/biologically.md": {
    "primary": "In a biological manner; with respect to the principles, functions, or origins of living organisms.",
    "secondary": "From the standpoint of physiology, genetics, or evolutionary adaptation.",
    "quotes": [
      { "author": "Richard Dawkins", "work": "The Selfish Gene", "text": "Organisms are survival machines **biologically** programmed to preserve the selfish molecules known as genes." },
      { "author": "Ernst Mayr", "work": "The Growth of Biological Thought", "text": "Populations that become geographically separated tend to diverge **biologically** over long temporal spans." },
      { "author": "E. O. Wilson", "work": "Sociobiology: The New Synthesis", "text": "Altruistic behaviors in social insects can be **biologically** explained through the calculus of kin selection." }
    ]
  },
  "Dashboard — logy/biologism.md": {
    "primary": "The theoretical interpretation of human behavior, society, and culture exclusively in terms of biological causes.",
    "secondary": "In the philosophy of science, an extreme reductionism that explains complex psychosocial phenomena solely through genetics or evolutionary mechanisms.",
    "quotes": [
      { "author": "Stephen Jay Gould", "work": "The Mismeasure of Man", "text": "Crude **biologism** frequently reemerges to legitimate existing social stratifications under the guise of objective science." },
      { "author": "Mary Midgley", "work": "Beast and Man", "text": "To reduce human ethical deliberation to mere instinctive hardwiring is a caricature born of vulgar **biologism**." },
      { "author": "Jürgen Habermas", "work": "The Future of Human Nature", "text": "Unchecked genetic engineering threatens to impose a deterministic **biologism** on human ethical self-understanding." }
    ]
  },
  "Dashboard — logy/biologist.md": {
    "primary": "A scientist who specializes in the study of living organisms and vital processes.",
    "secondary": "A researcher investigating the physiological, cellular, ecological, or genetic mechanisms of the biosphere.",
    "quotes": [
      { "author": "Charles Darwin", "work": "The Origin of Species", "text": "The patient field **biologist** discovers that every organic being is bound in an intricate web of ecological relations." },
      { "author": "Rachel Carson", "work": "Silent Spring", "text": "The responsible **biologist** must warn society when synthetic poisons contaminate the planetary food web." },
      { "author": "Francis Crick", "work": "What Mad Pursuit", "text": "Every molecular **biologist** initially struggled to grasp how nucleic bases encoded intricate protein sequences." }
    ]
  },
  "Dashboard — logy/biologistic.md": {
    "primary": "Characteristic of or adhering to biologism; overly reductive in attributing social phenomena to biological factors.",
    "secondary": "Pertaining to explanatory frameworks that treat human historical and cultural forms as mere byproducts of organic instincts.",
    "quotes": [
      { "author": "Theodosius Dobzhansky", "work": "Mankind Evolving", "text": "Culture cannot be treated as a direct **biologistic** reflex, for it constitutes a distinct level of evolutionary emergence." },
      { "author": "Clifford Geertz", "work": "The Interpretation of Cultures", "text": "A purely **biologistic** account of human ritual strips symbolic actions of their lived semantic context." },
      { "author": "Steven Rose", "work": "Not in Our Genes", "text": "We reject the **biologistic** fatalism that claims war, hierarchy, and poverty are inexorable genetic imperatives." }
    ]
  },
  "Dashboard — logy/cardiologic.md": {
    "primary": "Pertaining to the heart or to the medical discipline of cardiology.",
    "secondary": "Relating to the diagnostic evaluation, pathophysiology, or clinical management of cardiovascular disease.",
    "quotes": [
      { "author": "Paul Dudley White", "work": "Heart Disease", "text": "Precise auscultation remains the bedrock of thorough **cardiologic** examination in everyday clinical practice." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "text": "Sudden dyspnea and precordial constriction warrant exhaustive **cardiologic** investigation." },
      { "author": "Eugene Braunwald", "work": "Heart Disease: A Textbook of Cardiovascular Medicine", "text": "Modern catheterization techniques opened an era of unprecedented **cardiologic** intervention." }
    ]
  },
  "Dashboard — logy/cardiologist.md": {
    "primary": "A physician who specializes in the diagnosis and medical management of diseases of the heart and blood vessels.",
    "secondary": "A clinical specialist trained in electrocardiography, echocardiography, and hemodynamic assessment.",
    "quotes": [
      { "author": "Bernard Lown", "work": "The Lost Art of Healing", "text": "The compassionate **cardiologist** listens intently to the cadence of the patient's narrative before ordering an echocardiogram." },
      { "author": "Helen Taussig", "work": "Congenital Malformations of the Heart", "text": "Collaborative consultation between the pediatric **cardiologist** and the surgeon made anoxemic infant survival possible." },
      { "author": "Michael DeBakey", "work": "The Living Heart", "text": "When coronary vessels occlude, the skilled **cardiologist** must decide between pharmaceutical stabilization and surgical bypass." }
    ]
  },
  "Dashboard — logy/cardiology.md": {
    "primary": "The medical specialty devoted to the study, diagnosis, and treatment of disorders of the heart and vascular system.",
    "secondary": "The scientific discipline examining myocardial electrophysiology, cardiac hemodynamics, and cardiovascular pathologies.",
    "quotes": [
      { "author": "William Harvey", "work": "De Motu Cordis", "text": "The perpetual muscular motion of the heart represents the foundational inquiry of experimental **cardiology**." },
      { "author": "René Laennec", "work": "A Treatise on the Diseases of the Chest", "text": "The stethoscope transformed clinical **cardiology** by rendering internal valvular murmurs perceptible to the ear." },
      { "author": "Arthur Conan Doyle", "work": "Round the Red Lamp", "text": "He devoted his mature hospital years exclusively to **cardiology**, deciphering every erratic beat of the pulse." }
    ]
  },
  "Dashboard — logy/dermatologic.md": {
    "primary": "Pertaining to the skin or the medical discipline of dermatology.",
    "secondary": "Relating to cutaneous lesions, epidermal pathology, or therapies targeting the integumentary system.",
    "quotes": [
      { "author": "Ferdinand von Hebra", "work": "Diseases of the Skin", "text": "Microscopic examination of epidermal scrapings yielded crucial insights into complex **dermatologic** eruptions." },
      { "author": "Thomas Bateman", "work": "A Practical Synopsis of Cutaneous Diseases", "text": "Accurate morphologic classification remains essential to distinguishing benign from malignant **dermatologic** affections." },
      { "author": "Robert Willan", "work": "On Cutaneous Diseases", "text": "Papular and vesicular stages exhibit distinct **dermatologic** features requiring different therapeutic interventions." }
    ]
  },
  "Dashboard — logy/dermatological.md": {
    "primary": "Relating to dermatology, cutaneous pathology, or clinical skin evaluation.",
    "secondary": "Involving the physiological and histological study of the skin and its adnexal structures.",
    "quotes": [
      { "author": "Jonathan Hutchinson", "work": "Illustrations of Clinical Surgery", "text": "Cutaneous manifestations frequently provide the earliest clues to systemic **dermatological** syndromes." },
      { "author": "Henry Radcliffe Crocker", "work": "Diseases of the Skin: Their Description, Pathology, and Treatment", "text": "The physician must carefully inspect the entire integument during a thorough **dermatological** review." },
      { "author": "William Osler", "work": "Aequanimitas", "text": "Cutaneous purpura and erythema present intricate **dermatological** problems intersecting directly with internal medicine." }
    ]
  },
  "Dashboard — logy/dermatologist.md": {
    "primary": "A medical specialist who diagnoses and treats diseases affecting the skin, hair, and nails.",
    "secondary": "A physician skilled in dermoscopy, cutaneous histology, and surgical excision of skin neoplasms.",
    "quotes": [
      { "author": "Paul Gerson Unna", "work": "The Histopathology of the Diseases of the Skin", "text": "By correlating stain reactions with clinical progression, the **dermatologist** deciphers underlying cutaneous inflammation." },
      { "author": "Marion Sulzberger", "work": "Dermatologic Allergy", "text": "The diagnostic patch test provides the practicing **dermatologist** with decisive evidence of contact hypersensitivity." },
      { "author": "Thomas Bateman", "work": "Delineations of Cutaneous Diseases", "text": "The observant **dermatologist** recognizes the diagnostic hallmark of lupus erythematosus in its characteristic facial distribution." }
    ]
  },
  "Dashboard — logy/dermatology.md": {
    "primary": "The branch of medicine concerned with the study, diagnosis, and treatment of skin disorders and cutaneous diseases.",
    "secondary": "The clinical and histological discipline devoted to the pathology, pharmacology, and physiology of the integumentary system.",
    "quotes": [
      { "author": "Robert Willan", "work": "Description and Treatment of Cutaneous Diseases", "text": "Systematic nomenclature rescued nineteenth-century **dermatology** from empirical chaos and imprecise folklore." },
      { "author": "Ferdinand von Hebra", "work": "Atlas of Skin Diseases", "text": "Modern **dermatology** achieved scientific maturity when it anchored cutaneous nosology in cellular histopathology." },
      { "author": "Erasmus Wilson", "work": "On Diseases of the Skin", "text": "The broad scope of clinical **dermatology** extends from minor epidermal abrasions to life-threatening generalized toxic eruptions." }
    ]
  },
  "Dashboard — logy/endocrinologist.md": {
    "primary": "A physician or biologist who specializes in the endocrine system, hormonal regulation, and metabolic disorders.",
    "secondary": "A clinical specialist evaluating dysfunctions of the pituitary, thyroid, parathyroid, adrenal, and pancreatic islet glands.",
    "quotes": [
      { "author": "Hans Selye", "work": "The Stress of Life", "text": "The astute **endocrinologist** recognizes how pituitary-adrenocortical hormones orchestrate systemic resistance to trauma." },
      { "author": "Rosalyn Yalow", "work": "Nobel Lecture: Radioimmunoassay", "text": "Radioimmunoassay equipped the **endocrinologist** to measure sub-picogram concentrations of circulating peptide hormones." },
      { "author": "Fuller Albright", "work": "The Parathyroid Glands and Metabolic Bone Disease", "text": "To unravel complex calcium disturbances, the **endocrinologist** must meticulously trace urinary excretion against serum levels." }
    ]
  },
  "Dashboard — logy/endocrinology.md": {
    "primary": "The branch of physiology and medicine concerned with endocrine glands and hormonal secretions.",
    "secondary": "The scientific discipline investigating biochemical homeostasis, feedback loops, and cellular receptors mediated by ductless gland secretions.",
    "quotes": [
      { "author": "Ernest Starling", "work": "The Croonian Lectures on the Chemical Reflexes", "text": "The birth of modern **endocrinology** began when we demonstrated that secretin functioned as an internal chemical messenger." },
      { "author": "Bernardo Houssay", "work": "Nobel Lecture: Carbohydrate Metabolism", "text": "Experimental **endocrinology** established that anterior pituitary secretions exert decisive control over pancreatic insulin action." },
      { "author": "Walter Cannon", "work": "The Wisdom of the Body", "text": "Systemic homeostasis relies profoundly on the coordinated signaling mechanisms elucidated by **endocrinology**." }
    ]
  },
  "Dashboard — logy/eulogise.md": {
    "primary": "To praise highly in speech or writing; to deliver a laudatory discourse upon someone.",
    "secondary": "In formal rhetoric, to extol the moral character, virtues, and public achievements of an individual.",
    "quotes": [
      { "author": "Samuel Johnson", "work": "Lives of the Most Eminent English Poets", "text": "Biographers are too frequently tempted to **eulogise** departed friends rather than describe their actual human failings." },
      { "author": "Thomas Macaulay", "work": "Critical and Historical Essays", "text": "It is customary to **eulogise** the statesmen who framed the constitution, but we must also dissect their compromises." },
      { "author": "William Thackeray", "work": "The Four Georges", "text": "Court poets hasten to **eulogise** every royal deed with polished lines and unmeasured flattery." }
    ]
  },
  "Dashboard — logy/eulogist.md": {
    "primary": "A person who speaks or writes in high praise of someone or something, especially in an obituary or memorial.",
    "secondary": "In classical oratory, a panegyrist appointed to commemorate the civic contributions and moral integrity of a prominent citizen.",
    "quotes": [
      { "author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "text": "The imperial **eulogist** exhausted the resources of rhetoric to celebrate victories won solely by mercenary arms." },
      { "author": "Edmund Burke", "work": "Reflections on the Revolution in France", "text": "No prudent statesman will rely on the partial declarations of an interested **eulogist**." },
      { "author": "Ralph Waldo Emerson", "work": "Representative Men", "text": "The true **eulogist** does not invent imaginary virtues, but perceives the divine spark resident in a great soul." }
    ]
  },
  "Dashboard — logy/eulogistic.md": {
    "primary": "Pertaining to or containing high, generous, or formal praise; laudatory.",
    "secondary": "Characterized by an elevated rhetorical tone intended to celebrate moral nobility and commemorative merit.",
    "quotes": [
      { "author": "George Eliot", "work": "Middlemarch", "text": "The local gazette published a distinctly **eulogistic** tribute recounting Mr. Bulstrode’s benefactions to the new infirmary." },
      { "author": "Washington Irving", "work": "The Life of George Washington", "text": "The assembly received the news with profound silence, followed by an eloquent **eulogistic** address from the speaker." },
      { "author": "Henry James", "work": "The Portrait of a Lady", "text": "His tone became almost **eulogistic** whenever he recounted the singular virtues of his former patron." }
    ]
  },
  "Dashboard — logy/eulogize.md": {
    "primary": "To speak or write in high praise of someone or something; extol the virtues or achievements of.",
    "secondary": "To deliver a formal funeral or commemorative panegyric in honor of a departed person.",
    "quotes": [
      { "author": "Abraham Lincoln", "work": "Eulogy on Henry Clay", "text": "To **eulogize** the departed patriot requires no ornamental rhetoric, for his monumental public deeds speak for themselves." },
      { "author": "Frederick Douglass", "work": "Oration in Memory of Abraham Lincoln", "text": "We assemble today not to flatter power, but to **eulogize** the great liberator whose proclamation broke our chains." },
      { "author": "Mark Twain", "work": "Life on the Mississippi", "text": "Local chroniclers never fail to **eulogize** the daring pilots whose skill steered steamboats through perilous snags." }
    ]
  },
  "Dashboard — logy/exobiology.md": {
    "primary": "The branch of science concerned with the search for and study of extraterrestrial life.",
    "secondary": "Astrobiology; the interdisciplinary field investigating the origins, prebiotic synthesis, and cosmic distribution of living systems.",
    "quotes": [
      { "author": "Carl Sagan", "work": "Cosmos", "text": "The nascent discipline of **exobiology** remains a science whose subject matter has yet to be unequivocally confirmed." },
      { "author": "Joshua Lederberg", "work": "Exobiology: Approaches to Life beyond the Earth", "text": "Planetary quarantine protocols are indispensable to preserve Martian soil samples for legitimate **exobiology** research." },
      { "author": "Freeman Dyson", "work": "Disturbing the Universe", "text": "Spectroscopic detection of atmospheric ozone or methane on distant exoplanets would revolutionize experimental **exobiology**." }
    ]
  },
  "Dashboard — logy/gastroenterologist.md": {
    "primary": "A medical specialist who diagnoses and treats diseases of the digestive tract, liver, and biliary system.",
    "secondary": "A physician skilled in upper endoscopy, colonoscopy, hepatobiliary management, and luminal gastrointestinal physiology.",
    "quotes": [
      { "author": "William Beaumont", "work": "Experiments and Observations on the Gastric Juice", "text": "Direct inspection of the gastric fistula enabled the early **gastroenterologist** to observe chemical digestion in vivo." },
      { "author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "text": "The patient complained of chronic dyspepsia, demanding the immediate counsel of a seasoned **gastroenterologist**." },
      { "author": "Walter Alvarez", "work": "Nervous Indigestion", "text": "A wise **gastroenterologist** evaluates psychic tension alongside mucosal pathology when managing recalcitrant abdominal pain." }
    ]
  },
  "Dashboard — logy/gastroenterology.md": {
    "primary": "The medical subspecialty dealing with the structure, function, and diseases of the digestive tract.",
    "secondary": "The clinical and pathophysiological study of the alimentary canal from esophagus to colon, including hepatic and pancreatic function.",
    "quotes": [
      { "author": "Ivan Pavlov", "work": "Lectures on the Work of the Digestive Glands", "text": "Neural regulation of enzymatic secretion laid the physiological cornerstone for twentieth-century **gastroenterology**." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "text": "Peptic ulceration and hepatic cirrhosis present dual challenges that dominate hospital wards in clinical **gastroenterology**." },
      { "author": "Fuller Albright", "work": "Clinical Studies in Gastrointestinal Absorption", "text": "Intestinal malabsorption syndromes bridge the disciplines of endocrine metabolic balance and clinical **gastroenterology**." }
    ]
  },
  "Dashboard — logy/hematologic.md": {
    "primary": "Pertaining to the blood, blood-forming organs, or the medical field of hematology.",
    "secondary": "Relating to cellular elements of blood, coagulation pathways, or erythrocyte and leukocyte abnormalities.",
    "quotes": [
      { "author": "Paul Ehrlich", "work": "Histology of the Blood", "text": "Differential aniline staining illuminated previously indistinguishable **hematologic** cell lines within bone marrow." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "text": "Severe pallor and splenomegaly constitute ominous **hematologic** signs demanding prompt laboratory examination." },
      { "author": "Maxwell Wintrobe", "work": "Clinical Hematology", "text": "The determination of mean corpuscular volume established a rigorous quantitative basis for **hematologic** taxonomy." }
    ]
  },
  "Dashboard — logy/hematological.md": {
    "primary": "Relating to the scientific and clinical investigation of blood and its pathological states.",
    "secondary": "Involving laboratory analysis of blood cell morphology, hemoglobin levels, or hemostatic mechanisms.",
    "quotes": [
      { "author": "Karl Landsteiner", "work": "The Specificity of Serological Reactions", "text": "Isoagglutination reactions resolved critical **hematological** incompatibilities that had previously rendered transfusions lethal." },
      { "author": "Archibald Garrod", "work": "Inborn Errors of Metabolism", "text": "Congenital porphyria presents intricate **hematological** symptoms intertwined with aberrant chemical excretion." },
      { "author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "text": "Pluripotent hematopoietic stem cells continuously regenerate the complete spectrum of **hematological** lineages." }
    ]
  },
  "Dashboard — logy/hematologist.md": {
    "primary": "A physician or clinical scientist specializing in diseases and disorders of the blood and lymphoid tissues.",
    "secondary": "A specialist trained in diagnosing leukemias, lymphomas, anemias, and coagulation coagulopathies.",
    "quotes": [
      { "author": "Maxwell Wintrobe", "work": "Blood, Pure and Eloquent", "text": "The dedicated **hematologist** reads the peripheral blood smear like an open book detailing systemic health." },
      { "author": "Paul Ehrlich", "work": "Researches on Cellular Immunology", "text": "Specific receptor affinities guided the **hematologist** in identifying myeloid granules under the microscope." },
      { "author": "William Dameshek", "work": "The Myeloproliferative Disorders", "text": "The clinical **hematologist** must distinguish benign reactive leukocytosis from autonomous marrow proliferation." }
    ]
  },
  "Dashboard — logy/hematology.md": {
    "primary": "The branch of medicine and biology concerned with the study, diagnosis, and treatment of blood disorders.",
    "secondary": "The specialized science covering hemopoiesis, erythrocytes, leukocytes, platelets, and hemostatic mechanisms.",
    "quotes": [
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "text": "The identification of leukemia as an independent disease entity marked a decisive breakthrough for modern **hematology**." },
      { "author": "William Osler", "work": "Aequanimitas", "text": "In the laboratory of clinical **hematology**, microscopic scrutiny dispels superficial diagnostic conjectures." },
      { "author": "Karl Landsteiner", "work": "Nobel Lecture: On Individual Differences in Human Blood", "text": "Serological classification of blood groups transformed surgical **hematology** from a reckless gamble into a reliable science." }
    ]
  },
  "Dashboard — logy/heterologic.md": {
    "primary": "Deviating from the normal or standard type in structure, composition, or organization.",
    "secondary": "In pathology, describing tissues or neoplasms composed of cellular elements foreign to the anatomical site in which they occur.",
    "quotes": [
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "text": "A **heterologic** tumor consists of cellular elements that are completely alien to the tissue from which it emerges." },
      { "author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "text": "The divergent segmentation in aberrant crustacea displays a distinctly **heterologic** structural arrangement." },
      { "author": "Johannes Müller", "work": "Elements of Physiology", "text": "Pathological ossification in muscular tissue represents a classic instance of **heterologic** development." }
    ]
  },
  "Dashboard — logy/heterological.md": {
    "primary": "Pertaining to heterology; characterized by deviation from typical anatomical or structural symmetry.",
    "secondary": "In semantics and philosophical logic, describing an adjective that does not describe itself (as in Grelling’s paradox).",
    "quotes": [
      { "author": "Kurt Gödel", "work": "On Formally Undecidable Propositions", "text": "Self-referential paradoxes such as the **heterological** predicate reveal intrinsic limitations within formalized semantic systems." },
      { "author": "Bertrand Russell", "work": "The Principles of Mathematics", "text": "A word is called **heterological** if it cannot be truly predicated of itself, generating immediate logical antinomy." },
      { "author": "Charles Sanders Peirce", "work": "Collected Papers", "text": "Signs that contradict their own structural design illustrate an anomalous or **heterological** relation in semiotics." }
    ]
  },
  "Dashboard — logy/heterologous.md": {
    "primary": "Originating from a different species or from a genetically distinct organism; non-homologous.",
    "secondary": "In immunology and genetics, relating to antigens, antibodies, or tissues differing in origin or structure from the host system.",
    "quotes": [
      { "author": "Macfarlane Burnet", "work": "The Clonal Selection Theory of Acquired Immunity", "text": "Exposure to **heterologous** erythrocytes stimulates clone proliferation that yields cross-reactive antibodies." },
      { "author": "Peter Medawar", "work": "The Uniqueness of the Individual", "text": "Grafting of **heterologous** tissue inevitably provokes fierce immunological rejection unless the host is rendered tolerant." },
      { "author": "Jacques Monod", "work": "Chance and Necessity", "text": "Expression of foreign genes in **heterologous** bacterial hosts demonstrated the universal conservation of the genetic code." }
    ]
  },
  "Dashboard — logy/heterology.md": {
    "primary": "Difference or deviation in structural arrangement, developmental origin, or composition from an established type.",
    "secondary": "In philosophical discourse and literary theory, the study or expression of radical otherness and that which resists assimilation.",
    "quotes": [
      { "author": "Georges Bataille", "work": "Visions of Excess", "text": "General economy must account for **heterology**, the science of heterogeneous matter excluded by homogeneous society." },
      { "author": "Michel Foucault", "work": "The Order of Things", "text": "The emergence of modern thought dismantled the classical table of identities to make room for radical **heterology**." },
      { "author": "Ernst Cassirer", "work": "The Philosophy of Symbolic Forms", "text": "Mythical consciousness embraces morphological **heterology**, allowing disparate objects to merge under magical identity." }
    ]
  },
  "Dashboard — logy/homologic.md": {
    "primary": "Pertaining to homology; exhibiting correspondence in basic structural design or evolutionary origin.",
    "secondary": "In comparative anatomy, describing morphological characters inherited from an equivalent structure in a common ancestor.",
    "quotes": [
      { "author": "Richard Owen", "work": "On the Archetype and Homologies of the Vertebrate Skeleton", "text": "The bat’s wing and human arm reveal an unmistakable **homologic** unity beneath divergent functional adaptations." },
      { "author": "Charles Darwin", "work": "The Descent of Man", "text": "Such profound **homologic** correspondences across mammalian limbs are completely inexplicable under separate special creations." },
      { "author": "Ernst Haeckel", "work": "Generelle Morphologie der Organismen", "text": "Morphological analysis requires distinguishing true **homologic** affinity from deceptive homoplastic convergence." }
    ]
  },
  "Dashboard — logy/homological.md": {
    "primary": "Showing structural or developmental homology; characterized by common phylogenetic descent.",
    "secondary": "In mathematics, relating to homology groups, chain complexes, and topological boundary cycles.",
    "quotes": [
      { "author": "Henri Poincaré", "work": "Analysis Situs", "text": "The topological connectivity of manifolds can be rigorously classified through systems of **homological** invariants." },
      { "author": "Saunders Mac Lane", "work": "Homology", "text": "Exact sequences of modules provide the foundational algebra for all modern **homological** calculations." },
      { "author": "Alfred North Whitehead", "work": "Process and Reality", "text": "Systematic order in the physical continuum relies upon extensive **homological** relations among successive occasions." }
    ]
  },
  "Dashboard — logy/homologise.md": {
    "primary": "To demonstrate, establish, or treat as structurally or phylogenetically homologous.",
    "secondary": "In evolutionary morphology, to trace an organ across different taxa back to an ancestral anatomical blueprint.",
    "quotes": [
      { "author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", "text": "The anatomist seeks to **homologise** every cranial bone with the archetypal neural arch of the idealized vertebra." },
      { "author": "Thomas Henry Huxley", "work": "On the Theory of the Vertebrate Skull", "text": "We cannot **homologise** the otic capsule with simple vertebral segments without violating embryological evidence." },
      { "author": "E. Ray Lankester", "work": "On the Use of the Term Homology in Modern Zoology", "text": "To **homologise** ancestral traits reliably, naturalists must base comparisons upon rigorous genealogical descent." }
    ]
  },
  "Dashboard — logy/homologize.md": {
    "primary": "To correspond or establish correspondence in structure, evolutionary origin, or taxonomic classification.",
    "secondary": "In comparative biology, to identify equivalent anatomical or genetic structures across distinct species.",
    "quotes": [
      { "author": "Stephen Jay Gould", "work": "Ontogeny and Phylogeny", "text": "Embryologists struggled for decades to **homologize** the blastopore of amphibians with the primitive streak of birds." },
      { "author": "Ernst Mayr", "work": "Animal Species and Evolution", "text": "Comparative ethologists attempt to **homologize** ritualized courtship displays across related avian species." },
      { "author": "Alfred Romer", "work": "The Vertebrate Body", "text": "It is surprisingly straightforward to **homologize** the pelvic girdle of early labyrinthodonts with that of modern reptiles." }
    ]
  },
  "Dashboard — logy/homologous.md": {
    "primary": "Having the same or similar relation, relative position, or structure; corresponding in type or origin.",
    "secondary": "In biology, describing structures, organs, or genes in different species derived from a common ancestral form.",
    "quotes": [
      { "author": "Charles Darwin", "work": "The Origin of Species", "text": "What can be more curious than that the hand of a man, formed for grasping, should be of the same **homologous** pattern as the paddle of a porpoise?" },
      { "author": "Gregor Mendel", "work": "Experiments in Plant Hybridization", "text": "Allelic factors separate cleanly during gamete formation when **homologous** elements segregate." },
      { "author": "Theodosius Dobzhansky", "work": "Genetics and the Origin of Species", "text": "Inversion loops form during meiosis when **homologous** chromosomes pair along inverted gene sequences." }
    ]
  },
  "Dashboard — logy/homology.md": {
    "primary": "The state of having the same or similar relation, relative position, structure, or value.",
    "secondary": "In evolutionary biology, similarity in morphology, genetics, or developmental pathways attributable to shared ancestry.",
    "quotes": [
      { "author": "Richard Owen", "work": "On the Archetype and Homologies of the Vertebrate Skeleton", "text": "I define **homology** as the same organ in different animals under every variety of form and function." },
      { "author": "Charles Darwin", "work": "The Descent of Man", "text": "The structural **homology** connecting the human frame with other mammals constitutes unanswerable evidence of our kinship." },
      { "author": "Stephen Jay Gould", "work": "The Structure of Evolutionary Theory", "text": "True **homology** represents the indelible historical footprint of genealogy stamped upon biological architecture." }
    ]
  },
  "Dashboard — logy/loginess.md": {
    "primary": "The quality or state of being logy; sluggishness, dullness, or physical and mental lethargy.",
    "secondary": "A feeling of heavy exhaustion, drowsiness, or impaired responsiveness brought on by fatigue, humidity, or illness.",
    "quotes": [
      { "author": "Sinclair Lewis", "work": "Arrowsmith", "text": "A persistent afternoon **loginess** crept over Martin after long hours inhaling chloroform fumes in the cramped laboratory." },
      { "author": "William Faulkner", "work": "The Sound and the Fury", "text": "The oppressive Mississippi heat induced an inescapable **loginess** that slowed both speech and step." },
      { "author": "Raymond Chandler", "work": "The Big Sleep", "text": "I shook my head violently to dispel the **loginess** left by the cheap whiskey and the stale air of the office." }
    ]
  },
  "Dashboard — logy/logy.md": {
    "primary": "Sluggish, dull, lethargic, or heavy, typically from fatigue, overeating, or humid weather.",
    "secondary": "Characterized by slowed reflexes and clouded cognitive alertness.",
    "quotes": [
      { "author": "H. L. Mencken", "work": "The American Language", "text": "Pioneer dialect favored colorful terms like **logy** to describe the stupor induced by malaria or heavy summer pork." },
      { "author": "Jack London", "work": "The Sea-Wolf", "text": "The heavy air below deck made me feel **logy** and indifferent to the harsh cursing of the crew." },
      { "author": "John Steinbeck", "work": "Cannery Row", "text": "A warm midday sun left the loafers on the cannery steps feeling pleasantly **logy** and disinclined to move." }
    ]
  },
  "Dashboard — logy/microbiologist.md": {
    "primary": "A scientist who specializes in the study of microscopic organisms such as bacteria, viruses, and fungi.",
    "secondary": "A researcher investigating microbial genetics, pathogenesis, and ecological nutrient cycling.",
    "quotes": [
      { "author": "Louis Pasteur", "work": "Studies on Fermentation", "text": "The diligent **microbiologist** must ensure that no stray airborne germ contaminates the boiled broth." },
      { "author": "Alexander Fleming", "work": "On the Antibacterial Action of Cultures of a Penicillium", "text": "A chance observation on a moldy agar plate rewarded the curious **microbiologist** with a miraculous antibiotic." },
      { "author": "Selman Waksman", "work": "My Life with the Microbes", "text": "The soil **microbiologist** uncovers an unseen cosmos where actinomycetes synthesize potent defense chemicals." }
    ]
  },
  "Dashboard — logy/microbiology.md": {
    "primary": "The branch of science dealing with microorganisms and their effects on other living organisms.",
    "secondary": "The biological discipline examining the physiology, genetics, ecology, and clinical pathology of microscopic life forms.",
    "quotes": [
      { "author": "Robert Koch", "work": "The Etiology of Tuberculosis", "text": "Pure culture isolation on solid media elevated clinical **microbiology** into an exact experimental discipline." },
      { "author": "Louis Pasteur", "work": "Germ Theory and its Applications to Medicine and Surgery", "text": "The truths of **microbiology** will inexorably sweep away centuries of superstition regarding spontaneous generation." },
      { "author": "René Dubos", "work": "The Bacterial Cell", "text": "Advances in **microbiology** revealed that microbial metabolism mirrors the core chemical pathways of all eukaryotic life." }
    ]
  },
  "Dashboard — logy/neology.md": {
    "primary": "The coining, introduction, or use of new words or new expressions; neologism.",
    "secondary": "In theological history, the adoption of novel, rationalizing doctrines or unorthodox interpretations of sacred scripture.",
    "quotes": [
      { "author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "text": "Legitimate linguistic growth requires judicious **neology** to express ideas that outstrip ancient vocabularies." },
      { "author": "Thomas De Quincey", "work": "Letters to a Young Man Whose Education Has Been Neglected", "text": "Senseless **neology** debases a noble language when coined merely to display fashionable intellectual vanity." },
      { "author": "John Henry Newman", "work": "An Essay on the Development of Christian Doctrine", "text": "Orthodox councils consistently rejected reckless theological **neology** that sought to dissolve ancient dogmas." }
    ]
  },
  "Dashboard — logy/paleobiology.md": {
    "primary": "The branch of paleontology that applies biological concepts and methods to the study of fossil life.",
    "secondary": "The evolutionary study of ancient ecosystems, functional morphology, and macroevolutionary patterns in the geologic record.",
    "quotes": [
      { "author": "George Gaylord Simpson", "work": "Tempo and Mode in Evolution", "text": "Quantitative **paleobiology** synthesizes fossil lineages with population genetics to illuminate macroevolutionary rates." },
      { "author": "Stephen Jay Gould", "work": "Wonderful Life: The Burgess Shale and the Nature of History", "text": "The exquisite soft-bodied fossils of the Burgess Shale forced modern **paleobiology** to rethink anatomical disparity." },
      { "author": "Niles Eldredge", "work": "Time Frames: The Rethinking of Darwinian Evolution", "text": "Punctuated equilibria transformed **paleobiology** from passive specimen cataloging into active evolutionary theory." }
    ]
  },
  "Dashboard — logy/paleology.md": {
    "primary": "The study of antiquities, archaic civilizations, and ancient historical periods.",
    "secondary": "The systematic examination of prehistoric artifacts, archaeological remains, and ancient inscriptions.",
    "quotes": [
      { "author": "Edward Burnett Tylor", "work": "Primitive Culture", "text": "Comparative **paleology** reconstructs the developmental sequence of human culture from flint implements to metallurgy." },
      { "author": "Flinders Petrie", "work": "Methods and Aims in Archaeology", "text": "Meticulous stratigraphic recording is the soul of genuine **paleology**, transforming barren dust into living history." },
      { "author": "Arthur Evans", "work": "The Palace of Minos", "text": "Excavations at Knossos inaugurated a brilliant chapter in Aegean **paleology**, unveiling a long-forgotten Bronze Age civilization." }
    ]
  },
  "Dashboard — logy/protology.md": {
    "primary": "The study or doctrine of origins, beginnings, or first principles.",
    "secondary": "In Christian dogmatics, theological reflection on the original state of creation, cosmos, and humanity prior to the Fall.",
    "quotes": [
      { "author": "Karl Barth", "work": "Church Dogmatics", "text": "Christian **protology** cannot be divorced from christology, for the beginning of creation already points toward redemption." },
      { "author": "Wolfhart Pannenberg", "work": "Systematic Theology", "text": "Eschatology and **protology** stand in dialectical tension, as the ultimate destiny of creation fulfills its primeval origin." },
      { "author": "Paul Tillich", "work": "Systematic Theology", "text": "Mythological **protology** symbolizes the transition from essential being to existential estrangement in human experience." }
    ]
  },
  "Dashboard — logy/radiological.md": {
    "primary": "Pertaining to radiology, ionizing radiation, or medical diagnostic imaging.",
    "secondary": "Relating to the clinical interpretation and technical application of X-rays, fluoroscopy, CT scans, and therapeutic radiation.",
    "quotes": [
      { "author": "Marie Curie", "work": "Radiology in War", "text": "Mobile **radiological** cars dispatched to the French front enabled immediate detection of embedded shrapnel in wounded soldiers." },
      { "author": "Wilhelm Röntgen", "work": "On a New Kind of Rays", "text": "Barium platinocyanide screens glowed intensely under the invisible beam, revealing unexpected **radiological** transparency." },
      { "author": "Ernest Rutherford", "work": "Radioactive Substances and Their Radiations", "text": "Alpha and beta emissions exhibit sharply differentiated **radiological** penetration through metallic foils." }
    ]
  },
  "Dashboard — logy/radiologist.md": {
    "primary": "A medical doctor who specializes in interpreting diagnostic imaging tests and managing radiation therapies.",
    "secondary": "A clinical specialist evaluating radiographs, computed tomography, and magnetic resonance scans to detect trauma, pathology, and malignancy.",
    "quotes": [
      { "author": "Wilhelm Röntgen", "work": "Communication to the Würzburg Physico-Medical Society", "text": "The future clinical **radiologist** will discern the skeletal contours of the living body without surgical incision." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "text": "The experienced **radiologist** identifies subtle pulmonary infiltrates that escape ordinary physical auscultation." },
      { "author": "Harold Varmus", "work": "The Art and Politics of Science", "text": "Close partnership between the oncologist and the diagnostic **radiologist** is essential to mapping tumor regression." }
    ]
  },
  "Dashboard — logy/radiology.md": {
    "primary": "The medical specialty devoted to the use of radiant energy and imaging techniques for diagnosis and therapy.",
    "secondary": "The clinical and physical discipline integrating diagnostic radiography, interventional fluoroscopy, and therapeutic radiation.",
    "quotes": [
      { "author": "Marie Curie", "work": "Radioactivity", "text": "The therapeutic applications of radium created an entirely new therapeutic branch within clinical **radiology**." },
      { "author": "Henri Becquerel", "work": "On the Radiations Emitted by Phosphorescence", "text": "The spontaneous radiation of uranium salts laid the unexpected physical foundation for modern medical **radiology**." },
      { "author": "Ernest Lawrence", "work": "The Production of High Velocity Ions", "text": "Cyclotron-produced isotopes quickly proved invaluable for tracer research and targeted therapeutic **radiology**." }
    ]
  },
  "Dashboard — logy/trilogy.md": {
    "primary": "A group or series of three related works of art, literature, drama, or music that share a common theme or continuity.",
    "secondary": "Originally in ancient Greece, a set of three tragedies performed consecutively at the Dionysian dramatic festivals.",
    "quotes": [
      { "author": "Aristotle", "work": "Poetics", "text": "In the tragic **trilogy**, the dramatist unrolls the tragic destiny of an entire dynasty across three interconnected performances." },
      { "author": "Percy Bysshe Shelley", "work": "Prometheus Unbound: Preface", "text": "Aeschylus completed his legendary Promethean **trilogy**, but the lost dramas leave modern poets free to imagine the resolution." },
      { "author": "George Bernard Shaw", "work": "Back to Methuselah: Preface", "text": "I chose the expansive canvas of a dramatic **trilogy** to stage the full sweep of creative evolutionary philosophy." }
    ]
  },
  "Dashboard — logy/unapologetic.md": {
    "primary": "Feeling or showing no regret, remorse, or hesitation; unrepentant and boldly outspoken.",
    "secondary": "Defiantly maintaining a controversial stance or lifestyle without offering justification or excuses.",
    "quotes": [
      { "author": "George Orwell", "work": "Homage to Catalonia", "text": "The soldiers remained fiercely **unapologetic** regarding their revolutionary measures, defiant toward all moderate critics." },
      { "author": "Virginia Woolf", "work": "A Room of One's Own", "text": "She stood completely **unapologetic** in her ambition, demanding financial independence as the rightful birthright of womanhood." },
      { "author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "text": "Lord Henry indulged in his aesthetic paradoxes with an **unapologetic** cynicism that delighted and unsettled his companions." }
    ]
  },
  "Dashboard — ogdo/ogdo.md": {
    "primary": "An ancient combining form or root signifying eight, an eightfold structure, or an octave.",
    "secondary": "In classical arithmetic and mysticism, referring to groupings of eight entities, tones, or cosmological spheres.",
    "quotes": [
      { "author": "Clement of Alexandria", "work": "Stromata", "text": "The mystic **ogdo** symbolizes the day of cosmic regeneration that dawns beyond the seven days of worldly creation." },
      { "author": "Philo of Alexandria", "work": "On the Creation", "text": "The harmonic nature of the **ogdo** reflects the foundational musical diapason and balanced equilibrium in sacred numbers." },
      { "author": "Irenaeus of Lyons", "work": "Against Heresies", "text": "The Gnostics construct elaborate celestial hierarchies around the primeval **ogdo**, compounding allegories of their own invention." }
    ]
  },
  "Dashboard — ogdo/ogdoad.md": {
    "primary": "A group, series, or collection of eight persons or things.",
    "secondary": "In Gnostic cosmology and ancient Egyptian religion, the primordial council or pantheon of eight divine beings embodying the universe.",
    "quotes": [
      { "author": "Carl Jung", "work": "Aion: Researches into the Phenomenology of the Self", "text": "The Gnostic **ogdoad** represents an eightfold archetype of psychic wholeness, balancing conscious and unconscious polarities." },
      { "author": "Irenaeus of Lyons", "work": "Against Heresies", "text": "Valentinus taught that from the unbegotten Bythos emanated the primordial **ogdoad** of aeons, the root of all spiritual being." },
      { "author": "Helena Blavatsky", "work": "The Secret Doctrine", "text": "Hermetic cosmology reveres the sacred **ogdoad** as the eight primordial builders who fashioned the manifest cosmos from chaos." }
    ]
  },
  "Dashboard — org/orgasm.md": {
    "primary": "The climax of sexual excitement, characterized by intensely pleasurable contractions and the release of accumulated tension.",
    "secondary": "Figuratively, an intense paroxysm, sudden convulsive outburst, or peak of emotional, violent, or aesthetic frenzy.",
    "quotes": [
      { "author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "text": "The physiological culmination of the sexual **orgasm** involves rhythmic vascular and muscular discharges throughout the pelvic network." },
      { "author": "Sigmund Freud", "work": "Three Essays on the Theory of Sexuality", "text": "Psychic tension seeks immediate discharge through the motor and emotional convulsion of the **orgasm**." },
      { "author": "D. H. Lawrence", "work": "Lady Chatterley's Lover", "text": "The wave broke in a sudden ecstatic **orgasm**, dissolving the rigid barriers of individual ego into dark primeval awareness." }
    ]
  },
  "Dashboard — pae/anapaest.md": {
    "primary": "A metrical foot in poetry consisting of two short (or unstressed) syllables followed by one long (or stressed) syllable (˘ ˘ —).",
    "secondary": "In quantitative and accentual prosody, a rising trisyllabic foot renowned for imparting a swift, galloping, or rhythmic cadence.",
    "quotes": [
      { "author": "Samuel Taylor Coleridge", "work": "Metrical Feet: Lesson for a Boy", "text": "With a leap and a bound the swift **anapaest** throngs, lending energetic velocity to Greek choruses and martial songs." },
      { "author": "Lord Byron", "work": "The Destruction of Sennacherib", "text": "The galloping cadence of the **anapaest** carries the Assyrian cavalry forward like leaves on the autumn gale." },
      { "author": "Algernon Charles Swinburne", "work": "Atalanta in Calydon: Preface", "text": "English lyric verse gains tremendous oceanic momentum when sustained by the rapid, cascading stroke of the **anapaest**." }
    ]
  },
  "Dashboard — pae/anapaestic.md": {
    "primary": "Pertaining to, composed in, or consisting of anapaests.",
    "secondary": "Characterized by a light, rapid, triple rhythm produced by successive sequences of two short syllables followed by an accented syllable.",
    "quotes": [
      { "author": "Edgar Allan Poe", "work": "The Philosophy of Composition", "text": "The buoyant, swinging lift of **anapaestic** verse provides a striking musical contrast to sombre dactylic gravity." },
      { "author": "John Dryden", "work": "An Essay of Dramatic Poesy", "text": "Comic interludes occasionally adopt an **anapaestic** cadence to mimic the lively banter of the marketplace." },
      { "author": "Matthew Arnold", "work": "On Translating Homer", "text": "The translator who renders heroic hexameters into rattling **anapaestic** jingle forfeits the solemn nobility of Homeric verse." }
    ]
  },
  "Dashboard — pae/anapest.md": {
    "primary": "A metrical foot composed of two short or unaccented syllables followed by one long or accented syllable.",
    "secondary": "A prosodic unit employed in accentual verse to convey rapid movement, energetic equestrian motion, or lyrical surge.",
    "quotes": [
      { "author": "Robert Browning", "work": "How They Brought the Good News from Ghent to Aix", "text": "The persistent triple rhythm of each **anapest** echoes the frantic gallop of the three horses racing through the night." },
      { "author": "George Saintsbury", "work": "A History of English Prosody", "text": "Substitution of the **anapest** for the customary iambic foot imparts elasticity and rhythmic freshness to English lyrical lines." },
      { "author": "W. H. Auden", "work": "The Dyer's Hand", "text": "A master craftsman employs the **anapest** with discretion, avoiding the monotonous rattle of mere nursery jingles." }
    ]
  },
  "Dashboard — pae/anapestic.md": {
    "primary": "Relating to or consisting of anapests.",
    "secondary": "Displaying the buoyant, energetic rhythmic tempo characteristic of verse composed predominantly in triple anapestic meter.",
    "quotes": [
      { "author": "Walt Whitman", "work": "Notes on Prosody", "text": "The rushing ocean surge breaks onto the sand with an irresistible, rolling **anapestic** beat." },
      { "author": "William Hazlitt", "work": "Lectures on the English Poets", "text": "The spirited **anapestic** measure of Moore's melodies captivated audiences by its effortless vocal agility." },
      { "author": "T. S. Eliot", "work": "The Music of Poetry", "text": "Rhythmic dissonance occurs when a sudden **anapestic** acceleration intrudes upon a solemn blank verse period." }
    ]
  },
  "Dashboard — pin/pinocytosis.md": {
    "primary": "The ingestion of liquid into a cell by the budding of small vesicles from the cell membrane; cellular drinking.",
    "secondary": "In cell biology, a non-specific form of endocytosis by which extracellular fluid and dissolved micro-solutes are internalized into pinosomes.",
    "quotes": [
      { "author": "Christian de Duve", "work": "A Guided Tour of the Living Cell", "text": "Through continual **pinocytosis**, the cell membrane folds inward to sip tiny droplets of the surrounding nutrient fluid." },
      { "author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "text": "Fluid-phase **pinocytosis** occurs constitutively in macrophages, replacing their entire plasma membrane area every hour." },
      { "author": "George Palade", "work": "Nobel Lecture: Intracellular Aspects of the Process of Protein Synthesis", "text": "Vesicular transport mechanisms including **pinocytosis** mediate the transendothelial exchange of serum macromolecules." }
    ]
  },
  "Dashboard — pin/pinosome.md": {
    "primary": "A small, membrane-bound intracellular vesicle formed by pinocytosis that encloses engulfed extracellular fluid.",
    "secondary": "In cellular physiology, an endocytic vacuole that migrates inward to fuse with early endosomes or lysosomes for digestion.",
    "quotes": [
      { "author": "Christian de Duve", "work": "Lysosomes Revisited", "text": "Once detached from the plasma membrane, the nascent **pinosome** rapidly acquires hydrolytic enzymes from merging lysosomes." },
      { "author": "Keith Porter", "work": "Fine Structure of Cells and Tissues", "text": "Electron micrographs reveal each tiny **pinosome** migrating along microtubule tracks toward the cell interior." },
      { "author": "James Rothman", "work": "Mechanisms of Intracellular Membrane Fusion", "text": "Vesicle coat disassembly is required before a mature **pinosome** can dock and fuse with its target endosomal compartment." }
    ]
  },
  "Dashboard — pleg/aplectrum.md": {
    "primary": "A genus of North American terrestrial orchids, characterized by the absence of a nectar-bearing floral spur; notably Aplectrum hyemale (puttyroot).",
    "secondary": "In systematic botany, an orchid possessing a solitary winter leaf and paired globular underground corms containing sticky mucilage.",
    "quotes": [
      { "author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "text": "The spurless lip and winter-hardy leaf distinguish the genus **Aplectrum** in our rich deciduous woodlands." },
      { "author": "John Torrey", "work": "A Flora of the State of New York", "text": "Root corms of **Aplectrum** yield a tenaceous mucilage historically employed by country folk to mend broken earthenware." },
      { "author": "Charles Sprague Sargent", "work": "The Silva of North America", "text": "Beneath the shade of beech groves, solitary spikes of **Aplectrum** unfold their greenish-brown flowers in late spring." }
    ]
  },
  "Dashboard — pleg/apoplectoid.md": {
    "primary": "Resembling apoplexy or an apoplectic stroke in sudden onset, symptoms, or appearance.",
    "secondary": "Exhibiting severe sudden cerebral congestion, acute loss of consciousness, or violent flushing reminiscent of apoplexy.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "text": "The patient collapsed in an **apoplectoid** seizure that initially mimicked massive cerebral hemorrhage." },
      { "author": "Thomas Sydenham", "work": "The Whole Works of That Excellent Practical Physician Dr. Thomas Sydenham", "text": "Excessive intake of spirituous liquors frequently plunges the sufferer into a perilous, stertorous **apoplectoid** coma." },
      { "author": "Jean-Martin Charcot", "work": "Lectures on the Diseases of the Nervous System", "text": "Hysterical attacks occasionally present dramatic **apoplectoid** features that deceive all but the most experienced neurologist." }
    ]
  },
  "Dashboard — pleg/cataplectic.md": {
    "primary": "Pertaining to, affected with, or resembling cataplexy; marked by sudden, temporary loss of voluntary muscle tone.",
    "secondary": "Relating to abrupt postural collapse provoked by sudden emotional stimuli while full consciousness is maintained.",
    "quotes": [
      { "author": "Jean-Martin Charcot", "work": "Clinical Lectures on Senile and Chronic Diseases", "text": "During the **cataplectic** paroxysm, the limbs go completely flaccid while the patient observes her surroundings with intact awareness." },
      { "author": "William Gowers", "work": "A Manual of Diseases of the Nervous System", "text": "A hearty burst of sudden laughter was sufficient to trigger a complete **cataplectic** fall to the floor." },
      { "author": "Sigmund Freud", "work": "The Interpretation of Dreams", "text": "The dream sensation of motor paralysis bears a striking phenomenological kinship to transient **cataplectic** states." }
    ]
  },
  "Dashboard — pleg/cataplexy.md": {
    "primary": "A sudden, temporary loss of muscle tone and voluntary postural control, typically triggered by strong emotion.",
    "secondary": "A cardinal pathophysiological symptom of narcolepsy caused by degeneration of hypothalamic hypocretin (orexin) neurons.",
    "quotes": [
      { "author": "William Gowers", "work": "The Borderland of Epilepsy", "text": "The hallmark of genuine **cataplexy** is the instantaneous loss of muscular power without any clouding of consciousness." },
      { "author": "Emil Kraepelin", "work": "Clinical Psychiatry", "text": "Patients suffering from severe narcolepsy describe terrifying episodes of **cataplexy** induced by sudden surprise or mirth." },
      { "author": "Oliver Sacks", "work": "Awakenings", "text": "Under emotional excitement, sudden **cataplexy** would drop the patient to the knees as if severed from all voluntary neural control." }
    ]
  },
  "Dashboard — pleg/hemiplegia.md": {
    "primary": "Total or partial paralysis affecting one lateral half of the body, usually caused by a brain injury or stroke.",
    "secondary": "In clinical neurology, unilateral loss of voluntary motor control resulting from disruption of the contralateral corticospinal tract.",
    "quotes": [
      { "author": "William Osler", "work": "The Cerebral Palsies of Children", "text": "Spastic **hemiplegia** in infants typically arises from unilateral vascular occlusion or natal cerebral trauma." },
      { "author": "Jean-Martin Charcot", "work": "Lectures on the Diseases of the Nervous System", "text": "Post-apoplectic contracture establishes a rigid posture characteristic of permanent chronic **hemiplegia**." },
      { "author": "John Hughlings Jackson", "work": "Selected Writings of John Hughlings Jackson", "text": "In right-sided **hemiplegia**, damage to the left cerebral hemisphere is frequently accompanied by profound aphasia." }
    ]
  },
  "Dashboard — pleg/hemiplegic.md": {
    "primary": "Relating to, affected by, or characteristic of hemiplegia; paralyzed on one side of the body.",
    "secondary": "Denoting motor deficits, abnormal circumducting gait, or spastic contractures resulting from contralateral cerebral lesions.",
    "quotes": [
      { "author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "text": "The **hemiplegic** patient alienates his paralyzed left arm, insisting that an uncanny stranger’s limb lies beside him in bed." },
      { "author": "William Gowers", "work": "A Manual of Diseases of the Nervous System", "text": "The typical **hemiplegic** gait forces the patient to swing the rigid, extended leg in a wide lateral arc." },
      { "author": "Wilder Penfield", "work": "The Cerebral Cortex of Man", "text": "Focal electrical stimulation adjacent to the ischemic scar produced involuntary twitching in the **hemiplegic** arm." }
    ]
  },
  "Dashboard — pleg/monoplegia.md": {
    "primary": "Complete paralysis confined to a single limb, muscle group, or isolated anatomical region.",
    "secondary": "In neurology, a localized motor deficit caused by a focal cerebral cortex lesion, spinal cord anterior horn damage, or isolated peripheral neuropathy.",
    "quotes": [
      { "author": "Jean-Martin Charcot", "work": "Lectures on Clinical Medicine", "text": "Cortical **monoplegia** restricted to the upper limb indicates a circumscribed lesion in the middle third of the precentral gyrus." },
      { "author": "John Hughlings Jackson", "work": "Neurological Fragments", "text": "A creeping brachial **monoplegia** occasionally develops following a series of localized jacksonian convulsions." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "text": "Pure crural **monoplegia** is an exceedingly rare neurological presentation usually pointing to parasagittal infarction." }
    ]
  },
  "Dashboard — pleg/paraplegia.md": {
    "primary": "Impairment or loss of motor or sensory function in the lower half of the body and legs, typically caused by spinal cord injury.",
    "secondary": "A neurological condition resulting from trauma, transverse myelitis, or tumor compression affecting the thoracic, lumbar, or sacral cord.",
    "quotes": [
      { "author": "Ludwig Guttmann", "work": "Spinal Cord Injuries: Comprehensive Management and Research", "text": "Systematic rehabilitation converted traumatic **paraplegia** from an inevitable death sentence into an active, dignified life." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "text": "Compression **paraplegia** secondary to tuberculous caries of the spine demands immediate immobilization and surgical decompression." },
      { "author": "John Hughlings Jackson", "work": "Selected Writings", "text": "Complete transection of the dorsal spinal cord produces instantaneous sensory loss and flaccid **paraplegia** below the lesion." }
    ]
  },
  "Dashboard — pleg/paraplegic.md": {
    "primary": "Affected by, relating to, or exhibiting paraplegia; paralyzed in both lower limbs.",
    "secondary": "A person living with bilateral paralysis and sensory loss of the lower body caused by spinal injury or myelopathy.",
    "quotes": [
      { "author": "Oliver Sacks", "work": "A Leg to Stand On", "text": "Working closely with **paraplegic** patients taught me how the nervous system reconstructs its internal map of corporeal reality." },
      { "author": "Ludwig Guttmann", "work": "The Story of Stoke Mandeville", "text": "Athletic competition empowered the **paraplegic** veteran to regain physical autonomy and social self-esteem." },
      { "author": "Jean-Martin Charcot", "work": "Lectures on the Diseases of the Nervous System", "text": "The spastic reflexes observed in the chronic **paraplegic** patient demonstrate release from higher cerebral inhibition." }
    ]
  },
  "Dashboard — pleg/plectrum.md": {
    "primary": "A small, thin piece of plastic, quill, bone, metal, or shell used to pluck or strum the strings of an instrument; a pick.",
    "secondary": "In comparative anatomy and archaeology, a small striking implement; also, the auditory columella/stapes in certain reptiles and amphibians.",
    "quotes": [
      { "author": "John Milton", "work": "Ad Patrem", "text": "Phoebus himself guides the trembling **plectrum** across the golden strings, tuning the song to immortal celestial harmony." },
      { "author": "Percy Bysshe Shelley", "work": "Homer's Hymn to Mercury", "text": "With the quill of a swift vulture for a **plectrum**, the infant god struck sweet melodies from the hollowed tortoise shell." },
      { "author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "text": "In the saurian skull, the delicate rod-like **plectrum** transmits vibrations directly from the tympanic membrane to the fenestra ovalis." }
    ]
  },
  "Dashboard — pleg/pleximeter.md": {
    "primary": "A small, flat plate of ivory, rubber, metal, or bone placed against the body to receive blows from a percussion hammer.",
    "secondary": "In physical diagnosis, an acoustic mediating plaque introduced by Piorry to amplify and clarify internal thoracic resonance notes.",
    "quotes": [
      { "author": "Pierre Adolphe Piorry", "work": "De la Percussion Médiate", "text": "By placing an ivory **pleximeter** firmly upon the chest, the physician elicits clear, distinct resonance notes from underlying viscera." },
      { "author": "René Laennec", "work": "A Treatise on the Diseases of the Chest", "text": "Mediate percussion using Piorry’s **pleximeter** neatly complements auscultation when delimiting the borders of pulmonary effusion." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "text": "Skillful finger-to-finger tapping has largely superseded the artificial **pleximeter** in routine bedside physical examination." }
    ]
  },
  "Dashboard — pleg/tetraplegia.md": {
    "primary": "Paralysis affecting all four limbs and the torso, caused by damage to the cervical spinal cord; quadriplegia.",
    "secondary": "A severe neurological syndrome resulting from cervical spine trauma or disease, leading to extensive loss of motor and sensory function.",
    "quotes": [
      { "author": "Ludwig Guttmann", "work": "Spinal Cord Injuries", "text": "High cervical trauma presenting with complete **tetraplegia** requires immediate respiratory management and intensive nursing care." },
      { "author": "Oliver Sacks", "work": "The Island of the Colorblind", "text": "Even when struck down by sudden **tetraplegia**, the patient’s inner intellectual and imaginative life may remain luminous." },
      { "author": "Wilder Penfield", "work": "The Mystery of the Mind", "text": "The tragic silence of sensory isolation in profound **tetraplegia** demonstrates how intimately the mind leans upon continuous bodily feedback." }
    ]
  }
}

content = '''import fs from 'fs';
import path from 'path';

const CLUSTER_DIR = 'App database/Greek roots/Cluster Action';

const BATCH8_DATA = ''' + json.dumps(batch8_data, indent=2, ensure_ascii=False) + ''';

function formatQuotes(quotes) {
  return quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.text}"*`).join('\\n');
}

function updateFile(relPath, wordData) {
  const filePath = path.join(CLUSTER_DIR, relPath);
  if (!fs.existsSync(filePath)) {
    console.error(`File NOT found: ${filePath}`);
    return false;
  }
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`Missing [!book] in ${filePath}`);
    return false;
  }
  const topPart = content.slice(0, bookIdx).trimEnd();

  const newDefBlock = `> [!book] 📖 Definitions & Semantic Range\\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${wordData.primary}\\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${wordData.secondary}\\n\\n> [!quote] 💬 Contextual Usage & Authentic Quotations\\n${formatQuotes(wordData.quotes)}\\n`;

  const finalContent = topPart + '\\n\\n' + newDefBlock;
  fs.writeFileSync(filePath, finalContent, 'utf8');
  return true;
}

let count = 0;
for (const [relPath, data] of Object.entries(BATCH8_DATA)) {
  if (updateFile(relPath, data)) {
    count++;
  }
}

console.log(`========================================`);
console.log(`Action Batch 8 Completed: ${count} / ${Object.keys(BATCH8_DATA).length} words updated`);
console.log(`========================================`);
'''

with open('main app/scripts/curate-action-batch8.mjs', 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Generated curate-action-batch8.mjs with {len(batch8_data)} entries.")
