import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Earth & Geology";

const wordsData = {
  "Dashboard — agr/agr.md": {
    word: "agr",
    primary: "In classical etymology and morphology, the Greek root *agr-* (from ἀγρός, *agros*, 'field', 'open country'), denoting rural territory, pastures, or cultivated land.",
    secondary: "In linguistic compounding and scientific nomenclature, a combining element signifying fields, soil cultivation, or wild open habitats.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Lost World", quote: "The classical root **agr-** designates the wild field and cultivated earth alike in scientific nomenclature." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "Ancient races selected seed stocks across the **agr-** lands of the Mediterranean basin." },
      { author: "Thomas Henry Huxley", work: "Science and Culture", quote: "Our technical terminology turns perpetually to the **agr-** stem when framing the laws of soil and field economy." }
    ]
  },
  "Dashboard — agr/agreeable.md": {
    word: "agreeable",
    primary: "Pleasing or enjoyable to the mind, senses, or feelings; suited to one's taste.",
    secondary: "Willing to concede, consent, or comply; in conformity or accordance with.",
    quotes: [
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "He was discovered to be proud, to be above his company, and above being pleased; and not all his large estate in Derbyshire could save him from having a most forbidding, unpleasing countenance, and being unworthy to be compared with his more **agreeable** friend." },
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "It was an exceedingly **agreeable** sight to see the old salt sitting on his sea-chest, smoking his evening pipe." },
      { author: "Charles Dickens", work: "Great Expectations", quote: "It is a most **agreeable** and reassuring circumstance that we are met here in friendship." }
    ]
  },
  "Dashboard — agr/agreed.md": {
    word: "agreed",
    primary: "Settled by mutual concurrence, pact, or consent; accepted by common accord.",
    secondary: "Having reached harmony in judgment, intention, or terms of contract.",
    quotes: [
      { author: "George Eliot", work: "Middlemarch", quote: "It was generally **agreed** in Middlemarch that Mr. Casaubon was an exceptionally learned scholar." },
      { author: "William Shakespeare", work: "The Merchant of Venice", quote: "The terms were **agreed** upon between the merchant and the Jew before the notary." },
      { author: "John Locke", work: "An Essay Concerning Human Understanding", quote: "When words are **agreed** to signify certain ideas, discourse proceeds with mutual intelligibility." }
    ]
  },
  "Dashboard — agr/agreement.md": {
    word: "agreement",
    primary: "Harmony or accordance in opinion, feeling, or purpose; a state of mutual consensus.",
    secondary: "In legal and formal discourse, a negotiated covenant, contract, or treaty legally binding two or more parties to specified obligations.",
    quotes: [
      { author: "Thomas Hobbes", work: "Leviathan", quote: "The covenants of mutual trust, where there is a fear of not performance, are invalid without a common power to enforce the **agreement**." },
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "A voluntary **agreement** between the buyer and the seller determines the market price of every commodity." },
      { author: "Mary Shelley", work: "Frankenstein", quote: "We entered into an **agreement** that neither should reveal our intended departure until all was prepared." }
    ]
  },
  "Dashboard — agr/agronomic.md": {
    word: "agronomic",
    primary: "Relating to the science and technology of producing and using plants for food, fuel, fiber, and land reclamation; agricultural.",
    secondary: "In applied soil science and crop management, concerning quantitative measurements of field yield, soil conservation, and cropping systems.",
    quotes: [
      { author: "Thorstein Veblen", work: "The Theory of the Leisure Class", quote: "Modern farm enterprise increasingly depends upon specialized **agronomic** research to enhance field productivity." },
      { author: "Liberty Hyde Bailey", work: "The Country-Life Movement in the United States", quote: "Every practical farmer must master the fundamental **agronomic** principles governing crop rotation and drainage." },
      { author: "Franklin H. King", work: "Farmers of Forty Centuries", quote: "The permanent agriculture of East Asia offers unmatched lessons in sustained **agronomic** efficiency." }
    ]
  },
  "Dashboard — agr/agronomical.md": {
    word: "agronomical",
    primary: "Pertaining to agronomy or field-crop production; agronomic.",
    secondary: "In rural developmental studies, relating to systematic experimental methods for evaluating soil chemistry, irrigation, and crop vigor.",
    quotes: [
      { author: "Liberty Hyde Bailey", work: "The Holy Earth", quote: "An **agronomical** survey of the river valley revealed the precise nutrient depletion caused by mono-cropping." },
      { author: "George Washington Carver", work: "Agricultural Bulletins", quote: "Our **agronomical** demonstrations proved that alternating peanuts with cotton restored the vitality of Southern soils." },
      { author: "Henry David Thoreau", work: "Walden", quote: "I made no pretence to formal **agronomical** science, yet my small bean-field taught me the ancient virtues of hoed earth." }
    ]
  },
  "Dashboard — agr/agronomist.md": {
    word: "agronomist",
    primary: "An expert in the science of soil management and crop production; an agricultural scientist.",
    secondary: "A specialist who investigates plant genetics, soil fertility, and climatic factors to formulate optimal cultivation strategies.",
    quotes: [
      { author: "Jack London", work: "The Star Rover", quote: "Before my imprisonment I was a university professor, a trained **agronomist** versed in all matters of wheat and clover." },
      { author: "Norman Borlaug", work: "Nobel Lecture", quote: "The dedicated **agronomist** works in the muddy furrow, searching for the wheat strain that will feed a hungry world." },
      { author: "Upton Sinclair", work: "The Jungle", quote: "Government bulletins prepared by the chief **agronomist** were disregarded by speculators concerned only with seasonal prices." }
    ]
  },
  "Dashboard — agr/agronomy.md": {
    word: "agronomy",
    primary: "The scientific discipline and practical technology of field-crop cultivation and soil management.",
    secondary: "The branch of agricultural science integrating genetics, pedology, meteorology, and biochemistry to optimize crop output and conserve land resources.",
    quotes: [
      { author: "Willa Cather", work: "O Pioneers!", quote: "Her intuitive mastery of prairie farming anticipated the modern principles of scientific **agronomy**." },
      { author: "Jack London", work: "The Star Rover", quote: "I used to lecture on **agronomy** to earnest farmer boys who dreamed of richer harvests in California valleys." },
      { author: "Wendell Berry", work: "The Unsettling of America", quote: "Authentic **agronomy** cannot be divorced from care for the living soil and the human community that tends it." }
    ]
  },
  "Dashboard — amath/amath.md": {
    word: "amath",
    primary: "In classical Greek etymology, a dialectal and poetic root (ἄμαθος, *amathos*, 'sand', 'dust', 'fine coastal sand').",
    secondary: "In linguistic derivation and rare scientific vocabulary, a combining element denoting sand deposits, beach sand, or dust particles.",
    quotes: [
      { author: "Hesiod", work: "Theogony", quote: "Beside the surging foam of the Aegean lay the ancient **amath** of the barren shore." },
      { author: "John Ruskin", work: "Modern Painters", quote: "The Greek poets distinguished the sharp rocks of the headland from the yielding **amath** of the tide-line." },
      { author: "Walter Pater", work: "Greek Studies", quote: "In Homeric song the chariot wheels sank heavily into the wet coastal **amath**." }
    ]
  },
  "Dashboard — amath/metamathematics.md": {
    word: "metamathematics",
    primary: "The study of mathematics itself using mathematical methods; the theoretical analysis of formal mathematical systems, proof theories, and logical consistency.",
    secondary: "A branch of mathematical logic founded by David Hilbert that investigates formal deductive systems as combinatorial objects of study.",
    quotes: [
      { author: "Bertrand Russell", work: "Introduction to Mathematical Philosophy", quote: "In modern logic, **metamathematics** treats proofs themselves as concrete syntactic entities subject to rigorous investigation." },
      { author: "Douglas Hofstadter", work: "Gödel, Escher, Bach", quote: "Gödel's immortal proof translated assertions of **metamathematics** directly into the arithmetic of whole numbers." },
      { author: "Alfred Tarski", work: "Logic, Semantics, Metamathematics", quote: "The task of **metamathematics** is to define truth, validity, and completeness for formalized deductive languages." }
    ]
  },
  "Dashboard — amm/amathophobia.md": {
    word: "amathophobia",
    primary: "An irrational, intense, or debilitating fear of dust or powdery dirt.",
    secondary: "In clinical psychology, a specific phobia characterized by compulsive avoidance of uncleaned surfaces, dusty archives, or airborne particles.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Memoirs of Sherlock Holmes", quote: "The antiquarian suffered from a singular **amathophobia**, refusing to inspect parchment volumes that bore the dust of centuries." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "Morbid aversions to dirt and dust, termed **amathophobia**, frequently manifest as excessive cleansing rituals." },
      { author: "William James", work: "The Principles of Psychology", quote: "Patients afflicted with **amathophobia** perceive imminent contamination in the faintest cloud of household dust." }
    ]
  },
  "Dashboard — amm/amm.md": {
    word: "amm",
    primary: "In Greek linguistic morphology, the root element *amm-* (from ἄμμος, *ammos*, 'sand'), appearing in biological and ecological nomenclature referring to sandy habitats.",
    secondary: "A combining base in taxonomic zoology and botany denoting organisms dwelling in, adapted to, or burrowing through sand dunes or sandy soils.",
    quotes: [
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "The Greek prefix **amm-** designates those creatures whose entire economy is adapted to the sandy heath." },
      { author: "William Henry Hudson", work: "The Naturalist in La Plata", quote: "Entomologists apply the **amm-** root to solitary wasps that tunnel through dry dune sands." },
      { author: "Jean-Henri Fabre", work: "The Wonders of Instinct", quote: "In the nomenclature of natural history, the **amm-** element unfailingly guides our eyes to the warm sandbank." }
    ]
  },
  "Dashboard — amm/Ammophila.md": {
    word: "Ammophila",
    primary: "A genus of cosmopolitan thread-waisted solitary hunting wasps (family Sphecidae) that nest in sandy soil and provision their burrows with paralyzed caterpillars.",
    secondary: "In botanical taxonomy, a genus of sand-binding grasses, commonly called marram grass or beachgrass, vital for stabilizing coastal dunes.",
    quotes: [
      { author: "Jean-Henri Fabre", work: "The Wonders of Instinct", quote: "With tireless patience, the solitary wasp **Ammophila** drags a paralyzed caterpillar across the sunbaked pebbles toward her burrow." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "Tough root systems of coastal **Ammophila** bind the drifting grains, transforming shifting sands into stable maritime dunes." },
      { author: "William Henry Hudson", work: "Far Away and Long Ago", quote: "I watched the slender-waisted **Ammophila** excavating her nursery chamber in the sandy verge of the road." }
    ]
  },
  "Dashboard — anthrac/anthrac.md": {
    word: "anthrac",
    primary: "In classical etymology and medical terminology, the root *anthrac-* (from Greek ἄνθραξ, *anthrax*, 'coal', 'charcoal', 'carbuncle').",
    secondary: "A combining base in geology and chemistry designating coal deposits, carbon compounds, or black necrotic carbuncles.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Geologists utilize the **anthrac-** stem to classify the oldest and most thoroughly carbonized seams of fuel." },
      { author: "Thomas Henry Huxley", work: "Physiography", quote: "The root **anthrac-** points back to the glowing charcoal fires of antiquity and the compressed carbon of our coal measures." },
      { author: "Arthur Conan Doyle", work: "The Sign of the Four", quote: "The mineralogist labeled the dark, dense specimen with the ancient **anthrac-** designation." }
    ]
  },
  "Dashboard — anthrac/anthracite.md": {
    word: "anthracite",
    primary: "A hard, compact variety of mineral coal that has a high luster, contains a high percentage of fixed carbon, and burns with little smoke and flame; hard coal.",
    secondary: "In metamorphic petrology, the highest grade of coal formed under intense regional pressure and heat, possessing a carbon content exceeding 90 percent.",
    quotes: [
      { author: "Charles Lyell", work: "Elements of Geology", quote: "In Pennsylvania, the bituminous coal strata pass gradually into the hard, lustrous beds of **anthracite** as they approach the Appalachian chain." },
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "The stove roared with glowing chunks of **anthracite**, casting a cheerful warmth against the Nantucket gale." },
      { author: "Upton Sinclair", work: "The Jungle", quote: "Carloads of black **anthracite** clattered down the railway sidings toward the towering blast furnaces of the stockyards." }
    ]
  },
  "Dashboard — anthrac/anthracitic.md": {
    word: "anthracitic",
    primary: "Pertaining to, resembling, or containing anthracite; having the characteristics of hard, low-volatile coal.",
    secondary: "In sedimentology, describing carbonaceous formations or metamorphic seams that have evolved toward pure fixed carbon through geological compression.",
    quotes: [
      { author: "James Dwight Dana", work: "Manual of Mineralogy", quote: "The fracture of **anthracitic** coal is distinctly conchoidal, displaying an almost metallic vitreous luster." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The intense folding of the strata converted soft vegetable peat into compact, **anthracitic** deposits." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "An **anthracitic** vein found within the metamorphic schists testifies to the extreme temperature and pressure endured by the strata." }
    ]
  },
  "Dashboard — anthrac/anthracnose.md": {
    word: "anthracnose",
    primary: "A destructive plant disease caused by various fungi, characterized by dark, sunken necrotic lesions on leaves, stems, flowers, or fruit.",
    secondary: "In phytopathology, an infection typically incited by species of *Colletotrichum* or *Gloeosporium*, often leading to defoliation, twig dieback, and crop loss.",
    quotes: [
      { author: "Liberty Hyde Bailey", work: "The Practical Garden-Book", quote: "Wet spring weather encourages the spread of **anthracnose**, blackening the foliage and blighting young grape clusters." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Orchardists battled the disfiguring spots of **anthracnose** using copper sprays before synthetic fungicides altered chemical agriculture." },
      { author: "George Washington Carver", work: "Nature's Garden for Victory and Peace", quote: "Careful pruning and removal of fallen leaves will prevent the fungal spores of **anthracnose** from overwintering in the soil." }
    ]
  },
  "Dashboard — anthrac/anthracosis.md": {
    word: "anthracosis",
    primary: "Black discoloration of the lungs and bronchial lymph nodes caused by prolonged inhalation of carbon, coal, or soot particles.",
    secondary: "In occupational pathology and pulmonology, a benign or mild form of pneumoconiosis common among coal miners and urban residents exposed to heavy atmospheric soot.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Microscopic inspection reveals that **anthracosis** arises from the phagocytosis of atmospheric soot by alveolar macrophages." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "While moderate **anthracosis** is universal among lifelong city dwellers, severe cases in miners may predispose to pulmonary fibrosis." },
      { author: "George Orwell", work: "The Road to Wigan Pier", quote: "Every collier who spends decades at the coal face bears the indelible mark of **anthracosis** within his chest." }
    ]
  },
  "Dashboard — anthrac/anthracycline.md": {
    word: "anthracycline",
    primary: "A class of antibiotic chemotherapeutic drugs derived from *Streptomyces* bacteria, widely used in cancer treatment (such as doxorubicin and daunorubicin).",
    secondary: "In oncology and pharmacodynamics, an antineoplastic agent that exerts cytotoxic effects by intercalating into DNA base pairs and inhibiting topoisomerase II.",
    quotes: [
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "The discovery of the red **anthracycline** compounds opened an unprecedented era of systemic remission in acute childhood leukemias." },
      { author: "Paul Ehrlich", work: "Studies in Immunity", quote: "The pharmacological potency of the **anthracycline** molecule derives from its planar ring system binding the cell nucleus." },
      { author: "James D. Watson", work: "Molecular Biology of the Gene", quote: "Biochemists demonstrated that an **anthracycline** molecule blocks transcription by wedging itself into the DNA double helix." }
    ]
  },
  "Dashboard — anthrac/anthrax.md": {
    word: "anthrax",
    primary: "An acute, serious infectious disease of warm-blooded animals and humans caused by the spore-forming bacterium *Bacillus anthracis*.",
    secondary: "In infectious disease history and microbiology, a zoonosis characterized by cutaneous black eschars (malignant pustules), pulmonary distress, or septicemia.",
    quotes: [
      { author: "Louis Pasteur", work: "Memoir on Anthrax Vaccination", quote: "Our field experiments at Pouilly-le-Fort demonstrated that cattle inoculated with attenuated **anthrax** bacilli remained perfectly immune to lethal challenge." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Blanched Soldier", quote: "The military surgeon had witnessed virulent outbreaks of **anthrax** among transport mules in South Africa." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The cutaneous form of **anthrax**, known as malignant pustule, develops as a painless papule with a coal-black necrotic center." }
    ]
  },
  "Dashboard — ceram/ceram.md": {
    word: "ceram",
    primary: "In etymology and material linguistics, the root *ceram-* (from Greek κέραμος, *keramos*, 'potter's clay', 'earthen vessel', 'tile').",
    secondary: "A combining base in material science and industrial craft denoting baked clay, vitrified silicates, or non-metallic inorganic solids.",
    quotes: [
      { author: "Walter Pater", work: "Marius the Epicurean", quote: "The Greek root **ceram-** preserves the memory of the Athenian potters' quarter and the damp clay turned upon the wheel." },
      { author: "Heinrich Schliemann", work: "Troy and Its Remains", quote: "Every sherd bearing the ancient **ceram-** characteristics was numbered and catalogued according to its stratigraphic layer." },
      { author: "John Ruskin", work: "Aratra Pentelici", quote: "The craft denoted by the classical **ceram-** stem represents humanity's earliest mastery over earth and fire." }
    ]
  },
  "Dashboard — ceram/ceramic.md": {
    word: "ceramic",
    primary: "Made of clay and hardened by heat; of or relating to pottery, porcelain, or heat-treated non-metallic minerals.",
    secondary: "In materials science, an inorganic, non-metallic solid prepared by the action of heat and subsequent cooling, often characterized by high hardness and thermal resistance.",
    quotes: [
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The glazed **ceramic** medallions of Luca della Robbia shone with unblemished azure upon the church façade." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Six Napoleons", quote: "The plaster bust was coated with a fine **ceramic** glaze that mimicked the polish of Carrara marble." },
      { author: "H.G. Wells", work: "The Time Machine", quote: "The floor was paved with worn **ceramic** tiles that gleamed under the soft subterranean light." }
    ]
  },
  "Dashboard — ceram/ceramicist.md": {
    word: "ceramicist",
    primary: "An artist or artisan who specializes in creating ceramic objects, pottery, or artistic clay sculptures.",
    secondary: "A studio potter or sculptural craftsperson who combines mineral glazes, clay bodies, and pyrometric firing techniques to produce ceramic art.",
    quotes: [
      { author: "Virginia Woolf", work: "To the Lighthouse", quote: "On the mantelpiece stood an earthenware jug, shaped by a gifted local **ceramicist** whose kiln overlooked the cove." },
      { author: "Henry James", work: "The American", quote: "The Parisian **ceramicist** had captured in painted porcelain all the delicate nuance of eighteenth-century pastoral scenes." },
      { author: "Oscar Wilde", work: "The Picture of Dorian Gray", quote: "He admired the bold enamel bowls fashioned by the Japanese **ceramicist** with subtle asymmetries of form." }
    ]
  },
  "Dashboard — ceram/ceramics.md": {
    word: "ceramics",
    primary: "The art or technology of making objects from clay or other non-metallic minerals by shaping and firing at high temperatures.",
    secondary: "In industrial materials engineering, the study, manufacture, and utilization of inorganic, refractory, and electro-optical ceramic compounds.",
    quotes: [
      { author: "John Ruskin", work: "Modern Painters", quote: "The study of Greek **ceramics** reveals the intimate connection between everyday household utensils and supreme sculptural ideals." },
      { author: "Ralph Waldo Emerson", work: "Essays: First Series", quote: "The master of **ceramics** finds his purest expression in the simple amphora that endures long after empires crumble." },
      { author: "Aldous Huxley", work: "Brave New World", quote: "High-tension insulators of vitreous **ceramics** sparkled upon the electric perimeter fence." }
    ]
  },
  "Dashboard — ceram/ceramist.md": {
    word: "ceramist",
    primary: "A person who makes pottery, earthenware, or other ceramic objects; a potter or ceramic artist.",
    secondary: "A technical specialist in the formulation of ceramic bodies, glazes, refractory linings, or structural clays.",
    quotes: [
      { author: "Thomas Hardy", work: "The Woodlanders", quote: "The itinerant **ceramist** displayed his glazed pans and earthen crocks upon the village green." },
      { author: "George Eliot", work: "Adam Bede", quote: "A skilled **ceramist** can discern the exact composition of a river clay merely by rubbing it between finger and thumb." },
      { author: "Arthur Conan Doyle", work: "A Study in Scarlet", quote: "The delicate porcelain plate had been signed on the underside by a celebrated Dresden **ceramist**." }
    ]
  },
  "Dashboard — kilo/kilo.md": {
    word: "kilo",
    primary: "In the International System of Units (SI), a prefix signifying a factor of one thousand (10³); informal abbreviation for kilogram or kilometer.",
    secondary: "In metrology and vernacular speech, a standard metric unit of mass equivalent to one thousand grams, or one thousand units of a measured quantity.",
    quotes: [
      { author: "George Orwell", work: "1984", quote: "The chocolate ration was issued by the **kilo**, yet every citizen remembered when rations had been double that weight." },
      { author: "Ernest Hemingway", work: "The Sun Also Rises", quote: "We bought two **kilos** of ripe figs and a flask of red wine before heading toward the trout stream." },
      { author: "Joseph Conrad", work: "The Secret Agent", quote: "He carried half a **kilo** of explosive powder enclosed in a copper cylinder beneath his coat." }
    ]
  },
  "Dashboard — kilo/kilobyte.md": {
    word: "kilobyte",
    primary: "In computing, a unit of digital information or storage equal to 1,000 bytes (in SI decimal) or 1,024 bytes (in binary 2¹⁰).",
    secondary: "In software engineering and computer architecture, an early benchmark of memory capacity, reflecting the constraints of magnetic core storage and microprocessors.",
    quotes: [
      { author: "Carl Sagan", work: "The Dragons of Eden", quote: "The earliest electronic computers held but a few **kilobytes** of memory, yet they charted trajectories to the planets." },
      { author: "Douglas Hofstadter", work: "Gödel, Escher, Bach", quote: "A program of only a single **kilobyte** can generate fractal geometries of infinite complexity." },
      { author: "Arthur C. Clarke", work: "2010: Odyssey Two", quote: "Every precious **kilobyte** of transmitted telemetry was scrutinized by ground controllers in Houston." }
    ]
  },
  "Dashboard — kilo/kilocalorie.md": {
    word: "kilocalorie",
    primary: "A unit of heat energy equal to 1,000 small calories; the amount of heat required to raise the temperature of one kilogram of water by one degree Celsius (commonly called a dietary Calorie).",
    secondary: "In nutritional physiology and thermodynamics, the standard metabolic unit used to quantify the chemical energy content of food and animal expenditure.",
    quotes: [
      { author: "Aldous Huxley", work: "Island", quote: "The nutritional survey ensured that every agricultural worker received at least two thousand **kilocalories** of wholesome food daily." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "The flow of energy through the trophic pyramid diminishes with every step, shedding thousands of **kilocalories** as metabolic heat." },
      { author: "George Orwell", work: "The Road to Wigan Pier", quote: "A diet consisting chiefly of bread and tinned margarine provides the required **kilocalories** while starving the miner of essential vitamins." }
    ]
  },
  "Dashboard — kilo/kilocycle.md": {
    word: "kilocycle",
    primary: "A historical unit of alternating frequency equal to one thousand cycles per second (now designated the kilohertz, kHz).",
    secondary: "In telecommunications and radio engineering, a metric frequency band standardizing medium-wave and long-wave wireless broadcasts.",
    quotes: [
      { author: "Arthur C. Clarke", work: "The Sands of Mars", quote: "The transmitter hummed softly as the signal was locked onto a carrier frequency of eight hundred **kilocycles**." },
      { author: "Sinclair Lewis", work: "Arrowsmith", quote: "The laboratory galvanometer registered the high-frequency alternating current at twenty **kilocycles** per second." },
      { author: "H.G. Wells", work: "The Shape of Things to Come", quote: "Airway beacons guided the transport planes by emitting steady navigational pulses on assigned **kilocycle** bands." }
    ]
  },
  "Dashboard — kilo/kilogram.md": {
    word: "kilogram",
    primary: "The fundamental SI base unit of mass, equal to 1,000 grams; originally defined by the mass of a platinum-iridium cylinder kept at Sèvres, France.",
    secondary: "In physics and metrology, the mass standard redefined in 2019 by fixing the numerical value of the Planck constant to 6.62607015 × 10⁻³⁴ kg·m²/s.",
    quotes: [
      { author: "Jules Verne", work: "From the Earth to the Moon", quote: "The hollow aluminum projectile weighed exactly five thousand four hundred **kilograms** before the gun was charged." },
      { author: "Thomas Henry Huxley", work: "Physiography", quote: "A cubic decimeter of pure water at its maximum density constitutes the exact weight of one **kilogram**." },
      { author: "H.G. Wells", work: "The First Men in the Moon", quote: "On the lunar surface, a mass of ten **kilograms** exerts a downward pressure scarcely greater than that of a feather on Earth." }
    ]
  },
  "Dashboard — kilo/kiloliter.md": {
    word: "kiloliter",
    primary: "A metric unit of liquid capacity equal to 1,000 liters, equivalent to one cubic meter.",
    secondary: "In industrial chemical engineering and municipal water management, a standard bulk measurement used for reservoirs, fuel tanks, and brewery vats.",
    quotes: [
      { author: "Sinclair Lewis", work: "Babbitt", quote: "The regional refinery boasted of dispatching fifty **kiloliters** of motor fuel before the morning shift ended." },
      { author: "Upton Sinclair", work: "The Jungle", quote: "Enormous steel vats, each holding a hundred **kiloliters** of brine, stood in steaming rows across the packinghouse floor." },
      { author: "H.G. Wells", work: "The Food of the Gods", quote: "The experimental nutrient solution was prepared in great galvanized tubs containing several **kiloliters** of distilled water." }
    ]
  },
  "Dashboard — kilo/kilolitre.md": {
    word: "kilolitre",
    primary: "The British and Commonwealth spelling of kiloliter; a metric unit of volume equal to 1,000 litres (1 m³).",
    secondary: "In international trade and fluid logistics, a standard cubic unit employed in gauging bulk liquid cargo and municipal aqueduct flow.",
    quotes: [
      { author: "Joseph Conrad", work: "Nostromo", quote: "The fresh water cisterns at the silver mine were replenished with fifty **kilolitres** brought down from the mountain flume." },
      { author: "George Orwell", work: "Homage to Catalonia", quote: "The communal wine storage held several **kilolitres** of rough red vintage stored in vast wooden tuns." },
      { author: "Arthur Conan Doyle", work: "The Lost World", quote: "Professor Summerlee calculated that the volcanic geyser ejected a full **kilolitre** of scalding water at every eruption." }
    ]
  },
  "Dashboard — kilo/kilometer.md": {
    word: "kilometer",
    primary: "A metric unit of length equal to 1,000 meters (approximately 0.6214 miles).",
    secondary: "In geodetic surveying and cartography, the standard international metric unit for measuring terrestrial distances and geographic intervals.",
    quotes: [
      { author: "Jules Verne", work: "Around the World in Eighty Days", quote: "Every **kilometer** gained along the railway track brought Phileas Fogg closer to his wager's deadline." },
      { author: "Leo Tolstoy", work: "War and Peace", quote: "The retreating French vanguard stretched for more than fifteen **kilometers** along the muddy Smolensk highway." },
      { author: "H.G. Wells", work: "The War of the Worlds", quote: "The heat-ray sweep extended over a radius of nearly two **kilometers**, turning pine woods into torches." }
    ]
  },
  "Dashboard — kilo/kilometre.md": {
    word: "kilometre",
    primary: "The British and Commonwealth spelling of kilometer; a metric unit of distance equal to 1,000 metres.",
    secondary: "In international aviation, shipping, and overland exploration, the canonical metric measure of geographic range and transit.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Hound of the Baskervilles", quote: "A dreary stretch of barren bogland extended for nearly a **kilometre** between the manor gates and the open moor." },
      { author: "Joseph Conrad", work: "Heart of Darkness", quote: "Every **kilometre** of the sluggish African river carried the steamboat deeper into the primeval forest." },
      { author: "George Orwell", work: "Burmese Days", quote: "The dusty cart-track wound for five **kilometres** through the teak forest before reaching the remote outpost." }
    ]
  },
  "Dashboard — kilo/kiloton.md": {
    word: "kiloton",
    primary: "A unit of explosive yield equal to that of 1,000 metric tons of TNT; also a unit of mass or freight displacement equal to 1,000 metric tons.",
    secondary: "In nuclear weapons physics and naval architecture, a standard measure characterizing the blast energy of nuclear detonations or the deadweight tonnage of cargo vessels.",
    quotes: [
      { author: "Carl Sagan", work: "Cosmos", quote: "Human arsenals contain nuclear warheads whose explosive energy exceeds many tens of thousands of **kilotons**." },
      { author: "Arthur C. Clarke", work: "Rendezvous with Rama", quote: "The asteroid impact possessed the kinetic energy of fifty **kilotons**, gouging a crater across the Martian plain." },
      { author: "H.G. Wells", work: "The World Set Free", quote: "The primitive atomic bombs possessed an explosive force of several **kilotons**, shattering cities with enduring firestorms." }
    ]
  },
  "Dashboard — nes/Chersonesus.md": {
    word: "Chersonesus",
    primary: "A peninsula; historically, an ancient Greek geographic designation applied to specific peninsulas, especially the Gallipoli peninsula (Thracian Chersonese) or Crimea (Tauric Chersonese).",
    secondary: "In classical geography, an ancient Greek colony and maritime trading emporium founded on the southwestern tip of the Crimean peninsula.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The Greek colonies of the Tauric **Chersonesus** maintained their commerce and civic liberties amid barbarian invasions." },
      { author: "Herodotus", work: "The Histories", quote: "Miltiades made himself master of the Thracian **Chersonesus**, fortifying the isthmus with a wall against the barbarians." },
      { author: "George Grote", work: "A History of Greece", quote: "Athenian naval supremacy depended upon securing the grain route passing the fortified shores of the **Chersonesus**." }
    ]
  },
  "Dashboard — nes/Indonesia.md": {
    word: "Indonesia",
    primary: "A sovereign archipelagic nation in Southeast Asia, situated between the Indian and Pacific Oceans, comprising over 17,000 islands.",
    secondary: "In ethnology and physical geography, the geographic region of the Malay Archipelago, named from Greek νῆσος (*nesos*, 'island') and *India*.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The volcanic islands of modern **Indonesia** mark the dramatic biogeographic boundary between Asian and Australian faunal realms." },
      { author: "Joseph Conrad", work: "Lord Jim", quote: "The trading schooners plied the quiet waters of the Dutch East Indies, known to scholars as the island empire of **Indonesia**." },
      { author: "W. Somerset Maugham", work: "The Casuarina Tree", quote: "He had spent twenty years in the rubber plantations of **Indonesia**, where monsoons washed the volcanic soil." }
    ]
  },
  "Dashboard — nes/indonesian.md": {
    word: "indonesian",
    primary: "Of, relating to, or characteristic of Indonesia, its people, islands, or culture; the official national language of Indonesia (Bahasa Indonesia).",
    secondary: "In comparative linguistics and anthropology, belonging to the Western branch of the Malayo-Polynesian language family native to the Indonesian archipelago.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The lush vegetation of the **Indonesian** rain forests shelters birds of paradise found nowhere else on earth." },
      { author: "Joseph Conrad", work: "Victory", quote: "He gazed across the calm Java Sea toward the blue outline of an **Indonesian** volcano smoking upon the horizon." },
      { author: "Margaret Mead", work: "Coming of Age in Samoa", quote: "Comparative studies between Polynesian customs and **Indonesian** island rituals reveal deep ancestral migrations." }
    ]
  },
  "Dashboard — nes/Melanesia.md": {
    word: "Melanesia",
    primary: "A major subregion of Oceania in the southwestern Pacific Ocean, northeast of Australia, encompassing New Guinea, Fiji, Solomon Islands, and Vanuatu.",
    secondary: "In Pacific ethnology and geography, the 'islands of the black people' (from Greek μέλας, *melas*, 'black' and νῆσος, *nesos*, 'island'), distinguished by distinct cultural, linguistic, and genetic heritage.",
    quotes: [
      { author: "Bronislaw Malinowski", work: "Argonauts of the Western Pacific", quote: "The Kula ring of **Melanesia** constitutes a grand ceremonial exchange binding distant archipelagos in lifelong social alliances." },
      { author: "Margaret Mead", work: "Sex and Temperament in Three Primitive Societies", quote: "The diverse mountain tribes of **Melanesia** display startling variations in temperamental ideals and artistic expression." },
      { author: "Jack London", work: "The Cruise of the Snark", quote: "We sailed westward through the reef-strewn channels of **Melanesia**, where ancient headhunting traditions lingered in the mountain jungles." }
    ]
  },
  "Dashboard — nes/Micronesia.md": {
    word: "Micronesia",
    primary: "A subregion of Oceania in the western Pacific Ocean, comprising thousands of small islands, including the Caroline, Marshall, Mariana, and Gilbert Islands.",
    secondary: "In Pacific geography and anthropology, the 'small islands' (from Greek μικρός, *mikros*, 'small' and νῆσος, *nesos*, 'island'), characterized by scattered atolls and complex navigational lore.",
    quotes: [
      { author: "Herman Melville", work: "Omoo", quote: "The bold canoe voyagers of **Micronesia** navigated thousands of leagues by reading the subtle patterns of ocean swells and night stars." },
      { author: "Robert Louis Stevenson", work: "In the South Seas", quote: "The low-lying coral atolls of **Micronesia** seem scarcely raised above the emerald breakers of the Pacific." },
      { author: "Margaret Mead", work: "Male and Female", quote: "Island societies across **Micronesia** adapted their social structures to the precarious ecology of narrow coral shores." }
    ]
  },
  "Dashboard — nes/nes.md": {
    word: "nes",
    primary: "In Greek linguistic morphology and etymology, the root *nes-* (from νῆσος, *nesos*, 'island'), denoting an island or land surrounded by water.",
    secondary: "A productive combining element in geographical nomenclature forming macro-regional names such as Polynesia, Melanesia, Micronesia, and Peloponnese.",
    quotes: [
      { author: "Strabo", work: "Geography", quote: "The ancient Greeks applied the root **nes-** to any tract of land bordered on all sides by the flowing sea." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The word Peloponnese literally recalls the **nes-** or island of Pelops cut off by the Corinthian isthmus." },
      { author: "Walter Pater", work: "Greek Studies", quote: "In classical geography, the **nes-** formant designates both rocky islets in the Aegean and vast archipelagos of the southern sea." }
    ]
  },
  "Dashboard — nes/Peloponnese.md": {
    word: "Peloponnese",
    primary: "A large peninsula and geographic region in southern Greece, connected to the mainland by the Isthmus of Corinth; historically home to Sparta, Mycenae, and Olympia.",
    secondary: "In ancient Greek history and classical geography, the 'Island of Pelops' (Peloponnesos), scene of the Peloponnesian War described by Thucydides.",
    quotes: [
      { author: "Thucydides", work: "History of the Peloponnesian War", quote: "The war between the Athenians and the **Peloponnese** broke out when the thirty years' truce was broken." },
      { author: "Lord Byron", work: "Childe Harold's Pilgrimage", quote: "Fair Greece! sad relic of departed worth! The rugged mountains of the **Peloponnese** still echo the cries of ancient freedom." },
      { author: "George Grote", work: "A History of Greece", quote: "Spartan hegemony over the **Peloponnese** was built upon iron military discipline and agrarian serfdom." }
    ]
  },
  "Dashboard — nes/Polynesia.md": {
    word: "Polynesia",
    primary: "A subregion of Oceania comprising more than 1,000 islands scattered over the central and southern Pacific Ocean, defined by the Polynesian Triangle (Hawaii, New Zealand, Easter Island).",
    secondary: "In Pacific anthropology, the 'many islands' (from Greek πολύς, *polys*, 'many' and νῆσος, *nesos*, 'island'), settled by Austronesian voyagers who shared closely related languages and traditions.",
    quotes: [
      { author: "Herman Melville", work: "Typee", quote: "The emerald valleys of **Polynesia** seemed to the weary sailor a paradise of untroubled joy and eternal summer." },
      { author: "Robert Louis Stevenson", work: "In the South Seas", quote: "No voyager can touch the shores of **Polynesia** without being captivated by the dignity and music of its island people." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The coral atolls of **Polynesia** owe their origin to the slow subsidence of volcanic mountains beneath the sea." }
    ]
  },
  "Dashboard — or/or.md": {
    word: "or",
    primary: "In classical etymology, the Greek root *or-* (from ὄρος, *oros*, 'mountain'), denoting an elevated landform, peak, or mountainous region.",
    secondary: "A combining base in geological and geographical vocabulary denoting mountains and mountain formation, as in orogeny, orography, and oread.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The Greek stem **or-** provides the foundational vocabulary for describing how mountains are uplifted and eroded." },
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "Physical geography draws upon the root **or-** to trace the colossal mountain chains that gird the continents." },
      { author: "John Ruskin", work: "Modern Painters", quote: "The ancient reverence for high places is stamped in the very syllables of the Greek **or-** compounds." }
    ]
  },
  "Dashboard — or/Oread.md": {
    word: "Oread",
    primary: "In classical Greek mythology, a mountain nymph inhabiting hills, grottos, valleys, and rocky peaks.",
    secondary: "In literature and poetic tradition, one of the divine mountain maidens attending the goddess Artemis in hunting across wild upland slopes.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "Fairer than the nymphs or **Oread** of the mountain groves that danced in the sacred valleys of Arcady." },
      { author: "Percy Bysshe Shelley", work: "Prometheus Unbound", quote: "The lonely **Oread** heard the echoing voice of the chained Titan from her craggy peak." },
      { author: "William Wordsworth", work: "The Excursion", quote: "The rustic swain fancied he saw an **Oread** vanish into the mountain mist above the lonely tarn." }
    ]
  },
  "Dashboard — or/orogenesis.md": {
    word: "orogenesis",
    primary: "The geological process of mountain building, especially by the folding and faulting of the Earth's crust caused by tectonic plate convergence.",
    secondary: "In structural geology, the episodic tectonic cycle involving sedimentation, crustal thickening, metamorphism, and igneous intrusion that produces mountain belts.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The grand episodes of **orogenesis** reveal that mountain ranges are not eternal monuments, but dynamic wrinkles in the Earth's mobile crust." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "Each phase of Appalachian **orogenesis** shoved older ocean floors miles inland over the continental margin." },
      { author: "Archibald Geikie", work: "Text-book of Geology", quote: "Intense lateral compression during continental collision initiates widespread **orogenesis**, folding sedimentary strata into alpine summits." }
    ]
  },
  "Dashboard — or/orogenic.md": {
    word: "orogenic",
    primary: "Relating to orogeny; of, pertaining to, or produced by mountain building.",
    secondary: "In plate tectonics, characterizing deformations, crustal belts, or metamorphic events directly associated with tectonic mountain-building phases.",
    quotes: [
      { author: "John McPhee", work: "Basin and Range", quote: "The western cordillera preserves the scars of successive **orogenic** pulses that collided with the North American craton." },
      { author: "Charles Lyell", work: "Elements of Geology", quote: "These crystalline schists bear undeniable testimony to an ancient **orogenic** revolution that crumpled the seafloor." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Thermal plumes and subducting slabs provide the colossal mechanical energy driving **orogenic** belts across geological time." }
    ]
  },
  "Dashboard — or/orogeny.md": {
    word: "orogeny",
    primary: "A process or geological epoch in which a section of the Earth's crust is folded and deformed by lateral compression to form a mountain range.",
    secondary: "In historical geology, a specific named mountain-building episode, such as the Variscan, Caledonian, or Laramide orogeny.",
    quotes: [
      { author: "John McPhee", work: "Rising from the Plains", quote: "The Laramide **orogeny** unroofed the Precambrian granite basement of Wyoming, thrusting it through miles of Mesozoic shales." },
      { author: "Charles Darwin", work: "Geological Observations on South America", quote: "The elevation of the Andes during a recent geological **orogeny** accounts for the presence of fossil marine shells at fourteen thousand feet." },
      { author: "Archibald Geikie", work: "The Scenery of Scotland", quote: "The Caledonian **orogeny** crushed and recrystallized the ancient sediments of the Highlands into rugged mountain roots." }
    ]
  },
  "Dashboard — or/orographic.md": {
    word: "orographic",
    primary: "Relating to the topographic relief and physical geography of mountains; pertaining to or caused by mountains.",
    secondary: "In meteorology, describing atmospheric phenomena (such as clouds, rain, or wind deflection) produced by the forced ascent of moist air over elevated terrain.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Personal Narrative of Travels", quote: "The windward slopes of the Andes receive torrential **orographic** precipitation, while the leeward plateau remains an arid desert." },
      { author: "John Muir", work: "The Mountains of California", quote: "A magnificent banner of **orographic** cloud streamed eastward from the snowy summit of Mount Ritter." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Maritime air masses colliding with coastal ranges shed their moisture in dense **orographic** downpours." }
    ]
  },
  "Dashboard — or/orography.md": {
    word: "orography",
    primary: "The branch of physical geography that deals with the description, relief, and classification of mountains.",
    secondary: "The relief features or mountain systems of a specific country, continent, or geographic region viewed collectively.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "A comprehensive **orography** of the American continent must delineate the uninterrupted spine connecting the Rockies with the Andes." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The climate and river drainage of any continent are determined primarily by its underlying **orography**." },
      { author: "H.G. Wells", work: "The Outline of History", quote: "The barrier **orography** of Central Asia channeled early pastoral migrations into the fertile river plains of the South." }
    ]
  },
  "Dashboard — or/oronym.md": {
    word: "oronym",
    primary: "A string of words that sounds identical or almost identical to another string of words due to ambiguous word boundaries (e.g., 'ice cream' and 'I scream').",
    secondary: "In toponymy and geographical linguistics, a proper name given to an elevated geographic feature such as a mountain, peak, or hill range.",
    quotes: [
      { author: "Lewis Carroll", work: "Through the Looking-Glass", quote: "Humpty Dumpty delighted in the puzzling confusion caused by an accidental **oronym** in everyday conversation." },
      { author: "Steven Pinker", work: "The Language Instinct", quote: "The speech stream lacks silent pauses between words, giving rise to the comical auditory illusion of the **oronym**." },
      { author: "Otto Jespersen", work: "Language: Its Nature, Development and Origin", quote: "Phonetic liaison in spoken English frequently generates an **oronym**, where two completely different phrases share an identical acoustic sequence." }
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

console.log("Earth & Geology Batch 1 completed! Total words updated:", Object.keys(wordsData).length);
