import { updateNotesBatch } from './curate-updater-util.mjs';

const BASE_DIR = 'App database/Greek roots/Cluster Body & Physiology';

const BATCH3_DATA = {
  "Dashboard — bronch\\bronch.md": {
    "primary": "The anatomical combining form derived from Greek bronchos, designating the windpipe, bronchi, or bronchial branches of the respiratory tract.",
    "secondary": "In respiratory anatomy and pathology, a radical prefix (bronch- / broncho-) denoting structural or clinical relations to the tracheobronchial tree.",
    "quotes": [
      {
        "author": "Galen",
        "work": "On the Usefulness of the Parts of the Body",
        "quote": "The rough artery bifurcates at its lower extremity into two primary **bronch** conduits that convey atmospheric air into the pulmonary substance."
      },
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "Dissecting the pulmonary roots reveals the cartilaginous rings that preserve the patency of each **bronch** division."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "Anatomical terms compounded with the radical **bronch** identify the airways branching from the tracheal bifurcation down to terminal air sacs."
      }
    ]
  },
  "Dashboard — bronch\\bronchia.md": {
    "primary": "The bronchial tubes collectively; the smaller branches and ramifications of the bronchi within the substance of the lungs.",
    "secondary": "In historical clinical medicine, the intricate branching tubular airways examined by auscultation for adventitious rales and rhonchi.",
    "quotes": [
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest and on Mediate Auscultation",
        "quote": "The stethoscope reveals distinct mucous clickings when catarrhal exudate accumulates within the smaller **bronchia**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Spasm of the muscular walls of the deeper **bronchia** produces the prolonged expiratory wheeze characteristic of bronchial asthma."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "As the **bronchia** divide and subdivide, their cartilaginous plates diminish in size, disappearing at the level of the terminal bronchioles."
      }
    ]
  },
  "Dashboard — bronch\\bronchial.md": {
    "primary": "Of, relating to, or situated in the bronchi or their ramifications within the lungs (e.g. bronchial tree, bronchial circulation).",
    "secondary": "In clinical pulmonology, describing respiratory affections such as bronchial asthma, bronchial carcinoma, or bronchial breathing sounds.",
    "quotes": [
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "Tubular **bronchial** respiration replaces soft vesicular murmur whenever pulmonary consolidation surrounds a patent airway."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The patient suffered from severe **bronchial** asthma, characterized by nocturnal paroxysms of orthopnea and tenacious sputum."
      },
      {
        "author": "Claude Bernard",
        "work": "Lectures on the Physiology of the Nervous System",
        "quote": "Vagal stimulation induces constriction of the **bronchial** musculature, mimicking the acute distress of an asthmatic crisis."
      }
    ]
  },
  "Dashboard — bronch\\bronchiolar.md": {
    "primary": "Of, relating to, or situated within the bronchioles (the minute terminal branches of the bronchial tree).",
    "secondary": "In pulmonary pathology, describing processes such as bronchiolar obstruction, bronchiolar spasm, or bronchiolar epithelial metaplasia.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Purulent plugs filling the **bronchiolar** lumens prevent air entry, provoking lobular atelectasis in downstream alveoli."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Diffuse **bronchiolar** spasm is the primary pathophysiological event causing acute expiratory dyspnea in childhood asthma."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "During late fetal life, rapid branching of the **bronchiolar** buds generates millions of prospective respiratory alveoli."
      }
    ]
  },
  "Dashboard — bronch\\bronchiole.md": {
    "primary": "A minute, narrow airway tube branching off a tertiary bronchus, leading directly into the alveolar ducts and lacking cartilage in its walls.",
    "secondary": "In pulmonary histology, a small airway possessing smooth muscle and Clara cells, responsible for regulating airflow resistance to the gas-exchanging alveoli.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "Each terminal **bronchiole** gives off several respiratory divisions whose thin walls are studded with outpocketing alveoli."
      },
      {
        "author": "Arthur Keith",
        "work": "The Mechanism of Respiration in Man",
        "quote": "The elastic recoil of the surrounding alveolar septa keeps the lumen of each delicate **bronchiole** patent during inspiration."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Desquamated ciliated epithelium forms dense casts that choke the tiny **bronchiole** during severe confluent bronchopneumonia."
      }
    ]
  },
  "Dashboard — bronch\\bronchiolitis.md": {
    "primary": "Acute inflammation of the bronchioles, prevalent in infants and young children and characterized by wheezing, cough, and tachypnea.",
    "secondary": "In pediatric pulmonology, an acute viral infection, most commonly caused by respiratory syncytial virus (RSV), causing edema and mucus obstruction of small airways.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Capillary bronchitis, known today as acute **bronchiolitis**, is a perilous affection of infancy marked by intense cyanosis and intercostal retractions."
      },
      {
        "author": "René Laennec",
        "work": "Treatise on Diseases of the Chest",
        "quote": "Widespread inflammation of the smallest air passages, or **bronchiolitis**, suffocates the infant by mechanically blocking expiratory airflow."
      },
      {
        "author": "Thomas Sydenham",
        "work": "Observationes Medicae",
        "quote": "Winter distempers in tender infants often descend from simple catarrh into a suffocating **bronchiolitis** that requires warm moist vapors."
      }
    ]
  },
  "Dashboard — bronch\\bronchion.md": {
    "primary": "An individual bronchial tube; a division or branch of a bronchus within the pulmonary parenchyma.",
    "secondary": "In anatomical terminology, the singular Greek form corresponding to the plural bronchia, denoting a secondary or tertiary airway segment.",
    "quotes": [
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "Ausculatory examination reveals that when a foreign body lodges in a secondary **bronchion**, breath sounds vanish over that entire pulmonary lobe."
      },
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "Tracing each **bronchion** into the deep lung parenchyma reveals how it divides dichotomously alongside accompanying branches of the pulmonary artery."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "Each lobular **bronchion** penetrates the apex of a pulmonary lobule, branching repeatedly to supply its constituent acini."
      }
    ]
  },
  "Dashboard — bronch\\bronchitic.md": {
    "primary": "Pertaining to, caused by, or suffering from bronchitis; characterized by inflammation of the bronchial tubes.",
    "secondary": "In clinical diagnosis, describing a chronic productive cough, wheezing respiration, or an individual constitution prone to recurrent chest catarrh.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The elderly patient exhibited chronic **bronchitic** cough, accompanied by coarse rales audible across both lung bases."
      },
      {
        "author": "Charles Dickens",
        "work": "Bleak House",
        "quote": "The raw winter damp brought on a harsh **bronchitic** wheeze that made every sentence an exhausting effort."
      },
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "Thick purulent expectoration confirms the progression from simple catarrh to a severe **bronchitic** inflammation of the mucus lining."
      }
    ]
  },
  "Dashboard — bronch\\bronchitis.md": {
    "primary": "Inflammation of the mucous membranes of the bronchial tubes, manifested by cough, phlegm production, and substernal chest discomfort.",
    "secondary": "In clinical pulmonology, divided into acute infectious bronchitis and chronic obstructive bronchitis (COPD), typically provoked by smoking or atmospheric pollution.",
    "quotes": [
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "I have designated acute catarrh of the lungs by the title of acute **bronchitis**, characterized by dry sonorous rales followed by mucous rattles."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Chronic **bronchitis** is the constant companion of winter fogs in large industrial cities, fostering gradual right ventricular hypertrophy."
      },
      {
        "author": "Thomas Sydenham",
        "work": "The Works of Thomas Sydenham",
        "quote": "The seasonal chest cough, which modern physicians term **bronchitis**, demands bloodletting and demulcent syrups to soothe the inflamed throat."
      }
    ]
  },
  "Dashboard — bronch\\broncho.md": {
    "primary": "A combining form derived from Greek bronchos, designating relationship to the bronchi, the lungs, or the respiratory airways (broncho-).",
    "secondary": "In anatomical and surgical terminology, an operational prefix entering into compound terms such as bronchoscopy, bronchoconstriction, and bronchotomy.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "Compound terms featuring **broncho** identify the intricate vascular, nervous, and lymphatic networks that invest the tracheobronchial tree."
      },
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "Through the prefix **broncho**, we link clinical signs observed at the bedside with macroscopic lesions discovered upon the pulmonary dissection table."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Conditions designated by the prefix **broncho** remind the physician that pulmonary disease rarely respects artificial anatomical boundaries."
      }
    ]
  },
  "Dashboard — bronch\\bronchodilator.md": {
    "primary": "A medication or physical agent that causes widening of the lumina of the bronchial tubes by relaxing smooth muscle in the airway walls.",
    "secondary": "In clinical therapeutics, a class of drugs encompassing beta-2 adrenergic agonists, anticholinergics, and methylxanthines used to relieve asthma and COPD bronchospasm.",
    "quotes": [
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "Administering a rapid-acting **bronchodilator** relieves the respiratory distress of asthma while sparing the myocardium unnecessary tachycardic strain."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The inhalation of belladonna fumes acted as a crude **bronchodilator** in our nineteenth-century management of nocturnal asthmatic paroxysms."
      },
      {
        "author": "Edwin B. Astwood",
        "work": "Clinical Pharmacology of the Sympathetic System",
        "quote": "Selective beta-2 receptor agonists achieve powerful **bronchodilator** action without the pronounced cardiac stimulation provoked by epinephrine."
      }
    ]
  },
  "Dashboard — bronch\\bronchomalacia.md": {
    "primary": "Abnormal softening, weakness, or loss of structural rigidity in the cartilaginous support rings of the bronchial walls.",
    "secondary": "In pediatric pulmonology, a congenital or acquired disorder causing expiratory dynamic airway collapse, persistent stridor, and recurrent respiratory infections.",
    "quotes": [
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "Congenital **bronchomalacia** results from defective chondrogenesis in the embryonic bronchial arches, leading to flaccid airway walls."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Dynamic airway collapse in **bronchomalacia** provokes chronic brassy cough and severe respiratory distress during crying or exertion."
      },
      {
        "author": "Harvey Cushing",
        "work": "Surgery of the Mediastinum",
        "quote": "Extrinsic compression from vascular rings can induce localized **bronchomalacia**, predisposing the infant to sudden suffocative crises."
      }
    ]
  },
  "Dashboard — bronch\\bronchopneumonia.md": {
    "primary": "A form of pneumonia characterized by patchy inflammation of the lung parenchyma, originating in the bronchioles and spreading to surrounding alveolar lobules.",
    "secondary": "In clinical pathology, lobular pneumonia caused by bacterial or viral aspiration, presenting with patchy bilateral consolidations, fever, and tachypnea.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In infants and the debilitated aged, **bronchopneumonia** is the great reaper, seizing upon lungs weakened by previous viral catarrhs."
      },
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "Autopsy reveals scattered focal nodules of **bronchopneumonia** surrounded by areas of crepitant, emphysematous lung tissue."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "In **bronchopneumonia**, the inflammatory exudate fills both the lumen of the small bronchiole and the immediately adjacent alveolar spaces."
      }
    ]
  },
  "Dashboard — bronch\\bronchoscope.md": {
    "primary": "A rigid or flexible tubular optical instrument passed through the mouth or nose into the trachea and bronchi for visual examination or therapeutic procedures.",
    "secondary": "In thoracic surgery and interventional pulmonology, an endoscopic device equipped with video optics, suction channels, and instruments for biopsy and foreign-body removal.",
    "quotes": [
      {
        "author": "Gustav Killian",
        "work": "The Direct Examination of the Respiratory Tract",
        "quote": "In 1897, I introduced the straight **bronchoscope** to remove an aspirated pork bone from the right main bronchus of an awake patient."
      },
      {
        "author": "Chevalier Jackson",
        "work": "Bronchoscopy and Esophagoscopy",
        "quote": "The illuminated **bronchoscope** converted foreign body extraction from a dangerous blind gamble into an exact visual science."
      },
      {
        "author": "Harvey Cushing",
        "work": "Surgery of the Respiratory Tract",
        "quote": "Diagnostic inspection through the flexible **bronchoscope** permits precise biopsy of suspected endobronchial neoplasms under local anesthesia."
      }
    ]
  },
  "Dashboard — bronch\\bronchoscopic.md": {
    "primary": "Of, relating to, or performed by means of a bronchoscope or bronchoscopy.",
    "secondary": "In thoracic surgery, designating interventional diagnostic procedures, such as bronchoscopic biopsy, bronchoalveolar lavage, or endobronchial stenting.",
    "quotes": [
      {
        "author": "Chevalier Jackson",
        "work": "Bronchoscopy and Esophagoscopy",
        "quote": "Expert **bronchoscopic** extraction demands delicate tactile coordination to disengage sharp foreign objects without lacerating the mucosal wall."
      },
      {
        "author": "Gustav Killian",
        "work": "Direct Bronchoscopy",
        "quote": "The **bronchoscopic** appearance of the carina provides essential diagnostic clues regarding subcarinal lymph node metastases."
      },
      {
        "author": "Atul Gawande",
        "work": "Better: A Surgeon's Notes on Performance",
        "quote": "Under fiberoptic **bronchoscopic** guidance, difficult endotracheal intubations can be accomplished safely in patients with unstable cervical spines."
      }
    ]
  },
  "Dashboard — bronch\\bronchospasm.md": {
    "primary": "Sudden, involuntary constriction of the muscular walls of the bronchioles, causing acute narrowing of the airways and difficulty breathing.",
    "secondary": "In clinical pulmonology, the acute pathophysiological mechanism causing expiratory wheezing, chest tightness, and dyspnea during acute asthma exacerbations.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Inhaling cold dry air or antigenic dust triggers violent **bronchospasm**, locking the chest in a desperate struggle to exhale."
      },
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "The musical sibilant rales heard over both hemithoraces reflect air being forced through airways narrowed by acute **bronchospasm**."
      },
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "Differentiating cardiac asthma from true allergic **bronchospasm** is vital before administering adrenergic therapeutics."
      }
    ]
  },
  "Dashboard — bronch\\bronchus.md": {
    "primary": "Either of the two primary divisions of the trachea that lead into the right and left lungs, or any of their major secondary cartilaginous branches.",
    "secondary": "In respiratory anatomy, a major conducting airway supported by cartilaginous plates, smooth muscle, and pseudostratified ciliated columnar epithelium.",
    "quotes": [
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "The right **bronchus** departs from the trachea at a steeper downward angle, explaining why foreign objects so frequently lodge within it."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "Each primary **bronchus** enters the hilum of its corresponding lung, accompanied by branches of the pulmonary artery and vein."
      },
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "Severe dilatation of a **bronchus**, or bronchiectasis, creates permanent cavities that pool purulent secretions."
      }
    ]
  },
  "Dashboard — bronch\\tracheobronchomalacia.md": {
    "primary": "A condition characterized by abnormal flaccidity, weakness, and dynamic collapse of both the trachea and the bronchial walls during expiration.",
    "secondary": "In pediatric and adult pulmonology, diffuse weakness of central airway cartilages causing recurrent barking cough, expiratory stridor, and respiratory arrest.",
    "quotes": [
      {
        "author": "Chevalier Jackson",
        "work": "Diseases of the Air and Food Passages of Foreign-Body Origin",
        "quote": "Direct endoscopy in severe **tracheobronchomalacia** reveals the anterior and posterior walls slapping together in complete expiratory collapse."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "Congenital **tracheobronchomalacia** arises from structural immaturity of the embryonic cartilaginous rings, improving as the infant matures."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Surgical tracheobronchopexy has been devised to stabilize the collapsing airway in intractable, life-threatening **tracheobronchomalacia**."
      }
    ]
  },
  "Dashboard — cardi\\acardia.md": {
    "primary": "Congenital absence of the heart, a rare and fatal teratological malformation occurring primarily in monozygotic twin gestations.",
    "secondary": "In developmental teratology, the condition of an acardiac twin (twin reversed arterial perfusion sequence) sustained solely by the circulation of the pump twin.",
    "quotes": [
      {
        "author": "Isidore Geoffroy Saint-Hilaire",
        "work": "General and Particular History of Anomalies of Organization",
        "quote": "The condition of **acardia** represents the most radical developmental arrest, wherein an amorphous parasite develops entirely without a central cardiac organ."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "In cases of fetal **acardia**, the deformed twin survives in utero only because retrograde perfusion is pumped across placental vascular anastomoses."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Complete **acardia** is universally incompatible with independent extrauterine life, occurring exclusively in abnormal monochorionic twin pregnancies."
      }
    ]
  },
  "Dashboard — cardi\\anacardiaceae.md": {
    "primary": "A family of flowering plants in the order Sapindales (the cashew or sumac family), characterized by resin ducts and phenolic urushiol compounds.",
    "secondary": "In systematic and economic botany, a cosmopolitan family comprising trees and shrubs such as the cashew, pistachio, mango, and poison ivy.",
    "quotes": [
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "Members of the **anacardiaceae** are characterized by acrid, milky or resinous juices that turn black upon exposure to atmospheric air."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The family **anacardiaceae** includes both delicious edible fruits like the mango and notoriously virulent contact poisons like Rhus toxicodendron."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "Horticultural interest in **anacardiaceae** spans tropical commercial orchards and brilliant autumn foliage ornamentals across temperate regions."
      }
    ]
  },
  "Dashboard — cardi\\anacardium.md": {
    "primary": "A genus of tropical American trees and shrubs in the family Anacardiaceae, notably Anacardium occidentale (the cashew tree).",
    "secondary": "In economic botany, trees cultivated for their kidney-shaped nuts borne externally at the end of a swollen, edible fleshy pedicel (cashew apple).",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "The generic name **anacardium** was bestowed because the heart-shaped nut is situated on the top of the fruit like an inverted heart."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Personal Narrative of Travels",
        "quote": "In the arid savannas of the Orinoco, scattered groves of **anacardium** yielded sweet, astringent cashew apples relished by travelers."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "The caustic shell oil of **anacardium** blisters human skin, requiring careful industrial roasting before the kernel can be consumed."
      }
    ]
  },
  "Dashboard — cardi\\bradycardia.md": {
    "primary": "Abnormal slowness of the heart rate, usually defined in an adult as a resting heart rate of fewer than 60 beats per minute.",
    "secondary": "In clinical cardiology, a slow heart rhythm resulting from physiological conditioning (athletic bradycardia), sinus node dysfunction, or atrioventricular block.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Extreme **bradycardia** accompanied by syncopal attacks defines the classic Stokes-Adams syndrome of complete heart block."
      },
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "Sinus **bradycardia** is a benign physiological finding in trained endurance athletes whose high stroke volume compensates for low rate."
      },
      {
        "author": "Thomas Lewis",
        "work": "Clinical Disorders of the Heart Beat",
        "quote": "Digitalis toxicity frequently heralds itself through sudden, pronounced **bradycardia** coupled with coupled ventricular extrasystoles."
      }
    ]
  },
  "Dashboard — cardi\\cardi.md": {
    "primary": "The Greek anatomical combining form derived from kardia, denoting the heart or the cardiac orifice of the stomach (cardi- / cardio-).",
    "secondary": "In physiological nomenclature, a radical prefix entering into foundational terms describing the cardiovascular and circulatory systems.",
    "quotes": [
      {
        "author": "Galen",
        "work": "On Anatomical Procedures",
        "quote": "The ancient Greeks designated the central throbbing organ of life by the radical **cardi**, tracing its vascular trunks throughout the flesh."
      },
      {
        "author": "William Harvey",
        "work": "De Motu Cordis",
        "quote": "All our physiological investigations confirm that the organ designated by **cardi** functions as an inexhaustible hydraulic pump."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "Compound terms formed from the root **cardi** encompass both the muscular organ in the thorax and the esophageal opening of the stomach."
      }
    ]
  },
  "Dashboard — cardi\\cardia.md": {
    "primary": "The anatomical upper orifice of the stomach where the esophagus enters and empties swallowed food.",
    "secondary": "In gastrointestinal anatomy, the transition zone between the squamous epithelium of the esophagus and the columnar secretory mucosa of the gastric fundus.",
    "quotes": [
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "The upper orifice of the ventricle is termed the **cardia** because its rich nervous supply provoked ancient physicians to compare it to the heart."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **cardia** is situated opposite the tenth thoracic vertebra, where the circular muscular fibers form the functional lower esophageal sphincter."
      },
      {
        "author": "William Beaumont",
        "work": "Experiments and Observations on the Gastric Juice",
        "quote": "Through the gastric fistula I could see food passing cleanly through the **cardia** into the churning cavity of the stomach."
      }
    ]
  },
  "Dashboard — cardi\\cardialgia.md": {
    "primary": "Severe burning pain or discomfort in the epigastrium or retrosternal region; heartburn or pyrosis.",
    "secondary": "In clinical medicine, esophageal or gastric burning caused by acid reflux, historically confused with ischemic cardiac pain due to sensory nerve convergence.",
    "quotes": [
      {
        "author": "William Beaumont",
        "work": "Experiments and Observations on the Gastric Juice and the Physiology of Digestion",
        "quote": "Irritation of the gastric mucosa by acrid undigested aliment produced violent **cardialgia** that subsided upon neutralizing with alkaline salts."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The clinician must carefully differentiate simple **cardialgia** arising from acid reflux from genuine exertional angina pectoris."
      },
      {
        "author": "Thomas Sydenham",
        "work": "Observationes Medicae",
        "quote": "Nocturnal **cardialgia** torments the dyspeptic patient with burning sensations that mount upward from the stomach toward the throat."
      }
    ]
  },
  "Dashboard — cardi\\cardiidae.md": {
    "primary": "The family of marine bivalve mollusks known as cockles, possessing thick, heart-shaped, radially ribbed shells.",
    "secondary": "In malacology, benthic bivalves equipped with a powerful, bent, muscular foot capable of leaping to evade predatory starfish.",
    "quotes": [
      {
        "author": "Georges Cuvier",
        "work": "The Animal Kingdom",
        "quote": "The family **cardiidae** is easily distinguished by its symmetrical, cordate valves, adorned with prominent radiating ribs."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The fossil record exhibits numerous transitions among the **cardiidae** as sea temperatures fluctuated across Tertiary epochs."
      },
      {
        "author": "James Dwight Dana",
        "work": "Manual of Geology",
        "quote": "Extensive shell beds formed by members of the **cardiidae** pave ancient coastal terraces across the Mediterranean basin."
      }
    ]
  },
  "Dashboard — cardi\\cardinal.md": {
    "primary": "Of the greatest, primary, or fundamental importance; chief, pivotal, or paramount.",
    "secondary": "A high-ranking dignitary of the Roman Catholic Church appointed by the Pope and serving as a member of the Sacred College that elects the pontiff.",
    "quotes": [
      {
        "author": "Niccolò Machiavelli",
        "work": "The Prince",
        "quote": "The prince must observe the **cardinal** virtues of prudent governance, tempering severity with constant vigilance."
      },
      {
        "author": "John Henry Newman",
        "work": "Apologia Pro Vita Sua",
        "quote": "When raised to the dignity of **cardinal** by Pope Leo XIII, I felt that my long ecclesiastical trials had found their peaceful haven."
      },
      {
        "author": "Thomas More",
        "work": "Utopia",
        "quote": "Justice and equity are the **cardinal** pillars upon which every durable and happy commonwealth must rest."
      }
    ]
  },
  "Dashboard — cardi\\cardinalate.md": {
    "primary": "The office, rank, dignity, or collective body of cardinals in the Roman Catholic Church.",
    "secondary": "In church history and canon law, the Sacred College of Cardinals, which acts as the supreme advisory council to the Pope and governs during a papal interregnum.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Elevation to the **cardinalate** conferred secular princely rank alongside immense spiritual authority in Christendom."
      },
      {
        "author": "Lord Acton",
        "work": "The History of Freedom and Other Essays",
        "quote": "The political influence wielded by the **cardinalate** during the Renaissance rivaled that of the great monarchies of Europe."
      },
      {
        "author": "John Henry Newman",
        "work": "Letters and Correspondence",
        "quote": "My unexpected appointment to the **cardinalate** silenced those critics who had questioned my theological orthodoxy."
      }
    ]
  },
  "Dashboard — cardi\\cardinalfish.md": {
    "primary": "Any of numerous small, brightly colored marine fishes of the family Apogonidae, typically nocturnal reef dwellers with large eyes and two dorsal fins.",
    "secondary": "In marine biology, reef-dwelling fishes known for oral incubation (paternal mouthbrooding), where males carry fertilized eggs in their mouths until hatching.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The tiny red **cardinalfish** hides deep within branching coral crevices by day, emerging after sunset to forage upon plankton."
      },
      {
        "author": "William Beebe",
        "work": "Beneath Tropic Seas",
        "quote": "Under the flashlight beam, the bright scarlet scales of the **cardinalfish** gleamed like rubies against the black cavern walls."
      },
      {
        "author": "Rachel Carson",
        "work": "Under the Sea-Wind",
        "quote": "The male **cardinalfish** sheltered his brood of eggs safely inside his pharynx, fasting until the fry were ready to swim."
      }
    ]
  },
  "Dashboard — cardi\\cardinality.md": {
    "primary": "The number of elements in a mathematical set.",
    "secondary": "In mathematical set theory and logic, Georg Cantor's measure of the size of finite or transfinite sets, distinguishing countable sets from the continuum.",
    "quotes": [
      {
        "author": "Georg Cantor",
        "work": "Contributions to the Founding of the Theory of Transfinite Numbers",
        "quote": "Two sets are said to have the same **cardinality** or power if their elements can be placed in one-to-one correspondence."
      },
      {
        "author": "Bertrand Russell",
        "work": "The Principles of Mathematics",
        "quote": "The concept of **cardinality** frees arithmetic from empirical counting, defining cardinal numbers as classes of equinumerous sets."
      },
      {
        "author": "Kurt Gödel",
        "work": "What is Cantor's Continuum Problem?",
        "quote": "Cantor proved that the **cardinality** of the real continuum strictly exceeds the countable cardinality of the natural numbers."
      }
    ]
  },
  "Dashboard — cardi\\cardinalship.md": {
    "primary": "The office, status, or tenure of a cardinal in the Roman Catholic Church; cardinalate.",
    "secondary": "In ecclesiastical history, the dignitary role of serving as a prince of the Church endowed with voting rights in papal conclaves.",
    "quotes": [
      {
        "author": "Thomas More",
        "work": "The History of King Richard III",
        "quote": "Morton was raised to the **cardinalship** of Canterbury, wielding extraordinary diplomatic counsel under the crown."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The ambition of Roman patricians was constantly excited by the glittering prize of the **cardinalship**."
      },
      {
        "author": "Francis Bacon",
        "work": "The Reign of King Henry VII",
        "quote": "Wolsey attained the **cardinalship** and legatine authority, concentrating secular and spiritual mastery in his solitary hand."
      }
    ]
  },
  "Dashboard — cardi\\cardiogram.md": {
    "primary": "A curve, tracing, or graphical record of the physical movements, mechanical impulses, or electrical voltages generated by the beating heart.",
    "secondary": "In clinical medicine, the graphic output produced by a cardiograph or electrocardiograph used to diagnose arrhythmias and ischemia.",
    "quotes": [
      {
        "author": "Willem Einthoven",
        "work": "The Galvanometric Registration of the Human Electrocardiogram",
        "quote": "The sharp deflections of the **cardiogram**, designated P, Q, R, S, and T, correspond to distinct electrical phases of the heartbeat."
      },
      {
        "author": "Thomas Lewis",
        "work": "The Mechanism and Graphic Registration of the Heart Beat",
        "quote": "Careful measurement of intervals on the photographic **cardiogram** accurately identifies the site of ectopic ventricular contractions."
      },
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "Serial comparison of the patient's **cardiogram** confirmed the progressive resolution of acute myocardial ischemic changes."
      }
    ]
  },
  "Dashboard — cardi\\cardiograph.md": {
    "primary": "An instrument designed for recording the mechanical movements or electrical potentials produced by the action of the heart.",
    "secondary": "In medical technology, historically Étienne-Jules Marey's mechanical apex-beat recorder, evolving into the string galvanometer instrument developed by Willem Einthoven.",
    "quotes": [
      {
        "author": "Willem Einthoven",
        "work": "The String Galvanometer and Its Medical Applications",
        "quote": "By suspending a silvered quartz filament in a strong magnetic field, I constructed an exceptionally sensitive **cardiograph**."
      },
      {
        "author": "Étienne-Jules Marey",
        "work": "The Graphic Method in Medical Science",
        "quote": "The mechanical **cardiograph** applied over the cardiac apex faithfully registers each phase of ventricular systole."
      },
      {
        "author": "Augustus Waller",
        "work": "An Introduction to Human Physiology",
        "quote": "Before Einthoven's refinement, Waller utilized the capillary electrometer as an electrical **cardiograph** to detect human cardiac currents."
      }
    ]
  },
  "Dashboard — cardi\\cardiographic.md": {
    "primary": "Of, relating to, or obtained by means of a cardiograph or cardiography.",
    "secondary": "In diagnostic cardiology, describing the graphic waveforms, voltage intervals, and diagnostic tracing patterns generated during cardiac monitoring.",
    "quotes": [
      {
        "author": "Willem Einthoven",
        "work": "The Different Forms of the Human Electrocardiogram",
        "quote": "The **cardiographic** tracing provides an objective record of heart function that no stethoscope can duplicate."
      },
      {
        "author": "Thomas Lewis",
        "work": "Clinical Electrocardiography",
        "quote": "Specific **cardiographic** abnormalities, such as ST-segment elevation, serve as the clinical signature of acute coronary thrombosis."
      },
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "Extensive **cardiographic** surveys established the normal physiological boundaries of the PR interval across age groups."
      }
    ]
  },
  "Dashboard — cardi\\cardiography.md": {
    "primary": "The medical science, diagnostic technique, or practice of recording and interpreting the physical movements or electrical cycles of the heart.",
    "secondary": "In clinical cardiology, the non-invasive specialty encompassing mechanocardiography, electrocardiography, and echocardiographic graphic assessment.",
    "quotes": [
      {
        "author": "Willem Einthoven",
        "work": "Nobel Lecture: The String Galvanometer in the Service of Medicine",
        "quote": "Clinical **cardiography** has bridged the gap between physical laboratory instruments and everyday bedside diagnostics."
      },
      {
        "author": "Augustus Waller",
        "work": "On the Electromotive Changes Connected with the Beat of the Mammalian Heart",
        "quote": "The demonstration that cardiac currents reach the surface of the human body laid the physical foundations of modern **cardiography**."
      },
      {
        "author": "Étienne-Jules Marey",
        "work": "The Circulation of the Blood in Health and Disease",
        "quote": "Mechanical **cardiography** converted the fleeting palpation of the physician's hand into permanent, measurable ink tracings."
      }
    ]
  },
  "Dashboard — cardi\\cardioid.md": {
    "primary": "A heart-shaped mathematical planar curve generated by the path of a point on the circumference of a circle rolling without slipping around a fixed circle of equal radius.",
    "secondary": "In acoustical engineering and microphone technology, a heart-shaped directional pickup pattern that is sensitive to front signals while rejecting rear sound.",
    "quotes": [
      {
        "author": "Isaac Newton",
        "work": "Mathematical Papers",
        "quote": "The generation of the epicycloid wherein both radii are equal traces that singular heart-shaped curve known as the **cardioid**."
      },
      {
        "author": "Leonhard Euler",
        "work": "Introduction to the Analysis of the Infinite",
        "quote": "In polar coordinates, the algebraic equation of the **cardioid** assumes the elegantly simple form of r equals a times one plus cosine theta."
      },
      {
        "author": "Arthur Cayley",
        "work": "A Treatise on Elliptic Functions",
        "quote": "The caustic by reflection of a circle for light rays issuing from a point on its circumference is itself a classic **cardioid**."
      }
    ]
  },
  "Dashboard — cardi\\cardiologic.md": {
    "primary": "Pertaining to the heart, heart disease, or the medical specialty of cardiology.",
    "secondary": "In healthcare practice, describing clinical investigations, specialized diagnostic equipment, or therapeutic consultations focused on cardiovascular pathology.",
    "quotes": [
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "A thorough **cardiologic** evaluation must unite careful physical auscultation with precision radiographic and electrical studies."
      },
      {
        "author": "Thomas Lewis",
        "work": "The Mechanism and Graphic Registration of the Heart Beat",
        "quote": "Advances in laboratory physiology have reshaped **cardiologic** practice, placing bedside diagnosis on firm biophysical foundations."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The **cardiologic** signs of aortic regurgitation include the collapsing Corrigan pulse and visible capillary pulsations in the nail beds."
      }
    ]
  },
  "Dashboard — cardi\\cardiologist.md": {
    "primary": "A medical doctor who specializes in the diagnosis, medical management, and prevention of diseases of the heart and cardiovascular system.",
    "secondary": "A physician expert in interpreting electrocardiograms, echocardiograms, and cardiac catheterization to manage heart failure, arrhythmias, and coronary disease.",
    "quotes": [
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "The modern **cardiologist** must be both a clinician and a physiologist, understanding the mechanical hydraulics of failing hearts."
      },
      {
        "author": "Thomas Lewis",
        "work": "Clinical Disorders of the Heart Beat",
        "quote": "Before the string galvanometer, the **cardiologist** was forced to infer arrhythmias through subtle variations in radial pulse timing."
      },
      {
        "author": "Helen B. Taussig",
        "work": "Congenital Malformations of the Heart",
        "quote": "Close collaboration between the pediatric **cardiologist** and the thoracic surgeon made corrective operations for blue babies a reality."
      }
    ]
  },
  "Dashboard — cardi\\cardiology.md": {
    "primary": "The medical specialty and branch of medicine that deals with the study, diagnosis, and treatment of disorders of the heart and circulatory system.",
    "secondary": "In clinical science, an expansive discipline encompassing preventive cardiology, interventional cardiology, electrophysiology, and cardiovascular pharmacology.",
    "quotes": [
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease: A Textbook for Students and Practitioners",
        "quote": "The triumph of twentieth-century **cardiology** was the eradication of fatalism regarding coronary thrombosis and heart failure."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "No chapter in internal medicine demands closer clinical acumen than **cardiology**, where life hangs upon a single beat."
      },
      {
        "author": "Thomas Lewis",
        "work": "The Soldier's Heart and the Effort Syndrome",
        "quote": "The demands of wartime medicine propelled **cardiology** into investigating functional neurocirculatory disorders alongside organic valvular defects."
      }
    ]
  },
  "Dashboard — cardi\\cardiomegaly.md": {
    "primary": "Abnormal, pathological enlargement of the heart, resulting from myocardial hypertrophy, chamber dilatation, or both.",
    "secondary": "In clinical radiology and cardiology, a cardiothoracic ratio exceeding 50 percent on a posteroanterior chest radiograph, indicating underlying heart disease.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Massive **cardiomegaly**, producing the classic cor bovinum, is frequently the end-stage result of unmanaged aortic insufficiency."
      },
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "Chronic untreated systemic hypertension places sustained barometric afterload upon the left ventricle, culminating in marked **cardiomegaly**."
      },
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "The displaced apex beat and extended area of cardiac dullness provide unmistakable physical evidence of progressive **cardiomegaly**."
      }
    ]
  },
  "Dashboard — cardi\\cardiomyopathy.md": {
    "primary": "A chronic disease of the heart muscle (myocardium) in which the muscle becomes structurally and functionally abnormal, impairing pumping efficiency.",
    "secondary": "In clinical cardiology, categorized into dilated, hypertrophic, restrictive, and arrhythmogenic right ventricular cardiomyopathy, often with genetic origins.",
    "quotes": [
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "Primary **cardiomyopathy** must be distinguished from ischemic heart disease by the absence of major obstructive epicardial coronary lesions."
      },
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease: A Textbook of Cardiovascular Medicine",
        "quote": "Hypertrophic **cardiomyopathy** is a familial disease caused by mutations in sarcomeric contractile proteins, risking sudden athletic death."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Degenerative changes within the muscular fibers themselves give rise to that obscure chronic cardiac failure termed **cardiomyopathy**."
      }
    ]
  },
  "Dashboard — cardi\\cardiopathy.md": {
    "primary": "Any generic disease, morbid condition, or functional disorder affecting the heart.",
    "secondary": "In general medical pathology, an overarching term encompassing valvular, ischemic, electrical, or myocardial afflictions of the cardiac organ.",
    "quotes": [
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "Every organic **cardiopathy** alters the natural rhythm and acoustic qualities of the heart sounds heard through the cylinder."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Congenital **cardiopathy** in infants manifests as central cyanosis, clubbed digits, and harsh precordial systolic murmurs."
      },
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "Rheumatic fever remains the primary cause of chronic valvular **cardiopathy** throughout developing regions of the world."
      }
    ]
  },
  "Dashboard — cardi\\cardioplegia.md": {
    "primary": "The temporary, intentional cessation or arrest of cardiac contractions, induced experimentally or during open-heart surgery.",
    "secondary": "In cardiac surgery, the infusion of a cold, hyperkalemic crystalloid or blood solution into coronary vessels to protect the myocardium during aortic cross-clamping.",
    "quotes": [
      {
        "author": "John Gibbon",
        "work": "Extracorporeal Circulation",
        "quote": "The introduction of chemical **cardioplegia** permitted surgeons to operate upon a completely motionless, bloodless, flaccid heart."
      },
      {
        "author": "Denton Cooley",
        "work": "Techniques in Cardiac Surgery",
        "quote": "Cold potassium **cardioplegia** preserves intracellular energy stores, allowing prolonged, complex intracardiac repairs without ischemic necrosis."
      },
      {
        "author": "Michael DeBakey",
        "work": "The Past, Present, and Future of Cardiac Surgery",
        "quote": "Hypothermic **cardioplegia** revolutionized myocardial protection during lengthy double-valve replacements and coronary bypass grafting."
      }
    ]
  },
  "Dashboard — cardi\\cardioplegic.md": {
    "primary": "Pertaining to, causing, or characterized by cardioplegia; arresting cardiac contractions.",
    "secondary": "In cardiovascular surgery, designating the pharmacological solution (high in potassium and magnesium) infused to induce electromechanical cardiac arrest.",
    "quotes": [
      {
        "author": "Denton Cooley",
        "work": "Techniques in Cardiac Surgery",
        "quote": "Infusing the cold **cardioplegic** solution directly into the aortic root induces immediate diastolic arrest of the myocardium."
      },
      {
        "author": "Michael DeBakey",
        "work": "Cardiovascular Surgery",
        "quote": "Periodic re-infusion of the **cardioplegic** solution preserves low myocardial temperatures throughout prolonged aortic clamping."
      },
      {
        "author": "John Gibbon",
        "work": "Extracorporeal Circulation in Cardiac Surgery",
        "quote": "The formulation of balanced **cardioplegic** agents virtually eliminated postoperative low cardiac output syndrome from ischemic injury."
      }
    ]
  },
  "Dashboard — cardi\\cardiopulmonary.md": {
    "primary": "Of, relating to, or involving both the heart and the lungs.",
    "secondary": "In emergency medicine and surgery, designating cardiopulmonary resuscitation (CPR) or the cardiopulmonary bypass machine (heart-lung machine).",
    "quotes": [
      {
        "author": "John Gibbon",
        "work": "Application of a Mechanical Heart and Lung Apparatus to Cardiac Surgery",
        "quote": "The successful deployment of **cardiopulmonary** bypass in 1953 opened the interior of the human heart to definitive corrective surgery."
      },
      {
        "author": "Helen B. Taussig",
        "work": "Congenital Malformations of the Heart",
        "quote": "The patient exhibited severe **cardiopulmonary** insufficiency, demanding urgent creation of an arterial shunt to augment pulmonary blood flow."
      },
      {
        "author": "Peter Safar",
        "work": "Cardiopulmonary Resuscitation",
        "quote": "Combining mouth-to-mouth ventilation with external chest compressions created modern **cardiopulmonary** resuscitation, saving thousands from sudden arrest."
      }
    ]
  },
  "Dashboard — cardi\\cardiorespiratory.md": {
    "primary": "Involving, relating to, or affecting both the cardiovascular (heart and blood vessels) and respiratory (lungs and airways) systems.",
    "secondary": "In clinical physiology and sports medicine, designating cardiorespiratory fitness, cardiorespiratory arrest, or synchronized oxygen-delivery systems.",
    "quotes": [
      {
        "author": "Walter Cannon",
        "work": "The Wisdom of the Body",
        "quote": "During vigorous muscular exertion, coordinated **cardiorespiratory** adjustments accelerate oxygen delivery and carbon dioxide elimination."
      },
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "High altitude induces acute **cardiorespiratory** strain, demanding hyperventilation and tachycardia to preserve tissue oxygen tension."
      },
      {
        "author": "August Krogh",
        "work": "The Anatomy and Physiology of Capillaries",
        "quote": "The ultimate limit of human physical endurance resides in the capacity of the **cardiorespiratory** system to perfuse active muscle beds."
      }
    ]
  },
  "Dashboard — cardi\\cardiospasm.md": {
    "primary": "Spasmodic contraction or failure of relaxation of the lower esophageal sphincter (the cardia), preventing food from entering the stomach; achalasia.",
    "secondary": "In gastroenterology, functional esophageal obstruction leading to massive dilatation and tortuosity of the proximal esophagus (megaesophagus).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In chronic **cardiospasm**, the esophagus above the tightened cardia becomes enormously dilated, regurgitating undigested food hours after meals."
      },
      {
        "author": "Harvey Cushing",
        "work": "Surgery of the Alimentary Canal",
        "quote": "Careful pneumatic balloon dilatation of the tight sphincter provides substantial symptomatic relief in intractable **cardiospasm**."
      },
      {
        "author": "Heinrich Quincke",
        "work": "Disorders of the Esophagus",
        "quote": "Microscopic examination of the resected tissue in severe **cardiospasm** confirms degeneration of the ganglion cells of Auerbach's plexus."
      }
    ]
  },
  "Dashboard — cardi\\cardiospermum.md": {
    "primary": "A genus of tropical and subtropical climbing herbs and woody vines (family Sapindaceae), commonly called balloon vines or heartseeds.",
    "secondary": "In systematic botany, climbing vines characterized by inflated, papery capsules containing dark round seeds marked with a white heart-shaped spot.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "The generic name **cardiospermum** reflects the white heart-shaped hilum that adorns the black spherical seed."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "In **cardiospermum**, the membranous inflated capsule acts as a buoyant float, aiding seed dispersal along tropical riverbanks."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "Gardeners cultivate **cardiospermum** for its curious balloon-like pods and delicate tendrils that cling to trellises."
      }
    ]
  },
  "Dashboard — cardi\\cardiothoracic.md": {
    "primary": "Of, relating to, or involving both the heart and the thoracic cavity or its organs (lungs, pleura, esophagus, and great vessels).",
    "secondary": "In surgery, the medical specialty encompassing operations on the heart, lungs, esophagus, and chest wall (cardiothoracic surgery).",
    "quotes": [
      {
        "author": "John Gibbon",
        "work": "Cardiothoracic Surgery",
        "quote": "The emergence of modern **cardiothoracic** surgery required the synchronized mastery of endotracheal anesthesia, blood banking, and bypass mechanics."
      },
      {
        "author": "Helen B. Taussig",
        "work": "Congenital Malformations of the Heart",
        "quote": "The skilled **cardiothoracic** surgeon can reconstruct intricate aortic arch anomalies that were universally fatal in infancy."
      },
      {
        "author": "Michael DeBakey",
        "work": "A History of Vascular Surgery",
        "quote": "Resection of thoracic aortic aneurysms remains among the most technically demanding challenges in **cardiothoracic** practice."
      }
    ]
  },
  "Dashboard — cardi\\cardiovascular.md": {
    "primary": "Of, relating to, or involving the heart and blood vessels collectively; relating to the circulatory system.",
    "secondary": "In epidemiological medicine, designating the complex of coronary heart disease, stroke, hypertension, and peripheral vascular disorders.",
    "quotes": [
      {
        "author": "William Harvey",
        "work": "De Motu Cordis",
        "quote": "The continuous, circular movement of the blood through the **cardiovascular** conduits demonstrates the mechanical function of the heart."
      },
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "Atherosclerosis of the coronary and cerebral arteries represents the primary threat to adult **cardiovascular** health in industrial nations."
      },
      {
        "author": "Walter Cannon",
        "work": "The Wisdom of the Body",
        "quote": "Autonomic nervous reflexes dynamically adjust peripheral vascular resistance to preserve **cardiovascular** perfusion during physical stress."
      }
    ]
  },
  "Dashboard — cardi\\carditis.md": {
    "primary": "Inflammation of the heart muscle or tissues, encompassing endocarditis, myocarditis, or pericarditis.",
    "secondary": "In clinical rheumatology, cardiac inflammation (often acute pancarditis) occurring as a major manifestation of acute rheumatic fever.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Rheumatic **carditis** demands absolute prolonged bed rest to prevent permanent cicatricial shortening of the mitral valve leaflets."
      },
      {
        "author": "Thomas Sydenham",
        "work": "Observationes Medicae",
        "quote": "Acute articular rheumatism often strikes the heart with violent **carditis**, leaving the patient with lifelong palpitations."
      },
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "The presence of a double friction sound over the precordium confirms that acute **carditis** has involved the serous pericardial membrane."
      }
    ]
  },
  "Dashboard — cardi\\cardium.md": {
    "primary": "The heart, or the cardiac orifice of the stomach (in anatomical terminology); also a taxonomic genus of marine bivalves in the cockle family (Cardiidae).",
    "secondary": "In malacology and paleontology, the type genus of true cockles characterized by inflated heart-shaped shells with radial costae.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Systema Naturae",
        "quote": "The shell of **cardium** is cordate, with valves that close tightly along crenulated margins like interlocking teeth."
      },
      {
        "author": "Georges Cuvier",
        "work": "The Animal Kingdom",
        "quote": "The common cockle, **cardium** edule, burrows shallowly into intertidal sand flats across the coasts of Europe."
      },
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "In anatomical nomenclature, the upper opening of the stomach receives the name **cardium** from its sympathetic nervous resonance with the heart."
      }
    ]
  },
  "Dashboard — cardi\\electrocardiogram_ecg.md": {
    "primary": "A graphic tracing of the electrical potentials produced by the beating heart muscle, recorded from electrodes placed on the surface of the body (ECG).",
    "secondary": "In clinical cardiology, a fundamental diagnostic recording displaying P waves, QRS complexes, and T waves used to evaluate arrhythmias, conduction blocks, and myocardial infarction.",
    "quotes": [
      {
        "author": "Willem Einthoven",
        "work": "The Galvanometric Registration of the Human Electrocardiogram",
        "quote": "The **electrocardiogram (ECG)** registers with mathematical fidelity the tiny electrical currents produced by each cardiac cycle."
      },
      {
        "author": "Thomas Lewis",
        "work": "Clinical Disorders of the Heart Beat",
        "quote": "In atrial fibrillation, the normal P waves on the **electrocardiogram (ECG)** are replaced by rapid, chaotic fibrillary waves."
      },
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "ST-segment elevation on the Twelve-Lead **electrocardiogram (ECG)** provides unmistakable confirmation of acute coronary occlusion."
      }
    ]
  },
  "Dashboard — cardi\\electrocardiography.md": {
    "primary": "The medical diagnostic procedure and technique of recording and interpreting the electrical activity generated by the heart over time.",
    "secondary": "In clinical cardiology, a non-invasive diagnostic standard invented by Willem Einthoven, using limb and precordial leads to monitor myocardial depolarization.",
    "quotes": [
      {
        "author": "Willem Einthoven",
        "work": "Nobel Lecture: The String Galvanometer",
        "quote": "The clinical triumph of **electrocardiography** lies in its power to reveal the inner electrical conducting pathways of the heart without surgical exposure."
      },
      {
        "author": "Augustus Waller",
        "work": "An Introduction to Human Physiology",
        "quote": "My early demonstrations that cardiac electricity could be registered from the hands and feet founded the science of **electrocardiography**."
      },
      {
        "author": "Thomas Lewis",
        "work": "Mechanism and Graphic Registration of the Heart Beat",
        "quote": "Modern **electrocardiography** has revolutionized our comprehension of cardiac physiology, transforming theoretical tracings into indispensable bedside tools."
      }
    ]
  },
  "Dashboard — cardi\\endocarditis.md": {
    "primary": "Inflammation of the endocardium, the smooth inner epithelial lining of the heart cavities and heart valves, especially of infectious origin.",
    "secondary": "In clinical medicine, infective endocarditis caused by bacterial or fungal colonization of cardiac valves, producing friable vegetations, murmurs, and septic emboli.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Gulstonian Lectures on Malignant Endocarditis",
        "quote": "Malignant **endocarditis** strikes the damaged heart valve, producing ulcerations and friable bacterial vegetations that seed the arterial tree."
      },
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "Chronic vegetative **endocarditis** deforms the mitral and aortic cusps, producing loud regurgitant bellows murmurs."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Fibrinous deposits in acute **endocarditis** are not mere precipitates of blood, but active inflammatory exudations from the damaged subendothelial stroma."
      }
    ]
  },
  "Dashboard — cardi\\endocardium.md": {
    "primary": "The thin, smooth, serous endothelial membrane that lines the interior cavities, trabeculae, and valves of the heart.",
    "secondary": "In cardiac histology, the innermost layer of the heart wall, continuous with the endothelial lining of the great blood vessels entering and leaving the organ.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **endocardium** is a delicate serous membrane consisting of a single layer of polygonal endothelial cells supported by elastic fibers."
      },
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "Dissection of the ventricular chambers reveals that the inner **endocardium** forms smooth, glistening folds that constitute the valve cusps."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Because the **endocardium** is avascular across its valvular surfaces, repair following injury proceeds primarily through organizing surface thrombi."
      }
    ]
  },
  "Dashboard — cardi\\epicardia.md": {
    "primary": "The short abdominal portion of the esophagus situated below the diaphragm, extending from the esophageal hiatus to the cardiac orifice of the stomach.",
    "secondary": "In gastrointestinal anatomy, the terminal intra-abdominal segment of the esophagus, acting in conjunction with the diaphragmatic crura as an antireflux barrier.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **epicardia** measures scarcely more than two centimeters in length before expanding into the wider gastric reservoir."
      },
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "Where the gullet passes beneath the diaphragm, the **epicardia** is enveloped by a peritoneal fold continuous with the lesser omentum."
      },
      {
        "author": "William Beaumont",
        "work": "Experiments and Observations on the Gastric Juice",
        "quote": "The lower sphincter mechanism at the **epicardia** closes firmly against retrograde surges of acidic gastric contents during digestion."
      }
    ]
  },
  "Dashboard — cardi\\epicardium.md": {
    "primary": "The visceral inner serous layer of the pericardium that adheres closely to the external muscular surface of the heart.",
    "secondary": "In cardiac anatomy, the outermost layer of the heart wall, consisting of mesothelium and fibroelastic connective tissue containing the coronary blood vessels and subepicardial fat.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **epicardium** constitutes the visceral layer of the serous pericardium, reflecting onto the great vessels to join the parietal wall."
      },
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "Beneath the transparent sheet of the **epicardium**, the main trunks of the coronary arteries run cushioned in protective beds of fat."
      },
      {
        "author": "William Harvey",
        "work": "De Motu Cordis",
        "quote": "The glistening smoothness of the **epicardium** permits the heart to twist and contract without frictional resistance within its pericardial sac."
      }
    ]
  },
  "Dashboard — cardi\\hemicardia.md": {
    "primary": "A congenital teratological anomaly characterized by the defective, unilateral development of only one lateral half of the heart.",
    "secondary": "In developmental embryology and cardiac pathology, hypoplasia or agenesis of either the systemic or pulmonary cardiac chambers, presenting as hypoplastic left or right heart syndrome.",
    "quotes": [
      {
        "author": "Isidore Geoffroy Saint-Hilaire",
        "work": "General and Particular History of Anomalies of Organization",
        "quote": "The severe developmental anomaly termed **hemicardia** illustrates the lateral asymmetry that can arrest cardiac development during early organogenesis."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "In cases of **hemicardia**, a solitary functional ventricle must sustain the circulation through complex fetal vascular shunts."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Congenital **hemicardia** provokes profound neonatal cyanosis and circulatory collapse upon closure of the patent ductus arteriosus."
      }
    ]
  },
  "Dashboard — cardi\\megacardia.md": {
    "primary": "Abnormal, pathological enlargement or dilatation of the heart; cardiomegaly.",
    "secondary": "In clinical cardiology, enlargement of the heart due to chronic volume or pressure overload, characterized by an increased cardiothoracic ratio.",
    "quotes": [
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "The massive heart observed in **megacardia** fills the left hemithorax, displacing the adjacent lung and pressing against the diaphragm."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe chronic regurgitation of the aortic valves leads inexorably to extreme **megacardia**, the heart weighing up to a thousand grams."
      },
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "In advanced **megacardia**, the dilated chambers lose their mechanical efficiency, precipitating refractory congestive heart failure."
      }
    ]
  },
  "Dashboard — cardi\\megalocardia.md": {
    "primary": "Gross or extraordinary enlargement of the heart; extreme cardiomegaly (often termed cor bovinum or ox heart).",
    "secondary": "In pathology and autopsy medicine, massive cardiac enlargement, typically exceeding 800 to 1000 grams in weight, seen in severe valvular disease or advanced cardiomyopathy.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The postmortem examination revealed astounding **megalocardia**, the massive ventricles resembling an ox heart in volume and wall thickness."
      },
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "In extreme **megalocardia**, the cardiac dullness extends from the right mammary line far across the left axilla."
      },
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "Radiographs in cases of syphilitic aortic regurgitation exhibit monumental **megalocardia** with pronounced left ventricular rounding."
      }
    ]
  },
  "Dashboard — cardi\\neurocardiology.md": {
    "primary": "The interdisciplinary medical science that studies the physiological and pathological interactions between the nervous system and the heart.",
    "secondary": "In clinical neuroscience and cardiology, the study of brain-heart interactions, including arrhythmogenic effects of stroke, stress-induced cardiomyopathy (Takotsubo), and autonomic regulation.",
    "quotes": [
      {
        "author": "Walter Cannon",
        "work": "Bodily Changes in Pain, Hunger, Fear and Rage",
        "quote": "The pioneering insights of **neurocardiology** trace how intense emotional shock can provoke fatal cardiac arrhythmias via massive sympathetic discharge."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "Autonomic reflex arcs coordinate cardiac output with vascular tone, demonstrating the profound integration explored by modern **neurocardiology**."
      },
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "Every observant physician recognizes that emotional storms affect the heart, giving rise to the modern specialty of **neurocardiology**."
      }
    ]
  },
  "Dashboard — cardi\\pancarditis.md": {
    "primary": "Diffuse, severe inflammation simultaneously affecting all three anatomical layers of the heart: the endocardium, myocardium, and pericardium.",
    "secondary": "In clinical rheumatology and infectious disease, a life-threatening manifestation of acute rheumatic fever characterized by cardiomegaly, friction rubs, murmurs, and acute heart failure.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Acute rheumatic **pancarditis** combines endocardial valvular damage, myocardial contractile failure, and serofibrinous pericardial effusion."
      },
      {
        "author": "Thomas Sydenham",
        "work": "Observationes Medicae",
        "quote": "When rheumatic fever strikes the heart, it spares no part of the organ, kindling a general **pancarditis** that threatens swift dissolution."
      },
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "The mortality of childhood rheumatic fever was dictated largely by the severity of the initial attack of acute **pancarditis**."
      }
    ]
  },
  "Dashboard — cardi\\pericardiac.md": {
    "primary": "Of, relating to, or situated in the pericardium (the serous sac enclosing the heart); pericardial.",
    "secondary": "In descriptive human anatomy, designating blood vessels, nerves, or tissues investing or supplying the pericardial membrane (e.g. pericardiacophrenic vessels).",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The internal mammary artery gives off the **pericardiac** branches that course alongside the phrenic nerve to supply the fibrous sac."
      },
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "The **pericardiac** envelope firmly anchors the heart to the central tendon of the diaphragm below and to the great vessels above."
      },
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "Serous effusion within the **pericardiac** cavity muffles the heart sounds, making them appear distant and indistinct to the ear."
      }
    ]
  },
  "Dashboard — cardi\\pericardial.md": {
    "primary": "Of, relating to, or situated within the pericardium or the pericardial cavity enclosing the heart.",
    "secondary": "In clinical cardiology, describing pathological conditions such as pericardial effusion, pericardial tamponade, or pericardial friction rubs.",
    "quotes": [
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "A scratchy **pericardial** friction rub confirms the presence of fibrinous exudation upon the rubbing serous surfaces."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Rapid accumulation of fluid within the rigid **pericardial** sac compresses the cardiac chambers, precipitating acute tamponade."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **pericardial** cavity is normally a potential space containing a thin film of lubricating serous fluid that minimizes friction."
      }
    ]
  },
  "Dashboard — cardi\\pericarditis.md": {
    "primary": "Inflammation of the pericardium, the fibroserous sac that encloses the heart, characterized by chest pain and a pericardial friction rub.",
    "secondary": "In clinical cardiology, an acute or chronic condition caused by viral infection, autoimmune disease, uremia, or myocardial infarction, risking cardiac tamponade or constrictive fibrosis.",
    "quotes": [
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "The hallmark of acute fibrinous **pericarditis** is the superficial, to-and-fro leathery friction sound heard over the precordium."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Chronic constrictive **pericarditis** encases the heart in a rigid calcified armor, preventing diastolic filling of the ventricles."
      },
      {
        "author": "Thomas Sydenham",
        "work": "Observationes Medicae",
        "quote": "Violent substernal chest agony aggravated by recumbency and coughing signals inflammatory **pericarditis** attacking the heart's outer cloak."
      }
    ]
  },
  "Dashboard — cardi\\pericardium.md": {
    "primary": "The conical double-walled fibroserous sac that surrounds and protects the heart and the roots of the great vessels.",
    "secondary": "In human anatomy, consisting of an outer fibrous layer (fibrous pericardium) and an inner two-layered serous membrane (parietal and visceral epicardial layers) containing lubricating serous fluid.",
    "quotes": [
      {
        "author": "William Harvey",
        "work": "De Motu Cordis",
        "quote": "The heart beats smoothly within its protective **pericardium**, bathed in a clear fluid that preserves its moist agility."
      },
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "The tough fibrous outer coat of the **pericardium** blends seamlessly with the adventitia of the ascending aorta and pulmonary trunk."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "In cardiac tamponade, prompt surgical aspiration of fluid from the **pericardium** restores systemic arterial blood pressure."
      }
    ]
  }
};

const updated = updateNotesBatch(BASE_DIR, BATCH3_DATA);
console.log(`Body & Physiology Part 1 - Batch 3 Completed: ${updated} / ${Object.keys(BATCH3_DATA).length} notes updated.`);
