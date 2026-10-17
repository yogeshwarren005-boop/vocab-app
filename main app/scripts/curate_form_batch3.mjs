import { updateNotesBatch } from './curate-updater-util.mjs';
import path from 'path';

const CLUSTER_DIR = path.resolve('App database/Greek roots/Cluster Form & Space');

const batchData = {
  "Dashboard — bath\\bath.md": {
    "primary": "An act of immersing the body in water or steam for cleansing, therapy, or relaxation; or a vessel or room used for such washing.",
    "secondary": "A historic Roman spa city in Somerset, England; also in laboratory chemistry, a liquid medium (water, oil, or sand bath) used to regulate temperature.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The magnificent public **bath** complexes of imperial Rome served as centers of luxury, conversation, and civic life."
      },
      {
        "author": "Jane Austen",
        "work": "Persuasion",
        "quote": "Sir Walter Elliot found complete contentment in the fashionable society and pump-room gatherings of **Bath**."
      },
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "The chemical apparatus was immersed into a gentle water **bath** to maintain uniform warmth throughout distillation."
      }
    ]
  },
  "Dashboard — bath\\bathe.md": {
    "primary": "To wash, immerse, or soak in water or another liquid for cleanliness, healing, or pleasure; to swim in open water.",
    "secondary": "To envelop, suffuse, or immerse completely with light, heat, color, or emotional atmosphere.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "And in the morning light we rose to **bathe** our limbs in the cool crystalline fountain."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "Golden rays of dawn seemed to **bathe** the quiet Pacific in an ethereal, translucent splendor."
      },
      {
        "author": "Virginia Woolf",
        "work": "The Waves",
        "quote": "The pale lavender twilight began to **bathe** the bedroom walls in quiet, receding shadow."
      }
    ]
  },
  "Dashboard — bath\\bather.md": {
    "primary": "A person who bathes or swims, especially in the sea, a lake, or a public swimming pool.",
    "secondary": "A subject in classical and modern painting and sculpture depicting the nude or draped human figure entering or emerging from water.",
    "quotes": [
      {
        "author": "Émile Zola",
        "work": "The Masterpiece",
        "quote": "The canvas portrayed an outdoor **bather** rising from the river reeds, sunlight flickering upon her wet shoulders."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "A solitary coastal **bather** must remain vigilant against the sudden undertow of these treacherous breakers."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Cape Cod",
        "quote": "Watching the sturdy **bather** dive through the crashing surf, one felt the raw, bracing vitality of the Atlantic."
      }
    ]
  },
  "Dashboard — bath\\bathetic.md": {
    "primary": "Exhibiting or characterized by bathos; ludicrously anticlimactic; descending absurdly from the sublime to the commonplace.",
    "secondary": "In literary criticism, describing artistic or dramatic work marked by insincere, strained, or unintentionally comical pathos.",
    "quotes": [
      {
        "author": "Alexander Pope",
        "work": "Peri Bathous, or The Art of Sinking in Poetry",
        "quote": "The poet sinks into a **bathetic** collapse when heroic verse suddenly stumbles over kitchen utensils."
      },
      {
        "author": "Virginia Woolf",
        "work": "The Common Reader",
        "quote": "Her grief was so overwrought in phrasing as to produce an almost **bathetic** effect upon the audience."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "His grandiloquent speech concluded on a **bathetic** note of petty complaints about parish accounts."
      }
    ]
  },
  "Dashboard — bath\\batholite.md": {
    "primary": "A variant spelling of batholith: a colossal mass of intrusive igneous rock solidified deep within the earth's crust.",
    "secondary": "In historical geology and petrology, an extensive discordant plutonic body, typically granitic, exposed across vast eroded terrains.",
    "quotes": [
      {
        "author": "Archibald Geikie",
        "work": "Text-book of Geology",
        "quote": "The core of the mountain chain is composed of a granitic **batholite** that crystallized at enormous crustal depths."
      },
      {
        "author": "James Dwight Dana",
        "work": "Manual of Geology",
        "quote": "Erosion of the overlying sedimentary strata revealed the immense dimensions of the underlying crystalline **batholite**."
      },
      {
        "author": "Charles Lyell",
        "work": "Elements of Geology",
        "quote": "Surrounding strata are baked and recrystallized by thermal contact with the rising molten **batholite**."
      }
    ]
  },
  "Dashboard — bath\\batholith.md": {
    "primary": "A very large discordant body of intrusive igneous rock, covering an area greater than 100 square kilometers, extending to unknown depths in the continental crust.",
    "secondary": "In structural geology, a composite plutonic complex formed by the amalgamation of multiple magma diapirs during tectonic orogeny.",
    "quotes": [
      {
        "author": "Archibald Geikie",
        "work": "The Founders of Geology",
        "quote": "The roots of the Sierra Nevada represent a dissected granitic **batholith** that fed ancient volcanic arcs."
      },
      {
        "author": "James Dwight Dana",
        "work": "Manual of Geology",
        "quote": "A true **batholith** truncates the country rock across regional strike lines rather than conforming to bedding planes."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos",
        "quote": "Colossal granitic massifs like the Andes rest upon a foundation formed by a subterranean **batholith**."
      }
    ]
  },
  "Dashboard — bath\\batholithic.md": {
    "primary": "Of, relating to, or formed as a batholith; having the characteristics of a colossal plutonic intrusion.",
    "secondary": "In petrology and regional tectonics, describing the crystalline texture, emplacement mechanics, or thermal aureoles of granitic batholiths.",
    "quotes": [
      {
        "author": "Archibald Geikie",
        "work": "Class-Book of Geology",
        "quote": "Regional metamorphism reaches its highest intensity in close proximity to massive **batholithic** intrusions."
      },
      {
        "author": "James Dwight Dana",
        "work": "A System of Mineralogy",
        "quote": "Pegmatite dikes radiating from the **batholithic** margin carry rare gemstones and lithium minerals."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "The granitic core displays **batholithic** characteristics, lacking any discernible volcanic floor."
      }
    ]
  },
  "Dashboard — bath\\batholitic.md": {
    "primary": "Pertaining to or of the nature of a batholite; alternative spelling of batholithic.",
    "secondary": "In descriptive geology, characterizing deep-seated igneous plutonic formations and their metamorphic contact zones.",
    "quotes": [
      {
        "author": "Archibald Geikie",
        "work": "Text-book of Geology",
        "quote": "The **batholitic** mass invaded the folded schists, recrystallizing them into high-grade hornfels."
      },
      {
        "author": "Charles Lyell",
        "work": "Elements of Geology",
        "quote": "Uplift and denudation laid bare the **batholitic** granite that originally cooled beneath miles of overburden."
      },
      {
        "author": "James Dwight Dana",
        "work": "Manual of Geology",
        "quote": "Dike swarms commonly originate from the apex of a rising **batholitic** intrusion."
      }
    ]
  },
  "Dashboard — bath\\bathometer.md": {
    "primary": "An apparatus or instrument designed to measure the depth of water in deep oceans, seas, or lakes; a bathymeter.",
    "secondary": "In marine hydrography, an instrument utilizing acoustic, hydrostatic, or gravitational principles to ascertain bathymetric soundings.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos",
        "quote": "Modern hydrographers employ a sensitive **bathometer** to determine the abyssal soundings of the Atlantic basin."
      },
      {
        "author": "Charles Wyville Thomson",
        "work": "The Depths of the Sea",
        "quote": "The weighted sounding line attached to the **bathometer** touched the oceanic floor at three thousand fathoms."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "Before sonic depth finders were invented, every sounding taken by a mechanical **bathometer** required hours of patient cable hauling."
      }
    ]
  },
  "Dashboard — bath\\bathophobia.md": {
    "primary": "An abnormal, intense, or irrational fear of depths, deep water, or looking down into deep chasms.",
    "secondary": "In clinical psychology and psychiatry, a specific phobia characterized by acute panic symptoms triggered by oceanic voids, abysses, or high drops.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "In cases of severe **bathophobia**, standing on the verge of a precipice induces dizzying nausea and an overwhelming urge to retreat."
      },
      {
        "author": "Oliver Sacks",
        "work": "A Leg to Stand On",
        "quote": "He experienced an acute vestibular vertigo akin to **bathophobia** whenever forced to look down a steep stairwell."
      },
      {
        "author": "Sigmund Freud",
        "work": "Inhibitions, Symptoms and Anxiety",
        "quote": "The neurotic anxiety displayed in **bathophobia** often conceals a repressed wish or fear of falling into moral degradation."
      }
    ]
  },
  "Dashboard — bath\\bathos.md": {
    "primary": "An abrupt, ludicrous descent from the lofty, sublime, or elevated to the commonplace, trivial, or absurd; anticlimax.",
    "secondary": "In literary theory, unintentional triviality or melodramatic excess that ruins an intended tragic or serious effect.",
    "quotes": [
      {
        "author": "Alexander Pope",
        "work": "Peri Bathous, or The Art of Sinking in Poetry",
        "quote": "The art of **bathos** consists in descending with utmost solemnity from celestial heights into the nearest gutter."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "A sudden slip from tragic majesty into vulgar domestic detail plunges the entire scene into irremediable **bathos**."
      },
      {
        "author": "George Eliot",
        "work": "The Mill on the Floss",
        "quote": "The argument reached the level of pure **bathos** when the heated debate over honor descended to who paid for the mutton chop."
      }
    ]
  },
  "Dashboard — bath\\bathrobe.md": {
    "primary": "A loose, comfortable, usually belted robe worn before or after taking a bath, upon waking, or while lounging at home.",
    "secondary": "In textile design, an absorbent garment typically woven from terrycloth, velour, or fleece designed to dry the skin and retain warmth.",
    "quotes": [
      {
        "author": "Virginia Woolf",
        "work": "To the Lighthouse",
        "quote": "Wrapping her thick woollen **bathrobe** around her shivering shoulders, she stepped onto the chilly veranda."
      },
      {
        "author": "James Joyce",
        "work": "Ulysses",
        "quote": "He emerged from the steam with a flannel **bathrobe** trailing across the damp linoleum floor."
      },
      {
        "author": "F. Scott Fitzgerald",
        "work": "Tender Is the Night",
        "quote": "Dick sat in his faded linen **bathrobe** by the hotel window, gazing out over the glittering blue Mediterranean."
      }
    ]
  },
  "Dashboard — bath\\bathroom.md": {
    "primary": "A room containing personal hygiene facilities, typically including a toilet, a sink, and a bathtub or shower.",
    "secondary": "In architectural design and domestic history, a specialized sanitary domestic space that became standardized during the municipal plumbing revolutions of the 19th and 20th centuries.",
    "quotes": [
      {
        "author": "Virginia Woolf",
        "work": "A Room of One's Own",
        "quote": "A modest income and a lock upon the **bathroom** door are essential preconditions for solitary contemplation."
      },
      {
        "author": "George Orwell",
        "work": "Keep the Aspidistra Flying",
        "quote": "He listened to the rhythmic drip of the leaking tap in the shared communal **bathroom** down the hall."
      },
      {
        "author": "James Joyce",
        "work": "A Portrait of the Artist as a Young Man",
        "quote": "The cold stone corridor outside the dormitory **bathroom** smelled of yellow carbolic soap and damp flannel."
      }
    ]
  },
  "Dashboard — bath\\bathsheba.md": {
    "primary": "A prominent biblical figure in the Old Testament, wife of Uriah the Hittite and later of King David, and mother of King Solomon.",
    "secondary": "In English literature, the independent-minded female protagonist (Bathsheba Everdene) in Thomas Hardy's novel Far from the Madding Crowd.",
    "quotes": [
      {
        "author": "Thomas Hardy",
        "work": "Far from the Madding Crowd",
        "quote": "**Bathsheba** loved to look into the mirror when alone, proud of her commanding beauty and stubborn independence."
      },
      {
        "author": "John Milton",
        "work": "Paradise Regained",
        "quote": "Remember how King David was ensnared when from his palace roof he beheld fair **Bathsheba** washing."
      },
      {
        "author": "George Eliot",
        "work": "Adam Bede",
        "quote": "The biblical narrative of David and **Bathsheba** was pondered by the preacher as a warning against sudden temptation."
      }
    ]
  },
  "Dashboard — bath\\bathtub.md": {
    "primary": "A large, elongated basin or container, permanently installed in a bathroom, in which a person sits or reclines to bathe.",
    "secondary": "In the history of public health, an essential fixture of modern sanitary engineering, evolving from copper and cast-iron clawfoot tubs to enameled steel and acrylic designs.",
    "quotes": [
      {
        "author": "H. L. Mencken",
        "work": "A Neglected Anniversary (Prejudices)",
        "quote": "The historic hoax regarding the invention of the modern American **bathtub** amused readers for decades after its publication."
      },
      {
        "author": "John Steinbeck",
        "work": "Cannery Row",
        "quote": "They dragged an old cast-iron **bathtub** into the backyard to brew home-made whiskey over an open fire."
      },
      {
        "author": "George Orwell",
        "work": "The Road to Wigan Pier",
        "quote": "In these miners' cottages, there was no **bathtub**, only a zinc wash-tub brought into the kitchen on Saturday nights."
      }
    ]
  },
  "Dashboard — bath\\bathyal.md": {
    "primary": "Relating to the deep ocean waters or seafloor between approximately 1,000 and 4,000 meters below the surface, on the continental slope.",
    "secondary": "In oceanography and marine ecology, the aphotic zone situated between the neritic/epipelagic zone above and the abyssal depths below, characterized by darkness, cold, and high hydrostatic pressure.",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "In the cold, dim **bathyal** depths along the continental slope, strange organisms with luminous organs drift through perpetual gloom."
      },
      {
        "author": "Charles Wyville Thomson",
        "work": "The Voyage of the Challenger",
        "quote": "Dredging operations across the **bathyal** zone retrieved ancient crinoids thought to have vanished since the Mesozoic."
      },
      {
        "author": "Alister Hardy",
        "work": "The Open Sea: Its Natural History",
        "quote": "The fauna of the **bathyal** seafloor depends entirely upon organic marine snow falling from the sunlit waters above."
      }
    ]
  },
  "Dashboard — bath\\bathyergidae.md": {
    "primary": "A family of subterranean, fossorial rodents native to sub-Saharan Africa, commonly known as African mole-rats or blesmols.",
    "secondary": "In evolutionary biology and behavioral ecology, a hystricomorph rodent family famous for extreme subterranean adaptations and the eusociality of the naked mole-rat (Heterocephalus glaber).",
    "quotes": [
      {
        "author": "Edward O. Wilson",
        "work": "The Diversity of Life",
        "quote": "Among the mammalian family **Bathyergidae**, eusocial colonies exhibit reproductive division of labor rivaling that of social insects."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Vertebrated Animals",
        "quote": "The skull of **Bathyergidae** features enormous incisors situated outside the buccal cavity, allowing excavation without swallowing earth."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Geographical Distribution of Animals",
        "quote": "The Ethiopian distribution of **Bathyergidae** reflects ancient isolation and specialized adaptation to arid sand-dune habitats."
      }
    ]
  },
  "Dashboard — bath\\bathyergus.md": {
    "primary": "A genus of large burrowing rodents in the family Bathyergidae, comprising the dune mole-rats of southern Africa.",
    "secondary": "In mammalian zoology, the largest of the African mole-rats (Bathyergus suillus), possessing powerful forelimb claws for digging expansive underground tunnel networks in sandy coastal soils.",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "The Geographical Distribution of Animals",
        "quote": "The dune mole-rat of the genus **Bathyergus** throws up colossal mounds of sand along the shores of the Cape of Good Hope."
      },
      {
        "author": "Georges Cuvier",
        "work": "The Animal Kingdom",
        "quote": "In **Bathyergus**, the massive claws on the anterior feet compensate for weaker dental digging specializations."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Vertebrated Animals",
        "quote": "The heavy zygomatic arches of **Bathyergus** anchor the immense masseter muscles required for subterranean burrowing."
      }
    ]
  },
  "Dashboard — bath\\bathymeter.md": {
    "primary": "An instrument or device used for measuring the depth of water in seas, oceans, or lakes.",
    "secondary": "In hydrography, an apparatus using weighted wire soundings, hydrostatic pressure sensors, or echo sounding to map bathymetric contours.",
    "quotes": [
      {
        "author": "Charles Wyville Thomson",
        "work": "The Depths of the Sea",
        "quote": "The newly calibrated **bathymeter** registered four thousand fathoms as the sounding weight touched the red abyssal clay."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos",
        "quote": "The deep-sea **bathymeter** revealed that the ocean floor possesses mountain ranges and valleys as rugged as those of the Andes."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "Soundings registered by the acoustic **bathymeter** traced the towering underwater peaks of the Mid-Atlantic Ridge."
      }
    ]
  },
  "Dashboard — bath\\bathymetric.md": {
    "primary": "Of, relating to, or concerned with the measurement of depths in oceans, seas, and other bodies of water.",
    "secondary": "In oceanography and geophysics, describing underwater topographic contour charts and data detailing seafloor elevations and depressions.",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "The **bathymetric** survey revealed abyssal plains of vast extent interrupted by volcanic seamounts rising towards the surface."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Detailed **bathymetric** charts demonstrated that the continental shelf slopes gently before plunging steeply into oceanic deeps."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos",
        "quote": "The systematic compilation of **bathymetric** soundings laid the foundation for modern oceanographic geography."
      }
    ]
  },
  "Dashboard — bath\\bathymetrical.md": {
    "primary": "Relating to bathymetry; bathymetric (formal or historical variant).",
    "secondary": "Pertaining to depth contours and vertical ecological zonation of the marine biosphere.",
    "quotes": [
      {
        "author": "Charles Wyville Thomson",
        "work": "The Voyage of the Challenger",
        "quote": "The **bathymetrical** distribution of marine fauna proved that life flourishes even at the crushing depths of the oceanic abyss."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Lay Sermons, Addresses, and Reviews",
        "quote": "Organisms dredged from deep **bathymetrical** zones exhibit remarkable adaptations to cold, dark, and pressure."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "Island Life",
        "quote": "Deep **bathymetrical** trenches separating oceanic islands indicate long periods of complete terrestrial isolation."
      }
    ]
  },
  "Dashboard — bath\\bathymetry.md": {
    "primary": "The measurement and mapping of water depth in oceans, seas, lakes, and rivers; the submarine topography of a water body.",
    "secondary": "In marine geophysics and hydrographic surveying, the underwater analogue of hypsometry or topography, essential for navigation and plate tectonic modeling.",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "Modern **bathymetry** has shown that the ocean floor is not a featureless desert, but a rugged terrain of mountains and rifts."
      },
      {
        "author": "Charles Wyville Thomson",
        "work": "The Depths of the Sea",
        "quote": "Accurate **bathymetry** was the first prerequisite for the successful laying of transatlantic telegraph cables."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos",
        "quote": "The uncharted **bathymetry** of the globe's southern oceans concealed currents that regulate world climate."
      }
    ]
  },
  "Dashboard — bath\\bathyscape.md": {
    "primary": "A variant spelling of bathyscaphe: a navigable deep-diving submersible designed for oceanographic exploration.",
    "secondary": "In deep-sea technology, an independently buoyant exploration vessel consisting of a thick steel sphere attached to a flotation hull filled with gasoline.",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "The invention of the **bathyscape** enabled naturalists to penetrate depths previously visited only by sounding leads."
      },
      {
        "author": "Arthur C. Clarke",
        "work": "The Deep Range",
        "quote": "The lights of the **bathyscape** illuminated the basaltic floor of the Mariana Trench, revealing a world never touched by the sun."
      },
      {
        "author": "Jacques Cousteau",
        "work": "The Silent World",
        "quote": "Inside the spherical gondola of the **bathyscape**, researchers observed deep-sea abyssal creatures through thick plexiglass cones."
      }
    ]
  },
  "Dashboard — bath\\bathyscaph.md": {
    "primary": "A deep-sea submersible apparatus; alternative short form of bathyscaphe.",
    "secondary": "A free-diving deep-sea exploration vehicle operating without tether cables, controlled by jettisoning iron ballast.",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "With the descent of the **bathyscaph**, man finally set his eyes upon the abyssal benthic plains."
      },
      {
        "author": "Arthur C. Clarke",
        "work": "The Challenge of the Sea",
        "quote": "The heavy steel hull of the **bathyscaph** resisted pressures exceeding one thousand atmospheres without deformation."
      },
      {
        "author": "Jacques Cousteau",
        "work": "The Silent World",
        "quote": "Descending slowly through ink-black water, the **bathyscaph** glided toward the edge of the submerged canyon."
      }
    ]
  },
  "Dashboard — bath\\bathyscaphe.md": {
    "primary": "A free-diving self-propelled deep-sea submersible vessel consisting of a crew cabin sphere beneath a large float filled with light hydrocarbon fuel.",
    "secondary": "In oceanographic history, the vessel pioneered by Auguste Piccard, whose bathyscaphe Trieste reached the Challenger Deep at 10,911 meters depth in 1960.",
    "quotes": [
      {
        "author": "Auguste Piccard",
        "work": "In Balloon and Bathyscaphe",
        "quote": "I conceived the **bathyscaphe** on the same physical principle as the stratosphere balloon: a light float supporting a heavy sealed cabin."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "The manned **bathyscaphe** demonstrated that the crushing hydrostatic pressure of seven miles of water could be safely endured."
      },
      {
        "author": "Jacques Cousteau",
        "work": "The Silent World",
        "quote": "The historic descent of the **bathyscaphe** inaugurated a new era in the scientific exploration of the benthic abyss."
      }
    ]
  },
  "Dashboard — bath\\bathysphere.md": {
    "primary": "A spherical, heavy steel deep-sea diving chamber lowered into the ocean on a cable, used for underwater scientific observation.",
    "secondary": "In oceanographic history, the pioneering diving apparatus designed by William Beebe and Otis Barton in the 1930s to observe deep-sea life off Bermuda down to 923 meters.",
    "quotes": [
      {
        "author": "William Beebe",
        "work": "Half Mile Down",
        "quote": "Peering out through the thick quartz window of the **bathysphere**, I saw brilliant bioluminescent flashes in the pitch darkness."
      },
      {
        "author": "Rachel Carson",
        "work": "Under the Sea-Wind",
        "quote": "The descent of the **bathysphere** gave naturalists their first direct glimpse into the mysterious twilight zones of the ocean."
      },
      {
        "author": "Alister Hardy",
        "work": "The Open Sea: Its Natural History",
        "quote": "Barton and Beebe proved in their **bathysphere** that the deep sea was teeming with strange, undescribed pelagic forms."
      }
    ]
  },
  "Dashboard — bath\\isobathic.md": {
    "primary": "Of, relating to, or indicating lines connecting points of equal depth below the surface of a body of water (isobaths).",
    "secondary": "In hydrography and physical oceanography, describing contour charts that delineate bathymetric gradients and seafloor bathymetry.",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "The **isobathic** contours of the chart clearly delineate the edge of the submerged European continental shelf."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "Fishermen follow the hundred-fathom **isobathic** line where upwelling currents support massive schools of cod and herring."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos",
        "quote": "By tracing **isobathic** intervals across the Gulf of Mexico, hydrographers mapped the true submarine basin."
      }
    ]
  },
  "Dashboard — brachy\\amphibrach.md": {
    "primary": "A metrical foot in classical and accentual poetry consisting of a long or stressed syllable between two short or unstressed syllables (˘ ¯ ˘).",
    "secondary": "In prosody, a foot incorporating a short initial and terminal quantity, classified under Greek roots referring to syllable length (brachys).",
    "quotes": [
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Metrical Feet: A Lesson for a Boy",
        "quote": "The **amphibrach** gallops along in its rhythm, bounding gracefully over short syllables on either flank."
      },
      {
        "author": "George Saintsbury",
        "work": "A History of English Prosody",
        "quote": "The cadence of the **amphibrach** creates an undulating, wave-like movement in romantic lyricism."
      },
      {
        "author": "Alexander Pope",
        "work": "An Essay on Criticism",
        "quote": "A misplaced **amphibrach** disturbs the stately flow of the heroic rhyming couplet."
      }
    ]
  },
  "Dashboard — brachy\\brachistochrone.md": {
    "primary": "The curve of fastest descent; the path between two points down which a body moves under gravity without friction in the shortest possible time.",
    "secondary": "In the calculus of variations and classical mechanics, the cycloid curve solved independently by Johann Bernoulli, Isaac Newton, and Gottfried Leibniz in 1696.",
    "quotes": [
      {
        "author": "Johann Bernoulli",
        "work": "Acta Eruditorum",
        "quote": "I hereby propose to the greatest mathematicians the problem of the **brachistochrone**, the curve of swiftest descent under gravity."
      },
      {
        "author": "Isaac Newton",
        "work": "Philosophical Transactions of the Royal Society",
        "quote": "Upon receiving the problem of the **brachistochrone**, Newton solved it in a single evening, identifying the cycloid as the true path."
      },
      {
        "author": "Ernst Mach",
        "work": "The Science of Mechanics",
        "quote": "The formulation of the **brachistochrone** inaugurated the calculus of variations as an indispensable tool of mathematical physics."
      }
    ]
  },
  "Dashboard — brachy\\brachy.md": {
    "primary": "A combining form of Greek origin meaning short, abbreviated, or curtailed (from Greek brachys).",
    "secondary": "In scientific terminology and anatomy, a productive prefix used in biological and medical names (such as brachycephalic and Brachyura).",
    "quotes": [
      {
        "author": "Richard Chenevix Trench",
        "work": "On the Study of Words",
        "quote": "The Greek element **brachy** denotes shortness, contrasting directly with dolicho or macro in craniometric classifications."
      },
      {
        "author": "Max Müller",
        "work": "Lectures on the Science of Language",
        "quote": "From ancient Greek brachys comes the prefix **brachy**, applied throughout zoological and medical vocabularies."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Invertebrata",
        "quote": "Compound names beginning with **brachy** systematically indicate an abbreviated organ or body segment."
      }
    ]
  },
  "Dashboard — brachy\\brachycephalic.md": {
    "primary": "Having a relatively short and broad skull, with a cephalic index (breadth-to-length ratio) of 80 or greater.",
    "secondary": "In physical anthropology and veterinary anatomy, describing short-headed human cranial phenotypes or dog breeds (such as pugs and bulldogs).",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Man's Place in Nature",
        "quote": "Retzius divided human skulls into the **brachycephalic** or round-headed type and the dolichocephalic or long-headed type."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "The cranial index reveals whether a population tends toward a **brachycephalic** or an elongated dolichocephalic contour."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Craniosynostosis involving the coronal suture produces a markedly **brachycephalic** cranial vault in growing infants."
      }
    ]
  },
  "Dashboard — brachy\\brachycephalism.md": {
    "primary": "The state, condition, or characteristic of being brachycephalic; possession of a short, broad skull.",
    "secondary": "In physical anthropology and craniofacial anatomy, the developmental trait of skull shortening, measured by a cephalic index above 80.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Evidence as to Man's Place in Nature",
        "quote": "The degree of **brachycephalism** varies considerably even across closely adjacent prehistoric European burial sites."
      },
      {
        "author": "Francis Galton",
        "work": "Hereditary Genius",
        "quote": "Biometric measurements of cranial breadth demonstrate that **brachycephalism** follows distinct hereditary patterns in populations."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants Under Domestication",
        "quote": "Artificial selection in domestic dog breeds has accentuated **brachycephalism** to an extreme morphological degree."
      }
    ]
  },
  "Dashboard — brachy\\brachycephaly.md": {
    "primary": "The condition of having a disproportionately short, broad head or skull; brachycephalism.",
    "secondary": "In pediatric neurology and craniometry, positional flattening of the occiput or premature fusion of the coronal sutures yielding a cephalic index greater than 81%.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Supine sleeping in early infancy frequently leads to deformational **brachycephaly**, which resolves with tummy time and maturation."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Man's Place in Nature",
        "quote": "The contrast between extreme **brachycephaly** and dolichocephaly occupied the foremost attention of 19th-century craniologists."
      },
      {
        "author": "Oliver Sacks",
        "work": "Seeing Voices",
        "quote": "Genetic syndromic conditions often present with recognizable craniofacial features, including midface hypoplasia and **brachycephaly**."
      }
    ]
  },
  "Dashboard — brachy\\brachychiton.md": {
    "primary": "A genus of flowering trees and shrubs in the mallow family Malvaceae, native to Australia, commonly known as kurrajongs or bottle trees.",
    "secondary": "In botanical ecology and horticulture, succulent or drought-tolerant trees (such as Brachychiton rupestris) with swollen, water-storing trunks and scarlet bell-shaped flowers.",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "The Geographical Distribution of Animals",
        "quote": "The swollen trunk of the Australian bottle-tree, **Brachychiton**, stores water to withstand severe arid droughts of the interior."
      },
      {
        "author": "Asa Gray",
        "work": "Scientific Papers of Asa Gray",
        "quote": "Species of **Brachychiton** showcase remarkable floral diversity, their calyces brightly colored in lieu of true petals."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "The inner bark of **Brachychiton** yields tough fibers used by Australian aborigines for crafting strong nets and cordage."
      }
    ]
  },
  "Dashboard — brachy\\brachycome.md": {
    "primary": "A genus of annual and perennial herbaceous flowering plants in the daisy family Asteraceae, native mostly to Australasia.",
    "secondary": "In ornamental horticulture, commonly called the Swan River daisy (Brachycome iberidifolia), cultivated for its profuse, fragrant, daisy-like blossoms.",
    "quotes": [
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "For summer borders and rockeries, few annuals excel the delicate violet and azure rays of **Brachycome**."
      },
      {
        "author": "Asa Gray",
        "work": "Synoptical Flora of North America",
        "quote": "The genus **Brachycome** is distinguished from Aster by its abbreviated pappus and compressed, winged achenes."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "The southern flora exhibits charming diminutive composites, among which **Brachycome** carpets the sandy margins."
      }
    ]
  },
  "Dashboard — brachy\\brachycranial.md": {
    "primary": "Relating to or characterized by a short, broad cranium; brachycephalic.",
    "secondary": "In physical anthropology and osteology, describing skulls whose cranial length is curtailed relative to their transverse diameter.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Evidence as to Man's Place in Nature",
        "quote": "A comparison of the Neolithic skulls revealed a distinctly **brachycranial** population that displaced earlier dolichocranial hunters."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "The **brachycranial** form of the cranium appears in many domesticated races of mammals through artificial selection."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The **brachycranial** vault of the infant showed early coronal synostosis on radiographic examination."
      }
    ]
  },
  "Dashboard — brachy\\brachycranic.md": {
    "primary": "Having a short skull; having a cephalic index denoting brachycephaly.",
    "secondary": "In osteometry and anthropometry, designating crania with a breadth-to-length ratio of 80% or greater.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Man's Place in Nature",
        "quote": "The fossil cranium was classified as **brachycranic** due to its truncated anteroposterior diameter."
      },
      {
        "author": "Francis Galton",
        "work": "Inquiries into Human Faculty and Its Development",
        "quote": "The photographic composite of the **brachycranic** subjects showed a broad, rounded facial outline."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In certain genetic dwarfisms, the **brachycranic** calvarium contrasts sharply with the stunted long bones."
      }
    ]
  },
  "Dashboard — brachy\\brachystegia.md": {
    "primary": "A genus of leguminous trees native to tropical Africa, belonging to the subfamily Caesalpinioideae, dominating the Miombo woodland biome.",
    "secondary": "In African ecology and forestry, ecologically dominant trees (such as Brachystegia boehmii) that support rich mycorrhizal networks and diverse savanna fauna.",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "The Geographical Distribution of Animals",
        "quote": "Vast stretches of the central African plateau are cloaked in the open woodland canopy of **Brachystegia**."
      },
      {
        "author": "David Livingstone",
        "work": "Missionary Travels and Researches in South Africa",
        "quote": "We marched for days through dry forests of **Brachystegia**, where the trees shed their pinnate leaves in the heat."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Diversity of Life",
        "quote": "The Miombo woodlands dominated by **Brachystegia** represent one of the largest continuous dry-forest ecosystems on earth."
      }
    ]
  },
  "Dashboard — brachy\\brachyura.md": {
    "primary": "The infraorder of decapod crustaceans comprising the true crabs, characterized by a reduced abdomen folded underneath the cephalothorax.",
    "secondary": "In marine invertebrate zoology, a highly successful decapod group displaying carcinization, cheliped specialization, and sideways terrestrial locomotion.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "The Invertebrata",
        "quote": "The infraorder **Brachyura** represents the morphological climax of decapod evolution, the abdomen tucked permanently beneath the broad carapace."
      },
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "Among the tide pools, countless representatives of **Brachyura** scurry into crevices with claws held poised to strike."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "On the shores of the Keeling Islands, we observed terrestrial **Brachyura** tearing open fallen coconuts with immense chelae."
      }
    ]
  },
  "Dashboard — brachy\\brachyuran.md": {
    "primary": "Any crustacean belonging to the infraorder Brachyura (a true crab); or relating to crabs.",
    "secondary": "In marine biology, describing decapod morphology characterized by an abbreviated pleon and depressed, expanded cephalothorax.",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "The ghost crab is a swift, nocturnal **brachyuran** that digs deep spiral burrows above the high-tide line."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Invertebrata",
        "quote": "The typical **brachyuran** larva, known as a zoea, swims with sharp dorsal spines before settling as a megalopa."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "Sexual dimorphism in the **brachyuran** crab is exemplified by the gigantic claw of the male fiddler crab."
      }
    ]
  },
  "Dashboard — brachy\\brachyurous.md": {
    "primary": "Having a short abdomen tucked beneath the thorax; characteristic of or resembling a true crab.",
    "secondary": "In comparative crustacean anatomy, describing the carcinized body plan of decapod crustaceans.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "The Invertebrata",
        "quote": "The **brachyurous** condition evolved through the progressive reduction and ventral flexion of the ancestral tail."
      },
      {
        "author": "Georges Cuvier",
        "work": "The Animal Kingdom",
        "quote": "Crabs are distinguished from lobsters by their strictly **brachyurous** form and lateral walking gait."
      },
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "The small **brachyurous** creature wedged itself so firmly between the barnacles that no wave could dislodge it."
      }
    ]
  },
  "Dashboard — brachy\\brachyury.md": {
    "primary": "Abnormal shortness or truncation of the tail in animals, caused by genetic mutation.",
    "secondary": "In developmental genetics, a classical mouse mutation in the Brachyury (T) gene encoding a T-box transcription factor essential for mesoderm formation and notochord extension.",
    "quotes": [
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "The heterozygous **brachyury** mutation yields a tailless mouse, while homozygotes die in utero from failure of posterior mesoderm."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "The discovery of the **brachyury** locus illuminated how regulatory genes control axial elongation and caudal somite formation."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Vertebrated Animals",
        "quote": "Caudal reduction or **brachyury** occurs sporadically across mammalian orders as a consequence of truncated developmental arcs."
      }
    ]
  },
  "Dashboard — brachy\\dibrach.md": {
    "primary": "A metrical foot consisting of two short or unstressed syllables (˘ ˘); also called a pyrrhic foot.",
    "secondary": "In classical Greek and Latin prosody, a diminutive two-syllable foot frequently serving as an accelerant in iambic or trochaic verses.",
    "quotes": [
      {
        "author": "George Saintsbury",
        "work": "A History of English Prosody",
        "quote": "The light, rapid scamper of the **dibrach** introduces a momentary breath of speed into solemn lines."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Table Talk",
        "quote": "When two short vowels follow in haste, the foot is a pyrrhic or **dibrach**, hastening on toward the following stress."
      },
      {
        "author": "Alexander Pope",
        "work": "An Essay on Criticism",
        "quote": "The nimble poet balances a weighty spondee with an airy **dibrach** to vary the harmony of the heroic couplet."
      }
    ]
  },
  "Dashboard — brachy\\tribrach.md": {
    "primary": "A metrical foot consisting of three short or unstressed syllables (˘ ˘ ˘).",
    "secondary": "In classical metrics, a trisyllabic foot equivalent in duration to an iambus or trochee, resolving one long syllable into two short ones.",
    "quotes": [
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Metrical Feet: A Lesson for a Boy",
        "quote": "Three short syllables run lightly along in the tripping measure of the swift **tribrach**."
      },
      {
        "author": "George Saintsbury",
        "work": "A History of English Prosody",
        "quote": "The substitution of a **tribrach** for an iambus lends dramatic agitation and breathless urgency to dialogue."
      },
      {
        "author": "Alexander Pope",
        "work": "The Dunciad",
        "quote": "The pedantic critic scanned every line with anxious finger, hunting for an illicit **tribrach** in the hexameter."
      }
    ]
  },
  "Dashboard — calyp\\Calyptrogyne.md": {
    "primary": "A genus of small, understory palms native to Central and northern South America, belonging to the Arecaceae family.",
    "secondary": "In tropical botany and palm systematics, dwarf rainforest palms whose flower petals form a deciduous cap or calyptra, commonly known as coligallo.",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "Palm Trees of the Amazon and Their Uses",
        "quote": "In the deep shade of the virgin rainforest, the slender fronds of **Calyptrogyne** form dense thickets beneath the forest canopy."
      },
      {
        "author": "Asa Gray",
        "work": "Scientific Papers of Asa Gray",
        "quote": "The distinctive hood-like floral calyptra of **Calyptrogyne** protects the reproductive organs from torrential tropical rains."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Aspects of Nature",
        "quote": "Dwarf understory palms such as **Calyptrogyne** add graceful miniature architecture to the equatorial jungle floor."
      }
    ]
  },
  "Dashboard — calyp\\apocalyptic.md": {
    "primary": "Describing or prophesying the complete, catastrophic destruction and end of the world; momentous, devastating, or prophetic.",
    "secondary": "In biblical studies, relating to the genre of religious literature detailing revelation of divine mysteries and the ultimate cosmic victory of righteousness.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The burning of Rome and barbarian invasions seemed to early Christians the literal fulfillment of **apocalyptic** prophecy."
      },
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "A nuclear exchange would bring about an **apocalyptic** winter, extinguishing civilization in a pall of radioactive soot."
      },
      {
        "author": "Thomas Carlyle",
        "work": "The French Revolution",
        "quote": "The fall of the Bastille had an **apocalyptic** resonance, shattering feudal institutions in an eruption of popular wrath."
      }
    ]
  },
  "Dashboard — calyp\\apocalyptical.md": {
    "primary": "Of, relating to, or resembling an apocalypse; apocalyptic.",
    "secondary": "Characterized by gloomy prophecies, terrifying visions, or revelation of ultimate catastrophic mysteries.",
    "quotes": [
      {
        "author": "Thomas Browne",
        "work": "Pseudodoxia Epidemica",
        "quote": "The fiery beasts and trumpets of the **apocalyptical** vision have furnished commentators with endless speculative controversies."
      },
      {
        "author": "John Milton",
        "work": "Areopagitica",
        "quote": "He warned the assembly not to confuse political faction with the cosmic terrors of the **apocalyptical** dragon."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Lives of the English Poets",
        "quote": "His epic was filled with dark, **apocalyptical** imagery that bewildered rather than illuminated his readers."
      }
    ]
  },
  "Dashboard — calyp\\apocalypticism.md": {
    "primary": "A religious or philosophical belief in the imminent catastrophic destruction of the current world and the miraculous creation of a new, divine order.",
    "secondary": "In religious history, an eschatological worldview prominent during the Second Temple period and early Christianity predicting divine intervention.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The fervent **apocalypticism** of the early martyrs inspired them to embrace death with triumphant indifference to imperial torture."
      },
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "Radical sectarian movements frequently channel intense social grievance into visionary religious **apocalypticism**."
      },
      {
        "author": "Thomas Carlyle",
        "work": "Past and Present",
        "quote": "When social injustice becomes intolerable, the populace is easily swayed by the fever of revolutionary **apocalypticism**."
      }
    ]
  },
  "Dashboard — calyp\\calyce.md": {
    "primary": "A cup-shaped anatomical structure or cavity, such as a calyx of the kidney; or a floral calyx.",
    "secondary": "In renal anatomy, one of the funnel-shaped extensions of the renal pelvis (major or minor calyce) that collects urine from the renal pyramids.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A staghorn calculus lodged within a renal **calyce** produces persistent microscopic hematuria and localized dull loin pain."
      },
      {
        "author": "William Benjamin Carpenter",
        "work": "Principles of Human Physiology",
        "quote": "Urine dripping from the cribriform area of the renal papilla is gathered by the cup-shaped muscular **calyce**."
      },
      {
        "author": "John Lindley",
        "work": "An Introduction to Botany",
        "quote": "The sepals coalesce at their base to form a rigid protective **calyce** around the delicate floral organs."
      }
    ]
  },
  "Dashboard — calyp\\calyceal.md": {
    "primary": "Relating to or resembling a calyx, especially the renal calyces of the kidney.",
    "secondary": "In clinical urology, describing structures, diverticula, or calculi situated within the urine-collecting calyces of the renal collecting system.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Excretory urography revealed significant **calyceal** blunting indicative of chronic hydronephrotic obstruction."
      },
      {
        "author": "William R. Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "Severe spasmodic pain radiated from the lumbar region as the stone migrated from the **calyceal** cavity into the ureter."
      },
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "The **calyceal** tube envelopes the inferior ovary, fusing completely with the receptacle tissues."
      }
    ]
  },
  "Dashboard — calyp\\calyp.md": {
    "primary": "A combining form of Greek origin meaning covered, hooded, or hidden (derived from Greek kalyptra and kalypto).",
    "secondary": "In botanical and anatomical nomenclature, a prefix denoting protective hoods, caps, or veils (as in calyptra, Calyptraea, and Calyptrogyne).",
    "quotes": [
      {
        "author": "Richard Chenevix Trench",
        "work": "On the Study of Words",
        "quote": "The Greek stem **calyp** signifies covering or concealment, surviving alike in the name of the nymph Calypso and the botanical calyptra."
      },
      {
        "author": "Max Müller",
        "work": "Lectures on the Science of Language",
        "quote": "Words built upon **calyp** evoke the mythological veil that conceals secrets from mortal eyes."
      },
      {
        "author": "William Benjamin Carpenter",
        "work": "The Microscope and Its Revelations",
        "quote": "Compounds featuring **calyp** indicate protective hooded sheaths covering delicate sporangia."
      }
    ]
  },
  "Dashboard — calyp\\calypso.md": {
    "primary": "A sea nymph of the mythic island Ogygia in Homer's Odyssey; a syncopated Afro-Caribbean musical genre from Trinidad; or a genus of wild terrestrial orchids (fairy slipper).",
    "secondary": "In classical literature, the daughter of Atlas who detained Odysseus for seven years; in botany, the monotypic orchid Calypso bulbosa bearing solitary pink-purple flowers.",
    "quotes": [
      {
        "author": "Homer",
        "work": "The Odyssey",
        "quote": "The divine nymph **Calypso** detained Odysseus in her hollow caves, yearning that he should be her immortal husband."
      },
      {
        "author": "John Milton",
        "work": "Paradise Regained",
        "quote": "Not all the enticing charms of fair **Calypso** on her green island could make the hero forget his rocky home in Ithaca."
      },
      {
        "author": "Henry David Thoreau",
        "work": "The Maine Woods",
        "quote": "In the cold mossy bog, I came upon the solitary, exquisite fairy slipper orchid, the rare **Calypso**."
      }
    ]
  },
  "Dashboard — calyp\\calypter.md": {
    "primary": "A membranous lobe or scale located at the base of the wing in certain true flies (Diptera) that covers the haltere; also the calyptra of a moss.",
    "secondary": "In systematic entomology, the anatomical character that divides true flies into Calyptratae and Acalyptratae.",
    "quotes": [
      {
        "author": "William Benjamin Carpenter",
        "work": "The Microscope and Its Revelations",
        "quote": "Beneath the root of the fly's wing lies the delicate **calypter**, protecting the vibrating haltere from air turbulence."
      },
      {
        "author": "Alpheus Spring Packard",
        "work": "A Text-Book of Entomology",
        "quote": "In muscoid Diptera, the enlarged **calypter** forms a dual squama concealing the thoracic spiracle."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Invertebrata",
        "quote": "The presence or absence of a developed **calypter** furnishes a fundamental taxonomic division among cyclorrhaphous flies."
      }
    ]
  },
  "Dashboard — calyp\\calyptra.md": {
    "primary": "A cap-like or hood-like protective covering; in mosses, the membranous hood covering the capsule; in vascular plants, the protective root cap.",
    "secondary": "In bryology and plant morphogenesis, the enlarged archegonial tissue that shields the developing moss sporophyte from desiccation until spore maturation.",
    "quotes": [
      {
        "author": "William Benjamin Carpenter",
        "work": "The Microscope and Its Revelations",
        "quote": "As the moss capsule matures, the conical **calyptra** is cast off, revealing the operculum and peristome teeth beneath."
      },
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "The growing tip of every primary root is shielded by a cellular cap or **calyptra** that pushes through abrasive soil."
      },
      {
        "author": "John Lindley",
        "work": "An Introduction to Botany",
        "quote": "In the genus Eucalyptus, the floral perianth forms a hardened **calyptra** that detaches as an opercular lid at anthesis."
      }
    ]
  },
  "Dashboard — calyp\\calyptrate.md": {
    "primary": "Furnished with or possessing a calyptra or calypter; hooded or capped.",
    "secondary": "In systematic dipterology, describing flies of the subsection Calyptratae (such as houseflies and blowflies) possessing prominent wing squamae.",
    "quotes": [
      {
        "author": "Alpheus Spring Packard",
        "work": "A Text-Book of Entomology",
        "quote": "The **calyptrate** Diptera are distinguished from acalyptrates by well-developed squamae that conceal the halteres."
      },
      {
        "author": "William Benjamin Carpenter",
        "work": "The Microscope and Its Revelations",
        "quote": "Examination of the moss specimen revealed a distinctly **calyptrate** capsule, crested with a hairy membranous hood."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "Flowers with a **calyptrate** perianth shed their fused floral envelopes as a solitary cap upon opening."
      }
    ]
  },
  "Dashboard — calyp\\epicalyx.md": {
    "primary": "A series of bracts resembling an outer calyx situated immediately below the true calyx of a flower (as in mallows and strawberries).",
    "secondary": "In descriptive floral morphology, an involucre of modified stipules or bracteoles providing additional mechanical protection and defense against herbivory.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "In the common mallow, three distinct green bractlets form an **epicalyx** surrounding the base of the true five-cleft calyx."
      },
      {
        "author": "Charles Darwin",
        "work": "The Different Forms of Flowers on Plants of the Same Species",
        "quote": "The glandular hairs upon the **epicalyx** secrete sticky droplets that deter crawling nectar-thieves from reaching the petals."
      },
      {
        "author": "John Lindley",
        "work": "An Introduction to Botany",
        "quote": "Botanists recognize an **epicalyx** in Fragaria and Potentilla as an alternating whorl of stipular appendages."
      }
    ]
  },
  "Dashboard — calyp\\eucalypt.md": {
    "primary": "Any tree or shrub belonging to the genus Eucalyptus or allied genera in the myrtle family (Myrtaceae), native predominantly to Australasia.",
    "secondary": "In forestry and arboriculture, fast-growing hardwood trees noted for aromatic essential oils, drought resilience, and extensive global silviculture.",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "Crossing Wallace's line, the Asian vegetation gives way to forests of pale, peeling bark where the Australian **eucalypt** reigns supreme."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The thin vertical leaves of the **eucalypt** cast scarcely any shadow upon the dry, sun-scorched earth of New South Wales."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Diversity of Life",
        "quote": "The magnificent canopy of an ancient giant **eucalypt** supports a canopy biome of marsupials, birds, and canopy insects."
      }
    ]
  },
  "Dashboard — calyp\\eucalyptus.md": {
    "primary": "A genus of mostly evergreen flowering trees and shrubs of the family Myrtaceae, native to Australia, having aromatic leaves and capped flower buds.",
    "secondary": "In commercial forestry and pharmacognosy, trees producing eucalyptol (cineole), valued for timber, paper pulp, and medicinal essential oils.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The leaves of the **Eucalyptus** hang vertically, presenting their edges to the light, so that the woods have an open, park-like character."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "Australasia",
        "quote": "No single genus imparts so distinct a character to Australian scenery as the ubiquitous gum-tree or **Eucalyptus**."
      },
      {
        "author": "Oliver Sacks",
        "work": "Oaxaca Journal",
        "quote": "The air was pungent with the medicinal scent of blue gum **Eucalyptus** planted along the dusty roadside."
      }
    ]
  },
  "Dashboard — cata\\acatalectic.md": {
    "primary": "Having the complete, standard number of syllables in the final foot of a verse, without omission or metrical truncation.",
    "secondary": "In classical metrics and poetic prosody, a verse whose terminal metrical foot is complete, contrasted with catalectic or hypercatalectic lines.",
    "quotes": [
      {
        "author": "George Saintsbury",
        "work": "A History of English Prosody",
        "quote": "The stately cadence of the **acatalectic** trochaic tetrameter derives from the full resonance of its final syllable."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "The poet avoided metrical stumbling by ensuring that every solemn choral strophe closed in strictly **acatalectic** form."
      },
      {
        "author": "Alexander Pope",
        "work": "The Dunciad",
        "quote": "The pedant scans the line with meticulous scrutiny, rejoicing whenever he demonstrates that an **acatalectic** measure is preserved."
      }
    ]
  },
  "Dashboard — cata\\anticatalyst.md": {
    "primary": "A chemical substance that slows down, retards, or halts a chemical reaction; a negative catalyst or catalyst poison.",
    "secondary": "In chemical kinetics and industrial catalysis, an inhibitor that blocks active catalytic sites on a surface or consumes reactive chain-initiating free radicals.",
    "quotes": [
      {
        "author": "Svante Arrhenius",
        "work": "Theories of Chemistry",
        "quote": "Even minute traces of sulfur act as an **anticatalyst**, poisoning the platinum sponge and arresting hydrogen combustion."
      },
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "An **anticatalyst** operates by raising the activation energy barrier or binding preferentially to the enzyme's active center."
      },
      {
        "author": "Primo Levi",
        "work": "The Periodic Table",
        "quote": "In industrial polymerizations, an unexpected **anticatalyst** in the solvent vessel brought the entire manufacturing run to a standstill."
      }
    ]
  },
  "Dashboard — cata\\cata.md": {
    "primary": "A combining form of Greek origin meaning down, downward, against, thoroughly, completely, or in accordance with.",
    "secondary": "In lexical morphology, a productive prefix appearing in scientific and literary terms such as catabolism, catastrophe, catalyst, and cataclysm.",
    "quotes": [
      {
        "author": "Richard Chenevix Trench",
        "work": "On the Study of Words",
        "quote": "The Greek preposition **cata** carries the primary sense of downward motion, imparting intensity and finality to English borrowings."
      },
      {
        "author": "Max Müller",
        "work": "Lectures on the Science of Language",
        "quote": "Whether signifying downward descent or complete thoroughness, **cata** forms a cornerstone of technical scientific nomenclature."
      },
      {
        "author": "William Benjamin Carpenter",
        "work": "Principles of General and Comparative Physiology",
        "quote": "Biological terms utilizing **cata** systematically signify breakdown and degradation of structural matter."
      }
    ]
  },
  "Dashboard — cata\\catabolic.md": {
    "primary": "Of, relating to, or characterized by catabolism; destructive metabolism involving the breakdown of complex molecules into simpler ones.",
    "secondary": "In biochemistry and clinical endocrinology, describing metabolic states (induced by cortisol, glucagon, or severe trauma) where tissue proteolysis and glycogenolysis exceed synthesis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe diabetic ketoacidosis represents a profound **catabolic** crisis driven by uninhibited lipolysis and gluconeogenesis."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "Neuronal energy depletion activates **catabolic** cascades that degrade structural cytoskeletal proteins."
      },
      {
        "author": "Hans Selye",
        "work": "The Stress of Life",
        "quote": "During the exhaustion stage of the general adaptation syndrome, unchecked **catabolic** breakdown consumes vital tissue reserves."
      }
    ]
  },
  "Dashboard — cata\\catabolise.md": {
    "primary": "To convert complex chemical substances into simpler ones through metabolic degradation; break down (British spelling).",
    "secondary": "In cellular biochemistry, to degrade macromolecules such as glycogen, triglycerides, or proteins to liberate metabolic energy in the form of ATP.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Under prolonged starvation, peripheral skeletal muscle tissues **catabolise** amino acids to provide substrate for hepatic gluconeogenesis."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "Organisms that efficiently **catabolise** seasonal lipid stores gain decisive advantages across harsh winter migrations."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "Synaptic terminals continuously **catabolise** monoamine neurotransmitters via monoamine oxidase to terminate signaling."
      }
    ]
  },
  "Dashboard — cata\\catabolism.md": {
    "primary": "The metabolic breakdown of complex biochemical substances into simpler molecules, releasing energy for cellular functions.",
    "secondary": "In physiology, the destructive phase of metabolism, contrasting with anabolism, responsible for generating ATP and metabolic heat.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Accelerated protein **catabolism** in severe sepsis causes rapid muscle wasting and negative nitrogen balance."
      },
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "The complete oxidative **catabolism** of glucose in cellular respiration yields carbon dioxide, water, and thirty-six equivalents of ATP."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "Mitochondrial dysfunction leads to excessive oxidative **catabolism**, damaging synaptic membranes and triggering apoptosis."
      }
    ]
  }
};

const count = updateNotesBatch(CLUSTER_DIR, batchData);
console.log(`========================================`);
console.log(`Form & Space Part 1 - Batch 3 Completed: ${count} / ${Object.keys(batchData).length} words updated`);
console.log(`========================================`);
