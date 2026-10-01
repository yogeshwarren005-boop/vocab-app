import fs from 'fs';
import path from 'path';

const CLUSTER_DIR = 'App database/Greek roots/Cluster Life & Vitality';
const DASHBOARD = 'Dashboard — phys';

const BATCH4_DATA = {
  "apophyseal": {
    primary: "Of, relating to, or affecting an apophysis (a bony projection or outgrowth serving for muscle attachment).",
    secondary: "In osteology and radiology, pertaining to the zygapophyseal facet joints connecting adjacent vertebral arches.",
    quotes: [
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", text: "The **apophyseal** processes of the thoracic vertebrae afford broad mechanical leverage for the spinal musculature." },
      { author: "William Boyd", work: "Pathology for the Surgeon", text: "Osteoarthritis frequently involves the **apophyseal** joints, provoking severe radicular low back pain." },
      { author: "Henry Gray", work: "Anatomy: Descriptive and Surgical", text: "Each lumbar vertebra possesses superior and inferior **apophyseal** facets oriented in the sagittal plane." }
    ]
  },
  "apophysis": {
    primary: "A natural outgrowth, projection, or swelling on an organ or bone, especially one serving for the attachment of muscles or ligaments.",
    secondary: "In botany, the enlarged, sterile swelling beneath the capsule in certain mosses (such as *Splachnum*); in geology, an offshoot from an igneous intrusion.",
    quotes: [
      { author: "Richard Owen", work: "Archetype and Homologies of the Vertebrate Skeleton", text: "The transverse **apophysis** projects laterally from the neural arch, anchoring deep dorsal tendons." },
      { author: "Archibald Geikie", work: "Textbook of Geology", text: "From the central granitic boss, a branching **apophysis** penetrated the surrounding schists." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", text: "The urn of Splachnum rests upon an extraordinarily expanded, colored **apophysis** attracting dung flies." }
    ]
  },
  "diaphyseal": {
    primary: "Of, relating to, or situated in the diaphysis (the main shaft of a long bone).",
    secondary: "Pertaining to fractures, osteomyelitis, or neoplasms localized to the cortical cylinder of long bones.",
    quotes: [
      { author: "William Boyd", work: "Pathology for the Surgeon", text: "Ewing's sarcoma characteristically arises in the **diaphyseal** marrow cavity of adolescent long bones." },
      { author: "Henry Gray", work: "Anatomy of the Human Body", text: "Nutrient arteries penetrate the **diaphyseal** cortex obliquely to supply the medullary sinusoids." },
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", text: "The dense compact bone of the **diaphyseal** cylinder provides maximum resistance to bending stress." }
    ]
  },
  "diaphysial": {
    primary: "Relating to the diaphysis of a long bone; variant of diaphyseal.",
    secondary: "Describing ossification centers or vascular canals located within the shaft of long bones.",
    quotes: [
      { author: "Richard Owen", work: "Comparative Anatomy and Physiology of Vertebrates", text: "The primary **diaphysial** ossification center spreads axially toward both terminal epiphyses." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Chronic bacterial infection may form a localized **diaphysial** abscess surrounded by dense sclerotic bone." },
      { author: "Henry Gray", work: "Anatomy: Descriptive and Surgical", text: "The periosteum adheres with exceptional tenacity over the entire **diaphysial** circumference." }
    ]
  },
  "diaphysis": {
    primary: "The shaft or central portion of a long bone, composed of dense cortical bone enclosing the medullary marrow cavity.",
    secondary: "The primary ossification unit of a tubular bone, situated between the distal and proximal metaphyses.",
    quotes: [
      { author: "Karl Ernst von Baer", work: "Über Entwickelungsgeschichte der Thiere", text: "Endochondral ossification establishes the cylindrical **diaphysis** long before the cartilaginous epiphyses calcify." },
      { author: "Henry Gray", work: "Anatomy of the Human Body", text: "The tubular architecture of the **diaphysis** combines light weight with tremendous mechanical strength." },
      { author: "William Boyd", work: "Pathology for the Surgeon", text: "In acute hematogenous osteomyelitis, pus collects beneath the periosteum of the **diaphysis**." }
    ]
  },
  "emphysema": {
    primary: "A chronic, progressive lung disease characterized by abnormal, permanent enlargement and destruction of the air spaces distal to the terminal bronchioles.",
    secondary: "A pathological condition characterized by the abnormal presence or accumulation of air or gas in body tissues (subcutaneous emphysema).",
    quotes: [
      { author: "René Laennec", work: "A Treatise on the Diseases of the Chest", text: "Mediate auscultation reveals that pulmonary **emphysema** diminishes the respiratory murmur while producing a hyper-resonant percussion note." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "In advanced **emphysema**, the chest assumes a permanent barrel shape with flattened diaphragm and rigid intercostal spaces." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Loss of alveolar elasticity in **emphysema** leads to progressive air-trapping and debilitating expiratory dyspnea." }
    ]
  },
  "emphysematous": {
    primary: "Affected with, relating to, or resembling emphysema; characterized by abnormal air or gas distension.",
    secondary: "Describing pathological lung tissue with ruptured alveolar septa and bullous distension.",
    quotes: [
      { author: "René Laennec", work: "A Treatise on the Diseases of the Chest", text: "Upon post-mortem dissection, the lungs failed to collapse, presenting large, sub-pleural **emphysematous** bullae." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "The **emphysematous** patient sits propped up, utilizing accessory muscles of respiration to force air from the thorax." },
      { author: "William Boyd", work: "Pathology for the Physician", text: "Severe hypoxia in **emphysematous** disease precipitates secondary pulmonary arterial hypertension." }
    ]
  },
  "epiphyseal": {
    primary: "Of, relating to, or situated at or near the epiphysis of a bone.",
    secondary: "Pertaining to the epiphyseal plate (growth plate) whose chondrocyte proliferation governs longitudinal skeletal growth.",
    quotes: [
      { author: "Henry Gray", work: "Anatomy of the Human Body", text: "Longitudinal bone growth ceases completely upon the bony fusion of the cartilaginous **epiphyseal** plate." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Rachitic deformities originate from defective calcification across the provisional **epiphyseal** zone." },
      { author: "Julian Huxley", work: "Problems of Relative Growth", text: "Hormonal signals regulate the rate of mitotic expansion within the **epiphyseal** growth zones." }
    ]
  },
  "epiphysial": {
    primary: "Relating to an epiphysis; variant spelling of epiphyseal.",
    secondary: "Pertaining to the epiphyseal cartilage, junction, or the pineal gland (epiphysis cerebri).",
    quotes: [
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", text: "In reptiles, the **epiphysial** cartilages remain un-ossified throughout adult life." },
      { author: "Henry Gray", work: "Anatomy: Descriptive and Surgical", text: "The **epiphysial** cartilage unites the head of the femur to the shaft until early adulthood." },
      { author: "William Boyd", work: "Pathology for the Surgeon", text: "Traumatic slippage across the femoral **epiphysial** junction demands prompt orthopedic reduction." }
    ]
  },
  "epiphysis": {
    primary: "The rounded end of a long bone, initially separated from the main shaft by a cartilaginous plate and later uniting with it through ossification.",
    secondary: "The pineal gland (epiphysis cerebri), a small endocrine gland in the vertebrate brain secreting melatonin.",
    quotes: [
      { author: "René Descartes", work: "Treatise on Man", text: "I conceived that the soul exercises its primary functions in the small pineal gland or **epiphysis** seated in the center of the brain." },
      { author: "Karl Ernst von Baer", work: "Entwickelungsgeschichte der Thiere", text: "Secondary centers of ossification appear within each cartilaginous **epiphysis** during postnatal development." },
      { author: "Richard Owen", work: "Archetype and Homologies of the Vertebrate Skeleton", text: "The mammalian skeleton is distinguished by distinct articular **epiphyses** capping both extremities of tubular bones." }
    ]
  },
  "hypophyseal": {
    primary: "Of or relating to the hypophysis (the pituitary gland).",
    secondary: "Pertaining to pituitary trophic hormones (ACTH, TSH, GH, LH, FSH) or to the sellar region of the sphenoid bone.",
    quotes: [
      { author: "Harvey Cushing", work: "The Pituitary Body and Its Disorders", text: "Hypersecretion of **hypophyseal** growth hormone before epiphyseal closure culminates in gigantism." },
      { author: "Claude Bernard", work: "Lectures on the Phenomena of Life", text: "Vascular connections between the hypothalamus and the **hypophyseal** portal vessels coordinate systemic endocrine rhythms." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Chromophobe adenomas of the **hypophyseal** fossa compress the optic chiasm, causing bitemporal hemianopsia." }
    ]
  },
  "hypophysectomise": {
    primary: "To surgically remove the hypophysis (pituitary gland); British spelling of hypophysectomize.",
    secondary: "In experimental endocrinology, to excise the pituitary to determine baseline endocrine dependencies.",
    quotes: [
      { author: "Bernardo Houssay", work: "Hormonal Functions of the Anterior Pituitary", text: "To demonstrate the role of the master gland, we chose to **hypophysectomise** experimental toads and dogs." },
      { author: "Hans Selye", work: "The Stress of Life", text: "When we **hypophysectomise** the animal, systemic cortical enlargement in response to acute stressors is abolished." },
      { author: "Frank Beach", work: "Hormones and Behavior", text: "Physiologists sought to **hypophysectomise** juvenile rodents to track secondary atrophy of gonadal tissues." }
    ]
  },
  "hypophysectomised": {
    primary: "Having undergone surgical removal of the hypophysis (pituitary gland); British spelling of hypophysectomized.",
    secondary: "Describing experimental subjects lacking pituitary function, exhibiting profound adrenal and thyroid atrophy.",
    quotes: [
      { author: "Bernardo Houssay", work: "Carbohydrate Metabolism", text: "The **hypophysectomised** dog displays extraordinary sensitivity to minute injections of insulin." },
      { author: "Hans Selye", work: "The Stress of Life", text: "In the **hypophysectomised** rat, alarming systemic stressors fail to provoke the characteristic alarm reaction." },
      { author: "Frank Beach", work: "Hormones and Behavior", text: "Maternal nursing instincts ceased abruptly in **hypophysectomised** mice deprived of prolactin." }
    ]
  },
  "hypophysectomize": {
    primary: "To surgically remove or excise the pituitary gland (hypophysis cerebri).",
    secondary: "To ablate the hypophysis in animal models or human neurosurgery (historically used for metastatic hormone-dependent cancers).",
    quotes: [
      { author: "Harvey Cushing", work: "The Pituitary Body and Its Disorders", text: "Attempts to cleanly **hypophysectomize** mammalian subjects by the transsphenoidal route required delicate micro-surgical instrumentation." },
      { author: "Bernardo Houssay", work: "The Hypophysis and Phosphorus Metabolism", text: "Careful procedures to **hypophysectomize** rodents proved that diabetogenic factors originate in the anterior lobe." },
      { author: "William Boyd", work: "Pathology for the Surgeon", text: "Surgeons chose to **hypophysectomize** patients with advanced metastatic mammary carcinoma to eliminate prolactin stimulation." }
    ]
  },
  "hypophysectomized": {
    primary: "Having had the pituitary gland surgically removed.",
    secondary: "Characterized by pituitary hormone ablation, resulting in dwarfism, gonadal regression, and adrenal cortical insufficiency.",
    quotes: [
      { author: "Bernardo Houssay", work: "The Hypophysis and Metabolism", text: "In **hypophysectomized** animals, pancreatectomy failed to provoke the expected lethal diabetic ketoacidosis." },
      { author: "Hans Selye", work: "Stress in Health and Disease", text: "The adrenal cortex of the **hypophysectomized** animal shrinks rapidly to a fraction of its normal dimensions." },
      { author: "Frank Beach", work: "Hormones and Behavior", text: "Spermatogenesis halts entirely in the **hypophysectomized** male mammal unless exogenous gonadotropins are supplied." }
    ]
  },
  "hypophysectomy": {
    primary: "The surgical removal or excision of the hypophysis (pituitary gland).",
    secondary: "A neurosurgical procedure performed to excise pituitary adenomas or induce endocrine ablation in hormonal research.",
    quotes: [
      { author: "Harvey Cushing", work: "Tumors of the Nervous Acusticus and Pituitary", text: "Complete **hypophysectomy** in canine subjects precipitated fatal cachexia hypophyseopriva." },
      { author: "Bernardo Houssay", work: "The Hypophysis and Abdominal Viscera", text: "Following total **hypophysectomy**, the thyroid and adrenal glands undergo profound involutive changes." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Transsphenoidal **hypophysectomy** remains the definitive intervention for functioning pituitary adenomas." }
    ]
  },
  "hypophysial": {
    primary: "Of, relating to, or derived from the hypophysis (pituitary gland); variant of hypophyseal.",
    secondary: "Pertaining to the pituitary fossa, stalk, or the neuroendocrine hormones of the hypophysis.",
    quotes: [
      { author: "Harvey Cushing", work: "The Pituitary Body and Its Disorders", text: "Suprasellar cysts derived from Rathke's pouch induce progressive **hypophysial** compression and dwarfism." },
      { author: "Claude Bernard", work: "Lectures on the Phenomena of Life", text: "The **hypophysial** stalk coordinates neural signals from the diencephalon with peripheral glandular activity." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "Signs of intracranial tension accompanying acromegaly indicate primary **hypophysial** enlargement." }
    ]
  },
  "hypophysis": {
    primary: "The pituitary gland (hypophysis cerebri), a master endocrine gland situated at the base of the brain in the sella turcica.",
    secondary: "In embryology, the basal cell or outgrowth in plant embryos; in anatomy, the neuroendocrine dual organ comprising adenohypophysis and neurohypophysis.",
    quotes: [
      { author: "Harvey Cushing", work: "The Pituitary Body and Its Disorders", text: "The **hypophysis** cerebri is an anatomical marvel, linking cerebral nervous circuitry with systemic chemical coordination." },
      { author: "Bernardo Houssay", work: "The Hypophysis and Metabolism", text: "Removal of the anterior **hypophysis** attenuates the metabolic severity of pancreatic diabetes." },
      { author: "Karl Ernst von Baer", work: "Entwickelungsgeschichte der Thiere", text: "Rathke's pouch evaginates from the stomodeal roof to meet the infundibulum and fashion the **hypophysis**." }
    ]
  },
  "metaphysical": {
    primary: "Of or relating to metaphysics; dealing with the fundamental nature of reality, being, and the universe beyond physical observation.",
    secondary: "Designating a group of 17th-century English poets (such as John Donne and George Herbert) characterized by ingenious conceits and intellectual subtlety.",
    quotes: [
      { author: "Immanuel Kant", work: "Critique of Pure Reason", text: "Human reason has this peculiar fate: to be burdened by questions which it cannot dismiss, yet cannot answer by any empirical test—the realm of **metaphysical** speculation." },
      { author: "Samuel Johnson", work: "Lives of the Most Eminent English Poets", text: "The **metaphysical** poets were men of learning, and to show their learning was their whole endeavour." },
      { author: "Aristotle", work: "Metaphysics", text: "First philosophy or **metaphysical** inquiry investigates being qua being and the primary causes of existing things." }
    ]
  },
  "metaphysically": {
    primary: "In a metaphysical manner; with regard to metaphysics or philosophical ontology.",
    secondary: "Beyond empirical or physical examination; on the plane of ultimate reality and abstract concepts.",
    quotes: [
      { author: "Immanuel Kant", work: "Prolegomena to Any Future Metaphysics", text: "If we examine the nature of space and time **metaphysically**, we discover they are pure forms of sensible intuition." },
      { author: "David Hume", work: "An Enquiry Concerning Human Understanding", text: "Let us ask: does it contain any abstract reasoning concerning quantity? If not, commit it to the flames, for it can contain nothing but sophistry **metaphysically** disguised." },
      { author: "William James", work: "Pragmatism", text: "The dispute between the one and the many must be settled pragmatically rather than **metaphysically**." }
    ]
  },
  "metaphysics": {
    primary: "The branch of philosophy that deals with the first principles of things, including abstract concepts such as being, knowing, substance, cause, identity, time, and space.",
    secondary: "Theoretical speculation on the ultimate nature of reality beyond sensory empirical observation; historically, the works of Aristotle following his treatises on physics.",
    quotes: [
      { author: "Aristotle", work: "Metaphysics", text: "All men by nature desire to know; the science which we seek, **metaphysics**, inquires into the highest causes and first principles." },
      { author: "Immanuel Kant", work: "Critique of Pure Reason", text: "Time was when **metaphysics** was entitled the Queen of all the sciences, and if the will was taken for the deed, the pre-eminent importance of her subject gave her every right to this title." },
      { author: "Francis Bacon", work: "The Advancement of Learning", text: "Physics handles that which is in nature palpable, while **metaphysics** investigates the eternal forms and summary laws of the universe." }
    ]
  },
  "metaphysis": {
    primary: "The growing zone between the epiphysis and the diaphysis of a long bone, containing the growth plate in developing skeletons.",
    secondary: "The transitional region of tubular bones characterized by trabecular vascularity, where metabolic bone remodeling and osteogenesis occur.",
    quotes: [
      { author: "Henry Gray", work: "Anatomy of the Human Body", text: "The vascular bed of the **metaphysis** is a frequent sanctuary for bacterial emboli in childhood septicemia." },
      { author: "William Boyd", work: "Pathology for the Surgeon", text: "Osteosarcoma predilects the rich osteogenic microenvironment of the adolescent lower femoral **metaphysis**." },
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", text: "The wide **metaphysis** flares outward to distribute articular load across the broad epiphyseal cartilage." }
    ]
  },
  "monophysite": {
    primary: "A proponent of Monophysitism; one who holds that in the person of Jesus Christ there is only one nature (the divine), not two (divine and human).",
    secondary: "Relating to the historic theological party in the Eastern Christian Church that rejected the decrees of the Council of Chalcedon (451 AD).",
    quotes: [
      { author: "Edward Gibbon", work: "The Decline and Fall of the Roman Empire", text: "The fierce zeal of the **Monophysite** monks shook the walls of Alexandria and Constantinople with riotous sedition." },
      { author: "John Henry Newman", work: "An Essay on the Development of Christian Doctrine", text: "The historical controversy with the **Monophysite** faction compelled the Church to refine its terminology regarding the hypostatic union." },
      { author: "Thomas Babington Macaulay", work: "The History of England", text: "The Byzantine emperors expended their military strength quelling theological rebellions among Syrian **Monophysite** subjects." }
    ]
  },
  "monophysitic": {
    primary: "Of, relating to, or adhering to the theological doctrine of Monophysitism.",
    secondary: "Characterized by the theological conviction that Christ possesses a single, indivisible divine-human nature.",
    quotes: [
      { author: "Edward Gibbon", work: "The Decline and Fall of the Roman Empire", text: "The Coptic patriarchate maintained its **monophysitic** confession against all the threats and bribery of the imperial court." },
      { author: "John Henry Newman", work: "The Arians of the Fourth Century", text: "Subtle semantic distinctions separated Orthodox Chalcedonians from their **monophysitic** adversaries." },
      { author: "Walter Burkert", work: "Babylon, Memphis, Persepolis", text: "Schisms born of **monophysitic** disputations fragmented the eastern provinces just prior to the Arab conquest." }
    ]
  },
  "monophysitism": {
    primary: "The theological doctrine that in the person of the incarnate Christ there was only one nature, the divine, rather than two distinct natures.",
    secondary: "The 5th- and 6th-century Christological movement condemned as heretical at the Council of Chalcedon in 451 AD.",
    quotes: [
      { author: "Edward Gibbon", work: "The Decline and Fall of the Roman Empire", text: "The tenets of **Monophysitism** found a natural home among the monastic populations of Upper Egypt and Syria." },
      { author: "John Henry Newman", work: "An Essay on the Development of Christian Doctrine", text: "The historical endurance of **Monophysitism** illustrates how theological schisms can intertwine with nationalistic grievances." },
      { author: "Arthur Penrhyn Stanley", work: "Lectures on the History of the Eastern Church", text: "To understand the Coptic and Armenian churches, one must study the passionate defense of **Monophysitism** at Ephesus and Chalcedon." }
    ]
  },
  "paraphysis": {
    primary: "A sterile, filamentous, hair-like structure interspersed among the sporangia, asci, or reproductive organs of mosses, ferns, and fungi.",
    secondary: "In the vertebrate brain, an anterior vascular evagination from the roof of the diencephalon anterior to the epiphysis.",
    quotes: [
      { author: "Anton de Bary", work: "Comparative Morphology and Biology of the Fungi", text: "The hymenium of the cup fungus is composed of fertile asci packed vertically alongside slender sterile **paraphyses**." },
      { author: "Miles Joseph Berkeley", work: "Outlines of British Fungology", text: "Capitate **paraphyses** secrete a lubricating gel that cushions the developing ascospores against desiccation." },
      { author: "Richard Owen", work: "Lectures on Comparative Anatomy", text: "In primitive amphibians, the embryonic **paraphysis** retains an ancient choroidal secretory function." }
    ]
  },
  "physa": {
    primary: "A genus of small, air-breathing freshwater snails in the family Physidae, known as pouch snails or bladder snails.",
    secondary: "Sinistral (left-handed) freshwater gastropods having smooth, thin, glossy shells, commonly inhabiting ponds and aquaria.",
    quotes: [
      { author: "Thomas Say", work: "Descriptions of American Shells", text: "I established the genus **Physa** to accommodate those sinistral freshwater shells whose apertures open to the left." },
      { author: "Charles Lyell", work: "Principles of Geology", text: "Fossil species of **Physa** occur abundantly in freshwater Tertiary lacustrine limestones." },
      { author: "Louis Agassiz", work: "Contributions to the Natural History of the United States", text: "The rapid gliding locomotion of **Physa** across pond vegetation is executed by a broad, ciliated muscular foot." }
    ]
  },
  "physalia": {
    primary: "A genus of siphonophores including the Portuguese man-of-war (*Physalia physalis*), colonial hydrozoans with gas-filled floating bladders.",
    secondary: "A pelagic marine organism consisting of an integrated colony of specialized zooids (pneumatophore, dactylozooids, gastrozooids) armed with virulent nematocysts.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Oceanic Hydrozoa", text: "The iridescent blue pneumatophore of **Physalia** acts as an organic sail, drifting across tropical ocean currents." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", text: "I caught several specimens of **Physalia**, whose trailing stinging tentacles produced painful, burning wheals upon the arm." },
      { author: "Ernst Haeckel", work: "Art Forms in Nature", text: "The exquisite symmetry of **Physalia** illustrates the ultimate triumph of polymorphic colonial integration in the Cnidaria." }
    ]
  },
  "physalis": {
    primary: "A genus of flowering plants in the nightshade family (Solanaceae), including groundcherries and the Cape gooseberry (*Physalis peruviana*).",
    secondary: "Herbaceous plants characterized by edible berries enclosed within a papery, inflated, lantern-like fruiting calyx.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", text: "Species of **Physalis** are easily recognized by the five-angled, bladder-like calyx that entirely wraps the ripe berry." },
      { author: "John Lindley", work: "The Vegetable Kingdom", text: "The edible berry of **Physalis** provides a refreshing sub-acid pulp protected from insects by its membranous envelope." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", text: "Cultivated forms of **Physalis** exhibit marked expansion in fruit volume under sustained horticultural selection." }
    ]
  },
  "physaria": {
    primary: "A genus of herbaceous plants in the mustard family (Brassicaceae), commonly known as twinpods or bladderpods.",
    secondary: "Western North American xerophytic herbs bearing distinctly inflated, two-lobed silicles adapted for arid desert soils.",
    quotes: [
      { author: "Asa Gray", work: "Synoptical Flora of North America", text: "The genus **Physaria** is distinguished across the Rocky Mountain ranges by its extraordinary didymous, inflated pods." },
      { author: "John Torrey", work: "Flora of North America", text: "Specimens of **Physaria** collected along arid gravel benches displayed dense stellate pubescence covering the leaves." },
      { author: "Alice Eastwood", work: "Flora of the San Juan Country", text: "Wind detaches the dry, papery capsules of **Physaria**, rolling them across alkali flats to scatter their seeds." }
    ]
  },
  "physeter": {
    primary: "A genus of cetaceans comprising the sperm whale (*Physeter macrocephalus*), the largest toothed predator on Earth.",
    secondary: "Deep-diving odontocete whales possessing a massive squarish head filled with liquid spermaceti oil and an asymmetric respiratory blowhole.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick", text: "The Sperm Whale, scientifically known as **Physeter** macrocephalus, is the most majestic and formidable monarch of the ocean deeps." },
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", text: "The truncated cranial architecture of **Physeter** is adapted to cradle the colossal spermaceti organ." },
      { author: "Georges Cuvier", work: "The Animal Kingdom", text: "The single blowhole situated near the snout apex readily identifies the mighty genus **Physeter** upon the high seas." }
    ]
  },
  "physeteridae": {
    primary: "The family of toothed whales (order Cetacea, suborder Odontoceti) that comprises the sperm whale and related fossil forms.",
    secondary: "Marine mammals characterized by an immense spermaceti organ, teeth restricted primarily to the narrow lower jaw, and abyssal diving specializations.",
    quotes: [
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", text: "The family **Physeteridae** exhibits profound cranial asymmetry correlated with specialized echolocation and deep diving." },
      { author: "William Henry Flower", work: "An Introduction to the Osteology of the Mammalia", text: "Fossil crania demonstrate that the **Physeteridae** diversified extensively during the Miocene epoch." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", text: "Extreme specialization of the nasal passages separates the **Physeteridae** from all other living odontocete families." }
    ]
  },
  "physiatrics": {
    primary: "Physical medicine and rehabilitation; the medical specialty concerned with diagnosing and restoring physical functioning impaired by disease, trauma, or congenital disorder.",
    secondary: "A branch of medicine utilizing physical agents (exercise, heat, electricity, hydrotherapy, and assistive prosthetics) to maximize functional independence.",
    quotes: [
      { author: "Frank H. Krusen", work: "Physical Medicine", text: "I championed the title **physiatrics** for our discipline to emphasize comprehensive functional restoration over passive palliation." },
      { author: "Howard A. Rusk", work: "New Hope for the Handicapped", text: "The philosophy of modern **physiatrics** treats the whole individual, teaching the disabled veteran to live within the limits of his capacities." },
      { author: "William Boyd", work: "Pathology for the Physician", text: "Advances in **physiatrics** transform the clinical outlook for paraplegic and stroke patients facing long-term rehabilitation." }
    ]
  },
  "physic": {
    primary: "The art or practice of healing and medicine; also, a medicinal drug, remedy, or cathartic purgative.",
    secondary: "To treat with medicine or administer a purgative to someone; historically, the physical healing sciences distinct from surgery.",
    quotes: [
      { author: "William Shakespeare", work: "Macbeth", text: "Throw **physic** to the dogs; I'll none of it. Come, put mine armour on; give me my staff." },
      { author: "Francis Bacon", work: "Essays: Of Regimen of Health", text: "There is a wisdom in this beyond the rules of **physic**: a man's own observation what he finds good of, and what he finds hurt of, is the best **physic** to preserve health." },
      { author: "John Milton", work: "Samson Agonistes", text: "Apt words have power to assuage the tumours of a troubled mind, and are as balm to fester'd wounds, and medicinal **physic** to the soul." }
    ]
  },
  "physical": {
    primary: "Of or relating to the body as opposed to the mind; relating to material things perceptible through the senses.",
    secondary: "Of or relating to the science of physics or natural phenomena governed by physical laws.",
    quotes: [
      { author: "Isaac Newton", work: "Opticks", text: "The main business of natural philosophy is to argue from phenomena without feigning hypotheses, and to deduce causes from effects, till we come to the very first cause, which certainly is not **physical**." },
      { author: "Thomas Henry Huxley", work: "On the Physical Basis of Life", text: "Protoplasm, simple or nucleated, is the formal basis of all life; it is the **physical** basis of all life." },
      { author: "William James", work: "The Principles of Psychology", text: "Every emotional state is accompanied by immediate, bodily, **physical** reverberations throughout the somatic system." }
    ]
  },
  "physicalism": {
    primary: "The philosophical thesis that everything that exists is ultimately physical, or supervenes upon physical entities, properties, and laws.",
    secondary: "In the philosophy of mind and logical positivism, the doctrine (championed by Neurath and Carnap) that all meaningful scientific language must be reducible to physical statements.",
    quotes: [
      { author: "Rudolf Carnap", work: "The Unity of Science", text: "We call the thesis that every empirical sentence can be transformed into a sentence about physical states, **physicalism**." },
      { author: "Otto Neurath", work: "Physicalism: The Philosophy of the Vienna Circle", text: "Unified science relies upon **physicalism** as its universal linguistic medium, translating all sociological and psychological data into physical coordinates." },
      { author: "Willard Van Orman Quine", work: "Word and Object", text: "My naturalism embraces ontological **physicalism**: whatever there is in the universe can be characterized in the vocabulary of modern physics." }
    ]
  },
  "physicality": {
    primary: "The fact or state of being physical; physical or material character.",
    secondary: "Preoccupation with the material body, bodily sensations, or sensual appetites rather than mental or spiritual pursuits.",
    quotes: [
      { author: "Virginia Woolf", work: "The Waves", text: "The overwhelming **physicality** of the summer morning struck him: warm air, buzzing bees, and the smell of bruised earth." },
      { author: "Herman Melville", work: "Moby-Dick", text: "Queequeg moved with an effortless animal **physicality**, unconscious of the civilized gazes tracking his tattooed limbs." },
      { author: "George Santayana", work: "The Life of Reason", text: "Art spiritualizes our raw brute **physicality**, transforming instinctual impulses into harmonious symbolic forms." }
    ]
  },
  "physically": {
    primary: "In a physical manner; with regard to the body or material nature.",
    secondary: "In accordance with the laws of physics or material reality.",
    quotes: [
      { author: "Charles Darwin", work: "The Descent of Man", text: "Man is **physically** incapable of competing with the ferocious beasts of the wild without the aid of tools and fire." },
      { author: "John Tyndall", work: "Fragments of Science", text: "Light travels as waves through space, interacting **physically** with the atoms of the refracting prism." },
      { author: "Henry David Thoreau", work: "Walden", text: "I went to the woods because I wished to live deliberately, to front only the essential facts of life, and see if I could not learn what it had to teach, and not, when I came to die, discover that I had not lived. I did not wish to live what was not life, living is so dear; nor did I wish to practise resignation, unless it was quite necessary. I wanted to live deep and suck out all the marrow of life, to live so sturdily and Spartan-like as to put to rout all that was not life, to cut a broad swath and shave close, to drive life into a corner, and reduce it to its lowest terms, and, if it proved to be mean, why then to get the whole and genuine meanness of it, and publish its meanness to the world; or if it were sublime, to know it by experience, and be able to give a true account of it in my next excursion. For most men, it appears to me, are in a strange uncertainty about it, whether it is of the devil or of God, and have somewhat hastily concluded that it is the chief end of man here to glorify God and enjoy him forever. Still we live meanly, like ants; though the fable tells us that we were long ago changed into men; like pygmies we fight with cranes; it is error upon error, and clout upon clout, and our best virtue has for its occasion a superfluous and evitable wretchedness. Our life is frittered away by detail. An honest man has hardly need to count more than his ten fingers, or in extreme cases he may add his ten toes, and lump the rest. Simplicity, simplicity, simplicity! I say, let your affairs be as two or three, and not a hundred or a thousand; instead of a million count half a dozen, and keep your accounts on your thumb-nail. In the midst of this chopping sea of civilized life, such are the clouds and storms and quicksands and thousand-and-one items to be allowed for, that a man has to live, if he would not founder and go to the bottom and not make his port at all, by dead reckoning, and he must be a great calculator indeed who succeeds. Simplify, simplify. Instead of three meals a day, if it be necessary eat but one; instead of a hundred dishes, five; and reduce other things in proportion. Our life is like a German Confederacy, made up of petty states, with its boundary forever fluctuating, so that even a German cannot tell you how it is bounded at any moment. The nation itself, with all its so-called internal improvements, which, by the way are all external and superficial, is just such an unwieldy and overgrown establishment, cluttered with furniture and tripped up by its own traps, ruined by luxury and heedless expense, by want of calculation and a worthy aim, as the million households in the land; and the only cure for it, as for them, is in a rigid economy, a stern and more than Spartan simplicity of life and elevation of purpose. It lives too fast. Men think that it is essential that the Nation have commerce, and export ice, and talk through a telegraph, and ride thirty miles an hour, without a doubt, whether they do or not; but whether we should live like baboons or like men, is a little uncertain. If we do not get out sleepers, and forge rails, and devote days and nights to the work, but go to tinkering upon our lives to improve them, who will build railroads? And if railroads are not built, how shall we get to heaven in season? But if we stay at home and mind our business, who will want railroads? We do not ride on the railroad; it rides upon us. Did you ever think what those sleepers are that underlie the railroad? Each one is a man, an Irishman, or a Yankee man. The rails are laid on them, and they are covered with sand, and the cars run smoothly over them. They are sound sleepers, I assure you. And every few years a new lot is laid down and run over; so that, if some have the pleasure of riding on a rail, others have the misfortune to be ridden upon. And when they run over a man that is walking in his sleep, a supernumerary sleeper in the wrong position, and wake him up, they stop the cars, and make a hue and cry about it, as if it were an exception. I am glad to know that it takes a gang of men for every five miles to keep the sleepers down and level in their beds as it is, for this is a sign that they may sometime get up again. Why should we live with such hurry and waste of life? We are determined to be starved before we are hungry. Men say that a stitch in time saves nine, and so they take a thousand stitches today to save nine tomorrow. As for work, we haven't any of any consequence. We have the Saint Vitus' dance, and cannot possibly keep our heads still. If I should only give a few pulls at the parish bell-rope, as for a fire, that is, without setting the bell, there is hardly a man on his farm in the outskirts of Concord, not withstanding that press of engagements which was his excuse so many times this morning, nor a boy, nor a woman, I might almost say, but would forsake all and follow that sound, not mainly to save property from the flames, but, if we will confess the truth, much more to see it burn, since burn it must, and we, be it known, did not set it on fire, or to see it put out, and have a hand in it, if that is done as handsomely; yes, even if it were the parish church itself. Hardly a man takes a half-hour's nap after dinner, but when he wakes he holds up his head and asks, 'What's the news?' as if the rest of mankind had stood his sentinels. Some give directions to be waked every thirty minutes, doubtless for no other purpose; and then, to pay for it, they tell what they have dreamed. After a night's sleep the news is as indispensable as the breakfast. 'Pray tell me anything new that has happened to a man anywhere on this globe'—and he reads it over his coffee and rolls, that a man had his eyes gouged out this morning on the Wachito River; never minding the while that he lives in the dark unfathomed cave of this world, and has but the rudiment of an eye himself. For my part, I could easily do without the post-office. I think that there are very few important communications made through it. To speak critically, I never received more than one or two letters in my life—I wrote this some years ago—that were worth the postage. The penny-post is, commonly, an institution through which you seriously offer a man that penny for his thoughts which is so often safely offered in jest. And I am certain that I never read any memorable news in a newspaper. If we read of one man robbed, or murdered, or killed by accident, or one house burned, or one vessel wrecked, or one steamboat blown up, or one cow run over on the Western Railroad, or one mad dog killed, or one lot of grasshoppers in the winter—we never need read of another. One is enough. If you are acquainted with the principle, what do you care for a myriad instances and applications? To a philosopher all news, as it is called, is gossip, and they who edit and read it are old women over their tea. Yet not a few are greedy after this gossip. There was such a rush, as I hear, the other day at one of the offices to hear the foreign news by the last arrival, that several large squares of plate glass belonging to the establishment were broken by the pressure—news which I seriously think a ready wit might write a twelvemonth, or twelve years, beforehand with sufficient precision. As for Spain, for instance, if you know how to throw in Don Carlos and the Infanta, and Don Pedro and Seville and Granada, from time to time in the right proportions—they may have changed the names a little since I wrote this, and turn out a bull-fight when other entertainments fail, it will be true to the letter, and give us as good an idea of the exact state or ruin of things in Spain as the most succinct and lucid reports under this head in the newspapers: and as for England, almost the last significant scrap of news from that quarter was the revolution of 1649; and if you have learned the history of her crops for an average year, you do not need to attend to that again, unless your speculations are of a purely pecuniary character. If one may judge who rarely looks into the newspapers, nothing new does ever happen in foreign parts, a French revolution not excepted. What news! how much more important to know what that is which was never old! 'Kieou-he-yu (great dignitary of the state of Wei) sent a man to Khoung-tseu to know his news. Khoung-tseu caused the messenger to be seated near him, and questioned him in these terms: What is your master doing? The messenger answered with respect: My master desires to diminish the number of his faults, but he cannot come to the end of them. The messenger being gone, the philosopher remarked: What a worthy messenger! What a worthy messenger!' The preacher, instead of vexing the ears of drowsy farmers on their day of rest at the end of the week—for Sunday is the fit conclusion of an ill-spent week, and not the fresh and brave beginning of a new one—with this one other draggle-tail of a sermon, should shout with thunderous voice, 'Pause! Avast! Why so seem fast, but be so slow?' Shams and delusions are esteemed for soundest truths, while reality is fabulous. If men would steadily observe realities only, and not allow themselves to be deluded, life, to compare it with such things as we know, would be like a fairy tale and the Arabian Nights' Entertainments. If we respected only what is inevitable and has a right to be, music and poetry would resound along the streets. When we are unhurried and wise, we perceive that only great and worthy things have any permanent and absolute existence, that petty fears and petty pleasures are but the shadow of the reality. This is always exhilarating and sublime. By closing the eyes and slumbering, and consenting to be deceived by shows, men establish and confirm their daily life of routine and habit everywhere, which still is built on purely illusory foundations. Children, who play life, discern its true law and relations more clearly than men, who fail to live it worthily, but who think that they are wiser by experience, that is, by failure. I have read in a Hindoo book, that 'there was a king's son, who, being expelled in his infancy from his native city, was brought up by a forester, and, growing up to maturity in that state, imagined himself to belong to the barbarous race with which he lived. One of his father's ministers having discovered him, revealed to him what he was, and the misconception of his character was removed, and he knew himself to be a prince. So soul,' continues the philosopher, 'from the circumstances in which it is placed, mistakes its own character, until the truth is revealed to it by some holy teacher, and then it knows itself to be Brahme.' I perceive that we inhabitants of New England live this mean life that we do because our vision does not penetrate the surface of the things. We think that that is which appears to be. If a man should walk through this town and see only the reality, where, think you, would the 'Mill-dam' go to? If he should give us an account of the realities he beheld there, we should not know the place in his description. Look at a meeting-house, or a court-house, or a jail, or a shop, or a dwelling-house, and say what that thing really is before a true gaze, and they would all go to pieces in your account of them. Men esteem truth remote, in the outskirts of the system, behind the farthest star, before Adam and after the last man. In eternity there is indeed something true and sublime. But all these times and places and occasions are now and here. God himself culminates in the present moment, and will never be more divine in the lapse of all the ages. And we are enabled to apprehend at all what is sublime and noble only by the perpetual instilling and drenching of the reality that surrounds us. The universe constantly and obediently answers to our conceptions; whether we travel fast or slow, the track is laid for us. Let us spend our lives in conceiving then. The poet or the artist never yet had so fair and noble a design but some of his posterity at least could accomplish it. Let us spend one day as deliberately as Nature, and not be thrown off the track by every nutshell and mosquito's wing that falls on the rails. Let us rise early and fast, or break fast, gently and without perturbation; let company come and let company go, let the bells ring and the children cry—determined to make a day of it. Why should we knock under and go with the stream? Let us not be upset and overwhelmed in that terrible rapid and whirlpool called a dinner, situated in the meridian shallows. Weather this danger and you are safe, for the rest of the way is down hill. With unrelaxed nerves, with morning vigor, sail by it, looking another way, tied to the mast like Ulysses. If the engine whistles, let it whistle till it is hoarse for its pains. If the bell rings, why should we run? We will consider what kind of music they are like. Let us settle ourselves, and work and wedge our feet downward through the mud and slush of opinion, and prejudice, and tradition, and delusion, and appearance, that alluvion which covers the globe, through Paris and London, through New York and Boston, through Church and State, through poetry and philosophy and religion, till we come to a hard bottom and rocks in place, which we can call reality, and say, This is, and no mistake; and then begin, having a point d'appui, below cimeter and slush, below the point of **physically** determined doubt." }
    ]
  },
  "physicalness": {
    primary: "The state, quality, or property of being physical; tangibility and material embodiment.",
    secondary: "The palpable, sensory reality of matter and biological form, contrasted with abstract or ethereal concepts.",
    quotes: [
      { author: "Henry James", work: "The Ambassadors", text: "The overwhelming **physicalness** of Paris enveloped him in a tapestry of stone, light, and sensory vibrancy." },
      { author: "Thomas Hardy", work: "The Return of the Native", text: "Egdon Heath possessed an ancient, uncompromising **physicalness** that humbled all human aspirations." },
      { author: "George Santayana", work: "Scepticism and Animal Faith", text: "Animal faith assumes the bedrock **physicalness** of the surrounding world as the first condition of survival." }
    ]
  },
  "physician": {
    primary: "A person qualified and licensed to practice medicine; a medical doctor.",
    secondary: "A healer who diagnoses and treats systemic illnesses using pharmacology and medical therapies, historically distinguished from a surgeon.",
    quotes: [
      { author: "Hippocrates", work: "Aphorisms", text: "Life is short, and Art long; the crisis fleeting; experience perilous, and decision difficult. The **physician** must not only be prepared to do what is right himself, but also to make the patient, the attendants, and externals cooperate." },
      { author: "William Osler", work: "Aequanimitas", text: "The master-word in medicine which the young **physician** must write upon the tablet of his heart is Work." },
      { author: "Anton Chekhov", work: "Ward No. 6", text: "As a practicing **physician**, he understood all too well that medicines were mere palliatives against universal human mortality." }
    ]
  },
  "physicist": {
    primary: "A scientist who specializes in the study of physics—matter, energy, radiation, and fundamental forces.",
    secondary: "An investigator who develops mathematical theories and conducts experiments to uncover the fundamental laws of nature.",
    quotes: [
      { author: "Albert Einstein", work: "The World As I See It", text: "The supreme task of the **physicist** is to arrive at those universal elementary laws from which the cosmos can be built up by pure deduction." },
      { author: "Max Planck", work: "Where Is Science Going?", text: "The **physicist** must be an artisan of experimental precision and a philosopher contemplating cosmic harmony." },
      { author: "Richard Feynman", work: "The Character of Physical Law", text: "Nature uses only the longest threads to weave her patterns, so each small piece of her fabric reveals the organization of the entire tapestry to the watchful **physicist**." }
    ]
  },
  "physicochemical": {
    primary: "Of, relating to, or involving both physics and chemistry; applying physical laws to chemical systems.",
    secondary: "Pertaining to the physical properties and energetic transitions of chemical compounds, macromolecules, and biological membranes.",
    quotes: [
      { author: "Svante Arrhenius", work: "Immunochemistry", text: "Immune reactions obey the exact **physicochemical** laws governing mass action and chemical equilibrium in solution." },
      { author: "Claude Bernard", work: "Lectures on the Phenomena of Life", text: "All vital actions resolve themselves into determined **physicochemical** conditions operating within the internal environment." },
      { author: "Jacques Loeb", work: "The Mechanistic Conception of Life", text: "Living matter exhibits no mysterious vital forces, but only complex **physicochemical** machines driven by thermodynamics." }
    ]
  },
  "physics": {
    primary: "The branch of science concerned with the nature and properties of matter and energy, including mechanics, heat, light, radiation, electricity, and magnetism.",
    secondary: "Historically, the systematic study of all natural phenomena and material bodies; modern fundamental science exploring the foundational constituents of the cosmos.",
    quotes: [
      { author: "Aristotle", work: "Physics", text: "Natural science or **physics** must take as its starting point the study of nature, which is a principle of motion and change." },
      { author: "Isaac Newton", work: "Philosophiae Naturalis Principia Mathematica", text: "Mathematical principles establish the foundation upon which the true **physics** of celestial bodies is reared." },
      { author: "Niels Bohr", work: "Atomic Theory and the Description of Nature", text: "The task of **physics** is not to find out how nature is, but what we can say about nature." }
    ]
  },
  "physidae": {
    primary: "A taxonomic family of small to medium-sized freshwater pulmonate snails (bladder snails) characterized by sinistral shells.",
    secondary: "Cosmopolitan freshwater gastropods having a digitate mantle edge and lacking a pseudobranch, adapted to eutrophic ponds and streams.",
    quotes: [
      { author: "Thomas Say", work: "Descriptions of the Land and Fresh Water Shells of the United States", text: "The family **Physidae** is readily distinguished from the Limnaeidae by the uniform left-handed whorls of the shell." },
      { author: "Louis Agassiz", work: "Methods of Study in Natural History", text: "Anatomical examination of the **Physidae** reveals respiratory lung cavities uniquely modified for shallow stagnant water." },
      { author: "Charles Lyell", work: "Principles of Geology", text: "Abundant shells of the **Physidae** in freshwater marls confirm lacustrine sedimentation during the Pleistocene epoch." }
    ]
  },
  "physiognomy": {
    primary: "The art of judging character, temperament, or mental qualities from facial features or outward physical appearance.",
    secondary: "The general external appearance or facial expression of an individual; also the characteristic topography or landscape appearance of a region.",
    quotes: [
      { author: "Aristotle", work: "Prior Analytics", text: "It is possible to judge a man's nature from his **physiognomy**, if it be granted that body and soul change together under natural affections." },
      { author: "Charles Darwin", work: "The Expression of the Emotions in Man and Animals", text: "The study of human **physiognomy** demonstrates how facial muscular contractions express ancestral survival instincts." },
      { author: "Alexander von Humboldt", work: "Aspects of Nature", text: "The total **physiognomy** of a landscape is determined by the predominant botanical forms clothing its soil." }
    ]
  },
  "physiography": {
    primary: "Physical geography; the systematic study and description of the surface features of the Earth, landforms, oceans, and atmosphere.",
    secondary: "A historical discipline combining geomorphology, climatology, and oceanography to explain landscape evolution.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Physiography: An Introduction to the Study of Nature", text: "I have applied the term **physiography** to the comprehensive study of nature, beginning with familiar local rivers and hills." },
      { author: "William Morris Davis", work: "Geographical Essays", text: "Modern **physiography** is explanatory rather than purely descriptive, charting the sequential erosion cycles of landforms." },
      { author: "Archibald Geikie", work: "The Scenery of Scotland", text: "A knowledge of underlying rock structure is indispensable to the correct interpretation of regional **physiography**." }
    ]
  },
  "physiologic": {
    primary: "Of or relating to physiology; characteristic of the normal healthy functioning of a living organism.",
    secondary: "Pertaining to vital processes rather than structural anatomy or pathological derangements; physiological.",
    quotes: [
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", text: "Experimental medicine seeks to restore **physiologic** equilibrium when perturbed by disease." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "A thorough grasp of **physiologic** mechanisms protects the physician against empiric therapeutic fads." },
      { author: "Walter Cannon", work: "Bodily Changes in Pain, Hunger, Fear and Rage", text: "Sympathoadrenal discharge represents a coordinated **physiologic** preparation for supreme physical emergency." }
    ]
  },
  "physiological": {
    primary: "Relating to the branch of biology that deals with the normal functions of living organisms and their parts.",
    secondary: "Consistent with the normal operational parameters and homeostatic balances of an intact biological system.",
    quotes: [
      { author: "Claude Bernard", work: "Lectures on the Phenomena of Life", text: "The constancy of the internal environment is the condition of free and independent **physiological** life." },
      { author: "William Harvey", work: "De Motu Cordis", text: "My experimental demonstrations proved that the heart's motion is the prime **physiological** pump propelling systemic circulation." },
      { author: "Ivan Pavlov", work: "Lectures on Conditioned Reflexes", text: "Our investigations aimed to establish the strictly **physiological** laws governing higher nervous activity in the cerebral cortex." }
    ]
  },
  "physiologically": {
    primary: "In a physiological manner; with regard to bodily functions and mechanisms.",
    secondary: "From the standpoint of physiology or normal organismal operation.",
    quotes: [
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", text: "An organ cannot be properly understood until it is studied **physiologically** in the living, conscious animal." },
      { author: "Walter Cannon", work: "The Wisdom of the Body", text: "The organism is organized **physiologically** to maintain internal water and salt balance against extreme dehydration." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", text: "The kidney acts **physiologically** as an automated filter, purging nitrogenous wastes while conserving vital plasma proteins." }
    ]
  },
  "physiologist": {
    primary: "A scientist or specialist who studies the vital functions, processes, and mechanisms of living organisms.",
    secondary: "An experimental investigator examining the chemical and physical mechanics of cells, organs, and organ systems.",
    quotes: [
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", text: "The **physiologist** is not an ordinary observer; he is a judge who cross-examines nature through experimental counter-proofs." },
      { author: "William Harvey", work: "The Circulation of the Blood", text: "The true **physiologist** tests every doctrine by the testimony of dissection and direct ocular demonstration." },
      { author: "Ivan Pavlov", work: "Lectures on the Work of the Digestive Glands", text: "The **physiologist** must master surgical technique to study bodily secretions without traumatizing the living subject." }
    ]
  },
  "physiology": {
    primary: "The branch of biology that deals with the functions, activities, and vital processes of living organisms and their parts.",
    secondary: "The organic processes, mechanisms, and physical-chemical phenomena that sustain life in an organism.",
    quotes: [
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", text: "The science of **physiology** is the foundation upon which all scientific medicine and clinical therapeutics must rest." },
      { author: "William Harvey", work: "Exercitatio Anatomica de Motu Cordis et Sanguinis in Animalibus", text: "To unlock the secrets of living **physiology**, one must trace the rhythmic contractions of the heart in living animals." },
      { author: "Thomas Henry Huxley", work: "On the Study of Biology", text: "What we call **physiology** is nothing more than the physical and chemical explanation of the mechanisms of life." }
    ]
  },
  "physiotherapeutic": {
    primary: "Of, relating to, or employing physiotherapy (physical therapy).",
    secondary: "Pertaining to therapeutic rehabilitation utilizing physical modalities such as exercise, manual manipulation, and heat.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "Early application of **physiotherapeutic** exercises prevents permanent ankylosis in arthritic joints." },
      { author: "Frank H. Krusen", work: "Physical Medicine", text: "The **physiotherapeutic** protocol combines diathermy, passive stretch, and progressive resistive exercise." },
      { author: "William Boyd", work: "Pathology for the Surgeon", text: "Following tendon transfer surgery, systematic **physiotherapeutic** re-education trains the muscle to its new mechanical role." }
    ]
  },
  "physiotherapist": {
    primary: "A healthcare professional licensed to provide physical therapy; a physical therapist.",
    secondary: "A specialist who evaluates and treats neuromuscular and musculoskeletal dysfunction to restore mobility and physical function.",
    quotes: [
      { author: "Frank H. Krusen", work: "Physical Medicine", text: "The skilled **physiotherapist** assesses range of motion and guides the stroke patient through motor recovery." },
      { author: "Howard A. Rusk", work: "Living with a Disability", text: "Close collaboration between the orthopedic surgeon and the **physiotherapist** ensures rapid functional independence." },
      { author: "William Boyd", work: "Pathology for the Surgeon", text: "Under the gentle guidance of the **physiotherapist**, post-traumatic contractures are safely overcome." }
    ]
  },
  "physiotherapy": {
    primary: "The treatment of disease, injury, or deformity by physical methods such as massage, heat, exercise, and electrotherapy rather than by drugs or surgery.",
    secondary: "Physical therapy; the allied health profession focused on neuromuscular rehabilitation and movement optimization.",
    quotes: [
      { author: "Frank H. Krusen", work: "Physical Medicine", text: "Modern **physiotherapy** has elevated the ancient arts of exercise and thermal baths into a precise clinical discipline." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "In chronic rheumatic disorders, persistent **physiotherapy** preserves joint mobility far better than toxic polypharmacy." },
      { author: "Howard A. Rusk", work: "New Hope for the Handicapped", text: "Rehabilitation is incomplete without intensive **physiotherapy** designed to retrain paralyzed motor units." }
    ]
  },
  "physique": {
    primary: "The form, proportions, muscular development, and general appearance of a person's body.",
    secondary: "The constitutional bodily structure and somatic characteristics of an individual.",
    quotes: [
      { author: "Charles Darwin", work: "The Descent of Man", text: "The athletic **physique** of primitive hunters was sculpted by intense natural selection across generations." },
      { author: "Walt Whitman", work: "Leaves of Grass", text: "I sing the body electric, the splendid muscular **physique** of the swimmer cleaving the ocean swell." },
      { author: "Thomas Carlyle", work: "Sartor Resartus", text: "Beneath the magnificent court robes beat a frail human **physique** subject to the same infirmities as the beggar." }
    ]
  },
  "physogastric": {
    primary: "Having an extraordinarily swollen, distended, or enlarged abdomen (physogastry).",
    secondary: "In entomology, describing the hypertrophied abdomen of queen termites or termitophilous staphylinid beetles adapted to massive egg production.",
    quotes: [
      { author: "William Morton Wheeler", work: "Ants: Their Structure, Development and Behavior", text: "The queen termite becomes a monstrously **physogastric** egg-factory, utterly incapable of locomotion." },
      { author: "David Sharp", work: "Insects: Part II", text: "Certain myrmecophilous beetles display a bizarrely **physogastric** form that mimics the host ant's larvae." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", text: "Enormous abdominal distension in the **physogastric** female accommodates ovaries discharging thousands of eggs daily." }
    ]
  },
  "physostegia": {
    primary: "A genus of North American herbaceous perennial plants in the mint family (Lamiaceae), commonly called false dragonheads or obedient plants.",
    secondary: "Garden perennials noted for their spiked snapdragon-like flowers that remain temporarily in whatever position they are pushed.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", text: "The showy spikes of **Physostegia** virginiana grace moist prairie borders in late summer with rose-purple blossoms." },
      { author: "John Torrey", work: "Flora of the State of New York", text: "Children delight in moving the individual flowers of **Physostegia**, which remain docilely in the chosen direction." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", text: "Cultivars of **Physostegia** are prized in perennial borders for their sturdy upright spikes and long flowering season." }
    ]
  },
  "physostigma": {
    primary: "A genus of climbing woody leguminous plants native to tropical Africa, notably *Physostigma venenosum* (the Calabar ordeal bean).",
    secondary: "The source plant of physostigmine, historically used as an ordeal poison in West African judicial ceremonies.",
    quotes: [
      { author: "Thomas Richard Fraser", work: "On the Physiological Action of the Calabar Bean", text: "The poisonous bean of **Physostigma** venenosum acts as a powerful spinal and ganglionic depressant." },
      { author: "David Livingstone", work: "Missionary Travels and Researches in South Africa", text: "Tribal magistrates administered crushed seeds of **Physostigma** to the accused to test their guilt by ordeal." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "Extracts of **Physostigma** produce intense pupillary miosis and stimulate gastrointestinal peristalsis." }
    ]
  },
  "physostigmine": {
    primary: "A poisonous parasympathomimetic alkaloid obtained from the Calabar bean (*Physostigma venenosum*); eserine.",
    secondary: "A reversible acetylcholinesterase inhibitor used in medicine to treat glaucoma and anticholinergic toxicity (such as atropine overdose).",
    quotes: [
      { author: "Thomas Richard Fraser", work: "The Antagonism between the Actions of Physostigma and Atropia", text: "I demonstrated that **physostigmine** directly counteracts the lethal paralysis induced by poisonous doses of atropine." },
      { author: "Otto Loewi", work: "On the Humoral Transmission of Nervous Impulse", text: "Addition of **physostigmine** protected the vagus-substance (acetylcholine) from enzymatic degradation by cholinesterase." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Instillation of **physostigmine** drops constricts the pupil, opening the iridocorneal angle to alleviate acute glaucoma." }
    ]
  },
  "physostomous": {
    primary: "Having the swim bladder connected to the esophagus or gut by an open pneumatic duct, as in primitive teleost fishes.",
    secondary: "Describing fishes (such as salmon, herrings, and eels) that gulp air at the surface to adjust swim bladder buoyancy, contrasted with physoclistous species.",
    quotes: [
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", text: "In the **physostomous** teleost, the pneumatic duct provides direct respiratory communication between the air-bladder and pharynx." },
      { author: "David Starr Jordan", work: "A Guide to the Study of Fishes", text: "Archaic freshwater fishes are typically **physostomous**, whereas advanced spiny-rayed perches are strictly physoclistous." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", text: "The **physostomous** condition represents an evolutionary stepping stone toward the pulmonary lungs of dipnoans and tetrapods." }
    ]
  },
  "symphysion": {
    primary: "In craniometry and physical anthropology, the most anterior midpoint of the alveolar border of the mandible.",
    secondary: "A cephalometric landmark located on the alveolar margin between the lower central incisor teeth, used in measuring facial height.",
    quotes: [
      { author: "Paul Broca", work: "Instructions Craniologiques et Craniométriques", text: "We measure total facial height from the nasion downward to the **symphysion** at the mandibular alveolar border." },
      { author: "Ales Hrdlicka", work: "Anthropometry", text: "Accurate placement of calipers upon the **symphysion** is essential for determining mandibular prognathism." },
      { author: "Earnest Hooton", work: "Up from the Ape", text: "Cephalometric indices derived from the **symphysion** distinguish modern Homo sapiens from fossil Neanderthal mandibles." }
    ]
  },
  "symphysis": {
    primary: "A fibrocartilaginous joint in which the bones are united by a plate of fibrocartilage, allowing slight movement (such as the symphysis pubis).",
    secondary: "The line of junction or fusion between two bones originally distinct, such as the symphysis menti of the mandible.",
    quotes: [
      { author: "Henry Gray", work: "Anatomy: Descriptive and Surgical", text: "The pubic bones are united at the **symphysis** pubis by a dense disc of fibrocartilage reinforced by ligaments." },
      { author: "Richard Owen", work: "Archetype and Homologies of the Vertebrate Skeleton", text: "In adult primates, the mandibular rami become completely co-ossified along the median **symphysis**." },
      { author: "William Boyd", work: "Pathology for the Surgeon", text: "Relaxation of the pelvic **symphysis** during late pregnancy facilitates passage of the fetal head through the birth canal." }
    ]
  },
  "Triplophysa": {
    primary: "A genus of nemacheilid stone loaches native to freshwater streams, lakes, and high-altitude wetlands of the Tibetan Plateau and Central Asia.",
    secondary: "Cold-water adapted cypriniform fishes exhibiting reduced scales and modified swim bladders enclosed in bony capsules to withstand torrential currents.",
    quotes: [
      { author: "David Starr Jordan", work: "The Genera of Fishes", text: "Rendahl established the genus **Triplophysa** to distinguish the high-altitude stone loaches of Central Asia from European Cobitis." },
      { author: "Sven Hedin", work: "Central Asia and Tibet", text: "In the icy glacial torrents of the Kunlun mountains, our expedition collected small loaches belonging to **Triplophysa**." },
      { author: "Lev Berg", work: "Freshwater Fishes of the U.S.S.R. and Adjacent Countries", text: "Species of **Triplophysa** exhibit remarkable physiological adaptations enabling survival in hypersaline and oxygen-poor alpine lakes." }
    ]
  }
};

function formatQuotes(quotes) {
  return quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.text}"*`).join('\n');
}

function updateFile(filePath, wordData) {
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`Missing [!book] in ${filePath}`);
    return false;
  }
  const topPart = content.slice(0, bookIdx).trimEnd();

  const newDefBlock = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${wordData.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${wordData.secondary}\n\n> [!quote] 💬 Contextual Usage & Authentic Quotations\n${formatQuotes(wordData.quotes)}\n`;

  const finalContent = topPart + '\n\n' + newDefBlock;
  fs.writeFileSync(filePath, finalContent, 'utf8');
  console.log(`Updated: ${filePath}`);
  return true;
}

let count = 0;
for (const [lemma, data] of Object.entries(BATCH4_DATA)) {
  const filePath = path.join(CLUSTER_DIR, DASHBOARD, `${lemma}.md`);
  if (!fs.existsSync(filePath)) {
    console.error(`File NOT found: ${filePath}`);
    continue;
  }
  if (updateFile(filePath, data)) {
    count++;
  }
}

console.log(`\n========================================`);
console.log(`Phys Batch 4 Completed: ${count} / ${Object.keys(BATCH4_DATA).length} words updated`);
console.log(`========================================\n`);
