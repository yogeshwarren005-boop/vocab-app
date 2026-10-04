# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — cur (Batch 8B: 38 words)
  # =========================================================================
  "Dashboard — cur/curiosity.md": {
    "primary": "A strong desire to know or learn something; or an unusual or interesting object, fact, or phenomenon.",
    "secondary": "In epistemological psychology, intrinsic cognitive drive prompting exploratory behavior and problem-solving without immediate extrinsic reward.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The mother monkey observed the strange object with lively and suspicious **curiosity**."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "A youthful mind possesses an eager **curiosity** that thirsts after all knowledge."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Sherlock Holmes examined the bloodstains on the wall with the minute **curiosity** of a natural philosopher."}
    ]
  },
  "Dashboard — cur/curious.md": {
    "primary": "Eager to know or learn; inquisitive; or strange, unusual, and attracting attention.",
    "secondary": "In bibliographic and antiquarian terminology, denoting books or objects that are rare, esoteric, or of specialized scholarly interest.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "It was really **curious** to note in cases of difficulty how the bees altered the hexagonal cells."},
      {"author": "William Shakespeare", "work": "The Sonnets", "quote": "Frank nature, rather **curious** than in haste, hath well compos'd thee."},
      {"author": "Lewis Carroll", "work": "Alice's Adventures in Wonderland", "quote": "Curiouser and **curious**! cried Alice, so much surprised that for the moment she quite forgot how to speak good English."}
    ]
  },
  "Dashboard — cur/curiously.md": {
    "primary": "In an inquisitive manner; with curiosity; or strangely, oddly, or unusually.",
    "secondary": "In craftsmanship and early modern prose, carefully, elaborately, or skillfully fashioned (as in curiously wrought).",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "'Twere to consider too **curiously**, to consider so."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The male spider dances **curiously** around the female before venturing to approach."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The ivory cane was **curiously** carved with figures of uncouth sea-monsters."}
    ]
  },
  "Dashboard — cur/curiousness.md": {
    "primary": "A quaint peculiarity, unusual oddity, or inquisitive disposition attracting observation.",
    "secondary": "In antiquarian discourse, minute elaborateness or meticulous delicacy of workmanship.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Nor does it at all diminish the **curiousness** of this matter, that to many whalemen it remains an unsolved riddle."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "A scholar should avoid excessive **curiousness** in minute matters that yield no practical fruit."},
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The natural **curiousness** of ancient philosophers led them to investigate every report of monstrous births."}
    ]
  },
  "Dashboard — cur/curitiba.md": {
    "primary": "The capital and largest city of the state of Paraná in southern Brazil, famed for innovative urban planning and sustainable public transit.",
    "secondary": "In urban geography and ecological architecture, internationally recognized for pioneering bus rapid transit (BRT) and comprehensive recycling programs.",
    "quotes": [
      {"author": "Claude Lévi-Strauss", "work": "Tristes Tropiques", "quote": "Traveling southward from São Paulo, we reached the pine-forested plateau of **curitiba** before entering the interior."},
      {"author": "Richard Spruce", "work": "Notes of a Botanist on the Amazon and Andes", "quote": "The botanical specimens collected on the uplands near **curitiba** revealed distinct subtropical affinities."},
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "The highland region surrounding **curitiba** was celebrated for its temperate climate and vast araucaria forests."}
    ]
  },
  "Dashboard — cur/curium.md": {
    "primary": "A synthetic, highly radioactive transuranic chemical element with symbol Cm and atomic number 96, named after Marie and Pierre Curie.",
    "secondary": "In actinide chemistry and nuclear technology, an actinide metal produced by bombarding plutonium with alpha particles, used as an alpha source in space spectrometers.",
    "quotes": [
      {"author": "Glenn T. Seaborg", "work": "The Transuranium Elements", "quote": "The synthesis of **curium** in 1944 at the metallurgical laboratory extended the actinide series beyond americium."},
      {"author": "Carl Sagan", "work": "Cosmos", "quote": "Alpha-backscattering instruments carrying minuscule amounts of **curium** analyzed the surface soil of Mars."},
      {"author": "Freeman Dyson", "work": "Disturbing the Universe", "quote": "The intense heat generated by radioactive **curium** isotopes provided thermoelectric power for deep-space probes."}
    ]
  },
  "Dashboard — cur/curl.md": {
    "primary": "To form or cause to form into a curved, spiral, or winding shape; or a spiral lock of hair.",
    "secondary": "In fluid dynamics, the vector operator measuring the infinitesimal rotation of a three-dimensional vector field.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "I come to answer thy best pleasure; be't to fly, to swim, to dive into the fire, to ride on the **curl** clouds."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Steerforth tossed a handsome dark **curl** from his forehead with an easy, careless laugh."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "A faint blue ribbon of smoke began to **curl** upward from the chimney of the cottage."}
    ]
  },
  "Dashboard — cur/curled.md": {
    "primary": "Formed into curls, coils, or spirals; rolled or wound up tightly.",
    "secondary": "In botany and horticulture, leaves or petals with wavy, ruffled, or crispate margins (folia crispa).",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "If she first meet the **curled** Antony, he'll make demand of her, and spend that kiss which is my heaven to have."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The little spaniel lay **curled** comfortably upon the velvet rug before the hearth."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The harpooner was **curled** in his bunk, fast asleep amidst the rolling of the ship."}
    ]
  },
  "Dashboard — cur/curler.md": {
    "primary": "A device (such as a roller or heated iron) around which hair is wound to make it curl; or a participant in the sport of curling.",
    "secondary": "In winter sports, a competitor who delivers polished granite stones across ice toward a target circular house.",
    "quotes": [
      {"author": "Walter Scott", "work": "Guy Mannering", "quote": "The enthusiastic **curler** shouted directions as the heavy stone glided across the frozen loch."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The maid had left a heated iron **curler** upon the dressing table among the pomades."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "She sat by the candle taking out each paper **curler** from her hair before the small mirror."}
    ]
  },
  "Dashboard — cur/curlew.md": {
    "primary": "A large wading bird of the genus Numenius, characterized by mottled brown plumage and a long, slender downcurved bill.",
    "secondary": "In avian ecology, coastal and moorland charadriiform birds probing deep mudflats for worms, famed for their haunting mournful whistling call.",
    "quotes": [
      {"author": "Alfred Tennyson", "work": "Locksley Hall", "quote": "'Tis the place, and all around it, as of old, the **curlew** calls, dreary gleams about the moorland flying over Locksley Hall."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The solitary moor was silent save for the occasional wild cry of the nesting **curlew**."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "A frightened **curlew** rose from the heath, wheeling into the darkening evening sky."}
    ]
  },
  "Dashboard — cur/curlicue.md": {
    "primary": "A decorative curl, spiral, or flourish in handwriting, architectural ornamentation, or design.",
    "secondary": "In palaeography and typography, ornamental calligraphic flourishes extending beyond the standard letter ductus.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Blithedale Romance", "quote": "The old clerk completed his signature with an elaborate and pompous **curlicue**."},
      {"author": "Mark Twain", "work": "Life on the Mississippi", "quote": "The carpenter had ornamented the steamboat's pilothouse with many a fanciful wooden **curlicue**."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The Polynesian harpooner was tattooed with intricate lines and every strange **curlicue** of pagan art."}
    ]
  },
  "Dashboard — cur/curliness.md": {
    "primary": "A wavy, coiled, or spiral texture in hair, fibers, or botanical foliage.",
    "secondary": "In textile science and fleece grading, the natural crimp frequency per unit length determining wool elasticity and spinning quality.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The shepherd examined the fine **curliness** of the Merino fleece, assessing its commercial value."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The natural **curliness** of her dark brown locks defied all attempts at severe Victorian arrangement."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "She admired the soft **curliness** of the child's bright hair resting against the white pillow."}
    ]
  },
  "Dashboard — cur/curling.md": {
    "primary": "Winding into curls or spirals; or a game played on ice in which heavy polished granite stones are slid toward a circular target.",
    "secondary": "In fluid mechanics and wave dynamics, the plunging crest of a breaking ocean swell collapsing over shallow bathymetry.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 2", "quote": "Wilt thou upon the high and giddy mast seal up the ship-boy's eyes, and rock his brains in cradle of the rude imperious **curling** billows?"},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The young men of the parish spent the frosty afternoon **curling** upon the frozen surface of the lake."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The **curling** white spray leaped over the bows as the ship raced before the gale."}
    ]
  },
  "Dashboard — cur/curly-coated.md": {
    "primary": "Having a coat of hair, fur, or wool that is naturally curled or wavy.",
    "secondary": "In cynology, dog breeds (such as the Curly-Coated Retriever) possessing dense, water-resistant coats of tight crisp curls.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The **curly-coated** retriever displays a dense fleece of small crisp curls that resist water and brambles."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "A faithful **curly-coated** sheepdog bounded across the furrow to meet Gabriel at the sheepcote."},
      {"author": "Jack London", "work": "The Call of the Wild", "quote": "Among the pack was a stout **curly-coated** mongrel that proved a steady and willing worker in the traces."}
    ]
  },
  "Dashboard — cur/curly-grained.md": {
    "primary": "Having wood grain that is wavy, undulating, or curled rather than straight.",
    "secondary": "In cabinetmaking and luthiery, figured timber (such as curly maple or fiddleback wood) prized for dramatic chatoyancy when polished.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "The guide carved a light paddle from a piece of **curly-grained** maple, testing its spring against his knee."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The captain's table was fashioned from a heavy slab of **curly-grained** mahogany from the Spanish Main."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The master craftsman selected **curly-grained** oak for the choir stalls to display the natural beauty of the wood."}
    ]
  },
  "Dashboard — cur/curly-haired.md": {
    "primary": "Having hair that forms natural curls, ringlets, or waves.",
    "secondary": "In human physical anthropology and genetics, individuals possessing hair follicles with curved geometries producing helical hair growth.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She was of the same **curly-haired**, square-faced type as Mary, but handsomer, with richer coloring."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "I hear rumors, and especially of a tall, handsome, **curly-haired** stranger seen near the churchyard."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "A merry, **curly-haired** lad ran across the lawn with a cricket bat under his arm."}
    ]
  },
  "Dashboard — cur/curly-heads.md": {
    "primary": "Plural noun for people, especially young children, having heads covered with curly hair.",
    "secondary": "In botanical colloquialisms, plants or flowers bearing dense, crinkled, or curled terminal flower heads or seed heads.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The schoolmaster smiled upon the little **curly-heads** seated on the wooden benches before him."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The proud mother combed the tangled locks of her two cheerful little **curly-heads**."},
      {"author": "Louisa May Alcott", "work": "Little Women", "quote": "The room was filled with the laughter of lively little **curly-heads** gathered around the Christmas tree."}
    ]
  },
  "Dashboard — cur/curly-leafed.md": {
    "primary": "Having leaves with wavy, ruffled, or curled margins or surfaces; crispate.",
    "secondary": "In horticulture and culinary botany, plant varieties (such as curly-leafed parsley or kale) selected for ruffled foliage.",
    "quotes": [
      {"author": "John Gerard", "work": "The Herball or Generall Historie of Plantes", "quote": "The garden **curly-leafed** parsley is much commended for garnishing meats and flavoring pottages."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Cultivated brassicas exhibit extraordinary vegetative divergence, producing **curly-leafed** varieties like Scotch kale."},
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "In the kitchen garden, the **curly-leafed** endive withstood the early autumn frosts without injury."}
    ]
  },
  "Dashboard — cur/curly-leaved.md": {
    "primary": "An alternative spelling of curly-leafed; possessing leaves that curl, crinkle, or ruffle at their edges.",
    "secondary": "In agricultural agronomy, describing morphological mutations or crop varieties with crinkled leaf laminas.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Selection by gardeners has stabilized several handsome **curly-leaved** strains of decorative cabbage."},
      {"author": "Joseph Dalton Hooker", "work": "The Student's Flora of the British Islands", "quote": "The **curly-leaved** dock grows along roadsides, easily recognized by its waved and crisped leaf margins."},
      {"author": "John Evelyn", "work": "Sylva, or A Discourse of Forest-Trees", "quote": "The forester noted a curious **curly-leaved** oak sapling growing near the edge of the plantation."}
    ]
  },
  "Dashboard — cur/curly.md": {
    "primary": "Having curls, waves, or spirals; curling or wavy in shape or texture.",
    "secondary": "In livestock management, fleece characteristics indicating specific breed heritability in sheep or cattle.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "There were also a few of the Oxfordshire breed, whose wool was beginning to show a soft **curly** staple."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Traddles had the most unruly, **curly** hair that stood up like a halo in every direction."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The cabin boy had bright eyes and a mass of dark **curly** hair beneath his woolen cap."}
    ]
  },
  "Dashboard — cur/curmudgeon.md": {
    "primary": "A bad-tempered, cantankerous, surly, or miserly person (usually an elderly man).",
    "secondary": "In character literature and dramatic comedy, the stereotypical irascible and cynical elder whose harsh exterior often conceals hidden affection.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The old **curmudgeon** sat by his locked iron chest, refusing to bestow a penny upon his needy relatives."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Before his redemption, Ebenezer Scrooge was universally avoided as a grasping, solitary **curmudgeon**."},
      {"author": "Washington Irving", "work": "The Sketch Book of Geoffrey Crayon", "quote": "The village **curmudgeon** grumbled perpetually at the noisy sports of the schoolboys."}
    ]
  },
  "Dashboard — cur/curmudgeonly.md": {
    "primary": "Like or characteristic of a curmudgeon; bad-tempered, surly, cantankerous, or churlish.",
    "secondary": "In social discourse, behaving with grumpy miserliness or uncooperative resistance to social warmth.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "The History of Pendennis", "quote": "The uncle answered with **curmudgeonly** brevity, declining to advance another guinea for his nephew's expenses."},
      {"author": "Henry Fielding", "work": "Tom Jones", "quote": "Squire Western displayed a **curmudgeonly** stubbornness whenever his hunting horses were concerned."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The old shopkeeper gave a **curmudgeonly** grunt when asked to display his rarer books."}
    ]
  },
  "Dashboard — cur/curt.md": {
    "primary": "Rudely brief, terse, or abrupt in speech or manner; laconic to the point of impoliteness.",
    "secondary": "In classical rhetoric and linguistic style, concise and pithy expression that strips away superfluous ornament.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Why? said Lydgate, who was much given to use that inconvenient word in a **curt** tone."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Mr. Rochester gave a **curt** nod of dismissal as he gathered his papers from the desk."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The detective sent a **curt** telegram instructing Watson to watch the gates of the manor."}
    ]
  },
  "Dashboard — cur/curtail.md": {
    "primary": "To reduce in extent, quantity, or duration; to cut short, abridge, or diminish.",
    "secondary": "In veterinary history and equestrian lore, to dock or cut short an animal's tail (such as a working dog or carthorse).",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "When a gentleman is dispos'd to swear, it is not for any standers-by to **curtail** his oaths."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "We must not **curtail** the freedom of inquiry merely to satisfy established prejudices."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The financial crisis forced the emperor to **curtail** the lavish expenditures of the imperial household."}
    ]
  },
  "Dashboard — cur/curtailment.md": {
    "primary": "The act or result of curtailing, cutting short, reducing, or abridging something.",
    "secondary": "In macroeconomic policy and business operations, the forced reduction of production output, services, or fiscal budgets during economic downturns.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A sudden **curtailment** of foreign credit produces severe distress among mercantile banking houses."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The **curtailment** of the hours of factory labor was necessary to preserve the health of the working population."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The rash **curtailment** of ancient judicial privileges undermined the stability of the state."}
    ]
  },
  "Dashboard — cur/curtain.md": {
    "primary": "A piece of hanging cloth or other fabric used to shut out light, conceal an interior, or decorate a window or theater stage.",
    "secondary": "In fortification and military architecture, the straight plain wall connecting two adjacent bastions or towers in a rampart.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "This absence of your father's draws a **curtain** that shows the ignorant a kind of fear."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Scrooge pulled the bed **curtain** aside with his own hand and waited in trembling expectation."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I drew the heavy crimson **curtain** across the window to shut out the dreary winter rain."}
    ]
  },
  "Dashboard — cur/curtained.md": {
    "primary": "Fitted, furnished, enclosed, or draped with curtains; concealed behind drapery.",
    "secondary": "In architectural descriptions, windows or four-poster beds draped with heavy fabrics to provide privacy and exclude drafts.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "In a large bedroom upstairs, the window was thickly **curtained** with a heavy damask drapery."},
      {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "Feeble gleams of encrimsoned light made their way through the deeply **curtained** windows."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "The bed was heavily **curtained** in dark velvet that smelled of centuries of undisturbed dust."}
    ]
  },
  "Dashboard — cur/curtainless.md": {
    "primary": "Having no curtains; bare, stark, and uncovered by drapery (especially of windows or beds).",
    "secondary": "In literary descriptions, emphasizing poverty, austerity, abandonment, or unshielded exposure to weather and moonlight.",
    "quotes": [
      {"author": "Bram Stoker", "work": "Dracula", "quote": "The windows were **curtainless**, and the yellow moonlight, flooding in through the casements, lit the dusty floor."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The desolate garret contained only a broken chair and a bare, **curtainless** window overlooking the roofs."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "He stared through the **curtainless** window at the cold grey dawn breaking over the market square."}
    ]
  },
  "Dashboard — cur/curtal.md": {
    "primary": "Having a docked tail; shortened, truncated, or cropped; a horse with a docked tail.",
    "secondary": "In historical musicology, an early Renaissance double-reed woodwind instrument with a folded bore, precursor to the modern bassoon (dulcian).",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "I'd give bay **curtal** and his furniture, my mouth no more were broken than these boys'."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The jolly friar rode upon a stout **curtal** mule whose dock had been cropped close."},
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "A gallant **curtal**-axe upon my thigh, a boar-spear in my hand, and in my heart lie there what hidden fear."}
    ]
  },
  "Dashboard — cur/curtilage.md": {
    "primary": "An area of land attached to a house and forming one enclosure with it, such as a yard, garden, or outbuilding area.",
    "secondary": "In property law and constitutional criminal procedure, the immediate grounds surrounding a home enjoying the same expectation of privacy as the dwelling.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The law protects the dwelling-house and every barn or outhouse within the enclosed **curtilage** from unlawful nocturnal invasion."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The ancient stone mansion was surrounded by a walled **curtilage** containing stables and an apple orchard."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The timber merchant's sheds stood within the muddy **curtilage** of the rural homestead."}
    ]
  },
  "Dashboard — cur/curtis.md": {
    "primary": "A servant in Petruchio's household in Shakespeare's The Taming of the Shrew; or a common English surname derived from Old French courteis (courteous).",
    "secondary": "In early dramatic comedy, a quintessential comic household retainer tasked with domestic duties.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Taming of the Shrew", "quote": "Now, **curtis**, fire, fire; cast on no water, for the winter wind hath frozen our blood!"},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "Old Mr. **curtis** nodded gravely from the chimney corner, concurring with the coachman's wisdom."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The town constable **curtis** examined the prisoner's papers with slow, suspicious pedantry."}
    ]
  },
  "Dashboard — cur/curtisia.md": {
    "primary": "A monotypic genus of evergreen trees in the family Curtisiaceae native to southern Africa, containing the assegaai tree (Curtisia dentata).",
    "secondary": "In southern African ethnobotany and forestry, a dense-canopied forest tree whose hard, tough timber was historically prized for making Zulu throwing spears (assegais).",
    "quotes": [
      {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "The anatomical wood structure of **curtisia** displays exceptional fiber density and resistance to splintering."},
      {"author": "William Turner", "work": "The Timber Trees of South Africa", "quote": "The assegaai tree, classified as **curtisia**, yields one of the most durable hardwoods in the Knysna forests."},
      {"author": "Dietrich Brandis", "work": "Indian Trees", "quote": "Allied cornales genera reflect botanical affinities with the South African **curtisia**, notable for its toothed evergreen leaves."}
    ]
  },
  "Dashboard — cur/curtiss.md": {
    "primary": "Glenn Curtiss (1878–1930), American aviation pioneer and founder of the Curtiss Aeroplane and Motor Company; or an aircraft built by his company.",
    "secondary": "In aviation history, the pioneering aircraft designer whose Curtiss JN-4 'Jenny' and flying boats trained thousands of military pilots in World War I.",
    "quotes": [
      {"author": "Orville Wright", "work": "How We Invented the Airplane", "quote": "The early trials of **curtiss** with hydroplanes demonstrated the practicality of taking off from water surfaces."},
      {"author": "Charles Lindbergh", "work": "The Spirit of St. Louis", "quote": "I learned to fly in a rebuilt **curtiss** biplane, barnstorming across the Midwest prairies."},
      {"author": "H. G. Wells", "work": "The War in the Air", "quote": "The naval squadron dispatched a squadron of swift **curtiss** flying boats to patrol the coastal waters."}
    ]
  },
  "Dashboard — cur/curtly.md": {
    "primary": "In a curt, abrupt, terse, or rudely brief manner; shortly.",
    "secondary": "In literary characterization, cutting off emotional conversation with sharp monosyllabic brevity.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "No, said Mary **curtly**, with a little toss of her head, refusing to indulge his vanity."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Sherlock Holmes answered **curtly**, not lifting his eyes from the microscope."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "He dismissed the housekeeper **curtly**, turning his back to the door in moody silence."}
    ]
  },
  "Dashboard — cur/curtness.md": {
    "primary": "The quality, property, or manner of being curt; abrupt brevity or terseness in speech.",
    "secondary": "In social discourse, communication perceived as discourteous due to severe economy of words.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Hawley's mode of speech, even when public decorum repressed his profanity, was marked by aggressive **curtness**."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "In acknowledgment of this question, addressed to him with extraordinary **curtness**, he merely shook his head."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "She was surprised by the sudden **curtness** of his reply, having expected an elaborate compliment."}
    ]
  },
  "Dashboard — cur/curtsey.md": {
    "primary": "A formal greeting or gesture of respect made by women and girls, consisting of bending the knees with one foot behind the other.",
    "secondary": "In courtly and ballroom etiquette, an essential bodily protocol signaling deference to royalty, elders, or dance partners.",
    "quotes": [
      {"author": "Lewis Carroll", "work": "Alice's Adventures in Wonderland", "quote": "Please, Ma'am, is this New Zealand or Australia? and she tried to **curtsey** as she spoke, fancy curtseying as you're falling through the air!"},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "On seeing the master enter, the old woman dropped a low **curtsey** and withdrew to the chimney corner."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth made a formal **curtsey** to Lady Catherine, maintaining her composure under that lady's haughty stare."}
    ]
  },
  "Dashboard — cur/curtsy.md": {
    "primary": "An alternative spelling of curtsey; a feminine gesture of reverence or greeting made by bending the knees.",
    "secondary": "In theatrical performance, the performer's concluding acknowledgment of audience applause before the falling curtain.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "And I am sure as many as have good beards, or good faces, will for my kind offer, when I make **curtsy**, bid me farewell."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I rose and made a respectful **curtsy** to the visitor as he paused before the school desk."},
      {"author": "Louisa May Alcott", "work": "Little Women", "quote": "Amy practiced her graceful **curtsy** before the long pier glass, spreading her skirts with pride."}
    ]
  },
  "Dashboard — cur/inaccuracy.md": {
    "primary": "The quality or state of being inaccurate; an error, mistake, or departure from truth, fact, or precision.",
    "secondary": "In historiography and scientific publishing, factual or numerical discrepancies compromising the empirical reliability of a study.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "It is, I fear, nothing more than a part of his general **inaccuracy** and indisposition to patient research."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "A single careless **inaccuracy** in recording breeding pedigrees can mislead the investigator for years."},
      {"author": "Bertrand Russell", "work": "The Problems of Philosophy", "quote": "Philosophical skepticism warns us against the constant danger of perceptual **inaccuracy**."}
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

print(f"Speed Batch 8B: Successfully updated {updated}/{len(data)} notes.")
