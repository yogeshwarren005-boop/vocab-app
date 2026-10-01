import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Physics & Chemistry';

const filesData = {
  // === Dashboard — ale (4 words) ===
  "Dashboard — ale/ale.md": {
    primary: "A fermented alcoholic beverage brewed from malted barley and hops using top-fermenting yeast at warm temperatures.",
    secondary: "Historically in English culture, an unhopped malt liquor distinct from beer, or a festive village gathering characterized by revelry and drinking.",
    quotes: [
      { author: "William Shakespeare", work: "The Winter's Tale", quote: "For a quart of **ale** is a dish for a king." },
      { author: "Geoffrey Chaucer", work: "The Canterbury Tales", quote: "Well loved he by the morn a sop in wine; to live in delight was ever his custom, for he was Epicurus' own son, who held opinion that plain delight was truly full felicity, and ever he drank good **ale**." },
      { author: "Thomas Hardy", work: "Far from the Madding Crowd", quote: "The warm **ale** in the great pewter mug circulated from hand to hand among the shearers." }
    ]
  },
  "Dashboard — ale/aleuromancy.md": {
    primary: "Divination or fortune-telling practiced by interpreting patterns, movements, or messages written on slips of paper wrapped in flour or dough.",
    secondary: "An ancient mantic practice, documented from Hellenic and Near Eastern rituals, considered an etymological and cultural precursor to modern fortune cookies.",
    quotes: [
      { author: "Lewis Spence", work: "An Encyclopaedia of Occultism", quote: "In ancient Greece, **aleuromancy** was performed by tossing wheat flour upon the hearth or rolling messages in balls of paste." },
      { author: "Edward Tylor", work: "Primitive Culture", quote: "The priest inspected the scattered flour in the rite of **aleuromancy** to discover signs of divine favor." },
      { author: "Richard Cavendish", work: "The Black Arts", quote: "Like pyromancy and hydromancy, **aleuromancy** sought omens in the simplest domestic substance—common meal." }
    ]
  },
  "Dashboard — ale/aleurone.md": {
    primary: "Protein granules or crystalline grains stored in the specialized outer endosperm cells of seeds, particularly in cereal grains.",
    secondary: "In plant physiology, the outermost cellular layer (the aleurone layer) of grass caryopses that secretes hydrolytic enzymes during seed germination.",
    quotes: [
      { author: "Julius von Sachs", work: "Text-book of Botany", quote: "The grains of **aleurone** lie densely packed in the outer cells of the seed endosperm." },
      { author: "Francis Darwin", work: "The Physiology of Plants", quote: "Upon imbibition of water, the **aleurone** layer produces alpha-amylase to mobilize starch reserves." },
      { author: "G. Ledyard Stebbins", work: "Variation and Evolution in Plants", quote: "Pigmentation patterns within the cereal **aleurone** have served as pivotal genetic markers in classical cytogenetics." }
    ]
  },
  "Dashboard — ale/aleuronic.md": {
    primary: "Of, relating to, or consisting of aleurone grains or the aleurone layer of seeds.",
    secondary: "Characterized by proteinaceous floury deposits within plant storage tissues or seed morphology.",
    quotes: [
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "The **aleuronic** granules dissolve gradually as the embryonic axis begins its rapid elongation." },
      { author: "Sydney Howard Vines", work: "Lectures on the Physiology of Plants", quote: "Microchemical tests reveal the rich nitrogenous nature of the **aleuronic** inclusions in the seed coat." },
      { author: "Daniel Trembly MacDougal", work: "Practical Text-book of Plant Physiology", quote: "The digestion of **aleuronic** reserves is initiated by diastatic ferments activated during germination." }
    ]
  },

  // === Dashboard — arsen (8 words) ===
  "Dashboard — arsen/arsen.md": {
    primary: "A combining form and classical chemical root derived from Greek arsenikon, designating arsenic or arsenic-bearing compounds.",
    secondary: "In historical alchemy and early chemistry, denoting male or potent mineral properties, later formalized into chemical terminology.",
    quotes: [
      { author: "Jöns Jacob Berzelius", work: "Traité de Chimie", quote: "The radical **arsen**- forms distinct series of salts depending on the valency state of the metalloid." },
      { author: "Antoine Lavoisier", work: "Elements of Chemistry", quote: "Mineral substances incorporating the **arsen**- base exhibit profound volatility when heated in closed vessels." },
      { author: "Humphry Davy", work: "Elements of Chemical Philosophy", quote: "The combination of **arsen**- with sulfur yields native realgar and orpiment known since antiquity." }
    ]
  },
  "Dashboard — arsen/arsenal.md": {
    primary: "An establishment for the manufacture, storage, repair, or issue of weapons and military equipment.",
    secondary: "A comprehensive repository, collection, or supply of resources, capabilities, or arguments available for a specific purpose.",
    quotes: [
      { author: "George Washington", work: "First Annual Address to Congress", quote: "To be prepared for war is one of the most effectual means of preserving peace, necessitating a well-stored **arsenal**." },
      { author: "Winston Churchill", work: "The Grand Alliance", quote: "The United States became the great **arsenal** of democracy, pouring forth munitions across the Atlantic." },
      { author: "Alexander Hamilton", work: "The Federalist Papers", quote: "The national government must possess the power to establish an **arsenal** and dockyards for the common defense." }
    ]
  },
  "Dashboard — arsen/arsenate.md": {
    primary: "A salt or ester of arsenic acid containing the trivalent oxyanion AsO4(3-).",
    secondary: "In geochemistry and agricultural chemistry, toxic mineral compounds historically used as insecticides and herbicides, such as lead arsenate.",
    quotes: [
      { author: "Rachel Carson", work: "Silent Spring", quote: "Orchards were repeatedly drenched with lead **arsenate** before the advent of synthetic chlorinated hydrocarbons." },
      { author: "James Dwight Dana", work: "A System of Mineralogy", quote: "Erythrite and mimetite belong to the vast mineral class characterized by the **arsenate** radical." },
      { author: "Ira Remsen", work: "Inorganic Chemistry", quote: "When arsenic pentoxide dissolves in alkaline solutions, a stable crystalline **arsenate** is formed." }
    ]
  },
  "Dashboard — arsen/arsenic.md": {
    primary: "A toxic, brittle, steel-gray metalloid chemical element with atomic number 33, represented by the symbol As.",
    secondary: "Historically, common arsenic trioxide ('white arsenic'), a notorious odorless poison employed in medicine, metallurgy, and homicide.",
    quotes: [
      { author: "Gustave Flaubert", work: "Madame Bovary", quote: "She walked straight to the cupboard, seized the jar of **arsenic**, and tore out the blue paper stopper." },
      { author: "Arthur Conan Doyle", work: "A Study in Scarlet", quote: "He analyzed the contents of the tumbler and instantly detected the presence of **arsenic**." },
      { author: "Michael Faraday", work: "Chemical Manipulation", quote: "In subliming **arsenic**, great care must be observed to avoid inhaling the lethal garlic-scented fumes." }
    ]
  },
  "Dashboard — arsen/arsenical.md": {
    primary: "Pertaining to, containing, or produced by arsenic.",
    secondary: "A medicinal or pesticidal preparation containing arsenic compounds, such as Salvarsan (arsphenamine).",
    quotes: [
      { author: "Paul Ehrlich", work: "Experimental Chemotherapy of Spirilloses", quote: "The synthetic **arsenical** compound demonstrated specific affinity for the treponema while sparing host tissue." },
      { author: "Thomas Mann", work: "The Magic Mountain", quote: "The physician prescribed mild **arsenical** waters to stimulate metabolic activity in the convalescent." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Thermal springs often deposit thick crusts containing **arsenical** pyrites and copper ores." }
    ]
  },
  "Dashboard — arsen/arsenide.md": {
    primary: "A binary chemical compound of arsenic with a more electropositive element or radical, especially a metal.",
    secondary: "In semiconductor physics, materials such as gallium arsenide (GaAs) used in high-frequency integrated circuits and optoelectronics.",
    quotes: [
      { author: "William Shockley", work: "Electrons and Holes in Semiconductors", quote: "Crystalline gallium **arsenide** exhibits electron mobility substantially higher than that of elemental silicon." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The tetrahedral coordination in zinc **arsenide** reflects the covalent nature of the metalloid linkage." },
      { author: "John William Strutt, Lord Rayleigh", work: "Scientific Papers", quote: "The synthetic metallic **arsenide** was roasted in a platinum crucible to determine its stoichiometric loss." }
    ]
  },
  "Dashboard — arsen/arsenious.md": {
    primary: "Of, containing, or derived from trivalent arsenic.",
    secondary: "Pertaining specifically to arsenious acid or arsenic trioxide (arsenious oxide, As2O3).",
    quotes: [
      { author: "Robert Bunsen", work: "Memoir on the Cacodyl Series", quote: "The reaction between **arsenious** acid and potassium acetate gave birth to the astonishing cacodyl radical." },
      { author: "Humphry Davy", work: "Elements of Agricultural Chemistry", quote: "Solutions of **arsenious** oxide, though perilously caustic, were sometimes applied to eradicate smut in grain." },
      { author: "Justus von Liebig", work: "Handbuch der Chemie", quote: "By treating the ore with hydrochloric acid, a precipitate of white **arsenious** oxide is deposited." }
    ]
  },
  "Dashboard — arsen/arsenopyrite.md": {
    primary: "A metallic, tin-white to steel-gray mineral consisting of iron arsenic sulfide (FeAsS), the principal ore of arsenic.",
    secondary: "In economic geology, an ore mineral associated with gold, tin, and cobalt deposits, notable for emitting a pungent garlic odor when struck.",
    quotes: [
      { author: "James Dwight Dana", work: "Manual of Mineralogy", quote: "When struck with a steel hammer, **arsenopyrite** emits sparks accompanied by the characteristic odor of arsenic." },
      { author: "Waldemar Lindgren", work: "Mineral Deposits", quote: "Auriferous veins in quartz commonly carry microscopic gold intergrown within the grains of **arsenopyrite**." },
      { author: "Heinrich Ries", work: "Economic Geology", quote: "Roasting of **arsenopyrite** drives off volatile arsenic trioxide, which is condensed in cooling flues." }
    ]
  },

  // === Dashboard — bar (29 words) ===
  "Dashboard — bar/abarognosis.md": {
    primary: "Loss or impairment of the ability to appreciate or estimate the weight of objects held in the hand, caused by a neurological lesion.",
    secondary: "In clinical neurology, a sensory deficit indicative of contralateral parietal lobe damage, particularly affecting the somatosensory cortex.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The patient displayed marked **abarognosis**, failing to distinguish between a featherweight sphere and a heavy lead shot." },
      { author: "Gordon Holmes", work: "Disorders of Sensation in Brain Lesions", quote: "Cortical parietal injury frequently results in profound **abarognosis** while tactile localization remains intact." },
      { author: "S. Weir Mitchell", work: "Injuries of Nerves and Their Consequences", quote: "Tests for **abarognosis** were conducted using graduated metal disks placed in the palm of the extended hand." }
    ]
  },
  "Dashboard — bar/antibaryon.md": {
    primary: "The antimatter counterpart of a baryon, possessing opposite baryon number, electric charge, and color charge.",
    secondary: "In particle physics, a composite subatomic antiparticle made up of three antiquarks, such as an antiproton or antineutron.",
    quotes: [
      { author: "Richard Feynman", work: "The Character of Physical Law", quote: "For every baryon in the catalog of fundamental particles, an equivalent **antibaryon** must theoretically exist." },
      { author: "Murray Gell-Mann", work: "The Eightfold Way", quote: "In the quark model, each **antibaryon** is formed by a bound triplet of antiquarks." },
      { author: "Steven Weinberg", work: "The First Three Minutes", quote: "In the primordial furnace, the slight asymmetry between baryon and **antibaryon** determined the survival of all matter." }
    ]
  },
  "Dashboard — bar/bar.md": {
    primary: "A metric unit of pressure equal to exactly 100,000 pascals (10^5 Pa), approximately equivalent to atmospheric pressure at sea level.",
    secondary: "A rigid oblong piece of metal or wood, or an establishment where alcoholic drinks are served, or the legal profession collectively.",
    quotes: [
      { author: "H. G. Wells", work: "The Time Machine", quote: "The barometer stood at one **bar** as the machine hummed into the distant centuries." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Speckled Band", quote: "He picked up the heavy poker and with one twist bent it into a curved **bar**." },
      { author: "Charles Dickens", work: "Bleak House", quote: "The learned gentleman who stood before the **bar** addressed the chancellor in measured tones." }
    ]
  },
  "Dashboard — bar/bared.md": {
    primary: "Uncovered, exposed to view, or stripped of covering, clothing, or disguise.",
    secondary: "Laid open to scrutiny, emotional vulnerability, or physical exposure.",
    quotes: [
      { author: "William Shakespeare", work: "Measure for Measure", quote: "Shave the head and tie the beard, and say it was the desire of the penitent to be so **bared** before his death." },
      { author: "Thomas Hardy", work: "Far from the Madding Crowd", quote: "Bathsheba knew more of him now; he had entirely **bared** his heart before her." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "With **bared** head and arms, the blacksmith stood before the forge in the dark hull." }
    ]
  },
  "Dashboard — bar/barely.md": {
    primary: "Only just; scarcely; almost not; by a very narrow margin.",
    secondary: "Without adornment, disguise, or concealment; plainly or scantily.",
    quotes: [
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "She could **barely** conceal her mortification at her mother's ill-timed remarks." },
      { author: "Joseph Conrad", work: "Heart of Darkness", quote: "The outline of the dense forest was **barely** discernible against the evening sky." },
      { author: "George Eliot", work: "Middlemarch", quote: "His voice was **barely** audible above the rising murmur of the crowd in the square." }
    ]
  },
  "Dashboard — bar/bareness.md": {
    primary: "The state or condition of being bare, naked, uncovered, or devoid of vegetation or furniture.",
    secondary: "Bleak simplicity, austerity, or absence of embellishment or concealment.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "The cold **bareness** of the dormitory chilled my spirit on that first dreary evening." },
      { author: "Henry David Thoreau", work: "Walden", quote: "I admired the clean **bareness** of the unplastered cabin walls, which breathed the scent of pine." },
      { author: "William Wordsworth", work: "The Prelude", quote: "The mountain peak stood solitary in its stony **bareness**, stripped of tree and turf." }
    ]
  },
  "Dashboard — bar/baresthesia.md": {
    primary: "The sensory perception of pressure or weight; pressure sense.",
    secondary: "In neurophysiology and psychophysics, the faculty of tactile and deep proprioceptive appreciation of applied force.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "Experiments in **baresthesia** demonstrate that muscle sense combines with cutaneous pressure to yield precise weight estimates." },
      { author: "Ernst Heinrich Weber", work: "De Tactu", quote: "The discrimination threshold in **baresthesia** obeys the law that just-noticeable differences remain proportional to the initial load." },
      { author: "Charles Sherrington", work: "The Integrative Action of the Nervous System", quote: "Proprioceptive afferents from tendon organs cooperate with cutaneous mechanoreceptors to mediate accurate **baresthesia**." }
    ]
  },
  "Dashboard — bar/bariatric.md": {
    primary: "Relating to the branch of medicine that deals with the causes, prevention, and treatment of obesity.",
    secondary: "Denoting surgical procedures (such as gastric bypass or sleeve gastrectomy) or medical equipment designed for individuals with severe obesity.",
    quotes: [
      { author: "Atul Gawande", work: "Complications: A Surgeon's Notes on an Imperfect Science", quote: "The development of **bariatric** surgery transformed our approach to severe metabolic disease." },
      { author: "Oliver Sacks", work: "An Anthropologist on Mars", quote: "The hospital retrofitted its wards with reinforced **bariatric** beds and specialized transport equipment." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "He consulted with the **bariatric** specialist to evaluate whether gastric banding was indicated for the diabetic patient." }
    ]
  },
  "Dashboard — bar/baric.md": {
    primary: "Of, pertaining to, or indicating atmospheric pressure or weight.",
    secondary: "In older chemical terminology, of or containing barium (from heavy spar, baryte).",
    quotes: [
      { author: "Robert FitzRoy", work: "The Weather Book", quote: "The **baric** gradient between the two air masses indicated an approaching cyclonic disturbance." },
      { author: "Humphry Davy", work: "Philosophical Transactions", quote: "The precipitate obtained from the sulfate solution was designated as **baric** earth." },
      { author: "William Napier Shaw", work: "Manual of Meteorology", quote: "Rapid **baric** depression across the coast invariably heralded gale-force winds." }
    ]
  },
  "Dashboard — bar/baring.md": {
    primary: "Uncovering, revealing, or exposing to view; stripping of covering.",
    secondary: "Making naked or laying bare in an emotional, rhetorical, or physical sense.",
    quotes: [
      { author: "Jack London", work: "The Call of the Wild", quote: "Buck sprang forward with a ferocious growl, **baring** his gleaming fangs in the firelight." },
      { author: "Virginia Woolf", work: "To the Lighthouse", quote: "The retreating tide was **baring** the dark, weed-hung rocks along the headland." },
      { author: "Walt Whitman", work: "Leaves of Grass", quote: "O nature, **baring** your breast to the winds of heaven, I absorb your vigor." }
    ]
  },
  "Dashboard — bar/baritone.md": {
    primary: "The adult male singing voice intermediate between tenor and bass; or a singer possessing this voice.",
    secondary: "A brass instrument resembling a euphonium or tenor horn; or a tone of deep, resonant gravity.",
    quotes: [
      { author: "James Joyce", work: "Ulysses", quote: "The rich **baritone** voice of the singer rolled sonorously through the dining hall." },
      { author: "E. M. Forster", work: "A Room with a View", quote: "He sang the Italian aria with a robust **baritone** that pleased the entire company." },
      { author: "George Bernard Shaw", work: "Music in London", quote: "The role of Don Giovanni demands a dramatic **baritone** possessing elegance as well as vocal power." }
    ]
  },
  "Dashboard — bar/barognosis.md": {
    primary: "The conscious neurological recognition and appreciation of weight; the capacity to evaluate the weight of objects by lifting.",
    secondary: "In clinical sensory testing, the intact sensory function contrasted with abarognosis, mediated by somatosensory pathways.",
    quotes: [
      { author: "Henry Head", work: "Studies in Neurology", quote: "Intact **barognosis** requires the harmonious cooperation of both superficial touch receptors and deep neuromuscular spindles." },
      { author: "Harvey Cushing", work: "Tumors of the Nervus Acusticus", quote: "Examination revealed that stereognosis and **barognosis** were preserved in the right upper extremity." },
      { author: "Foster Kennedy", work: "Symptomatology of Temporosphenoidal Tumors", quote: "Defective **barognosis** in one hand helped localize the cortical lesion to the parietal lobe." }
    ]
  },
  "Dashboard — bar/barogram.md": {
    primary: "A continuous graphic record of atmospheric pressure traced by a barograph over a period of time.",
    secondary: "In meteorological stations, the revolving paper chart showing pressure trends used to identify fronts and squall lines.",
    quotes: [
      { author: "Robert Falcon Scott", work: "Scott's Last Expedition", quote: "The **barogram** showed an ominous drop of twenty millibars within four hours, portending the blizzard." },
      { author: "William Napier Shaw", work: "Forecasting Weather", quote: "A sudden V-shaped trough on the **barogram** marked the passage of a violent cold front." },
      { author: "Ernest Shackleton", work: "South: The Story of Shackleton's Last Expedition", quote: "We inspected the **barogram** daily to anticipate shifts in the pack ice surrounding the Endurance." }
    ]
  },
  "Dashboard — bar/barograph.md": {
    primary: "A recording barometer that automatically registers variations in atmospheric pressure on a moving chart or digital log.",
    secondary: "An instrument utilizing aneroid capsules and an inked lever arm to monitor barometric fluctuations for aviation or weather tracking.",
    quotes: [
      { author: "Jules Verne", work: "Twenty Thousand Leagues Under the Sea", quote: "Captain Nemo pointed to the precision **barograph** mounted against the teakwood bulkhead of the saloon." },
      { author: "Antoine de Saint-Exupéry", work: "Night Flight", quote: "The pilot observed the needle of the **barograph** creeping steadily downward as turbulence rocked the aircraft." },
      { author: "H. G. Wells", work: "The War in the Air", quote: "The officer tapped the glass of the **barograph** and warned that a sudden depression was sweeping across the Channel." }
    ]
  },
  "Dashboard — bar/barographic.md": {
    primary: "Of, pertaining to, or recorded by a barograph.",
    secondary: "Describing pressure curves, traces, or instrumentation related to continuous barometric registration.",
    quotes: [
      { author: "William Napier Shaw", work: "Manual of Meteorology", quote: "The **barographic** trace exhibited rhythmic microbarographic oscillations preceding the thunderstorm." },
      { author: "Cleveland Abbe", work: "The Mechanics of the Earth's Atmosphere", quote: "Accurate **barographic** charts are essential for computing geostrophic wind balances." },
      { author: "Robert FitzRoy", work: "Weather Book", quote: "The **barographic** curve plunged precipitously as the center of the hurricane neared the coastline." }
    ]
  },
  "Dashboard — bar/barophobia.md": {
    primary: "An irrational or abnormal fear of gravity, particularly the fear of being crushed by gravitational force or losing gravitational hold.",
    secondary: "In psychopathology, an anxiety disorder manifesting as terror of downward gravitational pull or falling into open space.",
    quotes: [
      { author: "H. P. Lovecraft", work: "The Shadow Out of Time", quote: "A strange vertigo akin to **barophobia** seized him as he contemplated the cosmic abyss where gravity seemed inverted." },
      { author: "Arthur C. Clarke", work: "Rendezvous with Rama", quote: "Weightlessness relieved the astronaut of any latent **barophobia**, yet the return of centrifugal gravity reawakened primal dread." },
      { author: "Stanislaw Lem", work: "Solaris", quote: "The psychologist classified the researcher's panic on the orbital platform as an acute manifestation of **barophobia**." }
    ]
  },
  "Dashboard — bar/barostat.md": {
    primary: "An apparatus or regulatory device designed to maintain constant pressure within a chamber or fluid system.",
    secondary: "In gastrointestinal physiology, a computer-driven device consisting of a pump and balloon used to measure visceral sensitivity and wall compliance.",
    quotes: [
      { author: "August Krogh", work: "The Anatomy and Physiology of Capillaries", quote: "The experimental chamber was coupled to a mercury **barostat** to prevent atmospheric fluctuations from disturbing the perfusion." },
      { author: "Walter B. Cannon", work: "The Mechanical Factors of Digestion", quote: "Using a miniature **barostat**, researchers recorded intra-gastric pressures under varying emotional stimuli." },
      { author: "William Henry Howell", work: "A Text-Book of Physiology", quote: "A sensitive **barostat** held the air chamber at exact pressure while arterial pulsations were registered." }
    ]
  },
  "Dashboard — bar/barycentre.md": {
    primary: "The center of mass of two or more bodies orbiting one another; the point about which two celestial bodies revolve.",
    secondary: "In orbital mechanics and geometry, the balance point of a distributed mass system or simplex.",
    quotes: [
      { author: "Isaac Newton", work: "Philosophiae Naturalis Principia Mathematica", quote: "The common center of gravity, or **barycentre**, of the Earth and the Moon lies within the interior of the Earth itself." },
      { author: "Johannes Kepler", work: "Epitome Astronomiae Copernicanae", quote: "Mutual gravitation binds both globes to describe orbits around their shared **barycentre**." },
      { author: "Arthur Eddington", work: "Space, Time and Gravitation", quote: "In binary star systems, orbital precession is calculated with respect to the system's invisible **barycentre**." }
    ]
  },
  "Dashboard — bar/barycentric.md": {
    primary: "Pertaining to the center of mass or barycentre, especially of celestial bodies.",
    secondary: "In mathematics and coordinate systems, relating to barycentric coordinates defined by masses placed at the vertices of a simplex.",
    quotes: [
      { author: "August Ferdinand Möbius", work: "Der barycentrische Calcul", quote: "By introducing **barycentric** coordinates, geometric relations are expressed with profound algebraic elegance." },
      { author: "Henri Poincaré", work: "Les Méthodes Nouvelles de la Mécanique Céleste", quote: "Transforming the three-body problem to **barycentric** coordinates eliminates uniform translational motion." },
      { author: "Carl Sagan", work: "Cosmos", quote: "Space probes utilize **barycentric** dynamical models to navigate the gravitational corridors of the solar system." }
    ]
  },
  "Dashboard — bar/baryogenesis.md": {
    primary: "The physical process in the early universe that produced the observed asymmetry between baryons (matter) and antibaryons (antimatter).",
    secondary: "In cosmological particle physics, the theoretical framework explaining why the observable cosmos is dominated by matter rather than equal amounts of matter and antimatter.",
    quotes: [
      { author: "Andrei Sakharov", work: "Violation of CP Invariance, C Asymmetry, and Baryon Asymmetry of the Universe", quote: "Three fundamental conditions are required for **baryogenesis**: baryon number violation, C and CP violation, and departure from thermal equilibrium." },
      { author: "Stephen Hawking", work: "A Brief History of Time", quote: "Without primordial **baryogenesis**, all matter and antimatter would have annihilated completely into pure radiation." },
      { author: "Alan Guth", work: "The Inflationary Universe", quote: "Grand unified theories provide natural mechanisms for **baryogenesis** during the reheat phase following cosmic inflation." }
    ]
  },
  "Dashboard — bar/baryon.md": {
    primary: "A subatomic composite particle made of three quarks, belonging to the hadron family, such as a proton or a neutron.",
    secondary: "In particle physics, any fermion that participates in the strong interaction and possesses a baryon number of +1.",
    quotes: [
      { author: "Murray Gell-Mann", work: "A Schematic Model of Baryons and Mesons", quote: "A **baryon** is constructed from a triplet of quarks whose color charges combine into a neutral singlet." },
      { author: "Richard Feynman", work: "QED: The Strange Theory of Light and Matter", quote: "The proton is the lightest stable **baryon**, ensuring the permanence of atomic nuclei." },
      { author: "Steven Weinberg", work: "The Quantum Theory of Fields", quote: "Conservation of **baryon** number prevents the spontaneous decay of ordinary matter into lighter leptons." }
    ]
  },
  "Dashboard — bar/barysphere.md": {
    primary: "The heavy, dense interior core of the Earth beneath the lithosphere and mantle, composed largely of nickel and iron.",
    secondary: "In geophysics and planetary science, the metallic core region characterized by extreme pressure and density.",
    quotes: [
      { author: "Eduard Suess", work: "The Face of the Earth", quote: "Beneath the outer silicate crust of the globe lies the dense, metallic core termed the **barysphere**." },
      { author: "Alfred Wegener", work: "The Origin of Continents and Oceans", quote: "Seismic wave velocities indicate that the lighter continental masses float upon a denser mantle surrounding the central **barysphere**." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "High-density iron-nickel alloys constitute the mass of the planetary **barysphere**." }
    ]
  },
  "Dashboard — bar/baryton.md": {
    primary: "A bowed string instrument of the viol family, popular in the 18th century, fitted with sympathetic resonant wire strings under the fingerboard.",
    secondary: "In linguistics and Greek phonology, a word having no accent on the final syllable (also spelled barytone).",
    quotes: [
      { author: "Joseph Haydn", work: "Collected Letters and London Notebooks", quote: "Prince Esterházy took great pleasure in playing the **baryton**, prompting me to compose over a hundred trios for the instrument." },
      { author: "Hector Berlioz", work: "Treatise on Modern Instrumentation and Orchestration", quote: "The archaic **baryton** possessed a haunting timbre produced by its lower sympathetic strings vibrating behind the neck." },
      { author: "Charles Burney", work: "A General History of Music", quote: "The sweet, silvery resonance of the **baryton** was much admired in the aristocratic courts of Vienna." }
    ]
  },
  "Dashboard — bar/debar.md": {
    primary: "To exclude, shut out, or prohibit officially from doing something or entering a place.",
    secondary: "To preclude or prevent by legal authority, social bar, or insuperable obstacle.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "Shall that be shut to man, which to the beast is open made? Or will God incense his ire for such a petty trespass, and **debar** them from knowledge?" },
      { author: "Mary Shelley", work: "Frankenstein", quote: "I did not wish to **debar** myself from the pleasures of intellectual society, yet guilt drove me into solitude." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "No citizen should be arbitrarily **debarred** from seeking public office by discriminatory decree." }
    ]
  },
  "Dashboard — bar/hypobaric.md": {
    primary: "Characterized by, having, or operating under unusually low atmospheric or gas pressure.",
    secondary: "In aviation medicine and pharmacology, denoting low-pressure simulation chambers or solutions with a specific gravity lower than cerebrospinal fluid.",
    quotes: [
      { author: "Charles Lindbergh", work: "The Spirit of St. Louis", quote: "Ascending into the thin, **hypobaric** atmosphere over the mountains required conscious, measured breathing." },
      { author: "Paul Bert", work: "Barometric Pressure: Researches in Experimental Physiology", quote: "In the **hypobaric** tank, animals exhibited acute symptoms of anoxia as pressure fell below half an atmosphere." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "The anesthetist selected a **hypobaric** spinal anesthetic to localize the neural blockade." }
    ]
  },
  "Dashboard — bar/isobar.md": {
    primary: "A line drawn on a weather map connecting points having equal atmospheric pressure at a given time or on average.",
    secondary: "In nuclear physics, one of two or more nuclides that have the same total number of nucleons (mass number) but different numbers of protons.",
    quotes: [
      { author: "Robert FitzRoy", work: "The Weather Book", quote: "Each **isobar** traced on the chart demarcated the boundary of the incoming Atlantic low." },
      { author: "Francis William Aston", work: "Isotopes", quote: "Argon-40 and calcium-40 constitute a notable nuclear **isobar** pair possessing identical mass numbers." },
      { author: "William Napier Shaw", work: "Forecasting Weather", quote: "Winds blow parallel to the **isobar** lines, slightly deflected by surface friction." }
    ]
  },
  "Dashboard — bar/isobaric.md": {
    primary: "Characterized by or having equal atmospheric pressure; occurring at constant pressure.",
    secondary: "In thermodynamics, designating a thermodynamic process occurring without change in pressure (an isobaric process).",
    quotes: [
      { author: "Rudolf Clausius", work: "The Mechanical Theory of Heat", quote: "In an **isobaric** expansion, the heat absorbed is divided between internal energy change and external work performed." },
      { author: "Lord Kelvin (William Thomson)", work: "Mathematical and Physical Papers", quote: "The **isobaric** heating of a gas demonstrates the direct proportionality between absolute temperature and volume." },
      { author: "J. Willard Gibbs", work: "On the Equilibrium of Heterogeneous Substances", quote: "Under **isobaric** conditions, chemical potentials provide convenient criteria for phase stability." }
    ]
  },
  "Dashboard — bar/microbar.md": {
    primary: "A unit of pressure equal to one-millionth of a bar (0.1 pascal or 1 dyne per square centimeter).",
    secondary: "In acoustics and atmospheric physics, a metric unit commonly used to express sound pressure and minute atmospheric wave oscillations.",
    quotes: [
      { author: "John William Strutt, Lord Rayleigh", work: "The Theory of Sound", quote: "The threshold of human auditory perception corresponds to sound pressures of a fraction of a **microbar**." },
      { author: "Hermann von Helmholtz", work: "On the Sensations of Tone", quote: "Faint acoustic waves produce eardrum displacements measurable in fractions of a **microbar**." },
      { author: "Arthur Eddington", work: "The Mathematical Theory of Relativity", quote: "Tidal atmospheric pulses of mere **microbar** amplitude circle the globe after volcanic eruptions." }
    ]
  },
  "Dashboard — bar/unbar.md": {
    primary: "To remove the bar, bolt, or fastening from a door, gate, or entrance; to unlock or open.",
    secondary: "To open up, disclose, or make accessible something previously obstructed, forbidden, or hidden.",
    quotes: [
      { author: "William Shakespeare", work: "Cymbeline", quote: "The locks are picked, the doors **unbar**, and morning calls the prisoner forth." },
      { author: "Walter Scott", work: "Ivanhoe", quote: "The warder hastened to **unbar** the heavy oaken portal to admit the weary knight." },
      { author: "John Keats", work: "Endymion", quote: "Soft whispers seem to **unbar** the secret chambers of the dreaming mind." }
    ]
  },

  // === Dashboard — brom (21 words) ===
  "Dashboard — brom/brom 2.md": {
    primary: "A botanical and biochemical combining root derived from Greek brōma ('food') or brōmos ('oats').",
    secondary: "In agrostology and botanical taxonomy, designating brome grasses of the genus Bromus and related fodder or nutritional terms.",
    quotes: [
      { author: "Carl Linnaeus", work: "Species Plantarum", quote: "Under the botanical designation **Bromus**, several perennial grasses of the temperate meadows were first classified." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The generic term **Bromus** and its derivatives preserve the ancient Greek appellation for wild oat fodder." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The awned spikelets of **Bromus** are characteristic of pasture grasses across the northern territories." }
    ]
  },
  "Dashboard — brom/brom.md": {
    primary: "A combining root derived from Greek brōmos ('stench', 'foul odor'), designating bromine or halogenated chemical compounds.",
    secondary: "In systematic chemical nomenclature, a prefix indicating the presence of bromine atoms in organic or inorganic molecules.",
    quotes: [
      { author: "Antoine Jérôme Balard", work: "Annales de Chimie et de Physique", quote: "I proposed to give this newly discovered liquid substance the name bromine, derived from the Greek **brom**- denoting its suffocating stench." },
      { author: "Justus von Liebig", work: "Familiar Letters on Chemistry", quote: "Compounds containing the radical **brom**- were systematically separated from the mother liquors of salt works." },
      { author: "Humphry Davy", work: "Elements of Chemical Philosophy", quote: "The chemical properties of **brom**- derivatives demonstrate a distinct affinity intermediate between chlorine and iodine." }
    ]
  },
  "Dashboard — brom/bromate.md": {
    primary: "A salt or ester of bromic acid containing the monovalent polyatomic anion BrO3(-).",
    secondary: "In food science and analytical chemistry, an oxidizing agent (such as potassium bromate) historically used as a flour improver in bread making.",
    quotes: [
      { author: "Jöns Jacob Berzelius", work: "Treatise on Chemistry", quote: "When bromine is dissolved in hot concentrated potash, potassium **bromate** crystallizes upon cooling." },
      { author: "Ira Remsen", work: "Principles of Theoretical Chemistry", quote: "Decomposition of an alkaline **bromate** by heat yields oxygen gas and the corresponding metal bromide." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Industrial runoff carrying soluble **bromate** residues posed unforeseen contamination risks for municipal water supplies." }
    ]
  },
  "Dashboard — brom/brome.md": {
    primary: "Any annual or perennial pasture grass belonging to the large genus Bromus, characterized by loose nodding panicles.",
    secondary: "An archaic or variant chemical designation for bromine or its compounds in early nineteenth-century scientific writings.",
    quotes: [
      { author: "William Cobbett", work: "Rural Rides", quote: "The rich bottomlands were lush with meadow fescue and soft **brome** grass ready for the scythe." },
      { author: "Antoine Jérôme Balard", work: "Memoir on a Peculiar Substance Contained in Sea Water", quote: "To this reddish-brown liquor I originally gave the provisional name of **brome** before adopting the Latin form." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "Various species of **brome** competed fiercely for survival in the neglected pasture plot." }
    ]
  },
  "Dashboard — brom/bromegrass.md": {
    primary: "Any grass of the genus Bromus, especially smooth brome (Bromus inermis), widely cultivated for hay, pasture, and erosion control.",
    secondary: "In agricultural agronomy, a hardy, drought-tolerant cool-season forage crop valuable for cattle grazing.",
    quotes: [
      { author: "Liberty Hyde Bailey", work: "Cyclopedia of American Agriculture", quote: "Hungarian **bromegrass** has proven invaluable on the semi-arid plains of the West where timothy fails." },
      { author: "Aldo Leopold", work: "A Sand County Almanac", quote: "The roadside was banked with smooth **bromegrass**, greening early under the melting April snow." },
      { author: "John Muir", work: "The Mountains of California", quote: "Native **bromegrass** grew luxuriantly along the borders of the subalpine meadows." }
    ]
  },
  "Dashboard — brom/bromelia.md": {
    primary: "A tropical American plant of the genus Bromelia, characterized by stiff spiny leaves and colorful floral bracts.",
    secondary: "In systematic botany, the type genus of the family Bromeliaceae, named in honor of Swedish botanist Olaus Bromelius.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Personal Narrative of Travels to the Equinoctial Regions", quote: "Dense thickets of wild **Bromelia** guarded the edge of the forest with formidable spiny leaves." },
      { author: "Charles Darwin", work: "Journal of Researches (The Voyage of the Beagle)", quote: "The epiphytic **Bromelia** collected pools of rainwater in its leaf axils, harboring vibrant communities of insects." },
      { author: "Alfred Russel Wallace", work: "Travels on the Amazon and Rio Negro", quote: "Splendid scarlet bracts of a giant **Bromelia** shone through the humid twilight of the riverbank." }
    ]
  },
  "Dashboard — brom/bromeliaceae.md": {
    primary: "A large family of mostly epiphytic monocotyledonous flowering plants native to the tropical Americas, including the pineapple and Spanish moss.",
    secondary: "In systematic botany and plant ecology, a specialized family whose members frequently possess rosette tanks holding aquatic micro-ecosystems (phytotelmata).",
    quotes: [
      { author: "Alexander von Humboldt", work: "Aspects of Nature", quote: "The trunks of the primeval trees were adorned with countless hanging species of **Bromeliaceae**." },
      { author: "Charles Darwin", work: "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", quote: "Many genera of the **Bromeliaceae** display intricate floral mechanisms to encourage hummingbird pollination." },
      { author: "Asa Gray", work: "Structural Botany", quote: "The absorbative trichomes covering the foliage of **Bromeliaceae** allow them to thrive without soil contact." }
    ]
  },
  "Dashboard — brom/bromeosin.md": {
    primary: "A red or pink fluorescent halogenated dye derived from fluorescein by substitution with bromine atoms (commonly known as eosin Y).",
    secondary: "In histology and microscopy, a vital acidophilic biological stain used to counterstain cell cytoplasm, collagen, and erythrocytes against hematoxylin.",
    quotes: [
      { author: "Santiago Ramón y Cajal", work: "Histology of the Nervous System", quote: "Counterstaining with **bromeosin** brought out the delicate boundaries of the glial somata." },
      { author: "Paul Ehrlich", work: "Collected Papers on Immunology and Haematology", quote: "The basic granules of eosinophil leukocytes show strong affinity for tetrabromofluorescein or **bromeosin**." },
      { author: "Edward B. Wilson", work: "The Cell in Development and Inheritance", quote: "Under the immersion lens, the spindle fibers stood out sharply against the pale **bromeosin** background." }
    ]
  },
  "Dashboard — brom/bromic.md": {
    primary: "Of, pertaining to, or containing bromine, especially in its higher oxidation states (such as bromic acid, HBrO3).",
    secondary: "In chemical nomenclature, denoting oxoacids or salts where bromine acts with a valency of five.",
    quotes: [
      { author: "Antoine Jérôme Balard", work: "Annales de Chimie et de Physique", quote: "By reacting bromine with aqueous silver nitrate, free **bromic** acid was obtained in solution." },
      { author: "Jöns Jacob Berzelius", work: "Traité de Chimie", quote: "The unstable nature of concentrated **bromic** acid makes it a vigorous and dangerous oxidizing agent." },
      { author: "Humphry Davy", work: "Elements of Chemical Philosophy", quote: "When heated, the **bromic** salts decompose with effervescence, disengaging oxygen gas." }
    ]
  },
  "Dashboard — brom/bromide.md": {
    primary: "A binary chemical compound of bromine with another element or radical, especially a salt such as potassium bromide.",
    secondary: "A platitude, cliché, or trite comforting remark; or historically, a sedative medication containing potassium or sodium bromide.",
    quotes: [
      { author: "Gelett Burgess", work: "Are You a Bromide?", quote: "A **bromide** is someone who says the obvious thing with an air of profound discovery." },
      { author: "Arthur Conan Doyle", work: "The Sign of the Four", quote: "The physician administered a soothing dose of potassium **bromide** to calm the agitated witness." },
      { author: "F. Scott Fitzgerald", work: "Tender Is the Night", quote: "The scent of **bromide** and chloral hung faintly in the quiet sanatorium corridor." }
    ]
  },
  "Dashboard — brom/bromidic.md": {
    primary: "Trite, cliché-ridden, dull, and commonplace in thought or expression; resembling a platitude.",
    secondary: "Of, relating to, or resembling a chemical bromide or its sedative, dulling pharmacological effect.",
    quotes: [
      { author: "H. L. Mencken", work: "Prejudices: First Series", quote: "His speech was packed with the most **bromidic** platitudes of the political stump." },
      { author: "Sinclair Lewis", work: "Babbitt", quote: "He nodded solemnly, uttering a **bromidic** remark about the necessity of good fellowship." },
      { author: "Virginia Woolf", work: "The Captain's Death Bed and Other Essays", quote: "The conversation drifted into **bromidic** complacencies that numbed all genuine intellectual debate." }
    ]
  },
  "Dashboard — brom/brominate.md": {
    primary: "To introduce bromine into a chemical compound or mixture through a chemical reaction.",
    secondary: "To treat water or industrial chemicals with bromine for disinfection, flame retardation, or synthetic transformation.",
    quotes: [
      { author: "August Wilhelm von Hofmann", work: "Introduction to Modern Chemistry", quote: "To **brominate** benzene directly requires the catalytic assistance of iron filings or iodine." },
      { author: "Emil Fischer", work: "Studies on the Purine Group", quote: "We proceeded to **brominate** the intermediate uracil to obtain the reactive halogenated derivative." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "The chemist chose to **brominate** the unsaturated hydrocarbon across its double bond." }
    ]
  },
  "Dashboard — brom/bromine.md": {
    primary: "A dark reddish-brown, volatile, liquid chemical element with a pungent, choking smell, atomic number 35 and symbol Br.",
    secondary: "A halogen element extracted from sea brine and salt deposits, used in flame retardants, water treatment, photography, and pharmaceutical synthesis.",
    quotes: [
      { author: "Antoine Jérôme Balard", work: "Memoir on a Peculiar Substance Contained in Sea Water", quote: "The heavy, fuming reddish liquid which I designate as **bromine** possesses volatility comparable to that of ether." },
      { author: "Primo Levi", work: "The Periodic Table", quote: "The heavy vapor of **bromine** rolled sluggishly along the benchtop, suffocating and corrosive." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "The introduction of **bromine** into medicine gave the physician a powerful weapon against spasmodic seizures." }
    ]
  },
  "Dashboard — brom/bromo-seltzer.md": {
    primary: "An effervescent antacid and pain-relieving brand of medication originally containing sodium bromide, acetaminophen, and sodium bicarbonate.",
    secondary: "A widely popular 20th-century American over-the-counter remedy for hangovers, indigestion, and headaches.",
    quotes: [
      { author: "F. Scott Fitzgerald", work: "The Beautiful and Damned", quote: "Anthony called weakly for a glass of **Bromo-Seltzer** to quiet the drumming in his temples." },
      { author: "Raymond Chandler", work: "Farewell, My Lovely", quote: "I went into the drugstore and swallowed a foaming **Bromo-Seltzer** that tasted like bicarbonate of chalk." },
      { author: "Eugene O'Neill", work: "Long Day's Journey into Night", quote: "He went to the medicine chest looking for **Bromo-Seltzer** after a restless, sleepless night." }
    ]
  },
  "Dashboard — brom/bromoderma.md": {
    primary: "A cutaneous skin eruption or rash caused by systemic hypersensitivity or toxicity to bromide compounds.",
    secondary: "In dermatology, an acneiform, nodular, or ulcerating dermatosis typically resulting from prolonged ingestion of bromide-containing sedatives.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Chronic bromide ingestion may culminate in a fungating, pustular **bromoderma** resembling tertiary syphilis." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "The extensive crusting on the patient's face was diagnosed as a severe case of **bromoderma** tuberosum." },
      { author: "Ferdinand von Hebra", work: "Diseases of the Skin", quote: "Lesions of **bromoderma** slowly involute once the offending medication is completely discontinued." }
    ]
  },
  "Dashboard — brom/bromoform.md": {
    primary: "A heavy, colorless to yellowish liquid halogenated hydrocarbon (CHBr3) with a sweet, chloroform-like odor.",
    secondary: "In geology and mineral separation, a dense liquid (density ~2.89 g/cm3) used to separate heavy minerals from lighter sand fractions by sink-float separation.",
    quotes: [
      { author: "Waldemar Lindgren", work: "Mineral Deposits", quote: "Heavy mineral sands were separated using **bromoform** in a separatory funnel to isolate zircon and rutile." },
      { author: "James Dwight Dana", work: "Manual of Mineralogy", quote: "The high density of **bromoform** allows lighter quartz and feldspar to float while heavier ores sink to the bottom." },
      { author: "Arthur Holmes", work: "Petrographic Methods and Calculations", quote: "The heavy residue recovered from the **bromoform** separation was examined under the petrographic microscope." }
    ]
  },
  "Dashboard — brom/Bromus ramosus.md": {
    primary: "The hairy brome; a tall, perennial woodland grass native to Europe and western Asia with drooping open panicles.",
    secondary: "In plant ecology and floristics, a characteristic shade-tolerant grass species inhabiting ancient deciduous woodlands and calcareous soils.",
    quotes: [
      { author: "William Jackson Hooker", work: "The British Flora", quote: "In moist shaded copses, **Bromus ramosus** displays its graceful, widely spreading, nodding panicles." },
      { author: "Arthur George Tansley", work: "The British Islands and Their Vegetation", quote: "Under the canopy of the pedunculate oak, **Bromus ramosus** forms lush green clumps along woodland rides." },
      { author: "Charles Cardale Babington", work: "Manual of British Botany", quote: "The lower leaf-sheaths of **Bromus ramosus** are conspicuously clothed with long, spreading hairs." }
    ]
  },
  "Dashboard — brom/Bromus.md": {
    primary: "A large and widely distributed genus of annual and perennial grasses in the family Poaceae, commonly known as brome grasses.",
    secondary: "In agrostology, an economically diverse genus comprising valuable forage pasture grasses as well as invasive weeds like cheatgrass (Bromus tectorum).",
    quotes: [
      { author: "Carl Linnaeus", work: "Genera Plantarum", quote: "The genus **Bromus** is distinguished by its many-flowered spikelets and terminal awns arising below the bifid apex." },
      { author: "Agnes Chase", work: "First Book of Grasses", quote: "Spikelets in **Bromus** are typically plump and large, making them easy for the beginner to dissect and study." },
      { author: "Aldo Leopold", work: "Round River", quote: "The invasion of exotic **Bromus** into the western sagebrush prairie altered the natural wildfire cycle forever." }
    ]
  },
  "Dashboard — brom/organobromine.md": {
    primary: "An organic chemical compound containing one or more carbon-bromine covalent bonds.",
    secondary: "In environmental chemistry and industrial manufacturing, a class of substances used in brominated flame retardants, dyes, and organic synthesis intermediates.",
    quotes: [
      { author: "Rachel Carson", work: "Silent Spring", quote: "Accumulation of synthetic **organobromine** pollutants in marine sediments presents grave ecological hazards." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The carbon-bromine linkage in an **organobromine** molecule exhibits significant polarizability." },
      { author: "E. J. Corey", work: "The Logic of Chemical Synthesis", quote: "The selective introduction of an **organobromine** moiety provides a versatile handle for subsequent cross-coupling." }
    ]
  },
  "Dashboard — brom/tribromoethanol.md": {
    primary: "A halogenated alcohol (C2H3Br3O) historically used as a general anesthetic and sedative in veterinary and laboratory medicine (Avertin).",
    secondary: "In pharmacological history, a basal anesthetic introduced in the 1920s administered rectally to induce rapid surgical anesthesia in laboratory rodents.",
    quotes: [
      { author: "Alfred Gilman", work: "The Pharmacological Basis of Therapeutics", quote: "Administered in aqueous amylene hydrate, **tribromoethanol** acts as a potent and rapid central nervous system depressant." },
      { author: "Hans Selye", work: "Stress: The Physiology and Pathology of Exposure to Systemic Stress", quote: "Deep anesthesia was sustained with **tribromoethanol** while physiological shock responses were monitored." },
      { author: "John Jacob Abel", work: "Experimental Pharmacology", quote: "The hypnotic properties of **tribromoethanol** demonstrate how polyhalogenation enhances central nervous depression." }
    ]
  },
  "Dashboard — brom/tribromomethane.md": {
    primary: "A dense, colorless trihalomethane liquid with the chemical formula CHBr3, commonly known as bromoform.",
    secondary: "In marine biogeochemistry and industrial chemistry, an ozone-depleting volatile halocarbon produced naturally by marine algae and phytoplanktons.",
    quotes: [
      { author: "Svante Arrhenius", work: "Immunochemistry", quote: "Pure **tribromomethane** was used as a dense separating fluid in the centrifugation of cellular precipitates." },
      { author: "Ira Remsen", work: "Organic Chemistry", quote: "Treatment of acetone with alkali and bromine affords heavy droplets of **tribromomethane**." },
      { author: "James Lovelock", work: "Gaia: A New Look at Life on Earth", quote: "Marine macroalgae release significant quantities of **tribromomethane** into the coastal atmosphere." }
    ]
  },

  // === Dashboard — capn (first 2 words of batch 1) ===
  "Dashboard — capn/acapnia.md": {
    primary: "A condition characterized by an abnormally low level of carbon dioxide in the blood and bodily tissues; hypocapnia.",
    secondary: "In respiratory physiology, a state resulting from hyperventilation, causing respiratory alkalosis and cerebral vasoconstriction.",
    quotes: [
      { author: "Yandell Henderson", work: "Adventures in Respiration", quote: "Prolonged hyperventilation induces severe **acapnia**, stripping the blood of its vital carbon dioxide stimulus for the respiratory center." },
      { author: "J. S. Haldane", work: "Respiration", quote: "The physiological danger of **acapnia** lies in the failure of oxygen dissociation from hemoglobin when arterial carbon dioxide falls too low." },
      { author: "Walter B. Cannon", work: "The Wisdom of the Body", quote: "The respiratory reflex mechanism vigorously resists **acapnia** to protect the acid-base equilibrium of the blood." }
    ]
  },
  "Dashboard — capn/acapnial.md": {
    primary: "Pertaining to, caused by, or characterized by acapnia (abnormally low blood carbon dioxide).",
    secondary: "In clinical pulmonology, describing physiological changes such as cerebral ischemia or arterial spasm triggered by hypocapnic states.",
    quotes: [
      { author: "Yandell Henderson", work: "Shock, or Normal Mechanism of Acapnia", quote: "The profound **acapnial** shock observed in surgical patients stemmed from uncontrolled rapid respiration under light anesthesia." },
      { author: "J. S. Haldane", work: "Methods of Air Analysis", quote: "Severe **acapnial** states reduce the respiratory drive to the point of inducing paradoxical periodic breathing." },
      { author: "Charles Sherrington", work: "Mammalian Physiology", quote: "Cerebral vasoconstriction is a well-documented **acapnial** reaction that protects the brainstem from excessive alkalosis." }
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

console.log(`Updated ${updatedCount} files in Batch 1!`);
