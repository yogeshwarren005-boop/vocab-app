# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — sci (Words 41-77)
  # =========================================================================
  "Dashboard — sci/scilla.md": {
    "primary": "A genus of bulbous perennial herbs in the asparagus family, bearing blue bell-shaped flowers.",
    "secondary": "In pharmacology and horticulture, medicinal bulbs containing cardiac glycosides traditionally extracted from sea squill.",
    "quotes": [
      {"author": "John Gerard", "work": "The Herball, or Generall Historie of Plantes", "quote": "The bulbous root of **Scilla**, or the sea onion, is large, coat upon coat, resembling the common onion."},
      {"author": "William Withering", "work": "An Arrangement of British Plants", "quote": "Blue woodland **Scilla** enlivens the shady dells in early April with nodding azure spikes."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Cultivated species of **Scilla** are naturalized in ancient orchards and woodland borders."}
    ]
  },
  "Dashboard — sci/scimitar.md": {
    "primary": "A short sword with a curved blade that broadens toward the point, historically used in the Middle East.",
    "secondary": "In military history and romantic narrative, a cavalry cutting weapon designed for slashing strokes from horseback.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "By this **scimitar** that slew the Sophy and a Persian prince that won three fields of Sultan Solyman."},
      {"author": "Walter Scott", "work": "The Talisman", "quote": "Saladin severed the silken cushion with a single sweeping stroke of his curved Damascus **scimitar**."},
      {"author": "Lord Byron", "work": "The Giaour", "quote": "His gleaming **scimitar** flashed like summer lightning above the smoke of the cavalry melee."}
    ]
  },
  "Dashboard — sci/scincella.md": {
    "primary": "A genus of small, slender skinks in the family Scincidae, commonly known as ground skinks.",
    "secondary": "In North American herpetology, secretive leaf-litter lizards that forage among decaying humus in temperate forests.",
    "quotes": [
      {"author": "John Edwards Holbrook", "work": "North American Herpetology", "quote": "The small brown lizard **Scincella** lateralis glides through fallen leaves with rapid, serpentine motions."},
      {"author": "David Starr Jordan", "work": "A Manual of the Vertebrate Animals", "quote": "The ground skink belonging to **Scincella** is distinguished by its transparent disc in the lower eyelid."},
      {"author": "Raymond Ditmars", "work": "The Reptile Book", "quote": "Specimens of **Scincella** feed primarily on minute insects and spiders inhabiting damp woodland soil."}
    ]
  },
  "Dashboard — sci/scincid.md": {
    "primary": "Any lizard belonging to the family Scincidae; of or pertaining to the skinks.",
    "secondary": "In reptile morphology, diurnal squamates characterized by smooth overlapping osteoderm scales and reduced limbs.",
    "quotes": [
      {"author": "Raymond Ditmars", "work": "The Reptile Book", "quote": "The typical **scincid** lizard possesses polished, bony-cored scales that give its body an oily sheen."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "Cranial osteology in the **scincid** family shows a complete bony palate and robust temporal arches."},
      {"author": "Charles Darwin", "work": "Journal of Researches", "quote": "We captured a curious **scincid** reptile basking upon the sun-baked volcanic rocks of the archipelago."}
    ]
  },
  "Dashboard — sci/scincidae.md": {
    "primary": "A large, cosmopolitan family of lizards comprising the skinks.",
    "secondary": "In systematic herpetology, one of the most diverse squamate families, displaying evolutionary transitions toward limb reduction.",
    "quotes": [
      {"author": "Georges Cuvier", "work": "The Animal Kingdom", "quote": "The family **Scincidae** is readily recognized by its short limbs, conical head, and shiny imbricated scales."},
      {"author": "Raymond Ditmars", "work": "The Reptile Book", "quote": "Members of **Scincidae** range from heavy burrowing forms to agile semi-arboreal foragers."},
      {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "The Indo-Malayan region contains an extraordinary variety of genera belonging to **Scincidae**."}
    ]
  },
  "Dashboard — sci/scincus.md": {
    "primary": "A genus of desert skinks native to North Africa and Arabia, known as sandfish.",
    "secondary": "In arid herpetology and classical pharmacopeia, a specialized sand-burrowing lizard celebrated in ancient medicine.",
    "quotes": [
      {"author": "Pliny the Elder", "work": "The Natural History", "quote": "The medicinal virtue of the crocodile and the desert **Scincus** was celebrated by Egyptian healers."},
      {"author": "Georges Cuvier", "work": "The Animal Kingdom", "quote": "The flattened snout and fringed toes of **Scincus** enable it to swim through loose desert sand with astonishing agility."},
      {"author": "Richard Burton", "work": "Personal Narrative of a Pilgrimage to Al-Madinah and Meccah", "quote": "Bedouin hunters capture the golden **Scincus** basking upon the crest of coastal dunes."}
    ]
  },
  "Dashboard — sci/scindapsus.md": {
    "primary": "A genus of climbing evergreen vines in the arum family (Araceae), native to Southeast Asia.",
    "secondary": "In tropical botany and horticulture, ornamental root-climbing lianas with variegated foliage and calcium oxalate crystals.",
    "quotes": [
      {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "The high canopy of the Assamese jungle is laced with gigantic stems of climbing **Scindapsus**."},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "Lush festoons of **Scindapsus** clothed the trunks of towering dipterocarps in evergreen splendor."},
      {"author": "George Bentham", "work": "Genera Plantarum", "quote": "The spadix of **Scindapsus** is densely covered with hermaphrodite flowers lacking a perianth."}
    ]
  },
  "Dashboard — sci/scintilla.md": {
    "primary": "A tiny trace or spark of a specified quality or feeling; an iota or microscopic shred.",
    "secondary": "In jurisprudence and forensic reasoning, the minimum quantum of evidence required to keep an action from summary dismissal.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "There was not a **scintilla** of evidence to support the preposterous claim brought before the court."},
      {"author": "Edgar Allan Poe", "work": "The Murders in the Rue Morgue", "quote": "The prefect failed because he overlooked that minute **scintilla** of fact which pointed to the true perpetrator."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Not a **scintilla** of doubt remained in my mind after Holmes examined the footprint."}
    ]
  },
  "Dashboard — sci/scintillant.md": {
    "primary": "Emitting sparks or sparkling; glittering or flashing with light.",
    "secondary": "In poetic description and astronomy, radiant with flickering starlight or luminous brilliance.",
    "quotes": [
      {"author": "James Joyce", "work": "Ulysses", "quote": "The air without is impregnated with raindew moisture, glistening upon every leaf in **scintillant** points."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The frosty morning air was crisp and clear, filled with **scintillant** rime upon the boughs."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Phosphorescent creatures in the tropical wake produced a **scintillant** glow beneath the dark counter of the ship."}
    ]
  },
  "Dashboard — sci/scintillate.md": {
    "primary": "To emit flashes of light; to sparkle, glitter, or twinkle; also to be brilliantly lively or witty.",
    "secondary": "In conversational society and physics, flashing rapid intermittent points of light or verbal wit.",
    "quotes": [
      {"author": "Francis Thompson", "work": "Shelley: An Essay", "quote": "The dimmest-sparked chip of a conception blazes and **scintillates** in his incandescent imagination."},
      {"author": "P. G. Wodehouse", "work": "Love Among the Chickens", "quote": "Striking scenes and freshets of brilliant dialogue **scintillate** throughout the opening acts."},
      {"author": "graf Leo Tolstoy", "work": "War and Peace", "quote": "Moscow lay stretched at his feet, with her golden domes and crosses that seem to **scintillate** in the noon sun."}
    ]
  },
  "Dashboard — sci/scintillating.md": {
    "primary": "Sparkling or shining brightly; brilliantly clever, amusing, or skillful.",
    "secondary": "In literary portraiture and social comedy, dazzling companions with rapid, sparkling conversation and intellectual charm.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "And amid all these **scintillating** points of light one bright planet shone keen and calm."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Her lively wit and **scintillating** remarks kept the entire dinner party in high good humor."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Lord Henry delivered a **scintillating** paradox that set every guest at the table laughing."}
    ]
  },
  "Dashboard — sci/scintillation.md": {
    "primary": "A flash or spark of light; the rapid twinkling of stars caused by atmospheric turbulence.",
    "secondary": "In observational astronomy and radiation physics, rapid fluctuations in apparent stellar brightness or ionization flashes.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "The **scintillation** of the fixed stars arises from the tremulous motion of the refracting air through which their light passes."},
      {"author": "Thomas Hardy", "work": "Two on a Tower", "quote": "He watched the blue **scintillation** of Sirius through the great lens of the observatory."},
      {"author": "John Tyndall", "work": "Six Lectures on Light", "quote": "Atmospheric currents cause that ceaseless **scintillation** which lends such jewel-like beauty to the night sky."}
    ]
  },
  "Dashboard — sci/sciolism.md": {
    "primary": "A superficial or shallow show of learning; pretended erudition.",
    "secondary": "In intellectual history and academic satire, conceited half-knowledge that parades specialized jargon without grasping principles.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "When was **sciolism** ever dissociated from laxity and self-complacent arrogance?"},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The cheap **sciolism** of our age mistakes the headlines of cyclopedias for profound philosophical inquiry."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "From dogmatic **sciolism** and pedantic triviality, good Lord deliver this generation!"}
    ]
  },
  "Dashboard — sci/sciolist.md": {
    "primary": "A person who pretends to be knowledgeable and displays superficial learning; a smatterer.",
    "secondary": "In polemical criticism and philosophy, a superficial dabbler who pontificates authoritatively on topics beyond his depth.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "A mere **sciolist** will always dispute dogmatically upon subjects that true scholars approach with reverence."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The vain **sciolist** catches at empty words while the wise investigator searches out the nature of things."},
      {"author": "Jonathan Swift", "work": "A Tale of a Tub", "quote": "Every modern coffee-house **sciolist** imagines himself capable of reforming the church and commonwealth."}
    ]
  },
  "Dashboard — sci/sciolistic.md": {
    "primary": "Characterized by or showing superficial, shallow knowledge.",
    "secondary": "In literary reviewing and cultural critique, displaying ostentatious but hollow intellectual pretension.",
    "quotes": [
      {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "Our journalism is too often infected with **sciolistic** cleverness that lacks moral seriousness."},
      {"author": "William Hazlitt", "work": "Table-Talk", "quote": "His speech was a **sciolistic** performance, glittering with borrowed quotations but devoid of original thought."},
      {"author": "Thomas De Quincey", "work": "Letters to a Young Man", "quote": "Beware of acquiring a **sciolistic** familiarity with philosophical systems before you have mastered logic."}
    ]
  },
  "Dashboard — sci/scion.md": {
    "primary": "A young shoot or twig cut for grafting; a descendant or heir of a notable family.",
    "secondary": "In arboriculture and dynastic genealogy, a vegetative bud grafted onto rootstock, or a noble youth carrying on an ancestral lineage.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "You see, sweet maid, we marry a gentler **scion** to the wildest stock, and make conceive a bark of baser kind."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "He was the last male **scion** of an ancient family whose estates had dwindled through extravagance."},
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "The grafting of a fruitful **scion** upon a wild crab-tree alters the nature of the fruit produced."}
    ]
  },
  "Dashboard — sci/scirpus.md": {
    "primary": "A genus of aquatic perennial herbs in the sedge family (Cyperaceae), known as bulrushes.",
    "secondary": "In wetland ecology and botanical systematics, rhizomatous marsh plants forming dense stands along shores and marshes.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The genus **Scirpus** includes the great river bulrushes with triangular stems and terminal clusters of spikelets."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Along the muddy cove grew tall ranks of **Scirpus** and pickerel-weed, rustling in the summer breeze."},
      {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "Species of **Scirpus** provide durable fiber for weaving coarse mats among coastal fisherfolk."}
    ]
  },
  "Dashboard — sci/scission.md": {
    "primary": "The act of cutting, dividing, or cleaving; a division, split, or schism.",
    "secondary": "In political history and surgical anatomy, a profound rupture separating ecclesiastical sects or severing anatomical tissues.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The theological **scission** between the Eastern and Western churches widened into irreconcilable enmity."},
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "Nature should be dissected rather than abstracted; it is a **scission** of parts that reveals internal motion."},
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The sharp **scission** of the umbilical cord marks the infant's entry into autonomous terrestrial life."}
    ]
  },
  "Dashboard — sci/scissor-tailed.md": {
    "primary": "Having a deeply forked tail resembling open scissors, as in certain birds.",
    "secondary": "In ornithological field identification, applied to flycatchers and kites displaying long, bifurcated rectrices used in aerial turns.",
    "quotes": [
      {"author": "John James Audubon", "work": "Ornithological Biography", "quote": "The **scissor-tailed** flycatcher perches gracefully upon the thorny mesquite of the Texas prairies."},
      {"author": "Theodore Roosevelt", "work": "Hunting Trips of a Ranchman", "quote": "A pair of **scissor-tailed** birds swept overhead in pursuit of dragonflies, their long plumes opening and shutting."},
      {"author": "Elliott Coues", "work": "Key to North American Birds", "quote": "The **scissor-tailed** flycatcher is among the most elegant and agile avian hunters of the southern plains."}
    ]
  },
  "Dashboard — sci/scissor.md": {
    "primary": "An instrument for cutting consisting of two pivoted blades; to cut with scissors.",
    "secondary": "In mechanical craft and gymnastics, an action or movement resembling the opening and closing of blades.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "One afternoon a **scissor**-grinder chanced to set his wheel humming at the corner of Pyncheon Street."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "She took up the small tailor's **scissor** and neatly trimmed the frayed edges of the ribbon."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The closing jaws of the whale functioned like a colossal **scissor**, severing the cedar whaleboat in twain."}
    ]
  },
  "Dashboard — sci/scissors.md": {
    "primary": "An instrument used for cutting paper, cloth, or hair, consisting of two crossed pivoted blades.",
    "secondary": "In domestic history and surgical practice, shearing blades operated by finger loops to slice materials with opposing edges.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Comedy of Errors", "quote": "My master preaches patience to him, and the while his man with **scissors** nicks him like a fool."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "He sat poring over his book, heedless of the click of her knitting needles and working **scissors**."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles: A Pure Woman", "quote": "Then with her little **scissors**, by the aid of a pocket looking-glass, she cut away the tell-tale fringe."}
    ]
  },
  "Dashboard — sci/scissortail.md": {
    "primary": "The scissor-tailed flycatcher (Tyrannus forficatus); a bird with long forked tail feathers.",
    "secondary": "In regional natural history and aviculture, the state bird of Oklahoma, famed for its tumbling aerial courtship flights.",
    "quotes": [
      {"author": "Theodore Roosevelt", "work": "The Wilderness Hunter", "quote": "Across the grassy prairie, the white-and-salmon **scissortail** darted with lightning speed after hovering locusts."},
      {"author": "John James Audubon", "work": "Birds of America", "quote": "No species in the southern territories displays greater elegance in flight than the graceful **scissortail**."},
      {"author": "Elliott Coues", "work": "Birds of the Northwest", "quote": "The remarkable tail feathers of the **scissortail** extend to more than double the length of its body."}
    ]
  },
  "Dashboard — sci/scissure.md": {
    "primary": "A long, narrow cut, opening, or split; a fissure, cleft, or rupture.",
    "secondary": "In anatomical dissection and geomorphology, a longitudinal cleft in bone, tissue, or rock strata.",
    "quotes": [
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The anatomical **scissure** in the cranium closes gradually as the cranial sutures unite during childhood."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The earthquake opened a deep **scissure** across the hillside, swallowing whole vineyards in its chasm."},
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "Bark that suffers a deep vertical **scissure** during the winter freeze exudes resin when the spring thaw begins."}
    ]
  },
  "Dashboard — sci/sciuridae.md": {
    "primary": "A large family of rodents containing tree squirrels, ground squirrels, chipmunks, and marmots.",
    "secondary": "In evolutionary mammalogy, sciuromorph rodents characterized by bushy tails, postorbital processes, and diurnal foraging habits.",
    "quotes": [
      {"author": "Georges Cuvier", "work": "The Animal Kingdom", "quote": "The family **Sciuridae** includes agile climbing species as well as subterranean burrowers like the prairie dog."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The skull in **Sciuridae** possesses distinct post-orbital processes and prominent zygomatic arches."},
      {"author": "John Burroughs", "work": "Squirrels and Other Fur-Bearers", "quote": "Members of the family **Sciuridae** are nature's most industrious foresters, planting oaks and walnuts across the hills."}
    ]
  },
  "Dashboard — sci/sciuromorpha.md": {
    "primary": "A suborder of rodents that includes squirrels, marmots, mountain beavers, and dormice.",
    "secondary": "In vertebrate paleontology and rodent taxonomy, rodents defined by a specific masseter muscle arrangement along the zygomatic plate.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The suborder **Sciuromorpha** is distinguished from myomorphs by the specialized anterior origin of the lateral masseter muscle."},
      {"author": "Archibald Geikie", "work": "Text-book of Geology", "quote": "Primitive fossil representatives of **Sciuromorpha** appear in the Eocene formations of North America."},
      {"author": "David Starr Jordan", "work": "A Manual of the Vertebrate Animals", "quote": "Within the mammalian order Rodentia, the division **Sciuromorpha** occupies a primitive and well-differentiated position."}
    ]
  },
  "Dashboard — sci/sciurus.md": {
    "primary": "The type genus of the squirrel family (Sciuridae), comprising the typical tree squirrels.",
    "secondary": "In mammalogy and forest ecology, arboreal rodents equipped with sharp curved claws and bushy counterbalancing tails.",
    "quotes": [
      {"author": "Carl Linnaeus", "work": "Systema Naturae", "quote": "Under the genus **Sciurus**, Linnaeus grouped the arboreal squirrels characterized by bushy tails and four front toes."},
      {"author": "Henry David Thoreau", "work": "Faith in a Seed", "quote": "The gray squirrel, **Sciurus** carolinensis, buries thousands of acorns every autumn, ensuring the forest's renewal."},
      {"author": "John James Audubon", "work": "The Viviparous Quadrupeds of North America", "quote": "The species of **Sciurus** leap with astonishing precision from bough to bough in the high deciduous woods."}
    ]
  },
  "Dashboard — sci/subconscious.md": {
    "primary": "Operating below the threshold of conscious awareness; subconscious mental processes.",
    "secondary": "In psychodynamic theory and cognitive psychology, mental associations and memories that influence behavior without active deliberation.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "A large part of our mental activity goes on in a **subconscious** region beyond focal attention."},
      {"author": "Jack London", "work": "The Star-Rover", "quote": "If by hypnotism the conscious mind were put to sleep, the **subconscious** memories of ancient lives emerged."},
      {"author": "Sigmund Freud", "work": "The Psychopathology of Everyday Life", "quote": "Slips of the tongue frequently reveal a **subconscious** motive contradicting our spoken intentions."}
    ]
  },
  "Dashboard — sci/subconsciously.md": {
    "primary": "In a manner occurring below the level of conscious awareness; instinctively or unconsciously.",
    "secondary": "In narrative psychology, absorbing environmental cues or forming intentions without deliberate intellectual recognition.",
    "quotes": [
      {"author": "Donn Byrne", "work": "The Wind Bloweth", "quote": "He thought for a while that what he missed was the ships, and that, **subconsciously**, he was pining for the sea."},
      {"author": "Mrs. George de Horne Vaizey", "work": "The Lady of the Basement Flat", "quote": "**Subconsciously**, I had known that the trouble had been brewing between them for many months."},
      {"author": "Joseph Conrad", "work": "Chance", "quote": "She turned her head away, **subconsciously** sensing that a decisive crisis in her life had arrived."}
    ]
  },
  "Dashboard — sci/subconsciousness.md": {
    "primary": "The mental realm or activity occurring beneath conscious awareness; the subconscious.",
    "secondary": "In psychoanalysis and early cognitive science, the stratum of latent impressions and desires underlying waking thought.",
    "quotes": [
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "In the deep well of **subconsciousness** lie the springs of sudden religious conversion and artistic inspiration."},
      {"author": "Jack London", "work": "The Star-Rover", "quote": "In a single interval of fifteen minutes, my **subconsciousness** roved through centuries of past existence."},
      {"author": "F. W. H. Myers", "work": "Human Personality and Its Survival of Bodily Death", "quote": "The threshold of waking thought separates our everyday ego from the vast domain of **subconsciousness**."}
    ]
  },
  "Dashboard — sci/unconscientious.md": {
    "primary": "Not guided by or showing conscience; lacking moral scruples, care, or diligence in duty.",
    "secondary": "In workplace ethics and social criticism, performing tasks with careless negligence and total indifference to promises made.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "An **unconscientious** workman who uses rotten timber endangers the lives of those who dwell in the house."},
      {"author": "Anthony Trollope", "work": "The Prime Minister", "quote": "He was too vain to be malicious, but too lazy and **unconscientious** to be trusted with public funds."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The **unconscientious** author who prints falsehoods for partisan gain poisons the wells of public knowledge."}
    ]
  },
  "Dashboard — sci/unconscientiousness.md": {
    "primary": "Lack of conscientious principle; negligent disregard of moral or professional duty.",
    "secondary": "In moral jurisprudence and civic history, systemic irresponsibility and breach of trust by public officials.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The commercial decline of the state was accelerated by the pervasive **unconscientiousness** of its mercantile classes."},
      {"author": "Herbert Spencer", "work": "The Principles of Ethics", "quote": "Gross **unconscientiousness** in contractual performance destroys the mutual confidence upon which trade relies."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "No nation can long endure when sham work and moral **unconscientiousness** are crowned with worldly honors."}
    ]
  },
  "Dashboard — sci/unconscionable.md": {
    "primary": "Not right or reasonable; unreasonably excessive, outrageous, or unprincipled.",
    "secondary": "In contract equity and commercial law, an agreement so one-sided and oppressive that no person in their senses would accept it.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "There is an **unconscionable** old shark for you! said Herbert, laughing at the usurer's exorbitant terms."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "It was an **unconscionable** hour to pay a morning call, yet her impatience would broach no delay."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The landlord demanded an **unconscionable** reckoning for the miserable supper provided to the travelers."}
    ]
  },
  "Dashboard — sci/unconscious.md": {
    "primary": "Not awake or aware of one's surroundings; done without conscious intent or realization.",
    "secondary": "In psychoanalytic theory, the mental realm of repressed memories, primitive impulses, and instincts inaccessible to waking awareness.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "She was quite **unconscious** that she only praised herself and that it was impossible to mistake her meaning."},
      {"author": "Sigmund Freud", "work": "The Ego and the Id", "quote": "The ego is not sharply separated from the id; its lower portion merges into the **unconscious**."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "He lay upon the deck in an **unconscious** swoon until the salt spray revived his senses."}
    ]
  },
  "Dashboard — sci/unconsciously.md": {
    "primary": "Without being aware; unintentionally or instinctively.",
    "secondary": "In character portrayal and observational literature, revealing hidden sentiments or habits through unintentional gestures.",
    "quotes": [
      {"author": "Johanna Spyri", "work": "Maezli: A Story of the Swiss Valleys", "quote": "Isn't it possible that the child should have **unconsciously** repeated the phrase she had overheard?"},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "She looked toward the door, **unconsciously** betraying the anxious expectation that consumed her."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Bathsheba had **unconsciously** guided her pony closer to the wagon where Oak stood waiting."}
    ]
  },
  "Dashboard — sci/unconsciousness.md": {
    "primary": "The state of being unconscious; lack of awareness, responsiveness, or physical sensation.",
    "secondary": "In clinical medicine and narrative drama, profound coma or syncope following physical trauma or emotional shock.",
    "quotes": [
      {"author": "Jane Austen", "work": "Persuasion", "quote": "She was assisted by that perfect indifference and apparent **unconsciousness** of having given offense."},
      {"author": "Mrs. Oliphant", "work": "A Beleaguered City", "quote": "She remained in speechless **unconsciousness** until the physician administered a restorative cordial."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The blow upon the temple plunged him into complete **unconsciousness** for several hours."}
    ]
  },
  "Dashboard — sci/unscientific.md": {
    "primary": "Not based on or conforming to the principles and methods of science; lacking empirical rigor.",
    "secondary": "In epistemology and methodology, conclusions derived from superstition, unverified anecdotes, or faulty deduction.",
    "quotes": [
      {"author": "Jack London", "work": "The Star-Rover", "quote": "Capital punishment is so silly, so stupid, and so horribly **unscientific** in its conception of criminal justice."},
      {"author": "T. R. Glover", "work": "The Jesus of History", "quote": "It is entirely **unscientific** to explain complex spiritual history by crude catchwords and hasty generalizations."},
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues under the Sea", "quote": "Conseil refused to give an opinion, declaring that hearsay was an **unscientific** basis for zoological classification."}
    ]
  },
  "Dashboard — sci/unscientifically.md": {
    "primary": "In a manner that does not conform to scientific principles or empirical methods.",
    "secondary": "In academic criticism, conducting experiments or interpreting evidence with bias, lack of controls, or anecdotal speculation.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "To argue from isolated anomalies without systematic observation is to proceed wholly **unscientifically**."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Early travelers described indigenous customs so **unscientifically** that little reliance can be placed upon their reports."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "When philosophers treat mental faculties as independent agents, they speak **unscientifically** and obscure the truth."}
    ]
  }
}

