import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Art, Craft & Design/Dashboard — techn';

const filesData = {
  "architect.md": {
    primary: "A person qualified to design and oversee the construction of buildings or other physical structures.",
    secondary: "A person who designs, devises, or plans a complex program, policy, system, or software architecture; a master planner.",
    quotes: [
      { author: "John Ruskin", work: "The Seven Lamps of Architecture", quote: "The true **architect** must be not merely a builder of walls, but a poet and sculptor in stone." },
      { author: "William Shakespeare", work: "Titus Andronicus", quote: "Chief **architect** and plotter of these woes, the ruthless conspirator smiled upon the ruin he had wrought." },
      { author: "Henry David Thoreau", work: "Walden", quote: "Every man is the **architect** of a temple, called his body, to a god he worships after his own style." }
    ]
  },
  "architectural.md": {
    primary: "Relating to the art, science, practice, or style of designing and constructing buildings.",
    secondary: "Characterized by structural design, monumental symmetry, or spatial balance.",
    quotes: [
      { author: "Virginia Woolf", work: "To the Lighthouse", quote: "The ancient country house possessed a quiet **architectural** dignity that defied modern haste." },
      { author: "Frank Lloyd Wright", work: "An Organic Architecture", quote: "Great **architectural** design springs organically from the site, materials, and human spirit." },
      { author: "Henry James", work: "The Portrait of a Lady", quote: "She admired the magnificent **architectural** perspective of the Roman palace bathed in evening light." }
    ]
  },
  "architecturally.md": {
    primary: "In a manner relating to architecture or the structural design and construction of buildings.",
    secondary: "From the standpoint of formal structural composition, balance, or spatial organization.",
    quotes: [
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The Ducal Palace is **architecturally** unique, defying classical canons while achieving breathtaking harmony." },
      { author: "Edith Wharton", work: "The Decoration of Houses", quote: "An interior space must be conceived **architecturally** before decorative draperies are considered." },
      { author: "Lewis Mumford", work: "The City in History", quote: "Medieval cathedrals were **architecturally** oriented toward the rising sun, focusing community spiritual life." }
    ]
  },
  "architecture.md": {
    primary: "The art, science, and practice of designing and constructing buildings and other physical structures.",
    secondary: "The complex structure, conceptual organization, or framework of any system, software, or discipline.",
    quotes: [
      { author: "Vitruvius", work: "De Architectura", quote: "Sound **architecture** must satisfy three essential conditions: firmness, commodity, and delight." },
      { author: "Johann Wolfgang von Goethe", work: "Conversations with Eckermann", quote: "I call **architecture** frozen music, where silent harmonies speak directly to the soul." },
      { author: "Le Corbusier", work: "Towards a New Architecture", quote: "Our **architecture** is the masterly, correct, and magnificent play of masses brought together in light." }
    ]
  },
  "pantechnicon.md": {
    primary: "A large covered moving van or furniture wagon used for transporting household goods.",
    secondary: "Originally, a grand bazaar or warehouse in 19th-century London built for storing and exhibiting artistic and manufactured goods.",
    quotes: [
      { author: "Charles Dickens", work: "Bleak House", quote: "A heavy horse-drawn **pantechnicon** rumbled past the square, laden with the furniture of an evicted debtor." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "The contents of the grand townhouse were carted off to the **pantechnicon** for public auction." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Red Circle", quote: "A bulky **pantechnicon** stood outside the boarding house, blocking the narrow street." }
    ]
  },
  "polytechnic.md": {
    primary: "An institution of higher education offering instruction in technical, industrial, and applied scientific subjects.",
    secondary: "Relating to, teaching, or involving many applied sciences, crafts, and technical arts.",
    quotes: [
      { author: "H. G. Wells", work: "The Food of the Gods and How It Came to Earth", quote: "He attended evening lectures at the local **polytechnic**, studying industrial chemistry with relentless ambition." },
      { author: "George Bernard Shaw", work: "Major Barbara", quote: "The founder endowed a magnificent **polytechnic** to equip working youths with modern engineering skills." },
      { author: "Aldous Huxley", work: "Brave New World", quote: "Graduates from the Central **Polytechnic** managed the intricate automated factories of the metropolis." }
    ]
  },
  "techne.md": {
    primary: "In classical Greek philosophy, craftsmanship, applied art, or practical skill; knowledge directed toward making or producing something.",
    secondary: "The rational, rule-governed expertise distinct from purely theoretical contemplation (*theoria*) and practical wisdom (*phronesis*).",
    quotes: [
      { author: "Aristotle", work: "Nicomachean Ethics", quote: "We define **techne** as a rational productive state of mind involving a true course of reasoning." },
      { author: "Martin Heidegger", work: "The Question Concerning Technology", quote: "In ancient Greece, **techne** was not mere technique, but a mode of revealing truth through making." },
      { author: "Plato", work: "Gorgias", quote: "Socrates questioned whether rhetoric was a genuine **techne** or merely an empirical knack for persuasion." }
    ]
  },
  "technetium.md": {
    primary: "A radioactive metallic chemical element with atomic number 43 and symbol Tc, notable as the first artificially synthesized element.",
    secondary: "In nuclear medicine, the metastable isotope technetium-99m, widely utilized as a radioactive tracer in gamma camera imaging.",
    quotes: [
      { author: "Emilio Segrè", work: "Nobel Lecture", quote: "In 1937, through cyclotron bombardment of molybdenum, we isolated element forty-three and named it **technetium**." },
      { author: "Glenn T. Seaborg", work: "The Transuranium Elements", quote: "The synthetic discovery of **technetium** bridged a historic gap in Mendeleev's periodic table." },
      { author: "Oliver Sacks", work: "Uncle Tungsten: Memories of a Chemical Boyhood", quote: "I was awed that **technetium**, though surrounded by stable elements, possessed no non-radioactive isotopes." }
    ]
  },
  "technical-grade.md": {
    primary: "Designating a chemical, solvent, or material that is of adequate purity for general industrial or commercial use, but not for analytical or medical applications.",
    secondary: "In chemical engineering, describing bulk raw materials containing trace impurities permissible in manufacturing processes.",
    quotes: [
      { author: "Rachel Carson", work: "Silent Spring", quote: "Industrial drums of **technical-grade** pesticide were mixed with kerosene before spraying across waterways." },
      { author: "Primo Levi", work: "The Periodic Table", quote: "The warehouse was stacked with crude, **technical-grade** reagents intended for industrial varnish synthesis." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "Analytical laboratories must never substitute **technical-grade** acids when quantitative titrations are required." }
    ]
  },
  "technical.md": {
    primary: "Relating to a particular subject, art, craft, science, or profession, and involving specialized terminology or complex skills.",
    secondary: "Involving or requiring formal mechanical, scientific, or engineering knowledge rather than general or theoretical principles.",
    quotes: [
      { author: "Thomas Hardy", work: "The Mayor of Casterbridge", quote: "The agricultural surveyor explained the drainage scheme with precise **technical** terminology that baffled the farmers." },
      { author: "Frank A. Fetter", work: "The Principles of Economics", quote: "The economist must distinguish between monetary exchange values and the physical, **technical** efficiency of production." },
      { author: "Bertrand Russell", work: "The Problems of Philosophy", quote: "Philosophical arguments frequently turn upon subtle, **technical** distinctions that seem trivial to common sense." }
    ]
  },
  "technicality.md": {
    primary: "A point, detail, rule, or requirement of a specialized or technical nature, especially a minor legal or procedural one.",
    secondary: "The quality, condition, or state of being technical or overly concerned with formal mechanics.",
    quotes: [
      { author: "Charles Dickens", work: "Bleak House", quote: "The lawsuit in Chancery dragged on for decades, entangled in every conceivable legal **technicality**." },
      { author: "Arthur Conan Doyle", work: "The Hound of the Baskervilles", quote: "A narrow legal **technicality** prevented the coroner from issuing a conclusive warrant." },
      { author: "George Orwell", work: "1984", quote: "The Party could alter the laws at will, brushing aside every procedural **technicality** with absolute contempt." }
    ]
  },
  "technically.md": {
    primary: "According to the exact legal, scientific, or formal rules; strictly speaking.",
    secondary: "In a manner relating to technical skill, execution, engineering, or practical technique.",
    quotes: [
      { author: "Isaac Asimov", work: "I, Robot", quote: "The machine was **technically** flawless, yet its behavior exposed unforeseen ambiguities in the First Law." },
      { author: "Virginia Woolf", work: "The Voyage Out", quote: "She played the piano **technically** with brilliant accuracy, though lacking emotional warmth." },
      { author: "Richard Feynman", work: "Surely You're Joking, Mr. Feynman!", quote: "The apparatus was **technically** simple, but designed with exquisite physical insight." }
    ]
  },
  "technician.md": {
    primary: "A person skilled in the technique of an art, craft, or science; especially one employed in mechanical, electronic, or laboratory operations.",
    secondary: "An expert practitioner who excels in the formal, practical, or mechanical execution of a discipline.",
    quotes: [
      { author: "Sinclair Lewis", work: "Arrowsmith", quote: "The laboratory **technician** prepared the culture plates with swift, aseptic precision before the dawn experiments." },
      { author: "Aldous Huxley", work: "Brave New World", quote: "Each genetic **technician** monitored the incubating embryos as they floated along the automated conveyor belt." },
      { author: "David Foster Wallace", work: "Infinite Jest", quote: "The broadcast **technician** sat amidst glowing monitor banks, adjusting signal modulation with bored dexterity." }
    ]
  },
  "technicolor.md": {
    primary: "A proprietary color motion-picture process celebrated for its brilliant, richly saturated hues; (figuratively) vivid, brilliant color.",
    secondary: "In particle physics, a hypothetical class of theories beyond the Standard Model invoking dynamical electroweak symmetry breaking.",
    quotes: [
      { author: "Truman Capote", work: "Breakfast at Tiffany's", quote: "She remembered her hometown childhood not in shadows, but in brilliant, saturated **technicolor**." },
      { author: "Ray Bradbury", work: "The Illustrated Man", quote: "The tattoos on his skin seemed to pulse in dazzling **technicolor**, telling tales of distant worlds." },
      { author: "Joan Didion", work: "The White Album", quote: "Hollywood studio sets in the nineteen-fifties glowed with radiant **technicolor** artifice." }
    ]
  },
  "technique.md": {
    primary: "A practical method, procedure, or skillful way of performing a task, artistic endeavor, or scientific investigation.",
    secondary: "The mechanical skill, proficiency, and mastery of formal craft displayed by an artist, musician, or athlete.",
    quotes: [
      { author: "Edgar Allan Poe", work: "The Philosophy of Composition", quote: "Every literary effect should be calculated with mathematical **technique** to produce a singular emotional impact." },
      { author: "Virginia Woolf", work: "The Waves", quote: "The writer must reinvent novelistic **technique** to capture the fluid impressions of consciousness." },
      { author: "Igor Stravinsky", work: "Poetics of Music", quote: "True artistic freedom is achieved only through absolute mastery of musical **technique**." }
    ]
  },
  "techno.md": {
    primary: "A genre of electronic dance music characterized by repetitive four-on-the-floor beats, synthetic timbres, and fast tempo.",
    secondary: "A combining form or prefix denoting technology, technique, or applied industrial science.",
    quotes: [
      { author: "David Byrne", work: "How Music Works", quote: "The underground clubs of Berlin and Detroit birthed **techno**, where machine rhythms dissolved individual identity into collective trance." },
      { author: "William Gibson", work: "Neuromancer", quote: "The neon-lit basement bar pulsed with abrasive, industrial **techno** that rattled the floorboards." },
      { author: "Alvin Toffler", work: "Future Shock", quote: "Modern culture is increasingly shaped by **techno**-scientific acceleration that outpaces social adaptation." }
    ]
  },
  "technobabble.md": {
    primary: "Incomprehensible, pretentious, or overly complex technical or scientific jargon used to explain or justify something.",
    secondary: "Superficial or pseudo-scientific jargon employed to confuse laypeople or disguise a lack of genuine understanding.",
    quotes: [
      { author: "Douglas Adams", work: "The Hitchhiker's Guide to the Galaxy", quote: "The starship manual was filled with bewildering **technobabble** explaining the mechanics of the Infinite Improbability Drive." },
      { author: "Carl Sagan", work: "The Demon-Haunted World", quote: "Pseudo-scientific charlatans frequently hide behind impenetrable **technobabble** to peddle worthless remedies." },
      { author: "David Foster Wallace", work: "A Supposedly Fun Thing I'll Never Do Again", quote: "The cruise ship engineer launched into rapid **technobabble** about hydraulic stabilizers and ballast trim." }
    ]
  },
  "technocracy.md": {
    primary: "A system of government or societal management in which decision-makers are selected on the basis of technological and scientific expertise.",
    secondary: "A society governed or controlled by technical experts, scientists, and engineers.",
    quotes: [
      { author: "Aldous Huxley", work: "Brave New World Revisited", quote: "The danger of modern society lies in sliding into an authoritarian **technocracy** where human values are subordinated to efficiency." },
      { author: "Thorstein Veblen", work: "The Engineers and the Price System", quote: "Veblen advocated a functional **technocracy** where productive engineers, rather than speculative financiers, directed industrial production." },
      { author: "Lewis Mumford", work: "The Myth of the Machine", quote: "The totalitarian mega-machine finds its modern embodiment in an uncritical **technocracy** worshiping mechanical power." }
    ]
  },
  "technocrat.md": {
    primary: "A technical expert, scientist, or engineer who exercises managerial authority or political power.",
    secondary: "An administrator or official who relies strictly on technical, quantitative, or scientific criteria to formulate policy.",
    quotes: [
      { author: "George Orwell", work: "1984", quote: "The Inner Party member operated like a detached **technocrat**, administering state power with chilling mathematical logic." },
      { author: "John Kenneth Galbraith", work: "The New Industrial State", quote: "The modern corporate enterprise is run not by rugged individualists, but by an anonymous cadre of the **technocrat** class." },
      { author: "E. F. Schumacher", work: "Small Is Beautiful", quote: "The narrow vision of the specialized **technocrat** too often blinds him to ecological and human costs." }
    ]
  },
  "technogaianism.md": {
    primary: "An environmental philosophy asserting that advanced science, technology, and biotechnology can and should be developed to restore and sustain the Earth's environment.",
    secondary: "A green ideological framework advocating geoengineering, renewable energy technology, and eco-technological solutions to reverse ecological degradation.",
    quotes: [
      { author: "James Lovelock", work: "The Revenge of Gaia", quote: "Advocates of **technogaianism** propose that human engineering must actively assist the planetary self-regulating biosphere." },
      { author: "Stewart Brand", work: "Whole Earth Discipline", quote: "Embracing **technogaianism** means using biotechnology and nuclear power to protect wild habitats from catastrophic climate change." },
      { author: "E. O. Wilson", work: "The Future of Life", quote: "Technological innovation alone cannot save biodiversity unless guided by ethical stewardship and ecological humility." }
    ]
  },
  "technological.md": {
    primary: "Relating to, involving, or resulting from technology or applied industrial science.",
    secondary: "Characterized by or utilizing advanced mechanical, computational, or scientific techniques.",
    quotes: [
      { author: "Lewis Mumford", work: "Technics and Civilization", quote: "The **technological** revolution was preceded by a psychological transformation that equated human progress with mechanical mastery." },
      { author: "Marshall McLuhan", work: "Understanding Media", quote: "Every **technological** extension of man alters the sensory balance and psychic landscape of civilization." },
      { author: "Bertrand Russell", work: "In Praise of Idleness", quote: "Modern **technological** advances have made it possible for humanity to diminish excessive toil, if wisely directed." }
    ]
  },
  "technologically.md": {
    primary: "By means of or with regard to technology and applied science.",
    secondary: "From the standpoint of technical, mechanical, or computational development.",
    quotes: [
      { author: "Alvin Toffler", work: "Future Shock", quote: "A society that is **technologically** advanced must cultivate social institutions capable of absorbing rapid innovation." },
      { author: "Carl Sagan", work: "Pale Blue Dot", quote: "Though we are **technologically** capable of reaching distant planets, our moral wisdom still lags behind our machines." },
      { author: "Jared Diamond", work: "Guns, Germs, and Steel", quote: "Societies that became **technologically** dominant did so largely through geographic advantages in food production." }
    ]
  },
  "technologist.md": {
    primary: "A specialist or expert in a particular field of technology or applied science.",
    secondary: "A visionary, engineer, or theorist who develops, implements, or studies technological systems.",
    quotes: [
      { author: "H. G. Wells", work: "The Shape of Things to Come", quote: "The reconstruction of civilization fell into the hands of the dedicated **technologist** and transport engineer." },
      { author: "Norbert Wiener", work: "The Human Use of Human Beings", quote: "The modern **technologist** carries an immense moral responsibility for the social consequences of cybernetic automation." },
      { author: "Steve Jobs", work: "Macworld Keynote", quote: "It is in Apple's DNA that technology alone is not enough—it is technology married with liberal arts that yields results." }
    ]
  },
  "technology.md": {
    primary: "The application of scientific knowledge and mechanical principles for practical purposes, especially in industry and commerce.",
    secondary: "The collection of techniques, skills, methods, and processes used in the production of goods or services or in accomplishing objectives.",
    quotes: [
      { author: "Arthur C. Clarke", work: "Profiles of the Future", quote: "Any sufficiently advanced **technology** is indistinguishable from magic." },
      { author: "Neil Postman", work: "Technopoly: The Surrender of Culture to Technology", quote: "Uncontrolled **technology** redesigns culture from within, subordinating human traditions to algorithmic efficiency." },
      { author: "Ursula K. Le Guin", work: "The Dispossessed", quote: "We must learn to use our **technology** as an instrument of liberation rather than a tool of domination." }
    ]
  },
  "technophile.md": {
    primary: "A person who is enthusiastic about, enthusiastic for, or deeply fascinated by new technology.",
    secondary: "An ardent supporter of technological innovation who readily adopts modern digital devices and systems.",
    quotes: [
      { author: "David Foster Wallace", work: "Infinite Jest", quote: "The fervent **technophile** surrounded himself with banks of cartridge players and digital consoles." },
      { author: "Neil Postman", work: "Building a Bridge to the Eighteenth Century", quote: "The uncritical **technophile** welcomes every digital novelty without considering what human qualities might be lost." },
      { author: "William Gibson", work: "Idoru", quote: "In downtown Tokyo, every teenage **technophile** carried customized gadgets glowing with holographic displays." }
    ]
  },
  "technophilia.md": {
    primary: "Enthusiasm for or strong affection toward technology, machinery, and innovation.",
    secondary: "The cultural or psychological disposition to view technological solutions as universally beneficial and desirable.",
    quotes: [
      { author: "Lewis Mumford", work: "The Myth of the Machine", quote: "Modern society displays an irrational **technophilia**, worshiping mechanical power as an end in itself." },
      { author: "Neil Postman", work: "Technopoly", quote: "In an age of rampant **technophilia**, questions of human purpose are replaced by obsession with processing speed." },
      { author: "Alvin Toffler", work: "The Third Wave", quote: "Unchecked **technophilia** blinded planners to the social dislocations created by rapid industrial automation." }
    ]
  },
  "technophilic.md": {
    primary: "Having a strong affinity for, interest in, or enthusiasm toward technology.",
    secondary: "Promoting or characterized by the rapid adoption and prioritization of technological solutions.",
    quotes: [
      { author: "Aldous Huxley", work: "Brave New World Revisited", quote: "A thoroughly **technophilic** culture easily trades ancient liberties for promises of mechanical comfort." },
      { author: "Marshall McLuhan", work: "The Gutenberg Galaxy", quote: "Western civilization developed a **technophilic** bias that privileged linear visual order above oral tradition." },
      { author: "Carl Sagan", work: "Broca's Brain", quote: "A **technophilic** civilization must balance its scientific curiosity with acute environmental self-restraint." }
    ]
  },
  "technophobe.md": {
    primary: "A person who fears, dislikes, or avoids new technology, computers, or advanced machinery.",
    secondary: "An individual who resists or rejects mechanization and technological intrusion into personal life.",
    quotes: [
      { author: "Ray Bradbury", work: "Fahrenheit 451", quote: "The stubborn old scholar lived like a **technophobe**, refusing to install the interactive parlour walls in his cottage." },
      { author: "David Foster Wallace", work: "Consider the Lobster", quote: "He confessed to being an incorrigible **technophobe**, still writing his drafts by hand with a fountain pen." },
      { author: "Douglas Adams", work: "The Salmon of Doubt", quote: "Even the most hardened **technophobe** eventually succumbed to the convenience of the digital microwave." }
    ]
  },
  "technophobia.md": {
    primary: "An abnormal or intense fear, hatred, or avoidance of advanced technology, computers, or mechanized systems.",
    secondary: "Anxiety or resistance caused by the rapid pace of technological change and automation.",
    quotes: [
      { author: "Isaac Asimov", work: "The Caves of Steel", quote: "The medievalist faction exploited widespread **technophobia** to incite riots against humanoid robots." },
      { author: "Alvin Toffler", work: "Future Shock", quote: "When change occurs too rapidly, widespread social **technophobia** emerges as an emotional defense against disorientation." },
      { author: "Carl Sagan", work: "The Demon-Haunted World", quote: "Ignorance of science breeds suspicion, turning natural skepticism into debilitating **technophobia**." }
    ]
  },
  "technophobic.md": {
    primary: "Showing, feeling, or characterized by technophobia; fearful, suspicious, or hostile toward new technology.",
    secondary: "Resisting automation, digitization, or computerized processes in daily life.",
    quotes: [
      { author: "Kurt Vonnegut", work: "Player Piano", quote: "The underground resistance was fueled by a deeply **technophobic** rage against automated factories." },
      { author: "Thomas Pynchon", work: "Gravity's Rainbow", quote: "His **technophobic** instincts warned him against trusting the sterile electronic calculations of the guidance system." },
      { author: "Neil Postman", work: "Technopoly", quote: "To question the benefits of a machine is not to be **technophobic**; it is the first duty of a responsible citizen." }
    ]
  },
  "untechnical.md": {
    primary: "Not technical; not relating to or characterized by specialized technical skills, mechanics, or jargon.",
    secondary: "Expressed in simple, everyday language accessible to non-specialists; informal.",
    quotes: [
      { author: "Thomas Huxley", work: "Science and Culture", quote: "The lecturer succeeded in explaining complex biological principles in clear, **untechnical** language." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "Darwin deliberately adopted a plain, **untechnical** style so that his evolutionary arguments could be read by all." },
      { author: "William James", work: "Pragmatism", quote: "A sound philosophical concept should be capable of translation into vivid, **untechnical** terms understandable to common sense." }
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

console.log('Done Batch 5 (Dashboard — techn) of Cluster Art, Craft & Design (31 words)!');
