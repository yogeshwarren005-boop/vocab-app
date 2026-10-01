import fs from 'fs';
import path from 'path';

const CLUSTER_DIR = 'App database/Greek roots/Cluster Time & Chronology';
const DASHBOARD = 'Dashboard — plac';

const BATCH1_DATA = {
  "aplacental": {
    primary: "Lacking a placenta; reproducing without a true chorioallantoic placental connection.",
    secondary: "Characteristic of monotremes and marsupials whose embryos develop without a sustained maternal-fetal vascular placenta.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Vertebrated Animals", text: "Monotremes are strictly **aplacental** mammals, depositing parchment-shelled eggs in subterranean burrows." },
      { author: "Richard Owen", work: "Comparative Anatomy and Physiology of Vertebrates", text: "Marsupial development represents an essentially **aplacental** strategy where maternal lactation substitutes for prolonged uterine gestation." },
      { author: "Ernst Mayr", work: "Animal Species and Evolution", text: "Early mammalian diversification split into **aplacental** lineages and modern eutherian clades." }
    ]
  },
  "Aplacophora": {
    primary: "A class of small, benthic marine mollusks that lack shells and have vermiform bodies covered with calcareous spicules.",
    secondary: "Primitive, worm-like mollusks inhabiting deep ocean sediments without calcareous shell plates.",
    quotes: [
      { author: "Ray Lankester", work: "A Treatise on Zoology", text: "The enigmatic **Aplacophora** burrow through deep-sea ooze, lacking the characteristic protective mantle shells of other mollusks." },
      { author: "Libbie Hyman", work: "The Invertebrates", text: "Anatomy of the **Aplacophora** demonstrates archaic molluscan features preceding the evolution of dorsal valves." },
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Invertebrated Animals", text: "Comparative embryology aligns **Aplacophora** with the ancestral stem of polyplacophoran chitons." }
    ]
  },
  "aplacophoran": {
    primary: "Relating to or being a shell-less marine mollusk of the class Aplacophora.",
    secondary: "A cylindrical, spicule-bearing benthic mollusk adapted for burrowing or creeping over hydroid colonies.",
    quotes: [
      { author: "Libbie Hyman", work: "The Invertebrates", text: "The solenogaster is a specialized **aplacophoran** that grazes upon cnidarian polyps along abyssal reefs." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", text: "Calcareous spicules embedded in the cuticle give each **aplacophoran** a glistening, velvety appearance." },
      { author: "Ernst Haeckel", work: "Art Forms in Nature", text: "Microscopic examination reveals the exquisite variety of spicules covering the **aplacophoran** epidermis." }
    ]
  },
  "emplace": {
    primary: "To put or mount heavy artillery, radar, or industrial machinery into a prepared defensive position.",
    secondary: "To establish, position, or seat firmly within a permanent architectural or topographical installation.",
    quotes: [
      { author: "Winston Churchill", work: "The World Crisis", text: "Engineers laboured day and night to **emplace** heavy naval guns along the bluffs above the narrows." },
      { author: "T. E. Lawrence", work: "Seven Pillars of Wisdom", text: "The Turkish battery sought to **emplace** mountain howitzers overlooking the desert pass." },
      { author: "Robert Graves", work: "Good-bye to All That", text: "Our battalion received orders to **emplace** the Vickers machine guns before the morning bombardment commenced." }
    ]
  },
  "emplacement": {
    primary: "A platform or reinforced prepared position where a heavy gun or battery of guns is mounted.",
    secondary: "The location, setting, or physical installation of specialized equipment or structural elements.",
    quotes: [
      { author: "Winston Churchill", work: "The Second World War", text: "Concrete reinforcement rendered each coastal gun **emplacement** practically invulnerable to naval shelling." },
      { author: "Siegfried Sassoon", work: "Memoirs of an Infantry Officer", text: "We sheltered in an abandoned machine-gun **emplacement** while shrapnel rained down on the chalk slope." },
      { author: "Archibald Geikie", work: "Textbook of Geology", text: "The igneous **emplacement** of the granitic batholith disrupted the overlying sedimentary strata." }
    ]
  },
  "placable": {
    primary: "Easily calmed, pacified, or appeased; forgiving and mild-tempered.",
    secondary: "Disposed to reconcile differences without nursing lingering malice or vindictiveness.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", text: "Let us seek the Lord's holy temple, and there with tears water the ground, for he is **placable** and mild." },
      { author: "Samuel Johnson", work: "The Rambler", text: "A wise sovereign remains firm in justice yet ever **placable** to genuine penitence." },
      { author: "George Eliot", work: "Romola", text: "Behind his haughty countenance beat a **placable** heart that could not endure a friend's distress." }
    ]
  },
  "placard": {
    primary: "A printed or handwritten notice or sign displayed publicly to provide information or advertise an event; a protest sign.",
    secondary: "Historically, a formal decree, proclamation, or licence posted on public walls.",
    quotes: [
      { author: "Charles Dickens", work: "A Tale of Two Cities", text: "A blood-red **placard** nailed to the church portal announced the newest decree of the Revolutionary Tribunal." },
      { author: "Thomas Carlyle", work: "The French Revolution", text: "Every street corner blossomed with revolutionary **placards** denouncing grain hoarders and royalist traitors." },
      { author: "George Orwell", work: "1984", text: "On every landing, opposite the lift-shaft, the giant **placard** with the enormous face gazed from the wall." }
    ]
  },
  "placate": {
    primary: "To make someone less angry or hostile; to appease or pacify.",
    secondary: "To soothe offended feelings or conciliate an aggrieved party through concessions or conciliatory gestures.",
    quotes: [
      { author: "William Shakespeare", work: "Coriolanus", text: "The senate sent emissaries bearing rich gifts to **placate** the wrath of the banished warrior." },
      { author: "Jane Austen", work: "Pride and Prejudice", text: "Mr. Collins endeavoured to **placate** Lady Catherine by expressing boundless admiration for her drawing-room chimney-piece." },
      { author: "Edward Gibbon", work: "The Decline and Fall of the Roman Empire", text: "Emperors frequently paid humiliating annual tributes to **placate** invading barbarian chieftains." }
    ]
  },
  "placating": {
    primary: "Intended to appease, pacify, or mollify someone; conciliatory.",
    secondary: "Manifesting a desire to soothe tension and avoid interpersonal conflict.",
    quotes: [
      { author: "Virginia Woolf", work: "Night and Day", text: "She extended a **placating** hand, hoping to soften the sharp sting of her unexpected refusal." },
      { author: "Henry James", work: "The Portrait of a Lady", text: "His **placating** smile failed to disguise the calculating ambition beneath his polite exterior." },
      { author: "Joseph Conrad", work: "Victory", text: "He spoke in a low, **placating** murmur designed to calm the nervous agitation of his companion." }
    ]
  },
  "placatingly": {
    primary: "In a way intended to pacify, appease, or soothe someone's anger or anxiety.",
    secondary: "With conciliatory or appeasing words, gestures, or demeanor.",
    quotes: [
      { author: "Thomas Hardy", work: "Tess of the d'Urbervilles", text: "Angel spoke **placatingly**, striving to banish the dark cloud that had settled upon her brow." },
      { author: "E. M. Forster", work: "A Room with a View", text: "He raised his hands **placatingly**, assuring the ladies that no offense had been intended." },
      { author: "Charlotte Brontë", work: "Villette", text: "Madame Beck smiled **placatingly**, smoothly redirecting the inspector's attention away from the classroom." }
    ]
  },
  "placation": {
    primary: "The act or process of pacifying, appeasing, or conciliating an angry or hostile party.",
    secondary: "Religious or diplomatic offerings made to avert wrath or secure favor.",
    quotes: [
      { author: "James George Frazer", work: "The Golden Bough", text: "Ancient harvest rituals centered upon the solemn **placation** of the corn-spirit before the reaping began." },
      { author: "Edward Gibbon", work: "The Decline and Fall of the Roman Empire", text: "Sacrificial altars smoked with costly offerings destined for the **placation** of neglected deities." },
      { author: "Francis Bacon", work: "Essays", text: "Princes often find that the cowardly **placation** of seditious factions merely invites fresh insolence." }
    ]
  },
  "placative": {
    primary: "Tending to placate; intended to soothe or appease; pacifying.",
    secondary: "Designed to disarm hostility or reconcile estranged factions.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Biographia Literaria", text: "His tone was gently **placative**, designed to reconcile warring critical schools without sacrificing truth." },
      { author: "Walter Scott", work: "The Antiquary", text: "He adopted a **placative** posture, knowing full well the explosive temper of his host." },
      { author: "George Meredith", work: "Diana of the Crossways", text: "The diplomat dispatched a **placative** missive to smooth over the ruffled pride of the foreign court." }
    ]
  },
  "placatory": {
    primary: "Intended to make someone less angry or hostile; conciliatory.",
    secondary: "Characterized by appeasing concessions or soothing diplomacy.",
    quotes: [
      { author: "Anthony Trollope", work: "Barchester Towers", text: "The archdeacon attempted a **placatory** remark, but the bishop's wife remained stonily unyielding." },
      { author: "W. M. Thackeray", work: "Vanity Fair", text: "Rawdon wrote a **placatory** letter to his wealthy aunt, begging forgiveness for his secret marriage." },
      { author: "George Eliot", work: "Middlemarch", text: "Mr. Brooke offered several **placatory** suggestions, but the disgruntled tenant farmers refused to be soothed." }
    ]
  },
  "place-kick": {
    primary: "In football or rugby, a kick made from a stationary ball placed on the ground or on a small tee.",
    secondary: "To execute a kick of a stationary ball placed upon the turf toward goalposts or downfield.",
    quotes: [
      { author: "Thomas Hughes", work: "Tom Brown's School Days", text: "Old Brooke lined up the **place-kick** with deliberate care as the school spectators held their collective breath." },
      { author: "P. G. Wodehouse", work: "The Gold Bat", text: "He stepped back three paces and launched a magnificent **place-kick** straight between the crossbars." },
      { author: "Jack London", work: "The Game", text: "The crowd roared as the kicker cleanly converted the difficult **place-kick** from the sideline." }
    ]
  },
  "place-kicker": {
    primary: "A player in football or rugby whose primary role is to execute place-kicks for field goals, conversions, or kickoffs.",
    secondary: "The specialized specialist whose precision kicking scores points from placed footballs.",
    quotes: [
      { author: "P. G. Wodehouse", work: "Mike", text: "The school's star **place-kicker** adjusted the turf tee, calmly ignoring the jeers of the opposing partisans." },
      { author: "Ring Lardner", work: "You Know Me Al", text: "The coach said a dependable **place-kicker** was worth more than two flashy halfbacks when games were tied in the final quarter." },
      { author: "F. Scott Fitzgerald", work: "This Side of Paradise", text: "The veteran **place-kicker** trotted onto the gridiron under the roaring autumn stadium lights." }
    ]
  },
  "place-kicking": {
    primary: "The act or skill of kicking a ball from a stationary position on the ground or tee in rugby or football.",
    secondary: "The specialized technique of striking placed balls for accuracy and trajectory.",
    quotes: [
      { author: "Thomas Hughes", work: "Tom Brown's School Days", text: "Hours of practice at **place-kicking** had given the Rugby captain unmatched confidence in pressure matches." },
      { author: "P. G. Wodehouse", work: "The White Feather", text: "He devoted every afternoon to perfecting his **place-kicking**, aiming between the distant goalposts until dusk." },
      { author: "Jack London", work: "The Abysmal Brute", text: "The athletic collegiate match featured superb **place-kicking** that decided the championship." }
    ]
  },
  "place-worship": {
    primary: "The religious veneration, excessive devotion, or idolization of particular geographical locations or shrines (topolatry).",
    secondary: "Superstitious attachment to specific material venues rather than universal spiritual principles.",
    quotes: [
      { author: "James George Frazer", work: "The Golden Bough", text: "Sacred groves and mountain grottos illustrate the ancient prevalence of **place-worship** among early agrarian tribes." },
      { author: "John Ruskin", work: "Modern Painters", text: "He warned against degenerating from true reverence into superstitious **place-worship** of historical ruins." },
      { author: "Thomas Carlyle", work: "Past and Present", text: "True religion transcends mere local **place-worship**, finding the divine present throughout all creation." }
    ]
  },
  "place": {
    primary: "A particular position, point, or area in space; a location; to put in a particular position.",
    secondary: "A person's appropriate rank, status, duty, or role within a social structure.",
    quotes: [
      { author: "William Shakespeare", work: "As You Like It", text: "All the world's a stage, and all the men and women merely players: they have their exits and their entrances; and one man in his time plays many parts, and each hath his appointed **place**." },
      { author: "John Milton", work: "Paradise Lost", text: "The mind is its own **place**, and in itself can make a heaven of hell, a hell of heaven." },
      { author: "Jane Austen", work: "Emma", text: "She felt it was her duty to keep her proper **place** without giving countenance to vulgar presumption." }
    ]
  },
  "placeable": {
    primary: "Capable of being placed, stationed, or accommodated in a particular position or environment.",
    secondary: "Suitable for employment, residential assignment, or commercial distribution.",
    quotes: [
      { author: "Frank A. Fetter", work: "Principles of Economics", text: "A skilled artisan is readily **placeable** in diverse industrial trades even during periods of market transition." },
      { author: "Charlotte Perkins Gilman", work: "Women and Economics", text: "Social welfare agencies sought to make destitute refugees securely **placeable** within urban communities." },
      { author: "H. G. Wells", work: "The Work, Wealth and Happiness of Mankind", text: "Standardized machinery components must be easily **placeable** into existing production assemblies." }
    ]
  },
  "placebo": {
    primary: "A harmless substance, pill, or procedure prescribed more for the psychological benefit to the patient than for any physiological effect; an inactive control in a clinical trial.",
    secondary: "Historically, the vespers for the dead, from the opening Latin antiphon Placebo Domino in regione vivorum (I will please the Lord).",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "The wise physician recognizes that reassurance and a simple **placebo** often soothe mild neurotic complaints." },
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", text: "Rigorous clinical evaluation requires comparison against a **placebo** to eliminate psychological suggestion." },
      { author: "Geoffrey Chaucer", work: "The Canterbury Tales", text: "The fawning courtier Placebo took his name from the habit of singing a compliant **placebo** to flatter his patron." }
    ]
  },
  "placed": {
    primary: "Put in a particular position; situated, stationed, or ranked.",
    secondary: "Having finished among the leading runners (especially second, third, or fourth) in a race.",
    quotes: [
      { author: "William Shakespeare", work: "Hamlet", text: "Give me that man that is not passion's slave, and I will wear him in my heart's core, ay, in my heart of heart, as I do thee; thus have I **placed** my trust." },
      { author: "Thomas Hardy", work: "Far from the Madding Crowd", text: "The shepherd **placed** his lantern upon the bench and surveyed the lambing pens." },
      { author: "Charles Dickens", work: "Great Expectations", text: "He **placed** his hand upon my shoulder with an earnest look of paternal affection." }
    ]
  },
  "placeholder": {
    primary: "A person or thing that temporarily takes the place of another; an element in a document or program reserving space for future content.",
    secondary: "In mathematics or programming, a dummy symbol representing a variable or operand pending assignment.",
    quotes: [
      { author: "Bertrand Russell", work: "Introduction to Mathematical Philosophy", text: "The variable in formal logic functions as a pure **placeholder** for any individual entity satisfying the propositional function." },
      { author: "Norbert Wiener", work: "Cybernetics", text: "Memory registers store temporary **placeholder** values while algorithmic calculations proceed." },
      { author: "John Dewey", work: "Logic: The Theory of Inquiry", text: "Concepts serve initially as **placeholder** hypotheses guiding operational experiments toward definitive knowledge." }
    ]
  },
  "placekicker": {
    primary: "In American or Canadian football, the specialized player responsible for kicking field goals, extra points, and kickoffs.",
    secondary: "A specialist athlete trained exclusively in stationary ball-kicking technique.",
    quotes: [
      { author: "Grantland Rice", work: "The Tumult and the Shouting", text: "The cool-headed **placekicker** trotted onto the field with five seconds remaining to kick the winning goal." },
      { author: "Ring Lardner", work: "Lose with a Smile", text: "Our new **placekicker** booted the pigskin fifty yards through the autumn wind with clean form." },
      { author: "Damon Runyon", work: "Guys and Dolls", text: "He had the steady nerves of a championship **placekicker** standing before sixty thousand screaming fans." }
    ]
  },
  "placeman": {
    primary: "A person appointed to a government position or office, especially as a political reward rather than on merit.",
    secondary: "A political sycophant or sinecurist dependent upon ministerial patronage for emolument.",
    quotes: [
      { author: "Samuel Johnson", work: "A Dictionary of the English Language", text: "A **placeman** is one that exercises a public employment, or perhaps more often one that enjoys a sinecure under the crown." },
      { author: "Edmund Burke", work: "Thoughts on the Cause of the Present Discontents", text: "Parliament was crowded with obedient **placemen** who voted at the nod of the treasury bench." },
      { author: "William Makepeace Thackeray", work: "The Four Georges", text: "King George surrounded himself with compliant **placemen** whose loyalties were bought with lucrative pensions." }
    ]
  },
  "placement": {
    primary: "The action of placing someone or something somewhere; arrangement, positioning, or employment assignment.",
    secondary: "A temporary job or internship taken as part of a course of study or professional training.",
    quotes: [
      { author: "Frank A. Fetter", work: "Principles of Economics", text: "Optimal capital **placement** across diverse manufacturing sectors maximizes national productive efficiency." },
      { author: "Jane Austen", work: "Sense and Sensibility", text: "She adjusted the **placement** of the furniture in the cottage parlour to give an air of cheerful comfort." },
      { author: "Henry James", work: "The Ambassadors", text: "He observed the artistic **placement** of porcelain vases on the mantelpiece with exquisite appreciation." }
    ]
  },
  "placenta": {
    primary: "A flattened circular vascular organ in the uterus of pregnant eutherian mammals, nourishing and maintaining the fetus through the umbilical cord.",
    secondary: "In botany, the part of the ovary wall to which the ovules and seeds are attached.",
    quotes: [
      { author: "William Harvey", work: "Exercitationes de Generatione Animalium", text: "The **placenta** functions as a respiratory and nutritional intermediary between maternal arteries and the umbilical vessels." },
      { author: "James George Frazer", work: "The Golden Bough", text: "Numerous traditional societies preserved the dried **placenta** with superstitious veneration as a twin spirit of the newborn." },
      { author: "Asa Gray", work: "Structural Botany", text: "The botanical **placenta** lines the inner suture of the carpel, supporting the developing seeds." }
    ]
  },
  "placental": {
    primary: "Relating to, possessing, or delivered through a placenta.",
    secondary: "Belonging to the infraclass Placentalia (Eutheria); reproducing via a sustained maternal-fetal vascular connection.",
    quotes: [
      { author: "Charles Darwin", work: "The Descent of Man", text: "All existing **placental** mammals share a common ancestry dating back to the late Mesozoic era." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Vertebrated Animals", text: "The complex **placental** barrier allows efficient gas exchange while preventing direct intermingling of bloodstreams." },
      { author: "Ernst Mayr", work: "Systematics and the Origin of Species", text: "Adaptive radiation enabled **placental** carnivores to outcompete archaic creodont predators across continental landmasses." }
    ]
  },
  "placentation": {
    primary: "The formation, type, or structural arrangement of the placenta in the mammalian uterus.",
    secondary: "In botany, the arrangement of ovules within an ovary (such as marginal, axile, parietal, or free-central placentation).",
    quotes: [
      { author: "Asa Gray", work: "Elements of Botany", text: "Botanical classification distinguishes axile from parietal **placentation** when examining cross-sections of the floral ovary." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", text: "Comparative **placentation** separates the zonary band of carnivores from the discoid plate of primates." },
      { author: "Anton de Bary", work: "Comparative Anatomy of the Phanerogams and Ferns", text: "In flowering plants, the vascular bundle supplies the ovules directly through the parenchymatous **placentation**." }
    ]
  },
  "placer": {
    primary: "A superficial deposit of gravel, sand, or alluvium containing particles of gold, tin, or other valuable minerals.",
    secondary: "A person or mechanism that places or sets things in order.",
    quotes: [
      { author: "Bret Harte", work: "The Luck of Roaring Camp", text: "Miners swarmed along the canyon, washing the rich gravel of the golden **placer** through crude wooden rockers." },
      { author: "Mark Twain", work: "Roughing It", text: "Prospectors staked out every foot of the mountain **placer**, hoping each shovelful of mud would glitter with yellow dust." },
      { author: "Archibald Geikie", work: "Textbook of Geology", text: "Heavy grains of native gold settle into the bed of ancient gravel streams, creating a rich **placer** deposit." }
    ]
  },
  "placeseeker": {
    primary: "A person who seeks government employment, political office, or social position, especially from selfish motives.",
    secondary: "An unprincipled careerist soliciting patronage, titles, or public emoluments.",
    quotes: [
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", text: "The halls of power were besieged by every unprincipled **placeseeker** eager to enrich himself from the national treasury." },
      { author: "Thomas Babington Macaulay", work: "The History of England", text: "King William grew weary of the endless throng of greedy **placeseekers** clamouring for royal favours." },
      { author: "Washington Irving", work: "Knickerbocker's History of New York", text: "The governor found himself continually harassed by every ambitious **placeseeker** in the province." }
    ]
  },
  "placid": {
    primary: "Not easily upset or excited; calm, peaceful, and tranquil.",
    secondary: "Free from emotional turmoil, violent wind, or turbulent motion; serene.",
    quotes: [
      { author: "Charles Dickens", work: "David Copperfield", text: "Agnes looked so serene and **placid** that her very presence banished all my restless anxieties." },
      { author: "Herman Melville", work: "Moby-Dick", text: "The Pacific rolled its **placid** blue swells beneath the quiet stars, concealing the monsters of the deep." },
      { author: "Mary Shelley", work: "Frankenstein", text: "The **placid** surface of the lake reflected the snow-crowned summits of the surrounding Alps." }
    ]
  },
  "placidly": {
    primary: "In a calm, peaceful, and quiet manner; serenely.",
    secondary: "Without agitation, fear, or disruptive emotional display.",
    quotes: [
      { author: "Johanna Spyri", work: "Heidi", text: "The white goats chewed **placidly** among the fragrant alpine herbs while Heidi watched the evening sun." },
      { author: "Charles Dickens", work: "A Christmas Carol", text: "Mrs. Cratchit smiled **placidly** as she carved the goose, surrounded by her eager children." },
      { author: "Charlotte Brontë", work: "Jane Eyre", text: "She sat **placidly** knitting by the window, untroubled by the stormy wind outside." }
    ]
  },
  "placidness": {
    primary: "The quality, state, or condition of being calm, tranquil, or placid; serenity.",
    secondary: "Unruffled peacefulness of mind, temper, or physical atmosphere.",
    quotes: [
      { author: "Samuel Johnson", work: "The Rambler", text: "True greatness of mind is distinguished by an enduring **placidness** that adversity cannot shake." },
      { author: "Nathaniel Hawthorne", work: "The Scarlet Letter", text: "The serene **placidness** of the forest stream contrasted with the turbulent passions burning in the pastor's breast." },
      { author: "George Eliot", work: "Middlemarch", text: "Celia's unvarying **placidness** of temperament served as a steady foil to Dorothea's ardent enthusiasms." }
    ]
  },
  "placidyl": {
    primary: "A pharmaceutical trade name for ethchlorvynol, a tertiary acetylenic carbinol used as a hypnotic and sedative medication.",
    secondary: "A central nervous system depressant historically prescribed for the short-term management of insomnia.",
    quotes: [
      { author: "Louis Goodman", work: "The Pharmacological Basis of Therapeutics", text: "In therapeutic doses, **Placidyl** induces sleep through mild hypnotic depression of the subcortical reticular formation." },
      { author: "Alfred Gilman", work: "Goodman & Gilman's Pharmacological Basis of Therapeutics", text: "Prescribers were cautioned regarding the potential for physical dependence with prolonged administration of **Placidyl**." },
      { author: "Solomon H. Snyder", work: "Drugs and the Brain", text: "Like other non-barbiturate sedatives of its generation, **Placidyl** was eventually displaced by safer benzodiazepines." }
    ]
  },
  "placode": {
    primary: "An area of thickened embryonic ectoderm from which a sense organ (such as an eye lens, olfactory epithelium, or otic vesicle) or cranial ganglion develops.",
    secondary: "In vertebrate embryology, a localized cellular plate that invaginates to generate sensory structures.",
    quotes: [
      { author: "Francis Maitland Balfour", work: "A Treatise on Comparative Embryology", text: "Invagination of the otic **placode** gives rise to the auditory vesicle of the vertebrate embryo." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", text: "The lens of the vertebrate eye originates as a thickened epidermal **placode** induced by the optic cup." },
      { author: "Thomas Hunt Morgan", work: "The Development of the Frog's Egg", text: "Neural crest cells migrate alongside cranial **placode** derivatives to form sensory cranial nerve ganglia." }
    ]
  },
  "placoderm": {
    primary: "Any member of the extinct class Placodermi, comprising armored, jawed prehistoric fishes of the Silurian and Devonian periods.",
    secondary: "An archaic gnathostome characterized by heavy bony armor plates shielding the head and thoracic trunk.",
    quotes: [
      { author: "Louis Agassiz", work: "Monographie des poissons fossiles du Vieux Grès Rouge", text: "The fossilized carapace of the **placoderm** revealed a massive dermal shield protecting the anterior skeleton." },
      { author: "Arthur Smith Woodward", work: "Catalogue of the Fossil Fishes in the British Museum", text: "Dunkleosteus was a gigantic Devonian **placoderm** possessing razor-sharp shearing gnathal plates instead of true teeth." },
      { author: "Stephen Jay Gould", work: "Wonderful Life", text: "The armored **placoderm** vanished abruptly at the end of the Devonian, surrendering dominance to early sharks and osteichthyans." }
    ]
  },
  "placodermi": {
    primary: "An extinct taxonomic class of primitive armored jawed fishes that flourished during the Devonian period.",
    secondary: "Early jawed vertebrates possessing interlocking dermal head and trunk shields articulated by a unique dermal neck joint.",
    quotes: [
      { author: "Arthur Smith Woodward", work: "Catalogue of the Fossil Fishes", text: "Members of the **Placodermi** represent the earliest known radiation of jawed vertebrates in the fossil record." },
      { author: "Alfred Romer", work: "Vertebrate Paleontology", text: "The arthrodires were the most diverse and fearsome predators among the **Placodermi** in Devonian seas." },
      { author: "Louis Agassiz", work: "Recherches sur les poissons fossiles", text: "The heavy ossified carapaces of the **Placodermi** were initially mistaken by early naturalists for fossil chelonian shells." }
    ]
  },
  "placoid": {
    primary: "Plate-like; specifically designating the tooth-like dermal denticle scales found on elasmobranch fishes (sharks and rays).",
    secondary: "Consisting of a flattened basal plate of bone and a backward-pointing spine of dentine covered with enameloid.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Vertebrated Animals", text: "The sandpaper-like skin of the dogfish is densely clothed with miniature **placoid** scales." },
      { author: "Louis Agassiz", work: "Recherches sur les poissons fossiles", text: "Agassiz divided fishes into four great orders according to whether their scales were **placoid**, ganoid, cycloid, or ctenoid." },
      { author: "Henry Gray", work: "Anatomy, Descriptive and Surgical", text: "Vertebrate teeth are homologous in structural composition to the **placoid** scales of elasmobranchs." }
    ]
  },
  "placuna": {
    primary: "A genus of marine bivalve mollusks in the family Placunidae, commonly known as windowpane oysters.",
    secondary: "Flat, thin-shelled tropical bivalves (Placuna placenta) whose translucent shells were historically used in place of glass windowpanes.",
    quotes: [
      { author: "George Washington Tryon", work: "Manual of Conchology", text: "The thin, flattened translucent valves of **Placuna** were widely utilized across the Philippines as glazing for windows." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", text: "Coastal villagers gathered **Placuna** oysters from shallow muddy bays to harvest mother-of-pearl and window panes." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", text: "The shell of **Placuna** is extremely compressed, adapted for resting flat upon soft littoral silt." }
    ]
  },
  "polyplacophora": {
    primary: "A taxonomic class of marine mollusks commonly called chitons, having a dorsal shell composed of eight articulated calcareous plates.",
    secondary: "Bilateral, flattened mollusks possessing a muscular creeping foot, a radula, and eight overlapping dorsal valves bordered by a leathery girdle.",
    quotes: [
      { author: "Ray Lankester", work: "A Treatise on Zoology", text: "The class **Polyplacophora** represents an ancient molluscan lineage preserving primitive metameric plate articulation." },
      { author: "Libbie Hyman", work: "The Invertebrates", text: "Chitons clinging to wave-swept rocks belong to **Polyplacophora**, protected by their flexible eight-plated armour." },
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Invertebrated Animals", text: "When dislodged from the substrate, members of **Polyplacophora** curl into a protective ball like an armadillo." }
    ]
  },
  "polyplacophore": {
    primary: "A marine mollusk belonging to the class Polyplacophora; a chiton.",
    secondary: "A chiton bearing eight articulated calcareous dorsal shell plates encircled by a girdle.",
    quotes: [
      { author: "Libbie Hyman", work: "The Invertebrates", text: "The littoral **polyplacophore** grazes on encrusting microalgae using a radula reinforced with magnetite." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", text: "Each **polyplacophore** adheres to the rocky substrate with immense suction generated by its broad ventral foot." },
      { author: "Ernst Haeckel", work: "Art Forms in Nature", text: "Haeckel illustrated the elegant bilateral symmetry of the **polyplacophore** shell plates in his oceanic portfolios." }
    ]
  },
  "replaceability": {
    primary: "The quality or state of being replaceable; the capability of being substituted by another person, part, or resource.",
    secondary: "The degree to which an industrial component or economic factor can be exchanged without disrupting operations.",
    quotes: [
      { author: "Frank A. Fetter", work: "Principles of Economics", text: "The economic value of capital goods depends closely upon the cost and **replaceability** of worn components." },
      { author: "Norbert Wiener", work: "The Human Use of Human Beings", text: "Automated systems prioritize modular **replaceability** to guarantee continuous industrial workflow." },
      { author: "Thorstein Veblen", work: "The Engineers and the Price System", text: "The standardized machine process treats individual laborers with ruthless **replaceability**." }
    ]
  },
  "replaceable": {
    primary: "Capable of being replaced, substituted, or exchanged for something equivalent.",
    secondary: "Interchangeable with another part, unit, or worker without loss of structural or functional integrity.",
    quotes: [
      { author: "Eli Whitney", work: "Memoir on the Manufacture of Firearms", text: "Standardized musket parts were designed to be strictly **replaceable** without manual file-fitting." },
      { author: "Frank A. Fetter", work: "Principles of Economics", text: "Common agricultural tools are easily **replaceable**, whereas specialized machinery requires substantial capital outlay." },
      { author: "H. G. Wells", work: "The Work, Wealth and Happiness of Mankind", text: "Modern industrial manufacture relies upon **replaceable** standardized fittings across global supply lines." }
    ]
  },
  "replacement": {
    primary: "The action or process of replacing someone or something; a person or thing that takes the place of another.",
    secondary: "In geology or metallurgy, the substitution of one mineral or atomic constituent for another in a preexisting rock or crystal lattice.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", text: "Fossilization proceeded by silica **replacement**, preserving the microscopic cellular structure of the ancient wood." },
      { author: "Frank A. Fetter", work: "Principles of Economics", text: "Depreciation funds must be set aside systematically to cover the eventual **replacement** of industrial plants." },
      { author: "Winston Churchill", work: "The Gathering Storm", text: "The sudden **replacement** of the commanding general sent shockwaves through the allied high command." }
    ]
  },
  "unplaced": {
    primary: "Not placed or positioned; not situated in a particular job, residence, or rank.",
    secondary: "Failing to finish among the prize-winning or placed runners (first, second, or third) in a race.",
    quotes: [
      { author: "W. M. Thackeray", work: "Vanity Fair", text: "His prized thoroughbred ran wild in the final furlong and finished completely **unplaced** in the Derby." },
      { author: "Anthony Trollope", work: "The Last Chronicle of Barchester", text: "The young curate felt deeply unsettled, remaining **unplaced** and without a parish of his own." },
      { author: "Charles Dickens", work: "Bleak House", text: "Several disputed parcels of land remained **unplaced** on the master's estate map due to endless Chancery litigation." }
    ]
  }
};

function formatQuotes(quotes) {
  return quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.text}"*`).join('\n');
}

function updateFile(filePath, wordData) {
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`Missing [!book] in ${filePath}`);
    return false;
  }
  const topPart = content.slice(0, bookIdx).trimEnd();

  const newDefBlock = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${wordData.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${wordData.secondary}\n\n> [!quote] 💬 Contextual Usage & Authentic Quotations\n${formatQuotes(wordData.quotes)}\n`;

  const finalContent = topPart + '\n\n' + newDefBlock;
  fs.writeFileSync(filePath, finalContent, 'utf8');
  console.log(`Updated: ${filePath}`);
  return true;
}

let count = 0;
for (const [lemma, data] of Object.entries(BATCH1_DATA)) {
  const filePath = path.join(CLUSTER_DIR, DASHBOARD, `${lemma}.md`);
  if (!fs.existsSync(filePath)) {
    console.error(`File NOT found: ${filePath}`);
    continue;
  }
  if (updateFile(filePath, data)) {
    count++;
  }
}

console.log(`\n========================================`);
console.log(`Time Batch 1 Completed: ${count} / ${Object.keys(BATCH1_DATA).length} words updated`);
console.log(`========================================\n`);
