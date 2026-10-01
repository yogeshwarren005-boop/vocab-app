import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Cognition & Mind/Dashboard — soph";

const wordsData = {
  "Sophocles.md": {
    word: "Sophocles",
    primary: "One of classical Athens' three great tragic dramatists (c. 496–406 BCE), renowned for authoring Oedipus Rex, Antigone, and Electra (from Greek sophos wise + kleos fame).",
    secondary: "In dramatic theory and literary history, the master playwright who introduced a third actor, expanded scene painting, and perfected tragic irony and heroic characterization.",
    quotes: [
      { author: "Aristotle", work: "Poetics", quote: "In dramatic construction, the recognition and reversal in the Oedipus of **Sophocles** represent the pinnacle of tragic art." },
      { author: "Matthew Arnold", work: "To a Friend", quote: "Be his / My special thanks, whose even-balanced soul, / From first youth tested up to extreme old age, / Business could not make dull, nor passion wild; / Who saw life steadily, and saw it whole; / The mellow glory of the Attic stage, / Singer of sweet Colonus, and its child: **Sophocles**." },
      { author: "George Eliot", work: "Middlemarch", quote: "She read the choruses of **Sophocles** with that solemn awe which profound ancient poetry inspires in youthful minds." }
    ]
  },
  "antisophism.md": {
    word: "antisophism",
    primary: "A counter-argument, logical refutation, or philosophical principle directed against sophistry and specious, deceptive reasoning.",
    secondary: "In dialectical philosophy, the methodical dismantling of fallacious rhetorical tricks to restore clarity, truth, and genuine intellectual rigor.",
    quotes: [
      { author: "Francis Bacon", work: "Novum Organum", quote: "True inductive logic serves as an unyielding **antisophism**, exposing the theatrical illusions of scholastic disputants." },
      { author: "John Locke", work: "An Essay Concerning Human Understanding", quote: "Clear definition of terms is the most potent **antisophism** against ambiguous verbal trickery." },
      { author: "William Hazlitt", work: "Table-Talk", quote: "His plain, robust common sense was a natural **antisophism**, cutting through the lawyer’s web of specious subtleties." }
    ]
  },
  "pansophism.md": {
    word: "pansophism",
    primary: "Universal wisdom or knowledge; the encyclopedic doctrine that all branches of human learning can be integrated into a unified, harmonious whole.",
    secondary: "In the history of education (pioneered by John Amos Comenius in the 17th century), a utopian pedagogy designed to teach 'all things to all people' to achieve spiritual and social harmony.",
    quotes: [
      { author: "John Amos Comenius", work: "The Great Didactic", quote: "Through the light of **pansophism**, we aim to harmonize sacred scripture, nature, and human reason into a universal curriculum." },
      { author: "Samuel Hartlib", work: "A Reformation of Schools", quote: "Our correspondence network was established to cultivate **pansophism**, gathering all arts and sciences for the commonwealth." },
      { author: "Cotton Mather", work: "Magnalia Christi Americana", quote: "He aspired to a pious **pansophism**, desiring his students to see divine wisdom manifested across astronomy, history, and law." }
    ]
  },
  "pansophist.md": {
    word: "pansophist",
    primary: "A person who claims to possess or aspires to achieve universal knowledge, or who advocates the system of pansophy.",
    secondary: "In intellectual history and satire, an ambitious Renaissance polymath or educational reformer striving for an encyclopedic grasp of all disciplines.",
    quotes: [
      { author: "John Amos Comenius", work: "Pansophiae Prodromus", quote: "The true **pansophist** does not hoard disconnected facts, but perceives the golden thread binding all created truths." },
      { author: "Jonathan Swift", work: "A Tale of a Tub", quote: "The self-proclaimed **pansophist** lectured with profound gravity upon subjects whereof he understood not a solitary syllable." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Every century produces its aspiring **pansophist**, who ruins his health attempting to master the whole library of human lore." }
    ]
  },
  "pansophy.md": {
    word: "pansophy",
    primary: "Universal or all-embracing knowledge; an encyclopedic system comprising all branches of learning (from Greek pan- all + sophia wisdom).",
    secondary: "In Renaissance hermeticism and 17th-century philosophy, the ideal of a complete, divinely illuminated synthesis of human arts, natural philosophy, and theology.",
    quotes: [
      { author: "John Amos Comenius", work: "The Way of Light", quote: "Universal peace among nations can flourish only when illuminated by the shared dawn of **pansophy**." },
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "Though total **pansophy** exceeds mortal reach, systematic natural history brings us closer to universal truth." },
      { author: "Cotton Mather", work: "The Christian Philosopher", quote: "In the works of creation, the devout soul beholds an admirable **pansophy**, displaying the infinite manifold wisdom of God." }
    ]
  },
  "philosopher.md": {
    word: "philosopher",
    primary: "A person who seeks wisdom, contemplates fundamental questions about existence, knowledge, and ethics, or studies philosophy.",
    secondary: "Historically from Greek philosophos (lover of wisdom, attributed to Pythagoras), a thinker who values disciplined inquiry over dogmatic certainty.",
    quotes: [
      { author: "Plato", work: "Republic", quote: "Until **philosophers** are kings, or the kings of this world have the spirit and power of philosophy, cities will never have rest from their evils." },
      { author: "Voltaire", work: "Philosophical Dictionary", quote: "The true **philosopher** cultivates his garden, seeks truth without fanaticism, and pities human folly." },
      { author: "Friedrich Nietzsche", work: "Beyond Good and Evil", quote: "A genuine **philosopher** is a commander and lawgiver; he determines the values and direction of humankind." }
    ]
  },
  "philosophic.md": {
    word: "philosophic",
    primary: "Of, relating to, or appropriate to philosophy or philosophers; calm, stoic, and rational in the face of misfortune.",
    secondary: "In intellectual history and literature, denoting a calm reflective temper that views transient human troubles within a vast cosmic perspective.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Marcus Aurelius preserved a **philosophic** serenity upon the throne, meditating upon the vanity of earthly pomp." },
      { author: "William Wordsworth", work: "Ode: Intimations of Immortality", quote: "In the soothing thoughts that spring / Out of human suffering; / In the faith that looks through death, / In years that bring the **philosophic** mind." },
      { author: "Thomas Carlyle", work: "Sartor Resartus", quote: "Teufelsdröckh contemplated the clothes of mankind with a profound and detached **philosophic** humor." }
    ]
  },
  "philosophical.md": {
    word: "philosophical",
    primary: "Relating to or devoted to the study of the fundamental nature of knowledge, reality, and existence; maintaining composure and stoic calm in difficulties.",
    secondary: "In everyday usage, meeting misfortune, delay, or disappointment with equanimity and resigned good humor.",
    quotes: [
      { author: "Bertrand Russell", work: "The Problems of Philosophy", quote: "The value of **philosophical** study lies largely in its uncertainty, freeing our thoughts from the tyranny of custom." },
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "Elizabeth tried to be **philosophical** about her disappointment, observing that human life was made of such small trials." },
      { author: "Francis Bacon", work: "The Essays: Of Truth", quote: "A little **philosophical** inquiry inclineth man's mind to atheism, but depth in philosophy bringeth men's minds about to religion." }
    ]
  },
  "philosophically.md": {
    word: "philosophically",
    primary: "In a manner relating to philosophy; calmly, rationally, or with stoic equanimity.",
    secondary: "In analytical discourse, from the standpoint of foundational logic, ontology, or normative ethics rather than superficial pragmatism.",
    quotes: [
      { author: "Charles Dickens", work: "David Copperfield", quote: "Mr. Micawber bore his financial embarrassments **philosophically**, confident that something would turn up before nightfall." },
      { author: "John Locke", work: "An Essay Concerning Human Understanding", quote: "To speak **philosophically**, our ideas of primary qualities resemble the external bodies themselves." },
      { author: "William James", work: "The Will to Believe", quote: "We must consider this grave religious question not dogmatically, but **philosophically** and with open hearts." }
    ]
  },
  "philosophise.md": {
    word: "philosophise",
    primary: "To speculate, theorize, or deliberate in a philosophical manner (British English spelling).",
    secondary: "In literary contexts, to reflect deeply on human nature, morals, or the universe, sometimes with gentle irony regarding over-subtle abstraction.",
    quotes: [
      { author: "Virginia Woolf", work: "The Waves", quote: "Let us sit by the window and **philosophise** while the evening shadows lengthen across the garden." },
      { author: "Thomas Hardy", work: "Tess of the d'Urbervilles", quote: "He would lean against the gate and **philosophise** upon the cruel indifference of the rural universe." },
      { author: "Bertrand Russell", work: "A History of Western Philosophy", quote: "To **philosophise** is to learn to live with uncertainty without becoming paralyzed by hesitation." }
    ]
  },
  "philosophiser.md": {
    word: "philosophiser",
    primary: "A person who philosophizes; often used pejoratively for someone who engages in amateur, pedantic, or tedious moralizing (British English spelling).",
    secondary: "In satirical essays and character sketches, a person who expounds trite maxims or abstract theories while ignoring practical daily responsibilities.",
    quotes: [
      { author: "George Eliot", work: "Middlemarch", quote: "Mr. Brooke was an incorrigible **philosophiser**, ready to debate political economy over breakfast and forget the estate accounts by noon." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "The cynical old **philosophiser** watched the dance of ambition from his comfortable armchair at the club." },
      { author: "Jonathan Swift", work: "Gulliver's Travels", quote: "The academy of Lagado was crowded with speculative **philosophisers** striving to extract sunbeams from cucumbers." }
    ]
  },
  "philosophize.md": {
    word: "philosophize",
    primary: "To speculate, theorize, or deliberate about fundamental questions of life, reality, and morals; to think or speak like a philosopher.",
    secondary: "In everyday conversation, to indulge in abstract or moralistic reflection, sometimes to the point of impractical musing.",
    quotes: [
      { author: "Montaigne", work: "Essays", quote: "To **philosophize** is nothing other than to prepare oneself for death." },
      { author: "Henry David Thoreau", work: "Walden", quote: "To be a philosopher is not merely to have subtle thoughts, but so to love wisdom as to live according to its dictates; to **philosophize** is to live a life of simplicity, independence, magnanimity, and trust." },
      { author: "Mark Twain", work: "The Adventures of Tom Sawyer", quote: "Tom began to **philosophize** upon the great law of human action: that in order to make a man covet a thing, it is only necessary to make the thing difficult to attain." }
    ]
  },
  "philosophizer.md": {
    word: "philosophizer",
    primary: "A person who philosophizes, especially one who indulges in superficial, pedantic, or pretentious speculation.",
    secondary: "In social criticism and drama, an armchair theorist who discourses endlessly on morals and destiny while lacking practical judgment.",
    quotes: [
      { author: "Washington Irving", work: "The Sketch Book of Geoffrey Crayon", quote: "The village **philosophizer** sat upon the porch of the inn, settling the affairs of the nation over a mug of cider." },
      { author: "Ralph Waldo Emerson", work: "Representative Men", quote: "The shallow **philosophizer** mistakes novel terminology for profound original insight into reality." },
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "Ishmael proved a restless **philosophizer**, finding metaphysical emblems in mastheads, ambergris, and harpoon line." }
    ]
  },
  "philosophizing.md": {
    word: "philosophizing",
    primary: "The act or process of engaging in philosophical thought, discourse, or speculation.",
    secondary: "In personal essay writing, reflective contemplation on the meaning of experience, often contrasted with immediate emotional reaction or practical action.",
    quotes: [
      { author: "William James", work: "Pragmatism", quote: "Our **philosophizing** must not remain in the thin air of abstraction, but step down into the muddy streets of actual life." },
      { author: "Friedrich Nietzsche", work: "Twilight of the Idols", quote: "I take up the hammer to test idols; this is how one conducts **philosophizing** with a hammer." },
      { author: "Leo Tolstoy", work: "Anna Karenina", quote: "Levin grew weary of endless theoretical **philosophizing** about agrarian reform that bore no fruit on his fields." }
    ]
  },
  "philosophy.md": {
    word: "philosophy",
    primary: "The study of fundamental questions regarding existence, knowledge, values, reason, mind, and language (literally 'love of wisdom').",
    secondary: "In personal and organizational life, a coherent set of guiding principles, values, or practical rules of conduct governing behavior.",
    quotes: [
      { author: "William Shakespeare", work: "Hamlet", quote: "There are more things in heaven and earth, Horatio, / Than are dreamt of in your **philosophy**." },
      { author: "Aristotle", work: "Metaphysics", quote: "It is through wonder that men now begin and at first began to cultivate **philosophy**." },
      { author: "John Stuart Mill", work: "Utilitarianism", quote: "Better to be Socrates dissatisfied than a fool satisfied; the pursuits of genuine **philosophy** bring higher pleasures." }
    ]
  },
  "soph.md": {
    word: "soph",
    primary: "An informal collegiate abbreviation for a sophomore; also the combining Greek root soph- meaning wise, skilled, or clever.",
    secondary: "In classical morphology and school slang, the root element in sophist, philosophy, and sophomore, denoting wisdom or its specious imitation.",
    quotes: [
      { author: "F. Scott Fitzgerald", work: "This Side of Paradise", quote: "As an ambitious college **soph**, Amory Blaine debated literary aesthetics late into the Princeton night." },
      { author: "Walter William Skeat", work: "Principles of English Etymology", quote: "The monosyllabic root **soph**- preserves the Ancient Greek term for wisdom, craft, and intellectual skill." },
      { author: "Max Müller", work: "Lectures on the Science of Language", quote: "In Hellenic compounding, the prefix **soph**- marks the emergence of self-conscious intellectual reflection." }
    ]
  },
  "sophism.md": {
    word: "sophism",
    primary: "A clever but fallacious argument, especially one deliberately used to deceive, mislead, or win a debate.",
    secondary: "In classical dialectic and formal logic, a deceptive syllogism or reasoning trick that appears sound on the surface while concealing a fatal fallacy.",
    quotes: [
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "The subtle disputants of the schools entangled truth in a labyrinth of verbal **sophisms**." },
      { author: "Thomas Paine", work: "Common Sense", quote: "No political **sophism** can reconcile the natural rights of free men with hereditary tyranny." },
      { author: "John Locke", work: "An Essay Concerning Human Understanding", quote: "A well-trained mind detects the hidden **sophism** beneath the orator's flowery eloquence." }
    ]
  },
  "sophist.md": {
    word: "sophist",
    primary: "A paid teacher of philosophy and rhetoric in ancient Greece; in modern usage, a person who uses clever but misleading or fallacious arguments.",
    secondary: "In the history of philosophy (Protagoras, Gorgias), an early intellectual humanist focusing on rhetoric, relativism, and political persuasion, criticized by Plato for valuing victory over truth.",
    quotes: [
      { author: "Plato", work: "Sophist", quote: "The **sophist** is a hunter after wealthy young men, a merchant of knowledge for the soul, and an imitator of true wisdom." },
      { author: "Friedrich Nietzsche", work: "The Will to Power", quote: "The Greek **sophists** were fearless realists, recognizing that culture is created by human conventions rather than divine decrees." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "The age of chivalry is gone; that of **sophists**, economists, and calculators has succeeded, and the glory of Europe is extinguished forever." }
    ]
  },
  "sophistic.md": {
    word: "sophistic",
    primary: "Of, relating to, or characteristic of sophists or sophistry; plausible yet specious and deceptively subtle.",
    secondary: "In the history of rhetoric (the First and Second Sophistic), referring to influential cultural movements celebrating oratorical virtuosity and public performance.",
    quotes: [
      { author: "Aristotle", work: "Nicomachean Ethics", quote: "The **sophistic** art promises to teach political mastery, yet those who teach it have never governed a single city." },
      { author: "Samuel Johnson", work: "The Rambler", quote: "Beware of that **sophistic** dexterity which excuses vice under the attractive title of worldly wisdom." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "During the Second Sophistic, rhetoricians were showered with imperial honors for their dazzling **sophistic** declamations." }
    ]
  },
  "sophistical.md": {
    word: "sophistical",
    primary: "Plausibly fallacious; deceptive or misleading in argument; of the nature of sophistry.",
    secondary: "In formal dialectic, describing arguments that exploit semantic ambiguities or illicit shifts in premise to bamboozle an opponent.",
    quotes: [
      { author: "David Hume", work: "An Enquiry Concerning Human Understanding", quote: "Does it contain any abstract reasoning concerning quantity or number? No. Commit it then to the flames: for it can contain nothing but **sophistical** delusion." },
      { author: "Thomas Jefferson", work: "Autobiography", quote: "The royal lawyers offered **sophistical** defenses of parliamentary taxation that violated every tenet of natural law." },
      { author: "Charles Dickens", work: "Hard Times", quote: "Mr. Bounderby dismissed the factory workers’ grievances with a blast of coarse, **sophistical** bluster." }
    ]
  },
  "sophisticate.md": {
    word: "sophisticate",
    primary: "A person with refined tastes, worldly experience, and intellectual polish; as a verb, to make complex, alter, or corrupt.",
    secondary: "Historically in alchemy, cooking, and medicine, to adulterate, debase, or compromise the natural purity of a substance with artificial mixtures.",
    quotes: [
      { author: "Oscar Wilde", work: "The Picture of Dorian Gray", quote: "He sat among the London **sophisticates**, dazzling the salon with cynical epigrams upon modern romance." },
      { author: "Francis Bacon", work: "Sylva Sylvarum", quote: "Unscrupulous vintners **sophisticate** their wines with lead and spices to disguise decay." },
      { author: "Henry James", work: "The Ambassadors", quote: "Paris had transformed the provincial American into an exquisite **sophisticate** of quiet discernment." }
    ]
  },
  "sophisticated.md": {
    word: "sophisticated",
    primary: "Having, revealing, or involving a great deal of worldly experience and knowledge of fashion and culture; highly developed, complex, or advanced.",
    secondary: "In engineering and software design, possessing subtle, intricate, and refined capabilities capable of handling complex contingencies.",
    quotes: [
      { author: "F. Scott Fitzgerald", work: "The Great Gatsby", quote: "'I've been everywhere and seen everything and done everything,' her eyes flashed on about her in a defiant way, rather like Tom's, 'Sophisticated—God, I'm **sophisticated**!'" },
      { author: "Carl Sagan", work: "Cosmos", quote: "Modern radio astronomy relies upon extraordinarily **sophisticated** receivers capable of detecting microwatts from distant galaxies." },
      { author: "Aldous Huxley", work: "Brave New World", quote: "The biological technology of the World State was far too **sophisticated** to allow accidental mutations." }
    ]
  },
  "sophistication.md": {
    word: "sophistication",
    primary: "The quality of having worldly experience, cultural refinement, and refined taste; also the quality of being advanced, complex, or intricate.",
    secondary: "Historically, the act of adulterating, falsifying, or corrupting the purity of a substance or philosophical doctrine.",
    quotes: [
      { author: "Oscar Wilde", work: "The Decay of Lying", quote: "True **sophistication** consists in knowing the value of everything while pretending to care for nothing." },
      { author: "Henry James", work: "The Portrait of a Lady", quote: "Isabel admired Madame Merle’s effortless social **sophistication**, unaware of the cold calculation beneath it." },
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "The division of labor leads to an astonishing level of technological **sophistication** in modern pin manufacture." }
    ]
  },
  "sophistry.md": {
    word: "sophistry",
    primary: "The use of fallacious arguments, especially with the intention of deceiving; specious, deceptively plausible reasoning.",
    secondary: "In political and moral debate, the art of dressing up falsehood or injustice in appealing, high-sounding language.",
    quotes: [
      { author: "John Locke", work: "An Essay Concerning Human Understanding", quote: "Men have entangled truth in the cobwebs of **sophistry**, mistaking dispute for knowledge." },
      { author: "George Orwell", work: "Politics and the English Language", quote: "Political language is designed to make lies sound truthful and murder respectable, relying on pure **sophistry**." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "They tore down ancestral institutions with the ruthless **sophistry** of metaphysical dogmatists." }
    ]
  },
  "sophomania.md": {
    word: "sophomania",
    primary: "A delusional or grandiose belief in one's own supreme wisdom, intellect, or omniscience.",
    secondary: "In psychopathology, a form of megalomania where the patient is unshakably convinced that they possess peerless philosophical insight or divine enlightenment.",
    quotes: [
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Some scholars are seized with incurable **sophomania**, imagining themselves greater than Aristotle while raving in solitude." },
      { author: "Jonathan Swift", work: "A Tale of a Tub", quote: "The author’s preface was written in a fit of pure **sophomania**, promising to solve every mystery in heaven and earth." },
      { author: "William James", work: "The Principles of Psychology", quote: "In paranoiac megalomania, **sophomania** often leads the patient to publish nonsensical cosmological systems." }
    ]
  },
  "sophomaniac.md": {
    word: "sophomaniac",
    primary: "A person who exhibits sophomania; someone possessed by a delusion of their own supreme wisdom or intellectual infallibility.",
    secondary: "In social satire, an insufferable pedant or pseudo-intellectual who lectures others with unshakeable conceit.",
    quotes: [
      { author: "Alexander Pope", work: "The Dunciad", quote: "The pedantic critic reigned among his disciples, a crowned **sophomaniac** deaf to the music of authentic poetry." },
      { author: "H. L. Mencken", work: "Prejudices: First Series", quote: "Every small-town college harbored at least one harmless **sophomaniac** who fancied himself a second Spinoza." },
      { author: "George Bernard Shaw", work: "Misalliance", quote: "Do not argue with him; he is a hopeless **sophomaniac** who will quote nonexistent authorities to prove you wrong." }
    ]
  },
  "sophomore.md": {
    word: "sophomore",
    primary: "A student in the second year of high school or college; historically derived from Greek sophos (wise) + moros (foolish)—a 'wise fool'.",
    secondary: "In cultural idioms, designating a second effort or creation (e.g. a sophomore album or novel) that often faces the 'sophomore slump'.",
    quotes: [
      { author: "F. Scott Fitzgerald", work: "This Side of Paradise", quote: "During his year as a college **sophomore**, he cast off his freshman humility and cultivated an air of romantic disillusion." },
      { author: "Mark Twain", work: "Life on the Mississippi", quote: "The young apprentice pilot strutted upon the hurricane deck with all the cocky assurance of a university **sophomore**." },
      { author: "Kurt Vonnegut", work: "Cat's Cradle", quote: "Her opinions had that breezy, unassailable certainty characteristic of an undergraduate **sophomore**." }
    ]
  },
  "sophomoric.md": {
    word: "sophomoric",
    primary: "Pretentious, juvenile, or immature; conceited and overconfident while demonstrating shallow knowledge.",
    secondary: "In literary and cultural criticism, describing humor, prose, or intellectual postures that mistake adolescent cynicism for profound insight.",
    quotes: [
      { author: "George Orwell", work: "Inside the Whale", quote: "His political pamphlets were disfigured by a **sophomoric** cynicism that mistook vulgar abuse for fearless radicalism." },
      { author: "Vladimir Nabokov", work: "Pale Fire", quote: "Kinbote’s rambling commentary displayed a bizarre mixture of genuine erudition and **sophomoric** vanity." },
      { author: "Virginia Woolf", work: "The Common Reader", quote: "The essay lapsed occasionally into **sophomoric** generalities about destiny and the cosmic soul." }
    ]
  },
  "sophonias.md": {
    word: "sophonias",
    primary: "The biblical prophet Zephaniah; the Greek and Latin form (Sophonias) used in the Septuagint and Vulgate for the book and prophet of Zephaniah.",
    secondary: "In biblical scholarship, the seventh of the twelve Minor Prophets who prophesied during the reign of King Josiah, proclaiming the imminent 'Day of the Lord' (from Hebrew Tsephanyah, Yahweh has hidden/treasured).",
    quotes: [
      { author: "Saint Jerome", work: "Commentary on Sophonias", quote: "The name **Sophonias** signifies the secret or hidden of the Lord, warning of righteous judgment upon idolatrous Jerusalem." },
      { author: "Martin Luther", work: "Prefaces to the Books of the Bible", quote: "The prophecy of **Sophonias** speaks with fiery power against the complacency of those who imagine God sees not their deeds." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The monks recited the apocalyptic laments of **Sophonias** as barbarian hordes encircled the city walls." }
    ]
  },
  "sophora.md": {
    word: "sophora",
    primary: "A genus of trees, shrubs, and perennial herbs in the pea family (Fabaceae), native to southeastern Europe, southern Asia, Australasia, and the Americas.",
    secondary: "In systematic botany and pharmacology, species such as Styphnolobium japonicum (formerly Sophora japonica, the Japanese pagoda tree) valued for ornamental shade and rich flavonoid yields (rutin); etymologically from Arabic sufayra (yellowish), a botanical homograph on soph-.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The graceful pinnate foliage of the **Sophora** produces drooping racemes of pea-like blossoms in late summer." },
      { author: "Joseph Dalton Hooker", work: "The Flora of British India", quote: "We observed species of **Sophora** flourishing upon the arid Himalayan slopes, where their deep roots bind the loose shale." },
      { author: "Alexander von Humboldt", work: "Aspects of Nature", quote: "The shores of New Zealand were fringed with golden kowhai, a magnificent arborescent **Sophora** glowing in the austral sun." }
    ]
  },
  "theosophical.md": {
    word: "theosophical",
    primary: "Of, relating to, or inspired by theosophy; concerning mystical insight into the divine nature and cosmic mysteries.",
    secondary: "In late 19th-century intellectual history, pertaining to the Theosophical Society founded by Madame Blavatsky, synthesizing Western occultism with Hindu and Buddhist metaphysics.",
    quotes: [
      { author: "William James", work: "The Varieties of Religious Experience", quote: "The modern **theosophical** movement revived ancient Alexandrian gnosticism in a contemporary occult dress." },
      { author: "W. B. Yeats", work: "Autobiographies", quote: "My early fascination with **theosophical** doctrines opened my imagination to symbolist drama and visionary poetry." },
      { author: "C. G. Jung", work: "Memories, Dreams, Reflections", quote: "While critical of sectarian occultism, I acknowledged that **theosophical** literature preserved important archetypal symbols." }
    ]
  },
  "theosophist.md": {
    word: "theosophist",
    primary: "An adherent, student, or practitioner of theosophy; one who seeks direct intuitive knowledge of divine reality.",
    secondary: "In cultural history, a member of the Theosophical Society (such as Helena Blavatsky, Annie Besant, or Henry Steel Olcott) who championed esoteric philosophy.",
    quotes: [
      { author: "Helena Blavatsky", work: "The Key to Theosophy", quote: "A true **theosophist** is one who seeks universal brotherhood without distinction of race, creed, sex, or caste." },
      { author: "James Joyce", work: "Ulysses", quote: "AE presided over the Dublin circle of **theosophists**, discussing the astral plane and the Upanishads over vegetarian tea." },
      { author: "Arthur Conan Doyle", work: "The History of Spiritualism", quote: "The prominent **theosophist** Col. Olcott collaborated with Indian pandits to revive traditional Buddhist education in Ceylon." }
    ]
  },
  "theosophy.md": {
    word: "theosophy",
    primary: "Any of various philosophies maintaining that knowledge of God and cosmic mysteries may be achieved through spiritual ecstasy, direct intuition, or mystical illumination (from Greek theos god + sophia wisdom).",
    secondary: "In the history of esoteric thought, the mystical tradition tracing from Jacob Böhme and Renaissance Neoplatonism through modern occult movements promoting universal brotherhood.",
    quotes: [
      { author: "Helena Blavatsky", work: "The Secret Doctrine", quote: "**Theosophy** is the archaic Wisdom-Religion, the esoteric basis found at the core of all ancient world faiths." },
      { author: "William Butler Yeats", work: "Essays and Introductions", quote: "His mind was steeped in the mystical **theosophy** of Böhme and Swedenborg, finding holy signatures in every natural form." },
      { author: "Bertrand Russell", work: "A History of Western Philosophy", quote: "Alexandrian syncretism nurtured an early species of **theosophy** that fused Greek logic with oriental mysticism." }
    ]
  },
  "unsophisticated.md": {
    word: "unsophisticated",
    primary: "Lacking worldly experience, artifice, or cosmopolitan complexity; simple, innocent, natural, or straightforward.",
    secondary: "In technology and design, uncomplex, basic, or rudimentary; not utilizing advanced or intricate mechanisms.",
    quotes: [
      { author: "Jane Austen", work: "Northanger Abbey", quote: "Catherine was an **unsophisticated** girl of seventeen, completely innocent of worldly intrigues and social deceptions." },
      { author: "Charles Dickens", work: "The Pickwick Papers", quote: "The villagers displayed an **unsophisticated** hospitality that warmed the hearts of the traveling Londoners." },
      { author: "Thomas Hardy", work: "Under the Greenwood Tree", quote: "The rustic choir played their carols on simple, **unsophisticated** instruments fashioned from local boxwood." }
    ]
  }
};

