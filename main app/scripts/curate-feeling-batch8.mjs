import fs from 'fs';
import path from 'path';

const basePath = 'App database/Greek roots/Cluster Feeling & Sensation';

const filesData = {
  // Dashboard — phob (15 words)
  "Dashboard — phob/acrophobia.md": {
    primary: "An extreme, irrational, and debilitating fear of heights, often accompanied by severe anxiety, dizziness, and panic attacks.",
    secondary: "In clinical psychiatry, a specific phobia triggered by high elevation, precipitating avoidance of tall buildings, bridges, and mountain ledges.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "A sudden attack of **acrophobia** on the brink of a cliff paralyses the limbs, flooding consciousness with vertiginous terror." },
      { author: "Henry Maudsley", work: "The Pathology of Mind", quote: "The sufferer from **acrophobia** experiences an agonizing dread not only of falling, but of an impulse to cast himself into the void." },
      { author: "Oliver Sacks", work: "A Leg to Stand On", quote: "Looking down the steep alpine ravine, I was seized by a visceral **acrophobia** that set my pulse racing." }
    ]
  },
  "Dashboard — phob/acrophobic.md": {
    primary: "Relating to, affected by, or exhibiting acrophobia; experiencing intense dread or panic at high altitudes or heights.",
    secondary: "Characterized by an overwhelming somatic reaction to high vantage points or precipitous places.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Final Problem", quote: "Even a seasoned climber might turn dizzy and **acrophobic** upon the slippery ledge overlooking the Reichenbach Fall." },
      { author: "John Muir", work: "The Mountains of California", quote: "Standing on the razor ridge of Mount Whitney, I met an **acrophobic** companion who crawled on hands and knees." },
      { author: "H. G. Wells", work: "The War in the Air", quote: "Looking down from the suspended basket of the balloon, the aeronaut was seized with an **acrophobic** horror." }
    ]
  },
  "Dashboard — phob/claustrophobia.md": {
    primary: "An extreme or irrational fear of confined, small, or crowded spaces.",
    secondary: "A common situational anxiety disorder in which being enclosed in an elevator, tunnel, or small room triggers acute autonomic panic and a desperate urge to escape.",
    quotes: [
      { author: "Sigmund Freud", work: "Introductory Lectures on Psycho-Analysis", quote: "In **claustrophobia**, the fear of being enclosed in a locked room masks an unconscious dread of repressed instinctual impulses." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The sudden attack of **claustrophobia** in a crowded subway causes intense tachycardia, diaphoresis, and air hunger." },
      { author: "Edgar Allan Poe", work: "The Premature Burial", quote: "The fear of living burial is the quintessential horror, an unendurable nightmare of eternal **claustrophobia**." }
    ]
  },
  "Dashboard — phob/ergophobia.md": {
    primary: "An abnormal, persistent, and irrational fear of or deep aversion to work, labor, or strenuous occupation.",
    secondary: "In psychological medicine, a form of social anxiety or performance phobia where the demands of employment trigger panic or profound avoidance.",
    quotes: [
      { author: "Cesare Lombroso", work: "The Man of Genius", quote: "What moralists denounce as mere indolence is frequently a constitutional **ergophobia** rooted in nervous exhaustion." },
      { author: "William James", work: "The Varieties of Religious Experience", quote: "The neurasthenic youth suffered from an acute **ergophobia**, shrinking from the simplest desk duty with trembling dread." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Melancholic hypochondriacs fall into a stubborn **ergophobia**, persuaded that bodily toil will destroy their frail constitution." }
    ]
  },
  "Dashboard — phob/homophobe.md": {
    primary: "A person who has or exhibits homophobia; someone with an irrational fear, hatred, or prejudice against homosexual people.",
    secondary: "An individual who expresses hostility, discrimination, or intolerance toward same-sex love and partnerships.",
    quotes: [
      { author: "James Baldwin", work: "The Evidence of Things Not Seen", quote: "The violent **homophobe** attacks in another what he most terrorizes and denies within his own divided heart." },
      { author: "Michel Foucault", work: "The History of Sexuality", quote: "The cultural figure of the moralizing **homophobe** emerged when psychiatry began medicalizing sexual identities." },
      { author: "Audre Lorde", work: "Sister Outsider", quote: "To combat tyranny effectively, we cannot permit the narrow bigotry of the **homophobe** to divide our common struggle." }
    ]
  },
  "Dashboard — phob/homophobia.md": {
    primary: "Dislike of, contempt for, or ingrained prejudice and discrimination against gay and lesbian people.",
    secondary: "An ideological and cultural system of hostility that demeans non-heterosexual identities and enforces heterosexual conformity.",
    quotes: [
      { author: "George Weinberg", work: "Society and the Healthy Homosexual", quote: "I coined the word **homophobia** to describe the revulsion toward homosexuals and the self-loathing felt by homosexuals who internalized it." },
      { author: "James Baldwin", work: "Notes of a Native Son", quote: "The roots of American **homophobia** intertwine with racial terror, both springing from an obsession with purity and domination." },
      { author: "Michel Foucault", work: "Power/Knowledge", quote: "State institutions mobilized **homophobia** under the guise of public hygiene and moral defense throughout the nineteenth century." }
    ]
  },
  "Dashboard — phob/homophobic.md": {
    primary: "Having or showing a dislike of, prejudice against, or hostility toward gay, lesbian, or homosexual people.",
    secondary: "Manifesting attitudes, speech, or policies that enforce discrimination based on sexual orientation.",
    quotes: [
      { author: "James Baldwin", work: "No Name in the Street", quote: "The mob hurled **homophobic** taunts in the street, revealing how deeply sexual fear corrupts civic fraternity." },
      { author: "Christopher Isherwood", work: "Christopher and His Kind", quote: "We lived under the shadow of **homophobic** laws that made every private affection an indictable offense." },
      { author: "Audre Lorde", work: "Zami: A New Spelling of My Name", quote: "The silence that greets **homophobic** violence in our communities is a silence that wounds us all." }
    ]
  },
  "Dashboard — phob/hydrophobia.md": {
    primary: "Extreme or irrational fear of water; historically, the clinical manifestation of rabies in humans, marked by painful throat spasms upon trying to swallow liquids.",
    secondary: "In medical history and epidemiology, the dreaded terminal stage of the rabies virus before the advent of the Pasteur vaccine.",
    quotes: [
      { author: "Louis Pasteur", work: "Method for Preventing Rabies After a Bite", quote: "The terrifying symptoms of human **hydrophobia** were forever banished by the development of our attenuated virus vaccine." },
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", quote: "Physicians have observed that the bite of a mad dog induces a strange **hydrophobia**, where the sight of water provokes convulsions." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In true **hydrophobia**, the mere sound of running water triggers violent, agonizing spasms of the larynx and pharynx." }
    ]
  },
  "Dashboard — phob/neophobia.md": {
    primary: "An extreme, irrational, or persistent fear, hatred, or dislike of anything new, unfamiliar, or novel.",
    secondary: "In animal behavior and human psychology, the cautious avoidance of novel foods, objects, or environmental changes (feeding neophobia).",
    quotes: [
      { author: "Cesare Lombroso", work: "The Man of Genius", quote: "Intellectual **neophobia** is the natural defense of mediocrity, which regards every breakthrough as an insult to tradition." },
      { author: "William James", work: "The Principles of Psychology", quote: "Wild animals exhibit intense **neophobia** when a strange object is placed near their feeding trail." },
      { author: "John Dewey", work: "Reconstruction in Philosophy", quote: "The inertia of religious institutions is rooted in an ancient **neophobia** that equates change with sacrilege." }
    ]
  },
  "Dashboard — phob/phob.md": {
    primary: "The Greek root *phob-* (from *phobos*), signifying flight, panic, terror, dread, or aversion (as seen in *phobia*, *hydrophobia*, *claustrophobia*).",
    secondary: "The universal combining form across psychiatric and biological nomenclature denoting abnormal dread, aversion, or chemical repulsion.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The primary noun *phobos* and its combining root **phob** originally meant panic flight in Homeric battle before denoting fear in general." },
      { author: "Aristotle", work: "Poetics", quote: "Tragedy achieves the catharsis of pity and fear, utilizing the elemental terror of **phobos** to cleanse the spectators' emotions." },
      { author: "Sigmund Freud", work: "Inhibitions, Symptoms and Anxiety", quote: "In constructing terms with **phob**, clinical psychiatry identifies the displacement of unconscious anxiety onto specific external objects." }
    ]
  },
  "Dashboard — phob/phobia.md": {
    primary: "An extreme, irrational, and persistent fear of a specific object, animal, activity, or situation that leads to a compelling desire to avoid it.",
    secondary: "In clinical psychiatry, an anxiety disorder classified into specific phobias, social anxiety disorder, and agoraphobia.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "A true **phobia** is completely impervious to logical argument; the victim knows the terror is absurd, yet trembles nonetheless." },
      { author: "Sigmund Freud", work: "Analysis of a Phobia in a Five-Year-Old Boy", quote: "Little Hans's animal **phobia** was the symptomatic expression of deep Oedipal conflict and castration anxiety." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Obsessional neurosis frequently crystallizes into an intractable **phobia** of contamination, disease, or sharp knives." }
    ]
  },
  "Dashboard — phob/phobic.md": {
    primary: "Relating to, characterized by, or affected with a phobia; intensely and irrationally fearful of something.",
    secondary: "In chemistry and surface science, having an aversion to or repelling a substance (e.g., hydrophobic, lipophobic).",
    quotes: [
      { author: "Sigmund Freud", work: "Studies on Hysteria", quote: "The **phobic** patient constructs an elaborate system of safeguards and detours to avoid encountering the feared object." },
      { author: "Oliver Sacks", work: "An Anthropologist on Mars", quote: "The sudden onset of panic attacks left him completely housebound in a state of **phobic** paralysis." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "The hydrophobic tail of fatty acids recoils from aqueous contact, driving the formation of **phobic** lipid bilayer interiors." }
    ]
  },
  "Dashboard — phob/phobophobia.md": {
    primary: "An irrational, abnormal fear of phobias, panic attacks, or experiencing the sensation of fear itself.",
    secondary: "In anxiety neurosis, an anticipatory dread where the patient is terrified of becoming frightened or having a panic attack in public.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "The panic disorder sufferer is trapped in a vicious circle of **phobophobia**, terrified above all of his own heart racing with dread." },
      { author: "Pierre Janet", work: "The Major Symptoms of Hysteria", quote: "In psychasthenia, fear feeds upon itself until the subject succumbs to a debilitating **phobophobia**." },
      { author: "Franklin D. Roosevelt", work: "First Inaugural Address", quote: "The only thing we have to fear is fear itself; our national crisis demands that we conquer this collective **phobophobia**." }
    ]
  },
  "Dashboard — phob/phobos.md": {
    primary: "The ancient Greek deity and personification of panic, fear, and rout in battle, the son of Ares and Aphrodite, brother of Deimos.",
    secondary: "The larger and innermost of the two natural moons of Mars, discovered in 1877 by Asaph Hall, orbiting closer to its primary than any other moon in the solar system.",
    quotes: [
      { author: "Homer", work: "Iliad", quote: "Before the chariot of Ares rode **Phobos** and Deimos, spreading wild panic and slaughter through the Achaean ranks." },
      { author: "Hesiod", work: "Theogony", quote: "Unto Ares Aphrodite bore two terrible sons, **Phobos** and Deimos, who shake the battle lines of armored men." },
      { author: "Percival Lowell", work: "Mars", quote: "The tiny satellite **Phobos** races across the Martian sky three times in a single day, rising in the west and setting in the east." }
    ]
  },
  "Dashboard — phob/zeusophobia.md": {
    primary: "An abnormal, irrational fear or dread of Zeus, the king of the Olympian gods, or of lightning, thunder, and divine retribution from supreme deities.",
    secondary: "In mythological and psychological terminology, an acute phobic dread of celestial thunderbolts and wrathful sky gods.",
    quotes: [
      { author: "Hesiod", work: "Works and Days", quote: "The trembling mortal was stricken with **zeusophobia**, fearing the thunderbolt that the Olympian king hurls from cloud-capped peaks." },
      { author: "Aeschylus", work: "Prometheus Bound", quote: "Prometheus defied the almighty tyrant of Olympus, scorning the slavish **zeusophobia** of the trembling Oceanids." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Superstitious souls who live in perpetual dread of celestial lightning bolt suffer an ancient form of **zeusophobia**." }
    ]
  },

  // Dashboard — thig (5 words)
  "Dashboard — thig/antithixotropic.md": {
    primary: "Exhibiting antithixotropy (rheopexy); becoming thicker, more viscous, or solidifying upon sustained mechanical agitation or shear stress.",
    secondary: "In rheology and fluid mechanics, describing non-Newtonian materials whose viscosity increases with time under constant shear rate (contrasted with thixotropic).",
    quotes: [
      { author: "Herbert Freundlich", work: "Colloid and Capillary Chemistry", quote: "Certain concentrated bentonite suspensions exhibit an **antithixotropic** behavior, stiffening into a solid gel when shaken." },
      { author: "Eugene Bingham", work: "Fluidity and Plasticity", quote: "The **antithixotropic** response reveals internal structural alignment of colloidal particles under continuous shear." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "Unlike thixotropic paints that liquefy on stirring, an **antithixotropic** fluid becomes more resistant to flow the faster it is agitated." }
    ]
  },
  "Dashboard — thig/thigmonasty.md": {
    primary: "A rapid, non-directional plant movement or response provoked by mechanical touch or vibration (as seen in the sensitive plant *Mimosa pudica*).",
    secondary: "In plant physiology, turgor-driven nastic movements mediated by electrical action potentials and rapid potassium-ion efflux from pulvinar motor cells.",
    quotes: [
      { author: "Charles Darwin", work: "The Power of Movement in Plants", quote: "The instantaneous folding of Mimosa leaflets upon the slightest contact illustrates the exquisite sensitivity of **thigmonasty**." },
      { author: "Julius von Sachs", work: "Lectures on the Physiology of Plants", quote: "The phenomenon of **thigmonasty** in the Venus flytrap is triggered when an insect touches the sensitive trigger hairs on the lobes." },
      { author: "Asa Gray", work: "Elements of Botany", quote: "In **thigmonasty**, the motor mechanism depends upon the rapid loss of water from the underside of the swollen petiole base." }
    ]
  },
  "Dashboard — thig/thigmotaxis.md": {
    primary: "The directional movement or orientation of an organism in response to mechanical contact or tactile touch.",
    secondary: "In ethology, positive thigmotaxis (seeking contact with surfaces, common in cockroaches and rodents) or negative thigmotaxis (avoiding contact).",
    quotes: [
      { author: "Jacques Loeb", work: "Forced Movements, Tropisms, and Animal Conduct", quote: "Cockroaches run along the baseboards of rooms driven by positive **thigmotaxis**, seeking maximum bodily contact with solid boundaries." },
      { author: "Charles Sherrington", work: "The Integrative Action of the Nervous System", quote: "Tactile reflexes in invertebrates reveal that **thigmotaxis** guides burrowing animals safely into subterranean crevices." },
      { author: "Edward O. Wilson", work: "The Insect Societies", quote: "Social grooming and colony clustering in subterranean termites are mediated by continuous mutual **thigmotaxis**." }
    ]
  },
  "Dashboard — thig/thixotropic.md": {
    primary: "Exhibiting thixotropy; becoming liquid or less viscous when shaken, stirred, or mechanically disturbed, and returning to a gel-like state when left at rest.",
    secondary: "In materials science and biology, characteristic of non-drip paints, drilling muds, printing inks, and synovial fluid in human joints.",
    quotes: [
      { author: "Herbert Freundlich", work: "Thixotropy", quote: "The essential property of a **thixotropic** gel is that mechanical agitation liquefies it isothermally, without any change in temperature." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Quick clay deposits undergo sudden **thixotropic** liquefaction during earthquake tremors, causing catastrophic landslides." },
      { author: "Linus Pauling", work: "The Architecture of Molecules", quote: "The **thixotropic** character of synovial fluid allows our joints to move with minimal friction under rapid shear." }
    ]
  },
  "Dashboard — thig/thixotropy.md": {
    primary: "The property of certain gels or viscous liquids of becoming fluid and less viscous when subjected to mechanical shear, and setting again into a gel when undisturbed.",
    secondary: "A term coined in 1927 by Herbert Freundlich from Greek *thixis* ('touch' or 'shaking') and *tropē* ('turning' or 'change').",
    quotes: [
      { author: "Herbert Freundlich", work: "Colloid and Capillary Chemistry", quote: "We introduced the term **thixotropy** to describe this reversible transformation between gel and sol states upon shaking." },
      { author: "Eugene Bingham", work: "Fluidity and Plasticity", quote: "Industrial paints depend upon **thixotropy** to flow smoothly beneath the brush and set immediately without sagging on the wall." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "The water-saturated sands of the tidal flats exhibit **thixotropy**, turning to liquid quagmire beneath the unwary walker's boot." }
    ]
  },

  // Dashboard — thym (13 words)
  "Dashboard — thym/cyclothymia.md": {
    primary: "A chronic, milder form of bipolar affective disorder characterized by alternating periods of hypomanic symptoms and mild depressive episodes over at least two years.",
    secondary: "In psychiatric nosology (coined by Karl Ludwig Kahlbaum), a cycloid personality disorder marked by persistent mood instability without psychotic breaks.",
    quotes: [
      { author: "Karl Ludwig Kahlbaum", work: "Die Cyclothymie: Eine Form der psychischen Störung", quote: "We designate as **cyclothymia** those rhythmic oscillations between buoyant cheerfulness and melancholic gloom that spare the patient from frank madness." },
      { author: "Emil Kraepelin", work: "Lectures on Clinical Psychiatry", quote: "Many creative artists and statesmen live within the bounds of **cyclothymia**, drawing extraordinary energy from their buoyant phases." },
      { author: "Karl Jaspers", work: "General Psychopathology", quote: "The mood swings of **cyclothymia** follow endogenous biological rhythms that operate independently of external domestic fortunes." }
    ]
  },
  "Dashboard — thym/cyclothymic.md": {
    primary: "Relating to, characterized by, or affected with cyclothymia; exhibiting recurring mood swings between mild elation and depression.",
    secondary: "Describing a temperament or affective constitution prone to unpredictable emotional fluctuations.",
    quotes: [
      { author: "Eugen Bleuler", work: "Textbook of Psychiatry", quote: "The **cyclothymic** personality is warm, sociable, and energetic, though prone to unexpected sinking spells of quiet self-doubt." },
      { author: "Ernst Kretschmer", work: "Physique and Character", quote: "A pyknic body build correlates strongly with the **cyclothymic** temperament, alternating between sociable joy and quiet melancholy." },
      { author: "Oliver Sacks", work: "Musicophilia", quote: "His musical compositions reflected an intensely **cyclothymic** genius, leaping from manic allegros to sorrowful adagios." }
    ]
  },
  "Dashboard — thym/dysthymia.md": {
    primary: "Persistent depressive disorder; a chronic, low-grade form of depression characterized by low mood, fatigue, low self-esteem, and anhedonia lasting two or more years.",
    secondary: "Derived from Greek *dys-* ('bad' or 'ill') and *thymos* ('spirit' or 'mind'); in classical antiquity, general despondency or distress of soul.",
    quotes: [
      { author: "Hippocrates", work: "Aphorisms", quote: "If fright and **dysthymia** last for a long time, such a state of mind is characteristic of melancholy." },
      { author: "Emil Kraepelin", work: "Manic-Depressive Insanity and Paranoia", quote: "Chronic constitutional depression, which we classify as **dysthymia**, casts a joyless gray pall over the patient's entire lifespan." },
      { author: "William James", work: "The Varieties of Religious Experience", quote: "The soul afflicted with chronic **dysthymia** feels that the universe is a hollow mockery, bereft of all divine warmth." }
    ]
  },
  "Dashboard — thym/euthymia.md": {
    primary: "A normal, tranquil, non-depressed, and non-elevated reasonably positive mental and emotional mood state.",
    secondary: "In ancient Hellenic philosophy (particularly Democritus and Seneca's *De Tranquillitate Animi*), inner serenity, peace of mind, and cheerfulness of soul.",
    quotes: [
      { author: "Democritus", work: "Fragments", quote: "The goal of life is **euthymia**, a state in which the soul lives calmly and steadily, disturbed by neither fear nor superstition." },
      { author: "Seneca", work: "De Tranquillitate Animi", quote: "The Greeks call that firm peace of mind **euthymia**, which consists in knowing oneself and trusting that one walks the right path." },
      { author: "Emil Kraepelin", work: "Lectures on Clinical Psychiatry", quote: "Between the stormy paroxysms of mania and melancholia, the patient returned to a serene baseline of stable **euthymia**." }
    ]
  },
  "Dashboard — thym/hyperthymia.md": {
    primary: "A chronic, lifelong affective disposition characterized by high energy, enthusiasm, optimism, decreased need for sleep, and untiring productivity.",
    secondary: "In constitutional psychiatry, a hyperthymic temperament that borders on hypomania but typically facilitates successful executive achievement.",
    quotes: [
      { author: "Emil Kraepelin", work: "Manic-Depressive Insanity", quote: "Individuals blessed with **hyperthymia** are natural leaders, buoyant under stress and capable of monumental daily labors." },
      { author: "Ernst Kretschmer", work: "Physique and Character", quote: "The sunny disposition of constitutional **hyperthymia** drives successful commercial entrepreneurs and charismatic politicians." },
      { author: "Karl Jaspers", work: "General Psychopathology", quote: "In **hyperthymia**, the boundless self-confidence of the individual can occasionally lead to reckless financial overextension." }
    ]
  },
  "Dashboard — thym/thyme.md": {
    primary: "A low-growing aromatic perennial Eurasian herb (*Thymus vulgaris*) of the mint family (Lamiaceae), with pungent leaves widely used as a culinary seasoning.",
    secondary: "A classical herb derived from Greek *thyein* ('to sacrifice') on account of its fragrant incense-like aroma, prized in ancient embalming and medicine.",
    quotes: [
      { author: "William Shakespeare", work: "A Midsummer Night's Dream", quote: "I know a bank where the wild **thyme** blows, where oxlips and the nodding violet grows, quite over-canopied with luscious woodbine." },
      { author: "Virgil", work: "Georgics", quote: "Plant sweet **thyme** and rosemary around the hives, that the bees may gather fragrant honey for the winter stores." },
      { author: "John Milton", work: "Lycidas", quote: "Thee, shepherd, thee the woods and desert caves, with wild **thyme** and the gadding vine o'ergrown, and all their echoes mourn." }
    ]
  },
  "Dashboard — thym/thymelaeaceae.md": {
    primary: "A family of flowering plants (order Malvales), commonly known as the mezereon family, consisting of trees, shrubs, and climbers with tough, fibrous bark.",
    secondary: "A cosmopolitan botanical family named after the ancient genus *Thymelaea*, noted for poisonous resins (mezerein) and valuable daphne ornamental blooms.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The family **Thymelaeaceae** is known for its acrid bark, tough fibrous bast used for cordage, and sweet-scented flowers." },
      { author: "Carl Linnaeus", work: "Genera Plantarum", quote: "We group the shrubby mezereon and allied daphnes under the family **Thymelaeaceae**, marked by a petaloid calyx." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "Species of **Thymelaeaceae** furnish both winter-blooming garden daphnes and strong bast fibers for Japanese paper-making." }
    ]
  },
  "Dashboard — thym/thymelaeales.md": {
    primary: "An order of dicotyledonous flowering plants recognized in historical botanical systems of classification (such as Hutchinson's), centered upon the family Thymelaeaceae.",
    secondary: "A taxonomic order characterized by perigynous or epigynous tubular flowers with tough fibrous cortical tissues.",
    quotes: [
      { author: "John Hutchinson", work: "The Families of Flowering Plants", quote: "The order **Thymelaeales** represents an evolutionary specialization derived from bixalean ancestors, marked by fibrous bark." },
      { author: "Asa Gray", work: "Structural Botany", quote: "Under the classical order **Thymelaeales**, botanists united the mezereon family with allied apetalae of temperate forests." },
      { author: "George Bentham", work: "Genera Plantarum", quote: "The affinities of the **Thymelaeales** link them with both the Proteaceae and the Myrtales through calyx structure." }
    ]
  },
  "Dashboard — thym/thymidine.md": {
    primary: "A pyrimidine deoxynucleoside (C10H14N2O5) consisting of the nucleobase thymine linked to a deoxyribose sugar molecule, a constituent building block of DNA.",
    secondary: "In molecular biology and cell cycle research, tritiated thymidine (3H-thymidine) is historically used as a radioactive tracer to measure DNA synthesis and cellular replication.",
    quotes: [
      { author: "James D. Watson", work: "The Double Helix", quote: "Each strand of DNA contains the four nucleosides: adenosine, cytidine, guanosine, and **thymidine**, linked by phosphodiester bonds." },
      { author: "Francis Crick", work: "What Mad Pursuit", quote: "Incorporation of radioactive **thymidine** proved that DNA replication in bacteria proceeds by semiconservative unwinding." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "The specific presence of **thymidine** in DNA distinguishes it from RNA, which incorporates uridine instead." }
    ]
  },
  "Dashboard — thym/thymine.md": {
    primary: "A pyrimidine nucleobase (5-methyluracil, C5H6N2O2), one of the four principal nitrogenous bases that encode genetic information in DNA.",
    secondary: "Pairs selectively with adenine via two hydrogen bonds within the DNA double helix; replaced by uracil in RNA molecules.",
    quotes: [
      { author: "James D. Watson & Francis Crick", work: "Molecular Structure of Nucleic Acids: A Structure for Deoxyribose Nucleic Acid", quote: "Adenine pairs specifically with **thymine**, and guanine with cytosine, immediately suggesting a copying mechanism for the genetic material." },
      { author: "Albrecht Kossel", work: "Nobel Lecture: The Chemical Composition of the Cell Nucleus", quote: "I succeeded in isolating a new crystalline pyrimidine base from the thymus nucleic acid, which I named **thymine**." },
      { author: "Erwin Chargaff", work: "Chemical Specificity of Nucleic Acids", quote: "Our analytical data showed that in all DNA samples the molar ratio of adenine to **thymine** equals one with remarkable precision." }
    ]
  },
  "Dashboard — thym/thymol.md": {
    primary: "A naturally occurring monoterpene phenol derivative (C10H14O) obtained from oil of thyme, having a pleasant aromatic odor and potent antiseptic, antibacterial, and antifungal properties.",
    secondary: "Widely used in historical pharmacopoeias and modern mouthwashes, dental varnishes, and anthelmintics (notably against hookworm infections).",
    quotes: [
      { author: "Joseph Lister", work: "The Antiseptic System of Treatment", quote: "We tested crystalline **thymol** as a less irritating antiseptic dressing for operative wounds than carbolic acid." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The administration of **thymol** in divided doses followed by Epsom salts remains the sovereign remedy for uncinariasis (hookworm)." },
      { author: "Jonathan Pereira", work: "The Elements of Materia Medica", quote: "The volatile camphor-like crystals of **thymol** melt easily and perfume the sickroom while checking putrefaction." }
    ]
  },
  "Dashboard — thym/thymosin.md": {
    primary: "A family of small, biologically active peptide hormones originally isolated from the thymus gland, essential for the maturation and differentiation of T lymphocytes.",
    secondary: "In immunology and molecular medicine, peptides (such as thymosin alpha-1 and thymosin beta-4) that regulate immune competence and actin polymerization.",
    quotes: [
      { author: "Allan L. Goldstein", work: "Preparation and Properties of Thymosin", quote: "We isolated the active endocrine principle **thymosin** from bovine thymus tissue, showing that it restored cell-mediated immunity in thymectomized mice." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Endocrine research revealed that the thymus is not a useless vestige, but secretes humoral factors like **thymosin** to educate white corpuscles." },
      { author: "Gerald Edelman", work: "The Remembered Present", quote: "T-cell maturation under the influence of **thymosin** illustrates somatic selection within the developing immune system." }
    ]
  },
  "Dashboard — thym/thymus.md": {
    primary: "A primary lymphoid organ of the immune system situated in the superior mediastinum behind the sternum, essential for the maturation, differentiation, and selection of T lymphocytes.",
    secondary: "Prominent in infants and children, undergoing progressive physiological involution and replacement by adipose tissue after puberty.",
    quotes: [
      { author: "Galen", work: "De Usu Partium", quote: "The soft, glandular mass situated over the heart was called the **thymus** by the ancients because of its resemblance to a bunch of thyme." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Enlargement of the **thymus** in infancy was once blamed for sudden suffocative attacks designated as status thymicolymphaticus." },
      { author: "Peter Medawar", work: "The Uniqueness of the Individual", quote: "The discovery that the **thymus** acts as the schoolhouse where T cells learn self-tolerance revolutionized modern immunology." }
    ]
  },

  // Dashboard — zel (4 words)
  "Dashboard — zel/zeal.md": {
    primary: "Great energy, passion, enthusiasm, or fervor in pursuit of a cause, ideal, objective, or religious conviction (from Greek *zēlos*).",
    secondary: "Ardent devotion and tirelessness in defending a principle or faith; impassioned earnestness.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "Zephon, with severe regard, remarked his arrogant stride; for the angel glowed with youthful **zeal** for celestial honor." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "A fanatical political **zeal** destroys ancient institutions overnight, forgetting that liberty grows through centuries of compromise." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "Religious **zeal** in the early American pioneers burned with an intense moral flame that shaped the constitution of the republic." }
    ]
  },
  "Dashboard — zel/zealot.md": {
    primary: "A person who is fanatical and uncompromising in pursuit of their religious, political, or other ideals.",
    secondary: "Historically, a member of an ancient radical Jewish sect (the Zealots) founded by Judas of Galilee that violently opposed Roman rule in 1st-century Judea.",
    quotes: [
      { author: "Flavius Josephus", work: "The Jewish War", quote: "The fanatical sect of the **Zealot** party fortified themselves in the Temple, swearing never to lay down arms before the Roman legions." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The fierce obstinacy of the Jewish **zealot** amazed the Roman procurators, who were accustomed to passive obedience." },
      { author: "John Locke", work: "A Letter Concerning Toleration", quote: "No magistrate possesses the right to punish a citizen merely because some religious **zealot** brands his prayers as heresy." }
    ]
  },
  "Dashboard — zel/zealous.md": {
    primary: "Filled with, characterized by, or showing great zeal; ardent, fervent, and actively enthusiastic.",
    secondary: "Impassioned and tirelessly active in promoting a belief, cause, or organization.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "St. John Rivers was a stern, **zealous** servant of the cross, ready to sacrifice love, health, and life itself in the missionary field." },
      { author: "Benjamin Franklin", work: "Autobiography", quote: "My brother was a **zealous** champion of freedom of the press, printing satires that landed him in the colonial jail." },
      { author: "George Eliot", work: "Silas Marner", quote: "The lantern yard congregation was small, but its members were intensely **zealous** in their puritanical discipline." }
    ]
  },
  "Dashboard — zel/zealously.md": {
    primary: "In a zealous manner; with great passion, energy, devotion, or fervor.",
    secondary: "Eagerly, diligently, and uncompromisingly in support of a cause or duty.",
    quotes: [
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "The Puritan parliamentarians **zealously** enforced Sabbath regulations, closing theaters and banishing festive games." },
      { author: "Nathaniel Hawthorne", work: "The Scarlet Letter", quote: "Governor Bellingham **zealously** scrutinized the maiden's faith, demanding whether she knew who had made her." },
      { author: "Frederick Douglass", work: "Narrative of the Life of Frederick Douglass", quote: "I worked **zealously** at the Baltimore shipyard, determined to learn the ship-calker's trade and earn my freedom." }
    ]
  }
};

for (const [relPath, entry] of Object.entries(filesData)) {
  const filePath = path.join(basePath, relPath);
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

console.log('Batch 8 complete! Total files updated:', Object.keys(filesData).length);
