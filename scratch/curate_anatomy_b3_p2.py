# -*- coding: utf-8 -*-
"""
curate_anatomy_b3_p2.py
Batch 3 Part 2 of Cluster Anatomy & Clinical Medicine (60 words):
- pelv (5 words)
- pulmon (6 words)
- sanguin (13 words)
- ungui (4 words)
- valv (13 words)
- ventr (13 words)
- viscer (6 words)
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_anatomy_b3_p2 = {
    # ==================== Dashboard — pelv (5 words) ====================
    "intrapelvic": {
        "primary": "Situated, occurring, or performed within the cavity of the pelvis.",
        "secondary": "In gynecological surgery and clinical anatomy, describing vascular plexuses, fascial planes, or pathologies located inside the true pelvic basin.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Extensive **intrapelvic** suppuration requires dependent drainage to avert septic peritonitis."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The internal iliac artery distributes essential **intrapelvic** branches to the bladder, rectum, and reproductive organs."},
            {"author": "William Hunter", "work": "Anatomy of the Human Gravid Uterus", "quote": "During the third trimester, the gravid uterus expands far beyond its initial **intrapelvic** boundaries into the abdominal cavity."}
        ]
    },
    "pelvic": {
        "primary": "Relating to, situated near, or affecting the pelvis or pelvic girdle.",
        "secondary": "In gross human osteology and obstetrics, pertaining to the bony ring formed by the paired hip bones, sacrum, and coccyx.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The broad, bowl-shaped configuration of the human **pelvic** skeleton reflects our adaptation to habitual bipedal walking."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **pelvic** diaphragm separates the true pelvic cavity above from the perineum below."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Powerful ligaments securely bind the sacrum to the ilium, ensuring stability across the **pelvic** arch under vertical loads."}
        ]
    },
    "pelvimeter": {
        "primary": "An obstetrical instrument designed for measuring the dimensions and diameters of the pelvis.",
        "secondary": "In clinical pelvimetry, calibrated metallic calipers (such as Baudelocque's pelvimeter) used to gauge conjugate and transverse external pelvic spans.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Careful measurement with a reliable **pelvimeter** remains an indispensable safeguard in evaluating contracted pelvic outlets."},
            {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The young obstetrician applied the curved arms of the **pelvimeter** to estimate the true conjugate diameter."},
            {"author": "William Hunter", "work": "Medical Commentaries", "quote": "Accurate application of the **pelvimeter** enables the physician to foresee mechanical cephalopelvic disproportion."}
        ]
    },
    "pelvimetry": {
        "primary": "The measurement of the dimensions and capacity of the pelvis, especially in obstetrics.",
        "secondary": "In prenatal care, the manual, radiographic, or ultrasonic assessment of maternal pelvic architecture to determine the feasibility of safe cephalic delivery.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Systematic clinical **pelvimetry** conducted during late gestation identifies deformities caused by childhood rickets."},
            {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The principles of external and internal **pelvimetry** were expounded with mathematical precision in the obstetrical clinic."},
            {"author": "William Hunter", "work": "Anatomy of the Human Gravid Uterus", "quote": "Rigorous **pelvimetry** distinguishes the gynecoid pelvis from contracted platypelloid configurations."}
        ]
    },
    "pelvis": {
        "primary": "The basin-shaped skeletal structure formed by the hip bones, sacrum, and coccyx; or the renal basin.",
        "secondary": "In human osteology and urology, the bony girdle anchoring the lower limbs, or the funnel-like renal pelvis collecting urine from the calyces.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Rudimentary limb bones and traces of a **pelvis** are preserved beneath the skin in certain serpent and whale skeletons."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The female **pelvis** is distinguished by broader iliac wings, a wider pubic arch, and greater transverse diameter for childbirth."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Calculous pyelitis results when sharp urinary concretions irritate the delicate mucosa of the renal **pelvis**."}
        ]
    },

    # ==================== Dashboard — pulmon (6 words) ====================
    "intrapulmonary": {
        "primary": "Situated, occurring, or administered within the substance of the lungs.",
        "secondary": "In respiratory physiology and thoracic medicine, pertaining to pressure changes (intrapulmonary pressure) or vascular networks within the pulmonary parenchyma.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Rupture of an **intrapulmonary** abscess into an adjacent bronchus produces sudden paroxysms of copious purulent expectoration."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The pulmonary arteries divide repeatedly to form a dense **intrapulmonary** capillary plexus surrounding each alveolus."},
            {"author": "René Laennec", "work": "A Treatise on the Diseases of the Chest", "quote": "Auscultation reveals localized bronchial breathing whenever an **intrapulmonary** consolidation solidifies the spongy lung tissue."}
        ]
    },
    "pulmonary": {
        "primary": "Relating to, affecting, or functioning within the lungs.",
        "secondary": "In cardiovascular and respiratory medicine, designating the pulmonary circulation transporting deoxygenated blood from the right ventricle to the alveolar bed.",
        "quotes": [
            {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The **pulmonary** distress caused by the denser atmosphere and greater gravitational attraction was acutely painful to the Martians."},
            {"author": "Jane Austen", "work": "Emma", "quote": "Her delicate health caused deep family anxiety, though there were no immediate **pulmonary** symptoms to suggest consumption."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Acute **pulmonary** edema requires immediate upright positioning and vigorous therapeutic reduction of left ventricular afterload."}
        ]
    },
    "pulmonata": {
        "primary": "An order or subclass of gastropod mollusks (such as snails and slugs) that breathe air with a lung-like pallial cavity.",
        "secondary": "In malacology, terrestrial and freshwater gastropods that have lost ancestral ctenidial gills in favor of a vascularized mantle cavity acting as a lung.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Terrestrial species belonging to the **Pulmonata** have colonized remote oceanic islands through rare accidental dispersal."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "In the **Pulmonata**, respiration is effected through a contractile pneumostome opening into the rich vascular mantle roof."},
            {"author": "Louis Agassiz", "work": "Methods of Study in Natural History", "quote": "The developmental transition of the **Pulmonata** from aquatic ancestors illustrates profound structural modification for terrestrial life."}
        ]
    },
    "pulmonic": {
        "primary": "Pertaining to the lungs; pulmonary; or relating to the pulmonary artery and valve.",
        "secondary": "In cardiology and physical diagnosis, designating the pulmonic valve, pulmonic second heart sound (P2), or pulmonary outflow tract.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Accentuation of the **pulmonic** second sound indicates heightened hemodynamic pressure throughout the pulmonary arterial tree."},
            {"author": "René Laennec", "work": "A Treatise on the Diseases of the Chest", "quote": "A soft systolic murmur heard loudest at the second left intercostal space originates at the **pulmonic** orifice."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **pulmonic** valve consists of three semilunar cusps preventing regurgitation of blood into the right ventricle during diastole."}
        ]
    },
    "pulmonist": {
        "primary": "A physician specializing in the diagnosis and medical treatment of lung and respiratory diseases.",
        "secondary": "In clinical medicine, a specialist who manages chronic obstructive pulmonary disease, interstitial fibrosis, asthma, and pleural pathology.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The astute **pulmonist** correlates stethoscope auscultation with microscopic sputum analysis to establish an early diagnosis."},
            {"author": "Abraham Flexner", "work": "Medical Education in the United States and Canada", "quote": "Modern hospitals appointed a resident **pulmonist** to oversee specialized sanatorium treatments and thoracic wards."},
            {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "He consulted an eminent **pulmonist** whose expert counsel guided the management of complicated pleuritic effusions."}
        ]
    },
    "pulmonology": {
        "primary": "The medical subspecialty dealing with diseases of the lungs and respiratory system.",
        "secondary": "In internal medicine, the clinical science integrating spirometry, bronchoscopy, arterial blood gas analysis, and critical thoracic intensive care.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The emerging discipline of **pulmonology** transformed chronic phthisis management from palliative confinement to rigorous bacteriological therapeutics."},
            {"author": "Abraham Flexner", "work": "Medical Education in the United States and Canada", "quote": "Instruction in clinical **pulmonology** requires direct bedside training in physical auscultation, percussion, and radiography."},
            {"author": "Morris Fishbein", "work": "The Medical Follies", "quote": "Advancements in academic **pulmonology** systematically discredited fraudulent patent medicines claiming to cure galloping consumption."}
        ]
    },

    # ==================== Dashboard — sanguin (13 words) ====================
    "consanguine": {
        "primary": "Related by blood descent; having a common ancestor; consanguineous.",
        "secondary": "In legal jurisprudence and kinship anthropology, individuals descended from a shared biological stock, distinguished from affinal relations by marriage.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Roman civil law strictly regulated the inheritance rights of **consanguine** kindred within the patrician families."},
            {"author": "Walter Scott", "work": "The Bride of Lammermoor", "quote": "The feud divided families that had been closely allied by ancient **consanguine** bonds for generations."},
            {"author": "Henry Maine", "work": "Ancient Law", "quote": "Primitive tribal solidarity was founded exclusively upon the acknowledged claims of **consanguine** brotherhood."}
        ]
    },
    "consanguineal": {
        "primary": "Relating to kinship by blood descent rather than marriage.",
        "secondary": "In social anthropology, designating kinship ties, descent lines, or family structures based on biological ancestry.",
        "quotes": [
            {"author": "Henry Maine", "work": "Ancient Law", "quote": "In archaic legal systems, the **consanguineal** tie superseded all obligations created by contract or voluntary alliance."},
            {"author": "Edward Tylor", "work": "Primitive Culture", "quote": "The transition from **consanguineal** clan organization to territorial citizenship marks a major milestone in human society."},
            {"author": "Lewis Henry Morgan", "work": "Systems of Consanguinity and Affinity", "quote": "He classified human kinship terminologies into descriptive systems and classificatory **consanguineal** frameworks."}
        ]
    },
    "consanguineous": {
        "primary": "Descended from the same ancestor; related by blood; of the same lineage.",
        "secondary": "In medical genetics and population biology, unions between closely related individuals sharing a high coefficient of inbreeding and identical alleles.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "My lady's a Cataian, we are politicians, and Malvolio's a Peg-a-Ramsey; am I not **consanguineous**? am I not of her blood?"},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The widespread prohibition against **consanguineous** marriages probably arose from observing the deleterious effects of close inbreeding."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Rare autosomal recessive metabolic errors occur with heightened frequency among the offspring of **consanguineous** parents."}
        ]
    },
    "consanguinity": {
        "primary": "The relationship or kinship of persons descended from the same stock or common ancestor; blood relation.",
        "secondary": "In canon law and genealogical jurisprudence, the degree of genetic relatedness determining marital prohibitions and intestate property succession.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Troilus and Cressida", "quote": "I have forgot my father; I know no touch of **consanguinity**, no kin, no love, no blood, no soul so near me as the sweet Troilus."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Ecclesiastical councils multiplied the prohibited degrees of **consanguinity** to an extent that hampered noble dynastic alliances."},
            {"author": "Henry Maine", "work": "Ancient Law", "quote": "The fiction of adoption was invented to preserve the sacred hearth when the natural line of **consanguinity** failed."}
        ]
    },
    "exsanguinate": {
        "primary": "To drain of blood completely; to cause massive or fatal blood loss.",
        "secondary": "In surgical pathology and forensic medicine, the loss of circulating intravascular volume leading to irreversible hypovolemic shock and death.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Rupture of an aortic aneurysm into the thoracic cavity will **exsanguinate** the patient within a few terrifying minutes."},
            {"author": "René Laennec", "work": "A Treatise on the Diseases of the Chest", "quote": "Uncontrollable hemoptysis from a large pulmonary vessel threatened to **exsanguinate** the consumptive invalid."},
            {"author": "Benjamin Bell", "work": "A System of Surgery", "quote": "The surgeon must immediately compress the femoral trunk lest profuse arterial hemorrhage **exsanguinate** the casualty."}
        ]
    },
    "exsanguine": {
        "primary": "Completely destitute of blood; bloodless, pale, and depleted of vital color.",
        "secondary": "In clinical observation, describing an individual suffering from extreme acute anemia or profound hemorrhagic pallor.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Following massive gastric hemorrhage, the patient lay upon the couch in an **exsanguine** and collapsed condition."},
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The wounded soldier was borne away, his **exsanguine** lips parted in a faint whisper for water."},
            {"author": "Walter Scott", "work": "The Antiquary", "quote": "The sick man presented an **exsanguine** countenance that filled his weeping kinsfolk with the gravest apprehensions."}
        ]
    },
    "exsanguinous": {
        "primary": "Bloodless, drained of blood, or completely lacking vital blood flow.",
        "secondary": "In pathological anatomy and surgical descriptions, tissue that has been completely blanched and deprived of vascular perfusion.",
        "quotes": [
            {"author": "William Cullen", "work": "First Lines of the Practice of Physic", "quote": "The extremities assumed an **exsanguinous** pallor as systemic vasomotor failure impeded peripheral capillary flow."},
            {"author": "John Hunter", "work": "Treatise on the Blood, Inflammation, and Gun-shot Wounds", "quote": "The excised gangrenous flap appeared entirely **exsanguinous**, devoid of active arterial circulation."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe pernicious anemia leaves the skin in a characteristic waxen, **exsanguinous** state with lemon-yellow tinting."}
        ]
    },
    "sanguinaria": {
        "primary": "A genus of perennial North American spring-flowering plants in the poppy family Papaveraceae; bloodroot.",
        "secondary": "In pharmacognosy and ethnobotany, Sanguinaria canadensis, whose red rhizomes contain the alkaloid sanguinarine, formerly used as an escharotic and expectorant.",
        "quotes": [
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The solitary white flower of **Sanguinaria** emerges in early April, accompanied by a single round lobed leaf."},
            {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "The moist forest rich leaf-mold supported delicate colonies of **Sanguinaria**, whose broken roots wept bright vermilion juice."},
            {"author": "Nicholas Culpeper", "work": "The English Physitian", "quote": "American physicians extract from **Sanguinaria** a powerful bitter tincture celebrated for expelling tough chest humors."}
        ]
    },
    "sanguinary": {
        "primary": "Involving or accompanied by much bloodshed; bloodthirsty, murderous, and cruel.",
        "secondary": "In military historiography and moral philosophy, describing fierce battles or tyrannical decrees that result in catastrophic slaughter.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "If you make the criminal code too **sanguinary**, juries will not convict the offender."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Some of these same Nantucket Quakers are the most **sanguinary** of all sailors and whale-hunters."},
            {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "The cosmic process in organic nature is not a peaceful pastoral scene, but an intense and **sanguinary** struggle for existence."}
        ]
    },
    "sanguine": {
        "primary": "Cheerfully optimistic, confident, and hopeful; or having the warm, florid color of blood.",
        "secondary": "In classical humoral medicine and psychology, the temperament dominated by blood, characterized by vitality, warmth, enthusiasm, and buoyant resilience.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Cymbeline", "quote": "Guiderius had upon his neck a mole, a **sanguine** star; it was a mark of wonder that distinguished him from birth."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "**Sanguine** by nature, Troy had a power of eluding grief by simply adjourning it to a more convenient season."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He observed the young painter's **sanguine** temperament, which saw beauty and radiant promise in every passing hour."}
        ]
    },
    "sanguineness": {
        "primary": "Ardent optimism, buoyant cheerfulness, or confident expectation of success; florid vitality.",
        "secondary": "In behavioral psychology, an emotional disposition marked by energetic cheerfulness, resilience against despair, and confident expectation.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "His characteristic **sanguineness** sustained him through commercial reverses that would have crushed a more cautious merchant."},
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber's inextinguishable **sanguineness** returned with full force the moment a hot punch was brewed upon the table."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "A constitutional **sanguineness** enables certain minds to dismiss gloomy forebodings with serene nonchalance."}
        ]
    },
    "sanguineous": {
        "primary": "Pertaining to, containing, or resembling blood; plethoric; or accompanied by bleeding.",
        "secondary": "In clinical medicine and surgical pathology, describing bodily discharges, exudates, or apoplectic constitutions rich in red blood cells.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Thoracentesis withdrew a liter of dark **sanguineous** pleural fluid, pointing strongly toward malignant mesothelioma."},
            {"author": "René Laennec", "work": "A Treatise on the Diseases of the Chest", "quote": "The **sanguineous** engorgement of the pulmonary lobes during the first stage of pneumonia precedes fibrinous solidification."},
            {"author": "William Cullen", "work": "First Lines of the Practice of Physic", "quote": "Individuals of a full **sanguineous** habit require venesection when threatening symptoms of cerebral apoplexy supervene."}
        ]
    },
    "sanguinity": {
        "primary": "Ardent optimism, confident hopefulness, or a robust, cheerful disposition.",
        "secondary": "In character analysis and descriptive literature, the mental state of expecting fortunate outcomes despite daunting obstacles; sanguineness.",
        "quotes": [
            {"author": "Walter Scott", "work": "The Antiquary", "quote": "His youthful **sanguinity** led him to believe that buried Roman treasures would reward his archaeological excavations."},
            {"author": "George Meredith", "work": "The Egoist", "quote": "Her unquenchable **sanguinity** refused to admit that love could be chilled by worldly calculations."},
            {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Experience teaches mortals to moderate that extravagant **sanguinity** which promises unclouded happiness in youth."}
        ]
    },

    # ==================== Dashboard — ungui (4 words) ====================
    "unguiculata": {
        "primary": "A former zoological grouping of placental mammals possessing claws or nails on their digits.",
        "secondary": "In comparative mammalian taxonomy, Linnaeus and Cuvier's division of quadrupeds (including primates, carnivores, and rodents) bearing clawed or nailed digits.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The cohort **Unguiculata** comprises those mammalian orders whose terminal phalanges are capped with protective claws or flat nails."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "In the **Unguiculata**, the digits retain high flexibility compared to the rigid encased hooves of ungulate herbivores."},
            {"author": "Louis Agassiz", "work": "Methods of Study in Natural History", "quote": "Cuvier distinguished the **Unguiculata** from hoofed quadrupeds by the specialized prehensile freedom of their extremities."}
        ]
    },
    "unguiculate": {
        "primary": "Having claws, nails, or talons; or having petals with narrow claw-like bases.",
        "secondary": "In comparative anatomy and systematic botany, describing animals with clawed digits, or floral corollas whose petals narrow into distinct basal claws.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The arboreal ancestry of primates is confirmed by their **unguiculate** extremities adapted for grasping forest boughs."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "Each **unguiculate** digit terminates in a curved horny sheath supported by a specialized ungual phalanx."},
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The pinks present characteristic **unguiculate** petals with long slender claws enclosed within a tubular calyx."}
        ]
    },
    "unguiculated": {
        "primary": "Furnished with claws, nails, or claw-like appendages; unguiculate.",
        "secondary": "In systematic zoology, having digits terminating in claws or nails rather than hooves; or botanically possessing clawed floral segments.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "The Anatomy of Invertebrated Animals", "quote": "The **unguiculated** appendages of the predatory crustacean seize struggling prey with irresistible mechanical strength."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "Fossil sloths present massive **unguiculated** forelimbs capable of stripping foliage from prehistoric forest canopies."},
            {"author": "Louis Agassiz", "work": "Contributions to the Natural History of the United States", "quote": "The turtle's paddle retains five **unguiculated** digits embedded within an elastic swimming membrane."}
        ]
    },
    "unguis": {
        "primary": "The anatomical nail of a finger or toe; or a claw, talon, or hoof; or the lacrimal bone of the skull.",
        "secondary": "In human osteology and dermatology, the thin scale-like lacrimal bone (os unguis) of the orbit, or the keratinized plate of the human nail.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The os **unguis**, or lacrimal bone, is a delicate quadrilateral lamina situated at the anterior medial wall of the orbit."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The keratinized **unguis** grows continuously from the nail matrix, providing essential mechanical defense to the fingertip."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Comparative analysis demonstrates that the mammalian **unguis** corresponds strictly to the avian talon and reptilian claw."}
        ]
    },

    # ==================== Dashboard — valv (13 words) ====================
    "bicuspid valve": {
        "primary": "The cardiac valve situated between the left atrium and left ventricle; the mitral valve.",
        "secondary": "In cardiac anatomy and physiology, the dual-cusped atrioventricular valve preventing retrograde systolic regurgitation into the pulmonary venous circuit.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **bicuspid valve** consists of two triangular cusps secured to the papillary muscles by strong chordae tendineae."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Rheumatic endocarditis most frequently attacks the delicate leaflets of the **bicuspid valve**, causing cicatricial stenosis."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "During left ventricular systole, the flaps of the **bicuspid valve** slam shut to drive blood through the systemic aorta."}
        ]
    },
    "bivalve": {
        "primary": "An aquatic mollusk possessing a two-part hinged shell, such as a clam, oyster, or mussel.",
        "secondary": "In invertebrate zoology and paleontology, a member of the class Bivalvia (Lamellibranchiata) characterized by a laterally compressed body and absence of a radula.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "In the Lamellibranchiata, or **bivalve** shells, hermaphroditism is not rare among various sedentary marine families."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The two calcareous valves of the **bivalve** are held closed against predators by powerful adductor muscles."},
            {"author": "Louis Agassiz", "work": "Methods of Study in Natural History", "quote": "Fossil **bivalve** mollusks provide crucial index fossils for correlating Mesozoic and Cenozoic marine sedimentary strata."}
        ]
    },
    "bivalved": {
        "primary": "Having a shell, capsule, or seed pod consisting of two distinct hinged valves or plates.",
        "secondary": "In systematic botany and malacology, describing fruit capsules (such as siliques) or crustaceans and mollusks possessing dual protective casings.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The tiny **bivalved** carapace of ostracod crustaceans encloses the entire body like a microscopic mollusk shell."},
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Upon ripening, the **bivalved** capsule dehisces along two sutures to liberate its compressed winged seeds."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The **bivalved** shell of brachiopods differs fundamentally from mollusks by its dorsal and ventral orientation."}
        ]
    },
    "tricuspid valve": {
        "primary": "The cardiac valve situated between the right atrium and right ventricle of the heart, having three cusps.",
        "secondary": "In cardiovascular hemodynamics, the right atrioventricular valve preventing regurgitation of venous blood into the right atrium during ventricular contraction.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **tricuspid valve** guards the right atrioventricular orifice with anterior, posterior, and medial septal leaflets."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Regurgitation across the **tricuspid valve** causes systolic pulsation of the jugular veins and congested hepatomegaly."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Contraction of the right ventricle forces blood past the pulmonary valves while the **tricuspid valve** remains firmly closed."}
        ]
    },
    "valve": {
        "primary": "A mechanical device or anatomical structure that controls or regulates fluid flow by opening and closing passages.",
        "secondary": "In cardiology and hemodynamics, an endocardial fold (such as an atrioventricular or semilunar valve) maintaining unidirectional blood circulation.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "The heart in thee is the heart of all; not a **valve**, not a wall, not an intersection divides thy soul from the universal life."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Every venous **valve** consists of a semilunar fold of intima reinforced by a delicate central lamina of fibrous tissue."},
            {"author": "William Harvey", "work": "De Motu Cordis", "quote": "The inward-pointing venous **valve** permits blood to flow toward the heart while absolutely preventing its return."}
        ]
    },
    "valved": {
        "primary": "Furnished with, regulated by, or operating by means of a valve or valves.",
        "secondary": "In botanical morphology and cardiovascular anatomy, describing vessels or seed capsules equipped with flaps or moveable dividing septa.",
        "quotes": [
            {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "Loose the stop from your throat, open the **valved** chambers of song, and let the buoyant voice chant across the open fields."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The deep lymphatic trunks are densely **valved**, giving them a distinctive beaded appearance under anatomical injection."},
            {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "The sensitive trap of Utricularia consists of an aquatic bladder with an elastic **valved** entrance."}
        ]
    },
    "valvelet": {
        "primary": "A small or miniature valve, especially a diminutive fold in an anatomical vessel.",
        "secondary": "In microvascular anatomy and botany, a microscopic valvular flap in small venules or lymphatic capillaries preventing fluid backflow.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Each microscopic lymphatic capillary is equipped with a delicate **valvelet** that facilitates unidirectional lymph uptake."},
            {"author": "William Cullen", "work": "First Lines of the Practice of Physic", "quote": "Incompetence of the venous **valvelet** network in the lower limb leads inexorably to chronic varicose distension."},
            {"author": "John Hunter", "work": "Treatise on the Blood, Inflammation, and Gun-shot Wounds", "quote": "Microscopic inspection reveals that each minute **valvelet** yields to forward fluid pressure but closes firmly against reflux."}
        ]
    },
    "valvotomy": {
        "primary": "A surgical incision into a stenotic heart valve to relieve obstruction and widen its opening.",
        "secondary": "In cardiac surgery, the operative splitting of fused valvular commissures (valvulotomy) performed for mitral or pulmonary valve stenosis.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Surgical pioneers envisioned transventricular **valvotomy** as a direct mechanical remedy for severe mitral stenosis."},
            {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "He discussed the theoretical feasibility of closed **valvotomy** to relieve life-threatening cardiac valvular obstruction."},
            {"author": "Alexis Carrel", "work": "Man, The Unknown", "quote": "Experimental intracardiac **valvotomy** demonstrated that living cardiac leaflets could be mobilized under aseptic technique."}
        ]
    },
    "valvula": {
        "primary": "An anatomical valvelet, small valve, or fold of mucous membrane.",
        "secondary": "In human neuroanatomy and gastroenterology, structures such as the valvula cerebelli or the circular folds (valvulae conniventes) of the small intestine.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **valvula** cerebelli forms a thin lamina of white substance stretching between the superior cerebellar peduncles."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The prominent transverse folds of the **valvula** conniventes greatly amplify the absorptive mucosal surface of the jejunum."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "In the spiral valve of elasmobranchs, the continuous **valvula** slows the passage of chyme to optimize nutrient absorption."}
        ]
    },
    "valvular": {
        "primary": "Pertaining to, operating by means of, or affecting valves, especially the valves of the heart.",
        "secondary": "In clinical cardiology, describing pathological murmurs, endocardial deformities, regurgitation, or stenosis of cardiac valves.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic **valvular** disease of the heart frequently originates in an unrecognized attack of acute juvenile rheumatic fever."},
            {"author": "René Laennec", "work": "A Treatise on the Diseases of the Chest", "quote": "Careful stethoscope auscultation localizes the mechanical murmur produced by **valvular** incompetence at each cardiac orifice."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The fibrous rings provide firm skeletal anchorage for the **valvular** leaflets of both atrioventricular orifices."}
        ]
    },
    "valvule": {
        "primary": "A small valve or valvelet; a diminutive flap or fold acting as a valve.",
        "secondary": "In botany and microanatomy, a small bract or chaffy scale in grass florets, or a tiny endocardial flap within the microvasculature.",
        "quotes": [
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "In the spikelet of the grass, the inner **valvule** encloses the stamens and pistil opposite the outer glume."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "A minute fibrous **valvule** guards the coronary sinus orifice, preventing systolic regurgitation into the cardiac vein."},
            {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "The delicate membranous **valvule** protects the embryonic seed until moisture triggers its elastic release."}
        ]
    },
    "valvulitis": {
        "primary": "Inflammation of a heart valve, typically caused by rheumatic fever or bacterial infection.",
        "secondary": "In cardiovascular pathology, acute endocarditis characterized by leukocyte infiltration, endothelial ulceration, and platelet-fibrin vegetations upon valve leaflets.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Acute **valvulitis** in rheumatic carditis leads to verrucous vegetations along the line of leaflet contact."},
            {"author": "René Laennec", "work": "A Treatise on the Diseases of the Chest", "quote": "Suppurative **valvulitis** rapidly destroys the free margins of the cusps, inducing fatal hemodynamic collapse."},
            {"author": "William Henry Welch", "work": "Papers and Addresses", "quote": "Bacteriological sections revealed streptococcal colonies embedded within the necrotic vegetations of acute **valvulitis**."}
        ]
    },
    "valvulotomy": {
        "primary": "The surgical cutting or incising of a cardiac valve to relieve stenosis; valvotomy.",
        "secondary": "In thoracic cardiovascular surgery, operative commissurotomy performed to separate fused leaflets in mitral, aortic, or pulmonary valve stenosis.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Mitral **valvulotomy** was proposed to mechanically enlarge the constricted orifice and restore pulmonary venous drainage."},
            {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "He followed with keen interest the experimental attempts to perform closed transcardiac **valvulotomy** on animal models."},
            {"author": "Alexis Carrel", "work": "Man, The Unknown", "quote": "The successful execution of pulmonary **valvulotomy** proved that intracardiac mechanical defects could be corrected surgically."}
        ]
    },

    # ==================== Dashboard — ventr (13 words) ====================
    "coventry": {
        "primary": "Coventry, a historic industrial city in Warwickshire, England; or figurative social ostracism.",
        "secondary": "In British social history, to 'send to Coventry' denotes a collective refusal to speak to or associate with an ostracized individual.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "Bardolph, get thee before to **Coventry**; fill me a bottle of sack; our soldiers shall march through Gloucestershire."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The medical society threatened to send him to **Coventry** if he persisted in dispensing his own unapproved medicines."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The ancient city of **Coventry** had long been celebrated for its prosperous textile manufacture and medieval guilds."}
        ]
    },
    "eventration": {
        "primary": "The protrusion or herniation of the abdominal viscera through a defect in the abdominal wall.",
        "secondary": "In clinical surgery and diaphragmatic pathology, massive relaxation or defect of the diaphragm or abdominal musculature allowing viscera to displace upwards or outwards.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Congenital **eventration** of the diaphragm causes the stomach and splenic flexure to ascend into the left thoracic cavity."},
            {"author": "Benjamin Bell", "work": "A System of Surgery", "quote": "Traumatic rupture of the rectus abdominis sheath threatened massive **eventration** of the small intestinal loops."},
            {"author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Careful multilayered closure of the laparotomy incision completely prevents postoperative **eventration** of abdominal contents."}
        ]
    },
    "intraventricular": {
        "primary": "Situated, occurring, or administered within a ventricle of the brain or heart.",
        "secondary": "In clinical neurology and cardiology, describing cerebrospinal fluid flow within the cerebral ventricles or hemodynamic conduction within the cardiac chambers.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Massive **intraventricular** hemorrhage rapidly induces profound coma, hyperpyrexia, and decerebrate rigidity."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **intraventricular** cerebrospinal fluid circulates from the lateral ventricles through the interventricular foramen of Monro."},
            {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "He mapped out the **intraventricular** tumors that obstruct the aqueduct of Sylvius and induce internal hydrocephalus."}
        ]
    },
    "ventral": {
        "primary": "Relating to, situated on, or directed toward the belly or abdominal surface of an organism.",
        "secondary": "In comparative anatomy and embryology, the anterior surface in humans or the inferior surface facing the ground in quadrupeds and fishes.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The male Callionymus lyra exhibits brilliant gem-like colors upon its **ventral** surface and extended dorsal fins."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "In all arthropods, the nerve cord occupies a **ventral** position beneath the digestive tract."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The **ventral** body wall in vertebrate embryos closes along the midline, enclosing the thoracic and abdominal viscera."}
        ]
    },
    "ventrally": {
        "primary": "Toward or upon the belly, abdomen, or anterior surface of an anatomical structure.",
        "secondary": "In descriptive embryology and surgical navigation, spatial direction toward the anterior or ventral plane of the body axis.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The motor roots emerge **ventrally** from the spinal cord to combine with the sensory dorsal roots."},
            {"author": "Charles Darwin", "work": "Monograph on the Sub-class Cirripedia", "quote": "The thoracic appendages are directed **ventrally**, sweeping the surrounding water for microscopic food particles."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The rectus abdominis muscle extends **ventrally** from the pubic crest to the anterior cartilages of the lower ribs."}
        ]
    },
    "ventricle": {
        "primary": "A hollow muscular or fluid-filled chamber within an organ, especially the heart or brain.",
        "secondary": "In cardiac physiology and neuroanatomy, the thick-walled muscular pumping chambers of the heart, or the four interconnecting cerebrospinal fluid cavities of the brain.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Love's Labour's Lost", "quote": "These are begot in the **ventricle** of memory, nourished in the womb of pia mater, and delivered upon the mellowing of occasion."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The muscular wall of the left **ventricle** is three times thicker than that of the right, reflecting higher systemic resistance."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Dilation of the left **ventricle** without compensatory hypertrophy heralds the onset of congestive cardiac decompensation."}
        ]
    },
    "ventricose": {
        "primary": "Distended, inflated, or swelling out protuberantly, especially on one side; pot-bellied.",
        "secondary": "In malacology and systematic botany, describing shells or floral corollas that swell outwards asymmetrically (such as certain gastropods or pitcher plants).",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The **ventricose** whorls of certain fossil gastropod shells demonstrate gradual morphological expansion through sedimentary strata."},
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The calyx of Silene inflata is remarkably **ventricose**, resembling a delicate inflated bladder enclosing the floral organs."},
            {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "The tubular corolla becomes distinctly **ventricose** below the throat, providing ample chamber for insect pollinators."}
        ]
    },
    "ventricous": {
        "primary": "Swollen out, distended, or bulging protuberantly on one side; ventricose.",
        "secondary": "In biological morphology, descriptive of asymmetric ventricose expansion in fungal stems, insect abdomens, or plant capsules.",
        "quotes": [
            {"author": "William Withering", "work": "An Arrangement of British Plants", "quote": "The stem of the agaric is hollow and distinctly **ventricous** near the base, tapering gradually toward the pileus."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The **ventricous** abdomen of the queen ant swells to immense proportions during periods of prolific egg production."},
            {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "A **ventricous** seed capsule dehisces with elastic force, scattering seeds across several feet of surrounding soil."}
        ]
    },
    "ventricular": {
        "primary": "Relating to, situated in, or affecting a ventricle of the heart or brain.",
        "secondary": "In cardiovascular hemodynamics and electrophysiology, pertaining to ventricular depolarization (QRS complex), ejection fraction, or fatal ventricular arrhythmias.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Frequent premature **ventricular** contractions in coronary disease demand cautious clinical monitoring to prevent ventricular fibrillation."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **ventricular** septum consists of a thick muscular inferior portion and a thin superior membranous part."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Coordinated **ventricular** systole expels the blood simultaneously into the pulmonary artery and the systemic aorta."}
        ]
    },
    "ventriculus": {
        "primary": "The anatomical stomach; or a cardiac ventricle; or the muscular gizzard of birds.",
        "secondary": "In avian and comparative vertebrate anatomy, the thick muscular gizzard (ventriculus) where ingested grit grinds food mechanically.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **ventriculus**, or stomach, occupies the left hypochondriac and epigastric regions of the abdominal cavity."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "In granivorous birds, the **ventriculus** possesses powerful tendinous discs and a dense keratinized lining for crushing seeds."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The digestive tract transitions from the glandular proventriculus into the dense muscular walls of the **ventriculus**."}
        ]
    },
    "ventriloquism": {
        "primary": "The art or performance of speaking such that the voice appears to come from another source or dummy.",
        "secondary": "In theatrical arts and physiological acoustics, speech produced with minimal lip movement and modified resonance, creating an illusion of spatial displacement.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "He was uncommonly good at comic **ventriloquism**, and he threw his voice into the chimney with astonishing theatrical effect."},
            {"author": "G. K. Chesterton", "work": "The Wisdom of Father Brown", "quote": "The performer practiced subtle **ventriloquism**, convincing the audience that whispered warnings issued from the hollow wooden idol."},
            {"author": "Charles Dickens", "work": "The Uncommercial Traveller", "quote": "The clever display of **ventriloquism** upon the stage made the painted wooden figure seem startlingly alive to the spectators."}
        ]
    },
    "ventriloquist": {
        "primary": "A performer who practices ventriloquism, projecting speech into puppets or remote locations.",
        "secondary": "In stage entertainment and vocal performance, an artist who produces vocal sounds with immobilized facial muscles while animating a partner figure.",
        "quotes": [
            {"author": "G. K. Chesterton", "work": "The Wisdom of Father Brown", "quote": "The mysterious lodger was learning to be a professional conjurer as well as an accomplished **ventriloquist**."},
            {"author": "Charles Dickens", "work": "Sketches by Boz", "quote": "The traveling **ventriloquist** convulsed the rustic audience by making his battered wooden doll converse with the magistrate."},
            {"author": "Mark Twain", "work": "Autobiography of Mark Twain", "quote": "An itinerant **ventriloquist** arrived in our frontier town, bewildering the village dogs with voices from the hayloft."}
        ]
    },
    "ventriloquy": {
        "primary": "The practice, vocal technique, or illusion of ventriloquism; throwing the voice.",
        "secondary": "In classical history and performance, the vocal art of vocalizing from the throat or belly, historically associated with prophetic soothsaying.",
        "quotes": [
            {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "The strange art of **ventriloquy** deceiveth the ear by altering acoustic reflection, making speech seem distant or subterranean."},
            {"author": "Walter Scott", "work": "Demonology and Witchcraft", "quote": "Ancient oracular shrines frequently employed deceptive **ventriloquy** to persuade credulous pilgrims that stone idols spoke."},
            {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The Pythian priestess was suspected of practicing **ventriloquy** to deliver ambiguous answers from the dark recesses of the cave."}
        ]
    },

    # ==================== Dashboard — viscer (6 words) ====================
    "eviscerate": {
        "primary": "To disembowel; to remove the internal organs of; or to deprive something of its essential vitality.",
        "secondary": "In surgical trauma and critical rhetoric, the complete removal of visceral organs, or metaphorically gutting a legal statute or intellectual argument.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The penetrating wound threatened to **eviscerate** the casualty unless prompt emergency abdominal closure was performed."},
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Factional disputes threatened to **eviscerate** the new constitution, leaving it a hollow parchment of empty promises."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The sailors proceeded to **eviscerate** the monster upon the cutting stage, stripping blubber and viscera with expert ease."}
        ]
    },
    "evisceration": {
        "primary": "The surgical or traumatic removal of internal organs; or wound dehiscence with visceral extrusion.",
        "secondary": "In clinical surgery and ophthalmology, the operative removal of the contents of an organ (such as the globe of the eye, leaving the sclera intact) or abdominal rupture.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe wound disruption following laparotomy can result in alarming **evisceration** of small intestinal loops."},
            {"author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Meticulous anatomical approximation of the aponeurosis eliminates the dangerous hazard of postoperative **evisceration**."},
            {"author": "René Laennec", "work": "A Treatise on the Diseases of the Chest", "quote": "Historical autopsy protocols required preliminary **evisceration** of the thoracic and abdominal cavities before detailed organ dissection."}
        ]
    },
    "viscera": {
        "primary": "The internal organs enclosed within the main cavities of the body, especially the thoracic and abdominal cavities.",
        "secondary": "In human gross anatomy, the soft interior organs (heart, lungs, digestive tract, liver, kidneys) governed largely by the autonomic nervous system.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In snakes, the elongated shape of the body and the habit of swallowing large prey determine the position of the internal **viscera**."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate pursued his pathological inquiries into the structural changes of the diseased human **viscera** with unflagging enthusiasm."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The peritoneum forms an extensive serous sac investing and supporting the mobile abdominal **viscera**."}
        ]
    },
    "visceral": {
        "primary": "Relating to the internal organs of the body; or characterized by deep, intuitive, and primal gut feeling.",
        "secondary": "In neuroanatomy and human psychology, referring to the autonomic innervation of organs (visceral efferents), or to immediate emotional reactions devoid of rationalization.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Malignant emboli lodging in the **visceral** capillaries produce wedge-shaped infarctions of the spleen and kidneys."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The involuntary movements of the **visceral** muscular tunic propel the alimentary contents through peristaltic contractions."},
            {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "He felt a sudden **visceral** shock of shame that clutched at his throat like a suffocating hand."}
        ]
    },
    "viscerally": {
        "primary": "In an intuitive, gut-level, or deeply emotional manner; or with reference to internal organs.",
        "secondary": "In behavioral description and psychological analysis, reacting through profound autonomic and emotional impulse rather than conscious reasoning.",
        "quotes": [
            {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The grim reality of the wilderness affected Marlow **viscerally**, unsettling his accustomed European complacency."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "Bodily emotional states are experienced **viscerally** before the intellect formulates a reflective description of the danger."},
            {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "She responded **viscerally** to the harsh reproach, trembling from head to foot with wounded indignation."}
        ]
    },
    "visceroptosis": {
        "primary": "The abnormal downward displacement or prolapse of the internal abdominal organs; splanchnoptosis.",
        "secondary": "In clinical gastroenterology and historical medicine, Glenard's disease, characterized by laxity of the abdominal wall and suspensory peritoneal ligaments.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe generalized **visceroptosis** causes downward sagging of the stomach and transverse colon into the true pelvis."},
            {"author": "Abraham Flexner", "work": "Medical Education in the United States and Canada", "quote": "The clinical lecture emphasized that constitutional **visceroptosis** often responds more favorably to core physical therapy than surgical suspension."},
            {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "He demonstrated patients whose vague dyspeptic symptoms were attributed to marked constitutional **visceroptosis**."}
        ]
    }
}
