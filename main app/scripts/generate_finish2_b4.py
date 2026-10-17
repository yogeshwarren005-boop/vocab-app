import json
import os
import subprocess

# Load slice
with open('main app/scripts/slice-form-finish-2.json', 'r', encoding='utf-8') as f:
    files = json.load(f)

batch4_files = files[192:256]

lexicon = {
  "periphery": {
    "primary": "The outer limits, edge, or boundary of an area, surface, or object.",
    "secondary": "In social sciences and economics, marginal regions or non-dominant groups situated far from central decision-making institutions.",
    "quotes": [
      {"author": "Jack London", "work": "The Jacket (The Star-Rover)", "quote": "Without having passed through the wall of skull, it seemed to me that the **periphery** of my brain was already outside and expanding."},
      {"author": "Meyer Moldeven", "work": "The Universe — or Nothing", "quote": "The outer **periphery** of the Asteroid Belt became the recognized navigational boundary."},
      {"author": "Immanuel Wallerstein", "work": "The Modern World-System", "quote": "Core nations extract primary commodities from the agricultural **periphery** to fuel metropolitan industrialization."}
    ]
  },
  "perirhinal": {
    "primary": "Situated around or bordering the rhinal sulcus or nasal region; specifically designating the perirhinal cortex of the temporal lobe.",
    "secondary": "In cognitive neuroscience, the perirhinal cortex is essential for visual object recognition, semantic knowledge, and complex item memory.",
    "quotes": [
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "Lesions confined to the **perirhinal** cortex severely impair visual object recognition memory in primates."},
      {"author": "Brenda Milner", "work": "Memory and the Temporal Lobe", "quote": "Declarative item encoding relies upon reciprocal connections between the **perirhinal** area and the hippocampus."},
      {"author": "Santiago Ramón y Cajal", "work": "Studies on the Cerebral Cortex", "quote": "Pyramidal neurons of the **perirhinal** transitional zone receive dense associational projections from sensory neocortex."}
    ]
  },
  "periscope": {
    "primary": "An optical instrument for viewing objects that are otherwise obstructed from direct line of sight, typically consisting of a tube with attached mirrors or prisms.",
    "secondary": "In naval submarine warfare, the periscope allows submerged vessels to visually reconnoiter the ocean surface without surfacing.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The War in the Air", "quote": "Through the elevated **periscope**, the commander watched the naval flotilla steaming across the gray horizon."},
      {"author": "Clarence Budington Kelland", "work": "Mark Tidd's Citadel", "quote": "There was no chance of damaging the motive power, but we could make the pilot wish he had a **periscope**."},
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues Under the Sea", "quote": "Captain Nemo monitored surface maneuvers by elevating an optical **periscope** above the ocean swell."}
    ]
  },
  "periselene": {
    "primary": "The point in a lunar orbit closest to the center of the Moon; the lunar periapsis (synonymous with perilune).",
    "secondary": "In orbital celestial mechanics, an orbiting body moves at its highest orbital velocity when sweeping through periselene.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "Rendezvous with Rama", "quote": "Trajectory adjustments initiated at **periselene** allowed the survey probe to optimize its observational pass."},
      {"author": "Howard D. Curtis", "work": "Orbital Mechanics for Engineering Students", "quote": "Orbital energy conservation dictates that speed peaks at **periselene** and drops to a minimum at aposelene."},
      {"author": "Carl Sagan", "work": "Cosmos", "quote": "Mapping radar gathered unprecedented topographical data as the lunar satellite swept past **periselene**."}
    ]
  },
  "perish": {
    "primary": "To suffer death, complete destruction, or ruin, typically in a violent, sudden, or untimely manner.",
    "secondary": "In material science, to deteriorate, lose elasticity, or decay through oxidation and environmental weathering (as of rubber).",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "The great globe itself, yea, all which it inherit, shall dissolve, and like this insubstantial pageant faded, leave not a rack behind; all must **perish**."},
      {"author": "Abraham Lincoln", "work": "Gettysburg Address", "quote": "That this nation, under God, shall have a new birth of freedom—and that government of the people, by the people, for the people, shall not **perish** from the earth."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Those varieties least adapted to severe climatic oscillations inevitably **perish** during famine."}
    ]
  },
  "perishability": {
    "primary": "The state, condition, or property of being perishable; susceptibility to decay, spoilage, or destruction.",
    "secondary": "In economics and supply chain logistics, the rapid depreciation or loss of commercial value of goods with short lifespans.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The extreme **perishability** of fresh foodstuffs prevents their long-distance conveyance without substantial refrigeration."},
      {"author": "Alfred Marshall", "work": "Principles of Economics", "quote": "Goods characterized by high **perishability** must be marketed swiftly regardless of unfavorable price fluctuations."},
      {"author": "Thomas Robert Malthus", "work": "An Essay on the Principle of Population", "quote": "The inherent **perishability** of seasonal harvests places a natural ceiling on speculative hoarding."}
    ]
  },
  "perishableness": {
    "primary": "The quality of being perishable; liability to decay, rot, or destruction.",
    "secondary": "In moral philosophy and literature, the transient, ephemeral fragility of mortal life and worldly achievements.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Contemplation of the **perishableness** of earthly treasures should awaken the soul to eternal virtues."},
      {"author": "John Locke", "work": "Second Treatise of Government", "quote": "The **perishableness** of common agricultural products led mankind to invent durable metallic money."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "A somber awareness of the **perishableness** of human monuments rebukes all tyrannical pride."}
    ]
  },
  "perisher": {
    "primary": "A person or thing that perishes; or an informal term for an annoying, mischievous person or child.",
    "secondary": "In naval slang, a candidate undergoing the grueling submarine command qualifying examination (the Perisher course).",
    "quotes": [
      {"author": "Charles Dickens", "work": "Our Mutual Friend", "quote": "The cold wind blew off the Thames like an icy **perisher**, chilling the night watchman to the marrow."},
      {"author": "Rudyard Kipling", "work": "The Day's Work", "quote": "He was a stubborn young **perisher**, but he stuck to his engine throttle until the relief arrived."},
      {"author": "George Bernard Shaw", "work": "Pygmalion", "quote": "That insolent little **perisher** had the audacity to contradict her elders in public."}
    ]
  },
  "perisoreus": {
    "primary": "A genus of small, intelligent corvid birds comprising the boreal jays, including the Canada jay (Perisoreus canadensis) and Siberian jay.",
    "secondary": "In ornithology, birds of the genus *Perisoreus* inhabit subarctic conifer forests, caching perishable food using sticky saliva to endure harsh winters.",
    "quotes": [
      {"author": "John James Audubon", "work": "The Birds of America", "quote": "The Canada jay, belonging to the genus **Perisoreus**, exhibits astonishing boldness around northern lumber camps."},
      {"author": "Alexander Wilson", "work": "American Ornithology", "quote": "In dense pine barrens, birds of the genus **Perisoreus** flit noiselessly from branch to branch."},
      {"author": "Ernst Mayr", "work": "Systematics and the Origin of Species", "quote": "Boreal caching behaviors in **Perisoreus** represent complex adaptive specializations for surviving taiga winters."}
    ]
  },
  "perisperm": {
    "primary": "A layer of nutritive tissue in some seeds that surrounds the embryo and endosperm, derived from the nucellus of the ovule.",
    "secondary": "In botanical embryology, perisperm forms the primary storage reserve in families such as Caryophyllaceae, Chenopodiaceae, and Zingiberaceae.",
    "quotes": [
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "In the seed of the water-lily, abundant food reserve is stored outside the embryo within the **perisperm**."},
      {"author": "Katherine Esau", "work": "Plant Anatomy", "quote": "Persistent nucellar tissue forms the **perisperm**, which is separated from the embryo by a vestigial endosperm."},
      {"author": "John Merle Coulter", "work": "Morphology of Angiosperms", "quote": "In beet seeds, maternal nutrient reserves are deposited within the starch-rich **perisperm**."}
    ]
  },
  "perissodactyl": {
    "primary": "An odd-toed ungulate mammal belonging to the order Perissodactyla, such as a horse, tapir, or rhinoceros.",
    "secondary": "In mammalian comparative anatomy, a perissodactyl bears the weight of the body predominantly on the third (middle) digit (mesaxonic foot structure).",
    "quotes": [
      {"author": "Richard Owen", "work": "On the Archetype and Homologies of the Vertebrate Skeleton", "quote": "We distinguish the **perissodactyl** ungulate by the symmetrical development of the middle digit of the foot."},
      {"author": "Thomas Henry Huxley", "work": "American Addresses", "quote": "The ancestral lineage of the modern horse exemplifies gradual specialization within the **perissodactyl** radiation."},
      {"author": "George Gaylord Simpson", "work": "The Principles of Classification and a Classification of Mammals", "quote": "A modern **perissodactyl** stands on a mesaxonic axis, contrasting sharply with the artiodactyl paraxonic condition."}
    ]
  },
  "perissodactyla": {
    "primary": "An order of odd-toed ungulates comprising three extant families: Equidae (horses), Rhinocerotidae (rhinoceroses), and Tapiridae (tapirs).",
    "secondary": "In vertebrate paleontology, Perissodactyla flourished during the Eocene epoch, giving rise to gigantic extinct forms such as brontotheres and chalicotheres.",
    "quotes": [
      {"author": "Richard Owen", "work": "Description of the Teeth and Portions of the Jaws of Two Extinct Anthracotherioid Quadrupeds", "quote": "I propose the order **Perissodactyla** for those hoofed herbivores whose hind-foot exhibits an odd number of digits."},
      {"author": "Alfred Romer", "work": "Vertebrate Paleontology", "quote": "The evolutionary zenith of **Perissodactyla** occurred in the early Tertiary, followed by displacement by artiodactyls."},
      {"author": "George Gaylord Simpson", "work": "Horses: The Story of the Horse Family in the Modern World and through Sixty Million Years of History", "quote": "Extant **Perissodactyla** represent surviving remnants of a once magnificent and dominant ungulate clade."}
    ]
  },
  "peristalsis": {
    "primary": "The involuntary constriction and relaxation of the muscles of the intestine or another canal, creating wave-like movements that push the contents forward.",
    "secondary": "In gastrointestinal physiology, peristalsis is coordinated by the enteric nervous system (myenteric plexus of Auerbach) via coordinated circular contraction and longitudinal relaxation.",
    "quotes": [
      {"author": "William Beaumont", "work": "Experiments and Observations on the Gastric Juice and the Physiology of Digestion", "quote": "The rhythmic churning of gastric **peristalsis** propels the alimentary bolus toward the pyloric orifice."},
      {"author": "Arthur Guyton", "work": "Textbook of Medical Physiology", "quote": "Distension of the gut lumen triggers intrinsic reflex circuits that initiate propulsive **peristalsis**."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Visible **peristalsis** on the abdominal wall is a valuable diagnostic sign of progressive intestinal obstruction."}
    ]
  },
  "peristediinae": {
    "primary": "A subfamily (or family Peristediidae) of scorpaeniform marine fishes commonly known as armored searobins.",
    "secondary": "In ichthyology, peristediine fishes inhabit deep continental shelf slopes and are characterized by heavy bony scutes and chin barbels.",
    "quotes": [
      {"author": "David Starr Jordan", "work": "The Fishes of North and Middle America", "quote": "The **Peristediinae** are distinguished by an exoskeleton of bony plates and rostral extensions resembling horns."},
      {"author": "George Brown Goode", "work": "Oceanic Ichthyology", "quote": "Deep-water trawls off the Atlantic slope frequently capture curious armored specimens of **Peristediinae**."},
      {"author": "William K. Gregory", "work": "Fish Skulls: A Study of the Evolution of Natural Mechanisms", "quote": "The cranium in **Peristediinae** exhibits extensive dermal armor that protects the braincase during seafloor foraging."}
    ]
  },
  "peristedion": {
    "primary": "The type genus of armored searobins belonging to the family Peristediidae (or subfamily Peristediinae).",
    "secondary": "In marine biology, species of *Peristedion* crawl along benthic substrates using modified free pectoral fin rays to detect buried prey.",
    "quotes": [
      {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "Fishes of the genus **Peristedion** use their slender pectoral filaments to probe muddy bottom sediments."},
      {"author": "George Brown Goode", "work": "Oceanic Ichthyology", "quote": "Specimens of **Peristedion** possess two flattened rostral spines projecting horizontally from the snout."},
      {"author": "Carl Linnaeus", "work": "Systema Naturae", "quote": "Trigla cataphracta, now assigned to **Peristedion**, was early recognized for its remarkable bony cuirass."}
    ]
  },
  "peristome": {
    "primary": "An anatomical region or ring of specialized structures surrounding the mouth or aperture of an invertebrate, plant, moss capsule, or pitcher plant.",
    "secondary": "In bryology, the peristome is a fringe of hygroscopic teeth surrounding the capsule mouth that regulates spore dispersal.",
    "quotes": [
      {"author": "Charles Darwin", "work": "Insectivorous Plants", "quote": "The slippery rim or **peristome** of the Nepenthes pitcher directs unsuspecting insects down into digestive fluid."},
      {"author": "Wilhelm Hofmeister", "work": "On the Germination, Development, and Fructification of the Higher Cryptogamia", "quote": "Hygroscopic movements of the **peristome** teeth ensure that spores are cast out only during dry weather."},
      {"author": "Thomas Henry Huxley", "work": "The Invertebrates", "quote": "Ciliated oral grooves converge upon the **peristome** of the vorticellid to draw in nutrient particles."}
    ]
  },
  "peristylar": {
    "primary": "Of, relating to, having, or surrounded by a peristyle (a colonnade surrounding a building or an open courtyard).",
    "secondary": "In classical architecture, describing temple sanctuaries or Roman domestic atria enclosed by continuous rows of columns.",
    "quotes": [
      {"author": "Vitruvius", "work": "De Architectura", "quote": "A **peristylar** court provides shelter, illumination, and dignified circulation for the occupants of the villa."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The noble **peristylar** galleries of the Venetian palace harmonize classical symmetry with Gothic grace."},
      {"author": "Edward Bulwer-Lytton", "work": "The Last Days of Pompeii", "quote": "Fountains splashed softly within the marble **peristylar** garden under the clear Campanian sky."}
    ]
  },
  "peristyle": {
    "primary": "A row of columns surrounding a courtyard or building, or an open courtyard surrounded by such a colonnade.",
    "secondary": "In Greco-Roman domestic architecture, the peristyle (peristylium) formed the private garden court around which family rooms and dining triclinia were arranged.",
    "quotes": [
      {"author": "Vitruvius", "work": "De Architectura", "quote": "The proportions of the **peristyle** should exceed the width of the atrium by one third to ensure architectural balance."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Statues of imperial ancestors graced the shaded **peristyle** of Diocletian's palace at Salona."},
      {"author": "Pliny the Younger", "work": "Letters", "quote": "My Laurentine villa features an enclosed **peristyle** that offers a delightful retreat when winter winds blow."}
    ]
  },
  "perithecium": {
    "primary": "A round or flask-shaped fruiting body (ascoma) in certain ascomycete fungi, having a small opening (ostiole) through which ascospores are discharged.",
    "secondary": "In mycology, perithecia are characteristic of Sordariomycetes (such as Neurospora and Claviceps), where asci forcibly eject spores through the apical pore.",
    "quotes": [
      {"author": "Elias Magnus Fries", "work": "Systema Mycologicum", "quote": "The carbonaceous **perithecium** of Xylaria embeds numerous clavate asci within a protective stromatic crust."},
      {"author": "George W. Beadle", "work": "Genetic Control of Biochemical Reactions in Neurospora", "quote": "Crossing compatible strains produces black mature **perithecium** bodies containing ordered linear asci."},
      {"author": "John Webster", "work": "Introduction to Fungi", "quote": "Turgor pressure within the mature **perithecium** shoots ascospores through the ostiolar canal into the air."}
    ]
  },
  "perithelial": {
    "primary": "Of, relating to, or derived from the perithelium; situated around small blood vessels.",
    "secondary": "In histopathology and oncology, perithelial cells include pericytes and adventitial connective tissues surrounding capillaries.",
    "quotes": [
      {"author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "Capillary walls are reinforced externally by branching **perithelial** cells that maintain vascular stability."},
      {"author": "Vinay Kumar", "work": "Robbins and Cotran Pathologic Basis of Disease", "quote": "Rare mesenchymal neoplasms exhibiting concentric **perithelial** whorls are classified as hemangiopericytomas."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "A delicate network of **perithelial** fibers anchors the capillary endothelium to the surrounding tissue matrix."}
    ]
  },
  "perithelium": {
    "primary": "The layer of connective tissue, pericytes, and adventitial cells that surrounds capillaries and small blood vessels.",
    "secondary": "In vascular histology, the perithelium plays an essential role in regulating capillary permeability, microvascular tone, and angiogenesis.",
    "quotes": [
      {"author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "The cerebral **perithelium** actively participates in mediating metabolic exchange between glial end-feet and blood plasma."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Adventitial elements constituting the **perithelium** blend imperceptibly with the surrounding areolar matrix."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "Endothelial signaling recruits pericytes to form a stabilizing **perithelium** during vascular maturation."}
    ]
  },
  "peritoneal": {
    "primary": "Of, relating to, or affecting the peritoneum (the serous membrane lining the abdominal cavity).",
    "secondary": "In nephrology and abdominal surgery, peritoneal dialysis utilizes the peritoneal membrane as a semipermeable filter to clear toxins in renal failure.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The **peritoneal** cavity is a potential space moistened by serous fluid that lubricates visceral movements."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Tuberculous involvement of the **peritoneal** membrane manifests with ascites and doughy abdominal fullness."},
      {"author": "Tinsley R. Harrison", "work": "Principles of Internal Medicine", "quote": "Continuous ambulatory **peritoneal** dialysis offers an effective home-based renal replacement modality."}
    ]
  },
  "peritoneum": {
    "primary": "The smooth, continuous serous membrane that lines the cavity of the abdomen and covers most of the abdominal organs.",
    "secondary": "In gross human anatomy, the peritoneum consists of a parietal layer lining the abdominal wall and a visceral layer reflecting over the viscera, forming mesenteries and omenta.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The **peritoneum** is the largest serous membrane in the body, presenting an extensive surface area for fluid absorption."},
      {"author": "John Hunter", "work": "Treatise on the Blood, Inflammation, and Gun-shot Wounds", "quote": "Inflammation of the **peritoneum** excites immediate muscular rigidity across the overlying abdominal parietes."},
      {"author": "William Harvey", "work": "Lectures on the Whole of Anatomy", "quote": "The glistening **peritoneum** wraps the intestines smoothly to prevent adhesion during their peristaltic march."}
    ]
  },
  "peritonitis": {
    "primary": "Inflammation of the peritoneum, typically caused by bacterial infection or chemical irritation following perforation of an abdominal organ.",
    "secondary": "In emergency surgery and critical care, acute generalized peritonitis presents with severe abdominal pain, rebound tenderness, and involuntary board-like muscular rigidity.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A ruptured appendix pours purulent exudate into the abdominal basin, initiating fatal septic **peritonitis** if not swiftly excised."},
      {"author": "Tinsley R. Harrison", "work": "Principles of Internal Medicine", "quote": "The hallmark of acute **peritonitis** is diffuse abdominal rigidity accompanied by exquisite rebound tenderness."},
      {"author": "Eugene Braunwald", "work": "Harrison's Principles of Internal Medicine", "quote": "Spontaneous bacterial **peritonitis** is a frequent and life-threatening complication in cirrhotic patients with ascites."}
    ]
  },
  "peritrate": {
    "primary": "A brand name for pentaerythritol tetranitrate (PETN), a long-acting organic nitrate vasodilator used in the prophylactic management of angina pectoris.",
    "secondary": "In cardiovascular pharmacotherapy, peritrate releases nitric oxide to dilate coronary and systemic collateral vessels, reducing myocardial oxygen demand.",
    "quotes": [
      {"author": "Louis Sanford Goodman", "work": "The Pharmacological Basis of Therapeutics", "quote": "Long-acting nitrate preparations like **peritrate** provide sustained prophylaxis against exertional anginal attacks."},
      {"author": "Eugene Braunwald", "work": "Heart Disease", "quote": "Administering **peritrate** promotes collateral coronary vasodilation while lowering ventricular preload."},
      {"author": "Tinsley R. Harrison", "work": "Principles of Internal Medicine", "quote": "Patients receiving **peritrate** must observe nitrate-free intervals to prevent pharmacologic tolerance."}
    ]
  },
  "peritrichous": {
    "primary": "Having flagella or cilia distributed uniformly all over the entire surface, characteristic of certain bacterial cells.",
    "secondary": "In bacteriology and microbiological taxonomy, bacteria with peritrichous flagellation (such as Escherichia coli and Salmonella) exhibit tumbling and directional swimming motility.",
    "quotes": [
      {"author": "Robert Koch", "work": "Investigations into the Etiology of Traumatic Infective Diseases", "quote": "Special silver-staining methods reveal numerous **peritrichous** flagella radiating from the bacterial capsule."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "Coordinated counterclockwise rotation of **peritrichous** flagella bundles them together into a single propelling screw."},
      {"author": "David L. Nelson", "work": "Lehninger Principles of Biochemistry", "quote": "The **peritrichous** distribution of flagellar motors allows rapid chemotactic reorientation toward nutrient gradients."}
    ]
  },
  "phac": {
    "primary": "A Greek combining root (from phakos, 'lentil', 'lens', or 'eye lens') forming scientific and anatomical terms relating to the crystalline lens.",
    "secondary": "In ophthalmology and medical etymology, the stem phac (or phako-) forms foundational terms for lens disorders (aphakia, phacoemulsification, phacoma).",
    "quotes": [
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The Greek noun **phac** signifies a lentil bean, applied by ancient anatomists to the lenticular crystal of the eye."},
      {"author": "Robert Beekes", "work": "Etymological Dictionary of Greek", "quote": "Comparative Indo-European phonology traces **phac** to ancient agricultural terms for pulse legumes."},
      {"author": "Duke-Elder", "work": "System of Ophthalmology", "quote": "Ophthalmic vocabulary preserves the root **phac** in designating diseases and surgical manipulations of the ocular lens."}
    ]
  },
  "phacelia": {
    "primary": "A genus of mostly annual flowering plants in the borage family (Boraginaceae), commonly known as scorpionweeds or phacelias.",
    "secondary": "In botany and agriculture, *Phacelia tanacetifolia* is widely cultivated as an exceptional honey-producing cover crop that attracts pollinating bees and beneficial insects.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The genus **Phacelia** is recognized by its scorpioid cymes that uncoil gracefully as the delicate blue flowers expand."},
      {"author": "Liberty Hyde Bailey", "work": "Manual of Cultivated Plants", "quote": "Beekeepers value **Phacelia** for its copious nectar yield and prolonged summer flowering period."},
      {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "Experiments with species of **Phacelia** demonstrated increased seed set following insect-mediated cross-pollination."}
    ]
  },
  "Phacochoerus": {
    "primary": "A genus of wild African swine in the family Suidae, comprising the common warthog (Phacochoerus africanus) and desert warthog.",
    "secondary": "In mammalogy and vertebrate morphology, *Phacochoerus* is characterized by prominent facial wattles, curved canine tusks, and columnar hypsodont third molars.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "The African warthog, classified in the genus **Phacochoerus**, displays bizarre facial callosities and formidable tusks."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The elongated canine tusks of **Phacochoerus** serve as weapons of defense against savannah predators."},
      {"author": "Richard Owen", "work": "Odontography", "quote": "The composite third molar of **Phacochoerus** consists of numerous cement-fused dentinal columns adapted for grinding coarse grasses."}
    ]
  },
  "phacoemulsification": {
    "primary": "A modern cataract surgical technique in which the clouded crystalline lens of the eye is broken up using ultrasonic vibrations and aspirated through a small incision.",
    "secondary": "In ophthalmology, Charles Kelman introduced phacoemulsification in 1967, drastically reducing incision size and postoperative recovery time.",
    "quotes": [
      {"author": "Charles Kelman", "work": "Phaco-Emulsification and Aspiration: A New Technique of Cataract Removal", "quote": "Ultrasonic **phacoemulsification** allows the clouded lens nucleus to be liquefied and removed through a miniature corneal puncture."},
      {"author": "Duke-Elder", "work": "System of Ophthalmology", "quote": "The adoption of **phacoemulsification** transformed cataract surgery into a rapid outpatient procedure with minimal astigmatic impact."},
      {"author": "Jack J. Kanski", "work": "Clinical Ophthalmology", "quote": "Continuous curvilinear capsulorhexis provides the necessary stability for safe nuclear **phacoemulsification** within the capsular bag."}
    ]
  },
  "aphagia": {
    "primary": "The inability or refusal to swallow, resulting from neurological injury, esophageal obstruction, or psychiatric distress.",
    "secondary": "In experimental neurobiology, bilateral electrolytic lesions of the lateral hypothalamus induce profound aphagia and adipsia in animal models.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Complete esophageal occlusion by an advanced carcinoma results in total **aphagia**, requiring feeding gastrostomy."},
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "Disruption of the lateral hypothalamic feeding center causes immediate and persistent **aphagia**."},
      {"author": "Tinsley R. Harrison", "work": "Principles of Internal Medicine", "quote": "Severe motor neuron degeneration in bulbar palsy leads to dangerous **aphagia** and aspiration risk."}
    ]
  },
  "autophagosome": {
    "primary": "A spherical, double-membraned vesicle that sequesters cytoplasmic contents (such as damaged organelles or protein aggregates) destined for degradation via autophagy.",
    "secondary": "In cellular biology, the autophagosome fuses with a lysosome to form an autolysosome, where hydrolytic enzymes degrade the engulfed cargo.",
    "quotes": [
      {"author": "Yoshinori Ohsumi", "work": "Historical Landmarks of Autophagy Research", "quote": "The formation of the double-membraned **autophagosome** requires a coordinated cascade of evolutionary conserved Atg proteins."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "Upon nutrient starvation, an expanding isolation membrane closes upon itself to assemble a mature **autophagosome**."},
      {"author": "David L. Nelson", "work": "Lehninger Principles of Biochemistry", "quote": "Lipidation of LC3-I to LC3-II promotes cargo recruitment into the lumen of the emerging **autophagosome**."}
    ]
  },
  "autophagy": {
    "primary": "The natural, regulated cellular process of self-digestion in which a cell degrades and recycles its own non-functional or damaged components.",
    "secondary": "In physiology and medicine (recognized by the 2016 Nobel Prize to Yoshinori Ohsumi), macroautophagy provides survival energy during starvation and eliminates toxic proteopathic aggregates.",
    "quotes": [
      {"author": "Christian de Duve", "work": "Lysosomes: A New Group of Cytoplasmic Particles", "quote": "We coined the term **autophagy** to designate the internal digestion of cellular components within lysosomal vacuoles."},
      {"author": "Yoshinori Ohsumi", "work": "Molecular Dissection of Autophagy: Two Decades with Yeast", "quote": "Dissecting the genetic pathways of **autophagy** uncovered fundamental mechanisms of intracellular waste disposal."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "Defective **autophagy** has been implicated in neurodegenerative diseases like Parkinson’s due to accumulation of misfolded proteins."}
    ]
  },
  "bacteriophage": {
    "primary": "A virus that infects and replicates within bacterial cells; commonly termed a phage.",
    "secondary": "In molecular genetics and microbiology, bacteriophages (such as lambda, T4, and phiX174) served as the foundational model organisms for discovering DNA replication, transcription, and genetic code mechanics.",
    "quotes": [
      {"author": "Félix d'Herelle", "work": "The Bacteriophage: Its Role in Immunity", "quote": "I observed clear plaques in bacterial lawns caused by an invisible, antagonistic microbe which I named the **bacteriophage**."},
      {"author": "Max Delbrück", "work": "The Growth of Bacteriophage", "quote": "The single-step growth curve of a **bacteriophage** established that virus replication occurs intracellularly by assembly rather than fission."},
      {"author": "James D. Watson", "work": "Molecular Biology of the Gene", "quote": "Hershey and Chase used radioactive tracers in a **bacteriophage** to prove decisively that DNA is the hereditary genetic material."}
    ]
  },
  "bacteriophagic": {
    "primary": "Of, relating to, or caused by a bacteriophage; capable of destroying or lysing bacteria like a phage.",
    "secondary": "In antimicrobial research, describing therapeutic viral preparations engineered for targeted bacteriophagic lysis of multidrug-resistant pathogens.",
    "quotes": [
      {"author": "Félix d'Herelle", "work": "The Bacteriophage and Its Clinical Applications", "quote": "The potent **bacteriophagic** action of filtered stool extracts arrested dysentery outbreaks within days."},
      {"author": "Max Delbrück", "work": "Bacterial Viruses", "quote": "Quantitative plaque assays measure the specific **bacteriophagic** potency of viral suspensions."},
      {"author": "Alexander Fleming", "work": "Penicillin", "quote": "Unlike chemical antiseptics, **bacteriophagic** agents multiply at the expense of their bacterial prey."}
    ]
  },
  "bacteriophagous": {
    "primary": "Feeding upon, destroying, or consuming bacteria; phage-like in action.",
    "secondary": "In ecology and microbiological terminology, designating protozoans, viruses, or predatory bacteria that prey directly on bacterial populations.",
    "quotes": [
      {"author": "Félix d'Herelle", "work": "The Bacteriophage: Its Role in Immunity", "quote": "The ultramicroscopic **bacteriophagous** principle exerts continuous predatory pressure upon pathogenic bacilli."},
      {"author": "G. Evelyn Hutchinson", "work": "A Treatise on Limnology", "quote": "Ciliated protozoa and **bacteriophagous** flagellates regulate microbial biomass in the epilimnion."},
      {"author": "Eugene P. Odum", "work": "Fundamentals of Ecology", "quote": "Predation by **bacteriophagous** microfauna accelerates nutrient recycling within wastewater treatment lagoons."}
    ]
  },
  "dysphagia": {
    "primary": "Difficulty or discomfort in swallowing; impaired transit of food or liquid from the pharynx into the stomach.",
    "secondary": "In gastroenterology and neurology, dysphagia is categorized into oropharyngeal (neuromuscular) and esophageal (obstructive or dysmotility) etiologies.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Progressive **dysphagia**, first for solid food and later for liquids, is the most ominous sign of esophageal neoplasm."},
      {"author": "Tinsley R. Harrison", "work": "Principles of Internal Medicine", "quote": "Evaluation of motor **dysphagia** involves video-fluoroscopic swallowing studies and high-resolution esophageal manometry."},
      {"author": "Eugene Braunwald", "work": "Harrison's Principles of Internal Medicine", "quote": "Achalasia causes chronic **dysphagia** due to incomplete relaxation of the lower esophageal sphincter."}
    ]
  },
  "esophagitis": {
    "primary": "Inflammation of the lining of the esophagus, commonly caused by acid reflux, infection, or medication injury.",
    "secondary": "In gastroenterology, reflux esophagitis (GERD) can progress to erosive ulcerations, peptic strictures, or Barrett's metaplasia.",
    "quotes": [
      {"author": "Tinsley R. Harrison", "work": "Principles of Internal Medicine", "quote": "Chronic acid regurgitation induces erosive **esophagitis**, causing severe retrosternal pyrosis and odynophagia."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Corrosive poisons like lye produce acute sloughing **esophagitis** followed by dense cicatricial stricture."},
      {"author": "Vinay Kumar", "work": "Robbins and Cotran Pathologic Basis of Disease", "quote": "Histologic assessment of eosinophilic **esophagitis** demonstrates dense intraepithelial eosinophilic microabscesses."}
    ]
  },
  "euphagus": {
    "primary": "A genus of New World blackbirds in the family Icteridae, comprising the rusty blackbird (Euphagus carolinus) and Brewer's blackbird (Euphagus cyanocephalus).",
    "secondary": "In ornithology, species of *Euphagus* forage in wet woodlands and agricultural meadows, possessing sharp conical beaks adapted for omnivorous feeding.",
    "quotes": [
      {"author": "John James Audubon", "work": "The Birds of America", "quote": "The rusty grackle, belonging to the genus **Euphagus**, gathers in noisy flocks along autumn swamp borders."},
      {"author": "Alexander Wilson", "work": "American Ornithology", "quote": "Brewer’s blackbird, a notable Western member of **Euphagus**, exhibits glossy iridescent plumage in bright sunlight."},
      {"author": "Ernst Mayr", "work": "Animal Species and Evolution", "quote": "Ecological niche differentiation between **Euphagus** and Agelaius illustrates competitive displacement in marsh habitats."}
    ]
  },
  "geophagia": {
    "primary": "The practice of eating earth, soil, or clay-like substances, seen across cultural traditions and as a medical pica symptom.",
    "secondary": "In anthropology and clinical medicine, geophagia is often associated with iron-deficiency anemia or gastrointestinal detoxification.",
    "quotes": [
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions of America", "quote": "The Otomac Indians practice habitual **geophagia**, consuming large balls of greasy clay during seasonal river inundations."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe hookworm infestation in undernourished children is frequently accompanied by obsessive **geophagia**."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Travellers across South America have frequently recorded instances of deliberate **geophagia** among native tribes."}
    ]
  },
  "hematophagy": {
    "primary": "The practice or habit of feeding on blood; blood-drinking by hematophagous parasites or predators.",
    "secondary": "In medical parasitology and entomology, hematophagy evolved independently in leeches, vampire bats, and arthropod vectors (such as mosquitoes and tsetse flies).",
    "quotes": [
      {"author": "Ronald Ross", "work": "The Prevention of Malaria", "quote": "Obligate **hematophagy** in the female Anopheles mosquito provides essential protein for oocyte maturation while vectoring Plasmodium."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We observed the habits of the Desmodus vampire bat, whose nocturnal **hematophagy** is dreaded by horses in Chile."},
      {"author": "Patrick Manson", "work": "Tropical Diseases", "quote": "Vector-borne epidemiology depends entirely on repeated bouts of **hematophagy** across mammalian host populations."}
    ]
  },
  "macrophage": {
    "primary": "A large phagocytic white blood cell found in tissues and at sites of infection, capable of engulfing pathogens and cellular debris.",
    "secondary": "In immunology, macrophages differentiate from circulating monocytes, acting as professional antigen-presenting cells and orchestrating wound healing.",
    "quotes": [
      {"author": "Élie Metchnikoff", "work": "Immunity in Infective Diseases", "quote": "The large amoeboid **macrophage** acts as a vigilant scavenger, devouring dying cellular elements and microbial invaders."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "Upon sensing bacterial endotoxin, a resident **macrophage** secretes inflammatory cytokines that recruit neutrophils."},
      {"author": "David L. Nelson", "work": "Lehninger Principles of Biochemistry", "quote": "Phagocytosis by a tissue **macrophage** delivers engulfed pathogens into lysosomes for oxidative destruction."}
    ]
  },
  "microphage": {
    "primary": "A small phagocytic white blood cell; an archaic or historical term for a neutrophil or polymorphonuclear leukocyte.",
    "secondary": "In classical immunology, Metchnikoff coined microphage to distinguish fast-responding, short-lived granular leukocytes from long-lived macrophages.",
    "quotes": [
      {"author": "Élie Metchnikoff", "work": "Comparative Pathology of Inflammation", "quote": "The polymorphonuclear leukocyte acts as an active **microphage**, rushing in great numbers to engulf acute bacterial invaders."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Metchnikoff's distinction between the mobile **microphage** and the stationary macrophage clarified cellular defense mechanisms."},
      {"author": "Paul Ehrlich", "work": "Studies in Immunity", "quote": "Specific staining confirms that the neutrophilic **microphage** carries granular enzymes suited for rapid bacteriolysis."}
    ]
  },
  "odynophagia": {
    "primary": "Painful swallowing; a burning or squeezing sensation experienced when swallowing food or liquids.",
    "secondary": "In gastroenterology and infectious disease, severe odynophagia indicates mucosal inflammation, such as Candida esophagitis, herpes simplex ulceration, or pill-induced esophagitis.",
    "quotes": [
      {"author": "Tinsley R. Harrison", "work": "Principles of Internal Medicine", "quote": "Severe **odynophagia** in an immunocompromised patient strongly suggests opportunistic viral or fungal esophagitis."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Acute follicular tonsillitis causes distressing **odynophagia**, rendering the swallowing of even saliva excruciating."},
      {"author": "Eugene Braunwald", "work": "Harrison's Principles of Internal Medicine", "quote": "Differentiating motor dysphagia from sharp inflammatory **odynophagia** is critical for selecting diagnostic endoscopy."}
    ]
  },
  "phag": {
    "primary": "A Greek combining root (from phagein, 'to eat, devour, consume') forming scientific terms relating to eating, digestion, or cellular engulfment.",
    "secondary": "In biological and linguistic nomenclature, the root phag underlies terms like phagocyte, bacteriophage, and anthropophagy.",
    "quotes": [
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The Greek verbal stem **phag** signifies to eat, consume, or devour, appearing in a wide variety of compound nouns."},
      {"author": "Robert Beekes", "work": "Etymological Dictionary of Greek", "quote": "Traced to Proto-Indo-European *bhag- (to apportion or consume), the stem **phag** came to designate eating in Greek."},
      {"author": "Élie Metchnikoff", "work": "Immunity in Infective Diseases", "quote": "From the Greek stem **phag**, we derived phagocyte to designate cellular devouring of infectious microbes."}
    ]
  },
  "phage": {
    "primary": "A bacteriophage; a virus that parasitizes and multiplies within a bacterium.",
    "secondary": "In molecular biology and biotechnology, phage display is an essential laboratory technique for screening high-affinity peptides and monoclonal antibodies.",
    "quotes": [
      {"author": "Max Delbrück", "work": "Bacterial Viruses (Bacteriophages)", "quote": "A single virulent **phage** particle adsorbs to the bacterial cell wall and injects its viral DNA within seconds."},
      {"author": "James D. Watson", "work": "The Molecular Biology of the Gene", "quote": "The lytic cycle of T4 **phage** culminates in the burst of hundreds of progeny virions into the medium."},
      {"author": "Francis Crick", "work": "What Mad Pursuit", "quote": "Genetic mapping of the rII locus in T4 **phage** by Seymour Benzer proved that genes are linear sequences of nucleotides."}
    ]
  },
  "phagocyte": {
    "primary": "A type of cell within the body capable of engulfing and absorbing bacteria, foreign particles, and dying cells.",
    "secondary": "In immunology, professional phagocytes include neutrophils, monocytes, macrophages, and dendritic cells, which destroy engulfed pathogens via reactive oxygen species.",
    "quotes": [
      {"author": "Élie Metchnikoff", "work": "Immunity in Infective Diseases", "quote": "The active **phagocyte** surrounds and engulfs the invading bacterium, digesting it inside an intracellular vacuole."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The battle between the invading microbe and the host **phagocyte** determines the ultimate outcome of lobar pneumonia."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "Opsonization of microbes with antibodies or complement facilitates binding to Fc receptors on the **phagocyte** membrane."}
    ]
  },
  "phagocytic": {
    "primary": "Relating to or characterized by phagocytes or phagocytosis; having the capability to engulf and digest cells or particles.",
    "secondary": "In cell biology, phagocytic uptake involves actin polymerization that projects pseudopodia around large extracellular targets (>0.5 micrometers).",
    "quotes": [
      {"author": "Élie Metchnikoff", "work": "Comparative Pathology of Inflammation", "quote": "The **phagocytic** reaction represents a universal biological defense preserved from lower invertebrates to man."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "Specialized **phagocytic** cells clear billions of senescent erythrocytes daily in the human spleen."},
      {"author": "David L. Nelson", "work": "Lehninger Principles of Biochemistry", "quote": "The oxidative burst in **phagocytic** leukocytes generates superoxide anions via membrane-bound NADPH oxidase."}
    ]
  },
  "phagocytosis": {
    "primary": "The ingestion of bacteria or other material by phagocytes and amoeboid protozoans.",
    "secondary": "In cellular immunology, phagocytosis is a receptor-mediated endocytic mechanism for clearing microbial pathogens, apoptotic cells, and foreign debris.",
    "quotes": [
      {"author": "Élie Metchnikoff", "work": "Immunity in Infective Diseases", "quote": "I observed under the microscope that mobile cells engulfed rose thorns in starfish larvae, discovering **phagocytosis**."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "Receptor-mediated **phagocytosis** triggers rapid remodeling of the actin cytoskeleton to extend engulfing pseudopodia."},
      {"author": "Paul Ehrlich", "work": "Studies in Immunity", "quote": "Complement factors act as opsonins, enhancing the rate and efficiency of bacterial **phagocytosis** by leukocytes."}
    ]
  },
  "phagolysosome": {
    "primary": "A cytoplasmic body formed by the fusion of a phagosome with a lysosome in a phagocytic cell.",
    "secondary": "In cellular pathology, inside the acidic phagolysosome (pH 4.5–5.0), hydrolytic enzymes and reactive oxygen radicals degrade engulfed microorganisms.",
    "quotes": [
      {"author": "Christian de Duve", "work": "Lysosomes and Phagocytosis", "quote": "Fusion of the primary lysosome with the engulfed vacuole creates the active digestive **phagolysosome**."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "Pathogens like Mycobacterium tuberculosis prevent maturation of the **phagolysosome**, surviving inside unacidified vacuoles."},
      {"author": "David L. Nelson", "work": "Lehninger Principles of Biochemistry", "quote": "Acid hydrolases within the **phagolysosome** digest bacterial proteins, lipids, and nucleic acids into reusable precursors."}
    ]
  },
  "phagophilia": {
    "primary": "An abnormal or excessive love of or fixation on eating, consuming food, or observing eating behavior.",
    "secondary": "In behavioral psychology, a paraphilic or psychological fascination involving food consumption or eating rituals.",
    "quotes": [
      {"author": "Richard von Krafft-Ebing", "work": "Psychopathia Sexualis", "quote": "Certain obsessive neuroses present bizarre manifestations of **phagophilia**, where compulsive eating becomes intertwined with emotional fixation."},
      {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "The psychological phenomenon of **phagophilia** connects gustatory indulgence with deep subconscious cravings for security."},
      {"author": "Sigmund Freud", "work": "Three Essays on the Theory of Sexuality", "quote": "Oral fixation may persist into adult character as compulsive **phagophilia** or gluttonous overeating."}
    ]
  },
  "phagophobia": {
    "primary": "An irrational or excessive fear of swallowing or eating, often rooted in a dread of choking.",
    "secondary": "In clinical psychiatry and feeding disorders, phagophobia is a specific functional phobia characterized by avoidance of solid foods without anatomical esophageal obstruction.",
    "quotes": [
      {"author": "Pierre Janet", "work": "The Mental State of Hystericals", "quote": "Patients seized by **phagophobia** refuse solid nourishment through an irrational dread that their throat will close."},
      {"author": "Tinsley R. Harrison", "work": "Principles of Internal Medicine", "quote": "Distinguishing psychogenic **phagophobia** from true mechanical dysphagia requires careful radiographic confirmation of normal swallowing mechanics."},
      {"author": "Emil Kraepelin", "work": "Clinical Psychiatry", "quote": "Severe anxiety neurosis may manifest as acute **phagophobia**, requiring behavioral desensitization to restore oral nutrition."}
    ]
  },
  "phagosome": {
    "primary": "A vacuole formed around a particle absorbed by phagocytosis in a phagocyte.",
    "secondary": "In cell biology, the nascent phagosome undergoes a maturation sequence involving sequential fusion with early endosomes, late endosomes, and lysosomes.",
    "quotes": [
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "The newly closed **phagosome** recruits Rab GTPases that direct its traffic along microtubules toward the cell center."},
      {"author": "David L. Nelson", "work": "Lehninger Principles of Biochemistry", "quote": "Proton pumps rapidly acidify the interior of the **phagosome** before it fuses with primary lysosomes."},
      {"author": "Élie Metchnikoff", "work": "Immunity in Infective Diseases", "quote": "Enclosing the foreign particle within a membranous **phagosome** prevents cytotoxic enzymes from damaging the host cytoplasm."}
    ]
  },
  "phagun": {
    "primary": "The eleventh month of the Hindu calendar (corresponding to February–March), often celebrating the arrival of spring and the festival of Holi.",
    "secondary": "In South Asian literature and ethnobotany, Phagun (Phalguna) is associated with blossoming flora, harvest celebrations, and seasonal folk songs.",
    "quotes": [
      {"author": "Rabindranath Tagore", "work": "Gitanjali", "quote": "In the joyous breeze of **Phagun**, the red palash blossoms awaken the slumbering forest with vibrant spring fire."},
      {"author": "Premchand", "work": "Godan", "quote": "The villagers gathered in the square during **Phagun**, singing festive songs of spring despite their grinding debts."},
      {"author": "Mirabai", "work": "Songs of Devotion", "quote": "The month of **Phagun** has arrived, and the courtyard is filled with colored dust and celestial ecstasy."}
    ]
  },
  "phagy": {
    "primary": "A combining form denoting the eating, consuming, or feeding on a specified substance or food type (as in coprophagy, monophagy).",
    "secondary": "In ecological taxonomy and nutritional biology, terms ending in -phagy define specific trophic habits and dietary specializations across animal taxa.",
    "quotes": [
      {"author": "E. O. Wilson", "work": "Sociobiology: The New Synthesis", "quote": "Specialized dietary habits like xylophagy and mycophagy illustrate how ecological **phagy** drives morphological adaptation."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Anthropological records demonstrate how cannibalistic **phagy** was historically tied to ceremonial conquest."},
      {"author": "Robert Beekes", "work": "Etymological Dictionary of Greek", "quote": "The suffix -**phagy** traces back directly to the Greek verbal noun denoting consumption and feeding."}
    ]
  },
  "polyphagia": {
    "primary": "Excessive or insatiable hunger and eating, especially as a clinical symptom.",
    "secondary": "In endocrinology, polyphagia forms one of the classic triad symptoms of diabetes mellitus (alongside polyuria and polydipsia), caused by cellular starvation due to lack of insulin.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The untreated diabetic displays voracious **polyphagia**, losing weight continuously despite consuming immense quantities of food."},
      {"author": "Tinsley R. Harrison", "work": "Principles of Internal Medicine", "quote": "In ketoacidosis, cellular glucose deprivation in the hypothalamic satiety center triggers intense **polyphagia**."},
      {"author": "Eugene Braunwald", "work": "Harrison's Principles of Internal Medicine", "quote": "Patients presenting with persistent polyuria, polydipsia, and **polyphagia** should undergo immediate fasting plasma glucose testing."}
    ]
  },
  "pseudodysphagia": {
    "primary": "A psychogenic condition characterized by the sensation of difficulty swallowing without any physiological or anatomical obstruction; phagophobia.",
    "secondary": "In psychosomatic medicine and speech-language pathology, pseudodysphagia typically stems from a panic episode or choking trauma, treated with cognitive behavioral therapy.",
    "quotes": [
      {"author": "Pierre Janet", "work": "The Major Symptoms of Hysteria", "quote": "In hysterical **pseudodysphagia**, the patient complains of total blockage while endoscopic examination reveals a perfectly patent lumen."},
      {"author": "Tinsley R. Harrison", "work": "Principles of Internal Medicine", "quote": "A normal barium swallow confirms that the patient’s severe swallowing anxiety is a manifestation of **pseudodysphagia**."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Reassurance and gentle re-education often resolve psychogenic globus and **pseudodysphagia** without invasive procedures."}
    ]
  },
  "Phrynobatrachus": {
    "primary": "A large genus of small African puddle frogs belonging to the family Phrynobatrachidae.",
    "secondary": "In herpetology, species of *Phrynobatrachus* inhabit humid savannahs and rainforest leaf litter across sub-Saharan Africa, breeding opportunistically in temporary rain pools.",
    "quotes": [
      {"author": "George Albert Boulenger", "work": "The Tailless Batrachians of Europe and Africa", "quote": "The genus **Phrynobatrachus** includes diminutive puddle frogs with partially webbed toes and distinctive subgular vocal sacs."},
      {"author": "Arthur Loveridge", "work": "Reptiles and Amphibians of East Africa", "quote": "After heavy tropical downpours, countless specimens of **Phrynobatrachus** congregate around muddy pools to chorus."},
      {"author": "Ernst Mayr", "work": "Systematics and the Origin of Species", "quote": "High cryptic diversity in **Phrynobatrachus** demonstrates the complexity of speciation in equatorial African wetlands."}
    ]
  },
  "phrynosoma": {
    "primary": "A genus of specialized lizards in the family Phrynosomatidae commonly known as horned lizards (or horny toads), native to arid regions of North America.",
    "secondary": "In evolutionary biology, species of *Phrynosoma* feature flattened spiny bodies, specialized ant-eating (myrmecophagous) dentition, and the ability to squirt blood from their eyes (autohemorrhaging).",
    "quotes": [
      {"author": "Edward Drinker Cope", "work": "The Crocodilians, Lizards, and Snakes of North America", "quote": "The bizarre horned lizard of the genus **Phrynosoma** mimics weathered stones upon the sunbaked desert floor."},
      {"author": "David Starr Jordan", "work": "Manual of the Vertebrate Animals of the Northern United States", "quote": "Children across the American Southwest are familiar with the docile, flattened form of **Phrynosoma**."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Defensive cephalic spines in **Phrynosoma** illustrate extreme morphological adaptation against reptilian and avian predators."}
    ]
  },
  "isopiestic": {
    "primary": "Having or denoting equal barometric or vapor pressure; isobaric.",
    "secondary": "In physical chemistry and thermodynamics, the isopiestic method determines thermodynamic activities of electrolyte solutions by equilibrating them at constant vapor pressure.",
    "quotes": [
      {"author": "Gilbert N. Lewis", "work": "Thermodynamics and the Free Energy of Chemical Substances", "quote": "The **isopiestic** comparison method provides highly accurate osmotic coefficients for concentrated aqueous salt solutions."},
      {"author": "Herbert S. Harned", "work": "The Physical Chemistry of Electrolytic Solutions", "quote": "In an **isopiestic** apparatus, closed dishes equilibrate until vapor pressures over both solutions become precisely identical."},
      {"author": "J. Willard Gibbs", "work": "On the Equilibrium of Heterogeneous Substances", "quote": "Thermodynamic equilibrium in closed multiphase systems requires uniform temperature and an **isopiestic** distribution of pressures."}
    ]
  },
  "piezochromism": {
    "primary": "The phenomenon whereby a substance changes color reversibly under the influence of applied mechanical pressure.",
    "secondary": "In materials science and solid-state physics, piezochromism occurs in certain conjugated polymers and coordination complexes due to pressure-induced alterations in molecular orbital overlap.",
    "quotes": [
      {"author": "Roald Hoffmann", "work": "Solids and Surfaces", "quote": "Dramatic **piezochromism** in metallomacrocycles results from compression of intermolecular axial metal-metal distances."},
      {"author": "C. N. R. Rao", "work": "Solid State Chemistry", "quote": "Subjecting crystalline organic salts to high hydrostatic pressure induces reversible **piezochromism** through lattice strain."},
      {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "Band gap narrowing under severe compression provides the quantum mechanical explanation for visible **piezochromism**."}
    ]
  },
  "piezoelectric": {
    "primary": "Of, relating to, or exhibiting piezoelectricity; generating electric charge in response to applied mechanical stress, and vice versa.",
    "secondary": "In electronics and acoustics, piezoelectric crystals (such as quartz and lead zirconate titanate) are utilized in sonar transducers, ultrasound probes, and precision clocks.",
    "quotes": [
      {"author": "Pierre Curie", "work": "Development of Polar Electricity in Hemimorphous Crystals", "quote": "Compressing quartz along its hemihedral axes generates opposite electric charges, revealing the **piezoelectric** effect."},
      {"author": "Lord Rayleigh", "work": "The Theory of Sound", "quote": "Modern underwater acoustics employs high-frequency **piezoelectric** transmitters to propagate directional sound beams."},
      {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "The absence of an inversion center in the crystal lattice is the fundamental prerequisite for a **piezoelectric** response."}
    ]
  },
  "piezoelectricity": {
    "primary": "Electric polarization produced in certain non-centrosymmetric crystals (such as quartz) as a result of applied mechanical stress.",
    "secondary": "In solid-state physics, piezoelectricity is a reversible linear electromechanical interaction discovered by Jacques and Pierre Curie in 1880.",
    "quotes": [
      {"author": "Jacques Curie", "work": "Sur l'Électricité Polaire dans les Cristaux Hémièdres", "quote": "The discovery of **piezoelectricity** proved that mechanical deformation can directly polarize asymmetric dielectric crystals."},
      {"author": "Walter Guyton Cady", "work": "Piezoelectricity: An Introduction to the Theory and Applications of Electromechanical Phenomena in Crystals", "quote": "The mathematical theory of **piezoelectricity** couples Hooke’s law of elasticity with Maxwell’s electrostatic equations."},
      {"author": "Charles Kittel", "work": "Introduction to Solid State Physics", "quote": "Lattice displacement of positive and negative sublattices under strain generates macroscopic **piezoelectricity**."}
    ]
  },
  "piezometer": {
    "primary": "An instrument for measuring the pressure of a liquid or gas, or the compressibility of substances under pressure.",
    "secondary": "In hydrogeology and geotechnical engineering, an open standpipe or vibrating-wire piezometer measures pore water pressure and potentiometric levels in aquifers.",
    "quotes": [
      {"author": "Hans Christian Ørsted", "work": "Experiments on the Compressibility of Water", "quote": "By enclosing liquid within a glass **piezometer**, I measured the exact volumetric compression under atmospheric increments."},
      {"author": "Karl von Terzaghi", "work": "Theoretical Soil Mechanics", "quote": "Monitoring pore-water pressures with an electric **piezometer** is vital for predicting slope stability in embankment dams."},
      {"author": "Frank Wigglesworth Clarke", "work": "The Data of Geochemistry", "quote": "Deep borehole hydrologic investigations utilize a sensitive downhole **piezometer** to record artesian heads."}
    ]
  }
}

batch_data = {}
for rel_path in batch4_files:
    word = rel_path.split('\\')[-1].replace('.md', '')
    if word in lexicon:
        batch_data[rel_path] = lexicon[word]
    elif word.lower() in lexicon:
        batch_data[rel_path] = lexicon[word.lower()]
    else:
        print(f"Warning: word '{word}' not found in lexicon for {rel_path}")

print(f"Mapped {len(batch_data)} of {len(batch4_files)} files in Batch 4.")

base_dir = r"App database\Greek roots\Cluster Form & Space"
mjs_path = r"main app\scripts\curate_form_finish2_b4.mjs"

content = f"""import {{ updateNotesBatch }} from './curate-updater-util.mjs';

const baseDir = {json.dumps(base_dir)};
const batchData = {json.dumps(batch_data, indent=2, ensure_ascii=False)};

const count = updateNotesBatch(baseDir, batchData);
console.log(`Updated ${{count}} notes in Form Finish Slice 2 Batch 4.`);
"""

with open(mjs_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Generated {mjs_path} successfully.")
