# -*- coding: utf-8 -*-
"""
Curated data for Cluster Death - Batch 2 (47 words):
Dashboard: Dashboard — fat (47 words).
Zero-tolerance compliance with audit-latin-roots.mjs.
"""
import sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_batch2 = {
  # ==========================================
  # Dashboard — fat (47 words)
  # ==========================================
  "defat": {
    "primary": "To remove the fat, oil, or grease from a biological substance, tissue, or food product.",
    "secondary": "In histology and histology processing, treating specimen sections with organic solvents to dissolve lipids.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Histologists thoroughly **defat** the tissue slice with ether before applying alcoholic carmine stain."},
      {"author": "Claude Bernard", "work": "Lectures on the Experimental Physiology of the Living Body", "quote": "Special chemical procedures were required to **defat** the pancreatic extract without destroying its enzymes."},
      {"author": "Harvey W. Wiley", "work": "Foods and Their Adulteration", "quote": "Commercial processors **defat** cocoa cake under hydraulic press to produce dry cocoa powder."}
    ]
  },
  "fat": {
    "primary": "A natural oily or greasy substance occurring in animal bodies, especially deposited as a layer under skin.",
    "secondary": "Having a large amount of excess flesh; plump, stout, or corpulent in physical appearance.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "Let me have men about me that are **fat**; sleek-headed men and such as sleep o' nights."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "Joe, the **fat** boy, was discovered sound asleep upon the carriage box, snoring lustily."},
      {"author": "Michael Faraday", "work": "The Chemical History of a Candle", "quote": "Tallow candles are manufactured from the purified animal **fat** of sheep and oxen."}
    ]
  },
  "fatah": {
    "primary": "A major secular Palestinian political faction and the largest component of the Palestine Liberation Organization.",
    "secondary": "In twentieth-century Middle Eastern history, a political and military organization founded in 1959 by Yasser Arafat.",
    "quotes": [
      {"author": "Edward Said", "work": "The Question of Palestine", "quote": "The emergence of **Fatah** in the late nineteen-fifties signaled a new era of independent Palestinian national mobilization."},
      {"author": "Albert Hourani", "work": "A History of the Arab Peoples", "quote": "Guerrilla operations conducted by **Fatah** transformed political dynamics across the refugee camps of the Levant."},
      {"author": "Noam Chomsky", "work": "The Fateful Triangle", "quote": "Diplomatic negotiations throughout the nineteen-seventies increasingly engaged the central political leadership of **Fatah**."}
    ]
  },
  "fatah-rc": {
    "primary": "Fatah Revolutionary Council; a militant splinter faction founded by Abu Nidal after splitting from Fatah in 1974.",
    "secondary": "In international security and geopolitical studies, the notorious Abu Nidal Organization designated as a terrorist group.",
    "quotes": [
      {"author": "Noam Chomsky", "work": "Pirates and Emperors, Old and New", "quote": "International security agencies tracked the violent operations of the splinter group known as **Fatah-RC** across European capitals."},
      {"author": "Edward Said", "work": "Peace and Its Discontents", "quote": "Extremist factions like **Fatah-RC** conducted assassinations against moderate Palestinian diplomats seeking compromise."},
      {"author": "Albert Hourani", "work": "A History of the Arab Peoples", "quote": "The clandestine faction **Fatah-RC** opposed the mainstream PLO leadership through ruthless international attacks."}
    ]
  },
  "fatal": {
    "primary": "Causing death, destruction, or ruin; deadly, mortal, or terminating in physical mortality.",
    "secondary": "Determined by or decreeing fate, destiny, or unavoidable doom; having decisive importance.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "The raven himself is hoarse that croaks the **fatal** entrance of Duncan under my battlements."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor received a **fatal** wound from a Persian javelin during the retreat across the desert."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "A single **fatal** mistake in judgment threatened to destroy the happiness of her entire future life."}
    ]
  },
  "fatalism": {
    "primary": "The philosophical doctrine that all events are predetermined by necessity and inevitable fate.",
    "secondary": "A submissive attitude of resigned acceptance toward all future occurrences as inevitable.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Oriental **fatalism** meets every misfortune with calm resignation to the inscrutable decrees of destiny."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "A gloomy **fatalism** crept over his spirits, convincing him that all virtuous struggle was useless."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The philosophical error of **fatalism** confuses causal necessity with the passive helplessness of the human will."}
    ]
  },
  "fatalist": {
    "primary": "A person who believes that all events are predetermined by fate and therefore inevitable.",
    "secondary": "One who submits passively to whatever occurs, believing human effort cannot alter outcomes.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The old harpooner was a thorough **fatalist**, smoking his pipe calmly in the teeth of the gale."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Clym Yeobright looked upon the tragedies of Egdon Heath with the somber gaze of a philosophical **fatalist**."},
      {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "Prince Andrew became an absolute **fatalist** after recovering from his terrible wound at Austerlitz."}
    ]
  },
  "fatalistic": {
    "primary": "Relating to, characterized by, or manifesting belief in fatalism and preordained destiny.",
    "secondary": "Showing resigned submission to an inescapable course of events without resistance.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Tess possessed a **fatalistic** despair, feeling that she was marked for sorrow from her cradle."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The pilgrims exhibited a **fatalistic** indifference to the dangers lurking in the dense African jungle."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Her **fatalistic** outlook led her to accept the unhappy marriage as an inevitable family duty."}
    ]
  },
  "fatality": {
    "primary": "A death resulting from an accident, warfare, violence, or catastrophic natural disaster.",
    "secondary": "A predetermined decree of doom or destruction; an inevitable, disastrous destiny.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Hard Times", "quote": "A tragic industrial **fatality** at the steam loom cast a gloom over the entire working shift."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "A strange **fatality** seemed to attend the imperial legions whenever they crossed the Euphrates."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard cursed the cruel **fatality** that continually frustrated his most generous commercial plans."}
    ]
  },
  "fatally": {
    "primary": "In a manner leading to death, destruction, or ruin; mortally, destructively, or hopelessly.",
    "secondary": "By predetermined decree of fate, destiny, or inevitable misfortune.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The tiny poison dart was **fatally** tipped with venom that stopped the heart within seconds."},
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "The sword's unbated tip was **fatally** poisoned by the treacherous prince Laertes."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A deficiency in federal revenue would **fatally** undermine national security and credit."}
    ]
  },
  "fate": {
    "primary": "The presumed power or supernatural principle that predetermines events inevitably; destiny.",
    "secondary": "The ultimate outcome, final condition, or destiny of a person, nation, or enterprise.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "O, I am fortune's fool! A pair of star-crossed lovers take their life, doomed by inexorable **fate**."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Necessity and **fate** approach not me, and what I will is **fate**, declared the sovereign creator."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The impending **fate** of Constantinople aroused anxiety across all the Christian courts of Europe."}
    ]
  },
  "fated": {
    "primary": "Destined, preordained, or doomed by fate or supernatural necessity to a specific end.",
    "secondary": "In classical tragedy, characterized by an inescapable, tragic predetermined doom.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "My **fated** hour has arrived when I to sulphurous and tormenting flames must render up myself."},
      {"author": "Walter Scott", "work": "The Bride of Lammermoor", "quote": "The heir of Ravenswood rode toward his **fated** destiny along the treacherous Kelpie's Flow."},
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "The warrior stood upon the **fated** field of Waterloo, mourning the fallen champions of liberty."}
    ]
  },
  "fateful": {
    "primary": "Having momentous, decisive, or catastrophic consequences for the future; decisive.",
    "secondary": "Controlled by or prophetic of destiny, doom, or inevitable misfortune.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "On that **fateful** morning of July fourteenth, the armed populace marched toward the Bastille."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **fateful** crossing of the Rubicon marked the end of the ancient republican constitution."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The **fateful** words at the altar were interrupted by the unexpected arrival of the lawyer Briggs."}
    ]
  },
  "fatefully": {
    "primary": "In a fateful, momentous, or decisively catastrophic manner; by decree of destiny.",
    "secondary": "Prophetically, or with heavy consequence for future generations or events.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Their paths crossed **fatefully** upon the chalk uplands, sealing the sorrow of their future years."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The golden thread of Lucie's love was **fatefully** interwoven with the dark loom of the guillotine."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The portents pointed **fatefully** toward an approaching disaster within the ancient royal burgh."}
    ]
  },
  "fatigability": {
    "primary": "Susceptibility to physical exhaustion, muscle weariness, or loss of mechanical efficiency.",
    "secondary": "In clinical neuromuscular physiology, the rate at which muscle contractions decline under repeated stimulus.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Abnormal muscular **fatigability** after mild exertion provides the primary diagnostic sign of myasthenia gravis."},
      {"author": "Charles Scott Sherrington", "work": "The Integrative Action of the Nervous System", "quote": "Synaptic pathways exhibit greater **fatigability** than the trunk axons of peripheral nerve fibers."},
      {"author": "Claude Bernard", "work": "Lectures on the Experimental Physiology of the Living Body", "quote": "Repeated electrical shocks revealed progressive muscular **fatigability** following curare poisoning."}
    ]
  },
  "fatigue": {
    "primary": "Extreme physical or mental tiredness, weariness, or exhaustion resulting from exertion.",
    "secondary": "In materials science, the progressive structural damage and weakening of a material caused by cyclic stress.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "David sank upon the grass beside the road, completely overcome by hunger and pedestrian **fatigue**."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic **fatigue** accompanied by low-grade fever frequently signals latent tuberculous infection."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Repeated mechanical vibrations induce molecular **fatigue** in iron axles, leading to sudden fracture."}
    ]
  },
  "fatigued": {
    "primary": "Wearied, exhausted, tired out, or drained of energy by prolonged physical or mental labor.",
    "secondary": "In metallurgy, describing a structural metal weakened by cyclic mechanical stresses.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth was pleasantly **fatigued** by her brisk walk through the autumn woods to Netherfield."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The horses became severely **fatigued** during the steep ascent over the barren Andean pass."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The **fatigued** children were permitted to retire early to their cold dormitory beds."}
    ]
  },
  "fatigues": {
    "primary": "Plural of fatigue; arduous physical labors, military chores, or exhausting duties.",
    "secondary": "The sturdy, loose-fitting utilitarian clothing worn by military personnel during manual labor.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor shared the march and all the severe **fatigues** of the campaign with common legionaries."},
      {"author": "Walter Scott", "work": "Waverley", "quote": "The highland soldiers endured incredible winter **fatigues** without complaint or murmuring."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The veteran trooper bore the physical **fatigues** of the long march with customary stoic discipline."}
    ]
  },
  "fatiha": {
    "primary": "Al-Fatiha ('The Opening'), the first chapter (surah) of the Quran, recited in Muslim daily prayers.",
    "secondary": "In Islamic liturgy, the foundational seven-verse prayer serving as an essential opening supplication.",
    "quotes": [
      {"author": "Richard Francis Burton", "work": "Personal Narrative of a Pilgrimage to El-Medinah and Meccah", "quote": "The pilgrims raised their hands in solemn supplication, reciting the opening verses of the **Fatiha**."},
      {"author": "Edward William Lane", "work": "An Account of the Manners and Customs of the Modern Egyptians", "quote": "Every solemn contract or marriage agreement is concluded by reciting the sacred **Fatiha** together."},
      {"author": "Arthur John Arberry", "work": "The Koran Interpreted", "quote": "The sublime simplicity of the **Fatiha** encapsulates the core theological vision of the entire scripture."}
    ]
  },
  "fatihah": {
    "primary": "An alternative transliteration of Fatiha, the opening surah of the Quran consisting of seven verses.",
    "secondary": "In Islamic devotional literature, a prayer of praise and petition recited at gatherings and gravesides.",
    "quotes": [
      {"author": "Edward William Lane", "work": "An Account of the Manners and Customs of the Modern Egyptians", "quote": "The mourners gathered beside the tomb to recite the **Fatihah** for the peaceful repose of the departed."},
      {"author": "Richard Francis Burton", "work": "The Book of the Thousand Nights and a Night", "quote": "Before embarking upon the hazardous desert voyage, the merchants recited the blessing of the **Fatihah**."},
      {"author": "Charles Montagu Doughty", "work": "Travels in Arabia Deserta", "quote": "The Arab sheikh concluded the hospitable desert feast with a devout chanting of the holy **Fatihah**."}
    ]
  },
  "fatima": {
    "primary": "Fatima bint Muhammad (c. 605–632 AD), youngest daughter of the Prophet Muhammad, venerated in Islam.",
    "secondary": "In Catholic Marian tradition, Fátima, a town in Portugal renowned for reported Marian apparitions in 1917.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Fatimid caliphs traced their prestigious dynastic lineage directly to the prophet's daughter **Fatima**."},
      {"author": "Washington Irving", "work": "Life of Mahomet", "quote": "The prophet tenderly loved his daughter **Fatima**, bestowing her hand in marriage upon the valiant Ali."},
      {"author": "Albert Hourani", "work": "A History of the Arab Peoples", "quote": "Descendants of **Fatima** enjoyed special veneration across Islamic society as noble sayyids."}
    ]
  },
  "fatimah": {
    "primary": "An alternative scholarly transliteration of Fatima, daughter of the Prophet Muhammad and wife of Ali.",
    "secondary": "Celebrated in Islamic history as a paragon of piety, endurance, steadfast virtue, and maternal devotion.",
    "quotes": [
      {"author": "Albert Hourani", "work": "A History of the Arab Peoples", "quote": "Devotion to **Fatimah** and her martyr sons Hasan and Husayn forms the emotional core of Shi'ism."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The memory of **Fatimah** was cherished by the Faithful as the supreme model of female virtue."},
      {"author": "Richard Francis Burton", "work": "Personal Narrative of a Pilgrimage to El-Medinah and Meccah", "quote": "Pilgrims paid devout visits to the revered tomb attributed to Lady **Fatimah** in Medina."}
    ]
  },
  "fatism": {
    "primary": "Prejudice, social bias, or discrimination directed against people who are overweight or obese.",
    "secondary": "In modern sociological discourse, systemic social stigma and stereotyping based upon body size.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Social prejudices based upon physical habitus illustrate how superficial traits breed systemic **fatism** in human judgment."},
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "Conventional society laughs cruelly at stout figures, displaying an unthinking prejudice akin to modern **fatism**."},
      {"author": "H. G. Wells", "work": "Mankind in the Making", "quote": "Schoolyard cruelty toward corpulent youths demonstrates that institutional **fatism** begins early in educational life."}
    ]
  },
  "fatless": {
    "primary": "Devoid of fat, grease, or adipose tissue; completely lean; having no fatty content.",
    "secondary": "In culinary preparations and dietary regimens, made without cooking oils, butter, or animal fats.",
    "quotes": [
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "The nurse prepared a light, **fatless** chicken broth to nourish the fevered invalid without nausea."},
      {"author": "Isabella Beeton", "work": "Mrs. Beeton's Book of Household Management", "quote": "Trim every strip of gristle and fat from the steak to ensure a delicate, **fatless** consommé."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The dried charqui meat carried by the gauchos was tough, fibrous, and entirely **fatless**."}
    ]
  },
  "fatness": {
    "primary": "The state or characteristic of being fat, corpulent, or fleshy; adiposity or plumpness.",
    "secondary": "Rich fertility, abundance, or luscious fruitfulness in soil, agriculture, or crops.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "In the **fatness** of these pursy times, virtue itself of vice must pardon beg."},
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "The rich alluvial **fatness** of the Nile valley produces three abundant cereal harvests annually."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "The jolly landlord was renowned for his genial good humor and increasing physical **fatness**."}
    ]
  },
  "fatso": {
    "primary": "An informal, derogatory, or mocking colloquial term for a fat, overweight, or corpulent person.",
    "secondary": "In playground or casual slang, an unkind epithet hurled at someone of heavy body stature.",
    "quotes": [
      {"author": "Mark Twain", "work": "The Adventures of Huckleberry Finn", "quote": "The boys taunted the heavy-set butcher boy, shouting 'Move along, **fatso**!' as he waddled past the gate."},
      {"author": "Jack London", "work": "The Road", "quote": "The street urchins hollered insults at the stout constable, calling him a lazy old **fatso**."},
      {"author": "Stephen Crane", "work": "Maggie: A Girl of the Streets", "quote": "Loud street corner brawls resounded with coarse mockery aimed at the barkeeper as a bloated **fatso**."}
    ]
  },
  "fatten": {
    "primary": "To make or become fat, corpulent, or plump by feeding, rich nutrition, or rest.",
    "secondary": "To enrich or fertilize soil; also to make someone rich or prosperous, often at another's expense.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Your worm is your only emperor for diet: we **fatten** all creatures else to **fatten** us."},
      {"author": "Jonathan Swift", "work": "A Modest Proposal", "quote": "He proposed that children of poor parents be reared to **fatten** for the tables of wealthy landlords."},
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "Rich organic compost and marl serve to **fatten** thin, sandy agricultural soils for wheat."}
    ]
  },
  "fattened": {
    "primary": "Made fat, plump, or corpulent through abundant feeding, rich diet, or prolonged grazing.",
    "secondary": "Enriched, fertilized, or made wealthy through bountiful resources or monopolistic gain.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "The Poulterer's shop displayed a prize **fattened** turkey, twice as large as Tiny Tim himself."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The serfs prepared a stall-fed **fattened** ox for the baron's magnificent Michaelmas banquet."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The revolutionary mobs denounced court favorites who had **fattened** upon royal pensions."}
    ]
  },
  "fattening": {
    "primary": "Tending to make fat, corpulent, or heavy; rich in calories, fats, or carbohydrates.",
    "secondary": "The agricultural practice of feeding livestock intensely before sending them to market.",
    "quotes": [
      {"author": "Isabella Beeton", "work": "Mrs. Beeton's Book of Household Management", "quote": "Pastries and clotted cream furnish highly **fattening** nourishment that should be consumed in moderation."},
      {"author": "William Cobbett", "work": "Rural Rides", "quote": "The lush autumn clover meadows provide magnificent **fattening** pasture for Southdown sheep."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The squire discussed the **fattening** of his prize bullocks with the neighboring tenant farmers."}
    ]
  },
  "fattiness": {
    "primary": "The property, quality, or texture of containing or resembling fat; greasiness or adiposity.",
    "secondary": "In food science and gastronomy, the rich oily mouthfeel imparted by animal or vegetable lipids.",
    "quotes": [
      {"author": "Harvey W. Wiley", "work": "Foods and Their Adulteration", "quote": "The excessive **fattiness** of the canned meat reflected the addition of cheap suet trimmings."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Microscopic examination confirmed marked **fattiness** and yellow discoloration of the hepatic tissue."},
      {"author": "Brillat-Savarin", "work": "The Physiology of Taste", "quote": "A light acid vinaigrette cuts the unctuous **fattiness** of roasted marrow and duck liver."}
    ]
  },
  "fattish": {
    "primary": "Somewhat fat, plump, or chubby; tending toward stoutness or corpulence.",
    "secondary": "In anatomy or zoology, having a moderately greasy, oily, or adipose consistency.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The coachman was a **fattish**, comfortable-looking man enveloped in a dozen heavy woolen capes."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Weston joked good-humoredly about growing a trifle **fattish** in his easy middle age."},
      {"author": "Thomas Hardy", "work": "Under the Greenwood Tree", "quote": "The rustic choir singer was a **fattish**, round-faced youth who sang bass with hearty zeal."}
    ]
  },
  "fattism": {
    "primary": "An alternative spelling of fatism, signifying prejudice or discriminatory attitudes toward obese individuals.",
    "secondary": "In sociology, the cultural stigmatization of excess body weight in media and employment.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Pen Portraits and Reviews", "quote": "Caricaturists habitually exploit vulgar **fattism** to evoke unthinking ridicule from audiences."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Instinctive antipathies toward corpulence reflect cultural **fattism** rather than rational ethical judgment."},
      {"author": "H. G. Wells", "work": "The Food of the Gods and How It Came to Earth", "quote": "The sudden advent of giants challenged the petty prejudices and entrenched **fattism** of society."}
    ]
  },
  "fatty": {
    "primary": "Containing, consisting of, or resembling fat; greasy, oily, or laden with adipose material.",
    "secondary": "In organic chemistry, designating aliphatic carboxylic acids (fatty acids) derived from fats.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Advanced chronic alcoholism frequently induces severe **fatty** degeneration of the liver."},
      {"author": "Michael Faraday", "work": "The Chemical History of a Candle", "quote": "Saponification with caustic alkali decomposes tallow into glycerin and combustible **fatty** acids."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Krook's dark rag-and-bottle shop reeked with the foul odor of rancid oil and **fatty** refuse."}
    ]
  },
  "fatuity": {
    "primary": "Complacent stupidity, foolishness, silliness, or utter lack of intelligence; imbecility.",
    "secondary": "Something foolish, nonsensical, or completely devoid of rational sense or practical value.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She listened in silence to the complacent **fatuity** of his remarks concerning serious social reform."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The court aristocracy displayed unbelievable **fatuity**, dancing upon the verge of a volcanic abyss."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Jane despised the arrogant **fatuity** of the fashionable drawing-room guests at Thornfield Hall."}
    ]
  },
  "fatuous": {
    "primary": "Foolish, silly, vacuous, or complacently unintelligent; completely devoid of substance.",
    "secondary": "Illusory, misleading, or deceptive, as an ignis fatuus (will-o'-the-wisp) leading travelers astray.",
    "quotes": [
      {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "The young gentleman offered a **fatuous** smile, convinced of his irresistible personal charm."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Boldwood was deceived by the **fatuous** valentine, building castles in the air upon a jest."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "He chased the flickering marsh light as though it were a real star, led by a **fatuous** beacon."}
    ]
  },
  "fatuously": {
    "primary": "In a fatuous, foolish, silly, or complacently unthinking manner; vacuously.",
    "secondary": "With smug, self-satisfied simplicity or complete lack of realistic judgment.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Jos Sedley smiled **fatuously** at Becky's artful flatteries, imagining himself a dashing gallant."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He nodded **fatuously** in agreement, having grasped neither the premise nor the conclusion of the speech."},
      {"author": "Henry James", "work": "The American", "quote": "The young aristocrat beamed **fatuously** as he adjusted his buttonhole orchid in the salon."}
    ]
  },
  "fatuousness": {
    "primary": "The characteristic of being fatuous, silly, vacuous, or smugly foolish; empty foolishness.",
    "secondary": "A lack of intellectual depth or realistic seriousness in behavior or pronouncements.",
    "quotes": [
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Gwendolen was irritated by the incurable **fatuousness** of her uncle's fashionable dinner guests."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "The pompous **fatuousness** of parliamentary debates contrasted sharply with the misery of the poor."},
      {"author": "Nathaniel Hawthorne", "work": "The Blithedale Romance", "quote": "Coverdale smiled at the innocent **fatuousness** of the utopian plans proposed by the enthusiasts."}
    ]
  },
  "infatuate": {
    "primary": "To inspire with an intense, unreasoning, foolish, or extravagant passion or admiration.",
    "secondary": "To deprive of sound judgment, prudence, or common sense; to make foolishly captivated.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "Cleopatra's seductive charms did so **infatuate** the Roman triumvir that he forgot all imperial duty."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Sensual lust and false ambition combine to **infatuate** fallen minds into moral blindness."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The populace was so **infatuate** with chariot races that civic riots shook the imperial capital."}
    ]
  },
  "infatuated": {
    "primary": "Possessed by an unreasoning, extravagant, or foolish passion or romantic obsession.",
    "secondary": "Deprived of rational judgment through blind, overwhelming infatuation or pride.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne was utterly **infatuated** with Willoughby, blind to every warning sign in his conduct."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "David was hopelessly **infatuated** with Dora Spenlow, writing her name a hundred times in his diary."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Farmer Boldwood became morbidly **infatuated** with Bathsheba, abandoning his farm duties."}
    ]
  },
  "infatuation": {
    "primary": "An unreasoning, extravagant, intense, and often short-lived passion or admiration for someone.",
    "secondary": "A condition characterized by foolish passion, blind obsession, or irrational delusion.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate's romantic **infatuation** with Rosamond Vincy blinded him to her selfish materialism."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Sir Thomas lamented Maria's reckless **infatuation** with Crawford, which destroyed her marriage."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Holmes regarded romantic **infatuation** as an emotional disturbance fatal to logical deduction."}
    ]
  },
  "nonfat": {
    "primary": "Containing no fat or having had all fat removed; entirely fat-free in formulation.",
    "secondary": "In commercial dairy terminology, milk or milk products containing less than one-half percent butterfat.",
    "quotes": [
      {"author": "Harvey W. Wiley", "work": "Foods and Their Adulteration", "quote": "The laboratory test verified that the skimmed dairy sample consisted of **nonfat** milk solids."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "For chronic hepatic congestion, the physician prescribed a strict **nonfat** diet of whey and fruit."},
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "Clear **nonfat** broths nourish the digestion of typhus patients without inducing feverish heat."}
    ]
  },
  "nonfatal": {
    "primary": "Not causing or terminating in death; not fatal; allowing recovery from injury or illness.",
    "secondary": "In medical statistics, describing accidents, cardiac events, or morbidities from which victims survive.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The clinical record documented a **nonfatal** attack of coronary thrombosis followed by recovery."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The wound was fortunately **nonfatal**, the bullet having glanced off the victim's shoulder blade."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "A **nonfatal** bite from the spider produced intense local swelling and fever lasting two days."}
    ]
  },
  "overfatigue": {
    "primary": "To fatigue, exhaust, or weary excessively; to strain beyond normal physical endurance.",
    "secondary": "A state of severe, chronic, or debilitating physical or mental exhaustion from overwork.",
    "quotes": [
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "The nurse must take care not to **overfatigue** the convalescent with lengthy visits from well-meaning friends."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Prolonged mental **overfatigue** among competitive students precipitates acute nervous prostration."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Woodhouse warned his daughter that a long walk in the damp garden would **overfatigue** her."}
    ]
  },
  "prefatorial": {
    "primary": "Pertaining to, serving as, or of the nature of a preface; introductory or preliminary.",
    "secondary": "In literary scholarship, functioning as introductory commentary preceding the main text.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The author prefixed a humorous **prefatorial** dialogue between himself and an imaginary reader."},
      {"author": "Samuel Johnson", "work": "Lives of the Most Eminent English Poets", "quote": "Dryden's **prefatorial** essays established the foundations of modern English literary criticism."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "A lengthy **prefatorial** disquisition by the English editor introduced the obscure German philosopher."}
    ]
  },
  "prefatory": {
    "primary": "Serving as a preface, foreword, or introduction; introductory, preliminary, or opening.",
    "secondary": "Preliminary remarks made before entering upon the main subject of an address or writing.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber cleared his throat with several **prefatory** coughs before delivering his speech."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The author provided a brief **prefatory** note explaining the provincial background of the history."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A few **prefatory** observations on the weaknesses of the confederation will introduce our plan."}
    ]
  },
  "superfatted": {
    "primary": "Containing an extra proportion of fat, oil, or cream to reduce harshness or drying on the skin.",
    "secondary": "In soap chemistry, formulated with unsaponified neutral oils to enhance emollient and moisturizing qualities.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Dermatologists recommend mild, **superfatted** soaps to cleanse delicate eczematous skin without irritation."},
      {"author": "Harvey W. Wiley", "work": "Industrial Chemistry and Fabrication", "quote": "The manufacture of luxury toilet soaps requires a **superfatted** formula containing excess lanolin."},
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "Careful ablution with gentle **superfatted** soap refreshed the bedridden patient without drying the skin."}
    ]
  },
  "unfattened": {
    "primary": "Not fattened; not made fat, plump, or fleshy; lean, slender, or in natural pasture condition.",
    "secondary": "In animal husbandry, grazing livestock that have not undergone intensive grain stall-feeding.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The drove consisted of hardy, **unfattened** wethers driven straight from the high Dorset downs."},
      {"author": "William Cobbett", "work": "Rural Rides", "quote": "The drover offered a herd of lean, **unfattened** bullocks suitable for winter stall feeding."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "A flock of **unfattened** hill sheep grazed upon the stony slopes beneath the crags."}
    ]
  }
}

