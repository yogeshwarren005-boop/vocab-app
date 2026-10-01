import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Medicine & Pathology";

const wordsData = {
  // === Dashboard — py ===
  "Dashboard — py/empyema.md": {
    word: "empyema",
    primary: "A collection of pus inside a naturally existing anatomical body cavity, especially the pleural space (pleural empyema).",
    secondary: "In thoracic surgery and pulmonology, an advanced purulent complication of bacterial pneumonia, thoracic trauma, or esophageal rupture requiring tube thoracostomy or decortication.",
    quotes: [
      { author: "Hippocrates", work: "Aphorisms", quote: "When **empyema** is evacuated by cautery or cutting, if pure white pus flows, the patients recover; but if mixed with bloody froth, they perish." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Exploratory puncture with a fine needle is the only certain method of detecting post-pneumonic **empyema** in the pleural cavity." },
      { author: "Sherwin B. Nuland", work: "Doctors: The Biography of Medicine", quote: "The evacuation of a foul **empyema** from the chest was one of the earliest successful major operations of antiquity." }
    ]
  },
  "Dashboard — py/pyemesis.md": {
    word: "pyemesis",
    primary: "The vomiting of pus or purulent material.",
    secondary: "In gastroenterology, an alarming clinical sign indicating the spontaneous rupture of an intra-abdominal, hepatic, or subphrenic abscess into the stomach or esophagus.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Copious **pyemesis** occurred when the huge amoebic abscess of the liver eroded through the diaphragm into the gastric fundus." },
      { author: "Percivall Pott", work: "Chirurgical Works", quote: "The patient experienced instant relief from epigastric oppression following an unexpected bout of **pyemesis**." },
      { author: "Abraham Verghese", work: "Cutting for Stone", quote: "The foul odor of the vomitus confirmed that **pyemesis** had ensued from the perforated gastric abscess." }
    ]
  },
  "Dashboard — py/pyemia.md": {
    word: "pyemia",
    primary: "Blood poisoning caused by the spread of pus-forming bacteria from an original focus of infection, characterized by metastatic abscesses.",
    secondary: "In nineteenth-century surgical pathology, a dreaded, often fatal septic condition marked by recurring rigors, drenching sweats, and multiple purulent deposits in internal organs.",
    quotes: [
      { author: "Joseph Lister", work: "On the Antiseptic Principle in the Practice of Surgery", quote: "Before the introduction of carbolic dressings, hospital gangrene and fatal **pyemia** stalked every surgical ward in Britain." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "I demonstrated that **pyemia** is caused by the detachment of infected fragments from a thrombus, which lodge downstream as purulent emboli." },
      { author: "Florence Nightingale", work: "Notes on Hospitals", quote: "Overcrowded, unventilated military hospitals became hotbeds of **pyemia**, destroying more brave soldiers than enemy artillery." }
    ]
  },
  "Dashboard — py/pyemic.md": {
    word: "pyemic",
    primary: "Of, relating to, caused by, or affected with pyemia; characterized by metastatic abscesses.",
    secondary: "In historical clinical pathology, describing septic fevers with violent chills, spiking temperatures, and purulent metastatic seeding throughout the viscera.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The onset of severe **pyemic** chills indicated that septic emboli had migrated from the infected heart valves to the kidneys." },
      { author: "Joseph Lister", work: "Collected Papers", quote: "Under antiseptic cleanliness, the dreaded **pyemic** abscesses that once riddled operative stumps completely disappeared." },
      { author: "Arthur Conan Doyle", work: "Round the Red Lamp", quote: "The old surgeon recognized the ominous **pyemic** flush on the patient's cheek with sinking dread." }
    ]
  },
  "Dashboard — py/pyesis.md": {
    word: "pyesis",
    primary: "The formation, generation, or discharge of pus; suppuration.",
    secondary: "In dermatological and surgical nosology, the pathological accumulation of dead neutrophils, liquefied necrotic tissue, and exudate in an infected wound.",
    quotes: [
      { author: "John Hunter", work: "A Treatise on the Blood, Inflammation, and Gun-shot Wounds", quote: "The process of **pyesis** represents nature's violent attempt to isolate and expel foreign matter from living tissue." },
      { author: "William Stewart Halsted", work: "Surgical Papers", quote: "A clean surgical incision with perfect hemostasis avoids tissue tension and the hazard of secondary **pyesis**." },
      { author: "Percivall Pott", work: "Chirurgical Observations", quote: "Unless free drainage is established, deep **pyesis** will burrow along the muscular fascial planes." }
    ]
  },
  "Dashboard — py/pyocyst.md": {
    word: "pyocyst",
    primary: "A cyst that has become filled with pus or infected with purulent exudate.",
    secondary: "In surgical urology and gynecology, a preexisting epithelial-lined cystic cavity (such as a renal or ovarian cyst) secondarily invaded by suppurative bacteria.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Infected renal echinococcus cysts frequently degenerate into a massive **pyocyst** requiring nephrostomy drainage." },
      { author: "Abraham Verghese", work: "Cutting for Stone", quote: "Upon exploring the retroperitoneum, the surgical team encountered a tense **pyocyst** clinging to the renal capsule." },
      { author: "Atul Gawande", work: "Complications", quote: "Careful aspiration of the suspected **pyocyst** yielded thick purulent fluid teeming with coliform bacilli." }
    ]
  },
  "Dashboard — py/pyogenesis.md": {
    word: "pyogenesis",
    primary: "The origin, formation, or physiological process of generating pus.",
    secondary: "In cellular immunology and microbiology, the recruitment of polymorphonuclear neutrophils guided by chemotactic leukotrienes and bacterial formyl peptides, ending in purulent lysis.",
    quotes: [
      { author: "Élie Metchnikoff", work: "Immunity in Infective Diseases", quote: "The phenomenon of **pyogenesis** is at bottom a heroic battle between predatory phagocytes and invasive bacteria." },
      { author: "Paul Ehrlich", work: "Studies in Immunity", quote: "The chemical chemotaxis that directs white cells to the bacterial invasion locus is the driving engine of **pyogenesis**." },
      { author: "Siddhartha Mukherjee", work: "The Song of the Cell", quote: "Neutrophils die by the millions in the drama of **pyogenesis**, releasing their chromatin nets to trap the invaders." }
    ]
  },
  "Dashboard — py/pyorrhea.md": {
    word: "pyorrhea",
    primary: "A discharge or flow of pus, especially from the gums and tooth sockets in advanced periodontitis (pyorrhea alveolaris).",
    secondary: "In dental medicine, chronic inflammatory periodontitis leading to destruction of periodontal ligament fibers, alveolar bone resorption, tooth loosening, and foul purulent exudate.",
    quotes: [
      { author: "Willoughby D. Miller", work: "The Micro-Organisms of the Human Mouth", quote: "Chronic **pyorrhea** alveolaris represents a polymicrobial infection destroying the connective tissue attachment of the teeth." },
      { author: "Sinclair Lewis", work: "Babbitt", quote: "He worried incessantly over his receding gums, dreading the socially humiliating ravages of **pyorrhea**." },
      { author: "G. V. Black", work: "Special Dental Pathology", quote: "Deep subgingival scaling is the only mechanical therapy capable of checking the purulent flow of **pyorrhea**." }
    ]
  },
  "Dashboard — py/pyorrhoea.md": {
    word: "pyorrhoea",
    primary: "A purulent discharge or flow of pus from mucous tissues, especially chronic purulent gum disease (standard British and classical medical spelling of pyorrhea).",
    secondary: "In historical Commonwealth medical texts, chronic periodontal infection characterized by pus oozing from deep periodontal pockets around the alveolar margins.",
    quotes: [
      { author: "George Bernard Shaw", work: "The Doctor's Dilemma", quote: "The fashionable Harley Street physician blamed all human infirmities upon chronic **pyorrhoea** and demanded total extraction of the teeth." },
      { author: "Virginia Woolf", work: "The Voyage Out", quote: "The elderly gentleman spoke with an impediment, having suffered for years from painful **pyorrhoea** of the gums." },
      { author: "Arthur Conan Doyle", work: "The Case-Book of Sherlock Holmes", quote: "The dental evidence showed marked **pyorrhoea**, matching the missing banker's recorded odontological chart." }
    ]
  },
  "Dashboard — py/pyosis.md": {
    word: "pyosis",
    primary: "The formation or development of pus in an infected tissue or organ; suppuration.",
    secondary: "In historical pathology, the transformation of acute inflammatory serous exudate into thick purulent fluid under the influence of pyogenic cocci.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The rapid progression of the cellulitis toward deep **pyosis** necessitated wide surgical incisions for relief of tension." },
      { author: "Joseph Lister", work: "Antiseptic Surgery", quote: "The absence of **pyosis** beneath the protective gauze proved that microscopic atmospheric germs had been excluded." },
      { author: "Percivall Pott", work: "Chirurgical Works", quote: "When **pyosis** establishes itself beneath the cranial periosteum, trephining must not be delayed." }
    ]
  },
  "Dashboard — py/pyoureter.md": {
    word: "pyoureter",
    primary: "The accumulation or distension of a ureter with pus, typically caused by an obstructed and infected urinary tract.",
    secondary: "In urology, an acute or chronic condition where an impacted ureteral calculus or stricture causes suppurative stasis, threatening urosepsis and renal parenchyma destruction.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Impacted calculous obstruction combined with ascending cystitis rapidly produces an acute **pyoureter** and perinephric phlegmon." },
      { author: "Abraham Verghese", work: "Cutting for Stone", quote: "The retrograde pyelogram revealed a dilated, tortuous **pyoureter** filled with thick purulent debris behind the stone." },
      { author: "Sherwin B. Nuland", work: "The Mysteries Within", quote: "Urgent drainage of a **pyoureter** via double-J stent or percutaneous nephrostomy is life-saving in obstructive sepsis." }
    ]
  },

  // === Dashboard — hygie ===
  "Dashboard — hygie/hygie.md": {
    word: "hygie",
    primary: "The foundational Greek combining root (from hygies, ὑγιής) signifying sound, healthy, whole, or wholesome.",
    secondary: "In lexical and etymological morphology, the base morpheme underlying hygiene, hygienic, and the personified deity of health, Hygieia.",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The root **hygie** enters English through the Greek hygies, denoting living soundly, healthily, and free from disease." },
      { author: "James Murray", work: "A New English Dictionary on Historical Principles", quote: "Terms compounded with **hygie** refer universally to the preservation of bodily well-being and sanitary science." },
      { author: "H. G. Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "In classical Greek, hygieia (stem **hygie**-) was health of body, sound judgment, and physical wholeness." }
    ]
  },
  "Dashboard — hygie/Hygieia.md": {
    word: "Hygieia",
    primary: "The Greek goddess of health, cleanliness, and sanitation, daughter of the divine physician Asclepius.",
    secondary: "In classical mythology and iconography, typically depicted holding a bowl from which a sacred serpent drinks, symbolizing the prevention of disease through wholesome living (hygiene).",
    quotes: [
      { author: "John Keats", work: "Ode to Apollo", quote: "Where **Hygieia** weaves her sacred wand, no pestilence can blast the blooming land." },
      { author: "Oliver Wendell Holmes Sr.", work: "Currents and Counter-Currents in Medical Science", quote: "The temple of **Hygieia** welcomes pure air, temperance, and water, scorning the toxic nostrums of greedy charlatans." },
      { author: "James George Frazer", work: "Pausanias's Description of Greece", quote: "At Epidaurus, statues of **Hygieia** stood beside those of Asclepius, for the Greeks honored prevention as equal to cure." }
    ]
  },
  "Dashboard — hygie/hygiene.md": {
    word: "hygiene",
    primary: "Conditions or practices conducive to maintaining health and preventing disease, especially through cleanliness.",
    secondary: "In public health and preventive medicine, the scientific principles and social practices designed to promote individual and communal physical, occupational, and environmental sanitation.",
    quotes: [
      { author: "Florence Nightingale", work: "Notes on Nursing", quote: "The very first canon of nursing, the absolute essential of all **hygiene**, is to keep the air the patient breathes as pure as the external air." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Personal and municipal **hygiene** has achieved vastly more for human longevity than all the chemical drugs of the dispensatory." },
      { author: "George Orwell", work: "The Road to Wigan Pier", quote: "In the dreary industrial slums, the basic requirements of human **hygiene** were rendered impossible by water shortages and coal dust." }
    ]
  },
  "Dashboard — hygie/hygienic.md": {
    word: "hygienic",
    primary: "Conducive to maintaining good health, preventing disease, and promoting cleanliness; sanitary.",
    secondary: "Characterized by clean, sterile, or wholesome living and working environments.",
    quotes: [
      { author: "H. G. Wells", work: "A Modern Utopia", quote: "The utopian cities were designed upon strict **hygienic** lines, with abundant sunlight, pure water, and smokeless dwellings." },
      { author: "Aldous Huxley", work: "Brave New World", quote: "Everything in the conditioning rooms was orderly, gleaming, and intensely **hygienic**." },
      { author: "Sinclair Lewis", work: "Arrowsmith", quote: "He scrubbed the wooden tables with carbolic soap, creating a **hygienic** barrier against laboratory contamination." }
    ]
  },
  "Dashboard — hygie/hygienical.md": {
    word: "hygienical",
    primary: "Pertaining to hygiene, sanitation, or the preservation of health; hygienic (historical and formal variant).",
    secondary: "Relating to public health treatises, sanitary regulations, or medical preventative science.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Science and Culture", quote: "The application of physical science to **hygienical** problems has halved the urban death rate from contagious fevers." },
      { author: "Herbert Spencer", work: "Education: Intellectual, Moral, and Physical", quote: "Knowledge of **hygienical** laws is more precious to the child than familiarity with all the battles of antiquity." },
      { author: "William Playfair", work: "The Commercial and Political Atlas", quote: "The report established that proper **hygienical** measures in manufacturing towns increased worker productivity." }
    ]
  },
  "Dashboard — hygie/hygienically.md": {
    word: "hygienically",
    primary: "In a hygienic, clean, and sanitary manner; so as to preserve health.",
    secondary: "Conforming to the rigorous sanitation standards required in food processing, surgical suites, and public water supplies.",
    quotes: [
      { author: "Florence Nightingale", work: "Notes on Hospitals", quote: "Unless bedding is washed and dried **hygienically** in fresh air, it retains the infectious emanations of the sick." },
      { author: "Upton Sinclair", work: "The Jungle", quote: "Meat destined for the market was handled in a manner that was neither clean nor **hygienically** defensible." },
      { author: "Atul Gawande", work: "Better", quote: "Surgeons who scrub **hygienically** for the full protocol drastically reduce the incidence of post-operative infection." }
    ]
  },
  "Dashboard — hygie/hygienics.md": {
    word: "hygienics",
    primary: "The science or system of principles and rules for the preservation of health; hygiene as a scientific discipline.",
    secondary: "In late nineteenth-century educational and military curricula, the comprehensive study of ventilation, dietetics, drainage, and physical culture.",
    quotes: [
      { author: "William Osler", work: "Aequanimitas", quote: "The chair of **hygienics** must teach the student that clean water and fresh air are the primary instruments of public health." },
      { author: "Herbert Spencer", work: "First Principles", quote: "The principles of physiological **hygienics** demonstrate that bodily vigor cannot be sacrificed without mental decline." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "A practical treatise on domestic **hygienics** is worth more to a mother than a whole shelf of patent medicines." }
    ]
  },
  "Dashboard — hygie/hygienise.md": {
    word: "hygienise",
    primary: "To make clean, healthy, or sanitary; to disinfect or subject to hygienic conditions (chiefly British spelling of hygienize).",
    secondary: "In public sanitation, to treat contaminated environments or implements so as to eliminate microbiological hazards.",
    quotes: [
      { author: "Florence Nightingale", work: "Notes on Nursing", quote: "The town council must drain the stagnant ditches and **hygienise** the public water pumps without delay." },
      { author: "George Bernard Shaw", work: "Plays Pleasant", quote: "Modern reformers dream that they can **hygienise** human nature by scrubbing every corner of London with soap." },
      { author: "H. G. Wells", work: "The Shape of Things to Come", quote: "The sanitary corps was dispatched to **hygienise** the abandoned ruins before the new city could be erected." }
    ]
  },
  "Dashboard — hygie/hygienist.md": {
    word: "hygienist",
    primary: "A person skilled in or dedicated to the promotion of hygiene and health; especially a licensed dental hygienist.",
    secondary: "In occupational health and public sanitation, a specialist who inspects and mitigates physical, chemical, or biological hazards in workplaces and communities.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The modern public **hygienist** has become the guardian of cities, tracing epidemics to their hidden microbial sources." },
      { author: "Sinclair Lewis", work: "Arrowsmith", quote: "As county health officer, Martin acted as a zealous **hygienist**, condemning polluted wells despite the fury of landlords." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "The industrial **hygienist** warned that continuous exposure to chemical vapors posed grave neurological dangers to workers." }
    ]
  },
  "Dashboard — hygie/hygienize.md": {
    word: "hygienize",
    primary: "To render hygienic, wholesome, clean, or sanitary; to cleanse thoroughly.",
    secondary: "In municipal engineering, to purify water supplies, treat sewage, or remodel tenements to eliminate breeding grounds for disease.",
    quotes: [
      { author: "Edwin Chadwick", work: "Report on the Sanitary Condition of the Labouring Population", quote: "To **hygienize** the great manufacturing centers, we must lay down subterranean drainage pipes and provide unpolluted river water." },
      { author: "Upton Sinclair", work: "The Jungle", quote: "Federal inspectors promised to **hygienize** the packinghouses, enforcing clean uniforms and tiled slaughter floors." },
      { author: "Lewis Mumford", work: "The City in History", quote: "Nineteenth-century urban planners sought to **hygienize** the crowded industrial city by introducing broad avenues and public parks." }
    ]
  },
  "Dashboard — hygie/unhygienic.md": {
    word: "unhygienic",
    primary: "Not clean, sanitary, or wholesome; liable to harbor disease-causing microorganisms or foster illness.",
    secondary: "In public health inspection, describing conditions, facilities, or practices that violate established sanitation codes and promote contagion.",
    quotes: [
      { author: "George Orwell", work: "The Road to Wigan Pier", quote: "The dark, damp basement was disgustingly **unhygienic**, its crumbling walls coated with green mold." },
      { author: "Florence Nightingale", work: "Notes on Hospitals", quote: "To place wounded men in such crowded, **unhygienic** wards is to deliver them over to hospital gangrene and death." },
      { author: "Atul Gawande", work: "Better", quote: "An **unhygienic** stethoscope carried from patient to patient can act as a vector for drug-resistant bacteria." }
    ]
  },
  "Dashboard — hygie/unhygienically.md": {
    word: "unhygienically",
    primary: "In a manner that is unclean, dirty, or unsanitary; without proper regard for health and cleanliness.",
    secondary: "Handled or maintained under conditions that facilitate bacterial contamination or spread infection.",
    quotes: [
      { author: "Upton Sinclair", work: "The Jungle", quote: "The spoiled meat was stored **unhygienically** on open wooden floors where rats nested undisturbed." },
      { author: "Charles Dickens", work: "Bleak House", quote: "The scavengers lived **unhygienically** along the foul banks of the Thames, breathing the pestilential night air." },
      { author: "Atul Gawande", work: "The Checklist Manifesto", quote: "Surgeons who prep **unhygienically** in haste increase the likelihood of deep surgical wound suppuration." }
    ]
  },

  // === Dashboard — myl ===
  "Dashboard — myl/amyl.md": {
    word: "amyl",
    primary: "The univalent hydrocarbon radical pentyl (C5H11-), historically derived from amyl alcohol obtained in the distillation of fermented starch.",
    secondary: "In organic chemistry and historical therapeutics, the chemical group present in amyl nitrite, a rapidly acting vasodilator used to relieve angina pectoris.",
    quotes: [
      { author: "Thomas Lauder Brunton", work: "On the Use of Nitrite of Amyl in Angina Pectoris", quote: "Inhalation of **amyl** nitrite caused the flushed face and dilated peripheral vessels, relieving the suffocating angina spasm within minutes." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Resident Patient", quote: "A broken pearl of **amyl** nitrite lay upon the carpet, indicating the patient's desperate attempt to avert a cardiac paroxysm." },
      { author: "Oliver Sacks", work: "Uncle Tungsten", quote: "My uncle explained that **amyl** acetate was responsible for the sweet, pear-drop aroma that filled the chemistry shed." }
    ]
  },
  "Dashboard — myl/amyloid.md": {
    word: "amyloid",
    primary: "An abnormal, waxy, insoluble protein aggregate that deposits in extracellular spaces of organs and tissues; or resembling starch.",
    secondary: "In histopathology and neurobiology, insoluble beta-pleated sheet fibrils (such as amyloid-beta in Alzheimer's plaques) that stain with Congo red and exhibit apple-green birefringence under polarized light.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Because this waxy substance in the degenerate liver stained with iodine like starch, I gave it the name **amyloid**, though it is truly proteinaceous." },
      { author: "Alois Alzheimer", work: "On a Peculiar Disease of the Cerebral Cortex", quote: "Dense extracellular deposits of silver-staining **amyloid** surrounded the dying neurons in the cortex of the demented patient." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Chronic suppurative osteomyelitis was formerly the commonest precursor of waxy **amyloid** degeneration of the kidneys and spleen." }
    ]
  },
  "Dashboard — myl/amyloidal.md": {
    word: "amyloidal",
    primary: "Of, relating to, or resembling starch or amyloid; starch-like.",
    secondary: "In pathology, describing organs or microscopic tissue sections displaying waxy amyloid infiltration.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The **amyloidal** spleen cuts with the firm consistency of bacon rind, presenting a translucent, waxy surface." },
      { author: "William Osler", work: "Lectures on the Diagnosis of Abdominal Tumors", quote: "Palpation revealed an enlarged, smooth, **amyloidal** liver extending four fingerbreadths beneath the costal margin." },
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "Certain plant seeds store nutrients in the form of thick **amyloidal** cell walls that dissolve during germination." }
    ]
  },
  "Dashboard — myl/amyloidosis.md": {
    word: "amyloidosis",
    primary: "A rare group of diseases characterized by the abnormal deposition of insoluble amyloid protein fibrils in organs and tissues, impairing their normal function.",
    secondary: "In internal medicine, a condition categorized into primary (AL), secondary (AA), hereditary (ATTR), or senile forms, often leading to restrictive cardiomyopathy, nephrotic syndrome, or autonomic neuropathy.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Systemic **amyloidosis** turns the liver and spleen into massive, painless viscera of glassy, lardaceous texture." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "The unexplained heart failure and purpura around the patient's eyes pointed to cardiac **amyloidosis**." },
      { author: "Atul Gawande", work: "Being Mortal", quote: "Advanced cardiac **amyloidosis** stiffened the heart muscle, resisting all standard pharmacological therapies." }
    ]
  },
  "Dashboard — myl/amylolysis.md": {
    word: "amylolysis",
    primary: "The digestion, enzymatic conversion, or hydrolysis of starch into soluble sugars such as maltose, dextrins, and glucose.",
    secondary: "In gastrointestinal physiology and biochemistry, the catalytic process executed by salivary and pancreatic alpha-amylases breaking alpha-1,4-glucosidic bonds in dietary starches.",
    quotes: [
      { author: "Claude Bernard", work: "Mémoire sur le pancréas", quote: "Pancreatic juice executes rapid **amylolysis**, converting boiled starch paste into fermentable sugar in a few minutes." },
      { author: "William Beaumont", work: "Experiments and Observations on the Gastric Juice", quote: "Salivary **amylolysis** begins in the mouth, but gastric acidity temporarily arrests the conversion until the chime reaches the duodenum." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Nearly all dietary carbohydrate undergoes complete **amylolysis** before absorption across the brush border." }
    ]
  },
  "Dashboard — myl/amylolytic.md": {
    word: "amylolytic",
    primary: "Capable of converting or hydrolyzing starch into sugars; exhibiting amylase activity.",
    secondary: "In zymology and digestive physiology, describing enzymes (such as ptyalin or pancreatin) that cleave complex starch polysaccharides.",
    quotes: [
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", quote: "The **amylolytic** ferments of the pancreatic secretion act upon raw and cooked starches alike with astonishing power." },
      { author: "Louis Pasteur", work: "Studies on Fermentation", quote: "The germination of barley develops strong **amylolytic** diastase, which saccharifies the grain mash for brewing." },
      { author: "Ivan Pavlov", work: "The Work of the Digestive Glands", quote: "A diet rich in bread stimulates the pancreas to secrete a juice with high **amylolytic** potency." }
    ]
  },
  "Dashboard — myl/amylopectin.md": {
    word: "amylopectin",
    primary: "A water-insoluble, highly branched polysaccharide that, along with amylose, makes up starch.",
    secondary: "In carbohydrate biochemistry, a major constituent (comprising seventy to eighty percent) of natural plant starches, consisting of alpha-1,4-linked glucose units with alpha-1,6 branches every twenty-four to thirty residues.",
    quotes: [
      { author: "Linus Pauling", work: "General Chemistry", quote: "While amylose forms straight helical chains, **amylopectin** forms a sprawling branched network resembling a miniature molecular tree." },
      { author: "Melvin Calvin", work: "The Path of Carbon in Photosynthesis", quote: "Photosynthetic sugars are polymerised into **amylopectin** within the plastids to provide compact long-term energy storage." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Debranching enzymes are required in addition to alpha-amylase to completely hydrolyze the complex structure of **amylopectin**." }
    ]
  },
  "Dashboard — myl/amylophagia.md": {
    word: "amylophagia",
    primary: "The abnormal, compulsive craving for and eating of purified starch (such as cornstarch or laundry starch), a specialized form of pica.",
    secondary: "In clinical hematology and nutritional psychiatry, a behavioral symptom frequently associated with iron deficiency anemia or pregnancy.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Curious varieties of pica, such as chalk-eating and **amylophagia**, are observed among chlorotic young women." },
      { author: "Jerome Groopman", work: "The Anatomy of Hope", quote: "The patient's secret **amylophagia**, consuming boxes of cornstarch daily, vanished as soon as her severe iron deficiency was corrected." },
      { author: "Oliver Sacks", work: "An Anthropologist on Mars", quote: "Nutritional pica syndromes like **amylophagia** reveal how deep biochemical deficits can hijack conscious dietary behavior." }
    ]
  },
  "Dashboard — myl/amyloplast.md": {
    word: "amyloplast",
    primary: "A non-pigmented organelle (leucoplast) in plant cells that synthesizes and stores starch granules.",
    secondary: "In plant physiology, specialized plastids abundant in roots and storage tubers that also function as statoliths in root cap cells, settling under gravity to mediate gravitropism.",
    quotes: [
      { author: "Charles Darwin", work: "The Power of Movement in Plants", quote: "Heavy particles in the cells of the root cap, which modern botanists identify as the **amyloplast**, tumble under gravity to guide the downward growth of roots." },
      { author: "Julius von Sachs", work: "Lectures on the Physiology of Plants", quote: "Each **amyloplast** acts as a microscopic starch factory, precipitating concentric layers of carbohydrate inside the tuber." },
      { author: "Peter Raven", work: "Biology of Plants", quote: "Dense starch granules inside the **amyloplast** displace the endoplasmic reticulum, initiating the gravitropic auxin gradient." }
    ]
  },
  "Dashboard — myl/amylose.md": {
    word: "amylose",
    primary: "A water-soluble linear polysaccharide component of starch composed of unbranched chains of D-glucose units linked by alpha-1,4-glucosidic bonds.",
    secondary: "In food chemistry and biochemistry, the starch fraction (twenty to thirty percent) that adopts a helical secondary structure capable of complexing with iodine to produce an intense deep blue color.",
    quotes: [
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The famous blue color of the iodine-starch test is produced by polyiodide ions trapped inside the helical core of the **amylose** molecule." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Salivary amylase cleaves **amylose** into maltose and maltotriose through endo-hydrolysis of internal alpha-1,4 bonds." },
      { author: "Oliver Sacks", work: "Uncle Tungsten", quote: "I marveled as a single drop of brown tincture turned the starch paste containing **amylose** into intense midnight blue." }
    ]
  },
  "Dashboard — myl/amylum.md": {
    word: "amylum",
    primary: "Starch, especially fine powdered pharmaceutical starch prepared from wheat, corn, or potatoes (Late Latin from Greek amylos).",
    secondary: "In historical pharmacopeias, a neutral excipient, dusting powder, and demulcent used to bind tablets, prepare soothing pastes, or counteract iodine poisoning.",
    quotes: [
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "The apothecary dusted the pills with powdered **amylum** to prevent them from adhering to the box." },
      { author: "John Lindley", work: "Flora Medica", quote: "Pure **amylum** obtained from maranta roots forms an easily digested invalid food known as arrowroot." },
      { author: "Asa Gray", work: "Structural Botany", quote: "Under the microscope, grains of **amylum** exhibit concentric rings surrounding an eccentric nucleus or hilum." }
    ]
  },
  "Dashboard — myl/myl.md": {
    word: "myl",
    primary: "The foundational Greek combining root (from myle, μύλη) meaning a mill, millstone, grinder, or molar tooth.",
    secondary: "In etymological analysis, the parent root of mylo- (molar/mill) and amylon (starch, literally 'unmilled' or meal not needing a millstone).",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The element **myl** corresponds to the Greek myle (a mill), giving rise to anatomical terms for the jaw and molar teeth." },
      { author: "James Murray", work: "A New English Dictionary on Historical Principles", quote: "From Greek myle (root **myl**-) arose mylohyoid, designating the muscular floor of the mouth adjacent to the grinding teeth." },
      { author: "H. G. Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "In classical Greek, myle (stem **myl**-) signified a millstone, a handmill, or the kneepan and molar grinders." }
    ]
  },

  // === Dashboard — iatr ===
  "Dashboard — iatr/iatr.md": {
    word: "iatr",
    primary: "The foundational Greek combining root (from iatros, ἰατρός) meaning a physician, healer, or medical treatment.",
    secondary: "In biomedical nomenclature, a prolific combining form underlying iatrogenic, pediatrics, psychiatry, and physiatry.",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The root **iatr** descends directly from the Greek iatros, a healer or physician, from iasthai (to heal)." },
      { author: "James Murray", work: "A New English Dictionary on Historical Principles", quote: "Scientific terms ending in -iatry or incorporating **iatr** denote specialized branches of the medical healing art." },
      { author: "H. G. Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "In Homeric times, iatros (stem **iatr**-) was honoured as a man worth many warriors for his skill in cutting out arrows and soothing wounds." }
    ]
  },
  "Dashboard — iatr/iatrogenic.md": {
    word: "iatrogenic",
    primary: "Relating to or caused by medical examination, treatment, or diagnostic procedures; inadvertently induced by a physician or medication.",
    secondary: "In healthcare quality and patient safety, describing adverse drug reactions, hospital-acquired infections, surgical complications, or diagnostic errors caused by medical intervention.",
    quotes: [
      { author: "Ivan Illich", work: "Medical Nemesis: The Expropriation of Health", quote: "The epidemic of **iatrogenic** disease has become a major threat to health, turning medicine itself into a pathogen." },
      { author: "Atul Gawande", work: "Complications: A Surgeon's Notes on an Imperfect Science", quote: "Every operation carries the inherent hazard of **iatrogenic** injury, demanding meticulous care with every cut." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "The patient's sudden kidney failure was traced to an **iatrogenic** toxicity from concurrent radiographic contrast and diuretics." }
    ]
  },
  "Dashboard — iatr/iatros.md": {
    word: "iatros",
    primary: "A physician or healer in ancient Greece.",
    secondary: "In the history of classical medicine, a trained medical practitioner who swore the Hippocratic Oath, distinguished from superstitious charlatans and root-cutters.",
    quotes: [
      { author: "Homer", work: "The Iliad", quote: "A physician, an **iatros**, is a man worth many other men, skilled to cut out darts and spread soothing unguents." },
      { author: "Plato", work: "Gorgias", quote: "The true **iatros** does not flatter the sick man's palate, but prescribes bitter draughts for the soul's restoration." },
      { author: "William Osler", work: "The Evolution of Modern Medicine", quote: "The ancient Greek **iatros** freed medicine from priestly incantations, establishing clinical observation at the bedside." }
    ]
  },
  "Dashboard — iatr/pediatric.md": {
    word: "pediatric",
    primary: "Relating to the branch of medicine concerned with the medical care and diseases of infants, children, and adolescents.",
    secondary: "Specialized in developmental physiology, pediatric pharmacology, congenital disorders, and childhood vaccinations.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A sound understanding of infant nutrition forms the bedrock of modern **pediatric** practice." },
      { author: "Abraham Verghese", work: "Cutting for Stone", quote: "The **pediatric** ward echoed with the cries of malnourished infants, their mothers rocking them under mosquito nets." },
      { author: "Atul Gawande", work: "Better", quote: "In the **pediatric** surgical intensive care unit, minute changes in fluid balance can spell the difference between life and death." }
    ]
  },
  "Dashboard — iatr/pediatrician.md": {
    word: "pediatrician",
    primary: "A medical doctor who specializes in the care, development, and diseases of children from infancy through adolescence.",
    secondary: "A specialist trained in monitoring developmental milestones, managing congenital anomalies, and providing preventive childhood immunizations.",
    quotes: [
      { author: "Benjamin Spock", work: "Baby and Child Care", quote: "Trust yourself; you know more than you think you do, and consult your **pediatrician** whenever serious illness threatens." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "The experienced **pediatrician** diagnosed the rare metabolic disorder simply by observing the infant's subtle lethargy." },
      { author: "Perri Klass", work: "A Not Entirely Benign Procedure", quote: "As a young **pediatrician**, I learned that listening to a mother's intuition often provides the crucial diagnostic clue." }
    ]
  },
  "Dashboard — iatr/pediatrics.md": {
    word: "pediatrics",
    primary: "The branch of medicine dealing with the health and medical care of infants, children, and adolescents.",
    secondary: "In medical history, established as an autonomous medical specialty in the nineteenth century (pioneered by Abraham Jacobi) to address the unique physiology of growing children.",
    quotes: [
      { author: "Abraham Jacobi", work: "Therapeutics of Infancy and Childhood", quote: "The foundation of **pediatrics** as an independent discipline rests upon the truth that a child is not merely a miniature adult." },
      { author: "William Osler", work: "Aequanimitas", quote: "No department of clinical medicine offers greater rewards than **pediatrics**, preserving the budding promise of human life." },
      { author: "Siddhartha Mukherjee", work: "The Song of the Cell", quote: "Advances in cellular **pediatrics** transformed childhood acute lymphoblastic leukemia from an absolute death sentence into a curable disease." }
    ]
  },
  "Dashboard — iatr/pediatrist.md": {
    word: "pediatrist",
    primary: "A physician who specializes in the treatment of diseases of children; an older or alternative term for pediatrician.",
    secondary: "In historical nineteenth- and early twentieth-century American medical literature, the standard term for a child specialist before 'pediatrician' gained universal dominance.",
    quotes: [
      { author: "Abraham Jacobi", work: "Infant Diet", quote: "The conscientious **pediatrist** must instruct the community on clean milk supplies to stamp out summer diarrhea." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "We consulted a renowned **pediatrist** regarding the child's persistent croup and nocturnal fevers." },
      { author: "Sinclair Lewis", work: "Arrowsmith", quote: "The fashionable city **pediatrist** catered to wealthy mothers anxious over teething powders and infant formulas." }
    ]
  },
  "Dashboard — iatr/physiatry.md": {
    word: "physiatry",
    primary: "The branch of medicine concerned with physical medicine and rehabilitation (PM&R), focused on diagnosing and treating musculoskeletal and neurological impairments.",
    secondary: "In multidisciplinary clinical practice, a specialty aimed at restoring maximal independence and physical function in patients recovering from stroke, spinal cord injury, amputation, or traumatic brain injury.",
    quotes: [
      { author: "Howard A. Rusk", work: "A World to Care For: The Autobiography of Howard A. Rusk", quote: "The mission of **physiatry** is not merely to save life, but to return the patient to the highest possible dignity and utility." },
      { author: "Oliver Sacks", work: "A Leg to Stand On", quote: "Through intensive **physiatry**, the patient re-learns how to recruit dormant neural pathways to operate a paralyzed limb." },
      { author: "Atul Gawande", work: "Being Mortal", quote: "Modern **physiatry** emphasizes functional mobility and adaptive independence over passive hospital convalescence." }
    ]
  },
  "Dashboard — iatr/podiatrist.md": {
    word: "podiatrist",
    primary: "A healthcare professional qualified by medical training to diagnose and treat disorders of the foot, ankle, and related structures of the leg.",
    secondary: "In orthopedic and wound-care medicine, a specialist who manages diabetic foot ulcers, biomechanical gait abnormalities, structural deformities (bunions, hammertoes), and sports injuries.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Diabetic peripheral neuropathy mandates regular inspection by a skilled **podiatrist** to prevent occult gangrene." },
      { author: "Atul Gawande", work: "Better", quote: "The **podiatrist** skillfully debrided the plantar ulcer, relieving pressure points that prevented soft tissue healing." },
      { author: "Sherwin B. Nuland", work: "How We Die", quote: "Routine foot care by a **podiatrist** preserves mobility and autonomy for thousands of elderly patients." }
    ]
  },
  "Dashboard — iatr/podiatry.md": {
    word: "podiatry",
    primary: "The branch of medicine and healthcare devoted to the study, diagnosis, and medical and surgical treatment of disorders of the foot, ankle, and lower extremity.",
    secondary: "In allied health disciplines, historically evolving from chiropody into an autonomous surgical and biomechanical specialty critical in sports medicine and diabetic foot salvage.",
    quotes: [
      { author: "Atul Gawande", work: "The Checklist Manifesto", quote: "In modern diabetic limb-salvage clinics, preventive **podiatry** reduces lower extremity amputations dramatically." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "The clinical spectrum of **podiatry** spans from delicate microvascular reconstructive surgery to corrective gait orthotics." },
      { author: "Sherwin B. Nuland", work: "The Mysteries Within", quote: "Specialized **podiatry** restores functional human bipedalism when arthritis or traumatic fractures crush the tarsal arches." }
    ]
  },
  "Dashboard — iatr/psychiatrist.md": {
    word: "psychiatrist",
    primary: "A medical doctor who specializes in the diagnosis, treatment, and prevention of mental, emotional, and behavioral disorders.",
    secondary: "In modern medicine, a physician qualified to assess both the neurobiological and psychological components of mental illness, authorized to prescribe psychotropic medication and deliver psychotherapy.",
    quotes: [
      { author: "Sigmund Freud", work: "The Question of Lay Analysis", quote: "The **psychiatrist** must listen with evenly suspended attention, allowing the patient's unconscious associations to reveal their hidden conflicts." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "As a **psychiatrist** and neurologist, I could not separate the neurological lesion from the existential crisis of the patient." },
      { author: "Sylvia Plath", work: "The Bell Jar", quote: "The **psychiatrist** spoke with a gentle, nonjudgmental cadence that cracked the bell jar of her despair." }
    ]
  },
  "Dashboard — iatr/psychiatry.md": {
    word: "psychiatry",
    primary: "The branch of medicine focused on the diagnosis, treatment, and prevention of mental, emotional, and behavioral disorders.",
    secondary: "In the history of medicine, the clinical science (pioneered by Philippe Pinel and Emil Kraepelin) that emancipated mental illness from demonic superstition and integrated it with clinical neurobiology and psychology.",
    quotes: [
      { author: "Philippe Pinel", work: "A Treatise on Insanity", quote: "To unchain the insane and treat them with moral dignity marked the true birth of scientific **psychiatry**." },
      { author: "Emil Kraepelin", work: "Lectures on Clinical Psychiatry", quote: "Modern **psychiatry** requires meticulous longitudinal case studies to differentiate dementia praecox from manic-depressive insanity." },
      { author: "William James", work: "The Principles of Psychology", quote: "The discoveries of **psychiatry** illuminate normal mental life by exposing the fault lines along which consciousness fractures." }
    ]
  },

  // === Dashboard — onco ===
  "Dashboard — onco/hematoma.md": {
    word: "hematoma",
    primary: "A localized collection of blood outside the blood vessels, usually in liquid form within tissue, resulting from disease or trauma; a blood clot.",
    secondary: "In neurosurgery and emergency medicine, an intracranial hemorrhage (such as an epidural or subdural hematoma) that expands within the rigid cranium, compressing the brainstem.",
    quotes: [
      { author: "Percivall Pott", work: "Chirurgical Works", quote: "A tense, expanding **hematoma** beneath the fractured temporal bone demands urgent trephining to evacuate the clot." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Subdural **hematoma** in the elderly may mimic dementia or stroke, presenting with fluctuating lethargy days after a minor fall." },
      { author: "Atul Gawande", work: "Complications", quote: "The surgeon peeled back the fascia, revealing a dark, jelly-like **hematoma** putting pressure on the sciatic nerve." }
    ]
  },
  "Dashboard — onco/lipoma.md": {
    word: "lipoma",
    primary: "A slow-growing, benign tumor composed of mature adipose (fat) tissue, typically soft, mobile, and situated just beneath the skin.",
    secondary: "In dermatological and general surgery, the most common soft-tissue mesenchymal neoplasm in adults, typically painless and requiring surgical excision only if cosmetically bothersome or compressing nerves.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The subcutaneous lump was soft, lobulated, and freely movable, presenting the classic characteristics of a benign **lipoma**." },
      { author: "Abraham Verghese", work: "Cutting for Stone", quote: "Under local anesthesia, the surgeon enucleated the large encapsulated **lipoma** from the patient's shoulder in a single sweep." },
      { author: "Atul Gawande", work: "Complications", quote: "Excising a simple **lipoma** is the first procedure every surgical intern masters before advancing to deep visceral surgery." }
    ]
  },
  "Dashboard — onco/lymphoma.md": {
    word: "lymphoma",
    primary: "A cancer of the lymphatic system, originating in lymphocytes (white blood cells) and affecting lymph nodes, the spleen, and bone marrow.",
    secondary: "In hematologic oncology, broadly classified into Hodgkin lymphoma (marked by pathognomonic Reed–Sternberg cells) and diverse aggressive or indolent non-Hodgkin lymphomas.",
    quotes: [
      { author: "Thomas Hodgkin", work: "On Some Morbid Appearances of the Absorbent Glands and Spleen", quote: "The painless enlargement of multiple absorbent glands in these cases represents a distinct primary systemic disease, now termed **lymphoma**." },
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "Combination chemotherapy with MOPP cured advanced Hodgkin **lymphoma**, demonstrating for the first time that metastatic cancer could be eradicated with drugs." },
      { author: "Jerome Groopman", work: "The Anatomy of Hope", quote: "The biopsy of the cervical lymph node confirmed an aggressive B-cell **lymphoma**, prompting immediate immunotherapy." }
    ]
  },
  "Dashboard — onco/onc 2.md": {
    word: "onc 2",
    primary: "The foundational Greek combining root (from onkos, ὄγκος) meaning a mass, bulk, swelling, or tumor; duplicate root entry.",
    secondary: "In lexical classification and database morphology, the variant root designation for oncology and neoplastic nomenclature.",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The root **onc** stems from the Greek onkos, meaning bulk or tumor, forming the prefix of all neoplastic medical terms." },
      { author: "James Murray", work: "A New English Dictionary on Historical Principles", quote: "In medical terminology, **onc** denotes pathological swellings, whether benign adenomas or invasive carcinomas." },
      { author: "H. G. Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The Greek onkos (root **onc**-) originally signified mass or burden, later adopted by physicians for abnormal bodily growths." }
    ]
  },
  "Dashboard — onco/oncocyte.md": {
    word: "oncocyte",
    primary: "A large, specialized epithelial cell characterized by abundant, deeply eosinophilic, granular cytoplasm packed with mitochondria.",
    secondary: "In surgical pathology and histology, an altered cell found in tumors (oncocytomas) or hyperplastic lesions of the thyroid (Hürthle cells), salivary glands, parathyroid, and kidneys.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The swollen glandular cells exhibited intense eosinophilic granulation, characteristic of that which pathologists now term an **oncocyte**." },
      { author: "Siddhartha Mukherjee", work: "The Song of the Cell", quote: "Under the electron microscope, the cytoplasm of an **oncocyte** is filled almost entirely with packed, abnormal mitochondria." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "The pathologist noted sheets of uniform **oncocytes** with round nuclei, reassuring the team that the renal mass was benign." }
    ]
  },
  "Dashboard — onco/oncocytoma.md": {
    word: "oncocytoma",
    primary: "A benign tumor composed entirely of oncocytes, typically occurring in the kidneys, salivary glands, or thyroid.",
    secondary: "In urologic pathology, a well-circumscribed, mahogany-brown renal cortical tumor featuring a central stellate scar, which mimics renal cell carcinoma on diagnostic imaging.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A benign renal **oncocytoma** may reach huge proportions without invading the renal vein or producing distant metastases." },
      { author: "Atul Gawande", work: "Complications", quote: "The frozen section returned as a benign **oncocytoma**, sparing the young patient from radical nephrectomy." },
      { author: "Sherwin B. Nuland", work: "The Mysteries Within", quote: "Gross inspection of the resected kidney revealed the distinctive central scar of an **oncocytoma**, confirming the radiologist's suspicion." }
    ]
  },
  "Dashboard — onco/oncogenesis.md": {
    word: "oncogenesis",
    primary: "The process of the initiation, development, and progression of tumors and cancer.",
    secondary: "In molecular oncology, the multistep genetic and epigenetic cascade whereby normal cells acquire the biological hallmarks of cancer, driven by oncogene activation and tumor-suppressor gene inactivation.",
    quotes: [
      { author: "Harold Varmus", work: "Nobel Lecture: Retroviruses and Cancer Genes", quote: "Viral **oncogenesis** provided the genetic Rosetta stone that decoded the cellular mechanisms of human cancer." },
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "Multi-hit **oncogenesis** implies that a single mutation rarely suffices; cancer requires a lethal convergence of sequential genomic accidents." },
      { author: "J. Michael Bishop", work: "How to Win the Nobel Prize", quote: "The study of chemical **oncogenesis** revealed that mutagens damage specific regulatory hotspots within cellular proto-oncogenes." }
    ]
  },
  "Dashboard — onco/oncologic.md": {
    word: "oncologic",
    primary: "Relating to or concerned with oncology; pertaining to the study, diagnosis, and treatment of tumors and cancer.",
    secondary: "Describing clinical protocols, staging criteria, and surgical resection margins designed specifically for cancer management.",
    quotes: [
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "The **oncologic** consultation resulted in a multidisciplinary strategy uniting surgical resection with adjuvant chemotherapy." },
      { author: "Atul Gawande", work: "Being Mortal", quote: "The aggressive **oncologic** treatment prolonged life by mere weeks at the terrible cost of debilitating nausea." },
      { author: "Jerome Groopman", work: "The Anatomy of Hope", quote: "Modern **oncologic** imaging with PET-CT detects microscopic metastases before they cause clinical symptoms." }
    ]
  },
  "Dashboard — onco/oncological.md": {
    word: "oncological",
    primary: "Of, relating to, or involving oncology (variant of oncologic).",
    secondary: "Pertaining to the scientific research, clinical trials, and epidemiological methodologies of cancer medicine.",
    quotes: [
      { author: "William Osler", work: "Aequanimitas", quote: "The foundation of a specialized **oncological** institute has concentrated scientific talents upon the mystery of malignant growths." },
      { author: "Siddhartha Mukherjee", work: "The Song of the Cell", quote: "Groundbreaking **oncological** trials with checkpoint inhibitors demonstrated durable remissions in previously incurable melanomas." },
      { author: "Atul Gawande", work: "The Checklist Manifesto", quote: "The **oncological** surgical team verified that clear margins had been achieved before closing the thoracic cavity." }
    ]
  },
  "Dashboard — onco/oncologist.md": {
    word: "oncologist",
    primary: "A medical doctor who specializes in the diagnosis, staging, and treatment of tumors and cancer.",
    secondary: "In modern medicine, subspecialized into medical oncologists (chemotherapy/immunotherapy), surgical oncologists (tumor resection), and radiation oncologists (radiotherapy).",
    quotes: [
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "The medical **oncologist** sits at the bedside of the dying patient, balancing compassionate palliation against the desperate courage of clinical trials." },
      { author: "Jerome Groopman", work: "The Anatomy of Hope", quote: "The **oncologist** leaned forward, explaining with gentle candor that while cure was impossible, remission was achievable." },
      { author: "Atul Gawande", work: "Being Mortal", quote: "When the **oncologist** stops offering further toxic therapies, hospice care can finally begin to restore quality of life." }
    ]
  },
  "Dashboard — onco/oncology.md": {
    word: "oncology",
    primary: "The branch of medicine and scientific research dedicated to the prevention, diagnosis, and treatment of tumors and cancer.",
    secondary: "In modern biomedicine, a rapidly evolving clinical field integrating molecular genetics, immunotherapy, targeted biologics, and precision medicine.",
    quotes: [
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies: A Biography of Cancer", quote: "The history of **oncology** is a chronicle of military campaigns against an internal, shape-shifting enemy that mirrors our own cellular biology." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The emergence of surgical **oncology** established the vital rule of en bloc excision for epithelial neoplasms." },
      { author: "Lewis Thomas", work: "The Medusa and the Snail", quote: "Basic cellular immunology and modern **oncology** are twin sciences converging upon the same fundamental riddle of self-recognition." }
    ]
  },
  "Dashboard — onco/oncoming.md": {
    word: "oncoming",
    primary: "Moving toward someone or something; approaching; nearing in time or space.",
    secondary: "In literary and descriptive usage, portending an impending event, crisis, storm, or seasonal change.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick", quote: "All eyes were fixed upon the **oncoming** breach of the leviathan as he rose foam-crested through the waves." },
      { author: "Charles Dickens", work: "A Tale of Two Cities", quote: "The silent crowd listened with dread to the **oncoming** thunder of revolutionary cannon across Paris." },
      { author: "Jack London", work: "The Call of the Wild", quote: "Buck read in the frosted pine needles the unmistakable herald of the **oncoming** Arctic winter." }
    ]
  },
  "Dashboard — onco/oncorhynchus.md": {
    word: "oncorhynchus",
    primary: "A genus of anadromous fish in the salmon family (Salmonidae), comprising Pacific salmon (such as sockeye, coho, and chinook) and Pacific trout.",
    secondary: "In ichthyology, named from Greek onkos (hooked) and rhynchos (snout), referencing the prominent hooked jaw (kype) that develops in breeding males during their upstream spawning migration.",
    quotes: [
      { author: "John Muir", work: "Travels in Alaska", quote: "Thousands of leaping salmon of the genus **Oncorhynchus** crowded the icy glacial streams, their crimson flanks flashing in the sun." },
      { author: "David Starr Jordan", work: "Fishes", quote: "The species of **Oncorhynchus** ascend the Pacific rivers for thousands of miles, spawn once with heroic devotion, and die upon their gravel redds." },
      { author: "Rachel Carson", work: "Under the Sea-Wind", quote: "Guided by the mysterious olfactory memory of their natal rivers, the **Oncorhynchus** salmon navigated home across vast ocean wastes." }
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
console.log("Medicine & Pathology Batch 3 completed! Total words updated:", Object.keys(wordsData).length);
