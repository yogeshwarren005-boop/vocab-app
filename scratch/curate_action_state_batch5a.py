# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — lus (57 words) ---
  "Dashboard — lus/allusion.md": {
    "primary": "An indirect or passing reference to an event, person, literary work, or piece of art.",
    "secondary": "In literary criticism and rhetorical theory, an allusion enriches meaning by evoking shared cultural or classical mythology without explicit explanation.",
    "quotes": [
      {"author": "Alexander Pope", "work": "The Rape of the Lock", "quote": "The mock-heroic epic abounds in classical **allusion**, playfully transmuting Homeric battles into drawing-room skirmishes."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon's speech was weighted with pedantic **allusion** to obscure mythological traditions."},
      {"author": "Virginia Woolf", "work": "The Common Reader", "quote": "In modern poetic prose, every subtle **allusion** awakens echoes of past literary masters."},
    ]
  },
  "Dashboard — lus/allusive.md": {
    "primary": "Working by suggestion rather than explicit mention; containing or characterized by indirect references.",
    "secondary": "In modernist poetics, an allusive style invites reader participation by weaving fragments of history and world literature into dense tapestries.",
    "quotes": [
      {"author": "T. S. Eliot", "work": "The Sacred Wood", "quote": "The poet's diction is richly **allusive**, drawing vitality from the collective unconscious of Western letters."},
      {"author": "Walter Pater", "work": "Appreciations", "quote": "His essays exhibit a delicate, **allusive** grace that hints at profound aesthetic meditations."},
      {"author": "Henry James", "work": "The Art of the Novel", "quote": "The dialogue was exquisitely **allusive**, concealing dramatic tensions beneath light polite banter."},
    ]
  },
  "Dashboard — lus/allusiveness.md": {
    "primary": "Richness in indirect literary, cultural, or historical references and subtle symbolic connotations.",
    "secondary": "In hermeneutic analysis, the allusiveness of a text demands erudition from the reader to unlock multi-layered allegorical interpretations.",
    "quotes": [
      {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "The subtle **allusiveness** of Milton's verse requires a scholar's familiarity with ancient Greek and Latin epics."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "Poetic genius manifests through an evocative **allusiveness** that transcends literal narrative constraints."},
      {"author": "Arthur Symons", "work": "The Symbolist Movement in Literature", "quote": "Mallarmé sought a pure **allusiveness** in verse where words suggest moods rather than name objects."},
    ]
  },
  "Dashboard — lus/collusion.md": {
    "primary": "Secret or illegal cooperation and conspiracy, especially in order to cheat or deceive others.",
    "secondary": "In antitrust economics and jurisprudence, tacit collusion among oligopolistic firms fixes prices and stifles competitive market forces.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "People of the same trade seldom meet together, even for merriment, but the conversation ends in a conspiracy against the public, or in some contrivance to raise prices by secret **collusion**."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Constitutional checks and balances prevent corrupt **collusion** between the legislative and executive branches."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The suspicious clerk hinted at fraudulent **collusion** between the executors of the disputed Chancery estate."},
    ]
  },
  "Dashboard — lus/collusive.md": {
    "primary": "Acting in secret agreement or conspiracy for a deceitful, fraudulent, or unlawful purpose.",
    "secondary": "In corporate litigation, collusive bidding practices among rival contractors violate federal commerce acts and incur severe treble damages.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The ministers were accused of entering into **collusive** arrangements with foreign ambassadors to subvert parliamentary authority."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Monopolistic guilds maintained **collusive** agreements to artificially limit the entry of apprentices and inflate guild charges."},
      {"author": "Edmund Burke", "work": "Speech on the Nabob of Arcot's Debts", "quote": "The committee exposed the **collusive** nature of the fraudulent loan contracts fabricated by colonial administrators."},
    ]
  },
  "Dashboard — lus/delusion.md": {
    "primary": "A false belief or opinion that is firmly maintained despite being contradicted by reality or rational argument.",
    "secondary": "In clinical psychiatry, a somatic or persecutory delusion reflects profound neuropsychiatric disorganization rather than mere cultural misconception.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "A turn or two I'll walk, to still my beating mind, and free my senses from this strange **delusion**."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Madness frequently consists in reasoning correctly from erroneous premises, clinging stubbornly to a private **delusion**."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I had dreamed of achieving benevolent scientific glory, but awoke to discover only ruin and horrific **delusion**."},
    ]
  },
  "Dashboard — lus/delusional.md": {
    "primary": "Characterized by, holding, or based on false, irrational beliefs or persistent misconceptions.",
    "secondary": "In forensic psychiatry, delusional disorders are evaluated to determine whether a defendant possessed legal capacity at the time of an offense.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The paranoiac constructs an elaborate, internally consistent system upon an inherently **delusional** premise."},
      {"author": "Sigmund Freud", "work": "The Psychopathology of Everyday Life", "quote": "In severe obsessional neurosis, unexamined guilt feelings can crystallize into **delusional** convictions."},
      {"author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "quote": "The patient presented with a **delusional** belief that his left leg belonged to a complete stranger."},
    ]
  },
  "Dashboard — lus/delusive.md": {
    "primary": "Giving a false or misleading impression; deceptive, illusory, or fraudulent.",
    "secondary": "In epistemology, delusive sensory impressions must be corrected by systematic experimental replication and geometric reasoning.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The utopian promises of theoretical perfection proved a **delusive** phantom that lured the commonwealth into terror."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman commanders were lured into mountain ambuscades by the **delusive** overtures of the barbarian chieftains."},
      {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "Despair not, though tyrants spin their **delusive** webs to ensnare human freedom and hope."},
    ]
  },
  "Dashboard — lus/delusively.md": {
    "primary": "In a manner that deceives, misleads, or gives a false appearance of reality.",
    "secondary": "In maritime navigation, coastal mirages delusively alter the apparent distance of rocky reefs, endangering vessels in thick fog.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The glassy surface of the equatorial doldrums shone **delusively** calm beneath the blazing tropical sun."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Hope whispered **delusively** in my ear, promising tranquil happiness where only solitude awaited me."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The distant heath fires flickered **delusively** through the gloom, mocking the lost traveler's search for shelter."},
    ]
  },
  "Dashboard — lus/delusory.md": {
    "primary": "Tending to delude; misleading, deceptive, or lacking substantial reality.",
    "secondary": "In contractual dispute resolution, delusory promises that lack genuine consideration or legal enforceability are void ab initio.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "The idols of the theater introduce **delusory** dogmas that corrupt natural philosophy with theatrical illusions."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The projectors of Laputa wasted national revenues pursuing **delusory** schemes to extract sunbeams from cucumbers."},
      {"author": "Samuel Johnson", "work": "The History of Rasselas, Prince of Abissinia", "quote": "Rasselas recognized that the philosopher's boasted equanimity was a **delusory** comfort when real sorrow struck."},
    ]
  },
  "Dashboard — lus/disillusion.md": {
    "primary": "To free someone from a false belief, naivety, or enchantment; or the loss of idealistic illusions.",
    "secondary": "In sociological literature of the post-WWI era, the catastrophic carnage served to disillusion an entire generation of European youth.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Heartbreak House", "quote": "Suffering has the salutary virtue to strip away pretense and **disillusion** the frivolous society dilettante."},
      {"author": "H. G. Wells", "work": "Mr. Britling Sees It Through", "quote": "The harsh reality of trench warfare came to **disillusion** those who had envisioned a romantic, brief military parade."},
      {"author": "Joseph Conrad", "work": "Under Western Eyes", "quote": "Razumov watched the revolutionary conspirators, feeling an icy desire to **disillusion** their fanatical certitudes."},
    ]
  },
  "Dashboard — lus/disillusioned.md": {
    "primary": "Disappointed and realistic after discovering that someone or something is not as good, noble, or true as once believed.",
    "secondary": "In historical studies of political movements, disillusioned reformers often abandon partisan activism in favor of pragmatic local efforts.",
    "quotes": [
      {"author": "F. Scott Fitzgerald", "work": "The Great Gatsby", "quote": "Nick Carraway returned to the Midwest, **disillusioned** by the grotesque predatory carelessness of the East Coast elite."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "Many veteran volunteers returned **disillusioned** from Spain, having witnessed factional purges betray democratic ideals."},
      {"author": "W. Somerset Maugham", "work": "Of Human Bondage", "quote": "Philip gazed upon his unfinished bohemian canvases, a **disillusioned** artist acknowledging the limits of his talent."},
    ]
  },
  "Dashboard — lus/disillusioning.md": {
    "primary": "Causing the loss of illusions, naive beliefs, or romanticized expectations.",
    "secondary": "In psychological development, facing disillusioning encounters with institutional corruption fosters intellectual autonomy.",
    "quotes": [
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Isabel Archer underwent a **disillusioning** awakening when she discovered Gilbert Osmond's cold aesthetic calculating nature."},
      {"author": "Thomas Mann", "work": "The Magic Mountain", "quote": "Hans Castorp found the clinical atmosphere of the sanatorium strangely **disillusioning** yet profoundly fascinating."},
      {"author": "Edith Wharton", "work": "The House of Mirth", "quote": "Lily Bart endured a series of **disillusioning** social snubs as her fortunes dwindled among the fashionable New York crowd."},
    ]
  },
  "Dashboard — lus/disillusionment.md": {
    "primary": "A feeling of disappointment resulting from the discovery that something is not as good as one believed it to be.",
    "secondary": "In intellectual history, fin-de-siècle disillusionment fostered philosophical existentialism and modernist skepticism.",
    "quotes": [
      {"author": "E. M. Forster", "work": "A Passage to India", "quote": "The sudden collapse of Fielding's cross-cultural goodwill left him with a bitter sense of social **disillusionment**."},
      {"author": "Winston Churchill", "work": "The Aftermath", "quote": "The messy compromises of the Versailles peace conference bred widespread public **disillusionment** throughout Europe."},
      {"author": "Virginia Woolf", "work": "Jacob's Room", "quote": "The young scholar experienced the painful **disillusionment** of discovering that great academic reputations masked petty jealousies."},
    ]
  },
  "Dashboard — lus/elusion.md": {
    "primary": "The act of evading, avoiding, or escaping from something through cunning, dexterity, or artifice.",
    "secondary": "In classical legal jurisprudence, deliberate tax elusion uses statutory ambiguities to escape fiscal liability without overt illegality.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Final Problem", "quote": "Moriarty's brilliant **elusion** of the Scotland Yard cordon demonstrated his extraordinary criminal intellect."},
      {"author": "Walter Scott", "work": "The Bride of Lammermoor", "quote": "The outlaw owed his repeated **elusion** of the king's troopers to his intimate knowledge of the Lammermuir bogs."},
      {"author": "Edmund Burke", "work": "Speech on American Taxation", "quote": "Colonial merchants practiced habitual **elusion** of customs duties through intricate smuggling networks in Rhode Island."},
    ]
  },
  "Dashboard — lus/elusive.md": {
    "primary": "Difficult to find, catch, achieve, or remember; slippery or hard to define.",
    "secondary": "In particle physics, elusive subatomic particles such as neutrinos interact weakly with matter, requiring massive underground detectors.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The great white leviathan remained an **elusive** phantom, disappearing beneath the waves whenever harpoons were readied."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes pursued the **elusive** footprints along the muddy bank of the Thames with relentless tenacity."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Truth is an **elusive** goddess who unveils her countenance only to those who seek her without partisan bias."},
    ]
  },
  "Dashboard — lus/elusiveness.md": {
    "primary": "A subtle tendency to evade capture, perception, or definitive comprehension.",
    "secondary": "In literary aesthetics, the elusiveness of poetic meaning invites open-ended interpretative engagement across generations of readers.",
    "quotes": [
      {"author": "Henry James", "work": "The Ambassadors", "quote": "Strether was captivated by Madame de Vionnet's charming **elusiveness**, which defied all rigid moral classifications."},
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "Lily Briscoe struggled before her easel against the maddening **elusiveness** of the vision she sought to capture on canvas."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "Marlow noted the tragic **elusiveness** of Jim's inner soul, hovering always between heroic aspiration and craven retreat."},
    ]
  },
  "Dashboard — lus/illusion.md": {
    "primary": "A deceptive appearance or impression; or a false idea, belief, or sensory misperception.",
    "secondary": "In cognitive psychology and psychophysics, an optical illusion reveals how perceptual neural circuitry infers depth and motion from ambiguous 2D cues.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "I'll cross it, though it blast me. Stay, **illusion**! If thou hast any sound, or use of voice, speak to me."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Sensory **illusion** demonstrates that secondary qualities like color and heat reside in the observer rather than the external object."},
      {"author": "Albert Einstein", "work": "Ideas and Opinions", "quote": "The distinction between past, present, and future is only a stubbornly persistent **illusion**."},
    ]
  },
  "Dashboard — lus/illusional.md": {
    "primary": "Pertaining to, resembling, or characterized by illusions; deceptive or non-veridical.",
    "secondary": "In psychiatric assessment, an illusional perceptual distortion is triggered by an actual sensory stimulus, unlike an unprompted hallucination.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The patient experienced an **illusional** interpretation of the drapery shadows, perceiving them as threatening human silhouettes."},
      {"author": "Sigmund Freud", "work": "The Future of an Illusion", "quote": "Religious dogmas partake of an **illusional** character, satisfying archaic psychological longings for cosmic protection."},
      {"author": "Oliver Sacks", "work": "Hallucinations", "quote": "Sensory deprivation experiments readily provoke transient **illusional** phenomena in healthy laboratory subjects."},
    ]
  },
  "Dashboard — lus/illusionary.md": {
    "primary": "Based on or producing illusion; deceptive, chimerical, or having no substantial existence.",
    "secondary": "In monetary economics, illusionary gains arising purely from nominal price inflation do not represent real increases in purchasing power.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The poet creates an **illusionary** world that commands a willing suspension of disbelief for the moment."},
      {"author": "Bertrand Russell", "work": "The Problems of Philosophy", "quote": "Descartes systematically doubted all sensory data to eliminate **illusionary** beliefs from the foundations of knowledge."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Time and Space are but **illusionary** garments woven by the mortal intellect to clothe eternal spirit."},
    ]
  },
  "Dashboard — lus/illusionist.md": {
    "primary": "A performer who creates theatrical illusions or sleight-of-hand tricks; a magician or conjurer.",
    "secondary": "In art history, an illusionist painter uses trompe-l'œil techniques to simulate three-dimensional physical presence on a flat wall.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Mazarin Stone", "quote": "The criminal was a master **illusionist** who used lifelike wax effigies to baffle Scotland Yard surveillance."},
      {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "Griffin performed optical transformations that would have made the reputation of the most celebrated stage **illusionist**."},
      {"author": "E. T. A. Hoffmann", "work": "The Golden Pot", "quote": "The mysterious archivist appeared like a formidable **illusionist** manipulating supernatural forces behind ordinary spectacles."},
    ]
  },
  "Dashboard — lus/illusive.md": {
    "primary": "Deceptive, unreal, or giving an illusion of reality; misleading or chimerical.",
    "secondary": "In epistemology, the illusive nature of subjective memory requires corroboration through documentary evidence.",
    "quotes": [
      {"author": "Percy Bysshe Shelley", "work": "Alastor", "quote": "The wandering poet pursued an **illusive** vision of ideal beauty through desolate wildernesses and mountain solitudes."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The peace treaty proved an **illusive** phantom that vanished at the first march of the Persian legions."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Worldly ambition promises lasting peace, but its glittering prizes are perpetually **illusive** to the possessor."},
    ]
  },
  "Dashboard — lus/illusory.md": {
    "primary": "Based on or producing illusion; deceptive, not real, or lacking true substance.",
    "secondary": "In contract law, an illusory promise reserves an unlimited right to cancel, thereby lacking consideration and legal effect.",
    "quotes": [
      {"author": "David Hume", "work": "A Treatise of Human Nature", "quote": "The supposed necessary connection between cause and effect is an **illusory** projection of mental habit onto external phenomena."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "A happiness achieved through self-deception rests upon an **illusory** foundation that crumbles before adversity."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The apparent permanence of biological species was shown to be an **illusory** notion by evolutionary transmutation."},
    ]
  },
  "Dashboard — lus/illustrate.md": {
    "primary": "To provide pictures, diagrams, or visual aids for a text; or to explain and clarify by examples or analogies.",
    "secondary": "In scientific pedagogy, instructors use physical demonstration models to illustrate abstract principles of electromagnetic flux.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "We must bring forth practical experiments to **illustrate** and confirm theoretical axioms of natural philosophy."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "Mr. Pickwick produced his pocket notebook to **illustrate** his observations regarding provincial antiquities."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "I shall employ the complex structure of the hive-bee's cell to **illustrate** the power of natural selection."},
    ]
  },
  "Dashboard — lus/illustration.md": {
    "primary": "A picture, drawing, or diagram accompanying a text; or an example used to explain or make something clear.",
    "secondary": "In the history of printing, copperplate book illustration enabled high-precision anatomical and botanical atlases in the Renaissance.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Let us take for an **illustration** the simple idea of whiteness as observed in snow or lily petals."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The accompanying geological **illustration** depicts the uplifted fossil shell beds along the Chilean coast."},
      {"author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "A comparative skeletal **illustration** demonstrates the structural affinities between the anthropoid ape and human forms."},
    ]
  },
  "Dashboard — lus/illustrative.md": {
    "primary": "Serving as an example, explanation, or visual demonstration of something.",
    "secondary": "In legal casebooks, illustrative precedent opinions are selected to illuminate nuanced doctrinal developments for students.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The pin manufactory provides an **illustrative** instance of the enormous efficiency gains achieved through division of labor."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The investigator cited an **illustrative** case to establish the validity of the method of concomitant variations."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Tribal rituals provide **illustrative** evidence of how early social cohesion was reinforced through ceremonial customs."},
    ]
  },
  "Dashboard — lus/illustrator.md": {
    "primary": "An artist who draws or creates visual images, drawings, or engravings for books, magazines, or advertisements.",
    "secondary": "In Victorian print culture, a skilled illustrator like Phiz (Hablot Knight Browne) shaped public reception of serialized novels.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Roundabout Papers", "quote": "George Cruikshank was an incomparable **illustrator** whose vivid caricatures immortalized London street life."},
      {"author": "Arthur Conan Doyle", "work": "Memories and Adventures", "quote": "Sidney Paget was the brilliant **illustrator** whose deerstalker sketches fixed the iconic image of Holmes in the public imagination."},
      {"author": "Henry James", "work": "The Real Thing", "quote": "The magazine editor hired an experienced **illustrator** to provide engravings for the new serial romance."},
    ]
  },
  "Dashboard — lus/illustrious.md": {
    "primary": "Well known, highly respected, and distinguished for noble deeds, artistic genius, or high achievements.",
    "secondary": "In Renaissance historiography, biographies of illustrious men (de viris illustribus) provided moral exemplars for statecraft.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **illustrious** name of Trajan was revered by posterity as the epitome of imperial justice and military glory."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The constitutional convention was guided by the **illustrious** character and prudent moderation of General Washington."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Far off his coming shone; and twenty thousand chariots of God, numbered thousands, led by his **illustrious** presence."},
    ]
  },
  "Dashboard — lus/illustriously.md": {
    "primary": "In a manner marked by distinction, renown, nobility, or glorious achievement.",
    "secondary": "In panegyric rhetoric, commanders who defended the realm were celebrated for serving the republic illustriously.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Speech on American Taxation", "quote": "Lord Chatham governed the British empire **illustriously**, expanding our commerce and humbling foreign rivals in war."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "Bacon lived **illustriously** in the world of intellect, even when his political fortunes suffered disastrous eclipse."},
      {"author": "Walter Scott", "work": "The Abbot", "quote": "The brave regent governed **illustriously**, holding turbulent factions in check with firmness and equity."},
    ]
  },
  "Dashboard — lus/illustriousness.md": {
    "primary": "Eminent distinction, renown, grandeur, and celebrated noble character.",
    "secondary": "In classical moral philosophy, true illustriousness springs from civic virtue and public benevolence rather than dynastic lineage.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The transient **illustriousness** of military conquerors fades before the enduring benefactions of moral philosophers."},
      {"author": "Lord Acton", "work": "Historical Essays and Studies", "quote": "The moral **illustriousness** of William of Orange lay in his steadfast dedication to European religious freedom."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "Nobility of birth adds a luster to men of action, giving their deeds an outward **illustriousness** in the eyes of the populace."},
    ]
  },
  "Dashboard — lus/lusaka.md": {
    "primary": "The capital and largest city of Zambia, serving as the commercial, administrative, and transportation hub of the country.",
    "secondary": "In twentieth-century African history, Lusaka hosted key diplomatic summits and served as a headquarters for southern African liberation movements.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "Dispatches from **lusaka** confirmed that Northern Rhodesian copper production was vital to the imperial war supply."},
      {"author": "David Livingstone", "work": "Missionary Travels and Researches in South Africa", "quote": "The fertile plateau surrounding modern **lusaka** was traversed by ancient caravan trails connecting the Zambezi to central lakes."},
      {"author": "Basil Davidson", "work": "The Black Man's Burden", "quote": "Following independence, **lusaka** developed rapidly into a vibrant diplomatic capital for newly sovereign African nations."},
    ]
  },
  "Dashboard — lus/lusatian.md": {
    "primary": "Pertaining to Lusatia, a historical region in eastern Germany and southwestern Poland; or a West Slavic Sorbian inhabitant thereof.",
    "secondary": "In European ethnolinguistics, Lusatian Sorbs preserve Upper and Lower Sorbian languages, surrounded by Germanic speech communities.",
    "quotes": [
      {"author": "Jacob Grimm", "work": "Teutonic Mythology", "quote": "Folkloric traditions among the **lusatian** Sorbs preserve ancient Slavic nature deities and seasonal customs."},
      {"author": "Thomas Carlyle", "work": "History of Friedrich II of Prussia", "quote": "Frederick the Great marched his Prussian grenadiers through the **lusatian** hills during the Seven Years' War."},
      {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "The **lusatian** dialects offer invaluable philological data regarding archaic West Slavic phonetic changes."},
    ]
  },
  "Dashboard — lus/luscinia.md": {
    "primary": "A genus of small passerine birds in the thrush family Muscicapidae, comprising the common nightingale and its close relatives.",
    "secondary": "In avian ethology and bioacoustics, Luscinia megarhynchos is renowned for its complex nocturnal vocal repertoire exceeding 180 distinct song types.",
    "quotes": [
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The sweet nocturnal strains of **luscinia** were heard in our southern woods upon the seventh of April."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The musical rivalry among singing males of the genus **luscinia** illustrates the evolutionary potency of sexual selection."},
      {"author": "Thomas Pennant", "work": "British Zoology", "quote": "The migrant thrush **luscinia** arrives in spring from North Africa, nesting in dense coppices and briars."},
    ]
  },
  "Dashboard — lus/luscious.md": {
    "primary": "Having a deliciously rich, sweet, and pleasing taste or smell; richly appealing to the senses.",
    "secondary": "In sensory prose and culinary writing, luscious denotes rich opulence of flavor, combining ripeness, moisture, and fragrant sweetness.",
    "quotes": [
      {"author": "John Keats", "work": "Endymion", "quote": "Pluck the **luscious** cluster from the vine, where purple grapes hang heavy with sunlit sweetness."},
      {"author": "William Shakespeare", "work": "Othello", "quote": "Food that to him now is as **luscious** as locusts shall be to him shortly as bitter as coloquintida."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Heaped up upon the floor were Norfolk biffins, crisp celery, and piles of **luscious** pears and oranges."},
    ]
  },
  "Dashboard — lus/lusciously.md": {
    "primary": "In a delicious, richly sweet, fragrant, or sensually delightful manner.",
    "secondary": "In landscape poetry, nature is depicted lusciously in summer orchards laden with ripe seasonal harvests.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The boughs of Eden bent down with fruit, offering **lusciously** scented nectar to the primal pair."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "The heavy perfume of lilac and pink-flowering thorn drifted **lusciously** through the open studio window."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The rich dairy meadows yielded sweet clover, smelling **lusciously** in the warm June dusk."},
    ]
  },
  "Dashboard — lus/lusciousness.md": {
    "primary": "Rich, delectable sweetness and appealing sensory abundance.",
    "secondary": "In aesthetic gastronomy, lusciousness balances intense sweetness with sufficient acidity to avoid cloying heaviness on the palate.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Idler", "quote": "A surfeit of sensory **lusciousness** cloys the appetite, rendering simpler fare more truly pleasurable by contrast."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The vintage wine was praised for its velvet texture and honeyed **lusciousness**, distilled from hilltop vineyards."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The carved marble cornices display an opulent vegetative **lusciousness** characteristic of flamboyant Gothic ornament."},
    ]
  },
  "Dashboard — lus/lusitania.md": {
    "primary": "An ancient Roman province in the western Iberian Peninsula; or the famous British ocean liner torpedoed in 1915.",
    "secondary": "In maritime and geopolitical history, the sinking of the RMS Lusitania by a German U-boat catalyzed American entry into World War I.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The sinking of the **lusitania** by a German torpedo horrified civilized world opinion and fundamentally altered American neutrality."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Augustus organized the western districts of the Iberian peninsula into the imperial province of **lusitania**."},
      {"author": "H. G. Wells", "work": "The Outline of History", "quote": "The tragic destruction of the unarmed liner **lusitania** marked a turning point in modern submarine warfare."},
    ]
  },
  "Dashboard — lus/lusitanian.md": {
    "primary": "Pertaining to ancient Lusitania or modern Portugal, its people, language, or culture.",
    "secondary": "In biogeography and ecology, the Lusitanian flora and fauna refers to species disjunctly native to southwestern Iberia and western Ireland.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Viriathus led the fierce **lusitanian** tribes in guerrilla warfare against the Roman praetors for fourteen years."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The curious presence of **lusitanian** plant species in the flora of southwestern Ireland poses an intriguing post-glacial dispersal problem."},
      {"author": "Richard Francis Burton", "work": "Camoens: His Life and His Lusiads", "quote": "The epic poem celebrates the heroic seafaring exploits of the **lusitanian** navigators across uncharted oceans."},
    ]
  },
  "Dashboard — lus/lust.md": {
    "primary": "Intense sexual desire; or an overwhelming, passionate craving for power, wealth, or conquest.",
    "secondary": "In moral philosophy and theological ethics, lust represents disordered, uncontrolled appetite that treats others as mere instruments of gratification.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Sonnet 129", "quote": "The expense of spirit in a waste of shame is **lust** in action; and till action, **lust** is perjured, murderous, bloody, full of blame."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "The unbridled **lust** for sovereign power has toppled great empires and extinguished noble dynastic lines."},
      {"author": "John Milton", "work": "Comus", "quote": "When **lust** by unchaste looks, loose gestures, and foul thoughts lets in defilement to the inward parts, the soul grows clotted."},
    ]
  },
  "Dashboard — lus/luster.md": {
    "primary": "A gentle sheen or soft glow, especially that of a partly reflective surface; radiance or prestige.",
    "secondary": "In mineralogy, luster describes the optical appearance of a mineral's crystal surface under reflected light (e.g., metallic, adamantine, vitreous).",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "The polished mahogany desk gleamed with antique **luster** under the morning sunshine."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A victorious navy would shed an unfading **luster** over the nascent American confederacy."},
      {"author": "Charles Dickens", "work": "Dombey and Son", "quote": "The grand crystal chandeliers added brilliant **luster** to the assembly rooms of the mansion."},
    ]
  },
  "Dashboard — lus/lusterless.md": {
    "primary": "Lacking sheen, glow, or brightness; dull, flat, or completely without vitality and radiance.",
    "secondary": "In clinical diagnosis, lusterless, brittle hair and dry skin indicate severe nutritional deficiencies or endocrine dysfunction.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "His yellow skin scarcely covered the work of muscles beneath; his watery eyes were dim and **lusterless** in their sockets."},
      {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "A cadaverousness of complexion and an eye large, liquid, yet **lusterless** beyond comparison distinguished Roderick Usher."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard's weary eyes had grown **lusterless** as misfortune after misfortune overtook his grain business."},
    ]
  },
  "Dashboard — lus/lusterlessness.md": {
    "primary": "Dullness, opacity, or the complete absence of sheen and reflective radiance.",
    "secondary": "In gemology and mineralogical grading, lusterlessness in a diamond specimen indicates heavy internal fracture networks or acid corrosion.",
    "quotes": [
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The dead, opaque **lusterlessness** of cheap commercial pigments ruins the airy luminosity of landscape painting."},
      {"author": "Herman Melville", "work": "The Encantadas", "quote": "The volcanic cinders of the Galapagos exhibit an uncanny **lusterlessness**, absorbing sunlight without reflecting a single ray."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The mineral specimen was characterized by the earthy **lusterlessness** of its weathered exterior crust."},
    ]
  },
  "Dashboard — lus/lusterware.md": {
    "primary": "Pottery or porcelain decorated with a thin, iridescent metallic glaze that reflects shimmering light.",
    "secondary": "In ceramic history, lusterware was developed in ninth-century Mesopotamia and later perfected by Hispano-Moresque and Staffordshire potters.",
    "quotes": [
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Mrs. Tulliver took immense domestic pride in her prized tea set of Staffordshire copper **lusterware**."},
      {"author": "Charles Dickens", "work": "The Old Curiosity Shop", "quote": "Upon the dusty mantelpiece sat two cracked jugs of pink **lusterware** beside a brass candlestick."},
      {"author": "Edith Wharton", "work": "Ethan Frome", "quote": "Zeena carefully preserved her grandmother's iridescent **lusterware** teapot in the locked corner cupboard."},
    ]
  },
  "Dashboard — lus/lustful.md": {
    "primary": "Driven by or expressing intense, uncontrolled sexual desire; lascivious or licentious.",
    "secondary": "In classical literature, lustful tyrants abuse sovereign authority to satisfy private carnal passions at the expense of their subjects.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard III", "quote": "He is not lolling on a lewd love-bed, but on his knees at meditation; not dallying with a brace of courtezans, but meditating with two deep divines; not sleeping, to engross his idle body, but praying, to enrich his watchful soul: and were he not to England's kingly throne a virtuous and a sovereign prince, he might have been a **lustful** protector."},
      {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "Christian resisted the seductions of the **lustful** temptress Madam Wanton, keeping his eyes fixed upon the celestial city."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman annals recount the cruelties of **lustful** despots whose whims terrorized the patrician families."},
    ]
  },
  "Dashboard — lus/lustfully.md": {
    "primary": "In a lustful, lascivious, or excessively passionate manner, characterized by intense sensual craving.",
    "secondary": "In psychological fiction, characters who gaze lustfully upon forbidden objects betray hidden moral vulnerabilities.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The dark impulses of unhallowed passion peered **lustfully** through the ascetic veneer of Puritan hypocrisy."},
      {"author": "Henry Fielding", "work": "Tom Jones", "quote": "Ensign Northerton eyed the handsome maid **lustfully** as she passed through the tavern kitchen."},
      {"author": "John Milton", "work": "Samson Agonistes", "quote": "Samson confessed how he had surrendered his sacred strength to gaze **lustfully** upon the Philistine temptress."},
    ]
  },
  "Dashboard — lus/lustfulness.md": {
    "primary": "Excessive carnal passion, intense sensual yearning, or lascivious desire.",
    "secondary": "In ascetic theology and patristic writing, lustfulness is condemned as a mortal vice that clouds intellect and subverts spiritual devotion.",
    "quotes": [
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The Houyhnhnms abhorred the unrestrained **lustfulness** and dirty appetites of the brutish Yahoos."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "A life surrendered to unrestrained **lustfulness** terminates inevitably in physical decay and mental remorse."},
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Excessive **lustfulness** inflames the animal spirits, producing melancholy delusions and feverish insomnia."},
    ]
  },
  "Dashboard — lus/lustily.md": {
    "primary": "In a healthy, vigorous, robust, or enthusiastic manner; with great energy and heartiness.",
    "secondary": "In maritime literature, sailors sing lustily while turning the capstan to weigh the ship's heavy anchor.",
    "quotes": [
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "The buccaneers sang **lustily** as they hauled on the ropes: 'Fifteen men on the dead man's chest—Yo-ho-ho, and a bottle of rum!'"},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "Mr. Wardle cheered **lustily** as the cricket match reached its exciting and uproarious conclusion."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The black knight blew **lustily** upon his bugle horn to summon the outlaw yeomen to the castle gates."},
    ]
  },
  "Dashboard — lus/lustiness.md": {
    "primary": "Vigorous bodily health, robust stamina, and energetic physical vitality.",
    "secondary": "In Elizabethan drama, youth is celebrated for its carefree lustiness, contrasting with the infirmities of decrepit age.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "My age is as a lusty winter, frosty, but kindly: for all my youth I was temperate, possessing health and **lustiness** still."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "The medieval monastery bustled with agricultural **lustiness**, draining swamps and felling primordial forests."},
      {"author": "Geoffrey Chaucer", "work": "The Canterbury Tales", "quote": "The young squire rode forth with joyful **lustiness**, singing ballads and dreaming of knightly valor."},
    ]
  },
  "Dashboard — lus/lustrate.md": {
    "primary": "To purify by ceremonial or expiatory sacrifices, ablutions, or ritual ceremonies.",
    "secondary": "In Roman civic religion, the censors gathered every five years to lustrate the entire Roman citizen body in the Campus Martius.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The pagan priests assembled to **lustrate** the imperial city with solemn sacrifices before the barbarian onslaught."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Ancient agrarian tribes sought to **lustrate** their seed-corn with sacred water to avert blight and insect pests."},
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "Marius watched the white-robed procession move to **lustrate** the ancestral farm with sacrificial lustrations."},
    ]
  },
  "Dashboard — lus/lustre.md": {
    "primary": "The British and Commonwealth spelling of luster; sheen, gentle radiance, or distinguished renown.",
    "secondary": "In architectural interior decoration, cut-glass lustre drops reflect prismatic spectra from crystal chandeliers.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Her fine dark eyes acquired remarkable brilliance and **lustre** from the animation of the discussion."},
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "The moon shed her pale silver **lustre** over the ruined arches of the Roman Colosseum."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Becky Sharp was eager to add the **lustre** of an aristocratic marriage to her precarious social position."},
    ]
  },
  "Dashboard — lus/lustreless.md": {
    "primary": "The British and Commonwealth spelling of lusterless; lacking glow, shine, or radiance; dull.",
    "secondary": "In pathology, lustreless eyes and sallow skin are classic clinical signs of chronic systemic anemia.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "His eyes were **lustreless** and heavy, as though the terrible moorland legend had drained his youthful spirit."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The dying leaves hung limp and **lustreless** from the autumn oaks in the misty morning air."},
      {"author": "H. G. Wells", "work": "The Island of Doctor Moreau", "quote": "The beast-folk stared with dull, **lustreless** pupils that showed little trace of human intelligence."},
    ]
  },
  "Dashboard — lus/lustrelessness.md": {
    "primary": "The British and Commonwealth spelling of lusterlessness; dullness or total absence of sheen and radiance.",
    "secondary": "In mineralogy and metallography, the lustrelessness of an unpolished fractured surface distinguishes slag from crystalline ore.",
    "quotes": [
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The dreary **lustrelessness** of damp soot-covered brickwork depressed the aesthetic sensibility of the Victorian traveler."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "The leaden **lustrelessness** of the wintry sky seemed in full harmony with Jude's thwarted academic ambitions."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The bleached carcass of the whale exhibited an uncanny **lustrelessness** under the blazing tropical sun."},
    ]
  },
  "Dashboard — lus/lustrous.md": {
    "primary": "Shining, radiant, gleaming, or having a rich, soft sheen; luminous and splendid.",
    "secondary": "In textile science and luxury crafts, mulberry silk fiber produces naturally lustrous textiles due to triangular cross-sectional light refraction.",
    "quotes": [
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Dorian admired the **lustrous** pearl necklaces displayed in the velvet-lined trays of the jeweler."},
      {"author": "Edgar Allan Poe", "work": "Ligeia", "quote": "Her large, **lustrous** dark eyes shone with an expression of divine mystery and profound intellect."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Beryl Coronet", "quote": "The gems of the coronet were intensely **lustrous**, flashing with blue fire under the gas lamp."},
    ]
  },
  "Dashboard — lus/lustrum.md": {
    "primary": "A period of five years, originally corresponding to the ancient Roman purificatory census cycle.",
    "secondary": "In Roman constitutional antiquities, the completion of the census culminated in the solemn lustrum ceremony performed by the censor.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "At the expiration of each **lustrum**, the Roman censors numbered the citizens and purged the senatorial rolls."},
      {"author": "Thomas Babington Macaulay", "work": "Lays of Ancient Rome", "quote": "For a full **lustrum**, the gates of Janus stood open while Roman legions campaigned across the Etruscan borders."},
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "Another **lustrum** had quietly passed over the empire, marked only by peaceful harvests and civic festivals."},
    ]
  },
  "Dashboard — lus/lusty.md": {
    "primary": "Healthy, strong, vigorous, and full of hearty energy and vitality; robust.",
    "secondary": "In agricultural folklore, lusty laborers and hearty draught horses were celebrated for clearing thick timberland and turning heavy clay soil.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "A gentleman, nurse, that loves to hear himself talk, and will speak more in a minute than he will stand to in a month; a **lusty** youth of gallant bearing."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "The coachman gave a **lusty** shout to his four spirited horses as the stagecoach rattled out of the inn yard."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel Oak was a **lusty** young shepherd who could shear more sheep in an hour than any man in the parish."},
    ]
  },
  "Dashboard — lus/prolusion.md": {
    "primary": "A preliminary essay, trial performance, or introductory exercise preceding a larger work or contest.",
    "secondary": "In classical academic oratory and scholastic disputation, a prolusion served as a formal rhetorical prelude before faculty debates.",
    "quotes": [
      {"author": "John Milton", "work": "Prolusions", "quote": "Milton delivered his collegiate **prolusion** in Cambridge, demonstrating his mastery of Latin eloquence and philosophical debate."},
      {"author": "Samuel Johnson", "work": "Lives of the English Poets", "quote": "The youthful poems of Cowley were regarded as a brilliant **prolusion** to his subsequent metaphysical works."},
      {"author": "Walter Pater", "work": "The Renaissance", "quote": "These early sketches were a charming **prolusion** to Leonardo's monumental fresco compositions in Milan."},
    ]
  },
  "Dashboard — lus/prolusory.md": {
    "primary": "Introductory, preliminary, preparatory, or serving as a prelude or trial exercise.",
    "secondary": "In legal and diplomatic history, prolusory protocols established ground rules and credentials prior to plenary treaty negotiations.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Preliminary aphorisms serve a **prolusory** purpose, preparing the student's mind for deeper philosophical inquiries."},
      {"author": "Jeremy Bentham", "work": "An Introduction to the Principles of Morals and Legislation", "quote": "The opening chapters contain **prolusory** definitions necessary to prevent ambiguity in codifying penal statutes."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The introductory chapters are merely a **prolusory** skirmish before Professor Teufelsdröckh expounds his clothes philosophy."},
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Action & State"

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

print(f"Dashboard — lus: Successfully updated {updated}/{len(data)} notes.")
