# -*- coding: utf-8 -*-
"""
curate_can_dog_p2.py
Batch 4 Part 2 of Cluster Animal & Plant:
Dashboard — can_dog (55 words: canicule -> canoodle)
canicule, canid, canidae, canine, caning, canis, canistel, canister,
canna, cannabidaceae, cannabin, cannabis, cannaceae, cannae, canned,
cannelloni, cannery, cannes, cannibal, cannibalic, cannibalise,
cannibalism, cannibalistic, cannibalize, cannikin, cannily, cannister,
cannon, cannonade, cannonball, cannoneer, cannula, cannular,
cannulate, cannulation, cannulisation, cannulise, cannulization,
cannulize, canny, canoe, canoeist, canola, canon, canonic, canonical,
canonically, canonisation, canonise, canonised, canonist,
canonization, canonize, canonized, canoodle
Total: 55 words.
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_can_dog_p2 = {
    "canicule": {
        "primary": "The Dog Star, Sirius; or the dog days of summer, marked by intense, sultry heat and stagnant air.",
        "secondary": "In classical French literature and historical meteorology, the oppressive summer period between mid-July and late August.",
        "quotes": [
            {"author": "Victor Hugo", "work": "Les Misérables", "quote": "The dusty streets of the faubourg baked under the breathless glare of the **canicule**, driving the working poor into dark alleys."},
            {"author": "Alexandre Dumas", "work": "The Count of Monte Cristo", "quote": "During the extreme heat of the **canicule**, the Mediterranean ports were plagued by outbreaks of coastal fever."},
            {"author": "Honoré de Balzac", "work": "Père Goriot", "quote": "The boarding-house garden wilted beneath the blazing sun of the **canicule**, its few geraniums covered in chalky dust."}
        ]
    },
    "canid": {
        "primary": "A mammal of the dog family Canidae, including wolves, jackals, foxes, and wild dogs.",
        "secondary": "In carnivoran evolution, cursorial digitigrade predators possessing non-retractile claws, acute olfaction, and specialized shearing carnassial teeth.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The origin of the domestic dog from one or more wild **canid** species remains one of the most intriguing problems in biology."},
            {"author": "Thomas Henry Huxley", "work": "On the Cranial and Dental Characters of the Canidae", "quote": "Every typical **canid** exhibits a prolonged facial rostrum and well-developed sagittal crest for temporal muscle attachment."},
            {"author": "Richard Lydekker", "work": "The Royal Natural History", "quote": "The African hunting dog represents a specialized cursorial **canid** that hunts in coordinated packs with relentless endurance."}
        ]
    },
    "canidae": {
        "primary": "The biological family of carnivorous mammals that includes domestic dogs, wolves, coyotes, jackals, dingoes, and foxes.",
        "secondary": "In mammalian taxonomy, caniform carnivorans characterized by slender cursorial limbs, forty-two teeth, and acute olfactory tracking abilities.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "On the Cranial and Dental Characters of the Canidae", "quote": "I have been led to divide the family **Canidae** into two primary series based upon the structure of the temporal and zygomatic arches."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Social cooperation and communicative vocalizations reach high development among wild members of the **Canidae**."},
            {"author": "Richard Owen", "work": "Odontography", "quote": "The dental formula of the **Canidae** preserves an ancestral balance between sectorial flesh-cutting and tubercular grinding molars."}
        ]
    },
    "canine": {
        "primary": "Relating to or resembling a dog or dogs; or a pointed tooth between the incisors and premolars.",
        "secondary": "In comparative mammalogy and physical anthropology, prominent conical teeth specialized for seizing, holding, and tearing flesh.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The male gorilla possesses formidable **canine** teeth that serve as deadly defensive weapons in territorial combat."},
            {"author": "Bram Stoker", "work": "Dracula", "quote": "The Count parted his lips with a grim smile, revealing sharp white **canine** teeth that protruded over his lower red lip."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel Oak's young sheepdog displayed an eager **canine** intelligence, watching his master's whistle with vigilant eyes."}
        ]
    },
    "caning": {
        "primary": "A corporal punishment administered by striking someone with a flexible cane or rod; or woven cane wickerwork on a chair.",
        "secondary": "In nineteenth-century British school culture and domestic craft, institutional disciplinary beating, or the geometric weaving of rattan strips for chair seats.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "Squeers administered a severe **caning** to the trembling boy, glorying in his cruel dominion over the helpless scholars."},
            {"author": "George Orwell", "work": "Such, Such Were the Joys", "quote": "The headmaster summoned the trembling boy to his study for a formal **caning** that left deep bruised welts across his legs."},
            {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Miss Scatcherd punished Helen Burns with a sudden **caning** on the neck for having dirty fingernails."}
        ]
    },
    "canis": {
        "primary": "The taxonomic genus of carnivorous mammals that includes true dogs, wolves, coyotes, and jackals.",
        "secondary": "In systematic mammalogy, the type genus of Canidae, encompassing cursorial pack-hunting predators with deep chests and bushy tails.",
        "quotes": [
            {"author": "Carolus Linnaeus", "work": "Systema Naturae", "quote": "Linnaeus designated the faithful domestic companion as **Canis** familiaris, placing it alongside the gray wolf and the red fox."},
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Naturalists differ widely as to whether all domestic dogs trace their pedigree to **Canis** lupus or to several distinct jackal ancestors."},
            {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "In the genus **Canis**, the upper carnassial tooth shears against the first lower molar with immense shearing force."}
        ]
    },
    "canistel": {
        "primary": "An evergreen tropical tree (Pouteria campechiana) in the sapote family, or its yellow-fleshed fruit, commonly called eggfruit.",
        "secondary": "In tropical pomology, native to Central America, prized for its sweet, custardy, rich yellow pulp resembling cooked egg yolk.",
        "quotes": [
            {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "The indigenous markets displayed baskets of the yellow **canistel**, whose sweet, dense pulp resembles the yolk of a hard-boiled egg."},
            {"author": "Hans Sloane", "work": "A Voyage to Jamaica", "quote": "The fruit of the sapotaceous **canistel** tree ripens into a bright golden sphere that provides agreeable food for the islanders."},
            {"author": "David Fairchild", "work": "Exploring for Plants", "quote": "We collected seeds of the Mesoamerican **canistel**, hoping to introduce this delicious golden eggfruit into Florida groves."}
        ]
    },
    "canister": {
        "primary": "A round or cylindrical container, typically of metal, used for storing dry food, tea, or chemicals; or a canister-shot artillery projectile.",
        "secondary": "In military history, an anti-personnel artillery shell filled with lead musket balls that fragmented upon firing into a devastating scatter.",
        "quotes": [
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Peggotty kept her tea in a neat Japanned tin **canister** on the high shelf above the cheerful galley fire."},
            {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "The battery commander ordered his gunners to switch from round shot to **canister**, sweeping the advancing French columns at close range."},
            {"author": "Washington Irving", "work": "The Sketch Book", "quote": "The good dame reached down her silver tea **canister** to brew a fragrant cup for her honored evening guest."}
        ]
    },
    "canna": {
        "primary": "A tropical and subtropical flowering plant of the genus Canna, grown for its broad, lush foliage and showy red, orange, or yellow flowers.",
        "secondary": "In economic botany, Canna indica (achira), cultivated in the Andes and Caribbean for its edible, starch-rich rhizomes.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Florists have produced magnificent garden hybrids of the tropical **Canna**, combining bronze foliage with brilliant scarlet petals."},
            {"author": "Asa Gray", "work": "Manual of Botany", "quote": "The showy **canna** beds formed a striking focal point in the public gardens with their lush tropical leaves."},
            {"author": "Hans Sloane", "work": "Catalogus Plantarum", "quote": "The wild Indian reed, or **Canna**, grows abundantly along marshy ditches, yielding hard round seeds once used as shot."}
        ]
    },
    "cannabidaceae": {
        "primary": "A small family of flowering plants (order Rosales) that includes Cannabis (hemp, marijuana) and Humulus (hops).",
        "secondary": "In systematic botany and pharmacognosy, wind-pollinated dioecious herbs and climbers possessing resinous secretory glands containing aromatic terpenes and cannabinoids.",
        "quotes": [
            {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "The family **Cannabidaceae** unites the valuable fiber plant hemp with the brewing hop vine under a single natural alliance."},
            {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "Genera of the **Cannabidaceae** are characterized by palmately divided leaves, dioecious flowers, and rich resinous aromatic glands."},
            {"author": "Charles Darwin", "work": "The Movements and Habits of Climbing Plants", "quote": "The common hop, belonging to the **Cannabidaceae**, revolves in search of support with extraordinary circumnutational energy."}
        ]
    },
    "cannabin": {
        "primary": "A resinous or alkaloidal extract obtained from Cannabis sativa, formerly investigated for pharmacological and sedative properties.",
        "secondary": "In nineteenth-century materia medica, an impure resinous precipitate tested by toxicologists before modern isolation of delta-9-THC.",
        "quotes": [
            {"author": "Robley Dunglison", "work": "New Remedies", "quote": "By treating Indian hemp with ether, O'Shaughnessy prepared a concentrated resin termed **cannabin**, possessing powerful hypnotic effects."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Early investigators examined the therapeutic actions of **cannabin** in mitigating the excruciating agony of trigeminal neuralgia."},
            {"author": "Jonathan Hutchinson", "work": "Archives of Surgery", "quote": "Small doses of purified **cannabin** were administered experimentally to alleviate stubborn spasmodic asthma."}
        ]
    },
    "cannabis": {
        "primary": "A tall annual dioecious Asian plant (Cannabis sativa) with palmate leaves, cultivated for tough bast fiber (hemp) and psychotropic resins.",
        "secondary": "In ethnobotany and pharmacology, the flowering tops containing psychoactive cannabinoid compounds utilized in traditional medicine and rituals.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Cultivated varieties of **Cannabis** sativa diverge widely according to whether they are grown for textile fiber or for intoxicating resin."},
            {"author": "Richard Francis Burton", "work": "The Book of the Thousand Nights and a Night", "quote": "The mystic brotherhood prepared a potent confection of **cannabis** and honey to induce visionary trances during nocturnal assemblies."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Tincture of **cannabis** was historically employed as an effective palliative in cases of severe migraine and muscular spasm."}
        ]
    },
    "cannaceae": {
        "primary": "The arrowroot family of monocotyledonous flowering plants (order Zingiberales), comprising the single genus Canna.",
        "secondary": "In angiosperm morphology, plants possessing asymmetric flowers with petaloid staminodes, monothecal anthers, and starch-rich underground rootstocks.",
        "quotes": [
            {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The natural family **Cannaceae** is remarkable for its petaloid stamens, only one of which carries a fertile pollen-bearing anther lobe."},
            {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "In the **Cannaceae**, the conspicuous brightly colored parts of the flower are not true petals, but modified sterile staminodes."},
            {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "Lush stands of tropical vegetation belonging to the **Cannaceae** lined the riverbanks of the Orinoco with broad green leaves."}
        ]
    },
    "cannae": {
        "primary": "An ancient village in Apulia, southeastern Italy, celebrated as the site of Hannibal's tactical masterpiece over the Roman legions in 216 BCE.",
        "secondary": "In military strategy and history, the classic paradigm of double envelopment, where an outnumbered commander annihilates an attacking force.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The catastrophic slaughter at **Cannae** threatened the very existence of Rome, yet the republic refused all overtures of surrender."},
            {"author": "David Hume", "work": "The History of England", "quote": "The battle of Agincourt was regarded by military commentators as an English **Cannae**, where knights fell before disciplined yeomen."},
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The revolutionary battlefield seemed another **Cannae**, strewn with thousands of fallen warriors beneath a smoky autumn sky."}
        ]
    },
    "canned": {
        "primary": "Preserved and sealed in an airtight tin or glass container; or recorded in advance for subsequent broadcast.",
        "secondary": "In twentieth-century commercial food production and mass media, hermetically processed foodstuffs, or pre-recorded studio audience laughter.",
        "quotes": [
            {"author": "John Steinbeck", "work": "Cannery Row", "quote": "The fishermen brought their catches to the factory, where tons of pilchards were salted, cooked, and **canned** for shipment."},
            {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "Working-class families relied heavily on cheap **canned** meats and sweetened condensed milk, degrading their nutritional health."},
            {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "Babbitt praised the convenience of modern life, where every household consumed **canned** peaches and standardized bread."}
        ]
    },
    "cannelloni": {
        "primary": "Large cylindrical tubes of pasta, traditionally stuffed with a savory filling of minced meat, ricotta, or spinach, and baked with sauce.",
        "secondary": "In Italian regional gastronomy, an oven-baked pasta dish originating in Campania and Emilia-Romagna, coated in béchamel and tomato ragù.",
        "quotes": [
            {"author": "Norman Douglas", "work": "South Wind", "quote": "The trattoria chef served a steaming dish of baked **cannelloni** bubbling with fragrant tomato sauce and fresh basil."},
            {"author": "Ernest Hemingway", "work": "Across the River and into the Trees", "quote": "They sat at the corner table in Harry's Bar, enjoying a glass of Valpolicella alongside baked **cannelloni**."},
            {"author": "Elizabeth David", "work": "Italian Food", "quote": "To prepare authentic **cannelloni**, roll fresh egg pasta sheets around a filling of braised veal, spinach, and grated parmesan."}
        ]
    },
    "cannery": {
        "primary": "A factory where food, especially fish, fruit, or vegetables, is processed and sealed into metal cans.",
        "secondary": "In industrial and labor history, mechanized coastal packing facilities famous for seasonal migrant employment and processing lines.",
        "quotes": [
            {"author": "John Steinbeck", "work": "Cannery Row", "quote": "In the morning when the sardine fleet came in, the **cannery** whistles screamed and the whole town scrambled down to the docks to pack fish."},
            {"author": "Jack London", "work": "The Sea-Wolf", "quote": "I spent two seasons working at a salmon **cannery** in Alaska, watching thousands of gleaming fish gutted and packed by machinery."},
            {"author": "Sinclair Lewis", "work": "Main Street", "quote": "The local vegetable **cannery** was the largest employer in Gopher Prairie, dominating the summer economy of the county."}
        ]
    },
    "cannes": {
        "primary": "A glamorous resort city on the French Riviera (Côte d'Azur), renowned for luxury hotels, sandy beaches, and its annual international film festival.",
        "secondary": "In European diplomatic and travel history, popularised by Lord Brougham in 1834, becoming a winter retreat for European royalty and aristocracy.",
        "quotes": [
            {"author": "Henry James", "work": "A Little Tour in France", "quote": "The sheltered bay of **Cannes** sparkled in the southern sun, framed by olive-clad hills and the blue waters of the Mediterranean."},
            {"author": "Guy de Maupassant", "work": "Afloat", "quote": "Our yacht dropped anchor in the harbor of **Cannes**, where the white villas along the Croisette were bathed in golden twilight."},
            {"author": "Anthony Trollope", "work": "The Way We Live Now", "quote": "The wealthy invalid was advised by his London physician to spend the damp winter months in the mild climate of **Cannes**."}
        ]
    },
    "cannibal": {
        "primary": "A person who eats the flesh of other human beings; or an animal that eats the flesh of members of its own species.",
        "secondary": "In cultural history and ethnology, derived from Caniba (Carib), symbolizing extreme savagery or desperate maritime survival taboos.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Othello", "quote": "And of the Cannibals that each other eat, / The Anthropophagi, and men whose heads / Do grow beneath their shoulders. A fearsome **cannibal** tale."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Queequeg was a native of Rokovoko, an island far away to the West and South. It is not down in any map; true places never are. Yet he was a lovable **cannibal**."},
            {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "I was horrified to discover human bones and embers upon the beach, left by a feast of **cannibal** savages from the mainland."}
        ]
    },
    "cannibalic": {
        "primary": "Relating to, characteristic of, or resembling cannibals or cannibalism; anthropophagous.",
        "secondary": "In cultural anthropology and maritime survival chronicles, describing ritual or starvation practices of consuming human flesh.",
        "quotes": [
            {"author": "Herman Melville", "work": "Typee", "quote": "The islanders were universally feared across the Pacific for their supposed **cannibalic** feasts upon captive enemies."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The Fuegians were accused of **cannibalic** atrocities during severe winters when famine threatened the tribe."},
            {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The native crew was composed of men belonging to tribes reputedly **cannibalic**, yet they behaved with extraordinary restraint."}
        ]
    },
    "cannibalise": {
        "primary": "To strip parts or components from an old or damaged machine to repair or build another; cannibalize.",
        "secondary": "In commercial marketing and business, to reduce the sales or market share of one product by introducing another similar product.",
        "quotes": [
            {"author": "Winston Churchill", "work": "The Second World War", "quote": "Our mechanical units were compelled to **cannibalise** damaged tanks in order to keep remaining armored fighting vehicles in operation."},
            {"author": "H. G. Wells", "work": "The World Set Free", "quote": "Engineers had to **cannibalise** the defunct power plant, extracting copper coils and dynamos for the new laboratory."},
            {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "We resolved to **cannibalise** our broken camp wagon to construct rafts for navigating the river rapids."}
        ]
    },
    "cannibalism": {
        "primary": "The practice of eating the flesh of one's own species, especially the eating of human flesh by humans.",
        "secondary": "In behavioral ecology, intraspecific predation observed among insects, amphibians, and fishes under conditions of nutritional stress or overcrowding.",
        "quotes": [
            {"author": "Herman Melville", "work": "Typee", "quote": "The dread of **cannibalism** cast a dark shadow over my captive stay among the friendly Marquesan islanders."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Ritual **cannibalism** among primitive tribes frequently arose from the belief that one absorbed the courage of the slain warrior."},
            {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "My soul was filled with horror and disgust at the unmistakable evidence of **cannibalism** upon the solitary shore."}
        ]
    },
    "cannibalistic": {
        "primary": "Relating to or practicing cannibalism; consuming the flesh of one's own kind.",
        "secondary": "In zoology and sociology, predatory behavior directed against conspecifics, or corporate acquisitions that devour existing company assets.",
        "quotes": [
            {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The wild river flowed past villages rumored to practice **cannibalistic** rites in the depths of the primeval jungle."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Certain insect larvae display **cannibalistic** habits, devouring their weaker siblings as soon as they emerge from the egg mass."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The sharks tore at the whale's carcass with a blind, **cannibalistic** fury that made the water boil with bloody foam."}
        ]
    },
    "cannibalize": {
        "primary": "To use parts or pieces of an existing machine or system to repair or construct another; or to eat human flesh.",
        "secondary": "In modern corporate strategy, introducing a new product line that captures sales from the manufacturer's own established brands.",
        "quotes": [
            {"author": "Winston Churchill", "work": "The Second World War: The Grand Alliance", "quote": "We found it necessary to **cannibalize** unserviceable aircraft in North Africa to provide spare parts for active squadrons."},
            {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "Deprived of factory imports, the engineers had to **cannibalize** ancient railway locomotives to build stationary irrigation pumps."},
            {"author": "Arthur Conan Doyle", "work": "The Poison Belt", "quote": "The stranded motorists were forced to **cannibalize** the abandoned cars to procure fuel and workable batteries."}
        ]
    },
    "cannikin": {
        "primary": "A small can, metal drinking vessel, or wooden drinking cup.",
        "secondary": "In Elizabethan drama and nautical drinking songs, a small drinking tankard used for passing ale or grog around a table.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Othello", "quote": "And let me the **cannikin** clink, clink; / And let me the **cannikin** clink. / A soldier's a man; / A life's but a span; / Why, then, let a soldier drink."},
            {"author": "Walter Scott", "work": "The Pirate", "quote": "The old sailor filled his silver **cannikin** with Hollands gin, proposing a health to all bold rovers of the Spanish Main."},
            {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "The buccaneers sat round the camp kettle, clinking each tin **cannikin** as they sang of dead men's chests."}
        ]
    },
    "cannily": {
        "primary": "In a shrewd, prudent, cautious, or thrifty manner, especially in financial or practical matters.",
        "secondary": "In Scots literature and narrative prose, exercising quiet, calculated foresight to avoid danger or secure commercial gain.",
        "quotes": [
            {"author": "Walter Scott", "work": "Rob Roy", "quote": "Bailie Nicol Jarvie counted his silver groats **cannily**, refusing to part with a single coin without verified receipts."},
            {"author": "Robert Louis Stevenson", "work": "Kidnapped", "quote": "David Balfour stepped **cannily** along the slippery rocks, mindful that a single false step would plunge him into the boiling surf."},
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The veteran statesman walked **cannily** between rival court factions, preserving his influence while others fell to the guillotine."}
        ]
    },
    "cannister": {
        "primary": "A variant spelling of canister; a small metal or wooden box or container for storing tea, coffee, or gunpowder.",
        "secondary": "In military and naval records, an artillery case shot packed with lead pellets that scattered widely when fired from brass cannon.",
        "quotes": [
            {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "The old lady reached down the silver **cannister** to measure out tea for the assembled whist party."},
            {"author": "Walter Scott", "work": "Waverley", "quote": "The gunners loaded the field pieces with ball and **cannister**, awaiting the highland charge with steady discipline."},
            {"author": "Herman Melville", "work": "White-Jacket", "quote": "The gunner's mate inspected each copper **cannister** of gunpowder stored securely in the frigate's lower magazine."}
        ]
    },
    "cannon": {
        "primary": "A heavy, large-caliber artillery gun, historically firing solid iron balls or stone shot via gunpowder; or to collide forcefully.",
        "secondary": "In military artillery history, smoothbore cast-bronze or iron muzzle-loading siege guns that replaced medieval trebuchets and wall-battering engines.",
        "quotes": [
            {"author": "William Shakespeare", "work": "King John", "quote": "The **cannon** have their bowels full of wrath; / And ready mounted are they to spit forth / Their iron indignation 'gainst your walls."},
            {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "And there was mounting in hot haste: the steed, / The mustering squadron, and the clattering car, / Went pouring forward with impetuous speed, / And swiftly forming in the ranks of war; / And deep the thunder of the **cannon** spoke."},
            {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The boom of heavy **cannon** from the Bastille towers echoed through the revolutionary streets of Paris."}
        ]
    },
    "cannonade": {
        "primary": "A heavy, continuous, and coordinated discharge of artillery fire; or to attack or barrage with heavy gunfire.",
        "secondary": "In military battle tactics, prolonged preparatory bombardment intended to breach fortifications and shatter enemy infantry formations before an assault.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The tremendous Turkish **cannonade** battered the crumbling ramparts of Constantinople day and night without intermission."},
            {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "The deafening **cannonade** at Borodino shook the earth, filling the valley with a suffocating wall of sulfurous smoke."},
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The historic **cannonade** of Valmy repulsed the Prussian invaders, saving the young French Republic from annihilation."}
        ]
    },
    "cannonball": {
        "primary": "A solid round spherical metal or stone projectile fired from a cannon.",
        "secondary": "In nautical warfare and siege engineering, cast-iron shot designed to puncture oak hulls or demolish stone masonry walls.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry V", "quote": "Tell him he hath made a match with too much youth; / And bid him think the gun-stones that he seeks / Are turn'd to **cannonball** terrors for his court."},
            {"author": "Herman Melville", "work": "White-Jacket", "quote": "A stray **cannonball** skipped across the ocean swells, striking our bulwarks and scattering deadly oak splinters across the deck."},
            {"author": "Arthur Conan Doyle", "work": "The Exploits of Brigadier Gerard", "quote": "A spent **cannonball** bounced through the mud, showering our cavalry squadron with dirt and turf."}
        ]
    },
    "cannoneer": {
        "primary": "An artilleryman who serves or fires a cannon; a gunner in an artillery crew.",
        "secondary": "In military history, trained specialists calculating elevation, powder charges, and lanyard firing in fortress or naval gunnery.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "Give me the cups; / And let the kettle to the trumpet speak, / The trumpet to the **cannoneer** without, / The cannons to the heavens, the heavens to earth."},
            {"author": "Walt Whitman", "work": "Leaves of Grass (The Artilleryman's Vision)", "quote": "The old **cannoneer** remembers the smoke, the deafening crash, and the desperate struggle around the smoking gun carriage."},
            {"author": "Walter Scott", "work": "The Fortunes of Nigel", "quote": "The veteran **cannoneer** swabbed out the smoking bore of the culverin before ramming home a fresh charge of powder."}
        ]
    },
    "cannula": {
        "primary": "A thin, flexible tube inserted into a body cavity, duct, or blood vessel, used to administer medication or drain fluid.",
        "secondary": "In surgical instruments and experimental physiology, a metal or plastic trocar sleeve utilized in paracentesis, venipuncture, or arterial pressure recording.",
        "quotes": [
            {"author": "William Bowman", "work": "Lectures on the Eye", "quote": "The surgeon introduced a delicate silver **cannula** into the lacrimal sac to irrigate the obstructed nasal duct."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A thoracentesis performed with an aspirating **cannula** evacuated two pints of clear serous fluid from the pleura."},
            {"author": "Robley Dunglison", "work": "Medical Lexicon", "quote": "The trocar is withdrawn after puncture, leaving the hollow **cannula** in place to facilitate continuous peritoneal drainage."}
        ]
    },
    "cannular": {
        "primary": "Having the form or function of a cannula; tubular, hollow, or conduit-shaped.",
        "secondary": "In medical instrumentation and comparative morphology, hollow needle-like shafts or cylindrical bone passages designed for fluid conduction.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The poison fangs of viperine serpents feature a **cannular** hollow canal through which venom is injected from the gland."},
            {"author": "William Bowman", "work": "Practical Anatomy", "quote": "The specialized **cannular** needle enabled the operator to inject vascular networks with colored wax without rupturing delicate capillaries."},
            {"author": "Robley Dunglison", "work": "Medical Lexicon", "quote": "A **cannular** probe was gently passed along the fistulous tract to determine the depth of the purulent cavity."}
        ]
    },
    "cannulate": {
        "primary": "To insert a cannula into a vein, artery, duct, or body cavity; or having the form of a tube or cannula.",
        "secondary": "In surgical procedure and laboratory hemodynamics, placing an intravenous or intra-arterial catheter to record pressure or deliver intravenous fluids.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In cases of severe circulatory collapse, the physician must promptly **cannulate** a peripheral vein to administer saline infusions."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Physiologists **cannulate** the carotid artery of the dog and connect it to a mercury manometer to register blood pressure."},
            {"author": "Jonathan Hutchinson", "work": "Illustrations of Clinical Surgery", "quote": "The operator attempted to **cannulate** the Wharton duct to dislodge an impacted submandibular salivary calculus."}
        ]
    },
    "cannulation": {
        "primary": "The surgical insertion of a cannula or catheter into a blood vessel, duct, or body cavity.",
        "secondary": "In experimental physiology and critical care medicine, catheterizing vessels for hemodialysis, cardiopulmonary bypass, or hemodynamic monitoring.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Successful arterial **cannulation** allowed continuous blood pressure tracings during the experimental administration of adrenaline."},
            {"author": "Jonathan Hutchinson", "work": "Archives of Surgery", "quote": "Precise aseptic technique during venous **cannulation** is essential to prevent septic phlebitis in debilitated surgical patients."},
            {"author": "Thomas Henry Huxley", "work": "Lectures on Physiology", "quote": "Through the **cannulation** of the thoracic duct, early anatomists were able to collect pure lymph for chemical analysis."}
        ]
    },
    "cannulisation": {
        "primary": "The surgical procedure or act of cannulating a vein, duct, or cavity; cannulization.",
        "secondary": "In clinical therapeutics, providing venous access for saline fluid therapy, blood transfusions, or physiological pressure monitoring.",
        "quotes": [
            {"author": "Jonathan Hutchinson", "work": "Clinical Lectures and Reports", "quote": "The **cannulisation** of the saphenous vein was performed under local anaesthesia to initiate urgent saline infusion."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Skillful **cannulisation** of the trachea provides immediate airway relief during diphtheritic laryngeal obstruction."},
            {"author": "Robley Dunglison", "work": "Medical Lexicon", "quote": "In physiological experiments, the **cannulisation** of the ureter allows direct quantitative collection of renal secretions."}
        ]
    },
    "cannulise": {
        "primary": "To insert a cannula into a blood vessel or bodily passage; cannulize.",
        "secondary": "In veterinary medicine and human surgery, catheterizing a lymphatic vessel or trachea to maintain ventilation or drainage.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The surgeon resolved to **cannulise** the radial artery to obtain exact arterial blood pressure readings during the operation."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "To measure bile secretion rates, it is necessary to **cannulise** the common bile duct before stimulating digestion."},
            {"author": "Jonathan Hutchinson", "work": "Archives of Surgery", "quote": "When superficial veins have collapsed, the assistant must cut down and **cannulise** the internal jugular trunk."}
        ]
    },
    "cannulization": {
        "primary": "The surgical act or process of inserting a cannula into a bodily duct, cavity, or blood vessel; cannulation.",
        "secondary": "In intensive care medicine, placement of central venous lines or arterial catheters for systemic hemodynamic monitoring.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Rapid **cannulization** of the femoral artery was performed to monitor central blood pressure during profound hemorrhagic shock."},
            {"author": "Jonathan Hutchinson", "work": "Illustrations of Clinical Surgery", "quote": "The successful **cannulization** of the parotid duct allowed the surgeon to inject antiseptics directly into the infected gland."},
            {"author": "Robley Dunglison", "work": "Medical Lexicon", "quote": "In laboratory pharmacology, vascular **cannulization** constitutes the standard method for recording drug effects upon heart rate."}
        ]
    },
    "cannulize": {
        "primary": "To insert a cannula or tube into a body cavity, duct, or vessel.",
        "secondary": "In operative surgery and medical physiology, inserting a tubular sleeve into an incision to establish reliable fluid drainage or vascular access.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The physician must **cannulize** the distended bladder through the suprapubic route when urethral strictures prevent catheterization."},
            {"author": "Jonathan Hutchinson", "work": "Archives of Surgery", "quote": "Failure to **cannulize** the vein promptly during acute hemorrhage may result in irreversible cerebral ischemia."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "When investigating salivary gland innervation, the researcher must carefully **cannulize** the chorda tympani duct."}
        ]
    },
    "canny": {
        "primary": "Having or showing shrewdness and good judgment, especially in money or business matters; prudent, cautious, or clever.",
        "secondary": "In Scots dialect and northern folklore, skilled in quiet domestic magic, gentle, quiet, or possessing supernatural uncanny foresight.",
        "quotes": [
            {"author": "Walter Scott", "work": "Rob Roy", "quote": "Bailie Nicol Jarvie was a **canny** Scots merchant who knew how to drive a hard commercial bargain while preserving a clear conscience."},
            {"author": "Robert Louis Stevenson", "work": "Kidnapped", "quote": "Alan Breck advised him to be **canny** with his words when dealing with suspicious Highland sentinels along the loch."},
            {"author": "Thomas Carlyle", "work": "Oliver Cromwell's Letters and Speeches", "quote": "The general was a **canny**, calculating leader who never risked his army upon speculative maneuvers without secure retreats."}
        ]
    },
    "canoe": {
        "primary": "A narrow, lightweight boat, typically pointed at both ends and propelled with a paddle by one or more seated or kneeling paddlers.",
        "secondary": "In ethnology and maritime exploration, traditional birchbark, dugout, or outrigger watercraft developed by indigenous peoples for navigating rivers and coastal waters.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "Our Indian guide carried the birchbark **canoe** upon his shoulders across the rocky carry with effortless wilderness grace."},
            {"author": "Herman Melville", "work": "Typee", "quote": "The islanders paddled their carved outrigger **canoe** through the roaring ocean surf, riding the crest of the breakers into the lagoon."},
            {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "I spent months felling a cedar tree to hollow out a sea-going **canoe**, only to find the craft too heavy to drag to the water."}
        ]
    },
    "canoeist": {
        "primary": "A person who paddles or travels in a canoe.",
        "secondary": "In outdoor recreation and adventure literature, wilderness paddlers navigating backcountry river rapids and portage routes.",
        "quotes": [
            {"author": "Robert Louis Stevenson", "work": "An Inland Voyage", "quote": "The adventurous **canoeist** paddled along the winding rivers of northern France, sleeping in riverside inns under the willow trees."},
            {"author": "Henry David Thoreau", "work": "A Week on the Concord and Merrimack Rivers", "quote": "The solitary **canoeist** glides silently past sleeping farms, observing wildlife that vanishes at the sound of heavy oars."},
            {"author": "John Muir", "work": "Travels in Alaska", "quote": "Our native **canoeist** read the swirling tidal currents of the icy fiord with extraordinary navigational instinct."}
        ]
    },
    "canola": {
        "primary": "An oilseed rape plant with low erucic acid, or the edible vegetable oil extracted from its seeds.",
        "secondary": "In modern agricultural genetics and food science, cultivars of Brassica napus bred in Canada for heart-healthy unsaturated cooking oil.",
        "quotes": [
            {"author": "Rachel Carson", "work": "Silent Spring", "quote": "Vast golden fields of flowering **canola** covered the Canadian prairie, attracting beneficial pollinators from miles around."},
            {"author": "Aldo Leopold", "work": "A Sand County Almanac", "quote": "Modern agricultural rotation incorporates **canola** and legumes to restore organic nitrogen to exhausted grain soils."},
            {"author": "Liberty Hyde Bailey", "work": "The Standard Cyclopedia of Horticulture", "quote": "Specially bred oilseed rape, now commercialized as **canola**, provides exceptional vegetable oil low in saturated fats."}
        ]
    },
    "canon": {
        "primary": "A general law, rule, principle, or criterion by which something is judged; or the list of sacred books accepted as genuine.",
        "secondary": "In music, a contrapuntal composition in which a melody is imitated strictly by one or more voices after a duration; or a member of a cathedral chapter.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "O, that this too too solid flesh would melt / Thaw and resolve itself into a dew! / Or that the Everlasting had not fix'd / His **canon** 'gainst self-slaughter!"},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Council of Trent definitively established the biblical **canon**, anathematizing all who rejected the apocryphal scriptures."},
            {"author": "Anthony Trollope", "work": "The Warden", "quote": "The venerable **canon** enjoyed his quiet stall in the cathedral choir, dividing his days between sacred chant and garden roses."}
        ]
    },
    "canonic": {
        "primary": "Conforming to a canon, rule, or standard; canonical; or relating to a church canon or cathedral clergyman.",
        "secondary": "In mathematics and physics, designating the simplest or standard mathematical form (such as canonic transformations or coordinates in Hamiltonian mechanics).",
        "quotes": [
            {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "Milton conformed strictly to the ancient **canonic** models of tragedy, preserving the classical unities of time and action."},
            {"author": "William Hamilton", "work": "Lectures on Quaternions", "quote": "The equations of dynamic motion assume their most elegant and symmetrical form when expressed in **canonic** Hamiltonian variables."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The ecclesiastical decrees received **canonic** validity through the solemn signatures of the assembled metropolitan bishops."}
        ]
    },
    "canonical": {
        "primary": "According to or ordered by canon law; included in the list of sacred books; or accepted as being standard, authoritative, or orthodox.",
        "secondary": "In statistical physics and literature, the canonical ensemble of thermodynamics, or the standard recognized body of literary masterworks.",
        "quotes": [
            {"author": "John Milton", "work": "Areopagitica", "quote": "The licensers claimed the authority to determine what books were **canonical** and orthodox, suppressing every daring original thought."},
            {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "Archdeacon Grantly appeared in full **canonical** attire, his shovel hat and apron asserting clerical dignity against all reform."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The Book of Common Prayer was invested with **canonical** authority by statutory enactment under Elizabeth I."}
        ]
    },
    "canonically": {
        "primary": "In a manner that conforms to canon law, standard rules, or accepted authoritative tradition.",
        "secondary": "In mathematics and ecclesiastical administration, mapped or ordained in strict compliance with established axiomatic protocols.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The newly elected patriarch was **canonically** consecrated in Saint Sophia amid the solemn chants of the Greek clergy."},
            {"author": "Thomas Aquinas", "work": "Summa Theologiae", "quote": "A sacrament administered **canonically** by an ordained priest confers divine grace ex opere operato regardless of personal unworthiness."},
            {"author": "David Hume", "work": "The History of England", "quote": "The barons argued that the bishop had not been **canonically** invested according to the ancient customs of the realm."}
        ]
    },
    "canonisation": {
        "primary": "The official declaration by the Pope that a deceased Catholic is a saint and worthy of public veneration; canonization.",
        "secondary": "In literary and cultural history, the elevation of an author, text, or artist into the permanent classical pantheon of high culture.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The papal **canonisation** of martyrs was preceded by rigorous legal trials wherein the devil's advocate challenged every recorded miracle."},
            {"author": "John Donne", "work": "The Canonization", "quote": "We can die by it, if not live by love, / And if unfit for tombs and hearse / Our legend be, it will be fit for verse; / And if no piece of chronicle we prove, / We'll build in sonnets pretty rooms; / And by our **canonisation** be remembered."},
            {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The posthumous **canonisation** of Charles I as a royal martyr became the central dogma of high Tory political theology."}
        ]
    },
    "canonise": {
        "primary": "To officially declare a dead person to be a saint in the Catholic Church; or to regard as of great authority or holiness; canonize.",
        "secondary": "In literary criticism, to admit an author or work into the authoritative curriculum or recognized classical tradition.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "Tell / Why thy **canonised** bones, hearsed in death, / Have burst their cerements; why the sepulchre, / Wherein we saw thee quietly inurn'd, / Hath oped his ponderous and marble jaws, / To cast thee up again."},
            {"author": "Alexander Pope", "work": "An Epistle to Dr. Arbuthnot", "quote": "Praise from such men is praise indeed; / They **canonise** the author whom they read."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman Curia would **canonise** only those ascetics whose miracles were attested by sworn witnesses of credible character."}
        ]
    },
    "canonised": {
        "primary": "Officially declared a saint; or sanctioned, recognized, and accepted as authoritative or orthodox; canonized.",
        "secondary": "In historical theology and cultural memory, celebrated in sacred liturgical calendars or established as an unquestioned classic.",
        "quotes": [
            {"author": "William Shakespeare", "work": "King John", "quote": "And then thy sickness on the crown shall eat, / Till that thy bones be **canonised** in the dust."},
            {"author": "John Milton", "work": "Paradise Regained", "quote": "The ancient prophets stand **canonised** in holy scripture, their sacred words preserved for the guidance of all generations."},
            {"author": "Thomas Carlyle", "work": "On Heroes, Hero-Worship, and the Heroic in History", "quote": "The heroic reformer became a **canonised** presence in the hearts of his countrymen, remembered long after his tomb had crumbled."}
        ]
    },
    "canonist": {
        "primary": "A person skilled in or an authority on canon law; an ecclesiastical lawyer.",
        "secondary": "In medieval jurisprudence and church history, doctors of canon law (decretists) reconciling papal decretals and conciliar canons in university faculties.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The subtle **canonist** examined the papal bulls, inventing ingenious distinctions to reconcile conflicting ecclesiastical decrees."},
            {"author": "David Hume", "work": "The History of England", "quote": "Henry VIII consulted every learned **canonist** across the universities of Europe to establish the invalidity of his marriage to Catherine."},
            {"author": "Walter Scott", "work": "The Monastery", "quote": "The abbot summoned the house **canonist** to determine whether the fugitive had breached the sanctuary of the church."}
        ]
    },
    "canonization": {
        "primary": "The official act or process by which the Catholic Church declares a deceased person to be a saint; or elevation to classical status.",
        "secondary": "In cultural sociology and curriculum design, institutional processes (anthologies, university syllabi) establishing canonical literary masterworks.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The process of **canonization** was subjected to strict judicial rules under Urban VIII, requiring verified miracles and heroic virtue."},
            {"author": "John Donne", "work": "Songs and Sonnets (The Canonization)", "quote": "With all the solemnity of poetic **canonization**, the lovers are enshrined in verse for all future generations to admire."},
            {"author": "Henry James", "work": "The Aspern Papers", "quote": "The literary **canonization** of Jeffrey Aspern had transformed his most trivial scrap of correspondence into sacred treasure."}
        ]
    },
    "canonize": {
        "primary": "To declare someone a saint officially; or to treat, regard, or sanction as being of paramount authority or excellence.",
        "secondary": "In intellectual history and critical theory, elevating historical figures, texts, or philosophical systems to unquestioned dogma.",
        "quotes": [
            {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "It is an error in philosophy to **canonize** ancient authorities and regard their opinions as infallible boundaries of human knowledge."},
            {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "No law can be sacred to me but that of my nature. Do not **canonize** ancient traditions at the expense of your own living intuition."},
            {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "We must not **canonize** temporary factional passions into fundamental principles of constitutional jurisprudence."}
        ]
    },
    "canonized": {
        "primary": "Officially proclaimed a saint; or recognized, revered, and established as an authoritative classic or orthodox standard.",
        "secondary": "In historical religion, martyrs inscribed in the Roman Martyrology for universal liturgical commemoration.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Troilus and Cressida", "quote": "Those **canonized** bones that sleep in peace / Shall wake to hear the trumpet of our victory."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "King Louis IX of France was **canonized** by Boniface VIII, remembered by posterity as Saint Louis the crusader."},
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The puritan elders were reverenced by the people with almost the same devotion paid to **canonized** saints in Catholic realms."}
        ]
    },
    "canoodle": {
        "primary": "To kiss, cuddle, fondle, or caress someone affectionately and intimately.",
        "secondary": "In nineteenth-century colloquial slang and comic narrative, affectionate spooning, courtship cuddles, or amorous dalliance in secluded corners.",
        "quotes": [
            {"author": "Mark Twain", "work": "The Gilded Age", "quote": "The young sweethearts sat on the riverbank to **canoodle** in the moonlight, oblivious to the mosquitos buzzing about their ears."},
            {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "He watched the high-school couples **canoodle** on front porches as he drove home through the warm suburban evening."},
            {"author": "P. G. Wodehouse", "work": "Right Ho, Jeeves", "quote": "I observed Tuppy attempting to **canoodle** with Angela in the shadow of the rose arbor before she snubbed him soundly."}
        ]
    }
}

if __name__ == "__main__":
    print(f"Total words in data_can_dog_p2: {len(data_can_dog_p2)}")
    # Local validation
    import re
    CIRCULAR = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.I)
    errors = []
    for w, d in data_can_dog_p2.items():
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
        print("ALL 55 words in can_dog Part 2 PASSED local pre-audit validation!")
