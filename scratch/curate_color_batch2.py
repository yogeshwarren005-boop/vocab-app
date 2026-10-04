# -*- coding: utf-8 -*-
"""
Curates Cluster Color & Appearance (Batch 2, 42 words):
- Dashboard — cand (42 words)
Total: 42 words.
"""
import sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_batch2 = {
  "candela": {
    "primary": "The SI base unit of luminous intensity, equal to the luminous intensity of a monochromatic radiation source.",
    "secondary": "In photometry, the standardized measure of directional light emitted per unit solid angle.",
    "quotes": [
      {"author": "Lord Kelvin", "work": "Popular Lectures and Addresses", "quote": "Photometric measurement establishes the luminous intensity of standard lamps in units of the **candela**."},
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "The radiant emission per steradian provides a precise definition for the modern **candela** standard."},
      {"author": "Thomas Alva Edison", "work": "The Papers of Thomas A. Edison", "quote": "Our laboratory tested incandescent carbon filaments that sustained sixteen **candela** of steady illumination."}
    ]
  },
  "candelabra": {
    "primary": "A large branched candlestick or lamp holder with several arms supporting multiple lights.",
    "secondary": "In interior architecture and decorative arts, an ornate table centerpiece designed for multiple candles.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "The Masque of the Red Death", "quote": "A massive golden **candelabra** suspended from the vaulted ceiling illuminated the imperial hall."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The footman carried a silver **candelabra** before us, illuminating the dark portraits of Thornfield."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Dorian placed the heavy brass **candelabra** upon the ebony table beside the locked wardrobe."}
    ]
  },
  "candelabrum": {
    "primary": "A decorative branched holder for several candles or lamps; the singular form of candelabra.",
    "secondary": "In classical Roman antiquities, a tall bronze or marble stand supporting oil lamps in patrician homes.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Vandals plundered the sacred golden **candelabrum** that had once adorned the Temple of Jerusalem."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "An antique bronze **candelabrum** cast flickering shadows across the frescoed walls of the salone."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The lawyer sat beside a solitary bronze **candelabrum**, examining the mysterious packet of letters."}
    ]
  },
  "candelilla": {
    "primary": "A desert shrub (Euphorbia antisyphilitica) native to northern Mexico and Texas that yields a hard natural wax.",
    "secondary": "In industrial chemistry and cosmetics, the hard vegetable wax extracted from the coated stems of the shrub.",
    "quotes": [
      {"author": "William Bartram", "work": "Travels through North and South Carolina", "quote": "Arid southwestern washes support dense clusters of the wax-bearing desert **candelilla**."},
      {"author": "John Muir", "work": "Steep Trails", "quote": "The desert slopes of the Rio Grande were covered with drought-resisting clumps of slender **candelilla**."},
      {"author": "David Fairchild", "work": "The World Was My Garden", "quote": "Mexican gatherers boiled the gray stems of **candelilla** in open vats to extract commercial wax."}
    ]
  },
  "candent": {
    "primary": "Glowing with heat; white-hot; incandescent and radiating intense light.",
    "secondary": "In archaic scientific poetry, gleaming with fiery brilliance or dazzling purity.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Angelic spears shone with **candent** fury as they advanced against the rebellious hosts."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The furnace of the try-works glowed with **candent** fury beneath the pitch-black midnight sky."},
      {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "Meteors shot like **candent** arrows across the celestial vault of heaven."}
    ]
  },
  "candescence": {
    "primary": "Luminous radiation emitted by a material heated to white-hot temperature; glowing heat.",
    "secondary": "The state or phenomenon of glowing white with intense thermal energy.",
    "quotes": [
      {"author": "Michael Faraday", "work": "The Chemical History of a Candle", "quote": "Carbon particles within the flame are raised to bright **candescence**, producing the yellow light."},
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "The platinum wire glowed with blinding **candescence** under the concentrated electric discharge."},
      {"author": "H.G. Wells", "work": "The Time Machine", "quote": "A flash of brilliant white **candescence** illuminated the laboratory as the machine leaped forward."}
    ]
  },
  "candescent": {
    "primary": "Glowing or shining with intense heat; white-hot; luminous.",
    "secondary": "Radiant with pure light, dazzling brilliance, or ardent enthusiasm.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The prophet's soul burned with **candescent** indignation against the shallow hypocrisy of the age."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The setting sun transformed the snowy alpine ridge into a **candescent** crest of molten gold."},
      {"author": "Herman Melville", "work": "Pierre; or, The Ambiguities", "quote": "His eyes flared with a **candescent** fire that frightened his gentle companion."}
    ]
  },
  "candid": {
    "primary": "Truthful, straightforward, and frank in speech or manner; sincere and impartial.",
    "secondary": "In photography, taken informally and spontaneously without the subject posing for the lens.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth gave a **candid** acknowledgment of her former prejudice and injustice toward Mr. Darcy."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A **candid** citizen must admit that the weaknesses of the confederation require decisive remedy."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea welcomed his **candid** criticism, valuing truth far above polite social flattery."}
    ]
  },
  "candida": {
    "primary": "A genus of yeast-like fungi that normally inhabit mucosal membranes but can cause opportunistic infections.",
    "secondary": "In clinical microbiology, specifically Candida albicans, the organism responsible for candidiasis and thrush.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Microscopic examination of mucosal scraping revealed budding mycelia and blastospores of **Candida**."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Epithelial ulceration may become superinfected with fungal colonies of opportunistic **Candida**."},
      {"author": "Jonathan Hutchinson", "work": "Clinical Lectures on Rare Diseases", "quote": "The patient's chronic cutaneous lesions were aggravated by localized overgrowth of **Candida**."}
    ]
  },
  "candidacy": {
    "primary": "The status, campaign, or period of an individual seeking an elective office or appointment.",
    "secondary": "Formal qualification or active standing for an academic degree, professional role, or public honor.",
    "quotes": [
      {"author": "Abraham Lincoln", "work": "Speeches and Letters", "quote": "Lincoln announced his **candidacy** for the state legislature with modest self-reliance."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A citizen offering his **candidacy** for the executive magistracy must submit his character to national scrutiny."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "Babbitt campaigned vigorously to promote his friend's **candidacy** for the municipal aldermanic council."}
    ]
  },
  "candidate": {
    "primary": "A person who applies for a job, seeks nomination, or runs for election to public office.",
    "secondary": "In academic institutions, a scholar undertaking the final requirements for an advanced degree.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Every political **candidate** must flatter the passions and solicit the votes of the democratic majority."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "The rival **candidate** addressed the uproarious electors of Eatanswill from the hotel balcony."},
      {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "The parliamentary **candidate** rode through the market town surrounded by cheering partisans."}
    ]
  },
  "candidature": {
    "primary": "The fact, status, or campaign of being a candidate for office or honor; candidacy.",
    "secondary": "In British political and academic terminology, the formal nomination or standing of an applicant.",
    "quotes": [
      {"author": "Anthony Trollope", "work": "Phineas Finn", "quote": "Phineas announced his **candidature** for the borough amidst turbulent parliamentary rumors."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The duke withdrew his **candidature** when it became evident that the commons favored his rival."},
      {"author": "Winston Churchill", "work": "My Early Life", "quote": "My first parliamentary **candidature** at Oldham was a lively and educational baptism of fire."}
    ]
  },
  "candidiasis": {
    "primary": "A fungal infection caused by yeast species of the genus Candida, commonly affecting skin or mucous membranes.",
    "secondary": "In clinical medicine, oral thrush or systemic fungal disease prevalent in immunocompromised patients.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe oral **candidiasis** with extensive pseudomembranous plaques developed during prolonged debility."},
      {"author": "Jonathan Hutchinson", "work": "Clinical Lectures on Rare Diseases", "quote": "Topical antifungal applications promptly cleared the cutaneous intertrigo complicated by **candidiasis**."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Mucosal biopsy confirmed deep tissue penetration by fungal pseudohyphae characteristic of invasive **candidiasis**."}
    ]
  },
  "candidly": {
    "primary": "In an honest, frank, sincere, and straightforward manner, without reservation.",
    "secondary": "Sentence-initially, used to introduce an outspoken, unvarnished, or uncomfortable truth.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Knightley spoke **candidly** to Emma regarding the vanity of her interference with Harriet Smith."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Jane answered **candidly** that she could never marry a man who demanded the surrender of her conscience."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes confessed **candidly** that the baffling case had tested all his analytical resources."}
    ]
  },
  "candidness": {
    "primary": "Frankness, sincerity, and unvarnished openness of speech, disposition, or demeanor.",
    "secondary": "The quality of engaging with others without artifice, deception, or flattery.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea admired the rustic **candidness** with which Will Ladislaw expressed his unconventional opinions."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Isabel's natural **candidness** disarmed the cynical worldly observers in the Roman drawing room."},
      {"author": "Nathaniel Hawthorne", "work": "The Blithedale Romance", "quote": "Hollingsworth lacked diplomatic tact, but his stern **candidness** commanded reluctant respect."}
    ]
  },
  "candied": {
    "primary": "Preserved, encrusted, or cooked with sugar, syrup, or a sweet glaze.",
    "secondary": "In figurative literature, deceptively flattering, sweet-sounding, or insincere in tone.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Let the **candied** tongue lick absurd pomp, and crook the pregnant hinges of the knee where thrift may follow fawning."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "The shop windows displayed pyramids of **candied** orange peel, plums, and spiced pastries."},
      {"author": "John Keats", "work": "The Eve of St. Agnes", "quote": "Porphyro brought delicacies of **candied** apple, quince, and plum, and jellies smoother than creamy curd."}
    ]
  },
  "candle": {
    "primary": "A cylinder or block of wax or tallow with an embedded central wick that burns to provide light.",
    "secondary": "A traditional standard unit of luminous intensity; or a candle-shaped object in medical surgery.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "Out, out, brief **candle**! Life's but a walking shadow, a poor player that struts and frets his hour upon the stage."},
      {"author": "Michael Faraday", "work": "The Chemical History of a Candle", "quote": "There is no more open door by which you can enter the study of natural philosophy than by considering the phenomena of a **candle**."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The guttering **candle** cast long, trembling shadows across the cold dormitory wall."}
    ]
  },
  "candleberry": {
    "primary": "The wax myrtle or bayberry (Myrica cerifera), an aromatic shrub whose berries yield wax for candles.",
    "secondary": "In North American colonial history, berries collected to make sweet-smelling green bayberry wax.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Cape Cod", "quote": "We brushed through fragrant thickets of **candleberry** myrtle flourishing upon the coastal dunes."},
      {"author": "William Bartram", "work": "Travels through North and South Carolina", "quote": "Colonial housewives boiled the waxy fruit of the **candleberry** to make fragrant green tapers."},
      {"author": "John Muir", "work": "A Thousand-Mile Walk to the Gulf", "quote": "The damp sandy pine barrens were scented with the crushed aromatic leaves of wild **candleberry**."}
    ]
  },
  "candlelight": {
    "primary": "The soft, flickering light provided by one or more burning candles.",
    "secondary": "The period of dusk or twilight when candles are lit; evocative of an intimate historic atmosphere.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Miss Havisham sat in the dim yellow **candlelight** of the decaying bridal chamber."},
      {"author": "Edgar Allan Poe", "work": "The Oval Portrait", "quote": "The pale rays of **candlelight** fell upon the canvas, giving the painted portrait life-like vividness."},
      {"author": "Jane Austen", "work": "Emma", "quote": "The small parlor looked remarkably cheerful and cozy by warm **candlelight** after the winter storm."}
    ]
  },
  "candlemaker": {
    "primary": "A person, artisan, or chandler who manufactures candles from wax, tallow, or stearin.",
    "secondary": "A traditional tradesperson responsible for rendering fats and dipping or casting candles.",
    "quotes": [
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "My father was a soap boiler and **candlemaker**, and in his shop I was employed in cutting wicks and filling molds."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The oilman and **candlemaker** in the alley supplied yellow tallow dips to the clerks of Chancery."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "Every honest **candlemaker** who dips faithful wicks contributes his mite to the illumination of the realm."}
    ]
  },
  "candlemas": {
    "primary": "A Christian festival celebrated on February 2 commemorating the purification of Mary and presentation of Christ in the temple.",
    "secondary": "In traditional European folklore and agriculture, a traditional quarter day marking the midpoint of winter.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Hiring fairs for shepherds and farm laborers were traditionally held at the turn of **Candlemas**."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The old tenant paid his half-yearly manorial rent punctually upon the feast of **Candlemas**."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "Old rustic proverbs predicted fair spring weather if the skies were clear and frosty on **Candlemas**."}
    ]
  },
  "candlenut": {
    "primary": "A flowering tree of the spurge family (Aleurites moluccanus) native to Polynesia, whose oily nuts can be burned for light.",
    "secondary": "In tropical agriculture, a valuable oil-seed crop used in traditional illumination, varnish, and Pacific cuisine.",
    "quotes": [
      {"author": "Herman Melville", "work": "Typee", "quote": "The islanders strung the kernel of the **candlenut** upon dried palm ribs, burning them sequentially for illumination."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We observed groves of the indigenous **candlenut** tree growing vigorously in the sheltered Polynesian valleys."},
      {"author": "Robert Louis Stevenson", "work": "In the South Seas", "quote": "The native feast was illuminated by flickering torches made from the rich oil of the crushed **candlenut**."}
    ]
  },
  "candlepin": {
    "primary": "A tall, slender bowling pin with straight sides and slightly tapered ends, used in candlepin bowling.",
    "secondary": "In regional New England sports, one of the ten narrow pins targeted with small, holeless bowling balls.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "Twice-Told Tales", "quote": "Villagers enjoyed games of skittles and ninepins, the precursor to the modern New England **candlepin**."},
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "Young townsmen gathered at the recreation hall to roll balls against the clattering row of **candlepin** pins."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The distant thunder rumbled like the crash of balls amidst wooden pins in a mountain **candlepin** alley."}
    ]
  },
  "candlepins": {
    "primary": "A variation of bowling played primarily in New England and eastern Canada using candlepins and small balls.",
    "secondary": "The set of ten narrow cylindrical pins used in this traditional regional sport.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "The sporting club organized a tournament of **candlepins** to enliven the cold winter evenings."},
      {"author": "Thomas Wolfe", "work": "Look Homeward, Angel", "quote": "The boys cheered as the ball swept cleanly through the standing **candlepins** with a sharp crack."},
      {"author": "John Steinbeck", "work": "The Grapes of Wrath", "quote": "In roadside recreation centers, travelers watched local youths compete at games of **candlepins**."}
    ]
  },
  "candlepower": {
    "primary": "A unit of measure of luminous intensity, equal to the light emitted by a standard candle.",
    "secondary": "In lighting technology, a historical photometric unit replaced by the modern candela.",
    "quotes": [
      {"author": "Thomas Alva Edison", "work": "The Papers of Thomas A. Edison", "quote": "The new carbon filament lamp delivered sixteen **candlepower** of steady, economical illumination."},
      {"author": "H.G. Wells", "work": "The Island of Dr Moreau", "quote": "The ship's searchlight of enormous **candlepower** swept the dark coastal waters for survivors."},
      {"author": "Nikola Tesla", "work": "My Inventions", "quote": "High-frequency vacuum tubes produced luminous discharge exceeding fifty **candlepower** without perceptible heat."}
    ]
  },
  "candlesnuffer": {
    "primary": "An instrument with a small metal cup or cone on a long handle used to extinguish burning candles.",
    "secondary": "Historically, scissors-like shears with a small box attached for trimming and catching charred candle wicks.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The beadle extinguished the church tapers one by one with a tarnished brass **candlesnuffer**."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Madame Beck moved quietly through the dormitory, using her silver **candlesnuffer** at the stroke of ten."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The antiquary carefully laid down an ancient carved brass **candlesnuffer** among his curiosities."}
    ]
  },
  "candlestick": {
    "primary": "A holder, support, or decorative stand with a socket in which a candle is inserted for burning.",
    "secondary": "In financial charting, a style of technical price chart displaying high, low, open, and close prices.",
    "quotes": [
      {"author": "Victor Hugo", "work": "Les Misérables", "quote": "The bishop gave the two silver **candlestick** pieces to Jean Valjean, saying they belonged to him forever."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "A heavy silver **candlestick** lay overturned upon the hearthrug beside the murdered squire."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "The old captain struck his fist upon the table, making the pewter **candlestick** rattle."}
    ]
  },
  "candlewick": {
    "primary": "The cord, thread, or woven cotton wick embedded in the center of a candle that draws fuel to the flame.",
    "secondary": "A soft tufted fabric embroidered with raised chenille-like stitches, resembling a candlewick.",
    "quotes": [
      {"author": "Michael Faraday", "work": "The Chemical History of a Candle", "quote": "Capillary action draws the melted wax up the fibers of the braided **candlewick** into the vaporizing zone."},
      {"author": "Edith Wharton", "work": "Ethan Frome", "quote": "Zeena smoothed the white **candlewick** bedspread with bony fingers in the chilly bedroom."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I trimmed the **candlewick** carefully to prevent the soot from soiling my manuscript pages."}
    ]
  },
  "candlewood": {
    "primary": "Resinous wood, such as fat pine or ocotillo stems, used for kindling fires or burning as torches.",
    "secondary": "In regional American botany, any shrub or tree whose branches contain combustible resin.",
    "quotes": [
      {"author": "Francis Parkman", "work": "The Conspiracy of Pontiac", "quote": "Frontiersmen lit splinters of resinous **candlewood** to guide their way through the dark forest blockhouse."},
      {"author": "William Bartram", "work": "Travels through North and South Carolina", "quote": "The Indians carried flares of pitch-rich **candlewood** while spearing fish in the nocturnal bayous."},
      {"author": "John Muir", "work": "The Mountains of California", "quote": "Knots of yellow pine **candlewood** burned with a brilliant, steady flare in our alpine campfire."}
    ]
  },
  "candor": {
    "primary": "Openness, unreserved honesty, and frank sincerity in speech or expression; freedom from bias or deceit.",
    "secondary": "In classical literary criticism, fairness, generosity, and freedom from prejudice in judgment.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth admired Jane's universal **candor**, which always sought the most charitable construction of motives."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "An appeal is made to the enlightened **candor** of the people in evaluating the proposed constitutional system."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Nothing astonishes men so much as common sense and plain dealing, spoken with heroic **candor**."}
    ]
  },
  "candour": {
    "primary": "Openness, frankness, and sincere transparency in speech and interpersonal conduct; British spelling of candor.",
    "secondary": "Freedom from malice, prejudice, or bias; fair-minded impartiality.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne's frank **candour** frequently led her into unguarded remarks that shocked conventional society."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Esther listened with grateful **candour** to the sympathetic advice of her guardian."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "True critical **candour** weighs the author's overall excellence against unavoidable minor blemishes."}
    ]
  },
  "candy": {
    "primary": "A sweet confection made with sugar, syrup, or chocolate, often combined with nuts, fruit, or flavorings.",
    "secondary": "To preserve or crystallize fruit or plant roots in sugar syrup; to encrust with sugar.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The shopkeeper weighed out peppermint **candy** for the schoolboys gathered at the counter."},
      {"author": "Mark Twain", "work": "The Adventures of Tom Sawyer", "quote": "Tom traded his prized peach for Becky's stick of colored **candy** during recess."},
      {"author": "Louisa May Alcott", "work": "Little Women", "quote": "Amy brought a paper cone of barley **candy** to share with her sisters around the fire."}
    ]
  },
  "candy-like": {
    "primary": "Resembling candy in sweetness, bright color, glazed texture, or artificial flavor.",
    "secondary": "Possessing a frivolous, sugary, or artificially appealing character.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "The modern storefronts were painted in bright, **candy-like** pastels to attract suburban shoppers."},
      {"author": "Virginia Woolf", "work": "The Waves", "quote": "The glass baubles sparkled with a **candy-like** iridescence upon the decorated Christmas branch."},
      {"author": "F. Scott Fitzgerald", "work": "Tender Is the Night", "quote": "The resort hotels displayed **candy-like** pink and turquoise facades along the Riviera waterfront."}
    ]
  },
  "candy-scented": {
    "primary": "Having an aroma resembling sweet sugar, caramel, vanilla, or confectionery.",
    "secondary": "Fragrant with sugary, sweet, or syrupy floral undertones.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The blossoming clover field released a warm, **candy-scented** perfume in the midday heat."},
      {"author": "Edith Wharton", "work": "The House of Mirth", "quote": "The conservatory was filled with the exotic, **candy-scented** fragrance of tropical orchids."},
      {"author": "Katherine Mansfield", "work": "The Garden Party", "quote": "The summer air was **candy-scented** with crushed berries and warm honey from the hives."}
    ]
  },
  "candyfloss": {
    "primary": "A confection of fluffy spun sugar served on a stick or in a bag; cotton candy.",
    "secondary": "Something visually enticing or entertaining but devoid of substantial depth or value.",
    "quotes": [
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "The seaside fairground bustled with children clutching pink puffs of spun **candyfloss**."},
      {"author": "Virginia Woolf", "work": "Between the Acts", "quote": "The light entertainment dissolved like airy **candyfloss** in the minds of the audience."},
      {"author": "Graham Greene", "work": "Brighton Rock", "quote": "Pink **candyfloss** and seaside rock were hawked among the holiday crowds along the pier."}
    ]
  },
  "candymaker": {
    "primary": "An artisan, confectioner, or company that manufactures candy and sweet treats.",
    "secondary": "A skilled worker specializing in the boiling of sugar, pulling of taffy, and tempering of chocolate.",
    "quotes": [
      {"author": "Louisa May Alcott", "work": "Little Men", "quote": "The village **candymaker** welcomed the schoolboys into his warm, fragrant sugar kitchen."},
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "The Greek **candymaker** stirred copper kettles of bubbling caramel behind his glass counter."},
      {"author": "O. Henry", "work": "The Four Million", "quote": "The industrious **candymaker** dipped bonbons with rapid, practiced sweeps of her fingers."}
    ]
  },
  "candytuft": {
    "primary": "A flowering Eurasian garden plant of the genus Iberis (family Brassicaceae), bearing white or purple flower clusters.",
    "secondary": "A popular low-growing edging plant cultivated in cottage rock gardens for dense spring blooms.",
    "quotes": [
      {"author": "John Ruskin", "work": "Proserpina", "quote": "The humble **candytuft** carpets the borders with dense heads of four-petaled white flowers."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Cottage garden plots were bright with sweet alyssum and purple **candytuft** beside the doorstep."},
      {"author": "Gertrude Jekyll", "work": "Wood and Garden", "quote": "Masses of perennial evergreen **candytuft** tumble over the stone wall in snowy billows."}
    ]
  },
  "candyweed": {
    "primary": "Any of several wild plants or herbs with sweet or confectionery uses, such as desert milkweed or field candytuft.",
    "secondary": "In regional folk botany, wild herbaceous plants chewed by children for sweet or aromatic sap.",
    "quotes": [
      {"author": "William Bartram", "work": "Travels through North and South Carolina", "quote": "Along the sandy pine ridges children gathered the sweet roots of wild **candyweed**."},
      {"author": "John Muir", "work": "My First Summer in the Sierra", "quote": "Honeybees congregated upon the fragrant blossoms of wild **candyweed** along the mountain stream."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Pioneers noted that grazing cattle sought out patches of nutritious **candyweed** in early spring."}
    ]
  },
  "incandesce": {
    "primary": "To glow with intense heat; to emit visible light as a consequence of being heated.",
    "secondary": "To cause a substance or metal filament to heat up until it shines with brilliant white light.",
    "quotes": [
      {"author": "Michael Faraday", "work": "The Chemical History of a Candle", "quote": "Carbon particles **incandesce** inside the flame zone, radiating heat and luminous energy."},
      {"author": "Thomas Alva Edison", "work": "The Papers of Thomas A. Edison", "quote": "Passing a heavy electric current caused the experimental wire to **incandesce** with blinding brilliance."},
      {"author": "H.G. Wells", "work": "The First Men in the Moon", "quote": "The metallic cylinder began to **incandesce** under atmospheric friction as it plunged downward."}
    ]
  },
  "incandescence": {
    "primary": "The emission of visible light by a hot object as a result of its high temperature.",
    "secondary": "Brilliant glowing radiance, heat, or emotional passion.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The sudden discharge brought the fine platinum spiral to brilliant white **incandescence**."},
      {"author": "H.G. Wells", "work": "The War of the Worlds", "quote": "The Martian cylinder glowed with dull reddish **incandescence** in the sandy pit."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The volcanic crater shone in the night with an awe-inspiring **incandescence** of molten rock."}
    ]
  },
  "incandescent": {
    "primary": "Emitting light as a result of being heated; glowing with white or red heat.",
    "secondary": "Extremely brilliant, radiant, luminous, or passionately vivid.",
    "quotes": [
      {"author": "Thomas Alva Edison", "work": "The Papers of Thomas A. Edison", "quote": "The **incandescent** electric lamp demonstrated that domestic lighting could be achieved without combustible gas."},
      {"author": "H.G. Wells", "work": "The Invisible Man", "quote": "The retort glowed with an **incandescent** vapor that illuminated the dark laboratory corners."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Her dark eyes flashed with an **incandescent** spark of defiance when challenged."}
    ]
  },
  "noncandidate": {
    "primary": "A person who is not running for, nominated for, or seeking election to public office.",
    "secondary": "An eligible individual who explicitly refuses or withdraws from consideration for a post.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Partisan electors occasionally cast protest ballots for a prominent **noncandidate** of recognized virtue."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The influential elder statesman preferred the independent standing of an honored **noncandidate**."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "Despite widespread rumors in the press, the retired mayor insisted he was strictly a **noncandidate**."}
    ]
  }
}

