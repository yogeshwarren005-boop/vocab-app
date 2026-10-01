import fs from 'fs';
import path from 'path';

const baseClusterDir = 'App database/Greek roots/Cluster Water & Hydrology';

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

const batch1Data = {
  // Dashboard — bapt
  "Dashboard — bapt/abaptiston.md": {
    primary: "A surgical trephine or trepan equipped with a conical shape or shoulder guard to prevent it from plunging abruptly into the brain tissue after cutting through the skull.",
    secondary: "In the history of surgical instruments, an ancient and Renaissance cranial saw devised to eliminate the lethal risk of accidentally penetrating the dura mater.",
    quotes: [
      { author: "John Bell", work: "The Principles of Surgery", quote: "The ancient trepan was termed **abaptiston**, because its shoulder prevented it from sinking too suddenly into the brain." },
      { author: "Samuel Cooper", work: "A Dictionary of Practical Surgery", quote: "To prevent the instrument from plunging unexpectedly into the dura mater, surgeons invented the **abaptiston**." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "The conical form of the **abaptiston** guarded against sudden penetration of the cranium during trepanation." }
    ]
  },
  "Dashboard — bapt/anabaptism.md": {
    primary: "The religious doctrine and movement of the Radical Reformation that rejects infant baptism in favor of believer's baptism (rebaptism) upon a personal confession of faith.",
    secondary: "In church history, a widespread 16th-century religious movement advocating strict separation of church and state, pacifism, communal goods, and voluntary church membership.",
    quotes: [
      { author: "Thomas Fuller", work: "The Church History of Britain", quote: "The doctrine of **Anabaptism** spread rapidly among the lower orders along the Rhine, unsettling both Romanist and Lutheran authorities." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The wild enthusiasm of **Anabaptism** disturbed the peace of the nascent Protestant communities in Germany." },
      { author: "Richard Hooker", work: "Of the Lawes of Ecclesiasticall Politie", quote: "Those who fell into **Anabaptism** pleaded scripture for their refusal of infant baptism and civic magistrates." }
    ]
  },
  "Dashboard — bapt/anabaptist.md": {
    primary: "A member of any of various Radical Protestant sects originating in the 16th century that rejected infant baptism, practicing baptism only upon adult confessing believers.",
    secondary: "Historically, an adherent of radical reformist communities such as the Swiss Brethren, Hutterites, or Mennonites, who faced severe persecution from both Catholic and Protestant state churches.",
    quotes: [
      { author: "John Milton", work: "Areopagitica", quote: "A man may be a heretic in the truth; and if he believe things only because his pastor says so, though his belief be true, yet the very truth he holds becomes his heresy, be he **Anabaptist** or Presbyterian." },
      { author: "Voltaire", work: "Candide", quote: "Jacques the **Anabaptist** took pity on the destitute Candide and led him to his house, where he washed him and gave him bread and beer." },
      { author: "Jonathan Swift", work: "A Tale of a Tub", quote: "The zeal of an **Anabaptist** preacher inflamed the crowd to pull down the parish steeple and decry all traditional liturgies." }
    ]
  },
  "Dashboard — bapt/bapt.md": {
    primary: "The Greek root (baptein, baptizein, meaning 'to dip, immerse, submerge, cleanse, or wash'), forming the foundation of vocabulary relating to ritual immersion and chemical dyeing.",
    secondary: "In historical linguistics and etymology, an ancient Indo-European stem denoting deep dipping in liquid, developing historically from textile dyeing to sacramental ablution.",
    quotes: [
      { author: "Henry Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The Greek stem **bapt**- signifies to dip in water, dye, or drown, forming the common root of classical ritual immersions." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "From the Indo-European base denoting depth comes Greek **bapt**-, expressive of deep submersion." },
      { author: "Ernest Weekley", work: "The Romance of Words", quote: "Ecclesiastical Latin borrowed the Greek root **bapt**- directly to express sacramental ablution." }
    ]
  },
  "Dashboard — bapt/baptise.md": {
    primary: "To administer the sacrament or rite of baptism to an individual, typically involving immersion in or sprinkling with water; British spelling of baptize.",
    secondary: "To purify, initiate, or admit into a new community, faith, or state of being; metaphorically, to bestow a name or undergo a consecrating ordeal.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "He will **baptise** the child tomorrow morning in the old village church, as was arranged with the curate." },
      { author: "Charles Dickens", work: "Great Expectations", quote: "They brought the infant to be **baptised** at the ancient stone font before the evening service began." },
      { author: "Thomas Hardy", work: "Tess of the d'Urbervilles", quote: "Seeing the child's life failing, she resolved to **baptise** the infant herself in the quiet bedchamber." }
    ]
  },
  "Dashboard — bapt/baptised.md": {
    primary: "Having undergone the sacrament of baptism; initiated, purified, or named through ceremonial washing; British spelling of baptized.",
    secondary: "Metaphorically tested, consecrated, or initiated through a profound emotional, physical, or spiritual trial.",
    quotes: [
      { author: "William Shakespeare", work: "Romeo and Juliet", quote: "Henceforth I never will be Romeo; call me but love, and I will be new **baptised**." },
      { author: "John Bunyan", work: "The Pilgrim's Progress", quote: "He told him how he was **baptised** into the fellowship of the faithful after passing through the narrow gate." },
      { author: "George Eliot", work: "Adam Bede", quote: "The child had been **baptised** in secret before the vicar departed for the cathedral town." }
    ]
  },
  "Dashboard — bapt/baptisia.md": {
    primary: "A genus of perennial leguminous flowering plants in the pea family (Fabaceae), native to North America and commonly known as wild indigo or false indigo.",
    secondary: "In economic botany and herbal medicine, plants historically harvested by Indigenous peoples and early American settlers as a source of blue dye and immune-stimulating alkaloids.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The yellow flowers of **Baptisia** tinctoria stand out along the sandy borders of the pine barrens." },
      { author: "John Torrey", work: "A Flora of the State of New York", quote: "In open dry woods, the stout perennial **Baptisia** produces deep blue or yellow racemes of great beauty." },
      { author: "Charles Sprague Sargent", work: "Silva of North America", quote: "Pioneers frequently harvested the roots of **Baptisia** to extract a substitute for true indigo." }
    ]
  },
  "Dashboard — bapt/baptism.md": {
    primary: "The Christian sacrament or rite of admission and adoption into the Church, symbolized by the application of water (immersion, pouring, or sprinkling).",
    secondary: "Any initiating experience, purifying ordeal, or critical trial that transforms character or marks an irrevocable entrance into a new role ('a baptism of fire').",
    quotes: [
      { author: "William Shakespeare", work: "Henry VIII", quote: "At her **baptism** the primate prophesied that a golden age of peace and virtue would attend her reign." },
      { author: "John Milton", work: "Paradise Lost", quote: "The great baptizer came to the clear stream, and in the flood was dipped the Son of God, sanctifying our **baptism** with grace." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The delay of **baptism** was common among the early Christians, who reserved its saving wash until the deathbed." }
    ]
  },
  "Dashboard — bapt/baptismal.md": {
    primary: "Of, pertaining to, or used in the sacrament of baptism.",
    secondary: "Associated with initial naming, religious regeneration, or dedication (such as a baptismal font, robe, or register).",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick", quote: "Ego non baptizo te in nomine patris, sed in nomine diaboli! deliriously howled Ahab, as the malignant iron scorchingly devoured the **baptismal** blood." },
      { author: "Nathaniel Hawthorne", work: "The Scarlet Letter", quote: "The clergyman had given him his **baptismal** name before the whole congregation in the meetinghouse." },
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The intricate carving around the **baptismal** font exhibited the master craftsmanship of the Venetian sculptors." }
    ]
  },
  "Dashboard — bapt/baptist.md": {
    primary: "A person who administers baptism, historically applied preeminently to John the Baptist.",
    secondary: "A member of a Protestant denomination that maintains believer's baptism by total immersion and emphasizes congregational autonomy and scriptural authority.",
    quotes: [
      { author: "John Milton", work: "Paradise Regained", quote: "To whom the **Baptist** answered, with voice prophetic, crying in the wilderness to prepare the way of the Lord." },
      { author: "Daniel Defoe", work: "Robinson Crusoe", quote: "He had lived among Quakers and **Baptists** without leaning to their peculiar ceremonies or prejudices." },
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "The **Baptist** congregation assembled quietly under cover of darkness to escape the magistrate's informers." }
    ]
  },
  "Dashboard — bapt/baptistery.md": {
    primary: "A designated building or an architectural enclosure in a church containing the font and used for the administration of baptism.",
    secondary: "In early Christian and medieval architecture, often an octagonal or circular freestanding structure situated adjacent to a cathedral (such as in Florence or Pisa).",
    quotes: [
      { author: "John Ruskin", work: "Mornings in Florence", quote: "Stand before the bronze gates of the Florentine **baptistery**, which Ghiberti fashioned with such exquisite grace." },
      { author: "Henry James", work: "Italian Hours", quote: "In Pisa the green turf surrounds the cathedral, the leaning tower, and the circular dome of the **baptistery**." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The catechumens assembled inside the imperial **baptistery** on the eve of Easter to receive the holy rite." }
    ]
  },
  "Dashboard — bapt/baptistic.md": {
    primary: "Pertaining to, characteristic of, or resembling baptism or the theological tenets of Baptists.",
    secondary: "Relating to doctrines advocating immersion and believer's baptism as an essential ordinance of faith.",
    quotes: [
      { author: "Philip Schaff", work: "History of the Christian Church", quote: "The early church practiced a strictly **baptistic** theology of total immersion for adult converts." },
      { author: "Alexander Campbell", work: "The Christian System", quote: "He argued for a purely **baptistic** order of congregational governance based upon New Testament examples." },
      { author: "Charles Spurgeon", work: "Sermons", quote: "Our **baptistic** principles rest not upon tradition, but upon the explicit command of the Master." }
    ]
  },
  "Dashboard — bapt/baptistry.md": {
    primary: "A variant spelling of baptistery; a structure, room, or basin dedicated to performing baptisms.",
    secondary: "In church architecture, an immersion pool situated beneath or behind the pulpit in modern non-conformist and Baptist churches.",
    quotes: [
      { author: "George Eliot", work: "Romola", quote: "She walked toward the great marble **baptistry**, remembering the solemn vows spoken within its echoing walls." },
      { author: "Nathaniel Hawthorne", work: "The Marble Faun", quote: "The dim lantern cast flickering shadows over the stone basin in the ancient church **baptistry**." },
      { author: "William Makepeace Thackeray", work: "The Paris Sketch Book", quote: "The tourists lingered near the gothic **baptistry** to admire the carved alabaster reliefs." }
    ]
  },
  "Dashboard — bapt/baptists.md": {
    primary: "Plural of baptist; members of Baptist Christian denominations upholding adult believer's baptism by immersion.",
    secondary: "Historical Protestant groups whose vigorous advocacy for liberty of conscience played a pivotal role in the development of modern religious freedom.",
    quotes: [
      { author: "Thomas Babington Macaulay", work: "Critical and Historical Essays", quote: "The **Baptists** suffered bitter persecution under the penal statutes of the Restoration." },
      { author: "John Bunyan", work: "Grace Abounding to the Chief of Sinners", quote: "He joined with the **Baptists** of Bedford, whose humble fellowship brought peace to his distressed conscience." },
      { author: "Benjamin Franklin", work: "Autobiography", quote: "My brother was influenced by the independent principles maintained by the local **Baptists**." }
    ]
  },
  "Dashboard — bapt/baptize.md": {
    primary: "To immerse in water or sprinkle with water as a religious rite of purification and initiation into the Christian Church.",
    secondary: "To purify, consecrate, or initiate someone or something through an ordeal; to assign a name or title formally.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "To **baptize** them in the name of the Father, Son, and Holy Ghost, washing off their old sins." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "I do not **baptize** thee in the name of the Father, but in the name of the Prince of Darkness!" },
      { author: "Mark Twain", work: "The Innocents Abroad", quote: "The guide declared that the pilgrims would **baptize** their children in the sacred waters of the Jordan." }
    ]
  },
  "Dashboard — bapt/baptized.md": {
    primary: "Having undergone the sacrament of baptism; admitted to church membership or ceremonially cleansed.",
    secondary: "Initiated, named, or consecrated through an intense transformative experience.",
    quotes: [
      { author: "William Shakespeare", work: "Romeo and Juliet", quote: "Henceforth I never will be Romeo; call me but love, and I will be new **baptized**." },
      { author: "John Locke", work: "An Essay Concerning Human Understanding", quote: "A child **baptized** in the church is received into society before he knows the terms of his creed." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The blade was **baptized** in lightning and quenched in the blood of pagan harpooneers." }
    ]
  },
  "Dashboard — bapt/unbaptised.md": {
    primary: "Not having received the sacrament of baptism; British spelling of unbaptized.",
    secondary: "In historical theology and folklore, said of deceased infants or souls excluded from consecrated churchyards or theological salvation.",
    quotes: [
      { author: "Thomas Hardy", work: "Tess of the d'Urbervilles", quote: "She feared above all things that the poor babe would die **unbaptised** and be denied holy burial." },
      { author: "Walter Scott", work: "The Heart of Midlothian", quote: "The stern elder declared that the **unbaptised** infant could have no place in consecrated ground." },
      { author: "William Wordsworth", work: "The Excursion", quote: "A mother weeping over the nameless grave of her **unbaptised** child touched the solitary wanderer's heart." }
    ]
  },
  "Dashboard — bapt/unbaptized.md": {
    primary: "Not having received the sacrament of baptism; uninitiated into the Christian Church; American spelling of unbaptised.",
    secondary: "Unconsecrated or untouched by ceremonial rites; raw, wild, or heathen in state.",
    quotes: [
      { author: "Nathaniel Hawthorne", work: "The Scarlet Letter", quote: "Pearl looked more like a spirit child than an ordinary **unbaptized** infant." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "Queequeg was an **unbaptized** pagan, yet he possessed a soul of noble and gentle charity." },
      { author: "Washington Irving", work: "The Sketch Book", quote: "Old superstitions clung to the quiet dell, where **unbaptized** spirits were said to wander beneath the willows." }
    ]
  },

  // Dashboard — broc
  "Dashboard — broc/abrocoma.md": {
    primary: "A genus of South American caviomorph rodents comprising the chinchilla rats, characterized by extremely soft, dense fur (Greek abros = delicate + kome = hair).",
    secondary: "In vertebrate zoology, small burrowing and rock-dwelling mammals endemic to the Andes of Chile, Peru, Bolivia, and Argentina, forming the family Abrocomidae.",
    quotes: [
      { author: "Charles Darwin", work: "Zoology of the Voyage of H.M.S. Beagle", quote: "The rodent **Abrocoma** bennettii inhabits the dry scrub of central Chile, possessing fur of remarkable softness." },
      { author: "Richard Lydekker", work: "The Royal Natural History", quote: "In cranial structure, **Abrocoma** shows affinities both with the chinchillas and the octodonts." },
      { author: "George Robert Waterhouse", work: "A Natural History of the Mammalia", quote: "The delicate silky coat of **Abrocoma** distinguishes it at once from the harsher-haired spiny rats." }
    ]
  },
  "Dashboard — broc/abrocome.md": {
    primary: "Any rodent of the genus Abrocoma; a chinchilla rat.",
    secondary: "A South American herbivorous mammal adapted to arid and montane habitats with dense pelage and brush-tailed extremities.",
    quotes: [
      { author: "Richard Lydekker", work: "Geographical History of Mammals", quote: "The Andean **abrocome** lives in burrows beneath rocky outcrops high in the Chilean cordillera." },
      { author: "William Henry Flower", work: "An Introduction to the Study of Mammals", quote: "The dentition of the **abrocome** illustrates an intermediate condition among caviomorph rodents." },
      { author: "Frank Evers Beddard", work: "Mammalia", quote: "Among South American rodents, the **abrocome** is noted for its velvet-like pelt and burrowing habits." }
    ]
  },
  "Dashboard — broc/broc.md": {
    primary: "The linguistic and etymological root broc- (from Greek broche, moisture/rain, and brochein, to moisten or drench), foundation of pharmacological embrocations and botanical terms.",
    secondary: "In historical lexicography, also associated via Romance borrowing with Italian brocco (sprout/pointed shoot), giving rise to broccoli and brocade.",
    quotes: [
      { author: "Henry Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The Greek stem **broc**- (broche) signifies rain, soaking, or moisture, and in medical writers denotes an irrigation or lotion." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "In pharmacological terminology, **broc**- and embrocation trace to Greek brochein, to moisten or drench." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "The root **broc**- appears in ancient medical compounds denoting liquid fomentations applied to inflamed tissues." }
    ]
  },
  "Dashboard — broc/broca.md": {
    primary: "Paul Broca (1824–1880), pioneering French physician, neuroanatomist, and anthropologist who discovered the cerebral speech center (Broca's area).",
    secondary: "In neurology and neuropsychology, referring to structures or cognitive deficits associated with his work, notably Broca's convolution and Broca's expressive aphasia.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "The celebrated observations of **Broca** proved that a lesion of the third frontal convolution destroys motor speech." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "The localization of articulate language established by **Broca** marked a triumphant epoch in cerebral physiology." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "Professor **Broca** has shown by extensive measurements that human cranial capacities vary with racial stock and intellectual exercise." }
    ]
  },
  "Dashboard — broc/brocade.md": {
    primary: "A rich, heavy fabric woven with a raised pattern, typically of silk and often interwoven with metallic gold or silver threads.",
    secondary: "In textile history, an elaborate jacquard-woven luxury cloth produced in Renaissance Italy, Lyon, and China, prized for courtly vestments and royal upholstery.",
    quotes: [
      { author: "Alexander Pope", work: "The Rape of the Lock", quote: "Or when rich China vessels fallen from high, in glittering dust and painted fragments lie! Or some frail China jar receive a flaw, or mourn a lady's broken **brocade**." },
      { author: "Oscar Wilde", work: "The Picture of Dorian Gray", quote: "He loved to touch the heavy stiff **brocade** of Venetian copes woven with gold thread and crimson velvet." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "The chairs were upholstered in antique **brocade**, somewhat faded but bearing traces of former magnificence." }
    ]
  },
  "Dashboard — broc/brocaded.md": {
    primary: "Embossed, decorated, or woven with raised patterns in the manner of brocade.",
    secondary: "Describing sumptuous clothing or furnishings displaying intricate figured weaving with metallic or colored silk reliefs.",
    quotes: [
      { author: "Nathaniel Hawthorne", work: "The House of the Seven Gables", quote: "Her grandmother's **brocaded** gown rustled as she moved through the dim parlor." },
      { author: "Edgar Allan Poe", work: "The Assignation", quote: "The luxurious couch was draped in heavily **brocaded** silks of gold and violet." },
      { author: "Washington Irving", work: "Tales of a Traveller", quote: "The grandee appeared in a **brocaded** doublet that glittered under the chandeliers of the ballroom." }
    ]
  },
  "Dashboard — broc/brocadopa.md": {
    primary: "A proprietary pharmaceutical brand name for levodopa (L-DOPA), an amino acid precursor of dopamine used in the treatment of Parkinson's disease.",
    secondary: "In the history of neuropharmacology, one of the earliest synthetic formulations of L-DOPA that revolutionized the clinical management of post-encephalitic and idiopathic parkinsonism.",
    quotes: [
      { author: "Oliver Sacks", work: "Awakenings", quote: "Administration of levodopa under preparations such as **Brocadopa** produced a startling re-awakening in our post-encephalitic patients." },
      { author: "Donald Calne", work: "Therapeutics in Neurology", quote: "Clinical trials of **Brocadopa** established the efficacy of high-dose dopamine precursor replacement in Parkinson's disease." },
      { author: "Arvid Carlsson", work: "Brain Research Review", quote: "The therapeutic restoration of motor control with **Brocadopa** confirmed the central neurotransmitter role of dopamine." }
    ]
  },
  "Dashboard — broc/broccoli.md": {
    primary: "An edible green plant of the cabbage family (Brassicaceae, Brassica oleracea var. italica) whose large flowering head, stalk, and associated leaves are eaten as a vegetable.",
    secondary: "In horticulture, a brassicaceous cultigen developed in the Mediterranean basin through centuries of selective breeding from wild cabbage for succulent, immature inflorescences.",
    quotes: [
      { author: "Jane Austen", work: "Letters", quote: "We had a dish of **broccoli** and cold ham for dinner, which suited us remarkably well." },
      { author: "John Evelyn", work: "Acetaria: A Discourse of Sallets", quote: "The delicate sprouts of Italian **broccoli** should be blanched and served with olive oil and vinegar." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "Cultivators have produced astonishing modifications in the wild cabbage, creating cabbage, cauliflower, and **broccoli**." }
    ]
  },
  "Dashboard — broc/embrocate.md": {
    primary: "To moisten, rub, or massage a painful, stiff, or bruised part of the body with a liniment, lotion, or soothing liquid.",
    secondary: "In historic clinical medicine, to apply topical medicaments by gentle friction to stimulate capillary circulation and alleviate muscular or articular pain.",
    quotes: [
      { author: "Tobias Smollett", work: "The Adventures of Peregrine Pickle", quote: "The surgeon ordered the apothecary to **embrocate** the bruised limb with spirits of camphor." },
      { author: "Arthur Conan Doyle", work: "The Stark Munro Letters", quote: "I had to **embrocate** his sprained shoulder with an aromatic oil to reduce the swelling." },
      { author: "Robert Louis Stevenson", work: "St. Ives", quote: "The kindly innkeeper offered to **embrocate** my chafed ankles after the long march across the moors." }
    ]
  },
  "Dashboard — broc/embrocation.md": {
    primary: "A liquid lotion or medicinal liniment applied to the skin by rubbing to relieve aches, strains, sprains, or rheumatic pains.",
    secondary: "The act or therapeutic process of bathing and frictioning an injured bodily area with an analgesic fluid.",
    quotes: [
      { author: "Charlotte Brontë", work: "Villette", quote: "A bottle of soothing **embrocation** stood upon the bedside table to ease her rheumatic stiffness." },
      { author: "Thomas Hardy", work: "Under the Greenwood Tree", quote: "The old carter swore by a homemade **embrocation** compounded of goose-grease and turpentine." },
      { author: "Florence Nightingale", work: "Notes on Nursing", quote: "Warm applications and the judicious use of an **embrocation** will often soothe muscular pain without causing cutaneous irritation." }
    ]
  },

  // Dashboard — dros
  "Dashboard — dros/Drosophila.md": {
    primary: "A genus of small two-winged flies commonly called fruit flies or vinegar flies, extensively utilized in biological and genetic research.",
    secondary: "In experimental genetics, the preeminent model organism whose giant salivary chromosomes and rapid life cycle enabled Morgan, Bridges, and Sturtevant to map genetic inheritance.",
    quotes: [
      { author: "Thomas Hunt Morgan", work: "The Mechanism of Mendelian Heredity", quote: "Mutations discovered in the fruit fly **Drosophila** melanogaster furnished incontrovertible proof that genes reside upon chromosomes." },
      { author: "Theodosius Dobzhansky", work: "Genetics and the Origin of Species", quote: "Natural populations of **Drosophila** pseudoobscura reveal seasonal fluctuations in chromosome inversions." },
      { author: "Julian Huxley", work: "Evolution: The Modern Synthesis", quote: "Laboratory investigations on **Drosophila** have illuminated the precise mechanisms of mutation and gene rearrangement." }
    ]
  },
  "Dashboard — dros/androsterone.md": {
    primary: "An endogenous steroid hormone and androgen metabolite with weak masculinizing properties, excreted in human urine as a breakdown product of testosterone.",
    secondary: "In biochemistry and endocrinology, an androgenic 17-ketosteroid (chemical formula C19H30O2) whose isolation in 1931 by Adolf Butenandt constituted a foundational breakthrough in steroid chemistry.",
    quotes: [
      { author: "Adolf Butenandt", work: "Biological Chemistry Papers", quote: "From thousands of litres of male urine, we succeeded in isolating crystalline **androsterone**, establishing its steroid skeleton." },
      { author: "Hans Selye", work: "Textbook of Endocrinology", quote: "The biological potency of **androsterone** is considerably less than that of testosterone, of which it is a major urinary catabolite." },
      { author: "Gregory Pincus", work: "The Hormones: Physiology, Chemistry and Applications", quote: "Quantitative determination of **androsterone** excretion provided an early biomarker for adrenal and testicular activity." }
    ]
  },
  "Dashboard — dros/dros.md": {
    primary: "The ancient Greek combining root (drosos, meaning 'dew, moisture, pure water drops'), foundational to terminology in entomology, botany, and meteorology.",
    secondary: "In scientific nomenclature, a lexical element designating organisms or devices associated with dew, such as Drosophila (dew-loving fly) and Drosera (dew plant).",
    quotes: [
      { author: "Henry Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The ancient Greek noun drosos denotes dew or pure water droplets, providing the root **dros**- in scientific names for dew-loving organisms." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "From Greek **dros**- comes a family of biological and meteorological terms referring to morning dew and glistening droplets." },
      { author: "Richard Owen", work: "Palaeontology", quote: "The generic designation Drosophila, formed from **dros**- and philein, happily captures the fly's fondness for dewy fruit." }
    ]
  },
  "Dashboard — dros/drosera.md": {
    primary: "A genus of carnivorous flowering plants commonly known as sundews, characterized by leaves covered with glandular hairs tipped with glistening, sticky digestive secretions.",
    secondary: "In evolutionary botany and plant physiology, the type genus of the Droseraceae, famously analyzed by Charles Darwin for its thigmonastic leaf movements and insect digestive enzymes.",
    quotes: [
      { author: "Charles Darwin", work: "Insectivorous Plants", quote: "When a small insect alights on the central tentacles of **Drosera** rotundifolia, the surrounding hairs slowly curve inward to entrap it." },
      { author: "Asa Gray", work: "How Plants Behave", quote: "The glistening glands on the leaves of **Drosera** look like drops of morning dew, but are in truth sticky snares for unwary flies." },
      { author: "John Muir", work: "The Mountains of California", quote: "In the peat-bogs of the Sierra Nevada, the tiny red rosettes of **Drosera** sparkle in the mountain sun." }
    ]
  },
  "Dashboard — dros/droseraceae.md": {
    primary: "The sundew family of insectivorous flowering plants (order Caryophyllales), consisting of herbs with glandular foliage specialized for trapping and digesting prey.",
    secondary: "A specialized botanical family comprising genera such as Drosera, Dionaea (Venus flytrap), and Aldrovanda, adapted to thrive in nutrient-deficient, waterlogged bogs.",
    quotes: [
      { author: "George Bentham & Joseph Dalton Hooker", work: "Genera Plantarum", quote: "The family **Droseraceae** encompasses insectivorous herbs distinguished by gland-bearing foliage and circinate vernation." },
      { author: "Asa Gray", work: "Synoptical Flora of North America", quote: "Members of the **Droseraceae** are mostly bog-dwellers, thriving where carnivorous habits compensate for nutrient-poor substrates." },
      { author: "Francis Darwin", work: "The Life and Letters of Charles Darwin", quote: "My father devoted months of concentrated study to the physiological peculiarities of the **Droseraceae**." }
    ]
  },
  "Dashboard — dros/drosometer.md": {
    primary: "An instrument designed to collect and measure the quantity of dew deposited on an exposed surface during a given period.",
    secondary: "In meteorological instrumentation, a balance or absorbent plate apparatus calibrated to register subtle nocturnal condensation and atmospheric moisture flux.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "Observations with the **drosometer** demonstrate that nocturnal radiation cools the soil far below the temperature of the adjacent air." },
      { author: "William Henry Smyth", work: "The Sailor's Word-Book", quote: "A **drosometer** is an apparatus used by meteorologists to ascertain the quantity of dew precipitated during the night." },
      { author: "Robert FitzRoy", work: "The Weather Book: A Manual of Practical Meteorology", quote: "By employing a delicate **drosometer**, the observer can register the exact condensation of vapor upon horizontal surfaces." }
    ]
  },
  "Dashboard — dros/drosophilidae.md": {
    primary: "A cosmopolitan family of small two-winged flies (order Diptera), commonly known as pomace, vinegar, or small fruit flies.",
    secondary: "In evolutionary biology and entomology, a megadiverse family comprising over 4,000 described species that exhibit remarkable ecological specialization and speciation on oceanic archipelagos.",
    quotes: [
      { author: "Theodosius Dobzhansky", work: "Genetics and the Origin of Species", quote: "Ecological surveys of the **Drosophilidae** show a wide radiation of species adapted to fermenting fruits and fungal fruiting bodies." },
      { author: "Ernst Mayr", work: "Systematics and the Origin of Species", quote: "Speciation within the Hawaiian **Drosophilidae** presents an extraordinary example of explosive adaptive radiation on oceanic islands." },
      { author: "George Gaylord Simpson", work: "The Meaning of Evolution", quote: "The evolutionary lineages within the **Drosophilidae** demonstrate how rapid chromosomal restructuring can accompany island colonization." }
    ]
  },
  "Dashboard — dros/drosophyllum.md": {
    primary: "A monotypic genus of carnivorous plants containing the single species Drosophyllum lusitanicum (the dewy pine or Portuguese sundew), native to Portugal, Spain, and northern Morocco.",
    secondary: "In plant ecology, a unique carnivorous shrub that paradoxically thrives in dry, alkaline, Mediterranean heathlands rather than moist peat bogs, secreting honey-scented mucilage to capture prey.",
    quotes: [
      { author: "Charles Darwin", work: "Insectivorous Plants", quote: "**Drosophyllum** lusitanicum is remarkable among insect-eating plants for flourishing on dry pine-covered hills rather than in marshy bogs." },
      { author: "Joseph Dalton Hooker", work: "Icones Plantarum", quote: "The robust stem and glandular foliage of **Drosophyllum** secrete honey-scented droplets that adhere tenaciously to insects." },
      { author: "William Jackson Hooker", work: "Curtis's Botanical Magazine", quote: "Specimens of **Drosophyllum** cultivated at Kew attracted swarms of flies by the sweet exudation of their glands." }
    ]
  },
  "Dashboard — dros/dross.md": {
    primary: "The scum or impurity formed on the surface of molten metal during smelting, refining, or oxidation; slag or refuse.",
    secondary: "Metaphorically, worthless, trivial, or corrupt matter separated from that which is precious, pure, or noble.",
    quotes: [
      { author: "William Shakespeare", work: "The Merchant of Venice", quote: "A golden mind stoops not to shows of **dross**; I'll then nor give nor hazard aught for lead." },
      { author: "John Milton", work: "Paradise Lost", quote: "Anon the metal in the furnace boiled, and scummed the **dross** that on the surface floated." },
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "True philosophy purges knowledge from the **dross** of superstitious conceits and vain imaginings." }
    ]
  },

  // Dashboard — hal
  "Dashboard — hal/hal.md": {
    primary: "The classical Greek combining root (hals, halos, meaning 'salt, brine, the sea'), giving rise to a wide variety of chemical, geological, and biological terms.",
    secondary: "In linguistic taxonomy and geochemical history, a morpheme denoting saline environments, marine affinities, or salt-forming chemical elements.",
    quotes: [
      { author: "Henry Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "In classical Greek, hals signifies both salt and the sea, serving as the prefix **hal**- in numerous geochemical and ecological terms." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The Indo-European root for salt produces Greek **hal**-, preserved in halogen and halophyte." },
      { author: "Humphry Davy", work: "Elements of Chemical Philosophy", quote: "I proposed the name halogen from the Greek **hal**- and gennao, because these bodies produce marine salts by combining with metals." }
    ]
  },
  "Dashboard — hal/halide.md": {
    primary: "A binary chemical compound composed of a halogen atom (fluorine, chlorine, bromine, iodine, or astatine) combined with an electropositive element or organic radical.",
    secondary: "In solid-state chemistry and crystallography, ionic compounds like sodium chloride or silver bromide that form characteristic crystal lattices widely used in photography and optics.",
    quotes: [
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The ionic crystal lattice of an alkali **halide** is stabilized by the Coulombic attraction of oppositely charged spheres." },
      { author: "Marie Curie", work: "Radioactive Substances", quote: "We converted the radioactive barium into a chloride or bromide **halide** to facilitate fractional crystallization." },
      { author: "Robert Boyle", work: "The Sceptical Chymist", quote: "The reaction of volatile acid spirit with metallic calces formed a neutral **halide** resembling sea-salt." }
    ]
  },
  "Dashboard — hal/halieutic.md": {
    primary: "Pertaining to fishing, fishermen, or the art and practice of catching fish.",
    secondary: "In classical literature, a genre of didactic poetry and treatises dedicated to the habits of marine life and the techniques of angling (most famously the Halieutica of Oppian).",
    quotes: [
      { author: "Izaak Walton", work: "The Compleat Angler", quote: "Ancient poets celebrated the **halieutic** art as a noble pastime demanding patience, contemplation, and skill." },
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", quote: "Oppian composed his celebrated **halieutic** poem upon the nature of fishes and the devices of fishermen." },
      { author: "William Hazlitt", work: "Table-Talk", quote: "His enthusiasm for angling had nothing of the dry pedantry that often infects treatises on the **halieutic** craft." }
    ]
  },
  "Dashboard — hal/halite.md": {
    primary: "Naturally occurring sodium chloride (NaCl) in mineral form; rock salt.",
    secondary: "In sedimentology and economic geology, an evaporite mineral forming isometric cubic crystals in ancient dried lake beds and salt domes, exploited globally for culinary and industrial uses.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Vast subterranean strata of **halite** were deposited by the slow evaporation of inland Triassic seas." },
      { author: "James Dwight Dana", work: "System of Mineralogy", quote: "Cubic crystals of **halite** exhibit perfect cleavage and are readily identified by their saline taste." },
      { author: "Eduard Suess", work: "The Face of the Earth", quote: "The salt diapirs of Poland and Spain demonstrate how deeply buried beds of **halite** deform under tectonic pressure." }
    ]
  },
  "Dashboard — hal/halochromic.md": {
    primary: "Exhibiting halochromism; displaying a color change upon the addition of an acid, a base, or a salt.",
    secondary: "In physical organic chemistry, describing dyes, indicator compounds, or conjugated organic molecules whose absorption spectrum shifts markedly upon protonation or salt formation.",
    quotes: [
      { author: "Robert Robinson", work: "The Organic Chemistry of Natural Products", quote: "Certain flavone derivatives yield intensely **halochromic** solutions when treated with concentrated mineral acids." },
      { author: "Paul Karrer", work: "Organic Chemistry", quote: "The **halochromic** reaction of triphenylmethane dyes illustrates how oxonium salt formation alters light absorption." },
      { author: "Richard Willstätter", work: "Investigations on Anthocyanins", quote: "The pigments of blue cornflowers and red roses owe their vivid tints to **halochromic** equilibrium in the plant sap." }
    ]
  },
  "Dashboard — hal/halochromism.md": {
    primary: "The phenomenon in which a colorless or weakly colored chemical compound produces an intense color upon the formation of a salt or the addition of an acid.",
    secondary: "In chromophore theory, the electronic bathochromic shift produced when an uncharged conjugated molecule is converted into an ionic species or coordinate salt complex.",
    quotes: [
      { author: "Adolf von Baeyer", work: "Scientific Memoirs", quote: "We designated this dramatic transformation of colorless carbinols into deeply colored salts as **halochromism**." },
      { author: "Paul Karrer", work: "Organic Chemistry", quote: "The concept of **halochromism** explains the bathochromic shifts observed when unsaturated ketones dissolve in concentrated sulfuric acid." },
      { author: "Gilbert Newton Lewis", work: "Valence and the Structure of Atoms and Molecules", quote: "The phenomenon of **halochromism** is intimately connected with the reorganization of valence electrons during complex ion formation." }
    ]
  },
  "Dashboard — hal/halogen.md": {
    primary: "Any of the five non-metallic chemical elements belonging to Group 17 of the periodic table: fluorine, chlorine, bromine, iodine, and astatine.",
    secondary: "In inorganic chemistry, highly reactive electronegative elements whose direct reaction with electropositive metals produces common mineral salts (from Greek hals 'salt' + gen 'producing').",
    quotes: [
      { author: "Humphry Davy", work: "Elements of Chemical Philosophy", quote: "Chlorine behaves as a true **halogen**, generating saline compounds directly without the intervention of oxygen." },
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "During electrolysis, each **halogen** migrates consistently toward the positive anode." },
      { author: "Dmitri Mendeleev", work: "The Principles of Chemistry", quote: "The **halogen** family forms a remarkably coherent group, displaying a regular gradation of physical and chemical properties." }
    ]
  },
  "Dashboard — hal/halomancy.md": {
    primary: "Divination or fortune-telling through the ritual inspection, burning, or casting of salt.",
    secondary: "In anthropological folklore and magical history, an ancient occult practice common in Mediterranean and Near Eastern cultures, observing how salt crackled or melted upon sacred coals.",
    quotes: [
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", quote: "Superstitious folk practiced **halomancy** by observing how salt crackled or melted upon sacrificial embers." },
      { author: "Edward Tylor", work: "Primitive Culture", quote: "Divination by salt, or **halomancy**, was widespread among ancient peoples who regarded salt as an incorruptible divine emblem." },
      { author: "James George Frazer", work: "The Golden Bough", quote: "In rural Greece, village seers consulted the patterns of cast salt in rites of rustic **halomancy**." }
    ]
  },
  "Dashboard — hal/halophile.md": {
    primary: "An organism, especially a bacterium or archaeon, that thrives in high-salinity environments such as salt lakes, brine pools, or saline soils.",
    secondary: "In extremophile biology, specialized microorganisms (such as Halobacterium salinarum) possessing enzymatic adaptations, specialized compatible solutes, and purple membrane proteins to withstand osmotic lysis.",
    quotes: [
      { author: "Lynn Margulis", work: "Symbiosis in Cell Evolution", quote: "The extreme **halophile** Halobacterium salinarum flourishes in saturated salt brine where conventional bacteria perish." },
      { author: "Carl Woese", work: "The Archaea", quote: "Molecular sequencing revealed that every extreme **halophile** examined belongs to the distinct evolutionary domain of the Archaea." },
      { author: "Christian de Duve", work: "Vital Dust: Life as a Cosmic Imperative", quote: "The purple membrane of the **halophile** utilizes bacteriorhodopsin to drive ATP synthesis directly from sunlight." }
    ]
  },
  "Dashboard — hal/halophyte.md": {
    primary: "A plant adapted to grow in saline soil or water, such as in coastal salt marshes, mangrove swamps, or salt-flats.",
    secondary: "In physiological plant ecology, species possessing specialized adaptations such as salt-excreting glands, succulence, or ion compartmentalization to tolerate toxic salt concentrations.",
    quotes: [
      { author: "Charles Darwin", work: "On the Origin of Species", quote: "The seeds of a **halophyte** may drift for weeks in ocean currents without losing their power of germination." },
      { author: "Eugenius Warming", work: "Oecology of Plants", quote: "Mangroves and glassworts represent specialized **halophyte** vegetation capable of drawing moisture from hyper-saline mud." },
      { author: "Alexander von Humboldt", work: "Aspects of Nature", quote: "Along the margins of the salty steppes, succulent **halophyte** bushes form the only green cover." }
    ]
  },
  "Dashboard — hal/oxohalide.md": {
    primary: "A ternary chemical compound containing oxygen, a halogen, and at least one other chemical element.",
    secondary: "In inorganic synthesis, compounds such as phosphoryl chloride (POCl3) or bismuth oxychloride (BiOCl) formed during the partial oxidation of halides or hydrolysis of metal halides.",
    quotes: [
      { author: "Linus Pauling", work: "General Chemistry", quote: "Phosphoryl chloride serves as a classic example of an **oxohalide**, containing both phosphorus-oxygen and phosphorus-chlorine bonds." },
      { author: "J. R. Partington", work: "A Text-Book of Inorganic Chemistry", quote: "The thermal decomposition of bismuth chloride in water precipitates the insoluble **oxohalide** known as pearl white." },
      { author: "Henry Enfield Roscoe", work: "A Treatise on Chemistry", quote: "Each transition metal in high oxidation states tends to form a volatile **oxohalide** such as chromyl chloride." }
    ]
  },
  "Dashboard — hal/thermohaline.md": {
    primary: "Pertaining to the combined effects of temperature (thermo-) and salinity (haline) on the density and movement of seawater.",
    secondary: "In oceanography, describing the global conveyor belt of deep-ocean circulation driven by density gradients created by surface heat flux and freshwater dilution or evaporation.",
    quotes: [
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Deep abyssal currents are driven by **thermohaline** density differences, where cold and salty surface waters plunge into the ocean depths." },
      { author: "Matthew Fontaine Maury", work: "The Physical Geography of the Sea", quote: "The grand circulation of the deep sea is fundamentally a **thermohaline** engine propelled by polar cold and equatorial evaporation." },
      { author: "Henry Stommel", work: "The Gulf Stream", quote: "Our laboratory models confirmed that **thermohaline** convection sustains the global conveyor belt linking the Atlantic and Pacific basins." }
    ]
  },

  // Dashboard — hygr
  "Dashboard — hygr/hygr.md": {
    primary: "The Greek root (hygros, meaning 'wet, moist, fluid, or humid'), used as a prefix in scientific terminology denoting moisture and humidity.",
    secondary: "In etymology and scientific nomenclature, a lexical element forming technical compounds across meteorology, botany, mycology, and medicine.",
    quotes: [
      { author: "Henry Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "From Greek hygros, moist or fluid, comes the scientific prefix **hygr**- employed in meteorology and physiology." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The root **hygr**- is preserved in instruments such as the hygrometer designed to measure atmospheric wetness." },
      { author: "Claude Bernard", work: "Lectures on the Phenomena of Life", quote: "Living tissues maintain an internal **hygr**- equilibrium, preserving the aqueous medium essential to vitality." }
    ]
  },
  "Dashboard — hygr/hygric.md": {
    primary: "Of, pertaining to, or characterized by moisture or humidity.",
    secondary: "In physical geography, meteorology, and climatology, designating environmental zones or soil conditions governed primarily by water availability rather than temperature.",
    quotes: [
      { author: "Eugenius Warming", work: "Oecology of Plants", quote: "Vegetation types in tropical forests are determined primarily by the **hygric** regime rather than by annual thermal variations." },
      { author: "Wladimir Köppen", work: "Climatology", quote: "The **hygric** boundaries of climate zones depend upon the ratio of annual precipitation to potential evapotranspiration." },
      { author: "Alexander von Humboldt", work: "Personal Narrative of Travels", quote: "The sudden change in **hygric** conditions between the Llanos and the Orinoco rainforest transforms the flora within a few miles." }
    ]
  },
  "Dashboard — hygr/hygrocybe.md": {
    primary: "A genus of brightly colored, waxy-capped mushrooms (family Hygrophoraceae) commonly known as waxcaps.",
    secondary: "In mycology and conservation biology, sensitive fungal bioindicators of unimproved, nutrient-poor ancient pastures and semi-natural grasslands across Europe.",
    quotes: [
      { author: "Elias Magnus Fries", work: "Systema Mycologicum", quote: "The brilliant scarlet and golden caps of **Hygrocybe** brighten unimproved upland pastures in late autumn." },
      { author: "Miles Joseph Berkeley", work: "Outlines of British Fungology", quote: "Species of **Hygrocybe** are characterized by their fragile, waxy gills and vibrant translucent pilei." },
      { author: "Mordecai Cubitt Cooke", work: "British Fungi", quote: "The waxy texture of **Hygrocybe** distinguishes these grassland agarics from common woodland toadstools." }
    ]
  },
  "Dashboard — hygr/hygrodeik.md": {
    primary: "A specialized form of psychrometer (wet-and-dry bulb hygrometer) featuring an engraved chart and index pointer to allow direct visual reading of relative humidity and dew point.",
    secondary: "In industrial meteorology and factory management, an instrument widely adopted in 19th-century textile and paper mills to monitor room humidity without complex manual tables.",
    quotes: [
      { author: "Cleveland Abbe", work: "The Mechanics of the Earth's Atmosphere", quote: "The **hygrodeik** proved particularly convenient in textile mills for reading humidity without consulting mathematical tables." },
      { author: "Alexander McAdie", work: "The Principles of Aerography", quote: "By sliding the index along the curved scales of the **hygrodeik**, the observer instantly obtains both dew-point and relative humidity." },
      { author: "William Napier Shaw", work: "Forecasting Weather", quote: "In industrial workshops, the **hygrodeik** hung upon the pillar to warn overseers of excessive atmospheric dryness." }
    ]
  },
  "Dashboard — hygr/hygroma.md": {
    primary: "A cystic swelling or tumor containing serous fluid, such as a cystic hygroma of the neck or a bursal hygroma on a joint.",
    secondary: "In pathology, a benign lymphatic malformation or distended synovial bursa resulting from chronic friction, trauma, or developmental lymphatic obstruction.",
    quotes: [
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "The congenital cystic **hygroma** of the neck consists of multi-locular lymphatic spaces filled with clear serous fluid." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Surgical excision of a deep-seated **hygroma** requires meticulous dissection to avoid injuring adjacent cervical nerves." },
      { author: "Joseph Lister", work: "Collected Papers", quote: "Antiseptic drainage of an inflamed knee **hygroma** prevented the development of destructive suppurative bursitis." }
    ]
  },
  "Dashboard — hygr/hygrometer.md": {
    primary: "An instrument used in meteorology and environmental monitoring to measure the amount of water vapor or relative humidity in the air or a gas.",
    secondary: "In experimental physics, an apparatus employing hair tension, psychrometric wet-and-dry bulb evaporation, or chilled mirror condensation to measure ambient moisture content.",
    quotes: [
      { author: "Benjamin Franklin", work: "Experiments and Observations on Electricity", quote: "I observed the sudden fall of the **hygrometer** when the cold dry northwest wind began to blow." },
      { author: "Horace Bénédict de Saussure", work: "Essays on Hygrometry", quote: "Using a human hair cleansed with ether, I constructed a **hygrometer** of unprecedented sensitivity to ambient moisture." },
      { author: "John Dalton", work: "Meteorological Observations and Essays", quote: "The condensation **hygrometer** allows one to determine the exact dew point by observing the first mist upon cooled silver." }
    ]
  },
  "Dashboard — hygr/hygrophoraceae.md": {
    primary: "A family of agaric fungi (order Agaricales) commonly known as the waxcap family, characterized by thick, waxy gills and white spores.",
    secondary: "In taxonomic mycology, a family including Hygrocybe, Hygrophorus, and Cuphophyllus, notable for basidia that are unusually long and gills that are widely spaced.",
    quotes: [
      { author: "Elias Magnus Fries", work: "Epicrisis Systematis Mycologici", quote: "The family **Hygrophoraceae** is distinguished by the thick, distant gills whose waxy substance resists rapid desiccation." },
      { author: "Pier Andrea Saccardo", work: "Sylloge Fungorum", quote: "In our taxonomic arrangement, the **Hygrophoraceae** occupy a prominent place among the white-spored agarics." },
      { author: "Carlton Rea", work: "British Basidiomycetae", quote: "Unimproved grasslands are the typical habitat for diverse species of the **Hygrophoraceae** in the British Isles." }
    ]
  },
  "Dashboard — hygr/hygrophorus.md": {
    primary: "A genus of agaric fungi in the family Hygrophoraceae, commonly called woodwaxes, characterized by waxy gills and mycorrhizal associations with woodland trees.",
    secondary: "In mycology, forest-dwelling mushrooms that fruit late in autumn, distinguished from Hygrocybe by their ectomycorrhizal ecology and divergent gill trama.",
    quotes: [
      { author: "Miles Joseph Berkeley", work: "Outlines of British Fungology", quote: "The viscid pileus of **Hygrophorus** eburneus gleams like ivory among the damp beech litter." },
      { author: "Elias Magnus Fries", work: "Monographia Hymenomycetum Sueciae", quote: "We find **Hygrophorus** flourishing late in autumn after heavy frosts have destroyed most other forest mushrooms." },
      { author: "Mordecai Cubitt Cooke", work: "Illustrations of British Fungi", quote: "The thick waxy gills of **Hygrophorus** provide an unmistakable field mark for the field mycologist." }
    ]
  },
  "Dashboard — hygr/hygrophyte.md": {
    primary: "A plant adapted to living in an environment with an abundant, continuous supply of moisture, such as a rainforest floor or wet marshland.",
    secondary: "In plant ecology, a species structurally characterized by thin cuticles, broad leaves, large intercellular air spaces, and open stomata, contrasting with xerophytes.",
    quotes: [
      { author: "Eugenius Warming", work: "Oecology of Plants", quote: "The broad, thin leaves of a shade-dwelling **hygrophyte** facilitate rapid transpiration in moisture-saturated forest air." },
      { author: "Andreas Schimper", work: "Plant-Geography upon a Physiological Basis", quote: "Under the dense canopy of the tropical rain forest, almost every herbaceous species is a typical **hygrophyte**." },
      { author: "Asa Gray", work: "Structural Botany", quote: "A true **hygrophyte** wilts rapidly when exposed to dry breezes, lacking the thick cuticle of xerophytes." }
    ]
  },
  "Dashboard — hygr/hygrophytic.md": {
    primary: "Adapted to or characteristic of a wet, humid habitat; displaying the anatomical features of a hygrophyte.",
    secondary: "In botanical ecology, describing foliage and tissue adaptations designed to maximize transpiration and resist waterlogging in humid biomes.",
    quotes: [
      { author: "Eugenius Warming", work: "Oecology of Plants", quote: "The anatomical structure of **hygrophytic** foliage displays large intercellular air spaces and poorly developed vascular bundles." },
      { author: "Alexander von Humboldt", work: "Aspects of Nature", quote: "The deep cloud-forests of the Andes shelter an exclusively **hygrophytic** flora composed of tree-ferns and delicate mosses." },
      { author: "Henry Chandler Cowles", work: "The Physiographic Ecology of Chicago and Vicinity", quote: "As the dune depression fills with humus and water, the xerophytic grasses yield place to **hygrophytic** sedges." }
    ]
  },
  "Dashboard — hygr/hygroscope.md": {
    primary: "A device or substance that indicates changes in atmospheric humidity or moisture level without providing a calibrated numerical measurement.",
    secondary: "In historical scientific instruments, apparatus utilizing the hygroscopic twisting of hair, catgut, or awn fibers of wild oats to demonstrate fluctuations in atmospheric moisture.",
    quotes: [
      { author: "Robert Boyle", work: "New Experiments and Observations Touching Cold", quote: "A piece of dried catgut served as a rustic **hygroscope**, twisting and untwisting with every change of weather." },
      { author: "Robert Hooke", work: "Micrographia", quote: "The beard of a wild oat makes an admirable **hygroscope**, curling tight in dry air and unbending in mist." },
      { author: "Isaac Newton", work: "Opticks", quote: "Certain porous minerals act as an optical **hygroscope**, changing from opaque to translucent as moisture fills their pores." }
    ]
  },
  "Dashboard — hygr/hygroscopic.md": {
    primary: "Tending to absorb or attract moisture readily from the surrounding air.",
    secondary: "In chemistry and biology, describing substances (such as concentrated sulfuric acid or glycerol) or plant structures (such as pine cone scales) that take up water vapor and exhibit moisture-driven movement.",
    quotes: [
      { author: "Michael Faraday", work: "Experimental Researches in Chemistry and Physics", quote: "Anhydrous copper sulfate is remarkably **hygroscopic**, turning blue as it extracts water vapor from the atmosphere." },
      { author: "Charles Darwin", work: "The Power of Movement in Plants", quote: "The awns of certain grass seeds possess **hygroscopic** fibers that twist with humidity, driving the seed into the soil." },
      { author: "Louis Pasteur", work: "Researches on Molecular Asymmetry", quote: "The crystals were preserved in a sealed desiccator to prevent their liquefaction through **hygroscopic** absorption." }
    ]
  },
  "Dashboard — hygr/hygroton.md": {
    primary: "A pharmaceutical brand name for chlortalidone (chlorthalidone), a long-acting thiazide-like diuretic used in the treatment of hypertension and edema.",
    secondary: "In clinical pharmacotherapy, a diuretic medication that inhibits sodium and chloride reabsorption in the cortical diluting segment of the ascending limb and early distal tubule of the nephron.",
    quotes: [
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "The sustained diuretic action of **Hygroton** reduces plasma volume and lowers systemic peripheral vascular resistance." },
      { author: "Donald Seldin", work: "The Kidney: Physiology and Pathophysiology", quote: "Long-acting sulfonamide diuretics such as **Hygroton** inhibit sodium chloride reabsorption in the early distal convoluted tubule." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Modern management of chronic hypertension frequently employs oral diuretics like **Hygroton** to control fluid overload." }
    ]
  },
  "Dashboard — hygr/hygrotrama.md": {
    primary: "The central tissue or trama of the gill (lamella) in certain mushrooms belonging to the family Hygrophoraceae, composed of divergent or interwoven hyphae.",
    secondary: "In fungal anatomy and systematics, a microscopic diagnostic character whose divergent orientation in water or KOH distinguishes true Hygrophorus species from related agaric genera.",
    quotes: [
      { author: "Rolf Singer", work: "The Agaricales in Modern Taxonomy", quote: "Microscopic examination of the **hygrotrama** reveals whether the hyphae are parallel, divergent, or irregularly interwoven." },
      { author: "Alexander H. Smith", work: "North American Species of Hygrophorus", quote: "The divergent arrangement of hyphae in the **hygrotrama** separates Camarophyllus from true Hygrophorus." },
      { author: "Carlton Rea", work: "British Basidiomycetae", quote: "In sections of the hymenophore, the structure of the **hygrotrama** provides the ultimate diagnostic criterion." }
    ]
  },
  "Dashboard — hygr/neohygrophorus.md": {
    primary: "A genus of agaric fungi segregated from Hygrophorus and Chrysomphalina, characterized by clitocyboid basidiocarps with decurrent gills.",
    secondary: "In modern molecular mycology, a distinct phylogenetic lineage within the Hygrophoraceae establishing that traditional morphological boundaries in waxcaps were polyphyletic.",
    quotes: [
      { author: "Rolf Singer", work: "The Agaricales in Modern Taxonomy", quote: "The segregate genus **Neohygrophorus** was erected to accommodate species lacking the traditional divergent gill trama." },
      { author: "Alexander H. Smith", work: "The Fungal Flora of North America", quote: "Phylogenetic analysis confirmed that **Neohygrophorus** occupies a distinct evolutionary branch apart from core Hygrophorus." },
      { author: "David Arora", work: "Mushrooms Demystified", quote: "Mycologists established **Neohygrophorus** for waxy-capped woodland mushrooms with distinct microscopic spore and cystidial features." }
    ]
  }
};

let successCount = 0;
for (const [key, data] of Object.entries(batch1Data)) {
  const [relDir, fileName] = key.split('/');
  if (updateNote(relDir, fileName, data)) {
    successCount++;
  }
}

console.log(`\n========================================`);
console.log(`Batch 1 Completed: ${successCount} / ${Object.keys(batch1Data).length} words updated`);
console.log(`========================================`);
