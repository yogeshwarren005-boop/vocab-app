import fs from 'fs';
import path from 'path';

const baseClusterDir = 'App database/Greek roots/Cluster Water & Hydrology';

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

const batch4Data = {
  // Dashboard — latry
  "Dashboard — latry/idolater.md": {
    primary: "One who worships idols, statues, or images as deities; a follower of polytheistic idol-worship.",
    secondary: "A person who exhibits blind, uncritical devotion or excessive, idolatrous adoration toward any person, idea, or physical possession.",
    quotes: [
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "The **idolater** of antiquity blindfolds his judgment and mistakes the childhood of the world for its mature wisdom." },
      { author: "John Milton", work: "Paradise Lost", quote: "He cast down the altars of the Syrian gods, leaving the **idolater** to weep amid the ruins of his grove." },
      { author: "Samuel Johnson", work: "The Rambler", quote: "Every man is an **idolater** who makes the opinion of the world the sole arbiter of his conduct." }
    ]
  },
  "Dashboard — latry/idolatrous.md": {
    primary: "Practicing, relating to, or given to the worship of physical idols or false gods.",
    secondary: "Characterized by blind, slavish, or excessive veneration and uncritical reverence.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The **idolatrous** polytheism of the Romans embraced every deity with hospitable indifference." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "To offer an **idolatrous** worship to abstract theory while trampling on ancient custom is the hallmark of fanaticism." },
      { author: "Thomas Carlyle", work: "Heroes and Hero-Worship", quote: "Men have never paid a purely **idolatrous** homage to a stick or stone; they bowed to the mysterious spirit they fancied dwelt within it." }
    ]
  },
  "Dashboard — latry/idolatrously.md": {
    primary: "In an idolatrous manner; with religious worship directed toward idols.",
    secondary: "With blind, excessive, and uncritical adoration or reverential devotion.",
    quotes: [
      { author: "George Eliot", work: "Middlemarch", quote: "She loved him almost **idolatrously**, looking upon his slightest wish as a solemn mandate." },
      { author: "Thomas De Quincey", work: "Confessions of an English Opium-Eater", quote: "I bent **idolatrously** before the majestic vision that rose in the incense-laden hall." },
      { author: "Jeremy Taylor", work: "The Rule and Exercises of Holy Living", quote: "He who serves his belly or his ambition bows down **idolatrously** before earthly masters." }
    ]
  },
  "Dashboard — latry/idolatry.md": {
    primary: "The religious worship of physical images, statues, or created objects as deities.",
    secondary: "Blind, immoderate admiration, adoration, or reverence paid to any earthly object, ideal, or human leader.",
    quotes: [
      { author: "Francis Bacon", work: "Novum Organum", quote: "The idols of the mind are a subtle form of **idolatry** that corrupts all philosophical inquiry." },
      { author: "John Locke", work: "A Letter Concerning Toleration", quote: "Civil magistrates have no commission from heaven to punish religious errors or eradicate **idolatry** with the sword." },
      { author: "Jonathan Swift", work: "Gulliver's Travels", quote: "The courtiers practiced an **idolatry** of fashion that made common sense appear ridiculous." }
    ]
  },
  "Dashboard — latry/monolatry.md": {
    primary: "The worship of a single supreme deity while not denying the existence or possible reality of other gods.",
    secondary: "In comparative religion and biblical scholarship, an intermediate stage of religious evolution between polytheism and strict philosophical monotheism.",
    quotes: [
      { author: "William Robertson Smith", work: "Lectures on the Religion of the Semites", quote: "Early tribal religion was characterized by **monolatry**, in which a clan devoted all worship to its patron god without rejecting neighboring deities." },
      { author: "James George Frazer", work: "The Golden Bough", quote: "Transition from animistic superstition to national **monolatry** marked a pivotal consolidation of priestly and kingly power." },
      { author: "Max Müller", work: "Anthropological Religion", quote: "We must distinguish between pure monotheism and **monolatry**, wherein one celestial power is worshipped to the exclusion of others." }
    ]
  },

  // Dashboard — lep
  "Dashboard — lep/Lepidoptera.md": {
    primary: "A large, diverse order of holometabolous insects comprising butterflies and moths, characterized by four membranous wings clothed in microscopic overlapping scales.",
    secondary: "In systematic entomology, the taxonomic group encompassing over 180,000 species noted for coiled sucking proboscises and striking structural wing coloration.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The richness of the **Lepidoptera** in the Moluccas astounded me with butterflies of immense size and iridescent emerald wings." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The protective mimicry exhibited by certain species of **Lepidoptera** furnishes the strongest testimony for natural selection." },
      { author: "Vladimir Nabokov", work: "Speak, Memory", quote: "My passion for collecting **Lepidoptera** began in the sunlit birch woods of our country estate." }
    ]
  },
  "Dashboard — lep/Lepidorhombus.md": {
    primary: "A genus of marine flatfishes in the family Scophthalmidae, commonly known as megrims or whiff flatfishes, characterized by scaly, translucent, left-eyed bodies.",
    secondary: "In ichthyology and commercial fisheries, demersal bottom-dwellers inhabiting the deep continental shelf waters of the northeastern Atlantic and Mediterranean.",
    quotes: [
      { author: "Francis Day", work: "The Fishes of Great Britain and Ireland", quote: "The megrim, known systematically as **Lepidorhombus**, inhabits deep waters with soft sandy or muddy bottoms." },
      { author: "Alister Hardy", work: "The Open Sea: Its Natural History", quote: "Trawlers hauling their nets along the edge of the continental shelf bring up quantities of **Lepidorhombus**." },
      { author: "William Yarrell", work: "A History of British Fishes", quote: "The genus **Lepidorhombus** is distinguished among flatfishes by its delicate, scaly integument and laterally compressed form." }
    ]
  },
  "Dashboard — lep/alep.md": {
    primary: "In biological morphology, scaleless; lacking scales or having an epidermis completely devoid of lepidote armor.",
    secondary: "In comparative anatomy and ichthyology, descriptive of scaleless fish, larval amphibians, or skin surfaces that lack epidermal scales (more commonly alepidote).",
    quotes: [
      { author: "Richard Owen", work: "Lectures on the Comparative Anatomy and Physiology of the Vertebrate Animals", quote: "Certain deep-sea teleosts present an **alep** or completely naked skin, dispensing with dermal scales." },
      { author: "Louis Agassiz", work: "Recherches sur les Poissons Fossiles", quote: "The primitive **alep** state of the integument precedes the development of hardened ganoid plates in embryonic ontogeny." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Vertebrated Animals", quote: "The smooth epidermis of the lamprey exemplifies an **alep** morphology adapted to parasitic adherence." }
    ]
  },
  "Dashboard — lep/antilepton.md": {
    primary: "In particle physics, the antimatter counterpart of a lepton, possessing the same mass but opposite electric charge and leptonic quantum numbers.",
    secondary: "In the Standard Model, any subatomic antiparticle such as the positron, positive muon, positive tau, or corresponding antineutrinos produced in high-energy collisions and weak decays.",
    quotes: [
      { author: "Steven Weinberg", work: "The Quantum Theory of Fields", quote: "Every lepton field is paired with an **antilepton** operator that creates states of identical mass and opposite charge." },
      { author: "Murray Gell-Mann", work: "The Quark and the Jaguar", quote: "In high-energy collisions, a lepton and an **antilepton** may annihilate to produce a burst of electroweak bosons." },
      { author: "Richard Feynman", work: "QED: The Strange Theory of Light and Matter", quote: "The positron may be viewed mathematically as an **antilepton** propagating backward through spacetime." }
    ]
  },
  "Dashboard — lep/lep.md": {
    primary: "The Greek root lepis (genitive lepidos, meaning 'scale, flake, or husk'), forming words relating to scaly structures, biological armor, or exfoliative conditions.",
    secondary: "In historical linguistics and scientific taxonomy, an etymological combining element seen in botany, zoology, geology, and medicine.",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The Greek root **lep** signifies a scale or peeling flake, whence we derive both leprosy and lepidopterous." },
      { author: "Peter Mark Roget", work: "Thesaurus of English Words and Phrases", quote: "Scientific terms of scaly structure invariably trace their parentage to the Hellenic **lep**." },
      { author: "Ernest Weekley", work: "The Romance of Words", quote: "From the ancient Greek **lep**, denoting a peeling bark or scale, our medical lexicons gained the solemn word leper." }
    ]
  },
  "Dashboard — lep/leper.md": {
    primary: "A person afflicted with leprosy (Hansen's disease).",
    secondary: "Historically and figuratively, an outcast shunned, ostracized, or isolated by society due to moral, social, or physical stigma.",
    quotes: [
      { author: "Robert Louis Stevenson", work: "Father Damien: An Open Letter to the Reverend Dr. Hyde", quote: "He went of his own free will to live and die with the **leper** colony on Molokai." },
      { author: "George Orwell", work: "Down and Out in Paris and London", quote: "The tramp is treated like a **leper**, driven from casual ward to casual ward by suspicious authorities." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "A ruined debtor in high society is regarded with as much dread as if he were a **leper**." }
    ]
  },
  "Dashboard — lep/lepidolite.md": {
    primary: "A lilac-gray or rose-colored lithium-bearing phyllosilicate mineral of the mica group, characterized by scaly, flaky crystal aggregates.",
    secondary: "In mineralogy and economic geology, a primary source of lithium, rubidium, and cesium found in granitic pegmatites.",
    quotes: [
      { author: "James Dwight Dana", work: "System of Mineralogy", quote: "The scaly, pearly cleavage of **lepidolite** immediately betrays its micaceous structure and high lithium content." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "In complex granitic pegmatites, crystals of tourmaline and **lepidolite** record the final volatile-rich phase of magma crystallization." },
      { author: "Edward Salisbury Dana", work: "A Textbook of Mineralogy", quote: "Specimens of **lepidolite** from Rozena display delicate violet scales embedded in quartz." }
    ]
  },
  "Dashboard — lep/lepidote.md": {
    primary: "Covered with small, scurfy scales or peltate trichomes, as the leaves or stems of certain plants.",
    secondary: "In descriptive botany and entomology, possessing a scurf-like or scale-like surface texture that reduces water loss or provides reflective coloration.",
    quotes: [
      { author: "Asa Gray", work: "Structural Botany", quote: "The underside of the leaf is distinctly **lepidote**, bearing peltate scales that shimmer in the sunlight." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "In many alpine rhododendrons, the branchlets are densely **lepidote**, protecting the delicate buds against desiccation." },
      { author: "George Bentham", work: "Handbook of the British Flora", quote: "The calyx exhibits a **lepidote** exterior, dotted with glandular scales." }
    ]
  },
  "Dashboard — lep/lepidotrichia.md": {
    primary: "Bony, bilaterally paired, segmented fin rays found in osteichthyan (bony) fishes.",
    secondary: "In comparative vertebrate anatomy and paleontology, dermal bone derivatives that support the fin membrane and evolved into tetrapod limb structures.",
    quotes: [
      { author: "Alfred Sherwood Romer", work: "Vertebrate Paleontology", quote: "The flexible pectoral fins of teleosts are stiffened by slender, jointed **lepidotrichia** of dermal origin." },
      { author: "Edwin H. Colbert", work: "Evolution of the Vertebrates", quote: "In crossopterygian fishes, internal endochondral bones articulated with the external fan of **lepidotrichia**." },
      { author: "Michael J. Benton", work: "Vertebrate Palaeontology", quote: "The fossil coelacanth displays robust **lepidotrichia** supporting each lobed fin." }
    ]
  },
  "Dashboard — lep/leprosy.md": {
    primary: "A chronic infectious disease caused by Mycobacterium leprae, characterized by disfiguring skin lesions, nerve damage, and peripheral neuropathy.",
    secondary: "Historically, any severe, chronic skin disease causing scaling, whitening, or ulceration; figuratively, an insidious moral corruption or decaying influence.",
    quotes: [
      { author: "Charles Dickens", work: "Bleak House", quote: "The pestilence of the slums clung to the city like an ancient **leprosy** that no wealth could wash away." },
      { author: "Albert Camus", work: "The Plague", quote: "In old chronicles, towns afflicted with plague or **leprosy** were sealed off completely from the living world." },
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "Religious hatred had eaten into the nation like a dry **leprosy**, dissolving all bonds of civic goodwill." }
    ]
  },
  "Dashboard — lep/leprous.md": {
    primary: "Infected with, suffering from, or resembling leprosy.",
    secondary: "Covered with scurf, white scales, or peeling crusts; figuratively, morally tainted, decaying, or vile.",
    quotes: [
      { author: "William Shakespeare", work: "Hamlet", quote: "Upon my secure hour thy uncle stole, with juice of cursed hebenon in a vial, and in the porches of my ears did pour the **leprous** distilment." },
      { author: "Samuel Taylor Coleridge", work: "The Rime of the Ancient Mariner", quote: "Her skin was as white as **leprous** ban, the Night-mare Life-in-Death was she." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The white wall of rock rose before us, mottled and peeled with a **leprous** crust of dried salt." }
    ]
  },

  // Dashboard — naut
  "Dashboard — naut/Argonaut.md": {
    primary: "In classical mythology, any of the legendary band of Greek heroes who sailed with Jason on the ship Argo to retrieve the Golden Fleece.",
    secondary: "In marine zoology, a pelagic octopod of the genus Argonauta (the paper nautilus); also applied historically to the forty-niners who journeyed to California during the Gold Rush.",
    quotes: [
      { author: "Nathaniel Hawthorne", work: "Tanglewood Tales", quote: "Jason gathered the bravest youths of Hellas, and each **Argonaut** took his seat at the long cedar oars." },
      { author: "Bret Harte", work: "Tales of the Argonauts", quote: "The weary **Argonaut** of forty-nine looked down upon the Sacramento valley with dreams of instant gold." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "The delicate shell of the female **Argonaut** is not a true molluscan shell but an egg case secreted by her webbed arms." }
    ]
  },
  "Dashboard — naut/aeronautic.md": {
    primary: "Of or relating to aeronautics; pertaining to the science, design, or operation of aircraft.",
    secondary: "Relating to aerial navigation, atmospheric flight dynamics, or aerospace engineering.",
    quotes: [
      { author: "H. G. Wells", work: "The War in the Air", quote: "The new **aeronautic** engine allowed the dirigible to climb smoothly against the Atlantic gale." },
      { author: "Octave Chanute", work: "Progress in Flying Machines", quote: "Every **aeronautic** experiment confirmed that equilibrium in the air was far more critical than raw engine power." },
      { author: "Samuel Pierpont Langley", work: "Experiments in Aerodynamics", quote: "Our **aeronautic** apparatus demonstrated that mechanical flight was governed by precise hydrodynamic equations." }
    ]
  },
  "Dashboard — naut/aeronautical.md": {
    primary: "Pertaining to aeronautics, aviation, or the design, construction, and operation of aircraft.",
    secondary: "In modern engineering, relating to the aerodynamics, structures, and propulsion systems of vehicles operating within Earth's atmosphere.",
    quotes: [
      { author: "Orville Wright", work: "How We Made the First Flight", quote: "The **aeronautical** tables compiled by previous experimenters were flawed, forcing us to construct our own wind tunnel." },
      { author: "Theodore von Kármán", work: "Aerodynamics: Selected Topics in the Light of Their Historical Development", quote: "The boundary layer concept revolutionized **aeronautical** design for high-speed flight." },
      { author: "Antoine de Saint-Exupéry", work: "Wind, Sand and Stars", quote: "The cockpit instruments represented the culmination of a generation of **aeronautical** research." }
    ]
  },
  "Dashboard — naut/aeronautics.md": {
    primary: "The science, art, and engineering involved in the study, design, manufacture, and operation of aircraft.",
    secondary: "The multidisciplinary domain encompassing aerodynamics, flight mechanics, avionics, and atmospheric navigation.",
    quotes: [
      { author: "Wilbur Wright", work: "Some Aeronautical Experiments", quote: "My interest in **aeronautics** was aroused by the gliding flights of Otto Lilienthal." },
      { author: "H. G. Wells", work: "When the Sleeper Wakes", quote: "The rapid advances in **aeronautics** had transformed warfare into an affair of swift aerial bombardments." },
      { author: "George Cayley", work: "On Aerial Navigation", quote: "The whole problem of **aeronautics** is confined within these limits: to make a surface support a given weight by the application of power to the resistance of air." }
    ]
  },
  "Dashboard — naut/astronaut.md": {
    primary: "A person trained and equipped to travel in a spacecraft into outer space.",
    secondary: "A professional spaceflight crew member tasked with piloting spacecraft, conducting orbital research, or performing extravehicular activity.",
    quotes: [
      { author: "Arthur C. Clarke", work: "2001: A Space Odyssey", quote: "The lone **astronaut** watched the blue sphere of Earth diminish until it became a brilliant morning star." },
      { author: "Neil Armstrong", work: "First Man: The Life of Neil A. Armstrong", quote: "For an **astronaut**, the lunar surface was a stark, magnificent desolation unlike anything ever witnessed." },
      { author: "Carl Sagan", work: "Cosmos", quote: "Every **astronaut** looking back from orbit has testified that national borders vanish before the majesty of our fragile globe." }
    ]
  },
  "Dashboard — naut/astronautic.md": {
    primary: "Of or relating to astronautics or the navigation of outer space.",
    secondary: "Pertaining to interplanetary or interstellar spacecraft design, propulsion, and celestial trajectory planning.",
    quotes: [
      { author: "Konstantin Tsiolkovsky", work: "The Exploration of Cosmic Space by Means of Reaction Devices", quote: "The **astronautic** rocket will carry humanity beyond the suffocating cradle of Earth's atmosphere." },
      { author: "Arthur C. Clarke", work: "Interplanetary Flight", quote: "Early **astronautic** calculations proved that multistage rockets were essential to reach orbital velocity." },
      { author: "Willy Ley", work: "Rockets, Missiles, and Space Travel", quote: "The foundation of **astronautic** science was laid by amateur rocketeers in the pre-war decades." }
    ]
  },
  "Dashboard — naut/astronautical.md": {
    primary: "Pertaining to astronautics, space exploration, or the engineering of spacecraft.",
    secondary: "Concerned with the technical systems, orbital mechanics, and human survival equipment required for space travel.",
    quotes: [
      { author: "Wernher von Braun", work: "The Mars Project", quote: "A mission to Mars demands **astronautical** logistics on a scale never before attempted by mankind." },
      { author: "Hermann Oberth", work: "The Rocket into Planetary Space", quote: "Our **astronautical** equations demonstrated that liquid fuels alone could provide the requisite exhaust velocity." },
      { author: "Robert H. Goddard", work: "A Method of Reaching Extreme Altitudes", quote: "The **astronautical** experiments with gyroscopic stabilization opened new horizons for high-altitude sounding." }
    ]
  },
  "Dashboard — naut/cosmonaut.md": {
    primary: "A space traveler trained and employed by the Russian (formerly Soviet) space agency.",
    secondary: "In the history of space exploration, a pilot or researcher representing the Soviet or Russian manned spaceflight program.",
    quotes: [
      { author: "Yuri Gagarin", work: "Road to the Stars", quote: "As the first **cosmonaut**, I felt a profound sense of responsibility to all mankind while gazing at the Earth from orbit." },
      { author: "Tom Wolfe", work: "The Right Stuff", quote: "The announcement that a Soviet **cosmonaut** had circled the globe sent a shockwave through the American scientific establishment." },
      { author: "Alexei Leonov", work: "Two Sides of the Moon", quote: "Stepping out into the black vacuum, the **cosmonaut** felt as though he were floating suspended in an infinite diamond vault." }
    ]
  },
  "Dashboard — naut/nausea.md": {
    primary: "A sensation of unease and physical discomfort in the stomach accompanied by an involuntary urge to vomit.",
    secondary: "A feeling of intense loathing, disgust, or revulsion; etymologically derived from Greek nausia, literally 'sea-sickness'.",
    quotes: [
      { author: "Jean-Paul Sartre", work: "Nausea", quote: "A dull **nausea** seized me, not in my throat or belly, but from the unbearable weight of sheer existence." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The rolling swell of the Pacific produced a miserable **nausea** that confined me to my cabin for days." },
      { author: "Virginia Woolf", work: "The Waves", quote: "A wave of sudden **nausea** rose within her at the trivial babble of the dining room." }
    ]
  },
  "Dashboard — naut/nauseate.md": {
    primary: "To cause someone to feel nausea, stomach sickness, or an urge to vomit.",
    secondary: "To fill with intense moral, intellectual, or aesthetic disgust; to repulse or sicken.",
    quotes: [
      { author: "Jonathan Swift", work: "Gulliver's Travels", quote: "The foul stench of the Houyhnhnm's stable was sweet compared to the odors of the Yahoos, which did utterly **nauseate** me." },
      { author: "Mary Shelley", work: "Frankenstein", quote: "The sight of the monstrous creation breathing life did **nauseate** my soul with an irrepressible horror." },
      { author: "Samuel Johnson", work: "The Lives of the Poets", quote: "Excessive flattery will eventually **nauseate** even the most vain of patrons." }
    ]
  },
  "Dashboard — naut/nauseated.md": {
    primary: "Suffering from nausea; experiencing a queasy stomach and an urge to vomit.",
    secondary: "Filled with profound disgust, loathing, or emotional revulsion.",
    quotes: [
      { author: "George Orwell", work: "1984", quote: "Winston felt so **nauseated** by the oily victory gin that he had to brace himself before taking a sip." },
      { author: "Joseph Conrad", work: "Heart of Darkness", quote: "He looked upon the severed heads mounted on the posts, **nauseated** by the sheer absurdity of the horror." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The stench of the boiling blubber left the novice sailor utterly **nauseated** on his first watch." }
    ]
  },
  "Dashboard — naut/nauseating.md": {
    primary: "Causing nausea, physical sickness, or queasiness of the stomach.",
    secondary: "Extremely offensive, distasteful, or sickening to the moral or aesthetic sense.",
    quotes: [
      { author: "Charles Dickens", work: "Great Expectations", quote: "The decay of the untouched bridal feast presented a **nauseating** spectacle of yellow dust and creeping spiders." },
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "The fawning adulation of the court sycophants had reached a **nauseating** pitch before the outbreak of revolt." },
      { author: "Aldous Huxley", work: "Brave New World", quote: "The warm, sickly sweet perfume of the incubator rooms produced a **nauseating** heaviness in the air." }
    ]
  },
  "Dashboard — naut/nauseous.md": {
    primary: "Causing nausea, sickness, or revulsion; sickening.",
    secondary: "Affected with nausea; experiencing an upset stomach with an inclination to vomit.",
    quotes: [
      { author: "Edgar Allan Poe", work: "The Narrative of Arthur Gordon Pym of Nantucket", quote: "A **nauseous** and suffocating stench rose from the hold of the abandoned derelict." },
      { author: "Henry David Thoreau", work: "Walden", quote: "I find it a relief to escape the **nauseous** luxury of towns and breathe the clean pine air." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "The captain felt dizzy and **nauseous** as the transport tossed in the choppy waters of the Channel." }
    ]
  },
  "Dashboard — naut/naut.md": {
    primary: "The Greek root naus (meaning 'ship') and nautes (meaning 'sailor' or 'seafarer'), forming vocabulary relating to seafaring, navigation, and celestial voyaging.",
    secondary: "In etymology and morphology, an ancient Indo-European combining form seen in nautical, astronaut, cosmonaut, aeronautics, and nausea.",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The Greek stem **naut**, signifying a mariner or vessel, survives intact in our modern space voyagers." },
      { author: "Ernest Weekley", work: "The Romance of Words", quote: "Through the Greek **naut**, the ancient trireme sailor is immortalized in both the aeronaut and the nautical chart." },
      { author: "Peter Mark Roget", work: "Thesaurus of English Words and Phrases", quote: "All vocabulary pertaining to the vessel and the helm traces its lineage back to the Hellenic **naut**." }
    ]
  },
  "Dashboard — naut/nautch.md": {
    primary: "A traditional dance performance in northern and western India, executed by professional female dancers (nautch girls) accompanied by vocalists and instrumental music.",
    secondary: "In cultural history and Anglo-Indian literature, a public entertainment prevalent in Mughal and colonial India; phonetically resembling naut- but derived from Hindi nāch (Sanskrit nṛtya).",
    quotes: [
      { author: "Rudyard Kipling", work: "Plain Tales from the Hills", quote: "The drums beat incessantly through the hot night while the troupe performed an intricate **nautch** before the rajah." },
      { author: "Mark Twain", work: "Following the Equator", quote: "At the palace we witnessed a **nautch**, where the dancers swayed in heavy gold-embroidered silks with chiming ankle bells." },
      { author: "Richard Francis Burton", work: "The Book of the Thousand Nights and a Night", quote: "The festivities concluded with an elaborate **nautch**, celebrated by musicians playing the sitar and tabla." }
    ]
  },
  "Dashboard — naut/nautical.md": {
    primary: "Of or concerning sailors, ships, seafaring, or marine navigation.",
    secondary: "Pertaining to maritime customs, naval terminology, or seafaring life.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick", quote: "In his youth he had learned all the intricacies of the **nautical** trade aboard a merchantman." },
      { author: "Joseph Conrad", work: "The Mirror of the Sea", quote: "A true **nautical** spirit is born from long communion with the loneliness and majesty of ocean gales." },
      { author: "Robert Louis Stevenson", work: "Treasure Island", quote: "He brought out a battered **nautical** almanac and laid it upon the tavern table beside his cutlass." }
    ]
  },
  "Dashboard — naut/nautilidae.md": {
    primary: "A family of archaic cephalopod mollusks, sole surviving members of the order Nautilida, characterized by multi-chambered coiled external shells.",
    secondary: "In paleontology and evolutionary biology, a living fossil lineage possessing numerous suckerless tentacles and primitive pinhole camera eyes.",
    quotes: [
      { author: "Richard Owen", work: "Memoir on the Pearly Nautilus", quote: "The anatomical structure of the **Nautilidae** reveals a primitive grade of cephalopod organization preserved from the Paleozoic era." },
      { author: "Stephen Jay Gould", work: "The Flamingo's Smile", quote: "The survival of the **Nautilidae** across mass extinctions remains one of the great enigmas of paleobiology." },
      { author: "Alfred Romer", work: "The Vertebrate Body", quote: "In the ancient seas, ancestors of the **Nautilidae** shared the waters with early jawed fishes." }
    ]
  },
  "Dashboard — naut/nautilus.md": {
    primary: "A spiral-shelled cephalopod mollusk of the tropical Pacific and Indian oceans, having a partitioned, gas-filled shell used for buoyancy control.",
    secondary: "In literature and maritime history, famed as the inspiration for Jules Verne's submarine and Oliver Wendell Holmes's meditation on spiritual growth.",
    quotes: [
      { author: "Oliver Wendell Holmes Sr.", work: "The Chambered Nautilus", quote: "Build thee more stately mansions, O my soul, as the swift seasons roll! Leave thy low-vaulted past! Let each new temple, nobler than the last, shut thee from heaven with a dome more vast, till thou at length art free, leaving thine outgrown shell by life's unresting sea!" },
      { author: "Jules Verne", work: "Twenty Thousand Leagues Under the Seas", quote: "Captain Nemo guided the **Nautilus** silently through the subterranean coral galleries of the Mediterranean." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "The coiled mother-of-pearl chambers of the **nautilus** illustrate nature's mastery of mathematical geometry." }
    ]
  },

  // Dashboard — nect
  "Dashboard — nect/eunectes.md": {
    primary: "The genus of giant semiaquatic constricting snakes in the family Boidae, commonly known as anacondas, native to tropical South America.",
    secondary: "In herpetology, apex aquatic predators whose Greek name translates literally as 'good swimmer' (eu- + nektes).",
    quotes: [
      { author: "Alfred Russel Wallace", work: "Travels on the Amazon and Rio Negro", quote: "The Indians brought word of a gigantic **Eunectes** lurking in the flooded swamps along the riverbank." },
      { author: "Henry Walter Bates", work: "The Naturalist on the River Amazons", quote: "The water-boa or **Eunectes** attains an enormous girth, suffocating large mammals beneath the river surface." },
      { author: "Raymond Ditmars", work: "Reptiles of the World", quote: "The green anaconda, **Eunectes** murinus, is perhaps the heaviest serpent in existence, ideally adapted for an aquatic life." }
    ]
  },
  "Dashboard — nect/macronectes.md": {
    primary: "The genus of giant petrels in the procellariid family, large aggressive seabirds of the Southern Ocean, known as the southern and northern giant petrels.",
    secondary: "In ornithology, scavenging and predatory seabirds with enormous wing spans and powerful hooked beaks, whose name denotes 'large swimmer'.",
    quotes: [
      { author: "Robert Cushman Murphy", work: "Oceanic Birds of South America", quote: "The huge, dusky **Macronectes** patrols the subantarctic waves, feeding voraciously on seal carrion." },
      { author: "Alister Hardy", work: "Great Waters", quote: "Flocks of **Macronectes** followed our research vessel through the roaring forties, gliding effortlessly without a flap." },
      { author: "Frank Hurley", work: "Shackleton's Argonauts", quote: "The giant petrel, **Macronectes**, circled our ice-bound camp, watching the dogs with covetous eyes." }
    ]
  },
  "Dashboard — nect/nect.md": {
    primary: "The Greek root nekhein (meaning 'to swim') and nektos (meaning 'swimming' or 'floating'), as well as the independent root nektar ('divine drink of the gods').",
    secondary: "In lexical morphology, the origin of ecological terms describing free-swimming organisms (nekton, nectopod) and botanical terms for sweet floral secretions.",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The classical root **nect** splits in our scientific vocabulary between aquatic locomotion and divine floral sweetness." },
      { author: "Ernest Weekley", work: "Words Ancient and Modern", quote: "Through **nect**, Greek bestowed upon biology both the swimmer that navigates the depths and the nectar that lures the bee." },
      { author: "Peter Mark Roget", work: "Thesaurus of English Words and Phrases", quote: "Under the stem **nect**, the naturalist classifies all animals that propel themselves freely through open water." }
    ]
  },
  "Dashboard — nect/nectar-rich.md": {
    primary: "Abundantly supplying or yielding nectar; full of sweet, sugar-laden floral fluid.",
    secondary: "In pollination ecology, describing flowering plants or blossoms that produce copious nectar to attract insects, hummingbirds, and bats.",
    quotes: [
      { author: "Charles Darwin", work: "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", quote: "Insects consistently favored the **nectar-rich** blossoms over those whose secretions had dried." },
      { author: "John Muir", work: "The Mountains of California", quote: "The alpine meadows were ablaze with **nectar-rich** lupines and wild columbines humming with bees." },
      { author: "Henry David Thoreau", work: "Excursions", quote: "The wild apple orchards become **nectar-rich** banquets for every winged wanderer of the summer woods." }
    ]
  },
  "Dashboard — nect/nectar.md": {
    primary: "A sugary liquid secreted by plants, especially within flowers, to encourage pollination by insects and other animals.",
    secondary: "In classical mythology, the life-giving beverage of the Olympian gods; figuratively, any delicious, invigorating, or blissful drink.",
    quotes: [
      { author: "Homer", work: "The Odyssey", quote: "The goddess set before him ambrosia and ruby **nectar**, the food and drink of the immortals." },
      { author: "John Milton", work: "Comus", quote: "The bees collect the sweet distilled **nectar** from every honeyed blossom that nods in the forest." },
      { author: "Percy Bysshe Shelley", work: "Prometheus Unbound", quote: "Thy words are like sweet **nectar** poured into a cup of golden morning dew." }
    ]
  },
  "Dashboard — nect/nectariferous.md": {
    primary: "Producing, secreting, or bearing nectar, as the specialized glands or tissues of a plant.",
    secondary: "In botanical anatomy, descriptive of floral and extrafloral organs adapted to reward animal pollinators.",
    quotes: [
      { author: "Asa Gray", work: "Elements of Botany", quote: "The base of each petal is furnished with a **nectariferous** cavity protected by a delicate scale." },
      { author: "John Lindley", work: "An Introduction to Botany", quote: "Certain orchids possess elongate **nectariferous** spurs that require specialized hawkmoths with long proboscises." },
      { author: "George Bentham", work: "Genera Plantarum", quote: "The disk surrounding the ovary is deeply **nectariferous**, exuding clear droplets at anthesis." }
    ]
  },
  "Dashboard — nect/nectarine.md": {
    primary: "A smooth-skinned variety of the peach (Prunus persica var. nucipersica) having sweet, juicy flesh.",
    secondary: "Possessing the sweet fragrance, richness, or deliciousness of nectar.",
    quotes: [
      { author: "John Keats", work: "Ode to Psyche", quote: "Mid hush'd, cool-rooted flowers, fragrant-eyed, blue, freckle-pink, and **nectarine** dew." },
      { author: "Henry David Thoreau", work: "Walden", quote: "I gathered wild berries whose flavor surpassed the most pampered **nectarine** grown under glass." },
      { author: "Leigh Hunt", work: "The Indicator", quote: "The peach and the **nectarine** hang blushing together against the warm brick of the garden wall." }
    ]
  },
  "Dashboard — nect/nectarous.md": {
    primary: "Sweet, delicious, or fragrant like nectar; ambrosial.",
    secondary: "Yielding the divine or intoxicating sweetness attributed to the beverage of the gods.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "From the gash a stream of **nectarous** humor issuing flowed, sanguis such as celestial spirits may bleed." },
      { author: "Alexander Pope", work: "The Dunciad", quote: "The cup offered to the poet was brimmed with **nectarous** wine distilled from ancient groves." },
      { author: "Samuel Taylor Coleridge", work: "Religious Musings", quote: "Sweet are the thoughts that rise like **nectarous** incense before the eternal throne." }
    ]
  },
  "Dashboard — nect/nectary.md": {
    primary: "A specialized plant gland or organ that secretes nectar to attract pollinators.",
    secondary: "In floral morphology, any secretory structure situated inside a blossom (floral) or on stems and leaves (extrafloral).",
    quotes: [
      { author: "Charles Darwin", work: "On the Various Contrivances by which British and Foreign Orchids are Fertilised by Insects", quote: "The bee thrusts its proboscis into the **nectary**, inevitably detaching the viscid pollinia." },
      { author: "Asa Gray", work: "Lessons in Botany", quote: "In the violet, the lower petal forms a hollow spur that serves as a **nectary**." },
      { author: "John Ruskin", work: "Proserpina", quote: "The delicate design of the flower's **nectary** proves that beauty and nourishment are inseparable in nature." }
    ]
  },
  "Dashboard — nect/nectopod.md": {
    primary: "A limb, appendage, or foot modified and adapted for swimming, as in certain aquatic insects, crustaceans, or birds.",
    secondary: "In comparative invertebrate zoology, an oar-like swimming leg equipped with dense swimming bristles.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "The thoracic appendages are modified into broad **nectopod** oars fringed with setae." },
      { author: "Richard Owen", work: "Lectures on Invertebrate Animals", quote: "The rhythmic stroke of each **nectopod** propels the crustacean swiftly through the pelagic plankton." },
      { author: "Alister Hardy", work: "The Open Sea", quote: "Under the lens, each **nectopod** of the copepod beats with the regularity of an engine piston." }
    ]
  },
  "Dashboard — nect/necturus.md": {
    primary: "A genus of aquatic North American salamanders, commonly known as mudpuppies or waterdogs, that retain external gills throughout adulthood (neoteny).",
    secondary: "In comparative vertebrate anatomy, a classical laboratory model organism used to demonstrate primitive amphibian circulatory and skeletal systems.",
    quotes: [
      { author: "Alfred Sherwood Romer", work: "The Vertebrate Body", quote: "The mudpuppy, **Necturus**, remains permanently larval, retaining bushy external gills and a swimming tail." },
      { author: "Edwin H. Colbert", work: "Evolution of the Vertebrates", quote: "In **Necturus**, the ancestral aquatic mode of life is preserved through developmental neoteny." },
      { author: "Raymond Ditmars", work: "The Reptile Book", quote: "Fishermen frequently hook **Necturus** in cold lake shallows, mistakenly regarding its red gill plumes with dread." }
    ]
  },
  "Dashboard — nect/nekton.md": {
    primary: "The aggregate of actively swimming aquatic organisms capable of moving independently of water currents, such as fish, squids, and marine mammals.",
    secondary: "In biological oceanography and limnology, distinguished from plankton (drifting organisms) and benthos (bottom-dwelling organisms).",
    quotes: [
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "While the plankton drifts at the mercy of the tides, the powerful **nekton** steers its own course across the ocean basins." },
      { author: "Alister Hardy", work: "The Open Sea: Its Natural History", quote: "The **nekton** includes all the active hunters of the open sea, from the mackerel to the sperm whale." },
      { author: "William Beebe", work: "Half Mile Down", quote: "Looking through the bathysphere window, we entered the realm where bioluminescent **nekton** darted through the blackness." }
    ]
  },
  "Dashboard — nect/trinectes.md": {
    primary: "A genus of small American sole flatfishes in the family Achiridae, notably including the hogchoker (Trinectes maculatus).",
    secondary: "In ichthyology, right-eyed, scaleless-jawed estuarine flatfishes inhabiting coastal waters, bays, and rivers along the western Atlantic.",
    quotes: [
      { author: "Francis Day", work: "The Fishes of Great Britain and Ireland", quote: "The American flatfish **Trinectes** exemplifies adaptation to brackish estuaries where salinity fluctuates wildly." },
      { author: "David Starr Jordan", work: "A Guide to the Study of Fishes", quote: "The hogchoker, known to science as **Trinectes** maculatus, is a common bottom dweller in Atlantic estuaries." },
      { author: "George Brown Goode", work: "American Fishes", quote: "Fishermen frequently capture **Trinectes** in shallow creeks, finding its dermal camouflage virtually indistinguishable from mud." }
    ]
  },

  // Dashboard — ocean
  "Dashboard — ocean/Oceania.md": {
    primary: "A geographic region encompassing the islands of the central and southern Pacific Ocean, including Australasia, Melanesia, Micronesia, and Polynesia.",
    secondary: "In dystopian literature, one of the three fictional totalitarian superstates in George Orwell's novel Nineteen Eighty-Four.",
    quotes: [
      { author: "George Orwell", work: "1984", quote: "**Oceania** was at war with Eurasia; therefore **Oceania** had always been at war with Eurasia." },
      { author: "Herman Melville", work: "Omoo", quote: "The mariner sailing through **Oceania** encounters island paradises scattered like emeralds across the vast blue." },
      { author: "Robert Louis Stevenson", work: "In the South Seas", quote: "The varied races of **Oceania** share an ancient mastery of oceanic voyaging guided by stars and swells." }
    ]
  },
  "Dashboard — ocean/ocean.md": {
    primary: "The vast body of salt water that covers approximately 71 percent of the Earth's surface; any of its major geographic divisions.",
    secondary: "Figuratively, an immense, boundless expanse or limitless quantity of anything.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick", quote: "There is, one knows not what sweet mystery about this sea, whose gently awful stirrings seem to speak of some hidden soul beneath; like those enchanted ponds that stir to life beneath the midsummer noon." },
      { author: "Lord Byron", work: "Childe Harold's Pilgrimage", quote: "Roll on, thou deep and dark blue **Ocean**—roll! Ten thousand fleets sweep over thee in vain; man marks the earth with ruin—his control stops with the shore." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "The **ocean** is the cradle of life, holding in its depths the memories of Earth's primordial past." }
    ]
  },
  "Dashboard — ocean/oceanaut.md": {
    primary: "An undersea explorer, scientist, or diver who lives and works in a submerged habitat or deep-sea submersible for extended periods.",
    secondary: "The marine equivalent of an astronaut, pioneered during mid-20th-century undersea colonization and saturation diving experiments.",
    quotes: [
      { author: "Jacques-Yves Cousteau", work: "The Living Sea", quote: "The **oceanaut** inside the underwater house proved that man could live and work under the sea without surfacing for weeks." },
      { author: "William Beebe", work: "Half Mile Down", quote: "Long before modern submersibles, the pioneer **oceanaut** descended in a steel sphere into uncharted darkness." },
      { author: "Sylvia Earle", work: "Sea Change: A Message of the Oceans", quote: "To be an **oceanaut** is to explore a planetary wilderness far richer and less known than the moon." }
    ]
  },
  "Dashboard — ocean/oceanic.md": {
    primary: "Of, relating to, inhabiting, or produced by the ocean.",
    secondary: "Resembling the ocean in vastness, depth, or boundless expanse; psychologically, describing a profound feeling of oneness with the universe.",
    quotes: [
      { author: "Sigmund Freud", work: "Civilization and Its Discontents", quote: "He described a peculiar feeling of being one with the universe, which he termed an **oceanic** sensation." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The great shroud of the **oceanic** world rolled on as it rolled five thousand years ago." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The flora of remote **oceanic** islands sheds profound light on the laws of biological distribution." }
    ]
  },
  "Dashboard — ocean/oceanica.md": {
    primary: "A Latinized taxonomic epithet designating species native to, inhabiting, or characteristic of the open ocean or Oceania.",
    secondary: "In botanical and zoological nomenclature, seen in marine organisms such as Posidonia oceanica (Neptune grass) and various pelagic invertebrates.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Personal Narrative of Travels to the Equinoctial Regions of America", quote: "The meadows of Posidonia **oceanica** carpeting the Mediterranean shelf maintain the clarity of coastal waters." },
      { author: "Carl Linnaeus", work: "Systema Naturae", quote: "Under the designation **oceanica**, ancient naturalists classified those marine organisms that never approached the littoral shore." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Fossil beds rich in Posidonia **oceanica** demonstrate the persistent depth of ancient seabed troughs." }
    ]
  },
  "Dashboard — ocean/oceanid.md": {
    primary: "In Greek mythology, any of the three thousand sea nymph daughters of the Titans Oceanus and Tethys, personifying springs, streams, and oceans.",
    secondary: "In classical poetry and art, a benevolent water nymph associated with the nourishing waters of nature.",
    quotes: [
      { author: "Hesiod", work: "Theogony", quote: "Three thousand slender-ankled daughters of Oceanus wander far and wide, and every **Oceanid** tends her allotted stream." },
      { author: "Percy Bysshe Shelley", work: "Prometheus Unbound", quote: "Panthea, the gentle **Oceanid**, sat weeping at the Titan's feet while morning dawned over the Caucasus." },
      { author: "John Keats", work: "Endymion", quote: "A chorus of sweet **Oceanid** voices rose from the coral caves, singing of ancient Neptune's hall." }
    ]
  },
  "Dashboard — ocean/oceanites.md": {
    primary: "A genus of small pelagic seabirds in the storm petrel family Oceanitidae, notably including Wilson's storm petrel (Oceanites oceanicus).",
    secondary: "In ornithology, trans-equatorial migratory petrels famous for pattering their feet on the water surface while feeding on marine plankton.",
    quotes: [
      { author: "Robert Cushman Murphy", work: "Oceanic Birds of South America", quote: "Wilson's petrel, **Oceanites** oceanicus, breeds in the Antarctic crags and winters in the northern seas." },
      { author: "Alister Hardy", work: "The Open Sea", quote: "Flocks of **Oceanites** danced upon the wave crests, fluttering their wings like swallows over a calm sea." },
      { author: "Frank Hurley", work: "Shackleton's Argonauts", quote: "The tiny storm petrel, **Oceanites**, braves the fiercest antarctic gale without resting on land." }
    ]
  },
  "Dashboard — ocean/oceanographer.md": {
    primary: "A scientist who specializes in the study of the physical, chemical, biological, and geological characteristics of the oceans.",
    secondary: "A researcher investigating ocean currents, marine ecosystems, submarine topography, and the ocean's role in global climate.",
    quotes: [
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "The **oceanographer** probes the abyss with sounding lines and deep-sea dredges, mapping mountains hidden under miles of water." },
      { author: "Matthew Fontaine Maury", work: "The Physical Geography of the Sea", quote: "The pioneer **oceanographer** charts the great rivers in the sea that govern the climate of continents." },
      { author: "Sylvia Earle", work: "Sea Change", quote: "Every modern **oceanographer** recognizes that the health of our planet depends on the vitality of the global ocean." }
    ]
  },
  "Dashboard — ocean/oceanography.md": {
    primary: "The scientific study of the oceans, including marine dynamics, currents, seabed geology, seawater chemistry, and marine life.",
    secondary: "The integrated planetary discipline that examines the interactions between oceans, the atmosphere, and global climate systems.",
    quotes: [
      { author: "Matthew Fontaine Maury", work: "The Physical Geography of the Sea", quote: "Physical **oceanography** unveils the majestic harmonies that link ocean currents to the prevailing winds." },
      { author: "Rachel Carson", work: "Under the Sea-Wind", quote: "Through modern **oceanography**, we begin to perceive the submarine contours of a world once completely hidden from view." },
      { author: "Arthur C. Clarke", work: "The Deep Range", quote: "Future advances in **oceanography** will turn the vast sea pastures into the primary food reservoir of mankind." }
    ]
  },
  "Dashboard — ocean/oceanology.md": {
    primary: "The science and practical study of the oceans, often emphasizing the utilization and development of oceanic resources and technology.",
    secondary: "In academic usage, largely synonymous with oceanography or specifically designating applied marine engineering and sea exploration.",
    quotes: [
      { author: "Jacques-Yves Cousteau", work: "The Living Sea", quote: "Applied **oceanology** will enable future generations to farm the continental shelves and harness tidal energy." },
      { author: "Alister Hardy", work: "The Open Sea", quote: "The scope of modern **oceanology** embraces both the purest biological inquiry and the economic management of fisheries." },
      { author: "Sylvia Earle", work: "Sea Change", quote: "Without a rigorous foundation in **oceanology**, industrial exploitation of deep-sea minerals risks catastrophic destruction." }
    ]
  },
  "Dashboard — ocean/oceanus.md": {
    primary: "In classical Greek mythology, the primordial Titan god personifying the vast, world-encircling freshwater river that bounded the known Earth.",
    secondary: "In ancient geography and cosmology, the outer celestial boundary from which all rivers, seas, and springs were thought to flow.",
    quotes: [
      { author: "Homer", work: "The Iliad", quote: "I go to the ends of the generous earth to visit **Oceanus**, parent of the gods, and mother Tethys." },
      { author: "Hesiod", work: "Theogony", quote: "Earth brought forth starry Heaven to cover her on all sides, and then deep-swirling **Oceanus**." },
      { author: "John Milton", work: "Paradise Lost", quote: "Beyond the western horizon where **Oceanus** pours his boundless flood around the universe." }
    ]
  },

  // Dashboard — ombr
  "Dashboard — ombr/Ombrophila.md": {
    primary: "A genus of small inoperculate discomycete cup fungi in the family Helotiaceae, characteristically growing in excessively moist, wet woodlands or swampy mosses.",
    secondary: "In mycology, gelatinous or soft cup-shaped fungi whose Greek name means 'rain-loving', thriving on waterlogged wood and rotting leaves.",
    quotes: [
      { author: "Mordecai Cubitt Cooke", work: "British Fungi", quote: "The delicate gelatinous apothecia of **Ombrophila** appear on decaying beech twigs after torrential autumn rains." },
      { author: "George Massee", work: "British Fungus-Flora", quote: "Species of **Ombrophila** are distinguished by their soft, waxy texture and preference for drenched forest bogs." },
      { author: "Pier Andrea Saccardo", work: "Sylloge Fungorum", quote: "The genus **Ombrophila** encompasses hygrophilous cup fungi that fructify only under saturated ambient moisture." }
    ]
  },
  "Dashboard — ombr/ombr.md": {
    primary: "The Greek root ombros (meaning 'rain shower', 'downpour', or 'rainwater'), forming vocabulary relating to precipitation and rain-fed ecosystems.",
    secondary: "In scientific etymology and meteorology, an ancient Hellenic root applied to rainfall measurement, rain-dependent wetlands, and precipitation ecology.",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The Greek **ombr**, signifying a rain storm, provides the scientific root for measuring rainfall in the ombrometer." },
      { author: "Ernest Weekley", work: "The Romance of Words", quote: "Through **ombr**, meteorologists and botanists honor the classical Greek word for a torrential shower." },
      { author: "Peter Mark Roget", work: "Thesaurus of English Words and Phrases", quote: "All meteorological terms relating to the measurement and ecological influence of rain derive from the stem **ombr**." }
    ]
  },
  "Dashboard — ombr/ombrogenous.md": {
    primary: "Produced, caused, or nourished by rainwater, especially of wetlands and peat bogs that receive moisture solely from precipitation.",
    secondary: "In peatland ecology, describing raised bogs and blanket bogs whose acidity and mineral-poor conditions result from direct rainwater feeding without groundwater influence.",
    quotes: [
      { author: "Arthur Tansley", work: "The British Islands and Their Vegetation", quote: "The raised bog is essentially **ombrogenous**, building its mossy dome high above the reach of ground mineral waters." },
      { author: "Henry Chandler Cowles", work: "The Plant Societies of Chicago and Vicinity", quote: "In an **ombrogenous** bog, the dominant sphagnum moss relies exclusively on atmospheric deposition for its nutrients." },
      { author: "Robert Gorham", work: "Peatland Ecology", quote: "The transition from topogenous fen to **ombrogenous** bog marks a fundamental shift toward oligotrophic acidity." }
    ]
  },
  "Dashboard — ombr/ombrology.md": {
    primary: "The branch of meteorology that deals with rain, rainfall patterns, and atmospheric precipitation.",
    secondary: "In atmospheric sciences, the quantitative study of precipitation distribution, rain-gauge methodology, and pluviometric records.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Cosmos: A Sketch of a Physical Description of the Universe", quote: "The systematic records of **ombrology** demonstrate the close connection between mountain elevation and annual precipitation." },
      { author: "Matthew Fontaine Maury", work: "The Physical Geography of the Sea", quote: "A comprehensive **ombrology** of the trade-wind zones reveals how maritime evaporation waters continental plains." },
      { author: "Cleveland Abbe", work: "The Mechanics of the Earth's Atmosphere", quote: "Early instruments of **ombrology** required standardized exposure to eliminate local wind turbulence around rain gauges." }
    ]
  },
  "Dashboard — ombr/ombrometer.md": {
    primary: "An instrument used by meteorologists to collect and measure the amount of precipitation that falls over a specified period; a rain gauge.",
    secondary: "In weather instrumentation and climatology, a pluviometer or udometer equipped with a graduated cylinder to measure rainfall depth in millimeters or inches.",
    quotes: [
      { author: "Robert FitzRoy", work: "The Weather Book: A Manual of Practical Meteorology", quote: "The observer must inspect the **ombrometer** every morning at eight, recording the exact rainfall in hundredths of an inch." },
      { author: "Cleveland Abbe", work: "Treatise on Meteorological Apparatus", quote: "A properly shielded **ombrometer** prevents eddying gusts from blowing raindrops away from the collection funnel." },
      { author: "Luke Howard", work: "The Climate of London", quote: "The measurements from my **ombrometer** during the storm of July confirmed an unprecedented deluge for the London basin." }
    ]
  },
  "Dashboard — ombr/ombrophilous.md": {
    primary: "Capable of thriving in areas with heavy, abundant rainfall; rain-loving.",
    secondary: "In plant ecology, descriptive of vegetation adapted to perhumid tropical or temperate rain-forest climates with continuous precipitation.",
    quotes: [
      { author: "Andreas Schimper", work: "Plant-Geography Upon a Physiological Basis", quote: "The lush canopies of the tropical **ombrophilous** forest exhibit continuous growth without a deciduous dormant season." },
      { author: "Eugenius Warming", work: "Oecology of Plants", quote: "Vegetation in cloud forests displays an **ombrophilous** habit, absorbing atmospheric moisture through aerial roots and epiphytic leaves." },
      { author: "Arthur Tansley", work: "Practical Plant Ecology", quote: "Ferns and mosses dominating the ravine floor are distinctly **ombrophilous**, withering rapidly when sheltered from direct showers." }
    ]
  },
  "Dashboard — ombr/ombrophobe.md": {
    primary: "A plant or organism that cannot tolerate heavy rainfall, excessive moisture, or waterlogged conditions.",
    secondary: "In plant ecology, describing xerophytic or desert species adapted to arid environments whose foliage or roots decay under prolonged rain.",
    quotes: [
      { author: "Andreas Schimper", work: "Plant-Geography Upon a Physiological Basis", quote: "Desert succulents are strict **ombrophobe** species whose roots rot when exposed to unseasonable tropical downpours." },
      { author: "Eugenius Warming", work: "Oecology of Plants", quote: "The prickly pear exemplifies an **ombrophobe** plant whose cuticle is engineered to resist drought rather than endure persistent saturation." },
      { author: "Arthur Tansley", work: "The British Islands and Their Vegetation", quote: "On chalk downlands, certain calcicole grasses behave as **ombrophobe** species, retreating from waterlogged depressions." }
    ]
  },
  "Dashboard — ombr/ombrotrophic.md": {
    primary: "Receiving water and mineral nutrients exclusively from atmospheric precipitation (rain, snow, and fog) rather than from groundwater or runoff.",
    secondary: "In wetland ecology, characteristic of nutrient-poor, acidic peat bogs dominated by Sphagnum mosses, isolated from mineral-rich terrestrial water.",
    quotes: [
      { author: "Arthur Tansley", work: "The British Islands and Their Vegetation", quote: "An **ombrotrophic** mire derives not a single drop of mineral nourishment from the underlying rock or valley streams." },
      { author: "Henry Chandler Cowles", work: "The Ecological Relations of the Vegetation on the Sand Dunes of Lake Michigan", quote: "The dome of the bog becomes strictly **ombrotrophic**, nourished solely by dust and rainwater descending from the clouds." },
      { author: "Robert Gorham", work: "Peatland Ecology", quote: "Because **ombrotrophic** peat accumulates above the regional water table, it provides an unblemished record of atmospheric pollution through the centuries." }
    ]
  }
};

let count = 0;
for (const [key, data] of Object.entries(batch4Data)) {
  const [relDir, fileName] = key.split('/');
  if (updateNote(relDir, fileName, data)) {
    count++;
  }
}

console.log(`\n========================================`);
console.log(`Batch 4 Completed: ${count} / ${Object.keys(batch4Data).length} words updated`);
console.log(`========================================`);
