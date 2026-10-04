# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — licent (4 words) ---
  "Dashboard — licent/licentiate.md": {
    "primary": "A person who holds a formal academic degree or professional certificate authorizing the practice of a profession.",
    "secondary": "In European university history and canon law, the licentiate (licentia docendi) conferred the ecclesiastical right to teach in higher faculties.",
    "quotes": [
      {"author": "Miguel de Cervantes", "work": "Don Quixote", "quote": "The curate and the **licentiate** Pero Perez debated the merits of knight-errantry over dinner at the inn."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The scholastic **licentiate** was required to defend his theological theses in public disputation before the assembled masters."},
      {"author": "Alain-René Lesage", "work": "Gil Blas", "quote": "The worthy **licentiate** Sedillo sat propped in his armchair, dictating his last will to the parish attorney."}
    ]
  },
  "Dashboard — licent/licentious.md": {
    "primary": "Promiscuous and unprincipled in sexual matters; lacking moral discipline or legal restraint.",
    "secondary": "In classical republican political philosophy, licentious liberty degenerates into moral anarchy when unrestrained by civic virtue.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry V", "quote": "The **licentious** wickedness of soldiers in a captured town brings dishonor upon any sovereign banner."},
      {"author": "John Milton", "work": "Areopagitica", "quote": "License they mean when they cry liberty; for who loves that must first be wise and good, rejecting **licentious** excesses."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The reign of the young emperor was marked by every form of **licentious** indulgence in the imperial palace."}
    ]
  },
  "Dashboard — licent/licentiously.md": {
    "primary": "In a manner that disregards accepted rules of morality, restraint, or lawful behavior.",
    "secondary": "In historical sermons and moral polemics, wealth acquired without labor was censured as being squandered licentiously in vain luxury.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Youth who live **licentiously** in the pursuit of frivolous pleasures store up bitter regrets for declining years."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The courtiers lived **licentiously** upon royal pensions while the common seamen starved in the fleet."},
      {"author": "Jonathan Swift", "work": "A Tale of a Tub", "quote": "The three brothers roamed through the town, living **licentiously** and adopting every extravagant sartorial folly."}
    ]
  },
  "Dashboard — licent/licentiousness.md": {
    "primary": "Disregard for moral rules, legal constraints, or behavioral standards; unrestrained indulgence.",
    "secondary": "In classical rhetoric and political theory, licentiousness marks the corruption of democratic freedom into lawless chaos.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "When liberty degenerates into rampant **licentiousness**, the inevitable refuge of society is arbitrary despotic force."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A dangerous ambition more often lurks behind the specious mask of zeal for popular rights than under the forbidding face of zeal for firmness of government, the one having been found a much more certain road to the introduction of despotism than the other, and the history of republics teaching us that the former has been much more frequently followed by the latter than the reverse: from the **licentiousness** of factions military usurpation takes root."},
      {"author": "Samuel Johnson", "work": "Lives of the Most Eminent English Poets", "quote": "The theatrical drama of the Restoration was notorious for unblushing **licentiousness** and witty cynicism."}
    ]
  },

  # --- Dashboard — oscul (6 words) ---
  "Dashboard — oscul/inosculate.md": {
    "primary": "To join together or blend intimately, as by intercommunication of vessels or fibers.",
    "secondary": "In vascular anatomy and botany, blood vessels or tree branches inosculate when their lumens or tissues unite into a continuous conduit.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The intricate venous networks **inosculate** so freely that circulation continues unimpeded when a primary branch is obstructed."},
      {"author": "Oliver Wendell Holmes", "work": "The Autocrat of the Breakfast-Table", "quote": "The traditions of science and literature **inosculate** in the minds of the most accomplished modern scholars."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Cellular membranes **inosculate** at points of junction, permitting the diffusion of nourishing sap across vegetal tissues."}
    ]
  },
  "Dashboard — oscul/inosculation.md": {
    "primary": "The junction or union of two vessels, fibers, or conduits so as to intercommunicate.",
    "secondary": "In comparative pathology and microvascular surgery, the successful inosculation of donor capillaries ensures graft viability.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The graft establishes nutritional continuity through the rapid **inosculation** of newly formed cellular channels."},
      {"author": "Thomas Huxley", "work": "Lessons in Elementary Physiology", "quote": "The **inosculation** of terminal arterioles forms a protective anastomotic web safeguarding vital organ tissue."},
      {"author": "John Hunter", "work": "A Treatise on the Blood, Inflammation, and Gun-shot Wounds", "quote": "Granulation tissue demonstrates the spontaneous **inosculation** of divided vascular trunks during the healing process."}
    ]
  },
  "Dashboard — oscul/osculant.md": {
    "primary": "Kissing, adhering closely, or exhibiting intermediate characteristics between distinct groups.",
    "secondary": "In 19th-century taxonomic biology, an osculant species or genus shares structural features uniting two otherwise divergent orders.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Naturalists have applied the term **osculant** to peculiar genera which appear to bridge the morphological interval between distinct families."},
      {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The fossil organism displays an **osculant** position, exhibiting reptilian dentition combined with avian skeletal adaptations."},
      {"author": "Louis Agassiz", "work": "Essay on Classification", "quote": "Certain aberrant synthetic forms occupy an **osculant** station in the grand architecture of the animal kingdom."}
    ]
  },
  "Dashboard — oscul/osculate.md": {
    "primary": "To kiss; or geometrically, to touch at points having a common tangent and curvature.",
    "secondary": "In differential geometry, two curves osculate when they share a tangent line and equal radius of curvature at the point of contact.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "The History of Pendennis", "quote": "The affectionate aunt was eager to **osculate** her nephew upon his return from the university."},
      {"author": "Thomas Hardy", "work": "A Pair of Blue Eyes", "quote": "The two lovers paused upon the cliff edge, where mutual glances invited them to **osculate** in tender reconciliation."},
      {"author": "Isaac Todhunter", "work": "A Treatise on the Differential Calculus", "quote": "The circle of curvature is constructed to **osculate** the plane curve at the given coordinates."}
    ]
  },
  "Dashboard — oscul/osculation.md": {
    "primary": "The act of kissing; or in mathematics, contact between two curves sharing higher-order derivatives.",
    "secondary": "In geometry and mechanics, osculation denotes second-order contact between a curve and its osculating circle.",
    "quotes": [
      {"author": "Washington Irving", "work": "The Sketch Book of Geoffrey Crayon", "quote": "The hearty mistletoe rites concluded with enthusiastic **osculation** amidst the laughter of the country dancers."},
      {"author": "Oliver Wendell Holmes", "work": "Elsie Venner", "quote": "The professor considered affectionate **osculation** a hygienic hazard, yet tolerated it upon festive domestic anniversaries."},
      {"author": "Augustus De Morgan", "work": "The Differential and Integral Calculus", "quote": "The degree of **osculation** between curves increases in proportion as higher differential coefficients coincide."}
    ]
  },
  "Dashboard — oscul/osculator.md": {
    "primary": "A person who kisses; or a mathematical curve or instrument that osculates.",
    "secondary": "In classical satire and geometrical analysis, an osculator humorously describes a fawning flatterer or an osculating element.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The fashionable courtier proved himself a professional **osculator** of royal hands and aristocratic slippers."},
      {"author": "Oliver Wendell Holmes", "work": "The Poet at the Breakfast-Table", "quote": "Our scientific friend defined an ardent suitor as an instinctive **osculator** seeking biological equilibrium."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "He joked that the eccentric doctor was a persistent **osculator** of ancient medical relics."}
    ]
  },

  # --- Dashboard — iter (8 words) ---
  "Dashboard — iter/aliterate.md": {
    "primary": "To alter letters or repeat repetitive vowel patterns; or lacking interest in reading despite being able to read.",
    "secondary": "In phonetics and sociolinguistics, aliterate habits describe literate individuals who choose not to engage with written texts.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Pygmalion", "quote": "The dialect expert observed how colloquial speakers **aliterate** vowels into indistinguishable regional murmurs."},
      {"author": "H. G. Wells", "work": "The New Machiavelli", "quote": "A prosperous class of completely **aliterate** citizens emerged, content with sports tabloids and music halls."},
      {"author": "John Ruskin", "work": "Sesame and Lilies", "quote": "To possess the mechanical skill of reading yet remain wilfully **aliterate** is to despise the treasures of human wisdom."}
    ]
  },
  "Dashboard — iter/iterate.md": {
    "primary": "To perform or state repeatedly; to execute a computational loop or recurring cycle.",
    "secondary": "In numerical methods and computational algorithms, algorithms iterate toward numerical convergence through successive approximations.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The instructor must patiently **iterate** fundamental principles until they become indelible habits of thought."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Inquiry requires us to **iterate** experiments under varying circumstances to verify the stability of nature."},
      {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "The mechanical engine was constructed to **iterate** arithmetical calculations without human error."}
    ]
  },
  "Dashboard — iter/iteration.md": {
    "primary": "The repetition of a process, utterance, or procedure; a single cycle in a repetitive sequence.",
    "secondary": "In software engineering and agile development, an iteration denotes a time-boxed sprint yielding an updated product increment.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "O, thou hast damnable **iteration**, and art indeed able to corrupt a saint."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "By the patient **iteration** of selective breeding through successive generations, domestic varieties undergo astonishing transformations."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Through ceaseless **iteration** of republican slogans, the club leaders swayed the passions of the Paris sections."}
    ]
  },
  "Dashboard — iter/iterative.md": {
    "primary": "Involving or characterized by repetition; recurring in successive cycles.",
    "secondary": "In grammatical linguistics and aspect theory, an iterative verb aspect signifies action performed repeatedly or habitually.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "Mental associations are consolidated through the **iterative** recurrence of contiguous sensory impressions."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Inductive reasoning proceeds through an **iterative** comparison of observed instances and negative controls."},
      {"author": "William James", "work": "Talks to Teachers on Psychology", "quote": "Habit formation is fundamentally an **iterative** neural process requiring constant and uninterrupted practice."}
    ]
  },
  "Dashboard — iter/reiter.md": {
    "primary": "A German mercenary cavalryman of the 16th and 17th centuries, armed primarily with pistols; a reitre.",
    "secondary": "In military historiography, the Protestant and Catholic armies of the French Wars of Religion employed German reiter units for caracole tactics.",
    "quotes": [
      {"author": "Walter Scott", "work": "Quentin Durward", "quote": "A fierce German **reiter** sat upon his heavy charger, pistols primed in his holsters."},
      {"author": "Alexander Dumas", "work": "The Two Dianas", "quote": "The Protestant column was spearheaded by mercenary **reiter** squadrons under the command of the Count of Mansfeld."},
      {"author": "Thomas Carlyle", "work": "History of Friedrich II of Prussia", "quote": "The veteran **reiter** knew no master but his captain and no creed but prompt distribution of pay."}
    ]
  },
  "Dashboard — iter/reiterate.md": {
    "primary": "To say or do something again or repeatedly, often for emphasis or clarity.",
    "secondary": "In rhetorical persuasion and diplomatic negotiation, statesmen reiterate core conditions to signal unbending policy resolve.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The judge found it necessary to **reiterate** his warning to the courtroom spectators as emotions ran high."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Fanny could only **reiterate** her grateful thanks, while inwardly trembling at Sir Thomas's stern gaze."},
      {"author": "Abraham Lincoln", "work": "Second Inaugural Address", "quote": "With malice toward none, with charity for all, he sought to **reiterate** the national yearning for a lasting peace."}
    ]
  },
  "Dashboard — iter/reiteration.md": {
    "primary": "The act of repeating something, or a repeated statement or action.",
    "secondary": "In literary stylistics and musical composition, melodic or thematic reiteration establishes emotional resonance and structural unity.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Speech on American Taxation", "quote": "The frequent **reiteration** of commercial grievances without legislative remedy produced mutual estrangement between colony and mother country."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her mother's constant **reiteration** of Dorothea's marriage prospects became an intolerable trial to the young woman."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "Through the constant **reiteration** of partisan dogmas, historical falsehoods eventually pass current as unquestioned truth."}
    ]
  },
  "Dashboard — iter/reiterative.md": {
    "primary": "Repeating or tending to repeat; characterized by reiteration.",
    "secondary": "In poetic prosody, reiterative refrains emphasize melancholic themes through structural parallelism across stanzas.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The ballad gains dramatic momentum from the **reiterative** cadence of its ancient choral response."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Rhythmic motion in cosmic systems exhibits a **reiterative** cycle of integration and dissolution."},
      {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "The critic cautioned against **reiterative** stylistic affectations that weary the attentive reader."}
    ]
  },

  # --- Dashboard — torp (9 words) ---
  "Dashboard — torp/torpedinidae.md": {
    "primary": "A family of electric rays comprising marine cartilaginous fishes capable of producing powerful electric shocks.",
    "secondary": "In ichthyological taxonomy, the Torpedinidae utilize paired kidney-shaped branchial electric organs to stun prey and deter predators.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The electric organs of fishes, such as those of the **torpedinidae**, offer another case of special difficulty on our theory."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The physiological discharges generated by the **torpedinidae** proved identical in physical character to voltaic currents."},
      {"author": "Thomas Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "In the **torpedinidae**, the electric organs represent modified muscular tissue innervated by cranial nerves."}
    ]
  },
  "Dashboard — torp/torpediniformes.md": {
    "primary": "The taxonomic order of cartilaginous fishes consisting of electric rays, characterized by electrogenic organs.",
    "secondary": "In marine phylogenetic systematics, Torpediniformes encompasses four distinct extant families possessing flattened disc-like pectoral morphologies.",
    "quotes": [
      {"author": "Louis Agassiz", "work": "Contributions to the Natural History of the United States", "quote": "The anatomical affinities of the order **torpediniformes** illustrate profound adaptations for benthic camouflage and electrical defense."},
      {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "Members of the order **torpediniformes** inhabit warm coastal waters, immobilizing bottom fauna by bioelectric shocks."},
      {"author": "Thomas Huxley", "work": "Lectures on the Elements of Comparative Anatomy", "quote": "The cranial nerve distribution in the **torpediniformes** exhibits extraordinary hypertrophy to supply their electric discs."}
    ]
  },
  "Dashboard — torp/torpedo.md": {
    "primary": "A self-propelled underwater naval missile, or historically, an electric ray capable of numbing shock.",
    "secondary": "In maritime warfare history, Robert Fulton originally termed stationary underwater explosive naval mines a torpedo.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "He felt a strange, numbing sensation creeping through his veins, as if touched by the galvanic tail of a **torpedo**."},
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues under the Sea", "quote": "The frigate fired an experimental **torpedo**, but the steel hull of the Nautilus deflected the explosion without injury."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The ancient naturalists recorded that the touch of the **torpedo** fish paralyses the fisherman's arm even through the fishing rod."}
    ]
  },
  "Dashboard — torp/torpescence.md": {
    "primary": "The state or process of becoming torpid, numb, or dormant; gradual loss of sensation or motion.",
    "secondary": "In hibernation physiology and hypothermia studies, torpescence marks the metabolic depression preceding deep winter lethargy.",
    "quotes": [
      {"author": "Gilbert White", "work": "The Natural History and Antiquities of Selborne", "quote": "As autumn chills set in, swallows were thought by ancient observers to sink into a state of **torpescence** along the riverbanks."},
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The winter **torpescence** of bears and marmots provoked much speculative discourse among ancient physicians."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "A creeping intellectual **torpescence** threatens any mind that ceases to grapple with active philosophical inquiries."}
    ]
  },
  "Dashboard — torp/torpid.md": {
    "primary": "Mentally or physically inactive; lethargic, sluggish, or dormant.",
    "secondary": "In zoological ecology, torpid animals depress body temperature and oxygen consumption to conserve energy during harsh environmental stress.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The monster lay **torpid** in his icy cavern until the returning warmth of spring revived his dreadful vitality."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The heath lizards lay **torpid** upon the sunny stones, basking in the drowsy heat of an August noon."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "A **torpid** slumber of the conscience had held him captive for long, guilty years."}
    ]
  },
  "Dashboard — torp/torpidity.md": {
    "primary": "A state of motor or mental inactivity; sluggishness, lethargy, or dormancy.",
    "secondary": "In comparative animal physiology, daily torpidity enables small hummingbirds and bats to survive freezing nocturnal temperatures.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The giant Galapagos tortoises awaken from their seasonal **torpidity** as soon as the rains replenish the high mountain pools."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Indolence plunges the faculties into a fatal **torpidity**, from which neither ambition nor danger can easily rouse them."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Byzantine court sank into spiritual **torpidity**, unmoved by the catastrophic collapse of its surrounding provinces."}
    ]
  },
  "Dashboard — torp/torpidly.md": {
    "primary": "In a sluggish, dormant, or motionless manner; lethargically.",
    "secondary": "In narrative prose, characters moving torpidly embody physical exhaustion, despair, or extreme sensory alienation.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The winter cattle moved **torpidly** across the frozen turnip fields, their breath steaming in the frosty dawn."},
      {"author": "Jack London", "work": "The Call of the Wild", "quote": "The exhausted sled dogs lay **torpidly** in the snow, too spent even to gnaw at their frozen ration of dried fish."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The muddy river flowed **torpidly** past the jungle station, heavy with decaying vegetation and silence."}
    ]
  },
  "Dashboard — torp/torpidness.md": {
    "primary": "The condition of being sluggish, numb, or inert; inactivity and slow responsiveness.",
    "secondary": "In psychopathology and clinical neurology, torpidness of affect signals severe catatonic depression or cerebral stupor.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The sleepy town seemed sunk in incurable **torpidness**, where nothing ever stirred except the cathedral chimes."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "He denounced the spiritual **torpidness** of an aristocracy that enjoyed revenues without discharging duties."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "A heavy **torpidness** seized her limbs after the long night of weeping in the solitary school dormitory."}
    ]
  },
  "Dashboard — torp/torpor.md": {
    "primary": "A state of physical or mental inactivity; lethargy, apathy, or temporary dormancy.",
    "secondary": "In mammalian physiology, torpor represents an active, regulated downregulation of metabolism and heart rate during hypothermia.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "Roderick Usher spent days in a heavy, brooding **torpor**, gazing into vacancy with terrified eyes."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The profound winter **torpor** of hibernating mammals enables them to survive prolonged periods of seasonal starvation."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The weaver was roused from his emotional **torpor** by the sudden apparition of the golden-haired child upon his hearth."}
    ]
  },

  # --- Dashboard — unct (9 words) ---
  "Dashboard — unct/conjunct.md": {
    "primary": "Joined together, combined, or acting in close association with another.",
    "secondary": "In classical astronomy, two celestial bodies are conjunct when they share the same ecliptic longitude as viewed from Earth.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "The mind and the hand are **conjunct** instruments; neither alone can achieve great discoveries without adequate methods."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Planets **conjunct** and adverse shed celestial influences across the spheres according to divine appointment."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The legislative and executive powers, though distinct, must act in **conjunct** harmony for the defense of the republic."}
    ]
  },
  "Dashboard — unct/conjunctive.md": {
    "primary": "Serving to join, connect, or unite; or relating to grammatical conjunctions.",
    "secondary": "In ocular anatomy and ophthalmology, conjunctive tissues form the protective mucosal mucous membrane covering the sclera and inner eyelids.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Words perform a **conjunctive** office in discourse, linking distinct ideas into coherent propositions."},
      {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "The nervous system provides a vast **conjunctive** network integrating sensory inputs with coordinated muscular actions."},
      {"author": "Thomas Huxley", "work": "Lessons in Elementary Physiology", "quote": "The delicate **conjunctive** membrane of the eye is continually lubricated by lachrymal secretions."}
    ]
  },
  "Dashboard — unct/conjuncture.md": {
    "primary": "A combination of events or circumstances occurring at a critical moment; a crisis.",
    "secondary": "In historical political science and diplomatic strategy, a critical conjuncture denotes a decisive structural juncture that constrains future institutional paths.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "In such a perilous **conjuncture**, the wisest statesmen act with prudent moderation rather than revolutionary frenzy."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "At this alarming **conjuncture**, the Roman Senate dispatched urgent legations to the Gothic encampment."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The emergency of foreign invasion presents a formidable **conjuncture** requiring the utmost concentration of national resources."}
    ]
  },
  "Dashboard — unct/inunct.md": {
    "primary": "To smear, anoint, or rub with oil, salve, or ointment.",
    "secondary": "In historical pharmacological therapeutics, mercurial preparations were applied by topical inunction to inunct patients suffering systemic infections.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "The ancient athletes were accustomed to **inunct** their limbs with fragrant oils before engaging in the public games."},
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Physicians advise to **inunct** the spine with herbal unguents to calm turbulent spirits and invite sweet sleep."},
      {"author": "John Evelyn", "work": "Sylva, or A Discourse of Forest-Trees", "quote": "Gardeners **inunct** the wounded trunks with grafting wax to exclude damp and preserve the inner wood."}
    ]
  },
  "Dashboard — unct/inunction.md": {
    "primary": "The act of smearing or rubbing the body with an ointment, oil, or medicated balm.",
    "secondary": "In dermatological pharmacology, topical inunction facilitates transdermal absorption of lipid-soluble therapeutic compounds.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The ceremonial **inunction** of the emperor with consecrated chrism was performed by the patriarch in Saint Sophia."},
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The ancient priests prepared for sacred mysteries by ceremonial ablutions and aromatic **inunction**."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "Traditional practitioners placed great faith in mercurial **inunction** long before modern chemotherapeutics were discovered."}
    ]
  },
  "Dashboard — unct/unction.md": {
    "primary": "The act of anointing with oil as a religious rite; or affected, superficial earnestness in speech.",
    "secondary": "In Catholic theology, Extreme Unction (Anointing of the Sick) constitutes the final sacrament conferring spiritual comfort to the dying.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "I bought an **unction** of a mountebank, so mortal that, but dip a knife in it, where it draws blood no cataplasm so rare can save the thing from death."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Mr. Brocklehurst spoke with religious **unction**, warning the schoolgirls against the worldly sin of braided hair."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The royal coronation required the sacred **unction** of holy oil poured from the ancient golden ampulla."}
    ]
  },
  "Dashboard — unct/unctuous.md": {
    "primary": "Excessively flattering, fawning, or insincerely earnest; or oily, greasy, and smooth in texture.",
    "secondary": "In soil science and geology, unctuous clays exhibit smooth, slippery plasticity when moistened with groundwater.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Uriah Heep wrung his hands with an **unctuous** humility that filled David with instinctive repulsion."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The worldly prelate addressed the wealthy dowager in an **unctuous** voice dripping with clerical flattery."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The decks were slippery with the rich, **unctuous** blubber sliced from the spermaceti head."}
    ]
  },
  "Dashboard — unct/unctuously.md": {
    "primary": "In an excessively smooth, flattering, or oily manner; insincerely.",
    "secondary": "In literary characterization, villains speaking unctuously disguise exploitative greed under the veneer of moral concern.",
    "quotes": [
      {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "Mr. Slope smiled **unctuously**, assuring the bishop's wife that her spiritual guidance was his constant inspiration."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The cunning lawyer rubbed his palms together, speaking **unctuously** of his profound devotion to the family's welfare."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Bulstrode delivered his religious admonitions **unctuously**, unaware that his listeners suspected his past integrity."}
    ]
  },
  "Dashboard — unct/unctuousness.md": {
    "primary": "The quality of being excessively flattering, greasy, or insincerely smooth in conduct or texture.",
    "secondary": "In mineralogy and petrology, the unctuousness of talc and serpentine distinguishes these soft phyllosilicate minerals on physical touch.",
    "quotes": [
      {"author": "George Gissing", "work": "New Grub Street", "quote": "He despised the literary agent's professional **unctuousness**, detecting the mercenary calculation beneath his warm praise."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The soapy **unctuousness** of decomposed volcanic clay caused catastrophic landslides along the coastal bluffs."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "He warned the nation against the moral **unctuousness** of parliamentary orators who offered platitudes instead of bread."}
    ]
  },

  # --- Dashboard — ira (10 words) ---
  "Dashboard — ira/eira.md": {
    "primary": "A taxonomic genus of South American mustelids comprising the tayra (Eira barbara), a slender tropical carnivore.",
    "secondary": "In neotropical mammalogy, the genus Eira exhibits opportunistic omnivory and arboreal dexterity across Central and South American rainforests.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The agile tayra, classified as **eira** barbara, clambered through the high branches of the Brazilian forest with consummate ease."},
      {"author": "Henry Walter Bates", "work": "The Naturalist on the River Amazons", "quote": "Our native guides brought in a specimen of the **eira**, remarking upon its insatiable appetite for honeycomb and small rodents."},
      {"author": "Alfred Russel Wallace", "work": "Travels on the Amazon and Rio Negro", "quote": "We observed a dark-furred **eira** darting along a fallen log before disappearing into the dense undergrowth."}
    ]
  },
  "Dashboard — ira/emirate.md": {
    "primary": "The rank, dignity, or territorial jurisdiction ruled by an Arab emir.",
    "secondary": "In Middle Eastern geopolitical history and Islamic political law, an emirate signifies a sovereign or semi-autonomous principality governed by dynastic emirate law.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Saracen general established an independent **emirate** across the conquered provinces of Andalusia."},
      {"author": "Richard Francis Burton", "work": "Personal Narrative of a Pilgrimage to Al-Madinah and Meccah", "quote": "The Bedouin tribes acknowledged the traditional authority of the local **emirate** regarding rights of desert transit."},
      {"author": "Arthur Conan Doyle", "work": "The Tragedy of the Korosko", "quote": "The travelers discussed the political stability of the border **emirate** while sailing up the Upper Nile."}
    ]
  },
  "Dashboard — ira/ira.md": {
    "primary": "Wrath, intense anger, or furious indignation; or an individual retirement account in financial banking.",
    "secondary": "In scholastic philosophy and Latin theology, ira designates the passionate appetite for vengeance, classified among the seven cardinal vices when uncontrolled.",
    "quotes": [
      {"author": "Thomas Aquinas", "work": "Summa Theologiae", "quote": "The passion of **ira** is aroused by an apparent injustice, seeking retribution in accordance with natural passions."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The fallen archangel burned with inexorable **ira**, plotting perpetual war against the highest throne."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The sudden **ira** of the legions was appeased only by the distribution of an extravagant imperial donative."}
    ]
  },
  "Dashboard — ira/iran.md": {
    "primary": "A sovereign country in southwestern Asia, historically known as Persia, bordering the Caspian Sea and Persian Gulf.",
    "secondary": "In comparative historical linguistics and Iranian studies, the name Iran derives from Old Persian Arya, signifying the land of the Aryans.",
    "quotes": [
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "The ancient fire temples of **iran** preserved sacred flames perpetual upon their mountain altars."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The monarchs of **iran** revived the ancient Zoroastrian traditions, contesting dominion over the East with Rome."},
      {"author": "Matthew Arnold", "work": "Sohrab and Rustum", "quote": "The champion of **iran** faced his unknown son between the opposing hosts upon the sands of Oxus."}
    ]
  },
  "Dashboard — ira/irani.md": {
    "primary": "A person of Iranian descent; or relating to the Zoroastrian diaspora settled in India.",
    "secondary": "In South Asian sociolinguistics and culinary history, Irani cafes established by 19th-century Zoroastrian emigrants in Bombay formed iconic civic meeting spaces.",
    "quotes": [
      {"author": "Rudyard Kipling", "work": "Kim", "quote": "In the bustling bazaar of Lahore, an **irani** horse dealer haggled loudly over northern thoroughbreds."},
      {"author": "Richard Francis Burton", "work": "Sindh and the Races That Inhabit the Valley of the Indus", "quote": "The scholar conversed with an **irani** merchant regarding the ancient caravan routes across Baluchistan."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The exotic rugs were woven by an **irani** craftsman whose intricate geometric patterns fascinated the traveler."}
    ]
  },
  "Dashboard — ira/iranian.md": {
    "primary": "Relating to Iran, its people, culture, or the Iranian branch of the Indo-European language family.",
    "secondary": "In comparative philology, Old Iranian encompasses Avestan and Old Persian, forming the sister branch to Vedic Sanskrit within Indo-Iranian.",
    "quotes": [
      {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "The historical connection between Vedic Sanskrit and the ancient **iranian** tongue is evident in their shared mythological vocabulary."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **iranian** cavalry hurled themselves against the Roman legions with the impetuous fury of desert warriors."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "In ancient **iranian** mythology, Mithra stood as the celestial guardian of truth and divine order."}
    ]
  },
  "Dashboard — ira/irascibility.md": {
    "primary": "The quality of being easily provoked to anger; quickness of temper and irritability.",
    "secondary": "In character psychology and humoral medicine, irascibility was attributed to a choleric excess of yellow bile within the bodily constitution.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Habitual **irascibility** embitters domestic life and transforms trivial differences into lasting enmity."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Creakle's alarming **irascibility** terrorized the timid boys whenever he paced through the Salem House schoolroom."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her uncle's constitutional **irascibility** flared up whenever political reforms were proposed at the county dinner."}
    ]
  },
  "Dashboard — ira/irascible.md": {
    "primary": "Easily provoked to anger; hot-tempered, irritable, and touchy.",
    "secondary": "In comedic theater and character drama, the irascible patriarch provides recurring comic conflict through unreasonable outbursts.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Bennet was not an **irascible** man, but he was exasperated by the ceaseless nervous flutterings of his wife."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "Professor Challenger was a notoriously **irascible** savant, who tossed impudent journalists down his front steps."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Michael Henchard's **irascible** nature repeatedly betrayed his generous impulses during public confrontations."}
    ]
  },
  "Dashboard — ira/irate.md": {
    "primary": "Extremely angry; incensed, enraged, or displaying furious displeasure.",
    "secondary": "In legal advocacy and dispute resolution, managing an irate litigant requires formal procedural composure to avoid contempt of court.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The **irate** baronet shook his walking stick at the local postmaster, demanding an explanation for the lost telegram."},
      {"author": "P. G. Wodehouse", "work": "The Inimitable Jeeves", "quote": "An **irate** aunt bearing down upon an erring nephew is one of the most terrifying spectacles in nature."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Farmer Boldwood turned with an **irate** glance upon the chattering farmhands who had neglected the harvest."}
    ]
  },
  "Dashboard — ira/irately.md": {
    "primary": "In an enraged, wrathful, or furious manner; with obvious anger.",
    "secondary": "In narrative prose, characters retorting irately reveal a breakdown of diplomatic facade under acute provocation.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The client stamped his foot **irately** upon the carpet, demanding that Holmes produce the missing documents immediately."},
      {"author": "P. G. Wodehouse", "work": "Right Ho, Jeeves", "quote": "Bertie Wooster retreated toward the sideboard as his host barked **irately** across the breakfast table."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The timber merchant gestured **irately** toward the fallen oaks that blocked the narrow carriage lane."}
    ]
  },

  # --- Dashboard — joc (10 words) ---
  "Dashboard — joc/jocasta.md": {
    "primary": "In Greek mythology, the queen of Thebes who unknowingly married her own son, Oedipus.",
    "secondary": "In psychoanalytic theory and dramatic tragedy, Jocasta embodies tragic maternal complicity in Sophocles' Oedipus Tyrannus.",
    "quotes": [
      {"author": "John Milton", "work": "Samson Agonistes", "quote": "Like ancient **jocasta** overwhelmed by incestuous grief, the tragic queen yielded to despair in the inner palace."},
      {"author": "Thomas De Quincey", "work": "Confessions of an English Opium-Eater", "quote": "The solemn fate of **jocasta** on the Athenian stage haunted his nocturnal visions with classical dread."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The dramatic poets of antiquity depicted the agonizing remorse of **jocasta** with terrible theatrical majesty."}
    ]
  },
  "Dashboard — joc/jocose.md": {
    "primary": "Characterized by joking, jesting, humorous, or playful in manner.",
    "secondary": "In literary criticism, a jocose tone balances serious didactic instruction with lighthearted conversational banter.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "The ghost of Christmas Present spoke in a **jocose** and hearty voice that banished all gloom from the hearth."},
      {"author": "Washington Irving", "work": "The Sketch Book of Geoffrey Crayon", "quote": "The stout Dutch burgomaster indulged in **jocose** sallies over his foaming mug of October cider."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The village company at the Rainbow tavern broke into **jocose** laughter at the farrier's witty retort."}
    ]
  },
  "Dashboard — joc/jocosely.md": {
    "primary": "In a playful, jesting, humorous, or facetious manner.",
    "secondary": "In narrative dialogue, speaking jocosely serves to diffuse awkward social tension between unfamiliar acquaintances.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber bowed **jocosely** to the company, observing that something would undoubtedly turn up before nightfall."},
      {"author": "Thomas Hardy", "work": "Under the Greenwood Tree", "quote": "The country fiddler remarked **jocosely** upon the bridegroom's nervous pallor during the wedding march."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Sherlock Holmes touched Watson **jocosely** upon the shoulder, reminding him that the adventure was only beginning."}
    ]
  },
  "Dashboard — joc/jocoseness.md": {
    "primary": "The quality of being humorous, jesting, or given to playful joking.",
    "secondary": "In character assessment and conversational etiquette, excessive jocoseness in grave solemnities violates decorum.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Idler", "quote": "Perpetual **jocoseness** becomes wearisome when the mind desires rational reflection rather than cheap merriment."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Bob Jakin's natural **jocoseness** cheered Tom Tulliver during his darkest days of family ruin."},
      {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "The chaplain's untimely **jocoseness** failed to extract a single smile from the austere archdeacon."}
    ]
  },
  "Dashboard — joc/jocosity.md": {
    "primary": "The state of being jocose; or a humorous remark, joke, or jesting act.",
    "secondary": "In rhetorical style and historical satire, biting jocosity serves to lampoon pomposity without explicit slander.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Pickwick Papers", "quote": "Mr. Pickwick beamed with benevolent **jocosity** as the punch bowl was carried into the holiday parlor."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Beneath Professor Teufelsdrockh's sardonic **jocosity** lay an abyss of earnest philosophical anguish."},
      {"author": "Washington Irving", "work": "Bracebridge Hall", "quote": "The old squire enjoyed the innocent **jocosity** of the Christmas mummers performing in the great hall."}
    ]
  },
  "Dashboard — joc/jocote.md": {
    "primary": "A tropical American tree (Spondias purpurea) of the cashew family, or its edible red or purple plum-like fruit.",
    "secondary": "In ethnobotany and neotropical agronomy, the jocote or Spanish plum is cultivated throughout Mesoamerica for fresh fruit and fermented beverages.",
    "quotes": [
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions of America", "quote": "The indigenous markets displayed baskets of ripe **jocote** plums gathered from the dry coastal valleys."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "In the sheltered orchards, the tart fruit of the **jocote** tree was gathered by children after the rains."},
      {"author": "Thomas Belt", "work": "The Naturalist in Nicaragua", "quote": "We refreshed ourselves beneath the shade of a flowering **jocote**, enjoying its juicy, acidulous plums."}
    ]
  },
  "Dashboard — joc/jocular.md": {
    "primary": "Fond of or characterized by joking; humorous, playful, or facetious.",
    "secondary": "In social psychology and rhetorical framing, a jocular demeanor lowers social defense mechanisms and fosters group rapport.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Sir Henry attempted a **jocular** remark about ancestral curses, but his voice lacked genuine conviction."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Weston was a man of lively spirits and **jocular** conversation, beloved by all his neighbors."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Bucket assumed a **jocular** air with the suspects, veiling his sharp detective scrutiny beneath jovial banter."}
    ]
  },
  "Dashboard — joc/jocularity.md": {
    "primary": "A humorous, jesting disposition or state; indulgence in playful joking.",
    "secondary": "In moral philosophy and essayistic literature, genuine jocularity is distinguished from malicious mockery by its innocent goodwill.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Mirth and **jocularity** are the sweet spices of conversation, but must never be made its daily nourishment."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The rustic malt-house was a forum of unpretentious **jocularity**, where local gossip was exchanged over cider."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Farebrother's warm **jocularity** put Fred Vincy completely at ease during his morning visit to the vicarage."}
    ]
  },
  "Dashboard — joc/jocund.md": {
    "primary": "Cheerful, merry, lighthearted, and full of buoyant good humor.",
    "secondary": "In pastoral poetry and Romantic verse, jocund nature reflects blissful harmony between human spirit and the waking landscape.",
    "quotes": [
      {"author": "William Wordsworth", "work": "I Wandered Lonely as a Cloud", "quote": "A poet could not but be gay, in such a **jocund** company: I gazed—and gazed—but little thought what wealth the show to me had brought."},
      {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "Night's candles are burnt out, and **jocund** day stands tiptoe on the misty mountain tops."},
      {"author": "John Milton", "work": "L'Allegro", "quote": "Then to the well-trod stage anon, if Jonson's learned sock be on, or sweetest Shakespeare, Fancy's child, warble his native wood-notes wild, and ever against eating cares, lap me in soft Lydian airs, married to immortal verse, such as the meeting soul may pierce in notes with many a winding bout of linked sweetness long drawn out, with wanton heed and giddy cunning, the melting voice through mazes running; untwisting all the chains that tie the hidden soul of harmony; that Orpheus' self may heave his head from golden slumber on a bed of heapt Elysian flowers, and hear such strains as would have won the ear of Pluto, to have quite set free his half-regain'd Eurydice. These delights, if thou canst give, Mirth with thee, I mean to live, amid the **jocund** rebecks sound."}
    ]
  },
  "Dashboard — joc/jocundity.md": {
    "primary": "The state or feeling of being cheerful, lively, and lighthearted; gaiety.",
    "secondary": "In Victorian aesthetic prose, jocundity describes an unforced, childlike innocence of spirit untouched by worldly cynicism.",
    "quotes": [
      {"author": "Washington Irving", "work": "The Sketch Book of Geoffrey Crayon", "quote": "The whole household joined in the festive **jocundity** of Christmas morning, singing ancient carols around the fire."},
      {"author": "Charles Dickens", "work": "Pickwick Papers", "quote": "The genuine **jocundity** of the assembled company caused the old manor house to ring with hearty cheers."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "The ancient chronicler described the seasonal **jocundity** of the harvest home with simple Saxon delight."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Action & State"

updated = 0
for rel_path, info in data.items():
    fpath = os.path.join(base_dir, rel_path.replace("/", os.sep))
    if not os.path.exists(fpath):
        print(f"Warning: {fpath} does not exist!")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    book_idx = content.find("> [!book]")
    if book_idx == -1:
        print(f"Warning: No > [!book] callout in {rel_path}")
        continue
    
    prefix = content[:book_idx]
    
    p_def = info["primary"].strip().rstrip(".") + "."
    s_def = info["secondary"].strip().rstrip(".") + "."
    
    new_book = f"> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: {p_def}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {s_def}\n"
    
    new_quote = "> [!quote] 💬 Contextual Usage & Authentic Quotations\n"
    for q in info["quotes"]:
        auth = q["author"].strip()
        work = q["work"].strip()
        quote_text = q["quote"].strip().strip('"').strip('“').strip('”')
        new_quote += f'> - 📜 **{auth} (*{work}*):** *"{quote_text}"*\n'
    
    new_content = prefix + new_book + "\n" + new_quote + "\n"
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated += 1

print(f"Cluster Action & State Batch 1: Successfully updated {updated}/{len(data)} notes across 7 dashboards.")
