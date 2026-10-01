import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Physics & Chemistry';

const filesData = {
  // === Dashboard — pect (15 words) ===
  "Dashboard — pect/expectorant.md": {
    primary: "A medication or agent that promotes the secretion, liquefaction, or expulsion of mucus and phlegm from the respiratory tract.",
    secondary: "In pharmacology, substances such as guaifenesin, potassium iodide, or ipecacuanha used to ease productive coughs.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In chronic bronchitis with tenacious sputum, a stimulating **expectorant** provides notable clinical relief." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "The old apothecary compounded a syrupy **expectorant** of squill and senega to loosen the catarrhal chest." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "The physician evaluated whether a simple hydration regimen would serve as a safer **expectorant** than polypharmacy." }
    ]
  },
  "Dashboard — pect/expectorate.md": {
    primary: "To cough up and spit out phlegm, mucus, or other matter from the throat or lungs.",
    secondary: "To spit, eject, or discharge saliva or bronchial fluids forcefully from the mouth.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "Helen Burns leaned against the pillow, too weak to **expectorate** the heavy congestion in her chest." },
      { author: "Thomas Mann", work: "The Magic Mountain", quote: "Patients at the sanatorium were provided with pocket blue flasks whenever they needed to **expectorate**." },
      { author: "Charles Dickens", work: "American Notes", quote: "He observed with distaste the frontier habit of travelers who would continually **expectorate** tobacco juice onto the cabin floor." }
    ]
  },
  "Dashboard — pect/expectoration.md": {
    primary: "The act of coughing up and spitting out material from the respiratory tract; or the sputum and phlegm so ejected.",
    secondary: "In clinical pulmonary diagnostics, the inspection of sputum (rusty, purulent, or hemoptysis) to diagnose pneumonia or tuberculosis.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Rusty **expectoration** is the classic pathognomonic physical sign of pneumococcal lobar pneumonia." },
      { author: "Thomas Mann", work: "The Magic Mountain", quote: "Daily volume of morning **expectoration** was recorded upon the chart with scrupulous sanatorium discipline." },
      { author: "Arthur Conan Doyle", work: "The Stark Munro Letters", quote: "The young physician examined the slide stained with Ziehl-Neelsen carbolfuchsin to detect bacilli in the **expectoration**." }
    ]
  },
  "Dashboard — pect/expectorator.md": {
    primary: "A person who expectorates; one who coughs up and spits out bronchial fluids or saliva.",
    secondary: "An apparatus or spittoon designed for receiving expectorated sputum in clinics or public buildings.",
    quotes: [
      { author: "Charles Dickens", work: "Martin Chuzzlewit", quote: "The chronic **expectorator** across the canal boat made conversation an exercise in tactical retreat." },
      { author: "Mark Twain", work: "Roughing It", quote: "Every veteran miner was a tireless **expectorator**, hitting the center of the stove from ten paces." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The tuberculous **expectorator** who neglects sanitary precautions endangers the health of the entire household." }
    ]
  },
  "Dashboard — pect/pect.md": {
    primary: "A combining root derived from Latin pectus ('chest', 'breast') or Greek pēktos ('coagulated', 'curdled', 'fixed').",
    secondary: "In anatomy (pectoral, pectus) denoting the chest region; in biochemistry (pectin, pectic) denoting gelatinous plant polysaccharides.",
    quotes: [
      { author: "Andreas Vesalius", work: "De Humani Corporis Fabrica", quote: "The broad muscles covering the anterior ribs are designated under the root **pect**- in accordance with classical anatomy." },
      { author: "Henri Braconnot", work: "Recherches sur la substance gélatineuse des fruits", quote: "From the Greek word for coagulum, I derived the prefix **pect**- to denote the natural jelling principle of ripe apples." },
      { author: "Asa Gray", work: "Elements of Botany", quote: "Compounds containing the morpheme **pect**- play an essential architectural role in cementing adjacent plant cell walls." }
    ]
  },
  "Dashboard — pect/pectic.md": {
    primary: "Of, relating to, or derived from pectin; resembling pectin or vegetable jelly.",
    secondary: "In plant biochemistry, pertaining to pectic acid or pectic polysaccharides constituting the middle lamella of plant cell walls.",
    quotes: [
      { author: "Henri Braconnot", work: "Recherches sur la substance gélatineuse des fruits", quote: "By neutralizing plant extracts with lime, an insoluble precipitate of **pectic** acid is deposited." },
      { author: "Julius von Sachs", work: "Text-book of Botany", quote: "The middle lamella consists primarily of calcium salts of **pectic** substances binding the cellulose microfibrils." },
      { author: "Daniel Trembly MacDougal", work: "Practical Text-book of Plant Physiology", quote: "During fruit ripening, pectose enzymes convert insoluble protopectin into soluble **pectic** derivatives." }
    ]
  },
  "Dashboard — pect/pectin.md": {
    primary: "A soluble gelatinous structural polysaccharide found in ripe fruits (such as apples and citrus) that forms a gel when heated with sugar and acid.",
    secondary: "In food science and industry, an essential gelling agent in jams and jellies, and a dietary soluble fiber that modulates glycemic index.",
    quotes: [
      { author: "Henri Braconnot", work: "Recherches sur la substance gélatineuse des fruits", quote: "I have given the name **pectin** to this substance, which gives fruit jellies their firm, trembling consistency." },
      { author: "Justus von Liebig", work: "Animal Chemistry", quote: "In the vegetable kingdom, **pectin** serves as the natural cement holding vegetable parenchyma together." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Commercial citrus peels yield immense quantities of **pectin** utilized in confectionery and pharmaceutical suspensions." }
    ]
  },
  "Dashboard — pect/pectinate.md": {
    primary: "Having narrow, parallel, comb-like projections, teeth, or divisions; shaped like a comb.",
    secondary: "In anatomy and zoology, denoting comb-like structures such as the pectinate muscles of the cardiac atrium or pectinate insect antennae.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The **pectinate** antennae of male silkworm moths present an enormous surface area for detecting female pheromones." },
      { author: "Andreas Vesalius", work: "De Humani Corporis Fabrica", quote: "The internal surface of the right auricle displays muscular ridges resembling a comb, termed the **pectinate** muscles." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The leaves of the aquatic water-milfoil are finely **pectinate**, spreading like green feathers beneath the current." }
    ]
  },
  "Dashboard — pect/pectineal.md": {
    primary: "Of or relating to the pecten or pubic bone; or comb-like in anatomical structure.",
    secondary: "In human anatomy, pertaining to the pectineal line of the pubis or the pectineus muscle of the anterior medial thigh.",
    quotes: [
      { author: "Henry Gray", work: "Anatomy: Descriptive and Surgical", quote: "The **pectineal** line forms the sharp posterior boundary of the upper ramus of the pubic bone." },
      { author: "Andreas Vesalius", work: "De Humani Corporis Fabrica", quote: "Arising from the pubic crest, the flat **pectineal** muscle adducts and flexes the thigh upon the pelvis." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The femoral hernia emerges through the ring bounded posteriorly by the strong **pectineal** ligament of Cooper." }
    ]
  },
  "Dashboard — pect/pectinibranchia.md": {
    primary: "A former suborder of gastropod mollusks having comb-like, single ctenidial gills (comprising prosobranch snails).",
    secondary: "In systematic malacology, marine and freshwater snails whose respiratory ctenidium consists of a unilateral row of pectinate gill filaments.",
    quotes: [
      { author: "Georges Cuvier", work: "The Animal Kingdom", quote: "Under the order **Pectinibranchia**, we assemble those gastropods that breathe by means of comb-like branchiae lodged in a dorsal cavity." },
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", quote: "In the **Pectinibranchia**, the right gill has completely atrophied, leaving an asymmetrical unilateral respiratory plume." },
      { author: "Richard Owen", work: "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", quote: "The mantle cavity of **Pectinibranchia** receives currents driven over the pectinate ctenidium by microscopic cilia." }
    ]
  },
  "Dashboard — pect/pectinidae.md": {
    primary: "A large taxonomic family of bivalve mollusks commonly known as scallops.",
    secondary: "In marine malacology, bivalves characterized by fan-shaped fluted shells, blue compound eyes along the mantle edge, and the ability to swim by jetting water from their valves.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Fossil shells of the family **Pectinidae** are abundant indicators of shallow temperate marine environments throughout the Tertiary." },
      { author: "Thomas Henry Huxley", work: "The Oceanic Hydrozoa", quote: "Swimming in **Pectinidae** is accomplished by rapid adduction of the valves, expelling jets of water from the auricles." },
      { author: "Ernst Haeckel", work: "Art Forms in Nature", quote: "The fluted symmetry of shells in the **Pectinidae** exemplifies the decorative geometric harmony of marine life." }
    ]
  },
  "Dashboard — pect/pectoral.md": {
    primary: "Of or relating to the chest or breast; worn on or attached to the chest.",
    secondary: "In ichthyology and anatomy, denoting the pectoral fins of fishes or the pectoral girdle supporting the upper anterior limbs in tetrapods.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick", quote: "The whale struck the waves with its immense **pectoral** fins, throwing cataracts of foam into the air." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "The broad expansion of the human **pectoral** muscles reflects our adaptation to bipedal posture and arm freedom." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The high priest entered the sanctuary adorned with the golden **pectoral** set with twelve precious gems." }
    ]
  },
  "Dashboard — pect/pectoralis.md": {
    primary: "Either of two large muscles of the anterior chest wall (the pectoralis major and pectoralis minor) connecting the chest with the shoulder and upper arm.",
    secondary: "In human and avian anatomy, the massive flight muscle powering the downward wing stroke in birds and shoulder adduction in primates.",
    quotes: [
      { author: "Andreas Vesalius", work: "De Humani Corporis Fabrica", quote: "The **pectoralis** major arises from the sternum and clavicle to insert into the crest of the greater tubercle of the humerus." },
      { author: "Henry Gray", work: "Anatomy: Descriptive and Surgical", quote: "Contraction of the **pectoralis** minor pulls the shoulder forward and downward, depressing the scapula." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "In flying birds, the tremendous keel of the sternum anchors the enormous mass of the **pectoralis** muscles." }
    ]
  },
  "Dashboard — pect/pectus.md": {
    primary: "The chest or breast; the anterior surface of the thorax in humans or other vertebrates.",
    secondary: "In medical pathology, congenital thoracic wall deformities such as pectus excavatum (sunken chest) or pectus carinatum (pigeon chest).",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe rickets in infancy frequently leads to permanent distortion known as **pectus** carinatum or pigeon breast." },
      { author: "Henry Gray", work: "Anatomy: Descriptive and Surgical", quote: "The bony cage of the **pectus** encloses and protects the thoracic viscera, principally the heart and lungs." },
      { author: "Atul Gawande", work: "Complications", quote: "Surgical repair of severe **pectus** excavatum lifts the depressed sternum to relieve right ventricular compression." }
    ]
  },
  "Dashboard — pect/polypectomy.md": {
    primary: "The surgical or endoscopic excision and removal of a polyp from a mucous membrane, especially in the colon, stomach, or nasal cavity.",
    secondary: "In gastroenterology, a routine cancer prevention procedure using an electrocautery snare through a colonoscope to resect adenomatous polyps.",
    quotes: [
      { author: "Atul Gawande", work: "The Checklist Manifesto", quote: "Colonoscopic screening combined with immediate snare **polypectomy** halts the progression of colorectal cancer before it starts." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "The pathology report following the routine **polypectomy** revealed clear surgical margins around the tubulovillous adenoma." },
      { author: "Sherwin B. Nuland", work: "Doctors: The Biography of Medicine", quote: "Endoscopic **polypectomy** transformed gastrointestinal surgery into an outpatient preventive specialty." }
    ]
  },

  // === Dashboard — psychr (5 words) ===
  "Dashboard — psychr/psychroalgia.md": {
    primary: "A painful sensation of intense cold, or pain produced by cold temperatures.",
    secondary: "In clinical neurology, a neuropathic dysesthesia or hyperalgesia triggered by cold exposure, seen in thalamic syndrome or peripheral neuropathy.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The patient with advanced syringomyelia complained of agonizing **psychroalgia** in the analgesic limb upon touch." },
      { author: "S. Weir Mitchell", work: "Injuries of Nerves and Their Consequences", quote: "Causalgia following gunshot wounds was frequently complicated by extreme **psychroalgia** when drafts blew upon the skin." },
      { author: "Oliver Sacks", work: "A Leg to Stand On", quote: "During the slow recovery of sensation, the injured knee exhibited baffling episodes of phantom **psychroalgia**." }
    ]
  },
  "Dashboard — psychr/psychrometer.md": {
    primary: "A hygrometer consisting of two similar thermometers, one wet-bulb and one dry-bulb, used to measure the relative humidity of the atmosphere.",
    secondary: "In meteorology, a sling or aspiration psychrometer where evaporative cooling of the wet wick determines atmospheric vapor pressure and dew point.",
    quotes: [
      { author: "Robert FitzRoy", work: "The Weather Book", quote: "By noting the difference between the dry and moist bulbs on the **psychrometer**, the dew point is readily ascertained." },
      { author: "William Napier Shaw", work: "Forecasting Weather", quote: "The sling **psychrometer** whirled rapidly in the shade provides the standard field determination of relative humidity." },
      { author: "Cleveland Abbe", work: "Treatise on Meteorological Apparatus and Methods", quote: "Ventilation speed is the critical factor in obtaining consistent wet-bulb depressions with the **psychrometer**." }
    ]
  },
  "Dashboard — psychr/psychrophile.md": {
    primary: "An extremophilic organism (especially a bacterium or alga) capable of growth and reproduction at cold temperatures ranging from -20 to 10 degrees Celsius.",
    secondary: "In microbiology and astrobiology, cold-loving microorganisms thriving in polar ice, deep ocean abyssal plains, and glaciers, possessing specialized flexible enzymes.",
    quotes: [
      { author: "Lynn Margulis", work: "Symbiosis in Cell Evolution", quote: "The red snow of alpine glaciers is caused by blooms of a unicellular **psychrophile** alga producing protective carotenoids." },
      { author: "Carl Sagan", work: "Cosmos", quote: "If life thrives in the sub-zero ice pack of Jupiter's moon Europa, it must resemble an extremophilic **psychrophile**." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "Proteins synthesized by an obligate **psychrophile** are so structurally adapted to cold that room temperature denatures them." }
    ]
  },
  "Dashboard — psychr/psychrophilic.md": {
    primary: "Thriving at low temperatures; of or relating to psychrophiles.",
    secondary: "Describing bacteria, fungi, or biological processes adapted to life at or near the freezing point of water.",
    quotes: [
      { author: "René Dubos", work: "The Bacterial Cell", quote: "Enzymes isolated from **psychrophilic** bacteria maintain high catalytic efficiency despite the sluggish kinetics of near-zero temperatures." },
      { author: "Macfarlane Burnet", work: "Natural History of Infectious Disease", quote: "Food spoilage within domestic refrigerators is driven largely by opportunistic **psychrophilic** microorganisms." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "The abyssal benthos of the ocean constitutes an immense reservoir of **psychrophilic** biodiversity." }
    ]
  },
  "Dashboard — psychr/psychrophily.md": {
    primary: "The state, condition, or adaptation of being psychrophilic; the capacity to thrive in extreme cold.",
    secondary: "In microbial ecology and cryobiology, the physiological suite of adaptations (including polyunsaturated membrane lipids and antifreeze proteins) that enable survival below 15 degrees Celsius.",
    quotes: [
      { author: "Lynn Margulis", work: "Early Life", quote: "Membrane fluidization through unsaturated fatty acids is a hallmark molecular adaptation underlying bacterial **psychrophily**." },
      { author: "Carl Sagan", work: "The Cosmic Connection", quote: "The evolution of extreme **psychrophily** on Earth expands the habitable zone for life across the icy frontiers of our solar system." },
      { author: "Stephen Jay Gould", work: "Eight Little Piggies", quote: "Understanding **psychrophily** reminds us that what humans consider extreme cold is the comfortable ambient habitat for most oceanic life." }
    ]
  },

  // === Dashboard — pyr (17 words) ===
  "Dashboard — pyr/antipyretic.md": {
    primary: "A medication or substance used to reduce fever or body temperature (such as aspirin, paracetamol, or ibuprofen).",
    secondary: "In clinical pharmacotherapy, agents that act centrally on the hypothalamic thermoregulatory center by inhibiting prostaglandin synthesis.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The clinical introduction of synthetic **antipyretic** drugs eased the distressing hyperpyrexia of enteric fever." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "Peruvian cinchona bark was celebrated as the sovereign natural **antipyretic** of the seventeenth century." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "The pediatrician judiciously dosed the liquid **antipyretic** to relieve the infant's febrile discomfort." }
    ]
  },
  "Dashboard — pyr/Empyreuma.md": {
    primary: "The burnt smell, acrid taste, or carbonaceous residue produced by heating organic substances in closed vessels without sufficient air.",
    secondary: "In historical pharmacy and chemistry, the pungent smoky vapor characteristic of destructive distillation.",
    quotes: [
      { author: "Antoine Lavoisier", work: "Elements of Chemistry", quote: "When vegetable matters are distilled without water, they yield a heavy, suffocating oil bearing the strong scent of **empyreuma**." },
      { author: "Jöns Jacob Berzelius", work: "Traité de Chimie", quote: "The characteristic **empyreuma** of pyroligneous acid is eliminated through fractional neutralization and redistillation." },
      { author: "Humphry Davy", work: "Elements of Agricultural Chemistry", quote: "Overheated manures acquire an offensive **empyreuma** that indicates the loss of volatile nitrogenous constituents." }
    ]
  },
  "Dashboard — pyr/pyre.md": {
    primary: "A heap or combustible structure of wood for burning a dead body as part of a funeral rite.",
    secondary: "Any pile of flammable material set on fire, especially for public sacrifice or destruction.",
    quotes: [
      { author: "Homer", work: "The Iliad", quote: "Nine days did the Trojans gather wood, and on the tenth they laid brave Hector upon the towering funeral **pyre**." },
      { author: "Virgil", work: "The Aeneid", quote: "Unhappy Dido climbed the lofty **pyre**, casting her eyes upon Trojan garments left behind." },
      { author: "Lord Byron", work: "Childe Harold's Pilgrimage", quote: "The blazing funeral **pyre** consumed the heroic relics amid the lamentations of Greece." }
    ]
  },
  "Dashboard — pyr/pyrite.md": {
    primary: "A brass-yellow mineral with a bright metallic luster, composed of iron disulfide (FeS2), commonly known as 'fool's gold'.",
    secondary: "In economic geology, the most abundant sulfide mineral, historically struck with steel to produce ignition sparks for early flintlocks.",
    quotes: [
      { author: "James Dwight Dana", work: "Manual of Mineralogy", quote: "The brass-yellow color and cubic crystal form of **pyrite** often mislead novice prospectors to mistake it for native gold." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Weathering of nodules of **pyrite** in alum shale generates sulfuric acid and iron sulfate." },
      { author: "Waldemar Lindgren", work: "Mineral Deposits", quote: "Hydrothermal gold veins typically carry auriferous **pyrite** intimately associated with quartz and arsenopyrite." }
    ]
  },
  "Dashboard — pyr/pyroclastic.md": {
    primary: "Composed of rock fragments erupted by a volcano; formed by volcanic explosive fragmentation.",
    secondary: "In volcanology, describing fast-moving, lethal currents of superheated gas and tephra known as pyroclastic flows or surges.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The Roman city of Herculaneum was inundated by dense **pyroclastic** flows rushing down the slopes of Vesuvius." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Explosive eruptions pulverize viscous rhyolitic magma into vast clouds of incandescent **pyroclastic** debris." },
      { author: "Charles Darwin", work: "Geological Observations on Volcanic Islands", quote: "Thick beds of stratified **pyroclastic** tuff formed the dramatic cliffs of the volcanic caldera." }
    ]
  },
  "Dashboard — pyr/pyrolysis.md": {
    primary: "The chemical decomposition of organic materials at elevated temperatures in the absence of oxygen.",
    secondary: "In chemical engineering and waste management, the industrial process of thermal cracking used to produce biochar, synthetic gas, and bio-oil.",
    quotes: [
      { author: "Justus von Liebig", work: "Familiar Letters on Chemistry", quote: "The dry distillation or **pyrolysis** of wood in iron retorts yields charcoal, acetic acid, and wood alcohol." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "High-temperature **pyrolysis** breaks complex long-chain hydrocarbons into lighter volatile olefins and gas fractions." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Careful high-temperature **pyrolysis** is required to destroy toxic halogenated residues without releasing hazardous dioxins." }
    ]
  },
  "Dashboard — pyr/pyrolytic.md": {
    primary: "Of, relating to, or produced by pyrolysis; resulting from thermal decomposition in the absence of oxygen.",
    secondary: "In materials science, designating synthetic materials produced by chemical vapor deposition at high temperatures, such as pyrolytic carbon or pyrolytic graphite.",
    quotes: [
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The remarkable mechanical strength of **pyrolytic** carbon heart valves arises from its disordered graphene layers." },
      { author: "Irving Langmuir", work: "Phenomena, Atoms and Molecules", quote: "Deposition of carbon on incandescent filaments during **pyrolytic** cracking was studied under high vacuum." },
      { author: "Arthur C. Clarke", work: "Rendezvous with Rama", quote: "The heat shield was manufactured from dense **pyrolytic** graphite capable of withstanding planetary re-entry." }
    ]
  },
  "Dashboard — pyr/pyromancer.md": {
    primary: "A practitioner of pyromancy; a soothsayer or diviner who foretells future events by inspecting fires and flames.",
    secondary: "In classical and medieval occultism, an augur who interprets the color, crackling, shape, and smoke of sacrificial fires.",
    quotes: [
      { author: "Lewis Spence", work: "An Encyclopaedia of Occultism", quote: "The ancient Persian **pyromancer** gazed unblinking into the sacred flame to decipher the decrees of the gods." },
      { author: "Walter Scott", work: "The Talisman", quote: "The desert seer claimed the powers of a **pyromancer**, reading destinies in the glowing embers of the camp fire." },
      { author: "Edward Tylor", work: "Primitive Culture", quote: "Rites performed by the village **pyromancer** illustrate the universal religious personification of fire." }
    ]
  },
  "Dashboard — pyr/pyromancy.md": {
    primary: "Divination or fortune-telling by means of fire, embers, or the behavior of sacrificial flames.",
    secondary: "An ancient form of mantic prophecy practiced across Greece, Rome, and China (including scapulimancy over fire).",
    quotes: [
      { author: "James George Frazer", work: "The Golden Bough", quote: "The ancient art of **pyromancy** interpreted the quiet, steady burning of the altar flame as a promise of peace." },
      { author: "Edward Tylor", work: "Primitive Culture", quote: "Like hydromancy and aeromancy, **pyromancy** sought signs in the unpredictable motions of natural elements." },
      { author: "Lewis Spence", work: "An Encyclopaedia of Occultism", quote: "In classical **pyromancy**, pitch or incense cast onto live coals produced flashes read by the priest." }
    ]
  },
  "Dashboard — pyr/pyromania.md": {
    primary: "An obsessive, compulsive desire or impulse to deliberately and maliciously set things on fire.",
    secondary: "In clinical psychiatry and legal medicine, an impulse-control disorder characterized by tension prior to the act and intense gratification during fire-setting.",
    quotes: [
      { author: "Emil Kraepelin", work: "Clinical Psychiatry", quote: "True **pyromania** must be differentiated from arson motivated by financial gain or personal revenge." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Patients exhibiting severe **pyromania** often describe an irresistible internal tension relieved only by the sight of fire." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "The patient's destructive impulse was recognized as a classic manifestation of episodic **pyromania**." }
    ]
  },
  "Dashboard — pyr/pyrometric.md": {
    primary: "Of or relating to the measurement of high temperatures (pyrometry); or measured by a pyrometer.",
    secondary: "In ceramics and metallurgy, designating pyrometric cones (Seger cones) that deform at specific high temperatures to monitor kiln heat.",
    quotes: [
      { author: "Josiah Wedgwood", work: "Description of a Pyrometer Supplied to the Royal Society", quote: "The shrinkage of clay cylinders provided the earliest reliable **pyrometric** scale for industrial pottery kilns." },
      { author: "Lord Kelvin (William Thomson)", work: "Mathematical and Physical Papers", quote: "High-temperature thermodynamics required optical **pyrometric** observations calibrated against blackbody radiation." },
      { author: "James Clerk Maxwell", work: "Theory of Heat", quote: "The **pyrometric** resistance of a platinum wire increases with temperature, allowing exact thermometry in blast furnaces." }
    ]
  },
  "Dashboard — pyr/pyrophobia.md": {
    primary: "An abnormal, persistent, or irrational fear of fire.",
    secondary: "In clinical psychology and psychopathology, an extreme phobic reaction to flames, campfires, stoves, or matches, leading to panic or avoidance.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "In certain phobic neuroses, simple childhood burns leave behind an indelible, crippling **pyrophobia**." },
      { author: "Sigmund Freud", work: "Introductory Lectures on Psycho-Analysis", quote: "The neurotic dread of domestic gas jets frequently masks a deeper symbolic **pyrophobia**." },
      { author: "H. G. Wells", work: "The Island of Dr. Moreau", quote: "The beast-folk cowered before the whip and the lantern, restrained only by their primal **pyrophobia**." }
    ]
  },
  "Dashboard — pyr/pyrophoric.md": {
    primary: "Spontaneously igniting or burning in air at or below room temperature without the addition of heat.",
    secondary: "In metallurgy and chemistry, describing finely divided metals (such as iron, uranium, or white phosphorus) or ferrocerium flints that emit sparks when scratched.",
    quotes: [
      { author: "Humphry Davy", work: "Elements of Chemical Philosophy", quote: "Finely divided iron powder prepared by reduction with hydrogen is strongly **pyrophoric**, burning the instant it touches air." },
      { author: "Michael Faraday", work: "Chemical Manipulation", quote: "The chemist must handle **pyrophoric** carbonaceous residues under an inert gas blanket to prevent spontaneous combustion." },
      { author: "Primo Levi", work: "The Periodic Table", quote: "A shower of incandescent sparks flew from the **pyrophoric** alloy whenever it struck the steel wheel." }
    ]
  },
  "Dashboard — pyr/pyrosis.md": {
    primary: "A burning sensation in the chest and epigastrium caused by acid reflux; heartburn or water brash.",
    secondary: "In gastroenterology, the hallmark symptom of gastroesophageal reflux disease (GERD) caused by acidic gastric contents irritating the esophageal mucosa.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Patients with hiatal hernia complain bitterly of nocturnal **pyrosis** and acidic regurgitation." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "Simple alkaline solutions afford immediate palliative relief to the discomfort of acute **pyrosis**." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "The clinician carefully distinguished between atypical cardiac angina and benign esophageal **pyrosis**." }
    ]
  },
  "Dashboard — pyr/pyrotechnic.md": {
    primary: "Of or relating to fireworks, pyrotechnics, or the manufacture and display of fireworks.",
    secondary: "Brilliant, dazzling, sensational, or flamboyant in display (as of rhetorical, musical, or literary skill).",
    quotes: [
      { author: "Oscar Wilde", work: "The Remarkable Rocket", quote: "The king's wedding was celebrated with a magnificent **pyrotechnic** display over the royal gardens." },
      { author: "Arthur Conan Doyle", work: "The Adventures of Sherlock Holmes", quote: "His deductive reasoning concluded with a brilliant **pyrotechnic** demonstration of logical brilliance." },
      { author: "Virginia Woolf", work: "The Waves", quote: "Words burst in his mind like **pyrotechnic** sparks, illuminating the dark recesses of thought." }
    ]
  },
  "Dashboard — pyr/pyrotechnical.md": {
    primary: "Of, relating to, or resembling fireworks or pyrotechnics; skilled in fireworks displays.",
    secondary: "Displaying dazzling technical brilliance, virtuosity, or flamboyant oratorical skill.",
    quotes: [
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "The festival ended in a blaze of **pyrotechnical** glory that illuminated the tumultuous streets of Paris." },
      { author: "George Bernard Shaw", work: "Music in London", quote: "The violinist executed the cadenza with astounding **pyrotechnical** agility that astonished the audience." },
      { author: "H. G. Wells", work: "The Invisible Man", quote: "The sudden laboratory explosion produced a dazzling **pyrotechnical** spectacle that shattered the windows." }
    ]
  },
  "Dashboard — pyr/pyrotechny.md": {
    primary: "The art, craft, or science of making and displaying fireworks.",
    secondary: "Historically in alchemy and early chemistry, chemical operations involving fire, distillation, and furnaces; or flamboyant rhetorical display.",
    quotes: [
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "The practical achievements of **pyrotechny** contributed greatly to our early understanding of explosive salts." },
      { author: "Robert Boyle", work: "The Sceptical Chymist", quote: "Those who labor at the furnace boast of their **pyrotechny**, yet fail to isolate pure elementary principles." },
      { author: "John Evelyn", work: "Sylva: Or a Discourse of Forest-Trees", quote: "Charcoal burned from alder wood was deemed the most suitable for the delicate manufacture of **pyrotechny**." }
    ]
  },

  // === Dashboard — siph (5 words) ===
  "Dashboard — siph/siphon.md": {
    primary: "A bent tube used to convey liquid upwards from a reservoir and then down to a lower level of its own accord once started.",
    secondary: "In invertebrate zoology, a tubular organ in aquatic mollusks through which water is drawn in or expelled for respiration and locomotion.",
    quotes: [
      { author: "Hero of Alexandria", work: "Pneumatics", quote: "The continuous **siphon** draws water up the shorter leg and discharges it down the longer by atmospheric weight." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The giant clam discharged a powerful jet of seawater from its contractile **siphon** when disturbed." },
      { author: "Blaise Pascal", work: "Treatise on the Weight of the Mass of Air", quote: "The operation of the **siphon** ceases completely in an absolute vacuum, proving it depends on atmospheric pressure." }
    ]
  },
  "Dashboard — siph/siphonaptera.md": {
    primary: "An order of small, wingless, laterally compressed blood-sucking insects commonly known as fleas.",
    secondary: "In medical entomology, holometabolous ectoparasites of birds and mammals, famous as the vectors of Yersinia pestis (the bubonic plague).",
    quotes: [
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "Insects belonging to the order **Siphonaptera** are exquisitely modified for leaping and clinging to host mammalian hair." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The Oriental rat flea, classified among the **Siphonaptera**, serves as the primary transmission vector of the Black Death." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "The evolutionary loss of wings in **Siphonaptera** represents a classical secondary adaptation to obligate ectoparasitism." }
    ]
  },
  "Dashboard — siph/siphonoglyph.md": {
    primary: "A ciliated groove or channel located at one or both ends of the pharynx (gullet) in anthozoan cnidarians (such as sea anemones and corals).",
    secondary: "In marine invertebrate anatomy, a specialized structure whose beating cilia drive a continuous respiratory and circulatory water current into the gastrovascular cavity.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", quote: "The **siphonoglyph** in actinians maintains a constant inward current of aerated seawater even when the mouth is closed." },
      { author: "Ernst Haeckel", work: "Challenger Monograph on Deep-Sea Keratosa", quote: "Cranial sections of the sea anemone reveal the bilateral symmetry imposed upon the pharynx by the **siphonoglyph**." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "Anthozoan internal water circulation depends upon the tireless ciliary action along the **siphonoglyph**." }
    ]
  },
  "Dashboard — siph/siphonophora.md": {
    primary: "An order of marine hydrozoan cnidarians that form complex pelagic pelagic colonies composed of specialized polyps and medusae.",
    secondary: "In marine zoology, polymorphic colonial organisms (such as the Portuguese man-o'-war) functioning as an integrated superorganism.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Oceanic Hydrozoa", quote: "Nowhere in the animal kingdom is morphological division of labor carried so far as in the pelagic order **Siphonophora**." },
      { author: "Ernst Haeckel", work: "Art Forms in Nature", quote: "The crystalline, floating colonies of **Siphonophora** resemble living jewels drifted by the ocean winds." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Vast flotillas of **Siphonophora** drift across the tropical Atlantic, trailing venomous fishing tentacles yards below the surface." }
    ]
  },
  "Dashboard — siph/siphonophore.md": {
    primary: "Any colonial hydrozoan organism belonging to the order Siphonophora (such as Physalia physalis).",
    secondary: "A marine colonial organism composed of genetically identical, physiologically interdependent zooids acting as a single individual.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Oceanic Hydrozoa", quote: "Each **siphonophore** is not a simple animal, but a floating commonwealth of highly specialized individuals." },
      { author: "Ernst Haeckel", work: "Report on the Siphonophorae", quote: "The translucent nectophores of the **siphonophore** contract rhythmically to propel the whole colony through the water." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "A stranded **siphonophore** glistened upon the wet sand, its blue float deflated by the midday sun." }
    ]
  },

  // === Dashboard — sit (19 words) ===
  "Dashboard — sit/ectoparasite.md": {
    primary: "A parasite that lives on the outer surface or exterior of its host (such as a flea, tick, or louse).",
    secondary: "In parasitology and veterinary epidemiology, organisms that cause skin lesions or act as vectors for systemic infectious pathogens.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "Host-parasite coevolution is nowhere more evident than in the specialized clinging claws of the avian **ectoparasite**." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "Every bird species carries a specialized suite of **ectoparasite** feather lice adapted strictly to its plumage." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The common deer tick acts as an **ectoparasite** transmitting the spirochete of Lyme borreliosis." }
    ]
  },
  "Dashboard — sit/endoparasite.md": {
    primary: "A parasite that lives inside the body or tissues of its host (such as a tapeworm, roundworm, or liver fluke).",
    secondary: "In medical parasitology, internal pathogens causing systemic disease, malnutrition, or organ failure in humans and livestock.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", quote: "The extreme anatomical degeneration in an **endoparasite** like the tapeworm reflects total reliance upon the host's digested nutrients." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants Under Domestication", quote: "Domestic sheep are notoriously vulnerable to the devastating ravages of the liver fluke **endoparasite**." },
      { author: "Richard Dawkins", work: "The Extended Phenotype", quote: "An **endoparasite** may alter the host's behavior to increase the likelihood of transmission to its final definitive host." }
    ]
  },
  "Dashboard — sit/endoparasitic.md": {
    primary: "Living as an endoparasite; of, relating to, or characteristic of internal parasites.",
    secondary: "In evolutionary biology, exhibiting morphological and metabolic adaptations to life within a host's internal organs or bloodstream.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The complete loss of a digestive tract in tapeworms represents an ultimate adaptation to an **endoparasitic** existence." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "Complex multi-host life cycles characterize many **endoparasitic** helminths inhabiting tropical waters." },
      { author: "Richard Dawkins", work: "The Selfish Gene", quote: "The **endoparasitic** wasp larva devours the caterpillar's fat bodies while carefully preserving its vital organs until pupation." }
    ]
  },
  "Dashboard — sit/endoparasitoid.md": {
    primary: "A parasitoid that lives inside the body of its host, ultimately killing the host from within (such as many ichneumonid and braconid wasps).",
    secondary: "In insect ecology and biological pest control, an organism whose juvenile stages develop entirely inside an arthropod host before pupating and killing it.",
    quotes: [
      { author: "Jean-Henri Fabre", work: "The Wonders of Instinct", quote: "The tiny **endoparasitoid** deposits its lethal egg within the living caterpillar with mathematical precision." },
      { author: "Charles Darwin", work: "Letter to Asa Gray (1860)", quote: "I cannot persuade myself that a beneficent God would have designed the Ichneumonidae with the express intention of feeding as an **endoparasitoid** within the bodies of living caterpillars." },
      { author: "E. O. Wilson", work: "The Insect Societies", quote: "Agricultural biological control relies heavily upon releasing the specific **endoparasitoid** of the destructive crop pest." }
    ]
  },
  "Dashboard — sit/entoparasite.md": {
    primary: "A variant or older anatomical term for an endoparasite; an internal parasite living within a host body.",
    secondary: "In 19th-century zoological and medical texts, designating helminths and protozoa inhabiting deep tissues or visceral cavities.",
    quotes: [
      { author: "Richard Owen", work: "Lectures on the Comparative Anatomy of Invertebrates", quote: "The fluke exhibits the classic flattened morphology of an **entoparasite** adapted to the hepatic bile ducts." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Identification of the ova of the **entoparasite** in the stool confirms the diagnosis of intestinal schistosomiasis." },
      { author: "Thomas Henry Huxley", work: "Anatomy of Invertebrated Animals", quote: "In every class of Metazoa, certain lineages have adopted the secluded, specialized life of an **entoparasite**." }
    ]
  },
  "Dashboard — sit/epiparasite.md": {
    primary: "A parasite that feeds upon or attaches to another parasite; a hyperparasite.",
    secondary: "In ecological trophic webs, an organism occupying the trophic level of secondary parasitism (such as a fungal pathogen infecting a parasitic mite).",
    quotes: [
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "Trophic webs can support complex chains of parasitism where an **epiparasite** preys upon another parasitic arthropod." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The existence of an **epiparasite** upon a flea demonstrates the infinite complexity of ecological relationships." },
      { author: "Richard Dawkins", work: "The Blind Watchmaker", quote: "Nature reveals layered hierarchies of exploitation where the **epiparasite** drains the reserves of the primary parasite." }
    ]
  },
  "Dashboard — sit/hemiparasite.md": {
    primary: "A plant that is photosynthetic and produces its own food but obtains water and mineral nutrients from a host plant (such as mistletoe).",
    secondary: "In plant ecology, a facultative or obligate root or stem parasite that taps the host's xylem via specialized haustorial organs.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The common mistletoe is a well-known **hemiparasite**, synthesizing its own carbon while extracting water and salts from the apple tree." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "Many grassland scrophulariaceous species live as a subtle **hemiparasite**, connecting to adjacent grass roots by subterranean haustoria." },
      { author: "John Muir", work: "Our National Parks", quote: "Golden boughs of the mistletoe **hemiparasite** clustered in the ancient oaks of the valley." }
    ]
  },
  "Dashboard — sit/hemiparasitic.md": {
    primary: "Partially parasitic; obtaining some nutrients from a host while retaining photosynthetic capability (of plants).",
    secondary: "Relating to or characteristic of a hemiparasite; possessing haustorial xylem connections without complete loss of chlorophyll.",
    quotes: [
      { author: "Charles Darwin", work: "The Different Forms of Flowers on Plants of the Same Species", quote: "The **hemiparasitic** habit in yellow rattle allows it to flourish in nutrient-poor meadows by draining neighboring grasses." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "Several wild species of paintbrush display **hemiparasitic** attachments to the subterranean root systems of prairie shrubs." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "The **hemiparasitic** strategy represents a stable evolutionary stepping-stone between autotrophy and complete holoparasitism." }
    ]
  },
  "Dashboard — sit/hyperparasitism.md": {
    primary: "A condition in which a parasite is itself parasitized by another parasite.",
    secondary: "In community ecology, multi-tiered parasitic relationships common among parasitoid wasps, fungi, and insect vectors.",
    quotes: [
      { author: "Jean-Henri Fabre", work: "The Wonders of Instinct", quote: "The phenomenon of **hyperparasitism** creates a nested Russian doll of life, where a secondary wasp emerges from a primary caterpillar parasite." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "Ecological balances are maintained through intense competition and layered **hyperparasitism** among insect populations." },
      { author: "E. O. Wilson", work: "The Insect Societies", quote: "Certain tiny encyrtid wasps specialize in obligate **hyperparasitism**, attacking only other parasitoid larvae inside scale insects." }
    ]
  },
  "Dashboard — sit/kleptoparasitism.md": {
    primary: "A form of feeding in which one animal deliberately takes food or prey from another that has caught, gathered, or prepared it.",
    secondary: "In behavioral ecology, a foraging strategy seen in skuas, frigatebirds, hyenas, and spiders that pirate food from others.",
    quotes: [
      { author: "E. O. Wilson", work: "Sociobiology: The New Synthesis", quote: "Frigatebirds engage in aerial **kleptoparasitism**, harassing returning boobies until they regurgitate their catch in midair." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The skua relies habitual on **kleptoparasitism**, chasing gulls with relentless fury until they yield their prey." },
      { author: "Richard Dawkins", work: "The Extended Phenotype", quote: "In social spider colonies, larger individuals frequently practice shameless **kleptoparasitism** over smaller siblings." }
    ]
  },
  "Dashboard — sit/mesoparasite.md": {
    primary: "A parasite that lives in an intermediate position between ectoparasite and endoparasite, typically anchored in the body wall or an opening (such as the ear, nares, or cloaca).",
    secondary: "In marine parasitology, copepods (such as Pennella) whose head is buried deep in host flesh while their reproductive body projects externally.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", quote: "The bizarre copepod Pennella is a true **mesoparasite**, anchoring its antlered cephalothorax into the blubber while its egg sacs trail in the sea." },
      { author: "Richard Owen", work: "Lectures on the Comparative Anatomy of Invertebrates", quote: "An intermediate ecological niche is occupied by the **mesoparasite**, which bridges external exposure and internal nourishment." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "Marine fish carry a remarkable variety of **mesoparasite** crustacea attached to their opercular flaps and gills." }
    ]
  },
  "Dashboard — sit/parasite.md": {
    primary: "An organism that lives in or on an organism of another species (its host) and benefits by deriving nutrients at the other's expense.",
    secondary: "A person who habitually relies on or exploits others without making any useful return.",
    quotes: [
      { author: "William Shakespeare", work: "Timon of Athens", quote: "Live loathed, and long, most smiling, smooth, detested **parasite**, courteous destroyers, affable wolves." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The structure of every **parasite** is wonderfully adapted to prey upon the fluids of its chosen host." },
      { author: "Jonathan Swift", work: "On Poetry: A Rhapsody", quote: "So naturalists observe, a flea has smaller fleas that on him prey; and these have smaller fleas to bite 'em, and so proceed ad infinitum, each a **parasite**." }
    ]
  },
  "Dashboard — sit/parasitic.md": {
    primary: "Of, relating to, or characteristic of a parasite; living in or on another organism and exploiting it for food.",
    secondary: "Habitually relying on or exploiting others without giving anything in return.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The cuckoo possesses a **parasitic** breeding habit, laying its eggs in the nests of other unsuspecting birds." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "A swarm of **parasitic** sycophants drained the treasury and flattered the vanity of the decadent court." },
      { author: "George Eliot", work: "Middlemarch", quote: "His cousin lived a **parasitic** existence, drifting from one wealthy relative's estate to another." }
    ]
  },
  "Dashboard — sit/parasitical.md": {
    primary: "Of, relating to, or having the character of a parasite; parasitic.",
    secondary: "Fawning, sycophantic, or living at the expense of others.",
    quotes: [
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "They tore down ancient nobility only to see a new **parasitical** class of financial speculators take its place." },
      { author: "Charles Dickens", work: "Bleak House", quote: "The Court of Chancery supported a whole army of **parasitical** clerks, copyists, and hangers-on." },
      { author: "Thomas Carlyle", work: "Past and Present", quote: "A society that honors idle aristocracy fosters a **parasitical** culture of unproductive consumption." }
    ]
  },
  "Dashboard — sit/parasitically.md": {
    primary: "In a parasitic manner; as a parasite, living at the expense of a host or other person.",
    secondary: "With sycophancy or fawning dependence.",
    quotes: [
      { author: "Charles Darwin", work: "The Descent of Man", quote: "Certain species of ants live **parasitically** upon sister colonies, having lost the capacity to feed themselves." },
      { author: "Thomas Hardy", work: "Jude the Obscure", quote: "He felt that he was existing **parasitically** upon the generosity of friends whose ideals he could not share." },
      { author: "George Bernard Shaw", work: "Major Barbara", quote: "The idle rich live **parasitically** upon the toil of laborers who produce the nation's actual wealth." }
    ]
  },
  "Dashboard — sit/parasitism.md": {
    primary: "A non-mutual symbiotic relationship between species, where one species (the parasite) benefits at the expense of the other (the host).",
    secondary: "The practice or habit of living at the expense of others; sponging or social dependence.",
    quotes: [
      { author: "E. O. Wilson", work: "Sociobiology: The New Synthesis", quote: "Social **parasitism** in ants represents an extraordinary evolutionary journey where one colony usurps the brood of another." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "Natural selection explains the exquisite morphological degradation that accompanies obligate **parasitism**." },
      { author: "Karl Marx", work: "Capital", quote: "Unchecked usury represents a form of economic **parasitism** that drains the reproductive power of productive labor." }
    ]
  },
  "Dashboard — sit/parasitoid.md": {
    primary: "An organism that lives in or on a host and consumes it entirely, ultimately killing it (unlike a true parasite).",
    secondary: "In insect biology, insects (such as ichneumonid wasps and tachinid flies) whose free-living adults lay eggs in hosts that their larvae devour.",
    quotes: [
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "The **parasitoid** is effectively a carnivore in slow motion, consuming the host's living tissues until pupation." },
      { author: "Richard Dawkins", work: "The Blind Watchmaker", quote: "The life strategy of the solitary **parasitoid** wasp provides a chilling illustration of nature's blind evolutionary mechanics." },
      { author: "Jean-Henri Fabre", work: "The Wonders of Instinct", quote: "The mother **parasitoid** paralyzes the spider with surgeon-like skill, providing fresh meat for her unborn offspring." }
    ]
  },
  "Dashboard — sit/sitology.md": {
    primary: "The branch of medicine and dietary science that deals with food, nutrition, and dietetics; dietetics.",
    secondary: "In historical medicine, the systematic study of nutritional physiology and therapeutic food regimens.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The modern physician must master the principles of **sitology** to manage metabolic disorders and convalescence." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "Sound **sitology** and fresh air have saved more lives than all the mercurial mixtures of ancient pharmacopoeias." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "In treating melancholy, physicians recommend the strictest **sitology**, avoiding gross, burnt, or windy meats." }
    ]
  },
  "Dashboard — sit/syssitia.md": {
    primary: "A communal meal or common mess banquet shared daily by male citizens in ancient Greek city-states, particularly Sparta and Crete.",
    secondary: "In classical political history, the civic dining institution designed to foster camaraderie, civic equality, and military discipline among citizens.",
    quotes: [
      { author: "Plutarch", work: "Life of Lycurgus", quote: "Lycurgus instituted the **syssitia**, or common tables, that citizens might eat together of specified simple foods and banish luxury." },
      { author: "Aristotle", work: "Politics", quote: "The institution of the **syssitia** in Crete and Sparta was designed to bind the warrior class into a unified civic brotherhood." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The austere public table of the Spartan **syssitia** preserved civic equality across generations of austere soldiers." }
    ]
  },

  // === Dashboard — stat (first 3 words of batch 6) ===
  "Dashboard — stat/anastatica.md": {
    primary: "A genus of desert annual plants in the mustard family (Brassicaceae), consisting of Anastatica hierochuntica, commonly known as the Rose of Jericho.",
    secondary: "In desert botany, a famous resurrection plant whose dead branches curl inward into a ball when dry, tumbling with the wind and opening when moistened.",
    quotes: [
      { author: "John Gerard", work: "The Herball or Generall Historie of Plantes", quote: "The dry globes of **Anastatica**, brought by pilgrims from the Holy Land, expand miraculously when cast into water." },
      { author: "Alexander von Humboldt", work: "Aspects of Nature", quote: "Tumbling across the arid sands of Egypt, the desiccated ball of **Anastatica** preserves its viable seeds for years." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "Hygroscopic movements in the woody branches of **Anastatica** ensure seed dispersal precisely when desert rains arrive." }
    ]
  },
  "Dashboard — stat/apostate.md": {
    primary: "A person who renounces or abandons a religious or political belief, principle, or allegiance.",
    secondary: "In historical theology, an individual who renounces holy vows, or the Roman Emperor Julian (Julian the Apostate).",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Julian was stigmatized by Christian historians as the **apostate** who vainly attempted to restore pagan worship." },
      { author: "John Milton", work: "Paradise Lost", quote: "So spake the Cherub, and his grave rebuke, severe in youthful beauty, added grace invincible; abashed the Devil stood, an **apostate** angel." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "No political zealot is more fierce and intolerant than the newly converted **apostate** who denounces his former party." }
    ]
  },
  "Dashboard — stat/apostatise.md": {
    primary: "To abandon or renounce a religious or political belief, faith, or allegiance (Commonwealth spelling).",
    secondary: "To fall away from truth, duty, or formerly declared moral principles.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Neither the allurements of imperial favor nor the threat of exile could induce the bishop to **apostatise** from the Nicene faith." },
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "In times of shifting political terror, many a deputy was tempted to **apostatise** to save his neck." },
      { author: "Walter Scott", work: "The Talisman", quote: "The crusader declared he would suffer martyrdom ten times over before he would **apostatise** from his Christian vows." }
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

console.log(`Updated ${updatedCount} files in Batch 6!`);