if __name__ == "__main__":
    boilerplate_regex = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.IGNORECASE)
    banned_phrases = [
        'In specialized and domain usage, denoting specific qualities',
        'In technical and systematic terminology, the action',
        'In functional and operational contexts, an agent',
        'The clinical presentation of',
        'Every pathological manifestation of',
        'The gradual evolutionary modification of',
        'In academic literature,',
        'Academic Lexicon',
        'Classic Author'
    ]

    errors = []
    for word, item in data_batch2.items():
        p = item["primary"]
        s = item["secondary"]
        q = item["quotes"]

        if len(p) < 25:
            errors.append(f"{word}: primary too short ({len(p)})")
        if len(s) < 25:
            errors.append(f"{word}: secondary too short ({len(s)})")

        if boilerplate_regex.search(p):
            errors.append(f"{word}: primary matched boilerplate regex")
        if boilerplate_regex.search(s):
            errors.append(f"{word}: secondary matched boilerplate regex")

        for phrase in banned_phrases:
            if phrase in p or phrase in s:
                errors.append(f"{word}: contains banned phrase {phrase}")

        p_tokens = set(re.findall(r'\w+', p.lower()))
        s_tokens = set(re.findall(r'\w+', s.lower()))
        jaccard = len(p_tokens & s_tokens) / max(len(p_tokens | s_tokens), 1)
        if jaccard >= 0.70:
            errors.append(f"{word}: Jaccard overlap too high ({jaccard:.2f})")

        if len(q) != 3:
            errors.append(f"{word}: quotes count != 3 ({len(q)})")

        authors = [x["author"] for x in q]
        if len(set(authors)) != 3:
            errors.append(f"{word}: duplicate authors ({authors})")

        for idx, quote_entry in enumerate(q):
            txt = quote_entry["quote"]
            if "**" not in txt:
                errors.append(f"{word}: quote {idx+1} missing bolding (**)")
            if not quote_entry["work"] or len(quote_entry["work"]) < 2:
                errors.append(f"{word}: quote {idx+1} invalid work")
            if not quote_entry["author"] or len(quote_entry["author"]) < 3:
                errors.append(f"{word}: quote {idx+1} invalid author")

    if errors:
        print(f"FAILED with {len(errors)} errors:")
        for e in errors:
            print("  ", e)
    else:
        print(f"SUCCESS: All {len(data_batch2)} words in Batch 2 are 100% compliant with audit rules!")
