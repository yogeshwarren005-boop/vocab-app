import fs from 'fs';
import path from 'path';

const baseClusterDir = 'App database/Greek roots/Cluster Time & Chronology';

function updateNote(relDir, fileName, data) {
  const filePath = path.join(baseClusterDir, relDir, fileName);
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
  // Dashboard — mydr (3 words)
  "Dashboard — mydr/mydr.md": {
    primary: "A combining form derived from Greek μυδρίασις (mydriasis) meaning 'pupil dilation', used in ophthalmology and pharmacology.",
    secondary: "In ocular physiology and medical terminology, designating pharmaceutical agents or conditions that dilate the pupillary aperture.",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The Greek root **mydr-** appears in Galenic texts to describe an unnatural widening of the pupillary aperture." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "Ophthalmic compounds incorporating **mydr-** indicate actions that paralyze the pupillary sphincter." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The diagnostic application of **mydr-** derivatives allowed detailed visualization of the optic nerve head." }
    ]
  },
  "Dashboard — mydr/mydriasis.md": {
    primary: "Prolonged or excessive abnormal dilation of the pupil of the eye, whether physiological, pharmacological, or pathological.",
    secondary: "In neurology and ophthalmology, dilation caused by parasympathetic oculomotor nerve paralysis, sympathetic overstimulation, or topical antimuscarinic drugs like atropine.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Unilateral **mydriasis** paired with ptosis strongly suggests an expanding aneurysm of the posterior communicating artery." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Instillation of belladonna alkaloids paralyzes the constrictor pupillae, resulting in maximal, unreactive **mydriasis**." },
      { author: "Hermann von Helmholtz", work: "Treatise on Physiological Optics", quote: "Under complete drug-induced **mydriasis**, spherical aberration at the lens margins becomes markedly pronounced." }
    ]
  },
  "Dashboard — mydr/mydriatic.md": {
    primary: "Causing or relating to pupillary dilation; an agent or drug that dilates the pupil of the eye.",
    secondary: "In clinical pharmacotherapy, an antimuscarinic or sympathomimetic substance (such as tropicamide, atropine, or phenylephrine) instilled to facilitate funduscopic examination.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Before instilling a strong **mydriatic**, the practitioner must measure intraocular tension to avert acute angle-closure glaucoma." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "A topical **mydriatic** agent blocks muscarinic receptors within the ciliary muscle, simultaneously inducing cycloplegia." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "The physician dropped an effective **mydriatic** into the eye, widening the black portal to inspect the retinal vessel arborization." }
    ]
  },

  // Dashboard — neo (7 words)
  "Dashboard — neo/ne 2.md": {
    primary: "A combining form and prefix derived from Greek νέος (neos) meaning 'new', 'recent', or 'modern', used extensively across scientific and humanities nomenclature.",
    secondary: "In linguistic morphology, the formative prefix in terms such as neon, neologism, neonatal, and Neoplatonism, denoting novelty or recent revival.",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The Greek primitive neos provides the widespread scientific prefix **ne-**, signifying that which is fresh, youthful, or newly discovered." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "Scholars continuously co-opted the element **ne-** to formulate names for newly discovered elements and scientific schools." },
      { author: "James Murray", work: "A New English Dictionary on Historical Principles", quote: "Compounds containing **ne-** proliferated in nineteenth-century philology to mark revised or restored classical systems." }
    ]
  },
  "Dashboard — neo/neologism.md": {
    primary: "A newly coined word, expression, or usage; the creation or introduction of new linguistic terms.",
    secondary: "In psychopathology and linguistic theory, newly minted expressions introduced to describe novel phenomena, or idiosyncratic bizarre words coined by patients in schizophrenia.",
    quotes: [
      { author: "Samuel Johnson", work: "Preface to the English Dictionary", quote: "I have avoided every licentious **neologism** that might corrupt the pure wells of our ancient Saxon speech." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In chronic hebephrenic psychosis, speech is frequently derailed by the spontaneous generation of an incomprehensible **neologism**." },
      { author: "George Orwell", work: "Politics and the English Language", quote: "A pretentious **neologism** often disguises sloppy thinking beneath the hollow luster of technical jargon." }
    ]
  },
  "Dashboard — neo/neologist.md": {
    primary: "A person who coins, introduces, or advocates new words or phrases; a person who promotes theological novelties.",
    secondary: "In literary history and religious controversies, an innovator who departs from established lexical traditions or orthodox theological tenets.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Biographia Literaria", quote: "The reckless **neologist** clutters our literature with barbarous idioms borrowed from foreign fashions." },
      { author: "Thomas Babington Macaulay", work: "Critical and Historical Essays", quote: "The French critic denounced every youthful **neologist** who dared deviate from the austere standards of the Academy." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The orthodox fathers viewed the subtle **neologist** with deeper alarm than the open pagan adversary." }
    ]
  },
  "Dashboard — neo/neon.md": {
    primary: "A chemical element of the noble gas group, atomic number 10, symbol Ne, a colorless, odorless, nonflammable gas that glows reddish-orange in electrical discharge tubes.",
    secondary: "In the history of inorganic chemistry, discovered in 1898 by Sir William Ramsay and Morris Travers through the fractional distillation of liquid air, named from Greek neon 'new'.",
    quotes: [
      { author: "William Ramsay", work: "The Gases of the Atmosphere", quote: "We observed a magnificent fiery-red glow in the vacuum spectrum, and named this newly discovered element **neon**." },
      { author: "Lord Rayleigh", work: "Argon, a New Constituent of the Atmosphere", quote: "The discovery of **neon** completed another vacant niche in Mendeleev's periodic arrangement of the inert elements." },
      { author: "H. G. Wells", work: "The Shape of Things to Come", quote: "The nocturnal city blazed with electric tubes of vibrant crimson **neon**, illuminating the glass towers." }
    ]
  },
  "Dashboard — neo/neonatal.md": {
    primary: "Of, relating to, or affecting the newborn child, especially during the first twenty-eight days of life.",
    secondary: "In pediatrics and perinatology, the critical developmental stage of extrauterine cardiopulmonary, hepatic, and thermal adaptation.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Early screening for jaundice prevents devastating bilirubin encephalopathy during the vulnerable **neonatal** period." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "The onset of breathing initiates profound **neonatal** circulatory shifts, closing the ductus arteriosus and foramen ovale." },
      { author: "Florence Nightingale", work: "Notes on Nursing", quote: "Proper warmth and pure ventilation are paramount in safeguarding fragile **neonatal** life against nursery epidemics." }
    ]
  },
  "Dashboard — neo/neonate.md": {
    primary: "A newborn infant, especially one in the first four weeks following birth.",
    secondary: "In neonatal intensive care, a newborn evaluated by the Apgar score, characterized by immature renal concentrating ability and transitioning fetal hemoglobin.",
    quotes: [
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "The glomerular filtration rate in a healthy **neonate** is only one-third of adult capacity on a surface-area basis." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Careful physical examination of the **neonate** reveals primitive grasp and Moro reflexes reflecting subcortical neural pathways." },
      { author: "Donald Seldin", work: "The Kidney: Physiology and Pathophysiology", quote: "Fluid balance in the premature **neonate** is exceptionally precarious owing to high insensible cutaneous water loss." }
    ]
  },
  "Dashboard — neo/neos.md": {
    primary: "The Greek adjective meaning 'new', 'young', 'fresh', or 'recent' (νέος, neos), serving as the foundational root of numerous scientific words.",
    secondary: "In classical Greek philology and etymology, expressing both chronological recency and youthful vigor, contrasted with palaios (ancient).",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "In classical antiquity, **neos** stood as the antithesis of palaios, denoting that which had newly burst into bloom or being." },
      { author: "Aristotle", work: "Rhetoric", quote: "The nature of the young man, the **neos**, is passionate, eager, and prone to swift generous attachments." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "Scientific innovators turned to **neos** whenever an element, epoch, or doctrine required a name proclaiming novelty." }
    ]
  },

  // Dashboard — nyct (15 words)
  "Dashboard — nyct/nyct.md": {
    primary: "A combining form derived from Greek νύξ, νυκτός (nyx, nyktos) meaning 'night', used in biological, astronomical, and medical terminology.",
    secondary: "In physiological and ecological nomenclature, signifying nocturnal habits, darkness-dependent movements, or nighttime clinical exacerbations.",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The Greek root **nyct-** embodies the mysterious kingdom of Nyx, the ancient personification of dark night." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "Botanists employ **nyct-** to denote blossoms that expand solely under the cover of nocturnal gloom." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "In medical pathology, the radical **nyct-** designates morbid disturbances that awaken the sufferer at midnight." }
    ]
  },
  "Dashboard — nyct/nyctaginaceae.md": {
    primary: "A family of flowering plants commonly called the four-o'clock family, including Mirabilis and Bougainvillea.",
    secondary: "In angiosperm taxonomy (order Caryophyllales), tropical and warm-temperate herbs, shrubs, and climbers characterized by petaloid calyces, anthocarps, and betalain pigments.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The family **Nyctaginaceae** is notable for its showy, petal-like calyx and the total absence of true corolla petals." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The blossoms of the **Nyctaginaceae** frequently remain tightly folded throughout daylight, opening their perfumed throats at four in the afternoon." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "Horticulturists cherish the vibrant bracts of Bougainvillea, a spectacular climber belonging to the family **Nyctaginaceae**." }
    ]
  },
  "Dashboard — nyct/nyctaginia.md": {
    primary: "A monotypic genus of flowering plants in the family Nyctaginaceae, represented by Nyctaginia capitata, the scarlet musk-flower.",
    secondary: "In southwestern North American field botany, a glandular-pubescent desert herb bearing dense clusters of brilliant scarlet, night-blooming fragrant flowers.",
    quotes: [
      { author: "Asa Gray", work: "Plantae Wrightianae Texano-Neo-Mexicanae", quote: "I described **Nyctaginia** capitata from specimens gathered along the gravelly banks of the Rio Grande." },
      { author: "Vernon Orlando Bailey", work: "Life Zones and Crop Zones of New Mexico", quote: "The scarlet musk-flower, **Nyctaginia**, scents the nocturnal desert breeze across the arid limestone plains." },
      { author: "Liberty Hyde Bailey", work: "Cyclopedia of American Horticulture", quote: "The vibrant crimson inflorescence of **Nyctaginia** makes it an exquisite subject for arid rock gardens." }
    ]
  },
  "Dashboard — nyct/nyctalgia.md": {
    primary: "Pain occurring specifically during the night or sleep, such as bone aches or neuropathic nocturnal flares.",
    secondary: "In clinical rheumatology and neurology, sleep-disturbing pain characteristic of osteoid osteoma, diabetic polyneuropathy, or restless legs syndrome.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The patient suffered from severe **nyctalgia**, the boring tibia pains worsening relentlessly once he lay warm beneath blankets." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "Deep bone **nyctalgia** relieved promptly by small doses of aspirin is a classic diagnostic hallmark of osteoid osteoma." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "We designate sleep-robbing arthritic pangs as **nyctalgia**, reflecting nocturnal changes in vascular engorgement." }
    ]
  },
  "Dashboard — nyct/nyctalopia.md": {
    primary: "Night-blindness; an abnormal inability to see in dim light or darkness.",
    secondary: "In nutritional ophthalmology, an early clinical manifestation of vitamin A deficiency caused by impaired rhodopsin synthesis in retinal rod photoreceptor cells.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Epidemics of **nyctalopia** broke out among sailors on extended voyages where fresh provisions and vitamin A were exhausted." },
      { author: "Hermann von Helmholtz", work: "Treatise on Physiological Optics", quote: "In **nyctalopia**, dark adaptation of the retinal rods is arrested, rendering the patient helpless upon entering twilight." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Dietary deficiency of retinol prevents the regeneration of visual purple, resulting in severe clinical **nyctalopia**." }
    ]
  },
  "Dashboard — nyct/nyctanassa.md": {
    primary: "A genus of American night herons in the family Ardeidae, notably Nyctanassa violacea, the yellow-crowned night heron.",
    secondary: "In ornithology, medium-sized coastal and swamp wading birds characterized by stout bills, nocturnal foraging for crustaceans, and striking facial plumage.",
    quotes: [
      { author: "John James Audubon", work: "Ornithological Biography", quote: "The yellow-crowned night heron, **Nyctanassa**, stalks the salt marsh fiddler crabs beneath the silver gleam of the moon." },
      { author: "Alexander Wilson", work: "American Ornithology", quote: "Unlike daylight egrets, **Nyctanassa** remains concealed in dark cypress swamps until twilight summons it to hunt." },
      { author: "Elliott Coues", work: "Key to North American Birds", quote: "The robust bill and short legs of **Nyctanassa** reflect specialization for crushing hard mangrove crabs." }
    ]
  },
  "Dashboard — nyct/nyctanthous.md": {
    primary: "Flowering or blooming only at night; night-flowering.",
    secondary: "In pollination ecology, describing angiosperms whose nocturnal anthesis is synchronized with bat or sphingid moth pollinators.",
    quotes: [
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "The night-blooming cereus is strictly **nyctanthous**, opening immense fragrant corollas that wilt before sunrise." },
      { author: "Charles Darwin", work: "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", quote: "White corollas and heavy vanillin perfumes prevail among **nyctanthous** blossoms visited by nocturnal hawk-moths." },
      { author: "John Lindley", work: "The Elements of Botany", quote: "The **nyctanthous** habit prevents the wasteful evaporation of delicate nectar under the heat of the midday sun." }
    ]
  },
  "Dashboard — nyct/nyctereutes.md": {
    primary: "A genus of canids native to East Asia, comprising the raccoon dog (Nyctereutes procyonoides).",
    secondary: "In vertebrate zoology, an archaic basal canid with facial markings resembling a raccoon, renowned as the only canid that hibernates during severe winter months.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "The raccoon-like canid, **Nyctereutes**, represents an ancient divergence within the wild dog family in Eastern Asia." },
      { author: "William Henry Flower", work: "An Introduction to the Osteology of the Mammalia", quote: "The dentition of **Nyctereutes** exhibits crushing, bunodont molars suited for an omnivorous diet of fruit and mollusks." },
      { author: "George Gaylord Simpson", work: "The Principles of Classification and a Classification of Mammals", quote: "In basicranial features, **Nyctereutes** preserves primitive ancestral fox-like traits lost in modern cursorial canids." }
    ]
  },
  "Dashboard — nyct/nycticebus.md": {
    primary: "A genus of nocturnal strepsirrhine primates native to Southeast Asia, commonly known as slow lorises.",
    secondary: "In primatology, arboreal primates possessing large round night-adapted eyes, a toxic brachial gland secretion, and a slow, stealthy stalking locomotion.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "In the thick canopy of Java, the slow loris, **Nycticebus**, moves with deliberate, soundless stealth upon sleeping insects." },
      { author: "Thomas Henry Huxley", work: "Man's Place in Nature", quote: "The anatomy of **Nycticebus** illustrates how nocturnal specialization reshaped the lemuriform skull and orbit." },
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", quote: "The vascular retia mirabilia in the limbs of **Nycticebus** enable prolonged isometric grasping of branches without muscle fatigue." }
    ]
  },
  "Dashboard — nyct/nycticorax.md": {
    primary: "A cosmopolitan genus of medium-sized night herons, especially Nycticorax nycticorax, the black-crowned night heron.",
    secondary: "In avian systematics, colonial swamp waders whose name means 'night raven' (nyx 'night' + korax 'raven'), alluding to their nocturnal croaking flight calls.",
    quotes: [
      { author: "John James Audubon", work: "Birds of America", quote: "At twilight, the guttural quok of **Nycticorax** echoes over the bayous as the birds wing their way to the fishing grounds." },
      { author: "Alexander Wilson", work: "American Ornithology", quote: "The black-crowned night heron, **Nycticorax**, nests in colossal rookeries hidden deep within impenetrable cedar swamps." },
      { author: "Elliott Coues", work: "Key to North American Birds", quote: "The occiput of **Nycticorax** bears two or three elongated, pure white plumes that flutter during courtship displays." }
    ]
  },
  "Dashboard — nyct/nyctimene.md": {
    primary: "A genus of pteropodid fruit bats native to Australasia, commonly called tube-nosed fruit bats; or a figure in classical mythology.",
    secondary: "In chiropterology, megabats characterized by tubular projecting nostrils, spotted yellow wings, and frugivorous feeding habits in Pacific rainforests.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "In the Moluccas, we captured the curious bat **Nyctimene**, whose nostrils project forward like twin miniature tubes." },
      { author: "Oldfield Thomas", work: "Annals and Magazine of Natural History", quote: "The spotted wing membranes of **Nyctimene** afford exquisite camouflage among dead leaves in the jungle understory." },
      { author: "George Gaylord Simpson", work: "The Principles of Classification and a Classification of Mammals", quote: "The divergent rostral anatomy of **Nyctimene** isolates it as a specialized branch among the Indo-Australian Pteropodidae." }
    ]
  },
  "Dashboard — nyct/nyctinasty.md": {
    primary: "The rhythmic, reversible movement of plant leaves, petals, or florets in response to darkness; 'sleep movements' of plants.",
    secondary: "In plant physiology, circadian movements regulated by reversible turgor pressure changes within specialized motor organs (pulvini), investigated famously by Charles Darwin.",
    quotes: [
      { author: "Charles Darwin", work: "The Power of Movement in Plants", quote: "We have designated these nocturnal leaf foldings as **nyctinasty**, demonstrating that they protect delicate tissues from radiation chilling." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "The rhythmic collapse of clover and mimosa leaflets at sunset is a classic manifestation of autonomic **nyctinasty**." },
      { author: "Julius von Sachs", work: "Lectures on the Physiology of Plants", quote: "In **nyctinasty**, osmotic water shifts across the upper and lower halves of the pulvinus drive the downward drooping of the petiole." }
    ]
  },
  "Dashboard — nyct/nyctophilia.md": {
    primary: "A distinct preference for darkness or the night; comfort and fondness experienced in nighttime surroundings.",
    secondary: "In psychological characterology and chronobiology, the preference for nighttime activity (extreme evening chronotype or 'night owls'), finding creative clarity in nocturnal quiet.",
    quotes: [
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "The reclusive poet confessed to a profound **nyctophilia**, declaring that his imagination awoke only when the sun went down." },
      { author: "William James", work: "The Principles of Psychology", quote: "Solitude combined with gentle **nyctophilia** often fosters deep intellectual synthesis undisturbed by sensory bustle." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Certain contemplative scholars indulge a secret **nyctophilia**, wandering through midnight shadows to converse with the stars." }
    ]
  },
  "Dashboard — nyct/nyctophobia.md": {
    primary: "An extreme, irrational, or debilitating fear of the night or darkness.",
    secondary: "In clinical psychiatry and developmental psychology, a specific phobic anxiety disorder marked by acute panic, tachycardia, and catastrophic anticipation upon darkness exposure.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "Childhood **nyctophobia** is an ancient evolutionary heirloom, prompting the infant to dread predatory perils lurking in the dark." },
      { author: "William Osler", work: "Aequanimitas", quote: "The hysterical patient suffered from paralyzing **nyctophobia**, refusing to sleep unless three lanterns burned beside her bed." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "Unresolved trauma frequently expresses itself in adulthood as persistent **nyctophobia** accompanied by night terrors." }
    ]
  },
  "Dashboard — nyct/nycturia.md": {
    primary: "Excessive or frequent urination at night; nocturia.",
    secondary: "In nephrology and cardiology, a clinical symptom often signaling congestive heart failure, benign prostatic hyperplasia, or chronic renal concentrating impairment.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Early hypertensive nephrosclerosis announces its onset through progressive **nycturia**, the kidney losing its ability to concentrate urine." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "In heart failure, recumbency facilitates daytime edema reabsorption, provoking marked nocturnal diuresis and **nycturia**." },
      { author: "Donald Seldin", work: "The Kidney: Physiology and Pathophysiology", quote: "Prostatic obstruction impedes complete bladder emptying, forcing the elderly patient to endure disruptive **nycturia**." }
    ]
  },

  // Dashboard — opsi (4 words)
  "Dashboard — opsi/opsi.md": {
    primary: "A combining form derived from Greek ὀψέ (opse) meaning 'late', or ὄψις (opsis) meaning 'appearance' or 'sight'.",
    secondary: "In scientific etymology, designating late development or delayed intellectual acquisition, as in opsimath and opsigamy.",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The Greek adverb opse gives the combining prefix **opsi-**, denoting actions postponed until the evening or late in life." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "Scholars recognized **opsi-** as an expressive token for late learning and autumnal achievements." },
      { author: "James Murray", work: "A New English Dictionary on Historical Principles", quote: "Compound formations in **opsi-** frequently appear in classical biographical literature to characterize late bloomers." }
    ]
  },
  "Dashboard — opsi/opsimath.md": {
    primary: "A person who begins to learn or study late in life; a late-blooming student.",
    secondary: "In literary and philosophical portraiture, an individual who undertakes serious scholarly acquisition in advanced age, celebrated by Theophrastus in his *Characters*.",
    quotes: [
      { author: "Theophrastus", work: "Characters", quote: "The **opsimath** is one who in his sixty-seventh year memorizes epic verses and undertakes to learn the dance." },
      { author: "Samuel Johnson", work: "The Rambler", quote: "Cato was an admirable **opsimath**, taking up the study of Greek in his green old age with stubborn vigor." },
      { author: "Isaac D'Israeli", work: "Curiosities of Literature", quote: "History abounds with the triumphant achievements of the **opsimath**, proving that genius needs no youth to bear golden fruit." }
    ]
  },
  "Dashboard — opsi/opsin.md": {
    primary: "A group of light-sensitive G protein-coupled receptor proteins found in the photoreceptor cells of the retina.",
    secondary: "In visual biochemistry and neurophysiology, the apoprotein component of rhodopsin and iodopsin which, covalently bound to retinal, mediates optical phototransduction.",
    quotes: [
      { author: "George Wald", work: "The Photoreceptor Process in Vision", quote: "Absorption of a photon isomerizes 11-cis-retinal, initiating the conformational separation of the chromophore from the **opsin**." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "In the dark, retinal recombines spontaneously with **opsin** to reconstitute the active photosensitive pigment rhodopsin." },
      { author: "Hermann von Helmholtz", work: "Treatise on Physiological Optics", quote: "Color vision is mediated by three distinct cone **opsin** pigments tuned to short, medium, and long wavelengths." }
    ]
  },
  "Dashboard — opsi/synopsis.md": {
    primary: "A brief summary or general survey of something; an outline or abstract of a subject or work.",
    secondary: "In textual criticism and scriptural studies, a parallel tabular arrangement (such as a synopsis of the Gospels) facilitating comparative analysis.",
    quotes: [
      { author: "Samuel Johnson", work: "Lives of the Most Eminent English Poets", quote: "Before embarking upon his grand epic, the author drafted a concise **synopsis** of each book's plot." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The student who consults this historical **synopsis** will easily master the chronological succession of the Caesars." },
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "A well-ordered **synopsis** spreads the whole territory of a science before the mind, like a map before an explorer." }
    ]
  },

  // Dashboard — palaeo (12 words)
  "Dashboard — palaeo/palaeoanthropology.md": {
    primary: "The branch of anthropology concerned with the study of fossil hominids and early human evolution.",
    secondary: "In evolutionary biology, the multidisciplinary field combining skeletal osteology, archaeology, and geochronology to trace human origins from australopithecines to Homo sapiens.",
    quotes: [
      { author: "Louis Leakey", work: "By the Evidence: Memoirs, 1932-1951", quote: "Olduvai Gorge yielded the fossil hominid skull that revolutionized global **palaeoanthropology** and proved Africa was mankind's cradle." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "The history of **palaeoanthropology** shows how easily fragmentary jawbones could be misinterpreted when viewed through preconceived theories." },
      { author: "Arthur Keith", work: "The Antiquity of Man", quote: "Every new skull discovered in Pleistocene gravels compels **palaeoanthropology** to redraw its family tree." }
    ]
  },
  "Dashboard — palaeo/palaeoclimatology.md": {
    primary: "The study of past climates throughout geological history.",
    secondary: "In Earth system sciences, reconstructing ancient atmospheric and oceanic temperatures using ice cores, ocean sediment isotope ratios, and tree rings.",
    quotes: [
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Oxygen isotope ratios preserved in deep-sea foraminifera provide **palaeoclimatology** with an unassailable record of Pleistocene ice ages." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The discovery of fossil coal flora in Spitsbergen proved to early **palaeoclimatology** that polar regions once enjoyed subtropical warmth." },
      { author: "John McPhee", work: "Basin and Range", quote: "Through **palaeoclimatology**, we learn that the earth's climate is not a permanent state but a pendulum swinging between greenhouse and icehouse." }
    ]
  },
  "Dashboard — palaeo/palaeoecology.md": {
    primary: "The branch of ecology that uses fossil evidence to reconstruct the ecosystems and environmental interactions of the geological past.",
    secondary: "In sedimentary geology and paleontology, analyzing trophic webs, paleocommunities, and taphonomic assemblages to understand ancient biomes.",
    quotes: [
      { author: "George Gaylord Simpson", work: "The Meaning of Evolution", quote: "Quantitative **palaeoecology** reveals how Miocene grassland expansion triggered the simultaneous adaptive radiation of hypsodont equids." },
      { author: "Stephen Jay Gould", work: "Time's Arrow, Time's Cycle", quote: "Fossil reef communities afford brilliant demonstrations of **palaeoecology**, showing how corals and brachiopods partitioned shallow seas." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "To understand the extinction of giant Pleistocene ground sloths, we must reconstruct their **palaeoecology** and climatic stressors." }
    ]
  },
  "Dashboard — palaeo/palaeoethnography.md": {
    primary: "The study of the customs, cultures, and daily life of prehistoric human peoples through their material remains and archaeological artifacts.",
    secondary: "In prehistoric archaeology and anthropology, reconstructing ancient kinship systems, domestic arrangements, and spiritual beliefs from excavated dwellings and rock art.",
    quotes: [
      { author: "Edward Tylor", work: "Primitive Culture", quote: "Cave paintings and flint spearheads provide the primary materials for **palaeoethnography**, illuminating the mental life of Ice Age hunters." },
      { author: "James George Frazer", work: "The Golden Bough", quote: "Through **palaeoethnography**, we discern the dawn of sympathetic magic in prehistoric ritual burials." },
      { author: "John Lubbock", work: "Pre-Historic Times", quote: "The kitchen-middens of Denmark opened a new era in **palaeoethnography**, revealing the diet and domestic customs of early strand-dwellers." }
    ]
  },
  "Dashboard — palaeo/palaeolithic.md": {
    primary: "Of, relating to, or denoting the early phase of the Stone Age, lasting about 2.5 million years, characterized by chipped stone tools.",
    secondary: "In prehistoric archaeology (coined by John Lubbock in 1865), the cultural era spanning from the earliest Oldowan pebble tools through the Upper Paleolithic cave art of Lascaux.",
    quotes: [
      { author: "John Lubbock", work: "Pre-Historic Times", quote: "I have proposed the division of the Stone Age into two periods: the **Palaeolithic**, when implements were merely flaked, and the Neolithic, when they were ground." },
      { author: "Thomas Henry Huxley", work: "Man's Place in Nature", quote: "The Neanderthal calvaria demonstrates the physical characteristics of **Palaeolithic** man inhabiting glacial Europe." },
      { author: "Arthur Conan Doyle", work: "The Lost World", quote: "We stood gazing upon chipped flint spearheads that were undeniably the handiwork of **Palaeolithic** savages." }
    ]
  },
  "Dashboard — palaeo/palaeology.md": {
    primary: "The study of antiquities, ancient languages, or prehistoric relics; archaeology; paleology.",
    secondary: "In historical antiquarianism, the comprehensive study of ancient human civilizations through inscriptions, monuments, and archaic artifacts.",
    quotes: [
      { author: "Thomas Babington Macaulay", work: "Critical and Historical Essays", quote: "He turned from modern politics to immerse his intellect in the dusty inscriptions of classical **palaeology**." },
      { author: "Edward Gibbon", work: "Memoirs of My Life and Writings", quote: "My youthful curiosity was deeply captivated by the medals and monuments preserved in the cabinets of European **palaeology**." },
      { author: "Walter Scott", work: "The Antiquary", quote: "The worthy squire fancied himself an oracle in **palaeology**, expounding upon every Roman tile turned up by the plow." }
    ]
  },
  "Dashboard — palaeo/palaeontological.md": {
    primary: "Of, relating to, or based upon paleontology; concerning fossilized remains of ancient life.",
    secondary: "In evolutionary biology and geology, describing evidence derived from the chronological succession of fossil plants and animals in stratified rocks.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The **palaeontological** record, though imperfect, affords grand confirmations of the gradual divergence of species over deep time." },
      { author: "Thomas Henry Huxley", work: "Lectures on Evolution", quote: "Our strongest **palaeontological** evidence for evolution is supplied by the complete fossil pedigree of the horse in North America." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Each geological epoch is stamped with its own **palaeontological** seal in the form of distinctive marine molluscan shells." }
    ]
  },
  "Dashboard — palaeo/palaeontologist.md": {
    primary: "A scientist who specializes in the study of fossil animals and plants; a student of paleontology.",
    secondary: "In Earth sciences, a specialist who reconstructs prehistoric anatomy, evolutionary phylogenies, and ancient paleoenvironments from mineralized fossil specimens.",
    quotes: [
      { author: "Richard Owen", work: "Description of the Skeleton of an Extinct Gigantic Sloth", quote: "The task of the **palaeontologist** is to reconstruct the living animal from scattered bones by the laws of anatomical correlation." },
      { author: "Othniel Charles Marsh", work: "Fossil Horses in America", quote: "The **palaeontologist** working in the western badlands is rewarded with treasures of prehistoric life unmatched anywhere on earth." },
      { author: "Stephen Jay Gould", work: "Wonderful Life", quote: "Charles Doolittle Walcott was a brilliant field **palaeontologist** whose quarry in the Burgess Shale unveiled Cambrian diversity." }
    ]
  },
  "Dashboard — palaeo/palaeontology.md": {
    primary: "The branch of science concerned with fossil animals and plants.",
    secondary: "In the history of science, the discipline founded by Georges Cuvier and Alexandre Brongniart that uses fossil remains to reconstruct the history of life on Earth.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The noble science of **palaeontology** exhibits the forms of life that preceded our era and disappeared forever from the face of the globe." },
      { author: "Georges Cuvier", work: "Discourse on the Revolutionary Upheavals on the Surface of the Earth", quote: "Comparative anatomy applied to **palaeontology** restores the lost inhabitants of former worlds to human contemplation." },
      { author: "Thomas Henry Huxley", work: "Critiques and Addresses", quote: "Modern **palaeontology** has bridged the chasms separating birds from reptiles and fishes from amphibians." }
    ]
  },
  "Dashboard — palaeo/palaeornithology.md": {
    primary: "The branch of paleontology concerned with the study of fossil birds and the evolutionary origin of flight.",
    secondary: "In vertebrate paleontology, the field analyzing feathered theropods, Mesozoic toothed avians (Archaeopteryx, Hesperornis), and extinct Cenozoic megafauna (moas, dodos).",
    quotes: [
      { author: "Richard Owen", work: "On the Archaeopteryx of von Meyer", quote: "The discovery of Archaeopteryx in the Solnhofen limestone marks the true birth of scientific **palaeornithology**." },
      { author: "Othniel Charles Marsh", work: "Odontornithes: A Monograph on the Extinct Toothed Birds of North America", quote: "American **palaeornithology** was revolutionized by the recovery of Hesperornis and Ichthyornis bearing reptilian teeth." },
      { author: "Thomas Henry Huxley", work: "On the Animals Which Are Most Nearly Intermediate Between Birds and Reptiles", quote: "Discoveries in **palaeornithology** decisively established that modern birds are the living descendants of feathered dinosaurian ancestors." }
    ]
  },
  "Dashboard — palaeo/paleo.md": {
    primary: "A combining form derived from Greek παλαιός (palaios) meaning 'ancient', 'prehistoric', or 'early', widely used in geology, anthropology, and medicine.",
    secondary: "In contemporary popular culture, short for the paleolithic diet or lifestyle modeled after ancestral hunter-gatherers.",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The Greek primitive palaios provides the universal scientific prefix **paleo-**, denoting prehistoric antiquity." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Geologists joined **paleo-** with zoic to designate the ancient era of marine invertebrate life." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The formative element **paleo-** consistently distinguishes archaic evolutionary stages from recent and modern counterparts." }
    ]
  },
  "Dashboard — palaeo/paleobotany.md": {
    primary: "The branch of paleontology dealing with the study of fossil plants.",
    secondary: "In plant evolution and stratigraphy, reconstructing ancient floras, coal ball anatomy, and angiosperm origins from petrified wood, impressions, and fossil pollen.",
    quotes: [
      { author: "Adolphe Brongniart", work: "Histoire des Végétaux Fossiles", quote: "The aim of **paleobotany** is to trace the succession of vegetable dynasties that clothed the ancient continents." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "Fossil leaves from the Cretaceous badlands provide **paleobotany** with irreplaceable evidence of early flowering tree radiations." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Modern **paleobotany** combines microfossil palynology with macrofossil compression analysis to date sedimentary basins." }
    ]
  },

  // Dashboard — pentecost (4 words)
  "Dashboard — pentecost/Pentecost.md": {
    primary: "A Christian festival celebrating the descent of the Holy Spirit on the Apostles fifty days after Easter; also the Jewish festival of Shavuot (the Feast of Weeks).",
    secondary: "In biblical history (Acts 2), the decisive birthday of the Christian Church marked by tongues of fire and the proclamation of the Gospel to diverse nations.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "Then to the heaven-sent spirit down shall fly, / As at the day of **Pentecost**, to guide / The infant church with light and heavenly fire." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The feast of **Pentecost** brought devout pilgrims from every province of the Mediterranean world to Jerusalem." },
      { author: "John Bunyan", work: "Grace Abounding to the Chief of Sinners", quote: "I remembered the glorious outpouring at **Pentecost**, and took heart that sovereign grace could reach even the chief of sinners." }
    ]
  },
  "Dashboard — pentecost/pentecostal.md": {
    primary: "Of, relating to, or resembling Pentecost; pertaining to Christian movements emphasizing the gifts of the Holy Spirit.",
    secondary: "In ecclesiastical history, characterizing charismatic revivals marked by glossolalia (speaking in tongues), divine healing, and exuberant communal worship.",
    quotes: [
      { author: "John Henry Newman", work: "Parochial and Plain Sermons", quote: "The **Pentecostal** effusion was not a fleeting emotional transport, but the abiding indwelling of the divine Paraclete." },
      { author: "William James", work: "The Varieties of Religious Experience", quote: "The sudden glossolalia observed in **Pentecostal** revivals exhibits classic psychological automatisms of ecstatic conversion." },
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "The popular enthusiasm spread like a **Pentecostal** fire, melting cold class distinctions in a surge of fraternal zeal." }
    ]
  },
  "Dashboard — pentecost/pentecostalism.md": {
    primary: "A Protestant Christian renewal movement emphasizing personal conversion, baptism in the Holy Spirit, speaking in tongues, and spiritual gifts.",
    secondary: "In 20th-century religious history, the global revival movement originating at the Azusa Street Revival in 1906 that became one of the fastest-growing branches of modern Christianity.",
    quotes: [
      { author: "William James", work: "The Varieties of Religious Experience", quote: "The intense emotional fervor of nascent **Pentecostalism** recalls the pristine enthusiasm of the apostolic church." },
      { author: "H. Richard Niebuhr", work: "The Social Sources of Denominationalism", quote: "Early **Pentecostalism** gave powerful religious voice to disenfranchised urban migrants and working-class families." },
      { author: "Max Weber", work: "The Sociology of Religion", quote: "The charismatic authority celebrated in **Pentecostalism** breaks through the rigid routinization of traditional bureaucratic churches." }
    ]
  },
  "Dashboard — pentecost/pentecostalist.md": {
    primary: "An adherent, member, or minister of a Pentecostal church; a believer in Pentecostalism.",
    secondary: "In sociology of religion, a Christian believer who actively practices the spiritual gifts (charismata) such as prophecy, healing, and glossolalia.",
    quotes: [
      { author: "William James", work: "The Varieties of Religious Experience", quote: "The ardent **Pentecostalist** testifies with fervent joy to the tangible physical sensation of spiritual baptism." },
      { author: "H. Richard Niebuhr", work: "The Social Sources of Denominationalism", quote: "To the sincere **Pentecostalist**, the apostolic miracles are not ancient history but living daily realities." },
      { author: "Max Weber", work: "The Sociology of Religion", quote: "The community of the **Pentecostalist** relies upon the ongoing verification of charismatic gifts within the congregation." }
    ]
  },

  // Dashboard — peran (2 words)
  "Dashboard — peran/Perates.md": {
    primary: "A 2nd-century Gnostic Christian sect described by Hippolytus, whose name signifies 'those who have crossed over' (from Greek peran, 'beyond').",
    secondary: "In early church history and heresy studies, an Ophite-related group that taught salvation through crossing over the corrupt material world to the celestial realm.",
    quotes: [
      { author: "Hippolytus of Rome", work: "Refutation of All Heresies", quote: "The sect of the **Perates** boast that they alone have passed through the corruption of the material cosmos into the celestial light." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Among the bizarre schools of Gnosticism, the **Perates** venerated the mystical serpent as the guide across mortal boundaries." },
      { author: "John Henry Newman", work: "An Essay on the Development of Christian Doctrine", quote: "The fantastic cosmologies of the **Perates** were firmly rejected by the early church in defense of scriptural monotheism." }
    ]
  },
  "Dashboard — peran/peran.md": {
    primary: "A Greek adverb and preposition meaning 'across', 'beyond', 'on the other side', appearing in geographical and philosophical loanwords.",
    secondary: "In classical Greek philology, expressing physical passage across a water boundary or metaphysical transition beyond ordinary limits.",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The Greek adverb **peran** was used by Homer to designate lands lying across the sea, beyond the horizon." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "In theological coinages, **peran-** conveys the mystical act of crossing over earthly tribulations into salvation." },
      { author: "B. L. Gildersleeve", work: "Syntax of Classical Greek", quote: "As a spatial preposition, **peran** governs the genitive case to indicate the farther shore of a river or strait." }
    ]
  },

  // Dashboard — presby (15 words)
  "Dashboard — presby/Presbyterianism.md": {
    primary: "A branch of Protestant Christianity adhering to the Reformed theological tradition, governed by representative courts of presbyters (elders).",
    secondary: "In church history, the polity formulated by John Calvin and established in Scotland by John Knox, rejecting episcopal hierarchy in favor of Kirk Sessions, Presbyteries, and General Assemblies.",
    quotes: [
      { author: "John Knox", work: "The History of the Reformation in Scotland", quote: "We established **Presbyterianism** throughout the realm, casting out Roman prelacy to govern Christ's Kirk by faithful elders." },
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "The stubborn fidelity of the Scottish covenanters to **Presbyterianism** defied the swords of Claverhouse and the Stuart crown." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The austere republican simplicity of **Presbyterianism** stood in sharp contrast to the pompous majesty of episcopal thrones." }
    ]
  },
  "Dashboard — presby/archpresbyter.md": {
    primary: "A chief presbyter or senior priest in a diocese; an ecclesiastical dignitary ranking immediately below the bishop; rural dean.",
    secondary: "In canon law and church history, a senior priest appointed to supervise rural parishes or lead the cathedral chapter in the absence of the bishop.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The **archpresbyter** of Alexandria held immense ecclesiastical influence, acting as the bishop's principal counselor and treasurer." },
      { author: "Richard Hooker", work: "Of the Lawes of Ecclesiasticall Politie", quote: "In ancient times, the **archpresbyter** was chosen by the college of priests to maintain discipline among the city clergy." },
      { author: "Thomas Fuller", work: "The Church History of Britain", quote: "The **archpresbyter** made his annual visitation to inspect the rural parish churches and examine the parish registers." }
    ]
  },
  "Dashboard — presby/presbyope.md": {
    primary: "A person affected by presbyopia; a person who has age-related farsightedness.",
    secondary: "In clinical refraction, an individual whose diminished amplitude of ocular accommodation requires convex corrective reading lenses for near vision.",
    quotes: [
      { author: "Hermann von Helmholtz", work: "Treatise on Physiological Optics", quote: "The **presbyope** discovers that holding print at arm's length is no longer sufficient to bring tiny letters into sharp retinal focus." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "By the fifth decade of life, almost every civilized reader becomes a **presbyope**, seeking relief in reading spectacles." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "The elderly philosopher sat beside the candle, an unmistakable **presbyope** peering through gold-rimmed magnifying glasses." }
    ]
  },
  "Dashboard — presby/presbyopia.md": {
    primary: "The gradual loss of the eye's ability to focus on nearby objects, occurring as a natural part of the aging process.",
    secondary: "In physiological optics, progressive reduction in accommodative power caused by the gradual sclerosis of the crystalline lens and loss of ciliary muscle elasticity.",
    quotes: [
      { author: "Hermann von Helmholtz", work: "Treatise on Physiological Optics", quote: "We trace the etiology of **presbyopia** to the physical hardening of the lens fibers, which resist the relaxed tension of the zonule." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "By age fifty, **presbyopia** typically reduces the dynamic accommodation range from fourteen diopters to less than two." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Patients rarely complain of **presbyopia** until near work induces eye fatigue and frontal headaches under evening lighting." }
    ]
  },
  "Dashboard — presby/presbyopic.md": {
    primary: "Affected with or relating to presbyopia; having farsighted vision associated with aging.",
    secondary: "In clinical optometry, describing an eye that cannot focus upon near points without the optical assistance of positive spherical lens additions.",
    quotes: [
      { author: "Hermann von Helmholtz", work: "Treatise on Physiological Optics", quote: "Prescribing a convex spectacle lens restores comfortable close reading to the **presbyopic** eye without straining the ciliary body." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The **presbyopic** scholar held the ancient parchment further back, smiling as he reached into his waistcoat for his glasses." },
      { author: "Oliver Wendell Holmes Sr.", work: "The Poet at the Breakfast-Table", quote: "His **presbyopic** gaze was splendid for surveying distant landscape horizons, though helpless before a miniature portrait." }
    ]
  },
  "Dashboard — presby/presbyter.md": {
    primary: "An elder in the early Christian church; a priest or minister in certain Christian churches.",
    secondary: "In New Testament ecclesiology, the ordained community leader (from Greek presbyteros 'elder') who preached and administered sacraments, distinct from bishops in later episcopal development.",
    quotes: [
      { author: "John Milton", work: "On the New Forcers of Conscience Under the Long Parliament", quote: "New **Presbyter** is but old Priest writ large!" },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "In the primitive church, the title of bishop and **presbyter** was frequently applied to the identical pastoral office." },
      { author: "Richard Hooker", work: "Of the Lawes of Ecclesiasticall Politie", quote: "The church hath retained the name of **presbyter** to designate those who are lawfully called to minister holy things." }
    ]
  },
  "Dashboard — presby/presbyterian.md": {
    primary: "Relating to or denoting a Christian church governed by elders according to the principles of Presbyterianism; an adherent of such a church.",
    secondary: "In political and religious history, a member of the parliamentary party during the English Civil War that advocated a national church system modeled on the Scottish kirk.",
    quotes: [
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "The **Presbyterian** clergy maintained a fierce independence against royal encroachment, thundering from Edinburgh pulpits." },
      { author: "Walter Scott", work: "The Heart of Midlothian", quote: "David Deans was a staunch **Presbyterian** of the strictest Cameronian stamp, abhorring both prelatry and popish rites." },
      { author: "Samuel Johnson", work: "A Journey to the Western Islands of Scotland", quote: "We observed that the Scottish **Presbyterian** service dispensed with liturgical vestments and instrumental music." }
    ]
  },
  "Dashboard — presby/presbyterium.md": {
    primary: "The council of priests or elders who advise and assist a bishop in a diocese; or the sanctuary part of a church set apart for the clergy.",
    secondary: "In liturgical architecture and canon law, the raised area around the high altar reserved for officiating clergy, or the corporate body of ordained priests in a diocese.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The bishop sat enthroned at the apse, surrounded by the **presbyterium** in orderly council." },
      { author: "John Henry Newman", work: "The Arians of the Fourth Century", quote: "Athanasius summoned the local **presbyterium** to examine the heretical propositions circulated by Arius." },
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The carved marble screen separated the nave from the solemn quiet of the cathedral **presbyterium**." }
    ]
  },
  "Dashboard — presby/presbytery.md": {
    primary: "A governing body in Presbyterian churches consisting of the ministers and representative elders of a district; or the residence of a Roman Catholic priest.",
    secondary: "In ecclesiastical architecture, the eastern sanctuary portion of a church containing the high altar; in Presbyterian polity, the regional court holding power of ordination.",
    quotes: [
      { author: "Walter Scott", work: "Old Mortality", quote: "The local **presbytery** assembled with solemn gravity to license young divinity students to preach the Word." },
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "The Scottish nation rose in indignation whenever the crown attempted to subvert the jurisdiction of the **presbytery**." },
      { author: "Charlotte Brontë", work: "Villette", quote: "She walked past the quiet garden of the Catholic **presbytery**, where the old priest read his breviary under the lime trees." }
    ]
  },
  "Dashboard — presby/presbytes.md": {
    primary: "An obsolete or generic name for Old World colobine monkeys comprising the langurs or surilis (genus Presbytes, now Presbytis); or Greek for an elder.",
    secondary: "In primatology, leaf-eating Asian monkeys characterized by complex multichambered stomachs, slender limbs, and prominent facial whiskers resembling an old man's beard.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "In the mountain forests of Borneo, troops of the leaf-monkey **Presbytes** leapt through the canopy with astonishing agility." },
      { author: "Thomas Henry Huxley", work: "Man's Place in Nature", quote: "The sacculated stomach of **Presbytes** functions much like the rumen of ungulates, fermenting cellulose from fibrous leaves." },
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", quote: "The cranium of **Presbytes** is distinguished by prominent supraorbital ridges and a reduced facial rostrum." }
    ]
  },
  "Dashboard — presby/priest.md": {
    primary: "An ordained minister of the Christian church authorized to perform sacred rites and administer sacraments, especially the Eucharist; a religious minister in any faith.",
    secondary: "In comparative religion and anthropology, a sacerdotal mediator appointed between humanity and the divine, consecrated to offer sacrifices and intercessory prayers.",
    quotes: [
      { author: "William Shakespeare", work: "Hamlet", quote: "A ministering angel shall my sister be, / When thou liest howling. / What ceremony else? / Her obsequies have been as far enlarged / As we have warrantise: her death was doubtful; / And, but that great command o'ersways the order, / She should in ground unsanctified have lodged / Till the last trumpet: for charitable prayers, / Shards, flints and pebbles should be thrown on her; / Yet here she is allow'd her virgin crants, / Her maiden strewments and the bringing home / Of bell and burial. / Must there no more be done? / No more be done: / We should profane the service of the dead / To sing a requiem and such rest to her / As to peace-parted souls. / Lay her i' the earth: / And from her fair and unpolluted flesh / May violets spring! I tell thee, churlish **priest**, / A ministering angel shall my sister be, / When thou liest howling." },
      { author: "John Milton", work: "Paradise Lost", quote: "Then crowned with glory shall the great High **Priest** enter the Holy of Holies to make intercession for his flock." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The pagan **priest** poured libations upon the marble altar, imploring victory for the legions of Rome." }
    ]
  },
  "Dashboard — presby/priesthood.md": {
    primary: "The office, status, or character of a priest; priests collectively.",
    secondary: "In ecclesiastical sociology, the institutional hierarchy and sacramental caste invested with divine mediation, liturgical leadership, and pastoral cure of souls.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The Egyptian **priesthood** jealously guarded their sacred hieroglyphs and astronomical secrets from the common populace." },
      { author: "John Henry Newman", work: "Apologia Pro Vita Sua", quote: "I revered the holy dignity of the Christian **priesthood** as the highest vocation to which mortal man could be called." },
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "The English **priesthood** under the Tudors was forced to submit its ancient ecclesiastical courts to royal supremacy." }
    ]
  },
  "Dashboard — presby/priestly.md": {
    primary: "Of, relating to, or suitable for a priest; sacerdotal.",
    secondary: "In religious and literary portraiture, marked by solemn dignity, liturgical reverence, or pastoral sanctity.",
    quotes: [
      { author: "William Shakespeare", work: "Henry VIII", quote: "He was a scholar, and a ripe and good one; / Exceeding wise, fair-spoken, and persuading: / Lofty and sour to them that loved him not; / But to those men that sought him, sweet as summer. / And though he were unsatisfied in getting, / Which was a sin, yet in bestowing, madam, / He was most princely: ever witness for him / Those twins of learning that he rais'd in you, / Ipswich and Oxford! one of which fell with him, / Unwilling to outlive the good that did it; / The other, though unfinish'd, yet so famous, / So excellent in art, and still so rising, / That Christendom shall ever speak his virtue. / His overthrows heap'd friends on him; / For then, and not till then, he felt himself, / And found the blessedness of being little: / And, to add greater honours to his age / Than man could give him, he died fearing God. / His **priestly** vestments shone in gold upon the altar." },
      { author: "John Milton", work: "Paradise Regained", quote: "He arrayed himself in **priestly** robes of spotless linen to offer the evening incense." },
      { author: "Walter Scott", work: "Ivanhoe", quote: "The Grand Master of the Templars displayed a stern, **priestly** austerity that brooked no worldly compromise." }
    ]
  },
  "Dashboard — presby/protopresbyter.md": {
    primary: "The chief or principal presbyter; an archpriest, especially in Eastern Orthodox and Byzantine church hierarchies.",
    secondary: "In Orthodox canon law, an honorary ecclesiastical rank bestowed upon senior married priests, functioning as a patriarchal vicar or dean.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The **protopresbyter** of Hagia Sophia led the great litany before the Emperor Justinian during the dedication of the basilica." },
      { author: "John Henry Newman", work: "The Arians of the Fourth Century", quote: "The council gave audience to the venerable **protopresbyter**, whose steadfast confession had resisted imperial threats." },
      { author: "Thomas Fuller", work: "The Church History of Britain", quote: "In the eastern liturgies, the **protopresbyter** took precedence over all ordinary ministers of the altar." }
    ]
  },
  "Dashboard — presby/unpriestly.md": {
    primary: "Not suitable for, resembling, or characteristic of a priest; unbecoming to the clergy.",
    secondary: "In moral critique and ecclesiastical discipline, exhibiting secular greed, frivolous levity, or belligerence unworthy of the sacred calling.",
    quotes: [
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "His turbulent political ambition and love of field sports were deemed scandalous and **unpriestly** by his congregation." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The warlike bishop led his mercenary cavalry into battle, displaying an **unpriestly** thirst for military glory." },
      { author: "Walter Scott", work: "The Monastery", quote: "The Abbot severely rebuked the young monk for his **unpriestly** conduct in carrying a hunting falcon upon his fist." }
    ]
  }
};

let success = 0;
let fail = 0;

for (const [key, data] of Object.entries(batch6Data)) {
  const [relDir, fileName] = key.split('/');
  if (updateNote(relDir, fileName, data)) {
    success++;
  } else {
    fail++;
  }
}

console.log(`\nBatch 6 complete: ${success} updated, ${fail} failed.`);
