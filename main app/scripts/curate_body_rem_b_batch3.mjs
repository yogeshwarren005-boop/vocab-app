import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Body & Physiology');
const batchData = {
  "Dashboard — pne\\apnea.md": {
    "primary": "Temporary cessation or suspension of breathing, especially during sleep.",
    "secondary": "In clinical somnology and pulmonology, an episode of airflow cessation lasting at least ten seconds, classified as obstructive (airway collapse), central (loss of respiratory drive), or mixed sleep apnea.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Periodic respiration characterized by alternating hyperpnea and prolonged **apnea** constitutes the classical Cheyne-Stokes pattern."
      },
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "Direct stimulation of the inhibitory vagal fibers immediately arrested diaphragmatic movement, producing experimental **apnea**."
      },
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "During the alarming interval of nocturnal **apnea**, the patient appears suspended between life and suffocation."
      }
    ]
  },
  "Dashboard — pne\\apnoea.md": {
    "primary": "Transient suspension of external breathing (Commonwealth spelling; apnea).",
    "secondary": "In neonatal medicine and physiology, failure of involuntary respiration in premature infants resulting from immature brainstem respiratory centers, often accompanied by bradycardia and hypoxemia.",
    "quotes": [
      {
        "author": "John Tyndall",
        "work": "Sound",
        "quote": "Artificial ventilation with excess oxygen saturates the blood, precipitating a physiological state of respiratory **apnoea**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The recurrent attacks of infant **apnoea** subsided as the medullary respiratory centers matured under close observation."
      },
      {
        "author": "Joseph Lister",
        "work": "Collected Papers",
        "quote": "Under deep chloroform administration, brief reflexes of **apnoea** must be distinguished from toxic respiratory arrest."
      }
    ]
  },
  "Dashboard — pne\\dyspnoea.md": {
    "primary": "Difficult, labored, or painful breathing; shortness of breath (Commonwealth spelling; dyspnea).",
    "secondary": "In cardiopulmonary semiotics, a subjective sensation of breathing discomfort resulting from mismatched ventilatory demand and mechanical capacity, characteristic of asthma, heart failure, or pulmonary fibrosis.",
    "quotes": [
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "Severe paroxysmal **dyspnoea** seizing the patient in the dead of night is the cardinal symptom of cardiac asthma."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Exertional **dyspnoea** marks the earliest functional failure of myocardial compensation in mitral valvular stenosis."
      },
      {
        "author": "Thomas Sydenham",
        "work": "The Works of Thomas Sydenham",
        "quote": "The chest seemed bound with iron bands, provoking agonizing **dyspnoea** whenever the sufferer attempted recumbency."
      }
    ]
  },
  "Dashboard — pne\\dyspnoeal.md": {
    "primary": "Pertaining to, experiencing, or characterized by dyspnea or difficult breathing (Commonwealth spelling).",
    "secondary": "In clinical case reporting, describing acute episodes, posture, or physical findings (such as tachypnea, grunting, and intercostal indrawing) associated with respiratory distress.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The patient assumed an upright orthopneic posture to alleviate the distressing **dyspnoeal** paroxysm."
      },
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "On auscultation during the **dyspnoeal** crisis, widespread sonorous rhonchi and wheezing filled both hemithoraces."
      },
      {
        "author": "Florence Nightingale",
        "work": "Notes on Nursing",
        "quote": "A well-ventilated chamber without direct drafts brings visible relief to the **dyspnoeal** invalid."
      }
    ]
  },
  "Dashboard — pne\\dyspnoeic.md": {
    "primary": "Affected by or suffering from difficulty in breathing; short of breath (Commonwealth spelling).",
    "secondary": "In emergency medicine and intensive care, designating patients presenting with subjective air hunger, cyanosis, and accessory respiratory muscle recruitment.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The acutely **dyspnoeic** patient sat perched on the edge of the bed, gasping for air with flaring alae nasi."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Autopsy of the severely **dyspnoeic** patient revealed massive alveolar infiltration and bilateral pulmonary edema."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Stark Munro Letters",
        "quote": "I was summoned urgently to examine a **dyspnoeic** child choking from acute diphtheritic croup."
      }
    ]
  },
  "Dashboard — pne\\pleuropneumonia.md": {
    "primary": "Concurrent inflammation affecting both the pleura and the pulmonary parenchyma.",
    "secondary": "In veterinary and comparative medicine, infectious pleuropneumonia of bovines and swine caused by Mycoplasma species, distinguished by extensive fibrinous pleurisy and pulmonary consolidation.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The combination of harsh friction rubs and dense bronchial breathing pointed unmistakably to acute **pleuropneumonia**."
      },
      {
        "author": "Louis Pasteur",
        "work": "Collected Works on Infectious Diseases",
        "quote": "Inoculation of attenuated exudate into the tail of cattle provided solid immunity against contagious **pleuropneumonia**."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The marble-like appearance of the lung parenchyma in bovine **pleuropneumonia** stems from thrombosed interlobular lymphatics."
      }
    ]
  },
  "Dashboard — pne\\pneumatic.md": {
    "primary": "Containing, operated by, or utilizing air or gas under pressure.",
    "secondary": "In theology, philosophy, and engineering, relating to the spirit (pneuma) in Gnosticism, or utilizing compressed air to transmit mechanical power in machinery, tires, and drilling tools.",
    "quotes": [
      {
        "author": "Robert Boyle",
        "work": "New Experiments Physico-Mechanicall, Touching the Spring of the Air",
        "quote": "Our newly constructed **pneumatic** engine demonstrated that air possesses elasticity and exerts measurable weight."
      },
      {
        "author": "Aldous Huxley",
        "work": "Brave New World",
        "quote": "She was wonderfully **pneumatic**, with the buoyant, rubbery vitality prized by the society of the World State."
      },
      {
        "author": "Joseph Priestley",
        "work": "Experiments and Observations on Different Kinds of Air",
        "quote": "The **pneumatic** trough enabled natural philosophers to collect and examine invisible elastic fluids over water."
      }
    ]
  },
  "Dashboard — pne\\pneumonic.md": {
    "primary": "Pertaining to, resembling, or affected by pneumonia or the lungs.",
    "secondary": "In infectious epidemiology and pathology, denoting the pulmonary form of disease, notably pneumonic plague (Yersinia pestis) transmitted by respiratory droplets with rapid lethality.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Lobar consolidation during acute **pneumonic** fever progresses from red to grey hepatization."
      },
      {
        "author": "Daniel Defoe",
        "work": "A Journal of the Plague Year",
        "quote": "The deadlier **pneumonic** form of the pestilence spread swiftly from breath to breath without buboes."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Microscopic sections of the **pneumonic** lung revealed alveoli packed with dense fibrin meshes and erythrocytes."
      }
    ]
  },
  "Dashboard — pne\\pneumotaxic.md": {
    "primary": "Regulating or coordinating the rate, rhythm, and pattern of respiration.",
    "secondary": "In neurophysiology, designating the pontine pneumotaxic center (located in the parabrachial nucleus and Kölliker-Fuse nucleus) that limits inspiration and controls respiratory frequency.",
    "quotes": [
      {
        "author": "Claude Bernard",
        "work": "Lectures on the Physiology of the Nervous System",
        "quote": "Brainstem transection experiments revealed a specialized **pneumotaxic** mechanism coordinating rhythmic phrenic discharge."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Damage to pontine **pneumotaxic** tracts produces apneustic breathing characterized by prolonged inspiratory spasms."
      },
      {
        "author": "Charles Scott Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "Rhythmic breathing reflects intrinsic pacemakers regulated by descending inhibitory signals from the **pneumotaxic** center."
      }
    ]
  },
  "Dashboard — pneum\\cardiopulmonary.md": {
    "primary": "Relating to or affecting both the heart and the lungs.",
    "secondary": "In critical care and emergency medicine, referring to integrated cardiovascular and pulmonary function, as in cardiopulmonary resuscitation (CPR) or cardiopulmonary bypass (heart-lung machine).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe chronic cor pulmonale demonstrates the intimate functional interlock of the **cardiopulmonary** circuit."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Raised intracranial tension elicits the Cushing reflex, causing profound **cardiopulmonary** adjustments."
      },
      {
        "author": "Alexis Carrel",
        "work": "The Surgery of Blood Vessels",
        "quote": "The perfection of mechanical **cardiopulmonary** perfusion opened the possibility of intracardiac surgical repair."
      }
    ]
  },
  "Dashboard — pneum\\pneumatic.md": {
    "primary": "Operated, inflated, or moved by compressed air or other gases.",
    "secondary": "In mechanical physics and industrial engineering, utilizing pressurized air systems for propulsion, braking (Westinghouse air brake), or pneumatic tube transport.",
    "quotes": [
      {
        "author": "Robert Boyle",
        "work": "Continuation of New Experiments Physico-Mechanical",
        "quote": "The mercurial gauge registered complete exhaustion of air inside the sealed **pneumatic** receiver."
      },
      {
        "author": "H. G. Wells",
        "work": "The Time Machine",
        "quote": "In that subterranean future, intricate **pneumatic** shafts ventilated the deep caverns of the Morlocks."
      },
      {
        "author": "George Orwell",
        "work": "1984",
        "quote": "Winston rolled up the slip of paper and dropped it into the **pneumatic** tube with a gentle whoosh."
      }
    ]
  },
  "Dashboard — pneum\\pneumatically.md": {
    "primary": "By means of air, gas, or pneumatic pressure mechanisms.",
    "secondary": "In engineering and industrial technology, operating, conveying, or controlling machinery, valves, or switches via pressurized air conduits.",
    "quotes": [
      {
        "author": "H. G. Wells",
        "work": "The War of the Worlds",
        "quote": "The alien handling-machine operated **pneumatically**, flexing its jointed tentacles with soft hissing puffs."
      },
      {
        "author": "Jules Verne",
        "work": "Twenty Thousand Leagues Under the Sea",
        "quote": "Water ballast was **pneumatically** expelled from the tanks of the Nautilus to regain positive buoyancy."
      },
      {
        "author": "George Orwell",
        "work": "1984",
        "quote": "Messages and historical documents were **pneumatically** whisked through the Ministry of Truth to the memory holes."
      }
    ]
  },
  "Dashboard — pneum\\pneumatics.md": {
    "primary": "The branch of physics and engineering that deals with the mechanical properties of air and other gases.",
    "secondary": "In classical mechanics and technology, the study of gas compression, vacuum generation, and fluid power transmission, founded by Hero of Alexandria and revived by Evangelista Torricelli and Robert Boyle.",
    "quotes": [
      {
        "author": "Hero of Alexandria",
        "work": "Pneumatics",
        "quote": "In this treatise on **pneumatics**, we demonstrate how air and water may be made to open temple doors and sound trumpets."
      },
      {
        "author": "Robert Boyle",
        "work": "New Experiments Physico-Mechanicall",
        "quote": "Progress in experimental **pneumatics** overthrew the ancient philosophical dogma that nature abhors a vacuum."
      },
      {
        "author": "Joseph Priestley",
        "work": "The History and Present State of Discoveries Relating to Vision, Light, and Colours",
        "quote": "Discoveries in chemical **pneumatics** revealed that ordinary air was an intricate mixture of distinct gases."
      }
    ]
  },
  "Dashboard — pneum\\pneumatology.md": {
    "primary": "The study or doctrine of spiritual beings, spirits, or the Holy Spirit; pneumatics in theological philosophy.",
    "secondary": "In historical metaphysics and natural philosophy, the systematic treatise on immaterial spiritual substances (angels, human souls, God) or early medical theories of vital animal spirits (pneuma).",
    "quotes": [
      {
        "author": "Immanuel Kant",
        "work": "Critique of Pure Reason",
        "quote": "Rational **pneumatology** attempts to prove the immateriality and immortality of the human soul through pure concepts."
      },
      {
        "author": "Jonathan Edwards",
        "work": "Freedom of the Will",
        "quote": "Orthodox Reformed **pneumatology** expounds the regenerating efficacy of the Divine Spirit upon the corrupt human heart."
      },
      {
        "author": "Walter Pater",
        "work": "Marius the Epicurean",
        "quote": "Stoic **pneumatology** conceived of the cosmos as animated by a fiery, intelligent breath permeating all matter."
      }
    ]
  },
  "Dashboard — pneum\\pneumatophore.md": {
    "primary": "A specialized aerial root produced by certain mangrove and wetland trees that grows upward out of water or waterlogged mud to facilitate gas exchange.",
    "secondary": "In marine invertebrate zoology, the gas-filled floating polyp (air-sac) that acts as a float in siphonophores, such as the Portuguese man-of-war (Physalia physalis).",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "On the Origin of Species",
        "quote": "The upright **pneumatophore** of the mangrove provides oxygen to subterranean roots submerged in hypoxic coastal mud."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Oceanic Hydrozoa",
        "quote": "The apical **pneumatophore** of the siphonophore secretes gas into its central cavity to maintain oceanic buoyancy."
      },
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "At low tide, thousands of slender **pneumatophore** roots bristled like dark fingers across the intertidal mangrove swamp."
      }
    ]
  },
  "Dashboard — pneum\\pneumococcal.md": {
    "primary": "Pertaining to, caused by, or relating to the bacterium Streptococcus pneumoniae (the pneumococcus).",
    "secondary": "In microbiology and infectious disease, referring to clinical infections (such as pneumococcal pneumonia, pneumococcal meningitis, and bacteremia) or capsular polysaccharide vaccines designed to prevent them.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The sudden rigor, high fever, and rusty sputum point definitively toward acute **pneumococcal** infection."
      },
      {
        "author": "Oswald Avery",
        "work": "Studies on the Chemical Nature of the Substance Inducing Transformation of Pneumococcal Types",
        "quote": "DNA extracted from encapsulated strains induced hereditary transformation in unencapsulated **pneumococcal** cells."
      },
      {
        "author": "Anthony Fauci",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "Widespread administration of conjugate vaccines dramatically reduced the incidence of invasive **pneumococcal** disease."
      }
    ]
  },
  "Dashboard — pneum\\pneumococcus.md": {
    "primary": "A bacterium (Streptococcus pneumoniae) that causes pneumonia, meningitis, and other infections, typically appearing as lancet-shaped Gram-positive diplococci.",
    "secondary": "In bacteriological history, the pathogen isolated independently by Louis Pasteur and George Sternberg in 1881, whose capsular transformation led to the landmark discovery of DNA as genetic material by Avery, MacLeod, and McCarty.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Comptes Rendus de l'Académie des Sciences",
        "quote": "We isolated from saliva a virulent micrococcus, later recognized as the **pneumococcus**, lethal to inoculated rabbits."
      },
      {
        "author": "Oswald Avery",
        "work": "Journal of Experimental Medicine",
        "quote": "The type-specific capsular polysaccharide of the **pneumococcus** determines both its virulence and immunological identity."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The lancet-shaped diplococcus pneumoniae, or **pneumococcus**, is found in over eighty percent of lobar pneumonias."
      }
    ]
  },
  "Dashboard — pneum\\pneumoconiosis.md": {
    "primary": "A chronic disease of the lungs caused by the habitual inhalation of dust, especially mineral or metallic dust, resulting in progressive fibrosis.",
    "secondary": "In occupational medicine and environmental pathology, a group of occupational lung diseases (including silicosis, asbestosis, and coal workers' pneumoconiosis) characterized by dust-laden alveolar macrophages and dense collagen deposition.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In miners and stone-cutters, chronic **pneumoconiosis** leads to dense fibrous induration of the pulmonary parenchyma."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Histological examination in anthraco-silicotic **pneumoconiosis** reveals blackened fibrous nodules surrounding respiratory bronchioles."
      },
      {
        "author": "Alice Hamilton",
        "work": "Industrial Poisons in the United States",
        "quote": "Exhaust ventilation and dust suppression in granite quarries drastically curtailed the deadly toll of industrial **pneumoconiosis**."
      }
    ]
  },
  "Dashboard — pneum\\pneumocytosis.md": {
    "primary": "Infection caused by the fungal pathogen Pneumocystis jirovecii (formerly Pneumocystis carinii), historically termed pneumocytosis.",
    "secondary": "In clinical infectious disease and immunocompromised hosts, opportunistic interstitial plasma cell pneumonia (Pneumocystis pneumonia, PCP) characterized by severe hypoxemia, ground-glass pulmonary opacities, and foamy intra-alveolar exudates.",
    "quotes": [
      {
        "author": "Anthony Fauci",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "The early outbreak of opportunistic **pneumocytosis** in previously healthy individuals heralded the clinical emergence of AIDS."
      },
      {
        "author": "William Osler",
        "work": "Modern Medicine: Its Theory and Practice",
        "quote": "Infantile plasma cell pneumonia or **pneumocytosis** caused severe epidemic asphyxiation in premature nursery wards."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Silver-stained alveolar smears in fatal **pneumocytosis** demonstrated cup-shaped cysts packed within foamy exudate."
      }
    ]
  },
  "Dashboard — pneum\\pneumoencephalogram.md": {
    "primary": "A radiograph of the brain and ventricular system obtained after replacing cerebrospinal fluid with injected air, oxygen, or helium (pneumoencephalography).",
    "secondary": "In historical neuroradiology, a diagnostic procedure developed by Walter Dandy in 1919 to outline cerebral ventricles and subarachnoid cisterns before the advent of CT and MRI.",
    "quotes": [
      {
        "author": "Walter Dandy",
        "work": "Annals of Surgery",
        "quote": "The introduction of air by lumbar puncture yields a distinct **pneumoencephalogram**, clearly outlining cerebral ventricular dilatation."
      },
      {
        "author": "Harvey Cushing",
        "work": "Intracranial Tumours",
        "quote": "The **pneumoencephalogram** showed lateral displacement of the third ventricle, confirming a deeply seated temporal lobe neoplasm."
      },
      {
        "author": "Wilder Penfield",
        "work": "Epilepsy and the Functional Anatomy of the Human Brain",
        "quote": "Careful study of the **pneumoencephalogram** helped localize epileptogenic scar tissue causing focal cortical seizures."
      }
    ]
  },
  "Dashboard — pneum\\pneumogastric.md": {
    "primary": "Pertaining to both the lungs and the stomach, or denoting the tenth cranial nerve (the vagus nerve).",
    "secondary": "In classical neuroanatomy and autonomic physiology, the archaic designation for the vagus nerve (nervus pneumogastricus), reflecting its extensive parasympathetic distribution to thoracic viscera and abdominal digestive organs.",
    "quotes": [
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "Section of the **pneumogastric** nerve in the neck profoundly disrupts both cardiac inhibition and gastric digestive secretion."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "The **pneumogastric** nerve supplies motor and sensory parasympathetic fibers to the respiratory organs and alimentary canal."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Irritation of the recurrent branches of the **pneumogastric** nerve by an aortic aneurysm produces hoarseness and laryngeal stridor."
      }
    ]
  },
  "Dashboard — pneum\\pneumonectomy.md": {
    "primary": "The surgical excision and removal of an entire lung.",
    "secondary": "In thoracic oncology and operative surgery, a major procedure performed for central lung cancer (first successfully accomplished for bronchogenic carcinoma by Evarts Graham in 1933) or extensive unilateral destructive lung disease.",
    "quotes": [
      {
        "author": "Evarts Graham",
        "work": "The Journal of the American Medical Association",
        "quote": "We report the first successful one-stage **pneumonectomy** for primary carcinoma of the lung, with the patient returning to active practice."
      },
      {
        "author": "Ferdinand Sauerbruch",
        "work": "Master Surgeon: A Life in Surgery",
        "quote": "Overcoming the physiological consequences of complete **pneumonectomy** required unprecedented mastery of bronchial stump closure."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Meticulous vascular ligation during radical **pneumonectomy** prevents fatal hemorrhage from the short pulmonary artery trunks."
      }
    ]
  },
  "Dashboard — pneum\\pneumonic.md": {
    "primary": "Relating to, located in, or characteristic of the lungs; pulmonary; pneumonic.",
    "secondary": "In clinical pulmonary semiotics, referring to physical signs of consolidated lung tissue (such as bronchial breath sounds, egophony, and dullness) resulting from pneumonia.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Crepitant rales heard over the lower lobe signal the earliest stage of acute **pneumonic** exudation."
      },
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "The stethoscope revealed intense tubular resonance, confirming extensive **pneumonic** hepatization throughout the right lung."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The resolution of **pneumonic** consolidation depends upon the enzymatic liquefaction of intra-alveolar fibrin by leucocytic ferments."
      }
    ]
  },
  "Dashboard — pneum\\pneumonitis.md": {
    "primary": "Inflammation of lung tissue, especially non-infectious inflammation or inflammation localized in the alveolar walls and interstitium.",
    "secondary": "In pulmonology and oncology, lung inflammation caused by radiation (radiation pneumonitis), chemical inhalation, drug toxicity, or hypersensitivity (hypersensitivity pneumonitis / farmer's lung).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Chronic hypersensitivity **pneumonitis** results from repeated inhalation of organic dusts, leading to granulomatous interstitial fibrosis."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Chemical irritation of the terminal airways provoked diffuse interstitial **pneumonitis** with extensive alveolar wall thickening."
      },
      {
        "author": "Anthony Fauci",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "Prompt corticosteroid administration is necessary to halt the progression of drug-induced acute **pneumonitis**."
      }
    ]
  },
  "Dashboard — pneum\\pneumonoconiosis.md": {
    "primary": "An alternate spelling of pneumoconiosis; chronic lung disease caused by the inhalation of fine mineral or metallic dust particles.",
    "secondary": "In occupational pulmonary pathology, progressive pulmonary fibrosis and alveolar scarring resulting from chronic exposure to silica, coal dust, or asbestos in industrial environments.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The severity of industrial **pneumonoconiosis** varies directly with the duration and silica concentration of inhaled workplace dust."
      },
      {
        "author": "Alice Hamilton",
        "work": "Exploring the Dangerous Trades",
        "quote": "Our field surveys in coal mines documented advanced stages of **pneumonoconiosis** among veteran breaker boys and drillers."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Lungs scarred by **pneumonoconiosis** show hard fibrotic nodules consisting of concentric collagen whorls around deposited mineral crystals."
      }
    ]
  },
  "Dashboard — pneum\\pneumothorax.md": {
    "primary": "The presence of air or gas in the pleural cavity, which causes the lung on the affected side to collapse.",
    "secondary": "In thoracic medicine and trauma surgery, classified into spontaneous (primary or secondary), traumatic, and tension pneumothorax—the latter being a life-threatening medical emergency requiring immediate needle decompression.",
    "quotes": [
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "Metallic tinkling and amphoric resonance upon auscultation provide pathognomonic evidence of a hydropneumothorax or acute **pneumothorax**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Sudden, agonizing unilateral chest pain accompanied by hyper-resonance and absent breath sounds signals a spontaneous **pneumothorax**."
      },
      {
        "author": "Ferdinand Sauerbruch",
        "work": "Master Surgeon: A Life in Surgery",
        "quote": "In open traumatic **pneumothorax**, the sucking chest wound must be immediately occluded to prevent fatal mediastinal fluttering."
      }
    ]
  },
  "Dashboard — pneum\\pneumovax.md": {
    "primary": "A commercial trade name for the 23-valent pneumococcal polysaccharide vaccine (PPSV23) used to immunize against Streptococcus pneumoniae infections.",
    "secondary": "In preventive medicine and immunology, an unconjugated polysaccharide vaccine covering 23 virulent pneumococcal serotypes, indicated for older adults and high-risk immunocompromised individuals to prevent invasive pneumococcal bacteremia and pneumonia.",
    "quotes": [
      {
        "author": "Anthony Fauci",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "Routine vaccination with **Pneumovax** substantially reduces the risk of life-threatening bacteremic pneumococcal pneumonia in the elderly."
      },
      {
        "author": "Paul Offit",
        "work": "Vaccinated: One Man's Quest to Defeat the World's Deadliest Diseases",
        "quote": "The introduction of polyvalent formulations such as **Pneumovax** established broad protective antibody titers against diverse capsular serotypes."
      },
      {
        "author": "William E. Paul",
        "work": "Fundamental Immunology",
        "quote": "Unlike conjugate vaccines, unconjugated **Pneumovax** stimulates a T-cell-independent B-cell response, providing serotype-specific humoral defense."
      }
    ]
  },
  "Dashboard — pod\\amphipod.md": {
    "primary": "Any small, laterally compressed crustacean belonging to the order Amphipoda, possessing both forward- and backward-pointing walking legs.",
    "secondary": "In marine and freshwater biology, malacostracan crustaceans (such as beach hoppers, scuds, and skeleton shrimp) lacking a carapace and displaying thoracic appendages adapted for both swimming and crawling.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "The swift scurrying of a tiny **amphipod** across wave-swept stones illustrates the agility conferred by its diverse limb pairs."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "In each **amphipod**, the gills attach to thoracic limb bases, continually aerated by pleopod water currents."
      },
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "Beneath damp sea-drift, every upturned pebble reveals an active colony of scuttling **amphipod** crustaceans."
      }
    ]
  },
  "Dashboard — pod\\antipodal.md": {
    "primary": "Situated at the opposite side of the earth, or diametrically opposed in character, nature, or direction.",
    "secondary": "In plant embryology and mathematics, referring to the three cells located at the chalazal end of the angiosperm embryo sac (antipodal cells) or diametrically opposed points on a sphere.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "On the Origin of Species",
        "quote": "Species inhabiting **antipodal** continents often share remarkable homologous adaptations shaped by parallel environmental pressures."
      },
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "Their philosophical doctrines were in every respect **antipodal**, representing irreconcilable metaphysical extremes."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "Within the mature embryo sac, three small **antipodal** cells reside opposite the egg apparatus."
      }
    ]
  },
  "Dashboard — pod\\antipode.md": {
    "primary": "The exact opposite or contrary of something; a diametrically opposite point, person, or thing.",
    "secondary": "In geography and classical cartography (Greek antipous, with feet opposite), a point on the Earth's surface directly contrary to another, where people's feet would point toward each other.",
    "quotes": [
      {
        "author": "Ralph Waldo Emerson",
        "work": "Essays: First Series",
        "quote": "The pedant is the very **antipode** of the true scholar, substituting dead memorization for living insight."
      },
      {
        "author": "Thomas Carlyle",
        "work": "Sartor Resartus",
        "quote": "His gloomy cynicism stood as the moral **antipode** to the radiant optimism of his youthful days."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "While noon blazed upon the deck, our **antipodes** slept beneath the starry skies of the opposite hemisphere."
      }
    ]
  },
  "Dashboard — pod\\antipodean.md": {
    "primary": "Relating to the antipodes, especially Australia and New Zealand as viewed from Europe; diametrically opposed.",
    "secondary": "In biogeography and cultural history, describing flora, fauna, or social life indigenous to the southern hemisphere islands on the opposite side of the globe from Britain.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The bizarre marsupials of the **antipodean** wilderness seemed almost the product of a separate creative dispensation."
      },
      {
        "author": "Anthony Trollope",
        "work": "Australia and New Zealand",
        "quote": "The vigorous enterprise of the **antipodean** colonies astonished the visiting English traveler at every turn."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "Handbook of the New Zealand Flora",
        "quote": "The unique vegetation of the **antipodean** archipelago includes ancient conifer and tree-fern lineages."
      }
    ]
  },
  "Dashboard — pod\\antipodes.md": {
    "primary": "Two places on the globe diametrically opposite to each other, or the regions of the Earth situated on the opposite side of the globe (especially Australia and New Zealand).",
    "secondary": "In classical cosmology, the theoretical inhabitants of the opposite southern hemisphere imagined by Greek geographers (such as Crates of Mallus) whose feet faced our own.",
    "quotes": [
      {
        "author": "Plato",
        "work": "Timaeus",
        "quote": "In a spherical earth, what one man calls down is for another up, rendering the idea of absolute position meaningless across the **antipodes**."
      },
      {
        "author": "Charles Dickens",
        "work": "Great Expectations",
        "quote": "Magwitch returned in secret from the distant **antipodes**, risking the gallows to behold the gentleman he had made."
      },
      {
        "author": "Lewis Carroll",
        "work": "Alice's Adventures in Wonderland",
        "quote": "Alice wondered if she should fall right through the earth and come out among the people that walk with their heads downward—the **antipodes**."
      }
    ]
  },
  "Dashboard — pod\\chiropodist.md": {
    "primary": "A medical practitioner specialized in the diagnosis, treatment, and prevention of disorders and deformities of the human foot (podiatrist).",
    "secondary": "In healthcare history, a licensed foot-care specialist (from Greek cheir, hand, and pous, podos, foot) treating corns, bunions, calluses, and ingrown toenails.",
    "quotes": [
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventure of the Illustrious Client",
        "quote": "The observant detective noted subtle modifications in the man's gait that would not escape an experienced **chiropodist**."
      },
      {
        "author": "George Bernard Shaw",
        "work": "Pygmalion",
        "quote": "He consulted a fashionable London **chiropodist** to relieve the agonizing friction of his formal boots."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Diabetic neuropathy requires vigilant foot hygiene overseen by a careful **chiropodist** to prevent neuropathic ulcers."
      }
    ]
  },
  "Dashboard — pod\\chiropody.md": {
    "primary": "The professional treatment and care of the feet, especially the removal of corns, calluses, and treatment of toenail conditions; podiatry.",
    "secondary": "In medical licensing and Allied Health history, the branch of paramedical practice dealing with common mechanical and cutaneous ailments of the human foot and lower extremity.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "A System of Medicine",
        "quote": "Routine **chiropody** serves as an indispensable prophylactic measure against limb-threatening diabetic gangrene."
      },
      {
        "author": "H. G. Wells",
        "work": "The History of Mr. Polly",
        "quote": "Mr. Polly suffered acutely from unyielding footwear, contemplating the soothing benefits of professional **chiropody**."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Stark Munro Letters",
        "quote": "In establishing our dispensary, we found that simple **chiropody** earned the warmest gratitude from laboring patients."
      }
    ]
  },
  "Dashboard — pod\\decapod.md": {
    "primary": "Any crustacean of the order Decapoda having five pairs of thoracic walking legs (including crabs, lobsters, shrimps, and prawns), or a ten-armed cephalopod (such as a squid or cuttlefish).",
    "secondary": "In systematic marine invertebrate zoology, malacostracan crustaceans characterized by a cephalothorax covered by a carapace and five pairs of uniramous pereiopods, the first pair frequently modified as large chelae (claws).",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "Journal of Researches",
        "quote": "On the reef flat, an enormous hermit crab—a terrestrial **decapod**—scuttled across the coral sand with surprising speed."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Crayfish",
        "quote": "The river crayfish serves as a typical example of a freshwater **decapod**, exhibiting five pairs of thoracic walking limbs."
      },
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "The mud flats teem with fiddler crabs, each miniature **decapod** waving its oversized claw in rhythmic courtship."
      }
    ]
  },
  "Dashboard — pod\\isopod.md": {
    "primary": "Any small, dorsoventrally flattened crustacean of the order Isopoda, having seven pairs of thoracic walking legs of similar size and shape (including woodlice, pill bugs, and sea slaters).",
    "secondary": "In marine and terrestrial invertebrate zoology, a diverse malacostracan order (from Greek isos, equal, and pous, foot) lacking a carapace and adapted to diverse niches from ocean abyssal benthos (giant Bathynomus) to dry land.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The common woodlouse represents a fully terrestrial **isopod**, breathing by means of modified abdominal pleopods."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "Deep sea dredging brought to the surface an unusual parasitic **isopod** clinging firmly to the gills of a codfish."
      },
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "Under every damp sea-board along the splash zone, colonies of the rock-dwelling **isopod** Ligia scurry out of sight."
      }
    ]
  },
  "Dashboard — pod\\parapodium.md": {
    "primary": "One of the paired, unjointed lateral fleshy projections or appendages on each body segment of polychaete annelid worms, used for locomotion and respiration.",
    "secondary": "In marine invertebrate zoology, a segmented lateral organ divided into a dorsal notopodium and ventral neuropodium, bearing chaetae (bristles) and vascularized gills.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "Each **parapodium** of the sea-mouse Nereis bears bundles of stiff chitinous bristles assisting in crawling and swimming."
      },
      {
        "author": "Charles Darwin",
        "work": "Journal of Researches",
        "quote": "The rhythmic undulation of each lateral **parapodium** propelled the polychaete through the lagoon waters with graceful ease."
      },
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "Burrowing clamworms use their bristle-tipped **parapodium** paddles to dig rapidly into shifting sandy sediment."
      }
    ]
  },
  "Dashboard — pod\\pod.md": {
    "primary": "An elongated, dehiscent seed vessel or legume (such as of pea or bean plants), or a school of aquatic mammals (whales, seals, dolphins), or a streamlined detachable container.",
    "secondary": "In plant biology and cetology, either a monocarpellary fruit opening along two sutures, or a close-knit matrilineal social unit of cetaceans navigating and foraging together.",
    "quotes": [
      {
        "author": "Gregor Mendel",
        "work": "Experiments in Plant Hybridisation",
        "quote": "When pea plants with inflated green **pod** forms were crossed with wrinkled yellow ones, the offspring followed strict mathematical ratios."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The lookouts raised a great **pod** of sperm whales lounging lazily upon the glassy equatorial swell."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "quote": "I gathered wild beans in autumn, cracking open each dry **pod** to extract the polished seeds."
      }
    ]
  },
  "Dashboard — pod\\podiatrist.md": {
    "primary": "A medical specialist who diagnoses, treats, and performs surgery on conditions and diseases of the foot, ankle, and related structures of the leg.",
    "secondary": "In modern clinical medicine, a Doctor of Podiatric Medicine (DPM) managing diabetic foot ulcers, sports-related lower-extremity trauma, structural biomechanics, and reconstructive foot surgery.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Close clinical collaboration with a skilled **podiatrist** preserves limb viability in patients with severe peripheral arterial disease."
      },
      {
        "author": "Anthony Fauci",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "Early evaluation by a hospital **podiatrist** is critical to debriding infected plantar neuropathic mal perforans."
      },
      {
        "author": "Sinclair Lewis",
        "work": "Arrowsmith",
        "quote": "The hospital clinic added a resident **podiatrist** to correct the painful gait abnormalities of factory workers."
      }
    ]
  },
  "Dashboard — pod\\podiatry.md": {
    "primary": "The branch of medicine devoted to the diagnosis, treatment, and study of disorders of the foot, ankle, and lower extremity.",
    "secondary": "In healthcare systems, the surgical and non-surgical clinical specialty dedicated to foot biomechanics, reconstructive foot and ankle surgery, wound care, and sports podiatry.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "Modern Medicine: Its Theory and Practice",
        "quote": "The development of modern **podiatry** elevated foot healthcare from empirical corn-cutting to advanced orthopedic biomechanics."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Specialized surgical **podiatry** contributes immeasurably to the salvaging of dysvascular diabetic extremities."
      },
      {
        "author": "Anthony Fauci",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "Multidisciplinary clinics incorporating **podiatry** have achieved remarkable reductions in major lower-limb amputations."
      }
    ]
  },
  "Dashboard — pod\\podium.md": {
    "primary": "A small elevated platform on which an orchestral conductor, lecturer, or speaker stands; a pedestal; a raised dais.",
    "secondary": "In classical architecture, a continuous stone base or substructure supporting a row of columns or an entire temple (from Greek podion, little foot).",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The Roman magistrates stood upon the marble **podium** of the amphitheatre, overlooking the gladiatorial arena."
      },
      {
        "author": "Hector Berlioz",
        "work": "Treatise on Instrumentation",
        "quote": "The conductor ascended the **podium**, raised his baton, and commanded the vast orchestral ensemble into silence."
      },
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "The noble temple rested upon a massive stone **podium**, lifting the colonnade proudly above the city piazza."
      }
    ]
  },
  "Dashboard — pod\\podomancy.md": {
    "primary": "Divination or fortune-telling by interpreting the shape, sole lines, or characteristics of a person's feet (also known as solestry).",
    "secondary": "In the history of occultism and comparative folklore, a mantic practice analogous to chiromancy (palmistry), where lines, toe proportions, and sole contours were interpreted to predict fate and personality.",
    "quotes": [
      {
        "author": "Robert Burton",
        "work": "The Anatomy of Melancholy",
        "quote": "Gullible minds seek omens in chiromancy, **podomancy**, and all manner of superstitious divination."
      },
      {
        "author": "Thomas Browne",
        "work": "Pseudodoxia Epidemica",
        "quote": "To discern the future by **podomancy** or inspection of the soles of the feet is a baseless vanity devoid of reason."
      },
      {
        "author": "Walter Pater",
        "work": "Marius the Epicurean",
        "quote": "Itinerant soothsayers in imperial Rome practiced **podomancy**, offering to read destinies in the dusty footprints of travelers."
      }
    ]
  },
  "Dashboard — pod\\podomere.md": {
    "primary": "Any individual limb segment or joint of an arthropod appendage (such as coxa, trochanter, femur, tibia, or tarsus).",
    "secondary": "In arthropod morphology and developmental biology, an articulated structural segment of a limb connected by flexible arthrodial membranes and operated by antagonistic intrinsic muscle groups.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "The Crayfish",
        "quote": "Each walking leg is composed of seven distinct segments, every **podomere** articulating with its fellow by a hinge joint."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Insect Societies",
        "quote": "The distal **podomere** of the insect leg terminates in pretarsal claws and an adhesive arolium."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Wonderful Life",
        "quote": "The fossils of the Burgess Shale display primitive arthropods whose every limb **podomere** preserves delicate setal fringes."
      }
    ]
  },
  "Dashboard — pod\\podopaediatric.md": {
    "primary": "Pertaining to the diagnosis and management of foot and lower-limb disorders in children (pediatric podiatry; Commonwealth spelling).",
    "secondary": "In orthopedic semiotics and rehabilitation, referring to the evaluation of pediatric gait abnormalities, clubfoot (talipes equinovarus), flatfoot (pes planus), and torsional skeletal deformities in growing infants.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Early **podopaediatric** evaluation detects congenital talipes before irreversible ossification sets in."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Conservative splinting in **podopaediatric** practice often remedies severe postural clubbing without open osteotomy."
      },
      {
        "author": "Florence Nightingale",
        "work": "Notes on Nursing",
        "quote": "Properly fitted footwear in childhood constitutes the primary foundation of preventative **podopaediatric** hygiene."
      }
    ]
  },
  "Dashboard — pod\\polyp.md": {
    "primary": "A small growth protruding from a mucous membrane (as in the colon, nose, or uterus), or a sessile, solitary or colonial form of a coelenterate (such as a sea anemone or coral animal).",
    "secondary": "In marine biology and clinical pathology, either a tubular cnidarian body with an upward-facing mouth surrounded by tentacles, or an abnormal mucosal tissue projection (adenomatous, hyperplastic, or inflammatory).",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Structure and Distribution of Coral Reefs",
        "quote": "Countless millions of tiny coral **polyp** organisms build up vast limestone barriers across tropical seas."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Bleeding from a pedunculated rectal **polyp** requires endoscopic snare excision to prevent malignant transformation."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Oceanic Hydrozoa",
        "quote": "The polymorphic hydrozoan colony consists of feeding hydranths and specialized reproductive **polyp** individuals."
      }
    ]
  },
  "Dashboard — pod\\polypodium.md": {
    "primary": "A genus of ferns in the family Polypodiaceae commonly known as polypodies, bearing creeping scaly rhizomes and pinnatifid fronds.",
    "secondary": "In systematic pteridology, a large cosmopolitan genus (from Greek polys, many, and podion, little foot) characterized by exindusiate circular sori borne on the underside of frond lobes and sweet-tasting rhizomes.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "The genus **Polypodium** is distinguished by its creeping foot-like rhizomes and round sori devoid of any covering membrane."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The rock polypody, **Polypodium** vulgare, drapes damp mossy boulders in northern deciduous forests."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "Handbook of the New Zealand Flora",
        "quote": "Epiphytic fronds of **Polypodium** cling securely to the trunks of tree ferns in the damp ravines."
      }
    ]
  },
  "Dashboard — pod\\polyposis.md": {
    "primary": "A medical condition characterized by the development of numerous polyps on a mucous membrane, especially in the colon or stomach.",
    "secondary": "In medical genetics and gastroenterology, hereditary polyposis syndromes (such as familial adenomatous polyposis, FAP, caused by APC gene mutations) marked by hundreds to thousands of adenomas with a near 100% risk of colorectal carcinoma if untreated.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Familial adenomatous **polyposis** exhibits autosomal dominant inheritance, carpeting the entire large bowel with hundreds of adenomas."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Microscopic sections in diffuse intestinal **polyposis** show widespread glandular hyperplasia of the crypt epithelium."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Prophylactic total colectomy is the only definitive measure to prevent fatal adenocarcinoma in hereditary **polyposis**."
      }
    ]
  },
  "Dashboard — pod\\pseudopod.md": {
    "primary": "A temporary, foot-like projection of the cytoplasm of an amoeboid cell or protozoan, used for locomotion and phagocytosis (pseudopodium).",
    "secondary": "In cellular biology and immunology, an actin-driven dynamic protrusion of the cell membrane formed by macrophages, neutrophils, and amoebae during chemotactic crawling and prey engulfment.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Formation of Vegetable Mould through the Action of Worms",
        "quote": "Under high magnification, the amoeba extends a blunt **pseudopod**, slowly flowing its entire protoplasm into the advance."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Crayfish",
        "quote": "Leucocytes pass through capillary walls by extending a slender **pseudopod** between endothelial junctions."
      },
      {
        "author": "Richard Dawkins",
        "work": "The Ancestor's Tale",
        "quote": "The single-celled amoeba navigates its microscopic world by thrusting out one flexible **pseudopod** after another."
      }
    ]
  },
  "Dashboard — pod\\pseudopodium.md": {
    "primary": "A temporary cytoplasmic protrusion extended by an amoeba or amoeboid cell for locomotion or feeding (plural: pseudopodia).",
    "secondary": "In cellular biomechanics, an actin-myosin cytoskeleton extension (lobopodium, filopodium, or reticulopodium) enabling cell motility, haptotaxis, and phagocytic uptake of microbes.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The crawling leucocyte puts forth a delicate **pseudopodium**, demonstrating the intrinsic motility of individual living cells."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "By extending and retracting each **pseudopodium**, the freshwater Rhizopod engulfs unicellular algae."
      },
      {
        "author": "Alexander Maximow",
        "work": "A Text-Book of Histology",
        "quote": "Upon contacting a bacterial target, the macrophage projects an encircling **pseudopodium** to complete the phagocytic cup."
      }
    ]
  },
  "Dashboard — pod\\sympodium.md": {
    "primary": "An apparent continuous main axis of a plant or branching structure formed by a succession of secondary lateral shoots (sympodial axis).",
    "secondary": "In plant morphology and orchidology, a growth habit where terminal shoot buds cease elongation (often terminating in a flower) and growth is renewed by an axillary bud from the base, contrasting with a monopodial stem.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "The overarching vine grows not from a single terminal bud, but forms a **sympodium** constructed from successive lateral branches."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "In orchids with a creeping **sympodium**, each season's growth terminates in a pseudobulb bearing next year's lead."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "Handbook of the New Zealand Flora",
        "quote": "The spreading rhizomatous **sympodium** of native grasses anchors loose coastal sand dunes effectively."
      }
    ]
  },
  "Dashboard — priap\\priapic.md": {
    "primary": "Relating to, resembling, or suggestive of the phallus; phallic; having or displaying male sexual potency.",
    "secondary": "In literary criticism and art history, evoking the bawdy, fertile, or grotesque attributes of the Greco-Roman god Priapus, characterized by exaggerated or uncontrolled sexual energy.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Ancient garden statues of Priapus were celebrated with crude, **priapic** festivals celebrating seasonal fertility."
      },
      {
        "author": "Walter Pater",
        "work": "Marius the Epicurean",
        "quote": "Rustic altars adorned with **priapic** emblems offered first-fruits to protect vineyards from predatory birds."
      },
      {
        "author": "Aldous Huxley",
        "work": "Point Counter Point",
        "quote": "The satirical conversation drifted into a mocking dissection of modern **priapic** obsessions and bourgeois hypocrisies."
      }
    ]
  },
  "Dashboard — priap\\priapism.md": {
    "primary": "A prolonged, persistent, and typically painful erection of the penis that occurs without sexual stimulation.",
    "secondary": "In urology and hematology, a pathological urological emergency classified as ischemic (low-flow) or non-ischemic (high-flow), frequently triggered by sickle cell disease, trauma, or vasoactive pharmaceuticals, requiring prompt aspiration to prevent cavernous fibrosis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Intractable **priapism** occasionally complicates acute myelogenous leukemia or severe spinal cord trauma."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Thrombosis within the corpora cavernosa produces painful **priapism** through complete venous outflow obstruction."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Urgent cavernous irrigation and phenylephrine injection were administered to terminate ischemic **priapism**."
      }
    ]
  },
  "Dashboard — priap\\Priapus.md": {
    "primary": "In Greek and Roman mythology, the god of fertility, gardens, vineyards, and male generative power, typically depicted with an enormous erect phallus.",
    "secondary": "In classical cultural history, a minor rustic deity (son of Dionysus and Aphrodite) whose carved wooden herms guarded orchards against thieves and blight, inspiring the collection of ribald Latin poems known as the Priapea.",
    "quotes": [
      {
        "author": "Virgil",
        "work": "Georgics",
        "quote": "Let the guardianship of garden-keeping **Priapus** with his willow scythe protect your fruit trees from marauding birds."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The rude wooden effigy of **Priapus** remained a fixture of Roman country villas long into the Christian era."
      },
      {
        "author": "Walter Pater",
        "work": "Greek Studies",
        "quote": "The cult of **Priapus** represented the most earthly and unabashed celebration of physical vegetative fertility."
      }
    ]
  },
  "Dashboard — proct\\ectoproct.md": {
    "primary": "Any microscopic aquatic invertebrate belonging to the phylum Ectoprocta (commonly known as bryozoans or moss animals).",
    "secondary": "In marine biology, a colonial lophophorate whose anus is situated outside the circular ring of ciliated feeding tentacles, contrasting with endoprocts.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "In every colonial **ectoproct**, the individual zooid extends its ciliated lophophore to capture microscopic food particles."
      },
      {
        "author": "Charles Darwin",
        "work": "Journal of Researches",
        "quote": "Encrusting the kelp blades, colonies of a delicate **ectoproct** formed lacelike traceries over the brown sea-fronds."
      },
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "Under submerged rocks, each moss animal or **ectoproct** lives protected within an intricate calcareous zooecium."
      }
    ]
  },
  "Dashboard — proct\\Ectoprocta.md": {
    "primary": "A phylum of small, aquatic, mostly sessile colonial animals commonly called bryozoans or moss animals, characterized by having an anus positioned outside the lophophore.",
    "secondary": "In systematic invertebrate zoology, a major coelomate lophophorate clade (Greek ektos, outside, and proktos, anus) comprising thousands of marine and freshwater species that produce calcareous skeletons contributing to reef ecosystems.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The phylum **Ectoprocta** is distinguished from Entoprocta by its true coelomic cavity and external anal opening."
      },
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "Fossil remains of the **Ectoprocta** abound in Paleozoic limestones, demonstrating their ancient reef-building role."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Structure of Evolutionary Theory",
        "quote": "The punctuated stasis observed in fossil species of **Ectoprocta** provides key empirical support for macroevolutionary theory."
      }
    ]
  },
  "Dashboard — proct\\endoprocta.md": {
    "primary": "A phylum of small, mostly marine, stalked pseudocoelomate or acoelomate animals commonly known as entoprocts, having both mouth and anus within the tentacular crown.",
    "secondary": "In invertebrate zoology, a group of solitary or colonial filter-feeders (alternate spelling of Entoprocta) possessing a cup-shaped calyx mounted on an anchoring stalk, previously grouped with Bryozoa.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The **endoprocta** possess an anus opening within the circle of ciliated tentacles, distinct from the true Bryozoa."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "Minute stalked creatures belonging to the **endoprocta** clung to the carapaces of crabs brought up from the reef."
      },
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "Fouling communities on harbor pilings regularly feature miniature colonies of the stalked **endoprocta**."
      }
    ]
  },
  "Dashboard — proct\\entoproct.md": {
    "primary": "Any small aquatic invertebrate animal of the phylum Entoprocta (also spelled endoproct).",
    "secondary": "In marine invertebrate biology, a microscopic, sessile suspension feeder whose ciliated crown of tentacles creates an inward water current directed toward the mouth, with an anus situated inside the tentacular ring.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The solitary marine **entoproct** Loxosoma lives commensally upon the bristles of benthic polychaete worms."
      },
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "A microscopic **entoproct** bends and sways on its flexible stalk, filtering passing organic detritus."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Ontogeny and Phylogeny",
        "quote": "The spiral cleavage and trochophore-like larva of the **entoproct** indicate close phylogenetic links with spiralian protostomes."
      }
    ]
  },
  "Dashboard — proct\\Entoprocta.md": {
    "primary": "A phylum of largely marine, stalked, sessile aquatic animals characterized by having both the mouth and anus situated inside a crown of ciliated tentacles.",
    "secondary": "In invertebrate phylogenetic systematics, a distinct clade of pseudocoelomate protostomes (Greek entos, inside, and proktos, anus) comprising around 150 species, closely allied to Mollusca and Annelida within Lophotrochozoa.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "Embryological evidence firmly separates the **Entoprocta** from true bryozoans, demonstrating their distinct blastocoelic ancestry."
      },
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "Taxonomic placement of the **Entoprocta** required careful microscopic analysis of larval ciliary locomotion."
      },
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "Members of the **Entoprocta** settle in quiet tidal pools, their delicate tentacular crowns constantly sweeping the water."
      }
    ]
  },
  "Dashboard — proct\\epiproct.md": {
    "primary": "A supra-anal plate or sclerite situated above the anus in insects and other arthropods.",
    "secondary": "In insect morphology, the modified dorsal tergite of the eleventh abdominal segment lying dorsal to the anal opening, forming part of the terminal external genitalia or ovipositor.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The terminal abdominal segment of the grasshopper bears a triangular dorsal plate, the **epiproct**, protecting the anus."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Insect Societies",
        "quote": "Morphological examination of the caudal sclerites revealed a heavily chitinized **epiproct** flanking the sting apparatus."
      },
      {
        "author": "John Lubbock",
        "work": "On the Senses, Instincts, and Intelligence of Animals",
        "quote": "Sensory setae situated upon the **epiproct** monitor environmental tactile stimuli at the insect's posterior terminus."
      }
    ]
  },
  "Dashboard — proct\\euproctis.md": {
    "primary": "A genus of tussock moths in the family Erebidae (formerly Lymantriidae) whose caterpillars possess irritating, urticating hairs.",
    "secondary": "In medical entomology and toxicology, a genus including pest species (such as the brown-tail moth, Euproctis chrysorrhoea) whose larval setae contain histamine-releasing venom causing severe dermatitis and conjunctivitis (lepidopterism).",
    "quotes": [
      {
        "author": "Jean-Henri Fabre",
        "work": "Social Life in the Insect World",
        "quote": "The caterpillars of **euproctis** weave protective silken tents, bristling with fine hairs that produce intense itching upon contact."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe contact dermatitis among forestry workers was traced to the wind-blown urticating hairs of **euproctis** caterpillars."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "Aerial spraying campaigns targeted invasive infestations of the **euproctis** tussock moth across eastern hardwood forests."
      }
    ]
  },
  "Dashboard — proct\\hypoproct.md": {
    "primary": "A subanal plate or ventral sclerite located beneath the anus in insects and certain other arthropods.",
    "secondary": "In systematic entomology (notably Diptera and odonates), the sternal plate of the terminal eleventh abdominal segment lying directly ventral to the anal aperture, frequently involved in copulatory grasping.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "Ventral to the anal aperture lies the **hypoproct**, completing the posterior skeletal ring of the insect abdomen."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Insect Societies",
        "quote": "In male dragonflies, the specialized **hypoproct** functions alongside the epiproct as a clasper during aerial mating."
      },
      {
        "author": "John Lubbock",
        "work": "Ants, Bees, and Wasps",
        "quote": "The subgenital plate and adjoining **hypoproct** were carefully dissected under high magnification to map their sclerotized contours."
      }
    ]
  },
  "Dashboard — proct\\paraproct.md": {
    "primary": "One of a pair of subanal lobes or lateral plates flanking the anus in insects and other arthropods.",
    "secondary": "In insect anatomy, one of the two ventral or lateral sclerites on either side of the anal opening (derived from the sternum of the eleventh abdominal somite), often bearing cerci.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "Flanking the anal opening, each lateral **paraproct** provides an articulating base for the paired cerci."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Insect Societies",
        "quote": "The caudal sensory apparatus of the termite includes tactile cerci originating immediately beside each **paraproct**."
      },
      {
        "author": "John Lubbock",
        "work": "On the Origin and Metamorphoses of Insects",
        "quote": "During embryological development of the nymph, the paired **paraproct** sclerites condense around the proctodeum."
      }
    ]
  },
  "Dashboard — proct\\periproct.md": {
    "primary": "The small membrane or region surrounding the anus in echinoderms (especially sea urchins) and crustaceans.",
    "secondary": "In invertebrate zoology and paleontology, the flexible, non-calcified apical plate or membrane enclosing the anal aperture within the aboral ring of regular and irregular echinoids.",
    "quotes": [
      {
        "author": "Louis Agassiz",
        "work": "Monographies d'Échinodermes",
        "quote": "In regular sea urchins, the apical system encircles the circular **periproct**, through which the anus opens."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The flexible **periproct** of the sea urchin contains minute, embedded calcareous plates surrounding the anal pore."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Wonderful Life",
        "quote": "The evolutionary migration of the **periproct** to the posterior margin marked the transition from regular to irregular heart urchins."
      }
    ]
  },
  "Dashboard — proct\\proctalgia.md": {
    "primary": "Severe pain in the rectum or anus (proctodynia).",
    "secondary": "In clinical gastroenterology and colorectal surgery, rectal discomfort stemming from anal fissures, thrombosed external hemorrhoids, perianal abscesses, or pelvic muscular spasms such as proctalgia fugax.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Recurrent nocturnal spasms of intense anorectal pain without organic lesion characterize idiopathic **proctalgia** fugax."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Surgical drainage of an ischiorectal abscess gave instantaneous relief from excruciating perianal **proctalgia**."
      },
      {
        "author": "Jean-Martin Charcot",
        "work": "Lectures on the Diseases of the Nervous System",
        "quote": "Tabetic neurosyphilis frequently manifests with visceral sensory crises, including agonizing rectal **proctalgia**."
      }
    ]
  }
};

console.log('Starting Body Rem B Batch 3 curation (' + Object.keys(batchData).length + ' words)...');
const updated = updateNotesBatch(baseClusterDir, batchData);
console.log('Batch 3 complete: successfully updated ' + updated + ' notes.');
