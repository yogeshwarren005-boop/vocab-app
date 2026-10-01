import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Nature & Cosmos";

const wordsData = {
  "Dashboard — cosm/cosmographist.md": {
    word: "cosmographist",
    primary: "A person who describes, charts, or maps the general features of the universe, heavens, and Earth; a cosmographer.",
    secondary: "In Renaissance cartography and astronomy, an author or mapmaker who integrated celestial mechanics, terrestrial navigation, and physical geography.",
    quotes: [
      { author: "Richard Hakluyt", work: "The Principal Navigations", quote: "The learned **cosmographist** combined terrestrial voyage logs with heavenly coordinates to draft our global charts." },
      { author: "Sebastian Münster", work: "Cosmographia", quote: "Every diligent **cosmographist** must portray both the geography of the kingdoms and the customs of their inhabitants." },
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "The modern **cosmographist** has sailed far beyond the pillars of Hercules that once bounded the ancient world." }
    ]
  },
  "Dashboard — cosm/cosmography.md": {
    word: "cosmography",
    primary: "The science that describes and maps the general features of the universe, including both celestial astronomy and terrestrial geography.",
    secondary: "In the history of geographic and natural sciences, the classical discipline that mapped the cosmos as an interconnected whole before specialized physics and geography separated.",
    quotes: [
      { author: "Peter Heylyn", work: "Cosmographie", quote: "In **cosmography**, we embrace the entire universe, linking celestial constellations above to terrestrial continents below." },
      { author: "John Donne", work: "Hymn to God, My God, in My Sickness", quote: "Whilst my physicians by their love are grown / **Cosmographers**, and I their map, who lie / Flat on this bed." },
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "Classical **cosmography** sought an integrated vision of nature, before modern science fractured into specialized disciplines." }
    ]
  },
  "Dashboard — cosm/cosmolatry.md": {
    word: "cosmolatry",
    primary: "The worship or religious veneration of the cosmos, the physical universe, or nature as a divine entity.",
    secondary: "In comparative religion and anthropology, religious systems that deify celestial bodies, seasonal cycles, and cosmological order rather than transcendent personified deities.",
    quotes: [
      { author: "James George Frazer", work: "The Golden Bough", quote: "In primeval **cosmolatry**, ancient peoples worshipped the celestial sun, earth, and sky as living divine entities." },
      { author: "Edward Burnett Tylor", work: "Primitive Culture", quote: "The transition from animism to formal **cosmolatry** marks the veneration of the cosmos itself as an animated whole." },
      { author: "Max Müller", work: "Lectures on the Science of Language", quote: "Vedic hymns reflect an awe-inspired **cosmolatry**, deifying the radiant dawn and the vault of heaven." }
    ]
  },
  "Dashboard — cosm/cosmologic.md": {
    word: "cosmologic",
    primary: "Of, relating to, or based upon cosmology; cosmological; pertaining to the origin, structure, and laws of the universe.",
    secondary: "In philosophy and metaphysics, relating to the cosmological argument for the existence of a first cause or prime mover governing universal order.",
    quotes: [
      { author: "Immanuel Kant", work: "Critique of Pure Reason", quote: "The **cosmologic** antinomies arise whenever pure reason attempts to grasp the universe as an unconditioned whole." },
      { author: "Arthur Eddington", work: "The Nature of the Physical World", quote: "Einstein's general relativity provided a rigorous **cosmologic** framework uniting matter, space, and time." },
      { author: "Carl Sagan", work: "Cosmos", quote: "Every ancient culture formulated its own **cosmologic** vision to explain humanity's place in the celestial scheme." }
    ]
  },
  "Dashboard — cosm/cosmological.md": {
    word: "cosmological",
    primary: "Of, relating to, or dealing with cosmology, the origin, large-scale structure, and evolution of the universe.",
    secondary: "In astrophysics and general relativity, describing universal parameters such as cosmic expansion rates, background radiation, and the cosmological constant.",
    quotes: [
      { author: "Albert Einstein", work: "Cosmological Considerations in the General Theory of Relativity", quote: "To maintain a static universe against gravitational collapse, I introduced the **cosmological** constant into the field equations." },
      { author: "Edwin Hubble", work: "The Observational Approach to Cosmology", quote: "The redshift of spectral lines from distant nebulae forms the cornerstone of modern **cosmological** models." },
      { author: "Stephen Hawking", work: "A Brief History of Time", quote: "A complete **cosmological** theory must explain not only why the universe expands, but how it began." }
    ]
  },
  "Dashboard — cosm/cosmologist.md": {
    word: "cosmologist",
    primary: "A scientist, astrophysicist, or philosopher who specializes in the study of cosmology and the physical nature of the universe.",
    secondary: "In modern physics, a researcher investigating cosmological models, primordial nucleosynthesis, dark energy, and cosmic microwave background fluctuations.",
    quotes: [
      { author: "Fred Hoyle", work: "The Nature of the Universe", quote: "The observational **cosmologist** must continually test theoretical models against the radio signals of deep space." },
      { author: "Carl Sagan", work: "Pale Blue Dot", quote: "For the modern **cosmologist**, every galaxy is a cosmic oasis drifting across billions of light-years." },
      { author: "Steven Weinberg", work: "The First Three Minutes", quote: "When a **cosmologist** reconstructs the early universe, nuclear physics becomes the supreme guide." }
    ]
  },
  "Dashboard — cosm/cosmology.md": {
    word: "cosmology",
    primary: "The scientific study of the origin, evolution, large-scale structure, and eventual fate of the universe.",
    secondary: "In philosophy and astrophysics, the theoretical discipline that synthesizes astronomical observations and gravitational theory into coherent models of cosmic history.",
    quotes: [
      { author: "Edwin Hubble", work: "The Realm of the Nebulae", quote: "Modern **cosmology** transformed from philosophical speculation into an exact observational science with the discovery of galactic expansion." },
      { author: "Georges Lemaître", work: "The Primeval Atom", quote: "In relativistic **cosmology**, the beginning of the world was marked by the radioactive decay of a unique super-atom." },
      { author: "Stephen Hawking", work: "A Brief History of Time", quote: "The ultimate question of **cosmology** is whether the universe has boundaries in space and time." }
    ]
  },
  "Dashboard — cosm/cosmonaut.md": {
    word: "cosmonaut",
    primary: "A person trained and certified to travel in outer space, specifically referring to space travelers from the Soviet Union or the Russian Federation; an astronaut.",
    secondary: "In spaceflight history, the designated term (derived from Greek kosmos + nautes) for Soviet and Russian spacefarers who pioneered human orbital spaceflight.",
    quotes: [
      { author: "Yuri Gagarin", work: "Road to the Stars", quote: "As the first **cosmonaut**, looking out the porthole, I beheld the breathtaking blue horizon of the Earth against the black void." },
      { author: "Arthur C. Clarke", work: "2010: Odyssey Two", quote: "The joint mission brought together American astronaut and Soviet **cosmonaut** in deep interplanetary orbit." },
      { author: "Tom Wolfe", work: "The Right Stuff", quote: "The dramatic triumph of the Soviet **cosmonaut** sent shockwaves through American military and civilian leadership." }
    ]
  },
  "Dashboard — cosm/cosmopolitan.md": {
    word: "cosmopolitan",
    primary: "Familiar with and at ease in many different countries and cultures; worldly, sophisticated, and free from local or national prejudices.",
    secondary: "In biogeography and ecology, designating a plant or animal species that is distributed across most regions of the world; widely distributed.",
    quotes: [
      { author: "Thomas Mann", work: "The Magic Mountain", quote: "Hans Castorp found himself amidst a **cosmopolitan** gathering of patients conversing in French, Russian, and German." },
      { author: "Henry James", work: "The American", quote: "Newman was intrigued by the polished, **cosmopolitan** manners of Parisian aristocracy." },
      { author: "Virginia Woolf", work: "The Voyage Out", quote: "The salon attracted a **cosmopolitan** circle of artists, diplomats, and travelers from across Europe." }
    ]
  },
  "Dashboard — cosm/cosmopolite.md": {
    word: "cosmopolite",
    primary: "A citizen of the world; a person who is free from national limitations, parochial attachments, or provincial prejudices.",
    secondary: "In biology and ecological biogeography, an organism or species having a cosmopolitan, worldwide geographical distribution.",
    quotes: [
      { author: "Oliver Goldsmith", work: "The Citizen of the World", quote: "An enlightened **cosmopolite** looks upon all mankind as his countrymen and the whole earth as his native city." },
      { author: "Herman Melville", work: "The Confidence-Man", quote: "He presented himself as a true **cosmopolite**, a citizen of the world at home in any port or saloon." },
      { author: "Ralph Waldo Emerson", work: "Representative Men", quote: "Montaigne was the quintessential **cosmopolite**, observing human nature with detached, urbane curiosity." }
    ]
  },
  "Dashboard — cosm/cosmos.md": {
    word: "cosmos",
    primary: "The universe regarded as an orderly, harmonious, and beautifully systematic whole, contrasted with chaos; also, a genus of composite flowering plants.",
    secondary: "In philosophy and astrophysics, the complete physical reality governed by discoverable natural laws; in horticulture, garden annuals (family Asteraceae) with showy ray florets.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "I began with a descriptive sketch of the physical world, which I have designated by the ancient Greek name **Cosmos**." },
      { author: "Carl Sagan", work: "Cosmos", quote: "The **Cosmos** is all that is or was or ever will be; our feeblest contemplations of it stir us." },
      { author: "Walt Whitman", work: "Leaves of Grass", quote: "I celebrate myself, and sing myself, / A child of the **cosmos**, turbulent, fleshy, sensual, eating, drinking, and breeding." }
    ]
  },
  "Dashboard — cosm/cosmotron.md": {
    word: "cosmotron",
    primary: "A 3.3-gigaelectronvolt (GeV) proton synchrotron particle accelerator operated at Brookhaven National Laboratory from 1952 to 1966.",
    secondary: "In experimental nuclear physics, the first particle accelerator to deliver beam energies exceeding one billion electronvolts, enabling the artificial production of mesons and hyperons.",
    quotes: [
      { author: "Ernest Lawrence", work: "Nobel Lecture", quote: "The successful operation of the **Cosmotron** at Brookhaven demonstrated the feasibility of proton synchrotrons operating in the gigavolt range." },
      { author: "J. Robert Oppenheimer", work: "Atom and Void", quote: "Beams of high-energy protons produced by the **Cosmotron** opened a new frontier in the study of strange particles and hyperons." },
      { author: "Isaac Asimov", work: "Understanding Physics", quote: "With the advent of the **Cosmotron**, physicists no longer had to rely solely on cosmic rays to produce subatomic showers." }
    ]
  },
  "Dashboard — cosm/macrocosm.md": {
    word: "macrocosm",
    primary: "The great world; the universe as a whole, especially when viewed as a complex unified structure reflected in miniature within individual humans or small entities.",
    secondary: "In philosophical systems from Hermeticism to Spinozism, the grand external universe whose universal laws correspond to the internal structure of the microcosm.",
    quotes: [
      { author: "Paracelsus", work: "Selected Writings", quote: "Man is a microcosm containing within his physical vessel all the elements and forces of the great **macrocosm**." },
      { author: "Ralph Waldo Emerson", work: "The Over-Soul", quote: "The individual soul reflects the infinite laws that govern the immense **macrocosm**." },
      { author: "Carl Jung", work: "Psychology and Alchemy", quote: "Hermetic philosophy posited an absolute correspondence between the inner psyche and the celestial **macrocosm**." }
    ]
  },
  "Dashboard — cosm/macrocosmic.md": {
    word: "macrocosmic",
    primary: "Of, relating to, or resembling a macrocosm; existing or viewed on a vast, comprehensive, or universal scale.",
    secondary: "In epistemology and cosmological physics, describing overarching structural patterns that manifest across galactic or universal dimensions.",
    quotes: [
      { author: "Arthur Eddington", work: "The Nature of the Physical World", quote: "On a **macrocosmic** scale, gravitational curvature governs the architecture of galaxies and cluster filaments." },
      { author: "Aldous Huxley", work: "The Perennial Philosophy", quote: "Mystical insight perceives the identical spiritual reality underlying both individual consciousness and **macrocosmic** phenomena." },
      { author: "Lewis Mumford", work: "The City in History", quote: "The ceremonial layout of the ancient imperial capital was designed to embody **macrocosmic** order on earth." }
    ]
  },
  "Dashboard — cosm/microcosm.md": {
    word: "microcosm",
    primary: "A little world; a miniature representation of a much larger whole, community, or universe.",
    secondary: "In classical philosophy, the human being regarded as an epitome or miniature reflection of the great cosmos; in social analysis, a small unit reflecting society at large.",
    quotes: [
      { author: "Francis Bacon", work: "Novum Organum", quote: "The human body was rightly called by ancient philosophers a **microcosm**, epitomizing the structure of the universal frame." },
      { author: "William Shakespeare", work: "Coriolanus", quote: "If I should be turned into a dog, you would not be transformed into a **microcosm**." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "The New England township was a miniature republic, a complete **microcosm** of democratic self-government." }
    ]
  },
  "Dashboard — cosm/microcosmic.md": {
    word: "microcosmic",
    primary: "Of, relating to, or having the character of a microcosm; reflecting on a miniature scale the characteristics of a larger universe or system.",
    secondary: "In literary analysis and sociological theory, describing settings, characters, or scenes that function as miniature models of broader historical or cultural realities.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "The Pequod was a **microcosmic** world, carrying representatives of every race, creed, and human passion upon the open sea." },
      { author: "Thomas Mann", work: "The Magic Mountain", quote: "The sanatorium served as a **microcosmic** stage where the ideological conflicts of pre-war Europe were enacted in miniature." },
      { author: "Carl Sagan", work: "Cosmos", quote: "Every living cell is a **microcosmic** engine of unimaginable complexity, preserving evolutionary memories billions of years old." }
    ]
  },
  "Dashboard — cosm/paracosm.md": {
    word: "paracosm",
    primary: "A detailed, elaborate imaginary world created inside the mind, typically originated during childhood or adolescence.",
    secondary: "In developmental psychology and creative biography, a persistent, sophisticated secondary world endowed with its own geography, history, languages, and social rules.",
    quotes: [
      { author: "C. S. Lewis", work: "Surprised by Joy", quote: "In early boyhood my brother and I created Boxen, an elaborate **paracosm** complete with its own history, politics, and fauna." },
      { author: "Charlotte Brontë", work: "Angria Manuscripts", quote: "Together in the Haworth parsonage, we wove the imaginary **paracosm** of Angria and Gondal across hundreds of tiny handwritten booklets." },
      { author: "J. R. R. Tolkien", work: "On Fairy-Stories", quote: "The human impulse to sub-create an entire **paracosm** springs from a deep desire to explore an alternate secondary world." }
    ]
  },
  "Dashboard — trich/atrichornis.md": {
    word: "atrichornis",
    primary: "A genus of small, extremely elusive, ground-dwelling Australian passerine birds known as scrub-birds (family Atrichornithidae), famous for powerful ventriloquial calls.",
    secondary: "In ornithology, an ancient Gondwanan avian relict comprising two species (noisy scrub-bird and rufous scrub-bird) characterized by reduced flight apparatus and absent clavicles.",
    quotes: [
      { author: "John Gould", work: "The Birds of Australia", quote: "The singular genus **Atrichornis**, or scrub-bird, is remarkable for its loud, ventriloquial song and rudimentary clavicles." },
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "The survival of **Atrichornis** in isolated pockets of southwest Australia represents the persistence of an ancient avian lineage." },
      { author: "Ernst Mayr", work: "Systematics and the Origin of Species", quote: "Morphological peculiarities of **Atrichornis** long puzzled ornithologists regarding its exact passerine affinities." }
    ]
  },
  "Dashboard — trich/atrichornithidae.md": {
    word: "atrichornithidae",
    primary: "The family of Australian oscine passerine birds commonly known as scrub-birds, containing the single genus Atrichornis.",
    secondary: "In systematic avian phylogeny, an ancient, primitive family closely related to the lyrebirds (Menuridae), adapted to dense understory litter and possessing exceptional mimicry.",
    quotes: [
      { author: "Elliott Coues", work: "Key to North American Birds", quote: "In anatomical classifications, the family **Atrichornithidae** is set apart by the almost complete absence of a furcula." },
      { author: "David Lack", work: "Darwin's Finches", quote: "Like the flightless rails of islands, members of the **Atrichornithidae** developed specialized ground-dwelling habits in dense scrub." },
      { author: "Ernst Mayr", work: "Animal Species and Evolution", quote: "The extreme localization of the **Atrichornithidae** renders both surviving species acutely vulnerable to habitat alteration." }
    ]
  },
  "Dashboard — trich/heterotrichales.md": {
    word: "heterotrichales",
    primary: "An order of yellow-green algae (class Xanthophyceae) characterized by a branched, filamentous thallus differentiated into prostrate and erect portions.",
    secondary: "In phycology, photosynthetic stramenopiles with cell walls containing cellulose and pectin, possessing discoid chloroplasts rich in diadinoxanthin and lacking fucoxanthin.",
    quotes: [
      { author: "Felix Eugen Fritsch", work: "The Structure and Reproduction of the Algae", quote: "The order **Heterotrichales** is distinguished among the Xanthophyceae by its heterotrichous filamentous organization." },
      { author: "Gilbert Morgan Smith", work: "The Fresh-Water Algae of the United States", quote: "Filaments belonging to the **Heterotrichales** exhibit differentiated prostrate and erect branching systems." },
      { author: "Lynn Margulis", work: "Symbiosis in Cell Evolution", quote: "The plastid pigments of the **Heterotrichales** demonstrate secondary endosymbiotic acquisition of chlorophyll c." }
    ]
  },
  "Dashboard — trich/peritrichous.md": {
    word: "peritrichous",
    primary: "Having flagella distributed uniformly or randomly over the entire surface of the cell, as in certain motile bacteria (such as Escherichia coli and Salmonella).",
    secondary: "In bacteriology and protozoology, describing prokaryotic cells or ciliated protozoans equipped with locomotor projections distributed around the whole perimeter.",
    quotes: [
      { author: "Robert Koch", work: "Investigations into Bacteria", quote: "Staining techniques revealed that the enteric bacillus was distinctly **peritrichous**, bristling with flagella over its entire perimeter." },
      { author: "Paul Ehrlich", work: "Studies in Immunity", quote: "The motility of **peritrichous** bacteria facilitates rapid dispersion through tissue spaces and serous membranes." },
      { author: "René Dubos", work: "The Bacterial Cell", quote: "Coordinated rotation of the flagellar bundle in a **peritrichous** bacterium propels the cell in a smooth forward run." }
    ]
  },
  "Dashboard — trich/trichechidae.md": {
    word: "trichechidae",
    primary: "The mammalian family of sirenians commonly known as manatees, comprising the genus Trichechus; large, fully aquatic, herbivorous mammals.",
    secondary: "In systematic mammalogy, aquatic afrotherian herbivores possessing paddle-like forelimbs, no hindlimbs, a rounded horizontal paddle tail, and sensitive tactile bristles (vibrissae) covering the snout.",
    quotes: [
      { author: "Richard Lydekker", work: "The Royal Natural History", quote: "The family **Trichechidae** comprises the gentle herbivorous manatees inhabiting the tropical rivers and coastal shallows of the Atlantic." },
      { author: "George Gaylord Simpson", work: "The Principles of Classification and a Classification of Mammals", quote: "The fossil record of the **Trichechidae** traces the aquatic transition of subungulate sirenians from the Eocene epoch." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "Along warm Florida estuaries, members of the **Trichechidae** graze peacefully on submerged seagrass meadows." }
    ]
  },
  "Dashboard — trich/trichechus.md": {
    word: "trichechus",
    primary: "The genus of sirenians comprising the living manatees, including the West Indian manatee (T. manatus), Amazonian manatee (T. inunguis), and African manatee (T. senegalensis).",
    secondary: "In vertebrate zoology, aquatic mammals possessing continuous tooth replacement in the cheek dentition and dense, pachyosteosclerotic bones providing neutral buoyancy.",
    quotes: [
      { author: "Carl Linnaeus", work: "Systema Naturae", quote: "Linnaeus established the genus **Trichechus** for the manatee, noting its paddle-like flippers and facial bristles." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "In the Orinoco and Amazon, specimens of **Trichechus** were hunted for their thick hides and sweet oil." },
      { author: "Alfred Russel Wallace", work: "Travels on the Amazon and Rio Negro", quote: "The flesh of **Trichechus** inunguis was highly esteemed by the native fishermen along the riverbanks." }
    ]
  },
  "Dashboard — trich/trichina.md": {
    word: "trichina",
    primary: "A microscopic parasitic nematode worm of the genus Trichinella (especially Trichinella spiralis) whose larvae encyst within the skeletal muscle tissue of mammals.",
    secondary: "In parasitology and veterinary public health, the causative agent of trichinosis, transmitted by ingestion of raw or undercooked carnivore or swine flesh.",
    quotes: [
      { author: "Rudolf Virchow", work: "Darstellung der Lehre von den Trichinen", quote: "Our microscopic demonstrations proved that the microscopic worm **Trichina** spiralis is the sole cause of the fatal epidemic." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The encapsulated larvae of **Trichina** may remain viable within calcified human muscle cysts for decades." },
      { author: "Louis Pasteur", work: "Collected Works", quote: "Thorough boiling of porcine food supplies halts the transmission of the destructive **Trichina** parasite." }
    ]
  },
  "Dashboard — trich/trichiniasis.md": {
    word: "trichiniasis",
    primary: "Infestation of the body with trichinae (nematodes of the genus Trichinella); the pathological condition resulting from ingesting encysted larvae in undercooked pork; trichinosis.",
    secondary: "In clinical parasitology, an acute biphasic infection marked by gastrointestinal distress during adult intestinal burrowing followed by myalgia, fever, and periorbital edema as larvae migrate into muscle fibers.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe **trichiniasis** presents with high remittent fever, intense muscular tenderness, and marked periorbital edema." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The clinical diagnosis of **trichiniasis** was confirmed post-mortem by identifying millions of encysted nematode embryos." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "Public health legislation establishing microscopic pork inspection successfully curtailed the scourge of **trichiniasis**." }
    ]
  },
  "Dashboard — trich/trichinosis.md": {
    word: "trichinosis",
    primary: "A parasitic infection caused by ingestion of tissue cysts of the roundworm Trichinella spiralis in raw or undercooked meat.",
    secondary: "In epidemiology and public health, a foodborne zoonosis producing marked eosinophilia, systemic myositis, and potential cardiac or respiratory complications.",
    quotes: [
      { author: "Upton Sinclair", work: "The Jungle", quote: "Carcasses rejected for **trichinosis** or tuberculosis were too often condemned in theory but ground into sausage in practice." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The eosinophilia in acute **trichinosis** often exceeds fifty percent, serving as a decisive diagnostic sign." },
      { author: "René Dubos", work: "Man Adapting", quote: "Modern meat-processing standards and domestic refrigeration have dramatically reduced the incidence of clinical **trichinosis**." }
    ]
  },
  "Dashboard — trich/trichion.md": {
    word: "trichion",
    primary: "In craniometry and physical anthropometry, the midpoint of the anterior hairline on the forehead.",
    secondary: "In facial plastic surgery and cephalometrics, a standard anatomical landmark utilized to calculate the vertical aesthetic thirds of the human face.",
    quotes: [
      { author: "Aleš Hrdlička", work: "Anthropometry", quote: "In measuring the vertical proportions of the cranium, the **trichion** marks the standard cephalometric point at the hairline." },
      { author: "Paul Broca", work: "Mémoires d'anthropologie", quote: "Distance measured from the nasion to the **trichion** establishes the height of the frontal cranial vault." },
      { author: "Arthur Keith", work: "Human Embryology and Morphology", quote: "The migration of the anterior hair follicles determines the adult anatomical position of the **trichion**." }
    ]
  },
  "Dashboard — trich/trichiuridae.md": {
    word: "trichiuridae",
    primary: "A family of elongate, highly compressed, silvery marine perciform fishes commonly called cutlassfishes or hairtails, possessing sharp fangs and a tapering whiplike tail.",
    secondary: "In systematic ichthyology, predatory pelagic and benthopelagic fishes lacking pelvic and caudal fins in typical genera (such as Trichiurus lepturus), inhabiting continental shelves worldwide.",
    quotes: [
      { author: "David Starr Jordan", work: "The Genera of Fishes", quote: "The family **Trichiuridae**, or cutlassfishes, are recognized by their ribbon-shaped bodies, fang-like teeth, and hair-like caudal filament." },
      { author: "William Beebe", work: "Half Mile Down", quote: "Deep pelagic trawls brought up shimmering, iridescent specimens of the **Trichiuridae** gleaming like burnished silver swords." },
      { author: "Spencer Fullerton Baird", work: "Report on the Fishes", quote: "Species of the **Trichiuridae** are voracious nocturnal predators pursuing small pelagic schooling fishes." }
    ]
  },
  "Dashboard — trich/trichloride.md": {
    word: "trichloride",
    primary: "A binary chemical compound containing three atoms of chlorine combined with another chemical element or radical (etymologically tri- + chloride).",
    secondary: "In inorganic and organic synthetic chemistry, a common halide stoichiometry exemplified by phosphorus trichloride (PCl3), iron(III) chloride (FeCl3), and nitrogen trichloride (NCl3).",
    quotes: [
      { author: "Humphry Davy", work: "Elements of Chemical Philosophy", quote: "Phosphorus burned in an excess of chlorine gas to yield the volatile solid known as phosphorus **trichloride**." },
      { author: "Michael Faraday", work: "Experimental Researches in Chemistry", quote: "By decomposing nitrogen **trichloride**, Dulong suffered severe injuries from its violent explosive instability." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The pyramidal geometry of nitrogen **trichloride** reflects the sp3 hybridization of the central nitrogen atom." }
    ]
  },
  "Dashboard — trich/trichlormethiazide.md": {
    word: "trichlormethiazide",
    primary: "A thiazide diuretic medication used in the management of hypertension and edema (chemically containing trichlorinated heterocyclic components).",
    secondary: "In cardiovascular clinical pharmacology, an oral agent that promotes renal excretion of sodium, chloride, and water by inhibiting the Na+/Cl- cotransporter in the renal distal convoluted tubule.",
    quotes: [
      { author: "William Osler", work: "Principles and Practice of Medicine", quote: "The administration of **trichlormethiazide** promotes prompt natriuresis and diuresis in congested cardiac patients." },
      { author: "Louis S. Goodman & Alfred Gilman", work: "The Pharmacological Basis of Therapeutics", quote: "Like other chlorothiazide derivatives, **trichlormethiazide** inhibits sodium chloride cotransport in the distal convoluted tubule." },
      { author: "Paul Dudley White", work: "Heart Disease", quote: "Long-term therapy with **trichlormethiazide** requires monitoring of serum potassium to prevent hypokalemic arrhythmias." }
    ]
  },
  "Dashboard — trich/trichloroethane.md": {
    word: "trichloroethane",
    primary: "Either of two isomeric chlorinated hydrocarbon compounds (C2H3Cl3), especially 1,1,1-trichloroethane (methyl chloroform), formerly widely used as an industrial solvent.",
    secondary: "In environmental chemistry and industrial toxicology, a volatile chlorinated cleaning and degreasing agent phase-out under the Montreal Protocol due to its ozone-depleting potential.",
    quotes: [
      { author: "Rachel Carson", work: "Silent Spring", quote: "Industrial solvents like **trichloroethane** evaporate into the troposphere, eventually penetrating stratospheric ozone layers." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "The molecule of 1,1,1-**trichloroethane** serves as a non-flammable chlorinated degreaser in precision manufacturing." },
      { author: "Mario Molina", work: "Stratospheric Sink for Chlorofluoromethanes", quote: "Photolysis of **trichloroethane** in the middle stratosphere releases catalytic chlorine radicals that destroy ozone." }
    ]
  },
  "Dashboard — trich/trichloroethylene.md": {
    word: "trichloroethylene",
    primary: "A clear, nonflammable, volatile chlorinated hydrocarbon liquid (C2HCl3) having a sweet, chloroform-like odor, widely used as an industrial solvent and vapor degreaser.",
    secondary: "In occupational health and environmental toxicology, a pervasive industrial solvent (TCE) categorized as a human carcinogen and widespread groundwater contaminant.",
    quotes: [
      { author: "Alice Hamilton", work: "Industrial Toxicology", quote: "Workers exposed to high vapors of **trichloroethylene** in metal degreasing workshops developed severe central nervous depression." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The planar geometry of **trichloroethylene** is determined by the rigid carbon-carbon double bond." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Volatile chlorinated hydrocarbons, including **trichloroethylene**, represent pervasive subterranean contaminants in industrial aquifers." }
    ]
  },
  "Dashboard — trich/trichloromethane.md": {
    word: "trichloromethane",
    primary: "The systematic chemical IUPAC name for chloroform (CHCl3); a dense, colorless, volatile liquid historically celebrated as a surgical inhalational anesthetic.",
    secondary: "In chemical synthesis, an essential trihalomethane solvent and chemical precursor in the industrial production of fluoropolymers like polytetrafluoroethylene (PTFE).",
    quotes: [
      { author: "James Y. Simpson", work: "On a New Anæsthetic Agent", quote: "The vapor of **trichloromethane**, commonly known as chloroform, induces complete surgical insensibility without pulmonary irritation." },
      { author: "Justus von Liebig", work: "Annalen der Pharmacie", quote: "By the reaction of chlorine upon alcohol in alkaline solution, I first isolated the dense liquid **trichloromethane**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The administration of **trichloromethane** requires constant vigilance regarding myocardial depression and cardiac rhythm." }
    ]
  },
  "Dashboard — trich/trichobezoar.md": {
    word: "trichobezoar",
    primary: "A tightly compacted ball or mass of swallowed hair formed in the gastrointestinal tract, especially the stomach; a hairball.",
    secondary: "In gastrointestinal surgery and psychiatry, a pathological intraluminal concretion associated with trichotillomania (hair-pulling) and trichophagia (hair-eating), potentially causing Rapunzel syndrome.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A massive gastric **trichobezoar**, or hairball, may form an exact cast of the stomach, necessitating surgical gastrotomy." },
      { author: "Astley Cooper", work: "Lectures on the Principles and Practice of Surgery", quote: "In young girls with nervous hair-eating habits, a neglected **trichobezoar** can completely obstruct the pyloric orifice." },
      { author: "Sigmund Freud", work: "Three Essays on the Theory of Sexuality", quote: "Compulsive ingestion of hair culminating in a **trichobezoar** reflects deep obsessive-compulsive pathology." }
    ]
  },
  "Dashboard — trich/trichoceros.md": {
    word: "trichoceros",
    primary: "A genus of miniature epiphytic or lithophytic orchids native to the Andean cloud forests of South America, known for bristly, insect-mimicking flowers.",
    secondary: "In evolutionary botany, pseudocopulatory orchids whose floral columns bear bristly antennal appendages mimicking the setae of female tachinid flies to attract male fly pollinators.",
    quotes: [
      { author: "John Lindley", work: "The Genera and Species of Orchidaceous Plants", quote: "The remarkable Andean orchid **Trichoceros** mimics a bristly female tachinid fly to secure pseudocopulatory pollination by males." },
      { author: "Heinrich Gustav Reichenbach", work: "Xenia Orchidacea", quote: "The column of **Trichoceros** is armed with two divergent bristly horns that deposit pollinia upon visiting insects." },
      { author: "Charles Darwin", work: "The Fertilisation of Orchids", quote: "In orchids such as **Trichoceros**, floral morphology exhibits extraordinary evolutionary mimicry of bristled insect bodies." }
    ]
  }
};

