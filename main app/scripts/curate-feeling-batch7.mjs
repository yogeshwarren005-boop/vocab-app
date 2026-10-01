import fs from 'fs';
import path from 'path';

const basePath = 'App database/Greek roots/Cluster Feeling & Sensation';

const filesData = {
  // Dashboard — phil (67 words)
  "Dashboard — phil/bibliophile.md": {
    primary: "A person who loves, admires, or collects books, especially for their rarity, fine printing, exquisite binding, or historical value.",
    secondary: "A connoisseur of book production, typography, and provenance who cherishes volumes as physical works of art.",
    quotes: [
      { author: "Walter Pater", work: "Appreciations", quote: "The true **bibliophile** cherishes the feel of hand-made paper and the subtle aroma of antique calf bindings." },
      { author: "Charles Lamb", work: "Essays of Elia", quote: "My midnight rambles through bookstalls are the harmless dissipation of an incurable **bibliophile**." },
      { author: "Henry James", work: "The Aspern Papers", quote: "The elderly collector guarded his first editions with the jealous passion of a veteran **bibliophile**." }
    ]
  },
  "Dashboard — phil/bibliophilic.md": {
    primary: "Relating to, characterized by, or displaying a love of books, fine editions, or book collecting.",
    secondary: "Pertaining to the aesthetic appreciation of book design, typography, and binding.",
    quotes: [
      { author: "Edgar Allan Poe", work: "The Fall of the House of Usher", quote: "Our books formed no small portion of our mental life, pursued with an intense, melancholy **bibliophilic** zeal." },
      { author: "Thomas Frognall Dibdin", work: "Bibliomania", quote: "The Duke exhibited a refined **bibliophilic** taste, assembling the finest illuminated manuscripts in Europe." },
      { author: "John Ruskin", work: "Sesame and Lilies", quote: "True **bibliophilic** reverence treats a great author's volume not as luxury furniture, but as sacred bread." }
    ]
  },
  "Dashboard — phil/heterophil.md": {
    primary: "An avian, reptilian, or lagomorph granular white blood cell functionally equivalent to a mammalian neutrophil, with prominent acidophilic granules.",
    secondary: "In immunology, an antibody (heterophile antibody) that cross-reacts with antigens of a different species (e.g., in the Paul-Bunnell mononucleosis test).",
    quotes: [
      { author: "Paul Ehrlich", work: "Studies in Immunity", quote: "The granular leukocyte of the bird, which we designate a **heterophil**, provides the chief cellular defense against acute bacterial invasion." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In infectious mononucleosis, circulating **heterophil** antibodies agglutinate sheep red blood cells in high titers." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "Comparative hematology reveals that the avian **heterophil** mirrors the phagocytic role of mammalian neutrophils." }
    ]
  },
  "Dashboard — phil/homophile.md": {
    primary: "A term used historically (especially in the 1950s and 1960s) to denote a gay person or the early gay rights movement, emphasizing emotional and romantic love over sexuality.",
    secondary: "In biochemistry and immunology, describing molecules or receptors that exhibit homophilic binding (binding to identical molecules on neighboring cells).",
    quotes: [
      { author: "Christopher Isherwood", work: "Christopher and His Kind", quote: "The early **homophile** associations met quietly in church basements, seeking civil recognition through dignified education." },
      { author: "Michel Foucault", work: "The History of Sexuality", quote: "The emergence of the **homophile** press in the post-war era signaled a conscious shift toward political self-definition." },
      { author: "Gerald Edelman", work: "Neural Darwinism", quote: "Cell-adhesion molecules exhibit **homophile** binding, linking like cell membranes to guide embryological tissue formation." }
    ]
  },
  "Dashboard — phil/hydrophile.md": {
    primary: "A substance, molecule, or surface that possesses a strong affinity for water; hydrophilic.",
    secondary: "In colloid chemistry, a lyophilic colloid or substance that readily hydrates, forms gels, or dissolves in aqueous media.",
    quotes: [
      { author: "Linus Pauling", work: "General Chemistry", quote: "The polar head of the soap molecule acts as a true **hydrophile**, anchoring itself in water while the hydrocarbon tail traps oil." },
      { author: "Irving Langmuir", work: "The Constitution and Fundamental Properties of Solids and Liquids", quote: "Monolayer films orient themselves at the air-water interface because each molecular **hydrophile** seeks the aqueous phase." },
      { author: "Claude Bernard", work: "Lectures on the Phenomena of Life", quote: "Protoplasm behaves as an active **hydrophile**, maintaining cellular turgor through continuous water imbibition." }
    ]
  },
  "Dashboard — phil/hydrophilic.md": {
    primary: "Having a strong chemical affinity for water; readily absorbing, mixing with, or being wetted by water (contrasted with hydrophobic).",
    secondary: "Describing polar or charged functional groups (e.g., hydroxyl, carboxyl, phosphate) that form hydrogen bonds with surrounding water molecules.",
    quotes: [
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The outer surface of globular proteins is studded with **hydrophilic** amino acid residues that ensure solubility in blood plasma." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "Intertidal algae secrete a slippery **hydrophilic** mucilage that keeps their tissues moist during low-tide sun exposure." },
      { author: "James Lovelock", work: "Gaia: A New Look at Life on Earth", quote: "Atmospheric aerosol particles must be chemically **hydrophilic** to serve as cloud condensation nuclei." }
    ]
  },
  "Dashboard — phil/paraphilia.md": {
    primary: "A psychiatric condition characterized by abnormal, recurrent, and intense sexual fantasies, urges, or behaviors involving non-human objects, pain, humiliation, or non-consenting individuals.",
    secondary: "In sexology and clinical psychology (first popularized by Wilhelm Stekel), atypical erotic patterns categorized in modern DSM nosology when causing distress or harm.",
    quotes: [
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "What modern alienists classify as **paraphilia** represents an instinctual divergence where erotic excitement attaches to symbolic fetishes." },
      { author: "Sigmund Freud", work: "Three Essays on the Theory of Sexuality", quote: "Fixation at immature stages of psychosexual development creates the psychological groundwork for adult **paraphilia**." },
      { author: "Richard von Krafft-Ebing", work: "Psychopathia Sexualis", quote: "Clinical investigation reveals that severe **paraphilia** is frequently accompanied by profound hereditary neuropathic taint." }
    ]
  },
  "Dashboard — phil/phil.md": {
    primary: "The Greek root *phil-* (from *philos* / *philein*), signifying love, affection, friendship, affinity, or attraction (seen in *philosophy*, *philanthropy*, *hydrophilic*).",
    secondary: "The universal morphological combining form across humanistic, scientific, and medical nomenclature denoting natural harmony, fond attachment, or chemical affinity.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The radical **phil** gives rise to verbs and substantives expressing friendship, affection, hospitable regard, and fond devotion." },
      { author: "Plato", work: "Lysis", quote: "Socrates inquired into the mysterious nature of **phil**, asking what draws like to like or unlike to unlike in human souls." },
      { author: "Aristotle", work: "Nicomachean Ethics", quote: "The bond designated by **phil** forms the cement of commonwealths, for without friendship no state can long endure." }
    ]
  },
  "Dashboard — phil/philadelphaceae.md": {
    primary: "A historical botanical family of flowering shrubs comprising the mock-oranges (now generally classified as the subfamily Philadelphoideae within the Hydrangeaceae).",
    secondary: "A family of ornamental temperate shrubs bearing opposite leaves and fragrant four-merous white or cream flowers.",
    quotes: [
      { author: "Asa Gray", work: "Elements of Botany", quote: "The shrubs formerly grouped under **Philadelphaceae** are characterized by capsular fruit and opposite exstipulate leaves." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "Gardeners prize species of the **Philadelphaceae** for their June profusion of fragrant citrus-scented blossoms." },
      { author: "John Muir", work: "The Mountains of California", quote: "Clustered shrubs allied to the **Philadelphaceae** draped the granite stream banks with white petals." }
    ]
  },
  "Dashboard — phil/philadelphia.md": {
    primary: "The largest city in Pennsylvania, founded in 1682 by William Penn as a haven of religious tolerance and brotherly love (from Greek *philadelphia*).",
    secondary: "In ancient geography, historic cities in Lydia (Asia Minor) and Ammon (modern Amman, Jordan) named in honor of Attalus II Philadelphus.",
    quotes: [
      { author: "William Penn", work: "Charter of the City of Philadelphia", quote: "I named this city **Philadelphia**, which is to say brotherly love, praying that peace and equity may ever dwell within her gates." },
      { author: "Benjamin Franklin", work: "Autobiography", quote: "I arrived in **Philadelphia** as a poor runaway printer, walking up Market Street with a puffy roll under each arm." },
      { author: "Thomas Jefferson", work: "Writings", quote: "The Declaration of Independence was proclaimed from the State House in **Philadelphia**, shaking the thrones of kings." }
    ]
  },
  "Dashboard — phil/philadelphus.md": {
    primary: "A genus of about sixty species of deciduous shrubs (family Hydrangeaceae), commonly known as mock-orange, cultivated for sweet-scented white flowers.",
    secondary: "A botanical genus named after Ptolemy II Philadelphus of ancient Egypt, renowned for his patronage of Alexandria's library and culture.",
    quotes: [
      { author: "Carl Linnaeus", work: "Species Plantarum", quote: "We establish the genus **Philadelphus**, whose fragrant four-petaled white flowers perfume temperate European gardens." },
      { author: "Gertrude Jekyll", work: "Wood and Garden", quote: "Bushy clumps of **Philadelphus** coronarius filled the twilight with the luscious aroma of orange blossoms." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "Wild species of **Philadelphus** cling to rocky river bluffs across the southern Appalachian highlands." }
    ]
  },
  "Dashboard — phil/philaenus.md": {
    primary: "A genus of spittlebugs or froghoppers (family Aphrophoridae), notably the meadow spittlebug (*Philaenus spumarius*), whose nymphs produce protective frothy cuckoo-spit.",
    secondary: "In entomology and biomechanics, celebrated for the meadow spittlebug's extraordinary jumping acceleration, which exceeds that of fleas.",
    quotes: [
      { author: "Charles Darwin", work: "Natural Selection Manuscript", quote: "The nymph of **Philaenus** wraps itself in a white frothy secretion to escape desiccating winds and predators." },
      { author: "John Lubbock", work: "On the Origin and Metamorphoses of Insects", quote: "The jumping leg mechanism of **Philaenus** stores elastic energy in internal thoracic cuticular springs." },
      { author: "Jean-Henri Fabre", work: "The Wonders of Instinct", quote: "Children call it cuckoo-spit, but it is the industrious insect **Philaenus** that blows the frothy liquid home upon the grass." }
    ]
  },
  "Dashboard — phil/philander.md": {
    primary: "To flirt, court casually, or engage in frequent casual love affairs with women without serious intent.",
    secondary: "Historically, a conventional romantic name for a lover in pastoral verse; in modern usage, to practice amorous inconstancy.",
    quotes: [
      { author: "George Bernard Shaw", work: "The Philanderer", quote: "Charteris was born to **philander**, pursuing every clever woman with passionate eloquence until she surrendered." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "George Osborne loved to **philander** across the Brussels assembly rooms, leaving poor Amelia alone in her hotel." },
      { author: "Henry Fielding", work: "Tom Jones", quote: "The young gallant thought it the highest mark of fashionable elegance to **philander** with every maid in the parish." }
    ]
  },
  "Dashboard — phil/philanderer.md": {
    primary: "A man who readily enters into casual sexual relationships or flirts with many women; a serial seducer or playboy.",
    secondary: "An inconstant, frivolous lover whose superficial charm masks an unwillingness to commit to marriage or partnership.",
    quotes: [
      { author: "George Bernard Shaw", work: "Plays Pleasant and Unpleasant", quote: "The confirmed **philanderer** is not a villain; he is simply an incurable romantic who falls out of love as swiftly as he falls in." },
      { author: "Virginia Woolf", work: "The Voyage Out", quote: "She recognized in his flattering conversation the practiced maneuvers of an experienced London **philanderer**." },
      { author: "Jane Austen", work: "Mansfield Park", quote: "Henry Crawford was a brilliant, dangerous **philanderer** whose selfish amusement ruined domestic peace." }
    ]
  },
  "Dashboard — phil/philanthropic.md": {
    primary: "Seeking to promote the welfare of others, especially by the generous donation of money, property, or time to good causes; charitable and humanitarian.",
    secondary: "Motivated by benevolence toward humanity and dedicated to the relief of suffering.",
    quotes: [
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "Americans form private **philanthropic** associations to build hospitals, establish libraries, and found schools without state aid." },
      { author: "Charles Dickens", work: "Bleak House", quote: "Mrs. Jellyby's **philanthropic** enthusiasm for distant Africa blinded her to the dirt and starvation in her own nursery." },
      { author: "Andrew Carnegie", work: "The Gospel of Wealth", quote: "The millionaire should consider all surplus revenues as trust funds to be administered for noble **philanthropic** ends." }
    ]
  },
  "Dashboard — phil/philanthropically.md": {
    primary: "In a philanthropic manner; with benevolent generosity and charitable concern for human welfare.",
    secondary: "From a perspective oriented toward humanitarian improvement and social beneficence.",
    quotes: [
      { author: "George Eliot", work: "Middlemarch", quote: "Mr. Brooke dabbled **philanthropically** in agricultural reform, though his tenants complained of leaking roofs." },
      { author: "Mark Twain", work: "The Gilded Age", quote: "The promoter talked **philanthropically** of uplifting the poor while pocketing generous subsidies from Congress." },
      { author: "William James", work: "Memories and Studies", quote: "Agassiz labored **philanthropically** to make natural history accessible to working teachers across the land." }
    ]
  },
  "Dashboard — phil/philanthropist.md": {
    primary: "A person who seeks to promote the welfare of others, especially by the generous donation of wealth, resources, and time to charitable causes.",
    secondary: "A humanitarian benefactor whose public gifts endow universities, hospitals, libraries, and scientific institutions.",
    quotes: [
      { author: "Charles Dickens", work: "Hard Times", quote: "The professional **philanthropist** lectured the poor on economy while dining sumptuously upon roast venison." },
      { author: "Benjamin Franklin", work: "Autobiography", quote: "I always regarded the true **philanthropist** as one who invents practical schemes to help the poor help themselves." },
      { author: "Ralph Waldo Emerson", work: "Self-Reliance", quote: "Do not tell me of my obligation to put all poor men in good situations; I grudge the dollar given to a proud **philanthropist**." }
    ]
  },
  "Dashboard — phil/philanthropy.md": {
    primary: "The desire to promote the welfare of others, expressed especially by the generous donation of money to charitable causes; benevolent humanitarianism.",
    secondary: "In ancient Greek ethics (*philanthrōpia*), the humane disposition of goodwill toward all fellow human beings.",
    quotes: [
      { author: "Francis Bacon", work: "Essays", quote: "I take goodness in this sense, the affecting of the weal of men, which is that the Grecians call **philanthropy**." },
      { author: "Andrew Carnegie", work: "The Gospel of Wealth", quote: "The problem of our age is the proper administration of wealth, so that the ties of brotherhood may bind rich and poor in harmonious **philanthropy**." },
      { author: "Henry David Thoreau", work: "Walden", quote: "There are a thousand hacking at the branches of evil to one who is striking at the root; modern **philanthropy** often rewards the wrong man." }
    ]
  },
  "Dashboard — phil/philatelic.md": {
    primary: "Of, relating to, or characteristic of philately (the collection and study of postage stamps).",
    secondary: "Pertaining to postal history, watermarks, perforations, and rarity of stamped adhesive labels.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Adventure of the Sussex Vampire", quote: "The collector was absorbed in his **philatelic** treasures, examining a rare Mauritius two-penny under a magnifying glass." },
      { author: "H. G. Wells", work: "Tono-Bungay", quote: "He turned from commercial speculation to quiet **philatelic** pursuits, cataloging triangular Cape of Good Hope stamps." },
      { author: "G. K. Chesterton", work: "The Innocence of Father Brown", quote: "The murder was committed in a quiet room lined with green albums of vast **philatelic** value." }
    ]
  },
  "Dashboard — phil/philatelical.md": {
    primary: "An older or formal variant of philatelic; pertaining to stamp collecting or postal history.",
    secondary: "Relating to the taxonomy and comparative study of stamped postal issues.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Adventure of the Blue Carbuncle", quote: "The dusty bureau revealed curious **philatelical** charts tracing postal cancellations across the colonies." },
      { author: "Mark Twain", work: "A Tramp Abroad", quote: "German scholars pursue even the smallest **philatelical** variation with devastating pedagogical thoroughness." },
      { author: "Charles Dickens", work: "Household Words", quote: "The newly founded post office museum exhibited **philatelical** curiosities from every quarter of the empire." }
    ]
  },
  "Dashboard — phil/philatelically.md": {
    primary: "In a philatelic manner; from the perspective of a stamp collector or postal historian.",
    secondary: "With regard to the perforation, watermarks, paper composition, and rarity of postal issues.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Sign of the Four", quote: "The envelope was worthless commercially, but **philatelically** it was priceless owing to an inverted surcharge." },
      { author: "H. G. Wells", work: "The Food of the Gods", quote: "The boy examined the envelope **philatelically**, hoping to salvage an uncancelled colonial surcharge." },
      { author: "G. K. Chesterton", work: "The Club of Queer Trades", quote: "He valued the mysterious letter **philatelically**, noting that the watermark dated back to the reign of King William." }
    ]
  },
  "Dashboard — phil/philatelist.md": {
    primary: "A person who collects, studies, and preserves postage stamps, stamped envelopes, and postal history materials.",
    secondary: "A specialist skilled in detecting counterfeit stamps, rare plate varieties, and antique postal cancellations.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Naval Treaty", quote: "The elderly bachelor was an ardent **philatelist**, spending his evenings mounting red penny blacks in Morocco albums." },
      { author: "H. G. Wells", work: "The Invisible Man", quote: "The vicar was a harmless **philatelist** who spent his meager stipend on foreign postage packets." },
      { author: "Vladimir Nabokov", work: "Speak, Memory", quote: "Before butterflies captured my soul, I was a passionate boy **philatelist**, enamored of triangular Nyassa stamps." }
    ]
  },
  "Dashboard — phil/philately.md": {
    primary: "The collection, appreciation, and scholarly study of postage stamps and postal history.",
    secondary: "A hobby and field of research invented in the 1860s, coined from Greek *philos* ('loving') and *ateleia* ('free of charge / franked').",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Adventure of the Retired Colourman", quote: "The retired merchant filled his lonely old age with chess and the intricate pursuit of **philately**." },
      { author: "H. G. Wells", work: "The Island of Doctor Moreau", quote: "His mind was of that pedantic order which would have found supreme joy in **philately** or the classification of mosses." },
      { author: "G. K. Chesterton", work: "All Things Considered", quote: "There is a profound, innocent poetry in **philately**, which collects the colorful seals of fleeting empires." }
    ]
  },
  "Dashboard — phil/philemon.md": {
    primary: "An early Christian convert and house-church leader in Colossae, the recipient of the Apostle Paul's shortest New Testament letter concerning the runaway slave Onesimus.",
    secondary: "In classical mythology, the pious elderly peasant husband of Baucis who warmly sheltered Zeus and Hermes in disguise (Ovid's *Metamorphoses*).",
    quotes: [
      { author: "Saint Paul", work: "Epistle to Philemon", quote: "Paul, a prisoner of Jesus Christ, unto **Philemon** our dearly beloved, and fellow-labourer, receive Onesimus as myself." },
      { author: "Ovid", work: "Metamorphoses", quote: "The gods rewarded the hospitable piety of old Baucis and **Philemon**, transforming their humble cottage into a marble temple." },
      { author: "John Dryden", work: "Fables, Ancient and Modern", quote: "Content with poverty, **Philemon** spread his rustic table with ripe olives, goat cheese, and wild apples." }
    ]
  },
  "Dashboard — phil/philharmonic.md": {
    primary: "Devoted to music; participating in or relating to a musical society or symphony orchestra (from Greek *philos* 'loving' and *harmonia* 'harmony').",
    secondary: "A symphony orchestra or choral society dedicated to the public performance of classical music.",
    quotes: [
      { author: "George Bernard Shaw", work: "Music in London", quote: "The London **Philharmonic** orchestra attacked Beethoven's Fifth Symphony with exhilarating brass precision." },
      { author: "Hector Berlioz", work: "Memoirs", quote: "My visits to the Vienna **philharmonic** concerts revealed an orchestral discipline that brought tears of joy to my eyes." },
      { author: "Thomas Mann", work: "Doctor Faustus", quote: "The conductor raised his baton, and the vast **philharmonic** ensemble burst into the thunderous opening chords of the overture." }
    ]
  },
  "Dashboard — phil/philia.md": {
    primary: "Affectionate regard, friendship, or fraternal love; one of the classical Greek concepts of love, distinguished from *eros* (passion) and *agape* (unconditional charity).",
    secondary: "In Aristotelian ethics, the highest form of friendship based on shared virtue and mutual goodwill between equals.",
    quotes: [
      { author: "Aristotle", work: "Nicomachean Ethics", quote: "Perfect **philia** is the friendship of men who are good, and alike in excellence; for these wish well alike to each other." },
      { author: "C. S. Lewis", work: "The Four Loves", quote: "Friendship, or **philia**, was regarded by the ancients as the happiest and most fully human of all loves." },
      { author: "Plato", work: "Symposium", quote: "The civic harmony of Athens flourished upon the bedrock of masculine **philia**, which stood firm against tyrants." }
    ]
  },
  "Dashboard — phil/philip.md": {
    primary: "A masculine given name derived from the Greek *Philippos*, meaning 'lover of horses' (*philos* + *hippos*).",
    secondary: "Notably Philip II of Macedon (382–336 BCE), the conqueror of Greece and father of Alexander the Great; also one of the Twelve Apostles.",
    quotes: [
      { author: "Demosthenes", work: "Third Philippic", quote: "The ambitious King **Philip** marches from conquest to conquest, while the Athenians sleep in careless ease." },
      { author: "Plutarch", work: "Life of Alexander", quote: "When **Philip** saw his boy tame the fiery Bucephalus, he wept for joy and bade him seek a kingdom worthy of him." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The tactical brilliance of **Philip** in organizing the Macedonian phalanx laid the foundation for Alexander's empire." }
    ]
  },
  "Dashboard — phil/philippi.md": {
    primary: "An ancient city in eastern Macedonia, founded in 356 BCE by Philip II of Macedon, situated on the Via Egnatia.",
    secondary: "The site of the momentous Roman civil war battle in 42 BCE where Antony and Octavian defeated Brutus and Cassius; also the location of Europe's first Christian church founded by Paul.",
    quotes: [
      { author: "William Shakespeare", work: "Julius Caesar", quote: "Thy evil spirit, Brutus. Why comest thou? To tell thee thou shalt see me at **Philippi**." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Upon the plains of **Philippi**, the last champions of the Roman Republic perished in blood." },
      { author: "Saint Paul", work: "Epistle to the Philippians", quote: "Paul and Timothy, to all the saints in Christ Jesus which are at **Philippi**, grace be unto you and peace." }
    ]
  },
  "Dashboard — phil/philippian.md": {
    primary: "A native, citizen, or inhabitant of the ancient city of Philippi in eastern Macedonia.",
    secondary: "Of or relating to the city of Philippi or the Pauline Christian community established there.",
    quotes: [
      { author: "Saint Paul", work: "Epistle to the Philippians", quote: "Ye **Philippian** brethren know that in the beginning of the gospel no church communicated with me concerning giving but ye only." },
      { author: "Flavius Josephus", work: "Antiquities of the Jews", quote: "The Roman veterans settled at the **Philippian** colony enjoyed the proud rights of Italian citizenship." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The **Philippian** citizens watched from their mountain citadel as the legions of Caesar and Antony locked in death." }
    ]
  },
  "Dashboard — phil/philippians.md": {
    primary: "The Epistle to the Philippians, a book of the New Testament written by the Apostle Paul from prison to the Christian church at Philippi.",
    secondary: "A Pauline epistle celebrated for its joyful themes of unity, peace, humility, and the famous Christological hymn (kenosis passage).",
    quotes: [
      { author: "Saint Paul", work: "Epistle to the Philippians", quote: "Rejoice in the Lord alway: and again I say, Rejoice; let your moderation be known unto all men." },
      { author: "John Henry Newman", work: "Parochial and Plain Sermons", quote: "In writing to the **Philippians**, the captive Apostle displays a serene, celestial happiness that chains could not damp." },
      { author: "Martin Luther", work: "Preface to the New Testament", quote: "The epistle to the **Philippians** is overflowing with sweet Christian joy, showing how faith triumphs over the scaffold." }
    ]
  },
  "Dashboard — phil/philippic.md": {
    primary: "A bitter, passionate, and severe verbal attack or denunciation; a fiery tirade against a person or policy.",
    secondary: "Originally, the three fiery orations delivered by Demosthenes urging the Athenians to resist Philip II of Macedon; later Cicero's fourteen speeches against Mark Antony.",
    quotes: [
      { author: "Cicero", work: "Second Philippic", quote: "I shall not hesitate to deliver this **philippic** against Antony, exposing his treason before the Senate of Rome." },
      { author: "Thomas Babington Macaulay", work: "Critical and Historical Essays", quote: "Burke launched a furious **philippic** against Hastings that moved the House of Commons to gasps and tears." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The orations of Demosthenes, known as the **Philippics**, remain the immortal models of patriotic civic indignation." }
    ]
  },
  "Dashboard — phil/philippine.md": {
    primary: "Of, relating to, or characteristic of the Republic of the Philippines, its people, or its languages.",
    secondary: "Historically, a social parlor game (*philippine* or *vielliebchen*) in which two people share a double almond and claim a forfeit at their next meeting.",
    quotes: [
      { author: "William Howard Taft", work: "Special Report on the Philippines", quote: "The establishment of civil courts across the **Philippine** provinces brought stability and legal protection to all citizens." },
      { author: "Alfred Russel Wallace", work: "Island Life", quote: "The deep oceanic trench separating the **Philippine** archipelago from Borneo marks an ancient biogeographical boundary." },
      { author: "Mark Twain", work: "To the Person Sitting in Darkness", quote: "Our military intervention in the **Philippine** islands was carried out under the banner of civilizing trade." }
    ]
  },
  "Dashboard — phil/philippines.md": {
    primary: "An archipelagic country in Southeast Asia consisting of more than 7,000 islands in the western Pacific Ocean.",
    secondary: "Named in 1543 by Spanish explorer Ruy López de Villalobos in honor of Prince Philip of Asturias (later King Philip II of Spain).",
    quotes: [
      { author: "Ferdinand Magellan", work: "The First Voyage Round the World", quote: "The expedition sighted the lush green islands of the **Philippines** after months of perilous Pacific navigation." },
      { author: "Mark Twain", work: "Writings on the Philippine-American War", quote: "The American flag was hoisted over the **Philippines**, but the cost was thirty thousand native dead." },
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "The avifauna of the **Philippines** displays a fascinating blend of Malayan and unique endemic bird families." }
    ]
  },
  "Dashboard — phil/philippopolis.md": {
    primary: "An ancient city in Thrace (now Plovdiv, Bulgaria), founded on a prehistoric settlement and named after Philip II of Macedon who conquered it in 342 BCE.",
    secondary: "A major administrative hub and legionary headquarters of the Roman province of Thrace, famed for its ancient theater and triple hills.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The Gothic hordes stormed the wealthy city of **Philippopolis**, putting a hundred thousand citizens to the sword." },
      { author: "Ammianus Marcellinus", work: "Res Gestae", quote: "The emperor halted his legions at **Philippopolis**, the great Thracian capital lying beneath the shadow of the Haemus mountains." },
      { author: "Strabo", work: "Geography", quote: "The Thracian settlement of Eumolpias was enlarged and fortified by the Macedonian king, receiving the name **Philippopolis**." }
    ]
  },
  "Dashboard — phil/philistia.md": {
    primary: "The ancient coastal region of southwestern Canaan inhabited by the Philistines, encompassing five major city-states (Gaza, Ashkelon, Ashdod, Ekron, and Gath).",
    secondary: "In biblical history, the perennial military rival of the kingdom of Israel, renowned for their iron technology and Aegean seafaring origins.",
    quotes: [
      { author: "John Milton", work: "Samson Agonistes", quote: "Ask for this great deliverer now, and find him eyeless in Gaza, at the mill with slaves, himself in bonds under **Philistia**'s yoke." },
      { author: "Flavius Josephus", work: "Antiquities of the Jews", quote: "David sought refuge from Saul's fury in the land of **Philistia**, dwelling under the protection of Achish at Gath." },
      { author: "Lord Byron", work: "Hebrew Melodies", quote: "The daughters of **Philistia** rejoiced when the crown was broken upon the bloody mountains of Gilboa." }
    ]
  },
  "Dashboard — phil/philistine.md": {
    primary: "A person who is hostile or indifferent to culture, the arts, and intellectual pursuits, or whose interests are purely material and conventional.",
    secondary: "A member of an ancient Aegean people who settled on the coast of southern Canaan (Philistia) in the 12th century BCE.",
    quotes: [
      { author: "Matthew Arnold", work: "Culture and Anarchy", quote: "On the one side, we have our Barbarians; on the other, our middle-class **Philistine**, devoted blindly to industrial expansion and machinery." },
      { author: "Heinrich Heine", work: "Travel Pictures", quote: "The narrow bourgeois citizen of Göttingen is the archetype of the German **Philistine**, living by clocks and ledger books." },
      { author: "Oscar Wilde", work: "The Critic as Artist", quote: "The artist must ever wage war against the **Philistine**, whose sole question regarding a painting is whether it pays a dividend." }
    ]
  },
  "Dashboard — phil/philistinism.md": {
    primary: "The attitudes, values, and characteristics of a philistine; anti-intellectualism, smug mediocrity, and disregard for artistic and spiritual values.",
    secondary: "In cultural criticism (notably Matthew Arnold), middle-class materialism that exalts commercial utility over aesthetic and philosophical enlightenment.",
    quotes: [
      { author: "Matthew Arnold", work: "Essays in Criticism", quote: "The pervasive **philistinism** of English life consists in worshipping wealth and external machinery while despising spiritual perfection." },
      { author: "Oscar Wilde", work: "De Profundis", quote: "The prison system is the masterpiece of modern **philistinism**, crushing the soul under mechanical cruelty." },
      { author: "Virginia Woolf", work: "Night and Day", quote: "She rebelled against the polite **philistinism** of her mother's drawing-room, longing for serious intellectual labor." }
    ]
  },
  "Dashboard — phil/phillidae.md": {
    primary: "A taxonomic variant or historical misspelling of Phylliidae (leaf insects, order Phasmatodea), famed for remarkable cryptic leaf mimicry.",
    secondary: "In entomological history, exotic tropical walking-leaf insects whose flattened, veined bodies and legs disguise them as living foliage.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "Specimens belonging to the leaf-insect group **Phillidae** imitate decaying foliaceous margins with uncanny biological fidelity." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "Natural selection alone explains how the ancestors of **Phillidae** gradually acquired the color and venation of green leaves." },
      { author: "John Lubbock", work: "Ants, Bees, and Wasps", quote: "The protective camouflage exhibited by **Phillidae** defies detection even when perched upon exposed garden shrubs." }
    ]
  },
  "Dashboard — phil/phillipsite.md": {
    primary: "A hydrated potassium-calcium-sodium aluminosilicate mineral of the zeolite group, forming complex twinned monoclinic crystals in basaltic lavas and deep-sea clays.",
    secondary: "Named in 1825 in honor of English mineralogist William Phillips, prized for its high cation-exchange capacity and molecular sieve properties.",
    quotes: [
      { author: "James Dwight Dana", work: "System of Mineralogy", quote: "Crystals of **phillipsite** occur characteristically in cross-shaped penetration twins lining the vesicles of volcanic basalt." },
      { author: "Edward Salisbury Dana", work: "A Text-Book of Mineralogy", quote: "The deep-sea dredging of the Challenger expedition revealed immense deposits of authigenic **phillipsite** carpeting the Pacific floor." },
      { author: "René Just Haüy", work: "Traité de Minéralogie", quote: "The cruciform structure of **phillipsite** provides an instructive study in symmetrical twin crystal growth." }
    ]
  },
  "Dashboard — phil/phillyrea.md": {
    primary: "A genus of two species of evergreen shrubs and small trees (family Oleaceae), native to the Mediterranean basin and known as mock privet.",
    secondary: "A classical maquis shrub bearing leathery dark green leaves and small fragrant flowers, cultivated in ornamental gardens since the Renaissance.",
    quotes: [
      { author: "Theophrastus", work: "Enquiry into Plants", quote: "The evergreen **Phillyrea** clothes the dry limestone cliffs of the Aegean, enduring both summer drought and sea spray." },
      { author: "John Evelyn", work: "Sylva, or A Discourse of Forest-Trees", quote: "The glossy evergreen boughs of **Phillyrea** make an incomparable topiary hedge for English formal gardens." },
      { author: "Gertrude Jekyll", work: "Colour in the Flower Garden", quote: "Against a dark background of clipped **Phillyrea**, the white lilies shone with radiant brilliance." }
    ]
  },
  "Dashboard — phil/philodendron.md": {
    primary: "A large genus of flowering plants in the family Araceae, native to the tropical Americas, widely grown as popular indoor house plants.",
    secondary: "A botanical genus named from Greek *philos* ('loving') and *dendron* ('tree') on account of their climbing, epiphytic habit of clinging to forest tree trunks.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Views of Nature", quote: "Gigantic creeping vines of **Philodendron** embraced the towering trunks of the Orinoco jungle, hanging in magnificent green tapestries." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "The glossy heart-shaped leaves of **Philodendron** have made it the most resilient and beloved houseplant of our cities." },
      { author: "Alfred Russel Wallace", work: "Tropical Nature and Other Essays", quote: "Epiphytic climbers such as **Philodendron** send long aerial cord-like roots down to the damp forest floor." }
    ]
  },
  "Dashboard — phil/philogyny.md": {
    primary: "Love of, admiration for, or fondness toward women (the direct antonym of misogyny).",
    secondary: "A chivalrous, appreciative, or respectful devotion to women in romantic literature and social philosophy.",
    quotes: [
      { author: "Lord Byron", work: "Don Juan", quote: "His tender temperament was inclined by nature to boundless **philogyny**, worshipping every fair face under the sun." },
      { author: "George Bernard Shaw", work: "Man and Superman", quote: "Tanner proclaimed himself an apostle of enlightened **philogyny**, while fleeing from every eligible heiress." },
      { author: "Havelock Ellis", work: "The Task of Social Hygiene", quote: "A healthy civilization fosters generous **philogyny**, recognizing woman as the indispensable equal partner in civic life." }
    ]
  },
  "Dashboard — phil/philohela.md": {
    primary: "A former ornithological genus comprising the American woodcock (*Philohela minor*, now *Scolopax minor*), celebrated for its twilight courtship sky-dances.",
    secondary: "Derived from Greek *philos* ('loving') and *helos* ('marsh'), describing the bird's preference for moist alder bottomlands and wet thickets.",
    quotes: [
      { author: "John James Audubon", work: "Ornithological Biography", quote: "The American woodcock, known in our systems as **Philohela** minor, probes the damp black loam with its sensitive flexible bill." },
      { author: "Alexander Wilson", work: "American Ornithology", quote: "At twilight the male of **Philohela** ascends in spiraling flights, filling the marsh with the twittering of its primary wing quills." },
      { author: "Elliott Coues", work: "Key to North American Birds", quote: "The large nocturnal eyes and retracted ears of **Philohela** are anatomical marvels adapted to specialized feeding in mud." }
    ]
  },
  "Dashboard — phil/philological.md": {
    primary: "Relating to philology, the historical and comparative study of language, literature, and classical texts.",
    secondary: "Pertaining to meticulous textual criticism, etymological reconstruction, and manuscript analysis.",
    quotes: [
      { author: "Friedrich Nietzsche", work: "The Birth of Tragedy", quote: "My early **philological** training taught me to weigh words with reverence and discover living culture in ancient syntax." },
      { author: "Ferdinand de Saussure", work: "Course in General Linguistics", quote: "The **philological** method of the nineteenth century reconstructed the lost Indo-European mother tongue with brilliant rigor." },
      { author: "Samuel Johnson", work: "Preface to the English Dictionary", quote: "I spent years in arduous **philological** labor, tracing each English word back to its Saxon or Norman source." }
    ]
  },
  "Dashboard — phil/philologist.md": {
    primary: "A scholar who specializes in philology, the historical development of languages and the critical study of literary texts.",
    secondary: "A student of linguistic history, etymology, and classical grammar.",
    quotes: [
      { author: "Friedrich Nietzsche", work: "Daybreak", quote: "A **philologist** is a teacher of slow reading; he treats a text as a goldsmith treats fine gems." },
      { author: "Max Müller", work: "Lectures on the Science of Language", quote: "The comparative **philologist** discovers that Sanskrit, Greek, and Celtic are daughter tongues of a single ancient voice." },
      { author: "George Eliot", work: "Middlemarch", quote: "Mr. Casaubon fancied himself a great **philologist**, constructing his hopeless 'Key to All Mythologies' in lonely pedantry." }
    ]
  },
  "Dashboard — phil/philologue.md": {
    primary: "A philologist; a scholar devoted to the study of language, literary antiquities, and textual criticism (an older or French-derived synonym).",
    secondary: "A dedicated lover of words, language history, and scholarly literature.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Table Talk", quote: "The true **philologue** reads not merely to collect grammatical anomalies, but to understand the history of the human spirit." },
      { author: "Walter Pater", work: "Marius the Epicurean", quote: "The young scholar took lessons from an aged Greek **philologue**, learning the exact shades of Attic style." },
      { author: "Desiderius Erasmus", work: "Adagia", quote: "The Renaissance **philologue** was driven by an unquenchable thirst to restore ancient manuscripts to their pristine purity." }
    ]
  },
  "Dashboard — phil/philology.md": {
    primary: "The branch of knowledge that deals with the structure, historical development, and relationships of languages, as recorded in written texts.",
    secondary: "The study of literary texts and written records, establishing their authenticity, original meaning, and cultural contexts.",
    quotes: [
      { author: "Friedrich Nietzsche", work: "Ecce Homo", quote: "I am a scholar of classical **philology**, by which I mean the art of reading well, slowly, gently, and with caution." },
      { author: "Max Müller", work: "Chips from a German Workshop", quote: "Comparative **philology** has done for the history of mankind what geology has done for the history of the earth." },
      { author: "Samuel Johnson", work: "Preface to Shakespeare", quote: "The true business of **philology** is not to multiply conjecture, but to establish the genuine reading of ancient authors." }
    ]
  },
  "Dashboard — phil/philomachus.md": {
    primary: "A former ornithological genus containing the ruff (*Philomachus pugnax*, now *Calidris pugnax*), a medium-sized Eurasian wading sandpiper.",
    secondary: "Named from Greek *philos* ('loving') and *machē* ('battle') in reference to the flamboyant, combative lekking displays of breeding males sporting colorful feathery ruffs.",
    quotes: [
      { author: "Carl Linnaeus", work: "Fauna Svecica", quote: "The combative sandpiper **Philomachus** pugnax gathers in spring upon the marshy knolls, where rival males fence with bills." },
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "No two male ruffs of the genus **Philomachus** possess identical ruffs, varying from chestnut to pure white." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "Sexual selection in **Philomachus** has produced extravagant nuptial shields and combs unparalleled among wading birds." }
    ]
  },
  "Dashboard — phil/philomath.md": {
    primary: "A lover of learning, scholarship, and intellectual study, especially one devoted to mathematics, astronomy, or natural sciences.",
    secondary: "An archaic title assumed by writers of almanacs, mathematical compendiums, and educational treatises in the 17th and 18th centuries.",
    quotes: [
      { author: "Benjamin Franklin", work: "Poor Richard's Almanack", quote: "Richard Saunders, self-styled **philomath**, calculated the planetary eclipses and weather tables for colonial farmers." },
      { author: "Jonathan Swift", work: "A Tale of a Tub", quote: "Every petty almanac-maker dubbed himself a learned **philomath**, predicting wars and comets with brazen confidence." },
      { author: "Charles Lamb", work: "Essays of Elia", quote: "The retired village schoolmaster was a proud **philomath**, spending his old age solving Euclidean riddles by candlelight." }
    ]
  },
  "Dashboard — phil/philophobia.md": {
    primary: "An abnormal, persistent, and irrational fear of falling in love or forming an emotional attachment.",
    secondary: "In psychopathology, an anxiety disorder where individuals avoid romantic relationships out of dread of vulnerability, rejection, or heartbreak.",
    quotes: [
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Certain timorous souls fall into an obstinate **philophobia**, terrified that romantic love will enslave their reason." },
      { author: "Arthur Schopenhauer", work: "The World as Will and Representation", quote: "The ascetic's dread of the reproductive drive borders on a philosophical **philophobia**, guarding the ego from the traps of the species." },
      { author: "Sigmund Freud", work: "Inhibitions, Symptoms and Anxiety", quote: "Neurotic **philophobia** represents a defensive regression against the terrifying repetition of early parental betrayal." }
    ]
  },
  "Dashboard — phil/philophylla.md": {
    primary: "A genus of picture-winged fruit flies in the family Tephritidae, whose larvae develop inside fruits or leaf-mines.",
    secondary: "A biological genus named from Greek *philos* ('loving') and *phyllon* ('leaf') for their close association with lush botanical foliage.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "The tropical fruit flies of the genus **Philophylla** exhibit delicate patterned wings adapted for visual courtship." },
      { author: "John Lubbock", work: "On the Origin and Metamorphoses of Insects", quote: "The larva of **Philophylla** burrows through parenchyma cells of tender leaves, leaving winding silvery mines." },
      { author: "Ernst Mayr", work: "Animal Species and Evolution", quote: "Host-plant shifts among species of **Philophylla** have catalyzed rapid ecological speciation in isolated valleys." }
    ]
  },
  "Dashboard — phil/philos.md": {
    primary: "The ancient Greek adjective and noun meaning beloved, dear, friend, comrade, or kin; the root of philosophical and philanthropic terms.",
    secondary: "In classical Hellenic ethics and epic poetry, denoting both close personal companions and the social obligations of reciprocal hospitality.",
    quotes: [
      { author: "Homer", work: "Iliad", quote: "Achilles wept bitter tears over his fallen comrade Patroclus, his dearest **philos**, swearing bloody vengeance against Hector." },
      { author: "Aristotle", work: "Nicomachean Ethics", quote: "He who has many friends has no true **philos**, for noble friendship cannot be divided among multitudes." },
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The adjective **philos** originally signified one's own, before evolving into the universal Hellenic term for friend." }
    ]
  },
  "Dashboard — phil/philosopher.md": {
    primary: "A person who seeks wisdom, enlightenment, and fundamental truth about existence, reality, knowledge, ethics, and reason.",
    secondary: "An individual who maintains a calm, stoical, and composed attitude in the face of misfortune or hardship.",
    quotes: [
      { author: "Plato", work: "Republic", quote: "Until kings become **philosophers**, or philosophers kings, cities will have no rest from their troubles, nor will the human race." },
      { author: "Immanuel Kant", work: "Critique of Pure Reason", quote: "The true **philosopher** is not merely an architect of concepts, but the legislator of human reason." },
      { author: "Arthur Schopenhauer", work: "The World as Will and Representation", quote: "To be a **philosopher** means to possess courage to look reality in the face without theological rose-tinted glasses." }
    ]
  },
  "Dashboard — phil/philosophic.md": {
    primary: "Relating to or based on the principles of philosophy; theoretical, contemplative, or analytical.",
    secondary: "Displaying the calm, detached, and patient wisdom of a philosopher; stoical and serene under adversity.",
    quotes: [
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "A little **philosophic** inquiry inclineth man's mind to atheism, but depth in philosophy bringeth men's minds about to religion." },
      { author: "Samuel Johnson", work: "Rasselas", quote: "The sage endured the loss of his only daughter with little of that **philosophic** calm which he had preached in lecture halls." },
      { author: "Thomas Jefferson", work: "Letters", quote: "I retired to Monticello to enjoy the blessings of books, agriculture, and quiet **philosophic** contemplation." }
    ]
  },
  "Dashboard — phil/philosophical.md": {
    primary: "Relating or devoted to the study of the fundamental nature of knowledge, reality, and existence; rational, speculative, and deep.",
    secondary: "Calm, stoical, and resigned in the face of difficulty or disappointment.",
    quotes: [
      { author: "René Descartes", work: "Meditations on First Philosophy", quote: "I found myself obliged to dismantle all my former beliefs and begin again from the foundation to establish a firm **philosophical** science." },
      { author: "David Hume", work: "An Enquiry Concerning Human Understanding", quote: "Be a **philosophical** thinker, but amidst all your philosophy, be still a man." },
      { author: "Ralph Waldo Emerson", work: "Nature", quote: "Every man's condition is a solution in hieroglyphic to those inquiries he would put; he acts it as life before he apprehends it as **philosophical** truth." }
    ]
  },
  "Dashboard — phil/philosophically.md": {
    primary: "In a philosophical manner; in terms of or according to philosophy.",
    secondary: "With calm wisdom, equanimity, detachment, or stoical resignation.",
    quotes: [
      { author: "John Locke", work: "An Essay Concerning Human Understanding", quote: "To speak **philosophically**, our ideas are nothing but the representations of external qualities operating upon the sensory organs." },
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "Elizabeth bore her sister's thoughtless elopement far more **philosophically** than her hysterical mother." },
      { author: "William James", work: "Pragmatism", quote: "Let us ask **philosophically** what concrete cash-value an idea brings into our actual lived experience." }
    ]
  },
  "Dashboard — phil/philosophise.md": {
    primary: "To speculate, theorize, or deliberate about fundamental questions of existence, truth, ethics, and knowledge (Commonwealth spelling).",
    secondary: "To moralize or explain events in terms of philosophical or general principles.",
    quotes: [
      { author: "Aristotle", work: "Metaphysics", quote: "It was wonder that first led men to **philosophise**, and wonder still drives them to explore the unknown." },
      { author: "David Hume", work: "A Treatise of Human Nature", quote: "I dine, I play a game of backgammon, I converse with friends; and when I return to **philosophise**, my doubts appear frivolous." },
      { author: "George Bernard Shaw", work: "Man and Superman", quote: "The devil loves to **philosophise** in hell, celebrating romantic illusions that earth-dwellers have outgrown." }
    ]
  },
  "Dashboard — phil/philosophiser.md": {
    primary: "A person who philosophizes, especially in a casual, amateurish, or superficial manner (Commonwealth spelling).",
    secondary: "A commentator or moralizer who constructs theoretical explanations for everyday conduct.",
    quotes: [
      { author: "Samuel Johnson", work: "The Idler", quote: "The coffee-house **philosophiser** settles the affairs of kingdoms between two dishes of tea." },
      { author: "William Makepeace Thackeray", work: "The History of Pendennis", quote: "Arthur fancied himself a profound **philosophiser**, puffing cigars while solving the mysteries of the universe." },
      { author: "George Eliot", work: "The Mill on the Floss", quote: "Uncle Pullet was a slow **philosophiser**, shaking his head at modern innovations with solemn ignorance." }
    ]
  },
  "Dashboard — phil/philosophize.md": {
    primary: "To speculate, theorize, or reason about fundamental matters of existence, morality, and knowledge (American spelling).",
    secondary: "To moralize, intellectualize, or view matters with philosophical detachment.",
    quotes: [
      { author: "Ralph Waldo Emerson", work: "The Transcendentalist", quote: "The young scholar leaves the marketplace to **philosophize** beneath the stars, seeking eternal laws behind passing forms." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "With a pipe in his mouth, a sailor can **philosophize** upon a whale's skull as calmly as a monk in his cell." },
      { author: "Henry David Thoreau", work: "Walden", quote: "To **philosophize** is to live a life of simplicity, independence, magnanimity, and trust." }
    ]
  },
  "Dashboard — phil/philosophizer.md": {
    primary: "A person who philosophizes; one who theorizes or moralizes (American spelling).",
    secondary: "Someone who engages in speculative discourse, often with an air of dogmatic authority.",
    quotes: [
      { author: "Benjamin Franklin", work: "Autobiography", quote: "Every amateur **philosophizer** in Philadelphia founded his own club to debate the nature of electricity and virtue." },
      { author: "Mark Twain", work: "The Innocents Abroad", quote: "Our fellow traveler was an inveterate **philosophizer**, discovering profound moral lessons in every broken Roman column." },
      { author: "Henry James", work: "Roderick Hudson", quote: "Rowland was a patient **philosophizer**, watching his brilliant young friend rush headlong into artistic ruin." }
    ]
  },
  "Dashboard — phil/philosophizing.md": {
    primary: "The act or practice of speculating philosophically; indulging in theoretical or ethical reflection.",
    secondary: "Often used pejoratively for abstract, idle moralizing disconnected from practical reality.",
    quotes: [
      { author: "Immanuel Kant", work: "Critique of Practical Reason", quote: "Mere **philosophizing** about virtue without actual moral discipline is as useless as medicine that is never swallowed." },
      { author: "Friedrich Nietzsche", work: "Twilight of the Idols", quote: "To engage in **philosophizing** with a hammer means tapping the great idols to hear their hollow ring." },
      { author: "William James", work: "Pragmatism", quote: "Professional **philosophizing** too frequently loses itself in verbal labyrinths that have no bearing upon human conduct." }
    ]
  },
  "Dashboard — phil/philosophy.md": {
    primary: "The systematic study of the fundamental nature of knowledge, reality, and existence, especially when considered as an academic discipline (from Greek *philosophia*, 'love of wisdom').",
    secondary: "A particular theory, system of principles, or guiding worldview concerning conduct and life.",
    quotes: [
      { author: "Plato", work: "Apology", quote: "The unexamined life is not worth living; to practice **philosophy** is the highest service a mortal can offer to the gods." },
      { author: "Aristotle", work: "Metaphysics", quote: "All men by nature desire to know; the science of first principles, which is **philosophy**, begins in wonder." },
      { author: "Francis Bacon", work: "Novum Organum", quote: "Natural **philosophy** is the mother of all sciences, providing the solid foundation for human dominion over nature." }
    ]
  },
  "Dashboard — phil/philter.md": {
    primary: "A potion, drug, or magical charm believed to arouse sexual love and passionate desire in the person who drinks it.",
    secondary: "A magic love charm or enchanted elixir in folklore, drama, and romance literature.",
    quotes: [
      { author: "William Shakespeare", work: "Othello", quote: "Judge me the world, if 'tis not gross in sense that thou hast practiced on her with foul charms, abused her delicate youth with drugs or **philter**." },
      { author: "John Dryden", work: "The Spanish Friar", quote: "She mixed a potent **philter** of mandrake root and nightshade to bind the young prince's wandering heart." },
      { author: "Walter Scott", work: "The Bride of Lammermoor", quote: "The superstitious crone claimed to sell an infallible **philter** that could turn cold indifference into burning passion." }
    ]
  },
  "Dashboard — phil/philtre.md": {
    primary: "Alternative spelling of philter; a love potion or magical draught intended to kindle sexual affection.",
    secondary: "A literary or archaic motif representing irrational, magically induced infatuation (as in the legend of Tristan and Isolde).",
    quotes: [
      { author: "Thomas Malory", work: "Le Morte d'Arthur", quote: "Tristram and the fair Isolde drank the enchanted **philtre** unawares upon the ship, binding their souls in tragic love." },
      { author: "Algernon Charles Swinburne", work: "Tristram of Lyonesse", quote: "The fiery wine was a fateful **philtre** whose drop sealed the doom of two royal lovers." },
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", quote: "Ancient sorcerers compounded their **philtres** of vervain, ambergris, and hippomanes to deceive gullible lovers." }
    ]
  },
  "Dashboard — phil/philtrum.md": {
    primary: "The vertical groove in the middle of the upper lip extending from the nasal septum down to the vermilion border.",
    secondary: "An anatomical feature formed during embryological fusion of the medial nasal and maxillary prominences, whose failure to fuse results in cleft lip.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A smooth, elongated **philtrum** with a thin upper vermilion border is a diagnostic facial hallmark of fetal alcohol syndrome." },
      { author: "Charles Darwin", work: "The Expression of the Emotions in Man and Animals", quote: "In sneering, the canine tooth is exposed by the retraction of the lip on one side of the medial **philtrum**." },
      { author: "Henry Gray", work: "Anatomy of the Human Body", quote: "The central depression of the human upper lip, known anatomically as the **philtrum**, marks the junction of the embryonic facial processes." }
    ]
  },
  "Dashboard — phil/symphilid.md": {
    primary: "A member of the class Symphyla; a small, blind, pale soil-dwelling myriapod (garden centipede), superficially resembling tiny centipedes.",
    secondary: "In soil biology and economic entomology, an agricultural pest that feeds on tender root hairs of vegetables and seedlings.",
    quotes: [
      { author: "John Lubbock", work: "On the Origin and Metamorphoses of Insects", quote: "The curious **symphilid** myriapod bridges the morphological gap between the primitive apterygote insects and the centipedes." },
      { author: "Charles Darwin", work: "The Formation of Vegetable Mould through the Action of Worms", quote: "Alongside earthworms, the blind subterranean **symphilid** burrows through the loose humus, consuming decayed vegetation." },
      { author: "Asa Fitch", work: "Reports on the Noxious, Beneficial and Other Insects of the State of New York", quote: "Greenhouse growers dread the microscopic **symphilid**, whose underground tunneling destroys the feeder roots of lettuce." }
    ]
  },
  "Dashboard — phil/xenophile.md": {
    primary: "An individual who is attracted to, loves, or has an intense admiration for foreign people, cultures, customs, or foreign things (contrasted with a xenophobe).",
    secondary: "A cosmopolitan cultural enthusiast who values diverse foreign traditions above parochial domestic norms.",
    quotes: [
      { author: "E. M. Forster", work: "A Passage to India", quote: "Fielding was an instinctive **xenophile**, preferring the hospitable company of cultivated Indian gentlemen to the club's insular gossip." },
      { author: "Henry James", work: "The European", quote: "The American cousin proved an eager **xenophile**, enchanted by every antique courtly custom brought from the Continent." },
      { author: "George Orwell", work: "The Lion and the Unicorn", quote: "The English intellectual is notoriously a **xenophile**, eager to praise foreign systems while belittling his own nation." }
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

console.log('Batch 7 complete! Total files updated:', Object.keys(filesData).length);
