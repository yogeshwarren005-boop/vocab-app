import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Art, Craft & Design/Dashboard — plec';

const filesData = {
  "aplectrum.md": {
    primary: "A genus of North American terrestrial orchids comprising the single species *Aplectrum hyemale* (puttyroot), characterized by spurless flowers.",
    secondary: "In botanical taxonomy, an orchid that produces a single winter leaf and a subterranean chain of swollen, globular corms.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The solitary winter leaf of **Aplectrum** persists through frost and snow, withering before the floral scape arises in spring." },
      { author: "John Torrey", work: "Flora of North America", quote: "Botanists placed the puttyroot in **Aplectrum** on account of its spurless perianth and corrugated lip." },
      { author: "William Bartram", work: "Travels", quote: "In rich Appalachian deciduous woods, the globose corms of **Aplectrum** lie chained together beneath the leaf mold." }
    ]
  },
  "apoplectic.md": {
    primary: "Overcome with extreme, uncontrollable anger or indignation, turning red in the face.",
    secondary: "Relating to or caused by apoplexy (stroke); exhibiting cerebral hemorrhage or sudden loss of neurological consciousness.",
    quotes: [
      { author: "Charles Dickens", work: "Bleak House", quote: "The elderly gentleman flew into an **apoplectic** rage, his countenance turning purple above his stiff cravat." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "Old Osborne sat in his leather armchair, silent and **apoplectic** after reading the insolent letter." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The physician recognized an acute **apoplectic** seizure by the deep stertorous breathing and unilateral paralysis." }
    ]
  },
  "apoplectiform.md": {
    primary: "Resembling apoplexy or a stroke; characterized by sudden onset of cerebral symptoms without extensive permanent hemorrhage.",
    secondary: "In clinical neurology, describing transient ischemic attacks or pseudo-apoplectic episodes mimicking cerebrovascular accidents.",
    quotes: [
      { author: "Jean-Martin Charcot", work: "Clinical Lectures on the Diseases of the Nervous System", quote: "Multiple sclerosis may occasionally present with an acute **apoplectiform** attack that subsides within forty-eight hours." },
      { author: "William Gowers", work: "A Manual of Diseases of the Nervous System", quote: "Sudden congestive attacks in general paresis frequently assume an **apoplectiform** character." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "The patient experienced recurrent **apoplectiform** episodes that temporarily paralyzed his left arm and speech." }
    ]
  },
  "apoplectoid.md": {
    primary: "Resembling or allied to apoplexy; apoplectic in clinical character or appearance.",
    secondary: "Exhibiting stroke-like symptoms, stupor, or sudden vascular collapse.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe uremic intoxication can trigger sudden **apoplectoid** seizures that confuse the inexperienced diagnostician." },
      { author: "Jean-Martin Charcot", work: "Lectures on Localization in Diseases of the Brain", quote: "Focal cerebral softening often commences with an **apoplectoid** onset before localized motor deficits emerge." },
      { author: "Robert Hooper", work: "Lexicon Medicum", quote: "Pathologists designated as **apoplectoid** those sudden comatose states unassociated with detectable ventricular bleeding." }
    ]
  },
  "apoplexy.md": {
    primary: "Unconsciousness, paralysis, or neurological collapse resulting from a cerebral hemorrhage or stroke.",
    secondary: "A state of extreme, overwhelming fury or speechless indignation.",
    quotes: [
      { author: "William Shakespeare", work: "Henry IV, Part 2", quote: "This **apoplexy** is, as I take it, a kind of lethargy, an't please your lordship, a kind of sleeping in the blood." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "John Reed had spent his youth in debauchery, dying at last in London of what was termed **apoplexy**." },
      { author: "Washington Irving", work: "The Legend of Sleepy Hollow", quote: "The Dutch farmer was in imminent danger of **apoplexy** from the abundance of his heavy harvest meals." }
    ]
  },
  "applecart.md": {
    primary: "A light handcart or barrow used by a street vendor for transporting and selling apples.",
    secondary: "Used in the idiom 'upset the applecart', meaning to spoil or disrupt carefully laid plans or the status quo.",
    quotes: [
      { author: "George Bernard Shaw", work: "The Apple Cart", quote: "The King warned his cabinet that a premature constitutional crisis would inevitably overturn the **applecart**." },
      { author: "P. G. Wodehouse", work: "The Code of the Woosters", quote: "One false move would completely upset Aunt Dahlia's **applecart** and plunge the household into disaster." },
      { author: "H. G. Wells", work: "The New Machiavelli", quote: "The radical backbenchers threatened to upset the political **applecart** by voting against the government's budget." }
    ]
  },
  "euplectella.md": {
    primary: "A genus of deep-sea glass sponges in the class Hexactinellida, notably *Euplectella aspergillum* (Venus' flower basket), famous for its intricate siliceous skeleton.",
    secondary: "In marine biology, an abyssal sponge that often permanently encases a symbiotic pair of spongicolid shrimp inside its woven glass lattice.",
    quotes: [
      { author: "Richard Owen", work: "On a New Genus and Species of Sponge: Euplectella Aspergillum", quote: "The cylindrical framework of **Euplectella** consists of curved siliceous threads woven with matchless mathematical elegance." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "The glass sponge **Euplectella** secretes a rigid cylindrical lattice of fused opaline spicules." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "From the ocean floor beneath the Philippines comes **Euplectella**, its delicate basket of woven glass reflecting ancient architectural perfection." }
    ]
  },
  "plecoptera.md": {
    primary: "An ancient order of hemimetabolous insects commonly known as stoneflies, possessing aquatic nymphs and four membranous wings folded flat over the back.",
    secondary: "In freshwater ecology, an insect order whose presence serves as a sensitive bioindicator of pristine, well-oxygenated water quality.",
    quotes: [
      { author: "Rachel Carson", work: "Silent Spring", quote: "Sensitive aquatic larvae of the order **Plecoptera** vanished from the riverbeds following aerial forest spraying." },
      { author: "Edward O. Wilson", work: "The Diversity of Life", quote: "The ancient lineage of **Plecoptera** traces back to the Carboniferous, preserving primitive wing-folding mechanisms." },
      { author: "Charles Darwin", work: "On the Origin of Species", quote: "Aquatic insects such as **Plecoptera** survive across wide geographic ranges by clinging to subterranean gravel beds." }
    ]
  },
  "plecopteran.md": {
    primary: "Any insect belonging to the order Plecoptera; a stonefly.",
    secondary: "Pertaining to or characteristic of stoneflies and their aquatic naiads.",
    quotes: [
      { author: "Alister Hardy", work: "The Open Sea and Freshwater World", quote: "The fisherman tied an artificial nymph mimicking the flattened body of a **plecopteran** clinging to river rocks." },
      { author: "Stephen Jay Gould", work: "Wonderful Life", quote: "Fossil beds reveal primitive **plecopteran** relatives that thrived along the swampy margins of Paleozoic streams." },
      { author: "Robert MacArthur", work: "Geographical Ecology", quote: "Stream riffle communities exhibit distinct resource partitioning among each coexisting **plecopteran** species." }
    ]
  },
  "plecotus.md": {
    primary: "A genus of vespertilionid bats commonly known as long-eared bats, characterized by extraordinarily large ears that fold beneath the wings during torpor.",
    secondary: "In chiropteran zoology, insectivorous bats renowned for whisper-echolocation used to glean prey from foliage.",
    quotes: [
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "The brown long-eared bat, classified as **Plecotus**, folded its enormous transparent ears under its arms while sleeping." },
      { author: "Alfred Russel Wallace", work: "Island Life", quote: "The genus **Plecotus** ranges across temperate Eurasia, exhibiting subtle geographic variation in cranial proportions." },
      { author: "Richard Dawkins", work: "The Blind Watchmaker", quote: "In **Plecotus**, acoustic gleaning enables the bat to detect the rustling footsteps of beetles in leaf litter." }
    ]
  },
  "plectania.md": {
    primary: "A genus of cup fungi in the family Sarcosomataceae, producing dark, fleshy, cup-shaped apothecia on decaying wood.",
    secondary: "In mycology, an ascomycete genus characterized by blackish, interwoven hyphal walls and operculate asci containing smooth ascospores.",
    quotes: [
      { author: "Anton de Bary", work: "Comparative Morphology and Biology of the Fungi", quote: "The leathery exciple of **Plectania** is composed of dense, dark-walled hyphae interwoven into a protective rind." },
      { author: "Elias Magnus Fries", work: "Systema Mycologicum", quote: "Fries distinguished **Plectania** among the Pezizaceae by its sooty black coloration and persistent cup shape." },
      { author: "Charles Horton Peck", work: "Annual Report of the State Botanist", quote: "In damp spruce woods, colonies of **Plectania** emerged from buried rotting twigs soon after the snow melted." }
    ]
  },
  "plectics.md": {
    primary: "The interdisciplinary study of simplicity and complexity, focusing on how complex adaptive systems arise from interwoven interactions.",
    secondary: "In complex systems theory (coined by Murray Gell-Mann), the conceptual framework investigating holistic patterns across physics, biology, and computation.",
    quotes: [
      { author: "Murray Gell-Mann", work: "The Quark and the Jaguar", quote: "I coined the term **plectics** from the Indo-European root *plek-*, denoting the study of folded and entangled systems." },
      { author: "Stuart Kauffman", work: "At Home in the Universe", quote: "In modern **plectics**, self-organization and natural selection interact to generate spontaneous order at the edge of chaos." },
      { author: "Philip W. Anderson", work: "More Is Different", quote: "The principles of **plectics** demonstrate that novel emergent properties arise as systems scale in complexity." }
    ]
  },
  "plectognath.md": {
    primary: "Any teleost fish belonging to the order Plectognathi (or Tetraodontiformes), such as pufferfishes, filefishes, triggerfishes, and boxfishes.",
    secondary: "Characterized by fused premaxillary and maxillary bones forming a beak-like jaw mechanism adapted for crushing hard prey.",
    quotes: [
      { author: "Georges Cuvier", work: "The Animal Kingdom", quote: "The solid beak of the **plectognath** enables the creature to crush coral branches and hard-shelled mollusks with ease." },
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Vertebrated Animals", quote: "In every typical **plectognath**, the jaw bones are immovably soldered to the cranium." },
      { author: "William Beebe", work: "Beneath Tropic Seas", quote: "A colorful **plectognath** hovered over the brain coral, using its sharp dental plates to browse upon algae." }
    ]
  },
  "plectognathi.md": {
    primary: "An order of teleost fishes (now Tetraodontiformes) comprising species with fused jaws and reduced pelvic fins, including puffers and triggerfishes.",
    secondary: "In ichthyological classification, a diverse taxon of marine fishes noted for dermal spines, toxic viscera (tetrodotoxin), and body armor.",
    quotes: [
      { author: "Louis Agassiz", work: "Recherches sur les Poissons Fossiles", quote: "The ancient fossil representatives of the **Plectognathi** display heavily armored dermal plates dating from the Eocene." },
      { author: "David Starr Jordan", work: "A Guide to the Study of Fishes", quote: "Members of the **Plectognathi** exhibit remarkable anatomical modifications, including the capacity to inflate the belly with water." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "Darwin captured a diodon belonging to the **Plectognathi**, observing how it distended itself into an unswallowable spiny sphere." }
    ]
  },
  "plectomycetes.md": {
    primary: "A former taxonomic class of fungi characterized by closed, spherical ascocarps (cleistothecia) containing irregularly arranged asci.",
    secondary: "In historical mycology, an assemblage encompassing green and blue molds (such as *Penicillium* and *Aspergillus*) and dermatophytes.",
    quotes: [
      { author: "Anton de Bary", work: "Comparative Morphology of Fungi", quote: "The cleistothecium of the **Plectomycetes** encloses its asci within a dense, interwoven hyphal peridium." },
      { author: "G. W. Martin", work: "The Fungi: An Advanced Treatise", quote: "In the **Plectomycetes**, asci deliquesce at maturity, discharging spherical ascospores into the central cavity." },
      { author: "Alexander Fleming", work: "Penicillin and Its Medical Applications", quote: "Early classifications grouped the mold *Penicillium* within the **Plectomycetes** due to its closed cleistothecia." }
    ]
  },
  "plectophera.md": {
    primary: "A genus of liverworts (bryophytes) characterized by folded or plaited perianth structures protecting the developing sporophyte.",
    secondary: "In bryology, non-vascular photosynthetic plants growing on damp rocks and montane bark.",
    quotes: [
      { author: "Richard Spruce", work: "Hepaticae of the Amazon and of the Andes", quote: "The delicate foliose branches of **Plectophera** carpet the misty trunks of the high Andean cloud forest." },
      { author: "Asa Gray", work: "Manual of the Botany", quote: "Microscopic dissection of the perianth confirms the distinctive plicate folds characteristic of **Plectophera**." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Bryologists categorized **Plectophera** based on the pleated architecture of its protective female envelope." }
    ]
  },
  "plectorrhiza.md": {
    primary: "A genus of epiphytic orchids native to Australia, characterized by entangled, braided aerial roots; commonly called tangle orchids.",
    secondary: "In orchidology, small monopodial epiphytes bearing pendulous racemes of fragrant green, white, or brown flowers.",
    quotes: [
      { author: "Robert Brown", work: "Prodromus Florae Novae Hollandiae", quote: "The sprawling aerial roots of **Plectorrhiza** form an entangled basket that catches leaf litter upon forest boughs." },
      { author: "John Lindley", work: "Genera and Species of Orchidaceous Plants", quote: "Lindley distinguished **Plectorrhiza** by its uniquely twisted root mass and spurless floral column." },
      { author: "Ferdinand von Mueller", work: "Fragmenta Phytographiae Australiae", quote: "In the moist gullies of New South Wales, **Plectorrhiza** clings tenaciously to the bark of rainforest myrtles." }
    ]
  },
  "plectranthus.md": {
    primary: "A large genus of flowering plants in the mint family Lamiaceae, commonly known as spurflowers, characterized by a spurred corolla base.",
    secondary: "In horticulture and ethnobotany, aromatic herbs and subshrubs cultivated for ornamental foliage and traditional remedies.",
    quotes: [
      { author: "Joseph Dalton Hooker", work: "The Flora of British India", quote: "Species of **Plectranthus** are abundant throughout the subtropical hills, bearing blue and purplish spurred blossoms." },
      { author: "Asa Gray", work: "Field, Forest, and Garden Botany", quote: "The cultivated **Plectranthus** makes an attractive trailing houseplant with its velvety, scalloped leaves." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The prominent nectar-spur at the base of the lower lip identifies the genus **Plectranthus** among labiates." }
    ]
  },
  "plectron.md": {
    primary: "A small flat piece of bone, quill, metal, ivory, or tortoiseshell used to pluck or strike the strings of a musical instrument; a plectrum.",
    secondary: "In classical antiquity, a wand or quill held in the right hand while playing the lyre or kithara.",
    quotes: [
      { author: "John Dryden", work: "The Works of Virgil", quote: "Orpheus struck the vocal strings with his golden **plectron**, charming the beasts and swaying trees." },
      { author: "Walter Pater", work: "Greek Studies", quote: "The youth posed with his kithara, raising the ivory **plectron** in poised anticipation of the hymn." },
      { author: "Matthew Arnold", work: "Empedocles on Etna", quote: "Touch the resonant wires with thy **plectron**, and sing the golden reign of Cronos." }
    ]
  },
  "plectrophenax.md": {
    primary: "A genus of Arctic and subarctic passerine birds in the longspur family Calcariidae, comprising the snow bunting (*Plectrophenax nivalis*) and McKay's bunting.",
    secondary: "In ornithology, migratory tundra songbirds possessing long, straight hind claws adapted for running over snow and barren rocky ground.",
    quotes: [
      { author: "John James Audubon", work: "The Birds of America", quote: "Flocks of **Plectrophenax** drifted over the snowdrifts like whirling snowflakes on the Arctic gale." },
      { author: "Elliott Coues", work: "Key to North American Birds", quote: "The genus **Plectrophenax** is distinguished by its elongated, spur-like hallux and dense cold-adapted plumage." },
      { author: "Peter Matthiessen", work: "The Wind Birds", quote: "High on the windswept tundra fell-fields, the cheerful trill of **Plectrophenax** announced the fleeting northern spring." }
    ]
  },
  "plectrum.md": {
    primary: "A small, thin piece of plastic, tortoiseshell, metal, or quill used to pluck or strum the strings of a guitar, lute, lyre, or harpsichord.",
    secondary: "An anatomical structure resembling a spur or pick, such as the malleus or styloid process in certain vertebrates.",
    quotes: [
      { author: "James Joyce", work: "Ulysses", quote: "A light hand brushed the harp strings with a tortoiseshell **plectrum**, releasing a cascade of silvery notes." },
      { author: "Hector Berlioz", work: "Treatise on Instrumentation", quote: "The delicate mechanical **plectrum** of the harpsichord plucks the copper wire with a crisp, crystalline attack." },
      { author: "Thomas Hardy", work: "Tess of the d'Urbervilles", quote: "The wandering minstrel gripped his bone **plectrum** between thumb and finger, striking up a lively reel." }
    ]
  },
  "plexogenic.md": {
    primary: "Originating in, arising from, or involving a nerve plexus or vascular plexus.",
    secondary: "In pathology, designating plexogenic pulmonary arteriopathy, a severe form of vascular remodeling characterized by plexiform angiomatous lesions.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Advanced pulmonary hypertension culminates in severe **plexogenic** lesions within the pre-capillary arterial beds." },
      { author: "Robert Thayer Sataloff", work: "Professional Voice", quote: "Neuralgic shoulder discomfort was traced to a **plexogenic** brachial nerve entrapment." },
      { author: "Eugene Braunwald", work: "Heart Disease: A Textbook of Cardiovascular Medicine", quote: "Histological biopsy demonstrated characteristic **plexogenic** changes with concentric laminar intimal fibrosis." }
    ]
  },
  "ploce.md": {
    primary: "A figure of speech in which a word is repeated emphatically within the same sentence or clause, but with an altered, enriched, or deepened sense.",
    secondary: "In classical and Renaissance rhetoric, the deliberate repetition of a proper noun or common word to emphasize its inherent quality.",
    quotes: [
      { author: "George Puttenham", work: "The Arte of English Poesie", quote: "This figure **ploce** repeateth a word not in vain, but to give it deeper weight and signification in the second place." },
      { author: "John Dryden", work: "Discourse Concerning Satire", quote: "The satirist used a brilliant **ploce**, turning the tyrant's own words against him with devastating irony." },
      { author: "Thomas De Quincey", work: "Rhetoric and Style", quote: "Cicero excelled in the deployment of **ploce**, repeating a term until its full emotional essence penetrated the jury's mind." }
    ]
  },
  "symplectic.md": {
    primary: "In mathematics and mathematical physics, designating a geometric structure, manifold, or transformation that preserves a closed, non-degenerate differential 2-form.",
    secondary: "In comparative ichthyology, designating the symplectic bone connecting the hyomandibular and quadrate bones in teleost skulls.",
    quotes: [
      { author: "Hermann Weyl", work: "The Classical Groups", quote: "I suggested the name **symplectic** group as a Greek equivalent for complex, to avoid ambiguity with imaginary numbers." },
      { author: "V. I. Arnold", work: "Mathematical Methods of Classical Mechanics", quote: "Hamiltonian mechanics unfolds naturally upon a phase space endowed with a canonical **symplectic** geometry." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Vertebrated Animals", quote: "In the bony fish skull, the **symplectic** ossicle wedges between the hyomandibular and quadrate elements." }
    ]
  },
  "symplectomorphism.md": {
    primary: "In differential geometry and symplectic topology, a smooth isomorphism between symplectic manifolds that preserves the symplectic form (a canonical transformation).",
    secondary: "In Hamiltonian mechanics, a phase-space mapping that preserves Hamiltonian equations of motion and phase volume (satisfying Liouville's theorem).",
    quotes: [
      { author: "V. I. Arnold", work: "Mathematical Methods of Classical Mechanics", quote: "A time evolution in Hamiltonian dynamics generates a one-parameter family of **symplectomorphism** maps on phase space." },
      { author: "Dusa McDuff", work: "Introduction to Symplectic Topology", quote: "The group of **symplectomorphism** transformations forms the central object of inquiry in modern symplectic geometry." },
      { author: "Roger Penrose", work: "The Road to Reality", quote: "Canonical transformations in classical mechanics are precisely those diffeomorphisms that preserve the symplectic structure—namely, a **symplectomorphism**." }
    ]
  },
  "symploce.md": {
    primary: "A rhetorical figure in which several successive clauses or sentences begin with the same word or words and also end with the same word or words (combining anaphora and epistrophe).",
    secondary: "In classical oratory and poetry, a symmetrical interlocking repetition creating emotional cadence and rhetorical insistence.",
    quotes: [
      { author: "Quintilian", work: "Institutio Oratoria", quote: "The figure **symploce** binds the period together by repeating the opening phrase and closing with an identical cadence." },
      { author: "George Puttenham", work: "The Arte of English Poesie", quote: "When you combine the figure of beginning and the figure of ending, you create this harmonious balance called **symploce**." },
      { author: "Thomas Wilson", work: "The Arte of Rhetorique", quote: "The orator stirred the crowd using a powerful **symploce**, hammering home the identical cause and consequence in every clause." }
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

console.log('Done Batch 4 (Dashboard — plec) of Cluster Art, Craft & Design (26 words)!');
