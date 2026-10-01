import fs from 'fs';
import path from 'path';

const basePath = 'App database/Greek roots/Cluster Sound & Auditory/Dashboard — phon';

const filesData = {
  "phon.md": {
    primary: "A unit of subjective perceived loudness level of sounds, equal to the sound pressure level in decibels of a 1,000-hertz pure tone judged equally loud.",
    secondary: "In acoustic engineering, a psychoacoustic measure based on human equal-loudness contours (Fletcher-Munson curves).",
    quotes: [
      { author: "Harvey Fletcher", work: "Speech and Hearing in Communication", quote: "The **phon** scale standardizes auditory loudness judgments by referencing them to a one-thousand-cycle tone." },
      { author: "Alton Everest", work: "Master Handbook of Acoustics", quote: "A noise level of eighty **phon** corresponds directly to the perceived intensity of an eighty-decibel tone at one kilohertz." },
      { author: "Leo Beranek", work: "Acoustics", quote: "Contour lines measured in **phon** units reveal how the human ear diminishes in sensitivity at extreme low and high frequencies." }
    ]
  },
  "phonaesthesia.md": {
    primary: "The systematic association between certain phonetic sounds or sound clusters and specific meanings, emotions, or physical sensory qualities.",
    secondary: "In psycholinguistics, the phenomenon whereby non-morphemic phonetic clusters (like gl- for light) evoke coherent semantic fields.",
    quotes: [
      { author: "J. R. Firth", work: "Papers in Linguistics", quote: "Through **phonaesthesia**, initial consonant groups like *sn-* or *sl-* acquire an expressive, visceral meaning of their own." },
      { author: "Roman Jakobson", work: "Six Lectures on Sound and Meaning", quote: "The study of **phonaesthesia** demonstrates that the relationship between phonetic form and conceptual meaning is not entirely arbitrary." },
      { author: "Otto Jespersen", work: "Language: Its Nature, Development and Origin", quote: "Human speech displays an innate **phonaesthesia**, linking sharp, bright vowels with diminutive or luminous objects." }
    ]
  },
  "phonaesthetics.md": {
    primary: "The study of the aesthetic qualities of vocal speech sounds and their perceived beauty, pleasantness, or expressiveness.",
    secondary: "In stylistics and literary criticism, the acoustic analysis of poetic diction and the musical euphony produced by specific combinations of vowels and consonants.",
    quotes: [
      { author: "J. R. R. Tolkien", work: "The Monsters and the Critics and Other Essays", quote: "In Celtic and Germanic verse, the subtle art of **phonaesthetics** guides the poet toward arrangements of words that delight the ear independently of sense." },
      { author: "David Crystal", work: "The Cambridge Encyclopedia of the English Language", quote: "In popular **phonaesthetics**, phrases like 'cellar door' are celebrated as sounding uniquely beautiful to English speakers." },
      { author: "I. A. Richards", work: "Principles of Literary Criticism", quote: "Rigorous **phonaesthetics** must distinguish between the physical sound of a phrase and the emotional imagery it conjures." }
    ]
  },
  "phonate.md": {
    primary: "To produce vocal sounds or speech through the vibration of the vocal folds and the expulsion of air from the lungs.",
    secondary: "In physiology and voice science, to engage the intrinsic laryngeal muscles to adduct the vocal cords and initiate sustained oscillation.",
    quotes: [
      { author: "Robert Thayer Sataloff", work: "Professional Voice", quote: "The patient was instructed to gently **phonate** a sustained vowel while the laryngoscopic camera recorded vocal fold closure." },
      { author: "Johan Sundberg", work: "The Science of the Singing Voice", quote: "To **phonate** efficiently across registers, a singer must balance subglottal pressure with muscular tension." },
      { author: "Oliver Sacks", work: "Musicophilia", quote: "Even when unable to articulate words, the afflicted individual could still **phonate** clear, musical pitches." }
    ]
  },
  "phonation.md": {
    primary: "The physiological process of producing vocal sounds through the vibration of the vocal cords in the larynx.",
    secondary: "In speech pathology and phonetics, the aeromechanical interaction between pulmonary airflow and laryngeal adduction that generates the voice source.",
    quotes: [
      { author: "Peter Ladefoged", work: "Elements of Acoustic Phonetics", quote: "During voiced speech, rapid cycles of **phonation** modulate the airstream into periodic acoustic pulses." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Any mechanical interference with the vocal cords impairs normal **phonation**, resulting in breathiness or stridor." },
      { author: "Noam Chomsky", work: "The Sound Pattern of English", quote: "The vocal tracts modify the periodic sound wave created by laryngeal **phonation** into distinct formant frequencies." }
    ]
  },
  "phone-in.md": {
    primary: "A radio or television broadcast program in which listeners or viewers participate by telephoning the studio to express opinions or ask questions.",
    secondary: "Pertaining to, designed for, or conducted via incoming telephone calls from members of the public.",
    quotes: [
      { author: "Marshall McLuhan", work: "The Medium is the Massage", quote: "The interactive **phone-in** program transformed passive mass audiences into direct co-producers of broadcast commentary." },
      { author: "Terry Pratchett", work: "Reaper Man", quote: "A chaotic local **phone-in** show buzzed with frantic callers demanding explanations for the strange occurrences." },
      { author: "David Foster Wallace", work: "Consider the Lobster", quote: "Talk radio stations depend entirely on the heated emotional energy of the late-night **phone-in** format." }
    ]
  },
  "phone.md": {
    primary: "A telephone; an electronic telecommunications device used for transmitting sound and voice across distances; also, in phonetics, any single unanalyzed speech sound.",
    secondary: "In mobile technology, a smartphone integrating cellular communications, mobile computing, and multimedia capabilities.",
    quotes: [
      { author: "Alexander Graham Bell", work: "Memoir upon the Formation of a Deaf Variety", quote: "I spoke into the crude transmitter, and through the wire the **phone** conveyed my words to the receiver." },
      { author: "Ray Bradbury", work: "Fahrenheit 451", quote: "He listened to the humming silence of the empty house, untouched by the ring of any friendly **phone**." },
      { author: "Daniel Jones", work: "An Outline of English Phonetics", quote: "A phonetician defines each **phone** as an individual speech sound regarded without reference to its functional status in a language." }
    ]
  },
  "phonebook.md": {
    primary: "A published telephone directory, listing telephone subscribers in alphabetical order alongside their addresses and telephone numbers.",
    secondary: "A contact list or database stored electronically on a mobile phone or personal computer containing telephone numbers and contact details.",
    quotes: [
      { author: "Arthur Miller", work: "Death of a Salesman", quote: "He leafed through the dog-eared pages of his city **phonebook**, hunting for past buyers who might still remember him." },
      { author: "Raymond Chandler", work: "The Big Sleep", quote: "I picked up the heavy Los Angeles **phonebook** and ran my finger down the column of private investigators." },
      { author: "Don DeLillo", work: "Underworld", quote: "Old numbers copied from a faded **phonebook** linked him to forgotten corners of the Bronx." }
    ]
  },
  "phoneme.md": {
    primary: "The smallest distinctive, contrastive unit of sound in a specified language that distinguishes one word from another.",
    secondary: "In theoretical and structural phonology, an abstract category of speech sounds that native speakers perceive as functionally identical.",
    quotes: [
      { author: "Ferdinand de Saussure", work: "Course in General Linguistics", quote: "The linguistic value of a **phoneme** resides entirely in its systematic opposition to other sounds within the language." },
      { author: "Edward Sapir", work: "Language: An Introduction to the Study of Speech", quote: "Speakers are acutely conscious of a difference in **phoneme**, but oblivious to non-distinctive acoustic variations." },
      { author: "Leonard Bloomfield", work: "Language", quote: "Substituting one **phoneme** for another in a minimal pair instantly transforms the meaning of the utterance." }
    ]
  },
  "phonemic.md": {
    primary: "Pertaining to, consisting of, or relating to phonemes or the functional sound system of a language.",
    secondary: "Contrastive in sound so as to distinguish lexical meaning; distinguished from purely phonetic or non-distinctive acoustic detail.",
    quotes: [
      { author: "Roman Jakobson", work: "Fundamentals of Language", quote: "A **phonemic** analysis isolates those binary acoustic features that serve a contrastive communicative function." },
      { author: "Kenneth L. Pike", work: "Phonemics: A Technique for Reducing Languages to Writing", quote: "The linguist must construct a valid **phonemic** alphabet before attempting to create written literature for an unwritten tongue." },
      { author: "Noam Chomsky", work: "Syntactic Structures", quote: "The abstract syntactic representation maps onto a string of **phonemic** units governed by rigorous transformational rules." }
    ]
  },
  "phonemics.md": {
    primary: "The branch of linguistics that studies phonemes and the functional sound patterns and contrasts of a language or languages.",
    secondary: "The methodology and theoretical framework used to identify, analyze, and transcribe the inventory of contrastive phonemes in speech.",
    quotes: [
      { author: "Leonard Bloomfield", work: "Language", quote: "Descriptive **phonemics** laid the empirical foundation for modern structural linguistics in the twentieth century." },
      { author: "Bernard Bloch", work: "Outline of Linguistic Analysis", quote: "In systematic **phonemics**, complementary distribution and phonetic similarity determine whether sounds belong to the same phoneme." },
      { author: "Claude Lévi-Strauss", work: "Structural Anthropology", quote: "The breakthroughs of structural **phonemics** provided anthropology with a revolutionary model for analyzing kinship systems." }
    ]
  },
  "phoner.md": {
    primary: "An interview, conversation, or conference conducted over the telephone, especially a broadcast or journalistic telephone interview.",
    secondary: "A person who makes a telephone call, particularly a caller contacting a broadcast radio program or call center.",
    quotes: [
      { author: "Hunter S. Thompson", work: "Fear and Loathing on the Campaign Trail '72", quote: "We were up until dawn conducting a marathon **phoner** with state campaign directors in Wisconsin." },
      { author: "Bob Woodward", work: "The Secret Man", quote: "The editor arranged a brief **phoner** to confirm the breaking diplomatic dispatch before going to press." },
      { author: "David Foster Wallace", work: "Infinite Jest", quote: "The talk show host punched the flashing button to take the next angry **phoner** on the live line." }
    ]
  },
  "phonesthemic.md": {
    primary: "Pertaining to, having the nature of, or involving a phonestheme (a recurring sound sequence associated with a specific semantic field).",
    secondary: "Relating to sub-morphemic sound symbolism and intuitive semantic associations in language.",
    quotes: [
      { author: "Dwight Bolinger", work: "Forms of English: Accent, Morpheme, Order", quote: "The English vocabulary exhibits powerful **phonesthemic** clusters where sound and meaning intertwine outside standard etymology." },
      { author: "J. R. Firth", work: "Speech", quote: "Words beginning with *sn-* carry a distinct **phonesthemic** flavor associated with the nose, mucus, or furtive movement." },
      { author: "Steven Pinker", work: "Words and Rules", quote: "Poets intuitively exploit **phonesthemic** resonances to charge ordinary words with evocative sensory weight." }
    ]
  },
  "phonetic.md": {
    primary: "Pertaining to, representing, or concerning human speech sounds, their physical production, acoustic transmission, and auditory perception.",
    secondary: "Corresponding directly to vocal pronunciation; designating a spelling system where each symbol consistently represents a single sound.",
    quotes: [
      { author: "Henry Sweet", work: "The Practical Study of Languages", quote: "A reformed **phonetic** script enables students to master foreign pronunciation without being misled by chaotic orthography." },
      { author: "George Bernard Shaw", work: "Pygmalion", quote: "Professor Higgins recorded every subtle vowel nuance in his notebook using an exact **phonetic** notation." },
      { author: "Peter Ladefoged", work: "Vowels and Consonants", quote: "Every language draws its vocabulary from a universal inventory of possible human **phonetic** articulations." }
    ]
  },
  "phonetically.md": {
    primary: "In a manner concerning speech sounds, pronunciation, or the phonetic representation of language.",
    secondary: "According to the actual acoustic pronunciation rather than conventional orthography.",
    quotes: [
      { author: "Max Müller", work: "Lectures on the Science of Language", quote: "Words that appear wildly divergent in spelling often correspond **phonetically** when traced back through historical sound laws." },
      { author: "H. L. Mencken", work: "The American Language", quote: "The dialect was recorded **phonetically** by early humorists attempting to capture frontier speech on the printed page." },
      { author: "David Crystal", work: "How Language Works", quote: "Transcribing speech **phonetically** requires setting aside all preconceived notions of conventional spelling." }
    ]
  },
  "phonetician.md": {
    primary: "A specialist or linguist who studies phonetics, the physical properties, production, and acoustic transmission of human speech sounds.",
    secondary: "An expert in speech analysis, vocal articulation, dialect identification, and phonetic transcription.",
    quotes: [
      { author: "George Bernard Shaw", work: "Pygmalion", quote: "Higgins was an impassioned **phonetician** who could place any Londoner within two streets by the turn of a single vowel." },
      { author: "Daniel Jones", work: "The Pronunciation of English", quote: "A trained **phonetician** must develop both acute auditory discrimination and precise control over the vocal organs." },
      { author: "Henry Sweet", work: "A Primer of Phonetics", quote: "The mission of the practical **phonetician** is to bridge the chasm between spoken dialect and written orthography." }
    ]
  },
  "phonetics.md": {
    primary: "The scientific study of human speech sounds, encompassing articulatory, acoustic, and auditory dimensions of vocal sound production.",
    secondary: "The branch of linguistics that analyzes how speech sounds are physically produced by the vocal tract, transmitted as sound waves, and perceived by the ear.",
    quotes: [
      { author: "Edward Sapir", work: "Language: An Introduction to the Study of Speech", quote: "While **phonetics** catalogs the raw physical sounds of speech, phonology studies their functional patterns." },
      { author: "Roman Jakobson", work: "Preliminaries to Speech Analysis", quote: "The integration of acoustic **phonetics** with information theory revolutionized our understanding of speech perception." },
      { author: "Peter Ladefoged", work: "A Course in Phonetics", quote: "Mastery of articulatory **phonetics** requires feeling the precise contacts between tongue, palate, and vocal cords." }
    ]
  },
  "phoney.md": {
    primary: "Fraudulent, counterfeit, fake, or insincere; not genuine or authentic.",
    secondary: "A person who pretends to have virtues, qualities, feelings, or an identity that they do not possess; a fraud or imposter.",
    quotes: [
      { author: "J. D. Salinger", work: "The Catcher in the Rye", quote: "It was full of **phoney** people all pretending they were grand intellectuals when they were just showing off." },
      { author: "Raymond Chandler", work: "Farewell, My Lovely", quote: "The jeweler inspected the gleaming diamond with a loupe and muttered that the whole setting was completely **phoney**." },
      { author: "George Orwell", work: "Homage to Catalonia", quote: "The political slogans plastered along the boulevard sounded hollow and **phoney** to the weary soldiers." }
    ]
  },
  "phonic.md": {
    primary: "Pertaining to sound, especially vocal speech sounds; acoustic or phonological.",
    secondary: "Relating to the sounds represented by written letters and alphabetic characters, as in phonic reading instruction.",
    quotes: [
      { author: "Edgar Allan Poe", work: "The Poetic Principle", quote: "The **phonic** resonance of verse exerts a direct spiritual power over the imagination of the listener." },
      { author: "David Crystal", work: "The English Language", quote: "Early childhood literacy programs emphasize the **phonic** relationship between letters on the page and spoken sounds." },
      { author: "Aldous Huxley", work: "Brave New World", quote: "The rhythmic repetition of soothing **phonic** syllables lulled the sleeping children into conditioned habits." }
    ]
  },
  "phonics.md": {
    primary: "A method of teaching reading and spelling based on the relationship between written letters and the sounds they represent.",
    secondary: "The sound-spelling correspondence system used in early childhood education to develop decoding skills and reading fluency.",
    quotes: [
      { author: "Jeanne Chall", work: "Learning to Read: The Great Debate", quote: "Decades of educational research confirm that systematic instruction in **phonics** provides children with essential decoding tools." },
      { author: "Steven Pinker", work: "The Language Instinct", quote: "A child learning to read must map arbitrary visual marks onto spoken language through the explicit rules of **phonics**." },
      { author: "David Crystal", work: "The Cambridge Encyclopedia of Language", quote: "Modern educators combine synthetic **phonics** with rich literature to cultivate both decoding accuracy and reading comprehension." }
    ]
  },
  "phonogram.md": {
    primary: "A written character or symbol that represents a speech sound, syllable, or phoneme rather than an object or idea.",
    secondary: "An early term for a sound recording or recorded disc/cylinder made on a phonograph.",
    quotes: [
      { author: "Isaac Taylor", work: "The History of the Alphabet", quote: "The critical transition in human writing occurred when the pictograph evolved into a purely phonetic **phonogram**." },
      { author: "Thomas Edison", work: "The Phonograph and Its Future", quote: "Each embossed groove upon the cylinder constitutes a permanent **phonogram** capable of reproducing the human voice indefinitely." },
      { author: "Ignace Gelb", work: "A Study of Writing", quote: "In hieroglyphic scripts, a **phonogram** was frequently appended to a logogram to confirm its pronunciation." }
    ]
  },
  "phonogramic.md": {
    primary: "Pertaining to or consisting of phonograms; using written symbols to represent speech sounds.",
    secondary: "Characterized by a phonetic writing system based on phonograms rather than ideographic or pictographic characters.",
    quotes: [
      { author: "David Diringer", work: "The Alphabet", quote: "The emergence of **phonogramic** scripts allowed ancient civilizations to record complex abstract thought with minimal symbols." },
      { author: "John Chadwick", work: "The Decipherment of Linear B", quote: "The syllabary consists of sixty distinct **phonogramic** signs representing vowel and consonant-vowel combinations." },
      { author: "Michael D. Coe", work: "Breaking the Maya Code", quote: "Scholars recognized that Maya glyphs included both semantic determinatives and strictly **phonogramic** syllables." }
    ]
  },
  "phonograph.md": {
    primary: "An early instrument for sound reproduction that played audio recordings engraved in grooves on rotating wax cylinders or flat discs.",
    secondary: "A historical technological invention (pioneered by Thomas Edison in 1877) that founded the modern recording industry.",
    quotes: [
      { author: "Thomas Edison", work: "The Phonograph and Its Future", quote: "I foresee that the **phonograph** will preserve the voices of great statesmen and singers for future generations." },
      { author: "Mark Twain", work: "A Connecticut Yankee in King Arthur's Court", quote: "He brought forth the miraculous **phonograph**, which startled the medieval assembly by speaking with human words." },
      { author: "H. G. Wells", work: "The Time Machine", quote: "In the ruinous museum of the far future, the remains of an ancient **phonograph** lay buried beneath accumulated dust." }
    ]
  },
  "phonologic.md": {
    primary: "Pertaining to phonology, the functional sound patterns, systematic relationships, and rule systems of language.",
    secondary: "Characterized by or relating to the mental organization and systematic contrasts of speech sounds in a linguistic system.",
    quotes: [
      { author: "Edward Sapir", work: "Language", quote: "Every natural language exhibits a strict **phonologic** economy that restricts which sound combinations are permissible." },
      { author: "Roman Jakobson", work: "Fundamentals of Language", quote: "The **phonologic** structure of language operates through binary oppositions between distinctive features." },
      { author: "Noam Chomsky", work: "Current Issues in Linguistic Theory", quote: "The generative model integrates syntactic output directly into the **phonologic** component of grammar." }
    ]
  },
  "phonological.md": {
    primary: "Relating to the systematic organization, patterning, and study of speech sounds within a language (phonology).",
    secondary: "Pertaining to the cognitive representations, rules, and constraints that govern sound changes and contrasts in human speech.",
    quotes: [
      { author: "Noam Chomsky", work: "The Sound Pattern of English", quote: "A comprehensive grammar must account for the underlying **phonological** representations that generate surface speech." },
      { author: "Steven Pinker", work: "The Language Instinct", quote: "Children acquire the **phonological** rules of their native tongue effortlessly before reaching school age." },
      { author: "Ferdinand de Saussure", work: "Course in General Linguistics", quote: "The **phonological** system of a language functions as a self-contained web of interdependent acoustic relations." }
    ]
  },
  "phonologist.md": {
    primary: "A linguist who specializes in the study of phonology, investigating the organization, patterning, and systems of speech sounds in languages.",
    secondary: "A researcher focused on abstract phonological theory, rule systems, distinctive feature analysis, and historical sound shifts.",
    quotes: [
      { author: "Nikolai Trubetzkoy", work: "Principles of Phonology", quote: "The task of the structural **phonologist** is to uncover the underlying functional oppositions that structure vocal communication." },
      { author: "Roman Jakobson", work: "Selected Writings", quote: "As a **phonologist**, my primary goal has been to discover the universal invariants that govern all human sound systems." },
      { author: "Leonard Bloomfield", work: "Language", quote: "The descriptive **phonologist** must avoid projecting external orthographic prejudices onto unwritten languages." }
    ]
  },
  "phonology.md": {
    primary: "The branch of linguistics that deals with the systems and patterns of sounds occurring in human languages.",
    secondary: "The sound system, rule inventory, and organizational structure of speech sounds characteristic of a specific language or dialect.",
    quotes: [
      { author: "Ferdinand de Saussure", work: "Course in General Linguistics", quote: "General **phonology** examines the abstract mechanics of sound systems rather than the raw physics of utterance." },
      { author: "Edward Sapir", work: "Sound Patterns in Language", quote: "Two languages may employ identical physiological sounds while possessing an entirely different underlying **phonology**." },
      { author: "Noam Chomsky", work: "The Sound Pattern of English", quote: "Generative **phonology** formalized the rule systems that bridge abstract syntax and concrete acoustic output." }
    ]
  },
  "phonophobia.md": {
    primary: "An abnormal, extreme, or irrational sensitivity to or fear of sound, especially loud, sharp, or sudden noises.",
    secondary: "In neurology, a common clinical symptom of migraine headaches and brain injury characterized by severe sensory intolerance to environmental sounds.",
    quotes: [
      { author: "Oliver Sacks", work: "Migraine", quote: "The patient retreated into a darkened, silent bedroom, debilitated by acute photophobia and unbearable **phonophobia**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "During severe cephalalgia, profound **phonophobia** renders the slightest footstep or rustling paper agonizing." },
      { author: "Harold Wolff", work: "Headache and Other Head Pain", quote: "Sensory hypersensitivity during vascular headaches manifests prominently as transient **phonophobia**." }
    ]
  },
  "phonosemantics.md": {
    primary: "The branch of linguistics and semiotics that investigates the direct, non-arbitrary relationships between speech sounds and their meanings.",
    secondary: "The theoretical study of how acoustic properties of phonemes naturally evoke psychological, sensory, and semantic associations across cultures.",
    quotes: [
      { author: "Roman Jakobson", work: "The Sound Shape of Language", quote: "Modern **phonosemantics** overturns the dogma of arbitrary signs by documenting universal cross-linguistic sound symbolism." },
      { author: "Otto Jespersen", work: "Language: Its Nature, Development and Origin", quote: "The principles of **phonosemantics** explain why front vowels universally correlate with smallness, delicacy, and light." },
      { author: "Margaret Magnus", work: "Gods of the Word: Archetypes in the Consonants", quote: "Through **phonosemantics**, we uncover how each consonant carries an inherent cognitive archetype within the lexicon." }
    ]
  },
  "phony.md": {
    primary: "Not genuine, fraudulent, fake, or counterfeit; deceptive in appearance or character.",
    secondary: "An insincere or fraudulent person; someone who assumes false pretenses or poses as something they are not.",
    quotes: [
      { author: "J. D. Salinger", work: "The Catcher in the Rye", quote: "I was surrounded by all kinds of **phony** guys who talked about their expensive suits and cars." },
      { author: "Raymond Chandler", work: "The Long Goodbye", quote: "He flashed an easy, practiced smile that looked as **phony** as a three-dollar bill." },
      { author: "George Orwell", work: "1984", quote: "The official news bulletins reported heroic production victories that everyone knew were entirely **phony**." }
    ]
  },
  "polyphone.md": {
    primary: "A written letter, character, or symbol that represents two or more distinct sounds or phonetic values.",
    secondary: "In linguistics and epigraphy, a polyphonic character; or an early type of mechanical music box playing multiple tunes on interchangeable discs.",
    quotes: [
      { author: "Henry Sweet", work: "The Practical Study of Languages", quote: "In English orthography, almost every vowel sign is an ambiguous **polyphone** with multiple disparate readings." },
      { author: "Isaac Taylor", work: "The History of the Alphabet", quote: "Sumerian cuneiform signs frequently functioned as a **polyphone**, acquiring new sound values as the script adapted across cultures." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Dancing Men", quote: "The code was complicated by the fact that certain pictorial figures served as a **polyphone** depending on context." }
    ]
  },
  "polyphonic.md": {
    primary: "Consisting of or having multiple voice parts or musical melodies sounded together, each having an independent melodic character and rhythm.",
    secondary: "Capable of producing multiple notes or audio channels simultaneously (e.g. a polyphonic synthesizer).",
    quotes: [
      { author: "Donald Jay Grout", work: "A History of Western Music", quote: "The Renaissance motet reached its artistic zenith in the intricate **polyphonic** masterpieces of Palestrina and Lassus." },
      { author: "Aldous Huxley", work: "Point Counter Point", quote: "Human experience unfolded before him like a vast **polyphonic** composition, multiple tragic and comic themes interweaving simultaneously." },
      { author: "Thomas Mann", work: "Doctor Faustus", quote: "Leverkühn's ambitious score integrated strict twelve-tone technique into a dazzling, multilayered **polyphonic** tapestry." }
    ]
  },
  "polyphonically.md": {
    primary: "In a polyphonic manner; combining multiple independent melodic voices, lines, or themes simultaneously.",
    secondary: "Figuratively, expressing multiple distinct viewpoints, narrative voices, or thematic layers in literature or philosophy.",
    quotes: [
      { author: "Mikhail Bakhtin", work: "Problems of Dostoevsky's Poetics", quote: "Dostoevsky structured his novels **polyphonically**, allowing independent consciousnesses to debate without being subordinated to an omniscient author." },
      { author: "Charles Rosen", work: "The Romantic Generation", quote: "Chopin wove inner voices **polyphonically** beneath the principal melody, creating breathtaking harmonic depth." },
      { author: "Theodor W. Adorno", work: "Philosophy of New Music", quote: "Modern orchestral works unfold **polyphonically**, rejecting monolithic homophonic textures in favor of relentless contrapuntal tension." }
    ]
  },
  "polyphonous.md": {
    primary: "Having many sounds or voices; marked by a multiplicity of simultaneous vocal or musical tones; polyphonic.",
    secondary: "Exhibiting multiple phonetic pronunciations or acoustic resonances.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick", quote: "The stormy gale roared with a **polyphonous** fury through the rigging of the Pequod, howling in twenty discordant keys." },
      { author: "Walter Pater", work: "The Renaissance", quote: "The cathedral choir sang in **polyphonous** grandeur, their blended voices filling every vaulted arch with golden resonance." },
      { author: "Thomas De Quincey", work: "The English Mail-Coach", quote: "The midnight wind sweeping over the moor struck the telegraph wires, eliciting a weird, **polyphonous** sigh." }
    ]
  },
  "polyphony.md": {
    primary: "A musical texture consisting of two or more simultaneous, independent melodic lines or voices sounding together in counterpoint.",
    secondary: "In literary theory (formulated by Mikhail Bakhtin), a narrative structure containing multiple autonomous and unmerged voices or worldviews.",
    quotes: [
      { author: "Mikhail Bakhtin", work: "Problems of Dostoevsky's Poetics", quote: "The essence of Dostoevskian novelistic structure is a genuine **polyphony** of fully valid voices." },
      { author: "Paul Henry Lang", work: "Music in Western Civilization", quote: "The flowering of Franco-Flemish **polyphony** established the contrapuntal foundation of all modern European music." },
      { author: "Igor Stravinsky", work: "Poetics of Music", quote: "True **polyphony** demands that each contrapuntal voice maintain its rhythmic vitality and linear integrity." }
    ]
  },
  "saxophone.md": {
    primary: "A single-reed woodwind musical instrument with a conical brass tube and finger keys, invented by Adolphe Sax around 1840.",
    secondary: "An iconic solo instrument in jazz, popular music, and symphonic concert repertoire, renowned for its expressive, flexible, and human-like vocal timbre.",
    quotes: [
      { author: "Jack Kerouac", work: "On the Road", quote: "The tenor **saxophone** player leaned back, closed his eyes, and blew a high, crying note that stopped everyone in their tracks." },
      { author: "Ralph Ellison", work: "Shadow and Act", quote: "Charlie Parker transformed the alto **saxophone** into an extension of his nervous system, redefining the grammar of modern music." },
      { author: "Hector Berlioz", work: "Treatise on Modern Instrumentation and Orchestration", quote: "The **saxophone** possesses a unique timbre, hovering between brass power and the mellow warmth of woodwinds." }
    ]
  },
  "saxophonist.md": {
    primary: "A musician who plays the saxophone.",
    secondary: "A professional instrumentalist specializing in saxophone performance across jazz, classical, or popular music traditions.",
    quotes: [
      { author: "Whitney Balliett", work: "American Musicians: Fifty-Six Portraits in Jazz", quote: "Every jazz **saxophonist** in the post-war era wrestled with the towering musical shadow of Charlie Parker." },
      { author: "Langston Hughes", work: "The Big Sea", quote: "In the smoky Harlem cellar, the young **saxophonist** poured out blues choruses that moved the patrons to tears." },
      { author: "Miles Davis", work: "Miles: The Autobiography", quote: "When John Coltrane stepped up to solo, that man played like no other **saxophonist** who ever lived." }
    ]
  },
  "symphonic.md": {
    primary: "Pertaining to, composed for, or resembling a symphony or full symphony orchestra.",
    secondary: "Figuratively, marked by harmonious grandeur, thematic development, and complex orchestral blending of varied elements.",
    quotes: [
      { author: "Leonard Bernstein", work: "The Infinite Variety of Music", quote: "Beethoven expanded the **symphonic** form into an epic canvas for the expression of universal human struggle." },
      { author: "Virginia Woolf", work: "To the Lighthouse", quote: "The sounds of the summer night gathered into a **symphonic** murmur that lulled the sleeping household." },
      { author: "Romain Rolland", work: "Jean-Christophe", quote: "He listened to the forest wind swelling like a vast **symphonic** prelude, full of mysterious longing." }
    ]
  },
  "symphonious.md": {
    primary: "Harmonious in sound; agreeing or blending together melodiously; symphonic.",
    secondary: "Figuratively, characterized by peaceful accord, unity, and harmonious agreement among diverse people or parts.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "Sounding brass and solemn organs blend their **symphonious** voices to celebrate the eternal throne." },
      { author: "Samuel Taylor Coleridge", work: "Religious Musings", quote: "The universe moved in **symphonious** rhythm, guided by the loving hand of divine providence." },
      { author: "Percy Bysshe Shelley", work: "The Revolt of Islam", quote: "A chorus of **symphonious** voices rose from the liberated multitude, welcoming the dawn of freedom." }
    ]
  },
  "symphonise.md": {
    primary: "To make harmonious or agree in sound; to blend or harmonize together into a unified musical or acoustic whole.",
    secondary: "Figuratively, to bring disparate elements, viewpoints, or components into harmonious coordination or systematic accord.",
    quotes: [
      { author: "Thomas Carlyle", work: "Sartor Resartus", quote: "The philosopher seeks to **symphonise** the clashing discords of human experience into a coherent spiritual truth." },
      { author: "George Saintsbury", work: "A History of Elizabethan Literature", quote: "Spenser knew how to **symphonise** rich archaic diction with delicate melodic verse rhythms." },
      { author: "Ralph Waldo Emerson", work: "Journals", quote: "Nature strives continually to **symphonise** individual striving with the overarching unity of the cosmos." }
    ]
  },
  "symphonist.md": {
    primary: "A composer of symphonies.",
    secondary: "A member of a symphony orchestra, or an orchestral musician or artist who creates grand, harmoniously integrated structures.",
    quotes: [
      { author: "Donald Francis Tovey", work: "Essays in Musical Analysis", quote: "Brahms emerged as the greatest classical **symphonist** of the late nineteenth century, preserving classical architecture with romantic warmth." },
      { author: "Gustav Mahler", work: "Selected Letters", quote: "To be a true **symphonist** means building a world with all the technical means at one's disposal." },
      { author: "Robert Schumann", work: "On Music and Musicians", quote: "We hailed Schubert as a lyrical **symphonist** whose melodies seemed poured directly from heaven." }
    ]
  },
  "symphonize.md": {
    primary: "To agree or harmonize in sound; to combine melodiously or play together in a symphonic manner.",
    secondary: "To bring disparate components, thoughts, or movements into concordant, harmonious unity.",
    quotes: [
      { author: "Walt Whitman", work: "Leaves of Grass", quote: "I hear the chorus of all human passions **symphonize** beneath the arches of the open sky." },
      { author: "William James", work: "The Varieties of Religious Experience", quote: "In mystical states, conflicting emotions **symphonize** into an overwhelming feeling of profound peace." },
      { author: "Henry David Thoreau", work: "A Week on the Concord and Merrimack Rivers", quote: "The ripple of the current and the sighing of the pines **symphonize** in an eternal hymn of nature." }
    ]
  },
  "symphony.md": {
    primary: "An elaborate, multi-movement musical composition for full orchestra, typically featuring sonata form in the opening movement.",
    secondary: "A symphony orchestra; or figuratively, an extraordinary harmonious combination or arrangement of colors, sounds, or elements.",
    quotes: [
      { author: "E. M. Forster", work: "Howards End", quote: "Helen listened with wholehearted absorption as the opening chords of Beethoven's Fifth **Symphony** thundered through Queen's Hall." },
      { author: "Hector Berlioz", work: "Memoirs", quote: "Conducting the final movement of my **symphony**, I felt the entire orchestra vibrate like a single giant instrument." },
      { author: "Willa Cather", work: "The Song of the Lark", quote: "The concert ended with an exhilarating modern **symphony** that left the young singer trembling with artistic ambition." }
    ]
  },
  "telephone.md": {
    primary: "A telecommunications system or apparatus that transmits speech and sound electronically across distances by wire or radio signals.",
    secondary: "To call, contact, or speak with someone using a telephone.",
    quotes: [
      { author: "Alexander Graham Bell", work: "Deposition on the Telephone Patent", quote: "Mr. Watson, come here, I want to see you—these words marked the birth of the electric **telephone**." },
      { author: "F. Scott Fitzgerald", work: "The Great Gatsby", quote: "The shrill ringing of the **telephone** shattered the tense silence of the stifling hotel room." },
      { author: "George Orwell", work: "1984", quote: "Winston sat frozen as the bell of the desk **telephone** rang with startling urgency." }
    ]
  },
  "telephoner.md": {
    primary: "A person who places a telephone call or makes use of a telephone.",
    secondary: "In telecommunications history, an operator or technician employed to operate telephone switchboards or transmitters.",
    quotes: [
      { author: "Sinclair Lewis", work: "Main Street", quote: "The persistent **telephoner** refused to hang up until Carol herself came to the receiver to answer the summons." },
      { author: "Agatha Christie", work: "The Murder of Roger Ackroyd", quote: "Poirot scrutinized the caller's log, determined to identify the mysterious midnight **telephoner**." },
      { author: "Raymond Chandler", work: "The Lady in the Lake", quote: "The nervous **telephoner** spoke in a hushed whisper, fearful of being overheard across the wire." }
    ]
  },
  "telephonic.md": {
    primary: "Pertaining to, transmitted by, or operating through a telephone or telephony system.",
    secondary: "Resembling telephone audio in acoustic fidelity; or characterized by communication over distance.",
    quotes: [
      { author: "H. G. Wells", work: "The War of the Worlds", quote: "All **telephonic** communication between London and the southern suburbs was abruptly severed as the Martians advanced." },
      { author: "Marcel Proust", work: "In Search of Lost Time", quote: "Hearing her voice across the crackling **telephonic** line, I felt the terrifying fragility of human connection across space." },
      { author: "Arthur Conan Doyle", work: "The Disintegration Machine", quote: "A brief **telephonic** summons from Professor Challenger brought me scurrying to his suburban laboratory." }
    ]
  },
  "telephonist.md": {
    primary: "An operator who works a telephone switchboard to connect calls manually.",
    secondary: "A specialist or military communications signaller trained in the operation of field telephones and telephone switchgear.",
    quotes: [
      { author: "Erich Maria Remarque", work: "The Road Back", quote: "The regimental **telephonist** sat crouching in the damp dugout, his headphones pressed tight against the distant shellfire." },
      { author: "Virginia Woolf", work: "Mrs Dalloway", quote: "At the central exchange, the alert **telephonist** deftly plugged jacks into glowing sockets, connecting the busy city's thoughts." },
      { author: "George Bernard Shaw", work: "Heartbreak House", quote: "The frantic orders were relayed by a weary **telephonist** whose voice cracked under the wartime strain." }
    ]
  },
  "telephony.md": {
    primary: "The technology, science, and process of transmitting speech, sounds, or data electronically over distance between telephone instruments.",
    secondary: "The commercial and engineering industry devoted to voice telecommunication networks, switching systems, and cellular infrastructure.",
    quotes: [
      { author: "Guglielmo Marconi", work: "Nobel Lecture", quote: "The advent of wireless **telephony** will soon unite continents in instantaneous spoken dialogue without cables." },
      { author: "Claude Shannon", work: "A Mathematical Theory of Communication", quote: "The statistical nature of speech signals is fundamental to the engineering of modern digital **telephony**." },
      { author: "Lewis Mumford", work: "Technics and Civilization", quote: "The development of electrical **telephony** annihilated geographic distance, collapsing society into an instantaneous global web." }
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

console.log('Done Batch 6 (phon Part 2) of Cluster Sound & Auditory!');
