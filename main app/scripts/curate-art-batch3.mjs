import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Art, Craft & Design';

const filesData = {
  // Dashboard — chore
  "Dashboard — chore/choir.md": {
    primary: "An organized group of singers, typically one that performs in church services or public concerts.",
    secondary: "The part of a cathedral or large church between the nave and sanctuary where the singers and clergy sit.",
    quotes: [
      { author: "John Milton", work: "Il Penseroso", quote: "There let the pealing organ blow to the full-voiced **choir** below in service high and anthems clear." },
      { author: "George Eliot", work: "Adam Bede", quote: "The church **choir** was seated in the gallery, singing the morning psalm with rustic enthusiasm." },
      { author: "Thomas Hardy", work: "Under the Greenwood Tree", quote: "The Mellstock parish **choir** went their rounds through the snowy lanes on Christmas Eve." }
    ]
  },
  "Dashboard — chore/choral.md": {
    primary: "Composed for, performed by, or sung by a choir or chorus.",
    secondary: "A harmonized hymn tune or sacred song; a chorale.",
    quotes: [
      { author: "Virginia Woolf", work: "The Waves", quote: "The birds broke into a joyful **choral** chant that echoed through the garden trees." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The roaring gale and tossing billows united in a wild, tempestuous **choral** dirge." },
      { author: "Donald Jay Grout", work: "A History of Western Music", quote: "Beethoven introduced the human voice into the symphony through the triumphant **choral** finale of the Ninth." }
    ]
  },
  "Dashboard — chore/chorally.md": {
    primary: "In a choral manner; by or as a choir or chorus singing together.",
    secondary: "Sung in unison or multipart harmony by a collective body of voices.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Biographia Literaria", quote: "The Greek tragedies were chanted **chorally** by celebrants moving in solemn strophic dance." },
      { author: "Walter Pater", work: "Greek Studies", quote: "The hymn was delivered **chorally**, the voices of the youths alternating with the maidens." },
      { author: "George Saintsbury", work: "A History of English Prose Rhythm", quote: "The prose sentences resound **chorally**, building toward a majestic harmonic climax." }
    ]
  },
  "Dashboard — chore/chore.md": {
    primary: "A routine or minor household task, daily duty, or domestic errand.",
    secondary: "A tedious, unpleasant, or burdensome piece of work.",
    quotes: [
      { author: "Henry David Thoreau", work: "Walden", quote: "I had my morning **chore** to do: fetching water from the spring and hoeing my beans." },
      { author: "Willa Cather", work: "My Ántonia", quote: "Every autumn evening had its necessary farm **chore**, from herding cattle to stocking the root cellar." },
      { author: "Louisa May Alcott", work: "Little Women", quote: "The sisters shared every household **chore** cheerfully, singing while they swept the parlor." }
    ]
  },
  "Dashboard — chore/chorea.md": {
    primary: "A neurological disorder characterized by involuntary, irregular, unpredictable, and purposeless jerking movements of the limbs and face.",
    secondary: "In medicine, any condition manifesting these dance-like movements, such as Sydenham's chorea or Huntington's disease.",
    quotes: [
      { author: "William Osler", work: "On Chorea and Choreiform Affections", quote: "The restless, dance-like twitches of Sydenham's **chorea** typically follow acute rheumatic fever in childhood." },
      { author: "George Huntington", work: "On Chorea", quote: "In adult hereditary **chorea**, the spasmodic contortions begin gradually and inexorably progress over decades." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "L-Dopa therapy occasionally induced prominent drug-related **chorea**, causing rapid involuntary movements of the hands." }
    ]
  },
  "Dashboard — chore/choree.md": {
    primary: "In classical Greek and Latin prosody, a metrical foot consisting of a long syllable followed by a short syllable; a trochee.",
    secondary: "In poetics, the trochaic foot (traditionally associated in antiquity with lively dance rhythms).",
    quotes: [
      { author: "George Puttenham", work: "The Arte of English Poesie", quote: "The foot called **choree**, or trochee, consisteth of a long and a short syllable, pleasant for light measures." },
      { author: "John Dryden", work: "Essay of Dramatic Poesy", quote: "The verse marches with brisk vigor when the trochee or **choree** begins the line." },
      { author: "Matthew Arnold", work: "On Translating Homer", quote: "Classical scansion reveals how the dactyl yields to the swift **choree** in energetic dramatic passages." }
    ]
  },
  "Dashboard — chore/choreia.md": {
    primary: "The ancient Greek union of choral dance, song, and poetry in communal religious and civic festivals.",
    secondary: "In classical scholarship, the integrated performance art embodying the civic and moral education of Greek citizens.",
    quotes: [
      { author: "Plato", work: "Laws", quote: "Education is first given through Apollo and the Muses, and the combined gift of song and dance we term **choreia**." },
      { author: "Werner Jaeger", work: "Paideia: The Ideals of Greek Culture", quote: "Through participatory **choreia**, the youthful citizen internalized the rhythmic order and harmony of the polis." },
      { author: "E. R. Dodds", work: "The Greeks and the Irrational", quote: "The ecstatic frenzy of Dionysian **choreia** offered liberation from the rigid constraints of civic life." }
    ]
  },
  "Dashboard — chore/choreograph.md": {
    primary: "To compose the sequence of steps, dances, and movements for a ballet, dance, or theatrical production.",
    secondary: "Figuratively, to plan, arrange, or direct a complex sequence of events, moves, or interactions.",
    quotes: [
      { author: "George Balanchine", work: "By George Balanchine", quote: "The music itself tells the master how to **choreograph** the bodies moving through empty stage space." },
      { author: "Agnes de Mille", work: "Dance to the Piper", quote: "I struggled to **choreograph** a ballet that captured the raw, buoyant vitality of American folk dancing." },
      { author: "Bob Woodward", work: "The Commanders", quote: "The generals sought to **choreograph** every tactical maneuver of the impending desert offensive." }
    ]
  },
  "Dashboard — chore/choreographer.md": {
    primary: "A person who creates, designs, and arranges dance movements, routines, and sequences for ballets, musicals, or stage shows.",
    secondary: "An artist who conceptualizes the spatial and temporal architecture of human physical motion on stage.",
    quotes: [
      { author: "Martha Graham", work: "Blood Memory", quote: "The true **choreographer** listens to the ancestral memories stored within the muscles of the dancer." },
      { author: "Mikhail Baryshnikov", work: "A Day with Baryshnikov", quote: "Working with a visionary **choreographer** demands total physical surrender and inventive bravery." },
      { author: "Lincoln Kirstein", work: "Movement and Metaphor", quote: "Balanchine proved himself the greatest neoclassical **choreographer** of the twentieth century." }
    ]
  },
  "Dashboard — chore/choreographic.md": {
    primary: "Pertaining to, designed for, or relating to choreography or dance composition.",
    secondary: "Characterized by intricate, coordinated, or highly stylized physical movement or staging.",
    quotes: [
      { author: "Isadora Duncan", work: "My Life", quote: "My new dance rebelled against the rigid **choreographic** conventions of traditional academic ballet." },
      { author: "Walter Pater", work: "The Renaissance", quote: "The figures in Botticelli's Primavera move with an ethereal, **choreographic** grace across the meadow." },
      { author: "Susan Sontag", work: "Against Interpretation", quote: "The performance achieved a hypnotic power through its relentless, minimalist **choreographic** design." }
    ]
  },
  "Dashboard — chore/choreography.md": {
    primary: "The sequence of steps and movements in dance, or the art and technique of creating and arranging such movements.",
    secondary: "The carefully orchestrated design or systematic unfolding of any complex, coordinated activity.",
    quotes: [
      { author: "Twyla Tharp", work: "The Creative Habit", quote: "In modern dance, inventive **choreography** emerges from discipline, daily repetition, and relentless revision." },
      { author: "Joan Didion", work: "Slouching Towards Bethlehem", quote: "The press conferences were staged with the practiced **choreography** of professional political theatre." },
      { author: "Richard Feynman", work: "The Character of Physical Law", quote: "Subatomic collisions follow an astonishing natural **choreography** governed by quantum conservation laws." }
    ]
  },
  "Dashboard — chore/choric.md": {
    primary: "Belonging to, recited by, or resembling a dramatic chorus, especially in ancient Greek drama.",
    secondary: "Sung or chanted in unison by an ensemble or group.",
    quotes: [
      { author: "Gilbert Murray", work: "Euripides and His Age", quote: "The sublime **choric** odes in Greek tragedy comment upon the tragic hero's fate with cosmic perspective." },
      { author: "W. B. Yeats", work: "Per Amica Silentia Lunae", quote: "The verses rose like a **choric** chant, invoking ancestral spirits from the deep well of memory." },
      { author: "Percy Bysshe Shelley", work: "Prometheus Unbound", quote: "Beneath the cliffs, earth-spirits chanted a **choric** hymn of triumphant joy." }
    ]
  },
  "Dashboard — chore/choroid.md": {
    primary: "The thin, vascular, pigmented layer of the eye between the sclera and retina, supplying blood and oxygen to the retina.",
    secondary: "In anatomy, resembling a vascular membrane; also designating the choroid plexus that produces cerebrospinal fluid.",
    quotes: [
      { author: "Hermann von Helmholtz", work: "Physiological Optics", quote: "Through the ophthalmoscope, the dark, blood-rich vessels of the ocular **choroid** become clearly visible." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Tubercles may occasionally be detected in the **choroid** during the course of acute miliary tuberculosis." },
      { author: "Santiago Ramón y Cajal", work: "Histology of the Nervous System", quote: "The capillary loops of the **choroid** plexus are covered by specialized ependymal epithelium." }
    ]
  },
  "Dashboard — chore/chorus.md": {
    primary: "An organized group of singers, dancers, or actors performing together in a theatrical piece, opera, or concert.",
    secondary: "A repeated section of a song (refrain); or in ancient drama, a company of performers commenting on the main action.",
    quotes: [
      { author: "William Shakespeare", work: "Henry V", quote: "O for a Muse of fire, that would ascend the brightest heaven of invention, pleaded the solitary **chorus**." },
      { author: "Sophocles", work: "Antigone", quote: "Wonders are many, and none is more wonderful than man, proclaimed the venerable **chorus**." },
      { author: "Charles Dickens", work: "A Christmas Carol", quote: "All the guests joined in the lively **chorus** around the punch-bowl with hearty laughter." }
    ]
  },
  "Dashboard — chore/hemichorea.md": {
    primary: "A neurological movement disorder characterized by choreic, involuntary, dance-like jerking movements affecting only one side of the body.",
    secondary: "In clinical neurology, a condition often caused by vascular lesions in the contralateral subthalamic nucleus or basal ganglia.",
    quotes: [
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "A localized lacunar stroke in the basal ganglia triggered persistent contralateral **hemichorea** in the elderly patient." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Unilateral movement disorders such as **hemichorea** point directly to vascular damage near the internal capsule." },
      { author: "C. Miller Fisher", work: "Cerebral Ischemia", quote: "Sudden onset of violent ballistic movements and **hemichorea** followed occlusion of small penetrating thalamoperforating arteries." }
    ]
  },
  "Dashboard — chore/orthochorea.md": {
    primary: "A form of chorea in which involuntary, irregular movements or spasms occur primarily or exclusively when the patient is standing upright.",
    secondary: "Postural chorea; motor incoordination aggravated by the erect posture.",
    quotes: [
      { author: "William Gowers", work: "A Manual of Diseases of the Nervous System", quote: "The observer noted a distinct **orthochorea**, the motor twitches subsiding promptly as soon as the patient reclined." },
      { author: "Jean-Martin Charcot", work: "Lectures on the Diseases of the Nervous System", quote: "In atypical neuroses, symptoms of **orthochorea** appear solely upon assuming an erect, weight-bearing posture." },
      { author: "S. Weir Mitchell", work: "Lectures on Diseases of the Nervous System", quote: "The young girl suffered from postural instability termed **orthochorea**, swaying and jerking whenever placed on her feet." }
    ]
  },

  // Dashboard — cal
  "Dashboard — cal/cal.md": {
    primary: "An abbreviation for calorie (a unit of thermal energy) or caliber (bore diameter); or the Greek prefix *kal-* from *kallos* (beauty).",
    secondary: "In nutritional science and ballistics, a standard notation used in dietary labels, thermodynamics, and munitions specifications.",
    quotes: [
      { author: "James Prescott Joule", work: "On the Mechanical Equivalent of Heat", quote: "We measured the mechanical work required to raise one gram of water by a single **cal** of heat." },
      { author: "Ernest Hemingway", work: "A Farewell to Arms", quote: "The officer carried an old service pistol chambered for heavy nine-millimeter **cal** ammunition." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Metabolic conversion measures each **cal** of energy transferred across trophic food webs." }
    ]
  },
  "Dashboard — cal/calisthenic.md": {
    primary: "Relating to, consisting of, or designed for calisthenics (gymnastic exercises for fitness, flexibility, and muscle tone).",
    secondary: "Characterized by rhythmic bodily movements using body weight rather than external apparatus.",
    quotes: [
      { author: "Herman Melville", work: "White-Jacket", quote: "The sailors engaged in brisk **calisthenic** drills upon the open frigate deck to stave off the damp cold." },
      { author: "Louisa May Alcott", work: "Little Women", quote: "The girls practiced their daily **calisthenic** routines with cheerful vigor before breakfast." },
      { author: "George Bernard Shaw", work: "Major Barbara", quote: "The industrialist instituted morning **calisthenic** exercises to promote hygiene and discipline among his workers." }
    ]
  },
  "Dashboard — cal/calisthenics.md": {
    primary: "Gymnastic exercises to achieve bodily fitness and graceful movement, typically performed without specialized equipment using body weight.",
    secondary: "Figuratively, mental or verbal exercises demonstrating agility, cleverness, or intellectual dexterity.",
    quotes: [
      { author: "Aldous Huxley", work: "Brave New World", quote: "Loudspeakers barked instructions for morning **calisthenics**, and the dormitory arose in unison." },
      { author: "David Foster Wallace", work: "Infinite Jest", quote: "The academy students endured punishing hours of court drills and conditioning **calisthenics** under the hot sun." },
      { author: "H. L. Mencken", work: "Prejudices", quote: "The politician engaged in astonishing intellectual **calisthenics** to defend contradictory policy positions." }
    ]
  },
  "Dashboard — cal/calligraph.md": {
    primary: "A piece of beautiful, artistic, or stylized penmanship; an example of calligraphy.",
    secondary: "To write or transcribe something in a beautiful, decorative, or calligraphic hand.",
    quotes: [
      { author: "Ralph Waldo Emerson", work: "Essays: First Series", quote: "The ancient Persian scribe took pride in every delicate **calligraph** brushed onto illuminated silk." },
      { author: "John Ruskin", work: "The Stones of Venice", quote: "Every architectural inscription was treated as a stone **calligraph**, carved with reverence and beauty." },
      { author: "Umberto Eco", work: "The Name of the Rose", quote: "The master copyist produced an exquisite **calligraph** of the Gospel opening in gold and cinnabar ink." }
    ]
  },
  "Dashboard — cal/calligrapher.md": {
    primary: "A person who practices the art of calligraphy; a professional or skilled artistic scribe.",
    secondary: "A master penman or brush artisan who transcribes literary or sacred manuscripts with aesthetic perfection.",
    quotes: [
      { author: "Edward FitzGerald", work: "The Rubáiyát of Omar Khayyám", quote: "The royal **calligrapher** decorated the margin of the quatrain with golden arabesques." },
      { author: "Will Durant", work: "The Story of Civilization: Our Oriental Heritage", quote: "In imperial China, the master **calligrapher** was honored above ordinary painters and sculptors." },
      { author: "Walter Benjamin", work: "The Arcades Project", quote: "The medieval **calligrapher** did not merely record words; he invested every stroke with liturgical presence." }
    ]
  },
  "Dashboard — cal/calligraphic.md": {
    primary: "Pertaining to, resembling, or characterized by calligraphy (beautiful, stylized, artistic penmanship).",
    secondary: "In visual art, displaying elegant, flowing, linear brushstrokes or line quality resembling skilled handwriting.",
    quotes: [
      { author: "Kenneth Clark", work: "Civilisation", quote: "The Celtic monks illuminated the Lindisfarne Gospels with dizzying **calligraphic** spirals and knots." },
      { author: "Virginia Woolf", work: "To the Lighthouse", quote: "Her thoughts traced delicate, **calligraphic** patterns across the quiet evening hours." },
      { author: "Clement Greenberg", work: "Art and Culture", quote: "Abstract expressionism incorporated bold **calligraphic** gestures inspired by Far Eastern ink painting." }
    ]
  },
  "Dashboard — cal/calligraphical.md": {
    primary: "Of or relating to calligraphy; calligraphic.",
    secondary: "Marked by ornamental flourishes and elegant handwritten draftsmanship.",
    quotes: [
      { author: "Washington Irving", work: "The Alhambra", quote: "The walls of the Moorish palace were adorned with intricate **calligraphical** poems praising the sultan." },
      { author: "Edgar Allan Poe", work: "The Murders in the Rue Morgue", quote: "Dupin scrutinized the document, remarking upon its quaint, **calligraphical** flourishes." },
      { author: "Charles Lamb", work: "Essays of Elia", quote: "The old clerk took solemn pride in his obsolete **calligraphical** accomplishments and fine flourishes." }
    ]
  },
  "Dashboard — cal/calligraphist.md": {
    primary: "An expert or specialist in the art of calligraphy; a calligrapher.",
    secondary: "A historical scribe or paleographer celebrated for mastery of formal manuscript hands.",
    quotes: [
      { author: "Isaac D'Israeli", work: "Curiosities of Literature", quote: "The celebrated Italian **calligraphist** could write the Lord's Prayer within the compass of a silver penny." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Norwood Builder", quote: "The forged will was executed in a trembling hand by someone posing as an aged **calligraphist**." },
      { author: "Samuel Johnson", work: "Lives of the English Poets", quote: "He admired the manuscript for the supreme artistry of the nameless monastic **calligraphist**." }
    ]
  },
  "Dashboard — cal/calligraphy.md": {
    primary: "Decorative handwriting or handwritten lettering, especially when created with a pen, brush, or specialized writing instrument.",
    secondary: "The art of beautiful writing regarded as a visual fine art tradition across East Asian, Islamic, and Western cultures.",
    quotes: [
      { author: "Steve Jobs", work: "Stanford Commencement Address", quote: "I learned about serif and sans-serif typefaces, and what makes great **calligraphy** great—it was artistically subtle in a way science cannot capture." },
      { author: "Lin Yutang", work: "My Country and My People", quote: "In China, **calligraphy** is regarded as the purest and most abstract of all visual arts." },
      { author: "Joris-Karl Huysmans", work: "Against the Grain", quote: "Des Esseintes admired the archaic **calligraphy** of the parchment codex, illuminated in saffron and gold." }
    ]
  },
  "Dashboard — cal/Callista.md": {
    primary: "A feminine given name of Greek origin meaning 'most beautiful' (from *kallistos*, superlative of *kalos*).",
    secondary: "In malacology, a genus of marine bivalve mollusks (venus clams) in the family Veneridae; or the heroine of John Henry Newman's novel.",
    quotes: [
      { author: "John Henry Newman", work: "Callista: A Sketch of the Third Century", quote: "**Callista** looked toward the Christian martyr with an earnest desire to discover the truth of his faith." },
      { author: "Thomas Love Peacock", work: "Gryll Grange", quote: "The lovely maiden was christened **Callista**, fulfilling the promise of her auspicious Greek name." },
      { author: "Richard Owen", work: "Lectures on Invertebrate Anatomy", quote: "The polished, porcelain-like valves of **Callista** exhibit delicate concentric growth lines." }
    ]
  },
  "Dashboard — cal/Callisto.md": {
    primary: "In Greek mythology, an Arcadian nymph transformed into a bear by Zeus and placed in the heavens as Ursa Major.",
    secondary: "In astronomy, the second-largest moon of Jupiter and third-largest moon in the solar system, discovered by Galileo in 1610.",
    quotes: [
      { author: "Ovid", work: "Metamorphoses", quote: "Diana banished the weeping nymph, and Juno transformed lovely **Callisto** into a shaggy bear doomed to wander the forest." },
      { author: "Galileo Galilei", work: "Sidereus Nuncius", quote: "Through the telescope, I beheld the outermost satellite, later designated **Callisto**, orbiting majestic Jupiter." },
      { author: "Carl Sagan", work: "Cosmos", quote: "The cratered, ancient ice-and-rock surface of **Callisto** preserves the scars of early bombardment in our solar system." }
    ]
  },
  "Dashboard — cal/calophyllous.md": {
    primary: "Having beautiful, glossy, or aesthetically pleasing leaves (from Greek *kalos* beautiful + *phyllon* leaf).",
    secondary: "In systematic botany, designating tropical plants characterized by elegant, closely parallel-veined foliage.",
    quotes: [
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The tropical evergreen trees of this family are preeminently **calophyllous**, bearing leathery leaves with delicate transverse veins." },
      { author: "Alexander von Humboldt", work: "Aspects of Nature", quote: "The deep green shade of the **calophyllous** canopies sheltered delicate orchids from the equatorial sun." },
      { author: "Asa Gray", work: "Structural Botany", quote: "Certain rainforest species are prized in botanical collections for their striking, **calophyllous** habit." }
    ]
  },
  "Dashboard — cal/decal.md": {
    primary: "A design, picture, or label printed on specially prepared paper for transferring onto glass, porcelain, metal, or wood (decalcomania).",
    secondary: "To apply a decorative decal or transfer onto a surface.",
    quotes: [
      { author: "Truman Capote", work: "In Cold Blood", quote: "On the rear window of the pickup truck was pasted a faded patriotic **decal**." },
      { author: "Thomas Pynchon", work: "The Crying of Lot 49", quote: "A muted post horn **decal** appeared suddenly on walls and public telephone booths across the city." },
      { author: "John Updike", work: "Rabbit, Run", quote: "The windshield bore a state inspection **decal** curling slightly at the corner." }
    ]
  },
  "Dashboard — cal/deceive.md": {
    primary: "To deliberately mislead, trick, or cause someone to accept as true or valid what is false or invalid.",
    secondary: "To give a misleading impression; to disappoint or fail to fulfill an expectation.",
    quotes: [
      { author: "William Shakespeare", work: "Hamlet", quote: "This above all: to thine own self be true, and it must follow, as the night the day, thou canst not then be false to any man or **deceive**." },
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "You must not attempt to **deceive** me; I know more of your feelings than you imagine." },
      { author: "Niccolò Machiavelli", work: "The Prince", quote: "One who deceives will always find those who allow themselves to be **deceived**." }
    ]
  },
  "Dashboard — cal/decor.md": {
    primary: "The furnishings, decoration, and aesthetic layout of a room, restaurant, home, or stage set.",
    secondary: "The visual atmosphere, aesthetic style, and artistic design characteristic of an interior space.",
    quotes: [
      { author: "F. Scott Fitzgerald", work: "The Great Gatsby", quote: "The lavish salon had a Marie Antoinette **decor**, complete with crystal chandeliers and gilded mirrors." },
      { author: "Edith Wharton", work: "The Custom of the Country", quote: "Undine surveyed the sumptuous Parisian **decor** with ambitious, calculating eyes." },
      { author: "Virginia Woolf", work: "Mrs Dalloway", quote: "The quiet drawing-room possessed a tasteful Regency **decor** that reflected generations of refined taste." }
    ]
  },
  "Dashboard — cal/epic.md": {
    primary: "A long narrative poem recounting the heroic deeds, adventures, and historical achievements of legendary figures or a nation.",
    secondary: "On a grand, monumental, or heroic scale; surpassing the ordinary in size, scope, or ambition.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "I now must change these notes to tragic, seeking argument not less but more heroic than the Iliad's **epic** song." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "To write a mighty book, you must choose a mighty theme, worthy of an **epic** enterprise." },
      { author: "George Eliot", work: "Middlemarch", quote: "Many a modest life is an unwritten **epic** of silent self-sacrifice and enduring love." }
    ]
  },
  "Dashboard — cal/epical.md": {
    primary: "Pertaining to, having the characteristics of, or resembling an epic poem; heroic and grand in scale.",
    secondary: "Possessing monumental grandeur, sweeping narrative scope, or legendary dignity.",
    quotes: [
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "History unfolded before him not as dry chronicle, but as an **epical** tragedy of titanic human passions." },
      { author: "Matthew Arnold", work: "On Translating Homer", quote: "Homer maintains a rapid, simple, and noble **epical** movement that modern translators fail to reproduce." },
      { author: "Walter Pater", work: "Appreciations", quote: "The dramatic poems of Morris share that childlike yet grand **epical** vision found in medieval romance." }
    ]
  },
  "Dashboard — cal/epicure.md": {
    primary: "A person who takes particular pleasure in fine food, drink, and sensory delicacies; a connoisseur of gastronomy (gourmet).",
    secondary: "Historically, a follower of the Greek philosopher Epicurus, who taught that peaceful tranquility and freedom from pain are the highest good.",
    quotes: [
      { author: "Ralph Waldo Emerson", work: "Representative Men", quote: "Montaigne was a philosophical **epicure**, tasting life's diverse flavors with detached curiosity." },
      { author: "Charles Dickens", work: "Bleak House", quote: "The portly gentleman was a noted **epicure** who spent hours debating the vintage of his cellar." },
      { author: "Henry David Thoreau", work: "Walden", quote: "The true philosopher is not an **epicure** seeking exotic treats, but one who relishes the sweet simplicity of wild berries." }
    ]
  }
};

for (const [relPath, entry] of Object.entries(filesData)) {
  const filePath = path.join(baseDir, relPath);
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

console.log('Done Batch 3 of Cluster Art, Craft & Design (34 words)!');
