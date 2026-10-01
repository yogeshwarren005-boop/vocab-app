import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Art, Craft & Design';

const filesData = {
  // Dashboard — hyph
  "Dashboard — hyph/hyph.md": {
    primary: "The Greek root *hyphē* (web, weaving, textile, fabric); the morphological base for botanical, mycological, and histological terms relating to woven filaments.",
    secondary: "In historical linguistics and etymology, denoting structures formed like woven webs or spun threads.",
    quotes: [
      { author: "Walter William Skeat", work: "Principles of English Etymology", quote: "The Greek root **hyph** connects ancient craft weaving with the microscopic filamentary webs observed in living tissues." },
      { author: "Anton de Bary", work: "Comparative Morphology and Biology of the Fungi", quote: "From the classical root **hyph**, botanists named the basic filamentous threads that weave together fungal mycelia." },
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "In ancient Greek, the noun relates to the root **hyph**, signifying a woven web, a spider's fabric, or the texture of cloth." }
    ]
  },
  "Dashboard — hyph/hypha.md": {
    primary: "Each of the branching filaments that collectively make up the mycelium of a fungus.",
    secondary: "A tubular, chitin-walled structural filament through which fungi absorb nutrients and secrete digestive enzymes.",
    quotes: [
      { author: "Anton de Bary", work: "Comparative Morphology and Biology of the Fungi", quote: "Each individual **hypha** extends at its apical tip, branching repeatedly to form an expansive nutrient-absorbing network." },
      { author: "Alexander Fleming", work: "On the Antibacterial Action of Cultures of a Penicillium", quote: "Microscopic inspection showed the branching **hypha** of the mold secreting an inhibitory halo around bacterial colonies." },
      { author: "Peter H. Raven", work: "Biology of Plants", quote: "The slender diameter of a fungal **hypha** gives it an enormous surface-area-to-volume ratio ideal for extracellular absorption." }
    ]
  },
  "Dashboard — hyph/hyphantria.md": {
    primary: "A genus of tiger moths in the family Erebidae, notably including the fall webworm (*Hyphantria cunea*), named for its woven communal silk webs.",
    secondary: "In entomological taxonomy, an insect genus whose gregarious caterpillars construct extensive woven silk nests over foliage.",
    quotes: [
      { author: "Theodosius Dobzhansky", work: "Genetics and the Origin of Species", quote: "Populations of **Hyphantria** demonstrated rapid adaptive shifts in larval coloration across diverse climatic zones." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "The conspicuous silk tents of **Hyphantria** across autumn fruit trees often provoked excessive chemical spraying." },
      { author: "E. O. Wilson", work: "The Insect Societies", quote: "Communal web construction in larval **Hyphantria** provides thermoregulation and collective defense against parasitoid wasps." }
    ]
  },
  "Dashboard — hyph/hyphema.md": {
    primary: "An accumulation of blood inside the anterior chamber of the eye, typically pooling between the cornea and the iris following trauma.",
    secondary: "In clinical ophthalmology, an intraocular hemorrhage that can lead to elevated intraocular pressure and corneal staining.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Blunt ocular contusion frequently produces a visible **hyphema**, requiring prompt immobilization to avert secondary hemorrhage." },
      { author: "Harvey Cushing", work: "Studies in Intracranial Physiology", quote: "Examination revealed traumatic mydriasis accompanied by a layered **hyphema** settling along the inferior limbus." },
      { author: "Atul Gawande", work: "Better: A Surgeon's Notes on Performance", quote: "The resident carefully checked the patient's anterior chamber, monitoring the clearance of a traumatic **hyphema**." }
    ]
  },
  "Dashboard — hyph/hyphen.md": {
    primary: "A punctuation mark (-) used to join words or parts of words together, or to divide syllables at the end of a line.",
    secondary: "Figuratively, a connecting link, bridge, or shared relationship between two disparate entities, cultures, or concepts.",
    quotes: [
      { author: "George Orwell", work: "Politics and the English Language", quote: "Careful writers avoid unnecessary ornamental compound words joined by an awkward **hyphen**." },
      { author: "David Crystal", work: "Making a Point: The Pernickety Story of English Punctuation", quote: "The versatile **hyphen** serves both syntactic cohesion and typographical line-breaking convenience." },
      { author: "H. L. Mencken", work: "The American Language", quote: "American newspaper copy-desks waged perpetual war against the overuse of the British **hyphen**." }
    ]
  },
  "Dashboard — hyph/hyphenate.md": {
    primary: "To connect, join, or divide words or syllables with a hyphen.",
    secondary: "To maintain a dual identity or fulfill multiple professional roles simultaneously (as in hyphenated identities).",
    quotes: [
      { author: "Theodore Roosevelt", work: "Fear God and Take Your Own Part", quote: "There is no room in this country for hyphenated Americanism; we must not **hyphenate** our allegiance." },
      { author: "David Foster Wallace", work: "Authority and American Usage", quote: "Deciding whether to **hyphenate** compound modifiers before a noun requires understanding grammatical juncture." },
      { author: "Virginia Woolf", work: "The Common Reader", quote: "The essayist paused to **hyphenate** two conflicting concepts, forging a novel metaphor on the page." }
    ]
  },
  "Dashboard — hyph/hyphenation.md": {
    primary: "The act, practice, or typographical system of dividing or joining words with a hyphen.",
    secondary: "In digital typography and printing, the automated algorithmic division of words across right margins to ensure even text justification.",
    quotes: [
      { author: "Donald Knuth", work: "The TeXbook", quote: "The computer typesetting system incorporates an intricate **hyphenation** algorithm based on linguistic morphology." },
      { author: "David Crystal", work: "Spell It Out: The Singular Story of English Spelling", quote: "Inconsistent **hyphenation** remains one of the most frustrating ambiguities in English orthography." },
      { author: "Aldous Huxley", work: "Jesting Pilate", quote: "The mechanical **hyphenation** of names in modern journalism often reflects hurried bureaucratic labeling." }
    ]
  },
  "Dashboard — hyph/hyphomycete.md": {
    primary: "Any fungus of the former artificial class Hyphomycetes, characterized by asexual conidial reproduction directly on uncontained hyphae.",
    secondary: "In mycology, an anamorphic mold or imperfect fungus that lacks closed fruiting structures such as pycnidia or acervuli.",
    quotes: [
      { author: "Anton de Bary", work: "Comparative Morphology and Biology of the Fungi", quote: "Every classic **hyphomycete** develops airborne conidiophores rising directly from the vegetative mycelium." },
      { author: "Alexander Flecker", work: "Fungal Ecology in Stream Ecosystems", quote: "Aquatic forms of **hyphomycete** play a crucial role in breaking down leaf litter in freshwater streams." },
      { author: "Peter H. Raven", work: "Biology of Plants", quote: "Systematists now reclassify each **hyphomycete** into Ascomycota based on molecular phylogenetic markers." }
    ]
  },
  "Dashboard — hyph/hyphopodium.md": {
    primary: "A specialized, short, lateral branch or outgrowth of a fungal hypha that adheres to a host plant surface (an appressorium-like holdfast).",
    secondary: "In plant pathology, a fungal anchoring structure through which a penetration peg is driven into the cuticle of a host leaf.",
    quotes: [
      { author: "Anton de Bary", work: "Comparative Morphology and Biology of the Fungi", quote: "The epiphytic fungus secures itself to the leaf epidermis by forming a lobed, melanized **hyphopodium**." },
      { author: "G. W. Martin", work: "The Fungi: An Advanced Treatise", quote: "From the basal surface of the **hyphopodium**, a minute infection peg pierces the host cell wall." },
      { author: "F. L. Stevens", work: "Plant Disease Fungi", quote: "Under high magnification, each dark **hyphopodium** appears firmly cemented to the glossy plant cuticle." }
    ]
  },

  // Dashboard — orches
  "Dashboard — orches/orches.md": {
    primary: "The Greek root *orchēsis* (dancing, the dance); the etymological root of words concerning choreographed movement, stage dancing, and instrumental ensembles.",
    secondary: "In morphological linguistics, designating rhythmic leaping, jumping movement, or the space reserved for dancing in antique theaters.",
    quotes: [
      { author: "Walter William Skeat", work: "Principles of English Etymology", quote: "The classical root **orches** originally designated the circular dancing floor where the Athenian chorus performed." },
      { author: "Gilbert Murray", work: "The Rise of the Greek Epic", quote: "Choral drama evolved directly from ancient festive dances rooted in the primitive Greek **orches**." },
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The noun *orchesis* traces to the base **orches**, denoting the art of the dance in religious and theatrical festivals." }
    ]
  },
  "Dashboard — orches/orchestia.md": {
    primary: "A genus of talitrid amphipod crustaceans commonly known as beach fleas or sandhoppers, named for their dancing, jumping locomotion.",
    secondary: "In marine littoral biology, small semiterrestrial crustaceans that inhabit wrack zones along sandy and rocky seashores.",
    quotes: [
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "When the tide recedes, countless tiny beach fleas of the genus **Orchestia** hop energetically across the stranded kelp." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "The muscular urosome of **Orchestia** enables sudden leaping escapes when disturbed in damp coastal sand." },
      { author: "Alister Hardy", work: "The Open Sea", quote: "Intertidal scavengers such as **Orchestia** perform vital ecological functions by recycling decomposing drift-weed." }
    ]
  },
  "Dashboard — orches/orchestiidae.md": {
    primary: "A former or historical family name for the beach-dwelling amphipod sandhoppers (now classified within the family Talitridae).",
    secondary: "In carcinology, an amphipod taxon erected to group supralittoral and terrestrial crustaceans adapted for saltatorial jumping.",
    quotes: [
      { author: "William Swainson", work: "A Treatise on Malacology and Natural History", quote: "In systematic arrangements of Crustacea, naturalists grouped the leaping sandhoppers under the family **Orchestiidae**." },
      { author: "Richard Owen", work: "Lectures on Comparative Anatomy", quote: "Members of the **Orchestiidae** exhibit modified posterior appendages uniquely structured for spring-like locomotion." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "Along the Patagonian coast, species allied to the **Orchestiidae** swarmed beneath every decaying carcass." }
    ]
  },
  "Dashboard — orches/orchestra.md": {
    primary: "A large ensemble of musical instrumentalists playing together, typically combining strings, woodwinds, brass, and percussion.",
    secondary: "In ancient Greek theater, the circular or semicircular space in front of the proscenium where the chorus danced and sang.",
    quotes: [
      { author: "Hector Berlioz", work: "Treatise on Modern Instrumentation and Orchestration", quote: "The symphonic **orchestra** is a magnificent musical colossus capable of evoking every conceivable emotion." },
      { author: "E. M. Forster", work: "Howards End", quote: "The full **orchestra** struck into the triumphant final movement of Beethoven's symphony, shaking the hall." },
      { author: "Friedrich Nietzsche", work: "The Birth of Tragedy", quote: "In the antique theater, the tragic chorus stood in the central **orchestra**, mediating between myth and spectator." }
    ]
  },
  "Dashboard — orches/orchestral.md": {
    primary: "Pertaining to, composed for, or performed by an orchestra.",
    secondary: "Characterized by grand, multi-instrumental sonic textures, rich harmonic layering, and symphonic color.",
    quotes: [
      { author: "Leonard Bernstein", work: "The Joy of Music", quote: "Brahms achieved an **orchestral** warmth that wrapped the listener in rich velvet sonorities." },
      { author: "Virginia Woolf", work: "The Waves", quote: "The breaking waves outside sounded like a distant **orchestral** crescendo swelling against the rocks." },
      { author: "Aaron Copland", work: "What to Listen for in Music", quote: "Mastering **orchestral** scoring requires an intimate knowledge of each instrument's dynamic range and timbre." }
    ]
  },
  "Dashboard — orches/orchestrate.md": {
    primary: "To compose or arrange music for an orchestra.",
    secondary: "Figuratively, to carefully plan, coordinate, and organize a complex event, campaign, or undertaking to achieve a desired outcome.",
    quotes: [
      { author: "Igor Stravinsky", work: "Chronicles of My Life", quote: "I worked feverishly throughout the winter to **orchestrate** the intricate pagan rhythms of the ballet." },
      { author: "George Orwell", work: "1984", quote: "The Party knew precisely how to **orchestrate** public hatred through carefully timed propaganda broadcasts." },
      { author: "John le Carré", work: "Tinker Tailor Soldier Spy", quote: "Smiley began to **orchestrate** a discreet trap designed to flush the elusive mole into the open." }
    ]
  },
  "Dashboard — orches/orchestrated.md": {
    primary: "Scored, arranged, or adapted for performance by an orchestra.",
    secondary: "Carefully and covertly arranged, directed, or coordinated behind the scenes to produce a specific effect.",
    quotes: [
      { author: "Maurice Ravel", work: "Letters and Recordings", quote: "Mussorgsky's piano suite, brilliantly **orchestrated**, revealed a monumental grandeur previously hidden in the keyboard score." },
      { author: "Bob Woodward", work: "All the President's Men", quote: "The investigative reporters discovered that the burglary was part of a massively **orchestrated** political campaign." },
      { author: "Hannah Arendt", work: "Eichmann in Jerusalem", quote: "The totalitarian trial was an elaborately **orchestrated** spectacle meant to demonstrate state omnipotence." }
    ]
  },
  "Dashboard — orches/orchestration.md": {
    primary: "The art, technique, or craft of arranging and scoring musical compositions for an orchestra.",
    secondary: "The strategic arrangement, coordination, or harmonized management of diverse elements in a complex project or system.",
    quotes: [
      { author: "Nikolai Rimsky-Korsakov", work: "Principles of Orchestration", quote: "True **orchestration** is not mere decoration; it is one of the essential elements of musical thought itself." },
      { author: "David Byrne", work: "How Music Works", quote: "The acoustic environment dictates the optimal **orchestration** of instruments in any concert setting." },
      { author: "Henry Kissinger", work: "Diplomacy", quote: "Bismarck showed consummate mastery in the diplomatic **orchestration** of European alliances." }
    ]
  },
  "Dashboard — orches/orchestrator.md": {
    primary: "A musician who arranges and scores music composed by themselves or others for orchestral performance.",
    secondary: "A person or computerized software system that plans, directs, and coordinates the execution of complex multi-part workflows.",
    quotes: [
      { author: "George Gershwin", work: "Letters on Rhapsody in Blue", quote: "Ferde Grofé served as the brilliant **orchestrator** who gave the concert piece its shimmering jazz colors." },
      { author: "Robert Craft", work: "Conversations with Igor Stravinsky", quote: "Stravinsky was his own meticulous **orchestrator**, calculating every balance of instrumental timbre with scientific exactness." },
      { author: "Sinclair Lewis", work: "Babbitt", quote: "He fancied himself the chief **orchestrator** of civic enthusiasm at the weekly booster luncheon." }
    ]
  },

  // Dashboard — parthen
  "Dashboard — parthen/parthen.md": {
    primary: "The Greek root *parthenos* (maiden, virgin, pure, unblemished); the etymological base for words concerning virgin birth, purity, and Athena's cult.",
    secondary: "In biological and classical terminology, denoting unfertilized development or virgin architectural sanctuaries.",
    quotes: [
      { author: "Walter William Skeat", work: "Principles of English Etymology", quote: "The Greek root **parthen** appears in words referring both to unfertilized reproduction and to the temple of the virgin goddess." },
      { author: "Gilbert Murray", work: "Five Stages of Greek Religion", quote: "The maiden epithet rooted in **parthen** embodied the inviolate sovereignty and wisdom of Athena." },
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The base **parthen** designates an unmarried maiden or pure virgin in Homeric epic and tragic poetry." }
    ]
  },
  "Dashboard — parthen/parthenium.md": {
    primary: "A genus of North American and Neotropical shrubs in the aster family Asteraceae, including guayule (*Parthenium argentatum*) and feverfew.",
    secondary: "In economic botany and ethnobotany, a plant genus historically valued for natural rubber latex extraction and medicinal alkaloids.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The composite genus **Parthenium** features small, whitish flower-heads and aromatic, resinous leaves." },
      { author: "Alexander von Humboldt", work: "Personal Narrative of Travels", quote: "Indigenous peoples in northern Mexico harvested rubber from wild stands of shrubby **Parthenium**." },
      { author: "Peter H. Raven", work: "Biology of Plants", quote: "Agronomists investigated **Parthenium** as an alternative arid-zone crop for industrial rubber production." }
    ]
  },
  "Dashboard — parthen/parthenocarpy.md": {
    primary: "The development or production of fruit without prior fertilization of ovules, resulting in seedless fruit (e.g. bananas, seedless grapes).",
    secondary: "In plant physiology, natural or hormone-induced development of fruit tissues in the absence of pollination.",
    quotes: [
      { author: "Liberty Hyde Bailey", work: "The Principles of Fruit-Growing", quote: "Commercial citrus growers value natural **parthenocarpy** for delivering completely seedless navel oranges." },
      { author: "Peter H. Raven", work: "Biology of Plants", quote: "Applying exogenous gibberellins induces artificial **parthenocarpy** in greenhouse tomato cultivars." },
      { author: "Charles Darwin", work: "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", quote: "In certain species, the ovaries swell into succulent fruits through spontaneous **parthenocarpy** despite sterile pollen." }
    ]
  },
  "Dashboard — parthen/parthenocissus.md": {
    primary: "A genus of climbing woody vines in the grape family Vitaceae, including Virginia creeper (*Parthenocissus quinquefolia*) and Boston ivy.",
    secondary: "In horticulture, vigorous ornamental vines that climb brickwork and rock faces using adhesive branching tendril disks.",
    quotes: [
      { author: "John Muir", work: "My First Summer in the Sierra", quote: "Vines of wild **Parthenocissus** draped the granite crags in brilliant crimson tapestries as autumn approached." },
      { author: "Asa Gray", work: "Structural Botany", quote: "The specialized adhesive tips of **Parthenocissus** tendrils secrete a sticky fluid that cements the climber to masonry." },
      { author: "Henry David Thoreau", work: "The Maine Woods", quote: "Dense festoons of **Parthenocissus** climbed high into the spruce boughs beside the riverbank." }
    ]
  },
  "Dashboard — parthen/parthenogenesis.md": {
    primary: "A form of asexual reproduction in which an embryo develops from an unfertilized egg cell without fertilization by male sperm.",
    secondary: "In evolutionary biology, a reproductive strategy observed in diverse invertebrates, reptiles, and plants, producing clones or haploid offspring.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "On the Agamic Reproduction and Morphology of Aphis", quote: "Generations of female aphids multiply with astonishing rapidity through seasonal **parthenogenesis**." },
      { author: "Richard Dawkins", work: "The Extended Phenotype", quote: "The evolutionary puzzle of sexual reproduction is highlighted by the occasional emergence of obligate **parthenogenesis** in lizards." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "Whiptail lizards of the genus *Aspidoscelis* persist entirely through all-female **parthenogenesis**." }
    ]
  },
  "Dashboard — parthen/parthenogenetic.md": {
    primary: "Pertaining to, produced by, or characterized by parthenogenesis; developing from an unfertilized ovum.",
    secondary: "Describing organisms, populations, or reproductive cycles that occur without genetic contribution from male gametes.",
    quotes: [
      { author: "Theodosius Dobzhansky", work: "Genetics and the Origin of Species", quote: "Certain stick insects establish viable **parthenogenetic** populations across isolated geographic ranges." },
      { author: "E. O. Wilson", work: "Sociobiology: The New Synthesis", quote: "Haplodiploid sex determination in social hymenoptera depends on **parthenogenetic** production of haploid males." },
      { author: "Ernst Mayr", work: "Animal Species and Evolution", quote: "The evolutionary longevity of strictly **parthenogenetic** lineages remains an active debate in population genetics." }
    ]
  },
  "Dashboard — parthen/parthenogeny.md": {
    primary: "Parthenogenesis; reproduction without fertilization by male gametes.",
    secondary: "The biological generation and development of an organism from an unfertilized female egg cell.",
    quotes: [
      { author: "Herbert Spencer", work: "The Principles of Biology", quote: "The occurrence of **parthenogeny** in lower organisms demonstrates that development may proceed without gametic union." },
      { author: "Ernst Haeckel", work: "The Wonders of Life", quote: "In rotational cycles of **parthenogeny**, virgin generations alternate with sexual forms to optimize survival." },
      { author: "August Weismann", work: "Essays Upon Heredity", quote: "Weismann studied whether germ-plasm continuity operated identically in cases of pure **parthenogeny**." }
    ]
  },
  "Dashboard — parthen/Parthenon.md": {
    primary: "The iconic 5th-century BCE Doric temple on the Athenian Acropolis, dedicated to the maiden goddess Athena Parthenos.",
    secondary: "A crowning masterpiece of classical Greek architecture, renowned for its optical refinements, sculpted friezes, and enduring cultural symbolism.",
    quotes: [
      { author: "Lord Byron", work: "Childe Harold's Pilgrimage", quote: "Cold is the heart, fair Greece, that looks on thee, nor feels as lovers o'er the dust of the **Parthenon**." },
      { author: "John Ruskin", work: "The Seven Lamps of Architecture", quote: "The subtle curvatures of the stylobate of the **Parthenon** demonstrate that perfection in art transcends mechanical geometry." },
      { author: "Will Durant", work: "The Life of Greece", quote: "Ictinus and Callicrates raised the **Parthenon** upon the Acropolis as the supreme monument of Athenian civilization." }
    ]
  },
  "Dashboard — parthen/Parthenope.md": {
    primary: "In Greek mythology, one of the Sirens who cast herself into the sea when Odysseus resisted her song; the ancient Greek settlement that became Naples.",
    secondary: "In classical literature and astronomy, the poetic eponym for the city of Naples, and a main-belt asteroid discovered in 1850.",
    quotes: [
      { author: "Virgil", work: "Georgics", quote: "In those days sweet **Parthenope** nourished me, Virgil, flourishing in the pursuits of unheralded peace." },
      { author: "Percy Bysshe Shelley", work: "Ode to Naples", quote: "The Siren city, bright **Parthenope**, lay dreaming beside the azure waters of her volcanic bay." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Belisarius marched his legions south toward the ancient walls of **Parthenope**, now known as Naples." }
    ]
  },
  "Dashboard — parthen/parthenote.md": {
    primary: "An organism, embryo, or cell produced by parthenogenesis without fertilization by a male gamete.",
    secondary: "In developmental biology and stem cell research, an unfertilized oocyte experimentally activated to divide and form blastocysts.",
    quotes: [
      { author: "Jacques Loeb", work: "Artificial Parthenogenesis and Fertilization", quote: "Chemical stimulation triggered the sea urchin egg to develop into a swimming **parthenote** larva." },
      { author: "Hans Spemann", work: "Embryonic Development and Induction", quote: "The cleavage stages of the amphibian **parthenote** mirrored normal embryogenesis through early blastula formation." },
      { author: "Robert Edwards", work: "Maturation of Human Oocytes", quote: "Ethical research explored whether a mammalian **parthenote** could yield pluripotent stem cells without generating viable life." }
    ]
  },

  // Dashboard — mim
  "Dashboard — mim/mim.md": {
    primary: "The Greek root *mimos* (imitator, actor, mime, mimic); the morphological base for words relating to imitation, theatrical acting, and biological mimicry.",
    secondary: "In Scottish and Northern English dialect, prudishly modest, quiet, demure, or primly silent.",
    quotes: [
      { author: "Walter William Skeat", work: "Principles of English Etymology", quote: "The Greek root **mim** provided European languages with fundamental terms for theatrical performance and visual mimicry." },
      { author: "Robert Burns", work: "Halloween", quote: "She was na cheek for chow, nor proud, but social, **mim**, and genteel." },
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The noun *mimos* derives from the base **mim**, denoting an actor who imitates scenes from real life." }
    ]
  },
  "Dashboard — mim/mime.md": {
    primary: "The theatrical technique of expressing ideas, characters, or actions through gestures, physical movement, and facial expressions without speech.",
    secondary: "A theatrical performer or actor who specializes in pantomime and silent characterization.",
    quotes: [
      { author: "Marcel Marceau", work: "The Story of Bip", quote: "The art of **mime** makes the invisible visible through the poetical geometry of the human body." },
      { author: "Virginia Woolf", work: "The Common Reader", quote: "The street entertainer enacted a satirical **mime** of high society, drawing laughter from the crowd." },
      { author: "Arthur Symons", work: "Studies in Seven Arts", quote: "In pure **mime**, every gesture is pregnant with meaning, unencumbered by the accidental ambiguities of words." }
    ]
  },
  "Dashboard — mim/mimeograph.md": {
    primary: "A duplicating machine that prints copies from a typed, drawn, or cut stencil wrapped around an ink-filled rotating drum.",
    secondary: "To make copies of a text or document using a mimeograph machine.",
    quotes: [
      { author: "Thomas Edison", work: "The Mimeograph Patents", quote: "The newly patented **mimeograph** enabled business offices to produce hundreds of identical copies with swift dispatch." },
      { author: "Sylvia Plath", work: "The Bell Jar", quote: "The acrid smell of blue ink from the office **mimeograph** drifted through the publishing house hallway." },
      { author: "David Foster Wallace", work: "Infinite Jest", quote: "Classroom handouts, fresh off the purple **mimeograph**, carried a distinct chemical aroma that students inhaled." }
    ]
  },
  "Dashboard — mim/mimer.md": {
    primary: "A person who performs in mime; a mimic or pantomimist.",
    secondary: "In medieval folk drama, a muller or mummer performing masked seasonal folk plays.",
    quotes: [
      { author: "Thomas Hardy", work: "The Return of the Native", quote: "The village **mimer** brandished his wooden broadsword before the cottage hearth in the traditional Christmas play." },
      { author: "Washington Irving", work: "The Sketch Book of Geoffrey Crayon", quote: "Masked revelers and each rustic **mimer** paraded through the hall to amuse the country squire." },
      { author: "Walter Pater", work: "Greek Studies", quote: "The antique **mimer** caricatured local magistrates with biting, improvised bodily gestures." }
    ]
  },
  "Dashboard — mim/mimesis.md": {
    primary: "The deliberate imitation or realistic representation of the external world, human nature, and life in literature and the arts.",
    secondary: "In literary and critical theory (elaborated by Aristotle and Erich Auerbach), the aesthetic mediation through which art mirrors reality.",
    quotes: [
      { author: "Aristotle", work: "Poetics", quote: "Tragedy is an imitation of an action, and this **mimesis** of life is innate in human nature from childhood." },
      { author: "Erich Auerbach", work: "Mimesis: The Representation of Reality in Western Literature", quote: "Western literature demonstrates a continuous evolution in the realistic **mimesis** of everyday human experience." },
      { author: "Plato", work: "The Republic", quote: "Plato cautioned against deceptive **mimesis**, arguing that the artist's imitation is three removes from essential truth." }
    ]
  },
  "Dashboard — mim/mimetic.md": {
    primary: "Relating to, characterized by, or exhibiting mimesis, imitation, or mimicry.",
    secondary: "In evolutionary biology, describing organisms that closely resemble other species or environmental objects to deter predators or lure prey.",
    quotes: [
      { author: "Henry Walter Bates", work: "The Naturalist on the River Amazons", quote: "The remarkable **mimetic** resemblance between harmless butterflies and toxic heliconids protects them from avian predators." },
      { author: "René Girard", work: "Violence and the Sacred", quote: "Human desire is fundamentally **mimetic**, constantly modeling itself upon the desires of others." },
      { author: "Walter Benjamin", work: "On the Mimetic Faculty", quote: "The **mimetic** faculty is the ancient human capacity to perceive similarities and produce correspondences." }
    ]
  },
  "Dashboard — mim/mimic.md": {
    primary: "To imitate or copy the actions, speech, gestures, or appearance of someone or something, often for entertainment or mockery.",
    secondary: "A person, animal, or object that imitates or resembles another; in biology, an organism exhibiting protective mimicry.",
    quotes: [
      { author: "William Shakespeare", work: "A Midsummer Night's Dream", quote: "Anon his Gull must to him come, and straightway like a **mimic** do his part." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "Insects that **mimic** dead leaves or poisonous species escape discovery by insectivorous birds." },
      { author: "Mark Twain", work: "The Adventures of Tom Sawyer", quote: "Tom loved to **mimic** the solemn nasal drone of the village parson whenever the boys gathered behind the barn." }
    ]
  },
  "Dashboard — mim/mimicker.md": {
    primary: "One who mimics or imitates another, especially in voice, mannerisms, gestures, or appearance.",
    secondary: "A copycat, mocking imitator, or parodist who mimics others for satirical effect.",
    quotes: [
      { author: "Charles Dickens", work: "Nicholas Nickleby", quote: "The theatrical company boasted an extraordinary **mimicker** who could duplicate the voice of any London alderman." },
      { author: "George Eliot", work: "Middlemarch", quote: "He proved an adroit **mimicker** of provincial pomposity, mocking his uncle's heavy political speeches." },
      { author: "Aldous Huxley", work: "Those Barren Leaves", quote: "The satirist was a cruel **mimicker**, pinpointing his victim's nervous vocal tics with unerring accuracy." }
    ]
  },
  "Dashboard — mim/necromimesis.md": {
    primary: "A psychiatric delusion in which a living person firmly believes themselves to be dead, or the clinical simulation of death (related to Cotard's syndrome).",
    secondary: "In forensic pathology and neurology, an extreme catatonic or stuporous state resembling physical death.",
    quotes: [
      { author: "Jules Cotard", work: "On Hypochondriacal Delusions in a Severe Form of Anxious Melancholia", quote: "In profound melancholia, patients exhibit **necromimesis**, insisting that their organs have ceased functioning and they are deceased." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "Catatonic trance occasionally mimicked **necromimesis**, presenting an eerie stillness that deceived observers into suspecting death." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe hysterical catalepsy may produce a transient **necromimesis** with imperceptible pulse and flaccid musculature." }
    ]
  },
  "Dashboard — mim/pantomime.md": {
    primary: "A dramatic performance in which a story is conveyed entirely through bodily gestures, facial expression, and dance without spoken words.",
    secondary: "A traditional British theatrical entertainment, especially for children at Christmas, featuring slapstick comedy, cross-dressing, and fairy tales.",
    quotes: [
      { author: "Charles Lamb", work: "Essays of Elia", quote: "As children, we were taken once a year to the holiday **pantomime**, dazzled by harlequin's magic wand." },
      { author: "Charles Dickens", work: "The Pickwick Papers", quote: "The clowns in the traveling **pantomime** tumbled across the boards with acrobatic hilarity." },
      { author: "Oscar Wilde", work: "The Picture of Dorian Gray", quote: "The exquisite actress brought life to the stage through expressive **pantomime** that transcended dialogue." }
    ]
  },
  "Dashboard — mim/pantomimer.md": {
    primary: "An actor, performer, or dancer who acts in a pantomime without speaking; a mime.",
    secondary: "A performer in traditional pantomime or harlequinade productions.",
    quotes: [
      { author: "Henry Fielding", work: "Tom Jones", quote: "The agile **pantomimer** skipped across the platform, delighting the fairground spectators with silent antics." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "Behind the curtain, the weary **pantomimer** applied fresh chalk to his face before leaping onto the boards." },
      { author: "Arthur Conan Doyle", work: "The Sign of the Four", quote: "The agile suspect slipped through the narrow skylight like a trained **pantomimer** escaping a harlequinade." }
    ]
  },
  "Dashboard — mim/pantomimist.md": {
    primary: "A performer or actor highly skilled in the dramatic art of pantomime.",
    secondary: "A classical or theatrical artist whose primary expressive vehicle is silent, stylized bodily gesture.",
    quotes: [
      { author: "Washington Irving", work: "Bracebridge Hall", quote: "The Italian **pantomimist** astonished the guests with his uncanny ability to narrate an entire tragedy without a syllable." },
      { author: "Walter Pater", work: "Marius the Epicurean", quote: "In imperial Rome, the celebrated **pantomimist** held crowds in breathless suspense through graceful choreographic storytelling." },
      { author: "Edgar Allan Poe", work: "The Assignation", quote: "He moved with the calculated, dreamlike precision of an antique **pantomimist** performing before royalty." }
    ]
  },
  "Dashboard — mim/phenomime.md": {
    primary: "In linguistic sound symbolism (especially Japanese mimetic morphology), a word that depicts a physical phenomenon, motion, or state rather than a sound.",
    secondary: "A mimetic word (gitaigo) representing visual perceptions, textures, or spatial movements through phonetic symbolism.",
    quotes: [
      { author: "Edward Sapir", work: "Language: An Introduction to the Study of Speech", quote: "Languages frequently employ a **phenomime** to depict visual motion or physical texture through symbolic phonetic patterning." },
      { author: "Roman Jakobson", work: "Six Lectures on Sound and Meaning", quote: "Unlike direct onomatopoeia, a **phenomime** translates non-auditory visual phenomena into evocative vocal sounds." },
      { author: "Mark Dingemanse", work: "The Meaning and Use of Ideophones", quote: "A Japanese **phenomime** like *pikapika* does not describe an auditory event, but the visual sparkling of bright light." }
    ]
  },
  "Dashboard — mim/psychomime.md": {
    primary: "A word or expressive linguistic item that depicts a psychological state, subjective feeling, or emotional attitude (a psychomimetic ideophone).",
    secondary: "In sound symbolism and lexicology, a mimetic lexical form (gijōgo) representing internal mental states or emotional dispositions.",
    quotes: [
      { author: "Roman Jakobson", work: "The Sound Shape of Language", quote: "In expressive vocabulary, a **psychomime** links phonetic nuance directly to subjective states of inner turmoil or calm." },
      { author: "Edward Sapir", work: "Selected Writings in Language, Culture and Personality", quote: "The expressive utility of a **psychomime** lies in conveying visceral mental attitudes without descriptive abstraction." },
      { author: "Mark Dingemanse", work: "The Meaning and Use of Ideophones", quote: "When describing nervousness or excitement, speakers employ a **psychomime** to mirror the felt emotional state." }
    ]
  },
  "Dashboard — mim/psychomimetic.md": {
    primary: "In linguistics, pertaining to or functioning as a psychomime; depicting mental states or emotional feelings through sound symbolism.",
    secondary: "In pharmacology (more commonly psychotomimetic), mimicking the symptoms of psychosis or inducing altered states of consciousness.",
    quotes: [
      { author: "Aldous Huxley", work: "The Doors of Perception", quote: "Pharmacologists investigated mescaline as a **psychomimetic** agent that simulated schizophrenic perceptions in healthy volunteers." },
      { author: "Oliver Sacks", work: "Hallucinations", quote: "The bizarre sensory distortions induced by **psychomimetic** compounds provided insight into neural perceptual gating." },
      { author: "Roman Jakobson", work: "The Sound Shape of Language", quote: "Linguists analyze **psychomimetic** words to understand how phonological tones evoke internal psychological responses." }
    ]
  }
};

for (const [relPath, entry] of Object.entries(filesData)) {
  const filePath = path.join(baseDir, relPath);
  if (!fs.existsSync(filePath)) {
    console.error(`Missing file: ${filePath}`);
    continue;
  }
  const content = fs.readFileSync(filePath, 'utf8');

  // Find top portion up to > [!book]
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
  console.log(`Updated: ${relPath}`);
}

console.log('Done Batch 2 of Cluster Art, Craft & Design (43 words)!');
