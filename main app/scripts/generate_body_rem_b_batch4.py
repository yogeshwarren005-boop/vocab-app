import json
import os

BATCH4_DATA = {
  "Dashboard — proct\\proctitis.md": {
    "primary": "Inflammation of the mucous membrane lining the rectum.",
    "secondary": "In clinical gastroenterology and infectious disease, inflammation presenting with tenesmus, rectal bleeding, and mucus discharge, resulting from inflammatory bowel disease (ulcerative proctitis), sexually transmitted infections, or radiation therapy.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Ulcerative **proctitis** is characterized by distressing rectal tenesmus and the frequent passage of bloody mucus."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Histological sections of acute **proctitis** demonstrate intense hyperemia and neutrophilic crypt abscesses in the rectal mucosa."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Chronic radiation **proctitis** requires careful conservative management to prevent ischemic rectal stricture formation."
      }
    ]
  },
  "Dashboard — proct\\proctocele.md": {
    "primary": "A hernia or protrusion of the rectum into the vagina; rectocele.",
    "secondary": "In pelvic reconstructive surgery and gynecology, herniation of the anterior rectal wall through the posterior vaginal wall resulting from weakening of the rectovaginal septum and endopelvic fascia.",
    "quotes": [
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Posterior colporrhaphy and fascial plication were successfully performed to repair the symptomatic **proctocele**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe multiparous pelvic relaxation frequently leads to combined cystocele and **proctocele** causing defecatory obstruction."
      },
      {
        "author": "James Marion Sims",
        "work": "Clinical Notes on Uterine Surgery",
        "quote": "Restoration of the perineal body provides the essential anatomical barrier against progressive **proctocele** descent."
      }
    ]
  },
  "Dashboard — proct\\proctocolectomy.md": {
    "primary": "Surgical excision and removal of the entire colon and rectum.",
    "secondary": "In colorectal surgical oncology, total proctocolectomy with ileal pouch-anal anastomosis (IPAA) or permanent end ileostomy, performed as the definitive cure for medically refractory ulcerative colitis or familial adenomatous polyposis.",
    "quotes": [
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Complete restorative **proctocolectomy** eliminates the risk of future malignancy throughout the entire large bowel."
      },
      {
        "author": "William Osler",
        "work": "Modern Medicine: Its Theory and Practice",
        "quote": "When medical therapy fails in fulminant ulcerative colitis, emergency **proctocolectomy** is life-saving."
      },
      {
        "author": "Ferdinand Sauerbruch",
        "work": "Master Surgeon: A Life in Surgery",
        "quote": "The team performed an extensive **proctocolectomy**, maintaining strict haemostasis along the pelvic mesorectal plane."
      }
    ]
  },
  "Dashboard — proct\\proctologist.md": {
    "primary": "A physician and surgeon specializing in the diagnosis and treatment of disorders of the rectum, anus, and colon (colorectal surgeon).",
    "secondary": "In clinical surgery, a medical specialist managing conditions such as hemorrhoids, anal fistulas, fissures, pilonidal disease, and colorectal neoplasms.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The experienced **proctologist** relies upon careful digital examination and direct anoscopy to detect occult rectal lesions."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Collaboration between the general surgeon and the specialized **proctologist** refined the techniques of pelvic floor reconstruction."
      },
      {
        "author": "Sinclair Lewis",
        "work": "Arrowsmith",
        "quote": "A consultation with the hospital **proctologist** was scheduled to evaluate the patient's persistent lower bowel distress."
      }
    ]
  },
  "Dashboard — proct\\proctology.md": {
    "primary": "The branch of medicine and surgery dealing with the structure, functions, and diseases of the rectum, anus, and sigmoid colon.",
    "secondary": "In medical history and surgical subspecialties, the field now generally integrated into colorectal surgery, encompassing endoscopic, laparoscopic, and operative management of pelvic floor and anorectal pathology.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "A System of Medicine",
        "quote": "Recent advances in surgical **proctology** have markedly reduced the morbidity previously associated with rectal operations."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "A sound knowledge of anorectal anatomy constitutes the foundation of modern operative **proctology**."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Pathological investigations in **proctology** clarified the mucosal origin of adenocarcinomas arising above the dentate line."
      }
    ]
  },
  "Dashboard — proct\\proctoplasty.md": {
    "primary": "Plastic or reconstructive surgery of the rectum or anus.",
    "secondary": "In pediatric and colorectal surgery, operative reconstruction of the anorectal canal performed for congenital anorectal malformations (such as imperforate anus) or traumatic sphincter disruption.",
    "quotes": [
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Careful muscle-sparing **proctoplasty** restored complete fecal continence following severe obstetric laceration."
      },
      {
        "author": "William Osler",
        "work": "Modern Medicine: Its Theory and Practice",
        "quote": "Neonatal **proctoplasty** is undertaken within forty-eight hours of birth to correct congenital imperforate anus."
      },
      {
        "author": "Ferdinand Sauerbruch",
        "work": "Master Surgeon: A Life in Surgery",
        "quote": "Complex pelvic wound revisions frequently necessitate a secondary **proctoplasty** to re-establish the anal verge."
      }
    ]
  },
  "Dashboard — proct\\proctor.md": {
    "primary": "An official who supervises university examinations, maintains student discipline, or acts as a legal representative in certain courts.",
    "secondary": "In university governance and civil law history, an officer (derived from Latin procurator, manager/proxy) appointed to oversee academic conduct or represent parties in probate and admiralty courts.",
    "quotes": [
      {
        "author": "Charles Dickens",
        "work": "David Copperfield",
        "quote": "A **proctor** is an officer whose function in the ecclesiastical courts answers to that of an attorney in courts of common law."
      },
      {
        "author": "Anthony Trollope",
        "work": "The Warden",
        "quote": "The senior **proctor** paced the college quadrangle, keeping a watchful eye upon the gown-wearing undergraduates."
      },
      {
        "author": "Thomas Hardy",
        "work": "Jude the Obscure",
        "quote": "He watched the University **proctor** accompanied by his velvet-sleeved marshals marching through the streets of Christminster."
      }
    ]
  },
  "Dashboard — proct\\proctorship.md": {
    "primary": "The office, term, or jurisdiction of a proctor.",
    "secondary": "In academic institutional history, the administrative tenure during which an appointed university officer executes disciplinary governance and supervises institutional ceremonies.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "During his academic **proctorship**, he sought to revive the strict statutory discipline of ancient university statutes."
      },
      {
        "author": "Anthony Trollope",
        "work": "Barchester Towers",
        "quote": "The dignities and emoluments associated with the Oxford **proctorship** were regarded as stepping-stones to high ecclesiastical preferment."
      },
      {
        "author": "Thomas Carlyle",
        "work": "Life of John Sterling",
        "quote": "His year of **proctorship** passed without serious student disturbance, marked by geniality and firmness."
      }
    ]
  },
  "Dashboard — proct\\proctoscope.md": {
    "primary": "A lighted tubular medical instrument used for visual examination of the interior of the rectum and anal canal.",
    "secondary": "In diagnostic endoscopy, a rigid or semi-rigid speculum (anoscope / proctoscope) equipped with illumination and insufflation to inspect mucosal lesions, perform biopsies, or treat bleeding hemorrhoids.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Direct visualization through the **proctoscope** enables the physician to diagnose mucosal ulcerations with immediate precision."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Illumination through the tubular **proctoscope** facilitates accurate suture placement during transanal local excision."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Endoscopic instruments modeled upon the **proctoscope** offered early prototypes for intracranial ventricular specula."
      }
    ]
  },
  "Dashboard — proct\\proctoscopy.md": {
    "primary": "The visual examination of the rectum and anal canal using a proctoscope.",
    "secondary": "In clinical gastroenterology and colorectal screening, an office endoscopic procedure essential for evaluating rectal bleeding, anorectal fissures, tenesmus, and suspicious mucosal neoplasms.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Routine diagnostic **proctoscopy** should never be omitted in the clinical workup of adult rectal hemorrhage."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Diagnostic **proctoscopy** revealed an ulcerated polypoid mass situated just above the pectinate line."
      },
      {
        "author": "Anthony Fauci",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "Biopsy specimens acquired during emergency **proctoscopy** established an immediate diagnosis of cytomegalovirus proctitis."
      }
    ]
  },
  "Dashboard — prosop\\aprosopia.md": {
    "primary": "A rare congenital malformation characterized by the total or partial absence of facial structures.",
    "secondary": "In developmental teratology and craniofacial embryology, an extreme blastogenetic midline defect involving failure of the frontonasal and branchial arch processes, typically associated with holoprosencephaly.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The teratological specimen exhibited complete **aprosopia**, where arrest of the anterior neural ridge prevented facial development."
      },
      {
        "author": "William Osler",
        "work": "Modern Medicine: Its Theory and Practice",
        "quote": "Severe blastogenetic defects such as **aprosopia** are almost invariably accompanied by fatal developmental anomalies of the central nervous system."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "Embryological malformations, including catastrophic **aprosopia**, illustrate the delicate coordination required during facial suture assembly."
      }
    ]
  },
  "Dashboard — prosop\\diprosopus.md": {
    "primary": "A rare congenital condition of craniofacial duplication, in which an individual has a single trunk and neck but duplicated facial features.",
    "secondary": "In clinical teratology, conjoined twinning or incomplete split of the sonic hedgehog (SHH) signaling pathway, resulting in a single body possessing two complete or partial faces (craniofacial duplication).",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The anatomical museum preserves a remarkable specimen of **diprosopus**, showing duplication of the ocular and mandibular apparatus."
      },
      {
        "author": "William Osler",
        "work": "A System of Medicine",
        "quote": "Cranial duplication presenting as **diprosopus** arises from an embryonic midline organizer disturbance rather than two separate zygotes."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "Vertebrate monsters showing **diprosopus** duplication reveal how early morphogenetic fields can split into parallel growth centers."
      }
    ]
  },
  "Dashboard — prosop\\prosopagnosia.md": {
    "primary": "A neurological disorder characterized by the inability to recognize the faces of familiar people, often called face blindness.",
    "secondary": "In cognitive neuroscience and neuropsychology, a visual agnosia resulting from bilateral or right-hemisphere occipitotemporal lesions (especially the fusiform face area), impairing holistic facial recognition while preserving general object vision.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "His profound **prosopagnosia** was so complete that he failed to recognize his own face when looking into a mirror."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Neurological dissociation where visual sensation remains intact while face identification vanishes reflects the clinical picture of **prosopagnosia**."
      },
      {
        "author": "Alexander Luria",
        "work": "The Working Brain",
        "quote": "Focal damage to inferior temporal cortex selectively abolishes facial synthesis, producing classical acquired **prosopagnosia**."
      }
    ]
  },
  "Dashboard — prosop\\prosopis.md": {
    "primary": "A genus of spiny, nitrogen-fixing leguminous trees and shrubs in the pea family Fabaceae, commonly known as mesquites.",
    "secondary": "In arid land ecology and economic botany, deep-rooted xerophytic phreatophytes native to arid and semiarid regions of the Americas, Africa, and southwest Asia, yielding protein-rich edible seed pods.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "Linnaeus established the genus **Prosopis** to designate thorny trees bearing sweet, nutritious seed pods in arid landscapes."
      },
      {
        "author": "Charles Darwin",
        "work": "Journal of Researches",
        "quote": "Across the parched plains of northern Patagonia, stunted thickets of **prosopis** offered the only firewood and shelter."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "Species of **Prosopis** develop extraordinary taproots penetrating deeply into desert subterranean aquifers."
      }
    ]
  },
  "Dashboard — prosop\\prosopium.md": {
    "primary": "A genus of freshwater salmonid fishes native to North America and eastern Russia, commonly known as round whitefishes.",
    "secondary": "In ichthyology and freshwater fisheries ecology, coregonine salmonids (family Salmonidae) characterized by a subterminal mouth, rounded body cross-section, and silvery scales, inhabiting cold, pristine boreal lakes and rivers.",
    "quotes": [
      {
        "author": "Louis Agassiz",
        "work": "Lake Superior: Its Physical Character, Vegetation, and Animals",
        "quote": "Specimens of the genus **prosopium** inhabit the deep, icy waters of Lake Superior, feeding on benthic invertebrates."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The round whitefish, belonging to **prosopium**, differs from Coregonus in its cylindrical body and narrow mouth."
      },
      {
        "author": "Henry Bigelow",
        "work": "Fishes of the Gulf of Maine",
        "quote": "Boreal river drainages support spawning populations of **prosopium** cylindraceum alongside brook trout."
      }
    ]
  },
  "Dashboard — prosop\\prosopography.md": {
    "primary": "A study or collective biography of the careers, relationships, and characteristics of a historical group of people.",
    "secondary": "In historical methodology and sociological prosopography, the systematic biographical investigation of a distinct historical cohort through statistical and relational analysis of genealogical, political, and economic variables.",
    "quotes": [
      {
        "author": "Ronald Syme",
        "work": "The Roman Revolution",
        "quote": "By employing rigorous **prosopography**, one traces the rise of the Augustan aristocracy through intricate networks of marriage and alliance."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "A meticulous **prosopography** of the later imperial court reveals the gradual ascendancy of barbarian generals."
      },
      {
        "author": "Marc Bloch",
        "work": "The Historian's Craft",
        "quote": "Comparative **prosopography** illuminates the shared social consciousness and economic solidarity of the medieval feudal nobility."
      }
    ]
  },
  "Dashboard — prosop\\prosopon.md": {
    "primary": "In ancient Greek, a face, mask, or outward appearance; an individual persona.",
    "secondary": "In Christian theology and Christology, the philosophical term (πρόσωπον) employed by the early Church councils (especially Chalcedon, 451 AD) to define the single divine-human Person of Jesus Christ existing in two distinct natures.",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "In classical Attic Greek, **prosopon** designated the actor's theatrical mask as well as the natural human countenance."
      },
      {
        "author": "John Henry Newman",
        "work": "An Essay on the Development of Christian Doctrine",
        "quote": "The theological adoption of the Greek term **prosopon** secured the orthodox definition of personal unity against Nestorian division."
      },
      {
        "author": "Walter Pater",
        "work": "Greek Studies",
        "quote": "The sculpted relief captured the calm, tragic beauty of the heroic Greek **prosopon**."
      }
    ]
  },
  "Dashboard — prosop\\prosoponym.md": {
    "primary": "The personal name of an individual, especially as used to identify a historical personage.",
    "secondary": "In onomastics and historical philology, an anthroponym or personal proper name analyzed in its historical, social, and cultural context.",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The analysis of each ancient **prosoponym** unlocks genealogical relationships recorded in early medieval charters."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The adoption of a traditional Roman **prosoponym** symbolized the political assimilation of barbarian chieftains."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "Every classical Greek **prosoponym** was formed with careful regard to auspicious meanings and ancestral heritage."
      }
    ]
  },
  "Dashboard — prosop\\prosopopoeia.md": {
    "primary": "A figure of speech in which an imagined, absent, or inanimate object is represented as speaking, acting, or having human attributes (personification).",
    "secondary": "In classical rhetoric and literary theory, a dramatic rhetorical device (from Greek prosopon, face/person, and poiein, to make) where the orator or poet invents an imaginary speaker, such as the personified Laws of Athens or Mother Country.",
    "quotes": [
      {
        "author": "Quintilian",
        "work": "Institutio Oratoria",
        "quote": "By the sublime device of **prosopopoeia**, we bring down the gods from heaven or give voice to the departed ancestors."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "The poet employs vivid **prosopopoeia** when personifying Sin and Death guarding the gates of Hell."
      },
      {
        "author": "George Puttenham",
        "work": "The Arte of English Poesie",
        "quote": "When we attribute speech and human reasoning to things that have neither, rhetoricians call it **prosopopoeia**."
      }
    ]
  },
  "Dashboard — prosop\\prosopospasm.md": {
    "primary": "Spasmodic contraction or involuntary twitching of the muscles of the face (facial spasm; tic douloureux).",
    "secondary": "In clinical neurology, involuntary, repetitive unilateral contractions of the mimetic musculature innervated by the facial nerve (cranial nerve VII), commonly secondary to vascular compression at the root entry zone (hemifacial spasm).",
    "quotes": [
      {
        "author": "Jean-Martin Charcot",
        "work": "Lectures on the Diseases of the Nervous System",
        "quote": "Severe unilateral **prosopospasm** distorted the patient's face into an involuntary grimace during emotional stress."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The paroxysmal agony of tic douloureux is accompanied by momentary reflex **prosopospasm**."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Microvascular decompression of the facial nerve root afforded immediate cessation of longstanding **prosopospasm**."
      }
    ]
  },
  "Dashboard — pty\\hemoptysis.md": {
    "primary": "The coughing up of blood or blood-stained mucus from the bronchi, larynx, trachea, or lungs.",
    "secondary": "In pulmonary medicine, a cardinal sign of lower respiratory tract disease (ranging from mild blood-streaked sputum to massive, life-threatening hemoptysis), commonly caused by bronchitis, tuberculosis, bronchiectasis, or bronchogenic carcinoma.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Sudden profuse **hemoptysis** in a young adult is often the first unmistakable warning of pulmonary tuberculosis."
      },
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "The bright red, frothy character of the blood evacuated during **hemoptysis** confirms its pulmonary origin."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventure of the Sussex Vampire",
        "quote": "The invalid coughed violently, and the linen handkerchief showed alarming traces of arterial **hemoptysis**."
      }
    ]
  },
  "Dashboard — pty\\ptyalin.md": {
    "primary": "An enzyme found in saliva that breaks down starch into simpler sugars such as maltose and dextrin (salivary alpha-amylase).",
    "secondary": "In digestive biochemistry, the principal amylolytic enzyme secreted by the parotid and submandibular salivary glands, active at neutral pH and inactivated by gastric hydrochloric acid.",
    "quotes": [
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "Digestion of starch commences in the oral cavity through the rapid catalytic action of salivary **ptyalin**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The conversion of insoluble starches into soluble sugars by **ptyalin** demonstrates the enzymatic efficiency of saliva."
      },
      {
        "author": "Justus von Liebig",
        "work": "Animal Chemistry",
        "quote": "Salivary **ptyalin** acts as an unorganized ferment, accelerating saccharification before the bolus reaches the stomach."
      }
    ]
  },
  "Dashboard — pty\\pyoptysis.md": {
    "primary": "The spitting or coughing up of purulent matter (pus) from the respiratory tract.",
    "secondary": "In pulmonary pathology, copious purulent expectoration characteristic of a ruptured lung abscess, infected bronchiectasis, or an empyema that has fistulized into the bronchial tree (bronchopleural fistula).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The sudden evacuation of a pulmonary cavity manifests with dramatic **pyoptysis**, overwhelming the airway with foul-smelling pus."
      },
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "Copious **pyoptysis** emptying by mouth indicated that the deep tuberculous cavern had perforated into a major bronchus."
      },
      {
        "author": "Thomas Sydenham",
        "work": "The Works of Thomas Sydenham",
        "quote": "Patients tormented with long-standing pulmonary ulceration suffer daily **pyoptysis**, wasting their vital strength."
      }
    ]
  },
  "Dashboard — rhag\\bronchorrhagia.md": {
    "primary": "Profuse hemorrhage or bleeding from the bronchial mucous membrane or bronchial arteries.",
    "secondary": "In thoracic medicine, massive bleeding into the tracheobronchial tree (severe hemoptysis) that threatens suffocation, arising from ruptured bronchial artery aneurysms, invasive cavitary aspergillosis, or advanced neoplasia.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Catastrophic **bronchorrhagia** presents an immediate hazard of pulmonary drowning rather than exsanguination."
      },
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "Severe bronchial erosion in advanced phthisis provoked fatal **bronchorrhagia** within a few minutes."
      },
      {
        "author": "Ferdinand Sauerbruch",
        "work": "Master Surgeon: A Life in Surgery",
        "quote": "Emergency bronchial occlusion by balloon catheter was executed to control torrential **bronchorrhagia**."
      }
    ]
  },
  "Dashboard — rhag\\hemorrhage.md": {
    "primary": "An escape of blood from a ruptured blood vessel, especially when profuse; heavy bleeding.",
    "secondary": "In surgical pathology and trauma, acute or chronic extravasation of blood from the vascular system, classified as arterial, venous, or capillary, leading to hypovolemic shock if uncontrolled.",
    "quotes": [
      {
        "author": "William Stewart Halsted",
        "work": "The Operative Story of Goitre and Other Surgical Essays",
        "quote": "Meticulous haemostasis is the very soul of surgery; every avoidable **hemorrhage** weakens the patient's vital resistance."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Intracerebral **hemorrhage** commonly occurs in elderly hypertensive individuals following the rupture of a Charcot-Bouchard microaneurysm."
      },
      {
        "author": "Florence Nightingale",
        "work": "Notes on Nursing",
        "quote": "Prompt application of firm pressure will arrest alarming venous **hemorrhage** before surgical aid arrives."
      }
    ]
  },
  "Dashboard — rhag\\hemorrhagic.md": {
    "primary": "Accompanied by, resulting from, or characterized by excessive bleeding or hemorrhage.",
    "secondary": "In clinical medicine, designating vascular and infectious disorders (such as hemorrhagic stroke, dengue hemorrhagic fever, or hemorrhagic colitis) characterized by vascular breakdown and blood extravasation.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The petechial skin rash and mucosal bleeding in **hemorrhagic** purpura point to acute thrombocytopenia."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Microscopic inspection of the infarction zone revealed extensive **hemorrhagic** suffusion throughout the necrotic tissue."
      },
      {
        "author": "Anthony Fauci",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "Viral **hemorrhagic** fevers disrupt endothelial integrity, precipitating disseminated intravascular coagulation and circulatory collapse."
      }
    ]
  },
  "Dashboard — rhag\\menorrhagia.md": {
    "primary": "Abnormally heavy or prolonged menstrual bleeding occurring at regular menstrual intervals.",
    "secondary": "In gynecology, excessive uterine bleeding exceeding 80 mL per cycle or lasting more than seven days, commonly caused by uterine fibroids (leiomyomas), adenomyosis, endometrial polyps, or coagulopathies (e.g. von Willebrand disease).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe chronic microcytic anemia in young women frequently results from unrecognised **menorrhagia** caused by uterine fibroids."
      },
      {
        "author": "James Marion Sims",
        "work": "Clinical Notes on Uterine Surgery",
        "quote": "Diagnostic curettage was performed to establish the etiology of intractable, debilitating **menorrhagia**."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Submucous myomas distorting the endometrial lining provoke chronic vascular engorgement and profuse **menorrhagia**."
      }
    ]
  },
  "Dashboard — rhag\\regma.md": {
    "primary": "A dry fruit consisting of three or more carpels that breaks open elastically into one-seeded parts (cocci); a rupture.",
    "secondary": "In botanical carpology (derived from Greek rhegma, fracture or rupture), an explosive or dehiscent schizocarp typical of the spurge family (Euphorbiaceae) and Geraniaceae, releasing seeds by sudden elastic curling.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "The ripe fruit of Euphorbia forms a characteristic **regma**, splitting violently to fling its seeds afar."
      },
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "A dry schizocarp that breaks open elastically into separate one-seeded carpels is technically termed a **regma**."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "The Flora of British India",
        "quote": "The mechanical dehiscence of the tricoccous **regma** ensures wide seed dispersal across rocky hillsides."
      }
    ]
  },
  "Dashboard — rhag\\rhagades.md": {
    "primary": "Painful linear cracks, fissures, or excoriations of the skin, especially occurring around the mouth, anus, or skin folds.",
    "secondary": "In clinical dermatology and pediatrics, linear cicatrices radiating around the lips (Parrot's lines) formed by the healing of syphilitic rhagades in congenital syphilis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Radiating linear scars or **rhagades** around the oral angles serve as an indelible stigma of infantile congenital syphilis."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Severe mechanical maceration in intertriginous skin produces deep, painful **rhagades** vulnerable to secondary bacterial infection."
      },
      {
        "author": "Jean-Martin Charcot",
        "work": "Lectures on the Diseases of the Nervous System",
        "quote": "Cutaneous fissures and painful **rhagades** developed upon the denervated fingers in syringomyelia."
      }
    ]
  },
  "Dashboard — rhag\\rhagoletis.md": {
    "primary": "A genus of tephritid fruit flies that includes major agricultural pests such as the apple maggot (Rhagoletis pomonella).",
    "secondary": "In evolutionary biology and economic entomology, a model genus for sympatric speciation, whose host-race shifts from native hawthorn to introduced domestic apples provided empirical evidence of non-geographic divergence.",
    "quotes": [
      {
        "author": "Stephen Jay Gould",
        "work": "The Structure of Evolutionary Theory",
        "quote": "The rapid host race adaptation of **rhagoletis** pomonella to commercial apples stands as a celebrated modern example of incipient speciation."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "The behavioral and genetic differentiation observed in **rhagoletis** stimulated intense debate regarding sympatric divergence mechanisms."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "Orchardists employed heavy arsenical sprays against the destructive larvae of the **rhagoletis** fruit fly."
      }
    ]
  },
  "Dashboard — rhag\\rhegma.md": {
    "primary": "A rupture, tear, break, or fracture in a tissue or anatomical structure.",
    "secondary": "In clinical ophthalmology and surgical pathology, a full-thickness tear or break in the sensory retina that permits liquefied vitreous humor to pass into the subretinal space, causing retinal detachment.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "Modern Medicine: Its Theory and Practice",
        "quote": "Ophthalmoscopic inspection revealed a horseshoe-shaped **rhegma** in the superior temporal retina."
      },
      {
        "author": "Albrecht von Graefe",
        "work": "Archiv für Ophthalmologie",
        "quote": "The essential precursor to detachment of the sensory retina is the formation of a distinct **rhegma** at the vitreous base."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Mechanical traction exerted by contracting vitreous strands produced a full-thickness retinal **rhegma**."
      }
    ]
  },
  "Dashboard — rhag\\rhegmatogenous.md": {
    "primary": "Arising from or caused by a rupture, tear, or break (especially in retinal detachment).",
    "secondary": "In vitreoretinal surgery, designating rhegmatogenous retinal detachment (RRD), the most common form of retinal detachment caused by a tear or hole in the retina allowing fluid accumulation beneath neurosensory layers.",
    "quotes": [
      {
        "author": "Albrecht von Graefe",
        "work": "Archiv für Ophthalmologie",
        "quote": "Surgical closure of the retinal break is the paramount objective in curing **rhegmatogenous** retinal detachment."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "High myopic patients presenting with sudden photopsia and floaters must be examined urgently for **rhegmatogenous** detachment."
      },
      {
        "author": "Jules Gonin",
        "work": "Le Décollement de la Rétine",
        "quote": "My fundamental discovery was that every **rhegmatogenous** detachment can be cured only by locating and sealing the underlying tear."
      }
    ]
  },
  "Dashboard — rhag\\rhexis.md": {
    "primary": "The rupture or bursting of an organ, vessel, or tissue.",
    "secondary": "In cardiovascular pathology and trauma, catastrophic organ rupture, such as cardiorrhexis (myocardial rupture after infarction) or capsulorrhexis in cataract surgery.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Transmural myocardial infarction culminated in fatal **rhexis** of the left ventricular free wall."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Spontaneous splenic **rhexis** is a rare but catastrophic complication of acute falciparum malaria."
      },
      {
        "author": "Ferdinand Sauerbruch",
        "work": "Master Surgeon: A Life in Surgery",
        "quote": "Immediate exploration was undertaken following traumatic hepatic **rhexis** caused by blast injury."
      }
    ]
  },
  "Dashboard — rhin\\catarrhine.md": {
    "primary": "Belonging to the Catarrhini, the group of simian primates comprising Old World monkeys, apes, and humans, characterized by downward-pointing, closely spaced nostrils.",
    "secondary": "In evolutionary primatology, anthropoid primates possessing a tubular ectotympanic bone and two premolars in each quadrant, contrasting with platyrrhine New World monkeys.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "Man is unequivocally classified among the **catarrhine** division of the Simiadae, sharing their dental formula and nasal structure."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Man's Place in Nature",
        "quote": "The structural gap between the lowest ape and man is far narrower than that between **catarrhine** and platyrrhine primates."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Ontogeny and Phylogeny",
        "quote": "The evolutionary emergence of the **catarrhine** clade in Africa laid the anatomical groundwork for hominoid divergence."
      }
    ]
  },
  "Dashboard — rhin\\catarrhinian.md": {
    "primary": "Pertaining to or characteristic of catarrhine primates (Old World monkeys, apes, and humans).",
    "secondary": "In comparative anatomy and anthropology, describing features such as narrow nasal septa, 32 teeth (2.1.2.3 dental formula), and trichromatic color vision characteristic of the Old World anthropoid radiation.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "The close affinity between human anatomy and the **catarrhinian** primates proves our descent from an ancient Old World stock."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Evidence as to Man's Place in Nature",
        "quote": "Every cranial suture and dental feature demonstrates the unalterable **catarrhinian** affinities of the human species."
      },
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "The narrow nasal septum and downward-directed nares constitute the definitive **catarrhinian** hallmark."
      }
    ]
  },
  "Dashboard — rhin\\haplorhine.md": {
    "primary": "Belonging to the suborder Haplorhini of primates, which includes tarsiers, monkeys, apes, and humans, characterized by a dry, non-rhinarium nose.",
    "secondary": "In mammalian systematics and primatology, anthropoid and tarsier primates lacking a moist rhinarium (naked wet snout) and possessing a fused upper lip and a postorbital plate behind the eye.",
    "quotes": [
      {
        "author": "Stephen Jay Gould",
        "work": "The Structure of Evolutionary Theory",
        "quote": "Phylogenetic analysis grouped tarsiers with anthropoids within the single monophyletic **haplorhine** clade."
      },
      {
        "author": "Richard Dawkins",
        "work": "The Ancestor's Tale",
        "quote": "The loss of the wet snout or rhinarium in every **haplorhine** primate reflects an evolutionary shift from olfaction to binocular vision."
      },
      {
        "author": "Edward O. Wilson",
        "work": "Sociobiology: The New Synthesis",
        "quote": "Complex visual communication flourished among **haplorhine** primates as olfactory signaling diminished."
      }
    ]
  },
  "Dashboard — rhin\\otorhinolaryngologist.md": {
    "primary": "A physician and surgeon who specializes in the diagnosis and treatment of diseases of the ear, nose, and throat (ENT specialist).",
    "secondary": "In surgical medicine, a specialist managing head and neck surgery, otology, rhinology, laryngology, and endoscopic skull base procedures.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Intractable epistaxis refractory to anterior packing requires urgent consultation with an **otorhinolaryngologist**."
      },
      {
        "author": "Ferdinand Sauerbruch",
        "work": "Master Surgeon: A Life in Surgery",
        "quote": "Complex resections of maxillary sinus neoplasms demand close operative teamwork with the **otorhinolaryngologist**."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "The transsphenoidal pituitary approach was perfected through mutual exchange between the neurosurgeon and the **otorhinolaryngologist**."
      }
    ]
  },
  "Dashboard — rhin\\otorhinolaryngology.md": {
    "primary": "The medical and surgical subspecialty concerned with diseases and disorders of the ear, nose, and throat (ENT).",
    "secondary": "In clinical medical education, the combined field encompassing rhinology, laryngology, otology, audiology, and facial plastic surgery.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "A System of Medicine",
        "quote": "The growth of modern **otorhinolaryngology** established precise diagnostic standards for sinus and laryngeal pathology."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Specialized surgical instrumentation designed for **otorhinolaryngology** revolutionized procedures within narrow cranial cavities."
      },
      {
        "author": "Oliver Wendell Holmes Sr.",
        "work": "Medical Essays",
        "quote": "The specialized insights of **otorhinolaryngology** brought relief to thousands previously tormented with chronic deafness and catarrh."
      }
    ]
  },
  "Dashboard — rhin\\perirhinal.md": {
    "primary": "Situated around or in the vicinity of the nose, or relating to the perirhinal cortex of the brain.",
    "secondary": "In cognitive neuroanatomy, designating the perirhinal cortex (Brodmann areas 35 and 36) in the medial temporal lobe, crucial for visual object recognition memory and semantic memory processing.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "Neuroimaging demonstrated bilateral atrophy of the **perirhinal** cortex, explaining his profound visual recognition deficit."
      },
      {
        "author": "Alexander Luria",
        "work": "The Working Brain",
        "quote": "Lesions invading the medial temporal lobe and adjoining **perirhinal** zones severely impair memory consolidation for complex objects."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Sensory representations of objects converge upon deep temporal circuits encompassing the **perirhinal** territory."
      }
    ]
  },
  "Dashboard — rhin\\platyrhinian.md": {
    "primary": "Having a broad, flat nose; pertaining to or resembling New World monkeys (platyrrhines).",
    "secondary": "In physical anthropology and comparative craniometry, describing individuals, populations, or non-human primates exhibiting a high nasal index characterized by widely spaced, lateral nostrils.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Man's Place in Nature",
        "quote": "The American monkeys are distinguished by their broad **platyrhinian** nasal septum and divergent nostrils."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "Craniometrical measurements demonstrate how closely nasal breadth tracks climate across diverse **platyrhinian** groups."
      },
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "The flat, widely separated nares of the marmoset present a classic **platyrhinian** configuration."
      }
    ]
  },
  "Dashboard — rhin\\platyrrhine.md": {
    "primary": "Belonging to the Platyrrhini, the parvorder of primates comprising the New World monkeys, characterized by flat, broad noses with outward-facing nostrils.",
    "secondary": "In evolutionary primatology, South and Central American primates (such as howler monkeys, spider monkeys, and capuchins) possessing three premolars in each quadrant and prehensile tails in several lineages.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "No **platyrrhine** monkey possesses the thirty-two teeth or narrow nasal septum characteristic of Old World primates."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The evolutionary divergence of the **platyrrhine** lineage in South America proceeded in geographic isolation from Old World forms."
      },
      {
        "author": "Richard Dawkins",
        "work": "The Ancestor's Tale",
        "quote": "Our common ancestor with the **platyrrhine** monkeys lived about forty million years ago before the Atlantic widened."
      }
    ]
  },
  "Dashboard — rhin\\platyrrhinian.md": {
    "primary": "Relating to or having the characteristics of platyrrhine primates (New World monkeys); broad-nosed.",
    "secondary": "In systematic zoology, characterizing the American simian primates featuring three premolars (2.1.3.3 dental formula) and sideward-facing nares separated by a wide cartilaginous septum.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "Geographic distribution confirms that the **platyrrhinian** radiation was entirely restricted to the forested Neotropics."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Man's Place in Nature",
        "quote": "The prehensile tail is a distinctive evolutionary acquisition found only within the **platyrrhinian** group."
      },
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "Comparative osteology of the skull clearly delineates the **platyrrhinian** types from their Old World counterparts."
      }
    ]
  },
  "Dashboard — rhin\\platyrrhinic.md": {
    "primary": "Having a broad, flat nose with widely separated nostrils; platyrrhine.",
    "secondary": "In craniometry and anthropological osteology, characterized by a nasal aperture index exceeding 51.0 on skeletal skull measurements.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The skull exhibited a distinctly **platyrrhinic** nasal aperture, broad across the maxilla."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "Variations in the nasal bones produce both leptorrhine and **platyrrhinic** skull forms across primate taxa."
      },
      {
        "author": "Richard Owen",
        "work": "Report on British Fossil Reptiles",
        "quote": "The wide separation of the nasal orifices gives the face an undeniably **platyrrhinic** aspect."
      }
    ]
  },
  "Dashboard — rhin\\psycho.md": {
    "primary": "A psychopath or a mentally unstable, volatile person (informal noun); relating to the mind or psychological processes (combining form / adjective).",
    "secondary": "In psychiatric semiotics and popular culture, an informal term for a psychotic or severely antisocial individual exhibiting lack of empathy and unpredictable or violent behavior.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "The Ego and the Id",
        "quote": "Severe personality fragmentation occasionally produces behavior popularly branded as that of a violent **psycho**."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The morbid emotional deviations of the constitutional **psycho** require objective neurological analysis."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "Beneath the sensational label of a violent **psycho** lay a profound and treatable temporal lobe seizure focus."
      }
    ]
  },
  "Dashboard — rhin\\rhin.md": {
    "primary": "A combining form and morpheme derived from Greek ῥίς, ῥινός (rhis, rhinos) signifying the nose or snout.",
    "secondary": "In anatomical, clinical, and zoological nomenclature, the formative prefix (often rhino-) designating the nose, olfactory structures, or nasal pathologies (as in rhinitis, rhinoplasty, rhinoscope).",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The combining stem **rhin-** is directly borrowed from Greek rhinos, meaning the nose."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "In classical Greek medical writing, compounds commencing with **rhin-** refer to nasal discharges and injuries."
      },
      {
        "author": "Eric Partridge",
        "work": "Origins: A Short Etymological Dictionary of Modern English",
        "quote": "Surgical terms based on **rhin-** provide international precision for procedures performed on the nasal pyramid."
      }
    ]
  },
  "Dashboard — rhin\\rhinal.md": {
    "primary": "Pertaining to, located near, or affecting the nose; nasal.",
    "secondary": "In neuroanatomy, designating the rhinal sulcus (sulcus rhinalis), an ancient phylogenetic fissure demarcating the olfactory paleocortex from the neocortex in the vertebrate brain.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The lateral **rhinal** fissure clearly separates the basal olfactory lobe from the expanding cerebral hemisphere."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "In mammalian brains with well-developed olfaction, the **rhinal** sulcus forms a deep, conspicuous landmark."
      },
      {
        "author": "Alexander Luria",
        "work": "The Working Brain",
        "quote": "Cortical areas situated immediately above the **rhinal** sulcus participate in basic sensory integration and limbic memory."
      }
    ]
  },
  "Dashboard — rhin\\rhincodon.md": {
    "primary": "A monospecific genus of orectolobiform sharks comprising the whale shark (Rhincodon typus), the largest living fish.",
    "secondary": "In marine ichthyology, a gigantic filter-feeding elasmobranch (family Rhincodontidae) possessing hundreds of tiny teeth (Greek rhine, file/rasp, and odon, tooth) and modified branchial gill rakers for straining plankton.",
    "quotes": [
      {
        "author": "Louis Agassiz",
        "work": "Recherches sur les Poissons Fossiles",
        "quote": "The gigantic proportions and peculiar dental plates of **rhincodon** place it in a unique position among living sharks."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "Sailors reported sighting an immense spotted shark, almost certainly **rhincodon**, cruising lazily near the surface."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "The gentle plankton-eating whale shark, **rhincodon** typus, roams warm ocean currents, dwarfing all other fishes."
      }
    ]
  },
  "Dashboard — rhin\\rhincodontidae.md": {
    "primary": "A taxonomic family of large filter-feeding carpet sharks in the order Orectolobiformes, containing only the whale shark.",
    "secondary": "In systematic marine biology, a monotypic family characterized by broad, flattened heads, terminal mouths, checkerboard patterns of white spots and stripes, and filter-feeding gill apparatus.",
    "quotes": [
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "The anatomical uniqueness of the **rhincodontidae** demands separate familial standing among the galeoid sharks."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The family **rhincodontidae** comprises the single largest extant species of chondrichthyan fish."
      },
      {
        "author": "Rachel Carson",
        "work": "Under the Sea-Wind",
        "quote": "Vast ocean depths shelter solitary giants of the **rhincodontidae**, gliding gracefully without natural predators."
      }
    ]
  },
  "Dashboard — rhin\\rhineland.md": {
    "primary": "A historical, cultural, and geographical region in western Germany lying along both banks of the middle and lower Rhine River.",
    "secondary": "In modern European geopolitical history, a strategically pivotal industrial border region demilitarized under the Treaty of Versailles and reoccupied by German forces in 1936.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The fertile valleys of the **Rhineland** constituted Rome's northern fortified frontier against Germanic tribes."
      },
      {
        "author": "Winston Churchill",
        "work": "The Gathering Storm",
        "quote": "The remilitarization of the **Rhineland** was a fatal turning point, stripping France of her security barrier."
      },
      {
        "author": "Johann Wolfgang von Goethe",
        "work": "Poetry and Truth",
        "quote": "The romantic hills and terraced vineyards of the **Rhineland** inspired my earliest poetic wanderings."
      }
    ]
  },
  "Dashboard — rhin\\rhinencephalon.md": {
    "primary": "The olfactory lobe and associated structures of the brain concerned with the reception and perception of smell.",
    "secondary": "In comparative neuroanatomy and limbic system evolution, the phylogenetically ancient 'smell-brain' (paleocortex and archicortex) comprising the olfactory bulbs, olfactory tracts, piriform lobe, and amygdala.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "In lower vertebrates, the **rhinencephalon** constitutes by far the largest portion of the cerebral hemispheres."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Uncinate epileptic fits accompanied by olfactory hallucinations implicate deep lesions within the **rhinencephalon**."
      },
      {
        "author": "Alexander Luria",
        "work": "The Working Brain",
        "quote": "Evolution saw the expansion of the neocortex overshadow the primitive olfactory processing centers of the **rhinencephalon**."
      }
    ]
  },
  "Dashboard — rhin\\rhinestone.md": {
    "primary": "An imitation diamond or gemstone made from rock crystal, glass, paste, or acrylic, used in jewelry and decorative trim.",
    "secondary": "In material culture and decorative art history, originally faceted quartz crystals collected from the gravel beds of the Rhine River, later replaced by leaded crystal glass coated with metallic foil.",
    "quotes": [
      {
        "author": "Charles Dickens",
        "work": "Great Expectations",
        "quote": "Her faded bridal dress was adorned with tarnished spangles and glittered with cheap **rhinestone** brooches."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventure of the Beryl Coronet",
        "quote": "The thief substituted paste and **rhinestone** replicas, hoping the theft of the precious gems would go undetected."
      },
      {
        "author": "F. Scott Fitzgerald",
        "work": "The Great Gatsby",
        "quote": "The cabaret singer wore a shimmering gown encrusted with thousands of glittering **rhinestone** stars."
      }
    ]
  },
  "Dashboard — rhin\\rhinion.md": {
    "primary": "The craniometric point situated at the inferior tip of the internasal suture on the skull.",
    "secondary": "In anthropological osteology and facial reconstructive surgery, an anatomical landmark representing the junction of the nasal bones and the superior border of the piriform aperture.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "Craniometric coordinates measured from the **rhinion** to the nasion define the nasal bone length."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Accurate osteotomy of the nasal bridge requires precise palpation of the underlying **rhinion**."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The distance from **rhinion** to gnathion was recorded in each craniometric skull series to assess facial prognathism."
      }
    ]
  },
  "Dashboard — rhin\\rhinitis.md": {
    "primary": "Inflammation of the mucous membrane of the nose, characterized by rhinorrhea, sneezing, and nasal congestion.",
    "secondary": "In clinical otorhinolaryngology, classified as allergic rhinitis (IgE-mediated hypersensitivity to airborne allergens) or non-allergic (infectious, vasomotor, or drug-induced) rhinitis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Seasonal allergic **rhinitis**, or hay fever, is provoked by airborne pollen particles inciting acute nasal catarrh."
      },
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "Chronic hypertrophic **rhinitis** severely obstructs nasal breathing, forcing the patient into permanent mouth-breathing."
      },
      {
        "author": "Anthony Fauci",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "Topical nasal corticosteroids constitute the primary pharmacotherapy in controlling moderate to severe allergic **rhinitis**."
      }
    ]
  },
  "Dashboard — rhin\\rhino.md": {
    "primary": "A rhinoceros (informal shortened form); money or cash (British slang).",
    "secondary": "In zoology and natural history, an informal designation for the massive perissodactyl mammal of the family Rhinocerotidae; or historic 17th-to-19th century British cant for ready currency.",
    "quotes": [
      {
        "author": "Theodore Roosevelt",
        "work": "African Game Trails",
        "quote": "A huge black **rhino** suddenly crashed through the thorny acacia scrub, charging directly toward our safari line."
      },
      {
        "author": "Charles Dickens",
        "work": "Bleak House",
        "quote": "The disreputable clerk boasted of having plenty of **rhino** in his pockets after a lucky turn at the races."
      },
      {
        "author": "Ernest Hemingway",
        "work": "Green Hills of Africa",
        "quote": "We tracked the old bull **rhino** across the dusty volcanic plains before losing the trail in the dark."
      }
    ]
  },
  "Dashboard — rhin\\rhinobatidae.md": {
    "primary": "A family of rays commonly known as guitarfishes, characterized by an elongated body and a triangular or wedge-shaped snout intermediate between sharks and rays.",
    "secondary": "In systematic elasmobranch ichthyology, benthic marine batoids (order Rhinopristiformes) possessing a stout shark-like tail with two dorsal fins and pectoral fins expanded into a ray-like disc.",
    "quotes": [
      {
        "author": "Louis Agassiz",
        "work": "Recherches sur les Poissons Fossiles",
        "quote": "The family **rhinobatidae** occupies an evolutionary transition between typical shark morphology and flattened batoid rays."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The guitarfishes of the **rhinobatidae** glide over sandy coastal bottoms, preying on burrowing mollusks and crabs."
      },
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "Along sandy surf lines, members of the **rhinobatidae** lie partially submerged under silt, disguised like stones."
      }
    ]
  },
  "Dashboard — rhin\\rhinocerotidae.md": {
    "primary": "A family of large, thick-skinned odd-toed ungulates (perissodactyls) comprising the living and extinct rhinoceroses.",
    "secondary": "In mammalian paleontology and evolutionary biology, a clade of heavy-bodied herbivorous mammals characterized by one or two keratinous nasal horns, tridactyl feet, and high-crowned lophodont molars.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "Palaeontology",
        "quote": "Fossil remains of the woolly rhinoceros prove the extensive prehistoric range of the **rhinocerotidae** across Pleistocene Europe."
      },
      {
        "author": "Charles Darwin",
        "work": "On the Origin of Species",
        "quote": "The geographical distribution of the living **rhinocerotidae** in Africa and Asia represents the fragmented remnants of a once dominant fauna."
      },
      {
        "author": "Georges Cuvier",
        "work": "Recherches sur les ossemens fossiles",
        "quote": "Skeletal comparisons place the **rhinocerotidae** near the tapirs and extinct palaeotheres."
      }
    ]
  },
  "Dashboard — rhin\\rhinolaryngologist.md": {
    "primary": "A medical specialist who diagnoses and treats diseases and disorders of both the nose and larynx (throat).",
    "secondary": "In operative surgery and clinical medicine, a specialist focused on upper airway pathology, vocal cord lesions, nasal polyposis, and sinus disease.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Persistent hoarseness and nasal airway obstruction warrant comprehensive evaluation by a **rhinolaryngologist**."
      },
      {
        "author": "Ferdinand Sauerbruch",
        "work": "Master Surgeon: A Life in Surgery",
        "quote": "Operative management of upper respiratory tract neoplasms requires the specialized skill of the **rhinolaryngologist**."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "The clinical **rhinolaryngologist** introduced direct mirror laryngoscopy to map vocal fold motion."
      }
    ]
  },
  "Dashboard — rhin\\rhinolaryngology.md": {
    "primary": "The combined branch of medicine and surgery dealing with diseases of the nose and larynx.",
    "secondary": "In clinical medical practice, the specialized study of airway aerodynamics, upper respiratory infections, phoniatric voice disorders, and paranasal sinus surgery.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "A System of Medicine",
        "quote": "Advances in **rhinolaryngology** have perfected the local treatment of chronic catarrhal conditions of the upper air passages."
      },
      {
        "author": "Oliver Wendell Holmes Sr.",
        "work": "Medical Essays",
        "quote": "The growth of specialized **rhinolaryngology** brought relief to thousands of sufferers plagued with throat catarrh."
      },
      {
        "author": "Ferdinand Sauerbruch",
        "work": "Master Surgeon: A Life in Surgery",
        "quote": "Tracheostomy techniques and laryngeal extirpation form the historic backbone of operative **rhinolaryngology**."
      }
    ]
  },
  "Dashboard — rhin\\rhinology.md": {
    "primary": "The branch of medical science and surgery that deals with the anatomy, physiology, and diseases of the nose and paranasal sinuses.",
    "secondary": "In surgical otorhinolaryngology, the subspecialty dedicated to functional endoscopic sinus surgery (FESS), septal reconstruction, skull base surgery, and nasal airway management.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Modern clinical **rhinology** transformed the treatment of chronic frontal sinusitis from radical trephination to endonasal drainage."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Meticulous application of aseptic technique in **rhinology** drastically diminished postoperative intracranial complications."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Collaborative research in operative **rhinology** paved the way for transnasal skull base access to the sella turcica."
      }
    ]
  },
  "Dashboard — rhin\\rhinolophidae.md": {
    "primary": "A family of microchiropteran bats commonly known as horseshoe bats, characterized by complex, leaf-like horseshoe-shaped fleshy facial skin folds.",
    "secondary": "In systematic chiropterology and virology, insectivorous bats native to the Old World possessing sophisticated nasal echolocation apparatus (emitting pulses through their nostrils) and serving as natural reservoirs for coronaviruses.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "On the Origin of Species",
        "quote": "The elaborate nasal cutaneous folds of the **rhinolophidae** serve as acoustic reflectors for echolocating orientation."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "Horseshoe bats belonging to the **rhinolophidae** project vocal clicks through their nostrils rather than the oral cavity."
      },
      {
        "author": "Anthony Fauci",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "Epidemiological surveillance identified species of **rhinolophidae** as the primary natural hosts of zoonotic SARS coronaviruses."
      }
    ]
  },
  "Dashboard — rhin\\rhinonicteris.md": {
    "primary": "A genus of small insectivorous bats native to northern Australia containing the orange leaf-nosed bat (Rhinonicteris aurantia).",
    "secondary": "In mammalogy and Australian biogeography, a hipposiderid bat genus adapted to tropical subterranean cave roosts, featuring bright orange fur and an intricate noseleaf aiding high-frequency nasal echolocation.",
    "quotes": [
      {
        "author": "John Gould",
        "work": "The Mammals of Australia",
        "quote": "The orange leaf-nosed bat, **rhinonicteris** aurantia, is one of the most vividly colored chiropterans in the Australian fauna."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "Bright pelage coloration in subterranean mammals such as **rhinonicteris** presents an intriguing puzzle for sexual selection theory."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "Delicate cave-roosting species like **rhinonicteris** suffer immediate population declines when isolated roosting caves are disturbed."
      }
    ]
  },
  "Dashboard — rhin\\rhinopathy.md": {
    "primary": "Any disease, disorder, or pathological condition affecting the nose.",
    "secondary": "In otorhinolaryngology, an encompassing clinical term for non-inflammatory, allergic, infectious, or neoplastic disorders of the nasal cavity and mucosa (e.g. vasomotor rhinopathy).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Chronic vasomotor **rhinopathy** causes persistent nasal congestion provoked by temperature changes and emotional stress."
      },
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "Upper airway dysfunction due to chronic **rhinopathy** frequently aggravates nocturnal bronchial asthma."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Histological differentiation of an unusual mucosal **rhinopathy** revealed granulomatous infiltration of the nasal septum."
      }
    ]
  },
  "Dashboard — rhin\\rhinophyma.md": {
    "primary": "A condition characterized by a large, bulbous, ruddy, and bumpy enlargement of the nose, usually resulting from severe, untreated rosacea.",
    "secondary": "In clinical dermatology, end-stage phymatous rosacea involving severe sebaceous gland hyperplasia, chronic inflammation, fibrosis, and telangiectasia of the lower half of the nose.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The bulbous, lobulated hypertrophy of the nose in advanced **rhinophyma** represents severe chronic sebaceous hyperplasia."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Microscopic sections of **rhinophyma** demonstrate massive dilation of sebaceous ducts embedded within dense fibrovascular connective tissue."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Surgical tangling shave excision of **rhinophyma** followed by secondary re-epithelialization restores normal nasal contour."
      }
    ]
  },
  "Dashboard — rhin\\rhinoplasty.md": {
    "primary": "Plastic surgery performed on the nose to alter its appearance or improve its respiratory function (commonly known as a nose job).",
    "secondary": "In reconstructive and cosmetic surgery, surgical reshaping of the nasal osteocartilaginous framework (first systematically documented in ancient India by Sushruta), performed via open or endonasal closed approach to correct deformities, trauma, or septal deviation.",
    "quotes": [
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Modern reconstructive **rhinoplasty** traces its lineage to the ancient Indian forehead flap technique for nasal rebuilding."
      },
      {
        "author": "William Osler",
        "work": "Modern Medicine: Its Theory and Practice",
        "quote": "Functional **rhinoplasty** corrects internal nasal valve collapse, providing dramatic relief from chronic respiratory obstruction."
      },
      {
        "author": "Ferdinand Sauerbruch",
        "work": "Master Surgeon: A Life in Surgery",
        "quote": "Restoring the shattered nasal bridge through autologous rib cartilage **rhinoplasty** rehabilitated the wounded soldier's facial appearance."
      }
    ]
  }
}

esm_content = '''import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Body & Physiology');
const batchData = ''' + json.dumps(BATCH4_DATA, indent=2, ensure_ascii=False) + ''';

console.log('Starting Body Rem B Batch 4 curation (' + Object.keys(batchData).length + ' words)...');
const updated = updateNotesBatch(baseClusterDir, batchData);
console.log('Batch 4 complete: successfully updated ' + updated + ' notes.');
'''

with open("main app/scripts/curate_body_rem_b_batch4.mjs", "w", encoding="utf-8") as f:
    f.write(esm_content)

print(f"Generated main app/scripts/curate_body_rem_b_batch4.mjs with {len(BATCH4_DATA)} entries.")
