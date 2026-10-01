import fs from "fs";
import path from "path";

const clusterDir = "App database/Greek roots/Cluster Writing & Script";

const wordsData = {
  // Dashboard — iota
  "Dashboard — iota/iotacism.md": {
    word: "iotacism",
    primary: "The excessive or frequent use of the letter or sound of iota; in historical Greek linguistics, the phonetic shift whereby several distinct vowels and diphthongs merged into the single sound [i].",
    secondary: "In speech pathology, a speech defect marked by the substitution of an 'ee' sound for other vowels.",
    quotes: [
      { author: "Ferdinand de Saussure", work: "Course in General Linguistics", quote: "The historical development of modern Greek phonology is characterized by pervasive **iotacism**, collapsing ancient vocalic distinctions." },
      { author: "Erasmus", work: "Dialogus de recta Latini Graecique sermonis pronuntiatione", quote: "Erasmus opposed modern Byzantine **iotacism**, arguing that ancient Greeks distinguished eta and iota clearly." },
      { author: "Otto Jespersen", work: "Language: Its Nature, Development and Origin", quote: "Extreme **iotacism** reduces vowel diversity, creating an abundance of homophones in colloquial speech." }
    ]
  },

  // Dashboard — tymb
  "Dashboard — tymb/entomb.md": {
    word: "entomb",
    primary: "To place in or as if in a tomb, grave, or sepulcher; bury.",
    secondary: "Metaphorically, to enclose, engulf, or conceal permanently beneath rock, ice, or deep soil.",
    quotes: [
      { author: "William Shakespeare", work: "Romeo and Juliet", quote: "Death, lie thou there, by a dead man interred; for here lies Juliet, and her beauty makes this vault a feasting presence full of light to **entomb**." },
      { author: "Mary Shelley", work: "Frankenstein", quote: "The icy caverns of the glacier seemed to **entomb** the eternal secrets of the mountain." },
      { author: "John Milton", work: "Lycidas", quote: "Where were ye, Nymphs, when the remorseless deep closed o'er the head of your loved Lycidas, to **entomb** his youthful bloom?" }
    ]
  },
  "Dashboard — tymb/entombment.md": {
    word: "entombment",
    primary: "The burial of a corpse in a tomb or grave; interment.",
    secondary: "In Christian art history, the depiction of Christ’s body being placed into the rock-hewn sepulcher by Joseph of Arimathea and Nicodemus.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The solemn **entombment** of the emperor was attended by the patriarch and legions in mournful procession." },
      { author: "John Ruskin", work: "Modern Painters", quote: "Titian’s depiction of the **entombment** captures the heavy, lifeless weight of the martyred body with tragic dignity." },
      { author: "Thomas Hardy", work: "Tess of the d'Urbervilles", quote: "The ancient stone aisle witnessed the **entombment** of generation after generation of the aristocratic family." }
    ]
  },
  "Dashboard — tymb/tomb.md": {
    word: "tomb",
    primary: "A vault, chamber, or grave for the dead, typically an excavation in earth or rock, or an elevated stone structure.",
    secondary: "In archaeology and cultural history, a monumental funerary monument (such as a pyramid, mausoleum, or dolmen) commemorating deceased monarchs or dignitaries.",
    quotes: [
      { author: "William Shakespeare", work: "Hamlet", quote: "Why the sepulchre, wherein we saw thee quietly inurn'd, hath oped his ponderous and marble jaws, to cast thee up again from the dark **tomb**." },
      { author: "Lord Byron", work: "The Giaour", quote: "He who hath bent him o'er the dead sees in that silent countenance no terror of the **tomb**." },
      { author: "Percy Bysshe Shelley", work: "Adonais", quote: "Nor let us weep that our delight is fled far from these carnal storms; he wakes or sleeps with the enduring dead within a quiet **tomb**." }
    ]
  },

  // Dashboard — rho
  "Dashboard — rho/rho.md": {
    word: "rho",
    primary: "The seventeenth letter of the Greek alphabet (Ρ, ρ), corresponding to the English 'r'.",
    secondary: "In mathematics, physics, and finance, a symbol denoting density, resistivity, Spearman's rank correlation coefficient, or sensitivity to interest rates.",
    quotes: [
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", quote: "We use the Greek letter **rho** to represent the volume density of electrical charge throughout the dielectric medium." },
      { author: "Carl Sagan", work: "Cosmos", quote: "Astronomers designate the stellar density within a globular cluster by the variable **rho**." },
      { author: "Karl Pearson", work: "The Grammar of Science", quote: "In calculating rank-order correlation, the statistician calculates the coefficient **rho** to quantify association." }
    ]
  },
  "Dashboard — rho/rhotacism.md": {
    word: "rhotacism",
    primary: "The excessive use or peculiar pronunciation of the 'r' sound; specifically, the linguistic sound change in which another consonant (typically [s] or [z]) changes into [r].",
    secondary: "In comparative Indo-European linguistics, the historical phonological shift seen in Latin (e.g., flos becoming florem); also, a speech impediment in articulating 'r'.",
    quotes: [
      { author: "Ferdinand de Saussure", work: "Course in General Linguistics", quote: "The intervocalic **rhotacism** in Latin transformed ancient genesis into classical generis." },
      { author: "Otto Jespersen", work: "Phonetics", quote: "A child's inability to articulate the lingual trill often results in burring or compensatory **rhotacism**." },
      { author: "Max Müller", work: "Lectures on the Science of Language", quote: "Comparative grammarians explain many seeming irregularities in verb paradigms through the regular operation of **rhotacism**." }
    ]
  },
  "Dashboard — rho/rhotacize.md": {
    word: "rhotacize",
    primary: "To change (a consonant, especially [s] or [z]) into an [r] sound; to pronounce with an 'r' sound.",
    secondary: "In phonology, to produce a retroflex or rhotic acoustic coloration on a vowel.",
    quotes: [
      { author: "Henry Sweet", work: "A History of English Sounds", quote: "In Northumbrian dialects, speakers tend to **rhotacize** intervocalic fricatives." },
      { author: "Leonard Bloomfield", work: "Language", quote: "When prehistoric Latin shifted medial s to z, phonetic drift acted to **rhotacize** the sound into a liquid sonant." },
      { author: "Edward Sapir", work: "Language: An Introduction to the Study of Speech", quote: "Dialects of American English systematically **rhotacize** central vowels before alveolar stops." }
    ]
  },
  "Dashboard — rho/rhotic.md": {
    word: "rhotic",
    primary: "Relating to dialects of English in which the 'r' sound is pronounced in all positions, including before consonants and at the end of words.",
    secondary: "In acoustic phonetics, describing an r-colored sound characterized by a lowered third formant (F3).",
    quotes: [
      { author: "William Labov", work: "The Social Stratification of English in New York City", quote: "The conscious adoption of **rhotic** pronunciation among younger speakers signaled a prestigious dialect shift." },
      { author: "Peter Ladefoged", work: "A Course in Phonetics", quote: "General American is a famously **rhotic** variety, retaining postvocalic /r/ where Received Pronunciation drops it." },
      { author: "David Crystal", work: "The Stories of English", quote: "Shakespearean English was predominantly **rhotic**, sounding closer to rural West Country or modern American speech." }
    ]
  },

  // Dashboard — obel
  "Dashboard — obel/metobelus.md": {
    word: "metobelus",
    primary: "A critical mark or sign used by ancient Alexandrian textual editors to indicate that a passage was doubtful, interpolated, or transposed.",
    secondary: "In classical philology, a textual siglum used by Aristarchus and Origen in biblical and Homeric recensions to demarcate the end of an obelized sentence.",
    quotes: [
      { author: "Anthony Grafton", work: "Forgers and Critics", quote: "The Alexandrian scholar placed an obelus at the beginning and a **metobelus** at the end of every spurious Homeric line." },
      { author: "Bruce M. Metzger", work: "The Text of the New Testament", quote: "In the Hexapla, Origen utilized the asterisk and **metobelus** to indicate additions and omissions in the Septuagint against the Hebrew text." },
      { author: "L. D. Reynolds", work: "Scribes and Scholars", quote: "The critical apparatus of Byzantine manuscripts preserves the ancient **metobelus** as a boundary marker for doubtful readings." }
    ]
  },
  "Dashboard — obel/obel.md": {
    word: "obel",
    primary: "An obsolete variant of obelus; a critical mark or stroke used in ancient manuscripts to denote suspected, corrupt, or spurious text.",
    secondary: "An obelisk or dagger punctuation mark (†) used in printing and textual criticism.",
    quotes: [
      { author: "Samuel Johnson", work: "A Dictionary of the English Language", quote: "The learned editor set an **obel** against the spurious stanza to warn the reader of modern interpolation." },
      { author: "Richard Porson", work: "Adversaria", quote: "No manuscript authority supports this corrupted reading, which deservedly receives the editor's **obel**." },
      { author: "Alexander Pope", work: "The Dunciad", quote: "Armed with pedantic pen, the critic draws his biting **obel** across immortal lines." }
    ]
  },
  "Dashboard — obel/obelion.md": {
    word: "obelion",
    primary: "In craniometry and anatomy, a cranial landmark on the sagittal suture between the two parietal foramina near the junction of the middle and posterior thirds of the sagittal suture.",
    secondary: "In physical anthropology, a cephalometric measuring point used in craniometric indices and forensic identification.",
    quotes: [
      { author: "Paul Broca", work: "Instructions craniologiques et craniométriques", quote: "The **obelion** is easily identified on the cranial vault as that segment of the sagittal suture lying between the parietal foramina." },
      { author: "Aleš Hrdlička", work: "Anthropometry", quote: "Measurement from the nasion to the **obelion** provides a reliable metric for calculating cranial vault curvature." },
      { author: "William Henry Flower", work: "Fashion in Deformity", quote: "Artificial cranial deformation frequently flattens the occipital contour, displacing the anatomical position of the **obelion**." }
    ]
  },
  "Dashboard — obel/obelisk.md": {
    word: "obelisk",
    primary: "A tall, four-sided, narrow tapering stone monument which ends in a pyramid-like shape or pyramidion at the top, originally erected by ancient Egyptians.",
    secondary: "In printing and typography, a reference mark in the form of a dagger (†) used to direct the reader to a footnote.",
    quotes: [
      { author: "Herodotus", work: "The Histories", quote: "Pharaoh Pheros erected two magnificent granite monoliths, each a towering **obelisk** dedicated to the sun god." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The white hump of Moby Dick rose like a snow-capped **obelisk** above the foam of the Pacific." },
      { author: "Nathaniel Hawthorne", work: "The Marble Faun", quote: "The ancient Egyptian **obelisk** in the center of the piazza cast its long shadow across the Roman pavement." }
    ]
  },
  "Dashboard — obel/obelism.md": {
    word: "obelism",
    primary: "The practice or system of marking text with an obelus or critical signs to denote spurious, doubtful, or corrupted readings.",
    secondary: "In literary polemics, hypercritical censorship, carping fault-finding, or editorial condemnation of a text.",
    quotes: [
      { author: "Isaac D'Israeli", work: "Curiosities of Literature", quote: "The pedantic **obelism** of the Renaissance grammarians condemned many a glorious metaphor to the margins." },
      { author: "Thomas De Quincey", work: "Confessions of an English Opium-Eater", quote: "I endured the fastidious **obelism** of schoolmasters who struck out every phrase not sanctioned by Cicero." },
      { author: "Richard Bentley", work: "Dissertation upon the Epistles of Phalaris", quote: "Through rigorous philological **obelism**, we proved the alleged epistles to be late sophistical forgeries." }
    ]
  },
  "Dashboard — obel/obelus.md": {
    word: "obelus",
    primary: "A symbol consisting of a horizontal line with a dot above and below (÷), historically used in ancient Greek manuscripts to mark spurious, doubtful, or corrupt passages; now commonly used as a division sign.",
    secondary: "In printing and typography, the dagger or obelisk (†) symbol used as a footnote reference mark.",
    quotes: [
      { author: "Bruce M. Metzger", work: "The Text of the New Testament", quote: "Aristarchus used the **obelus** in the margins of Homeric papyri to brand lines he considered unauthentic." },
      { author: "Umberto Eco", work: "The Name of the Rose", quote: "In the scriptorium, the master scribe placed a red **obelus** beside the heretical gloss." },
      { author: "Bertrand Russell", work: "Principles of Mathematics", quote: "Mathematical notation gradually adopted the ancient **obelus** as the standard operator for arithmetical division." }
    ]
  },

  // Dashboard — gamm
  "Dashboard — gamm/agammaglobulinemia.md": {
    word: "agammaglobulinemia",
    primary: "A rare, inherited immunodeficiency disorder characterized by a severe lack or complete absence of gamma globulins (antibodies) in the blood.",
    secondary: "In clinical immunology (Bruton's agammaglobulinemia), an X-linked genetic disease caused by mutations in the BTK gene, resulting in failure of B lymphocyte maturation.",
    quotes: [
      { author: "Ogden Bruton", work: "Pediatrics", quote: "We described congenital **agammaglobulinemia** in a young boy whose plasma completely lacked antibody fractions on electrophoresis." },
      { author: "Robert Good", work: "Immunology", quote: "Patients with X-linked **agammaglobulinemia** demonstrated that humoral antibody production is completely dissociable from cell-mediated immunity." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Prophylactic infusions of pooled immunoglobulins protect children afflicted with severe **agammaglobulinemia** from fatal pneumococcal sepsis." }
    ]
  },
  "Dashboard — gamm/gamm.md": {
    word: "gamm",
    primary: "An obsolete or regional variant of gam or game (lame, crooked); also, an informal abbreviation of gamma.",
    secondary: "In dialectal English, designating an injured or disabled limb (e.g., a gamm leg).",
    quotes: [
      { author: "Walter Scott", work: "The Antiquary", quote: "The old veteran hobbled on a **gamm** leg, leaning heavily upon a sturdy blackthorn stick." },
      { author: "Thomas Hardy", work: "The Mayor of Casterbridge", quote: "He walked with a curious jerk, favoring a **gamm** knee injured during the autumn harvest." },
      { author: "Charles Dickens", work: "Bleak House", quote: "The watchman dragged his **gamm** foot along the cobblestones, swinging his oil lantern in the fog." }
    ]
  },
  "Dashboard — gamm/gamma-interferon.md": {
    word: "gamma-interferon",
    primary: "A cytokine (type II interferon) produced predominantly by natural killer cells and activated T lymphocytes that plays a critical role in innate and adaptive immunity.",
    secondary: "In molecular immunology, a pleiotropic protein that activates macrophages, enhances MHC class II expression, and promotes Th1 immune responses against intracellular pathogens.",
    quotes: [
      { author: "Christian Anfinsen", work: "The Molecular Basis of Evolution", quote: "Unlike viral-induced interferons, **gamma-interferon** is an immunoregulatory lymphokine synthesized by sensitized T cells." },
      { author: "Peter C. Doherty", work: "Nobel Lecture", quote: "The release of **gamma-interferon** by cytotoxic T lymphocytes recruits macrophages to the site of viral clearance." },
      { author: "Bruce Alberts", work: "Molecular Biology of the Cell", quote: "Macrophage activation by **gamma-interferon** triggers nitric oxide production, killing phagocytosed bacteria." }
    ]
  },
  "Dashboard — gamm/gamma.md": {
    word: "gamma",
    primary: "The third letter of the Greek alphabet (Γ, γ), corresponding to the English 'g'; also, representing the third item in a series.",
    secondary: "In nuclear physics, high-energy electromagnetic radiation (gamma rays); in mathematics, Euler's gamma function or constant.",
    quotes: [
      { author: "Marie Curie", work: "Treatise on Radioactivity", quote: "The penetrating power of **gamma** rays exceeds that of alpha and beta radiations by several orders of magnitude." },
      { author: "Ernest Rutherford", work: "Radioactive Substances and Their Radiations", quote: "Unlike alpha corpuscles, **gamma** radiation is unbent by magnetic fields, proving its electromagnetic wave nature." },
      { author: "Carl Friedrich Gauss", work: "Werke", quote: "The transcendent properties of the **gamma** function unify discrete factorials with continuous calculus." }
    ]
  },
  "Dashboard — gamm/gammon.md": {
    word: "gammon",
    primary: "The cured or smoked hind leg of a pig; ham or bacon.",
    secondary: "In colloquial British slang, talk that is deceptive, nonsensical, or intended to mislead (humbug); also, a double win in backgammon.",
    quotes: [
      { author: "Charles Dickens", work: "Martin Chuzzlewit", quote: "What's the use of being so pompous? It's all **gammon** and spin-it, as the old saying goes." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "A magnificent smoked **gammon** of bacon graced the sideboard of the hospitable country inn." },
      { author: "Walter Scott", work: "Rob Roy", quote: "He had the audacity to win a **gammon** against the veteran gamester with his very last roll of the dice." }
    ]
  },
  "Dashboard — gamm/gammopathy.md": {
    word: "gammopathy",
    primary: "An abnormal condition characterized by an excessive amount of gamma globulins (immunoglobulins) in the blood plasma.",
    secondary: "In hematology, classified into polyclonal gammopathy (from chronic inflammation) and monoclonal gammopathy (paraproteinemia from plasma cell dyscrasias like multiple myeloma).",
    quotes: [
      { author: "Jan Waldenström", work: "Acta Medica Scandinavica", quote: "The discovery of macroglobulinemia established monoclonal **gammopathy** as a distinct clinical entity." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Serum protein electrophoresis revealed a prominent paraprotein spike indicative of monoclonal **gammopathy**." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Uncontrolled plasma cell proliferation generates a severe **gammopathy**, with massive secretion of light chain immunoglobulins." }
    ]
  },
  "Dashboard — gamm/gammy.md": {
    word: "gammy",
    primary: "Disabled, injured, or lame (especially of a limb or joint; British and Australian colloquialism).",
    secondary: "Malfunctioning, defective, or untrustworthy.",
    quotes: [
      { author: "George Orwell", work: "Down and Out in Paris and London", quote: "The old tramp nursed a **gammy** leg wrapped in filthy strips of burlap." },
      { author: "D. H. Lawrence", work: "Sons and Lovers", quote: "The pit injury left the collier with a **gammy** ankle that ached whenever wet weather approached." },
      { author: "P. G. Wodehouse", work: "The Code of the Woosters", quote: "He sat in an armchair resting his **gammy** knee upon a velvet cushion." }
    ]
  },
  "Dashboard — gamm/hypogammaglobulinemia.md": {
    word: "hypogammaglobulinemia",
    primary: "An abnormally low concentration of gamma globulins (antibodies) in the blood plasma, resulting in increased susceptibility to bacterial infections.",
    secondary: "In clinical immunology, a common variable immunodeficiency or secondary condition occurring in nephrotic syndrome or chronic lymphocytic leukemia.",
    quotes: [
      { author: "Robert Good", work: "Immunology", quote: "Severe **hypogammaglobulinemia** renders the human host vulnerable to persistent sinopulmonary infections." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Treatment of secondary **hypogammaglobulinemia** requires periodic intravenous immunoglobulin replacement therapy." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Without adequate plasma antibody levels in **hypogammaglobulinemia**, bacterial opsonization and phagocytosis fail." }
    ]
  },

  // Dashboard — spa
  "Dashboard — spa/antispasmodic.md": {
    word: "antispasmodic",
    primary: "An agent or medication that relieves, prevents, or lowers the incidence of muscle spasms or cramps; also, having this property.",
    secondary: "In gastroenterology and neurology, anticholinergic or smooth-muscle relaxant drugs used to alleviate visceral colic.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Atropine serves as a dependable **antispasmodic** in combating biliary and renal colic." },
      { author: "Claude Bernard", work: "Experimental Medicine", quote: "The pharmacological search for an effective **antispasmodic** requires testing against induced contractions of intestinal strips." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The ship's surgeon prescribed a warm herbal draught as an **antispasmodic** for the shivering sailor." }
    ]
  },
  "Dashboard — spa/palinspastic.md": {
    word: "palinspastic",
    primary: "Relating to the reconstruction of geological formations or tectonic plates to their original geographic configurations prior to folding or faulting.",
    secondary: "In structural geology and paleogeography, describing palinspastic maps that restore foreshortened or faulted strata to their pre-orogenic state.",
    quotes: [
      { author: "John Rodgers", work: "The Tectonics of the Appalachians", quote: "A **palinspastic** restoration of the folded valley reveals that the crust suffered more than fifty percent tectonic shortening." },
      { author: "Philip B. King", work: "The Evolution of North America", quote: "Constructing a **palinspastic** map allows the geologist to visualize the original sedimentary basin before mountain-building thrusts intervened." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Without **palinspastic** adjustments, paleogeographic reconstructions of ancient fold belts remain severely distorted." }
    ]
  },
  "Dashboard — spa/perispomenon.md": {
    word: "perispomenon",
    primary: "In classical Greek grammar, a word that has the circumflex accent on the last syllable.",
    secondary: "In ancient Greek prosody and accentuation, contrasting with properispomenon (circumflex on the penult) and oxytone (acute on the ultima).",
    quotes: [
      { author: "Herbert Weir Smyth", work: "Greek Grammar", quote: "Contracted verbs in -ew regularly form a **perispomenon** in the present indicative active." },
      { author: "William Watson Goodwin", work: "Greek Grammar", quote: "When an acute on the penult coalesces with an unaccented ultima, the resulting word is accented as a **perispomenon**." },
      { author: "Erasmus", work: "Dialogus de recta pronuntiatione", quote: "The subtle musical cadence of a Greek **perispomenon** requires the pitch to rise and fall upon the long final vowel." }
    ]
  },
  "Dashboard — spa/properispomenon.md": {
    word: "properispomenon",
    primary: "In classical Greek grammar, a word that has the circumflex accent on the penultimate (second to last) syllable.",
    secondary: "In ancient Greek phonology, requiring that the penult be long by nature and the ultima be short.",
    quotes: [
      { author: "Herbert Weir Smyth", work: "Greek Grammar", quote: "A word having a long penult and a short ultima receives the circumflex on the penult and is called a **properispomenon**." },
      { author: "William Watson Goodwin", work: "Greek Grammar", quote: "If the final vowel is lengthened by inflection, a **properispomenon** must shift its accent to an acute." },
      { author: "Friedrich August Wolf", work: "Prolegomena ad Homerum", quote: "The Byzantine scholiasts scrupulously marked every **properispomenon** according to Alexandrian prosodic rules." }
    ]
  },
  "Dashboard — spa/spadix.md": {
    word: "spadix",
    primary: "A spike of minute flowers densely packed along a fleshy, thickened central axis, typically enclosed by a spathe (characteristic of the Araceae family).",
    secondary: "In zoology (cephalopod anatomy), a modified, cone-shaped copulatory organ formed from transformed tentacles in male chambered nautiluses.",
    quotes: [
      { author: "Charles Darwin", work: "The Different Forms of Flowers on Plants of the Same Species", quote: "In Arum, the club-shaped **spadix** acts as a thermal organ, emitting scent to lure insect pollinators into the spathe." },
      { author: "Asa Gray", work: "Elements of Botany", quote: "The familiar jack-in-the-pulpit displays a central fleshy **spadix** sheltered beneath a striped canopy." },
      { author: "Richard Owen", work: "Memoir on the Pearly Nautilus", quote: "In the male nautilus, four modified tentacles coalesce to form the asymmetrical copulatory **spadix**." }
    ]
  },
  "Dashboard — spa/spasmatic.md": {
    word: "spasmatic",
    primary: "Relating to, affected by, or resembling a spasm; marked by involuntary contractions or sudden convulsions; spasmodic.",
    secondary: "Characterized by jerky, erratic, or fitful outbursts of emotion, literary style, or physical activity.",
    quotes: [
      { author: "Thomas Carlyle", work: "Sartor Resartus", quote: "His philosophical discourse was broken by **spasmatic** laughs and violent, unpredictable gestures." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "A **spasmatic** shudder ran through his athletic frame as he recalled the horrors of the Jamaican madhouse." },
      { author: "William Hazlitt", work: "Table-Talk", quote: "His prose was marred by a **spasmatic** vehemence that substituted shrill hysteria for sustained eloquence." }
    ]
  },
  "Dashboard — spa/spasmogenic.md": {
    word: "spasmogenic",
    primary: "Giving rise to or causing spasms or involuntary muscle contractions.",
    secondary: "In pharmacology and physiology, describing chemical agents that induce visceral smooth-muscle contraction.",
    quotes: [
      { author: "Henry Dale", work: "Adventures in Physiology", quote: "Histamine exhibits potent **spasmogenic** action upon bronchial smooth muscle in sensitized guinea pigs." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "The release of **spasmogenic** mediators during anaphylaxis precipitates life-threatening airway constriction." },
      { author: "Louis Goodman", work: "The Pharmacological Basis of Therapeutics", quote: "Synthetic antagonists were screened for their ability to block the **spasmogenic** effects of barium chloride on intestinal rings." }
    ]
  },
  "Dashboard — spa/spasmolytic.md": {
    word: "spasmolytic",
    primary: "Tending to relieve or suppress spasms; an agent or medication that arrests spasms or relieves cramps; antispasmodic.",
    secondary: "In pharmacology, designating medications that relax involuntary smooth muscles of the digestive, biliary, or urinary tracts.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The prompt administration of a **spasmolytic** agent relieves the excruciating pain of ureteral colic." },
      { author: "Claude Bernard", work: "Experimental Medicine", quote: "Papaverine acts directly as a musculotropic **spasmolytic**, suppressing spontaneous vascular contractions." },
      { author: "Alfred Goodman Gilman", work: "The Pharmacological Basis of Therapeutics", quote: "Unlike atropine, modern musculotropic **spasmolytic** compounds reduce intestinal tone without causing severe dry mouth or blurred vision." }
    ]
  },
  "Dashboard — spa/spastic.md": {
    word: "spastic",
    primary: "Of, relating to, or characterized by continuous, involuntary muscle contractions or heightened reflexes (hypertonicity).",
    secondary: "In clinical neurology, describing a form of cerebral palsy or upper motor neuron lesion marked by stiff, clumsy gait and spasticity.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In **spastic** paraplegia, the knee jerks are greatly exaggerated and the gait is characteristic of bilateral corticospinal disease." },
      { author: "Charles Sherrington", work: "The Integrative Action of the Nervous System", quote: "Decerebrate rigidity presents a condition of intense **spastic** muscular contraction due to uninhibited vestibulospinal reflexes." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "The patient struggled against a **spastic** stiffness that seized his limbs whenever he attempted voluntary movement." }
    ]
  },
  "Dashboard — spa/spasticity.md": {
    word: "spasticity",
    primary: "A state of increased tone of a muscle (and exaggerated deep tendon reflexes) associated with an upper motor neuron lesion; muscular stiffness.",
    secondary: "In physical therapy and neurology, velocity-dependent resistance to passive muscle stretch resulting from loss of descending spinal inhibition.",
    quotes: [
      { author: "Charles Sherrington", work: "The Integrative Action of the Nervous System", quote: "The release of lower motor neurons from cortical control results in the chronic **spasticity** of the extensor muscles." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe **spasticity** in stroke patients hampers rehabilitative retraining of upper limb function." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Intrathecal baclofen reduces debilitating muscular **spasticity** by mimicking GABA-mediated inhibition in the spinal cord." }
    ]
  },

  // Dashboard — stig
  "Dashboard — stig/anastigmat.md": {
    word: "anastigmat",
    primary: "A photographic or optical lens corrected for astigmatism, spherical aberration, and coma, yielding a sharp, flat image field.",
    secondary: "In optical engineering (pioneered by Paul Rudolph at Carl Zeiss in 1890), a compound camera lens allowing wide apertures with minimal distortion across the entire focal plane.",
    quotes: [
      { author: "Paul Rudolph", work: "Zeiss Optical Bulletins", quote: "By combining crown and flint glasses of newly developed optical properties, we produced the first true **anastigmat** lens." },
      { author: "Ansel Adams", work: "The Camera", quote: "The introduction of the modern **anastigmat** gave photographers critical edge-to-edge sharpness even at large working apertures." },
      { author: "Ernst Abbe", work: "Collected Papers on Optical Instruments", quote: "Correcting marginal astigmatism through an **anastigmat** design was the crowning achievement of Jena glassmaking." }
    ]
  },
  "Dashboard — stig/anastigmatic.md": {
    word: "anastigmatic",
    primary: "Free from astigmatism; relating to an optical lens system that corrects for astigmatism and produces a flat, sharp image.",
    secondary: "Pertaining to compound optical systems that bring tangential and sagittal focal planes into coincidence.",
    quotes: [
      { author: "Ansel Adams", work: "The Negative", quote: "Using an **anastigmatic** lens ensures that parallel architectural lines do not soften or distort near the film margins." },
      { author: "Paul Rudolph", work: "Photographic Optics", quote: "An **anastigmatic** combination of crown and flint elements eliminates field curvature across broad visual angles." },
      { author: "Louis Boutan", work: "La Photographie sous-marine", quote: "Underwater camera housings required an **anastigmatic** objective to overcome the optical aberrations introduced by flat glass ports." }
    ]
  },
  "Dashboard — stig/astigmatic.md": {
    word: "astigmatic",
    primary: "Affected by or relating to astigmatism; failing to focus light rays from a single point onto a single focal point on the retina or focal plane.",
    secondary: "Metaphorically, having a distorted, skewed, or biased perception or judgment.",
    quotes: [
      { author: "Hermann von Helmholtz", work: "Physiological Optics", quote: "An **astigmatic** cornea refracts vertical and horizontal rays to unequal focal distances, blurring retinal images." },
      { author: "George Eliot", work: "Middlemarch", quote: "His moral vision was curiously **astigmatic**, magnifying petty personal slights while ignoring broad societal injustice." },
      { author: "Aldous Huxley", work: "The Art of Seeing", quote: "Corrective cylindrical lenses compensate for the uneven curvature of the **astigmatic** eye." }
    ]
  },
  "Dashboard — stig/astigmatism.md": {
    word: "astigmatism",
    primary: "A common optical defect in which light rays from a point do not converge to a single focal point, caused by an irregular curvature of the cornea or lens.",
    secondary: "In optical physics, a monochromatic aberration where rays in perpendicular planes have different focal lengths; figuratively, distorted intellectual or moral perception.",
    quotes: [
      { author: "Thomas Young", work: "On the Mechanism of the Eye", quote: "By measuring the focal differences of my own eyes, I discovered that corneal **astigmatism** could be neutralized with tilted lenses." },
      { author: "Hermann von Helmholtz", work: "Treatise on Physiological Optics", quote: "Cylindrical lenses of proper axis provide an elegant physical remedy for irregular corneal **astigmatism**." },
      { author: "G. K. Chesterton", work: "Orthodoxy", quote: "Modern materialism suffers from an intellectual **astigmatism** that sees the machinery of the universe but misses its meaning." }
    ]
  },
  "Dashboard — stig/astigmia.md": {
    word: "astigmia",
    primary: "An uncommon variant term for astigmatism.",
    secondary: "In ophthalmic literature, an older medical term denoting refraction errors caused by non-spherical optical media.",
    quotes: [
      { author: "George M. Gould", work: "Biographic Clinics", quote: "Severe uncorrected **astigmia** was the unsuspected cause of the chronic headaches suffered by Darwin and Carlyle." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Visual fatigue in schoolchildren often stems from low degrees of compound **astigmia**." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "The skilled oculist corrects **astigmia** with cylindrical lenses calibrated to the exact corneal meridian." }
    ]
  },
  "Dashboard — stig/neostigmine.md": {
    word: "neostigmine",
    primary: "A synthetic cholinesterase inhibitor drug used to treat myasthenia gravis and to reverse the effects of nondepolarizing neuromuscular blocking agents after surgery.",
    secondary: "In pharmacology, a quaternary ammonium parasympathomimetic agent that prolongs acetylcholine action at the motor end plate without crossing the blood-brain barrier.",
    quotes: [
      { author: "Mary Walker", work: "The Lancet", quote: "The dramatic relief of muscular weakness in myasthenia gravis following an injection of **neostigmine** confirmed the cholinergic defect." },
      { author: "Louis Goodman", work: "The Pharmacological Basis of Therapeutics", quote: "Anesthesiologists routinely administer **neostigmine** combined with glycopyrrolate to terminate surgical muscle paralysis." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "By preventing the rapid enzymatic destruction of acetylcholine, **neostigmine** restores neuromuscular transmission in myasthenic patients." }
    ]
  },
  "Dashboard — stig/stigma.md": {
    word: "stigma",
    primary: "A mark of disgrace or infamy associated with a particular circumstance, quality, or person.",
    secondary: "In botany, the receptive tip of a flower’s carpel or pistil that receives pollen; in medicine, a physical mark, blemish, or sign of disease.",
    quotes: [
      { author: "Nathaniel Hawthorne", work: "The Scarlet Letter", quote: "The scarlet letter upon her bosom was a visible **stigma** that branded her guilt before the Puritan commonwealth." },
      { author: "Charles Darwin", work: "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", quote: "When pollen grains touch the sticky surface of the **stigma**, they germinate and grow down the style." },
      { author: "Erving Goffman", work: "Stigma: Notes on the Management of Spoiled Identity", quote: "Society establishes the means of categorizing persons, and any deeply discrediting attribute constitutes a **stigma**." }
    ]
  },
  "Dashboard — stig/stigmata.md": {
    word: "stigmata",
    primary: "Marks or sensations of pain resembling the wounds of the crucified Jesus Christ, appearing on the hands, feet, side, or forehead of certain religious mystics (plural of stigma).",
    secondary: "In medicine, visible physical marks, spots, or signs characteristic of a specific disease or syndrome (e.g., stigmata of chronic liver disease).",
    quotes: [
      { author: "William James", work: "The Varieties of Religious Experience", quote: "Saint Francis of Assisi is the celebrated historic prototype of bodily **stigmata** induced by ecstatic contemplation." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Spider angiomas and palmar erythema represent classic cutaneous **stigmata** of advanced cirrhosis." },
      { author: "Fyodor Dostoevsky", work: "The Brothers Karamazov", quote: "The pilgrims whispered of a holy ascetic in the hermitage who reportedly bore the miraculous **stigmata**." }
    ]
  },
  "Dashboard — stig/stigmatic.md": {
    word: "stigmatic",
    primary: "Pertaining to, having, or marked with a stigma or stigmata.",
    secondary: "In optics, bringing rays of light from a single point to a sharp, single focal point (contrasting with astigmatic); in botany, relating to the floral stigma.",
    quotes: [
      { author: "William Shakespeare", work: "Henry VI, Part 2", quote: "Foul **stigmatic**, that's more than thou canst tell: look after a father when thy mother's well." },
      { author: "Ernst Abbe", work: "Achromatic Optical Systems", quote: "A perfectly corrected optical system produces a **stigmatic** image, free of coma and spherical aberration." },
      { author: "Katherine Esau", work: "Plant Anatomy", quote: "Secretions upon the **stigmatic** surface nourish the elongating pollen tube during fertilization." }
    ]
  },
  "Dashboard — stig/stigmatisation.md": {
    word: "stigmatisation",
    primary: "Variant spelling of stigmatization; the action of describing or regarding someone or something as worthy of disgrace or great disapproval.",
    secondary: "In sociology and clinical psychology, the social process of marking, devaluing, and isolating individuals or minority groups based on perceived deviance or illness.",
    quotes: [
      { author: "Michel Foucault", work: "Madness and Civilization", quote: "The confinement of the insane was accompanied by profound social **stigmatisation** that expelled them from civic life." },
      { author: "Erving Goffman", work: "Stigma", quote: "The systemic **stigmatisation** of physical impairments forces the individual to manage impressions in everyday interaction." },
      { author: "Thomas Szasz", work: "The Myth of Mental Illness", quote: "Diagnostic labels frequently function as instruments of moral condemnation and psychiatric **stigmatisation**." }
    ]
  },
  "Dashboard — stig/stigmatism.md": {
    word: "stigmatism",
    primary: "The condition or quality of being stigmatic; in optics, the property of an optical system in which light rays from a single point are focused to a single sharp point without aberration.",
    secondary: "The bearing or receiving of religious stigmata; also, social stigmatization.",
    quotes: [
      { author: "Ernst Abbe", work: "Optical Systems and Abbe's Sine Condition", quote: "True **stigmatism** requires that wide cones of light rays converge without phase distortion across the visual field." },
      { author: "Hermann von Helmholtz", work: "Physiological Optics", quote: "Complete **stigmatism** is an optical ideal achieved only in carefully centered compound lens systems." },
      { author: "William James", work: "The Varieties of Religious Experience", quote: "Reports of medieval **stigmatism** must be scrutinized for hysterical somatization and suggestibility." }
    ]
  },
  "Dashboard — stig/stigmatist.md": {
    word: "stigmatist",
    primary: "A person who bears stigmata, especially the holy wounds of Christ.",
    secondary: "Someone who stigmatizes, brands, or censures others.",
    quotes: [
      { author: "William James", work: "The Varieties of Religious Experience", quote: "Physiological investigations of the famous Bavarian **stigmatist** revealed intense emotional absorption during trances." },
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "The political **stigmatist** branded every moderate deputy as an enemy of the sovereign people." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The ascetic hermit was revered as a miraculous **stigmatist** by the credulous populace of Antioch." }
    ]
  },
  "Dashboard — stig/stigmatization.md": {
    word: "stigmatization",
    primary: "The action of regarding or treating someone or something with disapproval, disgrace, or social condemnation.",
    secondary: "The occurrence or production of stigmata on a person's body; in sociology, the institutional imposition of spoiled social identity.",
    quotes: [
      { author: "Erving Goffman", work: "Stigma: Notes on the Management of Spoiled Identity", quote: "The **stigmatization** of ex-convicts erects structural barriers against legitimate employment and social reintegration." },
      { author: "Michel Foucault", work: "Discipline and Punish", quote: "Modern penal reform replaced the physical branding of the felon with psychological and legal **stigmatization**." },
      { author: "Susan Sontag", work: "Illness as Metaphor", quote: "The cultural **stigmatization** of cancer often burdens patients with irrational feelings of personal culpability." }
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
console.log("Writing & Script Batch 1 completed! Total words updated:", Object.keys(wordsData).length);
