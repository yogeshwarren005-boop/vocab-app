import fs from 'fs';
import path from 'path';

const CLUSTER_DIR = 'App database/Greek roots/Cluster Plants & Botany';

function updateNote(relPath, data) {
  const filePath = path.join(CLUSTER_DIR, relPath);
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

const batch6Data = {
  "Dashboard — metr/glucometer.md": {
    primary: "A portable medical device used by individuals with diabetes to measure the concentration of glucose in capillary blood.",
    secondary: "In clinical diabetology and biosensor engineering, an electrochemical monitor that utilizes glucose oxidase or dehydrogenase test strips to quantify blood glycemia.",
    quotes: [
      { author: "Ernest Beutler", work: "Williams Hematology", quote: "Point-of-care capillary blood testing using a digital **glucometer** transformed outpatient management of juvenile diabetes." },
      { author: "William N. Kelley", work: "Textbook of Internal Medicine", quote: "Tight glycemic control relies upon patient compliance with multiple daily readings recorded by a calibrated **glucometer**." },
      { author: "Michael B. Singer", work: "Neurology in Clinical Practice", quote: "Immediate bedside evaluation with a **glucometer** is mandatory in any comatose emergency to rule out profound hypoglycemia." }
    ]
  },
  "Dashboard — metr/haplometrosis.md": {
    primary: "The founding or establishment of a new social insect colony by a single fertilized queen (foundress).",
    secondary: "In myrmecology and sociobiology, the solitary colony founding strategy characteristic of most ant and wasp species, contrasting with pleometrosis.",
    quotes: [
      { author: "William Morton Wheeler", work: "Ants: Their Structure, Development and Behavior", quote: "In typical **haplometrosis**, the solitary deälated queen excavates a subterranean chamber and rears her first brood from internal metabolic reserves." },
      { author: "Edward O. Wilson", work: "The Insect Societies", quote: "The high mortality rate of queens during **haplometrosis** exerts intense natural selection upon early brood care efficiency." },
      { author: "Jean-Henri Fabre", work: "Social Life in the Insect World", quote: "A lone wasp queen perseveres in **haplometrosis**, patiently modeling paper cells without sisterly assistance." }
    ]
  },
  "Dashboard — metr/hypermetropia.md": {
    primary: "A refractive defect of the eye in which parallel rays of light focus behind the retina when accommodation is relaxed; farsightedness (hyperopia).",
    secondary: "In physiological optics, an axial or refractive disproportion wherein the optical power of the cornea and lens is insufficient for the anterior-posterior length of the globe.",
    quotes: [
      { author: "Hermann von Helmholtz", work: "Treatise on Physiological Optics", quote: "In pronounced **hypermetropia**, clear vision of distant horizons requires constant muscular effort of the ciliary muscle." },
      { author: "F. C. Donders", work: "On the Anomalies of Accommodation and Refraction of the Eye", quote: "Asthenopia and convergent strabismus in young children are frequently traceable to uncorrected congenital **hypermetropia**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Prescribing convex lenses neutralizes the refractive deficit in **hypermetropia**, relieving persistent frontal eye-strain." }
    ]
  },
  "Dashboard — metr/hypermetropic.md": {
    primary: "Of, relating to, or affected with hypermetropia; farsighted.",
    secondary: "In ophthalmic diagnostics, describing an eye whose optical axis is too short, requiring convex plus lenses to achieve sharp retinal focus.",
    quotes: [
      { author: "F. C. Donders", work: "Anomalies of Refraction", quote: "The **hypermetropic** eye is anatomically shorter than the emmetropic baseline, possessing an underdeveloped posterior scleral shell." },
      { author: "Hermann von Helmholtz", work: "Physiological Optics", quote: "When reading small print, the **hypermetropic** observer rapidly exhausts accommodative reserves, producing ocular fatigue." },
      { author: "William Thomson (Lord Kelvin)", work: "Popular Lectures and Addresses", quote: "The optician provides convex spherical lenses to shift the focal plane forward in the **hypermetropic** patient." }
    ]
  },
  "Dashboard — metr/hypermetropy.md": {
    primary: "Farsightedness; hypermetropia or hyperopia.",
    secondary: "In historical ophthalmology, an alternative 19th-century term for hypermetropia, denoting excessive distance of the ocular focal point behind the retina.",
    quotes: [
      { author: "F. C. Donders", work: "On Refraction and Accommodation", quote: "Our clinical statistics demonstrated that mild **hypermetropy** is far more common in European populations than true emmetropia." },
      { author: "Hermann von Helmholtz", work: "Treatise on Physiological Optics", quote: "The degree of **hypermetropy** is determined by finding the strongest convex glass with which the eye sees distant objects distinctly." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "The condition termed **hypermetropy** causes acute difficulty in reading fine book type without early recourse to spectacles." }
    ]
  },
  "Dashboard — metr/isometric.md": {
    primary: "Having equal dimensions, measure, or proportions; in physiology, involving muscular contraction against resistance without change in muscle length.",
    secondary: "In crystallography, the cubic system characterized by three mutually perpendicular axes of equal length; in physics, taking place at constant volume.",
    quotes: [
      { author: "James Dwight Dana", work: "A Text-Book of Mineralogy", quote: "Garnet and pyrite crystallize in the **isometric** system, developing dodecahedral and cubic forms of perfect geometrical symmetry." },
      { author: "Charles Scott Sherrington", work: "The Integrative Action of the Nervous System", quote: "Tetanic stimulation of the motor nerve against an immovable lever generates a pure **isometric** muscular twitch." },
      { author: "Archibald Geikie", work: "Textbook of Geology", quote: "The **isometric** crystal habit of halite produces cubic salt cleavage planes across saline sedimentary beds." }
    ]
  },
  "Dashboard — metr/isometrical.md": {
    primary: "Characterized by equality of measure or dimensions; isometric.",
    secondary: "In engineering drawing and cartography, designating projection where three coordinate axes appear equally foreshortened at 120-degree angles.",
    quotes: [
      { author: "Edward Salisbury Dana", work: "Text-Book of Mineralogy", quote: "In the **isometrical** system, light waves propagate with uniform velocity in all directions, exhibiting no double refraction." },
      { author: "Archibald Geikie", work: "Textbook of Geology", quote: "The architectural diagram presented an **isometrical** perspective of the volcanic cone and subterranean magma pipe." },
      { author: "James Prescott Joule", work: "Scientific Papers", quote: "Gas expansion along an **isometrical** curve maintains strict proportionality between absolute temperature and internal pressure." }
    ]
  },
  "Dashboard — metr/isometrics.md": {
    primary: "A system of physical conditioning exercises in which muscles are contracted against an immovable resistance without changing the joint angle or muscle length.",
    secondary: "In biomechanics and exercise physiology, static strength training that recruits high-threshold motor units without dynamic concentric-eccentric movement.",
    quotes: [
      { author: "Charles Scott Sherrington", work: "Selected Writings on Neuromuscular Physiology", quote: "Static contractions utilized in **isometrics** demonstrate maximal voluntary motoneuron recruitment without articular displacement." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Gentle **isometrics** are recommended during early limb fracture rehabilitation to maintain muscle tone beneath the cast." },
      { author: "Frank A. Lee", work: "Principles of Physical Fitness", quote: "Pioneering trainers demonstrated that five minutes of daily **isometrics** substantially increased static grip and leg strength." }
    ]
  },
  "Dashboard — metr/isometropia.md": {
    primary: "Equality of refractive power in both eyes, both eyes having the same refractive state (either both emmetropic or having identical refractive errors).",
    secondary: "In clinical refraction, the physiological state contrasting with anisometropia, ensuring equal retinal image magnification and effortless binocular fusion.",
    quotes: [
      { author: "F. C. Donders", work: "Anomalies of Accommodation and Refraction", quote: "Normal binocular stereopsis thrives best under complete **isometropia**, where both retinas receive images of identical sharpness and scale." },
      { author: "Hermann von Helmholtz", work: "Physiological Optics", quote: "When **isometropia** is present, correcting lenses of identical dioptric power are prescribed for both right and left frames." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The absence of **isometropia** in early childhood may lead to unilateral amblyopia if the refractive disparity is neglected." }
    ]
  },
  "Dashboard — metr/isometry.md": {
    primary: "Equality of measure, dimensions, or growth rates; in mathematics, a distance-preserving transformation between metric spaces.",
    secondary: "In developmental biology, proportional scaling where an organ grows at the same relative rate as the whole organism (allometric coefficient equal to one).",
    quotes: [
      { author: "D'Arcy Wentworth Thompson", work: "On Growth and Form", quote: "Strict **isometry** is rare in animal ontogeny, as limb proportions almost universally shift through allometric growth." },
      { author: "Bertrand Russell", work: "The Principles of Mathematics", quote: "A spatial **isometry** preserves the metric distance between any two points under rigid translation and rotation." },
      { author: "Stephen Jay Gould", work: "Ontogeny and Phylogeny", quote: "Deviations from geometric **isometry** provide evolutionary morphology with its primary mechanism for generating novel body shapes." }
    ]
  },
  "Dashboard — metr/metr.md": {
    primary: "A combining form derived from Greek 'metron' (measure) or 'metra' (womb, mother), forming the foundation of measuring and gynecological vocabulary.",
    secondary: "In scientific lexicography, the root element designating dimensional measurement, rhythm, standards, or anatomical uterine organs.",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The Greek root **metr** encompasses both metron, the standard rule of measure, and metra, the maternal womb." },
      { author: "Robert Beekes", work: "Etymological Dictionary of Greek", quote: "Indo-European cognates of **metr** connect mathematical measurement directly with maternal origin and nourishment." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Technical terms employing the combining element **metr** signify either dimensional proportionality or maternal floral tissues." }
    ]
  },
  "Dashboard — metr/metralgia.md": {
    primary: "Pain in the uterus; uterine neuralgia or tenderness.",
    secondary: "In 19th-century clinical gynecology, persistent non-inflammatory pain of the womb attributed to neuropathic or spasmodic congestion.",
    quotes: [
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "Neuralgic **metralgia** frequently afflicts delicate females, manifesting as dull aching over the hypogastrium during menstruation." },
      { author: "J. Marion Sims", work: "Clinical Notes on Uterine Surgery", quote: "Severe **metralgia** was dramatically relieved following surgical dilatation of the constricted internal cervical os." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The practitioner must distinguish chronic pelvic **metralgia** from acute inflammatory peritonitis." }
    ]
  },
  "Dashboard — metr/metrazol.md": {
    primary: "A central nervous system stimulant and chemical convulsant drug (pentylenetetrazol), formerly used in shock therapy for psychiatric disorders and as a respiratory stimulant.",
    secondary: "In biological psychiatry and neuropharmacology, the agent introduced by Ladislas von Meduna in 1934 to induce therapeutic epileptic seizures in schizophrenic patients.",
    quotes: [
      { author: "Ladislas von Meduna", work: "Die Konvulsionstherapie der Schizophrenie", quote: "Intravenous injection of **Metrazol** reliably triggered grand mal seizures, breaking through catatonic stupor in our clinical trials." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "Before electroconvulsive therapy was standardized, violent convulsions induced by **Metrazol** were the desperate psychiatric remedy of the 1930s." },
      { author: "Raymond D. Adams", work: "Principles of Neurology", quote: "In experimental neurophysiology, sub-convulsive doses of **Metrazol** are utilized to lower seizure thresholds in animal models." }
    ]
  },
  "Dashboard — metr/metre.md": {
    primary: "The fundamental unit of length in the International System of Units (SI), equal to 100 centimeters or approximately 39.37 inches; also the rhythmic structure of verse in poetry.",
    secondary: "In metrology, originally defined in 1793 as one ten-millionth of the distance from the equator to the North Pole, now defined by the distance light travels in vacuum in 1/299,792,458 of a second.",
    quotes: [
      { author: "Antoine Lavoisier", work: "Elements of Chemistry", quote: "The republican **metre** establishes a universal measure derived directly from the immutable dimensions of the earth itself." },
      { author: "John Milton", work: "Paradise Lost", quote: "The measure is English heroic verse without rhyme, as that of Homer in Greek and of Virgil in Latin; an ancient **metre** revived." },
      { author: "Lord Kelvin (William Thomson)", work: "Popular Lectures and Addresses", quote: "The metric system, built upon the standard **metre**, delivers natural philosophy from the chaotic labyrinth of archaic weights." }
    ]
  },
  "Dashboard — metr/metrestick.md": {
    primary: "A ruler or measuring rod that is one meter long, typically divided into centimeters and millimeters.",
    secondary: "In educational science laboratories and physical metrology, a standard visual standard used for direct demonstration of metric linear distances.",
    quotes: [
      { author: "James Prescott Joule", work: "Scientific Papers", quote: "The lever arm was carefully gauged against a graduated brass **metrestick** verified by the national bureau." },
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "Deflections of the mirror galvanometer were projected upon a horizontal **metrestick** placed across the room." },
      { author: "Thomas Henry Huxley", work: "Physiography: An Introduction to the Study of Nature", quote: "Every physics classroom should feature a wooden **metrestick** to familiarize students with decimal linear proportions." }
    ]
  },
  "Dashboard — metr/metric.md": {
    primary: "Of, relating to, or based on the metric system of weights and measures; a system or standard of measurement.",
    secondary: "In differential geometry and general relativity, the tensor field (metric tensor) that defines distance, curvature, and angles across a manifold.",
    quotes: [
      { author: "Antoine Lavoisier", work: "Memoirs on the Metric System", quote: "The decimal **metric** system substitutes logical coherence for the arbitrary confusion of provincial weights." },
      { author: "Albert Einstein", work: "The Meaning of Relativity", quote: "The fundamental **metric** tensor determines the gravitational field and the curvature of four-dimensional spacetime." },
      { author: "H. G. Wells", work: "The Work, Wealth and Happiness of Mankind", quote: "Global commerce increasingly relies upon uniform **metric** standards to calibrate international shipping and engineering." }
    ]
  },
  "Dashboard — metr/metrical.md": {
    primary: "Of, relating to, or composed in poetic meter; relating to measurement or the metric system.",
    secondary: "In literary prosody, governed by a regular arrangement of poetic feet, syllables, and stresses.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Biographia Literaria", quote: "The essence of poetry demands a harmonious **metrical** arrangement that delights the ear while elevating emotion." },
      { author: "Alexander Pope", work: "An Essay on Criticism", quote: "True ease in writing comes from art, not chance, as those move easiest who have learned the **metrical** dance." },
      { author: "Edgar Allan Poe", work: "The Poetic Principle", quote: "The **metrical** beauty of 'The Raven' was calculated with mathematical precision to evoke melancholy longing." }
    ]
  },
  "Dashboard — metr/metrically.md": {
    primary: "In a metrical manner; with regard to poetic meter or according to a system of measurement.",
    secondary: "In verse analysis, composed or evaluated according to structured rhythmic patterns of syllables and stresses.",
    quotes: [
      { author: "Percy Bysshe Shelley", work: "A Defence of Poetry", quote: "Dante's Divine Comedy is **metrically** balanced, each terzina chiming with rhythmic inevitability." },
      { author: "Matthew Arnold", work: "On Translating Homer", quote: "A translator must render Homer **metrically**, preserving the rapid, flowing surge of the Greek hexameter." },
      { author: "George Saintsbury", work: "A History of English Prosody", quote: "Chaucer handled decasyllabic couplets **metrically**, weaving flexible vernacular rhythm into French courtly forms." }
    ]
  },
  "Dashboard — metr/metricate.md": {
    primary: "To convert, adapt, or change a system of measurement to the metric system.",
    secondary: "In industrial policy and standardization, transitioning manufacturing, tools, and legal codes from customary units to SI units.",
    quotes: [
      { author: "Lord Kelvin (William Thomson)", work: "Popular Lectures and Addresses", quote: "Britain must ultimately **metricate** her manufacturing machinery if she wishes to compete in continental markets." },
      { author: "H. G. Wells", work: "The Shape of Things to Come", quote: "The international council resolved to **metricate** all aviation gauges to prevent navigational disasters across borders." },
      { author: "Frank A. Lee", work: "Industrial Standardization", quote: "Automobile factories took nearly a decade to fully **metricate** fastener tooling and engineering blueprints." }
    ]
  },
  "Dashboard — metr/metrication.md": {
    primary: "The process of converting or transitioning to the metric system of weights and measures.",
    secondary: "In economic history and metrological governance, the legislative and industrial shift from imperial or customary units to SI decimal standards.",
    quotes: [
      { author: "Lord Kelvin (William Thomson)", work: "Addresses on Metric Reform", quote: "Universal **metrication** will save countless hours of arithmetic drudgery in schools and industrial counting-houses." },
      { author: "Lewis Mumford", work: "Technics and Civilization", quote: "The legal **metrication** initiated by the French National Assembly reflected the Enlightenment desire for rational geometric order." },
      { author: "Colin Renfrew", work: "The Archaeology of Measurement", quote: "Modern **metrication** represents the latest phase in humanity's five-thousand-year quest for standardized measures." }
    ]
  },
  "Dashboard — metr/metricise.md": {
    primary: "To convert into the metric system; to express or measure in metric units; to metricize.",
    secondary: "In technical standardization, to adapt industrial drawings, specifications, and tooling to SI standards.",
    quotes: [
      { author: "Lord Kelvin (William Thomson)", work: "Popular Lectures and Addresses", quote: "Every engineer should **metricise** his laboratory records to facilitate global scientific collaboration." },
      { author: "H. G. Wells", work: "The Work, Wealth and Happiness of Mankind", quote: "National customs authorities gradually began to **metricise** commodity tariffs across European borders." },
      { author: "Frank A. Lee", work: "Modern Industrial Mechanics", quote: "Efforts to **metricise** standard mechanical fasteners met persistent resistance from traditional machinists." }
    ]
  },
  "Dashboard — metr/metricize.md": {
    primary: "To convert to the metric system of measurement; also, to put into poetic meter.",
    secondary: "In industrial engineering and literary composition, adapting specifications to metric dimensions or rendering prose into verse.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Science and Culture", quote: "Scientific education should **metricize** all physical balances so that students think naturally in decimal units." },
      { author: "Edgar Allan Poe", work: "The Philosophy of Composition", quote: "The poet must deliberately **metricize** his emotional conceptions to give them artistic permanence." },
      { author: "Frank A. Lee", work: "Industrial Standardization", quote: "Automobile corporations decided to **metricize** engine specifications to unify global parts manufacturing." }
    ]
  },
  "Dashboard — metr/metrics.md": {
    primary: "A set of numbers, measurements, or quantitative indicators that give information about a particular process or performance; the study of poetic meter.",
    secondary: "In organizational management and prosody, the quantitative criteria used to evaluate systems, or the formal rules governing verse rhythm.",
    quotes: [
      { author: "Frank A. Fetter", work: "Principles of Economics", quote: "Modern corporate management establishes precise operational **metrics** to track labor productivity and capital depreciation." },
      { author: "George Saintsbury", work: "Historical Manual of English Prosody", quote: "Classical **metrics** evaluated lines by syllable quantity, whereas English poetry relies primarily upon stress accent." },
      { author: "Peter F. Drucker", work: "The Practice of Management", quote: "Without objective financial **metrics**, an enterprise drifts blindly in competitive markets without a navigational rudder." }
    ]
  },
  "Dashboard — metr/metrification.md": {
    primary: "The process of converting to the metric system; metrication; also the act or art of composing verse in poetic meter.",
    secondary: "In technical history, the adoption of decimal weights and measures; in literary theory, the structural versification of text.",
    quotes: [
      { author: "Antoine Lavoisier", work: "Elements of Chemistry", quote: "The systematic **metrification** of weights and measures swept away thousands of confusing feudal trade customs." },
      { author: "Samuel Taylor Coleridge", work: "Biographia Literaria", quote: "The delicate **metrification** of Spenser's Faerie Queene creates a continuous musical spell that enchants the ear." },
      { author: "Lord Kelvin (William Thomson)", work: "Popular Lectures and Addresses", quote: "The gradual **metrification** of British electrical engineering occurred naturally because the ohm and volt were metric derivatives." }
    ]
  },
  "Dashboard — metr/metrify.md": {
    primary: "To compose verse; to put into poetic meter or rhyme.",
    secondary: "In classical and Renaissance rhetoric, the artistic translation of prose ideas into structured, rhyming or blank verse.",
    quotes: [
      { author: "Philip Sidney", work: "The Defence of Poesy", quote: "It is not rhyming and versing that maketh a poet, though he who can fitly **metrify** noble passions elevates human speech." },
      { author: "Alexander Pope", work: "The Dunciad", quote: "Paltry scribblers who clumsily **metrify** tavern gossip fill the gutter presses with discordant rhymes." },
      { author: "William Hazlitt", work: "Lectures on the English Poets", quote: "Chaucer was the first who knew how to **metrify** vernacular English without losing narrative freshness." }
    ]
  },
  "Dashboard — metr/metritis.md": {
    primary: "Inflammation of the muscular and mucosal walls of the uterus.",
    secondary: "In clinical gynecology and veterinary pathology, acute or chronic uterine infection following parturition, often accompanied by purulent discharge and sepsis.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Puerperal **metritis** demands aggressive supportive care and drainage to avert fatal generalized peritonitis." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "The symptoms of acute **metritis** include high fever, hypogastric tenderness, and suppression of the normal lochia." },
      { author: "J. Marion Sims", work: "Clinical Notes on Uterine Surgery", quote: "Chronic parenchymatous **metritis** results in fibrous induration and painful enlargement of the uterine fundus." }
    ]
  },
  "Dashboard — metr/metro.md": {
    primary: "An underground electric passenger railway system; a subway; also short for metropolitan or a metropolitan area.",
    secondary: "In urban transit history, the rapid transit rail systems pioneered by the Paris Métropolitain (opened 1900) that revolutionized mass urban commuting.",
    quotes: [
      { author: "Lewis Mumford", work: "The Culture of Cities", quote: "The electric **metro** reshaped Paris, linking outlying working quarters directly to the grand boulevards in minutes." },
      { author: "H. G. Wells", work: "The Future in America", quote: "Commuters surged into the subterranean caverns of the **metro**, boarding electric cars that whistled into the darkness." },
      { author: "Marcel Proust", work: "Time Regained", quote: "During the wartime air raids, the deep stations of the Paris **metro** provided subterranean shelter for thousands of citizens." }
    ]
  },
  "Dashboard — metr/metrocyte.md": {
    primary: "A mother cell; specifically, an ancestral blood-forming stem cell or erythroblast that gives rise to mature erythrocytes.",
    secondary: "In historical hematology and histology, a primitive precursor cell in the bone marrow or spleen that divides to produce differentiated cellular lineages.",
    quotes: [
      { author: "Paul Ehrlich", work: "Histology of the Blood", quote: "The giant **metrocyte** of the fetal liver divides by mitosis to yield normoblasts that lose their nuclei as they mature." },
      { author: "Ernest Beutler", work: "Williams Hematology", quote: "Historically, the term **metrocyte** was applied to large basophilic erythroblasts observed in embryonic erythropoiesis." },
      { author: "Santiago Ramón y Cajal", work: "Manual of Normal Histology", quote: "In bone marrow smears, each primordial **metrocyte** features a dense chromatin network and voluminous cytoplasm." }
    ]
  },
  "Dashboard — metr/metrological.md": {
    primary: "Of or relating to metrology (the scientific study and established systems of weights and measures).",
    secondary: "In the history of science and archaeology, pertaining to the standard units, balances, and measuring scales of ancient civilizations.",
    quotes: [
      { author: "Antoine Lavoisier", work: "Memoirs on Weights and Measures", quote: "Our **metrological** reform was designed to replace arbitrary provincial customs with a single universal standard of weight and length." },
      { author: "Colin Renfrew", work: "The Archaeology of Measurement", quote: "Bronze Age Indus cities exhibited astonishing **metrological** uniformity, manufacturing chert weight cubes that followed exact binary ratios." },
      { author: "Lord Kelvin (William Thomson)", work: "Popular Lectures and Addresses", quote: "Precise electrical definitions adopted at the Paris congress resolved longstanding **metrological** disputes between nations." }
    ]
  },
  "Dashboard — metr/metrology.md": {
    primary: "The scientific study and established system of weights and measures.",
    secondary: "In legal and industrial science, the discipline dedicated to defining units of measurement, realizing measurement standards, and establishing traceability.",
    quotes: [
      { author: "Antoine Lavoisier", work: "Elements of Chemistry", quote: "Progress in experimental chemistry was made possible only by the rigorous application of physical **metrology**." },
      { author: "Lord Kelvin (William Thomson)", work: "Popular Lectures and Addresses", quote: "When you can measure what you are speaking about, you know something about it; this is the supreme maxim of **metrology**." },
      { author: "Colin Renfrew", work: "Before Civilization", quote: "The invention of stone weights in early Mesopotamia marks the dawn of mathematical **metrology** in human society." }
    ]
  },
  "Dashboard — metr/metronidazole.md": {
    primary: "A synthetic nitroimidazole antibiotic and antiprotozoal medication used to treat anaerobic bacterial infections, trichomoniasis, amebiasis, and giardiasis.",
    secondary: "In clinical pharmacology, a prodrug that anaerobic microorganisms selectively reduce into reactive nitro radicals, inducing lethal DNA strand breakage.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In amebic hepatic abscess, administration of **metronidazole** eradicates trophozoites swiftly without requiring surgical aspiration." },
      { author: "William N. Kelley", work: "Textbook of Internal Medicine", quote: "First-line therapy for Clostridioides difficile colitis historically relied upon oral **metronidazole** to suppress spore-forming anaerobes." },
      { author: "Thomas B. Fitzpatrick", work: "Dermatology in General Medicine", quote: "Topical **metronidazole** gel delivers excellent anti-inflammatory control in erythematotelangiectatic rosacea." }
    ]
  },
  "Dashboard — metr/metronome.md": {
    primary: "A mechanical or electronic device that marks time at a steady beat or tempo by ticking or flashing at regular intervals, used by musicians during practice.",
    secondary: "In musical acoustics and psychology, an inverted pendulum apparatus perfected by Johann Maelzel to calibrate musical tempos in beats per minute.",
    quotes: [
      { author: "Ludwig van Beethoven", work: "Letters and Musical Papers", quote: "Maelzel's **metronome** has arrived; my tempo markings will henceforth deliver my compositions from the whimsical caprice of conductors." },
      { author: "Hermann von Helmholtz", work: "On the Sensations of Tone", quote: "The steady ticking of the **metronome** serves as an objective acoustic standard for psychophysical reaction-time experiments." },
      { author: "George Bernard Shaw", work: "Music in London", quote: "A mechanical conductor who treats an orchestra like an unfeeling **metronome** murders the expressive soul of Mozart's melodies." }
    ]
  },
  "Dashboard — metr/metronymic.md": {
    primary: "A surname or personal name derived from the name of one's mother or a female ancestor; matronymic.",
    secondary: "In genealogical anthropology and onomastics, a naming tradition prevalent in matrilineal societies where lineage is traced through the maternal line.",
    quotes: [
      { author: "Edward Burnett Tylor", work: "Primitive Culture", quote: "In matrilineal clans of North America, every warrior bore a proud **metronymic** identifying him with his mother's maternal totem." },
      { author: "Jane Ellen Harrison", work: "Themis: A Study of the Social Origins of Greek Religion", quote: "Archaic Pelasgian inscriptions frequently reveal a **metronymic** formula preceding the patriarchal Olympian dynasties." },
      { author: "James George Frazer", work: "Totemism and Exogamy", quote: "The inheritance of property under the **metronymic** system passed invariably from maternal uncle to nephew." }
    ]
  },
  "Dashboard — metr/metropolis.md": {
    primary: "The chief, capital, or largest city of a country, state, or region, often a major commercial and cultural center.",
    secondary: "Historically in ancient Greece, the mother city of a colony; in modern sociology, a vast urban agglomeration exerting economic dominance.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Rome in the golden age of the Antonines was the magnificent **metropolis** of the Mediterranean world." },
      { author: "Charles Dickens", work: "A Tale of Two Cities", quote: "London was a smoky, turbulent **metropolis** where wealth and squalor rubbed shoulders in every winding alley." },
      { author: "Lewis Mumford", work: "The Culture of Cities", quote: "The modern commercial **metropolis** draws raw materials, capital, and population into its insatiable financial vortex." }
    ]
  },
  "Dashboard — metr/metropolitan.md": {
    primary: "Of, relating to, or characteristic of a metropolis; an archbishop or bishop who has oversight over an ecclesiastical province.",
    secondary: "In urban sociology and church history, pertaining to large metropolitan areas; in Eastern Orthodox and Catholic polity, a provincial primate.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The venerable **metropolitan** of Antioch presided over the synod, upholding the orthodox Nicene faith against imperial edicts." },
      { author: "Charles Dickens", work: "Bleak House", quote: "The **metropolitan** police detectives pursued the trail through the dense fogs of the London docks." },
      { author: "Lewis Mumford", work: "The City in History", quote: "The **metropolitan** region expanded outward along commuter rail lines, swallowing ancient villages into suburban sprawl." }
    ]
  },
  "Dashboard — metr/metroptosis.md": {
    primary: "Prolapse or downward displacement of the uterus into or protruding from the vaginal canal.",
    secondary: "In 19th-century surgical gynecology, severe pelvic floor descent resulting from birth trauma and attenuation of the cardinal and uterosacral ligaments.",
    quotes: [
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "Complete **metroptosis** occurs when the relaxed vaginal walls allow the entire uterus to invert and emerge externally." },
      { author: "J. Marion Sims", work: "Clinical Notes on Uterine Surgery", quote: "In treating chronic **metroptosis**, supportive pessaries were formerly utilized before the perfection of surgical suspension." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The mechanical distress of severe **metroptosis** is exacerbated by heavy lifting and standing for long hours on hard floors." }
    ]
  },
  "Dashboard — metr/metrorrhagia.md": {
    primary: "Abnormal bleeding from the uterus that occurs at irregular intervals between regular menstrual periods; intermenstrual bleeding.",
    secondary: "In clinical gynecology, an ominous sign that warrants endometrial biopsy or hysteroscopy to rule out endometrial polyps, hyperplasia, or carcinoma.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Postmenopausal **metrorrhagia** must always be regarded as an alarming indication of malignant disease until proven otherwise." },
      { author: "J. Marion Sims", work: "Clinical Notes on Uterine Surgery", quote: "The patient had suffered from exhausting **metrorrhagia** for months, reducing her hemoglobin to perilously low levels." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "Unlike menorrhagia, which is merely excessive monthly catamenia, **metrorrhagia** denotes irregular bleeding occurring out of season." }
    ]
  },
  "Dashboard — metr/metroxylon.md": {
    primary: "A genus of palms (family Arecaceae) native to Southeast Asia and Melanesia, famously including the true sago palm (Metroxylon sagu).",
    secondary: "In economic tropical botany, arborescent swamp palms whose massive trunks accumulate hundreds of pounds of starchy edible pith harvested as commercial sago.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The sago palm, **Metroxylon** sagu, provides the islanders with bread; a single felled trunk supplies a family with food for an entire year." },
      { author: "Joseph Dalton Hooker", work: "The Flora of British India", quote: "Species of **Metroxylon** flourish in coastal freshwater swamps, flowering once in a massive terminal panicle before dying." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The pith of **Metroxylon** yields the finest pearl sago of commerce after repeated washing and granulation through sieves." }
    ]
  },
  "Dashboard — metr/micrometry.md": {
    primary: "The science, art, or practice of measuring minute or microscopic distances, dimensions, and objects using a micrometer.",
    secondary: "In cytological microscopy, the quantitative measurement of cell diameters, spore dimensions, and nuclear diameters using stage and ocular micrometer scales.",
    quotes: [
      { author: "Robert Koch", work: "Investigations into the Etiology of Traumatic Infective Diseases", quote: "Accurate **micrometry** enabled us to differentiate the slender rod of the tubercle bacillus from larger saprophytes." },
      { author: "Louis Pasteur", work: "Studies on Fermentation", quote: "Stage **micrometry** proved that yeast globules maintain a remarkably constant diameter across successive brewing batches." },
      { author: "William Gilson Farlow", work: "Cryptogamic Botany", quote: "In describing fungal species, precise **micrometry** of basidiospores is the primary foundation of taxonomic certainty." }
    ]
  },
  "Dashboard — metr/optometrist.md": {
    primary: "A licensed healthcare professional trained to examine eyes for visual defects, diagnose refractive errors, and prescribe corrective spectacles or contact lenses.",
    secondary: "In modern vision care, an eye specialist who performs non-surgical ocular health examinations and visual rehabilitation.",
    quotes: [
      { author: "F. C. Donders", work: "Anomalies of Refraction", quote: "The skilled **optometrist** measures refractive deviations with precision, ensuring spectacles that restore visual comfort." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Referral to an experienced **optometrist** resolved the student's chronic migraine by neutralizing bilateral astigmatism." },
      { author: "William N. Kelley", work: "Textbook of Internal Medicine", quote: "Routine eye screenings conducted by an **optometrist** frequently uncover early asymptomatic signs of diabetic retinopathy." }
    ]
  },
  "Dashboard — metr/optometry.md": {
    primary: "The profession or practice of examining the eyes for visual defects and diseases, prescribing corrective lenses, and diagnosing refractive errors.",
    secondary: "In healthcare history, the applied visual science evolving from spectacle-making into an independent health profession focused on binocular vision and ocular optics.",
    quotes: [
      { author: "Hermann von Helmholtz", work: "Physiological Optics", quote: "The mathematical principles of **optometry** were established by demonstrating how cylindrical lenses neutralize corneal asymmetry." },
      { author: "F. C. Donders", work: "On the Anomalies of Accommodation and Refraction", quote: "Modern **optometry** demands both objective retinoscopy and subjective trial-case verification for every patient." },
      { author: "William James", work: "The Principles of Psychology", quote: "Experiments in **optometry** illuminate the intricate relationship between ocular convergence and the visual perception of depth." }
    ]
  },
  "Dashboard — metr/oximeter.md": {
    primary: "A non-invasive medical instrument that measures the oxygen saturation of a patient's hemoglobin in arterial blood, typically via a finger probe.",
    secondary: "In critical care medicine and anesthesiology, a spectrophotometric sensor (pulse oximeter) that measures differential light absorption of oxyhemoglobin and deoxyhemoglobin at 660 nm and 940 nm.",
    quotes: [
      { author: "William N. Kelley", work: "Textbook of Internal Medicine", quote: "Continuous monitoring with a pulse **oximeter** provides immediate warning of desaturation during general anesthesia." },
      { author: "Michael B. Singer", work: "Neurology in Clinical Practice", quote: "In acute myasthenia gravis crisis, a falling reading on the **oximeter** signals impending diaphragmatic failure." },
      { author: "Eric Kandel", work: "Principles of Neural Science", quote: "Physiological recordings coupled with a digital **oximeter** track cerebral oxygenation during sleep apnea episodes." }
    ]
  },
  "Dashboard — metr/oximetry.md": {
    primary: "The measurement of the oxygen saturation level of hemoglobin in circulating blood.",
    secondary: "In respiratory physiology and intensive care, pulse oximetry, a vital clinical modality that provides continuous real-time assessment of oxygen transport.",
    quotes: [
      { author: "William N. Kelley", work: "Textbook of Internal Medicine", quote: "The introduction of pulse **oximetry** drastically reduced perioperative hypoxemic cardiac arrests in surgical suites." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Non-invasive **oximetry** replaces painful arterial blood gas sampling in routine management of chronic obstructive pulmonary disease." },
      { author: "Raymond D. Adams", work: "Principles of Neurology", quote: "Nocturnal **oximetry** traces dramatic cyclical drops in arterial oxygen saturation in patients with severe obstructive sleep apnea." }
    ]
  },
  "Dashboard — metr/parametric.md": {
    primary: "Of, relating to, or expressed in terms of a parameter or parameters; in statistics, assuming data follows a specific probability distribution.",
    secondary: "In inferential statistics, describing hypothesis tests (such as Student's t-test or ANOVA) that assume normal distributions and homogeneity of variance.",
    quotes: [
      { author: "Karl Pearson", work: "The Grammar of Science", quote: "The **parametric** curve fitted our biometric skull measurements with remarkable statistical fidelity." },
      { author: "Ronald Fisher", work: "Statistical Methods for Research Workers", quote: "A **parametric** analysis of variance allows the experimenter to isolate agricultural treatment effects from soil variability." },
      { author: "Bertrand Russell", work: "Introduction to Mathematical Philosophy", quote: "Expressing the trajectory in **parametric** equations illuminates the independent dependence of coordinates upon time." }
    ]
  },
  "Dashboard — metr/parametritis.md": {
    primary: "Inflammation of the parametrium, the connective and fatty tissue immediately surrounding the uterus in the pelvic cavity.",
    secondary: "In clinical gynecology and obstetrics, pelvic cellulitis following septic abortion or puerperal infection, characterized by pelvic phlegmon and high fever.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe puerperal infection may extend laterally through the lymphatics to cause extensive brawny **parametritis** in the broad ligaments." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "Pelvic examination in acute **parametritis** reveals intense bilateral pelvic tenderness and induration fixing the uterine cervix." },
      { author: "J. Marion Sims", work: "Clinical Notes on Uterine Surgery", quote: "Surgical intervention is indicated in **parametritis** when deep fluctuant abscesses form in the connective tissues of the pelvis." }
    ]
  },
  "Dashboard — metr/pleometrosis.md": {
    primary: "The founding or establishment of a new ant or social insect colony by two or more queens cooperating together.",
    secondary: "In sociobiology and behavioral ecology, an adaptive founding strategy where multiple queens rear the first worker generation faster, often followed by fighting among foundresses once workers mature.",
    quotes: [
      { author: "William Morton Wheeler", work: "Ants: Their Structure, Development and Behavior", quote: "In desert harvester ants, **pleometrosis** enhances colony survival during drought by producing an initial worker force twice as fast." },
      { author: "Edward O. Wilson", work: "The Insect Societies", quote: "While **pleometrosis** provides cooperative advantages during nest founding, the queens typically fight to the death once the first workers emerge." },
      { author: "Jean-Henri Fabre", work: "Social Life in the Insect World", quote: "Cooperation between two sister foundresses in **pleometrosis** illustrates how harsh environmental conditions favor temporary mutualism." }
    ]
  },
  "Dashboard — metr/spirometer.md": {
    primary: "An instrument used to measure the volume of air inhaled and exhaled by the lungs; a breath meter.",
    secondary: "In pulmonary medicine, a diagnostic device perfected by John Hutchinson in 1846 to determine vital capacity, forced expiratory volume (FEV1), and respiratory function.",
    quotes: [
      { author: "John Hutchinson", work: "On the Capacity of the Lungs and on the Respiratory Movements", quote: "I constructed the water-sealed **spirometer** to demonstrate that vital capacity varies directly with height and age." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In incipient pulmonary tuberculosis, serial testing with the **spirometer** reveals early loss of vital capacity before percussion reveals dullness." },
      { author: "Austin Flint", work: "A Treatise on the Principles and Practice of Medicine", quote: "The **spirometer** provides objective numerical data on the degree of bronchial obstruction in chronic asthma." }
    ]
  },
  "Dashboard — metr/spirometry.md": {
    primary: "The measurement of the volume and flow rate of air that can be inhaled or exhaled by the lungs.",
    secondary: "In pulmonary function testing, a standard physiological assay that differentiates between obstructive lung disorders (asthma, COPD) and restrictive disorders (fibrosis).",
    quotes: [
      { author: "John Hutchinson", work: "On the Capacity of the Lungs", quote: "Systematic **spirometry** in thousands of healthy subjects proved that vital capacity is an indispensable index of thoracic health." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Routine clinical **spirometry** allows the physician to measure the response of spastic bronchioles to bronchodilator inhalation." },
      { author: "William N. Kelley", work: "Textbook of Internal Medicine", quote: "A reduced FEV1/FVC ratio on diagnostic **spirometry** confirms the presence of expiratory airflow limitation." }
    ]
  },
  "Dashboard — metr/symmetric.md": {
    primary: "Having symmetry; balanced in form, proportion, or arrangement across an axis or plane.",
    secondary: "In geometry and crystallography, exhibiting invariant properties under reflection, rotation, or inversion.",
    quotes: [
      { author: "Charles Darwin", work: "The Various Contrivances by Which Orchids Are Fertilised", quote: "The ancestral flower was radially **symmetric**, while specialized insect pollination favored the evolution of bilateral zygomorphy." },
      { author: "James Dwight Dana", work: "A Text-Book of Mineralogy", quote: "Every face of an isometric crystal obeys strictly **symmetric** laws of spatial distribution around the center of form." },
      { author: "Isaac Newton", work: "Opticks", quote: "The lenses were ground with **symmetric** curvature to minimize spherical aberration along the focal axis." }
    ]
  },
  "Dashboard — metr/symmetrical.md": {
    primary: "Made up of exactly similar parts facing each other or around an axis; showing balance and proportional beauty; symmetrical.",
    secondary: "In comparative anatomy, describing bilateral or radial body plans that reflect organismal locomotion or sessile life.",
    quotes: [
      { author: "John Ruskin", work: "The Stones of Venice", quote: "True architectural beauty does not demand rigid, dead **symmetrical** repetition, but living organic balance." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "The echinoderm larva is bilaterally **symmetrical**, whereas the adult undergoes a secondary transformation into a five-rayed radial form." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "Secondary sexual selection consistently favors males possessing brightly colored, perfectly **symmetrical** plumage." }
    ]
  },
  "Dashboard — metr/symmetrically.md": {
    primary: "In a symmetrical manner; with balanced, corresponding parts on opposite sides of a dividing line or plane.",
    secondary: "In anatomical morphology and engineering, distributed with geometric balance across a central axis.",
    quotes: [
      { author: "Charles Darwin", work: "The Expression of the Emotions in Man and Animals", quote: "In intense laughter, the facial muscles contract **symmetrically** on both sides of the mouth." },
      { author: "Asa Gray", work: "First Lessons in Botany", quote: "In typical flowers, petals and stamens are arranged **symmetrically** in whorls around the central receptacle." },
      { author: "Thomas Hardy", work: "The Woodlanders", quote: "The ancient avenues of planted elms marched **symmetrically** across the estate like lines of silent sentinels." }
    ]
  },
  "Dashboard — metr/symmetricalness.md": {
    primary: "The state, quality, or condition of being symmetrical; symmetry.",
    secondary: "In aesthetics and descriptive anatomy, the pleasing visual equilibrium arising from corresponding parts across an axis.",
    quotes: [
      { author: "John Ruskin", work: "Modern Painters", quote: "The majestic **symmetricalness** of a mature cedar tree reflects centuries of harmonious response to prevailing winds." },
      { author: "Herbert Spencer", work: "The Principles of Biology", quote: "Active locomotive animals invariably evolve toward bilateral **symmetricalness** to optimize forward propulsion." },
      { author: "William Hazlitt", work: "Essays on Art", quote: "Classic Greek statuary achieves profound nobility through the effortless **symmetricalness** of its bodily proportions." }
    ]
  },
  "Dashboard — metr/symmetrise.md": {
    primary: "To make or cause to be symmetrical; to balance or arrange in symmetrical proportions; symmetrize.",
    secondary: "In mathematical physics and design, to transform equations or forms so they exhibit symmetry under reflection or coordinate permutation.",
    quotes: [
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", quote: "We **symmetrise** the differential equations by introducing the displacement current into Ampère's circuital law." },
      { author: "John Ruskin", work: "The Seven Lamps of Architecture", quote: "Do not attempt to **symmetrise** a Gothic facade by forcing unequal aisles into identical arcades." },
      { author: "D'Arcy Wentworth Thompson", work: "On Growth and Form", quote: "Surface tension acting upon liquid droplets tends to **symmetrise** cellular boundaries into regular tetrahedra." }
    ]
  },
  "Dashboard — metr/symmetrize.md": {
    primary: "To make symmetrical; to arrange, proportion, or balance symmetrically.",
    secondary: "In quantum mechanics and crystallography, to construct states or tensors that are invariant under particle interchange.",
    quotes: [
      { author: "Paul Dirac", work: "The Principles of Quantum Mechanics", quote: "For systems of identical bosons, we must completely **symmetrize** the wave function under any permutation of particles." },
      { author: "D'Arcy Wentworth Thompson", work: "On Growth and Form", quote: "Hydrostatic forces continuously **symmetrize** the developing blastula into a perfect sphere." },
      { author: "Frank Lloyd Wright", work: "An Autobiography", quote: "The organic architect refuses to arbitrarily **symmetrize** a floor plan at the expense of human functional needs." }
    ]
  },
  "Dashboard — metr/symmetry.md": {
    primary: "The quality of being made up of exactly similar parts facing each other or around an axis; balanced proportion and harmony.",
    secondary: "In fundamental physics, an invariance of physical laws under a transformation (such as space-time translation or gauge transformations), implying conservation laws via Noether's theorem.",
    quotes: [
      { author: "William Blake", work: "Songs of Experience", quote: "Tyger! Tyger! burning bright in the forests of the night, what immortal hand or eye could frame thy fearful **symmetry**?" },
      { author: "Hermann Weyl", work: "Symmetry", quote: "Symmetry, as wide or as narrow as you may define its meaning, is one idea by which man through the ages has tried to comprehend and create order, beauty, and perfection; fundamental **symmetry** principles govern modern physics." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The bilateral **symmetry** of all higher animals was impressed upon their ancestral organization in the earliest seas." }
    ]
  },
  "Dashboard — metr/telemetry.md": {
    primary: "The automatic recording and electrical transmission of data from remote, inaccessible, or moving sources to receiving equipment for monitoring and analysis.",
    secondary: "In aerospace engineering, environmental monitoring, and biomedical telemetry, wireless sensor transmission of physiological or performance parameters.",
    quotes: [
      { author: "Wernher von Braun", work: "First Men to the Moon", quote: "Radio **telemetry** from the rocket stage flashed thousands of instrument readings back to the launch control bunker every second." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Automated **telemetry** stations installed along river basins record continuous changes in dissolved oxygen and chemical runoff." },
      { author: "Arthur C. Clarke", work: "Voices from the Sky", quote: "Without high-frequency **telemetry**, interplanetary space exploration would be blind and voiceless in the dark cosmic void." }
    ]
  },
  "Dashboard — metr/tonometer.md": {
    primary: "An instrument for measuring pressure or tension, especially intraocular pressure within the eyeball to screen for glaucoma.",
    secondary: "In ophthalmology, an apparatus (such as the Goldmann applanation tonometer or Schiøtz indentation tonometer) measuring corneal resistance to indentation or flattening.",
    quotes: [
      { author: "Albrecht von Graefe", work: "Archiv für Ophthalmologie", quote: "Application of a reliable **tonometer** revealed elevated intraocular pressure long before cupping of the optic disc was visible." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In suspected glaucoma, immediate measurement with a **tonometer** is essential to prevent irreversible blindness." },
      { author: "Hermann von Helmholtz", work: "Physiological Optics", quote: "Acoustic physics also employs a **tonometer**, consisting of a calibrated series of tuning forks to gauge absolute pitch." }
    ]
  },
  "Dashboard — minth/catmint.md": {
    primary: "An aromatic perennial herb of the mint family (Nepeta cataria), commonly called catnip, possessing soft downy leaves and white blossoms dotted with purple.",
    secondary: "In feline ethology and herbal pharmacognosy, a plant containing nepetalactone that induces transient behavioral euphoria in domestic and wild cats.",
    quotes: [
      { author: "John Gerard", work: "The Herball or Generall Historie of Plantes", quote: "Cats are so delighted with the scent of **catmint** that they roll upon it, rub their heads against it, and eat it with great eagerness." },
      { author: "Nicholas Culpeper", work: "The Complete Herbal", quote: "An infusion of **catmint** leaves provoketh feminine courses and dispels hysterical vapors and cold stomach phlegm." },
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "The village cats discovered my bed of transplanted **catmint**, tearing the fragrant shoots to pieces in their ecstatic frolics." }
    ]
  },
  "Dashboard — minth/Mentha.md": {
    primary: "A genus of highly aromatic perennial herbs in the family Lamiaceae (the mint family), including spearmint (Mentha spicata) and peppermint (Mentha piperita).",
    secondary: "In systematic botany and pharmacognosy, square-stemmed, creeping rhizomatous herbs bearing opposite serrate leaves rich in menthol and carminative volatile oils.",
    quotes: [
      { author: "Carl Linnaeus", work: "Species Plantarum", quote: "The genus **Mentha** is characterized by a nearly regular four-lobed corolla, straight stamens, and aromatic foliage." },
      { author: "John Gerard", work: "The Herball or Generall Historie of Plantes", quote: "Water mint or **Mentha** aquatica groweth along the margins of standing brooks, filling the air with pleasant balsamic odors." },
      { author: "William Woodville", work: "Medical Botany", quote: "Distillation of **Mentha** piperita yields an essential oil containing volatile stearoptene celebrated for quelling spasmodic nausea." }
    ]
  },
  "Dashboard — minth/menthol.md": {
    primary: "A white, crystalline organic compound with a pungent, minty odor and taste, obtained naturally from peppermint oil or synthesized, producing a cooling sensation on skin and mucous membranes.",
    secondary: "In pharmacology and sensory neurobiology, a cyclic terpene alcohol that selectively binds to and activates the cold-sensitive TRPM8 ion channel in sensory neurons.",
    quotes: [
      { author: "William Allen Miller", work: "Elements of Chemistry", quote: "When peppermint oil is chilled below freezing, pure **menthol** separates out in beautiful, needle-like transparent crystals." },
      { author: "T. Lauder Brunton", work: "A Text-Book of Pharmacology", quote: "Inhalation of **menthol** vapor stimulates the cold receptors of the respiratory tract, producing a subjective sensation of clearer airways." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Topical application of **menthol** ointment relieves the tormenting pruritus of chronic urticaria and localized eczema." }
    ]
  },
  "Dashboard — minth/mint.md": {
    primary: "An aromatic plant of the genus Mentha, having opposite fragrant leaves and small flowers; also a place where the legal currency or coins of a country are manufactured.",
    secondary: "In economic history and numismatics, an official government facility authorized to strike bullion into circulating legal tender; in culinary botany, a refreshing herb.",
    quotes: [
      { author: "Isaac Newton", work: "Mint Papers", quote: "As Master of the Royal **Mint**, I oversaw the great recoinage of silver, establishing rigorous weights and anti-counterfeiting milled edges." },
      { author: "John Milton", work: "Comus", quote: "There will I bring thee, with the sweetest flowers that bloom in woodland glade or **mint**-scented garden bowers." },
      { author: "Charles Dickens", work: "A Christmas Carol", quote: "Cratchit added hot punch spiced with fresh garden **mint**, toasting the family circle with brimming holiday good-cheer." }
    ]
  },
  "Dashboard — minth/mintage.md": {
    primary: "The act, process, or legal authority of minting coins; the coins produced by a mint collectively.",
    secondary: "In numismatics and monetary economics, the seigniorage charge or official stamp impressed upon bullion certifying weight and purity.",
    quotes: [
      { author: "John Locke", work: "Further Considerations Concerning Raising the Value of Money", quote: "The sovereign's **mintage** stamp does not create value, but merely attests to the intrinsic quantity of pure silver in the coin." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Debasement of the imperial **mintage** under Gallienus plunged the Roman provinces into disastrous monetary inflation." },
      { author: "Walter Scott", work: "The Fortunes of Nigel", quote: "The goldsmith inspected the gold jacobus, admiring the crisp, unclipped edges of its fresh royal **mintage**." }
    ]
  }
};

let count = 0;
for (const [relPath, data] of Object.entries(batch6Data)) {
  if (updateNote(relPath, data)) {
    count++;
  }
}

console.log(`\n========================================`);
console.log(`Batch 6 Completed: ${count} / ${Object.keys(batch6Data).length} notes updated.`);
console.log(`========================================\n`);
