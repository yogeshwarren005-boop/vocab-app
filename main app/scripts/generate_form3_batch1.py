import json, os

data = {
  "Dashboard — de\\de.md": {
    "primary": "A Greek root meaning 'to bind', 'tie', or 'fasten', forming the morphological foundation for terms designating anatomical bonds, connective tissues, and syntactic linkages.",
    "secondary": "In linguistics and biological nomenclature, denotes structural connection, covalent binding, or grammatical conjunction.",
    "quotes": [
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The Greek verbal stem **de** signifies binding or fastening, seen clearly in nominal derivatives like desmos."},
      {"author": "Robert Beekes", "work": "Etymological Dictionary of Greek", "quote": "Reflecting Proto-Indo-European *deh₁-, the root **de** gives rise to words denoting physical ligature and structural union."},
      {"author": "Herbert Weir Smyth", "work": "Greek Grammar", "quote": "Grammatical binding and coordination often rely on compound constructions rooted in **de**."}
    ]
  },
  "Dashboard — de\\desmid.md": {
    "primary": "Any single-celled microscopic freshwater green alga of the family Desmidiaceae, characteristically divided into two symmetrical halves joined by an isthmus.",
    "secondary": "In phycology and limnology, desmids serve as sensitive bioindicators of oligotrophic, acidic water quality.",
    "quotes": [
      {"author": "G. M. Smith", "work": "The Freshwater Algae of the United States", "quote": "Each **desmid** cell exhibits striking bilateral symmetry, typically constricted at the center into two semicells."},
      {"author": "F. E. Fritsch", "work": "The Structure and Reproduction of the Algae", "quote": "The distinctive cell division of a **desmid** involves the budding of two new semicells at the central junction."},
      {"author": "Robert Edward Lee", "work": "Phycology", "quote": "Ecological surveys frequently evaluate **desmid** diversity to detect subtle shifts in freshwater nutrient loading."}
    ]
  },
  "Dashboard — de\\desmitis.md": {
    "primary": "Inflammation of a ligament, occurring typically as a sports or occupational strain injury in human and equine veterinary medicine.",
    "secondary": "In orthopedics and veterinary biomechanics, chronic desmitis can lead to fibrocartilaginous metaplasia and ligamentous laxity.",
    "quotes": [
      {"author": "Wayne McIlwraith", "work": "Diagnostic and Surgical Arthroscopy in the Horse", "quote": "Suspensory **desmitis** represents one of the most debilitating soft tissue injuries in performance horses."},
      {"author": "J. A. Auer", "work": "Equine Surgery", "quote": "Ultrasound evaluation of ligamentous architecture remains crucial for monitoring recovery from acute **desmitis**."},
      {"author": "S. Dyson", "work": "Diagnosis and Management of Lameness in the Horse", "quote": "Conservative management of collateral **desmitis** requires strict rest followed by controlled mechanical loading."}
    ]
  },
  "Dashboard — de\\desmoid.md": {
    "primary": "Resembling a band, ribbon, or ligament in macroscopic texture; specifically designating a benign yet locally aggressive, non-metastasizing fibroblastic tumor.",
    "secondary": "In oncologic pathology, desmoid tumors (aggressive fibromatoses) arise from deep fascial and aponeurotic connective structures.",
    "quotes": [
      {"author": "Juan Rosai", "work": "Rosai and Ackerman's Surgical Pathology", "quote": "A **desmoid** tumor exhibits prominent, sweeping fascicles of mature fibroblasts within abundant collagenous stroma."},
      {"author": "Christopher D. M. Fletcher", "work": "Diagnostic Histopathology of Tumors", "quote": "Despite its benign histologic appearance, a **desmoid** fibromatosis often exhibits infiltrative margins that complicate surgical resection."},
      {"author": "Vinay Kumar", "work": "Robbins and Cotran Pathologic Basis of Disease", "quote": "Mutations in the beta-catenin or APC genes are characteristically associated with intra-abdominal **desmoid** lesions."}
    ]
  },
  "Dashboard — de\\desmoplasia.md": {
    "primary": "The growth and proliferation of dense fibrous or connective tissue, particularly in response to an invasive malignant epithelial neoplasm.",
    "secondary": "In tumor biology, desmoplasia results from paracrine signaling between neoplastic cells and cancer-associated fibroblasts.",
    "quotes": [
      {"author": "Robert A. Weinberg", "work": "The Biology of Cancer", "quote": "Carcinomas induce intense **desmoplasia**, recruiting stromal fibroblasts that synthesize massive collagenous scaffolds."},
      {"author": "Vinay Kumar", "work": "Robbins Basic Pathology", "quote": "The stony hardness of scirrhous breast carcinoma is directly caused by reactive **desmoplasia**."},
      {"author": "Harold F. Dvorak", "work": "Tumors: Wounds That Do Not Heal", "quote": "Malignant stroma generation shares profound biochemical parallels with chronic scar formation and **desmoplasia**."}
    ]
  },
  "Dashboard — de\\desmosome.md": {
    "primary": "A specialized cell junction consisting of dense protein plaques and cadherins that mechanically anchors intermediate filaments between adjacent animal cells.",
    "secondary": "In cell biology and dermatopathology, disruption of desmosomal cadherins (desmogleins) causes severe acantholytic blistering diseases such as pemphigus vulgaris.",
    "quotes": [
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "A **desmosome** acts like a spot-weld between adjacent epithelial cells, anchoring keratin intermediate filaments to withstand mechanical stress."},
      {"author": "Harvey Lodish", "work": "Molecular Cell Biology", "quote": "Transmembrane desmogleins and desmocollins bridge the intercellular space within the core of each **desmosome**."},
      {"author": "Elaine Fuchs", "work": "Beauty Is Skin Deep: The Fascinating Biology of the Epidermis", "quote": "Epidermal integrity relies upon robust **desmosome** complexes that disperse shear forces throughout the epithelial sheet."}
    ]
  },
  "Dashboard — de\\diadem.md": {
    "primary": "An ornamental jeweled crown or headband worn as a symbol of sovereignty, royalty, or exalted dignity.",
    "secondary": "In numismatics and classical archaeology, the diadem was originally a white ribbon or fillet tied around the head of Hellenistic monarchs.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Diocletian assumed the **diadem**, exchanging the republican simplicity of the principate for oriental monarchy."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "High on a throne of royal state, which far outshone the wealth of Ormus and of Ind, the **diadem** sparkled on his brow."},
      {"author": "Alexander Pope", "work": "The Rape of the Lock", "quote": "The sparkling **diadem** adorned her regal brow, commanding the homage of assembled courtiers."}
    ]
  },
  "Dashboard — de\\exode.md": {
    "primary": "A farce, comic interlude, or light musical performance played at the conclusion of a formal tragedy or dramatic representation in classical Greece and Rome.",
    "secondary": "In classical theatrical history, the exodium or exode provided emotional relief following dramatic catharsis.",
    "quotes": [
      {"author": "A. E. Haigh", "work": "The Attic Theatre", "quote": "Following the tragic conclusion of the tetralogy, an afterpiece or **exode** restored festive cheer to the Athenian audience."},
      {"author": "Gilbert Murray", "work": "A History of Ancient Greek Literature", "quote": "The structural role of the **exode** evolved from ritual satyr plays into witty comic postludes."},
      {"author": "John Addington Symonds", "work": "Studies of the Greek Poets", "quote": "Laughter burst forth uninhibitedly during the **exode**, contrasting with the solemn pathos of the preceding tragedy."}
    ]
  },
  "Dashboard — de\\plasmodesma.md": {
    "primary": "A microscopic membrane-lined cytoplasmic channel passing through the cell wall of plant cells and allowing direct transport and communication between them.",
    "secondary": "In plant cell physiology, plasmodesmata regulate symplastic macromolecular transport, viral movement, and developmental patterning signals.",
    "quotes": [
      {"author": "Lincoln Taiz", "work": "Plant Physiology", "quote": "The plant symplast forms a continuous cytoplasmic continuum linked by thousands of individual **plasmodesma** channels."},
      {"author": "Peter H. Raven", "work": "Biology of Plants", "quote": "Molecules up to a certain size limit pass readily through a **plasmodesma**, governed by specialized internal desmotubules."},
      {"author": "Bruce Alberts", "work": "Essential Cell Biology", "quote": "Intercellular communication across rigid cellulose walls occurs almost exclusively via the narrow aperture of each **plasmodesma**."}
    ]
  },
  "Dashboard — de\\polysyndeton.md": {
    "primary": "A rhetorical device employing multiple coordinate conjunctions in close succession, typically for rhythmic cadence or cumulative emphasis.",
    "secondary": "In classical rhetoric and stylistics, polysyndeton slows the delivery tempo and endows each connected element with independent gravity.",
    "quotes": [
      {"author": "Quintilian", "work": "Institutio Oratoria", "quote": "Through calculated **polysyndeton**, the orator deliberately multiplies conjunctions to present a succession of overwhelming events."},
      {"author": "Richard A. Lanham", "work": "A Handlist of Rhetorical Terms", "quote": "The rhythm of **polysyndeton** creates an expansive, biblical cadence that elevates simple catalogues into ceremonial processions."},
      {"author": "George Campbell", "work": "The Philosophy of Rhetoric", "quote": "By repeating connective particles, **polysyndeton** obliges the mind to linger on each distinct member of the sentence."}
    ]
  },
  "Dashboard — de\\rede.md": {
    "primary": "Counsel, advice, or deliberation; also, to advise, interpret, or give wise direction.",
    "secondary": "In archaic and Germanic literature, rede denotes deep wisdom, discernment, or an authoritative warning.",
    "quotes": [
      {"author": "Geoffrey Chaucer", "work": "The Canterbury Tales", "quote": "Therfore I **rede** yow, taketh this to herte, and kepeth yow wel from flatterye."},
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Do not, as some ungracious pastors do, show me the steep and thorny way to heaven, whiles himself recks not his own **rede**."},
      {"author": "Walter Scott", "work": "The Lady of the Lake", "quote": "Short space had he to pause and **rede**, for clamor loud arose upon the wind."}
    ]
  },
  "Dashboard — de\\syndesis.md": {
    "primary": "The structural joining or binding together of parts, especially the surgical or physiological union of anatomical elements.",
    "secondary": "In linguistics and syntax, syndesis designates the linking of clauses or phrases by explicit coordinate or subordinate conjunctions.",
    "quotes": [
      {"author": "Otto Jespersen", "work": "The Philosophy of Grammar", "quote": "Syntactic coordination relies either on explicit **syndesis** with connectives or asyndetic juxtaposition without them."},
      {"author": "Antoine Meillet", "work": "Introduction à l'étude comparative des langues indo-européennes", "quote": "Grammatical **syndesis** evolved gradually as autonomous sentences were bound into complex subordinate periods."},
      {"author": "David Crystal", "work": "A Dictionary of Linguistics and Phonetics", "quote": "Sentences joined by conjunctive **syndesis** display explicit grammatical integration."}
    ]
  },
  "Dashboard — de\\syndesmosis.md": {
    "primary": "An articulation or joint in which the opposed bony surfaces are bound together by an interosseous ligament or membrane allowing slight movement.",
    "secondary": "In orthopedic traumatology, disruption of the distal tibiofibular syndesmosis (high ankle sprain) requires anatomical reduction to prevent post-traumatic arthrosis.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "A **syndesmosis** represents a fibrous articulation where bones are united by dense interosseous fibrous bands."},
      {"author": "Charles A. Rockwood", "work": "Fractures in Adults", "quote": "Widening of the clear space on radiographic views indicates complete disruption of the distal tibiofibular **syndesmosis**."},
      {"author": "S. Terry Canale", "work": "Campbell's Operative Orthopaedics", "quote": "Screw or suture-button fixation stabilizes the unstable **syndesmosis** until ligamentous healing is securely achieved."}
    ]
  },
  "Dashboard — de\\syndetic.md": {
    "primary": "Connected by one or more explicit coordinating or subordinating conjunctions; connective or binding in syntactic function.",
    "secondary": "In linguistic analysis and stylistic theory, syndetic structures contrast with asyndetic clauses to modulate discourse tempo and grammatical cohesion.",
    "quotes": [
      {"author": "Randolph Quirk", "work": "A Comprehensive Grammar of the English Language", "quote": "Coordination is described as **syndetic** when coordinators such as 'and' or 'but' are overtly present between conjoins."},
      {"author": "Michael Halliday", "work": "Cohesion in English", "quote": "The explicit presence of **syndetic** markers reinforces structural clarity across narrative transitions."},
      {"author": "Ferdinand de Saussure", "work": "Course in General Linguistics", "quote": "Linguistic units enter into associative relations as well as overt, **syndetic** linear syntagms."}
    ]
  },
  "Dashboard — de\\syndeton.md": {
    "primary": "A syntactic construction in which words, phrases, or clauses are joined together by explicit coordinating conjunctions.",
    "secondary": "In classical rhetoric, syndeton represents the standard, balanced grammatical construction from which polysyndeton and asyndeton deviate.",
    "quotes": [
      {"author": "G. H. Matthews", "work": "Syntax and Style in Classical Authors", "quote": "Normal prose discourse relies upon standard **syndeton** to establish clear, logical relations between successive thoughts."},
      {"author": "Richard A. Lanham", "work": "A Handlist of Rhetorical Terms", "quote": "Departures from straightforward **syndeton** allow authors to inject poetic haste or ceremonial grandeur into sentence architecture."},
      {"author": "Edward P. J. Corbett", "work": "Classical Rhetoric for the Modern Student", "quote": "The disciplined orator balances abrupt asyndeton against regular **syndeton** to sustain listener engagement."}
    ]
  },
  "Dashboard — delt\\delt.md": {
    "primary": "An informal or clinical abbreviation for the deltoid muscle of the shoulder.",
    "secondary": "In kinesiology and fitness conditioning, referring to the anterior, lateral, or posterior heads of the triangular shoulder musculature.",
    "quotes": [
      {"author": "Arnold Schwarzenegger", "work": "The New Encyclopedia of Modern Bodybuilding", "quote": "Isolating the rear **delt** requires precise dumbbell raises with elbows flared slightly forward."},
      {"author": "Mark Rippetoe", "work": "Starting Strength: Basic Barbell Training", "quote": "The overhead press thoroughly recruits the lateral **delt** alongside the triceps to lock the barbell overhead."},
      {"author": "Stuart McGill", "work": "Ultimate Back Fitness and Performance", "quote": "Shoulder stability during heavy lifting depends on balanced activation of rotator cuff tendons and the prime-moving **delt**."}
    ]
  },
  "Dashboard — delt\\deltahedron.md": {
    "primary": "A polyhedron whose faces are all congruent equilateral triangles.",
    "secondary": "In geometry and structural chemistry, there exist exactly eight convex deltahedra, including the regular tetrahedron, octahedron, and icosahedron.",
    "quotes": [
      {"author": "H. S. M. Coxeter", "work": "Regular Polytopes", "quote": "Any convex **deltahedron** must possess triangular faces meeting at vertices with valence between three and five."},
      {"author": "Branko Grünbaum", "work": "Convex Polytopes", "quote": "The classification of every convex **deltahedron** forms a fundamental chapter in the metric study of triangulated surfaces."},
      {"author": "Norman Johnson", "work": "Convex Polyhedra with Regular Faces", "quote": "Beyond the Platonic solids, five non-regular deltahedra complete the set of strictly convex **deltahedron** forms."}
    ]
  },
  "Dashboard — delt\\deltasone.md": {
    "primary": "A pharmaceutical brand name for prednisone, a synthetic corticosteroid used to suppress inflammation and treat allergic and autoimmune conditions.",
    "secondary": "In clinical pharmacology, prednisone acts as a prodrug converted in the liver to prednisolone, exerting systemic glucocorticoid effects.",
    "quotes": [
      {"author": "Laurence L. Brunton", "work": "Goodman & Gilman's The Pharmacological Basis of Therapeutics", "quote": "Oral administration of **deltasone** rapidly suppresses circulating inflammatory cytokines in acute autoimmune exacerbations."},
      {"author": "Anthony S. Fauci", "work": "Harrison's Principles of Internal Medicine", "quote": "High-dose **deltasone** induction therapy remains pivotal for stabilizing acute systemic vasculitis."},
      {"author": "Bertram G. Katzung", "work": "Basic & Clinical Pharmacology", "quote": "Tapering the dosage of **deltasone** is critical to avoid acute secondary adrenal insufficiency."}
    ]
  },
  "Dashboard — delt\\deltoid.md": {
    "primary": "Shaped like the Greek capital letter delta (an equilateral triangle); specifically, the large triangular muscle covering the glenohumeral shoulder joint.",
    "secondary": "In functional anatomy, the deltoid muscle abducts, flexes, and extends the arm, divided into clavicular, acromial, and spinal divisions.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The **deltoid** muscle forms the rounded contour of the shoulder and serves as the principal abductor of the upper limb."},
      {"author": "Arthur C. Guyton", "work": "Textbook of Medical Physiology", "quote": "Contraction of the middle **deltoid** fibers raises the humerus through the horizontal plane once initiation is accomplished by supraspinatus."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The human **deltoid** exhibits distinctive development in correlation with erect posture and liberated manual dexterity."}
    ]
  },
  "Dashboard — deuter\\Deuteromycota.md": {
    "primary": "A former taxonomic division of fungi, also known as the Fungi Imperfecti, comprising species with no known sexual reproductive stage.",
    "secondary": "In systematic mycology, molecular phylogenetics has reassigned most members of Deuteromycota into the Ascomycota and Basidiomycota.",
    "quotes": [
      {"author": "C. J. Alexopoulos", "work": "Introductory Mycology", "quote": "The artificial phylum **Deuteromycota** served historically as a taxonomic repository for asexual stages of higher fungi."},
      {"author": "David L. Hawksworth", "work": "Ainsworth & Bisby's Dictionary of the Fungi", "quote": "Phylogenetic DNA sequencing has rendered the formal taxon **Deuteromycota** obsolete in favor of natural holomorph systematics."},
      {"author": "Bryce Kendrick", "work": "The Fifth Kingdom", "quote": "Molds assigned to **Deuteromycota** produce billions of conidia responsible for agricultural rusts and commercial fermentations."}
    ]
  },
  "Dashboard — deuter\\Deuteronomy.md": {
    "primary": "The fifth book of the Hebrew Bible and Old Testament, containing Moses' final discourses and a restatement of the Mosaic law.",
    "secondary": "In biblical hermeneutics and Near Eastern history, Deuteronomy adopts the treaty structure of second-millennium BCE covenant agreements.",
    "quotes": [
      {"author": "William Foxwell Albright", "work": "From the Stone Age to Christianity", "quote": "The legal code preserved in **Deuteronomy** reflects the solemn renewal of the covenant on the plains of Moab."},
      {"author": "Martin Noth", "work": "The Deuteronomistic History", "quote": "The theology of **Deuteronomy** provides the normative framework for interpreting Israel's subsequent monarchic narrative."},
      {"author": "Gerhard von Rad", "work": "Old Testament Theology", "quote": "In **Deuteronomy**, the proclamation of divine grace precedes and undergirds the ethical imperatives of the law."}
    ]
  },
  "Dashboard — deuter\\deuter.md": {
    "primary": "A Greek combining element meaning 'second', 'secondary', or 'next in order'.",
    "secondary": "In scientific terminology, deuter- designates second-tier forms, secondary characters, or isotopic modifications containing deuterium.",
    "quotes": [
      {"author": "Robert Beekes", "work": "Etymological Dictionary of Greek", "quote": "Deriving from Proto-Indo-European *du-tero- ('the second of two'), the prefix **deuter** marks secondary status in Greek compounds."},
      {"author": "Carl Darling Buck", "work": "A Dictionary of Selected Synonyms in the Principal Indo-European Languages", "quote": "Cognates of **deuter** throughout the Indo-European family systematically signify that which follows primary rank."},
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The combining element **deuter** establishes second-order relationships across theatrical, chemical, and anatomical vocabularies."}
    ]
  },
  "Dashboard — deuter\\deuteragonist.md": {
    "primary": "The actor or character second in importance to the protagonist in classical Greek drama or modern dramatic literature.",
    "secondary": "In dramatic theory, Aeschylus introduced the deuteragonist to enable dialogue and conflict beyond the protagonist-chorus dynamic.",
    "quotes": [
      {"author": "Aristotle", "work": "Poetics", "quote": "Aeschylus first raised the number of actors from one to two, introducing the **deuteragonist** and diminishing the importance of the chorus."},
      {"author": "A. E. Haigh", "work": "The Tragic Drama of the Greeks", "quote": "The introduction of the **deuteragonist** transformed dramatic performance from lyrical recitation into dynamic conflict."},
      {"author": "Bernard Knox", "work": "The Heroic Temper: Studies in Sophoclean Tragedy", "quote": "In Sophocles, the **deuteragonist** often serves as an uncomprehending foil against the heroic isolation of the protagonist."}
    ]
  },
  "Dashboard — deuter\\deuteranomaly.md": {
    "primary": "A mild, hereditary form of color vision deficiency characterized by an abnormal sensitivity of green-sensitive cone photopigments.",
    "secondary": "In visual physiology and ophthalmology, deuteranomaly represents the most common congenital color blindness, affecting roughly 5% of males via X-linked recessive inheritance.",
    "quotes": [
      {"author": "David H. Hubel", "work": "Eye, Brain, and Vision", "quote": "An individual with **deuteranomaly** possesses all three cone types, but the spectral peak of the M-cone is shifted toward the red end."},
      {"author": "John H. Mollon", "work": "The Origins of Modern Color Science", "quote": "Unlike true dichromacy, **deuteranomaly** permits trichromatic color matching, albeit with anomalous green proportions."},
      {"author": "Arthur C. Guyton", "work": "Textbook of Medical Physiology", "quote": "Spectral anomalies like **deuteranomaly** stem from unequal crossing over between adjacent red and green pigment genes on the X chromosome."}
    ]
  },
  "Dashboard — deuter\\deuteranopia.md": {
    "primary": "A form of congenital color blindness characterized by the complete absence of functioning green-sensitive retinal cone photopigments.",
    "secondary": "In optometry and genetics, deuteranopia reduces color discrimination to a two-dimensional chromatic space, confusing green, red, and yellow wavelengths.",
    "quotes": [
      {"author": "Hermann von Helmholtz", "work": "Treatise on Physiological Optics", "quote": "In cases of **deuteranopia**, the entire green sensation is eliminated, collapsing the visible spectrum into warm and cool hues."},
      {"author": "Ewald Hering", "work": "Outlines of a Theory of the Light Sense", "quote": "The opponent-process theory explains why **deuteranopia** impairs red-green distinctions without altering blue-yellow perception."},
      {"author": "Stephen Polyak", "work": "The Retina", "quote": "Histological and molecular studies confirm that **deuteranopia** results from the complete deletion of the medium-wavelength opsin locus."}
    ]
  },
  "Dashboard — deuter\\deuteranopic.md": {
    "primary": "Pertaining to, affected with, or characteristic of deuteranopia (congenital green-blindness).",
    "secondary": "In psychophysics and visual displays, deuteranopic simulation algorithms assist in designing universally accessible graphic interfaces.",
    "quotes": [
      {"author": "W. D. Wright", "work": "Researches on Normal and Defective Colour Vision", "quote": "The neutral point of a **deuteranopic** observer occurs near 498 nanometers, where green wavelengths appear completely achromatic."},
      {"author": "Edwin H. Land", "work": "The Retinex Theory of Color Vision", "quote": "Experiments with **deuteranopic** subjects demonstrate remarkable lightness constancy despite diminished spectral bandwidth."},
      {"author": "Robert M. Boynton", "work": "Human Color Vision", "quote": "Interface designers must account for **deuteranopic** vision when choosing contrasting traffic signal cues."}
    ]
  },
  "Dashboard — deuter\\deuteride.md": {
    "primary": "A chemical compound in which deuterium (heavy hydrogen) is bonded to another chemical element or group.",
    "secondary": "In organometallic and nuclear chemistry, deuterides serve as isotopic tracers and moderate fast neutrons in experimental reactors.",
    "quotes": [
      {"author": "Glenn T. Seaborg", "work": "The Chemistry of the Actinide Elements", "quote": "Uranium **deuteride** forms as a pyrophoric black powder upon exposure of finely divided metal to deuterium gas."},
      {"author": "F. A. Cotton", "work": "Advanced Inorganic Chemistry", "quote": "Lithium **deuteride** plays an essential role as a solid thermonuclear fuel in secondary fusion stages."},
      {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "The vibrational frequencies of a metal **deuteride** shift predictably in accordance with the increased reduced mass of the deuteron."}
    ]
  },
  "Dashboard — deuter\\deuterium.md": {
    "primary": "A stable isotope of hydrogen with a mass number of 2, having one proton and one neutron in its atomic nucleus; heavy hydrogen ($^2H$).",
    "secondary": "In physical chemistry and nuclear physics, deuterium is used in NMR spectroscopy solvent systems and serves as a coolant/moderator in heavy-water reactors.",
    "quotes": [
      {"author": "Harold C. Urey", "work": "The Discovery of Heavy Hydrogen", "quote": "Fractional distillation of liquid hydrogen allowed us to concentrate and spectrographically detect the presence of **deuterium**."},
      {"author": "Niels Bohr", "work": "Nuclear Constitution and the Periodic System", "quote": "The nucleus of **deuterium**, consisting of one proton and one neutron, represents the simplest composite nuclear system."},
      {"author": "Richard Feynman", "work": "The Feynman Lectures on Physics", "quote": "In thermonuclear reactions inside stars and fusion devices, **deuterium** nuclei fuse to generate helium and release enormous energy."}
    ]
  },
  "Dashboard — deuter\\deuteromycetes.md": {
    "primary": "Plural noun designating fungi formerly classed in the artificial group Deuteromycota (imperfect fungi) lacking an observable sexual cycle.",
    "secondary": "In medical and industrial microbiology, deuteromycetes include economically critical genera such as Penicillium and Aspergillus.",
    "quotes": [
      {"author": "Alexander Fleming", "work": "On the Antibacterial Action of Cultures of a Penicillium", "quote": "The mold belonged to the **deuteromycetes**, producing an exudate that exhibited potent bactericidal properties."},
      {"author": "C. J. Alexopoulos", "work": "Introductory Mycology", "quote": "Because sexual states were unknown, **deuteromycetes** were classified strictly by conidial shape, septation, and color."},
      {"author": "Selman Waksman", "work": "Microbial Antagonisms and Antibiotic Substances", "quote": "Soil surveys revealed that **deuteromycetes** synthesize diverse secondary metabolites capable of inhibiting rival microorganisms."}
    ]
  },
  "Dashboard — deuter\\deuteromycotina.md": {
    "primary": "A taxonomic subdivision equivalent to Deuteromycota, encompassing the asexual and conidial fungi.",
    "secondary": "In botanical Latin and mycological taxonomy, Deuteromycotina formalized the rank of Fungi Imperfecti prior to phylogenetic revisions.",
    "quotes": [
      {"author": "David L. Hawksworth", "work": "Mycologist's Handbook", "quote": "Species catalogued under **Deuteromycotina** were assigned form-genera based solely on anamorph morphology."},
      {"author": "G. C. Ainsworth", "work": "Introduction to the History of Mycology", "quote": "The subdivision **Deuteromycotina** reflected practical clinical utility rather than natural evolutionary genealogy."},
      {"author": "John Webster", "work": "Introduction to Fungi", "quote": "With the discovery of teleomorph stages, many taxa of **Deuteromycotina** were integrated into Ascomycotina."}
    ]
  },
  "Dashboard — deuter\\deuteron.md": {
    "primary": "The nucleus of a deuterium atom, consisting of one proton and one neutron bound together by the strong nuclear force.",
    "secondary": "In nuclear physics and particle astrophysics, the deuteron has a binding energy of 2.224 MeV, playing a pivotal role in Big Bang nucleosynthesis.",
    "quotes": [
      {"author": "Hans Bethe", "work": "Elementary Nuclear Theory", "quote": "Because it has no bound excited states, the **deuteron** serves as the primary testing ground for the two-nucleon interaction."},
      {"author": "Enrico Fermi", "work": "Nuclear Physics", "quote": "Photodisintegration of the **deuteron** by gamma rays provides a direct measurement of nuclear binding energy."},
      {"author": "Steven Weinberg", "work": "The First Three Minutes", "quote": "Until the temperature dropped below one billion degrees, any synthesized **deuteron** was instantly broken apart by high-energy photons."}
    ]
  },
  "Dashboard — dia\\deacon.md": {
    "primary": "An ordained minister ranking immediately below a priest or pastor, charged with administrative, liturgical, and charitable duties.",
    "secondary": "In Christian ecclesiastical history, the diaconate originated in the early Jerusalem church to oversee the distribution of alms to widows and the poor.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The primitive bishop was assisted by a council of presbyters and the active ministrations of each parish **deacon**."},
      {"author": "John Henry Newman", "work": "Apologia Pro Vita Sua", "quote": "He was ordained as a **deacon** in the cathedral, dedicating his faculties to the service of the altar and the afflicted."},
      {"author": "Thomas Aquinas", "work": "Summa Theologiae", "quote": "The office of **deacon** corresponds to ministerial assistance, serving the priest during the celebration of holy mysteries."}
    ]
  },
  "Dashboard — dia\\dia.md": {
    "primary": "A Greek preposition and prefix meaning 'through', 'across', 'between', or 'thoroughly'.",
    "secondary": "In lexical morphology, dia- forms terms denoting transmission (diathermy), separation (dialysis), or penetrative examination (diagnosis).",
    "quotes": [
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "The preposition **dia** with the genitive signifies movement through space or time, and with the accusative denotes cause or agency."},
      {"author": "Robert Beekes", "work": "Etymological Dictionary of Greek", "quote": "Connected with the numeral two (*dwo-), **dia** primarily meant 'in two' or 'apart', evolving into 'through' and 'across'."},
      {"author": "Herbert Weir Smyth", "work": "Greek Grammar", "quote": "In verbal compounds, **dia** imparts notions of severance, thorough completion, or reciprocal action."}
    ]
  },
  "Dashboard — dida\\Didache.md": {
    "primary": "A brief early Christian treatise (c. late 1st or early 2nd century) summarizing apostolic teaching on moral conduct, liturgical rites, and church order.",
    "secondary": "In patristic studies and early church history, the full title is 'The Teaching of the Twelve Apostles', discovered in manuscript form by Philotheos Bryennios in 1873.",
    "quotes": [
      {"author": "J. B. Lightfoot", "work": "The Apostolic Fathers", "quote": "The recovery of the **Didache** unveiled the transitional liturgical practices of Christian communities outside the imperial mainstream."},
      {"author": "Henry Chadwick", "work": "The Early Church", "quote": "The two-ways doctrine set forth in the opening chapters of the **Didache** divides human conduct between life and death."},
      {"author": "Adolf von Harnack", "work": "The Expansion of Christianity in the First Three Centuries", "quote": "The archaic simplicity of baptism and eucharist in the **Didache** testifies to its very early provenance."}
    ]
  },
  "Dashboard — dida\\apodidae.md": {
    "primary": "A family of highly aerial, insectivorous birds (commonly known as swifts) characterized by extremely short legs and long sickle-shaped wings.",
    "secondary": "In ornithology, species of Apodidae spend the vast majority of their lives in flight, roosting clinging vertically to cliff faces or hollow chimneys.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "Nests constructed from hardened saliva by members of **apodidae** are gathered in sea caves for trade throughout the East."},
      {"author": "Elliott Coues", "work": "Key to North American Birds", "quote": "The rudimentary feet of **apodidae** are adapted exclusively for clinging rather than perching or walking on horizontal ground."},
      {"author": "Ernst Mayr", "work": "Animal Species and Evolution", "quote": "Rapid adaptive radiation within the family **apodidae** produced unmatched aerodynamic efficiency among non-passerine birds."}
    ]
  },
  "Dashboard — dida\\autodidact.md": {
    "primary": "A self-taught person who has acquired knowledge or mastery in a subject through independent reading and practice without formal schooling.",
    "secondary": "In educational philosophy and intellectual history, autodidacts often exhibit distinctive, idiosyncratic syntheses across disparate disciplines.",
    "quotes": [
      {"author": "Jean-Paul Sartre", "work": "Nausea", "quote": "The **autodidact** had spent seven years reading every volume in the municipal library in strict alphabetical order."},
      {"author": "Virginia Woolf", "work": "The Common Reader", "quote": "He possessed the voracious, unguided curiosity of the true **autodidact**, untamed by academic convention."},
      {"author": "George Steiner", "work": "Lessons of the Masters", "quote": "Every profound reader remains at heart an **autodidact**, discovering personal truths outside institutional syllabi."}
    ]
  },
  "Dashboard — dida\\autodidactic.md": {
    "primary": "Pertaining to, acquired through, or characteristic of self-education; self-taught.",
    "secondary": "In pedagogy and biography, designating intellectual development undertaken independently of formal teachers or institutional curricula.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "Uncle Tungsten: Memories of a Chemical Boyhood", "quote": "His **autodidactic** zeal led him to assemble a private basement laboratory stocked with rare mineral ores."},
      {"author": "Harold Bloom", "work": "The Western Canon", "quote": "Shakespeare's literary mastery was essentially **autodidactic**, absorbing every scrap of available vernacular literature."},
      {"author": "Lewis Mumford", "work": "The City in History", "quote": "Renaissance craftsmen cultivated an **autodidactic** ethos that merged manual mechanical skill with humanistic inquiry."}
    ]
  },
  "Dashboard — dida\\dida.md": {
    "primary": "A Greek root meaning 'to teach', 'instruct', or 'explain', forming the base for terms relating to education, pedagogical instruction, and doctrine.",
    "secondary": "In historical linguistics and etymology, dida- stems from the reduplicated PIE root *dek- ('to take, accept, learn').",
    "quotes": [
      {"author": "Robert Beekes", "work": "Etymological Dictionary of Greek", "quote": "The verb didaskein originates from the reduplicated causative formation of the root **dida**, signifying to cause someone to learn."},
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "From **dida** emerge the rich lexical families of didactic poetry, pedagogical drama, and doctrinal treatise."},
      {"author": "Pierre Chantraine", "work": "Dictionnaire étymologique de la langue grecque", "quote": "The semantic progression from receiving knowledge to active imparting is preserved in Greek words formed on **dida**."}
    ]
  },
  "Dashboard — dida\\didact.md": {
    "primary": "A person inclined to lecture, instruct, or preach moralistically, often in an excessively pedantic or authoritarian manner.",
    "secondary": "In literary criticism, an author who prioritizes instructional utility and ethical doctrine over aesthetic experience.",
    "quotes": [
      {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "The dogmatic **didact** mistakes narrow intellectual conformity for broad sweetness and light."},
      {"author": "George Bernard Shaw", "work": "Plays Pleasant and Unpleasant", "quote": "I am a natural **didact**, using the stage not merely to entertain but to overturn social preconceptions."},
      {"author": "W. H. Auden", "work": "The Dyer's Hand", "quote": "When the poet turns **didact**, his verses forfeit their musical ambiguity and become rhymed lectures."}
    ]
  },
  "Dashboard — dida\\didactic.md": {
    "primary": "Intended to teach, instruct, or convey information; especially featuring an inclination to lecture or impart moral lessons.",
    "secondary": "In literary genre classification, didactic poetry and drama explicitly prioritize educational exposition over pure lyrical expression.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "A poem may be deeply **didactic** in its ultimate effect, yet its immediate object must remain pleasure rather than doctrine."},
      {"author": "Percy Bysshe Shelley", "work": "A Defence of Poetry", "quote": "True poetry acts upon the imagination, and is therefore hindered when constrained by narrow, **didactic** moralizing."},
      {"author": "John Locke", "work": "Some Thoughts Concerning Education", "quote": "The tutor must adopt a conversational manner rather than dry, **didactic** dogmatism to awaken a child's natural curiosity."}
    ]
  },
  "Dashboard — dida\\didactical.md": {
    "primary": "Pertaining to instruction; educational, pedagogical, or instructional in design or character.",
    "secondary": "In academic and stylistic discourse, having an explanatory, textbook-like exposition intended to impart systematic knowledge.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Knowledge delivered in a **didactical** manner tends to be received uncritically rather than questioned and enlarged."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "His essays maintain a grave, **didactical** tone that directs the reader toward virtuous introspection."},
      {"author": "William Hazlitt", "work": "Table-Talk", "quote": "A purely **didactical** work seldom touches the heart, however much it may convince the understanding."}
    ]
  },
  "Dashboard — dida\\didactically.md": {
    "primary": "In a didactic manner; with the intention of instructing, teaching, or moralizing.",
    "secondary": "In literary critique, executed in an expository or pedagogical fashion that foregrounds an explicit lesson.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He spoke **didactically**, arranging his opinions like specimens in a collector's cabinet for her instruction."},
      {"author": "Henry James", "work": "The Art of Fiction", "quote": "To write **didactically** is to compromise that organic illusion of life which constitutes the novelist's supreme triumph."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The historian should narrate vividly rather than pause **didactically** at every turn to lecture his audience."}
    ]
  },
  "Dashboard — dida\\didacticism.md": {
    "primary": "The philosophy, practice, or quality of being didactic; emphasis on moral or educational instructional value in literature and art.",
    "secondary": "In aesthetics and art criticism, didacticism often implies an excessive subordinating of artistic beauty to ideological or moral indoctrination.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "The Poetic Principle", "quote": "The heresy of **didacticism** assumes that the ultimate goal of poetry is truth and moral virtue, rather than beauty."},
      {"author": "Oscar Wilde", "work": "The Decay of Lying", "quote": "Art never expresses anything but itself, and the intrusion of **didacticism** heralds the death of pure aesthetic form."},
      {"author": "T. S. Eliot", "work": "The Sacred Wood", "quote": "Dante achieves great moral depth without vulgar **didacticism**, because his ethical vision is fully realized as poetic imagery."}
    ]
  },
  "Dashboard — dida\\didactics.md": {
    "primary": "The theory, methodology, and practical art of teaching; pedagogical science.",
    "secondary": "In educational theory, didactics encompasses instructional design, curricular structuring, and assessment strategies across learning environments.",
    "quotes": [
      {"author": "John Amos Comenius", "work": "The Great Didactic", "quote": "The ultimate aim of **didactics** is to discover a method of instruction whereby teachers teach less and learners learn more."},
      {"author": "Johann Friedrich Herbart", "work": "General Pedagogics", "quote": "Systematic **didactics** coordinates the presentation of material with the natural stages of psychological apperception."},
      {"author": "Jean Piaget", "work": "The Science of Education and the Psychology of the Child", "quote": "Modern **didactics** must adapt its curriculum to match the child's developmental cognitive structures."}
    ]
  },
  "Dashboard — dida\\didanosine.md": {
    "primary": "A synthetic dideoxynucleoside analog (ddI) that acts as a reverse transcriptase inhibitor, formerly used to treat HIV-1 infection.",
    "secondary": "In clinical pharmacology, didanosine halts viral DNA chain elongation upon phosphorylation into dideoxyadenosine triphosphate.",
    "quotes": [
      {"author": "Anthony S. Fauci", "work": "Harrison's Principles of Internal Medicine", "quote": "Early combination antiretroviral protocols utilized **didanosine** to suppress plasma HIV RNA levels when zidovudine monotherapy failed."},
      {"author": "Laurence L. Brunton", "work": "Goodman & Gilman's The Pharmacological Basis of Therapeutics", "quote": "The clinical utility of **didanosine** was restricted by serious adverse toxicities, notably peripheral neuropathy and pancreatitis."},
      {"author": "Bertram G. Katzung", "work": "Basic & Clinical Pharmacology", "quote": "As an adenosine nucleoside analogue, **didanosine** requires buffered formulations to prevent gastric acid degradation."}
    ]
  },
  "Dashboard — ec\\ec.md": {
    "primary": "A Greek preposition and prefix (variant of 'ex' used before consonants) meaning 'out of', 'away from', or 'external'.",
    "secondary": "In morphological linguistics, ec- forms words designating outward derivation, deviation, or removal (eccentric, ectomy).",
    "quotes": [
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "Before consonants, the preposition ex becomes **ec**, maintaining its fundamental sense of emergence or detachment."},
      {"author": "Herbert Weir Smyth", "work": "Greek Grammar", "quote": "Compounds formed with **ec** denote physical exit, deviation from a center, or intensive completion of action."},
      {"author": "Robert Beekes", "work": "Etymological Dictionary of Greek", "quote": "Reflecting PIE *eǵʰs ('out'), the morpheme **ec** is preserved in numerous Greek loanwords in European scientific registers."}
    ]
  },
  "Dashboard — ec\\eccentric.md": {
    "primary": "Deviating from conventional or accepted character, practice, or norms; unconventional, odd, or idiosyncratic.",
    "secondary": "In geometry and astronomy, not situated in the center or not describing a concentric circle; having orbital axes displaced from a central body.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "That so few now dare to be **eccentric** marks the chief danger of the time, for eccentricity has always abounded when strength of character has abounded."},
      {"author": "Johannes Kepler", "work": "Astronomia Nova", "quote": "The elliptical trajectory proved that Mars moves along an **eccentric** orbit rather than a perfect circle centered upon the sun."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Miss Havisham lived in an **eccentric** seclusion that defied all conventional habits of the neighboring gentry."}
    ]
  },
  "Dashboard — ec\\eccentrically.md": {
    "primary": "In an eccentric or unconventional manner; deviating from ordinary conduct or from a central geometry.",
    "secondary": "In mechanics and engineering, mounted, rotating, or driven away from the geometric center of an axle or shaft.",
    "quotes": [
      {"author": "Washington Irving", "work": "The Sketch Book of Geoffrey Crayon", "quote": "He dressed **eccentrically** in antique velvet coats and wandered about the manor absorbed in quiet reverie."},
      {"author": "Robert Louis Stevenson", "work": "The Strange Case of Dr. Jekyll and Mr. Hyde", "quote": "His habits had begun to vary **eccentrically**, puzzling the faithful servants who attended him."},
      {"author": "Rankine, W. J. M.", "work": "A Manual of Applied Mechanics", "quote": "A wheel mounted **eccentrically** upon a spindle generates periodic reciprocating motions in adjacent levers."}
    ]
  },
  "Dashboard — ec\\exec.md": {
    "primary": "An informal abbreviation for an executive officer or corporate managerial administrator.",
    "secondary": "In computer systems and operating system shells, a command or system call that replaces the current process image with a new program.",
    "quotes": [
      {"author": "W. Richard Stevens", "work": "Advanced Programming in the UNIX Environment", "quote": "When a process calls an **exec** function, that process is completely replaced by the new program."},
      {"author": "Peter Drucker", "work": "The Effective Executive", "quote": "The modern corporate **exec** must focus not on busyness, but on high-leverage contributions to institutional goals."},
      {"author": "Andrew S. Tanenbaum", "work": "Modern Operating Systems", "quote": "The fork-and-**exec** paradigm forms the foundational mechanism for spawning child tasks in Unix-like kernels."}
    ]
  },
  "Dashboard — ecto\\ecto.md": {
    "primary": "A combining form and prefix derived from Greek, meaning 'outer', 'external', or 'situated on the outside'.",
    "secondary": "In anatomy and embryology, ecto- identifies peripheral layers and external structures, such as ectoderm and ectoplasm.",
    "quotes": [
      {"author": "Henry George Liddell", "work": "A Greek-English Lexicon", "quote": "Derived from the adverb ektos ('outside'), the combining element **ecto** denotes external spatial relationships."},
      {"author": "Arthur C. Guyton", "work": "Textbook of Medical Physiology", "quote": "Structures designated with **ecto** routinely represent surfaces interacting directly with the external environment."},
      {"author": "Robert Beekes", "work": "Etymological Dictionary of Greek", "quote": "The productive prefix **ecto** contrasts systematically with ento- and endo- across biological taxonomies."}
    ]
  },
  "Dashboard — ecto\\ectoderm.md": {
    "primary": "The outermost of the three primary germ layers of an animal embryo, giving rise to the nervous system, epidermis, hair, nails, and sensory organs.",
    "secondary": "In embryology, neural crest cells derived from the ectoderm undergo epithelial-mesenchymal transition to populate diverse tissues.",
    "quotes": [
      {"author": "Scott F. Gilbert", "work": "Developmental Biology", "quote": "During gastrulation, the cells remaining on the exterior surface of the embryo constitute the **ectoderm**."},
      {"author": "Bruce Alberts", "work": "Molecular Biology of the Cell", "quote": "Neural tube induction transforms a specialized patch of dorsal **ectoderm** into the progenitor cells of the brain and spinal cord."},
      {"author": "Ernst Haeckel", "work": "The Evolution of Man", "quote": "Comparative embryology reveals that the skin and brain share a common developmental cradle within the primary **ectoderm**."}
    ]
  },
  "Dashboard — ecto\\ectodermal.md": {
    "primary": "Pertaining to, derived from, or situated in the ectoderm (outer embryonic germ layer).",
    "secondary": "In clinical genetics, ectodermal dysplasias comprise inherited disorders affecting teeth, sweat glands, hair, and nails.",
    "quotes": [
      {"author": "Lewis Wolpert", "work": "Principles of Development", "quote": "Signals from the underlying mesenchyme instruct adjacent **ectodermal** tissue to initiate feather and hair placode morphogenesis."},
      {"author": "Vinay Kumar", "work": "Robbins and Cotran Pathologic Basis of Disease", "quote": "Hypohidrotic **ectodermal** dysplasia presents with diminished sweating, sparse hair, and abnormal conical dentition."},
      {"author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "The entire cerebral cortex traces its historical cellular lineage to specialized **ectodermal** neuroblasts."}
    ]
  },
  "Dashboard — ecto\\ectodermic.md": {
    "primary": "Variant of ectodermal; of or relating to the ectoderm.",
    "secondary": "In comparative anatomy and embryological literature, designating structures originating from the outermost embryonic germ layer.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "The Oceanic Hydrozoa", "quote": "The outer body wall of the medusa consists of an **ectodermic** cellular layer overlying gelatinous mesoglea."},
      {"author": "F. M. Balfour", "work": "A Treatise on Comparative Embryology", "quote": "The lens of the vertebrate eye arises as an invagination of the overlying **ectodermic** epithelium."},
      {"author": "E. B. Wilson", "work": "The Cell in Development and Inheritance", "quote": "Cell division planes during early cleavage accurately segregate prospective **ectodermic** determinants."}
    ]
  },
  "Dashboard — ecto\\ectomorph.md": {
    "primary": "A human body somatotype characterized by a lean, slender build, long limbs, and little muscle or fat accumulation.",
    "secondary": "In constitutional psychology and anthropometry (Sheldon's typology), an ectomorph was hypothesized to exhibit cerebrotonic introversion.",
    "quotes": [
      {"author": "William H. Sheldon", "work": "The Varieties of Human Physique", "quote": "The extreme **ectomorph** presents a linear, fragile frame dominated by a high surface-area-to-mass ratio."},
      {"author": "J. M. Tanner", "work": "Foetus into Man", "quote": "Somatotype scoring classifies the classic **ectomorph** with minimal subcutaneous adipose tissue and slender skeletal levers."},
      {"author": "Robert M. Malina", "work": "Growth, Maturation, and Physical Activity", "quote": "Adolescent growth spurts often exaggerate **ectomorph** proportions before muscle mass catches up."}
    ]
  },
  "Dashboard — ecto\\ectomorphic.md": {
    "primary": "Having or characteristic of the physical build of an ectomorph; slender, linear, and lightly muscled.",
    "secondary": "In kinesiology, ectomorphic physiques often demonstrate superior endurance efficiency due to lower thermal and mass loads.",
    "quotes": [
      {"author": "William H. Sheldon", "work": "Atlas of Men", "quote": "An **ectomorphic** physique exhibits narrow shoulders, thin wrists, and long, tapering fingers."},
      {"author": "Hans Eysenck", "work": "The Structure of Human Personality", "quote": "Correlations between **ectomorphic** body types and reserved, intellectual habits have been extensively investigated in constitutional psychology."},
      {"author": "P. B. Medawar", "work": "The Uniqueness of the Individual", "quote": "Human variation produces continuous gradations between endomorphic mass and **ectomorphic** attenuation."}
    ]
  },
  "Dashboard — ecto\\ectomorphy.md": {
    "primary": "The state, degree, or predominance of ectomorphic characteristics (thinness, linearity, fragility) in human body composition.",
    "secondary": "In anthropometric somatotyping (Heath-Carter method), ectomorphy is quantified using height-to-weight cubic ratios.",
    "quotes": [
      {"author": "J. E. Lindsay Carter", "work": "Somatotyping: Development and Applications", "quote": "High ratings of **ectomorphy** correlate closely with marathon runners and high jumpers whose performance rewards low inertia."},
      {"author": "William H. Sheldon", "work": "The Varieties of Delinquent Youth", "quote": "The third component of physical constitution, **ectomorphy**, measures the relative dispersion of bodily mass."},
      {"author": "G. A. Harrison", "work": "Human Biology: An Introduction to Human Evolution and Growth", "quote": "Desert and tropical populations frequently display elevated **ectomorphy** as an adaptation for radiative heat dissipation."}
    ]
  },
  "Dashboard — ecto\\ectotherm.md": {
    "primary": "An animal whose body temperature is primarily determined by heat absorbed from its external environment; a cold-blooded animal.",
    "secondary": "In physiological ecology, ectotherms exhibit low resting metabolic rates and rely heavily upon behavioral thermoregulation.",
    "quotes": [
      {"author": "Knut Schmidt-Nielsen", "work": "Animal Physiology: Adaptation and Environment", "quote": "An **ectotherm** regulates its internal temperature largely through behavioral adjustments such as basking on sunlit rocks."},
      {"author": "R. McNeill Alexander", "work": "Principles of Animal Locomotion", "quote": "Because an **ectotherm** expends far less energy on basal heat generation, it can survive on a fraction of an endotherm's caloric intake."},
      {"author": "Peter W. Hochachka", "work": "Biochemical Adaptation", "quote": "Enzymes in an **ectotherm** must maintain catalytic efficiency across wide daily fluctuations in ambient temperature."}
    ]
  },
  "Dashboard — ecto\\ectothermic.md": {
    "primary": "Of, relating to, or being an ectotherm; dependent on external environmental heat sources.",
    "secondary": "In vertebrate paleontology and evolutionary biology, debating whether extinct archosaurs and theropods were ectothermic or endothermic.",
    "quotes": [
      {"author": "Stephen Jay Gould", "work": "The Panda's Thumb", "quote": "The debate over dinosaur physiology challenged the classical assumption that all giant reptiles were sluggishly **ectothermic**."},
      {"author": "Robert T. Bakker", "work": "The Dinosaur Heresies", "quote": "High predator-to-prey ratios in fossil communities argue against purely **ectothermic** metabolisms in predatory dinosaurs."},
      {"author": "David Attenborough", "work": "Life on Earth", "quote": "Lizards survive in arid deserts by mastering an **ectothermic** lifestyle that economizes both food and water."}
    ]
  },
  "Dashboard — eg\\eg.md": {
    "primary": "A root and grammatical abbreviation: in Greek etymology, a root element relating to outward expulsion or goats (*aix*); also the common Latin abbreviation e.g. (*exempli gratia*, 'for example').",
    "secondary": "In clinical medicine, root eg- forms egophony (bleating lung resonance); in formal writing, e.g. introduces illustrative specimens.",
    "quotes": [
      {"author": "H. W. Fowler", "work": "Modern English Usage", "quote": "The abbreviation **eg** introduces illustrative examples, whereas i.e. provides an exhaustive rephrasing."},
      {"author": "Robert Beekes", "work": "Etymological Dictionary of Greek", "quote": "The Greek stem **eg** appears in medical diagnostic acoustics to describe sound quality mimicking a goat's voice."},
      {"author": "William Strunk Jr.", "work": "The Elements of Style", "quote": "Punctuate **eg** with periods and follow it with a comma when presenting selected instances in text."}
    ]
  },
  "Dashboard — eg\\egophony.md": {
    "primary": "An abnormal voice sound with a high-pitched, nasal, or bleating quality heard during lung auscultation when vocal resonance is transmitted through consolidated tissue.",
    "secondary": "In clinical pulmonology, egophony is elicited by having the patient say 'E', which sounds like a compressed nasal 'A' over pleural effusion or lobar pneumonia.",
    "quotes": [
      {"author": "René Laennec", "work": "A Treatise on the Diseases of the Chest", "quote": "I observed a peculiar voice timbre, which I named **egophony**, resembling the shrill, tremulous bleating of a goat."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Along the upper margin of a pleural effusion, auscultation frequently demonstrates marked **egophony**."},
      {"author": "Steven McGee", "work": "Evidence-Based Physical Diagnosis", "quote": "The presence of **egophony** significantly increases the post-test probability of pneumonia in patients presenting with cough and fever."}
    ]
  },
  "Dashboard — elem\\almoner.md": {
    "primary": "An official charged with distributing charitable donations, alms, and relief funds to the poor and needy.",
    "secondary": "In historical hospitals and monastic foundations, the almoner served as the institutional link to indigent patients and community paupers.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The grand lady acted as hereditary **almoner**, distributing blankets and shillings with serene condescension."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The King's Bedesman, or licensed blue-gown beggar, received his annual bounty from the royal **almoner**."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "In the twelfth century monastery, the **almoner** dispensed daily loaves to every wandering mendicant at the Abbey gate."}
    ]
  },
  "Dashboard — elem\\alms.md": {
    "primary": "Money, food, clothing, or other material goods donated freely to relieve the suffering of the impoverished.",
    "secondary": "In religious ethics and sociological history, giving alms was codified as a foundational moral duty across Abrahamic and Asian traditions.",
    "quotes": [
      {"author": "John Milton", "work": "Samson Agonistes", "quote": "To sit idle here, asking **alms** of passing pilgrims, were worse than the blindest bondage."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "Charity deferred till death is rather an angel's debt than a man's **alms**, for it giveth what it can no longer hold."},
      {"author": "Alexis de Tocqueville", "work": "Memoir on Pauperism", "quote": "Public **alms** legalizes the status of the pauper while often degrading the mutual dignity of the recipient and giver."}
    ]
  },
  "Dashboard — elem\\eleemosynary.md": {
    "primary": "Relating to or supported by charity, alms, or donations; charitable or philanthropic in nature.",
    "secondary": "In legal jurisprudence, an eleemosynary corporation is an organization created for the perpetual distribution of the founder's charitable bounty.",
    "quotes": [
      {"author": "John Marshall", "work": "Dartmouth College v. Woodward", "quote": "The college was an **eleemosynary** institution, founded not for political purposes, but for the perpetual distribution of educational benevolence."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "Hospitals, endowed schools, and charitable trusts fall under the ancient legal category of **eleemosynary** corporations."},
      {"author": "Thomas De Quincey", "work": "Confessions of an English Opium-Eater", "quote": "He subsisted for weeks upon the cold, **eleemosynary** hospitality of impoverished acquaintances in London."}
    ]
  },
  "Dashboard — elem\\elem.md": {
    "primary": "A root and common abbreviation for 'element', 'elementary', or 'elemental', signifying a fundamental constituent or foundational level.",
    "secondary": "In typography, grammar, and scientific code, elem designates atomic units, structural tags, or primary components.",
    "quotes": [
      {"author": "Euclid", "work": "The Elements (Stoicheia)", "quote": "A primary component or **elem** cannot be resolved into simpler geometric forms without losing its essential identity."},
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "I mean by **elem** those primitive and simple bodies of which all mixed bodies are compounded."},
      {"author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "The definition of an ultimate **elem** must rest on our inability to decompose it by any existing analytical method."}
    ]
  },
  "Dashboard — elem\\element.md": {
    "primary": "A fundamental, essential, or irreducible constituent of a composite entity or system.",
    "secondary": "In chemistry, a pure chemical substance consisting of atoms all having the same number of protons in their atomic nuclei.",
    "quotes": [
      {"author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "Every substance that has resisted all attempts at chemical decomposition must be regarded as an **element**."},
      {"author": "Dmitri Mendeleev", "work": "The Principles of Chemistry", "quote": "The periodic law demonstrates that the properties of an **element** are periodic functions of its atomic mass."},
      {"author": "Aristotle", "work": "Metaphysics", "quote": "An **element** is that into which a thing is divided, being itself undivided in form into other kinds."}
    ]
  }
}

base_dir = r"App database\Greek roots\Cluster Form & Space"
mjs_path = r"main app\scripts\curate-form3-batch1.mjs"

content = f"""import {{ updateNotesBatch }} from './curate-updater-util.mjs';

const baseDir = {json.dumps(base_dir)};
const batchData = {json.dumps(data, indent=2, ensure_ascii=False)};

const count = updateNotesBatch(baseDir, batchData);
console.log(`Updated ${{count}} notes in Form Part 3 Batch 1.`);
"""

with open(mjs_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Generated {mjs_path} with {len(data)} words.")
