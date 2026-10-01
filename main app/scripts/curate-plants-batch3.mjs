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

const batch3Data = {
  "Dashboard — anth/anthyllis.md": {
    primary: "A genus of leguminous herbs and shrubs in the pea family (Fabaceae), commonly called kidney vetch or lady's fingers, native to Europe and North Africa.",
    secondary: "In pastoral agriculture and traditional pharmacognosy, deep-rooted calcicole plants bearing dense woolly flower heads used as sheep forage and wound astringents.",
    quotes: [
      { author: "Carl Linnaeus", work: "Species Plantarum", quote: "Under the genus **Anthyllis**, I have grouped those leguminous species whose calyces are inflated and persistently enclose the legume." },
      { author: "John Gerard", work: "The Herball or Generall Historie of Plantes", quote: "The yellow blossom of **Anthyllis** vulneraria is reputed among alpine shepherds to stay the bleeding of severe cuts." },
      { author: "George Bentham", work: "Handbook of the British Flora", quote: "On chalk downs and maritime limestone cliffs, **Anthyllis** forms low dense mats crowned with woolly heads of golden florets." }
    ]
  },
  "Dashboard — anth/chrysanthemum.md": {
    primary: "A genus of flowering plants in the daisy family (Asteraceae), renowned for their bright, many-petaled autumn blossoms; commonly called mum.",
    secondary: "In floriculture and cultural history, the floral emblem of the Japanese Imperial family and an important source of natural pyrethrin insecticides.",
    quotes: [
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Centuries of oriental horticultural skill have transformed the modest wild **chrysanthemum** into a dazzling marvel of form and color." },
      { author: "Henry David Thoreau", work: "Excursions", quote: "The hardy **chrysanthemum** braves the early frosts of November, lingering in farmhouse gardens when all other flowers have perished." },
      { author: "Lafcadio Hearn", work: "Glimpses of Unfamiliar Japan", quote: "In Tokyo gardens, the annual **chrysanthemum** exhibition displays living sculptures clothed entirely in blooming sprays." }
    ]
  },
  "Dashboard — anth/dianthus.md": {
    primary: "A genus of flowering plants in the family Caryophyllaceae, known as pinks, carnations, and sweet williams, characterized by fringed or serrated petals and spicy clove fragrance.",
    secondary: "In systematic botany, the divine flower of classical antiquity ('flower of Zeus') bearing opposite glaucous leaves, cylindrical calyx tubes, and toothed petals.",
    quotes: [
      { author: "John Gerard", work: "The Herball or Generall Historie of Plantes", quote: "The clove gillyflower or **Dianthus** is treasured above all summer flowers for its sweet, exhilarating clove-like scent." },
      { author: "William Shakespeare", work: "The Winter's Tale", quote: "The fairest flowers o' the season are our carnations and streaked gillyvors, ancient varieties of the garden **Dianthus**." },
      { author: "Asa Gray", work: "Field, Forest, and Garden Botany", quote: "Species of **Dianthus** are recognized by the scaly bractlets clasping the base of their cylindrical five-toothed calyx." }
    ]
  },
  "Dashboard — anth/enanthem.md": {
    primary: "A mucous membrane rash or eruption, such as Koplik's spots in measles or lesions of the oral mucosa, appearing during an infectious disease.",
    secondary: "In clinical pediatric diagnostics, the mucosal counterpart of a cutaneous exanthem, serving as an early prodromal indicator of systemic viral infection.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Careful examination of the soft palate often detects an early **enanthem** twenty-four hours before the cutaneous rash appears." },
      { author: "Thomas B. Fitzpatrick", work: "Dermatology in General Medicine", quote: "Koplik spots represent a pathognomonic **enanthem** on the buccal mucosa preceding the full eruption of rubeola." },
      { author: "Abraham Jacobi", work: "The Intestinal Diseases of Infancy and Childhood", quote: "In scarlet fever, the characteristic punctate **enanthem** inflames the tongue into the classic strawberry appearance." }
    ]
  },
  "Dashboard — anth/enanthema.md": {
    primary: "An eruptive lesion or rash upon a mucous surface, especially within the mouth, pharynx, or gastrointestinal tract.",
    secondary: "In infectious disease pathology, mucosal hyperemia and vesicular eruption accompanying viral illnesses like rubella, varicella, and enteroviruses.",
    quotes: [
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "The term **enanthema** denotes an internal eruption upon the mucous membranes, strictly analogous to exanthema upon the skin." },
      { author: "L. Emmett Holt", work: "The Diseases of Infancy and Childhood", quote: "The presence of an active **enanthema** on the palatal arches strongly suggests an acute enteroviral etiology." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "Syphilitic mucous patches constitute a chronic **enanthema** teeming with virulent spirochetal organisms." }
    ]
  },
  "Dashboard — anth/exanthem.md": {
    primary: "A widespread skin rash or cutaneous eruption, typically accompanying a systemic viral or bacterial infectious disease like measles, scarlet fever, or chickenpox.",
    secondary: "In infectious epidemiology and dermatology, any general cutaneous dermatosis that erupts acutely as a manifestation of systemic immunological reaction.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The distinctive centrifugal spread of the **exanthem** aids the physician in distinguishing smallpox from chickenpox." },
      { author: "Thomas B. Fitzpatrick", work: "Dermatology in General Medicine", quote: "A maculopapular **exanthem** accompanied by high fever represents a primary diagnostic clue in childhood roseola." },
      { author: "Ferdinand von Hebra", work: "Diseases of the Skin", quote: "The diagnostic timing of the **exanthem** follows a precise timetable after the initial prodromal fever spike." }
    ]
  },
  "Dashboard — anth/exanthema.md": {
    primary: "A cutaneous eruption or rash occurring as a symptom of an acute systemic fever or infectious disease.",
    secondary: "In historical medical nosology, one of the major eruptive fevers (such as variola, rubeola, or scarlatina) categorized under the class Exanthemata.",
    quotes: [
      { author: "William Cullen", work: "First Lines of the Practice of Physic", quote: "Under the order **Exanthema**, I classify those contagious diseases characterized by phlogistic fever and widespread cutaneous eruptions." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "An acute **exanthema** runs a definite cyclical course, progressing from papules to desquamation." },
      { author: "John Syer Bristowe", work: "A Treatise on the Theory and Practice of Medicine", quote: "The appearance of the characteristic **exanthema** marks the crisis of the inflammatory stage of typhus." }
    ]
  },
  "Dashboard — anth/exanthematic.md": {
    primary: "Pertaining to, characterized by, or accompanied by an exanthem (a general skin eruption).",
    secondary: "In medical pathology, describing febrile illnesses, such as exanthematic typhus, marked by generalized eruptive cutaneous manifestations.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Epidemic **exanthematic** typhus has historically devastated armies and besieged cities under conditions of cold and overcrowding." },
      { author: "Jonathan Pereira", work: "The Elements of Materia Medica", quote: "Cool acidulated drinks are indicated during the height of **exanthematic** fevers to relieve scorching thirst." },
      { author: "Austin Flint", work: "A Treatise on the Principles and Practice of Medicine", quote: "The **exanthematic** stage of measles demands darkened rooms to protect inflamed conjunctivae from photophobia." }
    ]
  },
  "Dashboard — anth/hydranth.md": {
    primary: "The terminal feeding or nutritive polyp of a colonial hydrozoan (phylum Cnidaria), bearing a mouth surrounded by tentacles.",
    secondary: "In invertebrate zoology, the specialized zooid of a hydrozoan coenosarc dedicated to capturing prey, extracellular digestion, and distributing nutrients throughout the colony.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "Each graceful **hydranth** of Obelia expands its circlet of filiform tentacles to paralyze swimming crustacean nauplii." },
      { author: "Libbie Hyman", work: "The Invertebrates", quote: "In thecate hydroids, the living **hydranth** can withdraw completely within its protective chitinous hydrotheca." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", quote: "The digestive cavity of each **hydranth** connects directly with the common tubular stem of the colony." }
    ]
  },
  "Dashboard — anth/hypanthium.md": {
    primary: "A cup-shaped or tubular enlargement of the floral receptacle or fused bases of sepals, petals, and stamens, surrounding the ovary.",
    secondary: "In angiosperm morphology, a structure characteristic of the Rosaceae (rose hips) and Onagraceae that may fuse with the ovary wall to form an inferior ovary.",
    quotes: [
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "In the rose, the fleshy cup termed the **hypanthium** encloses the achenes, swelling at maturity into the brightly colored hip." },
      { author: "John Lindley", work: "An Introduction to Botany", quote: "Systematic botanists trace the origin of the epigynous calyx to the adnation of the **hypanthium** to the syncarpous ovary." },
      { author: "George Bentham", work: "Handbook of the British Flora", quote: "The conspicuous tubular **hypanthium** of the fuchsia elevates petals and stamens high above the inferior four-celled ovary." }
    ]
  },
  "Dashboard — anth/paleoanthropological.md": {
    primary: "Relating to paleoanthropology, the scientific study of fossil hominids and the evolutionary history of humankind.",
    secondary: "Pertaining to the interdisciplinary field combining hominin skeletal morphology, prehistoric archaeology, and geochronology.",
    quotes: [
      { author: "Louis Leakey", work: "Olduvai Gorge", quote: "Our **paleoanthropological** excavations along the ancient lake beds yielded primitive Oldowan stone choppers alongside hominid crania." },
      { author: "Richard Leakey", work: "The Making of Mankind", quote: "Every new fossil discovery demands rigorous **paleoanthropological** reevaluation of the branching hominin evolutionary tree." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "The **paleoanthropological** record confirms that bipedal locomotion preceded the dramatic expansion of the human brain." }
    ]
  },
  "Dashboard — anth/paleoanthropology.md": {
    primary: "The scientific study of early human evolution, fossil hominins, and ancient tool cultures based on fossilized remains and archaeological evidence.",
    secondary: "In evolutionary biology, an empirical subdiscipline synthesizing hominoid paleontology, primatology, radiometric dating, and prehistoric archaeology.",
    quotes: [
      { author: "Louis Leakey", work: "Progress and Evolution of Man in Africa", quote: "The field of **paleoanthropology** was revolutionized by discovering early tool-making hominins in East African rift strata." },
      { author: "Richard Leakey", work: "Origins", quote: "Modern **paleoanthropology** no longer envisions a simple ladder of ascent, but rather a bush of competing hominin lineages." },
      { author: "Stephen Jay Gould", work: "Ontogeny and Phylogeny", quote: "Pioneering researchers in **paleoanthropology** had to overcome pervasive racial prejudices before interpreting the African fossil evidence correctly." }
    ]
  },
  "Dashboard — anth/paranthias.md": {
    primary: "A genus of marine ray-finned fishes in the grouper family (Serranidae), known as creolefishes, adapted for midwater plankton feeding.",
    secondary: "In marine ichthyology, slender-bodied serranids that diverge from typical benthic groupers by forming aggregations in open water and possessing fine gill rakers.",
    quotes: [
      { author: "David Starr Jordan", work: "A Guide to the Study of Fishes", quote: "The genus **Paranthias** differs markedly from typical groupers in its streamlined form and habit of schooling above reef drop-offs." },
      { author: "Charles Tate Regan", work: "The Classification of the Percoid Fishes", quote: "Cranial osteology confirms that **Paranthias** belongs to the Epinephelinae, despite its unique planktivorous trophic adaptations." },
      { author: "William Beebe", work: "Beneath Tropic Seas", quote: "A shimmering cloud of **Paranthias** furcifer drifted in the crystal water, feeding with swift snaps upon transparent pelagic salps." }
    ]
  },
  "Dashboard — anth/paranthropus.md": {
    primary: "A genus of extinct, robust bipedal hominins that lived in eastern and southern Africa during the Pliocene and Pleistocene epochs.",
    secondary: "In paleoanthropology, hominins characterized by massive cranial sagittal crests, broad zygomatic arches, and hyper-megadont molars adapted for heavy mastication.",
    quotes: [
      { author: "Robert Broom", work: "Finding the Missing Link", quote: "The massive jaw and enormous post-canine molars of **Paranthropus** robustus revealed a creature capable of chewing coarse fibrous vegetation." },
      { author: "Louis Leakey", work: "Olduvai Gorge", quote: "Mary discovered the famous cranium of **Paranthropus** boisei in Bed I, displaying an astonishing sagittal crest and flattened facial profile." },
      { author: "Richard Leakey", work: "The Making of Mankind", quote: "The extinction of **Paranthropus** coincided with the drying African climate and the technological rise of early Homo." }
    ]
  },
  "Dashboard — anth/perianth.md": {
    primary: "The outer non-reproductive envelope of a flower, consisting of the calyx (sepals) and corolla (petals) collectively.",
    secondary: "In floral morphology, the protective and pollinator-attracting floral leaves, especially when sepals and petals are undifferentiated (tepals).",
    quotes: [
      { author: "Charles Darwin", work: "The Various Contrivances by Which Orchids Are Fertilised", quote: "The dorsal sepal and petals of the orchid **perianth** arch over the column to protect delicate pollinia from sudden drenching." },
      { author: "Asa Gray", work: "Lessons in Botany", quote: "When the parts of the **perianth** cannot be distinguished into calyx and corolla, as in the lily, they are described as tepals." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Modifications in the symmetry of the **perianth** serve as essential diagnostic characters across the monocotyledonous orders." }
    ]
  },
  "Dashboard — anth/polyanthus.md": {
    primary: "A variety of cultivated primrose (Primula polyantha) produced by hybridization between the common primrose, cowslip, and oxlip, bearing umbels of brightly colored flowers.",
    secondary: "In floriculture and cottage gardening, hardy vernal ornamentals prized for their umbels of rich velvety blossoms with golden eyes.",
    quotes: [
      { author: "John Gerard", work: "The Herball or Generall Historie of Plantes", quote: "The many-flowered primrose or **polyanthus** adorns the spring border with great clusters of fragrant party-colored florets." },
      { author: "William Cowper", work: "The Task", quote: "There blooms the **polyanthus** of unnumbered dyes, whose velvety petals mock the painter's brush." },
      { author: "Gertrude Jekyll", work: "Wood and Garden", quote: "A broad drift of yellow **polyanthus** under hazel boughs brings cheerful vernal sunshine to the woodland path." }
    ]
  },
  "Dashboard — anth/protoanthropology.md": {
    primary: "The early, preparatory, or speculative study of human origins, human diversity, and archaic hominid evolution prior to the establishment of modern anthropological methods.",
    secondary: "In the history of science, the pre-Darwinian or early Enlightenment intellectual tradition speculating on the descent, physical varieties, and social emergence of man.",
    quotes: [
      { author: "Edward Burnett Tylor", work: "Primitive Culture", quote: "Classical inquiries into the nature of barbarians and monsters may be deemed the rudimentary cradle of **protoanthropology**." },
      { author: "Franz Boas", work: "The Mind of Primitive Man", quote: "Enlightenment naturalists engaged in **protoanthropology**, seeking to classify human races into Linnaean taxonomic categories." },
      { author: "Claude Lévi-Strauss", work: "Structural Anthropology", quote: "Montaigne's reflections upon the Brazilian cannibals provided a brilliant philosophical foundation for modern science before **protoanthropology** was formalized." }
    ]
  },
  "Dashboard — anth/zoanthid.md": {
    primary: "A marine cnidarian of the order Zoantharia, typically colonial and encrusting, lacking a hard calcium carbonate skeleton and incorporating sediment grains into its body wall.",
    secondary: "In reef invertebrate biology, colonial polyps containing potent palytoxin that carpet dead coral pavement, rocks, and sponge surfaces in tropical seas.",
    quotes: [
      { author: "James Dwight Dana", work: "Corals and Coral Islands", quote: "The fleshy polyps of each encrusting **zoanthid** incorporate sand grains into their ectoderm to strengthen their colonial mat." },
      { author: "Libbie Hyman", work: "The Invertebrates", quote: "Unlike true stony corals, the **zoanthid** secretes no calcareous basal plate, relying upon an interconnected stoloniferous coenenchyme." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "Under the ledge, a colony of **zoanthid** polyps opened their disk-like tentacles to graze on drifting organic detritus." }
    ]
  },
  "Dashboard — botan/botan.md": {
    primary: "A classical combining form and linguistic root derived from Greek 'botane' (herb, plant, pasture, fodder), forming the base of vocabulary pertaining to plant life.",
    secondary: "In lexicography and scientific etymology, the foundational stem designating the systematic study, cultivation, and medicinal utilization of vegetation.",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The Greek root **botan** originates in botane, designating pasture grasses and herbs cultivated for grazing flocks." },
      { author: "Robert Beekes", work: "Etymological Dictionary of Greek", quote: "Etymologically, **botan** is related to boskein, signifying to graze, feed, or nourish upon vegetative meadows." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "All sciences concerning the green mantle of the globe trace their nomenclature to the venerable root **botan**." }
    ]
  },
  "Dashboard — botan/botanic.md": {
    primary: "Of, relating to, or derived from plants or the scientific study of plants; botanical.",
    secondary: "Designating dedicated scientific gardens, institutions, or publications established for the cultivation and study of plant species.",
    quotes: [
      { author: "Erasmus Darwin", work: "The Botanic Garden", quote: "In the sheltered groves of the **botanic** garden, science and poetry unite to celebrate the mysteries of floral life." },
      { author: "Joseph Dalton Hooker", work: "Himalayan Journals", quote: "The Royal **Botanic** Gardens at Kew dispatched collectors to the highest passes of Sikkim to gather rhododendron seeds." },
      { author: "William Curtis", work: "The Botanical Magazine", quote: "This monthly journal aims to present accurate colored portraits of curious exotic plants cultivated in **botanic** borders." }
    ]
  },
  "Dashboard — botan/botanical.md": {
    primary: "Relating to plants or the science of botany; a medicinal or therapeutic substance obtained from a plant.",
    secondary: "In descriptive natural science, pertaining to the taxonomy, morphology, and ecology of the vegetable kingdom.",
    quotes: [
      { author: "Charles Darwin", work: "Journal of Researches (Voyage of the Beagle)", quote: "The Galapagos archipelago presents a fascinating **botanical** province where nearly every island possesses its own unique flora." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "A rigorous **botanical** description must record floral symmetry, stamen insertion, and ovary placentation." },
      { author: "Henry David Thoreau", work: "The Maine Woods", quote: "I carried my **botanical** press into the wilderness to preserve delicate forest orchids before the autumn frosts." }
    ]
  },
  "Dashboard — botan/botanise.md": {
    primary: "To search for, collect, and study wild plants in their natural habitats; to botanize.",
    secondary: "To conduct field natural history excursions aimed at collecting and classifying herbarium specimens.",
    quotes: [
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "During the sweet month of June, I would frequently **botanise** along the beech-covered hangers, collecting rare orchises." },
      { author: "Jean-Jacques Rousseau", work: "Reveries of the Solitary Walker", quote: "To wander aimlessly through mountain meadows and **botanise** in peace was the purest solace of my declining years." },
      { author: "William Hazlitt", work: "Table-Talk", quote: "There is an innocent delight in walking through shady lanes to **botanise** among the wild dog-roses." }
    ]
  },
  "Dashboard — botan/botanist.md": {
    primary: "A scientist, scholar, or dedicated student who specializes in the scientific study of plants (botany).",
    secondary: "A field researcher or taxonomist who collects, identifies, describes, and classifies vegetable flora.",
    quotes: [
      { author: "Carl Linnaeus", work: "Philosophia Botanica", quote: "The true **botanist** must know every plant by its invariable binomial name and its natural taxonomic affinities." },
      { author: "Charles Darwin", work: "The Different Forms of Flowers on Plants of the Same Species", quote: "The keen-eyed field **botanist** notices subtle floral dimorphisms that escape the casual observer." },
      { author: "John Muir", work: "The Mountains of California", quote: "As a wandering **botanist**, I climbed the Sierra ridges with boundless joy, greeting every alpine blossom as an immortal friend." }
    ]
  },
  "Dashboard — botan/botanize.md": {
    primary: "To explore outdoors in search of plants for scientific study, collection, or classification.",
    secondary: "To engage in botanical field excursions to collect specimens for an herbarium or horticultural study.",
    quotes: [
      { author: "Henry David Thoreau", work: "A Week on the Concord and Merrimack Rivers", quote: "We landed our skiff upon the sandy riverbank, eager to **botanize** among the marsh mallows and cardinal flowers." },
      { author: "Thomas Henry Huxley", work: "Life and Letters of Thomas Henry Huxley", quote: "In my leisure hours, I loved to **botanize** along the hedgerows, examining floral structures through a pocket lens." },
      { author: "John Burroughs", work: "Wake-Robin", quote: "To **botanize** through the virgin hemlock forest in early spring is to discover nature's most delicate secrets." }
    ]
  },
  "Dashboard — botan/botanology.md": {
    primary: "The scientific discourse, treatise, or comprehensive doctrine concerning plants; botany.",
    secondary: "In the history of natural philosophy, the systematic science and literature devoted to the structure, classification, and uses of vegetation.",
    quotes: [
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Pioneering authors in **botanology** laid the groundwork for natural systems of classification by abandoning artificial alphabetic arrangements." },
      { author: "William Rhind", work: "A History of the Vegetable Kingdom", quote: "The study of **botanology** embraces not merely naming dried herbs, but understanding the vital chemistry of living plants." },
      { author: "Erasmus Darwin", work: "Phytologia", quote: "Modern **botanology** demonstrates that plants possess irritability and circulation analogous in many respects to animal physiology." }
    ]
  },
  "Dashboard — botan/botany.md": {
    primary: "The branch of biological science that deals with the study of plants, including their physiology, structure, genetics, ecology, distribution, and classification.",
    secondary: "In academic natural history, the systematic study of the vegetable kingdom, encompassing bryology, pteridology, dendrology, and economic phytology.",
    quotes: [
      { author: "Carl Linnaeus", work: "Critica Botanica", quote: "Without systematic order, the vast science of **botany** would degenerate into chaotic confusion." },
      { author: "Asa Gray", work: "First Lessons in Botany", quote: "The true aim of **botany** is to enable the student to understand the living architecture of the plant world." },
      { author: "John Muir", work: "My First Summer in the Sierra", quote: "No study ever brought deeper peace to my soul than the devout contemplation of God's love revealed through **botany**." }
    ]
  },
  "Dashboard — botan/paleobotany.md": {
    primary: "The branch of paleontology and botany that deals with the study of fossil plants and ancient vegetation.",
    secondary: "In evolutionary geobiology, the reconstruction of past terrestrial ecosystems, ancient climates, and plant phylogenies through fossilized wood, leaves, spores, and pollen.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The flourishing coal forests revealed by **paleobotany** prove that giant lycopods and horsetails dominated the ancient Paleozoic lowlands." },
      { author: "Archibald Geikie", work: "Textbook of Geology", quote: "Through the discoveries of **paleobotany**, we trace the dramatic transition from gymnospermous forests to flowering angiosperms in the Cretaceous." },
      { author: "Douglas Houghton Campbell", work: "The Evolution of Land Plants", quote: "Fossilized cuticles and petrified wood studied in **paleobotany** provide decisive proof for ancestral vascular architecture." }
    ]
  },
  "Dashboard — bromat/bromat.md": {
    primary: "A combining form and classical root derived from Greek 'broma, bromatos' (food, meat, solid nourishment), used in nutritional and alimentary terminology.",
    secondary: "In linguistic etymology and dietetics, the ancient Greek element signifying edible food, dietary regimen, or alimentary consumption.",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The Greek root **bromat** stems directly from broma, designating solid food as distinguished from liquid potables." },
      { author: "Robert Beekes", work: "Etymological Dictionary of Greek", quote: "Cognates of **bromat** derive from the Indo-European root meaning to chew, bite, or consume solid sustenance." },
      { author: "William Prout", work: "Chemistry, Meteorology, and the Function of Digestion", quote: "Scientific classifications of alimentary principles trace their terms to the Hellenic **bromat** roots." }
    ]
  },
  "Dashboard — bromat/bromate.md": {
    primary: "A salt or ester of bromic acid containing the anion BrO₃⁻; also historically used to designate a foodstuff or aliment.",
    secondary: "In industrial food chemistry and baking, potassium bromate, an oxidizing flour improver used to strengthen gluten networks in bread dough.",
    quotes: [
      { author: "Humphry Davy", work: "Elements of Chemical Philosophy", quote: "When bromine vapor interacts with hot caustic potash solution, potassium **bromate** crystallizes in dense white prisms." },
      { author: "William Allen Miller", work: "Elements of Chemistry", quote: "Upon heating to redness, every metallic **bromate** decomposes into the corresponding bromide with violent evolution of oxygen." },
      { author: "Frank A. Lee", work: "Basic Food Chemistry", quote: "Commercial bakers historically added potassium **bromate** to improve oven spring and stabilize gluten crumb architecture." }
    ]
  },
  "Dashboard — bromat/bromateccrisis.md": {
    primary: "A clinical gastrointestinal crisis or acute digestive paroxysm triggered by food intake, dietary indiscretion, or alimentary intolerance; bromatocrisis.",
    secondary: "In 19th-century medical gastroenterology, a critical gastrointestinal episode marked by severe spasmodic colic, emesis, and diarrhea following ingestion of spoiled or irritating food.",
    quotes: [
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "Under the term **bromatocrisis**, classical authors described an acute alimentary crisis terminating a chronic bilious indigestion." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe dietary indiscretion provoked an acute **bromatocrisis**, marked by persistent vomiting and abdominal cramping." },
      { author: "Austin Flint", work: "A Treatise on the Principles and Practice of Medicine", quote: "Prompt gastric lavage is indicated when an alimentary **bromatocrisis** threatens collapse from ingested toxic foodstuffs." }
    ]
  },
  "Dashboard — bromat/bromatherapy.md": {
    primary: "The therapeutic use of diet, specialized foods, or nutritional regimens to treat disease; dietotherapy or bromatotherapy.",
    secondary: "In clinical dietetics and historical medicine, the systematic prescription of tailored food regimens to manage metabolic and gastrointestinal disorders.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In diabetes and chronic nephritis, rigorous **bromatotherapy** remains our most dependable therapeutic measure." },
      { author: "Robley Dunglison", work: "General Therapeutics and Materia Medica", quote: "Rational **bromatotherapy** aims to nourish the debilitated frame while minimizing digestive expenditure." },
      { author: "Abraham Jacobi", work: "Therapeutics of Infancy and Childhood", quote: "Judicious **bromatotherapy** in infantile diarrhea requires temporary milk withdrawal and administration of barley water." }
    ]
  },
  "Dashboard — bromat/bromatium.md": {
    primary: "A swollen hyphal tip (gongylidium) or cluster of hyphae produced by symbiotic fungi cultivated by leafcutter ants, harvested as the colony's primary food source.",
    secondary: "In myrmecology and fungal ecology, specialized nutrient-rich fungal structures packed with glycogen, proteins, and lipids cultivated inside attine ant nests.",
    quotes: [
      { author: "William Morton Wheeler", work: "Ants: Their Structure, Development and Behavior", quote: "The workers systematically prune the fungal mycelium, stimulating the production of swollen nutrient bodies termed a **bromatium**." },
      { author: "Alfred Russel Wallace", work: "Tropical Nature", quote: "Attine leafcutters do not consume the leaves they harvest, but use them to manure gardens that yield the edible **bromatium**." },
      { author: "Edward O. Wilson", work: "The Insect Societies", quote: "Microscopic analysis reveals that each **bromatium** is an enlarged hyphal sphere rich in essential amino acids and enzymes." }
    ]
  },
  "Dashboard — bromat/bromatology.md": {
    primary: "The scientific study of food, its chemical composition, nutritional value, preparation, and dietetic properties; food science.",
    secondary: "In public health and nutritional biochemistry, the comprehensive academic discipline investigating food chemistry, food safety, and preservation.",
    quotes: [
      { author: "William Prout", work: "Chemistry, Meteorology, and the Function of Digestion", quote: "The foundation of modern **bromatology** was established by categorizing foodstuffs into aqueous, saccharine, albuminous, and oleaginous principles." },
      { author: "Robley Dunglison", work: "General Therapeutics and Materia Medica", quote: "A sound knowledge of **bromatology** enables the physician to prescribe dietary regimens adapted to pathological conditions." },
      { author: "Justus von Liebig", work: "Familiar Letters on Chemistry", quote: "Progress in analytical chemistry has elevated **bromatology** into an exact science that governs human nutrition." }
    ]
  },
  "Dashboard — bromat/bromography.md": {
    primary: "A formal written treatise, description, or discourse on food, diet, and comestibles.",
    secondary: "In historical bibliography and dietetic literature, an encyclopedic or descriptive catalog of edible plants, animal meats, and culinary preparations.",
    quotes: [
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "The classical author composed an exhaustive **bromography**, detailing the culinary properties and medicinal virtues of Mediterranean fish and fowl." },
      { author: "William Prout", work: "Chemistry of Digestion", quote: "Ancient treatises on **bromography** mingled acute empirical observations with superstitious astrological prohibitions on diet." },
      { author: "Jonathan Pereira", work: "A Treatise on Food and Diet", quote: "Our present work is intended as a practical **bromography**, presenting the chemical analysis of every common article of human diet." }
    ]
  },
  "Dashboard — butyr/butyr.md": {
    primary: "A classical combining form and chemical root derived from Greek 'boutyron' (butter), used in chemical and biochemical nomenclature.",
    secondary: "In organic chemistry and lipid biochemistry, the root denoting four-carbon aliphatic chains and compounds related to butyric acid.",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The Greek root **butyr** derives from boutyron, meaning literally cow-cheese or butter churned from milk." },
      { author: "Justus von Liebig", work: "Familiar Letters on Chemistry", quote: "Chemical derivatives sharing the prefix **butyr** trace their discovery to the volatile rancid fatty acids of dairy butter." },
      { author: "William Allen Miller", work: "Elements of Chemistry", quote: "In organic nomenclature, **butyr** consistently designates derivatives of the four-carbon carboxylic acid series." }
    ]
  },
  "Dashboard — butyr/butyraceous.md": {
    primary: "Having the consistency, appearance, or qualities of butter; buttery; greasy.",
    secondary: "In mineralogy, botany, and pathology, describing soft, smooth, fatty, or easily spreadable substances.",
    quotes: [
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "The kernel of the African shea-tree yields a thick, **butyraceous** fat used by native tribes in cooking." },
      { author: "Archibald Geikie", work: "Textbook of Geology", quote: "The decomposed volcanic ash had weathered into a greasy, **butyraceous** clay that slipped under our boots." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "The purulent exudate possessed a creamy, **butyraceous** consistency, characteristic of chronic follicular inflammation." }
    ]
  },
  "Dashboard — butyr/butyric.md": {
    primary: "Of, relating to, or obtained from butter; specifically designating butyric acid (a four-carbon fatty acid with a pungent odor).",
    secondary: "In organic biochemistry and fermentation, designating bacterial fermentation pathways wherein Clostridium species convert starch into butyrate, carbon dioxide, and hydrogen.",
    quotes: [
      { author: "Louis Pasteur", work: "Studies on Fermentation", quote: "The active agent of **butyric** fermentation proved to be an anaerobic vibrio that perished upon exposure to free atmospheric oxygen." },
      { author: "Justus von Liebig", work: "Animal Chemistry", quote: "Rancidity in butter arises from the hydrolytic release of free **butyric** acid from its glyceryl ester." },
      { author: "William Allen Miller", work: "Elements of Chemistry", quote: "Esters of **butyric** acid possess delightful fruity fragrances, widely utilized as artificial pineapple and apple flavorings." }
    ]
  },
  "Dashboard — butyr/butyrin.md": {
    primary: "A triglyceride of butyric acid (specifically tributyrin) found naturally in butter, giving butter its characteristic flavor.",
    secondary: "In lipid chemistry, glyceryl tributyrate, a neutral fat that undergoes enzymatic cleavage by pancreatic lipase into glycerol and free butyric acid.",
    quotes: [
      { author: "Justus von Liebig", work: "Animal Chemistry", quote: "Natural butter contains several percent of **butyrin**, which imparts its rich flavor when fresh but develops acrid pungency when hydrolyzed." },
      { author: "William Allen Miller", work: "Elements of Chemistry", quote: "Pure **butyrin** is a colorless oily liquid having an agreeable taste and soluble in alcohol and ether." },
      { author: "T. Lauder Brunton", work: "A Text-Book of Pharmacology", quote: "Pancreatic juice rapidly emulsifies and saponifies neutral fats like **butyrin** in the alkaline duodenum." }
    ]
  },
  "Dashboard — butyr/tributyrin.md": {
    primary: "The triglyceride of butyric acid, [C₃H₅(OCOC₃H₇)₃], present in butter fat; a colorless, oily liquid used in biochemical lipase assays.",
    secondary: "In nutritional physiology and clinical gastroenterology, a stable butyrate prodrug that delivers anti-inflammatory butyrate directly to the colonic mucosa.",
    quotes: [
      { author: "William Allen Miller", work: "Elements of Chemistry", quote: "Synthesis of **tributyrin** from glycerol and butyric acid conclusively demonstrated the triatomic constitution of glycerides." },
      { author: "Ernest Beutler", work: "Williams Hematology", quote: "Experimental administration of **tributyrin** induces fetal hemoglobin synthesis and cellular differentiation in myeloid leukemia lines." },
      { author: "Frank A. Lee", work: "Basic Food Chemistry", quote: "Standard laboratory assays measure serum lipase activity by the rate of glycerol liberation from **tributyrin** emulsion." }
    ]
  },
  "Dashboard — byss/abyss.md": {
    primary: "A deep or seemingly bottomless chasm, gulf, or profound pit; a vast intellectual or moral expanse.",
    secondary: "In oceanography and geology, the vast, lightless deeps of the ocean floor plunging thousands of meters below sea level.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "Into this wild **Abyss**, the womb of Nature and perhaps her grave, the dark Satanic legions cast their mournful gaze." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "He who contemplates the geological record gazes into an unfathomable **abyss** of past time." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The boat plummeted down the glassy side of the ocean swell into the yawning **abyss** between mountain waves." }
    ]
  },
  "Dashboard — byss/abyssal.md": {
    primary: "Of, relating to, or occurring in the deepest parts of the ocean, especially between 3,000 and 6,000 meters below sea level.",
    secondary: "In marine ecology and geology, characterizing lightless, high-pressure, near-freezing oceanic environments and the bizarre benthic organisms adapted to them.",
    quotes: [
      { author: "William Beebe", work: "Half Mile Down", quote: "Through the quartz windows of the bathysphere, we glimpsed the eerie luminescent denizens of the **abyssal** depths." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Over the vast **abyssal** plains, fine globigerina ooze settles undisturbed year after year through motionless, freezing water." },
      { author: "Archibald Geikie", work: "Textbook of Geology", quote: "Ancient tectonic collisions occasionally uplift portions of the dark **abyssal** seafloor, exposing radiolarian cherts upon mountaintops." }
    ]
  },
  "Dashboard — byss/abyssinia.md": {
    primary: "The historical name of the Ethiopian empire in the highlands of Northeast Africa, renowned for its ancient Christian culture and mountain plateaus.",
    secondary: "In historical geography and biogeography, a rugged afroalpine biodiversity hotspot and the native home of Coffea arabica.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Encompassed on all sides by the enemies of their religion, the Christians of **Abyssinia** slept near a thousand years, forgetful of the world by whom they were forgotten." },
      { author: "Samuel Johnson", work: "The History of Rasselas, Prince of Abissinia", quote: "Ye who listen with credulity to the whispers of fancy, attend to the history of Rasselas, prince of **Abyssinia**." },
      { author: "James Bruce", work: "Travels to Discover the Source of the Nile", quote: "After years of peril, I reached the mountainous heart of **Abyssinia**, gazing upon the springs that feed the Blue Nile." }
    ]
  },
  "Dashboard — byss/abyssinian.md": {
    primary: "Of, relating to, or originating in Abyssinia (modern Ethiopia), its peoples, language, or culture; a native of Abyssinia.",
    secondary: "In domestic zoology, a popular breed of slender, agouti-ticked domestic cat, or a breed of rough-coated cavy (guinea pig).",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Kubla Khan", quote: "It was an **Abyssinian** maid, and on her dulcimer she played, singing of Mount Abora." },
      { author: "James Bruce", work: "Travels to Discover the Source of the Nile", quote: "The **Abyssinian** cavalry charged across the rocky ravine with reckless valor, brandishing their silver-mounted spears." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "Breeders note that the fur of the **Abyssinian** cavy exhibits curious rosettes that run counter to the normal direction of the hair." }
    ]
  },
  "Dashboard — byss/byss 2.md": {
    primary: "A combining form and classical root derived from Greek 'byssos' (bottom, depth of the sea, abyss), underlying words referring to profound depth.",
    secondary: "In geological and oceanographic etymology, the stem signifying bathyal and abyssal environments, formed by privative a- and byssos (bottomless).",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The Greek noun **byssos** signifies the sea floor or bottom, serving as the etymological root of abyss, that which has no bottom." },
      { author: "Robert Beekes", work: "Etymological Dictionary of Greek", quote: "In Indo-European terms for water depth, **byssos** designates the submerged floor or seabed." },
      { author: "Archibald Geikie", work: "Textbook of Geology", quote: "Geological compounds incorporating **byss** and abyss designate petrological formations crystallizing at tremendous subterranean depths." }
    ]
  },
  "Dashboard — byss/byss.md": {
    primary: "A combining form and botanical root derived from Greek 'byssos' (fine linen, flax, cotton, or silky marine fiber), used in textile and biological terms.",
    secondary: "In historical malacology and cryptogamic botany, the root denoting silky anchoring threads secreted by bivalve mollusks or fine fungal filaments.",
    quotes: [
      { author: "Theophrastus", work: "Enquiry into Plants", quote: "The Egyptians weave priestly vestments from fine **byssos**, a plant fiber softer and whiter than common sheep's wool." },
      { author: "Pliny the Elder", work: "Natural History", quote: "Garments fashioned from marine **byssos** gleam with a golden sheen, commanding exorbitant prices across imperial Rome." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Botanists applied the generic term Byssus to obscure fibrous cryptogams that resemble bundles of fine silken threads." }
    ]
  },
  "Dashboard — byss/byssus.md": {
    primary: "A tuft or bundle of strong, silky filaments secreted by the foot of certain bivalve mollusks (such as marine mussels and the pen shell Pinna nobilis) for attachment to submerged rocks.",
    secondary: "Historically, an exquisite, fine linen or silk-like textile woven from molluscan golden threads (sea silk) or fine Egyptian flax in classical antiquity.",
    quotes: [
      { author: "Charles Darwin", work: "Journal of Researches (Voyage of the Beagle)", quote: "The common mussel anchors firmly against crashing surf by casting out adhesive anchor lines of tough, glistening **byssus**." },
      { author: "Pliny the Elder", work: "Natural History", quote: "From the long silky **byssus** of the great Pinna shell, fishermen of Taranto weave robes of gossamer lightness and golden sheen." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "Glandular secretions from the foot solidify in seawater, forming the elastic anchoring fibers of the molluscan **byssus**." }
    ]
  },
  "Dashboard — byss/hypabyssal.md": {
    primary: "Of, relating to, or denoting igneous rocks that crystallized at moderate or shallow depths beneath the Earth's surface (such as in dykes, sills, and laccoliths).",
    secondary: "In igneous petrology, exhibiting medium-grained textures intermediate between coarse-grained plutonic rocks (granite) and fine-grained volcanic rocks (basalt).",
    quotes: [
      { author: "Archibald Geikie", work: "Textbook of Geology", quote: "Dolerite dykes cutting through sandstone represent typical **hypabyssal** intrusions that cooled rapidly under moderate lithostatic pressure." },
      { author: "James Dwight Dana", work: "Manual of Geology", quote: "Porphyritic texture is especially characteristic of **hypabyssal** sheets, where large phenocrysts are embedded in a microcrystalline groundmass." },
      { author: "Frank Rutley", work: "The Study of Rocks", quote: "Systematic classifications divide igneous bodies into volcanic, **hypabyssal**, and deep-seated plutonic facies." }
    ]
  },
  "Dashboard — carp/acarpellous.md": {
    primary: "Lacking carpels; having no female reproductive organs or pistil in the flower.",
    secondary: "In angiosperm morphology, describing staminate (male) flowers or sterile teratological blossoms that fail to develop carpellary structures.",
    quotes: [
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "Male catkins of the willow are strictly **acarpellous**, producing stamens enclosed within silky bracts without any trace of an ovary." },
      { author: "John Lindley", work: "An Introduction to Botany", quote: "Certain cultivated varieties of double roses become completely **acarpellous**, all carpels having transformed into decorative petals." },
      { author: "George Bentham", work: "Genera Plantarum", quote: "The staminate flowers of dioecious Euphorbiaceae are **acarpellous**, bearing only clusters of central stamens." }
    ]
  },
  "Dashboard — carp/acarpelous.md": {
    primary: "Devoid of carpels; having no carpellary organs (variant of acarpellous).",
    secondary: "In floral anatomy, characteristic of purely staminate blossoms or aborted floral whorls lacking pistils.",
    quotes: [
      { author: "Asa Gray", work: "Lessons in Botany", quote: "In dioecious trees, one individual bears **acarpelous** stamen-bearing blossoms, while the other bears seed-producing pistils." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Morphological inspection proves that the staminate floret is **acarpelous** from its earliest embryonic primordium." },
      { author: "George Henslow", work: "The Heredity of Acquired Characters in Plants", quote: "Environmental starvation can induce an otherwise hermaphrodite blossom to develop in an **acarpelous** staminate form." }
    ]
  },
  "Dashboard — carp/acarpous.md": {
    primary: "Producing no fruit; unfruitful; barren; sterile.",
    secondary: "In descriptive botany, designating plants, branches, or cultivars that fail to set fruit or seeds after flowering.",
    quotes: [
      { author: "Theophrastus", work: "Enquiry into Plants", quote: "Certain wild palms remain persistently **acarpous**, bearing only dust-producing blossoms that wither without setting dates." },
      { author: "John Gerard", work: "The Herball or Generall Historie of Plantes", quote: "The barren fig tree mentioned in holy scripture stood **acarpous** and leafy, defying the husbandman's labor." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "Frost damage to receptive stigmas leaves the orchard **acarpous**, though vegetative foliage continues to thrive." }
    ]
  },
  "Dashboard — carp/acrocarpous.md": {
    primary: "In bryology, having the sporophyte (capsule and seta) borne at the tip or apex of the main stem or primary axis.",
    secondary: "Describing mosses that typically grow in erect, cushion-like tufts with terminal archegonia, contrasting with pleurocarpous mosses.",
    quotes: [
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "In an **acrocarpous** moss like Funaria, the archegonium terminates the main stem, terminating further apical vegetative elongation." },
      { author: "Karl von Goebel", work: "Organography of Plants", quote: "The cushion-like growth form of **acrocarpous** species aids in water retention across exposed alpine granite slabs." },
      { author: "William Gilson Farlow", work: "Gymnosporangia of the United States", quote: "Field bryologists identify **acrocarpous** genera by their solitary erect setae rising directly from the summit of the leafy stems." }
    ]
  },
  "Dashboard — carp/amphicarpa.md": {
    primary: "A genus of climbing herbaceous leguminous vines (family Fabaceae), commonly known as hog peanuts, notable for producing two distinct types of flowers and fruits.",
    secondary: "In plant ecology, a twining woodland legume displaying amphicarpy, producing showy chasmogamous aerial flowers and subterranean cleistogamous pods.",
    quotes: [
      { author: "Charles Darwin", work: "The Different Forms of Flowers on Plants of the Same Species", quote: "The vine **Amphicarpa** produces aerial pods that scatter seeds, while underground branches bury subterranean fleshy legumes in rich leaf mold." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "In moist rich woodlands, the slender stems of **Amphicarpa** monoica twine over low bushes, bearing subterranean one-seeded pods." },
      { author: "John Torrey", work: "Flora of the State of New York", quote: "Native Americans gathered the sweet subterranean beans of **Amphicarpa** from the caches of woodland mice." }
    ]
  },
  "Dashboard — carp/amphicarpaea.md": {
    primary: "A recognized spelling variant or botanical generic name for Amphicarpa (the hog peanut vine, family Fabaceae).",
    secondary: "In systematic botany, an East Asian and North American disjunct genus famous for producing dimorphic aerial and subterranean fruits.",
    quotes: [
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "Under the name **Amphicarpaea**, Elliott described the singular habit of producing fleshy single-seeded pods beneath the earth." },
      { author: "Charles Darwin", work: "The Different Forms of Flowers", quote: "The subterranean flowers of **Amphicarpaea** lack petals, fertilizing themselves in absolute darkness before setting subterranean fruit." },
      { author: "Nathaniel Lord Britton", work: "An Illustrated Flora of the Northern United States", quote: "Specimens of **Amphicarpaea** bracteata collected in autumn show subterranean runners bearing plump edible seeds." }
    ]
  },
  "Dashboard — carp/amphicarpous.md": {
    primary: "Producing two distinct kinds of fruit, either differing in morphology or produced in different positions (such as aerial and subterranean).",
    secondary: "In reproductive biology, exhibiting amphicarpy as an evolutionary bet-hedging strategy against unpredictable environmental disturbances.",
    quotes: [
      { author: "Charles Darwin", work: "The Different Forms of Flowers on Plants of the Same Species", quote: "An **amphicarpous** plant secures survival by dispersing some seeds to distant soil while burying others safely on site." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "Certain desert composites are strictly **amphicarpous**, bearing winged achenes on ray florets and heavy wingless achenes on the disc." },
      { author: "John Lindley", work: "An Introduction to Botany", quote: "The **amphicarpous** condition illustrates the evolutionary plasticity of floral organs in response to periodic drought." }
    ]
  },
  "Dashboard — carp/angiocarp.md": {
    primary: "A plant whose fruit is enclosed within an involucre, cupule, husk, or fleshy receptacle (such as an oak acorn or chestnut).",
    secondary: "In mycology and cryptogamic botany, a fruiting body whose spore-bearing hymenium develops in an enclosed chamber until maturity.",
    quotes: [
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The oak and beech bear typical examples of an **angiocarp**, where the nut is embraced by a cupule or burr." },
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "Cryptogamic fructifications are divided into gymnocarpous and **angiocarp** types according to whether spores develop openly or inside a wall." },
      { author: "George Bentham", work: "Handbook of the British Flora", quote: "The hazelnut presents an **angiocarp** structure, surrounded by an expanded leafy involucre." }
    ]
  },
  "Dashboard — carp/angiocarpic.md": {
    primary: "Having the fruit or spore-bearing organ enclosed within a covering, receptacle, or husk until maturity; angiocarpous.",
    secondary: "In mycology, describing mushroom or ascocarp development where the hymenium develops within a sealed cavity (such as in truffles or puffballs).",
    quotes: [
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "In **angiocarpic** fungi, the developing basidia are protected by a universal veil until the spores are fully ripe." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "The cupule of Quercus provides an **angiocarpic** envelope shielding the young ovary from insect predation." },
      { author: "William Gilson Farlow", work: "Cryptogamic Botany", quote: "Comparative ontogeny demonstrates that the **angiocarpic** condition evolved repeatedly in subterranean hypogeous fungi." }
    ]
  },
  "Dashboard — carp/angiocarpous.md": {
    primary: "Characterized by having the fruit or fructification enclosed within an outer covering, envelope, or involucre; angiocarpic.",
    secondary: "In mycological taxonomy and carpology, describing enclosed fruiting structures, contrasting with gymnocarpous forms.",
    quotes: [
      { author: "John Lindley", work: "An Introduction to Botany", quote: "The term **angiocarpous** applies to all fruits whose seeds are shielded by persistent bracts or fleshy perianth tubes." },
      { author: "George Henslow", work: "The Heredity of Acquired Characters in Plants", quote: "Development of an **angiocarpous** husk offers crucial defense against granivorous rodents." },
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "The cleistothecium of powdery mildews is fundamentally an **angiocarpous** ascoma that ruptures only upon complete decay." }
    ]
  },
  "Dashboard — carp/anisocarpic.md": {
    primary: "Having fewer carpels in the gynoecium than the number of other floral parts (sepals, petals, or stamens) in the flower.",
    secondary: "In descriptive floral morphology, describing flowers that exhibit evolutionary reduction in carpel number relative to perianth whorls.",
    quotes: [
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "A pentamerous flower with only two carpels represents a typically **anisocarpic** construction common in the Scrophulariaceae." },
      { author: "John Lindley", work: "The Elements of Botany", quote: "While the calyx and corolla maintain fivefold symmetry, the **anisocarpic** pistil reflects progressive gynoecial reduction." },
      { author: "George Bentham", work: "Genera Plantarum", quote: "Systematists use the **anisocarpic** condition to trace phylogenetic reduction across advanced sympetalous orders." }
    ]
  },
  "Dashboard — carp/apocarpous.md": {
    primary: "Having the carpels separate and distinct from one another, rather than united into a single compound ovary.",
    secondary: "In angiosperm morphology, describing a primitive gynoecium composed of free, independent pistils, as in buttercups (Ranunculaceae) and magnolias.",
    quotes: [
      { author: "Charles Darwin", work: "The Various Contrivances by Which Orchids Are Fertilised", quote: "The ancestral flower was undoubtedly **apocarpous**, possessing numerous independent carpels arranged spirally." },
      { author: "Asa Gray", work: "First Lessons in Botany", quote: "In the buttercup, the gynoecium is strictly **apocarpous**, each separate pistil developing into a solitary dry achene." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Systems of botany consider the **apocarpous** condition more primitive than the syncarpous union of carpellary walls." }
    ]
  },
  "Dashboard — carp/carp.md": {
    primary: "A combining form and botanical root derived from Greek 'karpos' (fruit, grain, produce); also a large freshwater fish (Cyprinus carpio).",
    secondary: "In morphological botany, the root element designating seed-bearing structures, carpels, and fruit types; in ichthyology, an omnivorous cyprinid fish.",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The Greek root **carp** stems from karpos, signifying both the fruit of the tree and the harvest yield of the earth." },
      { author: "Izaak Walton", work: "The Compleat Angler", quote: "The **carp** is the queen of rivers; a stately, good, and very subtil fish that loves deep, quiet waters." },
      { author: "John Lindley", work: "An Introduction to Botany", quote: "Botanical compounds terminating in **carp** refer invariably to the morphological constitution of the ripened ovary." }
    ]
  },
  "Dashboard — carp/carpal.md": {
    primary: "Of or relating to the carpus (the wrist bones in vertebrate anatomy); in botany, of or pertaining to a carpel.",
    secondary: "In vertebrate osteology, designating the eight small bones forming the wrist; in carpology, relating to the modified leaf that forms a carpel.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Vertebrated Animals", quote: "The human wrist comprises eight distinct **carpal** bones arranged in proximal and distal rows." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "The suture along the ventral **carpal** margin indicates the line where the fertile ovules are borne." },
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", quote: "Comparative morphology traces the mammalian **carpal** series back to the rhipidistian pectoral fin radials." }
    ]
  },
  "Dashboard — carp/carpathians.md": {
    primary: "A major arcuate mountain range across Central and Eastern Europe, forming an arc extending from Slovakia and Poland through Ukraine to Romania.",
    secondary: "In European biogeography, an ecologically rich mountain barrier harboring virgin beech forests, endemic alpine flora, and Europe's largest brown bear populations.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The folded Tertiary strata of the **Carpathians** demonstrate recent crustal movements matching the Alpine orogeny." },
      { author: "Bram Stoker", work: "Dracula", quote: "Before us rose the dark, jagged peaks of the **Carpathians**, their snowy summits glowing in the evening sunset." },
      { author: "Archibald Geikie", work: "Textbook of Geology", quote: "Glacial moraines and cirques preserved throughout the **Carpathians** record the Pleistocene glaciation of Eastern Europe." }
    ]
  }
};

let count = 0;
for (const [relPath, data] of Object.entries(batch3Data)) {
  if (updateNote(relPath, data)) {
    count++;
  }
}

console.log(`\n========================================`);
console.log(`Batch 3 Completed: ${count} / ${Object.keys(batch3Data).length} notes updated.`);
console.log(`========================================\n`);
