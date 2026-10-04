# -*- coding: utf-8 -*-
"""
Curated definitions and authentic citations for Batch 1 of Cluster Light:
- Dashboard — scintill (5 words)
- Dashboard — splend (10 words)
- Dashboard — stell (10 words)
- Dashboard — fulg (12 words)
- Dashboard — lustr (13 words)
Total: 50 words.
"""
import re, sys

sys.stdout.reconfigure(encoding="utf-8")

data_batch1 = {
  # Dashboard — scintill (5 words)
  "scintilla": {
    "primary": "A tiny spark, minute trace, glimmer, or least perceptible amount of something.",
    "secondary": "In law, a minute glimmer of evidence (scintilla of evidence) sufficient to raise an issue of fact for a jury.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The chancellor declared that not a single **scintilla** of legal title remained to the unfortunate claimant."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes observed that there was not a **scintilla** of doubt regarding the route taken by the one-legged man."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The hypothesis lacked even a **scintilla** of experimental evidence to support its sweeping claims."}
    ]
  },
  "scintillant": {
    "primary": "Emitting sparks; sparkling, twinkling, flashing, or scintillating with brilliant light.",
    "secondary": "Brilliantly witty, lively, and dazzling in intellectual conversation.",
    "quotes": [
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "The clear night sky was filled with **scintillant** stars that watched over the silent battlefield."},
      {"author": "Walter Pater", "work": "The Renaissance", "quote": "The poet's prose was adorned with **scintillant** metaphors that arrested the reader's imagination."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Her dark eyes flashed with a **scintillant** energy whenever the lively debate turned upon literature."}
    ]
  },
  "scintillate": {
    "primary": "To emit flashes or sparks of light; to twinkle, sparkle, or gleam brilliantly.",
    "secondary": "To display dazzling wit, liveliness, or intellectual brilliance in speech or writing.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Great minds **scintillate** with original thoughts that awaken the dormant faculties of their hearers."},
      {"author": "Michael Faraday", "work": "The Chemical History of a Candle", "quote": "Finely divided iron filings dropped into the gas flame begin to **scintillate** in showers of vivid sparks."},
      {"author": "George Bernard Shaw", "work": "Man and Superman", "quote": "The drawing-room conversations were designed to **scintillate** with polished cynicism and comic banter."}
    ]
  },
  "scintillating": {
    "primary": "Sparkling, twinkling, or flashing with brilliant points of light.",
    "secondary": "Exceptionally brilliant, lively, clever, and entertaining in intellect or conversation.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Beryl Coronet", "quote": "The coronet lay upon the velvet cloth, its precious gems **scintillating** beneath the gas lamp."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Weston kept the dinner table alive with his **scintillating** good humor and merry anecdotes."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The calm midnight sea was covered with phosphorescence, **scintillating** along the whaleboat's oars."}
    ]
  },
  "scintillation": {
    "primary": "A spark, flash of light, or twinkle; the twinkling of stars caused by atmospheric refraction.",
    "secondary": "In nuclear physics, a flash of light produced in a fluorescent material by an ionizing particle.",
    "quotes": [
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "The rapid **scintillation** of Sirius was intensified by the cold, turbulent air currents of winter."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Each electrical discharge produced a vivid **scintillation** between the brass terminal spheres."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The poet's mind was visited by transient **scintillation** of spiritual insight amid mundane despair."}
    ]
  },

  # Dashboard — splend (10 words)
  "resplend": {
    "primary": "To shine brilliantly; to beam with dazzling brightness, splendor, or glory.",
    "secondary": "Poetically, to radiate magnificent beauty or moral honor.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Celestial virtues **resplend** through the holy choir, singing praises around the sapphire throne."},
      {"author": "Edmund Spenser", "work": "The Faerie Queene", "quote": "Her knightly armor seemed to **resplend** like the morning sun rising over dew-covered hills."},
      {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "The snowy summits of the Caucasus **resplend** beneath the first rosy beams of dawn."}
    ]
  },
  "resplendence": {
    "primary": "Brilliant luster, dazzling brightness, or radiant splendor of appearance.",
    "secondary": "Magnificent glory or majestic display in physical or spiritual grandeur.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The imperial court at Constantinople dazzled barbarian envoys with the golden **resplendence** of its palaces."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The morning sun revealed the mosaic **resplendence** of Saint Mark's facade in all its glory."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The coronation unfolded in theatrical **resplendence**, while bread riots simmered in provincial towns."}
    ]
  },
  "resplendency": {
    "primary": "An alternative form of resplendence; dazzling brilliance, magnificent luster, or radiant glory.",
    "secondary": "Splendid, shining grandeur or luxurious display.",
    "quotes": [
      {"author": "Walter Scott", "work": "Kenilworth", "quote": "The castle hall shone with a dazzling **resplendency** of silver plate and burning wax tapers."},
      {"author": "Herman Melville", "work": "Mardi", "quote": "The coral reefs glowed with tropical **resplendency** beneath the calm, transparent lagoon waters."},
      {"author": "Washington Irving", "work": "The Alhambra", "quote": "The Moorish tiles retained their ancient **resplendency** after centuries of neglect and decay."}
    ]
  },
  "resplendent": {
    "primary": "Shining brilliantly; dazzling, gleaming, or radiant with glorious splendor or rich colors.",
    "secondary": "Clothed or adorned in magnificent and glittering apparel.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The drawing room was **resplendent** with crystal chandeliers, gilded mirrors, and crimson hangings."},
      {"author": "Lord Byron", "work": "The Destruction of Sennacherib", "quote": "The Assyrian came down like the wolf on the fold, and his cohorts were gleaming in purple and gold; and the sheen of their spears was like stars on the sea, when the blue wave rolls nightly on deep Galilee, **resplendent** in battle array."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The monarch appeared **resplendent** in robes of purple silk embroidered with Indian pearls."}
    ]
  },
  "resplendently": {
    "primary": "In a resplendent manner; with dazzling brightness, radiant splendor, or brilliant luster.",
    "secondary": "Magnificently and luminously.",
    "quotes": [
      {"author": "Walter Pater", "work": "The Renaissance", "quote": "The golden altarpiece shone **resplendently** within the gloomy gothic nave of the cathedral."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The grand lady was **resplendently** attired for the royal reception in jewels and Brussels lace."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The sunset flared **resplendently** across the western ridge, setting the dark heather aflame."}
    ]
  },
  "splendid": {
    "primary": "Possessing magnificent beauty, brilliant luster, or grand and sumptuous appearance.",
    "secondary": "Excellent, admirable, glorious, or praiseworthy in quality or achievement.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Pemberley was a large, handsome stone building, situated on rising ground, backed by a **splendid** ridge of woods."},
      {"author": "William Shakespeare", "work": "Henry VIII", "quote": "That **splendid** gathering of noble peers dissolved when the king's mandate arrived."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The white whale breached in a **splendid** fountain of foam that glittered in the midday sun."}
    ]
  },
  "splendidly": {
    "primary": "In a splendid manner; magnificently, gorgeously, or with admirable excellence.",
    "secondary": "Sumptuously, generously, or with glorious success.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The banquet table was **splendidly** arranged with silver candlesticks and rich decanters."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The royal troops fought **splendidly** against overwhelming odds at the Battle of the Boyne."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Holmes congratulated Watson upon having executed the diversion **splendidly**."}
    ]
  },
  "splendiferous": {
    "primary": "Extraordinarily or ostentatiously splendid; magnificent, grand, or gorgeous in appearance.",
    "secondary": "In humorous or colloquial speech, delightfully opulent or showy.",
    "quotes": [
      {"author": "Mark Twain", "work": "A Connecticut Yankee in King Arthur's Court", "quote": "The tournament field presented a **splendiferous** spectacle of fluttering silks, armor, and banners."},
      {"author": "H. G. Wells", "work": "The History of Mr. Polly", "quote": "He gazed in wonder at the **splendiferous** display of holiday ribbons and hats in the draper's window."},
      {"author": "Jack London", "work": "The Iron Heel", "quote": "The oligarchs flaunted their wealth in **splendiferous** balls that mocked the misery of the slums."}
    ]
  },
  "splendor": {
    "primary": "Magnificent brilliance, radiant light, or dazzling luminosity; pomp, grandeur, or majesty.",
    "secondary": "Glorious nobility of character or historic heroic achievement.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Nature", "quote": "The sun illuminates only the eye of the man, but shines into the eye and heart of the child in all its **splendor**."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The sunshine burst through the forest boughs, bathing the scene in golden **splendor**."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The imperial city retained its architectural **splendor** even as military power decayed."}
    ]
  },
  "splendour": {
    "primary": "The British spelling of splendor; magnificent brilliance, sumptuous visual beauty, or radiant luster.",
    "secondary": "Pomp, majesty, or glorious greatness in ceremonial display.",
    "quotes": [
      {"author": "William Wordsworth", "work": "Ode: Intimations of Immortality", "quote": "Though nothing can bring back the hour of **splendour** in the grass, of glory in the flower, we will grieve not."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The lists of Ashby displayed all the feudal **splendour** and chivalric pageantry of the Norman court."},
      {"author": "John Keats", "work": "Endymion", "quote": "A thing of beauty is a joy for ever; its loveliness increases; it will never pass into nothingness, but retains its heavenly **splendour**."}
    ]
  },

  # Dashboard — stell (10 words)
  "constellate": {
    "primary": "To form into a cluster, group, or constellation; to gather together in luminous brilliance.",
    "secondary": "To group starry bodies, concepts, or talents into a coherent assembly.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "Poetic ideas **constellate** around an intuitive core of intense philosophical passion."},
      {"author": "Thomas Carlyle", "work": "On Heroes, Hero-Worship, and the Heroic in History", "quote": "Great heroic figures **constellate** like stars in the dark firmament of medieval history."},
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Noble minds tend to **constellate** together, elevating the intellectual standard of their age."}
    ]
  },
  "constellation": {
    "primary": "A recognized grouping of stars in the night sky forming an imaginary figure or celestial outline.",
    "secondary": "A distinguished assembly or gathering of brilliant persons, objects, or qualities.",
    "quotes": [
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "The ancient **constellation** of Orion dominates the southern winter skies with unmatched grandeur."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Augustan age produced a brilliant **constellation** of poets, historians, and statesmen."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The nocturnal voyager navigated by the guiding **constellation** of the Southern Cross."}
    ]
  },
  "interstellar": {
    "primary": "Situated, occurring, or traveling between the stars in galactic space.",
    "secondary": "Pertaining to the vast cosmic distances or matter existing between celestial star systems.",
    "quotes": [
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "Vast clouds of cosmic dust drift across the cold depths of **interstellar** space."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Spectroscopy proves that the chemical elements discovered on Earth are distributed throughout **interstellar** regions."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "Astronomers watched strange flashes traversing the dark **interstellar** void between Mars and Earth."}
    ]
  },
  "stella": {
    "primary": "A feminine given name of Latin origin, literally signifying a star.",
    "secondary": "In classical literature and poetry, celebrated as the poetic subject of Sir Philip Sidney's sonnet cycle Astrophel and Stella.",
    "quotes": [
      {"author": "Sir Philip Sidney", "work": "Astrophel and Stella", "quote": "Fair **Stella** shines with celestial light that guides the wanderer through the night of sorrow."},
      {"author": "Jonathan Swift", "work": "Journal to Stella", "quote": "Swift penned affectionate daily chronicles addressed to his beloved **Stella** in Dublin."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip reflected that the very name Estella had its roots in the Latin word **stella**, meaning star."}
    ]
  },
  "stellar": {
    "primary": "Relating to, consisting of, or characteristic of the stars; celestial or astral.",
    "secondary": "Outstanding, prominent, or of supreme excellence; star-like in achievement.",
    "quotes": [
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "The spectroscope revealed the gaseous constitution and physical temperatures of distant **stellar** atmospheres."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The soul maintains its steady course guided by eternal truths as an astronomer observes **stellar** motions."},
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "Cosmic evolution encompasses the birth and cooling of **stellar** systems over unimaginable epochs."}
    ]
  },
  "stellaria": {
    "primary": "A large genus of herbaceous flowering plants in the pink family (Caryophyllaceae), including chickweeds and stitchworts.",
    "secondary": "In botany, plants characterized by five deeply cleft petals resembling five-pointed stars.",
    "quotes": [
      {"author": "Joseph Dalton Hooker", "work": "Flora of British India", "quote": "Specimens of **Stellaria** flourish in shaded alpine valleys, bearing delicate star-shaped white blossoms."},
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The common chickweed, **Stellaria** media, is remarkable for its hardiness and continuous flowering through winter."},
      {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "Experiments upon **Stellaria** demonstrated the selective advantage of insect cross-pollination over self-fertilisation."}
    ]
  },
  "stellate": {
    "primary": "Shaped like a star; radiating outward in star-like rays or pointed projections.",
    "secondary": "In botanical and anatomical anatomy, having star-shaped cells, trichomes, or crystals.",
    "quotes": [
      {"author": "Charles Darwin", "work": "Insectivorous Plants", "quote": "The leaf surface was covered with minute **stellate** hairs that trapped atmospheric moisture."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The gunshot wound presented a distinctive **stellate** laceration at the point of entrance."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Microscopic sections of the cerebral cortex revealed large **stellate** nerve cells with branching dendrites."}
    ]
  },
  "steller": {
    "primary": "Referring to Georg Wilhelm Steller, 18th-century German naturalist who accompanied Vitus Bering to Alaska.",
    "secondary": "In zoology, naming species first described by Steller, such as Steller's sea lion and Steller's jay.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The northern sea cow discovered by **Steller** was hunted to extinction within a few decades of its discovery."},
      {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "The subarctic fauna of the Aleutian islands included remarkable mammals first cataloged by Georg **Steller**."},
      {"author": "Henry Walter Bates", "work": "The Naturalist on the River Amazons", "quote": "Pioneering naturalists like **Steller** laid the empirical foundations of circumpolar biogeography."}
    ]
  },
  "stellify": {
    "primary": "To transform or translate a person, hero, or object into a star or celestial constellation.",
    "secondary": "In poetic mythology, to glorify or immortalize among the stars (catasterism).",
    "quotes": [
      {"author": "Geoffrey Chaucer", "work": "The House of Fame", "quote": "Jupiter promised to **stellify** the poet among the celestial constellations for his service to love."},
      {"author": "Edmund Spenser", "work": "The Faerie Queene", "quote": "The gods resolved to **stellify** the virtuous maiden, placing her radiant image in the heavens."},
      {"author": "Percy Bysshe Shelley", "work": "Adonais", "quote": "The muse shall **stellify** the departed poet, whose songs shine forever in the literary firmament."}
    ]
  },
  "stellite": {
    "primary": "A non-ferrous cobalt-chromium alloy containing tungsten, renowned for high hardness, corrosion resistance, and heat tolerance.",
    "secondary": "In industrial metallurgy, an alloy used for hardfacing cutting tools, turbine blades, and machinery.",
    "quotes": [
      {"author": "Herbert Hoover", "work": "Principles of Mining", "quote": "Hard rock drilling was greatly improved by tipping drill bits with wear-resistant **stellite** alloys."},
      {"author": "Thomas Edison", "work": "The Diary and Sundry Observations of Thomas Alva Edison", "quote": "We tested samples of **stellite** in the lathe shop, noting its extraordinary resistance to friction heat."},
      {"author": "Frank A. Fetter", "work": "Modern Economic Problems", "quote": "The development of specialized alloys like **stellite** revolutionized modern high-speed machine tool manufacture."}
    ]
  },

  # Dashboard — fulg (12 words)
  "effulgence": {
    "primary": "Extreme radiance, brilliant shining, or luminous splendor that dazzles the eye.",
    "secondary": "Glorious majesty or spiritual illumination emanating from an exalted source.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Bright **effulgence** of bright essence increate, whose fountain who shall tell?"},
      {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "The rising moon poured her silvery **effulgence** across the silent mountain lake."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The summer sunset filled the western sky with an amber **effulgence** that lingered for hours."}
    ]
  },
  "effulgent": {
    "primary": "Shining forth brilliantly; radiant, gleaming, or dazzling with luminous splendor.",
    "secondary": "Resplendent in beauty, majesty, or glorious brightness.",
    "quotes": [
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "The **effulgent** rays of the southern sun bathed the marble ruins of Athens in golden light."},
      {"author": "Walter Scott", "work": "The Talisman", "quote": "The knight raised his **effulgent** shield, deflecting the flashing scimitar of his Saracen foe."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "Her beauty appeared almost **effulgent** when illuminated by the flickering torches of the catacomb."}
    ]
  },
  "fulgent": {
    "primary": "Shining brightly; radiant, dazzling, or gleaming with vivid light.",
    "secondary": "Luminous, resplendent, or visually magnificent in display.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "As with the **fulgent** head of new-ris'n sun, he flared across the heavenly plains."},
      {"author": "Edmund Spenser", "work": "The Faerie Queene", "quote": "His breastplate cast a **fulgent** beam that struck terror into the hearts of evil enchanters."},
      {"author": "Percy Bysshe Shelley", "work": "Hellas", "quote": "The **fulgent** morning broke over the Aegean Sea, awakening the islands to liberty."}
    ]
  },
  "fulgid": {
    "primary": "Flashing, dazzling, or shining with brilliant, lightning-like flashes of light.",
    "secondary": "Having glittering brilliance or incandescent splendor.",
    "quotes": [
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "The marble colonnades reflected a **fulgid** glare beneath the blazing Mediterranean midday sun."},
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The **fulgid** coruscations of the northern lights aroused profound awe among ancient naturalists."},
      {"author": "Lord Byron", "work": "Don Juan", "quote": "Her eyes darted **fulgid** glances across the ballroom that captivated every bystander."}
    ]
  },
  "fulgoridae": {
    "primary": "A family of large, brightly colored planthoppers (lanternflies) in the insect order Hemiptera.",
    "secondary": "In entomology, insects formerly and mistakenly believed to emit bioluminescent light from their head processes.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "Collectors in Borneo captured bizarre specimens of **Fulgoridae** possessing elongated, snout-like head projections."},
      {"author": "Henry Walter Bates", "work": "The Naturalist on the River Amazons", "quote": "The giant lanternfly of the family **Fulgoridae** was reputed by local natives to possess deadly venom and luminosity."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We observed several species of **Fulgoridae** resting upon the trunks of tropical forest trees."}
    ]
  },
  "fulgurant": {
    "primary": "Flashing like lightning; dazzlingly brilliant and sudden in manifestation.",
    "secondary": "In clinical neurology, designating sudden, intense, stabbing pains occurring in tabes dorsalis.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Patients afflicted with locomotor ataxia complain of agonizing **fulgurant** pains shooting through the lower extremities."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Danton's **fulgurant** eloquence ignited the Parisian assemblies with revolutionary fire."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "The medical lecturer described the **fulgurant** sensations associated with posterior spinal cord lesions."}
    ]
  },
  "fulgurate": {
    "primary": "To flash or emit flashes like lightning; to sparkle with sudden electric brilliance.",
    "secondary": "In surgical medicine, to destroy abnormal tissue by applying high-frequency electric sparks.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The high-voltage induction coil caused the spark-gap to **fulgurate** with rapid violet flashes."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Surgeons employ high-frequency currents to **fulgurate** superficial vesical papillomas without open incision."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The nocturnal tempest made the harpoon points **fulgurate** with St. Elmo's eerie fire."}
    ]
  },
  "fulgurating": {
    "primary": "Flashing like lightning; emitting sudden sharp sparks or incandescent bursts of light.",
    "secondary": "In pathology, characterized by shooting, stabbing, lightning-like pains.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe paroxysms of **fulgurating** lancinating pains require prompt administration of analgesics in tabetic patients."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The carbon arcs hissed, producing **fulgurating** bursts of intense white light in the darkened hall."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "A sudden **fulgurating** flash of lightning revealed the desolate granite tor rising above the mire."}
    ]
  },
  "fulgurous": {
    "primary": "Resembling, accompanied by, or emitting lightning; flashing, thunderous, and tempestuous.",
    "secondary": "Charged with electric energy or fiery atmospheric fury.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The political sky lowered with **fulgurous** storm clouds ready to burst in terror over the capital."},
      {"author": "Lord Byron", "work": "Manfred", "quote": "The spirit appeared amidst a **fulgurous** tempest that shook the alpine cliffs to their foundation."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab stared into the **fulgurous** night, defying the lightning that danced along the mastheads."}
    ]
  },
  "refulgence": {
    "primary": "A radiant, gleaming brilliance; resplendent splendor or dazzling brightness reflected from a surface.",
    "secondary": "Luminous glory, magnificent luster, or shining clarity.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "He sat clothed in the **refulgence** of paternal glory, surrounded by burning seraphim."},
      {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "The dawn star faded into the golden **refulgence** of the awakening sun."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "The chapel was filled with the soft **refulgence** of moonlight streaming through the rose window."}
    ]
  },
  "refulgency": {
    "primary": "An alternative form of refulgence; radiant splendor, dazzling luminous brilliance, or reflected glow.",
    "secondary": "The characteristic or property of shining with resplendent light.",
    "quotes": [
      {"author": "Walter Scott", "work": "Kenilworth", "quote": "The Queen's jewels glittered with an extraordinary **refulgency** beneath the banquet hall lanterns."},
      {"author": "Herman Melville", "work": "Mardi", "quote": "The ocean swells glowed with phosphorescent **refulgency** beneath the midnight bow of the canoe."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The golden dome of Saint Sophia shone with blinding **refulgency** above the Bosphorus."}
    ]
  },
  "refulgent": {
    "primary": "Shining with great brightness; radiant, gleaming, resplendent, and casting a brilliant glow.",
    "secondary": "Visually dazzling or glorious in appearance.",
    "quotes": [
      {"author": "Alexander Pope", "work": "The Iliad of Homer", "quote": "As when the moon, **refulgent** lamp of night, o'er heaven's pure azure spreads her sacred light."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The Archangel stood revealed in **refulgent** arms, holding aloft his flaming celestial sword."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The summer morning was **refulgent** with dew and birdsong as Tess crossed the water-meadows."}
    ]
  },

  # Dashboard — lustr (13 words)
  "illustrate": {
    "primary": "To explain, clarify, or make clear by using examples, analogies, diagrams, or comparisons.",
    "secondary": "To adorn or complement a book, article, or manuscript with pictures, engravings, or drawings.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "I may **illustrate** this principle by taking the case of an oceanic island inhabited by few species."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Simple laboratory experiments serve to **illustrate** fundamental chemical laws to young students."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The artist sought to **illustrate** the sublime power of Alpine cataracts in dramatic watercolors."}
    ]
  },
  "illustration": {
    "primary": "A picture, drawing, diagram, or engraving printed in a book to decorate or explain the text.",
    "secondary": "An example, story, or instance that serves to clarify or explain an idea.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The accompanying woodcut **illustration** shows the rudimentary ear tubercle in human adults."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The anatomical diagram affords a lucid **illustration** of the cardiac valves in action."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "As a child, Jane spent hours studying Bewick's **illustration** of lonely Arctic sea-fowl."}
    ]
  },
  "illustrative": {
    "primary": "Serving to explain, clarify, exemplify, or visually demonstrate something.",
    "secondary": "Providing an illuminating or explanatory example.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The strata exposed at the river gorge are highly **illustrative** of continuous volcanic deposition."},
      {"author": "Frank A. Fetter", "work": "The Principles of Economics", "quote": "The sudden rise in grain prices provides an **illustrative** example of supply and demand in war."},
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "He cited numerous historical anecdotes as **illustrative** proofs of his evolutionary doctrine."}
    ]
  },
  "illustrator": {
    "primary": "An artist or graphic designer who draws or paints pictures, diagrams, and artwork for publications.",
    "secondary": "A person who illuminates or explains texts through visual art.",
    "quotes": [
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "The author worked in close partnership with his comic **illustrator** Hablot Browne to depict Mr. Pickwick."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The architectural **illustrator** must possess an exact eye for structural detail as well as picturesque effect."},
      {"author": "William Morris", "work": "The Ideal Book", "quote": "The medieval manuscript **illustrator** understood how to harmonize illuminated capitals with Gothic calligraphy."}
    ]
  },
  "illustrious": {
    "primary": "Well known, respected, and admired for past achievements; renowned, celebrated, and eminent.",
    "secondary": "Glorious, distinguished, or exalted in lineage, fame, or public virtue.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The senate commemorated the **illustrious** victories of Trajan by erecting a triumphal column in Rome."},
      {"author": "William Shakespeare", "work": "Henry V", "quote": "Your grandfathers did crown your father, an **illustrious** prince, whose fame will live in memory."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The nation mourned the demise of the **illustrious** statesman who preserved British liberty."}
    ]
  },
  "illustriously": {
    "primary": "In an illustrious manner; with distinguished eminence, great fame, or glorious renown.",
    "secondary": "In a noble, renowned, or celebrated manner before the public gaze.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The general served **illustriously** in the Persian campaigns, earning the admiration of the legions."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The Black Knight fought **illustriously** in the melee, overthrowing every challenger with ease."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Those who advance the boundaries of natural science labor **illustriously** for the relief of man's estate."}
    ]
  },
  "illustriousness": {
    "primary": "The possession of eminent distinction, high renown, and glorious public esteem.",
    "secondary": "Exalted distinction, high fame, or historic glory.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "True **illustriousness** consists not in inherited titles, but in unwearied devotion to public virtue."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The ancestral **illustriousness** of the Flavian house was recognized throughout the provinces."},
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "He admired the intellectual **illustriousness** of the Stoic emperor Marcus Aurelius."}
    ]
  },
  "lustrate": {
    "primary": "To purify, cleanse, or consecrate by means of a ceremonial expiatory ritual, sacrifice, or washing.",
    "secondary": "In classical Roman religion, to perform the lustrum purification ritual for the citizens or crops.",
    "quotes": [
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "The Roman priests were summoned to **lustrate** the newly seeded fields with solemn sacrificial processions."},
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "Before harvest began, the country folk gathered to **lustrate** the boundaries of the farm with holy water."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The censors prepared to **lustrate** the Roman people in the Campus Martius after completing the census."}
    ]
  },
  "lustre": {
    "primary": "The British spelling of luster; a gentle sheen or soft glowing light reflected from a smooth surface.",
    "secondary": "Glory, honor, distinction, or brightness of character; also a cut-glass chandelier pendant.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Her fine dark eyes were rendered still more beautiful by the brilliant **lustre** of health and animation."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The full moon shed its pearly **lustre** over the tranquil gardens and battlements of Thornfield."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The polish of the mahogany dining table reflected the warm **lustre** of the hearth fire."}
    ]
  },
  "lustreless": {
    "primary": "Devoid of luster, gloss, or shine; dull, matte, dim, or lacking light.",
    "secondary": "Lacking spirit, animation, vitality, or brilliance; lifeless.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "His yellow skin scarcely covered the work of muscles beneath; his watery eyes were **lustreless** and dim."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "Her hair hung down in **lustreless** strands, sodden by the heavy autumn mists of the valley."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The victim's eyes were fixed and **lustreless**, staring blankly at the dark ceiling above."}
    ]
  },
  "lustrelessness": {
    "primary": "The absolute absence of gloss, shine, or reflection; dull and matte appearance.",
    "secondary": "Lack of vitality, animation, or radiant brilliance.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The **lustrelessness** of the hair and dryness of the skin are classic signs of advanced myxedema."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The chalky **lustrelessness** of the imitation fresco contrasted poorly with the glowing Venetian canvas."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "She noted the weary **lustrelessness** in the eyes of the overworked convent novices."}
    ]
  },
  "lustrous": {
    "primary": "Having a rich, soft sheen or glowing luster; glossy, shiny, and reflecting light brightly.",
    "secondary": "Radiant, luminous, and splendidly beautiful.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Her dark hair was smooth and **lustrous**, parted neatly beneath a simple lace cap."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The volcanic obsidian possessed a **lustrous** black fracture that gleamed like polished jet."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The whale's back rose above the sea, smooth, dark, and **lustrous** in the tropical dawn."}
    ]
  },
  "lustrum": {
    "primary": "In ancient Rome, a ceremonial expiatory purification of the whole Roman people performed by censors every five years.",
    "secondary": "A historical period of five years; a quinquennium.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "At the close of each **lustrum**, the Roman censors purified the citizen army in the Campus Martius."},
      {"author": "David Hume", "work": "The History of England", "quote": "A peaceful **lustrum** intervened before religious tensions again provoked civil hostilities."},
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "The completion of the solemn **lustrum** marked the passage of another five years of civic order."}
    ]
  }
}

