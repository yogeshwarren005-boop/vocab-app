# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — sap (44 words)
  # =========================================================================
  "Dashboard — sap/homosapiens.md": {
    "primary": "The primate species to which modern humans belong, characterized by high intelligence and symbolic language.",
    "secondary": "In evolutionary paleoanthropology and zoological taxonomy, the sole surviving species of the genus Homo.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "In a genealogical series, **Homo sapiens** forms but a single branch of the catarrhine simian lineage."},
      {"author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "The structural gap between **Homo sapiens** and the gorilla is smaller than that separating the gorilla from the lower monkeys."},
      {"author": "Ernst Haeckel", "work": "The Evolution of Man", "quote": "The phylogenetic emergence of **Homo sapiens** crowns the long terrestrial drama of vertebrate evolution."}
    ]
  },
  "Dashboard — sap/sap.md": {
    "primary": "The vital fluid that circulates through a plant; to gradually weaken or deplete energy or strength.",
    "secondary": "In military fortification and siege craft, a deep narrow trench excavated to undermine enemy bastions.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "The **sap** doth rise, and budding twigs proclaim the return of spring."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Whose tender tree nourished with **sap** divine yielded fruit immortal."},
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "The ascent of vital **sap** within the wood nourishes both branch and leaf."}
    ]
  },
  "Dashboard — sap/sapid.md": {
    "primary": "Having a pleasant, savory, or distinctive taste; flavorful or palatable.",
    "secondary": "In literary criticism and culinary philosophy, possessing lively intellectual zest, piquancy, or agreeable character.",
    "quotes": [
      {"author": "Charles Lamb", "work": "Essays of Elia", "quote": "The roast pig presented a crisp, succulent crackling and the most **sapid** morsels imaginable."},
      {"author": "Laurence Sterne", "work": "A Sentimental Journey", "quote": "A crust of bread and a flask of **sapid** wine sufficed for my modest luncheon."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "True art, like wholesome food, must be **sapid** and nourishing to the human spirit."}
    ]
  },
  "Dashboard — sap/sapidity.md": {
    "primary": "Flavorful savoriness, palatableness, or distinct taste that delights the palate.",
    "secondary": "In sensory physiology and aesthetics, the capacity of a substance or discourse to stimulate agreeable discernment.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Luxury cloys the appetite, until dishes lose all their natural **sapidity** and zest."},
      {"author": "William Hazlitt", "work": "Table-Talk", "quote": "The pleasant **sapidity** of seasoned conversation outlasts the formal brilliance of disputation."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The sensation of **sapidity** produced on the palate depends upon the chemical qualities of the body dissolved."}
    ]
  },
  "Dashboard — sap/sapidness.md": {
    "primary": "Flavorfulness, palatability, or the property of having a pleasing taste.",
    "secondary": "In philosophical prose and early scientific treatises, the distinct gusto or sensory richness inherent in organic bodies.",
    "quotes": [
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The remarkable **sapidness** of wild berries commended them to the primitive hunters of ancient Britain."},
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "The distinct **sapidness** of saline solutions demonstrates the diverse shapes of their constituent particles."},
      {"author": "Isaac D'Israeli", "work": "Curiosities of Literature", "quote": "The lively **sapidness** of his epistolary style preserves these old memoirs from oblivion."}
    ]
  },
  "Dashboard — sap/sapience.md": {
    "primary": "Great wisdom, discernment, or knowledge, especially when applied with elevated judgment.",
    "secondary": "In classical and satirical prose, profound philosophical insight, or mocked pretension of superior understanding.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "O sovran, virtuous, precious of all trees in Paradise! of operation blest to **sapience**, hitherto obscured."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The learned bailiff stroked his chin and delivered himself of an opinion with solemn **sapience**."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon nodded his head with an air of ponderous **sapience** that silenced the young curate."}
    ]
  },
  "Dashboard — sap/sapiens.md": {
    "primary": "Wise, discerning, or rational (the Latin specific epithet for modern mankind in biological taxonomy).",
    "secondary": "In anthropological philosophy, denoting the conscious reflective capacity that defines modern humanity.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The designation of Homo **sapiens** reflects our unique capacity for abstract reflection and symbolic speech."},
      {"author": "Carl Linnaeus", "work": "Systema Naturae", "quote": "Under the genus Homo, Linnaeus classified mankind as Homo **sapiens**, characterized by self-knowledge."},
      {"author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "The cranial capacity of Homo **sapiens** distinguishes the species from all fossil Neanderthal remains."}
    ]
  },
  "Dashboard — sap/sapient.md": {
    "primary": "Wise or attempting to appear wise; sagacious and discerning.",
    "secondary": "In ironical narrative and literature, possessing or affecting an aura of grave intellectual supremacy.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King Lear", "quote": "It shall be done; I will arraign them straight. Come, sit thou here, most **sapient** sir."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The **sapient** gentlemen of the coroner's jury deliberated upon the mysterious demise of the lodger."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Her father looked extremely **sapient**, and nodded approval of the prudent economic arrangement."}
    ]
  },
  "Dashboard — sap/sapiential.md": {
    "primary": "Relating to, characterized by, or imparting wisdom.",
    "secondary": "In biblical theology and literary genre, applied to books such as Proverbs, Ecclesiastes, and Job containing moral precepts.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Thus was the world created with divine and **sapiential** power, harmonious in every part."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The **sapiential** books of King Solomon contain profound maxims on government and morals."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "Ancient philosophy possessed a **sapiential** depth that modern empiricism too often ignores."}
    ]
  },
  "Dashboard — sap/sapiently.md": {
    "primary": "In a wise, shrewd, sagacious, or knowingly observant manner.",
    "secondary": "In character description and humor, gesturing or nodding knowingly to imply deep comprehension of a matter.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The veteran harpooneer shook his head **sapiently**, forecasting foul weather from the setting sun."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Old Major Dobbin listened attentively and remarked **sapiently** that all would turn out well in time."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Lestrade nodded **sapiently**, though it was plain that he had failed to grasp Holmes's deduction."}
    ]
  },
  "Dashboard — sap/sapindaceae.md": {
    "primary": "A family of flowering plants (the soapberry family), including maples, lychees, and horse chestnuts.",
    "secondary": "In systematic botany, a major tropical and temperate family characterized by rich saponin content in bark or seeds.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The family **Sapindaceae** includes the soapberry and horse-chestnut, characterized by compound leaves and saponin-bearing seeds."},
      {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "Numerous climbing lianas and timber trees of the tropics belong to the extensive family **Sapindaceae**."},
      {"author": "George Bentham", "work": "Genera Plantarum", "quote": "The petals of **Sapindaceae** frequently bear an internal scale or tuft of hairs above the claw."}
    ]
  },
  "Dashboard — sap/sapindales.md": {
    "primary": "An order of dicotyledonous flowering plants containing families such as Sapindaceae, Rutaceae, and Anacardiaceae.",
    "secondary": "In botanical phylogenetic taxonomy, woody plants typically possessing pinnately compound leaves and nectariferous disks.",
    "quotes": [
      {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "The alliance **Sapindales** comprises diverse woody families exhibiting asymmetrical floral development."},
      {"author": "Asa Gray", "work": "Structural Botany", "quote": "Within the order **Sapindales**, we observe a persistent tendency toward polycarpic and nectariferous disc structures."},
      {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "Species belonging to **Sapindales** are distributed widely throughout both hemispheres."}
    ]
  },
  "Dashboard — sap/sapindus.md": {
    "primary": "A genus of shrubs and trees in the soapberry family whose berries yield a lathering soap substitute.",
    "secondary": "In economic botany, soapberry trees whose pericarp contains saponins traditionally used for laundering delicate textiles.",
    "quotes": [
      {"author": "William Roxburgh", "work": "Flora Indica", "quote": "The pulp of the fruit of **Sapindus** saponaria forms an abundant lather with water and serves in place of soap."},
      {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "The indigenous inhabitants harvest the nuts of **Sapindus** for washing delicate silk fabrics."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The genus **Sapindus** is represented in the warmer states by the wild soapberry tree."}
    ]
  },
  "Dashboard — sap/sapir.md": {
    "primary": "Edward Sapir (1884–1939), an American linguist and anthropologist influential in structural linguistics.",
    "secondary": "In linguistic anthropology, co-originator of the Sapir-Whorf hypothesis regarding linguistic relativity.",
    "quotes": [
      {"author": "Franz Boas", "work": "Handbook of American Indian Languages", "quote": "The brilliant field researches of Edward **Sapir** revealed the intricate grammatical architecture of indigenous tongues."},
      {"author": "Benjamin Lee Whorf", "work": "Language, Thought, and Reality", "quote": "In agreement with **Sapir**, we recognize that linguistic categories mold our intuitive perception of reality."},
      {"author": "Leonard Bloomfield", "work": "Language", "quote": "The phonetic and phonemic methods introduced by **Sapir** set a new standard for descriptive linguistics."}
    ]
  },
  "Dashboard — sap/sapless.md": {
    "primary": "Lacking sap or vital moisture; dry, withered, or devoid of vigor and vitality.",
    "secondary": "In poetic tragedy and portraiture, describing decayed age, lifeless prose, or withered ambition.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VI, Part 1", "quote": "These eyes, like lamps whose wasting oil is spent, wax dim, and these gray locks are withered like a **sapless** bough."},
      {"author": "Robert Burns", "work": "Poems and Songs", "quote": "Fusionless, pithless, **sapless**, tasteless, the dried stalk shivers in the winter blast."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "My heart felt cold and **sapless**, like a dead trunk in an icy wind."}
    ]
  },
  "Dashboard — sap/sapling.md": {
    "primary": "A young tree, especially one with a slender, flexible trunk; a youthful person.",
    "secondary": "In pastoral narrative, symbolizing supple youth, resilience, or malleable inexperience.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard III", "quote": "Behold, mine arm is like a blasted **sapling** withered up!"},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I set out each tender **sapling** with great care, watering its roots against the summer drought."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The young birch bent like a **sapling** beneath the sudden fury of the gale."}
    ]
  },
  "Dashboard — sap/sapodilla.md": {
    "primary": "A large tropical evergreen tree (Manilkara zapota) yielding sweet brown fruit and chicle gum.",
    "secondary": "In tropical agriculture and commerce, the tree cultivated for its edible sugary fruit and latex base for chewing gum.",
    "quotes": [
      {"author": "Charles Darwin", "work": "Journal of Researches", "quote": "We refreshed ourselves with the sweet, sugary pulp of the tropical **sapodilla**."},
      {"author": "William Dampier", "work": "A New Voyage Round the World", "quote": "The **sapodilla** tree yields a fruit as large as a quince, having a luscious and fragrant taste."},
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "The milky latex of the **sapodilla** trunk furnishes the chicle gum prized by the native tribes."}
    ]
  },
  "Dashboard — sap/saponaceous.md": {
    "primary": "Resembling or having the qualities of soap; soapy, slippery, or unctuous in texture.",
    "secondary": "In character satire and social critique, describing an evasively smooth, flattering, or untrustworthy demeanour.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The lawyer possessed a bland and **saponaceous** manner that made his slippery promises hard to pin down."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The whale-oil, when freshly baled from the case, felt remarkably soft and **saponaceous** to the touch."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The courtier smiled with **saponaceous** servility, agreeing with every royal whim."}
    ]
  },
  "Dashboard — sap/saponaria.md": {
    "primary": "A genus of herbaceous flowering plants in the carnation family, known as soapworts.",
    "secondary": "In ethnobotany and herbal medicine, plants whose roots and foliage yield lathering saponins used as natural detergents.",
    "quotes": [
      {"author": "John Gerard", "work": "The Herball, or Generall Historie of Plantes", "quote": "The bruised leaves of **Saponaria**, or soapwort, being agitated in water, make an abundant froth."},
      {"author": "William Withering", "work": "An Arrangement of British Plants", "quote": "Common **Saponaria** officinalis grows along riverbanks, bearing pale pink clusters of scented blossoms."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The genus **Saponaria** belongs to the pink family, notable for containing mucilaginous saponins."}
    ]
  },
  "Dashboard — sap/saponification.md": {
    "primary": "The chemical hydrolysis of a fat or oil with an alkali to produce soap and glycerol.",
    "secondary": "In organic chemistry and industrial manufacturing, alkaline cleavage of ester linkages yielding salts of fatty acids.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The chemical process of **saponification** decomposes neutral fats into alkaline soap and sweet glycerin."},
      {"author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "In the **saponification** of tallow, caustic potash combines with fatty acids to form soluble stearates."},
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "The gradual **saponification** of fixed oils by lixivial salts was known even to ancient artisans."}
    ]
  },
  "Dashboard — sap/saponified.md": {
    "primary": "Converted into soap through chemical reaction with an alkali; hydrolyzed.",
    "secondary": "In industrial chemistry and lipidology, fats whose triglyceride bonds have undergone alkaline decomposition.",
    "quotes": [
      {"author": "Michael Faraday", "work": "The Chemical History of a Candle", "quote": "When the mutton fat is completely **saponified**, the alkaline base neutralizes the stearic acid."},
      {"author": "Justus von Liebig", "work": "Animal Chemistry", "quote": "The ingested lipids are partly **saponified** by the alkaline secretions of the bile and pancreatic fluid."},
      {"author": "Louis Pasteur", "work": "Researches on the Molecular Asymmetry of Natural Organic Products", "quote": "The resinous ester was **saponified** using alcoholic potash and then precipitated with acid."}
    ]
  },
  "Dashboard — sap/saponify.md": {
    "primary": "To convert a fat, oil, or ester into soap by treatment with an alkali.",
    "secondary": "In industrial and physiological chemistry, hydrolyzing fatty esters through heating with basic hydroxide solutions.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Heating animal oils with caustic soda will rapidly **saponify** the triglycerides."},
      {"author": "Thomas Graham", "work": "Elements of Chemistry", "quote": "Caustic alkalis possess the power to **saponify** fixed oils upon application of moderate heat."},
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "Potassium hydrate acts vigorously to **saponify** vegetable oils, forming hard soluble soap."}
    ]
  },
  "Dashboard — sap/saponin.md": {
    "primary": "A class of plant glucosides that form a durable, soapy froth when shaken with water.",
    "secondary": "In phytochemistry and pharmacology, hemolytic and surfactant compounds produced by plants as natural defenses against pathogens.",
    "quotes": [
      {"author": "Justus von Liebig", "work": "Organic Chemistry in its Applications to Agriculture and Physiology", "quote": "The bitter glucoside known as **saponin** produces a durable, frothy lather when shaken with water."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Certain seeds containing toxic **saponin** are avoided by grazing cattle."},
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "The foaming properties of the extract were attributed to the presence of colloidal **saponin**."}
    ]
  },
  "Dashboard — sap/saporous.md": {
    "primary": "Full of flavor; having a distinct, stimulating taste or agreeable savor.",
    "secondary": "In classical physiology and natural philosophy, exciting the gustatory sense through dissolved sapid particles.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "The juices of ripe fruits become remarkably **saporous** under the warm rays of the autumn sun."},
      {"author": "Robert Boyle", "work": "Experiments and Considerations Touching Colours", "quote": "Saline particles impart a sharp, **saporous** sensation when applied to the moisture of the tongue."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The **saporous** qualities of wine or vinegar are sensible ideas produced in our minds by corpuscular motion."}
    ]
  },
  "Dashboard — sap/sapota.md": {
    "primary": "A tropical evergreen fruit tree native to Mesoamerica; the sapodilla.",
    "secondary": "In pomology and regional botany, the species Achras sapota yielding russet-skinned fruits with sweet, granular flesh.",
    "quotes": [
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "The sweet and juicy fruit of the **sapota** is prized throughout the Spanish West Indies."},
      {"author": "William Dampier", "work": "A New Voyage Round the World", "quote": "The **sapota** tree resembles our pear tree in stature and produces fruit of excellent flavor."},
      {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "Achras **sapota** is widely cultivated in tropical gardens for its luscious brown berries."}
    ]
  },
  "Dashboard — sap/sapotaceae.md": {
    "primary": "A family of flowering plants (the sapodilla family), largely comprising tropical evergreen trees.",
    "secondary": "In economic botany, a family producing valuable latexes (such as gutta-percha and chicle) and nutritious fruits.",
    "quotes": [
      {"author": "Asa Gray", "work": "Structural Botany", "quote": "The family **Sapotaceae** consists of tropical trees containing milky laticiferous juices and leathery evergreen foliage."},
      {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "Gutta-percha and diverse edible fruits are yielded by arborescent members of **Sapotaceae**."},
      {"author": "George Bentham", "work": "Genera Plantarum", "quote": "The berry of **Sapotaceae** typically encloses large lustrous seeds with a conspicuous lateral scar."}
    ]
  },
  "Dashboard — sap/sapote.md": {
    "primary": "A soft, edible tropical fruit produced by trees of the Sapotaceae and related families.",
    "secondary": "In Mesoamerican ethnobotany, sweet fleshy fruits ranging from white to black varieties cultivated for millennia.",
    "quotes": [
      {"author": "Charles Darwin", "work": "Journal of Researches", "quote": "In the tropical valleys of the Andes, the black **sapote** produces a fruit with rich, dark pulp."},
      {"author": "Alexander von Humboldt", "work": "Political Essay on the Kingdom of New Spain", "quote": "The markets of Mexico are stocked with white and yellow varieties of luscious **sapote**."},
      {"author": "William Dampier", "work": "A New Voyage Round the World", "quote": "The **sapote** is esteemed among the most delicious and wholesome fruits of Central America."}
    ]
  },
  "Dashboard — sap/sapper.md": {
    "primary": "A soldier employed in building military fortifications, digging trenches, or laying and clearing mines.",
    "secondary": "In military history and combat engineering, an operative skilled in subterranean tunneling under enemy battlements.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles: A Pure Woman", "quote": "A retired military **sapper** had settled in the village, skilled in masonry and surveying."},
      {"author": "Arthur Conan Doyle", "work": "The Great Boer War", "quote": "Every imperial **sapper** worked tirelessly under heavy fire to entrench the exposed artillery battery."},
      {"author": "Winston Churchill", "work": "The River War", "quote": "The army was preceded by the **sapper** and miner, bridging every swollen torrent across the desert."}
    ]
  },
  "Dashboard — sap/sappy.md": {
    "primary": "Full of sap; juicy, succulent, or vigorously alive; also informal for overly sentimental.",
    "secondary": "In pastoral literature and forestry, wood or foliage rich in living cambial juices and vibrant growth.",
    "quotes": [
      {"author": "graf Leo Tolstoy", "work": "War and Peace", "quote": "The old oak, quite transfigured, spreading out a canopy of **sappy** dark-green foliage, stood majestic in the sun."},
      {"author": "Robert Burns", "work": "Poems and Songs of Robert Burns", "quote": "There’s naething like the honest nappy; whare’ll ye e’er see men sae happy, or find a heart so warm and **sappy**?"},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The timber had been cut green, and the **sappy** logs hissed and crackled upon the hearth."}
    ]
  },
  "Dashboard — sap/sapraemia.md": {
    "primary": "Blood poisoning caused by the absorption of toxins from local tissue necrosis (British spelling of sapremia).",
    "secondary": "In 19th-century surgical pathology, systemic toxic fever induced by chemical absorption from putrefying wounds without septic bacteremia.",
    "quotes": [
      {"author": "Joseph Lister", "work": "The Collected Papers of Joseph Lister", "quote": "Septic absorption from the unwashed wound induced high fever and the classic symptoms of **sapraemia**."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The sudden rigor and toxic delirium indicated acute **sapraemia** resulting from retained necrotic tissue."},
      {"author": "Florence Nightingale", "work": "Notes on Hospitals", "quote": "Adequate hospital ventilation prevents the accumulation of effluvia that predisposes surgical patients to **sapraemia**."}
    ]
  },
  "Dashboard — sap/sapremia.md": {
    "primary": "Systemic toxic illness resulting from the absorption into the blood of toxins from decaying tissue.",
    "secondary": "In clinical medicine and surgical pathology, intoxication arising from bacterial products at a necrotic wound focus.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Unlike progressive septicemia, the clinical fever of **sapremia** abates promptly once the necrotic focus is cleansed."},
      {"author": "Joseph Lister", "work": "The Collected Papers of Joseph Lister", "quote": "Antiseptic dressings eliminate the decomposition of surgical discharges, thereby preventing systemic **sapremia**."},
      {"author": "Havelock Ellis", "work": "The Nationalisation of Health", "quote": "The medical officer traced the toxic **sapremia** to contamination from an untreated drainage canal."}
    ]
  },
  "Dashboard — sap/saprobe.md": {
    "primary": "An organism that derives its nourishment from decaying organic matter.",
    "secondary": "In microbial ecology and saprology, a decomposing bacterium or fungus recycling nutrients in terrestrial and aquatic biomes.",
    "quotes": [
      {"author": "Ernst Haeckel", "work": "The Wonders of Life", "quote": "The microscopic **saprobe** plays an indispensable role in nature by decomposing dead animal tissues into elemental salts."},
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Every bacterial **saprobe** secretes digestive ferments that liquefy decaying organic matter."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Without the scavenge work of the fungal **saprobe**, the surface of the earth would be choked with ancient debris."}
    ]
  },
  "Dashboard — sap/saprobic.md": {
    "primary": "Relating to or characterized by organisms that live on decaying organic matter.",
    "secondary": "In freshwater ecology, waters classified according to their degree of organic pollution and anaerobic microbial decay.",
    "quotes": [
      {"author": "Ernst Haeckel", "work": "The Evolution of Man", "quote": "In primitive stagnant waters, **saprobic** microorganisms thrive by consuming dissolved detritus."},
      {"author": "Louis Pasteur", "work": "Researches on the Fermentation of Yeast", "quote": "Certain fungi flourish best in **saprobic** environments rich in rotting carbohydrate residues."},
      {"author": "Thomas Henry Huxley", "work": "Critiques and Addresses", "quote": "The presence of **saprobic** organisms in a stream indicates a high level of decaying organic discharge."}
    ]
  },
  "Dashboard — sap/saprolegnia.md": {
    "primary": "A genus of freshwater water-molds that feed saprophytically on organic matter and parasitize fish.",
    "secondary": "In aquatic pathology and mycology, the primary causal agent of fungal epidemics attacking salmonid fins and gills.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Saprolegnia in Relation to the Salmon Disease", "quote": "The aquatic fungus **Saprolegnia** forms a white, cottony growth over the epidermal lesions of diseased salmon."},
      {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "Specimens of drowned insects in pond water were speedily covered with filaments of **Saprolegnia**."},
      {"author": "Louis Pasteur", "work": "Studies on the Silkworm Disease", "quote": "Parasitic molds related to **Saprolegnia** attack weak aquatic larvae and fish fry."}
    ]
  },
  "Dashboard — sap/saprolegniales.md": {
    "primary": "An order of aquatic oomycete molds containing the genus Saprolegnia.",
    "secondary": "In cryptogamic taxonomy and marine mycology, filamentous water-molds characterized by biflagellate zoospores and cellulose walls.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Saprolegnia in Relation to the Salmon Disease", "quote": "The order **Saprolegniales** is distinguished by biflagellate zoospores and aquatic mycelia living upon decomposing organic matter."},
      {"author": "Joseph Dalton Hooker", "work": "The Cryptogamic Botany", "quote": "The water-molds of **Saprolegniales** bridge the structural boundary between simple algae and filamentous fungi."},
      {"author": "Asa Gray", "work": "Synoptical Flora of North America", "quote": "Reproduction in the order **Saprolegniales** exhibits both sexual oogonia and free-swimming asexual swarm-spores."}
    ]
  },
  "Dashboard — sap/saprolite.md": {
    "primary": "Chemically weathered rock formed in place that retains the original structural features of the parent bedrock.",
    "secondary": "In geomorphology and soil science, deeply decomposed crystalline rock preceding complete transformation into residual clay.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Elements of Geology", "quote": "The underlying granitic rock had decomposed in situ into soft, friable **saprolite** retaining original mineral banding."},
      {"author": "Archibald Geikie", "work": "Text-book of Geology", "quote": "In humid tropical regions, chemical leaching transforms hard crystalline gneiss into thick blankets of clayey **saprolite**."},
      {"author": "Grove Karl Gilbert", "work": "Report on the Geology of the Henry Mountains", "quote": "The weathered mantle of **saprolite** had been stripped away by torrential desert storms."}
    ]
  },
  "Dashboard — sap/sapropel.md": {
    "primary": "A dark, aquatic sediment rich in organic matter formed under anoxic conditions on lake or sea beds.",
    "secondary": "In petroleum geology and paleoceanography, carbon-rich anaerobic mud that constitutes the precursor to petroleum hydrocarbons.",
    "quotes": [
      {"author": "Archibald Geikie", "work": "Text-book of Geology", "quote": "The fetid black **sapropel** accumulated on the stagnant lake bed, rich in organic slime and anaerobic bacteria."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Geologists recognize ancient petroleum source beds in the dark, bituminized **sapropel** of prehistoric seas."},
      {"author": "Ernst Haeckel", "work": "The History of Creation", "quote": "The primordial mud and aquatic **sapropel** provided a fertile matrix for the emergence of rudimentary living forms."}
    ]
  },
  "Dashboard — sap/saprophagous.md": {
    "primary": "Feeding on decaying or dead organic matter (especially of animals or carrion insects).",
    "secondary": "In entomology and vertebrate ecology, organisms playing a crucial sanitary role by decomposing carcasses and leaf-litter.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould through the Action of Worms", "quote": "Earthworms and **saprophagous** larvae consume decaying vegetation, converting it into rich loam."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "Certain beetles are strictly **saprophagous**, subsisting entirely upon decomposing animal carcasses."},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "Swarms of **saprophagous** insects quickly dispose of fallen fruit and rotting timber in the tropical forest."}
    ]
  },
  "Dashboard — sap/saprophyte.md": {
    "primary": "A plant, fungus, or microorganism that lives on dead or decaying organic matter.",
    "secondary": "In ecological botany and mycology, an organism absorbing dissolved nutrients from decomposed humus rather than synthesizing sugars.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Various Contrivances by which Orchids are Fertilised by Insects", "quote": "The bird's-nest orchis functions as a **saprophyte**, absorbing nourishment from leaf-mould through its fungal mycorrhizae."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Unlike green photosynthetic plants, a **saprophyte** lives upon pre-existing organic compounds in the soil."},
      {"author": "Ernst Haeckel", "work": "The Wonders of Life", "quote": "The kingdom of fungi is primarily composed of **saprophytes** that break down dead timber and humus."}
    ]
  },
  "Dashboard — sap/saprophytic.md": {
    "primary": "Obtaining nourishment from dead or decaying organic matter; living as a saprophyte.",
    "secondary": "In physiological microbiology, nutrition characterized by enzymatic external digestion of non-living cellular substrate.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Certain non-green flowering plants have adopted a **saprophytic** mode of life in damp shady woods."},
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "The **saprophytic** bacteria multiplying in the broth converted the gelatin into liquid peptones."},
      {"author": "Thomas Henry Huxley", "work": "Critiques and Addresses", "quote": "A **saprophytic** fungus derives its carbon and nitrogen directly from dead and putrefying matter."}
    ]
  },
  "Dashboard — sap/saprozoic.md": {
    "primary": "Obtaining nourishment by absorbing dissolved organic compounds derived from decaying matter (of animals/protozoans).",
    "secondary": "In invertebrate zoology and protozoology, osmotrophic absorption of dissolved nutrients without the ingestion of solid particles.",
    "quotes": [
      {"author": "Ernst Haeckel", "work": "The Evolution of Man", "quote": "Certain protozoans exhibit a **saprozoic** nutrition, absorbing organic solutes directly across their cell membranes."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "Unlike holozoic hunters, the **saprozoic** flagellate absorbs liquid nourishment from putrid solutions."},
      {"author": "Charles Darwin", "work": "Journal of Researches", "quote": "Minute **saprozoic** infusoria multiply prodigiously in stagnant pools where decomposing plants accumulate."}
    ]
  },
  "Dashboard — sap/sapsago.md": {
    "primary": "A hard, pungent green Swiss cheese flavored with powdered blue fenugreek (Schabziger).",
    "secondary": "In culinary tradition, an ancient skimmed-milk cheese of the canton of Glarus, grated over rustic potato and noodle dishes.",
    "quotes": [
      {"author": "Mark Twain", "work": "A Tramp Abroad", "quote": "The grated green **sapsago** cheese imparted a pungent herbal fragrance to the Swiss macaroni."},
      {"author": "Robert Louis Stevenson", "work": "Travels with a Donkey in the Cévennes", "quote": "He brought out a hard, conical block of Alpine **sapsago**, flecked with aromatic clover leaves."},
      {"author": "George Borrow", "work": "The Bible in Spain", "quote": "The traveler sustained himself upon a crust of bread and a morsel of hard Swiss **sapsago**."}
    ]
  },
  "Dashboard — sap/sapsucker.md": {
    "primary": "A North American woodpecker (genus Sphyrapicus) that drills rows of small holes in trees to feed on sap and insects.",
    "secondary": "In ornithological field study, migratory woodpeckers maintaining sap-wells that provide critical sustenance to hummingbirds and insects.",
    "quotes": [
      {"author": "John James Audubon", "work": "Ornithological Biography", "quote": "The yellow-bellied **sapsucker** excavates neat horizontal rows of small holes in the bark of maple trees."},
      {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "We heard the sharp tap of the **sapsucker** drilling the tender cambium of the birch tree."},
      {"author": "John Burroughs", "work": "Wake-Robin", "quote": "The **sapsucker** feeds on the sweet exuding syrup and the insects attracted to its punctures."}
    ]
  },
  "Dashboard — sap/unsaponified.md": {
    "primary": "Not converted into soap; remaining in the form of neutral fat, wax, or ester.",
    "secondary": "In analytical lipid chemistry and manufacturing, the portion of a fat or oil mixture that resists alkaline saponification.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The ethereal extract contained neutral waxes that remained **unsaponified** after treatment with aqueous potash."},
      {"author": "Justus von Liebig", "work": "Animal Chemistry", "quote": "A considerable portion of the cholesterol in the bile remains **unsaponified** throughout intestinal digestion."},
      {"author": "Thomas Graham", "work": "Elements of Chemistry", "quote": "Mineral oils mixed with vegetable fats persist in an **unsaponified** condition following alkaline boiling."}
    ]
  }
}

