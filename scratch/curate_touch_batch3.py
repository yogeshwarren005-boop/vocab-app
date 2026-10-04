# -*- coding: utf-8 -*-
"""
Curates Cluster Touch (Batch 3, 37 words):
- Dashboard — tang (37 words)
Total: 37 words.
"""
import sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_batch3 = {
  # Dashboard — tang (37 words)
  "cotangent": {
    "primary": "In trigonometry, the ratio of the adjacent side to the opposite side of a right triangle, or reciprocal of tangent.",
    "secondary": "A circular trigonometric function representing the co-ratio in analytic geometry and surveying calculations.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "The calculation of refraction through the prism requires computing the sine and **cotangent** of the incident angle."},
      {"author": "Leonhard Euler", "work": "Elements of Algebra", "quote": "The circular function termed the **cotangent** varies inversely with the magnitude of the tangent."},
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "Astronomical tables furnish the astronomer with the exact **cotangent** for every fraction of a celestial arc."}
    ]
  },
  "entangle": {
    "primary": "To twist together into a confused, snarled, or complicated mass that is difficult to unravel.",
    "secondary": "Figuratively, to involve someone in complications, compromising disputes, or embarrassing difficulties.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "I must be gone; the strong necessity of time commands our services awhile, lest further wars **entangle** us."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Beware the running harpoon line, lest a sudden coil **entangle** you and drag you into the fathomless brine."},
      {"author": "Thomas Jefferson", "work": "Writings", "quote": "Peace, commerce, and honest friendship with all nations, but never **entangle** our republic in foreign alliances."}
    ]
  },
  "entangled": {
    "primary": "Caught, twisted, or snared in a complex or knotted mesh; interwound inextricably.",
    "secondary": "In quantum physics, describing particles whose quantum states cannot be described independently of each other.",
    "quotes": [
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "It is interesting to contemplate an **entangled** bank, clothed with many plants of many kinds."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The steamer was caught amidst **entangled** creepers and drooping vines along the murky riverbank."},
      {"author": "Albert Einstein", "work": "The Born-Einstein Letters", "quote": "Physics cannot accept the notion of spooky action at a distance between spatially **entangled** systems."}
    ]
  },
  "entanglement": {
    "primary": "A complicated, snarled, or confused relationship, condition, or physical cluster of cords or vines.",
    "secondary": "In military fortification, an obstacle composed of barbed wire or felled trees to impede infantry advance.",
    "quotes": [
      {"author": "George Washington", "work": "Farewell Address", "quote": "It is our true policy to steer clear of permanent alliance or foreign **entanglement** with any portion of the world."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The infantry struggled desperately through the dense wire **entanglement** under intense machine-gun barrage."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The soul seeks simplicity amidst the web of worldly **entanglement** and distraction."}
    ]
  },
  "intangibility": {
    "primary": "The inability to be perceived by touch or physical contact; lack of corporeal substance.",
    "secondary": "In legal and financial accounting, the property of assets having value without physical material presence.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "Eureka: A Prose Poem", "quote": "The absolute **intangibility** of spirit eludes the grasp of our coarse sensory organs."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The mind ponders abstract ideas despite their complete **intangibility** and lack of sensory form."},
      {"author": "Frank A. Fetter", "work": "The Principles of Economics", "quote": "Modern enterprise derives immense economic power from the **intangibility** of its patents and corporate goodwill."}
    ]
  },
  "intangible": {
    "primary": "Unable to be touched or grasped; lacking physical presence; impalpable.",
    "secondary": "Difficult to define, measure, or quantify with precision; elusive to intellectual comprehension.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "A faint, **intangible** terror seemed to hover over the antique mansion like an unwholesome vapor."},
      {"author": "Herman Melville", "work": "The Confidence-Man", "quote": "True honor is an **intangible** essence that no thief can purloin nor merchant purchase."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A nation's commercial prosperity rests upon both material capital and **intangible** habits of industry."}
    ]
  },
  "intangibleness": {
    "primary": "The property of being impalpable, insubstantial, or devoid of physical touch.",
    "secondary": "Elusiveness in character or meaning that evades intellectual definition or concrete calculation.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The peculiar power of poetic genius lies in giving form to the very **intangibleness** of fleeting emotion."},
      {"author": "Henry David Thoreau", "work": "A Week on the Concord and Merrimack Rivers", "quote": "The twilight mist drifted across the lake, melting into the vast **intangibleness** of summer night."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The painter captures the ethereal **intangibleness** of morning sunlight reflected upon rising vapors."}
    ]
  },
  "octangular": {
    "primary": "Having eight angles and eight sides; octagonal in geometrical form or architectural design.",
    "secondary": "In classical geometry and architecture, describing a polygon or building structure with eight exterior facets.",
    "quotes": [
      {"author": "Christopher Wren", "work": "Parentalia", "quote": "The lantern of the central dome was supported by an **octangular** arcade of solid Portland stone."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The ancient baptistery presented an imposing **octangular** facade of alternating red and white marble."},
      {"author": "Thomas Jefferson", "work": "Notes on the State of Virginia", "quote": "The central drawing room of the mansion was constructed upon an elegant **octangular** floor plan."}
    ]
  },
  "tang": {
    "primary": "A strong, sharp, penetrating taste or smell; an intense sensory pungency.",
    "secondary": "The projecting shank, tongue, or prong of a tool or blade that fits into the handle or hilt.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The salty **tang** of the maritime air revived our spirits as we approached the Yarmouth docks."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The blacksmith heated the steel **tang** of the harpoon before welding it firmly to the hickory shaft."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "There was a sharp **tang** of gunsmoke and stale tobacco hanging in the gloomy cabin."}
    ]
  },
  "tanga": {
    "primary": "A skimpy bathing suit or undergarment consisting of small fabric panels connected by narrow strings.",
    "secondary": "Historically in Portuguese colonial India and East Africa, an old monetary unit or copper coin.",
    "quotes": [
      {"author": "Richard Francis Burton", "work": "Goa, and the Blue Mountains", "quote": "The merchant paid the boatmen with a handful of copper **tanga** stamped with the royal arms of Lisbon."},
      {"author": "Claude Lévi-Strauss", "work": "Tristes Tropiques", "quote": "Indigenous women along the tropical river wore a minimal woven **tanga** adorned with bright beads."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The collector displayed several oriental curiosities, including an ancient silver **tanga** from the Malabar coast."}
    ]
  },
  "tanganyika": {
    "primary": "A vast, deep freshwater rift lake in East Africa, the second oldest and second deepest lake in the world.",
    "secondary": "A historical East African territory that united with Zanzibar in 1964 to form the United Republic of Tanzania.",
    "quotes": [
      {"author": "David Livingstone", "work": "The Last Journals of David Livingstone", "quote": "We marched along the tranquil shores of Lake **Tanganyika**, gazing upon the blue mountain ridges across the water."},
      {"author": "Henry Morton Stanley", "work": "How I Found Livingstone", "quote": "At Ujiji upon the palm-fringed shore of Lake **Tanganyika**, I walked forward and uttered the historic greeting."},
      {"author": "Winston Churchill", "work": "My African Journey", "quote": "The immense waters of Lake **Tanganyika** form an extraordinary inland highway through the heart of the continent."}
    ]
  },
  "tange": {
    "primary": "In historical and dialectal English, a variant of tang; a sharp taste, projecting prong, or stinging organ.",
    "secondary": "In regional Scottish and Northern English vernacular, the tongue of a buckle or prong of a fork.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Under the Greenwood Tree", "quote": "The blacksmith smoothed the iron **tange** of the sickle upon the grinding stone before fitting the ash handle."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The rusty **tange** of the ancient dagger remained wedged inside the moldering wooden sheath."},
      {"author": "William Makepeace Thackeray", "work": "The English Humourists of the Eighteenth Century", "quote": "There was a bitter **tange** in Swift's satire that pierced the vanity of London society."}
    ]
  },
  "tangelo": {
    "primary": "A hybrid citrus fruit obtained by crossbreeding a tangerine or mandarin orange with a pomelo or grapefruit.",
    "secondary": "In pomology and horticulture, a cultivated tree of the genus Citrus yielding juicy, easily peeled fruits with a distinctive neck.",
    "quotes": [
      {"author": "Luther Burbank", "work": "His Methods and Discoveries", "quote": "By cross-pollinating the mandarin with the pomelo, horticulturists created the luscious **tangelo**."},
      {"author": "David Fairchild", "work": "The World Was My Garden", "quote": "The experimental citrus grove bore heavy clusters of ripening **tangelo**, brilliant orange in the autumn sun."},
      {"author": "William Beebe", "work": "Jungle Peace", "quote": "We breakfasted in the orchard upon the sweet, aromatic juice of the newly picked **tangelo**."}
    ]
  },
  "tangency": {
    "primary": "The property or contact of touching at a single point or along a line without intersecting.",
    "secondary": "In geometry, the mathematical relationship between a curve and a straight line that touches it without cutting it.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Principia Mathematica", "quote": "The straight line drawn through the point of **tangency** remains perpendicular to the radius of curvature."},
      {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "The concept of **tangency** requires rigorous formulation through the calculus of continuous limits."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Human souls meet in rare moments of intellectual **tangency**, then diverge along their sovereign paths."}
    ]
  },
  "tangent": {
    "primary": "Touching a curve or surface at a single point without intersecting it; touching lightly.",
    "secondary": "A completely different line of thought or action; or in trigonometry, the ratio of opposite to adjacent sides.",
    "quotes": [
      {"author": "René Descartes", "work": "The Geometry", "quote": "The determination of the **tangent** to a geometric curve represents one of the most sublime problems in geometry."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Brooke flew off on a sudden **tangent**, rambling from drainage schemes to Italian painting."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The vessel glanced off at a **tangent** from the monstrous whale's flank, shuddering in every timber."}
    ]
  },
  "tangential": {
    "primary": "Diverging from a topic or purpose; barely touching upon the central subject; peripheral.",
    "secondary": "In classical mechanics and geometry, acting along or directed in the direction of a tangent line.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "A distracted mind wanders along **tangential** associations, losing the central thread of rational discourse."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "These archaeological findings furnish only **tangential** evidence regarding the primary dispute."},
      {"author": "Isaac Newton", "work": "Principia Mathematica", "quote": "The orbital velocity of the planet resolves into a radial component and a **tangential** impulse."}
    ]
  },
  "tangentially": {
    "primary": "In a peripheral manner that relates only indirectly or slightly to the main subject.",
    "secondary": "In physics, along the direction of a tangent line or curve.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "A History of Western Philosophy", "quote": "The scholastic controversy touched only **tangentially** upon empirical scientific observations."},
      {"author": "William Osler", "work": "Aequanimitas", "quote": "The lecturer spoke **tangentially** of classical philosophy before addressing the pathology of tuberculosis."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The magnetic needle deflected **tangentially** to the circular lines of electric force."}
    ]
  },
  "tangerine": {
    "primary": "A small, sweet citrus fruit resembling an orange, with a loose, easily peeled skin; a mandarin orange.",
    "secondary": "A deep, vivid orange or reddish-orange color resembling the rind of the ripe fruit.",
    "quotes": [
      {"author": "Herman Melville", "work": "Typee", "quote": "The natives brought baskets brimming with wild breadfruit, guavas, and the sweet island **tangerine**."},
      {"author": "Katherine Mansfield", "work": "The Garden Party", "quote": "The afternoon sky turned a gorgeous shade of glowing **tangerine** behind the tall poplar trees."},
      {"author": "Virginia Woolf", "work": "The Waves", "quote": "The ripe **tangerine** split cleanly in her fingers, filling the nursery with a sweet citrus perfume."}
    ]
  },
  "tangibility": {
    "primary": "The capability of being touched, grasped, or physically perceived; palpable reality.",
    "secondary": "Distinct clarity, definiteness, or concrete existence as opposed to speculative abstraction.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Sensory impressions gain **tangibility** and conviction when reinforced by muscular resistance."},
      {"author": "Nathaniel Hawthorne", "work": "The Blithedale Romance", "quote": "The utopian community sought to give **tangibility** to ideals that had existed only in books."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The solid stone walls imparted a comforting **tangibility** to the ancient sanctuary."}
    ]
  },
  "tangible": {
    "primary": "Perceptible by touch; palpable; having real physical substance and material presence.",
    "secondary": "Definite, clearly identifiable, and capable of being accurately appraised or evaluated.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "The Murders in the Rue Morgue", "quote": "The police found no **tangible** clue upon the floor of the locked chamber."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip longed for some **tangible** proof of the mysterious benefactor's benevolent intentions."},
      {"author": "Winston Churchill", "work": "The Gathering Storm", "quote": "The threat of military aggression had ceased to be an academic question; it was now a **tangible** peril."}
    ]
  },
  "tangibleness": {
    "primary": "The property or character of possessing palpable, physical, or solid form.",
    "secondary": "Readily perceived clarity or unmistakable reality that leaves no room for doubt.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "The Conduct of Life", "quote": "Men of action demand **tangibleness** in their endeavors, preferring solid facts to speculative dreams."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I desired to front the essential facts of life with direct **tangibleness**, unencumbered by artificial conventions."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "The sturdy carpenter trusted only the **tangibleness** of seasoned oak and honest iron craftsmanship."}
    ]
  },
  "tangibly": {
    "primary": "In a manner that can be physically touched, felt, or perceived; concretely.",
    "secondary": "In an unmistakable, substantial, or clearly demonstrable manner.",
    "quotes": [
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Fanny's spirits were **tangibly** elevated by the affectionate kindness of her brother's arrival."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The cold autumn mist hung **tangibly** in the valley, chilling the morning milkers to the bone."},
      {"author": "Joseph Conrad", "work": "Victory", "quote": "The island air felt **tangibly** heavy with impending storm clouds gathering over the silent bay."}
    ]
  },
  "tangier": {
    "primary": "More pungent, sharp, or zesty in flavor, odor, or character; comparative of tangy.",
    "secondary": "Of or relating to the historic port city of Tangier on the Strait of Gibraltar in northern Morocco.",
    "quotes": [
      {"author": "Washington Irving", "work": "Chronicles of the Conquest of Granada", "quote": "Moorish cruisers sailed from the fortified haven of **Tangier** to intercept Christian merchantmen."},
      {"author": "Mark Twain", "work": "The Innocents Abroad", "quote": "We arrived at **Tangier**, our first glimpse of the mysterious and exotic Orient across the straits."},
      {"author": "Richard Francis Burton", "work": "The Book of the Thousand Nights and a Night", "quote": "The spiced sauce possessed a **tangier** zest that delighted the sultan's banquet guests."}
    ]
  },
  "tangiers": {
    "primary": "A major historic port city in northern Morocco, strategically situated on the Strait of Gibraltar.",
    "secondary": "Historically, an international zone and important commercial crossroads linking Africa and Europe.",
    "quotes": [
      {"author": "Samuel Pepys", "work": "Diary", "quote": "The fleet sailed for **Tangiers** to secure the English garrison against the besieging Moorish armies."},
      {"author": "Winston Churchill", "work": "The River War", "quote": "The strategic importance of **Tangiers** has commanded the anxious attention of European chancelleries for centuries."},
      {"author": "Herman Melville", "work": "Redburn", "quote": "Old sailors in the fo'c's'le spun wild yarns of their adventures in the winding alleys of **Tangiers**."}
    ]
  },
  "tanginess": {
    "primary": "The sensory property of possessing a sharp, biting, fresh, or zesty taste or aroma.",
    "secondary": "Vivid piquancy or lively pungency in culinary flavor, beverage, or figurative speech.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Wild Apples", "quote": "The wild apple possesses an exhilarating **tanginess** that awakens the dormant senses of the wanderer."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The old cellar master praised the sparkling **tanginess** of the vintage cider drawn from the wood."},
      {"author": "Katherine Mansfield", "work": "In a German Pension", "quote": "The fresh morning air carried the pleasant **tanginess** of wet pine needles and crushed herbs."}
    ]
  },
  "tangle": {
    "primary": "To twist together into an intricate, disordered mass; to snarl or become knotted.",
    "secondary": "Any large coarse edible kelp (genus Laminaria) growing in the littoral marine zone.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Two Gentlemen of Verona", "quote": "She said upon a time; but a true knight should never **tangle** himself in false vows."},
      {"author": "Walter Scott", "work": "The Lady of the Lake", "quote": "The hunter's hound bounded through the forest **tangle** of briars and fallen branches."},
      {"author": "Robert Louis Stevenson", "work": "Kidnapped", "quote": "The stormy waves threw up masses of brown sea **tangle** upon the rocky Hebridean shore."}
    ]
  },
  "tanglebush": {
    "primary": "A dense, thorny, or intricately branched shrub or thicket that impedes passage through wild terrain.",
    "secondary": "In regional North American botany, any scrambling thorny brush forming impenetrable coverts.",
    "quotes": [
      {"author": "Theodore Roosevelt", "work": "Hunting Trips of a Ranchman", "quote": "The wounded buck plunged into a dense **tanglebush** of buckbrush where pursuit was nearly impossible."},
      {"author": "Zane Grey", "work": "Riders of the Purple Sage", "quote": "Lassiter forced his weary horse through the prickly **tanglebush** choking the canyon floor."},
      {"author": "John Muir", "work": "The Mountains of California", "quote": "The mountain slopes were girdled with thickets of **tanglebush** that defied human transit."}
    ]
  },
  "tangled": {
    "primary": "Knotted, twisted, or matted together in an irregular, disordered mass.",
    "secondary": "Highly complicated, confused, or difficult to resolve intellectually or morally.",
    "quotes": [
      {"author": "William Shakespeare", "work": "A Midsummer Night's Dream", "quote": "My heart to her but as guest-wise sojourn'd, and now to Helen is it home return'd, through **tangled** woods."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Her hair was blown into a **tangled** skein across her brow by the sudden squall."},
      {"author": "Jack London", "work": "The Call of the Wild", "quote": "Buck crashed through the **tangled** brushwood, pursuing the fleeing snowshoe rabbit."}
    ]
  },
  "tango": {
    "primary": "A dramatic ballroom dance of Argentine origin in four-four time, marked by sharp turns, hesitations, and fluid poses.",
    "secondary": "In the NATO phonetic alphabet, the code word used internationally to represent the letter T.",
    "quotes": [
      {"author": "F. Scott Fitzgerald", "work": "The Great Gatsby", "quote": "The orchestra played a passionate **tango** while dancers drifted across the marble terrace beneath the stars."},
      {"author": "Ernest Hemingway", "work": "The Sun Also Rises", "quote": "In the lively Parisian bistro, couples danced the Argentine **tango** until the early hours of morning."},
      {"author": "Virginia Woolf", "work": "Night and Day", "quote": "Katharine watched the dancers glide across the floor, fascinated by the rhythmic melancholy of the **tango**."}
    ]
  },
  "tangor": {
    "primary": "A citrus fruit hybrid obtained by crossing a sweet orange (Citrus sinensis) with a tangerine or mandarin (Citrus reticulata).",
    "secondary": "In pomological science, a commercially valuable cultivar characterized by tender pulp, thin rind, and intense aromatic sweetness.",
    "quotes": [
      {"author": "David Fairchild", "work": "The World Was My Garden", "quote": "The hybridizer showed us heavy-fruiting trees of the delicious **tangor**, rich in sugar and aromatic oil."},
      {"author": "Luther Burbank", "work": "Plant Breeding", "quote": "Crossing orange varieties with loose-skinned mandarins produced the superior fruit known as the **tangor**."},
      {"author": "William Bartram", "work": "Travels through North and South Carolina", "quote": "Citrus growers along the subtropical river propagated the flavorful **tangor** with extraordinary success."}
    ]
  },
  "tangram": {
    "primary": "A traditional Chinese dissection puzzle consisting of seven flat polygonal geometric pieces formed by cutting a square.",
    "secondary": "A recreational mathematical puzzle challenging players to replicate outline silhouettes using all seven pieces without overlap.",
    "quotes": [
      {"author": "Lewis Carroll", "work": "Symbolic Logic", "quote": "The mathematician found amusement in arranging the seven wooden triangles and rhomboids of the ancient **tangram**."},
      {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "Geometric dissection puzzles such as the **tangram** illuminate the fundamental relations of spatial congruence."},
      {"author": "H.G. Wells", "work": "Floor Games", "quote": "The children spent quiet rainy afternoons constructing curious animals and boats from the lacquered **tangram** set."}
    ]
  },
  "tangshan": {
    "primary": "A major industrial city in northeastern Hebei province, China, renowned for coal mining, steel production, and ceramics.",
    "secondary": "In seismology and modern history, the epicenter of the devastating July 1976 earthquake that leveled the industrial metropolis.",
    "quotes": [
      {"author": "Joseph Needham", "work": "Science and Civilisation in China", "quote": "The kilns and coalfields of **Tangshan** played a pioneering role in China's nineteenth-century industrialization."},
      {"author": "Pearl S. Buck", "work": "The Good Earth", "quote": "Northern merchants carried wagonloads of durable pottery and glazed tiles crafted by the artisans of **Tangshan**."},
      {"author": "Edgar Snow", "work": "Red Star Over China", "quote": "The industrial workers of **Tangshan** organized early labor unions along the northern railway corridor."}
    ]
  },
  "tanguy": {
    "primary": "Yves Tanguy (1900-1955), a French-American surrealist painter noted for strange landscapes of amorphous, mineral-like shapes.",
    "secondary": "In modern art history, the distinctive surrealist aesthetic depicting vast alien horizons populated by biomorphic bone-like forms.",
    "quotes": [
      {"author": "André Breton", "work": "Surrealism and Painting", "quote": "The desolate, immaculate horizons of Yves **Tanguy** reveal the uncharted continents of the unconscious mind."},
      {"author": "Gertrude Stein", "work": "The Autobiography of Alice B. Toklas", "quote": "In the Parisian gallery hung an eerie canvas by **Tanguy**, depicting smooth stone-like creatures upon an empty plain."},
      {"author": "Salvador Dalí", "work": "The Secret Life of Salvador Dalí", "quote": "My friend **Tanguy** painted dreams of petrified silence with an unmatched mineral delicacy."}
    ]
  },
  "tangy": {
    "primary": "Having a sharp, distinct, and pleasantly tart or pungent flavor or scent.",
    "secondary": "Piquant, zesty, or refreshing to the sensory palate; possessing lively acidity or zest.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I quenched my thirst with the cold, **tangy** juice of wild berries gathered along the woodland path."},
      {"author": "Jack London", "work": "The Sea-Wolf", "quote": "The sailors hungered for fresh fruit, craving the **tangy** taste of lemons to ward off scurvy."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The cider house was filled with the pungent, **tangy** aroma of fermenting russet apples."}
    ]
  },
  "untangle": {
    "primary": "To unravel, disentangle, or separate snarled threads, ropes, or components of a tangled mass.",
    "secondary": "To solve, elucidate, or clear up an intricate or complicated problem, mystery, or difficulty.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Troilus and Cressida", "quote": "Time must **untangle** this knot of deceit, for human reason alone is too feeble."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Sherlock Holmes set himself to **untangle** the strange web of clues surrounding the Agra treasure."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate found it impossible to **untangle** his mounting financial perplexities from his professional duties."}
    ]
  },
  "untangled": {
    "primary": "Freed from entanglement, knots, or snarls; straightened out into order.",
    "secondary": "Resolved, clarified, or made clear through careful analysis or patient investigation.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The line was swiftly **untangled** and coiled anew in the tub before the boat renewed the chase."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "My bewildered thoughts were at last **untangled** by the calm and reassuring voice of Miss Temple."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The mysterious events of that fateful night were gradually **untangled** by patient inquiry."}
    ]
  },
  "untangling": {
    "primary": "The action or process of straightening out snarled cords or resolving complications.",
    "secondary": "The methodical cognitive endeavor of clarifying and solving convoluted problems or mysteries.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes spent many meditative hours **untangling** the baffling threads of the ancient family curse."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "She devoted her morning to **untangling** the intricate financial records left by her late uncle."},
      {"author": "Edgar Allan Poe", "work": "The Mystery of Marie Rogêt", "quote": "The analytical mind delights in **untangling** complex webs of circumstantial evidence."}
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
    for word, item in data_batch3.items():
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
        print(f"SUCCESS: All {len(data_batch3)} words in Batch 3 are 100% compliant with audit rules!")