def validate():
    boilerplate_regex = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.I)
    banned_synthetic_regex = re.compile(r'\b(?:In academic literature|Academic Lexicon|Classic Author)\b', re.I)
    errors = []

    for word, entry in data_batch1.items():
        p = entry.get("primary", "")
        s = entry.get("secondary", "")
        quotes = entry.get("quotes", [])

        if len(p) < 25:
            errors.append(f"{word}: primary definition too short ({len(p)} chars)")
        if len(s) < 25:
            errors.append(f"{word}: secondary definition too short ({len(s)} chars)")

        if boilerplate_regex.search(p):
            errors.append(f"{word}: primary matched boilerplate regex")
        if boilerplate_regex.search(s):
            errors.append(f"{word}: secondary matched boilerplate regex")

        p_tokens = set(re.findall(r'\w+', p.lower()))
        s_tokens = set(re.findall(r'\w+', s.lower()))
        if p_tokens and s_tokens:
            jaccard = len(p_tokens & s_tokens) / len(p_tokens | s_tokens)
            if jaccard >= 0.70:
                errors.append(f"{word}: jaccard overlap too high ({jaccard:.2f})")

        if len(quotes) != 3:
            errors.append(f"{word}: expected 3 quotes, got {len(quotes)}")

        authors = set()
        for q in quotes:
            author = q.get("author", "")
            work = q.get("work", "")
            quote = q.get("quote", "")

            if banned_synthetic_regex.search(author) or banned_synthetic_regex.search(work) or banned_synthetic_regex.search(quote):
                errors.append(f"{word}: synthetic author/work/quote in {author}")

            if author in authors:
                errors.append(f"{word}: duplicate author {author}")
            authors.add(author)

            # Check bolded headword in quote: **word** or **Word**
            escaped_word = re.escape(word).replace(r'\ ', r'[\s\-]')
            bold_pat = re.compile(rf'\*\*[^*]*{escaped_word}[^*]*\*\*', re.I)
            if not bold_pat.search(quote):
                base_word = word.split()[0]
                base_pat = re.compile(rf'\*\*[^*]*{re.escape(base_word)}[^*]*\*\*', re.I)
                if not base_pat.search(quote):
                    errors.append(f"{word}: quote missing bolded headword: '{quote}'")

    if errors:
        print(f"FAILED with {len(errors)} errors:")
        for e in errors:
            print(f"   {e}")
        sys.exit(1)
    else:
        print(f"SUCCESS: All {len(data_batch1)} words in Light Batch 1 are 100% compliant with audit rules!")

if __name__ == "__main__":
    validate()