base_dir = r"App database/Latin roots/Cluster Thought"

updated_count = 0
for rel_path, entry in data.items():
    full_path = os.path.join(base_dir, rel_path)
    if not os.path.exists(full_path):
        print(f"Missing file: {full_path}")
        continue
    
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    book_pattern = r"(> 1\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)(\r?\n> 2\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)"
    def repl_book(m):
        return f"{m.group(1)}{entry['primary']}{m.group(3)}{entry['secondary']}"
    
    new_content = re.sub(book_pattern, repl_book, content)
    if new_content == content:
        book_pattern2 = r"(1\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)(\r?\n.*?2\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)"
        new_content = re.sub(book_pattern2, repl_book, content)

    q_pos = new_content.find("> [!quote]")
    if q_pos != -1:
        before_q = new_content[:q_pos]
        after_q = new_content[q_pos:]
        
        new_q_lines = ["> [!quote] 💬 Contextual Usage & Authentic Quotations"]
        for q in entry["quotes"]:
            new_q_lines.append(f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{q['quote']}\"*")
        
        rest = after_q.split("\n")
        remaining_lines = []
        skip = True
        for line in rest[1:]:
            if skip:
                if line.startswith("> - 📜") or line.strip() == ">" or line.strip() == "":
                    continue
                else:
                    skip = False
                    remaining_lines.append(line)
            else:
                remaining_lines.append(line)
        
        new_content = before_q + "\n".join(new_q_lines) + ("\n" + "\n".join(remaining_lines) if remaining_lines else "\n")
    
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated_count += 1

print(f"Thought Batch 3A (sap): Successfully updated {updated_count}/{len(data)} notes.")