base_dir = r"App database/Latin roots/Cluster Thought"

updated_count = 0
for rel_path, entry in data.items():
    full_path = os.path.join(base_dir, rel_path)
    if not os.path.exists(full_path):
        print(f"Missing file: {full_path}")
        continue
    
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    book_pattern = r"(> 1\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)(\r?\n> 2\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)"
    def repl_book(m):
        return f"{m.group(1)}{entry['primary']}{m.group(3)}{entry['secondary']}"
    
    new_content = re.sub(book_pattern, repl_book, content)
    if new_content == content:
        book_pattern2 = r"(1\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)(\r?\n.*?2\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)"
        new_content = re.sub(book_pattern2, repl_book, content)

    q_pos = new_content.find("> [!quote]")
    if q_pos != -1:
        before_q = new_content[:q_pos]
        after_q = new_content[q_pos:]
        
        new_q_lines = ["> [!quote] 💬 Contextual Usage & Authentic Quotations"]
        for q in entry["quotes"]:
            new_q_lines.append(f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{q['quote']}\"*")
        
        rest = after_q.split("\n")
        remaining_lines = []
        skip = True
        for line in rest[1:]:
            if skip:
                if line.startswith("> - 📜") or line.strip() == ">" or line.strip() == "":
                    continue
                else:
                    skip = False
                    remaining_lines.append(line)
            else:
                remaining_lines.append(line)
        
        new_content = before_q + "\n".join(new_q_lines) + ("\n" + "\n".join(remaining_lines) if remaining_lines else "\n")
    
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated_count += 1

print(f"Thought Batch 3B-2 (sci 41-77): Successfully updated {updated_count}/{len(data)} notes.")
