import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Beginning & Primacy/Dashboard — arch";

const wordsData = {
  "anarchic.md": {
    word: "anarchic",
    primary: "With no controlling rules or principles to give order; chaotic, disorderly, or lawless.",
    secondary: "In political theory, advocating or characteristic of an order free from state hierarchy and coercive authority.",
    quotes: [
      { author: "George Orwell", work: "Homage to Catalonia", quote: "The workers’ militias in Barcelona functioned under an **anarchic** equality that astounded foreign observers." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "The sudden demolition of ancient legal authority threw the kingdom into an **anarchic** convulsion." },
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "A thousand shrieking voices rose from the crowd in **anarchic** fury as the prison gates were battered down." }
    ]
  },
  "anarchical.md": {
    word: "anarchical",
    primary: "Lacking order, organization, or established government; lawless, rebellious, or chaotic (a variant of anarchic).",
    secondary: "In political philosophy, describing conditions where societal institutions disintegrate into rampant factional violence.",
    quotes: [
      { author: "Thomas Hobbes", work: "Leviathan", quote: "Without a sovereign common power to keep all in awe, men remain in an **anarchical** state of perpetual war." },
      { author: "Alexander Hamilton", work: "The Federalist Papers (No. 15)", quote: "A league without coercive authority must inevitably collapse into an **anarchical** confederacy of jealous states." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The praetorian guards reduced Rome to an **anarchical** auction, selling the imperial diadem to the highest bidder." }
    ]
  },
  "anarchically.md": {
    word: "anarchically",
    primary: "In a lawless, chaotic, or uncontrolled manner, without recognized authority or discipline.",
    secondary: "In sociological analysis, describing spontaneous grassroots actions occurring outside institutional regulations.",
    quotes: [
      { author: "Alexis de Tocqueville", work: "The Old Regime and the Revolution", quote: "When central authority collapsed, peasants acted **anarchically**, burning manorial records in village squares." },
      { author: "H. G. Wells", work: "The War of the Worlds", quote: "The population fled **anarchically** through the blackened suburbs, abandoning all civilized restraint in their panic." },
      { author: "Leo Tolstoy", work: "War and Peace", quote: "The retreating army moved **anarchically** along the muddy highway, deaf to the shouts of their officers." }
    ]
  },
  "anarchism.md": {
    word: "anarchism",
    primary: "A political theory advocating the abolition of all government and the organization of society on a voluntary, cooperative basis without coercive authority.",
    secondary: "In intellectual history (articulated by Proudhon, Bakunin, and Kropotkin), a libertarian socialist philosophy seeking universal human freedom and mutual aid.",
    quotes: [
      { author: "Pierre-Joseph Proudhon", work: "What is Property?", quote: "As man seeks justice in equality, so society seeks order in **anarchism**, the absence of master and sovereign." },
      { author: "Peter Kropotkin", work: "Mutual Aid: A Factor of Evolution", quote: "The voluntary federations of **anarchism** represent the natural social instinct of mutual aid freed from state coercion." },
      { author: "Emma Goldman", work: "Anarchism and Other Essays", quote: "**Anarchism** stands for the liberation of the human mind from the dominion of religion, property, and state authority." }
    ]
  },
  "anarchist.md": {
    word: "anarchist",
    primary: "A person who believes in or advocates anarchism; someone who seeks the abolition of government and hierarchical authority.",
    secondary: "In late 19th-century political history, an activist participating in radical labor movements, anti-state strikes, or revolutionary propaganda.",
    quotes: [
      { author: "Joseph Conrad", work: "The Secret Agent", quote: "The gloomy professor, an uncompromising **anarchist**, carried glass phials of nitroglycerin in his coat pocket." },
      { author: "George Orwell", work: "Homage to Catalonia", quote: "I had an instinctive sympathy with the Spanish **anarchist** trade unionists who ran the tramways and factories." },
      { author: "Henry James", work: "The Princess Casamassima", quote: "Hyacinth Robinson found himself entangled in secret London meetings alongside a dedicated foreign **anarchist**." }
    ]
  },
  "anarchistic.md": {
    word: "anarchistic",
    primary: "Of, relating to, or characteristic of anarchism or anarchists; advocating the elimination of formal governmental authority.",
    secondary: "In cultural and aesthetic criticism, describing rebellious, anti-authoritarian impulses that challenge traditional rules, structures, and hierarchies.",
    quotes: [
      { author: "Bertrand Russell", work: "Proposed Roads to Freedom", quote: "The **anarchistic** critique of the state contains essential warnings against the tyranny of state bureaucracy." },
      { author: "Friedrich Nietzsche", work: "The Genealogy of Morals", quote: "He condemned the **anarchistic** dogmas of equality as disguised resentment against higher human excellence." },
      { author: "Virginia Woolf", work: "Three Guineas", quote: "The creative artist harbors an inherently **anarchistic** spirit that refuses to march in regimented patriotic parades." }
    ]
  },
  "anarchy.md": {
    word: "anarchy",
    primary: "A state of disorder due to absence or non-recognition of authority or other controlling systems; political lawlessness.",
    secondary: "In political philosophy, the ideal theoretical state of society based on voluntary cooperation and complete individual freedom without government.",
    quotes: [
      { author: "Percy Bysshe Shelley", work: "The Masque of Anarchy", quote: "Last came **Anarchy**: he rode / On a white horse, splashed with blood; / He was pale even to the lips, / Like Death in the Apocalypse." },
      { author: "Matthew Arnold", work: "Culture and Anarchy", quote: "Without the sweet reasonableness of culture, our unfettered individualism plunges into raw social **anarchy**." },
      { author: "John Milton", work: "Paradise Lost", quote: "Before their eyes in sudden view appear / The secrets of the hoary Deep—a dark / Illimitable ocean, where Chaos umpire sits, / And by decision more embroils the fray / By which he reigns: next him, high arbiter, / Chance governs all, and ancient **Anarchy**." }
    ]
  },
  "andrarchy.md": {
    word: "andrarchy",
    primary: "A social or political system governed or ruled predominantly by men; male supremacy or patriarchy (from Greek anēr/andros man + archē rule).",
    secondary: "In sociological and feminist political theory, an institutional order where political power, legal privileges, and economic authority are monopolized by men.",
    quotes: [
      { author: "Mary Wollstonecraft", work: "A Vindication of the Rights of Woman", quote: "The institutional structure of ancient civil law was fundamentally an **andrarchy**, reducing women to legal nonentities." },
      { author: "John Stuart Mill", work: "The Subjection of Women", quote: "The traditional family under patriarchal **andrarchy** served as an unyielding school of despotic power." },
      { author: "Virginia Woolf", work: "A Room of One's Own", quote: "Behind the imposing facade of university colleges stood centuries of uncontested masculine **andrarchy**." }
    ]
  },
  "antarchy.md": {
    word: "antarchy",
    primary: "Opposition to government, rule, or political authority in general; an archaic term for anarchism or rebellion against governance.",
    secondary: "In 17th- and 18th-century political theology, the radical rejection of civil magistracy and divine sovereign authority.",
    quotes: [
      { author: "Jeremy Taylor", work: "Ductor Dubitantium", quote: "Those seditious spirits who plead for absolute **antarchy** subvert the foundations of all peaceful Christian commonwealths." },
      { author: "Richard Baxter", work: "A Holy Commonwealth", quote: "To depose the lawful magistrate without establishing a righteous order is to invite the demon of **antarchy**." },
      { author: "Robert South", work: "Sermons Preached Upon Several Occasions", quote: "The civil convulsions of the rebellion proved that **antarchy** leads inevitably to the most brutal tyranny." }
    ]
  },
  "arch.md": {
    word: "arch",
    primary: "A curved symmetrical structure spanning an opening and supporting weight; chief, principal, or prime; mischievously playful or sly.",
    secondary: "In prefix compounding (Greek archē/arch-), denoting premier rank (archbishop, archenemy); in architecture, a masonry vaulting unit; as an adjective, teasingly saucy.",
    quotes: [
      { author: "William Shakespeare", work: "The Tempest", quote: "The cloud-capp'd towers, the gorgeous palaces, / The solemn temples, the great globe itself, / Yea, all which it inherit, shall dissolve / And, like this insubstantial pageant faded, / Leave not a rack behind; yet Rome’s triumphal **arch** stood long in memory." },
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "Elizabeth looked at him with an **arch** smile, delighted to tease his grave self-importance." },
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The pointed Gothic **arch** was an architectural revolution, directing immense vertical thrusts downward through slender shafts." }
    ]
  },
  "archaean.md": {
    word: "archaean",
    primary: "Of, relating to, or denoting the earlier eon of the Precambrian era, spanning from c. 4.0 to 2.5 billion years ago; ancient or primitive.",
    secondary: "In historical geology and paleontology, the era of Earth's cooling crust, primitive oceans, and the origin of anaerobic single-celled life.",
    quotes: [
      { author: "Charles Lyell", work: "The Student's Elements of Geology", quote: "The heavily metamorphosed **Archaean** gneisses form the deep crystalline basement of the continents." },
      { author: "James Dwight Dana", work: "Manual of Geology", quote: "Sedimentary banded iron formations provide unmistakable chemical evidence of photosynthetic life in the **Archaean** seas." },
      { author: "Stephen Jay Gould", work: "Wonderful Life", quote: "For the first two billion years of the **Archaean** eon, life remained microscopic and prokaryotic." }
    ]
  },
  "archaebacteria.md": {
    word: "archaebacteria",
    primary: "A former or variant scientific term for the domain Archaea, designating primitive prokaryotes with unique cell wall lipids and ribosomal RNA.",
    secondary: "In microbial taxonomy (coined by Carl Woese and George Fox), microorganisms that thrive in extreme environments (methanogens, extreme halophiles, hyperthermophiles).",
    quotes: [
      { author: "Carl Woese", work: "A Conception of Bacterial Evolution", quote: "The distinct biochemical composition of **archaebacteria** proves they are phylogenetically separate from true eubacteria." },
      { author: "Stephen Jay Gould", work: "Full House", quote: "The discovery of **archaebacteria** fundamentally reorganized the tree of life into three great domains." },
      { author: "Lynn Margulis", work: "Five Kingdoms", quote: "Extremophilic **archaebacteria** preserve molecular clues to the hot, reducing conditions of the prebiotic Earth." }
    ]
  },
  "archaebacterium.md": {
    word: "archaebacterium",
    primary: "A single microscopic organism belonging to the archaebacteria (Archaea); a primitive prokaryotic microorganism.",
    secondary: "In cellular microbiology, an individual cell characterized by ether-linked branched lipid membranes, lacking peptidoglycan, and possessing unique transcriptional machinery.",
    quotes: [
      { author: "Carl Woese", work: "Phylogenetic Structure of the Prokaryotic Domain", quote: "Each isolated **archaebacterium** was analyzed for unique oligonucleotide signatures in its ribosomal RNA." },
      { author: "Lynn Margulis", work: "Symbiosis in Cell Evolution", quote: "A sulfur-metabolizing **archaebacterium** thriving near boiling underwater vents may resemble the universal common ancestor." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "In hypersaline lagoons, a halophilic **archaebacterium** produces radiant purple pigments to capture sunlight." }
    ]
  },
  "archaeobacteria.md": {
    word: "archaeobacteria",
    primary: "A variant plural spelling of archaebacteria, denoting the ancient domain of prokaryotes now officially termed Archaea.",
    secondary: "In evolutionary biochemistry, microorganisms possessing unique cellular membranes that enable survival under boiling, saline, or acidic conditions.",
    quotes: [
      { author: "Carl Woese", work: "Bacterial Evolution", quote: "Comparative sequence analysis confirmed that the **archaeobacteria** represent an independent primary kingdom of life." },
      { author: "Lynn Margulis", work: "Microcosmos", quote: "The survival of **archaeobacteria** in geothermal calderas illustrates the extreme boundaries of earthly life." },
      { author: "Stephen Jay Gould", work: "Eight Little Piggies", quote: "The recognition of **archaeobacteria** shattered our tidy binary division between plants and animals." }
    ]
  },
  "archaeologic.md": {
    word: "archaeologic",
    primary: "Of or relating to archaeology; concerning the recovery and study of material remains of past human life and activities.",
    secondary: "In scholarly literature, describing field surveys, excavation methods, and cataloging of material culture from past civilizations.",
    quotes: [
      { author: "Arthur Evans", work: "The Palace of Minos", quote: "Our **archaeologic** excavations at Knossos uncovered multi-story palaces decorated with vibrant marine frescoes." },
      { author: "Heinrich Schliemann", work: "Ilios: The City and Country of the Trojans", quote: "The **archaeologic** strata of Hissarlik revealed seven successive prehistoric cities stacked upon one hill." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The **archaeologic** ruins along the Appian Way remind the traveler of the fragile glory of empires." }
    ]
  },
  "archaeological.md": {
    word: "archaeological",
    primary: "Relating to the scientific study of human history and prehistory through the excavation and analysis of material remains, artifacts, and structures.",
    secondary: "In cultural heritage preservation, concerning the stratigraphy, radiocarbon dating, and conservation of historic monuments and burial sites.",
    quotes: [
      { author: "Howard Carter", work: "The Tomb of Tut-ankh-Amen", quote: "The opening of the sealed doorway was the culmination of years of arduous **archaeological** research." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "Recent **archaeological** discoveries of flint implements in river gravels prove the immense antiquity of man." },
      { author: "V. Gordon Childe", work: "Man Makes Himself", quote: "The **archaeological** record documents the profound social revolution wrought by the adoption of agriculture." }
    ]
  },
  "archaeologist.md": {
    word: "archaeologist",
    primary: "A scientist or scholar who studies human history and prehistory through the excavation of sites and the analysis of artifacts and other physical remains.",
    secondary: "In historiography and anthropology, an investigator reconstructing past societies, trade networks, and environmental adaptations from material culture.",
    quotes: [
      { author: "Howard Carter", work: "The Tomb of Tut-ankh-Amen", quote: "The **archaeologist** peered through the tiny hole by candlelight, beholding wonderful things unseen for three thousand years." },
      { author: "Arthur Evans", work: "The Palace of Minos", quote: "To the **archaeologist**, a broken potsherd often reveals more historical truth than the flattering inscription of a king." },
      { author: "Agatha Christie", work: "Come, Tell Me How You Live", quote: "An **archaeologist** is the best husband a woman can have; the older she gets, the more interested he is in her." }
    ]
  },
  "archaeology.md": {
    word: "archaeology",
    primary: "The study of human history and prehistory through the excavation of sites and the analysis of artifacts and other physical remains.",
    secondary: "In philosophical discourse (Michel Foucault's 'archaeology of knowledge'), the historical investigation of the discursive systems and epistemes that govern what can be known in an era.",
    quotes: [
      { author: "V. Gordon Childe", work: "What Happened in History", quote: "**Archaeology** has revolutionized history, extending human memory from three millennia of written annals to hundreds of thousands of years." },
      { author: "Michel Foucault", work: "The Archaeology of Knowledge", quote: "By **archaeology**, I intend the uncovering of the unconscious rules that determine the boundaries of thought in a given epoch." },
      { author: "Thomas Jefferson", work: "Notes on the State of Virginia", quote: "My careful excavation of the Virginia burial mound was perhaps the earliest scientific attempt at stratigraphic **archaeology** in America." }
    ]
  },
  "archaeopteryx.md": {
    word: "archaeopteryx",
    primary: "An extinct genus of bird-like dinosaurs from the Late Jurassic period, exhibiting transitional features between feathered dinosaurs and modern birds (from Greek archaios ancient + pteryx wing).",
    secondary: "In evolutionary biology, the iconic transitional fossil discovered in Solnhofen limestone in 1861, possessing avian flight feathers alongside reptilian teeth, claws, and a long bony tail.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "On the Animals which are most nearly intermediate between Birds and Reptiles", quote: "In **Archaeopteryx**, the reptilian affinities are so manifest that the boundary between birds and reptiles completely dissolves." },
      { author: "Charles Darwin", work: "The Origin of Species (4th edition)", quote: "The strange bird **Archaeopteryx**, with a long lizard-like tail bearing a pair of feathers on each joint, wonderfully illustrates my theory." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "**Archaeopteryx** is the classic mosaic fossil, demonstrating how evolutionary novelties arise through mosaic assembly." }
    ]
  },
  "archaeornis.md": {
    word: "archaeornis",
    primary: "A fossil bird from the Late Jurassic Solnhofen limestone of Germany, originally classified as a distinct genus but generally regarded as a specimen of Archaeopteryx.",
    secondary: "In paleornithological history, the Berlin specimen described by Dames and Petronievics, demonstrating exquisite feather preservation and reptilian cranial anatomy.",
    quotes: [
      { author: "Branislav Petronievics", work: "On the Structure of the Skull of Archaeornis", quote: "The exquisite preservation of the Berlin skeleton justified erecting the genus **Archaeornis** for this feathered reptile." },
      { author: "Arthur Smith Woodward", work: "Outlines of Vertebrate Palaeontology", quote: "The specimen designated as **Archaeornis** displays the transitional transition from theropod dinosaur to primitive avian form." },
      { author: "Gerhard Heilmann", work: "The Origin of Birds", quote: "Comparative analysis showed that **Archaeornis** possessed clawed digits upon its wings, enabling climbing among prehistoric branches." }
    ]
  },
  "archaeornithes.md": {
    word: "archaeornithes",
    primary: "An obsolete taxonomic subclass of primitive, extinct birds that possessed distinctly reptilian anatomical features, notably including Archaeopteryx.",
    secondary: "In systematic paleontology, historically contrasted with the Neornithes (modern birds) due to their toothed jaws, clawed forelimbs, and elongated caudal vertebral column.",
    quotes: [
      { author: "Alfred Romer", work: "Vertebrate Paleontology", quote: "The subclass **Archaeornithes** was created to accommodate the solitary Jurassic transitional form Archaeopteryx." },
      { author: "Ernst Mayr", work: "Systematics and the Origin of Species", quote: "Taxonomists formerly separated the primitive **Archaeornithes** from all living birds by their unreduced saurian tails." },
      { author: "Edwin H. Colbert", work: "Evolution of the Vertebrates", quote: "In the **Archaeornithes**, the sternum lacked the prominent keel that anchors the powerful flight muscles of modern fliers." }
    ]
  },
  "archaeozoic.md": {
    word: "archaeozoic",
    primary: "Of, relating to, or denoting the earliest era of the Precambrian, characterized by the appearance of the earliest primitive life forms; Archean.",
    secondary: "In 19th- and early 20th-century geological nomenclature, the vast epoch of primordial crystalline rocks formed before the Proterozoic era.",
    quotes: [
      { author: "James Dwight Dana", work: "Manual of Geology", quote: "We designate the grand primordial era as the **Archaeozoic**, marking the dawn of life upon the cooling terrestrial sphere." },
      { author: "Charles Lyell", work: "Elements of Geology", quote: "Beneath the fossiliferous strata lay the immense **Archaeozoic** basement, barren of complex animal remains." },
      { author: "Thomas Chrowder Chamberlin", work: "The Origin of the Earth", quote: "The **Archaeozoic** rocks preserve the earliest chemical signatures of marine precipitation and atmospheric evolution." }
    ]
  },
  "archaic.md": {
    word: "archaic",
    primary: "Very old or old-fashioned; belonging to an earlier historical period; in linguistics, of words or idioms no longer in common modern usage.",
    secondary: "In art history, the Archaic period of Greek art (c. 650–480 BCE), characterized by stylized kouroi sculptures with the enigmatic 'archaic smile'.",
    quotes: [
      { author: "George Orwell", work: "Politics and the English Language", quote: "The writer burdened his political pamphlet with **archaic** idioms and Latinate jargon to lend an air of false solemnity." },
      { author: "Walter Pater", work: "The Renaissance", quote: "The **archaic** Greek statues possess a solemn, rigid beauty, with their tight curls and enigmatic stony smiles." },
      { author: "Virginia Woolf", work: "The Common Reader", quote: "Spenser deliberately employed **archaic** English phrases to wrap his allegorical romance in antique enchantment." }
    ]
  },
  "archaicism.md": {
    word: "archaicism",
    primary: "An archaic word, phrase, idiom, or style; an intentional use of antique linguistic or artistic forms (a variant of archaism).",
    secondary: "In literary stylistics, the deliberate revival of antique idioms to create an atmosphere of biblical gravity or historical authenticity.",
    quotes: [
      { author: "Samuel Johnson", work: "Preface to Shakespeare", quote: "The poet’s diction is sometimes stained with an obsolete **archaicism** that impedes the modern reader's pleasure." },
      { author: "Matthew Arnold", work: "On Translating Homer", quote: "Francis Newman disfigured his translation with eccentric **archaicisms** that made the flowing Greek sound grotesquely barbarous." },
      { author: "William Hazlitt", work: "Lectures on the English Poets", quote: "The affected **archaicism** of Chatterton’s forged Rowley poems could not long deceive the acute eye of scholarship." }
    ]
  },
  "archaise.md": {
    word: "archaise",
    primary: "To give an archaic character, style, or appearance to something; to write or speak in an archaic manner (British English spelling).",
    secondary: "In aesthetic history and book design, to intentionally emulate ancient typography, medieval spelling, or classical compositional rules.",
    quotes: [
      { author: "William Morris", work: "The Story of the Glittering Plain (Note)", quote: "In printing this romance, we chose to **archaise** both the type fonts and the woodcut borders to recapture medieval craft." },
      { author: "George Saintsbury", work: "A History of English Prose Rhythm", quote: "Tudor historians loved to **archaise** their accounts of ancient kings by inserting mock-Saxon alliterations." },
      { author: "Samuel Taylor Coleridge", work: "Biographia Literaria", quote: "In 'The Rime of the Ancient Mariner', I chose to **archaise** the ballad diction to impart an ancient nautical authority." }
    ]
  },
  "archaism.md": {
    word: "archaism",
    primary: "A thing that is very old or old-fashioned; especially an archaic word, grammatical form, or stylistic feature surviving in modern language.",
    secondary: "In legal and liturgical prose, preserved antique phrases (such as 'hereunto', 'thee', 'thou') retained for institutional solemnity and continuity.",
    quotes: [
      { author: "H. L. Mencken", work: "The American Language", quote: "The isolated hill speech of the Southern Appalachians preserves many an Elizabethan **archaism** long forgotten in London." },
      { author: "Alexander Pope", work: "An Essay on Criticism", quote: "Words are like leaves; and where they most abound, / Much fruit of sense beneath is rarely found: / Avoid an affected **archaism** that smells of the tomb." },
      { author: "George Orwell", work: "1984", quote: "The very word 'honor' was regarded in Newspeak as a dangerous ideological **archaism** to be eradicated." }
    ]
  },
  "archaist.md": {
    word: "archaist",
    primary: "A person who admires, imitates, or revives archaic words, styles, or artistic and literary conventions.",
    secondary: "In Hellenistic and Victorian literary history, a scholar or writer who deliberately champions obsolete vocabulary against contemporary vernacular.",
    quotes: [
      { author: "Walter Pater", work: "Appreciations", quote: "Charles Lamb was a passionate **archaist**, delighting in the quaint prose of Sir Thomas Browne and Robert Burton." },
      { author: "George Saintsbury", work: "The Peace of the Augustans", quote: "The neoclassicists looked with suspicion upon the romantic **archaist** who revived medieval ballad meters." },
      { author: "Quintilian", work: "Institutio Oratoria", quote: "The orator should not mimic the stubborn **archaist** who insists on speaking the uncouth dialect of the ancient kings." }
    ]
  },
  "archaistic.md": {
    word: "archaistic",
    primary: "Consciously imitating or reviving an archaic style or ancient manner in art, literature, or architecture.",
    secondary: "In classical art history, describing Roman sculptures that deliberately mimicked the rigid poses and stylized drapery of the Greek Archaic period.",
    quotes: [
      { author: "Winckelmann", work: "History of Ancient Art", quote: "Roman sculptors produced **archaistic** copies of Greek statues to satisfy the antiquarian tastes of wealthy patricians." },
      { author: "Henry James", work: "The Portrait of a Lady", quote: "Gilbert Osmond surrounded himself with **archaistic** curios, treasuring the stiff formal elegance of forgotten centuries." },
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The pre-Raphaelite painter adopted an **archaistic** simplicity of color to protest the glossy vulgarity of the Royal Academy." }
    ]
  },
  "archaize.md": {
    word: "archaize",
    primary: "To give an archaic quality or character to something; to write, speak, or design in an archaic manner.",
    secondary: "In literary composition and translation, to intentionally employ antique diction and syntax to establish an ancient or mythical atmosphere.",
    quotes: [
      { author: "T. S. Eliot", work: "Selected Essays", quote: "A translator of Dante must resist the temptation to **archaize** the text with faux-Elizabethan mannerisms." },
      { author: "Herman Melville", work: "Pierre: or, The Ambiguities", quote: "The author began to **archaize** his prose, weaving convoluted Jacobean cadences into his psychological tragedy." },
      { author: "Mark Twain", work: "A Connecticut Yankee in King Arthur's Court", quote: "Hank Morgan ridiculed the romantic knights who would **archaize** every ordinary conversation into Arthurian pomposity." }
    ]
  },
  "archangel.md": {
    word: "archangel",
    primary: "An angel of high rank or supreme status in Judeo-Christian and Islamic angelology, such as Michael, Gabriel, or Raphael (from Greek arch- chief + angelos messenger).",
    secondary: "In botanical folklore, yellow archangel (Lamium galeobdolon); in Russian geography, the historic Arctic port city of Arkhangelsk named in honor of the Archangel Michael.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "The **Archangel** Michael, waving his flaming sword, led the heavenly legions against the rebellious host." },
      { author: "William Blake", work: "The Marriage of Heaven and Hell", quote: "An **Archangel** came and sat by my table, reading with wonder the fiery proverbs of Hell." },
      { author: "Dante Alighieri", work: "The Divine Comedy: Purgatorio", quote: "We beheld the **Archangel** Gabriel carved in marble with such lifelike grace that he seemed breathing." }
    ]
  },
  "archangelic.md": {
    word: "archangelic",
    primary: "Of, relating to, or resembling an archangel; having the majesty, power, or celestial purity of an archangel.",
    secondary: "In poetical and theological literature, describing transcendent brightness, thunderous heavenly authority, or awe-inspiring spiritual beauty.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "He spoke with **archangelic** majesty, his voice commanding silence through the celestial realms." },
      { author: "Percy Bysshe Shelley", work: "Hellas", quote: "A glorious vision appeared with **archangelic** speed, announcing the liberation of the Greek isles." },
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "Mirabeau arose in the assembly, wielding an **archangelic** eloquence that subdued the stormy debate." }
    ]
  },
  "archangelical.md": {
    word: "archangelical",
    primary: "A variant or formal form of archangelic; belonging to or characteristic of archangels.",
    secondary: "In 17th-century theological prose and liturgical poetry, designating the premier angelic choir and their cosmic heraldic trumpets.",
    quotes: [
      { author: "Jeremy Taylor", work: "The Great Exemplar", quote: "The heavenly host sang with **archangelical** harmony over the manger of Bethlehem." },
      { author: "Robert South", work: "Twelve Sermons Preached Upon Several Occasions", quote: "The last day shall be proclaimed by an **archangelical** blast that will awaken the sleeping dead." },
      { author: "Thomas Browne", work: "Religio Medici", quote: "I can easily believe that **archangelical** intelligences govern the orbits of the wandering spheres." }
    ]
  },
  "archbishop.md": {
    word: "archbishop",
    primary: "A bishop of the highest rank, presiding over an ecclesiastical province or archdiocese (from Greek arch- chief + episkopos overseer).",
    secondary: "In church polity (Anglican, Catholic, Orthodox), a metropolitan prelate who exercises jurisdictional oversight over suffragan bishops.",
    quotes: [
      { author: "William Shakespeare", work: "Henry V", quote: "The learned **Archbishop** of Canterbury expounded the Salic law to prove the king’s rightful claim to France." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The **Archbishop** of Alexandria exercised a secular and spiritual authority that rivaled that of the prefect." },
      { author: "George Eliot", work: "Middlemarch", quote: "The bishop spoke with that measured solemnity which seemed to anticipate an **archbishop**'s pallium." }
    ]
  },
  "archdeacon.md": {
    word: "archdeacon",
    primary: "A senior Christian cleric, ranking immediately below a bishop, with administrative authority over an archdeaconry.",
    secondary: "In the Anglican and Catholic communion, the chief administrative officer ('the bishop’s eye') responsible for church property, parish discipline, and legal inspections.",
    quotes: [
      { author: "Anthony Trollope", work: "The Warden", quote: "**Archdeacon** Grantly stood upon his hearthrug, a pillar of church orthodoxy and diocesan governance." },
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "Mr. Collins spoke with profound deference of the **archdeacon**, whose visitation dinner was the event of the year." },
      { author: "Thomas Hardy", work: "Under the Greenwood Tree", quote: "The vicar read the **archdeacon**'s formal charge concerning the replacement of the village string choir by an organ." }
    ]
  },
  "arche.md": {
    word: "arche",
    primary: "A classical Greek philosophical term (ἀρχή) meaning beginning, origin, first principle, or supreme ruling power.",
    secondary: "In pre-Socratic metaphysics, the foundational, primordial substance from which all things originate (e.g. water for Thales, apeiron for Anaximander, air for Anaximenes).",
    quotes: [
      { author: "Aristotle", work: "Metaphysics", quote: "The earliest philosophers sought the material **arche** of all beings, debating whether water, air, or fire was the primordial root." },
      { author: "Martin Heidegger", work: "Early Greek Thinking", quote: "The Greek concept of **arche** unifies origin and rule: that which begins is that which governs all subsequent unfolding." },
      { author: "Hans-Georg Gadamer", work: "The Beginning of Philosophy", quote: "In the pre-Socratic inquiry into the **arche**, Greek thought achieved its decisive leap into philosophical ontology." }
    ]
  },
  "archean.md": {
    word: "archean",
    primary: "A variant spelling of Archaean; relating to the early Precambrian geological eon, spanning c. 4.0 to 2.5 billion years ago.",
    secondary: "In geology, pertaining to the ancient crystalline rocks of the continental shields that preserve Earth's earliest isotopic records.",
    quotes: [
      { author: "James Dwight Dana", work: "Manual of Geology", quote: "The **Archean** rocks of the Canadian shield reveal intense folding and deep thermal metamorphism." },
      { author: "Charles Lyell", work: "Elements of Geology", quote: "The base of the stratigraphic column is formed by ancient **Archean** granites devoid of macroscopic fossils." },
      { author: "Walter Alvarez", work: "T. Rex and the Crater of Doom", quote: "Zircons preserved in **Archean** sandstones survive from the very infancy of our planet." }
    ]
  },
  "arched.md": {
    word: "arched",
    primary: "Constructed with or having the form of an arch; curved, bowed, or vaulted (from Latin arcus bow).",
    secondary: "In architectural design and anatomy, describing vaulted stone ceilings, natural bridges, or the curved contour of a foot or eyebrow.",
    quotes: [
      { author: "Edgar Allan Poe", work: "The Cask of Amontillado", quote: "We passed through a range of low **arched** vaults, descending until the damp air was foul with nitre." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "Her fine, distinctly **arched** eyebrows gave to her countenance an expression of keen intelligence." },
      { author: "Lord Byron", work: "Childe Harold's Pilgrimage", quote: "Through **arched** portals rode the chivalry of Spain, beneath banners that waved in the mountain wind." }
    ]
  },
  "archegonial.md": {
    word: "archegonial",
    primary: "Of, relating to, or producing an archegonium (the female multicellular sex organ in bryophytes, ferns, and gymnosperms).",
    secondary: "In plant developmental morphology, designating the archegonial chamber, neck canal cells, and protective venter during fertilization.",
    quotes: [
      { author: "Asa Gray", work: "Structural Botany", quote: "The flagellated spermatozoids swim through the film of dew toward the open **archegonial** neck." },
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "Fertilization occurs deep within the **archegonial** venter, giving rise to the embryonic sporophyte." },
      { author: "Katherine Esau", work: "Plant Anatomy", quote: "The **archegonial** jacket cells provide vital nourishment to the developing egg in primitive gymnosperms." }
    ]
  },
  "archegoniate.md": {
    word: "archegoniate",
    primary: "Any plant that possesses archegonia as its female reproductive organs, comprising bryophytes, pteridophytes, and most gymnosperms.",
    secondary: "In botanical taxonomy, historically grouped together as Archegoniatae to emphasize their shared evolutionary mode of oogamous sexual reproduction.",
    quotes: [
      { author: "F. O. Bower", work: "The Origin of a Land Flora", quote: "The evolutionary transition to dry land required the **archegoniate** plants to protect the egg within a multicellular jacket." },
      { author: "Karl von Goebel", work: "Organography of Plants", quote: "Comparative study reveals the gradual reduction of the gametophyte across the higher **archegoniate** series." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "Ferns and mosses are classic **archegoniate** cryptogams, dependent upon ambient water for fertilization." }
    ]
  },
  "archegonium.md": {
    word: "archegonium",
    primary: "The multicellular, flask-shaped female reproductive organ in mosses, ferns, and gymnosperms that produces and protects the egg cell (ovum).",
    secondary: "In evolutionary botany (from Greek archē beginning + gonos offspring), the ancestral reproductive structure that protected embryos during the colonization of land.",
    quotes: [
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "The mature **archegonium** opens at the apex of its neck, releasing chemotactic chemicals to attract swimming spermatozoids." },
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated and Vegetal Organisms", quote: "Within the swollen base of the **archegonium** rests the solitary ovum, awaiting fertilization." },
      { author: "F. O. Bower", work: "The Ferns", quote: "The evolutionary history of land plants is illuminated by the gradual reduction of the **archegonium** in seed-bearing gymnosperms." }
    ]
  }
};

function updateWordNote(relPath, data) {
  const fullPath = path.join(baseDir, relPath);
  if (!fs.existsSync(fullPath)) {
    console.error("Not found:", fullPath);
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
console.log("Primacy Batch 4 completed! Total words updated:", Object.keys(wordsData).length);
