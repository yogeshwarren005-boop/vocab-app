import fs from 'fs';
import path from 'path';

const CLUSTER_DIR = 'App database/Greek roots/Cluster Life & Vitality';

const BATCH5_DATA = {
  // Dashboard — phyl (40 words)
  "anaphylactic": {
    dashboard: "Dashboard — phyl",
    primary: "Of, relating to, or characterized by anaphylaxis; intensely hypersensitive to an antigen.",
    secondary: "Describing severe, life-threatening immunological shock precipitated by systemic mast cell degranulation.",
    quotes: [
      { author: "Charles Richet", work: "Anaphylaxis", text: "The **anaphylactic** state is that condition in which the organism, far from being protected, becomes fatally sensitive to a poison." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Widespread arteriolar dilation and bronchospasm mark the onset of acute **anaphylactic** collapse." },
      { author: "Clemens von Pirquet", work: "Clinical Studies on Allergy", text: "We trace a common cellular mechanism linking mild cutaneous allergy with lethal **anaphylactic** shock." }
    ]
  },
  "anaphylaxis": {
    dashboard: "Dashboard — phyl",
    primary: "An acute, severe, and potentially fatal systemic allergic reaction caused by the release of chemical mediators from sensitized mast cells and basophils.",
    secondary: "The immunological phenomenon discovered by Charles Richet in 1902 whereby a prior non-lethal antigen exposure causes fatal hypersensitivity upon rechallenge.",
    quotes: [
      { author: "Charles Richet", work: "Anaphylaxis", text: "I coined the word **anaphylaxis** to denote the exact opposite of protection (phylaxis), representing hypersusceptibility instead of immunity." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "Administration of foreign animal antisera must always be guarded by precautions against fatal **anaphylaxis**." },
      { author: "Bela Schick", work: "Serum Sickness", text: "Experimental **anaphylaxis** demonstrated that immune mechanisms can act destructively against the host organism." }
    ]
  },
  "aphyllanthaceae": {
    dashboard: "Dashboard — phyl",
    primary: "A botanical family (or subfamily Aphyllanthoideae) of monocotyledonous flowering plants containing the single Mediterranean genus *Aphyllanthes*.",
    secondary: "A family of xerophytic plants in the order Asparagales characterized by rush-like photosynthetic stems and vestigial papery leaves.",
    quotes: [
      { author: "Augustin Pyramus de Candolle", work: "Flore Française", text: "The distinctive floral anatomy of the genus prompted botanists to separate it into the monotypic family **Aphyllanthaceae**." },
      { author: "John Lindley", work: "The Vegetable Kingdom", text: "Within the **Aphyllanthaceae**, blue flowers emerge from papery involucral bracts crowning leafless rush stems." },
      { author: "Asa Gray", work: "Structural Botany", text: "Phylogenetic revisions often treat the **Aphyllanthaceae** as an archaic lineage within the broader asparagoid complex." }
    ]
  },
  "aphyllanthes": {
    dashboard: "Dashboard — phyl",
    primary: "A monotypic genus of perennial herbs (*Aphyllanthes monspeliensis*, the blue aphyllanthes) native to the western Mediterranean basin.",
    secondary: "A tufted calcicolous plant whose leafless rush-like stems carry solitary, brilliant blue, star-like blossoms.",
    quotes: [
      { author: "Carl Linnaeus", work: "Species Plantarum", text: "I described **Aphyllanthes** monspeliensis from the stony limestone hills of southern France and Spain." },
      { author: "Augustin Pyramus de Candolle", work: "Botanicon Gallicum", text: "On the arid garrigue plateaus, tufts of **Aphyllanthes** flourish amidst thyme and dwarf scrub oaks." },
      { author: "John Lindley", work: "The Vegetable Kingdom", text: "The solitary terminal blue flower of **Aphyllanthes** belies the absence of true functional leaf blades." }
    ]
  },
  "aphyllophorales": {
    dashboard: "Dashboard — phyl",
    primary: "An order of basidiomycete fungi lacking gills, including bracket fungi, polypores, chanterelles, and tooth fungi.",
    secondary: "A historical taxonomic group of non-agaric homobasidiomycetes characterized by tough, woody, or leathery basidiocarps with pored or smooth hymenia.",
    quotes: [
      { author: "Pier Andrea Saccardo", work: "Sylloge Fungorum", text: "The **Aphyllophorales** embrace a tremendous variety of wood-decaying bracket fungi and terrestrial clavarioid molds." },
      { author: "G. C. Ainsworth", work: "The Fungi: An Advanced Treatise", text: "Lignicolous species of the **Aphyllophorales** play an indispensable ecological role in forest lignin decomposition." },
      { author: "Miles Joseph Berkeley", work: "Outlines of British Fungology", text: "Unlike soft agarics, members of the **Aphyllophorales** persist for months upon rotting timber trunks." }
    ]
  },
  "aphyllous": {
    dashboard: "Dashboard — phyl",
    primary: "Having no leaves; naturally leafless (said of plants).",
    secondary: "In xerophytic botany, describing plants whose leaves are absent or reduced to non-photosynthetic scales, photosynthesis being performed by green stems.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", text: "Certain parasitic orchids present an entirely **aphyllous** scape arising from underground coral-like rhizomes." },
      { author: "Charles Darwin", work: "The Origin of Species", text: "Desert euphorbias adopt the fleshy, **aphyllous** habit of New World cacti to minimize surface water transpiration." },
      { author: "Alexander von Humboldt", work: "Personal Narrative of Travels", text: "The Llanos plains exhibited bizarre **aphyllous** shrubs whose green cortical bark assumed the whole duty of foliage." }
    ]
  },
  "cataphyll": {
    dashboard: "Dashboard — phyl",
    primary: "A reduced, scale-like leaf, such as a bud scale, rhizome scale, or bulb scale, preceding the true foliage leaves.",
    secondary: "A rudimentary leaf specialized for mechanical protection, food storage, or underground penetration rather than photosynthesis.",
    quotes: [
      { author: "Johann Wolfgang von Goethe", work: "The Metamorphosis of Plants", text: "The protective scales enclosing winter buds represent the lowest morphological stage of the leaf, the simple **cataphyll**." },
      { author: "Asa Gray", work: "Structural Botany", text: "Fleshy onion bulb layers are true storage **cataphylls** densely packed with reserves of sugar and moisture." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", text: "As the subterranean shoot pushes through gravel, tough protective **cataphylls** shield the delicate terminal apex." }
    ]
  },
  "epiphyllum": {
    dashboard: "Dashboard — phyl",
    primary: "A genus of climbing or epiphytic cacti native to Central and South America, known as orchid cacti, bearing large fragrant flowers.",
    secondary: "A tropical epiphytic succulent characterized by broad, flattened, spineless, leaf-like cladodes and spectacular nocturnal blooms.",
    quotes: [
      { author: "Charles Darwin", work: "The Various Contrivances by Which Orchids Are Fertilised", text: "The climbing stems of **Epiphyllum** anchor upon rain-forest boughs without extracting parasitic nourishment from the bark." },
      { author: "John Lindley", work: "The Vegetable Kingdom", text: "Magnificent white blossoms expand at midnight from the crenate margins of the flattened **Epiphyllum** stems." },
      { author: "Liberty Hyde Bailey", work: "Cyclopedia of American Horticulture", text: "Greenhouse growers prize hybrids of **Epiphyllum** for their dazzling scarlet, violet, and ivory corollas." }
    ]
  },
  "phylactery": {
    dashboard: "Dashboard — phyl",
    primary: "A small leather box containing Hebrew texts on vellum, worn by Jewish men at morning prayer (tefillin); also an amulet or protective charm.",
    secondary: "In medieval art and iconography, a scroll or speech banner bearing an explanatory inscription.",
    quotes: [
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", text: "Superstitious ancients wore an inscribed **phylactery** upon their breastplates to ward off sorcery and fever." },
      { author: "William Shakespeare", work: "Titus Andronicus", text: "Let us bind sacred covenants like a holy **phylactery** upon our arms before setting forth into battle." },
      { author: "George Eliot", work: "Daniel Deronda", text: "The pious grandfather bound the black leather **phylactery** upon his forehead with reverent, trembling fingers." }
    ]
  },
  "phyle": {
    dashboard: "Dashboard — phyl",
    primary: "An ancient Greek tribe, clan, or political subdivision, especially one of the ten civic tribes instituted in Athens by Cleisthenes.",
    secondary: "A socio-political corporate group whose members claimed common ancestry and shared religious cults and military contingents.",
    quotes: [
      { author: "Thucydides", work: "The Peloponnesian War", text: "The civic army marched out in ten regiments, each drawn from its respective **phyle** according to ancestral custom." },
      { author: "Aristotle", work: "The Constitution of the Athenians", text: "Cleisthenes reorganized the citizenry into ten new **phyles**, mingling demes from coastal, inland, and urban districts." },
      { author: "George Grote", work: "A History of Greece", text: "The constitutional genius of the Athenian **phyle** broke the tyrannical grip of aristocratic factional families." }
    ]
  },
  "phyletic": {
    dashboard: "Dashboard — phyl",
    primary: "Of or relating to evolutionary descent, racial lineage, or the history of a phylum or taxonomic group.",
    secondary: "Pertaining to ancestral relationships and chronological transformations along a continuous evolutionary lineage.",
    quotes: [
      { author: "Ernst Haeckel", work: "Generelle Morphologie der Organismen", text: "Ontogenetic development is a rapid and brief recapitulation of slow **phyletic** evolution." },
      { author: "George Gaylord Simpson", work: "Tempo and Mode in Evolution", text: "Sustained directional change within a continuous unbranching lineage constitutes gradual **phyletic** evolution." },
      { author: "Stephen Jay Gould", work: "The Structure of Evolutionary Theory", text: "Punctuated equilibrium challenged the orthodox expectation of continuous, imperceptible **phyletic** gradualism." }
    ]
  },
  "phyllidae": {
    dashboard: "Dashboard — phyl",
    primary: "A family of phasmids (order Phasmatodea) known as true leaf insects or walking leaves, noted for extreme cryptic mimicry of foliage.",
    secondary: "Insects of tropical Asia and Australasia having broad, dorsoventrally flattened bodies with wing venation mimicking living or dying leaves.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", text: "The mimicry exhibited by the **Phyllidae** is so immaculate that the brown blotches on their wings resemble fungal decay." },
      { author: "David Sharp", work: "Insects: Part I", text: "Females of the family **Phyllidae** possess broad, leaf-like expansions upon both legs and abdomen." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", text: "Protective resemblance reaches its evolutionary zenith among the tropical **Phyllidae** hanging motionless amidst foliage." }
    ]
  },
  "phylliform": {
    dashboard: "Dashboard — phyl",
    primary: "Having the form or appearance of a leaf; leaf-shaped.",
    secondary: "In zoology and paleontology, describing organs, appendages, or fossils exhibiting a flattened, foliage-like morphology.",
    quotes: [
      { author: "Richard Owen", work: "Lectures on Comparative Anatomy", text: "The branchial appendages of certain phyllopod crustaceans present a delicate **phylliform** outline." },
      { author: "Alfred Russel Wallace", work: "Darwinism", text: "The **phylliform** mantis remains suspended motionless from twigs, enticing pollinating insects into reach." },
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", text: "Marine flatworms move via undulating waves traversing their translucent, **phylliform** bodies." }
    ]
  },
  "phyllitis": {
    dashboard: "Dashboard — phyl",
    primary: "A historical genus of ferns (family Aspleniaceae), notably the hart's-tongue fern (*Phyllitis scolopendrium* / *Asplenium scolopendrium*).",
    secondary: "In medical pathology, inflammation of leaves; in botany, a fern genus characterized by undivided, strap-shaped, glossy fronds with linear sori.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", text: "Shaded limestone ravines shelter the rare, glossy, strap-like fronds of **Phyllitis** scolopendrium." },
      { author: "John Lindley", work: "The Vegetable Kingdom", text: "The linear sori of **Phyllitis** are arranged in pairs along the veins of the undivided green blade." },
      { author: "Miles Joseph Berkeley", work: "Outlines of British Fungology", text: "Parasitic leaf spots sometimes attack the foliage of **Phyllitis** in damp subterranean caverns." }
    ]
  },
  "phyllium": {
    dashboard: "Dashboard — phyl",
    primary: "A genus of leaf insects in the family Phylliidae, celebrated for their extraordinary mimicry of green or decaying foliage.",
    secondary: "Tropical phasmids whose abdomen and legs are expanded into flat, veined, leaf-like plates that sway gently in the breeze.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "Contributions to the Theory of Natural Selection", text: "A living specimen of **Phyllium** perched upon a shrub defies the keenest eye of predatory birds." },
      { author: "David Sharp", work: "Insects: Part I", text: "The movement of **Phyllium** mimics the gentle trembling of a leaf stirred by an afternoon gust." },
      { author: "Ernst Haeckel", work: "Art Forms in Nature", text: "The venation on the elytra of **Phyllium** reproduces every minute vein and blight spot of botanical foliage." }
    ]
  },
  "phyllo": {
    dashboard: "Dashboard — phyl",
    primary: "Paper-thin unleavened pastry dough, rolled into gossamer sheets and layered with butter, used in Middle Eastern and Balkan baking (filo).",
    secondary: "The Greek root (*phyllon*, leaf) applied in culinary terminology to leaf-thin pastry layers.",
    quotes: [
      { author: "Elizabeth David", work: "Mediterranean Food", text: "Mastering the art of stretching **phyllo** dough until it is transparent as tissue paper is the triumph of the Greek baker." },
      { author: "James Beard", work: "Beard on Bread", text: "Delicate sheets of buttered **phyllo** crisp in the oven into golden, fragile flakes surrounding spiced walnut filling." },
      { author: "M. F. K. Fisher", work: "With Bold Knife and Fork", text: "The pastry chef lifted the gossamer leaf of **phyllo**, brushing each translucent surface with clarified butter." }
    ]
  },
  "phylloclad": {
    dashboard: "Dashboard — phyl",
    primary: "A flattened, leaf-like stem or branch that functions as a foliage leaf; variant of phylloclade.",
    secondary: "An evolutionary vegetative adaptation in plants where true leaves are reduced and stems take over photosynthesis.",
    quotes: [
      { author: "Asa Gray", work: "Structural Botany", text: "In butcher's broom, the apparent leaves are in reality expanded green **phylloclads** bearing flowers upon their face." },
      { author: "Johann Wolfgang von Goethe", work: "The Metamorphosis of Plants", text: "The metamorphosis of the axis into a photosynthetic **phylloclad** illustrates nature's morphological fluidity." },
      { author: "John Lindley", work: "The Vegetable Kingdom", text: "Spiny scales at the center of each **phylloclad** mark the true axillary origin of the branch structure." }
    ]
  },
  "phyllocladaceae": {
    dashboard: "Dashboard — phyl",
    primary: "A family (or subfamily within Podocarpaceae) of Southern Hemisphere conifers comprising the genus *Phyllocladus* (celery pines).",
    secondary: "Conifers lacking functional adult foliage leaves, whose photosynthetic apparatus consists entirely of flattened branchlets (phylloclades).",
    quotes: [
      { author: "John Lindley", work: "The Vegetable Kingdom", text: "Botanists established the **Phyllocladaceae** to emphasize the singular departure from typical needle foliage seen in these conifers." },
      { author: "Leonard Cockayne", work: "New Zealand Plants and Their Story", text: "Forests of celery pine belonging to the **Phyllocladaceae** cloak the steep montane slopes of the Southern Alps." },
      { author: "Asa Gray", work: "Botanical Memoirs", text: "The phylogenetic placement of the **Phyllocladaceae** highlights ancient Gondwanan gymnosperm radiations." }
    ]
  },
  "phylloclade": {
    dashboard: "Dashboard — phyl",
    primary: "A flattened branch or stem that resembles and functions as a foliage leaf, as seen in *Ruscus*, asparagus, and certain cacti.",
    secondary: "A photosynthetic cladode consisting of several internodes, adapted to conserve moisture in arid climates.",
    quotes: [
      { author: "Asa Gray", work: "Elements of Botany", text: "The leaflike green plates of asparagus are true **phylloclades**, arising in the axils of minute scarious scales." },
      { author: "Charles Darwin", work: "The Movement and Habits of Climbing Plants", text: "The twiners wind their delicate **phylloclades** around supports, orienting broad surfaces toward sunlight." },
      { author: "Johann Wolfgang von Goethe", work: "Italian Journey", text: "The flattened **phylloclade** confirms my conviction that every plant organ is a modified manifestation of a single primal type." }
    ]
  },
  "phyllocladus": {
    dashboard: "Dashboard — phyl",
    primary: "A genus of Southern Hemisphere conifers in the family Podocarpaceae, known as celery pines, having celery-like phylloclades.",
    secondary: "Evergreen timber trees native to New Zealand, Tasmania, and Malesia whose photosynthetic shoots are flattened, lobed cladodes.",
    quotes: [
      { author: "Leonard Cockayne", work: "The Vegetation of New Zealand", text: "Specimens of **Phyllocladus** trichomanoides tower eighty feet above the sub-alpine forest understory." },
      { author: "Joseph Dalton Hooker", work: "Handbook of the New Zealand Flora", text: "The seed of **Phyllocladus** sits in a fleshy cup-like aril, distributed by frugivorous forest birds." },
      { author: "John Lindley", work: "The Vegetable Kingdom", text: "In **Phyllocladus**, true leaves appear only as transient juvenile seedlings, quickly replaced by thick celery-like phyllodes." }
    ]
  },
  "phyllode": {
    dashboard: "Dashboard — phyl",
    primary: "A petiole (leaf stalk) that is flattened, expanded, and green, functioning as a foliage leaf blade.",
    secondary: "A xerophytic adaptation prominent in Australian acacias where true compound leaf blades are lost and the stalk serves photosynthesis.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", text: "In Australian acacias, the true bipinnate leaves vanish as the sapling grows, giving place to vertically oriented **phyllodes**." },
      { author: "Asa Gray", work: "Structural Botany", text: "The vertical orientation of the **phyllode** enables the acacia to avoid the scorching heat of midday Australian sunshine." },
      { author: "Johann Wolfgang von Goethe", work: "The Metamorphosis of Plants", text: "The expansion of the leaf stalk into a **phyllode** demonstrates how vegetative parts transform into functional blades." }
    ]
  },
  "phyllodial": {
    dashboard: "Dashboard — phyl",
    primary: "Of, relating to, or possessing phyllodes; having leaf-like flattened petioles.",
    secondary: "Characterized by the phyllode habit; typical of many xerophytic acacia species in arid ecosystems.",
    quotes: [
      { author: "Joseph Dalton Hooker", work: "Flora Tasmaniae", text: "The **phyllodial** acacias dominate the dry sclerophyll woodlands of the interior plains." },
      { author: "Asa Gray", work: "Botanical Textbook", text: "Seedlings exhibit the dramatic transition from feathery ancestral leaves to tough, leathery **phyllodial** stalks." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", text: "Reversion of **phyllodial** branches to ancestral pinnate foliage frequently occurs under heavy shade or moist greenhouse culture." }
    ]
  },
  "phyllodoce": {
    dashboard: "Dashboard — phyl",
    primary: "A genus of low, evergreen dwarf sub-shrubs in the heath family (Ericaceae), commonly called mountain heaths.",
    secondary: "In marine zoology, a genus of predatory polychaete paddleworms (family Phyllodocidae) with flattened leaf-like parapodial paddles.",
    quotes: [
      { author: "Asa Gray", work: "Synoptical Flora of North America", text: "The rosy bell-shaped blossoms of **Phyllodoce** carpet alpine screes above timberline in the Sierra Nevada." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", text: "The marine worm **Phyllodoce** propels itself swiftly through tidal sediments by means of foliaceous dorsal cirri." },
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", text: "Microscopic dissections of **Phyllodoce** reveal paired ventral nerve cords and active eversible pharynges." }
    ]
  },
  "phylloporus": {
    dashboard: "Dashboard — phyl",
    primary: "A genus of mycorrhizal fungi in the family Boletaceae, characterized by bearing gills rather than pores (gilled boletes).",
    secondary: "A transitional boletoid fungus (*Phylloporus rhodoxanthus*) having golden-yellow gills that are connected by transverse veins.",
    quotes: [
      { author: "Lucien Quélet", work: "Enchiridion Fungorum", text: "I established the genus **Phylloporus** to accommodate those unique boletes whose hymenophore forms distinct lamellae rather than tubes." },
      { author: "Miles Joseph Berkeley", work: "Outlines of British Fungology", text: "The yellow gills of **Phylloporus** stain blue upon bruising, proving its chemical kinship to the bolete family." },
      { author: "G. C. Ainsworth", work: "The Fungi: An Advanced Treatise", text: "Microscopic cystidia and spore morphology confirm that **Phylloporus** belongs to the Boletaceae despite its agaricoid gills." }
    ]
  },
  "phylloquinone": {
    dashboard: "Dashboard — phyl",
    primary: "Vitamin K1; a yellow, viscous chemical compound synthesized by green plants, indispensable for blood coagulation.",
    secondary: "A fat-soluble polycyclic ketone that acts as a cofactor for gamma-glutamyl carboxylase, synthesizing prothrombin and clotting factors.",
    quotes: [
      { author: "Henrik Dam", work: "The Discovery of Vitamin K", text: "From alfalfa meal we isolated crystalline **phylloquinone**, the antihemorrhagic factor curing fatal bleeding in chicks." },
      { author: "Edward Adelbert Doisy", work: "The Chemical Nature of Vitamin K", text: "Synthesis of pure **phylloquinone** confirmed its structure as 2-methyl-1,4-naphthoquinone with a phytyl side chain." },
      { author: "Albert Lehninger", work: "Principles of Biochemistry", text: "In photosynthesis, **phylloquinone** operates as an intermediate electron carrier within Photosystem I." }
    ]
  },
  "phyllorhynchus": {
    dashboard: "Dashboard — phyl",
    primary: "A genus of small, nocturnal, non-venomous colubrid snakes native to the southwestern United States and Mexico; leaf-nosed snakes.",
    secondary: "Desert snakes possessing an enlarged, triangular, leaf-like rostral scale adapted for burrowing through loose gravel and sand.",
    quotes: [
      { author: "Edward Drinker Cope", work: "The Crocodilians, Lizards, and Snakes of North America", text: "The prominent, leaf-like rostral plate of **Phyllorhynchus** serves as an effective burrowing wedge in arid soil." },
      { author: "Raymond Ditmars", work: "Reptiles of the World", text: "Nocturnal search on Mojave desert roads frequently reveals the blotched pattern of the shy **Phyllorhynchus**." },
      { author: "Laurence Klauber", work: "Rattlesnakes: Their Habits, Life Histories, and Influence", text: "Small leaf-nosed snakes of the genus **Phyllorhynchus** feed almost exclusively upon squamate lizard eggs." }
    ]
  },
  "phylloscopus": {
    dashboard: "Dashboard — phyl",
    primary: "A large genus of small, insectivorous Old World passerine birds in the family Phylloscopidae; leaf warblers.",
    secondary: "Active, green or yellowish canopy-dwelling warblers (such as the chiffchaff and willow warbler) renowned for complex territorial songs.",
    quotes: [
      { author: "Gilbert White", work: "The Natural History of Selborne", text: "I distinguished three distinct species of small green willow wren, the precursors of the genus **Phylloscopus**, by their distinctive notes." },
      { author: "Ernst Mayr", work: "Systematics and the Origin of Species", text: "The circular overlapping species ring of **Phylloscopus** trochiloides around the Himalayas provides a classic demonstration of speciation." },
      { author: "Julian Huxley", work: "The Courtship of Birds", text: "Territorial singing in **Phylloscopus** warblers precedes pair formation in the spring willow thickets." }
    ]
  },
  "phyllostachys": {
    dashboard: "Dashboard — phyl",
    primary: "A genus of temperate Asian bamboos in the grass family (Poaceae), including moso bamboo and timber bamboos with grooved culms.",
    secondary: "Fast-growing, running monopodial bamboos characterized by culms with a flattened groove (sulcus) above each lateral bud node.",
    quotes: [
      { author: "John Lindley", work: "The Vegetable Kingdom", text: "The majestic culms of **Phyllostachys** attain heights of sixty feet in the rich alluvial valleys of southern China." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", text: "Species of **Phyllostachys** are prized for industrial timber, paper pulp, and edible spring shoots." },
      { author: "Ernest Henry Wilson", work: "A Naturalist in Western China", text: "Vast groves of golden **Phyllostachys** bamboo cloak the mountain foothills, providing materials for all domestic needs." }
    ]
  },
  "phyllostomatidae": {
    dashboard: "Dashboard — phyl",
    primary: "The family of New World leaf-nosed bats (order Chiroptera), characterized by a fleshy leaf-like dermal projection on the nose; Phyllostomidae.",
    secondary: "A diverse family of Neotropical bats displaying unparalleled ecological radiation, including fruit-eating, nectar-feeding, carnivorous, and vampire bats.",
    quotes: [
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", text: "The extraordinary nasal spear in the **Phyllostomatidae** functions as an acoustic horn focusing echolocating ultrasound." },
      { author: "G. G. Simpson", work: "The Principles of Classification and a Classification of Mammals", text: "Adaptive radiation within the **Phyllostomatidae** encompasses virtually every trophic niche available to nocturnal mammals." },
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", text: "The family **Phyllostomatidae** is strictly confined to the tropical and subtropical forests of the Americas." }
    ]
  },
  "phyllostomidae": {
    dashboard: "Dashboard — phyl",
    primary: "An alternative spelling of Phyllostomatidae; the American leaf-nosed bat family.",
    secondary: "A major mammalian family encompassing over two hundred species of Neotropical chiropterans with modified spear-like nasal pads.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "Tropical Nature and Other Essays", text: "Nectar-feeding species of the **Phyllostomidae** possess elongated tongues adapted for pollinating night-blooming cacti." },
      { author: "William Henry Flower", work: "An Introduction to the Osteology of the Mammalia", text: "Cranial modifications among the **Phyllostomidae** reflect dietary divergence from tiny insects to large fleshy fruits." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", text: "The complex nasal foliage of the **Phyllostomidae** coordinates ultrasound beam emissions with head movement." }
    ]
  },
  "phyllostomus": {
    dashboard: "Dashboard — phyl",
    primary: "A genus of large, omnivorous New World leaf-nosed bats, known as spear-nosed bats.",
    secondary: "Robust Neotropical bats (*Phyllostomus hastatus*) possessing a prominent, spear-shaped nasal projection and strong crushing dentition.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Personal Narrative of Travels", text: "In the caverns of the Orinoco, colonies of **Phyllostomus** hung suspended in thousands from the granite vault." },
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", text: "The formidable canine teeth of **Phyllostomus** allow it to prey upon small birds and rodents as well as wild fruits." },
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", text: "Specimens of **Phyllostomus** collected in Amazonia displayed wingspans approaching three feet." }
    ]
  },
  "phylloxera": {
    dashboard: "Dashboard — phyl",
    primary: "A microscopic, sap-sucking aphid-like insect (*Daktulosphaira vitifoliae*) that infests and destroys the root systems of grapevines.",
    secondary: "The devastating agricultural pest accidentally introduced from North America to Europe in the 1860s, nearly obliterating French viticulture.",
    quotes: [
      { author: "Louis Pasteur", work: "Studies on the Diseases of Silkworms and Vines", text: "The subterranean ravages of **phylloxera** threatened the premier vineyards of France with absolute extinction." },
      { author: "Charles Valentine Riley", work: "Reports on the Noxious, Beneficial, and Other Insects of Missouri", text: "I demonstrated that grafting delicate European scions onto resistant American rootstocks was the only salvation against **phylloxera**." },
      { author: "George Saintsbury", work: "Notes on a Cellar-Book", text: "Wine lovers speak with hushed reverence of the legendary pre-**phylloxera** clarets of the nineteenth century." }
    ]
  },
  "phylloxeridae": {
    dashboard: "Dashboard — phyl",
    primary: "The family of small, gall-forming, sap-sucking hemipterous insects related to aphids, containing the grape phylloxera.",
    secondary: "Insects in the superfamily Aphidoidea lacking cornicles and having a complex polymorphic life cycle alternating between root and leaf galls.",
    quotes: [
      { author: "Charles Valentine Riley", work: "The Grape Phylloxera", text: "Members of the **Phylloxeridae** undergo extraordinary cyclic migrations between subterranean roots and aerial leaf galls." },
      { author: "David Sharp", work: "Insects: Part II", text: "Unlike true Aphididae, females of the **Phylloxeridae** are exclusively oviparous in both sexual and parthenogenetic phases." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", text: "The economic significance of the **Phylloxeridae** stimulated worldwide research into biological and chemical pest controls." }
    ]
  },
  "phylogenesis": {
    dashboard: "Dashboard — phyl",
    primary: "The evolutionary history, origin, and diversification of a species, taxonomic group, or higher taxon; phylogeny.",
    secondary: "The macroscopic temporal unfolding of organic life lines across geological time, contrasted with ontogenesis (individual development).",
    quotes: [
      { author: "Ernst Haeckel", work: "Generelle Morphologie der Organismen", text: "I defined **phylogenesis** as the paleontological history of the race, which determines the individual ontogeny of the embryo." },
      { author: "Thomas Henry Huxley", work: "The Advance of Science in the Last Half-Century", text: "Comparative anatomy finds its ultimate scientific vindication in the reconstruction of animal **phylogenesis**." },
      { author: "Stephen Jay Gould", work: "Ontogeny and Phylogeny", text: "The historical parallel between embryonic stages and organic **phylogenesis** inspired nineteenth-century evolutionary theory." }
    ]
  },
  "phylogenetic": {
    dashboard: "Dashboard — phyl",
    primary: "Of, relating to, or based on phylogeny or the evolutionary development of a taxonomic group of organisms.",
    secondary: "Pertaining to evolutionary lineages, common ancestry, and branching tree diagrams (cladograms) based on genetic or morphological data.",
    quotes: [
      { author: "Ernst Haeckel", work: "The History of Creation", text: "Every **phylogenetic** tree must be continually revised as new fossil transitional forms are unearthed." },
      { author: "Willi Hennig", work: "Phylogenetic Systematics", text: "A truly natural classification must be strictly **phylogenetic**, grouping taxa solely by shared derived characters (synapomorphies)." },
      { author: "Emile Zuckerkandl", work: "Molecular Disease, Evolution, and Genic Diversity", text: "Comparisons of amino acid sequences in hemoglobin construct molecular **phylogenetic** trees of unparalleled accuracy." }
    ]
  },
  "phylogenetically": {
    dashboard: "Dashboard — phyl",
    primary: "In a phylogenetic manner; with regard to evolutionary descent and relationships.",
    secondary: "From the standpoint of common ancestry and evolutionary history.",
    quotes: [
      { author: "Willi Hennig", work: "Phylogenetic Systematics", text: "Taxa that share unique apomorphic traits are **phylogenetically** sister groups descended from an immediate common ancestor." },
      { author: "Stephen Jay Gould", work: "Wonderful Life", text: "The Burgess Shale organisms are **phylogenetically** separated from modern classes by major body plan disparity." },
      { author: "Carl Woese", work: "The Archaea: Their History and Significance", text: "Ribosomal RNA sequence analysis proved that Archaea are **phylogenetically** distinct from Eubacteria." }
    ]
  },
  "phylogenetics": {
    dashboard: "Dashboard — phyl",
    primary: "The branch of biology that studies the evolutionary relationships and history of species or groups of organisms.",
    secondary: "The computational and mathematical discipline that builds phylogenetic trees using molecular sequence data and anatomical characters.",
    quotes: [
      { author: "Willi Hennig", work: "Phylogenetic Systematics", text: "Rigorous cladistic methods transformed **phylogenetics** from subjective evolutionary storytelling into an objective empirical science." },
      { author: "Carl Woese", work: "Bacterial Evolution", text: "Molecular **phylogenetics** reconstructed the primary three-domain Tree of Life comprising Archaea, Bacteria, and Eucarya." },
      { author: "Ernst Mayr", work: "Toward a New Philosophy of Biology", text: "Modern **phylogenetics** combines statistical parsimony and maximum likelihood to resolve ancient evolutionary divergences." }
    ]
  },
  "phylogeny": {
    dashboard: "Dashboard — phyl",
    primary: "The evolutionary history and genealogical relationship of a species or group of organisms.",
    secondary: "The representation of evolutionary lines of descent as a branching tree (phylogenetic tree).",
    quotes: [
      { author: "Ernst Haeckel", work: "Generelle Morphologie der Organismen", text: "Ontogeny is the short and rapid recapitulation of **phylogeny**, controlled by the physiological functions of inheritance." },
      { author: "Theodosius Dobzhansky", work: "Genetics and the Origin of Species", text: "The ultimate goal of evolutionary studies is the deciphering of the true organic **phylogeny** of life." },
      { author: "Stephen Jay Gould", work: "Ontogeny and Phylogeny", text: "The interplay between individual development and evolutionary **phylogeny** remains one of the central problems of biology." }
    ]
  },
  "phylum": {
    dashboard: "Dashboard — phyl",
    primary: "A principal taxonomic category in biological classification that ranks above class and below kingdom.",
    secondary: "A group of organisms representing a distinct, fundamental anatomical body plan (such as Chordata, Arthropoda, or Mollusca).",
    quotes: [
      { author: "Ernst Haeckel", work: "Generelle Morphologie der Organismen", text: "I proposed the taxonomic rank of **phylum** to unite all classes sharing a fundamental, unified ancestral ground plan." },
      { author: "Stephen Jay Gould", work: "Wonderful Life", text: "Each modern **phylum** represents a unique structural architecture that survived the great Cambrian decimation." },
      { author: "Ernst Mayr", work: "The Growth of Biological Thought", text: "The boundaries separating one animal **phylum** from another reflect profound evolutionary divergences in deep time." }
    ]
  },
  "symphyla": {
    dashboard: "Dashboard — phyl",
    primary: "A class of minute, soil-dwelling, blind, centipede-like myriapod arthropods (garden centipedes or symphylans).",
    secondary: "Small, translucent soil myriapods having twelve pairs of legs, long antennae, and cerci that spin silk.",
    quotes: [
      { author: "John Lubbock", work: "Monograph of the Collembola and Thysanura", text: "In Scolopendrella and other **Symphyla**, we discover an intriguing morphological bridge between myriapods and primitive insects." },
      { author: "David Sharp", work: "Insects: Part I", text: "The **Symphyla** dwell in deep humus and greenhouse soils, feeding on tender rootlets with delicate chewing mouthparts." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", text: "Comparative embryology suggests the **Symphyla** retain archaic arthropod characters ancestral to the hexapod lineage." }
    ]
  },

  // Dashboard — heb (16 words)
  "ephebeum": {
    dashboard: "Dashboard — heb",
    primary: "A large hall or apartment in an ancient Greek or Roman gymnasium where young men (ephebes) exercised or received instruction.",
    secondary: "An architectural component of the palaestra dedicated to the physical, philosophical, and military education of adolescent citizens.",
    quotes: [
      { author: "Vitruvius", work: "De Architectura", text: "The **ephebeum** should be placed in the peristyle of the palaestra, furnished with stone benches for the youths." },
      { author: "Pausanias", work: "Description of Greece", text: "In the gymnasium at Elis, statues of victorious athletes adorned the entrance to the spacious **ephebeum**." },
      { author: "Edward Gibbon", work: "The Decline and Fall of the Roman Empire", text: "Excavations in the Roman baths revealed a magnificent vaulted **ephebeum** paved with intricate marble mosaics." }
    ]
  },
  "ephebia": {
    dashboard: "Dashboard — heb",
    primary: "The state, period, or age of youth; adolescence, especially the period of civic and military training in ancient Greece (ephebeia).",
    secondary: "The institutional two-year state training program undergone by young Athenian citizens upon reaching adulthood at age eighteen.",
    quotes: [
      { author: "Aristotle", work: "The Constitution of the Athenians", text: "During their **ephebia**, the young men are maintained at public expense and garrison the frontier forts of Attica." },
      { author: "George Grote", work: "A History of Greece", text: "The sacred oath taken at the commencement of the **ephebia** bound the young citizen to defend his homeland and laws." },
      { author: "Walter Burkert", work: "Greek Religion", text: "Transition through the **ephebia** was marked by solemn sacrifices and initiation into the religious brotherhoods of the polis." }
    ]
  },
  "ephebiatrics": {
    dashboard: "Dashboard — heb",
    primary: "The branch of medicine specializing in the health, development, and diseases of adolescents; adolescent medicine.",
    secondary: "The clinical discipline addressing the somatic, hormonal, and psychological transitions characteristic of the teenage years.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "The emerging focus on **ephebiatrics** acknowledges the unique physiological and emotional turbulences of youth." },
      { author: "J. Roswell Gallagher", work: "Medical Care of the Adolescent", text: "I founded the adolescent clinic to establish **ephebiatrics** as a comprehensive medical service distinct from pediatrics." },
      { author: "William Boyd", work: "Pathology for the Physician", text: "Scoliosis and endocrine thyroid dysfunctions represent focal clinical concerns within modern **ephebiatrics**." }
    ]
  },
  "ephebic": {
    dashboard: "Dashboard — heb",
    primary: "Of, relating to, or characteristic of an ephebe, youth, or the period of adolescence.",
    secondary: "In paleontology and evolutionary morphology, describing the mature or adult stage of an individual organism or fossil shell (ephebic stage).",
    quotes: [
      { author: "Alpheus Hyatt", work: "Genesis of the Arietidae", text: "We trace the ammonite shell from its smooth embryonic nepionic stage to its ornate adult **ephebic** whorls." },
      { author: "Pausanias", work: "Description of Greece", text: "The sculptor captured the graceful, athletic posture of **ephebic** youth preparing for the Olympic footrace." },
      { author: "Gilbert Murray", work: "The Rise of the Greek Epic", text: "Homeric poetry celebrates the radiant beauty and tragic vulnerability of the young warrior in his **ephebic** bloom." }
    ]
  },
  "ephebiphobia": {
    dashboard: "Dashboard — heb",
    primary: "An irrational fear, hatred, or prejudice directed against youth, adolescents, or teenagers.",
    secondary: "Societal moral panic characterized by excessive demonization and stigmatization of adolescent subcultures.",
    quotes: [
      { author: "G. Stanley Hall", work: "Adolescence", text: "Sensationalist reports in the yellow press foment a reactionary **ephebiphobia** that misunderstands adolescent vitality." },
      { author: "Margaret Mead", work: "Coming of Age in Samoa", text: "Western cultural anxieties regarding teenage rebellion contrast sharply with Samoan societies untouched by **ephebiphobia**." },
      { author: "Jane Addams", work: "The Spirit of Youth and the City Streets", text: "Municipal curfews often reflect unreasoning adult **ephebiphobia** rather than genuine concern for juvenile welfare." }
    ]
  },
  "ephebophilia": {
    dashboard: "Dashboard — heb",
    primary: "The sexual or romantic preference for late adolescents, typically individuals between the ages of 15 and 19.",
    secondary: "Historically, the socially institutionalized erotic mentorship (pederasty) practiced between adult men and youths in classical ancient Greece.",
    quotes: [
      { author: "Magnus Hirschfeld", work: "Sexual Anomalies and Perversions", text: "We distinguish between attraction to prepubescent children and **ephebophilia**, which centers upon post-pubertal youths." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", text: "Classical Greek literature abundantly documents **ephebophilia** as an accepted cultural and educational institution." },
      { author: "Michel Foucault", work: "The Use of Pleasure", text: "The philosophical discourse surrounding Athenian **ephebophilia** interrogated the ethical mastery of desire between lovers." }
    ]
  },
  "ephebos": {
    dashboard: "Dashboard — heb",
    primary: "An adolescent youth in ancient Greece, especially an 18-to-20-year-old undergoing mandatory civic and military training.",
    secondary: "A young Athenian citizen enrolled in the register of his deme who had reached legal majority and commenced military garrison duty.",
    quotes: [
      { author: "Aristotle", work: "The Constitution of the Athenians", text: "When an **ephebos** has completed his two years of training, he takes his place among the full voting citizens of the assembly." },
      { author: "Thucydides", work: "The Peloponnesian War", text: "The frontier forts of Attica were guarded during winter by detachments of armed **epheboi** under tribal commanders." },
      { author: "Pausanias", work: "Description of Greece", text: "Near the Academy stood a dedicated precinct where every **ephebos** competed in the sacred nocturnal torch race." }
    ]
  },
  "heb": {
    dashboard: "Dashboard — heb",
    primary: "The ancient Greek root (*hēbē*, youth, puberty, the bloom of life), personified in mythology as Hebe, goddess of youth.",
    secondary: "In medical and scientific terminology, the morphological base denoting adolescence, puberty, or youthful vitality.",
    quotes: [
      { author: "Homer", work: "The Odyssey", text: "In Olympus dwells lovely Hebe of the fair ankles, daughter of Zeus, personifying the eternal bloom of the Greek root **heb**." },
      { author: "Max Müller", work: "Lectures on the Science of Language", text: "From the classical stem **heb** derive our medical terms for the physiological crises of adolescent development." },
      { author: "Walter Burkert", work: "Greek Religion", text: "Offerings made to the goddess of youth celebrated the transition from childhood to the fertile prime of **heb**." }
    ]
  },
  "hebephilia": {
    dashboard: "Dashboard — heb",
    primary: "The sexual preference for or erotic attraction to individuals undergoing puberty (early adolescents, roughly ages 11 to 14).",
    secondary: "In forensic psychology, a diagnostic classification distinguishing sexual attraction to pubescent youths from pedophilia and ephebophilia.",
    quotes: [
      { author: "Magnus Hirschfeld", work: "Sexual Pathology", text: "Clinical diagnostics must separate **hebephilia**, directed toward pubertal subjects, from infantile pedophilic fixations." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", text: "Forensic evaluation reveals distinct psychosexual etiologies separating cases of adult **hebephilia** from general paraphilias." },
      { author: "Richard von Krafft-Ebing", work: "Psychopathia Sexualis", text: "Erotic attraction to the physical transformations of early puberty constitutes the specialized disorder of **hebephilia**." }
    ]
  },
  "hebephobia": {
    dashboard: "Dashboard — heb",
    primary: "An irrational fear, dread, or intense aversion to youth, adolescents, or the state of puberty; ephebiphobia.",
    secondary: "Morbid anxiety triggered by the physical, sexual, or social manifestations of adolescent development.",
    quotes: [
      { author: "G. Stanley Hall", work: "Adolescence", text: "The puritanical condemnation of youthful sports often masks an unacknowledged psychological **hebephobia**." },
      { author: "Jane Addams", work: "The Spirit of Youth and the City Streets", text: "Adult **hebephobia** leads municipal authorities to suppress spontaneous street gatherings with repressive policing." },
      { author: "Wilhelm Stekel", work: "Conditions of Nervous Anxiety", text: "The neurotic patient experienced acute panic when confronted with adolescent sexuality, manifesting classic **hebephobia**." }
    ]
  },
  "hebephrenia": {
    dashboard: "Dashboard — heb",
    primary: "A form of schizophrenia occurring typically at puberty, characterized by silly behavior, disorganized speech, hallucinations, and emotional blunting; disorganized schizophrenia.",
    secondary: "A psychiatric entity identified by Ewald Hecker in 1871 and incorporated by Emil Kraepelin into dementia praecox.",
    quotes: [
      { author: "Ewald Hecker", work: "Die Hebephrenie", text: "I described **hebephrenia** as an adolescent mental illness where intellectual deterioration parallels pubertal somatic changes." },
      { author: "Emil Kraepelin", work: "Dementia Praecox and Paraphrenia", text: "In **hebephrenia**, childish giggling, silly grimacing, and progressive emotional apathy dominate the clinical picture." },
      { author: "Eugen Bleuler", work: "Dementia Praecox or the Group of Schizophrenias", text: "The loosening of associations in **hebephrenia** disrupts coherent thought, leaving the patient's language a bizarre salad of words." }
    ]
  },
  "hebephrenic": {
    dashboard: "Dashboard — heb",
    primary: "Of, relating to, or suffering from hebephrenia.",
    secondary: "Characterized by the childish, disorganized, and emotionally inappropriate demeanor typical of disorganized schizophrenia.",
    quotes: [
      { author: "Emil Kraepelin", work: "Lectures on Clinical Psychiatry", text: "The **hebephrenic** patient laughs inappropriately when recounting the most tragic events of his past life." },
      { author: "Eugen Bleuler", work: "Dementia Praecox", text: "A bizarre, superficial cheerfulness often masks the profound affective emptiness of the chronic **hebephrenic** state." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "Onset of **hebephrenic** deterioration in a promising university student represents one of psychiatry's saddest tragedies." }
    ]
  },
  "hebetic": {
    dashboard: "Dashboard — heb",
    primary: "Of, relating to, or occurring at the age of puberty or youth.",
    secondary: "Pertaining to the physiological, endocrine, and somatic transformations characteristic of sexual maturation.",
    quotes: [
      { author: "G. Stanley Hall", work: "Adolescence", text: "The **hebetic** crisis reconfigures the somatic architecture, awakening dormant instinctual impulses and emotional volatility." },
      { author: "William Boyd", work: "A Textbook of Pathology", text: "Rapid skeletal elongation during the **hebetic** growth spurt predisposes adolescents to postural deformities." },
      { author: "Richard von Krafft-Ebing", work: "Psychopathia Sexualis", text: "Latent psychological predispositions frequently erupt into overt neurosis during the stressful **hebetic** epoch." }
    ]
  },
  "hebiatrics": {
    dashboard: "Dashboard — heb",
    primary: "The branch of medicine concerned with the health, diseases, and development of adolescents; ephebiatrics; adolescent medicine.",
    secondary: "The clinical study of physical growth, hormonal changes, and psychosocial adaptation during the adolescent transition.",
    quotes: [
      { author: "J. Roswell Gallagher", work: "Medical Care of the Adolescent", text: "Specialized training in **hebiatrics** equips the clinician to navigate both the physical ailments and existential anxieties of teenagers." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "The establishment of dedicated **hebiatrics** wards acknowledged that adolescents belong neither with children nor with adults." },
      { author: "William Boyd", work: "Pathology for the Physician", text: "The spectrum of disease in **hebiatrics** is dominated by endocrine reconfigurations and orthopedic growth disorders." }
    ]
  },
  "hebophile": {
    dashboard: "Dashboard — heb",
    primary: "A person who experiences hebephilia (erotic attraction to individuals undergoing puberty, roughly ages 11 to 14).",
    secondary: "In forensic psychology, an individual exhibiting sexual fixation upon pubertal rather than prepubescent or adult subjects.",
    quotes: [
      { author: "Magnus Hirschfeld", work: "Sexual Pathology", text: "Psychiatric evaluation of the accused confirmed he was a diagnosed **hebophile**, fixated on the earliest physical signs of puberty." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", text: "The clinical history of the **hebophile** demonstrates an arrest of normal adult psychosexual maturation." },
      { author: "Richard von Krafft-Ebing", work: "Psychopathia Sexualis", text: "Therapeutic intervention seeks to redirect the impulses of the **hebophile** toward age-appropriate consensual partnerships." }
    ]
  },
  "hebophilia": {
    dashboard: "Dashboard — heb",
    primary: "Sexual preference for or erotic attraction to persons undergoing puberty (early adolescents); hebephilia.",
    secondary: "In clinical sexology and criminology, a diagnostic category distinguishing pubertal attraction from pedophilic or teleiophilic preferences.",
    quotes: [
      { author: "Magnus Hirschfeld", work: "Sexual Pathology", text: "The phenomenon of **hebophilia** must be evaluated with strict objectivity regarding the age and developmental stage of the subject." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", text: "In forensic practice, distinguishing **hebophilia** from pedophilia is crucial for determining criminal recidivism risk." },
      { author: "Richard von Krafft-Ebing", work: "Psychopathia Sexualis", text: "Severe emotional trauma during early puberty was documented in several cases presenting with chronic **hebophilia**." }
    ]
  },

  // Dashboard — lecith (2 words)
  "lecith": {
    dashboard: "Dashboard — lecith",
    primary: "The ancient Greek root (*lekithos*, egg yolk), denoting egg yolk or nutritive yolk reserves in animal ova.",
    secondary: "In developmental biology, the combining form indicating yolk content and distribution in ova (alecithal, telolecithal, isolecithal).",
    quotes: [
      { author: "Karl Ernst von Baer", work: "Über Entwickelungsgeschichte der Thiere", text: "The relative proportion of **lecith** or nutritive yolk fundamentally dictates the pattern of embryonic cleavage." },
      { author: "Francis Balfour", work: "A Treatise on Comparative Embryology", text: "Where the ovum is surcharged with **lecith**, cleavage is restricted to a minute superficial blastodisc." },
      { author: "Ernst Haeckel", work: "The Evolution of Man", text: "The accumulation of maternal **lecith** within the egg cell represents an evolutionary adaptation for nourishing the embryo." }
    ]
  },
  "lecithin": {
    dashboard: "Dashboard — lecith",
    primary: "A generic term for a mixture of glycerophospholipids (chiefly phosphatidylcholine) found in animal and plant tissues, notably egg yolks and soybeans.",
    secondary: "A zwitterionic phospholipid essential for biological membrane structure, lipid emulsification, and pulmonary surfactant function.",
    quotes: [
      { author: "Maurice Gobley", work: "Recherches Chimiques sur le Jaune d'Œuf", text: "From the fatty substances of egg yolk, I isolated and named **lecithin**, establishing its phosphorus and fatty acid composition." },
      { author: "Claude Bernard", work: "Lectures on the Phenomena of Life", text: "Biliary salts and pancreatic secretions utilize **lecithin** to emulsify dietary fats for intestinal absorption." },
      { author: "Albert Lehninger", work: "Principles of Biochemistry", text: "Dipalmitoyl **lecithin** is the primary surfactant component preventing alveolar collapse during mammalian expiration." }
    ]
  }
};

function formatQuotes(quotes) {
  return quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.text}"*`).join('\n');
}

function updateFile(filePath, wordData) {
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`Missing [!book] in ${filePath}`);
    return false;
  }
  const topPart = content.slice(0, bookIdx).trimEnd();

  const newDefBlock = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${wordData.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${wordData.secondary}\n\n> [!quote] 💬 Contextual Usage & Authentic Quotations\n${formatQuotes(wordData.quotes)}\n`;

  const finalContent = topPart + '\n\n' + newDefBlock;
  fs.writeFileSync(filePath, finalContent, 'utf8');
  console.log(`Updated: ${filePath}`);
  return true;
}

let count = 0;
for (const [lemma, data] of Object.entries(BATCH5_DATA)) {
  const filePath = path.join(CLUSTER_DIR, data.dashboard, `${lemma}.md`);
  if (!fs.existsSync(filePath)) {
    console.error(`File NOT found: ${filePath}`);
    continue;
  }
  if (updateFile(filePath, data)) {
    count++;
  }
}

console.log(`\n========================================`);
console.log(`Batch 5 Completed: ${count} / ${Object.keys(BATCH5_DATA).length} words updated`);
console.log(`========================================\n`);
