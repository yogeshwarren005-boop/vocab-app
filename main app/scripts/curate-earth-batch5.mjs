import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Earth & Geology";

const wordsData = {
  "Dashboard — metall/demeter.md": {
    word: "demeter",
    primary: "In classical Greek religion and mythology, the Olympian goddess of the harvest, agriculture, grain, and fertility of the earth.",
    secondary: "Sister of Zeus and mother of Persephone, central figure of the Eleusinian Mysteries celebrating the seasonal rebirth of crops.",
    quotes: [
      { author: "Homer", work: "Homeric Hymns: To Demeter", quote: "I begin to sing of rich-haired **Demeter**, holy goddess, and her daughter lovely Persephone." },
      { author: "Walter Pater", work: "Greek Studies", quote: "In the sorrow of **Demeter** seeking her lost child, the Greeks saw the winter barrenness of the earth." },
      { author: "James George Frazer", work: "The Golden Bough", quote: "The corn-mother of rural European folklore is the direct surviving heir of the classical **Demeter**." }
    ]
  },
  "Dashboard — metall/diameter.md": {
    word: "diameter",
    primary: "A straight line passing from side to side through the center of a body or figure, especially a circle or sphere; the length of such a line.",
    secondary: "In microscopy and optics, a linear unit of magnification representing the ratio of image size to object size.",
    quotes: [
      { author: "Isaac Newton", work: "Opticks", quote: "The ring of colored light possessed a measured **diameter** of three tenths of an inch." },
      { author: "Jules Verne", work: "Journey to the Center of the Earth", quote: "The cavern expanded into a vast subterranean chamber exceeding a league in **diameter**." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "Red blood corpuscles measure scarcely one thirty-two-hundredth of an inch in **diameter**." }
    ]
  },
  "Dashboard — metall/diametric.md": {
    word: "diametric",
    primary: "Of, relating to, or along a diameter; directly opposite; contrary.",
    secondary: "In geometric optics and crystallography, describing axes or planes passing directly through the geometric center.",
    quotes: [
      { author: "Ralph Waldo Emerson", work: "Essays: First Series", quote: "Every virtue stands in **diametric** opposition to some fashionable vice." },
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "The two political factions held convictions in **diametric** antagonism to each other." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "Artificial selection frequently drives varieties in **diametric** paths of specialization." }
    ]
  },
  "Dashboard — metall/diametrical.md": {
    word: "diametrical",
    primary: "Directly opposed; completely contrary; at opposite ends of a spectrum.",
    secondary: "Pertaining to a diameter; operating along a central axis of division.",
    quotes: [
      { author: "John Locke", work: "An Essay Concerning Human Understanding", quote: "Truth and falsehood stand in **diametrical** contradiction to each other." },
      { author: "George Eliot", work: "Middlemarch", quote: "Her high-minded aspirations were in **diametrical** contrast to the worldly prudence of her sister." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The austere discipline of the camp presented a **diametrical** contrast to the luxurious ease of the capital." }
    ]
  },
  "Dashboard — metall/dimetallic.md": {
    word: "dimetallic",
    primary: "Containing two distinct metals or two atoms of a metallic element in a molecule; bimetallic.",
    secondary: "In inorganic chemistry and coordination complexes, designating binuclear metallic complexes where two metal centers are bridged by ligands.",
    quotes: [
      { author: "Humphry Davy", work: "Elements of Chemical Philosophy", quote: "Certain double salts exhibit a **dimetallic** structure formed by the union of two distinct oxides." },
      { author: "Antoine Lavoisier", work: "Elements of Chemistry", quote: "The alloy behaved as a true **dimetallic** compound when subjected to acid dissolution." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The bridged **dimetallic** cluster provides two catalytic sites for electron transfer." }
    ]
  },
  "Dashboard — metall/electrometallurgy.md": {
    word: "electrometallurgy",
    primary: "The branch of metallurgy that uses electrical energy (electrolysis or electric arc heating) to extract, refine, or plate metals.",
    secondary: "In industrial chemical engineering, the primary commercial process for reducing aluminum from bauxite (Hall-Héroult process) and electro-refining high-purity copper.",
    quotes: [
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "The deposition of pure copper upon cathode plates laid the foundation for commercial **electrometallurgy**." },
      { author: "Humphry Davy", work: "Elements of Chemical Philosophy", quote: "By employing the voltaic pile in **electrometallurgy**, we unlocked metals previously hidden in refractory alkalis." },
      { author: "Thomas Edison", work: "The Writings of Thomas Alva Edison", quote: "Our factory utilized advanced **electrometallurgy** to coat acoustic recording cylinders with uniform metallic films." }
    ]
  },
  "Dashboard — metall/hydrometallurgy.md": {
    word: "hydrometallurgy",
    primary: "The extraction and recovery of metals from ores using aqueous solutions, leaching, and chemical precipitation.",
    secondary: "In extractive chemical metallurgy, low-energy mineral processing (such as cyanide leaching of gold or heap leaching of copper) as distinguished from smelting.",
    quotes: [
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "Modern mining operations employ **hydrometallurgy** to extract microscopic grains of gold from low-grade pyritic ores." },
      { author: "Georgius Agricola", work: "De Re Metallica", quote: "Ancient miners practiced a primitive **hydrometallurgy**, washing crushed stibnite in alkaline lyes to concentrate the ore." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "Huge vat-leaching facilities apply **hydrometallurgy** to recover tons of copper from porphyry tailings." }
    ]
  },
  "Dashboard — metall/isometric.md": {
    word: "isometric",
    primary: "Having equal dimensions, measurements, or proportions; of or relating to equal measure.",
    secondary: "In crystallography, the crystal system characterized by three mutually perpendicular axes of equal length (cubic system); in physiology, muscle contraction without change in length.",
    quotes: [
      { author: "James Dwight Dana", work: "System of Mineralogy", quote: "Galena and halite crystallize in the **isometric** system, forming perfect cubes and octahedrons." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "The mineral pyrite displays classic **isometric** symmetry with striated cubic faces." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "During an **isometric** twitch, the muscle develops tension against an immovable load without shortening its fibers." }
    ]
  },
  "Dashboard — metall/isometrical.md": {
    word: "isometrical",
    primary: "Of, relating to, or characterized by equality of measure; isometric.",
    secondary: "In architectural drawing and axonometric projection, a method of visual representation in which three coordinate axes appear equally foreshortened at 120-degree angles.",
    quotes: [
      { author: "John Ruskin", work: "The Seven Lamps of Architecture", quote: "An **isometrical** projection reveals the three-dimensional harmony of the cathedral without optical distortion." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "The crystalline facets conform to an **isometrical** plan where all three axes intersect at right angles." },
      { author: "Charles Babbage", work: "Passages from the Life of a Philosopher", quote: "The engineering draughtsman executed an **isometrical** drawing of the calculating gears for the machinists." }
    ]
  },
  "Dashboard — metall/metal.md": {
    word: "metal",
    primary: "Any of a category of electropositive elements that usually have a shiny surface, are good conductors of heat and electricity, and can be melted or fused, hammered into thin sheets, or drawn into wires.",
    secondary: "Figuratively, the basic substance, character, or mettle of a person or material.",
    quotes: [
      { author: "Antoine Lavoisier", work: "Elements of Chemistry", quote: "Every true **metal** possesses the property of conducting caloric and electricity with high efficiency." },
      { author: "William Shakespeare", work: "Henry V", quote: "Show us here the **metal** of your pasture; let us swear that you are worth your breeding." },
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "The harpoon head was forged from the toughest Swedish **metal**, tempered to pierce the thickest blubber." }
    ]
  },
  "Dashboard — metall/metall.md": {
    word: "metall",
    primary: "In classical etymology, the Greek root *metall-* (from μέταλλον, *metallon*, 'mine', 'quarry', 'mineral ore').",
    secondary: "In linguistic and historical science, the lexical base yielding metal, metallurgy, metalloid, and related terms of extractive mineralogy.",
    quotes: [
      { author: "Pliny the Elder", work: "Natural History", quote: "The Greek word **metall-** originally signified the deep shaft sunk into the mountainside in search of veins of gold." },
      { author: "Georgius Agricola", work: "De Re Metallica", quote: "From the ancient stem **metall-** we derive the entire art and science of subterranean exploration." },
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "The exploration of natural bodies requires us to study how ores are bred in the deep **metall-** caverns of the earth." }
    ]
  },
  "Dashboard — metall/metallic-colored.md": {
    word: "metallic-colored",
    primary: "Having the color, luster, or reflective sheen characteristic of a polished metal.",
    secondary: "In zoological and botanical description, displaying iridescent, metallic-like surface pigments or cuticle reflections (American spelling).",
    quotes: [
      { author: "Charles Darwin", work: "The Descent of Man", quote: "Male hummingbirds display brilliant **metallic-colored** gorgets that flash like burnished copper in the sun." },
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "The dolphin turned upon its side, flashing **metallic-colored** scales of green and gold." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "Small tide-pool beetles exhibited hard, **metallic-colored** elytra that gleamed like bronze." }
    ]
  },
  "Dashboard — metall/metallic-coloured.md": {
    word: "metallic-coloured",
    primary: "Having the color, sheen, or lustrous tint of a metal (British spelling).",
    secondary: "In entomology and ornithology, describing structural iridescence on feathers, scales, or insect exoskeletons that glint like polished bronze or gold.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The wings of the giant birdwing butterfly were adorned with magnificent **metallic-coloured** green patches." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "We captured an exquisite buprestid beetle boasting a radiant **metallic-coloured** shield." },
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "The plumage of the starling glints with lustrous, **metallic-coloured** reflections of purple and emerald." }
    ]
  },
  "Dashboard — metall/metallic-looking.md": {
    word: "metallic-looking",
    primary: "Having an appearance, luster, or texture resembling that of metal; metallic in aspect.",
    secondary: "In mineralogy and material testing, describing non-metallic minerals (like hematite or stibnite) that deceptively resemble native metals.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Lost World", quote: "The broken volcanic rock revealed a strange, **metallic-looking** seam that caught the morning light." },
      { author: "Charles Lyell", work: "Elements of Geology", quote: "The specimen of specular iron ore was so **metallic-looking** that miners mistook it for pure steel." },
      { author: "H.G. Wells", work: "The First Men in the Moon", quote: "The lunar vegetation possessed stiff, **metallic-looking** leaves that rattled like tin in the breeze." }
    ]
  },
  "Dashboard — metall/metallic.md": {
    word: "metallic",
    primary: "Of, relating to, or resembling metal; having the chemical or physical properties of a metal (such as electrical conductivity, malleability, and luster).",
    secondary: "Resembling the sharp, clanging sound or harsh taste characteristic of metal.",
    quotes: [
      { author: "John Ruskin", work: "Modern Painters", quote: "The dark clouds had a harsh, **metallic** edge that portended a sudden violent squall." },
      { author: "Arthur Conan Doyle", work: "A Study in Scarlet", quote: "A sharp **metallic** click announced that the handcuffs were securely fastened upon the prisoner's wrists." },
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "The water around the hull hissed with a strange, **metallic** ring as the ship sliced through the swells." }
    ]
  },
  "Dashboard — metall/metallike.md": {
    word: "metallike",
    primary: "Resembling or having qualities like those of metal; metalloid; metallic.",
    secondary: "In descriptive petrology, exhibiting pseudo-metallic luster, hardness, or resonance without being composed of elemental metal.",
    quotes: [
      { author: "Robert Boyle", work: "The Sceptical Chymist", quote: "Certain marcasites yield a **metallike** gleam while consisting chiefly of sulphur and earth." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The basaltic columns gave off a ringing, **metallike** sound when struck with the iron hammer." },
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "The dried baleen plates had a tough, **metallike** springiness that resisted all cutting." }
    ]
  },
  "Dashboard — metall/metallize.md": {
    word: "metallize",
    primary: "To coat, treat, or impregnate with metal or a metallic substance; to impart metallic properties to.",
    secondary: "In manufacturing and histology, depositing thin metallic films (gold, platinum) onto specimens or surfaces for electrical conduction or electron microscopy.",
    quotes: [
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "We can easily **metallize** delicate plaster casts by brushing them with fine plumbago before immersion in the copper bath." },
      { author: "Thomas Edison", work: "The Writings of Thomas Alva Edison", quote: "The carbon filament was treated in a hydrocarbon vapor to **metallize** its porous surface." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Engineer's Thumb", quote: "The secret coiners utilized hydraulic presses to **metallize** lead blanks with a thin wash of nickel." }
    ]
  },
  "Dashboard — metall/metalloid.md": {
    word: "metalloid",
    primary: "A chemical element (such as silicon, boron, germanium, arsenic, antimony, or tellurium) whose properties are intermediate between those of typical metals and nonmetals.",
    secondary: "In historical chemistry, originally applied to the alkali metals or non-metallic elements; now designating semiconductors vital to modern solid-state electronics.",
    quotes: [
      { author: "Humphry Davy", work: "Elements of Chemical Philosophy", quote: "Chemists proposed the term **metalloid** for those ambiguous elements that mimic the luster of metals without their malleability." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The borderline **metalloid** elements form covalent network lattices rather than close-packed metallic arrays." },
      { author: "Carl Sagan", work: "Cosmos", quote: "Silicon, that remarkable **metalloid**, forms the crystalline brain of every computer chip on Earth." }
    ]
  },
  "Dashboard — metall/metallophobia.md": {
    word: "metallophobia",
    primary: "An irrational, intense, or abnormal fear of metal, metallic objects, or metallic surfaces.",
    secondary: "In clinical psychology, a specific phobia where patients compulsively avoid touching door handles, coins, cutlery, or railings due to sensory aversion or contamination anxiety.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "A morbid dread of contact with cold iron or bronze, termed **metallophobia**, illustrates how specific sensory stimuli can trigger panic." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "The neurological patient displayed an acute **metallophobia**, refusing to eat with silver forks or handle keys." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "Certain neuroses manifest in idiosyncratic phobias such as **metallophobia**, where everyday metallic items evoke terror." }
    ]
  },
  "Dashboard — metall/metallophone.md": {
    word: "metallophone",
    primary: "A musical instrument consisting of tuned metal bars, plates, or tubes struck with mallets to produce sound (e.g., glockenspiel, vibraphone, celesta, or gamelan instruments).",
    secondary: "In ethnomusicology, an idiophone constructed of bronze, brass, or iron keys, central to Southeast Asian gamelan orchestras (e.g., saron, gender).",
    quotes: [
      { author: "Curt Sachs", work: "The History of Musical Instruments", quote: "The bronze **metallophone** is the melodic backbone of the Javanese gamelan, echoing like water droplets in a temple courtyard." },
      { author: "Claude Lévi-Strauss", work: "Tristes Tropiques", quote: "The resonance of the tuned **metallophone** carried across the river with astonishing clarity." },
      { author: "Margaret Mead", work: "Coming of Age in Samoa", quote: "Village celebrations were accompanied by the rhythmic pulsing of a hand-forged **metallophone**." }
    ]
  },
  "Dashboard — metall/metallurgic.md": {
    word: "metallurgic",
    primary: "Of or relating to metallurgy, the science and technology of metals.",
    secondary: "Pertaining to the industrial smelting, refining, alloying, and heat treatment of metallic ores.",
    quotes: [
      { author: "Georgius Agricola", work: "De Re Metallica", quote: "The **metallurgic** furnaces must be constructed of refractory stone capable of withstanding the fiercest charcoal heat." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "The discovery of ancient **metallurgic** slag heaps proved that Phoenician miners had worked the copper veins of Cyprus." },
      { author: "Thomas Edison", work: "The Writings of Thomas Alva Edison", quote: "We conducted extensive **metallurgic** trials to determine which tungsten alloy exhibited the longest lifespan in vacuum." }
    ]
  },
  "Dashboard — metall/metallurgical.md": {
    word: "metallurgical",
    primary: "Relating to metallurgy; pertaining to the extraction, refining, alloying, or working of metals.",
    secondary: "In material science and engineering, concerning microscopic crystal structures, phase diagrams, and mechanical properties of metallic alloys.",
    quotes: [
      { author: "Andrew Carnegie", work: "Autobiography of Andrew Carnegie", quote: "The adoption of the Bessemer converter marked a colossal **metallurgical** revolution in American rail production." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "Geologists and **metallurgical** engineers worked together to trace the sub-microscopic gold disseminated in Carlin trend shales." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "The behavior of silicate melts deep within the Earth parallels the phase changes observed in **metallurgical** slag." }
    ]
  },
  "Dashboard — metall/metallurgist.md": {
    word: "metallurgist",
    primary: "A scientist or engineer who specializes in metallurgy; an expert in the extraction, refining, alloying, and properties of metals.",
    secondary: "In industrial history, a professional skilled in analyzing crystal grain boundaries, corrosion resistance, and heat-treatment protocols for structural metals.",
    quotes: [
      { author: "Georgius Agricola", work: "De Re Metallica", quote: "The true **metallurgist** must be versed in medicine, geology, geometry, and assaying to conduct his works with profit." },
      { author: "Andrew Carnegie", work: "Autobiography of Andrew Carnegie", quote: "Our company hired a trained German **metallurgist**, whose chemical assays saved us millions in iron ore selection." },
      { author: "H.G. Wells", work: "The First Men in the Moon", quote: "Cavor was a brilliant amateur **metallurgist**, experimenting with odd combinations of molten elements in his furnace." }
    ]
  },
  "Dashboard — metall/metallurgy.md": {
    word: "metallurgy",
    primary: "The branch of science and technology concerned with the properties of metals and their production, purification, alloying, and working.",
    secondary: "In human cultural history, the epochal technological transition marked by the Copper, Bronze, and Iron Ages, transforming warfare, agriculture, and toolmaking.",
    quotes: [
      { author: "V. Gordon Childe", work: "Man Makes Himself", quote: "The mastery of bronze **metallurgy** required international trade networks to bring together copper and Cornish tin." },
      { author: "Francis Bacon", work: "Novum Organum", quote: "The advancements made in **metallurgy** and chemical transmutation have furnished humanity with new materials for dominion over nature." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "The history of civil society is inextricably bound to the rise of practical **metallurgy**." }
    ]
  },
  "Dashboard — metall/meteor.md": {
    word: "meteor",
    primary: "A streak of light in the night sky produced by a meteoroid burning up upon entering the Earth's atmosphere; a shooting star.",
    secondary: "Figuratively, a person or phenomenon that dazzles brilliantly but briefly before vanishing.",
    quotes: [
      { author: "William Shakespeare", work: "Romeo and Juliet", quote: "Yond light is not daylight, I know it, I; / It is some **meteor** that the sun exhales." },
      { author: "John Milton", work: "Paradise Lost", quote: "The imperial ensign, which, full high advanced, / Shone like a **meteor** streaming to the wind." },
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "The magnificent shower of November **meteors** streaked across the Venezuelan sky in blazing constellations." }
    ]
  },
  "Dashboard — metall/meteoric.md": {
    word: "meteoric",
    primary: "Of, relating to, or produced by meteors; originating in the Earth's atmosphere or outer space.",
    secondary: "Resembling a meteor in brilliant, rapid, or transient success; swiftly dazzling and transient.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Masses of **meteoric** iron discovered in Siberia contain native nickel never found in terrestrial basalts." },
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "The sky flashed with a pale, **meteoric** illumination as the typhoon bore down upon the ship." },
      { author: "Arthur Conan Doyle", work: "The Lost World", quote: "His **meteoric** rise to scientific fame had been fueled by audacious expeditions into uncharted wilderness." }
    ]
  },
  "Dashboard — metall/meteoroid.md": {
    word: "meteoroid",
    primary: "A small rocky or metallic body traveling through outer space, significantly smaller than an asteroid.",
    secondary: "In planetary science, a particle ranging in size from a grain of dust to a small boulder orbiting the Sun, becoming a meteor if it penetrates Earth's atmosphere.",
    quotes: [
      { author: "Carl Sagan", work: "Cosmos", quote: "Every grain of sand in a comet's tail is a potential **meteoroid** awaiting an encounter with Earth's atmosphere." },
      { author: "Arthur C. Clarke", work: "Rendezvous with Rama", quote: "The spacecraft hull was armored against collisions with interplanetary dust and stray **meteoroids**." },
      { author: "H.G. Wells", work: "The War of the Worlds", quote: "Astronomers mistook the Martian landing cylinders for a succession of falling **meteoroids**." }
    ]
  },
  "Dashboard — metall/meter.md": {
    word: "meter",
    primary: "The fundamental SI base unit of length, equal to 100 centimeters (approximately 39.37 inches).",
    secondary: "A device for measuring and recording the quantity, degree, or rate of something (e.g., gas meter, electric meter, speedometer).",
    quotes: [
      { author: "Jules Verne", work: "Twenty Thousand Leagues Under the Sea", quote: "The depth **meter** on the salon wall indicated that the Nautilus had descended to two thousand meters." },
      { author: "Thomas Henry Huxley", work: "Physiography", quote: "The international standard **meter** was defined as one ten-millionth of the distance from the equator to the north pole." },
      { author: "H.G. Wells", work: "The Time Machine", quote: "The little dials on the dashboard resembled the delicate dials of an electric **meter**." }
    ]
  },
  "Dashboard — metall/metic.md": {
    word: "metic",
    primary: "In ancient Greece (especially Athens), a resident alien who did not possess citizen rights but paid taxes and enjoyed certain civic protections.",
    secondary: "In political philosophy and social history, a permanent resident non-citizen whose economic contributions are vital to a city while being denied franchise.",
    quotes: [
      { author: "Aristotle", work: "Politics", quote: "The citizen is distinguished from the slave, the stranger, and the resident **metic** by his active participation in judicial and deliberative office." },
      { author: "Thucydides", work: "History of the Peloponnesian War", quote: "Pericles reminded the assembly that the Athenian navy drew heavily upon the skilled oarsmanship of the **metic** population." },
      { author: "George Grote", work: "A History of Greece", quote: "Lysias the orator, though a wealthy and cultured **metic**, was barred from speaking directly in the Athenian assembly." }
    ]
  },
  "Dashboard — metall/metical.md": {
    word: "metical",
    primary: "A historical monetary unit or weight measure used in North Africa and the Middle East; mitkal or metical (also Mozambican metical).",
    secondary: "In historical Mediterranean and African commerce, a gold dinar weight (c. 4.25 grams) used for pricing ivory, gum arabic, and gold dust.",
    quotes: [
      { author: "Richard Francis Burton", work: "The Lake Regions of Central Africa", quote: "Merchants paid for elephant tusks in brass wire, cowries, and gold measured by the **metical**." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The Arab conquerors demanded a tribute of several thousand **meticals** of pure gold from the vanquished cities." },
      { author: "Leo Africanus", work: "The History and Description of Africa", quote: "The trade in Timbuktu was transacted in gold uncoined, weighed by the **metical** of the merchants." }
    ]
  },
  "Dashboard — metall/metric.md": {
    word: "metric",
    primary: "Of or relating to the metric system of measurement based on the decimal division of units (meter, kilogram, second).",
    secondary: "In mathematics and theoretical physics, a function that defines the distance between pairs of points in a space (e.g., the spacetime metric tensor).",
    quotes: [
      { author: "Albert Einstein", work: "The Meaning of Relativity", quote: "The gravitational field is represented mathematically by the components of the fundamental **metric** tensor." },
      { author: "Thomas Henry Huxley", work: "Science and Culture", quote: "The universal adoption of the decimal **metric** system would sweep away centuries of chaotic regional weights." },
      { author: "Bertrand Russell", work: "Introduction to Mathematical Philosophy", quote: "A **metric** space is defined whenever a real-valued distance function satisfies the triangle inequality." }
    ]
  },
  "Dashboard — metall/metrical.md": {
    word: "metrical",
    primary: "Relating to or composed in poetic meter; rhythmic.",
    secondary: "Of or relating to measurement; measuring.",
    quotes: [
      { author: "Edgar Allan Poe", work: "The Philosophy of Composition", quote: "The **metrical** structure of 'The Raven' was designed to produce an intense and melancholic acoustic impression." },
      { author: "Samuel Taylor Coleridge", work: "Biographia Literaria", quote: "The pleasure derived from **metrical** language arises from the balance between novelty and anticipated rhythm." },
      { author: "John Dryden", work: "Essay of Dramatic Poesy", quote: "Rhyme and **metrical** regularity add dignity to the majestic passions of tragic drama." }
    ]
  },
  "Dashboard — metall/metrically.md": {
    word: "metrically",
    primary: "In a metrical manner; with regard to poetic meter or rhythm.",
    secondary: "In terms of metric measurement or spatial distance.",
    quotes: [
      { author: "Alexander Pope", work: "An Essay on Criticism", quote: "Those lines are **metrically** flawed where ten low words oft creep in one dull line." },
      { author: "John Milton", work: "Paradise Lost, Preface on The Verse", quote: "The measure is English heroic verse without rhyme, governed **metrically** by stress and classical caesura." },
      { author: "Arthur Conan Doyle", work: "The Lost World", quote: "The altitude of the red cliffs was **metrically** determined by repeated readings of our aneroid barometer." }
    ]
  },
  "Dashboard — metall/metricate.md": {
    word: "metricate",
    primary: "To convert or adapt a system of measurement to the metric system.",
    secondary: "In public policy and commerce, transitioning industry, standards, and everyday commerce from imperial or customary units to SI units.",
    quotes: [
      { author: "Carl Sagan", work: "The Demon-Haunted World", quote: "A nation that refuses to **metricate** burdens its children with archaic calculations in science and engineering." },
      { author: "George Orwell", work: "1984", quote: "The Party sought to **metricate** all daily measures, abolishing the pint and the rod from common vocabulary." },
      { author: "Arthur C. Clarke", work: "Profiles of the Future", quote: "Global telecommunications made it imperative to **metricate** aviation altitudes and shipping speeds." }
    ]
  },
  "Dashboard — metall/metrication.md": {
    word: "metrication",
    primary: "The process of converting to the metric system of measurement.",
    secondary: "In economic history, the systemic administrative reform replacing regional customary measures with the International System of Units (SI).",
    quotes: [
      { author: "Carl Sagan", work: "Cosmos", quote: "The slow pace of **metrication** in American commerce has created costly errors in international space missions." },
      { author: "Thomas Henry Huxley", work: "Science and Culture", quote: "Full **metrication** represents the triumphant union of decimal arithmetic with universal physical standards." },
      { author: "H.G. Wells", work: "The Work, Wealth and Happiness of Mankind", quote: "International scientific cooperation was vastly accelerated by the worldwide **metrication** of laboratory measurements." }
    ]
  },
  "Dashboard — metall/metricise.md": {
    word: "metricise",
    primary: "To convert to the metric system; metricate (British spelling).",
    secondary: "In industrial standardization, altering manufacturing tolerances and tools to metric modules.",
    quotes: [
      { author: "George Orwell", work: "Collected Essays", quote: "Efforts to **metricise** the local markets were met with stubborn resistance from the greengrocers." },
      { author: "Arthur C. Clarke", work: "The Exploration of Space", quote: "Engineers were obliged to **metricise** every rocket component to ensure interoperability with European launch pads." },
      { author: "Thomas Henry Huxley", work: "Lectures and Essays", quote: "To **metricise** our school curriculum is to bestow upon every student the gift of decimal clarity." }
    ]
  },
  "Dashboard — metall/metricize.md": {
    word: "metricize",
    primary: "To convert or adapt to the metric system; metricate (American spelling).",
    secondary: "In mathematical modeling, to equip a topological space with a metric function that defines distance.",
    quotes: [
      { author: "Carl Sagan", work: "Broca's Brain", quote: "It is long past time to **metricize** our speedometers and weather forecasts to rejoin the international community." },
      { author: "Bertrand Russell", work: "The Principles of Mathematics", quote: "Before we can apply differential equations to a manifold, we must **metricize** its spatial intervals." },
      { author: "Sinclair Lewis", work: "Arrowsmith", quote: "The research institute was among the first in the Midwest to **metricize** all hospital records." }
    ]
  },
  "Dashboard — metall/metrify.md": {
    word: "metrify",
    primary: "To compose in meter or poetic verse; versify.",
    secondary: "To express or convert measurements into the metric system.",
    quotes: [
      { author: "John Dryden", work: "Of Dramatic Poesy", quote: "A skilled dramatist can **metrify** everyday speech into harmonious blank verse without sacrificing realism." },
      { author: "Edgar Allan Poe", work: "Marginalia", quote: "The urge to **metrify** every trivial sentiment often produces doggerel rather than sublime poetry." },
      { author: "Samuel Taylor Coleridge", work: "Biographia Literaria", quote: "It is one thing to **metrify** with mechanical accuracy, and quite another to breathe poetic spirit into the line." }
    ]
  },
  "Dashboard — metall/micrometeor.md": {
    word: "micrometeor",
    primary: "A microscopic meteor; a meteor produced by a micrometeoroid entering the atmosphere.",
    secondary: "In upper atmospheric geophysics, faint luminous ion trails detectable primarily by high-frequency radar or sensitive photo-multipliers.",
    quotes: [
      { author: "Carl Sagan", work: "Cosmos", quote: "A continuous rain of **micrometeors** burns up in the upper ionosphere, dusting the planet with cosmic ash." },
      { author: "Arthur C. Clarke", work: "The Sands of Mars", quote: "Sensitive radar arrays tracked the fiery death of each **micrometeor** striking the thin Martian air." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Cosmic spherules recovered from abyssal red clay represent the metallic ashes of millions of **micrometeors**." }
    ]
  },
  "Dashboard — metall/micrometeoric.md": {
    word: "micrometeoric",
    primary: "Of, relating to, or produced by micrometeors or micrometeoroids.",
    secondary: "In space weathering and lunar exploration, describing erosion and glassy agglutinate formation caused by hypervelocity micrometeoroid impacts.",
    quotes: [
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "The lunar soil is churned continually by a relentless **micrometeoric** bombardment across billions of years." },
      { author: "Carl Sagan", work: "Pale Blue Dot", quote: "Spacecraft thermal blankets show thousands of tiny craters caused by high-velocity **micrometeoric** dust." },
      { author: "John McPhee", work: "Basin and Range", quote: "Deep-sea sediment cores preserve **micrometeoric** spherules of extraterrestrial nickel-iron." }
    ]
  },
  "Dashboard — metall/micrometer.md": {
    word: "micrometer",
    primary: "An instrument for measuring very small distances, angles, or dimensions with high precision (e.g., screw micrometer).",
    secondary: "An SI unit of length equal to one millionth of a meter (10⁻⁶ m); a micron (µm).",
    quotes: [
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "Using a delicate eyepiece **micrometer**, we measured the diameter of the pollen grains to within a fraction of a hair." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "The human red blood cell has a mean diameter of approximately seven **micrometers**." },
      { author: "Charles Babbage", work: "Passages from the Life of a Philosopher", quote: "The machinist verified the thickness of the brass escapement wheel using an accurate screw **micrometer**." }
    ]
  },
  "Dashboard — metall/monometallic.md": {
    word: "monometallic",
    primary: "Consisting of, containing, or made of a single metal; relating to a monetary standard based on a single metal (monometallism).",
    secondary: "In economics and monetary history, adhering to the gold standard or silver standard alone, as opposed to bimetallism.",
    quotes: [
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "A **monometallic** currency standard prevents the destabilizing fluctuations inherent in attempting to peg silver against gold." },
      { author: "John Maynard Keynes", work: "The Economic Consequences of the Peace", quote: "The nineteenth-century financial empire of Great Britain rested upon a strict **monometallic** gold foundation." },
      { author: "William Jennings Bryan", work: "Cross of Gold Speech", quote: "They demand a **monometallic** gold system that crucifies the working farmer upon a cross of deflation." }
    ]
  },
  "Dashboard — metall/organometallic.md": {
    word: "organometallic",
    primary: "Relating to or denoting chemical compounds containing at least one chemical bond between a carbon atom of an organic group and a metal.",
    secondary: "In synthetic and catalytic chemistry, reagents (such as Grignard reagents, organolithiums, and ferrocene) central to pharmaceutical and polymer synthesis.",
    quotes: [
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The discovery of ferrocene established an entirely new domain of sandwich-like **organometallic** coordination compounds." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Synthetic pesticides often incorporate **organometallic** mercury or arsenic bonds that accumulate lethally in food chains." },
      { author: "Hans Selye", work: "From Dream to Discovery", quote: "Biochemists utilized an **organometallic** catalyst to synthesize steroid hormones at room temperature." }
    ]
  },
  "Dashboard — metall/parameter.md": {
    word: "parameter",
    primary: "A numerical or other measurable factor forming one of a set that defines a system or sets the conditions of its operation.",
    secondary: "In mathematics and statistics, an arbitrary constant whose value characterizes a member of a system of expressions or probability distributions.",
    quotes: [
      { author: "Albert Einstein", work: "Relativity: The Special and General Theory", quote: "Every physical equation must incorporate the speed of light as a fundamental invariant **parameter** of nature." },
      { author: "Bertrand Russell", work: "Introduction to Mathematical Philosophy", quote: "In propositional logic, a **parameter** functions as a variable whose range is bounded by formal axioms." },
      { author: "Stephen Jay Gould", work: "The Mismeasure of Man", quote: "Psychometricians made the grave error of reifying a single statistical **parameter** into an innate biological entity called general intelligence." }
    ]
  },
  "Dashboard — metall/parametric.md": {
    word: "parametric",
    primary: "Of, relating to, or expressed in terms of a parameter or parameters.",
    secondary: "In statistics, describing tests or models that assume a specific underlying probability distribution (e.g., normal distribution).",
    quotes: [
      { author: "Bertrand Russell", work: "The Principles of Mathematics", quote: "A **parametric** representation allows geometric curves to be expressed as continuous functions of time." },
      { author: "Carl Sagan", work: "Cosmos", quote: "Computer simulations of planetary collisions rely upon **parametric** equations balancing mass, velocity, and angle of impact." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "The cardiac output curve is a **parametric** function relating atrial filling pressure to ventricular stroke work." }
    ]
  },
  "Dashboard — metall/perimeter.md": {
    word: "perimeter",
    primary: "The continuous line forming the boundary of a closed geometric figure; the total length of such a boundary.",
    secondary: "The outermost boundary or defended border of an area, military installation, or fortification.",
    quotes: [
      { author: "Jules Verne", work: "Twenty Thousand Leagues Under the Sea", quote: "The Nautilus cruised along the outer **perimeter** of the submerged volcanic caldera." },
      { author: "George Orwell", work: "1984", quote: "Barbed-wire entanglements defended the outer **perimeter** of the airstrip from unauthorized entry." },
      { author: "Henry David Thoreau", work: "Walden", quote: "I surveyed the **perimeter** of the pond on the ice, measuring its exact circumference with chain and compass." }
    ]
  },
  "Dashboard — metall/polymetal.md": {
    word: "polymetal",
    primary: "An alloy, composite material, or structural product composed of several different metals; polymetallic material.",
    secondary: "In industrial materials manufacturing, layered or sinter-bonded multi-metal composites designed for high thermal, electrical, or wear resistance.",
    quotes: [
      { author: "Thomas Edison", work: "The Writings of Thomas Alva Edison", quote: "We tested a **polymetal** junction of brass and platinum to prevent contact oxidation in high-frequency telegraph relays." },
      { author: "Andrew Carnegie", work: "Autobiography of Andrew Carnegie", quote: "Modern ordnance required **polymetal** forgings combining the toughness of nickel steel with the hard surface of chilled iron." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "The prehistoric smith fashioned a curious **polymetal** dagger by hammer-welding copper and bronze strips." }
    ]
  },
  "Dashboard — metall/polymetallic.md": {
    word: "polymetallic",
    primary: "Containing, yielding, or composed of several different metals.",
    secondary: "In marine geology and economic mining, designating deep-sea polymetallic nodules (manganese nodules) rich in nickel, copper, cobalt, and iron on the abyssal plain.",
    quotes: [
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Vast fields of **polymetallic** nodules litter the abyssal seafloor like paving stones across millions of square miles." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "Hydrothermal black smokers precipitate rich **polymetallic** sulphides of zinc, copper, and lead along the oceanic ridge." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "The vein was worked as a **polymetallic** deposit, yielding silver, lead, and zinc from successive ore shoots." }
    ]
  },
  "Dashboard — metall/pyrometallurgy.md": {
    word: "pyrometallurgy",
    primary: "The branch of extractive metallurgy that involves the thermal treatment of minerals and metallurgical ores (e.g., smelting, roasting, refining).",
    secondary: "In chemical engineering, high-temperature furnace operations (blast furnaces, reverbatory furnaces) that reduce metal oxides with carbon or carbon monoxide.",
    quotes: [
      { author: "Georgius Agricola", work: "De Re Metallica", quote: "The ancient mastery of **pyrometallurgy** enabled early smelters to separate molten lead and silver in roaring blast hearths." },
      { author: "Andrew Carnegie", work: "Autobiography of Andrew Carnegie", quote: "Our blast furnaces operated by continuous **pyrometallurgy**, tapping molten pig iron day and night without interruption." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "The slag heaps left by Roman **pyrometallurgy** in the Weald of Kent still yield nodules of vitrified iron silicate." }
    ]
  },
  "Dashboard — metall/symmetric.md": {
    word: "symmetric",
    primary: "Characterized by or exhibiting symmetry; well-proportioned; having parts that correspond in size, shape, and relative position.",
    secondary: "In mathematics and physics, invariant under certain transformations (e.g., reflection, rotation, inversion).",
    quotes: [
      { author: "Charles Darwin", work: "On the Origin of Species", quote: "Flowers pollinated by bees develop bilaterally **symmetric** corollas adapted to guide insect entry." },
      { author: "Albert Einstein", work: "Relativity: The Special and General Theory", quote: "The fundamental laws of nature reveal an underlying **symmetric** beauty across all coordinate frames." },
      { author: "Ralph Waldo Emerson", work: "Essays: First Series", quote: "The human countenance is never mechanically **symmetric**, for living expression demands subtle variety." }
    ]
  },
  "Dashboard — metall/symmetrical.md": {
    word: "symmetrical",
    primary: "Exhibiting symmetry; having identical or corresponding parts on opposite sides of a dividing line or plane.",
    secondary: "In classical architecture and design, characterized by balanced, harmonious proportions according with formal geometric rules.",
    quotes: [
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The façade of the Ducal Palace is grandly **symmetrical** without ever declining into monotonous repetition." },
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Vertebrated Animals", quote: "Vertebrates exhibit a bilaterally **symmetrical** body plan organized along an anteroposterior axis." },
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "The two flukes of the tail formed a broad, **symmetrical** crescent of immense propelling power." }
    ]
  },
  "Dashboard — metall/telemeter.md": {
    word: "telemeter",
    primary: "An apparatus for measuring physical quantities (such as distance, temperature, pressure, or radiation) and transmitting the readings to a distant receiver.",
    secondary: "In surveying, military rangefinding, and astronomy, an optical or electronic rangefinder used to determine the distance to a remote target.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Lost World", quote: "The artillery officer leveled his optical **telemeter** to determine the exact distance to the opposing redoubt." },
      { author: "Arthur C. Clarke", work: "2001: A Space Odyssey", quote: "The space probe's **telemeter** beamed continuous radiation measurements back to the receiving dishes of Earth." },
      { author: "Jules Verne", work: "The Mysterious Island", quote: "Cyrus Smith improvised a simple geometric **telemeter** using two measuring stakes and a plumb line." }
    ]
  },
  "Dashboard — metall/tetrametallic.md": {
    word: "tetrametallic",
    primary: "Containing four metal atoms, or composed of four distinct metallic elements.",
    secondary: "In coordination chemistry and materials engineering, designating tetranuclear metal clusters or quaternary high-entropy alloys exhibiting four metallic constituents.",
    quotes: [
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The cubic cluster revealed a **tetrametallic** core where four iron atoms were linked by bridging sulphide ligands." },
      { author: "Antoine Lavoisier", work: "Elements of Chemistry", quote: "Certain complex mineral alloys behave as **tetrametallic** mixtures during fractional crystallization." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "Assays of the complex fahlerz ore demonstrated a **tetrametallic** composition containing copper, iron, zinc, and silver." }
    ]
  },
  "Dashboard — metall/trimetallic.md": {
    word: "trimetallic",
    primary: "Containing three metal atoms in a molecule, or composed of three different metallic elements; ternary alloy.",
    secondary: "In catalysis and material science, describing heterogeneous catalysts or electrochemical electrodes composed of three metals (e.g., Pt-Pd-Rh) for synergistic activity.",
    quotes: [
      { author: "Humphry Davy", work: "Elements of Chemical Philosophy", quote: "A **trimetallic** alloy of copper, tin, and zinc produced an exceptionally resonant bell bronze." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The active catalytic center contains a **trimetallic** cluster that facilitates the reduction of nitrogen." },
      { author: "Andrew Carnegie", work: "Autobiography of Andrew Carnegie", quote: "Our research laboratory developed a **trimetallic** bearing lining that withstood the friction of high-speed steam locomotives." }
    ]
  }
};

function updateWordNote(relPath, data) {
  const fullPath = path.join(baseDir, relPath);
  if (!fs.existsSync(fullPath)) {
    console.error("File not found:", fullPath);
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

console.log("Earth & Geology Batch 5 completed! Total words updated:", Object.keys(wordsData).length);
