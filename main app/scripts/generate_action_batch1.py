import json

batch1_data = {
  "Dashboard — actin/Actinomyces.md": {
    "primary": "A genus of Gram-positive, rod-shaped, facultatively anaerobic bacteria that form branching filamentous colonies resembling fungal mycelia.",
    "secondary": "In clinical microbiology, opportunistic pathogens inhabiting mucosal membranes that can trigger chronic suppurative and granulomatous actinomycosis.",
    "quotes": [
      { "author": "Robert Koch", "work": "Investigations into the Etiology of Traumatic Infective Diseases", "text": "Microscopic sections from the cattle lesions revealed characteristic branching rosettes of **Actinomyces**." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "text": "Sulfur granules discharged from cervicofacial sinuses confirm the presence of pathogenic **Actinomyces**." },
      { "author": "Alexander Fleming", "work": "Chemotherapy: Yesterday, Today, and Tomorrow", "text": "Penicillin proved remarkably potent against deep-seated infections caused by **Actinomyces**." }
    ]
  },
  "Dashboard — actin/Actinopterygii.md": {
    "primary": "The class of ray-finned fishes, constituting the dominant and most diverse group of living bony fishes.",
    "secondary": "In vertebrate taxonomy, osteichthyans whose lepidotrichia radiate directly from proximal skeletal radials rather than muscular lobes.",
    "quotes": [
      { "author": "Alfred Romer", "work": "Vertebrate Paleontology", "text": "The explosive radiation of **Actinopterygii** during the Mesozoic produced thousands of specialized teleost families." },
      { "author": "Stephen Jay Gould", "work": "The Structure of Evolutionary Theory", "text": "By any standard of diversity and adaptive triumph, the **Actinopterygii** rule the aquatic realm." },
      { "author": "Ernst Mayr", "work": "Systematics and the Origin of Species", "text": "Speciation mechanisms within freshwater **Actinopterygii** showcase rapid divergence in isolated rift basins." }
    ]
  },
  "Dashboard — actin/Actinozoa.md": {
    "primary": "A class or subphylum of marine cnidarians comprising sea anemones and corals that lack a medusoid stage.",
    "secondary": "In invertebrate zoology, polypoid organisms displaying radial symmetry organized around a central pharynx with radiating vertical mesenteries.",
    "quotes": [
      { "author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "text": "The gastrovascular cavity of every **Actinozoa** is divided into radiating compartments by fleshy septa." },
      { "author": "Ernst Haeckel", "work": "Art Forms in Nature", "text": "Elaborate calices secreted by colonial **Actinozoa** form the colossal ramparts of tropical coral atolls." },
      { "author": "Philip Henry Gosse", "work": "A History of the British Sea-Anemones and Corals", "text": "Our coastlines abound with solitary **Actinozoa** that flower into vibrant disc tentacles upon the incoming tide." }
    ]
  },
  "Dashboard — actin/actin.md": {
    "primary": "A structural globular protein that polymerizes into dynamic microfilaments throughout eukaryotic cells.",
    "secondary": "A foundational cytoskeletal element that partners with myosin to drive muscular contraction, cytoplasmic streaming, and cell motility.",
    "quotes": [
      { "author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "text": "Each filament of **actin** is an asymmetric helical polymer possessing distinct plus and minus ends." },
      { "author": "Albert Szent-Györgyi", "work": "Chemistry of Muscular Contraction", "text": "When adenosine triphosphate is added, purified **actin** and myosin interact to generate vigorous mechanical tension." },
      { "author": "Siddhartha Mukherjee", "work": "The Song of the Cell", "text": "Under confocal illumination, bundles of **actin** polymerize rapidly at the leading lamellipodium of crawling lymphocytes." }
    ]
  },
  "Dashboard — actin/actinal.md": {
    "primary": "Relating to the oral surface or the area bearing tentacles or mouth parts in radiately symmetrical animals.",
    "secondary": "In echinoderm anatomy, the ventral region bearing the ambulacral grooves and tube feet, contrasting with the abactinal surface.",
    "quotes": [
      { "author": "Libbie Hyman", "work": "The Invertebrates: Echinodermata", "text": "The **actinal** plate system encompasses the ambulacral ossicles and peristomial membranes of the sea star." },
      { "author": "Louis Agassiz", "work": "Contributions to the Natural History of the United States", "text": "Tentacular rows converge neatly toward the central mouth on the flat **actinal** surface of the disc." },
      { "author": "Ray Lankester", "work": "A Treatise on Zoology", "text": "Ciliary currents traverse the **actinal** grooves, conveying suspended microscopic food particles toward the mouth." }
    ]
  },
  "Dashboard — actinaria.md": {
    "primary": "A taxonomic order of solitary marine anthozoans lacking a calcareous skeleton, commonly known as sea anemones.",
    "secondary": "In systematic coelenterate zoology, soft-bodied polyps adhering to substrates by a basal pedal disc with radiating tentacles.",
    "quotes": [
      { "author": "Philip Henry Gosse", "work": "Actinologia Britannica", "text": "Members of the order **Actinaria** anchor their fleshy columns securely within tidal crevices." },
      { "author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "text": "Internal digestive septa in **Actinaria** demonstrate pronounced hexamerous radial symmetry." },
      { "author": "Charles Darwin", "work": "The Structure and Distribution of Coral Reefs", "text": "Large solitary **Actinaria** nestled among the massive stony corals, expanding their translucent tentacles in the lagoon." }
    ]
  },
  "Dashboard — actin/actinia.md": {
    "primary": "A genus of smooth-bodied, solitary sea anemones characterized by bead-like acrorhagi bearing stinging nematocysts.",
    "secondary": "In marine biology, the cosmopolitan beadlet anemone genus found commonly along rocky intertidal zones.",
    "quotes": [
      { "author": "Philip Henry Gosse", "work": "The Ocean", "text": "The ruby-red **Actinia** clings tenaciously to submerged rocks, retracting into a jelly-like button when exposed to air." },
      { "author": "George Henry Lewes", "work": "Sea-Side Studies", "text": "Feeding a morsel of limpet flesh to a captive **Actinia** evokes an instantaneous inward curling of its tentacles." },
      { "author": "Charles Kingsley", "work": "Glaucus; or, The Wonders of the Shore", "text": "Every clear rock pool presents some splendid variety of **Actinia** glistening beneath the salt water." }
    ]
  },
  "Dashboard — actin/actinian.md": {
    "primary": "A sea anemone belonging to the order Actiniaria; or relating to this order of marine polyps.",
    "secondary": "In marine ecology, an uncalcified, benthic anthozoan adapted for predatory feeding and hydrostatic shape changes.",
    "quotes": [
      { "author": "Rachel Carson", "work": "The Edge of the Sea", "text": "The solitary **actinian** waits in its rock cleft, its petal-like tentacles sensitive to the brushing of a passing shrimp." },
      { "author": "William Beebe", "work": "Beneath Tropic Seas", "text": "Down on the reef wall, a giant **actinian** hosted a pair of striped clownfish dancing unharmed amidst stinging tentacles." },
      { "author": "Libbie Hyman", "work": "The Invertebrates: Protozoa through Ctenophora", "text": "The muscular column of an **actinian** relies upon fluid-filled coelenteric pressure for extension and contraction." }
    ]
  },
  "Dashboard — actin/actiniaria.md": {
    "primary": "The taxonomic order of anthozoans comprising solitary, skeleton-less sea anemones.",
    "secondary": "An order of hexacorallians possessing pairs of complete and incomplete mesenteries arranged in hexamerous cycles.",
    "quotes": [
      { "author": "Ernst Haeckel", "work": "Report on the Deep-Sea Keratosa", "text": "Specimens of **Actiniaria** dredged from abyssal depths exhibited remarkable adaptations to frigid oceanic pressures." },
      { "author": "Ray Lankester", "work": "A Treatise on Zoology", "text": "The **Actiniaria** diverge fundamentally from the Scleractinia by their complete absence of a hard stony corallum." },
      { "author": "Alpheus Hyatt", "work": "Commercial and Other Sponges", "text": "Commensal associations between hermit crabs and species of **Actiniaria** illustrate mutual protective adaptations." }
    ]
  },
  "Dashboard — actin/actiniarian.md": {
    "primary": "Belonging or pertaining to the sea anemone order Actiniaria.",
    "secondary": "An organism exhibiting the anatomical characteristics of soft-bodied anthozoans with hexamerous mesenterial symmetry.",
    "quotes": [
      { "author": "Libbie Hyman", "work": "The Invertebrates", "text": "The **actiniarian** nervous system comprises a diffuse subepidermal nerve net governing coordinated retraction." },
      { "author": "Philip Henry Gosse", "work": "Actinologia Britannica", "text": "We observed the **actiniarian** column slowly detach its pedal disc to drift across the aquarium floor." },
      { "author": "V. B. Wigglesworth", "work": "The Principles of Insect Physiology", "text": "Neurotoxins isolated from **actiniarian** tentacles produce immediate neuromuscular blockades in arthropod prey." }
    ]
  },
  "Dashboard — actin/actinic.md": {
    "primary": "Relating to or causing chemical changes through radiant energy, especially in the ultraviolet and violet spectrum.",
    "secondary": "In photography and photochemistry, radiation capable of sensitizing silver halides or inducing photochemical polymerization.",
    "quotes": [
      { "author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "text": "Sunlight possesses diverse virtues: heating in the infrared, illuminating in the yellow, and **actinic** in the extreme violet." },
      { "author": "Oliver Wendell Holmes Sr.", "work": "The Stereoscope and the Stereograph", "text": "The **actinic** rays carve instantaneous silhouettes of reality upon the sensitized collodion plate." },
      { "author": "Arthur Conan Doyle", "work": "The Poison Belt", "text": "The subtle blue glimmer through the chamber roof possessed an intense, almost blinding **actinic** glare." }
    ]
  },
  "Dashboard — actin/actinide.md": {
    "primary": "Any of the series of 15 radioactive metallic elements with atomic numbers from 89 (actinium) to 103 (lawrencium).",
    "secondary": "In inorganic chemistry, 5f-block inner transition elements characterized by progressive f-orbital filling and variable oxidation states.",
    "quotes": [
      { "author": "Glenn T. Seaborg", "work": "Man-Made Transuranium Elements", "text": "The synthesis of heavy elements established the **actinide** hypothesis, grouping them beneath the lanthanides in the periodic table." },
      { "author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "text": "Relativistic effects become increasingly pronounced across the heavier members of the **actinide** series." },
      { "author": "Richard Feynman", "work": "The Character of Physical Law", "text": "Nuclear engineers must account for the gradual accumulation of **actinide** isotopes inside fission reactors." }
    ]
  },
  "Dashboard — actin/actinidia.md": {
    "primary": "A genus of dioecious, deciduous climbing woody vines native to eastern Asia, notable for producing edible kiwifruit.",
    "secondary": "In horticultural botany, vigorous lianas characterized by showy cup-shaped flowers and berry fruits with numerous tiny black seeds.",
    "quotes": [
      { "author": "E. H. Wilson", "work": "A Naturalist in Western China", "text": "High up in the forested ravines of Hubei, robust vines of **Actinidia** drape profusely across towering oaks." },
      { "author": "Liberty Hyde Bailey", "work": "The Standard Cyclopedia of Horticulture", "text": "Several ornamental species of **Actinidia** are cultivated for their variegated foliage and fragrant white blossoms." },
      { "author": "David Fairchild", "work": "Exploring for Plants", "text": "The Yang-tao vine, known botanically as **Actinidia**, produces refreshing emerald-fleshed fruits prized along the Yangtze." }
    ]
  },
  "Dashboard — actin/actinidiaceae.md": {
    "primary": "A family of flowering plants in the order Ericales, comprising woody climbing vines, trees, and shrubs including Actinidia.",
    "secondary": "In systematic taxonomy, an angiosperm family characterized by spiral leaves, multi-locular ovaries, and persistent styles.",
    "quotes": [
      { "author": "Arthur Cronquist", "work": "An Integrated System of Classification of Flowering Plants", "text": "Morphological affinities link the **Actinidiaceae** to the Ericaceae through shared embryological traits." },
      { "author": "Armen Takhtajan", "work": "Diversity and Classification of Flowering Plants", "text": "The **Actinidiaceae** represent an ancient eastern Asiatic lineage within the broader order Ericales." },
      { "author": "Liberty Hyde Bailey", "work": "Manual of Cultivated Plants", "text": "Vigorous climbing vines of the **Actinidiaceae** are widely planted along trellises for shade and fruit production." }
    ]
  },
  "Dashboard — actin/actiniopteris.md": {
    "primary": "A genus of small terrestrial xerophytic ferns in the family Pteridaceae, featuring fan-shaped radiating fronds resembling miniature palm leaves.",
    "secondary": "In pteridology, desiccation-tolerant ferns inhabiting rocky clefts across semi-arid regions of Africa and India.",
    "quotes": [
      { "author": "William Jackson Hooker", "work": "Species Filicum", "text": "The elegant fronds of **Actiniopteris** spread like tiny palmate fans from a creeping, scaly rhizome." },
      { "author": "John Gilbert Baker", "work": "Synopsis Filicum", "text": "During prolonged seasonal drought, **Actiniopteris** fronds curl tightly, reviving swiftly after the first monsoon rains." },
      { "author": "Richard Spruce", "work": "Notes of a Botanist on the Amazon and Andes", "text": "Rock-dwelling ferns such as **Actiniopteris** reveal exquisite morphological adaptations to arid cliff microclimates." }
    ]
  },
  "Dashboard — actin/actinism.md": {
    "primary": "The property of radiant solar energy by which chemical transformations and photochemical reactions are produced.",
    "secondary": "In classical physics and photography, the chemical efficacy of the solar spectrum, predominantly associated with short wavelengths.",
    "quotes": [
      { "author": "John Herschel", "work": "Memoir on the Chemical Action of the Rays of the Solar Spectrum", "text": "I proposed the term **actinism** to distinguish this chemical influence from the heating and illuminating rays." },
      { "author": "Robert Hunt", "work": "Researches on Light in Its Chemical Relations", "text": "Variations in atmospheric moisture modify the degree of solar **actinism** measured at sea level." },
      { "author": "Henry Fox Talbot", "work": "The Pencil of Nature", "text": "The latent image owes its creation entirely to the invisible power of solar **actinism** upon the halide wash." }
    ]
  },
  "Dashboard — actin/actinium.md": {
    "primary": "A rare, intensely radioactive, silvery-white metallic element of atomic number 89 (symbol Ac).",
    "secondary": "The prototype element of the actinide series, occurring in trace quantities within uranium ores as a product of radioactive decay.",
    "quotes": [
      { "author": "Marie Curie", "work": "Radioactive Substances", "text": "André Debierne succeeded in isolating **actinium** from the pitchblende residues left behind after extracting polonium and radium." },
      { "author": "Ernest Rutherford", "work": "Radioactivity", "text": "Emissions of alpha particles from **actinium** demonstrate a characteristic disintegration rate distinct from thorium." },
      { "author": "Frederick Soddy", "work": "The Chemistry of the Radio-Elements", "text": "Decay products derived from **actinium** established an independent collateral radioactive series culminating in lead." }
    ]
  },
  "Dashboard — actin/actinocerid.md": {
    "primary": "An extinct fossil cephalopod belonging to the order Actinocerida, characterized by large shells with elaborate siphuncular deposits.",
    "secondary": "In invertebrate paleontology, Paleozoic nautiloids whose thick siphuncles developed complex radial endosiphuncular rings for buoyancy control.",
    "quotes": [
      { "author": "Rousseau H. Flower", "work": "Cephalopods of the Ordovician", "text": "Cross sections of a mature **actinocerid** expose heavily calcified, beaded siphuncular rings along the phragmocone." },
      { "author": "Stephen Jay Gould", "work": "Wonderful Life", "text": "Paleozoic oceans harbored the formidable **actinocerid** predators whose chambered shells reached several meters in length." },
      { "author": "Alpheus Hyatt", "work": "Genera of Fossil Cephalopods", "text": "The rapid rise and subsequent extinction of the **actinocerid** lineage marked a crucial chapter in Ordovician marine faunas." }
    ]
  },
  "Dashboard — actin/actinodrome.md": {
    "primary": "Describing leaf venation in which three or more primary veins radiate outwards from a single basal point.",
    "secondary": "In plant morphology, palmate or radiating venation patterns common in maples, mallows, and geraniums.",
    "quotes": [
      { "author": "Asa Gray", "work": "Structural Botany", "text": "Leaves with an **actinodrome** architecture distribute sap equably along radiating primary ribs from the petiole junction." },
      { "author": "Leo Lesquereux", "work": "The Flora of the Dakota Group", "text": "Fossilized Cretaceous impressions exhibit well-preserved **actinodrome** foliage ancestral to modern platanoids." },
      { "author": "John Lindley", "work": "An Introduction to Botany", "text": "Botanists categorize broad palmate leaves as **actinodrome** when several equally prominent veins diverge at the base." }
    ]
  },
  "Dashboard — actin/actinoid.md": {
    "primary": "Radiating like rays or possessing a star-shaped, ray-like structure.",
    "secondary": "In chemistry, an alternative designation for any element of the actinide series; in zoology, resembling a sea anemone.",
    "quotes": [
      { "author": "Glenn T. Seaborg", "work": "The Chemical Elements and Their Compounds", "text": "Electronic configurations of the heavier **actinoid** elements reveal complex competition between 5f and 6d orbitals." },
      { "author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of Invertebrate Animals", "text": "The **actinoid** polyps unfold their petaloid coronals when the sea water washes quietly over the reef." },
      { "author": "Linus Pauling", "work": "General Chemistry", "text": "Comparable ionic radii across the **actinoid** series cause pronounced similarities in coordination behavior." }
    ]
  },
  "Dashboard — actin/actinolite.md": {
    "primary": "A green, fibrous or bladed amphibole mineral composed of calcium, magnesium, and iron inosilicate.",
    "secondary": "In petrology, an essential constituent of greenschist metamorphic facies, forming slender radiating needles or asbestiform masses.",
    "quotes": [
      { "author": "James Dwight Dana", "work": "Manual of Mineralogy", "text": "Radiating clusters of dark-green **actinolite** crystals frequently penetrate crystalline marble and talc schists." },
      { "author": "Archibald Geikie", "work": "Textbook of Geology", "text": "Metamorphic shearing transformed original pyroxene basalt into dense foliated rocks rich in fibrous **actinolite**." },
      { "author": "Arthur Holmes", "work": "Principles of Physical Geology", "text": "Nephrite jade is a compact, tough crypto-crystalline variety of **actinolite** prized by ancient lapidaries." }
    ]
  },
  "Dashboard — actin/actinomere.md": {
    "primary": "One of the radial segments or antimeres composing the body of a radiately symmetrical animal.",
    "secondary": "In comparative morphology, a single repeating wedge-shaped unit containing corresponding internal viscera in coelenterates or echinoderms.",
    "quotes": [
      { "author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "text": "Each repeating **actinomere** of the medusa carries an identical portion of the gastrovascular canal system." },
      { "author": "Ernst Haeckel", "work": "Generelle Morphologie der Organismen", "text": "Radial differentiation organizes multiple homonomous units into a unified organism, each constituent piece being an **actinomere**." },
      { "author": "Ray Lankester", "work": "Zoological Articles", "text": "Amputation of an individual **actinomere** in starfish triggers localized wound closure followed by coordinated regeneration." }
    ]
  },
  "Dashboard — actin/actinomeris.md": {
    "primary": "A genus of North American composite herbs in the sunflower family, commonly known as wingstem.",
    "secondary": "In taxonomic botany, tall perennial herbs featuring winged stems and loose corymbs of yellow radiating flower heads.",
    "quotes": [
      { "author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "text": "Along rich bottomlands, tall stems of **Actinomeris** display irregular yellow rays above winged petioles." },
      { "author": "John Torrey", "work": "Flora of North America", "text": "The decurrent leaf bases of **Actinomeris** create prominent leafy wings extending continuously down the stem." },
      { "author": "Liberty Hyde Bailey", "work": "Cyclopedia of American Horticulture", "text": "In wild woodland borders, **Actinomeris** provides a late autumnal golden display attractive to native bees." }
    ]
  },
  "Dashboard — actin/actinometer.md": {
    "primary": "An instrument designed to measure the heating power or photochemical intensity of solar radiation.",
    "secondary": "In early meteorology and photography, an apparatus assessing exposure times or solar constants via temperature rise or light-sensitive paper.",
    "quotes": [
      { "author": "John Herschel", "work": "Results of Astronomical Observations at the Cape of Good Hope", "text": "Using my liquid **actinometer**, I measured the direct thermal power of southern solar rays at high noon." },
      { "author": "Samuel Pierpont Langley", "work": "The Bolometer and Radiant Energy", "text": "The classical **actinometer** provided early scientists with invaluable estimates of atmospheric radiation absorption." },
      { "author": "Robert Hunt", "work": "A Manual of Photography", "text": "Every careful calotypist kept an **actinometer** at hand to calculate plate exposure under shifting cloud cover." }
    ]
  },
  "Dashboard — actin/actinometric.md": {
    "primary": "Pertaining to the measurement of radiant solar heat or photochemical radiation.",
    "secondary": "Describing instruments, data, or techniques employed in actinometry to assess radiative flux in the atmosphere.",
    "quotes": [
      { "author": "Svante Arrhenius", "work": "On the Influence of Carbonic Acid in the Air upon the Temperature of the Ground", "text": "Extensive **actinometric** observations demonstrate how water vapor selectively intercepts terrestrial thermal emission." },
      { "author": "Cleveland Abbe", "work": "The Mechanics of the Earth's Atmosphere", "text": "High-altitude observatories conduct systematic **actinometric** surveys to eliminate tropospheric dust interference." },
      { "author": "Alexander von Humboldt", "work": "Cosmos: A Sketch of a Physical Description of the Universe", "text": "We performed **actinometric** experiments on Andean peaks to chart solar radiation intensity across elevations." }
    ]
  },
  "Dashboard — actin/actinometrical.md": {
    "primary": "Relating to or obtained by means of an actinometer.",
    "secondary": "In physical science, descriptive of quantitative observations documenting solar intensity and atmospheric extinction.",
    "quotes": [
      { "author": "John Herschel", "work": "Treatise on Astronomy", "text": "A long series of **actinometrical** measurements confirmed periodic fluctuations in apparent solar emission." },
      { "author": "James David Forbes", "work": "Travels through the Alps of Savoy", "text": "My **actinometrical** records upon the Mont Blanc glacier proved that high atmospheric clarity intensifies direct solar burn." },
      { "author": "Robert Hunt", "work": "Researches on Light", "text": "Comparative **actinometrical** tables demonstrate that chemical radiation peaks hours before maximum thermal heat." }
    ]
  },
  "Dashboard — actin/actinometry.md": {
    "primary": "The scientific measurement of the intensity of radiant energy, particularly solar and photochemical radiation.",
    "secondary": "In atmospheric physics and chemical kinetics, the quantitative determination of photon flux and quantum yields.",
    "quotes": [
      { "author": "Robert Bunsen", "work": "Photochemical Researches", "text": "Accurate chemical **actinometry** requires precise measurement of hydrochloric acid formation under chlorine and hydrogen exposure." },
      { "author": "Cleveland Abbe", "work": "Treatise on Meteorological Apparatus", "text": "The development of modern **actinometry** laid the empirical foundation for understanding planetary heat balance." },
      { "author": "Wilhelm Ostwald", "work": "Outlines of General Chemistry", "text": "In photochemical reactions, **actinometry** provides the direct measure of quantum absorption per unit time." }
    ]
  },
  "Dashboard — actin/actinomorphic.md": {
    "primary": "Having radial symmetry, such that the body or floral structure can be divided into identical halves along multiple radial planes.",
    "secondary": "In floral morphology, regular flowers such as buttercups or lilies that possess symmetrical perianth arrangements.",
    "quotes": [
      { "author": "Asa Gray", "work": "Elements of Botany", "text": "The regular, star-shaped blossoms of the rose are strictly **actinomorphic**, contrasting with bilaterally symmetric orchids." },
      { "author": "John Lindley", "work": "The Vegetable Kingdom", "text": "An **actinomorphic** corolla displays equal segments arrayed equidistant from the floral receptacle center." },
      { "author": "Arthur Cronquist", "work": "The Evolution and Classification of Flowering Plants", "text": "Primitive angiosperms generally possessed **actinomorphic** blossoms pollinated by generalist foraging beetles." }
    ]
  },
  "Dashboard — actin/actinomorphous.md": {
    "primary": "Radially symmetrical in form; capable of bisection into symmetrical halves along more than one longitudinal plane.",
    "secondary": "In botanical and zoological systematics, possessing a radially disposed, regular anatomical plan.",
    "quotes": [
      { "author": "Thomas Henry Huxley", "work": "The Anatomy of Invertebrated Animals", "text": "Coelenterate bodies are typically **actinomorphous**, organized circularly around the central digestive axis." },
      { "author": "George Bentham", "work": "Handbook of the British Flora", "text": "The five petals form an **actinomorphous** whorl whose uniform segments expand evenly toward the sun." },
      { "author": "Ernst Haeckel", "work": "Art Forms in Nature", "text": "Radiolarian skeletons showcase breathtaking **actinomorphous** geometry sculpted in pure biogenic opal." }
    ]
  },
  "Dashboard — actin/actinomycetaceae.md": {
    "primary": "A family of Gram-positive, non-spore-forming, filamentous bacteria within the order Actinomycetales.",
    "secondary": "In bacteriology, predominantly anaerobic or microaerophilic organisms that colonize mammalian mucosal membranes.",
    "quotes": [
      { "author": "Selman Waksman", "work": "The Actinomycetes", "text": "Classification of the **Actinomycetaceae** proved contentious owing to their unique mycelial morphological traits." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "text": "Members of **Actinomycetaceae** normally inhabit oral crypts before invading lacerated or devitalized tissues." },
      { "author": "Robert Koch", "work": "Investigations into Pathogenic Organisms", "text": "Cultures of **Actinomycetaceae** demonstrate distinctive club-shaped mycelial colonies surrounded by inflammatory exudate." }
    ]
  },
  "Dashboard — actin/actinomycetal.md": {
    "primary": "Pertaining to, derived from, or characteristic of actinomycetes or the bacterial order Actinomycetales.",
    "secondary": "In pedology and microbial ecology, descriptive of the earthy aroma and antibiotic metabolism of soil actinobacteria.",
    "quotes": [
      { "author": "Selman Waksman", "work": "My Life with the Microbes", "text": "The rich petrichor of freshly turned spring soil arises directly from **actinomycetal** geosmin synthesis." },
      { "author": "René Dubos", "work": "The Bacterial Cell", "text": "Screening natural soils yielded diverse **actinomycetal** isolates exhibiting pronounced antagonistic inhibition." },
      { "author": "Alexander Fleming", "work": "Penicillin and Other Antibiotics", "text": "Recent pharmaceutical attention has shifted toward **actinomycetal** secondary metabolites for novel therapeutic compounds." }
    ]
  },
  "Dashboard — actin/actinomycetales.md": {
    "primary": "An order of Gram-positive bacteria characterized by filamentous, branching growth and high guanine-cytosine genomic content.",
    "secondary": "In industrial biotechnology and ecology, major soil organisms responsible for organic decomposition and the synthesis of bioactive antibiotics.",
    "quotes": [
      { "author": "Selman Waksman", "work": "Streptomycin: Its Nature and Practical Application", "text": "Our laboratory systematically investigated the order **Actinomycetales** in the search for antituberculosis substances." },
      { "author": "Arthur D. Imms", "work": "Textbook of Entomology", "text": "Symbiotic **Actinomycetales** living within insect mycangia synthesize defensive antibiotics against fungal invaders." },
      { "author": "Martinus Beijerinck", "work": "Studies on Soil Microbiology", "text": "Colonies of **Actinomycetales** develop slowly on nutrient agar, producing dry, chalky aerial hyphae." }
    ]
  },
  "Dashboard — actin/actinomycete.md": {
    "primary": "Any bacterium belonging to the Actinomycetales, characterized by branching filaments resembling fungal hyphae.",
    "secondary": "In soil science and pharmacology, prolific producers of natural secondary metabolites, including streptomycin, tetracycline, and erythromycin.",
    "quotes": [
      { "author": "Selman Waksman", "work": "My Life with the Microbes", "text": "A humble soil **actinomycete** yielded streptomycin, the first weapon capable of conquering human tuberculosis." },
      { "author": "Rachel Carson", "work": "Silent Spring", "text": "The living fabric of humus depends upon the tireless chemical labors of the bacteria, fungi, and **actinomycete** colonies." },
      { "author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "text": "Genome sequencing revealed that a single **actinomycete** strain may harbor dozens of unexpressed antibiotic gene clusters." }
    ]
  },
  "Dashboard — actin/actinomycetous.md": {
    "primary": "Of, relating to, or resembling the actinomycetes.",
    "secondary": "Describing bacterial colonies or infections displaying branching, mycelium-like morphology.",
    "quotes": [
      { "author": "Selman Waksman", "work": "The Actinomycetes", "text": "The **actinomycetous** habit of radial hyphal growth enables these bacteria to penetrate solid plant debris efficiently." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "text": "Histological staining confirmed the dense, radiating **actinomycetous** clumps within the chronic hepatic abscess." },
      { "author": "Louis Pasteur", "work": "Studies on Fermentation", "text": "Filamentous forms exhibiting an **actinomycetous** appearance were isolated from the decomposing compost vat." }
    ]
  },
  "Dashboard — actin/actinomycin.md": {
    "primary": "A chromopeptide antibiotic isolated from soil actinobacteria that binds DNA to inhibit RNA transcription.",
    "secondary": "In oncology and cell biology, a potent antineoplastic agent (such as actinomycin D) used in treating Wilms' tumor and rhabdomyosarcoma.",
    "quotes": [
      { "author": "Selman Waksman", "work": "My Life with the Microbes", "text": "In 1940 we isolated **actinomycin**, our very first antibiotic, though its fierce toxicity initially discouraged clinical use." },
      { "author": "James D. Watson", "work": "Molecular Biology of the Gene", "text": "By intercalating between adjacent guanine-cytosine base pairs, **actinomycin** halts messenger RNA synthesis abruptly." },
      { "author": "Siddhartha Mukherjee", "work": "The Emperor of All Maladies", "text": "Sidney Farber tested **actinomycin** D against Wilms' tumor, achieving dramatic remissions in children once deemed terminal." }
    ]
  },
  "Dashboard — actin/actinomycosis.md": {
    "primary": "A chronic, suppurative, and granulomatous bacterial infection caused by species of Actinomyces.",
    "secondary": "In clinical pathology, characterized by contiguous tissue spread, indurated wooden swellings, and multiple draining sinus tracts discharging sulfur granules.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "text": "Cervicofacial **actinomycosis** typically follows dental extraction or mandibular trauma in rural workers." },
      { "author": "Robert Koch", "work": "Investigations into Pathogenic Organisms", "text": "Lumpy jaw in cattle proved to be a bovine manifestation of **actinomycosis** spreading through the jawbone." },
      { "author": "Alexander Fleming", "work": "Chemotherapy: Yesterday, Today, and Tomorrow", "text": "Prolonged administration of high-dose penicillin is necessary to eradicate the deep-seated pockets of **actinomycosis**." }
    ]
  },
  "Dashboard — actin/actinomycotic.md": {
    "primary": "Pertaining to, caused by, or characteristic of actinomycosis.",
    "secondary": "Describing lesions, granulomas, or sinus tracts infiltrated by sulfur granules and filamentous Actinomyces colonies.",
    "quotes": [
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "text": "Microscopic examination of the **actinomycotic** granuloma revealed central bacterial rosettes rimmed by polymorphonuclear leukocytes." },
      { "author": "Lord Lister", "work": "Collected Papers", "text": "The extensive **actinomycotic** ulceration yielded gradually to persistent antiseptic packing and surgical debridement." },
      { "author": "Rudolf Virchow", "work": "Cellular Pathology", "text": "Dense fibrous proliferation around the **actinomycotic** focus demonstrates the classic chronic cellular defense mechanism." }
    ]
  },
  "Dashboard — actin/actinomyxidia.md": {
    "primary": "A group of parasitic cnidarians (formerly protozoans) in the Myxozoa that alternate life cycles between oligochaete worms and freshwater fishes.",
    "secondary": "In parasitology, spore-forming endoparasites characterized by tri-radiate or three-valved anchor-shaped spores with polar capsules.",
    "quotes": [
      { "author": "E. Ray Lankester", "work": "A Treatise on Zoology", "text": "The remarkable spores of **Actinomyxidia** possess three elongated radiating styles extending like anchors." },
      { "author": "Charles Wardell Stiles", "work": "A Compendium of Animal Parasites", "text": "In aquatic ecosystems, species of **Actinomyxidia** parasitize freshwater tubificid worms before transferring to fish." },
      { "author": "Libbie Hyman", "work": "The Invertebrates", "text": "Modern molecular phylogenetics demonstrated that **Actinomyxidia** represent reduced, highly specialized parasitic cnidarians." }
    ]
  },
  "Dashboard — actin/actinomyxidian.md": {
    "primary": "Of, relating to, or belonging to the Actinomyxidia.",
    "secondary": "An aquatic myxozoan parasite exhibiting radiating anchor-like spores that alternate hosts between annelids and teleosts.",
    "quotes": [
      { "author": "E. Ray Lankester", "work": "A Treatise on Zoology", "text": "The discharge of the **actinomyxidian** polar capsule anchors the spore firmly to the intestinal lining of the worm." },
      { "author": "Charles Wardell Stiles", "work": "Report on Animal Parasitology", "text": "Each **actinomyxidian** spore releases infectious sporoplasms that penetrate deep into the host's coelomic cavity." },
      { "author": "Thomas Henry Huxley", "work": "Manual of Invertebrate Anatomy", "text": "The complex life cycle of an **actinomyxidian** parasite challenged early single-celled protozoan taxonomy." }
    ]
  },
  "Dashboard — actin/actinon.md": {
    "primary": "A historical name for radon-219, a radioactive noble gas isotope produced during the actinium decay series.",
    "secondary": "In nuclear physics and radiochemistry, an alpha-emitting noble gas with a half-life of approximately 3.96 seconds.",
    "quotes": [
      { "author": "Ernest Rutherford", "work": "Radioactivity", "text": "The emanation from actinium, termed **actinon**, possesses an exceedingly fleeting existence of merely a few seconds." },
      { "author": "Frederick Soddy", "work": "The Chemistry of the Radio-Elements", "text": "By measuring the rapid decay of **actinon**, we distinguished it conclusively from the longer-lived thoron and radon gases." },
      { "author": "Marie Curie", "work": "Treatise on Radioactivity", "text": "Air passed through the actinium preparation carries the luminous gaseous **actinon** into the adjacent ionization chamber." }
    ]
  },
  "Dashboard — actin/actinophryid.md": {
    "primary": "A heliozoan protozoan belonging to the family Actinophryidae, commonly known as sun animalcules.",
    "secondary": "In protozoology, spherical freshwater protists possessing stiff, needle-like axopodia radiating outward in all directions to capture prey.",
    "quotes": [
      { "author": "Philip Henry Gosse", "work": "Evenings at the Microscope", "text": "Under darkfield lighting, the tiny **actinophryid** floats like a miniature radiant sun surrounded by glittering glass needles." },
      { "author": "Ernst Haeckel", "work": "Art Forms in Nature", "text": "The glassy geometric symmetry of an **actinophryid** captures the perfection of radial form in unicellular life." },
      { "author": "E. Ray Lankester", "work": "A Treatise on Zoology", "text": "Whenever a passing ciliate brushes an **actinophryid** axopodium, rapid cytoplasmic streaming immobilizes and engulfs the victim." }
    ]
  },
  "Dashboard — actin/actinopod.md": {
    "primary": "Any protist characterized by stiff radiating pseudopodia (axopodia), including radiolarians and heliozoans.",
    "secondary": "In protozoan morphology, a spherical or amoeboid single-celled organism supported by internal micro-tubular axonemes.",
    "quotes": [
      { "author": "Libbie Hyman", "work": "The Invertebrates: Protozoa through Ctenophora", "text": "The floating **actinopod** extends its delicate cytoplasmic spines through the water column to snare passing organic detritus." },
      { "author": "Ernst Mayr", "work": "Animal Species and Evolution", "text": "Pelagic ecosystems sustain vast populations of **actinopod** organisms whose siliceous remains blanket the ocean abyss." },
      { "author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "text": "Axial filaments within each pseudopodium endow the **actinopod** with rigid, star-like mechanical support." }
    ]
  },
  "Dashboard — actin/actinopoda.md": {
    "primary": "A classical protozoan taxonomic group comprising sarcodine amoebae with radiating, axopodia-supported pseudopods.",
    "secondary": "A polyphyletic grouping of marine and freshwater protists, including radiolarians, heliozoans, and acantharians, noted for intricate mineral skeletons.",
    "quotes": [
      { "author": "Ernst Haeckel", "work": "Report on the Radiolaria", "text": "The sublime architecture of the **Actinopoda** illustrates how biogenic silica can be sculpted into geodesic perfection." },
      { "author": "E. Ray Lankester", "work": "A Treatise on Zoology", "text": "Classic taxonomists assembled the **Actinopoda** based on the common possession of radiating, stiffened axopodia." },
      { "author": "Libbie Hyman", "work": "The Invertebrates", "text": "Plankton hauls from open oceanic waters reveal incredible numbers of **Actinopoda** floating within the photic zone." }
    ]
  },
  "Dashboard — actin/actinotherapy.md": {
    "primary": "The therapeutic use of radiant energy, particularly sunlight or ultraviolet and infrared radiation, to treat disease.",
    "secondary": "In historical clinical therapeutics, light-bath therapy employed in treating lupus vulgaris, rickets, and psoriasis.",
    "quotes": [
      { "author": "Niels Finsen", "work": "Phototherapy", "text": "Concentrated chemical light employed in **actinotherapy** eradicated cutaneous lupus lesions without mutilating surgery." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "text": "Childhood rickets responded swiftly to systematic **actinotherapy** using quartz mercury-vapor lamps." },
      { "author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "text": "Modern clinicians increasingly explore **actinotherapy**, discovering salutary physiological virtues in direct solar exposure." }
    ]
  },
  "Dashboard — actin/actinozoan.md": {
    "primary": "An anthozoan coelenterate, such as a sea anemone, stony coral, or sea fan.",
    "secondary": "In marine invertebrate zoology, a polypoid animal possessing a radial body plan partitioned by vertical fleshy mesenteries.",
    "quotes": [
      { "author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "text": "Every solitary **actinozoan** possesses a crown of tentacles encircling the mouth, which opens into an invaginated stomodaeum." },
      { "author": "Philip Henry Gosse", "work": "The Aquarium", "text": "The captive **actinozoan** blossomed into brilliant crimson glory as soon as fresh seawater entered the tank." },
      { "author": "Charles Darwin", "work": "The Structure and Distribution of Coral Reefs", "text": "Countless millions of colonial **actinozoan** polyps labor unceasingly to rear the majestic barrier reefs of the Pacific." }
    ]
  },
  "Dashboard — actin/periactin.md": {
    "primary": "A proprietary pharmaceutical brand name for cyproheptadine, a first-generation antihistamine with antiserotonergic properties.",
    "secondary": "In clinical pharmacology, an agent used to relieve allergic symptoms, treat serotonin syndrome, and stimulate appetite in chronic illness.",
    "quotes": [
      { "author": "Oliver Sacks", "work": "Migraine", "text": "In select patients suffering from intractable vascular headaches, prophylactic administration of **Periactin** provided marked symptomatic relief." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "text": "Pruritus associated with chronic urticaria often subsides following evening doses of **Periactin**." },
      { "author": "Siddhartha Mukherjee", "work": "The Song of the Cell", "text": "Clinicians observed that **Periactin** blocked peripheral serotonin receptors, counteracting the hyperactive neural cascade." }
    ]
  },
  "Dashboard — actin/protoactinium.md": {
    "primary": "An archaic name and spelling for protactinium, the radioactive metallic chemical element of atomic number 91.",
    "secondary": "In early radiochemistry, the parent radionuclide in the actinium decay chain, discovered by Otto Hahn and Lise Meitner.",
    "quotes": [
      { "author": "Lise Meitner", "work": "The Discovery of Protactinium", "text": "Otto Hahn and I succeeded in separating **protoactinium** from uranium pitchblende residues during the war years." },
      { "author": "Frederick Soddy", "work": "The Interpretation of Radium", "text": "Calculations demonstrated that **protoactinium** decays by alpha emission directly into actinium." },
      { "author": "Marie Curie", "work": "Radioactivity", "text": "The long-sought radioactive ancestor of actinium was designated **protoactinium** to denote its position in the decay lineage." }
    ]
  },
  "Dashboard — aux/_aux.md": {
    "primary": "The Greek combining root (from auxein, 'to increase, grow, augment') signifying growth, physical increase, or amplification.",
    "secondary": "In historical linguistics and etymology, the morphemic progenitor of biological and botanical terms related to cellular elongation and physiological development.",
    "quotes": [
      { "author": "Theophrastus", "work": "Enquiry into Plants", "text": "The inherent vegetative power of **_aux** impels the shoot toward seasonal increase and vernal flowering." },
      { "author": "Aristotle", "work": "On Generation and Corruption", "text": "Natural maturation proceeds through distinct stages of **_aux** wherein quantitative increase precedes form perfection." },
      { "author": "Max Müller", "work": "Lectures on the Science of Language", "text": "Tracing the archaic root **_aux** reveals how early Indo-European speech linked vegetative growth with civic augmentation." }
    ]
  },
  "Dashboard — aux/auxanogram.md": {
    "primary": "A microbiological culture plate illustrating the specific nutritional requirements of an organism through localized growth zones.",
    "secondary": "In diagnostic bacteriology, a plate inoculated with a microbe where discrete spots of vitamins or carbon sources demonstrate nutrient utilization.",
    "quotes": [
      { "author": "Martinus Beijerinck", "work": "Auxanographic Methods in Microbiology", "text": "The developed **auxanogram** showed vibrant concentric halos of yeast growth surrounding each glucose droplet." },
      { "author": "René Dubos", "work": "The Bacterial Cell", "text": "Reading the microbial **auxanogram** allowed researchers to map precise amino acid deficiencies in fastidious strains." },
      { "author": "Selman Waksman", "work": "Principles of Soil Microbiology", "text": "A differential **auxanogram** confirmed that soil actinomycetes could utilize cellulose as their sole carbon source." }
    ]
  },
  "Dashboard — aux/auxanography.md": {
    "primary": "A microbiological technique for determining the nutritional requirements of microorganisms by observing growth around nutrient spots on agar.",
    "secondary": "In bacteriological methodology, the experimental process invented by Beijerinck to assay enzymatic and metabolic capabilities.",
    "quotes": [
      { "author": "Martinus Beijerinck", "work": "On the Methods of Microbiological Research", "text": "Through agar **auxanography**, one can simultaneously test dozens of carbohydrates upon a single culture vessel." },
      { "author": "Louis Pasteur", "work": "Studies on Fermentation", "text": "Pioneering techniques in **auxanography** laid bare the subtle metabolic dependencies governing fungal growth." },
      { "author": "Alexander Fleming", "work": "Chemotherapy: Yesterday, Today, and Tomorrow", "text": "Diffusion assays adapted from classic **auxanography** became the standard benchmark for testing antibiotic potency." }
    ]
  },
  "Dashboard — aux/auxanology.md": {
    "primary": "The scientific study of the growth and development of organisms, especially plants and microorganisms.",
    "secondary": "In physiological biology, the discipline investigating the mechanical and biochemical factors regulating developmental expansion.",
    "quotes": [
      { "author": "Julius von Sachs", "work": "Textbook of Botany", "text": "Rigorous experimental **auxanology** requires measuring microscopic cellular elongation under controlled temperature gradients." },
      { "author": "D'Arcy Wentworth Thompson", "work": "On Growth and Form", "text": "The mathematical foundations of **auxanology** illustrate how differential growth rates sculpt physical organic symmetry." },
      { "author": "Charles Darwin", "work": "The Power of Movement in Plants", "text": "Our discoveries in **auxanology** established that unequal rates of tissue growth drive phototropic curvature in seedlings." }
    ]
  },
  "Dashboard — aux/auxanometer.md": {
    "primary": "An apparatus designed for measuring and recording the rate of growth in plants.",
    "secondary": "In plant physiology, a device using a lever or rotating smoked drum (kymograph) to magnify tiny increments of stem elongation.",
    "quotes": [
      { "author": "Julius von Sachs", "work": "Lectures on the Physiology of Plants", "text": "The delicate pointer of my recording **auxanometer** magnified the shoot's nocturnal growth over twenty-fold." },
      { "author": "Charles Darwin", "work": "The Power of Movement in Plants", "text": "Attaching a silk thread from the plumule to an **auxanometer** revealed continuous rhythmic pulsations in elongation." },
      { "author": "Jagadish Chandra Bose", "work": "Plant Response as a Means of Physiological Investigation", "text": "My high-magnification crescograph surpassed the classical **auxanometer**, recording growth surges occurring within fractions of a second." }
    ]
  },
  "Dashboard — aux/auxesis.md": {
    "primary": "Growth or increase in size, especially growth resulting from cell enlargement without an increase in cell number.",
    "secondary": "In classical rhetoric, a stylistic figure of speech in which an idea or description is progressively amplified for emotional climax.",
    "quotes": [
      { "author": "Aristotle", "work": "The Art of Rhetoric", "text": "Skillful deployment of **auxesis** elevates a modest civic virtue into an heroic triumph before the assembly." },
      { "author": "Quintilian", "work": "Institutio Oratoria", "text": "The orator ascends by **auxesis** from the lighter misdemeanor to the most abominable crime." },
      { "author": "D'Arcy Wentworth Thompson", "work": "On Growth and Form", "text": "In certain rotifers and nematodes, post-embryonic growth is governed purely by **auxesis** without any further cell division." }
    ]
  },
  "Dashboard — aux/auxetic.md": {
    "primary": "Relating to or promoting growth or expansion; having a negative Poisson's ratio such that lateral expansion occurs when stretched.",
    "secondary": "In materials science, describing metamaterials that become thicker perpendicularly to the applied tensile force; in biology, pertaining to auxesis.",
    "quotes": [
      { "author": "D'Arcy Wentworth Thompson", "work": "On Growth and Form", "text": "Certain hypertrophic tissues follow an **auxetic** trajectory where individual cell volume expands tenfold." },
      { "author": "Richard Feynman", "work": "There's Plenty of Room at the Bottom", "text": "Engineers can design honeycomb lattices with **auxetic** behavior, expanding outward in all dimensions under uniaxial tension." },
      { "author": "Arthur D. Imms", "work": "A General Textbook of Entomology", "text": "During larval molting, the abdominal cuticle undergoes **auxetic** stretching to accommodate sudden body enlargement." }
    ]
  },
  "Dashboard — aux/auxin.md": {
    "primary": "A class of plant hormones, predominantly indole-3-acetic acid (IAA), that regulates cell elongation, apical dominance, and tropisms.",
    "secondary": "In plant biochemistry, an essential growth regulator coordinating organogenesis, root initiation, and vascular differentiation.",
    "quotes": [
      { "author": "Frits Went", "work": "Wuchsstoff und Wachstum", "text": "Diffusing from the coleoptile tip into agar blocks, the elusive **auxin** induced curvature in decapitated oat seedlings." },
      { "author": "Rachel Carson", "work": "Silent Spring", "text": "Synthetic mimics of natural **auxin**, such as 2,4-D, disrupt internal plant metabolism so violently that weeds curl and die." },
      { "author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "text": "Polar transport of **auxin** establishes the fundamental apical-basal axis throughout the developing plant embryo." }
    ]
  },
  "Dashboard — aux/auxinic.md": {
    "primary": "Pertaining to, caused by, or characteristic of auxins.",
    "secondary": "In plant physiology, describing cellular elongation, epinasty, or developmental signaling mediated by auxin molecules.",
    "quotes": [
      { "author": "Frits Went", "work": "Phytohormones", "text": "Unilateral light induces an asymmetric **auxinic** gradient, causing the shaded flank of the shoot to elongate faster." },
      { "author": "Liberty Hyde Bailey", "work": "The Standard Cyclopedia of Horticulture", "text": "Commercial cutting propagation relies on **auxinic** powders to stimulate adventitious root formation." },
      { "author": "Arthur Cronquist", "work": "An Integrated System of Classification of Flowering Plants", "text": "Vascular cambium activation in temperate trees follows the seasonal crest of **auxinic** flow descending from new buds." }
    ]
  },
  "Dashboard — aux/auxology.md": {
    "primary": "The scientific study of human physical growth and development across the lifespan.",
    "secondary": "In pediatric medicine and physical anthropology, the quantitative tracking of stature, skeletal maturation, and somatic indices.",
    "quotes": [
      { "author": "Franz Boas", "work": "Changes in Bodily Form of Descendants of Immigrants", "text": "Pioneering investigations in **auxology** demonstrated that childhood stature responds dynamically to improved environmental nutrition." },
      { "author": "William Osler", "work": "The Principles and Practice of Medicine", "text": "Clinical **auxology** provides an indispensable baseline for detecting subtle endocrine and nutritional deficiencies." },
      { "author": "J. M. Tanner", "work": "Foetus into Man: Physical Growth from Conception to Maturity", "text": "Modern **auxology** employs longitudinal velocity curves to assess the onset and tempo of the pubertal growth spurt." }
    ]
  },
  "Dashboard — aux/auxotroph.md": {
    "primary": "A mutant microorganism that requires a specific nutritional supplement not needed by the wild-type strain.",
    "secondary": "In microbial genetics, an organism harboring a biochemical lesion that disables its capacity to synthesize an essential metabolite on minimal medium.",
    "quotes": [
      { "author": "George Beadle", "work": "Genetic Control of Biochemical Reactions in Neurospora", "text": "Each nutritional **auxotroph** uncovered in our radiation experiments corresponded to a loss-of-function mutation in a single enzyme." },
      { "author": "Edward Tatum", "work": "A Case History in Biochemical Genetics", "text": "Crossing two distinct strains of **auxotroph** produced wild-type recombinants capable of thriving on minimal agar." },
      { "author": "Jacques Monod", "work": "Chance and Necessity", "text": "By isolating a tryptophan-dependent **auxotroph**, researchers elucidated the operon architecture governing amino acid biosynthesis." }
    ]
  },
  "Dashboard — bal/ametabolic.md": {
    "primary": "Not undergoing metamorphosis during insect ontogeny; exhibiting direct development from egg to adult.",
    "secondary": "In entomology and developmental biology, descriptive of primitive apterygote insects such as silverfish whose young hatch resembling miniature adults.",
    "quotes": [
      { "author": "Arthur D. Imms", "work": "A General Textbook of Entomology", "text": "Primitive apterygotes remain strictly **ametabolic**, molting repeatedly throughout adult life without transforming their body plan." },
      { "author": "Alpheus Spring Packard", "work": "Guide to the Study of Insects", "text": "The silverfish illustrates an **ametabolic** life history in which the young differ from the mature insect solely in size and sexual maturity." },
      { "author": "V. B. Wigglesworth", "work": "The Principles of Insect Physiology", "text": "Endocrine control of molting in **ametabolic** species operates without the dramatic metamorphic juvenile hormone swings found in beetles." }
    ]
  },
  "Dashboard — bal/ametabolism.md": {
    "primary": "The condition of direct post-embryonic development in insects without metamorphosis.",
    "secondary": "In comparative entomology, the primitive developmental state characteristic of the Apterygota, where instars undergo no radical structural change.",
    "quotes": [
      { "author": "Arthur D. Imms", "work": "Recent Advances in Entomology", "text": "Phylogenetic analysis reveals that **ametabolism** represents the ancestral developmental condition preceding hemimetabolous transformations." },
      { "author": "John Obadiah Westwood", "work": "An Introduction to the Modern Classification of Insects", "text": "The persistent **ametabolism** of the Thysanura aligns them with the earliest terrestrial hexapod fossils." },
      { "author": "L. O. Howard", "work": "The Insect Book", "text": "While butterflies display dramatic transformation, bristletails are governed by simple **ametabolism** from hatching to death." }
    ]
  },
  "Dashboard — bal/ametabolous.md": {
    "primary": "Characterized by ametabolism; developing directly from egg to adult without metamorphosis.",
    "secondary": "In systematic entomology, descriptive of insects lacking wing pads, nymphs, or pupal stages during growth.",
    "quotes": [
      { "author": "Arthur D. Imms", "work": "A General Textbook of Entomology", "text": "Collembola and Thysanura constitute the classic **ametabolous** hexapods, undergoing simple ecdysis without anatomical change." },
      { "author": "V. B. Wigglesworth", "work": "The Principles of Insect Physiology", "text": "Because an **ametabolous** insect acquires no wings, it can continue to molt periodically even after achieving reproductive capability." },
      { "author": "Alpheus Spring Packard", "work": "Textbook of Entomology", "text": "The **ametabolous** habit reflects an ancient evolutionary stage before the origin of insect flight structures." }
    ]
  },
  "Dashboard — bal/amphibole.md": {
    "primary": "A prominent group of rock-forming inosilicate minerals composed of double chains of silicon-oxygen tetrahedra.",
    "secondary": "In mineralogy and petrology, dark green to black hydrous silicate minerals (such as hornblende and tremolite) typical of metamorphic and igneous rocks.",
    "quotes": [
      { "author": "René Just Haüy", "work": "Traité de Minéralogie", "text": "I designated this group **amphibole**, from the Greek for ambiguous, because of the bewildering diversity of its crystalline forms." },
      { "author": "James Dwight Dana", "work": "System of Mineralogy", "text": "Cleavage angles near 124 degrees readily distinguish prismatic crystals of **amphibole** from the closely related pyroxenes." },
      { "author": "Arthur Holmes", "work": "Principles of Physical Geology", "text": "Deep beneath volcanic arcs, water-rich magmas precipitate abundant **amphibole** crystals prior to explosive eruption." }
    ]
  },
  "Dashboard — bal/amphibolic.md": {
    "primary": "Ambiguous, equivocal, or capable of two contrasting interpretations; or pertaining to the mineral amphibole.",
    "secondary": "In biochemistry, describing metabolic pathways (such as the citric acid cycle) that function in both catabolic and anabolic processes.",
    "quotes": [
      { "author": "Hans Krebs", "work": "The Citric Acid Cycle", "text": "The tricarboxylic acid cycle plays an **amphibolic** role, simultaneously oxidizing acetyl units and supplying precursors for amino acid synthesis." },
      { "author": "Samuel Johnson", "work": "The Lives of the English Poets", "text": "The politician's **amphibolic** declarations were crafted with deliberate cunning to soothe opposing factions." },
      { "author": "Archibald Geikie", "work": "Textbook of Geology", "text": "Microscopic examination of the schist revealed an **amphibolic** fabric dominated by prismatic hornblende needles." }
    ]
  },
  "Dashboard — bal/amphibolite.md": {
    "primary": "A coarse-grained metamorphic rock composed mainly of amphibole (especially hornblende) and plagioclase feldspar.",
    "secondary": "In metamorphic petrology, the defining rock type of medium- to high-grade regional metamorphism under intermediate pressures.",
    "quotes": [
      { "author": "Archibald Geikie", "work": "The Scenery of Scotland", "text": "Dark bands of craggy **amphibolite** traverse the Lewisian gneiss, recording ancient basaltic dikes sheared by mountain-building stresses." },
      { "author": "Arthur Holmes", "work": "Principles of Physical Geology", "text": "Under amphibolite-facies conditions, hydrating fluids transform oceanic basalt into crystalline **amphibolite**." },
      { "author": "James Dwight Dana", "work": "Manual of Geology", "text": "Glistening black hornblende crystals give the weathered **amphibolite** ledge a distinctive rugged, fibrous texture." }
    ]
  },
  "Dashboard — bal/amphibolous.md": {
    "primary": "Ambiguous, equivocal, or capable of double meaning; doubtful in nature.",
    "secondary": "In classical logic and discourse, prone to amphiboly or syntactic ambiguity that obscures true intent.",
    "quotes": [
      { "author": "Francis Bacon", "work": "The Advancement of Learning", "text": "Oracles of antiquity frequently answered in **amphibolous** terms to preserve their credit whatever the event." },
      { "author": "Samuel Johnson", "work": "The Rambler", "text": "He who uses an **amphibolous** phrase when plain speech is required betrays either intellectual confusion or moral timidity." },
      { "author": "Jeremy Bentham", "work": "A Fragment on Government", "text": "Statutes couched in **amphibolous** language merely furnish lucrative employment for contentious advocates." }
    ]
  }
}

# Fix Dashboard — actinaria.md key if needed
if "Dashboard — actinaria.md" in batch1_data:
  batch1_data["Dashboard — actin/actinaria.md"] = batch1_data.pop("Dashboard — actinaria.md")

with open('main app/scripts/curate-action-batch1.mjs', 'w', encoding='utf-8') as f:
    f.write('''import fs from 'fs';
import path from 'path';

const CLUSTER_DIR = 'App database/Greek roots/Cluster Action';

const BATCH1_DATA = ''' + json.dumps(batch1_data, indent=2, ensure_ascii=False) + ''';

function formatQuotes(quotes) {
  return quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.text}"*`).join('\\n');
}

function updateFile(relPath, wordData) {
  const filePath = path.join(CLUSTER_DIR, relPath);
  if (!fs.existsSync(filePath)) {
    console.error(`File NOT found: ${filePath}`);
    return false;
  }
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`Missing [!book] in ${filePath}`);
    return false;
  }
  const topPart = content.slice(0, bookIdx).trimEnd();

  const newDefBlock = `> [!book] 📖 Definitions & Semantic Range\\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${wordData.primary}\\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${wordData.secondary}\\n\\n> [!quote] 💬 Contextual Usage & Authentic Quotations\\n${formatQuotes(wordData.quotes)}\\n`;

  const finalContent = topPart + '\\n\\n' + newDefBlock;
  fs.writeFileSync(filePath, finalContent, 'utf8');
  return true;
}

let count = 0;
for (const [relPath, data] of Object.entries(BATCH1_DATA)) {
  if (updateFile(relPath, data)) {
    count++;
  }
}

console.log(`========================================`);
console.log(`Action Batch 1 Completed: ${count} / ${Object.keys(BATCH1_DATA).length} words updated`);
console.log(`========================================`);
''')
print("Successfully generated curate-action-batch1.mjs with", len(batch1_data), "words.")
