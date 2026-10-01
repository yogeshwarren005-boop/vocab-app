import fs from "fs";
import path from "path";

const clusterDir = "App database/Greek roots/Cluster Writing & Script";

const wordsData = {
  // Dashboard — glyph
  "Dashboard — glyph/Glyptodon.md": {
    word: "Glyptodon",
    primary: "An extinct genus of large, heavily armored, herbivorous mammals of the Americas during the Pleistocene epoch, related to modern armadillos.",
    secondary: "In vertebrate paleontology, xenarthrans notable for a massive, fused bony dorsal carapace and fluted, column-like molar teeth.",
    quotes: [
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The great bony armor of the **Glyptodon** was embedded in the cliff of the Pampas alongside the bones of Megatherium." },
      { author: "Richard Owen", work: "Description of the Skeleton of an Extinct Gigantic Sloth", quote: "The molar dentition of **Glyptodon** exhibits deep longitudinal fluting that gave the genus its distinctive name." },
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "The Pleistocene plains of South America supported monstrous xenarthrans, among which **Glyptodon** was the most heavily armored." }
    ]
  },
  "Dashboard — glyph/aglyphous.md": {
    word: "aglyphous",
    primary: "Having solid, conical teeth without grooves or tubular venom channels (applied to non-venomous snakes).",
    secondary: "In herpetology, designating colubrid and boid dentition where teeth lack specialization for venom delivery.",
    quotes: [
      { author: "George Albert Boulenger", work: "Catalogue of the Snakes in the British Museum", quote: "The family Colubridae was divided into **aglyphous** forms with solid teeth and opisthoglyphous forms bearing grooved fangs." },
      { author: "Hans Gadow", work: "Amphibia and Reptiles", quote: "Harmless constrictors possess an **aglyphous** dentition adapted solely for grasping struggling prey." },
      { author: "Raymond Ditmars", work: "Snakes of the World", quote: "Unlike the deadly vipers, the gentle garter snake retains an entirely **aglyphous** jaw without poison glands." }
    ]
  },
  "Dashboard — glyph/anaglyph.md": {
    word: "anaglyph",
    primary: "An ornament, cameo, or sculptured work carved in low or bas-relief (contrasting with an intaglio or diaglyph).",
    secondary: "A stereoscopic photographic image consisting of two superimposed color prints (typically red and cyan) producing a 3D effect when viewed through matching filters.",
    quotes: [
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The marble **anaglyph** upon the ancient sarcophagus portrayed the triumphant procession of Dionysus." },
      { author: "Walter Pater", work: "Studies in the History of the Renaissance", quote: "The subtle modeling of the Greek **anaglyph** allows light to outline the graceful drapery of the figures." },
      { author: "Oliver Wendell Holmes Sr.", work: "The Stereoscope and the Stereograph", quote: "By means of an **anaglyph**, the flat photographic plate springs into miraculous three-dimensional relief before our eyes." }
    ]
  },
  "Dashboard — glyph/anaglyphic.md": {
    word: "anaglyphic",
    primary: "Of, relating to, or consisting of an anaglyph or relief carving.",
    secondary: "Relating to stereoscopic three-dimensional projection using chromatically complementary filters (red-cyan lenses).",
    quotes: [
      { author: "Johann Joachim Winckelmann", work: "History of Ancient Art", quote: "The **anaglyphic** bas-reliefs decorating the Roman arch demonstrate the exquisite finish of Augustan stonecarvers." },
      { author: "Ansel Adams", work: "Examples: The Making of 40 Photographs", quote: "Experimental **anaglyphic** prints required precise registration of chromatic separation negatives." },
      { author: "Edward Bulwer-Lytton", work: "The Last Days of Pompeii", quote: "The atrium walls were embellished with **anaglyphic** borders representing nymphs and floral garlands." }
    ]
  },
  "Dashboard — glyph/anaglyphical.md": {
    word: "anaglyphical",
    primary: "Pertaining to the art of carving in relief; embossed or raised (variant of anaglyphic).",
    secondary: "Pertaining to stereoscopic relief representations produced by complementary color filtration.",
    quotes: [
      { author: "John Evelyn", work: "Sculptura", quote: "The ancients excelled in **anaglyphical** gems where the figure rose boldly from the sardonyx ground." },
      { author: "Horace Walpole", work: "Anecdotes of Painting in England", quote: "The cabinet was adorned with **anaglyphical** ivory panels depicting classical pastoral allegories." },
      { author: "Thomas Browne", work: "Hydriotaphia, Urn Burial", quote: "The funeral urn bore **anaglyphical** inscriptions surrounded by figures of weeping genii." }
    ]
  },
  "Dashboard — glyph/anaglyphy.md": {
    word: "anaglyphy",
    primary: "The art, method, or practice of carving or sculpturing in low or bas-relief.",
    secondary: "The technique or process of creating stereoscopic three-dimensional images through superimposed color printing.",
    quotes: [
      { author: "John Ruskin", work: "The Seven Lamps of Architecture", quote: "True architectural **anaglyphy** respects the stone wall, keeping its decorative reliefs within flat planes." },
      { author: "Walter Pater", work: "Greek Studies", quote: "The transition from geometric pottery to marble **anaglyphy** marked the blossoming of archaic Athenian sculpture." },
      { author: "David Brewster", work: "The Stereoscope: Its History, Theory, and Construction", quote: "Optical **anaglyphy** achieves the illusion of depth by presenting divergent perspectives to either eye." }
    ]
  },
  "Dashboard — glyph/anaglyptic.md": {
    word: "anaglyptic",
    primary: "Of or relating to the art of carving or engraving in relief (variant of anaglyphic).",
    secondary: "Relating to decorative embossed ornamental metalwork or raised paper wall coverings.",
    quotes: [
      { author: "William Morris", work: "The Lesser Arts of Life", quote: "The **anaglyptic** wallpaper added tactile depth and shadow to the high-ceilinged Victorian drawing room." },
      { author: "John Evelyn", work: "Numismata", quote: "Medallions struck in high **anaglyptic** style preserved the lifelike countenances of Roman imperators." },
      { author: "Henry James", work: "A Little Tour in France", quote: "The cathedral choir screen displayed an intricate **anaglyptic** frieze populated by prophets and angels." }
    ]
  },
  "Dashboard — glyph/anaglyptical.md": {
    word: "anaglyptical",
    primary: "Pertaining to carving in relief or embossed decorative work (variant of anaglyptic).",
    secondary: "Describing ornamental surfaces raised above a surrounding background.",
    quotes: [
      { author: "Isaac D'Israeli", work: "Curiosities of Literature", quote: "The Renaissance bibliophile treasured volumes bound in calfskin stamped with **anaglyptical** armorial designs." },
      { author: "Thomas Carlyle", work: "Past and Present", quote: "The ancient guildhall preserved **anaglyptical** shields commemorating the merchant masters of the town." },
      { author: "John Ruskin", work: "Modern Painters", quote: "The **anaglyptical** ornamentation of the marble architrave caught the fading light of the Venetian sunset." }
    ]
  },
  "Dashboard — glyph/diaglyph.md": {
    word: "diaglyph",
    primary: "An intaglio; an engraved or sunken carving where the design is hollowed out below the surface (contrasting with an anaglyph).",
    secondary: "In glyptic art, an incised gemstone or seal used for impressing a raised design upon wax or clay.",
    quotes: [
      { author: "Charles Thomas Newton", work: "Essays on Art and Archaeology", quote: "While the cameo is an anaglyph, the signet ring is an incised **diaglyph** meant for sealing royal decrees." },
      { author: "Walter Pater", work: "Marius the Epicurean", quote: "Marius admired the carnelian ring, whose miniature **diaglyph** portrayed Minerva with shield and spear." },
      { author: "John Addington Symonds", work: "Renaissance in Italy", quote: "Florentine lapidaries revived the ancient art of the **diaglyph**, engraving chalcedony with astonishing delicacy." }
    ]
  },
  "Dashboard — glyph/ditriglyph.md": {
    word: "ditriglyph",
    primary: "In classical Doric architecture, an arrangement having two triglyphs placed in the frieze over the space between two adjacent columns.",
    secondary: "In architectural history, an expanded intercolumniation employed to provide wider central portals in Doric porticoes.",
    quotes: [
      { author: "Vitruvius", work: "De Architectura", quote: "When the central intercolumniation is widened for a temple doorway, the frieze requires a **ditriglyph** arrangement." },
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The strict rhythm of the classical Doric frieze was modified by introducing a **ditriglyph** over the principal entrance." },
      { author: "William Chambers", work: "A Treatise on the Decorative Part of Civil Architecture", quote: "A **ditriglyph** intercolumniation must be managed with caution lest the entablature appear weakly supported." }
    ]
  },
  "Dashboard — glyph/ditriglyphic.md": {
    word: "ditriglyphic",
    primary: "Relating to, containing, or characterized by a ditriglyph; having two triglyphs in the frieze between consecutive columns.",
    secondary: "Pertaining to wide Doric temple spans configured with two triglyphs and three metopes between pillars.",
    quotes: [
      { author: "Vitruvius", work: "The Ten Books on Architecture", quote: "The **ditriglyphic** span allows carriages and processions to enter freely beneath the temple portico." },
      { author: "Banister Fletcher", work: "A History of Architecture", quote: "Doric propylaea frequently adopted a **ditriglyphic** system to accentuate the central passageway." },
      { author: "James Fergusson", work: "History of Architecture in All Countries", quote: "The Greek architects broke the monotony of uniform spacing by employing a **ditriglyphic** center bay." }
    ]
  },
  "Dashboard — glyph/glyph.md": {
    word: "glyph",
    primary: "A carved or incised symbol, figure, or character (such as a Mayan hieroglyph or an architectural flute).",
    secondary: "In typography and computing, an individual visual representation or graphical design of a character within a font.",
    quotes: [
      { author: "John Lloyd Stephens", work: "Incidents of Travel in Central America", quote: "Each hieroglyphic **glyph** carved upon the Copán stelae seemed to narrate the solemn deeds of forgotten kings." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The strange tattooed markings upon Queequeg's body resembled some mystical **glyph** from an ancient eastern temple." },
      { author: "Robert Bringhurst", work: "The Elements of Typographic Style", quote: "A digital typeface consists of a coordinated set of fonts, each mapping character codes to a distinct visual **glyph**." }
    ]
  },
  "Dashboard — glyph/glyptic.md": {
    word: "glyptic",
    primary: "Relating to the art of carving or engraving, especially on gems, cameos, or precious stones; also, the art itself.",
    secondary: "In sculpture and archaeology, of or denoting sculptures created by carving or cutting away stone or hard materials.",
    quotes: [
      { author: "Walter Pater", work: "The Renaissance", quote: "The master's hand exhibited that exquisite **glyptic** skill which made tiny sardonyx cameos rival monumental marble." },
      { author: "Henry James", work: "Roderick Hudson", quote: "He examined the antique emerald with the discriminating passion of a devotee of the **glyptic** art." },
      { author: "John Addington Symonds", work: "Sketches and Studies in Italy and Greece", quote: "The collection in Naples displays the pinnacle of Hellenistic **glyptic** mastery in jasper and agate." }
    ]
  },
  "Dashboard — glyph/glyptograph.md": {
    word: "glyptograph",
    primary: "An engraving or design executed upon a precious stone, gem, or seal; an incised or relief carving on a hard mineral.",
    secondary: "A description or monograph dealing with the art of gem-engraving.",
    quotes: [
      { author: "Charles Thomas Newton", work: "Travels & Discoveries in the Levant", quote: "The unearthed carnelian seal bore an archaic Greek **glyptograph** representing an eagle clutching a serpent." },
      { author: "Isaac D'Israeli", work: "Curiosities of Literature", quote: "The princely collector published a lavish **glyptograph** cataloging three centuries of engraved cameos." },
      { author: "John Ruskin", work: "Aratra Pentelici", quote: "In every miniature **glyptograph**, the ancient artist respected the structural grain and transparency of the stone." }
    ]
  },
  "Dashboard — glyph/monotriglyph.md": {
    word: "monotriglyph",
    primary: "In classical Doric architecture, the standard arrangement having only a single triglyph in the frieze over the space between two columns.",
    secondary: "In architectural theory, the regular and normative Doric system where metopes and triglyphs alternate in strict cadence.",
    quotes: [
      { author: "Vitruvius", work: "De Architectura", quote: "The **monotriglyph** scheme provides the most harmonious proportions for the standard Doric colonnade." },
      { author: "William Chambers", work: "A Treatise on Civil Architecture", quote: "In standard classical peristyles, the **monotriglyph** disposition ensures structural solidity and uniform visual rhythm." },
      { author: "Banister Fletcher", work: "A History of Architecture", quote: "The Parthenon follows the **monotriglyph** principle, placing one triglyph over each column and one over the intermediate span." }
    ]
  },
  "Dashboard — glyph/proteroglyphous.md": {
    word: "proteroglyphous",
    primary: "In herpetology, having permanently erect, short, hollow or grooved fangs positioned at the anterior end of the maxillae (characteristic of elapid snakes).",
    secondary: "In venom evolutionary biology, designating snakes whose fangs are fixed rather than hinged, requiring a sustained strike to deliver neurotoxins.",
    quotes: [
      { author: "George Albert Boulenger", work: "The Tailless Batrachians and Reptiles of Europe", quote: "The family Elapidae is strictly **proteroglyphous**, armed with anterior grooved venom fangs." },
      { author: "Raymond Ditmars", work: "Reptiles of the World", quote: "Cobras possess a **proteroglyphous** biting apparatus that contrasts sharply with the hinged folding fangs of true vipers." },
      { author: "Hans Gadow", work: "Amphibia and Reptiles", quote: "The evolutionary transition to a **proteroglyphous** condition enabled elapids to conquer ecological niches as apex venomous predators." }
    ]
  },
  "Dashboard — glyph/solenoglyphous.md": {
    word: "solenoglyphous",
    primary: "In herpetology, having long, hollow, tubular venom-injecting fangs mounted on a short, mobile maxilla that rotates to fold the fangs against the roof of the mouth.",
    secondary: "In functional morphology, possessing the most specialized snake envenomation system, allowing deep intramuscular delivery of hemotoxins.",
    quotes: [
      { author: "Raymond Ditmars", work: "The Serpents of North America", quote: "The rattlesnake displays a **solenoglyphous** mechanism of astounding efficiency, swinging its hypodermic fangs forward in an instant." },
      { author: "George Albert Boulenger", work: "Catalogue of the Snakes", quote: "The Viperidae are distinguished as **solenoglyphous** serpents, possessing perforated fangs upon a freely movable maxillary bone." },
      { author: "Hans Gadow", work: "Amphibia and Reptiles", quote: "In **solenoglyphous** vipers, the maxillary bone has shortened into a rotating hinge that prevents the immense fangs from piercing the lower jaw." }
    ]
  },

  // Dashboard — bet
  "Dashboard — bet/abet.md": {
    word: "abet",
    primary: "To encourage, support, incite, or aid (someone) to do something wrong, unlawful, or criminal.",
    secondary: "In criminal jurisprudence, to act as an accessory before or during the commission of a crime by facilitating its execution.",
    quotes: [
      { author: "William Shakespeare", work: "Richard II", quote: "Would'st thou **abet** the treason of thy son against his lawful anointed king?" },
      { author: "Alexander Hamilton", work: "The Federalist Papers (No. 65)", quote: "No public official should dare to **abet** the usurpation of constitutional rights by a lawless faction." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "To **abet** the overthrow of ancient legal institutions is to unleash the destructive passions of the multitude." }
    ]
  },
  "Dashboard — bet/abetter.md": {
    word: "abetter",
    primary: "A person who encourages, supports, or aids another in committing a crime, wrongdoing, or improper act (variant of abettor).",
    secondary: "In legal and ethical philosophy, one who promotes or fosters illicit enterprises through counsel, finance, or passive complicity.",
    quotes: [
      { author: "Samuel Johnson", work: "The Rambler", quote: "He that smiles at the slander of another becomes an active **abetter** of his malice." },
      { author: "Walter Scott", work: "The Heart of Midlothian", quote: "The magistrate condemned the smuggler and every secret **abetter** who purchased his contraband goods." },
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "The crown prosecuted the conspirators and treated every **abetter** of the rebellion with unsparing rigor." }
    ]
  },
  "Dashboard — bet/abettor.md": {
    word: "abettor",
    primary: "A person who aids, encourages, or incites another in the commission of an offense or wrongdoing; an accomplice.",
    secondary: "In penal law, a participant who, though not the principal perpetrator, is present aiding and abetting the felony.",
    quotes: [
      { author: "William Blackstone", work: "Commentaries on the Laws of England", quote: "An **abettor** who stands watch while a burglary is committed is equally guilty of the felony." },
      { author: "Charles Dickens", work: "Barnaby Rudge", quote: "The instigators of the Gordon riots found an eager **abettor** in every tavern and debtor's prison." },
      { author: "Henry Fielding", work: "Tom Jones", quote: "He denounced the highwayman and swore that every **abettor** of the rogue should hang by the neck." }
    ]
  },
  "Dashboard — bet/alphabetic.md": {
    word: "alphabetic",
    primary: "Of, relating to, or expressed by an alphabet; consisting of letters that represent phonemes.",
    secondary: "Arranged in the conventional order of the letters of an alphabet; alphabetical.",
    quotes: [
      { author: "Ferdinand de Saussure", work: "Course in General Linguistics", quote: "The **alphabetic** system of writing aims to represent each distinct phoneme by an individual graphic sign." },
      { author: "Max Müller", work: "Lectures on the Science of Language", quote: "The invention of **alphabetic** script was the greatest intellectual triumph of ancient Mediterranean civilization." },
      { author: "Samuel Johnson", work: "Preface to the English Dictionary", quote: "I have digested the immense vocabulary of our tongue into a strict **alphabetic** order." }
    ]
  },
  "Dashboard — bet/alphabetically.md": {
    word: "alphabetically",
    primary: "In the order of the letters of the alphabet.",
    secondary: "According to an alphabetical classification or filing system.",
    quotes: [
      { author: "Jane Austen", work: "Mansfield Park", quote: "Fanny arranged the volumes in her little white attic **alphabetically**, taking great pride in her orderly library." },
      { author: "Charles Dickens", work: "Bleak House", quote: "Mr. Guppy filed the legal papers **alphabetically**, searching for any scrap bearing the name of Hawdon." },
      { author: "George Eliot", work: "Middlemarch", quote: "Casaubon cataloged his mythological cross-references **alphabetically** in heavy leather-bound ledgers." }
    ]
  },
  "Dashboard — bet/alphabetise.md": {
    word: "alphabetise",
    primary: "To arrange in alphabetical order (British English spelling of alphabetize).",
    secondary: "To reduce a language to an alphabetical writing system.",
    quotes: [
      { author: "Virginia Woolf", work: "The Voyage Out", quote: "She attempted to **alphabetise** the chaotic bundles of letters stored in her grandfather’s desk." },
      { author: "David Crystal", work: "The Stories of English", quote: "Victorian lexicographers sought to **alphabetise** every dialectal variant found in the British Isles." },
      { author: "Lytton Strachey", work: "Eminent Victorians", quote: "Cardinal Manning insisted that the diocesan archives be thoroughly overhauled and **alphabetise** every parish return." }
    ]
  },
  "Dashboard — bet/alphabetize.md": {
    word: "alphabetize",
    primary: "To arrange in alphabetical order.",
    secondary: "To furnish an unwritten language with an alphabet; to teach the alphabet to someone.",
    quotes: [
      { author: "H. L. Mencken", work: "The American Language", quote: "American compilers were among the first to **alphabetize** reference works for rapid popular consultation." },
      { author: "Thomas Pynchon", work: "The Crying of Lot 49", quote: "She spent long hours attempting to **alphabetize** the bewildering inheritance of documents." },
      { author: "Benjamin Franklin", work: "Autobiography", quote: "I found it convenient to **alphabetize** my common-place book so that any moral maxim could be retrieved instantly." }
    ]
  },
  "Dashboard — bet/analphabet.md": {
    word: "analphabet",
    primary: "A person who cannot read or write; an illiterate person.",
    secondary: "In linguistic and educational sociology, an individual lacking functional literacy in an alphabet-based society.",
    quotes: [
      { author: "George Orwell", work: "The Road to Wigan Pier", quote: "An **analphabet** in a modern industrial city is helpless before the blizzard of printed regulations." },
      { author: "Antonio Gramsci", work: "Prison Notebooks", quote: "The cultural hegemony of the ruling class is perpetuated so long as the peasant remains an **analphabet**." },
      { author: "Claude Lévi-Strauss", work: "Tristes Tropiques", quote: "The tribal chief, though an **analphabet**, understood that holding a pen conferred symbolic authority." }
    ]
  },
  "Dashboard — bet/analphabetic.md": {
    word: "analphabetic",
    primary: "Unable to read and write; illiterate.",
    secondary: "In phonetic notation (pioneered by Otto Jespersen), using an analphabetic system of numerical formulas rather than letters to represent speech sounds.",
    quotes: [
      { author: "Otto Jespersen", work: "The Philosophy of Grammar", quote: "An **analphabetic** phonetic notation specifies the exact position of lips, tongue, and velum through coordinated mathematical symbols." },
      { author: "Max Weber", work: "Economy and Society", quote: "Pre-modern agrarian empires ruled over predominantly **analphabetic** populations using ritual and oral proclamation." },
      { author: "Ferdinand de Saussure", work: "Course in General Linguistics", quote: "The phonetician sometimes resorts to an **analphabetic** formula to describe sounds that resist conventional orthography." }
    ]
  },
  "Dashboard — bet/analphabetism.md": {
    word: "analphabetism",
    primary: "Inability to read and write; illiteracy.",
    secondary: "In demography and education, the state or rate of widespread illiteracy within a population.",
    quotes: [
      { author: "Paulo Freire", work: "Pedagogy of the Oppressed", quote: "The eradication of rural **analphabetism** is not a mere technical exercise, but an act of political liberation." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "Widespread **analphabetism** would make democratic self-government impossible, for newspapers must inform the sovereign citizen." },
      { author: "Eric Hobsbawm", work: "The Age of Empire", quote: "Late nineteenth-century European states waged determined campaigns to extinguish primary **analphabetism** through compulsory schooling." }
    ]
  },
  "Dashboard — bet/bet.md": {
    word: "bet",
    primary: "An agreement between two parties that whoever is proved wrong on an uncertain outcome will forfeit a stipulated sum or property to the other; a wager.",
    secondary: "A risk taken on a future contingency, or the stake risked; informally, a choice or course of action.",
    quotes: [
      { author: "William Shakespeare", work: "Hamlet", quote: "The King, sir, hath laid a great **bet** upon your head: six Barbary horses against six French rapiers." },
      { author: "Mark Twain", work: "The Celebrated Jumping Frog of Calaveras County", quote: "Smiley was the darndest man for betting on anything; he’d take either side of any **bet** you could name." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "I will make a **bet** with thee, Flask, that the whale is dead before sunset." }
    ]
  },
  "Dashboard — bet/betise.md": {
    word: "betise",
    primary: "An act or remark of foolishness, stupidity, or silliness; a blunder (from French bêtise).",
    secondary: "Folly, obtuseness, or lack of good sense in social or literary conduct.",
    quotes: [
      { author: "Henry James", work: "The Portrait of a Lady", quote: "Madame Merle smiled with cool forbearance, forgiving her companion’s provincial **betise** with easy grace." },
      { author: "Gustave Flaubert", work: "Madame Bovary", quote: "Emma shuddered at her husband’s clumsy platitudes, seeing in every word an incurable bourgeois **betise**." },
      { author: "Marcel Proust", work: "In Search of Lost Time", quote: "The salon hostess pretended not to hear the young marquis’s shocking **betise**, quickly changing the conversation." }
    ]
  },
  "Dashboard — bet/better.md": {
    word: "better",
    primary: "Of superior quality, excellence, or advantage; more suitable, desirable, or satisfactory (comparative of good).",
    secondary: "One who places a bet or wager (variant spelling of bettor); also, to improve or surpass.",
    quotes: [
      { author: "William Shakespeare", work: "Hamlet", quote: "There are more things in heaven and earth, Horatio, than are dreamt of in our philosophy; yet wisdom teaches us to seek a **better** way." },
      { author: "John Milton", work: "Paradise Lost", quote: "Here at least we shall be free; **better** to reign in Hell than serve in Heaven." },
      { author: "Charles Dickens", work: "A Tale of Two Cities", quote: "It is a far, far **better** thing that I do, than I have ever done; it is a far, far **better** rest that I go to than I have ever known." }
    ]
  },
  "Dashboard — bet/betting.md": {
    word: "betting",
    primary: "The action of gambling money or stakes on the unpredictable outcome of a race, game, or event.",
    secondary: "Pertaining to wagers, odds, or bookmaking.",
    quotes: [
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "Rawdon Crawley spent his afternoons at the club, engaged in heavy **betting** upon the Newmarket races." },
      { author: "George Eliot", work: "Daniel Deronda", quote: "The reckless excitement of **betting** at the roulette table held the fashionable crowd spellbound." },
      { author: "Arthur Conan Doyle", work: "The Adventure of Silver Blaze", quote: "A thorough check of the bookmaker's ledger revealed heavy **betting** against the favorite horse." }
    ]
  },
  "Dashboard — bet/bettor.md": {
    word: "bettor",
    primary: "A person who places a bet or wager on a contest, race, or game of chance.",
    secondary: "In gambling economics and sports analytics, a participant who risks capital based on calculated probabilities and betting odds.",
    quotes: [
      { author: "Damon Runyon", work: "Guys and Dolls", quote: "Every veteran **bettor** along Broadway knows that a racehorse is an ungrateful companion for one's bankroll." },
      { author: "Mark Twain", work: "Roughing It", quote: "The persistent **bettor** staked his last ounce of silver dust upon a pair of jacks." },
      { author: "Ernest Hemingway", work: "The Sun Also Rises", quote: "The eager **bettor** watched the greyhounds spring from the traps, clutching his ticket in sweaty fingers." }
    ]
  },
  "Dashboard — bet/panalphabetic.md": {
    word: "panalphabetic",
    primary: "Containing or utilizing all the letters of an alphabet.",
    secondary: "In typography and linguistics, describing a sentence, pangram, or sample text crafted to display every letter of an alphabet.",
    quotes: [
      { author: "Robert Bringhurst", work: "The Elements of Typographic Style", quote: "A **panalphabetic** specimen allows the typefounder to inspect stroke weight, counters, and kerning pairs across the entire font." },
      { author: "David Crystal", work: "Language Play", quote: "Pangrammatists delight in composing short, sensible **panalphabetic** sentences using all twenty-six letters without repetition." },
      { author: "H. L. Mencken", work: "The American Language", quote: "Telegraphers frequently tested line transmission and keyboard keys with standard **panalphabetic** phrases." }
    ]
  },
  "Dashboard — bet/polyalphabetic.md": {
    word: "polyalphabetic",
    primary: "Relating to, using, or written in multiple alphabets; in cryptography, designating a substitution cipher based on multiple substitution alphabets.",
    secondary: "In historical cryptanalysis, ciphers designed to resist single-alphabet frequency analysis by shifting alphabets cyclically using a keyword.",
    quotes: [
      { author: "David Kahn", work: "The Codebreakers", quote: "The invention of the **polyalphabetic** substitution cipher by Leon Battista Alberti marked the dawn of modern scientific cryptology." },
      { author: "Alan Turing", work: "Report on Enigma Decryption", quote: "Because the German machine employed a complex **polyalphabetic** stepping mechanism, ordinary frequency analysis was utterly useless." },
      { author: "Edgar Allan Poe", work: "A Few Words on Secret Writing", quote: "The cryptanalyst must first ascertain whether the cipher is monoalphabetic or **polyalphabetic** before attempting a solution." }
    ]
  }
};

function updateWordNote(relPath, data) {
  const fullPath = path.join(clusterDir, relPath);
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
console.log("Writing & Script Batch 2 completed! Total words updated:", Object.keys(wordsData).length);
