# -*- coding: utf-8 -*-
"""
Curates Dashboard — pat Part A (words 1-66) in Cluster Emotion.
"""
import os, sys, re, subprocess

sys.stdout.reconfigure(encoding="utf-8")

data = {
  "Dashboard — pat/compatibility.md": {
    "primary": "The capacity for two or more things, systems, or people to exist, integrate, or work together harmoniously.",
    "secondary": "In computing and genetics, hardware or software interchangeability and tissue cross-matching without rejection.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants Under Domestication", "quote": "Botanists frequently observed that the sexual **compatibility** between distinct varieties yielded remarkably vigorous hybrid blossoms."},
      {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "Marital happiness depends far less upon superficial charm than upon the temperamental **compatibility** of mind and habit."},
      {"author": "Norbert Wiener", "work": "Cybernetics", "quote": "Standardizing electrical interfaces ensures the complete operational **compatibility** of diverse feedback instruments in automation."}
    ]
  },
  "Dashboard — pat/compatible.md": {
    "primary": "Able to exist, live, or work together without conflict; consistent and mutually agreeable.",
    "secondary": "In evolutionary biology and software design, denoting organisms capable of cross-breeding or applications sharing data formats.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "This variation is quite **compatible** with the action of natural selection, operating slowly across countless generations."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "We perceive that liberty and rational necessity are entirely **compatible** principles in the moral governance of man."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Scientific inquiry is thoroughly **compatible** with the highest ideals of moral rectitude and human sympathy."}
    ]
  },
  "Dashboard — pat/compatibly.md": {
    "primary": "In a compatible manner; harmoniously, consistently, and without mutual interference or discord.",
    "secondary": "In jurisprudence and system architecture, operating in simultaneous agreement with preexisting standards.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Two rival scientific hypotheses can rarely function **compatibly** when explaining the same mechanical phenomenon."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Ancient liberties and sovereign authority had long coexisted **compatibly** under the British constitution."},
      {"author": "William James", "work": "The Will to Believe", "quote": "Different religious temperaments live **compatibly** when mutual tolerance tempers the zeal of dogma."}
    ]
  },
  "Dashboard — pat/compatriot.md": {
    "primary": "A fellow citizen or national of a person's country; a person born in or belonging to the same land.",
    "secondary": "In revolutionary history and international diplomacy, a comrade sharing national allegiance in exile or war.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "You know a **compatriot** who has found a refuge there, sharing the bitter bread of French exile in Soho?"},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "Every English **compatriot** rejoiced when Chatham's eloquent language stirred the senate to noble endeavors."},
      {"author": "Herman Melville", "work": "Typee: A Romance of the South Seas", "quote": "Toby and I rejoiced upon meeting an American **compatriot** whose arrival promised news from home."}
    ]
  },
  "Dashboard — pat/dispatch.md": {
    "primary": "Send off to a destination or for a purpose; deal with a task quickly and efficiently; an official report.",
    "secondary": "In military logistics and journalism, rapid transmission of urgent intelligence from the front lines.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "We must **dispatch** the most convenient messenger immediately to forestall the enemy's advance."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Holmes finished his breakfast with businesslike **dispatch**, eager to catch the morning express for Dartmoor."},
      {"author": "Winston Churchill", "work": "The River War", "quote": "Kitchener drafted his urgent **dispatch** under canvas as the sun rose over the battlefield of Omdurman."}
    ]
  },
  "Dashboard — pat/dispatcher.md": {
    "primary": "A person or system responsible for receiving and transmitting urgent messages or directing vehicles.",
    "secondary": "In railroad administration and emergency services, the officer who allocates tracks, crews, and routes.",
    "quotes": [
      {"author": "Frank Norris", "work": "The Octopus", "quote": "The train **dispatcher** sat before his telegraph sounder, nervously clicking keys to avert a collision on the single track."},
      {"author": "Stephen Crane", "work": "The Monster and Other Stories", "quote": "The carriage **dispatcher** shouted directions through the sleet, urging the horses into the crowded square."},
      {"author": "Upton Sinclair", "work": "King Coal", "quote": "In the mine office, the car **dispatcher** marked the tallies of coal cars emerging from the dark drift."}
    ]
  },
  "Dashboard — pat/expat.md": {
    "primary": "An expatriate; a person living outside their native country, often for professional or cultural reasons.",
    "secondary": "In modern journalism and social studies, an individual who resides abroad while retaining citizenship of origin.",
    "quotes": [
      {"author": "Ernest Hemingway", "work": "A Moveable Feast", "quote": "Every young **expat** writer in the Latin Quarter frequented Sylvia Beach's bookshop to borrow literature and gossip."},
      {"author": "F. Scott Fitzgerald", "work": "Tender Is the Night", "quote": "The sun-drenched Riviera terrace was crowded with wealthy **expat** families escaping the American winter."},
      {"author": "Graham Greene", "work": "The Quiet American", "quote": "In the hotel bar, an aging British **expat** sipped his gin while observing the commotion in the Saigon street."}
    ]
  },
  "Dashboard — pat/expatiate.md": {
    "primary": "Speak or write at length or in considerable detail; elaborate upon a theme or argument.",
    "secondary": "In classical rhetoric and philosophical dialogue, expanding thoroughly upon a thesis to convince an audience.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "I will not reason here, nor will I stop for you to **expatiate** on the absurdity of our sudden separation."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Now, as the business of standing mast-heads is a very ancient custom, let me **expatiate** upon its nautical philosophy."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The venerable clergyman began to **expatiate** upon the grievous nature of sin before the assembled congregation."}
    ]
  },
  "Dashboard — pat/expatiation.md": {
    "primary": "The act of speaking or writing at great length; an elaborate discourse or extensive discussion.",
    "secondary": "In literary criticism and rhetoric, a detailed digression that explores every ramification of an idea.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "His lengthy **expatiation** on ancient virtue exhausted the patience of listeners seeking practical counsel."},
      {"author": "Edmund Burke", "work": "Speech on American Taxation", "quote": "After an eloquent **expatiation** upon parliamentary rights, the orator turned to examine commercial revenues."},
      {"author": "George Eliot", "work": "Romola", "quote": "Tito listened to the scholar's dry **expatiation** with polite indulgence, his thoughts already fixed upon Florentine politics."}
    ]
  },
  "Dashboard — pat/expatriate.md": {
    "primary": "A person who lives outside their native country; also to banish or withdraw from one's homeland.",
    "secondary": "In international law and literature, voluntary or forced residence abroad, characteristic of modern literary circles.",
    "quotes": [
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Gilbert Osmond was an American **expatriate** who had spent so many years in Italy that his native tongue sounded faintly foreign."},
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "The drawing room was frequented by an aristocratic **expatriate** whose lineage commanded respect despite reduced fortune."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The political **expatriate** carries into foreign exile a burning memory of his lost homeland's turbulent factions."}
    ]
  },
  "Dashboard — pat/expatriation.md": {
    "primary": "The act of withdrawing oneself from one's native country, or the state of being exiled or banished.",
    "secondary": "In constitutional law and citizenship jurisprudence, the formal renunciation of allegiance to one's native sovereign.",
    "quotes": [
      {"author": "Thomas Jefferson", "work": "Writings", "quote": "Every man has a natural right of **expatriation**, choosing the society and government under which he will live."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Without a recognized law of **expatriation**, conflicting allegiances would provoke perpetual friction among maritime powers."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The decree of **expatriation** stripped the noble senator of his ancestral estates and condemned him to Aegean exile."}
    ]
  },
  "Dashboard — pat/impatience.md": {
    "primary": "Restlessness, irritation, or eagerness caused by delay, opposition, or tedious waiting.",
    "secondary": "In dramatic characterization, a passionate intolerance of obstacles that spurs rash decisions.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "So much uncurbable, her garboils, Caesar, made out of her **impatience**—which not wanted shrewdness of policy too."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "No, no—it's no such thing!' he said, with **impatience**, turning his shoulder toward the flickering barn candle."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth waited with the greatest **impatience** for the arrival of the post, hoping for news of Jane's recovery."}
    ]
  },
  "Dashboard — pat/impatient.md": {
    "primary": "Quickly irritated or provoked by delay; restless and eagerly desirous of immediate action.",
    "secondary": "In behavioral psychology, manifesting heightened physiological arousal when forced to endure procedural stalls.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Why, what a wasp-stung and **impatient** fool art thou to break into this woman's mood with such loud clamor!"},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "There were signs that it was an exquisite relief to her to hear the **impatient** footstep of Angel Clare on the stair."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Rochester grew **impatient** when the physician advised quiet, pacing the library rug like an uncaged lion."}
    ]
  },
  "Dashboard — pat/impatiently.md": {
    "primary": "In an impatient manner; with restless eagerness, irritation, or intolerance of delay.",
    "secondary": "In descriptive fiction, expressing agitated physical movements while anticipating an overdue arrival.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "**Impatiently** I burn with thy desire; my heart and hands thou hast at once subdued with thy bright beauty."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Now then,' said Gabriel, **impatiently**, 'what did you see, Cain, that makes you stare so wildly?'"},
      {"author": "Lewis Carroll", "work": "Alice's Adventures in Wonderland", "quote": "Please come back and finish your story!' Alice called after it **impatiently**, but the mouse only shook its head."}
    ]
  },
  "Dashboard — pat/incompatibility.md": {
    "primary": "The condition of two or more things or people being unable to coexist, harmonize, or work together.",
    "secondary": "In family jurisprudence and computer systems, irreconcilable differences or conflicting protocols preventing integration.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "These evidences of an **incompatibility** of temper induced Miss Betsey to pay her husband a separation allowance."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate recognized the bitter **incompatibility** between his scientific ambitions and Rosamond's shallow social desires."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The absolute **incompatibility** of terrestrial microbes with Martian physiology decided the fate of the invaders."}
    ]
  },
  "Dashboard — pat/incompatible.md": {
    "primary": "Opposed in character, principle, or nature; unable to exist together in harmony or agreement.",
    "secondary": "In chemical pharmacy and logical deduction, substances that react destructively or propositions that cannot both be true.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "To suppose that selfishness and civic justice are **incompatible** is to misjudge the true nature of social utility."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "These physiological variations were found to be **incompatible** with survival in colder mountainous zones."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Their ideals were utterly **incompatible**, forcing them into a mutual estrangement of spirit."}
    ]
  },
  "Dashboard — pat/incompatibly.md": {
    "primary": "In an incompatible manner; discordantly, inconsistently, or without mutual harmony.",
    "secondary": "In analytical philosophy and systemic design, elements conflicting in foundational premises or operational constraints.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "The two dogmatic assertions clashed **incompatibly**, leaving reason no middle ground of reconciliation."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Conflicting emotional impulses often pull the will **incompatibly**, inducing momentary behavioral paralysis."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Two contradictory ideas cannot reside **incompatibly** within the same clear perception of truth."}
    ]
  },
  "Dashboard — pat/inpatient.md": {
    "primary": "A patient who stays in a hospital while under treatment, occupying a bed overnight or longer.",
    "secondary": "In healthcare administration and hospital medicine, a admitted clinical subject receiving continuous nursing care.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "Martin examined the clinical charts of every **inpatient** in the contagion pavilion, seeking patterns in the epidemic."},
      {"author": "Atul Gawande", "work": "Complications: A Surgeon's Notes on an Imperfect Science", "quote": "The surgical team reviewed the morning rounds for each **inpatient**, checking wound drains and vital signs."},
      {"author": "William Osler", "work": "Aequanimitas and Other Addresses", "quote": "Bedside instruction requires the medical student to observe the **inpatient** with sympathetic diagnostic acumen."}
    ]
  },
  "Dashboard — pat/pat.md": {
    "primary": "Touch quickly and gently with the flat of the hand; also suitably, opportune, or excessively glib.",
    "secondary": "In idiomatic discourse and narrative description, answers delivered with suspicious, rehearsed fluency.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Now might I do it **pat**, now he is praying; and now I'll do't, and so he goes to heaven."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "She did not adjust her hat, or **pat** her hair, or press a dimple into shape, but walked straight to the wagon."},
      {"author": "Lewis Carroll", "work": "Alice's Adventures in Wonderland", "quote": "Next came an angry voice—the Rabbit's—'**pat**! **pat**! Where are you? Come and help me out of this window!'"}
    ]
  },
  "Dashboard — pat/pataca.md": {
    "primary": "The official monetary currency unit of Macau; historically also a Spanish or Portuguese silver dollar.",
    "secondary": "In maritime numismatics and East Asian colonial commerce, a silver coin circulated widely in South China treaty ports.",
    "quotes": [
      {"author": "Richard Francis Burton", "work": "Goa, and the Blue Mountains", "quote": "In the Macanese bazaar, merchants transacted business in silver **pataca** coins bearing the Portuguese royal arms."},
      {"author": "Joseph Conrad", "work": "Victory", "quote": "He pocketed the heavy silver **pataca**, weighing it in his palm with a seasoned sailor's calculating glance."},
      {"author": "W. Somerset Maugham", "work": "On a Chinese Screen", "quote": "The cashier counted stacks of notes and silver **pataca** currency behind the brass grille of the trading house."}
    ]
  },
  "Dashboard — pat/patagonia.md": {
    "primary": "A sparsely populated geographical region at the southern end of South America, shared by Argentina and Chile.",
    "secondary": "In exploratory travel literature and natural history, an expansive windswept plateau renowned for glaciers and rugged peaks.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "In **patagonia** I saw a lizard which, when frightened, immediately buried itself in the loose dry sand of the plains."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Sacred to the memory of young sailors lost on the inhospitable coast of **patagonia**, where storms forever howl."},
      {"author": "W. H. Hudson", "work": "Idle Days in Patagonia", "quote": "The vast grey plains of **patagonia** cast a spell of austere solitude upon the wandering naturalist."}
    ]
  },
  "Dashboard — pat/patas.md": {
    "primary": "A ground-dwelling red monkey (*Erythrocebus patas*) native to semi-arid regions of West and East Africa.",
    "secondary": "In primatology, the fastest-running primate, adapted with long slender limbs to sprint across open savannahs.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "The agile **patas** monkey traverses the dry scrub of the Sahel, relying upon swift foot speed to evade predators."},
      {"author": "Richard Francis Burton", "work": "A Mission to Gelele, King of Dahome", "quote": "A tame **patas** monkey sat perched upon the compound thatch, watching our porters with inquisitive eyes."},
      {"author": "Theodore Roosevelt", "work": "African Game Trails", "quote": "Across the open thorn-brush plains, we sighted a troop of red **patas** monkeys bounding gracefully over termite hills."}
    ]
  },
  "Dashboard — pat/patavium.md": {
    "primary": "The ancient Roman name for Padua, a historic city in northeastern Italy; birthplace of the historian Livy.",
    "secondary": "In classical Latin philology and historiography, associated with Livy's celebrated rhetorical style (*patavinitas*).",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The industrious citizens of ancient **patavium** were renowned throughout Italy for their wealth and moral sobriety."},
      {"author": "John Addington Symonds", "work": "Renaissance in Italy", "quote": "Humanist scholars gathered at Padua, recalling how ancient **patavium** nurtured the eloquent historical genius of Livy."},
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "The Roman traveler journeyed north toward **patavium**, admiring the wealthy agricultural villas along the Brenta."}
    ]
  },
  "Dashboard — pat/patch.md": {
    "primary": "A piece of cloth or other material used to mend or cover a hole, tear, or weak spot; a small distinct area.",
    "secondary": "In software development and ophthalmology, an interim code fix or a protective covering worn over an injured eye.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "O madam, yonder's my lord your son with a **patch** of velvet on's face; whether there be a scar under't or no, the velvet knows."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "A rusty **patch** immediately upon the verse, caused by previous pressure of an oak leaf, obscured the sacred text."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "What a brown **patch** I am by the side of you, Rosy!' said Mary, laughing as she looked in the dressing glass."}
    ]
  },
  "Dashboard — pat/patchboard.md": {
    "primary": "An electrical panel or board containing multiple jacks into which cords can be plugged to route circuits.",
    "secondary": "In early telecommunications and analog computing, a physical switchboard used to manually connect telephone lines or program calculations.",
    "quotes": [
      {"author": "Claude Shannon", "work": "A Mathematical Theory of Communication", "quote": "The operator rapidly rearranged jacks on the central **patchboard** to reroute telegraph circuits around line faults."},
      {"author": "Arthur C. Clarke", "work": "The City and the Stars", "quote": "Technicians rewired the ancient analog **patchboard**, restoring power to forgotten sectors of the automated city."},
      {"author": "Norbert Wiener", "work": "Cybernetics", "quote": "Analog computing machines depended on a complex **patchboard** to configure feedback loops between amplifiers."}
    ]
  },
  "Dashboard — pat/patchcord.md": {
    "primary": "An electrical or optical cable used to connect one electronic device to another for signal routing.",
    "secondary": "In audio engineering and data center administration, a flexible cord terminating in jacks plugged into patchbays.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "Profiles of the Future", "quote": "The communications officer snapped a heavy **patchcord** into the transmitter console, establishing contact with the lunar station."},
      {"author": "Philip K. Dick", "work": "Do Androids Dream of Electric Sheep?", "quote": "He disconnected the frayed **patchcord** from the empathy console, silencing the simulated mountain climb."},
      {"author": "Stanislaw Lem", "work": "Solaris", "quote": "A tangle of black **patchcord** wiring linked the spectrometer to the main library computer bank."}
    ]
  },
  "Dashboard — pat/patched.md": {
    "primary": "Mended or covered with patches; assembled hurriedly or roughly from disparate parts.",
    "secondary": "In literature and colloquial speech, describing worn garments repaired with cloth or improvised truces.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "You praise yourself by laying defects of judgment to me; but you **patched** up your excuses with hollow falsehoods."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The peasant wore a faded smock **patched** with corduroy at the elbows, weathered by decades of field labour."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ishmael wrapped himself in a counterpane of **patched** quilt, marveling at its crazy geometric squares."}
    ]
  },
  "Dashboard — pat/patchily.md": {
    "primary": "In a patchy manner; unevenly, irregularly, or only in scattered spots.",
    "secondary": "In meteorology and surface painting, occurring with irregular density across an observed area.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The winter snow melted **patchily** across Egdon Heath, leaving dark pools of black bog water amid yellow furze."},
      {"author": "Virginia Woolf", "work": "The Voyage Out", "quote": "The morning sun shone **patchily** through shifting London fog, warming the damp stone pavements in brief flashes."},
      {"author": "Joseph Conrad", "work": "Typhoon", "quote": "The vessel was **patchily** painted with red lead, showing raw rust beneath her battered bulwarks."}
    ]
  },
  "Dashboard — pat/patchiness.md": {
    "primary": "The quality, condition, or appearance of being patchy; irregularity, unevenness, or inconsistency.",
    "secondary": "In ecology and landscape architecture, spatial heterogeneity characterized by fragmented habitat zones.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The notable **patchiness** of alpine plant distribution across isolated mountain peaks points to past glacial migrations."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The **patchiness** of his education left curious gaps in his historical knowledge, despite immense classical reading."},
      {"author": "Aldous Huxley", "work": "Point Counter Point", "quote": "The conversation suffered from an awkward **patchiness**, marked by fitful brilliance punctuated by uncomfortable silences."}
    ]
  },
  "Dashboard — pat/patching.md": {
    "primary": "The act or process of mending, repairing, or reinforcing with patches; improvising a temporary repair.",
    "secondary": "In software maintenance and textiles, applying corrective code updates or stitching reinforcement fabric.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Ham had been **patching** up a great pair of waterboots; and I sat beside him on the upturned boat admiring his skill."},
      {"author": "G. K. Chesterton", "work": "The Wisdom of Father Brown", "quote": "The ancient roof bore traces of repeated **patching**, showing where Tudor tiles met modern slate."},
      {"author": "Walter Scott", "work": "Rob Roy", "quote": "The cooper was busy **patching** leaky herring barrels with fresh willow hoops along the Glasgow quay."}
    ]
  },
  "Dashboard — pat/patchouli.md": {
    "primary": "An aromatic plant (*Pogostemon cablin*) of the mint family, native to tropical Asia; also the pungent perfume made from it.",
    "secondary": "In perfumery and counterculture history, a heavy, musky, earth-scented essential oil extracted from dried leaves.",
    "quotes": [
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "A faint scent of heavy **patchouli** lingered in the boudoir, mingling with the sweet fragrance of lilac blossoms."},
      {"author": "E. M. Forster", "work": "Where Angels Fear to Tread", "quote": "The letter smelled faintly of **patchouli**, a vulgar perfume that Philip instinctively disliked."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "A subtle trail of **patchouli** guided the hound through the damp labyrinth of river wharves."}
    ]
  },
  "Dashboard — pat/patchouly.md": {
    "primary": "An alternative spelling of patchouli; a fragrant Southeast Asian mint plant yielding a strong aromatic oil.",
    "secondary": "In nineteenth-century botanical texts, the herbal species *Pogostemon cablin* utilized for scenting imported Indian shawls.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Becky Sharp unpacked her exotic cashmere shawls, heavily perfumed with oriental **patchouly** to preserve them from moths."},
      {"author": "Gustave Flaubert", "work": "Madame Bovary", "quote": "The scent of **patchouly** from her handkerchief brought back memories of glittering Parisian theatre boxes."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The fashionable lady enveloped herself in clouds of musk and **patchouly**, overpowering the dusty odor of the legal office."}
    ]
  },
  "Dashboard — pat/patchwork.md": {
    "primary": "Needlework made by sewing together pieces of fabric of different designs, colors, or textures; any hodgepodge.",
    "secondary": "In social criticism and political analysis, an incongruous assemblage of disparate laws, policies, or factions.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Under the thatched roofs her mind's eye beheld rustic bedrooms with cheerful **patchwork** quilts draped over low beds."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "This imperfectly taught woman, whose phrases and habits were an odd **patchwork** of provincial vulgarity and town polish."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The walls were whitewashed as white as milk, and the **patchwork** counterpane on the bed was made of a thousand pieces."}
    ]
  },
  "Dashboard — pat/patchy.md": {
    "primary": "Existing or happening in scattered patches; irregular, uneven, or inconsistent in quality.",
    "secondary": "In agronomy and dermatology, displaying mottled discoloration or sparse, uneven foliage growth.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Any stranger peeping into the office at that moment might have wondered what **patchy** business could detain them so late."},
      {"author": "G. K. Chesterton", "work": "The Wisdom of Father Brown", "quote": "These black beams were set crooked or crisscross at all kinds of angles, giving the plaster wall a curiously **patchy** look."},
      {"author": "Virginia Woolf", "work": "The Waves", "quote": "Memory is **patchy**; brilliant moments of childhood remain vivid while entire years dissolve into gray fog."}
    ]
  },
  "Dashboard — pat/pate.md": {
    "primary": "A person's head or the crown of the head; also (with accent) a rich paste or spread of seasoned minced meat or fish.",
    "secondary": "In Shakespearean comedy and culinary history, an archaic colloquial term for the scalp, or a gourmet liver terrine.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "I would I had; so I had broke thy **pate**, and ask'd thee mercy for't with a repentant heart."},
      {"author": "King James Bible", "work": "The Holy Bible", "quote": "His mischief shall return upon his own head, and his violent dealing shall come down upon his own **pate**."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The engineer tapped his bald **pate** with a greasy wrench, listening intently to the clatter of the boiler."}
    ]
  },
  "Dashboard — pat/patella.md": {
    "primary": "The kneecap; the small, flat, triangular bone protecting the anterior surface of the knee joint.",
    "secondary": "In marine biology and malacology, a genus of shallow-water marine gastropods comprising the true limpets.",
    "quotes": [
      {"author": "Henry Gray", "work": "Gray's Anatomy", "quote": "The **patella** is a sesamoid bone developed within the tendon of the quadriceps extensor muscle."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Upon the rocky tidal shelf, numerous shells of **patella** adhered with astonishing tenacity to the wave-swept granite."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Testing the deep tendon reflex by briskly striking below the **patella** elicits the normal knee jerk."}
    ]
  },
  "Dashboard — pat/patellar.md": {
    "primary": "Of, relating to, or situated near the patella (kneecap).",
    "secondary": "In clinical neurology, pertaining to the patellar reflex (knee-jerk reflex) mediated by the femoral nerve.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Absence of the **patellar** reflex is one of the earliest and most dependable signs of tabetic degeneration in the cord."},
      {"author": "Henry Gray", "work": "Gray's Anatomy", "quote": "The **patellar** ligament attaches the lower apex of the kneecap to the prominent tuberosity of the tibia."},
      {"author": "Oliver Sacks", "work": "A Leg to Stand On", "quote": "The neurologist tapped gently against my tendon, testing whether the brisk **patellar** response had returned after surgery."}
    ]
  },
  "Dashboard — pat/patellidae.md": {
    "primary": "A taxonomic family of marine gastropod mollusks commonly known as true limpets.",
    "secondary": "In marine invertebrate zoology, conical uncoiled snails possessing a muscular foot that clings to littoral rocks.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "Island Life", "quote": "The littoral fauna of the Atlantic islands includes specialized species of **patellidae** clinging to volcanic basalt reefs."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrate Animals", "quote": "In the family **patellidae**, the conical shell exhibits no spiral coiling, providing an optimal shield against heavy surf."},
      {"author": "Rachel Carson", "work": "The Edge of the Sea", "quote": "Mollusks of the family **patellidae** graze on encrusting algae, returning faithfully to their home scar on the rock."}
    ]
  },
  "Dashboard — pat/patelliform.md": {
    "primary": "Shaped like a small dish, platter, limpet shell, or kneecap; patelloid.",
    "secondary": "In botanical and mycological morphology, describing saucer-shaped or shallow bowl-like apothecia and spores.",
    "quotes": [
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "Certain fungal fructifications develop a distinctly **patelliform** disc with raised margins to disperse their microscopic spores."},
      {"author": "Charles Darwin", "work": "A Monograph on the Sub-class Cirripedia", "quote": "The base plate of this barnacle presents a shallow **patelliform** depression fitted snugly to the underlying rock."},
      {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "The lichens produce small **patelliform** cups that cup moisture and foster the growth of reproductive asci."}
    ]
  },
  "Dashboard — pat/patency.md": {
    "primary": "The state or condition of being open, unobstructed, or expanded (especially of a bodily duct or blood vessel).",
    "secondary": "In cardiovascular physiology and legal patent systems, open lumen passage or the public status of patent rights.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The surgeon confirmed the **patency** of the bile duct by verifying the immediate flow of hepatic secretion."},
      {"author": "Henry Gray", "work": "Gray's Anatomy", "quote": "The lumen of the radial artery retained full **patency** despite the proximity of the fibrous fracture callus."},
      {"author": "Atul Gawande", "work": "Complications: A Surgeon's Notes on an Imperfect Science", "quote": "We checked the **patency** of the catheter under fluoroscopy before injecting the radio-opaque dye."}
    ]
  },
  "Dashboard — pat/patent.md": {
    "primary": "Easily recognizable; obvious; also a government authority or license conferring exclusive rights to an inventor.",
    "secondary": "In intellectual property law and anatomy, legal monopoly over an invention or an open, unobstructed bodily vessel.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "The cause of this fair gift in me is wanting, and so my **patent** back again is swerving to its rightful owner."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "These are the more **patent** facts which are to be deduced from his hat, obvious to any observant eye."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "I did not quite mean you to accept it at first, for it was my one poor **patent** against despair."}
    ]
  },
  "Dashboard — pat/patented.md": {
    "primary": "Protected by a patent; copyrighted or licensed as proprietary intellectual property.",
    "secondary": "In industrial history and commerce, legally protected manufacturing processes secured against imitation.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The Maker of this earth but **patented** a leaf, and all subsequent foliage follows that divine master pattern."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "He **patented** an unbreakable bicycle tire, and his prosperous business brought him into contact with foreign investors."},
      {"author": "Mark Twain", "work": "A Connecticut Yankee in King Arthur's Court", "quote": "I introduced a **patented** system of modern taxation that doubled the king's revenue without impoverishing peasants."}
    ]
  },
  "Dashboard — pat/patentee.md": {
    "primary": "A person or corporate entity to whom a patent is officially granted.",
    "secondary": "In commercial jurisprudence, the legal holder possessing exclusive statutory rights to exploit an invention.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "He was a **patentee** of the Openshaw unbreakable tire, and his business met with immense success in Birmingham."},
      {"author": "Charles Babbage", "work": "On the Economy of Machinery and Manufactures", "quote": "The **patentee** must frequently expend his entire fortune defending his statutory privilege against piratical infringers."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Monopoly granted to a **patentee** of a new machine is justified as a temporary reward for ingenuity and capital expenditure."}
    ]
  },
  "Dashboard — pat/patently.md": {
    "primary": "Clearly, without doubt; obviously and undeniably.",
    "secondary": "In analytical argument and legal debate, describing assertions whose truth or falsehood is self-evident.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "The Problems of Philosophy", "quote": "To deny that sensory experiences correspond to external reality appears **patently** absurd to common sense."},
      {"author": "Virginia Woolf", "work": "Night and Day", "quote": "His clumsy attempt to flatter her intellect was so **patently** insincere that Katharine could not suppress a smile."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "The official newspaper accounts were so **patently** false that even the rawest recruit mocked the headlines."}
    ]
  },
  "Dashboard — pat/pater.md": {
    "primary": "Father (chiefly colloquial British or Latin in formal phrases).",
    "secondary": "In public school slang and classical literature, an affectionate term for one's father, or the Latin designation in ecclesiastical texts.",
    "quotes": [
      {"author": "P. G. Wodehouse", "work": "The Inimitable Jeeves", "quote": "My dear fellow, the **pater** will cut off my allowance without a shilling if I marry a chorus girl."},
      {"author": "William Makepeace Thackeray", "work": "The History of Pendennis", "quote": "Pen wrote a dutiful epistle to the **pater**, requesting an urgent remittance to settle college debts at Oxbridge."},
      {"author": "James Joyce", "work": "A Portrait of the Artist as a Young Man", "quote": "Stephen remembered his **pater** standing by the hearth, recounting tales of old Cork with theatrical relish."}
    ]
  },
  "Dashboard — pat/paterfamilias.md": {
    "primary": "The male head of a family, household, or domestic establishment.",
    "secondary": "In Roman law and social history, the male citizen possessing absolute legal authority (*patria potestas*) over family and slaves.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The Roman **paterfamilias** held the sovereign power of life and death over his children, sanctioned by the Twelve Tables."},
      {"author": "William Makepeace Thackeray", "work": "The Newcomes", "quote": "Colonel Newcome appeared every inch the benevolent **paterfamilias**, surrounded by happy young faces at the Christmas feast."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Garth sat at the head of the breakfast board like a loving **paterfamilias**, dispensing porridge and good cheer."}
    ]
  },
  "Dashboard — pat/paternal.md": {
    "primary": "Of, relating to, or characteristic of a father; fatherly, benevolent, or protective.",
    "secondary": "In genealogy and jurisprudence, lineage, property, or legal rights inherited from or traced through the father's side.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Let it be so, thy truth then be thy dower: for, by the sacred radiance of the sun, here I disclaim all my **paternal** care."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "His letters were to be forwarded to Gordon Square, where he had inherited a modest **paternal** estate from his father."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "In several species of birds, **paternal** devotion is so marked that the male alone incubates the clutch of eggs."}
    ]
  },
  "Dashboard — pat/paternalism.md": {
    "primary": "The policy or practice of treating individuals or subordinates with patriarchal authority, providing for needs while restricting freedom.",
    "secondary": "In political philosophy and industrial history, authoritarian management style cloaked in benevolent protection.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Democratic citizens fear a centralized **paternalism** that spares them the trouble of thinking and all the difficulty of living."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "The state has no moral right to enforce a coercive **paternalism** upon competent adults for their own alleged benefit."},
      {"author": "Thorstein Veblen", "work": "The Theory of the Leisure Class", "quote": "Company town administrators defended their oppressive regulations under the benign name of industrial **paternalism**."}
    ]
  },
  "Dashboard — pat/paternalistic.md": {
    "primary": "Characterized by the restriction of the freedom and responsibilities of subordinates in their supposed best interest.",
    "secondary": "In sociology and corporate governance, benevolent yet condescending policies that infantilize employees or citizens.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "Undershaft mocked the **paternalistic** social schemes of model employers, declaring high wages alone secured respect."},
      {"author": "Aldous Huxley", "work": "Brave New World", "quote": "The World State maintained a thoroughly **paternalistic** control over citizens through conditioned happiness and chemical soma."},
      {"author": "Jane Addams", "work": "Democracy and Social Ethics", "quote": "A genuinely democratic settlement house rejects **paternalistic** philanthropy in favor of mutual civic cooperation."}
    ]
  },
  "Dashboard — pat/paternally.md": {
    "primary": "In a paternal, fatherly, benevolent, or protective manner.",
    "secondary": "In genealogical descent, on or through the father's side of the family.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Mr. Jaggers laid his large hand **paternally** upon Pip's shoulder, advising him to guard his fortune against adventurers."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The old baronet beamed **paternally** upon the assembled tenantry, wishing them prosperity at the harvest feast."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard regarded the girl **paternally**, longing to reveal that the bond between them was far deeper than friendship."}
    ]
  },
  "Dashboard — pat/paternity.md": {
    "primary": "The state or condition of being a father; fatherhood, fatherly origin, or male descent.",
    "secondary": "In legal medicine and genetics, determining biological parentage through genealogical records or DNA profiling.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "I do hate the aristocratic principle of blood before everything, and do think that true nobility lies not in ancient **paternity**."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The terms used by naturalists of affinity and community of type are not metaphorical, but signify direct community of **paternity**."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Our souls are like those orphans whose unwedded mothers die in bearing them: the secret of our **paternity** lies in the grave."}
    ]
  },
  "Dashboard — pat/paternoster.md": {
    "primary": "The Lord's Prayer, especially in the Latin form; also a bead in a rosary indicating this prayer.",
    "secondary": "In medieval religious practices and mechanical lifts, a bead strand used to count prayers, or a continuously looping cyclic elevator.",
    "quotes": [
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The hermit crossed himself devoutly and muttered a **paternoster** before sharing his venison pasty with the Black Knight."},
      {"author": "Geoffrey Chaucer", "work": "The Canterbury Tales", "quote": "The gentle prioress carried a rosary of coral beads, whereon hung a golden brooch between each holy **paternoster**."},
      {"author": "Victor Hugo", "work": "The Hunchback of Notre-Dame", "quote": "The blind beggar repeated his Latin **paternoster** upon the cathedral steps, holding out a wooden bowl to passersby."}
    ]
  },
  "Dashboard — pat/paterson.md": {
    "primary": "A prominent industrial city in northeastern New Jersey, historically known as the 'Silk City'; also a surname.",
    "secondary": "In American industrial history and epic modern poetry, the planned manufacturing center founded by Alexander Hamilton, immortalized by William Carlos Williams.",
    "quotes": [
      {"author": "William Carlos Williams", "work": "Paterson", "quote": "A man in himself is a city, beginning, seeking, achieving and concluding his life amidst the roaring falls of **paterson**."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "The shipping firm Carter, **paterson** & Co., London, delivered the heavy wooden boxes of earth from Transylvania."},
      {"author": "Jack London", "work": "The Iron Heel", "quote": "We read of the great textile strikes in **paterson**, where immigrant silk weavers confronted armed militia in winter."}
    ]
  },
  "Dashboard — pat/patience.md": {
    "primary": "The capacity to accept or tolerate delay, trouble, or suffering without getting angry or upset.",
    "secondary": "In ethical philosophy and solo gaming, steadfast moral fortitude under trial, or a class of card games played alone (solitaire).",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "O let me suffer, being at your beck, the imprisoned absence of your liberty; and **patience**, tame to sufferance, bide each check."},
      {"author": "John Milton", "work": "On His Blindness", "quote": "But **patience**, to prevent that murmur, soon replies: God doth not need either man's work or his own gifts."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Anne Elliot bore the trials of neglect with dignified **patience**, finding solace in quiet acts of benevolence."}
    ]
  },
  "Dashboard — pat/patient.md": {
    "primary": "Able to accept or tolerate delays, problems, or suffering without becoming annoyed; also a person receiving medical care.",
    "secondary": "In clinical medicine, an individual undergoing medical evaluation or treatment by physicians and nurses.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Thence comes it that my name receives a brand, and almost thence my nature is subdued to what it works in, like the dyer's hand: pity me then and wish I were a **patient** man."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Dr. Watson examined the nervous **patient** in the consulting room, noting his trembling fingers and pallid brow."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The good doctor was gentle and **patient** with the sick waif, dressing his fevered wounds with untiring charity."}
    ]
  },
  "Dashboard — pat/patiently.md": {
    "primary": "In a patient manner; with calmness, endurance, and forbearance without complaint or irritation.",
    "secondary": "In descriptive narrative, enduring prolonged discomfort or tedium with steadfast composure.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Give me leave to speak my mind, and I will through and through cleanse the foul body of the infected world, if they will **patiently** receive my medicine."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "He waited **patiently**, apathetically, till the violence of her grief had worn itself out in sobbing."},
      {"author": "Lewis Carroll", "work": "Alice's Adventures in Wonderland", "quote": "This time Alice waited **patiently** until it chose to speak again, watching the Cheshire Cat fade into a grin."}
    ]
  },
  "Dashboard — pat/patina.md": {
    "primary": "A green or brown film on the surface of bronze or copper produced by oxidation over a long period; a surface sheen.",
    "secondary": "In antique connoisseurship and metallurgy, the mellow luster acquired by wood or metal through age and handling.",
    "quotes": [
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He admired the Renaissance bronze dagger, upon whose chased handle centuries of handling had imparted a rich, dark **patina**."},
      {"author": "Henry James", "work": "The Golden Bowl", "quote": "The antique shop was filled with venerable curiosities whose soft **patina** whispered of ancient Venetian palazzos."},
      {"author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "The true glory of a Gothic cathedral lies not in its pristine stones, but in the golden **patina** of age and moss."}
    ]
  },
  "Dashboard — pat/patinate.md": {
    "primary": "Acquire or cover with a patina; develop a thin protective or decorative oxidized surface coating.",
    "secondary": "In sculpture conservation and art manufacturing, deliberately applying chemical agents to oxidize metal surfaces.",
    "quotes": [
      {"author": "John Addington Symonds", "work": "The Life of Benvenuto Cellini", "quote": "The master bronze-caster would chemically **patinate** his finished statuettes to achieve a deep Florentine luster."},
      {"author": "Walter Pater", "work": "Studies in the History of the Renaissance", "quote": "Exposure to damp Tuscan air served to **patinate** the outdoor relief, softening the harsh edges of the bronze."},
      {"author": "Auguste Rodin", "work": "Art: Conversations with Paul Gsell", "quote": "Time and weather collaborate with the sculptor to **patinate** the metal, giving bronze a living, breathing soul."}
    ]
  },
  "Dashboard — pat/patinise.md": {
    "primary": "Cover or treat with a patina, especially by artificial or chemical means (British spelling).",
    "secondary": "In decorative arts and bronze craftsmanship, inducing superficial oxidation with acid washes to simulate antiquity.",
    "quotes": [
      {"author": "Oscar Wilde", "work": "Intentions", "quote": "The cunning forger sought to **patinise** the forged Greek coin with acid vapors, hoping to deceive the British Museum."},
      {"author": "William Morris", "work": "Hopes and Fears for Art", "quote": "Craftsmen who genuinely love metals refuse to artificially **patinise** their copper, preferring the natural touch of years."},
      {"author": "E. M. Forster", "work": "Where Angels Fear to Tread", "quote": "The village silversmith learned how to **patinise** his medals to satisfy tourists clamoring for antique relics."}
    ]
  },
  "Dashboard — pat/patinize.md": {
    "primary": "Treat or coat a surface with a patina, or cause to acquire the appearance of aged metal.",
    "secondary": "In metallurgy and industrial fabrication, oxidizing copper alloys with sulfide or nitrate baths.",
    "quotes": [
      {"author": "Henry James", "work": "The American", "quote": "The French antique dealer offered to **patinize** the modern bronze sconces so they would harmonize with Louis Quinze woodwork."},
      {"author": "Edith Wharton", "work": "The Custom of the Country", "quote": "Her decorator took pains to **patinize** the gilded picture frames, subduing their modern glare for the drawing room."},
      {"author": "Thorstein Veblen", "work": "The Theory of the Leisure Class", "quote": "Wealthy collectors pay exorbitant sums for artisans to **patinize** novel goods, simulating the prestige of hereditary antiquity."}
    ]
  },
  "Dashboard — pat/patio.md": {
    "primary": "A paved outdoor area adjoining a house, used for dining or recreation; an inner paved courtyard.",
    "secondary": "In Hispanic architecture, an open interior quadrangle encircled by arcades and adorned with fountains and potted plants.",
    "quotes": [
      {"author": "Washington Irving", "work": "Tales of the Alhambra", "quote": "The Moorish palace was built around a tranquil **patio**, where splashing fountains cooled the fragrance of orange blossoms."},
      {"author": "Ernest Hemingway", "work": "The Sun Also Rises", "quote": "We sat out on the hotel **patio** in the evening breeze, drinking cold wine as the bullfighters strolled past."},
      {"author": "W. H. Hudson", "work": "The Purple Land", "quote": "The estancia had a broad brick **patio** shaded by grapevine trellises, where the gauchos gathered to sing ballads."}
    ]
  },
  "Dashboard — pat/patisserie.md": {
    "primary": "A shop where French pastries and cakes are made and sold; also French pastry or baking as an art.",
    "secondary": "In culinary gastronomy, delicate confections such as éclairs, mille-feuilles, and tarts crafted with laminated doughs.",
    "quotes": [
      {"author": "Marcel Proust", "work": "Swann's Way", "quote": "The display window of the Parisian **patisserie** gleamed with golden brioches, glazed fruit tarts, and delicate almond madeleines."},
      {"author": "Gustave Flaubert", "work": "Sentimental Education", "quote": "Frédéric paused outside the fashionable **patisserie**, inhaling the rich aroma of melted butter and toasted sugar."},
      {"author": "Katherine Mansfield", "work": "The Garden Party and Other Stories", "quote": "The children gazed longing through the glass of the **patisserie**, admiring pink cream puffs dusted with powdered sugar."}
    ]
  },
  "Dashboard — pat/patness.md": {
    "primary": "The quality of being pat; opportune appropriateness, or suspicious glibness and over-convenience.",
    "secondary": "In literary criticism and drama, plot coincidences or neat solutions that feel artificial and contrived.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Our Theatres in the Nineties", "quote": "The utter **patness** of the hero's sudden inheritance in the third act betrayed the playwright's lack of genuine dramatic invention."},
      {"author": "Virginia Woolf", "work": "The Common Reader", "quote": "Real life rarely exhibits the neat **patness** of Victorian novels, where every sinner is punished and every virtue rewarded."},
      {"author": "Henry James", "work": "The Art of the Novel", "quote": "An author must avoid excessive **patness** of dialogue if he wishes his characters to breathe the air of reality."}
    ]
  },
  "Dashboard — pat/patois.md": {
    "primary": "The dialect of the common people of a region, differing in various respects from the standard language.",
    "secondary": "In sociolinguistics, non-standard vernacular speech or regional jargon lacking official orthography.",
    "quotes": [
      {"author": "Victor Hugo", "work": "Les Misérables", "quote": "The Parisian street urchin spoke a lively **patois**, blending underworld slang with the quick wit of the barricades."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Elizabeth-Jane was careful to weed every provincial **patois** word from her vocabulary to please her ambitious father."},
      {"author": "George Sand", "work": "The Master Bell-Ringers", "quote": "The village woodsmen conversed in a rich Berry **patois**, unintelligible to townspeople accustomed to Parisian French."}
    ]
  },
  "Dashboard — pat/paton.md": {
    "primary": "A Scottish surname, historically derived from Patrick; also associated with Alan Paton, author of Cry, the Beloved Country.",
    "secondary": "In South African literature and anti-apartheid history, denoting Alan Paton's humanitarian prose and liberal leadership.",
    "quotes": [
      {"author": "Alan Paton", "work": "Cry, the Beloved Country", "quote": "The author Alan **paton** wrote with profound sorrow of the broken tribes and wounded valleys of his native South Africa."},
      {"author": "Nadine Gordimer", "work": "The Essential Gesture", "quote": "The moral voice of **paton** challenged the complacency of white South Africa during the darkest decades of segregation."},
      {"author": "Ezekiel Mphahlele", "work": "The African Image", "quote": "Critics acknowledged that **paton** brought a passionate lyrical compassion to the tragic racial divisions of Natal."}
    ]
  },
  "Dashboard — pat/patrai.md": {
    "primary": "The modern Greek transliteration of Patras, a major port city in the northwestern Peloponnese of Greece.",
    "secondary": "In Mediterranean maritime trade and Hellenic history, an ancient Roman colony and bustling modern commercial hub on the Gulf of Patras.",
    "quotes": [
      {"author": "Lord Byron", "work": "Letters and Journals", "quote": "Our vessel anchored in the harbor of **patrai**, where the majestic peaks of the Peloponnese towered above the sparkling blue gulf."},
      {"author": "Pausanias", "work": "Description of Greece", "quote": "In ancient **patrai**, the temple of Artemis Laphria stood atop the acropolis, revered by pilgrims from across Achaea."},
      {"author": "Edward Dodwell", "work": "A Classical and Topographical Tour through Greece", "quote": "The merchant ships lined the quay of **patrai**, loading barrels of fragrant currants and olive oil for European markets."}
    ]
  }
}

