import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Physics & Chemistry';

const filesData = {
  // === Dashboard — stat (4 words) ===
  "Dashboard — stat/statutorily.md": {
    primary: "In a statutory manner; in accordance with, or as required by, a formal statute or written law.",
    secondary: "By legal enactment; pursuant to statutory mandates established by a legislature.",
    quotes: [
      { author: "William Blackstone", work: "Commentaries on the Laws of England", quote: "Certain fiduciary obligations are **statutorily** imposed upon executors to safeguard estates." },
      { author: "Oliver Wendell Holmes Jr.", work: "Collected Legal Papers", quote: "The administrative commission was **statutorily** empowered to fix maximum freight rates." },
      { author: "Alexander Hamilton", work: "The Federalist Papers", quote: "Rights that are **statutorily** defined remain subject to amendment by subsequent legislative assemblies." }
    ]
  },
  "Dashboard — stat/statutory.md": {
    primary: "Enacted, created, or required by a statute or legislative body; prescribed by written law.",
    secondary: "In jurisprudence, distinguishing positive written law (statutory law) from judicial precedent (common law).",
    quotes: [
      { author: "William Blackstone", work: "Commentaries on the Laws of England", quote: "We must distinguish between the common law of time immemorial and modern **statutory** enactments." },
      { author: "Alexander Hamilton", work: "The Federalist Papers", quote: "The courts must adhere to the Constitution whenever a **statutory** decree conflicts with the fundamental charter." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "No abstract theory can supersede the explicit provisions of a solemn **statutory** covenant." }
    ]
  },
  "Dashboard — stat/unstated.md": {
    primary: "Not declared, expressed, or specified explicitly in words; implied or tacit.",
    secondary: "Understood without direct verbal declaration; taking for granted an unmentioned premise.",
    quotes: [
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "There remained between them an **unstated** understanding that needed no spoken reassurance." },
      { author: "George Eliot", work: "Middlemarch", quote: "An **unstated** assumption governed their household that Dorothea's intellectual pursuits should yield to her husband's." },
      { author: "Bertrand Russell", work: "The Analysis of Mind", quote: "In deductive arguments, the most dangerous fallacy often lurks within an **unstated** major premise." }
    ]
  },
  "Dashboard — stat/unstatesmanlike.md": {
    primary: "Not characteristic of or suitable for a statesman; exhibiting narrow, petty, or short-sighted political judgment.",
    secondary: "Marked by factional partisanship, demagoguery, or disregard for the long-term public welfare.",
    quotes: [
      { author: "Edmund Burke", work: "Speech on Conciliation with America", quote: "To penalize an entire continent for the indiscretions of a few was deemed thoroughly **unstatesmanlike**." },
      { author: "Winston Churchill", work: "The Gathering Storm", quote: "It would have been cowardly and **unstatesmanlike** to conceal the mortal peril confronting our defenses." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "Appealing to temporary popular passions for electoral victory is an **unstatesmanlike** abdication of duty." }
    ]
  },

  // === Dashboard — stomat (12 words) ===
  "Dashboard — stomat/astomatal.md": {
    primary: "Devoid of stomata (microscopic breathing pores); astomatous.",
    secondary: "In plant anatomy, describing submersed aquatic leaves or specialized plant surfaces that lack epidermal stomatal openings.",
    quotes: [
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "Completely submerged aquatic plants exhibit **astomatal** foliage, absorbing gases directly across thin cuticles." },
      { author: "Julius von Sachs", work: "Text-book of Botany", quote: "The upper epidermis of many shade-loving leaves is entirely **astomatal**, confining gas exchange to the lower surface." },
      { author: "Daniel Trembly MacDougal", work: "Practical Text-book of Plant Physiology", quote: "An **astomatal** leaf surface prevents water loss, but severely restricts transpiration and photosynthetic influx." }
    ]
  },
  "Dashboard — stomat/astomatous.md": {
    primary: "Having no mouth, oral opening, or stomata.",
    secondary: "In invertebrate zoology and botany, designating mouthless parasites (such as adult tapeworms) or plants devoid of epidermal breathing pores.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", quote: "The adult cestode is an **astomatous** endoparasite, absorbing dissolved chyme through its microvillar tegument." },
      { author: "Richard Owen", work: "Lectures on the Comparative Anatomy and Physiology of Invertebrates", quote: "Certain parasitic protozoa remain **astomatous**, having lost all vestige of a cytostome." },
      { author: "Asa Gray", work: "Structural Botany", quote: "Submerged bryophyte phylloids are typically **astomatous**, lacking the complex guard cells of vascular foliage." }
    ]
  },
  "Dashboard — stomat/colostomy.md": {
    primary: "A surgical operation in which a piece of the colon is diverted to an artificial opening in the abdominal wall so as to bypass a damaged part of the colon.",
    secondary: "The stoma or artificial opening created in the abdominal wall by such a surgical procedure.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In obstructing neoplasms of the sigmoid colon, a palliative **colostomy** relieves acute mechanical ileus." },
      { author: "Atul Gawande", work: "Complications: A Surgeon's Notes on an Imperfect Science", quote: "The patient adapted with admirable resilience to managing his permanent sigmoid **colostomy**." },
      { author: "Sherwin B. Nuland", work: "How We Die", quote: "A temporary diverting **colostomy** was fashioned to allow the distal rectal anastomosis to heal without contamination." }
    ]
  },
  "Dashboard — stomat/gastrostomy.md": {
    primary: "The surgical creation of an opening into the stomach through the abdominal wall, typically for the insertion of a feeding tube (PEG tube).",
    secondary: "In clinical nutrition and surgery, a permanent or temporary enteral access technique utilized when swallowing is impaired by esophageal disease or stroke.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In impermeable malignant strictures of the esophagus, a feeding **gastrostomy** maintains life and nutrition." },
      { author: "Atul Gawande", work: "Being Mortal", quote: "The family debated whether to proceed with a percutaneous endoscopic **gastrostomy** for the failing elder." },
      { author: "Sherwin B. Nuland", work: "Doctors: The Biography of Medicine", quote: "Pioneering nineteenth-century surgeons perfected the technique of **gastrostomy** to bypass corrosive esophageal burns." }
    ]
  },
  "Dashboard — stomat/ileostomy.md": {
    primary: "A surgical procedure in which the ileum (the lowest part of the small intestine) is brought out through an opening in the abdominal wall to form a stoma.",
    secondary: "In colorectal surgery, an artificial opening used to divert digestive contents following total proctocolectomy for ulcerative colitis or polyposis.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In fulminant ulcerative colitis refractory to medical management, an urgent **ileostomy** may prove life-saving." },
      { author: "Atul Gawande", work: "Better: A Surgeon's Notes on Performance", quote: "Modern ostomy appliances have made living with a temporary loop **ileostomy** far more manageable for patients." },
      { author: "Sherwin B. Nuland", work: "The Mysteries Within", quote: "The stoma of a well-matured **ileostomy** delivers liquid effluent that requires meticulous peristomal skin protection." }
    ]
  },
  "Dashboard — stomat/stomatal.md": {
    primary: "Of, relating to, or involving stomata (microscopic pores in plant epidermis).",
    secondary: "In plant physiology, pertaining to stomatal conductance, guard cell turgor mechanics, and transpirational gas exchange regulation.",
    quotes: [
      { author: "Francis Darwin", work: "Observations on Stomata", quote: "Changes in light intensity produce immediate **stomatal** responses through osmotic swelling of the guard cells." },
      { author: "Julius von Sachs", work: "Text-book of Botany", quote: "The **stomatal** aperture widens when potassium ions accumulate inside the crescent-shaped guard cells." },
      { author: "Daniel Trembly MacDougal", work: "Practical Text-book of Plant Physiology", quote: "Water stress induces synthesis of abscisic acid, triggering rapid **stomatal** closure to prevent wilting." }
    ]
  },
  "Dashboard — stomat/stomate.md": {
    primary: "A single stoma; a microscopic pore found in the epidermis of leaves and stems used for gas exchange.",
    secondary: "In botany, the functional unit consisting of the pore aperture flanked by two specialized photosynthetic guard cells.",
    quotes: [
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "Each **stomate** acts as a self-adjusting hydraulic valve governing the entry of carbon dioxide into the spongy mesophyll." },
      { author: "Francis Darwin", work: "The Physiology of Plants", quote: "Under the microscope, the slit of the **stomate** opened visibly as the illuminating mirror concentrated morning light." },
      { author: "Julius von Sachs", work: "Text-book of Botany", quote: "Turgor changes within the twin cells bordering the **stomate** regulate the transpirational stream." }
    ]
  },
  "Dashboard — stomat/stomatitis.md": {
    primary: "Inflammation of the mucous membranes of the mouth (including lips, tongue, gums, and cheeks).",
    secondary: "In clinical medicine, oral ulcerations or lesions caused by viral infection (herpes simplex), candidiasis, nutritional deficiencies, or chemotherapy.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Aphthous **stomatitis** presents as painful, recurrent superficial ulcers surrounded by an inflammatory red halo." },
      { author: "Atul Gawande", work: "Being Mortal", quote: "Chemotherapeutic regimens often induce distressing **stomatitis**, impairing the patient's ability to swallow solid food." },
      { author: "Jerome Groopman", work: "The Anatomy of Hope", quote: "Gentle anesthetic rinses were prescribed to ease the mucosal pain of radiation-induced **stomatitis**." }
    ]
  },
  "Dashboard — stomat/stomatology.md": {
    primary: "The branch of medicine and dentistry that deals with the mouth and its diseases.",
    secondary: "In European and international medical systems, a medical specialty integrating dental surgery, oral medicine, and maxillofacial pathology.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The expanding field of **stomatology** bridges the traditional divide between systemic medicine and dentistry." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "Clinical **stomatology** provides early warning signs of systemic diseases like syphilis and leukemia upon the oral mucosa." },
      { author: "Sherwin B. Nuland", work: "The Mysteries Within", quote: "Advances in **stomatology** have demonstrated the direct link between chronic periodontal sepsis and cardiovascular disease." }
    ]
  },
  "Dashboard — stomat/stomatopod.md": {
    primary: "Any marine crustacean of the order Stomatopoda, commonly known as a mantis shrimp.",
    secondary: "In marine zoology, predatory crustaceans possessing raptorial appendages capable of striking prey with bullet-like velocity and cavitation bubbles.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", quote: "The formidable raptorial claw of the **stomatopod** strikes with astonishing velocity, shattering snail shells with ease." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "The complex compound eyes of the **stomatopod** possess up to sixteen distinct photoreceptor types, analyzing polarized light." },
      { author: "Ernst Haeckel", work: "Art Forms in Nature", quote: "The segmented carapace and kaleidoscopic hues of the **stomatopod** exhibit remarkable marine morphological elegance." }
    ]
  },
  "Dashboard — stomat/stomatopoda.md": {
    primary: "An order of predatory marine crustaceans in the subclass Hoplocarida, containing the mantis shrimps.",
    secondary: "In arthropod paleontology and marine ecology, an ancient lineage dating to the Carboniferous, possessing raptorial thoracic limbs modified for spearing or smashing.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Anatomy of Invertebrated Animals", quote: "Crustaceans of the order **Stomatopoda** depart markedly from decapods in having five pairs of subchelate limbs." },
      { author: "Richard Owen", work: "Lectures on the Comparative Anatomy of Invertebrates", quote: "Fossil specimens belonging to **Stomatopoda** preserved in Jurassic lithographic limestone show virtually modern claw architecture." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "The explosive biomechanics of prey capture in **Stomatopoda** represent nature's fastest predatory strike." }
    ]
  },
  "Dashboard — stomat/stomatous.md": {
    primary: "Having a mouth, oral aperture, or stomata; furnished with stomata.",
    secondary: "In botany, describing plant surfaces (such as lower leaf surfaces) that bear abundant functional stomata for gas exchange.",
    quotes: [
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "The lower epidermis of the maple leaf is densely **stomatous**, accommodating thousands of pores per square millimeter." },
      { author: "Julius von Sachs", work: "Text-book of Botany", quote: "Gas diffusion into the mesophyll is strictly confined to the **stomatous** areas of the leaf surface." },
      { author: "Daniel Trembly MacDougal", work: "Practical Text-book of Plant Physiology", quote: "Epidermal peels from the **stomatous** surface were floated on saline solutions to observe plasmolysis in guard cells." }
    ]
  },

  // === Dashboard — therm (48 words) ===
  "Dashboard — therm/athermancy.md": {
    primary: "The property of being athermanous; impermeability or resistance to radiant heat.",
    secondary: "In thermodynamics and physical optics, the capacity of a medium (such as alum solution or thick glass) to absorb infrared radiation while transmitting visible light.",
    quotes: [
      { author: "John Tyndall", work: "Heat Considered as a Mode of Motion", quote: "Water displays remarkable **athermancy**, absorbing radiant heat rays with extraordinary completeness." },
      { author: "James Clerk Maxwell", work: "Theory of Heat", quote: "The relative **athermancy** of different gases was demonstrated by measuring thermal transmission through absorption tubes." },
      { author: "Lord Kelvin (William Thomson)", work: "Mathematical and Physical Papers", quote: "The thermal shield utilized an alum cell whose **athermancy** blocked intense radiant heat from reaching delicate instruments." }
    ]
  },
  "Dashboard — therm/diathermancy.md": {
    primary: "The property of transmitting radiant heat; transparency to infrared radiation.",
    secondary: "In physical optics, the capacity of substances like rock salt (halite) or dry air to allow thermal radiation to pass through without substantial absorption.",
    quotes: [
      { author: "Macedonio Melloni", work: "La Thermochrôse ou la Coloration Calorifique", quote: "Rock salt exhibits near-perfect **diathermancy**, allowing heat rays of all wavelengths to traverse it unimpeded." },
      { author: "John Tyndall", work: "Contributions to Molecular Physics in the Domain of Radiant Heat", quote: "While pure dry air possesses high **diathermancy**, the addition of water vapor dramatically impedes radiant heat." },
      { author: "James Clerk Maxwell", work: "Theory of Heat", quote: "The **diathermancy** of a medium varies according to the quality and wavelength of the incident radiant heat." }
    ]
  },
  "Dashboard — therm/diathermy.md": {
    primary: "A medical and surgical technique involving the production of heat in body tissues by high-frequency electric currents.",
    secondary: "In physical therapy, shortwave or microwave diathermy used for deep tissue heating; in surgery, electrodiathermy used for tissue coagulation and cutting.",
    quotes: [
      { author: "Harvey Cushing", work: "Electrosurgery in Brain Surgery", quote: "Surgical **diathermy** sealed capillary oozing across the resected tumor bed without mechanical pressure." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Shortwave **diathermy** was applied to the arthritic joint to relieve chronic stiffness and promote deep circulation." },
      { author: "Atul Gawande", work: "Complications", quote: "The surgeon tapped the pedal, activating the **diathermy** pen to coagulate a bleeding subcutaneous vessel." }
    ]
  },
  "Dashboard — therm/ectotherm.md": {
    primary: "An organism that relies on external sources of heat to regulate its body temperature; a cold-blooded animal.",
    secondary: "In comparative physiology and ecology, an animal (such as a reptile, amphibian, or fish) whose metabolic rate is predominantly determined by ambient temperature.",
    quotes: [
      { author: "Bernd Heinrich", work: "The Hot-Blooded Insects", quote: "The basking lizard is an archetypal **ectotherm**, utilizing solar radiation to raise its body temperature before foraging." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "Being an **ectotherm** requires far less caloric energy per day than that demanded by an endothermic mammal." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "The debate over dinosaur physiology asks whether they were sluggish **ectotherm** reptiles or active endotherms." }
    ]
  },
  "Dashboard — therm/ectothermic.md": {
    primary: "Relating to or being an ectotherm; dependent on external sources of body heat.",
    secondary: "In physiological ecology, exhibiting body temperature fluctuations driven by environmental thermal gradients.",
    quotes: [
      { author: "Bernd Heinrich", work: "Bumblebee Economics", quote: "While most insects are strictly **ectothermic**, large fliers can generate internal heat by shivering their flight muscles." },
      { author: "Charles Darwin", work: "The Expression of the Emotions in Man and Animals", quote: "The physiological sluggishness of **ectothermic** animals in winter is directly dictated by ambient temperature." },
      { author: "Stephen Jay Gould", work: "Dinosaur in a Haystack", quote: "Bone histology was scrutinized to determine whether theropod dinosaurs possessed an **ectothermic** or endothermic metabolism." }
    ]
  },
  "Dashboard — therm/endotherm.md": {
    primary: "An organism that generates heat internally through metabolic activity to maintain a constant, elevated body temperature; a warm-blooded animal.",
    secondary: "In vertebrate zoology, birds and mammals whose high metabolic rates sustain homeothermy regardless of environmental temperatures.",
    quotes: [
      { author: "Bernd Heinrich", work: "The Hot-Blooded Insects", quote: "As an active **endotherm**, the arctic fox can withstand fifty degrees below zero without lowering its internal temperature." },
      { author: "Stephen Jay Gould", work: "Bully for Brontosaurus", quote: "The discovery of polar dinosaurs challenged the old assumption that no Mesozoic reptile could live as an **endotherm**." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "The immense food intake required by a mammalian **endotherm** shapes the carrying capacity of terrestrial food webs." }
    ]
  },
  "Dashboard — therm/endothermal.md": {
    primary: "Pertaining to internal heat production; or accompanied by the absorption of heat; endothermic.",
    secondary: "In physical chemistry and thermodynamics, describing chemical reactions that absorb thermal energy from their surroundings.",
    quotes: [
      { author: "Julius Thomsen", work: "Thermochemical Investigations", quote: "Dissolution of ammonium nitrate in water is a strongly **endothermal** process that produces sharp cooling." },
      { author: "Marcellin Berthelot", work: "Essai de Mécanique Chimique", quote: "Reactions that proceed with absorption of heat were classified under the term **endothermal** transformations." },
      { author: "Svante Arrhenius", work: "Textbook of Electrochemistry", quote: "The electrolytic dissociation constant increases with temperature for an **endothermal** ionization." }
    ]
  },
  "Dashboard — therm/endothermic.md": {
    primary: "Accompanied by or requiring the absorption of heat (of a chemical reaction or physical process).",
    secondary: "In biology, warm-blooded; generating internal heat to maintain a stable body temperature.",
    quotes: [
      { author: "Linus Pauling", work: "General Chemistry", quote: "In an **endothermic** reaction, the enthalpy of the products exceeds that of the reactants, resulting in a positive delta-H." },
      { author: "Bernd Heinrich", work: "Thermal Warriors: Strategies of Insect Survival", quote: "The evolution of **endothermic** regulation allowed early mammals to forage during the cold nocturnal hours." },
      { author: "J. Willard Gibbs", work: "On the Equilibrium of Heterogeneous Substances", quote: "An **endothermic** phase transition requires continuous influx of latent heat to sustain equilibrium." }
    ]
  },
  "Dashboard — therm/exotherm.md": {
    primary: "A process, reaction, or stage characterized by the release or evolution of heat; an exothermic transformation.",
    secondary: "In polymer and materials engineering, the peak heat release curve observed during resin curing or polymer crosslinking.",
    quotes: [
      { author: "Marcellin Berthelot", work: "Thermochimie", quote: "The sudden **exotherm** observed upon spontaneous polymerization indicates rapid release of chemical energy." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "Covalent bond formation between free radicals produces a sharp **exotherm** equal to the dissociation energy." },
      { author: "Justus von Liebig", work: "Familiar Letters on Chemistry", quote: "Slaking quicklime with water generates a dangerous **exotherm** capable of boiling the liquid." }
    ]
  },
  "Dashboard — therm/exothermal.md": {
    primary: "Accompanied by the liberation or release of heat; exothermic.",
    secondary: "In chemical thermodynamics, describing reactions where the enthalpy of products is lower than that of reactants.",
    quotes: [
      { author: "Marcellin Berthelot", work: "Essai de Mécanique Chimique", quote: "The principle of maximum work states that purely spontaneous reactions tend to be **exothermal**." },
      { author: "Julius Thomsen", work: "Thermochemische Untersuchungen", quote: "Precise calorimetric measurement revealed that the neutralization of strong acids by alkalis is uniformly **exothermal**." },
      { author: "Ira Remsen", work: "Principles of Theoretical Chemistry", quote: "Combustion of hydrocarbons constitutes the most familiar class of **exothermal** chemical transformations." }
    ]
  },
  "Dashboard — therm/exothermic.md": {
    primary: "Releasing heat into the surroundings; characterized by a negative change in enthalpy (delta-H < 0).",
    secondary: "In thermodynamics and explosives chemistry, reactions that release energy as heat, light, or sound (such as combustion or thermite reactions).",
    quotes: [
      { author: "Linus Pauling", work: "General Chemistry", quote: "The synthesis of water from hydrogen and oxygen is violently **exothermic**, releasing fifty-seven kilocalories per mole." },
      { author: "Svante Arrhenius", work: "Studies on Chemical Dynamics", quote: "According to Le Chatelier's principle, elevating the temperature shifts an **exothermic** equilibrium toward the reactants." },
      { author: "Primo Levi", work: "The Periodic Table", quote: "The ignition of magnesium powder and barium peroxide produces a fiercely **exothermic** thermite flash." }
    ]
  },
  "Dashboard — therm/geothermal.md": {
    primary: "Of, relating to, or produced by the internal heat of the Earth.",
    secondary: "In renewable energy engineering, energy harnessed from subterranean steam, hot dry rock, or volcanic aquifers to generate electricity or heating.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The presence of boiling geysers in Iceland demonstrates the intense **geothermal** energy underlying volcanic terrains." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Deep boreholes reveal a steady **geothermal** gradient of approximately thirty degrees Celsius per kilometer of depth." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Deep-sea hydrothermal vents powered by **geothermal** volcanism support vibrant communities of chemosynthetic organisms." }
    ]
  },
  "Dashboard — therm/geothermally.md": {
    primary: "By means of geothermal energy or internal terrestrial heat.",
    secondary: "With respect to geothermal processes, heating, or volcanic groundwater circulation.",
    quotes: [
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "The groundwater in the volcanic caldera was **geothermally** superheated far above its surface boiling point." },
      { author: "John Muir", work: "Our National Parks", quote: "Yellowstone's geyser basins are **geothermally** nurtured, smoking amid the subalpine snows throughout the winter." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Mineral ores precipitated from **geothermally** circulated brines fill fractures in the granite country rock." }
    ]
  },
  "Dashboard — therm/geothermic.md": {
    primary: "Of or relating to the heat of the Earth's interior; geothermal.",
    secondary: "Pertaining to the geothermic degree or subterranean temperature gradient measured in mines and drill holes.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "Mine shafts sunk deep into the Bohemian plateau confirmed the universal increase of the **geothermic** gradient." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The **geothermic** degree varies considerably between ancient continental shields and young volcanic provinces." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Decay of radioactive isotopes in the crust constitutes the primary engine powering terrestrial **geothermic** activity." }
    ]
  },
  "Dashboard — therm/heterothermic.md": {
    primary: "Exhibiting physiological variation in body temperature; capable of switching between poikilothermy and homeothermy.",
    secondary: "In mammalian and avian physiology, describing animals (such as bats, hummingbirds, and bears) that utilize torpor or hibernation to conserve metabolic energy.",
    quotes: [
      { author: "Bernd Heinrich", work: "Winter World: The Ingenuity of Animal Survival", quote: "The chickadee is a facultatively **heterothermic** bird, dropping its core temperature at night by ten degrees to survive arctic freezes." },
      { author: "E. O. Wilson", work: "Sociobiology: The New Synthesis", quote: "Daily torpor in **heterothermic** mammals represents an exquisite metabolic strategy for coping with unpredictable nectar supplies." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "Hibernating mammals reveal that homeothermy is not an inflexible rule, but can be relaxed through regulated **heterothermic** cycles." }
    ]
  },
  "Dashboard — therm/homeothermy.md": {
    primary: "The physiological capability of maintaining a stable internal body temperature regardless of ambient environmental temperatures.",
    secondary: "In vertebrate physiology, the hallmark thermoregulatory characteristic of mammals and birds, governed by hypothalamic feedback.",
    quotes: [
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", quote: "The constancy of the internal environment (milieu intérieur) reaches its perfection in mammalian **homeothermy**." },
      { author: "Walter B. Cannon", work: "The Wisdom of the Body", quote: "Shivering, sweating, and peripheral vasoconstriction coordinate to defend the constancy of **homeothermy**." },
      { author: "Stephen Jay Gould", work: "Ever Since Darwin", quote: "The evolution of **homeothermy** unlocked nocturnal niches and allowed vertebrates to colonize high-latitude habitats." }
    ]
  },
  "Dashboard — therm/homotherm.md": {
    primary: "An organism that maintains a constant internal body temperature; a homeotherm.",
    secondary: "In animal biology, a bird or mammal that regulates its core temperature through physiological metabolic feedback.",
    quotes: [
      { author: "Claude Bernard", work: "Lectures on the Phenomena of Life Common to Animals and Plants", quote: "The **homotherm** carries its own tropical climate within itself, independent of external seasons." },
      { author: "Bernd Heinrich", work: "The Hot-Blooded Insects", quote: "Maintaining life as a true **homotherm** demands continuous foraging to supply an enormous basal metabolic furnace." },
      { author: "Stephen Jay Gould", work: "Dinosaur in a Haystack", quote: "If dinosaurs were active predators, many argued they must have functioned as an agile **homotherm**." }
    ]
  },
  "Dashboard — therm/homothermic.md": {
    primary: "Characterized by or capable of maintaining a constant internal body temperature; homeothermic.",
    secondary: "Warm-blooded; maintaining constant body temperature via physiological thermoregulation.",
    quotes: [
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", quote: "In **homothermic** species, thermal homeostasis insulates biochemical machinery from the fluctuations of the outside world." },
      { author: "Walter B. Cannon", work: "The Wisdom of the Body", quote: "The autonomic nervous system orchestrates vascular and pilomotor reflexes that preserve the **homothermic** state." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "The feather was an evolutionary insulator long before it was co-opted for flight in **homothermic** avians." }
    ]
  },
  "Dashboard — therm/hyperthermal.md": {
    primary: "Of, relating to, or characterized by abnormally high temperatures; superheated.",
    secondary: "In paleoclimatology, designating transient geological warming events (such as the Paleocene-Eocene Thermal Maximum, a hyperthermal).",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Subterranean steam from **hyperthermal** springs deposits thick terraces of calcareous travertine." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Deep abyssal smokers erupt **hyperthermal** mineral plumes into the freezing bottom waters of the ocean." },
      { author: "Al Gore", work: "Earth in the Balance", quote: "Geological records warn that ancient **hyperthermal** spikes were accompanied by widespread oceanic acidification and extinction." }
    ]
  },
  "Dashboard — therm/hyperthermia.md": {
    primary: "An abnormally high body temperature, occurring when internal heat regulation fails to manage environmental heat or metabolic heat production.",
    secondary: "In emergency medicine, heat stroke (core temp > 40°C), distinct from fever; or malignant hyperthermia triggered by volatile anesthetics.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In classic heat stroke, profound anhydrosis and delirium signal life-threatening **hyperthermia** requiring instant iced immersion." },
      { author: "Atul Gawande", work: "The Checklist Manifesto", quote: "An unexpected spike in expired carbon dioxide alerted the anesthetist to acute malignant **hyperthermia**." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "Differentiating between hypothalamic fever and environmental **hyperthermia** is essential for selecting correct therapy." }
    ]
  },
  "Dashboard — therm/hyperthermy.md": {
    primary: "A variant or older medical term for hyperthermia; abnormally high body temperature.",
    secondary: "In historical therapeutics, the deliberate therapeutic induction of fever (pyrotherapy) to treat neurosyphilis, championed by Julius Wagner-Jauregg.",
    quotes: [
      { author: "Julius Wagner-Jauregg", work: "Nobel Lecture: The Treatment of Dementia Paralytica by Malaria Inoculation", quote: "Sustained clinical **hyperthermy** induced by benign tertian malaria eradicated the fragile spirochetes in the central nervous system." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Extreme **hyperthermy** exceeding one hundred and seven degrees Fahrenheit threatens irreversible cellular damage in cerebral neurons." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "Post-encephalitic crises were often ushered in by sudden bouts of autonomic tachycardia and central **hyperthermy**." }
    ]
  },
  "Dashboard — therm/hypothermia.md": {
    primary: "A medical emergency that occurs when your body loses heat faster than it can produce heat, causing a dangerously low body temperature (core temp < 35°C).",
    secondary: "In clinical surgery and neuroprotection, therapeutic hypothermia intentionally induced after cardiac arrest to protect ischemic brain tissue.",
    quotes: [
      { author: "Robert Falcon Scott", work: "Scott's Last Expedition", quote: "As the blizzard raged, creeping numbness and insidious **hypothermia** dulled our frozen limbs." },
      { author: "Atul Gawande", work: "Complications", quote: "Induced therapeutic **hypothermia** cooled the patient's brain during cardiopulmonary arrest, preserving intact neurological function." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe accidental **hypothermia** presents with lethargy, shivering, bradycardia, and eventual paradoxical undressing." }
    ]
  },
  "Dashboard — therm/hypothermic.md": {
    primary: "Of, relating to, or suffering from hypothermia; having an abnormally low body temperature.",
    secondary: "In cardiovascular and transplant surgery, designating cold storage solutions or protective hypothermic perfusion protocols.",
    quotes: [
      { author: "Atul Gawande", work: "Better: A Surgeon's Notes on Performance", quote: "The donor heart was flushed with ice-cold cardioplegic solution to maintain a stable **hypothermic** state during transport." },
      { author: "Jerome Groopman", work: "Second Opinions", quote: "The emergency team warmed the severely **hypothermic** skier slowly to avoid re-warming ventricular fibrillation." },
      { author: "Ernest Shackleton", work: "South: The Story of Shackleton's Last Expedition", quote: "Soaked through with icy brine, the sailors huddled in a shivering, **hypothermic** misery upon the open boat." }
    ]
  },
  "Dashboard — therm/isotherm.md": {
    primary: "A line on a weather map connecting points having the same temperature at a given time or on average over a given period.",
    secondary: "In thermodynamics and physical chemistry, a curve on a pressure-volume diagram showing the state of a system at constant temperature.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Des Lignes Isothermes et de la Distribution de la Chaleur sur le Globe", quote: "By connecting points of equal mean annual temperature with an **isotherm**, the true climatic belts of the earth were first visualized." },
      { author: "Rudolf Clausius", work: "The Mechanical Theory of Heat", quote: "Along any **isotherm** on the indicator diagram, the internal energy of an ideal gas remains strictly constant." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "The deflection of the coastal **isotherm** lines reveals the powerful thermal buffering of oceanic currents." }
    ]
  },
  "Dashboard — therm/isothermal.md": {
    primary: "Occurring at a constant temperature; having or characterized by equal or constant temperatures.",
    secondary: "In thermodynamics, denoting an isothermal process—an expansion or compression where temperature remains unchanged due to heat exchange with a reservoir.",
    quotes: [
      { author: "Sadi Carnot", work: "Reflections on the Motive Power of Fire", quote: "The ideal heat engine operates by alternating between two **isothermal** transformations and two adiabatic expansions." },
      { author: "Lord Kelvin (William Thomson)", work: "Mathematical and Physical Papers", quote: "During **isothermal** compression, the mechanical work performed upon the gas is completely conducted away as heat." },
      { author: "J. Willard Gibbs", work: "Graphical Methods in the Thermodynamics of Fluids", quote: "The work done during an **isothermal** change equals the decrease in Helmholtz free energy." }
    ]
  },
  "Dashboard — therm/isothermic.md": {
    primary: "Characterized by equal or constant temperatures; isothermal.",
    secondary: "In meteorology, exhibiting layers of the atmosphere where temperature remains constant with increasing altitude.",
    quotes: [
      { author: "Cleveland Abbe", work: "The Mechanics of the Earth's Atmosphere", quote: "Above the tropospheric convective boundary lies an **isothermic** stratospheric zone where temperature ceases to fall." },
      { author: "William Napier Shaw", work: "Manual of Meteorology", quote: "The chart revealed an extensive **isothermic** plateau over the mid-Atlantic." },
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "Zones situated along the same **isothermic** band exhibit striking correspondences in their natural flora." }
    ]
  },
  "Dashboard — therm/poikilotherm.md": {
    primary: "An organism that cannot regulate its body temperature except by behavioral means, whose body temperature varies with the environment; a cold-blooded animal.",
    secondary: "In comparative zoology, fish, amphibians, and reptiles whose internal metabolic rate is low and fluctuates with environmental heat.",
    quotes: [
      { author: "Bernd Heinrich", work: "The Hot-Blooded Insects", quote: "Unlike a bird or mammal, a **poikilotherm** can endure days of fasting because it spends no calories keeping warm." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "Tropical rainforests shelter immense diversities of **poikilotherm** vertebrates whose metabolic needs remain minimal." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "The physiological contrast between an active mammal and a sluggish **poikilotherm** reptile framed the debate on dinosaur metabolism." }
    ]
  },
  "Dashboard — therm/poikilothermic.md": {
    primary: "Having a body temperature that varies with the temperature of the surrounding environment; cold-blooded.",
    secondary: "In comparative physiology, exhibiting metabolic rates and enzyme kinetics directly dependent on ambient thermal conditions.",
    quotes: [
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", quote: "In **poikilothermic** animals like frogs, life functions slow down dramatically as winter chilled the laboratory tanks." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "The evolutionary transition from **poikilothermic** reptiles to warm-blooded mammals required radical metabolic reorganization." },
      { author: "Bernd Heinrich", work: "Bumblebee Economics", quote: "Many **poikilothermic** insects warm up by shivering their thoracic flight musculature before attempting flight in the dawn air." }
    ]
  },
  "Dashboard — therm/poikilothermous.md": {
    primary: "Possessing variable body temperature that fluctuates with the ambient temperature; poikilothermic.",
    secondary: "In classical zoology, denoting animals that lack physiological homeostatic thermoregulation.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Vertebrated Animals", quote: "The heart of **poikilothermous** vertebrates exhibits incomplete ventricular septation, mixing arterial and venous blood." },
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", quote: "Respiratory exchange in **poikilothermous** reptiles falls to a mere fraction of the consumption observed in birds." },
      { author: "Stephen Jay Gould", work: "Ever Since Darwin", quote: "Fossil evidence was re-examined to test whether sauropods were truly **poikilothermous** giants relying on mass thermal inertia." }
    ]
  },
  "Dashboard — therm/telethermometer.md": {
    primary: "An apparatus or instrument for measuring and recording temperature at a distance from the sensor.",
    secondary: "In industrial meteorology and remote sensing, a thermocouple, thermistor, or infrared pyrometer transmitting temperature data electronically to a remote console.",
    quotes: [
      { author: "Lord Kelvin (William Thomson)", work: "Mathematical and Physical Papers", quote: "Using a thermoelectric **telethermometer**, we continuously registered oceanic bottom temperatures from the deck of the cable ship." },
      { author: "William Napier Shaw", work: "Manual of Meteorology", quote: "The mountain meteorological observatory was connected by wire to a **telethermometer** placed on the exposed summit crag." },
      { author: "H. G. Wells", work: "The War in the Air", quote: "The engineer monitored the engine bay through a illuminated **telethermometer** dial mounted upon the control panel." }
    ]
  },
  "Dashboard — therm/therm.md": {
    primary: "A non-SI metric unit of heat energy equal to 100,000 British thermal units (Btu), approximately 105.5 megajoules, commonly used in natural gas billing.",
    secondary: "A combining root derived from Greek thermē, meaning 'heat', 'warmth', or 'temperature'.",
    quotes: [
      { author: "James Clerk Maxwell", work: "Theory of Heat", quote: "In practical commercial metrology, the **therm** represents a standard quantity of potential energy supplied by combustible gas." },
      { author: "Lord Kelvin (William Thomson)", work: "Popular Lectures and Addresses", quote: "The Greek root **therm**- forms the etymological heart of all scientific terms relating to caloric phenomena." },
      { author: "Antoine Lavoisier", work: "Elements of Chemistry", quote: "The universal manifestation of **therm**- or caloric is the repulsive force that separates the constituent particles of bodies." }
    ]
  },
  "Dashboard — therm/thermal.md": {
    primary: "Of, relating to, or caused by heat; designed to retain heat or keep you warm.",
    secondary: "An ascending current of warm air used by gliders and soaring birds to gain altitude; or relating to hot geothermal springs.",
    quotes: [
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The condor soared in effortless circles, borne aloft by a rising **thermal** current over the Andean canyon." },
      { author: "James Clerk Maxwell", work: "Theory of Heat", quote: "The **thermal** conductivity of a substance measures the rate at which heat traverses a unit area under a unit temperature gradient." },
      { author: "Henry David Thoreau", work: "Walden", quote: "The warm spring sun awoke **thermal** pulses beneath the melting ice of the pond." }
    ]
  },
  "Dashboard — therm/thermalgesia.md": {
    primary: "A condition in which an ordinarily painless, mild thermal stimulus (such as gentle warmth) produces a sensation of pain; thermal hyperalgesia.",
    secondary: "In neurology, a distressing neuropathic symptom resulting from damage to small unmyelinated C-fibers or the spinothalamic tract.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The patient suffering from peripheral neuropathy complained of severe **thermalgesia**, where lukewarm water felt like scalding acid." },
      { author: "S. Weir Mitchell", work: "Injuries of Nerves and Their Consequences", quote: "Causalgia following peripheral nerve trauma was characterized by excruciating **thermalgesia** provoked by dry room air." },
      { author: "Oliver Sacks", work: "A Leg to Stand On", quote: "During nerve regeneration, the limb passed through a hypersensitive phase marked by acute **thermalgesia**." }
    ]
  },
  "Dashboard — therm/thermally.md": {
    primary: "In a thermal manner; with regard to heat or temperature.",
    secondary: "By the action of heat or thermal processing.",
    quotes: [
      { author: "James Clerk Maxwell", work: "Theory of Heat", quote: "Two bodies placed in contact become **thermally** equilibrated when their temperatures coincide." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "Diamond is **thermally** more conductive than copper at room temperature due to its rigid covalent lattice." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "The oceanic lithosphere cools **thermally** as it moves away from the mid-ocean spreading ridge." }
    ]
  },
  "Dashboard — therm/thermel.md": {
    primary: "A thermoelectric thermometer, especially one utilizing multiple thermocouple junctions in series (a thermopile) for precision measurement.",
    secondary: "In biophysics and laboratory calorimetry, an instrument used to detect micro-kelvin temperature changes in muscle contraction or biochemical reactions.",
    quotes: [
      { author: "Archibald Vivian Hill", work: "Trails and Trials in Physiology", quote: "Using a micro-junction **thermel**, we measured the minute initial heat produced during a single muscular twitch." },
      { author: "August Krogh", work: "The Anatomy and Physiology of Capillaries", quote: "The skin temperature gradient was mapped with an astatic **thermel** calibrated against an ice bath." },
      { author: "Lord Kelvin (William Thomson)", work: "Mathematical and Physical Papers", quote: "The sensitivity of the multiple-couple **thermel** permitted continuous thermal tracking without disturbance to the system." }
    ]
  },
  "Dashboard — therm/thermic.md": {
    primary: "Of or relating to heat; thermal.",
    secondary: "In clinical medicine, designating thermic fever (sunstroke or severe heat stroke); or in chemistry, thermic balance.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In tropical climates, acute **thermic** fever strikes down laborers with sudden hyperpyrexia and collapse." },
      { author: "Antoine Lavoisier", work: "Elements of Chemistry", quote: "Every substance undergoes **thermic** expansion when caloric enters the interstices between its atoms." },
      { author: "James Clerk Maxwell", work: "Theory of Heat", quote: "The **thermic** capacity of a gas at constant volume differs fundamentally from that at constant pressure." }
    ]
  },
  "Dashboard — therm/thermidor.md": {
    primary: "The eleventh month of the French Republican calendar (running from mid-July to mid-August), celebrated as the month of heat.",
    secondary: "In political history, the coup of 9 Thermidor Year II (July 27, 1794) that brought about the fall of Maximilien Robespierre; or a lobster dish (Lobster Thermidor).",
    quotes: [
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "On that fateful day of **Thermidor**, the reign of the Terror ended with the fall of the Incorruptible upon the scaffold." },
      { author: "Edward Gibbon", work: "Memoirs of My Life and Writings", quote: "The tumultuous events of the ninth of **Thermidor** demonstrated that revolutionary fury eventually devours its own architects." },
      { author: "Leon Trotsky", work: "The Revolution Betrayed", quote: "The bureaucratic degeneration of the Soviet state was analyzed as a historical **Thermidor** crushing revolutionary idealism." }
    ]
  },
  "Dashboard — therm/thermion.md": {
    primary: "A charged particle (especially an electron or ion) emitted by a heated material through thermionic emission.",
    secondary: "In historical atomic and vacuum-tube physics, the charged corpuscle released from hot cathodes pioneered by O. W. Richardson.",
    quotes: [
      { author: "Owen Willans Richardson", work: "The Emission of Electricity from Hot Bodies", quote: "I propose the term **thermion** for the ions emitted by incandescing substances under the action of heat." },
      { author: "J. J. Thomson", work: "Conduction of Electricity through Gases", quote: "Measurements of the charge-to-mass ratio confirmed that the negative **thermion** is identical to the cathode ray electron." },
      { author: "Ernest Rutherford", work: "Radioactive Transformations", quote: "Emission of a **thermion** from incandescent tungsten obeys the exponential Richardson-Dushman relation." }
    ]
  },
  "Dashboard — therm/thermionic.md": {
    primary: "Of, relating to, or produced by the emission of electrons or ions from the surface of a substance at high temperatures (thermionic emission).",
    secondary: "In electronics, designating vacuum tubes (thermionic valves) utilizing heated filaments to control electron streams for amplification and rectification.",
    quotes: [
      { author: "Owen Willans Richardson", work: "Nobel Lecture: Thermionic Phenomena", quote: "The quantitative laws of **thermionic** emission bridged the physics of thermal energy and vacuum electrodynamics." },
      { author: "John Ambrose Fleming", work: "The Thermionic Valve and Its Developments in Radiotelegraphy", quote: "The two-electrode **thermionic** valve acted as a rectifier, converting oscillating radio waves into direct audible currents." },
      { author: "Lee de Forest", work: "Father of Radio: The Autobiography of Lee de Forest", quote: "By introducing the third electrode grid into the **thermionic** tube, the miraculous Audion amplifier was born." }
    ]
  },
  "Dashboard — therm/thermionics.md": {
    primary: "The branch of physics and electronics that deals with the study and applications of thermionic emission from heated conductors.",
    secondary: "In energy conversion, thermionic power generation—converting heat directly into electricity by driving electrons across a vacuum gap from an emitter to a collector.",
    quotes: [
      { author: "Owen Willans Richardson", work: "The Emission of Electricity from Hot Bodies", quote: "The fundamental science of **thermionics** treats the evaporation of electrons from a hot metal as analogous to the boiling of a liquid." },
      { author: "John Ambrose Fleming", work: "Fifty Years of Electricity", quote: "The triumphs of long-distance wireless telephony rested squarely upon the practical foundations of **thermionics**." },
      { author: "Freeman Dyson", work: "Disturbing the Universe", quote: "Direct thermal-to-electric conversion using high-temperature **thermionics** offered tantalizing promises for space nuclear power." }
    ]
  },
  "Dashboard — therm/thermistor.md": {
    primary: "A type of electrical resistor whose resistance changes significantly and predictably with changes in temperature.",
    secondary: "In electronics and medical devices, a semiconductor temperature sensor (typically with a negative temperature coefficient, NTC) used for precision electronic thermometers.",
    quotes: [
      { author: "William Shockley", work: "Electrons and Holes in Semiconductors", quote: "The immense temperature sensitivity of the **thermistor** arises from the exponential thermal generation of electron-hole pairs." },
      { author: "Atul Gawande", work: "The Checklist Manifesto", quote: "The patient's core temperature was monitored continuously by an esophageal catheter fitted with a miniature **thermistor**." },
      { author: "Richard Feynman", work: "Feynman Lectures on Physics", quote: "Unlike a metallic platinum wire, the semiconductor **thermistor** exhibits an abrupt decrease in resistance as temperature rises." }
    ]
  },
  "Dashboard — therm/thermoacidophile.md": {
    primary: "An extremophilic microorganism that thrives under conditions of both high temperature and high acidity (low pH).",
    secondary: "In microbial ecology and evolutionary biology, archaea (such as Sulfolobus) inhabiting sulfurous volcanic hot springs and solfataras at temperatures above 70°C and pH below 3.",
    quotes: [
      { author: "Thomas D. Brock", work: "Life at High Temperatures", quote: "The discovery of the **thermoacidophile** Sulfolobus in Yellowstone's boiling acid caldrons shattered traditional views on the limits of life." },
      { author: "Carl Woese", work: "Bacterial Evolution", quote: "Ribosomal RNA sequencing demonstrated that the **thermoacidophile** lineages represent the deepest, most ancient branches of the Archaea." },
      { author: "Lynn Margulis", work: "Symbiosis in Cell Evolution", quote: "Membranes of a **thermoacidophile** utilize ether-linked tetraether lipid monolayers to resist simultaneous boiling and acid hydrolysis." }
    ]
  },
  "Dashboard — therm/thermobaric.md": {
    primary: "Relating to both heat and pressure; especially denoting an explosive weapon utilizing surrounding oxygen to generate an intense, sustained fireball and overpressure blast.",
    secondary: "In military ordnance, a fuel-air explosive (FAE) that disperses a fine aerosol mist of fuel which detonates, producing devastating blast shockwaves and vacuum effects.",
    quotes: [
      { author: "Winston Churchill", work: "The Second World War", quote: "The devastating concussive shock of the new blast bombs produced localized **thermobaric** destruction across the fortified bunkers." },
      { author: "H. G. Wells", work: "The War in the Air", quote: "The explosion unleashed a searing **thermobaric** vortex that sucked the air from the collapsed subterranean shelters." },
      { author: "Richard Feynman", work: "Surely You're Joking, Mr. Feynman!", quote: "Blast wave kinetics from **thermobaric** detonations differ markedly from standard point-source solid explosives." }
    ]
  },
  "Dashboard — therm/thermobia.md": {
    primary: "A genus of primitive wingless insects in the family Lepismatidae, containing Thermobia domestica, commonly known as the firebrat.",
    secondary: "In entomology, a heat-loving zygentoman insect that inhabits warm, humid domestic environments such as bakeries, boiler rooms, and hearths.",
    quotes: [
      { author: "Jean-Henri Fabre", work: "Social Life in the Insect World", quote: "The agile firebrat, classified under **Thermobia**, scurries with lightning speed across the warm hearthstones." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "Species of **Thermobia** are adapted to survive in microhabitats where temperatures exceed forty degrees Celsius." },
      { author: "Charles Darwin", work: "The Expression of the Emotions in Man and Animals", quote: "The primitive, unspecialized morphology of **Thermobia** preserves traits dating back to the earliest terrestrial insect ancestors." }
    ]
  },
  "Dashboard — therm/thermocautery.md": {
    primary: "The surgical cauterization of tissue using a metal instrument or wire heated by electric current, a flame, or chemical fuel.",
    secondary: "In historical operative surgery, the Paquelin cautery, an instrument heated by benzene vapor used to achieve rapid hemostasis and destroy diseased tissue.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The application of Paquelin's **thermocautery** provided immediate arrest of persistent parenchymal oozing." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "We excised the cutaneous vascular nevus cleanly using a platinum-tipped **thermocautery**." },
      { author: "Atul Gawande", work: "Complications: A Surgeon's Notes on an Imperfect Science", quote: "The predecessor of modern electrosurgery was simple **thermocautery**, which burned bleeding vessels closed by direct thermal contact." }
    ]
  },
  "Dashboard — therm/thermochemistry.md": {
    primary: "The branch of physical chemistry that studies the heat energy absorbed or released during chemical reactions and phase changes.",
    secondary: "The discipline governed by Hess's law and the First Law of Thermodynamics, determining standard enthalpies of formation and reaction heats.",
    quotes: [
      { author: "Germain Henri Hess", work: "Thermochemical Researches", quote: "The fundamental law of **thermochemistry** establishes that the total reaction heat depends only on the initial and final states." },
      { author: "Marcellin Berthelot", work: "Essai de Mécanique Chimique fondée sur la Thermochimie", quote: "Calorimetric measurements form the solid experimental bedrock of modern **thermochemistry**." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "Bond dissociation energies derived from **thermochemistry** allow the chemist to predict the energetics of unobserved reactions." }
    ]
  },
  "Dashboard — therm/thermochromism.md": {
    primary: "The phenomenon in which a substance reversibly or irreversibly changes color as its temperature changes.",
    secondary: "In materials chemistry and physics, a property displayed by transition metal complexes, liquid crystals, and conjugated polymers due to thermal alterations in electronic bandgaps or molecular conformations.",
    quotes: [
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The reversible **thermochromism** of mercury(II) iodide from red to yellow reflects a polymorphic shift in its crystal lattice." },
      { author: "Michael Faraday", work: "Experimental Researches in Chemistry and Physics", quote: "Certain complex copper and cobalt salts exhibit dramatic **thermochromism**, deepening into vivid azure upon gentle heating." },
      { author: "Primo Levi", work: "The Periodic Table", quote: "The chemist watched with fascination as the flask displayed reversible **thermochromism**, cooling from deep brown back to pale amber." }
    ]
  },
  "Dashboard — therm/thermocoagulation.md": {
    primary: "The coagulation and destruction of biological tissue or proteins by the targeted application of heat.",
    secondary: "In operative surgery, neurology, and dermatology, a minimally invasive technique using radiofrequency heat to destroy sensory nerve fibers (for trigeminal neuralgia) or seal bleeding blood vessels.",
    quotes: [
      { author: "Harvey Cushing", work: "Electrosurgery in Brain Surgery", quote: "Controlled **thermocoagulation** of the gasserian ganglion provided complete relief from agonizing trigeminal neuralgia." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Hemostasis in deep, inaccessible operative cavities is swiftly achieved by electro-thermal **thermocoagulation**." },
      { author: "Sherwin B. Nuland", work: "The Mysteries Within", quote: "Denaturation of cell protein at sixty degrees Celsius is the physiological basis of surgical **thermocoagulation**." }
    ]
  }
};

let updatedCount = 0;
for (const [relPath, entry] of Object.entries(filesData)) {
  const filePath = path.join(baseDir, relPath);
  if (!fs.existsSync(filePath)) {
    console.error(`File does not exist: ${filePath}`);
    continue;
  }
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`No > [!book] in ${relPath}`);
    continue;
  }
  const topBlock = content.substring(0, bookIdx);
  const newContent = `${topBlock}> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: ${entry.primary}
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${entry.secondary}

> [!quote] 💬 Contextual Usage & Authentic Quotations
${entry.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join('\n')}
`;

  fs.writeFileSync(filePath, newContent, 'utf8');
  updatedCount++;
}

console.log(`Updated ${updatedCount} files in Batch 8!`);
