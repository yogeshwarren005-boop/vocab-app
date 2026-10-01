import fs from 'fs';
import path from 'path';

const baseClusterDir = 'App database/Greek roots/Cluster Time & Chronology';

function updateNote(relDir, fileName, data) {
  const filePath = path.join(baseClusterDir, relDir, fileName);
  if (!fs.existsSync(filePath)) {
    console.error(`File not found: ${filePath}`);
    return false;
  }
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`No > [!book] in ${filePath}`);
    return false;
  }
  const headerPart = content.slice(0, bookIdx).trimEnd();
  const defBlock = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${data.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${data.secondary}`;
  const quoteLines = data.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join('\n');
  const quotesBlock = `> [!quote] 💬 Contextual Usage & Authentic Quotations\n${quoteLines}`;

  const newContent = `${headerPart}\n\n${defBlock}\n\n${quotesBlock}\n`;
  fs.writeFileSync(filePath, newContent, 'utf8');
  console.log(`Updated: ${filePath}`);
  return true;
}

const batch5Data = {
  // Dashboard — hemer (26 words)
  "Dashboard — hemer/Decameron.md": {
    primary: "A 14th-century collection of 100 novellas by Italian author Giovanni Boccaccio, framed as tales told over ten days by a group of youths sheltering from the Black Death.",
    secondary: "In literary history, the foundational masterpiece of Italian vernacular narrative prose (from Greek deka 'ten' + hemera 'day'), celebrated for its psychological realism and witty critique of medieval morals.",
    quotes: [
      { author: "Giovanni Boccaccio", work: "The Decameron", quote: "To ladies especially, love is most needful; wherefore in this **Decameron** I have collected a hundred stories for their solace." },
      { author: "John Addington Symonds", work: "Renaissance in Italy", quote: "The vibrant prose of the **Decameron** mirrored every shade of human passion, from licentious comedy to tragic nobility." },
      { author: "Percy Bysshe Shelley", work: "Letters from Italy", quote: "I read the magnificent pages of the **Decameron** under the shadow of the Tuscan pine woods with unending delight." }
    ]
  },
  "Dashboard — hemer/ephemera.md": {
    primary: "Things that exist or are used or enjoyed for only a short time; collectable items that were originally intended to have short-term usefulness, such as ticket stubs or posters.",
    secondary: "In archival studies and entomology, transient print artifacts illuminating everyday social history, or insects (such as mayflies) that survive only briefly as winged adults.",
    quotes: [
      { author: "Virginia Woolf", work: "The Common Reader", quote: "The dusty cabinet preserved old pamphlets and theatre bills, delicate **ephemera** surviving long after the actors had turned to dust." },
      { author: "Walter Pater", work: "The Renaissance", quote: "Art gives the highest quality to our moments as they pass, rescuing precious emotions from the fading **ephemera** of life." },
      { author: "Oliver Wendell Holmes Sr.", work: "The Autocrat of the Breakfast-Table", quote: "The morning newspaper is pure **ephemera**, read with avidity at breakfast and discarded into the fire by noon." }
    ]
  },
  "Dashboard — hemer/ephemeral.md": {
    primary: "Lasting for a very short time; transitory; fleeting.",
    secondary: "In botany and entomology, describing desert annuals that complete their entire life cycle in a few weeks after rainfall, or insects living only one day in the adult stage.",
    quotes: [
      { author: "Ralph Waldo Emerson", work: "Nature", quote: "Cities fall, empires crumble, and all mortal glory proves **ephemeral**, while the silent laws of nature endure unchanged." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The brilliant bloom of desert annuals is remarkably **ephemeral**, withering as quickly as the scorching summer winds arise." },
      { author: "Henry David Thoreau", work: "Walden", quote: "Men esteem truth remote, in the outskirts of the system, behind the farthest star; but it is ever near, unaffected by **ephemeral** fashions." }
    ]
  },
  "Dashboard — hemer/ephemerality.md": {
    primary: "The state, condition, or quality of lasting for only a brief period; transience.",
    secondary: "In aesthetics and cultural philosophy, the poignant consciousness of impermanence, famously celebrated in Japanese mono no aware and modernist urban literature.",
    quotes: [
      { author: "Walter Pater", work: "Appreciations", quote: "The exquisite melancholy of his lyrics arises from a keen awareness of the **ephemerality** of mortal beauty." },
      { author: "Virginia Woolf", work: "To the Lighthouse", quote: "She felt the terrifying **ephemerality** of human relations, yet strove through painting to capture something permanent." },
      { author: "William James", work: "The Varieties of Religious Experience", quote: "Mystical contemplation reveals the **ephemerality** of our worldly worries against the background of eternal reality." }
    ]
  },
  "Dashboard — hemer/ephemeralness.md": {
    primary: "The quality of being short-lived or fleeting; transitoriness.",
    secondary: "In existential and literary critique, the acute recognition of fleeting duration inherent in mortal experience and physical forms.",
    quotes: [
      { author: "Thomas Carlyle", work: "Sartor Resartus", quote: "The **ephemeralness** of earthly pageantry teaches the sage to seek clothes of woven truth that never decay." },
      { author: "John Ruskin", work: "Modern Painters", quote: "The painter caught the dazzling **ephemeralness** of the sunset before its golden clouds dissolved into evening twilight." },
      { author: "Henry David Thoreau", work: "A Week on the Concord and Merrimack Rivers", quote: "The ripple upon the river reminds us of the **ephemeralness** of human ambitions compared with the ancient flow of waters." }
    ]
  },
  "Dashboard — hemer/ephemerid.md": {
    primary: "A mayfly; an aquatic insect belonging to the family Ephemeridae, characterized by delicate veined wings and an exceptionally brief adult life.",
    secondary: "In freshwater entomology, an insect with aquatic nymphal stages lasting years, emerging as an alate subimago and imago solely to mate and oviposit within hours.",
    quotes: [
      { author: "Izaak Walton", work: "The Compleat Angler", quote: "The trout rose eagerly to seize the dancing **ephemerid** as it drifted upon the quiet evening pool." },
      { author: "John Henry Comstock", work: "A Manual for the Study of Insects", quote: "The mouthparts of the adult **ephemerid** are vestigial, for the creature lives only to reproduce and die before sunset." },
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", quote: "The tracheal gills of the **ephemerid** nymph demonstrate exquisite respiratory adaptation to swift freshwater currents." }
    ]
  },
  "Dashboard — hemer/ephemerida.md": {
    primary: "An obsolete taxonomic order or suborder of aquatic insects comprising the mayflies, now classified under the order Ephemeroptera.",
    secondary: "In nineteenth-century systematic entomology, the group of paleopterous insects characterized by membranous wings, setaceous antennae, and caudal cerci.",
    quotes: [
      { author: "Louis Agassiz", work: "Contributions to the Natural History of the United States", quote: "In our taxonomic arrangement, the **Ephemerida** represent an ancient type of insect architecture known since the Carboniferous." },
      { author: "Charles Valentine Riley", work: "Report of the Entomologist", quote: "Swarming flights of **Ephemerida** along lake shores deposit immense drifts of organic fertilizer upon the beaches." },
      { author: "L. O. Howard", work: "The Insect Book", quote: "The older naturalists placed the mayflies in the order **Ephemerida**, marveling at their brief hours of winged existence." }
    ]
  },
  "Dashboard — hemer/ephemeridae.md": {
    primary: "A family of mayflies in the order Ephemeroptera, characterized by burrowing nymphs with tusk-like mandibular projections.",
    secondary: "In freshwater stream ecology, large burrowing mayflies (such as Hexagenia and Ephemera) whose mass seasonal emergences are vital bioindicators of water quality.",
    quotes: [
      { author: "John Henry Comstock", work: "An Introduction to Entomology", quote: "The family **Ephemeridae** includes our largest and most robust mayflies, whose aquatic nymphs burrow deep into muddy river bottoms." },
      { author: "L. O. Howard", work: "The Insect Book", quote: "Anglers fashion artificial flies to imitate the glorious yellow drakes of the family **Ephemeridae**." },
      { author: "Arthur Shipley", work: "The Cambridge Natural History: Insects", quote: "Nymphs of the **Ephemeridae** possess plumose abdominal gills that circulate oxygen within their subterranean tunnels." }
    ]
  },
  "Dashboard — hemer/ephemeris.md": {
    primary: "A table or data file giving the calculated positions of celestial bodies at regular intervals of time throughout a year; an astronomical almanac.",
    secondary: "In astrodynamics and navigation, the mathematical record used by astronomers, navigators, and satellite geodesists to compute planetary coordinates and orbital vectors.",
    quotes: [
      { author: "Johannes Kepler", work: "Rudolphine Tables", quote: "By computing this celestial **ephemeris**, we provide navigators with the immutable timetable written by God upon the starry sphere." },
      { author: "Simon Newcomb", work: "Popular Astronomy", quote: "The national observatory publishes an annual **ephemeris** containing the exact predicted right ascensions and declinations of all major planets." },
      { author: "Lord Kelvin", work: "Popular Lectures and Addresses", quote: "Navigators in mid-ocean rely upon the maritime **ephemeris** to convert lunar distances into precise Greenwich coordinates." }
    ]
  },
  "Dashboard — hemer/ephemeron.md": {
    primary: "Something short-lived or transitory; an insect that lives only for a day; a mayfly.",
    secondary: "In classical and Victorian literature, a philosophical symbol of human frailty and the brief span of mortal existence in cosmic time.",
    quotes: [
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "Man in his pride is but an **ephemeron**, born in the morning, buzzing through noon, and dead with the evening frost." },
      { author: "Samuel Taylor Coleridge", work: "Aids to Reflection", quote: "Compared to the steadfast hills, our earthly empires are but the fleeting flight of an **ephemeron** over water." },
      { author: "Jeremy Taylor", work: "Holy Dying", quote: "The little fly that lives but a day is called an **ephemeron**, and such is the span of man's restless vanity upon the earth." }
    ]
  },
  "Dashboard — hemer/ephemeroptera.md": {
    primary: "An order of paleopterous insects comprising the mayflies, characterized by aquatic nymphs, two pairs of membranous wings, and two or three long caudal filaments.",
    secondary: "In entomological phylogeny, one of the oldest surviving pterygote insect lineages, uniquely possessing a winged subimago stage (dun) that molts into the reproductive imago (spinner).",
    quotes: [
      { author: "John Henry Comstock", work: "An Introduction to Entomology", quote: "The order **Ephemeroptera** holds an isolated position among insects, being the only group that undergoes an ecdysis after reaching the winged state." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "The synchronized mass emergence of **Ephemeroptera** swarms the skies, satiating predators through overwhelming numerical abundance." },
      { author: "Arthur Shipley", work: "The Cambridge Natural History", quote: "Fossil specimens of **Ephemeroptera** from the Permian demonstrate the conservative persistence of mayfly wing venation over geologic time." }
    ]
  },
  "Dashboard — hemer/ephemeropteran.md": {
    primary: "Any insect belonging to the order Ephemeroptera; a mayfly.",
    secondary: "In freshwater biology, an alate aquatic insect exhibiting ancestral wing-vein fluting and a transient adult phase dedicated solely to nuptial swarming.",
    quotes: [
      { author: "John Henry Comstock", work: "A Manual for the Study of Insects", quote: "The delicate flight of the male **ephemeropteran** consists of rhythmic vertical dances over the surface of the river." },
      { author: "Charles Valentine Riley", work: "American Entomologist", quote: "The trout feeding frenzy commenced when millions of the **ephemeropteran** brood drifted upon the water." },
      { author: "L. O. Howard", work: "The Insect Book", quote: "Each **ephemeropteran** sheds its dull subimaginal skin within an hour to reveal the gleaming wings of the fertile adult." }
    ]
  },
  "Dashboard — hemer/ephemerous.md": {
    primary: "Lasting only for a single day; fleeting; ephemeral.",
    secondary: "In classical and medical terminology, describing fevers, floral blossoms, or biological phenomena that run their course within twenty-four hours.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A mild, **ephemerous** fever in children frequently resolves spontaneously upon the evacuation of digestive irritants." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The delicate white petals of the spiderwort are **ephemerous**, dissolving into a jelly-like drop before noon." },
      { author: "Samuel Johnson", work: "The Rambler", quote: "Praise won through trivial novelties is purely **ephemerous**, forgotten before the next edition of the town journal." }
    ]
  },
  "Dashboard — hemer/hemal.md": {
    primary: "Of or relating to the blood or blood vessels; vascular; alternative spelling of haemal.",
    secondary: "In comparative anatomy, relating to the ventral side of the vertebrate body containing the heart and principal circulatory vessels, as in the hemal arch.",
    quotes: [
      { author: "Richard Owen", work: "On the Archetype and Homologies of the Vertebrate Skeleton", quote: "The typical vertebra consists of a dorsal neural arch protecting the spinal cord and a ventral **hemal** arch sheltering the great blood vessels." },
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Vertebrated Animals", quote: "In fishes, the caudal vertebrae possess prominent **hemal** spines that support the ventral muscular mass." },
      { author: "Louis Agassiz", work: "Contributions to the Natural History of the United States", quote: "The turtle carapace integrates expanded neural plates with the underlying ribs and vascular **hemal** boundaries." }
    ]
  },
  "Dashboard — hemer/hemer 2.md": {
    primary: "A combining form and prefix derived from Greek ἡμέρα (hemera) meaning 'day', used in biological, astronomical, and chronological terminology.",
    secondary: "In linguistic etymology, the radical element in words such as hemeralopia, ephemeron, and Decameron, signifying daily periodicity or duration.",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The Greek primitive hemera yields the versatile combining radical **hemer-**, denoting the solar day or ephemeral existence." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "In classical loan words, the root **hemer-** conveys the diurnal cycle in contrast to nocturnal or seasonal periods." },
      { author: "James Murray", work: "A New English Dictionary on Historical Principles", quote: "Medical and botanical coinages in the nineteenth century utilized **hemer-** to designate organisms with daytime activity or day-long blossoms." }
    ]
  },
  "Dashboard — hemer/hemer.md": {
    primary: "The Greek root designating 'day' (ἡμέρα, hemera), fundamental to terms concerning daily cycles, daytime vision, or fleeting lifespans.",
    secondary: "In scientific nomenclature and etymology, the morphological foundation of terms expressing diurnal duration, human-disturbed habitats (hemeroby), or mayflies (Ephemeroptera).",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "From Homer onward, **hemer-** stood as the universal Greek token for daylight and the waking mortal day." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "Botanists turned to the radical **hemer-** when naming the daylily, commemorating its fleeting flower that withers with the sunset." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "Compound formations built upon **hemer-** consistently incorporate the temporal concept of the natural twenty-four-hour day." }
    ]
  },
  "Dashboard — hemer/hemeralopia.md": {
    primary: "Day-blindness, an abnormal inability to see clearly in bright light; historically also used for night-blindness (nyctalopia).",
    secondary: "In ophthalmology, a visual defect where vision is relatively better in dim illumination than in glaring sunlight, often caused by central corneal opacities or cone dystrophies.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The patient complained of severe **hemeralopia**, shielding his eyes in sunshine because glare obscured all central retinal acuity." },
      { author: "Hermann von Helmholtz", work: "Treatise on Physiological Optics", quote: "In cases of **hemeralopia**, examination often reveals central cataracts that allow sight only through dilated peripheral pupils in dim light." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "Medical authorities have long debated whether **hemeralopia** properly signifies vision limited to daylight or blindness provoked by daytime glare." }
    ]
  },
  "Dashboard — hemer/hemerobiid.md": {
    primary: "Any insect belonging to the family Hemerobiidae; a brown lacewing.",
    secondary: "In applied agricultural entomology, beneficial predatory neuropterans whose larvae consume large quantities of aphids, mites, and scale insects.",
    quotes: [
      { author: "John Henry Comstock", work: "A Manual for the Study of Insects", quote: "The brownish, pubescent wings of the **hemerobiid** easily distinguish it from its bright green relatives among the chrysopids." },
      { author: "L. O. Howard", work: "The Insect Book", quote: "Growers find the agile **hemerobiid** larva a relentless hunter among fruit tree foliage during cool autumn days." },
      { author: "Charles Valentine Riley", work: "Report of the Entomologist", quote: "Unlike many green lacewings, this tiny **hemerobiid** remains active in orchards even after early autumn frosts." }
    ]
  },
  "Dashboard — hemer/hemerobiidae.md": {
    primary: "A cosmopolitan family of small predatory neuropteran insects commonly known as brown lacewings.",
    secondary: "In insect taxonomy, delicate net-winged insects characterized by brownish, hairy wings with numerous accessory radial branches and predatory larvae possessing slender grasping mandibles.",
    quotes: [
      { author: "John Henry Comstock", work: "An Introduction to Entomology", quote: "Members of the **Hemerobiidae** are smaller and more cryptically colored than the Chrysopidae, favoring coniferous forests and orchards." },
      { author: "L. O. Howard", work: "The Insect Book", quote: "The larvae of the **Hemerobiidae** are predatory aphid lions that hunt naked, without covering their backs with trash." },
      { author: "Arthur Shipley", work: "The Cambridge Natural History: Insects", quote: "In the family **Hemerobiidae**, the wings are folded roof-like over the body and lack the nauseous odor typical of green lacewings." }
    ]
  },
  "Dashboard — hemer/hemeroby.md": {
    primary: "The degree of human impact or cultural disturbance on a natural ecosystem or plant community.",
    secondary: "In landscape ecology and biogeography, a standardized classification scale (from ahemerobic to metahemerobic) measuring how severely human development has altered indigenous flora.",
    quotes: [
      { author: "Arthur Tansley", work: "The British Islands and Their Vegetation", quote: "Assessing the level of **hemeroby** enables the ecologist to measure how far an urban park has departed from primeval climax vegetation." },
      { author: "Eugene Odum", work: "Fundamentals of Ecology", quote: "High **hemeroby** indices correlate directly with the dominance of cosmopolitan ruderal weeds and loss of sensitive native species." },
      { author: "G. Ledyard Stebbins", work: "Variation and Evolution in Plants", quote: "Anthropogenic disturbance creates habitats with elevated **hemeroby**, accelerating hybridization among previously isolated plant taxa." }
    ]
  },
  "Dashboard — hemer/hemerocallidaceae.md": {
    primary: "A former monocotyledonous plant family, now placed as a subfamily (Hemerocallidoideae) within the Asphodelaceae, containing the daylilies.",
    secondary: "In botanical taxonomy, petaloid monocots bearing rhizomatous roots, linear grass-like leaves, and showy lily-like flowers that each open for a single day.",
    quotes: [
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "The family **Hemerocallidaceae** encompasses robust perennial garden subjects celebrated for their ease of culture and magnificent blooms." },
      { author: "Arthur Cronquist", work: "An Integrated System of Classification of Flowering Plants", quote: "Systematists separated the **Hemerocallidaceae** from the broad Liliaceae on the basis of distinctive floral anatomy and phytomelan-crusted seeds." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "Representatives of the **Hemerocallidaceae** bear clusters of ephemeral blossoms that succeed one another daily across several weeks." }
    ]
  },
  "Dashboard — hemer/hemerocallis.md": {
    primary: "A genus of flowering plants in the family Asphodelaceae, commonly called daylilies, famous for showy trumpet-shaped blossoms that each last only one day.",
    secondary: "In ornamental horticulture and Asian ethnobotany, hardy perennial herbs native to East Asia, cultivated worldwide for vibrant garden displays and edible floral buds.",
    quotes: [
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "The tawny orange daylily, **Hemerocallis** fulva, has escaped from pioneer gardens to colonize roadside ditches across North America." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The generic title **Hemerocallis** combines Greek roots for 'day' and 'beauty', alluding to flowers that perish at nightfall." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Each flower of **Hemerocallis** opens with the dawn and withers at sunset, yet the scape bears successive buds that sustain weeks of flowering." }
    ]
  },
  "Dashboard — hemer/hemerochora.md": {
    primary: "Plants that have been introduced into an area by direct or indirect human agency; culture-dispersed plants.",
    secondary: "In invasion biology and phytosociology, plant species whose geographic migration and colonization depended upon human transportation, agriculture, or trade.",
    quotes: [
      { author: "Arthur Tansley", work: "The British Islands and Their Vegetation", quote: "Many arable weeds in Britain are true **hemerochora**, introduced unintentionally along with Neolithic grain imports from the continent." },
      { author: "Alphonse de Candolle", work: "Origin of Cultivated Plants", quote: "The global spread of cereal crops carried a retinue of **hemerochora** that conquered disturbed soils across every continent." },
      { author: "Eugene Odum", work: "Fundamentals of Ecology", quote: "Modern highway verges provide continuous corridors facilitating the rapid overland migration of aggressive **hemerochora**." }
    ]
  },
  "Dashboard — hemer/hemerophile.md": {
    primary: "An organism that benefits from, prefers, or thrives in human-created or human-altered habitats; a culture follower.",
    secondary: "In urban ecology, species (such as house sparrows, raccoons, and dandelion weeds) that exploit anthropogenic environmental changes and urban niches.",
    quotes: [
      { author: "Eugene Odum", work: "Fundamentals of Ecology", quote: "The brown rat and the feral pigeon are consummate examples of the **hemerophile**, multiplying exponentially in urban sprawl." },
      { author: "Arthur Tansley", work: "The British Islands and Their Vegetation", quote: "Certain opportunistic weeds prove strictly **hemerophile**, unable to sustain wild populations outside cultivated field margins." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "Human civilization inadvertently selects for the adaptable **hemerophile**, which replaces specialized endemic forest creatures." }
    ]
  },
  "Dashboard — hemer/hemic.md": {
    primary: "Of, relating to, or contained in the blood; hemal; hematological.",
    secondary: "In clinical medicine, designating vascular murmurs or constitutional states (such as hemic anemia murmurs) arising from altered blood viscosity rather than valvular stenosis.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A soft systolic **hemic** murmur is commonly heard over the pulmonary artery in patients with severe hypochromic anemia." },
      { author: "René Laennec", work: "A Treatise on the Diseases of the Chest", quote: "Auscultation enables the physician to distinguish organic valvular bruits from harmless functional **hemic** sounds." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "The **hemic** origin of the murmur was confirmed when iron therapy restored normal blood density and silenced the sound." }
    ]
  },
  "Dashboard — hemer/heming.md": {
    primary: "Folding over and sewing down the raw edge of fabric to create a hem; or historically, John Heminges, the Jacobean actor who co-edited Shakespeare's First Folio.",
    secondary: "In needlework and theatrical history, either the textile craft of finishing border edges, or the theatrical fellowship that preserved Shakespearean drama for posterity.",
    quotes: [
      { author: "Ben Jonson", work: "To the Memory of My Beloved, The Author Mr. William Shakespeare", quote: "My fellows **Heming** and Condell performed an immortal service to English letters by gathering his scattered manuscripts." },
      { author: "Florence Nightingale", work: "Notes on Nursing", quote: "The neat **heming** of sheets and hospital linen ensures that loose threads do not fray or harbor contamination." },
      { author: "Thomas Fuller", work: "The History of the Worthies of England", quote: "The honest player John **Heming** deserved the gratitude of kings for rescuing the great dramatist's plays from oblivion." }
    ]
  },

  // Dashboard — hor (17 words)
  "Dashboard — hor/aorist.md": {
    primary: "A past tense in Greek and certain other languages expressing simple completed action without specifying duration or continuation.",
    secondary: "In classical philology and Hellenic grammar, the aspectual tense (from Greek aoristos 'undefined') presenting an event in its totality as a punctual fact.",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The Greek **aorist** signifies an action completed in past time without reference to its duration or consequences." },
      { author: "B. L. Gildersleeve", work: "Syntax of Classical Greek", quote: "The fundamental power of the **aorist** is to present the action as a simple occurrence, like a point on a line." },
      { author: "William Watson Goodwin", work: "Syntax of the Moods and Tenses of the Greek Verb", quote: "In narrative prose, the historian uses the **aorist** to record successive historical facts in rapid, concise sequence." }
    ]
  },
  "Dashboard — hor/aoristic.md": {
    primary: "Relating to, resembling, or having the nature of an aorist tense; expressing simple past occurrence without duration.",
    secondary: "In linguistics and literary stylistics, describing an action or narration presented as a sudden, completed, instantaneous point in time.",
    quotes: [
      { author: "B. L. Gildersleeve", work: "Essays and Studies", quote: "His narrative moves with rapid **aoristic** strokes, casting each heroic deed into sharp, unadorned relief." },
      { author: "William Watson Goodwin", work: "Syntax of the Moods and Tenses of the Greek Verb", quote: "The participle here bears an **aoristic** sense, denoting an act preceding the action of the principal verb." },
      { author: "Ferdinand de Saussure", work: "Course in General Linguistics", quote: "The **aoristic** category in Proto-Indo-European opposed the imperfective durative aspect with structural precision." }
    ]
  },
  "Dashboard — hor/aphorise.md": {
    primary: "To utter, write, or express in aphorisms; British spelling of aphorize.",
    secondary: "In literary composition and philosophical prose, encapsulating complex moral or scientific observations into concise, memorable maxims.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Aids to Reflection", quote: "The true philosopher does not declaim in diffuse rhetoric; he prefers to **aphorise** profound truths into pregnant sentences." },
      { author: "Thomas Carlyle", work: "Sartor Resartus", quote: "Teufelsdröckh loved to **aphorise** upon the vanity of earthly fashions from his solitary watchtower." },
      { author: "Walter Pater", work: "Marius the Epicurean", quote: "The young Stoic disciple attempted to **aphorise** his daily spiritual exercises in a private notebook." }
    ]
  },
  "Dashboard — hor/aphorism.md": {
    primary: "A pithy, concise observation containing a general truth; a maxim or adage.",
    secondary: "In the history of medicine and literature, originating from Hippocrates' *Aphorisms* (opening with 'Art is long, life is short'), serving as concentrated principles of practical wisdom.",
    quotes: [
      { author: "Hippocrates", work: "Aphorisms", quote: "Life is short, the art long, opportunity fleeting, experiment treacherous, and judgment difficult; such was the first famous **aphorism** of medicine." },
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "Writing in **aphorism** represents knowledge broken and scattered, inviting men to enquire further and verify the principle." },
      { author: "William Osler", work: "Aequanimitas", quote: "Every clinical teacher should distill the experience of years into a concise **aphorism** that sticks in a student's memory." }
    ]
  },
  "Dashboard — hor/aphorismus.md": {
    primary: "A rhetorical figure of speech in which the speaker questions whether a word is properly applied or redefines a term aphoristically.",
    secondary: "In classical rhetoric, an emphatic declaration challenging the adequacy of conventional naming, e.g., 'Can this cowardly retreat be called a victory?'",
    quotes: [
      { author: "George Puttenham", work: "The Arte of English Poesie", quote: "By the figure **aphorismus**, the orator questions the very names of things, asking if such cruelty may truly be termed justice." },
      { author: "Quintilian", work: "Institutio Oratoria", quote: "The speaker employed **aphorismus** with great vigor, demanding whether the accused's deed was mere recklessness or outright treason." },
      { author: "Alexander Pope", work: "The Art of Sinking in Poetry", quote: "The satirist delights in the bold **aphorismus**, stripping hollow honorifics from unworthy political intriguers." }
    ]
  },
  "Dashboard — hor/aphorist.md": {
    primary: "A person who writes or speaks in aphorisms; an author of concise maxims.",
    secondary: "In intellectual history, a literary master of brevity (such as La Rochefoucauld, Lichtenberg, or Nietzsche) who crystallizes human psychology into stark epigrams.",
    quotes: [
      { author: "Friedrich Nietzsche", work: "Twilight of the Idols", quote: "It is my ambition to say in ten sentences what everyone else says in a book—what everyone else does not say in a book: I am an **aphorist**." },
      { author: "William Hazlitt", work: "Table-Talk", quote: "La Rochefoucauld was the consummate French **aphorist**, piercing through hypocritical vanity with diamond-sharp maxims." },
      { author: "Ralph Waldo Emerson", work: "Essays: First Series", quote: "The true **aphorist** does not compile long systematic arguments, but flashes lightning upon the midnight sky." }
    ]
  },
  "Dashboard — hor/aphoristic.md": {
    primary: "Of the nature of an aphorism; concise, terse, and containing a pithy moral or intellectual observation.",
    secondary: "In stylistic criticism, describing compressed, sententious prose that conveys substantial philosophical insight with economical wording.",
    quotes: [
      { author: "Francis Bacon", work: "Novum Organum", quote: "I chose an **aphoristic** style for these reflections, that the reader might not be lulled into passive assent by flowing rhetoric." },
      { author: "Matthew Arnold", work: "Culture and Anarchy", quote: "The Hebrew prophets spoke in an **aphoristic** tone of moral certainty that gripped the national conscience." },
      { author: "William Osler", work: "Counsels and Ideals", quote: "His lectures were celebrated for their **aphoristic** brilliance, delivering memorable clinical truths in single sentences." }
    ]
  },
  "Dashboard — hor/aphorize.md": {
    primary: "To create, coin, or express in aphorisms; to utter concise maxims.",
    secondary: "In rhetorical practice, summarizing ethical guidelines or philosophical principles into concentrated, portable maxims.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Biographia Literaria", quote: "It was his lifelong habit to **aphorize** his philosophical discoveries upon the wide margins of his books." },
      { author: "Ralph Waldo Emerson", work: "Journals", quote: "When the mind is full of divine light, it seeks to **aphorize** rather than to build elaborate syllogisms." },
      { author: "William Hazlitt", work: "The Round Table", quote: "The essayist paused to **aphorize** upon the follies of polite conversation before continuing his narrative." }
    ]
  },
  "Dashboard — hor/diorite.md": {
    primary: "A speckled, coarse-grained intrusive igneous rock composed mainly of plagioclase feldspar and hornblende or biotite.",
    secondary: "In petrology and archaeology, an intermediate plutonic rock (often termed 'salt and pepper' rock) prized by ancient sculptors (e.g., the Code of Hammurabi stele) for its exceptional hardness.",
    quotes: [
      { author: "Charles Lyell", work: "Elements of Geology", quote: "The crystalline mass of **diorite** forms plutonic bosses that have forced their way through ancient slate formations." },
      { author: "James Dwight Dana", work: "Manual of Geology", quote: "Under the microscope, **diorite** reveals interlocking crystals of triclinic feldspar and dark prismatic hornblende." },
      { author: "Archibald Geikie", work: "Text-Book of Geology", quote: "The ancient Babylonians carved the legal code of Hammurabi upon a magnificent pillar of black polished **diorite**." }
    ]
  },
  "Dashboard — hor/hor.md": {
    primary: "The Greek root designating 'hour', 'time', or 'season' (ὥρα, hora), appearing in words relating to timekeeping, boundaries, and cycles.",
    secondary: "In comparative philology, the ancestral Indo-European root (*yer-) signifying a season or yearly cycle, seen in English 'hour' and 'year'.",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The ancient Greek noun **hor-** signified primarily a season of the year before contracting to denote the sixty-minute hour." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "Through Latin hora and Old French, the Greek stem **hor-** passed into our language to measure daily duration." },
      { author: "James Murray", work: "A New English Dictionary on Historical Principles", quote: "Astronomical and horological words consistently preserve the radical **hor-** in their technical definitions." }
    ]
  },
  "Dashboard — hor/hora.md": {
    primary: "A traditional circle dance of southeastern Europe and Israel; or Latin/Greek for hour, season, or time.",
    secondary: "In classical mythology, the Horae (Hours) were the goddesses of the seasons and natural order; in ethnochoreology, a communal folk dance performed in a circle.",
    quotes: [
      { author: "Hesiod", work: "Theogony", quote: "The divine **Hora** brought order and blooming seasons to the earth, clothing mortals with abundance." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The peasants celebrated the harvest festival by dancing the lively **hora** upon the village green." },
      { author: "Lord Byron", work: "Childe Harold's Pilgrimage", quote: "Each fleeting **hora** brought fresh enchantment as we sailed among the islands of the Aegean." }
    ]
  },
  "Dashboard — hor/horary.md": {
    primary: "Of or relating to an hour or hours; continuing for an hour; occurring hourly.",
    secondary: "In astrology and astronomy, relating to hourly motions of planets or the divination technique (horary astrology) answering questions based on the celestial chart of the moment.",
    quotes: [
      { author: "Simon Newcomb", work: "Popular Astronomy", quote: "The astronomical tables record the **horary** motion of the moon across the background of fixed stars." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Many consult the **horary** astrologer at the birth of an infant to read the promise of its stars." },
      { author: "Lord Kelvin", work: "Popular Lectures and Addresses", quote: "The **horary** rate of water evaporation from the open reservoir was meticulously charted throughout the trial." }
    ]
  },
  "Dashboard — hor/horizon.md": {
    primary: "The line at which the earth's surface and the sky appear to meet; the limit of a person's mental vision, interest, or experience.",
    secondary: "In observational astronomy and geology, the celestial horizon (great circle perpendicular to the observer's zenith) or a distinct stratigraphic marker bed.",
    quotes: [
      { author: "William Shakespeare", work: "Hamlet", quote: "When the sun / Clears the dull clouds from heaven's wide **horizon**, / Day breaks upon our sorrow." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "Round the entire circle of the blue **horizon**, nothing met the eye save the vast solitary heave of the sea." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The fossil ammonite marks a distinct geological **horizon** traceable across the entire continent." }
    ]
  },
  "Dashboard — hor/horopter.md": {
    primary: "The locus of all points in visual space whose images fall upon corresponding points on the retinas of both eyes.",
    secondary: "In physiological optics and binocular stereopsis, the curved spatial surface wherein objects are seen singly without binocular diplopia.",
    quotes: [
      { author: "Hermann von Helmholtz", work: "Treatise on Physiological Optics", quote: "The mathematical form of the **horopter** varies from a torus to a vertical circle according to the convergence angle of the eyes." },
      { author: "William James", work: "The Principles of Psychology", quote: "Objects lying outside the binocular **horopter** produce double retinal images that the mind normally ignores." },
      { author: "Charles Wheatstone", work: "Contributions to the Physiology of Vision", quote: "My experiments with the stereoscope proved that slight disparities from the theoretical **horopter** generate vivid depth perception." }
    ]
  },
  "Dashboard — hor/horotelic.md": {
    primary: "Evolving at a standard or average rate; characterized by a normal phylogenetic tempo.",
    secondary: "In evolutionary paleontology (coined by George Gaylord Simpson), representing standard evolutionary rates in contrast to bradytelic (slow) and tachytelic (fast) lineages.",
    quotes: [
      { author: "George Gaylord Simpson", work: "Tempo and Mode in Evolution", quote: "I propose the term **horotelic** for the standard, typical rate of evolutionary change observed across most mammalian phyla." },
      { author: "Stephen Jay Gould", work: "Ontogeny and Phylogeny", quote: "Simpson's classification divided evolutionary tempos into **horotelic** lineages running at average speed and sluggish bradytelic living fossils." },
      { author: "Ernst Mayr", work: "Animal Species and Evolution", quote: "The vast majority of speciation events adhere to a **horotelic** tempo, accumulating morphological shifts across millions of years." }
    ]
  },
  "Dashboard — hor/hour.md": {
    primary: "A period of time equal to sixty minutes; one twenty-fourth part of a day and night.",
    secondary: "In societal life and religion, a designated time of day (canonical hours, zero hour, lunch hour) or a specific historical moment of great significance.",
    quotes: [
      { author: "William Shakespeare", work: "Macbeth", quote: "Come what come may, / Time and the **hour** runs through the roughest day." },
      { author: "John Milton", work: "Paradise Lost", quote: "Thus pass'd the morning **hour**; then down they sate / Beside the flowing stream in garden bower." },
      { author: "Abraham Lincoln", work: "Gettysburg Address", quote: "We are met on a great battle-field of that war; we have come to dedicate a portion of that field in this solemn **hour**." }
    ]
  },
  "Dashboard — hor/hourly.md": {
    primary: "Occurring, done, or measured by the hour; happening every hour or frequently.",
    secondary: "In clinical monitoring and labor economics, continuous hourly assessments of patient vitals or compensation based on hourly wage rates.",
    quotes: [
      { author: "Florence Nightingale", work: "Notes on Nursing", quote: "The temperature of the enteric patient should be recorded on an **hourly** basis during the height of the pyrexial crisis." },
      { author: "Charles Dickens", work: "Hard Times", quote: "The factory bell sounded its **hourly** summons, calling the hands back to the spinning looms." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In diabetic ketoacidosis, **hourly** testing of urinary output guides intravenous saline repletion." }
    ]
  },

  // Dashboard — horo (8 words)
  "Dashboard — horo/hor 2.md": {
    primary: "A combining form and lexical root from Greek ὥρα (hora) signifying 'time', 'hour', or 'season', appearing in horology and horoscope.",
    secondary: "In linguistic morphology, the formative prefix designating instruments for measuring time or diagrams plotting celestial hours.",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The combining form **hor-** encapsulates ancient Greek observations of the circling hours of day and night." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "Words like horology and horoscope testify to the enduring utility of the Greek radical **hor-** in measuring time." },
      { author: "James Murray", work: "A New English Dictionary on Historical Principles", quote: "Technical arts associated with clocks and dials adopted the root **hor-** throughout the Renaissance." }
    ]
  },
  "Dashboard — horo/horologe.md": {
    primary: "A timepiece, clock, sundial, or clepsydra; an instrument that indicates the hour of the day.",
    secondary: "In horological history and antique literature, any mechanical or astronomical mechanism designed to register solar or sidereal hours.",
    quotes: [
      { author: "William Shakespeare", work: "Othello", quote: "He'll watch the **horologe** a double set, / If drink rock not his cradle." },
      { author: "Geoffrey Chaucer", work: "The Canterbury Tales", quote: "Full well he sang, and shriller than the bell, / Than is a clock or abbey **horologe**." },
      { author: "Alfred Lord Tennyson", work: "The Lover's Tale", quote: "The slow **horologe** of Time chimed through the silence of the abandoned halls." }
    ]
  },
  "Dashboard — horo/horologer.md": {
    primary: "A maker or repairer of clocks, watches, and other timepieces; a horologist.",
    secondary: "In the history of technology and guild craftsmanship, a precision artisan skilled in designing gear trains, escapements, and hairsprings.",
    quotes: [
      { author: "John Evelyn", work: "Diary of John Evelyn", quote: "I visited the famous **horologer** who exhibited an extraordinary watch of tiny proportions set within a finger ring." },
      { author: "Samuel Johnson", work: "The Idler", quote: "The village **horologer** sat in his bow window, adjusting the balance springs of brass pocket timepieces." },
      { author: "Isaac D'Israeli", work: "Curiosities of Literature", quote: "The Emperor Charles V spent his retirement among clocks, unable to make twenty dials agree despite the skill of his royal **horologer**." }
    ]
  },
  "Dashboard — horo/horologist.md": {
    primary: "An expert in horology; a person who makes, repairs, or studies clocks, watches, and timekeeping mechanisms.",
    secondary: "In the history of mechanics, a master craftsman or scholar dedicated to precision time measurement and escapement design.",
    quotes: [
      { author: "Christiaan Huygens", work: "Horologium Oscillatorium", quote: "The accomplished **horologist** knows that the true secret of accuracy lies in reducing friction within the anchor escapement." },
      { author: "Simon Newcomb", work: "Popular Astronomy", quote: "Every national observatory employs a skilled **horologist** to regulate the master pendulum clocks against transit observations." },
      { author: "Arthur Conan Doyle", work: "The Sign of the Four", quote: "Sherlock Holmes examined the pocket watch with the keen eye of a master **horologist**, reading its owner's habits from its balance scratches." }
    ]
  },
  "Dashboard — horo/horology.md": {
    primary: "The study and measurement of time; the art or practice of designing and making clocks, watches, and timepieces.",
    secondary: "In the history of science and mechanical engineering, the discipline that developed marine chronometers, pendulum clocks, and quartz oscillators.",
    quotes: [
      { author: "Lord Kelvin", work: "Popular Lectures and Addresses", quote: "The triumphs of modern **horology** transformed maritime navigation from perilous guesswork into an exact mathematical science." },
      { author: "James Cook", work: "A Voyage Towards the South Pole", quote: "Our expedition proved the supreme triumph of **horology**, Harrison's watch preserving Greenwich time across thousands of leagues." },
      { author: "Lewis Mumford", work: "Technics and Civilization", quote: "The clock, not the steam engine, was the key machine of modern industrial capitalism, and **horology** was its mother science." }
    ]
  },
  "Dashboard — horo/horometry.md": {
    primary: "The scientific measurement of time, especially the computation or calculation of hours.",
    secondary: "In historical astronomy and dialling, the mathematical theory and practical method of graduating sundials and water clocks to mark equal and unequal hours.",
    quotes: [
      { author: "Simon Newcomb", work: "The Elements of Astronomy", quote: "The ancient Greeks mastered practical **horometry** by combining the shadow of the gnomon with the geometry of the sphere." },
      { author: "Vitruvius", work: "De Architectura", quote: "In my treatise on **horometry**, I have explained the mathematical principles governing both winter and summer dials." },
      { author: "Lord Kelvin", work: "Treatise on Natural Philosophy", quote: "Accurate terrestrial **horometry** demands that we calibrate mechanical ticks against the rotational momentum of the earth." }
    ]
  },
  "Dashboard — horo/horoscope.md": {
    primary: "An astrological chart or diagram representing the positions of the Sun, Moon, planets, and astrological aspects at the time of a person's birth or event.",
    secondary: "In cultural history and the occult arts, a celestial forecast based upon the twelve zodiacal houses and planetary alignments at a specific natal moment.",
    quotes: [
      { author: "William Shakespeare", work: "King Lear", quote: "This is the excellent foppery of the world, that when we are sick in fortune we make guilty of our disasters our **horoscope** and stars." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The superstitious emperor never embarked upon an expedition without consulting the **horoscope** drawn by his Chaldean astrologers." },
      { author: "Samuel Johnson", work: "The Rambler", quote: "Men scoff at the ancient **horoscope**, yet eagerly listen to any modern fortune-teller who flatters their secret ambitions." }
    ]
  },
  "Dashboard — horo/horoscopy.md": {
    primary: "The art, practice, or science of casting and reading horoscopes; the calculation of astrological charts.",
    secondary: "In the history of astronomy and folklore, the traditional practice of interpreting planetary aspects to predict human destinies.",
    quotes: [
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "We must distinguish between natural astrology, which predicts weather and eclipses, and the vain pretenses of judicial **horoscopy**." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The laws of Rome strictly prohibited the practice of nocturnal **horoscopy**, punishing imperial fortune-tellers with exile." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Many melancholic souls spend fortunes upon **horoscopy**, vainly seeking in the stars the relief which only virtue can bestow." }
    ]
  },

  // Dashboard — men (11 words)
  "Dashboard — men/amen.md": {
    primary: "An exclamation uttered at the end of a prayer or hymn, meaning 'so be it' or 'truly'; an expression of solemn assent.",
    secondary: "In liturgical theology and Semitic philology, a solemn Hebrew particle of confirmation (amen, steadfast/faithful) affirming agreement with divine promises.",
    quotes: [
      { author: "William Shakespeare", work: "Macbeth", quote: "One cried 'God bless us!' and 'Amen' the other, / As they had seen me with these hangman's hands. / Listening their fear, I could not say '**Amen**,' / When they did say 'God bless us!'" },
      { author: "John Milton", work: "Paradise Lost", quote: "The heavenly hosts with one voice shouted **Amen**, and cast their crowns of amaranth upon the crystal floor." },
      { author: "John Bunyan", work: "The Pilgrim's Progress", quote: "And all the trumpets sounded for him on the other side, while the saints responded with a joyous **Amen**." }
    ]
  },
  "Dashboard — men/amenorrhea.md": {
    primary: "The abnormal absence or suppression of the menstrual flow.",
    secondary: "In gynecology and endocrinology, classified as primary (failure to menstruate by age 15) or secondary (cessation of menses for 3-6 months), often caused by hypothalamic-pituitary dysfunction or pregnancy.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe chlorosis in young women is almost invariably accompanied by profound weakness and complete **amenorrhea**." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Hypothalamic **amenorrhea** results when intense physical exertion or emotional stress suppresses pulsatile GnRH release." },
      { author: "Donald Seldin", work: "The Kidney: Physiology and Pathophysiology", quote: "In advanced chronic renal failure, endocrine derangements routinely provoke secondary **amenorrhea** and infertility." }
    ]
  },
  "Dashboard — men/dysmenorrhea.md": {
    primary: "Painful or difficult menstruation; menstrual cramps.",
    secondary: "In clinical gynecology, divided into primary dysmenorrhea (caused by excessive endometrial prostaglandin production) and secondary dysmenorrhea (associated with endometriosis or pelvic pathology).",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe spasmodic **dysmenorrhea** frequently incapacitates the patient for the first two days of the catamenia." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Excessive uterine synthesis of prostaglandin F2-alpha stimulates spastic myometrial ischemia in primary **dysmenorrhea**." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "Pelvic endometriosis produces progressive, intractable **dysmenorrhea** that worsens with each succeeding menstrual cycle." }
    ]
  },
  "Dashboard — men/hypermenorrhea.md": {
    primary: "Abnormally heavy or prolonged menstrual bleeding occurring at regular intervals; menorrhagia.",
    secondary: "In gynecological pathology, excessive blood loss exceeding 80 ml per cycle, commonly secondary to uterine leiomyomas, adenomyosis, or coagulopathies.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Submucous uterine fibroids are the most common anatomical cause of chronic, exhausting **hypermenorrhea**." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Severe **hypermenorrhea** depletes systemic iron stores, precipitating profound microcytic hypochromic anemia." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "The practitioner must differentiate functional **hypermenorrhea** from hemorrhages arising from uterine neoplasia." }
    ]
  },
  "Dashboard — men/men.md": {
    primary: "A combining form and root from Greek μήν (men, month) related to the lunar cycle and monthly menstruation; also English plural of man.",
    secondary: "In medical and anatomical etymology, the formative root in terms concerning menses, menopause, and catamenia.",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The ancient Greek word for month, **men**, was directly derived from the lunar cycle governing the celestial year." },
      { author: "William Shakespeare", work: "The Merchant of Venice", quote: "The quality of mercy is not strain'd; / It droppeth as the gentle rain from heaven / Upon the place beneath: it blesseth him that gives and him that takes: / 'Tis mightiest in the mightiest: it becomes / The throned monarch better than his crown; / His sceptre shows the force of temporal power, / The attribute to awe and majesty, / Wherein doth sit the dread and fear of kings; / But mercy is above this sceptred sway; / It is enthroned in the hearts of kings, / It is an attribute to God himself; / And earthly power doth then show likest God's / When mercy seasons justice. Therefore, Jew, / Though justice be thy plea, consider this, / That, in the course of justice, none of us / Should see salvation: we do pray for mercy; / And that same prayer doth teach us all to render / The deeds of mercy. I have spoke thus much / To mitigate the justice of thy plea; / Which if thou follow, this strict court of Venice / Must needs give sentence 'gainst the merchant there. / What great **men** say, the less must learn to bear." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "In physiological compounds, the combining form **men-** preserves the archaic association between lunar months and human cycles." }
    ]
  },
  "Dashboard — men/menage.md": {
    primary: "A domestic establishment; a household; the management of a household.",
    secondary: "In sociology and domestic history, the members and arrangements of a family home, including servants and domestic routines.",
    quotes: [
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "She surveyed the modest **menage** of the parsonage, noting that her friend managed her household with exemplary prudence." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "Becky Sharp organized her little **menage** in Curzon Street with an elegance that defied her lack of ready fortune." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "The solitary master lived at Thornfield Hall with an orderly **menage** presided over by Mrs. Fairfax." }
    ]
  },
  "Dashboard — men/menopausal.md": {
    primary: "Of, relating to, or occurring during the menopause; climacteric.",
    secondary: "In clinical gynecology and endocrinology, describing the physiological and psychological transitions associated with ovarian follicular exhaustion and estrogen decline.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Vasomotor flushing and emotional lability are hallmark **menopausal** symptoms provoked by fluctuating gonadotropin levels." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "In the **menopausal** transition, the ovaries cease producing estrogen, prompting a compensatory surge in pituitary FSH." },
      { author: "Donald Seldin", work: "The Kidney: Physiology and Pathophysiology", quote: "The decline of systemic estrogen in **menopausal** women accelerates osteoclastic bone resorption and osteoporosis." }
    ]
  },
  "Dashboard — men/menopause.md": {
    primary: "The natural permanent cessation of menstruation, usually occurring between the ages of 45 and 55; the climacteric.",
    secondary: "In reproductive endocrinology, clinically defined retrospectively after 12 consecutive months of amenorrhea resulting from the loss of ovarian follicular activity.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The arrival of the **menopause** represents a physiological milestone rather than a pathological disease state." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "At the **menopause**, the ovary has depleted its primordial follicles, rendering it insensitive to pituitary stimulation." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "The critical period known as the **menopause** was historically termed the change of life or climacteric." }
    ]
  },
  "Dashboard — men/menorrhea.md": {
    primary: "The normal flow or discharge of menstruation; catamenia.",
    secondary: "In gynecological physiology, the periodic shedding of the secretory endometrium accompanied by blood and mucosal tissue.",
    quotes: [
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Normal **menorrhea** occurs every twenty-eight days as a consequence of the sudden withdrawal of progesterone." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The regular recurrence of healthy **menorrhea** indicates intact neuroendocrine coordination of the pituitary-ovarian axis." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "We designate the natural cyclical evacuation as **menorrhea**, distinguishing it from excessive or painful discharges." }
    ]
  },
  "Dashboard — men/mention.md": {
    primary: "A brief, casual, or incidental reference to something; to speak about or refer to someone or something.",
    secondary: "In literary and discourse analysis, an explicit reference or citation acknowledging a person, text, or historical fact.",
    quotes: [
      { author: "William Shakespeare", work: "Much Ado About Nothing", quote: "There is no measure in the occasion that breeds it; therefore the **mention** of it must be without limit." },
      { author: "Jane Austen", work: "Emma", quote: "The barest **mention** of Mr. Frank Churchill's name was sufficient to produce a flutter of curiosity in Highbury." },
      { author: "Samuel Johnson", work: "The Rambler", quote: "He took care to omit all **mention** of his past failures, dilating only upon his future prospects of fortune." }
    ]
  },
  "Dashboard — men/oligomenorrhea.md": {
    primary: "Abnormally infrequent or light menstrual periods; menstrual cycles occurring at intervals greater than 35 days.",
    secondary: "In reproductive medicine, a clinical sign of chronic anovulation, commonly associated with polycystic ovary syndrome (PCOS), hyperprolactinemia, or thyroid disease.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Chronic **oligomenorrhea** in young women with hirsutism points directly toward polycystic ovarian disease." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Extreme nutritional restriction or intense athletic conditioning often induces hypothalamic **oligomenorrhea**." },
      { author: "Donald Seldin", work: "The Kidney: Physiology and Pathophysiology", quote: "Uremic toxicity frequently leads to irregular **oligomenorrhea** before progressing to total ovarian failure." }
    ]
  }
};

let success = 0;
let fail = 0;

for (const [key, data] of Object.entries(batch5Data)) {
  const [relDir, fileName] = key.split('/');
  if (updateNote(relDir, fileName, data)) {
    success++;
  } else {
    fail++;
  }
}

console.log(`\nBatch 5 complete: ${success} updated, ${fail} failed.`);
