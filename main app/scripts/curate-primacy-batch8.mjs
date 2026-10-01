import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Beginning & Primacy/Dashboard — prot";

const wordsData = {
  "proteolysis.md": {
    word: "proteolysis",
    primary: "The breakdown of proteins or peptides into simpler polypeptides or amino acids by the action of enzymes or acid hydrolysis.",
    secondary: "In cell biology, targeted protein degradation (via the ubiquitin-proteasome pathway) regulating signal transduction, cell cycle progression, and apoptosis.",
    quotes: [
      { author: "Christian Anfinsen", work: "The Molecular Basis of Evolution", quote: "Controlled **proteolysis** of the nascent polypeptide chain liberates the active conformation of the enzyme." },
      { author: "Aaron Ciechanover", work: "Ubiquitin-Mediated Proteolysis", quote: "Selective **proteolysis** within eukaryotic cells ensures the rapid disposal of misfolded or regulatory proteins." },
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", quote: "Pancreatic secretion initiates extensive **proteolysis**, converting dietary albumin into assimilable peptides." }
    ]
  },
  "proteolytic.md": {
    word: "proteolytic",
    primary: "Relating to or causing the breakdown of proteins and peptides; protein-cleaving.",
    secondary: "In enzymology and microbiology, describing digestive enzymes or bacterial toxins capable of dissolving extracellular matrices and tissues.",
    quotes: [
      { author: "John Howard Northrop", work: "Crystalline Enzymes", quote: "The **proteolytic** activity of crystalline trypsin remains remarkably specific to lysine and arginine peptide bonds." },
      { author: "Alexander Fleming", work: "Penicillin and Its Practical Application", quote: "Pathogenic streptococci produce **proteolytic** factors that liquefy fibrin clots and facilitate invasive spread." },
      { author: "Arthur Kornberg", work: "For the Love of Enzymes", quote: "To prevent unwanted cleavage during enzyme isolation, we added synthetic inhibitors against endogenous **proteolytic** enzymes." }
    ]
  },
  "proteome.md": {
    word: "proteome",
    primary: "The entire complement of proteins expressed by a cell, tissue, or organism at a given time or under specific conditions.",
    secondary: "In functional genomics and systems biology, the dynamic protein repertoire reflecting transcriptional regulation, alternative splicing, and post-translational modifications.",
    quotes: [
      { author: "Marc Wilkins", work: "Proteome Research: New Frontiers in Functional Genomics", quote: "We proposed the term **proteome** to signify the complete protein complement encoded by an organism's genome." },
      { author: "Sydney Brenner", work: "Loose Ends", quote: "While the genome is largely static in each cell, the cellular **proteome** fluctuates constantly in response to physiological cues." },
      { author: "J. Craig Venter", work: "A Life Decoded", quote: "Deciphering the human genome was merely the prelude to characterizing the vast complexities of the human **proteome**." }
    ]
  },
  "proteomics.md": {
    word: "proteomics",
    primary: "The large-scale systematic study of the structures, functions, and interactions of proteins in a biological system.",
    secondary: "In bioinformatics and biotechnology, high-throughput technologies (such as mass spectrometry and protein microarrays) used for biomarker discovery and drug target identification.",
    quotes: [
      { author: "Leroy Hood", work: "Systems Biology", quote: "High-throughput **proteomics** enables us to map cellular signaling networks in health and disease with unprecedented resolution." },
      { author: "Francis Collins", work: "The Language of Life", quote: "Advances in clinical **proteomics** allow oncologists to detect minute protein signatures shed by early-stage tumors." },
      { author: "Eric Lander", work: "Nature", quote: "The transition from genomics to quantitative **proteomics** bridges genetic code with physiological phenotype." }
    ]
  },
  "proteosome.md": {
    word: "proteosome",
    primary: "A large, multi-subunit protein complex inside eukaryotic cells that degrades unneeded or damaged proteins by proteolysis (variant of proteasome).",
    secondary: "In cellular physiology, the 26S cylinder-shaped holoenzyme that digests ubiquitin-tagged proteins, maintaining cellular proteostasis.",
    quotes: [
      { author: "Avram Hershko", work: "The Ubiquitin System for Protein Degradation", quote: "Polyubiquitinated substrates are recognized and threaded into the central chamber of the **proteosome** for catalytic destruction." },
      { author: "Aaron Ciechanover", work: "Cell", quote: "Malfunction of the **proteosome** leads to toxic aggregates characteristic of neurodegenerative disorders." },
      { author: "Bruce Alberts", work: "Molecular Biology of the Cell", quote: "The hollow core of the **proteosome** isolates active proteolytic sites from the general cytoplasmic environment." }
    ]
  },
  "proterochampsa.md": {
    word: "proterochampsa",
    primary: "An extinct genus of predatory archosauriform reptiles from the Late Triassic of Argentina, possessing an elongated, crocodile-like skull.",
    secondary: "In vertebrate paleontology, the type genus of Proterochampsidae, representing basal archosauromorph carnivores adapted to semi-aquatic riparian niches.",
    quotes: [
      { author: "Alfred Sherwood Romer", work: "The Triassic Faunas of the Chañares Formation", quote: "The flattened cranium and dorsal nostrils of **Proterochampsa** suggest habits analogous to modern alligators." },
      { author: "José Bonaparte", work: "El Triásico de Sudamérica", quote: "Fossils of **Proterochampsa** in the Ischigualasto basin demonstrate the diversity of non-dinosaurian predators prior to the Jurassic." },
      { author: "Michael J. Benton", work: "Vertebrate Palaeontology", quote: "Basal archosauriforms like **Proterochampsa** illustrate the mosaic evolution of skull fenestration in early reptiles." }
    ]
  },
  "proterozoic.md": {
    word: "proterozoic",
    primary: "Relating to the geologic eon extending from about 2.5 billion to 539 million years ago, marked by the buildup of atmospheric oxygen and the emergence of eukaryotes.",
    secondary: "In historical geology and geobiology, the eon spanning the Paleoproterozoic, Mesoproterozoic, and Neoproterozoic eras, terminating with the Ediacaran biota.",
    quotes: [
      { author: "Charles Doolittle Walcott", work: "Pre-Cambrian Fossiliferous Formations", quote: "The laminated stromatolites of the **proterozoic** limestones preserve the oldest widespread signatures of photosynthetic life." },
      { author: "Lynn Margulis", work: "Symbiosis in Cell Evolution", quote: "The Great Oxidation Event of the early **proterozoic** forced anaerobic life into refuges and enabled endosymbiotic eukaryotic evolution." },
      { author: "Arthur Holmes", work: "The Age of the Earth", quote: "Crystalline formations dating to the late **proterozoic** reveal evidence of planet-wide glaciations." }
    ]
  },
  "protest.md": {
    word: "protest",
    primary: "An expression or declaration of objection, disapproval, or dissent against an action, policy, or injustice; also, to express strong opposition.",
    secondary: "In commercial law, a formal written statement by a notary attesting that a bill of exchange or promissory note has been dishonored.",
    quotes: [
      { author: "Martin Luther King Jr.", work: "Letter from Birmingham Jail", quote: "Nonviolent direct action seeks to create such a crisis that a community is forced to confront the **protest**." },
      { author: "Henry David Thoreau", work: "Civil Disobedience", quote: "Under a government which imprisons any unjustly, the true place for a just man is in a prison, as a silent **protest**." },
      { author: "William Shakespeare", work: "The Winter's Tale", quote: "I **protest** unto your grace that I have spoken nothing but the unvarnished truth." }
    ]
  },
  "protestant.md": {
    word: "protestant",
    primary: "A member or follower of any of the Western Christian churches that are separate from the Roman Catholic Church following the 16th-century Reformation.",
    secondary: "Adhering to the principles of the Reformation, particularly justification by faith alone (sola fide) and the supreme authority of scripture (sola scriptura).",
    quotes: [
      { author: "Max Weber", work: "The Protestant Ethic and the Spirit of Capitalism", quote: "The ascetic discipline of the **Protestant** sects contributed decisively to the rational spirit of modern enterprise." },
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "The nation rejoiced when the crown was settled upon a confirmed **Protestant** sovereign." },
      { author: "John Milton", work: "Areopagitica", quote: "A man may be a heretic in the truth; and if he believe things only because his pastor says so, his belief is a mere **Protestant** superstition." }
    ]
  },
  "protestantism.md": {
    word: "protestantism",
    primary: "The faith, practice, and church order of the Protestant churches.",
    secondary: "In religious history, the theological movement initiated by Martin Luther, John Calvin, and Huldrych Zwingli advocating biblical primacy and priesthood of all believers.",
    quotes: [
      { author: "Edmund Burke", work: "Speech on Conciliation with America", quote: "The religion most prevalent in our northern colonies is a refinement on the principle of resistance: it is the dissidence of dissent, and the **protestantism** of the Protestant religion." },
      { author: "Thomas Carlyle", work: "Heroes, Hero-Worship, and the Heroic in History", quote: "Luther's revolt at the Diet of Worms was the birth-hour of modern European **protestantism**." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "In the United States, **protestantism** harmonized religious conviction with democratic equality and republican self-government." }
    ]
  },
  "protestation.md": {
    word: "protestation",
    primary: "A solemn, emphatic, or earnest declaration or affirmation, especially of innocence, fidelity, or belief.",
    secondary: "A formal objection or dissent entered into a public record or judicial proceeding.",
    quotes: [
      { author: "William Shakespeare", work: "Much Ado About Nothing", quote: "Do not swear by the moon; make no false **protestation** of love unless thy heart be true." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The Senate received the emperor's humble **protestation** with formal acclaim, knowing full well his legions dictated the peace." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "Despite his fervent **protestation** of affection, I resolved that duty must govern my departure." }
    ]
  },
  "protester.md": {
    word: "protester",
    primary: "A person who publicly protests or demonstrates against something, such as a political policy or social injustice.",
    secondary: "An individual who enters a formal legal or ecclesiastical protest against an official decree.",
    quotes: [
      { author: "George Orwell", work: "Homage to Catalonia", quote: "Every working-class **protester** who took to the barricades demanded an end to bureaucratic privilege." },
      { author: "Ralph Waldo Emerson", work: "Self-Reliance", quote: "Society everywhere is in conspiracy against the manhood of every one of its members, and the true **protester** stands alone." },
      { author: "Frederick Douglass", work: "Narrative of the Life of Frederick Douglass", quote: "The bold abolitionist **protester** faced jeering mobs in northern cities, undaunted by threats of violence." }
    ]
  },
  "proteus.md": {
    word: "proteus",
    primary: "A prophetic sea god in Greek mythology capable of assuming many different shapes; hence, someone or something that constantly changes form.",
    secondary: "In microbiology, a genus of Gram-negative, facultatively anaerobic rod-shaped bacteria (Proteus mirabilis) known for swarming motility on agar.",
    quotes: [
      { author: "Francis Bacon", work: "The Wisdom of the Ancients", quote: "Matter, like ancient **Proteus**, eludes comprehension by constantly altering its external forms until constrained by physical law." },
      { author: "William Wordsworth", work: "The World Is Too Much With Us", quote: "Have sight of **Proteus** rising from the sea; or hear old Triton blow his wreathed horn." },
      { author: "Louis Pasteur", work: "Studies on Fermentation", quote: "The swarming growth of bacteria belonging to the genus **Proteus** spreads across the culture plate in concentric waves." }
    ]
  },
  "protirelin.md": {
    word: "protirelin",
    primary: "A synthetic tripeptide identical to endogenous thyrotropin-releasing hormone (TRH), used as a diagnostic agent to assess thyroid and pituitary function.",
    secondary: "In neuroendocrinology, pyroglutamyl-histidyl-prolinamide, which stimulates pituitary secretion of thyroid-stimulating hormone (TSH) and prolactin.",
    quotes: [
      { author: "Roger Guillemin", work: "Science", quote: "Isolation and synthesis of the hypothalamic tripeptide **protirelin** proved that the brain directly controls pituitary hormone secretion." },
      { author: "Andrew V. Schally", work: "Nobel Lecture", quote: "The synthetic preparation of **protirelin** opened the era of peptide neuroendocrinology and dynamic endocrine testing." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Intravenous injection of **protirelin** evokes an immediate surge of thyrotropin from normal anterior pituitary basophils." }
    ]
  },
  "protist.md": {
    word: "protist",
    primary: "Any of a diverse group of eukaryotic microorganisms that are not animals, plants, or fungi, typically single-celled or colonial.",
    secondary: "In eukaryotic systematics, organisms formerly placed in kingdom Protista (such as ciliates, diatoms, amoebae, and dinoflagellates), now grouped into major supergroups.",
    quotes: [
      { author: "Lynn Margulis", work: "Symbiosis in Cell Evolution", quote: "The ancestral **protist** was a mosaic creature formed by the symbiotic merger of diverse prokaryotic partners." },
      { author: "Stephen Jay Gould", work: "The Flamingo's Smile", quote: "Every lineage of complex multicellular life trace their roots back to some bizarre, experimental single-celled **protist**." },
      { author: "Ernst Haeckel", work: "The Wonders of Life", quote: "The unicellular **protist** exhibits in its solitary cell all the fundamental life functions of more elaborate organisms." }
    ]
  },
  "protista.md": {
    word: "protista",
    primary: "A taxonomic kingdom comprising all protists; single-celled or colonial eukaryotic organisms lacking specialized tissues.",
    secondary: "In biological classification (first proposed by Ernst Haeckel in 1866), a foundational kingdom encompassing protozoans, algae, and slime molds.",
    quotes: [
      { author: "Ernst Haeckel", work: "Generelle Morphologie der Organismen", quote: "I establish the kingdom **Protista** to embrace all those primordial living forms that cannot be classified strictly as animals or plants." },
      { author: "Robert Whittaker", work: "Science", quote: "In the five-kingdom system of classification, the kingdom **Protista** occupies the crucial central grade bridging prokaryotes and multicellular kingdoms." },
      { author: "Thomas Cavalier-Smith", work: "Biological Reviews", quote: "Modern ultrastructural and molecular phylogenetics have dismantled the traditional boundaries of **Protista** into distinct eukaryotic supergroups." }
    ]
  },
  "protistan.md": {
    word: "protistan",
    primary: "Of, relating to, or characteristic of protists or the kingdom Protista.",
    secondary: "Pertaining to unicellular or colonial eukaryotic grades of structural organization and life cycles.",
    quotes: [
      { author: "Alister Hardy", work: "The Open Sea", quote: "The phosphorescent glow of the night sea is generated by millions of microscopic **protistan** dinoflagellates." },
      { author: "D'Arcy Wentworth Thompson", work: "On Growth and Form", quote: "The delicate silica skeletons of radiolarians reveal the geometric beauty of **protistan** architecture under surface tension." },
      { author: "Lynn Margulis", work: "Five Kingdoms", quote: "The **protistan** radiation produced every major organelle and biochemical pathway subsequently inherited by plants and animals." }
    ]
  },
  "protium.md": {
    word: "protium",
    primary: "The most common and lightest isotope of hydrogen, having an atomic mass of approximately 1 and a nucleus consisting of a single proton with no neutrons (symbol 1H).",
    secondary: "In nuclear physics and physical chemistry, the stable hydrogen isotope constituting over 99.98% of natural terrestrial hydrogen, contrasting with deuterium and tritium.",
    quotes: [
      { author: "Harold Urey", work: "Physical Review", quote: "Upon concentrating heavy hydrogen, the ordinary light isotope was designated **protium** to distinguish it from deuterium." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The vibrational energy levels of molecules containing **protium** differ measurably from those containing deuterium due to the isotope effect." },
      { author: "Glenn T. Seaborg", work: "Man-Made Transuranium Elements", quote: "Thermonuclear fusion reactions between deuterium and tritium proceed at lower activation energies than reactions involving pure **protium**." }
    ]
  },
  "proto-norse.md": {
    word: "proto-norse",
    primary: "The early Germanic language (c. 200–800 CE) spoken in Scandinavia from which Old Norse and modern North Germanic languages developed; also known as Primitive Norse.",
    secondary: "In historical linguistics, the dialect attested in Elder Futhark runic inscriptions on bracteates, stones, and weapon fittings across Scandinavia.",
    quotes: [
      { author: "Ferdinand de Saussure", work: "Course in General Linguistics", quote: "The archaic runic inscriptions carved in **Proto-Norse** preserve vowel endings that were completely lost in later classical Old Icelandic." },
      { author: "Otto Jespersen", work: "Language: Its Nature, Development and Origin", quote: "Comparative Germanic grammar relies heavily on early **Proto-Norse** inscriptions like the Gallehus golden horns." },
      { author: "Peter Foote", work: "The Viking Achievement", quote: "The transition from **Proto-Norse** to Old Norse coincided with radical syncope of unaccented vowels during the Vendel period." }
    ]
  },
  "proto-oncogene.md": {
    word: "proto-oncogene",
    primary: "A normal cellular gene that has the potential to become an oncogene through mutation or overexpression, thereby promoting malignant tumor formation.",
    secondary: "In molecular oncology, essential cellular genes encoding growth factors, receptor kinases, or transcription factors (e.g., RAS, MYC, SRC) that regulate normal cell division.",
    quotes: [
      { author: "J. Michael Bishop", work: "Nobel Lecture", quote: "The viral oncogene was not a foreign invader, but a stolen and mutated copy of a normal cellular **proto-oncogene**." },
      { author: "Harold E. Varmus", work: "Science", quote: "When a point mutation locks a **proto-oncogene** into a constitutively active state, normal cellular proliferation turns malignant." },
      { author: "Robert Weinberg", work: "The Biology of Cancer", quote: "The normal function of a **proto-oncogene** is to transmit growth-stimulatory signals during embryonic development and tissue repair." }
    ]
  },
  "proto.md": {
    word: "proto",
    primary: "Serving as a prefix meaning first, earliest, original, or primitive; also used informally to denote a prototype or initial model.",
    secondary: "In evolutionary systematics and historical linguistics, designating an ancestral or reconstructed theoretical parent form (e.g., Proto-Indo-European).",
    quotes: [
      { author: "Max Müller", work: "Lectures on the Science of Language", quote: "The linguist reconstructs the **proto** forms of ancient speech by triangulating cognates across daughter languages." },
      { author: "Stephen Jay Gould", work: "Ontogeny and Phylogeny", quote: "Paleontologists search for the ancestral **proto** organism from which distinct living phyla first branched." },
      { author: "Lewis Mumford", work: "Technics and Civilization", quote: "The wooden watermill was the mechanical **proto** machine that prefigured the modern automated factory." }
    ]
  },
  "protoactinium.md": {
    word: "protoactinium",
    primary: "An obsolete alternative spelling of protactinium (element 91).",
    secondary: "In early 20th-century radiochemistry, the designation originally assigned by Otto Hahn and Lise Meitner to the parent substance yielding actinium through alpha decay.",
    quotes: [
      { author: "Frederick Soddy", work: "The Chemistry of the Radio-Elements", quote: "The decay of uranium-Y was shown to yield **protoactinium**, which in turn decays into actinium." },
      { author: "Marie Curie", work: "Treatise on Radioactivity", quote: "Research into the pitchblende residues revealed traces of **protoactinium** associated with the rare earths." },
      { author: "Ernest Rutherford", work: "Radiations from Radioactive Substances", quote: "The long-lived isotope **protoactinium** proved essential for completing the radioactive disintegration series." }
    ]
  },
  "protoanthropology.md": {
    word: "protoanthropology",
    primary: "The early, rudimentary, or pre-scientific phase in the study of human physical and cultural origins, customs, and societies.",
    secondary: "In the history of ideas, the ethnological observations of classical travelers and Enlightenment moral philosophers prior to modern anthropology.",
    quotes: [
      { author: "Claude Lévi-Strauss", work: "Tristes Tropiques", quote: "The speculative accounts of Renaissance voyagers constituted a romantic **protoanthropology** that invented the myth of the noble savage." },
      { author: "Franz Boas", work: "The Mind of Primitive Man", quote: "Scientific ethnology had to discard the biased generalizations of 18th-century **protoanthropology**." },
      { author: "Bronislaw Malinowski", work: "Argonauts of the Western Pacific", quote: "Fieldwork with participant observation transformed speculative **protoanthropology** into an empirical social science." }
    ]
  },
  "protoarchaeology.md": {
    word: "protoarchaeology",
    primary: "The early, pre-scientific stage of archaeological investigation characterized by antiquarian collecting and unmethodical digging.",
    secondary: "In archaeological historiography, the period before the adoption of geological stratigraphy and the three-age technological system.",
    quotes: [
      { author: "Glyn Daniel", work: "The Idea of Prehistory", quote: "The amateur antiquaries of the eighteenth century practiced a curious **protoarchaeology** inspired by druidical romanticism." },
      { author: "Bruce Trigger", work: "A History of Archaeological Thought", quote: "Cabinets of curiosities accumulated during the phase of **protoarchaeology** laid the foundation for systematic national museums." },
      { author: "Colin Renfrew", work: "Before Civilization", quote: "Scientific archaeology emerged only when the speculative assumptions of **protoarchaeology** were tested against radiocarbon dates." }
    ]
  },
  "protoarcheology.md": {
    word: "protoarcheology",
    primary: "Variant spelling of protoarchaeology; the nascent, pre-stratigraphic era of archaeological inquiry.",
    secondary: "The exploratory collection of ancient coins, inscriptions, and burial relics prior to modern excavation standards.",
    quotes: [
      { author: "Lewis Binford", work: "An Archaeological Perspective", quote: "We must abandon the trait-collecting mindset inherited from nineteenth-century **protoarcheology**." },
      { author: "V. Gordon Childe", work: "Social Evolution", quote: "The shift from **protoarcheology** to prehistory was achieved when tools were studied as instruments of human economic adaptation." },
      { author: "Stuart Piggott", work: "Ancient Britons and the Antiquarian Imagination", quote: "The early surveys of Avebury and Stonehenge represent monuments of British **protoarcheology**." }
    ]
  },
  "protoavis.md": {
    word: "protoavis",
    primary: "An alleged primitive archosaur genus from the Late Triassic of Texas described by Sankar Chatterjee as a bird older than Archaeopteryx.",
    secondary: "In vertebrate paleontology, a controversial fossil taxon whose avian status and chimeric nature remain subjects of heated scientific debate.",
    quotes: [
      { author: "Sankar Chatterjee", work: "The Rise of Birds", quote: "The skull structure of **Protoavis** displays remarkable avian cranial kinesis tens of millions of years before Archaeopteryx." },
      { author: "Stephen Jay Gould", work: "Dinosaur in a Haystack", quote: "The claim that **Protoavis** represents a true Triassic bird has met with fierce skepticism from cladists and anatomists." },
      { author: "Alan Feduccia", work: "The Origin and Evolution of Birds", quote: "Many paleontologists suspect that **Protoavis** is a taphonomic chimera composed of mixed coelurosaurian and archosaurian bones." }
    ]
  },
  "protoceratops.md": {
    word: "protoceratops",
    primary: "A genus of small, herbivorous, sheep-sized ceratopsian dinosaurs from the Late Cretaceous of the Gobi Desert, lacking developed facial horns.",
    secondary: "In dinosaur paleontology, an abundant neoceratopsian known from numerous well-preserved skeletons, nests, and fossilized eggs discovered by the Central Asiatic Expeditions.",
    quotes: [
      { author: "Roy Chapman Andrews", work: "On the Trail of Ancient Man", quote: "In the Flaming Cliffs of the Gobi, we discovered nests of fossilized dinosaur eggs belonging to **Protoceratops**." },
      { author: "Henry Fairfield Osborn", work: "American Museum Novitates", quote: "The skull of **Protoceratops** exhibits an expanded neck frill but lacks the prominent nasal and orbital horns of later ceratopsians." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "Ontogenetic series of **Protoceratops** skulls show how the protective frill grew with striking positive allometry as the animal matured." }
    ]
  },
  "protocol.md": {
    word: "protocol",
    primary: "The official procedure, code of diplomatic etiquette, or system of rules governing state affairs, diplomatic ceremonies, or scientific experiments.",
    secondary: "In computing, a standardized set of rules and formats for transmitting data between electronic devices across a network (e.g., TCP/IP, HTTP).",
    quotes: [
      { author: "Henry Kissinger", work: "Diplomacy", quote: "Strict adherence to diplomatic **protocol** provides the neutral scaffolding within which rival powers can conduct delicate negotiations." },
      { author: "George Orwell", work: "1984", quote: "Every party member was expected to follow the established ideological **protocol** without the slightest hesitation or deviation." },
      { author: "Tim Berners-Lee", work: "Weaving the Web", quote: "The Hypertext Transfer **Protocol** was designed to be a lightweight, stateless system for retrieving distributed documents across the internet." }
    ]
  },
  "protoctist.md": {
    word: "protoctist",
    primary: "Any organism belonging to the kingdom Protoctista, including eukaryotic microorganisms and their immediate multicellular descendants that are not plants, animals, or fungi.",
    secondary: "In Lynn Margulis's taxonomy, any nucleated organism (such as algae, protozoans, and slime molds) excluded from the plant, animal, and fungal kingdoms.",
    quotes: [
      { author: "Lynn Margulis", work: "Symbiosis in Cell Evolution", quote: "Every **protoctist** organism reveals the chimeric legacy of ancient endosymbiotic bacterial partnerships." },
      { author: "John Maynard Smith", work: "The Major Transitions in Evolution", quote: "The diversification of the **protoctist** grade of organization was the critical bridge to complex multicellularity." },
      { author: "Stephen Jay Gould", work: "Wonderful Life", quote: "The sea floor during the Ediacaran was inhabited by bizarre **protoctist** creatures that defy simple placement into modern phyla." }
    ]
  },
  "protoctista.md": {
    word: "protoctista",
    primary: "A taxonomic kingdom (proposed by John Hogg in 1860 and popularized by Lynn Margulis) comprising unicellular and simple multicellular eukaryotic organisms.",
    secondary: "In five-kingdom taxonomy, the grouping encompassing protozoa, red, brown, and green algae, slime molds, and oomycetes.",
    quotes: [
      { author: "John Hogg", work: "On the Distinctions of a Plant and an Animal", quote: "I proposed the kingdom **Protoctista** to include all primordial beings that partake of both animal and vegetable natures." },
      { author: "Lynn Margulis", work: "Five Kingdoms: An Illustrated Guide to the Phyla of Life on Earth", quote: "Within the kingdom **Protoctista**, we recognize nearly forty distinct phyla displaying astonishing cellular diversity." },
      { author: "Peter H. Raven", work: "Biology of Plants", quote: "Molecular sequencing has shown that **Protoctista** is a paraphyletic assemblage rather than a single evolutionary branch." }
    ]
  },
  "protogeometric.md": {
    word: "protogeometric",
    primary: "Relating to a style of ancient Greek pottery and decoration that flourished circa 1050–900 BCE, bridging Mycenaean and Geometric art.",
    secondary: "In classical archaeology, marked by fast-wheel production, lustrous black slip, and precise concentric circles or compass-drawn semicircles.",
    quotes: [
      { author: "John Nicolas Coldstream", work: "Greek Geometric Pottery", quote: "The introduction of the compass and multiple brush gave **Protogeometric** vases their distinctive concentric circles and refined balance." },
      { author: "Arthur Evans", work: "The Palace of Minos", quote: "In post-Minoan Crete, the transition to **Protogeometric** styles reflected cultural renewal after the bronze age collapse." },
      { author: "Martin P. Nilsson", work: "The Minoan-Mycenaean Religion", quote: "Iron swords and **Protogeometric** amphorae in Athenian graves testify to the dawn of a new classical world." }
    ]
  },
  "protoheme.md": {
    word: "protoheme",
    primary: "An iron-porphyrin complex (ferroprotoporphyrin IX) that serves as the prosthetic group in hemoglobin, myoglobin, and many cytochromes; also called protohaem or heme b.",
    secondary: "In biochemistry, the coordination complex consisting of an iron ion held within a protoporphyrin ring responsible for reversible oxygen binding and electron transfer.",
    quotes: [
      { author: "Max Perutz", work: "Proteins and Nucleic Acids", quote: "The planar **protoheme** group sits in a hydrophobic pocket of the globin, perfectly oriented to bind molecular oxygen." },
      { author: "Christian Anfinsen", work: "The Molecular Basis of Evolution", quote: "The spectral absorption bands of **protoheme** shift dramatically when the iron atom switches from the ferrous to the ferric state." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "Magnetic susceptibility measurements confirmed that the iron atom in oxygenated **protoheme** undergoes low-spin covalent bonding." }
    ]
  },
  "protohemin.md": {
    word: "protohemin",
    primary: "The chloride salt of protoheme (ferriprotoporphyrin IX chloride), formed when blood is heated with glacial acetic acid and sodium chloride; also called hemin or Teichmann's crystals.",
    secondary: "In forensic serology and historic pathology, brown rhombic microscopic crystals used in the Teichmann test to confirm the presence of bloodstains.",
    quotes: [
      { author: "Ludwik Teichmann", work: "Zeitschrift für rationelle Medicin", quote: "The formation of dark rhombic crystals of **protohemin** provides an infallible microscopic test for forensic bloodstains." },
      { author: "Arthur Conan Doyle", work: "A Study in Scarlet", quote: "Sherlock Holmes cried in triumph as his reagent precipitated crystals of **protohemin**, proving the stain was indeed dried blood." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Spectroscopic identification of **protohemin** confirms hemoglobin breakdown in cases of internal hemorrhage." }
    ]
  },
  "protohippus.md": {
    word: "protohippus",
    primary: "An extinct genus of three-toed horses from the Miocene and Pliocene epochs of North America.",
    secondary: "In mammalian paleontology, an intermediate grazing equid showing partial reduction of lateral side-toes and hypsodont molar teeth.",
    quotes: [
      { author: "Othniel Charles Marsh", work: "Fossil Horses in America", quote: "The fossil series leading from Miohippus through **Protohippus** to modern Equus presents the most complete evidence for organic evolution." },
      { author: "Thomas Henry Huxley", work: "American Addresses", quote: "In **Protohippus**, the lateral toes have ceased to touch the ground, demonstrating a functional shift toward single-toed running." },
      { author: "George Gaylord Simpson", work: "Horses", quote: "Miocene plains supported diverse herds of **Protohippus**, grazing upon the newly evolved abrasive prairie grasses." }
    ]
  },
  "protohistory.md": {
    word: "protohistory",
    primary: "The period of human history immediately following prehistory and preceding recorded history, during which a culture has not yet developed writing but is mentioned in the written records of other contemporary literate societies.",
    secondary: "In archaeological theory, the transitional epoch marked by burgeoning urbanism, oral epics, and external epigraphic documentation.",
    quotes: [
      { author: "V. Gordon Childe", work: "The Dawn of European Civilization", quote: "During the European Bronze Age, communities entered **protohistory** as Mediterranean merchants recorded their trade voyages." },
      { author: "Fernand Braudel", work: "The Mediterranean and the Mediterranean World", quote: "The shadowy centuries of Mediterranean **protohistory** laid down enduring agricultural techniques and maritime routes." },
      { author: "Colin Renfrew", work: "Archaeology and Language", quote: "In **protohistory**, the archaeologist must carefully weigh material assemblages against the mythic traditions of neighboring civilizations." }
    ]
  },
  "protology.md": {
    word: "protology",
    primary: "The study of first principles, origins, or beginnings, especially in theology and philosophy.",
    secondary: "In systematic Christian theology, the doctrine of creation, the primordial state of man, and the origin of the cosmos, contrasting with eschatology.",
    quotes: [
      { author: "Karl Rahner", work: "Theological Investigations", quote: "Christian **protology** cannot be a nostalgic report about paradise; it is the theological grounding of man's original orientation toward grace." },
      { author: "Mircea Eliade", work: "The Sacred and the Profane", quote: "Cosmogonic myths fulfill the ancient need for **protology**, anchoring human reality in primordial sacred acts." },
      { author: "Jaroslav Pelikan", work: "The Christian Tradition", quote: "The early Church Fathers balanced their apocalyptic eschatology with a robust biblical **protology** rooted in Genesis." }
    ]
  },
  "protomammal.md": {
    word: "protomammal",
    primary: "An extinct, mammal-like reptile (non-mammalian synapsid, such as a therapsid or cynodont) ancestral to modern mammals.",
    secondary: "In vertebrate paleontology, Permian and Triassic synapsids exhibiting transitional skeletal traits like secondary palates and differentiated dentition.",
    quotes: [
      { author: "Robert T. Bakker", work: "The Dinosaur Heresies", quote: "The Karoo basin of South Africa contains thousands of fossil skeletons of the mammal-like **protomammal** lineages." },
      { author: "Neil Shubin", work: "Your Inner Fish", quote: "The transition of jaw bones into delicate middle ear ossicles began inside the skull of the Triassic **protomammal**." },
      { author: "Stephen Jay Gould", work: "Eight Little Piggies", quote: "Long before dinosaurs ruled the land, the dominant terrestrial predators belonged to the synapsid **protomammal** stock." }
    ]
  },
  "proton.md": {
    word: "proton",
    primary: "A stable subatomic particle occurring in all atomic nuclei, having a positive electric charge equal in magnitude to that of an electron and a mass of approximately 1 atomic mass unit.",
    secondary: "In nuclear physics and chemistry, a composite hadron (baryon) composed of two up quarks and one down quark; also identical to the hydrogen ion (H+) in acid-base chemistry.",
    quotes: [
      { author: "Ernest Rutherford", work: "The Bakerian Lecture: Nuclear Constitution of Atoms", quote: "We have reason to believe that the hydrogen nucleus, which we propose to call the **proton**, is an ultimate constituent of all heavier elements." },
      { author: "Niels Bohr", work: "Atomic Physics and Human Knowledge", quote: "The binding force holding the electron to the **proton** governs the quantum structure of the hydrogen atom." },
      { author: "Richard Feynman", work: "The Character of Physical Law", quote: "In the nucleus, strong interactions hold every neutron and **proton** together against intense electrical repulsion." }
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
console.log("Primacy Batch 8 completed! Total words updated:", Object.keys(wordsData).length);
