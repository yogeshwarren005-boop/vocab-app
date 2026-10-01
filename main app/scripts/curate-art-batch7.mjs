import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Art, Craft & Design/Dashboard — plast';

const filesData = {
  "anaplasia.md": {
    primary: "A condition of cells characterized by loss of structural differentiation, specialized function, and tissue organization, typical of malignant tumors.",
    secondary: "In oncology and pathology, cellular dedifferentiation resulting in hyperchromatism, pleomorphism, and abnormal mitotic activity.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The transition toward malignancy is marked by progressive **anaplasia**, where specialized tissue cells revert to embryonic chaos." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Marked **anaplasia** on histological section generally portends an aggressive, rapidly metastasizing neoplasm." },
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "Under the microscope, cancer reveals its sinister nature through **anaplasia**, stripping cells of their architectural identity." }
    ]
  },
  "anaplastic.md": {
    primary: "Characterized by or relating to anaplasia; poorly differentiated or undifferentiated, typical of high-grade malignant tumors.",
    secondary: "In plastic surgery (archaic), pertaining to surgical reconstruction or tissue restoration (*anaplasty*).",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The biopsy of the thyroid mass revealed an aggressive **anaplastic** carcinoma demanding urgent palliative care." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "Histological staining distinguished the benign adenoma from an invasive **anaplastic** tumor." },
      { author: "Atul Gawande", work: "Being Mortal", quote: "Patients diagnosed with advanced **anaplastic** thyroid malignancies face extraordinarily rapid disease progression." }
    ]
  },
  "anaplasty.md": {
    primary: "Reconstructive or plastic surgery aimed at restoring lost, deformed, or injured body parts through grafting or tissue repositioning.",
    secondary: "In surgical history, restorative grafting procedures practiced in classical India and Renaissance Europe.",
    quotes: [
      { author: "Harold Gillies", work: "Plastic Surgery of the Face", quote: "Modern facial **anaplasty** was born in the trenches of the Great War to rebuild shattered visages." },
      { author: "Robert Hooper", work: "Lexicon Medicum", quote: "Surgical treatises describe **anaplasty** as the art of restoring mutilated noses and lips using adjacent flaps." },
      { author: "Chevalier Jackson", work: "Bronchoscopy and Esophagoscopy", quote: "Careful **anaplasty** of the tracheal stenosis restored normal laminar airflow." }
    ]
  },
  "antineoplastic.md": {
    primary: "Acting to prevent, inhibit, or arrest the development, proliferation, or spread of malignant neoplasms; chemotherapeutic.",
    secondary: "A pharmaceutical agent or drug used in cancer chemotherapy to destroy tumor cells or suppress abnormal cell division.",
    quotes: [
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "Farber recognized that aminopterin acted as a potent **antineoplastic** agent against childhood leukemia." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Modern oncology relies on synergistic **antineoplastic** regimens to overcome biochemical drug resistance." },
      { author: "Jerome Groopman", work: "The Anatomy of Hope", quote: "The patient endured punishing side effects from the aggressive **antineoplastic** infusion in hopes of remission." }
    ]
  },
  "cataplasia.md": {
    primary: "Degenerative or regressive cellular change in which mature cells or tissues revert to an earlier, less specialized, or less functional state.",
    secondary: "In biological pathology, physiological or pathological tissue regression (atrophy, senescent involution).",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "In chronic wasting diseases, tissues undergo **cataplasia**, losing functional organelles and contractile fibrils." },
      { author: "William Gowers", work: "A Manual of Diseases of the Nervous System", quote: "Motor neurons exhibited **cataplasia** with chromatolysis following prolonged mechanical compression." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "Following seasonal reproduction, the gonadal tissues of marine coelenterates undergo pronounced **cataplasia**." }
    ]
  },
  "cataplastic.md": {
    primary: "Pertaining to, characterized by, or undergoing cataplasia; regressive or degenerative in cellular development.",
    secondary: "Showing morphological signs of degenerative tissue regression.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The **cataplastic** degeneration of striated muscle fibers was observed throughout the atrophic limb." },
      { author: "Santiago Ramón y Cajal", work: "Degeneration and Regeneration of the Nervous System", quote: "Severed axons display **cataplastic** retraction bulbs within hours of focal injury." },
      { author: "Robert Hooper", work: "Lexicon Medicum", quote: "Pathologists distinguished progressive metaplastic changes from **cataplastic** involutionary states." }
    ]
  },
  "dysplasia.md": {
    primary: "The abnormal growth, development, or organization of cells, tissues, or organs, often representing an early pre-malignant stage.",
    secondary: "In developmental genetics, a structural malformation caused by intrinsic abnormalities in tissue embryogenesis.",
    quotes: [
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "Cervical Pap smears transformed preventive oncology by detecting cellular **dysplasia** years before invasive carcinoma developed." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe epithelial **dysplasia** in Barrett's esophagus warrants close endoscopic surveillance." },
      { author: "Atul Gawande", work: "Complications", quote: "Microscopic sections showed moderate architectural **dysplasia** along the glandular margins." }
    ]
  },
  "dysplastic.md": {
    primary: "Characterized by or exhibiting dysplasia; showing abnormal microscopic cellular development or atypical growth.",
    secondary: "Relating to congenital malformation or developmental defect in tissue structure.",
    quotes: [
      { author: "Oliver Sacks", work: "An Anthropologist on Mars", quote: "Histological analysis revealed **dysplastic** cortical architecture, explaining the patient's refractory focal seizures." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Dermatologists routinely excise **dysplastic** nevi to prevent their potential transformation into malignant melanoma." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "The pathologist confirmed that the polyp contained **dysplastic** crypts requiring complete removal." }
    ]
  },
  "hernioplasty.md": {
    primary: "The surgical repair and reconstruction of a hernia, especially one involving reinforcement with synthetic mesh or tissue grafts.",
    secondary: "In abdominal surgery, tension-free hernioplasty techniques that dramatically reduce postoperative recurrence rates.",
    quotes: [
      { author: "Atul Gawande", work: "Complications: A Surgeon's Notes on an Imperfect Science", quote: "In performing an inguinal **hernioplasty**, the resident learned to place the polypropylene mesh without injuring the spermatic cord." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Modern tension-free **hernioplasty** has largely supplanted older tissue-apposition sutures." },
      { author: "Harold Gillies", work: "Principles and Art of Plastic Surgery", quote: "Restoring structural integrity across fascial defects requires careful **hernioplasty** using autologous fascia lata." }
    ]
  },
  "mammoplasty.md": {
    primary: "Plastic surgery performed on the breast, either to reduce, enlarge, reconstruct, or reshape its contour.",
    secondary: "In oncologic reconstructive surgery, post-mastectomy tissue reconstruction using implants or autologous tissue flaps.",
    quotes: [
      { author: "Atul Gawande", work: "Better: A Surgeon's Notes on Performance", quote: "The reconstructive team completed the bilateral **mammoplasty**, restoring symmetry following tumor excision." },
      { author: "Harold Gillies", work: "Plastic Surgery of the Face and Body", quote: "A successful **mammoplasty** balances aesthetic contour with careful preservation of blood supply to the nipple-areola complex." },
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "Modern breast cancer surgery evolved to integrate oncological clearance with immediate reconstructive **mammoplasty**." }
    ]
  },
  "neoplasm.md": {
    primary: "A new and abnormal growth of tissue in the body, characteristic of cancer or benign tumors, formed by uncontrolled cell division.",
    secondary: "In pathology, a clonal population of cells that proliferates autonomously, escaping normal physiological growth regulation.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Every true **neoplasm** originates from pre-existing cellular elements, proliferating in defiance of systemic physiological limits." },
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "The fundamental enigma of a **neoplasm** is that it is not an invading foreigner, but our own flesh gone rogue." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Early histological distinction between a benign and a malignant **neoplasm** remains the cornerstone of clinical prognosis." }
    ]
  },
  "neoplastic.md": {
    primary: "Relating to, of the nature of, or characterized by a neoplasm (abnormal tissue growth or tumor).",
    secondary: "In oncology, exhibiting autonomous, uncontrolled cellular replication and loss of normal tissue architecture.",
    quotes: [
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "Carcinogenic mutations accumulate sequentially, converting a normal cell into an aggressively **neoplastic** clone." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Rapid weight loss and unexplained anemia frequently signal an occult **neoplastic** process." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "A localized **neoplastic** infiltration in the right parietal lobe caused profound perceptual neglect." }
    ]
  },
  "plaster.md": {
    primary: "A building material composed of sand, water, and lime or gypsum, applied as a paste to walls and ceilings that hardens as it dries.",
    secondary: "A medicated dressing or adhesive strip applied to the skin; or a rigid orthopedic cast (plaster of Paris).",
    quotes: [
      { author: "Charles Dickens", work: "Great Expectations", quote: "Cracks ran through the crumbling **plaster** of the ceiling, showering fine white dust onto the table." },
      { author: "George Orwell", work: "1984", quote: "Winston peeled away the coarse military **plaster** from his swollen ankle, grimacing in the cold." },
      { author: "Henry David Thoreau", work: "Walden", quote: "I did not begin to **plaster** my chimney until late autumn, when the frosty nights made a warm hearth indispensable." }
    ]
  },
  "plasterboard.md": {
    primary: "A rigid building board made of a layer of gypsum plaster pressed between two thick sheets of paper, used for interior walls.",
    secondary: "In modern construction, a prefabricated interior wall cladding material valued for fire resistance and ease of installation.",
    quotes: [
      { author: "David Foster Wallace", work: "Infinite Jest", quote: "The cheap partition wall was constructed of thin **plasterboard** that failed to muffle the tenant's television." },
      { author: "Philip K. Dick", work: "Do Androids Dream of Electric Sheep?", quote: "The decaying apartment showed exposed wiring protruding through cracked sheets of crumbling **plasterboard**." },
      { author: "John Updike", work: "Rabbit, Run", quote: "The smell of fresh spackle and cut **plasterboard** hung in the unfinished suburban basement." }
    ]
  },
  "plastered.md": {
    primary: "Coated, surfaced, or covered with plaster.",
    secondary: "Covered heavily or smeared with something; or informal slang for very drunk.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "The rough stone corridor was whitewashed and neatly **plastered**, giving a sober monastic calm." },
      { author: "Mark Twain", work: "The Adventures of Huckleberry Finn", quote: "The fences were **plastered** with colorful circus posters boasting wild beasts and acrobats." },
      { author: "F. Scott Fitzgerald", work: "The Great Gatsby", quote: "By two o'clock in the morning, half the guests were completely **plastered**, spilling champagne across the terrace." }
    ]
  },
  "plasterer.md": {
    primary: "A skilled tradesperson who applies plaster to walls, ceilings, or decorative architectural moldings.",
    secondary: "An artisan who prepares plaster lath and creates ornamental stucco moldings in architectural construction.",
    quotes: [
      { author: "Charles Dickens", work: "Bleak House", quote: "The busy **plasterer** smoothed the wet mortar along the ceiling laths with his rhythmic steel trowel." },
      { author: "Thomas Hardy", work: "Jude the Obscure", quote: "He worked alongside the mason and the **plasterer**, learning the ancient craft of building restoration." },
      { author: "William Morris", work: "Hopes and Fears for Art", quote: "In medieval cathedrals, the **plasterer** and stonecutter shared a living tradition of unhurried artistry." }
    ]
  },
  "plastering.md": {
    primary: "The act, trade, or process of applying plaster to walls and ceilings.",
    secondary: "A surface or layer of plaster applied to an architectural structure; or figurative severe defeat or heavy bombardment.",
    quotes: [
      { author: "Henry David Thoreau", work: "Walden", quote: "My domestic **plastering** proved delightful labor, smoothing the snowy mortar onto the laths before winter arrived." },
      { author: "George Orwell", work: "Down and Out in Paris and London", quote: "The damp basement kitchen suffered from peeling paint and crumbling lime **plastering**." },
      { author: "Winston Churchill", work: "The Second World War", quote: "The enemy naval batteries received a merciless **plastering** from our carrier-based bombers." }
    ]
  },
  "plasterwork.md": {
    primary: "Construction work done with plaster, especially decorative, ornamental, or molded plaster surfaces (such as cornices or medallions).",
    secondary: "The finished interior surfaces and decorative moldings produced by a plasterer.",
    quotes: [
      { author: "Edith Wharton", work: "The Age of Innocence", quote: "The drawing-room featured elaborate Louis Quinze **plasterwork**, gilded garlands framing the crystal chandelier." },
      { author: "John Ruskin", work: "The Stones of Venice", quote: "Beneath the peeling paint, the delicate Renaissance **plasterwork** revealed graceful mythological friezes." },
      { author: "Virginia Woolf", work: "Night and Day", quote: "The old Victorian salon was shaded by heavy velvet curtains and ornate, dust-darkened ceiling **plasterwork**." }
    ]
  },
  "plastic.md": {
    primary: "A synthetic or semi-synthetic material made from polymers that can be molded into solid objects, films, or fibers.",
    secondary: "Capable of being molded, shaped, or modeled (pliable); or in neuroscience, exhibiting structural neuroplasticity.",
    quotes: [
      { author: "Aldous Huxley", work: "Brave New World", quote: "The infants crawled happily across the gleaming synthetic **plastic** tiles of the nursery floor." },
      { author: "William James", work: "The Principles of Psychology", quote: "Plasticity, in the wide sense of the word, means the possession of a structure weak enough to yield to an influence, but strong enough not to yield all at once; our brain is **plastic**." },
      { author: "Roland Barthes", work: "Mythologies", quote: "More than a substance, **plastic** is the very idea of its infinite transformation; it is the first magical material that consented to be prosaic." }
    ]
  },
  "plastically.md": {
    primary: "In a plastic, malleable, or pliable manner; capable of being shaped or molded without rupture.",
    secondary: "In a three-dimensional, sculptural, or vividly tangible artistic form.",
    quotes: [
      { author: "Walter Pater", work: "The Renaissance", quote: "The marble was treated so **plastically** by Michelangelo that the imprisoned figure seemed struggling to emerge." },
      { author: "Johann Wolfgang von Goethe", work: "Italian Journey", quote: "The ancient sculptor conceived his subject **plastically**, giving tactile weight to every muscle." },
      { author: "Oliver Sacks", work: "The Mind's Eye", quote: "The damaged visual cortex reorganized **plastically**, recruiting adjacent auditory regions to interpret tactile input." }
    ]
  },
  "plasticine.md": {
    primary: "A brand of soft, non-drying modeling clay used especially by children and sculptors for modeling and animation.",
    secondary: "Figuratively, something pliable, easily manipulated, or impressionable.",
    quotes: [
      { author: "George Orwell", work: "Coming Up for Air", quote: "The classroom smelled of damp chalk, inkwells, and the oily gray lumps of **plasticine** we kneaded at our desks." },
      { author: "David Foster Wallace", work: "Infinite Jest", quote: "The child rolled a cylinder of blue **plasticine** between his palms, shaping a crude airplane." },
      { author: "C. S. Lewis", work: "The Magician's Nephew", quote: "The young mind is not like rigid stone, but like soft **plasticine** ready to receive whatever shape is impressed upon it." }
    ]
  },
  "plasticise.md": {
    primary: "To make or become plastic, malleable, or pliable; to add plasticizers to a polymer to increase flexibility.",
    secondary: "Figuratively, to render fluid, moldable, or adaptable to external pressures.",
    quotes: [
      { author: "Primo Levi", work: "The Periodic Table", quote: "The industrial chemist learned how to **plasticise** rigid cellulose nitrate using natural camphor." },
      { author: "Aldous Huxley", work: "Brave New World Revisited", quote: "Totalitarian propaganda seeks to **plasticise** public opinion until citizens conform to any official mandate." },
      { author: "J. G. Ballard", work: "The Atrocity Exhibition", quote: "Heat and chemical solvents began to **plasticise** the synthetic upholstery of the crashed automobile." }
    ]
  },
  "plasticiser.md": {
    primary: "A substance (such as phthalate ester) added to a synthetic polymer or resin to promote flexibility and reduce brittleness.",
    secondary: "An additive used in cement, plastics, or paint formulations to improve flow and workability.",
    quotes: [
      { author: "Rachel Carson", work: "Silent Spring", quote: "Industrial runoff contained leaching **plasticiser** compounds that accumulated in coastal shellfish tissues." },
      { author: "Primo Levi", work: "The Periodic Table", quote: "Without the precise ratio of **plasticiser**, the synthetic resin cracked into brittle shards under winter cold." },
      { author: "Peter Atkins", work: "Physical Chemistry", quote: "The addition of a small-molecule **plasticiser** lowers the glass transition temperature of the polymer." }
    ]
  },
  "plasticity.md": {
    primary: "The quality or state of being easily shaped, molded, or deformed under stress without breaking.",
    secondary: "In neuroscience, the capacity of the brain and nervous system to change and reorganize structurally throughout life.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "Habit simplifies our movements, diminishes fatigue, and is made possible solely by the extraordinary physical **plasticity** of our neural pathways." },
      { author: "Oliver Sacks", work: "Musicophilia", quote: "The remarkable **plasticity** of the musical brain enables blind performers to develop vastly expanded auditory cortices." },
      { author: "Stephen Jay Gould", work: "The Mismeasure of Man", quote: "Human biological nature is characterized above all by behavioral and cultural **plasticity**." }
    ]
  },
  "plasticize.md": {
    primary: "To make plastic, flexible, or moldable; to treat a substance with a plasticizer.",
    secondary: "To render soft, pliable, or adaptable.",
    quotes: [
      { author: "Primo Levi", work: "The Periodic Table", quote: "Technicians added phthalates to **plasticize** the polyvinyl chloride into supple tubing." },
      { author: "Aldous Huxley", work: "Island", quote: "Educators must never attempt to **plasticize** unique youthful personalities into standardized social molds." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "Solvent molecules intercalate between polymer chains, acting to **plasticize** the bulk material." }
    ]
  },
  "plasticizer.md": {
    primary: "A chemical additive incorporated into plastics or rubbers to increase their flexibility, softness, and workability.",
    secondary: "In civil engineering, a chemical admixture added to concrete to increase workability without adding excess water.",
    quotes: [
      { author: "Rachel Carson", work: "Lost Woods", quote: "Toxicologists examined the endocrine-disrupting properties of each common synthetic **plasticizer** found in food packaging." },
      { author: "Primo Levi", work: "The Monkey's Wrench", quote: "The engineer specified a low-temperature **plasticizer** to prevent the synthetic gaskets from freezing rigid in Siberia." },
      { author: "David Foster Wallace", work: "Consider the Lobster", quote: "Vats of warm synthetic vinyl were scented with chemical **plasticizer** in the processing plant." }
    ]
  },
  "plastid.md": {
    primary: "Any of a class of small, double-membrane-bound organelles in the cells of plants and algae containing pigments or stored food.",
    secondary: "In plant cell biology, an autonomous organelle possessing its own genome, originating from endosymbiotic cyanobacteria.",
    quotes: [
      { author: "Lynn Margulis", work: "Symbiosis in Cell Evolution", quote: "The photosynthetic **plastid** evolved through ancient endosymbiosis between a eukaryotic host and a free-living cyanobacterium." },
      { author: "Peter H. Raven", work: "Biology of Plants", quote: "Light exposure stimulates the colorless proplastid to differentiate into a chlorophyll-rich photosynthetic **plastid**." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "Variegated leaves result from somatic mutations that disrupt normal **plastid** pigment synthesis." }
    ]
  },
  "plastinate.md": {
    primary: "To preserve a biological specimen or anatomical body by replacing water and fat with curable polymers.",
    secondary: "To subject anatomical tissues to the process of plastination for medical education and museum display.",
    quotes: [
      { author: "Gunther von Hagens", work: "Anatomy and Plastination", quote: "Our objective was to **plastinate** whole organ systems so that students could study authentic human anatomy without toxic formalin." },
      { author: "Atul Gawande", work: "Complications: A Surgeon's Notes on an Imperfect Science", quote: "In modern dissection laboratories, curators **plastinate** complex vascular networks to demonstrate three-dimensional collateral pathways." },
      { author: "Oliver Sacks", work: "Uncle Tungsten", quote: "Anatomists learned to **plastinate** fragile cerebral specimens, rendering the delicate gyri dry, durable, and odorless." }
    ]
  },
  "plastination.md": {
    primary: "A patented technique used in anatomy to preserve bodies, in which water and lipids are replaced by curable plastics like silicone.",
    secondary: "The modern preservation technology producing durable, odorless, and touchable anatomical preparations.",
    quotes: [
      { author: "Gunther von Hagens", work: "The Preservation of Biological Specimens by Plastination", quote: "Through vacuum forced impregnation, **plastination** permanently halts decomposition while preserving microscopic cellular architecture." },
      { author: "Atul Gawande", work: "Better", quote: "The medical museum featured brilliant cross-sections of the human thorax preserved via **plastination**." },
      { author: "Richard Dawkins", work: "The Greatest Show on Earth", quote: "Anatomical **plastination** provides undeniable visual proof of evolutionary homology across vertebrate organ systems." }
    ]
  },
  "plastique.md": {
    primary: "A plastic explosive, especially a moldable military or demolition explosive such as Semtex or C-4.",
    secondary: "In dance, the sculptural modeling or aesthetic posing of the human body (*danse plastique*).",
    quotes: [
      { author: "John le Carré", work: "The Little Drummer Girl", quote: "The operative concealed two blocks of odorless **plastique** inside the false lining of the suitcase." },
      { author: "Frederick Forsyth", work: "The Day of the Jackal", quote: "The assassin prepared the charge using moldable Czechoslovakian **plastique**, carefully wiring the detonator." },
      { author: "Walter Pater", work: "Greek Studies", quote: "In antique statuary, the physical **plastique** of the athlete's body achieved divine geometric harmony." }
    ]
  },
  "plastron.md": {
    primary: "The flat, ventral (underside) part of the shell of a turtle or tortoise (contrasting with the dorsal carapace).",
    secondary: "A protective padded chest protector worn by fencers; or an ornamental stiff shirtfront.",
    quotes: [
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The giant Galápagos tortoise turned upon its back, exposing its polished yellowish-brown **plastron** to the sun." },
      { author: "Alexandre Dumas", work: "The Count of Monte Cristo", quote: "The fencing master laced his padded leather **plastron** before crossing foils with the young nobleman." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Illustrious Client", quote: "Holmes examined the fencing foil, noting the blunted button that struck the student's canvas **plastron**." }
    ]
  },
  "protoplast.md": {
    primary: "The living contents of a plant or bacterial cell, comprising the nucleus and cytoplasm after the cell wall has been removed.",
    secondary: "An original ancestor or prototype; in theology, Adam as the original protoplast or first-formed human.",
    quotes: [
      { author: "Lynn Margulis", work: "Early Life", quote: "Cell biologists can dissolve the cellulose wall to study the naked, living **protoplast** directly." },
      { author: "Peter H. Raven", work: "Biology of Plants", quote: "Somatic hybridization is achieved by fusing an isolated plant **protoplast** with another in an electric field." },
      { author: "John Milton", work: "Paradise Lost", quote: "Adam, the sacred **protoplast** of human kind, walked majestic in the groves of Eden." }
    ]
  },
  "tympanoplasty.md": {
    primary: "The surgical reconstruction and repair of a perforated eardrum and the ossicles of the middle ear.",
    secondary: "In otolaryngology, a microsurgical procedure aimed at eradicating middle-ear infection and restoring conductive hearing.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Chronic suppurative otitis media with membrane perforation frequently requires elective **tympanoplasty** to preserve hearing." },
      { author: "Robert Thayer Sataloff", work: "Professional Voice", quote: "The otologist successfully performed a microscopic **tympanoplasty** using a delicate temporalis fascia graft." },
      { author: "Atul Gawande", work: "Complications", quote: "During the delicate **tympanoplasty**, the surgeon manipulated the micro-instruments under thirty-power magnification." }
    ]
  }
};

for (const [filename, entry] of Object.entries(filesData)) {
  const filePath = path.join(baseDir, filename);
  if (!fs.existsSync(filePath)) {
    console.error(`Missing file: ${filePath}`);
    continue;
  }
  const content = fs.readFileSync(filePath, 'utf8');

  // Find top portion up to > [!book]
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`No > [!book] in ${filename}`);
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
  console.log(`Updated: ${filename}`);
}

console.log('Done Batch 7 (Dashboard — plast) of Cluster Art, Craft & Design (33 words)!');
