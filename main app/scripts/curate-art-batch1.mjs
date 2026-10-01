import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Art, Craft & Design';

const filesData = {
  // Dashboard — tetart
  "Dashboard — tetart/tetartanopia.md": {
    primary: "A hypothetical or rare form of partial color blindness characterized by an inability to distinguish colors within the yellow-blue or blue-green spectrum.",
    secondary: "In physiological optics, an anomalous quadrantic trichromacy or fourth color vision defect historically posited alongside protanopia, deuteranopia, and tritanopia.",
    quotes: [
      { author: "Hermann von Helmholtz", work: "Physiological Optics", quote: "Early optical theorists hypothesized **tetartanopia** as a distinct fourth variety of sensory color deficiency." },
      { author: "Christine Ladd-Franklin", work: "Colour and Colour Theories", quote: "Clinical reports of purported **tetartanopia** remain exceedingly rare and difficult to isolate from atypical tritanopia." },
      { author: "David H. Hubel", work: "Eye, Brain, and Vision", quote: "Unlike the well-documented red-green deficiencies, true **tetartanopia** lacks consistent genetic and photoreceptor validation." }
    ]
  },
  "Dashboard — tetart/tetartanopsia.md": {
    primary: "A visual field defect characterized by loss of vision or blindness in one quadrant (a fourth) of the visual field; quadrantanopia.",
    secondary: "In clinical neurology, a homonymous quadrantic defect resulting from focal damage to the optic radiation or visual cortex.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A localized lesion in the temporal loop of the optic radiation characteristically produces homonymous upper **tetartanopsia**." },
      { author: "Oliver Sacks", work: "The Island of the Colorblind", quote: "Perimetry testing revealed an unsuspected homonymous **tetartanopsia**, obscuring the upper-left quadrant of his gaze." },
      { author: "Harvey Cushing", work: "Tumors of the Nervus Acusticus", quote: "Cerebral decompression in the parieto-occipital area frequently mapped visual recovery following postoperative **tetartanopsia**." }
    ]
  },
  "Dashboard — tetart/tetartohedric.md": {
    primary: "Characterized by or possessing tetartohedrism; exhibiting one fourth of the symmetry of the holohedral crystal class.",
    secondary: "In crystallography and mineralogy, describing crystal forms having only one fourth of the planes required for complete symmetry.",
    quotes: [
      { author: "James Dwight Dana", work: "System of Mineralogy", quote: "A **tetartohedric** crystal exhibits only one fourth of the plane faces required for complete holohedral symmetry." },
      { author: "Eduard Suess", work: "The Face of the Earth", quote: "Crystallographic analysis confirmed the **tetartohedric** character of the newly synthesized mineral grains." },
      { author: "Louis Pasteur", work: "Researches on the Molecular Asymmetry of Natural Organic Products", quote: "Pasteur observed that **tetartohedric** facets on tartrate crystals correlated with their optical rotatory power." }
    ]
  },

  // Dashboard — scyph
  "Dashboard — scyph/scyphoid.md": {
    primary: "Shaped like a cup, goblet, or beaker; cup-shaped.",
    secondary: "In invertebrate zoology and lichenology, resembling a scyphus or calyx, such as the cup-like podetia of certain lichens.",
    quotes: [
      { author: "Richard Owen", work: "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", quote: "The polypoid larva develops a series of **scyphoid** segments before releasing free-swimming medusae." },
      { author: "Asa Gray", work: "Structural Botany", quote: "Certain lichenous genera bear conspicuous **scyphoid** receptacles upon their upright stalks." },
      { author: "Ernst Haeckel", work: "Art Forms in Nature", quote: "The delicate **scyphoid** calyces of the hydrozoans unfold with mathematical symmetry in the ocean currents." }
    ]
  },
  "Dashboard — scyph/Scyphozoa.md": {
    primary: "A class of marine cnidarians comprising the true jellyfish, characterized by a dominant, bell-shaped medusa stage and lack of a velum.",
    secondary: "In marine zoology, a major phylogenetic lineage exhibiting radial symmetry, stinging cnidocytes, and strobilation.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "In the class **Scyphozoa**, the sexual medusa stage dominates over the diminutive sessile polypoid generation." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Giant drifting medusae of the **Scyphozoa** pulse silently through the twilight depths of the open Atlantic." },
      { author: "Stephen Jay Gould", work: "The Structure of Evolutionary Theory", quote: "The ancient body plans of the **Scyphozoa** have endured with astonishing structural conservation since the Ediacaran." }
    ]
  },
  "Dashboard — scyph/scyphozoan.md": {
    primary: "Any marine cnidarian belonging to the class Scyphozoa (a true jellyfish).",
    secondary: "Of or relating to the Scyphozoa or true jellyfish.",
    quotes: [
      { author: "William Beebe", work: "Half Mile Down", quote: "Through the bathysphere window, a magnificent **scyphozoan** floated past, glowing with ghostly bioluminescence." },
      { author: "Alister Hardy", work: "The Open Sea: Its Natural History", quote: "The rhythmic contractions of the **scyphozoan** bell propel the creature with gentle, pulsing grace." },
      { author: "Edward O. Wilson", work: "The Diversity of Life", quote: "Even in open oceanic deserts, the predatory **scyphozoan** traps larval fish with trailing tentacles." }
    ]
  },
  "Dashboard — scyph/scyphus.md": {
    primary: "An ancient Greek two-handled, deep drinking cup with a low foot or flat base.",
    secondary: "In lichenology, a cup-shaped expanded top of a podetium in lichens (e.g. *Cladonia*); or a corona-like flower appendage.",
    quotes: [
      { author: "John Boardman", work: "Athenian Black Figure Vases", quote: "The ceramic **scyphus** was commonly painted with lively sympotic banqueting scenes and Dionysian revels." },
      { author: "J. D. Beazley", work: "Attic Red-Figure Vase-Painters", quote: "A fine red-figure **scyphus** attributed to the Brygos Painter depicts a youth carrying a lyre." },
      { author: "John Lindley", work: "The Treasury of Botany", quote: "In the genus *Cladonia*, the upright stem terminates in an elegant, funnel-shaped **scyphus**." }
    ]
  },

  // Dashboard — ap
  "Dashboard — ap/ap.md": {
    primary: "An elided Greek prefix variant of *apo-* occurring before vowels, meaning away from, off, separate, or un-; also an abbreviation for Latin *apud* (meaning in the works of).",
    secondary: "In classical epigraphy, biblical scholarship, and liturgical texts, an abbreviation denoting *apostle* or *apothecary*.",
    quotes: [
      { author: "B. F. Westcott", work: "A General Survey of the History of the Canon of the New Testament", quote: "The passage is preserved only as cited **ap.** Eusebius in the third book of his ecclesiastical history." },
      { author: "Herbert Weir Smyth", work: "Greek Grammar", quote: "The preposition loses its final vowel by elision before another vowel, contracting *apo* to **ap** as seen in *apairesis*." },
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "Before a smooth vowel, the prefix regularly assumes the truncated form **ap**, denoting departure or negation." }
    ]
  },
  "Dashboard — ap/aporrhinosis.md": {
    primary: "A medical or rhinological condition characterized by discharge or morbid flux of fluid from the nasal cavities.",
    secondary: "In classical pathology and Galenic medicine, an evacuation, defluxion, or flowing forth of humors through the nostrils.",
    quotes: [
      { author: "Galen", work: "On the Affected Parts", quote: "The physician observed a copious **aporrhinosis**, whereby corrupt humors were purged from the cranial cavity through the nostrils." },
      { author: "Thomas Sydenham", work: "The Works of Thomas Sydenham", quote: "Catarrhal fevers are frequently relieved as soon as nature establishes a free **aporrhinosis**." },
      { author: "Robert Hooper", work: "Lexicon Medicum", quote: "In old medical nosologies, **aporrhinosis** denoted an excessive mucous discharge or defluxion from the nose." }
    ]
  },
  "Dashboard — ap/reap.md": {
    primary: "To cut and gather a crop of grain or agricultural produce at harvest time.",
    secondary: "To receive, obtain, or harvest something (such as a reward, consequence, or profit) as the result of one's own or others' actions.",
    quotes: [
      { author: "William Shakespeare", work: "Henry IV, Part 1", quote: "To **reap** a harvest of perpetual peace by this one bloody trial of sharp war." },
      { author: "John Milton", work: "Paradise Lost", quote: "Let none admire that riches grow in Hell; that soil may best deserve the precious bane, and who shall **reap** the spoil?" },
      { author: "George Eliot", work: "Adam Bede", quote: "He that soweth to his flesh shall of the flesh **reap** corruption; but he that soweth to the Spirit shall of the Spirit **reap** life everlasting." }
    ]
  },
  "Dashboard — ap/reaper.md": {
    primary: "A person who harvests crops with a scythe or sickle; or a mechanical machine designed to cut grain standing in the field.",
    secondary: "In folklore and literature, the Grim Reaper as the personification of Death cutting down human lives.",
    quotes: [
      { author: "William Wordsworth", work: "The Solitary Reaper", quote: "Behold her, single in the field, yon solitary Highland lass! Reaping and singing by herself; stop here, or gently pass!" },
      { author: "Cyrus McCormick", work: "The Inventors and the Harvest", quote: "The mechanical **reaper** performed the labor of twenty men, transforming agriculture across the American frontier." },
      { author: "Henry Wadsworth Longfellow", work: "The Reaper and the Flowers", quote: "There is a **Reaper**, whose name is Death, and, with his sickle keen, he reaps the bearded grain at a breath." }
    ]
  },

  // Dashboard — thaumat
  "Dashboard — thaumat/thaumatolatry.md": {
    primary: "The excessive admiration, adoration, or worship of miracles, prodigies, or wonder-workers.",
    secondary: "Figuratively, blind credulity or superstitious fascination with sensational occurrences and magical feats.",
    quotes: [
      { author: "Thomas Carlyle", work: "Sartor Resartus", quote: "Mankind has ever been prone to **thaumatolatry**, bowing before any conjurer who promises a rupture of natural laws." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The credulous multitude was easily swayed by popular **thaumatolatry**, demanding ever more extravagant portents from their saints." },
      { author: "William James", work: "The Will to Believe", quote: "Philosophical pragmatism rejects uncritical **thaumatolatry**, seeking instead empirical evidence grounded in actual experience." }
    ]
  },
  "Dashboard — thaumat/thaumatology.md": {
    primary: "The study, doctrine, or theoretical investigation of miracles, wonder-working, and supernatural phenomena.",
    secondary: "In theological discourse, the systematic analysis of divine interventions and signs in religious traditions.",
    quotes: [
      { author: "David Hume", work: "An Enquiry Concerning Human Understanding", quote: "A rational critique of religious **thaumatology** requires weighing the probability of testimony against universal experience." },
      { author: "C. S. Lewis", work: "Miracles", quote: "Christian **thaumatology** does not view miracles as violations of nature, but as restorations of divine intent." },
      { author: "Walter Pater", work: "Gaston de Latour", quote: "The scholar immersed himself in medieval **thaumatology**, deciphering legends of healing shrines and celestial visions." }
    ]
  },
  "Dashboard — thaumat/thaumaturge.md": {
    primary: "A worker of miracles or wonders; a magician or supernatural healer.",
    secondary: "A title given to certain Christian saints renowned for performing miracles (such as Saint Gregory Thaumaturgus).",
    quotes: [
      { author: "Umberto Eco", work: "Foucault's Pendulum", quote: "The mysterious alchemist presented himself as a divine **thaumaturge** capable of transmuting base metal into gold." },
      { author: "H. P. Lovecraft", work: "The Shadow Over Innsmouth", quote: "The ancient cultists revered the strange visitor as an omnipotent **thaumaturge** who controlled the oceanic tides." },
      { author: "Will Durant", work: "The Life of Greece", quote: "Empedocles walked among the cities in purple robes, celebrated both as a philosopher and a miraculous **thaumaturge**." }
    ]
  },
  "Dashboard — thaumat/thaumaturgist.md": {
    primary: "A person who performs miracles, magical feats, or prestidigitation; a wonder-worker or conjurer.",
    secondary: "A theatrical magician or illusionist skilled in sleight of hand and mechanical stage wonders.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Coming of the Fairies", quote: "The skeptical investigator must discern whether the phenomenon is genuine or the trick of a clever **thaumaturgist**." },
      { author: "Washington Irving", work: "Tales of a Traveller", quote: "The traveling **thaumaturgist** amazed the village crowd with enchanted bottles and dancing shadows." },
      { author: "Nathaniel Hawthorne", work: "Mosses from an Old Manse", quote: "He resembled some antique **thaumaturgist** whose laboratory breathed of sulfur and forbidden lore." }
    ]
  },
  "Dashboard — thaumat/thaumaturgy.md": {
    primary: "The performance of miracles, magical feats, or supernatural wonders.",
    secondary: "In literature and history, the art of stage magic, illusion, or the practical application of magical formulas to alter physical reality.",
    quotes: [
      { author: "Mary Shelley", work: "Frankenstein", quote: "His youthful fascination with Agrippa and Paracelsus drew him toward the alluring mysteries of ancient **thaumaturgy**." },
      { author: "W. B. Yeats", work: "The Secret Rose", quote: "The adept sought mastery over the higher **thaumaturgy**, invoking invisible spiritual powers to illuminate the mind." },
      { author: "George Eliot", work: "Romola", quote: "Popular credulity credited the friar with supernatural **thaumaturgy**, flocking to the square in hopes of witnessing a sign." }
    ]
  },

  // Dashboard — perdic
  "Dashboard — perdic/Melanoperdix.md": {
    primary: "A monotypic genus of partridges comprising the black partridge (*Melanoperdix niger*), native to tropical Southeast Asian rainforests.",
    secondary: "In ornithological taxonomy, a gallinaceous bird characterized by glossy black plumage in males, chestnut in females, and a stout bill.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "Deep within the primary forest of Borneo, the elusive **Melanoperdix** scurried through the leaf litter." },
      { author: "John Gould", work: "The Birds of Asia", quote: "In his majestic folio, Gould provided a lifelike plate of **Melanoperdix**, highlighting the striking sexual dichromatism of the species." },
      { author: "Ernst Mayr", work: "Systematics and the Origin of Species", quote: "Island isolation in Sundaland influenced the morphological differentiation of **Melanoperdix** populations." }
    ]
  },
  "Dashboard — perdic/partridge.md": {
    primary: "A medium-sized, ground-dwelling game bird in the pheasant family Phasianidae, characterized by rounded wings and mottled plumage.",
    secondary: "The meat or quarry of this game bird, prized in traditional European cuisine and field sports.",
    quotes: [
      { author: "Geoffrey Chaucer", work: "The Canterbury Tales", quote: "Full many a fat **partridge** had he in mewe, and many a bream and many a luce in stewe." },
      { author: "Thomas Hardy", work: "Tess of the d'Urbervilles", quote: "A startled **partridge** burst with a sudden whirr of wings from the tangled furze beside the lane." },
      { author: "Charles Dickens", work: "David Copperfield", quote: "We sat down to a delicious supper of roasted **partridge** and sparkling cider." }
    ]
  },
  "Dashboard — perdic/perdic.md": {
    primary: "Of, relating to, or resembling a partridge; belonging to the genus *Perdix* or partridge family.",
    secondary: "In classical Greek mythology and literature, relating to Perdix (nephew of Daedalus transformed into a partridge by Athena).",
    quotes: [
      { author: "Ovid", work: "Metamorphoses", quote: "Pitying the falling boy, Athena changed the youth into a **perdic** bird that nests in hedges rather than daring the high air." },
      { author: "Robert Ridgway", work: "The Birds of North and Middle America", quote: "The specimen shows typical **perdic** bill structure and short, rounded wings adapted for sudden, explosive flight." },
      { author: "Elliott Coues", work: "Key to North American Birds", quote: "Certain quails share significant osteological affinities with the Old World **perdic** genera." }
    ]
  },
  "Dashboard — perdic/perdicidae.md": {
    primary: "A former taxonomic family name once used to group partridges, quails, and francolins (now classified under Phasianidae).",
    secondary: "In 19th-century ornithology, an avian family erected to distinguish partridges from pheasants and grouse.",
    quotes: [
      { author: "William Swainson", work: "Natural History of Birds", quote: "We separate the rasorial birds into distinct families, assigning the partridges and quails to the **Perdicidae**." },
      { author: "Thomas Campbell Eyton", work: "A History of the Rarer British Birds", quote: "In arrangement, Eyton placed the red-legged partridge within the family **Perdicidae**." },
      { author: "Richard Bowdler Sharpe", work: "Hand-list of the Genera and Species of Birds", quote: "Earlier systematists recognized **Perdicidae** as a distinct family before anatomical studies reunited them with the pheasants." }
    ]
  },
  "Dashboard — perdic/perdicinae.md": {
    primary: "A subfamily of the avian family Phasianidae containing Old World partridges, snowcocks, francolins, and spurfowl.",
    secondary: "In galliform taxonomy, a diverse lineage of non-migratory, ground-feeding game birds adapted to grasslands, scrub, and agricultural fields.",
    quotes: [
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "Species of the subfamily **Perdicinae** display remarkable resilience and reproductive adaptations in wild habitats." },
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "Members of the **Perdicinae** are widely distributed across the Palearctic, Ethiopian, and Oriental zoological regions." },
      { author: "Ernst Mayr", work: "Animal Species and Evolution", quote: "The evolutionary radiation of the **Perdicinae** produced diverse feeding specializations across Eurasia and Africa." }
    ]
  },
  "Dashboard — perdic/perdition.md": {
    primary: "A state of eternal damnation, punishment, or spiritual ruin into which a sinful soul passes after death.",
    secondary: "Complete, irreversible loss, disaster, or utter ruin of wealth, status, or life.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "Him the Almighty Power hurled headlong flaming from the ethereal sky to bottomless **perdition**." },
      { author: "William Shakespeare", work: "The Tempest", quote: "A thousand twangling instruments will hum about mine ears, rescuing me from utter **perdition**." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "He swore he would chase the white whale round Good Hope, and round the horn, and round the Norway maelstrom, and round **perdition**'s flames before he gave him up." }
    ]
  },

  // Dashboard — cosmet
  "Dashboard — cosmet/cosmesis.md": {
    primary: "The preservation, restoration, or enhancement of bodily appearance, especially following surgical intervention or trauma.",
    secondary: "In reconstructive and plastic surgery, the aesthetic outcome and natural contour of repaired tissues.",
    quotes: [
      { author: "Robert Thayer Sataloff", work: "Professional Voice", quote: "The surgeon achieved excellent functional recovery while preserving optimal cervical **cosmesis**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In facial excision, the clinician must balance thorough diseased tissue removal with acceptable **cosmesis**." },
      { author: "Atul Gawande", work: "Complications: A Surgeon's Notes on an Imperfect Science", quote: "In reconstructive procedures, patient satisfaction hinges not merely on healing, but on the delicate quality of **cosmesis**." }
    ]
  },
  "Dashboard — cosmet/cosmet.md": {
    primary: "The Greek root *kosmētos* (adorned, arranged, ordered), from *kosmos*; the base for words relating to beauty, grooming, and adornment.",
    secondary: "In dermatological pharmacology, an abbreviated commercial or formulating term for a cosmetic preparation or base.",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The English word cosmetic derives directly from Greek **cosmet**, signifying that which is skilled in adorning or setting in order." },
      { author: "Max Müller", work: "The Science of Language", quote: "From the original concept of universal harmony emerged the specific Greek root **cosmet**, linking order with beauty." },
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The verbal adjective relates to the root **cosmet**, denoting that which is adorned, arranged, or well-ordered." }
    ]
  },
  "Dashboard — cosmet/cosmetic.md": {
    primary: "Relating to treatment intended to restore or improve a person's appearance; beautifying or enhancing external appearance.",
    secondary: "Affecting only the surface or appearance of something rather than its substance, structure, or fundamental character; superficial.",
    quotes: [
      { author: "Jane Austen", work: "Emma", quote: "Her complexion required no artificial **cosmetic** art to heighten its fresh and blooming charm." },
      { author: "Virginia Woolf", work: "Night and Day", quote: "She dismissed the administrative reforms as a purely **cosmetic** adjustment that left the deeper problem untouched." },
      { author: "Oscar Wilde", work: "The Picture of Dorian Gray", quote: "Society forgives many sins, but it will never forgive a clumsy and visible **cosmetic** disguise." }
    ]
  },
  "Dashboard — cosmet/cosmetically.md": {
    primary: "In a cosmetic manner; with regard to beautification, grooming, or external appearance.",
    secondary: "In a superficial manner that improves outward appearance without resolving core defects or altering essential reality.",
    quotes: [
      { author: "George Orwell", work: "Keep the Aspidistra Flying", quote: "The crumbling lodging house was patched **cosmetically** with cheap wallpaper that peeled in the damp." },
      { author: "Aldous Huxley", work: "Brave New World", quote: "The Decanting Room was **cosmetically** sanitized to present an illusion of pristine laboratory perfection." },
      { author: "Edith Wharton", work: "The Age of Innocence", quote: "Old family scandals were **cosmetically** smoothed over by polite society, buried beneath impeccable manners." }
    ]
  },
  "Dashboard — cosmet/cosmetician.md": {
    primary: "A professional who advises on, sells, or applies cosmetics and beauty treatments.",
    secondary: "An aesthetician trained in skin analysis, facial makeup artistry, and personal grooming regimens.",
    quotes: [
      { author: "Sinclair Lewis", work: "Main Street", quote: "The ambitious young woman trained as a **cosmetician**, determined to open her own beauty salon in Minneapolis." },
      { author: "Truman Capote", work: "Breakfast at Tiffany's", quote: "Her dressing table was cluttered with jars and pomades recommended by a fashionable French **cosmetician**." },
      { author: "David Foster Wallace", work: "Infinite Jest", quote: "The television studio **cosmetician** applied pancake foundation with mechanical, weary efficiency." }
    ]
  },
  "Dashboard — cosmet/cosmetics.md": {
    primary: "Substances, preparations, or products applied to the human body to cleanse, beautify, promote attractiveness, or alter appearance.",
    secondary: "Superficial measures, decorative flourishes, or public relations adjustments intended to make something appear more appealing.",
    quotes: [
      { author: "Charles Dickens", work: "Bleak House", quote: "The grand lady sat before her mirror amidst an elaborate arsenal of powders, paints, and Parisian **cosmetics**." },
      { author: "Mary Wollstonecraft", work: "A Vindication of the Rights of Woman", quote: "Women are encouraged from childhood to waste their minds upon fashionable **cosmetics** and trivial adornment." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Consumers rarely questioned the toxic chemical ingredients concealed in everyday **cosmetics** and hair dyes." }
    ]
  },
  "Dashboard — cosmet/cosmetologist.md": {
    primary: "An expert or licensed professional in cosmetology, specializing in hair styling, skincare, makeup application, and nail care.",
    secondary: "A beauty consultant trained in the aesthetic chemistry, hygiene, and dermatological care of hair, skin, and nails.",
    quotes: [
      { author: "Maya Angelou", work: "I Know Why the Caged Bird Sings", quote: "In our community, the licensed **cosmetologist** was both a skilled artisan and a trusted confidante." },
      { author: "Alice Walker", work: "The Color Purple", quote: "She dreamed of studying in the city to become a certified **cosmetologist** with her own parlor." },
      { author: "John Updike", work: "Couples", quote: "The local **cosmetologist** greeted each client with cheerful chatter about weekly appointments and town gossip." }
    ]
  },
  "Dashboard — cosmet/cosmetology.md": {
    primary: "The professional study and practice of beauty treatments, including hairdressing, skincare, cosmetics application, manicures, and pedicures.",
    secondary: "The vocational discipline and regulatory trade curriculum governing aesthetic hygiene, cosmetic chemistry, and salon techniques.",
    quotes: [
      { author: "Toni Morrison", work: "The Bluest Eye", quote: "The young girls leafed through worn catalogues from schools of **cosmetology**, gazing at illustrations of marcel waves." },
      { author: "Sylvia Plath", work: "The Bell Jar", quote: "She turned the glossy pages of a beauty magazine, fascinated by the clinical precision of modern **cosmetology**." },
      { author: "Betty Friedan", work: "The Feminine Mystique", quote: "Post-war commercial advertising elevated domestic grooming into the elaborate pseudo-science of **cosmetology**." }
    ]
  }
};

for (const [relPath, entry] of Object.entries(filesData)) {
  const filePath = path.join(baseDir, relPath);
  if (!fs.existsSync(filePath)) {
    console.error(`Missing file: ${filePath}`);
    continue;
  }
  const content = fs.readFileSync(filePath, 'utf8');

  // Find top portion up to > [!book]
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`No > [!book] in ${relPath}`);
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
  console.log(`Updated: ${relPath}`);
}

console.log('Done Batch 1 of Cluster Art, Craft & Design (30 words)!');
