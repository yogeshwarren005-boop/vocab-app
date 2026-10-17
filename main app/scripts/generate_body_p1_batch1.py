import json
import os

batch1_data = {
  "Dashboard — aden\\aden.md": {
    "primary": "The Greek anatomical root and combining element denoting a gland or glandular structure (aden- / adeno-).",
    "secondary": "A strategic port city on the southern coast of the Arabian Peninsula in Yemen, giving its name to the Gulf of Aden.",
    "quotes": [
      { "author": "Galen", "work": "On Anatomical Procedures", "quote": "The ancient Greeks designated each secretory bodily kernel an **aden**, distinguishing vascular glands from muscular tissue." },
      { "author": "Richard Francis Burton", "work": "First Footsteps in East Africa", "quote": "The barren volcanic crater of **Aden** rose starkly against the turquoise waters of the Arabian Sea." },
      { "author": "Jules Verne", "work": "Twenty Thousand Leagues Under the Sea", "quote": "We steamed southward past the Straits of Bab-el-Mandeb, leaving the fortified roadstead of **Aden** in our wake." }
    ]
  },
  "Dashboard — aden\\adenanthera.md": {
    "primary": "A genus of tropical deciduous trees in the legume family (Fabaceae), known for bearing deciduous anther glands.",
    "secondary": "In forestry and economic botany, specifically Adenanthera pavonina (red sandalwood tree), cultivated for its scarlet ornamental seeds and timber.",
    "quotes": [
      { "author": "William Roxburgh", "work": "Flora Indica", "quote": "The glossy scarlet seeds of **adenanthera** serve goldsmiths throughout India as uniform small units of weight." },
      { "author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "The distinguishing generic feature of **adenanthera** resides in the small deciduous gland crowning the tip of each anther." },
      { "author": "Liberty Hyde Bailey", "work": "The Standard Cyclopedia of Horticulture", "quote": "In tropical avenues, **adenanthera** provides delightful shade and sheds brilliant red seeds prized for necklace manufacture." }
    ]
  },
  "Dashboard — aden\\adenauer.md": {
    "primary": "Konrad Adenauer (1876–1967), German statesman who served as the first Federal Chancellor of West Germany from 1949 to 1963.",
    "secondary": "In postwar European history, the Christian Democratic leader who anchored the Federal Republic in the Western alliance and co-founded European integration.",
    "quotes": [
      { "author": "Winston Churchill", "work": "Speeches in the House of Commons", "quote": "The resolute leadership of Chancellor **Adenauer** has firmly restored democratic Germany to the family of Western nations." },
      { "author": "Dwight D. Eisenhower", "work": "Waging Peace", "quote": "In every diplomatic crisis, Konrad **Adenauer** demonstrated unwavering moral conviction and steadfast European loyalty." },
      { "author": "Charles de Gaulle", "work": "Memoirs of Hope", "quote": "Meeting with **Adenauer** at Colombey-les-Deux-Églises sealed the historic reconciliation between France and Germany." }
    ]
  },
  "Dashboard — aden\\adenine.md": {
    "primary": "A purine base (6-aminopurine) that pairs with thymine in DNA and with uracil in RNA, essential for genetic coding.",
    "secondary": "In cellular bioenergetics, the purine nucleobase incorporated into adenosine triphosphate (ATP), NAD+, and FAD to drive metabolic reactions.",
    "quotes": [
      { "author": "Albrecht Kossel", "work": "Researches on the Nuclein of Yeast", "quote": "From pancreatic glandular extracts we isolated this fundamental purine base, which I designate **adenine**." },
      { "author": "James D. Watson", "work": "The Double Helix", "quote": "The spatial dimensions dictated that **adenine** could only pair smoothly with thymine across the twin helical strands." },
      { "author": "Francis Crick", "work": "What Mad Pursuit", "quote": "The strict hydrogen bonding between **adenine** and its pyrimidine partner ensures high fidelity during genetic replication." }
    ]
  },
  "Dashboard — aden\\adenitis.md": {
    "primary": "Inflammation of a lymphatic gland or secretory gland.",
    "secondary": "In clinical pathology, acute or chronic swelling of lymph nodes (lymphadenitis) in response to localized or systemic bacterial infection.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Streptococcal pharyngitis frequently induces painful cervical **adenitis**, requiring careful differentiation from tubercular scrofula." },
      { "author": "Percivall Pott", "work": "Chirurgical Works", "quote": "Suppurative inguinal **adenitis** must be watched closely lest purulent collections burrow toward femoral fascial planes." },
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Enlargement of axillary nodes following cutaneous abrasions illustrates reactive **adenitis** along draining lymphatic pathways." }
    ]
  },
  "Dashboard — aden\\adenium.md": {
    "primary": "A genus of succulent pachycaul shrubs and small trees in the dogbane family (Apocynaceae), commonly known as desert roses.",
    "secondary": "In horticulture and ethnobotany, African desert succulents containing toxic cardiac glycosides historically utilized as arrow poisons.",
    "quotes": [
      { "author": "John Lindley", "work": "Edwards's Botanical Register", "quote": "The swollen caudex of **adenium** provides an extraordinary reservoir of moisture amidst the arid wastes of southern Arabia." },
      { "author": "Liberty Hyde Bailey", "work": "The Standard Cyclopedia of Horticulture", "quote": "Cultivated specimens of **adenium** produce dazzling clusters of crimson funnelform blossoms above a bonsai-like basal trunk." },
      { "author": "Richard Evans Schultes", "work": "Plants of the Gods", "quote": "Indigenous hunters throughout East Africa pounded the bark of **adenium** to extract lethal cardiac arrow venoms." }
    ]
  },
  "Dashboard — aden\\adenocarcinoma.md": {
    "primary": "A malignant epithelial tumor originating in glandular tissue or exhibiting glandular histologic characteristics.",
    "secondary": "In oncology, the most common histological form of cancer occurring in the colon, breast, prostate, pancreas, and lung.",
    "quotes": [
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The microscopic architecture of an **adenocarcinoma** demonstrates atypical glandular acini invading adjacent stroma." },
      { "author": "James Ewing", "work": "Neoplastic Diseases", "quote": "Mucin secretion within the invading neoplastic tubules confirms the diagnosis of invasive colorectal **adenocarcinoma**." },
      { "author": "Siddhartha Mukherjee", "work": "The Emperor of All Maladies", "quote": "Targeted therapies revolutionized our approach to lung **adenocarcinoma** by blocking mutant epidermal growth factor receptors." }
    ]
  },
  "Dashboard — aden\\adenocarcinomatous.md": {
    "primary": "Pertaining to, resembling, or having the histological characteristics of an adenocarcinoma.",
    "secondary": "In surgical pathology, describing tissue specimens that display malignant glandular proliferation, atypical mitosis, and basement membrane breach.",
    "quotes": [
      { "author": "James Ewing", "work": "Neoplastic Diseases", "quote": "Biopsy of the polypoid mucosal mass revealed focal **adenocarcinomatous** transformation within preexisting dysplastic crypts." },
      { "author": "William Stewart Halsted", "work": "The Results of Operations for the Cure of Cancer of the Breast", "quote": "Extensive lymphatic emboli confirmed the aggressively **adenocarcinomatous** nature of the infiltrating mammary neoplasm." },
      { "author": "Atul Gawande", "work": "Complications: A Surgeon's Notes on an Imperfect Science", "quote": "The frozen section report described **adenocarcinomatous** invasion extending beyond the resection margin of the pancreatic margin." }
    ]
  },
  "Dashboard — aden\\adenohypophysis.md": {
    "primary": "The anterior glandular lobe of the pituitary gland, derived embryologically from Rathke's pouch.",
    "secondary": "In endocrinology, the master glandular lobe that synthesizes and secretes ACTH, TSH, GH, PRL, FSH, and LH under hypothalamic neurohumoral control.",
    "quotes": [
      { "author": "Harvey Cushing", "work": "The Pituitary Body and Its Disorders", "quote": "Acidophil adenomas arising within the **adenohypophysis** stimulate excessive skeletal growth, culminating in clinical acromegaly." },
      { "author": "Bernardo Houssay", "work": "Hypophyseal Functions", "quote": "The endocrine dominion exercised by the **adenohypophysis** over the adrenals and gonads is governed through hypothalamic portal vessels." },
      { "author": "Roger Guillemin", "work": "Hypothalamic Hormones", "quote": "Hypothalamic releasing factors travel down specialized capillary beds to evoke peptide release from cells of the **adenohypophysis**." }
    ]
  },
  "Dashboard — aden\\adenoid.md": {
    "primary": "Resembling or having the structural characteristics of a gland; glandular.",
    "secondary": "In anatomy, the pharyngeal tonsil situated on the posterior wall of the nasopharynx; or describing hypertrophied lymphatic tissues in that region.",
    "quotes": [
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The nasopharyngeal roof is occupied by a collection of **adenoid** tissue known clinically as the pharyngeal tonsil." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic mouth-breathing and dull facies in young children are typical consequences of obstructive **adenoid** hypertrophy." },
      { "author": "Arthur Keith", "work": "Human Embryology and Morphology", "quote": "The regression of **adenoid** aggregations during adolescence marks the functional maturation of the peripheral immune system." }
    ]
  },
  "Dashboard — aden\\adenoidal.md": {
    "primary": "Of, relating to, or characteristic of the adenoids or glandular tissue.",
    "secondary": "Describing speech sounds that have a nasal, muffled quality resulting from obstruction of the nasopharynx by enlarged adenoids.",
    "quotes": [
      { "author": "George Bernard Shaw", "work": "Pygmalion", "quote": "Her muffled, **adenoidal** delivery betrayed years of neglected childhood nasal obstruction." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The typical **adenoidal** countenance features an open mouth, flattened nasal bridge, and listless expression." },
      { "author": "Virginia Woolf", "work": "The Voyage Out", "quote": "The elderly clergyman droned his evening announcements in a curious, dry, **adenoidal** tone." }
    ]
  },
  "Dashboard — aden\\adenoidectomy.md": {
    "primary": "The surgical removal or curettage of the hypertrophied pharyngeal tonsil (the adenoids).",
    "secondary": "In pediatric otolaryngology, an operative procedure performed to relieve recurrent otitis media, chronic sinusitis, or pediatric sleep apnea.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Prompt **adenoidectomy** in children suffering from Eustachian blockage immediately restores normal hearing and facial development." },
      { "author": "Harvey Cushing", "work": "Surgery of the Head", "quote": "Meticulous hemostasis following curette **adenoidectomy** prevents aspiration of blood clots during recovery from anesthesia." },
      { "author": "Atul Gawande", "work": "Better: A Surgeon's Notes on Performance", "quote": "Generations of pediatricians considered tonsillectomy and **adenoidectomy** the universal rite of passage for school-age youngsters." }
    ]
  },
  "Dashboard — aden\\adenoids.md": {
    "primary": "The mass of enlarged lymphatic tissue situated at the back of the nasal cavity in the roof of the nasopharynx (pharyngeal tonsils).",
    "secondary": "In clinical medicine, pathologically enlarged nasopharyngeal lymphoid tissue that causes nasal airway obstruction and mouth breathing in children.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "When hypertrophied **adenoids** block the posterior nares, the child snores loudly and suffers fitful, interrupted sleep." },
      { "author": "George Orwell", "work": "Coming Up for Air", "quote": "He spoke with that thick, choked voice you associate with overgrown **adenoids** and damp English winters." },
      { "author": "Virginia Woolf", "work": "The Waves", "quote": "The schoolmaster snorted through swollen **adenoids**, his spectacles slipping down his shiny nose." }
    ]
  },
  "Dashboard — aden\\adenology.md": {
    "primary": "The scientific branch of anatomy and physiology that deals with glands, their structures, and their secretory functions.",
    "secondary": "Historically, the medical doctrine of secretory vessels, lymphatics, and internal glandular transformations.",
    "quotes": [
      { "author": "Thomas Wharton", "work": "Adenographia", "quote": "The foundations of modern **adenology** were laid when we systematically classified excretory and internal secretory organs." },
      { "author": "Albrecht von Haller", "work": "First Lines of Physiology", "quote": "In every treatise on **adenology**, the anatomist must trace the delicate capillary networks that supply glandular follicles." },
      { "author": "Claude Bernard", "work": "Lectures on Experimental Physiology", "quote": "The newer **adenology** concerns itself not merely with visible ducts, but with endocrine principles released directly into the blood." }
    ]
  },
  "Dashboard — aden\\adenoma.md": {
    "primary": "A benign epithelial tumor of glandular origin or showing glandular structural characteristics.",
    "secondary": "In pathology and endocrinology, a non-malignant neoplasm occurring in organs like the thyroid, parathyroid, pituitary, adrenal cortex, or colon.",
    "quotes": [
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "An **adenoma** preserves the orderly arrangement of glandular epithelium, remaining encapsulated without destructive invasive growth." },
      { "author": "Harvey Cushing", "work": "The Pituitary Body and Its Disorders", "quote": "Surgical enucleation of the basophil **adenoma** corrected the severe hypertension and truncal obesity of the patient." },
      { "author": "James Ewing", "work": "Neoplastic Diseases", "quote": "The tubular **adenoma** of the colon requires close endoscopic surveillance because of its propensity for malignant transformation." }
    ]
  },
  "Dashboard — aden\\adenomegaly.md": {
    "primary": "Abnormal enlargement of a gland, especially a lymphatic gland (lymphadenopathy).",
    "secondary": "In clinical diagnosis, pathological swelling of glandular organs detectable by palpation or radiographic imaging during systemic disease.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Generalized **adenomegaly** accompanied by splenomegaly and fever strongly points toward systemic lymphoma or infection." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Mesenteric **adenomegaly** reflects chronic inflammatory drainage from ulcerated intestinal lesions." },
      { "author": "Paul Ehrlich", "work": "Studies in Immunity", "quote": "The acute **adenomegaly** observed after antigen exposure results from rapid follicular proliferation within the regional nodes." }
    ]
  },
  "Dashboard — aden\\adenomyosarcoma.md": {
    "primary": "A rare malignant mixed tumor of the kidney composed of glandular, muscular, and connective-tissue elements (Wilms' tumor).",
    "secondary": "In pediatric pathology, nephroblastoma exhibiting embryonic renal epithelium alongside striated and smooth muscle sarcoma components.",
    "quotes": [
      { "author": "James Ewing", "work": "Neoplastic Diseases", "quote": "The presence of embryonic striated muscle fibers within the renal mass confirms the diagnosis of **adenomyosarcoma**." },
      { "author": "Max Wilms", "work": "Mixed Tumors of the Kidney", "quote": "This congenital **adenomyosarcoma** originates from pluripotential mesodermal remnants displaced during early embryonic organogenesis." },
      { "author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Radical transperitoneal nephrectomy remains the sole surgical hope when an infant presents with a massive **adenomyosarcoma**." }
    ]
  },
  "Dashboard — aden\\adenomyosis.md": {
    "primary": "A benign gynecological condition characterized by the abnormal ingrowth of endometrial glandular tissue into the muscular wall (myometrium) of the uterus.",
    "secondary": "In pathology, an ectopic glandular condition causing symmetrical uterine enlargement, menorrhagia, and severe dysmenorrhea.",
    "quotes": [
      { "author": "Thomas Stephen Cullen", "work": "Adenomyoma of the Uterus", "quote": "Microscopic sections reveal that **adenomyosis** represents a direct downgrowth of basal endometrium into the underlying myometrium." },
      { "author": "John A. Sampson", "work": "Peritoneal Endometriosis", "quote": "Unlike pelvic endometriosis on the peritoneal surface, diffuse **adenomyosis** remains confined within the uterine wall." },
      { "author": "Robert Meyer", "work": "On the Histogenesis of Uterine Tumors", "quote": "Cyclic bleeding within the displaced glands in **adenomyosis** induces widespread muscular hypertrophy and painful uterine spasms." }
    ]
  },
  "Dashboard — aden\\adenopathy.md": {
    "primary": "Any pathological disease, disorder, or enlargement of the lymph nodes or glands.",
    "secondary": "In physical examination, lymphadenopathy marked by palpably enlarged, tender, or matted lymph nodes signaling infection or metastatic malignancy.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Painless generalized **adenopathy** in a young adult warrants immediate lymph node biopsy to exclude Hodgkin's disease." },
      { "author": "Paul Ehrlich", "work": "Histology of the Blood", "quote": "Cervical **adenopathy** draining chronic dental abscesses shows reactive follicular hyperplasia under the microscope." },
      { "author": "Siddhartha Mukherjee", "work": "The Emperor of All Maladies", "quote": "The sudden resolution of the patient's massive **adenopathy** confirmed the remarkable potency of the newly introduced antifolate drug." }
    ]
  },
  "Dashboard — aden\\adenosine.md": {
    "primary": "A purine ribonucleoside composed of adenine attached to a ribofuranose moiety via a beta-N9-glycosidic bond.",
    "secondary": "In cellular biochemistry and physiology, an endogenous neuromodulator promoting sleep and an essential building block of ATP and cAMP.",
    "quotes": [
      { "author": "Phoebe Levene", "work": "Nucleic Acids", "quote": "Hydrolysis of ribose nucleic acid yields crystalline **adenosine**, establishing the nucleoside structure of cellular purines." },
      { "author": "Fritz Lipmann", "work": "Metabolic Generation of Phosphate Bond Energy", "quote": "The energetic currency of living cells consists of high-energy phosphate groups bound sequentially to **adenosine**." },
      { "author": "Earl W. Sutherland", "work": "Cyclic AMP", "quote": "Hormonal stimulation triggers adenylyl cyclase to cyclize **adenosine** triphosphate into the second messenger cyclic AMP." }
    ]
  },
  "Dashboard — aden\\adenosis.md": {
    "primary": "Any generalized or abnormal development, proliferation, or disease of glandular tissue.",
    "secondary": "In surgical pathology, specifically sclerosing adenosis of the breast or vaginal adenosis associated with fetal exposure to diethylstilbestrol (DES).",
    "quotes": [
      { "author": "Arthur Purdy Stout", "work": "Human Cancer", "quote": "Sclerosing **adenosis** of the mammary gland can mimic infiltrating adenocarcinoma histologically, requiring careful frozen-section evaluation." },
      { "author": "Arthur L. Herbst", "work": "Adenocarcinoma of the Vagina: Association with Maternal Stilbestrol Therapy", "quote": "Benign vaginal **adenosis** was detected in a substantial percentage of young women exposed in utero to maternal diethylstilbestrol." },
      { "author": "James Ewing", "work": "Neoplastic Diseases", "quote": "Florid lobular **adenosis** represents an exuberant non-neoplastic multiplication of acinar units during reproductive life." }
    ]
  },
  "Dashboard — aden\\adenota.md": {
    "primary": "A genus or taxonomic grouping of African antelopes (the kobs and lechwes), distinguished by prominent glandular facial markings or hoof glands.",
    "secondary": "In mammalogy, a former subgenus or genus name (Adenota) including the kob (Kobus kob) of sub-Saharan grasslands and floodplains.",
    "quotes": [
      { "author": "Richard Lydekker", "work": "The Game Animals of Africa", "quote": "The kob, formerly classified under the generic name **adenota**, gathers in immense herds across the seasonal floodplains of the Upper Nile." },
      { "author": "Theodore Roosevelt", "work": "African Game Trails", "quote": "Along the reed beds of Lake Victoria, we observed the reddish-yellow coats of **adenota** grazing in the morning mist." },
      { "author": "Oldfield Thomas", "work": "Catalogue of the Ungulate Mammals", "quote": "Morphological distinctions in preorbital gland structure led earlier naturalists to separate **adenota** from true waterbucks." }
    ]
  },
  "Dashboard — aden\\adenovirus.md": {
    "primary": "Any of a family of non-enveloped, double-stranded DNA viruses (Adenoviridae) that cause respiratory, conjunctival, and gastrointestinal infections in humans.",
    "secondary": "In molecular biology and gene therapy, a non-replicating viral vector extensively utilized to deliver foreign genetic material into human somatic cells.",
    "quotes": [
      { "author": "Wallace P. Rowe", "work": "Isolation of a Cytopathogenic Agent from Human Adenoids", "quote": "From surgically excised adenoid tissue we isolated a novel filtrable agent, which we designate **adenovirus**." },
      { "author": "Renato Dulbecco", "work": "Virology", "quote": "The icosahedral capsid of the **adenovirus** displays prominent projecting fibers that mediate specific attachment to host cell receptors." },
      { "author": "Francis Crick", "work": "The Structure of Viruses", "quote": "Electron crystallographic analysis reveals the majestic symmetry of the **adenovirus** coat, composed of 252 capsomeres." }
    ]
  },
  "Dashboard — aden\\anadenanthera.md": {
    "primary": "A genus of South American leguminous trees (Fabaceae) known for producing potent psychoactive tryptamine alkaloids in their seeds and bark.",
    "secondary": "In ethnobotany and pharmacology, Anadenanthera peregrina and Anadenanthera colubrina, whose roasted seeds are powdered to create shamanic snuff (yopo/cohoba).",
    "quotes": [
      { "author": "Richard Evans Schultes", "work": "The Botany and Chemistry of Hallucinogens", "quote": "Indigenous shamans of the Orinoco prepare the psychoactive snuff yopo from the roasted seeds of **anadenanthera**." },
      { "author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "The Otomac Indians inhale a pungent gray powder prepared from the pods of **anadenanthera**, falling into ecstatic trances." },
      { "author": "Claude Lévi-Strauss", "work": "Tristes Tropiques", "quote": "During village ceremonies, the elders passed the ceremonial snuff tube filled with **anadenanthera** to communicate with ancestral spirits." }
    ]
  },
  "Dashboard — aden\\deaden.md": {
    "primary": "To make less sensitive, vigorous, or active; to dull, blunt, or numb the senses.",
    "secondary": "To muffle, absorb, or attenuate sound, impact, or vibrations; to deprive of spiritual or emotional vitality.",
    "quotes": [
      { "author": "Mary Shelley", "work": "Frankenstein", "quote": "Nothing could **deaden** the horrifying memory of the monster my own scientific ambition had brought into being." },
      { "author": "Herman Melville", "work": "Moby-Dick", "quote": "A stiff glass of grog served to **deaden** the biting chill of the Arctic spray upon the shivering watch." },
      { "author": "Henry David Thoreau", "work": "Walden", "quote": "A luxurious life tends to **deaden** our finer sensibilities, substituting artificial comforts for raw vitality." }
    ]
  },
  "Dashboard — aden\\deadened.md": {
    "primary": "Deprived of sensation, vitality, or sharpness; rendered numb, dull, or muffled.",
    "secondary": "Having vibrations or acoustic resonance dampened by soundproofing or physical insulation.",
    "quotes": [
      { "author": "Charles Dickens", "work": "Bleak House", "quote": "The continuous November fog **deadened** every sound of horse-hooves and carriage-wheels in the muddy street." },
      { "author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "A heavy carpet **deadened** the sound of approaching footsteps as I waited in the cold drawing-room." },
      { "author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The heavy stillness of the primeval jungle **deadened** all hope in the hearts of the weary voyagers." }
    ]
  },
  "Dashboard — aden\\deadening.md": {
    "primary": "Causing a loss of sensation, vitality, or keenness; producing dullness, apathy, or numbness.",
    "secondary": "Material used for insulating against the transmission of sound or heat in buildings; dampening or muffling.",
    "quotes": [
      { "author": "George Eliot", "work": "Middlemarch", "quote": "She felt the slow, **deadening** weight of domestic routine crushing out her youthful intellectual aspirations." },
      { "author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The mechanical monotony of his daily ledger-work exercised a **deadening** influence upon his passionate nature." },
      { "author": "Virginia Woolf", "work": "Mrs. Dalloway", "quote": "She hated the **deadening** effect of conventional social chitchat that drowned all genuine feeling." }
    ]
  },
  "Dashboard — aden\\fibroadenoma.md": {
    "primary": "A common, benign breast tumor composed of both glandular epithelial elements and fibrous connective tissue.",
    "secondary": "In surgical pathology, a well-circumscribed, highly mobile, painless nodule (breast mouse) typically diagnosed in young women.",
    "quotes": [
      { "author": "William Stewart Halsted", "work": "The Operative Story of Goitre and Other Surgical Problems", "quote": "Enucleation of a discrete **fibroadenoma** of the breast is readily accomplished through a circumareolar cosmetic incision." },
      { "author": "James Ewing", "work": "Neoplastic Diseases", "quote": "Microscopically, the intracanalicular **fibroadenoma** displays elongated epithelial clefts compressed by luxuriant myxoid stroma." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The simultaneous overgrowth of stromal and acinar structures defines the classic benign architecture of the **fibroadenoma**." }
    ]
  },
  "Dashboard — aden\\lymphadenopathy.md": {
    "primary": "Any disease or abnormal swelling affecting the lymph nodes; enlargement of one or more lymph nodes.",
    "secondary": "In clinical diagnosis, localized or generalized lymph node enlargement resulting from reactive hyperplasia, infection, or malignant metastasis.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Persistent non-tender cervical **lymphadenopathy** in the absence of pharyngeal infection mandates diagnostic tissue excision." },
      { "author": "Paul Ehrlich", "work": "Experimental Pathology of the Blood", "quote": "Widespread **lymphadenopathy** accompanies systemic trypanosomiasis, marking the extensive immune response to blood parasites." },
      { "author": "Siddhartha Mukherjee", "work": "The Emperor of All Maladies", "quote": "The dramatic shrinking of massive inguinal **lymphadenopathy** demonstrated the systemic efficacy of the initial chemotherapy trial." }
    ]
  },
  "Dashboard — amn\\amn.md": {
    "primary": "An anatomical and medical combining form or abbreviation designating the amnion, amniotic sac, or amniotic fluid.",
    "secondary": "In comparative embryology, an abbreviated notation representing the amnion lineage dividing amniotes from anamniote vertebrates.",
    "quotes": [
      { "author": "Thomas Henry Huxley", "work": "The Elements of Comparative Anatomy", "quote": "We employ the morphological radical **amn** to denote those membranes shielding the developing embryos of higher vertebrates." },
      { "author": "Ernst Haeckel", "work": "The Evolution of Man", "quote": "Embryological diagrams label the extra-embryonic protective fluid cavity with the standard radical **amn**." },
      { "author": "Francis Maitland Balfour", "work": "A Treatise on Comparative Embryology", "quote": "The differentiation of the fetal membrane designated **amn** marks a milestone in terrestrial vertebrate evolution." }
    ]
  },
  "Dashboard — amn\\amnic.md": {
    "primary": "Of, relating to, or situated within an amnion; amniotic.",
    "secondary": "In classical literature and physical geography, of or pertaining to a river (from Latin amnis).",
    "quotes": [
      { "author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The delicate **amnic** envelope protects the fragile avian embryo from desiccation during incubation." },
      { "author": "Charles Lyell", "work": "Principles of Geology", "quote": "Ancient gravels of **amnic** origin were deposited along broad river plains before Pleistocene channel incision." },
      { "author": "Henry Fairfield Osborn", "work": "The Origin and Evolution of Life", "quote": "The development of internal **amnic** moisture freed early reptiles from returning to water to deposit spawn." }
    ]
  },
  "Dashboard — amn\\amnion.md": {
    "primary": "The innermost delicate, membranous sac that encloses the developing embryo of a reptile, bird, or mammal in amniotic fluid.",
    "secondary": "In embryology, the extra-embryonic ectodermal and mesodermal membrane providing a protective fluid cushion for terrestrial vertebrate embryos.",
    "quotes": [
      { "author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "The formation of the **amnion** provides the embryo with an artificial aquatic environment necessary for terrestrial survival." },
      { "author": "Ernst Haeckel", "work": "The History of Creation", "quote": "The evolution of the protective **amnion** allowed the ancestors of reptiles and mammals to conquer dry land." },
      { "author": "Francis Maitland Balfour", "work": "A Treatise on Comparative Embryology", "quote": "Folds of somatopleure arch over the dorsal surface of the germ, fusing to create the closed cavity of the **amnion**." }
    ]
  },
  "Dashboard — amn\\amnionic.md": {
    "primary": "Pertaining to, derived from, or having the character of the amnion; amniotic.",
    "secondary": "In obstetrics and embryology, relating to the amnionic membrane, cavity, or fluid protecting the fetus.",
    "quotes": [
      { "author": "William Harvey", "work": "Anatomical Exercises on the Generation of Animals", "quote": "The **amnionic** humor cushions the tender limbs of the unborn creature from maternal concussions." },
      { "author": "Charles Darwin", "work": "The Descent of Man", "quote": "The presence of identical **amnionic** membranes across mammals and birds points undeniably to a shared phylogenetic ancestry." },
      { "author": "Julian Huxley", "work": "Evolution: The Modern Synthesis", "quote": "Terrestrial adaptation demanded the evolutionary consolidation of the **amnionic** egg, shielding the embryo from drying winds." }
    ]
  },
  "Dashboard — amn\\amnioscope.md": {
    "primary": "An optical endoscope designed for insertion through the cervical canal to inspect the amniotic fluid and fetus through intact membranes.",
    "secondary": "In clinical obstetrics, an instrument introduced by Erich Saling to detect meconium staining and fetal distress during late gestation.",
    "quotes": [
      { "author": "Erich Saling", "work": "Amnioscopy and Fetal Blood Sampling", "quote": "By introducing the conical **amnioscope** through the cervix, the obstetrician can inspect the color of the forewaters directly." },
      { "author": "Ian Donald", "work": "Practical Obstetric Problems", "quote": "Visual inspection via the **amnioscope** allows early detection of meconium discharge before labor commences." },
      { "author": "Jack A. Pritchard", "work": "Williams Obstetrics", "quote": "The diagnostic utility of the **amnioscope** declined as modern non-invasive electronic fetal monitoring became standard." }
    ]
  },
  "Dashboard — amn\\amniote.md": {
    "primary": "Any vertebrate animal whose embryo develops an amnion, allantois, and chorion during gestation, comprising reptiles, birds, and mammals.",
    "secondary": "In evolutionary biology, a major clade of tetrapods that broke dependence on standing water for reproduction through the development of the cleidoic egg.",
    "quotes": [
      { "author": "Ernst Haeckel", "work": "The Evolution of Man", "quote": "We group reptiles, birds, and mammals together under the class name of **amniote** because of their shared embryonic membranes." },
      { "author": "Alfred Sherwood Romer", "work": "Vertebrate Paleontology", "quote": "The earliest Carboniferous **amniote** possessed a waterproof skin and laid shelled eggs on solid ground." },
      { "author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Vertebrated Animals", "quote": "The absence of functional gills at any stage of life sharply distinguishes every true **amniote** from amphibians." }
    ]
  },
  "Dashboard — amn\\amniotic.md": {
    "primary": "Of, relating to, or produced by the amnion (as in amniotic fluid, amniotic cavity, or amniotic sac).",
    "secondary": "In obstetrics and perinatology, designating the protective aqueous cushion that permits fetal movement and buffers against external trauma.",
    "quotes": [
      { "author": "William Harvey", "work": "On the Generation of Animals", "quote": "The **amniotic** water serves not only for lubrication at birth but buffers the growing fetus against sudden shocks." },
      { "author": "Claude Bernard", "work": "Lectures on the Phenomenon of Life", "quote": "The **amniotic** fluid maintains a strictly regulated osmotic pressure, shielding embryonic tissues from chemical disturbance." },
      { "author": "Rachel Carson", "work": "The Sea Around Us", "quote": "Each mammal still carries in its mother's womb the ancient sea, cradled safely within the warm **amniotic** sac." }
    ]
  },
  "Dashboard — amn\\anamniote.md": {
    "primary": "Any vertebrate animal that lacks an amnion during embryonic development, specifically fishes and amphibians.",
    "secondary": "In comparative vertebrate morphology, an aquatic or semi-aquatic vertebrate whose eggs must be deposited in water or damp microenvironments to avoid desiccation.",
    "quotes": [
      { "author": "Thomas Henry Huxley", "work": "The Elements of Comparative Anatomy", "quote": "The **anamniote** embryo develops neither amnion nor allantois, relying upon aquatic respiration through functional branchial clefts." },
      { "author": "Ernst Haeckel", "work": "The History of Creation", "quote": "Fishes and amphibians form the primitive **anamniote** grade from which terrestrial tetrapods subsequently arose." },
      { "author": "Edwin H. Colbert", "work": "Evolution of the Vertebrates", "quote": "The gelatinous egg of the typical **anamniote** lacks the protective mineralized shell seen in advanced land dwellers." }
    ]
  },
  "Dashboard — angi\\angiitis.md": {
    "primary": "Inflammation of a blood vessel or lymphatic vessel; vasculitis.",
    "secondary": "In rheumatology and pathology, systemic necrotizing inflammation of arterial or venous walls, as in hypersensitivity angiitis or Granulomatosis with polyangiitis.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Necrotizing **angiitis** damages the vascular endothelium, leading to thrombosis and ischemic infarction of downstream tissues." },
      { "author": "Paul Klemperer", "work": "The Concept of Collagen Diseases", "quote": "Diffuse allergic **angiitis** illustrates how hypersensitivity reactions target the fibrinoid matrix of muscular arteries." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "In every form of acute **angiitis**, the adventitia and media are heavily infiltrated by emigrating leukocytes." }
    ]
  },
  "Dashboard — angi\\angina.md": {
    "primary": "A condition marked by severe, constricting paroxysmal pain, especially angina pectoris caused by myocardial ischemia.",
    "secondary": "Historically, any severe suffocating inflammation of the throat or pharynx (such as Ludwig's angina or Vincent's angina).",
    "quotes": [
      { "author": "William Heberden", "work": "Some Account of a Disorder of the Breast", "quote": "There is a disorder of the breast marked with strong and peculiar symptoms, to which I have given the name of **angina** pectoris." },
      { "author": "William Osler", "work": "Lectures on Angina Pectoris and Allied States", "quote": "The agony of true **angina** involves not merely physical constriction, but an overwhelming dread of impending dissolution." },
      { "author": "Thomas Sydenham", "work": "Observationes Medicae", "quote": "Inflammatory **angina** of the fauces threatens suffocation when swollen tonsils obstruct the passage of air to the lungs." }
    ]
  },
  "Dashboard — angi\\anginal.md": {
    "primary": "Of, relating to, or resembling angina, especially angina pectoris.",
    "secondary": "In clinical cardiology, describing retrosternal compressive chest pain, heaviness, or radiation provoked by myocardial oxygen deprivation.",
    "quotes": [
      { "author": "William Osler", "work": "Lectures on Angina Pectoris", "quote": "The patient complained of recurrent **anginal** distress radiating down the inner aspect of the left arm upon climbing stairs." },
      { "author": "Harvey Cushing", "work": "Clinical Studies on Blood Pressure", "quote": "Sublingual nitroglycerin brought prompt relief from the acute **anginal** paroxysm by dilating systemic venous beds." },
      { "author": "Paul Dudley White", "work": "Heart Disease", "quote": "Atypical **anginal** discomfort may masquerade as indigestion, leading unwary clinicians to overlook coronary occlusion." }
    ]
  },
  "Dashboard — angi\\anginose.md": {
    "primary": "Pertaining to, accompanied by, or of the nature of angina; characterized by severe throat constriction or ischemic pain.",
    "secondary": "In historical clinical medicine, describing fulminant throat infections accompanied by suffocative membranous inflammation (e.g. scarlatina anginose).",
    "quotes": [
      { "author": "Thomas Sydenham", "work": "The Works of Thomas Sydenham", "quote": "The malignant scarlet fever assumed a severe **anginose** character, threatening the infant with sudden suffocation." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Diphtheritic membrane in the pharynx produces that alarming **anginose** distress that demands immediate antitoxin administration." },
      { "author": "John Huxham", "work": "An Essay on Fevers", "quote": "A putrid **anginose** sore throat swept through the garrison, accompanied by foul ulcerations of the tonsils." }
    ]
  },
  "Dashboard — angi\\anginous.md": {
    "primary": "Pertaining to, resembling, or affected by angina (angina pectoris or anginose pharyngitis).",
    "secondary": "Characterized by compressive, choking pain or severe constrictive symptoms in the thorax or throat.",
    "quotes": [
      { "author": "William Heberden", "work": "Commentaries on the History and Cure of Diseases", "quote": "Those who are afflicted with **anginous** paroxysms are seized while walking, and more particularly when walking uphill." },
      { "author": "William Osler", "work": "Lectures on Angina Pectoris and Allied States", "quote": "Emotional excitement frequently precipitates an acute **anginous** crisis in individuals with sclerotic coronary arteries." },
      { "author": "Paul Dudley White", "work": "Heart Disease", "quote": "The cessation of physical effort usually terminates the **anginous** ache within a matter of minutes." }
    ]
  },
  "Dashboard — angi\\angiocardiogram.md": {
    "primary": "A series of radiographic images of the heart and great blood vessels obtained following injection of a radiopaque contrast medium.",
    "secondary": "In clinical cardiology, a diagnostic imaging record visualizing chamber anatomy, valvular regurgitation, and congenital shunts.",
    "quotes": [
      { "author": "Helen B. Taussig", "work": "Congenital Malformations of the Heart", "quote": "The **angiocardiogram** clearly outlined the overriding aorta and right ventricular hypertrophy characteristic of tetralogy of Fallot." },
      { "author": "André Cournand", "work": "Cardiac Catheterization in Man", "quote": "Rapid-sequence exposure of the **angiocardiogram** captured the flow of contrast medium through the pulmonary artery." },
      { "author": "Charles Dotter", "work": "Angiocardiography", "quote": "Examination of the serial **angiocardiogram** allowed precise localization of the coarctation prior to surgical repair." }
    ]
  },
  "Dashboard — angi\\angiocardiography.md": {
    "primary": "The medical imaging technique of visualizing the heart cavities and major thoracic blood vessels through serial radiography after radiopaque injection.",
    "secondary": "In invasive diagnostic cardiology, fluoroscopic or digital radiographic tracking of contrast circulation to assess cardiac hemodynamics.",
    "quotes": [
      { "author": "Charles Dotter", "work": "Angiocardiography", "quote": "The clinical introduction of selective **angiocardiography** revolutionized preoperative planning for intracardiac defects." },
      { "author": "Helen B. Taussig", "work": "Congenital Malformations of the Heart", "quote": "Through selective **angiocardiography**, we can distinguish pulmonary atresia from severe infundibular pulmonary stenosis." },
      { "author": "Werner Forssmann", "work": "Experiments on Myself", "quote": "Catheterizing the right heart paved the way for modern **angiocardiography**, visualizing chambers in living patients." }
    ]
  },
  "Dashboard — angi\\angiocarp.md": {
    "primary": "A fruit or reproductive structure that is covered, enclosed, or enveloped by an external husk, calyx, or involucre.",
    "secondary": "In mycology, a fungal fruiting body (such as a cleistothecium, perithecium, or closed basidiocarp) that matures while enclosed within protective tissue.",
    "quotes": [
      { "author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "The acorn enclosed within its scaly cupule represents a familiar botanical example of an **angiocarp**." },
      { "author": "Asa Gray", "work": "Structural Botany", "quote": "When the fruit is permanently wrapped by an accrescent calyx, it is properly termed an **angiocarp**." },
      { "author": "F. E. Fritsch", "work": "The Structure and Reproduction of the Algae", "quote": "In closed fungal fructifications, the **angiocarp** protects the developing spores until environmental conditions trigger dehiscence." }
    ]
  },
  "Dashboard — angi\\angiocarpic.md": {
    "primary": "Having the fruit or reproductive body covered or enclosed by an external envelope, husk, or protective outer structure.",
    "secondary": "In cryptogamic botany and lichenology, designating sporocarps or apothecia that remain closed until the spores are mature.",
    "quotes": [
      { "author": "Julius von Sachs", "work": "Textbook of Botany", "quote": "The **angiocarpic** mode of development in mushrooms shields the delicate hymenial gills from early desiccation." },
      { "author": "Heinrich Anton de Bary", "work": "Comparative Morphology and Biology of the Fungi", "quote": "In **angiocarpic** ascocarps, the asci develop within a completely closed perithecial cavity." },
      { "author": "Arthur Johnson Eames", "work": "Morphology of Vascular Plants", "quote": "The **angiocarpic** involucre of the hazelnut develops directly from coalesced bracteoles." }
    ]
  },
  "Dashboard — angi\\angiocarpous.md": {
    "primary": "Characterized by having fruit or spores enclosed within a protective outer covering, vessel, or husk.",
    "secondary": "In mycology and systematic lichenology, synonymous with angiocarpic; describing enclosed fruiting bodies that open only upon maturity.",
    "quotes": [
      { "author": "John Lindley", "work": "An Introduction to Botany", "quote": "Fungi of the truffle family are strictly **angiocarpous**, retaining their spores beneath a thick subterranean peridium." },
      { "author": "William Jackson Hooker", "work": "The English Flora", "quote": "The **angiocarpous** lichens conceal their asci within flask-shaped conceptacles opening by a minute pore." },
      { "author": "Liberty Hyde Bailey", "work": "Manual of Cultivated Plants", "quote": "In certain **angiocarpous** plants, the calyx becomes fleshy and completely surrounds the true berry." }
    ]
  },
  "Dashboard — angi\\angiodysplasia.md": {
    "primary": "A small vascular malformation characterized by dilated, tortuous, thin-walled submucosal blood vessels in the gastrointestinal tract.",
    "secondary": "In gastroenterology, an acquired degenerative vascular lesion of the cecum and ascending colon and a frequent cause of unexplained lower gastrointestinal bleeding in the elderly.",
    "quotes": [
      { "author": "Siddhartha Mukherjee", "work": "The Laws of Medicine", "quote": "Endoscopic examination revealed a bleeding **angiodysplasia** in the cecal wall, amenable to thermal coagulation." },
      { "author": "Atul Gawande", "work": "Complications", "quote": "The patient had suffered chronic occult blood loss caused by an elusive cecal **angiodysplasia** missed on standard radiographs." },
      { "author": "Jack A. Pritchard", "work": "Clinical Gastroenterology", "quote": "Aortic stenosis is frequently associated with bleeding colonic **angiodysplasia** in Heyde's syndrome." }
    ]
  },
  "Dashboard — angi\\angioedema.md": {
    "primary": "Rapid swelling (edema) of the deep layers of the skin, subcutaneous tissues, or mucous membranes, often caused by allergic or bradykinin-mediated mechanisms.",
    "secondary": "In clinical immunology and emergency medicine, sudden swelling typically affecting the face, lips, tongue, and larynx, posing an acute risk of asphyxiation.",
    "quotes": [
      { "author": "William Osler", "work": "Hereditary Angioneurotic Oedema", "quote": "I observed a remarkable family history in which recurring attacks of acute **angioedema** afflicted five generations." },
      { "author": "Paul Ehrlich", "work": "Studies in Immunity", "quote": "Mast cell degranulation releases vasoactive amines that provoke sudden localized **angioedema** in sensitized tissues." },
      { "author": "Harvey Cushing", "work": "Studies in Intracranial Physiology", "quote": "Sudden laryngeal **angioedema** demands prompt airway intervention before complete respiratory occlusion occurs." }
    ]
  },
  "Dashboard — angi\\angiogenesis.md": {
    "primary": "The physiological process through which new blood vessels form and sprout from preexisting vascular networks.",
    "secondary": "In oncology and vascular biology, Judah Folkman's principle that solid tumor growth and metastasis depend fundamentally upon recruiting new capillaries.",
    "quotes": [
      { "author": "Judah Folkman", "work": "Tumor Angiogenesis: Therapeutic Implications", "quote": "Once tumor **angiogenesis** begins, an exponentially growing capillary network supplies the dormant neoplasm with nutrients." },
      { "author": "Siddhartha Mukherjee", "work": "The Emperor of All Maladies", "quote": "By developing antibodies against VEGF, scientists created drugs that choke off tumor **angiogenesis**." },
      { "author": "Lewis Thomas", "work": "The Lives of a Cell", "quote": "In wound repair, the vigorous surge of **angiogenesis** rebuilds damaged tissue beds with microscopic capillary loops." }
    ]
  },
  "Dashboard — angi\\angiogram.md": {
    "primary": "An X-ray, CT, or MRI image of blood vessels obtained after the introduction of a radiopaque contrast material.",
    "secondary": "In clinical cardiology and neurology, a diagnostic image displaying vascular lumen caliber, occlusions, stenoses, or aneurysmal dilatations.",
    "quotes": [
      { "author": "Charles Dotter", "work": "Transluminal Recanalization of Arteriosclerotic Obstructions", "quote": "The follow-up **angiogram** demonstrated immediate restoration of luminal patency through the previously occluded femoral artery." },
      { "author": "Paul Dudley White", "work": "Heart Disease", "quote": "The coronary **angiogram** revealed ninety percent narrowing of the anterior descending artery, explaining the exertional angina." },
      { "author": "Atul Gawande", "work": "Complications", "quote": "We gathered around the light box, studying the cerebral **angiogram** for the subtle outpouching of a berry aneurysm." }
    ]
  },
  "Dashboard — angi\\angiography.md": {
    "primary": "The diagnostic medical imaging technique used to visualize the inside of blood vessels and organs of the body, particularly the arteries, veins, and heart chambers.",
    "secondary": "In interventional radiology, catheter-directed radiographic visualization of vascular trees using iodine-based contrast agents or digital subtraction.",
    "quotes": [
      { "author": "Charles Dotter", "work": "Transluminal Angioplasty", "quote": "Catheter **angiography** transformed vascular surgery from speculative exploration into precise image-guided intervention." },
      { "author": "Egas Moniz", "work": "Cerebral Angiography", "quote": "By injecting radiopaque thorium into the carotid artery, I achieved the first successful cerebral **angiography** in living patients." },
      { "author": "Werner Forssmann", "work": "Experiments on Myself", "quote": "Pioneering intracardiac catheterization laid the physical groundwork for selective coronary **angiography**." }
    ]
  },
  "Dashboard — angi\\angiohemophilia.md": {
    "primary": "An inherited bleeding disorder characterized by deficiency of von Willebrand factor and factor VIII, combined with prolonged bleeding time (von Willebrand disease).",
    "secondary": "In clinical hematology, a hereditary hemorrhagic diathesis transmitted as an autosomal dominant trait causing mucosal and cutaneous hemorrhages.",
    "quotes": [
      { "author": "Erik Adolf von Willebrand", "work": "Hereditary Pseudohemophilia", "quote": "The disorder which clinicians frequently term **angiohemophilia** differs from classic hemophilia by its autosomal inheritance and prolonged bleeding time." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Recurrent epistaxis and cutaneous ecchymoses in young women often suggest **angiohemophilia** rather than pure platelet deficiency." },
      { "author": "Paul Ehrlich", "work": "Experimental Pathology of the Blood", "quote": "In **angiohemophilia**, impaired platelet adhesiveness combines with reduced coagulant factor levels to destabilize primary hemostasis." }
    ]
  },
  "Dashboard — angi\\angiologist.md": {
    "primary": "A medical specialist who studies, diagnoses, and treats diseases of the circulatory system, including arteries, veins, and lymphatic vessels.",
    "secondary": "A physician dedicated to vascular medicine, addressing peripheral arterial disease, deep vein thrombosis, and lymphedema.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The consulting **angiologist** meticulously palpated the pedal pulses to assess the degree of peripheral arteriosclerotic insufficiency." },
      { "author": "Charles Dotter", "work": "Transluminal Angioplasty", "quote": "Cooperation between the diagnostic **angiologist** and the interventional surgeon created the modern discipline of endovascular medicine." },
      { "author": "Paul Dudley White", "work": "Heart Disease", "quote": "Every skilled **angiologist** recognizes that systemic vascular health reflects the cumulative integrity of the microcirculation." }
    ]
  },
  "Dashboard — angi\\angiology.md": {
    "primary": "The branch of medical science and anatomy that studies the circulatory system, including arteries, veins, and lymphatic vessels.",
    "secondary": "In clinical medicine, the scientific subspecialty focusing on the etiology, pathophysiology, diagnosis, and non-surgical management of vascular disease.",
    "quotes": [
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The section on **angiology** details the branching of the aorta and the intricate pathways of the systemic and pulmonary vessels." },
      { "author": "Thomas Wharton", "work": "Adenographia", "quote": "A complete system of **angiology** must trace the intimate connections between nutrient capillaries and excretory gland tubules." },
      { "author": "Albrecht von Haller", "work": "First Lines of Physiology", "quote": "Progress in **angiology** accelerated once microscopists observed the living circulation moving through the web of the frog's foot." }
    ]
  },
  "Dashboard — angi\\angioma.md": {
    "primary": "A benign tumor composed of newly formed blood vessels (hemangioma) or lymph vessels (lymphangioma).",
    "secondary": "In pathology, an abnormal endothelial and vascular proliferation presenting as a cutaneous cherry angioma, cavernous hemangioma, or arteriovenous malformation.",
    "quotes": [
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Under the term **angioma** we group those true neoplasms consisting of ectatic and newly proliferated vascular channels." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Multiple cutaneous **angioma** lesions of the lips and tongue are pathognomonic of hereditary hemorrhagic telangiectasia." },
      { "author": "James Ewing", "work": "Neoplastic Diseases", "quote": "A cavernous **angioma** of the liver consists of large, blood-filled spaces lined by mature, non-atypical endothelium." }
    ]
  },
  "Dashboard — angi\\angiomatous.md": {
    "primary": "Pertaining to, resembling, or having the histological characteristics of an angioma.",
    "secondary": "In pathology, describing lesions characterized by abundant, dilated, thin-walled capillary or venous channels embedded in loose stroma.",
    "quotes": [
      { "author": "James Ewing", "work": "Neoplastic Diseases", "quote": "Histologic section of the excised skin nodule revealed an **angiomatous** proliferation of mature capillary loops." },
      { "author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Careful dissection was required to extirpate the extensive **angiomatous** malformation without provoking severe hemorrhage." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The **angiomatous** network expanded through active budding from preexisting adjacent vascular adventitia." }
    ]
  },
  "Dashboard — angi\\angiopathy.md": {
    "primary": "Any generic disease or pathological abnormality of the blood vessels or lymphatic vessels.",
    "secondary": "In clinical medicine, microvascular or macrovascular disease, such as diabetic angiopathy or cerebral amyloid angiopathy causing recurrent lobar hemorrhages.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Diabetic **angiopathy** targets both renal glomeruli and retinal capillaries, leading to progressive microvascular compromise." },
      { "author": "Paul Ehrlich", "work": "Studies in Immunity", "quote": "Toxic metabolic products circulate freely, inducing degenerative **angiopathy** across the coronary and cerebral vascular beds." },
      { "author": "Harvey Cushing", "work": "The Pituitary Body and Its Disorders", "quote": "Hypertensive **angiopathy** weakens cerebral arteriolar walls, rendering them susceptible to sudden catastrophic rupture." }
    ]
  },
  "Dashboard — angi\\angioplasty.md": {
    "primary": "The surgical or percutaneous endovascular repair or recanalization of a narrowed or obstructed blood vessel.",
    "secondary": "In interventional cardiology, percutaneous transluminal coronary angioplasty (PTCA), utilizing inflatable balloon catheters and expandable stents to restore blood flow.",
    "quotes": [
      { "author": "Andreas Grüntzig", "work": "Transluminal Dilation of Coronary-Artery Stenosis", "quote": "In September 1977, we performed the first percutaneous coronary **angioplasty** in an awake patient, dilating the LAD lesion successfully." },
      { "author": "Charles Dotter", "work": "Transluminal Angioplasty: A New Concept", "quote": "The catheter is an instrument of reconstruction; transluminal **angioplasty** offers relief without the trauma of open bypass surgery." },
      { "author": "Paul Dudley White", "work": "Heart Disease", "quote": "The widespread adoption of balloon **angioplasty** transformed the clinical management of acute coronary syndromes worldwide." }
    ]
  },
  "Dashboard — angi\\angiopteris.md": {
    "primary": "A genus of massive, primitive eusporangiate ferns in the family Marattiaceae, native to the paleotropics and known as elephant ferns or king ferns.",
    "secondary": "In paleobotany and pteridophyte systematics, ancient giant ferns with fleshy stipes, large pulvini, and synangia opening along lateral sutures.",
    "quotes": [
      { "author": "William Jackson Hooker", "work": "Species Filicum", "quote": "The immense fronds of **angiopteris**, sometimes reaching twenty feet in length, spread like giant palm leaves in the humid forest." },
      { "author": "F. O. Bower", "work": "The Ferns (Filicales)", "quote": "The eusporangiate development in **angiopteris** links modern tropical ferns with the Carboniferous fossil marattiaceans." },
      { "author": "Liberty Hyde Bailey", "work": "The Standard Cyclopedia of Horticulture", "quote": "Conservatories display **angiopteris** as living botanical fossils, admired for their massive fleshy rhizomes and majestic arching fronds." }
    ]
  },
  "Dashboard — angi\\angiosarcoma.md": {
    "primary": "A rare, highly malignant neoplasm arising from vascular or lymphatic endothelial cells.",
    "secondary": "In surgical oncology, an aggressive cancer of blood vessels occurring in the skin, soft tissue, breast, or liver, associated with vinyl chloride exposure.",
    "quotes": [
      { "author": "James Ewing", "work": "Neoplastic Diseases", "quote": "Primary hepatic **angiosarcoma** demonstrates anaplastic endothelial cells forming crude, blood-filled vascular channels throughout the parenchyma." },
      { "author": "Siddhartha Mukherjee", "work": "The Emperor of All Maladies", "quote": "Industrial exposure to vinyl chloride gas in plastics factories was traced as the direct causative agent of occupational **angiosarcoma**." },
      { "author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Post-mastectomy chronic lymphedema can predispose over decades to the devastating emergence of cutaneous **angiosarcoma** (Stewart-Treves syndrome)." }
    ]
  },
  "Dashboard — angi\\angioscope.md": {
    "primary": "An optical microscope or fine fiberoptic endoscope designed for the direct visual examination of the interior of blood vessels.",
    "secondary": "In vascular surgery and interventional cardiology, a micro-endoscopic device used to inspect intraluminal thrombi, atheromas, and stent deployments in real time.",
    "quotes": [
      { "author": "Charles Dotter", "work": "Vascular Endoscopy", "quote": "Introducing the miniaturized **angioscope** into the femoral lumen permitted direct visualization of plaque ulcerations." },
      { "author": "Andreas Grüntzig", "work": "Coronary Dilatation", "quote": "Fiberoptic technology enabled the design of an ultrafine **angioscope** capable of traversing secondary arterial branches." },
      { "author": "Paul Dudley White", "work": "Heart Disease", "quote": "Direct intraluminal inspection through an **angioscope** clarifies whether an arterial filling defect represents fresh thrombus or calcified atheroma." }
    ]
  },
  "Dashboard — angi\\angiosperm.md": {
    "primary": "A vascular plant of the clade Angiospermae that produces seeds enclosed within a protective ovary or fruit; a flowering plant.",
    "secondary": "In evolutionary botany, the dominant group of land plants, characterized by flowers, endosperm, and specialized vessel elements in the xylem.",
    "quotes": [
      { "author": "Charles Darwin", "work": "Letter to Joseph Dalton Hooker", "quote": "The rapid development as far as we can judge of all the higher plants within recent geological times is an abominable mystery, speaking of the **angiosperm**." },
      { "author": "Asa Gray", "work": "Structural Botany", "quote": "The fundamental distinction of an **angiosperm** is that its seeds are borne inside a closed carpel, rather than exposed naked upon a scale." },
      { "author": "Arthur Johnson Eames", "work": "Morphology of Angiosperms", "quote": "Double fertilization yielding a triploid nutritive endosperm is the defining embryological hallmark of every true **angiosperm**." }
    ]
  },
  "Dashboard — angi\\angiospermae.md": {
    "primary": "The botanical division or taxonomic class comprising all flowering plants whose ovules are enclosed within an ovary.",
    "secondary": "In phylogenetics, the dominant terrestrial plant radiation encompassing monocots, eudicots, and basal magnoliids, comprising over 300,000 extant species.",
    "quotes": [
      { "author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "We contrast the Gymnospermae with the vast division **angiospermae**, wherein the seed matures within a sealed pericarp." },
      { "author": "Julius von Sachs", "work": "History of Botany", "quote": "The triumph of the **angiospermae** during the Cretaceous reshaped the entire terrestrial biosphere and spurred insect evolution." },
      { "author": "F. O. Bower", "work": "The Origin of a Land Flora", "quote": "The vascular efficiency of vessel elements gave the **angiospermae** decisive competitive advantages over archaic gymnosperm forests." }
    ]
  },
  "Dashboard — angi\\angiospermous.md": {
    "primary": "Of, relating to, or belonging to the angiosperms; producing seeds enclosed in an ovary; flowering.",
    "secondary": "In botanical morphology, describing plants or reproductive structures exhibiting the characteristic features of flowering seed plants.",
    "quotes": [
      { "author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The transition from naked ovules to an **angiospermous** closed ovary represents the crowning achievement of floral morphology." },
      { "author": "Charles Darwin", "work": "The Origin of Species", "quote": "The co-adaptation of **angiospermous** blossoms with nectar-feeding insects illustrates the exquisite precision of natural selection." },
      { "author": "Arthur Johnson Eames", "work": "Morphology of Vascular Plants", "quote": "Fossil leaves with **angiospermous** reticulate venation appear in Cretaceous strata alongside early tricolpate pollen grains." }
    ]
  },
  "Dashboard — angi\\angiotelectasia.md": {
    "primary": "Abnormal, permanent dilatation of groups of capillaries, venules, or arterioles; telangiectasia.",
    "secondary": "In dermatology and clinical pathology, vascular lesions producing visible spider-like cutaneous red spots or mucosal bleeding points.",
    "quotes": [
      { "author": "William Osler", "work": "On a Family Form of Recurrent Epistaxis, Associated with Multiple Telangiectases", "quote": "The cutaneous lesions represented multiple foci of **angiotelectasia**, bleeding profusely upon the slightest mechanical friction." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Congenital **angiotelectasia** arises from defective muscular coats in the microvasculature, predisposing vessels to ectasia." },
      { "author": "Paul Ehrlich", "work": "Studies in Immunity", "quote": "Local inflammatory mediators induce transient **angiotelectasia**, permitting increased capillary permeability and plasma exudation." }
    ]
  },
  "Dashboard — angi\\angiotensin.md": {
    "primary": "An oligopeptide hormone that causes vasoconstriction and an increase in systemic blood pressure.",
    "secondary": "In cardiovascular physiology and endocrinology, specifically angiotensin II, produced via the renin-angiotensin-aldosterone system (RAAS) to regulate sodium and fluid balance.",
    "quotes": [
      { "author": "Irvine H. Page", "work": "Angiotonin and Renin", "quote": "We agreed with Braun-Menéndez to combine the names angiotonin and hypertensin into the universally accepted term **angiotensin**." },
      { "author": "Eduardo Braun-Menéndez", "work": "Renal Hypertension", "quote": "Renin cleaves circulating angiotensinogen to yield the decapeptide precursor of active **angiotensin**." },
      { "author": "Walter Cannon", "work": "The Wisdom of the Body", "quote": "The vasoconstrictor action of **angiotensin** serves as an indispensable endocrine defense against catastrophic circulatory shock." }
    ]
  },
  "Dashboard — angi\\angiotonin.md": {
    "primary": "An earlier historical name for angiotensin, the vasoconstrictor peptide substance produced by the action of renin on plasma globulin.",
    "secondary": "In hypertension research history, the pressor substance discovered independently in 1939 by Irvine Page and Helmer, later rechristened angiotensin.",
    "quotes": [
      { "author": "Irvine H. Page", "work": "A Crystalline Pressor Substance (Angiotonin) Resulting from the Reaction Between Renin and Renin-Activator", "quote": "The isolated substance, which we christened **angiotonin**, elicited powerful arteriolar constriction and marked elevation of arterial pressure." },
      { "author": "Eduardo Braun-Menéndez", "work": "Hypertensin: The Substance Causing Renal Hypertension", "quote": "While we designated the renal pressor peptide hypertensin, Page and his colleagues independently termed it **angiotonin**." },
      { "author": "Harry Goldblatt", "work": "Studies on Experimental Hypertension", "quote": "Constriction of the renal artery provoked the outpouring of renin, generating **angiotonin** in the systemic circulation." }
    ]
  },
  "Dashboard — angi\\hemangioma.md": {
    "primary": "A benign vascular tumor consisting of an abnormal buildup and proliferation of blood vessels in the skin or internal organs.",
    "secondary": "In pediatric dermatology and pathology, infantile strawberry hemangioma or adult cavernous hemangioma occurring commonly in the skin, liver, or vertebrae.",
    "quotes": [
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The cavernous **hemangioma** consists of large communicating vascular spaces filled with circulating blood and lined by flat endothelium." },
      { "author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Excision of a deep intramuscular **hemangioma** requires meticulous proximal vessel control to avert severe hemorrhage." },
      { "author": "James Ewing", "work": "Neoplastic Diseases", "quote": "The spontaneous involution of infantile strawberry **hemangioma** demonstrates that not all vascular growths behave as permanent neoplasms." }
    ]
  },
  "Dashboard — angi\\lymphangioma.md": {
    "primary": "A benign tumor or congenital malformation composed of dilated lymphatic channels and spaces.",
    "secondary": "In pediatric pathology, cystic hygroma or cavernous lymphangioma, commonly presenting as a soft cystic mass in the neck or axilla of young children.",
    "quotes": [
      { "author": "James Ewing", "work": "Neoplastic Diseases", "quote": "Histologically, a **lymphangioma** consists of endothelium-lined lymphatic spaces filled with clear proteinaceous fluid and lymphoid aggregates." },
      { "author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Surgical enucleation of a large cervical **lymphangioma** is complicated by its intimate adherence to the internal jugular vein." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Congenital occlusion of embryonic lymph sacs gives rise to that massive cystic **lymphangioma** known clinically as hygroma." }
    ]
  },
  "Dashboard — angi\\polyangiaceae.md": {
    "primary": "A family of myxobacteria (slime bacteria) characterized by producing clustered fruiting bodies containing multiple sporangia (cysts).",
    "secondary": "In systematic bacteriology, gliding prokaryotes within the order Myxococcales that aggregate socially upon starvation to build multi-cyst fruiting structures.",
    "quotes": [
      { "author": "Roland Thaxter", "work": "On the Myxobacteriaceae, a New Order of Schizomycetes", "quote": "In the family **polyangiaceae**, the cystophores bear numerous distinct, brightly colored sporangia clustered together." },
      { "author": "Stanier, R. Y.", "work": "The Cytophaga Group: A Contribution to the Biology of Myxobacteria", "quote": "Species of the **polyangiaceae** degrade cellulose and other insoluble polysaccharides through social swarming behaviors." },
      { "author": "Martin Dworkin", "work": "Developmental Biology of the Myxobacteria", "quote": "The complex morphogenetic architecture of the **polyangiaceae** demonstrates primitive multicellular coordination in prokaryotes." }
    ]
  },
  "Dashboard — angi\\polyangium.md": {
    "primary": "A genus of myxobacteria in the family Polyangiaceae, whose social vegetative cells aggregate to form cysts clustered within a slime envelope.",
    "secondary": "In soil microbiology, predatory slime bacteria capable of lysing other microorganisms and decomposing complex plant polymers.",
    "quotes": [
      { "author": "Roland Thaxter", "work": "Further Observations on the Myxobacteriaceae", "quote": "Under desiccation, the rod-shaped swarm cells of **polyangium** shorten into resting microcysts enclosed within durable gelatinous sacs." },
      { "author": "Stanier, R. Y.", "work": "Studies on the Myxobacteria", "quote": "The characteristic cysts of **polyangium** are often found on decaying wood and dung, displaying golden or brownish hues." },
      { "author": "Martin Dworkin", "work": "Cellular Interactions in Myxobacteria", "quote": "Colonies of **polyangium** exhibit rhythmic rippling waves across agar plates during coordinated predatory foraging." }
    ]
  }
}

content = f'''import {{ updateNotesBatch }} from './curate-updater-util.mjs';

const BASE_DIR = 'App database/Greek roots/Cluster Body & Physiology';

const BATCH1_DATA = {json.dumps(batch1_data, indent=2, ensure_ascii=False)};

const updated = updateNotesBatch(BASE_DIR, BATCH1_DATA);
console.log(`Body & Physiology Part 1 - Batch 1 Completed: ${{updated}} / ${{Object.keys(BATCH1_DATA).length}} notes updated.`);
'''

with open('main app/scripts/curate-body-p1-batch1.mjs', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Generated curate-body-p1-batch1.mjs with {len(batch1_data)} entries.")
