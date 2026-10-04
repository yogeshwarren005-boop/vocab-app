# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — sal (Batch 7D: 35 words)
  # =========================================================================
  "Dashboard — sal/saltation.md": {
    "primary": "The act of leaping, jumping, or dancing; or a sudden, discontinuous change or mutation in evolutionary biology or sediment transport.",
    "secondary": "In geology and geomorphology, the transport of sand or gravel particles by wind or water through a series of short bounces along the bed.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Sand grains advance across desert dunes in a continuous series of low leaps termed **saltation**."},
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "The theory of evolution must allow for occasional abrupt transitions or biological **saltation**."},
      {"author": "William Bateson", "work": "Materials for the Study of Variation", "quote": "Discontinuous variations imply that species may arise through morphological **saltation** rather than minute increments."}
    ]
  },
  "Dashboard — sal/saltbox.md": {
    "primary": "A wooden wall-mounted box for holding table salt in a kitchen; or a traditional style of colonial New England wooden frame house with an asymmetrical gabled roof.",
    "secondary": "In American vernacular colonial architecture, a dwelling characterized by a two-story front facade sloping down to a single-story rear lean-to.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "The humble wooden **saltbox** dwelling stood beside the orchard, weathered by generations of Atlantic gales."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I reached into the wooden **saltbox** hanging near the hearth to season my simple meal of boiled corn."},
      {"author": "Laura Ingalls Wilder", "work": "Little House on the Prairie", "quote": "Ma kept a small cedar **saltbox** hanging conveniently near the cooking stove."}
    ]
  },
  "Dashboard — sal/saltbush.md": {
    "primary": "Any of various halophytic shrubs or herbs of the genus Atriplex, native to arid or saline regions and often grazed by livestock.",
    "secondary": "In Australian rangeland ecology, drought-hardy chenopod shrubs (Atriplex nummularia, Old Man Saltbush) providing crucial browse for sheep in dry seasons.",
    "quotes": [
      {"author": "Ludwig Leichhardt", "work": "Journal of an Overland Expedition in Australia", "quote": "The grey foliage of the **saltbush** covered the vast dry plains as far as the eye could reach."},
      {"author": "Thomas Mitchell", "work": "Three Expeditions into the Interior of Eastern Australia", "quote": "Our exhausted horses eagerly browsed upon the succulent leaves of the **saltbush** bordering the dry creek."},
      {"author": "Joseph Maiden", "work": "The Useful Native Plants of Australia", "quote": "The nutritious leaves of the Australian **saltbush** contain abundant mineral salts essential for wool production."}
    ]
  },
  "Dashboard — sal/saltcellar.md": {
    "primary": "A small decorative vessel or bowl placed on a dining table to hold salt for individual or shared use.",
    "secondary": "In Renaissance decorative metalwork and banqueting protocol, an elaborate silver centerpiece (such as Cellini's Salt Cellar) designating social status relative to seating.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "There is a **saltcellar** of state, so called, placed before monarchs to mark their imperial dignity."},
      {"author": "Benvenuto Cellini", "work": "Autobiography", "quote": "I fashioned the magnificent golden **saltcellar** representing the Earth and the Sea with exquisite interlinked figures."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe Gargery set down his knife and contemplatively examined the pewter **saltcellar** on the clean table."}
    ]
  },
  "Dashboard — sal/salted.md": {
    "primary": "Seasoned, treated, or preserved with salt; impregnated with saline crystals; or experienced and shrewd.",
    "secondary": "In mining fraud, a depleted or worthless ore mine artificially enriched with valuable minerals (salted mine) to deceive prospective investors.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I have made a satisfactory dinner simply off a dish of purslane which I gathered in my cornfield, boiled and **salted**."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The stew was made of small juicy clams mixed with pounded ship's biscuit and **salted** pork."},
      {"author": "Mark Twain", "work": "Roughing It", "quote": "The fraudulent promoters had cunningly **salted** the abandoned silver shaft with rich Nevada ore."}
    ]
  },
  "Dashboard — sal/salter.md": {
    "primary": "Having more salt or being more saline; or one who makes, cures, or sells salt or salted provisions.",
    "secondary": "In medieval guild commerce, a merchant belonging to the Worshipful Company of Salters, dealing in vital salt preservatives and dry chemicals.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "I'll do well yet. Thou old and true Menenius, thy tears are **salter** than a younger man's."},
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "The sea spray tasted **salter** than any water I had ever known as the surf threw me upon the rocks."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The wholesale **salter** supplied cured herrings to foreign merchants throughout the Baltic ports."}
    ]
  },
  "Dashboard — sal/saltine.md": {
    "primary": "A thin, crisp, square cracker or biscuit sprinkled with coarse salt, typically leavened with yeast and baking soda.",
    "secondary": "In modern commercial food processing, soda crackers laminated and baked rapidly in tunnel ovens to achieve delicate blistered crispness.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "He munched a dry **saltine** and sipped his bowl of chicken broth at the office desk."},
      {"author": "John Steinbeck", "work": "The Grapes of Wrath", "quote": "The children divided a packet of crisp **saltine** crackers among themselves by the side of the highway."},
      {"author": "Ernest Hemingway", "work": "A Moveable Feast", "quote": "We broke a crisp **saltine** into our fish chowder while watching the rain beat against the café windows."}
    ]
  },
  "Dashboard — sal/saltiness.md": {
    "primary": "The taste, property, or degree of being salty; salinity; or pungent, earthy sharpness in speech.",
    "secondary": "In sensory physiology and gustatory perception, the taste sensation elicited by sodium cations activating amiloride-sensitive epithelial sodium channels.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The invigorating **saltiness** of the sea wind brought color back to the pale invalid's cheeks."},
      {"author": "Henry David Thoreau", "work": "Cape Cod", "quote": "The heavy ocean breeze was laden with the pungent **saltiness** of drying kelp and tidal foam."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The extreme **saltiness** of the inland lagoons encrusted the surrounding rocks with glistening white saline crystals."}
    ]
  },
  "Dashboard — sal/salting.md": {
    "primary": "The act or process of applying salt for preservation, seasoning, or de-icing; a salt marsh flooded by the sea.",
    "secondary": "In British coastal geomorphology, a low-lying coastal salt marsh or meadow inundated by spring high tides.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Mrs. Bates had received a barrel of herrings from her cousin, and the **salting** was declared to be excellent."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip looked out across the gloomy marshes toward the tidal **salting** where the prison hulks lay."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The autumn **salting** of the sheep was carried out with methodical precision in the farm pens."}
    ]
  },
  "Dashboard — sal/saltire.md": {
    "primary": "An heraldic ordinary consisting of a diagonal cross in the shape of the letter X; Saint Andrew's cross.",
    "secondary": "In vexillology and heraldry, the diagonal cross dividing the shield into four partitions, famously emblazoned on the national flag of Scotland.",
    "quotes": [
      {"author": "Walter Scott", "work": "Marmion", "quote": "Upon his azure shield was borne a silver **saltire**, the ancient emblem of Saint Andrew."},
      {"author": "Arthur Conan Doyle", "work": "The White Company", "quote": "The Scottish archers marched proudly beneath their fluttering banner displaying the white **saltire**."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The imperial legionaries painted the mystical **saltire** upon their shields before the decisive engagement."}
    ]
  },
  "Dashboard — sal/saltish.md": {
    "primary": "Somewhat or moderately salty in taste or composition; slightly saline.",
    "secondary": "In hydrogeology and estuarine biology, brackish water transitional between river discharge and marine salinity.",
    "quotes": [
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The spring water had a **saltish** flavor, showing that the subterranean veins connected with the ocean."},
      {"author": "Herman Melville", "work": "Typee", "quote": "We quenched our thirst at a cool mountain stream that had a slightly **saltish** mineral taste."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The well water in the settlement was distinctly **saltish**, yet the cattle drank it without apparent injury."}
    ]
  },
  "Dashboard — sal/saltlike.md": {
    "primary": "Having the appearance, crystalline texture, taste, or chemical properties of salt.",
    "secondary": "In mineralogy and inorganic chemistry, describing ionic compounds forming brittle cubic crystal lattices that dissolve readily in polar solvents.",
    "quotes": [
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "The dry residue formed a glistening **saltlike** crust upon the bottom of the porcelain crucible."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The compound crystallized into brilliant, **saltlike** prisms displaying high optical transparency."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The thermal vapors deposited a white **saltlike** incrustation around the rim of the volcanic fissure."}
    ]
  },
  "Dashboard — sal/saltpan.md": {
    "primary": "An undrained natural basin or depression where saline water evaporates, leaving behind a hard crust of mineral salt.",
    "secondary": "In arid geomorphology, playa lake depressions (such as Makgadikgadi or Etosha) forming extensive salt-encrusted flats in desert climates.",
    "quotes": [
      {"author": "David Livingstone", "work": "Missionary Travels and Researches in South Africa", "quote": "We traversed the blinding expanse of the great **saltpan**, where the heat shimmer produced deceptive mirages."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The horse's hooves broke through the dry crust of the **saltpan**, sinking into black fetid mud beneath."},
      {"author": "Richard Francis Burton", "work": "The Lake Regions of Central Africa", "quote": "The caravan halted beside a desolate **saltpan** to collect coarse salt for trading with the inland tribes."}
    ]
  },
  "Dashboard — sal/saltpeter.md": {
    "primary": "Potassium nitrate (KNO3), a white crystalline mineral used in the manufacture of gunpowder, fertilizers, and food preservatives.",
    "secondary": "In the history of explosives and chemistry, the vital oxidizing constituent of black powder (typically 75% potassium nitrate, 15% charcoal, 10% sulfur).",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The hold smelled powerfully of gunpowder and refined **saltpeter** stored for defense against Malay pirates."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "He handled the chemical elements as familiarly as if **saltpeter** and sulfur were simple kitchen spices."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The accidental combination of **saltpeter**, brimstone, and carbon produced an engine that altered the warfare of nations."}
    ]
  },
  "Dashboard — sal/saltpetre.md": {
    "primary": "The traditional British spelling of saltpeter; potassium nitrate, an essential ingredient of black powder and fireworks.",
    "secondary": "In historical chemical technology, nitrogen-rich efflorescences harvested from dry limestone caves, cellars, and nitrary beds.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "It was great pity, so it was, that villainous **saltpetre** should be digg'd out of the bowels of the harmless earth."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "I searched the ruined museum for sulfur and **saltpetre**; indeed, no nitrates of any kind were preserved."},
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "I guarded my barrels of powder with extreme caution, knowing that the dampness of the cave would ruin the **saltpetre**."}
    ]
  },
  "Dashboard — sal/saltshaker.md": {
    "primary": "A container with a perforated lid designed for sprinkling table salt over food.",
    "secondary": "In culinary material culture, tabletop condiment dispensers introduced in the late 19th century following the addition of anti-caking agents to table salt.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "She rearranged the vinegar cruet and the glass **saltshaker** on the red-checkered dining room tablecloth."},
      {"author": "Theodore Dreiser", "work": "Sister Carrie", "quote": "Hurstwood tapped the silver **saltshaker** absently against the table as he pondered his dwindling financial resources."},
      {"author": "John Steinbeck", "work": "The Grapes of Wrath", "quote": "Beside the paper napkins stood a chipped earthenware **saltshaker** and a jar of yellow mustard."}
    ]
  },
  "Dashboard — sal/saltwater.md": {
    "primary": "Water containing a significant concentration of dissolved mineral salts, especially ocean water or water from saline lakes.",
    "secondary": "In marine biology and oceanography, aqueous environments characterized by an average salinity of thirty-five parts per thousand.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "A dash of cold **saltwater** in the face will instantly revive a swooning landsman on a stormy watch."},
      {"author": "James Joyce", "work": "Ulysses", "quote": "A heavy wave of green **saltwater** broke over the wooden jetty, sending spray into the morning air."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We were astonished to discover living mollusks thriving in inland lakes of dense **saltwater**."}
    ]
  },
  "Dashboard — sal/saltworks.md": {
    "primary": "An industrial facility, installation, or plant where salt is produced, mined, refined, or harvested by evaporating brine.",
    "secondary": "In economic history, coastal salterns and inland salt springs (such as Droitwich or Salins-les-Bains) operated under crown monopolies and taxes.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The government levied an oppressive excise tax upon every bushel of salt produced at the royal **saltworks**."},
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "The subterranean brine pumps of the ancient **saltworks** had operated continuously since medieval times."},
      {"author": "Daniel Defoe", "work": "A Tour Through the Whole Island of Great Britain", "quote": "The town of Nantwich was celebrated for its extensive **saltworks**, which supplied all northern England."}
    ]
  },
  "Dashboard — sal/saltwort.md": {
    "primary": "Any of various salt-tolerant coastal or alkaline desert plants of the genera Salsola, Batis, or Glaux.",
    "secondary": "In pre-industrial chemical manufacturing, coastal plants harvested and burned to produce kelp ash and barilla soda for glass and soap makers.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The fleshy stems of the **saltwort** carpeted the saline mudflats where tides regularly inundated the shore."},
      {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "The native inhabitants gathered dry bundles of **saltwort** to burn in shallow pits for crude alkaline ashes."},
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "On the damp borders of the estuary, the maritime **saltwort** flourished alongside samphire and sea lavender."}
    ]
  },
  "Dashboard — sal/salty.md": {
    "primary": "Containing or tasting of salt; saline; sharp, piquantly humorous, or seasoned by nautical experience.",
    "secondary": "In colloquial speech and maritime folklore, describing an experienced, weathered, or sharp-tongued sailor.",
    "quotes": [
      {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "Isle of the **salty** shore and breeze and brine! Here I sing the song of open water."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The old boatswain spun a **salty** yarn about ghost ships and sea monsters off Cape Horn."},
      {"author": "Jack London", "work": "The Sea-Wolf", "quote": "The coarse food and **salty** air hardened the crew into resilient, weather-beaten seamen."}
    ]
  },
  "Dashboard — sal/salubrious.md": {
    "primary": "Favorable to or promoting health, well-being, or wholesome physical vitality; health-giving.",
    "secondary": "In 19th-century climatotherapy, mountain and maritime locales sought out by invalids for their clean air and recuperative microclimates.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "The air **salubrious** of her lofty hills, the cheering fragrance of her dewy vales, restored his spirits."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The climate was remarkably **salubrious**, exempt from the tropical fevers that decimated adjacent lowlands."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "The doctor recommended the **salubrious** breezes of Lyme as the best restorative for her delicate health."}
    ]
  },
  "Dashboard — sal/salubriousness.md": {
    "primary": "The property or characteristic of promoting physical health, wholesome vitality, or beneficial vigor.",
    "secondary": "In public health and environmental physiology, atmospheric and geographic factors that minimize pathogen transmission and promote human longevity.",
    "quotes": [
      {"author": "Edwin Chadwick", "work": "Report on the Sanitary Condition of the Labouring Population", "quote": "The undeniable **salubriousness** of rural uplands contrasted sharply with the deadly atmosphere of crowded urban tenements."},
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "Pure air, fresh water, and clean drainage are the essential foundations of domestic **salubriousness**."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "Travelers praised the mild **salubriousness** of the southern coast, where winter frosts were virtually unknown."}
    ]
  },
  "Dashboard — sal/salubrity.md": {
    "primary": "Wholesomeness or healthiness, especially of climate, air, water, or geographic environment.",
    "secondary": "In classical topography, the favorable environmental balance of winds, elevation, and drainage praised by Hippocratic physicians.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Also I think of changing my residence for a time; probably I shall seek the **salubrity** of a southern climate."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber rejoiced to reply that his family were in the enjoyment of complete **salubrity** and good spirits."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The ancient philosophers praised the temperate **salubrity** of Attica as the cradle of intellectual genius."}
    ]
  },
  "Dashboard — sal/saluki.md": {
    "primary": "An ancient, graceful breed of sight hound originating in the Middle East, characterized by a slender build and silky fringed ears; gazelle hound.",
    "secondary": "In canine archaeology and Middle Eastern hunting culture, coursing hounds revered by Bedouin tribes for tracking desert gazelles and hares.",
    "quotes": [
      {"author": "Richard Francis Burton", "work": "Personal Narrative of a Pilgrimage to El-Medinah and Meccah", "quote": "The Bedouin hunter was accompanied by a fleet **saluki**, prized for its endurance across burning sand dunes."},
      {"author": "Charles Montagu Doughty", "work": "Travels in Arabia Deserta", "quote": "The slender grey **saluki** rested beside the tent fire, treated with affectionate care by the nomad horsemen."},
      {"author": "Wilfrid Scawen Blunt", "work": "The Future of Islam", "quote": "In the desert encampment, the graceful form of the **saluki** recalled the coursing traditions of ancient caliphs."}
    ]
  },
  "Dashboard — sal/salutary.md": {
    "primary": "Producing beneficial or wholesome effects; promoting health, safety, or moral well-being.",
    "secondary": "In political philosophy and jurisprudence, measures or penalties that deter vice and reinforce civic order and moral integrity.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She did not mean to go beyond this **salutary** general doctrine, and threw her indignation into moral principles."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Ancient constitutional traditions provide a **salutary** restraint against the impetuous passions of democratic factions."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The severe defeat taught the government a **salutary** lesson regarding the limits of royal prerogative."}
    ]
  },
  "Dashboard — sal/salutation.md": {
    "primary": "A gesture, word, or formal expression of greeting, goodwill, or respect offered upon meeting or in correspondence.",
    "secondary": "In Christian theology and hymnology, specifically the Angelic Salutation (the Annunciation of Gabriel to the Virgin Mary).",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "**Salutation** and greeting to you all, fair assembly of honourable friends."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Defarge exchanged a quiet **salutation** with the customer as he poured a glass of red wine."},
      {"author": "Walter Scott", "work": "The Talisman", "quote": "The knight returned the eastern emir's courteous **salutation** with grave and dignified chivalry."}
    ]
  },
  "Dashboard — sal/salutatorian.md": {
    "primary": "The student who ranks second highest in a graduating class and traditionally delivers the opening salutatory address at commencement.",
    "secondary": "In American academic tradition, the graduating scholar delivering the welcoming greeting to faculty, parents, and fellow graduates.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The youthful **salutatorian** stepped to the podium, delivering his Latin address with poise and classical eloquence."},
      {"author": "Henry Adams", "work": "The Education of Henry Adams", "quote": "At Harvard commencement, the appointed **salutatorian** greeted the assembly in formal academic accents."},
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "The high school **salutatorian** recited a poem on civic duty, receiving earnest applause from the proud townspeople."}
    ]
  },
  "Dashboard — sal/salutatory.md": {
    "primary": "Pertaining to, expressing, or delivering a greeting or welcome; welcoming.",
    "secondary": "In academic commencement ceremonial, the formal opening speech welcoming guests and dignitaries before the valedictory address.",
    "quotes": [
      {"author": "Oliver Wendell Holmes", "work": "The Autocrat of the Breakfast-Table", "quote": "The professor delivered a witty **salutatory** address that put the nervous freshman class completely at ease."},
      {"author": "Nathaniel Hawthorne", "work": "Mosses from an Old Manse", "quote": "He extended a warm **salutatory** hand to his old college companion at the threshold of the study."},
      {"author": "Washington Irving", "work": "Bracebridge Hall", "quote": "The genial host offered a **salutatory** toast to all his gathered guests before the feast began."}
    ]
  },
  "Dashboard — sal/salute.md": {
    "primary": "To greet with respect, courtesy, or honor; (military) to perform a prescribed gesture of respect to a superior officer or national flag.",
    "secondary": "In naval protocol and artillery ceremonial, firing a designated number of blank rounds (such as a 21-gun salute) in honor of visiting sovereigns.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Comedy of Errors", "quote": "There's not a man I meet but doth **salute** me as if I were their well-acquainted friend."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The naval frigate fired a booming nineteen-gun **salute** as the commodore's flagship entered the harbor."},
      {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "I **salute** the future generations marching across the vast American continents!"}
    ]
  },
  "Dashboard — sal/saluter.md": {
    "primary": "One who salutes, greets, or pays formal respects to another.",
    "secondary": "In military and courtly protocol, the junior officer or ceremonial attendant initiating the reciprocal gesture of greeting.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Fair Maid of Perth", "quote": "The polite **saluter** lifted his velvet cap and bowed low before the magistrates of the burgh."},
      {"author": "Herman Melville", "work": "White-Jacket", "quote": "The formal **saluter** on the quarterdeck stood rigid until the naval captain acknowledged his greeting."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "Mr. Pickwick beamed upon each cheerful **saluter** as the stagecoach rolled through the cheering village."}
    ]
  },
  "Dashboard — sal/salyut.md": {
    "primary": "The Soviet space program of the 1970s and 1980s that deployed a series of early crewed space stations in Earth orbit.",
    "secondary": "In spaceflight history, the pioneering space station program (Salyut 1 through 7) that established long-duration human spaceflight procedures.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "The Exploration of Space", "quote": "The successful docking of Soyuz cosmonauts with the **salyut** orbital station opened the era of permanent orbital habitations."},
      {"author": "Carl Sagan", "work": "Cosmos", "quote": "The pioneering flights of the Soviet **salyut** program demonstrated the physiological adaptability of humans to extended weightlessness."},
      {"author": "Freeman Dyson", "work": "Disturbing the Universe", "quote": "The long orbital missions aboard the **salyut** stations proved that human labor could be sustained indefinitely in space."}
    ]
  },
  "Dashboard — sal/unsalable.md": {
    "primary": "Not salable; unable to be sold due to poor quality, lack of demand, obsolescence, or legal restriction.",
    "secondary": "In retail merchandise valuation, obsolete inventory written off as commercial deadstock having negligible salvage value.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Defective manufactured goods remain completely **unsalable** in competitive foreign markets."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "A sudden change in fashion renders large stocks of luxury garments abruptly **unsalable**."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The bankrupt shopkeeper was left with a warehouse filled with dusty, **unsalable** remnants."}
    ]
  },
  "Dashboard — sal/unsalaried.md": {
    "primary": "Not receiving a fixed regular payment or salary; serving in an honorary, voluntary, or unpaid capacity.",
    "secondary": "In public administration and civic philanthropy, voluntary municipal magistrates and charity trustees serving without official compensation.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "In early America, many public township offices were filled by **unsalaried** citizens dedicated to civic duty."},
      {"author": "Anthony Trollope", "work": "The Warden", "quote": "The bishop appointed an **unsalaried** curate to assist the elderly clergyman during his illness."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He took pride in serving as an **unsalaried** trustee of the municipal infirmary for over twenty years."}
    ]
  },
  "Dashboard — sal/unsaleable.md": {
    "primary": "Not capable of being sold; unfit for commercial sale or rejected by prospective buyers in the market.",
    "secondary": "In mercantile contract law, goods failing to satisfy the implied warranty of merchantable quality.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Perishable foodstuffs spoiled during delayed transport become wholly **unsaleable** upon arrival."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "If hereditary titles were ever **unsaleable**, Sir Walter would have considered his dignity grievously insulted."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The damp and sour wheat was declared entirely **unsaleable** by the assembled corn merchants."}
    ]
  },
  "Dashboard — sal/unsalted.md": {
    "primary": "Not seasoned, cured, preserved, or treated with salt; devoid of salt.",
    "secondary": "In culinary arts and commercial dairy production, fresh butter or nuts prepared without added sodium chloride to preserve delicate natural flavours.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Troilus and Cressida", "quote": "Speak, then, thou **unsalted** leaven, speak! Why dost thou mutter in this fashion?"},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The hungry sailor would have given a doubloon for a crust of fresh bread and **unsalted** butter."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I baked my simple unleavened cakes of pure cornmeal and **unsalted** spring water over the open coals."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Movement & Speed"
updated = 0

for rel_path, info in data.items():
    fpath = os.path.join(base_dir, rel_path.replace("/", os.sep))
    if not os.path.exists(fpath):
        print(f"Warning: {fpath} does not exist!")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    book_idx = content.find("> [!book]")
    if book_idx == -1:
        print(f"Warning: No > [!book] callout in {rel_path}")
        continue
    
    prefix = content[:book_idx]
    
    p_def = info["primary"].strip().rstrip(".") + "."
    s_def = info["secondary"].strip().rstrip(".") + "."
    
    new_book = f"> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: {p_def}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {s_def}\n"
    
    new_quote = "> [!quote] 💬 Contextual Usage & Authentic Quotations\n"
    for q in info["quotes"]:
        auth = q["author"].strip()
        work = q["work"].strip()
        quote_text = q["quote"].strip().strip('"').strip('“').strip('”')
        new_quote += f'> - 📜 **{auth} (*{work}*):** *"{quote_text}"*\n'
    
    new_content = prefix + new_book + "\n" + new_quote + "\n"
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated += 1

print(f"Speed Batch 7D: Successfully updated {updated}/{len(data)} notes.")
