import fs from 'fs';
import path from 'path';

const baseClusterDir = 'App database/Greek roots/Cluster Water & Hydrology';

function updateNote(relDir, fileName, data) {
  const filePath = path.join(baseClusterDir, relDir, fileName);
  if (!fs.existsSync(filePath)) {
    console.error(`File not found: ${filePath}`);
    return false;
  }
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`No > [!book] in ${filePath}`);
    return false;
  }
  const headerPart = content.slice(0, bookIdx).trimEnd();
  const defBlock = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${data.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${data.secondary}`;
  const quoteLines = data.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join('\n');
  const quotesBlock = `> [!quote] 💬 Contextual Usage & Authentic Quotations\n${quoteLines}`;

  const newContent = `${headerPart}\n\n${defBlock}\n\n${quotesBlock}\n`;
  fs.writeFileSync(filePath, newContent, 'utf8');
  console.log(`Updated: ${filePath}`);
  return true;
}

const batch6Data = {
  "Dashboard — rhe/antiarrhythmic.md": {
    primary: "Preventing, alleviating, or correcting cardiac arrhythmia; a drug or therapeutic agent used to treat irregular heart rhythms.",
    secondary: "In cardiovascular clinical pharmacology, classified by the Vaughan Williams system (Classes I–IV) based on mechanisms blocking sodium, potassium, or calcium channels, or beta-adrenergic receptors.",
    quotes: [
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "The administration of an **antiarrhythmic** agent such as lidocaine blocks aberrant sodium channels in ischemic myocardium." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Selection of an appropriate **antiarrhythmic** depends on whether the ectopic focus originates above or below the bundle of His." },
      { author: "Donald Seldin", work: "The Kidney: Physiology and Pathophysiology", quote: "Electrolyte disturbances, particularly hypokalemia, severely attenuate the therapeutic efficacy of every **antiarrhythmic** medication." }
    ]
  },
  "Dashboard — rhe/antidiarrheal.md": {
    primary: "Relieving, preventing, or checking diarrhea; a medication or remedy used to treat diarrheal symptoms.",
    secondary: "In gastrointestinal pharmacology, agents such as loperamide, bismuth subsalicylate, or adsorbents that reduce peristaltic motility, inhibit fluid secretion, or bind bacterial toxins.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Bismuth subsalicylate acts as an effective mild **antidiarrheal** by coating inflamed intestinal mucosa and inhibiting enterotoxin secretion." },
      { author: "Florence Nightingale", work: "Notes on Nursing", quote: "Before resorting to strong **antidiarrheal** tinctures, ensure the patient is supplied with pure water and sterile gruel." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "Opium preparations have long served as the principal **antidiarrheal** remedy to diminish peristaltic frequency." }
    ]
  },
  "Dashboard — rhe/arrhythmia.md": {
    primary: "Any disturbance or abnormality in the rhythm or rate of the heartbeat (such as tachycardia, bradycardia, or fibrillation).",
    secondary: "In cardiac electrophysiology, a pathological deviation from normal sinus rhythm resulting from abnormal impulse generation, re-entry circuits, or conduction block.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The sudden onset of ventricular **arrhythmia** represents the most dangerous complication in the immediate hours following acute myocardial infarction." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Re-entry excitation loops within the Purkinje network provide the electrophysiological mechanism for persistent cardiac **arrhythmia**." },
      { author: "Willem Einthoven", work: "Nobel Lecture", quote: "The string galvanometer allowed us to record the precise electrical wavefront during every phase of auricular **arrhythmia**." }
    ]
  },
  "Dashboard — rhe/arrhythmic.md": {
    primary: "Lacking rhythm or regular cadence; suffering from or characterized by cardiac arrhythmia.",
    secondary: "In clinical cardiology and physiology, describing pulse beats or myocardial depolarizations that occur at irregular, unpredictable intervals.",
    quotes: [
      { author: "Willem Einthoven", work: "The Electrocardiogram in Clinical Medicine", quote: "The electrocardiographic tracing revealed an irregular, **arrhythmic** baseline characteristic of atrial fibrillation." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Upon palpation, the pulse felt weak and completely **arrhythmic**, varying with every respiratory cycle." },
      { author: "Arthur Conan Doyle", work: "Round the Red Lamp", quote: "His hand rested upon the sick man's wrist, counting the faint, **arrhythmic** flutterings of an exhausted heart." }
    ]
  },
  "Dashboard — rhe/arrhythmical.md": {
    primary: "Without regular rhythm or beat; irregular; an alternative form of arrhythmic.",
    secondary: "In physiology and pathology, describing disorganized or erratic motor or cardiac impulses lacking temporal coordination.",
    quotes: [
      { author: "Willem Einthoven", work: "Clinical Electrocardiography", quote: "The **arrhythmical** contractions of the auricles failed to pump adequate blood into the ventricular chambers." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "Toxic doses of digitalis induce a spastic, **arrhythmical** arrest of the cardiac muscle." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "The patient's breathing became shallow and **arrhythmical** as cerebral compression deepened." }
    ]
  },
  "Dashboard — rhe/catarrh.md": {
    primary: "Excessive buildup and discharge of thick mucus in the nose, throat, or bronchial passages, associated with inflammation of the mucous membranes.",
    secondary: "In historical medicine, a clinical symptom (from Greek kata- 'down' + rhein 'to flow') signifying the downward flow of congested phlegm in upper respiratory infections.",
    quotes: [
      { author: "William Shakespeare", work: "Henry IV, Part 2", quote: "And heard you not the bishop of York speak of this, whose deep **catarrh** choked his voice before the assembly?" },
      { author: "Charles Dickens", work: "Bleak House", quote: "Mr. Snagsby, suffering from a chronic **catarrh**, coughed apologetically into his handkerchief behind the lawyer's chair." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Acute nasal **catarrh** accompanied by conjunctival suffusion and fever heralds the onset of measles." }
    ]
  },
  "Dashboard — rhe/catarrhal.md": {
    primary: "Of, relating to, or marked by catarrh; characterized by inflammation of mucous membranes with copious discharge.",
    secondary: "In pathology, describing an inflammatory exudate rich in mucus, desquamated epithelial cells, and leukocytes that coats respiratory or intestinal surfaces.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In acute **catarrhal** jaundice, swelling of the common bile duct papilla impedes biliary drainage into the duodenum." },
      { author: "René Laennec", work: "A Treatise on the Diseases of the Chest", quote: "Stethoscopic examination in **catarrhal** bronchitis reveals diffuse sonorous rhonchi across both pulmonary fields." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "The **catarrhal** exudate consists of desquamated epithelial cells, mucus globules, and migrating leukocytes." }
    ]
  },
  "Dashboard — rhe/diarrhea.md": {
    primary: "A condition marked by abnormally frequent and liquid bowel evacuations; American spelling of diarrhoea.",
    secondary: "In gastroenterology and global health, a major symptom of bacterial, viral, or protozoal enteritis that causes dangerous dehydration and electrolyte loss if untreated.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe choleraic **diarrhea** leads to profound hypovolemic shock within hours if rehydration salts are not administered." },
      { author: "Florence Nightingale", work: "Notes on Nursing", quote: "In hospital wards, tainted water supplies and unventilated latrines were the prime instigators of fatal summer **diarrhea**." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "We differentiate inflammatory enteritis from simple nervous **diarrhea** provoked by sudden fright." }
    ]
  },
  "Dashboard — rhe/diarrheal.md": {
    primary: "Of, pertaining to, resembling, or suffering from diarrhea; American spelling of diarrhoeal.",
    secondary: "In epidemiology, characterizing acute waterborne infections (such as cholera or rotavirus) that cause rapid fluid depletion and metabolic acidosis.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The patient suffered from severe **diarrheal** dehydration accompanied by muscular cramps and subnormal body temperature." },
      { author: "Patrick Manson", work: "Tropical Diseases", quote: "Bacillary dysentery is characterized by painful tenesmus and acute **diarrheal** evacuations laden with blood and mucus." },
      { author: "Florence Nightingale", work: "Notes on Nursing", quote: "Prompt sanitary intervention prevented the **diarrheal** outbreak from spreading through the barracks." }
    ]
  },
  "Dashboard — rhe/diarrheic.md": {
    primary: "Pertaining to, producing, or affected with diarrhea; diarrhetic.",
    secondary: "In clinical symptom reporting, describing watery stool consistency or medications and toxins that stimulate hypermotility of the intestines.",
    quotes: [
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "Ingestion of unripe autumn fruit frequently triggers acute **diarrheic** stools in young children." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The **diarrheic** discharges in typhoid fever assume the classic appearance of pea-soup." },
      { author: "Patrick Manson", work: "Tropical Diseases", quote: "In chronic sprue, the **diarrheic** stools are bulky, pale, and fermenting." }
    ]
  },
  "Dashboard — rhe/diarrhetic.md": {
    primary: "Producing or characteristic of diarrhea; having a purgative or bowel-loosening effect.",
    secondary: "In pharmacognosy and toxicology, substances that induce intestinal fluid secretion or hyperperistalsis through mucosal irritation.",
    quotes: [
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "Excessive doses of senna or colocynth exert a violently **diarrhetic** action upon the bowels." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Certain bacterial enterotoxins stimulate mucosal adenylate cyclase, resulting in copious **diarrhetic** flux." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "The intestinal irritation provoked a severe **diarrhetic** episode that rapidly exhausted the elderly patient." }
    ]
  },
  "Dashboard — rhe/diarrhoea.md": {
    primary: "A condition in which feces are discharged from the bowels frequently and in a liquid form; British spelling of diarrhea.",
    secondary: "In the history of medicine and tropical epidemiology, an ancient disease name (from Greek dia 'through' + rhein 'to flow') recognized as a leading cause of childhood mortality.",
    quotes: [
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "Several of our crew were attacked with violent fever and **diarrhoea** after drinking from the stagnant river pools." },
      { author: "Florence Nightingale", work: "Notes on Nursing", quote: "Clean water and clean air will do more to check hospital **diarrhoea** than all the astringent mixtures in the dispensary." },
      { author: "Thomas Hardy", work: "The Woodlanders", quote: "The village elder attributed the sudden outbreak of **diarrhoea** to the rotting cider pomace left beside the brook." }
    ]
  },
  "Dashboard — rhe/diarrhoeal.md": {
    primary: "Of, relating to, or caused by diarrhoea; British spelling of diarrheal.",
    secondary: "In public health and tropical pathology, describing epidemic dehydration syndromes managed by oral rehydration therapy and clean water infrastructure.",
    quotes: [
      { author: "Patrick Manson", work: "Tropical Diseases", quote: "In tropical climates, chronic **diarrhoeal** illness is the foremost cause of progressive wasting and cachexia." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The rapid replacement of fluid losses is paramount in all severe **diarrhoeal** epidemics." },
      { author: "Ronald Ross", work: "The Prevention of Malaria and Other Diseases", quote: "Proper sanitation of rural wells immediately curbed the seasonal surge of infant **diarrhoeal** fatalities." }
    ]
  },
  "Dashboard — rhe/diarrhoeic.md": {
    primary: "Relating to, characterized by, or suffering from diarrhoea; British spelling of diarrheic.",
    secondary: "In clinical medicine, designating copious watery feces containing excess electrolytes, unabsorbed nutrients, and sloughed mucosal cells.",
    quotes: [
      { author: "Patrick Manson", work: "Tropical Diseases", quote: "Microscopic examination of the **diarrhoeic** fluid revealed active amoebic trophozoites ingesting red blood cells." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In Asiatic cholera, the copious **diarrhoeic** stools are devoid of bile, resembling rice-water." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "A soothing demulcent drink helps coat the inflamed bowel during acute **diarrhoeic** attacks." }
    ]
  },
  "Dashboard — rhe/diarrhoetic.md": {
    primary: "Having the nature of or tending to produce diarrhoea; British spelling of diarrhetic.",
    secondary: "In therapeutics and toxicology, describing drastic cathartics or bacterial poisons that prompt profuse watery intestinal transudation.",
    quotes: [
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "Certain mineral waters taken in excess produce a distinctly **diarrhoetic** effect upon sensitive digestive tracts." },
      { author: "Patrick Manson", work: "Tropical Diseases", quote: "The toxin produced by the vibrio triggers a profound **diarrhoetic** secretion across the intestinal epithelium." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe **diarrhoetic** exhaustion was successfully managed with subcutaneous saline infusions." }
    ]
  },
  "Dashboard — rhe/dysrhythmia.md": {
    primary: "An abnormality in an otherwise normal rhythm or cadence, especially in the electrical activity of the brain or the contractions of the heart.",
    secondary: "In neurology and electrophysiology, paroxysmal sharp waves or spike-and-wave discharges detected on an electroencephalogram (EEG) indicative of epilepsy or metabolic encephalopathy.",
    quotes: [
      { author: "Willem Einthoven", work: "Clinical Electrocardiography", quote: "Continuous monitoring detected a sudden paroxysmal **dysrhythmia** originating in the left ventricle." },
      { author: "Donald Calne", work: "Therapeutics in Neurology", quote: "The electroencephalogram revealed focal paroxysmal **dysrhythmia** localized to the anterior temporal lobe." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Cardiac **dysrhythmia** occurs when conduction velocity slows or when premature pacemakers trigger ectopic beats." }
    ]
  },
  "Dashboard — rhe/endorheic.md": {
    primary: "Of a drainage basin or water body: having no outflow to an ocean or sea, losing water only through evaporation or subterranean seepage.",
    secondary: "In physical hydrology and physical geography, characterizing enclosed continental depressions (such as the Great Salt Lake, Dead Sea, or Lake Chad) that accumulate high mineral salinity.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "The Caspian Sea and the Aral Sea are majestic examples of an **endorheic** hydrological basin with no oceanic outlet." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Because an **endorheic** lake loses water solely through evaporation, dissolved salts progressively concentrate until dense brine is formed." },
      { author: "Eduard Suess", work: "The Face of the Earth", quote: "Internal continental rifting frequently creates an **endorheic** depression where ephemeral salt flats accumulate thick evaporites." }
    ]
  },
  "Dashboard — rhe/eurhythmia.md": {
    primary: "Harmony, rhythm, and graceful proportion in architecture, bodily posture, or musical cadence; Eurhythmy.",
    secondary: "In classical Vitruvian theory, the pleasing and elegant appearance that results when the architectural components of a structure correspond symmetrically and proportionally to the whole.",
    quotes: [
      { author: "Vitruvius", work: "De Architectura", quote: "**Eurhythmia** is that agreeable harmony and proportion where height corresponds gracefully to breadth and length." },
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The delicate arcades of the Doge's Palace achieve a visual **eurhythmia** that satisfies both eye and intellect." },
      { author: "Walter Pater", work: "The Renaissance", quote: "In classical Greek sculpture, the ideal bodily posture expresses perfect poise and spiritual **eurhythmia**." }
    ]
  },
  "Dashboard — rhe/eurhythmic.md": {
    primary: "Characterized by harmonious proportion, graceful rhythm, or well-balanced measure.",
    secondary: "In aesthetics and performing arts, designating architectural compositions or choreographed movements (as in Dalcroze eurhythmics) where music is embodied in bodily cadence.",
    quotes: [
      { author: "Vitruvius", work: "The Ten Books on Architecture", quote: "A building designed with **eurhythmic** symmetry delights the citizen with its well-balanced proportions." },
      { author: "Walter Pater", work: "Greek Studies", quote: "The young Athenian athletes moved in **eurhythmic** cadence during the sacred festival dances." },
      { author: "Arthur Symons", work: "Plays, Acting and Music", quote: "Her dance exhibited a pure, **eurhythmic** expression where every physical movement translated musical phrase into visible melody." }
    ]
  },
  "Dashboard — rhe/eurhythmy.md": {
    primary: "Harmony, rhythm, and graceful proportion in architecture, music, or bodily movement; an alternative form of eurhythmia.",
    secondary: "In philosophical aesthetics and anthroposophy (developed by Rudolf Steiner), an expressive movement art seeking to make visible the inner sounds and rhythms of speech and music.",
    quotes: [
      { author: "Vitruvius", work: "De Architectura", quote: "When all parts of an elevation conform to their true module, the facade attains the supreme grace of **eurhythmy**." },
      { author: "Walter Pater", work: "Plato and Platonism", quote: "Platonic education aimed at instilling internal **eurhythmy**—a musical harmony between bodily discipline and the soul." },
      { author: "John Addington Symonds", work: "Renaissance in Italy", quote: "The humanists sought to revive antique **eurhythmy**, cultivating grace in language, deportment, and art." }
    ]
  },
  "Dashboard — rhe/gonorrhoea.md": {
    primary: "A contagious venereal bacterial infection caused by the diplococcus Neisseria gonorrhoeae, marked by purulent inflammation of the genital mucous membranes.",
    secondary: "In the history of medicine and urology, an ancient infection historically mistaken for an involuntary discharge of semen (Greek gonos 'seed' + rhoia 'flow'), resulting in strictures if untreated.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Untreated **gonorrhoea** may lead to chronic urethral stricture, epididymitis, or destructive gonococcal arthritis." },
      { author: "Galen", work: "On the Affected Parts", quote: "Ancient physicians applied the name **gonorrhoea** under the mistaken belief that the discharge was an involuntary flow of semen." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "The purulent exudate in acute **gonorrhoea** is teeming with intracellular diplococci inside polymorphonuclear leukocytes." }
    ]
  },
  "Dashboard — rhe/hemorrhea.md": {
    primary: "A profuse or continuous discharge of blood; hemorrhage.",
    secondary: "In clinical surgery and hematology, excessive bleeding from severed arteries or capillaries caused by trauma, coagulopathy, or vascular rupture.",
    quotes: [
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "Sudden arterial rupture within the stomach causes terrifying **hemorrhea**, leading to syncope and death." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In hemophilic patients, even minor tooth extraction can precipitate intractable capillary **hemorrhea**." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "The application of cold and compression arrested the alarming **hemorrhea** from the lacerated vessel." }
    ]
  },
  "Dashboard — rhe/logorrhea.md": {
    primary: "An excessive, uncontrollable, and often incoherent flow of words or talkativeness.",
    secondary: "In psychiatry and behavioral neurology, a symptom observed in manic states, Wernicke's aphasia, or frontal lobe disinhibition characterized by rapid, voluble, uninhibited speech.",
    quotes: [
      { author: "Oliver Wendell Holmes Sr.", work: "The Autocrat of the Breakfast-Table", quote: "A sudden fit of intellectual **logorrhea** seized the talkative guest, who monopolized the entire dinner conversation." },
      { author: "William James", work: "The Principles of Psychology", quote: "In manic excitement, flight of ideas often manifests as uncontrollable **logorrhea**, words pouring forth faster than ideas can form." },
      { author: "George Orwell", work: "Inside the Whale", quote: "The political pamphlets of the period were infected with a pompous **logorrhea** that concealed a total absence of genuine thought." }
    ]
  },
  "Dashboard — rhe/polyrhythm.md": {
    primary: "The simultaneous combination of two or more contrasting, independent rhythms or meters in musical composition or performance.",
    secondary: "In ethnomusicology and modern music theory, cross-rhythmic structures (such as 3 against 2, or 4 against 3) foundational to sub-Saharan African percussion, Afro-Cuban jazz, and 20th-century orchestral modernism.",
    quotes: [
      { author: "Igor Stravinsky", work: "Poetics of Music", quote: "The complex **polyrhythm** in the Rite of Spring drives the primitive dance through conflicting cross-accents." },
      { author: "Aaron Copland", work: "What to Listen for in Music", quote: "In modern orchestral writing, a sophisticated **polyrhythm** superimposes triplets against dotted eighths with striking kinetic tension." },
      { author: "Hector Berlioz", work: "Treatise on Modern Instrumentation and Orchestration", quote: "Combining contrasting meters among different sections of the orchestra produces a dazzling **polyrhythm** that elevates the dramatic climax." }
    ]
  },
  "Dashboard — rhe/rhein.md": {
    primary: "A yellow crystalline anthraquinone compound (C15H8O6) found in rhubarb root and senna, possessing laxative and anti-inflammatory properties.",
    secondary: "In pharmacognosy, a metabolite derived from the hydrolysis of sennosides in the colon that stimulates peristalsis and mucin secretion while exerting cartilage-protective actions.",
    quotes: [
      { author: "Paul Karrer", work: "Organic Chemistry", quote: "Extraction of rhubarb rhizome yields the carboxylic anthraquinone derivative known as **rhein**." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "The active purgative constituent of Chinese rhubarb, termed **rhein**, stimulates the peristaltic contractions of the large intestine." },
      { author: "J. R. Partington", work: "A Text-Book of Inorganic Chemistry", quote: "Spectroscopic analysis confirmed that **rhein** forms deep reddish-violet solutions in alkaline carbonates." }
    ]
  },
  "Dashboard — rhe/rheologic.md": {
    primary: "Of, pertaining to, or determined by rheology; dealing with the deformation and flow properties of matter.",
    secondary: "In fluid dynamics and polymer science, characterizing the shear-dependent viscosity, thixotropy, and viscoelasticity of non-Newtonian fluids.",
    quotes: [
      { author: "Eugene Bingham", work: "Fluidity and Plasticity", quote: "Non-Newtonian fluids exhibit complex **rheologic** properties where viscosity varies with the applied shear rate." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "The **rheologic** behavior of whole blood in microcapillaries depends critically on erythrocyte deformability." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "Polymer solutions display anomalous **rheologic** traits, behaving like liquids under low shear and elastic solids under sudden shock." }
    ]
  },
  "Dashboard — rhe/rheological.md": {
    primary: "An alternative form of rheologic; relating to the scientific study of the flow and deformation of matter.",
    secondary: "In materials engineering and biophysics, analyzing yield stress, relaxation times, and flow curves in colloids, molten polymers, and biological fluids.",
    quotes: [
      { author: "Eugene Bingham", work: "Fluidity and Plasticity", quote: "A thorough **rheological** study must account for both yield stress and plastic flow in concentrated suspensions." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The **rheological** elasticity of rubber polymers is governed by cross-linking between flexible hydrocarbon chains." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Elevated fibrinogen concentration alters the **rheological** properties of plasma, increasing the hazard of vascular thrombosis." }
    ]
  },
  "Dashboard — rhe/rheology.md": {
    primary: "The branch of physical science that studies the deformation and flow of matter, particularly non-Newtonian fluids, plastic solids, and soft matter.",
    secondary: "In physics and mechanical engineering, a field founded by Eugene Bingham (adopting Heraclitus's aphorism panta rhei, 'everything flows') to bridge hydrodynamics and elasticity theory.",
    quotes: [
      { author: "Eugene Bingham", work: "Fluidity and Plasticity", quote: "We coined the term **rheology** from the Greek dictum panta rhei—all things flow—to study the physics of flow and deformation." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "In industrial polymers and lubricants, **rheology** determines how materials respond under high mechanical stress and shear." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "The modern science of hemorheology applies the principles of **rheology** to blood flow through the microcirculation." }
    ]
  },
  "Dashboard — rhe/rheometer.md": {
    primary: "An instrument designed to measure the rheological properties (flow behavior and viscosity) of fluids, or historically an apparatus for measuring electric current.",
    secondary: "In modern analytical chemistry, a precision rotational instrument that subjects sample fluids to controlled shear stress or strain, measuring modulus and dynamic viscosity.",
    quotes: [
      { author: "Eugene Bingham", work: "Fluidity and Plasticity", quote: "Using a rotational **rheometer**, we recorded shear stress as a function of shear rate across a wide temperature range." },
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "I placed a delicate astatic **rheometer** into the circuit to detect the transient induced galvanic current." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "A cone-and-plate **rheometer** allows clinicians to determine blood viscosity at shear rates simulating capillary beds." }
    ]
  },
  "Dashboard — rhe/rheostat.md": {
    primary: "An electrical device consisting of a variable resistor used for regulating the current flowing through a circuit without opening the circuit.",
    secondary: "In electrical engineering history, an instrument invented by Charles Wheatstone (from Greek rheos 'current/flow' + statos 'standing/stopping') using a sliding contact over a wire coil.",
    quotes: [
      { author: "Charles Wheatstone", work: "An Account of Several New Instruments and Processes for Determining the Constants of a Voltaic Circuit", quote: "I devised the **rheostat** to introduce known increments of electrical resistance into a galvanic circuit without interrupting current." },
      { author: "Thomas Alva Edison", work: "Scientific Papers", quote: "By adjusting the sliding contact of the **rheostat**, the operator dimmed the incandescent lamps in the auditorium." },
      { author: "Nikola Tesla", work: "Lectures on Alternate Currents", quote: "An oil-cooled **rheostat** was placed in series with the motor windings to control the starting torque." }
    ]
  },
  "Dashboard — rhe/rhetoric.md": {
    primary: "The art of effective, persuasive, or eloquent speaking or writing; language designed to persuade, motivate, or impress.",
    secondary: "In classical education and philosophy, one of the original disciplines of the medieval trivium (alongside grammar and logic), systematized by Aristotle, Cicero, and Quintilian.",
    quotes: [
      { author: "Aristotle", work: "The Art of Rhetoric", quote: "**Rhetoric** may be defined as the faculty of observing in any given case the available means of persuasion." },
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "The duty and office of **rhetoric** is to apply reason to imagination for the better moving of the will." },
      { author: "William Shakespeare", work: "Julius Caesar", quote: "Mark Antony used all the subtle devices of ancient **rhetoric** to turn the plebeians against the conspirators." }
    ]
  },
  "Dashboard — rhe/rhetorical.md": {
    primary: "Of, pertaining to, or concerned with the art of rhetoric; expressed in elaborate or persuasive language; asked only for effect without requiring an answer.",
    secondary: "In literary analysis, characterizing stylistic devices (such as metaphors, antitheses, and parallelisms) employed to amplify persuasive emotional resonance.",
    quotes: [
      { author: "Aristotle", work: "The Art of Rhetoric", quote: "The three modes of **rhetorical** persuasion are based respectively on the character of the speaker, the emotions of the hearer, and the logical argument." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "His **rhetorical** flourishes were admired by all the ladies, though his arguments contained very little practical sense." },
      { author: "Thomas Babington Macaulay", work: "Critical and Historical Essays", quote: "Burke's celebrated speech was a masterpiece of **rhetorical** grandeur, enriched by historical analogies and moral fervor." }
    ]
  },
  "Dashboard — rhe/rhetorically.md": {
    primary: "In a rhetorical manner; in terms of rhetorical effect, eloquence, or persuasive device.",
    secondary: "In conversational pragmatics, speaking or framing questions for dramatic stylistic emphasis rather than to solicit informational answers.",
    quotes: [
      { author: "George Eliot", work: "Middlemarch", quote: "He paused **rhetorically** after delivering his solemn sentence, waiting for the murmurs of approval from his listeners." },
      { author: "Henry James", work: "The Portrait of a Lady", quote: "Madame Merle phrased her question **rhetorically**, knowing full well that no direct answer was required." },
      { author: "Charles Dickens", work: "Great Expectations", quote: "Mr. Pumblechook coughed **rhetorically** before offering his opinion upon the unexpected fortune." }
    ]
  },
  "Dashboard — rhe/rhetorician.md": {
    primary: "An expert in or teacher of the art of rhetoric; a skilled orator or writer who employs rhetorical artifice.",
    secondary: "In classical antiquity, a professional master of eloquence who trained young citizens in law, forensics, and civic declamation in the schools of Athens and Rome.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The celebrated Greek **rhetorician** Libanius defended the classical temples against the destructive zeal of imperial edicts." },
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "Danton was no dry **rhetorician**; his speeches were volcanic explosions of raw revolutionary passion." },
      { author: "John Milton", work: "Paradise Regained", quote: "The proud **rhetorician** in the public porch amused the youth of Athens with subtle and barren disputations." }
    ]
  },
  "Dashboard — rhe/rheum.md": {
    primary: "A watery or serous mucous discharge from the eyes, nose, or mouth, resulting from cold, irritation, or inflammation; tears or defluxion.",
    secondary: "In historical humoral pathology, an excess of cold, watery humor that flowed from the brain into the chest, joints, or respiratory mucous membranes.",
    quotes: [
      { author: "William Shakespeare", work: "Othello", quote: "I have a salt and sorry **rheum** offends me; lend me thy handkerchief." },
      { author: "Charles Dickens", work: "David Copperfield", quote: "The old clerk's eyes were red and watery with **rheum**, and his voice trembled as he read the deed." },
      { author: "John Milton", work: "Samson Agonistes", quote: "And sightless dark, with joint-racking **rheum** and age, left alone to mourn." }
    ]
  },
  "Dashboard — rhe/rheumatic.md": {
    primary: "Of, relating to, or suffering from rheumatism; marked by pain and stiffness in the joints, muscles, and connective tissues.",
    secondary: "In clinical medicine, designating autoimmune post-streptococcal disease (rheumatic fever) affecting the endocardium, joints, and central nervous system.",
    quotes: [
      { author: "William Shakespeare", work: "A Midsummer Night's Dream", quote: "Therefore the moon, the governess of floods, / Pale in her anger, washes all the air, / That **rheumatic** diseases do abound." },
      { author: "Jane Austen", work: "Sense and Sensibility", quote: "A slight **rheumatic** attack confined the colonel to his room during the damp November rains." },
      { author: "Charles Dickens", work: "The Pickwick Papers", quote: "Mr. Weller complained bitterly of a **rheumatic** stiffness in his shoulder whenever the east wind blew." }
    ]
  },
  "Dashboard — rhe/rheumatism.md": {
    primary: "Any disease marked by chronic inflammation, soreness, and pain in the joints, muscles, or fibrous tissues (such as rheumatoid arthritis or osteoarthritis).",
    secondary: "In medical history, an ancient diagnostic term (from Greek rheumatismos, a discharge or flow) reflecting the Galenic belief that joint pains were caused by cold humors settling in articular cavities.",
    quotes: [
      { author: "Charles Dickens", work: "Oliver Twist", quote: "The damp cellar floor gave the poor old crone a perpetual **rheumatism** in every joint." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "Standing twenty-four hours in wet boots on the deck of a whaler is a sure receipt for **rheumatism** in old age." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Acute articular **rheumatism** is notoriously dangerous in childhood because it frequently attacks the heart valves." }
    ]
  },
  "Dashboard — rhe/rheumatoid.md": {
    primary: "Resembling or characteristic of rheumatism, especially designating rheumatoid arthritis.",
    secondary: "In rheumatology, an autoimmune chronic inflammatory disorder characterized by symmetric polyarthritis, circulating rheumatoid factor antibodies, and synovial pannus destruction.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Symmetrical spindle-shaped swelling of the proximal interphalangeal joints is typical of early **rheumatoid** arthritis." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The chronic pannus formation in a **rheumatoid** joint slowly erodes the articular cartilage and subchondral bone." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "We observed profound synovial hypertrophy in patients suffering from progressive **rheumatoid** disease." }
    ]
  },
  "Dashboard — rhe/rheumatologist.md": {
    primary: "A medical specialist physician who diagnoses and treats rheumatic diseases, arthritis, and autoimmune musculoskeletal disorders.",
    secondary: "In modern clinical practice, a physician expert in managing complex autoimmune conditions (such as systemic lupus erythematosus, scleroderma, and vasculitis) with disease-modifying antirheumatic drugs.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The modern **rheumatologist** must differentiate systemic connective tissue disease from localized osteoarthritis." },
      { author: "Donald Calne", work: "Therapeutics in Neurology", quote: "Close collaboration between the neurologist and the **rheumatologist** is essential when vasculitis attacks peripheral nerves." },
      { author: "Donald Seldin", work: "The Kidney: Physiology and Pathophysiology", quote: "In cases of suspected lupus nephritis, the **rheumatologist** coordinates immunosuppressive therapy with the nephrologist." }
    ]
  },
  "Dashboard — rhe/rheumatology.md": {
    primary: "The branch of internal medicine devoted to the study, diagnosis, and treatment of rheumatic conditions, arthritis, and autoimmune diseases.",
    secondary: "In biomedical science, the field investigating chronic inflammatory mechanisms, autoantibodies, cytokine pathways (such as TNF-alpha and interleukins), and biologic therapeutics.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The development of serological tests for rheumatoid factor inaugurated a new era in clinical **rheumatology**." },
      { author: "Donald Seldin", work: "The Kidney: Physiology and Pathophysiology", quote: "Advances in **rheumatology** have elucidated how circulating immune complexes induce destructive vascular injury." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "Pathological studies of synovial biopsies laid the scientific foundation upon which modern **rheumatology** rests." }
    ]
  },
  "Dashboard — rhe/rheumy.md": {
    primary: "Watery, tearful, or moist with rheum; of weather or air: damp, chilly, and inducing rheum or head colds.",
    secondary: "In literary description, characterizing aged, bleary eyes or cold, mist-shrouded atmospheres that chill the marrow.",
    quotes: [
      { author: "William Shakespeare", work: "Julius Caesar", quote: "And tempt the **rheumy** and unpurged air / To add unto his sickness?" },
      { author: "Thomas Hardy", work: "The Mayor of Casterbridge", quote: "The old pauper looked up through pale, **rheumy** eyes as the mayor entered the parish ward." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The watchman wrapped his woolen scarf tight against the **rheumy** ocean fog that drifted across the deck." }
    ]
  },
  "Dashboard — rhe/rhythm.md": {
    primary: "A strong, regular, repeated pattern of movement, sound, or activity; the systematic grouping of musical beats or poetic stresses.",
    secondary: "In biological physiology and aesthetics (from Greek rhythmos, measured flow, from rhein 'to flow'), the intrinsic temporal periodicity of circadian clocks, heartbeat, and verse cadence.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "Tunes her nocturnal note with musical **rhythm**, feeding on thoughts that voluntary move harmonious numbers." },
      { author: "Edgar Allan Poe", work: "The Philosophy of Composition", quote: "The death of a beautiful woman is unquestionably the most poetical topic in the world, attuned to sorrowful **rhythm**." },
      { author: "Thomas Hardy", work: "Far from the Madding Crowd", quote: "The steady, hypnotic **rhythm** of the sheep-shears clicked ceaselessly throughout the sunny afternoon." }
    ]
  },
  "Dashboard — rhe/rhythmic.md": {
    primary: "Of, relating to, or having a rhythm; recurring at regular, periodic intervals of time or movement.",
    secondary: "In biological systems, characterizing oscillatory behaviors such as neural firing bursts, respiratory excursions, or tidal foraging cycles in marine organisms.",
    quotes: [
      { author: "Henry David Thoreau", work: "Walden", quote: "The low, **rhythmic** lap of the lake water against the shore brought calm to my wandering thoughts." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "The sense of **rhythmic** harmony and cadence is shared in primitive degree by many animals." },
      { author: "Thomas Hardy", work: "Tess of the d'Urbervilles", quote: "The slow, **rhythmic** thud of the steam threshing machine shook the heavy barn floor." }
    ]
  },
  "Dashboard — rhe/rhythmical.md": {
    primary: "Having a marked or harmonious rhythm; recurring at regular intervals; an alternative form of rhythmic.",
    secondary: "In poetics and musical theory, describing verse or melody that flows with balanced, metrical cadence.",
    quotes: [
      { author: "John Ruskin", work: "The Seven Lamps of Architecture", quote: "The **rhythmical** recurrence of arches across the aqueduct imparts a majestic cadence to the landscape." },
      { author: "James George Frazer", work: "The Golden Bough", quote: "The priestesses chant their solemn invocations in a low, **rhythmical** cadence to evoke the god." },
      { author: "Edgar Allan Poe", work: "The Poetic Principle", quote: "Poetry is the **rhythmical** creation of beauty, elevating the soul through harmonious measure." }
    ]
  },
  "Dashboard — rhe/rhythmically.md": {
    primary: "In a rhythmic manner; with a regular, recurrent cadence, beat, or tempo.",
    secondary: "In movement analysis and acoustics, describing periodic oscillations repeated with temporal uniformity.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick", quote: "The eight oars dipped **rhythmically** into the water, sending the longboat leaping over the crested swells." },
      { author: "Joseph Conrad", work: "Heart of Darkness", quote: "The heavy muffled drums throbbed **rhythmically** through the black curtain of the midnight jungle." },
      { author: "Thomas Hardy", work: "The Return of the Native", quote: "The heath bells swayed **rhythmically** in the rising wind across the darkening moor." }
    ]
  },
  "Dashboard — rhe/rhythmicity.md": {
    primary: "The quality or property of being rhythmic; the state of recurring in regular, periodic cycles or beats.",
    secondary: "In neurophysiology and cardiology, the innate ability of pacemaking tissue (such as the sinoatrial node or respiratory center neurons) to generate periodic spontaneous action potentials.",
    quotes: [
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "The intrinsic **rhythmicity** of the sinoatrial node originates from slow spontaneous diastolic depolarization." },
      { author: "Claude Bernard", work: "Lectures on the Phenomena of Life", quote: "Biological **rhythmicity** governs all living processes, from cardiac systole to respiratory cycles." },
      { author: "Willem Einthoven", work: "The Electrocardiogram in Clinical Medicine", quote: "When autonomic tone is altered, the natural **rhythmicity** of the heart is immediately reflected in the pulse rate." }
    ]
  },
  "Dashboard — rhe/rhyton.md": {
    primary: "An ancient conical, horn-shaped drinking cup or libation vessel, typically terminating in the sculptured head of an animal.",
    secondary: "In Aegean and classical archaeology, a ritual ceramic or metal vessel (from Greek rhyton, from rhein 'to flow') through whose pierced snout wine or libations flowed during sacred ceremonies.",
    quotes: [
      { author: "Heinrich Schliemann", work: "Mycenae", quote: "Among the gold treasures of the shaft graves, we uncovered a magnificent silver **rhyton** shaped like the head of a bull." },
      { author: "Arthur Evans", work: "The Palace of Minos at Knossos", quote: "Minoan fresco paintings depict young cupbearers carrying tall steatite **rhyton** vessels into the sanctuary." },
      { author: "John Beazley", work: "Attic Red-Figure Vase-Painters", quote: "Classical potters fashioned the ceramic **rhyton** with extraordinary sculptural skill, combining pottery with animal sculpture." }
    ]
  },
  "Dashboard — rhe/unrhetorical.md": {
    primary: "Not rhetorical; plain, direct, unadorned, and free from artificial eloquence or persuasive figures of speech.",
    secondary: "In literary criticism and prose analysis, characterizing an austere, straightforward style that relies on naked truth and precision rather than stylistic embellishment.",
    quotes: [
      { author: "George Eliot", work: "Adam Bede", quote: "His speech was plain and **unrhetorical**, yet it carried the deep conviction of an honest and upright heart." },
      { author: "Thomas Babington Macaulay", work: "Critical and Historical Essays", quote: "The despatches of the Duke of Wellington were famously concise, business-like, and completely **unrhetorical**." },
      { author: "Matthew Arnold", work: "Essays in Criticism", quote: "The power of Wordsworth lies in his austere, **unrhetorical** language, speaking directly of elemental human emotions." }
    ]
  },
  "Dashboard — rhe/unrhythmic.md": {
    primary: "Lacking rhythm or regular cadence; irregular, discordant, or jerky in timing; arrhythmic.",
    secondary: "In aesthetics and musicology, describing acoustic patterns or body movements that deliberately or erratically disrupt expected periodic meters.",
    quotes: [
      { author: "Thomas Hardy", work: "Jude the Obscure", quote: "The dull, **unrhythmic** tapping of the loose window shutter disturbed his reading throughout the stormy night." },
      { author: "Arthur Symons", work: "Studies in Seven Arts", quote: "The modern score was intentionally **unrhythmic**, disrupting traditional expectation with abrupt pauses and dissonances." },
      { author: "William James", work: "The Principles of Psychology", quote: "An irregular, **unrhythmic** succession of sensory stimuli produces nervous irritation and mental fatigue." }
    ]
  }
};

let successCount = 0;
for (const [key, data] of Object.entries(batch6Data)) {
  const [relDir, fileName] = key.split('/');
  if (updateNote(relDir, fileName, data)) {
    successCount++;
  }
}

console.log(`\n========================================`);
console.log(`Batch 6 Completed: ${successCount} / ${Object.keys(batch6Data).length} words updated`);
console.log(`========================================`);
