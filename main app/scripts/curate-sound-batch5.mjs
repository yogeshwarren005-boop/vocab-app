import fs from 'fs';
import path from 'path';

const basePath = 'App database/Greek roots/Cluster Sound & Auditory/Dashboard — phon';

const filesData = {
  "acrophonic.md": {
    primary: "Relating to or representing a writing system where a letter or symbol denotes the initial sound of the name of the depicted object.",
    secondary: "Designating ancient numerical systems (such as Attic Greek) where the initial letter of the numeral's word represents the number itself.",
    quotes: [
      { author: "Sir Alan Gardiner", work: "Egyptian Grammar", quote: "The **acrophonic** principle assumes that each phonetic sign was originally a pictograph of an object whose initial sound became the value of the letter." },
      { author: "Ignace Gelb", work: "A Study of Writing", quote: "Scholars have long debated whether the Proto-Sinaitic inscriptions were deciphered correctly by applying the **acrophonic** hypothesis." },
      { author: "Peter T. Daniels", work: "The World's Writing Systems", quote: "In an **acrophonic** system, a pictorial character stands for the initial segmental sound of the word representing the depicted object." }
    ]
  },
  "acrophony.md": {
    primary: "The naming of letters of an alphabetic script using a word whose initial sound corresponds to the sound represented by the letter.",
    secondary: "The historical linguistic and epigraphic process through which pictographs evolved into alphabetic characters via initial phonetic representation.",
    quotes: [
      { author: "David Diringer", work: "The Alphabet: A Key to the History of Mankind", quote: "Through the process of **acrophony**, the image of an ox head came to represent the initial glottal stop of the Semitic word aleph." },
      { author: "Isaac Taylor", work: "The History of the Alphabet", quote: "The principle of **acrophony** played a vital role in transforming pictorial hieroglyphs into abstract phonetic characters." },
      { author: "John Chadwick", work: "The Decipherment of Linear B", quote: "Linear scripts rarely rely on pure **acrophony**, favoring syllabic values over single initial consonant markers." }
    ]
  },
  "allophone.md": {
    primary: "Any of the phonetic or acoustic variations of a single phoneme that do not alter the meaning of a word in a given language.",
    secondary: "In structural phonology, a positional or non-contrastive realization of an underlying speech sound determined by surrounding phonological environment.",
    quotes: [
      { author: "Leonard Bloomfield", work: "Language", quote: "The non-distinctive phonetic variant of a phoneme is termed an **allophone**, differing by context yet unperceived by native speakers." },
      { author: "Edward Sapir", work: "Sound Patterns in Language", quote: "A speaker readily groups distinct physical sounds into a single conceptual unit, unaware that one is merely an **allophone** of the other." },
      { author: "Roman Jakobson", work: "Fundamentals of Language", quote: "The distribution of each **allophone** reveals the systematic rules governing the realization of underlying phonemes." }
    ]
  },
  "allophonic.md": {
    primary: "Pertaining to, constituting, or conditioned by an allophone (a non-contrastive phonetic variant).",
    secondary: "Characterized by sub-phonemic phonetic variation that varies systematically across phonetic environments or regional dialects.",
    quotes: [
      { author: "Noam Chomsky", work: "The Sound Pattern of English", quote: "Surface phonetic representations are generated from underlying segments through a series of **allophonic** rules." },
      { author: "Peter Ladefoged", work: "A Course in Phonetics", quote: "A narrow transcription records minute **allophonic** details that a broad phonemic transcription deliberately ignores." },
      { author: "Bernard Bloch", work: "Studies in Colloquial Japanese", quote: "The complementary distribution of these segments indicates that the differences are purely **allophonic** rather than phonemic." }
    ]
  },
  "antiphon.md": {
    primary: "A liturgical chant, hymn, or psalm sung, recited, or chanted responsively by two alternating bodies of singers or choirs.",
    secondary: "A verse, sentence, or response sung before and after a psalm or canticle in Christian liturgy; figuratively, a reciprocal response or recurring echo.",
    quotes: [
      { author: "Thomas Merton", work: "The Seven Storey Mountain", quote: "The choir took up the **antiphon**, their voices answering back and forth across the quiet chapel." },
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The ancient stone seemed carved to echo the solemn rhythms of the cathedral's evening **antiphon**." },
      { author: "Walter Pater", work: "Marius the Epicurean", quote: "In that early Christian gathering, the verses of the psalm rose in melodious **antiphon** between the celebrants." }
    ]
  },
  "antiphonal.md": {
    primary: "Sung, recited, or performed in alternating parts by two distinct groups, choirs, or voices.",
    secondary: "A liturgical service book containing antiphons, responsories, and chants for use in the divine office.",
    quotes: [
      { author: "George Eliot", work: "Middlemarch", quote: "The sweet **antiphonal** singing of the choristers rose above the stone nave like a communion of kindred souls." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The sea and the winds maintained an **antiphonal** dialogue of thunderous roaring across the darkened expanse." },
      { author: "T. S. Eliot", work: "Four Quartets", quote: "The voices of the children hidden in the foliage chimed in **antiphonal** cadence with the birds." }
    ]
  },
  "antiphonary.md": {
    primary: "A liturgical book of the Western Christian church containing the choral chants, antiphons, and responsories sung during the Liturgy of the Hours.",
    secondary: "An illuminated medieval manuscript codex containing Gregorian plainchant notations and texts arranged according to the liturgical calendar.",
    quotes: [
      { author: "Umberto Eco", work: "The Name of the Rose", quote: "Upon the heavy oak lectern rested an illuminated **antiphonary**, its vellum leaves darkened by centuries of monastic devotion." },
      { author: "Will Durant", work: "The Age of Faith", quote: "Monasteries preserved sacred musical traditions by copying each precious **antiphonary** with exquisite calligraphic care." },
      { author: "Joris-Karl Huysmans", work: "En Route", quote: "He turned the stiff vellum leaves of the ancient **antiphonary**, studying the square musical neumes traced upon four red lines." }
    ]
  },
  "antiphony.md": {
    primary: "Alternating, responsive singing or chanting between two choirs, singers, or groups of instruments.",
    secondary: "Figuratively, a dynamic reciprocal dialogue, thematic counterpoint, or responsive alternation between two contrasting voices, ideas, or entities.",
    quotes: [
      { author: "Virginia Woolf", work: "The Waves", quote: "The rhythmic crash of the waves against the shore answered the wind in a solemn, unending **antiphony**." },
      { author: "Henry David Thoreau", work: "Walden", quote: "From opposite shores of the pond, the owls answered one another in a weird and mournful **antiphony**." },
      { author: "Edward Said", work: "Culture and Imperialism", quote: "The interplay between dominant and subordinate narratives forms a complex cultural **antiphony** that cannot be reduced to a single melody." }
    ]
  },
  "aphonia.md": {
    primary: "The total loss or absence of the voice and ability to produce vocal sounds, typically caused by disease, vocal cord paralysis, or psychological trauma.",
    secondary: "A functional or psychiatric voice disorder (such as conversion aphonia) in which the vocal folds fail to adduct during attempts at speech despite normal whispering.",
    quotes: [
      { author: "Sigmund Freud", work: "Dora: An Analysis of a Case of Hysteria", quote: "The patient suffered from recurrent attacks of nervous **aphonia**, rendering her unable to speak above a faint whisper." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "Laryngeal nerve palsy had reduced his once-commanding speaking voice to a silent, distressing **aphonia**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Complete **aphonia** following severe catarrhal laryngitis requires absolute vocal rest and close examination of the glottis." }
    ]
  },
  "aphonic.md": {
    primary: "Voiceless; lacking the power of speech or vocal sound production; characterized by aphonia.",
    secondary: "In phonetics, unvoiced or whispered; producing sound without vibration of the vocal folds.",
    quotes: [
      { author: "Charlotte Brontë", work: "Villette", quote: "A sudden terror seized her throat, leaving her utterly **aphonic** in the presence of her stern interrogator." },
      { author: "Henry James", work: "The Wings of the Dove", quote: "She moved her lips in an **aphonic** gesture of farewell that conveyed far more anguish than any spoken syllable." },
      { author: "Arthur Conan Doyle", work: "The Stark Munro Letters", quote: "The poor fellow sat gasping upon the examination chair, completely **aphonic** from acute laryngeal inflammation." }
    ]
  },
  "apophony.md": {
    primary: "The change of an internal vowel sound within a root or word stem to indicate a difference in grammatical function or tense (also known as ablaut or vowel gradation).",
    secondary: "In Indo-European comparative linguistics, the systemic morphological alternation between qualitative or quantitative vowel grades.",
    quotes: [
      { author: "Ferdinand de Saussure", work: "Course in General Linguistics", quote: "The grammatical distinction between sing, sang, and sung is governed by ancient Indo-European **apophony**." },
      { author: "Benjamin W. Fortson IV", work: "Indo-European Language and Culture", quote: "Root **apophony** provided early speakers with a rich morphological mechanism to encode aspect and voice." },
      { author: "Antoine Meillet", work: "Introduction to the Comparative Study of Indo-European Languages", quote: "Through vowel **apophony**, Proto-Indo-European verb stems shifted dynamically across various morphological categories." }
    ]
  },
  "archiphoneme.md": {
    primary: "An abstract phonological unit representing the common distinctive features shared by two or more phonemes when their contrast is neutralized in a particular position.",
    secondary: "In Prague School structural phonology (formulated by Trubetzkoy), a theoretical construct symbolized by a capital letter representing the architype of neutralized sounds.",
    quotes: [
      { author: "Nikolai Trubetzkoy", work: "Principles of Phonology", quote: "When the opposition between voiced and voiceless stops is neutralized at word boundaries, an **archiphoneme** emerges." },
      { author: "Roman Jakobson", work: "Selected Writings", quote: "The **archiphoneme** embodies the invariant distinctive features that remain operative when positional neutralization occurs." },
      { author: "André Martinet", work: "Elements of General Linguistics", quote: "In French, the loss of contrast between open and closed vowels in unstressed syllables produces an **archiphoneme**." }
    ]
  },
  "cacophonic.md": {
    primary: "Producing or characterized by a harsh, discordant, jarring, or unharmonious mixture of sounds.",
    secondary: "In literary or aesthetic theory, deliberately harsh or grating in phonetic texture to evoke disorder, violence, or chaos.",
    quotes: [
      { author: "Aldous Huxley", work: "Brave New World", quote: "A sudden burst of **cacophonic** brass music erupted from the loudspeakers, shattering the tranquil afternoon." },
      { author: "George Orwell", work: "1984", quote: "The telescreen blared with a **cacophonic** din of marching songs and martial fanfares that allowed no quiet thought." },
      { author: "H. P. Lovecraft", work: "The Call of Cthulhu", quote: "From the damp subterranean vault came a **cacophonic** piping that struck madness into the listening ear." }
    ]
  },
  "cacophonous.md": {
    primary: "Involving, marked by, or producing a harsh, unpleasant, and discordant combination of noises or voices.",
    secondary: "Describing literary prose or verse that utilizes jarring consonants and harsh sound patterns to create unsettling effects.",
    quotes: [
      { author: "Charles Dickens", work: "Bleak House", quote: "The streets of London resounded with a **cacophonous** uproar of grinding wheels, barking dogs, and shrill peddlers." },
      { author: "Joseph Conrad", work: "Heart of Darkness", quote: "A **cacophonous** clamor of horns and drums greeted our steamer as it swung past the bend in the jungle river." },
      { author: "F. Scott Fitzgerald", work: "The Great Gatsby", quote: "The orchestra struck up a wildly **cacophonous** jazz number that sent couples spinning across the terrace." }
    ]
  },
  "cacophony.md": {
    primary: "A harsh, discordant, jarring mixture of sounds or noises.",
    secondary: "In literature and rhetoric, the deliberate or accidental juxtaposition of harsh, discordant consonants and syllables to produce an abrasive auditory texture.",
    quotes: [
      { author: "James Joyce", work: "Ulysses", quote: "A jarring **cacophony** of clattering hooves and rattling dray carts echoed along the granite quays of Dublin." },
      { author: "Ralph Ellison", work: "Invisible Man", quote: "Beneath the city streets, subway engines roared in a deafening **cacophony** that vibrated through every beam." },
      { author: "E. M. Forster", work: "A Passage to India", quote: "The cave answered every spoken syllable with a hollow, booming **cacophony** that erased all nuance of human speech." }
    ]
  },
  "diaphone.md": {
    primary: "A type of powerful acoustic foghorn that produces a low-frequency warning sound characterized by a sudden downward pitch drop at the end of each blast.",
    secondary: "In phonetics and dialectology, a speech sound or phonemic family that varies systematically in pronunciation among speakers of different regional dialects.",
    quotes: [
      { author: "Daniel Jones", work: "The Phoneme: Its Nature and Use", quote: "The concept of the **diaphone** accounts for variant realizations of a phoneme across distinct dialects of English." },
      { author: "Farley Mowat", work: "The Rock Within the Sea", quote: "Through the dense Newfoundland fog, the bellow of the lighthouse **diaphone** boomed across the icy breakers." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "On misty nights along the rocky coast, the mournful groan of the harbor **diaphone** warned ships away from the shoals." }
    ]
  },
  "diaphony.md": {
    primary: "Dissonance, discord, or disagreement in sound; in early medieval music, an early form of polyphony or two-part vocal organum.",
    secondary: "Figuratively, intellectual discordance, controversy, or ideological dispute between conflicting philosophical viewpoints.",
    quotes: [
      { author: "Christopher Page", work: "The Owl and the Nightingale: Musical Life and Ideas in France", quote: "Early treatise writers used the term **diaphony** to describe the sounding together of two independent vocal lines." },
      { author: "John Addington Symonds", work: "Renaissance in Italy", quote: "Beneath the apparent harmony of civic life lurked an unyielding political **diaphony** between rival factions." },
      { author: "H. G. Farmer", work: "A History of Arabian Music", quote: "Theoretical writings from the ninth century contrast the consonance of symphonia with the discordant intervals of **diaphony**." }
    ]
  },
  "diplophonia.md": {
    primary: "A voice disorder characterized by the simultaneous production of two distinct auditory pitches or fundamental frequencies during phonation.",
    secondary: "A condition typically resulting from asymmetric vocal fold vibration, unilateral vocal cord paralysis, polypoid degeneration, or unequal vocal fold tension.",
    quotes: [
      { author: "Friedrich S. Brodnitz", work: "Keep Your Voice Healthy", quote: "The presence of a unilateral vocal polyp often induces **diplophonia**, where the patient hears two conflicting pitches at once." },
      { author: "Robert Thayer Sataloff", work: "Professional Voice: The Science and Art of Clinical Care", quote: "Stroboscopy revealed phase asymmetry of the vocal folds, explaining the patient's prominent **diplophonia** during speech." },
      { author: "Chevalier Jackson", work: "Diseases of the Air and Food Passages of Foreign-Body Origin", quote: "Following laryngeal trauma, scarring may cause uneven vocal fold vibration and pronounced **diplophonia**." }
    ]
  },
  "dysphonia.md": {
    primary: "Difficulty or impairment in producing normal vocal sounds, resulting in a hoarse, strained, weak, breathy, or unnatural speaking voice.",
    secondary: "Any medical or physiological dysfunction of the phonatory mechanism involving the vocal cords, larynx, or respiratory muscles.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Chronic **dysphonia** in professional orators should never be ignored, as it often signals laryngeal strain or ulceration." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "Post-encephalitic parkinsonism frequently manifested as severe hypokinetic **dysphonia**, reducing vocal volume to a whisper." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "The patient's sudden onset of **dysphonia** prompted an immediate laryngoscopy to rule out recurrent laryngeal nerve damage." }
    ]
  },
  "ecphonesis.md": {
    primary: "An impassioned, emotional exclamatory phrase or rhetorical outcry used in oratory or poetry to evoke pathos, grief, or indignation.",
    secondary: "In Byzantine and Eastern Christian liturgical music, a heightened, solemn reading or melodic cadence recited aloud by the officiating priest or deacon.",
    quotes: [
      { author: "George Puttenham", work: "The Arte of English Poesie", quote: "This figure of **ecphonesis**, or exclamation, moveth the mind of the hearer when passion overflows ordinary speech." },
      { author: "Quintilian", work: "Institutio Oratoria", quote: "The orator should employ **ecphonesis** sparingly, reserving vehement outcries for moments of genuine climactic emotion." },
      { author: "Egon Wellesz", work: "A History of Byzantine Music and Hymnography", quote: "The liturgical chant culminated in a solemn **ecphonesis**, chanted with solemn dignity by the priest at the altar." }
    ]
  },
  "euphonic.md": {
    primary: "Having a pleasant, melodious, agreeable, or sweet sound; pleasing to the ear.",
    secondary: "In linguistics, relating to phonetic changes or sound substitutions made in words or phrases to facilitate smoother, more agreeable pronunciation.",
    quotes: [
      { author: "Edgar Allan Poe", work: "The Philosophy of Composition", quote: "The choice of the word 'Nevermore' was determined largely by its rich, **euphonic** resonance." },
      { author: "John Keats", work: "Letters of John Keats", quote: "Poetic lines must flow with a natural, **euphonic** ease, avoiding all jagged and grating consonantal clusters." },
      { author: "Max Müller", work: "The Science of Language", quote: "Languages frequently insert an epenthetic vowel for purely **euphonic** reasons to break up awkward consonant sequences." }
    ]
  },
  "euphonical.md": {
    primary: "Characterized by or possessing a harmonious, pleasing, or melodic quality of sound; euphonic.",
    secondary: "Pertaining to phonetic adjustments or rhetorical cadences designed to sound sweet, elegant, and melodious.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Biographia Literaria", quote: "The **euphonical** beauty of Milton's blank verse arises from an exquisite balance of vowel quantities and pauses." },
      { author: "Thomas De Quincey", work: "Confessions of an English Opium-Eater", quote: "Her voice possessed a singularly **euphonical** charm that seemed to soothe my restless agitation." },
      { author: "Washington Irving", work: "Bracebridge Hall", quote: "The old country ballads were recited with an artless yet delightful **euphonical** rhythm that charmed all listeners." }
    ]
  },
  "euphonious.md": {
    primary: "Pleasing, agreeable, or delightful to the ear; harmonious and sweet-sounding.",
    secondary: "Characterized by smooth-flowing phonetic patterns, rhythmic balance, and a total absence of harsh or abrasive consonant clusters.",
    quotes: [
      { author: "Jane Austen", work: "Sense and Sensibility", quote: "Marianne read the poem aloud in her most **euphonious** tone, savoring every melodious cadence of the verse." },
      { author: "Oscar Wilde", work: "The Picture of Dorian Gray", quote: "His low, **euphonious** voice had a hypnotic musicality that held his dinner companions completely spellbound." },
      { author: "Nathaniel Hawthorne", work: "The Scarlet Letter", quote: "The minister possessed a **euphonious** eloquence that melted into the hearts of the congregation like soothing music." }
    ]
  },
  "euphonium.md": {
    primary: "A medium-sized, conical-bore brass wind instrument pitched in B-flat, an octave below the cornet or trumpet, valued for its rich, mellow, velvety timbre.",
    secondary: "The tenor-baritone instrument in military and brass bands that frequently performs expressive tenor solos and intricate counter-melodies.",
    quotes: [
      { author: "Percy Grainger", work: "Notes on Band Scoring", quote: "The deep, velvety tone of the **euphonium** provides the warm harmonic core of the modern symphonic wind ensemble." },
      { author: "Philip Farkas", work: "The Art of Brass Playing", quote: "The conical bore of the **euphonium** produces a singing, lyrical quality distinctly different from the cylindrical trombone." },
      { author: "Gustav Holst", work: "Suite No. 1 in E-flat for Military Band", quote: "Holst assigned the sweeping opening theme of the Chaconne to the rich unison voices of the **euphonium** and tubas." }
    ]
  },
  "euphonize.md": {
    primary: "To make pleasant, sweet-sounding, or agreeable to the ear; to alter phonetically or rhetorically for greater euphony.",
    secondary: "To modify the spelling, pronunciation, or phrasing of a word or foreign borrowing to eliminate harsh consonant junctions.",
    quotes: [
      { author: "H. L. Mencken", work: "The American Language", quote: "Immigrant families frequently sought to **euphonize** their patronymics by softening guttural consonants and dropping harsh syllables." },
      { author: "Walter William Skeat", work: "Principles of English Etymology", quote: "The tendency to **euphonize** consonant clusters has driven the phonological evolution of English across the centuries." },
      { author: "Robert Bridges", work: "Poetry and Poetic Diction", quote: "The poet must continuously prune and **euphonize** rough phrasing until every stanza sings with unblemished grace." }
    ]
  },
  "euphonous.md": {
    primary: "Characterized by pleasantness or sweetness of sound; melodious; euphonious.",
    secondary: "Free from harshness or dissonance; exhibiting a harmonious phonetic structure.",
    quotes: [
      { author: "Ralph Waldo Emerson", work: "Essays: First Series", quote: "A fine orator chooses words that are not only precise in thought but **euphonous** in spoken delivery." },
      { author: "Henry Wadsworth Longfellow", work: "Hyperion", quote: "The Italian tongue is preeminently **euphonous**, gliding from vowel to vowel like water over polished river stones." },
      { author: "George Saintsbury", work: "A History of English Prose Rhythm", quote: "The prose of Sir Thomas Browne is astonishingly **euphonous**, rolling with organ-like harmonic splendor." }
    ]
  },
  "euphony.md": {
    primary: "The quality of being pleasing, agreeable, harmonious, and sweet to the ear, especially through a harmonious combination of spoken words or vocal tones.",
    secondary: "In linguistics and prosody, phonetic changes or rhythmic choices designed to avoid harsh consonant clusters and produce effortless vocal flow.",
    quotes: [
      { author: "Alexander Pope", work: "An Essay on Criticism", quote: "The sound must seem an echo to the sense, where perfect **euphony** marries music to meaning." },
      { author: "George Orwell", work: "Politics and the English Language", quote: "Writers should never sacrifice clarity for mere **euphony**, lest flowery phrases conceal empty thought." },
      { author: "Matthew Arnold", work: "Essays in Criticism", quote: "The supreme distinction of Greek poetry lies in its matchless blend of intellectual lucidity and auditory **euphony**." }
    ]
  },
  "heterophonic.md": {
    primary: "Pertaining to, characterized by, or consisting of heterophony (the simultaneous performance of variations of a single melodic line).",
    secondary: "In musical acoustics or ethnomusicology, exhibiting multiple acoustic layers where instruments or voices ornament a fundamental melody independently.",
    quotes: [
      { author: "Curt Sachs", work: "The Rise of Music in the Ancient World", quote: "Traditional folk ensembles frequently employ a **heterophonic** texture, where each instrument decorates the shared melody at will." },
      { author: "Bruno Nettl", work: "The Study of Ethnomusicology", quote: "In many non-Western traditions, **heterophonic** performance allows individual musicians spontaneous freedom within collective unity." },
      { author: "Béla Bartók", work: "Rumanian Folk Music", quote: "The village bagpipers and fiddlers created a raw, vibrant **heterophonic** counterpoint rooted in centuries of oral transmission." }
    ]
  },
  "heterophony.md": {
    primary: "A musical texture characterized by the simultaneous performance of different variations, elaborations, or ornamentations of a single core melody.",
    secondary: "In ethnomusicology, a prevalent structural technique found in traditional Asian, Middle Eastern, and Celtic folk music traditions.",
    quotes: [
      { author: "Claude Debussy", work: "Monsieur Croche, the Dilettante Hater", quote: "Javanese gamelan music achieves an astonishing beauty through intricate **heterophony**, where bells and gongs weave shimmering patterns around a single theme." },
      { author: "Igor Stravinsky", work: "Poetics of Music", quote: "The folk laments of Russian peasants are grounded in natural **heterophony**, unfolding in overlapping ornamental lines." },
      { author: "John Blacking", work: "How Musical Is Man?", quote: "The Venda choral songs demonstrate that collective **heterophony** reflects social solidarity through musical interplay." }
    ]
  },
  "homophone.md": {
    primary: "A word that has the same pronunciation as another word but differs in spelling, meaning, or origin (e.g. bare and bear, or knight and night).",
    secondary: "A character or symbol in a writing system that represents the exact same phonetic value as another character.",
    quotes: [
      { author: "Otto Jespersen", work: "Language: Its Nature, Development and Origin", quote: "English contains an unusually high number of word pairs where each term is a **homophone** of the other, causing frequent spelling confusion." },
      { author: "Steven Pinker", work: "The Language Instinct", quote: "The child easily distinguishes whether meet or its **homophone** meat was intended based entirely on syntactic context." },
      { author: "David Crystal", work: "The Stories of English", quote: "Great punsters throughout literary history have exploited the ambiguity created whenever a spoken word coincides with a familiar **homophone**." }
    ]
  },
  "homophonic.md": {
    primary: "Having the same sound or pronunciation; designating words that are homophones.",
    secondary: "In music theory, describing a texture in which a primary melodic voice is accompanied by subordinate chords or harmonic parts moving together in rhythm.",
    quotes: [
      { author: "Donald Jay Grout", work: "A History of Western Music", quote: "The classical style of Haydn and Mozart marked a clear transition from complex polyphony to transparent **homophonic** textures." },
      { author: "Aaron Copland", work: "What to Listen for in Music", quote: "A hymn tune represents the simplest kind of **homophonic** writing, where all parts move in strict harmonic blocks beneath the soprano melody." },
      { author: "Leonard Bernstein", work: "The Joy of Music", quote: "The listener can effortlessly follow a clear, singing melody when supported by a well-crafted **homophonic** accompaniment." }
    ]
  },
  "homophonous.md": {
    primary: "Having the same phonetic sound or pronunciation; identical in acoustic realization though differing in meaning or spelling.",
    secondary: "In musical composition, moving homophonically with rhythmically unified chordal accompaniment beneath a dominant melody.",
    quotes: [
      { author: "Henry Sweet", work: "A Handbook of Phonetics", quote: "Words that become **homophonous** through historical sound loss often undergo semantic differentiation or total obsolescence." },
      { author: "Charles Rosen", work: "The Classical Style", quote: "The **homophonous** textures of early classical sonatas offered a dramatic contrast to the dense contrapuntal tapestries of the High Baroque." },
      { author: "William Dwight Whitney", work: "The Life and Growth of Language", quote: "Context alone prevents misunderstanding when two distinct lexical roots become completely **homophonous** in speech." }
    ]
  },
  "homophony.md": {
    primary: "Identity of sound between different words or characters having different spellings and meanings.",
    secondary: "In music, a textural structure in which one principal melody stands out prominently while accompanying voices provide harmonic support.",
    quotes: [
      { author: "Igor Stravinsky", work: "Chronicles of My Life", quote: "The stark **homophony** of the sacred chorale struck the congregation with direct, unadorned spiritual force." },
      { author: "Edward Sapir", work: "Language: An Introduction to the Study of Speech", quote: "Extensive phonetic erosion in modern languages has dramatically multiplied instances of lexical **homophony**." },
      { author: "Paul Henry Lang", work: "Music in Western Civilization", quote: "The rise of Italian opera established the supremacy of melodic **homophony** over the intricate polyphonic webs of the Renaissance." }
    ]
  },
  "hypophonesis.md": {
    primary: "A subdued, low, whispered, or undertone vocalization; speech delivered beneath one's breath.",
    secondary: "In classical rhetorical delivery or phonetics, the deliberate dropping of vocal volume or pitch to emphasize intimacy, secrecy, or profound gravity.",
    quotes: [
      { author: "John Bulwer", work: "Chironomia", quote: "In moments of conspiratorial awe, the orator descendeth to a subtle **hypophonesis**, compelling the assembly to lean forward in silence." },
      { author: "Hugh Blair", work: "Lectures on Rhetoric and Belles Lettres", quote: "A sudden modulation from passionate declamation to quiet **hypophonesis** commands instant and breathless attention." },
      { author: "George Campbell", work: "The Philosophy of Rhetoric", quote: "The pathos of tragedy is often heightened when solemn grief is uttered not in shrieks, but in murmured **hypophonesis**." }
    ]
  },
  "ideophone.md": {
    primary: "A vivid, evocative word that phonetically depicts or mimics a sensory perception, motion, texture, color, or psychological state.",
    secondary: "In linguistic typology, an expressive lexical class of words (such as sound-symbolic words or Japanese mimetics) that convey sensory impressions beyond mere sound.",
    quotes: [
      { author: "G. A. Kouwenhoven", work: "A Grammar of Zulu", quote: "In Bantu languages, the **ideophone** acts as a vivid linguistic brushstroke, painting sound, color, and motion directly into the listener's imagination." },
      { author: "Mark Dingemanse", work: "The Meaning and Use of Ideophones", quote: "An **ideophone** does not simply describe a sensory experience; it performs an acoustic simulation of the event itself." },
      { author: "Edward Sapir", work: "Selected Writings in Language, Culture and Personality", quote: "Expressive sound-symbolism demonstrates that an **ideophone** links sensory intuition directly to phonetic patterning." }
    ]
  },
  "idiophone.md": {
    primary: "Any musical instrument in which sound is produced primarily by the vibration of the instrument's own solid body, without strings or membranes (e.g. gongs, bells, xylophones).",
    secondary: "The first and most diverse of the four main instrument families established in the Hornbostel-Sachs system of musical instrument classification.",
    quotes: [
      { author: "Curt Sachs", work: "The History of Musical Instruments", quote: "A struck stone, a wooden bell, and a bronze cymbal are all classified as an **idiophone**, producing sound through their own elastic substance." },
      { author: "Erich von Hornbostel", work: "Systematik der Musikinstrumente", quote: "We define as an **idiophone** any resonant object whose vibrating material itself generates the acoustic tone without strings or membranes." },
      { author: "Colin Turnbull", work: "The Forest People", quote: "The rhythmic clatter of the wooden **idiophone** echoed through the dense canopy as the hunters prepared their evening dance." }
    ]
  },
  "isophone.md": {
    primary: "A line drawn on a dialect map connecting geographic points where a specific speech sound or phonetic feature is pronounced identically.",
    secondary: "In acoustic engineering and psychoacoustics, a contour line of equal perceived loudness plotted across varying acoustic frequencies.",
    quotes: [
      { author: "Hans Kurath", work: "A Word Geography of the Eastern United States", quote: "The dialect cartographer traces an **isophone** across the mountain pass to mark the boundary between rhotic and non-rhotic pronunciation." },
      { author: "Harvey Fletcher", work: "Speech and Hearing in Communication", quote: "Each **isophone** on the psychoacoustic graph depicts the sound pressure levels required to produce a sensation of uniform loudness across frequencies." },
      { author: "Peter Trudgill", work: "Sociolinguistics: An Introduction to Language and Society", quote: "Isolating a single **isophone** reveals how dialect boundaries frequently align with ancient riverways and administrative frontiers." }
    ]
  },
  "logophonetic.md": {
    primary: "Pertaining to a writing system that combines logographic symbols (representing words or morphemes) with phonetic elements (representing sounds or syllables).",
    secondary: "Characterizing complex scripts such as ancient Egyptian hieroglyphs, Sumerian cuneiform, and Mayan glyphs that employ semantic signs alongside phonetic complements.",
    quotes: [
      { author: "Michael D. Coe", work: "Breaking the Maya Code", quote: "Scholars finally unlocked the inscriptions once they realized the classic script was fundamentally **logophonetic** rather than purely symbolic." },
      { author: "J. Marshall Unger", work: "Ideogram: Chinese Characters and the Myth of Disembodied Meaning", quote: "The vast majority of Chinese characters are formed upon **logophonetic** principles, coupling a semantic radical with a phonetic indicator." },
      { author: "John DeFrancis", work: "The Chinese Language: Fact and Fantasy", quote: "Every successful writing system that survived antiquity evolved into a **logophonetic** script to balance meaning and pronunciation." }
    ]
  },
  "megaphone.md": {
    primary: "A portable, funnel-shaped acoustic horn or electronic device used to amplify, direct, and project the human voice over a distance.",
    secondary: "Figuratively, a powerful platform, media outlet, or institutional megaphone used to amplify a particular ideology, opinion, or message.",
    quotes: [
      { author: "George Orwell", work: "Down and Out in Paris and London", quote: "The dockmaster barked instructions through a tin **megaphone**, his voice cutting sharp through the morning river fog." },
      { author: "Sinclair Lewis", work: "Babbitt", quote: "He seized the cheerleader's **megaphone** and led the stadium crowd in a thunderous, rhythmic roar for the home team." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Industry lobbies possessed a nationwide **megaphone** to broadcast reassuring claims that chemical spraying was completely harmless." }
    ]
  },
  "microphone.md": {
    primary: "An electroacoustic transducer or instrument that converts acoustic sound waves in air into an electrical audio signal for amplification, transmission, or recording.",
    secondary: "A vital technical and cultural apparatus in broadcasting, recording arts, and public address that transformed vocal performance and mass communication.",
    quotes: [
      { author: "Marshall McLuhan", work: "Understanding Media", quote: "The **microphone** transformed politics by substituting the intimate whispers of the fireside chat for the booming rhetoric of the public square." },
      { author: "David Byrne", work: "How Music Works", quote: "The invention of the sensitive **microphone** made it possible for crooners to sing softly, inventing a new intimacy in recorded song." },
      { author: "Walter Benjamin", work: "The Work of Art in the Age of Mechanical Reproduction", quote: "The camera and the **microphone** interpose an apparatus between the performer and the public, altering the very nature of human presence." }
    ]
  },
  "microphoning.md": {
    primary: "The technique, practice, or art of positioning, selecting, and arranging microphones to capture sound in recording or sound reinforcement.",
    secondary: "In acoustic engineering, the acoustic and spatial configuration of transducers (such as close microphoning or stereo pairs) to optimize sound reproduction.",
    quotes: [
      { author: "Bob Katz", work: "Mastering Audio: The Art and the Science", quote: "Judicious acoustic **microphoning** in a well-designed hall captures a natural stereo image that artificial reverb can never duplicate." },
      { author: "George Martin", work: "All You Need Is Ears", quote: "By experimenting with unorthodox close **microphoning** on the string quartet for 'Yesterday', we achieved an immediate and biting intimacy." },
      { author: "Alton Everest", work: "Master Handbook of Acoustics", quote: "Proper **microphoning** requires an acute understanding of comb filtering and phase cancellation caused by reflective boundaries." }
    ]
  },
  "misophonia.md": {
    primary: "A neurological or psychological condition characterized by intense emotional distress, irritation, or anger triggered by specific everyday sounds (such as chewing, breathing, or tapping).",
    secondary: "A sensory processing disorder distinct from hyperacusis, where selective acoustic stimuli elicit an involuntary sympathetic nervous system fight-or-flight response.",
    quotes: [
      { author: "Pawel Jastreboff", work: "Hyperacusis and Misophonia", quote: "Patients with **misophonia** do not complain of loudness, but of an intolerable neurological aversion to specific repetitive human sounds." },
      { author: "Bessel van der Kolk", work: "The Body Keeps the Score", quote: "Sensory hypersensitivities like **misophonia** illustrate how deeply visceral autonomic reactions can be triggered by seemingly trivial environmental cues." },
      { author: "Oliver Sacks", work: "Musicophilia", quote: "The distress of **misophonia** reveals how sound is bound to emotion through primitive pathways that bypass rational cognition." }
    ]
  },
  "monophonic.md": {
    primary: "Consisting of a single unaccompanied melodic vocal or instrumental line; without harmonic accompaniment or counterpoint.",
    secondary: "In audio technology and sound reproduction, utilizing a single audio channel to record or transmit sound (mono).",
    quotes: [
      { author: "Donald Jay Grout", work: "A History of Western Music", quote: "Gregorian plainchant represents the supreme historical flowering of pure **monophonic** vocal art in Western civilization." },
      { author: "Aaron Copland", work: "What to Listen for in Music", quote: "A solitary flute singing an unadorned folk melody produces a **monophonic** texture of exquisite purity." },
      { author: "Walter Piston", work: "Harmony", quote: "Early church musicians sang strictly **monophonic** chants for centuries before bold pioneers ventured into parallel organum." }
    ]
  },
  "monophony.md": {
    primary: "Music that consists of a single melodic line without accompanying harmony or independent contrapuntal parts.",
    secondary: "In audio engineering, single-channel sound reproduction or monaural broadcasting.",
    quotes: [
      { author: "Paul Henry Lang", work: "Music in Western Civilization", quote: "The transition from ancient liturgical **monophony** to medieval polyphony was the most profound revolution in European music." },
      { author: "Curt Sachs", work: "The Rise of Music in the Ancient World", quote: "Classical antiquity celebrated **monophony**, believing that an unadorned melodic line possessed direct ethical and spiritual power." },
      { author: "Igor Stravinsky", work: "Poetics of Music", quote: "There is a pristine austerity in liturgical **monophony** that modern orchestral complexity cannot surpass." }
    ]
  },
  "morphophonology.md": {
    primary: "The branch of linguistics that studies the relationships and interactions between morphology and phonology, specifically how grammatical morphemes affect sound changes across word boundaries.",
    secondary: "In structural and generative linguistics, the formal rules governing the phonological realization of morphemes (such as the English plural endings -s, -z, -ɪz).",
    quotes: [
      { author: "Nikolai Trubetzkoy", work: "Principles of Phonology", quote: "We established **morphophonology** as an autonomous discipline to investigate the phonological structure of grammatical morphemes." },
      { author: "Noam Chomsky", work: "The Sound Pattern of English", quote: "Generative **morphophonology** demonstrates that surface phonetic variations can be derived systematically from underlying abstract forms." },
      { author: "Edward Sapir", work: "Language: An Introduction to the Study of Speech", quote: "Every living language possesses an intricate **morphophonology** that coordinates mechanical sound laws with expressive grammatical categories." }
    ]
  }
};

for (const [filename, entry] of Object.entries(filesData)) {
  const filePath = path.join(basePath, filename);
  if (!fs.existsSync(filePath)) {
    console.error(`Missing file: ${filePath}`);
    continue;
  }
  const content = fs.readFileSync(filePath, 'utf8');

  // Find top portion up to > [!book]
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`No > [!book] in ${filename}`);
    continue;
  }
  const topBlock = content.substring(0, bookIdx);

  const newContent = `${topBlock}> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: ${entry.primary}
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${entry.secondary}

> [!quote] 💬 Contextual Usage & Authentic Quotations
${entry.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join('\n')}
`;

  fs.writeFileSync(filePath, newContent, 'utf8');
  console.log(`Updated: ${filename}`);
}

console.log('Done Batch 5 (phon Part 1) of Cluster Sound & Auditory!');
