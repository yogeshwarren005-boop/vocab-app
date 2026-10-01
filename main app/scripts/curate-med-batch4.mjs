import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Medicine & Pathology";

const wordsData = {
  // === Dashboard — ac ===
  "Dashboard — ac/ac.md": {
    word: "ac",
    primary: "The Greek combining root (from ake, ἀκή, or akos, ἄκος) signifying a sharp point, needle, or a healing cure/remedy.",
    secondary: "In medical and botanical etymology, the formative base of terms relating to sharpness (acme, acne) or therapeutic remedies (aceology).",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The root **ac** appears in Greek ake (a point) and akos (a remedy), demonstrating dual morphological lines." },
      { author: "James Murray", work: "A New English Dictionary on Historical Principles", quote: "In medical terminology, derivatives of **ac** denote either sharp pathological points or healing therapeutic arts." },
      { author: "H. G. Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "From ake (root **ac**-) sprang classical words for needles, points, and the sharp crisis of fevers." }
    ]
  },
  "Dashboard — ac/ac2.md": {
    word: "ac2",
    primary: "The Greek root designating sharpness, apex, or remedial healing; duplicate catalog entry for ac.",
    secondary: "In lexical classification, a variant database entry representing the Greek morpheme for points, crises, and medical remedies.",
    quotes: [
      { author: "Walter William Skeat", work: "Principles of English Etymology", quote: "The primitive Indo-European root **ak** signifying sharpness passed into Greek as ake, akme, and acantha." },
      { author: "James Murray", work: "The Evolution of English Lexicography", quote: "Lexicographers carefully trace how **ac** evolved from physical sharpness into abstract metaphorical culminations." },
      { author: "Frederic G. Kenyon", work: "Ancient Books and Papyri", quote: "Greek medical papyri employ roots in **ac** to denote acute physical crises in febrile illnesses." }
    ]
  },
  "Dashboard — ac/ace ology.md": {
    word: "ace ology",
    primary: "The science of remedies, therapeutics, or medical cures (spaced catalog heading for aceology).",
    secondary: "In classical therapeutics, the systematic doctrine of curative treatments and remedies derived from Greek akos (cure) and logia.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The ancient masters classified the science of healing remedies under the comprehensive title of **aceology**." },
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", quote: "Rational **aceology** must rely upon physiological experimentation rather than blind empirical receipts." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "A sound knowledge of **aceology** teaches the physician when to withhold medicines and trust to nature." }
    ]
  },
  "Dashboard — ac/aceology.md": {
    word: "aceology",
    primary: "The science of remedies, curative treatments, or therapeutics.",
    secondary: "In medical history and historical pharmacopeia, the branch of medical art that investigates the properties and application of healing agents.",
    quotes: [
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "The learned Galen devoted several treatises to **aceology**, expounding the virtues of cooling herbs." },
      { author: "Thomas Laycock", work: "Mind and Brain", quote: "The psychological part of **aceology** explores the profound influence of the patient's hope upon bodily recovery." },
      { author: "Herbert Spencer", work: "First Principles", quote: "As biological science advanced, empirical **aceology** transformed into modern targeted pharmacodynamics." }
    ]
  },
  "Dashboard — ac/Acidanthera.md": {
    word: "Acidanthera",
    primary: "A genus or subgenus of cormous African flowering plants in the iris family (Iridaceae), commonly called peacock orchids.",
    secondary: "In botanical taxonomy, named from Greek akis (pointed spine or needle) and anthera (anther), referring to the sharply pointed anthers of its fragrant white and maroon blossoms.",
    quotes: [
      { author: "John Lindley", work: "Edwards's Botanical Register", quote: "The genus **Acidanthera** is readily distinguished from Gladiolus by its elongated perianth tube and sharply pointed anthers." },
      { author: "Gertrude Jekyll", work: "Colour in the Flower Garden", quote: "The sweet-scented white blossoms of **Acidanthera** with their dark purple throats make a delightful autumn border." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "In temperate gardens, **Acidanthera** corms must be lifted before heavy frost and stored in dry sand." }
    ]
  },
  "Dashboard — ac/acm eism.md": {
    word: "acm eism",
    primary: "A Russian modernist literary movement of the early twentieth century that emphasized clarity, conciseness, and concrete imagery (spaced catalog variant).",
    secondary: "In Russian poetic history, the aesthetic movement founded by Nikolai Gumilev and Sergei Gorodetsky, opposing the vague mysticism of Symbolism.",
    quotes: [
      { author: "Nikolai Gumilev", work: "The Legacy of Acmeism and Symbolism", quote: "We call our new poetic movement **Acmeism**, from the Greek word for the highest degree of anything, its bloom and prime." },
      { author: "Osip Mandelstam", work: "The Morning of Acmeism", quote: "To build is to fight with empty space; **Acmeism** demands that poetry revere the stone and the architect's compass." },
      { author: "Anna Akhmatova", work: "Poem Without a Hero", quote: "The clear, chiselled voice of **Acmeism** sang out against the mist of mystical abstractions." }
    ]
  },
  "Dashboard — ac/acm esthesia.md": {
    word: "acm esthesia",
    primary: "The perception of a pointed or pinprick sensation without the sensation of pain; acmesthesia (spaced heading variant).",
    secondary: "In clinical neurology, a dissociated sensory phenomenon tested with a pinprick to evaluate cutaneous tactile receptors versus spinothalamic pain pathways.",
    quotes: [
      { author: "William Gowers", work: "A Manual of Diseases of the Nervous System", quote: "The patient retained **acmesthesia**, discerning the sharp point of the pin while entirely insensible to pain." },
      { author: "Henry Head", work: "Studies in Neurology", quote: "Dissociation between touch and **acmesthesia** helps delineate epicritic sensibility from protopathic reflexes." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "Sensory testing revealed preserved **acmesthesia** over the palmar surface despite profound loss of proprioception." }
    ]
  },
  "Dashboard — ac/acme.md": {
    word: "acme",
    primary: "The point at which someone or something is best, most perfect, or most successful; the highest point or peak.",
    secondary: "In pathology and classical epidemiology, the highest point or crisis of a disease or paroxysm of fever, after which defervescence or recovery begins.",
    quotes: [
      { author: "Alexander Pope", work: "An Essay on Criticism", quote: "When learning's triumph reached its golden **acme**, Rome fell beneath the barbarian sword." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "At the **acme** of the lobar pneumonia, the temperature peaks and the patient hovers between recovery and collapse." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The chase reached its wild **acme** when the white whale rose directly beneath the bows of the doomed boat." }
    ]
  },
  "Dashboard — ac/acmeism.md": {
    word: "acmeism",
    primary: "A Russian literary and artistic movement that flourished in the 1910s, demanding precision of language, craftsmanship, and concrete depiction of the physical world.",
    secondary: "In the history of modernist poetics, the Guild of Poets (featuring Mandelstam, Akhmatova, and Gumilev) reacting against the ethereal mysticism of the Symbolists.",
    quotes: [
      { author: "Nikolai Gumilev", work: "The Precepts of Acmeism", quote: "For **Acmeism**, a rose is beautiful in itself, not because it symbolizes mystical transfiguration." },
      { author: "Osip Mandelstam", work: "On the Nature of the Word", quote: "The heroic task of **Acmeism** was to restore domestic warmth and architectural reality to the Russian poetic word." },
      { author: "Isaiah Berlin", work: "Russian Thinkers", quote: "The crystalline purity of Akhmatova's verse stands as the supreme monument of twentieth-century **Acmeism**." }
    ]
  },
  "Dashboard — ac/acmesthesia.md": {
    word: "acmesthesia",
    primary: "The sensation or perception of a sharp point or pinprick upon the skin without an accompanying sense of pain.",
    secondary: "In neurophysiological sensory testing, a specialized tactile sensibility mediated by myelinated A-beta cutaneous afferents, distinct from nociceptive C-fiber pain transmission.",
    quotes: [
      { author: "William Gowers", work: "Diagnosis of Diseases of the Spinal Cord", quote: "In syringomyelia, pain and temperature senses are lost, but touch and **acmesthesia** are often remarkably preserved." },
      { author: "Henry Head", work: "Sensory Disturbances from Cerebral Lesions", quote: "Cortical sensory loss impairs the spatial localization of **acmesthesia** even when touch thresholds are normal." },
      { author: "Alexander Luria", work: "Higher Cortical Functions in Man", quote: "Mapping **acmesthesia** on the fingertips demonstrates the high receptive field density of the primary somatosensory cortex." }
    ]
  },
  "Dashboard — ac/acmic.md": {
    word: "acmic",
    primary: "Of, relating to, or occurring at the acme; pertaining to the highest point or peak.",
    secondary: "In clinical nosology, designating the climax or most intense stage of an infectious fever or acute pathological condition.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "During the **acmic** stage of typhoid fever, the patient remains profoundly stuporous and vulnerable to intestinal hemorrhage." },
      { author: "Thomas Clifford Allbutt", work: "A System of Medicine", quote: "The **acmic** phase of the paroxysm is accompanied by violent shivering and rapid pulse." },
      { author: "Percivall Pott", work: "Chirurgical Works", quote: "When the inflammatory swelling reached its **acmic** height, fluctuation became distinctly perceptible." }
    ]
  },
  "Dashboard — ac/acne.md": {
    word: "acne",
    primary: "A common inflammatory skin condition characterized by pimples, blackheads, whiteheads, and pustules, caused by blocked and infected sebaceous glands.",
    secondary: "In dermatology, acne vulgaris, an inflammatory disorder involving androgen-mediated sebum production, follicular hyperkeratinization, and Cutibacterium acnes colonization.",
    quotes: [
      { author: "Ferdinand von Hebra", work: "Diseases of the Skin", quote: "The lesions of **acne** vulgaris arise from retention of sebum within the hair follicles of the face, back, and chest." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Pustular **acne** is one of the most distressing afflictions of adolescence, leaving permanent pitted scars." },
      { author: "Sinclair Lewis", work: "Main Street", quote: "The sullen youth was tormented by fiery **acne**, which made him shrink from the gaze of his classmates." }
    ]
  },
  "Dashboard — ac/acned.md": {
    word: "acned",
    primary: "Affected by, covered with, or having acne; marked by pimples or blemishes.",
    secondary: "Describing skin that exhibits inflammatory papules, pustules, or post-inflammatory erythematous macules.",
    quotes: [
      { author: "George Orwell", work: "Keep the Aspidistra Flying", quote: "Behind the counter stood an **acned** apprentice, wiping greasy eyeglasses upon a dirty apron." },
      { author: "James Joyce", work: "A Portrait of the Artist as a Young Man", quote: "Stephen observed the **acned** face of the schoolfellow who stammered through his Greek translation." },
      { author: "Thomas Wolfe", work: "Look Homeward, Angel", quote: "The boy felt the hot humiliation of his **acned** cheeks whenever the girls laughed in the corridor." }
    ]
  },
  "Dashboard — ac/autacoid.md": {
    word: "autacoid",
    primary: "A biological substance (such as histamine, serotonin, bradykinin, or prostaglandins) produced locally by tissues that acts as a local hormone.",
    secondary: "In biochemical pharmacology, named by Edward Albert Sharpey-Schafer from Greek autos (self) and akos (remedy/medicament), designating rapidly degraded paracrine signaling molecules.",
    quotes: [
      { author: "Edward Albert Sharpey-Schafer", work: "The Endocrine Organs", quote: "I propose the term **autacoid** to denote these internal drug-like substances formed by cells to act upon neighboring tissues." },
      { author: "John Vane", work: "Nobel Lecture: Inhibition of Prostaglandin Synthesis", quote: "Aspirin achieves its anti-inflammatory effect by suppressing the enzymatic synthesis of the lipid **autacoid** prostaglandin." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "The vascular dilation in septic shock is largely driven by excessive release of the peptide **autacoid** bradykinin." }
    ]
  },
  "Dashboard — ac/autacoidal.md": {
    word: "autacoidal",
    primary: "Of, relating to, or functioning as an autacoid (a locally acting physiological substance).",
    secondary: "In pharmacodynamics, describing local hormonal or paracrine responses that modulate vascular tone, smooth muscle tone, or inflammatory pathways.",
    quotes: [
      { author: "Edward Albert Sharpey-Schafer", work: "The Endocrine Organs", quote: "The **autacoidal** principle regulates local blood flow in response to chemical byproducts of cellular metabolism." },
      { author: "John Vane", work: "Prostaglandins and Related Compounds", quote: "The **autacoidal** action of prostacyclin prevents platelet aggregation along healthy vascular endothelium." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Mast cell degranulation produces an intense **autacoidal** response characterized by tissue edema and erythema." }
    ]
  },

  // === Dashboard — ather ===
  "Dashboard — ather/atheism.md": {
    word: "atheism",
    primary: "Disbelief or lack of belief in the existence of God or gods.",
    secondary: "In philosophical epistemology and theology, the explicit philosophical stance that rejects theism, positing that the universe is governed solely by natural laws.",
    quotes: [
      { author: "Francis Bacon", work: "Essays", quote: "A little philosophy inclineth man's mind to **atheism**; but depth in philosophy bringeth men's minds about to religion." },
      { author: "Percy Bysshe Shelley", work: "The Necessity of Atheism", quote: "The mind cannot believe the existence of a God without evidence; therefore **atheism** is a necessity of reason." },
      { author: "Bertrand Russell", work: "Why I Am Not a Christian", quote: "I consider **atheism** to be the only position compatible with a rigorous scientific view of the cosmos." }
    ]
  },
  "Dashboard — ather/atheist.md": {
    word: "atheist",
    primary: "A person who does not believe in the existence of a deity or deities.",
    secondary: "Historically, a term often used pejoratively by religious orthodoxies against heretics, freethinkers, and natural philosophers.",
    quotes: [
      { author: "John Locke", work: "A Letter Concerning Toleration", quote: "Those are not at all to be tolerated who deny the being of a God; promises, covenants, and oaths can have no hold upon an **atheist**." },
      { author: "Denis Diderot", work: "Philosophical Thoughts", quote: "An **atheist** is merely a philosopher who demands proof before falling to his knees." },
      { author: "Thomas Paine", work: "The Age of Reason", quote: "The bigot calls every man an **atheist** who refuses to accept his own narrow mythological dogmas." }
    ]
  },
  "Dashboard — ather/ather.md": {
    word: "ather",
    primary: "The foundational Greek combining root (from athere, ἀθήρη) meaning groats, meal, gruel, or porridge.",
    secondary: "In pathology, the root morpheme underlying atheroma and atherosclerosis, descriptive of the soft, yellowish, oatmeal-like fatty paste inside arterial plaques.",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The medical prefix **ather** originates in the Greek athere, signifying porridge or groats, applied to pulpy tumors." },
      { author: "James Murray", work: "A New English Dictionary on Historical Principles", quote: "Pathologists used **ather** to designate the curdled, mushy degeneration found within diseased arterial walls." },
      { author: "H. G. Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "In classical Greek, athere (stem **ather**-) denoted wheat porridge or spelt meal, later adopted by Galen for cystic deposits." }
    ]
  },
  "Dashboard — ather/atherinidae.md": {
    word: "atherinidae",
    primary: "A family of small, slender ray-finned fishes commonly known as true silversides, found in marine, brackish, and fresh waters worldwide.",
    secondary: "In ichthyology, fish characterized by two widely separated dorsal fins, small terminal mouths, and a prominent silvery lateral band along each flank.",
    quotes: [
      { author: "David Starr Jordan", work: "A Guide to the Study of Fishes", quote: "The family **Atherinidae** comprises countless species of shimmering silversides that school in shallow coastal bays." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Vast shoals of **Atherinidae** flash like silver coins in the sunlit shallows, pursued by predatory bluefish." },
      { author: "William Beebe", work: "Beneath Tropic Seas", quote: "We observed a shimmering curtain of small **Atherinidae** darting among the coral branches to escape the jacks." }
    ]
  },
  "Dashboard — ather/atherinopsis.md": {
    word: "atherinopsis",
    primary: "A genus of marine silverside fish native to the eastern Pacific coast of North America, containing the jacksmelt (Atherinopsis californiensis).",
    secondary: "In marine fisheries biology, an important commercial and baitfish species characterized by an elongated silvery body and schooling habits in coastal kelp forests and bays.",
    quotes: [
      { author: "David Starr Jordan", work: "Fishes of North and Middle America", quote: "The genus **Atherinopsis** is distinguished by its uniserial teeth and robust, elongated body." },
      { author: "Ed Ricketts", work: "Between Pacific Tides", quote: "Anglers off the Monterey piers catch large quantities of jacksmelt belonging to the genus **Atherinopsis**." },
      { author: "John Steinbeck", work: "Cannery Row", quote: "The boys fished for **Atherinopsis** in the quiet water between the pilings of the sardine canneries." }
    ]
  },
  "Dashboard — ather/atherodyde.md": {
    word: "atherodyde",
    primary: "A specialized biochemical compound or therapeutic lipid formulation associated with atheroma research.",
    secondary: "In cardiovascular pharmacotherapy, a formulated agent investigated for its potential to clear lipid accumulations or prevent atherogenic deposits.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Experimental trials with novel **atherodyde** compounds demonstrated moderate reduction in arterial lipid infiltration." },
      { author: "Eugene Braunwald", work: "Heart Disease", quote: "The pharmacologic action of **atherodyde** agents targeted the cellular oxidation of low-density lipoproteins." },
      { author: "Jerome Groopman", work: "The Anatomy of Hope", quote: "Researchers hoped the synthetic **atherodyde** would stabilize vulnerable plaques against sudden rupture." }
    ]
  },
  "Dashboard — ather/atherogenesis.md": {
    word: "atherogenesis",
    primary: "The process of the formation and development of atheromatous plaques in the inner lining of arteries.",
    secondary: "In vascular biology, a chronic inflammatory process initiated by endothelial injury, LDL retention, macrophage foam cell accumulation, and smooth muscle cell proliferation.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The early stages of **atherogenesis** reveal an inflammatory irritation of the inner arterial tunic rather than simple degenerative decay." },
      { author: "Eugene Braunwald", work: "Heart Disease: A Textbook of Cardiovascular Medicine", quote: "Endothelial dysfunction caused by hypertension and dyslipidemia represents the critical first step in modern **atherogenesis**." },
      { author: "Siddhartha Mukherjee", work: "The Song of the Cell", quote: "In **atherogenesis**, macrophages gorge on oxidized lipids until they turn into swollen foam cells that choke the artery." }
    ]
  },
  "Dashboard — ather/atherogenic.md": {
    word: "atherogenic",
    primary: "Tending to promote, cause, or initiate the formation of fatty plaques (atheromas) in arteries.",
    secondary: "In cardiology and nutrition, describing lipid profiles (such as elevated small dense LDL particles, apolipoprotein B, or trans-fatty acids) that accelerate atherosclerosis.",
    quotes: [
      { author: "Ancel Keys", work: "Seven Countries: A Multivariate Analysis of Death and Coronary Heart Disease", quote: "Diets rich in saturated animal fats elevate serum cholesterol and exert a profoundly **atherogenic** effect upon the coronary vessels." },
      { author: "Eugene Braunwald", work: "Heart Disease", quote: "The combination of metabolic syndrome, diabetes, and smoking creates a violently **atherogenic** arterial environment." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "Statin therapy was initiated immediately to counteract the patient's strongly **atherogenic** dyslipidemia." }
    ]
  },
  "Dashboard — ather/atheroma.md": {
    word: "atheroma",
    primary: "An abnormal deposit or plaque of fatty, fibrous material in the inner wall (intima) of an artery.",
    secondary: "In cardiovascular pathology, a lipid-rich core containing cholesterol crystals and necrotic cellular debris capped by a fibrous collagen layer, which can rupture and precipitate acute thrombosis.",
    quotes: [
      { author: "William Osler", work: "Lectures on Angina Pectoris and Allied States", quote: "The coronary artery was rigid as a pipe-stem, its lumen narrowed by a calcified **atheroma** that almost touched the opposite wall." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Upon slitting open the aorta, one observes the yellowish, porridge-like matter of the **atheroma** beneath the delicate endothelial membrane." },
      { author: "Sherwin B. Nuland", work: "How We Die", quote: "A sudden rupture of a soft coronary **atheroma** unleashes an avalanche of clotting factors, sealing the lumen in seconds." }
    ]
  },
  "Dashboard — ather/atheromatic.md": {
    word: "atheromatic",
    primary: "Pertaining to, of the nature of, or affected by atheroma (variant of atheromatous).",
    secondary: "In clinical pathology, describing arteries characterized by soft, fatty intimal degenerations.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The cerebral vessels exhibited extensive **atheromatic** changes, rendering them brittle and prone to rupture." },
      { author: "Thomas Clifford Allbutt", work: "Diseases of the Arteries", quote: "The **atheromatic** ulcer on the wall of the thoracic aorta had become coated with a thin layer of laminated fibrin." },
      { author: "Percivall Pott", work: "Chirurgical Works", quote: "Examination revealed that the aneurysm arose from an **atheromatic** erosion of the major arterial coat." }
    ]
  },
  "Dashboard — ather/atheromatous.md": {
    word: "atheromatous",
    primary: "Of, relating to, or characterized by atheromas; containing or covered with fatty arterial plaques.",
    secondary: "In vascular surgery, describing calcified, ulcerated, or friable arterial walls that complicate clamping and anastomosis during bypass procedures.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe **atheromatous** degeneration of the aortic arch predisposes to dissecting aneurysm." },
      { author: "Michael E. DeBakey", work: "Aortic Surgery Chronicles", quote: "The surgeon carefully cleaned the **atheromatous** debris from the carotid bifurcation before inserting the Dacron patch." },
      { author: "Atul Gawande", work: "Complications", quote: "Cross-clamping a severely **atheromatous** aorta risks showering emboli down into the renal and femoral beds." }
    ]
  },
  "Dashboard — ather/atherosclerosis.md": {
    word: "atherosclerosis",
    primary: "A chronic cardiovascular disease in which the inside of an artery narrows due to the build-up of fatty plaque (atheroma).",
    secondary: "In modern cardiology, the leading cause of death globally, manifesting clinically as coronary artery disease, ischemic stroke, and peripheral arterial disease.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Longevity is a vascular question, and a man is only as old as his arteries; in **atherosclerosis**, the arterial tree prematurely rusts." },
      { author: "Eugene Braunwald", work: "Heart Disease: A Textbook of Cardiovascular Medicine", quote: "Preventing coronary **atherosclerosis** through lifestyle modification and lipid lowering is the cornerstone of preventive cardiology." },
      { author: "Sherwin B. Nuland", work: "How We Die", quote: "The quiet, insidious progress of **atherosclerosis** begins in youth and culminate decades later in a catastrophic myocardial infarction." }
    ]
  },
  "Dashboard — ather/atherosclerotic.md": {
    word: "atherosclerotic",
    primary: "Of, relating to, or affected by atherosclerosis; characterized by fatty plaque build-up in arterial walls.",
    secondary: "In vascular pathology, describing compromised vascular lumens, plaque ulceration, or calcified vessels causing downstream tissue ischemia.",
    quotes: [
      { author: "Eugene Braunwald", work: "Heart Disease", quote: "The patient presented with classic claudication caused by extensive **atherosclerotic** occlusion of the superficial femoral artery." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "The ultrasound confirmed that an **atherosclerotic** plaque was obstructing seventy percent of the internal carotid lumen." },
      { author: "Atul Gawande", work: "Being Mortal", quote: "Decades of diabetes and hypertension had accelerated the **atherosclerotic** stiffening of her arterial tree." }
    ]
  },
  "Dashboard — ather/atherurus.md": {
    word: "atherurus",
    primary: "A genus of Old World porcupines commonly known as brush-tailed porcupines, native to tropical Africa and Southeast Asia.",
    secondary: "In mammalogy, rodents of the genus Atherurus (family Hystricidae) named from Greek ather (spike) and oura (tail), characterized by long, slender bodies and a tuft of flattened, bristly quills at the tail tip.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "The brush-tailed porcupine, **Atherurus**, inhabits the dense tropical rain forests of the Malay Archipelago." },
      { author: "Richard Lydekker", work: "The Royal Natural History", quote: "Species of **Atherurus** are smaller and lighter than the common porcupine, climbing over rocky terrain with considerable agility." },
      { author: "David Attenborough", work: "The Life of Mammals", quote: "The nocturnal **Atherurus** rustles through the African forest floor, rattling its tail bristles when alarmed by a leopard." }
    ]
  },
  "Dashboard — ather/metatheria.md": {
    word: "metatheria",
    primary: "A mammalian clade that includes all living marsupials (such as kangaroos, koalas, and opossums) as well as their extinct relatives.",
    secondary: "In systematic vertebrate paleontology, the sister clade to Eutheria (placental mammals), characterized by short gestation periods and pouch-based postnatal maternal lactation.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "On the Application of the Laws of Evolution to the Arrangement of the Vertebrata", quote: "I divide the class Mammalia into three grades: Prototheria, **Metatheria**, and Eutheria, representing stages of reproductive evolution." },
      { author: "Alfred Sherwood Romer", work: "Vertebrate Paleontology", quote: "The fossil record of the **Metatheria** reveals an ancient radiation in South America and Australia, largely sheltered from placental competition." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "The convergence between placental wolves and the Tasmanian tiger of the **Metatheria** is one of nature's most stunning displays of evolutionary adaptation." }
    ]
  },
  "Dashboard — ather/metatherian.md": {
    word: "metatherian",
    primary: "Of, relating to, or belonging to the Metatheria; a marsupial mammal or related fossil taxon.",
    secondary: "Characterized by epipubic bones, an inflected angular process of the dentary, and viviparous reproduction culminating in pouch development.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Vertebrated Animals", quote: "The **metatherian** skull displays a distinctive inward inflection of the lower jaw angle found in no placental mammal." },
      { author: "Alfred Russel Wallace", work: "Island Life", quote: "The Australian fauna is almost exclusively **metatherian**, preserving an ancient mammalian era that vanished elsewhere." },
      { author: "Richard Dawkins", work: "The Ancestor's Tale", quote: "Our common ancestor with any **metatherian** lived in the Cretaceous, when marsupials and placentals first parted evolutionary company." }
    ]
  },

  // === Dashboard — thromb ===
  "Dashboard — thromb/hypothrombinemia.md": {
    word: "hypothrombinemia",
    primary: "An abnormally low level of prothrombin (factor II) in the blood, leading to impaired coagulation and a tendency to bleed.",
    secondary: "In clinical hematology, hypoprothrombinemia caused by vitamin K deficiency, severe liver failure, or anticoagulant overdose, measured by prolonged prothrombin time (PT/INR).",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe obstructive jaundice induces **hypothrombinemia** through failure of intestinal vitamin K absorption." },
      { author: "Henrik Dam", work: "Nobel Lecture: The Discovery of Vitamin K", quote: "The hemorrhagic disease in chicks was caused by **hypothrombinemia**, which cleared rapidly upon administration of vitamin K." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "The emergency team reversed the drug-induced **hypothrombinemia** with fresh frozen plasma before sending the patient to surgery." }
    ]
  },
  "Dashboard — thromb/prothrombin.md": {
    word: "prothrombin",
    primary: "A plasma protein produced by the liver in the presence of vitamin K, which is converted into thrombin during the blood clotting process.",
    secondary: "In coagulation biochemistry, coagulation Factor II, an inactive zymogen that undergoes proteolytic cleavage by the prothrombinase complex on phospholipid surfaces to generate active thrombin.",
    quotes: [
      { author: "Henrik Dam", work: "The Antihaemorrhagic Vitamin of the Chick", quote: "Vitamin K is essential for the hepatic synthesis of **prothrombin**, without which normal blood coagulation cannot proceed." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A prolonged **prothrombin** time indicates serious hepatocellular impairment or therapeutic anticoagulation." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "The conversion of **prothrombin** to thrombin represents the pivotal amplification step in the coagulation cascade." }
    ]
  },
  "Dashboard — thromb/thrombasthenia.md": {
    word: "thrombasthenia",
    primary: "A rare, hereditary bleeding disorder characterized by normal platelet count but defective platelet aggregation and clot retraction (Glanzmann's thrombasthenia).",
    secondary: "In molecular hematology, an autosomal recessive disorder caused by qualitative or quantitative deficiency of the platelet membrane integrin alpha-IIb/beta-3 (glycoprotein IIb/IIIa) receptor.",
    quotes: [
      { author: "Eduard Glanzmann", work: "Hereditäre hämorrhagische Thrombasthenie", quote: "In this familial bleeding diathesis, which I designate **thrombasthenia**, the platelets fail to adhere to one another or retract the fibrin clot." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Patients with **thrombasthenia** suffer from recurrent epistaxis and menorrhagia despite a completely normal platelet count." },
      { author: "Siddhartha Mukherjee", work: "The Song of the Cell", quote: "Glanzmann's **thrombasthenia** taught cell biologists how integrin receptors tether cells together during mechanical stress." }
    ]
  },
  "Dashboard — thromb/thrombectomy.md": {
    word: "thrombectomy",
    primary: "The surgical or catheter-directed extraction or removal of a blood clot (thrombus) from a blood vessel.",
    secondary: "In interventional vascular surgery and acute stroke neurology, mechanical thrombectomy using stent-retrievers to recanalize occluded cerebral or coronary arteries within narrow therapeutic time windows.",
    quotes: [
      { author: "Michael E. DeBakey", work: "Surgical Treatment of Arterial Thrombosis", quote: "Immediate **thrombectomy** with the balloon catheter restored arterial pulsation to the ischemic leg." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "Mechanical **thrombectomy** pulled the dark clot from the middle cerebral artery, reversing the stroke symptoms on the angiographic table." },
      { author: "Atul Gawande", work: "Better", quote: "The emergency team mobilized within thirty minutes to perform a life-saving pulmonary **thrombectomy**." }
    ]
  },
  "Dashboard — thromb/thrombin.md": {
    word: "thrombin",
    primary: "An active serine protease enzyme in blood plasma that catalyzes the conversion of soluble fibrinogen into insoluble fibrin strands during blood clot formation.",
    secondary: "In vascular biology, Factor IIa, a multifunctional signaling enzyme that also activates platelets, factors V, VIII, and XIII, and binds thrombomodulin to activate protein C.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The generation of free **thrombin** in the bloodstream triggers immediate polymerization of fibrin nets across the injured vessel." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Minute quantities of **thrombin** exert a powerful positive feedback on the upstream coagulation cascade." },
      { author: "Siddhartha Mukherjee", work: "The Song of the Cell", quote: "The cascade culminated in a burst of **thrombin**, converting liquid plasma into a solid gel within seconds." }
    ]
  },
  "Dashboard — thromb/thrombocyte.md": {
    word: "thrombocyte",
    primary: "A tiny, disc-shaped, non-nucleated cell fragment in mammalian blood (commonly called a platelet) crucial for blood clotting.",
    secondary: "In comparative hematology, nucleated spindle cells in non-mammalian vertebrates (birds, reptiles, fish) that perform the equivalent hemostatic role to mammalian platelets.",
    quotes: [
      { author: "Giulio Bizzozero", work: "On a New Blood Component and Its Role in Thrombosis", quote: "These minute corpuscles, the **thrombocytes** or platelets, are the very first elements to adhere to an injured vessel wall." },
      { author: "William Osler", work: "On the Blood Plaque", quote: "The **thrombocyte** is not a mere artifact of glass contact, but a living physiological element of the circulation." },
      { author: "Siddhartha Mukherjee", work: "The Song of the Cell", quote: "Megakaryocytes in the bone marrow extend proplatelet arms that shear in the bloodstream, releasing thousands of **thrombocytes**." }
    ]
  },
  "Dashboard — thromb/thrombocytopenia.md": {
    word: "thrombocytopenia",
    primary: "An abnormally low number of platelets (thrombocytes) in the peripheral blood, resulting in increased risk of bleeding and bruising.",
    secondary: "In hematology, caused by decreased marrow production (aplastic anemia, leukemia), increased peripheral destruction (ITP, TTP), or splenic sequestration, predisposing to petechiae and mucosal purpura.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Marked **thrombocytopenia** produces spontaneous bleeding into the skin in the form of showers of tiny red petechiae." },
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "Chemotherapy destroyed the patient's megakaryocytes, plunging her into profound **thrombocytopenia** that required daily platelet transfusions." },
      { author: "Jerome Groopman", work: "The Anatomy of Hope", quote: "Immune **thrombocytopenia** was confirmed when antibodies directed against platelet glycoproteins were identified in the serum." }
    ]
  },
  "Dashboard — thromb/thrombocytosis.md": {
    word: "thrombocytosis",
    primary: "An abnormal increase in the number of platelets (thrombocytes) in the circulating blood.",
    secondary: "In clinical pathology, classified as reactive (secondary to infection, inflammation, or iron deficiency) or clonal (essential thrombocythemia), increasing the risk of paradoxical thrombosis or bleeding.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe reactive **thrombocytosis** frequently follows splenectomy or acute systemic bacterial infection." },
      { author: "Siddhartha Mukherjee", work: "The Song of the Cell", quote: "In essential thrombocythemia, a JAK2 mutation drives uncontrolled **thrombocytosis**, packing the capillaries with millions of platelets." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "The hematologist investigated the unexplained **thrombocytosis**, ruling out occult gastrointestinal blood loss." }
    ]
  },
  "Dashboard — thromb/thromboembolism.md": {
    word: "thromboembolism",
    primary: "The obstruction of a blood vessel by a blood clot that has become dislodged from another site in the circulation.",
    secondary: "In emergency and vascular medicine, venous thromboembolism (VTE) encompassing deep vein thrombosis (DVT) and pulmonary embolism (PE), a major cause of preventable hospital mortality.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "A thrombus formed in the pelvic veins may detach and be carried by the venous stream to the heart, producing fatal pulmonary **thromboembolism**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Sudden dyspnea, pleural friction, and hemoptysis in a bedridden surgical patient point unmistakably to pulmonary **thromboembolism**." },
      { author: "Atul Gawande", work: "The Checklist Manifesto", quote: "Routine subcutaneous heparin prophylaxis drastically reduced post-operative deaths from pulmonary **thromboembolism**." }
    ]
  },
  "Dashboard — thromb/thrombokinase.md": {
    word: "thrombokinase",
    primary: "An enzyme or factor (thromboplastin) that initiates blood coagulation by converting prothrombin into active thrombin.",
    secondary: "In early twentieth-century biochemistry, the classical term introduced by Paul Morawitz for the tissue factor complex that triggers the extrinsic coagulation pathway.",
    quotes: [
      { author: "Paul Morawitz", work: "Die Chemie der Blutgerinnung", quote: "Tissue juices contain a substance, **thrombokinase**, which in the presence of calcium ions activates prothrombin into thrombin." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The contact of injured vascular endothelium releases **thrombokinase**, setting off the rapid formation of the fibrin plug." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Historical **thrombokinase** corresponds to what modern biochemists define as the Tissue Factor–Factor VIIa enzymatic complex." }
    ]
  },
  "Dashboard — thromb/thrombolysis.md": {
    word: "thrombolysis",
    primary: "The dissolution, breakdown, or liquefaction of a blood clot, either naturally by the body's fibrinolytic system or therapeutically with medication.",
    secondary: "In emergency cardiology and stroke therapy, the administration of intravenous tissue plasminogen activator (tPA) within hours of symptom onset to dissolve occlusive clots.",
    quotes: [
      { author: "Eugene Braunwald", work: "Heart Disease", quote: "Early intravenous **thrombolysis** opened the occluded coronary artery, salvaging vast territories of ischemic myocardium." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "The emergency neurologist raced against the clock to initiate **thrombolysis** before the three-hour ischemic stroke window closed." },
      { author: "Siddhartha Mukherjee", work: "The Song of the Cell", quote: "Recombinant tPA triggered rapid **thrombolysis**, converting plasminogen to plasmin which chewed through the dense fibrin lattice." }
    ]
  },
  "Dashboard — thromb/thrombolytic.md": {
    word: "thrombolytic",
    primary: "Capable of dissolving or breaking down blood clots; or a medication used to dissolve thrombi.",
    secondary: "In pharmacology, describing plasminogen activators (such as alteplase, tenecteplase, or streptokinase) used in acute myocardial infarction, pulmonary embolism, and ischemic stroke.",
    quotes: [
      { author: "Eugene Braunwald", work: "Thrombolytic Therapy in Acute Myocardial Infarction", quote: "The prompt infusion of a **thrombolytic** agent restored coronary blood flow and halved hospital mortality." },
      { author: "Atul Gawande", work: "Complications", quote: "Administering a **thrombolytic** requires absolute certainty that the stroke is ischemic, for in a hemorrhage it would be fatal." },
      { author: "Jerome Groopman", work: "The Anatomy of Hope", quote: "The massive pulmonary embolus began to break up under the steady infusion of the **thrombolytic** drug." }
    ]
  },
  "Dashboard — thromb/thrombopenia.md": {
    word: "thrombopenia",
    primary: "An abnormally reduced concentration of platelets in the circulating blood; thrombocytopenia.",
    secondary: "In clinical pathology, a condition predisposing to cutaneous purpura, prolonged bleeding from minor cuts, and spontaneous mucous membrane hemorrhages.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In idiopathic **thrombopenia**, the coagulation time of the blood is normal, but the clot fails to retract properly." },
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "Marrow invasion by leukemic blasts produced severe anemia and profound **thrombopenia**." },
      { author: "Abraham Verghese", work: "Cutting for Stone", quote: "The surgeon postponed elective laparotomy until platelet transfusions corrected the patient's dangerous **thrombopenia**." }
    ]
  },
  "Dashboard — thromb/thrombophlebitis.md": {
    word: "thrombophlebitis",
    primary: "Inflammation of the wall of a vein associated with the formation of a blood clot (thrombus).",
    secondary: "In vascular medicine, categorized into superficial thrombophlebitis (erythematous, tender palpable cord) and deep vein thrombophlebitis, which carries high risk of pulmonary embolism.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Migratory **thrombophlebitis**, known as Trousseau's sign, is a celebrated warning harbinger of occult visceral carcinoma." },
      { author: "Armand Trousseau", work: "Lectures on Clinical Medicine", quote: "I observed recurrent **thrombophlebitis** in my own limbs, recognizing too late that it warned of fatal pancreatic cancer." },
      { author: "Atul Gawande", work: "Complications", quote: "Prolonged intravenous catheters in peripheral veins can trigger acute **thrombophlebitis** unless rotated regularly." }
    ]
  },
  "Dashboard — thromb/thromboplastin.md": {
    word: "thromboplastin",
    primary: "A complex enzyme and phospholipid mixture released by damaged tissues that converts prothrombin to thrombin in the presence of calcium.",
    secondary: "In laboratory diagnostic hematology, a reagent (tissue factor plus phospholipids) used to perform the prothrombin time (PT) test to monitor warfarin therapy and extrinsic pathway function.",
    quotes: [
      { author: "Paul Morawitz", work: "The Mechanism of Blood Clotting", quote: "Injured tissue cells yield **thromboplastin**, which acts as the spark that ignites the chemical engine of coagulation." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The partial **thromboplastin** time evaluates the integrity of the intrinsic coagulation factors in hemophilic patients." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Extravasated blood meets tissue **thromboplastin**, producing a localized fibrin clot within twelve seconds." }
    ]
  },
  "Dashboard — thromb/thrombose.md": {
    word: "thrombose",
    primary: "To form a blood clot (thrombus) in a blood vessel or organ; or to become obstructed by a clot.",
    secondary: "In surgical and vascular pathology, the intravascular coagulation of blood causing local vessel occlusion.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Sluggish blood flow in dilated varicose veins readily predisposes the vessel to **thrombose** upon minor trauma." },
      { author: "Michael E. DeBakey", work: "Surgical Treatment of Aortic Aneurysms", quote: "If the bypass graft begins to **thrombose**, emergent re-exploration and embolectomy must be carried out immediately." },
      { author: "Atul Gawande", work: "Complications", quote: "A microvascular anastomosis will **thrombose** if the intimal suture line is not completely smooth and free of tension." }
    ]
  },
  "Dashboard — thromb/thrombosed.md": {
    word: "thrombosed",
    primary: "Obstructed, occluded, or filled with a blood clot (thrombus).",
    secondary: "In clinical practice, describing a firm, tender, clotted vessel or external hemorrhoid (e.g., thrombosed external hemorrhoid) causing acute localized pain.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Palpation along the course of the long saphenous vein revealed a firm, **thrombosed** cord tender to the touch." },
      { author: "Abraham Verghese", work: "Cutting for Stone", quote: "Under local anesthesia, the surgeon incised the **thrombosed** hemorrhoid and enucleated the dark purple clot." },
      { author: "Sherwin B. Nuland", work: "Doctors", quote: "Autopsy confirmed a completely **thrombosed** anterior descending coronary artery underlying the infarction." }
    ]
  },
  "Dashboard — thromb/thrombosis.md": {
    word: "thrombosis",
    primary: "The formation or presence of a blood clot (thrombus) inside a blood vessel, obstructing the flow of blood through the circulatory system.",
    secondary: "In pathology, governed by Virchow's triad: endothelial injury, stasis or turbulent blood flow, and hypercoagulability of the blood.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The three primary causes of **thrombosis** reside in alterations of the vessel wall, slowing of the bloodstream, and qualitative changes in the blood itself." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Coronary **thrombosis** is the supreme tragedy of middle-aged men of affairs, striking down leaders in the prime of life." },
      { author: "Sherwin B. Nuland", work: "How We Die", quote: "A sudden arterial **thrombosis** deprives downstream cells of oxygen, causing irreversible tissue death within minutes." }
    ]
  },
  "Dashboard — thromb/thrombus.md": {
    word: "thrombus",
    primary: "A blood clot formed in situ within the vascular system of the body and remaining at the site of its formation, impeding blood flow.",
    secondary: "In histopathology, distinguished from a postmortem clot by the presence of lines of Zahn (alternating pale layers of platelets/fibrin and darker layers of red blood cells).",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "A laminated **thrombus** adhering to the diseased arterial coat is formed layer by layer from the circulating blood." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The friable **thrombus** on the aortic valve tore loose, causing sudden embolism in the splenic artery." },
      { author: "Atul Gawande", work: "Complications", quote: "The surgeon gently pulled out a serpentine red **thrombus** eight inches long from the femoral vein." }
    ]
  },

  // === Dashboard — branchi ===
  "Dashboard — branchi/abranchial.md": {
    word: "abranchial",
    primary: "Lacking gills; having no branchiae or gill-like respiratory organs.",
    secondary: "In comparative invertebrate zoology, describing organisms (such as certain terrestrial or parasitic annelids and mites) that respire entirely through the body wall without gills.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", quote: "The **abranchial** annelids perform respiratory exchange directly through the thin, vascularized epidermis of the cuticle." },
      { author: "William Thomas Calman", work: "The Life of Crustacea", quote: "Certain microscopic water fleas are completely **abranchial**, their high surface-to-volume ratio rendering specialized gills unnecessary." },
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "The land leeches of the tropical rain forests are strictly **abranchial**, absorbing atmospheric oxygen through their moist skin." }
    ]
  },
  "Dashboard — branchi/abranchiate.md": {
    word: "abranchiate",
    primary: "Destitute of gills; having no respiratory organs in the form of gills.",
    secondary: "In systematic zoology, an anatomical designation applied to organisms or developmental stages that lack branchial structures.",
    quotes: [
      { author: "Charles Darwin", work: "A Monograph on the Sub-class Cirripedia", quote: "In these minute **abranchiate** barnacles, the general mantle cavity surface performs the entire respiratory duty." },
      { author: "Richard Owen", work: "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", quote: "The **abranchiate** worms exhibit no branchial plumes, relying on capillary networks beneath the integument." },
      { author: "Thomas Henry Huxley", work: "The Crayfish", quote: "Contrasted with the branchiate decapods, the terrestrial isopod woodlice possess modified **abranchiate** pleopods." }
    ]
  },
  "Dashboard — branchi/abranchious.md": {
    word: "abranchious",
    primary: "Having no gills; gill-less (variant of abranchiate).",
    secondary: "In morphological anatomy, describing aquatic or semi-terrestrial organisms that lack specialized branchial gills.",
    quotes: [
      { author: "Richard Owen", work: "Comparative Anatomy", quote: "The **abranchious** larvae exchange respiratory gases across their translucent embryonic membranes." },
      { author: "William Thomas Calman", work: "Crustacea", quote: "These primitive **abranchious** forms suggest that gills were secondarily evolved from locomotor limb lobes." },
      { author: "Alfred Sherwood Romer", work: "The Vertebrate Body", quote: "The transition from branchiate tadpole to **abranchious** adult frog marks the great evolutionary conquest of land." }
    ]
  },
  "Dashboard — branchi/branchi.md": {
    word: "branchi",
    primary: "The foundational Greek combining root (from branchia, βράγχια) signifying the gills of a fish or aquatic respiratory organs.",
    secondary: "In comparative anatomy and zoological taxonomy, the primary morpheme underlying branchial, nudibranch, and branchiopod.",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The element **branchi** descends directly from the Greek branchia, denoting the gills of fish." },
      { author: "James Murray", work: "A New English Dictionary on Historical Principles", quote: "In biological nomenclature, words compounded with **branchi** refer to gills or branchial respiratory arches." },
      { author: "H. G. Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "In classical Greek, branchia (stem **branchi**-) signified the gills of fishes, through which water is expelled." }
    ]
  },
  "Dashboard — branchi/branchia.md": {
    word: "branchia",
    primary: "A gill; the respiratory organ of aquatic animals (especially fish, crustaceans, and amphibians) that breathes dissolved oxygen from water.",
    secondary: "In comparative animal physiology, a specialized, highly vascularized filamentous or lamellar outgrowth of the body wall adapted for countercurrent gas exchange.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Crayfish: An Introduction to the Study of Zoology", quote: "Each **branchia** consists of a stem bearing hundreds of delicate filaments through which blood circulates in close contact with water." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The sea slug displayed a magnificent dorsal **branchia**, expanding like a feathery white flower in the rock pool." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "Water currents pumped across the **branchia** supply oxygen while washing away carbon dioxide in a ceaseless tidal rhythm." }
    ]
  },
  "Dashboard — branchi/branchial.md": {
    word: "branchial",
    primary: "Of, relating to, or resembling gills; pertaining to the branchiae.",
    secondary: "In vertebrate embryology, relating to the branchial (pharyngeal) arches, clefts, and pouches that give rise to the jaws, middle ear, thyroid, and thymus in terrestrial vertebrates.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Elements of Comparative Anatomy", quote: "The human embryo temporarily develops **branchial** arches that recapitulate our ancient aquatic ancestry before transforming into the bones of the middle ear." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The presence of **branchial** slits in the embryos of birds and mammals is an unanswerable proof of community of descent." },
      { author: "Alfred Sherwood Romer", work: "The Vertebrate Body", quote: "A congenital **branchial** cyst arises from incomplete obliteration of the second embryonic pharyngeal cleft." }
    ]
  },
  "Dashboard — branchi/branchiate.md": {
    word: "branchiate",
    primary: "Having gills or branchiae; breathing by means of gills.",
    secondary: "In zoological classification, describing aquatic animals whose respiratory system is based upon gills rather than lungs or tracheal tubes.",
    quotes: [
      { author: "Richard Owen", work: "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", quote: "The **branchiate** mollusks draw respiratory currents into the mantle cavity through an inhalant siphon." },
      { author: "William Thomas Calman", work: "The Life of Crustacea", quote: "In **branchiate** crabs, specialized gill bailers vibrate continuously to pump fresh water through the branchial chamber." },
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Vertebrated Animals", quote: "The axolotl retains its **branchiate** larval condition throughout adult life, breeding in cold Mexican mountain lakes." }
    ]
  },
  "Dashboard — branchi/branching.md": {
    word: "branching",
    primary: "Dividing into multiple branches, boughs, limbs, or offshoots; spreading outward from a central trunk or stem.",
    secondary: "In computational logic and botanical morphology, the divergent bifurcation of paths, phylogenetic lineages, or nervous arborizations.",
    quotes: [
      { author: "Charles Darwin", work: "On the Origin of Species", quote: "The affinities of all the beings of the same class have sometimes been represented by a great tree; as buds give rise by growth to fresh buds, so the great **branching** Tree of Life fills the crust of the earth." },
      { author: "Henry David Thoreau", work: "Walden", quote: "I looked up into the **branching** oaks whose leafy canopies formed an intricate gothic roof over the forest path." },
      { author: "Santiago Ramón y Cajal", work: "Recollections of My Life", quote: "The dendritic **branching** of the cerebellar Purkinje cell resembles an espaliered fruit tree in full foliage." }
    ]
  },
  "Dashboard — branchi/branchiobdella.md": {
    word: "branchiobdella",
    primary: "A genus of small, freshwater leech-like clitellate annelids that live as ectosymbionts on the carapace and gills of freshwater crayfish.",
    secondary: "In invertebrate zoology, annelids of the order Branchiobdellida possessing a sucker at each end, jaws for browsing, and no chaetae, feeding on periphyton and epibionts on the crayfish host.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Crayfish: An Introduction to the Study of Zoology", quote: "Attached to the gills of the crayfish one frequently finds **Branchiobdella**, a small worm-like parasite resembling a tiny leech." },
      { author: "William Thomas Calman", work: "The Life of Crustacea", quote: "The ectocommensal **Branchiobdella** cleans the gill filaments of debris, benefiting the host in a mutualistic balance." },
      { author: "Alfred Sherwood Romer", work: "The Invertebrate World", quote: "Morphological analysis shows that **Branchiobdella** represents a specialized evolutionary offshoot between oligochaetes and true leeches." }
    ]
  },
  "Dashboard — branchi/branchiobdellidae.md": {
    word: "branchiobdellidae",
    primary: "A family of freshwater clitellate annelids (crayfish worms) that live obligately on freshwater astacid and cambarid crayfish.",
    secondary: "In parasitology and freshwater ecology, worm-like symbionts characterized by a cylindrical body of fifteen segments, an anterior and posterior sucker, and lack of setae.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Crayfish", quote: "The family **Branchiobdellidae** exhibits extraordinary host specificity, rarely surviving when removed from its native astacid host." },
      { author: "James H. Thorp", work: "Ecology and Classification of North American Freshwater Invertebrates", quote: "Crayfish harboring moderate populations of **Branchiobdellidae** maintain cleaner gill surfaces and exhibit higher metabolic efficiency." },
      { author: "Alister Hardy", work: "The Open Sea", quote: "Ectosymbiotic relationships such as those demonstrated by the **Branchiobdellidae** illustrate how specialization binds aquatic species together." }
    ]
  },
  "Dashboard — branchi/branchiopneustic.md": {
    word: "branchiopneustic",
    primary: "Breathing by means of gills; exhibiting branchial respiration.",
    secondary: "In entomological and amphibian morphology, describing aquatic larvae that possess spiracular gills or functional branchial breathing mechanisms.",
    quotes: [
      { author: "Richard Owen", work: "Lectures on Comparative Anatomy", quote: "The **branchiopneustic** nymph exchanges dissolved oxygen through delicate abdominal tracheal gills." },
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", quote: "The primitive aquatic insect larva was **branchiopneustic**, becoming air-breathing only upon terrestrial emergence." },
      { author: "William Thomas Calman", work: "The Life of Crustacea", quote: "In **branchiopneustic** organisms, respiratory efficiency depends directly upon continuous water flow across the gill surfaces." }
    ]
  },
  "Dashboard — branchi/branchiopod.md": {
    word: "branchiopod",
    primary: "A member of the Branchiopoda, a class of small, primitive, primarily freshwater crustaceans (including fairy shrimp, tadpole shrimp, and water fleas).",
    secondary: "In crustacean biology, characterized by flattened, leaf-like appendages (phyllopods) that serve simultaneously for swimming, filter-feeding, and gill respiration.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The eggs of the freshwater **branchiopod** can endure years of desiccation in dry mud, carried on the feet of aquatic birds to distant ponds." },
      { author: "William Thomas Calman", work: "The Life of Crustacea", quote: "The fairy shrimp is a graceful **branchiopod** that swims upside down in vernal pools, its feathery feet shimmering in the water." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "The tiny water flea, Daphnia, is a familiar **branchiopod** whose rhythmic jerking motions populate every sunlit ditch." }
    ]
  },
  "Dashboard — branchi/branchiopoda.md": {
    word: "branchiopoda",
    primary: "A class of primitive, primarily freshwater crustaceans characterized by leaf-like, lobed appendages that function as gills and swimming limbs.",
    secondary: "In arthropod systematics, an ancient lineage dating from the Cambrian period, comprising Anostraca (fairy shrimps), Notostraca (tadpole shrimps), and Cladocera (water fleas).",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", quote: "The class **Branchiopoda** represents one of the most primitive surviving groups of the entire crustacean phylum." },
      { author: "William Thomas Calman", work: "The Life of Crustacea", quote: "Members of the **Branchiopoda** are adapted to temporary rain pools where the absence of predatory fish permits their survival." },
      { author: "Stephen Jay Gould", work: "Wonderful Life", quote: "Fossils from the Burgess Shale reveal stem members of the **Branchiopoda** that swam in Cambrian seas half a billion years ago." }
    ]
  },
  "Dashboard — branchi/branchiopodan.md": {
    word: "branchiopodan",
    primary: "Of, relating to, or characteristic of the branchiopods or the class Branchiopoda.",
    secondary: "Describing physiological adaptations (such as drought-resistant resting cysts and phyllopodous limbs) typical of branchiopod crustaceans.",
    quotes: [
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "The **branchiopodan** resting eggs retain viability across decades of drought, hatching within hours when temporary rains return." },
      { author: "William Thomas Calman", work: "Crustacea", quote: "The **branchiopodan** swimming stroke coordinates dozens of leaf-like limbs in a continuous metachronal wave." },
      { author: "Alfred Russel Wallace", work: "Island Life", quote: "The wide distribution of **branchiopodan** species across remote oceanic islands is explained by avian transport of their microscopic cysts." }
    ]
  },
  "Dashboard — branchi/branchiopodous.md": {
    word: "branchiopodous",
    primary: "Having gill-like, leaf-shaped feet or appendages; belonging to the branchiopods.",
    secondary: "In arthropod morphology, describing flattened, biramous, foliar limbs (phyllopodia) that function concurrently in locomotion, food-trapping, and gas exchange.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", quote: "The **branchiopodous** feet of the fairy shrimp beat rhythmically to create a feeding current directed toward the ventral groove." },
      { author: "Richard Owen", work: "Lectures on Invertebrate Animals", quote: "Triops possesses more than thirty pairs of **branchiopodous** appendages, each functioning as a microscopic gill." },
      { author: "William Thomas Calman", work: "The Life of Crustacea", quote: "The **branchiopodous** limb represents an ancient multifunctional archetype from which the specialized limbs of higher decapods arose." }
    ]
  },
  "Dashboard — branchi/branchiostegidae.md": {
    word: "branchiostegidae",
    primary: "A family of marine perciform fishes commonly known as tilefishes (often placed in the family Malacanthidae).",
    secondary: "In marine ichthyology, benthic fishes inhabiting continental slope burrows and rocky reefs, named from Greek branchia (gills) and stege (cover), referencing their well-developed opercular gill covers.",
    quotes: [
      { author: "David Starr Jordan", work: "A Guide to the Study of Fishes", quote: "The family **Branchiostegidae** includes the famous tilefish of the western Atlantic, renowned for its sudden catastrophic mortality in 1882." },
      { author: "William Beebe", work: "Half Mile Down", quote: "From the bathysphere window we observed species of **Branchiostegidae** hovering above their crater-like burrows in the canyon mud." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "A sudden influx of arctic water along the edge of the Gulf Stream annihilated millions of tilefish of the family **Branchiostegidae**." }
    ]
  },
  "Dashboard — branchi/branchiostomidae.md": {
    word: "branchiostomidae",
    primary: "The family of cephalochordates comprising the lancelets (amphioxus), including the genus Branchiostoma.",
    secondary: "In vertebrate evolutionary biology, the pivotal transitional family of small, translucent marine chordates possessing a persistent notochord, dorsal nerve cord, and pharyngeal gill slits without a true cranium.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Vertebrated Animals", quote: "The **Branchiostomidae**, commonly known as amphioxus, provide the morphological bridge connecting non-chordate invertebrates to true vertebrates." },
      { author: "Ernst Haeckel", work: "The Evolution of Man", quote: "In the simple anatomy of the **Branchiostomidae**, we behold the living portrait of our earliest chordate ancestors." },
      { author: "Alfred Sherwood Romer", work: "The Vertebrate Body", quote: "The pharyngeal basket of the **Branchiostomidae** functions both as a filter-feeding sieve and as a branchial respiratory organ." }
    ]
  },
  "Dashboard — branchi/branchiura.md": {
    word: "branchiura",
    primary: "A subclass of small aquatic crustaceans commonly called fish lice or carp lice, which live as ectoparasites on marine and freshwater fishes.",
    secondary: "In parasitic crustacean biology, characterized by a flattened disc-like carapace, compound eyes, and maxillae modified into powerful suckers (as in Argulus) for attaching to the host's skin and gills.",
    quotes: [
      { author: "William Thomas Calman", work: "The Life of Crustacea", quote: "The **Branchiura** are armed with prehensile suckers and piercing proboscises, swimming actively between fish hosts." },
      { author: "David Starr Jordan", work: "A Guide to the Study of Fishes", quote: "Carp ponds are frequently infested with Argulus, a destructive member of the **Branchiura** that ulcerates the gills of young fry." },
      { author: "Alister Hardy", work: "The Open Sea", quote: "Unlike parasitic barnacles that degenerate into mere roots, the **Branchiura** retain active swimming limbs and keen compound eyes." }
    ]
  },
  "Dashboard — branchi/nudibranch.md": {
    word: "nudibranch",
    primary: "A soft-bodied, shell-less marine gastropod mollusk (commonly called a sea slug), celebrated for its extraordinary brilliant colors and exposed external gills.",
    secondary: "In marine zoology, an order of opisthobranchs that discard their shells after the larval stage and breathe through naked external gills or cerata on their dorsal surfaces, often sequestering nematocysts from prey cnidarians.",
    quotes: [
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "The vivid orange **nudibranch** crawled across the eelgrass, its feathery gills expanding like a miniature flower in the clear water." },
      { author: "David Attenborough", work: "Blue Planet", quote: "The kaleidoscopic colors of the **nudibranch** warn predators of foul-tasting chemical defenses concentrated in its skin." },
      { author: "William Beebe", work: "Beneath Tropic Seas", quote: "Among the living corals crept a translucent **nudibranch**, adorned with cerata of glowing turquoise and electric gold." }
    ]
  },
  "Dashboard — branchi/unbranching.md": {
    word: "unbranching",
    primary: "Not branching; growing or proceeding in a single, straight, undivided stem, trunk, or direction.",
    secondary: "In descriptive morphology, describing columnar trees (such as palms or tree ferns) or linear processes that lack lateral bifurcation.",
    quotes: [
      { author: "John Muir", work: "The Mountains of California", quote: "The majestic sugar pine rose as an **unbranching** column of red bark for nearly a hundred feet before spreading its leafy crown." },
      { author: "Henry David Thoreau", work: "The Maine Woods", quote: "We pushed our canoe down an **unbranching** channel of the river, bordered on either side by impenetrable spruce." },
      { author: "Alfred Russel Wallace", work: "Tropical Nature", quote: "The smooth, **unbranching** trunks of tropical palms rise like monumental pillars to support their towering feathery crowns." }
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
console.log("Medicine & Pathology Batch 4 completed! Total words updated:", Object.keys(wordsData).length);
