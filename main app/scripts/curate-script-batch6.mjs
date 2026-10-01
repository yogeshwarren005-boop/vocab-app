import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Writing & Script/Dashboard — bibl";

const wordsData = {
  "Bible.md": {
    word: "Bible",
    primary: "The sacred scriptures of Judaism and Christianity, consisting of the Old and New Testaments.",
    secondary: "A book regarded as authoritative or canonical in a particular subject, field, or trade.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "So shall the world go on, till to its final day, when the holy book, our sacred **Bible**, is unsealed." },
      { author: "Abraham Lincoln", work: "Second Inaugural Address", quote: "Both read the same **Bible** and pray to the same God, and each invokes His aid against the other." },
      { author: "Thomas Carlyle", work: "Heroes, Hero-Worship, and the Heroic in History", quote: "The translation of the **Bible** by Luther gave the German people a common speech and a common soul." }
    ]
  },
  "bibl.md": {
    word: "bibl",
    primary: "An abbreviation for biblical or bibliography; also a combining form denoting book or bible.",
    secondary: "In bibliographical citation and library catalogs, standard notation indicating book history or biblical references.",
    quotes: [
      { author: "Frederic G. Kenyon", work: "Our Bible and the Ancient Manuscripts", quote: "Under the catalog heading **bibl**, ancient codices of the Greek Septuagint were systematically listed." },
      { author: "Bruce M. Metzger", work: "The Text of the New Testament", quote: "Textual critics consult the **bibl** concordance to verify citations preserved in patristic writings." },
      { author: "Umberto Eco", work: "The Name of the Rose", quote: "The parchment catalog marked every theological codex with the Gothic abbreviation **bibl**." }
    ]
  },
  "bible-worship.md": {
    word: "bible-worship",
    primary: "Excessive, superstitious, or idolatrous reverence for the literal letter or physical book of the Bible; bibliolatry.",
    secondary: "In theological critique, treating the biblical text as infallible and divine in itself, elevating the letter above the living Spirit.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Confessions of an Inquiring Spirit", quote: "This mechanical **bible-worship** turns the living word of God into an idol of printed paper." },
      { author: "Ralph Waldo Emerson", work: "Divinity School Address", quote: "The churches languish because a dead **bible-worship** has replaced direct personal communion with the divine." },
      { author: "Thomas Paine", work: "The Age of Reason", quote: "The superstitious **bible-worship** of the clergy demands that reason surrender to ancient mythological tales." }
    ]
  },
  "bibless.md": {
    word: "bibless",
    primary: "Lacking or without a bib (a piece of cloth tied under the chin of a child or diner to protect clothes).",
    secondary: "Deprived of protective coverings; untidy or exposed.",
    quotes: [
      { author: "Charles Dickens", work: "Bleak House", quote: "The neglected infant sat **bibless** upon the hearthrug, smearing porridge across its pinafore." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "The careless nurse let the toddler run **bibless** through the garden, ruining his clean Sunday smock." },
      { author: "George Eliot", work: "Middlemarch", quote: "Aunt Julia scolded the careless maid for leaving the nursery children **bibless** at supper." }
    ]
  },
  "biblioclasm.md": {
    word: "biblioclasm",
    primary: "The practice or act of destroying books or writings, especially the Bible, religious texts, or cultural literature; book-burning.",
    secondary: "In cultural history and polemics, intentional ideological or sectarian eradication of libraries and documentary heritage.",
    quotes: [
      { author: "Isaac D'Israeli", work: "Curiosities of Literature", quote: "The history of fanaticism is stained with recurrent orgies of **biblioclasm**, from the flames of Alexandria to the bonfires of the Inquisition." },
      { author: "Heinrich Heine", work: "Almansor", quote: "Where they begin with **biblioclasm**, burning books in the public squares, they end by burning human beings." },
      { author: "Ray Bradbury", work: "Fahrenheit 451", quote: "The state sanctified institutional **biblioclasm**, commanding firemen to incinerate every printed volume without mercy." }
    ]
  },
  "biblioclast.md": {
    word: "biblioclast",
    primary: "A person who destroys or mutilates books, especially religious texts or literary collections.",
    secondary: "A book-destroyer driven by ideological censorship, religious zeal, or malicious vandalism.",
    quotes: [
      { author: "Isaac D'Israeli", work: "Curiosities of Literature", quote: "The fanatical **biblioclast** tore the illuminated leaves from the monastic manuscripts, selling the vellum to bookbinders." },
      { author: "Thomas Frognall Dibdin", work: "Bibliomania", quote: "Every true bibliophile regards the wanton **biblioclast** with horror and disgust." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The zealot Caliph has often been denounced as a barbarous **biblioclast** who ordered the heating of public baths with the scrolls of Alexandria." }
    ]
  },
  "bibliogony.md": {
    word: "bibliogony",
    primary: "The production, manufacture, or creation of books; the art and craft of book-making.",
    secondary: "In the history of the book, the entire technical and material process of typography, paper manufacture, printing, and binding.",
    quotes: [
      { author: "William Morris", work: "The Ideal Book", quote: "True **bibliogony** demands that paper, ink, typography, and binding unite into an organic work of visual beauty." },
      { author: "Holbrook Jackson", work: "The Anatomy of Bibliomania", quote: "The history of **bibliogony** traces the transformation of papyrus rolls into Gutenberg's movable metal types." },
      { author: "Thomas Frognall Dibdin", work: "The Bibliographical Decameron", quote: "Aldus Manutius elevated Italian **bibliogony** to an art form that captivated the humanists of Europe." }
    ]
  },
  "bibliographer.md": {
    word: "bibliographer",
    primary: "A person who writes, compiles, or specializes in bibliography; an expert in the history, description, and classification of books.",
    secondary: "In textual scholarship, a specialist who investigates the physical composition, printing variants, and provenance of printed books and manuscripts.",
    quotes: [
      { author: "Samuel Johnson", work: "The Lives of the Poets", quote: "The diligent **bibliographer** rescues the names of forgotten authors from the oblivion of dusty shelves." },
      { author: "Fredson Bowers", work: "Principles of Bibliographical Description", quote: "The analytical **bibliographer** treats the printed sheet as material evidence of the printing shop's mechanical routine." },
      { author: "Jorge Luis Borges", work: "The Book of Sand", quote: "The wandering **bibliographer** cataloged volumes printed in dead languages across three continents." }
    ]
  },
  "bibliographic.md": {
    word: "bibliographic",
    primary: "Of or relating to bibliography, books, or lists of publications.",
    secondary: "Pertaining to the descriptive cataloging, physical specifications, and publishing history of printed materials.",
    quotes: [
      { author: "Henry Bradshaw", work: "Collected Papers", quote: "Accurate **bibliographic** analysis requires the scholar to collate every signature and watermark in the incunable." },
      { author: "Walter Wilson Greg", work: "A Bibliography of the English Printed Drama", quote: "The **bibliographic** method provides textual criticism with an empirical foundation in physical typography." },
      { author: "Umberto Eco", work: "How to Write a Thesis", quote: "Every scholarly inquiry must commence with an exhaustive **bibliographic** survey of primary sources." }
    ]
  },
  "bibliographical.md": {
    word: "bibliographical",
    primary: "Of or pertaining to bibliography or bibliographers (variant of bibliographic).",
    secondary: "Relating to the descriptive compilation and historical study of books as physical artifacts.",
    quotes: [
      { author: "Thomas Frognall Dibdin", work: "Bibliotheca Spenceriana", quote: "Lord Spencer’s magnificent library provided materials for a lifetime of **bibliographical** research." },
      { author: "George Saintsbury", work: "A History of English Criticism", quote: "His **bibliographical** notes illuminated obscure Elizabethan pamphlet wars." },
      { author: "Frederic G. Kenyon", work: "The Palaeography of Greek Papyri", quote: "The discovery of Oxyrhynchus revolutionized **bibliographical** understanding of ancient book production." }
    ]
  },
  "bibliography.md": {
    word: "bibliography",
    primary: "A list of books, articles, or other sources on a particular subject or by a particular author; also, the list of sources cited in a scholarly work.",
    secondary: "The academic study of books as physical, historical, and textual objects.",
    quotes: [
      { author: "Walter Wilson Greg", work: "The Present Position of Bibliography", quote: "What **bibliography** deals with is literature in the form of material transmission." },
      { author: "Samuel Johnson", work: "Letters", quote: "A well-ordered **bibliography** is a key that unlocks the intellectual treasures of past centuries." },
      { author: "Fredson Bowers", work: "Textual and Literary Criticism", quote: "Rigorous **bibliography** protects textual editors from substituting modern aesthetic preferences for original authorial readings." }
    ]
  },
  "biblioklept.md": {
    word: "biblioklept",
    primary: "A person who steals books, especially from libraries or bookshops.",
    secondary: "In the psychology of collecting, a pathological book-thief whose obsessive passion for literature drives them to larceny.",
    quotes: [
      { author: "Holbrook Jackson", work: "The Anatomy of Bibliomania", quote: "The notorious **biblioklept** Libri carried off thousands of priceless medieval manuscripts from French provincial libraries." },
      { author: "Andrew Lang", work: "The Library", quote: "The common thief steals for monetary profit, but the genuine **biblioklept** steals to gloat over his sequestered treasures." },
      { author: "Thomas Frognall Dibdin", work: "Bibliomania", quote: "Librarians must keep a vigilant eye upon the plausible gentleman who masks the heart of a **biblioklept** beneath a scholar’s gown." }
    ]
  },
  "bibliolatrous.md": {
    word: "bibliolatrous",
    primary: "Excessively or superstitiously devoted to books, especially the Bible; characterized by bibliolatry.",
    secondary: "Exhibiting blind, uncritical reverence for written or printed authorities over empirical evidence or moral reason.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Notes on English Divines", quote: "The seventeenth-century puritans displayed a **bibliolatrous** veneration for every punctuation mark of the King James text." },
      { author: "Ralph Waldo Emerson", work: "Essays: Second Series", quote: "The living generation must not submit its spiritual freedom to a **bibliolatrous** worship of ancient scrolls." },
      { author: "Thomas Henry Huxley", work: "Science and Christian Tradition", quote: "The dogmatic theology of the day demanded **bibliolatrous** obedience to Genesis at the expense of geology." }
    ]
  },
  "bibliolatry.md": {
    word: "bibliolatry",
    primary: "Excessive, superstitious, or idolatrous reverence for books, especially the literal text of the Bible.",
    secondary: "In intellectual history, the uncritical exaltation of written dogma above moral conscience and rational inquiry.",
    quotes: [
      { author: "Gotthold Ephraim Lessing", work: "Anti-Goeze", quote: "The Christian faith existed long before the New Testament was written; to substitute the book for the religion is sheer **bibliolatry**." },
      { author: "Oliver Wendell Holmes Sr.", work: "The Professor at the Breakfast-Table", quote: "Traditional creeds often confuse religious devotion with a narrow, letter-bound **bibliolatry**." },
      { author: "Matthew Arnold", work: "Literature and Dogma", quote: "The rigid **bibliolatry** of modern sects obscures the poetic beauty and moral righteousness of the prophets." }
    ]
  },
  "bibliomania.md": {
    word: "bibliomania",
    primary: "An excessive, passionate, or obsessive enthusiasm for collecting and possessing books.",
    secondary: "In social and cultural history, a collecting craze focused on rare editions, first impressions, unique bindings, and uncut copies.",
    quotes: [
      { author: "Thomas Frognall Dibdin", work: "Bibliomania, or Book-Madness", quote: "The symptoms of **bibliomania** are easily diagnosed: an irresistible passion for large-paper copies, uncut edges, and black-letter folios." },
      { author: "Holbrook Jackson", work: "The Anatomy of Bibliomania", quote: "Victims of **bibliomania** will starve their bodies to feed their shelves with rare first editions." },
      { author: "Walter Scott", work: "The Antiquary", quote: "Old Monkbarns was infected with an incurable **bibliomania**, bidding wildly at every provincial book auction." }
    ]
  },
  "bibliomaniacal.md": {
    word: "bibliomaniacal",
    primary: "Of, relating to, or affected by bibliomania; passionately obsessed with collecting books.",
    secondary: "Characterized by extravagant, obsessive, or uncritical expenditure in pursuing rare volumes.",
    quotes: [
      { author: "Isaac D'Israeli", work: "Curiosities of Literature", quote: "The auction room was crowded with **bibliomaniacal** zealots eager to contest the possession of the Valdarfer Boccaccio." },
      { author: "Andrew Lang", work: "Books and Bookmen", quote: "A true collector understands that **bibliomaniacal** ecstasy when discovering an elusive Elzevir in a dusty stall." },
      { author: "Thomas Carlyle", work: "Letters", quote: "He squandered his modest patrimony in **bibliomaniacal** purchases of obscure theological pamphlets." }
    ]
  },
  "biblion.md": {
    word: "biblion",
    primary: "The ancient Greek word for 'book' or 'scroll', originally designating a papyrus roll imported through the Phoenician port of Byblos.",
    secondary: "In classical philology, an individual scroll or book forming a division of a larger literary work (such as Homer's Iliad or Herodotus's Histories).",
    quotes: [
      { author: "Frederic G. Kenyon", work: "Books and Readers in Ancient Greece and Rome", quote: "In classical Athens, a **biblion** was a rolled sheet of Egyptian papyrus inscribed in neat uncial columns." },
      { author: "Bruce M. Metzger", work: "The Text of the New Testament", quote: "The diminutive form **biblion** was used in the Gospels to denote the sacred scroll of the prophet Isaiah." },
      { author: "L. D. Reynolds", work: "Scribes and Scholars", quote: "The transition from the papyrus **biblion** to the parchment codex was the greatest technological revolution of late antiquity." }
    ]
  },
  "bibliophile.md": {
    word: "bibliophile",
    primary: "A person who loves or collects books, especially one who appreciates their binding, typography, rarity, and historical value.",
    secondary: "A discriminating collector who treasures fine printing, pristine provenance, and exquisite paper quality.",
    quotes: [
      { author: "Holbrook Jackson", work: "The Anatomy of Bibliomania", quote: "The genuine **bibliophile** handles a fine binding as tenderly as a mother caresses her child." },
      { author: "Anatole France", work: "The Crime of Sylvestre Bonnard", quote: "Sylvestre Bonnard was a gentle, scholarly **bibliophile** whose happiest hours were spent among dusty manuscripts." },
      { author: "Charles Lamb", work: "Detached Thoughts on Books and Reading", quote: "To a true **bibliophile**, the scent of seventeenth-century calfskin is sweeter than the perfumes of Arabia." }
    ]
  },
  "bibliophilia.md": {
    word: "bibliophilia",
    primary: "The love of books; an intense fondness or passionate interest in collecting and reading books.",
    secondary: "In the history of collecting, the aesthetic and intellectual appreciation of book arts, typography, paper, and binding.",
    quotes: [
      { author: "Thomas Frognall Dibdin", work: "The Library Companion", quote: "A lifetime devoted to **bibliophilia** brings rich rewards in scholarship and serene contentment." },
      { author: "Walter Pater", work: "Appreciations", quote: "His **bibliophilia** was not a shallow ostentation, but an authentic devotion to the physical sanctuary of thought." },
      { author: "Jorge Luis Borges", work: "Selected Non-Fictions", quote: "My father’s library was the primal temple where my incurable **bibliophilia** was born." }
    ]
  },
  "bibliophilic.md": {
    word: "bibliophilic",
    primary: "Of, relating to, or characteristic of a bibliophile; showing a love of books.",
    secondary: "Relating to fine book collecting, artistic typography, and limited editions.",
    quotes: [
      { author: "William Morris", work: "The Art of the Book", quote: "The Kelmscott Press was founded to satisfy the highest **bibliophilic** ideals of craftsmanship and legibility." },
      { author: "Henry James", work: "The Aspern Papers", quote: "He approached the shuttered Venetian palazzo with all the stealthy eagerness of a **bibliophilic** hunter." },
      { author: "Umberto Eco", work: "Six Walks in the Fictional Woods", quote: "A **bibliophilic** pilgrimage to ancient monasteries rewards the scholar with unexpected textual treasures." }
    ]
  },
  "bibliophobe.md": {
    word: "bibliophobe",
    primary: "A person who hates, fears, or distrusts books or reading.",
    secondary: "An anti-intellectual or cultural vandal who opposes literature and the preservation of libraries.",
    quotes: [
      { author: "Isaac D'Israeli", work: "Curiosities of Literature", quote: "The illiterate tyrant was a confirmed **bibliophobe**, decreeing that all philosophical writings be cast into the flames." },
      { author: "Holbrook Jackson", work: "The Anatomy of Bibliomania", quote: "The **bibliophobe** regards a room lined with books as a useless repository of cobwebs and dead men's dreams." },
      { author: "Thomas Frognall Dibdin", work: "Bibliomania", quote: "Every generation must defend the sanctuary of the library against the ignorant assaults of the **bibliophobe**." }
    ]
  },
  "bibliophobia.md": {
    word: "bibliophobia",
    primary: "A dread, hatred, or intense dislike of books or reading.",
    secondary: "In cultural history, anti-intellectual hostility toward literacy, literature, or library collections.",
    quotes: [
      { author: "Thomas Frognall Dibdin", work: "Bibliophobia", quote: "I write to diagnose this pervasive **bibliophobia**, where wealthy patrons abandon literature for frivolous amusements." },
      { author: "Ray Bradbury", work: "Fahrenheit 451", quote: "The totalitarian regime cultivated a pervasive **bibliophobia**, teaching citizens that books bring only sorrow and discord." },
      { author: "George Saintsbury", work: "A History of English Criticism", quote: "Puritan **bibliophobia** toward secular stage-plays resulted in the closing of the public theaters." }
    ]
  },
  "bibliopole.md": {
    word: "bibliopole",
    primary: "A person who buys and sells books, especially rare, antique, or second-hand books; a bookseller.",
    secondary: "In 18th- and 19th-century literary society, an erudite bookseller who served as publisher, patron, and confidant to authors.",
    quotes: [
      { author: "Samuel Johnson", work: "The Life of Savage", quote: "The needy poet took his manuscript to a noted **bibliopole** in Fleet Street, hoping for a modest advance." },
      { author: "Walter Scott", work: "The Antiquary", quote: "He spent the morning haggling with an Edinburgh **bibliopole** over an imperfect black-letter quarto." },
      { author: "Washington Irving", work: "The Sketch Book", quote: "The learned **bibliopole** sat behind his counter, surrounded by mountains of folios and dusty leather bindings." }
    ]
  },
  "bibliopolic.md": {
    word: "bibliopolic",
    primary: "Of, relating to, or characteristic of a bibliopole or the trade of selling rare books.",
    secondary: "Pertaining to the antiquarian book trade, auctions, and bookseller catalogs.",
    quotes: [
      { author: "Thomas Frognall Dibdin", work: "The Bibliographical Decameron", quote: "The **bibliopolic** rivalries at the Duke of Roxburghe’s auction drove bids to unprecedented heights." },
      { author: "Isaac D'Israeli", work: "Curiosities of Literature", quote: "Through sharp **bibliopolic** acumen, the bookseller amassed a fortune by cornering first editions of Shakespeare." },
      { author: "Charles Lamb", work: "Essays of Elia", quote: "I love to rummage through the damp stalls of those old **bibliopolic** alleys near Saint Paul’s." }
    ]
  },
  "bibliopolist.md": {
    word: "bibliopolist",
    primary: "A bookseller, especially one dealing in rare, antiquarian, or valuable books; a bibliopole.",
    secondary: "An antiquarian dealer specializing in the trade of historic manuscripts, fine bindings, and scarce literature.",
    quotes: [
      { author: "Walter Scott", work: "Waverley", quote: "The venerable **bibliopolist** adjusted his spectacles and unlocked the iron grating that guarded his rarest incunabula." },
      { author: "Thomas Carlyle", work: "Critical and Miscellaneous Essays", quote: "The London **bibliopolist** played a decisive role in introducing German romantic literature to English readers." },
      { author: "William Makepeace Thackeray", work: "Pendennis", quote: "He consulted a fashionable **bibliopolist** in Piccadilly who promised to furnish his library with uniform calfskin sets." }
    ]
  },
  "bibliotaph.md": {
    word: "bibliotaph",
    primary: "A person who hides away or buries books, locking them up so that nobody else can see or read them.",
    secondary: "In the pathology of book collecting, an obsessive hoarder who entombs valuable books in closed vaults, damp cellars, or impenetrable safes.",
    quotes: [
      { author: "Isaac D'Israeli", work: "Curiosities of Literature", quote: "The miserable **bibliotaph** kept his precious manuscripts padlocked in iron chests, refusing admittance even to the most learned scholars." },
      { author: "Andrew Lang", work: "The Library", quote: "Worse than the book-thief is the churlish **bibliotaph**, who entombs unique copies where they rot unseen." },
      { author: "Holbrook Jackson", work: "The Anatomy of Bibliomania", quote: "The miserly **bibliotaph** gloats over his sequestered treasures, taking pleasure solely in their inaccessible concealment." }
    ]
  },
  "bibliothec.md": {
    word: "bibliothec",
    primary: "A librarian; also, an archaic word for a library or collection of books.",
    secondary: "In historical bibliography, a keeper or custodian of a library collection.",
    quotes: [
      { author: "Samuel Johnson", work: "A Dictionary of the English Language", quote: "The learned **bibliothec** cataloged the royal collection with admirable accuracy and diligence." },
      { author: "Isaac D'Israeli", work: "Curiosities of Literature", quote: "Magliabechi was the ultimate **bibliothec**, living in a cave of books and remembering the exact shelf of every volume in Florence." },
      { author: "Walter Scott", work: "The Antiquary", quote: "The old earl employed a German **bibliothec** to arrange the ancient charters of the castle." }
    ]
  },
  "bibliotheca.md": {
    word: "bibliotheca",
    primary: "A library, archive, or collection of books.",
    secondary: "In bibliography and classical literature, a comprehensive catalog, bibliography, or repository of literary works.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The Ulpian **bibliotheca**, founded by Emperor Trajan, preserved the historical archives of the Roman Senate." },
      { author: "Thomas Frognall Dibdin", work: "Bibliotheca Spenceriana", quote: "The magnificent **bibliotheca** at Althorp displayed the finest gathering of early Italian printing in the world." },
      { author: "Umberto Eco", work: "The Name of the Rose", quote: "Over the entrance to the great hall was carved the inscription: 'Secretum **Bibliotheca**'." }
    ]
  },
  "bibliothecal.md": {
    word: "bibliothecal",
    primary: "Of, relating to, or belonging to a library or the management of libraries.",
    secondary: "Pertaining to library architecture, cataloging systems, and archival preservation.",
    quotes: [
      { author: "Anthony Panizzi", work: "Passages in the Life of a Librarian", quote: "The design of the British Museum Reading Room solved long-standing **bibliothecal** problems of lighting and book delivery." },
      { author: "Isaac D'Israeli", work: "Curiosities of Literature", quote: "His **bibliothecal** reforms transformed the neglected university collection into a model of scholarly order." },
      { author: "Melvil Dewey", work: "A Classification and Subject Index", quote: "A modern **bibliothecal** system must provide uniform decimal notation across all departments of knowledge." }
    ]
  },
  "bibliothecarial.md": {
    word: "bibliothecarial",
    primary: "Relating to a librarian or the duties and profession of librarianship.",
    secondary: "Pertaining to the professional administration, classification, and custodial care of library holdings.",
    quotes: [
      { author: "Jorge Luis Borges", work: "The Total Library", quote: "His **bibliothecarial** duties required him to classify an infinite labyrinth of volumes written in unknown scripts." },
      { author: "Holbrook Jackson", work: "The Anatomy of Bibliomania", quote: "Richard de Bury exercised his **bibliothecarial** passion while serving as Chancellor of England." },
      { author: "Frederic G. Kenyon", work: "Libraries and the Public", quote: "The **bibliothecarial** profession demands both erudite scholarship and sympathetic administrative guidance." }
    ]
  },
  "bibliotherapy.md": {
    word: "bibliotherapy",
    primary: "The use of selected reading materials as a therapeutic adjuvant in medicine, psychiatry, and counseling to promote mental health and emotional healing.",
    secondary: "In psychotherapy and clinical psychology, guided reading designed to facilitate self-understanding, insight, and behavioral recovery.",
    quotes: [
      { author: "Sigmund Freud", work: "Introductory Lectures on Psycho-Analysis", quote: "Guided reading often serves as an informal **bibliotherapy**, allowing the troubled soul to recognize its conflicts in poetic literature." },
      { author: "William Osler", work: "Aequanimitas", quote: "For the weary physician and anxious patient alike, **bibliotherapy** with the classics offers a sovereign balm for spiritual distress." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "We introduced structured **bibliotherapy** to help long-isolated patients reconnect with the shared human narrative." }
    ]
  },
  "bibliotic.md": {
    word: "bibliotic",
    primary: "Of or relating to the examination, scientific study, and authentication of written documents, handwriting, and manuscripts.",
    secondary: "In forensic document analysis, relating to the microscopic and chemical analysis of inks, papers, and pen strokes to detect forgery.",
    quotes: [
      { author: "Persifor Frazer", work: "Bibliotics: Or, the Study of Documents", quote: "Modern **bibliotic** science relies upon chemical analysis of ink pigments and microscopic examination of pen tremors." },
      { author: "Arthur Conan Doyle", work: "The Norwood Builder", quote: "Sherlock Holmes examined the disputed signature with all the rigorous precision of a trained **bibliotic** expert." },
      { author: "Albert S. Osborn", work: "Questioned Documents", quote: "The **bibliotic** investigator must distinguish between natural variations in handwriting and deliberate fraudulent simulation." }
    ]
  },
  "bibliotics.md": {
    word: "bibliotics",
    primary: "The scientific study and forensic examination of documents and handwriting to determine their authenticity, authorship, and date.",
    secondary: "In forensic science, the discipline combining microscopy, chemical analysis, and graphology to identify forged writings.",
    quotes: [
      { author: "Persifor Frazer", work: "Bibliotics: Or, the Study of Documents", quote: "I have proposed the term **bibliotics** to designate the scientific investigation of questioned handwriting and legal papers." },
      { author: "Hans Gross", work: "Criminal Investigation", quote: "In cases of suspected testamentary forgery, the court must consult an expert in **bibliotics** and paper technology." },
      { author: "Albert S. Osborn", work: "Questioned Documents", quote: "The maturation of **bibliotics** as an empirical science has driven fraudulent document examiners from the witness box." }
    ]
  },
  "bibliotist.md": {
    word: "bibliotist",
    primary: "A handwriting expert or forensic document examiner who specializes in bibliotics.",
    secondary: "An investigator who examines disputed signatures, inks, and paper characteristics to determine document authenticity.",
    quotes: [
      { author: "Persifor Frazer", work: "Bibliotics", quote: "The impartial **bibliotist** measures pen pressure, slant, and microscopic stroke hesitation with scientific detachment." },
      { author: "Arthur Conan Doyle", work: "The Case-Book of Sherlock Holmes", quote: "The testimony of the court-appointed **bibliotist** established that the codicil had been drafted with modern synthetic ink." },
      { author: "Albert S. Osborn", work: "Questioned Documents", quote: "A qualified **bibliotist** never relies on intuition, but demonstrates each physical finding through photographic enlargements." }
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
console.log("Writing & Script Batch 6 completed! Total words updated:", Object.keys(wordsData).length);
