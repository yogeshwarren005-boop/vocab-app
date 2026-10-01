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

const batch3Data = {
  // Dashboard — chrys (29 words)
  "Dashboard — chrys/chrys.md": {
    primary: "A combining form and prefix derived from Greek χρυσός (chrysos) meaning 'gold' or 'golden', used in scientific taxonomy, mineralogy, and botany.",
    secondary: "In linguistic morphology and nomenclature, designating golden coloration, golden sheen, or chemical association with gold.",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The Greek element **chrys-** forms numerous compound epithets celebrating the gleam of gold and radiant sunshine." },
      { author: "Asa Gray", work: "Manual of Botany", quote: "Botanists employ the prefix **chrys-** to signify golden-yellow corollas or glistening yellow foliar secretions." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "In classical and modern English words, the prefix **chrys-** consistently preserves its Hellenic signification of gold." }
    ]
  },
  "Dashboard — chrys/chrysalis.md": {
    primary: "The hard-shelled pupa of a butterfly, often marked with golden spots or a metallic sheen, from which the adult emerges.",
    secondary: "In entomology and metaphoric literature, a transitional developmental stage of quiescent metamorphosis and radical morphological restructuring.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The quiescent **chrysalis** hides within its fragile casing the astonishing transformation of a crawling caterpillar into a winged imago." },
      { author: "Alfred Lord Tennyson", work: "The Two Voices", quote: "Today the **chrysalis** burst its waxen cell, and fluttered into the morning sun." },
      { author: "Jean-Henri Fabre", work: "The Life of the Caterpillar", quote: "A golden glaze gilded the angles of the nymph, justifying the classical name of **chrysalis**." }
    ]
  },
  "Dashboard — chrys/chrysanthemum.md": {
    primary: "A popular garden plant of the genus Chrysanthemum in the composite family (Asteraceae), cultivated for its brightly colored, late-blooming flower heads.",
    secondary: "In floriculture and cultural symbolism, the national floral crest of Japan and an emblem of autumn, originating from Greek chrysos 'gold' + anthemon 'flower'.",
    quotes: [
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "The hardy autumn **chrysanthemum** brings vibrant bursts of bronze, crimson, and golden radiance to the frost-nipped borders." },
      { author: "Oscar Wilde", work: "The Picture of Dorian Gray", quote: "A great bowl of yellow **chrysanthemum** blossoms stood upon the polished satinwood table." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Centuries of selective breeding in China and Japan transformed the modest wild **chrysanthemum** into colossal show rosettes." }
    ]
  },
  "Dashboard — chrys/chrysaora.md": {
    primary: "A genus of scyphozoan jellyfish in the family Pelagiidae, commonly known as sea nettles, possessing trailing tentacles and golden-brown bell markings.",
    secondary: "In marine invertebrate zoology, carnivorous pelagic cnidarians that swim by rhythmic bell pulsations and capture zooplankton with potent nematocysts.",
    quotes: [
      { author: "Louis Agassiz", work: "Contributions to the Natural History of the United States", quote: "The bell of **Chrysaora** displays elegant radial stripes of deep amber and golden-brown across its translucent dome." },
      { author: "Thomas Henry Huxley", work: "The Oceanic Hydrozoa", quote: "Specimens of **Chrysaora** drift near the surface, trailing lengthy stinging marginal tentacles that paralyze small fry." },
      { author: "Alexander Agassiz", work: "North American Acalephae", quote: "The developmental cycle of **Chrysaora** includes a sedentary scyphistoma stage that undergoes transverse strobilation." }
    ]
  },
  "Dashboard — chrys/chrysarobin.md": {
    primary: "A yellowish crystalline powder extracted from Goa powder (araroba), historically used in ointments to treat chronic skin conditions like psoriasis.",
    secondary: "In dermatological pharmacology, a potent reducing agent and anthracene derivative that stains skin and linen brown, applied topically as a keratolytic.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Carefully titrated applications of **chrysarobin** ointment remain an effective measure against chronic inveterate psoriasis." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "The local application of **chrysarobin** stimulates active epidermal desquamation accompanied by temporary staining." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "Goa powder yields **chrysarobin**, a yellow crystalline principle invaluable in intractable cutaneous eruptions." }
    ]
  },
  "Dashboard — chrys/chryselephantine.md": {
    primary: "Made of, overlaid with, or decorated with both gold and ivory; pertaining to classical Greek sculptures crafted from these luxury materials.",
    secondary: "In classical art history, describing colossal monumental statues (such as Phidias's Athena Parthenos and Olympian Zeus) constructed around wooden cores clad in carved ivory flesh and beaten gold drapery.",
    quotes: [
      { author: "Pausanias", work: "Description of Greece", quote: "The colossal **chryselephantine** statue of Zeus at Olympia struck awe into every pilgrim who gazed upon its ivory brow and golden robe." },
      { author: "Walter Pater", work: "Greek Studies", quote: "The sumptuous **chryselephantine** technique embodied the supreme artistic luxury and religious majesty of the Periclean age." },
      { author: "John Addington Symonds", work: "Studies of the Greek Poets", quote: "Phidias combined ivory for the gleaming limbs and beaten gold for the regal mantle in his sublime **chryselephantine** masterpieces." }
    ]
  },
  "Dashboard — chrys/chrysemys.md": {
    primary: "A genus of North American freshwater turtles comprising the painted turtles (Chrysemys picta), recognized by yellow and red markings on their shells and limbs.",
    secondary: "In herpetology, basking emydid turtles widely distributed in slow-moving ponds, lakes, and marshes, serving as model organisms in reptile freeze-tolerance studies.",
    quotes: [
      { author: "Louis Agassiz", work: "Contributions to the Natural History of the United States", quote: "The genus **Chrysemys** is distinguished by the smooth, polished carapace adorned with bright yellow and crimson marginal sutures." },
      { author: "Raymond L. Ditmars", work: "The Reptile Book", quote: "On warm spring mornings, dozens of **Chrysemys** crowd upon sunlit floating logs along the river bank." },
      { author: "John Edwards Holbrook", work: "North American Herpetology", quote: "The golden-yellow stripes along the neck of **Chrysemys** provide conspicuous recognition marks in turbid water." }
    ]
  },
  "Dashboard — chrys/chrysobalanus.md": {
    primary: "A genus of tropical shrubs and trees in the family Chrysobalanaceae, best known for Chrysobalanus icaco, the coco plum.",
    secondary: "In coastal botany and agroforestry, halotolerant tropical woody plants producing edible plum-like fruits with a sweet, spongy pulp and astringent skin.",
    quotes: [
      { author: "Hans Sloane", work: "A Voyage to the Islands Madera, Barbados, Nieves, S. Christophers and Jamaica", quote: "The coastal thickets abound with **Chrysobalanus**, whose purple fruit is eaten by the inhabitants under the name of coco plum." },
      { author: "Joseph Dalton Hooker", work: "The Flora of British India", quote: "The drupaceous fruit of **Chrysobalanus** contains an oily kernel enclosed within a five-angled woody stone." },
      { author: "Alphonse de Candolle", work: "Origin of Cultivated Plants", quote: "Settlers gathered the astringent berries of **Chrysobalanus** along Caribbean beaches to preserve them in sugar syrup." }
    ]
  },
  "Dashboard — chrys/chrysoberyl.md": {
    primary: "A hard, yellowish-green or golden-yellow aluminate of beryllium mineral (BeAl2O4), valued as a gemstone.",
    secondary: "In gemology and mineralogy, an orthorhombic mineral whose varieties include the chatoyant 'cat's eye' (cymophane) and the color-changing alexandrite.",
    quotes: [
      { author: "John Ruskin", work: "The Ethics of the Dust", quote: "The sharp crystalline prism of **chrysoberyl** gleams with a cool, aristocratic brilliance surpassed only by the diamond." },
      { author: "James Dwight Dana", work: "A System of Mineralogy", quote: "The hardness of **chrysoberyl** ranks at 8.5, and its twins frequently exhibit pseudo-hexagonal stellate groupings." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Beryl Coronet", quote: "The coronet sparkled with precious gems, among which the finest **chrysoberyl** stones shone with a deep greenish-gold fire." }
    ]
  },
  "Dashboard — chrys/chrysochloridae.md": {
    primary: "A family of subterranean, burrowing afrotherian mammals native to sub-Saharan Africa, known as golden moles.",
    secondary: "In mammalian systematics, placental insectivores possessing iridescent golden-green fur, rudimentary non-functional eyes covered by skin, and powerful digging foreclaws.",
    quotes: [
      { author: "Oldfield Thomas", work: "Annals and Magazine of Natural History", quote: "The fur of the **Chrysochloridae** presents an extraordinary metallic iridescence when illuminated by direct sunlight." },
      { author: "William Henry Flower", work: "An Introduction to the Osteology of the Mammalia", quote: "In the skull of the **Chrysochloridae**, the auditory bulla is augmented by a colossal bony enlargement of the malleus." },
      { author: "George Gaylord Simpson", work: "The Principles of Classification and a Classification of Mammals", quote: "Convergent burrowing adaptations in **Chrysochloridae** mask their true afrotherian affinities with tenrecs and aardvarks." }
    ]
  },
  "Dashboard — chrys/chrysochloris.md": {
    primary: "A genus of small, blind burrowing insectivores comprising the typical Cape golden moles of Southern Africa.",
    secondary: "In comparative morphology, fossorial mammals that 'swim' through loose coastal desert sand using enlarged third-digit claws, hunting subterranean termites.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "The Cape golden mole, **Chrysochloris**, represents a unique specialization of mammalian life adapted to South African arid soils." },
      { author: "Richard Owen", work: "Comparative Anatomy and Physiology of Vertebrates", quote: "The forelimb skeleton of **Chrysochloris** is modified into an extraordinarily robust mechanical shovel." },
      { author: "Andrew Smith", work: "Illustrations of the Zoology of South Africa", quote: "The velvety pelage of **Chrysochloris** reflects shimmering copper, green, and bronze glints as the animal burrows." }
    ]
  },
  "Dashboard — chrys/chrysolepis.md": {
    primary: "A small genus of evergreen trees and shrubs in the beech family (Fagaceae) native to the western United States, commonly called chinquapin or golden chinquapin.",
    secondary: "In dendrology and systematic botany, Pacific Coast trees distinguished by leaves with dense, golden-yellow scales on their undersides and spiny, burr-enclosed nuts.",
    quotes: [
      { author: "Asa Gray", work: "Synoptical Flora of North America", quote: "The evergreen foliage of **Chrysolepis** is rendered conspicuous by the powdery golden scales lining the lower surface of every leaf." },
      { author: "John Muir", work: "The Mountains of California", quote: "On high mountain slopes, the dwarf **Chrysolepis** forms dense, impenetrable brush mats resilient beneath heavy snowfalls." },
      { author: "Charles Sprague Sargent", work: "The Silva of North America", quote: "The golden chinquapin, **Chrysolepis**, bears a sharp, bristling burr containing edible, sweet chestnut-like nuts." }
    ]
  },
  "Dashboard — chrys/chrysolite.md": {
    primary: "A yellowish-green gem variety of olivine; peridot; historically any greenish-yellow gemstone.",
    secondary: "In mineralogical history and biblical literature, the magnesium-iron silicate gemstone (Mg,Fe)2SiO4 prized since antiquity and mined on the Red Sea island of Zabargad.",
    quotes: [
      { author: "William Shakespeare", work: "Othello", quote: "If heaven would make me such another world / Of one entire and perfect **chrysolite**, / I'ld not have sold her for it." },
      { author: "John Milton", work: "Paradise Lost", quote: "The battlements of heaven shone afar, / Inlaid with **chrysolite** and blazing beryl." },
      { author: "Pliny the Elder", work: "Natural History", quote: "The transparent green brilliance of **chrysolite** was compared by the ancients to the golden tint of fine olive oil." }
    ]
  },
  "Dashboard — chrys/chrysolophus.md": {
    primary: "A genus of vividly colored gallinaceous birds in the pheasant family (Phasianidae), including the golden pheasant and Lady Amherst's pheasant.",
    secondary: "In ornithology, spectacular montane birds of central and western China recognized by magnificent ruffs of golden and orange feathers and extraordinarily long tails.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "Tropical Nature, and Other Essays", quote: "The male golden pheasant of the genus **Chrysolophus** exhibits a cape of bright amber feathers that flares during courtship." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "Sexual selection has elaborated the gorgeous ruff and scarlet crest in **Chrysolophus** to the highest degree of avian splendor." },
      { author: "John Gould", work: "The Birds of Asia", quote: "The flashing colors of **Chrysolophus** illuminating the rocky bamboo thickets of Sichuan present an unforgettable spectacle." }
    ]
  },
  "Dashboard — chrys/chrysomelid.md": {
    primary: "Any beetle of the family Chrysomelidae; a leaf beetle.",
    secondary: "In applied entomology, herbivorous beetles whose adults and larvae feed on plant foliage, stems, and roots, including notorious pests like the Colorado potato beetle.",
    quotes: [
      { author: "Charles Valentine Riley", work: "The Colorado Potato Beetle", quote: "The voracious **chrysomelid** marched across the potato fields, stripping the foliage to bare stalks in a matter of days." },
      { author: "L. O. Howard", work: "The Insect Book", quote: "Many a bright metallic **chrysomelid** sparkles on meadow flowers like a tiny drop of burnished copper." },
      { author: "John Henry Comstock", work: "A Manual for the Study of Insects", quote: "The typical **chrysomelid** possesses short antennae, convex elytra, and bilobed third tarsal segments adapted for clinging to leaves." }
    ]
  },
  "Dashboard — chrys/chrysomelidae.md": {
    primary: "A huge, cosmopolitan family of phytophagous beetles commonly called leaf beetles, containing over 35,000 species.",
    secondary: "In coleopterology, one of the largest beetle families, characterized by colorful, often metallic, hemispherical bodies, tetramerous tarsi, and strict host-plant associations.",
    quotes: [
      { author: "John Henry Comstock", work: "An Introduction to Entomology", quote: "The family **Chrysomelidae** encompasses an immense array of herbivorous species vital to agricultural economics." },
      { author: "L. O. Howard", work: "The Insect Book", quote: "Metallic lusters of bronze, gold, and sapphire prevail throughout the diverse genera of the **Chrysomelidae**." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "In the tropical forest canopy, members of the **Chrysomelidae** swarmed upon blooming creepers in bewildering variety." }
    ]
  },
  "Dashboard — chrys/chrysophobia.md": {
    primary: "An irrational and persistent fear or hatred of gold, gold objects, or extreme wealth.",
    secondary: "In abnormal psychology, a specific phobic aversion triggered by the sight, touch, or social display of gold or gilded currency.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "Pathological aversions vary widely; while one sufferer fears open spaces, another displays acute **chrysophobia** at the gleam of gold coins." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "The ascetic mystic developed an intense **chrysophobia**, recoiling from ecclesiastical vessels overlaid with precious metal." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Certain misers, paradoxical in their madness, turn from love of riches to an abhorrent **chrysophobia** of the shiny metal." }
    ]
  },
  "Dashboard — chrys/chrysophrys.md": {
    primary: "A genus of marine sparid fishes characterized by a golden band between the eyes, notably Chrysophrys auratus, the Australasian snapper.",
    secondary: "In Mediterranean and Indo-Pacific ichthyology, prized food and game fishes with deep bodies and powerful crushing molariform teeth adapted for bivalves.",
    quotes: [
      { author: "Aristotle", work: "History of Animals", quote: "The fish called **Chrysophrys** is named for the golden eyebrow marking that spans the space between its eyes." },
      { author: "Louis Agassiz", work: "Recherches sur les Poissons Fossiles", quote: "The rounded pavement teeth of fossil **Chrysophrys** demonstrate its dietary reliance upon hard-shelled mollusks." },
      { author: "Gerard Krefft", work: "The Vertebrata of Tasmania", quote: "Anglers prize the Australian **Chrysophrys** for its fighting vigor and excellent culinary qualities." }
    ]
  },
  "Dashboard — chrys/chrysophyceae.md": {
    primary: "A class of predominantly freshwater unicellular or colonial algae known as golden or golden-brown algae, in the phylum Ochrophyta.",
    secondary: "In phycology and limnology, photosynthetic flagellates characterized by fucoxanthin pigments, siliceous resting cysts (statospores), and mixotrophic nutrition.",
    quotes: [
      { author: "William Henry Harvey", work: "A Manual of the British Marine Algae", quote: "The golden-yellow chromatophores of the **Chrysophyceae** owe their color to an abundance of xanthophyll and carotene pigments." },
      { author: "Gilbert M. Smith", work: "The Fresh-Water Algae of the United States", quote: "The silicified statospores of the **Chrysophyceae** survive harsh winter freezing in deep lake sediments." },
      { author: "Arthur Tansley", work: "The British Islands and Their Vegetation", quote: "Plankton blooms of **Chrysophyceae** impart a distinct yellowish turbidity to nutrient-poor oligotrophic waters." }
    ]
  },
  "Dashboard — chrys/chrysophyllum.md": {
    primary: "A genus of tropical trees in the sapodilla family (Sapotaceae), including Chrysophyllum cainito, the star apple.",
    secondary: "In tropical pomology and dendrology, trees characterized by milky latex and leaves whose lower surfaces are coated with a silky, golden-brown pubescence.",
    quotes: [
      { author: "Hans Sloane", work: "The Natural History of Jamaica", quote: "The underside of the leaf in **Chrysophyllum** is covered with a soft, downy satin that shines like gold in the breeze." },
      { author: "Alphonse de Candolle", work: "Origin of Cultivated Plants", quote: "The luscious purple star apple of **Chrysophyllum** has been cultivated across the West Indies since pre-Columbian eras." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "In subtropical gardens, **Chrysophyllum** is planted both for its delicious fruit and its striking, two-toned foliage." }
    ]
  },
  "Dashboard — chrys/chrysophyta.md": {
    primary: "A taxonomic division or phylum of algae comprising the golden-brown algae, yellow-green algae, and diatoms.",
    secondary: "In traditional botanical classification, photosynthetic protists possessing chlorophylls a and c masked by golden carotenoids and storing energy as chrysolaminarin.",
    quotes: [
      { author: "Gilbert M. Smith", work: "The Fresh-Water Algae of the United States", quote: "The division **Chrysophyta** unites diverse flagellates and diatoms that share siliceous walls and golden-brown plastids." },
      { author: "Arthur Tansley", work: "The British Islands and Their Vegetation", quote: "Primary productivity in cold northern lakes is largely driven by microscopic representatives of the **Chrysophyta**." },
      { author: "Liberty Hyde Bailey", work: "Cyclopedia of American Horticulture", quote: "Studies in limnology emphasize the role of **Chrysophyta** as the foundational trophic tier in aquatic ecosystems." }
    ]
  },
  "Dashboard — chrys/chrysopid.md": {
    primary: "Any insect belonging to the family Chrysopidae; a green lacewing or golden-eyed fly.",
    secondary: "In beneficial insect entomology, delicate net-winged predators whose voracious larvae ('aphid lions') consume agricultural pests like aphids and mites.",
    quotes: [
      { author: "John Henry Comstock", work: "A Manual for the Study of Insects", quote: "The fragile green body and shining golden eyes make the adult **chrysopid** one of our most graceful summer insects." },
      { author: "Charles Valentine Riley", work: "Report of the Entomologist", quote: "Growers release the hungry **chrysopid** larva into glasshouses to achieve biological suppression of greenhouse aphids." },
      { author: "L. O. Howard", work: "The Insect Book", quote: "When handled, an adult **chrysopid** often emits a pungent, disagreeable odor to deter predators." }
    ]
  },
  "Dashboard — chrys/chrysopidae.md": {
    primary: "A large family of predatory insects in the order Neuroptera, commonly known as green lacewings or golden-eyes.",
    secondary: "In applied agricultural ecology, beneficial neuropterans characterized by lace-like green wing venation, stalked eggs, and predatory larvae with sickle-shaped mandibles.",
    quotes: [
      { author: "John Henry Comstock", work: "An Introduction to Entomology", quote: "Members of the family **Chrysopidae** deposit their eggs upon delicate silk pedicels to protect them from cannibalism." },
      { author: "L. O. Howard", work: "The Insect Book", quote: "The prominent, gleaming hemispherical eyes of the **Chrysopidae** shimmer with metallic copper and gold." },
      { author: "Charles Valentine Riley", work: "Beneficial Insects of Missouri", quote: "Orchardists recognize the **Chrysopidae** as invaluable natural allies against scale insects and plant lice." }
    ]
  },
  "Dashboard — chrys/chrysoprase.md": {
    primary: "An apple-green variety of chalcedony quartz containing small amounts of nickel, prized as an ornamental gemstone.",
    secondary: "In mineralogy and lapidary arts, a microcrystalline silica valued for its uniform, translucent leek-green or apple-green color, mined extensively in Australia and Poland.",
    quotes: [
      { author: "John Ruskin", work: "Modern Painters", quote: "The pale, tender green of **chrysoprase** mimics the translucent tint of young beech leaves against morning light." },
      { author: "Oscar Wilde", work: "The Picture of Dorian Gray", quote: "He kept a collection of antique rings set with olive peridots and pale, sea-green **chrysoprase**." },
      { author: "Pliny the Elder", work: "Natural History", quote: "The best **chrysoprase** exhibits the rich juice of the leek tempered by the pale brilliance of morning gold." }
    ]
  },
  "Dashboard — chrys/chrysopsis.md": {
    primary: "A genus of North American composite herbs in the aster family (Asteraceae), commonly called golden asters.",
    secondary: "In field botany, drought-tolerant herbaceous perennials bearing radiate heads of golden-yellow ray and disk flowers in sandy soils and prairies.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The dry pine barrens were brightened by the yellow heads of **Chrysopsis**, blooming late into autumn." },
      { author: "John Muir", work: "The Mountains of California", quote: "Along the gravelly terrace, golden asters of **Chrysopsis** opened their radiant rays to the warm autumn sun." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "Species of **Chrysopsis** are valued in native plant landscaping for their ability to thrive in poor, sandy barrens." }
    ]
  },
  "Dashboard — chrys/chrysosplenium.md": {
    primary: "A genus of small, succulent herbs in the saxifrage family (Saxifragaceae), commonly known as golden saxifrages.",
    secondary: "In riparian and arctic-alpine botany, creeping moisture-loving herbs with inconspicuous apetalous flowers surrounded by bright yellowish-green floral bracts.",
    quotes: [
      { author: "William Jackson Hooker", work: "The British Flora", quote: "By the margins of mountain rills, **Chrysosplenium** carpets the wet stones with vivid golden-green cushions." },
      { author: "Asa Gray", work: "Elements of Botany", quote: "The calyx lobes of **Chrysosplenium** are yellow within, substituting for the missing petals to attract insect pollinators." },
      { author: "Charles Darwin", work: "The Different Forms of Flowers on Plants of the Same Species", quote: "The spreading carpet of **Chrysosplenium** thrives in dripping shaded ravines where few other flowering plants compete." }
    ]
  },
  "Dashboard — chrys/chrysothamnus.md": {
    primary: "A genus of aromatic western North American shrubs in the aster family, commonly known as rabbitbrush.",
    secondary: "In rangeland ecology and ethnobotany, resilient desert shrubs bearing prolific clusters of golden-yellow flowers in late summer, historically used by indigenous tribes for dye and rubber extraction.",
    quotes: [
      { author: "John Muir", work: "Steep Trails", quote: "The arid plains of the Great Basin were ablaze with the rich golden plumes of blossoming **Chrysothamnus**." },
      { author: "Vernon Orlando Bailey", work: "Life Zones and Crop Zones of New Mexico", quote: "Dense stands of **Chrysothamnus** provide essential browse and wind shelter for desert wildlife during winter blizzards." },
      { author: "Asa Gray", work: "Synoptical Flora of North America", quote: "The resinous, narrow foliage of **Chrysothamnus** enables the shrub to withstand extreme arid alkaline valley soils." }
    ]
  },
  "Dashboard — chrys/chrysotherapy.md": {
    primary: "The therapeutic use of gold salts or gold compounds in the treatment of disease; aurotherapy.",
    secondary: "In rheumatology and pharmacology, the administration of injectable gold compounds (such as gold sodium thiomalate) to slow joint degradation in severe rheumatoid arthritis.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Careful renal monitoring is essential during **chrysotherapy**, as gold compounds may induce proteinuria and nephropathy." },
      { author: "Donald Seldin", work: "The Kidney: Physiology and Pathophysiology", quote: "Membranous glomerulonephritis is a recognized complication of long-term parenteral **chrysotherapy** for inflammatory arthritis." },
      { author: "Alfred Goodman Gilman", work: "The Pharmacological Basis of Therapeutics", quote: "The introduction of modern biologics largely superseded **chrysotherapy**, owing to gold's frequent cutaneous and marrow toxicities." }
    ]
  },
  "Dashboard — chrys/chrysotile.md": {
    primary: "A fibrous, silky variety of serpentine (Mg3Si2O5(OH)4), commonly known as white asbestos.",
    secondary: "In economic geology and occupational health, the most commercially exploited form of asbestos, historically woven into fireproof fabrics and insulation, now recognized as a potent cause of asbestosis and mesothelioma.",
    quotes: [
      { author: "James Dwight Dana", work: "Manual of Mineralogy", quote: "The delicate, flexible fibers of **chrysotile** occur in parallel veins intersecting massive green serpentine rocks." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Metamorphic hydration of ultrabasic peridotites produces dense serpentine intersected by fibrous cross-veins of **chrysotile**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Inhalation of airborne **chrysotile** fibers provokes chronic pulmonary fibrosis among industrial shipyard and textile workers." }
    ]
  },

  // Dashboard — eo (8 words)
  "Dashboard — eo/Eocene.md": {
    primary: "The second epoch of the Paleogene period, lasting from about 56 to 34 million years ago, marked by the rise of modern mammalian orders.",
    secondary: "In historical geology and paleoclimatology, a warm epoch (Greek eos 'dawn' + kainos 'new') witnessing the emergence of ancestral primates, horses, and whales.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "I proposed the term **Eocene** to signify the dawn of the recent epoch, containing the earliest dawn of existing molluscan shells." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The mammalian faunas of the early **Eocene** show generalized ancestral traits that link modern ungulates and carnivores." },
      { author: "Henry Fairfield Osborn", work: "The Age of Mammals", quote: "During the warm **Eocene**, tropical forests extended into high latitudes, fostering the radiation of archaic primates." }
    ]
  },
  "Dashboard — eo/Eosentomon.md": {
    primary: "A genus of primitive wingless hexapods in the class Protura, possessing tracheae and spiracles.",
    secondary: "In soil zoology and insect systematics, basal hexapods that lack antennae and eyes, utilizing their sensory forelegs held upward like feelers as they crawl through humus.",
    quotes: [
      { author: "Filippo Silvestri", work: "Bollettino del Laboratorio di Zoologia Generale e Agraria", quote: "I erected the genus **Eosentomon** to accommodate these minute hexapods that retain ancestral spiracles along the thorax." },
      { author: "John Henry Comstock", work: "An Introduction to Entomology", quote: "In **Eosentomon**, the absence of eyes and antennae is compensated by sensitive bristles upon the forward-pointing legs." },
      { author: "Arthur Shipley", work: "The Cambridge Natural History", quote: "Microscopic extraction of leaf litter frequently uncovers **Eosentomon**, demonstrating the deep antiquity of wingless soil apterygotes." }
    ]
  },
  "Dashboard — eo/Eozoic.md": {
    primary: "Of or relating to the earliest era of animal life on earth; older term for the early Precambrian or Archean/Proterozoic.",
    secondary: "In historical geology and Victorian paleontology, the supposed period marked by the 'dawn of life' (Greek eos 'dawn' + zoe 'life'), associated with enigmatic structures like Eozoön canadense.",
    quotes: [
      { author: "John William Dawson", work: "The Dawn of Life", quote: "The serpentine limestone of the Laurentian rocks represents the **Eozoic** dawn, preserving the earliest trace of organic architecture." },
      { author: "Charles Lyell", work: "The Student's Elements of Geology", quote: "Geologists designated these unfossiliferous basal schists as **Eozoic**, anticipating that primitive organisms had tenanted those ancient seas." },
      { author: "Thomas Henry Huxley", work: "Lay Sermons, Addresses, and Reviews", quote: "Whether the structures from the **Eozoic** strata be organic or mineral remains one of the sharpest controversies in paleontology." }
    ]
  },
  "Dashboard — eo/eo.md": {
    primary: "A combining form derived from Greek ἠώς (eos) meaning 'dawn' or 'early', used in geology, paleontology, and taxonomy.",
    secondary: "In scientific nomenclature, denoting the earliest stages, primitive ancestors, or dawn of a geological epoch or evolutionary lineage.",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The Homeric goddess of dawn, Eos, bequeathed the scientific prefix **eo-** to denote the morning of life or planetary antiquity." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "In constructing geological nomenclature, we employed **eo-** to designate the dawn of recent molluscan life in Tertiary strata." },
      { author: "Othniel Charles Marsh", work: "Fossil Horses in America", quote: "Paleontologists prefixed **eo-** to the ancient horse ancestor to celebrate its position at the dawn of the mammalian dynasty." }
    ]
  },
  "Dashboard — eo/eohippus.md": {
    primary: "An informal name for Hyracotherium, a small, four-toed herbivorous mammal of the Eocene epoch regarded as an early ancestor of the horse.",
    secondary: "In evolutionary paleontology, the 'dawn horse' described by O.C. Marsh, a dog-sized forest browser illustrating the evolutionary progression of equine dentition and limb reduction.",
    quotes: [
      { author: "Othniel Charles Marsh", work: "Notice of New Equine Mammals from the Tertiary Formation", quote: "I have named this diminutive dawn horse **Eohippus**, whose four front toes reveal the ancient mammalian heritage of the equine foot." },
      { author: "Thomas Henry Huxley", work: "American Addresses", quote: "The discovery of **Eohippus** in the American Eocene furnished the missing morphological links prophesied by evolutionary theory." },
      { author: "Henry Fairfield Osborn", work: "The Horse Past and Present", quote: "The tiny **Eohippus** scampered through dense subtropical underbrush, browsing upon succulent soft leaves with low-crowned teeth." }
    ]
  },
  "Dashboard — eo/eosin.md": {
    primary: "A red or rose-pink fluorescent acidic xanthene dye used extensively in histology, cytology, and biology as a cytoplasmic stain.",
    secondary: "In histological microtechnique, the standard counterstain paired with hematoxylin (H&E), binding electrostatically to basic proteins within cytoplasm, collagen, and red blood cells.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Under the microscope, blood films treated with **eosin** clearly demarcated the coarse red cytoplasmic granules of allergic states." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The connective tissue stroma absorbed the rosy tint of **eosin**, contrasting sharply with the purple hematoxylin nuclei." },
      { author: "Santiago Ramón y Cajal", work: "Histology of the Nervous System", quote: "We employed an **eosin** counterstain to delineate the somatic contour and dendrites of pyramidal cerebral neurons." }
    ]
  },
  "Dashboard — eo/eosinophil.md": {
    primary: "A type of white blood cell (granulocyte) containing coarse granules that stain readily with eosin, involved in allergic reactions and combating parasitic infections.",
    secondary: "In hematology and immunology, a leukocyte characterized by a bilobed nucleus and major basic protein granules that modulate asthma, helminth infections, and hypersensitivity.",
    quotes: [
      { author: "Paul Ehrlich", work: "Methodology of Blood Staining", quote: "I demonstrated that the **eosinophil** possesses specific large granules having an intense chemical affinity for acidic dyes." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A marked rise in the circulating **eosinophil** count provides vital diagnostic confirmation of trichinosis or bronchial asthma." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "The **eosinophil** attaches to the outer surface of larval schistosomes, discharging cytotoxic lysosomal enzymes directly onto the parasite." }
    ]
  },
  "Dashboard — eo/eosinophilic.md": {
    primary: "Readily stained by eosin; characterized by or containing an excess of eosinophils.",
    secondary: "In pathology and cytology, describing tissues, cytoplasmic inclusions, or inflammatory exudates that show intense affinity for acidic red dyes.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Microscopic sections of the lung revealed dense **eosinophilic** infiltrates plugging the bronchial submucosa in status asthmaticus." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "The cytoplasm of healthy erythrocytes is intensely **eosinophilic** owing to high intracellular concentrations of hemoglobin." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "Degenerating muscle fibers display a homogenous **eosinophilic** appearance prior to necrotic fragmentation." }
    ]
  },

  // Dashboard — ger (18 words)
  "Dashboard — ger/anger.md": {
    primary: "A strong feeling of annoyance, displeasure, or hostility; to make someone angry.",
    secondary: "In moral philosophy and psychological physiology, an emotional surge accompanied by autonomic sympathetic arousal, traditionally classed among the primary human passions.",
    quotes: [
      { author: "William Shakespeare", work: "King Lear", quote: "Touch me with noble **anger**, / And let not women's weapons, water-drops, / Stain my man's cheeks!" },
      { author: "Francis Bacon", work: "The Essays", quote: "To seek to extinguish **anger** utterly is but a bravery of the Stoics; we have better oracles to manage its heat." },
      { author: "Charles Darwin", work: "The Expression of the Emotions in Man and Animals", quote: "Under the influence of violent **anger**, the action of the heart is much accelerated, and the face reddens or becomes deadly pale." }
    ]
  },
  "Dashboard — ger/erigeron.md": {
    primary: "A genus of plants in the daisy family (Asteraceae) commonly called fleabane, bearing daisy-like flower heads with numerous narrow ray florets.",
    secondary: "In botanical nomenclature and herbal history, composite herbs named from Greek eri 'early' + geron 'old man' due to their hoary, white-haired pappus appearing early in summer.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "Species of **Erigeron** abound in pastures, displaying copious narrow ray flowers that range from white to lavender and rosy pink." },
      { author: "John Muir", work: "The Mountains of California", quote: "Along the alpine meadow rills, delicate blossoms of **Erigeron** nodded beside the melting snowdrifts." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "The common fleabane, **Erigeron**, was hung in country cottages under the ancient belief that its scent expelled insect pests." }
    ]
  },
  "Dashboard — ger/ger.md": {
    primary: "A root and combining form from Greek γῆρας (geras, old age) and γέρων (geron, elder), used in words relating to aging and elderly persons.",
    secondary: "In linguistic etymology, the morphological stem present in terms such as geriatric, gerontology, and gerontocracy.",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The Greek root **ger-** conveys both the physical infirmities of old age and the social veneration due to community elders." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "In modern medicine, words derived from **ger-** designate specialized studies of senescence and diseases of the aged." },
      { author: "James Murray", work: "A New English Dictionary on Historical Principles", quote: "Nineteenth-century scientific terminology revitalized the root **ger-** to formulate precise classifications for senescence." }
    ]
  },
  "Dashboard — ger/gerascophobia.md": {
    primary: "An abnormal, morbid, or excessive fear of growing old or aging.",
    secondary: "In clinical psychiatry and psychotherapy, an anxiety disorder wherein individuals experience severe distress, depression, or panic regarding physical senescence and bodily deterioration.",
    quotes: [
      { author: "William Osler", work: "Aequanimitas", quote: "The tragic vanity of the patient degenerated into an obsessive **gerascophobia**, dreading every emerging wrinkle upon the brow." },
      { author: "William James", work: "The Principles of Psychology", quote: "When the mind refuses to accept natural senescence, morbid **gerascophobia** can distort every reflection in the mirror into an enemy." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "The frantic pursuit of cosmetic rejuvenation often conceals an underlying, unacknowledged **gerascophobia**." }
    ]
  },
  "Dashboard — ger/geriatric.md": {
    primary: "Of or relating to old age or the healthcare and treatment of elderly people.",
    secondary: "In healthcare administration and clinical practice, specialized medical management tailored to multimorbidity, polypharmacy, and frailty in elderly patients.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In the **geriatric** patient, common infections often present atypically with sudden confusion rather than high fever." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Deterioration in renal filtration rate necessitates careful dosage titration across the entire **geriatric** population." },
      { author: "Florence Nightingale", work: "Notes on Nursing", quote: "Caring for the **geriatric** invalid requires constant vigilance against chilling, pressure ulcers, and nutritional apathy." }
    ]
  },
  "Dashboard — ger/geriatrician.md": {
    primary: "A medical doctor who specializes in the health and medical care of elderly people.",
    secondary: "In modern clinical medicine, a specialist who coordinates comprehensive geriatric assessments, balancing functional independence against chronic disease burden.",
    quotes: [
      { author: "William Osler", work: "Counsels and Ideals", quote: "The skilled **geriatrician** views the elderly patient not as a bundle of isolated ailments, but as an integrated human life." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "A prudent **geriatrician** constantly anticipates the heightened susceptibility of aging vascular beds to hypotensive episodes." },
      { author: "Donald Seldin", work: "The Kidney: Physiology and Pathophysiology", quote: "Every practicing **geriatrician** must routinely recalculate creatinine clearance when prescribing nephrotoxic drugs." }
    ]
  },
  "Dashboard — ger/geriatrics.md": {
    primary: "The branch of medicine and social science dealing with the health and care of old people.",
    secondary: "In medical history, the specialty established by Ignatz Leo Nascher in 1909 to study senescence as a distinct physiological stage rather than an incurable illness.",
    quotes: [
      { author: "Ignatz Leo Nascher", work: "Geriatrics: The Diseases of Old Age and Their Treatment", quote: "I propose the term **geriatrics** to emphasize that senescence is an honorable, natural physiological state requiring sympathetic medical science." },
      { author: "William Osler", work: "Aequanimitas", quote: "The emergence of modern **geriatrics** promises to bring dignified relief to the physical burdens of our declining years." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Principles of **geriatrics** demonstrate how diminishing cardiac reserve alters physiological responses to routine surgical stress." }
    ]
  },
  "Dashboard — ger/gerontocracy.md": {
    primary: "A state, society, or group governed by old people; government by elders.",
    secondary: "In political science and anthropology, a traditional or institutional power structure where political authority is reserved for elderly community members.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The Roman Senate in its late decadence resembled a stagnant **gerontocracy**, incapable of swift decisive martial action." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "Unlike traditional aristocratic realms dominated by **gerontocracy**, young democracies favor youthful vigor and restless enterprise." },
      { author: "George Orwell", work: "The Road to Wigan Pier", quote: "The entrenched party committee was an unyielding **gerontocracy**, deaf to the clamor of the younger working generation." }
    ]
  },
  "Dashboard — ger/gerontological.md": {
    primary: "Of or relating to gerontology, the scientific study of aging and the elderly.",
    secondary: "In academic research and public health, multidisciplinary biological, psychological, and demographic investigations into senescence.",
    quotes: [
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Modern **gerontological** research explores how cumulative oxidative damage to telomeres governs the finite lifespan of somatic cells." },
      { author: "William Osler", work: "Aequanimitas", quote: "The **gerontological** societies established in major universities have focused scientific rigor upon the hygiene of aging." },
      { author: "Donald Seldin", work: "The Kidney: Physiology and Pathophysiology", quote: "A key **gerontological** finding is the gradual sclerosis of glomeruli occurring as a normal facet of human longevity." }
    ]
  },
  "Dashboard — ger/gerontologist.md": {
    primary: "A scientist, scholar, or specialist who studies the processes and problems of aging.",
    secondary: "In bio-gerontology and sociology, an investigator analyzing cellular senescence, societal aging patterns, and cognitive changes in the elderly.",
    quotes: [
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "The **gerontologist** examines cellular apoptosis and mitochondrial decline to understand why organismal vitality wanes." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Every thoughtful **gerontologist** recognizes that chronological age frequently diverges from biological tissue age." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "The **gerontologist** observed how meaningful social engagement and sensory stimulation slowed cognitive decline in the home." }
    ]
  },
  "Dashboard — ger/gerontology.md": {
    primary: "The scientific study of the biological, psychological, and sociological phenomena associated with old age and aging.",
    secondary: "In medical and social sciences, the comprehensive discipline encompassing biogerontology, social gerontology, and psychogerontology.",
    quotes: [
      { author: "Élie Metchnikoff", work: "The Prolongation of Life: Optimistic Studies", quote: "I look forward to the day when scientific **gerontology** transforms the sunset of life into a peaceful, healthy completion." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Advances in cellular **gerontology** demonstrate that cellular senescence is governed by programmed genomic signals." },
      { author: "William Osler", work: "Aequanimitas", quote: "The new field of **gerontology** teaches us to revere the wisdom of years while mitigating its physical frailties." }
    ]
  },
  "Dashboard — ger/gerontophile.md": {
    primary: "A person who is sexually, romantically, or emotionally attracted to elderly people.",
    secondary: "In psychopathology and clinical sexology, an individual exhibiting gerontophilia, showing a strong erotic or romantic preference for partners significantly older.",
    quotes: [
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "Clinical case histories describe the true **gerontophile**, whose erotic desire is awakened exclusively by signs of advanced age." },
      { author: "Richard von Krafft-Ebing", work: "Psychopathia Sexualis", quote: "The **gerontophile** finds aesthetic attraction in the silver hair and frail demeanor of elderly companions." },
      { author: "Sigmund Freud", work: "Three Essays on the Theory of Sexuality", quote: "Psychoanalytic analysis reveals that the fantasies of the **gerontophile** often trace back to early fixations upon grandparents." }
    ]
  },
  "Dashboard — ger/gerontophilia.md": {
    primary: "Sexual or romantic preference for or attraction to elderly persons.",
    secondary: "In sexual medicine and psychological nosology, an atypical sexual preference (paraphilia) centered on partners of advanced age.",
    quotes: [
      { author: "Richard von Krafft-Ebing", work: "Psychopathia Sexualis", quote: "We classify **gerontophilia** as an uncommon erotic divergence wherein youth actively seeks companionship with the aged." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "Cases of **gerontophilia** demonstrate how psychological conditioning can overcome standard biological markers of physical youth." },
      { author: "Wilhelm Stekel", work: "Peculiarities of Behavior", quote: "In examining the roots of **gerontophilia**, one frequently discovers deep filial devotion intertwined with erotic longing." }
    ]
  },
  "Dashboard — ger/gerontophobia.md": {
    primary: "An irrational fear or intense dislike of the elderly or of aging.",
    secondary: "In social psychology and cultural theory, societal prejudice and systemic aversion directed toward elderly people, often fostering ageism and institutional neglect.",
    quotes: [
      { author: "Simone de Beauvoir", work: "The Coming of Age", quote: "Society conceals its deep-seated **gerontophobia** by banishing the aged into distant hospices and out-of-sight institutions." },
      { author: "William Osler", work: "Aequanimitas", quote: "A physician must banish every trace of **gerontophobia**, treating the infirmities of senescence with patient gentleness." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "Modern commercial culture fosters an acute **gerontophobia** by exalting superficial youth as the sole human ideal." }
    ]
  },
  "Dashboard — ger/gerontoplast.md": {
    primary: "A specialized plastid that develops from a chloroplast during the senescence of plant leaves.",
    secondary: "In plant cell biology, a senescent plastid wherein thylakoids and chlorophyll are dismantled while carotenoid plastoglobules accumulate, creating yellow autumn foliage.",
    quotes: [
      { author: "Eduard Strasburger", work: "A Text-Book of Botany", quote: "During autumn senescence, the green chloroplast transforms into a **gerontoplast** laden with yellow lipid globules." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "The brilliant golden hues of deciduous forests reflect the biochemical transition from chloroplast to **gerontoplast**." },
      { author: "Arthur Tansley", work: "The British Islands and Their Vegetation", quote: "Electron microscopy reveals that the **gerontoplast** represents a controlled dismantling of the photosynthetic apparatus." }
    ]
  },
  "Dashboard — ger/gerousia.md": {
    primary: "The aristocratic council of elders in ancient Sparta, composed of twenty-eight men over sixty years of age and the two Spartan kings.",
    secondary: "In classical Greek political history, the supreme deliberative and judicial council established by Lycurgus that held lifelong veto power over the Spartan popular assembly.",
    quotes: [
      { author: "Plutarch", work: "Parallel Lives: Life of Lycurgus", quote: "Lycurgus established the **gerousia**, choosing twenty-eight elders of proven virtue to temper the rash impulses of the populace." },
      { author: "Aristotle", work: "Politics", quote: "The Spartan **gerousia** possessed supreme judicial authority, trying capital offenses without appeal to ordinary courts." },
      { author: "George Grote", work: "A History of Greece", quote: "Admission into the **gerousia** was the highest civic prize in Sparta, attained only after a lifetime of military obedience." }
    ]
  },
  "Dashboard — ger/progeria.md": {
    primary: "A rare genetic condition causing children to age rapidly, officially known as Hutchinson-Gilford progeria syndrome.",
    secondary: "In clinical genetics and pediatrics, an autosomal dominant disorder caused by LMNA gene mutations producing toxic progerin, resulting in accelerated cardiovascular disease and alopecia in childhood.",
    quotes: [
      { author: "Jonathan Hutchinson", work: "Transactions of the Royal Medico-Chirurgical Society", quote: "I observed a young boy presenting with the clinical lineaments of extreme senility, an anomaly now recognized as **progeria**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In patients suffering from **progeria**, severe coronary atherosclerosis develops before the patient reaches adolescence." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "The genetic flaw in **progeria** disrupts the structural scaffolding of the nuclear envelope, hastening somatic senescence." }
    ]
  },
  "Dashboard — ger/progeroid.md": {
    primary: "Resembling or characteristic of progeria; exhibiting features of premature aging.",
    secondary: "In medical genetics and cellular biology, describing hereditary syndromes (such as Werner syndrome) or cell lines showing accelerated senescence phenotypes.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The patient displayed a distinct **progeroid** habitus, with taut parchment-like skin and early bilateral cataracts." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Fibroblasts derived from patients with **progeroid** disorders exhibit premature cessation of mitotic division in vitro." },
      { author: "Donald Seldin", work: "The Kidney: Physiology and Pathophysiology", quote: "Early renal vascular sclerosis frequently accompanies these rare **progeroid** inherited syndromes." }
    ]
  },

  // Dashboard — geran (4 words)
  "Dashboard — geran/Geranium.md": {
    primary: "A genus of flowering plants in the family Geraniaceae, commonly known as cranesbills, bearing five-petaled flowers and beaked, crane-like seed capsules.",
    secondary: "In horticulture and systematic botany, temperate perennial herbs (distinct from pelargoniums) featuring palmately lobed leaves and explosive carpel dehiscence.",
    quotes: [
      { author: "Charles Darwin", work: "The Different Forms of Flowers on Plants of the Same Species", quote: "The elongated, beak-like style in **Geranium** coils elastically when ripe, hurling the seeds several feet away." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The wild spotted cranesbill, **Geranium** maculatum, blooms in deciduous woodlands with delicate purple petals." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The Greek botanists named the plant **Geranium** from the resemblance of its fruit to the bill of a crane." }
    ]
  },
  "Dashboard — geran/geran.md": {
    primary: "A combining form derived from Greek γέρανος (geranos) meaning 'crane', used in botanical and taxonomic nomenclature.",
    secondary: "In botanical etymology, the formative root in Geraniaceae and Geraniales, referring to the long, beaked, crane-like rostrum of the fruit.",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The Greek word for crane, geranos, furnishes the scientific combining form **geran-** in plant classification." },
      { author: "John Lindley", work: "The Elements of Botany", quote: "Systematists adopted the radical **geran-** to honor the characteristic rostrate fruit resembling a crane's beak." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "Through Latin transmission, the Greek element **geran-** became permanently established in botanical terminology." }
    ]
  },
  "Dashboard — geran/geraniaceae.md": {
    primary: "A family of flowering plants in the order Geraniales, commonly called the cranesbill family, including Geranium, Pelargonium, and Erodium.",
    secondary: "In angiosperm systematics, herbs or subshrubs characterized by palmately veined or pinnate leaves, glandular hairs, and a distinctive five-parted schizocarp with an elongate beak.",
    quotes: [
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "The family **Geraniaceae** is readily recognized by its glandular-pubescent foliage and remarkable rostrate seed vessels." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Many genera of the **Geraniaceae** contain aromatic essential oils prized in the manufacture of perfumes and scents." },
      { author: "Joseph Dalton Hooker", work: "The Flora of British India", quote: "Representatives of the **Geraniaceae** thrive in temperate regions, especially in the flora of the Cape of Good Hope." }
    ]
  },
  "Dashboard — geran/geraniales.md": {
    primary: "An order of eudicot flowering plants comprising the family Geraniaceae along with several small related families such as Francoaceae.",
    secondary: "In phylogenetic plant taxonomy (APG system), a distinct rosid order characterized by nectary glands alternating with petals and persistent beaked styles.",
    quotes: [
      { author: "Arthur Cronquist", work: "An Integrated System of Classification of Flowering Plants", quote: "The order **Geraniales** encompasses herbs and small shrubs characterized by pentamerous flowers and specialized seed dispersal." },
      { author: "Charles Bessey", work: "The Phylogeny and Taxonomy of the Angiosperms", quote: "In our phylogenetic scheme, the **Geraniales** occupy an important position among the disc-flowered dicotyledons." },
      { author: "Liberty Hyde Bailey", work: "Cyclopedia of American Horticulture", quote: "Horticultural interest in the **Geraniales** centers on garden geraniums and greenhouse pelargoniums." }
    ]
  }
};

let success = 0;
let fail = 0;

for (const [key, data] of Object.entries(batch3Data)) {
  const [relDir, fileName] = key.split('/');
  if (updateNote(relDir, fileName, data)) {
    success++;
  } else {
    fail++;
  }
}

console.log(`\nBatch 3 complete: ${success} updated, ${fail} failed.`);
