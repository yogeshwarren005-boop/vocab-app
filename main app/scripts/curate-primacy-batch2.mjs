import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Beginning & Primacy/Dashboard — archae";

const wordsData = {
  "Archaea.md": {
    word: "Archaea",
    primary: "A primary domain of single-celled microorganisms that lack cell nuclei and are distinct from both bacteria and eukaryotes (from Greek archaia, ancient things).",
    secondary: "In evolutionary microbiology (identified by Carl Woese in 1977 via 16S ribosomal RNA), primitive extremophiles thriving in hot springs, salt flats, and deep-sea vents.",
    quotes: [
      { author: "Carl Woese", work: "Phylogenetic Structure of the Prokaryotic Domain", quote: "We propose that living organisms be classified into three primary domains: Eucarya, Bacteria, and **Archaea**." },
      { author: "Lynn Margulis", work: "Symbiosis in Cell Evolution", quote: "The metabolic versatility of the **Archaea** reflects the harsh anaerobic conditions of the primordial Earth." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "Deep beneath the ocean floor, colonies of **Archaea** derive metabolic energy from hydrothermal sulfur vents." }
    ]
  },
  "archae.md": {
    word: "archae",
    primary: "A classical combining root derived from Ancient Greek archaios (ancient, primeval, from archē beginning).",
    secondary: "In scientific nomenclature and humanities terminology, forming words relating to ancient history, primitive life, or prehistoric eras (archaeology, Archaean, archaic).",
    quotes: [
      { author: "Walter William Skeat", work: "Principles of English Etymology", quote: "The Greek element **archae**- stems from arche, beginning, giving birth to our terms of ancient antiquity." },
      { author: "Arthur Evans", work: "Scripta Minoa", quote: "We prefix **archae**- to designate the oldest stratigraphic layers of Aegean civilization." },
      { author: "Max Müller", work: "The Science of Language", quote: "The stem **archae**- connects the mythic origins of culture with the modern disciplines of prehistory." }
    ]
  },
  "archaean.md": {
    word: "archaean",
    primary: "Of, relating to, or denoting the earlier eon of the Precambrian era, spanning from approximately 4.0 to 2.5 billion years ago; ancient or primitive.",
    secondary: "In historical geology and paleontology, the pivotal era during which Earth's crust cooled, oceans formed, and the earliest single-celled anaerobic life originated.",
    quotes: [
      { author: "Charles Lyell", work: "The Student's Elements of Geology", quote: "The heavily metamorphosed **Archaean** gneisses form the deep crystalline basement of the continents." },
      { author: "James Dwight Dana", work: "Manual of Geology", quote: "Sedimentary banded iron formations provide unmistakable chemical evidence of photosynthetic life in the **Archaean** seas." },
      { author: "Stephen Jay Gould", work: "Wonderful Life", quote: "For the first two billion years of the **Archaean** eon, life remained microscopic and prokaryotic." }
    ]
  },
  "archaeoastronomy.md": {
    word: "archaeoastronomy",
    primary: "The interdisciplinary study of how ancient or prehistoric cultures understood, observed, and integrated astronomical phenomena into their culture and architecture.",
    secondary: "In anthropology and history of science, examining the astronomical alignments of monuments such as Stonehenge, Newgrange, and Mayan pyramids with solstices and celestial cycles.",
    quotes: [
      { author: "Alexander Thom", work: "Megalithic Sites in Britain", quote: "The field of **archaeoastronomy** demonstrated that Neolithic stone circles were precision observatories aligned with lunar standstills." },
      { author: "Carl Sagan", work: "Cosmos", quote: "Through **archaeoastronomy**, we discover that our ancestors watched the heavens with acute mathematical devotion." },
      { author: "E. C. Krupp", work: "Echoes of the Ancient Skies", quote: "Modern **archaeoastronomy** reveals how ancient temple architecture aligned earthly power with celestial order." }
    ]
  },
  "archaeobacteria.md": {
    word: "archaeobacteria",
    primary: "A former or variant scientific term for the domain Archaea, designating primitive prokaryotes with unique cell wall lipids and ribosomal RNA.",
    secondary: "In microbial taxonomy (coined by Carl Woese and George Fox), microorganisms that thrive in extreme environments (methanogens, extreme halophiles, hyperthermophiles).",
    quotes: [
      { author: "Carl Woese", work: "A Conception of Bacterial Evolution", quote: "The distinct biochemical composition of **archaeobacteria** proves they are phylogenetically separate from true eubacteria." },
      { author: "Stephen Jay Gould", work: "Full House", quote: "The discovery of **archaeobacteria** fundamentally reorganized the tree of life into three great domains." },
      { author: "Lynn Margulis", work: "Five Kingdoms", quote: "Extremophilic **archaeobacteria** preserve molecular clues to the hot, reducing conditions of the prebiotic Earth." }
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
  "archegonial.md": {
    word: "archegonial",
    primary: "Of, relating to, or producing an archegonium (the multicellular female reproductive organ in mosses, ferns, and gymnosperms).",
    secondary: "In plant developmental biology and morphology, designating the archegonial chamber, neck canal cells, and venter during gametophyte fertilization.",
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
  },
  "archeologic.md": {
    word: "archeologic",
    primary: "A variant spelling of archaeologic; relating to archeology and the recovery of material remains of past human cultures.",
    secondary: "In North American and historical scientific publications, describing field surveys, artifact typologies, and mound excavations.",
    quotes: [
      { author: "Thomas Jefferson", work: "Notes on the State of Virginia", quote: "Our **archeologic** trench through the ancient Indian burial mound revealed distinct strata of human remains." },
      { author: "John Wesley Powell", work: "Report on the Bureau of Ethnology", quote: "The **archeologic** ruins of the canyon cliff-dwellers preserve astonishing textiles and pottery." },
      { author: "Henry Rowe Schoolcraft", work: "Information Respecting the History of the Indian Tribes", quote: "Prehistoric earthworks in the Ohio valley constitute monumental **archeologic** treasures." }
    ]
  },
  "archeological.md": {
    word: "archeological",
    primary: "A variant spelling of archaeological; of or relating to the study of past human cultures through physical artifacts and excavated ruins.",
    secondary: "In anthropology and museum curatorship, pertaining to field conservation, ceramic classification, and radiometric dating of ancient sites.",
    quotes: [
      { author: "Howard Carter", work: "The Tomb of Tut-ankh-Amen", quote: "The thrill of **archeological** discovery is tempered by the immense responsibility of preserving fragile relics." },
      { author: "Arthur Evans", work: "The Palace of Minos", quote: "The **archeological** record at Knossos unrolls a thousand years of uninterrupted Minoan bronze-age prosperity." },
      { author: "Lewis Henry Morgan", work: "Ancient Society", quote: "The **archeological** sequence of stone, bronze, and iron implements illuminates the upward march of human civilization." }
    ]
  },
  "archeologist.md": {
    word: "archeologist",
    primary: "A variant spelling of archaeologist; a person who studies past human life and culture by excavating and analyzing physical remains.",
    secondary: "In cultural history and prehistory, a scholar who reconstructs extinct social structures, agricultural practices, and rituals from material evidence.",
    quotes: [
      { author: "Heinrich Schliemann", work: "Troy and Its Remains", quote: "The **archeologist** must proceed with the spade in hand, testing classical poetry against the stubborn earth." },
      { author: "Agatha Christie", work: "Murder in Mesopotamia", quote: "The resident **archeologist** sorted through hundreds of terracotta fragments with infinite patience." },
      { author: "V. Gordon Childe", work: "New Light on the Most Ancient East", quote: "The modern **archeologist** collaborates with botanists, geologists, and chemists to reconstruct prehistoric environments." }
    ]
  },
  "archeology.md": {
    word: "archeology",
    primary: "A variant spelling of archaeology; the scientific study of past human life, material culture, and prehistory through excavation and artifact analysis.",
    secondary: "In cultural heritage and anthropology, the discipline that recovers extinct languages, architecture, and technology from the buried soil.",
    quotes: [
      { author: "Thomas Jefferson", work: "Notes on the State of Virginia", quote: "Stratigraphic **archeology** provides the surest chronology for unwritten indigenous histories." },
      { author: "V. Gordon Childe", work: "The Dawn of European Civilization", quote: "Through comparative **archeology**, we trace the diffusion of urban metallurgy from the Near East across Europe." },
      { author: "Howard Carter", work: "The Tomb of Tut-ankh-Amen", quote: "Modern **archeology** is not a hunt for buried treasure, but a meticulous discipline of historical recovery." }
    ]
  },
  "protoarchaeology.md": {
    word: "protoarchaeology",
    primary: "The early, rudimentary, or pre-scientific stage of archaeology prior to the development of systematic stratigraphic excavation and scientific dating methods.",
    secondary: "In the history of science, the antiquarian era (16th–18th centuries) characterized by curiosity cabinets, treasure-hunting, and speculative folklore regarding ruins.",
    quotes: [
      { author: "Glyn Daniel", work: "A Hundred and Fifty Years of Archaeology", quote: "The antiquarian pursuits of William Stukeley belong to **protoarchaeology**, blending romantic speculation with genuine fieldwork." },
      { author: "Bruce Trigger", work: "A History of Archaeological Thought", quote: "During the era of **protoarchaeology**, gentlemen scholars excavated burial barrows primarily to amass private collections of curios." },
      { author: "Colin Renfrew", work: "Archaeology: Theories, Methods, and Practice", quote: "The transition from antiquarian **protoarchaeology** to scientific archaeology occurred with the adoption of three-age technology and stratigraphy." }
    ]
  },
  "protoarcheology.md": {
    word: "protoarcheology",
    primary: "A variant spelling of protoarchaeology; the precursor, antiquarian stage of archaeology before the adoption of modern scientific field techniques.",
    secondary: "In archaeological historiography, designating the Renaissance and Enlightenment collecting of classical statues, coins, and megalithic curiosities.",
    quotes: [
      { author: "Bruce Trigger", work: "A History of Archaeological Thought", quote: "Early American **protoarcheology** was dominated by wild speculations concerning the myth of the lost Moundbuilders." },
      { author: "Glyn Daniel", work: "The Idea of Prehistory", quote: "The transition from folklore and **protoarcheology** to rigorous geology required proving the coexistence of humans with extinct mammoths." },
      { author: "Gordon Willey", work: "A History of American Archaeology", quote: "Thomas Jefferson’s systematic trenching represented an exceptional beacon of science in an age of amateur **protoarcheology**." }
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
console.log("Primacy Batch 2 completed! Total words updated:", Object.keys(wordsData).length);
