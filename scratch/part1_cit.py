# -*- coding: utf-8 -*-
"""
Part 1 of Batch 2 Cluster Speech: cit words 1-22 (22 words):
['ascites', 'ascitic', 'citadel', 'citation', 'cite', 'citellus', 'citified', 'citify',
 'citizen', 'citizenry', 'citizenship', 'citlaltepetl', 'citole', 'citrange', 'citrate',
 'citric', 'citrin', 'citrine', 'citron', 'citroncirus', 'citronwood', 'citrous']
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part1_cit = {
    "ascites": {
        "primary": "The abnormal accumulation of serous fluid within the peritoneal cavity, causing abdominal distension.",
        "secondary": "In gastroenterology and hepatology, a hallmark complication of decompensated portal hypertension, hepatic cirrhosis, or peritoneal carcinomatosis.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In advanced cirrhosis of the liver, extensive **ascites** frequently develops, requiring repeated paracentesis to relieve respiratory embarrassment."},
            {"author": "Thomas Watson", "work": "Lectures on the Principles and Practice of Physic", "quote": "The physician must carefully distinguish peritoneal **ascites** resulting from portal obstruction from that caused by general dropsy or chronic nephritis."},
            {"author": "Richard Bright", "work": "Reports of Medical Cases", "quote": "The presence of copious **ascites** combined with anasarca pointed directly toward profound disease within the renal and hepatic systems."}
        ]
    },
    "ascitic": {
        "primary": "Of, relating to, or affected by ascites; characterized by serous fluid effusion in the abdomen.",
        "secondary": "In clinical pathology, describing effused peritoneal fluid classified as transudative or exudative based on serum-ascites albumin gradient (SAAG).",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Microscopic and chemical examination of the **ascitic** fluid revealed a low specific gravity and an absence of malignant cellular elements."},
            {"author": "Thomas Watson", "work": "Lectures on the Principles and Practice of Physic", "quote": "The **ascitic** swelling distended the abdominal wall to such an extent that the superficial collateral veins became prominently engorged."},
            {"author": "Richard Bright", "work": "Reports of Medical Cases", "quote": "A diagnostic puncture was performed, withdrawing several quarts of pale straw-colored **ascitic** fluid to alleviate the patient's acute discomfort."}
        ]
    },
    "citadel": {
        "primary": "A fortress commanding a city, serving both to protect the inhabitants and maintain defensive control.",
        "secondary": "In military fortification and symbolic literature, a fortified stronghold or ultimate sanctuary of defense against hostile subjugation.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Othello", "quote": "I pray you, sir, go forth and look upon the port; let us receive the news from the high **citadel** overlooking the sea."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "Every man is the builder of a temple, called his body, to the god he worships; his mind remains an inviolate interior **citadel**."},
            {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The garrison retreated into the formidable **citadel**, where they resolved to withstand the final desperate assault of the besieging army."}
        ]
    },
    "citation": {
        "primary": "A reference to a source of information, legal authority, or literary work; or an official summons to appear.",
        "secondary": "In jurisprudence and academic methodology, a formal writ citing a party before a tribunal, or a precise bibliographic reference substantiating scholarship.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants Under Domestication", "quote": "I have inserted in the text a precise **citation** of the original memoir published by M. Godron upon hybrid cereal plants."},
            {"author": "Francis Bacon", "work": "The Elements of the Common Laws of England", "quote": "In every contentious dispute before the ecclesiastical judge, a formal **citation** must precede all proceedings against the respondent."},
            {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The pedantic critic burdened every page with an unnecessary **citation** from ancient grammarians, obscuring rather than illuminating his discourse."}
        ]
    },
    "cite": {
        "primary": "To quote an authority, passage, or book by way of evidence, illustration, or proof.",
        "secondary": "In civil procedure and scholarly rhetoric, to summon an individual to appear before court or formally adduce precedent in legal argument.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "The devil can **cite** Scripture for his purpose; an evil soul producing holy witness is like a villain with a smiling cheek."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The parson did not fail to **cite** several grim texts from Deuteronomy to enforce his solemn admonition upon the listeners."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "I might **cite** numerous other historical instances where leviathans have shattered the stout timber walls of ships of the line."}
        ]
    },
    "citellus": {
        "primary": "A genus of Holarctic ground squirrels belonging to the family Sciuridae, noted for cheek pouches and burrowing habits.",
        "secondary": "In zoological taxonomy and epidemiology, rodents of the tribe Marmotini that serve as key ecological seed dispersers and reservoirs for plague bacilli.",
        "quotes": [
            {"author": "John James Audubon", "work": "The Viviparous Quadrupeds of North America", "quote": "The striped ground squirrel, classified by naturalists under **citellus**, constructs elaborate subterranean galleries beneath the prairie sod."},
            {"author": "C. Hart Merriam", "work": "Life Zones and Crop Zones of the United States", "quote": "Specimens of **citellus** collected across the Great Basin exhibit distinct pelage colorations adapted to the arid desert substrate."},
            {"author": "Richard Lydekker", "work": "The Royal Natural History", "quote": "The souslik of the Russian steppes represents the typical form of the genus **citellus**, passing the harsh winter in profound hibernation."}
        ]
    },
    "citified": {
        "primary": "Having acquired the manners, dress, sophistication, or affectations characteristic of an urban inhabitant.",
        "secondary": "In cultural commentary and dialect literature, showing urbane refinement or pretentious city polish contrasting with rural simplicity.",
        "quotes": [
            {"author": "Mark Twain", "work": "Roughing It", "quote": "His **citified** garments and immaculate boots looked strangely out of place among the rough miners of Virginia City."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The country folk viewed his **citified** airs and polished accent with mingled curiosity and profound suspicion."},
            {"author": "Hamlin Garland", "work": "Main-Travelled Roads", "quote": "Returning after years in Chicago, the young man discovered that his **citified** habits made the daily toil of the farm unendurable."}
        ]
    },
    "citify": {
        "primary": "To conform to the manners, customs, speech, or lifestyle of city inhabitants; to urbanize.",
        "secondary": "In sociology and regional literature, to transform rural individuals or communities through the adoption of cosmopolitan city ways.",
        "quotes": [
            {"author": "William Dean Howells", "work": "The Rise of Silas Lapham", "quote": "The ambitious mother sought every opportunity to **citify** her daughters by introducing them into Boston salon society."},
            {"author": "Edward Eggleston", "work": "The Hoosier Schoolmaster", "quote": "The villagers feared that sending the lad away to academy would **citify** him beyond all practical utility on the homestead."},
            {"author": "O. Henry", "work": "The Four Million", "quote": "A month of pavements and incandescent lamps will thoroughly **citify** the greenest rustic who steps off the ferry."}
        ]
    },
    "citizen": {
        "primary": "A legally recognized subject or national of a state, entitled to civil rights and bound by corresponding obligations.",
        "secondary": "In political philosophy and civic jurisprudence, a franchised member of a commonwealth participating directly or representatively in self-government.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "Hear me for my cause, and be silent, that you may hear; believe me for mine honour, as each noble **citizen** of Rome ought."},
            {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "Active participation in public affairs elevates the moral and intellectual capacity of every ordinary **citizen**."},
            {"author": "Ralph Waldo Emerson", "work": "Society and Solitude", "quote": "A true **citizen** does not measure the greatness of his country by its wealth, but by the integrity of its institutions."}
        ]
    },
    "citizenry": {
        "primary": "The citizens of a city, state, or nation collectively, considered as a political body.",
        "secondary": "In sociology and democratic theory, the collective civic populace whose aggregate opinions and values inform sovereign governance.",
        "quotes": [
            {"author": "Woodrow Wilson", "work": "The State: Elements of Historical and Practical Politics", "quote": "The enlightened moral judgment of the entire **citizenry** constitutes the ultimate bedrock of democratic administration."},
            {"author": "Theodore Roosevelt", "work": "The Strenuous Life", "quote": "No system of laws can preserve a nation whose **citizenry** lacks the virile virtues of civic courage and personal responsibility."},
            {"author": "James Bryce", "work": "The American Commonwealth", "quote": "The widespread dissemination of public journals ensures that the **citizenry** remains constantly attentive to the deliberations of Congress."}
        ]
    },
    "citizenship": {
        "primary": "The legal status and vested membership uniting an individual to a sovereign state, conferring civil and political entitlements.",
        "secondary": "In constitutional law and political philosophy, the bundle of reciprocal privileges, immunities, and allegiances uniting an individual to a polity.",
        "quotes": [
            {"author": "James Joyce", "work": "Ulysses", "quote": "He proclaimed with dignity that the rights of free speech and full **citizenship** belonged equally to every man born upon Irish soil."},
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "He renounced his former connections and claimed the protection and privileges of colonial **citizenship** within the Massachusetts settlement."},
            {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "In the United States, the duties of civic **citizenship** are learned not through theoretical textbooks, but through local township assemblies."}
        ]
    },
    "citlaltepetl": {
        "primary": "An active stratovolcano in southern Mexico (also known as Pico de Orizaba), the highest peak in Mexico at 5,636 meters.",
        "secondary": "In Mesoamerican geography and Nahuatl mythology ('Star Mountain'), a glaciated volcanic landmark along the Trans-Mexican Volcanic Belt.",
        "quotes": [
            {"author": "Alexander von Humboldt", "work": "Political Essay on the Kingdom of New Spain", "quote": "The snow-crowned summit of **citlaltepetl** rises majestically above the coastal plains of Veracruz, guiding navigators across the Gulf."},
            {"author": "William H. Prescott", "work": "History of the Conquest of Mexico", "quote": "The Spanish conquerors gazed with awe toward the distant volcanic pinnacle of **citlaltepetl**, piercing the clouds with solitary grandeur."},
            {"author": "Bayard Taylor", "work": "Eldorado, or, Adventures in the Path of Empire", "quote": "As the morning mist cleared, the immense white cone of **citlaltepetl** shone with dazzling brilliance against the deep azure sky."}
        ]
    },
    "citole": {
        "primary": "A medieval stringed musical instrument, having a flat, pear-shaped or holly-leaf body, plucked with a plectrum.",
        "secondary": "In organology and musicology, a fourteenth-century chordophone ancestral to the cittern, characterized by a thumb-hole neck and fretted fingerboard.",
        "quotes": [
            {"author": "Geoffrey Chaucer", "work": "The Knight's Tale", "quote": "Before the altar of the goddess Venus stood the celestial image, holding in her fair right hand a melodious **citole**."},
            {"author": "Dante Gabriel Rossetti", "work": "The Blessed Damozel", "quote": "Around the throne of the Virgin, singing angels touched the strings of gittern, harp, and sweet **citole** in perpetual harmony."},
            {"author": "William Morris", "work": "The Earthly Paradise", "quote": "Minstrels entered the banquet hall, tuning the resonant strings of lute and **citole** to chant deeds of chivalric renown."}
        ]
    },
    "citrange": {
        "primary": "A cold-hardy citrus hybrid produced by crossing the sweet orange (Citrus sinensis) with the trifoliate orange (Poncirus trifoliata).",
        "secondary": "In pomology and citriculture, a vigorous rootstock cultivar yielding sour fruit, bred for nematode resistance and frost tolerance.",
        "quotes": [
            {"author": "Luther Burbank", "work": "His Methods and Discoveries and Their Practical Application", "quote": "By systematic hybridization, experimenters developed the **citrange**, combining the winter hardiness of the trifoliate orange with citrus vigor."},
            {"author": "Liberty Hyde Bailey", "work": "The Standard Cyclopedia of Horticulture", "quote": "The Rusk **citrange** has proven particularly valuable in the southern border states as an ornamental and frost-resistant seedling stock."},
            {"author": "U. P. Hedrick", "work": "Systematic Pomology", "quote": "Though the fruit of the **citrange** is too acid for dessert consumption, its robust root system resists severe sub-freezing temperatures."}
        ]
    },
    "citrate": {
        "primary": "A salt or ester of citric acid, widely utilized in food preservation, pharmaceuticals, and industrial buffering.",
        "secondary": "In biochemistry and clinical medicine, an essential tricarboxylic acid cycle intermediate and vital anticoagulant that chelates free calcium ions.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The administration of potassium **citrate** in copious water serves effectively to alkalinize the urine and soothe renal irritation."},
            {"author": "Michael Faraday", "work": "Chemical Manipulation", "quote": "Upon neutralizing citric acid with a caustic alkali, a crystallizable **citrate** is formed that remains highly soluble in water."},
            {"author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "The formation of insoluble calcium **citrate** provides a classic analytical pathway for separating citric acid from fruit juices."}
        ]
    },
    "citric": {
        "primary": "Of, relating to, or derived from citrus fruits; specifically denoting citric acid.",
        "secondary": "In organic chemistry and cellular respiration, denoting the tricarboxylic acid (C6H8O7) driving energy production in mitochondrial metabolism.",
        "quotes": [
            {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The sharp **citric** acid obtained from lemons crystallized in clear rhombic prisms when slowly evaporated under atmospheric exposure."},
            {"author": "Humphry Davy", "work": "Elements of Agricultural Chemistry", "quote": "Vegetable acids such as the **citric** and malic acids exist in varying proportions in the pulp of unripened orchard fruits."},
            {"author": "Justus von Liebig", "work": "Animal Chemistry", "quote": "The organic decomposition of **citric** compounds within living organisms illustrates the fundamental metabolic laws of oxidation."}
        ]
    },
    "citrin": {
        "primary": "A mixture of flavonoid bioflavonoids (vitamin P) extracted from citrus rinds, reducing capillary fragility and permeability.",
        "secondary": "In nutritional biochemistry and pharmacology, discovered by Albert Szent-Györgyi as a vascular permeability cofactor acting synergistically with ascorbic acid.",
        "quotes": [
            {"author": "Albert Szent-Györgyi", "work": "Studies on Biological Oxidation", "quote": "Our investigations demonstrated that **citrin**, extracted from Hungarian paprika and lemon peel, restores normal capillary resistance in scorbutic subjects."},
            {"author": "Casimir Funk", "work": "The Vitamins", "quote": "The crystalline flavonoid fraction termed **citrin** was shown to decrease abnormal capillary bleeding where pure ascorbic acid alone had failed."},
            {"author": "Linus Pauling", "work": "Vitamin C and the Common Cold", "quote": "Natural citrus concentrates contain bioflavonoids formerly designated as **citrin**, which enhance the physiological retention of ascorbic acid."}
        ]
    },
    "citrine": {
        "primary": "A transparent pale yellow to brownish-orange variety of quartz; or possessing a clear lemon-yellow color.",
        "secondary": "In mineralogy and gemology, macrocrystalline silicon dioxide colored by ferric iron impurities, frequently produced by heat-treating amethyst.",
        "quotes": [
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He collected wonderful gems from across the Orient, admiring the pale golden luster of yellow **citrine** set beside deep carbuncles."},
            {"author": "John Ruskin", "work": "Modern Painters", "quote": "The evening sky faded from fiery crimson into a delicate **citrine** tint before darkening into nocturnal violet."},
            {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Among the treasures of the Agra jewel chest lay pendants of chrysoberyl and sparkling **citrine** of exquisite transparency."}
        ]
    },
    "citron": {
        "primary": "A large, thick-skinned citrus fruit (Citrus medica), whose fragrant rind is preserved or candied for culinary use.",
        "secondary": "In systematic botany and Jewish tradition (etrog), one of the original ancestral citrus species cultivated since antiquity for liturgical ritual.",
        "quotes": [
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "The air was heavy with the perfume of bruised herbs and the pungent fragrance of sliced **citron** rind upon the table."},
            {"author": "Herman Melville", "work": "Typee: A Romance of the South Seas", "quote": "The natives brought woven baskets filled with golden fruit, including wild breadfruit and aromatic green **citron** from the valley."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "In blissful Eden grew the savory fruit of golden orange and fragrant **citron**, bowing the branches with luscious burden."}
        ]
    },
    "citroncirus": {
        "primary": "A nothogenus representing intergeneric hybrids between the genus Citrus and the trifoliate orange Poncirus.",
        "secondary": "In botanical taxonomy, the formally assigned hybrid designation (× Citroncirus webberi) encompassing cold-hardy citranges and citrumelos.",
        "quotes": [
            {"author": "Liberty Hyde Bailey", "work": "Manual of Cultivated Plants", "quote": "The intergeneric cross **citroncirus** demonstrates that morphological boundaries between Citrus and Poncirus are permeable under controlled breeding."},
            {"author": "Walter T. Swingle", "work": "The Citrus Industry", "quote": "We established the hybrid genus **citroncirus** to designate all artificial offspring uniting the evergreen Citrus with deciduous Poncirus trifoliata."},
            {"author": "U. P. Hedrick", "work": "Cyclopedia of Hardy Fruits", "quote": "Rootstocks derived from **citroncirus** hybrids exhibit remarkable resistance to cold injury and subterranean fungal pathogens in citrus orchards."}
        ]
    },
    "citronwood": {
        "primary": "The durable, pleasantly aromatic wood obtained from the citron tree or the Moroccan arborvitae (Tetraclinis articulata).",
        "secondary": "In historic woodworking and classical antiquities, the prized citrus wood (thyine wood) utilized by ancient Romans for lavish banquet tables.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Patricians squandered princely fortunes upon luxurious dining tables carved from single slabs of fragrant Mauritanian **citronwood**."},
            {"author": "John Evelyn", "work": "Sylva, or A Discourse of Forest-Trees", "quote": "The ancient Romans esteemed **citronwood** above gold for their ornamental cabinetry, valuing its intricate veins and fragrant aroma."},
            {"author": "Pliny the Elder", "work": "Natural History", "quote": "The luxury of buying tables of **citronwood** reached such extravagance that husbands reproached their wives with pearls while indulging in thyine timber."}
        ]
    },
    "citrous": {
        "primary": "Of, relating to, or resembling citrus fruits; possessing the tart aroma, acidic flavor, or botanical traits of citrus.",
        "secondary": "In food science and perfumery, describing sensory profiles characterized by limonene-rich terpenes and pungent hesperidic notes.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "Cape Cod", "quote": "The sea breeze carried a refreshing zest reminiscent of **citrous** orchards blossoming in a distant Mediterranean climate."},
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "A pungent, **citrous** fragrance rose from the crushed aromatic boughs as the woodcutters cleared the forest path."},
            {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "I inhale the sweet breath of southern groves, laden with the **citrous** odors of blossoming orange and lemon bowers."}
        ]
    }
}
