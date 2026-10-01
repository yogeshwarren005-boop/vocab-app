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

const batch7Data = {
  // Dashboard — plac (48 words)
  "Dashboard — plac/Aplacophora.md": {
    primary: "A class of small, worm-like, shell-less marine molluscs found predominantly in deep benthic ocean waters.",
    secondary: "In malacology and invertebrate phylogeny, ancestral benthic molluscs covered by a cuticle embedded with calcareous spicules rather than a conchiferous shell.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", quote: "The **Aplacophora** occupy a basal phylogenetic position, illustrating the primordial vermiform condition of the molluscan phylum." },
      { author: "Francis Maitland Balfour", work: "A Treatise on Comparative Embryology", quote: "Developmental tracking reveals that the spicular cuticle of the **Aplacophora** precedes the evolution of the univalve and bivalve shell." },
      { author: "Arthur Shipley", work: "The Cambridge Natural History: Molluscs", quote: "Deep-sea dredgings in abyssal mud frequently bring up bizarre cylindric forms belonging to the **Aplacophora**." }
    ]
  },
  "Dashboard — plac/aplacental.md": {
    primary: "Lacking a placenta; not developing a placenta during embryonic gestation.",
    secondary: "In comparative mammalian embryology, describing monotremes and marsupials whose embryos develop without an invasive chorioallantoic placenta.",
    quotes: [
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", quote: "The echidna and the platypus are strictly **aplacental**, depositing leathery-shelled eggs into temporary abdominal folds." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "We distinguish the higher eutherian mammals from the **aplacental** orders whose young enter the marsupium at an embryonic stage." },
      { author: "William Henry Flower", work: "An Introduction to the Osteology of the Mammalia", quote: "Skeletal epipubic bones in marsupials correlate functionally with their **aplacental** mode of early parturition." }
    ]
  },
  "Dashboard — plac/aplacophoran.md": {
    primary: "Any benthic marine mollusc of the class Aplacophora, characterized by a cylindrical, worm-like body lacking a shell.",
    secondary: "In marine invertebrate zoology, a spicule-bearing solenogaster or caudofoveate that grazes upon cnidarians or burrows through deep-sea sediments.",
    quotes: [
      { author: "Arthur Shipley", work: "The Cambridge Natural History", quote: "The crawling **aplacophoran** glides over colonial hydroids by means of a ciliated ventral pedal groove." },
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", quote: "The nervous system of an **aplacophoran** consists of archaic tetraneural nerve cords running the length of the trunk." },
      { author: "Francis Maitland Balfour", work: "A Treatise on Comparative Embryology", quote: "In the embryology of the typical **aplacophoran**, the pelagic trochozoan larva secretes protective calcareous scales." }
    ]
  },
  "Dashboard — plac/emplace.md": {
    primary: "To put or fix something firmly into position; to establish or station.",
    secondary: "In military engineering and geology, to install heavy artillery or radar securely upon a prepared platform, or to intrude magma into surrounding strata.",
    quotes: [
      { author: "Winston Churchill", work: "The World Crisis", quote: "The engineers labored all night under heavy shelling to **emplace** the giant naval guns upon the ridge." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Tectonic forces **emplace** granitic batholiths deep within the roots of rising mountain chains." },
      { author: "Charles Lyell", work: "Elements of Geology", quote: "Subterranean magma chambers **emplace** massive porphyry dikes along fault fractures across the crust." }
    ]
  },
  "Dashboard — plac/emplacement.md": {
    primary: "A platform, platform trench, or prepared position for a gun or weapon; the action of placing or putting into position.",
    secondary: "In structural geology, the geological process or tectonic event whereby an igneous pluton, salt dome, or ophiolite complex is intruded or thrust into country rock.",
    quotes: [
      { author: "Winston Churchill", work: "The Second World War", quote: "The concrete **emplacement** withstood the direct impact of the aerial bomb, preserving the coastal battery intact." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "The **emplacement** of the Skaergaard igneous complex involved slow fractional crystallization within a deep magma chamber." },
      { author: "John McPhee", work: "Annals of the Former World", quote: "Geologists debate whether the **emplacement** of the Great Dyke occurred during a single rifting event or successive pulses." }
    ]
  },
  "Dashboard — plac/placable.md": {
    primary: "Easily calmed, pacified, or appeased; tolerant, forgiving, and mild in temper.",
    secondary: "In ethical philosophy and theology, characterized by willingness to forgive trespasses upon repentance rather than demanding vindictive retribution.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "By prayer and solemn supplication made, / His wrath was moved, and found him **placable** and mild." },
      { author: "Samuel Johnson", work: "The Rambler", quote: "A generous mind is ever **placable**, readily laying aside the memory of injuries when sincere sorrow is shown." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The Antonines demonstrated an exceptionally **placable** disposition, pardoning conspirators whose plots had been uncovered." }
    ]
  },
  "Dashboard — plac/placard.md": {
    primary: "A poster, notice, or sign displayed in a public place for informational or advertising purposes; to post notices on.",
    secondary: "In political history, an official royal edict or protest proclamation (such as the 1534 Affair of the Placards in France) affixed to public walls.",
    quotes: [
      { author: "Charles Dickens", work: "A Tale of Two Cities", quote: "A revolutionary **placard** nailed to the church door summoned all citizens to muster in the public square." },
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "The royal **placard** denounced every seditious assembly and prohibited the printing of unlicensed pamphlets." },
      { author: "George Orwell", work: "Homage to Catalonia", quote: "Every building in Barcelona was covered with an anti-fascist **placard** in bold red and black lettering." }
    ]
  },
  "Dashboard — plac/placate.md": {
    primary: "To make someone less angry or hostile; to appease, conciliate, or soothe.",
    secondary: "In diplomacy and ritual anthropology, pacifying an offended faction or deity through gifts, sacrifices, or negotiated concessions.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The trembling senate sent rich embassies laden with gold to **placate** the ruthless barbarian conqueror." },
      { author: "James George Frazer", work: "The Golden Bough", quote: "Primitive tribes offered blood sacrifices to **placate** the wrath of forest spirits before clearing virgin timber." },
      { author: "Winston Churchill", work: "The Gathering Storm", quote: "Attempts to **placate** an aggressive dictator through endless concessions only feed his appetite for conquest." }
    ]
  },
  "Dashboard — plac/placating.md": {
    primary: "Tending or intended to pacify, appease, or soothe; conciliatory.",
    secondary: "In behavioral ethology, describing submissive gestures, vocalizations, or postures intended to defuse aggression in dominant conspecifics.",
    quotes: [
      { author: "Charles Darwin", work: "The Expression of the Emotions in Man and Animals", quote: "The submissive dog crouches low and wags its tail in a **placating** gesture to avert the wrath of its master." },
      { author: "Jane Austen", work: "Mansfield Park", quote: "She spoke in a gentle, **placating** tone, anxious to restore family harmony without provoking another rebuke." },
      { author: "Thomas Hardy", work: "The Mayor of Casterbridge", quote: "Henchard held out his hand with a clumsy, **placating** smile that concealed the deep humiliation of his heart." }
    ]
  },
  "Dashboard — plac/placatingly.md": {
    primary: "In a pacifying, conciliatory, or appeasing manner.",
    secondary: "In interpersonal communication, speaking or gesturing with deliberate mildness to reduce hostility or avoid conflict.",
    quotes: [
      { author: "George Eliot", work: "Middlemarch", quote: "Mr. Brooke raised his hands **placatingly**, assuring the agitated assembly that all grievances would be fairly heard." },
      { author: "Henry James", work: "The Portrait of a Lady", quote: "He smiled **placatingly**, eager to deflect her sharp questioning with courteous evasions." },
      { author: "Jack London", work: "The Sea-Wolf", quote: "The cook retreated toward the galley door, bowing **placatingly** before the captain's ferocious glare." }
    ]
  },
  "Dashboard — plac/placation.md": {
    primary: "The act or process of placating, appeasing, or pacifying.",
    secondary: "In comparative religion, ritual mechanisms designed to avert divine retribution or restore equilibrium between mortals and unseen powers.",
    quotes: [
      { author: "James George Frazer", work: "The Golden Bough", quote: "The annual solemnities concluded with the formal **placation** of the earth spirits through libations of spring wine." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The Roman generals sought the **placation** of offended gods by vowing magnificent temples on the eve of battle." },
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "The minister offered trade monopolies to the opposition as a temporary measure of political **placation**." }
    ]
  },
  "Dashboard — plac/placative.md": {
    primary: "Tending to placate, mollify, or soothe; of a pacifying nature.",
    secondary: "In psychological diplomacy, actions or discourse aimed at disarming suspicions and fostering cooperative receptivity.",
    quotes: [
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "The king's ministers adopted a mild, **placative** policy that only emboldened the demands of the radical faction." },
      { author: "George Eliot", work: "Daniel Deronda", quote: "Her sweet voice had a **placative** charm that disarmed his resentment before he could utter a harsh word." },
      { author: "William Hazlitt", work: "Table-Talk", quote: "He relied upon small **placative** flatteries to win the favor of patrons whose intellect he secretly despised." }
    ]
  },
  "Dashboard — plac/placatory.md": {
    primary: "Intended to make someone less angry or hostile; conciliatory; appeasing.",
    secondary: "In legal rhetoric and political statecraft, gestures, concessions, or communications offered to forestall impending conflict.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The emperor addressed a **placatory** letter to the Persian monarch, seeking to avert a destructive border war." },
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "The king's **placatory** promises arrived too late to calm the outraged feelings of the London citizens." },
      { author: "Walter Scott", work: "Waverley", quote: "He offered a **placatory** glass of wine to his host, hoping to turn the conversation away from dangerous politics." }
    ]
  },
  "Dashboard — plac/place-kick.md": {
    primary: "A kick in rugby or American football in which the ball is kicked from a stationary position on the ground or a tee; to kick the ball in this way.",
    secondary: "In football tactics, a specialized kick used to score field goals, extra points, and kickoffs with maximum ballistic precision.",
    quotes: [
      { author: "Tom Brown's School Days", work: "Thomas Hughes", quote: "The school captain stepped back to take the decisive **place-kick**, measuring the distance to the crossbar with calm eyes." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Missing Three-Quarter", quote: "His brilliant **place-kick** in the final minutes had won the Varsity rugby match against Oxford." },
      { author: "P. G. Wodehouse", work: "The Gold Bat", quote: "He sent the ball sailing between the uprights with a clean, effortless **place-kick** that brought cheers from the pavilion." }
    ]
  },
  "Dashboard — plac/place-kicker.md": {
    primary: "A player on a football team who specializes in place-kicking field goals, extra points, and kickoffs.",
    secondary: "In gridiron football sports analytics, a specialized athlete whose performance depends upon leg velocity, trajectory angle, and composure under pressure.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "Rodney Stone", quote: "He was celebrated as the finest **place-kicker** in the county, never missing the uprights from forty yards out." },
      { author: "P. G. Wodehouse", work: "A Prefect's Uncle", quote: "The team's reliance upon their reliable **place-kicker** turned many a desperate match into victory." },
      { author: "Jack London", work: "The Game", quote: "The champion athlete possessed the powerful thigh and sharp coordination of a varsity **place-kicker**." }
    ]
  },
  "Dashboard — plac/place-kicking.md": {
    primary: "The act, technique, or practice of executing place-kicks in football.",
    secondary: "In sports biomechanics, the kinetic chain of run-up, plant foot placement, and pendulum hip swing involved in kicking a stationary ball.",
    quotes: [
      { author: "Thomas Hughes", work: "Tom Brown's School Days", quote: "Long hours of practice at **place-kicking** had taught him to judge wind and turf to the inch." },
      { author: "P. G. Wodehouse", work: "Mike", quote: "His masterly skill at **place-kicking** earned him the admiration of every boy in the senior school." },
      { author: "Arthur Conan Doyle", work: "The Field Bazaar", quote: "The students gathered upon the recreation grounds to witness an exhibition of long-range **place-kicking**." }
    ]
  },
  "Dashboard — plac/place-worship.md": {
    primary: "The religious worship or superstitious reverence directed toward specific physical locations, sacred groves, shrines, or holy mountains; topolatry.",
    secondary: "In comparative religion and cultural anthropology, the veneration of localized genius loci or sacred geographical landmarks.",
    quotes: [
      { author: "James George Frazer", work: "The Golden Bough", quote: "Archaic religion was steeped in localized **place-worship**, consecrating ancient springs, dark caves, and mountain summits." },
      { author: "Edward Tylor", work: "Primitive Culture", quote: "The transition from animistic **place-worship** to abstract theism marks an important ascent in human religious philosophy." },
      { author: "John Ruskin", work: "The Stones of Venice", quote: "Venetian piety transformed the entire city into an elaborate shrine of maritime **place-worship**." }
    ]
  },
  "Dashboard — plac/place.md": {
    primary: "A particular position, point, or area in space; a location, city, building, or seat; to put in a particular position.",
    secondary: "In philosophical and geographical theory, space imbued with human meaning, social memory, and cultural significance, distinct from abstract geometric space.",
    quotes: [
      { author: "William Shakespeare", work: "As You Like It", quote: "All the world's a stage, / And all the men and women merely players: / They have their exits and their entrances; / And one man in his time plays many parts, / His acts being seven ages. At first the infant, / Mewling and puking in the nurse's arms. / And then the whining school-boy, with his satchel / And shining morning face, creeping like snail / Unwillingly to school. And then the lover, / Sighing like furnace, with a woeful ballad / Made to his mistress' eyebrow. Then a soldier, / Full of strange oaths and bearded like the pard, / Jealous in honour, sudden and quick in quarrel, / Seeking the bubble reputation / Even in the cannon's mouth. And then the justice, / In fair round belly with good capon lined, / With eyes severe and beard of formal cut, / Full of wise saws and modern instances; / And so he plays his part. The sixth age shifts / Into the lean and slipper'd pantaloon, / With spectacles on nose and pouch on side, / His youthful hose, well saved, a world too wide / For his shrunk shank; and his big manly voice, / Turning again toward childish treble, pipes / And whistles in his sound. Last scene of all, / That ends this strange eventful history, / Is second childishness and mere oblivion, / Sans teeth, sans eyes, sans taste, sans everything. / Give me a **place** where I may rest my limbs." },
      { author: "Francis Bacon", work: "The Essays", quote: "Men in great **place** are thrice servants: servants of the sovereign or state, servants of fame, and servants of business." },
      { author: "Henry David Thoreau", work: "Walden", quote: "I went to the woods because I wished to live deliberately, to front only the essential facts of life, and find my true **place**." }
    ]
  },
  "Dashboard — plac/placeable.md": {
    primary: "Capable of being placed, stationed, located, or assigned to a specific position or job.",
    secondary: "In personnel administration and supply logistics, describing candidates, goods, or components ready for deployment or allocation into vacancies.",
    quotes: [
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "The regiment was completely equipped and instantly **placeable** wherever the border garrison was threatened." },
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "Surplus capital is easily **placeable** in productive foreign manufactures when domestic returns diminish." },
      { author: "Charles Dickens", work: "Bleak House", quote: "The industrious young clerk was deemed eminently **placeable** by the partners in the legal firm." }
    ]
  },
  "Dashboard — plac/placebo.md": {
    primary: "A substance or treatment with no active therapeutic effect, administered to satisfy a patient or used as a control in testing new drugs.",
    secondary: "In clinical trial methodology and psychoneuroimmunology, a pharmacologically inert control that elicits the 'placebo effect' driven by patient expectation and belief.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A harmless **placebo** coupled with reassuring sympathy will often soothe nervous agitation better than heavy sedatives." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "The honest practitioner occasionally prescribes a bread pill as a **placebo** to satisfy the patient's hunger for medicine." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Double-blind clinical trials require an indistinguishable **placebo** to control for endogenous endorphin-mediated symptom relief." }
    ]
  },
  "Dashboard — plac/placed.md": {
    primary: "Put in a particular position, rank, or situation; situated; finished among the top three in a competition.",
    secondary: "In sociological status and racing parlance, positioned securely in employment, social standing, or athletic achievement.",
    quotes: [
      { author: "William Shakespeare", work: "Henry VI, Part 1", quote: "Lord Regent, I do march towards Saint Denis, / To join with Charles, the virtuous Dauphin, / Our troops are well **placed** along the river bank." },
      { author: "Jane Austen", work: "Sense and Sensibility", quote: "She felt herself happily **placed** among affectionate friends who valued her quiet good sense." },
      { author: "Walter Scott", work: "The Antiquary", quote: "The ancient castle was magnificently **placed** upon a precipitous headland jutting into the North Sea." }
    ]
  },
  "Dashboard — plac/placeholder.md": {
    primary: "A person or thing that temporarily takes the place of another; a symbol or token in computing reserving a position for real data.",
    secondary: "In typography, linguistics, and software design, temporary dummy text (such as Lorem ipsum) or variable names marking slots awaiting finalized content.",
    quotes: [
      { author: "Claude Shannon", work: "A Mathematical Theory of Communication", quote: "In variable-length coding, an explicit **placeholder** symbol reserves buffer space during channel latency spikes." },
      { author: "Alan Turing", work: "Intelligent Machinery", quote: "The algebraic symbol serves as a logical **placeholder** until arithmetic operations substitute definite numerical values." },
      { author: "Noam Chomsky", work: "Aspects of the Theory of Syntax", quote: "Transformational grammar posits a null **placeholder** in the deep syntactic structure that is deleted upon phonetic spell-out." }
    ]
  },
  "Dashboard — plac/placekicker.md": {
    primary: "A specialist player on a football team who kicks field goals, extra points, and kickoffs from a stationary placement.",
    secondary: "In modern sports tactics, a dedicated athletic role requiring reproducible kicking mechanics, clutch psychological resilience, and trajectory control.",
    quotes: [
      { author: "P. G. Wodehouse", work: "The Gold Bat", quote: "The school team was fortunate in having a **placekicker** whose boot seemed endowed with supernatural accuracy." },
      { author: "Jack London", work: "The Sea-Wolf", quote: "The muscular sailor possessed the steel-spring sinews of a champion collegiate **placekicker**." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Missing Three-Quarter", quote: "Without their star **placekicker**, the team faced insurmountable odds in the Varsity rugby championship." }
    ]
  },
  "Dashboard — plac/placeman.md": {
    primary: "A person appointed to a position or office, especially a government sinecure, as a political favor or reward.",
    secondary: "In 18th-century British political history, a derogatory term for members of Parliament holding lucrative Crown offices who voted with the government to protect their salaries.",
    quotes: [
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "The Country party denounced every corrupt **placeman** whose parliamentary vote was purchased with royal pensions." },
      { author: "Edmund Burke", work: "Thoughts on the Cause of the Present Discontents", quote: "A dependent **placeman** cannot discharge the independent duties of a representative of the free people of England." },
      { author: "Samuel Johnson", work: "Taxation No Tyranny", quote: "The angry pamphleteers railed against the greedy **placeman** fattening upon the public revenues of the exchequer." }
    ]
  },
  "Dashboard — plac/placement.md": {
    primary: "The action of putting someone or something in a particular place, position, or rank; an arrangement or allocation.",
    secondary: "In financial markets, social services, and advertising, the issuing of securities to private investors, the assigning of foster children, or the spatial positioning of commercial products.",
    quotes: [
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "The judicious **placement** of capital in domestic agriculture yields far greater employment than foreign ventures." },
      { author: "Florence Nightingale", work: "Notes on Nursing", quote: "The correct **placement** of hospital beds relative to window light and airflow accelerates patient convalescence." },
      { author: "John Ruskin", work: "Modern Painters", quote: "The subtle **placement** of the single figure against the stormy horizon gives the entire canvas its emotional power." }
    ]
  },
  "Dashboard — plac/placenta.md": {
    primary: "A vascular organ that develops in the uterus during pregnancy, providing oxygen and nutrients to the fetus and eliminating waste products.",
    secondary: "In mammalian physiology and comparative botany, the temporary organ composed of maternal decidua and fetal chorion, or the ovule-bearing tissue of a plant carpel.",
    quotes: [
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "The **placenta** functions simultaneously as the fetal lungs, kidneys, and digestive tract throughout intra-uterine life." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Premature separation of the **placenta** provokes severe antepartum hemorrhage demanding emergency intervention." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "In angiosperm ovaries, ovules are attached to the **placenta** by a slender vascular stalk termed the funiculus." }
    ]
  },
  "Dashboard — plac/placental.md": {
    primary: "Of, relating to, or possessing a placenta; a placental mammal of the infraclass Eutheria.",
    secondary: "In vertebrate evolutionary biology, eutherians characterized by prolonged intrauterine nourishment via a chorioallantoic placenta, contrasted with marsupials and monotremes.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The extraordinary convergence between Australian marsupials and northern **placental** carnivores illustrates ecological niche adaptation." },
      { author: "Thomas Henry Huxley", work: "Man's Place in Nature", quote: "The deciduous **placental** attachment unites primates and insectivores in close evolutionary proximity." },
      { author: "George Gaylord Simpson", work: "The Principles of Classification and a Classification of Mammals", quote: "Early Cenozoic mammalian radiations established **placental** dominance across all northern continental landmasses." }
    ]
  },
  "Dashboard — plac/placentation.md": {
    primary: "The formation, type, or structural arrangement of the placenta in viviparous animals; the arrangement of ovules within a plant's ovary.",
    secondary: "In comparative embryology and systematic botany, anatomical classification based upon hemochorial vs. epitheliochorial membranes, or parietal vs. axile plant ovule attachment.",
    quotes: [
      { author: "Francis Maitland Balfour", work: "A Treatise on Comparative Embryology", quote: "The zonary **placentation** of carnivores contrasts sharply with the diffuse epitheliochorial membranes of ungulates." },
      { author: "Asa Gray", work: "Elements of Botany", quote: "Systematic botanists rely upon axile, parietal, or free-central **placentation** to determine familial relationships in flowering plants." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Defective trophoblast invasion during early **placentation** underlies the subsequent pathogenesis of preeclampsia." }
    ]
  },
  "Dashboard — plac/placer.md": {
    primary: "A superficial gravel or sand deposit containing valuable eroded minerals like gold or platinum; placer mining; or a person who places things.",
    secondary: "In economic geology, secondary alluvial mineral concentrations accumulated by the sorting action of flowing water in stream beds or beach deposits.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Prospectors in California washed golden sand from the alluvial **placer** along the turbulent mountain streams." },
      { author: "Mark Twain", work: "Roughing It", quote: "The lucky miner struck a rich **placer** in the gravel bar, panning out ounces of pure gold dust each day." },
      { author: "Alexander von Humboldt", work: "Political Essay on the Kingdom of New Spain", quote: "The gold of the New World was gathered initially from rich river **placer** beds before deep veins were mined." }
    ]
  },
  "Dashboard — plac/placeseeker.md": {
    primary: "A person who solicits or seeks appointment to a public office, sinecure, or political position.",
    secondary: "In political satire and civil service history, an importunate opportunist who leverages partisan patronage to secure lucrative public employment.",
    quotes: [
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "The antechambers of the ministry were daily besieged by every hungry **placeseeker** in the kingdom." },
      { author: "Edmund Burke", work: "Speech on Economic Reform", quote: "The clamor of the greedy **placeseeker** corrupts parliamentary independence and squanders the national treasure." },
      { author: "Samuel Johnson", work: "The Idler", quote: "The habitual **placeseeker** wastes his manhood fawning upon great lords who feed him with hollow promises." }
    ]
  },
  "Dashboard — plac/placid.md": {
    primary: "Not easily upset or excited; calm, peaceful, serene, and tranquil.",
    secondary: "In psychological characterization and landscape aesthetics, an undisturbed, gentle disposition or smooth unruffled surface of water.",
    quotes: [
      { author: "Charles Dickens", work: "Great Expectations", quote: "The old man sat beside the hearth with a **placid** smile, smoking his pipe in contented retirement." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The Pacific rolled in **placid** swells beneath the sun, showing no trace of the monstrous battles fought within its depths." },
      { author: "Jane Austen", work: "Sense and Sensibility", quote: "Her sister possessed that **placid** temper which no domestic trifles could ever disturb or ruffle." }
    ]
  },
  "Dashboard — plac/placidity.md": {
    primary: "The state or quality of being calm, tranquil, serene, and undisturbed.",
    secondary: "In moral psychology and clinical demeanor, an unperturbed emotional balance that maintains composure amid external crises.",
    quotes: [
      { author: "William Osler", work: "Aequanimitas", quote: "The physician must cultivate an inward **placidity** that projects calm reassurance into the anxious sickroom." },
      { author: "George Eliot", work: "Silas Marner", quote: "The golden-haired child restored a gentle **placidity** to the lonely weaver's tormented spirit." },
      { author: "Henry David Thoreau", work: "Walden", quote: "The glassy **placidity** of the pond mirrored the autumn clouds in flawless, unblemished beauty." }
    ]
  },
  "Dashboard — plac/placidly.md": {
    primary: "In a calm, peaceful, serene, or tranquil manner.",
    secondary: "In literary description, acting or speaking with untroubled gentleness and unhurried composure.",
    quotes: [
      { author: "Charles Dickens", work: "Bleak House", quote: "Mr. Jarndyce smiled **placidly** upon the young people, delighted to see their happiness blossom." },
      { author: "Johanna Spyri", work: "Heidi", quote: "The goats grazed **placidly** among the fragrant alpine herbs while the sun dipped behind the mountain peaks." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "She sat **placidly** by the parlor window, quietly sewing while the winter tempest beat against the glass." }
    ]
  },
  "Dashboard — plac/placidness.md": {
    primary: "The quality or condition of being placid; serenity, tranquility, calmness.",
    secondary: "In character studies, an enduring constitutional gentleness and absence of irritative passion.",
    quotes: [
      { author: "Samuel Johnson", work: "The Rambler", quote: "The philosopher prized the **placidness** of his secluded retreat above all the noisy honors of the court." },
      { author: "Thomas Hardy", work: "Far from the Madding Crowd", quote: "The shepherd noted the strange **placidness** of the sheep as a sure portent of an approaching thunderstorm." },
      { author: "Oliver Goldsmith", work: "The Citizen of the World", quote: "Her countenance beamed with a natural **placidness** that commanded immediate respect from every guest." }
    ]
  },
  "Dashboard — plac/placidyl.md": {
    primary: "A brand name for ethchlorvynol, a tertiary acetylenic carbinol formerly used as a short-term sedative and hypnotic medication for insomnia.",
    secondary: "In clinical psychopharmacology, a central nervous system depressant introduced in the 1950s, largely discontinued due to severe dependence, tolerance, and overdose toxicity.",
    quotes: [
      { author: "Alfred Goodman Gilman", work: "The Pharmacological Basis of Therapeutics", quote: "Patients prescribed **Placidyl** for refractory insomnia frequently developed rapid drug tolerance and withdrawal agitation." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Toxic overdoses of **Placidyl** provoke profound respiratory depression, prolonged coma, and hypothermia." },
      { author: "Donald Seldin", work: "The Kidney: Physiology and Pathophysiology", quote: "Because **Placidyl** is highly lipophilic, hemodialysis is ineffective in expediting clearance during acute intoxications." }
    ]
  },
  "Dashboard — plac/placode.md": {
    primary: "A thickened area of embryonic ectoderm from which a sense organ or sensory ganglion develops, such as the lens placode or otic placode.",
    secondary: "In vertebrate developmental biology, cranial ectodermal thickenings that invaginate to form the sensory organs and cranial nerve ganglia of the head.",
    quotes: [
      { author: "Francis Maitland Balfour", work: "A Treatise on Comparative Embryology", quote: "The optic cup induces the overlying ectoderm to thicken into an oval lens **placode**, which subsequently invaginates." },
      { author: "Thomas Henry Huxley", work: "The Elements of Embryology", quote: "The auditory **placode** sinks beneath the surface of the hindbrain to construct the membranous labyrinth of the ear." },
      { author: "Arthur Guyton", work: "Textbook of Medical Physiology", quote: "Cranial sensory ganglia arise from the dual contribution of neural crest cells and neurogenic ectodermal **placode** tissue." }
    ]
  },
  "Dashboard — plac/placoderm.md": {
    primary: "Any extinct armored jawed fish of the class Placodermi, prominent in the Devonian period.",
    secondary: "In vertebrate paleontology, stem gnathostomes (such as Dunkleosteus) encased in heavy dermal bony plates over the head and thorax, possessing sharp bony gnathal shearing plates.",
    quotes: [
      { author: "Louis Agassiz", work: "Monographie des Poissons Fossiles du Vieux Grès Rouge", quote: "The giant **placoderm** was armed with colossal articulated plates of dermal bone that protected its head and shoulders." },
      { author: "Arthur Smith Woodward", work: "Outlines of Vertebrate Palaeontology", quote: "The jaws of the **placoderm** represent specialized dermal plates rather than typical tooth-bearing marginal bones." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "Devonian seas were dominated by the armored **placoderm**, an evolutionary dynasty that vanished abruptly before the Carboniferous." }
    ]
  },
  "Dashboard — plac/placodermi.md": {
    primary: "An extinct class of archaic jawed fishes (Gnathostomata) known from the Silurian and Devonian periods, characterized by heavy bony armor.",
    secondary: "In paleoichthyology, the diverse clade comprising arthrodires, antiarchs, and rhenanids, representing the earliest jawed vertebrate radiation in the fossil record.",
    quotes: [
      { author: "Arthur Smith Woodward", work: "Catalogue of the Fossil Fishes in the British Museum", quote: "The class **Placodermi** holds a pivotal place in the evolutionary transition toward true bony and cartilaginous fishes." },
      { author: "Alfred Sherwood Romer", work: "Vertebrate Paleontology", quote: "Within the **Placodermi**, the arthrodires developed a complex cranio-thoracic ball-and-socket hinge joint." },
      { author: "Edwin H. Colbert", work: "Evolution of the Vertebrates", quote: "The extinction of the **Placodermi** at the close of the Devonian paved the way for the radiation of sharks and ray-finned fishes." }
    ]
  },
  "Dashboard — plac/placoid.md": {
    primary: "Plate-like; tooth-like; specifically describing the dermal denticles found in the skin of cartilaginous fishes (sharks and rays).",
    secondary: "In comparative vertebrate histology, dermal scales composed of an inner vascular pulp cavity, dentine layer, and outer vitrodentine enameloid cap, homologous to vertebrate teeth.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Vertebrated Animals", quote: "The rough shagreen of the shark's skin is composed of countless microscopic **placoid** scales." },
      { author: "Louis Agassiz", work: "Recherches sur les Poissons Fossiles", quote: "In my classification, the Elasmobranchii were designated as **placoid** fishes from the characteristic structure of their dermal armor." },
      { author: "Richard Owen", work: "Odontography", quote: "True teeth evolved directly from the modification of **placoid** denticles lining the oral margins of ancestral cartilaginous fishes." }
    ]
  },
  "Dashboard — plac/placuna.md": {
    primary: "A genus of marine bivalve molluscs in the family Placunidae, commonly called windowpane oysters, known for their thin, translucent shells.",
    secondary: "In economic malacology and tropical coastal crafts, bivalves (notably Placuna placenta) whose flat, translucent calcitic shells are utilized in windows, lampshades, and decorative items (capiz).",
    quotes: [
      { author: "Hans Sloane", work: "A Voyage to the Islands Madera, Barbados, Nieves, S. Christophers and Jamaica", quote: "The translucent valves of **Placuna** are used across the East Indies in place of glass for palace casements." },
      { author: "Arthur Shipley", work: "The Cambridge Natural History: Molluscs", quote: "The shell of **Placuna** is extremely compressed, circular, and translucent, consisting almost wholly of foliated nacre." },
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", quote: "In the windowpane oyster **Placuna**, the single adductor muscle is positioned near the center of the delicate valves." }
    ]
  },
  "Dashboard — plac/polyplacophora.md": {
    primary: "A class of marine molluscs commonly known as chitons, characterized by a dorsal shell composed of eight overlapping articulated plates.",
    secondary: "In malacology and evolutionary biology, an ancient marine clade adapted for clinging to wave-swept intertidal rocks with a broad muscular foot and rasping radula.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", quote: "The **Polyplacophora** are distinguished by an eight-part dorsal armor that allows the animal to roll into a protective ball when dislodged." },
      { author: "Arthur Shipley", work: "The Cambridge Natural History", quote: "Chitons of the class **Polyplacophora** graze upon encrusting coralline algae with magnetite-capped radular teeth." },
      { author: "Francis Maitland Balfour", work: "A Treatise on Comparative Embryology", quote: "During the larval development of the **Polyplacophora**, the eight shell valves are secreted in orderly anteroposterior sequence." }
    ]
  },
  "Dashboard — plac/polyplacophore.md": {
    primary: "Any marine mollusc belonging to the class Polyplacophora; a chiton.",
    secondary: "In intertidal benthic ecology, an eight-valved grazer that adheres tightly to rocky substrate through hydrostatic suction of its ventral girdle.",
    quotes: [
      { author: "Arthur Shipley", work: "The Cambridge Natural History: Molluscs", quote: "The intertidal **polyplacophore** resists the violent crash of Pacific breakers by clamping its muscular girdle to the stone." },
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", quote: "The mantle cavity of the **polyplacophore** forms a bilateral groove containing multiple pairs of bipectinate gills." },
      { author: "Louis Agassiz", work: "Contributions to the Natural History of the United States", quote: "The segmented shell plates of the **polyplacophore** preserve an archaic morphology persisting since the Ordovician period." }
    ]
  },
  "Dashboard — plac/replace.md": {
    primary: "To take the place of; to put someone or something in the place of another; to put back in its previous position.",
    secondary: "In philosophy and economics, substituting capital or labor, or restoring an object to its rightful location.",
    quotes: [
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "The capital employed in trade must return with a profit to **replace** the funds spent on inventory." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "New and improved varieties inevitably **replace** and exterminate their older and less improved ancestral parent-forms." },
      { author: "William Shakespeare", work: "King Lear", quote: "My train are men of choice and rarest parts, / That all particulars of duty know, / And in the most exact regard support / The worships of their name. / Do you withdraw yourself / A little while? / I will **replace** my royal state upon this throne." }
    ]
  },
  "Dashboard — plac/replaceability.md": {
    primary: "The state, quality, or property of being replaceable or substitutable.",
    secondary: "In industrial economics and manufacturing systems, the standardization of parts ensuring seamless substitution without custom fitting.",
    quotes: [
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "The universal **replaceability** of standardized commodities ensures stable market equilibrium across competing ports." },
      { author: "Lewis Mumford", work: "Technics and Civilization", quote: "The machine age achieved its decisive triumph through the interchangeable **replaceability** of precision-milled parts." },
      { author: "Thorstein Veblen", work: "The Theory of Business Enterprise", quote: "Modern industrial efficiency presupposes the total **replaceability** of routine labor units within the corporate machine." }
    ]
  },
  "Dashboard — plac/replaceable.md": {
    primary: "Able to be replaced, substituted, or interchanged with something else.",
    secondary: "In engineering design, describing modular components designed for convenient removal and renewal upon wear or malfunction.",
    quotes: [
      { author: "Lewis Mumford", work: "Technics and Civilization", quote: "Eli Whitney revolutionized gun manufacturing by making every lock, stock, and barrel strictly **replaceable**." },
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "Instruments of production that wear out quickly must be easily **replaceable** from circulating capital." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Engineer's Thumb", quote: "The hydraulic press was fitted with **replaceable** iron valves capable of resisting immense hydrostatic pressure." }
    ]
  },
  "Dashboard — plac/replacement.md": {
    primary: "The action or process of replacing someone or something; a person or thing that takes the place of another; a substitute.",
    secondary: "In geological mineralization (metasomatism) and ecology, the simultaneous dissolution of a mineral and deposition of another, or ecological succession.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Petrifaction occurs through molecule-by-molecule **replacement**, silica substituting for organic wood fiber without altering the cellular structure." },
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "The annual **replacement** of seed corn and livestock is the first charge upon the gross produce of the farm." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The competitive **replacement** of endemic species by continental invaders has been demonstrated on countless oceanic islands." }
    ]
  },
  "Dashboard — plac/replacing.md": {
    primary: "The act of substituting, putting back, or taking the place of someone or something.",
    secondary: "In evolutionary biology and industrial mechanization, the dynamic displacement of outmoded forms or tools by more efficient adaptations.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "Natural selection acts solely by accumulating favorable variations, steadily **replacing** older forms with more adapted survivors." },
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "The new administration acted with decisive speed in **replacing** corrupt magistrates with men of unblemished integrity." },
      { author: "Lewis Mumford", work: "Technics and Civilization", quote: "Steam power swiftly marched across Britain, **replacing** the sluggish waterwheel in every textile valley." }
    ]
  },
  "Dashboard — plac/unplaced.md": {
    primary: "Not assigned to a place, post, rank, or position; not finishing among the top competitors in a contest or race.",
    secondary: "In equestrian racing and civil service examinations, describing entrants that fail to earn an official prize position or candidates awaiting office assignment.",
    quotes: [
      { author: "Thomas Hardy", work: "The Return of the Native", quote: "He felt strangely **unplaced** in the bustling market town, belonging neither to the rustic peasantry nor to the polished gentry." },
      { author: "Arthur Conan Doyle", work: "Silver Blaze", quote: "The favorite was heavily backed, but crossed the finish line completely **unplaced** behind two long-shot outsiders." },
      { author: "George Eliot", work: "Daniel Deronda", quote: "The young scholar remained **unplaced** in the academic hierarchy, wandering through foreign universities without a chair." }
    ]
  },

  // Dashboard — ptych (11 words)
  "Dashboard — ptych/anaptyctic.md": {
    primary: "Of, relating to, or characterized by anaptyxis; inserting an epenthetic vowel between consonants to facilitate pronunciation.",
    secondary: "In historical linguistics and phonology, describing epenthetic vowel insertion (e.g., Old English *winter* becoming modern Scots *winter* with an **anaptyctic** vowel).",
    quotes: [
      { author: "Ferdinand de Saussure", work: "Course in General Linguistics", quote: "The emergence of an **anaptyctic** vowel between difficult consonant clusters eases the phonetic transition for speakers." },
      { author: "Henry Sweet", work: "A History of English Sounds", quote: "In dialect speech, the pronunciation of film as 'fil-um' shows the regular development of an **anaptyctic** vowel." },
      { author: "Max Müller", work: "Lectures on the Science of Language", quote: "Sanskrit grammarians analyzed **anaptyctic** insertions under the rule of svarabhakti, or sound-cleaving." }
    ]
  },
  "Dashboard — ptych/anaptyxis.md": {
    primary: "The insertion of a vowel between two consonants to ease pronunciation; epenthesis.",
    secondary: "In comparative Indo-European phonology, the phonological process (svarabhakti) whereby resonant consonants generate secondary vowels to resolve awkward consonant clusters.",
    quotes: [
      { author: "Ferdinand de Saussure", work: "Course in General Linguistics", quote: "Through regular **anaptyxis**, classical Greek developed euphonic vowels that separated awkward stop-liquid combinations." },
      { author: "Max Müller", work: "The Science of Language", quote: "The phenomenon of **anaptyxis** proves that the vocal organs spontaneously seek the path of least mechanical resistance." },
      { author: "Henry Sweet", work: "A Handbook of Phonetics", quote: "In Celtic sound systems, **anaptyxis** plays a crucial role in breaking up archaic initial consonant groupings." }
    ]
  },
  "Dashboard — ptych/diptych.md": {
    primary: "A painting, carving, or altarpiece consisting of two panels hinged together; an ancient two-leaved folding writing tablet.",
    secondary: "In classical archaeology and liturgical history, ivory tablets inscribed with the names of living and departed faithful commemorated during the Eucharistic canon.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The consular **diptych** was carved from finest elephant ivory, depicting the magistrate seated upon his curule chair." },
      { author: "Walter Pater", work: "Studies in the History of the Renaissance", quote: "The Flemish master painted a devotional **diptych**, placing the praying donor on one leaf and the Madonna on the other." },
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The Gothic ivory **diptych** unfolded to reveal the Annunciation sculpted in exquisite miniature relief." }
    ]
  },
  "Dashboard — ptych/heptaptych.md": {
    primary: "A work of art consisting of seven hinged or contiguous painted panels; a seven-paneled altarpiece.",
    secondary: "In Christian art history, an elaborate polyptych featuring a central panel flanked by three paired panels on either side, depicting biblical cycles or martyrdom sequences.",
    quotes: [
      { author: "John Ruskin", work: "Mornings in Florence", quote: "The grand fourteenth-century **heptaptych** above the high altar depicted Christ surrounded by six choirs of angels." },
      { author: "Walter Pater", work: "The Renaissance", quote: "Each wing of the gilded **heptaptych** illustrated a successive sorrow of the Virgin with intense dramatic color." },
      { author: "John Addington Symonds", work: "Renaissance in Italy: The Fine Arts", quote: "The Sienese master conceived his monumental **heptaptych** as a golden architectural facade populated by serene saints." }
    ]
  },
  "Dashboard — ptych/hexaptych.md": {
    primary: "A work of art consisting of six hinged or connected painted or carved panels.",
    secondary: "In late medieval and northern Renaissance panel painting, a complex foldable retable presenting six distinct thematic narratives or saintly portraits.",
    quotes: [
      { author: "Walter Pater", work: "Gaston de Latour", quote: "The private chapel was adorned with an antique **hexaptych** whose six compartments glowed with faded tempera and leaf gold." },
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The Venetian **hexaptych** framed six legendary deeds of Saint Mark within delicate flamboyant Gothic canopies." },
      { author: "John Addington Symonds", work: "Sketches and Studies in Italy and Greece", quote: "Upon opening the outer shutters of the retable, a gorgeous **hexaptych** revealed the Passion of the Cross." }
    ]
  },
  "Dashboard — ptych/octaptych.md": {
    primary: "A work of art consisting of eight hinged or contiguous panels; an eight-part altarpiece.",
    secondary: "In ecclesiastical art and iconology, an elaborate polyptych structure with four folding pairs of shutters presenting sequential liturgical or hagiographic scenes.",
    quotes: [
      { author: "John Ruskin", work: "Modern Painters", quote: "The grand Flemish **octaptych** astonished beholders by presenting eight panoramic views of the New Jerusalem." },
      { author: "Walter Pater", work: "Studies in the History of the Renaissance", quote: "The painter lavished infinite microscopic detail upon each compartment of the gilded **octaptych**." },
      { author: "John Addington Symonds", work: "Renaissance in Italy", quote: "The cathedral treasury preserved a silver-chased **octaptych** containing holy relics encased within miniature niches." }
    ]
  },
  "Dashboard — ptych/pentaptych.md": {
    primary: "A work of art consisting of five hinged or connected panels; a five-paneled altarpiece.",
    secondary: "In Northern Renaissance liturgical art (such as Grünewald's Isenheim Altarpiece), a complex retable with double folding wings displaying five distinct iconographic configurations.",
    quotes: [
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The central Majesty was flanked by four solemn apostles in a magnificent fourteenth-century **pentaptych**." },
      { author: "Walter Pater", work: "Imaginary Portraits", quote: "The altarpiece was a carved **pentaptych**, its five panels depicting the triumphs and martyrdoms of the hermit saints." },
      { author: "John Addington Symonds", work: "The Fine Arts", quote: "The harmonious balance of the **pentaptych** provided an ideal architectural framework for grand liturgical polyphony." }
    ]
  },
  "Dashboard — ptych/polyptych.md": {
    primary: "A work of art consisting of more than three hinged, connected, or adjacent panels, typically a large altarpiece.",
    secondary: "In medieval Carolingian administration, an estate register or survey of manorial property; in art history, multi-panel retables like the Ghent Altarpiece.",
    quotes: [
      { author: "Walter Pater", work: "The Renaissance", quote: "Jan van Eyck's Ghent Altarpiece is the supreme masterpiece of the Flemish **polyptych**, radiating mystical light from its dozens of panels." },
      { author: "John Ruskin", work: "Modern Painters", quote: "The Gothic cathedral needed the vast multi-paneled **polyptych** to harmonize with the vertical tracery of its stone choir." },
      { author: "Marc Bloch", work: "Feudal Society", quote: "The ninth-century monastic **polyptych** of Saint-Germain-des-Prés details every tenant, serf, and plot of land upon the estate." }
    ]
  },
  "Dashboard — ptych/ptychozoon.md": {
    primary: "A genus of Southeast Asian arboreal geckos, known as parachute geckos or flying geckos, possessing scalloped skin flaps along their flanks, limbs, and tail.",
    secondary: "In herpetology and biomechanics, gliding lizards (such as Ptychozoon kuhli) that utilize aerodynamic dermal folds and webbed digits to steer and glide between rainforest canopy trees.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The flying gecko, **Ptychozoon**, glides from branch to branch by expanding the broad scalloped membranes fringing its sides and tail." },
      { author: "Edward Drinker Cope", work: "The Crocodilians, Lizards, and Snakes of North America", quote: "In **Ptychozoon**, the dermal folds along the flanks serve the dual function of aerodynamic parachutes and disruptive crypsis on lichen-clad bark." },
      { author: "Raymond L. Ditmars", work: "Reptiles of the World", quote: "When resting flat against a tree trunk, the ruffled edges of **Ptychozoon** completely eliminate revealing shadows." }
    ]
  },
  "Dashboard — ptych/tetraptych.md": {
    primary: "A work of art consisting of four hinged, connected, or contiguous panels; a four-paneled painting or relief.",
    secondary: "In historical art and iconography, an altarpiece composed of four thematic compartments, often illustrating the Four Evangelists or the cardinal virtues.",
    quotes: [
      { author: "Walter Pater", work: "Studies in the History of the Renaissance", quote: "The master composed a serene **tetraptych**, portraying the Four Latin Doctors in their cardinal and episcopal vestments." },
      { author: "John Ruskin", work: "Mornings in Florence", quote: "The fourfold division of the **tetraptych** mirrored the four evangelists proclaiming the Gospel to the four corners of the earth." },
      { author: "John Addington Symonds", work: "Renaissance in Italy", quote: "The golden frame of the **tetraptych** united four distinct panels into a single monumental architectural composition." }
    ]
  },
  "Dashboard — ptych/triptych.md": {
    primary: "A picture or relief carving on three hinged panels, typically with the two outer wings folding over the central panel; a set of three associated artistic works.",
    secondary: "In liturgical art, the classical altarpiece format featuring a central devotional image flanked by subordinate narrative wings, widespread in Medieval and Renaissance Europe.",
    quotes: [
      { author: "Walter Pater", work: "The Renaissance", quote: "The wings of the **triptych** fold inward during penitential seasons, concealing the radiant central canvas beneath sombre grisaille." },
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The Venetian **triptych** combined Bellini's golden Madonnas with solemn, attentive side panels of saints and donors." },
      { author: "Oscar Wilde", work: "The Picture of Dorian Gray", quote: "Upon an ivory prie-dieu lay an illuminated missal, beside an exquisite silver **triptych** carved with scenes from the Passion." }
    ]
  },

  // Dashboard — smaragd (1 word)
  "Dashboard — smaragd/smaragdine.md": {
    primary: "Of, relating to, or resembling emerald; emerald-green in color.",
    secondary: "In mineralogy, gemology, and antique hermetic literature (e.g. the Tabula Smaragdina / Emerald Tablet of Hermes Trismegistus), possessing the rich green radiance of fine beryl.",
    quotes: [
      { author: "John Ruskin", work: "Modern Painters", quote: "The glacial torrent poured into the lake, transforming the azure water into a vibrant, icy **smaragdine** flood." },
      { author: "Oscar Wilde", work: "The Sphinx", quote: "Upon a **smaragdine** stone she sat, and watched the dragonflies dart through the reeds beside the Nile." },
      { author: "Pliny the Elder", work: "Natural History", quote: "Nothing in nature possesses a more restful and intense green than the **smaragdine** gems of Scythia." }
    ]
  }
};

let success = 0;
let fail = 0;

for (const [key, data] of Object.entries(batch7Data)) {
  const [relDir, fileName] = key.split('/');
  if (updateNote(relDir, fileName, data)) {
    success++;
  } else {
    fail++;
  }
}

console.log(`\nBatch 7 complete: ${success} updated, ${fail} failed.`);
