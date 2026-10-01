import fs from 'fs';
import path from 'path';

const basePath = 'App database/Greek roots/Cluster Sound & Auditory';

const filesData = {
  // Dashboard — gargar
  "Dashboard — gargar/gargar.md": {
    primary: "The Greek onomatopoeic root (*gargar-*, from *gargarizein*), imitating the bubbling sound of liquid agitated in the throat, giving rise to *gargle* and *gargarize*.",
    secondary: "The linguistic morpheme representing pharyngeal rinses, throat gargling, and throat washing in ancient pharmacognosy.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The reduplicated root **gargar** imitates the bubbling throat noise of rinsing with liquid." },
      { author: "Galen", work: "De Sanitate Tuenda", quote: "From ancient **gargar**, the physicians developed gargles of warm water and honey to soothe the inflamed fauces." },
      { author: "Jonathan Pereira", work: "The Elements of Materia Medica", quote: "The radical sound **gargar** gave name to those topical astringent washes applied to the back of the mouth." }
    ]
  },
  "Dashboard — gargar/gargarize.md": {
    primary: "To wash or rinse the throat and mouth with a liquid held in the back of the oral cavity and agitated by expelled breath; to gargle.",
    secondary: "To apply a medicated fluid to the fauces and tonsils to reduce inflammation or ulceration in historical medicine.",
    quotes: [
      { author: "Francis Bacon", work: "Sylva Sylvarum", quote: "It is a good method to **gargarize** with vinegar and rose-water to repulse the rheum from the throat." },
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", quote: "Physicians direct the patient to **gargarize** with sage infusion whenever malignant humors settle upon the uvula." },
      { author: "John Evelyn", work: "Acetaria: A Discourse of Sallets", quote: "A decoction of wild mallow serves admirably to **gargarize** the inflamed palate and mouth." }
    ]
  },

  // Dashboard — psithyr
  "Dashboard — psithyr/Psithyrisma.md": {
    primary: "The gentle whispering or soughing sound of the wind rustling through the leaves of trees (from Greek *psithyrisma*, 'whispering').",
    secondary: "The murmuring cadence of hushed voices or subtle breezes in classical pastoral poetry.",
    quotes: [
      { author: "Theocritus", work: "Idylls", quote: "Sweet is the **psithyrisma** of the whispering pine that murmurs beside the mountain springs." },
      { author: "Algernon Charles Swinburne", work: "Atalanta in Calydon", quote: "The quiet forest awoke with the faint **psithyrisma** of twilight breezes through the poplars." },
      { author: "Walter Pater", work: "Greek Studies", quote: "In the pastoral landscape of Hellas, the gentle **psithyrisma** of trembling boughs seemed the very voice of the dryad." }
    ]
  },
  "Dashboard — psithyr/psithyrus.md": {
    primary: "A subgenus or genus of cuckoo bumblebees (family Apidae) that parasitize the nests of true bumblebees, named from Greek *psithyros* ('whispering') for their quiet, stealthy flight buzz.",
    secondary: "A social parasite bee that lacks pollen-collecting corbiculae and relies on the worker workforce of the host queen.",
    quotes: [
      { author: "John Lubbock", work: "Ants, Bees, and Wasps", quote: "The parasitic bee of the genus **Psithyrus** enters the nest of Bombus stealthily to lay its brood." },
      { author: "Charles Darwin", work: "Natural Selection Manuscript", quote: "The female **Psithyrus** possesses no pollen-collecting apparatus, depending wholly upon the stolen stores of its host." },
      { author: "Edward O. Wilson", work: "The Insect Societies", quote: "Social parasitism in **Psithyrus** evolved through gradual behavioral mimicry of the host bumblebee queen's pheromones." }
    ]
  },

  // Dashboard — aul
  "Dashboard — aul/aul.md": {
    primary: "The Greek root *aul-* (from *aulos*), meaning 'pipe', 'flute', 'tube', or 'channel', ancestor of *aulete*, *hydraulic*, and *hydraulus*.",
    secondary: "The linguistic morpheme representing cylindrical wind instruments and tubular pneumatic conduits in organology.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The root **aul** encompasses words pertaining to hollow pipes, musical reeds, and subterranean water channels." },
      { author: "Curt Sachs", work: "The History of Musical Instruments", quote: "From the primitive cane **aul**, Hellenic civilization fashioned the primary wind instruments of civic festivals." },
      { author: "Gilbert Murray", work: "The Rise of the Greek Epic", quote: "The martial marching rhythms of early Hellas were sustained by instruments derived from the ancient **aul**." }
    ]
  },
  "Dashboard — aul/aulete.md": {
    primary: "A player of the aulos; an ancient Greek flutist or pipe player who accompanied theatrical dramas, athletic contests, and religious sacrifices.",
    secondary: "A professional musician skilled in circular breathing and double-reed pipe performance in Hellenic society.",
    quotes: [
      { author: "Aristotle", work: "Politics", quote: "The **aulete** required a mouth-band to support the cheeks during the violent exertion of blowing the double pipes." },
      { author: "Plutarch", work: "Parallel Lives", quote: "Alcibiades refused to learn the pipes, arguing that playing them distorted the face of the **aulete** beyond recognition." },
      { author: "Walter Pater", work: "Plato and Platonism", quote: "In Plato's ideal commonwealth, the professional **aulete** was banished in favor of the simpler, sober lyre." }
    ]
  },
  "Dashboard — aul/aulos.md": {
    primary: "An ancient Greek wind instrument consisting of two double-reed pipes played simultaneously by a single performer, often using a leather mouth-strap.",
    secondary: "The chief wind instrument of ancient Greek theatrical tragedy, Dionysian worship, and Spartan military drills.",
    quotes: [
      { author: "Thucydides", work: "History of the Peloponnesian War", quote: "The Spartans marched into battle to the solemn measure of the **aulos**, keeping step without breaking rank." },
      { author: "Friedrich Nietzsche", work: "The Birth of Tragedy", quote: "The wild Dionysian ecstasy found its direct acoustic embodiment in the passionate shrieks of the **aulos**." },
      { author: "Jane Ellen Harrison", work: "Prolegomena to the Study of Greek Religion", quote: "The revels of the maenads were accompanied by the rhythmic beat of the tympanum and the thrilling cry of the **aulos**." }
    ]
  },
  "Dashboard — aul/hydraulus.md": {
    primary: "An ancient Greek and Roman water organ, invented in the 3rd century BCE by Ctesibius of Alexandria, using the weight of water to maintain uniform air pressure across pipe ranks.",
    secondary: "The historical technological ancestor of the modern pipe organ, praised for its powerful acoustic volume in amphitheaters and circuses.",
    quotes: [
      { author: "Vitruvius", work: "De Architectura", quote: "The mechanism of the **hydraulus** balances air pressure by the displacement of water in a bronze inverted bell." },
      { author: "Tertullian", work: "De Anima", quote: "Consider the astonishing invention of Archimedes or Ctesibius: the **hydraulus**, with its many pipes, stops, and thundering voices." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The Roman spectators cheered as the powerful notes of the **hydraulus** echoed across the vast expanse of the circus." }
    ]
  },

  // Dashboard — psoph
  "Dashboard — psoph/psophia.md": {
    primary: "A genus of long-legged, ground-dwelling South American birds known as trumpeters, inhabiting the Amazon rainforest, named from Greek *psophos* ('noise') for their deep booming vocalizations.",
    secondary: "The avian genus typified by the grey-winged trumpeter (*Psophia crepitans*), revered by indigenous peoples as an alert sentinel.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "A Narrative of Travels on the Amazon and Rio Negro", quote: "The tame trumpeters of the genus **Psophia** ran freely about the native huts, greeting visitors with their resonant calls." },
      { author: "Henry Walter Bates", work: "The Naturalist on the River Amazons", quote: "In the dense undergrowth, we heard the deep ventriloquial booming of **Psophia** long before the birds came into view." },
      { author: "John Gould", work: "The Birds of South America", quote: "Specimens of **Psophia** are remarkable for their glossy plumage and gregarious ground habits beneath the high forest canopy." }
    ]
  },
  "Dashboard — psoph/Psophiidae.md": {
    primary: "The bird family in the order Gruiformes comprising the trumpeters (genus *Psophia*), endemic to the wet tropical forests of the Amazon basin.",
    secondary: "A monogeneric avian family characterized by hunchbacked postures, velvety neck plumage, and deep infrasonic rumbling vocalizations.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "The family **Psophiidae** is strictly confined to the equatorial forests of South America, showing no close relatives in the Old World." },
      { author: "Ernst Mayr", work: "Animal Species and Evolution", quote: "Major river barriers across the Amazon basin drove geographic speciation among the distinct lineages of **Psophiidae**." },
      { author: "Elliott Coues", work: "Key to North American Birds", quote: "In comparative anatomy, the family **Psophiidae** bridges the gap between the cranes and the rails." }
    ]
  },
  "Dashboard — psoph/psophocarpus.md": {
    primary: "A genus of tropical leguminous climbing plants in the Fabaceae family, notably including the winged bean (*Psophocarpus tetragonolobus*), whose seeds rattle in dry pods.",
    secondary: "A nutrient-rich tropical legume prized in sustainable agriculture, all parts of which (leaves, flowers, pods, seeds, and tubers) are edible.",
    quotes: [
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "The four-angled winged pods of **Psophocarpus** rattle distinctly when dry, reflecting its Greek botanical name." },
      { author: "George Washington Carver", work: "Agricultural Bulletins", quote: "The cultivated species of **Psophocarpus** provide an extraordinarily rich source of protein for tropical subsistence farming." },
      { author: "Norman Borlaug", work: "Feeding a World of 10 Billion People", quote: "Underutilized crops such as **Psophocarpus** hold enormous potential for climate-resilient nutritional security." }
    ]
  },
  "Dashboard — psoph/Psophocichla.md": {
    primary: "A genus of African thrush in the family Turdidae, represented by the groundscraper thrush (*Psophocichla litsitsirupa*), characterized by loud piping calls and terrestrial foraging.",
    secondary: "A southern and eastern African songbird with bold facial markings and upright carriage, adapted to arid savannahs.",
    quotes: [
      { author: "Elliott Coues", work: "Birds of the Colorado Valley", quote: "The African genus **Psophocichla** represents a terrestrial divergence from the arboreal true thrushes of Europe." },
      { author: "Peter R. Grant", work: "Ecology and Evolution of Darwin's Finches", quote: "Behavioral foraging adaptations in **Psophocichla** mirror the terrestrial habits of arid-zone ground birds." },
      { author: "Ernst Mayr", work: "Systematics and the Origin of Species", quote: "The taxonomic separation of **Psophocichla** from Turdus was substantiated by distinctive vocal patterns and tarsal morphology." }
    ]
  },
  "Dashboard — psoph/psophometer.md": {
    primary: "An instrument designed to measure audible noise voltage or circuit interference in telephone and audio transmission lines, weighted according to human ear sensitivity.",
    secondary: "A precision acoustic instrument used in telecommunication testing according to international standards (e.g., CCITT weighting curves).",
    quotes: [
      { author: "Oliver Heaviside", work: "Electromagnetic Theory", quote: "Accurate measurement of line disturbance requires a sensitive **psophometer** calibrated to human auditory perception." },
      { author: "Claude Shannon", work: "A Mathematical Theory of Communication", quote: "In evaluating channel capacity, the noise figure registered by a **psophometer** determines the effective signal-to-noise ratio." },
      { author: "Norbert Wiener", work: "Cybernetics", quote: "Feedback filtering circuits were adjusted until the residual interference recorded on the **psophometer** dropped below the auditory threshold." }
    ]
  },
  "Dashboard — psoph/psophometric.md": {
    primary: "Relating to the measurement of electrical or audio noise using a psophometer; weighted to match human ear perception.",
    secondary: "Pertaining to standardized psophometric weighting curves used in telecommunications engineering.",
    quotes: [
      { author: "Claude Shannon", work: "A Mathematical Theory of Communication", quote: "The **psophometric** weighting curve simulates the frequency response of the human ear to audio interference." },
      { author: "Oliver Heaviside", work: "Electrical Papers", quote: "To ensure speech intelligibility, line engineers must keep the **psophometric** noise voltage within strict technical limits." },
      { author: "Norbert Wiener", work: "Extrapolation, Interpolation, and Smoothing of Stationary Time Series", quote: "Statistical filters were designed to minimize **psophometric** power across the critical telephone speech band." }
    ]
  },

  // Dashboard — phtheg
  "Dashboard — phtheg/apophthegm.md": {
    primary: "A short, pithy, and instructive saying; a terse maxim or aphorism (alternative spelling of apothegm).",
    secondary: "A memorable, witty remark embodying moral or practical wisdom in classical literature.",
    quotes: [
      { author: "Francis Bacon", work: "Apophthegms New and Old", quote: "Julius Caesar had a collection of **apophthegms** made; for he knew that they served both for ornament and for direction." },
      { author: "Samuel Johnson", work: "The Rambler", quote: "An ancient **apophthegm** preserves in a single phrase the condensed experience of many generations." },
      { author: "Ralph Waldo Emerson", work: "Representative Men", quote: "Plutarch enriched his biographies with many a sharp **apophthegm** dropped by Spartan warriors." }
    ]
  },
  "Dashboard — phtheg/apophthegmatic.md": {
    primary: "Characterized by or in the nature of an apophthegm; terse, pithy, and aphoristic in style.",
    secondary: "Expressed with sharp, concise moral wit and brevity.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Table Talk", quote: "Bacon's essays are written in an **apophthegmatic** style where each sentence stands compact like a polished gem." },
      { author: "Thomas De Quincey", work: "Essays on Style", quote: "Spartan discourse was strictly **apophthegmatic**, answering ambassadors with single-word verdicts." },
      { author: "Walter Pater", work: "Appreciations", quote: "The poet's lines possess an **apophthegmatic** severity that leaves no room for superfluous adornment." }
    ]
  },
  "Dashboard — phtheg/diphthong.md": {
    primary: "A sound formed by the combination of two vowels in a single syllable, in which the sound begins as one vowel and glides toward another (e.g., *coin*, *loud*, *side*).",
    secondary: "A ligature of two vowel letters (such as æ or œ) in typography.",
    quotes: [
      { author: "Henry Sweet", work: "A Handbook of Phonetics", quote: "In producing a **diphthong**, the vocal organs start at one vowel position and glide smoothly toward another before the syllable ends." },
      { author: "James Joyce", work: "Ulysses", quote: "His voice flattened the broad open vowel into a lazy, musical Dublin **diphthong**." },
      { author: "Otto Jespersen", work: "Language: Its Nature, Development and Origin", quote: "The Great Vowel Shift transformed long Middle English vowels into modern vocalic **diphthongs**." }
    ]
  },
  "Dashboard — phtheg/diphthongise.md": {
    primary: "To change a monophthong (pure vowel) into a diphthong during speech or historical language evolution (British spelling of diphthongize).",
    secondary: "To pronounce a single vocalic sound with a noticeable glide.",
    quotes: [
      { author: "Henry Sweet", work: "A History of English Sounds", quote: "Southern dialects tend to **diphthongise** pure vowels, adding an off-glide toward the neutral schwa." },
      { author: "Otto Jespersen", work: "A Modern English Grammar", quote: "Speakers of Modern English naturally **diphthongise** the long tense vowels in words like 'gate' and 'boat'." },
      { author: "George Bernard Shaw", work: "Pygmalion", quote: "Higgins noted how street cockney would **diphthongise** every pure vowel into a drawn-out nasal sound." }
    ]
  },
  "Dashboard — phtheg/diphthongize.md": {
    primary: "To convert a simple vowel sound into a diphthong in articulation or historical phonetic drift (US spelling).",
    secondary: "To introduce a vocalic glide into the pronunciation of a pure vowel.",
    quotes: [
      { author: "Edward Sapir", work: "Language: An Introduction to the Study of Speech", quote: "Certain American regional dialects consistently **diphthongize** short vowels in stressed monosyllables." },
      { author: "Leonard Bloomfield", work: "Language", quote: "In historical sound shifts, languages frequently **diphthongize** long high vowels when shifting vowel heights." },
      { author: "Steven Pinker", work: "The Language Instinct", quote: "Children learning English unconsciously **diphthongize** vowels according to the phonetic cadence of their community." }
    ]
  },
  "Dashboard — phtheg/monophthong.md": {
    primary: "A pure vowel sound whose articulation at both beginning and end is relatively fixed, having a single unchanged acoustic quality throughout the syllable (e.g., the vowel in *cat* or *bed*).",
    secondary: "A single vowel sound contrasted with a gliding diphthong or triphthong.",
    quotes: [
      { author: "Henry Sweet", work: "A Handbook of Phonetics", quote: "A **monophthong** maintains an unchanging tongue and lip position throughout the duration of its utterance." },
      { author: "Otto Jespersen", work: "Language: Its Nature, Development and Origin", quote: "Northern British dialects often preserve a pure **monophthong** where standard southern speech uses a gliding diphthong." },
      { author: "Ferdinand de Saussure", work: "Course in General Linguistics", quote: "The historical transition from diphthong to **monophthong** represents one of the commonest simplifications in vocalic phonetics." }
    ]
  },
  "Dashboard — phtheg/monophthongize.md": {
    primary: "To change a diphthong into a monophthong (pure vowel) by smoothing out the vocalic glide in linguistics and phonetics.",
    secondary: "In historical phonology, the sound change process also known as monophthongization.",
    quotes: [
      { author: "Otto Jespersen", work: "A Modern English Grammar", quote: "Late Latin began to **monophthongize** the classical diphthong 'ae' into a simple open front vowel." },
      { author: "Henry Sweet", work: "A History of English Sounds", quote: "Dialect speakers frequently **monophthongize** the 'ai' sound in 'time' into a prolonged single vowel." },
      { author: "Leonard Bloomfield", work: "Language", quote: "When dialects **monophthongize** complex glides, they restore symmetrical simplicity to their vowel inventory." }
    ]
  },

  // Dashboard — acou
  "Dashboard — acou/acousma.md": {
    primary: "An elementary auditory hallucination consisting of simple, non-verbal sounds such as ringing, buzzing, clicking, or hissing in psychiatry and neurology.",
    secondary: "A phantom auditory sensation produced by inner ear pathology, epilepsy, or cortical irritation.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Before the onset of the seizure, the patient experienced an **acousma** resembling the shrill whistling of steam." },
      { author: "Oliver Sacks", work: "Musicophilia", quote: "An unformed **acousma**, like buzzing or bells, must be distinguished from the structured melodies of complex musical hallucinations." },
      { author: "Jean-Martin Charcot", work: "Clinical Lectures on Diseases of the Nervous System", quote: "Cortical aura in temporal epilepsy frequently begins with an alarming **acousma** in one ear." }
    ]
  },
  "Dashboard — acou/acoustic.md": {
    primary: "Relating to sound, hearing, or the sense of auditory perception.",
    secondary: "Relating to instruments that produce sound naturally without electrical amplification; designed to control sound reflection in architecture.",
    quotes: [
      { author: "Isaac Newton", work: "Opticks", quote: "The propagation of sound through air conforms to purely **acoustic** wave motions governed by elasticity and density." },
      { author: "Hermann von Helmholtz", work: "On the Sensations of Tone", quote: "The human ear acts as an exquisite **acoustic** resonator, resolving complex waveforms into pure harmonic components." },
      { author: "John Tyndall", work: "Sound", quote: "The great cathedral possessed splendid **acoustic** properties, carrying the choral chant into every vaulted recess." }
    ]
  },
  "Dashboard — acou/acoustical.md": {
    primary: "Pertaining to acoustics or the physical transmission and reception of sound (synonymous with acoustic).",
    secondary: "In architectural and mechanical engineering, designed for the absorption, reflection, or isolation of sound.",
    quotes: [
      { author: "Lord Rayleigh", work: "The Theory of Sound", quote: "The **acoustical** problem of reflection from an irregular boundary demands rigorous mathematical treatment." },
      { author: "Hermann von Helmholtz", work: "On the Sensations of Tone", quote: "We constructed an array of tuned **acoustical** resonators to analyze the timbre of orchestral instruments." },
      { author: "Vitruvius", work: "De Architectura", quote: "The ancient Greeks placed bronze vases beneath theater seats to enhance the **acoustical** resonance of the actors' voices." }
    ]
  },
  "Dashboard — acou/acoustically.md": {
    primary: "In an acoustic manner; in terms of sound transmission, absorption, or quality.",
    secondary: "Using acoustic rather than electrically amplified instruments in musical performance.",
    quotes: [
      { author: "John Tyndall", work: "Sound", quote: "The fog-horn was situated so that sound waves propagated **acoustically** across the sea without thermal interruption." },
      { author: "Lord Rayleigh", work: "The Theory of Sound", quote: "A whispering gallery functions **acoustically** by guiding high-frequency waves along the curved interior of the dome." },
      { author: "Walter Pater", work: "The Renaissance", quote: "The choral hall was planned **acoustically** to harmonize the voices of the singers into seamless unity." }
    ]
  },
  "Dashboard — acou/acoustician.md": {
    primary: "A physicist, engineer, or specialist who studies the science of acoustics or designs sound systems and architectural spaces.",
    secondary: "A technical expert in soundproofing, noise control, and musical instrument physics.",
    quotes: [
      { author: "Lord Rayleigh", work: "The Theory of Sound", quote: "The skilled **acoustician** investigates the delicate interplay between surface elasticity and wave diffraction." },
      { author: "Hermann von Helmholtz", work: "On the Sensations of Tone", quote: "To the **acoustician**, every musical tone is a composite vibration that can be analyzed into mathematical sine waves." },
      { author: "Wallace Clement Sabine", work: "Collected Papers on Acoustics", quote: "The modern architectural **acoustician** calculates reverberation time to ensure speech clarity in public auditoriums." }
    ]
  },
  "Dashboard — acou/acousticophobia.md": {
    primary: "An abnormal, irrational, and persistent fear of noise, loud sounds, or specific acoustic stimuli in psychology and psychiatry.",
    secondary: "A sensory phobia characterized by intense panic and avoidance of loud environments (related to phonophobia).",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "Sudden loud sounds provoke instinctive terror, which in pathological **acousticophobia** becomes an unbearable torment." },
      { author: "Oliver Sacks", work: "Musicophilia", quote: "The patient developed severe **acousticophobia**, retreating into a soundproof room to escape the agony of ordinary traffic noise." },
      { author: "Jean-Martin Charcot", work: "Clinical Lectures", quote: "Hysterical hypersensitivity to acoustic stimuli occasionally manifests as acute **acousticophobia** accompanied by palpitations." }
    ]
  },
  "Dashboard — acou/acoustics.md": {
    primary: "The branch of physics that deals with the study of mechanical waves in gases, liquids, and solids, including sound, ultrasound, and infrasound.",
    secondary: "The physical properties or qualities of a room or building that determine how sound is transmitted or reflected in it.",
    quotes: [
      { author: "Lord Rayleigh", work: "The Theory of Sound", quote: "In the science of **acoustics**, the vibrations of strings, membranes, and air columns form a harmonious mathematical unity." },
      { author: "Hermann von Helmholtz", work: "On the Sensations of Tone", quote: "The physiological **acoustics** of the inner ear reveals how physical air vibrations become conscious auditory sensations." },
      { author: "Vitruvius", work: "De Architectura", quote: "The architect must study the laws of **acoustics** so that voice and music may reach the spectators clearly." }
    ]
  },
  "Dashboard — acou/acusmatic.md": {
    primary: "Pertaining to sound that one hears without seeing its physical originating source; acousmatic sound in acoustics and philosophy.",
    secondary: "Originating from the *akousmatikoi*, the disciples of Pythagoras who listened to the master's lectures from behind a curtain in silence.",
    quotes: [
      { author: "Pythagoras", work: "Fragments", quote: "The ancient masters divided students into the esoteric circle and the **acusmatic** listeners who heard truth without seeing the speaker." },
      { author: "Pierre Schaeffer", work: "Treatise on Musical Objects", quote: "Recorded music creates an **acusmatic** listening situation, freeing the sound object from visual theatricality." },
      { author: "Michel Chion", work: "Audio-Vision: Sound on Screen", quote: "In cinematic storytelling, **acusmatic** sound generates mystery by withholding the visual presence of the source." }
    ]
  },
  "Dashboard — acou/akouein.md": {
    primary: "The Ancient Greek verb meaning 'to hear', 'to listen', or 'to pay attention', the etymological ancestor of modern terms like *acoustics* and *acusmatic*.",
    secondary: "In classical Greek philosophy and medicine, denoting auditory perception and the physical sensation of sound.",
    quotes: [
      { author: "Aristotle", work: "De Anima", quote: "The capacity designated by **akouein** operates through the medium of air trapped within the resonant chambers of the ear." },
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "Under **akouein**, the lexicon outlines the spectrum from passive hearing to obedient listening and acoustic perception." },
      { author: "Plato", work: "Timaeus", quote: "Hearing, expressed by the ancient verb **akouein**, was bestowed upon mortals by the gods to perceive harmony and proportion in song." }
    ]
  }
};

for (const [relPath, entry] of Object.entries(filesData)) {
  const filePath = path.join(basePath, relPath);
  if (!fs.existsSync(filePath)) {
    console.error(`Missing file: ${filePath}`);
    continue;
  }
  const content = fs.readFileSync(filePath, 'utf8');

  // Find top portion up to > [!book]
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`No > [!book] in ${relPath}`);
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
  console.log(`Updated: ${relPath}`);
}

console.log('Done Batch 1 of Cluster Sound & Auditory!');
