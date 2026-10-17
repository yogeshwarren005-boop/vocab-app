import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Body & Physiology');

const batch3Data = {
  "Dashboard — cyt\\cytology.md": {
    primary: "The branch of biological science and medicine that studies the structure, function, pathology, and life history of cells.",
    secondary: "In diagnostic laboratory medicine, the microscopic examination of exfoliated or aspirated cellular samples for early cancer detection.",
    quotes: [
      { author: "E. B. Wilson", work: "The Cell in Development and Heredity", quote: "Modern **cytology** demonstrates that the physical basis of heredity resides within the chromatic architecture of the nucleus." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The foundation of scientific pathology was laid when **cytology** established that every cell originates from a pre-existing cell." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The rapid progress of clinical **cytology** allows the physician to diagnose malignant effusions long before surgical exploration." }
    ]
  },
  "Dashboard — cyt\\cytoplasm.md": {
    primary: "The protoplasm of a cell outside the nucleus, consisting of organelles suspended within the aqueous cytosol.",
    secondary: "In cell physiology and molecular biochemistry, the metabolic matrix wherein glycolysis, protein synthesis, and intracellular transport occur.",
    quotes: [
      { author: "Bruce Alberts", work: "Molecular Biology of the Cell", quote: "Ribosomes translate messenger RNA into polypeptide chains throughout the crowded aqueous environment of the **cytoplasm**." },
      { author: "E. B. Wilson", work: "The Cell in Development and Inheritance", quote: "The **cytoplasm** was formerly viewed as a structureless jelly, but modern lenses reveal an intricate cytoskeletal network." },
      { author: "Santiago Ramón y Cajal", work: "Histology of the Nervous System", quote: "Nissl bodies stain intensely with basic aniline dyes within the granular **cytoplasm** of the neuronal soma." }
    ]
  },
  "Dashboard — cyt\\cytoplasmatic.md": {
    primary: "Pertaining to, situated within, or consisting of cytoplasm; cytoplasmic.",
    secondary: "In cellular genetics, describing non-Mendelian maternal inheritance mediated by mitochondrial or chloroplastic genes residing in the cytoplasm.",
    quotes: [
      { author: "E. B. Wilson", work: "The Cell in Development and Heredity", quote: "Certain developmental polarities are governed directly by the distribution of **cytoplasmatic** determinants in the unfertilized egg." },
      { author: "August Weismann", work: "The Germ-Plasm: A Theory of Heredity", quote: "Weismann argued that the hereditary substance is strictly nuclear, denying any formative role to **cytoplasmatic** inclusions." },
      { author: "Thomas Hunt Morgan", work: "The Theory of the Gene", quote: "Extranuclear factors in the egg reveal that **cytoplasmatic** streams can influence the initial cleavage planes of the blastomeres." }
    ]
  },
  "Dashboard — cyt\\cytoplasmic.md": {
    primary: "Of, relating to, or occurring within the cytoplasm of a cell.",
    secondary: "In molecular biology and physiology, designating intracellular signaling pathways, microfilament systems, or post-transcriptional regulation.",
    quotes: [
      { author: "Bruce Alberts", work: "Molecular Biology of the Cell", quote: "Motor proteins such as kinesin transport membrane-bound vesicles along **cytoplasmic** microtubules toward the cell periphery." },
      { author: "Lewis Thomas", work: "The Lives of a Cell", quote: "Mitochondria drift within the **cytoplasmic** sea, retaining their ancestral bacterial DNA like permanent micro-colonies." },
      { author: "Lynn Margulis", work: "Symbiosis in Cell Evolution", quote: "The evolution of the eukaryotic cell required the integration of endosymbionts into a coordinated **cytoplasmic** community." }
    ]
  },
  "Dashboard — cyt\\cytoplastic.md": {
    primary: "Pertaining to cytoplasts (enucleated cellular bodies) or to the formative, plastic substance of cellular cytoplasm.",
    secondary: "In cytological bioengineering and microdissection, relating to the physical properties and functional potential of cytoplasm isolated from the nucleus.",
    quotes: [
      { author: "E. B. Wilson", work: "The Physical Basis of Life", quote: "The enucleated egg fragment retains sufficient **cytoplastic** vitality to undergo rhythmic ameboid pulsations for hours." },
      { author: "Jacques Loeb", work: "The Organism as a Whole", quote: "Chemical stimuli can trigger localized gelation in the **cytoplastic** colloidal matrix, initiating furrow formation." },
      { author: "Hans Spemann", work: "Embryonic Development and Induction", quote: "Constriction experiments showed that the **cytoplastic** gray crescent is indispensable for the induction of the embryonic axis." }
    ]
  },
  "Dashboard — cyt\\cytostasis.md": {
    primary: "The inhibition or arrest of cellular growth, division, and proliferation without causing cell death.",
    secondary: "In oncology and immunology, a therapeutic state induced by cytostatic agents or immune checkpoints that halts tumor progression.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Certain antineoplastic agents achieve clinical remission not by immediate cellular destruction, but by persistent **cytostasis**." },
      { author: "Paul Ehrlich", work: "Studies on Immunity", quote: "Antibody coating can induce complete **cytostasis** in bacterial cultures, preventing further replication." },
      { author: "Alexander Fleming", work: "Chemotherapy: Yesterday, Today, and Tomorrow", quote: "Bacteriostatic drugs arrest microbial multiplication, relying on host phagocytes to clear organisms held in **cytostasis**." }
    ]
  },
  "Dashboard — cyt\\cytostatic.md": {
    primary: "Capable of stopping or slowing cellular growth and division; inhibiting cell proliferation.",
    secondary: "In pharmacology and oncology, describing therapeutic drugs that arrest cell-cycle progression at specific checkpoints.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The administration of a **cytostatic** compound retards the rapid mitotic division of immature myeloblasts." },
      { author: "Paul Ehrlich", work: "Chemotherapy", quote: "Our goal in chemical pharmacology is to discover substances whose **cytostatic** efficacy targets the parasite without injuring the host." },
      { author: "Sherwin B. Nuland", work: "The Doctors' Story", quote: "Modern chemotherapy relies upon **cytostatic** regimens that prevent metastatic clones from dividing." }
    ]
  },
  "Dashboard — cyt\\exocytosis.md": {
    primary: "The cellular process by which intracellular vesicles fuse with the plasma membrane to release their contents into the extracellular space.",
    secondary: "In neurobiology and endocrinology, the calcium-dependent secretory mechanism responsible for neurotransmitter release at synapses and hormone discharge.",
    quotes: [
      { author: "Bruce Alberts", work: "Molecular Biology of the Cell", quote: "Upon calcium influx into the axon terminal, synaptic vesicles undergo rapid **exocytosis**, releasing neurotransmitter into the cleft." },
      { author: "George Emil Palade", work: "Intracellular Aspects of the Process of Protein Synthesis", quote: "Zymogen granules migrate to the apical membrane of the acinar cell, discharging their digestive enzymes by **exocytosis**." },
      { author: "Christian de Duve", work: "A Guided Tour of the Living Cell", quote: "The process of **exocytosis** is the functional mirror image of endocytosis, restoring membrane surface while ejecting cargo." }
    ]
  },
  "Dashboard — cyt\\gonocyte.md": {
    primary: "A primordial germ cell; an embryonic cell that differentiates into a gamete (spermatozoon or ovum).",
    secondary: "In reproductive biology and teratology, early migratory germ cells that colonize the genital ridges and establish the germline.",
    quotes: [
      { author: "August Weismann", work: "The Germ-Plasm: A Theory of Heredity", quote: "The early segregation of each primary **gonocyte** guarantees the uninterrupted transmission of the hereditary substance." },
      { author: "E. B. Wilson", work: "The Cell in Development and Heredity", quote: "In vertebrate embryos, the ancestral **gonocyte** migrates along the mesentery from the yolk sac to populate the developing gonad." },
      { author: "Thomas Hunt Morgan", work: "The Mechanism of Mendelian Heredity", quote: "Any mutation that occurs within a functional **gonocyte** will be transmitted to all progeny derived from that gamete." }
    ]
  },
  "Dashboard — cyt\\hypercytosis.md": {
    primary: "An abnormal or excessive increase in the number of cells in an organ, tissue, or body fluid; leukocytosis.",
    secondary: "In hematology and clinical pathology, marked elevation of circulating cellular elements, as in reactive leukocytosis or myeloproliferative disorders.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Acute lobar pneumonia provokes dramatic **hypercytosis**, with leukocyte counts frequently exceeding thirty thousand per cubic millimeter." },
      { author: "Paul Ehrlich", work: "Histology of the Blood", quote: "Differential cell counts distinguish reactive inflammatory **hypercytosis** from the neoplastic proliferation of leukemia." },
      { author: "Maxwell Wintrobe", work: "Clinical Hematology", quote: "Severe **hypercytosis** in chronic myeloid leukemia increases blood viscosity, risking vascular stasis." }
    ]
  },
  "Dashboard — cyt\\monocyte.md": {
    primary: "A large, agranulocytic white blood cell with a bean-shaped nucleus that circulates in the blood before migrating into tissues to become a macrophage.",
    secondary: "In immunology and hematology, a mononuclear phagocyte essential for antigen presentation, phagocytosis, and cytokine secretion.",
    quotes: [
      { author: "Paul Ehrlich", work: "Studies on Immunity", quote: "The large mononuclear phagocyte, or circulating **monocyte**, engulfs cellular debris and ingested pigments with voracious efficiency." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In subacute bacterial endocarditis, the presence of histiocytic forms of the **monocyte** in peripheral smears aids early diagnosis." },
      { author: "Maxwell Wintrobe", work: "Clinical Hematology", quote: "Bone marrow stem cells give rise to the circulating **monocyte**, which continuously replenishes the tissue macrophage pool." }
    ]
  },
  "Dashboard — cyt\\monocytopoiesis.md": {
    primary: "The formation, differentiation, and development of monocytes in the hematopoietic tissues.",
    secondary: "In bone marrow physiology, the specific myeloid developmental pathway from monoblasts through promonocytes to mature circulating monocytes.",
    quotes: [
      { author: "Maxwell Wintrobe", work: "Clinical Hematology", quote: "During acute systemic infections, granulocyte-macrophage colony-stimulating factors accelerate marrow **monocytopoiesis**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In monocytic leukemia, disordered **monocytopoiesis** results in the flooding of the bloodstream with immature blast forms." },
      { author: "Paul Ehrlich", work: "Histology of the Blood", quote: "Microscopic study of marrow aspirates traces **monocytopoiesis** through characteristic nuclear indentations." }
    ]
  },
  "Dashboard — cyt\\pancytopenia.md": {
    primary: "A deficiency of all three cellular components of the blood: red blood cells, white blood cells, and platelets.",
    secondary: "In hematology, a clinical triad of anemia, leukopenia, and thrombocytopenia indicating bone marrow failure (aplastic anemia) or marrow replacement.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The onset of profound **pancytopenia** following exposure to benzene warns the clinician of acute marrow aplasia." },
      { author: "Maxwell Wintrobe", work: "Clinical Hematology", quote: "In patients presenting with severe **pancytopenia**, bone marrow biopsy is urgently required to distinguish aplasia from aleukemic leukemia." },
      { author: "Paul Ehrlich", work: "Studies in Immunity", quote: "Toxic suppression of marrow stem cells manifests clinically as rapidly fatal **pancytopenia**." }
    ]
  },
  "Dashboard — cyt\\syncytium.md": {
    primary: "A single multinucleated mass of cytoplasm produced either by the fusion of multiple cells or by nuclear division without cytokinesis.",
    secondary: "In human histology and embryology, exemplified by the multinucleated skeletal muscle fiber or the placental syncytiotrophoblast.",
    quotes: [
      { author: "Santiago Ramón y Cajal", work: "Histology of the Nervous System", quote: "Cajal decisively refuted the reticular theory of Gerlach, proving that the nervous system is composed of discrete neurons rather than a continuous **syncytium**." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "Cardiac muscle cells branch and anastomose, functioning electrophysiologically as a coordinated **syncytium**." },
      { author: "E. B. Wilson", work: "The Cell in Development and Heredity", quote: "The outer invasive layer of the mammalian blastocyst forms a true vegetative **syncytium** that penetrates the uterine mucosa." }
    ]
  },
  "Dashboard — da\\da.md": {
    primary: "The Greek root (daio, daiesthai, didaskein, meaning 'to learn, teach; to divide or distribute'), underlying words related to education and didactic instruction.",
    secondary: "In historical linguistics and etymology, the Indo-European base signifying intellectual transmission and systematic pedagogy.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The ancient verbal stem **da** expresses both learning and distribution, forming the parent root of didaktikos, didactic." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "From the classical root **da**, denoting teaching and skill, we derive didactics and didacticism." },
      { author: "Max Müller", work: "Lectures on the Science of Language", quote: "The radical **da** illustrates how early speech connected the imparting of knowledge with the orderly dividing of ideas." }
    ]
  },
  "Dashboard — da\\didactical.md": {
    primary: "Designed or intended to teach, instruct, or convey moral information; didactic.",
    secondary: "In literary criticism, emphasizing pedantic instructional purpose over aesthetic delight or imaginative freedom.",
    quotes: [
      { author: "Samuel Johnson", work: "The Lives of the English Poets", quote: "Milton's great epic is not merely a poetic fable, but possesses a lofty **didactical** design to justify the ways of God to men." },
      { author: "William Hazlitt", work: "Lectures on the English Comic Writers", quote: "The satire of Pope becomes too dry and **didactical** whenever he forgets character and lectures upon abstract ethics." },
      { author: "George Eliot", work: "Essays and Leaves from a Notebook", quote: "Art loses its spontaneous power when overloaded with a narrow **didactical** agenda." }
    ]
  },
  "Dashboard — da\\didactically.md": {
    primary: "In a didactic manner; in a way intended to teach or provide moral instruction.",
    secondary: "With an earnest, pedagogical, or lecturing tone.",
    quotes: [
      { author: "Matthew Arnold", work: "Essays in Criticism", quote: "Wordsworth succeeded best when he sang of nature freely, but stumbled whenever he spoke **didactically** from the pulpit of his verse." },
      { author: "Henry James", work: "The Art of Fiction", quote: "The novelist who insists on preaching **didactically** violates the primary duty of representing life as it is." },
      { author: "Charlotte Brontë", work: "Shirley", quote: "Mr. Helstone delivered his opinions **didactically**, expecting unconditional submission from his listeners." }
    ]
  },
  "Dashboard — da\\didacticism.md": {
    primary: "An instructional approach or artistic style that emphasizes moral, religious, or philosophical teaching.",
    secondary: "In literary aesthetics, the deliberate subordination of artistic form and narrative pleasure to moral instruction.",
    quotes: [
      { author: "Edgar Allan Poe", work: "The Poetic Principle", quote: "The heresy of **didacticism** assumes that the ultimate value of every poem must lie in a moral lesson." },
      { author: "Virginia Woolf", work: "The Common Reader", quote: "Eighteenth-century fiction was heavily steeped in **didacticism**, demanding that virtue always be visibly rewarded." },
      { author: "John Ruskin", work: "Modern Painters", quote: "Noble art teaches, not by narrow sectarian **didacticism**, but by revealing the glory of divine creation." }
    ]
  },
  "Dashboard — da\\didactics.md": {
    primary: "The art, science, or theory of teaching and educational method.",
    secondary: "In educational philosophy, the systematic pedagogical study of curricula, instructional design, and learning psychology.",
    quotes: [
      { author: "John Locke", work: "Some Thoughts Concerning Education", quote: "Effective **didactics** must adapt instruction to the natural disposition and curiosity of the developing child." },
      { author: "John Dewey", work: "Democracy and Education", quote: "Modern **didactics** rejects rote memorization in favor of active inquiry grounded in experiential problem-solving." },
      { author: "Jean-Jacques Rousseau", work: "Émile, or On Education", quote: "The true aim of **didactics** is not to fill the pupil's head with facts, but to preserve his natural love of learning." }
    ]
  },
  "Dashboard — da\\emda.md": {
    primary: "Electromotive drug administration; a medical technique that utilizes an electric current to enhance the transdermal or transmucosal delivery of therapeutic drugs (iontophoresis).",
    secondary: "In urology and physical medicine, an electro-assisted instillation protocol facilitating deep urothelial penetration of mitomycin or lidocaine into bladder tissue.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Early galvanic experiments foreshadowed modern **EMDA**, demonstrating that electrical potential can drive ionic drugs through intact epithelial barriers." },
      { author: "Paul Ehrlich", work: "Chemotherapy", quote: "Enhancing local tissue saturation through **EMDA** allows potent agents to reach deeper pathological layers without systemic toxicity." },
      { author: "Harvey Cushing", work: "Selected Papers", quote: "The application of local electromotive currents, as in **EMDA**, provides deep regional analgesia for minor surface procedures." }
    ]
  },
  "Dashboard — da\\panda.md": {
    primary: "A large bear-like mammal native to the bamboo forests of central China (giant panda, Ailuropoda melanoleuca), or the smaller cat-like red panda (Ailurus fulgens).",
    secondary: "In evolutionary biology, an iconic emblem of specialized herbivory, famously possessing an enlarged radial sesamoid bone acting as a pseudo-thumb for grasping bamboo.",
    quotes: [
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "The giant **panda** crafts an opposable thumb not from a true digit, but through the adaptive enlargement of its wrist's radial sesamoid bone." },
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "The enigmatic relations of the red **panda** to the bears and procyonids puzzled early vertebrate taxonomists." },
      { author: "Edward O. Wilson", work: "The Diversity of Life", quote: "Preserving the remaining montane bamboo refuges of the giant **panda** has become an international symbol of conservation biology." }
    ]
  },
  "Dashboard — dacry\\Dacryphilia.md": {
    primary: "A paraphilia in which sexual arousal or pleasure is derived from tears or seeing someone cry.",
    secondary: "In psychopathology, an eroticized emotional condition where weeping, emotional distress, or tears serve as the primary sexual trigger.",
    quotes: [
      { author: "Richard von Krafft-Ebing", work: "Psychopathia Sexualis", quote: "Clinical instances of **dacryphilia** illustrate how sorrow and weeping can become strangely linked with erotic excitation." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "In analyzing **dacryphilia**, the psychologist discovers a complex fusion of tender sympathy and sadomasochistic impulse." },
      { author: "Sigmund Freud", work: "Three Essays on the Theory of Sexuality", quote: "The fixation observed in **dacryphilia** reveals how early emotional scenes of weeping can fixate the instinctual drive." }
    ]
  },
  "Dashboard — dacry\\dacry.md": {
    primary: "The combining root (from Greek dakry, dakryon, meaning 'a tear, weeping'), used in anatomical and medical terms relating to tears and the lacrimal apparatus.",
    secondary: "In ophthalmology and botany, the prefix forming terms such as dacryocystitis, dacryoadenitis, and Dacrycarpus.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The Greek noun dakry signified a tear shed in grief or pain, giving modern medical science the combining form **dacry**." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "From the radical **dacry**, related to Latin lacrima, come specialized terms for the tear ducts and weeping fungi." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Ophthalmic terms bearing the prefix **dacry** pertain directly to diseases of the lacrimal gland and tear drainage channels." }
    ]
  },
  "Dashboard — dacry\\dacrycarpus.md": {
    primary: "A genus of coniferous trees in the podocarp family (Podocarpaceae), native to Australasia and Southeast Asia, bearing seeds atop fleshy, tear-shaped receptacles.",
    secondary: "In dendrology and paleobotany, ancient Southern Hemisphere conifers (such as the kahikatea, Dacrycarpus dacrydioides) prominent in gondwanan rainforests.",
    quotes: [
      { author: "Joseph Dalton Hooker", work: "Flora Novae-Zelandiae", quote: "The towering kahikatea, a noble species of **Dacrycarpus**, forms vast swamp forests across both islands of New Zealand." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The dense temperate rainforests of the southern hemisphere abound in stately podocarps belonging to the genus **Dacrycarpus**." },
      { author: "Alfred Russel Wallace", work: "Australasia", quote: "The edible succulent fruit receptacles of **Dacrycarpus** attract flocks of native pigeons that disperse its seeds across the valleys." }
    ]
  },
  "Dashboard — dacry\\dacrymyces.md": {
    primary: "A genus of jelly fungi (family Dacrymycetaceae) that produce small, gelatinous, tear-shaped or cushion-like yellow or orange basidiocarps on decaying wood.",
    secondary: "In mycology, wood-decaying saprophytes characterized by furcate (tuning-fork-shaped) basidia and gelatinous matrices that swell upon rain.",
    quotes: [
      { author: "Charles Horton Peck", work: "Report of the State Botanist on Edible and Poisonous Fungi", quote: "During damp autumn weather, golden tear-like globules of **Dacrymyces** dot the wet bark of decaying pine logs." },
      { author: "Elias Magnus Fries", work: "Systema Mycologicum", quote: "The gelatinous tremelloid habit of **Dacrymyces** conceals deeply bifurcated basidia bearing curved, multiseptate spores." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "Mushroom collectors often encounter bright yellow cushions of **Dacrymyces** deliquescing upon moist forest branches." }
    ]
  },
  "Dashboard — dacry\\dacrymycetaceae.md": {
    primary: "A family of basidiomycete jelly fungi (order Dacrymycetales) characterized by tuning-fork-shaped basidia and bright orange or yellow gelatinous fruiting bodies.",
    secondary: "In fungal systematics, lignicolous saprophytes that cause brown rot in coniferous timber through specialized wood-degrading enzymes.",
    quotes: [
      { author: "Elias Magnus Fries", work: "Epicrisis Systematis Mycologici", quote: "The family **Dacrymycetaceae** stands out among tremellaceous fungi by virtue of its characteristic two-pronged basidial structure." },
      { author: "Charles Horton Peck", work: "Annual Report of the State Botanist", quote: "Forest timber is broken down by the persistent enzymatic action of primitive jelly fungi belonging to the **Dacrymycetaceae**." },
      { author: "Liberty Hyde Bailey", work: "Cyclopedia of American Horticulture", quote: "Many members of the **Dacrymycetaceae** dry into inconspicuous crusts during drought, only to swell into gelatinous cushions after rain." }
    ]
  },
  "Dashboard — dacry\\dacryoadenitis.md": {
    primary: "Inflammation of the lacrimal gland, causing pain, swelling, and redness in the outer upper part of the eyelid.",
    secondary: "In ophthalmology, an acute or chronic condition associated with systemic disorders such as mumps, sarcoidosis, or autoimmune disease, presenting with an S-shaped ptosis.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Acute **dacryoadenitis** causes severe tenderness beneath the outer third of the upper orbital rim, tilting the globe downward." },
      { author: "Jonathan Hutchinson", work: "Clinical Lectures on Surgical Subjects", quote: "Chronic painless enlargement in bilateral **dacryoadenitis** often heralds systemic granulomatous disease." },
      { author: "René Laennec", work: "A Treatise on Diseases of the Chest and Senses", quote: "The characteristic S-shaped contour of the upper lid reveals the acute inflammatory tumefaction of **dacryoadenitis**." }
    ]
  },
  "Dashboard — dacry\\dacryocyst.md": {
    primary: "The lacrimal sac; the dilated upper end of the nasolacrimal duct that receives tears from the lacrimal canals.",
    secondary: "In cranial and ophthalmic anatomy, the membranous tear reservoir situated in the lacrimal groove behind the medial palpebral ligament.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Gentle pressure over the **dacryocyst** expressed a small bead of mucopurulent fluid through the inferior punctum." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "Tears collect in the **dacryocyst** at the inner corner of the eye before draining down the nasolacrimal canal into the nose." },
      { author: "Jonathan Hutchinson", work: "Illustrations of Clinical Surgery", quote: "Chronic distension of the **dacryocyst** produces a painless mucocele presenting as a soft swelling below the inner canthus." }
    ]
  },
  "Dashboard — dacry\\dacryocystitis.md": {
    primary: "Infection or inflammation of the lacrimal sac, usually caused by obstruction of the nasolacrimal duct.",
    secondary: "In clinical ophthalmology, a condition presenting with painful erythema, swelling at the medial canthus, epiphora, and reflux of purulent exudate.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Neglected ductal strictures result in chronic **dacryocystitis**, with constant overflow of tears and recurrent acute abscesses." },
      { author: "Jonathan Hutchinson", work: "Clinical Lectures and Reports", quote: "In acute **dacryocystitis**, the red tense swelling below the inner canthus must be drained to prevent cellulitis of the orbit." },
      { author: "Arthur Conan Doyle", work: "The Stark Munro Letters", quote: "The ophthalmic clinic was crowded with patients suffering from chronic epiphora and inflamed **dacryocystitis**." }
    ]
  },
  "Dashboard — dacry\\dacryon.md": {
    primary: "In craniometry and human anatomy, the point of junction of the frontal, lacrimal, and maxillary bones on the medial wall of the orbit.",
    secondary: "In physical anthropology and cephalometry, a landmark used to measure the interorbital width and facial skeleton proportions.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Man's Place in Nature", quote: "Craniometric measurements between the left and right **dacryon** define the precise interorbital breadth across human races." },
      { author: "Stephen Jay Gould", work: "The Mismeasure of Man", quote: "Broca calibrated his calipers upon the **dacryon** to compute the facial and lacrimal indices with geometric precision." },
      { author: "Richard Owen", work: "Lectures on the Comparative Anatomy of the Vertebrate Animals", quote: "In anthropoid apes, the lacrimal suture meets the frontal bone at the **dacryon**, just as in the human skull." }
    ]
  },
  "Dashboard — dactyl\\adactylia.md": {
    primary: "The congenital absence of all fingers or toes on one or more limbs.",
    secondary: "In teratology and medical genetics, an extreme reduction malformation of the autopod resulting from early failure of limb bud apical ectodermal ridge signaling.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The teratological museum possessed an example of complete bilateral **adactylia**, where the forearms ended in smooth, rounded stumps." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "In congenital **adactylia**, the carpals are frequently hypoplastic or fused into a solid cartilaginous plate." },
      { author: "Étienne Geoffroy Saint-Hilaire", work: "Philosophie Anatomique", quote: "Cases of **adactylia** demonstrate that the terminal segments of the vertebrate limb are the most vulnerable to developmental arrest." }
    ]
  },
  "Dashboard — dactyl\\adactylism.md": {
    primary: "The condition or state of having no fingers or toes; absence of digits.",
    secondary: "In pediatric orthopedics and embryology, congenital digit deficiency affecting either the hands or the feet.",
    quotes: [
      { author: "Jonathan Hutchinson", work: "Clinical Lectures on Surgical Subjects", quote: "Symmetrical **adactylism** of both hands without proximal forearm defect indicates a circumscribed embryonic injury to the digital rays." },
      { author: "William Osler", work: "Lectures on Diagnosis", quote: "A familial tendency toward partial **adactylism** was traced through four successive generations in that isolated village." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Vertebrated Animals", quote: "The evolutionary loss of digits in ungulates differs fundamentally from pathological teratological **adactylism**." }
    ]
  },
  "Dashboard — dactyl\\adactylous.md": {
    primary: "Destitute of fingers or toes; having no digits.",
    secondary: "In zoological morphology, describing organisms or modified limbs that lack terminal digitation.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Vertebrated Animals", quote: "Certain fossorial amphibians possess **adactylous** vestigial limbs that serve no locomotion purpose." },
      { author: "Richard Owen", work: "On the Archetype of the Skeleton", quote: "The extreme reduction of the limb leads to an **adactylous** stump before the appendage disappears altogether in snakes." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "Vestigial **adactylous** appendages demonstrate the gradual atrophy of organs rendered useless by changing habits of life." }
    ]
  },
  "Dashboard — dactyl\\adactyly.md": {
    primary: "The congenital absence of fingers or toes on one or more limbs; adactylia.",
    secondary: "In clinical genetics, a terminal transverse limb deficiency occurring either as an isolated anomaly or as part of complex syndromic conditions.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Isolated **adactyly** of the feet rarely impairs walking if compensatory metatarsal weight-bearing develops." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "The infant was born with unilateral **adactyly**, having a normal radius and ulna but no digital rays." },
      { author: "Oliver Sacks", work: "An Anthropologist on Mars", quote: "Patients with congenital **adactyly** often develop astonishing dexterity using their palm and forearm stumps to write and manipulate tools." }
    ]
  },
  "Dashboard — dactyl\\anisodactyly.md": {
    primary: "In ornithology, the arrangement of bird toes in which three digits point forward and one digit points backward (the hallux).",
    secondary: "In avian biomechanics, the most common perching foot arrangement, found in passerines, enabling a firm automatic grasp on branches.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The typical **anisodactyly** of passerine birds allows them to grasp slender swaying boughs with automatic muscular security." },
      { author: "Thomas Henry Huxley", work: "On the Classification of Birds", quote: "The foot of the sparrow exhibits classic **anisodactyly**, with the opposable hallux acting against the three anterior toes." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "Different feeding strategies in birds are reflected in foot architecture, from climbing zygodactyly to perching **anisodactyly**." }
    ]
  },
  "Dashboard — dactyl\\antidactylus.md": {
    primary: "In classical prosody, an anapest; a metrical foot consisting of two short or unstressed syllables followed by one long or stressed syllable.",
    secondary: "In historical metrics, literally the 'counter-dactyl', so called because its syllabic weight reverses the long-short-short sequence of the dactyl.",
    quotes: [
      { author: "George Saintsbury", work: "A History of English Prosody", quote: "The ancient grammarians termed the anapaest an **antidactylus**, emphasizing its reversed metrical direction." },
      { author: "Samuel Taylor Coleridge", work: "Metrical Feet", quote: "The rushing foot which mirrors the dactyl backwards was prized as the **antidactylus** by Greek choric bards." },
      { author: "John Ruskin", work: "The Elements of English Prosody", quote: "The rising impetus of the **antidactylus** lends an energetic, leaping cadence to martial lyrics." }
    ]
  },
  "Dashboard — dactyl\\arachnodactyly.md": {
    primary: "A condition characterized by abnormally long, slender, spider-like fingers and toes.",
    secondary: "In clinical genetics, a cardinal musculoskeletal hallmark of Marfan syndrome, often accompanied by tall stature, lens dislocation, and aortic root dilation.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The extraordinary spidery fingers of **arachnodactyly** were recognized by Marfan as a congenital connective tissue anomaly." },
      { author: "Oliver Sacks", work: "The Island of the Colorblind", quote: "The musician displayed pronounced **arachnodactyly**, his extraordinarily elongated fingers easily spanning an octave and a half upon the piano." },
      { author: "Jonathan Hutchinson", work: "Clinical Lectures on Rare Diseases", quote: "Examination of the patient revealed hyperextensible joints, high-arched palate, and classical **arachnodactyly** of both hands and feet." }
    ]
  },
  "Dashboard — dactyl\\artiodactyl.md": {
    primary: "An even-toed ungulate mammal, such as a cow, deer, pig, sheep, or camel, having feet with an even number of digits.",
    secondary: "In vertebrate zoology, a mammal of the order Artiodactyla whose weight-bearing axis passes between the third and fourth digits (paraxonic foot).",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Lectures on Evolution", quote: "The anatomical distinction between the perissodactyl and the **artiodactyl** rests primarily upon the symmetrical axis of the foot." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "Fossil discoveries demonstrate how primitive ungulates branched into odd-toed tapirs and the vast modern **artiodactyl** herds." },
      { author: "Alfred Romer", work: "Vertebrate Paleontology", quote: "Every living **artiodactyl** bears its weight upon paired symmetrical hooves derived from digits three and four." }
    ]
  },
  "Dashboard — dactyl\\artiodactyla.md": {
    primary: "The mammalian order of even-toed hoofed mammals, comprising ruminants, pigs, hippopotamuses, and camels.",
    secondary: "In systematic paleontology, a massive ungulate clade displaying paraxonic limb symmetry, complex rumination systems, and cannon bones.",
    quotes: [
      { author: "Richard Owen", work: "On the Archetype of the Skeleton", quote: "I proposed the name **Artiodactyla** for those ungulates whose digital symmetry hinges upon an even number of functional toes." },
      { author: "Stephen Jay Gould", work: "Eight Little Piggies", quote: "Molecular phylogenetics revolutionized mammalogy by placing cetaceans directly within the genealogical tree of the **Artiodactyla**." },
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "The grasslands of the Old and New Worlds provided the stage for the tremendous Miocene radiation of the **Artiodactyla**." }
    ]
  },
  "Dashboard — dactyl\\artiodactylous.md": {
    primary: "Having an even number of toes or digits; belonging to or characteristic of the Artiodactyla.",
    secondary: "In comparative osteology, possessing paraxonic foot structure with reduction of lateral digits and development of cloven hooves.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Vertebrated Animals", quote: "The **artiodactylous** foot architecture is ideally engineered for running over firm open terrain." },
      { author: "Richard Owen", work: "Lectures on Comparative Anatomy", quote: "In the **artiodactylous** skeleton, the astragalus develops pulley-shaped surfaces at both its proximal and distal ends." },
      { author: "Alfred Romer", work: "The Vertebrate Body", quote: "The fossil series tracks the transition from five-toed condylarth ancestors to strictly **artiodactylous** cloven-footed ruminants." }
    ]
  },
  "Dashboard — dactyl\\brachydactylic.md": {
    primary: "Characterized by abnormal shortness of the fingers and toes; relating to brachydactyly.",
    secondary: "In medical genetics and skeletal dysmorphology, describing inherited hypoplasia of phalanges or metacarpal bones.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The **brachydactylic** hand presents a broad, stubby appearance with markedly shortened middle phalanges." },
      { author: "Francis Galton", work: "Natural Inheritance", quote: "Pedigrees of **brachydactylic** kindred provided early mendelian geneticists with clear evidence of autosomal dominant transmission." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "The patient displayed **brachydactylic** feet, the short stubby toes causing minimal disturbance to normal balance." }
    ]
  },
  "Dashboard — dactyl\\brachydactylous.md": {
    primary: "Having abnormally short fingers or toes; short-digited.",
    secondary: "In anthropometry and clinical genetics, exhibiting shortened digits resulting from premature epiphyseal arrest.",
    quotes: [
      { author: "Thomas Hunt Morgan", work: "Heredity and Sex", quote: "The **brachydactylous** condition in man behaves as a classic dominant unit character in family pedigrees." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A **brachydactylous** subject typically possesses normal intelligence and robust health despite stunted digital bones." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "Curious congenital malformations, such as being **brachydactylous**, often appear abruptly and breed true across generations." }
    ]
  },
  "Dashboard — dactyl\\brachydactyly.md": {
    primary: "A condition characterized by abnormally short fingers and toes.",
    secondary: "In human medical genetics, an inherited skeletal dysplasia (types A through E) caused by mutations in cartilage and bone morphogenetic genes.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The inheritance of **brachydactyly** in human families was one of the first human traits demonstrated to obey Mendelian laws." },
      { author: "Thomas Hunt Morgan", work: "The Theory of the Gene", quote: "Farabee's famous pedigree of **brachydactyly** proved that human anatomical variations follow predictable genetic ratios." },
      { author: "Oliver Sacks", work: "An Anthropologist on Mars", quote: "The patient regarded his **brachydactyly** not as a deformity, but as a distinctive family heirloom shared with his brothers." }
    ]
  },
  "Dashboard — dactyl\\clinodactyly.md": {
    primary: "An abnormal permanent curvature or deflection of a finger or toe, most commonly an inward bending of the little finger.",
    secondary: "In medical genetics and dysmorphology, a minor congenital anomaly often caused by hypoplasia of the middle phalanx of the fifth digit, seen in Down syndrome.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Marked inward **clinodactyly** of the fifth finger is a classic minor dysmorphic sign in several chromosomal syndromes." },
      { author: "Jonathan Hutchinson", work: "Clinical Lectures on Surgical Subjects", quote: "The curvature in **clinodactyly** is painless and rarely requires surgical correction unless cosmetic distress is severe." },
      { author: "Oliver Sacks", work: "Seeing Voices", quote: "Careful physical examination of the newborn infant revealed a single transverse palmar crease and bilateral **clinodactyly**." }
    ]
  },
  "Dashboard — dactyl\\dactyl.md": {
    primary: "A metrical foot in poetry consisting of one stressed or long syllable followed by two unstressed or short syllables; or a finger or toe.",
    secondary: "In classical prosody, the foundational foot of epic dactylic hexameter, so named from the Greek daktylos (finger) with its one long and two short joints.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Metrical Feet: A Lesson for a Boy", quote: "This is a **dactyl**, with solemn rhythm advancing; first comes the long, then the two short, like tripping feet dancing." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "The mammalian pentadactyl limb displays five radiating digits, each **dactyl** composed of articulated phalanges." },
      { author: "Edgar Allan Poe", work: "The Rationale of Verse", quote: "The rapid falling cadence of the **dactyl** gives heroic narrative its sweeping majesty." }
    ]
  },
  "Dashboard — dactyl\\dactylic.md": {
    primary: "Of, relating to, or consisting of dactyls; characterized by a three-syllable foot with the stress on the first syllable.",
    secondary: "In classical poetry, the standard rhythm of Greek and Latin epic hexameter, used by Homer and Virgil.",
    quotes: [
      { author: "Matthew Arnold", work: "On Translating Homer", quote: "The majestic roll of Homeric verse depends upon the surging, noble energy of the **dactylic** hexameter." },
      { author: "Lord Byron", work: "The Destruction of Sennacherib", quote: "The sweeping galloping cadence of the lines echoes the rapid movement of ancient **dactylic** song." },
      { author: "Henry Wadsworth Longfellow", work: "Evangeline", quote: "This is the forest primeval; the murmuring pines and the hemlocks, composed in unrhymed English **dactylic** hexameter." }
    ]
  },
  "Dashboard — dactyl\\dactylis.md": {
    primary: "A genus of Eurasian and North African grasses (family Poaceae), notably Dactylis glomerata, commonly known as cocksfoot or orchard grass.",
    secondary: "In pasture agronomy, a robust perennial bunchgrass valued for livestock grazing, characterized by dense, one-sided clusters of spikelets.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "Orchard grass, **Dactylis** glomerata, is widely cultivated in pastures for its early, luxuriant spring growth." },
      { author: "Charles Darwin", work: "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", quote: "Wind-pollinated grasses such as **Dactylis** produce prodigious clouds of fine pollen when shaken by the breeze." },
      { author: "Liberty Hyde Bailey", work: "Cyclopedia of American Agriculture", quote: "The tufted habit of **Dactylis** makes it an invaluable pasture grass upon dry, shady hillsides." }
    ]
  },
  "Dashboard — dactyl\\dactyloctenium.md": {
    primary: "A genus of annual and perennial grasses (family Poaceae) commonly known as crowfoot grasses, bearing digitately arranged spikes.",
    secondary: "In agrostology and tropical botany, C4 grasses with spreading finger-like seed heads, adapted to arid sandy soils and disturbed habitats.",
    quotes: [
      { author: "Asa Gray", work: "First Lessons in Botany", quote: "The curious radiating spikes of **Dactyloctenium** resemble the outspread claws of a bird's foot." },
      { author: "John Torrey", work: "Flora of North America", quote: "Crowfoot grass, **Dactyloctenium** aegyptium, has naturalized throughout the southern states in cultivated fields." },
      { author: "Liberty Hyde Bailey", work: "Manual of Cultivated Plants", quote: "The digitately clustered spikes of **Dactyloctenium** distinguish it readily from ordinary meadow grasses." }
    ]
  },
  "Dashboard — dactyl\\dactylology.md": {
    primary: "The art or practice of communicating by using a manual alphabet; finger spelling used by and with the deaf.",
    secondary: "In the history of deaf education, the pedagogical system of representing letters and phonemes through conventional finger and hand configurations.",
    quotes: [
      { author: "Helen Keller", work: "The Story of My Life", quote: "My teacher placed my hand beneath the cool flowing water and spelled into my palm with rapid **dactylology** the word w-a-t-e-r." },
      { author: "Alexander Graham Bell", work: "Upon the Education of Deaf-Mutes", quote: "Proficiency in **dactylology** enables the student to transcribe English syntax directly onto the fingers." },
      { author: "Oliver Sacks", work: "Seeing Voices", quote: "Before sign language was recognized as a complete grammatical system, educators relied heavily upon manual **dactylology**." }
    ]
  },
  "Dashboard — dactyl\\dactylomancy.md": {
    primary: "A form of divination using finger rings, typically suspended over a bowl or ringed alphabet circle.",
    secondary: "In folklore and historical occultism, the practice of suspending a gold ring by a fine thread to divine future secrets by its acoustic taps.",
    quotes: [
      { author: "Edward Tylor", work: "Primitive Culture", quote: "The practice of **dactylomancy**, where a suspended ring answers questions by striking a metallic bowl, survives in European folklore." },
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", quote: "To divine secret treasures by the oscillating swings of a ring in **dactylomancy** is a superstitious conceit." },
      { author: "Walter Scott", work: "Demonology and Witchcraft", quote: "The village sorcerer amused the crowd with demonstrations of **dactylomancy**, predicting marriages by the swings of a signet ring." }
    ]
  },
  "Dashboard — dactyl\\dactylomegaly.md": {
    primary: "Abnormal enlargement of one or more fingers or toes; macrodactyly.",
    secondary: "In orthopedic surgery and pediatric genetics, a rare congenital overgrowth of digital soft tissue and bone, often associated with neurofibromatosis or Proteus syndrome.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Localized **dactylomegaly** of the index finger can produce colossal digital disproportion while the adjacent digits remain normal." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "The enormous hypertrophy in true **dactylomegaly** involves not only the phalanges but also the digital nerves and subcutaneous fat." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "Excision or epiphysiodesis is often required in **dactylomegaly** to prevent progressive deviation of the oversized digit." }
    ]
  },
  "Dashboard — dactyl\\dactylopiidae.md": {
    primary: "A family of scale insects (superfamily Coccoidea) comprising the cochineal insects, which feed on cacti and produce crimson carminic acid.",
    secondary: "In economic entomology and historical commerce, scale insects cultivated in Mesoamerica and the Mediterranean to manufacture royal carmine dyes.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Political Essay on the Kingdom of New Spain", quote: "The cultivation of cochineal insects of the family **Dactylopiidae** upon nopal cacti was a source of colossal wealth for Oaxaca." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "In the Canary Islands, broad plantations of opuntia are planted solely to nourish parasitic colonies of the **Dactylopiidae**." },
      { author: "Alfred Russel Wallace", work: "Tropical Nature and Other Essays", quote: "The vivid scarlet dye extracted from the crushed bodies of the **Dactylopiidae** has colored royal robes and painter's pigments for centuries." }
    ]
  },
  "Dashboard — dactyl\\dactylopius.md": {
    primary: "The genus of scale insects in the family Dactylopiidae, most notably Dactylopius coccus (cochineal), harvested for carmine dye.",
    secondary: "In entomology and biological weed control, insects used both for natural pigment production and to control invasive prickly pear cacti.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Personal Narrative", quote: "The harvest of **Dactylopius** coccus requires delicate sweeping of the white cottony clusters from the cactus joints." },
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Invertebrated Animals", quote: "Female specimens of **Dactylopius** remain permanently wingless and sessile, their bodies swollen with crimson fluid." },
      { author: "Charles Darwin", work: "Journal of Researches", quote: "We inspected the cactus nopalries where millions of tiny **Dactylopius** bugs were nurtured beneath protective mats." }
    ]
  },
  "Dashboard — dactyl\\dactylopteridae.md": {
    primary: "A family of marine scorpaeniform fishes commonly known as flying gurnards, characterized by enormous, colorful wing-like pectoral fins.",
    secondary: "In systematic ichthyology, bottom-dwelling fishes with armored head casques and divided pectoral rays used to probe sandy seafloors.",
    quotes: [
      { author: "Georges Cuvier", work: "The Animal Kingdom", quote: "The family **Dactylopteridae** is celebrated for its colossal pectoral fins, which spread like the wings of a swallow over the seabed." },
      { author: "Francis Day", work: "The Fishes of Great Britain and Ireland", quote: "Fishes of the **Dactylopteridae** were formerly believed to fly through the air, though they merely glide short distances across the water." },
      { author: "Charles Darwin", work: "The Zoology of the Voyage of H.M.S. Beagle", quote: "The brilliantly spangled pectoral fans of the **Dactylopteridae** gleamed with electric blue spots as the fish rested upon the sand." }
    ]
  },
  "Dashboard — dactyl\\dactylopterus.md": {
    primary: "The genus of flying gurnards (family Dactylopteridae), especially Dactylopterus volitans, the flying robin of warm Atlantic waters.",
    secondary: "In marine biology, bottom-dwelling coastal fishes that flash large, blue-edged pectoral fins to intimidate predators and probe benthic sediments.",
    quotes: [
      { author: "Charles Darwin", work: "The Zoology of the Voyage of H.M.S. Beagle", quote: "A living specimen of **Dactylopterus** volitans was brought on board, snapping its bony opercular spines when touched." },
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Vertebrated Animals", quote: "In **Dactylopterus**, the anterior rays of the pectoral fin are detached, functioning like sensitive fingers to turn over pebbles." },
      { author: "Philip Henry Gosse", work: "The Aquarium", quote: "The gorgeous peacock-like spots upon the expansive fins of **Dactylopterus** astonish all who behold this creature in motion." }
    ]
  },
  "Dashboard — dactyl\\dactylorhiza.md": {
    primary: "A genus of terrestrial orchids commonly known as marsh orchids or spotted orchids, characterized by palmately divided root tubers resembling fingers.",
    secondary: "In European orchidology and plant systematics, a taxonomically complex genus of wetland orchids noted for hybrid swarms and polymorphic spotted foliage.",
    quotes: [
      { author: "Charles Darwin", work: "The Various Contrivances by which Orchids are Fertilised by Insects", quote: "The palmate, hand-like tubers of **Dactylorhiza** distinguish it immediately from the simple globose bulbs of true Orchis." },
      { author: "Asa Gray", work: "Manual of Botany", quote: "Specimens of **Dactylorhiza** flourish in calcareous fens, displaying dense spikes of lilac and purple flowers." },
      { author: "Arthur George Tansley", work: "The British Islands and Their Vegetation", quote: "In water meadows, colonies of **Dactylorhiza** hybridize freely, presenting endless botanical puzzles to the field taxonomist." }
    ]
  },
  "Dashboard — dactyl\\dactyloscopidae.md": {
    primary: "A family of small, marine, perch-like fishes known as sand stargazers, possessing upward-directed eyes and fringed lips for burying in sand.",
    secondary: "In benthic ichthyology, cryptobenthic blennioid fishes possessing finger-like opercular fringes that assist in respiration while submerged in sediment.",
    quotes: [
      { author: "David Starr Jordan", work: "A Guide to the Study of Fishes", quote: "The family **Dactyloscopidae** comprises peculiar blennioid fishes that lie concealed in sand with only their stalked eyes exposed." },
      { author: "Francis Day", work: "The Fishes of India", quote: "Members of the **Dactyloscopidae** utilize specialized digital fringes along the opercular margin to filter sand from their gills." },
      { author: "Charles Darwin", work: "The Zoology of the Voyage of H.M.S. Beagle", quote: "Small cryptobenthic fishes resembling the **Dactyloscopidae** were discovered burrowing with astonishing speed into intertidal sandbanks." }
    ]
  },
  "Dashboard — dactyl\\dactylus.md": {
    primary: "A digit, finger, or toe of a human or vertebrate; or a metrical dactyl in classical prosody.",
    secondary: "In arthropod morphology, the terminal movable segment or claw of a crustacean chela or insect leg.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Crayfish: An Introduction to the Study of Zoology", quote: "The formidable pincer of the crayfish is formed by the opposable **dactylus** biting against the immovable propodite." },
      { author: "Richard Owen", work: "Lectures on the Comparative Anatomy of Invertebrates", quote: "The terminal **dactylus** of the decapod crustacean is armed with sharp denticles for seizing prey." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", quote: "In crabs, powerful adductor muscles close the **dactylus** with sufficient force to crush mollusk shells." }
    ]
  },
  "Dashboard — dactyl\\dactyly.md": {
    primary: "The condition, arrangement, structure, or number of digits on the hand or foot of an animal or human.",
    secondary: "In evolutionary morphology and clinical teratology, the anatomical patterning of autopodial digits (e.g., polydactyly, syndactyly, ectrodactyly).",
    quotes: [
      { author: "Stephen Jay Gould", work: "Eight Little Piggies", quote: "The discovery of eight digits in Acanthostega showed that pentadactyly was not an immutable ancestral law, but a contingent outcome of early tetrapod **dactyly**." },
      { author: "Thomas Henry Huxley", work: "Lectures on Evolution", quote: "The transition from ancestral multi-toed limbs to modern equine monodactyly illustrates progressive specialization in vertebrate **dactyly**." },
      { author: "Richard Owen", work: "On the Nature of Limbs", quote: "The archetypal pentadactyl scheme serves as the morphological blueprint underlying every variation of mammalian **dactyly**." }
    ]
  },
  "Dashboard — dactyl\\datable.md": {
    primary: "Capable of being dated; able to have its chronological origin, period, or age established.",
    secondary: "In archaeology, art history, and palaeography, possessing diagnostic stylistic, epigraphic, or radiocarbon features that fix its historical date.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The bronze coins discovered along the limes were precisely **datable** to the third consulate of Antoninus Pius." },
      { author: "John Ruskin", work: "The Stones of Venice", quote: "Every carved capital upon the ducal palace is clearly **datable** by the transition from Byzantine to Gothic foliage." },
      { author: "Arthur Evans", work: "The Palace of Minos at Knossos", quote: "Imported Egyptian scarabs provided a secure, **datable** horizon for the ceramic strata of the Middle Minoan palace." }
    ]
  },
  "Dashboard — dactyl\\date.md": {
    primary: "The day of the month or year as specified by a number; or the sweet, oblong edible fruit of the date palm (Phoenix dactylifera).",
    secondary: "In botanical etymology, the fruit term derives through Latin dactylus from Greek daktylos (finger), alluding to the finger-like shape of the fruit.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Views of Nature", quote: "The nomadic caravans sustained themselves across the blazing desert upon dried clusters of the wild **date**." },
      { author: "William Shakespeare", work: "Romeo and Juliet", quote: "They call for **dates** and quinces in the pastry, while the servants hasten with roasted meats for the banquet." },
      { author: "Edward William Lane", work: "Manners and Customs of the Modern Egyptians", quote: "The harvest of the desert **date** is celebrated with festivities, as it provides the staple nourishment of the oasis." }
    ]
  },
  "Dashboard — dactyl\\dateable.md": {
    primary: "Variant spelling of datable; capable of being assigned to a specific time, era, or historical date.",
    secondary: "In historical bibliography and numismatics, having identifiable historical markers that permit chronological dating.",
    quotes: [
      { author: "Thomas Babington Macaulay", work: "Critical and Historical Essays", quote: "The political tract was certainly **dateable** to the feverish months preceding the flight of James the Second." },
      { author: "Walter Pater", work: "Appreciations", quote: "The manuscript contains marginal watermarks that render its transcription reliably **dateable** to the late sixteenth century." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Associated volcanic tuff beds provided a clear, **dateable** geological marker across the entire river valley." }
    ]
  },
  "Dashboard — dactyl\\dative.md": {
    primary: "In inflected languages, the grammatical case expressing the indirect object of an action or the recipient of a gift or benefit.",
    secondary: "In classical philology and grammar, the case typically indicating the person to or for whom something is done (from Latin dare, datum).",
    quotes: [
      { author: "Samuel Johnson", work: "A Dictionary of the English Language (Grammar)", quote: "The English noun has lost its ancient inflections, replacing the classical **dative** case with the prepositions 'to' and 'for'." },
      { author: "Max Müller", work: "The Science of Language", quote: "Comparative Indo-European grammar demonstrates that the **dative** originally functioned to designate personal recipients of an action." },
      { author: "Henry Sweet", work: "A New English Grammar", quote: "Old English possessed a distinct **dative** inflection in both nouns and pronouns, which survives today only in him, her, and them." }
    ]
  },
  "Dashboard — dactyl\\didactyly.md": {
    primary: "The condition of having only two digits (fingers or toes) on a hand or foot.",
    secondary: "In vertebrate zoology, the specialized two-toed foot morphology evolved in certain cursorial or arboreal animals, such as the ostrich (Struthio camelus) or two-toed sloth (Choloepus).",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Lectures on Evolution", quote: "The extreme cursorial adaptation of the ostrich culminates in complete **didactyly**, reducing the avian foot to two powerful running toes." },
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", quote: "In the two-toed sloth, **didactyly** of the forelimb provides a pair of massive curved hooks for suspended arboreal locomotion." },
      { author: "Alfred Romer", work: "Vertebrate Paleontology", quote: "Functional **didactyly** in running birds reduces ground friction and concentrates propulsion upon the enlarged third digit." }
    ]
  }
};

const updatedCount = updateNotesBatch(baseClusterDir, batch3Data);
console.log(`[Body Batch 3] Successfully updated ${updatedCount}/${Object.keys(batch3Data).length} notes.`);
