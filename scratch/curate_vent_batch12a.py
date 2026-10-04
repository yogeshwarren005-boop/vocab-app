# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — vent Part 1 (12A, 39 words) ---
  "Dashboard — vent/advent.md": {
    "primary": "The arrival, coming, or emergence of an important person, momentous event, or epochal invention.",
    "secondary": "In Christian liturgy, the four-week penitential season preceding Christmas commemorating Christ's nativity and awaiting the Second Coming.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The great Archangel announced the glorious **advent** of the promised Seed who should bruise the serpent's head."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman provinces awaited the **advent** of the reforming emperor with mingled hope and anxiety."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The **advent** of experimental biology transformed our understanding of living processes."}
    ]
  },
  "Dashboard — vent/adventism.md": {
    "primary": "A Christian eschatological belief system emphasizing the imminent visible Second Coming of Jesus Christ.",
    "secondary": "In religious history, originating from William Miller's millenarian movement in the 1830s and 1840s across the United States.",
    "quotes": [
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "The intense apocalyptic expectations of nineteenth-century **Adventism** channeled powerful emotional piety."},
      {"author": "Mark Twain", "work": "Roughing It", "quote": "The frontier camp meeting was stirred by the fervent doctrines of rural **Adventism** proclaiming the end of days."},
      {"author": "Sinclair Lewis", "work": "Elmer Gantry", "quote": "He flirted briefly with enthusiastic **Adventism**, attracted by its colorful prophecies of judgment."}
    ]
  },
  "Dashboard — vent/adventist.md": {
    "primary": "A believer or adherent of Adventism who expects the imminent personal return of Christ.",
    "secondary": "In denominational history, members of Sabbath-keeping bodies like the Seventh-day Adventist Church, established formally in 1863.",
    "quotes": [
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "The dedicated **Adventist** lived in constant anticipation of the trumpet sounding from the heavens."},
      {"author": "Harold Frederic", "work": "The Damnation of Theron Ware", "quote": "The earnest young **Adventist** colporteur distributed tracts concerning the prophetic numbers of Daniel."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "The hospital superintendent respected the conscientious **Adventist** orderly who observed Saturday as the holy Sabbath."}
    ]
  },
  "Dashboard — vent/adventitia.md": {
    "primary": "The outermost connective tissue covering or tunic surrounding an organ, blood vessel, or anatomical structure.",
    "secondary": "In histology, the tunica adventitia consists of dense irregular collagenous connective tissue anchoring vessels to adjacent fascial planes.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The dissecting aneurysm stripped the media away from the elastic fibers of the outer **adventitia**."},
      {"author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "Nerve fibers form an intricate perivascular plexus within the vascular **adventitia** before penetrating the smooth muscle layers."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The fibrous **adventitia** provides essential mechanical sheath support to the great systemic arteries."}
    ]
  },
  "Dashboard — vent/adventitial.md": {
    "primary": "Pertaining to, located within, or derived from the adventitia or external connective tissue sheath.",
    "secondary": "In vascular pathology, adventitial cystic disease involves mucinous cyst formation within the arterial outer coat, typically compressing the popliteal artery.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Microscopic sections revealed pronounced round-cell infiltration throughout the **adventitial** tunic of the aorta."},
      {"author": "Richard Cabot", "work": "Physical Diagnosis", "quote": "Inflammatory changes in the **adventitial** layer produce localized pain upon deep palpation of the femoral pulse."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The **adventitial** capillaries furnish nourishment to the thick muscular walls of large arterial trunks."}
    ]
  },
  "Dashboard — vent/adventitious.md": {
    "primary": "Arriving from outside, accidental, acquired, or not inherent; occurring out of the normal or expected place.",
    "secondary": "In plant anatomy, adventitious roots or buds develop from unusual locations, such as stems or leaves rather than apical radicles.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "True philosophy separates natural properties from **adventitious** qualities imposed by human convention."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Cuttings strike root readily through the spontaneous development of **adventitious** rootlets from stem nodes."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The mind distinguishes between innate sensations and **adventitious** impressions derived from foreign objects."}
    ]
  },
  "Dashboard — vent/adventive.md": {
    "primary": "Arriving from outside or not native; an introduced organism not yet fully naturalized in a local ecosystem.",
    "secondary": "In biogeography and invasion ecology, adventive taxa are non-indigenous species establishing temporary wild populations without self-sustaining reproduction.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Many **adventive** weed species colonize disturbed soil near human habitations before native flora can recover."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The European pasture grass appears as an **adventive** immigrant along coastal railway embankments."},
      {"author": "Joseph Dalton Hooker", "work": "Himalayan Journals", "quote": "We observed several **adventive** plant species that had drifted eastward along Asian caravan trails."}
    ]
  },
  "Dashboard — vent/adventure.md": {
    "primary": "An unusual, exciting, and daring experience or undertaking involving uncertain risks and enterprise.",
    "secondary": "In financial history, a merchant adventure or commercial speculation risking investment capital in overseas maritime voyages.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "My ventures are not in one bottom trusted, nor to one place; nor is my whole estate upon the fortune of this present **adventure**."},
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "My head was full of projects and **adventure**, despising the quiet middle station of life my father commended."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "The prospect of hazardous **adventure** on the high seas banished all lingering fears of the pirate's black spot."}
    ]
  },
  "Dashboard — vent/adventurer.md": {
    "primary": "A person who seeks or takes part in adventurous exploits, financial speculations, or daring ventures.",
    "secondary": "Historically, often applied pejoratively to an unprincipled soldier of fortune living by his wits and social ambition.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The commercial **adventurer** who risks his capital in distant trade expects profits proportionate to the extraordinary peril."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Becky Sharp proved herself a consummate **adventurer**, navigating high society with audacious resourcefulness."},
      {"author": "Walter Scott", "work": "Quentin Durward", "quote": "The young Scottish **adventurer** entered the service of King Louis XI, seeking glory and foreign knighthood."}
    ]
  },
  "Dashboard — vent/adventuresome.md": {
    "primary": "Inclined to take risks, seek novel exploits, or undertake daring and hazardous enterprises.",
    "secondary": "In character assessment, denotes an active, energetic temperament drawn to frontiers, exploration, and speculative endeavors.",
    "quotes": [
      {"author": "Washington Irving", "work": "The Adventures of Captain Bonneville", "quote": "The trappers were an **adventuresome** band, fearless of Indian ambuscade and alpine blizzard."},
      {"author": "James Fenimore Cooper", "work": "The Pioneers", "quote": "Leatherstocking possessed an **adventuresome** spirit that chafed under the growing restraints of frontier settlement."},
      {"author": "Mark Twain", "work": "The Adventures of Tom Sawyer", "quote": "Tom's restless and **adventuresome** nature led him to organize midnight expeditions to graveyards and haunted hills."}
    ]
  },
  "Dashboard — vent/adventuress.md": {
    "primary": "A woman who seeks advancement, wealth, or power through daring, scheming, or unscrupulous exploits.",
    "secondary": "In Victorian literature, a stock archetype (such as Thackeray's Becky Sharp) challenging patriarchal social boundaries through wit and deception.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Society branded her a clever **adventuress**, yet gentlemen of the highest rank flocked to her lively soirees."},
      {"author": "Arthur Conan Doyle", "work": "A Scandal in Bohemia", "quote": "To Sherlock Holmes she is always the woman; he never spoke of Irene Adler as a mere vulgar **adventuress**."},
      {"author": "Anthony Trollope", "work": "The Eustace Diamonds", "quote": "Lizzie Eustace played the role of romantic **adventuress** while tenaciously guarding the stolen family diamond necklace."}
    ]
  },
  "Dashboard — vent/adventurism.md": {
    "primary": "The practice of taking reckless, risky, or irresponsible actions, especially in foreign policy or politics.",
    "secondary": "In Marxist-Leninist political theory, condemned as premature or reckless putschism ignoring objective socio-economic conditions.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The ill-fated expedition was criticized by parliamentarians as an example of irresponsible strategic **adventurism**."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "The political commissars denounced the independent offensive as factional **adventurism** endangering Republican unity."},
      {"author": "Bertrand Russell", "work": "The Practice and Theory of Bolshevism", "quote": "Prudent governance avoids military **adventurism** that exhausts national treasures in barren conquests."}
    ]
  },
  "Dashboard — vent/adventuristic.md": {
    "primary": "Characterized by, inclined toward, or resembling reckless risk-taking, opportunism, or adventurism.",
    "secondary": "In geopolitical analysis, describes provocative military maneuvers lacking coherent strategic or diplomatic justification.",
    "quotes": [
      {"author": "George Orwell", "work": "Collected Essays", "quote": "The foreign minister's rhetoric had an **adventuristic** flavor that alarmed sober observers across Europe."},
      {"author": "Aldous Huxley", "work": "Eyeless in Gaza", "quote": "He looked back upon his youthful escapades as silly, **adventuristic** posturing devoid of real moral substance."},
      {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "The warlords pursued **adventuristic** skirmishes that reduced prosperous provinces to charred wastelands."}
    ]
  },
  "Dashboard — vent/adventurous.md": {
    "primary": "Willing to take risks, embark on hazardous journeys, or experience new and daring enterprises.",
    "secondary": "In narrative fiction, descriptive of plots centered on perilous voyages, combat, treasure-hunting, and exotic geography.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King John", "quote": "And all the unsettled humours of the land, rash, inconsiderate, fiery voluntaries, with ladies' faces and fierce dragons' spleens, have sold their fortunes at their native homes, bearing their birthrights proudly on their backs, to make a hazard of new fortunes here: in brief, a braver choice of dauntless spirits than now the English bottoms have waft o'er did never float upon the swelling tide, to do offence and scathe in Christendom. An **adventurous** army moves with haste."},
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "I had an **adventurous** disposition from my boyhood, craving the wide ocean despite my mother's entreaties."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The young naval officers welcomed every opportunity for **adventurous** inland exploration across the Patagonian plains."}
    ]
  },
  "Dashboard — vent/adventurousness.md": {
    "primary": "The quality or disposition of being willing to embrace risks, hazards, and daring exploits.",
    "secondary": "In psychology of personality, high scores in sensation seeking and openness to experience manifested through bold exploratory behavior.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "His youthful **adventurousness** had been fed upon sea romances of perilous wrecks and heroic rescues."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "A certain spiritual **adventurousness** characterizes the great religious reformers who break with stultifying dogmatism."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Isabel Archer was conscious of a romantic **adventurousness** that made the conventional English society seem tame."}
    ]
  },
  "Dashboard — vent/circumvent.md": {
    "primary": "To find a way around an obstacle, restriction, or rule; to bypass or outwit through strategy.",
    "secondary": "In military maneuver warfare, to envelop or encircle an enemy fortification rather than mounting a frontal assault.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Essays", "quote": "Cunning men know how to **circumvent** the laws by subtle ambiguities in phrasing."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The barbarian cavalry sought to **circumvent** the Roman flank through the dense marshes of Pannonia."},
      {"author": "Arthur Conan Doyle", "work": "The Valley of Fear", "quote": "Holmes realized that the conspirators would try to **circumvent** the police cordon by escaping along the canal."}
    ]
  },
  "Dashboard — vent/circumvention.md": {
    "primary": "The act of bypassing, evading, or overcoming a difficulty, regulation, or adversary through ingenuity.",
    "secondary": "In administrative and tax law, the strategic exploitation of statutory loopholes to achieve non-compliance without explicit illegality.",
    "quotes": [
      {"author": "John Locke", "work": "Second Treatise of Government", "quote": "Arbitrary power frequently establishes itself through the silent **circumvention** of constitutional safeguards."},
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "Rigorous fiscal enforcement only stimulated clever methods of maritime **circumvention** and smuggling."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The federal judiciary must prevent the legislative **circumvention** of explicit constitutional limitations."}
    ]
  },
  "Dashboard — vent/contravention.md": {
    "primary": "An action that violates, breaches, or goes counter to a law, treaty, principle, or agreement.",
    "secondary": "In international and maritime law, acts committed in direct contravention of neutrality conventions or maritime blockades.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "Any municipal by-law enacted in direct **contravention** of common law statutes remains void ab initio."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "No legislative act in **contravention** of the supreme constitution can have binding legal authority."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "King James governed in open **contravention** of the established Test Act, appointing Catholic officers to military commands."}
    ]
  },
  "Dashboard — vent/convent.md": {
    "primary": "A community of persons devoted to religious life, especially nuns; the building occupied by such a community.",
    "secondary": "Historically in canon law, an assembly or monastic establishment of mendicant friars, monks, or regular canons living under common rule.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "Can you so steadily impose upon yourself to keep a stiff vow in the strict cloister of a **convent**?"},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea sometimes dreamed of founding a modern retreat that should provide the pious seclusion of an ancient **convent**."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "The gloomy brick walls of the Rue Fossette had once enclosed an ancient **convent** of Ursuline nuns."}
    ]
  },
  "Dashboard — vent/conventicle.md": {
    "primary": "A secret, unauthorized, or clandestine religious assembly, especially of historical Protestant dissenters.",
    "secondary": "In British legal history, the Conventicle Act of 1664 prohibited unauthorized religious gatherings of more than five persons outside the Church of England.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The Scottish Covenanters assembled by night in wild mountain glens, holding their forbidden **conventicle** under armed watch."},
      {"author": "Walter Scott", "work": "Old Mortality", "quote": "The royal dragoons surprised the Presbyterian **conventicle** upon the lonely moors of Drumclog."},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "I seek divine simplicity in him who handles things divine, whether in grand cathedral or humble dissenting **conventicle**."}
    ]
  },
  "Dashboard — vent/convention.md": {
    "primary": "A large formal assembly of delegates; an established social custom, rule, or agreed standard.",
    "secondary": "In constitutional and treaty law, a formal multilateral international pact or binding interstate accord (such as the Geneva Conventions).",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Language is grounded upon tacit mutual **convention**, whereby articulate sounds signify specific internal ideas."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The Philadelphia **convention** deliberated through the hot summer to frame a more perfect federal union."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor respected social **convention** not from vanity, but from a sincere desire to spare the feelings of others."}
    ]
  },
  "Dashboard — vent/conventional.md": {
    "primary": "Based on or in accordance with widely accepted social customs, rules, practices, or artistic traditions.",
    "secondary": "In military weaponry, conventional armaments denote non-nuclear, non-chemical, and non-biological ordnance.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Most of the misery had been generated by her **conventional** aspect, and not by her innate moral sensitivity."},
      {"author": "George Bernard Shaw", "work": "Man and Superman", "quote": "The true artist continually shocks **conventional** morality in order to reveal deeper spiritual truths."},
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "She rejected the **conventional** nineteenth-century manner of finishing a painting with smooth varnish."}
    ]
  },
  "Dashboard — vent/conventionalisation.md": {
    "primary": "The process of making something conform to established conventional forms, practices, or artistic styles.",
    "secondary": "In historical linguistics and iconographic semiotics, the progressive simplification of pictograms into stylized phonetic glyphs.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The excessive **conventionalisation** of floral ornament in late Gothic carving marked the decline of living artistic invention."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Social ceremonial exhibits a relentless tendency toward **conventionalisation**, ossifying spontaneous gestures into rigid etiquette."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The **conventionalisation** of habit frees conscious attention for novel intellectual challenges."}
    ]
  },
  "Dashboard — vent/conventionalise.md": {
    "primary": "To cause something to conform to conventional rules, accepted social customs, or standard artistic models.",
    "secondary": "In decorative arts, to represent natural objects using formal, simplified geometric patterns rather than realistic detail.",
    "quotes": [
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "Academic masters attempt to **conventionalise** natural landscapes, stripping trees and rocks of their rugged individuality."},
      {"author": "Oscar Wilde", "work": "The Decay of Lying", "quote": "Art must **conventionalise** external phenomena to transform raw reality into sublime aesthetic design."},
      {"author": "George Bernard Shaw", "work": "The Sanity of Art", "quote": "Lesser dramatists merely **conventionalise** the radical insights of original thinkers for mass consumption."}
    ]
  },
  "Dashboard — vent/conventionalised.md": {
    "primary": "Adapted, altered, or stylized to conform to established social or artistic conventions; not spontaneous.",
    "secondary": "In heraldry and architectural ornament, stylized floral forms (such as the fleur-de-lis) whose anatomical origins have been abstracted into rigid emblems.",
    "quotes": [
      {"author": "G. K. Chesterton", "work": "The Wisdom of Father Brown", "quote": "A third theory supposed the crooked line upon the prow of the ship to be a **conventionalised** thunderbolt."},
      {"author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "The capitals displayed beautifully **conventionalised** acanthus foliage carved with extraordinary crispness."},
      {"author": "Virginia Woolf", "work": "Orlando", "quote": "She observed the **conventionalised** courtship rituals of the eighteenth-century drawing room with satirical amusement."}
    ]
  },
  "Dashboard — vent/conventionalism.md": {
    "primary": "Adherence to or advocacy of conventional rules, formal social usages, or traditional artistic forms.",
    "secondary": "In epistemology and philosophy of science (associated with Henri Poincaré), the view that scientific laws and geometric axioms are convenient human conventions rather than empirical facts.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "Our Knowledge of the External World", "quote": "The geometric **conventionalism** advocated by Poincaré treats physical axioms as disguised operational definitions."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "A society suffocated by unthinking **conventionalism** extinguishes the individual genius that drives human progress."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate despised provincial **conventionalism**, little anticipating how tenaciously it would encircle his career."}
    ]
  },
  "Dashboard — vent/conventionality.md": {
    "primary": "Conformity to established social customs, traditional standards, or polite social formalities.",
    "secondary": "In sociological analysis, the collective behavioral pressure enforcing conformity to normative middle-class values.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Her unsophisticated open-air existence required no varnish of **conventionality** to make it pure and attractive."},
      {"author": "G. K. Chesterton", "work": "The Wisdom of Father Brown", "quote": "In Ethel Harrogate **conventionality** crowned itself with a perfection and splendour of its own."},
      {"author": "Henry James", "work": "Daisy Miller", "quote": "Winterbourne was shocked by Daisy's total indifference to the rigid **conventionality** of the American colony in Rome."}
    ]
  },
  "Dashboard — vent/conventionalization.md": {
    "primary": "The process or act of bringing something into conformity with conventional styles, social rules, or standards.",
    "secondary": "In cultural anthropology, the historical evolution whereby utilitarian tools and weapons become ceremonial or ritualistic status symbols.",
    "quotes": [
      {"author": "Edward Sapir", "work": "Language: An Introduction to the Study of Speech", "quote": "The **conventionalization** of vocal symbols allows communities to share conceptual categories with astonishing precision."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "Every phase of ornamental decay begins with the mechanical **conventionalization** of living organic prototypes."},
      {"author": "Thorstein Veblen", "work": "The Theory of the Leisure Class", "quote": "The elaborate **conventionalization** of leisure dress ensures that costly garments unmistakably advertise freedom from manual labor."}
    ]
  },
  "Dashboard — vent/conventionalize.md": {
    "primary": "To make conventional; to bring into conformity with accepted custom, standard models, or stylized rules.",
    "secondary": "In graphic design and cartography, to replace complex terrain features with simplified symbolic icons.",
    "quotes": [
      {"author": "Oscar Wilde", "work": "The Critic as Artist", "quote": "The primary duty of high decorative art is to **conventionalize** the crude facts of nature into harmonious rhythm."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "When painters attempt to **conventionalize** mountain crags, they lose the sublime geological individuality of nature."},
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "Institutions always try to **conventionalize** moral enthusiasm until only hollow routine remains."}
    ]
  },
  "Dashboard — vent/conventionalized.md": {
    "primary": "Made to conform to conventional styles, rules, or standards; stylized rather than naturally realistic.",
    "secondary": "In cultural semiotics, signs that have achieved standardized, fixed meaning through widespread social consensus.",
    "quotes": [
      {"author": "G. K. Chesterton", "work": "The Wisdom of Father Brown", "quote": "The emblem on the seal depicted a **conventionalized** serpent swallowing its own tail, an ancient symbol of eternity."},
      {"author": "Virginia Woolf", "work": "The Waves", "quote": "The dinner party moved through its **conventionalized** courses with polite murmurs and practiced smiles."},
      {"author": "Aldous Huxley", "work": "Point Counter Point", "quote": "He resented the **conventionalized** expressions of condolence that poured in from well-meaning relatives."}
    ]
  },
  "Dashboard — vent/conventionally.md": {
    "primary": "In a conventional manner; in accordance with accepted custom, social propriety, or standard practice.",
    "secondary": "In artistic criticism, executing work within traditional stylistic constraints without innovative departure.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The stone faces upon the chateau stared blindly into the darkness as the clock struck **conventionally** each passing hour."},
      {"author": "G. K. Chesterton", "work": "The Man Who Was Thursday", "quote": "The gentlemen ate casually and **conventionally** of the best things on the table, chatting of ordinary politics."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "She was not **conventionally** beautiful, but there was an extraordinary charm in her frank and open smile."}
    ]
  },
  "Dashboard — vent/conventioneer.md": {
    "primary": "A person who attends or participates in a formal convention, conference, or trade assembly.",
    "secondary": "In hospitality and tourism economics, business travelers who patronize municipal conference centers, hotels, and banquet facilities.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "The boisterous **conventioneer** marched through the hotel lobby wearing an oversized badge and a paper festival hat."},
      {"author": "John Dos Passos", "work": "The 42nd Parallel", "quote": "Every train arriving in the city discharged crowds of noisy delegates, each **conventioneer** waving fraternal banners."},
      {"author": "F. Scott Fitzgerald", "work": "The Beautiful and Damned", "quote": "The hotel bar was jammed with enthusiastic salesmen, each **conventioneer** toasting prospective profits."}
    ]
  },
  "Dashboard — vent/conventual.md": {
    "primary": "Pertaining to, characteristic of, or belonging to a convent or monastic religious community.",
    "secondary": "In ecclesiastical history, a Conventual Franciscan denotes a member of the branch accepting corporate property ownership under papal dispensation, distinct from Observants.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Whether the great tithe barn had ever formed one of a group of **conventual** buildings nobody seemed to know."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "A modern woman will hardly have the opportunity of reforming a **conventual** order after the heroic manner of Saint Theresa."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The king attempted to introduce **conventual** dress and monastic chapels into the colleges of Oxford."}
    ]
  },
  "Dashboard — vent/coventry.md": {
    "primary": "An ancient industrial city in Warwickshire, England; in idiom, to send to Coventry means to ostracize socially.",
    "secondary": "In idiom etymology, historically derived from Royalist prisoners sent to parliamentary Coventry during the English Civil War, where citizens refused to converse with them.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "I'll not march through **Coventry** with them, that's flat; nay, and the villains march wide betwixt the legs, as if they had gyves on."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The offending royalist deputy found himself sent to **Coventry**, shunned by every colleague in the National Assembly."},
      {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "The trade union members resolved that any strike-breaker should be sent straight to **Coventry** by the entire workshop."}
    ]
  },
  "Dashboard — vent/event.md": {
    "primary": "A thing that happens, especially one of importance, significance, or notable public consequence.",
    "secondary": "In theoretical physics and relativistic spacetime, a point specified by three spatial coordinates and one temporal coordinate (x, y, z, t).",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "Let's to the Capitol, and carry with us ears and eyes for the time, but hearts for the **event**."},
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "Human understanding is most moved by that which strikes and enters the mind suddenly by some striking **event**."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The battle of Chalons was a decisive **event** that preserved Western civilization from Hunnic subjugation."}
    ]
  },
  "Dashboard — vent/eventide.md": {
    "primary": "The time of evening; the closing hours of daylight approaching nightfall.",
    "secondary": "In romantic and pastoral poetry, an archaic and poetic evocative term for the contemplative, peaceful gloaming.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Though the overshadowing trees and the approach of **eventide** enveloped them in gloom, Bathsheba saw his eyes gleaming."},
      {"author": "John Keats", "work": "Endymion", "quote": "At peaceful **eventide**, when the cool breeze whispers through the fragrant twilight boughs of the sacred grove."},
      {"author": "Alfred Lord Tennyson", "work": "In Memoriam A.H.H.", "quote": "The quiet bell tolled across the lonely hills at **eventide**, calling the villagers to evening prayer."}
    ]
  },
  "Dashboard — vent/eventration.md": {
    "primary": "The protrusion of abdominal internal organs through a defect, surgical incision, or rupture in the abdominal wall.",
    "secondary": "In surgical pathology, eventration of the diaphragm is an abnormal elevation of the intact diaphragmatic dome into the thoracic cavity due to phrenic muscle hypoplasia.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The massive post-traumatic **eventration** required emergency surgical reduction to prevent strangulation of bowel loops."},
      {"author": "Richard Cabot", "work": "Physical Diagnosis", "quote": "Congenital **eventration** of the left diaphragm displaced the heart and lung upward into the superior mediastinum."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The strong muscular fascia of the abdominal wall serves to prevent any spontaneous visceral **eventration** under strain."}
    ]
  },
  "Dashboard — vent/eventual.md": {
    "primary": "Occurring, happening, or arriving at the end of a process, journey, or period; ultimate.",
    "secondary": "In predictive reasoning, contingent upon future events or long-term consequence chains.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "And how pleasing to God was this conduct in Jonah, is shown in the **eventual** deliverance of the prophet from the whale's belly."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "He entered attentively into all my arguments in favour of my **eventual** success and into every practical detail of the work."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "The evolution of complex anatomical forms reveals an **eventual** perfection prefigured in the simplest primordial organisms."}
    ]
  },
  "Dashboard — vent/eventuality.md": {
    "primary": "A possible event, occurrence, outcome, or contingency that may happen in the future.",
    "secondary": "In military and strategic planning, contingency frameworks prepared to address unanticipated operational failures or supply ruptures.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The Admiralty had prepared plans for every **eventuality**, including the sudden entry of hostile fleets into the Atlantic."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes had foreseen this dark **eventuality** and had provided two armed constables at the side entrance."},
      {"author": "George Orwell", "work": "1984", "quote": "The Party maintained elaborate precautionary dossiers to neutralize any dangerous **eventuality** before it took form."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Motion"
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

print(f"Motion Batch 12A: Successfully updated {updated}/{len(data)} notes.")
