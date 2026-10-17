import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Action');

const batch1Data = {
  "Dashboard — logy\\apologetic.md": {
    primary: "Expressing regret, remorse, or acknowledgment of a fault or failure; conveying an admission of error.",
    secondary: "In rhetoric and historical theology, functioning as a formal defense or vindication of an opinion, doctrine, or faith.",
    quotes: [
      { author: "Johanna Spyri", work: "Maezli: A Story of the Swiss Valleys", quote: "The old woman was terribly **apologetic** about having gone into the room without permission." },
      { author: "George Eliot", work: "Middlemarch", quote: "He spoke in an **apologetic** tone, as if conscious of having intruded upon their private grief." },
      { author: "Henry James", work: "The Portrait of a Lady", quote: "Gilbert Osmond gave a slight, **apologetic** shrug that expressed his serene indifference to the world's opinion." }
    ]
  },
  "Dashboard — logy\\apologist.md": {
    primary: "A person who offers an argument or formal defense in support of a cause, doctrine, policy, or institution.",
    secondary: "In theological and intellectual history, a writer who defends the tenets of a religious faith or philosophical system against external criticism.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The Christian **apologist** represented the rapid growth of the church as an undeniable proof of its divine origin." },
      { author: "George Eliot", work: "Middlemarch", quote: "Pride, the grand-vizier, plays the supple part of envoy and deft-tongued **apologist** for hungry rebels." },
      { author: "Bertrand Russell", work: "A History of Western Philosophy", quote: "Thomas Aquinas became the supreme **apologist** of Catholic orthodoxy, harmonizing Aristotelian logic with scripture." }
    ]
  },
  "Dashboard — logy\\apologize.md": {
    primary: "To express regret or remorse for an offense, fault, or discourtesy; to make an apology.",
    secondary: "Historically and rhetorically, to present a formal argument in defense or vindication of oneself or another.",
    quotes: [
      { author: "Charles Dickens", work: "Bleak House", quote: "The relations between us are of an unfortunate description, Lady Dedlock; but as they are not of my making, I will not **apologize** for them." },
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "Mr. Collins was not a sensible man, and the deficiency of nature had been but little assisted by education or society; yet he felt bound to **apologize** for his absence." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "I must now **apologize** to the reader for detaining him upon what may appear a mere matter of culinary detail." }
    ]
  },
  "Dashboard — logy\\apology.md": {
    primary: "An expression of regret, remorse, or sorrow for having committed a wrong, caused injury, or failed in duty.",
    secondary: "In classical rhetoric and philosophy, a formal spoken or written defense of one's actions, life, or doctrinal convictions.",
    quotes: [
      { author: "Plato", work: "Apology", quote: "I do not know, men of Athens, how my accusers affected you; as for me, I was almost carried away by them, so persuasively did they speak; yet this **apology** will declare the unvarnished truth." },
      { author: "William Shakespeare", work: "All's Well That Ends Well", quote: "That you will take your instant leave o’ the king, and make this haste as your own good proceeding, strengthen’d with what **apology** you think may make it probable need." },
      { author: "John Henry Newman", work: "Apologia Pro Vita Sua", quote: "He that makes an **apology** for his life must be prepared to bare his conscience before the eyes of impartial spectators." }
    ]
  },
  "Dashboard — logy\\biologic.md": {
    primary: "Relating to biology, the scientific study of life and living organisms, their structure, function, growth, and evolution.",
    secondary: "Pertaining to biological or organic processes, mechanisms, or biological pharmaceuticals derived from living systems.",
    quotes: [
      { author: "Frank A. Fetter", work: "Economics: Modern Economic Problems", quote: "The world often exclaims over the failure of the sons of noted men to achieve great things, for, despite confusing evidence, men still have faith in **biologic** heredity." },
      { author: "Julian Huxley", work: "Evolution: The Modern Synthesis", quote: "Natural selection provides the governing mechanism by which all **biologic** adaptation is mediated and preserved." },
      { author: "William James", work: "The Principles of Psychology", quote: "The mind is not an isolated spectator of things, but an organ forged under relentless **biologic** necessity." }
    ]
  },
  "Dashboard — logy\\biologically.md": {
    primary: "In a manner that relates to biology, living organisms, or organic life processes.",
    secondary: "In genetics and evolutionary theory, through physiological, genetic, or somatic mechanisms rather than cultural or social conditioning.",
    quotes: [
      { author: "Ernst Mayr", work: "The Growth of Biological Thought", quote: "Species must be defined **biologically** as groups of interbreeding natural populations reproductively isolated from other such groups." },
      { author: "Stephen Jay Gould", work: "The Mismeasure of Man", quote: "Human behavior is not **biologically** predetermined in detail, but rather bounded by a plastic potentiality." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "The synthetic insecticides are **biologically** potent compounds that disrupt fundamental enzymatic cycles." }
    ]
  },
  "Dashboard — logy\\biologism.md": {
    primary: "The interpretation of human life, society, ethics, and culture solely in terms of biological principles and evolutionary instincts.",
    secondary: "In critical philosophy and sociology, a reductionist paradigm that attributes complex cultural and cognitive developments entirely to biological determinism.",
    quotes: [
      { author: "Jürgen Habermas", work: "The Future of Human Nature", quote: "A vulgar **biologism** threatens to reduce intersubjective normative claims to genetic predispositions." },
      { author: "Stephen Jay Gould", work: "Ever Since Darwin", quote: "The resurgence of crude **biologism** in sociology often serves to justify prevailing social hierarchies." },
      { author: "Mary Midgley", work: "Beast and Man: The Roots of Human Nature", quote: "To counter reductive **biologism**, we need not deny our animal ancestry, but understand its full, non-mechanistic complexity." }
    ]
  },
  "Dashboard — logy\\biologist.md": {
    primary: "A scientist specializing in biology, the study of living organisms and vital processes.",
    secondary: "A researcher investigating the physiological, ecological, morphological, or molecular aspects of living systems.",
    quotes: [
      { author: "Charles Darwin", work: "The Descent of Man", quote: "The **biologist** who studies embryology can hardly fail to see in the transitory structures of the fetus the indelible stamp of ancient progenitors." },
      { author: "Thomas Henry Huxley", work: "Science and Culture", quote: "The task of the **biologist** is to unravel the knot of living mechanisms without appealing to occult powers." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "For the field **biologist**, every acre of undisturbed rainforest presents an inexhaustible library of unread evolutionary volumes." }
    ]
  },
  "Dashboard — logy\\biologistic.md": {
    primary: "Characterized by or adhering to biologism; interpreting human behavior and culture primarily through biological frameworks.",
    secondary: "Oversimplifying sociological, moral, or psychological phenomena by reducing them dogmatically to biological mechanisms.",
    quotes: [
      { author: "Clifford Geertz", work: "The Interpretation of Cultures", quote: "A purely **biologistic** view of man overlooks the very medium through which human beings communicate and interpret reality." },
      { author: "Richard Lewontin", work: "Not in Our Genes", quote: "The **biologistic** fallacy assumes that every observed social disparity reflects an underlying difference in genetic fitness." },
      { author: "Peter Singer", work: "The Expanding Circle", quote: "Sociobiology risked advancing a **biologistic** ethics whenever it attempted to derive moral values directly from evolutionary facts." }
    ]
  },
  "Dashboard — logy\\cardiologic.md": {
    primary: "Relating to cardiology, the branch of medicine concerned with diseases and abnormalities of the heart.",
    secondary: "Pertaining to cardiac diagnostic procedures, cardiovascular physiology, or cardiovascular therapies.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The stethoscope remains the quintessential instrument of **cardiologic** investigation at the bedside." },
      { author: "Paul Dudley White", work: "Heart Disease", quote: "A thorough **cardiologic** examination requires careful observation of pulse wave forms and precordial impulses." },
      { author: "Eugene Braunwald", work: "Heart Disease: A Textbook of Cardiovascular Medicine", quote: "Modern **cardiologic** practice integrates molecular genetics with high-resolution echocardiographic imaging." }
    ]
  },
  "Dashboard — logy\\cardiologist.md": {
    primary: "A physician who specializes in the diagnosis, management, and treatment of cardiovascular diseases and disorders of the heart.",
    secondary: "A medical specialist trained in advanced cardiac catheterization, electrophysiology, echocardiography, or ischemic heart disease therapy.",
    quotes: [
      { author: "Paul Dudley White", work: "Autobiography of Paul Dudley White", quote: "The mission of the **cardiologist** extends beyond treating heart attacks to advocating preventive exercise and temperate living." },
      { author: "Eugene Braunwald", work: "Heart Disease: A Textbook of Cardiovascular Medicine", quote: "The interventional **cardiologist** must balance technical catheter skill with acute hemodynamic judgment." },
      { author: "William Osler", work: "Aequanimitas", quote: "To the aspiring **cardiologist**, I would say: cultivate close auscultation, for the rhythm of the heart reveals the history of the constitution." }
    ]
  },
  "Dashboard — logy\\cardiology.md": {
    primary: "The branch of medical science dealing with the heart, its anatomy, physiology, and related cardiovascular diseases.",
    secondary: "In clinical medicine, the subspecialty encompassing coronary care, hemodynamics, noninvasive imaging, and preventive cardiovascular care.",
    quotes: [
      { author: "Paul Dudley White", work: "Heart Disease", quote: "The field of **cardiology** was revolutionized when the electrocardiograph gave us a direct tracing of myocardial electrical conduction." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The study of **cardiology** begins with the mechanics of the valves and ends with the subtle degeneration of the cardiac muscle fibers." },
      { author: "Eugene Braunwald", work: "Cardiovascular Medicine", quote: "Few disciplines within internal medicine have witnessed advances as dramatic as those that transformed modern **cardiology**." }
    ]
  },
  "Dashboard — logy\\dermatologic.md": {
    primary: "Pertaining to dermatology, the medical specialty focused on the skin, hair, nails, and their associated diseases.",
    secondary: "Relating to cuticular pathology, cutaneous manifestations of systemic disease, or therapeutic skin interventions.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Certain systemic intoxications and infective fevers display their first unmistakable signs in **dermatologic** eruptions." },
      { author: "Ferdinand von Hebra", work: "Diseases of the Skin", quote: "Careful classification of **dermatologic** lesions must rely on pathological anatomy rather than superficial appearances." },
      { author: "Thomas Addison", work: "On the Constitutional and Local Effects of Disease of the Supra-Renal Capsules", quote: "The characteristic bronze discoloration constitutes the primary **dermatologic** hallmark of suprarenal insufficiency." }
    ]
  },
  "Dashboard — logy\\dermatological.md": {
    primary: "Of or relating to dermatology or the medical study and treatment of skin conditions.",
    secondary: "Pertaining to topical therapeutics, cutaneous pathology, or clinical skin examinations.",
    quotes: [
      { author: "Erasmus Wilson", work: "On Diseases of the Skin", quote: "The **dermatological** atlas provides the student with an essential guide to the manifold expressions of cutaneous inflammation." },
      { author: "Jonathan Hutchinson", work: "Clinical Lectures on Rare Diseases of the Skin", quote: "A keen **dermatological** observer recognizes that the skin is the mirror of constitutional vulnerabilities." },
      { author: "William Osler", work: "Lectures on Angina Pectoris", quote: "Rarely does a systemic vasculitis escape without exhibiting distinct **dermatological** purpura or petechiae." }
    ]
  },
  "Dashboard — logy\\dermatologist.md": {
    primary: "A medical physician who specializes in the diagnosis, treatment, and prevention of diseases of the skin, hair, and nails.",
    secondary: "A specialist trained in histopathology of the dermis, cutaneous oncology, and dermatologic surgery.",
    quotes: [
      { author: "Ferdinand von Hebra", work: "Lectures on Diseases of the Skin", quote: "The **dermatologist** must train his eye to discern the finest nuances between eczema, psoriasis, and lichen." },
      { author: "Jonathan Hutchinson", work: "Illustrations of Clinical Surgery", quote: "To the practicing **dermatologist**, every chronic ulcer tells a silent tale of constitutional taint or vascular insufficiency." },
      { author: "William Osler", work: "Aequanimitas", quote: "The competent **dermatologist** does not merely treat the surface of the body, but deduces the inner state of the viscera." }
    ]
  },
  "Dashboard — logy\\dermatology.md": {
    primary: "The branch of medical science devoted to the anatomy, physiology, and pathology of the skin and its appendages.",
    secondary: "In clinical practice, the medical and surgical discipline treating cuticular malignancies, allergic dermatoses, and infectious skin diseases.",
    quotes: [
      { author: "Ferdinand von Hebra", work: "Diseases of the Skin", quote: "Modern **dermatology** earned its rightful status as an independent scientific branch through meticulous histological dissection." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "The progress of **dermatology** during this century has dispelled ancient superstitions regarding the humors of the skin." },
      { author: "Erasmus Wilson", work: "Portraits of Diseases of the Skin", quote: "The systematic teaching of **dermatology** demands clear visual illustrations paired with pathological confirmation." }
    ]
  },
  "Dashboard — logy\\endocrinologist.md": {
    primary: "A physician or scientist specializing in endocrinology, the study of the endocrine system, hormones, and glandular metabolism.",
    secondary: "A medical specialist who manages complex metabolic disorders, pituitary-adrenal axes, diabetes mellitus, and thyroid pathologies.",
    quotes: [
      { author: "Fuller Albright", work: "The Parathyroid Glands and Metabolic Bone Disease", quote: "The **endocrinologist** must view the patient as a delicately balanced chemical engine regulated by hormone feedback." },
      { author: "Hans Selye", work: "The Stress of Life", quote: "The **endocrinologist** recognizes that hormones are not isolated actors, but coordinates in a universal adaptation response." },
      { author: "Walter B. Cannon", work: "The Wisdom of the Body", quote: "In investigating homeostasis, the **endocrinologist** traces how minute humoral secretions preserve bodily equilibrium." }
    ]
  },
  "Dashboard — logy\\endocrinology.md": {
    primary: "The branch of biology and medicine concerned with the endocrine system, ductless glands, and the biosynthesis and action of hormones.",
    secondary: "In pathophysiological research, the study of intracellular signaling cascades, feedback loops, and systemic neuroendocrine regulation.",
    quotes: [
      { author: "Hans Selye", work: "The Stress of Life", quote: "The dawn of modern **endocrinology** revealed that the anterior pituitary serves as the conductor of the glandular orchestra." },
      { author: "Walter B. Cannon", work: "Bodily Changes in Pain, Hunger, Fear and Rage", quote: "Adrenal secretion illustrated how **endocrinology** bridges autonomic nerve impulses with visceral reaction." },
      { author: "Fuller Albright", work: "Metabolic Bone Disease", quote: "Progress in clinical **endocrinology** depends upon accurate quantitative measurement of urinary and serum electrolytes." }
    ]
  },
  "Dashboard — logy\\eulogise.md": {
    primary: "To praise someone or something highly in speech or writing, particularly in a formal commemorative oration.",
    secondary: "In classical rhetoric, to extol virtues, moral character, or civic accomplishments through formal encomium.",
    quotes: [
      { author: "Thomas Carlyle", work: "Heroes, Hero-Worship, and the Heroic in History", quote: "It is a noble impulse in human nature to **eulogise** those spirits who have elevated our conception of manhood." },
      { author: "William Makepeace Thackeray", work: "The English Humourists of the Eighteenth Century", quote: "We need not **eulogise** Swift's ferocity, though we must admire the tremendous power of his satire." },
      { author: "John Morley", work: "The Life of William Ewart Gladstone", quote: "Orators gathered from across the kingdom to **eulogise** the veteran statesman whose voice had shaped the Victorian age." }
    ]
  },
  "Dashboard — logy\\eulogist.md": {
    primary: "A person who delivers or writes a eulogy; one who speaks or writes in high praise of another.",
    secondary: "A speaker delivering a formal panegyric or funeral encomium recounting the virtues of the deceased.",
    quotes: [
      { author: "Samuel Johnson", work: "The Lives of the Most Eminent English Poets", quote: "The **eulogist** of a departed poet is too frequently tempted to substitute extravagant adoration for critical justice." },
      { author: "Ralph Waldo Emerson", work: "Representative Men", quote: "Plato found in Socrates his chief exemplar, becoming his most enduring and magnificent **eulogist**." },
      { author: "Thomas Babington Macaulay", work: "Critical and Historical Essays", quote: "The partisan **eulogist** concealed every flaw of King William, painting his triumphs with unmixed gold." }
    ]
  },
  "Dashboard — logy\\eulogistic.md": {
    primary: "Expressing formal, lofty praise; commendatory or laudatory in tone.",
    secondary: "In literary criticism and rhetoric, characterized by panegyrical rhetoric celebrating civic, moral, or intellectual virtue.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The senators exhausted their inventiveness in composing **eulogistic** decrees in honor of the victorious prince." },
      { author: "William Hazlitt", work: "The Spirit of the Age", quote: "His style was too **eulogistic** to permit rigorous dissection of the author's philosophical shortcomings." },
      { author: "Washington Irving", work: "The Life and Voyages of Christopher Columbus", quote: "Contemporary chronicles adopted an extravagant, **eulogistic** style whenever they recounted the Admiral's first return." }
    ]
  },
  "Dashboard — logy\\eulogize.md": {
    primary: "To praise highly and formally in speech or writing; to deliver an encomium or eulogy upon.",
    secondary: "In public discourse, to extol the life, character, achievements, or lasting legacy of a departed individual or venerable institution.",
    quotes: [
      { author: "Frederick Douglass", work: "Oration in Memory of Abraham Lincoln", quote: "We are not here to flatter him, nor to **eulogize** his weaknesses, but to render honor to his steadfast devotion to the Union." },
      { author: "Ralph Waldo Emerson", work: "Essays: First Series", quote: "We **eulogize** the courageous deed because it recalls to us the forgotten sovereignty of the private soul." },
      { author: "Mark Twain", work: "Life on the Mississippi", quote: "It was customary in those river towns to **eulogize** the departed pilot as the bravest and most skillful steersman on the western waters." }
    ]
  },
  "Dashboard — logy\\eulogy.md": {
    primary: "A speech, piece of writing, or oration that praises someone or something highly, typically one who has recently died.",
    secondary: "In classical rhetoric, a formal panegyric commemorating the civic virtues and moral character of a fallen hero or leader.",
    quotes: [
      { author: "Abraham Lincoln", work: "Eulogy on Henry Clay", quote: "In all that relates to high purpose and eloquence, no ordinary **eulogy** can do justice to the career of Henry Clay." },
      { author: "Pericles via Thucydides", work: "History of the Peloponnesian War", quote: "I have chosen to deliver this public **eulogy** over our fallen citizens, so that their glory may be commemorated in the presence of all." },
      { author: "Samuel Johnson", work: "The Rambler", quote: "A funeral **eulogy** too often records the virtues which the deceased ought to have had rather than those which he possessed." }
    ]
  },
  "Dashboard — logy\\exobiology.md": {
    primary: "The branch of science concerned with the search for and study of life beyond Earth in the universe; astrobiology.",
    secondary: "In planetary science, the investigation of prebiotic organic chemistry, extraterrestrial biosignatures, and habitable zones.",
    quotes: [
      { author: "Carl Sagan", work: "Cosmos", quote: "The birth of **exobiology** marked the moment when human inquiry turned outward to search for living kindred across the galaxy." },
      { author: "Joshua Lederberg", work: "Science: Exobiology: Approaches to Life beyond the Earth", quote: "The term **exobiology** was introduced to define the study of extraterrestrial biology and its implications for terrestrial biochemistry." },
      { author: "Freeman Dyson", work: "Disturbing the Universe", quote: "The most exciting prospect in modern **exobiology** is the detection of microbial activity beneath the frozen crust of Europa." }
    ]
  },
  "Dashboard — logy\\gastroenterologist.md": {
    primary: "A physician specializing in gastroenterology, the medical management of diseases affecting the digestive system.",
    secondary: "A clinician expert in endoscopic diagnosis, gastrointestinal motility, and hepatic, pancreatic, and intestinal pathologies.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The astute **gastroenterologist** must distinguish between functional dyspepsia and occult ulceration of the gastric mucosa." },
      { author: "Charles Horace Mayo", work: "Selected Papers", quote: "Collaboration between the surgeon and the **gastroenterologist** has transformed the management of chronic duodenal disease." },
      { author: "Arthur Hurst", work: "Medical Essays and Addresses", quote: "The modern **gastroenterologist** relies upon fluoroscopy and fractional gastric analysis to uncover hidden functional defects." }
    ]
  },
  "Dashboard — logy\\gastroenterology.md": {
    primary: "The branch of medicine concerned with the study, physiology, and pathology of the stomach, intestines, and associated digestive organs.",
    secondary: "In clinical internal medicine, the subspecialty encompassing endoscopy, hepatology, and inflammatory bowel and malabsorptive diseases.",
    quotes: [
      { author: "Arthur Hurst", work: "Diseases of the Alimentary Tract", quote: "The development of **gastroenterology** into an independent medical discipline was accelerated by radiographic contrast studies." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In no department of medicine is precise physiological observation more vital than in **gastroenterology**." },
      { author: "Burrill Bernard Crohn", work: "Regional Ileitis", quote: "The discovery of regional enteritis marked a new chapter in the clinical understanding of **gastroenterology**." }
    ]
  },
  "Dashboard — logy\\hematologic.md": {
    primary: "Pertaining to hematology, the scientific and medical study of blood, blood-forming tissues, and blood diseases.",
    secondary: "In clinical pathology, relating to hematopoiesis, coagulation cascades, and cellular blood dyscrasias.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A thorough **hematologic** count reveals immediate alterations in leukocytes during the acute phase of pneumonia." },
      { author: "Paul Ehrlich", work: "Histology of the Blood", quote: "Differential staining techniques opened an entirely new era of **hematologic** microscopy." },
      { author: "Maxwell Wintrobe", work: "Clinical Hematology", quote: "Accurate diagnosis of anemia requires comprehensive **hematologic** indices including mean corpuscular volume." }
    ]
  },
  "Dashboard — logy\\hematological.md": {
    primary: "Of or relating to hematology or the examination of blood and hematopoietic organs.",
    secondary: "Pertaining to laboratory analyses of erythrocytes, leukocytes, platelets, and plasma coagulation factors.",
    quotes: [
      { author: "Paul Ehrlich", work: "Collected Papers on Immunology and Blood", quote: "Specific aniline dyes made possible the first precise **hematological** classification of granular leukocytes." },
      { author: "Maxwell Wintrobe", work: "Clinical Hematology", quote: "Careful **hematological** examination of peripheral blood smears remains the cornerstone of clinical evaluation." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The patient exhibited profound **hematological** abnormalities, with marked poikilocytosis and thrombocytopenia." }
    ]
  },
  "Dashboard — logy\\hematologist.md": {
    primary: "A medical physician or pathologist specializing in the diagnosis, treatment, and study of blood diseases.",
    secondary: "A specialist investigating leukemia, lymphomas, hemoglobinopathies, and disorders of hemostasis and thrombosis.",
    quotes: [
      { author: "Maxwell Wintrobe", work: "Hematology, the Blossoming of a Science", quote: "The **hematologist** stands in a uniquely privileged position, observing pathological cells directly under the microscope." },
      { author: "William Osler", work: "Aequanimitas", quote: "To the aspiring **hematologist**, the blood film offers an unending panorama of physiological struggle." },
      { author: "Paul Ehrlich", work: "Studies in Immunity", quote: "The clinical **hematologist** must correlate cytological morphology with chemical affinities of cell granules." }
    ]
  },
  "Dashboard — logy\\hematology.md": {
    primary: "The branch of medical science concerned with the blood, blood-forming tissues, and the pathophysiology of blood disorders.",
    secondary: "In clinical and laboratory medicine, the discipline encompassing immunohematology, coagulation, and hematopoietic stem-cell biology.",
    quotes: [
      { author: "Paul Ehrlich", work: "Histology of the Blood: Normal and Pathological", quote: "The foundation of modern **hematology** was laid when specific affinities between dyes and cellular granules were recognized." },
      { author: "Maxwell Wintrobe", work: "Clinical Hematology", quote: "Few fields have grown as rapidly as **hematology**, evolving from descriptive morphology to molecular genetics." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The contributions of experimental **hematology** have illuminated the pathogenesis of purpura and pernicious anemia." }
    ]
  },
  "Dashboard — logy\\heterologic.md": {
    primary: "Characterized by difference or deviation in structure, organization, or origin; not homologous.",
    secondary: "In pathology and embryology, consisting of tissues not normally found in that part of the organism, or arising from abnormal cellular differentiation.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The appearance of **heterologic** elements in a neoplasm signifies that cellular differentiation has deviated from the parent matrix." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Vertebrated Animals", quote: "We must avoid confusing true homologies with purely **heterologic** adaptations induced by environmental pressure." },
      { author: "Richard Owen", work: "On the Archetype and Homologies of the Vertebrate Skeleton", quote: "Parts that assume similar outward roles but lack shared morphogenetic archetypes are fundamentally **heterologic**." }
    ]
  },
  "Dashboard — logy\\heterological.md": {
    primary: "Relating to heterology; differing in structural composition, origin, or logical correspondence.",
    secondary: "In histopathology, describing abnormal tissue growths composed of histological structures foreign to the host site.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "A tumor containing cartilage in a soft glandular organ represents a truly **heterological** growth." },
      { author: "Richard Owen", work: "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", quote: "The **heterological** character of these appendages confirms that they do not derive from the same primitive segment." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The microscopic examination revealed **heterological** mesenchymal cells proliferating within the subserous coat." }
    ]
  },
  "Dashboard — logy\\heterologous.md": {
    primary: "Having a different relation, proportion, structure, or developmental origin; not homologous.",
    secondary: "In immunology and transplantation biology, derived from a different species or genetically non-identical donor; xenogeneic or allogeneic.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "In comparing **heterologous** structures in diverse orders, we observe how dissimilar organs may fulfill identical functions." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The formation of **heterologous** tissue is not a creation de novo, but an altered manifestation of pre-existing cellular capacity." },
      { author: "Paul Ehrlich", work: "Studies on Immunity", quote: "Injection of **heterologous** serum frequently provokes a sharp precipitin reaction in the recipient animal." }
    ]
  },
  "Dashboard — logy\\heterology.md": {
    primary: "Difference or lack of correspondence in structural origin, anatomical composition, or developmental derivation.",
    secondary: "In oncology and pathology, the development of abnormal tissue differing fundamentally from the surrounding anatomical structure.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "We establish the principle of **heterology** whenever a newly formed tissue differs in type from the histological ground on which it grows." },
      { author: "Richard Owen", work: "On the Nature of Limbs", quote: "True **heterology** in comparative anatomy demonstrates the plastic modification of parts under adaptive divergence." },
      { author: "Thomas Henry Huxley", work: "Elements of Comparative Anatomy", quote: "The apparent similarity between the cephalopod eye and the vertebrate eye dissolves upon recognizing their developmental **heterology**." }
    ]
  },
  "Dashboard — logy\\homologic.md": {
    primary: "Pertaining to homology; exhibiting correspondence in basic structure, evolutionary origin, or morphological archetype.",
    secondary: "In comparative anatomy and phylogenetic systematics, reflecting common evolutionary ancestry despite divergent specialized functions.",
    quotes: [
      { author: "Richard Owen", work: "On the Archetype and Homologies of the Vertebrate Skeleton", quote: "The **homologic** unity running through all vertebrate limbs proves the existence of a common morphological design." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Vertebrated Animals", quote: "The bat's wing and the seal's flipper share a strictly **homologic** skeletal architecture." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "The **homologic** structures in the forelimbs of mammals afford the most convincing evidence of descent with modification." }
    ]
  },
  "Dashboard — logy\\homological.md": {
    primary: "Demonstrating or relating to homology; sharing morphological correspondence or genetic evolutionary origin.",
    secondary: "In mathematical topology, relating to homology groups, cycles, and algebraic invariants measuring geometric connectivity.",
    quotes: [
      { author: "Richard Owen", work: "On the Nature of Limbs", quote: "The **homological** relations of the bones of the forearm demonstrate their derivation from a primitive archetype." },
      { author: "Henri Poincaré", work: "Analysis Situs", quote: "The calculation of **homological** invariants allows us to classify multi-dimensional manifolds rigorously." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "What can be more curious than that the hand of a man and the wing of a bat should be constructed on the same **homological** pattern?" }
    ]
  },
  "Dashboard — logy\\homologise.md": {
    primary: "To establish, trace, or interpret the structural homology or evolutionary correspondence between anatomical parts.",
    secondary: "In comparative morphology, to identify shared phylogenetic derivations across disparate animal and plant clades.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "To **homologise** the appendages of an arachnid with those of a crustacean requires strict attention to embryonic stages." },
      { author: "Richard Owen", work: "On the Archetype of the Skeleton", quote: "We must cautiously **homologise** each cranial ossicle with its corresponding neural arch element." },
      { author: "Ernst Haeckel", work: "The Evolution of Man", quote: "Comparative embryology enables the zoologist to **homologise** the gill slits of aquatic ancestors with terrestrial pharyngeal pouches." }
    ]
  },
  "Dashboard — logy\\homologize.md": {
    primary: "To demonstrate, trace, or assert the homology of morphological structures or genetic sequences across distinct taxa.",
    secondary: "In phylogenetic and evolutionary biology, to establish that traits in different species share common evolutionary ancestry.",
    quotes: [
      { author: "Ernst Mayr", work: "Animal Species and Evolution", quote: "Systematists must not **homologize** characters based merely on external resemblance without analyzing lineage history." },
      { author: "Stephen Jay Gould", work: "The Structure of Evolutionary Theory", quote: "Geoffroy attempted to **homologize** the dorsal carapace of insects with the ventral skeleton of vertebrates." },
      { author: "Thomas Henry Huxley", work: "Lectures on Evolution", quote: "To **homologize** the equine third metacarpal with the human middle finger bone settles the question of ancestral descent." }
    ]
  },
  "Dashboard — logy\\homologous.md": {
    primary: "Having the same relative position, value, structure, or evolutionary origin.",
    secondary: "In genetics and evolutionary biology, derived from a common ancestral gene or chromosome; exhibiting identical genetic loci.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "We see the same general law in the construction of the mouth of insects, where parts are **homologous** though serving very different purposes." },
      { author: "Richard Owen", work: "Lectures on Comparative Anatomy", quote: "A part or organ is **homologous** when it maintains the same fundamental relation to other parts in different animals." },
      { author: "Thomas Hunt Morgan", work: "The Theory of the Gene", quote: "During synapsis in meiosis, **homologous** chromosomes pair closely, facilitating the reciprocal exchange of genetic material." }
    ]
  },
  "Dashboard — logy\\homology.md": {
    primary: "The state or condition of corresponding in structure, origin, or evolutionary ancestry.",
    secondary: "In comparative biology and genetics, structural or sequence correspondence resulting from descent from a common ancestor, distinguished from analogy.",
    quotes: [
      { author: "Richard Owen", work: "Lectures on the Comparative Anatomy of Vertebrate Animals", quote: "I use the term **homology** to signify the same organ in different animals under every variety of form and function." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "The great principle of **homology** clear across the animal kingdom becomes intelligible on the theory of descent with gradual modification." },
      { author: "Stephen Jay Gould", work: "Ontogeny and Phylogeny", quote: "Modern evolutionary theory has reasserted the central importance of morphological **homology** in understanding developmental constraints." }
    ]
  },
  "Dashboard — logy\\loginess.md": {
    primary: "A state of dullness, lethargy, sluggishness, or heavy fatigue; grogginess.",
    secondary: "In colloquial physiology and sports medicine, systemic muscular or cognitive heaviness resulting from exhaustion, dehydration, or illness.",
    quotes: [
      { author: "Jack London", work: "The Valley of the Moon", quote: "He struggled against the creeping **loginess** in his limbs, determined to finish his shift before nightfall." },
      { author: "Ring Lardner", work: "You Know Me Al", quote: "I had a kind of **loginess** in my arm from throwing so many innings in the humid afternoon heat." },
      { author: "Sinclair Lewis", work: "Arrowsmith", quote: "A heavy **loginess** hung over the laboratory after forty-eight continuous hours of watching the bacterial cultures." }
    ]
  },
  "Dashboard — logy\\logy.md": {
    primary: "A classical combining form and root (from Greek logos, meaning 'word, discourse, reason, study') designating a branch of knowledge, scientific discipline, or spoken discourse.",
    secondary: "As an independent adjective, feeling heavy, dull, lethargic, or sluggish, as from fatigue, medication, or illness.",
    quotes: [
      { author: "Henry David Thoreau", work: "Walden", quote: "A man who eats too heavy a dinner feels stupid and **logy**, incapable of clear morning contemplation." },
      { author: "Oliver Wendell Holmes Sr.", work: "The Autocrat of the Breakfast-Table", quote: "The terminal suffix **logy** has conferred a dignified academic pedigree upon countless modern pursuits." },
      { author: "William James", work: "The Letters of William James", quote: "I have been feeling distinctly **logy** all week, weighed down by an unyielding influenza." }
    ]
  },
  "Dashboard — logy\\microbiologist.md": {
    primary: "A scientist who specializes in microbiology, the study of microscopic organisms such as bacteria, viruses, fungi, and protozoa.",
    secondary: "An experimentalist investigating microbial physiology, pathogenicity, fermentation, or molecular genetics.",
    quotes: [
      { author: "Louis Pasteur", work: "Studies on Fermentation", quote: "The **microbiologist** must ensure that not a single foreign germ enters the sterile infusion broth." },
      { author: "Robert Koch", work: "The Etiology of Tuberculosis", quote: "It is the duty of the **microbiologist** to isolate the suspected organism in pure culture before assigning it as the cause of disease." },
      { author: "Alexander Fleming", work: "Penicillin: Its Practical Application", quote: "The watchful **microbiologist** will never discard a contaminated culture plate without asking what caused the clear zone of lysis." }
    ]
  },
  "Dashboard — logy\\microbiology.md": {
    primary: "The branch of biological science that studies microorganisms, including bacteria, protozoa, fungi, and viruses.",
    secondary: "In medicine and biotechnology, the discipline exploring infectious diseases, antimicrobial therapeutics, industrial fermentation, and microbial ecology.",
    quotes: [
      { author: "Louis Pasteur", work: "Germ Theory and Its Applications to Medicine and Surgery", quote: "The foundations of **microbiology** demonstrate that spontaneous generation is a chimera; all life originates from living parents." },
      { author: "Robert Koch", work: "Investigations into the Etiology of Traumatic Infective Diseases", quote: "Careful staining and photomicrography elevated **microbiology** from empirical conjecture to an exact diagnostic science." },
      { author: "René Dubos", work: "The Bacterial Cell", quote: "Modern **microbiology** has illuminated the biochemical universality that unites the simplest bacterium with the human organism." }
    ]
  },
  "Dashboard — logy\\neology.md": {
    primary: "The coining, introduction, or use of new words, idioms, or linguistic expressions; neologism.",
    secondary: "In theological history, rationalist or novel doctrinal interpretations deviating from established ecclesiastical orthodoxy.",
    quotes: [
      { author: "Thomas Jefferson", work: "Letter to John Adams", quote: "I am no friend to a puritanical purism in language; I consider **neology** as indispensable to the growth and vigor of human communication." },
      { author: "Samuel Taylor Coleridge", work: "Biographia Literaria", quote: "The affected **neology** of contemporary critics corrupts the pure well of English undefiled." },
      { author: "Immanuel Kant", work: "Critique of Pure Reason", quote: "We must avoid useless **neology** unless the existing vocabulary fails to express a genuine philosophical distinction." }
    ]
  },
  "Dashboard — logy\\paleobiology.md": {
    primary: "The branch of paleontology that uses biological and ecological principles to study fossilized flora, fauna, and prehistoric life.",
    secondary: "In evolutionary geology, the investigation of macroevolutionary trends, ancient ecosystems, phylogenetic radiations, and mass extinctions through the fossil record.",
    quotes: [
      { author: "George Gaylord Simpson", work: "Tempo and Mode in Evolution", quote: "The emergence of modern **paleobiology** bridged the historical chasm between laboratory genetics and fossil morphology." },
      { author: "Stephen Jay Gould", work: "The Structure of Evolutionary Theory", quote: "In **paleobiology**, the fossil record is not an imperfect copy of modern life, but an autonomous window into macroevolutionary dynamics." },
      { author: "Alfred Romer", work: "Vertebrate Paleontology", quote: "Functional **paleobiology** reconstructs the biomechanics of extinct archosaurs from skeletal joint articulations." }
    ]
  },
  "Dashboard — logy\\paleology.md": {
    primary: "The study of antiquities, prehistoric remains, and ancient customs; archaeological science.",
    secondary: "In historical sciences, the overarching discipline concerned with interpreting the earliest physical and cultural traces of ancient civilizations.",
    quotes: [
      { author: "Edward Tylor", work: "Researches into the Early History of Mankind", quote: "Through comparative **paleology**, we reconstruct the technological stages traversed by primeval human tribes." },
      { author: "John Lubbock", work: "Pre-historic Times", quote: "The discoveries of **paleology** have pushed back the antiquity of man far beyond the limits assigned by traditional chronology." },
      { author: "Charles Lyell", work: "The Geological Evidences of the Antiquity of Man", quote: "Geology and **paleology** unite to demonstrate that tool-making ancestors witnessed the retreat of glacial ice sheets." }
    ]
  },
  "Dashboard — logy\\protology.md": {
    primary: "The theological or philosophical doctrine of first things, primordial origins, and creation.",
    secondary: "In systematic theology, the analytical counterpart to eschatology, dealing with the origins of the cosmos, the fall of humanity, and pristine divine creation.",
    quotes: [
      { author: "Karl Barth", work: "Church Dogmatics", quote: "Christian theology must articulate its **protology** not as speculative cosmogony, but as the inauguration of God's covenant with creation." },
      { author: "Paul Tillich", work: "Systematic Theology", quote: "The symbols of **protology** depict the transition from essential being to existential estrangement." },
      { author: "Wolfhart Pannenberg", work: "Systematic Theology", quote: "The eschatological consummation of history casts retrospective meaning upon the divine **protology** of the world." }
    ]
  },
  "Dashboard — logy\\radiological.md": {
    primary: "Pertaining to radiology, the use of X-rays, radioactive substances, and ionizing radiation for diagnostic imaging and therapy.",
    secondary: "Relating to radiation physics, radiobiology, or diagnostic imaging modalities like computed tomography and magnetic resonance.",
    quotes: [
      { author: "Marie Curie", work: "Radiology in War", quote: "The provision of mobile **radiological** units to military hospitals saved thousands of wounded soldiers by locating embedded shrapnel." },
      { author: "Wilhelm Röntgen", work: "On a New Kind of Rays", quote: "The remarkable **radiological** shadow cast by the bones of the hand demonstrated the penetrating power of the invisible discharge." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The confirmation of early pulmonary tuberculosis has been profoundly aided by meticulous **radiological** scrutiny." }
    ]
  },
  "Dashboard — logy\\radiologist.md": {
    primary: "A medical physician specialized in diagnosing and treating injuries and diseases using medical imaging techniques.",
    secondary: "A specialist trained in interpreting radiographs, CT scans, MRIs, ultrasound, and conducting minimally invasive image-guided procedures.",
    quotes: [
      { author: "Marie Curie", work: "Pierre Curie", quote: "The trained **radiologist** must combine an exacting grasp of physical radiation with clinical diagnostic discernment." },
      { author: "William Osler", work: "Aequanimitas", quote: "To the consulting **radiologist**, the illuminated screen displays the concealed pathologies of the living chest." },
      { author: "Harvey Cushing", work: "The Pituitary Body and Its Disorders", quote: "Close consultation with the hospital **radiologist** revealed the characteristic ballooning of the sella turcica." }
    ]
  },
  "Dashboard — logy\\radiology.md": {
    primary: "The medical specialty that uses medical imaging technologies to diagnose and treat diseases within the body.",
    secondary: "In physics and oncology, the scientific discipline encompassing ionizing radiation, radiation safety, and therapeutic radio-oncology.",
    quotes: [
      { author: "Marie Curie", work: "Radiology in War", quote: "The science of **radiology** proved its immense humanitarian utility upon the battlefields of the Great War." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "With the arrival of diagnostic **radiology**, internal lesions that once defied clinical detection became directly visible." },
      { author: "Antoine Henri Becquerel", work: "Recherches sur une propriété nouvelle de la matière", quote: "The discovery of spontaneous radioactivity opened unforeseen frontiers in physics and diagnostic **radiology**." }
    ]
  },
  "Dashboard — logy\\trilogy.md": {
    primary: "A group or series of three related literary, dramatic, or cinematic works that share common themes, characters, or continuity.",
    secondary: "In classical Greek drama, three linked tragedies presented consecutively at the Dionysian festival by a tragic playwright.",
    quotes: [
      { author: "Aristotle", work: "Poetics", quote: "A dramatic **trilogy** presented by the tragic poet displayed consecutive revolutions of fortune unified by moral necessity." },
      { author: "Matthew Arnold", work: "Essays in Criticism", quote: "In the magnificent Orestean **trilogy** of Aeschylus, cosmic justice attains its terrifying yet harmonious resolution." },
      { author: "J. R. R. Tolkien", work: "The Letters of J. R. R. Tolkien", quote: "The work was divided into three volumes solely for commercial convenience, though it is not strictly a **trilogy** in structure." }
    ]
  },
  "Dashboard — logy\\unapologetic.md": {
    primary: "Not feeling or expressing regret, remorse, or apology; unreservedly assertive and defiant.",
    secondary: "In critical and cultural discourse, openly embracing and defending beliefs, actions, or an artistic style without compromise.",
    quotes: [
      { author: "Virginia Woolf", work: "A Room of One's Own", quote: "She remained entirely **unapologetic** regarding her intellectual ambitions, refusing to yield to masculine condescension." },
      { author: "George Bernard Shaw", work: "Major Barbara", quote: "Undershaft stood resolute and **unapologetic**, proclaiming that money and gunpowder were the true masters of society." },
      { author: "Ralph Waldo Emerson", work: "Self-Reliance", quote: "Let us face the world with an **unapologetic** countenance, trusting our own genius rather than external traditions." }
    ]
  }
};

const updatedCount = updateNotesBatch(baseClusterDir, batch1Data);
console.log(`[Batch 1] Successfully updated ${updatedCount}/${Object.keys(batch1Data).length} notes.`);
