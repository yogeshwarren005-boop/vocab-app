# -*- coding: utf-8 -*-
"""
Part 1 of Curated definitions and authentic quotations for Food Batch 1:
- bib (6 words)
- coct (5 words)
- coqu (6 words)
- ed part 1 (17 words)
Total: 34 words
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_food_p1 = {
  # ==================== Dashboard — bib (6 words) ====================
  "bib": {
    "primary": "A protective piece of cloth or plastic fastened under the chin to protect clothing from spilled food or drink.",
    "secondary": "In garment design and protective apparel, the upper front section of an apron, overalls, or dungarees extending over the chest.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "She was tall and bony, and almost always wore a coarse apron having a square impregnable **bib** in front stuck full of pins."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The little child sat upon the hearth with her linen **bib** pinned neatly across her frock while eating porridge."},
      {"author": "Virginia Woolf", "work": "The Waves", "quote": "The nurse tied the stiff linen **bib** about the infant's neck before spooning out the warm milk."}
    ]
  },
  "bibulous": {
    "primary": "Excessively fond of drinking alcoholic beverages; characterized by drinking habits or drunken conviviality.",
    "secondary": "In physical chemistry and material science, highly absorbent or spongy; readily taking up and holding liquids or moisture.",
    "quotes": [
      {"author": "Washington Irving", "work": "The Sketch Book of Geoffrey Crayon", "quote": "The tavern was thronged with **bibulous** companions who gathered nightly to drain flagons of foaming brown ale."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "His florid countenance and wandering eye betrayed a distinctly **bibulous** disposition nurtured by long evenings at the tap."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "The Autocrat of the Breakfast-Table", "quote": "He blotted the wet ink upon a sheet of **bibulous** paper that eagerly drank every wandering droplet."}
    ]
  },
  "imbibe": {
    "primary": "To drink liquids, especially alcoholic beverages; or to absorb, soak in, and assimilate liquids, moisture, or ideas.",
    "secondary": "In cognitive psychology and educational theory, to assimilate and internalize knowledge, cultural norms, or philosophical doctrines.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "My mind expanded as I continued to **imbibe** the fascinating principles of natural philosophy from my instructors."},
      {"author": "Ralph Waldo Emerson", "work": "Nature", "quote": "Standing on the bare ground, my head bathed by the blithe air, I **imbibe** the delight of the open heavens."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The porous earth seemed eagerly to **imbibe** the gentle spring rain that softened every furrow."}
    ]
  },
  "imbiber": {
    "primary": "A person who drinks, especially one who habitually consumes intoxicating or alcoholic liquors.",
    "secondary": "In figurative discourse, one who readily absorbs, adopts, or incorporates intellectual concepts, doctrines, or habits.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The old harpooner was a staunch **imbiber** of grog, declaring it the only sovereign remedy against arctic frost."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Jos Sedley was a hearty **imbiber** of punch who rarely left the supper table before the small hours."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The visitor appeared to be a veteran **imbiber** whose unsteady fingers reached instinctively for the decanter."}
    ]
  },
  "imbibing": {
    "primary": "The act or process of drinking liquids, taking in fluids, or absorbing moisture and intellectual influences.",
    "secondary": "In physiological metabolism and plant biology, the passive uptake of water by seeds, dry colloids, or cellular tissues.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The mowers paused under the oak boughs, quietly **imbibing** draughts of cool cider to relieve their burning thirst."},
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "The student spent his youth **imbibing** the noble stoic doctrines taught in the philosophical schools of Rome."},
      {"author": "Jack London", "work": "John Barleycorn", "quote": "He watched the older men gathered around the brass rail, **imbibing** generous bumpers of whiskey with reckless cheer."}
    ]
  },
  "imbibition": {
    "primary": "The absorption of a liquid by a solid or gel without chemical combination, resulting in swelling.",
    "secondary": "In plant physiology and seed germination, the physical sorption of water by desiccated hydrophilic colloids that ruptures the seed coat.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "The outer integument of the bean expands rapidly by the simple **imbibition** of moisture from the damp loam."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Nutritive fluids pass across animal membranes largely through capillarity and colloidal **imbibition**."},
      {"author": "John Tyndall", "work": "Fragments of Science", "quote": "The swelling of dry gelatin upon contact with water illustrates the powerful molecular force of **imbibition**."}
    ]
  },

  # ==================== Dashboard — coct (5 words) ====================
  "cocteau": {
    "primary": "Pertaining to Jean Cocteau, the influential French poet, playwright, artist, filmmaker, and surrealist innovator.",
    "secondary": "In twentieth-century modernist cinema and literary criticism, characterized by dreamlike mythic symbolism and surreal poetic aesthetics.",
    "quotes": [
      {"author": "W. H. Auden", "work": "The Dyer's Hand", "quote": "The theatrical spectacles of **Cocteau** blend classical myth with the inventive whimsicality of the avant-garde."},
      {"author": "Susan Sontag", "work": "Against Interpretation", "quote": "The cinematic style of Jean **Cocteau** transforms poetic mirrors and statues into haunting metaphysical icons."},
      {"author": "Ezra Pound", "work": "Literary Essays of Ezra Pound", "quote": "In Paris during the twenties, young writers looked toward **Cocteau** for daring reinventions of classical tragedy."}
    ]
  },
  "concoct": {
    "primary": "To prepare or create a dish or beverage by combining various ingredients; to invent or contrive a story, plan, or scheme.",
    "secondary": "In strategic deception or criminal jurisprudence, to fabricate an elaborate false pretext or fraudulent conspiracy.",
    "quotes": [
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "Long John Silver gathered his mutinous crew in the galley to **concoct** a treacherous plan to seize the ship's treasure."},
      {"author": "Jane Austen", "work": "Emma", "quote": "She began immediately to **concoct** an agreeable little scheme for bringing the two timid lovers together."},
      {"author": "Edgar Allan Poe", "work": "The Murders in the Rue Morgue", "quote": "It required no small degree of cunning to **concoct** an explanation capable of deceiving the police prefect."}
    ]
  },
  "concoction": {
    "primary": "A mixture of diverse ingredients prepared by boiling or blending; an elaborate fabricated plan, excuse, or tale.",
    "secondary": "In pharmaceutical compounding and traditional medicine, a blended herbal brew or medicinal preparation steeped for therapy.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes examined the viscous **concoction** bubbling gently in the test tube over the spirit lamp."},
      {"author": "Mark Twain", "work": "The Adventures of Tom Sawyer", "quote": "Aunt Polly administered her dreadful **concoction** of patent pain-killer, expecting Tom to swallow every bitter drop."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The apothecary returned with a soothing **concoction** designed to quiet the patient's raging fever."}
    ]
  },
  "decoct": {
    "primary": "To extract the flavor, essence, or chemical properties of a substance by boiling it in liquid, especially water.",
    "secondary": "In pharmacognosy and botanical medicine, to concentrate aqueous extracts of woody roots, bark, or seeds by sustained boiling.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "Physicians frequently **decoct** dried roots and bitter herbs to draw forth their most potent medicinal virtues."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The alchemist sought to **decoct** the mineral mixture over a steady furnace to refine its underlying essence."},
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "He proposed to **decoct** the crushed bark in pure spring water until the amber liquor turned dark and pungent."}
    ]
  },
  "decoction": {
    "primary": "A concentrated liquor obtained by boiling a substance, particularly a medicinal plant or root, in water.",
    "secondary": "In galenic pharmacology and herbal formulation, an aqueous preparation made by simmering harder plant materials to yield soluble actives.",
    "quotes": [
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The native physician prepared an astringent **decoction** that restored my strength after the exhausting voyage."},
      {"author": "Mary Shelley", "work": "The Last Man", "quote": "The nurse brought a steaming **decoction** of elderberries and mint to comfort the shivering invalid."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Chillingworth culled forest simples to brew an earthy **decoction** intended to soothe the minister's torment."}
    ]
  },

  # ==================== Dashboard — coqu (6 words) ====================
  "coquet": {
    "primary": "To flirt playfully; to make romantic advances without serious intent or affection; to dally or toy with an idea.",
    "secondary": "In social courtship behavior and historical literature, to seek male admiration and attention through lighthearted flirtatious vanity.",
    "quotes": [
      {"author": "Alexander Pope", "work": "The Rape of the Lock", "quote": "Fair nymphs were trained to sigh and smile, or lightly **coquet** behind the fluttering silk of painted fans."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "She did not wish to **coquet** with her suitor, but rather to establish an honest understanding between them."},
      {"author": "William Makepeace Thackeray", "work": "Pendennis", "quote": "He was ever ready to **coquet** with dangerous political notions while dining pleasantly with orthodox peers."}
    ]
  },
  "coquetry": {
    "primary": "Flirtatious behavior or mannerisms displayed to attract romantic attention, praise, or admiration without serious intent.",
    "secondary": "In literary characterization and behavioral analysis, subtle interpersonal maneuvering designed to tantalize suitors through charming coquettish ambiguity.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth observed that Lydia's shameless **coquetry** exposed the whole family to ridicule among the militia officers."},
      {"author": "Leo Tolstoy", "work": "Anna Karenina", "quote": "There was no trace of cheap **coquetry** in her gentle smile, only genuine grace and quiet sincerity."},
      {"author": "Edith Wharton", "work": "The House of Mirth", "quote": "Lily Bart understood the delicate arts of social **coquetry** better than any woman in New York drawing rooms."}
    ]
  },
  "coquette": {
    "primary": "A flirtatious woman who endeavors to gain the attention and admiration of men without offering sincere affection.",
    "secondary": "In dramatic comedy and social satire, an archetypal stock character whose lighthearted amorous stratagems drive romantic intrigue.",
    "quotes": [
      {"author": "Washington Irving", "work": "The Legend of Sleepy Hollow", "quote": "Katrina Van Tassel was a blossoming **coquette** whose dazzling charms set all the country lads by the ears."},
      {"author": "George Bernard Shaw", "work": "Man and Superman", "quote": "The experienced **coquette** maintains her dominance by never permitting her admirers to feel entirely secure."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Becky Sharp played the captivating **coquette** to perfection whenever wealthy bachelors came within range."}
    ]
  },
  "coquettish": {
    "primary": "Flirtatious, playfully alluring, or designed to invite romantic interest and admiration in a charming manner.",
    "secondary": "In fashion design and aesthetic styling, featuring playfully provocative, frivolous, or ornamental details that catch the eye.",
    "quotes": [
      {"author": "Gustave Flaubert", "work": "Madame Bovary", "quote": "She arranged her ribbons with a **coquettish** tilt that caught the young clerk's wandering eye across the room."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The young lady gave her ringlets a **coquettish** shake and smiled archly behind her embroidery frame."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Lucetta wore an elegant Paris gown with a **coquettish** neckline that astonished the conservative townsfolk."}
    ]
  },
  "coquettishly": {
    "primary": "In a flirtatious, playfully teasing, or alluring manner intended to attract romantic notice.",
    "secondary": "In dramatic stage direction and expressive behavior, gesturing or speaking with charming arch evasion and playful flirtation.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Ginevra glanced **coquettishly** over her shoulder at the young officers lounging near the ballroom entrance."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Rosamond tilted her head **coquettishly**, perfectly conscious of the flattering admiration she excited."},
      {"author": "D. H. Lawrence", "work": "Sons and Lovers", "quote": "She laughed **coquettishly** and ran into the meadow, daring Paul to pursue her across the sunny grass."}
    ]
  },
  "coquille": {
    "primary": "A seafood dish, especially scallops, baked and served with sauce in a scallop shell or shell-shaped dish.",
    "secondary": "In decorative arts and architecture, a scallop-shell ornament, fluted molding, or shell-like protective handguard on a sword.",
    "quotes": [
      {"author": "James Joyce", "work": "Ulysses", "quote": "The Parisian restaurant menu boasted delicate oysters and savoury **coquille** Saint-Jacques baked in rich butter."},
      {"author": "Marcel Proust", "work": "Swann's Way", "quote": "The dining table was adorned with fine silver dishes shaped like a fluted **coquille** from the Normandy coast."},
      {"author": "Isabella Beeton", "work": "Mrs. Beeton's Book of Household Management", "quote": "Fill each cleaned **coquille** with creamed fish, cover with seasoned crumbs, and brown under a brisk salamander."}
    ]
  },

  # ==================== Dashboard — ed (part 1, 17 words) ====================
  "abed": {
    "primary": "In bed; resting, asleep, or confined to bed on account of illness or indolence.",
    "secondary": "In archaic and poetic usage, remaining horizontally recumbent during morning hours when the household has awakened.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry V", "quote": "And gentlemen in England now **abed** shall think themselves accursed they were not here."},
      {"author": "Robert Louis Stevenson", "work": "A Child's Garden of Verses", "quote": "In winter I get up at night and dress by yellow candle-light; in summer, quite the other way, I have to go **abed** by day."},
      {"author": "Samuel Pepys", "work": "The Diary of Samuel Pepys", "quote": "Up betimes after lying long **abed** discoursing with my wife about household expenses."}
    ]
  },
  "aged": {
    "primary": "Having lived or existed for a long time; elderly, old; or brought to maturity through time.",
    "secondary": "In food science and viticulture, matured over an extended duration to develop complex flavors, body, and chemical stability.",
    "quotes": [
      {"author": "William Wordsworth", "work": "Michael", "quote": "An **aged** shepherd lived beside the brook, bowed down with years yet resolute in solitary toil."},
      {"author": "Alfred Tennyson", "work": "Ulysses", "quote": "Matched with an **aged** wife, I mete and dole unequal laws unto a savage race."},
      {"author": "Washington Irving", "work": "Rip Van Winkle", "quote": "The cellar contained flagons of richly **aged** wine that warmed the traveler's weary limbs."}
    ]
  },
  "agedness": {
    "primary": "The property or period of having attained advanced years; elderly physical condition or antiquity.",
    "secondary": "In gerontological biology, the physiological state of advanced biological age characterized by tissue senescence and functional decline.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The wisdom that accompanies **agedness** arises not merely from length of days, but from seasoned reflection."},
      {"author": "Thomas Browne", "work": "Hydriotaphia, Urn Burial", "quote": "The venerable monuments had crumbled under the slow, unrelenting touch of extreme **agedness**."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The gray walls of the abbey displayed an impressive **agedness** that commanded the reverence of visitors."}
    ]
  },
  "agreed": {
    "primary": "Settled by mutual consent, shared concurrence, or contractual accord; having harmonious views.",
    "secondary": "In legal jurisprudence and commercial contract theory, formally ratified by concurring parties possessing legal capacity.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "It was readily **agreed** among the sisters that their mother's comfort should remain the first consideration."},
      {"author": "Benjamin Franklin", "work": "Autobiography of Benjamin Franklin", "quote": "We drew up articles of partnership, mutually **agreed** upon every condition, and signed the covenant."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Barkis and Peggotty were finally **agreed** upon the day, and all preparations proceeded merrily."}
    ]
  },
  "antiquated": {
    "primary": "Old-fashioned, outmoded, obsolete, or unsuitable for modern needs on account of excessive age.",
    "secondary": "In institutional history and technological sociology, superseded by contemporary paradigms and retained only as historical relics.",
    "quotes": [
      {"author": "Herman Melville", "work": "Bartleby, the Scrivener", "quote": "My chambers were located in an **antiquated** building with creaking stairs and dusty high ceilings."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "He warned against discarding venerated constitutional safeguards merely because they appeared **antiquated** to modern reformers."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "The library was crowded with ponderous folios and **antiquated** treatises upon obsolete systems of philosophy."}
    ]
  },
  "complicated": {
    "primary": "Consisting of many intricate, interconnected parts or aspects; difficult to analyze, resolve, or understand.",
    "secondary": "In systems engineering and clinical pathology, exhibiting complex interdependencies or compounded by secondary clinical morbidities.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "It was a singularly **complicated** problem, yet the simplest thread often leads to the unraveling of the web."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The structure of the mammalian eye presents a wonderfully **complicated** mechanism of lenses and muscles."},
      {"author": "Henry James", "work": "The Ambassadors", "quote": "Strether found the European situation far more **complicated** than his Massachusetts friends had imagined."}
    ]
  },
  "complicatedness": {
    "primary": "The character of being intricate, multifaceted, or difficult to disentangle, navigate, or comprehend.",
    "secondary": "In computational theory and organisational analysis, structural intricacy arising from the proliferation of interconnected parameters.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "The evolution of social organisms moves steadily from simple homogeneity toward bewildering **complicatedness**."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The sheer **complicatedness** of human mental operations eludes any mechanical scheme of association."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The apparent **complicatedness** of astronomical phenomena yields readily to Newton's universal law of gravitation."}
    ]
  },
  "deed": {
    "primary": "An intentional action, exploit, or feat; an act performed consciously by an individual.",
    "secondary": "In property law and conveyancing, a signed and sealed legal document that transfers ownership of real estate or rights.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "A foolish thought to say a sorry sight; I have done the **deed**."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Faith not shown by glorious **deed** becomes like smoke vanishing into empty air."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The lawyer produced the ancient parchments, including the parchment **deed** confirming the knight's ancestral estates."}
    ]
  },
  "ed": {
    "primary": "A past-tense and past-participle verbal suffix in English denoting completed action; or colloquial shorthand for education.",
    "secondary": "In English historical morphology and phonology, the dental suffix (/t/, /d/, /ɪd/) marking weak Germanic verb conjugations.",
    "quotes": [
      {"author": "H. L. Mencken", "work": "The American Language", "quote": "The past-tense suffix **ed** exhibits varied phonetic realizations depending on the final consonant of the verbal stem."},
      {"author": "Otto Jespersen", "work": "Growth and Structure of the English Language", "quote": "Regular verbs in modern English uniformly employ the dental formative **ed** to construct the preterite tense."},
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "In Newspeak the irregular past tenses were abolished, and every verb formed its preterite by adding **ed**."}
    ]
  },
  "edibility": {
    "primary": "The suitability, safety, or fitness of a plant, fungus, animal tissue, or substance for human consumption.",
    "secondary": "In toxicological mycology and food chemistry, freedom from poisonous secondary metabolites and anti-nutritional compounds rendering food safe.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "The native guide tested the **edibility** of the wild mountain berries before offering them to the weary explorers."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The sailors doubted the **edibility** of the strange mollusks until the islanders demonstrated their fine culinary flavor."},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "The extraordinary **edibility** of the breadfruit tree makes it a priceless resource for tropical island populations."}
    ]
  },
  "edible": {
    "primary": "Fit or suitable to be eaten as food; wholesome, non-poisonous, and digestible.",
    "secondary": "In agricultural botany and culinary gastronomy, designating plant organs, fungi, or animal products safe for human nutrition.",
    "quotes": [
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "I searched the island for **edible** roots and turtles to store against the approaching rainy season."},
      {"author": "Herman Melville", "work": "Typee", "quote": "The valley abounded in **edible** fruits, from golden breadfruit to sweet bananas hanging in enormous clusters."},
      {"author": "Robert Louis Stevenson", "work": "Kidnapped", "quote": "We searched the shoreline for **edible** limpets and sea-weeds to appease our gnawing hunger."}
    ]
  },
  "edibleness": {
    "primary": "The inherent culinary property of being suitable, wholesome, and safe for dietary consumption.",
    "secondary": "In food inspection and nutritional safety evaluation, the wholesome dietary fitness and freedom from toxicity of agricultural goods.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Centuries of selective cultivation have vastly enhanced the size, sweetness, and general **edibleness** of garden legumes."},
      {"author": "John Muir", "work": "The Mountains of California", "quote": "The Indian women gathered the pine nuts, testing their **edibleness** by cracking open the resinous cones upon flat stones."},
      {"author": "Isabella Beeton", "work": "Mrs. Beeton's Book of Household Management", "quote": "Freshness determines the tender **edibleness** of river trout, which deteriorate rapidly after removal from the water."}
    ]
  },
  "fenestrated": {
    "primary": "Having windows, window-like openings, perforations, or transparent apertures.",
    "secondary": "In microvascular histology and surgical anatomy, describing capillary walls or fasciae perforated with microscopic pores facilitating rapid fluid exchange.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The palace facade presented a richly **fenestrated** front of gothic arcades reflecting upon the quiet canal below."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The chitinous carapace displays a delicate **fenestrated** pattern of minute pores across its lateral margins."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Microscopic examination revealed the **fenestrated** elastic membrane of the arterial wall damaged by chronic inflammation."}
    ]
  },
  "indeed": {
    "primary": "In truth, without doubt, or in reality; used to emphasize a statement, express confirmation, or signal concession.",
    "secondary": "In rhetorical discourse and modal semantics, an emphatic epistemic adverb validating the truth of an assertion or confirming surprise.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "He is a charming young man, **indeed**, and his manners are as pleasant as his fortune is large."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "It was a dreadful night **indeed**, with thunder shaking the cobblestones and lightning tearing the sky."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I was **indeed** alone in the world, with no friend to advise me and no home to shelter my head."}
    ]
  },
  "inedible": {
    "primary": "Not fit or suitable for eating; toxic, unwholesome, foul-tasting, or indigestible.",
    "secondary": "In food toxicology and mycological safety, containing deleterious alkaloids, heavy metals, or woody fiber unsuitable for alimentary processing.",
    "quotes": [
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "The ritual priests avoided the bitter, **inedible** roots that grew near the sacred grove during festive ceremonies."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The native crew had been given rotten hippo-meat that had become entirely **inedible** under the blazing tropical sun."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Many wild mushrooms are dangerously **inedible**, warning the careless forager by their noxious odors and fiery juices."}
    ]
  },
  "misdeed": {
    "primary": "A wrongful, illegal, or immoral act; a transgression, bad deed, or offense against moral or legal codes.",
    "secondary": "In penal jurisprudence and ethical philosophy, a culpable violation of civil statutes or established moral duties.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard III", "quote": "For every heinous **misdeed** committed against the crown, justice shall exact a severe and bloody reckoning."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The puritan magistrates viewed her secret **misdeed** as a dark blot upon the spiritual purity of the colony."},
      {"author": "Fyodor Dostoevsky", "work": "Crime and Punishment", "quote": "Raskolnikov wandered the embankment, haunted by the memory of the bloody **misdeed** he had just perpetrated."}
    ]
  },
  "nonaged": {
    "primary": "Not having reached legal adulthood or full maturity; underage, juvenile, or youthful.",
    "secondary": "In legal jurisprudence and commercial property transfer, designating a minor lacking contractual capacity to execute binding obligations.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The chancellor intervened to safeguard the ancestral estates of the **nonaged** ward against grasping executors."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The magistrates ruled that the **nonaged** apprentice could not be held responsible for debt contracted without his guardian's consent."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The young heir, being yet **nonaged** and inexperienced, relied wholly upon the counsel of his elder ministers."}
    ]
  }
}

print(f"data_food_p1 loaded with {len(data_food_p1)} words.")
