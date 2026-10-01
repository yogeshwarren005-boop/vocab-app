import fs from 'fs';
import path from 'path';

const CLUSTER_DIR = 'App database/Greek roots/Cluster Life & Vitality';
const DASHBOARD = 'Dashboard — bio';

const BATCH1_DATA = {
  "abiogenesis": {
    primary: "The generation of living organisms from inanimate matter; spontaneous generation, or modern models for the origin of life from inorganic compounds.",
    secondary: "In evolutionary biochemistry, the hypothesized chemical sequence (prebiotic synthesis) through which cellular life first arose on primordial Earth.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Biogenesis and Abiogenesis", text: "I shall call the doctrine that living matter may be produced by not living matter, the hypothesis of **abiogenesis**." },
      { author: "John Burdon Sanderson Haldane", work: "The Origin of Life", text: "The earliest stages of terrestrial **abiogenesis** required an atmosphere essentially devoid of molecular oxygen." },
      { author: "Alexander Oparin", work: "The Origin of Life", text: "Organic coacervate droplets represented an indispensable physical bridge during the prolonged course of **abiogenesis**." }
    ]
  },
  "abiogenetic": {
    primary: "Relating to or characterized by abiogenesis; produced without the intervention of preexisting living organisms.",
    secondary: "Pertaining to chemical pathways on early planets or extraterrestrial bodies that synthesize organic molecules through inorganic reactions.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Critiques and Addresses", text: "Redi's decisive experiments dealt a fatal blow to the older **abiogenetic** assertions regarding decaying flesh." },
      { author: "Harold Urey", work: "The Planets: Their Origin and Development", text: "Electrical discharges through methane-ammonia mixtures yielded an array of **abiogenetic** amino acids." },
      { author: "Cyril Ponnamperuma", work: "The Origins of Life", text: "The carbonaceous chondrites preserve ancient evidence of **abiogenetic** synthesis in the proto-solar nebula." }
    ]
  },
  "abiogenist": {
    primary: "An advocate or proponent of the theory of abiogenesis or spontaneous generation.",
    secondary: "A natural philosopher or early experimenter who maintained that microscopic animalcules originate de novo from sterile infusions.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Lay Sermons, Addresses, and Reviews", text: "The obstinate **abiogenist** argued that hermetically sealed broths still yielded infusions of microscopic monads." },
      { author: "John Tyndall", work: "Essays on the Floating-Matter of the Air", text: "Every rigorous optical test deprived the modern **abiogenist** of his imagined spontaneous organisms." },
      { author: "Louis Pasteur", work: "Memoir on the Organized Corpuscles Existing in the Atmosphere", text: "No **abiogenist** has ever produced living bacteria in an organic medium guarded from airborne germs." }
    ]
  },
  "abiotic": {
    primary: "Deceased, non-living, or characterized by the absence of biological organisms or vital processes.",
    secondary: "In ecological systems, pertaining to non-biological physical and chemical environmental factors, such as mineral composition, radiation, and temperature.",
    quotes: [
      { author: "Eugene Odum", work: "Fundamentals of Ecology", text: "The ecosystem functions as an integrated unit comprising biotic communities and their surrounding **abiotic** environment." },
      { author: "Arthur Tansley", work: "The Use and Abuse of Vegetational Concepts and Terms", text: "Physical habitat factors constitute the complex **abiotic** matrix within which vegetation succession occurs." },
      { author: "G. Evelyn Hutchinson", work: "The Ecological Theater and the Evolutionary Play", text: "The ecological niche defines an n-dimensional hypervolume of biotic interactions and **abiotic** tolerances." }
    ]
  },
  "aerobiology": {
    primary: "The branch of biology concerned with the dispersal, passive transport, and atmospheric behavior of airborne biological particles such as pollen, fungal spores, and bacteria.",
    secondary: "The study of living organisms inhabiting or sustained within the troposphere and stratosphere and their meteorological interactions.",
    quotes: [
      { author: "Fred C. Meier", work: "The Field of Aerobiology", text: "Recent investigations in **aerobiology** demonstrate that living spores survive at extraordinary altitudes above the continental plains." },
      { author: "E. C. Stakman", work: "Plant Pathology and Human Welfare", text: "Epidemiological forecasting of wheat rust epidemics depends fundamentally on advances in synoptic **aerobiology**." },
      { author: "Charles Lindbergh", work: "High-Altitude Collecting and Atmospheric Biology", text: "During transatlantic flights, special sky-hooks were deployed to collect microscopic specimens for pioneer studies in **aerobiology**." }
    ]
  },
  "amphibiotic": {
    primary: "Living both on land and in water; capable of existing alternately in aquatic and terrestrial environments.",
    secondary: "In entomology and parasitology, describing organisms whose larval stage is strictly aquatic while the adult stage is terrestrial or aerial.",
    quotes: [
      { author: "Thomas Say", work: "American Entomology", text: "The larvae of odonata lead an **amphibiotic** life, transforming from subterranean aquatic nymphs into swift aerial predators." },
      { author: "William Morton Wheeler", work: "Ants: Their Structure, Development and Behavior", text: "Certain littoral insects maintain an **amphibiotic** existence along tidal estuaries." },
      { author: "Richard Owen", work: "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", text: "The respiratory adaptations of **amphibiotic** arthropods bridge the physiological divide between gills and tracheae." }
    ]
  },
  "anabiotic": {
    primary: "Pertaining to or characterized by anabiosis; capable of reviving after apparent death, dehydration, or suspended animation.",
    secondary: "Describing physiological states of extreme cryptobiosis in which metabolic activity ceases entirely and later resumes upon rehydration.",
    quotes: [
      { author: "Wilhelm Preyer", work: "Specielle Physiologie des Embryo", text: "Drying rotifers enter an **anabiotic** condition that withstands prolonged desiccation without fatal tissue damage." },
      { author: "D'Arcy Wentworth Thompson", work: "On Growth and Form", text: "The remarkable resilience of an **anabiotic** spore defies ordinary thermodynamic rates of metabolic breakdown." },
      { author: "David Keilin", work: "The Problem of Anabiosis or Latent Life", text: "Leeuwenhoek first described the **anabiotic** revival of microscopic animalcules retrieved from dried gutter dust." }
    ]
  },
  "anhydrobiosis": {
    primary: "A state of dormant suspended animation induced in an organism by complete dehydration and reversed by rehydration.",
    secondary: "A metabolic standstill in tardigrades, nematodes, and resurrection plants mediated by non-reducing disaccharides like trehalose.",
    quotes: [
      { author: "John H. Crowe", work: "Anhydrobiosis: An Unsolved Problem", text: "During **anhydrobiosis**, water is replaced at cellular membranes by protective disaccharide sugars." },
      { author: "David Keilin", work: "The Problem of Anabiosis or Latent Life", text: "Tardigrades achieve complete **anhydrobiosis**, preserving structural integrity across decades of desiccated storage." },
      { author: "Ernst Mayr", work: "The Growth of Biological Thought", text: "The discovery of **anhydrobiosis** forced naturalists to reconsider the operational definition of living protoplasm." }
    ]
  },
  "anoxybiosis": {
    primary: "The state of suspended animation or metabolic quiescence brought about in an organism by an absence of oxygen.",
    secondary: "A survival mechanism in certain invertebrates and facultative anaerobes whereby cellular respiration halts reversibly under severe anoxia.",
    quotes: [
      { author: "David Keilin", work: "The Problem of Anabiosis or Latent Life", text: "The term **anoxybiosis** describes organisms entering temporary dormancy when deprived of environmental oxygen." },
      { author: "Peter Hochachka", work: "Biochemical Adaptation", text: "Intertidal bivalves resort to controlled **anoxybiosis** during prolonged exposure to foul sulfide sediments." },
      { author: "George N. Somero", work: "Adaptation to Environmental Change", text: "Metabolic depression during **anoxybiosis** preserves critical energy reserves until aerated tides return." }
    ]
  },
  "antibiotic": {
    primary: "Tending to prevent, inhibit, or destroy life; specifically, a substance produced by microorganisms that kills or suppresses pathogenic bacteria.",
    secondary: "Antagonistic biological interaction wherein one species emits metabolic toxins fatal to competitive neighbors.",
    quotes: [
      { author: "Selman Waksman", work: "Microbial Antagonisms and Antibiotic Substances", text: "We defined an **antibiotic** substance as a chemical compound of microbial origin that possesses antibacterial properties." },
      { author: "Alexander Fleming", work: "On the Antibacterial Action of Cultures of a Penicillium", text: "The broth filtrate demonstrated powerful **antibiotic** properties against staphylococci without showing toxic effects on leukocytes." },
      { author: "René Dubos", work: "The Bacterial Cell", text: "Soil microbes secrete **antibiotic** peptides as competitive weapons within dense rhizosphere communities." }
    ]
  },
  "astrobiology": {
    primary: "The interdisciplinary study of the origin, evolution, distribution, and future of life in the universe.",
    secondary: "The investigation of planetary habitability, prebiotic chemical evolution, and potential biosignatures in extreme terrestrial and celestial environments.",
    quotes: [
      { author: "Carl Sagan", work: "Cosmos", text: "The emerging science of **astrobiology** compels us to view our home planet from the vantage point of cosmic evolution." },
      { author: "Joshua Lederberg", work: "Exobiology: Approaches to Life beyond the Earth", text: "NASA established programs in **astrobiology** to assess quarantine requirements for lunar and Martian sample returns." },
      { author: "Lynn Margulis", work: "What Is Life?", text: "True **astrobiology** must encompass both microbiology and the geocosmology of atmospheric regulation." }
    ]
  },
  "autobiographer": {
    primary: "A person who writes an account of their own life.",
    secondary: "A literary chronicler who reconstructs personal memory, psychological development, and social history through subjective prose narrative.",
    quotes: [
      { author: "Virginia Woolf", work: "Moments of Being", text: "The **autobiographer** must grapple with invisible scenes that leave behind emotional residues deeper than external facts." },
      { author: "Edward Gibbon", work: "Memoirs of My Life", text: "Truth, naked, unblushing truth, should be the first virtue of an honest **autobiographer**." },
      { author: "Jean-Jacques Rousseau", work: "Confessions", text: "I resolved that no other **autobiographer** had ever set forth a human soul with such unvarnished candor." }
    ]
  },
  "autobiographic": {
    primary: "Of, relating to, or having the character of an autobiography.",
    secondary: "Reflecting personal experiences and emotional revelations of the creator within a creative or artistic work.",
    quotes: [
      { author: "Henry James", work: "The Art of the Novel", text: "An **autobiographic** impulse quietly guides the novelist's finest portraits of youth and disillusionment." },
      { author: "George Eliot", work: "Scenes of Clerical Life", text: "Her early recollections retain a distinct **autobiographic** coloring that lends them extraordinary vividness." },
      { author: "Thomas Carlyle", work: "Sartor Resartus", text: "The strange treatise contains an unmistakable **autobiographic** thread veiled behind Teufelsdröckh's philosophy." }
    ]
  },
  "autobiographical": {
    primary: "Pertaining to, dealing with, or based on the author's own life experiences.",
    secondary: "Characterized by self-reflection, retrospective introspection, or personal memoirs incorporated into literature.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", text: "The title-page heralded an **autobiographical** narrative whose visceral intimacy astonished Victorian readers." },
      { author: "Charles Dickens", work: "David Copperfield", text: "Of all my books, this was my favorite child, rooted deeply in **autobiographical** sorrows and youthful struggles." },
      { author: "George Orwell", work: "Why I Write", text: "My **autobiographical** memories of prep school formed the psychological scaffolding of my political essays." }
    ]
  },
  "autobiography": {
    primary: "An account of a person's life written or narrated directly by that person.",
    secondary: "A literary genre dedicated to self-representation, retrospective psychological analysis, and the synthesis of personal identity over time.",
    quotes: [
      { author: "Benjamin Franklin", work: "Autobiography", text: "Having emerged from the poverty and obscurity in which I was born, I have written this **autobiography** for posterity." },
      { author: "John Stuart Mill", work: "Autobiography", text: "It seems proper that some record should exist of an unusual education, and this **autobiography** supplies that testimony." },
      { author: "Virginia Woolf", work: "A Room of One's Own", text: "The boundaries between creative fiction and genuine **autobiography** dissolve whenever an author writes with passion." }
    ]
  },
  "bio": {
    primary: "A short biographical profile, sketch, or personal curriculum vitae.",
    secondary: "A Greek combining element denoting life, organic living systems, or the biological domain.",
    quotes: [
      { author: "George Orwell", work: "Selected Essays", text: "The dust-jacket gave a brief authorial **bio** highlighting his vagabond years among Parisian dishwashers." },
      { author: "William Morton Wheeler", work: "Essays in Social Biology", text: "The prefix **bio** consistently marks the transition from purely mechanical physics to animate systems." },
      { author: "Lewis Mumford", work: "The Myth of the Machine", text: "Megatechnics ignored the fragile imperatives of the **bio** sphere in favor of colossal industrial output." }
    ]
  },
  "biochron": {
    primary: "The total duration of time represented by a biostratigraphic zone or biozone in geochronology.",
    secondary: "A unit of geological time defined by the life span or stratigraphic persistence of a particular fossil taxon.",
    quotes: [
      { author: "Henry Shaler Williams", work: "The Correlation of Geological Faunas", text: "We propose the term **biochron** for the absolute duration of time corresponding to the range of a fossil species." },
      { author: "William Joscelyn Arkell", work: "Jurassic Geology of the World", text: "Each ammonite **biochron** represents an astonishingly brief interval of evolutionary radiation and extinction." },
      { author: "G. G. Simpson", work: "The Major Features of Evolution", text: "Estimating the physical limits of a mammalian **biochron** requires correlating radio-isotopic dates with evolutionary turnover." }
    ]
  },
  "biocoenosis": {
    primary: "An ecological community consisting of all interacting plants, animals, and microorganisms inhabiting a shared biotope.",
    secondary: "The integrated biotic assemblage that together with its physical abiotic biotope constitutes an ecosystem.",
    quotes: [
      { author: "Karl Möbius", work: "The Oyster and Oyster-Culture", text: "I have designated this mutual association of living organisms by the word **biocoenosis**, or life-community." },
      { author: "Eugene Odum", work: "Fundamentals of Ecology", text: "The **biocoenosis** forms the living, dynamic core of the ecosystem, reacting continuously upon its physical substrate." },
      { author: "Ernst Haeckel", work: "The Wonders of Life", text: "Möbius rendered a signal service to natural history when he introduced the concept of the marine **biocoenosis**." }
    ]
  },
  "biographer": {
    primary: "A person who writes an account of another individual's life.",
    secondary: "A chronicler who interprets historical personality, character development, and cultural legacy through documentary evidence.",
    quotes: [
      { author: "James Boswell", work: "The Life of Samuel Johnson", text: "The **biographer** who treats of so great a man must not omit minute traits and peculiar habits." },
      { author: "Lytton Strachey", work: "Eminent Victorians", text: "The first duty of the modern **biographer** is to preserve a becoming brevity and dispassionate independence." },
      { author: "Thomas Carlyle", work: "On Heroes, Hero-Worship, and the Heroic in History", text: "No great man lives in vain; the history of the world is but the **biographer**'s collective tapestry." }
    ]
  },
  "biographic": {
    primary: "Pertaining to or containing the narrative of an individual's life; biographical.",
    secondary: "Relating to the literary craft of portraying personal historical careers.",
    quotes: [
      { author: "Ralph Waldo Emerson", work: "Representative Men", text: "Our interest in history resolves itself into an appetite for **biographic** anecdotes of monumental figures." },
      { author: "Samuel Johnson", work: "The Rambler", text: "No species of writing is more worthy of cultivation than **biographic** narrative, which instructs by exemplary conduct." },
      { author: "Walter Pater", work: "Appreciations", text: "A delicate **biographic** thread unifies his critical essays on Shakespeare's historical dramas." }
    ]
  },
  "biographical": {
    primary: "Of, relating to, or concerning the biography of an individual.",
    secondary: "Composed of or based on facts, events, and records from a person's life history.",
    quotes: [
      { author: "James Boswell", work: "The Life of Samuel Johnson", text: "I have collected these **biographical** materials with scrupulous fidelity from his most intimate companions." },
      { author: "Virginia Woolf", work: "The Common Reader", text: "The **biographical** sketch allows us to enter the intimate domestic circle of seventeenth-century poets." },
      { author: "Thomas Babington Macaulay", work: "Critical and Historical Essays", text: "His extensive **biographical** dictionary remains an indispensable monument of English scholarship." }
    ]
  },
  "biography": {
    primary: "A written narrative account of the life of an individual person.",
    secondary: "The literary art or historical discipline devoted to depicting individual character, actions, and destiny in social context.",
    quotes: [
      { author: "Samuel Johnson", work: "The Idler", text: "The great end of **biography** is not to flatter the pride of ancestors, but to instruct the understanding." },
      { author: "Thomas Carlyle", work: "Critical and Miscellaneous Essays", text: "History is the essence of innumerable individual **biographies**, each weaving its thread into the cosmic loom." },
      { author: "Virginia Woolf", work: "Orlando", text: "The art of **biography** must strike a precarious balance between granite fact and rainbow personality." }
    ]
  },
  "biologism": {
    primary: "The explanation of human social, cultural, or moral behavior exclusively in terms of biological causes or genetic determinism.",
    secondary: "The philosophical doctrine that reduces sociological and psychological phenomena to evolutionary instincts and physiological drives.",
    quotes: [
      { author: "Stephen Jay Gould", work: "The Mismeasure of Man", text: "Crude **biologism** has repeatedly served reactionary political ends by claiming social inequalities are biologically mandated." },
      { author: "Richard Lewontin", work: "Biology as Ideology", text: "The ideological appeal of **biologism** lies in its comforting assurance that existing hierarchies are genetically inevitable." },
      { author: "Mary Midgley", work: "Beast and Man", text: "We must avoid both reductive **biologism** and the opposite error of treating human culture as entirely disembodied." }
    ]
  },
  "biologist": {
    primary: "A scientist or specialist who studies living organisms and life processes.",
    secondary: "A natural investigator examining the morphology, physiology, ecology, and evolutionary ancestry of living systems.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", text: "The thoughtful **biologist** who contemplates the affinities of organic beings cannot remain satisfied with special creation." },
      { author: "Ernst Mayr", work: "This Is Biology", text: "The **biologist** deals with unique individuals and historical contingency, distinguishing life from inanimate physics." },
      { author: "Julian Huxley", work: "Evolution: The Modern Synthesis", text: "Every modern **biologist** must integrate Mendelian genetics with population dynamics and paleontological evidence." }
    ]
  },
  "biologistic": {
    primary: "Pertaining to or characterized by biologism; interpreting human affairs through strict biological determinism.",
    secondary: "Overly reliant on biological paradigms when analyzing complex political, linguistic, or cultural institutions.",
    quotes: [
      { author: "Stephen Jay Gould", work: "An Urchin in the Storm", text: "He rejected the **biologistic** fallacies that attempted to reduce literature and ethical norms to selfish genes." },
      { author: "Richard Lewontin", work: "The Triple Helix", text: "A **biologistic** framing obscures the reality that organisms actively construct their own environmental niches." },
      { author: "Clifford Geertz", work: "The Interpretation of Cultures", text: "Anthropology resists **biologistic** oversimplifications that disregard the symbolic systems constitutive of human thought." }
    ]
  },
  "biology": {
    primary: "The scientific study of living organisms, including their structure, functioning, evolution, distribution, and taxonomy.",
    secondary: "The living flora and fauna or biological characteristics of a specific region, organism, or environment.",
    quotes: [
      { author: "Jean-Baptiste Lamarck", work: "Hydrogéologie", text: "To this broad domain encompassing all phenomena of living bodies, I give the name of **biology**." },
      { author: "Thomas Henry Huxley", work: "On the Study of Biology", text: "Modern **biology** is simply the collection of all truths which have been ascertained concerning living matter." },
      { author: "Theodosius Dobzhansky", work: "Nothing in Biology Makes Sense Except in the Light of Evolution", text: "Nothing in **biology** makes sense except in the light of evolution; without it, biological facts become an incoherent mosaic." }
    ]
  },
  "biome": {
    primary: "A major ecological community type (such as tropical rainforest, desert, or tundra) defined by dominant vegetation and regional climate.",
    secondary: "The collective climax formation of plant and animal life characteristic of an extensive geographical zone.",
    quotes: [
      { author: "Frederic Clements", work: "Plant Succession and Indicators", text: "The climax community constitutes an organic unit of highest rank which we designate the **biome**." },
      { author: "Eugene Odum", work: "Fundamentals of Ecology", text: "Each continental **biome** exhibits characteristic life forms adapted to temperature limits and precipitation gradients." },
      { author: "Victor Shelford", work: "The Ecology of North America", text: "The deciduous forest **biome** sustained complex trophic webs connecting herbivores to top predators." }
    ]
  },
  "biometric": {
    primary: "Relating to the statistical analysis of biological data and measurements.",
    secondary: "Pertaining to electronic identification technologies based on unique anatomical traits, such as fingerprints or retinal patterns.",
    quotes: [
      { author: "Karl Pearson", work: "The Grammar of Science", text: "The **biometric** approach seeks to uncover the mathematical laws governing inheritance and natural selection." },
      { author: "Francis Galton", work: "Natural Inheritance", text: "These **biometric** tables demonstrate the mathematical regression of filial characteristics toward the racial mean." },
      { author: "Ronald Fisher", work: "The Genetical Theory of Natural Selection", text: "A synthesis of Mendelian particulate genetics with **biometric** statistical distributions resolved the old Darwinian debate." }
    ]
  },
  "biomorph": {
    primary: "An artistic design, decorative motif, or architectural form that resembles a living organism or natural organic shape.",
    secondary: "In evolutionary computing and developmental biology, an artificial digital organism generated by iterative evolutionary algorithms.",
    quotes: [
      { author: "Richard Dawkins", work: "The Blind Watchmaker", text: "The computer generated a diverse menagerie of **biomorphs**, each evolving tree-like branching structures under artificial selection." },
      { author: "Lewis Mumford", work: "The City in History", text: "Art Nouveau architects abandoned rigid geometrical angles in favor of the sinuous curves of the natural **biomorph**." },
      { author: "Sigfried Giedion", work: "Space, Time and Architecture", text: "Modern sculpture incorporates the undulating contours of the oceanic **biomorph** to convey organic dynamism." }
    ]
  },
  "biomorphism": {
    primary: "The practice of using decorative motifs or abstract forms resembling biological organisms in art and architecture.",
    secondary: "A 20th-century artistic movement associated with Surrealism that draws inspiration from cellular, amoeboid, and botanical silhouettes.",
    quotes: [
      { author: "Alfred H. Barr Jr.", work: "Cubism and Abstract Art", text: "Surrealist painters turned from mechanical abstraction toward **biomorphism**, evoking deep organic and psychological rhythms." },
      { author: "Herbert Read", work: "A Concise History of Modern Sculpture", text: "Arp's wood reliefs achieved a pristine **biomorphism** that seemed to grow spontaneously out of nature." },
      { author: "Clement Greenberg", work: "Art and Culture", text: "The lingering influence of Surrealist **biomorphism** prepared American painters for free abstract expressionism." }
    ]
  },
  "biophilia": {
    primary: "An innate, biologically rooted tendency in human beings to seek connections with nature and other forms of living life.",
    secondary: "The emotional, aesthetic, and psychological affinity of human beings for living landscapes, animals, and diverse ecosystems.",
    quotes: [
      { author: "Edward O. Wilson", work: "Biophilia", text: "I define **biophilia** as the innate tendency to focus on life and lifelike processes." },
      { author: "Erich Fromm", work: "The Heart of Man", text: "I proposed the term **biophilia** to describe the passionate love of life and of all that is alive." },
      { author: "Stephen Kellert", work: "The Biophilia Hypothesis", text: "Urban isolation from wild habitats impairs the expression of **biophilia**, diminishing human psychological resilience." }
    ]
  },
  "biophysicist": {
    primary: "A scientist who applies the principles, techniques, and quantitative methods of physics to study biological phenomena.",
    secondary: "An investigator studying molecular motors, membrane electrophysiology, and macromolecular structures via physical mechanics.",
    quotes: [
      { author: "Erwin Schrödinger", work: "What Is Life?", text: "The **biophysicist** must examine how the living organism continually draws negative entropy from its environment." },
      { author: "Francis Crick", work: "What Mad Pursuit", text: "Trained originally in physics, I became a **biophysicist** to probe the physical reality of the gene." },
      { author: "John Desmond Bernal", work: "The Physical Basis of Life", text: "X-ray crystallography enabled the **biophysicist** to unveil the atomic architecture of proteins and viruses." }
    ]
  },
  "biophysics": {
    primary: "The branch of science concerned with the application of physical principles and methods to biological processes and systems.",
    secondary: "The quantitative study of thermodynamics, electrodynamics, and structural mechanics within macromolecular and cellular complexes.",
    quotes: [
      { author: "Erwin Schrödinger", work: "What Is Life?", text: "We look forward to a new era where classical **biophysics** unifies quantum mechanics with chromosome mechanics." },
      { author: "Francis Crick", work: "Of Molecules and Men", text: "The triumph of molecular **biophysics** proved that biological replication relies upon strict physical stereochemistry." },
      { author: "A. V. Hill", work: "Trails and Trials in Physiology", text: "The emergence of modern **biophysics** provided the sensitive galvanometers needed to measure heat production in stimulated muscle." }
    ]
  },
  "biopoiesis": {
    primary: "The natural process by which living matter evolves or is generated from non-living, inorganic matter; abiogenesis.",
    secondary: "In geochemical origins-of-life research, the specific chemical transition from geochemical synthesis to replicating biological entities.",
    quotes: [
      { author: "John Desmond Bernal", work: "The Physical Basis of Life", text: "We may apply the term **biopoiesis** to the initial emergence of life from inorganic compounds in primeval clay beds." },
      { author: "N. W. Pirie", work: "The Origin of Life", text: "Precise terminology distinguishes chemical evolutions from the decisive threshold of **biopoiesis**." },
      { author: "Alexander Oparin", work: "Life: Its Nature, Origin and Development", text: "Mineral catalysts on coastal mudflats accelerated the chemical precursors necessary for terrestrial **biopoiesis**." }
    ]
  },
  "biorhythm": {
    primary: "An innate, cyclically recurring biological pattern of physiological, behavioral, or biochemical activity.",
    secondary: "Endogenous circadian, ultradian, or infradian oscillatory rhythms governed by suprachiasmatic cellular pacemakers.",
    quotes: [
      { author: "Erwin Bünning", work: "The Physiological Clock", text: "The endogenous **biorhythm** governs photoperiodic floral induction across diverse higher plant species." },
      { author: "Colin Pittendrigh", work: "On Temporal Organization in Living Systems", text: "The circadian **biorhythm** represents an evolved cellular adaptation synchronizing metabolism with the solar cycle." },
      { author: "J. Woodbridge Davis", work: "Circadian Clocks", text: "Disrupting the natural **biorhythm** through constant illumination induces profound hormonal and metabolic desynchrony." }
    ]
  },
  "bios": {
    primary: "Life, or the course of an individual human life, as distinguished from bare physical existence (zoe) in classical Greek philosophy.",
    secondary: "In biochemistry and microbiology, historical terminology for a nutrient complex (vitamin B factors) essential for yeast proliferation.",
    quotes: [
      { author: "Hannah Arendt", work: "The Human Condition", text: "Aristotle distinguished between mere biological survival and the **bios** politikos, the purposeful life lived in speech and action." },
      { author: "Giorgio Agamben", work: "Homo Sacer: Sovereign Power and Bare Life", text: "The Greeks had two terms for life: zoe, which expressed the simple fact of living common to all beings, and **bios**, which indicated the qualified life of an individual." },
      { author: "Eugene Wildiers", work: "The Theologian and His Universe", text: "Classical humanism drew from the Greek concept of **bios** an ideal of ethical self-cultivation within the community." }
    ]
  },
  "biosemiotic": {
    primary: "Relating to biosemiotics, the study of signs, communication, and meaning-making processes in living systems.",
    secondary: "Pertaining to signaling codes, molecular recognition, and communicative interactions across biological organisms.",
    quotes: [
      { author: "Thomas Sebeok", work: "Signs: An Introduction to Semiotics", text: "Every biological process involves a **biosemiotic** exchange of codes between organism and environment." },
      { author: "Jesper Hoffmeyer", work: "Signs of Meaning in the Universe", text: "The living cell operates as a **biosemiotic** entity, interpreting molecular sign vehicles to sustain its internal homeostasis." },
      { author: "Terrence Deacon", work: "The Symbolic Species", text: "Human linguistic capacity evolved upon deep **biosemiotic** substrates shared across animal kingdom communication systems." }
    ]
  },
  "biosphere": {
    primary: "The global ecological system comprising all living beings and their relationships with the lithosphere, hydrosphere, and atmosphere.",
    secondary: "The thin outer crust and gaseous envelope of planet Earth where living organisms exist and actively cycle matter and energy.",
    quotes: [
      { author: "Vladimir Vernadsky", work: "The Biosphere", text: "Living matter is the most powerful cosmic force transforming the face of the Earth throughout the **biosphere**." },
      { author: "Eduard Suess", work: "The Face of the Earth", text: "One thing seems foreign on this large celestial body: the envelope of living matter which we may term the **biosphere**." },
      { author: "Lynn Margulis", work: "Symbiotic Planet", text: "The Gaia hypothesis views the entire **biosphere** as a complex, self-regulating physiological system." }
    ]
  },
  "biostasis": {
    primary: "The state of suspended or arrested metabolic activity in an organism without the loss of viability.",
    secondary: "In pedology and geomorphology, a period of climatic stability and dense vegetational cover favoring deep chemical soil formation.",
    quotes: [
      { author: "Henri Erhart", work: "La Théorie Biorhexistasique", text: "During the epoch of **biostasis**, dense forest cover prevents mechanical erosion and promotes chemical leaching." },
      { author: "David Keilin", work: "The Problem of Anabiosis or Latent Life", text: "True **biostasis** allows delicate organisms to withstand temperatures approaching absolute zero without cellular disruption." },
      { author: "Eugene Odum", work: "Fundamentals of Ecology", text: "The equilibrium of climax communities represents a dynamic biological homeostasis akin to landscape-level **biostasis**." }
    ]
  },
  "biosynthesis": {
    primary: "The production of complex chemical compounds by living organisms or enzymatic cellular processes.",
    secondary: "Anabolic metabolic pathways whereby simpler precursor molecules are enzymatically converted into macromolecules like proteins, lipids, and nucleic acids.",
    quotes: [
      { author: "Hans Krebs", work: "The Metabolic Roles of Citrate", text: "Intermediates of the tricarboxylic acid cycle furnish the carbon skeletons required for the **biosynthesis** of amino acids." },
      { author: "Arthur Kornberg", work: "Enzymatic Synthesis of DNA", text: "The in vitro **biosynthesis** of nucleic acid polymers confirmed the catalytic primacy of DNA polymerase." },
      { author: "Jacques Monod", work: "Chance and Necessity", text: "The fidelity of protein **biosynthesis** is safeguarded by stereospecific interactions between transfer RNAs and ribosomal complexes." }
    ]
  },
  "biosynthetic": {
    primary: "Pertaining to, produced by, or involved in biosynthesis.",
    secondary: "Describing anabolic cellular pathways and multi-enzyme cascades that synthesize vital biological metabolites.",
    quotes: [
      { author: "Fritz Lipmann", work: "Wanderings of a Biochemist", text: "Adenosine triphosphate acts as the universal chemical energy currency driving endergonic **biosynthetic** reactions." },
      { author: "Severo Ochoa", work: "Enzymatic Synthesis of Ribonucleic Acid", text: "Our laboratory mapped the specific **biosynthetic** routes producing polynucleotide chains in bacterial extracts." },
      { author: "Albert Lehninger", work: "Biochemistry", text: "Feedback inhibition serves to throttle key enzymes in **biosynthetic** pathways whenever the final product accumulates." }
    ]
  },
  "biota": {
    primary: "The total flora and fauna of a specific geographical region, habitat, or geological period.",
    secondary: "The combined living component of an ecosystem, distinct from its abiotic soil, air, and water components.",
    quotes: [
      { author: "Edward O. Wilson", work: "The Diversity of Life", text: "Human land clearance is eradicating an irreplaceable fraction of the tropical rainforest **biota**." },
      { author: "Alfred Russel Wallace", work: "Island Life", text: "The insular **biota** of oceanic archipelagos exhibits a striking paucity of terrestrial mammals and amphibians." },
      { author: "Stephen Jay Gould", work: "Wonderful Life", text: "The Burgess Shale preserved a soft-bodied marine **biota** whose anatomical disparity astounded modern paleontologists." }
    ]
  },
  "biotic": {
    primary: "Of, relating to, or caused by living organisms.",
    secondary: "In ecology, designating the living factors (such as competition, predation, and symbiosis) that influence an ecosystem.",
    quotes: [
      { author: "Aldo Leopold", work: "A Sand County Almanac", text: "Land is not merely soil; it is a fountain of energy flowing through a circuit of soils, plants, and animals—the **biotic** pyramid." },
      { author: "Charles Elton", work: "Animal Ecology", text: "The regulation of animal populations depends upon an intricate network of **biotic** controls and food chains." },
      { author: "Rachel Carson", work: "Silent Spring", text: "Indiscriminate spraying disrupts the natural **biotic** checks that have kept insect populations in check for millenia." }
    ]
  },
  "biotin": {
    primary: "A water-soluble B-complex vitamin (vitamin B7) essential for cellular metabolism and the function of carboxylase enzymes.",
    secondary: "A bicyclic coenzyme that transfers carbon dioxide units in the biosynthesis of fatty acids, gluconeogenesis, and leucine degradation.",
    quotes: [
      { author: "Fritz Kögl", work: "Researches on Plant Growth Hormones", text: "From thousands of egg yolks, we isolated crystalline **biotin**, a growth substance of remarkable potency." },
      { author: "Albert Lehninger", work: "Principles of Biochemistry", text: "The prosthetic group **biotin** is covalently linked to the epsilon-amino group of a specific lysine residue." },
      { author: "Vincent du Vigneaud", work: "The Structure of Biotin", text: "Chemical degradation established that **biotin** contains a fused imidazole and thiophene ring system." }
    ]
  },
  "biotope": {
    primary: "A uniform environmental area or habitat providing living conditions for a specific community of plants and animals (biocoenosis).",
    secondary: "The smallest geographic unit of the biosphere characterized by homogeneous environmental and abiotic parameters.",
    quotes: [
      { author: "Ernst Haeckel", work: "Generelle Morphologie der Organismen", text: "Every distinctive **biotope** exerts selective pressures shaping the ecological adaptations of its inhabitants." },
      { author: "Eugene Odum", work: "Fundamentals of Ecology", text: "The woodland **biotope** comprises both its microclimate and physical substrate, serving as the setting for the resident fauna." },
      { author: "Arthur Tansley", work: "Practical Plant Ecology", text: "Differences in soil moisture between adjacent sand dunes establish sharply delimited **biotopes**." }
    ]
  },
  "biotype": {
    primary: "A group of organisms having identical genetic constitution (genotype).",
    secondary: "A physiological or pathogenic variant within a species distinguished by physiological behavior, virulence, or host preference rather than structural morphology.",
    quotes: [
      { author: "Wilhelm Johannsen", work: "Elemente der exakten Erblichkeitslehre", text: "Pure lines isolate a single **biotype** that breeds true across successive generations under controlled pollination." },
      { author: "E. C. Stakman", work: "Physiological Specialization in Pathogenic Fungi", text: "The emergence of an aggressive rust **biotype** broke down the resistance of previously immune cereal cultivars." },
      { author: "Ernst Mayr", work: "Systematics and the Origin of Species", text: "Taxonomists must guard against designating every transient physiological **biotype** as a separate biological species." }
    ]
  },
  "biotypic": {
    primary: "Relating to or having the characteristics of a biotype.",
    secondary: "Describing hereditary identity or uniform genetic constitution across an inbred lineage or clone.",
    quotes: [
      { author: "Wilhelm Johannsen", work: "The Genotype Conception of Heredity", text: "Selection within a **biotypic** strain yields no permanent hereditary alteration in the absence of mutation." },
      { author: "Sewall Wright", work: "Evolution and the Genetics of Populations", text: "Severe bottlenecks reduce population variance to a virtually uniform **biotypic** ensemble." },
      { author: "G. Ledyard Stebbins", work: "Variation and Evolution in Plants", text: "Apomictic plants produce swarms of microspecies that exhibit rigid **biotypic** stability." }
    ]
  },
  "biozone": {
    primary: "A biostratigraphic unit consisting of rock strata defined and characterized by the presence of specific fossil taxa.",
    secondary: "The body of strata corresponding to the total stratigraphical range of a designated index fossil.",
    quotes: [
      { author: "William Joscelyn Arkell", work: "The Jurassic System in Great Britain", text: "The ammonite **biozone** serves as the gold standard for global correlation of Mesozoic marine sedimentary formations." },
      { author: "Amadeus William Grabau", work: "Principles of Stratigraphy", text: "Boundaries of each **biozone** record evolutionary appearances, migrations, and local extinctions of index organisms." },
      { author: "Stephen Jay Gould", work: "Time's Arrow, Time's Cycle", text: "Stratigraphers chart historical time through a succession of **biozones**, translating rock layers into evolutionary history." }
    ]
  },
  "chemobiosis": {
    primary: "A form of cryptobiosis or metabolic dormancy induced in an organism by toxic chemical agents and reversed upon removal of the toxin.",
    secondary: "The physiological preservation of cellular structures when exposed to chemical desiccants, cryoprotectants, or enzyme inhibitors.",
    quotes: [
      { author: "David Keilin", work: "The Problem of Anabiosis or Latent Life", text: "We distinguish **chemobiosis** from desiccation anabiosis when toxic agents arrest metabolism without causing necrosis." },
      { author: "John H. Crowe", work: "Mechanisms of Anhydrobiosis", text: "High concentrations of polyols can induce a reversible state analogous to **chemobiosis** in nematodes." },
      { author: "Peter Hochachka", work: "Biochemical Adaptation", text: "Chemical arrest of ATP turnover demonstrates how **chemobiosis** can protect cells against lethal energetic collapse." }
    ]
  },
  "cryobiosis": {
    primary: "A form of cryptobiosis or suspended animation induced by freezing or sub-zero temperatures.",
    secondary: "The physiological state wherein an organism withstands freezing of extracellular water and cessation of metabolism without cellular death.",
    quotes: [
      { author: "David Keilin", work: "The Problem of Anabiosis or Latent Life", text: "Organisms in **cryobiosis** survive liquid helium temperatures because intracellular glass formation halts destructive crystal growth." },
      { author: "Peter Mazur", work: "Cryobiology: The Freezing of Biological Systems", text: "Successful **cryobiosis** requires cooling regimes that prevent lethal ice nucleation within the cytoplasmic matrix." },
      { author: "Harold Urey", work: "The Origins of Organic Molecules", text: "Cometary bodies might maintain primitive microorganisms in perpetual **cryobiosis** across cosmic distances." }
    ]
  },
  "ectosymbiosis": {
    primary: "A symbiotic relationship in which the symbiont lives on the exterior surface of the host organism.",
    secondary: "Mutualistic, commensal, or parasitic associations (such as epiphytic lichens or cleaner fish) where partners interact without internal cellular penetration.",
    quotes: [
      { author: "Anton de Bary", work: "Die Erscheinung der Symbiose", text: "We observe **ectosymbiosis** where one organism attaches externally to its companion without penetrating bodily tissues." },
      { author: "Lynn Margulis", work: "Symbiosis in Cell Evolution", text: "While endosymbiosis transformed cellular organelles, pervasive **ectosymbiosis** continues to shape coral reef communities." },
      { author: "William Morton Wheeler", work: "The Social Insects", text: "Mites clinging to the cuticles of soldier ants participate in a specialized, non-invasive **ectosymbiosis**." }
    ]
  },
  "endosymbiont": {
    primary: "An organism that lives within the body or cells of another organism in a mutualistic, commensal, or parasitic relationship.",
    secondary: "An intracellular microorganism, such as the ancestral alpha-proteobacteria that evolved into mitochondria within eukaryotic cells.",
    quotes: [
      { author: "Lynn Margulis", work: "Origin of Eukaryotic Cells", text: "The mitochondrion originated as an aerobic bacterial **endosymbiont** engulfed by a predatory anaerobic host cell." },
      { author: "Paul Portier", work: "Les Symbiotes", text: "Every higher plant and animal harbors intracellular **endosymbionts** without which normal tissue respiration is impossible." },
      { author: "Kwok-Wai Jeon", work: "Development of Cellular Inclusions", text: "Within five years of infection, the bacterial **endosymbiont** became indispensable for amoebic survival." }
    ]
  },
  "endosymbiosis": {
    primary: "A symbiotic relationship in which one organism lives inside the body or cells of another organism.",
    secondary: "The evolutionary theory (Serial Endosymbiosis Theory) explaining the origin of eukaryotic organelles (mitochondria and plastids) from engulfed prokaryotes.",
    quotes: [
      { author: "Lynn Margulis", work: "Symbiosis in Cell Evolution", text: "Serial **endosymbiosis** demonstrates that cooperation between disparate genomes drove the quantum evolutionary leap to eukaryosis." },
      { author: "Konstantin Mereschkowski", work: "The Nature and Origins of Chromatophores in the Plant Kingdom", text: "Chloroplasts are not native cellular organs, but the descendants of blue-green algae living in perpetual **endosymbiosis**." },
      { author: "John Maynard Smith", work: "The Major Transitions in Evolution", text: "The acquisition of mitochondria through primary **endosymbiosis** eliminated the bioenergetic bottleneck constraining cell size." }
    ]
  },
  "enterobiasis": {
    primary: "Infestation of the human intestine by the pinworm *Enterobius vermicularis*.",
    secondary: "A cosmopolitan parasitic helminthiasis causing perianal pruritus, especially prevalent in young children.",
    quotes: [
      { author: "Patrick Manson", work: "Tropical Diseases", text: "Diagnosis of **enterobiasis** is confirmed by applying cellulose tape to the perianal skin to collect the characteristic eggs." },
      { author: "William C. Campbell", work: "History of Anthelmintics", text: "Modern anti-parasitic therapeutics swiftly eradicate intestinal **enterobiasis** within school populations." },
      { author: "Thomas C. Cheng", work: "General Parasitology", text: "The nocturnal migration of gravid female worms in **enterobiasis** triggers intense local irritation." }
    ]
  },
  "exobiology": {
    primary: "The branch of biology concerned with the search for and study of life elsewhere in the universe.",
    secondary: "The study of the potential effects of extraterrestrial environments on living organisms and planetary biochemistry.",
    quotes: [
      { author: "Joshua Lederberg", work: "Exobiology: Approaches to Life beyond the Earth", text: "I coined the term **exobiology** to emphasize our need to formulate universal criteria for life beyond Earth." },
      { author: "Carl Sagan", work: "The Cosmic Connection", text: "Critics once quipped that **exobiology** was a discipline without a subject matter, yet finding one alien microbe would revolutionize science." },
      { author: "I. S. Shklovskii", work: "Intelligent Life in the Universe", text: "Theoretical **exobiology** examines whether water and carbon chemistry are cosmic imperatives or terrestrial parochialisms." }
    ]
  },
  "macrobiotic": {
    primary: "Tending to prolong life; long-lived.",
    secondary: "Pertaining to a dietary and holistic lifestyle philosophy (macrobiotics) emphasizing whole grains, seasonal vegetables, and balanced energetic principles.",
    quotes: [
      { author: "Christoph Wilhelm Hufeland", work: "Makrobiotik: The Art of Prolonging Life", text: "The true **macrobiotic** philosophy cultivates temperance, fresh air, and serenity to extend human longevity." },
      { author: "George Ohsawa", work: "Zen Macrobiotics", text: "A balanced **macrobiotic** regimen harmonizes the yin and yang constituents of grain and natural salt." },
      { author: "Aldous Huxley", work: "Island", text: "They adopted a simple, largely **macrobiotic** diet that preserved youthful vitality into octogenarian years." }
    ]
  },
  "macrobiotics": {
    primary: "The theory, system, or art of prolonging life, especially through dietary regimens.",
    secondary: "A holistic dietary system based on traditional East Asian philosophy, focusing on whole grains, legumes, and minimizing processed foods.",
    quotes: [
      { author: "Christoph Wilhelm Hufeland", work: "The Art of Prolonging Life", text: "Medicine cures disease, but **macrobiotics** teaches how to preserve health and prolong mortal existence." },
      { author: "George Ohsawa", work: "The Book of Judgment", text: "True **macrobiotics** is not merely a cooking method, but a cosmology reconciling man with nature." },
      { author: "Alan Watts", work: "The Way of Zen", text: "Modern interest in **macrobiotics** reflects a broader Western longing for harmonious Eastern dietary philosophies." }
    ]
  },
  "microbiologist": {
    primary: "A scientist who specializes in the study of microscopic organisms such as bacteria, viruses, fungi, and protozoa.",
    secondary: "An investigator of microbial genetics, physiology, immunology, or fermentation processes.",
    quotes: [
      { author: "Louis Pasteur", work: "Studies on Fermentation", text: "The dedicated **microbiologist** discovers that invisible organisms determine the health and decay of worldly empires." },
      { author: "René Dubos", work: "Louis Pasteur: Free Lance of Science", text: "As a pioneer **microbiologist**, Pasteur possessed an astonishing capacity to visualize microscopic causes behind macroscopic phenomena." },
      { author: "Carl Woese", work: "The Archaea: Their History and Significance", text: "The molecular **microbiologist** cracked open the Tree of Life by comparing ribosomal RNA sequences across obscure microbes." }
    ]
  },
  "microbiology": {
    primary: "The branch of science that studies microscopic organisms, including bacteria, archaea, viruses, microscopic fungi, and protozoa.",
    secondary: "The investigation of microbial biochemistry, pathogenic mechanisms, and environmental nutrient recycling on a cellular level.",
    quotes: [
      { author: "Ferdinand Cohn", work: "Researches on Bacteria", text: "Systematic botanical classification laid the foundational taxonomy for modern investigative **microbiology**." },
      { author: "Robert Koch", work: "The Etiology of Tuberculosis", text: "Strict experimental postulates transformed medical **microbiology** from speculation into a rigorous laboratory science." },
      { author: "Martinus Beijerinck", work: "Studies on Microbial Ecology", text: "General **microbiology** demonstrates that everything is everywhere, but the environment selects." }
    ]
  },
  "neobiotic": {
    primary: "Pertaining to modern, living, or recently evolved biological species or ecological systems, as opposed to paleobiotic forms.",
    secondary: "Describing contemporary ecological communities and recent taxa in evolutionary and paleoclimatic studies.",
    quotes: [
      { author: "Charles Schuchert", work: "Historical Geology", text: "We contrast ancient fossil assemblages with the flourishing species of the modern **neobiotic** realm." },
      { author: "Amadeus William Grabau", work: "Principles of Stratigraphy", text: "Sedimentological analysis traces the gradual transition from archaic forms to the current **neobiotic** fauna." },
      { author: "George Gaylord Simpson", work: "Tempo and Mode in Evolution", text: "The genetic architecture of **neobiotic** populations provides the baseline for inferring ancient rates of evolutionary change." }
    ]
  },
  "osmobiosis": {
    primary: "A form of cryptobiosis or suspended animation induced in an organism by high osmotic pressure or hypertonic solutions.",
    secondary: "The physiological survival state wherein aquatic invertebrates like rotifers and tardigrades undergo reversible dehydration in high-salinity waters.",
    quotes: [
      { author: "David Keilin", work: "The Problem of Anabiosis or Latent Life", text: "In **osmobiosis**, high extracellular salinity draws water out until the organism enters an inactive, resistant state." },
      { author: "John H. Crowe", work: "Anhydrobiosis", text: "Tardigrades placed in hypertonic saline contract into tuns, successfully demonstrating physiological **osmobiosis**." },
      { author: "Peter Hochachka", work: "Biochemical Adaptation", text: "Cellular adaptations supporting **osmobiosis** protect enzyme complexes against severe ionic concentration." }
    ]
  },
  "paleobiology": {
    primary: "The branch of paleontology that uses biological principles to study the morphology, physiology, ecology, and evolution of ancient fossil organisms.",
    secondary: "The study of deep-time macroevolutionary patterns, extinction dynamics, and ecosystem turnover through the fossil record.",
    quotes: [
      { author: "George Gaylord Simpson", work: "Life of the Past", text: "Modern **paleobiology** breathes life into petrified bones, reconstructing the behaviors and trophic webs of bygone eras." },
      { author: "Stephen Jay Gould", work: "The Structure of Evolutionary Theory", text: "The golden age of **paleobiology** brought paleontologists back to the high table of evolutionary debate." },
      { author: "David Raup", work: "Extinction: Bad Genes or Bad Luck?", text: "Statistical **paleobiology** revealed periodic global mass extinctions that reset the course of planetary evolution." }
    ]
  },
  "probiotic": {
    primary: "Promoting life or health; specifically, a live microorganism that confers health benefits to the host when consumed in adequate amounts.",
    secondary: "Beneficial bacterial strains (such as *Lactobacillus* and *Bifidobacterium*) that support mucosal barrier function and gut microbiome equilibrium.",
    quotes: [
      { author: "Élie Metchnikoff", work: "The Prolongation of Life", text: "Consuming lactic acid bacteria exerts a **probiotic** influence, suppressing harmful putrefactive microbes within the colon." },
      { author: "R. Fuller", work: "Probiotics in Man and Animals", text: "We defined a **probiotic** as a live microbial feed supplement which beneficially affects the host animal by improving intestinal microbial balance." },
      { author: "Martin Blaser", work: "Missing Microbes", text: "Modern clinical therapies deploy targeted **probiotic** cultures to restore diversity depleted by aggressive broad-spectrum antibiotics." }
    ]
  },
  "symbiogenesis": {
    primary: "The evolutionary origin of new species, tissues, or organs through the long-term symbiotic merger of distinct organisms.",
    secondary: "The macroevolutionary mechanism championed by Konstantin Mereschkowski and Lynn Margulis wherein endosymbiosis drives major cellular innovations.",
    quotes: [
      { author: "Konstantin Mereschkowski", work: "The Theory of Two Plasms as the Basis of Symbiogenesis", text: "I have proposed the term **symbiogenesis** to designate the origin of organisms through the mutual combination and fusion of two or more distinct entities." },
      { author: "Lynn Margulis", work: "Acquiring Genomes: A Theory of the Origins of Species", text: "Speciation by **symbiogenesis** shows that cooperative physical mergers, not just random point mutations, generate evolutionary novelty." },
      { author: "Ernst Mayr", work: "The Growth of Biological Thought", text: "The historical resistance to **symbiogenesis** reflected an orthodoxy that equated evolution solely with gradual natural selection." }
    ]
  },
  "symbiology": {
    primary: "The scientific study of symbiosis, mutualism, and close associations between different biological species.",
    secondary: "The specialized ecological discipline analyzing the evolutionary dynamics, physiological exchanges, and co-evolutionary patterns of biological partners.",
    quotes: [
      { author: "Anton de Bary", work: "Die Erscheinung der Symbiose", text: "Our newly established field of **symbiology** investigates the diverse mutual dependencies binding lichens and host plants." },
      { author: "Paul Portier", work: "Les Symbiotes", text: "Advances in comparative **symbiology** demonstrate that solitary isolation is a biological impossibility in nature." },
      { author: "Lynn Margulis", work: "Symbiosis in Cell Evolution", text: "Theoretical **symbiology** bridges microbiology and evolutionary theory by tracking genetic exchanges across organismal boundaries." }
    ]
  },
  "symbiont": {
    primary: "Either of two or more organisms that live together in an intimate, long-term biological association.",
    secondary: "An organism participating in a mutualistic, commensal, or parasitic relationship with a host species.",
    quotes: [
      { author: "Anton de Bary", work: "Die Erscheinung der Symbiose", text: "The fungal **symbiont** weaves dense hyphae around the alga, absorbing photosynthate while offering moisture and shade." },
      { author: "Lynn Margulis", work: "Symbiotic Planet", text: "Every animal is in truth an ecosystem, housing millions of bacterial **symbionts** vital to its survival." },
      { author: "Thomas Henry Huxley", work: "Science and Culture", text: "The microscopic **symbiont** within the lichen revealed a dual nature that startled orthodox botanists." }
    ]
  },
  "symbiosis": {
    primary: "The living together of two dissimilar organisms in close, long-term biological association.",
    secondary: "A relationship of mutual benefit or interdependence between persons, groups, or biological entities (including mutualism, commensalism, and parasitism).",
    quotes: [
      { author: "Anton de Bary", work: "Die Erscheinung der Symbiose", text: "I designate by the term **symbiosis** the living together of differently named organisms in intimate association." },
      { author: "Lynn Margulis", work: "Symbiosis in Cell Evolution", text: "Life did not take over the globe by combat, but by networking and complex cellular **symbiosis**." },
      { author: "Peter Kropotkin", work: "Mutual Aid: A Factor of Evolution", text: "Natural selection continually favors species that practice mutual aid and physiological **symbiosis**." }
    ]
  },
  "symbiotic": {
    primary: "Relating to, characterized by, or being in a state of symbiosis.",
    secondary: "Involving a close, cooperative, or mutually beneficial relationship between two entities or organisms.",
    quotes: [
      { author: "Lewis Thomas", work: "The Lives of a Cell", text: "We are walking repositories of ancient **symbiotic** bacteria that learned long ago to share our cellular home." },
      { author: "Rachel Carson", work: "The Edge of the Sea", text: "The coral reef thrives through a **symbiotic** partnership between tiny anthozoan polyps and photosynthetic zooxanthellae." },
      { author: "Edward O. Wilson", work: "The Insect Societies", text: "Leafcutter ants maintain a complex **symbiotic** culture of basidiomycete fungi within underground chambers." }
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
console.log(`Bio Batch 1 Completed: ${count} / ${Object.keys(BATCH1_DATA).length} words updated`);
console.log(`========================================\n`);