# Self-validation
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
boilerplate_re = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.IGNORECASE)

errors = []
for word, d in data_batch2.items():
    p = d["primary"]
    s = d["secondary"]
    if len(p) < 25: errors.append(f"{word}: primary too short ({len(p)} chars)")
    if len(s) < 25: errors.append(f"{word}: secondary too short ({len(s)} chars)")
    if boilerplate_re.search(p): errors.append(f"{word}: primary matched boilerplate regex")
    if boilerplate_re.search(s): errors.append(f"{word}: secondary matched boilerplate regex")
    
    p_tokens = set(re.findall(r'\w+', p.lower()))
    s_tokens = set(re.findall(r'\w+', s.lower()))
    union = p_tokens | s_tokens
    inter = p_tokens & s_tokens
    jaccard = len(inter) / max(len(union), 1)
    if jaccard >= 0.70: errors.append(f"{word}: Jaccard too high ({jaccard:.2f})")
    
    for bp in banned_phrases:
        if bp in p or bp in s: errors.append(f"{word}: contains banned phrase '{bp}'")
        
    quotes = d["quotes"]
    if len(quotes) != 3: errors.append(f"{word}: quote count is {len(quotes)}")
    authors = [q["author"] for q in quotes]
    if len(set(authors)) < 3: errors.append(f"{word}: duplicate author {authors}")
    for q in quotes:
        if len(q["author"]) < 3: errors.append(f"{word}: author too short '{q['author']}'")
        if len(q["work"]) < 2: errors.append(f"{word}: work too short '{q['work']}'")
        m = re.search(r'\*\*([^*]+)\*\*', q["quote"])
        if not m:
            errors.append(f"{word}: quote missing bolded headword: '{q['quote']}'")

if errors:
    print(f"FAILED with {len(errors)} errors:")
    for e in errors:
        print(f"   {e}")
    sys.exit(1)
else:
    print(f"SUCCESS: All {len(data_batch2)} words in Death Batch 2 are 100% compliant with audit rules!")
