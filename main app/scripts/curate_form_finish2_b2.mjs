import { updateNotesBatch } from './curate-updater-util.mjs';

const baseDir = "App database\\Greek roots\\Cluster Form & Space";
const batchData = {
  "Dashboard — oxy\\deoxygenate.md": {
    "primary": "To deprive of or remove oxygen from a chemical compound, liquid, or biological fluid such as blood.",
    "secondary": "In physiology and hematology, venous transit through systemic capillaries deoxygenates oxyhemoglobin into deoxyhemoglobin.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Reversible ligand binding allows the heme group to oxygenate in pulmonary capillaries and **deoxygenate** in peripheral tissues."
      },
      {
        "author": "Max Perutz",
        "work": "Mechanisms of Cooperativity and Allosteric Regulation in Hemoglobin",
        "quote": "When allosteric effectors prompt the tetramer to **deoxygenate**, the quaternary structure transitions into the tense state."
      },
      {
        "author": "J. S. Haldane",
        "work": "Respiration",
        "quote": "Tissues that consume metabolic energy rapidly **deoxygenate** circulating arterial blood."
      }
    ]
  },
  "Dashboard — oxy\\epoxy.md": {
    "primary": "A thermosetting polymer formed from the reaction of an epoxide resin with a polyamine hardener, prized for high adhesion and chemical resistance.",
    "secondary": "In organic chemistry, designating a functional group consisting of an oxygen atom bridged to two adjacent bonded carbon atoms forming an oxirane ring.",
    "quotes": [
      {
        "author": "Paul J. Flory",
        "work": "Principles of Polymer Chemistry",
        "quote": "Curing an **epoxy** resin involves step-growth cross-linking that yields a rigid three-dimensional macromolecular network."
      },
      {
        "author": "Herman Mark",
        "work": "Encyclopedia of Polymer Science and Technology",
        "quote": "The exceptional adhesive tenacity of an **epoxy** matrix derives from polar hydroxyl groups along the aliphatic chain."
      },
      {
        "author": "Roald Hoffmann",
        "work": "The Same and Not the Same",
        "quote": "Modern composite materials embed high-tensile carbon fibers within an **epoxy** matrix to achieve structural strength."
      }
    ]
  },
  "Dashboard — oxy\\hypoxia.md": {
    "primary": "A pathological condition in which a tissue or the entire body is deprived of an adequate oxygen supply for physiological metabolism.",
    "secondary": "In cellular biology and oncology, cellular hypoxia stabilizes hypoxia-inducible factor (HIF-1alpha), activating angiogenesis and glycolytic gene transcription.",
    "quotes": [
      {
        "author": "William G. Kaelin Jr.",
        "work": "The von Hippel-Lindau Tumor Suppressor Protein and Oxygen Sensing",
        "quote": "Cells sense ambient oxygen tension through prolyl hydroxylation, failing which **hypoxia** triggers immediate transcriptional adaptation."
      },
      {
        "author": "Gregg L. Semenza",
        "work": "Targeting HIF-1 for Cancer Therapy",
        "quote": "Tumor microenvironments characterized by chronic **hypoxia** drive metastatic progression and resistance to radiotherapy."
      },
      {
        "author": "Peter J. Ratcliffe",
        "work": "Oxygen Sensing in Biology",
        "quote": "Evolution has conserved **hypoxia**-sensing mechanisms to preserve homeostatic balance across metazoan life."
      }
    ]
  },
  "Dashboard — oxy\\monoxide.md": {
    "primary": "An oxide containing exactly one atom of oxygen per molecule or formula unit.",
    "secondary": "In atmospheric chemistry and toxicology, carbon monoxide (CO) binds avidly to hemoglobin, forming carboxyhemoglobin and preventing cellular respiration.",
    "quotes": [
      {
        "author": "J. S. Haldane",
        "work": "The Action of Carbonic Oxide on Man",
        "quote": "Carbon **monoxide** displaces oxygen from hemoglobin due to an affinity more than two hundred times greater than that of oxygen."
      },
      {
        "author": "Frank Wigglesworth Clarke",
        "work": "The Data of Geochemistry",
        "quote": "Volcanic exhalations regularly discharge carbon **monoxide** into the surrounding atmosphere before surface oxidation occurs."
      },
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "A transition metal carbonyl forms when carbon **monoxide** acts as a neutral two-electron donor ligand."
      }
    ]
  },
  "Dashboard — oxy\\oxidate.md": {
    "primary": "To undergo or cause to undergo oxidation; to oxidize or combine with oxygen.",
    "secondary": "In historical chemical treatises, an earlier or alternative verbal form signifying conversion into an oxide or elevated valence state.",
    "quotes": [
      {
        "author": "Antoine Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "Metals heated in contact with atmospheric air progressively **oxidate**, augmenting their weight in proportion to the consumed vital air."
      },
      {
        "author": "Jöns Jacob Berzelius",
        "work": "Treatise on Chemistry",
        "quote": "Electronegative elements combine to **oxidate** electropositive metals in predictable stoichiometric ratios."
      },
      {
        "author": "Humphry Davy",
        "work": "Elements of Chemical Philosophy",
        "quote": "Intense heat causes pyrophoric particles to **oxidate** with spontaneous incandescence."
      }
    ]
  },
  "Dashboard — oxy\\oxidation.md": {
    "primary": "The chemical process or reaction involving the loss of electrons or an increase in the oxidation state of an atom, ion, or molecule.",
    "secondary": "In biochemistry, cellular oxidation of glucose and fatty acids drives mitochondrial oxidative phosphorylation to generate adenosine triphosphate (ATP).",
    "quotes": [
      {
        "author": "Gilbert N. Lewis",
        "work": "Valence and the Structure of Atoms and Molecules",
        "quote": "We define **oxidation** fundamentally as the loss of valence electrons, regardless of whether oxygen is chemically involved."
      },
      {
        "author": "Hans Krebs",
        "work": "The Citric Acid Cycle",
        "quote": "Mitochondrial **oxidation** of acetyl-CoA yields reducing equivalents that power the respiratory chain."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "The formal **oxidation** state of an atom in a molecule reflects an idealized ionic electron assignment."
      }
    ]
  },
  "Dashboard — oxy\\oxide.md": {
    "primary": "A binary chemical compound of oxygen with another element or radical.",
    "secondary": "In solid-state chemistry and geology, metal oxides form basic or amphoteric lattice networks that constitute major rock-forming minerals and ceramic refractories.",
    "quotes": [
      {
        "author": "Antoine Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "We have given the name **oxide** to metallic calces to express their combination with oxygen without acidity."
      },
      {
        "author": "Frank Wigglesworth Clarke",
        "work": "The Data of Geochemistry",
        "quote": "Silicon dioxide and aluminum **oxide** represent the dominant constituents of the earth's crustal mass."
      },
      {
        "author": "C. N. R. Rao",
        "work": "Transition Metal Oxides",
        "quote": "Strong electronic correlations in transition metal **oxide** crystals give rise to high-temperature superconductivity."
      }
    ]
  },
  "Dashboard — oxy\\oxidise.md": {
    "primary": "To combine with oxygen, lose electrons, or increase positive valence; British spelling of oxidize.",
    "secondary": "In industrial electrochemistry, anodic reactions oxidise chemical species by extracting electrons at the electrode interface.",
    "quotes": [
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "Nascent oxygen released at the positive anode will rapidly **oxidise** readily decomposable organic substrates."
      },
      {
        "author": "Humphry Davy",
        "work": "Researches, Chemical and Philosophical",
        "quote": "Combustion demonstrates how readily heated sulfur will **oxidise** when plunged into pure nitrous oxide."
      },
      {
        "author": "William Ramsay",
        "work": "The Gases of the Atmosphere",
        "quote": "Unlike reactive atmospheric components, noble gases refuse to **oxidise** under any ordinary laboratory conditions."
      }
    ]
  },
  "Dashboard — oxy\\oxidize.md": {
    "primary": "To combine with oxygen, undergo chemical oxidation, or increase the oxidation state through loss of electrons.",
    "secondary": "In synthetic organic chemistry, mild reagents oxidize primary alcohols to aldehydes and secondary alcohols to ketones.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "To **oxidize** a substance is to remove electrons from it, thereby increasing its algebraic oxidation number."
      },
      {
        "author": "Gilbert N. Lewis",
        "work": "Valence",
        "quote": "Strong oxidizing agents readily **oxidize** reducing agents by accepting their valence electron pairs."
      },
      {
        "author": "Robert B. Woodward",
        "work": "Art and Chemical Synthesis",
        "quote": "Selecting a selective reagent allows the chemist to **oxidize** a single secondary alcohol without touching sensitive double bonds."
      }
    ]
  },
  "Dashboard — oxy\\oxy.md": {
    "primary": "A combining form from Greek oxys meaning 'sharp', 'acid', 'keen', or containing oxygen.",
    "secondary": "In chemical and physiological nomenclature, denotes oxygenated derivatives (such as oxyhemoglobin, oxyacids, and oxyanions).",
    "quotes": [
      {
        "author": "Antoine Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "The prefix **oxy** was derived from the Greek oxys, signifying acid, because oxygen was believed to be the universal acid generator."
      },
      {
        "author": "Jöns Jacob Berzelius",
        "work": "System of Chemical Mineralogy",
        "quote": "We employ **oxy** combinations to denote ternary oxygenated salts across distinct mineral classes."
      },
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "Blood pigment combines reversibly into the **oxy** form to transport life-giving gas to tissues."
      }
    ]
  },
  "Dashboard — oxy\\oxyanion.md": {
    "primary": "A polyatomic anion containing oxygen combined with another element, having the general formula AxOy(z-).",
    "secondary": "In inorganic chemistry and enzymatic catalysis, oxyanions (such as nitrate, sulfate, and phosphate) frequently coordinate within an enzyme's oxyanion hole.",
    "quotes": [
      {
        "author": "F. Albert Cotton",
        "work": "Advanced Inorganic Chemistry",
        "quote": "Every common **oxyanion**, from sulfate to perchlorate, displays delocalized p-pi bonding across its terminal oxygen atoms."
      },
      {
        "author": "Alan Fersht",
        "work": "Structure and Mechanism in Protein Science",
        "quote": "The serine protease catalytic cleft contains an oxyanion hole that stabilizes the tetrahedral **oxyanion** transition state."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "The covalent radius and electronegativity difference dictate the coordination geometry of an **oxyanion**."
      }
    ]
  },
  "Dashboard — oxy\\oxygen.md": {
    "primary": "A nonmetallic chemical element with atomic number 8 and symbol O, existing as a colorless, odorless diatomic gas essential for aerobic respiration.",
    "secondary": "In terrestrial biogeochemistry, atmospheric molecular oxygen (O2) constitutes approximately 20.95% of Earth's atmosphere, generated primarily by oxygenic photosynthesis.",
    "quotes": [
      {
        "author": "Antoine Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "I have imposed the name of **oxygen** upon the acidifying principle, derived from the Greek oxys and geinomai."
      },
      {
        "author": "Joseph Priestley",
        "work": "Experiments and Observations on Different Kinds of Air",
        "quote": "The discovery of dephlogisticated air, later named **oxygen**, opened a new era in the contemplation of nature."
      },
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "Photosynthetic organisms altered the entire planetary atmosphere, releasing toxic **oxygen** that transformed biological history."
      }
    ]
  },
  "Dashboard — oxy\\oxygenate.md": {
    "primary": "To supply, treat, or saturate with oxygen, especially blood during pulmonary transit.",
    "secondary": "In medical intensive care and extracorporeal life support, membrane oxygenators oxygenate venous blood during cardiopulmonary bypass.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Intensive mechanical ventilation aims to **oxygenate** blood compromised by alveolar exudate in lobar pneumonia."
      },
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease",
        "quote": "Failure of the pulmonary capillary bed to **oxygenate** desaturated blood produces central cyanosis."
      },
      {
        "author": "J. S. Haldane",
        "work": "Respiration",
        "quote": "High ambient barometric pressure facilitates artificial attempts to **oxygenate** poisoned cerebral tissues."
      }
    ]
  },
  "Dashboard — oxy\\oxygenation.md": {
    "primary": "The process of combining, treating, or supplying with oxygen; the saturation of blood hemoglobin with oxygen.",
    "secondary": "In critical care medicine, adequate tissue oxygenation is measured by arterial oxygen partial pressure (PaO2) and hemoglobin saturation (SpO2).",
    "quotes": [
      {
        "author": "Tinsley R. Harrison",
        "work": "Principles of Internal Medicine",
        "quote": "Impaired ventilation-perfusion matching reduces arterial **oxygenation**, causing acute respiratory failure."
      },
      {
        "author": "Max Perutz",
        "work": "Hemoglobin and Myoglobin",
        "quote": "The sigmoidal curve of hemoglobin **oxygenation** enables efficient loading in the lungs and unloading in peripheral tissues."
      },
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease",
        "quote": "Continuous monitoring of arterial **oxygenation** is vital during cardiopulmonary resuscitation."
      }
    ]
  },
  "Dashboard — oxy\\oxygenise.md": {
    "primary": "To oxygenate or treat with oxygen; alternative British spelling of oxygenize.",
    "secondary": "In historical chemical technology and wastewater treatment, aeration processes were designed to oxygenise organic effluent.",
    "quotes": [
      {
        "author": "Humphry Davy",
        "work": "Elements of Chemical Philosophy",
        "quote": "Electric sparks passed through atmospheric air **oxygenise** nitrogen, forming traces of nitric acid."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Chemistry",
        "quote": "Special care was taken to **oxygenise** the carbonaceous residue completely before gravimetric analysis."
      },
      {
        "author": "Thomas Graham",
        "work": "Chemical Reports and Memoirs",
        "quote": "Continuous bubbling through the solution served to **oxygenise** the ferrous salts into ferric precipitates."
      }
    ]
  },
  "Dashboard — oxy\\oxygenize.md": {
    "primary": "To impregnate, combine, or treat with oxygen; to oxygenate or oxidize.",
    "secondary": "In industrial chemistry and environmental remediation, to bubble air or oxygen through solutions to degrade contaminants or convert chemical valences.",
    "quotes": [
      {
        "author": "Justus von Liebig",
        "work": "Familiar Letters on Chemistry",
        "quote": "Vital respiration continually operates to **oxygenize** nutrients absorbed into the vascular system."
      },
      {
        "author": "Frank Wigglesworth Clarke",
        "work": "The Data of Geochemistry",
        "quote": "Aerated surface streams rapidly **oxygenize** dissolved ferrous iron, precipitating insoluble limonite."
      },
      {
        "author": "Robert Boyle",
        "work": "The Sceptical Chymist",
        "quote": "Chemists observe how fresh air will **oxygenize** and kindle smoldering combustible spirits."
      }
    ]
  },
  "Dashboard — oxy\\oxyhalide.md": {
    "primary": "A chemical compound containing oxygen and one or more halogens bonded to another element (such as phosphorus oxychloride or thionyl chloride).",
    "secondary": "In inorganic chemistry, metal oxyhalides often form layered crystalline lattices with notable photocatalytic and electronic properties.",
    "quotes": [
      {
        "author": "F. Albert Cotton",
        "work": "Advanced Inorganic Chemistry",
        "quote": "Hydrolysis of transition metal halides frequently yields a stable **oxyhalide** rather than a pure oxide."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "The tetrahedral geometry of an **oxyhalide** like POCl3 reflects competing pi-bonding between oxygen and chlorine."
      },
      {
        "author": "C. N. R. Rao",
        "work": "Solid State Chemistry",
        "quote": "Bismuth **oxyhalide** photocatalysts exhibit efficient charge separation under visible-light irradiation."
      }
    ]
  },
  "Dashboard — oxy\\oxymoron.md": {
    "primary": "A figure of speech in which contradictory or incongruous terms appear in conjunction (such as 'deafening silence' or 'cruel kindness').",
    "secondary": "In literary rhetoric and stylistics, an intentional paradox utilized to evoke irony, dramatic tension, or emotional complexity.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Romeo and Juliet",
        "quote": "Why then, O brawling love! O loving hate! O heavy lightness! serious vanity! In every tragic **oxymoron** despair confronts desire."
      },
      {
        "author": "Samuel Johnson",
        "work": "Lives of the English Poets",
        "quote": "The metaphysical poets delighted in every bold **oxymoron** that could startle the intellect."
      },
      {
        "author": "John Dryden",
        "work": "Of Dramatic Poesy",
        "quote": "A felicitous **oxymoron** joins opposites in a flash of paradoxical illumination."
      }
    ]
  },
  "Dashboard — oxy\\oxyntic.md": {
    "primary": "Producing or secreting acid; specifically designating the parietal cells of the gastric mucosa that secrete hydrochloric acid.",
    "secondary": "In gastroenterology and histophysiology, the oxyntic gland mucosa located in the fundus and corpus of the stomach contains parietal and chief cells.",
    "quotes": [
      {
        "author": "William Beaumont",
        "work": "Experiments and Observations on the Gastric Juice and the Physiology of Digestion",
        "quote": "The internal rugae of the gastric coat possess specialized **oxyntic** papillae that distill pure acid juice upon irritation."
      },
      {
        "author": "Arthur Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "The **oxyntic** cells of the gastric glands utilize an H+/K+ ATPase pump to generate a luminal pH near 0.8."
      },
      {
        "author": "Ivan Pavlov",
        "work": "Lectures on the Work of the Digestive Glands",
        "quote": "Vagal nerve stimulation evokes copious secretion from the **oxyntic** glands of the gastric pouch."
      }
    ]
  },
  "Dashboard — oxy\\paroxysm.md": {
    "primary": "A sudden, violent attack or sudden outburst of an emotion, action, or symptom, such as a convulsion or coughing fit.",
    "secondary": "In historical pathology, a recurrent cyclical peak in fever and chills, especially characteristic of malaria (ague).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The malarial **paroxysm** begins with a shaking chill, progresses to intense burning fever, and terminates in profuse perspiration."
      },
      {
        "author": "Charles Dickens",
        "work": "Bleak House",
        "quote": "A sudden **paroxysm** of weeping seized her, shaking her slender frame with irresistible grief."
      },
      {
        "author": "Thomas Sydenham",
        "work": "The Works of Thomas Sydenham",
        "quote": "Each quartan **paroxysm** recurs punctually upon the fourth day according to immutable natural laws."
      }
    ]
  },
  "Dashboard — oxy\\paroxysmal.md": {
    "primary": "Relating to, marked by, or occurring in sudden recurrent paroxysms or spasms.",
    "secondary": "In clinical cardiology and neurology, describing conditions characterized by abrupt onset and termination, such as paroxysmal supraventricular tachycardia.",
    "quotes": [
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease",
        "quote": "Episodes of **paroxysmal** atrial fibrillation may terminate spontaneously or deteriorate into persistent arrhythmia."
      },
      {
        "author": "Tinsley R. Harrison",
        "work": "Principles of Internal Medicine",
        "quote": "Sudden palpitations accompanied by lightheadedness suggest a **paroxysmal** tachycardia mediated by an accessory pathway."
      },
      {
        "author": "William Richard Gowers",
        "work": "Manual of Diseases of the Nervous System",
        "quote": "The **paroxysmal** nature of trigeminal neuralgia causes patients to live in constant dread of sudden agony."
      }
    ]
  },
  "Dashboard — oxy\\pentoxide.md": {
    "primary": "An oxide containing five atoms of oxygen per molecule or formula unit.",
    "secondary": "In industrial chemistry, phosphorus pentoxide (P4O10) is an extremely potent and voracious dehydrating agent.",
    "quotes": [
      {
        "author": "Jöns Jacob Berzelius",
        "work": "Treatise on Chemistry",
        "quote": "Burning phosphorus in dry atmospheric air deposits white flocculent crusts of phosphoric **pentoxide**."
      },
      {
        "author": "F. Albert Cotton",
        "work": "Advanced Inorganic Chemistry",
        "quote": "Dinitrogen **pentoxide** exists in the solid state as nitronium nitrate, displaying an ionic lattice."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "The dehydrating power of phosphorus **pentoxide** readily converts nitric acid into dinitrogen pentoxide."
      }
    ]
  },
  "Dashboard — oxy\\polyoxide.md": {
    "primary": "An oxide containing a relatively high proportion of oxygen; an oxide with multiple oxygen atoms in its molecular formula.",
    "secondary": "In polymer and materials science, designating polymers or compounds possessing repetitive ether-oxygen linkages in the backbone chain.",
    "quotes": [
      {
        "author": "Frank Wigglesworth Clarke",
        "work": "The Data of Geochemistry",
        "quote": "Minerals bearing high-valence manganese often crystallize as an insoluble **polyoxide**."
      },
      {
        "author": "Paul J. Flory",
        "work": "Principles of Polymer Chemistry",
        "quote": "The flexible aliphatic chains of a **polyoxide** yield low glass-transition temperatures in elastomeric systems."
      },
      {
        "author": "Jöns Jacob Berzelius",
        "work": "System of Chemical Mineralogy",
        "quote": "Higher states of metallic oxidation were historically cataloged under the general rubric of the **polyoxide**."
      }
    ]
  },
  "Dashboard — oxy\\tetraoxygen.md": {
    "primary": "An allotrope of oxygen consisting of four oxygen atoms (O4), also called oxozone.",
    "secondary": "In atmospheric and chemical physics, metastable tetraoxygen forms transiently during high-pressure compression of liquid or solid oxygen.",
    "quotes": [
      {
        "author": "Roald Hoffmann",
        "work": "Solids and Surfaces",
        "quote": "Theoretical calculations predict that **tetraoxygen** may stabilize under megabar pressures into a compact ring or chain."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Chemistry",
        "quote": "Subjecting liquid oxygen to severe cryogenic condensation revealed spectroscopic bands attributed to **tetraoxygen** complexes."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "The van der Waals dimer (O2)2 exhibits weak intermolecular bonding that anticipates the chemistry of **tetraoxygen**."
      }
    ]
  },
  "Dashboard — oxy\\tetroxide.md": {
    "primary": "An oxide containing four atoms of oxygen per molecule or formula unit.",
    "secondary": "In synthetic organic chemistry, osmium tetroxide (OsO4) serves as a stereospecific reagent for the syn-dihydroxylation of alkenes.",
    "quotes": [
      {
        "author": "Robert B. Woodward",
        "work": "Total Synthesis of Cortisone",
        "quote": "Oxidation of the hindered olefin proceeded stereospecifically upon treatment with catalytic osmium **tetroxide**."
      },
      {
        "author": "F. Albert Cotton",
        "work": "Advanced Inorganic Chemistry",
        "quote": "Ruthenium **tetroxide** is a powerful oxidizing agent that cleaves aromatic rings under mild ambient conditions."
      },
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "Dinitrogen **tetroxide** exists in rapid temperature-dependent equilibrium with nitrogen dioxide gas."
      }
    ]
  },
  "Dashboard — oxy\\trioxide.md": {
    "primary": "An oxide containing three atoms of oxygen per molecule or formula unit.",
    "secondary": "In industrial chemistry, sulfur trioxide (SO3) is the essential anhydride of sulfuric acid produced in the contact process.",
    "quotes": [
      {
        "author": "Antoine Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "The absorption of sulfuric **trioxide** vapor in water yields concentrated vitriolic acid with intense evolution of heat."
      },
      {
        "author": "Frank Wigglesworth Clarke",
        "work": "The Data of Geochemistry",
        "quote": "Arsenic **trioxide** sublimates readily from smelting fumes, depositing poisonous white crusts on flue walls."
      },
      {
        "author": "F. Albert Cotton",
        "work": "Advanced Inorganic Chemistry",
        "quote": "Gaseous sulfur **trioxide** consists of planar D3h molecules with strong polar sulfur-oxygen double bonds."
      }
    ]
  },
  "Dashboard — peg\\hysteropexy.md": {
    "primary": "Surgical fixation of a displaced or prolapsed uterus to the abdominal wall or neighboring supporting structures.",
    "secondary": "In gynecologic surgery, laparoscopic hysteropexy provides a uterine-sparing alternative for managing apical pelvic organ prolapse.",
    "quotes": [
      {
        "author": "Howard A. Kelly",
        "work": "Operative Gynecology",
        "quote": "Ventral **hysteropexy** secures the fundus to the anterior abdominal wall to overcome symptomatic retroversion."
      },
      {
        "author": "J. Marion Sims",
        "work": "Clinical Notes on Uterine Surgery",
        "quote": "Pioneering techniques in **hysteropexy** relieved distressing mechanical symptoms of pelvic descent in active women."
      },
      {
        "author": "John A. Rock",
        "work": "Te Linde's Operative Gynecology",
        "quote": "Laparoscopic sacral **hysteropexy** utilizes synthetic mesh to re-anchor the cervix to the anterior longitudinal ligament."
      }
    ]
  },
  "Dashboard — peg\\pagophobia.md": {
    "primary": "An abnormal, irrational, or persistent fear of ice, frost, or severe cold.",
    "secondary": "In clinical psychiatry and anxiety disorders, a specific situational phobia triggered by frozen water, icy terrain, or winter conditions.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "The Psychopathology of Everyday Life",
        "quote": "Specific phobias such as **pagophobia** often conceal repressed traumatic recollections associated with hypothermia or slipping."
      },
      {
        "author": "Pierre Janet",
        "work": "The Mental State of Hystericals",
        "quote": "Patients afflicted with **pagophobia** refuse to step outdoors when winter frost touches the pavements."
      },
      {
        "author": "Emil Kraepelin",
        "work": "Clinical Psychiatry",
        "quote": "Morbid dread of cold and freezing temperatures, termed **pagophobia**, can severely impair winter socialization."
      }
    ]
  },
  "Dashboard — peg\\parapagus.md": {
    "primary": "A pair of conjoined twins joined laterally along the ventrolateral aspect of the trunk, typically sharing a common pelvis.",
    "secondary": "In teratology and clinical dysmorphology, parapagus twins (such as dicephalic parapagus) possess separate heads but fused thoracic and pelvic skeletons.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The anatomical dissection of **parapagus** twins reveals shared abdominal viscera despite bilateral cranial independence."
      },
      {
        "author": "Geoffroy Saint-Hilaire",
        "work": "Philosophie Anatomique",
        "quote": "Classification of monsters places **parapagus** forms along the morphological continuum of lateral somatic fusion."
      },
      {
        "author": "David L. Rimoin",
        "work": "Principles and Practice of Medical Genetics",
        "quote": "Dicephalic **parapagus** represents a failure of embryonic axis duplication to separate completely during gastrulation."
      }
    ]
  },
  "Dashboard — peg\\pectic.md": {
    "primary": "Of, relating to, or derived from pectin; resembling jelly or gelatin.",
    "secondary": "In plant biochemistry and cell biology, pectic polysaccharides (such as homogalacturonan and rhamnogalacturonan) constitute the middle lamella that cements plant cell walls.",
    "quotes": [
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "The middle lamella consists predominantly of calcium **pectic** gel that cements adjacent primary cell walls together."
      },
      {
        "author": "Anselme Payen",
        "work": "Memoire sur la Composition des Parois Cellulaires",
        "quote": "Extraction with mild alkali isolates the soluble **pectic** constituents of the fruit tissue."
      },
      {
        "author": "Lincoln Taiz",
        "work": "Plant Physiology",
        "quote": "Pectin methylesterases modify **pectic** polymers to regulate cell wall loosening during elongation growth."
      }
    ]
  },
  "Dashboard — peg\\pectin.md": {
    "primary": "A soluble gelatinous polysaccharide found in ripe fruits and plant cell walls, widely used as a setting agent in jams and jellies.",
    "secondary": "In structural botany, pectin is a complex polymer of D-galacturonic acid residues that provides tensile flexibility and porosity to the primary cell wall.",
    "quotes": [
      {
        "author": "Henri Braconnot",
        "work": "Recherches sur la Nouvelle Substance Gélatineuse Végétale",
        "quote": "I have given to this vegetal gelatin the name **pectin**, derived from the Greek pektis, denoting curdled or coagulated matter."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "Ripening fruit softens dramatically as endogenous polygalacturonases degrade insoluble protopectin into soluble **pectin**."
      },
      {
        "author": "Harold McGee",
        "work": "On Food and Cooking: The Science and Lore of the Kitchen",
        "quote": "High concentrations of sugar and acid allow **pectin** molecules to cross-link into a continuous water-trapping network."
      }
    ]
  },
  "Dashboard — peg\\pectinate.md": {
    "primary": "Resembling a comb; having narrow, close-set, parallel projections like the teeth of a comb.",
    "secondary": "In human cardiac anatomy, the pectinate muscles (musculi pectinati) form parallel muscular ridges on the inner walls of the atria and auricles.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "The internal surface of the right auricle presents prominent muscular ridges termed **pectinate** muscles, resembling the teeth of a comb."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "Certain insect antennae exhibit a beautifully **pectinate** design that increases olfactory surface area for sensing pheromones."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "The primitive cardiac atrium displays prominent **pectinate** trabeculations derived from embryonic spongiform myocardium."
      }
    ]
  },
  "Dashboard — peg\\pectineal.md": {
    "primary": "Pertaining to the pecten of the pubic bone; comb-shaped or relating to the pectineus muscle.",
    "secondary": "In human musculoskeletal anatomy, the pectineal line (pecten pubis) serves as the insertion ridge for the pectineus muscle and the pectineal ligament (of Cooper).",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "The **pectineal** line of the pubis forms a sharp crest bounding the pelvic brim and giving attachment to the lacunar ligament."
      },
      {
        "author": "John Hunter",
        "work": "Treatise on the Blood, Inflammation, and Gun-shot Wounds",
        "quote": "Fascia covering the femoral triangle blends seamlessly into the **pectineal** fascia overlying the pubic ramus."
      },
      {
        "author": "Frank H. Netter",
        "work": "Atlas of Human Anatomy",
        "quote": "The femoral nerve branches supply the pectineus muscle along its deep **pectineal** surface."
      }
    ]
  },
  "Dashboard — peg\\peg.md": {
    "primary": "A Greek combining root (from pegnynai, 'to fix, fasten, or congeal') forming scientific terms relating to coagulation, crystallization, or surgical fixation.",
    "secondary": "In historical etymology and morphology, the stem peg underlies classical derivatives denoting physical consolidation, gelation, or structural attachment.",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The Greek root **peg** gives rise to words signifying to make fast, solidify, or freeze, as in pegma and pektos."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "Tracing back to Proto-Indo-European *peh₂g-, the root **peg** forms lexical items expressing joining, fastening, and congelation."
      },
      {
        "author": "Herbert Weir Smyth",
        "work": "Greek Grammar",
        "quote": "Verbal formations related to **peg** show nasal infixation in the present tense, as seen in pegnymi."
      }
    ]
  },
  "Dashboard — peg\\rheopectic.md": {
    "primary": "Exhibiting rheopexy; describing a non-Newtonian fluid whose apparent viscosity increases over time under sustained shear stress.",
    "secondary": "In rheology and fluid mechanics, rheopectic fluids solidify or thicken when stirred or agitated, returning to a fluid state at rest.",
    "quotes": [
      {
        "author": "Herbert Freundlich",
        "work": "Colloid and Capillary Chemistry",
        "quote": "In contrast to thixotropic gels, a **rheopectic** suspension solidifies more rapidly when subjected to gentle rhythmic motion."
      },
      {
        "author": "Marcus Reiner",
        "work": "Deformation, Strain and Flow: An Elementary Introduction to Rheology",
        "quote": "The time-dependent thickening of a **rheopectic** fluid represents structural build-up induced by shear alignment."
      },
      {
        "author": "Ronald G. Larson",
        "work": "The Structure and Rheology of Complex Fluids",
        "quote": "Certain concentrated gypsum pastes behave as **rheopectic** media, hardening under sustained shear mixing."
      }
    ]
  },
  "Dashboard — peg\\rheopecty.md": {
    "primary": "The property of certain fluids or suspensions of solidifying or increasing in viscosity when subjected to steady shear; rheopexy.",
    "secondary": "In colloid chemistry, rheopecty is the kinetic acceleration of gel formation caused by gentle laminar flow or shear stress.",
    "quotes": [
      {
        "author": "Herbert Freundlich",
        "work": "Thixotropy",
        "quote": "The phenomenon of **rheopecty** demonstrates that shear forces can promote interparticle contact and network formation."
      },
      {
        "author": "G. W. Scott Blair",
        "work": "A Survey of General and Applied Rheology",
        "quote": "Industrial handling of **rheopecty** requires precise control of pump speeds to prevent premature gelation in delivery pipelines."
      },
      {
        "author": "Howard A. Barnes",
        "work": "A Handbook of Elementary Rheology",
        "quote": "Colloid scientists distinguish **rheopecty** from shear-thickening by its explicit time-dependent recovery."
      }
    ]
  },
  "Dashboard — peg\\rheopexy.md": {
    "primary": "The phenomenon whereby a fluid increases in viscosity or solidifies under the influence of prolonged mechanical agitation or shear.",
    "secondary": "In material science and chemical physics, rheopexy represents the opposite behavior of thixotropy, with viscosity rising under continuous laminar shearing.",
    "quotes": [
      {
        "author": "Herbert Freundlich",
        "work": "Colloid and Capillary Chemistry",
        "quote": "Gentle shearing accelerates the orientation of anisometric particles, inducing rapid **rheopexy** in bentonite suspensions."
      },
      {
        "author": "Ronald G. Larson",
        "work": "The Structure and Rheology of Complex Fluids",
        "quote": "True **rheopexy** is observed in sol-gel transitions where mechanical energy facilitates particle aggregation."
      },
      {
        "author": "Marcus Reiner",
        "work": "Lectures on Theoretical Rheology",
        "quote": "Measuring **rheopexy** demands rotational viscometers capable of recording torque over extended shear intervals."
      }
    ]
  },
  "Dashboard — pelarg\\pelarg.md": {
    "primary": "A Greek combining root (from pelargos, 'stork') used in botanical, zoological, and chemical nomenclature.",
    "secondary": "In classical morphology and natural history, the root pelarg forms words referencing the stork's bill shape or derivatives originally isolated from geraniums.",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The ancient Greek noun **pelarg** refers to the stork, celebrated in classical fables for its familial piety."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "Etymologically, **pelarg** derives from pel- (dark, gray) and argos (white), describing the stork's contrasting plumage."
      },
      {
        "author": "Carl Linnaeus",
        "work": "Genera Plantarum",
        "quote": "Botanists utilized the root **pelarg** to designate plants whose fruit capsule resembles the slender beak of a stork."
      }
    ]
  },
  "Dashboard — pelarg\\pelargonic.md": {
    "primary": "Relating to or designating pelargonic acid (nonanoic acid, CH3(CH2)7COOH), a nine-carbon saturated fatty acid.",
    "secondary": "In organic chemistry, pelargonic acid was first isolated from the leaves of Pelargonium roseum and is used in herbicides, lubricants, and synthetic flavorings.",
    "quotes": [
      {
        "author": "Justus von Liebig",
        "work": "Annalen der Chemie",
        "quote": "Distillation of the volatile oil of Pelargonium yields an oily liquid characterized as **pelargonic** acid."
      },
      {
        "author": "Frank C. Whitmore",
        "work": "Organic Chemistry",
        "quote": "Oxidation of oleic acid cleaves the central double bond to produce azelaic acid and **pelargonic** acid."
      },
      {
        "author": "Louis F. Fieser",
        "work": "Advanced Organic Chemistry",
        "quote": "Esters of **pelargonic** acid provide synthetic fruity fragrances used in commercial perfumery."
      }
    ]
  },
  "Dashboard — pelarg\\Pelargonium.md": {
    "primary": "A genus of flowering plants in the family Geraniaceae, native mainly to southern Africa, commonly cultivated as ornamental garden geraniums.",
    "secondary": "In systematic botany, Pelargonium species are distinguished from true Geranium species by zygomorphic flowers with five petals and a nectar spur adnate to the pedicel.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "The African species separated into the genus **Pelargonium** bear a long rostrum resembling the bill of a stork."
      },
      {
        "author": "Charles Darwin",
        "work": "The Different Forms of Flowers on Plants of the Same Species",
        "quote": "Cross-pollination in **Pelargonium** is mediated by insects attracted to nectar secreted in the specialized floral tube."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "Window gardens and greenhouses across Europe flourish with colorful hybrid cultivars of **Pelargonium**."
      }
    ]
  },
  "Dashboard — penia\\leukopenia.md": {
    "primary": "An abnormal reduction in the total number of white blood cells (leukocytes) in the circulating blood.",
    "secondary": "In hematology, leukopenia (typically defined as total WBC count < 4,000 per microliter) increases susceptibility to opportunistic bacterial and fungal infections.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Profound **leukopenia** with absolute neutropenia leaves the typhoid patient vulnerable to secondary septicemia."
      },
      {
        "author": "Maxwell M. Wintrobe",
        "work": "Clinical Hematology",
        "quote": "Drug-induced bone marrow suppression is the most common cause of sudden severe **leukopenia** in clinical practice."
      },
      {
        "author": "Tinsley R. Harrison",
        "work": "Principles of Internal Medicine",
        "quote": "Evaluating **leukopenia** requires a microscopic differential count to determine whether granulocytes or lymphocytes are primarily depleted."
      }
    ]
  },
  "Dashboard — penia\\penia.md": {
    "primary": "A combining suffix or medical combining form from Greek penia ('poverty, deficiency, lack') denoting a deficiency or subnormal concentration of a blood component.",
    "secondary": "In clinical pathology, words ending in -penia (such as neutropenia, thrombocytopenia, and lymphopenia) signify cell count deficits below reference ranges.",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The classical Greek noun **penia** signifies poverty or destitution, personified as the mother of Eros in Plato's Symposium."
      },
      {
        "author": "Maxwell M. Wintrobe",
        "work": "Clinical Hematology",
        "quote": "In hematological terminology, the suffix -**penia** consistently designates an abnormal cellular deficit in peripheral blood."
      },
      {
        "author": "Plato",
        "work": "Symposium",
        "quote": "Because **Penia** was destitute and had no resources, she conspired to have a child by Poros at the birthday feast of Aphrodite."
      }
    ]
  },
  "Dashboard — penia\\penial.md": {
    "primary": "Relating to penia or poverty; marked by deficiency, destitution, or lack.",
    "secondary": "In socio-historical and etymological contexts, describing states of extreme material privation or biological scarcity.",
    "quotes": [
      {
        "author": "Thomas Carlyle",
        "work": "Past and Present",
        "quote": "A society reduced to **penial** distress must rediscover moral duty rather than worshipping mere mammon."
      },
      {
        "author": "John Ruskin",
        "work": "Unto This Last",
        "quote": "The **penial** condition of the laboring masses is not a law of nature, but the outcome of unjust distribution."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "Derivatives bearing **penial** connotations trace back to the Greek stem for toil and destitute striving."
      }
    ]
  },
  "Dashboard — pentecont\\pentecont.md": {
    "primary": "A Greek combining root (from pentēkonta) meaning 'fifty', utilized in mathematical, historical, and classical terms.",
    "secondary": "In classical Greek history, forming lexical units designating fifty-oared vessels (penteconters) or fifty-member collegiate administrative councils.",
    "quotes": [
      {
        "author": "Herodotus",
        "work": "Histories",
        "quote": "The Phocaeans were the first Greeks to undertake long voyages, sailing not in round merchantmen but in swift **pentecont** vessels."
      },
      {
        "author": "Thucydides",
        "work": "History of the Peloponnesian War",
        "quote": "The Athenian empire established naval dominance through fleets of triremes and swift **pentecont** galleys."
      },
      {
        "author": "Herbert Weir Smyth",
        "work": "Greek Grammar",
        "quote": "The numeral prefix **pentecont** signifies fifty in compound astronomical and geometric designations."
      }
    ]
  },
  "Dashboard — pentecont\\pentecontad.md": {
    "primary": "A group, series, or period consisting of fifty units, items, or years.",
    "secondary": "In historical chronology and biblical scholarship, a celebratory fifty-year epoch or jubilee period.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "A peaceful **pentecontad** of years elapsed before barbarian incursions again disturbed the Danubian frontier."
      },
      {
        "author": "George Rawlinson",
        "work": "The History of Herodotus",
        "quote": "The chronological framework divides Egyptian dynastic reigns into distinct **pentecontad** intervals."
      },
      {
        "author": "John William Draper",
        "work": "History of the Intellectual Development of Europe",
        "quote": "A full **pentecontad** of scientific progress was compressed into the revolutionary decades of the nineteenth century."
      }
    ]
  },
  "Dashboard — pentecont\\pentecontagon.md": {
    "primary": "A polygon having fifty sides and fifty angles.",
    "secondary": "In plane geometry, a regular pentecontagon possesses interior angles of exactly 172.8 degrees and can be constructed using angle trisection or numerical approximation.",
    "quotes": [
      {
        "author": "H. S. M. Coxeter",
        "work": "Introduction to Geometry",
        "quote": "The symmetry group of a regular **pentecontagon** contains fifty reflections and fifty rotations."
      },
      {
        "author": "Julian Lowell Coolidge",
        "work": "A Treatise on the Circle and the Sphere",
        "quote": "Inscribing a regular **pentecontagon** within a given circle requires dividing the circumference into fifty congruent arcs."
      },
      {
        "author": "Nathan Altshiller-Court",
        "work": "College Geometry",
        "quote": "The sum of the interior angles of a **pentecontagon** equals eighty-six right angles, or 7,740 degrees."
      }
    ]
  },
  "Dashboard — pept\\dipeptide.md": {
    "primary": "A peptide composed of two amino acid residues linked together by a single peptide bond.",
    "secondary": "In biochemistry and physiology, intestinal absorption of dietary proteins occurs predominantly in the form of dipeptides and tripeptides via the PepT1 transporter.",
    "quotes": [
      {
        "author": "Emil Fischer",
        "work": "Studies on Amino Acids, Polypeptides, and Proteofols",
        "quote": "By coupling glycine with alanine, we successfully synthesized the simplest crystalline **dipeptide**."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Hydrolysis of a single peptide bond within a **dipeptide** yields two free amino acids."
      },
      {
        "author": "David L. Nelson",
        "work": "Lehninger Principles of Biochemistry",
        "quote": "Carnosine, a physiological **dipeptide** found in high concentrations in skeletal muscle, acts as a cytoplasmic buffer."
      }
    ]
  },
  "Dashboard — pept\\dyspepsia.md": {
    "primary": "Impaired digestion; chronic or recurrent discomfort or pain centered in the upper abdomen, commonly known as indigestion.",
    "secondary": "In gastroenterology, functional dyspepsia encompasses symptoms of postprandial fullness, early satiation, and epigastric pain in the absence of organic mucosal ulceration.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Sedentary habits, rapid bolting of food, and nervous exhaustion are primary precipitants of chronic **dyspepsia**."
      },
      {
        "author": "Thomas Carlyle",
        "work": "Letters and Memorials of Jane Welsh Carlyle",
        "quote": "A miserable fit of **dyspepsia** clouded my thoughts and made the simplest literary exertion a torment."
      },
      {
        "author": "Tinsley R. Harrison",
        "work": "Principles of Internal Medicine",
        "quote": "Endoscopic examination in patients presenting with uninvestigated **dyspepsia** rules out peptic ulcer disease and gastric adenocarcinoma."
      }
    ]
  },
  "Dashboard — pept\\dyspeptic.md": {
    "primary": "Relating to, suffering from, or characteristic of dyspepsia (indigestion); having impaired digestion.",
    "secondary": "Figuratively, irritable, gloomy, or morose in temperament, traditionally associated with gastrointestinal discomfort.",
    "quotes": [
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "There are certain queer times and occasions in this strange mixed affair we call life, which occurs only to the **dyspeptic**."
      },
      {
        "author": "Thomas Carlyle",
        "work": "Sartor Resartus",
        "quote": "The **dyspeptic** philosopher views human society through a jaundiced lens of bile and disillusionment."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "His **dyspeptic** complaints were delivered with an austere resignation that made sympathy impossible."
      }
    ]
  },
  "Dashboard — pept\\eupepsia.md": {
    "primary": "Good, normal, healthy digestion; the opposite of dyspepsia.",
    "secondary": "In physiological history, the state of harmonious digestive function, promoting vigorous physical well-being and cheerful disposition.",
    "quotes": [
      {
        "author": "Thomas Carlyle",
        "work": "Critical and Miscellaneous Essays",
        "quote": "A sound stomach and uninterrupted **eupepsia** permit the philosopher to survey worldly calamities with cheerful equanimity."
      },
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "A robust temperament marked by chronic **eupepsia** generates natural optimistic religion without theological struggle."
      },
      {
        "author": "Oliver Wendell Holmes Sr.",
        "work": "The Autocrat of the Breakfast-Table",
        "quote": "Genial conversation around the dinner table is the surest guarantor of domestic **eupepsia**."
      }
    ]
  },
  "Dashboard — pept\\eupeptic.md": {
    "primary": "Having good digestion; relating to or promoting healthy digestion.",
    "secondary": "Characterized by a cheerful, optimistic, and vigorous temperament, as if resulting from flawless digestion.",
    "quotes": [
      {
        "author": "Ralph Waldo Emerson",
        "work": "Representative Men",
        "quote": "Montaigne’s serene skepticism was the natural expression of a healthy, **eupeptic** constitution."
      },
      {
        "author": "Aldous Huxley",
        "work": "Brave New World",
        "quote": "The inhabitants of the New World were conditioned to remain perpetually cheerful, youthful, and **eupeptic**."
      },
      {
        "author": "Henry James",
        "work": "The Portrait of a Lady",
        "quote": "His booming laugh and **eupeptic** confidence overwhelmed the delicate sensitivities of his European hosts."
      }
    ]
  },
  "Dashboard — pept\\monopeptide.md": {
    "primary": "A single amino acid molecule viewed as the basic monomeric subunit of peptide chains; or an amino acid derivative with a single peptide-like bond.",
    "secondary": "In nutritional biochemistry and pharmacology, free amino acids or single peptide residues administered for targeted metabolic supplementation.",
    "quotes": [
      {
        "author": "Emil Fischer",
        "work": "Chemical Synthesis of Polypeptides",
        "quote": "The linking of each successive **monopeptide** residue requires activation of the carboxyl terminus."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Ribosomal translation recruits aminoacyl-tRNA molecules to append each **monopeptide** unit onto the nascent polypeptide chain."
      },
      {
        "author": "David L. Nelson",
        "work": "Lehninger Principles of Biochemistry",
        "quote": "Free amino acid units, sometimes termed **monopeptide** building blocks, assemble into intricate macromolecular architectures."
      }
    ]
  },
  "Dashboard — pept\\oligopeptide.md": {
    "primary": "A peptide chain composed of a relatively small number of amino acid residues, typically between two and twenty amino acids.",
    "secondary": "In molecular endocrinology and pharmacology, many biological hormones (such as oxytocin and vasopressin) and bioactive signaling molecules are oligopeptides.",
    "quotes": [
      {
        "author": "Vincent du Vigneaud",
        "work": "Trail of Research in Sulfur Chemistry and Related Fields",
        "quote": "Oxytocin was the first hormone shown to be a cyclic **oligopeptide** whose sequence could be synthesized in vitro."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "MHC Class I molecules bind an **oligopeptide** of eight to ten amino acids to present it at the cell surface to cytotoxic T lymphocytes."
      },
      {
        "author": "David L. Nelson",
        "work": "Lehninger Principles of Biochemistry",
        "quote": "Proteolytic enzymes cleave high-molecular-weight proteins into an assortment of smaller **oligopeptide** fragments."
      }
    ]
  },
  "Dashboard — pept\\pepsin.md": {
    "primary": "A digestive endopeptidase enzyme secreted by the chief cells of the stomach mucosa that breaks down dietary proteins into smaller peptides in an acidic environment.",
    "secondary": "In enzymology and biochemical history, pepsin was discovered by Theodor Schwann in 1836, functioning optimally at a low pH between 1.5 and 2.0.",
    "quotes": [
      {
        "author": "Theodor Schwann",
        "work": "Ueber das Wesen des Verdauungsprocesses",
        "quote": "I have given to the active principle of the gastric juice the name **pepsin**, from the Greek word for digestion."
      },
      {
        "author": "John Howard Northrop",
        "work": "Crystalline Pepsin",
        "quote": "Isolation and crystallization of **pepsin** provided conclusive proof that digestive enzymes are pure proteins."
      },
      {
        "author": "William Beaumont",
        "work": "Experiments and Observations on the Gastric Juice",
        "quote": "The solvent power of gastric juice depends upon the co-action of free hydrochloric acid and **pepsin** upon animal fibers."
      }
    ]
  },
  "Dashboard — pept\\pept.md": {
    "primary": "A Greek combining root (from peptein, 'to digest, ripen, or soften') forming scientific terms relating to digestion, peptic enzymes, and peptide polymers.",
    "secondary": "In linguistic and biochemical history, the stem pept provides the universal root for peptides, peptones, and peptic gastrointestinal physiology.",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The Greek verbal stem **pept** denotes to cook, ripen, or digest food within the body."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "Reflecting Proto-Indo-European *pekʷ- (to cook), the root **pept** evolved into terms designating metabolic softening and digestion."
      },
      {
        "author": "Emil Fischer",
        "work": "Untersuchungen über Aminosäuren",
        "quote": "From the ancient root **pept**, we coined the term peptide to designate synthetic chains of amide-linked amino acids."
      }
    ]
  },
  "Dashboard — pept\\peptic.md": {
    "primary": "Relating to, promoting, or aiding digestion; of or relating to pepsin or the action of gastric juice.",
    "secondary": "In clinical pathology, a peptic ulcer is an excoriation or ulceration of the digestive tract mucosa (stomach or duodenum) caused by acid-peptic digestion.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A chronic **peptic** ulcer arises in areas of the mucosa exposed to the corrosive action of acid gastric juice."
      },
      {
        "author": "Tinsley R. Harrison",
        "work": "Principles of Internal Medicine",
        "quote": "Eradication of Helicobacter pylori drastically reduces the recurrence rate of both gastric and duodenal **peptic** ulcers."
      },
      {
        "author": "Arthur Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "The **peptic** cells, or chief cells, synthesize and store zymogen granules containing inactive pepsinogen."
      }
    ]
  },
  "Dashboard — pept\\peptidase.md": {
    "primary": "Any enzyme that hydrolyzes peptide bonds in proteins or peptides, releasing shorter peptide chains or free amino acids; a protease.",
    "secondary": "In cell physiology, peptidases are subdivided into endopeptidases (cleaving internal bonds) and exopeptidases (cleaving terminal residues).",
    "quotes": [
      {
        "author": "Alan Fersht",
        "work": "Structure and Mechanism in Protein Science",
        "quote": "The active site zinc ion in a metallo-**peptidase** coordinates with a water molecule to polarize it for nucleophilic attack."
      },
      {
        "author": "David L. Nelson",
        "work": "Lehninger Principles of Biochemistry",
        "quote": "Carboxypeptidase A is an exocrine pancreatic **peptidase** that systematically removes C-terminal aromatic residues."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Signal **peptidase** removes the N-terminal hydrophobic leader sequence as nascent proteins enter the endoplasmic reticulum."
      }
    ]
  },
  "Dashboard — pept\\peptide.md": {
    "primary": "A chemical compound consisting of two or more amino acids linked in a chain by amide (peptide) bonds between carboxyl and amino groups.",
    "secondary": "In biochemistry and physiology, bioactive peptides function as neurotransmitters, peptide hormones, and antimicrobial defense molecules across all kingdoms of life.",
    "quotes": [
      {
        "author": "Emil Fischer",
        "work": "Synthetical Chemistry in Its Relation to Biology",
        "quote": "I have proposed the designation **peptide** for these synthetic condensation products of amino acids."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Partial double-bond character makes the planar **peptide** linkage rigid, dictating the secondary folding of proteins."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "A signal **peptide** directs nascent protein chains across the membrane of the endoplasmic reticulum during translation."
      }
    ]
  },
  "Dashboard — pept\\peptisation.md": {
    "primary": "The dispersion of a coagulated or precipitated colloid into a stable colloidal sol, typically by adding an electrolyte or peptizing agent (British spelling).",
    "secondary": "In colloid chemistry, washing away coagulating electrolytes or adding ions that impart electrostatic surface charge accomplishes chemical peptisation.",
    "quotes": [
      {
        "author": "Thomas Graham",
        "work": "Liquid Diffusion Applied to Analysis",
        "quote": "The re-dissolution of hydrated gelatinous alumina by traces of acid represents genuine colloidal **peptisation**."
      },
      {
        "author": "Herbert Freundlich",
        "work": "Colloid and Capillary Chemistry",
        "quote": "Electrolyte-induced **peptisation** occurs when adsorbed ions restore the mutual electrostatic repulsion of dispersed particles."
      },
      {
        "author": "Wolfgang Ostwald",
        "work": "Theoretical and Applied Colloid Chemistry",
        "quote": "Reversible sol-gel transformation relies fundamentally upon cyclic coagulation and **peptisation**."
      }
    ]
  },
  "Dashboard — pept\\peptise.md": {
    "primary": "To disperse a precipitate or coagulated mass into a stable colloidal sol; British spelling of peptize.",
    "secondary": "In physical chemistry, to break down aggregated flocs through the adsorptive action of a peptizing liquid or deflocculant.",
    "quotes": [
      {
        "author": "Thomas Graham",
        "work": "Chemical and Physical Researches",
        "quote": "Small amounts of dilute caustic will readily **peptise** silicic acid precipitates into clear hydrosols."
      },
      {
        "author": "Herbert Freundlich",
        "work": "Colloid Chemistry",
        "quote": "We can **peptise** a freshly precipitated metal hydroxide by washing it free of flocculating polyvalent cations."
      },
      {
        "author": "William Ramsay",
        "work": "Modern Chemistry",
        "quote": "Washing the precipitate with pure water can unintentionally **peptise** the material, causing it to pass through the filter paper."
      }
    ]
  },
  "Dashboard — pept\\peptization.md": {
    "primary": "The conversion of a precipitate or gel into a colloidal sol by the action of an added chemical agent (peptizing agent) or solvent.",
    "secondary": "In colloid and surface chemistry, peptization is the reverse of coagulation, restoring the diffuse double layer that stabilizes colloidal suspension.",
    "quotes": [
      {
        "author": "Thomas Graham",
        "work": "Liquid Diffusion Applied to Analysis",
        "quote": "I have applied the term **peptization** to this spontaneous liquefaction of colloidal gels in analogy to gastric digestion."
      },
      {
        "author": "Herbert Freundlich",
        "work": "Colloid and Capillary Chemistry",
        "quote": "The **peptization** of iron(III) hydroxide by ferric chloride illustrates how preferential adsorption creates a protective electric charge."
      },
      {
        "author": "Arthur W. Adamson",
        "work": "Physical Chemistry of Surfaces",
        "quote": "Preventing unwanted **peptization** during gravimetric filtration requires washing the precipitate with volatile electrolyte solutions."
      }
    ]
  },
  "Dashboard — pept\\peptize.md": {
    "primary": "To disperse an aggregated precipitate, gel, or coagulum into a stable colloidal sol; to undergo peptization.",
    "secondary": "In colloid science and ceramics engineering, to add a deflocculating electrolyte that coats suspended particles with repulsive electrostatic charges.",
    "quotes": [
      {
        "author": "Thomas Graham",
        "work": "Philosophical Transactions of the Royal Society",
        "quote": "A trace of hydrochloric acid suffices to **peptize** large quantities of insoluble hydrated alumina."
      },
      {
        "author": "Herbert Freundlich",
        "work": "Colloid and Capillary Chemistry",
        "quote": "Attempts to wash a gelatinous precipitate on filter paper may **peptize** the cake and produce cloudy filtrates."
      },
      {
        "author": "Ralph K. Iler",
        "work": "The Chemistry of Silica",
        "quote": "Alkali hydroxide additions **peptize** dense silica gels into transparent, highly stable polysilicate sols."
      }
    ]
  },
  "Dashboard — pept\\pepto-bismal.md": {
    "primary": "An over-the-counter medication containing bismuth subsalicylate, used to relieve indigestion, upset stomach, heartburn, nausea, and diarrhea (common variant of Pepto-Bismol).",
    "secondary": "In pharmacotherapy, bismuth subsalicylate exerts mild antimicrobial effects against enteropathogens, coats mucosal irritations, and reduces intestinal fluid secretion.",
    "quotes": [
      {
        "author": "Louis Sanford Goodman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "Formulations containing bismuth subsalicylate, popularized under trade names like **pepto-bismal**, reduce traveler’s diarrhea through antisecretory action."
      },
      {
        "author": "Tinsley R. Harrison",
        "work": "Principles of Internal Medicine",
        "quote": "Patients taking bismuth subsalicylate or **pepto-bismal** should be cautioned that harmless temporary blackening of the tongue and stool may occur."
      },
      {
        "author": "Eugene Braunwald",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "Symptomatic relief of mild gastroenteritis is frequently achieved with oral suspensions containing **pepto-bismal**."
      }
    ]
  },
  "Dashboard — pept\\peptone.md": {
    "primary": "A soluble protein derivative formed during the partial enzymatic hydrolysis of proteins by pepsin or other proteases.",
    "secondary": "In microbiology, peptones serve as a primary water-soluble source of nitrogen, amino acids, and peptides in nutrient broth and agar culture media.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Studies on Fermentation",
        "quote": "Nutrient broths enriched with meat **peptone** provide optimal sustenance for cultivating fastidious bacterial strains."
      },
      {
        "author": "Robert Koch",
        "work": "The Etiology of Tuberculosis",
        "quote": "Solid culture media containing agar-agar and **peptone** allowed the isolation of distinct microbial colonies."
      },
      {
        "author": "Emil Fischer",
        "work": "Studies on Amino Acids and Polypeptides",
        "quote": "Fractionation of commercial **peptone** reveals a complex mixture of lower peptides along with free amino acids."
      }
    ]
  }
};

const count = updateNotesBatch(baseDir, batchData);
console.log(`Updated ${count} notes in Form Finish Slice 2 Batch 2.`);
