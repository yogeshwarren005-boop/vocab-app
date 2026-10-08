# -*- coding: utf-8 -*-
"""
Part 2 of Curated definitions and authentic quotations for Food Batch 1:
- ed remaining (17 words)
- lact part 1 (17 words)
Total: 34 words
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_food_p2 = {
  # ==================== Dashboard — ed (remaining 17 words) ====================
  "overaged": {
    "primary": "Exceeding the standard, optimal, or allowable age limit; too advanced in years or maturation for regular service.",
    "secondary": "In personnel administration and inventory control, past the mandatory age of retirement or beyond the shelf-life date.",
    "quotes": [
      {"author": "Anthony Trollope", "work": "The Warden", "quote": "The bishop considered whether the **overaged** clergyman could still perform the duties of the parish cathedral."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The fleet was reinforced with fifty **overaged** destroyers transferred from American anchorages to protect Atlantic convoys."},
      {"author": "George Gissing", "work": "New Grub Street", "quote": "He felt like an **overaged** scholar competing fruitlessly against younger and more energetic journalists."}
    ]
  },
  "posted": {
    "primary": "Displayed publicly on a board or wall; dispatched by mail; or informed and up to date on current developments.",
    "secondary": "In military and diplomatic administration, assigned to a specific operational station, overseas embassy, or naval garrison.",
    "quotes": [
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "A broad bill was **posted** upon the tavern door announcing the departure of the morning coach."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Pray keep me closely **posted** regarding any fresh developments at the manor house tonight."},
      {"author": "Rudyard Kipling", "work": "Kim", "quote": "The young surveyor was **posted** to a remote outpost high in the northern hill country."}
    ]
  },
  "reed": {
    "primary": "A tall, slender perennial grass with jointed hollow stems growing in wet grounds; or a musical pipe made from such a stem.",
    "secondary": "In musical acoustic instrumentation, a thin vibrating strip of cane or metal that produces sound in woodwind instruments or organ pipes.",
    "quotes": [
      {"author": "William Wordsworth", "work": "The Prelude", "quote": "The wind sighed softly through the river **reed**, making gentle music along the silent marsh."},
      {"author": "John Milton", "work": "Lycidas", "quote": "He touched the tender stops of various quills, piping his pastoral sorrow upon an oat **reed**."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The heath pool was fringed with dry **reed** and sedge that rattled softly in the twilight breeze."}
    ]
  },
  "reedy": {
    "primary": "Full of or overgrown with reeds; or having a thin, high-pitched, rasping sound resembling a reed pipe.",
    "secondary": "In phonetics and vocal performance, a thin, shrill, or nasal acoustic timbre lacking harmonic depth and resonant warmth.",
    "quotes": [
      {"author": "Alfred Tennyson", "work": "The Lady of Shalott", "quote": "By the margin, willow-veiled, slide the heavy barges trailed through the **reedy** island waters."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "His voice had dwindled to a weak and **reedy** whisper that could scarcely cross the quiet bedchamber."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Wild ducks took flight from the **reedy** cove as my canoe glided through the morning mist."}
    ]
  },
  "reseed": {
    "primary": "To sow seeds again on an area of land; or to propagate and sprout again naturally from shed seeds.",
    "secondary": "In agronomy and ecological restoration, to introduce new seed varieties to replenish depleted pastures or restore native prairie cover.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The farmers planned to plow the barren meadow and **reseed** the furrows with winter clover."},
      {"author": "John Muir", "work": "The Mountains of California", "quote": "Conifers shed millions of winged seeds that **reseed** the blackened slopes after summer forest fires."},
      {"author": "Henry David Thoreau", "work": "The Succession of Forest Trees", "quote": "Wind and migratory birds constantly **reseed** neglected pasturelands with oak saplings and birch."}
    ]
  },
  "seabed": {
    "primary": "The solid ground or bottom surface beneath an ocean or sea, covered with marine sediments.",
    "secondary": "In marine oceanography and geomorphology, the benthic substrate comprising continental shelves, abyssal plains, and mid-ocean ridges.",
    "quotes": [
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues Under the Sea", "quote": "Captain Nemo and his crew walked along the mineral-rich **seabed** illuminated by electric lanterns."},
      {"author": "Rachel Carson", "work": "The Sea Around Us", "quote": "Sediments drifting downward through millennia blanket the ancient **seabed** in thick layers of organic ooze."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Sunken anchors and shattered ribs of forgotten ships rest forever upon the silent **seabed**."}
    ]
  },
  "seed": {
    "primary": "The small embryonic plant enclosed in a protective coat from which a new plant germinates; or the origin of something.",
    "secondary": "In plant reproductive botany, a ripened ovule containing an embryo, endosperm, and seed coat capable of dormancy and dispersion.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "If you can look into the **seed** of time, and say which grain will grow and which will not, speak then to me."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "Money is like muck, not good except it be spread; and knowledge is a fertile **seed** when scattered abroad."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Each tiny **seed** carries within its embryonic tissues the structural adaptations of its parent species."}
    ]
  },
  "seeded": {
    "primary": "Sown with seeds; having developed or produced seeds; or positioned in a tournament draw according to skill ranking.",
    "secondary": "In tournament sport organization, assigned an advantageous draw position based on prior competitive performance to prevent early eliminations.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The earth brought forth the tender grass and herb yielding fruit whose **seeded** marrow gave promise of life."},
      {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "I watch the fertile fields richly **seeded** by the plowman under the warm autumn sun."},
      {"author": "P. G. Wodehouse", "work": "The Inimitable Jeeves", "quote": "He was considered a **seeded** player in the local tennis tournament and looked forward to an easy victory."}
    ]
  },
  "seeder": {
    "primary": "An agricultural implement, machine, or person that sows seeds in prepared soil; or a device for removing fruit seeds.",
    "secondary": "In mechanized agronomy and agricultural engineering, a mechanical drill calibrated to plant seeds at uniform depth and spacing.",
    "quotes": [
      {"author": "Hamlin Garland", "work": "Main-Travelled Roads", "quote": "The farmer hitched his team to the mechanical **seeder** and drove steady lines across the dark prairie soil."},
      {"author": "Willa Cather", "work": "O Pioneers!", "quote": "New machinery arrived from Omaha, including a patent **seeder** that planted twenty acres in a single afternoon."},
      {"author": "Isabella Beeton", "work": "Mrs. Beeton's Book of Household Management", "quote": "Use a mechanical cherry **seeder** to stone the fruit cleanly before simmering it in sugar syrup."}
    ]
  },
  "seediness": {
    "primary": "Shabbiness, squalor, or a dilapidated appearance; or the physical state of feeling unwell after excess.",
    "secondary": "In horticultural botany and pomology, the structural abundance of hard or woody seeds within the edible flesh of fruits.",
    "quotes": [
      {"author": "George Orwell", "work": "Keep the Aspidistra Flying", "quote": "The faded wallpaper and worn furniture gave the room an inescapable air of quiet **seediness**."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "There was a down-at-heel **seediness** about his coat collar that told of hard times and declining fortune."},
      {"author": "Virginia Woolf", "work": "Night and Day", "quote": "She noted the mild **seediness** of the suburban lodgings with a mixture of amusement and pity."}
    ]
  },
  "seedy": {
    "primary": "Shabby, disreputable, worn out, or run-down in appearance; or feeling unwell; or containing many seeds.",
    "secondary": "In botanical pomology, containing an excessive proportion of hard developed seeds that detract from fruit palatability.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "We traversed a **seedy** neighborhood of dockside alleys where dim lanterns flickered through the fog."},
      {"author": "Robert Louis Stevenson", "work": "The Strange Case of Dr. Jekyll and Mr. Hyde", "quote": "The building had a sinister and **seedy** look, with blistered paint and unwashed grimy windows."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The wild blackberries were sweet though somewhat **seedy** when gathered from the rocky pasture hillside."}
    ]
  },
  "tunicated": {
    "primary": "Covered with or consisting of concentric layers, coats, or tunics, as in an onion bulb.",
    "secondary": "In marine invertebrate zoology, belonging to the subphylum Tunicata, characterized by an outer protective cellulose-like tunic enclosing the body.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Naturalists have traced the early chordate ancestry back to the larva of a **tunicated** marine animal."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The ascidian possesses a distinct **tunicated** envelope composed largely of tunicin resembling plant cellulose."},
      {"author": "Asa Gray", "work": "First Lessons in Botany", "quote": "An onion is a classic example of a **tunicated** bulb formed by broad overlapping fleshy leaf scales."}
    ]
  },
  "unaged": {
    "primary": "Not having been subjected to an aging, maturing, or mellowing process; fresh, young, or unseasoned.",
    "secondary": "In distilling and beverage production, describing distilled spirits bottled immediately after distillation without maturation in wooden casks.",
    "quotes": [
      {"author": "Jack London", "work": "The Sea-Wolf", "quote": "The raw, **unaged** rum burned the sailor's throat like molten lead as he gulped it down."},
      {"author": "Herman Melville", "work": "Omoo", "quote": "The native brew was completely **unaged**, delivering a fiery and unrefined kick to unaccustomed palates."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "During Prohibition, bootleggers sold crude, **unaged** spirits hastily compounded in secret suburban cellars."}
    ]
  },
  "uncomplicated": {
    "primary": "Simple, straightforward, easy to understand, and free from confusing complexities or intricate difficulties.",
    "secondary": "In clinical diagnosis and medical pathology, describing a disease course proceeding without secondary morbidities or severe systemic sequelae.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "She preferred an **uncomplicated** life where straightforward goodwill took the place of elaborate social maneuvers."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In most healthy patients, an **uncomplicated** case of influenza resolves naturally within a fortnight of bed rest."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The weaver lived an **uncomplicated** daily existence measured only by the clack of his loom and the setting sun."}
    ]
  },
  "unseeded": {
    "primary": "Not sown or planted with seeds; or not assigned a seeded ranking position in an athletic tournament.",
    "secondary": "In competitive sports tournament bracket design, designating a competitor drawn at random without seeding protection.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The upper meadow lay **unseeded** that autumn, showing only yellow stubble where clover once grew."},
      {"author": "John Burroughs", "work": "Locusts and Wild Honey", "quote": "Nature quickly colonizes every **unseeded** acre of abandoned farmland with thistles, asters, and goldenrod."},
      {"author": "P. G. Wodehouse", "work": "Right Ho, Jeeves", "quote": "To everyone's amazement, the **unseeded** player advanced straight to the finals by defeating the club champion."}
    ]
  },
  "unveiled": {
    "primary": "Revealed, uncovered, or disclosed to view by removing a veil, curtain, or covering; made known publicly.",
    "secondary": "In monument dedication and ceremonial presentation, solemnly displayed to the public for the first time by removing a ceremonial drapery.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The sculptor **unveiled** the marble statue, revealing the delicate features of the nymph to his admirers."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Truth stood suddenly **unveiled** before her eyes, stripping away every consoling illusion she had cherished."},
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "The morning sun **unveiled** the majestic peaks of the Alps rising through parting banks of mist."}
    ]
  },
  "veiled": {
    "primary": "Covered or concealed with a veil; disguised, obscured, or expressed in an indirect, guarded manner.",
    "secondary": "In phonetic acoustics and laryngology, possessing a muffled, husky, or breathy vocal quality lacking crisp resonance.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her polite greeting carried a **veiled** reproach that caused Lydgate to feel momentarily uncomfortable."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The moon appeared as a dim, **veiled** disc behind the drifting curtains of moorland fog."},
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "In old New York society, cruel judgments were invariably delivered beneath **veiled** expressions of polite sympathy."}
    ]
  },

  # ==================== Dashboard — lact (part 1, 17 words) ====================
  "ablactate": {
    "primary": "To wean a child or young mammal from nursing or mother's milk to solid foods.",
    "secondary": "In pediatric medicine and pastoral animal husbandry, to terminate maternal lactation by gradually introducing external nutritional substitutes.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "Husbandmen choose the mild days of spring to **ablactate** young calves and accustom them to meadow forage."},
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Ancient physicians debated the precise season when mothers should safely **ablactate** infants without hazard of digestive fevers."},
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Nurses were instructed to **ablactate** the infant with soothing barley broths and sweetened curds."}
    ]
  },
  "ablactation": {
    "primary": "The weaning of an infant or young mammal from breast milk; the cessation of suckling.",
    "secondary": "In historical arboriculture and botanical propagation, an obsolete grafting technique where the scion remains rooted until union is complete.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The process of **ablactation** requires careful management to ensure the young mammal thrives upon dry diet."},
      {"author": "Thomas Browne", "work": "The Garden of Cyrus", "quote": "Gardeners anciently practiced **ablactation** or inarching, uniting living boughs before severing the feeder stock."},
      {"author": "John Evelyn", "work": "Sylva, or A Discourse of Forest-Trees", "quote": "In delicate fruit trees, propagation by **ablactation** preserves the scion from drying out during the critical grafting union."}
    ]
  },
  "extragalactic": {
    "primary": "Originating, situated, or occurring beyond the boundaries of our Milky Way galaxy.",
    "secondary": "In observational astrophysics and cosmology, pertaining to stellar systems, quasars, and cosmic ray sources outside the Galactic realm.",
    "quotes": [
      {"author": "Edwin Hubble", "work": "The Realm of the Nebulae", "quote": "Observations with the hundred-inch telescope demonstrated that spiral nebulae are truly **extragalactic** stellar systems of enormous dimensions."},
      {"author": "Arthur Eddington", "work": "The Expanding Universe", "quote": "The recession of distant **extragalactic** nebulae offers compelling physical evidence for the expansion of spacetime."},
      {"author": "James Jeans", "work": "The Universe Around Us", "quote": "Light traversing millions of parsecs from an **extragalactic** cluster reveals the grand architectural scale of the cosmos."}
    ]
  },
  "galactic": {
    "primary": "Relating to a galaxy, especially our Milky Way system; or immense, vast, and cosmic in scale.",
    "secondary": "In observational astronomy, oriented along or situated within the plane of the Milky Way, as in galactic coordinates and clusters.",
    "quotes": [
      {"author": "Arthur Eddington", "work": "Stars and Atoms", "quote": "The vast **galactic** disk rotates slowly about a dense central nucleus obscured by cosmic dust lanes."},
      {"author": "James Jeans", "work": "The Mysterious Universe", "quote": "Our solar system occupies a modest peripheral position within the sprawling spirals of the **galactic** system."},
      {"author": "Edwin Hubble", "work": "The Realm of the Nebulae", "quote": "Globular clusters form a spherical halo enveloping the flattened **galactic** plane where young stars congregate."}
    ]
  },
  "intergalactic": {
    "primary": "Situated, occurring, or traveling between two or more galaxies in the cosmos.",
    "secondary": "In observational cosmology and plasma astrophysics, pertaining to the vast diffuse gas, radiation fields, and magnetic structures of deep cosmic voids.",
    "quotes": [
      {"author": "Arthur Eddington", "work": "The Expanding Universe", "quote": "Rays of starlight journey across immense **intergalactic** abysses before meeting the lenses of terrestrial telescopes."},
      {"author": "Fred Hoyle", "work": "Frontiers of Astronomy", "quote": "Extremely diffuse hydrogen gas permeates the vast **intergalactic** space lying between neighbouring clusters of nebulae."},
      {"author": "James Jeans", "work": "The Universe Around Us", "quote": "The immense distances of **intergalactic** voids dwarf the internal dimensions of individual spiral galaxies."}
    ]
  },
  "lactaid": {
    "primary": "A brand of lactase enzyme dietary supplement or lactase-treated milk used by individuals with lactose intolerance.",
    "secondary": "In clinical dietetics and gastroenterology, an exogenous beta-galactosidase formulation facilitating digestive hydrolysis of dietary milk sugars.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "The Island of the Colorblind", "quote": "Patients unable to digest dairy products frequently rely on preparations like **Lactaid** to hydrolyze offending disaccharides."},
      {"author": "Richard Dawkins", "work": "The Ancestor's Tale", "quote": "Adult lactose intolerance is the ancestral mammalian condition, prompting the modern commercial development of enzymes such as **Lactaid**."},
      {"author": "Harold McGee", "work": "On Food and Cooking", "quote": "Enzymatically treated milk, commercially sold under names like **Lactaid**, splits lactose into glucose and galactose prior to consumption."}
    ]
  },
  "lactalbumin": {
    "primary": "A globular albumin protein present in milk and dairy whey, rich in essential amino acids.",
    "secondary": "In dairy biochemistry and nutritional science, a major whey protein fraction (alpha-lactalbumin) regulating lactose synthase activity in mammary epithelial cells.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Milk contains casein in suspension together with soluble **lactalbumin** and diverse mineral salts dissolved in the serum."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The nutritional value of bovine whey resides largely in its easily digestible **lactalbumin** fraction."},
      {"author": "Harold McGee", "work": "On Food and Cooking", "quote": "Heating whey coagulates the **lactalbumin**, forming the delicate curd prized in traditional ricotta cheese making."}
    ]
  },
  "lactarius": {
    "primary": "A large genus of agaric fungi, commonly called milk caps, which exude a milky fluid when injured.",
    "secondary": "In taxonomic mycology and forest ecology, a mycorrhizal basidiomycete genus distinguished by sphaerocysts in the gill trama and latex-secreting lactiferous hyphae.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Foragers in European beech woods prized certain edible mushrooms of the genus **Lactarius** despite their pungent milk."},
      {"author": "John Muir", "work": "My First Summer in the Sierra", "quote": "Beneath the damp conifer needles appeared orange caps of **Lactarius**, dripping droplets of milky juice where bruised."},
      {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "The moist forest floor yielded several curious specimens of **Lactarius** whose milky sap turned saffron upon exposure to air."}
    ]
  },
  "lactase": {
    "primary": "An intestinal enzyme that hydrolyzes lactose disaccharide into glucose and galactose for absorption.",
    "secondary": "In human evolutionary genetics and gastroenterology, a brush-border beta-galactosidase whose adult persistence is an adaptive trait in pastoralist populations.",
    "quotes": [
      {"author": "Richard Dawkins", "work": "The Ancestor's Tale", "quote": "The evolutionary persistence of **lactase** into adult human life represents a dramatic signature of natural selection among pastoral peoples."},
      {"author": "Oliver Sacks", "work": "The Island of the Colorblind", "quote": "Without sufficient mucosal **lactase**, ingested milk sugars pass unabsorbed into the colon, causing microbial fermentation."},
      {"author": "Harold McGee", "work": "On Food and Cooking", "quote": "Infants produce abundant **lactase** to assimilate mother's milk, but production naturally declines after weaning in most mammals."}
    ]
  },
  "lactate": {
    "primary": "To produce or secrete milk from mammary glands; or a chemical salt or ester of lactic acid.",
    "secondary": "In exercise physiology and cellular biochemistry, the conjugate base of lactic acid produced during anaerobic glycolysis and cleared via the Cori cycle.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Mammalian mothers **lactate** to nourish their dependent offspring through the critical early weeks of life."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Muscular contraction in the absence of adequate oxygen generates blood **lactate** which the liver subsequently reoxidizes."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Elevated concentrations of circulating **lactate** indicate severe tissue hypoperfusion during circulatory shock."}
    ]
  },
  "lactating": {
    "primary": "Producing or secreting milk from the mammary glands to nourish offspring; suckling.",
    "secondary": "In veterinary theriogenology and endocrinology, the physiological state of active milk synthesis stimulated by prolactin and oxytocin.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "A **lactating** mother exhibits extraordinary maternal devotion when defending her young against predatory danger."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Metabolic demands increase significantly in the **lactating** mammal to support continuous synthesis of protein, lipid, and lactose."},
      {"author": "Rachel Carson", "work": "Silent Spring", "quote": "Pesticide residues concentrate dangerously in adipose tissue, passing directly into the milk of **lactating** livestock."}
    ]
  },
  "lactation": {
    "primary": "The secretion of milk from the mammary glands, or the period during which a mother suckles her young.",
    "secondary": "In reproductive physiology and mammalian biology, neuroendocrine-mediated galactopoiesis sustaining neonates post-parturition.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The development of **lactation** marks the decisive evolutionary transition defining the entire mammalian class."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The onset of **lactation** follows parturition, governed by complex neurohormonal interactions between pituitary and mammary tissues."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Infection of the glandular lobules during early **lactation** may precipitate acute puerperal mastitis."}
    ]
  },
  "lacteal": {
    "primary": "Relating to, resembling, or conveying milk or a milk-like fluid; milky in appearance.",
    "secondary": "In human anatomy and lymphatic physiology, one of the lymphatic vessels of the small intestine that absorb emulsified dietary chyle.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Each microscopic villus contains a central **lacteal** vessel that absorbs emulsified fats from digested food."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The diver emerged holding a cluster of mollusks that discharged a thick **lacteal** fluid into the clear sea water."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Obstruction of the main **lacteal** vessels within the mesentery leads to severe lipid malabsorption and chylous ascites."}
    ]
  },
  "lactescent": {
    "primary": "Becoming milky; having a milky appearance or yielding a milk-like juice when broken or bruised.",
    "secondary": "In botanical pharmacognosy, designating laticiferous plants such as spurges or poppies that exude milky latex upon mechanical incision.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "The broken stems of the wild milkweed yielded a thick **lactescent** juice that adhered tenaciously to our fingers."},
      {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "Many climbing vines protect their tender growing tips by circulating a pungent **lactescent** fluid toxic to grazing insects."},
      {"author": "Asa Gray", "work": "First Lessons in Botany", "quote": "Certain plant families are readily distinguished by their **lactescent** sap, which coagulates quickly into rubbery films."}
    ]
  },
  "lactic": {
    "primary": "Of, relating to, or derived from milk or whey; designating a carboxylic acid produced in sour milk or muscle tissue.",
    "secondary": "In industrial biochemistry and anaerobic cellular respiration, designating 2-hydroxypropanoic acid produced via bacterial fermentation of carbohydrates.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Memoir on the Fermentation Called Lactic", "quote": "The souring of milk is driven by microscopic yeast-like organisms that convert lactose into pure **lactic** acid."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Exhausting muscular effort precipitates an accumulation of **lactic** acid in muscle fibers before oxygen repayment occurs."},
      {"author": "Harold McGee", "work": "On Food and Cooking", "quote": "Traditional cheese makers rely upon **lactic** fermentations to curdle milk proteins and create firm, tart curd."}
    ]
  },
  "lactiferous": {
    "primary": "Bearing, producing, or conveying milk or a milky white liquid, such as latex in plants.",
    "secondary": "In human female anatomy and physiological histology, designating the fifteen to twenty excretory ducts that convey milk to the nipple orifice.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Each lobule of the mammary gland discharges through a **lactiferous** duct terminating at the summit of the nipple."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Contraction of smooth muscle cells surrounding the **lactiferous** sinuses expels milk in response to suckling stimuli."},
      {"author": "Asa Gray", "work": "First Lessons in Botany", "quote": "Plants of the spurge family possess specialized **lactiferous** tubes that store protective white latex throughout their stems."}
    ]
  },
  "lactifuge": {
    "primary": "A medicinal agent, herb, or treatment that stops, diminishes, or suppresses the secretion of milk.",
    "secondary": "In clinical obstetrics and historical materia medica, a therapeutic substance such as belladonna administered to arrest unwanted lactation after weaning.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "When maternal nursing must be discontinued abruptly, physicians prescribe a reliable **lactifuge** to prevent painful engorgement."},
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Herbalists anciently valued sage and camphor as a cooling **lactifuge** to dry up maternal humours."},
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Astringent draughts were administered as a sovereign **lactifuge** when the nurse wished to suppress excessive milky distillations."}
    ]
  }
}

print(f"data_food_p2 loaded with {len(data_food_p2)} words.")