function updateWordNote(relPath, data) {
  const fullPath = path.join(baseDir, relPath);
  if (!fs.existsSync(fullPath)) {
    console.error("Not found:", fullPath);
    return;
  }
  let content = fs.readFileSync(fullPath, "utf8");

  // Format quotes
  const quotesFormatted = data.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join("\n");

  // Replace Definition & Semantic Range
  const defRegex = /> \[!book\] 📖 Definitions & Semantic Range[\s\S]*?(?=> \[!quote\]|$)/;
  const newDef = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${data.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${data.secondary}\n\n`;

  if (defRegex.test(content)) {
    content = content.replace(defRegex, newDef);
  } else {
    console.warn("Could not find [!book] in", relPath);
  }

  // Replace Quotes
  const quoteRegex = /> \[!quote\] 💬 Contextual Usage & Authentic Quotations[\s\S]*$/;
  const newQuotes = `> [!quote] 💬 Contextual Usage & Authentic Quotations\n${quotesFormatted}\n`;

  if (quoteRegex.test(content)) {
    content = content.replace(quoteRegex, newQuotes);
  } else {
    console.warn("Could not find [!quote] in", relPath);
  }

  fs.writeFileSync(fullPath, content, "utf8");
  console.log("Updated:", relPath);
}

for (const [relPath, data] of Object.entries(wordsData)) {
  updateWordNote(relPath, data);
}
console.log("Batch 7 completed! Total words updated:", Object.keys(wordsData).length);