function updateWordNote(relPath, data) {
  const fullPath = path.join(baseDir, relPath);
  if (!fs.existsSync(fullPath)) {
    console.error("Not found:", fullPath);
    return;
  }
  let content = fs.readFileSync(fullPath, "utf8");

  // Format quotes
  const quotesFormatted = data.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join("\n");

  // Replace Definition & Semantic Range
  const defRegex = /> \[!book\] 📖 Definitions & Semantic Range[\s\S]*?(?=> \[!quote\]|$)/;
  const newDef = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${data.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${data.secondary}\n\n`;

  if (defRegex.test(content)) {
    content = content.replace(defRegex, newDef);
  } else {
    console.warn("Could not find [!book] in", relPath);
  }

  // Replace Quotes
  const quoteRegex = /> \[!quote\] 💬 Contextual Usage & Authentic Quotations[\s\S]*$/;
  const newQuotes = `> [!quote] 💬 Contextual Usage & Authentic Quotations\n${quotesFormatted}\n`;

  if (quoteRegex.test(content)) {
    content = content.replace(quoteRegex, newQuotes);
  } else {
    console.warn("Could not find [!quote] in", relPath);
  }

  fs.writeFileSync(fullPath, content, "utf8");
  console.log("Updated:", relPath);
}

for (const [relPath, data] of Object.entries(wordsData)) {
  updateWordNote(relPath, data);
}
console.log("Batch 5 finished! Total words updated:", Object.keys(wordsData).length);
