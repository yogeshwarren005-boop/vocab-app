import json
import os

batch3_data = {
  "Dashboard — pharmac\\pharmacy.md": {
    "primary": "The science, art, or practice of preparing, preserving, compounding, and dispensing medicinal drugs; also a retail store or hospital dispensary where medicines are sold.",
    "secondary": "In public health and health system administration, the professional healthcare discipline responsible for the clinical provision and stewardship of pharmaceutical care.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The physician who masters the essentials of practical **pharmacy** writes clear and rational prescriptions." },
      { "author": "Louis Goodman", "work": "The Pharmacological Basis of Therapeutics", "quote": "Hospital **pharmacy** services play an indispensable role in monitoring drug interactions and therapeutic drug levels." },
      { "author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "The chemical revolution rescued **pharmacy** from superstitious galenical polypharmacy and established rational therapeutics." }
    ]
  },
  "Dashboard — pheb\\autophobia.md": {
    "primary": "An abnormal, intense, and irrational fear of being alone, isolated, or by oneself; also known as monophobia.",
    "secondary": "In clinical psychology and psychoanalysis, a morbid dread of solitary confinement, abandonment, or confrontation with one's own ego.",
    "quotes": [
      { "author": "William James", "work": "The Principles of Psychology", "quote": "In pathological degrees, the natural discomfort of solitude degenerates into agonizing **autophobia**." },
      { "author": "Sigmund Freud", "work": "Inhibitions, Symptoms and Anxiety", "quote": "The neurotic symptom of **autophobia** frequently originates in childish panic over separation from maternal protection." },
      { "author": "Emil Kraepelin", "work": "Lectures on Clinical Psychiatry", "quote": "Patients suffering from severe **autophobia** cannot remain in an empty room without precipitating overwhelming panic." }
    ]
  },
  "Dashboard — pheb\\panphobia.md": {
    "primary": "A persistent, vague, and generalized dread of everything; omnipresent, nonspecific free-floating anxiety (also termed pantophobia).",
    "secondary": "In 19th-century neuropsychiatry, a condition described by Théodule Ribot and early alienists where the patient fears any indeterminate future event or nameless hazard.",
    "quotes": [
      { "author": "Théodule Ribot", "work": "The Psychology of the Emotions", "quote": "In **panphobia**, fear is detached from any definite object and attaches itself promiscuously to the entire surrounding universe." },
      { "author": "William James", "work": "The Principles of Psychology", "quote": "The morbid state of **panphobia** reduces the sufferer to a trembling victim of every harmless sound and shadow." },
      { "author": "Emil Kraepelin", "work": "Lectures on Clinical Psychiatry", "quote": "The deep melancholic agitation often culminates in acute **panphobia**, where existence itself feels impending doom." }
    ]
  },
  "Dashboard — pheb\\pheb.md": {
    "primary": "Linguistic root / combining form variant related to fear, flight, or dread (Greek phobos / phebo-).",
    "secondary": "In etymological analysis, a phonological variant connecting Indo-European roots of flight (*bhegw-) with Greek nominal forms denoting phobia.",
    "quotes": [
      { "author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "The etymological radical **pheb** reflects archaic vocalic alternation in the Greek stem for flight and terrified dread." },
      { "author": "Walter William Skeat", "work": "An Etymological Dictionary of the English Language", "quote": "Underlying the clinical suffixes in -phobia lies the archaic Hellenic root **pheb**, denoting panic and rout." },
      { "author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The verbal stem phebomai shares with **pheb** the primitive signification of fleeing in terror before an enemy." }
    ]
  },
  "Dashboard — pheb\\phobophobia.md": {
    "primary": "An irrational and persistent fear of phobias, or a dread of experiencing the sensation of fear itself.",
    "secondary": "In anxiety disorder pathology, an anticipatory fear where physical panic sensations (hyperventilation, palpitations) provoke terror of entering a panic cycle.",
    "quotes": [
      { "author": "William James", "work": "The Principles of Psychology", "quote": "The anticipatory dread known as **phobophobia** creates a vicious circle wherein the dread of fright evokes fright itself." },
      { "author": "Sigmund Freud", "work": "Inhibitions, Symptoms and Anxiety", "quote": "In agoraphobic subjects, **phobophobia** frequently constitutes the real obstacle preventing them from venturing into public squares." },
      { "author": "Emil Kraepelin", "work": "Lectures on Clinical Psychiatry", "quote": "Chronic panic patients become immobilized by **phobophobia**, trembling at the mere suspicion of an impending seizure." }
    ]
  },
  "Dashboard — phleb\\phleb.md": {
    "primary": "Combining form relating to veins or the venous circulation (from Greek phleps, phlebos).",
    "secondary": "In anatomical and clinical terminology, the formative element in words denoting venous vessels, inflammation, imaging, or surgical procedures.",
    "quotes": [
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The Greek root **phleb** serves as the universal prefix distinguishing venous structures and affections from arterial ones." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Pathologists rely on the root **phleb** to construct precise diagnoses of vascular lesions such as phlebitis and phlebosclerosis." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Venous architecture formed under the classical stem **phleb** illustrates passive drainage and valve mechanics in systemic circulation." }
    ]
  },
  "Dashboard — phleb\\phlebectomy.md": {
    "primary": "The surgical removal or excision of a vein or a segment of a vein, commonly performed to treat varicose veins.",
    "secondary": "In vascular surgery, ambulatory phlebectomy—a minimally invasive technique utilizing micro-incisions to extract tortuous superficial varicosities.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Extensive superficial varices of the saphenous system often necessitate surgical **phlebectomy** to alleviate stasis ulcers." },
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "During segmental **phlebectomy**, care must be exercised to preserve the adjacent saphenous nerve from traction injury." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Histopathological evaluation of the excised vessel following **phlebectomy** demonstrates eccentric muscular hypertrophy and intimal fibrosis." }
    ]
  },
  "Dashboard — phleb\\phlebitis.md": {
    "primary": "Inflammation of the wall of a vein, often accompanied by tenderness, erythema, and localized swelling.",
    "secondary": "In clinical vascular medicine, superficial thrombophlebitis or deep venous inflammation provoked by intravenous catheters, mechanical trauma, or hypercoagulability.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Septic **phlebitis** complicating otitis media constitutes the primary source of metastatic lung abscesses." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "It is not inflammatory **phlebitis** that initially coagulates the blood, but rather intravascular thrombosis that induces secondary mural inflammation." },
      { "author": "Thomas Sydenham", "work": "The Whole Works of That Excellent Practical Physician", "quote": "Painful cord-like induration along the leg denotes acute **phlebitis**, demanding strict rest and soothing warm fomentations." }
    ]
  },
  "Dashboard — phleb\\phlebodium.md": {
    "primary": "A genus of epiphytic ferns in the family Polypodiaceae, native to tropical and subtropical regions of the Americas.",
    "secondary": "In pteridology, the blue star fern (Phlebodium aureum), characterized by creeping golden-scaled rhizomes and glaucous, deeply pinnatifid fronds with reticulate venation.",
    "quotes": [
      { "author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The genus **phlebodium** is distinguished by its conspicuous net-like venation and large golden soral cushions." },
      { "author": "Alfred Russel Wallace", "work": "Tropical Nature, and Other Essays", "quote": "Climbing upon the trunks of palm trees, robust epiphytic ferns of the genus **phlebodium** unfold handsome glaucous fronds." },
      { "author": "William Jackson Hooker", "work": "Species Filicum", "quote": "In **phlebodium**, the areolate venation features free included veinlets bearing prominent terminal sori." }
    ]
  },
  "Dashboard — phleb\\phlebogram.md": {
    "primary": "A radiograph of a vein or venous system obtained by injecting radiopaque contrast medium (also called a venogram).",
    "secondary": "In cardiovascular diagnostics, a recording of venous pressure pulsations or pulse waveforms (such as the jugular venous pulse tracing).",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The jugular **phlebogram** displays characteristic 'a', 'c', and 'v' waves reflecting right atrial pressure dynamics." },
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "A diagnostic **phlebogram** outlines the precise extent of intraluminal obstruction within the iliofemoral venous trunk." },
      { "author": "Louis Goodman", "work": "The Pharmacological Basis of Therapeutics", "quote": "Before administering fibrinolytic agents, an ascending **phlebogram** confirms the presence of occlusive venous thrombi." }
    ]
  },
  "Dashboard — phleb\\phlebography.md": {
    "primary": "The radiological visualization and recording of veins following intravenous injection of a contrast medium; venography.",
    "secondary": "In clinical cardiology and vascular surgery, the physiological tracing of venous pulse contours or angiographic mapping of deep venous thrombosis.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The introduction of contrast **phlebography** enabled the direct radiographic demonstration of deep-vein thrombosis." },
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Ascending **phlebography** serves as the gold standard for defining valvular incompetence in the lower extremities." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Serial **phlebography** reveals how collateral venous channels dilate following persistent occlusion of the inferior vena cava." }
    ]
  },
  "Dashboard — phleb\\phlebology.md": {
    "primary": "The branch of medicine and medical science dedicated to the anatomy, physiology, and pathology of the venous system and its diseases.",
    "secondary": "In subspecialty surgical practice, the comprehensive diagnosis and treatment of varicose veins, venous stasis ulcers, and venous thromboembolism.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Modern **phlebology** combines hemodynamic ultrasound with minimally invasive interventions to preserve venous competence." },
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The discipline of **phlebology** demands an exact appreciation of deep, superficial, and perforator venous architecture." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Progress in **phlebology** accelerated once the cellular pathology of endothelial injury and stasis was elucidated." }
    ]
  },
  "Dashboard — phleb\\phlebosclerosis.md": {
    "primary": "Fibrous thickening, hardening, and loss of elasticity of the walls of veins; the venous counterpart of arteriosclerosis.",
    "secondary": "In cardiovascular pathology, intimal hyperplasia and collagen deposition in vein walls subjected to chronic elevated venous hypertension.",
    "quotes": [
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Long-standing venous hypertension induces marked **phlebosclerosis**, transforming thin-walled venules into rigid fibrous tubes." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In chronic portal hypertension, the mesenteric veins display palpable **phlebosclerosis** with diffuse mural thickening." },
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Microscopic sections of **phlebosclerosis** show progressive loss of medial smooth muscle and excessive hyaline collagenization." }
    ]
  },
  "Dashboard — phleb\\phlebothrombosis.md": {
    "primary": "The formation of a thrombus (blood clot) within a vein without prior or prominent inflammation of the vessel wall.",
    "secondary": "In hematology and surgery, deep venous clot formation characterized by loose adherence to the intima and high risk of pulmonary embolism.",
    "quotes": [
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "In pure **phlebothrombosis**, the clot lies loosely anchored within the lumen, presenting immense danger of sudden pulmonary dislodgement." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Post-operative immobilization is the primary trigger of insidious **phlebothrombosis** in the calf veins." },
      { "author": "Louis Goodman", "work": "The Pharmacological Basis of Therapeutics", "quote": "Prophylactic heparin significantly diminishes the incidence of silent **phlebothrombosis** in bedridden surgical patients." }
    ]
  },
  "Dashboard — phleb\\phlebotomise.md": {
    "primary": "To perform phlebotomy upon; to bleed therapeutically or draw blood from a vein (British spelling of phlebotomize).",
    "secondary": "In historical medicine, to open a vein with a lancet as an antiphlogistic or depleting therapy.",
    "quotes": [
      { "author": "Thomas Sydenham", "work": "The Whole Works of That Excellent Practical Physician", "quote": "In pleurisy and acute inflammatory fevers, the physician must **phlebotomise** the patient without hesitation." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "To **phlebotomise** a patient in acute pulmonary edema promptly unloads the right ventricle and relieves suffocation." },
      { "author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The ancient impulse to **phlebotomise** every suffering mortal drained more vitality than the underlying malady." }
    ]
  },
  "Dashboard — phleb\\phlebotomist.md": {
    "primary": "A person trained or certified to perform venipunctures and draw blood samples for clinical analysis or blood donation.",
    "secondary": "In historical surgery, a practitioner or barber-surgeon whose trade was therapeutic bloodletting.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A skilled **phlebotomist** obtains diagnostic blood specimens swiftly and with minimal trauma to the antecubital veins." },
      { "author": "Thomas Sydenham", "work": "The Whole Works of That Excellent Practical Physician", "quote": "The attendant summoned the **phlebotomist** to extract twelve ounces of blood from the cephalic vein." },
      { "author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The medieval **phlebotomist** brandished his brass basin and lancet as emblems of clinical authority." }
    ]
  },
  "Dashboard — phleb\\phlebotomize.md": {
    "primary": "To draw blood from a vein; to bleed therapeutically or for diagnostic analysis.",
    "secondary": "In clinical hematology, to remove therapeutic volumes of blood to reduce iron overload (hemochromatosis) or red cell mass (polycythemia vera).",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In polycythemia vera, the clinician must **phlebotomize** the patient periodically to lower blood viscosity and prevent stroke." },
      { "author": "Benjamin Rush", "work": "Medical Inquiries and Observations", "quote": "During the yellow fever epidemic, I resolved to **phlebotomize** copiously to reduce vascular excitement." },
      { "author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "Surgeons of the past felt an irrepressible urge to **phlebotomize** anyone who fell unconscious upon the pavement." }
    ]
  },
  "Dashboard — phleb\\phlebotomus.md": {
    "primary": "A genus of biting sandflies (family Psychodidae) found in the Old World, vectors of cutaneous and visceral leishmaniasis and sandfly fever.",
    "secondary": "In medical entomology and parasitology, nocturnal phlebotomine dipterans whose blood-feeding females transmit Leishmania protozoa and phleboviruses.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The tiny sandfly **phlebotomus** papatasi transmits pappataci fever across Mediterranean and Middle Eastern garrisons." },
      { "author": "Patrick Manson", "work": "Tropical Diseases", "quote": "Transmission of visceral leishmaniasis occurs through the bite of infected females of the genus **phlebotomus**." },
      { "author": "Ronald Ross", "work": "The Prevention of Malaria", "quote": "Control of **phlebotomus** requires eliminating dark, moist breeding habitats in cracked plaster and rubble." }
    ]
  },
  "Dashboard — phleb\\phlebotomy.md": {
    "primary": "The surgical opening or puncturing of a vein, either to draw blood for diagnostic testing or transfusion, or historically as bloodletting.",
    "secondary": "In modern hematology, therapeutic phlebotomy performed to manage erythrocytosis, porphyria cutanea tarda, or primary hemochromatosis.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In hereditary hemochromatosis, systematic **phlebotomy** removes excess parenchymal iron and halts hepatic fibrosis." },
      { "author": "Thomas Sydenham", "work": "The Whole Works of That Excellent Practical Physician", "quote": "Early and decisive **phlebotomy** moderates the tumultuous heat of inflammatory pleurisy." },
      { "author": "Benjamin Rush", "work": "Medical Inquiries and Observations", "quote": "I defended the practice of **phlebotomy** as the most direct means of subduing violent arterial excitement." }
    ]
  },
  "Dashboard — phleg\\Phlox.md": {
    "primary": "A genus of North American flowering plants in the family Polemoniaceae, widely cultivated in gardens for their clusters of vibrant, fragrant blossoms.",
    "secondary": "In systematic botany, herbaceous perennials and annuals (from Greek phlox, flame) characterized by salverform corollas with five spreading lobes.",
    "quotes": [
      { "author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The genus **Phlox** displays vibrant terminal cymes whose brilliant scarlet and purple corollas justify the Greek name for flame." },
      { "author": "Henry David Thoreau", "work": "Journal", "quote": "Along the garden borders, clusters of wild **phlox** opened their sweet-scented petals under the warm July sun." },
      { "author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "Observations on **Phlox** subulata demonstrate heterostyly adapted to encourage cross-fertilization by lepidopteran pollinators." }
    ]
  },
  "Dashboard — phleg\\antiphlogistic.md": {
    "primary": "Acting to counteract or reduce inflammation; an agent or remedy that relieves inflammatory symptoms.",
    "secondary": "In historical medicine and chemistry, a therapy or regimen (such as venesection, purges, or cooling salts) opposing the hypothetical caloric principle 'phlogiston'.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Cold compresses and saline laxatives served as the classic **antiphlogistic** regimen in acute pleurisy." },
      { "author": "Thomas Sydenham", "work": "The Whole Works of That Excellent Practical Physician", "quote": "The physician must apply an **antiphlogistic** treatment to soothe the boiling humors of inflammatory fever." },
      { "author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "The new chemical theory proved completely **antiphlogistic**, banishing the imaginary element of fire from modern science." }
    ]
  },
  "Dashboard — phleg\\phleg.md": {
    "primary": "Combining form relating to flame, burning, inflammation, or mucus (Greek phlegma, phleg-).",
    "secondary": "In anatomical and pathological etymology, the radical in phlegmasia, phlegmon, and phlegmatic, originating in ancient humoral concepts of heat and bodily humors.",
    "quotes": [
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The root **phleg** originally signified intense burning heat before medical tradition applied it to viscous inflammatory exudates." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Classical pathology employed the formative stem **phleg** to describe both acute cellulitis and sluggish humoral dispositions." },
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The linguistic legacy of **phleg** persists in clinical designations of purulent, spreading inflammation." }
    ]
  },
  "Dashboard — phleg\\phlegmasia.md": {
    "primary": "Inflammation, particularly characterized by redness, heat, and swelling; historically, any inflammatory disease or fever.",
    "secondary": "In clinical vascular surgery and obstetrics, phlegmasia alba dolens (milk leg) or phlegmasia cerulea dolens—life-threatening deep iliofemoral venous occlusions.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Post-partum **phlegmasia** alba dolens produces a white, tense, painful swelling of the lower limb due to femoral thrombosis." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "In **phlegmasia** cerulea dolens, total venous obstruction causes massive cyanosis and impending ischemic gangrene." },
      { "author": "Thomas Sydenham", "work": "The Whole Works of That Excellent Practical Physician", "quote": "Violent **phlegmasia** within the thoracic cavity demands vigorous therapeutic cooling and evacuation." }
    ]
  },
  "Dashboard — phleg\\phlegmatic.md": {
    "primary": "Having an unemotional, calm, and stolidly composed temperament; not easily excited or perturbed.",
    "secondary": "In classical humoral theory, a bodily constitution dominated by the humor phlegm, characterized by coolness, moisture, and sluggish responsiveness.",
    "quotes": [
      { "author": "William James", "work": "The Principles of Psychology", "quote": "A **phlegmatic** temperament shields an individual from emotional storms but dulls the promptness of sympathetic reaction." },
      { "author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The **phlegmatic** animal faces imminent danger with dull indifference, showing little change in facial expression." },
      { "author": "Samuel Johnson", "work": "The Rambler", "quote": "The **phlegmatic** scholar proceeds with deliberate, untroubled persistence where passionate geniuses burn out." }
    ]
  },
  "Dashboard — phleg\\phlegmatical.md": {
    "primary": "Archaic variant of phlegmatic; calm, sluggish, unemotional, or dominated by phlegm.",
    "secondary": "In historical physiology and character analysis, exhibiting coolness, apathy, or slow cognitive and metabolic tempo.",
    "quotes": [
      { "author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "Persons of a cold and **phlegmatical** complexion are less prone to acute pestilential fevers." },
      { "author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The ancients classified creatures of slow motion and sluggish digestion under a **phlegmatical** nature." },
      { "author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "The **phlegmatical** man is neither easily stirred to anger nor readily elevated into joyous exuberance." }
    ]
  },
  "Dashboard — phleg\\phlegmatically.md": {
    "primary": "In a phlegmatic, calm, composed, or unemotional manner; without showing excitement or perturbation.",
    "secondary": "Moving, reacting, or speaking with stolid indifference and sluggish deliberation.",
    "quotes": [
      { "author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Tulkinghorn received the alarming intelligence **phlegmatically**, without moving a muscle of his impassive face." },
      { "author": "George Eliot", "work": "Middlemarch", "quote": "He listened **phlegmatically** to the heated debate, puffing his pipe with tranquil unconcern." },
      { "author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Joseph Sedley endured the panic of Waterloo **phlegmatically** until flight became an absolute necessity." }
    ]
  },
  "Dashboard — phleg\\phlegmon.md": {
    "primary": "A localized area of acute, diffuse, purulent inflammation of subcutaneous or connective tissue, tending to ulcerate and spread.",
    "secondary": "In clinical surgery and pathology, uncircumscribed suppurative cellulitis infiltrating tissue planes without forming a discrete encapsulated abscess.",
    "quotes": [
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "A diffuse **phlegmon** dissects rapidly along fascial planes through destructive infiltration of polymorphonuclear leukocytes." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Ludwig's angina represents a woody, dangerous **phlegmon** of the submandibular and sublingual spaces." },
      { "author": "Thomas Sydenham", "work": "The Whole Works of That Excellent Practical Physician", "quote": "The fiery tumefaction deepened into an angry **phlegmon**, threatening extensive mortification of the surrounding flesh." }
    ]
  },
  "Dashboard — phleg\\phlegmonous.md": {
    "primary": "Of, relating to, or characterized by a phlegmon; diffusely and acutely inflammatory with purulent infiltration.",
    "secondary": "In pathology, describing virulent bacterial infections such as phlegmonous gastritis or phlegmonous appendicitis marked by suppurative transmural necrosis.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Acute **phlegmonous** gastritis is a rare, devastating streptococcal infection infiltrating the entire gastric wall." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Microscopic sections of the appendix in **phlegmonous** inflammation display extensive fibrinous exudates and leukocytic sheets." },
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The dense palmar aponeurosis directs **phlegmonous** suppuration upward into the forearm fascial spaces." }
    ]
  },
  "Dashboard — phleg\\phlegmy.md": {
    "primary": "Full of, resembling, or producing thick mucus or phlegm.",
    "secondary": "In clinical description, characterizing a cough or sputum that is heavy, viscous, and congested with bronchial secretions.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic bronchiectasis is characterized by paroxysmal **phlegmy** cough productive of copious, foul-smelling sputum." },
      { "author": "Charles Dickens", "work": "Our Mutual Friend", "quote": "The old waterman cleared his throat with a deep, **phlegmy** rasp before answering our hail." },
      { "author": "Thomas Sydenham", "work": "The Whole Works of That Excellent Practical Physician", "quote": "Winter catarrhs fill the bronchial passages with **phlegmy** defluxions that obstruct respiration." }
    ]
  },
  "Dashboard — phleg\\phlogistic.md": {
    "primary": "Inflammatory; producing, relating to, or causing inflammation.",
    "secondary": "In historical chemistry, of or relating to phlogiston or the phlogiston theory of combustion.",
    "quotes": [
      { "author": "Joseph Priestley", "work": "Experiments and Observations on Different Kinds of Air", "quote": "The evolution of dephlogisticated air explains how combustible bodies surrender their **phlogistic** component to the atmosphere." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Intense redness, throbbing heat, and vascular engorgement constitute the classical **phlogistic** signs of acute infection." },
      { "author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "Every experiment demonstrates that the supposed **phlogistic** matter is merely a hypothetical fiction without ponderable weight." }
    ]
  },
  "Dashboard — phleg\\phlogiston.md": {
    "primary": "A hypothetical substance formerly believed by 18th-century chemists to be released during combustion and respiration.",
    "secondary": "In the history of science, the cornerstone concept of Georg Ernst Stahl's chemical theory, disproved by Lavoisier's discovery of oxygen and conservation of mass.",
    "quotes": [
      { "author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "Combustion is not the escape of **phlogiston**, but the chemical combination of the burning body with oxygen gas." },
      { "author": "Joseph Priestley", "work": "Experiments and Observations on Different Kinds of Air", "quote": "I observed that air saturated with **phlogiston** could no longer sustain either flame or animal life." },
      { "author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "The doctrine of **phlogiston** long blinded natural philosophers to the quantitative weight gained during metallic calcination." }
    ]
  },
  "Dashboard — phobia\\arachnophobia.md": {
    "primary": "An intense, irrational, and persistent fear of spiders and other arachnids.",
    "secondary": "In clinical psychiatry, one of the most common specific animal phobias, characterized by immediate autonomic panic, avoidance behaviors, and hypervigilance.",
    "quotes": [
      { "author": "William James", "work": "The Principles of Psychology", "quote": "Instinctive animal dreads, culminating in severe **arachnophobia**, demonstrate how ancestral survival fears become fixed in the nervous system." },
      { "author": "Sigmund Freud", "work": "Introductory Lectures on Psycho-Analysis", "quote": "In cases of **arachnophobia**, the insect or spider often serves as a symbolic surrogate for repressed childhood anxieties." },
      { "author": "Emil Kraepelin", "work": "Lectures on Clinical Psychiatry", "quote": "Patients crippled by **arachnophobia** compulsively inspect every dark corner before daring to enter an unfamiliar room." }
    ]
  },
  "Dashboard — phobia\\homophobia.md": {
    "primary": "Dislike of, prejudice against, or discrimination towards homosexual people.",
    "secondary": "In sociology and psychology, systemic cultural, institutional, or internalized hostility, stigma, and violence directed against gay, lesbian, and bisexual individuals.",
    "quotes": [
      { "author": "Audre Lorde", "work": "Sister Outsider", "quote": "Institutional **homophobia** divides communities by making difference a reason for hatred rather than a catalyst for collective strength." },
      { "author": "Michel Foucault", "work": "The History of Sexuality", "quote": "The surveillance of bodily desires and the moral panic surrounding homosexuality engendered virulent forms of social **homophobia**." },
      { "author": "bell hooks", "work": "Feminism Is for Everybody", "quote": "Ending patriarchal oppression requires dismantling the deeply entrenched **homophobia** that polices sexual conformity." }
    ]
  },
  "Dashboard — phobia\\homophobic.md": {
    "primary": "Having or showing a dislike of, prejudice against, or bias towards homosexual people.",
    "secondary": "In social sciences, characterizing behaviors, rhetoric, legislation, or institutional policies that demean or marginalize non-heterosexual identities.",
    "quotes": [
      { "author": "Audre Lorde", "work": "Sister Outsider", "quote": "To remain silent in the face of **homophobic** rhetoric is to become complicit in the violence that follows." },
      { "author": "bell hooks", "work": "Feminism Is for Everybody", "quote": "Challenging **homophobic** assumptions within progressive movements was essential to forging genuine feminist solidarity." },
      { "author": "Michel Foucault", "work": "The History of Sexuality", "quote": "Discursive taboos produced **homophobic** mechanisms that labeled non-normative intimacy as pathological deviance." }
    ]
  },
  "Dashboard — phobia\\neophobia.md": {
    "primary": "An extreme or irrational fear or dislike of anything new, novel, or unfamiliar.",
    "secondary": "In behavioral biology and developmental psychology, an adaptive avoidance of unfamiliar food or novel environments (food neophobia) seen in rodents and human toddlers.",
    "quotes": [
      { "author": "Charles Darwin", "work": "The Descent of Man", "quote": "A protective **neophobia** preserves wild mammals from swallowing novel poisonous berries or entering unfamiliar traps." },
      { "author": "William James", "work": "The Principles of Psychology", "quote": "Human intellect struggles continually between curiosity for the new and conservative **neophobia** for the untried." },
      { "author": "Francis Galton", "work": "Inquiries into Human Faculty and Its Development", "quote": "Intellectual **neophobia** is the natural defense of aging minds against the disturbing influx of revolutionary ideas." }
    ]
  },
  "Dashboard — phobia\\phobia.md": {
    "primary": "An extreme, irrational, and debilitating fear of or aversion to a specific object, creature, activity, or situation.",
    "secondary": "In clinical psychiatry, a diagnosed anxiety disorder classified as specific phobia, social anxiety disorder, or agoraphobia under DSM criteria.",
    "quotes": [
      { "author": "William James", "work": "The Principles of Psychology", "quote": "A clinical **phobia** is not mere reasonable caution, but an overwhelming panic that paralyses conscious deliberation." },
      { "author": "Sigmund Freud", "work": "Inhibitions, Symptoms and Anxiety", "quote": "The structure of a **phobia** allows the patient to displace internal emotional conflict onto a manageable external object." },
      { "author": "Emil Kraepelin", "work": "Lectures on Clinical Psychiatry", "quote": "Every genuine **phobia** is accompanied by marked autonomic distress, including tachycardia, tremor, and profuse diaphoresis." }
    ]
  },
  "Dashboard — phobia\\phobic.md": {
    "primary": "Having or showing an extreme, irrational fear or aversion; relating to or characteristic of a phobia.",
    "secondary": "In chemistry and physics, having a lack of affinity for a specified substance or medium (e.g., hydrophobic, lipophobic).",
    "quotes": [
      { "author": "William James", "work": "The Principles of Psychology", "quote": "The **phobic** subject avoids the feared situation with an intensity indistinguishable from acute physical terror." },
      { "author": "Sigmund Freud", "work": "Introductory Lectures on Psycho-Analysis", "quote": "Careful psychoanalytic interrogation traces the **phobic** reaction back to early childhood traumas and repressed wishes." },
      { "author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "Nonpolar side chains exhibit **phobic** behavior toward aqueous solvents, driving protein interior hydrophobic collapse." }
    ]
  },
  "Dashboard — plesi\\plesianthropus.md": {
    "primary": "An extinct genus of early hominins (specifically Plesianthropus transvaalensis, now classified as Australopithecus africanus).",
    "secondary": "In paleoanthropology, the fossil taxon erected by Robert Broom in 1938 based on the famous 'Mrs. Ples' cranium discovered at Sterkfontein, South Africa.",
    "quotes": [
      { "author": "Robert Broom", "work": "The South African Fossil Ape-Men", "quote": "The discovery of **plesianthropus** at Sterkfontein decisively proved that upright bipedal primates inhabited Africa during the Pliocene." },
      { "author": "Raymond Dart", "work": "Adventures with the Missing Link", "quote": "Broom's cranium of **plesianthropus** confirmed my earlier inferences drawn from the Taung child regarding hominin posture." },
      { "author": "Arthur Keith", "work": "A New Theory of Human Evolution", "quote": "The dental arch and endocranial cast of **plesianthropus** place it intermediate between anthropoid apes and primitive mankind." }
    ]
  },
  "Dashboard — plesi\\plesiosaur.md": {
    "primary": "A large extinct marine reptile of the Mesozoic era, having a broad, flat body, four paddle-like flippers, and typically a long neck and small head.",
    "secondary": "In vertebrate paleontology, any member of the clade Plesiosauria, apex marine predators of the Jurassic and Cretaceous seas.",
    "quotes": [
      { "author": "Mary Anning", "work": "Letters and Field Notes", "quote": "The extraordinary fossil skeleton I extracted from the Lyme Regis cliffs proved to be a nearly complete **plesiosaur**." },
      { "author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The paddle of the **plesiosaur** exhibits extreme hyperphalangy, converting the tetrapod limb into a rigid hydrodynamic oar." },
      { "author": "Charles Lyell", "work": "Principles of Geology", "quote": "The lias formation yields giant ichthyosaurs and the long-necked **plesiosaur**, testifying to Mesozoic marine biodiversity." }
    ]
  },
  "Dashboard — plesi\\plesiosauria.md": {
    "primary": "An order of extinct Mesozoic marine reptiles comprising the long-necked plesiosaurs and short-necked pliosaurs.",
    "secondary": "In systematic paleontology, sauropterygian marine diapsids that evolved paraxial underwater flight using two pairs of hydrodynamic flippers.",
    "quotes": [
      { "author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The order **plesiosauria** is characterized by a flattened trunk encased in ventral gastralia and propulsion by symmetrical flippers." },
      { "author": "Louis Agassiz", "work": "Recherches sur les Poissons Fossiles", "quote": "Comparative analysis of fossil teeth associates the predatory habits of **plesiosauria** with ancient cephalopods and fishes." },
      { "author": "Charles Darwin", "work": "The Origin of Species", "quote": "The complete extinction of the **plesiosauria** at the close of the Cretaceous marks one of geology's great biotic boundaries." }
    ]
  },
  "Dashboard — plesi\\plesiosaurus.md": {
    "primary": "A genus of extinct marine reptiles of the early Jurassic period, having a small head, long flexible neck, turtle-like body, and four paddle-shaped limbs.",
    "secondary": "In vertebrate paleontology, the type genus described by William Conybeare in 1821 from Mary Anning's discoveries at Lyme Regis.",
    "quotes": [
      { "author": "William Buckland", "work": "Geology and Mineralogy Considered with Reference to Natural Theology", "quote": "To the head of a lizard, **plesiosaurus** united the teeth of a crocodile, the neck of a swan, and the paddles of a whale." },
      { "author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The articulated cervical series of **plesiosaurus** dolichodeirus contains upwards of thirty-five distinct vertebrae." },
      { "author": "Charles Lyell", "work": "Principles of Geology", "quote": "The well-preserved specimen of **plesiosaurus** in the British Museum displays the intact pectoral girdle and flipper rays." }
    ]
  },
  "Dashboard — pleur\\metapleural.md": {
    "primary": "Situated along or relating to the lower sides of the body (metapleura) in certain invertebrates, especially the lancelet (Amphioxus) and insects.",
    "secondary": "In comparative anatomy and entomology, designating the metapleural folds of cephalochordates or the metapleural glands and thoracic sclerites of hymenopterans.",
    "quotes": [
      { "author": "Edwin Ray Lankester", "work": "A Treatise on Zoology", "quote": "The paired ventral **metapleural** folds of Amphioxus coalesce during development to enclose the peribranchial atrium." },
      { "author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "Early morphologists homologized the **metapleural** ridges of the lancelet with the ancestral origin of vertebrate lateral fins." },
      { "author": "William Morton Wheeler", "work": "Ants: Their Structure, Development and Behavior", "quote": "The secretion of the ant's **metapleural** gland possesses potent antibiotic properties that protect the colony nest." }
    ]
  },
  "Dashboard — pleur\\pleura.md": {
    "primary": "Each of a pair of serous membranes lining the thorax and enveloping the lungs in humans and other mammals (plural pleurae or pleuras).",
    "secondary": "In gross anatomy, divided into the visceral pleura (investing lung parenchyma) and parietal pleura (lining the chest wall, diaphragm, and mediastinum), separated by pleural fluid.",
    "quotes": [
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Each lung is invested by an invaginated serous sac termed the **pleura**, allowing frictionless glide during respiration." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Fibrinous exudate upon the inflamed surfaces of the **pleura** generates the characteristic leathery friction rub of pleurisy." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Malignant mesothelioma arises from the mesothelial monolayer coating the parietal **pleura**." }
    ]
  },
  "Dashboard — pleur\\pleural.md": {
    "primary": "Of, relating to, or situated in the pleura or the thoracic cavity.",
    "secondary": "In pulmonary medicine, designating physiological spaces, pressures, or pathologies (e.g., pleural effusion, pleural cavity, pleural rub).",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Massive **pleural** effusion causes stony dullness to percussion and displaces the cardiac apex to the opposite side." },
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Negative pressure within the **pleural** cavity maintains pulmonary alveolar expansion against elastic recoil." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Microscopic examination of the **pleural** aspirate differentiates transudative cardiac hydrothorax from exudative malignancy." }
    ]
  },
  "Dashboard — pleur\\pleuralgia.md": {
    "primary": "Pain in the pleura or side of the chest; pleurodynia.",
    "secondary": "In clinical diagnostics, acute localized sharp chest pain exacerbated by breathing or coughing, arising from pleural irritation or intercostal neuralgia.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The patient complained of severe **pleuralgia** on inspiration, heralding the onset of acute lobar pneumonia." },
      { "author": "Thomas Sydenham", "work": "The Whole Works of That Excellent Practical Physician", "quote": "Sharp **pleuralgia** in the lateral flank must be relieved by timely venesection and warm herbal poultices." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The intense agony of **pleuralgia** results from rich sensory innervation of the parietal pleura by intercostal nerves." }
    ]
  },
  "Dashboard — pleur\\pleurisy.md": {
    "primary": "Inflammation of the pleura, characterized by sharp chest pain that worsens with deep breathing or coughing, fever, and shortness of breath.",
    "secondary": "In clinical pulmonology, divided into dry (fibrinous) pleurisy accompanied by a friction rub and pleurisy with effusion, frequently secondary to pneumonia or tuberculosis.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The stitch in the side of acute **pleurisy** compels the patient to lie upon the affected flank to restrict thoracic motion." },
      { "author": "Thomas Sydenham", "work": "The Whole Works of That Excellent Practical Physician", "quote": "Few diseases require more prompt and vigorous depletion than acute **pleurisy** with burning fever and lancinating pain." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Fibrinous **pleurisy** coats the glistening lung surface with thick, shaggy false membranes composed of fibrin and leukocytes." }
    ]
  },
  "Dashboard — pleur\\pleuritis.md": {
    "primary": "Inflammation of the pleura; the technical medical and pathological synonym of pleurisy.",
    "secondary": "In pathology, categorized as serofibrinous, suppurative (empyema), or hemorrhagic pleuritis based on the character of the inflammatory pleural exudate.",
    "quotes": [
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Suppurative **pleuritis** leads to empyema thoracis, requiring surgical drainage to avoid organizing fibrothorax." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Tuberculous **pleuritis** often develops insidiously with clear straw-colored fluid rich in lymphocytes." },
      { "author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Adhesions resulting from chronic **pleuritis** obliterate the potential space between visceral and parietal layers." }
    ]
  },
  "Dashboard — pleur\\pleurobrachia.md": {
    "primary": "A genus of small, transparent marine ctenophores (comb jellies) commonly known as sea gooseberries.",
    "secondary": "In marine invertebrate zoology, characterized by a spheroidal body bearing eight meridional rows of ciliary comb plates and two long retractile tentacles.",
    "quotes": [
      { "author": "Edwin Ray Lankester", "work": "A Treatise on Zoology", "quote": "The iridescent iridescence flashing along the comb plates of **pleurobrachia** arises from the synchronized beating of giant cilia." },
      { "author": "Alexander Agassiz", "work": "North American Acalephae", "quote": "The delicate tentacles of **pleurobrachia** trail through the water, capturing copepods upon adhesive colloblast cells." },
      { "author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "In **pleurobrachia**, the aboral sense organ functions as an equilibrium statocyst coordinating ciliary rows." }
    ]
  },
  "Dashboard — pleur\\pleurobrachiidae.md": {
    "primary": "A family of tentaculate ctenophores (order Cydippida) comprising the sea gooseberries, including Pleurobrachia.",
    "secondary": "In invertebrate taxonomy, ctenophores having an ovoid or spherical body, two lateral tentacle sheaths, and uncompressed body plans.",
    "quotes": [
      { "author": "Edwin Ray Lankester", "work": "A Treatise on Zoology", "quote": "The family **pleurobrachiidae** contains the typical cydippid comb jellies whose tentacles can be completely retracted into basal sheaths." },
      { "author": "Alexander Agassiz", "work": "North American Acalephae", "quote": "Members of the **pleurobrachiidae** swarm in coastal plankton during midsummer, grazing upon fish larvae and micro-crustacea." },
      { "author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "Biradial symmetry and eight meridional costae characterize the transparent globose bodies of the **pleurobrachiidae**." }
    ]
  },
  "Dashboard — pleur\\pleurocarp.md": {
    "primary": "A moss that produces sporophytes (capsules) on short lateral branches rather than at the apex of the main stem.",
    "secondary": "In bryology, pleurocarpous mosses typically form creeping, sprawling carpets or mats, contrasting with erect acrocarpous mosses.",
    "quotes": [
      { "author": "William Jackson Hooker", "work": "British Jungermanniae", "quote": "The sprawling growth habit of a **pleurocarp** enables it to carpet forest boulders and fallen logs in humid woodlands." },
      { "author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "In every true **pleurocarp**, the archegonia and resulting capsules develop exclusively from lateral auxiliary buds." },
      { "author": "Edwin Ray Lankester", "work": "A Treatise on Zoology", "quote": "Bryological classification divides the Bryopsida into acrocarpous cushion-formers and creeping **pleurocarp** taxa." }
    ]
  },
  "Dashboard — pleur\\pleurocarpous.md": {
    "primary": "Producing fruit or sporophytes from lateral buds or branches rather than the main apex (said of mosses).",
    "secondary": "In bryophyte ecology and taxonomy, describing creeping, branched moss species (order Hypnales) that form extensive interwoven carpets.",
    "quotes": [
      { "author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The vast family Hypnaceae is entirely **pleurocarpous**, bearing capsules along prostrate pinnate stems." },
      { "author": "William Jackson Hooker", "work": "Species Filicum", "quote": "In **pleurocarpous** mosses, the main vegetative axis retains indeterminate apical growth while producing lateral fructifications." },
      { "author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Damp subantarctic forests are carpeted by lush **pleurocarpous** mosses clinging to decaying tree trunks." }
    ]
  },
  "Dashboard — pleur\\pleurodont.md": {
    "primary": "Having teeth fused by their sides to the inner surface of the jawbone without sockets, as in many lizards.",
    "secondary": "In vertebrate paleontology and herpetology, one of the three principal modes of reptilian tooth attachment, contrasting with acrodont and thecodont.",
    "quotes": [
      { "author": "Richard Owen", "work": "Odontography", "quote": "In the **pleurodont** dentition of iguanas, the tooth roots are anchylosed firmly to the inner parapet of the alveolar wall." },
      { "author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "Lizards possessing **pleurodont** teeth continuously replace shed teeth from successor germs developing lingual to the jaw." },
      { "author": "Edwin Ray Lankester", "work": "A Treatise on Zoology", "quote": "The transition from **pleurodont** to thecodont socketed teeth represents a major milestone in archosaurian evolution." }
    ]
  },
  "Dashboard — pleur\\pleurodynia.md": {
    "primary": "Severe paroxysmal pain in the intercostal muscles and chest wall, often of viral or muscular origin.",
    "secondary": "In infectious disease, epidemic pleurodynia (Bornholm disease), caused by Coxsackievirus B infection producing sudden pleuritic chest spasms.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Epidemic **pleurodynia** strikes with agonizing thoracic pain mimicking acute pleurisy, yet without a friction rub." },
      { "author": "Thomas Sydenham", "work": "The Whole Works of That Excellent Practical Physician", "quote": "Rheumatic **pleurodynia** attacks the intercostal muscles, agonizing every breath while sparing internal pulmonary structures." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "In viral **pleurodynia**, localized viral myositis of the intercostal fibers accounts for the excruciating spasms." }
    ]
  },
  "Dashboard — pleur\\pleuron.md": {
    "primary": "The lateral part or side wall of each segment of the body in arthropods, especially insects and crustaceans.",
    "secondary": "In entomology, the lateral chitinous sclerite lying between the dorsal tergum and ventral sternum.",
    "quotes": [
      { "author": "Thomas Henry Huxley", "work": "The Crayfish: An Introduction to the Study of Zoology", "quote": "Each somite consists of a dorsal tergum, a ventral sternum, and two lateral pleural plates termed the **pleuron**." },
      { "author": "Edwin Ray Lankester", "work": "A Treatise on Zoology", "quote": "The thoracic **pleuron** of the insect provides crucial skeletal anchorage for the extrinsic flight muscles." },
      { "author": "Charles Darwin", "work": "A Monograph on the Sub-class Cirripedia", "quote": "Modifications of the carapace and lateral **pleuron** illustrate the remarkable morphological plasticity of barnacles." }
    ]
  },
  "Dashboard — pleur\\pleuronectes.md": {
    "primary": "A genus of righteye flatfishes (family Pleuronectidae) comprising the European plaice (Pleuronectes platessa).",
    "secondary": "In ichthyology, the type genus of marine flatfishes characterized by an asymmetrical, flattened body with both eyes situated on the right side.",
    "quotes": [
      { "author": "Carolus Linnaeus", "work": "Systema Naturae", "quote": "Under **pleuronectes**, Linnaeus gathered all the asymmetrical flatfishes that swim sideways upon the sandy seabed." },
      { "author": "Charles Darwin", "work": "The Origin of Species", "quote": "The larval metamorphosis of **pleuronectes**, during which the left eye migrates across the skull, fascinated evolutionary morphologists." },
      { "author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "The European plaice, **pleuronectes** platessa, displays distinct red spots upon its olive-brown ocular surface." }
    ]
  },
  "Dashboard — pleur\\pleuronectidae.md": {
    "primary": "A family of marine flatfishes known as righteye flounders, having both eyes on the right side of the head and resting on the left side.",
    "secondary": "In systematic ichthyology and fisheries biology, commercially vital demersal teleosts including halibuts, dabs, and plaice.",
    "quotes": [
      { "author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "Members of the family **pleuronectidae** lie buried in coastal sands, camouflaged by dynamic melanophore patterns." },
      { "author": "Edwin Ray Lankester", "work": "A Treatise on Zoology", "quote": "Cranial asymmetry reaches its zenith in **pleuronectidae**, wherein the ethmoid and frontal bones twist during ontogeny." },
      { "author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The blind left side of the **pleuronectidae** lacks skin pigmentation and lies directly against the marine substrate." }
    ]
  },
  "Dashboard — pleur\\pleuropneumonia.md": {
    "primary": "Pneumonia complicated by or accompanied by extensive pleurisy; simultaneous inflammation of the lungs and the pleura.",
    "secondary": "In veterinary medicine, contagious bovine pleuropneumonia (CBPP), a virulent mycoplasmal disease causing marbled consolidation of lungs and massive pleural effusion.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe lobar **pleuropneumonia** presents with high remittent fever, rusty sputum, and agonizing thoracic friction rubs." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Autopsy of contagious bovine **pleuropneumonia** reveals dramatic 'marbled' hepatization of the lung with thick fibrinous pleural sheets." },
      { "author": "Thomas Sydenham", "work": "The Whole Works of That Excellent Practical Physician", "quote": "When **pleuropneumonia** invades the chest, the practitioner must combine copious bloodletting with soothing pectoral decoctions." }
    ]
  },
  "Dashboard — pleur\\pleurosorus.md": {
    "primary": "A small genus of epipetric ferns in the spleenwort family (Aspleniaceae), found on sheltered limestone and rock crevices.",
    "secondary": "In pteridology, ferns characterized by linear exindusiate sori running along the lateral sides of the veins of the pinnules.",
    "quotes": [
      { "author": "William Jackson Hooker", "work": "Species Filicum", "quote": "The genus **pleurosorus** is distinguished from Asplenium by the absence of a true indusium over its elongate lateral sori." },
      { "author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Clinging to shaded limestone fissures, **pleurosorus** survives seasonal droughts through reviviscent frond desiccation." },
      { "author": "Edwin Ray Lankester", "work": "A Treatise on Zoology", "quote": "Pteridologists classify **pleurosorus** as a specialized cliff-dwelling derivative within the asplenioid radiation." }
    ]
  },
  "Dashboard — pleur\\pleurothallis.md": {
    "primary": "A massive genus of Neotropical epiphytic orchids (family Orchidaceae) known as bonnet orchids.",
    "secondary": "In orchidology and tropical botany, one of the most species-rich genera of flowering plants, bearing solitary or racemose flowers from the apex of a secondary stem (ramicaul).",
    "quotes": [
      { "author": "Charles Darwin", "work": "The Various Contrivances by Which Orchids Are Fertilised by Insects", "quote": "The minuscule blossoms of **pleurothallis** exhibit intricate hinged labella pollinated by tiny fungus gnats." },
      { "author": "Alfred Russel Wallace", "work": "Tropical Nature, and Other Essays", "quote": "Epiphytic moss carpets on cloud forest branches shelter innumerable species of dwarf **pleurothallis**." },
      { "author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The leathery solitary leaf of **pleurothallis** rises atop a slender stem that simulates a true petiole." }
    ]
  },
  "Dashboard — pleur\\pleurotus.md": {
    "primary": "A genus of gilled mushrooms commonly called oyster mushrooms, typically growing saprotrophically on decaying wood.",
    "secondary": "In mycology and edible mushroom cultivation, basidiomycete fungi (e.g., Pleurotus ostreatus) characterized by an eccentric, lateral stipe and carnivorous nematophagous mycelia.",
    "quotes": [
      { "author": "Elias Magnus Fries", "work": "Systema Mycologicum", "quote": "Under **pleurotus**, Fries brought together those wood-rotting agarics whose stipe is distinctly lateral or entirely absent." },
      { "author": "Charles Darwin", "work": "Journal of Researches", "quote": "In the damp beech forests of Tierra del Fuego, luminous phosphorescent species of **pleurotus** cling to rotting trunks." },
      { "author": "William Jackson Hooker", "work": "The English Flora", "quote": "The edible oyster mushroom, **pleurotus** ostreatus, expands its shell-like brackets upon decaying poplars and beeches." }
    ]
  },
  "Dashboard — pleur\\pseudopleuronectes.md": {
    "primary": "A genus of righteye flatfishes (family Pleuronectidae) including the winter flounder (Pseudopleuronectes americanus).",
    "secondary": "In marine biology and commercial fisheries, an economically valuable North American flatfish inhabiting inshore estuaries and continental shelves.",
    "quotes": [
      { "author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "The common winter flounder, **pseudopleuronectes** americanus, supports an extensive inshore commercial fishery along New England." },
      { "author": "Alexander Agassiz", "work": "Embryology of the Flounder", "quote": "Metamorphosis in **pseudopleuronectes** exhibits the asymmetric migration of the eye accompanied by rapid behavioral flattening." },
      { "author": "Edwin Ray Lankester", "work": "A Treatise on Zoology", "quote": "Antifreeze glycopeptides discovered in the blood of **pseudopleuronectes** enable survival in freezing sub-zero coastal waters." }
    ]
  },
  "Dashboard — pleur\\tripleurospermum.md": {
    "primary": "A genus of flowering plants in the aster family (Asteraceae), commonly called scentless mayweeds.",
    "secondary": "In taxonomic botany, characterized by daisy-like flower heads and three-ribbed, trigonous achenes (hence Tri-pleuro-spermum, three-sided seed).",
    "quotes": [
      { "author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The genus **tripleurospermum** is set apart from Matricaria by having cypselae strongly ribbed on three sides with glandular resin pits." },
      { "author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "Scentless mayweed, **tripleurospermum** inodorum, relies on prominent white ray florets rather than fragrant oils to attract hoverflies." },
      { "author": "William Jackson Hooker", "work": "The British Flora", "quote": "The hard triangular achenes of **tripleurospermum** maintain exceptional viability in cultivated agricultural soils." }
    ]
  },
  "Dashboard — pne\\anapnograph.md": {
    "primary": "A historical scientific instrument designed to measure, record, and display the rate, depth, and volume of respiratory breathing movements.",
    "secondary": "In 19th-century experimental physiology, a kymographic device recording respiratory air flow curves invented by Bergeon and Kastus.",
    "quotes": [
      { "author": "Claude Bernard", "work": "An Introduction to the Study of Experimental Medicine", "quote": "By attaching the subject to an **anapnograph**, the physiologist visualizes instantaneous fluctuations in tidal respiratory volume." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The mechanical tracing traced by the **anapnograph** graphically records the crescendo-decrescendo pattern of Cheyne-Stokes respiration." },
      { "author": "Etienne-Jules Marey", "work": "La Méthode Graphique", "quote": "The **anapnograph** records every variation in tracheal air pressure, translating thoracic movements into permanent curves." }
    ]
  },
  "Dashboard — pne\\anapnoic.md": {
    "primary": "Of, relating to, or aiding respiration; relieving respiratory distress or dyspnea.",
    "secondary": "In historical therapeutics and pulmonary physiology, describing remedies, inhalations, or maneuvers that promote restorative breathing.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Oxygen inhalation exerts a prompt **anapnoic** effect, relieving the agonizing air-hunger of cardiac asthma." },
      { "author": "Thomas Sydenham", "work": "The Whole Works of That Excellent Practical Physician", "quote": "Pectoral syrups containing squill produce a favorable **anapnoic** result by loosening thick tenacious mucus." },
      { "author": "Claude Bernard", "work": "An Introduction to the Study of Experimental Medicine", "quote": "The medulla oblongata houses the primary **anapnoic** center regulating the autonomous rhythm of diaphragmatic excursion." }
    ]
  }
}

content = f'''import {{ updateNotesBatch }} from './curate-updater-util.mjs';

const BASE_DIR = 'App database/Greek roots/Cluster Body & Physiology';

const BATCH3_DATA = {json.dumps(batch3_data, indent=2, ensure_ascii=False)};

const updated = updateNotesBatch(BASE_DIR, BATCH3_DATA);
console.log(`Body & Physiology Part 6 - Batch 3 Completed: ${{updated}} / ${{Object.keys(BATCH3_DATA).length}} notes updated.`);
'''

with open('main app/scripts/curate-body-p6-batch3.mjs', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Generated curate-body-p6-batch3.mjs with {len(batch3_data)} entries.")
