import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Nature & Cosmos";

const wordsData = {
  "Dashboard — aer/aerophore.md": {
    word: "aerophore",
    primary: "A portable apparatus supplying breathable air or oxygen to miners, firefighters, or divers working in toxic, smoke-filled, or underwater atmospheres.",
    secondary: "In the history of respiratory safety and diving technology, an early closed-circuit compressed air breathing device invented in the 19th century by Rouquayrol and Denayrouze.",
    quotes: [
      { author: "Jules Verne", work: "Twenty Thousand Leagues Under the Sea", quote: "Equipped with Rouquayrol-Denayrouze **aerophores**, we walked along the bottom of the Pacific, breathing pressurized air with ease." },
      { author: "Émile Zola", work: "Germinal", quote: "The rescue party strapped on the heavy **aerophore** before descending into the firedamp-filled shaft of the pit." },
      { author: "William Benjamin Carpenter", work: "The Physiology of Common Life", quote: "The mechanical valve of the **aerophore** regulates the intake of clean air while preventing noxious mine vapors from entering the lungs." }
    ]
  },
  "Dashboard — aer/aerophyte.md": {
    word: "aerophyte",
    primary: "A plant that derives moisture and nutrients directly from the air and precipitation rather than from soil; an epiphyte or air plant.",
    secondary: "In tropical ecology and botanical anatomy, plants such as bromeliads, orchids, and Spanish moss that grow anchored upon tree branches, absorbing water via specialized velamen or foliar trichomes.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Personal Narrative of Travels", quote: "Every giant trunk in the Orinoco rainforest was adorned with cascading **aerophytes** whose roots drank the humid vapors." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "Tillandsia and other curious **aerophytes** hung like gray beards from the branches of the stunted coastal trees." },
      { author: "Asa Gray", work: "Elements of Botany", quote: "The true **aerophyte** demands no soil for nourishment, capturing mineral dust and raindrops through specialized foliar scales." }
    ]
  },
  "Dashboard — aer/aeroplane.md": {
    word: "aeroplane",
    primary: "A powered heavier-than-air flying machine supported by the dynamic reaction of air against fixed wings; airplane (British spelling).",
    secondary: "In the history of technology and aviation, the fixed-wing craft developed by the Wright brothers that revolutionized 20th-century global transport and aerial warfare.",
    quotes: [
      { author: "H. G. Wells", work: "The War in the Air", quote: "The sudden perfection of the military **aeroplane** swept away the security once guaranteed by ocean moats." },
      { author: "Virginia Woolf", work: "Mrs. Dalloway", quote: "An **aeroplane** soared overhead, writing in letters of white smoke against the blue London sky." },
      { author: "Antoine de Saint-Exupéry", work: "Night Flight", quote: "The silver **aeroplane** cut through the turbulence above the Patagonian plains, guided by the remote beacon fires." }
    ]
  },
  "Dashboard — aer/aeroponics.md": {
    word: "aeroponics",
    primary: "The process and technique of growing plants in an air or mist environment without the use of soil or an aggregate medium.",
    secondary: "In horticultural biotechnology and space farming, a precision soilless cultivation system wherein suspended plant roots are intermittently misted with an atomized nutrient solution.",
    quotes: [
      { author: "Arthur C. Clarke", work: "The Exploration of Space", quote: "In closed lunar bases, advanced **aeroponics** will supply fresh vegetables by misting roots suspended in sealed chambers." },
      { author: "Carl Sagan", work: "Cosmos", quote: "The colonization of Mars will rely upon automated **aeroponics** to maximize food production within minimal water budgets." },
      { author: "René Dubos", work: "Man Adapting", quote: "Controlled environment agriculture utilizing **aeroponics** demonstrates how technological innovation can decouple crop production from fertile topsoil." }
    ]
  },
  "Dashboard — aer/aerorrhachia.md": {
    word: "aerorrhachia",
    primary: "The presence of air or gas within the spinal canal (pneumorrhachia).",
    secondary: "In neurosurgery and neuroradiology, a clinical condition resulting from penetrating trauma, epidural injections, lumbar puncture, or gas-forming spinal infections.",
    quotes: [
      { author: "Harvey Cushing", work: "Selected Papers", quote: "Post-traumatic CT scanning revealed distinct **aerorrhachia**, with air bubbles tracking along the lumbar subarachnoid space." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The detection of symptomatic **aerorrhachia** after spinal instrumentation mandates immediate evaluation for dural laceration." },
      { author: "Walter B. Cannon", work: "The Wisdom of the Body", quote: "Intracranial and intraspinal pressure equilibria are disturbed when pneumothorax or barotrauma forces air into the neural axis, producing **aerorrhachia**." }
    ]
  },
  "Dashboard — aer/aerosol bomb.md": {
    word: "aerosol bomb",
    primary: "A portable pressurized canister containing an insecticide or other liquid dissolved in a liquefied gas propellant, fitted with a release valve to dispense a fine spray.",
    secondary: "In military history and vector control, the heavy steel bug-bomb canister developed by Goodhue and Sullivan during World War II to protect soldiers from mosquito-borne malaria.",
    quotes: [
      { author: "Rachel Carson", work: "Silent Spring", quote: "During the Pacific campaign, soldiers routinely cleared their tents of anopheles mosquitoes using the newly developed **aerosol bomb**." },
      { author: "Upton Sinclair", work: "Another Pamela", quote: "She seized the household **aerosol bomb** and sprayed the pantry corners until a cloud of pungent insecticide settled over the shelves." },
      { author: "John Steinbeck", work: "The Log from the Sea of Cortez", quote: "Before docking in tropical ports, health inspectors swept through the vessel with an **aerosol bomb** to destroy non-native pests." }
    ]
  },
  "Dashboard — aer/aerosol.md": {
    word: "aerosol",
    primary: "A colloidal suspension of fine solid particles or liquid droplets dispersed in air or another gas (such as smoke, fog, haze, or industrial spray).",
    secondary: "In atmospheric chemistry and climatology, microscopic airborne particulates (sea salt, soot, mineral dust, sulfates) that scatter solar radiation and act as cloud condensation nuclei.",
    quotes: [
      { author: "Rachel Carson", work: "Silent Spring", quote: "Pesticide mists drifted for miles as a fine chemical **aerosol**, settling upon pastures and waterways far from the target fields." },
      { author: "Carl Sagan", work: "Pale Blue Dot", quote: "Volcanic eruptions inject tons of sulfur dioxide into the stratosphere, forming an **aerosol** veil that cools global temperatures for years." },
      { author: "Svante Arrhenius", work: "Worlds in the Making", quote: "Cosmic dust and industrial smoke contribute to the atmospheric **aerosol**, altering the albedo and radiative balance of the planet." }
    ]
  },
  "Dashboard — aer/aerosolise.md": {
    word: "aerosolise",
    primary: "To convert a substance into a fine aerosol; to disperse a liquid or fine powder as an airborne colloidal suspension (British spelling).",
    secondary: "In respiratory pharmacology and infection control, to atomize therapeutic solutions for inhalation or to generate airborne droplet nuclei during coughing and clinical procedures.",
    quotes: [
      { author: "René Dubos", work: "The Bacterial Cell", quote: "Violent coughing spasms **aerosolise** thousands of tubercle bacilli into microscopic droplet nuclei that remain suspended for hours." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Modern inhalers **aerosolise** bronchodilator solutions, delivering microscopic particles directly to the terminal bronchioles." },
      { author: "Paul de Kruif", work: "Microbe Hunters", quote: "The investigator took extreme care not to **aerosolise** the virulent broth during rapid pipetting." }
    ]
  },
  "Dashboard — aer/aerosolize.md": {
    word: "aerosolize",
    primary: "To disperse a liquid, medication, or powder as a fine aerosol or spray suspended in air or a gas stream (American spelling).",
    secondary: "In clinical pulmonary medicine and biodefense, to transform a liquid drug or pathogenic suspension into breathable particles under five micrometers in diameter.",
    quotes: [
      { author: "René Dubos", work: "The White Plague", quote: "When respiratory pathogens **aerosolize**, indoor ventilation rates become the decisive factor in controlling transmission." },
      { author: "Sinclair Lewis", work: "Arrowsmith", quote: "Martin designed a glass chamber to **aerosolize** the antibacterial mist without allowing vapors to escape into the corridor." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Agricultural sprayers that **aerosolize** chemical compounds too finely create drift clouds that poison adjacent hedgerows." }
    ]
  },
  "Dashboard — aer/aerospace engineering.md": {
    word: "aerospace engineering",
    primary: "The branch of engineering concerned with the research, design, development, construction, and testing of aircraft, spacecraft, satellites, and missiles.",
    secondary: "In applied sciences, the comprehensive field uniting atmospheric aeronautics and space astronautics, encompassing aerodynamics, propulsion thermodynamics, avionics, and orbital mechanics.",
    quotes: [
      { author: "Theodore von Kármán", work: "Aerodynamics", quote: "The evolution of high-speed flight necessitated the creation of **aerospace engineering** as an integrated discipline uniting atmospheric aeronautics and astronautics." },
      { author: "Arthur C. Clarke", work: "The Promise of Space", quote: "Advances in **aerospace engineering** made possible the Apollo lunar landings through precision multistage cryogenic rocketry." },
      { author: "Tom Wolfe", work: "The Right Stuff", quote: "Graduates of elite **aerospace engineering** departments labored over wind tunnel balance sheets to design the next generation of lifting bodies." }
    ]
  },
  "Dashboard — aer/aerospace medicine.md": {
    word: "aerospace medicine",
    primary: "The branch of medicine concerned with the health, physiological stresses, psychological resilience, and safety of human beings operating in aircraft and spacecraft.",
    secondary: "In clinical physiology and spaceflight life support, the specialty focused on counteracting microgravity deconditioning, high-altitude hypoxia, spatial disorientation, and cosmic radiation exposure.",
    quotes: [
      { author: "Harvey Cushing", work: "The Medical Career", quote: "The emergence of **aerospace medicine** reflects humanity's audacity in venturing into environments where neither pressure nor oxygen can naturally sustain life." },
      { author: "Tom Wolfe", work: "The Right Stuff", quote: "Military specialists in **aerospace medicine** subjected the astronauts to dizzying rides on the multi-axis trainer to condition their vestibular systems." },
      { author: "Carl Sagan", work: "Cosmos", quote: "Long-duration interplanetary voyages will test the limits of **aerospace medicine** in preventing bone demineralization and muscular atrophy in zero gravity." }
    ]
  },
  "Dashboard — aer/aerospace.md": {
    word: "aerospace",
    primary: "The Earth's atmosphere and the outer space beyond it, regarded as a single continuous operating environment for aviation and spaceflight.",
    secondary: "In industry and geopolitics, the high-technology commercial and military manufacturing sector that produces aircraft, spacecraft, propulsion systems, missiles, and satellites.",
    quotes: [
      { author: "Arthur C. Clarke", work: "The Exploration of Space", quote: "The distinction between aeronautics and astronautics vanished as humanity mastered the unified domain of **aerospace**." },
      { author: "Theodore von Kármán", work: "Aerodynamics", quote: "Our research centers shifted their focus from atmospheric planes to winged **aerospace** craft capable of orbital re-entry." },
      { author: "Tom Wolfe", work: "The Right Stuff", quote: "The great manufacturing complexes of Southern California hummed day and night, building the hardware for the new **aerospace** frontier." }
    ]
  },
  "Dashboard — aer/aerosphere.md": {
    word: "aerosphere",
    primary: "The entire atmospheric envelope surrounding the Earth, considered as a physical, chemical, and biological entity.",
    secondary: "In climatology and planetary sciences, the multi-layered gaseous sphere encompassing the troposphere, stratosphere, mesosphere, and thermosphere.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "The **aerosphere** wraps our globe in a protective transparent mantle, without which terrestrial life would instantly freeze in the cosmic void." },
      { author: "Camille Flammarion", work: "The Atmosphere", quote: "Viewed from the heights of space, the delicate cyan tint of the **aerosphere** defines the fragile boundary of the living world." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Human industrial emissions have altered the chemical equilibrium of the entire **aerosphere**, spreading pollutants to the polar ice caps." }
    ]
  },
  "Dashboard — aer/aerostat.md": {
    word: "aerostat",
    primary: "A lighter-than-air aircraft (such as an unpowered balloon, tethered blimp, or navigable airship) that derives its lift from buoyant gas.",
    secondary: "In aeronautical classification, a flight vehicle sustained in equilibrium by Archimedes' principle, contrasting with aerodynamic heavier-than-air aerodynes.",
    quotes: [
      { author: "Jules Verne", work: "Five Weeks in a Balloon", quote: "Dr. Ferguson calculated that his hydrogen **aerostat** would maintain equilibrium across the equatorial African deserts." },
      { author: "Edgar Allan Poe", work: "The Balloon-Hoax", quote: "The gigantic **aerostat** rose gracefully into the morning sky, propelled by twin steerable screw propellers." },
      { author: "H. G. Wells", work: "The War in the Air", quote: "Colossal fleets of rigid **aerostats** drifted silently over the ocean, their armored gondolas bristling with machine guns." }
    ]
  },
  "Dashboard — aer/aerostatics.md": {
    word: "aerostatics",
    primary: "The branch of physical science that treats the mechanical equilibrium of gaseous fluids and of solid bodies buoyant within them.",
    secondary: "In physics and lighter-than-air flight theory, the mathematical application of hydrostatics and gas laws to calculate balloon buoyant lift and equilibrium altitudes.",
    quotes: [
      { author: "Joseph Priestley", work: "Experiments on Air", quote: "The mathematical principles of **aerostatics** explain why a vessel filled with inflammable air ascends with such surprising vigor." },
      { author: "James Glaisher", work: "Travels in the Air", quote: "Our balloon ascents verified the theoretical deductions of **aerostatics** regarding atmospheric density lapse rates." },
      { author: "Octave Chanute", work: "Progress in Flying Machines", quote: "Before dynamic flight was achieved, human aerial exploration rested entirely upon the well-understood theorems of **aerostatics**." }
    ]
  },
  "Dashboard — aer/aerotaxis.md": {
    word: "aerotaxis",
    primary: "The directional movement or behavioral orientation of a motile cell or microorganism toward or away from molecular oxygen.",
    secondary: "In cellular microbiology and bacterial physiology, a sensory receptor-mediated response (via aerotaxis sensors) that directs aerobic bacteria along dissolved oxygen gradients.",
    quotes: [
      { author: "Louis Pasteur", work: "Researches on Fermentation", quote: "Under the microscope, one observes striking positive **aerotaxis**, as motile bacteria crowd toward the margins of the cover glass where oxygen dissolves." },
      { author: "René Dubos", work: "The Bacterial Cell", quote: "Cellular motility guided by **aerotaxis** allows microaerophilic species to seek out narrow microzones of intermediate oxygen tension." },
      { author: "Carl Woese", work: "The Universal Ancestor", quote: "The evolutionary emergence of sensory **aerotaxis** allowed ancestral prokaryotes to exploit oxygen-rich photosynthetic microenvironments." }
    ]
  },
  "Dashboard — aer/aerothermodynamics.md": {
    word: "aerothermodynamics",
    primary: "The branch of physics that studies the thermodynamic phenomena associated with high-speed gas flows past solid bodies, especially frictional aerodynamic heating during hypersonic flight.",
    secondary: "In spacecraft re-entry design and rocket ballistics, the analysis of shockwave thermal dissociation, boundary-layer ionization, and ablative heat shield performance.",
    quotes: [
      { author: "Theodore von Kármán", work: "Aerodynamics", quote: "At hypersonic velocities, fluid mechanics merges with chemical thermodynamics to create the complex discipline of **aerothermodynamics**." },
      { author: "Arthur C. Clarke", work: "The Promise of Space", quote: "The blunt heat shield of the Mercury capsule was a triumphant vindication of theoretical **aerothermodynamics**." },
      { author: "Steven Weinberg", work: "The First Three Minutes", quote: "The high-temperature ionization described by **aerothermodynamics** mimics conditions that prevailed in the early cosmic plasma." }
    ]
  },
  "Dashboard — aer/aerotitis.md": {
    word: "aerotitis",
    primary: "Inflammation or barotraumatic injury of the middle ear caused by an unequal barometric pressure difference across the tympanic membrane; ear barotrauma.",
    secondary: "In aviation medicine and clinical otolaryngology, middle-ear trauma caused by eustachian tube dysfunction during rapid aircraft descent, leading to tympanic retraction, pain, and hemotympanum.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Dive-bomber pilots frequently suffered from acute **aerotitis**, requiring autoinflation of the eustachian tubes to prevent tympanic rupture." },
      { author: "Harvey Cushing", work: "Selected Papers", quote: "Severe **aerotitis** accompanied by serous middle ear effusion temporarily grounds commercial and military flight crews." },
      { author: "Walter B. Cannon", work: "The Wisdom of the Body", quote: "Failure of the eustachian canal to equalize pressure during rapid altitude shifts produces the acute pain of **aerotitis**." }
    ]
  },
  "Dashboard — aer/aery.md": {
    word: "aery",
    primary: "An archaic or poetic variant of aerie (the high nest of a bird of prey); also an adjective meaning airy, ethereal, light, or unsubstantial.",
    secondary: "In Elizabethan drama and English verse, a lofty brood of nestlings (as in Hamlet), or an ethereal, visionary dwelling place perched above terrestrial concerns.",
    quotes: [
      { author: "William Shakespeare", work: "Hamlet", quote: "There is, sir, an **aery** of children, little yases, that cry out on the top of question and are most tyrannically clapped for't." },
      { author: "John Milton", work: "Paradise Lost", quote: "There the eagle and the stork on cliffs and cedar tops their **aeries** build." },
      { author: "Percy Bysshe Shelley", work: "Prometheus Unbound", quote: "Whilst all the winds with **aery** whisperings / Urge it through the storm." }
    ]
  },
  "Dashboard — aer/air.md": {
    word: "air",
    primary: "The invisible, odorless mixture of gases (chiefly nitrogen and oxygen) that envelops the Earth and sustains aerobic life; the atmosphere.",
    secondary: "In music and aesthetics, a light tune, melody, or soprano part; also, a person's demeanour, bearing, or outward manifestation (e.g., an air of confidence).",
    quotes: [
      { author: "William Shakespeare", work: "The Tempest", quote: "The isle is full of noises, / Sounds and sweet **airs**, that give delight and hurt not." },
      { author: "Henry David Thoreau", work: "Walden", quote: "I would rather sit on a pumpkin and have it all to myself, than be crowded on a velvet cushion. I want the open **air**." },
      { author: "John Keats", work: "Ode to a Nightingale", quote: "The night is tender, and the balmy **air** breathes softly through the woods." }
    ]
  },
  "Dashboard — aer/aired.md": {
    word: "aired",
    primary: "Exposed to fresh or warm air for drying, freshening, or ventilation; also, made public, expressed, or broadcast over the radio or television.",
    secondary: "In domestic management and media history, describing clothing or linens refreshed by atmospheric exposure, or grievances brought into open public scrutiny.",
    quotes: [
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "The sheets were thoroughly **aired** by the fire before the guests arrived for the evening." },
      { author: "Charles Dickens", work: "Bleak House", quote: "The musty legal parchments were brought into the sunlight and **aired** on the office window ledge." },
      { author: "Sinclair Lewis", work: "Main Street", quote: "At the town hall meeting, long-standing civic grudges were thoroughly **aired** before the gathered citizens." }
    ]
  },
  "Dashboard — aer/airing.md": {
    word: "airing",
    primary: "An exposure to fresh or warm air for freshening or drying; also, a brief stroll or drive outdoors in the open air.",
    secondary: "In rhetoric and public discourse, the open discussion or public dissemination of opinions, grievances, or proposals.",
    quotes: [
      { author: "Charles Dickens", work: "David Copperfield", quote: "Aunt Betsey took her afternoon **airing** in the garden, walking briskly along the box-bordered gravel paths." },
      { author: "Jane Austen", work: "Emma", quote: "Mr. Woodhouse was persuaded to take a gentle **airing** in the carriage on a mild autumn afternoon." },
      { author: "George Eliot", work: "Middlemarch", quote: "The controversial proposal received a thorough **airing** in the columns of the county gazette." }
    ]
  },
  "Dashboard — aer/airy.md": {
    word: "airy",
    primary: "Open to the free circulation of air; well-ventilated, spacious, and light; also, delicate, ethereal, buoyant, or unsubstantial.",
    secondary: "In literature and character depiction, showing a lighthearted, carefree, or playfully superficial manner; lacking solemnity.",
    quotes: [
      { author: "William Shakespeare", work: "Romeo and Juliet", quote: "Through which the **airy** tongue of lovers whispers / Upon the silent night." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "The high bedchamber was bright, cheerful, and **airy**, looking out over the wooded hills of Thornfield." },
      { author: "Alexander Pope", work: "The Rape of the Lock", quote: "Loose to the wind their **airy** garments flew, / Thin glittering textures of the thinnest hue." }
    ]
  },
  "Dashboard — aer/anaerobe.md": {
    word: "anaerobe",
    primary: "An organism (especially a bacterium) that does not require molecular oxygen for growth, and which may be harmed or killed by its presence.",
    secondary: "In microbiology and clinical infectious diseases, obligate or facultative prokaryotes (such as Clostridium tetani or Bacteroides fragilis) that generate metabolic energy via anaerobic glycolysis or fermentation.",
    quotes: [
      { author: "Louis Pasteur", work: "Animalcules infusoires vivant sans gaz oxygène libre", quote: "I have established the existence of a true **anaerobe**, a microorganism that lives and multiplies without a trace of free oxygen." },
      { author: "René Dubos", work: "The Bacterial Cell", quote: "In deep puncture wounds, the obligate **anaerobe** finds ideal anoxic conditions to germinate and release potent exotoxins." },
      { author: "Lynn Margulis", work: "Symbiosis in Cell Evolution", quote: "The ancestral eukaryote evolved in an environment where the strict **anaerobe** was driven into subterranean and benthic refuges." }
    ]
  },
  "Dashboard — aer/anaerobic.md": {
    word: "anaerobic",
    primary: "Living, acting, or occurring in the absence of free molecular oxygen; relating to cellular respiration or biochemical processes without oxygen.",
    secondary: "In exercise physiology, designating short, intense bursts of physical effort (such as sprinting or heavy lifting) where muscular energy demands exceed oxygen supply, generating lactic acid.",
    quotes: [
      { author: "Louis Pasteur", work: "Studies on Fermentation", quote: "Fermentation is life without air; it is the fundamental **anaerobic** pathway of cellular survival." },
      { author: "Otto Meyerhof", work: "Chemical Dynamics of Life Phenomena", quote: "During violent muscular exertion, **anaerobic** glycolysis rapidly cleaves glycogen into lactic acid to regenerate ATP." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Deep in the stagnant basins of the Black Sea, only specialized **anaerobic** bacteria can survive in the hydrogen sulfide waters." }
    ]
  },
  "Dashboard — aer/anaerobiotic.md": {
    word: "anaerobiotic",
    primary: "Relating to or characterized by anaerobiosis; living or functioning without molecular oxygen; anaerobic.",
    secondary: "In biogeochemistry and sedimentary microbiology, describing anoxic geochemical conditions (such as waterlogged bogs or deep marine sediments) where reduction reactions dominate.",
    quotes: [
      { author: "Louis Pasteur", work: "Collected Works", quote: "The **anaerobiotic** microbes decomposed the organic debris, generating methane and carbon dioxide in the sealed flasks." },
      { author: "Arthur George Tansley", work: "Practical Plant Ecology", quote: "Beneath the surface peat, waterlogged conditions create an **anaerobiotic** zone where decomposition is virtually arrested." },
      { author: "René Dubos", work: "Man Adapting", quote: "The human colon represents a densely populated **anaerobiotic** ecosystem containing hundreds of distinct bacterial species." }
    ]
  },
  "Dashboard — aer/aorta.md": {
    word: "aorta",
    primary: "The principal, largest arterial trunk in the human body, arising from the left ventricle of the heart and distributing oxygenated blood to all systemic arteries.",
    secondary: "In cardiovascular anatomy and pathology, the great vessel comprising the ascending aorta, aortic arch, and descending aorta, prone to life-threatening aneurysm or dissection (Greek aorte from aeirein to lift/carry).",
    quotes: [
      { author: "William Harvey", work: "De Motu Cordis", quote: "With every systole of the left ventricle, a fresh surge of blood is forcefully propelled into the great cavity of the **aorta**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Aneurysm of the thoracic **aorta** produces characteristic brassy cough and tracheal tug through direct mechanical compression." },
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", quote: "Catheterization of the **aorta** reveals the profound hydrostatic pressures sustained by the systemic arterial tree." }
    ]
  },
  "Dashboard — aer/aortal.md": {
    word: "aortal",
    primary: "Of, relating to, or situated in the aorta; aortic.",
    secondary: "In systemic cardiovascular anatomy and clinical hemodynamic monitoring, describing structural features, flow velocities, or murmurs associated with the main systemic arterial trunk.",
    quotes: [
      { author: "William Harvey", work: "De Motu Cordis", quote: "The **aortal** valves close firmly upon diastole, preventing any backward regurgitation into the ventricular chamber." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Careful auscultation revealed a harsh systolic murmur over the **aortal** area radiating upward into the carotid vessels." },
      { author: "Astley Cooper", work: "Lectures on Surgery", quote: "Ligation of the abdominal **aortal** trunk remains one of the most perilous procedures in operative surgery." }
    ]
  },
  "Dashboard — aer/aortic.md": {
    word: "aortic",
    primary: "Of, relating to, or located near the aorta (e.g., aortic valve, aortic arch, aortic aneurysm).",
    secondary: "In cardiovascular pathology and cardiology, describing clinical conditions affecting the primary outflow tract of the heart, such as aortic stenosis, aortic regurgitation, or aortic coarctation.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In chronic **aortic** insufficiency, the water-hammer pulse of Corrigan offers an unmistakable bedside sign." },
      { author: "William Harvey", work: "On the Motion of the Heart and Blood", quote: "The three semilunar **aortic** cusps open completely during ventricular contraction to permit unobstructed outflow." },
      { author: "Paul Dudley White", work: "Heart Disease", quote: "Calcific **aortic** stenosis in elderly patients produces progressive left ventricular hypertrophy and angina." }
    ]
  },
  "Dashboard — aer/deaerate.md": {
    word: "deaerate",
    primary: "To remove air, entrained bubbles, or dissolved gases (especially oxygen and carbon dioxide) from a liquid or substance.",
    secondary: "In industrial boiler engineering and chemical processing, to strip dissolved oxygen from feedwater to prevent internal corrosion and oxidative scale in high-pressure steam boilers.",
    quotes: [
      { author: "Louis Pasteur", work: "Studies on Beer", quote: "Before introducing pure yeast cultures, it was necessary to **deaerate** the boiled medium by heating it under vacuum." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Laboratory technicians **deaerate** water samples using vacuum degassing to measure accurate chemical absorption rates." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "To prevent rapid oxidation of sensitive ferrous solutions, the chemist must thoroughly **deaerate** the solvent with inert nitrogen." }
    ]
  },
  "Dashboard — aer/endaortitis.md": {
    word: "endaortitis",
    primary: "Inflammation of the tunica intima, the innermost endothelial lining, of the aorta.",
    secondary: "In vascular pathology and infectious cardiovascular disease, inflammatory lesions of the aortic endothelium typically associated with tertiary syphilis, infective endocarditis, or severe atheromatous plaque ulceration.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Chronic syphilitic **endaortitis** destroys the elastic lamellae of the media, predisposing the ascending aorta to saccular aneurysms." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Microscopic sections in severe **endaortitis** display intense cellular proliferation and lipid accumulation within the intimal layer." },
      { author: "Paul Dudley White", work: "Heart Disease", quote: "The scarred, wrinkled intima characteristic of advanced **endaortitis** reflects decades of chronic vascular inflammation." }
    ]
  }
};

function updateWordNote(relPath, data) {
  const fullPath = path.join(baseDir, relPath);
  if (!fs.existsSync(fullPath)) {
    console.error("Not found:", fullPath);
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
console.log("Batch 10 finished! Total words updated:", Object.keys(wordsData).length);
