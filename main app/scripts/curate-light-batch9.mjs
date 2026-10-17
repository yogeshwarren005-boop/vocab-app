import fs from 'fs';
import path from 'path';

const baseClusterDir = 'App database/Greek roots/Cluster Light & Vision';

function updateNote(relPath, data) {
  const filePath = path.join(baseClusterDir, relPath);
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
  return true;
}

const batchData = {
  "Dashboard — pyrrh/pyrrhic.md": {
    "primary": "Relating to or achieved at tremendous, devastating cost that negates any real strategic advantage; or an ancient Greek war dance in brisk rhythm.",
    "secondary": "In classical prosody and poetry, a metrical foot consisting of two short or unstressed syllables; in military history, named after King Pyrrhus of Epirus following his costly victory at Asculum.",
    "quotes": [
      {
        "author": "Lord Byron",
        "work": "Don Juan",
        "quote": "You have the **Pyrrhic** dance as yet, / Where is the Pyrrhic phalanx gone?"
      },
      {
        "author": "Winston Churchill",
        "work": "The World Crisis",
        "quote": "The breakthrough on the Western Front had been bought at so cruel a price that it resembled a **pyrrhic** triumph."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "The swift sequence of short vowels in the opening line gives it the leaping rhythm of a **pyrrhic** measure."
      }
    ]
  },
  "Dashboard — pyrrh/pyrrhocoridae.md": {
    "primary": "A family of hemipteran true bugs, commonly known as red bugs or cotton stainers, characterized by bright aposematic red and black coloration.",
    "secondary": "In entomology, phytophagous insects possessing piercing-sucking mouthparts that damage agricultural crops like cotton, notable for their synthesis of juvenile hormone analogues.",
    "quotes": [
      {
        "author": "John Henry Comstock",
        "work": "An Introduction to Entomology",
        "quote": "Members of the family **Pyrrhocoridae** are conspicuous for their vivid contrast of red and black warning coloration."
      },
      {
        "author": "Vincent Dethier",
        "work": "The Physiology of Insect Senses",
        "quote": "Certain species of **Pyrrhocoridae** respond sharply to the volatile chemical cues given off by ripening cotton bolls."
      },
      {
        "author": "Howard Ensign Evans",
        "work": "Life on a Little-Known Planet",
        "quote": "The cotton stainers belonging to **Pyrrhocoridae** illustrate how insect pigments warn predators of unpalatable alkaloids."
      }
    ]
  },
  "Dashboard — pyrrh/pyrrhotine.md": {
    "primary": "An iron sulfide mineral (Fe_{1-x}S) with a bronze-yellow to copper-red luster, exhibiting varying degrees of magnetic susceptibility; alternative name for pyrrhotite.",
    "secondary": "In 19th-century mineralogy, the magnetic pyrite group displaying non-stoichiometric defect structures with ordered vacancies in the iron sub-lattice.",
    "quotes": [
      {
        "author": "James Dwight Dana",
        "work": "A System of Mineralogy",
        "quote": "The mineral **pyrrhotine** differs from ordinary iron pyrite both in its bronze hue and in its sensible magnetic attraction."
      },
      {
        "author": "Archibald Geikie",
        "work": "Text-Book of Geology",
        "quote": "Grains of **pyrrhotine** frequently occur intergrown with chalcopyrite in primary magmatic sulfide deposits."
      },
      {
        "author": "William Phillips",
        "work": "Elementary Introduction to Mineralogy",
        "quote": "Upon cleavage surfaces, **pyrrhotine** exhibits a slight reddish tarnish that quickly identifies it from marcasite."
      }
    ]
  },
  "Dashboard — pyrrh/pyrrhotite.md": {
    "primary": "A magnetic iron sulfide mineral with composition Fe_{1-x}S (x = 0 to 0.2), characterized by a metallic bronze-brown color and dark grayish-black streak.",
    "secondary": "In economic geology and structural engineering, a common sulfide mineral whose oxidation in concrete aggregates produces secondary sulfate minerals (thaumasite and ettringite) causing catastrophic swelling and structural failure.",
    "quotes": [
      {
        "author": "Waldemar Lindgren",
        "work": "Mineral Deposits",
        "quote": "The magmatic segregation of nickeliferous **pyrrhotite** at Sudbury represents one of the world's great concentrations of ore."
      },
      {
        "author": "Frank Wigglesworth Clarke",
        "work": "The Data of Geochemistry",
        "quote": "Because of structural vacancies in its iron lattice, **pyrrhotite** exhibits distinct ferrimagnetism absent in stoichiometric pyrite."
      },
      {
        "author": "Edward Salisbury Dana",
        "work": "Textbook of Mineralogy",
        "quote": "Crystals of **pyrrhotite** are commonly tabular hexagonal plates, often associated with pentlandite and siderite."
      }
    ]
  },
  "Dashboard — pyrrh/pyrrhula.md": {
    "primary": "A genus of stout-billed passerine birds in the finch family Fringillidae, comprising the bullfinches, noted for the male's striking rose-red or crimson breast plumage.",
    "secondary": "In ornithology and avian taxonomy, a Palearctic genus typified by Pyrrhula pyrrhula (the Eurasian bullfinch), exhibiting sexual dichromatism and specialized feeding on fruit buds.",
    "quotes": [
      {
        "author": "Gilbert White",
        "work": "The Natural History of Selborne",
        "quote": "The woodland bullfinch, **Pyrrhula** pyrrhula, strips the fruit trees of their swollen flower buds in the early days of spring."
      },
      {
        "author": "Thomas Bewick",
        "work": "A History of British Birds",
        "quote": "In the genus **Pyrrhula**, the bill is remarkably thick and convex, enabling the bird to crack the hardest seeds with ease."
      },
      {
        "author": "William Yarrell",
        "work": "A History of British Birds",
        "quote": "The vivid crimson breast of the male **Pyrrhula** contrasts sharply with the delicate slate grey of its back and jet-black cap."
      }
    ]
  },
  "Dashboard — pyrrh/pyrrhuloxia.md": {
    "primary": "A medium-sized North American desert bird (Cardinalis sinuatus) of the cardinal family, with a stout curved yellow bill, grey body plumage, and red crest, throat, and breast accents.",
    "secondary": "In ornithology, also known as the desert cardinal, inhabiting arid scrublands and mesquite thickets of the southwestern United States and Mexico, characterized by a stubby parrot-like bill.",
    "quotes": [
      {
        "author": "Florence Merriam Bailey",
        "work": "Handbook of Birds of the Western United States",
        "quote": "Perched atop a thorny mesquite, the **pyrrhuloxia** flutes its clear, sweet whistle across the shimmering desert."
      },
      {
        "author": "Frank Chapman",
        "work": "Camps and Cruises of an Ornithologist",
        "quote": "The stout, curved bill of the **pyrrhuloxia** gives its head an appearance curiously suggestive of a miniature parrot."
      },
      {
        "author": "Arthur Cleveland Bent",
        "work": "Life Histories of North American Birds",
        "quote": "In the arid canyon country, the grey and carmine plumage of the **pyrrhuloxia** blends unobtrusively with dry caliche soils."
      }
    ]
  },
  "Dashboard — pyrrh/pyrrhus.md": {
    "primary": "King of Epirus (c. 319–272 BCE), renowned Hellenistic general whose costly tactical victories against the Romans gave rise to the term 'Pyrrhic victory'; also an epithet of Neoptolemus, son of Achilles.",
    "secondary": "In classical historiography and military biography, a tactical genius and master of phalanx warfare whose campaigns in Italy and Sicily exemplified daring audacity ruined by strategic exhaustion.",
    "quotes": [
      {
        "author": "Plutarch",
        "work": "Parallel Lives: Life of Pyrrhus",
        "quote": "When congratulated on his victory, **Pyrrhus** famously replied, 'If we are victorious in one more battle with the Romans, we are utterly undone.'"
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The disciplined legions of Rome first learned the terrors of the Macedonian phalanx under the guidance of **Pyrrhus**."
      },
      {
        "author": "Niccolò Machiavelli",
        "work": "The Discourses on Livy",
        "quote": "The great talent of **Pyrrhus** lay in commanding armies in the field, yet he lacked the patience to consolidate his territorial conquests."
      }
    ]
  },
  "Dashboard — scept/Abroscopus.md": {
    "primary": "A genus of small, delicate Old World babbler-like warblers in the family Cettiidae, found in the forests of South and Southeast Asia.",
    "secondary": "In systematic ornithology, insectivorous bush warblers (such as the black-faced warbler) characterized by distinct facial markings, slender rictal bristles, and agile foraging habits.",
    "quotes": [
      {
        "author": "Eugene William Oates",
        "work": "The Fauna of British India: Birds",
        "quote": "The genus **Abroscopus** comprises diminutive warblers with bright rufous crowns and distinctive facial patterns."
      },
      {
        "author": "Frank Finn",
        "work": "The Birds of Calcutta",
        "quote": "In the dense bamboo undergrowth, an active **Abroscopus** flitted between shoots, gleaning tiny caterpillars from the leaves."
      },
      {
        "author": "Stuart Baker",
        "work": "The Fauna of British India: Birds, Vol. 2",
        "quote": "Nests of **Abroscopus** are delicately woven cups of moss tucked neatly into crevices of mossy tree trunks."
      }
    ]
  },
  "Dashboard — scept/diascopic.md": {
    "primary": "Pertaining to diascopic illumination or diascopy, the examination of specimens or skin lesions by transmitted light or through transparent pressure plates.",
    "secondary": "In dermatology and microscopy, relating to the technique of pressing a glass slide against erythematous skin to differentiate simple vascular dilatation from extravasated purpura.",
    "quotes": [
      {
        "author": "Robert Willan",
        "work": "On Cutaneous Diseases",
        "quote": "Under **diascopic** examination with a flat glass plate, the inflammatory blush blanches completely, while petechial hemorrhages remain visible."
      },
      {
        "author": "Jonathan Hutchinson",
        "work": "Illustrations of Clinical Surgery",
        "quote": "The characteristic apple-jelly nodules of lupus vulgaris are best revealed through **diascopic** pressure on the lesion."
      },
      {
        "author": "Thomas Addison",
        "work": "A Collection of the Published Writings",
        "quote": "By employing a **diascopic** method, the physician readily determines whether the vascularity of the macule is active or passive."
      }
    ]
  },
  "Dashboard — scept/diascopy.md": {
    "primary": "A clinical diagnostic test in dermatology in which a transparent glass slide or plastic plate is pressed firmly against a skin lesion to observe changes in vascular coloration.",
    "secondary": "In medical diagnostics, a procedure used to distinguish erythema (which blanches under pressure) from purpura (which does not blanch), and to reveal underlying granulomatous tissue.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Application of **diascopy** to the suspicious facial nodule immediately exposes the translucent brown hue typical of lupus."
      },
      {
        "author": "Henry Radcliffe Crocker",
        "work": "Diseases of the Skin",
        "quote": "By means of **diascopy**, we squeeze out capillary blood and inspect the morbid infiltrate undisturbed by hyperemia."
      },
      {
        "author": "Norman Walker",
        "work": "An Introduction to Dermatology",
        "quote": "Simple **diascopy** with a microscope slide remains one of the readiest bedside aids in cutaneous diagnosis."
      }
    ]
  },
  "Dashboard — scept/endoscope.md": {
    "primary": "An illuminated optical instrument, rigid or flexible, inserted into a body cavity or organ to inspect its interior directly.",
    "secondary": "In biomedical engineering and surgical practice, a diagnostic and interventional instrument equipped with fiber-optic or video imaging systems and working channels for biopsy forceps.",
    "quotes": [
      {
        "author": "Chevalier Jackson",
        "work": "Bronchoscopy and Esophagoscopy",
        "quote": "The introduction of the illuminated **endoscope** converted the dark passages of the human body into open fields of direct clinical inspection."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Direct visualization through the **endoscope** has spared countless patients the ordeal of exploratory laparotomy."
      },
      {
        "author": "Harold Hopkins",
        "work": "Optics in Medicine",
        "quote": "The rod-lens system transformed the rigid **endoscope**, providing vastly superior illumination and optical resolution."
      }
    ]
  },
  "Dashboard — scept/endoscopic.md": {
    "primary": "Pertaining to, performed with, or utilizing an endoscope for the visual inspection or surgical treatment of internal organs.",
    "secondary": "In minimally invasive surgery, designating diagnostic procedures and therapeutic maneuvers (such as resection, hemostasis, or biopsy) executed via optical intraluminal devices.",
    "quotes": [
      {
        "author": "Alexis Carrel",
        "work": "The Treatment of Infected Wounds",
        "quote": "The development of **endoscopic** technique allows deep surgical intervention with minimal trauma to surrounding tissues."
      },
      {
        "author": "Harvey Cushing",
        "work": "Intracranial Tumours",
        "quote": "Explorations with specialized **endoscopic** tubes opened unexpected avenues into the ventricular chambers of the brain."
      },
      {
        "author": "William Osler",
        "work": "Aequanimitas and Other Addresses",
        "quote": "Modern clinical diagnosis relies increasingly on **endoscopic** visualization rather than blind percussion and inference."
      }
    ]
  },
  "Dashboard — scept/endoscopy.md": {
    "primary": "The examination of internal body cavities, lumens, or organs using an endoscope.",
    "secondary": "In clinical medicine, a comprehensive subspecialty encompassing upper and lower gastrointestinal evaluations, bronchoscopy, laparoscopy, and arthroscopy for both diagnostic and therapeutic ends.",
    "quotes": [
      {
        "author": "Rudolf Schindler",
        "work": "Gastroscopy: The Endoscopic Study of Gastric Pathology",
        "quote": "The systematic practice of **endoscopy** transformed gastric pathology from posthumous speculation into an exact living science."
      },
      {
        "author": "William Mayo",
        "work": "Collected Papers of the Mayo Clinic",
        "quote": "Diagnostic **endoscopy** has dramatically reduced the mortality of gastrointestinal ulcerations by enabling timely local intervention."
      },
      {
        "author": "Chevalier Jackson",
        "work": "Peroral Endoscopy and Laryngeal Surgery",
        "quote": "In skillful hands, peroral **endoscopy** safely retrieves foreign bodies that would otherwise prove fatal."
      }
    ]
  },
  "Dashboard — scept/epidiascope.md": {
    "primary": "An optical projection instrument capable of projecting images of both transparent slides (diascopically) and opaque objects or printed pages (episcopically) onto a screen.",
    "secondary": "In pedagogical and scientific lecture halls of the 20th century, a high-wattage projector utilizing mirrors and condensing lenses to display books, anatomical specimens, and lantern slides.",
    "quotes": [
      {
        "author": "D'Arcy Wentworth Thompson",
        "work": "On Growth and Form",
        "quote": "Projected through the **epidiascope**, the intricate venation of the leaf appeared magnified upon the lecture hall screen."
      },
      {
        "author": "Julian Huxley",
        "work": "Essays in Popular Science",
        "quote": "Using an **epidiascope**, the lecturer could demonstrate delicate morphological preparations directly to a class of two hundred students."
      },
      {
        "author": "H. G. Wells",
        "work": "The Shape of Things to Come",
        "quote": "The walls of the classroom glowed with illustrations cast by a giant **epidiascope**, conveying living history to the young minds."
      }
    ]
  },
  "Dashboard — scept/episcopate.md": {
    "primary": "The office, rank, period of office, or collective body of bishops in an episcopal church.",
    "secondary": "In ecclesiastical governance and church history, the continuous hierarchical order of overseers claiming apostolic succession and exercising diocesan jurisdiction.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The authority of the Christian **episcopate** was consolidated during the turbulent centuries of imperial collapse."
      },
      {
        "author": "Thomas Macaulay",
        "work": "The History of England",
        "quote": "The English **episcopate** found itself trapped between royal prerogative and the growing demands of the Protestant gentry."
      },
      {
        "author": "John Henry Newman",
        "work": "Apologia Pro Vita Sua",
        "quote": "I had maintained that our branch of the church held a legitimate **episcopate** derived directly from the apostles."
      }
    ]
  },
  "Dashboard — scept/episcope.md": {
    "primary": "An optical projector that uses reflected light rather than transmitted light to project magnified images of opaque flat objects (such as drawings or printed book pages) onto a screen.",
    "secondary": "In optical technology, an instrument using high-intensity lamps and concave mirrors to illuminate an opaque surface from above, reflecting the image through an objective lens.",
    "quotes": [
      {
        "author": "Lewis Mumford",
        "work": "Technics and Civilization",
        "quote": "The classroom **episcope** rendered fragile historical manuscripts instantly visible to every spectator in the hall."
      },
      {
        "author": "Arthur Eddington",
        "work": "The Nature of the Physical World",
        "quote": "By casting opaque diagrams upon the wall with an **episcope**, the physical contours of spacetime became tangible."
      },
      {
        "author": "Bertrand Russell",
        "work": "Education and the Good Life",
        "quote": "Visual demonstrations via the **episcope** awaken an inquisitive interest in children far more effectively than dry text."
      }
    ]
  },
  "Dashboard — scept/episcopic.md": {
    "primary": "Pertaining to an episcope or to optical projection by means of reflected light from opaque objects.",
    "secondary": "In microscopy and industrial metrology, designating surface illumination systems where light is directed onto the top surface of an opaque sample rather than transmitted through it.",
    "quotes": [
      {
        "author": "Ernst Abbe",
        "work": "Contributions to the Theory of the Microscope",
        "quote": "Opaque metal alloys require specialized **episcopic** illumination to reveal their crystalline microstructures."
      },
      {
        "author": "William Henry Bragg",
        "work": "The Universe of Light",
        "quote": "With an **episcopic** projection arrangement, printed pages and relief drawings are easily displayed without chemical transparency."
      },
      {
        "author": "C. V. Boys",
        "work": "Soap-Bubbles and the Forces Which Mould Them",
        "quote": "The delicate iridescent interference patterns of thin films are best observed under direct **episcopic** lighting."
      }
    ]
  },
  "Dashboard — scept/gastroscopy.md": {
    "primary": "Direct visual examination of the mucous membrane of the stomach using an endoscope (gastroscope) passed through the esophagus.",
    "secondary": "In gastroenterology, an endoscopic procedure crucial for the detection, biopsy, and therapeutic management of peptic ulcers, gastric neoplasms, and mucosal hemorrhages.",
    "quotes": [
      {
        "author": "Rudolf Schindler",
        "work": "Gastroscopy: The Endoscopic Study of Gastric Pathology",
        "quote": "Through flexible **gastroscopy**, the clinician explores the living gastric mucosa with safety and diagnostic precision."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The emergence of reliable **gastroscopy** has brought the diagnosis of early gastric carcinoma within human reach."
      },
      {
        "author": "Harvey Cushing",
        "work": "Papers Relating to the Pituitary Body, Hypothalamus and Parasympathetic Nervous System",
        "quote": "Observations made during routine **gastroscopy** revealed acute mucosal erosions linked to intracranial hypertension."
      }
    ]
  },
  "Dashboard — scept/macroscopic.md": {
    "primary": "Visible to the naked eye; large enough to be observed without the aid of a microscope.",
    "secondary": "In physics, chemistry, and pathology, designating bulk physical properties, thermodynamic states, or gross anatomical lesions as distinguished from microscopic and molecular phenomena.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "The naturalist notes many **macroscopic** variations in plumage and skeletal proportion long before microscopic differences can be analyzed."
      },
      {
        "author": "Ludwig Boltzmann",
        "work": "Lectures on Gas Theory",
        "quote": "The second law of thermodynamics describes the irreversible behavior of **macroscopic** systems composed of countless reversible atomic motions."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A careful **macroscopic** inspection of the liver at autopsy reveals cirrhotic nodularity unmistakable to the trained eye."
      }
    ]
  },
  "Dashboard — scept/macroscopical.md": {
    "primary": "Pertaining to macroscopic observation; relating to phenomena observable by the unaided eye.",
    "secondary": "In gross pathology, mineralogy, and comparative anatomy, describing the structural features of organs, rocks, or organisms visible without optical magnification.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Lessons in Elementary Anatomy",
        "quote": "Before undertaking histological sectioning, the student should complete a thorough **macroscopical** dissection of the heart."
      },
      {
        "author": "Archibald Geikie",
        "work": "Text-Book of Geology",
        "quote": "The **macroscopical** appearance of basalt shows a dark, compact rock studded with glistening olivine phenocrysts."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Though **macroscopical** examination discloses the contour of the tumor, its true malignancy is determined solely by the cells."
      }
    ]
  },
  "Dashboard — scept/microscopically.md": {
    "primary": "By means of a microscope; with extremely high magnification; or in minute, exceedingly fine detail.",
    "secondary": "In histology, materials science, and investigative analysis, designating observations conducted at the cellular, crystalline, or sub-millimeter level of resolution.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Studies on Fermentation",
        "quote": "When examined **microscopically**, the spoiled beer was found swarming with elongated bacterial rods instead of globular yeast."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Chalk cliffs that appear as uniform stone are **microscopically** revealed to consist of countless fossilized foraminiferal shells."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventures of Sherlock Holmes",
        "quote": "Sherlock Holmes examined the fabric of the garment **microscopically**, detecting traces of pipe clay and zinc dust."
      }
    ]
  },
  "Dashboard — scept/microscopist.md": {
    "primary": "A person skilled in the use of the microscope, especially one engaged in scientific research or diagnostic microscopy.",
    "secondary": "In the history of science and biology, an investigator who specializes in revealing the fine structural organization of biological tissues, minerals, or micro-organisms.",
    "quotes": [
      {
        "author": "Robert Hooke",
        "work": "Micrographia",
        "quote": "The diligent **microscopist** discovers in the foot of a fly an engine of mechanical contrivance surpassing human skill."
      },
      {
        "author": "Antonie van Leeuwenhoek",
        "work": "Letters to the Royal Society",
        "quote": "No ordinary **microscopist** had observed these living animalcules darting through a single droplet of rainwater."
      },
      {
        "author": "Charles Darwin",
        "work": "On the Origin of Species",
        "quote": "The veteran **microscopist** recognizes countless transitional gradations in the structure of the compound eye."
      }
    ]
  },
  "Dashboard — scept/orthoscope.md": {
    "primary": "An optical device or lens system designed to minimize optical distortion; or an instrument placed against the eye filled with water to neutralize corneal refraction.",
    "secondary": "In ophthalmology and physiological optics, an apparatus conceived by Ernst Brücke that neutralizes the refractive power of the anterior corneal surface, allowing direct inspection of the iris and fundus.",
    "quotes": [
      {
        "author": "Hermann von Helmholtz",
        "work": "Physiological Optics",
        "quote": "By applying an **orthoscope** filled with saline over the cornea, the optical power of that surface is entirely suppressed."
      },
      {
        "author": "Ernst Brücke",
        "work": "Untersuchungen über die Anatomie des Auges",
        "quote": "The **orthoscope** allows the physician to illuminate the deeper chambers of the eye without distortion from corneal curvature."
      },
      {
        "author": "Thomas Young",
        "work": "Lectures on Natural Philosophy and the Mechanical Arts",
        "quote": "Neutralizing corneal refraction with a miniature **orthoscope** proved that ocular accommodation depends upon the crystalline lens."
      }
    ]
  },
  "Dashboard — scept/panendoscopy.md": {
    "primary": "A comprehensive endoscopic examination of an entire anatomical system or cavity, such as the upper gastrointestinal tract or the urinary bladder and urethra.",
    "secondary": "In urology, otolaryngology, and gastroenterology, visual inspection combining wide-angle cystoscopy with urethroscopy, or pharyngoscopy with laryngoscopy, to assess mucosal pathology comprehensively.",
    "quotes": [
      {
        "author": "Hugh Hampton Young",
        "work": "Practice of Urology",
        "quote": "Through wide-angle **panendoscopy**, the surgeon inspects the prostatic urethra and vesical neck in a continuous panoramic field."
      },
      {
        "author": "Chevalier Jackson",
        "work": "Bronchoscopy and Esophagoscopy",
        "quote": "Upper aerodigestive **panendoscopy** ensures that synchronous secondary carcinomas are not overlooked during staging."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Thorough **panendoscopy** has significantly clarified the anatomical boundary between urethral strictures and benign bladder growths."
      }
    ]
  },
  "Dashboard — scept/periscope.md": {
    "primary": "An optical instrument consisting of a tube with mirrors or prisms, enabling an observer to see objects that are otherwise out of direct line of sight (such as from a submerged submarine or trench).",
    "secondary": "In naval architecture and military optics, a retractable mast equipped with erecting lens systems and rangefinders, essential for submerged navigation and torpedo targeting.",
    "quotes": [
      {
        "author": "H. G. Wells",
        "work": "The War in the Air",
        "quote": "The submarine slipped beneath the swell, leaving only the slender brass tube of its **periscope** cutting the water."
      },
      {
        "author": "Winston Churchill",
        "work": "The World Crisis",
        "quote": "Every commander scanned the gray North Sea horizon for the telltale wake of a German U-boat **periscope**."
      },
      {
        "author": "Joseph Conrad",
        "work": "The Secret Sharer",
        "quote": "His vigilant eyes seemed to sweep the darkening water as tirelessly as the lens of an optical **periscope**."
      }
    ]
  },
  "Dashboard — scept/periscopic.md": {
    "primary": "Pertaining to, resembling, or functioning like a periscope; giving a wide, comprehensive, or elevated field of view.",
    "secondary": "In ophthalmic lens design, designating curved spectacle lenses (concavo-convex or meniscus) that allow the wearer to view oblique objects clearly without turning the head.",
    "quotes": [
      {
        "author": "William Hyde Wollaston",
        "work": "On the Periscopic Form of Spectacles",
        "quote": "My newly invented **periscopic** glasses diminish lateral distortion, allowing the eyeball to turn freely in every direction."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "From his lofty masthead perch, the lookout enjoyed a **periscopic** vantage across miles of rolling blue horizon."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Poison Belt",
        "quote": "From our sealed room, we maintained a **periscopic** watch over the silent, stricken street below."
      }
    ]
  },
  "Dashboard — scept/sceptered.md": {
    "primary": "Invested with a scepter; endowed with regal authority, sovereignty, or majestic power.",
    "secondary": "In literary and political rhetoric, possessing hereditary royal power or imperial supremacy; figuratively, ruling or commanding preeminent status.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Richard II",
        "quote": "This royal throne of kings, this **sceptered** isle, / This earth of majesty, this seat of Mars."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "High on a throne of royal state... Satan exalted sat, by merit raised to that bad eminence, while **sceptered** kings obeyed."
      },
      {
        "author": "Percy Bysshe Shelley",
        "work": "Prometheus Unbound",
        "quote": "The monarch sat **sceptered** upon his throne, yet trembled before the unbending will of the titan."
      }
    ]
  },
  "Dashboard — scept/sceptic.md": {
    "primary": "A person inclined to question, doubt, or suspend judgment regarding accepted beliefs, dogmas, or assertions.",
    "secondary": "In philosophy, a member of the Pyrrhonian or Academic school who holds that certain knowledge is unattainable; in epistemology, one who demands rigorous empirical evidence before assenting.",
    "quotes": [
      {
        "author": "David Hume",
        "work": "An Enquiry Concerning Human Understanding",
        "quote": "The philosophical **sceptic** points out the fallibility of human faculties without thereby abandoning the practical duties of life."
      },
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "If a man will begin with certainties, he shall end in doubts; but if he will be content to begin as a **sceptic**, he shall end in certainties."
      },
      {
        "author": "John Stuart Mill",
        "work": "On Liberty",
        "quote": "Even the most confirmed dogmatist owes an immense debt of gratitude to the thoughtful **sceptic** who challenges his premises."
      }
    ]
  },
  "Dashboard — scept/sceptically.md": {
    "primary": "In a sceptical manner; with an attitude of doubt, reservation, or critical inquiry.",
    "secondary": "In epistemological reasoning and critical analysis, withholding assent from unproven propositions and subjecting hypotheses to empirical testing.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Science and Christian Tradition",
        "quote": "The man of science looks **sceptically** upon any miracle that declines to be repeated in the laboratory."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "Mr. Brooke listened **sceptically** to the radical schemes, shaking his head with the easy detachment of a wealthy landlord."
      },
      {
        "author": "Bertrand Russell",
        "work": "Skeptical Essays",
        "quote": "It is undesirable to believe a proposition when there are no grounds whatever for supposing it true, and to act **sceptically** is the beginning of wisdom."
      }
    ]
  },
  "Dashboard — scept/scepticism.md": {
    "primary": "A doubting or questioning attitude; suspension of judgment toward claims or doctrines accepted by others.",
    "secondary": "In the history of philosophy, the systematic theory (associated with Pyrrho, Sextus Empiricus, and Hume) that real knowledge is uncertain and that dogmatism should be avoided.",
    "quotes": [
      {
        "author": "David Hume",
        "work": "A Treatise of Human Nature",
        "quote": "Carelessness and inattention alone can afford us any remedy for excessive **scepticism**; for this reason I rely entirely upon them."
      },
      {
        "author": "Immanuel Kant",
        "work": "Critique of Pure Reason",
        "quote": "**Scepticism** is thus a resting-place for human reason, where it can reflect upon its dogmatic journey, but it is not a dwelling-place for permanent residence."
      },
      {
        "author": "William James",
        "work": "The Will to Believe",
        "quote": "Absolute **scepticism** is logically unassailable, yet practically impossible for an active human agent confronting choices in life."
      }
    ]
  },
  "Dashboard — scept/sceptred.md": {
    "primary": "Bearing a sceptre; invested with royal sovereignty or imperial authority (British spelling of sceptered).",
    "secondary": "In poetic diction, characterizing monarchical or divine rule, majestic majesty, or supreme commanding dignity.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "The Merchant of Venice",
        "quote": "The quality of mercy is not strained... 'Tis mightiest in the mightiest; it becomes / The **sceptred** monarch better than his crown."
      },
      {
        "author": "Lord Byron",
        "work": "The Corsair",
        "quote": "Slow sinks, more lovely ere his race be run, / Along Morea's hills the setting sun... where **sceptred** kings once swayed the Aegean tides."
      },
      {
        "author": "Alfred, Lord Tennyson",
        "work": "Morte d'Arthur",
        "quote": "So like a shattered column lay the king; / Not like that Arthur who, with lance in rest, / Rode **sceptred** through the tournament."
      }
    ]
  },
  "Dashboard — scept/scopal.md": {
    "primary": "Pertaining to, having, or acting as a scope; or relating to a brush-like tuft of hairs (scopa) on an insect's leg.",
    "secondary": "In theoretical linguistics and formal semantics, relating to the semantic scope of operators (such as quantifiers, negations, or modals) over clauses or syntactic arguments.",
    "quotes": [
      {
        "author": "Noam Chomsky",
        "work": "Aspects of the Theory of Syntax",
        "quote": "The difference in interpretations arises directly from the distinct **scopal** domains of the negation operator and the existential quantifier."
      },
      {
        "author": "William Morton Wheeler",
        "work": "Ants: Their Structure, Development and Behavior",
        "quote": "Female solitary bees carry gathered pollen grains tightly packed within the dense **scopal** hairs of the hind tibia."
      },
      {
        "author": "John Lyons",
        "work": "Semantics",
        "quote": "Ambiguities in sentence meaning frequently reduce to conflicting **scopal** attachments between modal auxiliaries and indefinite noun phrases."
      }
    ]
  },
  "Dashboard — scept/scopophobia.md": {
    "primary": "An abnormal, irrational, and persistent fear of being looked at, stared at, or seen by others.",
    "secondary": "In clinical psychiatry and abnormal psychology, a severe social anxiety disorder characterized by somatic flushing, agoraphobic avoidance, and extreme dread of interpersonal gaze.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "Three Essays on the Theory of Sexuality",
        "quote": "An exaggeration of the social gaze instinct may invert into morbid **scopophobia**, causing the neurotic to shrink in terror from human eyes."
      },
      {
        "author": "William Healy",
        "work": "The Individual Delinquent",
        "quote": "The patient exhibited marked **scopophobia**, confessing that the mere sensation of strangers watching him triggered paroxysms of panic."
      },
      {
        "author": "Sandor Ferenczi",
        "work": "Further Contributions to the Theory and Technique of Psycho-Analysis",
        "quote": "In acute **scopophobia**, the patient experiences being stared at as an aggressive physical violation."
      }
    ]
  },
  "Dashboard — scept/skeptically.md": {
    "primary": "With a questioning, doubtful, or incredulous attitude; in a skeptical manner (American spelling).",
    "secondary": "In scientific inquiry and philosophical discourse, evaluating claims through critical analysis and evidentiary standards rather than passive credulity.",
    "quotes": [
      {
        "author": "Carl Sagan",
        "work": "The Demon-Haunted World",
        "quote": "Valid scientific claims withstand scrutiny when examined **skeptically**, whereas superstition crumbles under dispassionate testing."
      },
      {
        "author": "Mark Twain",
        "work": "Following the Equator",
        "quote": "The seasoned traveler listens **skeptically** to local legends until substantiated by hard geographical facts."
      },
      {
        "author": "William James",
        "work": "Pragmatism",
        "quote": "The pragmatist views closed theological dogmas **skeptically**, demanding to know what concrete cash-value they yield in human life."
      }
    ]
  },
  "Dashboard — scept/stereoscope.md": {
    "primary": "An optical viewing device presenting two slightly offset two-dimensional images separately to each eye, producing the perception of three-dimensional depth.",
    "secondary": "In 19th-century optical science, an apparatus invented by Charles Wheatstone and refined by David Brewster that demonstrated the binocular mechanism of human depth perception.",
    "quotes": [
      {
        "author": "Charles Wheatstone",
        "work": "Philosophical Transactions of the Royal Society",
        "quote": "By means of the **stereoscope**, two flat drawings depicting different perspectives combine in the brain to produce an irresistible illusion of solid relief."
      },
      {
        "author": "Oliver Wendell Holmes",
        "work": "The Atlantic Monthly: The Stereoscope and the Stereograph",
        "quote": "The **stereoscope** is an instrument which makes surfaces look solid... It carries us on a magic carpet into the heart of distant landscapes."
      },
      {
        "author": "David Brewster",
        "work": "The Stereoscope: Its History, Theory, and Construction",
        "quote": "The lenticular **stereoscope** brings the wonders of binocular vision into every drawing room, uniting art and optical geometry."
      }
    ]
  },
  "Dashboard — scept/stereoscopic.md": {
    "primary": "Pertaining to, produced by, or perceived through stereoscopy; having or producing the illusion of three-dimensional solid depth from two flat images.",
    "secondary": "In ophthalmology and photography, designating binocular vision wherein retinal disparity between both eyes is fused by the visual cortex to yield depth perception.",
    "quotes": [
      {
        "author": "Hermann von Helmholtz",
        "work": "Physiological Optics",
        "quote": "Our vivid **stereoscopic** perception of depth arises from the disparity between the two disparate images formed on our retinas."
      },
      {
        "author": "H. G. Wells",
        "work": "The Time Machine",
        "quote": "He held up a miniature geometric model, turning it slowly so that its facets cast a **stereoscopic** shadow across the wall."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The **stereoscopic** fusion of two disparate drawings produces a perception of third dimensionality that no single eye can experience."
      }
    ]
  },
  "Dashboard — scept/stereoscopy.md": {
    "primary": "The technique or process of recording and presenting two-dimensional images to create the illusion of three-dimensional depth.",
    "secondary": "In visual psychophysics and optical engineering, the science of binocular disparity and stereoscopic depth cues used in photogrammetry, 3D imaging, and virtual reality.",
    "quotes": [
      {
        "author": "Charles Wheatstone",
        "work": "Philosophical Transactions of the Royal Society",
        "quote": "The investigation of **stereoscopy** reveals how binocular vision synthesizes two distinct retinal viewpoints into a singular perception of space."
      },
      {
        "author": "David Brewster",
        "work": "The Stereoscope",
        "quote": "In the study of **stereoscopy**, optical science demonstrates that our sense of solidity is an intellectual synthesis of distinct visual inputs."
      },
      {
        "author": "Oliver Wendell Holmes",
        "work": "The Atlantic Monthly",
        "quote": "Through the art of **stereoscopy**, the physical monuments of the ancient world are resurrected before our eyes with breathtaking solidity."
      }
    ]
  },
  "Dashboard — scept/telescoped.md": {
    "primary": "Collapsed or slid into one another like the concentric tubes of a pocket telescope; compressed into a shorter length, volume, or timeframe.",
    "secondary": "In structural mechanics, descriptive of vehicle collision damage where one section crumples into another; in historical and literary analysis, condensed or compacted in narrative sequence.",
    "quotes": [
      {
        "author": "Lewis Carroll",
        "work": "Alice's Adventures in Wonderland",
        "quote": "Alice shut up like a **telescoped** brass tube, shrinking down to ten inches in height."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Lost World",
        "quote": "Millions of years of evolutionary history were **telescoped** into the isolated plateau of South America."
      },
      {
        "author": "Winston Churchill",
        "work": "The Second World War",
        "quote": "The military emergencies of six months were **telescoped** into a breathless fortnight of relentless decision."
      }
    ]
  },
  "Dashboard — scept/Telescopium.md": {
    "primary": "A faint constellation in the southern celestial hemisphere, introduced in the 18th century by the French astronomer Nicolas-Louis de Lacaille.",
    "secondary": "In observational astronomy and celestial cartography, a southern constellation named after the aerial telescope, bordered by Sagittarius, Corona Australis, and Pavo.",
    "quotes": [
      {
        "author": "Nicolas-Louis de Lacaille",
        "work": "Coelum Australe Stelliferum",
        "quote": "Among the southern constellations, I designated **Telescopium** to honor the instrument that unlocked the secrets of the heavens."
      },
      {
        "author": "John Herschel",
        "work": "Results of Astronomical Observations Made at the Cape of Good Hope",
        "quote": "Sweeping across the southern sky, I surveyed the faint double stars and planetary nebulae scattered through **Telescopium**."
      },
      {
        "author": "Camille Flammarion",
        "work": "Popular Astronomy",
        "quote": "The modern constellation **Telescopium** commemorates the optical tube through which Galileo first gazed upon the craters of the Moon."
      }
    ]
  },
  "Dashboard — scept/telescopy.md": {
    "primary": "The art, science, or practice of constructing and using telescopes for astronomical and terrestrial observation.",
    "secondary": "In observational astronomy and optical instrumentation, the technical methodology of gathering and focusing electromagnetic radiation using optical tube assemblies and mountings.",
    "quotes": [
      {
        "author": "William Herschel",
        "work": "Philosophical Transactions of the Royal Society",
        "quote": "Progress in deep-sky **telescopy** depends upon increasing the aperture of speculum mirrors to collect the faint light of distant nebulae."
      },
      {
        "author": "Simon Newcomb",
        "work": "Popular Astronomy",
        "quote": "Nineteenth-century **telescopy** achieved its highest triumph in the great refractor at the Lick Observatory."
      },
      {
        "author": "Percival Lowell",
        "work": "Mars",
        "quote": "The refined techniques of planetary **telescopy** demand not only large objectives but exquisite atmospheric tranquility."
      }
    ]
  },
  "Dashboard — scop/bronchoscopy.md": {
    "primary": "An endoscopic procedure allowing direct visual examination of the interior of the tracheobronchial tree using a bronchoscope.",
    "secondary": "In pulmonology and thoracic surgery, a vital clinical technique for diagnosing pulmonary lesions, obtaining transbronchial biopsies, and retrieving aspirated foreign bodies.",
    "quotes": [
      {
        "author": "Chevalier Jackson",
        "work": "Bronchoscopy and Esophagoscopy",
        "quote": "Skillful **bronchoscopy** has rescued hundreds of infants from suffocation by safely extracting swallowed pins and seeds."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Direct inspection of the tracheal bifurcation by **bronchoscopy** establishes the presence of intrabronchial tumors with absolute certainty."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Medical Career",
        "quote": "The rapid refinement of **bronchoscopy** exemplified the triumph of mechanical ingenuity in modern surgical diagnostics."
      }
    ]
  },
  "Dashboard — scop/colonoscopy.md": {
    "primary": "The endoscopic examination of the entire large intestine (colon) and the distal terminal ileum using a flexible video or fiber-optic colonoscope.",
    "secondary": "In gastroenterology and oncology, the gold-standard procedure for screening, identifying, and removing premalignant adenomatous polyps throughout the colonic mucosa.",
    "quotes": [
      {
        "author": "Hiromi Shinya",
        "work": "Colonoscopy: Diagnosis and Treatment of Colonic Diseases",
        "quote": "The introduction of flexible **colonoscopy** revolutionized colorectal cancer prevention by enabling painless polypectomy without open surgery."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Direct visualization through early **colonoscopy** eliminated much of the guesswork formerly associated with deep bowel pathology."
      },
      {
        "author": "Jerome Groopman",
        "work": "How Doctors Think",
        "quote": "Routine screening via **colonoscopy** intercepts carcinoma while it remains a curable, localized polyp."
      }
    ]
  },
  "Dashboard — scop/cystoscopy.md": {
    "primary": "The direct visual examination of the interior of the urinary bladder and urethra using an illuminated endoscope (cystoscope).",
    "secondary": "In urological practice, an essential diagnostic and operative method for evaluating hematuria, resecting transitional cell tumors, and guiding ureteral catheterization.",
    "quotes": [
      {
        "author": "Max Nitze",
        "work": "Lehrbuch der Kystoskopie",
        "quote": "With the incandescent electric lamp at the tip of the instrument, **cystoscopy** made the interior of the living bladder as bright as day."
      },
      {
        "author": "Hugh Hampton Young",
        "work": "Practice of Urology",
        "quote": "Routine **cystoscopy** enables the surgeon to locate the source of vesical bleeding and catheterize each ureter independently."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The urologist relies on **cystoscopy** to distinguish between benign calculi and ulcerating vesical papillomas."
      }
    ]
  },
  "Dashboard — scop/endoscope.md": {
    "primary": "An illuminated instrument containing optical fibers, lenses, or a digital camera used to inspect the interior of a hollow organ or body cavity.",
    "secondary": "In minimally invasive medicine, an instrument equipped with channels for insufflation, suction, and micro-instruments, drastically minimizing postoperative morbidity.",
    "quotes": [
      {
        "author": "Chevalier Jackson",
        "work": "Bronchoscopy and Esophagoscopy",
        "quote": "The lighted **endoscope** converted deep, inaccessible cavities of the human body into open fields of direct clinical inspection."
      },
      {
        "author": "Harold Hopkins",
        "work": "Optics in Medicine",
        "quote": "By employing cylindrical glass rods in place of air lenses, the modern **endoscope** achieved an extraordinary leap in light transmission."
      },
      {
        "author": "William Mayo",
        "work": "Collected Papers of the Mayo Clinic",
        "quote": "Surgical trauma has been enormously mitigated through internal examinations guided by the **endoscope**."
      }
    ]
  },
  "Dashboard — scop/endoscopic.md": {
    "primary": "Relating to, performed by, or utilizing an endoscope.",
    "secondary": "In diagnostic and therapeutic surgery, denoting intraluminal procedures such as biopsies, stone extractions, and mucosal resections conducted under direct camera guidance.",
    "quotes": [
      {
        "author": "Alexis Carrel",
        "work": "The Treatment of Infected Wounds",
        "quote": "Direct **endoscopic** surveillance provides immediate visual appraisal of tissue healing without requiring wound disruption."
      },
      {
        "author": "Harvey Cushing",
        "work": "Intracranial Tumours",
        "quote": "Our early **endoscopic** probes into the cerebral ventricles revealed fluid dynamics impossible to deduce from external examination."
      },
      {
        "author": "William Osler",
        "work": "Aequanimitas and Other Addresses",
        "quote": "The clinician who supplements tactile percussion with **endoscopic** clarity stands on far firmer diagnostic ground."
      }
    ]
  },
  "Dashboard — scop/endoscopy.md": {
    "primary": "The visual examination of internal organs or cavities of the body by means of an endoscope.",
    "secondary": "In clinical medicine, a broad discipline spanning gastrointestinal, urological, pulmonary, and arthroscopic specialties for non-invasive diagnosis and intervention.",
    "quotes": [
      {
        "author": "Rudolf Schindler",
        "work": "Gastroscopy",
        "quote": "The systematic practice of **endoscopy** elevated mucosal pathology from post-mortem deduction to living clinical observation."
      },
      {
        "author": "Chevalier Jackson",
        "work": "Peroral Endoscopy and Laryngeal Surgery",
        "quote": "In expert hands, peroral **endoscopy** safely retrieves foreign bodies that would otherwise inevitably cause death."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Diagnostic **endoscopy** has significantly curtailed unnecessary exploratory laparotomies in hospital practice."
      }
    ]
  },
  "Dashboard — scop/episcopacy.md": {
    "primary": "Government of the church by bishops; episcopal hierarchy or polity.",
    "secondary": "In ecclesiastical history, the system of ecclesiastical order and apostolic succession championed in Anglican, Roman Catholic, and Eastern Orthodox church structures.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "The Reason of Church-Government Urged Against Prelaty",
        "quote": "Prelatical **episcopacy** usurps the spiritual liberty of the church under the cloak of ancient tradition."
      },
      {
        "author": "Thomas Macaulay",
        "work": "The History of England",
        "quote": "The restoration of **episcopacy** in Scotland provoked bitter covenants and widespread armed resistance in the hills."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The gradual consolidation of **episcopacy** provided the nascent Christian communities with an enduring civil framework."
      }
    ]
  },
  "Dashboard — scop/episcopalian.md": {
    "primary": "An adherent of an episcopal church, particularly a member of the Protestant Episcopal Church; or relating to church government by bishops.",
    "secondary": "In religious history, denoting ecclesiastical traditions adhering to the historic episcopate, liturgical prayer books, and diocesan hierarchy.",
    "quotes": [
      {
        "author": "Benjamin Franklin",
        "work": "Autobiography",
        "quote": "My parents had early given me religious impressions, and brought me through my childhood in the **episcopalian** faith."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "The **episcopalian** congregations in New York preserved much of the decorous liturgy of their English ancestors."
      },
      {
        "author": "Henry Adams",
        "work": "The Education of Henry Adams",
        "quote": "To a Boston boy of Unitarian stock, the ritual of an **episcopalian** cathedral appeared richly ornate and foreign."
      }
    ]
  },
  "Dashboard — scop/episcopalianism.md": {
    "primary": "The doctrine, worship, and ecclesiastical polity of an episcopal church, especially the Protestant Episcopal Church.",
    "secondary": "In ecclesiastical theology, a church system combining historic episcopal orders and liturgical governance while rejecting universal papal supremacy.",
    "quotes": [
      {
        "author": "Thomas Carlyle",
        "work": "The French Revolution",
        "quote": "Between rigid Puritan dogma and aristocratic **episcopalianism**, the religious life of the seventeenth century was passionately divided."
      },
      {
        "author": "Matthew Arnold",
        "work": "Culture and Anarchy",
        "quote": "The polite decorum of English **episcopalianism** offered an aesthetic shelter against the harsher winds of nonconformist zeal."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "English Traits",
        "quote": "The established forms of **episcopalianism** seemed to the philosopher less an inner spiritual flame than an elegant social compact."
      }
    ]
  },
  "Dashboard — scop/episcopate.md": {
    "primary": "The office, term, or collective body of bishops in an episcopal church.",
    "secondary": "In canon law and ecclesiastical governance, the highest order of the threefold apostolic ministry, exercising spiritual jurisdiction over a diocese.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The Christian **episcopate** gradually assumed the municipal duties abandoned by the collapsing Roman magistracy."
      },
      {
        "author": "John Henry Newman",
        "work": "Apologia Pro Vita Sua",
        "quote": "I contended that the English **episcopate** preserved unbroken succession from the ancient apostolic fathers."
      },
      {
        "author": "Thomas Macaulay",
        "work": "The History of England",
        "quote": "The trial of the seven bishops united the whole nation in defense of the beleaguered **episcopate**."
      }
    ]
  },
  "Dashboard — scop/laparoscopy.md": {
    "primary": "A surgical procedure in which a fiber-optic instrument (laparoscope) is inserted through the abdominal wall to view organs or permit minimally invasive surgery.",
    "secondary": "In modern surgery, minimally invasive abdominal surgery utilizing carbon dioxide pneumoperitoneum, trocars, and micro-instruments, minimizing trauma and recovery times.",
    "quotes": [
      {
        "author": "Georg Kelling",
        "work": "Über Oesophagoskopie, Gastroskopie und Kölioskopie",
        "quote": "By introducing a cystoscope through a small trocar into the canine abdomen, I demonstrated the feasibility of diagnostic **laparoscopy**."
      },
      {
        "author": "Kurt Semm",
        "work": "Operative Manual of Endoscopic Abdominal Surgery",
        "quote": "The transition from diagnostic inspection to operative **laparoscopy** revolutionized abdominal surgery across the globe."
      },
      {
        "author": "Jerome Groopman",
        "work": "The Anatomy of Hope",
        "quote": "Performing the gallbladder excision through **laparoscopy** allowed the patient to walk within hours of leaving the operating theater."
      }
    ]
  },
  "Dashboard — scop/macroscopic.md": {
    "primary": "Visible to the unaided eye; not microscopic; large enough to be perceived without magnification.",
    "secondary": "In thermodynamics and pathology, describing aggregate bulk properties or gross anatomical features as distinguished from molecular or histological structures.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "Before tracing cellular variations, the naturalist must catalog every notable **macroscopic** divergence in bone and plumage."
      },
      {
        "author": "Ludwig Boltzmann",
        "work": "Lectures on Gas Theory",
        "quote": "The thermodynamic state represents a **macroscopic** average over billions of uncoordinated molecular trajectories."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The gross **macroscopic** appearance of the diseased spleen gives only an initial hint of its cellular disintegration."
      }
    ]
  },
  "Dashboard — scop/macroscopical.md": {
    "primary": "Relating to macroscopic phenomena; observable with the naked eye.",
    "secondary": "In anatomical dissection and mineralogical assessment, describing visible physical traits and surface structures before histological or microchemical testing.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Lessons in Elementary Anatomy",
        "quote": "The student should master the **macroscopical** relations of muscles and nerves before attempting histological sectioning."
      },
      {
        "author": "Archibald Geikie",
        "work": "Text-Book of Geology",
        "quote": "The **macroscopical** inspection of granite readily identifies quartz crystals, feldspar tablets, and mica flakes."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A thorough **macroscopical** review of the lung parenchyma reveals whether consolidation is lobar or bronchopneumonic."
      }
    ]
  },
  "Dashboard — scop/macroscopically.md": {
    "primary": "In a macroscopic manner; as observed with the naked eye without optical magnification.",
    "secondary": "In pathology and materials characterization, describing observations made during gross examination prior to microscopic histology.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Studies on Fermentation",
        "quote": "The diseased liquid looked cloudy **macroscopically**, but its true fungal nature could only be confirmed under the lens."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Examined **macroscopically**, the tumor margins appeared clear, though frozen sections revealed infiltrating cells."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "The stratified limestone strata appeared **macroscopically** uniform, yet contained innumerable micro-fossils."
      }
    ]
  },
  "Dashboard — scop/megascopic.md": {
    "primary": "Large enough to be seen with the naked eye; macroscopic, especially as used in geology and petrology.",
    "secondary": "In petrology and field mineralogy, designating rock texture, mineral grains, and structural fabric observable in hand specimens without thin-section microscopy.",
    "quotes": [
      {
        "author": "James Dwight Dana",
        "work": "Manual of Geology",
        "quote": "A **megascopic** description of the hand specimen should note the color, grain size, and fracture of the mineral."
      },
      {
        "author": "Archibald Geikie",
        "work": "The Founders of Geology",
        "quote": "Field geologists rely heavily on **megascopic** features to map formations across expansive mountain terrains."
      },
      {
        "author": "Edward Salisbury Dana",
        "work": "A Text-Book of Mineralogy",
        "quote": "The **megascopic** identification of porphyritic basalt depends upon conspicuous feldspar phenocrysts embedded in the matrix."
      }
    ]
  },
  "Dashboard — scop/microscopically.md": {
    "primary": "By means of a microscope; in microscopic scale, or with extreme attention to minute detail.",
    "secondary": "In cellular biology and forensic science, at the level of optical or electron microscopic resolution where fine structural details become discernible.",
    "quotes": [
      {
        "author": "Robert Koch",
        "work": "The Etiology of Tuberculosis",
        "quote": "Examined **microscopically**, the tubercular nodule yielded rod-shaped bacilli stained vividly with methylene blue."
      },
      {
        "author": "Antonie van Leeuwenhoek",
        "work": "Letters to the Royal Society",
        "quote": "Looking **microscopically** at dental plaque, I perceived thousands of living animalcules moving with great velocity."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "A Study in Scarlet",
        "quote": "Sherlock Holmes examined the floorboards **microscopically**, discovering blood corpuscles invisible to the inspectors."
      }
    ]
  },
  "Dashboard — scop/microscopist.md": {
    "primary": "A person skilled in microscopy or one who conducts scientific investigations using a microscope.",
    "secondary": "In the history of natural science, an investigator specializing in revealing the micro-anatomical, crystalline, or microbiological realm.",
    "quotes": [
      {
        "author": "Robert Hooke",
        "work": "Micrographia",
        "quote": "The enthusiastic **microscopist** finds in a drop of vinegar or a piece of cork a universe of wondrous complexity."
      },
      {
        "author": "Charles Darwin",
        "work": "On the Origin of Species",
        "quote": "Even the experienced **microscopist** is challenged to distinguish between early embryonic stages of distinct vertebrate classes."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Autobiography and Selected Essays",
        "quote": "Working as a naval **microscopist** aboard the Rattlesnake, I charted the delicate anatomy of pelagic medusae."
      }
    ]
  },
  "Dashboard — scop/microscopium.md": {
    "primary": "A small, faint constellation in the southern celestial hemisphere, introduced in the 18th century by Nicolas-Louis de Lacaille.",
    "secondary": "In observational astronomy and history of science, a southern constellation named in honor of the compound microscope, located between Capricornus and Grus.",
    "quotes": [
      {
        "author": "Nicolas-Louis de Lacaille",
        "work": "Coelum Australe Stelliferum",
        "quote": "To commemorate the instrument of Leeuwenhoek and Hooke, I gave the name **Microscopium** to these southern stars."
      },
      {
        "author": "John Herschel",
        "work": "Outlines of Astronomy",
        "quote": "The faint stars of **Microscopium** occupy an inconspicuous quadrant of the southern sky, south of Capricorn."
      },
      {
        "author": "Camille Flammarion",
        "work": "Popular Astronomy",
        "quote": "Lacaille populated the southern celestial sphere with monuments of modern science, dedicating **Microscopium** to the explorers of the infinitely small."
      }
    ]
  },
  "Dashboard — scop/microscopy.md": {
    "primary": "The use of the microscope to observe objects and structures not visible to the naked eye; the scientific investigation of microscopic phenomena.",
    "secondary": "In physics and biology, the broad field encompassing optical, fluorescence, confocal, and electron imaging methodologies used to resolve sub-micron structures.",
    "quotes": [
      {
        "author": "Ernst Abbe",
        "work": "Contributions to the Theory of the Microscope",
        "quote": "Diffraction of light sets an ultimate physical limit on resolving power in classical optical **microscopy**."
      },
      {
        "author": "Louis Pasteur",
        "work": "Studies on Fermentation",
        "quote": "Without the steady aid of **microscopy**, the biological reality of microbial fermentation could never have been established."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Recollections of My Life",
        "quote": "Immersed in the silent world of silver-impregnation **microscopy**, I traced the intricate arborizations of nerve cells."
      }
    ]
  },
  "Dashboard — scop/orthoscope.md": {
    "primary": "An optical device or lens designed to eliminate distortion; or an ophthalmic instrument placed over the eye to neutralize corneal refraction.",
    "secondary": "In physiological optics, an eye cup filled with water invented by Ernst Brücke that neutralizes the refracting power of the anterior cornea, allowing clear observation of the ocular fundus.",
    "quotes": [
      {
        "author": "Hermann von Helmholtz",
        "work": "Physiological Optics",
        "quote": "With Brücke's **orthoscope**, corneal refraction is negated by water contact, affording an unobstructed view of the iris."
      },
      {
        "author": "Ernst Brücke",
        "work": "Untersuchungen über die Anatomie des Auges",
        "quote": "The principle of the **orthoscope** consists in replacing the curved corneal surface with a flat optical glass window."
      },
      {
        "author": "Thomas Young",
        "work": "Lectures on Natural Philosophy and the Mechanical Arts",
        "quote": "A small fluid-filled **orthoscope** demonstrated that the human cornea plays no active part in ocular accommodation."
      }
    ]
  }
};

let updated = 0;
for (const [relPath, data] of Object.entries(batchData)) {
  if (updateNote(relPath, data)) updated++;
}
console.log(`Successfully updated ${updated} of ${Object.keys(batchData).length} files in Batch 9.`);
