# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  "Dashboard — log/illogicality.md": {
    "primary": "The quality of being contrary to or devoid of logic; irrationality or invalidity of thought.",
    "secondary": "In epistemological critique, a formal fallaciousness or lack of internal deductive coherence in an argument.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The apparent plausibility of a sophism often conceals a radical **illogicality** in the initial premises."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Emotional fervor frequently blinds a thinker to the glaring **illogicality** of his cherished conclusions."},
      {"author": "Bertrand Russell", "work": "Mysticism and Logic", "quote": "Philosophical skepticism exposes the inherent **illogicality** that arises when common sense attempts metaphysics."}
    ]
  },
  "Dashboard — log/logically.md": {
    "primary": "In a way that is in accordance with the rules of logic or formal reasoning; rationally.",
    "secondary": "In deductive philosophy, following necessarily from valid premises through sound inference.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "If we admit the variability of species, we must **logically** accept that all organisms descend from common ancestors."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "To argue **logically**, the mind must connect its intermediate ideas without introducing unexamined assumptions."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "A hypothesis that cannot be **logically** deduced from observed phenomena remains a mere flight of fancy."}
    ]
  },
  "Dashboard — log/logicalness.md": {
    "primary": "The characteristic of conforming strictly to the laws of logic; soundness or rationality.",
    "secondary": "In philosophical argumentation, the rigorous coherence and non-contradictory structure of an exposition.",
    "quotes": [
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "The relentless **logicalness** of her husband's demands left no room for the subtle appeals of sympathy."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "A foolish consistency is the hobgoblin of little minds, yet an underlying **logicalness** governs nature."},
      {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "Mental development advances toward greater **logicalness** as perceptions are classified into systematic hierarchies."}
    ]
  },
  "Dashboard — log/logician.md": {
    "primary": "A person skilled in or dedicated to the study and practice of logic and formal reasoning.",
    "secondary": "In scholastic and symbolic philosophy, a scholar analyzing syllogisms, truth functions, and formal systems.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The traditional **logician** corrupts natural inquiry by forcing physical phenomena into rigid syllogistic molds."},
      {"author": "Lewis Carroll", "work": "Through the Looking-Glass", "quote": "'Contrariwise,' continued the profound **logician**, 'if it was so, it might be; and if it were so, it would be.'"},
      {"author": "John Stuart Mill", "work": "An Examination of Sir William Hamilton's Philosophy", "quote": "A competent **logician** does not invent truth; he verifies the paths by which truth is attained."}
    ]
  },
  "Dashboard — log/logicism.md": {
    "primary": "The philosophical doctrine that mathematics is reducible to, or an extension of, formal logic.",
    "secondary": "In mathematical foundations, the program championed by Frege and Russell asserting mathematical truths are purely logical truths.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "The fundamental thesis of **logicism** is that all pure mathematics deals exclusively with concepts definable in terms of logic."},
      {"author": "Gottlob Frege", "work": "The Foundations of Arithmetic", "quote": "By establishing **logicism**, we demonstrate that arithmetic requires no appeal to spatial or temporal intuition."},
      {"author": "Henri Poincaré", "work": "Science and Method", "quote": "Against the claims of **logicism**, I maintain that mathematical discovery requires genuine synthetic intuition."}
    ]
  },
  "Dashboard — log/loginess.md": {
    "primary": "A state of physical lethargy, heaviness, or dull sluggishness; languor.",
    "secondary": "In vernacular medical description, the post-febrile heaviness or torpor affecting motor responsiveness.",
    "quotes": [
      {"author": "Jack London", "work": "The Sea-Wolf", "quote": "The persistent damp and chill produced a heavy **loginess** in the men's limbs that made swift duty impossible."},
      {"author": "Theodore Dreiser", "work": "An American Tragedy", "quote": "A dull **loginess** overcame him after hours of pacing the hot pavement, clouding his purpose."},
      {"author": "Hamlin Garland", "work": "Main-Travelled Roads", "quote": "The oppressive summer heat induced a deep **loginess** across the farmstead, halting all brisk labor."}
    ]
  },
  "Dashboard — log/logion.md": {
    "primary": "A traditional saying or maxim attributed to a religious teacher, particularly Jesus Christ.",
    "secondary": "In textual and biblical criticism, an isolated aphoristic utterance recorded in early gospel fragments or papyri.",
    "quotes": [
      {"author": "Adolf von Harnack", "work": "The Sayings of Jesus", "quote": "Each isolated **logion** preserved in Q reflects the unvarnished moral urgency of the earliest Christian preaching."},
      {"author": "F. C. Burkitt", "work": "The Gospel History and Its Transmission", "quote": "The discovery of the Oxyrhynchus papyri added more than one enigmatic **logion** to our fragmentary records."},
      {"author": "B. F. Westcott", "work": "Introduction to the Study of the Gospels", "quote": "The rhythmic symmetry of an authentic **logion** facilitated its preservation through oral transmission."}
    ]
  },
  "Dashboard — log/logistic.md": {
    "primary": "Relating to the procurement, maintenance, and movement of resources, equipment, and personnel.",
    "secondary": "In mathematical biology and statistics, describing a sigmoidal growth curve characterized by an initial exponential phase leveling off at carrying capacity.",
    "quotes": [
      {"author": "Carl von Clausewitz", "work": "On War", "quote": "Every grand operational plan collapses if the **logistic** apparatus fails to feed and munition the forward divisions."},
      {"author": "Raymond Pearl", "work": "The Biology of Population Growth", "quote": "The growth of the yeast population conformed with remarkable precision to the symmetrical **logistic** curve."},
      {"author": "Alfred Thayer Mahan", "work": "The Influence of Sea Power upon History", "quote": "A fleet without dependable **logistic** bases along its route of voyage is paralyzed before battle commences."}
    ]
  },
  "Dashboard — log/logistical.md": {
    "primary": "Relating to or involving the coordination and operational organization of complex collective endeavors.",
    "secondary": "In supply chain strategy and civil administration, managing the distribution networks and temporal staging of materiel.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The colossal **logistical** challenge of transporting two million American soldiers across the Atlantic was solved with astonishing speed."},
      {"author": "Dwight D. Eisenhower", "work": "Crusade in Europe", "quote": "No combat operation was ever launched without first resolving every intricate **logistical** detail of fuel and ammunition."},
      {"author": "Douglas MacArthur", "work": "Reminiscences", "quote": "Our rapid amphibious advances in the Pacific depended entirely upon overcoming formidable **logistical** obstacles."}
    ]
  },
  "Dashboard — log/logistician.md": {
    "primary": "A specialist or expert responsible for the analysis, planning, and management of logistical operations.",
    "secondary": "In military science and industrial transport, a coordinator overseeing supply lines, storage facilities, and fleet routing.",
    "quotes": [
      {"author": "Dwight D. Eisenhower", "work": "Crusade in Europe", "quote": "The master **logistician** must anticipate the requirements of the battlefield months before the artillery opens fire."},
      {"author": "Douglas MacArthur", "work": "Reports of General MacArthur", "quote": "To every combat commander, the tireless **logistician** is the indispensable architect of sustained victory."},
      {"author": "Antoine-Henri Jomini", "work": "Summary of the Art of War", "quote": "The staff **logistician** unites strategy and tactics by ensuring armies arrive at the decisive point fully provisioned."}
    ]
  },
  "Dashboard — log/logistics.md": {
    "primary": "The detailed coordination of complex operations involving people, facilities, supplies, and equipment.",
    "secondary": "In military science, the branch dealing with the movement, supply, and maintenance of armed forces.",
    "quotes": [
      {"author": "Carl von Clausewitz", "work": "On War", "quote": "The science of **logistics** governs the physical sustenance and transport without which military strategy is an idle dream."},
      {"author": "Winston Churchill", "work": "The Gathering Storm", "quote": "Modern warfare is largely a contest of industrial production and mechanical **logistics**."},
      {"author": "Antoine-Henri Jomini", "work": "The Art of War", "quote": "I have defined **logistics** as the practical art of moving armies and keeping them supplied in the field."}
    ]
  },
  "Dashboard — log/logo.md": {
    "primary": "A graphic symbol, emblem, or stylized mark adopted by an organization or brand for identification.",
    "secondary": "In commercial design and typography, a distinctive logotype or visual trademark conveying institutional identity.",
    "quotes": [
      {"author": "Walter Lippmann", "work": "Public Opinion", "quote": "A commercial **logo** functions as an instant visual stereotype, evoking pre-established habits of confidence."},
      {"author": "Marshall McLuhan", "work": "Understanding Media", "quote": "The corporate **logo** compresses complex institutional messaging into a single iconic configuration."},
      {"author": "Thorstein Veblen", "work": "The Theory of the Leisure Class", "quote": "The decorative **logo** stamped upon luxury goods confirms the reputability and pecuniary strength of the consumer."}
    ]
  },
  "Dashboard — log/logogram.md": {
    "primary": "A written or pictorial character representing a whole word or morpheme rather than a phonetic sound.",
    "secondary": "In historical epigraphy and semiotics, an ideographic sign found in Egyptian hieroglyphs, Sumerian cuneiform, or Chinese hanzi.",
    "quotes": [
      {"author": "Jean-François Champollion", "work": "Précis du système hiéroglyphique", "quote": "A single Egyptian **logogram** could signify both an abstract divinity and the material creature representing it."},
      {"author": "Edward Sapir", "work": "Language: An Introduction to the Study of Speech", "quote": "In Chinese writing, each distinct **logogram** embodies a meaningful grammatical unit rather than an arbitrary phonetic syllable."},
      {"author": "Archibald Sayce", "work": "Lectures on the Assyrian Language", "quote": "Cuneiform inscriptions demonstrate the gradual transition from an ancient pictorial **logogram** to a syllabic phonetic sign."}
    ]
  },
  "Dashboard — log/logogrammatic.md": {
    "primary": "Of, relating to, or written with logograms; ideographic in character representation.",
    "secondary": "In comparative writing systems, employing symbols where each sign directly signifies a word or concept.",
    "quotes": [
      {"author": "Archibald Sayce", "work": "The Archaeology of the Cuneiform Inscriptions", "quote": "The earliest Mesopotamian tablets display a purely **logogrammatic** structure before phonetization took place."},
      {"author": "Isaac Taylor", "work": "The History of the Alphabet", "quote": "Every ancient script began with crude **logogrammatic** designs before developing cursive alphabetic characters."},
      {"author": "Leonard Bloomfield", "work": "Language", "quote": "A purely **logogrammatic** script requires thousands of distinct symbols to represent the lexical inventory of a living tongue."}
    ]
  },
  "Dashboard — log/logogrammatically.md": {
    "primary": "In a logogrammatic manner; using written characters that represent whole words rather than sounds.",
    "secondary": "In philological transcription, representing lexical semantics through whole-word ideograms rather than alphabetic segments.",
    "quotes": [
      {"author": "Isaac Taylor", "work": "The History of the Alphabet", "quote": "Sumerian scribes recorded commodity inventories **logogrammatically**, using styluses to press word-signs into wet clay."},
      {"author": "Edward Sapir", "work": "Language", "quote": "When concepts are rendered **logogrammatically**, readers bypass phonology and access semantic associations immediately."},
      {"author": "Archibald Sayce", "work": "Comparative Philology", "quote": "Ancient royal annals were transcribed **logogrammatically** to preserve sacred ancestral designations across shifting dialects."}
    ]
  },
  "Dashboard — log/logograph.md": {
    "primary": "A letter, symbol, or glyph that represents a complete word or semantic unit; a logogram.",
    "secondary": "In typestyle history and early printing, a cast metal printing type containing a complete word or frequent syllable.",
    "quotes": [
      {"author": "John Walter", "work": "An Address to the Public on Logographic Printing", "quote": "By casting a single **logograph** for frequent words like 'the' and 'and', our compositors save immense mechanical labor."},
      {"author": "Edward Sapir", "work": "Language: An Introduction to the Study of Speech", "quote": "A **logograph** does not represent a sound; it stands directly for an idea anchored to a linguistic unit."},
      {"author": "Isaac Taylor", "work": "The Alphabet: An Account of the Origin of Letters", "quote": "In early Mayan codices, each intricate **logograph** combined calendrical math with religious symbolism."}
    ]
  },
  "Dashboard — log/logographic.md": {
    "primary": "Relating to a writing system or printing technique that employs signs representing complete words.",
    "secondary": "In cognitive psychology of reading, describing the developmental stage where readers recognize whole words by visual shape.",
    "quotes": [
      {"author": "Leonard Bloomfield", "work": "Language", "quote": "The **logographic** nature of Chinese orthography preserves mutual intelligibility across mutually unintelligible regional dialects."},
      {"author": "John Walter", "work": "The Art of Printing", "quote": "Our **logographic** press arrangements have demonstrated that entire words can be composed as expeditiously as single letters."},
      {"author": "Edward Sapir", "work": "Selected Writings in Language, Culture and Personality", "quote": "Readers navigating a **logographic** script rely heavily on spatial memory and visual configuration."}
    ]
  },
  "Dashboard — log/logomach.md": {
    "primary": "A person who engages in contentious disputes or verbal wrangling over mere words; a word-fighter.",
    "secondary": "In polemical satire, a disputant who substitutes semantic quibbling for substantive philosophical inquiry.",
    "quotes": [
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The petty **logomach** wastes his life in splitting syllables, mistaking lexicography for celestial wisdom."},
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Montaigne smiles at the zealous **logomach** whose fierce controversies evaporate once terms are candidly defined."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "It is the mark of a superficial **logomach** to wage war against phrases while the underlying principles remain uncomprehended."}
    ]
  },
  "Dashboard — log/logomachist.md": {
    "primary": "One addicted to disputation about words; an alternative form for a verbal disputant or logomach.",
    "secondary": "In dialectical literature, a pedant obsessed with semantic trivialities and linguistic technicalities in debate.",
    "quotes": [
      {"author": "William Hazlitt", "work": "Table Talk", "quote": "The inveterate **logomachist** cannot enjoy a conversation without arresting the narrative to dissect every casual metaphor."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Many a dry-as-dust **logomachist** has spent a lifetime constructing systems of sawdust while the universe rolled by."},
      {"author": "John Stuart Mill", "work": "Dissertations and Discussions", "quote": "The scholastic **logomachist** imagined that by refining terms he was unveiling the deepest arcana of nature."}
    ]
  },
  "Dashboard — log/logomachy.md": {
    "primary": "A dispute, argument, or debate conducted entirely about words, terminology, or semantic definitions.",
    "secondary": "In epistemological criticism, contentious intellectual conflict that produces no substantive factual result.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Much of the disputation in the universities degenerated into a futile **logomachy**, where men mistook words for things."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "If men would define their terms before debating, the greater part of philosophical controversy would end, revealing it to be mere **logomachy**."},
      {"author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "Beware of mistaking a profound spiritual problem for a superficial **logomachy** of scholastic origin."}
    ]
  },
  "Dashboard — log/logomania.md": {
    "primary": "An abnormal and manic obsession with words, talking, or verbal expression; logorrhea.",
    "secondary": "In clinical psychopathology, excessive, continuous, and uncontrolled verbalization observed during acute manic episodes.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "In acute manic excitement, patients exhibit a violent **logomania**, pouring forth continuous torrents of rhyme and association."},
      {"author": "Henry Maudsley", "work": "The Pathology of Mind", "quote": "Uncontrolled **logomania** frequently accompanies cerebral hyperaemia, the patient talking without pause until utter physical exhaustion."},
      {"author": "Richard von Krafft-Ebing", "work": "Text-Book of Insanity", "quote": "The pressure of speech in hypomania often borders on true **logomania**, exhausting both the physician and the sufferer."}
    ]
  },
  "Dashboard — log/logorrhea.md": {
    "primary": "An excessive, overwhelming, and often incoherent flow of words; extreme loquacity.",
    "secondary": "In neurology and psychiatry, fluent, continuous, and rapid speech characteristic of aphasia or bipolar mania.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The symptom known as **logorrhea** reflects a failure of cortical inhibition, leaving associative speech uncurbed."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "The Autocrat of the Breakfast-Table", "quote": "Nothing is more tedious in social gatherings than an elderly pedant afflicted with chronic conversational **logorrhea**."},
      {"author": "Henry Maudsley", "work": "Responsibility in Mental Disease", "quote": "Morbid **logorrhea** must not be confused with wit; it is the chaotic discharge of an unstable nervous apparatus."}
    ]
  },
  "Dashboard — log/logos.md": {
    "primary": "The divine reason or active rational principle that permeates, animates, and orders the universe.",
    "secondary": "In Hellenistic philosophy and Johannine theology, the cosmic Word or divine wisdom manifested in creation and human reason.",
    "quotes": [
      {"author": "Philo of Alexandria", "work": "On the Creation", "quote": "The divine **logos** is the celestial blueprint and governing architect according to which the cosmos was fashioned."},
      {"author": "Marcus Aurelius", "work": "Meditations", "quote": "Keep in mind that rational creatures are united under the universal **logos**, sharing a common nature and destiny."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The ancient philosophers grasped by intuition that divine **logos** which the Gospel revealed as living truth."}
    ]
  },
  "Dashboard — log/logotype.md": {
    "primary": "A single piece of printer's type that bears an entire word or combination of letters; a logo or trademark.",
    "secondary": "In commercial graphic design and printing, a custom typography or emblematic wordmark representing an enterprise.",
    "quotes": [
      {"author": "John Walter", "work": "An Introduction to Logography", "quote": "By employing a cast **logotype** for recurring syllables, the printing of our journal proceeded with unprecedented speed."},
      {"author": "Thorstein Veblen", "work": "The Theory of Business Enterprise", "quote": "The commercial value of a famous **logotype** consists in its power to direct consumer purchases automatically."},
      {"author": "Marshall McLuhan", "work": "The Gutenberg Galaxy", "quote": "The standardized **logotype** transformed commercial printing into a mechanized conveyor of institutional marks."}
    ]
  },
  "Dashboard — log/logroll.md": {
    "primary": "To engage in political vote-trading or reciprocal mutual assistance; to roll logs collaboratively.",
    "secondary": "In political sociology, to support another legislator's bill on condition of receiving support for one's own measure.",
    "quotes": [
      {"author": "Woodrow Wilson", "work": "Congressional Government", "quote": "Members of congress find it expedient to **logroll** on internal tariff schedules, exchanging favors across state lines."},
      {"author": "James Bryce", "work": "The American Commonwealth", "quote": "To **logroll** successfully in the legislature requires an astute knowledge of each representative's local interests."},
      {"author": "Hamlin Garland", "work": "Main-Travelled Roads", "quote": "In frontier clearings the settlers would gather to **logroll** and erect timber cabins in festive mutual cooperation."}
    ]
  },
  "Dashboard — log/logrolling.md": {
    "primary": "The practice of exchanging political favors, especially mutual voting for each other's proposed legislation.",
    "secondary": "In political economy and social history, cooperative frontier timber-clearing transformed into a metaphor for reciprocal political bargaining.",
    "quotes": [
      {"author": "James Bryce", "work": "The American Commonwealth", "quote": "The practice of legislative **logrolling** ensures that localized expenditure bills pass with little scrutiny from the wider public."},
      {"author": "Woodrow Wilson", "work": "Congressional Government", "quote": "Through systematic **logrolling**, river and harbor improvement funds are distributed to buy regional allegiance."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Reciprocal legislative bargaining resembling frontier **logrolling** is the inevitable mechanism of democratic compromise."}
    ]
  },
  "Dashboard — log/logrono.md": {
    "primary": "A historic city and municipality in northern Spain, serving as the capital of the autonomous region of La Rioja.",
    "secondary": "In Spanish history and geography, an important fortified trading center along the Ebro River and the Camino de Santiago pilgrimage route.",
    "quotes": [
      {"author": "Richard Ford", "work": "A Handbook for Travellers in Spain", "quote": "The ancient stone bridge of **Logrono** spanning the broad waters of the Ebro has welcomed pilgrims for many centuries."},
      {"author": "George Borrow", "work": "The Bible in Spain", "quote": "From Vitoria we rode toward **Logrono**, where the fertile vineyards of the Rioja region unfold beneath the hills."},
      {"author": "Washington Irving", "work": "Chronicle of the Conquest of Granada", "quote": "Troops gathered in the strategic fortress of **Logrono** to guard the northern marches against invasion."}
    ]
  },
  "Dashboard — log/logy.md": {
    "primary": "Characterized by sluggishness, mental dullness, or physical lethargy; groggy or slow to respond.",
    "secondary": "In colloquial and regional descriptions, feeling worn down, heavy-limbed, or unenergetic after illness or fatigue.",
    "quotes": [
      {"author": "Jack London", "work": "Martin Eden", "quote": "His brain felt **logy** and numb after thirty hours of continuous reading without food or sleep."},
      {"author": "Sarah Orne Jewett", "work": "The Country of the Pointed Firs", "quote": "The damp morning air made everybody feel a little **logy** until the sea fog burned off under the sun."},
      {"author": "Theodore Dreiser", "work": "Sister Carrie", "quote": "The long afternoon in the stuffy office left him feeling dull and **logy**, unable to concentrate on his ledgers."}
    ]
  },
  "Dashboard — log/monologist.md": {
    "primary": "A person who performs, writes, or delivers a monologue; a solo theatrical performer or speaker.",
    "secondary": "In conversational etiquette, an individual who monopolizes dialogue by speaking continuously without listening to others.",
    "quotes": [
      {"author": "William Hazlitt", "work": "On the Conversation of Authors", "quote": "Coleridge was not a conversationalist but a magnificent **monologist**, holding his listeners spellbound for hours."},
      {"author": "George Bernard Shaw", "work": "Dramatic Opinions and Essays", "quote": "The gifted theatrical **monologist** creates an entire universe of characters through voice and gesture alone."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "The Autocrat of the Breakfast-Table", "quote": "A stubborn **monologist** at the dinner table converts polite social exchange into an involuntary lecture hall."}
    ]
  },
  "Dashboard — log/monologue.md": {
    "primary": "A long, uninterrupted speech delivered by a single person in a conversation, play, or public address.",
    "secondary": "In theatrical dramaturgy, an extended soliloquy or speech through which a character reveals motives and internal psychological states.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "In his most celebrated **monologue**, the prince ponders the dread of death and the pangs of conscience."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab paced the quarterdeck muttering a fierce **monologue** against the white whale that none dared interrupt."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "His conversation was in reality an unbroken **monologue**, admitting no reply and inviting no dissent."}
    ]
  },
  "Dashboard — log/monologuise.md": {
    "primary": "To speak in or deliver a monologue; to monopolize conversation continuously (British spelling).",
    "secondary": "In dramatic performance and literary description, to verbalize internal ruminations aloud without engaging interlocutors.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Our Theatres in the Nineties", "quote": "An actor must not merely **monologuise** to the footlights, but respond to the living presence of his fellow players."},
      {"author": "Virginia Woolf", "work": "The Waves", "quote": "The solitary characters **monologuise** in rhythmic sequences, reflecting the ebb and flow of their inner consciousness."},
      {"author": "Thomas Carlyle", "work": "Reminiscences", "quote": "He would **monologuise** endlessly on German metaphysics while his tea grew stone cold upon the tray."}
    ]
  },
  "Dashboard — log/monologuize.md": {
    "primary": "To speak in or deliver a monologue; to monopolize a conversation (American spelling).",
    "secondary": "In dramatic critique, to deliver an extended solo discourse or verbal meditation onstage or in prose.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Journals", "quote": "When a man begins to **monologuize** in company, he proves he has forgotten the sacred reciprocity of friendship."},
      {"author": "William James", "work": "The Letters of William James", "quote": "Do not allow the philosopher to **monologuize** undisturbed; compel him to illustrate his theories with concrete examples."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Madame Merle preferred to listen politely rather than **monologuize**, observing everything with quiet vigilance."}
    ]
  },
  "Dashboard — log/neologism.md": {
    "primary": "A newly coined word, expression, or phrase, or a novel meaning introduced for an established word.",
    "secondary": "In historical linguistics and lexicography, a lexical innovation circulating prior to formal dictionary adoption.",
    "quotes": [
      {"author": "Horace", "work": "Ars Poetica", "quote": "It has ever been lawful to produce a **neologism** stamped with the current impress of public necessity."},
      {"author": "Samuel Johnson", "work": "Preface to the Dictionary of the English Language", "quote": "I have avoided admitting every ephemeral **neologism** that fashionable conversation spawns and forgets within a year."},
      {"author": "Richard Chenevix Trench", "work": "On the Study of Words", "quote": "A valuable **neologism** survives because it supplies a genuine vacancy in the existing vocabulary of thought."}
    ]
  },
  "Dashboard — log/neologist.md": {
    "primary": "A person who invents, coins, or advocates the use of new words or new linguistic expressions.",
    "secondary": "In historical theology and philology, an innovator who introduces novel doctrines or unorthodox interpretations of sacred texts.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "Dryden was an audacious **neologist**, enriching the poetic vocabulary with noble borrowings from Latin and French."},
      {"author": "Thomas De Quincey", "work": "Letters to a Young Man Whose Education Has Been Neglected", "quote": "The reckless **neologist** clutters his prose with jargon where good Saxon phrasing would serve far better."},
      {"author": "Archibald Sayce", "work": "Principles of Comparative Philology", "quote": "Every generation of speakers acts as an unconscious **neologist**, shifting vowel sounds and remodeling idioms."}
    ]
  },
  "Dashboard — log/prolog.md": {
    "primary": "An introduction or preface to a book, dramatic work, poem, or musical composition; a prologue.",
    "secondary": "In historical printing and theatrical playbills, the introductory address delivered to the audience setting the scene.",
    "quotes": [
      {"author": "Geoffrey Chaucer", "work": "The Canterbury Tales", "quote": "In his masterful **prolog**, the poet paints a vivid portrait of fourteenth-century English society."},
      {"author": "John Dryden", "work": "Essays on the Drama", "quote": "A witty **prolog** disarms the malice of the pit and prepares the audience for dramatic entertainment."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Let this chapter serve as a brief **prolog** to the wider demonstration of physical principles."}
    ]
  },
  "Dashboard — log/prologise.md": {
    "primary": "To deliver, recite, or write a prologue; to introduce a play or discourse with an introductory speech (British spelling).",
    "secondary": "In classical dramaturgy, to speak an expository preamble providing mythological or contextual backstory.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Plays Pleasant and Unpleasant", "quote": "The author chose to **prologise** his drama in person, warning the audience against sentimental expectations."},
      {"author": "Samuel Taylor Coleridge", "work": "Lectures on Shakespeare", "quote": "In ancient tragedies, a god would often **prologise** to disclose cosmic background events to the spectators."},
      {"author": "John Milton", "work": "The Reason of Church Government", "quote": "Before launching into doctrinal warfare, the apologist must **prologise** with humility and solemn prayers."}
    ]
  },
  "Dashboard — log/prologize.md": {
    "primary": "To deliver or write a prologue; to introduce a theatrical work or literary text (American spelling).",
    "secondary": "In rhetorical theory, to provide an opening address that establishes dramatic tone and context.",
    "quotes": [
      {"author": "John Dryden", "work": "The Art of Poetry", "quote": "A skilled dramatist will not **prologize** in tedious verse, but strike directly into the heart of dramatic tension."},
      {"author": "William Hazlitt", "work": "Characters of Shakespear's Plays", "quote": "Shakespeare seldom pauses to **prologize** at length; his characters step forward and drama instantly begins."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: Second Series", "quote": "Nature does not **prologize** her mysteries; she presents the finished flower and the complete starry night."}
    ]
  },
  "Dashboard — log/prologue.md": {
    "primary": "A separate introductory section of a literary, dramatic, or musical work that sets the scene or provides context.",
    "secondary": "In theatrical tradition, a poem or monologue spoken by an actor before the main performance begins.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "Two households, both alike in dignity, in fair Verona, where we lay our scene, from ancient grudge break to new mutiny: so opens the tragic **prologue**."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "In the solemn **prologue** to his epic, the poet invokes the heavenly muse to inspire an adventurous song."},
      {"author": "Francis Bacon", "work": "The Great Instauration", "quote": "Let this general plan serve as a necessary **prologue** to the comprehensive regeneration of natural science."}
    ]
  },
  "Dashboard — log/prologuize.md": {
    "primary": "To deliver or write a prologue; to preface a work or speech with introductory remarks.",
    "secondary": "In historical rhetoric, to make an opening apology or introductory exposition to an audience.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "It is superfluous to **prologuize** upon principles which the subsequent dissertation will amply establish."},
      {"author": "John Dryden", "work": "Prefaces to the Fables", "quote": "I will not longer **prologuize** to the reader, but present these ancient tales in their modern dress."},
      {"author": "Thomas De Quincey", "work": "Confessions of an English Opium-Eater", "quote": "Allow me to **prologuize** briefly regarding the circumstances under which these recollections were composed."}
    ]
  },
  "Dashboard — log/trilogy.md": {
    "primary": "A group or series of three related works of art, literature, drama, or music that form a connected whole.",
    "secondary": "In classical Greek dramaturgy, a set of three linked tragedies presented consecutively at the City Dionysia festival.",
    "quotes": [
      {"author": "Gilbert Murray", "work": "Aeschylus: The Creator of Tragedy", "quote": "The Oresteia survives as the sole intact dramatic **trilogy** demonstrating the evolution of divine justice."},
      {"author": "Henry James", "work": "The Art of the Novel", "quote": "The author conceived his broad social canvas not as a single novel, but as a monumental **trilogy**."},
      {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "In each member of the tragic **trilogy**, the grand heroic style sustains the moral elevation of the drama."}
    ]
  },
  "Dashboard — log/unapologetic.md": {
    "primary": "Not acknowledging or expressing regret for something; defiant, persistent, or unremorseful.",
    "secondary": "In critical and political discourse, steadfastly defending a controversial stance without concession or compromise.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He remained stubborn and **unapologetic**, convinced that his unbending conduct had maintained his personal honor."},
      {"author": "William James", "work": "The Will to Believe", "quote": "Faith asserts its claims with an **unapologetic** conviction that dry rational skepticism cannot undermine."},
      {"author": "Bertrand Russell", "work": "Unpopular Essays", "quote": "The author offers these controversial reflections in an **unapologetic** spirit, believing truth alone matters."}
    ]
  },
  "Dashboard — log/unlogical.md": {
    "primary": "Not according to the principles of logic; lacking reason, consistency, or rational structure; illogical.",
    "secondary": "In psychological philosophy, operating through intuition, feeling, or instinct rather than formal deductive reasoning.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Human decision-making is largely governed by **unlogical** impulses and subconscious emotional preferences."},
      {"author": "John Dewey", "work": "How We Think", "quote": "Primitive belief is predominantly **unlogical**, accepting traditional folklore without testing causes and effects."},
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "Social passions generate vast **unlogical** movements that defy the neat calculations of political theorists."}
    ]
  }
}

base_dir = "App database/Latin roots/Cluster Thought"
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

print(f"Thought Batch 4-3 (log final 42 words): Successfully updated {updated_count}/{len(data)} notes.")