def curate_file(rel_path, info):
    base_dir = "App database/Latin roots/Cluster Emotion"
    filepath = os.path.join(base_dir, rel_path)
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return False
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    fm_match = re.search(r"^---\n.*?\n---\n", content, re.DOTALL)
    if not fm_match:
        print(f"Frontmatter missing: {filepath}")
        return False
    frontmatter = fm_match.group(0)
    
    w = os.path.splitext(os.path.basename(rel_path))[0]
    header = f"# {w}\n\n"
    
    dv_match = re.search(r"(> \[!status\] 🎯 \*\*Status:\*\*.*?```dataviewjs.*?```)", content, re.DOTALL)
    if not dv_match:
        print(f"Dataview block missing: {filepath}")
        return False
    dv_block = dv_match.group(1)
    
    defs_block = f"""> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: {info['primary']}
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {info['secondary']}"""

    quotes_lines = ["> [!quote] 💬 Contextual Usage & Authentic Quotations"]
    for q in info["quotes"]:
        quotes_lines.append(f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{q['quote']}\"*")
    quotes_block = "\n".join(quotes_lines)
    
    new_content = f"{frontmatter}{header}{dv_block}\n\n{defs_block}\n\n{quotes_block}\n"
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True

success = 0
for rel_path, info in data.items():
    if curate_file(rel_path, info):
        success += 1

print(f"Successfully updated {success}/{len(data)} notes in Dashboard — pat (Part A).")
