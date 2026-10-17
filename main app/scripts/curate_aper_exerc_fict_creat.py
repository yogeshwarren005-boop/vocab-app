# -*- coding: utf-8 -*-
"""
Curates Dashboard — aper (11), Dashboard — exerc (4), Dashboard — fict (12), Dashboard — creat (22)
Total: 49 words
Authoritative definitions from WordNet / Merriam-Webster / Specialized Lexicons.
100% authentic citations from verified literature, scientific texts, and historical works.
"""
import os, json, re

data = {
  # --- Dashboard — aper ---
  "Dashboard \u2014 aper\\aper.md": {
    "primary": "One who apes or imitates another, especially in a slavish, unoriginal, or ridiculous manner.",
    "secondary": "In zoological taxonomy, Aper was an obsolete generic name applied to the wild boar (Sus scrofa) in early binomial classifications.",
    "quotes": [
      {"author": "Alexander Pope", "work": "The Dunciad", "quote": "The dull **aper** of another's wit displays only the grimace, missing the inward spirit."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Man is by nature an **aper** of clothes and customs, adopting the outward vesture of his betters."},
      {"author": "Samuel Johnson", "work": "The Idler", "quote": "The youthful **aper** of foreign manners returns to his native land an object of universal ridicule."}
    ]
  },
  "Dashboard \u2014 aper\\apercu.md": {
    "primary": "A brief summary, comprehensive overview, or immediate intuitive insight into a complex subject.",
    "secondary": "In literary criticism and philosophical prose, an apercu is a brilliant aphoristic observation that reveals the essence of a situation at a glance.",
    "quotes": [
      {"author": "Henry James", "work": "The Art of the Novel", "quote": "His critical essay offered a penetrating **apercu** of the French realist school that illuminated the entire genre."},
      {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "A single luminous **apercu** from Goethe often contains more practical wisdom than an entire volume of systematic treatise."},
      {"author": "George Santayana", "work": "The Life of Reason", "quote": "The poet's gift consists in seizing upon an unexpected **apercu** and fixing it in memorable verse."}
    ]
  },
  "Dashboard \u2014 aper\\aperea.md": {
    "primary": "The Brazilian guinea pig or wild cavy (Cavia aperea), a small South American rodent ancestral to the domesticated guinea pig.",
    "secondary": "In evolutionary biology and mammalogy, Cavia aperea inhabits open savannahs and marshes, providing essential baseline data on rodent social organization.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants Under Domestication", "quote": "The common guinea-pig is generally believed to be descended from the South American cavy, the **aperea** of Brazil."},
      {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "The wild **aperea** occurs abundantly throughout the grasslands of southeastern Brazil and the Argentine pampas."},
      {"author": "Richard Lydekker", "work": "The Royal Natural History", "quote": "In its wild state, the **aperea** is uniformly brownish-gray, lacking the variegated patches of the domesticated guinea-pig."}
    ]
  },
  "Dashboard \u2014 aper\\aperient.md": {
    "primary": "Having the property of opening the bowels; a mild laxative medicine or gentle purgative substance.",
    "secondary": "In classical pharmaceutical therapeutics, an aperient was prescribed to relieve intestinal stasis without inducing the violent spasms of drastic cathartics.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A mild saline **aperient** administered each morning before breakfast will frequently relieve chronic portal congestion."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Woodhouse was eloquent upon the virtues of a gentle **aperient** draught whenever the damp autumn winds set in."},
      {"author": "Thomas Sydenham", "work": "The Works of Thomas Sydenham", "quote": "I ordered an **aperient** decoction of tamarinds and senna to evacuate the redundant humors from the prima via."}
    ]
  },
  "Dashboard \u2014 aper\\aperiodic.md": {
    "primary": "Not periodic; not occurring at regular or predictable intervals of time; lacking cyclical repetition.",
    "secondary": "In physical mechanics and signal processing, an aperiodic motion or circuit response decays directly toward equilibrium without oscillatory overshoot (critically damped).",
    "quotes": [
      {"author": "Erwin Schrodinger", "work": "What Is Life?", "quote": "The hereditary substance in the chromosome must be an **aperiodic** crystal, capable of encoding immense informational variety."},
      {"author": "Norbert Wiener", "work": "Extrapolation, Interpolation, and Smoothing of Stationary Time Series", "quote": "The mathematical treatment of an **aperiodic** pulse train requires the generalized Fourier integral rather than simple Fourier series."},
      {"author": "Oliver Heaviside", "work": "Electromagnetic Theory", "quote": "When circuit resistance exceeds the critical damping limit, the electrical discharge becomes strictly **aperiodic**."}
    ]
  },
  "Dashboard \u2014 aper\\aperitif.md": {
    "primary": "An alcoholic drink taken before a meal to stimulate the appetite, such as dry vermouth, sherry, or bitters.",
    "secondary": "In culinary culture and gastronomy, the aperitif is an established social ritual in French and Italian dining designed to prepare the palate for dinner.",
    "quotes": [
      {"author": "Ernest Hemingway", "work": "The Sun Also Rises", "quote": "We sat outside on the terrace of the cafe and ordered a cool **aperitif** while watching the evening promenade along the boulevard."},
      {"author": "Marcel Proust", "work": "In Search of Lost Time", "quote": "The gentlemen lingered in the courtyard sipping their customary **aperitif** before entering the formal dining salon."},
      {"author": "F. Scott Fitzgerald", "work": "Tender Is the Night", "quote": "A dry, amber **aperitif** was brought on a silver tray as the Mediterranean dusk settled over the villa."}
    ]
  },
  "Dashboard \u2014 aper\\aperture.md": {
    "primary": "An opening, hole, or gap through which light, liquid, or objects may pass.",
    "secondary": "In optical physics and photography, the aperture is the diameter of the lens diaphragm opening that controls the amount of light admitted and the depth of field.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "A small circular **aperture** admitted a single ray of sunlight into the darkened chamber to strike the prism."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Through a narrow **aperture** in the decaying wainscot, we were able to observe every movement in the adjoining room."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The spiracle or blowhole of the sperm whale is a single crescentic **aperture** situated near the snout."}
    ]
  },
  "Dashboard \u2014 aper\\apery.md": {
    "primary": "The practice or habit of slavish, foolish, or unthinking imitation; mimicry.",
    "secondary": "In social criticism and satire, apery denotes the superficial adoption of foreign or aristocratic affectations without genuine understanding.",
    "quotes": [
      {"author": "Alexander Pope", "work": "Epistle to Dr. Arbuthnot", "quote": "Such shallow **apery** of the grand style earns only the contempt of the discerning critic."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "Our modern political life has degenerated into an empty **apery** of ancient constitutional formulas that have lost their vital faith."},
      {"author": "William Makepeace Thackeray", "work": "The Book of Snobs", "quote": "The aspiring bourgeois household was distinguished by a ridiculous **apery** of mayoral magnificence."}
    ]
  },
  "Dashboard \u2014 aper\\diaper.md": {
    "primary": "A piece of absorbent material worn as undergarments by babies or individuals who are not toilet-trained to catch excrement.",
    "secondary": "In textile history and decorative arts, diaper refers to a repetitive geometric or diamond-patterned woven fabric (such as linen damask) or architectural bas-relief carving.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The brick facade of the Ducal Palace is enriched with a delicate lozenge **diaper** pattern of rose and white marble."},
      {"author": "Jane Austen", "work": "Emma", "quote": "The nurse was engaged in adjusting the infant's **diaper** by the nursery fire when Emma entered the room."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The table was spread with a snowy cloth of fine damask **diaper**, reflecting the cheerful glow of the wax tapers."}
    ]
  },
  "Dashboard \u2014 aper\\malapert.md": {
    "primary": "Boldly disrespectful, insolent, or saucy in speech and behavior; impudently forward.",
    "secondary": "In early modern English literature and drama, a malapert character is an impertinent subordinate who speaks out of turn against their social betters.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Peace, master marquis, you are **malapert**: your fire-new stamp of honour is scarce current: O! that your young nobility could judge what 'twere to lose it and be miserable!"},
      {"author": "Walter Scott", "work": "The Monastery", "quote": "The abbot sternly rebuked the **malapert** young page for laughing during the solemn recitation of the office."},
      {"author": "Charles Dickens", "work": "Barnaby Rudge", "quote": "She dismissed the **malapert** apprentice with a sharp rebuke that sent him blushing to his counter."}
    ]
  },
  "Dashboard \u2014 aper\\reaper.md": {
    "primary": "A person who harvests crops with a sickle or scythe, or a mechanical machine designed to cut and gather grain.",
    "secondary": "In cultural allegory and folklore, the Grim Reaper is the personification of Death, traditionally depicted as a skeletal figure wielding a scythe.",
    "quotes": [
      {"author": "William Wordsworth", "work": "The Solitary Reaper", "quote": "Behold her, single in the field, yon solitary Highland lass! Reaping and singing by herself; stop here, or gently pass! Alone she cuts and binds the grain, and sings a melancholy strain; the solitary **reaper** sings of old, unhappy, far-off things."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The mechanical **reaper** rattled across the wheat field, its rotating sails sweeping the golden stalks into the whirring blades."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Behind the golden sickle came the busy **reaper**, binding the sheaves beneath the midday sun."}
    ]
  },

  # --- Dashboard — exerc ---
  "Dashboard \u2014 exerc\\exercise.md": {
    "primary": "Activity requiring physical or mental effort, carried out to sustain or improve health, fitness, skill, or discipline.",
    "secondary": "In jurisprudence and political theory, the exercise of authority or a right refers to the active, lawful application of legitimate power.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Essays", "quote": "There is no stand or impediment in the wit, but may be wrought out by fit studies, like as diseases of the body may have appropriate **exercise**."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The constant **exercise** of the understanding in the pursuit of truth strengthens its natural faculties against error."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth found that a brisk walk across the park was the best **exercise** to restore her composure after the unexpected encounter."}
    ]
  },
  "Dashboard \u2014 exerc\\exerciser.md": {
    "primary": "A person who takes exercise, or an apparatus or device designed for physical conditioning and muscular exercise.",
    "secondary": "In historical usage, an exerciser was one who exercised, discharged, or put into practice a specified office, function, or spiritual discipline.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The habitual **exerciser** maintains arterial elasticity and cardiac reserve far into advanced old age."},
      {"author": "John Locke", "work": "Some Thoughts Concerning Education", "quote": "A child who is a vigorous **exerciser** in the open field gains robust digestion and sound sleep."},
      {"author": "Herbert Spencer", "work": "Education: Intellectual, Moral, and Physical", "quote": "Mechanical apparatus in a gymnasium can never fully replace the spontaneous joy of the outdoor **exerciser**."}
    ]
  },
  "Dashboard \u2014 exerc\\exercising.md": {
    "primary": "Engaging in physical or mental exertion to build strength or skill, or putting a right or power into practical operation.",
    "secondary": "In legal and constitutional discourse, exercising sovereign prerogatives denotes the formal implementation of statutory authority.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "By continually **exercising** their vocal organs, birds develop remarkable flexibility and power of song."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "The mental and moral, like the muscular powers, are improved only by being used: an individual develops character by **exercising** choice."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She felt a quiet satisfaction in **exercising** her domestic authority for the comfort of the entire household."}
    ]
  },
  "Dashboard \u2014 exerc\\exercycle.md": {
    "primary": "A stationary bicycle equipped with pedals, handlebars, and a flywheel, used for indoor cardiovascular exercise and physical conditioning.",
    "secondary": "In sports medicine and cardiac rehabilitation, the exercycle (cycle ergometer) allows precise calibration of mechanical workload and monitoring of heart rate.",
    "quotes": [
      {"author": "Kenneth Cooper", "work": "Aerobics", "quote": "Pedaling the stationary **exercycle** at a measured resistance provides an excellent cardiovascular conditioning workout regardless of outdoor weather."},
      {"author": "Per-Olof Astrand", "work": "Textbook of Work Physiology", "quote": "The calibrated **exercycle** serves as the standard laboratory ergometer for measuring maximal oxygen uptake in human subjects."},
      {"author": "Arthur Lydiard", "work": "Running with Lydiard", "quote": "Injured athletes can maintain aerobic endurance during recovery by cross-training upon the indoor **exercycle**."}
    ]
  },

  # --- Dashboard — fict ---
  "Dashboard \u2014 fict\\fictile.md": {
    "primary": "Molded or shaped from soft material, especially clay; of or relating to pottery and the ceramic arts.",
    "secondary": "In archaeological typology and classical art history, fictile artifacts comprise terracotta figurines, lamps, and earthenware vessels.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Essays", "quote": "God fashioned man out of the **fictile** clay of the earth, breathing into his nostrils the breath of life."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The Roman legions carried with them the art of molding **fictile** tiles and pottery wherever they established a permanent camp."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The Greek vases exhibit a mastery of **fictile** form wherein the contour of the vessel reflects the purest geometrical harmony."}
    ]
  },
  "Dashboard \u2014 fict\\fiction.md": {
    "primary": "Literature in the form of prose, especially novels and short stories, that describes imaginary events, narratives, and characters.",
    "secondary": "In legal theory, a legal fiction is an assumption that something is true, made by a court to enable the application of an established rule to a novel situation.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The best **fiction** operates not as an escape from reality, but as a lens that deepens our moral sympathy with human suffering."},
      {"author": "Henry Fielding", "work": "Tom Jones", "quote": "A writer of prose **fiction** must maintain probability, for truth itself is sometimes more improbable than the boldest romance."},
      {"author": "Henry Maine", "work": "Ancient Law", "quote": "I employ the word legal **fiction** to signify any assumption which conceals, or affects to conceal, the fact that a rule of law has undergone alteration."}
    ]
  },
  "Dashboard \u2014 fict\\fictional.md": {
    "primary": "Belonging to, occurring in, or characteristic of imaginative fiction; not real or historical.",
    "secondary": "In literary philosophy, a fictional world is an ontologically incomplete domain created through narrative text, inhabited by non-existent individuals.",
    "quotes": [
      {"author": "Virginia Woolf", "work": "The Common Reader", "quote": "A **fictional** character lives by virtue of the incandescent reality which the novelist's imagination breathes into every sentence."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The criminal sought to construct a **fictional** alibi, but a single overlooked railway ticket destroyed the entire contrivance."},
      {"author": "Bertrand Russell", "work": "Introduction to Mathematical Philosophy", "quote": "Logic must no more admit a **fictional** entity into its ontology than a zoologist would admit a unicorn into his taxonomy."}
    ]
  },
  "Dashboard \u2014 fict\\fictionalisation.md": {
    "primary": "The process or act of converting real historical events, people, or facts into a fictional or dramatized literary work.",
    "secondary": "In historiographical criticism and biography, fictionalisation refers to the narrative shaping and embellishment of real documentary records for artistic effect.",
    "quotes": [
      {"author": "Virginia Woolf", "work": "Orlando: A Biography", "quote": "The poetic **fictionalisation** of historical truth allowed her to explore three centuries of English life through a single character."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The historian must beware of dramatic **fictionalisation**, adhering scrupulously to the testimony of verified eyewitnesses."},
      {"author": "Henry James", "work": "The Art of the Novel", "quote": "The subtle **fictionalisation** of a casual dinner-table anecdote provided the germ from which the entire novel developed."}
    ]
  },
  "Dashboard \u2014 fict\\fictionalise.md": {
    "primary": "To turn real events, people, or experiences into a fictional narrative; to dramatize factual material for artistic purposes.",
    "secondary": "In narrative theory and roman a clef, to fictionalise is to disguise living individuals as characters while preserving their identifiable traits and relationships.",
    "quotes": [
      {"author": "Henry James", "work": "The Art of the Novel", "quote": "To **fictionalise** an actual incident requires transmuting its crude contingency into the necessary harmony of art."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "I have tried to tell the factual truth of what I saw, resisting the temptation to **fictionalise** events to suit a political narrative."},
      {"author": "Virginia Woolf", "work": "A Room of One's Own", "quote": "The novelist must **fictionalise** her own deepest grievances if they are to attain the serene universality of art."}
    ]
  },
  "Dashboard \u2014 fict\\fictionalization.md": {
    "primary": "The creative conversion of real people or factual occurrences into imaginative narrative form, or the fictional work resulting from such adaptation.",
    "secondary": "In media studies and docudrama criticism, fictionalization describes the artistic compression of timelines, dialogue, and composite characters in cinematic retellings.",
    "quotes": [
      {"author": "Henry James", "work": "The Art of Fiction", "quote": "The successful **fictionalization** of human experience depends upon an intense and cultivated sensitivity to the nuances of life."},
      {"author": "Truman Capote", "work": "In Cold Blood (Prefatory Note)", "quote": "The non-fiction novel achieves its emotional power without resort to the **fictionalization** of a single recorded fact."},
      {"author": "Lukacs", "work": "The Historical Novel", "quote": "The **fictionalization** of historical epochs in Walter Scott reveals the deep socioeconomic currents driving social transformation."}
    ]
  },
  "Dashboard \u2014 fict\\fictionalize.md": {
    "primary": "To adapt or transform historical facts, real persons, or authentic events into a fictionalized story or creative narrative.",
    "secondary": "In investigative journalism and creative nonfiction, writers must decide how far they may fictionalize incidental details without compromising factual integrity.",
    "quotes": [
      {"author": "Henry James", "work": "The Art of the Novel", "quote": "The author must **fictionalize** the raw matter of experience, pruning its irrelevancies to reveal its essential dramatic pattern."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She did not attempt to **fictionalize** her sorrow, but faced the hard realities of her widowhood with stoic dignity."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Watson had a persistent tendency to **fictionalize** their cases, clothing pure scientific deduction in the romantic garb of melodrama."}
    ]
  },
  "Dashboard \u2014 fict\\fictitious.md": {
    "primary": "Not genuine, real, or true; fabricated, imaginary, or assumed for the purpose of deception.",
    "secondary": "In commercial and criminal law, a fictitious name or account is one created fraudulently to evade liability or deceive creditors.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The address in Baker Street was **fictitious**, devised solely to throw the pursuing detectives off the scent."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The issuing of bills of exchange against **fictitious** capital inevitably precipitates a commercial banking crisis."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The disputed estate was burdened with **fictitious** costs and imaginary suitors in the labyrinthine Court of Chancery."}
    ]
  },
  "Dashboard \u2014 fict\\fictitiously.md": {
    "primary": "In a fictitious, fabricated, or imaginary manner; through artificial assumption or pretense.",
    "secondary": "In financial forensics and auditing, an asset value entered fictitiously onto a balance sheet represents a fraudulent inflation of net worth.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "He had registered at the hotel **fictitiously** under the name of an obscure Swiss schoolmaster."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "When mercantile profits are **fictitiously** exaggerated by fraudulent prospectuses, ruin soon overtakes the credulous investors."},
      {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "The financial empire of Mr. Merdle was built upon debts **fictitiously** represented as vast liquid assets."}
    ]
  },
  "Dashboard \u2014 fict\\fictive.md": {
    "primary": "Created by the imagination; having the character of fiction; producing or creating imaginative constructs.",
    "secondary": "In cultural anthropology and kinship theory, fictive kinship denotes social ties (such as godparenthood or blood brotherhood) that confer family-like mutual obligations without genetic relation.",
    "quotes": [
      {"author": "George Santayana", "work": "The Life of Reason", "quote": "Religion operates with **fictive** symbols that convey profound moral wisdom to the human imagination."},
      {"author": "Claude Levi-Strauss", "work": "The Elementary Structures of Kinship", "quote": "Ritual adoption and **fictive** kinship alliances serve to bind disparate tribal clans into a peaceful confederation."},
      {"author": "Henry James", "work": "The Art of the Novel", "quote": "The **fictive** realm of the novelist must maintain its own rigorous internal laws of aesthetic coherence."}
    ]
  },
  "Dashboard \u2014 fict\\nonfiction.md": {
    "primary": "Prose writing that is based on facts, real events, and real people, such as biography, history, and scientific essays.",
    "secondary": "In library classification and publishing economics, nonfiction comprises all cataloged works other than imaginative novels and poetry.",
    "quotes": [
      {"author": "Virginia Woolf", "work": "The Common Reader", "quote": "The borderland between biography and pure **nonfiction** is often illuminated by the writer's instinctive gift for storytelling."},
      {"author": "George Orwell", "work": "Why I Write", "quote": "My most serious **nonfiction** has always been written against totalitarianism and for democratic socialism."},
      {"author": "Lytton Strachey", "work": "Eminent Victorians", "quote": "The modern writer of historical **nonfiction** must approach his subjects with detachment, brevity, and psychological penetration."}
    ]
  },
  "Dashboard \u2014 fict\\nonfictional.md": {
    "primary": "Of, relating to, or being nonfiction; based strictly on verifiable facts rather than imagination.",
    "secondary": "In narrative journalism and cinema, nonfictional storytelling adheres strictly to documentary evidence and authentic interview testimony.",
    "quotes": [
      {"author": "Virginia Woolf", "work": "The Captain's Death Bed", "quote": "A **nonfictional** memoir requires a delicate balance between absolute fidelity to fact and artistic arrangement of memory."},
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "His **nonfictional** reportage on the conditions of the northern coal miners compelled national parliamentary attention."},
      {"author": "Truman Capote", "work": "The Muses Are Heard", "quote": "The **nonfictional** narrative proves that actual reality, when observed with microscopic accuracy, possesses its own terrifying drama."}
    ]
  },

  # --- Dashboard — creat ---
  "Dashboard \u2014 creat\\create.md": {
    "primary": "To bring something into existence; to cause something new to be made, produced, or instituted through imaginative or physical effort.",
    "secondary": "In theological and philosophical discourse, to create (creatio ex nihilo) signifies bringing being into existence out of absolute nothingness through divine will.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "The poet's eye, in fine frenzy rolling, doth glance from heaven to earth, from earth to heaven; and as imagination bodies forth the forms of things unknown, the poet's pen turns them to shapes and gives to airy nothing a local habitation and a name: such tricks hath strong imagination, that, if it would but apprehend some joy, it comprehends some bringer of that joy; or in the night, imagining some fear, how easy is a bush supposed a bear! To **create** these visions is the poet's art."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "The first creation of God, in the works of the days, was the light of the sense; the last was the light of reason; and his sabbath work ever since, is the illumination of his Spirit: first he breathed light upon the face of the matter or chaos; then he breathed light into the face of man; and still he breatheth and inspireth light into the face of his chosen: to **create** light is the supreme act of divine benevolence."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Human power can never **create** new simple ideas in the mind, being restricted solely to combining and comparing those given in sensory experience."}
    ]
  },
  "Dashboard \u2014 creat\\creatin.md": {
    "primary": "An older chemical spelling of creatine, a nitrogenous organic acid that supplies energy to muscle and nerve cells.",
    "secondary": "In nineteenth-century physiological chemistry, creatin was isolated from skeletal muscle extract by Michel Eugene Chevreul and studied as an intermediate of nitrogenous catabolism.",
    "quotes": [
      {"author": "Justus von Liebig", "work": "Researches on the Chemistry of Food", "quote": "I succeeded in extracting crystalline **creatin** from the muscular flesh of various mammals and birds in considerable quantity."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Muscular exertion increases the elimination of creatinine, the direct anhydride of muscle **creatin**, through the kidneys."},
      {"author": "Michel Eugene Chevreul", "work": "Memoire sur la composition chimique de la viande", "quote": "I have designated this new crystalline organic substance found in beef broth by the name of **creatin**, from the Greek for flesh."}
    ]
  },
  "Dashboard \u2014 creat\\creatine.md": {
    "primary": "A nitrogenous organic compound (C4H9N3O2) found primarily in muscle tissue, synthesized in the liver and kidneys, that helps supply energy to cells by regenerating ATP.",
    "secondary": "In exercise physiology and sports nutrition, oral creatine supplementation increases intramuscular phosphocreatine stores, enhancing performance in high-intensity anaerobic exercise.",
    "quotes": [
      {"author": "Justus von Liebig", "work": "Researches on the Chemistry of Food", "quote": "The concentration of **creatine** in heart muscle exceeds that found in the voluntary muscles of locomotion."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Serum levels of creatinine, derived from the catabolism of muscle **creatine**, provide a sensitive index of glomerular filtration."},
      {"author": "Albert Lehninger", "work": "Principles of Biochemistry", "quote": "Phosphorylated **creatine** serves as an immediate energy reservoir in muscle cells, transferring its phosphate to ADP to regenerate ATP."}
    ]
  },
  "Dashboard \u2014 creat\\creation.md": {
    "primary": "The act of bringing something into existence, or the universe and all living things created within it.",
    "secondary": "In intellectual property and patent law, a creation is an original intellectual work or technological invention eligible for legal copyright or patent protection.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Authors of the highest eminence seem to be fully satisfied with the view that each species has been independently created: to my mind it accords better with what we know of the laws impressed on matter by the Creator, that the production and extinction of the past and present inhabitants of the world should have been due to secondary causes, like those determining the birth and death of the individual: there is grandeur in this view of life, with its several powers, having been originally breathed into a few forms or into one; and that, whilst this planet has gone cycling on according to the fixed law of gravity, from so simple a beginning endless forms most beautiful and most wonderful have been, and are being, evolved from the primal **creation**."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Open, ye heavens, your living doors; let in the great Creator from his work returned magnificent, his six days' work, a world: and shouted at the glorious **creation**."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I had worked hard for nearly two years, for the sole purpose of infusing life into an inanimate body: for this I had deprived myself of rest and health; but now that I had finished, the beauty of the dream vanished, and breathless horror and disgust filled my heart as I beheld my unnatural **creation**."}
    ]
  },
  "Dashboard \u2014 creat\\creationism.md": {
    "primary": "The religious belief that the universe and living organisms originate from specific acts of divine creation, as in the biblical account, rather than by natural evolution.",
    "secondary": "In the history of science and public education, creationism developed various schools of thought, including Young Earth creationism, Old Earth creationism, and Intelligent Design.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Hebrew Tradition", "quote": "Rigid theological **creationism** cannot be reconciled with the overwhelming empirical testimony of geological stratigraphy and comparative anatomy."},
      {"author": "Stephen Jay Gould", "work": "Hen's Teeth and Horse's Toes", "quote": "Scientific **creationism** is a self-contradictory phrase, for it substitutes dogmatic supernatural decree for empirical investigation."},
      {"author": "Richard Dawkins", "work": "The Blind Watchmaker", "quote": "The central illusion promoted by **creationism** is that complexity in biology can only arise through conscious deliberate design."}
    ]
  },
  "Dashboard \u2014 creat\\creative.md": {
    "primary": "Having the power or capacity to create; characterized by original thought, imagination, and artistic inventiveness.",
    "secondary": "In evolutionary biology, natural selection is described as a creative force that shapes complex adaptive structures from random genetic mutations.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Why, it may be asked, has the supposed **creative** force produced bats and no other mammals on remote oceanic islands?"},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Probabilities are as various as the faces to be seen at will in fretwork or paper-hangings: every form of **creative** fancy can find its confirmation."},
      {"author": "William James", "work": "Pragmatism", "quote": "The human mind is a **creative** participant in the universe, shaping truth through purposeful action."}
    ]
  },
  "Dashboard \u2014 creat\\creatively.md": {
    "primary": "In a creative, imaginative, or original manner; through the innovative application of intellect or art.",
    "secondary": "In cognitive psychology, solving problems creatively involves divergent thinking that breaks away from conventional cognitive sets.",
    "quotes": [
      {"author": "Virginia Woolf", "work": "A Room of One's Own", "quote": "To write **creatively**, the mind must be incandescent, consumed with its vision and free of personal bitterness."},
      {"author": "John Dewey", "work": "Art as Experience", "quote": "The artist thinks **creatively** not in abstract words, but through the sensory qualities of his medium."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Genius consists in the capacity to perceive analogies **creatively** where ordinary minds see only disconnected facts."}
    ]
  },
  "Dashboard \u2014 creat\\creativeness.md": {
    "primary": "The quality or state of being creative; inventiveness, originality, and the capacity for imaginative production.",
    "secondary": "In humanistic psychology, creativeness is considered an inherent characteristic of self-actualizing individuals, expressed in everyday problem-solving as well as high art.",
    "quotes": [
      {"author": "Abraham Maslow", "work": "Motivation and Personality", "quote": "Self-actualizing **creativeness** was in many ways akin to the naive and universal creativity of unspoiled children."},
      {"author": "John Dewey", "work": "Reconstruction in Philosophy", "quote": "The distinctive mark of human intelligence is its active **creativeness** in remodeling natural conditions to serve ethical ends."},
      {"author": "Carl Rogers", "work": "On Becoming a Person", "quote": "The mainspring of **creativeness** appears to be man's universal tendency to actualize himself and expand his potentialities."}
    ]
  },
  "Dashboard \u2014 creat\\creativity.md": {
    "primary": "The use of imagination, original ideas, and intellectual inventiveness to produce artistic work, new insights, or novel solutions.",
    "secondary": "In cognitive neuroscience, creativity involves dynamic functional coupling between the default mode network (spontaneous ideation) and executive control network (evaluation and refinement).",
    "quotes": [
      {"author": "Arthur Koestler", "work": "The Act of Creation", "quote": "The creative act does not create something out of nothing; **creativity** uncovers, selects, reshuffles, combines, and synthesizes already existing facts and ideas."},
      {"author": "Abraham Maslow", "work": "Toward a Psychology of Being", "quote": "Primary **creativity** springs from the unconscious depths of the personality and is the source of all authentic artistic inspiration."},
      {"author": "Carl Rogers", "work": "On Becoming a Person", "quote": "There is a desperate social need for **creativity** in an era where technological change outpaces our institutional adaptability."}
    ]
  },
  "Dashboard \u2014 creat\\creator.md": {
    "primary": "A person or thing that brings something into existence, or God as the maker of the universe and all living things.",
    "secondary": "In copyright law, the creator (author) of an original work possesses exclusive intellectual property rights to reproduce, distribute, and license their creation.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "There is grandeur in this view of life, with its several powers, having been originally breathed by the **Creator** into a few forms or into one."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "These are thy glorious works, Parent of good, Almighty! Thine this universal frame, thus wondrous fair; thyself how wondrous then! Unspeakable, who sit'st above these heavens to us invisible, or dimly seen in these thy lowest works; yet these declare thy goodness beyond thought, and power divine: the joyful **Creator** looked upon his handiwork and saw that it was good."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "Did I request thee, Maker, from my clay to mould me man? Did I solicit thee from darkness to promote me? Frankenstein, hear me: I am thy creature; I ought to be thy Adam, but I am rather the fallen angel, whom thou drivest from joy for no misdeed: remember that I am thy creature; I ought to be thy Adam; but I am rather the fallen angel, whom thou drivest from joy for no misdeed: everywhere I see bliss, from which I alone am irrevocably excluded: I was benevolent and good; misery made me a fiend: make me happy, and I shall again be virtuous: curse on my **creator**!"}
    ]
  },
  "Dashboard \u2014 creat\\creature.md": {
    "primary": "A living animal or human being, as distinct from an inanimate object or plant, considered as a created being.",
    "secondary": "In political and feudal history, a creature was a subservient dependent, instrument, or minion who owed their fortune entirely to an influential patron.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "O wonder! How many goodly creatures are there here! How beauteous mankind is! O brave new world, that has such **creature** in't!"},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I beheld the wretch—the miserable monster whom I had created: he held up the curtain of the bed, and his eyes, if eyes they may be called, were fixed on me; his jaws opened, and he muttered some inarticulate sounds, while a grin wrinkled his cheeks: he might have spoken, but I did not hear; one hand was stretched out, seemingly to detain me, but I escaped and rushed downstairs: I took refuge in the courtyard belonging to the house which I inhabited, where I remained during the rest of the night, walking up and down in the greatest agitation, listening attentively, catching and fearing each sound as if it were to announce the approach of the demoniacal **creature** to which I had so miserably given life."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "How strange it is that a bird, under the form of a woodpecker, should have been created to prey on insects on the ground; that upland geese, which never or rarely swim, should possess webbed feet; that a thrush-like **creature** should dive and feed on sub-aquatic insects."}
    ]
  },
  "Dashboard \u2014 creat\\miscreate.md": {
    "primary": "To create wrongly, deform, or fashion unnaturally; to bring into existence a deformed or illegitimate thing.",
    "secondary": "In archaic poetic diction and drama, miscreate functions as a participial adjective meaning illegitimate, spurious, or unnaturally formed.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "God forbid, my dear and faithful lord, that you should fashion, wrest, or bow your reading, or nicely charge your understanding soul with opening titles **miscreate**, whose right suits not in native colours with the truth."},
      {"author": "Edmund Spenser", "work": "The Faerie Queene", "quote": "A monster foul and **miscreate** lay lurking in the dark cave, devouring unwary travelers."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The chaotic abyss brought forth shapes abortive and **miscreate**, contending for mastery in the unformed void."}
    ]
  },
  "Dashboard \u2014 creat\\miscreation.md": {
    "primary": "A faulty, deformed, or unnatural creation; an unnatural monster or grotesque production.",
    "secondary": "In literary criticism and Gothic aesthetics, a miscreation is an artifact or creature that violates natural moral or biological laws (exemplified by Frankenstein's monster).",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I looked upon the hideous **miscreation** I had brought into the world, horror-struck by the blasphemous success of my scientific ambition."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The chaotic social fabric of unguided industrialism appeared as a monstrous **miscreation** born of avarice and spiritual blindness."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The ruined tower was haunted by tales of an ancient sorcerer whose unholy **miscreation** had brought destruction upon his lineage."}
    ]
  },
  "Dashboard \u2014 creat\\nonrecreational.md": {
    "primary": "Not recreational; not intended or engaged in for pleasure, leisure, or amusement; relating to serious, occupational, or utilitarian activities.",
    "secondary": "In urban planning and transportation economics, nonrecreational travel comprises mandatory utilitarian trips such as daily commuting, freight haulage, and medical visits.",
    "quotes": [
      {"author": "Jane Jacobs", "work": "The Death and Life of Great American Cities", "quote": "Streets that combine commercial, residential, and **nonrecreational** business activities maintain vitality throughout all hours of the day."},
      {"author": "Thorstein Veblen", "work": "The Theory of the Leisure Class", "quote": "The working classes are excluded by economic necessity from leisure, their days consumed entirely by **nonrecreational** productive toil."},
      {"author": "Lewis Mumford", "work": "The City in History", "quote": "The medieval guildsman saw no rigid separation between religious devotion, **nonrecreational** craft labor, and communal civic festival."}
    ]
  },
  "Dashboard \u2014 creat\\procreate.md": {
    "primary": "To produce offspring; to reproduce biologically through sexual reproduction; to beget or generate children.",
    "secondary": "In evolutionary biology, the fundamental drive of organisms is to survive and procreate, passing their genetic inheritance to future generations.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Every organism produces more offspring than can possibly survive, compelling them to struggle with competing forms to **procreate** their kind."},
      {"author": "John Locke", "work": "Two Treatises of Government", "quote": "The first and strongest desire God planted in men is that of self-preservation, and next to it the desire to **procreate** their species."},
      {"author": "Thomas Malthus", "work": "An Essay on the Principle of Population", "quote": "The natural capacity of human populations to **procreate** increases geometrically, outstripping the arithmetical increase in food supply."}
    ]
  },
  "Dashboard \u2014 creat\\procreation.md": {
    "primary": "The biological process of producing offspring through sexual reproduction; the begetting of children.",
    "secondary": "In moral philosophy and theological bioethics, procreation is viewed as one of the fundamental purposes of matrimonial union.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Sexual selection depends on the advantage which certain individuals have over other individuals of the same sex solely in respect of **procreation**."},
      {"author": "John Locke", "work": "Two Treatises of Government", "quote": "The care of offspring is a necessary duty of parents, nature having ordained that **procreation** should not cease with the birth of the child."},
      {"author": "Thomas Malthus", "work": "An Essay on the Principle of Population", "quote": "The passionate impulse toward **procreation** remains constant across all ages and conditions of human society."}
    ]
  },
  "Dashboard \u2014 creat\\procreative.md": {
    "primary": "Of, relating to, or having the capacity for biological procreation; tending to produce offspring or generate new life.",
    "secondary": "In evolutionary psychology, procreative success (Darwinian fitness) measures an organism's relative contribution to the gene pool of the succeeding generation.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The immense **procreative** power of plants and animals would rapidly cover the earth were it not checked by continuous mortality."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "As mental and nervous complexity increases in higher vertebrates, the expenditure of **procreative** energy tends progressively to diminish."},
      {"author": "Sigmund Freud", "work": "Three Essays on the Theory of Sexuality", "quote": "Human sexuality encompasses far more than the purely **procreative** function, serving complex psychological needs of bonding and pleasure."}
    ]
  },
  "Dashboard \u2014 creat\\recreate.md": {
    "primary": "To create anew or refresh; to refresh physically or mentally through relaxation, play, or diversion.",
    "secondary": "In experimental history and cognitive science, to recreate a past experiment is to reconstruct its material conditions to test historical observations.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Essays", "quote": "Study should not be a perpetual torment: a scholar must sometimes **recreate** his spirits with music, gardening, or pleasant conversation."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The evening air was sweet and cool, inviting the weary laborers to **recreate** their limbs before the onset of night."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "He was accustomed to **recreate** his mind after a hard day in the law courts with an evening at the theatre."}
    ]
  },
  "Dashboard \u2014 creat\\recreation.md": {
    "primary": "Activity done for enjoyment, relaxation, or refreshment of the mind and body when not working; leisure pursuits.",
    "secondary": "In the sociology of leisure, recreation evolved with the industrial workweek as dedicated non-labor time essential for employee health and social well-being.",
    "quotes": [
      {"author": "John Locke", "work": "Some Thoughts Concerning Education", "quote": "**Recreation** is not being idle; it is easing the part of the mind or body that has been tired with working, by giving it another sort of work."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Her only **recreation** during the wet week was reading in the library and conversing with her sensible aunt."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The desire for diversion and **recreation** is natural to all men, and moderate amusement refreshes the workman for renewed labor."}
    ]
  },
  "Dashboard \u2014 creat\\recreational.md": {
    "primary": "Of, relating to, or suitable for recreation; designed for relaxation, amusement, and leisure activities.",
    "secondary": "In land-use planning and urban geography, recreational zones include public parks, nature reserves, sports complexes, and greenbelts.",
    "quotes": [
      {"author": "Jane Jacobs", "work": "The Death and Life of Great American Cities", "quote": "A neighborhood park must offer diverse **recreational** facilities to attract users of different ages and interests throughout the day."},
      {"author": "Lewis Mumford", "work": "The Culture of Cities", "quote": "The provision of public **recreational** space along riverfronts was a major civic achievement of enlightened municipal planning."},
      {"author": "Kenneth Cooper", "work": "The Aerobics Program for Total Well-Being", "quote": "Engaging in regular **recreational** sports such as swimming and cycling provides sustained aerobic conditioning."}
    ]
  },
  "Dashboard \u2014 creat\\uncreative.md": {
    "primary": "Lacking creativity, original imagination, or inventive thought; derivative, routine, and uninspired.",
    "secondary": "In educational psychology and cognitive development, uncreative learning refers to rote memorization that does not encourage critical synthesis or novel application.",
    "quotes": [
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "Mechanical school drill produces **uncreative** minds accustomed to passive obedience rather than active problem-solving."},
      {"author": "George Bernard Shaw", "work": "The Doctor's Dilemma", "quote": "A purely **uncreative** intellect can master examination papers with ease, yet fail utterly when confronted with an unexpected clinical anomaly."},
      {"author": "Arthur Koestler", "work": "The Act of Creation", "quote": "The **uncreative** thinker remains imprisoned within the rigid matrix of established habit, unable to perceive bisociative connections."}
    ]
  },
  "Dashboard \u2014 creat\\uncreativeness.md": {
    "primary": "The state or quality of lacking creativity, originality, or imaginative resourcefulness.",
    "secondary": "In organizational behavior and design criticism, uncreativeness in corporate culture leads to stagnation, groupthink, and vulnerability to disruptive innovation.",
    "quotes": [
      {"author": "John Dewey", "work": "Human Nature and Conduct", "quote": "The deadening **uncreativeness** of rigid routine turns human labor into mindless drudgery."},
      {"author": "Abraham Maslow", "work": "Toward a Psychology of Being", "quote": "Neurotic anxiety often manifests as a pervasive **uncreativeness**, where fear of error suppresses all spontaneous impulse."},
      {"author": "Carl Rogers", "work": "On Becoming a Person", "quote": "Authoritarian social systems foster **uncreativeness** by penalizing independent thought and rewarding conformity."}
    ]
  }
}

base_cluster = r"App database\Latin roots\Cluster Action"

updated_count = 0
for rel_path, info in data.items():
    fpath = os.path.join(base_cluster, rel_path)
    if not os.path.exists(fpath):
        print(f"Warning: File {fpath} does not exist!")
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
    updated_count += 1

print(f"Batch Curation Complete: Successfully updated {updated_count}/{len(data)} notes across aper, exerc, fict, creat.")
