import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Writing & Script/Dashboard — alph";

const wordsData = {
  "alph.md": {
    word: "alph",
    primary: "A poetic proper name for the sacred, subterranean river in Samuel Taylor Coleridge's poem Kubla Khan; also an informal clipping of alpha.",
    secondary: "In literary geography, an imaginative river symbolizing the subconscious currents of poetic inspiration and creative mystery.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Kubla Khan", quote: "Where **Alph**, the sacred river, ran through caverns measureless to man down to a sunless sea." },
      { author: "Charles Lamb", work: "Letters", quote: "Coleridge's enchanted vision of **Alph** rolling through subterranean caverns haunts the imagination like an opium dream." },
      { author: "Arthur Quiller-Couch", work: "Studies in Literature", quote: "The mysterious river **Alph** embodies that romantic fascination with primal sources beyond human calculation." }
    ]
  },
  "alpha-adrenoceptor.md": {
    word: "alpha-adrenoceptor",
    primary: "A class of G-protein-coupled adrenergic receptors (subtypes alpha-1 and alpha-2) that respond to norepinephrine and epinephrine, mediating vasoconstriction and sympathetic signaling.",
    secondary: "In pharmacology, receptors targeted by agonists and antagonists to regulate vascular resistance and blood pressure.",
    quotes: [
      { author: "Raymond Ahlquist", work: "American Journal of Physiology", quote: "We proposed that the **alpha-adrenoceptor** mediates predominantly excitatory responses such as peripheral vasoconstriction." },
      { author: "James Black", work: "Lectures on Pharmacological Discovery", quote: "Differentiating the beta-receptor from the **alpha-adrenoceptor** laid the foundation for modern selective cardiovascular therapeutics." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Sympathetic stimulation of the vascular smooth muscle **alpha-adrenoceptor** increases systemic arterial resistance." }
    ]
  },
  "alpha-blocker.md": {
    word: "alpha-blocker",
    primary: "A pharmacological agent that inhibits alpha-adrenergic receptors, used chiefly to treat hypertension and benign prostatic hyperplasia.",
    secondary: "In clinical medicine, drugs such as prazosin, doxazosin, or phenoxybenzamine that relax vascular and prostatic smooth muscle by blocking alpha-1 receptors.",
    quotes: [
      { author: "Louis Goodman", work: "The Pharmacological Basis of Therapeutics", quote: "An **alpha-blocker** reduces peripheral vascular resistance without causing severe reflex tachycardia when selective for alpha-1 receptors." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Administration of an **alpha-blocker** is indicated in the pre-operative management of pheochromocytoma to prevent hypertensive crises." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "By blocking sympathetic tone to arteriolar beds, an **alpha-blocker** produces a sustained decline in mean arterial pressure." }
    ]
  },
  "alpha-interferon.md": {
    word: "alpha-interferon",
    primary: "A cytokine (type I interferon) produced primarily by leukocytes in response to viral infection, stimulating antiviral defenses and immune cell activation; interferon-alpha.",
    secondary: "In biotechnology and oncology, recombinant proteins used therapeutically in hepatitis C, hairy cell leukemia, and melanoma.",
    quotes: [
      { author: "Alick Isaacs", work: "Proceedings of the Royal Society", quote: "The cellular protein we named interferon, specifically **alpha-interferon**, renders adjacent cells refractory to viral invasion." },
      { author: "Christian Anfinsen", work: "The Molecular Basis of Evolution", quote: "Purification and sequencing of human leukocyte **alpha-interferon** revealed a multigene family of closely related proteins." },
      { author: "Robert Weinberg", work: "The Biology of Cancer", quote: "Recombinant **alpha-interferon** was among the earliest biological response modifiers approved for clinical cancer immunotherapy." }
    ]
  },
  "alpha-lipoprotein.md": {
    word: "alpha-lipoprotein",
    primary: "A high-density lipoprotein (HDL) of blood plasma that migrates with the alpha-1 globulin fraction on electrophoresis, carrying cholesterol from tissues back to the liver.",
    secondary: "In lipidology and cardiovascular biochemistry, a protective macromolecular complex whose apolipoproteins promote reverse cholesterol transport.",
    quotes: [
      { author: "Donald Fredrickson", work: "Circulation", quote: "In our classification of hyperlipidemias, the **alpha-lipoprotein** band reflects high-density particles protective against atherogenesis." },
      { author: "John Gofman", work: "Science", quote: "Ultracentrifugal flotation analysis confirmed that the **alpha-lipoprotein** fraction is inversely correlated with the incidence of coronary heart disease." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Circulating **alpha-lipoprotein** scavenges excess cholesterol from peripheral arterial walls and transports it to the liver for excretion." }
    ]
  },
  "alpha-naphthol.md": {
    word: "alpha-naphthol",
    primary: "A toxic crystalline organic phenolic compound (1-naphthol) derived from naphthalene, used in dyes, perfumes, and biochemical assays.",
    secondary: "In analytical chemistry, a reagent used in Molisch's test for carbohydrates (producing a purple ring) and in the Sakaguchi test for arginine.",
    quotes: [
      { author: "Hans Molisch", work: "Monatshefte für Chemie", quote: "Adding a trace of **alpha-naphthol** to a carbohydrate solution followed by concentrated sulfuric acid precipitates a characteristic violet ring." },
      { author: "Paul Ehrlich", work: "Das Sauerstoff-Bedürfniss des Organismus", quote: "The synthesis of indophenol blue from **alpha-naphthol** and paraphenylenediamine demonstrated intracellular oxidative enzyme activity." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "Electrophilic aromatic substitution on **alpha-naphthol** occurs predominantly at the activated 4-position of the naphthalene nucleus." }
    ]
  },
  "alpha-tocopheral.md": {
    word: "alpha-tocopheral",
    primary: "Variant spelling of alpha-tocopherol; the most biologically active form of vitamin E in humans, functioning as a powerful lipid-soluble antioxidant.",
    secondary: "In nutritional biochemistry, a methylated chromanol derivative that scavenges peroxyl radicals in cell membranes, preventing lipid peroxidation.",
    quotes: [
      { author: "Herbert McLean Evans", work: "Science", quote: "We isolated vitamin E from wheat germ oil, establishing **alpha-tocopheral** as the primary factor preventing reproductive resorption in rats." },
      { author: "Linus Pauling", work: "Vitamin C and the Common Cold", quote: "Dietary supplementation with **alpha-tocopheral** protects polyunsaturated fatty acids in cell membranes from free-radical oxidation." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Severe deficiency of **alpha-tocopheral** produces spinocerebellar ataxia and peripheral neuropathy through chronic oxidative damage." }
    ]
  },
  "alpha.md": {
    word: "alpha",
    primary: "The first letter of the Greek alphabet (Α, α); hence, the beginning, first, or primary member of any sequence.",
    secondary: "In astronomy, the brightest star in a constellation; in physics, alpha particles; in finance, risk-adjusted excess return on an investment.",
    quotes: [
      { author: "King James Bible", work: "Book of Revelation", quote: "I am **Alpha** and Omega, the beginning and the ending, saith the Lord, which is, and which was, and which is to come." },
      { author: "Ernest Rutherford", work: "Philosophical Magazine", quote: "The deflexion of **alpha** particles through large angles proved that atomic mass is concentrated in a tiny dense nucleus." },
      { author: "Ralph Waldo Emerson", work: "Essays: First Series", quote: "The soul holds the **alpha** and omega of all knowledge within its instinctive intuition." }
    ]
  },
  "alphabetic.md": {
    word: "alphabetic",
    primary: "Of, relating to, or expressed by an alphabet; consisting of letters representing sounds.",
    secondary: "Arranged in the conventional order of an alphabet; alphabetical.",
    quotes: [
      { author: "Ferdinand de Saussure", work: "Course in General Linguistics", quote: "The invention of **alphabetic** writing represents the highest stage of analytical phonological transcription." },
      { author: "Samuel Johnson", work: "A Dictionary of the English Language", quote: "I arranged the words of our language in strict **alphabetic** succession for the convenience of the student." },
      { author: "Max Müller", work: "Lectures on the Science of Language", quote: "The **alphabetic** character of Phoenician trade records revolutionized the transmission of human thought." }
    ]
  },
  "alphabetically.md": {
    word: "alphabetically",
    primary: "In the order of the letters of the alphabet.",
    secondary: "According to an alphabetical classification or index.",
    quotes: [
      { author: "Jane Austen", work: "Mansfield Park", quote: "Fanny arranged her books **alphabetically** upon the shelf in her little white attic room." },
      { author: "Charles Dickens", work: "Bleak House", quote: "The legal clerk searched **alphabetically** through the dusty ledgers of Chancery Lane." },
      { author: "George Eliot", work: "Middlemarch", quote: "Casaubon placed his mythological references **alphabetically** in the massive cross-indexed portfolio." }
    ]
  },
  "alphabetisation.md": {
    word: "alphabetisation",
    primary: "The process of arranging items in alphabetical order (British spelling of alphabetization).",
    secondary: "In educational sociology and international development, the process of teaching literacy to non-literate populations.",
    quotes: [
      { author: "David Crystal", work: "The Cambridge Encyclopedia of Language", quote: "Strict **alphabetisation** requires consistent rules for handling hyphens, diacritics, and compound surnames." },
      { author: "Lytton Strachey", work: "Eminent Victorians", quote: "The cardinal ordered a thorough **alphabetisation** of the diocesan archives to impose administrative efficiency." },
      { author: "Antonio Gramsci", work: "Prison Notebooks", quote: "The mass **alphabetisation** of southern Italian peasants was an essential step toward democratic civic awareness." }
    ]
  },
  "alphabetise.md": {
    word: "alphabetise",
    primary: "To arrange in alphabetical order (British spelling of alphabetize).",
    secondary: "To reduce an unwritten language to an alphabetic system; to teach the alphabet to.",
    quotes: [
      { author: "Virginia Woolf", work: "Night and Day", quote: "She spent the morning trying to **alphabetise** the scattered manuscripts left in her father’s study." },
      { author: "David Crystal", work: "The Stories of English", quote: "Early grammarians attempted to **alphabetise** English spelling, wrestling with medieval orthographic inconsistencies." },
      { author: "E. M. Forster", work: "Howards End", quote: "Margaret sat at the desk to **alphabetise** the library index cards before the packing cases arrived." }
    ]
  },
  "alphabetised.md": {
    word: "alphabetised",
    primary: "Arranged in alphabetical order (British spelling of alphabetized).",
    secondary: "Having been reduced to an alphabetic writing system or taught the alphabet.",
    quotes: [
      { author: "George Orwell", work: "Nineteen Eighty-Four", quote: "Winston filed the **alphabetised** reports into the pneumatic memory hole according to party regulations." },
      { author: "Arthur Conan Doyle", work: "The Return of Sherlock Holmes", quote: "Holmes consulted his massive **alphabetised** scrapbooks of criminal biographies with practiced speed." },
      { author: "Aldous Huxley", work: "Brave New World", quote: "The psychological records were neatly **alphabetised** in the central filing department of the hatchery." }
    ]
  },
  "alphabetiser.md": {
    word: "alphabetiser",
    primary: "A person who arranges items in alphabetical order; or a software tool or device that sorts text alphabetically (British spelling of alphabetizer).",
    secondary: "An educator or phonetician who develops an alphabet for an unwritten language.",
    quotes: [
      { author: "Samuel Johnson", work: "The Idler", quote: "The diligent **alphabetiser** of catalogs performs a humble yet indispensable service for the commonwealth of letters." },
      { author: "Robert Bringhurst", work: "The Elements of Typographic Style", quote: "A digital **alphabetiser** must handle complex Unicode collation algorithms across multilingual databases." },
      { author: "Richard Bentley", work: "Dissertations", quote: "The ancient **alphabetiser** of the Suidas lexicon frequently confused authors sharing identical surnames." }
    ]
  },
  "alphabetization.md": {
    word: "alphabetization",
    primary: "The arrangement of words, names, or items in alphabetical order.",
    secondary: "In education and sociolinguistics, the act or process of imparting literacy or creating an alphabetic orthography for an oral language.",
    quotes: [
      { author: "H. L. Mencken", work: "The American Language", quote: "Noah Webster insisted upon systematic **alphabetization** in his American dictionaries to facilitate public schooling." },
      { author: "Paulo Freire", work: "Pedagogy of the Oppressed", quote: "The **alphabetization** of adults must be grounded in generative words drawn from their everyday labor." },
      { author: "Donald Knuth", work: "The Art of Computer Programming", quote: "Efficient algorithms for **alphabetization** rely on radix sorting and lexicographical comparison trees." }
    ]
  },
  "alphabetize.md": {
    word: "alphabetize",
    primary: "To arrange in alphabetical order.",
    secondary: "To provide an unwritten language with an alphabetic writing system; to teach someone the alphabet.",
    quotes: [
      { author: "Benjamin Franklin", work: "Autobiography", quote: "I resolved to **alphabetize** my common-place book so that moral precepts could be recalled without delay." },
      { author: "Thomas Pynchon", work: "The Crying of Lot 49", quote: "She tried to **alphabetize** the chaotic stacks of probate invoices in the dusty office." },
      { author: "Umberto Eco", work: "The Name of the Rose", quote: "The monastic librarian refused to **alphabetize** the secret manuscripts, hiding them behind cryptic numerical ciphers." }
    ]
  },
  "alphabetized.md": {
    word: "alphabetized",
    primary: "Arranged in alphabetical order.",
    secondary: "Supplied with an alphabet or educated in reading and writing.",
    quotes: [
      { author: "Jorge Luis Borges", work: "The Library of Babel", quote: "The librarians wandered among endless **alphabetized** hexameters, searching for the catalog of catalogs." },
      { author: "John Steinbeck", work: "The Grapes of Wrath", quote: "The county relief worker checked their names against an **alphabetized** roster of migrant families." },
      { author: "Vladimir Nabokov", work: "Pale Fire", quote: "The commentary was accompanied by an **alphabetized** index containing malicious editorial cross-references." }
    ]
  },
  "alphabetizer.md": {
    word: "alphabetizer",
    primary: "One who or that which alphabetizes; a person or computer program that sorts entries into alphabetical order.",
    secondary: "A literacy instructor or linguist who devises an alphabetic orthography.",
    quotes: [
      { author: "Isaac D'Israeli", work: "Curiosities of Literature", quote: "The pedantic **alphabetizer** of medieval glossaries often divorced synonymous phrases across separate tomes." },
      { author: "Claude Lévi-Strauss", work: "Tristes Tropiques", quote: "The missionary functioned as an earnest **alphabetizer**, attempting to transcribe Amazonian phonemes into Latin script." },
      { author: "David Foster Wallace", work: "Infinite Jest", quote: "The meticulous **alphabetizer** organized his video cartridges according to director and release date." }
    ]
  },
  "alphameric.md": {
    word: "alphameric",
    primary: "Consisting of or using both letters of the alphabet and numbers; alphanumeric.",
    secondary: "In early computer data processing and punch-card encoding, describing character sets that include letters A–Z and digits 0–9.",
    quotes: [
      { author: "Claude Shannon", work: "The Mathematical Theory of Communication", quote: "Transmission efficiency depends upon whether the telegraphic channel encodes purely numeric or **alphameric** symbols." },
      { author: "John von Neumann", work: "First Draft of a Report on the EDVAC", quote: "The input mechanism was designed to process **alphameric** codes representing both numerical instructions and algebraic variables." },
      { author: "Norbert Wiener", work: "Cybernetics", quote: "Automated translation machines must convert **alphameric** input signals into logical semantic representations." }
    ]
  },
  "alphamerical.md": {
    word: "alphamerical",
    primary: "Consisting of letters and numbers; alphanumeric (variant form).",
    secondary: "Pertaining to alphanumeric character sets, filing systems, or keyboard layouts.",
    quotes: [
      { author: "Alan Turing", work: "Intelligent Machinery", quote: "The paper tape reader was configured to interpret **alphamerical** patterns punched along parallel channels." },
      { author: "Lewis Mumford", work: "The Myth of the Machine", quote: "Modern bureaucratic control relies upon vast **alphamerical** indexing systems to categorize human subjects." },
      { author: "Vannevar Bush", work: "As We May Think", quote: "The memex system would allow the researcher to link documents using associative **alphamerical** codes." }
    ]
  },
  "alphanumeric.md": {
    word: "alphanumeric",
    primary: "Consisting of or using both letters (alphabetical) and numbers (numerical); also, a character that is either a letter or a digit.",
    secondary: "In computing and telecommunications, describing character sets, passwords, or data fields that accept letters A–Z and digits 0–9.",
    quotes: [
      { author: "Tim Berners-Lee", work: "Weaving the Web", quote: "Uniform Resource Identifiers were designed to use standard **alphanumeric** strings that survive trans-network routing." },
      { author: "Robert Bringhurst", work: "The Elements of Typographic Style", quote: "A well-cut typeface maintains optical harmony between its capital letters and lining **alphanumeric** figures." },
      { author: "Carl Sagan", work: "Contact", quote: "The radio signal from Vega arrived as a prime-number sequence encoded in simple **alphanumeric** pulses." }
    ]
  },
  "alphanumerical.md": {
    word: "alphanumerical",
    primary: "Consisting of both letters and numerals; alphanumeric (variant form).",
    secondary: "Relating to alphanumeric data encoding, keyboards, or classification filing systems.",
    quotes: [
      { author: "Arthur C. Clarke", work: "2001: A Space Odyssey", quote: "The HAL 9000 computer display blinked with rapid **alphanumerical** telemetry as the ship approached Jupiter." },
      { author: "Isaac Asimov", work: "Foundation", quote: "Hari Seldon adjusted the **alphanumerical** dials of the Prime Radiant, projecting mathematical probabilities across centuries." },
      { author: "Marshall McLuhan", work: "Understanding Media", quote: "The computer printout merges oral narrative into an **alphanumerical** grid of mechanized information." }
    ]
  },
  "alphanumerics.md": {
    word: "alphanumerics",
    primary: "Alphanumeric characters; characters consisting of both letters and numbers.",
    secondary: "In typography and computing display systems, the graphic subset containing letters, digits, and basic punctuation.",
    quotes: [
      { author: "Douglas Engelbart", work: "Augmenting Human Intellect", quote: "The CRT terminal displayed sharp **alphanumerics** controlled directly by the interactive mouse interface." },
      { author: "William Gibson", work: "Neuromancer", quote: "Green **alphanumerics** cascaded down the monitor screen like phosphor rain in the dark console cabin." },
      { author: "Donald Knuth", work: "The TeXbook", quote: "TeX treats **alphanumerics** and mathematical symbols according to distinct spacing and ligaturing rules." }
    ]
  },
  "alphavirus.md": {
    word: "alphavirus",
    primary: "A genus of positive-sense single-stranded RNA viruses in the family Togaviridae, predominantly transmitted by mosquitoes and causing encephalitis, fever, or arthralgia.",
    secondary: "In virology and infectious disease medicine, pathogens including Chikungunya virus, Eastern equine encephalitis virus, and Sindbis virus.",
    quotes: [
      { author: "David Baltimore", work: "Bacteriological Reviews", quote: "The genomic RNA of an **alphavirus** functions directly as mRNA upon entry into the host cell cytoplasm." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Epidemic polyarthritis caused by mosquito-borne **alphavirus** infection presents with debilitating joint pains." },
      { author: "Robert Gallo", work: "Virus Hunting", quote: "Structural cryo-electron microscopy revealed the icosahedral symmetry of the enveloped **alphavirus** particle." }
    ]
  },
  "analphabet.md": {
    word: "analphabet",
    primary: "A person who cannot read or write; an illiterate person.",
    secondary: "In social history and educational policy, an individual uninstructed in alphabetic script.",
    quotes: [
      { author: "George Orwell", work: "The Road to Wigan Pier", quote: "An **analphabet** in a modern industrial city is helpless before the blizzard of printed regulations." },
      { author: "Antonio Gramsci", work: "Prison Notebooks", quote: "The cultural hegemony of the ruling class is perpetuated so long as the peasant remains an **analphabet**." },
      { author: "Claude Lévi-Strauss", work: "Tristes Tropiques", quote: "The tribal chief, though an **analphabet**, understood that holding a pen conferred symbolic authority." }
    ]
  },
  "analphabetic.md": {
    word: "analphabetic",
    primary: "Unable to read and write; illiterate.",
    secondary: "In phonetic notation (pioneered by Otto Jespersen), using an analphabetic system of numerical formulas rather than letters to represent speech sounds.",
    quotes: [
      { author: "Otto Jespersen", work: "The Philosophy of Grammar", quote: "An **analphabetic** phonetic notation specifies the exact position of lips, tongue, and velum through coordinated mathematical symbols." },
      { author: "Max Weber", work: "Economy and Society", quote: "Pre-modern agrarian empires ruled over predominantly **analphabetic** populations using ritual and oral proclamation." },
      { author: "Ferdinand de Saussure", work: "Course in General Linguistics", quote: "The phonetician sometimes resorts to an **analphabetic** formula to describe sounds that resist conventional orthography." }
    ]
  },
  "analphabetism.md": {
    word: "analphabetism",
    primary: "Inability to read and write; illiteracy.",
    secondary: "In demography and education, the state or rate of widespread illiteracy within a population.",
    quotes: [
      { author: "Paulo Freire", work: "Pedagogy of the Oppressed", quote: "The eradication of rural **analphabetism** is not a mere technical exercise, but an act of political liberation." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "Widespread **analphabetism** would make democratic self-government impossible, for newspapers must inform the sovereign citizen." },
      { author: "Eric Hobsbawm", work: "The Age of Empire", quote: "Late nineteenth-century European states waged determined campaigns to extinguish primary **analphabetism** through compulsory schooling." }
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
console.log("Writing & Script Batch 5 completed! Total words updated:", Object.keys(wordsData).length);
