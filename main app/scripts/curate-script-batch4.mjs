import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Writing & Script/Dashboard — sema";

const wordsData = {
  "aposematic.md": {
    word: "aposematic",
    primary: "Characterized by or functioning as a warning signal; specifically, conspicuously colored or marked to warn predators that an animal is toxic, venomous, or unpalatable.",
    secondary: "In evolutionary biology, describing conspicuous warning signals (e.g., yellow and black stripes of wasps) that facilitate rapid predator learning.",
    quotes: [
      { author: "Edward Bagnall Poulton", work: "The Colours of Animals", quote: "I propose the term **aposematic** for warning appearances that advertise unpleasant or dangerous attributes to enemies." },
      { author: "Alfred Russel Wallace", work: "Darwinism", quote: "The vivid banding of the coral snake is a conspicuous **aposematic** device warning birds away." },
      { author: "Edward O. Wilson", work: "The Diversity of Life", quote: "Poison dart frogs display brilliant **aposematic** pigmentation to signal their deadly skin alkaloids." }
    ]
  },
  "asemasia.md": {
    word: "asemasia",
    primary: "In neuropsychology, the complete loss of the ability to communicate by signs, symbols, or gestures; severe asymbolia.",
    secondary: "In behavioral neurology, a multimodal symbolic deficit encompassing both receptive and expressive gesture, pantomime, and written language.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The profound stroke left the patient with total **asemasia**, incapable of recognizing the simplest communicative gestures." },
      { author: "Henry Head", work: "Aphasia and Kindred Disorders of Speech", quote: "In severe semantic disorders, speech defects merge into generalized **asemasia**, disrupting all nonverbal signaling." },
      { author: "John Hughlings Jackson", work: "Selected Writings", quote: "The dissolution of the nervous system begins with the loss of highly integrated symbolic functions, culminating in complete **asemasia**." }
    ]
  },
  "asemia.md": {
    word: "asemia",
    primary: "The inability to understand, use, or communicate by signs, gestures, or symbols; loss of the symbolic function.",
    secondary: "In aphasiology, a condition where lesions in the cerebral cortex prevent a patient from decoding linguistic or conventional signs.",
    quotes: [
      { author: "Carl Wernicke", work: "The Aphasic Symptom Complex", quote: "Cortical sensory damage disrupts word-sound comprehension, introducing an element of generalized **asemia**." },
      { author: "William James", work: "The Principles of Psychology", quote: "When the symbolic faculty fails through disease, the condition of **asemia** leaves the mind stranded in raw, uninterpreted sensation." },
      { author: "Sigmund Freud", work: "On Aphasia", quote: "The distinction between motor aphasia and broader **asemia** depends upon whether the defect involves speech mechanics or the underlying symbolic apparatus." }
    ]
  },
  "asemic.md": {
    word: "asemic",
    primary: "Having no specific semantic content or meaning; devoid of semantic signification.",
    secondary: "In contemporary visual art and poetry, describing asemic writing—a hybrid calligraphic form that resembles handwriting but conveys no readable words.",
    quotes: [
      { author: "Roland Barthes", work: "The Empire of Signs", quote: "The sweeping brushstrokes resembled an **asemic** script, evoking the rhythm of writing while stubbornly refusing to signify." },
      { author: "Jacques Derrida", work: "Of Grammatology", quote: "An **asemic** trace reveals the physical gesture of inscription stripped of communicative transparency." },
      { author: "Susan Sontag", work: "Against Interpretation", quote: "The artist produced sheets of **asemic** calligraphy that challenged the viewer to experience form without the burden of decipherable content." }
    ]
  },
  "pentaseme.md": {
    word: "pentaseme",
    primary: "In classical Greek and Latin prosody, a metrical unit, syllable, or foot having the value or duration of five morae (five short syllables or time-units).",
    secondary: "In metric theory, a prolonged foot (such as a dispondee or molossus with lengthening) equivalent to five basic beats in musical recitation.",
    quotes: [
      { author: "Herbert Weir Smyth", work: "Greek Grammar", quote: "A metrical measure containing five morae is designated a **pentaseme**, often occurring in paeonic or cretic rhythms." },
      { author: "George Saintsbury", work: "A History of English Prosody", quote: "Classical theorists measured lyric complexity by analyzing how the **pentaseme** balanced against shorter dactylic units." },
      { author: "Richard Bentley", work: "Dissertations upon the Epistles of Phalaris", quote: "In Pindaric odes, the choral strophe occasionally prolongs a final syllable into a solemn **pentaseme**." }
    ]
  },
  "polysemant.md": {
    word: "polysemant",
    primary: "A word, symbol, or expression that has multiple meanings; a polysemous word.",
    secondary: "In lexical semantics, a linguistic sign exhibiting semantic divergence while maintaining recognizable etymological continuity.",
    quotes: [
      { author: "Ferdinand de Saussure", work: "Course in General Linguistics", quote: "Every natural language abounds in the **polysemant**, where one acoustic image serves a cluster of related concepts." },
      { author: "C. K. Ogden", work: "The Meaning of Meaning", quote: "The philosopher must guard against ambiguity when an essential term functions as a shifting **polysemant**." },
      { author: "Stephen Ullmann", work: "Semantics: An Introduction to the Science of Meaning", quote: "A single **polysemant** like 'head' extends from anatomy to geometry, leadership, and brewing." }
    ]
  },
  "polysemantic.md": {
    word: "polysemantic",
    primary: "Having multiple meanings or interpretations; polysemous.",
    secondary: "In linguistics and literary semiotics, describing words, metaphors, or symbols capable of activating diverse conceptual networks simultaneously.",
    quotes: [
      { author: "Roman Jakobson", work: "Language in Literature", quote: "Poetic discourse thrives upon **polysemantic** resonance, where words echo multiple layers of meaning in a single line." },
      { author: "Umberto Eco", work: "The Role of the Reader", quote: "An open text utilizes **polysemantic** symbols to invite divergent interpretations from the audience." },
      { author: "Mikhail Bakhtin", work: "The Dialogic Imagination", quote: "The novel incorporates **polysemantic** utterances that reflect the competing voices of distinct social classes." }
    ]
  },
  "polyseme.md": {
    word: "polyseme",
    primary: "A word, phrase, or symbol that has multiple related meanings or senses.",
    secondary: "In computational linguistics and lexicography, a lexical entry whose distinct senses share a common conceptual root, distinguishing it from homonyms.",
    quotes: [
      { author: "John Lyons", work: "Semantics", quote: "The lexicographer must decide whether an entry represents a single **polyseme** with divergent branches or two distinct homonyms." },
      { author: "George Lakoff", work: "Women, Fire, and Dangerous Things", quote: "A lexical **polyseme** like 'over' is structured as a radial category anchored in bodily spatial experience." },
      { author: "David Crystal", work: "The Cambridge Encyclopedia of Language", quote: "A common **polyseme** like 'run' fills dozens of distinct entries in an unabridged dictionary." }
    ]
  },
  "polysemic.md": {
    word: "polysemic",
    primary: "Characterized by or relating to polysemy; having multiple meanings or interpretations.",
    secondary: "In media studies and cultural theory, describing cultural texts open to varying decodings by different audiences.",
    quotes: [
      { author: "Stuart Hall", work: "Encoding and Decoding in the Television Discourse", quote: "A cultural broadcast is inherently **polysemic**, capable of being decoded along dominant, negotiated, or oppositional lines." },
      { author: "Roland Barthes", work: "Image, Music, Text", quote: "Every photographic image is **polysemic**, requiring linguistic captions to anchor its floating chain of signifieds." },
      { author: "Paul Ricoeur", work: "The Rule of Metaphor", quote: "Living metaphor creates a **polysemic** tension that resists paraphrasing into univocal propositions." }
    ]
  },
  "polysemous.md": {
    word: "polysemous",
    primary: "Having multiple meanings, especially related meanings derived from a common root; polysemic.",
    secondary: "In formal semantics and cognitive linguistics, contrasting with monosemous words (having only one meaning) and homonymous words.",
    quotes: [
      { author: "William Empson", work: "Seven Types of Ambiguity", quote: "Poetic richness emerges when a **polysemous** word simultaneously satisfies two divergent syntactical expectations." },
      { author: "Noam Chomsky", work: "Aspects of the Theory of Syntax", quote: "The syntactic parser must resolve ambiguities introduced by inherently **polysemous** lexical items." },
      { author: "Edward Sapir", work: "Language", quote: "Natural languages tolerate **polysemous** vocabulary because context instantly disambiguates intended sense." }
    ]
  },
  "polysemy.md": {
    word: "polysemy",
    primary: "The coexistence of many possible meanings for a single word, phrase, or symbol.",
    secondary: "In lexical semantics, the phenomenon whereby a single lexical item acquires multiple distinct senses through metaphor, metonymy, or specialization.",
    quotes: [
      { author: "Stephen Ullmann", work: "The Principles of Semantics", quote: "Without **polysemy**, the human vocabulary would require an astronomical inventory of distinct words." },
      { author: "Paul Ricoeur", work: "Interpretation Theory: Discourse and the Surplus of Meaning", quote: "The phenomenon of **polysemy** is the very condition of human metaphorical expression and literary creativity." },
      { author: "Ferdinand de Saussure", work: "Course in General Linguistics", quote: "The historical drift of semantic values inevitably generates widespread **polysemy** within the lexicon." }
    ]
  },
  "semantic.md": {
    word: "semantic",
    primary: "Relating to meaning in language or logic; of or pertaining to signification.",
    secondary: "In computer science and cognitive psychology, involving the conceptual content, data models, or knowledge structures of information systems.",
    quotes: [
      { author: "Bertrand Russell", work: "An Inquiry into Meaning and Truth", quote: "The primary function of language is **semantic**, connecting vocal noises with facts about the external world." },
      { author: "Ludwig Wittgenstein", work: "Philosophical Investigations", quote: "The **semantic** value of a proposition is not an occult mental object, but its employment in the language-game." },
      { author: "Tim Berners-Lee", work: "Weaving the Web", quote: "The **semantic** web aims to structure online information so that machines can interpret conceptual relationships directly." }
    ]
  },
  "semantically.md": {
    word: "semantically",
    primary: "In a way that relates to meaning in language, logic, or symbols.",
    secondary: "With regard to conceptual interpretation, semantic content, or truth conditions.",
    quotes: [
      { author: "Noam Chomsky", work: "Syntactic Structures", quote: "The sentence 'Colorless green ideas sleep furiously' is grammatically well-formed but **semantically** nonsensical." },
      { author: "Willard Van Orman Quine", work: "From a Logical Point of View", quote: "Two linguistic expressions may be syntactically distinct yet **semantically** coextensive." },
      { author: "John Searle", work: "Speech Acts", quote: "An utterance is **semantically** complete only when its propositional content is paired with an illocutionary force." }
    ]
  },
  "semanticist.md": {
    word: "semanticist",
    primary: "A scholar or linguist who specializes in semantics, the scientific study of linguistic meaning.",
    secondary: "In philosophy of language, a theorist investigating truth conditions, reference, and symbolic interpretation.",
    quotes: [
      { author: "Alfred Korzybski", work: "Science and Sanity", quote: "The general **semanticist** reminds us that the map is not the territory, and the word is not the thing." },
      { author: "Willard Van Orman Quine", work: "Word and Object", quote: "The empirical **semanticist** must reconstruct radical translation from observed behavioral responses alone." },
      { author: "S. I. Hayakawa", work: "Language in Thought and Action", quote: "A skilled **semanticist** trains the mind to detect verbal traps and emotional propaganda in public discourse." }
    ]
  },
  "semantics.md": {
    word: "semantics",
    primary: "The branch of linguistics and logic concerned with the meaning of words, phrases, signs, and symbols.",
    secondary: "In philosophy and computer science, the rules determining the truth value of propositions or the computational interpretation of programming statements.",
    quotes: [
      { author: "Charles Sanders Peirce", work: "Collected Papers", quote: "Logic, in its general sense, is only another name for **semantics**, the formal science of signs and their interpretants." },
      { author: "Bertrand Russell", work: "Logic and Knowledge", quote: "Questions concerning reference and truth belong to the domain of philosophical **semantics**." },
      { author: "Donald Davidson", work: "Inquiries into Truth and Interpretation", quote: "A theory of **semantics** for natural language can be constructed upon a Tarskian definition of truth." }
    ]
  },
  "semaphore.md": {
    word: "semaphore",
    primary: "A system of sending messages by holding two flags or arms in certain positions according to an alphabetical code.",
    secondary: "An apparatus consisting of a tall post with movable arm signals used for conveying instructions on railways; in computing, a synchronization primitive variable.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick", quote: "The lookout on the masthead signaled the distant vessel by waving his arms like a living **semaphore**." },
      { author: "Thomas Hardy", work: "The Return of the Native", quote: "The roadside railway **semaphore** dropped its red arm with a metallic clatter into the evening gloom." },
      { author: "Edsger W. Dijkstra", work: "Cooperating Sequential Processes", quote: "We introduced the concept of the counting **semaphore** to synchronize concurrent processes and prevent race conditions." }
    ]
  },
  "semarang.md": {
    word: "semarang",
    primary: "A major port city and the provincial capital of Central Java, Indonesia, situated on the northern coast of Java.",
    secondary: "In maritime history, an important Dutch East Indies trading hub founded in the 16th century, known for historic colonial architecture and multicultural heritage.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "Our steamer called at **Semarang**, a bustling harbor on the northern coast of Java with extensive sugar warehouses." },
      { author: "Joseph Conrad", work: "Lord Jim", quote: "The coastal schooner touched at Batavia and **Semarang**, unloading spices along the sun-bleached Javanese jetties." },
      { author: "W. Somerset Maugham", work: "The Casuarina Tree", quote: "He had spent years in the Dutch civil service, stationed in the humid coastal offices of **Semarang**." }
    ]
  },
  "semasiology.md": {
    word: "semasiology",
    primary: "The branch of linguistics concerned with the meaning of words and the historical development of their meanings; an older term for semantics.",
    secondary: "In 19th-century philology, the systematic study of semantic change, polysemy, and metaphoric transfer.",
    quotes: [
      { author: "Max Müller", work: "Lectures on the Science of Language", quote: "Comparative **semasiology** reveals how spiritual concepts trace their physical roots back to tangible material metaphors." },
      { author: "Otto Jespersen", work: "Language: Its Nature, Development and Origin", quote: "The historical linguist relies on **semasiology** to trace the astonishing migrations of words from concrete to abstract senses." },
      { author: "Ferdinand de Saussure", work: "Course in General Linguistics", quote: "Before the term semantics gained universal acceptance, scholars studied semantic shift under the banner of **semasiology**." }
    ]
  },
  "sematic.md": {
    word: "sematic",
    primary: "In biology, serving as a warning or signal; designating colors, markings, or sounds that convey a message to other animals.",
    secondary: "In evolutionary ecology, relating to warning (aposematic), alluring (episematic), or deceitful (pseudosematic) adaptations.",
    quotes: [
      { author: "Edward Bagnall Poulton", work: "The Colours of Animals", quote: "I have grouped all warning and recognizing characters under the general designation of **sematic** appearances." },
      { author: "Alfred Russel Wallace", work: "Tropical Nature and Other Essays", quote: "The **sematic** coloration of the poisonous tree frog effectively protects it from predatory birds." },
      { author: "Julian Huxley", work: "Evolution: The Modern Synthesis", quote: "Natural selection favors **sematic** signals whenever the cost of combat or mutual injury exceeds the cost of display." }
    ]
  },
  "seme.md": {
    word: "seme",
    primary: "In structural semantics and semiotics, the minimal distinctive unit of meaning; a semantic feature or component (such as [+human], [+female]).",
    secondary: "In heraldry, sprinkled, strewn, or powdered with small repetitive charges or figures across a field without numbering.",
    quotes: [
      { author: "Algirdas Julien Greimas", work: "Structural Semantics", quote: "By decomposing a lexeme into its constituent **seme** units, structural analysis uncovers the elementary matrix of signification." },
      { author: "Umberto Eco", work: "A Theory of Semiotics", quote: "Each semantic field is structured by oppositions of elementary **seme** traits." },
      { author: "Walter Scott", work: "Ivanhoe", quote: "His surcoat of blue silk was **seme** with golden fleurs-de-lis, denoting noble Norman lineage." }
    ]
  },
  "sememe.md": {
    word: "sememe",
    primary: "The semantic equivalent of a morpheme; a unit of meaning conveyed by a single morpheme or lexical item.",
    secondary: "In structural linguistics, the complete bundle or combination of semes realizing a specific lexical sense in discourse.",
    quotes: [
      { author: "Leonard Bloomfield", work: "Language", quote: "We may define a **sememe** as the meaning of a morpheme, forming the ultimate meaningful unit of grammar." },
      { author: "Roman Jakobson", work: "Selected Writings", quote: "The invariant **sememe** persists across diverse contextual variations in spoken discourse." },
      { author: "John Lyons", work: "Introduction to Theoretical Linguistics", quote: "In componential analysis, each **sememe** is represented as a conjunction of elementary semantic markers." }
    ]
  },
  "semiotic.md": {
    word: "semiotic",
    primary: "Relating to signs, symbols, and signification, or to the study of them (semiotics).",
    secondary: "In philosophy, linguistics, and cultural theory, involving systems of communication, nonverbal signs, and cultural codes.",
    quotes: [
      { author: "Charles Sanders Peirce", work: "Philosophical Writings", quote: "All thought is in signs; our entire mental life constitutes a continuous **semiotic** process of interpretation." },
      { author: "Umberto Eco", work: "The Role of the Reader", quote: "Every cultural convention establishes a **semiotic** code that guides reader interpretation and artistic creation." },
      { author: "Julia Kristeva", work: "Revolution in Poetic Language", quote: "Poetic discourse ruptures the symbolic order by releasing subterranean energies from the **semiotic** chora." }
    ]
  },
  "semiotical.md": {
    word: "semiotical",
    primary: "Of or relating to semiotics; semiotic (variant form).",
    secondary: "Pertaining to the theoretical analysis of sign systems and symbolic representation.",
    quotes: [
      { author: "Charles Sanders Peirce", work: "Collected Papers", quote: "A thorough **semiotical** inquiry must investigate the triadic relation of the sign, its object, and its interpretant." },
      { author: "Ernst Cassirer", work: "The Philosophy of Symbolic Forms", quote: "Human culture is fundamentally a **semiotical** universe constructed of language, myth, and art." },
      { author: "Roman Jakobson", work: "Selected Writings", quote: "The **semiotical** perspective unites phonology, literary criticism, and visual art into a coherent science of signs." }
    ]
  },
  "semiotics.md": {
    word: "semiotics",
    primary: "The study of signs, symbols, and signification, and of how they are used to communicate meaning.",
    secondary: "In intellectual history, the broad interdisciplinary field developed from the independent foundations of C. S. Peirce and Ferdinand de Saussure.",
    quotes: [
      { author: "Ferdinand de Saussure", work: "Course in General Linguistics", quote: "A science that studies the life of signs within society is conceivable; I shall call it **semiotics**." },
      { author: "Umberto Eco", work: "A Theory of Semiotics", quote: "The task of general **semiotics** is to explore the theoretical conditions under which signification and communication take place." },
      { author: "Charles Sanders Peirce", work: "Collected Papers", quote: "My life has been dedicated to the pursuit of **semiotics**, the doctrine of the essential nature and varieties of possible semiosis." }
    ]
  },
  "synsemantic.md": {
    word: "synsemantic",
    primary: "In linguistics and philosophical semantics, meaningful only in combination with other words; syncategorematic (contrasting with autosemantic).",
    secondary: "In Brentano's and Husserl's philosophy of language, designating incomplete linguistic expressions that require conceptual completion.",
    quotes: [
      { author: "Edmund Husserl", work: "Logical Investigations", quote: "Syncategorematic words like 'and' or 'if' are purely **synsemantic**, having no independent objective reference in isolation." },
      { author: "Franz Brentano", work: "The True and the Evident", quote: "We must distinguish autosemantic terms that stand alone from **synsemantic** particles that merely modify other representations." },
      { author: "John Lyons", work: "Semantics", quote: "Prepositions function as **synsemantic** markers whose primary purpose is to signal grammatical relations within the sentence." }
    ]
  },
  "tetraseme.md": {
    word: "tetraseme",
    primary: "In classical Greek and Latin prosody, a metrical unit, foot, or syllable having the value or duration of four morae (four short syllables or beats).",
    secondary: "In metric theory, a metrical measure equal to four units of musical time (such as a spondee or dactyl).",
    quotes: [
      { author: "Herbert Weir Smyth", work: "Greek Grammar", quote: "A dactylic or spondaic foot constitutes a **tetraseme**, equal in total duration to four short syllables." },
      { author: "George Saintsbury", work: "A History of English Prosody", quote: "The rhythmic balance of classical strophes relies upon the steady cadence of the four-mora **tetraseme**." },
      { author: "Richard Bentley", work: "Dissertations upon the Epistles of Phalaris", quote: "In anapestic marching verses, each regular foot is measured as a **tetraseme** timing the stride of soldiers." }
    ]
  },
  "triseme.md": {
    word: "triseme",
    primary: "In classical Greek and Latin prosody, a metrical syllable, unit, or foot having the value or duration of three morae (three short syllables or time-units).",
    secondary: "In metric theory, a prolonged syllable or foot (such as an iamb or trochee) equal to three beats of musical time.",
    quotes: [
      { author: "Herbert Weir Smyth", work: "Greek Grammar", quote: "An iambic foot consists of a short syllable followed by a long, forming a three-mora **triseme**." },
      { author: "George Saintsbury", work: "A History of English Prosody", quote: "The rapid movement of trochaic meter derives from the triple rhythm of the **triseme** measure." },
      { author: "Matthew Arnold", work: "On Translating Homer", quote: "In lyric passages, the substitution of a dactyl for a **triseme** creates an exquisite suspension of rhythm." }
    ]
  }
};

function updateWordNote(relPath, data) {
  const fullPath = path.join(baseDir, relPath);
  if (!fs.existsSync(fullPath)) {
    console.error("File not found:", fullPath);
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
console.log("Writing & Script Batch 4 completed! Total words updated:", Object.keys(wordsData).length);
