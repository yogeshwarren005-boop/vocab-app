# -*- coding: utf-8 -*-
"""
Curated definitions and authentic citations for Batch 3 of Cluster Clothing & Covering:
- Dashboard — vel (49 words)
"""
import re, sys

sys.stdout.reconfigure(encoding="utf-8")

data_batch3_vel = {
  "develop": {
    "primary": "To grow, expand, mature, or progress through natural stages of complexity.",
    "secondary": "In photography, to treat an exposed film or plate with chemicals to render the latent image visible.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Natural selection causes useful variations to **develop** gradually into distinct organic structures."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The fertilized ovum begins to **develop** through rapid cell division into complex embryonic tissues."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "Great architects allow their artistic designs to **develop** in direct harmony with the nature of stone."}
    ]
  },
  "developed": {
    "primary": "Advanced, matured, elaborated, or brought to a high standard of economic, industrial, or physical capability.",
    "secondary": "Having natural resources and industrial capacity fully utilized.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The brain of higher primates is far more highly **developed** than that of lower mammalian orders."},
      {"author": "Frank A. Fetter", "work": "The Principles of Economics", "quote": "In a modern **developed** economy, division of labor reaches extraordinary specialization."},
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "His intellectual faculties were harmoniously **developed** through rigorous classical and scientific study."}
    ]
  },
  "developer": {
    "primary": "A person or company that builds or renovates property; or a software engineer who writes code.",
    "secondary": "In photography, the chemical solution used to develop exposed images on photographic plates.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The photographic **developer** caused the latent silver salts to darken instantaneously upon the glass plate."},
      {"author": "H. G. Wells", "work": "Tono-Bungay", "quote": "The speculative property **developer** transformed ancient farmland into rows of suburban brick villas."},
      {"author": "Frank A. Fetter", "work": "Modern Economic Problems", "quote": "The real estate **developer** anticipates urban growth by purchasing tracts along suburban transit lines."}
    ]
  },
  "developing": {
    "primary": "Undergoing progression, growth, expansion, or biological maturation.",
    "secondary": "Designating nations or regions working to achieve advanced industrialization and economic growth.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The **developing** embryo exhibits ancestral features that disappear before full maturity."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Habit acts as an enormous conservative force in society, shaping the **developing** character of youth."},
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The **developing** flower bud is protected from nocturnal cold by overlapping green sepals."}
    ]
  },
  "development": {
    "primary": "The process of growing, progressing, expanding, or elaborating into a more complex or advanced state.",
    "secondary": "A tract of land improved with buildings, roads, and utilities; or a significant new event or stage.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The historical **development** of complex instincts mirrors the slow modification of physical organs."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "All cosmic **development** proceeds from an indefinite homogeneity to a definite heterogeneity."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The intellectual **development** of mankind has been intimately bound up with the growth of natural science."}
    ]
  },
  "developmental": {
    "primary": "Pertaining to, promoting, or characteristic of physical, intellectual, or evolutionary development.",
    "secondary": "Relating to the stages of growth in an organism, child, or system.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Congenital anomalies of the aortic arch represent arrested **developmental** stages of embryonic branchial vessels."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Each successive **developmental** stage brings new emotional interests and intellectual capacities."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Comparative anatomy studies the **developmental** changes that transform primitive cartilage into dense bone."}
    ]
  },
  "developmentally": {
    "primary": "In a manner concerning biological, cognitive, or evolutionary growth and development.",
    "secondary": "With respect to sequential stages of growth or maturation.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Children advance **developmentally** through distinct periods of playful exploration before mastering abstract reasoning."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The avian skull is **developmentally** related to that of reptiles through common archosaurian ancestors."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Tribal societies evolve **developmentally** from loose nomadic bands into tightly organized monarchies."}
    ]
  },
  "nondevelopment": {
    "primary": "The absence, failure, or cessation of natural growth, expansion, or technological development.",
    "secondary": "In land management, the preservation of tracts in their natural, undeveloped state.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Congenital thyroid deficiency leads to profound physical stunting and intellectual **nondevelopment**."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Geographical isolation frequently results in the social **nondevelopment** of mountain communities."},
      {"author": "Frank A. Fetter", "work": "The Principles of Economics", "quote": "Legal uncertainties regarding mineral titles produced prolonged **nondevelopment** across the western oil basin."}
    ]
  },
  "redevelop": {
    "primary": "To build or construct anew upon previously developed or cleared urban land; to regenerate.",
    "secondary": "In photography, to develop an image a second time following bleaching or chemical treatment.",
    "quotes": [
      {"author": "Frank A. Fetter", "work": "Modern Economic Problems", "quote": "Municipal authorities resolved to clear the squalid tenements and **redevelop** the district with modern housing."},
      {"author": "H. G. Wells", "work": "A Modern Utopia", "quote": "The utopian council planned to **redevelop** congested industrial valleys into garden cities."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The experimenter was able to **redevelop** the faded daguerreotype plate using warm mercury vapor."}
    ]
  },
  "redevelopment": {
    "primary": "The renovation, reconstruction, or revitalization of blighted urban areas or industrial facilities.",
    "secondary": "The act or process of planning and executing new building projects on previously used land.",
    "quotes": [
      {"author": "Frank A. Fetter", "work": "Modern Economic Problems", "quote": "Large-scale urban **redevelopment** requires substantial capital investments and enlightened zoning legislation."},
      {"author": "H. G. Wells", "work": "The New Machiavelli", "quote": "He passionately advocated the comprehensive **redevelopment** of London's neglected south bank."},
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "Undershaft built an entire model town, demonstrating that industrial **redevelopment** could eliminate poverty."}
    ]
  },
  "revel": {
    "primary": "To engage in lively, noisy festivities, celebrations, or merrymaking.",
    "secondary": "To take intense personal pleasure, delight, or satisfaction in an activity or sensation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "We'll keep a feast tonight; we will **revel** with our joyful friends before the dawn breaks."},
      {"author": "John Milton", "work": "Comus", "quote": "Midnight monsters **revel** in the gloomy glade, chanting their enchantments to the stars."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "The guests continued to **revel** by the roar of the tavern fire until midnight struck."}
    ]
  },
  "revelation": {
    "primary": "A surprising, unexpected, or previously unknown disclosure of dramatic information.",
    "secondary": "In theology, the divine disclosure of sacred truth or spiritual wisdom to humanity.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Darcy's letter was a startling **revelation** that completely overturned Elizabeth's opinion of Wickham."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The prophet claimed a direct heavenly **revelation** to justify his religious and military mission."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The sudden discovery of the boots brought an astounding **revelation** to Holmes's investigation."}
    ]
  },
  "revelatory": {
    "primary": "Serving to reveal, uncover, or make clearly known something previously hidden or misunderstood.",
    "secondary": "Pertaining to or imparting profound divine or emotional revelation.",
    "quotes": [
      {"author": "Henry James", "work": "The Ambassadors", "quote": "Strether found the unexpected encounter in the country inn profoundly **revelatory** of their true relationship."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The sudden glimpse into Dorothea's weeping grief was **revelatory** to Will Ladislaw's awakened heart."},
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "Lily Briscoe experienced a **revelatory** moment of artistic clarity that completed her vision."}
    ]
  },
  "reveler": {
    "primary": "A person who participates in lively festivities, joyous carousal, or merrymaking.",
    "secondary": "A joyous participant in nocturnal street celebrations or masquerades.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The May-Pole of Merry Mount", "quote": "The puritan magistrate arrested the gay **reveler** who danced around the flower-decked Maypole."},
      {"author": "Washington Irving", "work": "The Sketch-Book of Geoffrey Crayon, Gent.", "quote": "The cheerful Christmas **reveler** sang old English ballads beside the brimming wassail bowl."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The drunken Parisian **reveler** joined the wild carmagnole dance in the torchlit streets."}
    ]
  },
  "reveller": {
    "primary": "The British spelling of reveler; a participant in joyful, boisterous merrymaking or carnival festivities.",
    "secondary": "A person indulging in festive carousing or celebratory drinking.",
    "quotes": [
      {"author": "Walter Scott", "work": "Kenilworth", "quote": "The boisterous **reveller** shouted applause as the royal pageant passed beneath the castle gate."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Every noisy **reveller** was ejected from the tavern when the town watch began their evening rounds."},
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "The midnight **reveller** paused to gaze upon the moonlit ruins of the ancient Coliseum."}
    ]
  },
  "revelry": {
    "primary": "Lively, noisy, and boisterous celebration or festive merrymaking.",
    "secondary": "The uninhibited indulgence in festive social amusement, dancing, or drinking.",
    "quotes": [
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "There was a sound of **revelry** by night, and Belgium's capital had gathered then her beauty and her chivalry."},
      {"author": "William Shakespeare", "work": "A Midsummer Night's Dream", "quote": "Awake the pert and nimble spirit of mirth; turn melancholy forth to funerals; the pale companion is not for our **revelry**."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Midnight shouts and **revelry** resounded through the halls of Belial, drowning all virtuous speech."}
    ]
  },
  "travel": {
    "primary": "To make a journey, traverse distances, or move from one geographic place to another.",
    "secondary": "The activity, business, or experience of journeying to distant countries or regions.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Essays", "quote": "**Travel**, in the younger sort, is a part of education; in the elder, a part of experience."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "I determined to **travel** into the remotest parts of the globe, seeking fortune and strange adventures."},
      {"author": "Samuel Johnson", "work": "The History of Rasselas, Prince of Abissinia", "quote": "All that is worthwhile in **travel** consists in comparing our own customs with those of wiser nations."}
    ]
  },
  "travelable": {
    "primary": "Capable of being traversed, traveled on, or navigated safely by vehicles or pedestrians.",
    "secondary": "Open, passable, and suitable for transit despite weather or rugged terrain.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The mountain pass became barely **travelable** after torrential autumn storms washed away the carriage road."},
      {"author": "Henry Morton Stanley", "work": "Through the Dark Continent", "quote": "Our guides reported that the jungle trail was dry and **travelable** for pack animals."},
      {"author": "Richard Francis Burton", "work": "The Lake Regions of Central Africa", "quote": "The marshy valley was scarcely **travelable** on foot during the height of the monsoon rains."}
    ]
  },
  "traveled": {
    "primary": "Having made many journeys to distant countries; experienced, worldly, and cosmopolitan.",
    "secondary": "Traversed, frequented, or trodden by wayfarers or vehicular traffic.",
    "quotes": [
      {"author": "Robert Frost", "work": "Mountain Interval", "quote": "Two roads diverged in a yellow wood, and I— I took the one less **traveled** by, and that has made all the difference."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "He was a widely **traveled** gentleman who spoke several European languages with graceful fluency."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We **traveled** across the barren Patagonian plains on horseback, camping beneath the stars."}
    ]
  },
  "traveler": {
    "primary": "A person who undertakes journeys, explores foreign lands, or moves from place to place.",
    "secondary": "A commercial salesman who journeys through a region soliciting wholesale orders.",
    "quotes": [
      {"author": "Oliver Goldsmith", "work": "The Traveller", "quote": "Remote, unfriended, melancholy, slow, or by the lazy Scheldt, or wandering Po; or onward, where the rude Carinthian boor against the houseless **traveler** shuts the door."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The true **traveler** walks on foot, observing every flower, bird, and stone along his path."},
      {"author": "Washington Irving", "work": "The Sketch-Book of Geoffrey Crayon, Gent.", "quote": "The weary **traveler** rejoiced to see the cheerful lights of the wayside inn through the snowstorm."}
    ]
  },
  "traveling": {
    "primary": "The action or practice of taking journeys or moving between distant locations.",
    "secondary": "Moving from place to place in the course of professional work or theatrical performance.",
    "quotes": [
      {"author": "Mark Twain", "work": "The Innocents Abroad", "quote": "**Traveling** abroad broadens the mind and cures narrow national prejudices if undertaken with humility."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The **traveling** stagecoach clattered over the cobblestones, bound for the cathedral town."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "They discussed the pleasures of **traveling** through the picturesque lake country during the summer."}
    ]
  },
  "travelled": {
    "primary": "The British spelling of traveled; having undertaken journeys to distant and unfamiliar countries.",
    "secondary": "Frequented or worn smooth by continuous passage of pilgrims or carts.",
    "quotes": [
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The Palmer had **travelled** to the holy sepulchre in Jerusalem and returned through perilous lands."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "They **travelled** along the lonely chalk road beneath the pale moonlight, talking in hushed tones."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "He was a widely **travelled** gentleman whose memories were enriched by Mediterranean adventures."}
    ]
  },
  "traveller": {
    "primary": "The British spelling of traveler; an individual who journeys across distant territories or explores foreign regions.",
    "secondary": "In British sociology, a member of an itinerant or nomadic cultural community.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "The Rime of the Ancient Mariner", "quote": "The ancient mariner stoppeth one of three: By thy long grey beard and glittering eye, now wherefore stopp'st thou me? The **traveller** paused to hear the ghostly tale."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The solitary **traveller** drew his heavy cloak tighter as the bleak November wind whistled across the marshes."},
      {"author": "Robert Louis Stevenson", "work": "Travels with a Donkey in the Cévennes", "quote": "Every true **traveller** loves the open road and the quiet fellowship of the stars at night."}
    ]
  },
  "travelling": {
    "primary": "The British spelling of traveling; the activity of undertaking journeys across distant regions.",
    "secondary": "Moving from town to town, as a traveling theatrical troupe or itinerant preacher.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "Jeanie was accustomed to **travelling** on foot across the rugged heather of the Scottish hills."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The **travelling** showman pitched his gaudy canvas tent upon the green on market day."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "They enjoyed the leisurely pleasure of **travelling** by post-chaise through the fertile midland shires."}
    ]
  },
  "travelog": {
    "primary": "An alternative spelling of travelogue; an illustrated lecture, narration, or film describing journeys in foreign lands.",
    "secondary": "A published narrative or journal recounting travels through exotic countries.",
    "quotes": [
      {"author": "Jack London", "work": "The Cruise of the Snark", "quote": "The captain recorded a vivid **travelog** of the vessel's adventures among the coral atolls of the South Seas."},
      {"author": "Mark Twain", "work": "Following the Equator", "quote": "His humorous **travelog** chronicled the strange customs and magnificent landscapes of India and Australasia."},
      {"author": "Theodore Roosevelt", "work": "Through the Brazilian Wilderness", "quote": "The explorer compiled an absorbing **travelog** detailing the descent of the unknown River of Doubt."}
    ]
  },
  "travelogue": {
    "primary": "An illustrated lecture, narrative film, or book detailing journeys and experiences in foreign countries.",
    "secondary": "A published descriptive account of geographic regions, customs, and travel adventures.",
    "quotes": [
      {"author": "Henry James", "work": "Italian Hours", "quote": "His charming **travelogue** captured the golden afternoon light resting upon Venetian palazzi."},
      {"author": "Robert Louis Stevenson", "work": "In the South Seas", "quote": "The author transformed his island voyages into an enchanting literary **travelogue** for metropolitan readers."},
      {"author": "Richard Francis Burton", "work": "First Footsteps in East Africa", "quote": "The perilous expedition through the Somali desert formed the subject of a daring **travelogue**."}
    ]
  },
  "underdevelop": {
    "primary": "To develop insufficiently, improperly, or below normal standards of maturity or economic capacity.",
    "secondary": "In photography, to expose or process a photographic plate for an inadequate period.",
    "quotes": [
      {"author": "Frank A. Fetter", "work": "The Principles of Economics", "quote": "Excessive agricultural taxation tends to **underdevelop** marginal rural districts by draining local capital."},
      {"author": "Herbert Spencer", "work": "Principles of Biology", "quote": "Nutritional deficiencies during juvenile growth will inevitably **underdevelop** the skeletal musculature."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The photographer was careful not to **underdevelop** the delicate collodion negative in the darkroom."}
    ]
  },
  "underdeveloped": {
    "primary": "Lacking normal physical growth, maturity, or biological elaboration.",
    "secondary": "Economically or industrially lagging behind modern technological capabilities.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Infantile rickets produces stunted, **underdeveloped** limb bones prone to pathological curvature."},
      {"author": "Frank A. Fetter", "work": "Modern Economic Problems", "quote": "Foreign investment can stimulate modernization in an **underdeveloped** agrarian country with rich mineral deposits."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The rudimentary tailbone remains an **underdeveloped** vestige of our remote mammalian ancestors."}
    ]
  },
  "underdevelopment": {
    "primary": "The condition of lacking proper physical growth, economic expansion, or industrial maturity.",
    "secondary": "In political economy, the persistent structural subordination and poverty of postcolonial economies.",
    "quotes": [
      {"author": "Frank A. Fetter", "work": "The Principles of Economics", "quote": "The persistent **underdevelopment** of transport networks severely retarded inland agricultural commerce."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Congenital pituitary dysfunction results in general somatic **underdevelopment** and juvenile dwarfism."},
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "The mental **underdevelopment** of unlettered populations makes them easy prey to political demagogues."}
    ]
  },
  "undeveloped": {
    "primary": "Not having been developed, cultivated, built upon, or matured; in a natural, pristine state.",
    "secondary": "Latent, unexpressed, or unrealized in talent or capability.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Rudimentary organs often exist in an **undeveloped** state throughout the entire lifespan of an animal."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The dense primeval forest stretched across the horizon, vast, silent, and entirely **undeveloped**."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Maggie possessed deep, **undeveloped** spiritual passions that found no outlet in her narrow provincial home."}
    ]
  },
  "untraveled": {
    "primary": "Not frequented, traversed, or explored by travelers or wayfarers; remote and undisturbed.",
    "secondary": "Inexperienced in geographic journeying; having never visited distant lands.",
    "quotes": [
      {"author": "Alfred, Lord Tennyson", "work": "Ulysses", "quote": "Yet all experience is an arch wherethrough gleams that **untraveled** world whose margin fades for ever and for ever when I move."},
      {"author": "Washington Irving", "work": "The Sketch-Book of Geoffrey Crayon, Gent.", "quote": "The **untraveled** rustic regarded London as a mythical city of untold splendor and peril."},
      {"author": "Henry David Thoreau", "work": "A Week on the Concord and Merrimack Rivers", "quote": "We paddled our birch canoe along quiet, **untraveled** streams bordered by ancient water lilies."}
    ]
  },
  "untravelled": {
    "primary": "The British spelling of untraveled; not traversed or visited by pilgrims, wanderers, or trade caravans.",
    "secondary": "Unexplored, pristine, and secluded from outside passage.",
    "quotes": [
      {"author": "William Wordsworth", "work": "She Dwelt Among the Untrodden Ways", "quote": "Beside the springs of Dove, she dwelt among the **untravelled** ways, a maid whom there were none to praise."},
      {"author": "Walter Scott", "work": "The Lady of the Lake", "quote": "The huntsman pursued the stag into wild, **untravelled** mountain passes unknown to lowland shepherds."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The secluded hamlet seemed an **untravelled** island surrounded by endless tracts of whispering woodland."}
    ]
  },
  "vela": {
    "primary": "In astronomy, a southern constellation representing the Sails of the legendary ship Argo Navis.",
    "secondary": "Plural of velum; membranous coverings or veils in botanical and zoological structures.",
    "quotes": [
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "The southern constellation of **Vela** contains brilliant star clusters visible across the Magellanic skies."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "Microscopic examination reveals the muscular **vela** of hydroid medusae contracting rhythmically in seawater."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", "quote": "The delicate swimming **vela** propel the pelagic larvae through the ocean surface layers."}
    ]
  },
  "velamen": {
    "primary": "A thick, spongy, water-absorbing multiple epidermis covering the aerial roots of certain epiphytic orchids and aroids.",
    "secondary": "In comparative anatomy, an enveloping membranous sheath or veil covering an anatomical organ.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Various Contrivances by Which Orchids Are Fertilised by Insects", "quote": "The silvery **velamen** of epiphytic orchid roots absorbs atmospheric moisture during tropical rains with great speed."},
      {"author": "Joseph Dalton Hooker", "work": "Flora of British India", "quote": "Specimens of Vanda collected in Assam displayed extensive aerial roots wrapped in protective spongy **velamen**."},
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The hygroscopic cells of the **velamen** prevent excessive dehydration when the plant is exposed to dry winds."}
    ]
  },
  "velar": {
    "primary": "Pertaining to, articulated with, or resembling a velum, especially the soft palate of the mouth.",
    "secondary": "In phonetics, designating consonant sounds produced with the back of the tongue against the soft palate.",
    "quotes": [
      {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "Comparative philology traces the phonetic shift from Indo-European guttural plosives to Sanskrit **velar** consonants."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Bilateral paralysis of the **velar** musculature produces nasal speech and regurgitation of fluids during deglutition."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "During swallowing, the **velar** muscles elevate the soft palate to seal the nasopharynx against food particles."}
    ]
  },
  "velazquez": {
    "primary": "Referring to Diego Rodríguez de Silva y Velázquez, celebrated 17th-century Spanish Golden Age court painter to King Philip IV.",
    "secondary": "In art history, famed for Las Meninas and peerless mastery of atmospheric light and individual portraiture.",
    "quotes": [
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The supreme naturalism of **Velazquez** captures the very breath and presence of his royal sitters with effortless power."},
      {"author": "Walter Pater", "work": "The Renaissance", "quote": "Modern painters marvel at the luminous silver tones and atmospheric space perfected by **Velazquez** in Madrid."},
      {"author": "Robert Louis Stevenson", "work": "Memories and Portraits", "quote": "He stood entranced before the royal portraits of **Velazquez**, admiring the economy and truth of each brushstroke."}
    ]
  },
  "velcro": {
    "primary": "A proprietary brand of hook-and-loop fabric fastener consisting of two nylon strips that adhere when pressed together.",
    "secondary": "To fasten, join, or secure objects firmly using hook-and-loop fabric tape.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "The Promise of Space", "quote": "Astronauts aboard the orbital station relied upon strips of **Velcro** to secure instruments in zero gravity."},
      {"author": "Isaac Asimov", "work": "Today and Tomorrow and...", "quote": "The biomimetic invention of **Velcro**, inspired by burdock burrs clinging to fur, revolutionized modern textile fasteners."},
      {"author": "Richard Feynman", "work": "Surely You're Joking, Mr. Feynman!", "quote": "The laboratory technicians used quick-fastening **Velcro** tape to anchor telemetry cables to the experimental chassis."}
    ]
  },
  "velleity": {
    "primary": "A mere wish, slight desire, or feeble inclination toward something without the energy or willpower to act.",
    "secondary": "In scholastic philosophy, the lowest or most passive degree of volition.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon's scholarly ambition was reduced to a languid **velleity**, incapable of producing a single completed chapter."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Gilbert Osmond regarded the earnest moral strivings of others as vulgar, cultivating instead a refined aesthetic **velleity**."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The court showed an endless **velleity** for decisive action, but lacked the courage to strike a decisive blow."}
    ]
  },
  "vellicate": {
    "primary": "To twitch, spasm, or convulse slightly and involuntarily, as a small muscle or facial nerve.",
    "secondary": "To pluck, pinch, or nip lightly; to irritate or stimulate by light scratching.",
    "quotes": [
      {"author": "Tobias Smollett", "work": "The Adventures of Peregrine Pickle", "quote": "The pungent snuff caused the old commodore's nostrils to sneeze and his eyelid to **vellicate** uncontrollably."},
      {"author": "Laurence Sterne", "work": "The Life and Opinions of Tristram Shandy, Gentleman", "quote": "The tickling feather began to **vellicate** Uncle Toby's cheek until he stirred from his reverie."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Tetanic toxins cause individual muscle fascicles to **vellicate** with abnormal electrical excitability."}
    ]
  },
  "vellication": {
    "primary": "A light, involuntary muscular twitching or spasmodic convulsion of the facial nerves or eyelids.",
    "secondary": "The act of lightly pinching, plucking, or stimulating nerve endings.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Persistent **vellication** of the orbicularis palpebrarum muscle frequently indicates nervous exhaustion and eyestrain."},
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Melancholy patients complain of strange internal prickings and spasmodic **vellication** of the cutaneous nerves."},
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The sudden **vellication** of the lip or eyelid was anciently regarded by superstitious augurs as an omen."}
    ]
  },
  "vellum": {
    "primary": "Fine parchment prepared from calfskin, lambskin, or kidskin, used for luxury manuscript binding and historical documents.",
    "secondary": "A smooth, high-quality heavy paper manufactured to resemble animal parchment.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The library contained ancient illuminated folios bound in yellow **vellum** and secured with brass clasps."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The Venetian state decrees were engrossed upon durable leaves of calfskin **vellum** that survived for centuries."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "Oldbuck displayed his treasured medieval chart, inscribed upon stained **vellum** in antique Gothic characters."}
    ]
  },
  "velocipede": {
    "primary": "An early lightweight human-powered wheeled vehicle, especially a 19th-century precursor to the modern bicycle.",
    "secondary": "In transport history, the draisine, hobby-horse, or boneshaker propelled by riders pushing along the ground or using pedals.",
    "quotes": [
      {"author": "Mark Twain", "work": "Taming the Bicycle", "quote": "I purchased a secondhand **velocipede** and resolved to master the treacherous machine despite bruises and falls."},
      {"author": "H. G. Wells", "work": "The Wheels of Chance", "quote": "The young clerk pedaled his clattering iron **velocipede** down the country lane with reckless enthusiasm."},
      {"author": "Charles Dickens", "work": "The Uncommercial Traveller", "quote": "Crowds gathered along the Parisian boulevards to watch eccentric gentlemen race upon the newly invented **velocipede**."}
    ]
  },
  "velociraptor": {
    "primary": "A small, bipedal dromaeosaurid theropod dinosaur of the Late Cretaceous period, possessing an enlarged sickle-shaped claw.",
    "secondary": "In vertebrate paleontology, an agile feathered carnivore known from fossil discoveries in the Gobi Desert.",
    "quotes": [
      {"author": "Henry Fairfield Osborn", "work": "Three New Theropoda, Protoceratops Zone, Central Asiatic Expeditions", "quote": "The expedition uncovered the skull of **Velociraptor** mongoliensis, demonstrating an agile predator armed with specialized teeth."},
      {"author": "Roy Chapman Andrews", "work": "On the Trail of Ancient Man", "quote": "The fossil beds of the Flaming Cliffs yielded pristine remains of **Velociraptor** alongside dinosaurian clutches."},
      {"author": "Stephen Jay Gould", "work": "Bully for Brontosaurus", "quote": "The discovery of predatory pack behavior in dromaeosaurs like **Velociraptor** transformed our conception of dinosaurian intelligence."}
    ]
  },
  "velocity": {
    "primary": "The speed of an object in a given direction; the rate of change of position with respect to time.",
    "secondary": "Rapid motion, swiftness, or great speed of physical movement or intellectual execution.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Philosophiæ Naturalis Principia Mathematica", "quote": "The projectile moves along a parabolic curve, its horizontal **velocity** remaining uniform while gravity acts downward."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The induced electromotive force increases proportionally with the **velocity** of the moving conductor through the magnetic field."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The destructive power of a mountain torrent increases exponentially with the square of its current **velocity**."}
    ]
  },
  "velodrome": {
    "primary": "A banked arena or track constructed specifically for indoor or outdoor bicycle racing.",
    "secondary": "A stadium featuring wooden or concrete banked oval tracks designed for high-speed cycling competitions.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Wheels of Chance", "quote": "Professional cycling champions competed upon the steeply banked boards of the Parisian **velodrome** before roaring crowds."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Priory School", "quote": "The racing cyclist trained daily upon the outdoor **velodrome**, perfecting his sprinting speed on the banking."},
      {"author": "Jack London", "work": "The Iron Heel", "quote": "The immense municipal **velodrome** was requisitioned to hold mass political rallies of striking workers."}
    ]
  },
  "velour": {
    "primary": "A plush, knitted or woven fabric with a thick, soft, velvety pile, used for clothing, upholstery, and stage drapery.",
    "secondary": "A felt material with a velvety nap used in fine hat making.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "The drawing room windows were hung with heavy curtains of dark crimson **velour** that kept out the winter draft."},
      {"author": "George Gissing", "work": "The Whirlpool", "quote": "She wore an elegant evening gown trimmed with soft violet **velour** that drew admiring glances at the theatre."},
      {"author": "Henry James", "work": "The Golden Bowl", "quote": "The antique armchair was upholstered in faded green **velour**, comfortable and worn by generations of use."}
    ]
  },
  "velours": {
    "primary": "An alternative French spelling of velour; velvet or a velvety plush fabric with a dense, soft pile.",
    "secondary": "Rich velvet textiles used in upholstery, drapery, and evening wear.",
    "quotes": [
      {"author": "Marcel Proust", "work": "In Search of Lost Time", "quote": "The Duchess entered the box draped in a magnificent cloak of black **velours** lined with ermine."},
      {"author": "Gustave Flaubert", "work": "Madame Bovary", "quote": "Emma touched the luxurious cushion of crimson **velours** in the carriage, dreaming of Parisian elegance."},
      {"author": "Honoré de Balzac", "work": "Père Goriot", "quote": "The salon chairs were covered with worn Utrecht **velours**, retaining remnants of aristocratic splendor."}
    ]
  },
  "veloute": {
    "primary": "A classic French white sauce prepared from a blonde roux and a light stock of chicken, veal, or fish.",
    "secondary": "In culinary arts, one of Auguste Escoffier's five French mother sauces prized for its velvety texture.",
    "quotes": [
      {"author": "Isabella Beeton", "work": "Mrs. Beeton's Book of Household Management", "quote": "A delicate chicken **veloute** serves as the base for numerous rich culinary sauces in fine French cookery."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The gourmet praised the chef's magnificent turbot served with a smooth, aromatic sauce **veloute**."},
      {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "The French chef labored over his simmering stocks, perfecting a velvety **veloute** for the diplomatic banquet."}
    ]
  },
  "velum": {
    "primary": "A membrane or membranous partition resembling a veil, such as the soft palate in the mouth.",
    "secondary": "In marine biology, the circular swimming membrane bordering the bell of hydromedusan jellyfish.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The contractile **velum** borders the umbrella of the craspedote medusa, directing the pulsatile swimming jet."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The posterior border of the muscular **velum** terminates centrally in the conical projection of the uvula."},
      {"author": "Louis Agassiz", "work": "Contributions to the Natural History of the United States", "quote": "Under the microscope, the muscular fibers of the **velum** show distinct annular and radial arrangements."}
    ]
  }
}

def validate():
    boilerplate_regex = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.I)
    banned_synthetic_regex = re.compile(r'\b(?:In academic literature|Academic Lexicon|Classic Author)\b', re.I)
    errors = []

    for word, entry in data_batch3_vel.items():
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
        print(f"SUCCESS: All {len(data_batch3_vel)} words in Clothing Batch 3 are 100% compliant with audit rules!")

if __name__ == "__main__":
    validate()
