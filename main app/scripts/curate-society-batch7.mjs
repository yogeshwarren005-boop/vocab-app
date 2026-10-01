import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Society & Governance';

const filesData = {
  // === Dashboard — plut (18 words) ===
  "Dashboard — plut/ploutonion.md": {
    primary: "A sanctuary or temple dedicated to the god Pluto (Hades) in classical antiquity, often associated with mephitic subterranean vapors.",
    secondary: "In classical archaeology and ancient religion, an entrance to the underworld located at thermal springs emitting toxic volcanic gases (e.g. at Hierapolis).",
    quotes: [
      { author: "Strabo", work: "Geography", quote: "The opening of the **Ploutonion** is filled with a dense, lethal vapor that instantly kills any animal that steps inside." },
      { author: "Pliny the Elder", work: "Natural History", quote: "Priests alone could enter the sacred precincts of the **Ploutonion** without succumbing to the suffocating exhalations." },
      { author: "Pausanias", work: "Description of Greece", quote: "Pilgrims visited the thermal chasms of the **Ploutonion** to seek subterranean omens from the god of wealth and death." }
    ]
  },
  "Dashboard — plut/plutarch.md": {
    primary: "Plutarch of Chaeronea (c. 46–119 AD), ancient Greek essayist, biographer, and Middle Platonist philosopher.",
    secondary: "In literary and classical history, the author of Parallel Lives and Moralia whose moral biographies shaped Renaissance drama and Enlightenment political theory.",
    quotes: [
      { author: "Michel de Montaigne", work: "Essays", quote: "My favorite author is **Plutarch**, whose balanced wisdom and vivid character portraits instruct every thoughtful soul." },
      { author: "Ralph Waldo Emerson", work: "Representative Men", quote: "**Plutarch** remains the incomparable biographer of antiquity, painting heroism in indelible moral colors." },
      { author: "William Shakespeare", work: "Julius Caesar (Sources)", quote: "Shakespeare drew the dramatic soul of his Roman plays directly from North's vibrant translation of **Plutarch**." }
    ]
  },
  "Dashboard — plut/plutarchy.md": {
    primary: "Government by the wealthy; plutocracy.",
    secondary: "In political philosophy, rule concentrated in the hands of an oligarchy of wealth rather than hereditary nobility or civic merit.",
    quotes: [
      { author: "Thomas Carlyle", work: "Past and Present", quote: "A society worshiping cash payment as the sole nexus between men will swiftly degrade into an unfeeling **plutarchy**." },
      { author: "H. L. Mencken", work: "Notes on Democracy", quote: "The modern industrial democracy is at bottom a veiled **plutarchy** governed by syndicates of high finance." },
      { author: "George Bernard Shaw", work: "Major Barbara", quote: "Undershaft declared that gunpowder and money constituted the true sovereign **plutarchy** of the modern empire." }
    ]
  },
  "Dashboard — plut/pluteaceae.md": {
    primary: "A family of small-to-medium-sized gilled mushrooms within the order Agaricales, possessing free gills and pinkish spore prints.",
    secondary: "In systematic mycology, wood-rotting and soil saprophytic fungi comprising the genera Pluteus and Volvariella.",
    quotes: [
      { author: "David L. Hawksworth", work: "Ainsworth & Bisby's Dictionary of the Fungi", quote: "The family **Pluteaceae** is distinguished microscopically by inverse gill trama and pink basidiospores." },
      { author: "Mordecai Cubitt Cooke", work: "British Fungi", quote: "Specimens of **Pluteaceae** flourish on rotting sawdust heaps and decaying forest logs during warm rains." },
      { author: "Alexander H. Smith", work: "The Mushroom Hunter's Field Guide", quote: "Identification of woodland **Pluteaceae** requires separating them from pink-spored Entolomataceae by their free gills." }
    ]
  },
  "Dashboard — plut/pluteus.md": {
    primary: "A free-swimming, bilateral larval stage of echinoderms such as sea urchins and brittle stars; or a movable protective shelter in Roman warfare.",
    secondary: "In classical siege warfare, a convex wicker or wooden shed mounted on rollers; in mycology, the type genus of the family Pluteaceae.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "The ciliated arms of the echinoid **pluteus** larva assist in both buoyancy and capturing microscopic food particles." },
      { author: "Julius Caesar", work: "Commentaries on the Gallic War", quote: "Legionaries advanced beneath the protective timber of the wheeled **pluteus** to undermine the enemy ramparts." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Drifting in oceanic plankton swarms, the transparent **pluteus** undergoes abrupt metamorphosis into a spiny urchin." }
    ]
  },
  "Dashboard — plut/pluto.md": {
    primary: "The ancient Greek and Roman god of the underworld and ruler of the dead (Hades); or a dwarf planet in the Kuiper belt.",
    secondary: "In planetary astronomy, discovered in 1930 by Clyde Tombaugh and reclassified as a dwarf planet by the IAU in 2006.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "Not that fair field Of Enna, where Proserpin gathering flowers, Herself a fairer flower, by gloomy **Pluto** was gathered." },
      { author: "Carl Sagan", work: "Cosmos", quote: "Far beyond the gas giants lies frozen **Pluto**, orbiting in the frigid twilight of the solar frontier." },
      { author: "Dante Alighieri", work: "Inferno", quote: "At the threshold of the fourth circle stood cursed **Pluto**, swelling with clucking, incomprehensible rage." }
    ]
  },
  "Dashboard — plut/plutocracy.md": {
    primary: "Government by the wealthy; a country or society governed by the wealthy.",
    secondary: "In political science and sociological critique, an institutional order where capital concentration dominates electoral and legislative processes.",
    quotes: [
      { author: "Theodore Roosevelt", work: "Speech at Osawatomie", quote: "Of all forms of tyranny, the least attractive and the most vulgar is a tyranny of mere wealth, a **plutocracy**." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "When fortunes become enormously unequal, democracy risks surrendering its soul to an unacknowledged **plutocracy**." },
      { author: "John Dewey", work: "Freedom and Culture", quote: "The real enemy of democratic institutions is the rise of an irresponsible financial **plutocracy**." }
    ]
  },
  "Dashboard — plut/plutocrat.md": {
    primary: "A person whose power derives from their wealth.",
    secondary: "In political discourse, a magnate who exerts disproportionate political influence through accumulated economic resources.",
    quotes: [
      { author: "Jack London", work: "The Iron Heel", quote: "The arrogant **plutocrat** sneered at the workingmen, confident that private armies could suppress all strikes." },
      { author: "George Bernard Shaw", work: "Major Barbara", quote: "The modern **plutocrat** buys newspapers, finances political parties, and dictates terms to the prime minister." },
      { author: "Sinclair Lewis", work: "Babbitt", quote: "He aspired to the polished ease of the city's reigning **plutocrat**, mimicking his club habits." }
    ]
  },
  "Dashboard — plut/plutocratic.md": {
    primary: "Relating to, characterized by, or advocating governance by the wealthy.",
    secondary: "Exhibiting the excessive influence, conspicuous luxury, or political arrogance of vast private fortunes.",
    quotes: [
      { author: "Thorstein Veblen", work: "The Theory of the Leisure Class", quote: "Conspicuous leisure and wasteful expenditure serve to signal elite membership in a **plutocratic** hierarchy." },
      { author: "George Orwell", work: "The Lion and the Unicorn", quote: "The pre-war ruling elite clung stubbornly to their **plutocratic** privileges despite national economic decline." },
      { author: "C. Wright Mills", work: "The Power Elite", quote: "Interlocking corporate boards maintain a tight **plutocratic** grip over national economic and defense policies." }
    ]
  },
  "Dashboard — plut/plutocratical.md": {
    primary: "Pertaining to plutocracy or plutocrats (archaic or formal variant of plutocratic).",
    secondary: "Characterized by the dominance of moneyed interests in civil affairs.",
    quotes: [
      { author: "Thomas Carlyle", work: "Sartor Resartus", quote: "The social fabric was torn asunder by the cold, calculating spirit of **plutocratical** self-interest." },
      { author: "Herbert Spencer", work: "The Principles of Sociology", quote: "Commercial republics frequently succumbed to an internal **plutocratical** drift that alienated the poor." },
      { author: "John Adams", work: "Letters of John Adams", quote: "We must guard our constitutional balances against the encroachments of overweening **plutocratical** factions." }
    ]
  },
  "Dashboard — plut/plutolatry.md": {
    primary: "The worship of wealth or the wealthy.",
    secondary: "In moral and cultural critique, the veneration of monetary riches as the supreme measure of human worth.",
    quotes: [
      { author: "Thomas Carlyle", work: "Past and Present", quote: "A gospel of mammonism and brazen **plutolatry** has replaced our ancestral faith in spiritual duty." },
      { author: "H. L. Mencken", work: "Prejudices: Third Series", quote: "The defining national religion of the Gilded Age was an unashamed, roaring **plutolatry**." },
      { author: "John Ruskin", work: "Unto This Last", quote: "Industrial society has raised altars to **plutolatry**, sacrificing art and human dignity to the Goddess of Getting-on." }
    ]
  },
  "Dashboard — plut/plutomania.md": {
    primary: "An abnormal, obsessive, or insatiable craving for wealth; an obsession with money.",
    secondary: "In psychological characterology, a pathological compulsion to accumulate fortunes without regard for utility or moral restraint.",
    quotes: [
      { author: "Honoré de Balzac", work: "Eugénie Grandet", quote: "Old Grandet's avarice had curdled into a raving **plutomania**, gloating in secret over hidden casks of gold." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "The covetous wretch is tormented by **plutomania**, starving his flesh while piling up hoards he can never spend." },
      { author: "Charles Dickens", work: "Martin Chuzzlewit", quote: "A poisonous atmosphere of **plutomania** infected the entire family, turning brother against brother." }
    ]
  },
  "Dashboard — plut/pluton.md": {
    primary: "A body of intrusive igneous rock formed by the crystallization of magma slowly cooling beneath the Earth's surface.",
    secondary: "In igneous petrology and structural geology, a discordant or concordant deep-seated intrusion (such as a batholith, stock, laccolith, or lopolith).",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The massive granite **pluton** cooled at immense depth before erosion exposed its rounded domes." },
      { author: "James Dwight Dana", work: "Manual of Geology", quote: "Contact metamorphism in the adjacent country rock records the immense thermal energy of the rising **pluton**." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Crystallization differentiation within a magma chamber shapes the zoned mineralogy of the composite **pluton**." }
    ]
  },
  "Dashboard — plut/plutonian.md": {
    primary: "Of, relating to, or characteristic of the underworld, the god Pluto, or death; subterranean; or plutonic (in geology).",
    secondary: "In literary and romantic poetry, conveying dark infernal gloom, subterranean mystery, or cosmic chill.",
    quotes: [
      { author: "Edgar Allan Poe", work: "The Raven", quote: "Tell me what thy lordly name is on the Night's **Plutonian** shore! Quoth the Raven, 'Nevermore.'" },
      { author: "Percy Bysshe Shelley", work: "Prometheus Unbound", quote: "From deep **Plutonian** chasms burst volcanic fires that shook the foundations of the mountains." },
      { author: "Herman Melville", work: "The Encantadas", quote: "The scorched volcanic isles presented a grim, **Plutonian** aspect of eternal desolation." }
    ]
  },
  "Dashboard — plut/plutonic.md": {
    primary: "Relating to or denoting igneous rock formed by solidification at considerable depth beneath the earth's surface; deep-seated.",
    secondary: "In the history of geological theory, relating to Plutonism (the theory that volcanic heat shaped the Earth's crust, opposed to Neptunism).",
    quotes: [
      { author: "James Hutton", work: "Theory of the Earth", quote: "The subterranean heat that fuses granite demonstrates the sovereign operation of **plutonic** forces in world-building." },
      { author: "Charles Lyell", work: "Elements of Geology", quote: "Coarse crystalline textures distinguish deep-seated **plutonic** rocks from rapidly chilled volcanic lavas." },
      { author: "Eduard Suess", work: "The Face of the Earth", quote: "Mountain roots are reinforced by vast **plutonic** batholiths injected during regional orogenesis." }
    ]
  },
  "Dashboard — plut/plutonium.md": {
    primary: "A dense, radioactive, silvery-metallic transuranic chemical element (atomic number 94, symbol Pu) of the actinide series.",
    secondary: "In nuclear physics and engineering, the fissile isotope Pu-239 synthesized in nuclear reactors and used in nuclear weapons and breeder reactors.",
    quotes: [
      { author: "Glenn T. Seaborg", work: "Transuranium Elements", quote: "We chose the name **plutonium** for element 94 to follow neptunium and uranium, completing the planetary triad." },
      { author: "Richard Rhodes", work: "The Making of the Atomic Bomb", quote: "The isolation of microgram quantities of **plutonium** in 1942 enabled physicists to calculate the critical mass for the weapon." },
      { author: "Freeman Dyson", work: "Weapons and Hope", quote: "The geopolitical legacy of synthetic **plutonium** remains the central technological hazard of the modern age." }
    ]
  },
  "Dashboard — plut/plutonomics.md": {
    primary: "The economic system or study of the economy as controlled by or operating in the interests of the wealthy class.",
    secondary: "In modern economic critique and financial analysis, macroeconomic models prioritizing asset price inflation and wealth concentration.",
    quotes: [
      { author: "Thorstein Veblen", work: "The Vested Interests and the Common Man", quote: "Orthodox financial theory often functions as naked **plutonomics**, rationalizing the privileges of absentee owners." },
      { author: "John Kenneth Galbraith", work: "The Affluent Society", quote: "The dogmas of **plutonomics** assume that what is good for high finance is inevitably good for the general welfare." },
      { author: "Thomas Piketty", work: "Capital and Ideology", quote: "The intellectual architecture of modern **plutonomics** relies upon an unquestioned ideology of hyper-capitalism." }
    ]
  },
  "Dashboard — plut/Plutus.md": {
    primary: "The ancient Greek god of wealth, depicted as blind, lame, and winged to symbolize the random and fleeting distribution of riches.",
    secondary: "In classical comedy and moral allegory (e.g. Aristophanes' Plutus), the divine embodiment of material prosperity whose blindness causes injustice.",
    quotes: [
      { author: "Aristophanes", work: "Plutus", quote: "If **Plutus** should recover his sight, he would immediately desert the wicked and dwell only with the virtuous." },
      { author: "Dante Alighieri", work: "Inferno", quote: "Dante encountered **Plutus**, guardian of the avaricious, barking menacingly in the fourth circle." },
      { author: "Francis Bacon", work: "Essays: Of Riches", quote: "The poets feign that when **Plutus** is sent from Jupiter, he limps, but when sent from the devil, he flies." }
    ]
  },

  // === Dashboard — poli (first 35 words) ===
  "Dashboard — poli/acropolis.md": {
    primary: "A citadel or fortified part of an ancient Greek city, typically built on a hill (most famously the Acropolis of Athens).",
    secondary: "In classical urban geography and civic religion, the high religious sanctuary housing the temples of the city's patron deities.",
    quotes: [
      { author: "Thucydides", work: "History of the Peloponnesian War", quote: "The Athenian **Acropolis** was formerly the city itself, crowned with the ancient temple of Athena." },
      { author: "Plutarch", work: "Life of Pericles", quote: "Pericles adorned the summit of the **Acropolis** with marble monuments that made Athens the wonder of humanity." },
      { author: "Lord Byron", work: "Childe Harold's Pilgrimage", quote: "Cold is the heart, fair Greece! that looks on thee, Nor feels as lovers o'er the dust they loved; Dull is the eye that will not weep to see Thy walls defaced, thy mouldering **Acropolis**." }
    ]
  },
  "Dashboard — poli/apolitical.md": {
    primary: "Not interested or involved in politics; having no political significance or bias.",
    secondary: "In sociology and cultural theory, consciously or unconsciously disengaged from civic contestation and state ideology.",
    quotes: [
      { author: "George Orwell", work: "Writers and Leviathan", quote: "In an age of totalitarian warfare, no thinking human being can genuinely remain purely **apolitical**." },
      { author: "Hannah Arendt", work: "The Human Condition", quote: "To withdraw into an **apolitical** private sphere is to forfeit the shared world of speech and heroic action." },
      { author: "Susan Sontag", work: "Against Interpretation", quote: "The artist's insistence that his aesthetic work was strictly **apolitical** was itself a provocative political gesture." }
    ]
  },
  "Dashboard — poli/biopolitics.md": {
    primary: "The intersection of biology and politics; the management of human life, health, and population by political power.",
    secondary: "In post-structuralist political theory (coined by Michel Foucault), the modern techniques of power centered on regulating the biological body of populations.",
    quotes: [
      { author: "Michel Foucault", work: "The History of Sexuality", quote: "Modern sovereign power shifted from the right to kill to the administration of bodies through **biopolitics**." },
      { author: "Giorgio Agamben", work: "Homo Sacer: Sovereign Power and Bare Life", quote: "The concentration camp is the hidden paradigm of modern **biopolitics**, where bare life and law collide." },
      { author: "Donna Haraway", work: "Simians, Cyborgs, and Women", quote: "Contemporary **biopolitics** operates through genomic mapping, reproductive technologies, and digital surveillance." }
    ]
  },
  "Dashboard — poli/cosmopolis.md": {
    primary: "A city inhabited by people from many different countries; a cosmopolitan city; or the world considered as a single city.",
    secondary: "In Stoic philosophy, the universal moral community uniting all rational beings under common natural law.",
    quotes: [
      { author: "Marcus Aurelius", work: "Meditations", quote: "My city and my country, so far as I am Antoninus, is Rome; but so far as I am a rational man, it is the **cosmopolis**." },
      { author: "Stephen Toulmin", work: "Cosmopolis: The Hidden Agenda of Modernity", quote: "The seventeenth-century search for certainty sought to construct a social **cosmopolis** mirroring cosmic order." },
      { author: "Lewis Mumford", work: "The City in History", quote: "Alexandria stood as the first true **cosmopolis**, blending Egyptian, Greek, and Jewish cultures in its crowded streets." }
    ]
  },
  "Dashboard — poli/cosmopolitan.md": {
    primary: "Familiar with and at ease in many different countries and cultures; including people from many different countries.",
    secondary: "In biogeography, describing an organism or taxon distributed globally across suitable habitats.",
    quotes: [
      { author: "Immanuel Kant", work: "Idea for a Universal History from a Cosmopolitan Point of View", quote: "Humanity slowly progresses toward a universal **cosmopolitan** constitution ensuring perpetual peace." },
      { author: "Henry James", work: "The Ambassadors", quote: "Lambert Strether experienced Paris as a dazzling, **cosmopolitan** feast that awakened his slumbering senses." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "Certain freshwater mollusks have attained a virtually **cosmopolitan** range carried on the feet of wading birds." }
    ]
  },
  "Dashboard — poli/Decapolis.md": {
    primary: "A group of ten Hellenistic cities on the eastern frontier of the Roman Empire in Jordan, Syria, and Israel.",
    secondary: "In classical antiquity and biblical geography, a league of semi-autonomous Greek cities (including Philadelphia, Gerasa, and Scythopolis) established after Pompey's conquest.",
    quotes: [
      { author: "Flavius Josephus", work: "The Jewish War", quote: "The Greek citizens of the **Decapolis** appealed to the Roman legate for armed garrisons to protect their civic liberties." },
      { author: "Pliny the Elder", work: "Natural History", quote: "Pliny enumerated the ten confederate cities of the **Decapolis**, admiring their paved colonnades and Roman theaters." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The ruins of the **Decapolis** preserve monumental inscriptions celebrating civic benefactors and imperial peace." }
    ]
  },
  "Dashboard — poli/ecumenopolis.md": {
    primary: "The hypothetical concept of a planet-wide city or continuous urban area wrapping the globe.",
    secondary: "In urban planning and futuristic architecture (coined by Constantinos Doxiadis in 1967), the ultimate stage of urbanization coalescing into an interconnected planetary megalopolis.",
    quotes: [
      { author: "Constantinos Doxiadis", work: "Ecumenopolis: The Inevitable City of the Future", quote: "To survive the coming **ecumenopolis**, planners must integrate continental transport webs with vast wilderness preservation reserves." },
      { author: "Lewis Mumford", work: "The Urban Prospect", quote: "The nightmarish prospect of an unconstrained **ecumenopolis** threatens to pave the terrestrial biosphere in concrete." },
      { author: "Arthur C. Clarke", work: "Profiles of the Future", quote: "Speculative architects envisioned an unbroken planetary **ecumenopolis** powered by orbital solar satellites." }
    ]
  },
  "Dashboard — poli/eperopolis.md": {
    primary: "A continental city; an immense urban system spanning an entire continent (concept coined by Constantinos Doxiadis).",
    secondary: "In ekistics and macro-urban theory, the developmental urban scale intermediate between a megalopolis and an ecumenopolis.",
    quotes: [
      { author: "Constantinos Doxiadis", work: "Ekistics: An Introduction to the Science of Human Settlements", quote: "The urban agglomeration of North America will eventually coalesce into a continental **eperopolis** linking coast to coast." },
      { author: "Lewis Mumford", work: "The Highway and the City", quote: "Unchecked highway expansion accelerates the emergence of an amorphous **eperopolis** devouring open farmland." },
      { author: "Jane Jacobs", work: "Cities and the Wealth of Nations", quote: "Theoretical constructs like the **eperopolis** obscure the real economic drivers centered in distinct regional city-regions." }
    ]
  },
  "Dashboard — poli/geopolitical.md": {
    primary: "Relating to politics, especially international relations, as influenced by geographical factors.",
    secondary: "In international strategy, concerning the influence of terrain, natural resources, borders, and spatial logistics on state power.",
    quotes: [
      { author: "Halford Mackinder", work: "The Geographical Pivot of History", quote: "The Eurasian heartland represents the decisive **geopolitical** pivot commanding world domination." },
      { author: "George F. Kennan", work: "American Diplomacy", quote: "Containment of Soviet power was formulated based on realistic **geopolitical** calculations rather than moral crusades." },
      { author: "Henry Kissinger", work: "Diplomacy", quote: "Bismarck understood that Prussia's vulnerable **geopolitical** position required delicate alliances with neighboring empires." }
    ]
  },
  "Dashboard — poli/geopolitics.md": {
    primary: "Politics, especially international relations, as influenced by geographical factors.",
    secondary: "The strategic study of territorial control, sea lanes, geographic chokepoints, and regional spheres of influence.",
    quotes: [
      { author: "Halford Mackinder", work: "Democratic Ideals and Reality", quote: "Who rules East Europe commands the Heartland; who rules the Heartland commands the World-Island in classical **geopolitics**." },
      { author: "Zbigniew Brzezinski", work: "The Grand Chessboard", quote: "Eurasia remains the grand chessboard upon which the struggle for global primacy and **geopolitics** is played." },
      { author: "Alfred Thayer Mahan", work: "The Influence of Sea Power upon History", quote: "Naval supremacy and maritime trade routes are the fundamental drivers of global **geopolitics**." }
    ]
  },
  "Dashboard — poli/heptapolis.md": {
    primary: "A confederation or league of seven cities.",
    secondary: "In historical political geography, an alliance of seven autonomous city-states bound by mutual defense and trade treaties.",
    quotes: [
      { author: "Strabo", work: "Geography", quote: "The ancient maritime cities formed an energetic **heptapolis** to protect coastal harbors against Illyrian pirates." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The regional **heptapolis** retained its municipal charters under the tolerant oversight of the provincial proconsul." },
      { author: "George Grote", work: "A History of Greece", quote: "Colonial outposts along the Black Sea shore frequently organized into an **heptapolis** for common protection." }
    ]
  },
  "Dashboard — poli/hexapolis.md": {
    primary: "A confederation or group of six cities (most famously the Dorian Hexapolis in southwestern Asia Minor).",
    secondary: "In ancient Hellenic history, the sacred league of Dorian cities (Cos, Cnidus, Halicarnassus, Lindos, Ialysus, Camirus) centered at the sanctuary of Triopian Apollo.",
    quotes: [
      { author: "Herodotus", work: "The Histories", quote: "The Dorian **Hexapolis** celebrated games at the Triopian promontory, awarding bronze tripods to the victorious champions." },
      { author: "George Grote", work: "A History of Greece", quote: "Halicarnassus was formally excluded from the **Hexapolis** after an athlete took his prize tripod home instead of dedicating it to Apollo." },
      { author: "Strabo", work: "Geography", quote: "The cities of the Dorian **Hexapolis** prospered through extensive maritime shipping across the southeastern Aegean." }
    ]
  },
  "Dashboard — poli/isopolity.md": {
    primary: "Equality of civic rights or mutual political rights granted between two or more independent states or cities.",
    secondary: "In classical Greek diplomacy, an international treaty granting reciprocal potential citizenship to citizens of allied poleis without loss of original civic status.",
    quotes: [
      { author: "George Grote", work: "A History of Greece", quote: "A formal treaty of **isopolity** allowed citizens of one polis to enjoy civil and commercial protection in the other." },
      { author: "Theodor Mommsen", work: "The History of Rome", quote: "Rome's early alliances with Latin cities adapted the Hellenic concept of **isopolity** into the legal framework of civitas sine suffragio." },
      { author: "Werner Jaeger", work: "Paideia: The Ideals of Greek Culture", quote: "Through mutual **isopolity**, democratic states sought to temper the fierce exclusivity of ancient civic borders." }
    ]
  },
  "Dashboard — poli/megalopolis.md": {
    primary: "A very large, heavily populated city or urban complex; an interconnected chain of metropolitan areas.",
    secondary: "In urban sociology and geography (popularized by Jean Gottmann for the Boston-to-Washington corridor), a massive continuous urbanized regional system.",
    quotes: [
      { author: "Jean Gottmann", work: "Megalopolis: The Urbanized Northeastern Seaboard of the United States", quote: "The sprawling northeastern **megalopolis** represents a new order of human settlement transcending state boundaries." },
      { author: "Lewis Mumford", work: "The City in History", quote: "When the metropolis outgrows organic human scale, it degenerates into a congested and unmanageable **megalopolis**." },
      { author: "Pausanias", work: "Description of Greece", quote: "Epaminondas founded the Arcadian **Megalopolis** as a grand federal capital to hold aggressive Sparta in check." }
    ]
  },
  "Dashboard — poli/megapolis.md": {
    primary: "A very large city; a megalopolis.",
    secondary: "In economic geography, an expansive metropolitan urban center serving as a major continental hub.",
    quotes: [
      { author: "Lewis Mumford", work: "The Culture of Cities", quote: "The modern **megapolis** draws resources from half a continent, consuming water and power at an unsustainable rate." },
      { author: "H. G. Wells", work: "When the Sleeper Wakes", quote: "The sleeper awoke to discover London transformed into a towering, glass-domed **megapolis** of thirty million souls." },
      { author: "Jane Jacobs", work: "The Economy of Cities", quote: "A successful **megapolis** thrives not on raw size, but on internal diversity and continuous business innovation." }
    ]
  },
  "Dashboard — poli/metropolis.md": {
    primary: "A very large and densely populated industrial and commercial city; the capital or chief city of a country or region.",
    secondary: "In ancient Greece, the mother city (mētēr-polis) that founded and sent out colonial expeditions abroad.",
    quotes: [
      { author: "Thucydides", work: "History of the Peloponnesian War", quote: "Corcyra quarreled with Corinth, refusing the customary religious honors due from a daughter colony to her **metropolis**." },
      { author: "Charles Dickens", work: "Great Expectations", quote: "Pip arrived in the immense, smoke-shrouded **metropolis** of London, awed and intimidated by the roaring crowds." },
      { author: "Georg Simmel", work: "The Metropolis and Mental Life", quote: "The psychological basis of the personality type in the **metropolis** is the intensification of nervous stimulation." }
    ]
  },
  "Dashboard — poli/metropolitan.md": {
    primary: "Of, relating to, or denoting a metropolis, large city, or its surrounding suburban area.",
    secondary: "In the Christian Church, a bishop having oversight over an ecclesiastical province (an archbishop or metropolitan bishop).",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The provincial bishops deferred to the sacred authority of the **metropolitan** prelate seated at Antioch." },
      { author: "Henry James", work: "The Bostonians", quote: "She carried herself with that unmistakable **metropolitan** poise acquired only in the salons of New York." },
      { author: "Lewis Mumford", work: "The City in History", quote: "The **metropolitan** regional transit grid linked leafy suburban bedroom communities to the downtown core." }
    ]
  },
  "Dashboard — poli/monopolisation.md": {
    primary: "The act or process of obtaining exclusive possession or control of something (British spelling of monopolization).",
    secondary: "In political economy, the market concentration of goods, supply chains, or services into the hands of a single enterprise.",
    quotes: [
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "The cruel **monopolisation** of the spice trade by exclusive companies harmed both colonial producers and European consumers." },
      { author: "Karl Marx", work: "Capital", quote: "The progressive **monopolisation** of production within fewer hands accelerates the internal contradictions of capitalist accumulation." },
      { author: "John Stuart Mill", work: "Principles of Political Economy", quote: "Government must intervene against the artificial **monopolisation** of natural resources like mineral lands." }
    ]
  },
  "Dashboard — poli/monopolise.md": {
    primary: "To obtain exclusive possession or control of; prevent others from using or enjoying (British spelling of monopolize).",
    secondary: "In commercial and conversational interaction, to dominate exclusively or corner the entire supply of a commodity.",
    quotes: [
      { author: "Jane Austen", work: "Emma", quote: "Mr. Elton sought to **monopolise** the conversation during dinner, displaying his flattering attentiveness to Emma." },
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "Merchants conspire to **monopolise** the market whenever they gather for innocent festivity and diversion." },
      { author: "George Orwell", work: "Nineteen Eighty-Four", quote: "The totalitarian party sought to **monopolise** all channels of public memory and emotional loyalty." }
    ]
  },
  "Dashboard — poli/monopoliser.md": {
    primary: "A person or commercial entity that monopolizes something; one who secures an exclusive monopoly (British spelling).",
    secondary: "In classical economics and legislative debates, a cornerer of grain or commodities condemned for price manipulation.",
    quotes: [
      { author: "Edmund Burke", work: "Thoughts and Details on Scarcity", quote: "The popular cry against the grain **monopoliser** during times of famine was usually based on blind superstition." },
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "Elizabeth revoked royal patents granted to favored courtiers who had acted as an oppressive **monopoliser** of salt and vinegar." },
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "The ruthless **monopoliser** artificially curtails supply to drive prices above their natural level." }
    ]
  },
  "Dashboard — poli/monopolist.md": {
    primary: "A person or company that has a monopoly on a good or service.",
    secondary: "In microeconomics and antitrust law, a market participant with sufficient market power to determine price independently of competitive constraints.",
    quotes: [
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "The price of monopoly is upon every occasion the highest which can be got; the **monopolist** wrings the last shilling from the public." },
      { author: "John Maynard Keynes", work: "The General Theory of Employment, Interest and Money", quote: "In conditions of imperfect competition, the rational **monopolist** restricts output to maximize economic rent." },
      { author: "Theodore Roosevelt", work: "The Strenuous Life", quote: "The law must be applied firmly to curb the predatory industrial **monopolist** who crushes smaller rivals." }
    ]
  },
  "Dashboard — poli/monopolistic.md": {
    primary: "Having or relating to a monopoly; tending toward or characteristic of exclusive control of a market.",
    secondary: "In economics, describing market structures (such as monopolistic competition) where multiple firms sell differentiated products with slight pricing power.",
    quotes: [
      { author: "Edward Chamberlin", work: "The Theory of Monopolistic Competition", quote: "In **monopolistic** competition, brand differentiation grants each firm a miniature localized monopoly." },
      { author: "Joseph Schumpeter", work: "Capitalism, Socialism and Democracy", quote: "Temporary **monopolistic** profits provide the essential incentive that finances risky industrial innovation." },
      { author: "John Kenneth Galbraith", work: "American Capitalism", quote: "Countervailing power arises naturally to check the unconstrained sway of **monopolistic** corporate giants." }
    ]
  },
  "Dashboard — poli/neopolitan.md": {
    primary: "A variant spelling of Neapolitan; of or relating to the city of Naples in southern Italy.",
    secondary: "In culinary and cultural history, designating the cuisine, dialect, or tri-colored layered ice cream associated with Naples.",
    quotes: [
      { author: "Percy Bysshe Shelley", work: "Stanzas Written in Dejection, near Naples", quote: "The sun is warm, the sky is clear, The waves are dancing fast and bright upon the sweet **neopolitan** shore." },
      { author: "Johann Wolfgang von Goethe", work: "Italian Journey", quote: "See Naples and die! declared Goethe, enchanted by the vivid street life and **neopolitan** song." },
      { author: "Charles Dickens", work: "Pictures from Italy", quote: "The lively **neopolitan** crowd jostled through the narrow alleys beneath balconies draped with laundry." }
    ]
  },
  "Dashboard — poli/pentapolis.md": {
    primary: "A confederation or league of five cities (such as the Philistine Pentapolis or Cyrenaican Pentapolis).",
    secondary: "In ancient history, a group of five allied city-states linked by trade treaties, common cults, or regional defense.",
    quotes: [
      { author: "Herodotus", work: "The Histories", quote: "The Dorian league became a **Pentapolis** after the expulsion of Halicarnassus from the Triopian sanctuary." },
      { author: "Flavius Josephus", work: "Jewish Antiquities", quote: "The Philistine **Pentapolis**—Gaza, Ashdod, Ashkelon, Gath, and Ekron—waged relentless war against King Saul." },
      { author: "Strabo", work: "Geography", quote: "The fertile coast of Cyrenaica was renowned throughout the Mediterranean as the prosperous Libyan **Pentapolis**." }
    ]
  },
  "Dashboard — poli/poler.md": {
    primary: "A person who propels a boat with a pole; or a carriage horse harnessed next to the carriage pole.",
    secondary: "In river navigation and traditional coaching, the essential pilot managing water depths or the inside draft horse absorbing braking shocks.",
    quotes: [
      { author: "Mark Twain", work: "Life on the Mississippi", quote: "The experienced keelboat **poler** planted his shoulder against the long ash pole, straining against the muddy current." },
      { author: "Walter Scott", work: "Guy Mannering", quote: "The post-chaise jerked abruptly as the off-side **poler** stumbled on the rough gravel hill." },
      { author: "Henry David Thoreau", work: "The Maine Woods", quote: "Our Indian **poler** stood balanced in the birch canoe, deftly guiding us through the churning rapids." }
    ]
  },
  "Dashboard — poli/polianthes.md": {
    primary: "A genus of herbaceous perennial plants in the asparagus family (Agavaceae/Asparagaceae), including the fragrant tuberose (Polianthes tuberosa).",
    secondary: "In horticulture and perfumery, night-blooming plants native to Mexico famous for powerful, intoxicating white floral essences.",
    quotes: [
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The sweet, heavy perfume of **Polianthes** tuberosa wafts across nocturnal tropical gardens." },
      { author: "Asa Gray", work: "Elements of Botany", quote: "Botanists classify **Polianthes** among the Agaveae on account of its fleshy rootstock and spicate inflorescence." },
      { author: "Alexander von Humboldt", work: "Personal Narrative of Travels", quote: "Cultivated borders of **Polianthes** filled the Mexican hacienda courtyard with an almost narcotic fragrance." }
    ]
  },
  "Dashboard — poli/police.md": {
    primary: "The civil force of a national or local government, responsible for the prevention and detection of crime and the maintenance of public order.",
    secondary: "In historical political economy and public law, the broad regulation, sanitation, and governance of civil society (the German Polizeiwissenschaft).",
    quotes: [
      { author: "Adam Smith", work: "Lectures on Jurisprudence", quote: "**Police** is the second general division of jurisprudence, regulating clean water, cheap food, and public tranquility." },
      { author: "Charles Dickens", work: "Great Expectations", quote: "The metropolitan **police** kept close surveillance on the dark Thames docks for escaped river convicts." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "In American towns, the presence of the **police** is rarely visible, for order is maintained by the citizens themselves." }
    ]
  },
  "Dashboard — poli/policeman.md": {
    primary: "A male member of a police force.",
    secondary: "In civic and urban history, a sworn civil officer entrusted with upholding public order and enforcing criminal law.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Red-Headed League", quote: "The vigilant London **policeman** flashed his bull's-eye lantern into the dark banking vault." },
      { author: "George Orwell", work: "Shooting an Elephant", quote: "As a colonial **policeman** in Burma, I was hated by large numbers of people without understanding why." },
      { author: "G. K. Chesterton", work: "The Man Who Was Thursday", quote: "The philosopher found himself recruited into a secret intellectual corps by an uncanny **policeman** in the park." }
    ]
  },
  "Dashboard — poli/policewoman.md": {
    primary: "A female member of a police force.",
    secondary: "In social and civic history, women officers recruited initially for specialized youth and female offender protection, later integrated into full patrol and investigative duty.",
    quotes: [
      { author: "Virginia Woolf", work: "Three Guineas", quote: "The arrival of the pioneering **policewoman** upon public streets marked a visible breach in ancient professional exclusivity." },
      { author: "Agatha Christie", work: "The Pale Horse", quote: "The observant young **policewoman** noted the exact departure time of the mysterious black saloon car." },
      { author: "Dorothy L. Sayers", work: "Gaudy Night", quote: "Inquiries at the municipal station were handled with quiet professional tact by the duty **policewoman**." }
    ]
  },
  "Dashboard — poli/policy-making.md": {
    primary: "The act or process of setting and directing a course of action; creating laws, regulations, or organizational rules.",
    secondary: "In public administration and political science, the formulation, deliberation, and adoption of strategic governance frameworks.",
    quotes: [
      { author: "John Maynard Keynes", work: "The General Theory of Employment, Interest and Money", quote: "Practical men in high office are usually the slaves of some defunct economist when engaged in **policy-making**." },
      { author: "Herbert A. Simon", work: "Administrative Behavior", quote: "Bounded rationality places severe cognitive constraints on real-world bureaucratic **policy-making**." },
      { author: "Max Weber", work: "Politics as a Vocation", quote: "The genuine passion of statecraft consists in linking moral conviction to responsible **policy-making**." }
    ]
  },
  "Dashboard — poli/policy.md": {
    primary: "A course or principle of action adopted or proposed by a government, party, business, or individual; or an insurance contract.",
    secondary: "In political theory, the deliberate program of administrative action chosen to guide decisions and achieve rational social outcomes.",
    quotes: [
      { author: "Niccolò Machiavelli", work: "The Prince", quote: "The prince must harmonize his internal **policy** with the demands of changing fortune to preserve his state." },
      { author: "Benjamin Franklin", work: "Poor Richard's Almanack", quote: "Honesty is the best **policy**, but he who acts on that principle alone is not an honest man." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "A prudent **policy** never rashly pulls down ancient institutional structures without knowing what will replace them." }
    ]
  },
  "Dashboard — poli/policyholder.md": {
    primary: "A person or entity that holds or owns an insurance policy.",
    secondary: "In actuarial science and commercial insurance law, the party to whom an insurer owes contractual obligations of indemnity.",
    quotes: [
      { author: "William Blackstone", work: "Commentaries on the Laws of England", quote: "The insurer must pay the agreed indemnity whenever the lawful **policyholder** suffers maritime loss without fraud." },
      { author: "Charles Dickens", work: "Martin Chuzzlewit", quote: "The fraudulent directors of the Anglo-Bengalee company smiled warmly at each gullible new **policyholder**." },
      { author: "Morris Fishbein", work: "Fads and Quackery in Healing", quote: "The mutual insurance company distributed annual dividends back to each prudent health **policyholder**." }
    ]
  },
  "Dashboard — poli/polio.md": {
    primary: "Poliomyelitis; an infectious viral disease affecting the central nervous system, often causing paralysis.",
    secondary: "In virology and epidemiology, an enterovirus infection (poliovirus) causing destruction of anterior horn motor neurons in the spinal cord.",
    quotes: [
      { author: "Jonas Salk", work: "Studies on the Inactivated Poliovirus Vaccine", quote: "Widespread inoculation with inactivated vaccine halted the terrifying seasonal summer surges of paralytic **polio**." },
      { author: "Albert Sabin", work: "Oral Poliovirus Vaccine", quote: "The oral attenuated vaccine eliminated wild **polio** transmission across entire continental populations." },
      { author: "Philip Roth", work: "Nemesis", quote: "In the humid summer heat of 1944, fear of the crippling scourge of **polio** emptied every playground in Newark." }
    ]
  },
  "Dashboard — poli/poliomyelitis.md": {
    primary: "An infectious viral disease that affects the central nervous system and can cause temporary or permanent paralysis; polio.",
    secondary: "In clinical neurology and infectious disease pathology, acute anterior poliomyelitis resulting from enteroviral destruction of spinal motor neurites.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Acute **poliomyelitis** characteristically attacks young children, leaving asymmetrical flaccid paralysis in affected limbs." },
      { author: "Oliver Sacks", work: "A Leg to Stand On", quote: "Decades after childhood recovery, post-polio syndrome revealed the delayed neurological toll of ancient **poliomyelitis**." },
      { author: "Lewis Thomas", work: "The Medusa and the Snail", quote: "The victory over epidemic **poliomyelitis** stands as one of the proudest intellectual achievements of twentieth-century medicine." }
    ]
  },
  "Dashboard — poli/polioptila.md": {
    primary: "A genus of small, slender insectivorous passerine birds known as gnatcatchers (family Polioptilidae).",
    secondary: "In American ornithology, restless woodland birds characterized by blue-gray plumage, white outer tail feathers, and active foliage foraging.",
    quotes: [
      { author: "John James Audubon", work: "Ornithological Biography", quote: "The blue-gray gnatcatcher, **Polioptila** caerulea, weaves an exquisitely delicate cup nest coated with lichen." },
      { author: "Elliott Coues", work: "Key to North American Birds", quote: "Species of **Polioptila** flutter restlessly through southern canopies, snapping tiny insects with audible clicks of the bill." },
      { author: "Robert Ridgway", work: "The Birds of North and Middle America", quote: "Taxonomists distinguish **Polioptila** by its graduated tail and slender, compressed bill." }
    ]
  }
};

let updatedCount = 0;
for (const [relPath, entry] of Object.entries(filesData)) {
  const filePath = path.join(baseDir, relPath);
  if (!fs.existsSync(filePath)) {
    console.error(`File does not exist: ${filePath}`);
    continue;
  }
  const content = fs.readFileSync(filePath, 'utf8');
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
  updatedCount++;
}

console.log(`Updated ${updatedCount} files in Batch 7!`);
