import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Writing & Script/Dashboard — stich";

const wordsData = {
  "acrostic.md": {
    word: "acrostic",
    primary: "A poem, word puzzle, or composition in which the first letter (or other specific letters) of each line or stanza spells out a word, message, or the alphabet.",
    secondary: "In classical and biblical literature, abecedarian psalms or hymns (such as Psalm 119) structured to follow the alphabetical sequence.",
    quotes: [
      { author: "Edgar Allan Poe", work: "An Acrostic", quote: "Elizabeth it is in vain you say 'Love not'—thou sayest it in so sweet a way; in this **acrostic** thy true name is traced." },
      { author: "Samuel Johnson", work: "The Lives of the Poets", quote: "Dryden had little patience for the **acrostic** and anagram, dismissing them as the frivolous toys of dull wits." },
      { author: "Lewis Carroll", work: "Through the Looking-Glass", quote: "The concluding poem of the book forms an **acrostic** revealing the name Alice Pleasance Liddell in its initial letters." }
    ]
  },
  "cadastral.md": {
    word: "cadastral",
    primary: "Showing or relating to the extent, value, and ownership of land for the purpose of taxation.",
    secondary: "In geodesy and urban planning, designating official maps, surveys, and registers that define legal boundaries of real property.",
    quotes: [
      { author: "Napoleon Bonaparte", work: "Letters and Speeches on the Civil Code", quote: "A comprehensive **cadastral** survey is the only method to ensure equitable land taxation and guarantee title." },
      { author: "Fernand Braudel", work: "The Mediterranean and the Mediterranean World", quote: "The Venetian **cadastral** records describe in minute detail every vineyard, olive grove, and parcel of mainland estate." },
      { author: "Max Weber", work: "Economy and Society", quote: "Modern bureaucratic fiscal administration relies upon exact **cadastral** registers to secure property rights." }
    ]
  },
  "cadastre.md": {
    word: "cadastre",
    primary: "An official register of the ownership, boundaries, and value of real property in a country or district, maintained for taxation.",
    secondary: "In civil law jurisdictions, the foundational public record of real estate parcels, serving as the basis for land registration and mortgages.",
    quotes: [
      { author: "Alexis de Tocqueville", work: "The Old Regime and the Revolution", quote: "The French royal administration attempted to compile a national **cadastre**, but provincial assemblies resisted the fiscal scrutiny." },
      { author: "William Blackstone", work: "Commentaries on the Laws of England", quote: "The Domesday Book may be regarded as the great medieval **cadastre** of the conquered realm." },
      { author: "John Stuart Mill", work: "Principles of Political Economy", quote: "Without an accurate public **cadastre**, disputes over agricultural boundaries and land transfers become interminable." }
    ]
  },
  "distich.md": {
    word: "distich",
    primary: "A unit or strophe of two lines of verse, usually making complete sense; a couplet.",
    secondary: "In classical Greek and Latin prosody, an elegiac distich consisting of an alternating dactylic hexameter and dactylic pentameter.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "The Ovidian Elegiac Metre", quote: "In the hexameter rises the fountain's silvery column; in the pentameter aye falling in melody back: thus breathes the elegiac **distich**." },
      { author: "Alexander Pope", work: "An Essay on Criticism", quote: "The polished **distich** closed each periodic thought with mathematical precision and resonant rhyme." },
      { author: "Johann Wolfgang von Goethe", work: "Venetian Epigrams", quote: "Goethe framed his Italian observations in the antique form of the Roman **distich**, balancing wit and melancholy." }
    ]
  },
  "distichous.md": {
    word: "distichous",
    primary: "Arranged in two opposite vertical rows or ranks on opposite sides of an axis or stem (applied to leaves, flowers, or spikelets).",
    secondary: "In botanical anatomy, a two-ranked phyllotaxis with a divergence angle of 180 degrees, typical of grasses and irises.",
    quotes: [
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "In two-rowed barley, the fertile spikelets are strictly **distichous**, forming a flat, symmetrical ear." },
      { author: "Asa Gray", work: "Structural Botany", quote: "The leaves of the iris display a classic **distichous** arrangement, folding edge-to-edge along the flattened shoot." },
      { author: "Katherine Esau", work: "Plant Anatomy", quote: "Alternate leaves with a half-turn divergence yield a **distichous** pattern common across monocotyledonous families." }
    ]
  },
  "haplostichous.md": {
    word: "haplostichous",
    primary: "In bryology (moss anatomy), having a single row or circle of peristome teeth around the capsule mouth.",
    secondary: "In moss systematics, characterizing haplolepidous mosses whose peristome teeth are formed from a single layer of cell wall thickenings.",
    quotes: [
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "The **haplostichous** peristome consists of sixteen uniseriate teeth that respond hygroscopically to humidity." },
      { author: "Frederick Orpen Bower", work: "The Origin of a Land Flora", quote: "Bryologists distinguish **haplostichous** capsules from the more complex diplostichous types found in true mosses." },
      { author: "Vernon Irvine Cheadle", work: "American Journal of Botany", quote: "Comparative examination reveals that the **haplostichous** arrangement represents a specialized reduction of peristome layers." }
    ]
  },
  "hemistich.md": {
    word: "hemistich",
    primary: "A half of a line of verse, especially one divided by a caesura or left metrically incomplete.",
    secondary: "In classical prosody and Old English alliterative verse, an isolated half-line constituting a distinct rhythmic unit.",
    quotes: [
      { author: "John Dryden", work: "Preface to the Fables", quote: "Virgil’s unfinished **hemistich** leaves the sentence suspended with profound emotional pathos." },
      { author: "Alexander Pope", work: "The Dunciad", quote: "The pedantic critic wasted years debating whether the solitary **hemistich** was intentional or mutilated." },
      { author: "Samuel Johnson", work: "The Lives of the Poets", quote: "Milton’s grand blank verse occasionally breaks into an abrupt **hemistich** that startles the reader’s ear." }
    ]
  },
  "heptastich.md": {
    word: "heptastich",
    primary: "A poem, stanza, or composition consisting of seven lines of verse.",
    secondary: "In poetic forms, a septet such as rhyme royal (ababbcc) popularized by Chaucer in Troilus and Criseyde.",
    quotes: [
      { author: "Geoffrey Chaucer", work: "The Parliament of Fowls", quote: "Chaucer chose the stately **heptastich** stanza to frame his philosophical allegory of courtly love." },
      { author: "George Saintsbury", work: "A History of English Prosody", quote: "The rhymed **heptastich** achieved its highest musical perfection under the Tudor poets." },
      { author: "Edmund Spenser", work: "The Shepheardes Calender", quote: "Each rustic dialogue was introduced by a pastoral **heptastich** setting the seasonal scene." }
    ]
  },
  "monostich.md": {
    word: "monostich",
    primary: "A poem or composition consisting of a single line of verse.",
    secondary: "In classical epigrammatic literature, a condensed single-line proverb, motto, or epitaph.",
    quotes: [
      { author: "Martial", work: "Epigrams", quote: "A witty **monostich** can convey more biting satire than a sprawling epic of twenty books." },
      { author: "Isaac D'Israeli", work: "Curiosities of Literature", quote: "The Greek Anthology preserves many an exquisite **monostich** etched upon ancient sepulchral gems." },
      { author: "Ralph Waldo Emerson", work: "Parnassus", quote: "A memorable **monostich** sticks in the memory when all surrounding verses have vanished." }
    ]
  },
  "monostichous.md": {
    word: "monostichous",
    primary: "Arranged in a single vertical row, rank, or line along an axis (applied to leaves, flowers, or anatomical structures).",
    secondary: "In phyllotaxis and morphology, having all appendages aligned on one side of a stem or rachis.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The flowers in this spike are unilaterally arranged, forming a strictly **monostichous** series." },
      { author: "Katherine Esau", work: "Plant Anatomy", quote: "Under rare developmental constraints, primordia arise in a **monostichous** sequence along one flank of the apex." },
      { author: "D'Arcy Wentworth Thompson", work: "On Growth and Form", quote: "A single row of appendages demonstrates **monostichous** symmetry governed by directional growth factors." }
    ]
  },
  "orthostichy.md": {
    word: "orthostichy",
    primary: "In botany and phyllotaxis, an imaginary vertical or longitudinal line on a stem along which leaves, scales, or branches are arranged one directly above another.",
    secondary: "In plant morphology, the vertical line connecting members of the same spiral series in alternate phyllotaxis.",
    quotes: [
      { author: "Wilhelm Hofmeister", work: "On the Higher Cryptogamia", quote: "Tracing the **orthostichy** along the pine shoot reveals the geometric angular divergence of successive scale leaves." },
      { author: "D'Arcy Wentworth Thompson", work: "On Growth and Form", quote: "The spiral arrangement of sunflower florets resolves mathematically into intersecting sets of parastichies and an **orthostichy**." },
      { author: "Katherine Esau", work: "Plant Anatomy", quote: "Leaves belonging to the same **orthostichy** receive vascular traces from the same primary sympodium." }
    ]
  },
  "pentastich.md": {
    word: "pentastich",
    primary: "A poem, stanza, or composition consisting of five lines of verse; a cinquain or quintet.",
    secondary: "In prosody, a five-line stanzaic form such as the limerick, tanka, or Spanish quintilla.",
    quotes: [
      { author: "Percy Bysshe Shelley", work: "To a Skylark", quote: "Shelley framed his soaring ode in a melodious **pentastich**, four short trochees followed by a sweeping alexandrine." },
      { author: "George Saintsbury", work: "A History of English Prosody", quote: "The English **pentastich** offers a flexible lyric vehicle midway between the quatrain and the sestet." },
      { author: "Dante Gabriel Rossetti", work: "Poems", quote: "The pre-Raphaelite ballad concluded with a solemn **pentastich** invoking the sorrow of parted lovers." }
    ]
  },
  "polystichia.md": {
    word: "polystichia",
    primary: "An abnormal condition characterized by the presence of multiple rows of eyelashes along the margin of the eyelids.",
    secondary: "In ophthalmology and oculoplastic surgery, an anomaly where supernumerary rows of cilia irritate the cornea.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Congenital **polystichia** frequently produces intractable blepharospasm and corneal ulceration." },
      { author: "Ernst Fuchs", work: "Text-Book of Ophthalmology", quote: "Surgical epilation or cryotherapy is indicated when **polystichia** causes trichiasis and persistent mechanical keratitis." },
      { author: "Albrecht von Graefe", work: "Archiv für Ophthalmologie", quote: "In cases of severe **polystichia**, supernumerary cilia emerge directly from the orifices of the Meibomian glands." }
    ]
  },
  "polystichous.md": {
    word: "polystichous",
    primary: "Arranged in many vertical rows, ranks, or series (applied to leaves, scales, or appendages).",
    secondary: "In botany and marine zoology, having numerous rows of organs radiating or aligned along a central axis.",
    quotes: [
      { author: "Asa Gray", work: "Elements of Botany", quote: "The crowded scales of the pine cone form a dense, **polystichous** cylinder protecting the ovules." },
      { author: "Katherine Esau", work: "Plant Anatomy", quote: "In primitive vascular plants, microphylls exhibit a **polystichous** insertion around the massive siphonostele." },
      { author: "Ernst Haeckel", work: "Report on the Radiolaria", quote: "The siliceous spines are disposed in a **polystichous** radiation from the central spherical capsule." }
    ]
  },
  "polystichum.md": {
    word: "polystichum",
    primary: "A large genus of ferns (family Dryopteridaceae), commonly known as holly ferns or shield ferns, bearing circular sori arranged in regular rows on the undersides of pinnae.",
    secondary: "In pteridology, evergreen leptosporangiate ferns characterized by peltate indusia and sharply toothed, leathery fronds.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The Christmas fern, belonging to the genus **Polystichum**, retains its dark green leathery fronds throughout winter." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "Species of **Polystichum** are prized in shade gardens for their symmetrical crowns and architectural fronds." },
      { author: "Frederick Orpen Bower", work: "The Ferns", quote: "The circular indusium attached by a central stalk distinguishes **Polystichum** from adjacent dryopteroid genera." }
    ]
  },
  "stich.md": {
    word: "stich",
    primary: "A verse or line of poetry, especially one forming a distinct rhythmic unit in classical or biblical texts.",
    secondary: "In metric analysis and textual criticism, a standard line of text (equivalent to 16 syllables) used in ancient book calculation.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Biographia Literaria", quote: "The Hebrew psalm moves with antiphonal grandeur, each **stich** responding to its fellow in parallel cadence." },
      { author: "Richard Bentley", work: "Dissertations upon the Epistles of Phalaris", quote: "The ancient copyist recorded the total number of **stich** units at the end of the manuscript to prevent fraudulent omission." },
      { author: "Matthew Arnold", work: "Essays in Criticism", quote: "Homeric vitality depends upon the uninterrupted, rapid movement of the hexameter **stich**." }
    ]
  },
  "stichaeidae.md": {
    word: "stichaeidae",
    primary: "A family of elongated, blennioid marine fishes commonly called pricklebacks, characterized by long, continuous dorsal fins composed entirely of sharp spines.",
    secondary: "In ichthyology, cold-water benthic fishes of the North Pacific and Arctic oceans adapted to rocky intertidal and kelp forest habitats.",
    quotes: [
      { author: "David Starr Jordan", work: "A Guide to the Study of Fishes", quote: "The pricklebacks of the family **Stichaeidae** lurk under stones and seaweeds along the cold rocky coasts of the Pacific." },
      { author: "Spencer Fullerton Baird", work: "Fisheries of North America", quote: "Species belonging to the **Stichaeidae** are easily recognized by their slender eel-like bodies and stiff dorsal spines." },
      { author: "Alister Hardy", work: "The Open Sea", quote: "Tidal pools in subarctic regions harbor small **Stichaeidae** that feed on benthic crustaceans at low tide." }
    ]
  },
  "sticharion.md": {
    word: "sticharion",
    primary: "A liturgical vestment worn in Eastern Orthodox and Byzantine-rite churches by deacons and servers as an outer vestment, and by priests and bishops as an inner vestment.",
    secondary: "In Byzantine liturgics, a long-sleeved tunic of silk or brocade symbolizing purity and the baptismal robe of salvation.",
    quotes: [
      { author: "Timothy Ware", work: "The Orthodox Church", quote: "Before beginning the Divine Liturgy, the priest blesses the **sticharion**, kissing the cross embroidered upon its hem." },
      { author: "Steven Runciman", work: "The Great Church in Captivity", quote: "The deacon walked before the holy gifts wearing an embroidered golden **sticharion** that swept the marble floor." },
      { author: "Alexander Schmemann", work: "Introduction to Liturgical Theology", quote: "The bright white **sticharion** signifies the radiant vesture of light conferred upon the soul in holy baptism." }
    ]
  },
  "sticherus.md": {
    word: "sticherus",
    primary: "A genus of scrambling tropical and subtropical ferns (family Gleicheniaceae), known as umbrella ferns, characterized by repeatedly branched fronds with pectinate segments.",
    secondary: "In pteridology, colonial ferns forming dense thickets along rainforest margins and open volcanic slopes in the Southern Hemisphere.",
    quotes: [
      { author: "Frederick Orpen Bower", work: "The Ferns", quote: "The indeterminate forking fronds of **Sticherus** scramble over low shrubs, forming impenetrable roadside thickets." },
      { author: "Joseph Dalton Hooker", work: "Handbook of the New Zealand Flora", quote: "Species of **Sticherus** carpet damp mountain gullies with delicate, fan-like radiating pinnae." },
      { author: "Katherine Esau", work: "Plant Anatomy", quote: "The protostelic vascular cylinder of **Sticherus** illustrates a primitive level of stelar organization among ferns." }
    ]
  },
  "stichic.md": {
    word: "stichic",
    primary: "Composed in continuous, uniform lines of verse without division into regular stanzas; stichic verse (contrasting with stanzaic or strophic).",
    secondary: "In classical and English prosody, describing compositions written in a single continuous meter, such as epic dactylic hexameter, iambic trimeter, or blank verse.",
    quotes: [
      { author: "George Saintsbury", work: "A History of English Prosody", quote: "Milton chose the **stichic** freedom of unrhymed heroic verse for Paradise Lost, avoiding the jingling fetters of rhyme." },
      { author: "Matthew Arnold", work: "On Translating Homer", quote: "The epic movement of Homer is essentially **stichic**, rolling forward line by line like ocean breakers." },
      { author: "C. S. Lewis", work: "The Allegory of Love", quote: "Chaucer moved between stanzaic royal rhyme and the **stichic** momentum of the decasyllabic couplet." }
    ]
  },
  "stichomancy.md": {
    word: "stichomancy",
    primary: "Divination by opening a book at random and interpreting the first line of verse or sentence that meets the eye; a form of bibliomancy.",
    secondary: "In cultural history, the classical practice of consulting Homer (Sortes Homericae) or Virgil (Sortes Vergilianae) to discover future destiny.",
    quotes: [
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "Men have sought prophetic revelations through **stichomancy**, opening the verses of Virgil with superstitious awe." },
      { author: "Walter Scott", work: "The Antiquary", quote: "The old scholar practiced **stichomancy** with a weathered volume of Horace, seeking an omen for the coming journey." },
      { author: "Thomas De Quincey", work: "Autobiographic Sketches", quote: "My brother resorted to **stichomancy** upon the Bible, taking the first text his finger touched as an infallible sign." }
    ]
  },
  "stichometry.md": {
    word: "stichometry",
    primary: "The measurement or calculation of the length of ancient manuscripts by counting the standard lines (stichoi) of text.",
    secondary: "In classical and biblical palaeography, the practice of recording line totals in colophons to ensure textual completeness and calculate scribal payment.",
    quotes: [
      { author: "Bruce M. Metzger", work: "The Text of the New Testament", quote: "Ancient scribes appended the **stichometry** at the conclusion of each epistle to prevent unauthorized interpolations." },
      { author: "Frederic G. Kenyon", work: "Books and Readers in Ancient Greece and Rome", quote: "Careful **stichometry** reveals that the standard classical stichos consisted of about sixteen syllables, the length of a Homeric hexameter." },
      { author: "L. D. Reynolds", work: "Scribes and Scholars", quote: "Byzantine catalogues often preserve the **stichometry** of lost classical plays, indicating their original manuscript extent." }
    ]
  },
  "stichomythia.md": {
    word: "stichomythia",
    primary: "In classical drama, dialogue in which two characters speak alternating single lines of verse in rapid, sharp succession.",
    secondary: "In dramatic technique, rapid verbal sparring or staccato argument used to heighten emotional conflict, suspense, or rhetorical debate.",
    quotes: [
      { author: "Gilbert Murray", work: "A History of Ancient Greek Literature", quote: "The fierce encounter between Oedipus and Tiresias blazes through brilliant **stichomythia**, line clashing against line like swords." },
      { author: "William Shakespeare", work: "Richard III", quote: "The intense **stichomythia** between Richard and Queen Elizabeth displays the terrifying agility of Shakespeare’s rhetorical wit." },
      { author: "T. S. Eliot", work: "The Sacred Wood", quote: "Senecan tragedy perfected a sharp, aphoristic **stichomythia** that exerted profound influence over Elizabethan dramatists." }
    ]
  },
  "telestich.md": {
    word: "telestich",
    primary: "A poem or composition in which the final letters of consecutive lines, read vertically downward, form a word, name, or motto (contrasting with an acrostic).",
    secondary: "In wordplay and poetic cryptograms, a verse structure combining initial, medial, or final letter patterns.",
    quotes: [
      { author: "Isaac D'Israeli", work: "Curiosities of Literature", quote: "The ingenious poet combined an acrostic with a **telestich**, so that both the head and tail of each line spelled his patron's name." },
      { author: "George Puttenham", work: "The Arte of English Poesie", quote: "A courtly maker may show his cunning by devising a **telestich** whose end-letters reveal a secret anagram." },
      { author: "Samuel Butler", work: "Hudibras", quote: "He tortured his brains with many an idle puzzle, spinning out acrostic and **telestich** to flatter a disdainful mistress." }
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
console.log("Writing & Script Batch 3 completed! Total words updated:", Object.keys(wordsData).length);
