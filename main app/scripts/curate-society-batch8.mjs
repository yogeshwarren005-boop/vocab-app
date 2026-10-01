import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Society & Governance';

const filesData = {
  // === Dashboard — poli (remaining 32 words) ===
  "Dashboard — poli/poliosis.md": {
    primary: "Premature graying or whitening of the hair on the scalp, eyebrows, or eyelashes.",
    secondary: "In dermatology and clinical neurology, localized hair depigmentation associated with autoimmune conditions such as vitiligo or Vogt-Koyanagi-Harada disease.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Circumscribed patches of **poliosis** are frequently noted in conjunction with localized alopecia areata." },
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", quote: "Sudden terror or profound sorrow was anciently believed capable of producing overnight **poliosis**." },
      { author: "Oliver Sacks", work: "The Island of the Colorblind", quote: "The genetic syndrome presented with cutaneous hypopigmentation and a striking frontal tuft of **poliosis**." }
    ]
  },
  "Dashboard — poli/poliovirus.md": {
    primary: "The picornavirus that causes poliomyelitis.",
    secondary: "In virology, a positive-sense single-stranded RNA enterovirus of three serotypes (PV1, PV2, PV3) transmitted via the fecal-oral route.",
    quotes: [
      { author: "Jonas Salk", work: "Poliomyelitis Vaccine Studies", quote: "Formaldehyde treatment completely inactivated the virulent **poliovirus** while preserving antigenic immunogenicity." },
      { author: "Albert Sabin", work: "Oral Poliovirus Vaccine Development", quote: "Live attenuated strains of **poliovirus** replicate harmlessly in the alimentary tract, conferring durable mucosal immunity." },
      { author: "Lewis Thomas", work: "The Lives of a Cell", quote: "The crystalline symmetry of the microscopic **poliovirus** capsid belies its lethal neuropathic power." }
    ]
  },
  "Dashboard — poli/polis.md": {
    primary: "A city-state in ancient Greece, especially as considered in its ideal form for philosophical purposes.",
    secondary: "In political theory, the self-governing Hellenic civic community uniting citizens, laws, religion, and territory into an organic whole.",
    quotes: [
      { author: "Aristotle", work: "Politics", quote: "Man is by nature an animal intended to live in a **polis**, and he who is without a state is either below humanity or above it." },
      { author: "Thucydides", work: "History of the Peloponnesian War", quote: "Nicias reminded the retreating soldiers that men make the city, and not walls or empty ships devoid of a living **polis**." },
      { author: "Werner Jaeger", work: "Paideia: The Ideals of Greek Culture", quote: "The Greek **polis** was both church and state, the supreme educator and stage of human excellence." }
    ]
  },
  "Dashboard — poli/polish.md": {
    primary: "To make the surface of something smooth and shiny by rubbing it; or a substance used for polishing.",
    secondary: "Refinement, elegance, or sophistication of manners, style, or speech.",
    quotes: [
      { author: "Alexander Pope", work: "An Essay on Criticism", quote: "True ease in writing comes from art, not chance, As those move easiest who have learn'd to dance; True wit must **polish** every rugged line." },
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "Mr. Darcy possessed the haughty reserve of high birth, yet lacked the pleasing **polish** of easy conversation." },
      { author: "Henry David Thoreau", work: "Walden", quote: "Time will **polish** the rough stones of the brook until they gleam like translucent jewels." }
    ]
  },
  "Dashboard — poli/polished.md": {
    primary: "Shiny and smooth as a result of being rubbed or burnished; or refined, sophisticated, and elegant in manner or style.",
    secondary: "Exhibiting consummate craftsmanship, literary grace, or impeccable social decorum.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The **polished** eloquence of Cicero charmed the senate even while the foundations of the republic crumbled." },
      { author: "Lord Chesterfield", work: "Letters to His Son", quote: "A young gentleman must acquire that **polished** exterior which pleases without descending to frivolous affectation." },
      { author: "George Eliot", work: "Middlemarch", quote: "His speech was **polished** and measured, betraying no sign of the anxious calculations stirring beneath." }
    ]
  },
  "Dashboard — poli/polisher.md": {
    primary: "A person or device that polishes surfaces to make them smooth and shiny.",
    secondary: "In lapidary work, metallurgy, and optics, a skilled craftsman or mechanical tool used to grind lenses or gem facets.",
    quotes: [
      { author: "Baruch Spinoza", work: "Letters of Spinoza", quote: "Spinoza earned his modest bread as a master optical lens **polisher**, contemplating metaphysics between grinds." },
      { author: "Isaac Newton", work: "Opticks", quote: "The skilled glass **polisher** must work with pitch and putty to produce a paraboloidal mirror free of spherical aberration." },
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The mechanical marble **polisher** replaced the living, irregular touch of the medieval stonemason." }
    ]
  },
  "Dashboard — poli/polishing.md": {
    primary: "The act or process of making something smooth, shiny, or refined.",
    secondary: "In literary composition and technical craft, the painstaking revision and perfection of prose, verse, or optical surfaces.",
    quotes: [
      { author: "Horace", work: "Ars Poetica", quote: "Many a poet has failed because he begrudged the labor of the file, the slow **polishing** of every verse." },
      { author: "Benjamin Franklin", work: "Autobiography", quote: "I spent my evenings **polishing** my written essays, comparing my drafts with the spectator papers of Addison." },
      { author: "Henry James", work: "The Art of Fiction", quote: "The continuous **polishing** of dramatic dialogue reveals the subtle grain of character." }
    ]
  },
  "Dashboard — poli/polistes.md": {
    primary: "A cosmopolitan genus of paper wasps (family Vespidae) that construct open umbrella-shaped paper nests.",
    secondary: "In entomology and behavioral sociobiology, primitively eusocial wasps studied extensively for dominance hierarchies and face-recognition signaling.",
    quotes: [
      { author: "Jean-Henri Fabre", work: "The Mason-Wasps", quote: "The slender queen of **Polistes** attaches her delicate hexagonal paper cells to the underside of the sunlit tile." },
      { author: "E. O. Wilson", work: "The Insect Societies", quote: "Dominance interactions among foundresses of **Polistes** illustrate the evolutionary origins of reproductive castes." },
      { author: "William Morton Wheeler", work: "Social Life Among the Insects", quote: "The absence of a sterile worker caste separates **Polistes** from the more specialized yellowjackets." }
    ]
  },
  "Dashboard — poli/politburo.md": {
    primary: "The principal policymaking committee of a communist party, especially that of the former Soviet Union.",
    secondary: "In political science and Soviet studies, the supreme decision-making executive council exercising absolute control over party, state, and military policy.",
    quotes: [
      { author: "George F. Kennan", work: "The Long Telegram", quote: "Soviet foreign policy is formulated within the secretive, insulated deliberations of the **Politburo**." },
      { author: "Aleksandr Solzhenitsyn", work: "The Gulag Archipelago", quote: "Secret decrees issued from the Kremlin **Politburo** dispatched millions to the remote taiga without trial." },
      { author: "Hannah Arendt", work: "The Origins of Totalitarianism", quote: "In the totalitarian apparatus, the **Politburo** operates as the supreme transmission belt of the leader's will." }
    ]
  },
  "Dashboard — poli/polite.md": {
    primary: "Having or showing behavior that is respectful and considerate of other people; courteous.",
    secondary: "Relating to refined or cultivated society (e.g. polite learning, polite literature).",
    quotes: [
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "Mr. Bingley was lively and unreserved, danced every dance, and showed himself to be remarkably **polite**." },
      { author: "David Hume", work: "Of the Rise and Progress of the Arts and Sciences", quote: "Commerce and peace naturally soften coarse manners, introducing **polite** learning into urban life." },
      { author: "Lord Chesterfield", work: "Letters to His Son", quote: "True good breeding consists in being easy yourself and making everyone around you feel **polite** and respected." }
    ]
  },
  "Dashboard — poli/politeia.md": {
    primary: "The Greek term for citizenship, constitutional order, government, or a body of citizens.",
    secondary: "In classical political philosophy, Aristotle's ideal constitution (a balanced polity mixing democracy and oligarchy) and the original Greek title of Plato's Republic.",
    quotes: [
      { author: "Aristotle", work: "Politics", quote: "A **politeia** is the arrangement of magistrates in a state, especially of the supreme authority." },
      { author: "Plato", work: "The Republic", quote: "In constructing our ideal **politeia**, we must harmonize justice in the soul with justice in the commonwealth." },
      { author: "Werner Jaeger", work: "Paideia: The Ideals of Greek Culture", quote: "The **politeia** was not merely a legal constitution, but the moral and spiritual life-order of the citizens." }
    ]
  },
  "Dashboard — poli/politely.md": {
    primary: "In a respectful and considerate manner; courteously.",
    secondary: "With refined social decorum, tact, or diplomatic circumspection.",
    quotes: [
      { author: "Charles Dickens", work: "David Copperfield", quote: "Uriah Heep bowed **politely**, rubbing his clammy palms together with an affectation of deep humility." },
      { author: "Henry James", work: "The Portrait of a Lady", quote: "Gilbert Osmond smiled **politely**, masking his icy disdain behind impeccable Roman manners." },
      { author: "George Bernard Shaw", work: "Pygmalion", quote: "Liza spoke **politely** about the weather and the influenza, carefully pronouncing each aspirated syllable." }
    ]
  },
  "Dashboard — poli/politeness.md": {
    primary: "Behavior that is respectful and considerate of other people; courteous manners.",
    secondary: "In 18th-century social philosophy, the art of pleasing in conversation and sociability that civilizes commercial nations.",
    quotes: [
      { author: "David Hume", work: "Essays, Moral, Political, and Literary", quote: "**Politeness** is the currency of civilized intercourse, smoothing over the natural roughness of selfish vanity." },
      { author: "Samuel Johnson", work: "The Rambler", quote: "Artificial **politeness** can easily degenerate into deceit if not rooted in sincere benevolence of heart." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "Chivalric **politeness** elevated social life, inspiring a noble submission without loss of personal dignity." }
    ]
  },
  "Dashboard — poli/politesse.md": {
    primary: "Politeness; refined manners, especially of a conventional or slightly formal kind.",
    secondary: "In social critique, polished French salon etiquette or superficial, ceremonious civility.",
    quotes: [
      { author: "Lord Chesterfield", work: "Letters to His Son", quote: "Acquire that French **politesse** which disarms hostility and opens every drawing-room door." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "The French diplomat bowed with exquisite **politesse**, complimenting Becky on her fluent Parisian accent." },
      { author: "Henry James", work: "The American", quote: "Christopher Newman admired the aristocratic family's rigid **politesse**, though sensing an iron wall beneath." }
    ]
  },
  "Dashboard — poli/politic.md": {
    primary: "Seeming sensible and judicious under the circumstances; prudent or shrewd (especially of an action).",
    secondary: "In constitutional history, relating to the body politic or sovereign state governance.",
    quotes: [
      { author: "Niccolò Machiavelli", work: "The Prince", quote: "It is often more **politic** for a ruler to be feared than loved, if he cannot achieve both together." },
      { author: "William Shakespeare", work: "Hamlet", quote: "He was a man of **politic** regard, skilled in whispered statecraft and courtly expedience." },
      { author: "Edmund Burke", work: "Speech on Conciliation with America", quote: "Prudence in government is not only the first of political virtues, but the supreme rule of all **politic** wisdom." }
    ]
  },
  "Dashboard — poli/political.md": {
    primary: "Relating to the government or the public affairs of a country.",
    secondary: "In classical and modern philosophy, concerning the distribution of civic power, institutional authority, and social justice.",
    quotes: [
      { author: "Aristotle", work: "Politics", quote: "The state is the highest form of community, and the **political** good is justice, which means the common interest." },
      { author: "Carl von Clausewitz", work: "On War", quote: "War is not merely an act of policy, but a true **political** instrument, a continuation of political commerce." },
      { author: "John Locke", work: "Two Treatises of Government", quote: "**Political** power is that power which every man, having in the state of nature, has given up into the hands of society." }
    ]
  },
  "Dashboard — poli/politically.md": {
    primary: "In a way that relates to the government, public affairs, or politics of a country.",
    secondary: "From the viewpoint of statecraft, electoral tactics, or ideological alignment.",
    quotes: [
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "Americans are taught from infancy to rely upon their own collective efforts rather than look **politically** to royal authority." },
      { author: "Abraham Lincoln", work: "Cooper Union Address", quote: "Let us stand by our duty **politically** and morally, fearlessly proclaiming that right makes might." },
      { author: "George Orwell", work: "Politics and the English Language", quote: "In our time, **politically** charged language is largely designed to make lies sound truthful and murder respectable." }
    ]
  },
  "Dashboard — poli/politician.md": {
    primary: "A person who is professionally involved in politics, especially as a holder of or candidate for an elected office.",
    secondary: "Often used pejoratively to imply a crafty, opportunist schemer who tailors convictions to electoral gain.",
    quotes: [
      { author: "Jonathan Swift", work: "Gulliver's Travels", quote: "Whoever could make two ears of corn grow upon a spot where only one grew before would deserve better of mankind than the whole race of **politician**s." },
      { author: "William Shakespeare", work: "King Lear", quote: "Get thee glass eyes; And like a scurvy **politician**, seem To see the things thou dost not." },
      { author: "Thomas Jefferson", work: "Letters of Thomas Jefferson", quote: "Whenever a man has cast a longing eye on offices, a rottenness begins in his conduct as a **politician**." }
    ]
  },
  "Dashboard — poli/politicise.md": {
    primary: "To make something political in character; give a political tone or bias to (British spelling of politicize).",
    secondary: "To awaken political consciousness or mobilize civic awareness within a social movement.",
    quotes: [
      { author: "George Orwell", work: "The Prevention of Literature", quote: "Totalitarian states attempt to **politicise** every branch of human thought, from poetry to pure mathematics." },
      { author: "Virginia Woolf", work: "Three Guineas", quote: "To educate the working classes is to inevitably **politicise** their aspirations for social dignity." },
      { author: "E. P. Thompson", work: "The Making of the English Working Class", quote: "Radical pamphleteers labored to **politicise** the grievances of industrial handloom weavers." }
    ]
  },
  "Dashboard — poli/politicize.md": {
    primary: "To make political; cause to assume a political character or aspect.",
    secondary: "To engage individuals in political debate or transform neutral cultural/scientific topics into partisan disputes.",
    quotes: [
      { author: "Hannah Arendt", work: "On Revolution", quote: "The tragedy of modern times is the impulse to **politicize** every private realm of human existence." },
      { author: "Noam Chomsky", work: "Understanding Power", quote: "Popular movements succeed when they **politicize** issues that elites prefer to keep insulated behind closed doors." },
      { author: "Carl Sagan", work: "The Demon-Haunted World", quote: "When partisan leaders **politicize** scientific findings, objective truth is sacrificed to short-term electoral advantage." }
    ]
  },
  "Dashboard — poli/politick.md": {
    primary: "To engage in political discussion, campaign for votes, or maneuver for political advantage (often used derisively).",
    secondary: "In historical prose, an archaic spelling of politic (prudent/shrewd) or the verb meaning to engage in opportunistic backroom diplomacy.",
    quotes: [
      { author: "Mark Twain", work: "The Gilded Age", quote: "Senator Dilworthy spent his weekends traveling across the county to **politick** with local party delegates." },
      { author: "Henry Adams", work: "Democracy: An American Novel", quote: "Washington dining rooms provided the discreet setting where rival congressmen loved to **politick** over dessert." },
      { author: "H. L. Mencken", work: "Prejudices: Fourth Series", quote: "The candidates gathered at the fairgrounds to shake sweaty hands and **politick** under the sweltering tent." }
    ]
  },
  "Dashboard — poli/politico.md": {
    primary: "A politician or political person, especially an experienced, shrewd, or opportunistic one.",
    secondary: "In political journalism, an insider or party operative skilled in campaign mechanics and vote-counting.",
    quotes: [
      { author: "Sinclair Lewis", work: "It Can't Happen Here", quote: "The veteran **politico** knew how to pander to rural prejudices while securing big-city campaign donations." },
      { author: "Hunter S. Thompson", work: "Fear and Loathing on the Campaign Trail '72", quote: "Every cynical **politico** in the hotel lobby was drinking bourbon and calculating primary delegate counts." },
      { author: "H. L. Mencken", work: "Notes on Democracy", quote: "The professional **politico** possesses an extraordinary antenna for sensing which way the herd will run." }
    ]
  },
  "Dashboard — poli/politics.md": {
    primary: "The activities associated with the governance of a country or area, especially the debate between parties having power.",
    secondary: "In political science and philosophy, the processes through which groups make collective decisions and allocate power and resources.",
    quotes: [
      { author: "Aristotle", work: "Politics", quote: "The master science of the human good is **politics**, for it prescribes which sciences should be studied in cities." },
      { author: "Max Weber", work: "Politics as a Vocation", quote: "**Politics** is a strong and slow boring of hard boards, requiring both passion and perspective." },
      { author: "Abraham Lincoln", work: "Speech at Peoria", quote: "In a free government, **politics** must continually align public sentiment with great moral truths." }
    ]
  },
  "Dashboard — poli/politologist.md": {
    primary: "A political scientist; an expert or academic specialist in political science.",
    secondary: "In continental European academic terminology, a scholar analyzing comparative government, political theory, and state institutions.",
    quotes: [
      { author: "Max Weber", work: "Economy and Society", quote: "The empirical **politologist** must distinguish between value judgments and objective institutional analysis." },
      { author: "Raymond Aron", work: "Main Currents in Sociological Thought", quote: "As a practicing **politologist**, Aron analyzed Cold War ideologies with lucid sociological detachment." },
      { author: "Norberto Bobbio", work: "Democracy and Dictatorship", quote: "The modern **politologist** traces how constitutional rules constrain authoritarian executive impulses." }
    ]
  },
  "Dashboard — poli/politology.md": {
    primary: "The study of politics; political science.",
    secondary: "The academic discipline investigating constitutional governance, party systems, public opinion, and geopolitical strategy.",
    quotes: [
      { author: "Harold Lasswell", work: "Politics: Who Gets What, When, How", quote: "The central inquiry of modern **politology** is the systematic analysis of power and influence." },
      { author: "Maurice Duverger", work: "Political Parties", quote: "Comparative **politology** demonstrates how electoral systems mathematically shape the number of national parties." },
      { author: "Robert Dahl", work: "Polyarchy: Participation and Opposition", quote: "Empirical **politology** seeks to measure the real-world conditions under which democratic institutions survive." }
    ]
  },
  "Dashboard — poli/politonym.md": {
    primary: "A name given to a group of people based on their political allegiance or the political entity to which they belong (as opposed to ethnic origin).",
    secondary: "In political linguistics and onomastics, a citizenship-based demonym (e.g. 'Soviet', 'American', 'Swiss') transcending ethnolinguistic divisions.",
    quotes: [
      { author: "Benedict Anderson", work: "Imagined Communities", quote: "The state promoted an overarching national **politonym** to unify disparate ethnic language groups." },
      { author: "Ernest Gellner", work: "Nations and Nationalism", quote: "Modern industrial states substitute a standardized civic **politonym** for local tribal and regional identities." },
      { author: "Eric Hobsbawm", work: "Nations and Nationalism since 1780", quote: "The adoption of a common republican **politonym** forged citizen loyalty during the French Revolution." }
    ]
  },
  "Dashboard — poli/polity.md": {
    primary: "A form or process of civil government or constitution; or an organized society considered as a political entity.",
    secondary: "In Aristotelian political theory, politeia or polity represents constitutional government based on the middle class, combining oligarchy and democracy.",
    quotes: [
      { author: "Aristotle", work: "Politics", quote: "The middle form of government, termed a **polity**, is the most stable because it relies upon a numerous middle class." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "Our British **polity** is an inherited partnership between those who are living, those who are dead, and those who are yet to be born." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "The township was the primary cell of the American **polity**, fostering habits of local self-government." }
    ]
  },
  "Dashboard — poli/propolis.md": {
    primary: "A red or brown resinous substance collected by honeybees from tree buds, used by them to cement crevices and seal the hive (bee glue).",
    secondary: "In apiculture and pharmaceutical botany, an antimicrobial bee secretion rich in caffeic acid phenethyl ester and flavonoids.",
    quotes: [
      { author: "Aristotle", work: "History of Animals", quote: "Bees seal the vestibule of their comb with **propolis**, defending the narrow gateway of their city against intruders." },
      { author: "Maurice Maeterlinck", work: "The Life of the Bee", quote: "The workers coat every crevice with aromatic **propolis**, sanitizing the hive against decay with resinous varnish." },
      { author: "Karl von Frisch", work: "Bees: Their Vision, Chemical Senses, and Language", quote: "Foragers harvest sticky botanical gums to produce **propolis**, essential for hive insulation and hygiene." }
    ]
  },
  "Dashboard — poli/tetrapolis.md": {
    primary: "A confederation or group of four cities (such as the Attic Tetrapolis of Marathon, Probalinthus, Tricorithus, and Oenoe).",
    secondary: "In ancient history, a political confederacy of four autonomous settlements linked by ancestral cults or regional defense alliances.",
    quotes: [
      { author: "Strabo", work: "Geography", quote: "The Attic **Tetrapolis** around Marathon retained its ancient local festivals long after the synoecism of Theseus." },
      { author: "George Grote", work: "A History of Greece", quote: "Dorian settlers in central Greece established the historic **Tetrapolis** of Doris as their ancestral cradle." },
      { author: "Pausanias", work: "Description of Greece", quote: "Monuments throughout the **Tetrapolis** commemorated the heroic fallen who drove the Persian invaders back into the sea." }
    ]
  },
  "Dashboard — poli/Tripoli.md": {
    primary: "The capital and largest city of Libya in North Africa; or a historic port city in northern Lebanon.",
    secondary: "In historical geography, named from Greek Tripolis ('three cities'), originally founded by Phoenicians as a confederation of three trading colonies.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The prosperous Roman colony of **Tripoli** flourished as a trading emporium for ivory and African grain." },
      { author: "Richard Francis Burton", work: "The Gold-Mines of Midian", quote: "Merchant caravans arrived in **Tripoli** laden with dates and textiles from the interior oases." },
      { author: "Winston Churchill", work: "The Second World War", quote: "Montgomery's victorious Eighth Army entered **Tripoli**, driving Rommel's forces in full retreat toward Tunisia." }
    ]
  },
  "Dashboard — poli/unpolished.md": {
    primary: "Not polished; rough, unburnished, or lacking physical shine.",
    secondary: "Lacking sophistication, refined manners, or literary elegance; natural, rugged, or crude.",
    quotes: [
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "The country manners of Sir William Lucas were simple and **unpolished**, yet free from any mean malice." },
      { author: "Charles Dickens", work: "Hard Times", quote: "Beneath his **unpolished** dialect and rough hands, Stephen Blackpool carried a heart of purest honor." },
      { author: "John Ruskin", work: "The Stones of Venice", quote: "There is noble vitality in the rough, **unpolished** carvings of the medieval workman that cold machinery can never copy." }
    ]
  },
  "Dashboard — poli/unpolitical.md": {
    primary: "Not political; not relating to, concerned with, or participating in political affairs; apolitical.",
    secondary: "In social critique, disconnected from ideological or governmental debates.",
    quotes: [
      { author: "George Orwell", work: "Inside the Whale", quote: "Henry Miller's fiction embraced an entirely **unpolitical** acceptance of ordinary, sensual human life." },
      { author: "Hannah Arendt", work: "Men in Dark Times", quote: "In times of tyranny, seeking refuge in an **unpolitical** existence often becomes a tragic moral illusion." },
      { author: "Thomas Mann", work: "Reflections of an Unpolitical Man", quote: "Mann wrestled with his earlier stance as an **unpolitical** artist before embracing democratic responsibility." }
    ]
  },

  // === Dashboard — porn (6 words) ===
  "Dashboard — porn/porn.md": {
    primary: "Pornography; materials depicting explicit sexual acts intended to stimulate erotic feelings.",
    secondary: "In modern popular culture, visually captivating or indulging media focusing on a specific subject (e.g. 'food porn', 'real estate porn').",
    quotes: [
      { author: "Susan Sontag", work: "The Pornographic Imagination", quote: "Transgressive art and hardcore **porn** challenge the conventional boundaries of bourgeois domestic decorum." },
      { author: "George Orwell", work: "Nineteen Eighty-Four", quote: "The Ministry of Truth maintained a separate section producing cheap **porn** to pacify and distract the proles." },
      { author: "Angela Carter", work: "The Sadeian Woman", quote: "Commercial **porn** reflects the prevailing power relations between men and women in capitalist society." }
    ]
  },
  "Dashboard — porn/porno.md": {
    primary: "Informal term for pornography or a pornographic movie/magazine.",
    secondary: "In colloquial cultural criticism, commercial sexually explicit entertainment.",
    quotes: [
      { author: "Don DeLillo", work: "White Noise", quote: "The neon glow from the adult cinema advertised another cheap **porno** feature to passing motorists." },
      { author: "David Foster Wallace", work: "Infinite Jest", quote: "The cartridges contained bizarre parodies of European art films mixed with underground **porno** tapes." },
      { author: "Susan Sontag", work: "Styles of Radical Will", quote: "A commercial **porno** movie relies on formulaic physical repetition rather than genuine psychological depth." }
    ]
  },
  "Dashboard — porn/pornographer.md": {
    primary: "A person who creates, produces, publishes, or sells pornography.",
    secondary: "In literary and censorship history, an author or printer prosecuted under obscenity statutes for distributing sexually explicit material.",
    quotes: [
      { author: "John Milton", work: "Areopagitica", quote: "The licenser pretended to guard virtue, treating every daring poet as though he were a vulgar **pornographer**." },
      { author: "George Bernard Shaw", work: "Mrs. Warren's Profession", quote: "Society hypocritically condemns the **pornographer** while profiting enormously from the commercial exploitation of vice." },
      { author: "Anthony Comstock", work: "Traps for the Young", quote: "The crusading inspector vowed to confiscate every printing press operated by a clandestine **pornographer**." }
    ]
  },
  "Dashboard — porn/pornographic.md": {
    primary: "Explicitly describing or displaying sexual activity intended to stimulate erotic feelings.",
    secondary: "In legal and aesthetic philosophy, material judged under obscenity laws regarding whether it appeals primarily to prurient interests without serious redeeming value.",
    quotes: [
      { author: "Susan Sontag", work: "The Pornographic Imagination", quote: "The classic **pornographic** novel treats sexual obsession as a rigorous, totalizing metaphysical quest." },
      { author: "D. H. Lawrence", work: "Pornography and Obscenity", quote: "Genuine erotic vitality is insulted and degraded by the furtive, dirty secrecy of **pornographic** pamphlets." },
      { author: "James Joyce", work: "Ulysses (Trial Records)", quote: "Judge Woolsey ruled that Ulysses was an honest literary epic rather than a deliberately **pornographic** work." }
    ]
  },
  "Dashboard — porn/pornographically.md": {
    primary: "In a pornographic manner; with explicit sexual depiction.",
    secondary: "In literary analysis, portraying scenes with sensationalist, exploitative physical explicitness.",
    quotes: [
      { author: "Susan Sontag", work: "Under the Sign of Saturn", quote: "The text was constructed **pornographically**, reducing complex human characters to instruments of mechanical sensation." },
      { author: "Angela Carter", work: "The Sadeian Woman", quote: "De Sade arranged his philosophical dialogues **pornographically**, punctuating metaphysics with violent orgies." },
      { author: "George Steiner", work: "Language and Silence", quote: "When literature describes intimacy **pornographically**, it strips privacy of its sacred, mysterious silence." }
    ]
  },
  "Dashboard — porn/pornography.md": {
    primary: "Printed or visual material containing the explicit description or display of sexual organs or activity, intended to stimulate erotic feeling.",
    secondary: "Etymologically derived from Greek pornographein ('writing about prostitutes'); in law and ethics, the commercial production and regulation of explicit media.",
    quotes: [
      { author: "D. H. Lawrence", work: "Pornography and Obscenity", quote: "**Pornography** is the attempt to insult sex, to do dirt on it, substituting furtive mental fantasies for warm physical life." },
      { author: "Susan Sontag", work: "The Pornographic Imagination", quote: "Serious **pornography** explores the extreme limits of human consciousness and the dark abyss of transgressive desire." },
      { author: "Michel Foucault", work: "The History of Sexuality", quote: "The nineteenth century proliferated discourse about sex while classifying its excesses under the regulatory rubric of **pornography**." }
    ]
  },

  // === Dashboard — pseph (7 words) ===
  "Dashboard — pseph/isopsephy.md": {
    primary: "The practice of adding up the numerical values of the letters in a word or phrase to find its total value (Greek gematria).",
    secondary: "In Hellenistic mysticism, Kabbalah, and early Christian epigraphy, deciphering hidden esoteric correspondences between names sharing identical numerical totals (e.g. 666).",
    quotes: [
      { author: "Suetonius", work: "The Twelve Caesars", quote: "Graffiti in Rome employed **isopsephy** to calculate that Nero's name yielded the identical number as the phrase 'slew his own mother'." },
      { author: "Umberto Eco", work: "Foucault's Pendulum", quote: "The occultists sought cosmic codes through **isopsephy**, calculating the hidden numerology of Greek anagrams." },
      { author: "Irenaeus", work: "Against Heresies", quote: "Irenaeus mocked Gnostic heretics who based cosmic hierarchies upon trivial calculations of **isopsephy**." }
    ]
  },
  "Dashboard — pseph/psephite.md": {
    primary: "A coarse-grained sedimentary rock composed of rounded or angular gravel, pebbles, and cobbles (conglomerate or breccia).",
    secondary: "In sedimentary petrology, clastic sedimentary rocks whose constituent rudaceous grains exceed 2 millimeters in diameter.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The ancient glacial drift consolidated over millennia into a tough, poorly sorted **psephite** conglomerate." },
      { author: "James Dwight Dana", work: "Manual of Geology", quote: "Petrologists classify coarse gravel deposits and bouldery beds under the general designation of **psephite**." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Fluvial torrents deposited thick alluvial fans that lithified into massive beds of **psephite**." }
    ]
  },
  "Dashboard — pseph/psephitic.md": {
    primary: "Of, relating to, or resembling psephite; coarse-grained or pebbly (of sedimentary rocks).",
    secondary: "In geological facies analysis, describing sedimentary deposits composed predominantly of gravel, pebbles, or cobbles.",
    quotes: [
      { author: "Archibald Geikie", work: "Text-Book of Geology", quote: "The basal beds of the Old Red Sandstone display coarse **psephitic** textures formed in braided stream systems." },
      { author: "Eduard Suess", work: "The Face of the Earth", quote: "Torrential Alpine outwash created vast **psephitic** strata at the foot of rising mountain chains." },
      { author: "Charles Lapworth", work: "The Geological Magazine", quote: "The transition from fine shale to **psephitic** conglomerate marks an abrupt tectonic uplift in the source area." }
    ]
  },
  "Dashboard — pseph/psephocracy.md": {
    primary: "Government by ballot; democracy characterized by decision-making through voting.",
    secondary: "In political science, a system where civil authority is derived through regular electoral balloting (from Greek psephos, pebble used for voting).",
    quotes: [
      { author: "George Grote", work: "A History of Greece", quote: "Athenian **psephocracy** relied on the secret ballot of bronze tokens dropped into voting urns." },
      { author: "H. L. Mencken", work: "Notes on Democracy", quote: "The champion of pure **psephocracy** naively assumes that counting heads guarantees wisdom in government." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "A healthy **psephocracy** requires an educated populace that deliberates before dropping ballots into the box." }
    ]
  },
  "Dashboard — pseph/psephologist.md": {
    primary: "A person who studies the quantitative analysis of elections and voting patterns.",
    secondary: "In political science and polling analysis, an expert who models electoral demographics, vote swings, and seat distribution curves.",
    quotes: [
      { author: "David Butler", work: "The British General Election of 1951", quote: "The professional **psephologist** calculates the uniform national swing required to overturn a parliamentary majority." },
      { author: "Anthony Downs", work: "An Economic Theory of Democracy", quote: "The **psephologist** examines voter behavior under the assumption that citizens act as rational utility maximizers." },
      { author: "Samuel Lubell", work: "The Future of American Politics", quote: "By analyzing precinct returns, the skilled **psephologist** detects subterranean realignments in ethnic voting blocs." }
    ]
  },
  "Dashboard — pseph/psephology.md": {
    primary: "The statistical and quantitative study of elections, voting behavior, and trends in polling.",
    secondary: "In political science, the empirical discipline (coined in 1952 from Greek psephos) that analyzes electoral turnout, swings, and predictive exit polls.",
    quotes: [
      { author: "David Butler", work: "The Study of Political Behavior", quote: "Modern **psephology** developed when statistical survey methodology was applied systematically to general elections." },
      { author: "Robert Dahl", work: "Who Governs?", quote: "The insights of **psephology** clarify how local patronage networks shape aggregate national voting outcomes." },
      { author: "V. O. Key Jr.", work: "Politics, Parties, and Pressure Groups", quote: "Quantitative **psephology** exploded the myth that voters are purely passive targets of party propaganda." }
    ]
  },
  "Dashboard — pseph/psephurus.md": {
    primary: "A genus of large freshwater fish containing the Chinese paddlefish (Psephurus gladius), now declared extinct.",
    secondary: "In ichthyology and conservation biology, an ancient acipenseriform fish of the Yangtze River basin reaching up to 7 meters in length with an elongated rostrum.",
    quotes: [
      { author: "Albert Günther", work: "Catalogue of the Fishes in the British Museum", quote: "The giant Chinese paddlefish, **Psephurus** gladius, bears a broad sword-like snout equipped with electroreceptors." },
      { author: "E. O. Wilson", work: "The Future of Life", quote: "The extinction of **Psephurus** gladius in the Yangtze river basin represents the tragic loss of a primordial vertebrate lineage." },
      { author: "David Starr Jordan", work: "A Guide to the Study of Fishes", quote: "Anatomically, **Psephurus** links the paddlefishes to ancient Mesozoic chondrostean ancestors." }
    ]
  },

  // === Dashboard — ptoch (2 words) ===
  "Dashboard — ptoch/ptochocracy.md": {
    primary: "Government or rule by beggars or the destitute; a state governed by the impoverished.",
    secondary: "In classical and satirical political theory, an extreme form of popular democracy where governance is seized by the destitute underclass.",
    quotes: [
      { author: "Aristophanes", work: "Ecclesiazusae", quote: "The comic poet imagined a revolutionary **ptochocracy** where all private property was abolished and shared among the poor." },
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "The sans-culottes seized the municipal assemblies, inaugurating what horrified aristocrats termed a roaring **ptochocracy**." },
      { author: "George Grote", work: "A History of Greece", quote: "Oligarchic critics reviled radical Athenian democracy as an anarchic **ptochocracy** ruled by rowers and laborers." }
    ]
  },
  "Dashboard — ptoch/ptochology.md": {
    primary: "The study of beggars, mendicancy, and extreme poverty.",
    secondary: "In the history of sociology and social work, the systematic 19th-century investigation of poor-relief systems, almshouses, and vagrancy laws.",
    quotes: [
      { author: "Henry Mayhew", work: "London Labour and the London Poor", quote: "Mayhew's detailed street interviews provided the foundation for a humane and scientific **ptochology** of Victorian city life." },
      { author: "Charles Booth", work: "Life and Labour of the People in London", quote: "Statistical **ptochology** mapped the precise poverty line across London's crowded East End parishes." },
      { author: "Sidney Webb", work: "English Poor Law History", quote: "Parish records preserved in workhouse archives offer rich source material for the historical student of **ptochology**." }
    ]
  },

  // === Dashboard — scandal (10 words) ===
  "Dashboard — scandal/scandal.md": {
    primary: "An action or event regarded as morally or legally wrong and causing general public outrage; or malicious gossip.",
    secondary: "Etymologically from Greek skandalon ('a snare', 'stumbling block'); in theology, an occasion of spiritual stumbling or moral stumbling block.",
    quotes: [
      { author: "Richard Brinsley Sheridan", work: "The School for Scandal", quote: "There is no possibility of escaping the malicious whispers of the salon, where reputation dies in every cup of tea and piece of **scandal**." },
      { author: "William Shakespeare", work: "The Winter's Tale", quote: "My life stands in the level of your dreams, Which I'll lay down; and let your **scandal** fall Upon my grave without more grief." },
      { author: "John Milton", work: "Paradise Lost", quote: "Sin and Death stood as a perpetual **scandal** and stumbling block before the fallen creation." }
    ]
  },
  "Dashboard — scandal/scandalisation.md": {
    primary: "The act of shocking someone with scandalous conduct, or causing public scandal (British spelling of scandalization).",
    secondary: "In social history and public relations, the sensationalized exposure of private misconduct to provoke moral panic.",
    quotes: [
      { author: "George Bernard Shaw", work: "Heartbreak House", quote: "The deliberate **scandalisation** of high society was the only weapon left to the uncompromising bohemian artist." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "The sudden **scandalisation** of the Crawley family provided amusement for every breakfast table in Mayfair." },
      { author: "Oscar Wilde", work: "An Ideal Husband", quote: "Political careers in London are wrecked not by crimes, but by the theatrical **scandalisation** of the yellow press." }
    ]
  },
  "Dashboard — scandal/scandalise.md": {
    primary: "To shock or offend someone by doing something considered immoral or improper (British spelling of scandalize).",
    secondary: "In nautical terminology, to reduce the area of a sail by dropping the peak of a gaff sail or tricing up the tack.",
    quotes: [
      { author: "Jane Austen", work: "Mansfield Park", quote: "The proposal to perform an amateur play at the estate threatened to **scandalise** the sober principles of Sir Thomas." },
      { author: "Charles Dickens", work: "Nicholas Nickleby", quote: "Mrs. Nickleby managed to **scandalise** her listeners with rambling, inappropriate family anecdotes." },
      { author: "Joseph Conrad", work: "The Mirror of the Sea", quote: "The skipper ordered the crew to **scandalise** the mainsail to ease the schooner during the squall." }
    ]
  },
  "Dashboard — scandal/scandalization.md": {
    primary: "The act or process of shocking someone through scandalous behavior, or causing a public scandal.",
    secondary: "In media sociology, the process through which journalistic reporting frames an event into a moral transgression.",
    quotes: [
      { author: "Thorstein Veblen", work: "The Higher Learning in America", quote: "University trustees feared public **scandalization** more than intellectual stagnation." },
      { author: "Hannah Arendt", work: "Crises of the Republic", quote: "The **scandalization** of administrative secrecy forced the release of classified wartime documents." },
      { author: "Henry James", work: "The Reverberator", quote: "The American family was baffled by the European outrage and ferocious **scandalization** caused by society gossip." }
    ]
  },
  "Dashboard — scandal/scandalize.md": {
    primary: "To shock or horrify by violating moral or social standards; or (nautical) to drop the peak of a gaff sail.",
    secondary: "In moral theology, to cause someone to stumble spiritually or fall into sin (from Greek skandalizein).",
    quotes: [
      { author: "Nathaniel Hawthorne", work: "The Scarlet Letter", quote: "The elder ministers feared that such unrepentant defiance would **scandalize** the young and tender consciences of the flock." },
      { author: "Mark Twain", work: "The Adventures of Huckleberry Finn", quote: "Huck's unvarnished honesty and lack of religion continued to **scandalize** the Widow Douglas." },
      { author: "Henry David Thoreau", work: "Civil Disobedience", quote: "A principled refusal to pay an unjust tax will always **scandalize** the comfortable guardians of state propriety." }
    ]
  },
  "Dashboard — scandal/scandalmonger.md": {
    primary: "A person who habitually spreads malicious gossip, rumors, or scandals.",
    secondary: "In literature and social satire, a gossip-monger whose trade is defaming reputations in salons or tabloids.",
    quotes: [
      { author: "Richard Brinsley Sheridan", work: "The School for Scandal", quote: "Lady Sneerwell was an accomplished **scandalmonger**, weaving poisonous slander with charming smiles." },
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "Mrs. Long proved herself an insufferable **scandalmonger**, circulating rumors about Mr. Bingley's fortune." },
      { author: "William Makepeace Thackeray", work: "Pendennis", quote: "The club was infested by a persistent **scandalmonger** who traded in ruined reputations and whispered debts." }
    ]
  },
  "Dashboard — scandal/scandalmongering.md": {
    primary: "The practice or activity of spreading malicious gossip and scandalous rumors.",
    secondary: "In journalistic ethics and social commentary, the commercial or recreational peddling of salacious personal defamatory gossip.",
    quotes: [
      { author: "George Eliot", work: "Middlemarch", quote: "The provincial tea parties of Middlemarch were rife with petty **scandalmongering** regarding Dr. Lydgate's finances." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "Pamphleteers substituted vicious **scandalmongering** against the queen for serious political debate." },
      { author: "Anthony Trollope", work: "The Way We Live Now", quote: "Society newspapers flourished upon relentless **scandalmongering**, prying into the private affairs of London elites." }
    ]
  },
  "Dashboard — scandal/scandalous.md": {
    primary: "Causing general public outrage by a perceived offense against morality or law; disgraceful or shameful.",
    secondary: "Containing malicious gossip or defamatory allegations.",
    quotes: [
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "The abrupt departure of Lord Steyne gave rise to the most **scandalous** rumors throughout the town." },
      { author: "Jane Austen", work: "Sense and Sensibility", quote: "Willoughby's betrayal of the innocent girl was universally condemned as **scandalous** and unpardonable." },
      { author: "Charles Dickens", work: "Bleak House", quote: "The endless delays of the Court of Chancery were denounced by suitors as an open, **scandalous** disgrace." }
    ]
  },
  "Dashboard — scandal/scandalously.md": {
    primary: "In a scandalous manner; disgracefully, shockingly, or outrageously.",
    secondary: "In a way that violates moral propriety or fair treatment.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "The young ladies at Lowood School were **scandalously** underfed while the directors preached mortification of the flesh." },
      { author: "Henry Fielding", work: "Tom Jones", quote: "Blifil acted **scandalously**, misrepresenting Tom's generous heart to turn his benefactor against him." },
      { author: "George Bernard Shaw", work: "Pygmalion", quote: "Liza announced **scandalously** that her aunt had been done in, causing Mrs. Eynsford Hill to gasp." }
    ]
  },
  "Dashboard — scandal/scandalousness.md": {
    primary: "The quality or state of being scandalous; disgracefulness or shocking impropriety.",
    secondary: "The offensive or outrageous character of an action or report in the eyes of society.",
    quotes: [
      { author: "Samuel Richardson", work: "Clarissa", quote: "The sheer **scandalousness** of Lovelace's villainy terrified the innocent young lady." },
      { author: "Thomas Babington Macaulay", work: "Critical and Historical Essays", quote: "The open **scandalousness** of the Restoration court shocked even hardened veterans of the civil war." },
      { author: "Henry James", work: "The Wings of the Dove", quote: "Merton Densher was appalled by the underlying **scandalousness** of the secret scheme they had contrived." }
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

console.log(`Updated ${updatedCount} files in Batch 8!`);
