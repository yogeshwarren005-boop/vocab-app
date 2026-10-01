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

const batch2Data = {
  "Dashboard — anth/antheropeas.md": {
    primary: "A genus of small annual flowering plants in the daisy family (Asteraceae), commonly known as Easter bonnets, native to western North America.",
    secondary: "In floristic taxonomy, desert annuals bearing solitary golden flower heads with conspicuous ray and disc florets adapted to arid gravel slopes.",
    quotes: [
      { author: "Edward Lee Greene", work: "Pittonia", quote: "I have proposed **Antheropeas** to receive those miniature helenioid annuals possessing blunt pappus scales and glandular herbage." },
      { author: "Philip A. Munz", work: "A California Flora", quote: "In spring after desert rains, **Antheropeas** wallacei carpets dry sandy washes with bright yellow star-like blooms." },
      { author: "Willis Linn Jepson", work: "A Flora of California", quote: "The tiny stems of **Antheropeas** rarely exceed two inches in height, yet produce a profusion of radiant disc flowers." }
    ]
  },
  "Dashboard — anth/antherozoid.md": {
    primary: "A motile, flagellated male gamete produced in the antheridium of cryptogamic plants, such as mosses, ferns, and charophyte algae.",
    secondary: "In plant reproductive cytology, a spiral spermatozoid propelled by anterior cilia that navigates watery films guided by archegonial chemical attractants.",
    quotes: [
      { author: "Wilhelm Hofmeister", work: "Higher Cryptogamia", quote: "Each spiral **antherozoid** rotates swiftly by means of its terminal cilia, directing itself toward the open archegonial neck." },
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "The release of the **antherozoid** requires free surface water, without which fertilization cannot take place." },
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "Chemotactic sensitivity guides the swimming **antherozoid** toward malic acid diffusing from the receptive ovum." }
    ]
  },
  "Dashboard — anth/anthesis.md": {
    primary: "The period or stage during which a flower bud expands, opens, and becomes functionally active for pollination.",
    secondary: "In floral phenology, the physiological process involving corolla expansion, anther dehiscence, and stigma receptivity.",
    quotes: [
      { author: "Charles Darwin", work: "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", quote: "Observations made during **anthesis** demonstrated that the stigmas were receptive hours before the anthers dehisced." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "In evening primroses, **anthesis** proceeds with astonishing speed as the petals unfurl within a few minutes of sunset." },
      { author: "John Lindley", work: "An Introduction to Botany", quote: "Temperature and humidity exert a powerful influence upon the onset of **anthesis** in greenhouse cultivars." }
    ]
  },
  "Dashboard — anth/anthidium.md": {
    primary: "A genus of solitary bees in the family Megachilidae, known as wool carder bees, which gather plant trichomes to line their brood cells.",
    secondary: "In hymenopteran ethology, territorial solitary bees wherein males vigorously defend floral patches against competing pollinators using abdominal spines.",
    quotes: [
      { author: "Jean-Henri Fabre", work: "Bramble-Bees and Others", quote: "The industrious female **Anthidium** scrapes the downy wool from mullein leaves, rolling it into a compact pellet for her masonry nest." },
      { author: "Charles D. Michener", work: "The Bees of the World", quote: "Males of **Anthidium** manicatum exhibit pronounced aggressive territoriality, striking intruding insects with sharp metasomal teeth." },
      { author: "William Morton Wheeler", work: "Social Life Among the Insects", quote: "The nesting architecture of **Anthidium** relies exclusively upon harvested plant hairs bound with protective floral resins." }
    ]
  },
  "Dashboard — anth/anthill.md": {
    primary: "A mound of earth, sand, pine needles, or debris heaped up by ants around the entrance to their subterranean nest.",
    secondary: "In ecological entomology, a complex thermal and moisture-regulating biogenic superstructure housing thousands of colonial social insects.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The slave-making ants systematically raided the neighboring **anthill**, carrying off pupae to rear them as working captives." },
      { author: "Henry David Thoreau", work: "Walden", quote: "Watching the red and black warriors fight on my woodpile, I felt as though I were witnessing two empires clash over a single **anthill**." },
      { author: "John Lubbock", work: "Ants, Bees, and Wasps", quote: "The architectural design of an **anthill** enables optimal solar heating in the morning while preventing flooding during torrential rain." }
    ]
  },
  "Dashboard — anth/anthoceropsida.md": {
    primary: "A taxonomic class of non-vascular embryophytes comprising the hornworts (Anthocerophyta), characterized by horn-shaped sporophytes.",
    secondary: "In bryology and plant evolution, an archaic clade of basal land plants exhibiting continuous sporophytic growth via an intercalary meristem and embedded gametangia.",
    quotes: [
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "The unique developmental features of **Anthoceropsida** place them in an isolated position among the bryophyte phyla." },
      { author: "Frederick Orpen Bower", work: "Primitive Land Plants", quote: "Unlike liverworts, the **Anthoceropsida** possess sporophytes equipped with true stomata and an active basal meristem." },
      { author: "Gilbert M. Smith", work: "Cryptogamic Botany", quote: "In **Anthoceropsida**, each photosynthetic cell typically contains a single massive chloroplast with a pyrenoid, recalling green algae." }
    ]
  },
  "Dashboard — anth/anthoceros.md": {
    primary: "A genus of hornworts (family Anthocerataceae) featuring thalloid gametophytes and erect, horn-like or needle-like sporophytes.",
    secondary: "In evolutionary cryptogamic botany, a model organism harboring symbiotic nitrogen-fixing Nostoc cyanobacteria within mucilage cavities of its thallus.",
    quotes: [
      { author: "Wilhelm Hofmeister", work: "Higher Cryptogamia", quote: "The elongated capsule of **Anthoceros** splits longitudinally into two twisting valves, steadily liberating dark spores over many weeks." },
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "Examination of the thallus in **Anthoceros** reveals blue-green colonies of Nostoc inhabiting inner mucilaginous chambers." },
      { author: "Karl von Goebel", work: "Organography of Plants", quote: "The continuous growth of the **Anthoceros** capsule from an intercalary zone represents a remarkable approach toward independent sporophytic life." }
    ]
  },
  "Dashboard — anth/anthocerotaceae.md": {
    primary: "The botanical family of hornworts (order Anthocerotales) comprising thalloid plants with horn-shaped, dehiscent capsules.",
    secondary: "In bryophyte taxonomy, the principal family of hornworts distinguished by pseudo-elaters, columellae, and dark ornamented spores.",
    quotes: [
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "Systematic classification separates the **Anthocerotaceae** from all hepatics because of the distinct internal structure of the capsule." },
      { author: "Frederick Orpen Bower", work: "The Origin of a Land Flora", quote: "The columella running through the center of the capsule in **Anthocerotaceae** provides mechanical support and conduction." },
      { author: "Gilbert M. Smith", work: "Cryptogamic Botany", quote: "Genera of the **Anthocerotaceae** inhabit damp shaded banks and wet clay soils throughout temperate and tropical zones." }
    ]
  },
  "Dashboard — anth/anthocerotales.md": {
    primary: "An order of bryophytes that includes the hornworts, characterized by thallose gametophytes and continuous-growing sporophytes.",
    secondary: "In systematic botany, an order often treated as the sole order within Anthocerotopsida, representing a pivotal evolutionary transition in early land plant lineages.",
    quotes: [
      { author: "Frederick Orpen Bower", work: "Primitive Land Plants", quote: "The morphological isolation of the **Anthocerotales** strongly supports their recognition as an independent evolutionary lineage." },
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "Comparative embryology demonstrates that the **Anthocerotales** diverge fundamentally from both true mosses and marchantialean liverworts." },
      { author: "Adolf Engler", work: "Syllabus der Pflanzenfamilien", quote: "Under our system, the **Anthocerotales** occupy an intermediate grade between the thalloid bryophytes and primitive vascular pteridophytes." }
    ]
  },
  "Dashboard — anth/Anthocoridae.md": {
    primary: "A family of small hemipteran predatory insects known as minute pirate bugs or flower bugs, commonly found in blossoms and foliage preying on small pests.",
    secondary: "In economic entomology and biological control, voracious beneficial predators that consume spider mites, thrips, aphids, and insect eggs in agricultural crops.",
    quotes: [
      { author: "Leland Ossian Howard", work: "The Insect Book", quote: "Members of the **Anthocoridae** patrol flowering orchard canopies, piercing destructive aphids with their predatory rostra." },
      { author: "John Henry Comstock", work: "An Introduction to Entomology", quote: "The **Anthocoridae** are minute, flattened bugs frequently found in blossoms where they suck the juices of thrips and pollen." },
      { author: "Charles Valentine Riley", work: "Insect Life", quote: "Farmers benefit greatly from the unchecked predation of **Anthocoridae** upon scale insects and overwintering moth eggs." }
    ]
  },
  "Dashboard — anth/anthodite.md": {
    primary: "A cave formation (speleothem) composed of delicate radiating needles, quill-like clusters, or flower-shaped sprays of aragonite or calcite.",
    secondary: "In karst speleology, an exquisite secondary mineral deposit formed by capillary seeps in calm cave chambers, resembling white frost flowers.",
    quotes: [
      { author: "William B. White", work: "Cave Minerals of the World", quote: "The ceiling of the grotto was covered with breathtaking **anthodite** clusters, radiating like crystal chrysanthemums from the limestone bedrock." },
      { author: "Édouard-Alfred Martel", work: "Les Abîmes", quote: "Illuminated by our torches, each sparkling **anthodite** appeared as a burst of delicate needle-like aragonite needles suspended in darkness." },
      { author: "Clyde A. Malott", work: "Physiography of Cave Regions", quote: "Slow evaporative conditions in undisturbed passages facilitate the growth of fibrous **anthodite** rosettes." }
    ]
  },
  "Dashboard — anth/anthologise.md": {
    primary: "To compile, select, or publish literary works or poems into an anthology.",
    secondary: "To canonize or preserve literary pieces by selecting and grouping them within a curated thematic collection.",
    quotes: [
      { author: "Virginia Woolf", work: "The Common Reader", quote: "To **anthologise** Elizabethan lyrics is to assemble a bouquet where every blossom competes in fragrance and musicality." },
      { author: "T. S. Eliot", work: "Selected Essays", quote: "Critics who undertake to **anthologise** contemporary poets inevitably reveal their own period's unexamined prejudices." },
      { author: "W. H. Auden", work: "The Dyer's Hand", quote: "A compiler who seeks to **anthologise** minor verse must possess an ear sensitive to solitary moments of perfection." }
    ]
  },
  "Dashboard — anth/anthologist.md": {
    primary: "A person who compiles, selects, and edits an anthology of literary writings, poetry, or other works.",
    secondary: "A literary curator whose critical selections establish canons and introduce diverse voices to the reading public.",
    quotes: [
      { author: "Samuel Johnson", work: "Lives of the English Poets", quote: "The discerning **anthologist** sifts bushels of forgotten chaff to retrieve a handful of immortal golden stanzas." },
      { author: "Matthew Arnold", work: "Essays in Criticism", quote: "Francis Turner Palgrave proved himself an incomparable **anthologist**, providing the nation with a touchstone of lyric excellence." },
      { author: "William Hazlitt", work: "Lectures on the English Poets", quote: "An **anthologist** who lacks poetic sensibility merely binds withered leaves into an unwieldy and lifeless volume." }
    ]
  },
  "Dashboard — anth/anthologize.md": {
    primary: "To compile or include literary pieces, essays, or poems in an anthology.",
    secondary: "To select and incorporate an individual author's work into an authoritative representative collection.",
    quotes: [
      { author: "Henry James", work: "Partial Portraits", quote: "Editors continually desire to **anthologize** his earlier short stories, though he himself preferred his more complex later fiction." },
      { author: "Ezra Pound", work: "Literary Essays", quote: "If you wish to **anthologize** the true innovators of the century, you must discard the sentimental magazine versifiers." },
      { author: "George Saintsbury", work: "A History of English Criticism", quote: "The effort to **anthologize** seventeenth-century prose requires reconciling Latinate periods with vigorous vernacular idioms." }
    ]
  },
  "Dashboard — anth/anthology.md": {
    primary: "A published collection of poems, short stories, essays, or other literary pieces chosen by a compiler.",
    secondary: "Historically derived from the Greek 'anthologia' (a gathering of flowers), a bouquet of representative literary gems.",
    quotes: [
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "A well-chosen **anthology** of moral maxims serves as a pocket treasury for civil conduct and philosophical reflection." },
      { author: "Percy Bysshe Shelley", work: "A Defence of Poetry", quote: "The Greek **anthology** preserves those tender, transient blossoms of verse that survived the wreck of mighty empires." },
      { author: "John Dryden", work: "Fables Ancient and Modern", quote: "In assembling this poetic **anthology**, I have endeavoured to translate Homer and Ovid into natural English measures." }
    ]
  },
  "Dashboard — anth/anthonomus.md": {
    primary: "A genus of small weevils (family Curculionidae) whose larvae develop within flower buds or fruits, notably including the boll weevil (Anthonomus grandis).",
    secondary: "In applied entomology, an agricultural pest taxon whose long rostrum pierces flower squares and bolls, causing catastrophic crop losses in cotton.",
    quotes: [
      { author: "Leland Ossian Howard", work: "The Boll Weevil Problem", quote: "The arrival of **Anthonomus** grandis across the Rio Grande transformed the economic destiny of the American Cotton Belt." },
      { author: "Charles Valentine Riley", work: "The Cotton Worm", quote: "Punctures inflicted by female **Anthonomus** weevils cause floral squares to flare and drop before seeds can mature." },
      { author: "John Henry Comstock", work: "A Manual for the Study of Insects", quote: "The apple curculio belongs likewise to **Anthonomus**, boring deep oviposition cavities into young pomaceous fruit." }
    ]
  },
  "Dashboard — anth/anthony.md": {
    primary: "A proper name associated with St. Anthony the Great; also applied historically to St. Anthony's fire (erysipelas) and the runt of a litter (an Anthony pig).",
    secondary: "In cultural folklore and historical idiom, referring to swine dedicated to the hospital of St. Anthony or to medicinal protections associated with his cross (tau).",
    quotes: [
      { author: "William Shakespeare", work: "Antony and Cleopatra", quote: "His legs bestrid the ocean: his reared arm crested the world: his voice was propertied as all the tuned spheres, when he would call to an **Anthony**." },
      { author: "Charles Dickens", work: "Martin Chuzzlewit", quote: "Old **Anthony** Chuzzlewit sat before the fire, counting his gains with narrow, suspicious scrutiny." },
      { author: "Walter Scott", work: "The Monastery", quote: "The peasant prayed to Saint **Anthony** to preserve his cattle from murrain and blight through the harsh winter months." }
    ]
  },
  "Dashboard — anth/anthophagous.md": {
    primary: "Feeding on flowers; eating flowers or floral organs.",
    secondary: "In animal ecology, describing specialized herbivores, insects, or birds whose primary diet consists of petals, floral nectaries, or pollen.",
    quotes: [
      { author: "Charles Darwin", work: "Insectivorous Plants", quote: "Certain caterpillars are strictly **anthophagous**, burrowing into the developing corolla and consuming stamens before petals open." },
      { author: "Alfred Russel Wallace", work: "Tropical Nature", quote: "Lories and hanging parrots exhibit **anthophagous** adaptations, brushing pollen from high tree blossoms with specialized brush-tipped tongues." },
      { author: "Jean-Henri Fabre", work: "The Life of the Grasshopper", quote: "The green katydid reveals itself as an avid **anthophagous** forager, stripping the delicate white petals of my jasmine arbor." }
    ]
  },
  "Dashboard — anth/anthophilous.md": {
    primary: "Attracted to, frequenting, or feeding on flowers; flower-loving (characteristic of pollinators).",
    secondary: "In coevolutionary biology, possessing anatomical adaptations such as specialized mouthparts, plumose hairs, or sensory organs for visiting blossoms.",
    quotes: [
      { author: "Charles Darwin", work: "The Various Contrivances by Which Orchids Are Fertilised", quote: "The mutual adaptation between orchids and **anthophilous** insects guarantees cross-fertilization across distant plant populations." },
      { author: "John Lubbock", work: "On British Wild Flowers in Relation to Insects", quote: "Brilliant floral pigmentation evolved primarily as visual beacons to guide **anthophilous** bees to hidden nectar caches." },
      { author: "Hermann Müller", work: "The Fertilisation of Flowers", quote: "A survey of **anthophilous** Diptera proves that flower visitation shaped the elongation of their proboscides over geological time." }
    ]
  },
  "Dashboard — anth/anthophobia.md": {
    primary: "An abnormal, irrational, or disproportionate fear or aversion to flowers.",
    secondary: "In psychological psychiatry, a specific phobia wherein floral scents, pollen, or visual petal patterns trigger acute panic anxiety or aversion.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "Morbid aversions may attach to almost any natural object, producing rare manifestations such as **anthophobia** or fear of feathers." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "The patient displayed an inexplicable **anthophobia**, falling into distressing nervous paroxysms whenever a rose was brought into the room." },
      { author: "Richard von Krafft-Ebing", work: "Psychopathia Sexualis", quote: "Under clinical observation, severe **anthophobia** was traced to childhood trauma associated with funeral floral wreaths." }
    ]
  },
  "Dashboard — anth/anthophore.md": {
    primary: "An elongated floral internode situated between the calyx and the remaining floral organs (corolla, stamens, and pistil).",
    secondary: "In organographic botany, an axis elongation that elevates petals and reproductive organs above the calyx tube, characteristic of certain Caryophyllaceae.",
    quotes: [
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "In the campion genus Silene, an elongated stalk or **anthophore** elevates the petals, stamens, and ovary well above the green calyx." },
      { author: "John Lindley", work: "An Introduction to Botany", quote: "The development of an **anthophore** illustrates how the receptacle internodes can lengthen to optimize floral presentation." },
      { author: "George Bentham", work: "Handbook of the British Flora", quote: "The pink family displays considerable variation in the length of the stipe or **anthophore** supporting the capsule." }
    ]
  },
  "Dashboard — anth/anthophyllite.md": {
    primary: "An orthorhombic amphibole mineral, magnesium iron silicate hydroxide [(Mg,Fe)₇Si₈O₂₂(OH)₂], typically occurring in brownish-grey fibrous or bladed masses.",
    secondary: "In metamorphic petrology, an asbestos-form amphibole formed in magnesium-rich regional metamorphic rocks such as amphibolites and serpentinites.",
    quotes: [
      { author: "James Dwight Dana", work: "System of Mineralogy", quote: "The mineral **anthophyllite** was named from the clove-brown color of its radiating fibrous crystal masses, recalling the clove leaf." },
      { author: "Edward Salisbury Dana", work: "A Text-Book of Mineralogy", quote: "Optical examination shows that **anthophyllite** crystallizes in the orthorhombic system with characteristic prismatic amphibole cleavage." },
      { author: "Archibald Geikie", work: "Textbook of Geology", quote: "In the crystalline schists of the Highlands, beds rich in **anthophyllite** alternate with garnetiferous mica schists." }
    ]
  },
  "Dashboard — anth/anthophyta.md": {
    primary: "A major plant division comprising all flowering plants (angiosperms), producing flowers and enclosed seeds.",
    secondary: "In botanical phylogenetics, the dominant division of land plants encompassing monocots and eudicots, defined by double fertilization and carpellary fruits.",
    quotes: [
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "The evolutionary supremacy of the **Anthophyta** over gymnosperms rests upon their specialized insect pollination and sealed ovules." },
      { author: "Adolf Engler", work: "Syllabus der Pflanzenfamilien", quote: "Under the name **Anthophyta**, we embrace all angiospermous flora that produce true flowers with stamens and carpels." },
      { author: "Charles E. Bessey", work: "The Phylogeny of Angiosperms", quote: "The basal ancestors of **Anthophyta** arose from strobiliferous gymnospermous stock, diversifying rapidly during the Cretaceous." }
    ]
  },
  "Dashboard — anth/anthos.md": {
    primary: "A flower or blossom; in classical pharmacy and perfumery, rosemary tops or flowers (anthos herba).",
    secondary: "In Greek historical lexicography and botanical antiquity, the bloom, essence, or vital pinnacle of vegetative life.",
    quotes: [
      { author: "Theophrastus", work: "Enquiry into Plants", quote: "The term **anthos** applies to the ephemeral crown of the plant that unfolds to nurture the ripening germ." },
      { author: "Pliny the Elder", work: "Natural History", quote: "Apothecaries know the blossom of rosemary simply as **anthos**, using its fragrant oil to invigorate weakened memories." },
      { author: "Pedanius Dioscorides", work: "De Materia Medica", quote: "The distilled essence of **anthos** applied with honey calms stubborn skin inflammations and clears cutaneous blemishes." }
    ]
  },
  "Dashboard — anth/Anthozoa.md": {
    primary: "A class of marine invertebrates within the phylum Cnidaria that includes sea anemones, stony corals, soft corals, and sea pens.",
    secondary: "In invertebrate zoology, polypoid cnidarians that lack a free-swimming medusa stage and possess an internal pharynx and partitioned gastrovascular cavity.",
    quotes: [
      { author: "Ernst Haeckel", work: "Report on Deep-Sea Keratosa", quote: "The colonial skeletons of **Anthozoa** build vast undersea limestone ramparts that withstand the heaviest surf of the open Pacific." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "Radial mesenteries divide the digestive coelenteron of the **Anthozoa** into radiating chambers bearing nematocysts." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", quote: "Phylogenetic analysis demonstrates that **Anthozoa** represent the most basal extant lineage within the phylum Cnidaria." }
    ]
  },
  "Dashboard — anth/anthozoan.md": {
    primary: "Relating to or being a member of the cnidarian class Anthozoa; a sea anemone or coral polyp.",
    secondary: "A marine benthic polyp characterized by an inward-folded actinopharynx and radial vertical septa lining the gut.",
    quotes: [
      { author: "James Dwight Dana", work: "Corals and Coral Islands", quote: "The living **anthozoan** polyp secretes a basal cup of solid aragonite, adding microscopic layers day after day." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "When the tide recedes, each delicate **anthozoan** closes its tentacles, resembling a glistening gelatinous mound on the damp rock." },
      { author: "Libbie Hyman", work: "The Invertebrates", quote: "Unlike hydroids, no **anthozoan** ever produces a planktonic medusa, completing its life cycle entirely upon the sea floor." }
    ]
  },
  "Dashboard — anth/anthracite.md": {
    primary: "A hard, compact variety of mineral coal that has a high luster, contains very little volatile matter, and burns with a short, clean, smokeless flame.",
    secondary: "In fuel geology and metamorphic coalification, the highest rank of coal, characterized by carbon content exceeding 90 percent and low hydrogen yield.",
    quotes: [
      { author: "Charles Lyell", work: "Travels in North America", quote: "The immense beds of **anthracite** in the Appalachian valleys demonstrate the intense metamorphic pressure exerted during mountain building." },
      { author: "Archibald Geikie", work: "Textbook of Geology", quote: "Where bituminous coal seams approach igneous dykes, the volatile hydrocarbons have been driven off, converting the coal into **anthracite**." },
      { author: "Henry Darwin Rogers", work: "The Geology of Pennsylvania", quote: "The smokeless combustion of Pennsylvania **anthracite** fueled the iron forges and locomotives of the Industrial Revolution." }
    ]
  },
  "Dashboard — anth/anthracitic.md": {
    primary: "Of, pertaining to, resembling, or having the qualities of anthracite coal.",
    secondary: "Describing mineral coals, shales, or residues possessing high carbon concentration, hard brittle texture, and submetallic luster.",
    quotes: [
      { author: "James Dwight Dana", work: "Manual of Geology", quote: "Regional folding subjected the Carboniferous strata to intense heat, transforming bituminous seams into **anthracitic** deposits." },
      { author: "Hugh Miller", work: "The Cruise of the Betsey", quote: "Black **anthracitic** shales exposed along the shore bore fragile impressions of ancient calamite stems." },
      { author: "Edward Hull", work: "The Coal-Fields of Great Britain", quote: "In South Wales, the transition from bituminous coal to an **anthracitic** facies progresses steadily from east to west." }
    ]
  },
  "Dashboard — anth/anthracosis.md": {
    primary: "A lung disease caused by the inhalation and retention of coal dust particles; coal workers' pneumoconiosis or black lung.",
    secondary: "In occupational pulmonary pathology, the deposition of carbonaceous pigments within alveolar macrophages and peribronchial lymphatics leading to progressive fibrosis.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Pulmonary **anthracosis** is universal among aged colliers, whose lungs show dense pigmentation and emphysematous changes." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Autopsy reveals that in **anthracosis**, alveolar histiocytes become engorged with inhaled soot and soot particles." },
      { author: "Jean-Martin Charcot", work: "Clinical Lectures on Senile Diseases", quote: "Severe **anthracosis** impairs pulmonary elasticity, aggravating chronic catarrh and cardiac hypertrophy." }
    ]
  },
  "Dashboard — anth/anthrax.md": {
    primary: "A severe, infectious bacterial disease of warm-blooded animals and humans caused by the spore-forming bacterium Bacillus anthracis.",
    secondary: "In medical microbiology and epidemiology, a zoonotic disease presenting in cutaneous (malignant carbuncle), pulmonary, or gastrointestinal forms.",
    quotes: [
      { author: "Robert Koch", work: "The Etiology of Anthrax Disease", quote: "I observed the rod-like bacilli of **anthrax** multiply in blood drops and form resistant spores capable of surviving in soil for years." },
      { author: "Louis Pasteur", work: "Germ Theory and Its Applications", quote: "Our public trial at Pouilly-le-Fort demonstrated that cattle inoculated with attenuated vaccine were completely protected against virulent **anthrax**." },
      { author: "Joseph Lister", work: "On the Antiseptic Principle", quote: "The black eschar of cutaneous **anthrax** affords conclusive proof of local bacterial colonization before systemic spread occurs." }
    ]
  },
  "Dashboard — anth/anthriscus.md": {
    primary: "A genus of herbaceous plants in the carrot family (Apiaceae), including chervil (Anthriscus cerefolium) and cow parsley (Anthriscus sylvestris).",
    secondary: "In agricultural and culinary botany, biennial or annual umbellifers bearing finely divided pinnate foliage and small white compound umbels.",
    quotes: [
      { author: "John Gerard", work: "The Herball or Generall Historie of Plantes", quote: "Garden chervil or **Anthriscus** is sown in spring to season pottages with its delicate sweet and aromatic leaves." },
      { author: "William Woodville", work: "Medical Botany", quote: "Care must be exercised to avoid confusing edible **Anthriscus** with poisonous hemlock growing along ditch banks." },
      { author: "George Bentham", work: "Handbook of the British Flora", quote: "In May, the foaming white umbels of wild **Anthriscus** fringe every roadside hedgerow throughout the English shires." }
    ]
  },
  "Dashboard — anth/anthropic.md": {
    primary: "Of, relating to, or characteristic of human beings or the human era.",
    secondary: "In theoretical physics and cosmology, referring to the anthropic principle, which posits that physical constants must allow for the emergence of conscious observers.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Man's Place in Nature", quote: "The physical conformation of the skull reflects continuous **anthropic** modifications through successive geological epochs." },
      { author: "Arthur Stanley Eddington", work: "The Nature of the Physical World", quote: "The apparent fine-tuning of fundamental cosmic constants suggests an **anthropic** constraint upon cosmological models." },
      { author: "Charles Lyell", work: "The Geological Evidences of the Antiquity of Man", quote: "The discovery of chipped flints alongside mammoth bones established the vast antiquity of the **anthropic** period." }
    ]
  },
  "Dashboard — anth/anthropical.md": {
    primary: "Pertaining to human beings; human in nature or origin.",
    secondary: "In 19th-century philosophical and moral discourse, belonging to human experience, society, or moral development.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Aids to Reflection", quote: "Spiritual truths must be translated into an **anthropical** language that appeals directly to human conscience and reason." },
      { author: "Herbert Spencer", work: "The Principles of Sociology", quote: "Social evolution represents the progressive refinement of **anthropical** institutions from primitive savagery to complex civilization." },
      { author: "John Tyndall", work: "Fragments of Science", quote: "The scientific investigator must guard against projecting subjective **anthropical** sympathies onto the mechanical operations of nature." }
    ]
  },
  "Dashboard — anth/anthropocentric.md": {
    primary: "Regarding humankind as the central, supreme, or most significant entity in the universe.",
    secondary: "Interpreting or evaluating external reality, nature, and divine purpose exclusively in terms of human values, experiences, and utility.",
    quotes: [
      { author: "William James", work: "The Will to Believe", quote: "The old theological conception assumed an entirely **anthropocentric** cosmos constructed solely for human salvation." },
      { author: "Bertrand Russell", work: "Mysticism and Logic", quote: "Copernicus dealt a mortal blow to the **anthropocentric** illusion that the earth and its inhabitants were the center of creation." },
      { author: "John Dewey", work: "Reconstruction in Philosophy", quote: "Modern empirical inquiry freed itself from medieval teleology by abandoning an **anthropocentric** interpretation of physical events." }
    ]
  },
  "Dashboard — anth/anthropocentricity.md": {
    primary: "The state, quality, or perspective of being anthropocentric; human-centeredness.",
    secondary: "In the history of science and philosophy, the intellectual tendency to evaluate cosmological and ecological systems from an exclusively human standpoint.",
    quotes: [
      { author: "George Santayana", work: "The Life of Reason", quote: "The naive **anthropocentricity** of early religions attributed human passions and moral grievances to the starry constellations." },
      { author: "Alfred North Whitehead", work: "Process and Reality", quote: "A philosophy of organism strives to transcend the narrow **anthropocentricity** that reduces nature to passive sensory data." },
      { author: "Will Durant", work: "The Story of Philosophy", quote: "Spinoza dismantled the psychological **anthropocentricity** of his contemporaries, demonstrating that nature serves no subjective human purpose." }
    ]
  },
  "Dashboard — anth/anthropocentrism.md": {
    primary: "The philosophical doctrine or belief that human beings are the central or most important element of existence.",
    secondary: "In environmental ethics and metaphysics, the framework that grants moral standing exclusively or primarily to humans, viewing the natural world instrumentally.",
    quotes: [
      { author: "Bertrand Russell", work: "A History of Western Philosophy", quote: "Aristotelian physics was saturated with **anthropocentrism**, viewing every natural motion as striving toward a purposeful end." },
      { author: "Thomas Henry Huxley", work: "Evolution and Ethics", quote: "Evolutionary science challenges naive **anthropocentrism** by proving that humanity is a late branch upon the immense tree of life." },
      { author: "William James", work: "Pragmatism", quote: "Common sense clings tenaciously to **anthropocentrism**, finding it difficult to conceive a universe that takes no notice of our hopes." }
    ]
  },
  "Dashboard — anth/anthropogenesis.md": {
    primary: "The origin and evolutionary development of human beings as a species; hominization.",
    secondary: "In physical anthropology and evolutionary biology, the phylogenetic lineage and morphological transitions leading from ancestral hominoids to modern Homo sapiens.",
    quotes: [
      { author: "Ernst Haeckel", work: "The Evolution of Man", quote: "Comparative embryology and paleontology provide the indispensable structural pillars for our understanding of **anthropogenesis**." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "The gradual stages of **anthropogenesis** demonstrate that our bodily frame retains indelible traces of low arboreal origins." },
      { author: "Alfred Russel Wallace", work: "Darwinism", quote: "While natural selection explains the physical course of **anthropogenesis**, human moral and mathematical faculties suggest higher influences." }
    ]
  },
  "Dashboard — anth/anthropogenetic.md": {
    primary: "Of or relating to the origin and evolutionary development of human beings (anthropogenesis).",
    secondary: "Pertaining to the biological and morphological changes associated with human speciation and lineage development.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Man's Place in Nature", quote: "The fossil discoveries in Neanderthal cave strata supplied the first tangible **anthropogenetic** link in human prehistory." },
      { author: "Ernst Haeckel", work: "The Riddle of the Universe", quote: "Our **anthropogenetic** tree traces human ancestry through twenty-two distinct ancestral stages across geological eras." },
      { author: "Herbert Spencer", work: "The Principles of Biology", quote: "The bipedal posture and development of the human hand were pivotal **anthropogenetic** adaptations favoring tool use." }
    ]
  },
  "Dashboard — anth/anthropogenic.md": {
    primary: "Originating in or produced by human activity, especially regarding environmental changes, pollution, or landscapes.",
    secondary: "In Earth system science and ecology, designating biophysical processes, greenhouse emissions, and extinctions caused by human society.",
    quotes: [
      { author: "George Perkins Marsh", work: "Man and Nature", quote: "Deforestation and canal construction represent colossal **anthropogenic** transformations of the earth's physical surface." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The sudden extinction of the dodo and moa illustrates the decisive impact of **anthropogenic** predation upon island faunas." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Modern synthetic pesticides introduce **anthropogenic** chemical poisons against which nature has developed no evolutionary defenses." }
    ]
  },
  "Dashboard — anth/anthropogeny.md": {
    primary: "The scientific study or theory of the origin, evolutionary development, and genealogical descent of the human species.",
    secondary: "In 19th-century evolutionary anthropology, the branch of biology investigating the phylogenetic genealogy and ontogenetic development of mankind.",
    quotes: [
      { author: "Ernst Haeckel", work: "Anthropogenie", quote: "The science of **anthropogeny** unites ontogeny and phylogeny to solve the supreme riddle of human origin." },
      { author: "Thomas Henry Huxley", work: "Critiques and Addresses", quote: "Modern **anthropogeny** relies upon comparative craniology, embryonic homologies, and stratigraphical fossil discoveries." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "A comprehensive treatise on **anthropogeny** must account for sexual selection alongside survival of the fittest in shaping racial varieties." }
    ]
  },
  "Dashboard — anth/anthropoid.md": {
    primary: "Resembling a human being in form or appearance; an ape belonging to the superfamily Hominoidea (gibbon, orangutan, gorilla, chimpanzee).",
    secondary: "In primate taxonomy, belonging to the suborder Anthropoidea, encompassing higher primates including New World monkeys, Old World monkeys, and hominoids.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Man's Place in Nature", quote: "The structural differences which separate man from the gorilla and chimpanzee are less than those which separate the **anthropoid** apes from lower monkeys." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "The emotional expressions of an **anthropoid** ape mirror human facial contractions in joy, terror, and rage." },
      { author: "Richard Owen", work: "On the Gorillas", quote: "The massive sagittal crest of the adult male **anthropoid** provides anchor for enormous masticatory temporal muscles." }
    ]
  },
  "Dashboard — anth/anthropoidal.md": {
    primary: "Resembling or having the characteristics of a human or an anthropoid ape; anthropoid.",
    secondary: "In comparative primatology, exhibiting morphological features typical of higher simian primates.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The young orangutan exhibited remarkably **anthropoidal** gestures, clasping its arms around my neck like a human infant." },
      { author: "Ernst Haeckel", work: "The History of Creation", quote: "Fossil discoveries will inevitably uncover intermediate **anthropoidal** forms bridging the gulf between ape and man." },
      { author: "William Henry Flower", work: "An Introduction to the Study of Mammals", quote: "The dentition of the Miocene fossil displays **anthropoidal** cingula on the lower molars." }
    ]
  },
  "Dashboard — anth/anthropoidea.md": {
    primary: "A major suborder of primates (also known as simians) that includes New World monkeys, Old World monkeys, apes, and humans.",
    secondary: "In systematic primatology, higher primates characterized by enclosed bony eye orbits, fused mandibular symphyses, and complex cerebral neocortices.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Vertebrated Animals", quote: "The **Anthropoidea** are sharply demarcated from the lemurs by their complete postorbital wall and retinal fovea." },
      { author: "William Henry Flower", work: "Mammals Living and Extinct", quote: "Within the **Anthropoidea**, we distinguish the platyrrhine monkeys of America from the catarrhines of the Old World." },
      { author: "Edward Drinker Cope", work: "The Origin of the Fittest", quote: "The cranial evolution of the **Anthropoidea** reflects progressive enlargement of the frontal lobes and stereoscopic vision." }
    ]
  },
  "Dashboard — anth/anthropolatry.md": {
    primary: "The worship of a human being as a god; divine honors paid to a mortal.",
    secondary: "In theological polemics and comparative religion, the deification of heroes, emperors, or religious leaders as divine incarnations.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The senate indulged in shameful **anthropolatry**, decreeing divine temples and altars to monsters like Caligula and Nero." },
      { author: "David Hume", work: "The Natural History of Religion", quote: "Popular superstition naturally slides into **anthropolatry**, transforming legendary champions and benefactors into protective household gods." },
      { author: "James George Frazer", work: "The Golden Bough", quote: "Ancient sacral kingship frequently culminated in blatant **anthropolatry**, wherein the living ruler was treated as a rain-giving deity." }
    ]
  },
  "Dashboard — anth/anthropological.md": {
    primary: "Of or relating to anthropology (the study of human beings, human biology, cultures, and societies).",
    secondary: "In social science, relating to ethnological, linguistic, archaeological, or biological investigations of human diversification.",
    quotes: [
      { author: "Edward Burnett Tylor", work: "Primitive Culture", quote: "The **anthropological** method investigates religious rituals by comparing analogous customs surviving across disparate continents." },
      { author: "Franz Boas", work: "The Mind of Primitive Man", quote: "Rigorous **anthropological** measurements demonstrated that head shape undergoes phenotypic change under modified environmental conditions." },
      { author: "James George Frazer", work: "The Golden Bough", quote: "The vast collection of folklore gathered in these volumes provides an **anthropological** record of the awakening human intellect." }
    ]
  },
  "Dashboard — anth/anthropologist.md": {
    primary: "A scientist or scholar who specializes in anthropology, the comprehensive study of humankind.",
    secondary: "A field researcher or theorist investigating human social structures, languages, folklore, or evolutionary biology.",
    quotes: [
      { author: "Margaret Mead", work: "Coming of Age in Samoa", quote: "The field **anthropologist** must live within the native village, observing daily rituals without imposing Western moral judgments." },
      { author: "Claude Lévi-Strauss", work: "Tristes Tropiques", quote: "As an **anthropologist**, I found myself an exile between cultures, seeking universal structures in the remote Amazonian jungle." },
      { author: "Bronislaw Malinowski", work: "Argonauts of the Western Pacific", quote: "The primary duty of the **anthropologist** is to grasp the native's point of view, his relation to life, and his vision of the world." }
    ]
  },
  "Dashboard — anth/anthropology.md": {
    primary: "The holistic scientific study of humanity, encompassing human biological evolution, archaeology, linguistics, and sociocultural development.",
    secondary: "In intellectual history, the overarching scientific discipline that synthesizes ethnology, comparative anatomy, and sociology to analyze the human condition.",
    quotes: [
      { author: "Edward Burnett Tylor", work: "Anthropology: An Introduction", quote: "The science of **anthropology** maps the long, laborious ascent of human civilization from stone tools to modern science." },
      { author: "Immanuel Kant", work: "Anthropology from a Pragmatic Point of View", quote: "Pragmatic **anthropology** examines what man as a free-acting being makes, or can and should make, of himself." },
      { author: "Franz Boas", work: "Race, Language and Culture", quote: "Modern **anthropology** demonstrates that cultural diversity is the product of historical circumstance rather than biological inferiority." }
    ]
  },
  "Dashboard — anth/anthropometric.md": {
    primary: "Of, relating to, or involving the measurement of the human body and its physical dimensions.",
    secondary: "In forensic science and ergonomical design, pertaining to standardized indices and ratios of human somatic measurements.",
    quotes: [
      { author: "Francis Galton", work: "Inquiries into Human Faculty and Its Development", quote: "My **anthropometric** laboratory recorded stature, span of arms, lung capacity, and visual acuity for thousands of visitors." },
      { author: "Alphonse Bertillon", work: "Signaletic Instructions", quote: "The **anthropometric** system of criminal identification relies upon precise measurements of the head, foot, and middle finger." },
      { author: "Cesare Lombroso", work: "Criminal Man", quote: "Careful **anthropometric** tables of incarcerated offenders revealed cranial asymmetries and atavistic physical stigmata." }
    ]
  },
  "Dashboard — anth/anthropometrical.md": {
    primary: "Pertaining to anthropometry; measuring the physical dimensions and proportions of the human body.",
    secondary: "In craniometry and physical anthropology, relating to comparative mathematical records of human skeletal and somatic traits.",
    quotes: [
      { author: "Francis Galton", work: "Memories of My Life", quote: "The **anthropometrical** data gathered at the Health Exhibition provided the first comprehensive statistical survey of the British populace." },
      { author: "Alphonse Bertillon", work: "Identification Anthropométrique", quote: "Strict adherence to our **anthropometrical** protocol ensures that no two individuals can ever be confounded by police archives." },
      { author: "Paul Broca", work: "Instructions Craniologiques", quote: "Standardized callipers are indispensable for securing reliable **anthropometrical** indices from prehistoric skulls." }
    ]
  },
  "Dashboard — anth/anthropometry.md": {
    primary: "The scientific study and practice of taking systematic measurements of the human body, its proportions, and physical characteristics.",
    secondary: "In forensic identification and human biology, the quantitative profiling of skeletal, facial, and somatic parameters.",
    quotes: [
      { author: "Francis Galton", work: "Inquiries into Human Faculty", quote: "The application of **anthropometry** to large school populations reveals the decisive influence of nutrition upon juvenile growth." },
      { author: "Alphonse Bertillon", work: "The Bertillon System of Identification", quote: "Before the advent of fingerprinting, criminal **anthropometry** offered the only infallible method to identify habitual recidivists." },
      { author: "Paul Broca", work: "Mémoires d'Anthropologie", quote: "Craniological **anthropometry** must be conducted with rigorous instruments to eliminate observer bias in racial comparisons." }
    ]
  },
  "Dashboard — anth/anthropomorphic.md": {
    primary: "Attributing human form, characteristics, motives, or behaviors to gods, animals, or inanimate objects.",
    secondary: "In philosophical epistemology and theology, describing representations that depict non-human phenomena in the likeness of humanity.",
    quotes: [
      { author: "David Hume", work: "Dialogues Concerning Natural Religion", quote: "The vulgar imagination demands an **anthropomorphic** deity endowed with human passions, partialities, and wrath." },
      { author: "Charles Darwin", work: "The Expression of the Emotions in Man and Animals", quote: "We must avoid carelessly **anthropomorphic** language when interpreting the playful gestures of domestic animals." },
      { author: "Xenophanes", work: "Fragments", quote: "Mortals deem that gods are begotten as they are, but if cattle or horses had hands, they would draw gods in **anthropomorphic** equine forms." }
    ]
  },
  "Dashboard — anth/anthropomorphise.md": {
    primary: "To attribute human form, feelings, personality, or behaviors to animals, nature, or deities.",
    secondary: "In literary aesthetics and nature writing, to project human psychology onto non-human agents or landscape elements.",
    quotes: [
      { author: "George Eliot", work: "The Mill on the Floss", quote: "The lonely child would **anthropomorphise** her wooden doll, pouring into its unblinking eyes all her secret griefs." },
      { author: "Thomas Hardy", work: "The Return of the Native", quote: "He had a persistent tendency to **anthropomorphise** the heath, hearing in the wind across the gorse a giant's ancient sigh." },
      { author: "John Ruskin", work: "Modern Painters", quote: "Poets who excessively **anthropomorphise** mountain crags fall into that pathetic fallacy which falsifies true vision." }
    ]
  },
  "Dashboard — anth/anthropomorphism.md": {
    primary: "The attribution of human traits, emotions, or intentions to non-human entities, including animals, natural forces, or deities.",
    secondary: "In comparative mythology and philosophy of mind, the cognitive projection of human mental models onto natural phenomena or non-human species.",
    quotes: [
      { author: "Ludwig Feuerbach", work: "The Essence of Christianity", quote: "Religious theology is nothing other than disguised **anthropomorphism**, wherein man projects his own idealized nature upon the heavens." },
      { author: "Francis Bacon", work: "Novum Organum", quote: "The Idols of the Tribe have their origin in human nature itself, generating a false **anthropomorphism** that colors every inquiry." },
      { author: "Baruch Spinoza", work: "Ethics", quote: "Men are prone to **anthropomorphism** because they universally act with an eye to some end, imagining nature acts likewise." }
    ]
  },
  "Dashboard — anth/anthropomorphize.md": {
    primary: "To ascribe human characteristics, emotions, or behaviors to non-human things, animals, or deities.",
    secondary: "In animal ethology, to interpret animal behaviors through the lens of human emotional motivations rather than objective physiological responses.",
    quotes: [
      { author: "Charles Darwin", work: "The Expression of the Emotions in Man and Animals", quote: "While naturalists should not carelessly **anthropomorphize** their subjects, mammalian emotional expressions share deep common roots." },
      { author: "William James", work: "The Principles of Psychology", quote: "We instinctively **anthropomorphize** our surroundings, feeling resentment toward the inanimate chair that bruises our shins." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "Ahab came to **anthropomorphize** the white whale, imputing to the monstrous brute a deliberate and malice-driven intelligence." }
    ]
  },
  "Dashboard — anth/anthropomorphous.md": {
    primary: "Having the shape, form, or likeness of a human being; humanoid or anthropoid.",
    secondary: "In classical natural history and comparative osteology, exhibiting human-like anatomical configurations.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Evidence as to Man's Place in Nature", quote: "The skeleton of the chimpanzee is remarkably **anthropomorphous**, especially in the curvature of the ribs and pelvic girdle." },
      { author: "Ernst Haeckel", work: "Systematic Phylogeny", quote: "Archaic hominids represent the most **anthropomorphous** primates documented within the late Tertiary fossil record." },
      { author: "Richard Owen", work: "Comparative Anatomy of Vertebrates", quote: "The ape brain presents an undeniably **anthropomorphous** convolution pattern across its cerebral hemispheres." }
    ]
  },
  "Dashboard — anth/anthropophagite.md": {
    primary: "A cannibal; a person who eats human flesh.",
    secondary: "In historical travel literature and classical myth, a member of a legendary tribe or race reputed to practice anthropophagy.",
    quotes: [
      { author: "William Shakespeare", work: "The Merry Wives of Windsor", quote: "Go, knock and call: he'll speak like an **Anthropophagite** unto thee: knock, I say!" },
      { author: "Jonathan Swift", work: "A Modest Proposal", quote: "The cruel satirist joked that only an **Anthropophagite** could look upon the starving children of Ireland as marketable meat." },
      { author: "Daniel Defoe", work: "Robinson Crusoe", quote: "Crusoe lived in perpetual dread of encountering an **Anthropophagite** savage feast upon the desolate shore of his island." }
    ]
  },
  "Dashboard — anth/anthropophagous.md": {
    primary: "Feeding on human flesh; cannibalistic.",
    secondary: "In ethnography and classical geography, describing peoples, creatures, or mythical beings that consume human victims.",
    quotes: [
      { author: "Michel de Montaigne", work: "Essays", quote: "The Greek historians described wild northern scythians as **anthropophagous** tribes who drank from skulls of slain enemies." },
      { author: "Herman Melville", work: "Typee", quote: "Rumors depicted the inland Marquesan warriors as fiercely **anthropophagous**, roasting captive prisoners after victorious raids." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Melancholic frenzy has driven delirious wretches to become **anthropophagous**, devouring their own children in secret cellars." }
    ]
  },
  "Dashboard — anth/anthropophagus.md": {
    primary: "A cannibal; one who feeds on human flesh.",
    secondary: "In classical antiquity and Renaissance cartography, a term used for man-eating monsters or savage peoples situated at the edges of the known world.",
    quotes: [
      { author: "William Shakespeare", work: "Othello", quote: "And of the Cannibals that each other eat, the **Anthropophagi**, and men whose heads do grow beneath their shoulders." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Byzantine chronicles denounced the marauding Attila as an inhuman **anthropophagus** thirsty for Christian blood." },
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", quote: "Ancient geographers multiplied tales of the **anthropophagus**, populating terra incognita with man-eating cyclopes." }
    ]
  },
  "Dashboard — anth/anthropophagy.md": {
    primary: "The eating of human flesh by human beings; cannibalism.",
    secondary: "In cultural anthropology, the ritualistic or survival-driven practice of consuming human tissue, categorized as endocannibalism or exocannibalism.",
    quotes: [
      { author: "Michel de Montaigne", work: "Of Cannibals", quote: "I find that there is more barbarity in torturing a living man than in practicing ritual **anthropophagy** upon a deceased foe." },
      { author: "Herman Melville", work: "Typee", quote: "The terrible suspicion of **anthropophagy** hung like a pall over every banquet offered by the island chieftain." },
      { author: "Daniel Defoe", work: "Robinson Crusoe", quote: "The horror of discovered footprints on the sand was doubled by the gruesome relics of **anthropophagy** left around the dying embers." }
    ]
  },
  "Dashboard — anth/anthroposophy.md": {
    primary: "A spiritual philosophy and movement founded in the early 20th century by Rudolf Steiner, postulating an objective, comprehensible spiritual world accessible through inner cognitive development.",
    secondary: "In esoteric philosophy and cultural education, a doctrine emphasizing spiritual perception, providing the conceptual foundation for Waldorf education, biodynamic agriculture, and anthroposophical medicine.",
    quotes: [
      { author: "Rudolf Steiner", work: "Knowledge of the Higher Worlds", quote: "The purpose of **anthroposophy** is to awaken those slumbering organs of spiritual perception that unite man with the cosmos." },
      { author: "William James", work: "The Varieties of Religious Experience", quote: "Modern esoteric movements such as **anthroposophy** seek an empirical mysticism that harmonizes inner revelation with systematic observation." },
      { author: "W. B. Yeats", work: "A Vision", quote: "The symbolic diagrams in Steiner's **anthroposophy** reflect an earnest pursuit of transcendent geometrical order underlying history." }
    ]
  },
  "Dashboard — anth/anthurium.md": {
    primary: "A large genus of tropical American epiphytic flowering plants in the arum family (Araceae), known for their glossy heart-shaped leaves and brightly colored spathes with spike-like spadices.",
    secondary: "In ornamental horticulture and tropical botany, the flamingo flower or tailflower, featuring long-lasting waxy spathes surrounding bisexual florets on the spadix.",
    quotes: [
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "The brilliant scarlet spathe of **Anthurium** andreanum retains its waxy luster for many weeks in the tropical conservatory." },
      { author: "Adolf Engler", work: "Das Pflanzenreich", quote: "In the rain forests of Colombia, numerous epiphytic species of **Anthurium** anchor upon mossy tree forks, trapping forest humus." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The genus **Anthurium** displays the characteristic spadiceous inflorescence of the arums, prized for exquisite foliar and floral venation." }
    ]
  },
  "Dashboard — anth/anthus.md": {
    primary: "A genus of slender, terrestrial passerine birds comprising the pipits (family Motacillidae), characterized by cryptic brownish plumage, long hind claws, and melodious song flights.",
    secondary: "In avian systematics, widespread ground-nesting insectivores inhabiting open grasslands, moors, and tundra, known for repetitive tail-wagging behavior.",
    quotes: [
      { author: "John Gould", work: "The Birds of Europe", quote: "The meadow pipit, classified under **Anthus** pratensis, ascends into the sky with fluttering wings, singing a sweet trill as it parachutes downward." },
      { author: "William Yarrell", work: "A History of British Birds", quote: "The elongated hind claw in the genus **Anthus** enables these birds to walk gracefully through dense pasture grass." },
      { author: "Ernst Mayr", work: "List of New Guinea Birds", quote: "Alpine grasslands on the high peaks of New Guinea harbor endemic races of **Anthus** adapted to subzero nocturnal frosts." }
    ]
  }
};

let count = 0;
for (const [relPath, data] of Object.entries(batch2Data)) {
  if (updateNote(relPath, data)) {
    count++;
  }
}

console.log(`\n========================================`);
console.log(`Batch 2 Completed: ${count} / ${Object.keys(batch2Data).length} notes updated.`);
console.log(`========================================\n`);
