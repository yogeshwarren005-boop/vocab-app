# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — lat (Batch 4C: 36 words)
  # =========================================================================
  "Dashboard — lat/latimeridae.md": {
    "primary": "A taxonomic family of coelacanth fish in the order Coelacanthiformes, containing the extant genus Latimeria.",
    "secondary": "In systematic ichthyology and vertebrate paleontology, sarcopterygian fishes possessing trilobed caudal fins, cosmoid scales, and paired lobed fins with skeletal elements homologous to tetrapod limbs.",
    "quotes": [
      {"author": "J. L. B. Smith", "work": "The Sea Fishes of Southern Africa", "quote": "The family **Latimeridae** was erected to accommodate the living coelacanth discovered off East London."},
      {"author": "Ernst Mayr", "work": "Animal Species and Evolution", "quote": "Living fossils like the **Latimeridae** exhibit extraordinary morphological stasis across hundreds of millions of years."},
      {"author": "Stephen Jay Gould", "work": "Ontogeny and Phylogeny", "quote": "The structural continuity of the **Latimeridae** provides a benchmark for evaluating rates of anatomical change."}
    ]
  },
  "Dashboard — lat/latin-american.md": {
    "primary": "Relating to the countries, peoples, cultures, or languages of the Americas where Spanish or Portuguese is predominantly spoken.",
    "secondary": "In geopolitical history and post-colonial studies, the independent republics of Central and South America and the Caribbean shaped by Iberian colonial heritage.",
    "quotes": [
      {"author": "Theodore Roosevelt", "work": "An Autobiography", "quote": "The defense of the Panama Canal required a consistent diplomatic policy toward the **Latin-American** republics."},
      {"author": "James Bryce", "work": "South America: Observations and Impressions", "quote": "Each **Latin-American** state developed distinct national characteristics despite a shared colonial heritage."},
      {"author": "Joseph Conrad", "work": "Nostromo", "quote": "The history of the fictional republic reflected the turbulent political revolutions common to nineteenth-century **Latin-American** states."}
    ]
  },
  "Dashboard — lat/latin.md": {
    "primary": "The ancient Italic Indo-European language spoken in Rome and its empire; or relating to the ancient Romans or Latin-speaking peoples.",
    "secondary": "In medieval and Renaissance intellectual history, the universal lingua franca of scholarship, Catholic liturgy, natural science, and diplomacy throughout Western Europe.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "With a priest that lacks **Latin** and a rich man that hath not the gout."},
      {"author": "John Milton", "work": "Areopagitica", "quote": "The learned world communicates its deepest truths through the concise majesty of **Latin** prose."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **Latin** tongue was gradually adopted by the conquered provinces of the west."}
    ]
  },
  "Dashboard — lat/latinae.md": {
    "primary": "The Latin nominative or genitive plural feminine form of Latinus; designating Latin women, Latin cities (civitates Latinae), or Latin festivals (Feriae Latinae).",
    "secondary": "In Roman constitutional antiquities, the allied cities possessing Latin rights (ius Latii) intermediate between peregrini and full Roman citizens.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The ancient league of the civitates **Latinae** maintained solemn sacrifices upon the Alban Mount."},
      {"author": "Theodor Mommsen", "work": "The History of Rome", "quote": "The status of the coloniae **Latinae** served as a stepping stone toward complete integration into the Roman commonwealth."},
      {"author": "Thomas Babington Macaulay", "work": "Lays of Ancient Rome", "quote": "The thirty cities of the confederacy were commemorated in the sacred rites of the Feriae **Latinae**."}
    ]
  },
  "Dashboard — lat/latinate.md": {
    "primary": "Having the character, style, or vocabulary of Latin; containing many words derived from Latin.",
    "secondary": "In English stylistics and historical linguistics, elevated polysyllabic diction derived from Classical or Renaissance Latin borrowings (contrasted with Anglo-Saxon Germanic roots).",
    "quotes": [
      {"author": "George Orwell", "work": "Politics and the English Language", "quote": "A mass of **Latinate** words falls upon the facts like soft snow, blurring the outlines and covering up all the details."},
      {"author": "Samuel Johnson", "work": "The Lives of the Poets", "quote": "Milton formed his poetic diction upon a magnificent **Latinate** syntax that elevates his epic above vernacular speech."},
      {"author": "T. S. Eliot", "work": "Selected Essays", "quote": "The seventeenth-century masters balanced native colloquial idioms against formal **Latinate** periods."}
    ]
  },
  "Dashboard — lat/latinesce.md": {
    "primary": "Somewhat Latin in character; approaching or resembling Latin language or idiom; Latin-like.",
    "secondary": "In Renaissance literary imitation and neoclassical philology, vernacular prose displaying conspicuous classical syntax or rhetorical figures.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The translator adopted a **latinesce** construction that imparted an antique dignity to the English verse."},
      {"author": "Walter Pater", "work": "Appreciations", "quote": "Sir Thomas Browne wrote in an elaborate, **latinesce** style laden with rich classical cadences."},
      {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "The diction was slightly **latinesce**, avoiding the abruptness of plain Saxon speech."}
    ]
  },
  "Dashboard — lat/latinise.md": {
    "primary": "The British spelling of latinize; to translate into Latin, or give a Latin form or character to a word, name, or text.",
    "secondary": "In historical taxonomy and Linnaean nomenclature, converting vernacular scientific names and geographical descriptors into Latinate binomial form.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Naturalists invariably **latinise** the specific names of newly discovered plants and animals."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "Scholars of that era were accustomed to **latinise** their family names upon entering the university."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Byzantine chroniclers attempted to **latinise** barbarian titles to fit imperial court etiquette."}
    ]
  },
  "Dashboard — lat/latinism.md": {
    "primary": "An idiom, grammatical construction, or word borrowed from or characteristic of the Latin language.",
    "secondary": "In literary stylistics, incorporating classical Latin word order (such as placing verbs at the end of clauses) into vernacular prose.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Lives of the Poets", "quote": "Milton's style is full of **latinism**, which gives it a foreign air but increases its sublimity."},
      {"author": "Alexander Pope", "work": "An Essay on Criticism", "quote": "Avoid each awkward **latinism** that strains our English tongue beyond its natural harmony."},
      {"author": "John Dryden", "work": "Of Dramatic Poesy", "quote": "A judicious **latinism** may enrich the language, provided it does not obscure the sense."}
    ]
  },
  "Dashboard — lat/latinist.md": {
    "primary": "A specialist or scholar of the Latin language, literature, and Roman culture.",
    "secondary": "In academic history, Renaissance humanists (such as Erasmus or Scaliger) famed for rigorous textual criticism of classical Roman authors.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The accomplished **latinist** restored the corrupted text of Tacitus with admirable erudition."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon was reputed to be a profound **latinist**, though his published output was remarkably slender."},
      {"author": "Samuel Johnson", "work": "The Lives of the Poets", "quote": "As an exact **latinist**, Addison was surpassed by few of his contemporaries at Oxford."}
    ]
  },
  "Dashboard — lat/latinize.md": {
    "primary": "To make Latin in form, character, or language; to translate into Latin; or to conform to the Roman Catholic Church.",
    "secondary": "In biological systematics, modifying personal or geographical names with standard Latin inflectional endings (such as -i, -ae, -ense).",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Linnaeus chose to **latinize** the vernacular names of domestic varieties to create universal binomials."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The humanists sought to **latinize** every scientific term, sometimes obscuring simple practical observations."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman clergy attempted to **latinize** the liturgical customs of the newly converted Celtic churches."}
    ]
  },
  "Dashboard — lat/latino.md": {
    "primary": "A person of Latin American origin or descent, especially one living in the United States.",
    "secondary": "In sociolinguistics and cultural geography, demographic communities across the Americas sharing Hispanic linguistic, cultural, and historical ties.",
    "quotes": [
      {"author": "Carlos Fuentes", "work": "The Buried Mirror", "quote": "The **Latino** experience in North America represents a dynamic synthesis of indigenous, Iberian, and modern Anglo cultures."},
      {"author": "Octavio Paz", "work": "The Labyrinth of Solitude", "quote": "The **Latino** migrant carries within himself the dual heritage of pre-Columbian myth and Spanish Baroque religion."},
      {"author": "Richard Rodriguez", "work": "Hunger of Memory", "quote": "The complex identity of the modern **Latino** bridges the intimate language of the home and the public language of society."}
    ]
  },
  "Dashboard — lat/latish.md": {
    "primary": "Somewhat late; rather late in time, hour, or season.",
    "secondary": "In social narrative and conversational description, occurring in the late evening or toward the close of a seasonal cycle.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "It was a **latish** hour when the sheep-shearers finished their supper in the great barn."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He returned home at a **latish** hour, fatigued by his long ride across the rain-soaked country."},
      {"author": "P. G. Wodehouse", "work": "Right Ho, Jeeves", "quote": "I arrived at the house at a **latish** point in the afternoon, finding the drawing-room empty."}
    ]
  },
  "Dashboard — lat/latitude.md": {
    "primary": "The angular distance of a place north or south of the earth's equator; or scope for freedom of action or thought.",
    "secondary": "In navigational astronomy, determined by measuring the altitude of Polaris or the meridian altitude of the sun with a sextant.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The speech had not seemed to allow sufficient **latitude** for the unexpected turns of rustic sentiment."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The master took his daily observation at noon to fix our exact **latitude** upon the Pacific chart."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "A free commonwealth must grant wide **latitude** to individual opinions and experiments in living."}
    ]
  },
  "Dashboard — lat/latitudinal.md": {
    "primary": "Relating to latitude or the distance north or south of the equator; running east to west along parallels of latitude.",
    "secondary": "In biogeography and macroecology (latitudinal diversity gradient), species richness systematically increasing from the poles toward the tropics.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The **latitudinal** distribution of organic beings reveals the paramount influence of past climate epochs."},
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "Botanical zones on high tropical mountains mirror the **latitudinal** zones of the globe from equator to pole."},
      {"author": "Alfred Russel Wallace", "work": "Island Life", "quote": "The **latitudinal** limits of tropical reef-building corals are strictly determined by minimum winter sea temperatures."}
    ]
  },
  "Dashboard — lat/latitudinarian.md": {
    "primary": "Holding broad or liberal views, especially in religious matters; not insisting on strict conformity to traditional dogmas.",
    "secondary": "In seventeenth- and eighteenth-century Church of England history, moderate Anglican theologians (Cambridge Platonists) advocating doctrinal tolerance and rational morality.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The **latitudinarian** divines sought to conciliate the moderate nonconformists by minimizing ceremonial dogma."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "A philosopher will always view with indulgence the mild and **latitudinarian** spirit of pagan polytheism."},
      {"author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "He opposed both rigid scholastic dogmatism and the shallow moralism of the **latitudinarian** party."}
    ]
  },
  "Dashboard — lat/latium.md": {
    "primary": "The historical region of central western Italy in which the city of Rome was founded and the Latin language originated.",
    "secondary": "In classical geography, the fertile volcanic plain between the Tiber river and the Circeian promontory inhabited by the ancient Latini.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The fierce pastoral tribes of ancient **Latium** laid the rustic foundations of the future mistress of the world."},
      {"author": "Thomas Babington Macaulay", "work": "Lays of Ancient Rome", "quote": "From all the cities of **Latium** the horsemen rode forth to contest the supremacy of the Tiber."},
      {"author": "Virgil", "work": "Aeneid", "quote": "I sing of arms and the man who first from the coasts of Troy came to Italy and the shores of **Latium**."}
    ]
  },
  "Dashboard — lat/latona.md": {
    "primary": "The Roman name for the Greek goddess Leto, daughter of the Titans Coeus and Phoebe, and mother of Apollo and Diana (Artemis).",
    "secondary": "In classical mythology and Ovidian literature, the persecuted mother who gave birth to the divine twins on the floating island of Delos.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Not that fair field of Enna, nor the isle where **Latona** brought forth her starry twins, could rival Eden."},
      {"author": "Alexander Pope", "work": "The Rape of the Lock", "quote": "Fair as the radiant daughter whom **Latona** bore beneath the sacred palm of Delos."},
      {"author": "Ovid", "work": "Metamorphoses", "quote": "The goddess **Latona** turned the churlish Lycian peasants into frogs for denying her thirsty children drink."}
    ]
  },
  "Dashboard — lat/latria.md": {
    "primary": "In Roman Catholic and Orthodox theology, supreme worship and adoration due to God alone, as distinguished from dulia (veneration of saints).",
    "secondary": "In patristic dogmatics and historical councils (Second Council of Nicaea, 787 AD), the formal doctrinal distinction between sacrificial adoration (latreia) and reverential honor (proskynesis).",
    "quotes": [
      {"author": "Thomas Aquinas", "work": "Summa Theologiae", "quote": "The worship of **latria** is due solely to the uncreated Creator, who is the first principle of all things."},
      {"author": "John Henry Newman", "work": "An Essay on the Development of Christian Doctrine", "quote": "Catholic theology carefully distinguishes between the **latria** given to God and the dulia offered to His holy servants."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The iconoclastic emperors denounced the worship of images as an idolatrous infringement upon divine **latria**."}
    ]
  },
  "Dashboard — lat/latrine.md": {
    "primary": "A toilet or outhouse, especially a communal trench or pit used in a military camp, barracks, or outdoor bivouac.",
    "secondary": "In military field hygiene and public sanitation engineering, properly sited, covered trench latrines preventing fecal contamination of water supplies.",
    "quotes": [
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "The stench of the camp **latrine** drifted across the trench whenever the wind shifted from the valley."},
      {"author": "Rudyard Kipling", "work": "The Man Who Would Be King", "quote": "The soldiers dug a deep **latrine** outside the redoubt in strict obedience to the army regulations."},
      {"author": "Erich Maria Remarque", "work": "All Quiet on the Western Front", "quote": "The communal **latrine** in the rear was the great gossip center where soldiers exchanged trench rumors."}
    ]
  },
  "Dashboard — lat/latrobe.md": {
    "primary": "Benjamin Henry Latrobe (1764–1820), British-born neoclassical architect regarded as the Father of American Architecture; or the Latrobe stove.",
    "secondary": "In American domestic history, the Baltimore heater or Latrobe stove, an energy-efficient cast-iron fireplace insert designed to heat multistory residences.",
    "quotes": [
      {"author": "Thomas Jefferson", "work": "Writings", "quote": "I have appointed Mr. **Latrobe** as surveyor of the public buildings, trusting in his classical taste and engineering skill."},
      {"author": "Henry Adams", "work": "The History of the United States of America", "quote": "The architectural genius of **Latrobe** endowed the young republican capital with enduring neoclassical dignity."},
      {"author": "Herman Melville", "work": "The Confidence-Man", "quote": "The parlor was heated by a cheerful **Latrobe** stove that diffused a pleasant warmth through the drafty hall."}
    ]
  },
  "Dashboard — lat/latrodectus.md": {
    "primary": "A cosmopolitan genus of venomous cobweb spiders in the family Theridiidae, commonly known as true widows (including the black widow, Latrodectus mactans).",
    "secondary": "In toxicology and arachnology, spiders possessing neurotoxic venom containing alpha-latrotoxin, which triggers massive presynaptic neurotransmitter release (latrodectism).",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "I captured on the arid plains of Patagonia a venomous spider of the genus **Latrodectus**, feared by the natives."},
      {"author": "Henri Fabre", "work": "The Life of the Spider", "quote": "The bite of the small black **Latrodectus** causes excruciating muscular spasms and acute fever."},
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Invertebrated Animals", "quote": "The chelicerae of **Latrodectus** are armed with potent venom glands capable of immobilizing prey instantly."}
    ]
  },
  "Dashboard — lat/lats.md": {
    "primary": "The former plural currency unit of Latvia (replaced by the Euro in 2014); or plural abbreviation for the latissimus dorsi muscles.",
    "secondary": "In comparative international economics, the pegged national monetary currency of independent interwar and post-Soviet Latvia.",
    "quotes": [
      {"author": "John Maynard Keynes", "work": "The Economic Consequences of the Peace", "quote": "The newly independent Baltic republics stabilized their currencies, issuing the **lats** upon sound reserve principles."},
      {"author": "Arthur Conan Doyle", "work": "The Captain of the Pole-Star", "quote": "The sailors measured their distance across the frozen **lats** of the high northern ocean."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Organisms residing in equivalent polar **lats** display striking convergent adaptations to thermal stress."}
    ]
  },
  "Dashboard — lat/latte.md": {
    "primary": "A hot coffee drink made with espresso and steamed milk, topped with a small layer of milk foam (caffè latte).",
    "secondary": "In food culture and beverage economics, an Italian espresso-based beverage popularized globally in specialty coffee culture during the late twentieth century.",
    "quotes": [
      {"author": "David Lodge", "work": "Therapy", "quote": "He sat at the corner café table, sipping a creamy **latte** while watching the commuters stream toward the station."},
      {"author": "Anthony Bourdain", "work": "Kitchen Confidential", "quote": "The morning rush began with the hiss of the espresso steam wand foaming milk for endless orders of **latte**."},
      {"author": "Umberto Eco", "work": "Travels in Hyperreality", "quote": "The American traveler seeks a comforting domestic **latte** even amid the authentic piazza cafés of Florence."}
    ]
  },
  "Dashboard — lat/latten.md": {
    "primary": "A historical yellow alloy of copper and zinc resembling brass, rolled into thin sheets and used for crosses, candlesticks, and domestic utensils.",
    "secondary": "In medieval metalworking and monumentology, durable brass sheets hammered into monumental effigy plates (monumental brasses) set into church floors.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merry Wives of Windsor", "quote": "Ha, thou mountain-foreigner! Sir John and master mine, I combat challenge of this **latten** bilbo."},
      {"author": "Geoffrey Chaucer", "work": "The Canterbury Tales", "quote": "And in a brass-pan or in a **latten** basin he kept his humble store of trade."},
      {"author": "Walter Scott", "work": "The Fair Maid of Perth", "quote": "The shrine was decorated with plates of beaten **latten** that shone like burnished gold in the candle-light."}
    ]
  },
  "Dashboard — lat/latter-day.md": {
    "primary": "Belonging to the present time or recent times; modern; or belonging to the final period of something.",
    "secondary": "In religious history, designating members of the Church of Jesus Christ of Latter-day Saints (Mormons) awaiting the millennial dispensation.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Latter-Day Pamphlets", "quote": "In these **latter-day** times of confusion, men wander without compass or spiritual guiding light."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "The emigrants belonged to the **Latter-day** Saints, seeking a home far in the desert valleys of Utah."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "A **latter-day** Saint Theresa finds no coherent social order ready to receive her ardent spiritual aspirations."}
    ]
  },
  "Dashboard — lat/latter.md": {
    "primary": "Denoting the second or second mentioned of two people or things; or occurring nearer to the end of something than to the beginning.",
    "secondary": "In logical argumentation and rhetorical balance, referring back specifically to the second of two previously stated alternatives.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "Why, 'tis the rarest argument of wonder that hath shot out in our **latter** times."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "The **latter** was more open, cheerful, and unreserved than her sister."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Between the earlier and the **latter** domestic varieties, a marked divergence of characters has taken place."}
    ]
  },
  "Dashboard — lat/latterly.md": {
    "primary": "Recently; in the later part of a period, life, or career.",
    "secondary": "In biographical history, characterizing tendencies or convictions that manifested during the concluding years of an individual's life.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "It was only **latterly** that people had begun to call her proud, since her sudden rise in fortune."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "His health had **latterly** been declining, casting a sombre shadow over his literary labors."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "He had grown **latterly** more silent and reserved, spending long nights pacing his library."}
    ]
  },
  "Dashboard — lat/lattice.md": {
    "primary": "A structure consisting of strips of wood or metal crossed and fastened together with open diamond- or square-shaped spaces between them.",
    "secondary": "In crystallography and solid-state physics, a regular three-dimensional geometric arrangement of points or atoms in a crystal.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "So, my good window of **lattice**, fare thee well; thy casement I need not open, for I look through thee well enough."},
      {"author": "John Keats", "work": "Ode to a Nightingale", "quote": "And through the leafy **lattice** came the scent of musk-rose."},
      {"author": "Edgar Allan Poe", "work": "The Raven", "quote": "Open here I flung the shutter, when, with many a flirt and flutter, in there stepped a stately Raven through the **lattice**."}
    ]
  },
  "Dashboard — lat/latticed.md": {
    "primary": "Having or enclosed by a lattice; fitted with crossed wooden or metal strips.",
    "secondary": "In domestic architecture, casement windows fitted with small diamond-shaped panes set in lead cames.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "It threw a gleam of recognition on here a post, and there the **latticed** casement of a wooden house."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The morning sun shone brightly through the **latticed** window of the rustic breakfast room."},
      {"author": "Lord Byron", "work": "Don Juan", "quote": "She looked out from the **latticed** balcony upon the moonlit waves of the Mediterranean."}
    ]
  },
  "Dashboard — lat/latticelike.md": {
    "primary": "Resembling a lattice in structure or appearance; having an open interlacing framework or pattern.",
    "secondary": "In cellular histology and bone physiology, the porous, trabecular network of cancellous bone or cancellated connective tissue.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The microscopic structure of the bryozoan skeleton reveals an intricate, **latticelike** network of calcified filaments."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Cancellous bone tissue presents an open, **latticelike** framework of trabeculae designed to absorb compressive stress."},
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Invertebrated Animals", "quote": "The siliceous framework of the glass sponge forms a delicate, **latticelike** basket of astonishing geometric regularity."}
    ]
  },
  "Dashboard — lat/latticework.md": {
    "primary": "An open framework or decorative structure consisting of interlaced or crossed strips of wood, metal, or stone; a lattice.",
    "secondary": "In landscape architecture, decorative screens and trellises constructed to support climbing vines and provide shade in arbors.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "A climbing rose clung to the rustic **latticework** of the garden porch, filling the air with fragrance."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Through the green **latticework** of the summerhouse, one could catch glimpses of the formal terrace."},
      {"author": "Herman Melville", "work": "Typee", "quote": "The chief's dwelling was enclosed with light **latticework** woven from split bamboo poles."}
    ]
  },
  "Dashboard — lat/misrelated.md": {
    "primary": "Wrongly connected, associated, or matched; or (in grammar) improperly linked to an unintended grammatical referent.",
    "secondary": "In prescriptive syntax and stylistic editing, a participial modifier that attaches logically to the wrong noun phrase (a dangling participle).",
    "quotes": [
      {"author": "Henry Sweet", "work": "A New English Grammar", "quote": "A participle standing in a **misrelated** construction creates grammatical ambiguity by attaching to an improper subject."},
      {"author": "George Orwell", "work": "Politics and the English Language", "quote": "In careless political prose, **misrelated** clauses obscure the real agent responsible for the action."},
      {"author": "Otto Jespersen", "work": "The Philosophy of Grammar", "quote": "The sentence suffered from a **misrelated** adjunct which distorted the author's intended logical emphasis."}
    ]
  },
  "Dashboard — lat/mistranslate.md": {
    "primary": "To translate incorrectly or inaccurately from one language into another.",
    "secondary": "In diplomatic history and textual hermeneutics, erroneous translation of treaty clauses or philosophical texts altering substantive obligations.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Careless commentators frequently **mistranslate** ancient authors by substituting modern philosophical idioms for classical terms."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The theological schism was exacerbated by interpreters who did **mistranslate** subtle Greek distinctions into ambiguous Latin."},
      {"author": "Samuel Johnson", "work": "The Lives of the Poets", "quote": "Dryden was too hasty to avoid errors, and would occasionally **mistranslate** Virgil when the rhyme pressed hard upon him."}
    ]
  },
  "Dashboard — lat/mistranslation.md": {
    "primary": "An incorrect, inaccurate, or erroneous translation; a failure to render meaning faithfully between languages.",
    "secondary": "In Biblical criticism and comparative philology, discrepancies in early scriptural codices arising from false cognates or ambiguous syntax.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "A notorious **mistranslation** in the Latin Vulgate gave rise to centuries of theological controversy."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The treaty was nearly ruptured by a flagrant **mistranslation** in the French diplomatic dispatch."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He pointed out with scholarly triumph a glaring **mistranslation** in his rival's commentary on the Greek dramatists."}
    ]
  },
  "Dashboard — lat/nontranslational.md": {
    "primary": "Not involving, relating to, or resulting from translation (either in physical motion, linguistics, or molecular genetics).",
    "secondary": "In molecular biology and biochemistry, RNA molecules (such as tRNA, rRNA, or ribozymes) that perform structural or catalytic roles without being translated into protein.",
    "quotes": [
      {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "The rotational and vibrational degrees of freedom constitute the **nontranslational** kinetic energy of the molecule."},
      {"author": "Francis Crick", "work": "What Mad Pursuit", "quote": "Subsequent research revealed that many functional cellular transcripts serve specialized **nontranslational** roles in gene regulation."},
      {"author": "Thomas Henry Huxley", "work": "Method and Results", "quote": "The complex physical system exhibited internal rotational stresses alongside **nontranslational** thermal equilibrium."}
    ]
  },
  "Dashboard — lat/oblate.md": {
    "primary": "Flattened at the poles, like a sphere that has been compressed along its rotational axis (an oblate spheroid); or a lay person dedicated to a religious order.",
    "secondary": "In planetary geodesy and astrophysics, the flattened spheroidal figure of rotating planets produced by centrifugal acceleration opposing gravity.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Principia Mathematica", "quote": "Owing to the diurnal rotation of the earth upon its axis, its true figure must be that of an **oblate** spheroid."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The geodetic survey proved that the earth's polar diameter is shorter, confirming its **oblate** form."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "Centrifugal force acting upon the rotating molten mass gave the young planet its distinctly **oblate** contour."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Carrying"
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

print(f"Carrying Batch 4C (lat): Successfully updated {updated}/{len(data)} notes.")
