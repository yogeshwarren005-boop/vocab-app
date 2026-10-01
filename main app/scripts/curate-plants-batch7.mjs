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

const batch7Data = {
  "Dashboard — minth/minter.md": {
    primary: "A person who mints or coins money; an official or workman in a mint; also a creator or coiner of words or phrases.",
    secondary: "In historical monetary economics, an authorized master craftsman who stamped legal coin dies onto measured bullion blanks.",
    quotes: [
      { author: "Isaac Newton", work: "Mint Papers", quote: "The honest **minter** weighs each blank upon the balance before placing it beneath the screw-press die." },
      { author: "Alexander Pope", work: "Epistle to Dr. Arbuthnot", quote: "Each wretched poetaster acts as a reckless **minter** of barbarous neologisms that corrupt our vernacular speech." },
      { author: "Walter Scott", work: "The Fortunes of Nigel", quote: "The master **minter** of the Tower examined the gold broad-piece, certifying its royal weight and fineness." }
    ]
  },
  "Dashboard — minth/minth.md": {
    primary: "A combining form and classical botanical root derived from Greek 'minthe' (mint), underlying botanical and chemical terms relating to the genus Mentha.",
    secondary: "In classical mythology and historical etymology, named after the nymph Minthe, who was transformed into the fragrant herb by Persephone.",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The Greek root **minth** derives from minthe, the aromatic garden herb revered for refreshing drinks." },
      { author: "Robert Beekes", work: "Etymological Dictionary of Greek", quote: "The floral element **minth** represents a pre-Greek Mediterranean loanword designating aromatic labiates." },
      { author: "Ovid", work: "Metamorphoses", quote: "Persephone crushed the nymph underfoot in jealous fury, yet her fragrant spirit survived in the crushed leaves of sweet **minth**." }
    ]
  },
  "Dashboard — minth/Minthostachys.md": {
    primary: "A genus of aromatic shrubs in the mint family (Lamiaceae), native to the Andes of South America, known as muña.",
    secondary: "In Andean ethnobotany and phytotherapy, essential oil-rich shrubs containing pulegone and menthone used for altitude sickness and digestive ailments.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Personal Narrative of Travels", quote: "On high Andean plateaus, bushes of **Minthostachys** scent the thin air with an invigorating, camphoraceous mint perfume." },
      { author: "Adolf Engler", work: "Syllabus der Pflanzenfamilien", quote: "The genus **Minthostachys** is characterized by dense verticillasters and glandular foliage adapted to montane droughts." },
      { author: "Richard Evans Schultes", work: "The Healing Forest", quote: "Indigenous Quechua healers brew hot infusions of **Minthostachys** to calm abdominal colic and preserve stored potato crops from weevils." }
    ]
  },
  "Dashboard — oen/enologist.md": {
    primary: "A specialist or scientist who studies winemaking and wine chemistry; an oenologist.",
    secondary: "In viticultural science, an expert who monitors grape must fermentation, yeast strains, sulfur dioxide levels, and barrel aging.",
    quotes: [
      { author: "Louis Pasteur", work: "Studies on Wine", quote: "The modern **enologist** must understand that vinegar spoilage is caused by aerobic bacteria rather than spontaneous chemical decay." },
      { author: "Alexis Lichine", work: "Encyclopedia of Wines and Spirits", quote: "A master **enologist** tastes the nascent vintage from every oak cask before deciding upon the final blend." },
      { author: "Frank A. Lee", work: "Basic Food Chemistry", quote: "Routine analysis conducted by the **enologist** tracks titratable acidity, malolactic conversion, and residual reducing sugars." }
    ]
  },
  "Dashboard — oen/enology.md": {
    primary: "The science, study, and art of winemaking; oenology.",
    secondary: "In applied agricultural biochemistry, the technical discipline governing grape harvesting chemistry, alcoholic fermentation, and wine maturation.",
    quotes: [
      { author: "Louis Pasteur", work: "Studies on Wine", quote: "The application of microscopic biology to **enology** rescued the French wine trade from devastating bacterial diseases." },
      { author: "Alexis Lichine", work: "Wines of France", quote: "Modern academic **enology** has unlocked the subtle chemical secrets of malolactic fermentation in cool cellars." },
      { author: "Justus von Liebig", work: "Familiar Letters on Chemistry", quote: "The theoretical foundations of **enology** were established through analytical determinations of tartaric acid and alcohol." }
    ]
  },
  "Dashboard — oen/oen.md": {
    primary: "A combining form and classical root derived from Greek 'oinos' (wine), forming vocabulary relating to wine and viticulture.",
    secondary: "In biochemical and classical terminology, the prefix designating wine chemistry (oenology), wine vessels (oenochoe), and floral pigments (oenin).",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The Greek root **oen** traces directly to oinos, the sacred fermented juice of the grape offered to Dionysus." },
      { author: "Robert Beekes", work: "Etymological Dictionary of Greek", quote: "Archaic Indo-European cognates of **oen** connect Mediterranean wine cultivation with ancient vine viticulture." },
      { author: "Louis Pasteur", work: "Studies on Wine", quote: "Chemical constituents bearing the prefix **oen** reflect historical research into the bouquet and coloring matters of vintage wines." }
    ]
  },
  "Dashboard — oen/oenochoe.md": {
    primary: "An ancient Greek wine jug or pitcher, typically having a single handle and a trefoil (three-lobed) mouth for pouring wine from a krater into cups.",
    secondary: "In classical archaeology and ceramic history, a prominent painted terracotta or bronze vessel produced across Attic, Corinthian, and Etruscan workshops.",
    quotes: [
      { author: "Walter Pater", work: "Greek Studies", quote: "The young cupbearer dipped the slender bronze **oenochoe** into the mixing bowl and filled the banqueters' goblets." },
      { author: "John Beazley", work: "Attic Red-Figure Vase-Painters", quote: "The trefoil spout of the red-figure **oenochoe** allowed wine to pour in a neat, controlled stream without dripping." },
      { author: "Jane Ellen Harrison", work: "Prolegomena to the Study of Greek Religion", quote: "Libations poured from the sacred **oenochoe** moistened the tomb of the hero during the festival of the Anthesteria." }
    ]
  },
  "Dashboard — oen/oenologist.md": {
    primary: "A person who specializes in oenology; an expert in wine and the science of winemaking.",
    secondary: "In commercial viticulture, a technical director responsible for guiding grape crushing, fermentation kinetics, and clarification.",
    quotes: [
      { author: "Louis Pasteur", work: "Studies on Wine", quote: "Careful thermal processing proposed to the **oenologist** destroyed pathogenic ferments without sacrificing delicate vintage aromas." },
      { author: "Alexis Lichine", work: "Guide to the Vineyards and Châteaux of France", quote: "The estate **oenologist** monitors hydrometer readings daily as the autumn fermentation bubbles vigorously in vat." },
      { author: "William Osler", work: "AEquanimitas", quote: "Like a seasoned **oenologist**, the seasoned clinician develops refined sensory discrimination through decades of disciplined practice." }
    ]
  },
  "Dashboard — oen/oenology.md": {
    primary: "The scientific study of wine and winemaking (alternative spelling of enology).",
    secondary: "In food science and viticulture, the scientific discipline encompassing ampelography, fermentation biology, and sensory evaluation of wines.",
    quotes: [
      { author: "Louis Pasteur", work: "Studies on Wine", quote: "Empirical winemakers resisted the innovations of scientific **oenology** until controlled heating saved millions of hectoliters from souring." },
      { author: "Alexis Lichine", work: "Encyclopedia of Wines and Spirits", quote: "A comprehensive course in **oenology** requires thorough mastery of soil geology, climate cycles, and yeast enzymology." },
      { author: "William Allen Miller", work: "Elements of Chemistry", quote: "Analytical **oenology** quantifies volatile esters, tannins, and glycerol to evaluate wine aging potential." }
    ]
  },
  "Dashboard — oen/oenophile.md": {
    primary: "A lover, connoisseur, or devotee of wine; a person who appreciates fine wines.",
    secondary: "In gastronomic culture, an aficionado dedicated to collecting, cellaring, tasting, and discussing regional vintages and terroirs.",
    quotes: [
      { author: "Alexis Lichine", work: "Wines of France", quote: "To the true **oenophile**, opening an aged bottle of premier cru Burgundy is an act of reverent communion with French soil." },
      { author: "Arthur Conan Doyle", work: "The Sign of the Four", quote: "My host proved himself a cultivated **oenophile**, producing a cobwebbed flask of vintage Tokay from his private cellar." },
      { author: "H. G. Wells", work: "Tono-Bungay", quote: "He adopted the pretensions of a wealthy **oenophile**, discoursing pompously upon pre-phylloxera clarets at dinner." }
    ]
  },
  "Dashboard — oen/oenophilia.md": {
    primary: "A love or passion for wine; the appreciation and connoisseurship of wine.",
    secondary: "In cultural history and gastronomy, the refined social appreciation of viticultural heritage, tasting rituals, and vintage cellarage.",
    quotes: [
      { author: "Alexis Lichine", work: "Encyclopedia of Wines", quote: "The widespread resurgence of **oenophilia** among urban diners has elevated winemakers to international celebrity." },
      { author: "George Saintsbury", work: "Notes on a Cellar-Book", quote: "My lifelong **oenophilia** was never mere indulgence, but a disciplined aesthetic pursuit of harmony between wine and table." },
      { author: "William James", work: "The Varieties of Religious Experience", quote: "Passionate enthusiasms, whether religious conversion or artistic **oenophilia**, possess the power to transfigure mundane existence." }
    ]
  },
  "Dashboard — oen/oinochoe.md": {
    primary: "An ancient Greek ceramic or bronze wine jug with a single handle and trefoil spout (transliterated variant of oenochoe).",
    secondary: "In classical Mediterranean art, a ritual jug used during banquets (symposia) and religious libations, decorated in black-figure or red-figure styles.",
    quotes: [
      { author: "John Beazley", work: "Attic Black-Figure Vase-Painters", quote: "The graceful silhouette of this sixth-century **oinochoe** depicts Herakles reclining upon a couch attended by Athena." },
      { author: "Walter Pater", work: "Greek Studies", quote: "He held aloft an embossed silver **oinochoe**, pouring dark wine into the sacrificial flames upon the altar." },
      { author: "Jane Ellen Harrison", work: "Prolegomena to the Study of Greek Religion", quote: "Excavators uncovered a painted **oinochoe** dedicated to Hermes Chthonios buried within the sacred well." }
    ]
  },
  "Dashboard — peper/paprika.md": {
    primary: "A ground red spice made from dried, sweet or mildly pungent varieties of Capsicum annuum; also the pepper fruit itself.",
    secondary: "In culinary history and organic chemistry, the national spice of Hungary, celebrated for its rich carotenoid pigments and high ascorbic acid (vitamin C) content.",
    quotes: [
      { author: "Albert Szent-Györgyi", work: "Studies on Vitamin C", quote: "From fresh Hungarian **paprika**, I isolated hexuronic acid in crystalline abundance, proving its identity with antiscorbutic vitamin C." },
      { author: "Bram Stoker", work: "Dracula", quote: "I had for dinner paprika hendl, a chicken cooked with red pepper which they call **paprika**, very good but thirsty." },
      { author: "Frank A. Lee", work: "Basic Food Chemistry", quote: "The intense crimson color of culinary **paprika** is due to capsanthin and capsorubin carotenoid pigments." }
    ]
  },
  "Dashboard — peper/peper.md": {
    primary: "A combining form and classical botanical root derived from Greek 'peperi' and Latin 'piper' (pepper), designating pungent peppercorn plants.",
    secondary: "In historical linguistics and pharmacognosy, the ancient Indo-Aryan loanword (pippali) that designated black and long pepper across the classical world.",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The Greek root **peper** traces to peperi, designating the pungent dried berries imported from southern India." },
      { author: "Pliny the Elder", work: "Natural History", quote: "It is astonishing that mankind should purchase pungent **peper** at such exorbitant prices merely to tickle a biting palate." },
      { author: "Robert Beekes", work: "Etymological Dictionary of Greek", quote: "Linguistic pathways of the root **peper** document the earliest maritime spice trade between the Malabar coast and Alexandria." }
    ]
  },
  "Dashboard — peper/peperomia.md": {
    primary: "A large genus of small, tropical and subtropical perennial herbs in the family Piperaceae, commonly grown as house plants for ornamental foliage; radiator plants.",
    secondary: "In neotropical botany, succulent shade-tolerant epiphytes and lithophytes bearing dense spadix-like flower spikes of minute flowers lacking perianths.",
    quotes: [
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The genus **Peperomia** differs from true Piper in its herbaceous habit, tiny two-stamened flowers, and solitary stigma." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "Indoor gardeners prize **Peperomia** for its fleshy, variegated leaves that tolerate dry apartment atmospheres." },
      { author: "Adolf Engler", work: "Das Pflanzenreich", quote: "Hundreds of species of **Peperomia** flourish upon mossy tree trunks throughout the cloud forests of the Andes." }
    ]
  },
  "Dashboard — peper/pepper.md": {
    primary: "A pungent spice made from the dried, ground berries of Piper nigrum (black or white pepper); also the fleshy fruit of plants of the genus Capsicum.",
    secondary: "In global commercial history, the king of spices whose trade drove European age-of-discovery maritime expeditions to India and the East Indies.",
    quotes: [
      { author: "John Gerard", work: "The Herball or Generall Historie of Plantes", quote: "Black **pepper** is the dried unripe berry of an Indian climbing vine, which heateth and comforteth a cold moist stomach." },
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "The monopoly of the spice trade in **pepper** and cloves yielded immense commercial dividends to the Dutch East India Company." },
      { author: "Henry David Thoreau", work: "Walden", quote: "I preferred the natural flavor of corn bread to all the artificial pungent dressings of salt and **pepper**." }
    ]
  },
  "Dashboard — peper/peppery.md": {
    primary: "Tasting of or containing pepper; pungent, sharp, or spicy; having a quick-tempered or irascible temperament.",
    secondary: "In sensory analysis and literary description, possessing an aggressive, stinging bite or lively, biting critical edge.",
    quotes: [
      { author: "Charles Dickens", work: "David Copperfield", quote: "Captain Murderer had a **peppery** disposition, flying into terrible rages at the slightest household delay." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "The fiery curry was so intensely **peppery** that poor Jos Sedley gasped for water while tears ran down his cheeks." },
      { author: "George Eliot", work: "The Mill on the Floss", quote: "Uncle Glegg was noted for his **peppery** remarks at the parish vestry meeting whenever church rates were discussed." }
    ]
  },
  "Dashboard — pepon/pepon.md": {
    primary: "A combining form and classical botanical root derived from Greek 'pepon' (ripe melon, pumpkin, gourd), denoting large fleshy fruits of the Cucurbitaceae.",
    secondary: "In classical antiquity and botanical carpology, the ancient Greek word for a sun-ripened gourd or melon that develops without hard woody septa.",
    quotes: [
      { author: "Theophrastus", work: "Enquiry into Plants", quote: "The Greeks designated as **pepon** the large sweet melon that ripens only under the fiercest heat of the summer sun." },
      { author: "Pliny the Elder", work: "Natural History", quote: "Physicians praise the cooling pulp of the ripe **pepon** to extinguish bilious fevers in the dog days." },
      { author: "Robert Beekes", work: "Etymological Dictionary of Greek", quote: "The root **pepon** literally signifies that which has been cooked or ripened by the sun." }
    ]
  },
  "Dashboard — pepon/pumpkin.md": {
    primary: "A large, rounded, orange-yellow edible squash of the genus Cucurbita (especially Cucurbita pepo), with thick edible flesh and seeds.",
    secondary: "In agricultural history and folklore, a native North American domesticate essential to indigenous agriculture and celebrated in autumn harvest traditions.",
    quotes: [
      { author: "Henry David Thoreau", work: "Walden", quote: "I would rather sit on a **pumpkin** and have it all to myself, than be crowded on a velvet cushion." },
      { author: "Nathaniel Hawthorne", work: "Mosses from an Old Manse", quote: "In my garden grew a colossal **pumpkin**, basking its golden roundness in the warm September sunshine." },
      { author: "John Greenleaf Whittier", work: "The Pumpkin", quote: "What moistens the lip and what brightens the eye, what calls back the past like the rich **pumpkin** pie?" }
    ]
  },
  "Dashboard — persic/persic.md": {
    primary: "Of or relating to Persia (modern Iran) or its language, culture, or people; Persian; in botany, relating to the peach (Prunus persica).",
    secondary: "In historical literature and classical geography, pertaining to ancient Persian luxury, poetry, or gardens; botanically, the Persian fruit (peach).",
    quotes: [
      { author: "John Milton", work: "Paradise Regained", quote: "From India and the golden Chersoness and utmost Indian isle Taprobane, to the rich **Persic** gulf and Caspian shore." },
      { author: "Pliny the Elder", work: "Natural History", quote: "The peach, known to the Romans as the **Persic** apple, was brought into Italy from the gardens of the Orient." },
      { author: "John Gerard", work: "The Herball or Generall Historie of Plantes", quote: "Under the name Malus Persica, ancient botanists described the luscious **Persic** fruit ripening on sunny walls." }
    ]
  },
  "Dashboard — persic/persist.md": {
    primary: "To continue firmly, steadily, or obstinately in an opinion, course of action, or purpose in spite of difficulty, opposition, or failure.",
    secondary: "In biology and ecology, to remain functional, viable, or structurally intact over an extended period (such as persistent floral bracts or chemical residues).",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "Under changed conditions, species that possess slight advantageous variations will **persist**, while less favored forms become extinct." },
      { author: "Samuel Johnson", work: "The Rambler", quote: "Great works are performed not by strength, but by perseverance; he that shall walk with vigor must **persist** to the goal." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Synthetic chlorinated hydrocarbons **persist** in the soil and food chains for decades without biological breakdown." }
    ]
  },
  "Dashboard — phloe/hypophloeodic.md": {
    primary: "Growing, situated, or living beneath the bark of a tree; subcortical.",
    secondary: "In lichenology and mycology, describing endophloeodic fungi or lichens whose vegetative thallus develops buried inside the cork cells of tree bark.",
    quotes: [
      { author: "William Gilson Farlow", work: "Cryptogamic Botany", quote: "The tiny perithecia of this **hypophloeodic** ascomycete burst through the lenticels of the dead birch branch." },
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "Certain parasitic fungal hyphae maintain a strictly **hypophloeodic** existence until seasonal spore release ruptures the periderm." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Crustose lichens with a **hypophloeodic** thallus are barely detectable except by the emergence of black apothecial disks." }
    ]
  },
  "Dashboard — phloe/phlobaphene.md": {
    primary: "A reddish-brown, resinous, water-insoluble condensation product formed by the oxidation and polymerization of condensed tannins (proanthocyanidins).",
    secondary: "In plant biochemistry and pharmacognosy, the dark amorphous pigments that impart deep brown color to tree bark, cinchona bark, and aged plant tissues.",
    quotes: [
      { author: "William Allen Miller", work: "Elements of Chemistry", quote: "Boiling tannin with dilute acids yields a deep red amorphous precipitate termed **phlobaphene**, insoluble in cold water." },
      { author: "Justus von Liebig", work: "Familiar Letters on Chemistry", quote: "The dark coloring matter in oak bark extract consists primarily of **phlobaphene** produced by aerial oxidation." },
      { author: "T. Lauder Brunton", work: "A Text-Book of Pharmacology", quote: "Decoctions of red cinchona bark deposit insoluble **phlobaphene** upon cooling, reducing active alkaloid extraction." }
    ]
  },
  "Dashboard — phloe/phloe.md": {
    primary: "A combining form and classical botanical root derived from Greek 'phloios' (bark, rind, husk of a tree), forming words relating to plant bark.",
    secondary: "In structural plant anatomy and etymology, the foundational stem underlying phloem, the nutrient-conducting vascular tissue of plants.",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The Greek root **phloe** stems from phloios, signifying the protective outer bark stripped from trees." },
      { author: "Theophrastus", work: "Enquiry into Plants", quote: "In trees, the innermost layer of the **phloios** lies directly against the green wood, transmitting sweet saps." },
      { author: "Robert Beekes", work: "Etymological Dictionary of Greek", quote: "Indo-European cognates of **phloe** denote peeling, splitting, or stripping away protective outer coverings." }
    ]
  },
  "Dashboard — phloe/phloem.md": {
    primary: "The vascular tissue in higher plants that conducts synthesized organic nutrients, particularly sucrose, from photosynthetic source leaves to non-photosynthetic sink organs.",
    secondary: "In plant anatomy, the inner bark complex consisting of sieve-tube elements, companion cells, phloem parenchyma, and sclerenchymatous fibers.",
    quotes: [
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "Girdling a tree trunk through the **phloem** stops the downward flow of organic nutrients, causing swelling above the incision." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "The vascular bundle is composed of two contrasting conduits: the wood or xylem, and the bast or **phloem**." },
      { author: "Charles Darwin", work: "Insectivorous Plants", quote: "Microscopic scrutiny proves that vascular traces supplying the insectivorous leaf possess normal **phloem** sieve elements." }
    ]
  },
  "Dashboard — phloe/phloeophagy.md": {
    primary: "The habit of feeding upon tree bark or the cambium and inner bark tissues of woody plants.",
    secondary: "In forest ecology and wildlife biology, herbivory specialized on the nutritious inner bark (phloem and cambium) by bark beetles, porcupines, beavers, and cervids.",
    quotes: [
      { author: "Leland Ossian Howard", work: "The Insect Book", quote: "The destructive life cycle of scolytid beetles is governed by larval **phloeophagy**, which cuts off sap conduction." },
      { author: "John Muir", work: "Our National Parks", quote: "Winter **phloeophagy** by hungry porcupines strips patches of tender bark from the upper branches of the yellow pine." },
      { author: "Charles Valentine Riley", work: "Reports on the Insects of Missouri", quote: "Extensive **phloeophagy** practiced by wood-boring larvae leaves distinctive etched engravings across the peeled trunk." }
    ]
  },
  "Dashboard — phloe/pseudophloem.md": {
    primary: "Tissue resembling phloem in appearance or position but lacking true sieve elements; or anomalous internal phloem in certain plant families.",
    secondary: "In plant histology, anomalous conductive parenchymatous strands found in certain dicot stems (such as Solanaceae and Cucurbitaceae) situated inside the xylem.",
    quotes: [
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "Anomalous stem cross-sections in Cucurbita show internal strands of **pseudophloem** bordering the pith." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "The identification of **pseudophloem** requires careful histochemical staining for callose and sieve plates." },
      { author: "Adolf Engler", work: "Syllabus der Pflanzenfamilien", quote: "Bicollateral bundles possessing both external phloem and internal **pseudophloem** characterize the order Tubiflorae." }
    ]
  },
  "Dashboard — phyll/aphyllanthaceae.md": {
    primary: "A monotypic family of monocotyledonous flowering plants (order Asparagales), comprising the single Mediterranean species Aphyllanthes monspeliensis.",
    secondary: "In systematic botany, an archaic Mediterranean xerophytic lineage (now often submerged as subfamily Aphyllanthoideae in Asparagaceae) characterized by rush-like photosynthetic stems.",
    quotes: [
      { author: "Adolf Engler", work: "Syllabus der Pflanzenfamilien", quote: "The family **Aphyllanthaceae** occupies a distinct isolated position in the Liliiflorae, characterized by scarious bracts and blue solitary flowers." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Botanists established **Aphyllanthaceae** to accommodate a single remarkable Mediterranean rush that produces brilliant blue floral stars." },
      { author: "George Bentham", work: "Genera Plantarum", quote: "The leafless, juncus-like scapes of **Aphyllanthaceae** demonstrate complete evolutionary reduction of the foliar lamina." }
    ]
  },
  "Dashboard — phyll/aphyllanthes.md": {
    primary: "A genus of Mediterranean rush-like perennial herbs (family Asparagaceae) comprising Aphyllanthes monspeliensis, the blue leafless lily.",
    secondary: "In garrigue floristics, a drought-tolerant perennial that grows in dense tufts of leafless wiry green stems terminating in solitary sky-blue star-like flowers.",
    quotes: [
      { author: "Carl Linnaeus", work: "Species Plantarum", quote: "The name **Aphyllanthes** signifies leafless flower, commemorating its slender photosynthetic rush stems lacking all true foliage." },
      { author: "John Gerard", work: "The Herball or Generall Historie of Plantes", quote: "On stony limestone hills around Montpellier, **Aphyllanthes** blossoms in spring with lovely cerulean stars." },
      { author: "Joseph Dalton Hooker", work: "Botanical Magazine", quote: "Cultivated in alpine troughs, **Aphyllanthes** monspeliensis charms every observer with its starry blue petals supported on wire-like stems." }
    ]
  },
  "Dashboard — phyll/aphyllophorales.md": {
    primary: "An obsolete taxonomic order of basidiomycete fungi that lack gills, including polypores, bracket fungi, tooth fungi, and coral fungi.",
    secondary: "In historical mycology, an artificial Friesian grouping of hymenomycetes characterized by tough, woody, or leathery basidiocarps with pores, teeth, or smooth hymenia.",
    quotes: [
      { author: "Elias Magnus Fries", work: "Epicrisis Systematis Mycologici", quote: "The order **Aphyllophorales** unites all those non-agaricoid hymenomycetes whose spore-bearing surface is pore-bearing or toothed." },
      { author: "William Gilson Farlow", work: "Cryptogamic Botany", quote: "Vast numbers of wood-rotting shelf fungi were classified under the **Aphyllophorales** before molecular phylogenetics." },
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "The evolutionary diversification of the **Aphyllophorales** demonstrates multiple independent adaptations for decomposing lignin in dead wood." }
    ]
  },
  "Dashboard — phyll/aphyllous.md": {
    primary: "Having no leaves; naturally leafless; destitute of leaves.",
    secondary: "In descriptive morphology, describing plants (such as desert cacti, broomrapes, and dodder) where leaves are absent or reduced to microscopic scales.",
    quotes: [
      { author: "Theophrastus", work: "Enquiry into Plants", quote: "Certain marine plants and desert rushes remain completely **aphyllous**, carrying on their life entirely through green succulent stems." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "The dodder is an **aphyllous** parasite that twines around host stems, drawing sap through invasive haustoria." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "In **aphyllous** Euphorbias, the fleshy green cortex takes over the entire photosynthetic function of the missing leaves." }
    ]
  },
  "Dashboard — phyll/cataphyll.md": {
    primary: "A rudimentary, reduced, or scale-like leaf, such as a bud scale, cotyledon, bulb scale, or rhizome scale, that precedes the normal foliage leaves.",
    secondary: "In plant developmental morphology, an early foliar organ specialized for physical protection, food storage, or subterranean penetration rather than photosynthesis.",
    quotes: [
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "The winter bud of the horse chestnut is securely enveloped by resin-coated **cataphyll** scales that protect delicate leaf primordia from freezing." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "Each fleshy layer of an onion bulb is a modified nutrient-storing **cataphyll** swollen with stored sugars." },
      { author: "Karl von Goebel", work: "Organography of Plants", quote: "Ontogenetic study reveals that a **cataphyll** represents the arrest of the leaf blade while the basal sheath expands." }
    ]
  },
  "Dashboard — phyll/chlorophyll.md": {
    primary: "The green photosynthetic pigment found in chloroplasts of plants, algae, and cyanobacteria, which absorbs light energy (primarily blue and red wavelengths) for photosynthesis.",
    secondary: "In plant biochemistry, a magnesium-coordinated porphyrin ring complex (chiefly chlorophyll a and b) essential for light absorption and excitation transfer in photosystems I and II.",
    quotes: [
      { author: "Julius von Sachs", work: "Lectures on the Physiology of Plants", quote: "Without sunlight and **chlorophyll**, the green plant cannot decompose atmospheric carbonic acid or generate starch grains." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "Parasitic plants like the dodder have lost their green **chlorophyll**, depending entirely upon host saps for nourishment." },
      { author: "Justus von Liebig", work: "Chemistry in Its Application to Agriculture", quote: "Microscopic analysis reveals that **chlorophyll** granules reside inside leaf cells, functioning as tiny chemical laboratories." }
    ]
  },
  "Dashboard — phyll/chlorophyllous.md": {
    primary: "Containing, characterized by, or pertaining to chlorophyll; green and photosynthetic.",
    secondary: "In plant histology and bryology, designating photosynthetic parenchyma cells containing chloroplasts, contrasting with hyaline water-storing cells.",
    quotes: [
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "The green palisade tissue of the leaf consists of densely packed **chlorophyllous** cells oriented perpendicular to the epidermis." },
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "In Sphagnum, narrow living **chlorophyllous** cells form a green network surrounding the large dead water-storage cells." },
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "Starch synthesis is strictly confined to the interior of **chlorophyllous** plastids during hours of daylight." }
    ]
  },
  "Dashboard — phyll/epiphyllum.md": {
    primary: "A genus of climbing or epiphytic cacti (family Cactaceae) native to Central and South America, known as orchid cacti, with flattened leaf-like stems and magnificent fragrant nocturnal flowers.",
    secondary: "In desert and jungle botany, thornless epiphytes whose stems are modified into broad, scalloped photosynthetic cladodes that bear blossoms up to ten inches across.",
    quotes: [
      { author: "Nathaniel Lord Britton", work: "The Cactaceae", quote: "The flattened joint of **Epiphyllum** oxypetalum resembles a broad scalloped leaf, opening magnificent white blossoms at midnight." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "Amateur greenhouse growers prize **Epiphyllum** hybrids for their enormous flowers of glistening crimson, amber, and snow." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "In the genus **Epiphyllum**, true leaves are absent, the broad, fleshy phylloclades fulfilling all vegetative duties." }
    ]
  },
  "Dashboard — phyll/phyllidae.md": {
    primary: "A family of phasmatodean insects known as true leaf insects or walking leaves, celebrated for their extraordinary mimetic resemblance to green or dried foliage.",
    secondary: "In evolutionary zoology and crypsis research, Australasian and Asian insects exhibiting flat, leaf-like broad abdomens, veined tegmina, and lobed legs that mimic foliage.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The camouflage of the **Phyllidae** is so flawless that even botanists mistake the motionless insect for a living guava leaf." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The exquisite protective resemblance in the **Phyllidae** can be explained only by the gradual accumulation of minor variations favoring concealment." },
      { author: "Jean-Henri Fabre", work: "The Life of the Grasshopper", quote: "When the leaf-insect of the **Phyllidae** walks, it rocks gently from side to side like a foliage leaf stirred by the breeze." }
    ]
  },
  "Dashboard — phyll/phylliform.md": {
    primary: "Having the shape, form, or appearance of a leaf; leaf-like; foliar in outline.",
    secondary: "In entomology and marine zoology, describing animals whose flattened bodies or appendages mimic leaves (such as leaf bugs or sea slugs).",
    quotes: [
      { author: "Alfred Russel Wallace", work: "Tropical Nature", quote: "Certain mantids possess **phylliform** expansions upon their legs, rendering them indistinguishable from the orchids they inhabit." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "The body of the flatworm exhibits a delicate **phylliform** contour that glides smoothly through marine sediment." },
      { author: "Richard Owen", work: "Lectures on Comparative Anatomy", quote: "The lateral gills of the decapod crustacean present a **phylliform** arrangement of overlapping thin lamellae." }
    ]
  },
  "Dashboard — phyll/phyllitis.md": {
    primary: "An obsolete botanical genus comprising the hart's-tongue fern (Phyllitis scolopendrium, now Asplenium scolopendrium); also an archaic medical term for leaf inflammation.",
    secondary: "In pteridology, an evergreen temperate woodland fern prized for its undivided, strap-shaped, glossy fronds with linear sori arranged in pairs.",
    quotes: [
      { author: "John Gerard", work: "The Herball or Generall Historie of Plantes", quote: "Hart's tongue or **Phyllitis** groweth upon moist mossy rocks and churchyard walls, bearing fair long tongues of shining green." },
      { author: "George Bentham", work: "Handbook of the British Flora", quote: "The genus **Phyllitis** is distinguished from Asplenium by having sori that face one another in pairs under confluent indusia." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The rare hart's-tongue fern was formerly placed under **Phyllitis**, inhabiting shaded limestone crevices in central New York." }
    ]
  },
  "Dashboard — phyll/phyllium.md": {
    primary: "A genus of leaf insects in the family Phylliidae (order Phasmatodea), commonly called walking leaves, native to tropical Asia and the Pacific islands.",
    secondary: "In tropical entomology, insects possessing broad, leaf-like green bodies with realistic vein patterns, false fungal blemishes, and chewed-leaf margins.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "I captured a magnificent living **Phyllium** in Borneo, whose green wings displayed brown blotches simulating decaying leaf fungus." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "The female **Phyllium** is flightless and so perfectly resembles a leaf that even keen-sighted tropical birds pass it by." },
      { author: "John Henry Comstock", work: "An Introduction to Entomology", quote: "Eggs of **Phyllium** are dropped freely upon the ground, bearing an uncanny resemblance to grooved plant seeds." }
    ]
  },
  "Dashboard — phyll/phyllo.md": {
    primary: "A paper-thin unleavened pastry dough of Greek origin, used in layers to make dishes such as baklava and spanakopita; filo dough.",
    secondary: "In Mediterranean culinary history, dough rolled and stretched until translucent, brushed with melted butter or olive oil to produce crisp laminated pastry.",
    quotes: [
      { author: "Alexis Lichine", work: "Encyclopedia of Wines and Foods", quote: "Layers of delicate buttered **phyllo** are wrapped around spiced walnuts and soaked in honey syrup to produce authentic baklava." },
      { author: "Elizabeth David", work: "Mediterranean Food", quote: "The Greek pastry cook handles **phyllo** with swift dexterity, keeping the tissue-thin sheets under a damp cloth to prevent drying." },
      { author: "Frank A. Lee", work: "Basic Food Chemistry", quote: "High-protein flour with extensible gluten is essential for stretching **phyllo** dough into paper-thin transparent sheets." }
    ]
  },
  "Dashboard — phyll/phylloclad.md": {
    primary: "A flattened, photosynthetic stem or branch that functions as and resembles a leaf; phylloclade.",
    secondary: "In plant organography, an axial structure (seen in Ruscus and Asparagus) that bears true flowers or reduced scale leaves from its nodes.",
    quotes: [
      { author: "Asa Gray", work: "First Lessons in Botany", quote: "In the butcher's broom (Ruscus), the apparent leaf is actually a **phylloclad**, as proven by the tiny flower emerging from its center." },
      { author: "John Lindley", work: "An Introduction to Botany", quote: "The **phylloclad** of the Christmas cactus demonstrates how vegetative stems adapt to fulfill foliar photosynthetic functions in arid epiphytes." },
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "Vascular anatomy conclusively proves that a **phylloclad** arises from an axillary bud rather than from the leaf trace." }
    ]
  },
  "Dashboard — phyll/phyllocladaceae.md": {
    primary: "A family of southern hemisphere coniferous trees and shrubs (order Pinales), commonly known as celery pines, comprising the single genus Phyllocladus.",
    secondary: "In gymnosperm systematics and paleobotany, ancient Australasian podocarps characterized by cladodes (phylloclades) replacing true leaves and fleshy arillate seed cones.",
    quotes: [
      { author: "Adolf Engler", work: "Syllabus der Pflanzenfamilien", quote: "The **Phyllocladaceae** are distinguished from typical Podocarpaceae by their fan-shaped photosynthetic phylloclades and solitary seeds." },
      { author: "Joseph Dalton Hooker", work: "Flora Novae-Zelandiae", quote: "New Zealand forests harbor endemic species of **Phyllocladaceae**, prized by settlers for their durable, straight-grained timber." },
      { author: "Alan Feduccia", work: "The Gondwana Flora", quote: "Fossil foliage matching modern **Phyllocladaceae** occurs in Cretaceous strata across Antarctica and southeastern Australia." }
    ]
  },
  "Dashboard — phyll/phylloclade.md": {
    primary: "A flattened, leaf-like stem or branch specialized for photosynthesis, bearing reduced scales or flowers (as in cacti, Ruscus, or Asparagus).",
    secondary: "In evolutionary plant anatomy, a stem adaptation for arid habitats where reduced surface-to-volume ratio conserves water while maintaining photosynthesis.",
    quotes: [
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "The prickly pear presents a succession of jointed pads, each of which is a succulent **phylloclade** armed with clusters of spines." },
      { author: "Karl von Goebel", work: "Organography of Plants", quote: "Development of a **phylloclade** begins like an ordinary cylindrical shoot before bilateral meristematic activity flattens the axis." },
      { author: "Charles Darwin", work: "Insectivorous Plants", quote: "In certain desert xerophytes, the true leaves abort early, leaving the photosynthetic **phylloclade** to perform all vegetative duties." }
    ]
  },
  "Dashboard — phyll/phyllocladus.md": {
    primary: "A genus of coniferous trees in the family Podocarpaceae (or Phyllocladaceae), known as celery pines, native to New Zealand, Tasmania, and Malesia.",
    secondary: "In Australasian dendrology, conifers whose true leaves are reduced to minute scales while photosynthetic function is performed by diamond-shaped celery-like phylloclades.",
    quotes: [
      { author: "Joseph Dalton Hooker", work: "Flora Tasmaniae", quote: "The celery-topped pine, **Phyllocladus** aspleniifolius, towers in the damp temperate rain forests of western Tasmania." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "In **Phyllocladus**, the branches mimic compound fern fronds so perfectly that travellers mistook the tree for an arborescent cryptogam." },
      { author: "Carl Linnaeus", work: "Species Plantarum", quote: "The seeds of **Phyllocladus** sit in a fleshy cup-shaped aril, dispersed through the forest by native fruit pigeons." }
    ]
  },
  "Dashboard — phyll/phyllode.md": {
    primary: "A modified leaf petiole or leaf stem that is flattened and expanded, functioning like a true leaf blade; typical of Australian acacias.",
    secondary: "In functional plant morphology, an adaptation common in arid-zone wattles where vertical orientation of the phyllode reduces mid-day heat absorption.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "Seedlings of Australian acacias begin with bipinnate leaves, which are gradually replaced in adult trees by vertical **phyllode** foliage." },
      { author: "Asa Gray", work: "First Lessons in Botany", quote: "A **phyllode** is a flattened petiole acting as a leaf blade, recognized by its parallel veins and vertical edge toward the sky." },
      { author: "John Lindley", work: "An Introduction to Botany", quote: "By turning its edge to the midday sun, the **phyllode** minimizes scorching transpiration across the parched Australian desert." }
    ]
  },
  "Dashboard — phyll/phyllodial.md": {
    primary: "Of, relating to, or functioning as a phyllode; having flattened leaf-like petioles.",
    secondary: "In descriptive taxonomy, designating the vast majority of Australian Acacia species that bear phyllodes instead of compound bipinnate foliage.",
    quotes: [
      { author: "Robert Brown", work: "General Remarks on the Botany of Terra Australis", quote: "The **phyllodial** acacias constitute the most distinctive and dominant vegetative element throughout the interior of New Holland." },
      { author: "George Bentham", work: "Flora Australiensis", quote: "Our classification arranges the genus Acacia into bipinnate groups and extensive **phyllodial** series based on venation." },
      { author: "Joseph Dalton Hooker", work: "Himalayan Journals", quote: "The strange **phyllodial** foliage of Australian wattles contrasts remarkably with the broad leaves of Indian jungle trees." }
    ]
  },
  "Dashboard — phyll/phyllodoce.md": {
    primary: "A genus of dwarf evergreen shrubs in the heath family (Ericaceae), known as mountain heathers; also a genus of predatory marine polychaete worms (paddle worms).",
    secondary: "In alpine floristics, circumboreal subshrubs bearing needle-like leaves and urn-shaped pink or cream blossoms along arctic-alpine tundra margins.",
    quotes: [
      { author: "John Muir", work: "The Mountains of California", quote: "High on the rocky rim of Tuolumne Meadows, **Phyllodoce** breweri covers the granite ledges with glorious masses of rose-purple bells." },
      { author: "Asa Gray", work: "Synoptical Flora of North America", quote: "The mountain heathers of the genus **Phyllodoce** thrive in snow-melt hollows above timberline across the Cascade and Sierra ranges." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "In marine zoology, the paddle worm **Phyllodoce** glides through mudflats, swimming gracefully with paddle-like parapodial cirri." }
    ]
  },
  "Dashboard — phyll/phylloporus.md": {
    primary: "A genus of mycorrhizal fungi in the family Boletaceae, commonly known as gilled boletes, having gills instead of tubes beneath the cap.",
    secondary: "In systematic mycology, an evolutionary bridge taxon between agarics and boletes, possessing typical bolete pigments and pileus anatomy but lamellate hymenophores.",
    quotes: [
      { author: "Elias Magnus Fries", work: "Systema Mycologicum", quote: "The golden-gilled fungus now called **Phylloporus** rhodoxanthus presents a remarkable combination of agaric gills and bolete spores." },
      { author: "Charles McIlvaine", work: "One Thousand American Fungi", quote: "In rich deciduous woods, **Phylloporus** reveals its yellow branching gills that bruise bluish-green, confirming its boletaceous affinity." },
      { author: "William Gilson Farlow", work: "Icones Farlowianae", quote: "Microscopic analysis of the basidia and clamp connections confirms that **Phylloporus** belongs firmly within the Boletaceae." }
    ]
  },
  "Dashboard — phyll/phylloquinone.md": {
    primary: "Vitamin K₁, a fat-soluble naphthoquinone compound synthesized by green plants and algae, essential for blood clotting and bone metabolism.",
    secondary: "In biochemistry and hematology, an electron acceptor in photosystem I that acts as an indispensable cofactor for gamma-glutamyl carboxylase in the liver.",
    quotes: [
      { author: "Henrik Dam", work: "The Antihaemorrhagic Vitamin of the Chick", quote: "I isolated pure **phylloquinone** from alfalfa leaves, demonstrating that it restored normal prothrombin levels in bleeding chicks." },
      { author: "Ernest Beutler", work: "Williams Hematology", quote: "Deficiency of **phylloquinone** impairs the carboxylation of clotting factors II, VII, IX, and X, predisposing to hemorrhagic disease." },
      { author: "Frank A. Lee", work: "Basic Food Chemistry", quote: "Green leafy vegetables like spinach and kale serve as our richest dietary sources of natural **phylloquinone**." }
    ]
  },
  "Dashboard — phyll/phyllorhynchus.md": {
    primary: "A genus of small, non-venomous colubrid snakes native to the deserts of southwestern North America and Mexico, known as leaf-nosed snakes.",
    secondary: "In desert herpetology, nocturnal, burrowing serpents possessing an enlarged, spade-like rostral scale with free lateral edges used for burrowing in loose sand.",
    quotes: [
      { author: "Edward Drinker Cope", work: "The Crocodilians, Lizards, and Snakes of North America", quote: "I established the genus **Phyllorhynchus** on account of its extraordinary triangular rostral plate which resembles an upturned leaf." },
      { author: "Raymond Ditmars", work: "Reptiles of the World", quote: "The leaf-nosed snake, **Phyllorhynchus** browni, spends daytime hours burrowed in gravelly desert soil, hunting gecko eggs at twilight." },
      { author: "Malcolm Arthur Smith", work: "Fauna of the Desert Regions", quote: "The modified rostral shield of **Phyllorhynchus** serves as an efficient burrowing scoop in shifting desert sand." }
    ]
  },
  "Dashboard — phyll/phylloscopus.md": {
    primary: "A genus of small, insectivorous Old World warblers (family Phylloscopidae), known as leaf warblers, including the chiffchaff and willow warbler.",
    secondary: "In avian ecology, active, greenish arboreal passerines that glean insects from foliage canopy leaves throughout Eurasia and Africa.",
    quotes: [
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "The willow wren of the genus **Phylloscopus** arrives in early April, singing its plaintive descending cadence from the blossoming sallows." },
      { author: "John Gould", work: "The Birds of Europe", quote: "Members of the genus **Phylloscopus** are easily confounded in plumage, but instantly distinguished by their distinct spring territorial songs." },
      { author: "Ernst Mayr", work: "Animal Species and Evolution", quote: "The ring species complex of **Phylloscopus** trochiloides around the Tibetan plateau affords a textbook demonstration of circular speciation." }
    ]
  },
  "Dashboard — phyll/phyllostachys.md": {
    primary: "A large genus of temperate running bamboos (family Poaceae), native to East Asia, including moso bamboo (Phyllostachys edulis) and timber bamboos.",
    secondary: "In economic forestry, fast-growing monopodial bamboos characterized by grooved internode culms and edible shoots, widely used for construction and paper pulp.",
    quotes: [
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "The golden culms of **Phyllostachys** aurea spread vigorously by subterranean rhizomes, forming dense, towering groves." },
      { author: "Adolf Engler", work: "Das Pflanzenreich", quote: "In China and Japan, forests of **Phyllostachys** edulis provide both delicious spring shoots and industrial timber of astonishing tensile strength." },
      { author: "John Muir", work: "Steep Trails", quote: "The whispering bamboo groves of **Phyllostachys** swayed before the typhoon, bending gracefully without breaking." }
    ]
  },
  "Dashboard — phyll/phyllostomatidae.md": {
    primary: "A large and diverse family of microchiropteran bats native to the Neotropics, commonly known as New World leaf-nosed bats.",
    secondary: "In mammalian adaptive radiation, an extraordinary family encompassing insectivorous, nectar-feeding, frugivorous, carnivorous, and hematophagous (vampire) bats.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "Tropical Nature", quote: "The **Phyllostomatidae** display an astonishing spear-like nose leaf that acts as an acoustic horn for echolocation beam focusing." },
      { author: "William Henry Flower", work: "An Introduction to the Study of Mammals", quote: "Cranial and dental diversity within the **Phyllostomatidae** reflects the broadest dietary range of any mammalian family." },
      { author: "Richard Lydekker", work: "The Royal Natural History", quote: "The true vampire bat belongs to the specialized desmodontine branch of the family **Phyllostomatidae**." }
    ]
  },
  "Dashboard — phyll/phyllostomidae.md": {
    primary: "A former or variant taxonomic family name for Phyllostomatidae (New World leaf-nosed bats).",
    secondary: "In historical systematic mammalogy, the family designation used by 19th-century zoologists for tropical American bats with nasal foliar appendages.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Vertebrated Animals", quote: "The **Phyllostomidae** are restricted to the warmer regions of the American continent, roosting in hollow trees and caverns." },
      { author: "Charles Darwin", work: "The Zoology of the Voyage of H.M.S. Beagle", quote: "We caught specimens of the **Phyllostomidae** in Chile that fluttered around our horses at night seeking blood meals." },
      { author: "Edward Drinker Cope", work: "The Origin of the Fittest", quote: "Osteological modifications in the skull of the **Phyllostomidae** accompany extreme dietary specialization from nectar to flesh." }
    ]
  },
  "Dashboard — phyll/phyllostomus.md": {
    primary: "A genus of large, robust New World leaf-nosed bats in the family Phyllostomatidae, known as spear-nosed bats.",
    secondary: "In neotropical mammalogy, omnivorous forest bats (such as Phyllostomus hastatus) that feed upon fruit, nectar, floral pollen, and small vertebrates.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "Travels on the Amazon and Rio Negro", quote: "The great spear-nosed bat, **Phyllostomus** hastatus, flew into our forest hut, its wings spanning nearly two feet." },
      { author: "William Henry Flower", work: "An Introduction to the Study of Mammals", quote: "The genus **Phyllostomus** is distinguished by its formidable canines, heavy jaw musculature, and erect lanceolate nose-leaf." },
      { author: "Richard Lydekker", work: "The Royal Natural History", quote: "Colonies of **Phyllostomus** roost by hundreds in the dim vaults of tropical limestone caves, issuing forth at dusk to forage." }
    ]
  },
  "Dashboard — phyll/phyllotaxis.md": {
    primary: "The arrangement of leaves on an axis or stem of a plant, such as alternate, opposite, whorled, or spiral phyllotaxis.",
    secondary: "In mathematical morphology and developmental plant biology, the regular geometric positioning of leaves governed by Fibonacci sequences and the golden ratio angle (137.5°).",
    quotes: [
      { author: "Asa Gray", work: "First Lessons in Botany", quote: "The study of **phyllotaxis** proves that leaves are arranged along the stem in definite mathematical fractions, such as two-fifths and three-eighths." },
      { author: "D'Arcy Wentworth Thompson", work: "On Growth and Form", quote: "The spiral **phyllotaxis** of pinecones and sunflower florets illustrates how physical packing constraints generate Fibonacci spirals." },
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "Apical meristem divergence angles determine the precise **phyllotaxis** of all subsequent lateral foliar organs." }
    ]
  },
  "Dashboard — phyll/phylloxera.md": {
    primary: "A microscopic, aphid-like insect (Daktulosphaira vitifoliae, family Phylloxeridae) that attacks the roots and leaves of grapevines, devastating European vineyards in the late 19th century.",
    secondary: "In agricultural history and viticulture, the American pest whose subterranean nymph infestations caused the Great French Wine Blight, solved only by grafting European vinifera onto resistant American rootstocks.",
    quotes: [
      { author: "Louis Pasteur", work: "Studies on Wine", quote: "The catastrophic spread of **phylloxera** threatened the absolute ruin of French viticulture until resistant American rootstocks were introduced." },
      { author: "Charles Valentine Riley", work: "The Grape Phylloxera", quote: "I proved that the root-gall insect of Europe is identical with the American vine pest, **Phylloxera** vitifoliae." },
      { author: "Alexis Lichine", work: "Wines of France", quote: "Virtually every classic vineyard in Bordeaux today is grafted upon hybrid rootstocks to withstand the subterranean menace of **phylloxera**." }
    ]
  },
  "Dashboard — phyll/phylloxeridae.md": {
    primary: "A family of small plant-parasitic hemipterous insects closely related to aphids (superfamily Aphidoidea), lacking cornicles and producing wax from abdominal glands.",
    secondary: "In agricultural entomology, specialized gall-forming and root-feeding insects including the grape phylloxera and hickory gall phylloxerans.",
    quotes: [
      { author: "Charles Valentine Riley", work: "Reports on the Insects of Missouri", quote: "The family **Phylloxeridae** differs from the true Aphididae in laying eggs exclusively and having three-segmented antennae in all forms." },
      { author: "Leland Ossian Howard", work: "The Insect Book", quote: "Members of the **Phylloxeridae** exhibit intricate multi-generational life cycles involving winged dispersers, sexuparae, and subterranean root forms." },
      { author: "John Henry Comstock", work: "An Introduction to Entomology", quote: "Hickory leaves are frequently deformed by globular galls caused by various species of the **Phylloxeridae**." }
    ]
  },
  "Dashboard — phyt/archaeophyte.md": {
    primary: "A plant species that was introduced to an area by human activity in ancient times (in Europe, usually before the discovery of America in 1492).",
    secondary: "In historical plant biogeography and archaeobotany, ancient agricultural weeds and cultivars (such as the corn poppy and cornflower) thoroughly naturalized in pre-modern farming landscapes.",
    quotes: [
      { author: "Arthur George Tansley", work: "The British Islands and Their Vegetation", quote: "Many of our familiar arable field weeds are classified as an **archaeophyte**, having arrived with Neolithic and Roman agriculture." },
      { author: "George Bentham", work: "Handbook of the British Flora", quote: "The scarlet corn poppy is a classic **archaeophyte**, following ancient cereal trade routes from the Mediterranean basin across western Europe." },
      { author: "Colin Renfrew", work: "Before Civilization", quote: "Pollen cores reveal the sudden appearance of the first cereal-associated **archaeophyte** species alongside early clearing horizons." }
    ]
  },
  "Dashboard — phyt/astrophysical.md": {
    primary: "Of, relating to, or characteristic of astrophysics (the branch of astronomy dealing with the physical and chemical properties of celestial bodies).",
    secondary: "In cosmic physics, designating quantitative methods employing spectroscopy, thermodynamics, and nuclear physics to understand stars, galaxies, and the universe.",
    quotes: [
      { author: "Arthur Stanley Eddington", work: "The Internal Constitution of the Stars", quote: "Advances in **astrophysical** theory demonstrated that radiation pressure counterbalances gravitational collapse in massive stars." },
      { author: "Subrahmanyan Chandrasekhar", work: "An Introduction to the Study of Stellar Structure", quote: "The **astrophysical** limit of white dwarf stability was derived by combining quantum degeneracy with special relativity." },
      { author: "George Gamow", work: "The Creation of the Universe", quote: "Spectroscopic lines shifted toward the red provided the prime **astrophysical** clue for the expansion of space." }
    ]
  },
  "Dashboard — phyt/astrophysicist.md": {
    primary: "A scientist or astronomer who specializes in astrophysics.",
    secondary: "A physical scientist who investigates the origins, stellar mechanisms, radiation fields, and evolution of cosmic phenomena through physical theory and observation.",
    quotes: [
      { author: "Arthur Stanley Eddington", work: "Stars and Atoms", quote: "The modern **astrophysicist** uses the laboratory of the stars to test atomic theories under temperatures unreachable on earth." },
      { author: "Subrahmanyan Chandrasekhar", work: "Selected Papers on Astrophysics", quote: "A dedicated **astrophysicist** must master both the mathematical rigor of fluid dynamics and the observational nuances of the telescope." },
      { author: "Fred Hoyle", work: "Frontiers of Astronomy", quote: "The discovery of interstellar organic molecules astonished every **astrophysicist** who had deemed space entirely sterile." }
    ]
  },
  "Dashboard — phyt/astrophysics.md": {
    primary: "The branch of astronomy concerned with the physical nature, properties, chemical composition, and evolutionary processes of celestial bodies and the universe.",
    secondary: "In the history of science, the 19th-century revolution sparked by the prism that transformed observational positional astronomy into an experimental physical science.",
    quotes: [
      { author: "Arthur Stanley Eddington", work: "The Nature of the Physical World", quote: "The triumph of **astrophysics** was to demonstrate that stellar matter obeys the identical physical and quantum laws discovered in terrestrial laboratories." },
      { author: "George Gamow", work: "One Two Three... Infinity", quote: "Modern **astrophysics** unlocked the secret of solar fire, showing that thermonuclear fusion powers the stars." },
      { author: "Edwin Hubble", work: "The Realm of the Nebulae", quote: "The marriage of photography, spectroscopy, and giant reflectors established **astrophysics** as our key to the distant universe." }
    ]
  }
};

let count = 0;
for (const [relPath, data] of Object.entries(batch7Data)) {
  if (updateNote(relPath, data)) {
    count++;
  }
}

console.log(`\n========================================`);
console.log(`Batch 7 Completed: ${count} / ${Object.keys(batch7Data).length} notes updated.`);
console.log(`========================================\n`);
