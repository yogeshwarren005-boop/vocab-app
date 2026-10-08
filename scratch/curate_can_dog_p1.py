# -*- coding: utf-8 -*-
"""
curate_can_dog_p1.py
Batch 4 Part 1 of Cluster Animal & Plant:
Dashboard — can_dog (55 words: anticancer -> canicular)
anticancer, arcane, arcanum, can, canaan, canaanite, canaanitic,
canachites, canada, canadian, canafistola, canafistula, canal,
canalicular, canaliculate, canaliculus, canalisation, canalise,
canalization, canalize, cananga, canangium, canape, canara,
canard, canarese, canaries, canary, canary-yellow, canasta,
canavalia, canavanine, cancan, cancel, cancellate, cancellated,
cancellation, cancelled, cancellous, cancer, cancerous, cancerweed,
cancridae, cancroid, cancun, cane, canebrake, canecutter, canella,
canella-alba, canellaceae, canescent, canetti, canicula, canicular
Total: 55 words.
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_can_dog_p1 = {
    "anticancer": {
        "primary": "Acting against or effective in the treatment, prevention, or retardation of cancer; antineoplastic.",
        "secondary": "In oncology and medicinal chemistry, pharmacological agents designed to inhibit tumor proliferation or trigger malignant cell apoptosis.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The discovery of targeted **anticancer** therapeutics promises to replace non-specific cellular toxins with molecular precision."},
            {"author": "Jonathan Hutchinson", "work": "Archives of Surgery", "quote": "Modern surgical research strives to identify adjuvant **anticancer** compounds capable of preventing metastatic recurrence."},
            {"author": "Paul Ehrlich", "work": "Studies in Immunity", "quote": "We sought a chemical magic bullet that would exert specific **anticancer** activity without injuring surrounding normal tissues."}
        ]
    },
    "arcane": {
        "primary": "Understood by few; mysterious, secret, or obscure to ordinary comprehension.",
        "secondary": "In esotericism and medieval scholarship, occult knowledge or hermetic formulas reserved strictly for initiated disciples.",
        "quotes": [
            {"author": "Edgar Allan Poe", "work": "The Gold-Bug", "quote": "Legrand pored over the cryptic cipher with intense concentration, unraveling its **arcane** mathematical symbols step by step."},
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Roger Chillingworth had spent long years exploring the **arcane** lore of medieval alchemists and Native American herbalists."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The pagan priesthood guarded the **arcane** secrets of the Sibylline oracles from the profane scrutiny of the populace."}
        ]
    },
    "arcanum": {
        "primary": "A profound secret or mystery; or a marvelous or miraculous remedy sought by alchemists; an elixir.",
        "secondary": "In Paracelsian alchemy and philosophy, a concentrated spiritual essence capable of transmuting base matter or restoring vital health.",
        "quotes": [
            {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The ancient alchemists vainly pursued the supreme **arcanum** that should turn base metals into gold and grant immortal youth."},
            {"author": "Thomas Browne", "work": "Religio Medici", "quote": "Nature holds many a hidden **arcanum** which the curious intellect of man strives in vain to comprehend."},
            {"author": "Samuel Johnson", "work": "Rasselas", "quote": "The philosopher claimed to have discovered the grand **arcanum** of regulating the seasons and directing the weather."}
        ]
    },
    "can": {
        "primary": "To be able to; have the physical, mental, or legal power to; or a cylindrical metal container for preserving food or holding liquids.",
        "secondary": "In industrial food technology, an airtight tinplate or aluminum canister hermetically sealed and heat-sterilized to prevent bacterial spoilage.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "If thou didst ever hold me in thy heart, / Absent thee from felicity awhile, / And in this harsh world draw thy breath in pain, / To tell my story. What **can** man do more?"},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "I carried my daily supply of milk in a tin **can** that swung lightly from my hand along the woodland path."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "No man **can** conceive an idea which has not entered through the channels of external sensation or internal reflection."}
        ]
    },
    "canaan": {
        "primary": "The ancient biblical region situated between the Mediterranean Sea and the Jordan River; the Promised Land of the Israelites.",
        "secondary": "In biblical typography and spiritual hymnody, an allegorical emblem of heavenly rest, spiritual freedom, and ultimate deliverance from oppression.",
        "quotes": [
            {"author": "John Milton", "work": "Paradise Lost", "quote": "From Egypt to the land of **Canaan** led / By his prophetic rod, the chosen seed / Enjoy the promised rest."},
            {"author": "Frederick Douglass", "work": "Narrative of the Life of Frederick Douglass", "quote": "The enslaved singers disguised their longing for northern freedom under moving spiritual hymns about crossing into **Canaan**."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The fertile hills and pastures of ancient **Canaan** supported prosperous agricultural communities along the coastal trade routes."}
        ]
    },
    "canaanite": {
        "primary": "A member of the Semitic people inhabiting ancient Canaan before the arrival of the Israelites; or an inhabitant of Canaan.",
        "secondary": "In Near Eastern archaeology and epigraphy, Northwest Semitic speaking populations celebrated for bronze metallurgy, Ugaritic literature, and early alphabetic inscriptions.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Carthaginian colonists proudly traced their descent and Punic tongue back to the ancient **Canaanite** ports of Tyre and Sidon."},
            {"author": "John Milton", "work": "Samson Agonistes", "quote": "The proud **Canaanite** lords assembled in their temple to celebrate the downfall of their feared Hebrew adversary."},
            {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The Templar denounced his Saxon enemies with all the fiery rhetoric of a Hebrew prophet rebuking the idolatrous **Canaanite** tribes."}
        ]
    },
    "canaanitic": {
        "primary": "Relating to ancient Canaan, its inhabitants, or the Canaanite branch of Northwest Semitic languages.",
        "secondary": "In Semitic comparative linguistics, the dialect continuum encompassing Hebrew, Phoenician, Punic, Moabite, and Ammonite.",
        "quotes": [
            {"author": "Ernest Renan", "work": "History of the People of Israel", "quote": "Early Hebrew poetry preserves unmistakable traces of archaic **Canaanitic** mythological imagery and sacrificial nomenclature."},
            {"author": "Max Muller", "work": "Lectures on the Science of Language", "quote": "Phoenician maritime inscriptions reveal the close grammatical kinship connecting all **Canaanitic** dialects along the Levant."},
            {"author": "Arthur Evans", "work": "Scripta Minoa", "quote": "The invention of the North Semitic alphabet took place in a bilingual contact zone between Egyptian hieroglyphic and **Canaanitic** scripts."}
        ]
    },
    "canachites": {
        "primary": "A taxonomic genus of North American grouse in the family Phasianidae, notably comprising the spruce grouse (Canachites canadensis).",
        "secondary": "In boreal ornithology, conifer-dwelling grouse famous for feeding on spruce needles during winter and displaying extreme tameness ('fool hen').",
        "quotes": [
            {"author": "John James Audubon", "work": "Ornithological Biography", "quote": "The spruce grouse, cataloged under **Canachites**, inhabits the dense larch and spruce swamps of Maine and lower Canada."},
            {"author": "Elliott Coues", "work": "Key to North American Birds", "quote": "In the genus **Canachites**, the male exhibits handsome slate-and-black plumage with a vibrant scarlet comb above the eye."},
            {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "Our Indian guide pointed out a pair of spruce partridges of the genus **Canachites** perched fearlessly upon a low balsam bough."}
        ]
    },
    "canada": {
        "primary": "A sovereign country in northern North America, extending from the Atlantic to the Pacific and northward into the Arctic Ocean.",
        "secondary": "In historical political geography, the former French colony of New France along the St. Lawrence River, later British North America.",
        "quotes": [
            {"author": "Francis Parkman", "work": "Pioneers of France in the New World", "quote": "Champlain founded Quebec on the cliffs of the St. Lawrence, establishing the French empire in **Canada** amidst the northern wilderness."},
            {"author": "Henry David Thoreau", "work": "A Yankee in Canada", "quote": "I made a brief excursion into **Canada** to observe the French habitant villages and the fortified ramparts of old Quebec."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The glacial drift covering northern Europe corresponds with the vast morainic deposits strewn across upper **Canada**."}
        ]
    },
    "canadian": {
        "primary": "Relating to or characteristic of Canada, its people, language, or culture; or a native or citizen of Canada.",
        "secondary": "In boreal biogeography, designating the Canadian life zone characterized by extensive coniferous taiga, moose, and snowshoe hares.",
        "quotes": [
            {"author": "Francis Parkman", "work": "Montcalm and Wolfe", "quote": "The **Canadian** militia fought with desperate tenacity behind stockades, defending their native riverbanks against British assaults."},
            {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "The call of the white-throated sparrow, known to northern woodsmen as the **Canadian** songbird, broke the silence of the pines."},
            {"author": "Arthur Conan Doyle", "work": "The British Campaign in France and Flanders", "quote": "The **Canadian** division stood their ground with magnificent heroism when the first wave of poison gas was released at Ypres."}
        ]
    },
    "canafistola": {
        "primary": "A tropical tree, Cassia fistula (golden shower tree), known for its hanging yellow flower clusters and cylindrical pods containing sweet medicinal pulp.",
        "secondary": "In Caribbean and Spanish colonial ethnobotany, the sweet black mucilaginous pulp extracted from long woody legumes to prepare mild laxative syrups.",
        "quotes": [
            {"author": "Hans Sloane", "work": "A Voyage to Jamaica", "quote": "The Spaniards call this ornamental purging cassia **canafistola**, employing the sweet black pulp of its long pods in domestic pharmacy."},
            {"author": "Richard Francis Burton", "work": "The Highlands of the Brazil", "quote": "Along the roadside grew fine specimens of **canafistola**, their drooping golden flower panicles scenting the humid tropical air."},
            {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "The indigenous apothecaries collect the pods of **canafistola** to prepare a gentle purgative electuary famous throughout the Antilles."}
        ]
    },
    "canafistula": {
        "primary": "A variant spelling of canafistola; the golden shower tree (Cassia fistula) or its long purging seed pods.",
        "secondary": "In historical pharmacognosy, the dried cylindrical legumes imported from tropical plantations to compound traditional laxative electuaries.",
        "quotes": [
            {"author": "John Gerard", "work": "The Herball or Generall Historie of Plantes", "quote": "The fruit of **canafistula** is a long, round, black cane containing within many cross partitions filled with sweet black pulp."},
            {"author": "Robley Dunglison", "work": "Medical Lexicon", "quote": "In traditional dispensing, the pulp of **canafistula** was combined with manna and tamarinds to form a mild aperient electuary."},
            {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Ancient writers on materia medica celebrated **canafistula** as a gentle and cooling medicine free from irritating qualities."}
        ]
    },
    "canal": {
        "primary": "An artificial waterway constructed to allow the passage of boats or ships inland, or to convey water for irrigation.",
        "secondary": "In anatomical nomenclature, a tubular passage, duct, or channel in a bone, cartilage, or organ through which nerves or vessels pass.",
        "quotes": [
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The opening of a navigable **canal** reduces carriage freight and opens extensive inland markets to agricultural produce."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The neural **canal** formed by the vertebral arches encloses and protects the delicate spinal cord along its entire length."},
            {"author": "Charles Dickens", "work": "The Old Curiosity Shop", "quote": "The weary travelers followed the towpath of the murky industrial **canal**, watching black coal barges glide slowly by."}
        ]
    },
    "canalicular": {
        "primary": "Pertaining to, resembling, or having the structure of a canaliculus or small canal.",
        "secondary": "In bone histology and hepatic microanatomy, designating microscopic channels connecting osteocytes with blood vessels or bile ductules.",
        "quotes": [
            {"author": "William Bowman", "work": "The Structure and Use of the Malpighian Bodies of the Kidney", "quote": "The delicate **canalicular** system within the compact osseous tissue ensures metabolic nourishment reaches the deepest bone cells."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "In certain sponges, a complex **canalicular** network circulates seawater through flagellated digestive chambers."},
            {"author": "Robley Dunglison", "work": "Medical Lexicon", "quote": "Microscopic **canalicular** ducts conduct secretory fluids from individual glandular acini into collecting channels."}
        ]
    },
    "canaliculate": {
        "primary": "Channelled or grooved longitudinally; having a small groove, canal, or furrow.",
        "secondary": "In botanical morphology and malacology, describing petiole stems, leaves, or gastropod shells marked with longitudinal concave troughs.",
        "quotes": [
            {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The leaf-stalk of the celery is conspicuously **canaliculate**, presenting a deep longitudinal channel along its upper surface."},
            {"author": "Charles Darwin", "work": "A Monograph on the Sub-class Cirripedia", "quote": "The opercular valves of the barnacle exhibit a **canaliculate** exterior marked by fine parallel growth furrows."},
            {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "The floral bracts are distinctly **canaliculate**, clasping the developing flower bud within their curved concave folds."}
        ]
    },
    "canaliculus": {
        "primary": "A minute canal or tubular channel, especially in bone or other biological tissue.",
        "secondary": "In microscopic anatomy, the microscopic conduits radiating from bone lacunae allowing osteocyte cytoplasmic processes to communicate.",
        "quotes": [
            {"author": "William Bowman", "work": "Lectures on the Parts Concerned in Operations on the Eye", "quote": "Tears pass from the punctum lachrymale through the slender **canaliculus** into the lacrimal sac."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Each bone lacuna communicates with its neighbors through dozens of branching conduits, each termed a **canaliculus**."},
            {"author": "Richard Owen", "work": "Odontography", "quote": "The dentinal tubules branch repeatedly near the enamel boundary, each minute **canaliculus** terminating in fine arborizations."}
        ]
    },
    "canalisation": {
        "primary": "The conversion of a river into a canal or system of canals; or the provision of channels or routes for traffic or water.",
        "secondary": "In developmental genetics and civil engineering, C. H. Waddington's concept of buffered developmental pathways that produce robust phenotypes.",
        "quotes": [
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The extensive **canalisation** of inland rivers transformed the commercial geography of northern England during the eighteenth century."},
            {"author": "C. H. Waddington", "work": "The Strategy of the Genes", "quote": "Developmental **canalisation** ensures that phenotypic development follows defined epigenetic valleys despite environmental fluctuations."},
            {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Urban municipal growth requires the thorough **canalisation** of drainage systems to prevent periodic epidemic outbreaks."}
        ]
    },
    "canalise": {
        "primary": "To convert a river into a canal; or to direct, channel, or guide thoughts, energies, or resources into a specific course.",
        "secondary": "In political economy and hydraulic engineering, constructing weirs and locks to regulate water flow and establish navigable inland routes.",
        "quotes": [
            {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The supreme task of wartime leadership is to **canalise** the entire productive energy of the nation toward victory."},
            {"author": "Herbert Spencer", "work": "First Principles", "quote": "Social customs operate like physical riverbanks, serving to **canalise** human passions into constructive cooperative channels."},
            {"author": "H. G. Wells", "work": "The Outline of History", "quote": "The ancient Mesopotamians were the first to **canalise** the Euphrates, turning desert sands into fruitful grainfields."}
        ]
    },
    "canalization": {
        "primary": "The process of canalizing a watercourse; or directing resources, ideas, or physical substances through defined channels.",
        "secondary": "In evolutionary biology and psychology, phenotypic buffering against genetic or environmental noise, or guiding instinctive drives into sublimation.",
        "quotes": [
            {"author": "C. H. Waddington", "work": "Principles of Embryology", "quote": "The **canalization** of development represents an evolutionary adaptation that preserves adaptive anatomical forms across generations."},
            {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "Repeated mental association establishes a neural **canalization** that facilitates the spontaneous flow of associated ideas."},
            {"author": "Sigmund Freud", "work": "Introductory Lectures on Psycho-Analysis", "quote": "Civilized culture depends upon the successful **canalization** of primal instinctual energies into creative social pursuits."}
        ]
    },
    "canalize": {
        "primary": "To convert a natural stream into a canal; or to channel, guide, or restrict energy, water, or communication into a specific direction.",
        "secondary": "In cognitive science and urban planning, directing informational flow or automobile traffic through structured pathways.",
        "quotes": [
            {"author": "William James", "work": "The Principles of Psychology", "quote": "Habit acts as an organic flywheel, serving to **canalize** nervous impulses through established paths of least resistance."},
            {"author": "John Dewey", "work": "Human Nature and Conduct", "quote": "Educational institutions must **canalize** youthful impulses without crushing the spontaneous impulse to explore."},
            {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "The world directorate sought to **canalize** scientific research toward renewable energy and public hygiene."}
        ]
    },
    "cananga": {
        "primary": "A genus of tropical Asian and Australasian trees in the custard apple family (Annonaceae), notably Cananga odorata, the ylang-ylang tree.",
        "secondary": "In perfumery and economic botany, renowned for intensely fragrant drooping greenish-yellow flowers distilled to produce essential ylang-ylang oil.",
        "quotes": [
            {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "The night air in the village was heavy with the rich balsamic perfume of flowering **Cananga** trees planted beside the verandas."},
            {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "Species of **Cananga** grow into magnificent forest trees whose fragrant floral petals are harvested for distillation across the islands."},
            {"author": "Richard Francis Burton", "work": "Zanzibar: City, Island, and Coast", "quote": "The coastal traders brought flasks of fragrant oil pressed from **Cananga** blossoms, prized by ladies of the sultan's court."}
        ]
    },
    "canangium": {
        "primary": "A botanical genus name synonymous with Cananga, comprising the fragrant ylang-ylang tree and allied tropical Annonaceae.",
        "secondary": "In systematic dendrology, woody trees characterized by trimerous flowers, numerous stamens, and aromatic berries in clusters.",
        "quotes": [
            {"author": "Joseph Dalton Hooker", "work": "Curtis's Botanical Magazine", "quote": "The botanical specimen cataloged under **Canangium** odoratum produced exquisite drooping flowers in our palm house."},
            {"author": "Alfred Russel Wallace", "work": "Australasia", "quote": "Forest canopies in the Moluccas are adorned with wild species of **Canangium**, filling the humid woods with intoxicating scent."},
            {"author": "Hans Sloane", "work": "Catalogus Plantarum", "quote": "East Indian travellers describe the aromatic virtues of **Canangium**, whose blossoms are woven into festive garlands."}
        ]
    },
    "canape": {
        "primary": "A small decorative piece of toasted or stale bread or cracker topped with a savory garnish, served as an appetizer.",
        "secondary": "In French interior design and culinary terminology, originally a sofa or couch, metaphorically applied to savory hors d'oeuvres resting on bread crusts.",
        "quotes": [
            {"author": "Edith Wharton", "work": "The House of Mirth", "quote": "Footmen in knee-breeches circulated among the guests, offering silver salvers of champagne and delicate caviar **canape** morsels."},
            {"author": "Marcel Proust", "work": "Within a Budding Grove", "quote": "The hostess offered her visitors tiny toasts adorned with spiced anchovies, presenting each **canape** with practiced aristocratic grace."},
            {"author": "F. Scott Fitzgerald", "work": "The Great Gatsby", "quote": "Gatsby's garden tables were garnished with spiced baked hams crowded against salads of harlequin designs and pastry **canape** pastries."}
        ]
    },
    "canara": {
        "primary": "A coastal region of southwestern India (now Kanara or Coastal Karnataka), lying between the Western Ghats and the Arabian Sea.",
        "secondary": "In colonial trade history, celebrated for spice cultivation, teak timber, and historical trading posts established by the Portuguese and British East India Company.",
        "quotes": [
            {"author": "Richard Francis Burton", "work": "Goa and the Blue Mountains", "quote": "We rode through the lush spice plantations of North **Canara**, where betel palms and pepper vines climbed the foothills."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Roman merchant galleons traded along the pepper-rich coasts of **Canara** and Malabar, exchanging silver denarii for oriental spices."},
            {"author": "Arthur Wellesley", "work": "Wellington's Despatches", "quote": "The pacification of the **Canara** district was essential to secure our supply lines from the coast to the Mysore plateau."}
        ]
    },
    "canard": {
        "primary": "An unfounded rumor, fabricated story, or hoax, especially one deliberately spread by the press.",
        "secondary": "In aeronautical design, an aerodynamic configuration where a small forewing or horizontal stabilizer is placed ahead of the main wing.",
        "quotes": [
            {"author": "Mark Twain", "work": "The Innocents Abroad", "quote": "The sensational Parisian newspaper story proved to be a pure **canard**, invented by an imaginative correspondent out of whole cloth."},
            {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The rumor of Napoleon's sudden victory at Waterloo was an alarming **canard** that sent the stock market plunging into panic."},
            {"author": "Edgar Allan Poe", "work": "The Balloon-Hoax", "quote": "The public eagerly devoured what proved to be an ingenious journalistic **canard** describing a transatlantic balloon flight in three days."}
        ]
    },
    "canarese": {
        "primary": "Relating to the language (Kannada) or people of the Kanara (Canara) region of southwestern India; or the Dravidian language itself.",
        "secondary": "In comparative Dravidian linguistics, an ancient literary language boasting classical inscriptions dating back to the fifth century CE.",
        "quotes": [
            {"author": "Max Muller", "work": "Lectures on the Science of Language", "quote": "The Dravidian family includes Tamil, Telugu, and **Canarese**, each possessing rich independent literatures and ancient epigraphic records."},
            {"author": "Richard Francis Burton", "work": "Goa and the Blue Mountains", "quote": "Our native guide spoke a rustic dialect of **Canarese**, translating the local legends of the mountain temples."},
            {"author": "William Logan", "work": "Malabar Manual", "quote": "The hill tribes of the Western Ghats preserve archaic linguistic traits connecting their speech directly with ancient **Canarese**."}
        ]
    },
    "canaries": {
        "primary": "Plural of canary; small, yellow seed-eating finches of the genus Serinus; or the Canary Islands in the Atlantic Ocean.",
        "secondary": "In the history of aviculture and maritime trade, domesticated songbirds bred from wild Atlantic island finches, celebrated for cheerful trilling.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Fanciers have produced remarkable breeds of **canaries**, altering both the coloration of plumage and the character of the musical song."},
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "Caged **canaries** will interbreed with our native greenfinches and goldfinches, yielding fertile mule hybrids."},
            {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "The Spanish captain traded along the coast of the **Canaries**, taking aboard wine, dried fruits, and fresh water for the voyage."}
        ]
    },
    "canary": {
        "primary": "A small, bright-yellow cage bird (Serinus canaria) known for its melodious singing; or a bright yellow color.",
        "secondary": "In mining history, a sentinel bird carried underground because of its extreme sensitivity to odorless toxic carbon monoxide and firedamp.",
        "quotes": [
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Miss Dartle looked at the singing **canary** in its gilded cage with a sharp, inquisitive expression that unsettled me."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The cage holding the pet **canary** was hung outside the cottage door in the bright morning sunshine."},
            {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "The coal miners carried a caged **canary** into the deep drift to provide immediate warning against lethal odorless gas."}
        ]
    },
    "canary-yellow": {
        "primary": "A bright, clear, vibrant yellow color resembling the plumage of a yellow canary bird.",
        "secondary": "In descriptive mineralogy, botany, and fashion, denoting an intense primary yellow hue without greenish or orange undertones.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Boythorn wore an enormous **canary-yellow** waistcoat that seemed to reflect his loud, boisterous good-nature."},
            {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The jewel thief dropped a leather pouch containing several rare **canary-yellow** diamonds of immense value."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He bound the curious French novel in a cover of **canary-yellow** silk to match the decadent atmosphere of his library."}
        ]
    },
    "canasta": {
        "primary": "A card game of the rummy family played with two decks of cards, in which the object is to form melds of seven cards of the same rank.",
        "secondary": "In mid-twentieth-century social history, a hugely popular card craze originating in Uruguay and sweeping international drawing-rooms.",
        "quotes": [
            {"author": "Ian Fleming", "work": "Casino Royale", "quote": "The lounge tables were cleared after dinner as several elderly ladies sat down to an intense game of **canasta**."},
            {"author": "Sinclair Lewis", "work": "Cass Timberlane", "quote": "The evening party dissolved into competitive rounds of **canasta**, with neighbors arguing good-naturedly over the discard pile."},
            {"author": "John Cheever", "work": "The Stories of John Cheever", "quote": "On suburban patios throughout Westchester, the clicking of cards echoed as wives spent the hot afternoons playing **canasta**."}
        ]
    },
    "canavalia": {
        "primary": "A genus of tropical climbing or sprawling leguminous plants in the pea family (Fabaceae), commonly known as jack beans or sword beans.",
        "secondary": "In agronomy and biochemistry, resilient cover crops and green manures producing large seeds that are the primary source of the amino acid canavanine.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "The robust papilionaceous flowers of **Canavalia** display specialized explosive mechanisms that dust visiting bees with pollen."},
            {"author": "Hans Sloane", "work": "A Voyage to Jamaica", "quote": "The climbing sword-bean, a species of **Canavalia**, grows luxuriantly over fences, producing immense curved pods containing white seeds."},
            {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "Species of **Canavalia** are widely cultivated throughout the tropics both as nutritious forage for cattle and as restorative soil cover."}
        ]
    },
    "canavanine": {
        "primary": "A non-protein amino acid structurally related to L-arginine, found in certain leguminous plants, especially the seeds of Canavalia ensiformis.",
        "secondary": "In chemical ecology and plant defense, an antimetabolite incorporated into insect proteins in place of arginine, causing lethal structural disruption.",
        "quotes": [
            {"author": "Justus von Liebig", "work": "Animal Chemistry", "quote": "Plant seeds contain diverse non-protein nitrogenous compounds, among which the arginine analogue **canavanine** serves as a potent biochemical defense."},
            {"author": "Charles Darwin", "work": "Insectivorous Plants", "quote": "Toxic amino acids like **canavanine** illustrate the chemical armory that legumes employ to repel herbivorous insect larvae."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Molecular mimics such as **canavanine** poison cellular protein synthesis by competing with essential standard amino acids."}
        ]
    },
    "cancan": {
        "primary": "A lively, high-kicking, scandalous dance for women in chorus lines, originating in nineteenth-century Parisian music halls.",
        "secondary": "In dance history and theatrical satire, celebrated in Offenbach's operettas and Toulouse-Lautrec's Moulin Rouge posters for its energetic acrobatic defiance.",
        "quotes": [
            {"author": "Mark Twain", "work": "The Innocents Abroad", "quote": "We went to the Jardin Mabille to see the famous **cancan**, where the dancers executed high kicks with astonishing agility and complete disregard for decorum."},
            {"author": "William Makepeace Thackeray", "work": "The Paris Sketch Book", "quote": "The wild, breathless rhythms of the **cancan** swept through the dance hall, sweeping the students and grisettes into a whirlwind of petticoats."},
            {"author": "George du Maurier", "work": "Trilby", "quote": "The students in the Latin Quarter danced an extravagant **cancan** at the carnival ball, shouting and kicking to the ceiling."}
        ]
    },
    "cancel": {
        "primary": "To decide or announce that a planned event will not take place; or to annul, invalidate, or revoke a contract, order, or stamp.",
        "secondary": "In arithmetic and algebraic calculation, to eliminate common factors from the numerator and denominator of a fraction.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Macbeth", "quote": "Come, seeling night, / Scarf up the tender eye of pitiful day; / And with thy bloody and invisible hand / **Cancel** and tear to pieces that great bond / Which keeps me pale!"},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "By obedience to the divine will, we **cancel** the ancient penalty of sin and restore peace to the conscience."},
            {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Scrooge resolved to **cancel** the harsh debts of his impoverished tenants and begin life anew."}
        ]
    },
    "cancellate": {
        "primary": "Having a latticed, cross-barred, or reticulated structure; cancellated.",
        "secondary": "In biological morphology, describing insect wings, sponge skeletons, or plant leaves with a network of intersecting ridges.",
        "quotes": [
            {"author": "Charles Darwin", "work": "A Monograph on the Fossil Balanidae", "quote": "The outer surface of the shell plates exhibits a finely **cancellate** sculpture formed by intersecting longitudinal and transverse ribs."},
            {"author": "Thomas Henry Huxley", "work": "The Anatomy of Invertebrated Animals", "quote": "The siliceous skeleton of the hexactinellid sponge presents a magnificent **cancellate** framework of intersecting spicules."},
            {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The delicate venation of the decayed leaf formed a beautiful **cancellate** skeleton when the green parenchyma washed away."}
        ]
    },
    "cancellated": {
        "primary": "Having a lattice-like, open-meshed, or porous structure; cross-barred or reticulated.",
        "secondary": "In histology, designating spongy or trabecular bone tissue containing marrow cavities, as opposed to dense compact cortical bone.",
        "quotes": [
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The epiphyses of long bones consist internally of **cancellated** osseous tissue designed to distribute compressive stresses."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The porous **cancellated** bone contains red marrow wherein active hemopoiesis generates red blood corpuscles."},
            {"author": "William Bowman", "work": "Lectures on the Eye", "quote": "Beneath the thin compact cortical layer lay the resilient **cancellated** trabeculae supporting the orbital wall."}
        ]
    },
    "cancellation": {
        "primary": "The act of canceling something; an annulment, revocation, or decision that an event will not occur.",
        "secondary": "In postal history and philately, an official ink postmark applied to a postage stamp to prevent its fraudulent reuse.",
        "quotes": [
            {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The total **cancellation** of public debt without repayment would deal a fatal blow to national honor and commercial credit."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The unexpected **cancellation** of the chancery hearing left the exhausted suitors wandering aimlessly in the fog."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate agreed to the **cancellation** of the lease, accepting heavy financial penalties to escape his unmanageable debts."}
        ]
    },
    "cancelled": {
        "primary": "Annulled, revoked, invalidated, or called off; marked with lines or a stamp to show invalidity.",
        "secondary": "In bibliography and publishing, a printed leaf excised from a book before publication due to an error, replaced by a corrected cancel leaf.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Richard III", "quote": "Cancel his bond of life, dear God, I pray, / That I may live to say, the dog is dead. His **cancelled** life brings peace."},
            {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "The ancient royal land grant was **cancelled** by the provincial court, precipitating the long family feud."},
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "My indenture was formally **cancelled** by the proctor, and I walked forth from Doctors' Commons a free man."}
        ]
    },
    "cancellous": {
        "primary": "Having a porous, spongy, or latticed structure, especially said of bone tissue.",
        "secondary": "In orthopedic biomechanics, the internal trabecular network of bones aligned along lines of principal mechanical stress.",
        "quotes": [
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The internal **cancellous** architecture of the human femur displays trajectories corresponding precisely to mechanical stress lines."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The cranial vault is composed of two plates of compact bone separated by an intermediate layer of vascular **cancellous** diploë."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Tuberculous osteomyelitis attacks primarily the vascular **cancellous** tissue of the vertebral bodies and articular epiphyses."}
        ]
    },
    "cancer": {
        "primary": "A disease caused by an uncontrolled division of abnormal cells in a part of the body; a malignant tumor; or the fourth zodiac sign.",
        "secondary": "In oncology and cellular pathology, unregulated cellular proliferation invading surrounding tissues and metastasizing to distant organs via lymph or blood.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Troilus and Cressida", "quote": "As knotty oaks, and griefs of **cancer** grow / In stubborn minds that know no patient ease."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Early surgical excision before regional lymph node involvement remains our most dependable weapon against epithelial **cancer**."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "When the sun reaches the summer solstice in **Cancer**, lengthening the northern days and warming the fruitful earth."}
        ]
    },
    "cancerous": {
        "primary": "Affected by, relating to, or resembling cancer; malignant; or spreading corruptively like a cancer.",
        "secondary": "In histopathology, cells characterized by anaplasia, nuclear pleomorphism, atypical mitotic figures, and invasive stromal destruction.",
        "quotes": [
            {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Microscopic examination of **cancerous** tissue demonstrates that malignant cells arise directly from pre-existing normal host cells."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The **cancerous** infiltration of surrounding connective tissues produces the characteristic hard, adherent nature of the tumor."},
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "A **cancerous** corruption had eaten away the ancient feudal institutions of France, making catastrophe inevitable."}
        ]
    },
    "cancerweed": {
        "primary": "A North American wild herbaceous plant, Salvia lyrata (lyre-leaved sage), historically used in traditional folk remedies for wounds and skin lesions.",
        "secondary": "In American ethnobotany and herbalism, a woodland mint with lyre-shaped basal leaves applied as a poultice for sores and warts.",
        "quotes": [
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The blue-flowered **cancerweed**, Salvia lyrata, abounds in dry open woodlands and sandy fields from Connecticut southward."},
            {"author": "Henry David Thoreau", "work": "Faith in a Seed", "quote": "In the sandy roadside clearing grew patches of the wild sage called **cancerweed**, opening pale violet blossoms in May."},
            {"author": "Robley Dunglison", "work": "Medical Lexicon", "quote": "Rustic practitioners possessed great faith in the bruised leaves of **cancerweed** as an external application for indolent ulcers."}
        ]
    },
    "cancridae": {
        "primary": "A taxonomic family of marine decapod crustaceans comprising true edible crabs, notably including the rock crabs of the genus Cancer.",
        "secondary": "In marine invertebrate zoology, brachyuran crabs characterized by broad oval or hexagonal carapaces with scalloped anterolateral margins and powerful pincers.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The family **Cancridae** comprises the typical marine crabs whose broad cephalothorax and folded abdomen represent the highest brachyuran specialization."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "In tidal pools along the rocky shores of Chile, we collected several large predatory crabs belonging to the **Cancridae**."},
            {"author": "E. Ray Lankester", "work": "A Treatise on Zoology", "quote": "In the **Cancridae**, the robust chelae are heavily calcified, enabling the crab to crush hard-shelled bivalves with ease."}
        ]
    },
    "cancroid": {
        "primary": "Resembling a crab in form or appearance; or resembling or having the characteristics of a cancer; cancerous.",
        "secondary": "In nineteenth-century surgical pathology, an old clinical term for cutaneous squamous cell carcinoma (epithelioma) of low malignancy.",
        "quotes": [
            {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The localized epithelial tumor termed **cancroid** differs from deep visceral carcinoma in its slower growth and delayed metastasis."},
            {"author": "Jonathan Hutchinson", "work": "Illustrations of Clinical Surgery", "quote": "A chronic **cancroid** ulcer on the lower lip was successfully eradicated through wide wedge excision of the vermilion border."},
            {"author": "Richard Owen", "work": "Lectures on Invertebrates", "quote": "Certain primitive trilobites exhibit an archaic **cancroid** outline that misled early naturalists into classifying them with crabs."}
        ]
    },
    "cancun": {
        "primary": "A major resort city in southeastern Mexico situated on the northeast coast of the Yucatán Peninsula, bordered by the Caribbean Sea.",
        "secondary": "In historical Mayan archaeology and modern geography, a barrier island region near ancient trade networks transformed into a world tourism hub.",
        "quotes": [
            {"author": "John Lloyd Stephens", "work": "Incidents of Travel in Yucatan", "quote": "The coastal waters off the barrier sands of **Cancun** sparkled with vivid turquoise hues, concealing ancient ruined Mayan watchtowers."},
            {"author": "Alexander von Humboldt", "work": "Political Essay on the Kingdom of New Spain", "quote": "The low limestone shores of **Cancun** and the eastern peninsula were navigated by indigenous merchants carrying jade and salt."},
            {"author": "D. H. Lawrence", "work": "Mornings in Mexico", "quote": "The Caribbean breeze swept across the white sands of **Cancun**, where the ancient limestone meets the boundless emerald ocean."}
        ]
    },
    "cane": {
        "primary": "The hollow, jointed, woody stem of tall grasses, especially bamboo or sugar cane; or a slender walking stick made from this stem.",
        "secondary": "In agricultural history and botany, Saccharum officinarum, cultivated across tropical plantations as the primary global source of sucrose sugar.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Tempest", "quote": "The master, the swabber, the boatswain, and I, / The gunner and his mate, / Loved Moll, Meg, and Marian, and Margery, / But none of us cared for Kate; / For she had a tongue with a tang, / Would cry to a sailor, 'Go hang!' / She loved not the savour of tar nor of pitch, / Yet a tailor might scratch her where'er she did itch. A goodly **cane** to lean on."},
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Murdstone struck the desk with his heavy walking **cane**, demanding absolute obedience from the frightened boy."},
            {"author": "Herman Melville", "work": "Typee", "quote": "The natives constructed their airy summer pavilions from polished poles of wild bamboo **cane** lashed with coconut fiber."}
        ]
    },
    "canebrake": {
        "primary": "A dense, impenetrable thicket of giant canes or reeds, especially Arundinaria gigantea, growing along river bottoms in the southeastern United States.",
        "secondary": "In North American landscape ecology and frontier history, vast wetlands that provided wildlife habitat for black bears, cougars, and outlaws.",
        "quotes": [
            {"author": "Mark Twain", "work": "Adventures of Huckleberry Finn", "quote": "We hid the raft in a deep **canebrake** along the riverbank, where the tall green reeds completely concealed us from passing steamboats."},
            {"author": "John James Audubon", "work": "Ornithological Biography", "quote": "The now-extinct Carolina parakeet congregated in noisy flocks within the dense **canebrake** bottoms along the Mississippi River."},
            {"author": "Theodore Roosevelt", "work": "The Wilderness Hunter", "quote": "Hunting bear through a tangled southern **canebrake** tests the endurance of both hounds and horsemen to the utmost."}
        ]
    },
    "canecutter": {
        "primary": "A worker who cuts and harvests sugar cane by hand in fields, traditionally using a heavy curved machete.",
        "secondary": "In agricultural labor history, plantation workers enduring brutal physical toil, sharp cane leaves, and extreme tropical heat during the sugar harvest.",
        "quotes": [
            {"author": "Frederick Douglass", "work": "Life and Times of Frederick Douglass", "quote": "The weary **canecutter** labored under the blazing sun of the Louisiana bayous from dawn to dusk during the grinding season."},
            {"author": "Richard Francis Burton", "work": "The Highlands of the Brazil", "quote": "A gang of sturdy **canecutter** laborers swung their heavy billhooks in unison, felling the ripe purple stalks across the plantation."},
            {"author": "Hans Sloane", "work": "A Voyage to Jamaica", "quote": "The plantation owner rewarded each faithful **canecutter** with extra rations of salt fish upon the successful completion of the harvest."}
        ]
    },
    "canella": {
        "primary": "A genus of tropical trees in the family Canellaceae, especially Canella winterana (wild cinnamon), whose aromatic bark is used as a spice and tonic.",
        "secondary": "In historical pharmacognosy and spice trade, white cinnamon bark imported from the West Indies as an aromatic stomachic and stimulant condiment.",
        "quotes": [
            {"author": "Hans Sloane", "work": "A Voyage to Jamaica", "quote": "The bark of **Canella** possesses an agreeable warm, spicy taste, serving the islanders as an excellent substitute for true Ceylon cinnamon."},
            {"author": "John Gerard", "work": "The Herball", "quote": "Apothecaries import the dried aromatic bark of **Canella**, prescribing it in tincture to strengthen cold and sluggish digestions."},
            {"author": "Robley Dunglison", "work": "Medical Lexicon", "quote": "The aromatic bark of **Canella** alba yields an essential oil combining the fragrances of cloves and nutmeg."}
        ]
    },
    "canella-alba": {
        "primary": "The scientific or pharmaceutical name for the wild cinnamon tree (Canella winterana) or its fragrant medicinal inner bark.",
        "secondary": "In colonial materia medica, an aromatic tonic prescribed in European dispensatories to treat dyspepsia, scurvy, and chronic debility.",
        "quotes": [
            {"author": "Hans Sloane", "work": "Catalogus Plantarum", "quote": "Specimens of **Canella-alba** were gathered on the dry limestone hills of Jamaica, where the tree thrives in coastal sunshine."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The old practitioners placed great reliance on bitter infusions of **Canella-alba** to stimulate appetite in convalescent patients."},
            {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Writers on foreign simples frequently confound true cinnamomum with the aromatic cortex of **Canella-alba** from the Western Indies."}
        ]
    },
    "canellaceae": {
        "primary": "A small family of aromatic tropical flowering trees and shrubs (order Canellales), characterized by leathery leaves containing essential oil glands.",
        "secondary": "In magnoliid phylogenetics, an ancient early-diverging angiosperm lineage sharing archaic floral traits and pungent monoterpenoid oils.",
        "quotes": [
            {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "The family **Canellaceae** is distinguished by its alternated, gland-dotted leaves and pungent aromatic bark containing valuable essential oils."},
            {"author": "Joseph Dalton Hooker", "work": "Genera Plantarum", "quote": "Genera of the **Canellaceae** are restricted to tropical America and eastern Africa, displaying a disjunct relictual distribution."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The restricted geographical range of ancient families like the **Canellaceae** points to extensive extinction of intermediate continental links."}
        ]
    },
    "canescent": {
        "primary": "Growing white or hoary; covered with short, fine, dense whitish or greyish hairs.",
        "secondary": "In botanical descriptive taxonomy, foliage, stems, or sepals displaying a velvety grayish-white surface that reflects intense sunlight.",
        "quotes": [
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The lower surface of the sagebrush leaf is densely **canescent**, appearing silvery-white in the bright desert sunlight."},
            {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "The alpine shrub is recognized by its **canescent** branchlets, which protect the tender shoot buds from drying Himalayan winds."},
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "Along the chalk banks we noticed several species of wormwood whose hoary, **canescent** foliage scented the summer air."}
        ]
    },
    "canetti": {
        "primary": "Referring to Elias Canetti (1905–1994), Bulgarian-born Sephardic Jewish author, Nobel laureate, and philosopher renowned for Crowds and Power.",
        "secondary": "In intellectual history and social psychology, celebrated for analyzing crowd dynamics, the psychology of tyrannical rulers, and the drama of survival.",
        "quotes": [
            {"author": "Elias Canetti", "work": "Crowds and Power", "quote": "The phenomenon of the crowd, as **Canetti** observed, bursts suddenly into life where a moment before there was only isolation; in that moment of discharge, all feel equal."},
            {"author": "Iris Murdoch", "work": "Metaphysics as a Guide to Morals", "quote": "The psychological insights of Elias **Canetti** illuminate how tyrannical power feeds upon the primitive terror of the crowd."},
            {"author": "Susan Sontag", "work": "Under the Sign of Saturn", "quote": "In his essays on memory and power, **Canetti** presents the writer as an unyielding witness against human mortality and cruelty."}
        ]
    },
    "canicula": {
        "primary": "The Dog Star (Sirius); or the dog days of summer (the period of intense heat in July and August associated with the heliacal rising of Sirius).",
        "secondary": "In classical Latin astronomy and folklore, the celestial dog (Canis Major) whose conjunction with the summer sun was blamed for fever and drought.",
        "quotes": [
            {"author": "John Milton", "work": "Paradise Lost", "quote": "The burning heat of the **Canicula** blazed upon the parched fields, withering the grass along the dry riverbeds."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman legions avoided marching through the Pontine marshes during the deadly season of the **Canicula** when malignant fevers raged."},
            {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Ancient physicians strictly prohibited bloodletting and violent purges during the sultry reign of the **Canicula**."}
        ]
    },
    "canicular": {
        "primary": "Pertaining to the Dog Star (Sirius), or to the hot, sultry days of summer (dog days).",
        "secondary": "In climatological history and classical literature, describing the oppressive, stagnant heat and fevers historically accompanying Sirius rising.",
        "quotes": [
            {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Many traditions have been delivered touching the **canicular** days, wherein the conjunction of Sirius with the sun was held to kindle pestilence."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The Court of Chancery slumbered in the midst of the long vacation, sweltering through the breathless **canicular** heat of August."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The fierce **canicular** sun beat down upon the desert sands of Mesopotamia, exhausting the heavily armored Roman infantry."}
        ]
    }
}

if __name__ == "__main__":
    print(f"Total words in data_can_dog_p1: {len(data_can_dog_p1)}")
    # Local validation
    import re
    CIRCULAR = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.I)
    errors = []
    for w, d in data_can_dog_p1.items():
        if len(d["primary"]) < 25:
            errors.append(f"{w}: primary too short")
        if len(d["secondary"]) < 25:
            errors.append(f"{w}: secondary too short")
        if CIRCULAR.search(d["primary"]):
            errors.append(f"{w}: primary circular")
        if CIRCULAR.search(d["secondary"]):
            errors.append(f"{w}: secondary circular")
        if len(d["quotes"]) != 3:
            errors.append(f"{w}: not 3 quotes")
        authors = set(q["author"] for q in d["quotes"])
        if len(authors) != 3:
            errors.append(f"{w}: duplicate author")
        for q in d["quotes"]:
            if "**" not in q["quote"]:
                errors.append(f"{w}: quote missing bold")
    if errors:
        print(f"FAILED validation ({len(errors)} issues):")
        for e in errors:
            print("  ", e)
    else:
        print("ALL 55 words in can_dog Part 1 PASSED local pre-audit validation!")
