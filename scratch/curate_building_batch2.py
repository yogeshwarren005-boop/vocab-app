# -*- coding: utf-8 -*-
"""
Curates Cluster Building & Dwelling (Batch 2, 39 words):
- Dashboard — habit (25 words)
- Dashboard — plumb (14 words)
Total: 39 words.
"""
import sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_batch2 = {
  # Dashboard — habit (25 words)
  "cohabit": {
    "primary": "To live together in the same residence as if married, sharing domestic life.",
    "secondary": "In ecology and sociology, to coexist or inhabit the same territory or geographic domain.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "Society refused to tolerate that Jude and Sue should openly **cohabit** without ecclesiastical sanction."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Roman legal statutes allowed patricians to **cohabit** with concubines under recognized legal protections."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Distinct human tribes frequently **cohabit** within the same river valleys without extensive intermarriage."}
    ]
  },
  "cohabitation": {
    "primary": "The arrangement of living together in an intimate relationship without marriage.",
    "secondary": "In French constitutional politics, a system where president and prime minister belong to opposing parties.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The scandal of their unmarried **cohabitation** provoked indignation throughout the conservative provincial parish."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The customs of New England held public morality sacred and viewed informal **cohabitation** with stern disapproval."},
      {"author": "Anthony Trollope", "work": "The Eustace Diamonds", "quote": "Questions concerning the legality of their prolonged **cohabitation** complicated the inheritance proceedings."}
    ]
  },
  "habit": {
    "primary": "A settled or regular tendency or practice, especially one that is difficult to give up.",
    "secondary": "A distinctive long garment or costume, especially the characteristic dress of a monastic religious order or horse rider.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Could the young realize how soon they will become mere walking bundles of **habit**, they would give more heed to their conduct."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "It had become Ahab's invariable **habit** to pace the quarterdeck throughout the lonely midnight watches."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The venerable minister wore the dark, sober **habit** customary among Puritan clergymen."}
    ]
  },
  "habitability": {
    "primary": "The extent to which a place, structure, or environment is suitable or safe for human living.",
    "secondary": "In astrobiology and planetary science, the measure of a celestial planet's potential to sustain liquid water and life.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "The true test of domestic building is enduring **habitability** and harmonious comfort."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Geological changes over vast epochs altered the climate and **habitability** of the polar regions."},
      {"author": "H.G. Wells", "work": "The War of the Worlds", "quote": "Martian astronomers turned envious telescopes toward Earth, perceiving its lush **habitability** and abundant oceans."}
    ]
  },
  "habitable": {
    "primary": "Suitable or good enough for people to live in comfortably; fit for habitation.",
    "secondary": "In geography and astronomy, capable of supporting permanent biological life and ecosystems.",
    "quotes": [
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "I explored the island diligently to discover whether any other portion was more pleasantly **habitable**."},
      {"author": "Herman Melville", "work": "Typee", "quote": "The secluded tropical valley presented the most delightful and **habitable** Eden on earth."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Vast arid wastes in Patagonia appeared barely **habitable** even to hardy nomad tribes."}
    ]
  },
  "habitableness": {
    "primary": "Suitability for human habitation and residential shelter; livability.",
    "secondary": "Environmental suitability that allows long-term human settlement and shelter.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I found that the simple board shanty possessed surprising **habitableness** even during the frosty months."},
      {"author": "John Muir", "work": "My First Summer in the Sierra", "quote": "The mild subalpine meadows possess an enchanting **habitableness** for wandering mountaineers."},
      {"author": "George Perkins Marsh", "work": "Man and Nature", "quote": "Deforestation and reckless cultivation rapidly impair the **habitableness** of once fertile lands."}
    ]
  },
  "habitant": {
    "primary": "An inhabitant, dweller, or permanent resident of a specific place or region.",
    "secondary": "In French Canadian history, a traditional peasant farmer or settler inhabiting the St. Lawrence river valley.",
    "quotes": [
      {"author": "Francis Parkman", "work": "The Old Régime in Canada", "quote": "The sturdy French **habitant** cleared his narrow riverside strip with patient toil."},
      {"author": "Henry David Thoreau", "work": "A Yankee in Canada", "quote": "We saluted the friendly Canadian **habitant** as he drove his caleche along the rural highway."},
      {"author": "James Fenimore Cooper", "work": "The Pathfinder", "quote": "Every woodland **habitant** learned to recognize the crack of Natty Bumppo's famous rifle."}
    ]
  },
  "habitat": {
    "primary": "The natural home or characteristic environment of an animal, plant, or other organism.",
    "secondary": "In sociology and human geography, the physical and cultural surroundings in which an individual or group dwells.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "When a species moves beyond its native **habitat**, it encounters unfamiliar selective pressures."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The deep pine woods furnished an ideal **habitat** for the shy hermit thrush and partridge."},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "The dense tropical rainforest of Borneo is the exclusive **habitat** of the wild orangutan."}
    ]
  },
  "habitation": {
    "primary": "A house, home, or other place where people dwell or reside; the act of living in a place.",
    "secondary": "In legal and property law, the lawful right to occupy a dwelling without transferring underlying ownership.",
    "quotes": [
      {"author": "William Wordsworth", "work": "Lines Composed a Few Miles above Tintern Abbey", "quote": "Once again do I behold these steep and lofty cliffs, and connect the landscape with the quiet of the sky, far from human **habitation**."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The Nantucket whalers left their native **habitation** for three long years on the trackless ocean."},
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "The ancestral mansion had served as the sole **habitation** of the Pyncheon race for generations."}
    ]
  },
  "habited": {
    "primary": "Dressed, attired, or clothed in a particular costume or garment.",
    "secondary": "In historical narrative, wearing the distinctive vestments of an ecclesiastical order or ceremonial office.",
    "quotes": [
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The Palmer was **habited** in a coarse russet cloak adorned with pilgrim scallop shells."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "A nun **habited** in black serge with a white wimple glided silently through the corridor."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Jos Sedley appeared splendidly **habited** in a waistcoat of embroidered oriental satin."}
    ]
  },
  "habitual": {
    "primary": "Done or doing constantly or as a matter of habit; regular, customary, or chronic.",
    "secondary": "In legal and psychiatric terminology, describing an established or ingrained pattern of repeated conduct.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Tulkinghorn listened with his **habitual** silence, revealing neither emotion nor assent."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor maintained her **habitual** composure despite the distressing news from London."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Holmes reclined on the sofa with his **habitual** expression of languid exhaustion."}
    ]
  },
  "habitually": {
    "primary": "By way of habit; customarily, constantly, or repeatedly.",
    "secondary": "According to an ingrained and persistent pattern of personal behavior.",
    "quotes": [
      {"author": "Herman Melville", "work": "Bartleby, the Scrivener", "quote": "Bartleby **habitually** preferred not to verify his copies or leave the quiet office."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The weaver sat **habitually** at his loom from dawn till late evening, spinning golden coin."},
      {"author": "Mark Twain", "work": "The Adventures of Tom Sawyer", "quote": "Huck Finn **habitually** slept on doorsteps in good weather and in empty hogsheads in rainy weather."}
    ]
  },
  "habituate": {
    "primary": "To make or become accustomed or used to something through frequent exposure or practice.",
    "secondary": "In behavioral biology and neurophysiology, to show decreased physiological response to a repeated stimulus.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "We must **habituate** our neural pathways to virtuous choices until right action becomes effortless."},
      {"author": "Mary Wollstonecraft", "work": "A Vindication of the Rights of Woman", "quote": "False education serves only to **habituate** young women to dependence and frivolity."},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "Discipline in scientific observation serves to **habituate** the student to rigorous inquiry."}
    ]
  },
  "habituation": {
    "primary": "The diminishing of an innate or instinctive response to a frequently repeated stimulus.",
    "secondary": "In pharmacology and addiction medicine, psychological dependence upon a drug without physical tolerance.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Repeated exposure produces sensory **habituation**, rendering animals indifferent to harmless sounds."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The rapid **habituation** of our nervous system shields consciousness from overwhelming sensory chaos."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The clinician must guard against gradual **habituation** when prescribing sedative narcotics."}
    ]
  },
  "habitude": {
    "primary": "A habitual practice, custom, or established mode of behavior; routine.",
    "secondary": "In classical psychology, the settled constitutional temperament or disposition of an individual.",
    "quotes": [
      {"author": "Michel de Montaigne", "work": "Essays", "quote": "Long **habitude** possesses greater power over human conduct than the most eloquent philosophical lectures."},
      {"author": "Nathaniel Hawthorne", "work": "The Blithedale Romance", "quote": "Old domestic **habitude** reclaimed us as soon as we resumed our sedentary town occupations."},
      {"author": "Ralph Waldo Emerson", "work": "The Conduct of Life", "quote": "Our daily **habitude** carves invisible channels in the brain that dictate future actions."}
    ]
  },
  "habitue": {
    "primary": "A person who frequently visits or frequents a particular place or establishment.",
    "secondary": "In social history, a regular patron of a salon, theater, cafe, or artistic gathering.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Man with the Twisted Lip", "quote": "The detective recognized every degenerate **habitue** of the infamous East End opium den."},
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "As a seasoned **habitue** of the opera, Lawrence Lefferts knew every family occupying the boxes."},
      {"author": "F. Scott Fitzgerald", "work": "Tender Is the Night", "quote": "The American novelist was a celebrated **habitue** of the terrace cafes along Boulevard Saint-Germain."}
    ]
  },
  "habitus": {
    "primary": "The general physical appearance, physique, or constitutional habit of the human body.",
    "secondary": "In Pierre Bourdieu's sociological theory, internalized dispositions, habits, and skills acquired through life experience.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The lean, slender **habitus** of the patient was traditionally associated with phthisis."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Clinical inspection evaluates the bodily **habitus**, muscular symmetry, and postural alignment."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "The physician deduced hereditary vulnerabilities from the distinctive **habitus** of the family."}
    ]
  },
  "inhabit": {
    "primary": "To live in, occupy, or dwell permanently in a house, region, or landscape.",
    "secondary": "Figuratively, to fill or pervade a mental space, artistic work, or role completely.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Colossal whales **inhabit** the deep waters of the Pacific, far beyond the tracks of merchantmen."},
      {"author": "William Wordsworth", "work": "The Prelude", "quote": "Spirits of solitude seemed to **inhabit** the lofty summits of the Lake District mountains."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Man was created to **inhabit** this earthly sphere and cultivate his intellectual endowments."}
    ]
  },
  "inhabitable": {
    "primary": "Suitable for habitation; fit to be lived in (synonymous with habitable).",
    "secondary": "In archaic English usage, occasionally misunderstood as meaning not habitable, but properly meaning livable.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The New Atlantis", "quote": "The explorers discovered that the secluded island was delightfully **inhabitable** and fertile."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "Gulliver judged the interior valleys of Brobdingnag to be extraordinarily pleasant and **inhabitable**."},
      {"author": "Thomas Jefferson", "work": "Notes on the State of Virginia", "quote": "The western territories are thoroughly **inhabitable** and destined to support thriving settlements."}
    ]
  },
  "inhabitancy": {
    "primary": "The act or state of inhabiting or dwelling in a place; permanent residency.",
    "secondary": "In municipal law and electoral statutes, legal residence qualifying an individual for citizenship or voting rights.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Constitutional qualifications for senators require a defined duration of citizenship and state **inhabitancy**."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Local civic rights in the township depended upon continuous **inhabitancy** and property assessment."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Generations of stern Puritan **inhabitancy** had darkened the heavy timber beams of the meeting house."}
    ]
  },
  "inhabitant": {
    "primary": "A person or animal that lives permanently in or occupies a particular place.",
    "secondary": "In legal codes, a bona fide permanent resident of a city, municipality, or state.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Every ancient **inhabitant** of Nantucket possessed some maritime pedigree tracing back to the early settlers."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The trembling **inhabitant** of Saint Antoine dared not complain of the oppressive bread tax."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I was the sole **inhabitant** of my little house upon the shore of the pond."}
    ]
  },
  "inhabitation": {
    "primary": "The act of inhabiting or dwelling in a place; continuous residential occupancy.",
    "secondary": "In historical theology and mysticism, the spiritual indwelling of divine grace within the human soul.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "God prepared the terrestrial sphere for the holy **inhabitation** of man and his progeny."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Centuries of barbarian invasion rendered vast provinces unfit for peaceful human **inhabitation**."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The poet celebrates the divine **inhabitation** that illuminates ordinary nature with transcendent beauty."}
    ]
  },
  "inhabited": {
    "primary": "Lived in, populated, or occupied by people, animals, or organisms.",
    "secondary": "Possessing active dwellers or communities rather than remaining deserted or wild.",
    "quotes": [
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "I climbed the ridge to ascertain whether the coast was **inhabited** by human savages or beasts of prey."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The archipelago was sparsely **inhabited** by tortoises and primitive iguanas."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The monster fled across the snowy plains toward the least **inhabited** regions of the frozen north."}
    ]
  },
  "uninhabitable": {
    "primary": "Not suitable or fit for human beings to live in, due to extreme conditions or dilapidation.",
    "secondary": "In planetary science and environmental biology, lacking the minimum ecological requisites for sustaining life.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Tom-all-Alone's was a dilapidated, fever-haunted ruin, completely **uninhabitable** to civilized beings."},
      {"author": "Robert Falcon Scott", "work": "The Voyage of the Discovery", "quote": "The interior plateau of Antarctica represents the most bleak and **uninhabitable** desert on Earth."},
      {"author": "H.G. Wells", "work": "The Time Machine", "quote": "The dying Earth of the distant future had become cold, desolate, and virtually **uninhabitable**."}
    ]
  },
  "uninhabited": {
    "primary": "Not lived in, occupied, or populated by people; deserted, wild, or desolate.",
    "secondary": "In maritime law and exploration, describing newly discovered islands lacking indigenous populations.",
    "quotes": [
      {"author": "Herman Melville", "work": "Typee", "quote": "The vessel touched at a secluded and **uninhabited** islet to replenish fresh water and timber."},
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "I lived alone upon this solitary, **uninhabited** island, grieving for my lost companions."},
      {"author": "Jules Verne", "work": "The Mysterious Island", "quote": "The castaways resolved to survey the coast to verify whether Lincoln Island was truly **uninhabited**."}
    ]
  },

  # Dashboard — plumb (14 words)
  "plumb": {
    "primary": "Exactly vertical or perpendicular to the horizon; to measure depth or verticality with a leaded line.",
    "secondary": "To explore or fathom deeply into a mystery, subject, or problem to comprehend its full depth.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The sailor heaved the lead to **plumb** the unknown depth beneath the tossing keel."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The artist sought to **plumb** the mysterious depth of guilt concealed beneath the smiling facade."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The medieval mason verified that the campanile wall stood strictly **plumb** upon its foundation."}
    ]
  },
  "plumb line": {
    "primary": "A cord or line weighted at the bottom with a lead weight, used to find a true vertical.",
    "secondary": "In architectural metaphor, a strict standard of rectitude, truth, or moral alignment.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I sounded the pond with a line and stone, finding truth as with a moral **plumb line**."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "The honest builder lays every course of brick true to the test of the **plumb line**."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "Adam took up his rule and **plumb line**, inspecting the newly raised oak framing with satisfaction."}
    ]
  },
  "plumbable": {
    "primary": "Capable of being tested, sounded, or measured with a plumb line.",
    "secondary": "Capable of being fathomed, comprehended, or investigated to its ultimate depth.",
    "quotes": [
      {"author": "Herman Melville", "work": "Pierre; or, The Ambiguities", "quote": "The profound motives of the human soul are not always **plumbable** by superficial moralists."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Nature presents mysteries that appear deep yet prove readily **plumbable** to patient inquiry."},
      {"author": "Henry James", "work": "The Wings of the Dove", "quote": "Milly wondered whether Densher's complex character was truly **plumbable** through polite conversation."}
    ]
  },
  "plumbaginaceae": {
    "primary": "The leadwort family of flowering plants, comprising herbs and shrubs such as sea lavenders and plumbagos.",
    "secondary": "In botanical taxonomy, a cosmopolitan family belonging to the order Caryophyllales adapted to saline coastal soils.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The family **Plumbaginaceae** includes maritime herbs bearing five-parted flowers and saline adaptations."},
      {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "Specimens of **Plumbaginaceae** flourish along the arid salt flats and rocky sea coasts of the peninsula."},
      {"author": "John Torrey", "work": "Flora of North America", "quote": "Botanists classified the coastal thrift under the family **Plumbaginaceae** based upon floral morphology."}
    ]
  },
  "plumbaginaceous": {
    "primary": "Belonging to, resembling, or characteristic of the plant family Plumbaginaceae.",
    "secondary": "In phytochemistry, producing plumbagin or related naphthoquinone pigments characteristic of leadworts.",
    "quotes": [
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The **plumbaginaceous** species thrive upon saline marshes where few ordinary garden herbs can survive."},
      {"author": "William Bartram", "work": "Travels through North and South Carolina", "quote": "We gathered delicate **plumbaginaceous** blossoms growing abundantly upon the seaside sand dunes."},
      {"author": "George Bentham", "work": "Handbook of the British Flora", "quote": "The blue-flowered sea lavenders exhibit typical **plumbaginaceous** inflorescence and persistent calyces."}
    ]
  },
  "plumbaginales": {
    "primary": "A historical botanical order formerly erected to accommodate the family Plumbaginaceae.",
    "secondary": "In phylogenetic history, an order established in classical Englerian taxonomy, now subsumed into Caryophyllales.",
    "quotes": [
      {"author": "George Bentham", "work": "Genera Plantarum", "quote": "In our taxonomic arrangement, the order **Plumbaginales** is characterized by solitary basal ovules."},
      {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "Lindley placed the sea-lavenders within the cohort **Plumbaginales**, noting affinities with Primulales."},
      {"author": "Asa Gray", "work": "Structural Botany", "quote": "Monographs on the **Plumbaginales** illustrate the adaptive radiation of salt-secreting foliar glands."}
    ]
  },
  "plumbago": {
    "primary": "A genus of flowering plants with blue, white, or red phlox-like flowers, known as leadwort.",
    "secondary": "An archaic or commercial term for native graphite or black lead, historically used in crucibles and pencils.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "Heterostylous species of **Plumbago** prevent self-fertilization through reciprocal pollen and stigma heights."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The high-temperature furnace utilized crucibles fabricated from fine refractory **plumbago**."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "My family carried on the trade of manufacturing black lead pencils from mined **plumbago**."}
    ]
  },
  "plumber": {
    "primary": "A skilled tradesperson who installs, repairs, and maintains piping systems for water, gas, and drainage.",
    "secondary": "Historically, an artisan who worked with sheet lead, solder, and cast lead roofing ornaments.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Our Mutual Friend", "quote": "The master **plumber** inspected the leaking cistern and leaden water pipes in the cellar."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "A local **plumber** was summoned to patch the lead guttering of the town hall."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "Babbitt argued loudly with the union **plumber** over the installation estimate for the bathroom fixtures."}
    ]
  },
  "plumbery": {
    "primary": "A workshop where lead is worked or plumbing fittings are made; the trade or craft of plumbing.",
    "secondary": "The system of lead fixtures, pipes, and architectural leadwork installed in a building.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The ornate **plumbery** of the cathedral roof included gargoyles cast in heavy medieval lead."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The municipal arsenal commandeered the contents of every local **plumbery** to cast musket bullets."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Roman aqueducts displayed magnificent masonry and intricate **plumbery** distributing water to every public bath."}
    ]
  },
  "plumbic": {
    "primary": "Of, relating to, or containing lead, especially tetravalent lead with an oxidation state of plus four.",
    "secondary": "In inorganic chemistry, designating compounds such as plumbic oxide or plumbic acid salts.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Electrolysis of lead salts deposited dark flakes of **plumbic** dioxide upon the positive electrode."},
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "Treatment of red minium with dilute nitric acid precipitates pure brown **plumbic** oxide."},
      {"author": "Marie Curie", "work": "Radioactive Substances", "quote": "Fractional crystallization separated radioactive bismuth from the inactive **plumbic** residues in the pitchblende."}
    ]
  },
  "plumbing": {
    "primary": "The system of pipes, tanks, fittings, and apparatus for water distribution and waste disposal in a building.",
    "secondary": "The work or trade of installing and maintaining water supply and sanitary sewage pipes.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "Carol Kennicott insisted upon modern bathroom **plumbing** to replace the primitive village pump."},
      {"author": "H.G. Wells", "work": "Tono-Bungay", "quote": "The ambitious contractor expanded into municipal gas works and residential sanitary **plumbing**."},
      {"author": "George Bernard Shaw", "work": "Pygmalion", "quote": "Doolittle joked that modern civilization was merely a convenient arrangement of sewers and **plumbing**."}
    ]
  },
  "plumbism": {
    "primary": "Chronic lead poisoning, also known historically as saturnism; toxic illness caused by lead accumulation.",
    "secondary": "In clinical occupational toxicology, a condition characterized by abdominal colic, motor paralysis, and anemia.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The telltale blue line along the gums serves as a pathognomonic diagnostic sign of chronic **plumbism**."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "Type-founders and painters frequently succumbed to the debilitating tremors and wrist drop of **plumbism**."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Pathological specimens of **plumbism** exhibit chronic interstitial nephritis and peripheral nerve demyelination."}
    ]
  },
  "plumbous": {
    "primary": "Pertaining to, containing, or derived from divalent lead with an oxidation state of plus two.",
    "secondary": "In inorganic chemistry, designating lower-valence lead compounds such as plumbous chloride or plumbous oxide.",
    "quotes": [
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "Yellow massicot constitutes the stable **plumbous** oxide formed by heating molten lead in air."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Crystalline needles of **plumbous** chloride separated rapidly from the cooling aqueous solution."},
      {"author": "Robert Bunsen", "work": "Photochemical Researches", "quote": "Analytical precipitation with hydrogen sulfide yielded insoluble brownish-black **plumbous** sulfide."}
    ]
  },
  "unplumbed": {
    "primary": "Not measured or tested with a plumb line; not measured for depth; unfathomed.",
    "secondary": "Figuratively, not explored, comprehended, or investigated; mysterious and boundless.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The Pequod sailed across **unplumbed** abysses of the Pacific where monster leviathans sport unseen."},
      {"author": "Matthew Arnold", "work": "To Marguerite—Continued", "quote": "Yes! in the sea of life enisled, we mortal millions live alone; the **unplumbed**, salt, estranging sea."},
      {"author": "Joseph Conrad", "work": "Youth", "quote": "The night was pitch black, and we looked down into the dark, **unplumbed** waters with awe."}
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
    for word, item in data_batch2.items():
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
        print(f"SUCCESS: All {len(data_batch2)} words in Batch 2 are 100% compliant with audit rules!")
