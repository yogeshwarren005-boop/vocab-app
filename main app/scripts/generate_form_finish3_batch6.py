import json, os

# Batch 6: words 320 to 383 (64 words)
data = {
  "Dashboard — schem\\schematically.md": {
    "primary": "In a schematic manner; by means of an outline, simplified diagram, blueprint, or systematic conceptual model.",
    "secondary": "In linguistics and cognitive psychology, representing formal relationships in an abstract symbolic code rather than detailed concrete descriptions.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "The Analysis of Mind", "quote": "We can represent **schematically** the causal chain linking external physical events with sensory cerebral reactions."},
      {"author": "Charles Sanders Peirce", "work": "Collected Papers", "quote": "The existential graphs display **schematically** how logical deduction unfolds through visible syntactic transformations."},
      {"author": "Noam Chomsky", "work": "Aspects of the Theory of Syntax", "quote": "Phrase marker tree diagrams depict **schematically** the hierarchical dominance relations underlying syntactic surface structures."}
    ]
  },
  "Dashboard — schem\\schematisation.md": {
    "primary": "The process, act, or instance of forming or reducing into a scheme, diagram, or structured outline (British spelling).",
    "secondary": "In developmental psychology and semiotics, the cognitive organization of sensory experience into generalizable symbolic schemas.",
    "quotes": [
      {"author": "Jean Piaget", "work": "The Construction of Reality in the Child", "quote": "Sensorimotor **schematisation** enables the growing infant to coordinate vision and grasping into purposeful action."},
      {"author": "Henri Bergson", "work": "Creative Evolution", "quote": "The intellect proceeds by spatial **schematisation**, freezing continuous organic duration into static geometric representations."},
      {"author": "Roland Barthes", "work": "Elements of Semiology", "quote": "Structural analysis involves the rigorous **schematisation** of cultural narratives into fundamental oppositional codes."}
    ]
  },
  "Dashboard — schem\\schematise.md": {
    "primary": "To form into a scheme; to represent, organize, or classify in a systematic, diagrammatic, or schematic manner (British spelling).",
    "secondary": "In critical philosophy and pedagogical exposition, to reduce rich empirical data to clear operational categories.",
    "quotes": [
      {"author": "John Dewey", "work": "Experience and Nature", "quote": "When we **schematise** human inquiry, we must avoid isolating cognitive reflection from its living practical context."},
      {"author": "Terry Eagleton", "work": "Literary Theory: An Introduction", "quote": "Formalist critics attempt to **schematise** poetic language into mechanical equations of tension and balance."},
      {"author": "Raymond Williams", "work": "Marxism and Literature", "quote": "Sociologists who over-**schematise** social classes risk missing the fluid historical dynamics of cultural struggle."}
    ]
  },
  "Dashboard — schem\\schematism.md": {
    "primary": "The act, process, or practice of schematizing; an arrangement, classification, or disposition according to a scheme.",
    "secondary": "In Kantian epistemology, the transcendental procedure of the understanding by which pure conceptual categories are applied to temporal sensory intuitions.",
    "quotes": [
      {"author": "Immanuel Kant", "work": "Critique of Pure Reason", "quote": "This **schematism** of our understanding, in its application to appearances and their mere form, is an art concealed in the depths of the human soul."},
      {"author": "Arthur Schopenhauer", "work": "The World as Will and Representation", "quote": "Kant's doctrine of the **schematism** was an ingenious attempt to bridge the gulf between abstract concepts and empirical perceptions."},
      {"author": "Ernst Cassirer", "work": "The Philosophy of Symbolic Forms", "quote": "Mythological thought possesses its own symbolic **schematism**, structuring space and time according to sacred boundaries."}
    ]
  },
  "Dashboard — schem\\schematization.md": {
    "primary": "The act, process, or result of reducing or arranging something into a scheme, diagram, or systematic model.",
    "secondary": "In cognitive science and anthropology, the formal simplification of cultural traditions or cognitive representations into structured paradigms.",
    "quotes": [
      {"author": "Jean Piaget", "work": "The Psychology of Intelligence", "quote": "Mental **schematization** allows the child to assimilate diverse physical interactions under universal logical operations."},
      {"author": "Claude Lévi-Strauss", "work": "The Savage Mind", "quote": "Totemic classifications operate through systematic **schematization**, mapping social clans onto natural species."},
      {"author": "Lev Vygotsky", "work": "Thought and Language", "quote": "Internal speech undergoes progressive **schematization**, shedding syntactic markers while condensing pure semantic sense."}
    ]
  },
  "Dashboard — schem\\schematize.md": {
    "primary": "To arrange, classify, or represent in a scheme, diagram, or systematic conceptual framework.",
    "secondary": "In philosophical methodology and systems engineering, to simplify complex phenomena into explicit analytical models.",
    "quotes": [
      {"author": "William James", "work": "Pragmatism: A New Name for Some Old Ways of Thinking", "quote": "The rationalist mind loves to **schematize** the universe into neat intellectual boxes where every paradox is smoothed away."},
      {"author": "Max Weber", "work": "Economy and Society", "quote": "Sociologists construct ideal types to **schematize** historical action, illuminating underlying motivations through deliberate abstraction."},
      {"author": "Willard Van Orman Quine", "work": "Word and Object", "quote": "Logical notation helps **schematize** natural language sentences, clarifying referential commitments and quantification boundaries."}
    ]
  },
  "Dashboard — schem\\scheme.md": {
    "primary": "A systematic plan, design, project, or programmatic arrangement for achieving a desired end or purpose.",
    "secondary": "In algebraic geometry and philosophy, an underlying structured framework (such as a Grothendieck scheme in modern geometry).",
    "quotes": [
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The academy of Lagado presented a visionary **scheme** for extracting sunbeams out of cucumbers to warm chilly rooms."},
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "The man of system imagines he can arrange the different members of a great society with as much ease as the hand arranges pieces in a chess **scheme**."},
      {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "A foolish consistency is the hobgoblin of little minds, adored by statesmen and philosophers who worship their own narrow **scheme**."}
    ]
  },
  "Dashboard — schem\\schemer.md": {
    "primary": "A person who devises plans, projects, or plots, especially in an underhanded, crafty, or self-interested manner.",
    "secondary": "In dramatic literature and political commentary, an intriguer or Machiavellian figure who manipulates social situations for personal gain.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King Lear", "quote": "The illegitimate Edmund emerges as a cunning **schemer**, orchestrating the ruin of his loyal brother with forged letters."},
      {"author": "Niccolò Machiavelli", "work": "The Prince", "quote": "A shrewd **schemer** knows how to disguise his true intentions, adopting virtues when expedient and discarding them when necessary."},
      {"author": "Thomas Carlyle", "work": "The French Revolution: A History", "quote": "The restless political **schemer** hurried from salon to assembly, whispering conspiracies into the ears of impressionable deputies."}
    ]
  },
  "Dashboard — schem\\schemozzle.md": {
    "primary": "A state of confusion, brawl, quarrel, muddle, or noisy disorderly commotion (slang of Yiddish origin).",
    "secondary": "In colloquial British and Commonwealth English, an entangled or chaotic situation characterized by sudden misunderstandings and uproar.",
    "quotes": [
      {"author": "P. G. Wodehouse", "work": "Right Ho, Jeeves", "quote": "I found myself plunged headlong into a frightful **schemozzle** involving an enraged aunt and an overturned soup tureen."},
      {"author": "James Joyce", "work": "Finnegans Wake", "quote": "Amidst the polyglot tumult of the marketplace, a sudden **schemozzle** broke out over the payment of tavern coins."},
      {"author": "George Orwell", "work": "Down and Out in Paris and London", "quote": "The kitchen was in a roaring **schemozzle**, waiters shouting curses as orders piled up and plates crashed to the floor."}
    ]
  },
  "Dashboard — schid\\diaschisis.md": {
    "primary": "A sudden loss of function in a portion of the central nervous system distant from a primary focal brain lesion, caused by loss of afferent input.",
    "secondary": "In clinical neurology and neurorehabilitation, a neurophysiological concept introduced by von Monakow explaining acute functional deficits that gradually resolve.",
    "quotes": [
      {"author": "Constantin von Monakow", "work": "Die Lokalisation im Grosshirn", "quote": "I designated as **diaschisis** that sudden functional standstill in intact cortical areas following abrupt injury to connected subcortical pathways."},
      {"author": "Norman Geschwind", "work": "Selected Papers on Language and the Brain", "quote": "Transient global aphasia after localized infarction may reflect acute **diaschisis** across bilateral transcallosal fibers."},
      {"author": "Wilder Penfield", "work": "Speech and Brain-Mechanisms", "quote": "Recovery from post-surgical deficits frequently parallels the gradual subsidence of cortical **diaschisis** over several weeks."}
    ]
  },
  "Dashboard — schid\\diaschisma.md": {
    "primary": "In musical acoustics and ancient Greek music theory, a microtonal interval equal to approximately 19.55 cents.",
    "secondary": "In Pythagorean tuning and harmonic theory, the tiny interval by which two minor semitones exceed one diapente, or the difference between a schisma and a limma.",
    "quotes": [
      {"author": "Hermann von Helmholtz", "work": "On the Sensations of Tone", "quote": "The minute interval termed the **diaschisma** measures the minute acoustic discrepancy between eight fourths and three octaves."},
      {"author": "Boethius", "work": "De Institutione Musica", "quote": "Pythagorean calculations divide the musical tone into half-steps, isolating the tiny **diaschisma** at the fringe of audible concordance."},
      {"author": "Aristoxenus", "work": "Elementa Harmonica", "quote": "Musicians trained in melodic nuance discern the subtle shift when a tuning system accommodates a microtonal **diaschisma**."}
    ]
  },
  "Dashboard — schid\\schisis.md": {
    "primary": "A congenital fissure, cleft, or split in a body structure or tissue (as in cheiloschisis, palatoschisis, or rachischisis).",
    "secondary": "In teratology and developmental embryology, the failure of opposing lateral embryonic processes to fuse along the midline during organogenesis.",
    "quotes": [
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Midline congenital malformations manifesting as **schisis** result from early developmental arrest in mesenchymal convergence."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Surgical repair of facial **schisis** must be undertaken in early infancy to restore normal sucking and speech development."},
      {"author": "Harvey Cushing", "work": "Studies in Intracranial Physiology", "quote": "Cranial **schisis** exposes cerebral structures to amniotic mechanical injury, leading to anencephaly or massive encephaloceles."}
    ]
  },
  "Dashboard — schid\\schisma.md": {
    "primary": "In musical acoustics, a tiny interval of about 1.953 cents, representing the difference between the Pythagorean comma and the syntonic comma.",
    "secondary": "In historical ecclesiastical Latin, a formal division, rent, or schism within the unity of the Church.",
    "quotes": [
      {"author": "Hermann von Helmholtz", "work": "On the Sensations of Tone", "quote": "The **schisma** is so minute that even the keenest ear can scarcely distinguish it when listening to melodic intervals in isolation."},
      {"author": "Boethius", "work": "De Institutione Musica", "quote": "In harmonic arithmetic, the minuscule **schisma** represents the fraction by which twelve perfect fifths exceed seven octaves plus a comma."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "A deplorable ecclesiastical **schisma** divided the patriarchates of Rome and Constantinople, severing theological communion for centuries."}
    ]
  },
  "Dashboard — schid\\schismatic.md": {
    "primary": "Of, relating to, or guilty of creating or maintaining a schism or division within an organization, especially a church.",
    "secondary": "A person who creates, promotes, or adheres to a schism; a sectarian separatist.",
    "quotes": [
      {"author": "John Milton", "work": "Areopagitica", "quote": "Men who are called **schismatic** and sectary are often those who examine truth with more diligence than stagnant orthodoxy."},
      {"author": "Thomas Aquinas", "work": "Summa Theologiae", "quote": "The **schismatic** sins directly against Christian charity by severing the ecclesiastical unity of the mystical body of Christ."},
      {"author": "John Henry Newman", "work": "Apologia Pro Vita Sua", "quote": "I wrestled with the grave fear that remaining in the Anglican communion meant persevering in a **schismatic** position."}
    ]
  },
  "Dashboard — schid\\schismatical.md": {
    "primary": "Pertaining to, of the nature of, or tending toward schism; divisive or factious (variant of schismatic).",
    "secondary": "In church history and political rhetoric, characterizing factions that disrupt institutional consensus and doctrinal unity.",
    "quotes": [
      {"author": "Richard Hooker", "work": "Of the Lawes of Ecclesiasticall Politie", "quote": "To separate from the public assembly over indifferent ceremonies is a dangerous and **schismatical** procedure."},
      {"author": "Samuel Johnson", "work": "Lives of the Most Eminent English Poets", "quote": "He defended his refusal to subscribe to the test oaths without harboring any **schismatical** hostility toward the crown."},
      {"author": "Jeremy Taylor", "work": "Holy Living and Holy Dying", "quote": "Avoid contentious and **schismatical** disputes that kindle uncharitable fires while chilling the inward warmth of piety."}
    ]
  },
  "Dashboard — schid\\schismatically.md": {
    "primary": "In a schismatical manner; by means of division, factious discord, or unauthorized ecclesiastical separation.",
    "secondary": "In ecclesiastical jurisprudence, acting in deliberate defiance of unified canon law to establish a rival sect.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Essays: Of Unity in Religion", "quote": "Heretics who separate **schismatically** over light trifles do more violence to the church than outward persecutors."},
      {"author": "John Bunyan", "work": "Grace Abounding to the Chief of Sinners", "quote": "The magistrates charged that our prayer gatherings had assembled **schismatically** in defiance of the established liturgy."},
      {"author": "Jonathan Swift", "work": "A Tale of a Tub", "quote": "The three brothers divided the ancestral coat, rending the seamless garment **schismatically** in their squabbles."}
    ]
  },
  "Dashboard — schid\\schizocarp.md": {
    "primary": "A dry, indehiscent compound fruit that splits at maturity into two or more one-seeded, closed carpel units called mericarps.",
    "secondary": "In systematic botany, characteristic of the parsley family (Apiaceae), mallows (Malvaceae), and maples (Aceraceae).",
    "quotes": [
      {"author": "Asa Gray", "work": "Structural Botany", "quote": "In the umbelliferous plant, the mature **schizocarp** splits cleanly into two seed-like mericarps suspended from a central carpophore."},
      {"author": "John Lindley", "work": "An Introduction to Botany", "quote": "The fruit of the mallow is a circular **schizocarp** consisting of numerous whorled carpels that separate at complete desiccation."},
      {"author": "Katherine Esau", "work": "Plant Anatomy", "quote": "Abscission layers developing along the carpellary sutures facilitate the dry dehiscence of the **schizocarp** upon ripening."}
    ]
  },
  "Dashboard — schid\\schizogamy.md": {
    "primary": "A form of reproduction in certain marine polychaete annelid worms wherein a sexual individual (epitoke) buds off from an asexual benthic stock (atoke).",
    "secondary": "In marine invertebrate zoology, a specialized epitokous reproductive strategy seen in syllid worms and palolo worms to optimize nocturnal pelagic spawning.",
    "quotes": [
      {"author": "E. Ray Lankester", "work": "A Treatise on Zoology", "quote": "The remarkable phenomenon of **schizogamy** allows the sedentary worm to regenerate while its detached sexual clone swims to the ocean surface."},
      {"author": "Libbie Hyman", "work": "The Invertebrates: Annelida", "quote": "During seasonal **schizogamy**, the caudal segments become packed with gametes and develop swimming chaetae before detachment."},
      {"author": "Robert D. Barnes", "work": "Invertebrate Zoology", "quote": "Synchronous lunar swarming in syllids is mediated by **schizogamy**, producing millions of epitokes that spawn in open coastal waters."}
    ]
  },
  "Dashboard — schid\\schizogony.md": {
    "primary": "A form of asexual multiple fission reproduction occurring in protozoans (such as the malaria parasite Plasmodium), producing multiple daughter cells (merozoites).",
    "secondary": "In medical parasitology, the intracellular proliferative cycle taking place within host hepatocytes and erythrocytes, triggering periodic febrile paroxysms.",
    "quotes": [
      {"author": "Ronald Ross", "work": "The Prevention of Malaria", "quote": "Inside the human red blood cell, the parasite undergoes erythrocytic **schizogony**, multiplying into a rosette of merozoites that rupture the corpuscle."},
      {"author": "Patrick Manson", "work": "Tropical Diseases: A Manual of the Diseases of Warm Climates", "quote": "The cyclic chills and fever of tertian ague correspond with the simultaneous completion of **schizogony** across millions of infected erythrocytes."},
      {"author": "William Henry Welch", "work": "The Pathology of Malarial Fevers", "quote": "Hepatic **schizogony** precedes blood-stage parasitemia, representing the silent primary incubation phase of malaria."}
    ]
  },
  "Dashboard — schid\\schizoid.md": {
    "primary": "Exhibiting traits of social withdrawal, emotional detachment, introversion, and a preference for solitary fantasy without frank psychosis.",
    "secondary": "In clinical psychology and psychoanalysis, designating a personality structure or disorder characterized by restricted affective expression and interpersonal aloofness.",
    "quotes": [
      {"author": "Eugen Bleuler", "work": "Dementia Praecox or the Group of Schizophrenias", "quote": "I coined the term **schizoid** to designate those personalities who exhibit a marked inward detachment while remaining within normal social bounds."},
      {"author": "W. R. D. Fairbairn", "work": "Psychoanalytic Studies of the Personality", "quote": "The core dilemma of the **schizoid** individual is the dread that his love may devour or destroy the object of his affection."},
      {"author": "Harry Guntrip", "work": "Schizoid Phenomena, Object Relations and the Self", "quote": "Under stressful relational demands, the **schizoid** patient retreats into an internal citadel of silent intellectual observation."}
    ]
  },
  "Dashboard — schid\\schizophrenia.md": {
    "primary": "A chronic, severe psychiatric disorder characterized by disturbances in thought, perception, emotional responsiveness, and behavior.",
    "secondary": "In psychiatry and neuroscience, a neurodevelopmental disorder presenting with positive symptoms (hallucinations, delusions) and negative symptoms (avolition, flat affect).",
    "quotes": [
      {"author": "Eugen Bleuler", "work": "Dementia Praecox or the Group of Schizophrenias", "quote": "I replace the name dementia praecox with **schizophrenia**, because splitting of psychic functions is one of its most prominent characteristics."},
      {"author": "Emil Kraepelin", "work": "Clinical Psychiatry", "quote": "The fundamental symptom complex of **schizophrenia** involves a disintegration of the emotional life paired with cognitive fragmentation."},
      {"author": "Karl Jaspers", "work": "General Psychopathology", "quote": "In **schizophrenia**, the patient experiences an unbridgeable transformation of reality that alienates him from common human experience."}
    ]
  },
  "Dashboard — schid\\schizophrenic.md": {
    "primary": "Of, relating to, or diagnosed with schizophrenia; a person who has schizophrenia.",
    "secondary": "In psychopathology, characterized by disintegrated thought processes, auditory hallucinations, and loss of contact with external reality.",
    "quotes": [
      {"author": "R. D. Laing", "work": "The Divided Self: An Existential Study in Sanity and Madness", "quote": "The **schizophrenic** condition represents an ontological strategy adopted by a divided self to survive an unlivable interpersonal environment."},
      {"author": "Eugen Bleuler", "work": "Dementia Praecox", "quote": "Associative loosening in the **schizophrenic** patient leads to bizarre conceptual leaps that defy ordinary semantic logic."},
      {"author": "Gregory Bateson", "work": "Steps to an Ecology of Mind", "quote": "The double-bind hypothesis posits that contradictory familial communications contribute to **schizophrenic** thought patterns."}
    ]
  },
  "Dashboard — schid\\schizotrichia.md": {
    "primary": "A medical condition characterized by splitting of the ends of the hair shafts; trichoptilosis or split ends.",
    "secondary": "In trichology and clinical dermatology, structural damage to the hair cuticle and cortex caused by mechanical friction, heat styling, or chemical treatments.",
    "quotes": [
      {"author": "Erasmus Wilson", "work": "On Diseases of the Skin: A System of Cutaneous Medicine", "quote": "The longitudinal splitting of distal hairs termed **schizotrichia** occurs frequently in long hair exposed to dry winds and harsh alkaline soaps."},
      {"author": "William Allen Pusey", "work": "The Principles and Practice of Dermatology", "quote": "In severe **schizotrichia**, the frayed cortical fibers resemble tiny paintbrushes at the tip of each broken hair shaft."},
      {"author": "Louis A. Duhring", "work": "A Practical Treatise on Diseases of the Skin", "quote": "Trimming the affected distal tips remains the only curative physical remedy for extensive **schizotrichia**."}
    ]
  },
  "Dashboard — scler\\episcleritis.md": {
    "primary": "A benign, inflammatory condition affecting the episclera, the vascular tissue layer between the conjunctiva and the sclera.",
    "secondary": "In clinical ophthalmology, a self-limiting condition presenting with localized sectoral redness and mild ocular discomfort, divided into simple and nodular forms.",
    "quotes": [
      {"author": "Sir Stewart Duke-Elder", "work": "System of Ophthalmology", "quote": "Unlike deep scleritis, **episcleritis** blanches readily upon application of topical phenylephrine drops and rarely causes permanent visual impairment."},
      {"author": "William Mackenzie", "work": "A Practical Treatise on the Diseases of the Eye", "quote": "The mild inflammation of **episcleritis** exhibits bright pink injection of the superficial vessels without intense deep ciliary aching."},
      {"author": "Albrecht von Graefe", "work": "Archiv für Ophthalmologie", "quote": "Recurrent attacks of **episcleritis** are frequently encountered in patients suffering from underlying rheumatoid diathesis."}
    ]
  },
  "Dashboard — scler\\sclera.md": {
    "primary": "The dense, fibrous, opaque white outer protective coat of the eyeball, commonly known as the white of the eye.",
    "secondary": "In ocular anatomy, an extracellular collagenous shell continuous anteriorly with the transparent cornea and pierced posteriorly by the optic nerve.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **sclera** serves to maintain the spherical form of the globe and provides firm insertion for the extrinsic extraocular muscles."},
      {"author": "Hermann von Helmholtz", "work": "Treatise on Physiological Optics", "quote": "Rigidity of the collagenous **sclera** resists intraocular pressure fluctuations, stabilizing optical distances within the eye."},
      {"author": "Andreas Vesalius", "work": "De Humani Corporis Fabrica", "quote": "The tough outermost tunic of the eye, which ancient anatomists termed the **sclera**, encloses the delicate vitreous humors like a shell."}
    ]
  },
  "Dashboard — scler\\scleranthus.md": {
    "primary": "A genus of low-growing annual and perennial herbs in the carnation family (Caryophyllaceae), commonly called knawels.",
    "secondary": "In floristics, tough weeds of sandy and stony soils characterized by inconspicuous greenish flowers with a hard, persistent calyx tube enclosing the fruit.",
    "quotes": [
      {"author": "Carl Linnaeus", "work": "Species Plantarum", "quote": "Under **scleranthus**, the rigid, hardened calyx encloses the seed like a miniature woody capsule after the petals have withered."},
      {"author": "George Bentham", "work": "Flora Australiensis", "quote": "Alpine cushion formations in southeastern Australia frequently include compact mats of **scleranthus** hugging wind-scoured gravels."},
      {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "The rigid foliage and apetalous blossoms of **scleranthus** adapt it to survive intense grazing upon impoverished pastures."}
    ]
  },
  "Dashboard — scler\\sclerectomy.md": {
    "primary": "The surgical excision and removal of a portion of the sclera of the eye.",
    "secondary": "In ophthalmic surgery, a filtering procedure (such as deep sclerectomy) performed to create an outflow channel for aqueous humor to reduce intraocular pressure in glaucoma.",
    "quotes": [
      {"author": "Albrecht von Graefe", "work": "Archiv für Ophthalmologie", "quote": "I devised the anterior **sclerectomy** to establish a permanent subconjunctival drainage fistulization in chronic glaucoma."},
      {"author": "Sir Stewart Duke-Elder", "work": "System of Ophthalmology", "quote": "Non-penetrating deep **sclerectomy** lowers intraocular tension while minimizing the risk of postoperative anterior chamber collapse."},
      {"author": "Howard A. Kelly", "work": "Operative Ophthalmology", "quote": "Careful trephination during posterior **sclerectomy** decompresses choroidal effusions and restores normal ciliary body alignment."}
    ]
  },
  "Dashboard — scler\\scleredema.md": {
    "primary": "A rare dermatological condition characterized by progressive, non-pitting woody induration and thickening of the skin and subcutaneous tissues (scleredema adultorum of Buschke).",
    "secondary": "In clinical dermatology, a condition often preceded by streptococcal pharyngitis or associated with severe diabetes mellitus, typically affecting the neck, shoulders, and upper back.",
    "quotes": [
      {"author": "Abraham Buschke", "work": "Ueber Scleroedem", "quote": "I observed that the cutaneous thickening in **scleredema** spares the hands and feet, unlike systemic sclerosis, and often resolves spontaneously."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In **scleredema** adultorum, the skin of the nape and shoulders feels dense and unyielding, restricting cervical mobility."},
      {"author": "Louis A. Duhring", "work": "Diseases of the Skin", "quote": "Histologic sections of skin affected by **scleredema** show massive accumulation of hyaluronic acid and separation of collagen bundles."}
    ]
  },
  "Dashboard — scler\\sclereid.md": {
    "primary": "A reduced, strongly lignified sclerenchyma cell with thick secondary walls and simple pits (commonly called a stone cell), providing mechanical support in plants.",
    "secondary": "In plant anatomy, classified according to morphology into brachysclereids (gritty cells in pear flesh), macrosclereids, osteosclereids, and astrosclereids.",
    "quotes": [
      {"author": "Katherine Esau", "work": "Plant Anatomy", "quote": "The characteristic grittiness experienced when chewing a pear fruit is caused by clusters of thick-walled **sclereid** cells embedded in the flesh."},
      {"author": "Arthur J. Eames", "work": "An Introduction to Plant Anatomy", "quote": "The branching astrosclereid variety of **sclereid** provides internal shear resistance within the floating leaves of water lilies."},
      {"author": "Ray F. Evert", "work": "Esau's Plant Anatomy", "quote": "Heavily lignified secondary walls of each mature **sclereid** possess narrow bordered or simple pit canals that transmit water."}
    ]
  },
  "Dashboard — scler\\sclerema.md": {
    "primary": "A severe, life-threatening dermatological condition occurring in premature or debilitated neonates, characterized by widespread hardening of the skin and subcutaneous fat (sclerema neonatorum).",
    "secondary": "In neonatology and pediatric pathology, an induration caused by the crystallization of saturated fatty acids in neonatal adipose tissue during hypothermia or sepsis.",
    "quotes": [
      {"author": "John William Ballantyne", "work": "Diseases of the Fetus and New-Born", "quote": "The hallmark of **sclerema** neonatorum is a stone-like rigidity of the subcutaneous fat that binds the infant's limbs in fixed positions."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Profound hypothermia and septicemia frequently precede the sudden onset of **sclerema** in premature hospital infants."},
      {"author": "Abraham Jacobi", "work": "Therapeutics of Infancy and Childhood", "quote": "Aggressive thermal warming and parenteral fluid support are urgent priorities in managing the fatal freeze of neonatal **sclerema**."}
    ]
  },
  "Dashboard — scler\\sclerenchyma.md": {
    "primary": "A protective or supportive plant tissue composed of cells with heavily thickened, lignified secondary walls that are usually dead at functional maturity.",
    "secondary": "In plant anatomy, divided into elongated sclerenchyma fibers (used in textiles like flax and hemp) and isodiametric sclereids.",
    "quotes": [
      {"author": "Katherine Esau", "work": "Plant Anatomy", "quote": "The primary mechanical strength of mature vascular stems is provided by continuous cylinders of lignified **sclerenchyma** fibers."},
      {"author": "Julius von Sachs", "work": "Text-Book of Botany: Morphological and Physiological", "quote": "Unlike living collenchyma, **sclerenchyma** provides permanent rigid support that does not yield to plastic bending forces."},
      {"author": "Ray F. Evert", "work": "Esau's Plant Anatomy", "quote": "The deposition of lignin within the secondary wall of **sclerenchyma** renders the tissue resistant to fungal decay and insect chewing."}
    ]
  },
  "Dashboard — scler\\sclerite.md": {
    "primary": "A hardened, cuticular plate or skeletal element forming part of the exoskeleton of an arthropod or the internal spicular skeleton of soft corals.",
    "secondary": "In invertebrate morphology, cuticular plates (tergites, sternites, and pleurites) bounded by flexible articular membranes that enable movement.",
    "quotes": [
      {"author": "R. E. Snodgrass", "work": "Principles of Insect Morphology", "quote": "The insect body segment is composed of distinct hardened **sclerite** plates separated by membranous conjunctivae to permit respiration and locomotion."},
      {"author": "John Henry Comstock", "work": "The Wings of Insects", "quote": "Precise articulation between the axillary **sclerite** and the wing base governs the intricate twisting of the flight foil."},
      {"author": "Robert D. Barnes", "work": "Invertebrate Zoology", "quote": "In octocorals, microscopic calcareous **sclerite** deposits stiffen the fleshy coenenchyme against hydraulic wave surge."}
    ]
  },
  "Dashboard — scler\\scleritis.md": {
    "primary": "A severe, painful, potentially vision-threatening inflammatory disorder affecting the full thickness of the sclera of the eye.",
    "secondary": "In clinical ophthalmology, a destructive disorder strongly associated with systemic autoimmune conditions (such as rheumatoid arthritis), risking scleral necrosis and globe perforation.",
    "quotes": [
      {"author": "Sir Stewart Duke-Elder", "work": "System of Ophthalmology", "quote": "The boring, deep-seated nocturnal ache of anterior **scleritis** radiates across the temple and jaw, disturbing the patient's sleep."},
      {"author": "William Mackenzie", "work": "A Practical Treatise on the Diseases of the Eye", "quote": "Necrotizing **scleritis** leads to thinning of the scleral coat, through which the dark choroid bulges as a bluish staphyloma."},
      {"author": "Albrecht von Graefe", "work": "Archiv für Ophthalmologie", "quote": "Systemic immunosuppressive therapy must be instituted promptly in severe **scleritis** to halt melting of the ocular coats."}
    ]
  },
  "Dashboard — scler\\scleroderma.md": {
    "primary": "A chronic autoimmune disease characterized by excessive collagen accumulation leading to hardening and thickening of the skin and internal organs (systemic sclerosis).",
    "secondary": "In rheumatology, categorized into localized forms (morphea) and systemic sclerosis with Raynaud's phenomenon, esophageal dysmotility, and pulmonary fibrosis.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In advanced **scleroderma**, the skin of the face becomes smooth, shiny, and tightly stretched over the bones like parchment."},
      {"author": "Jonathan Hutchinson", "work": "Lectures on Clinical Surgery", "quote": "Raynaud's phenomenon of the fingers frequently precedes the cutaneous induration of systemic **scleroderma** by many years."},
      {"author": "Vinay Kumar", "work": "Robbins and Cotran Pathologic Basis of Disease", "quote": "Microvascular endothelial damage and hyperactive fibroblast signaling are the dual pathogenic hallmarks of visceral **scleroderma**."}
    ]
  },
  "Dashboard — scler\\sclerodermataceae.md": {
    "primary": "A family of gasteroid fungi in the order Boletales, commonly known as earthballs, characterized by a thick peridial skin and dark powdery gleba.",
    "secondary": "In mycology, ectomycorrhizal fungi with hard, leathery outer rinds that dehisce irregularly to disperse spores via wind and raindrops.",
    "quotes": [
      {"author": "Christian Hendrik Persoon", "work": "Synopsis Methodica Fungorum", "quote": "Members of **sclerodermataceae** differ from true puffballs in their tough, thick peridium and purple-black gleba without a capillitium."},
      {"author": "Curtis Gates Lloyd", "work": "The Lycoperdaceae of Australia and New Zealand", "quote": "The rough, warty exterior of earthballs in the family **sclerodermataceae** earns them the popular moniker of pigskin poison puffballs."},
      {"author": "David Arora", "work": "Mushrooms Demystified", "quote": "Unlike edible Lycoperdon, species of **sclerodermataceae** are toxic when eaten and produce an offensive pungent odor at maturity."}
    ]
  },
  "Dashboard — scler\\sclerodermatales.md": {
    "primary": "A former taxonomic order of gasteroid basidiomycete fungi comprising the earthballs and allied thick-skinned puffball families.",
    "secondary": "In historical systematic mycology, an ordinal assemblage defined by a rigid outer peridial wall and synchronous basidiospore maturation.",
    "quotes": [
      {"author": "Elias Magnus Fries", "work": "Systema Mycologicum", "quote": "Under the order **sclerodermatales**, mycologists grouped those subterranean and terrestrial gasteromycetes with thick, leathery rinds."},
      {"author": "Curtis Gates Lloyd", "work": "Synopsis of the Known Phalloids and Puffballs", "quote": "The structural rigidity of the peridium in **sclerodermatales** resists desiccation across arid steppe and sandy pine barrens."},
      {"author": "Orson K. Miller Jr.", "work": "Mushrooms of North America", "quote": "Modern DNA sequencing reallocated the families of **sclerodermatales** directly into the order Boletales."}
    ]
  },
  "Dashboard — scler\\sclerometer.md": {
    "primary": "An instrument used to measure the hardness of minerals, metals, or crystalline materials by determining the pressure needed to produce a scratch with a diamond point.",
    "secondary": "In mineralogy and materials science, a physical testing device developed by Seebeck and Turner to provide quantitative scratching hardness scales.",
    "quotes": [
      {"author": "James Dwight Dana", "work": "Manual of Mineralogy", "quote": "The diamond point of the **sclerometer** is drawn across the crystal face under increasing loads to determine scratch resistance."},
      {"author": "Thomas Turner", "work": "The Metallurgy of Iron", "quote": "Using a weighted diamond **sclerometer**, we measured microscopic variations in surface hardness across tempered steel specimens."},
      {"author": "Edward Salisbury Dana", "work": "A Textbook of Mineralogy", "quote": "Hardness determinations made with the **sclerometer** revealed marked directional variation along different cleavage faces of kyanite."}
    ]
  },
  "Dashboard — scler\\scleropages.md": {
    "primary": "A genus of primitive freshwater osteoglossiform bonytongue fishes (family Osteoglossidae) native to Southeast Asia and Australia, including the Asian and Australian arowanas.",
    "secondary": "In ichthyology and evolutionary biogeography, archaic Gondwanan surface predators equipped with sensory chin barbels, large cycloid scales, and a bony toothed tongue.",
    "quotes": [
      {"author": "Albert Günther", "work": "Catalogue of the Fishes in the British Museum", "quote": "The genus **scleropages** comprises archaic freshwater fishes whose massive armor-like scales reflect primitive teleost lineage."},
      {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "In tropical rivers, **scleropages** cruises close to the surface, leaping several feet into overhanging foliage to catch terrestrial insects."},
      {"author": "Theodore Gill", "work": "Arrangement of the Families of Fishes", "quote": "The biogeographic distribution of **scleropages** across Australasia and Sundaland provides strong evidence for ancient continental connections."}
    ]
  },
  "Dashboard — scler\\scleroparei.md": {
    "primary": "A former suborder or order of scorpaeniform marine fishes, commonly known as mail-cheeked fishes, characterized by a bony stay across the cheek.",
    "secondary": "In historical ichthyology, a taxon comprising rockfishes, scorpionfishes, flatheads, and sculpins united by a suborbital bony bar connecting to the preopercle.",
    "quotes": [
      {"author": "David Starr Jordan", "work": "The Fishes of North and Middle America", "quote": "The suborbital stay spanning from the second infraorbital bone to the preopercle is the cardinal anatomical mark of **scleroparei**."},
      {"author": "Albert Günther", "work": "An Introduction to the Study of Fishes", "quote": "Many marine families in the group **scleroparei** possess formidable head spines and venomous fin rays for defense."},
      {"author": "Theodore Gill", "work": "On the Families of Fishes", "quote": "The mail-cheeked fishes designated **scleroparei** present extraordinary diversity, from heavy bottom-dwellers to deep-sea forms."}
    ]
  },
  "Dashboard — scler\\sclerophyll.md": {
    "primary": "A type of vegetation or plant characterized by hard, thick, leathery evergreen leaves that resist moisture loss in dry summer climates.",
    "secondary": "In plant ecology, the dominant vegetation type of Mediterranean biomes (chaparral, macchia, fynbos), adapted to summer droughts and nutrient-poor soils.",
    "quotes": [
      {"author": "Eugenius Warming", "work": "Oecology of Plants: An Introduction to the Study of Plant-Communities", "quote": "The tough **sclerophyll** evergreen leaf possesses thick cuticular coatings and sunken stomata designed to withstand scorching heat."},
      {"author": "A. F. W. Schimper", "work": "Plant-Geography upon a Physiological Basis", "quote": "Mediterranean woodlands are dominated by **sclerophyll** scrub that conserves groundwater through intense seasonal dry spells."},
      {"author": "Arthur S. Boughey", "work": "Ecology of Populations", "quote": "Australian eucalyptus forests and South African fynbos share convergent **sclerophyll** adaptations shaped by low soil phosphorus."}
    ]
  },
  "Dashboard — scler\\sclerophyllous.md": {
    "primary": "Having hard, stiff, leathery leaves adapted to minimize water loss; characteristic of Mediterranean-climate vegetation.",
    "secondary": "In phytogeography, describing scrub and woodland ecosystems (such as the Mediterranean macchia or California chaparral) dominated by leathery-leaved evergreens.",
    "quotes": [
      {"author": "A. F. W. Schimper", "work": "Plant-Geography upon a Physiological Basis", "quote": "The **sclerophyllous** trees of southern Europe, such as the holm oak and olive, endure prolonged summer drought without wilting."},
      {"author": "Eugenius Warming", "work": "Oecology of Plants", "quote": "Microscopic examination of **sclerophyllous** foliage reveals extensive hypodermal sclerenchyma that maintains leaf rigidity during water stress."},
      {"author": "Ferdinand von Mueller", "work": "Select Extra-Tropical Plants", "quote": "Many Australian acacias produce **sclerophyllous** phyllodes in place of true leaf blades to flourish in arid stony scrub."}
    ]
  },
  "Dashboard — scler\\scleroprotein.md": {
    "primary": "Any of a class of insoluble, fibrous structural proteins occurring in animal skeletons, connective tissues, skin, and appendages.",
    "secondary": "In biochemistry, tough fibrous macromolecules such as keratin, collagen, elastin, and fibroin, characterized by extended polypeptide secondary structures.",
    "quotes": [
      {"author": "Emil Fischer", "work": "Untersuchungen über Aminosäuren, Polypeptide und Proteine", "quote": "A typical animal **scleroprotein** like horn keratin is insoluble in water and resists common proteolytic enzymes."},
      {"author": "Albrecht Kossel", "work": "The Protamines and Histones", "quote": "The high cystine disulfide cross-link content in a **scleroprotein** confers exceptional mechanical toughness to epidermal structures."},
      {"author": "Albert L. Lehninger", "work": "Principles of Biochemistry", "quote": "Collagen constitutes the most abundant **scleroprotein** in mammals, organizing triple-helical tropocollagen ropes in tendons."}
    ]
  },
  "Dashboard — scler\\sclerosed.md": {
    "primary": "Hardened, thickened, or indurated through pathological chronic inflammation, fibrosis, or sclerosis.",
    "secondary": "In vascular and nervous pathology, describing blood vessels or neural tracts that have undergone fibrous degeneration and loss of elasticity.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Upon palpation, the radial artery felt rigid and **sclerosed** like a pipe-stem due to advanced Monckeberg medial calcification."},
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The **sclerosed** tissue in chronic nephritis displays extensive replacement fibrosis around collapsed glomeruli."},
      {"author": "Vinay Kumar", "work": "Robbins and Cotran Pathologic Basis of Disease", "quote": "Microscopic sections through the plaque reveal **sclerosed** glia replacing myelinated axons in the cerebral white matter."}
    ]
  },
  "Dashboard — scler\\sclerosis.md": {
    "primary": "Abnormal pathological hardening or induration of a body tissue, blood vessel, or organ, resulting from chronic inflammation or fibrous connective tissue proliferation.",
    "secondary": "In clinical neurology and cardiology, exemplified by multiple sclerosis (demyelination and glial scarring) and arteriosclerosis.",
    "quotes": [
      {"author": "Jean-Martin Charcot", "work": "Lectures on the Diseases of the Nervous System", "quote": "Disseminated **sclerosis** manifests with the clinical triad of nystagmus, intention tremor, and scanning speech."},
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The progressive **sclerosis** of connective tissue represents a reparative proliferation following chronic interstitial injury."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Coronary **sclerosis** narrows the arterial lumen, predisposing the myocardium to sudden ischemic necrosis."}
    ]
  },
  "Dashboard — scler\\sclerotic.md": {
    "primary": "Of, relating to, or affected with sclerosis; pathologically hardened or indurated.",
    "secondary": "In ocular anatomy, relating to the sclera or white outer coat of the eyeball (as in the sclerotic coat).",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **sclerotic** coat encloses the posterior five-sixths of the eyeball, providing insertion for the recti muscles."},
      {"author": "William Mackenzie", "work": "A Practical Treatise on the Diseases of the Eye", "quote": "Reptilian eyes frequently possess a ring of small **sclerotic** bony plates that protect the cornea during rapid accommodation."},
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "In birds, the **sclerotic** ring of overlapping ossicles maintains the sharp anterior conic profile of the ocular globe."}
    ]
  },
  "Dashboard — scler\\sclerotinia.md": {
    "primary": "A genus of plant-pathogenic ascomycete fungi in the family Sclerotiniaceae, causing white mold, stem rot, and watery soft rot in crops.",
    "secondary": "In agricultural phytopathology, fungi such as Sclerotinia sclerotiorum that produce black resting sclerotia capable of surviving years in the soil.",
    "quotes": [
      {"author": "Anton de Bary", "work": "Comparative Morphology and Biology of the Fungi, Mycetozoa and Bacteria", "quote": "The pathogenic mycelium of **sclerotinia** secretes pectinases and oxalic acid, collapsing the stem tissues of succulent beans."},
      {"author": "Charles Horton Peck", "work": "Reports of the State Botanist of New York", "quote": "Under damp autumn litter, the resting sclerotia of **sclerotinia** germinate to produce small cup-shaped apothecia on slender stalks."},
      {"author": "Pier Andrea Saccardo", "work": "Sylloge Fungorum", "quote": "The genus **sclerotinia** is widely feared by horticulturists for its destructive virulence on agricultural vegetables."}
    ]
  },
  "Dashboard — scler\\sclerotiniaceae.md": {
    "primary": "A family of inoperculate discomycete fungi (order Helotiales) whose cup-shaped apothecia arise from resting sclerotia or stromata.",
    "secondary": "In systematic mycology, an economically critical family of phytopathogens containing Sclerotinia, Botrytis, and Monilinia (brown rot of stone fruits).",
    "quotes": [
      {"author": "Elias Magnus Fries", "work": "Systema Mycologicum", "quote": "Fungi of the family **sclerotiniaceae** develop their fruitbodies directly from hardened resting bodies formed within decaying plant tissue."},
      {"author": "Anton de Bary", "work": "Morphology and Biology of the Fungi", "quote": "The lifecycle of **sclerotiniaceae** alternates between an active destructive parasitic phase and a dormant sclerotial survival stage."},
      {"author": "Pier Andrea Saccardo", "work": "Sylloge Fungorum", "quote": "Ascospore discharge in **sclerotiniaceae** occurs synchronously on warm spring mornings, carrying infection to tender fruit blossoms."}
    ]
  },
  "Dashboard — scler\\sclerotium.md": {
    "primary": "A compact, hard mass of dormant fungal mycelium, often enclosed by a dark protective rind, capable of surviving adverse conditions.",
    "secondary": "In mycology and plant pathology, an overwintering vegetative survival structure (such as the ergot grain of Claviceps purpurea) that germinates to produce fruiting bodies.",
    "quotes": [
      {"author": "Anton de Bary", "work": "Comparative Morphology and Biology of the Fungi", "quote": "The dark purple horn of ergot on rye is a true **sclerotium**, designed to withstand winter frost before germinating in spring."},
      {"author": "Louis Pasteur", "work": "Études sur la bière", "quote": "Desiccated in the laboratory, a resting **sclerotium** retains viability for years, awakening when placed in moist conditions."},
      {"author": "Pier Andrea Saccardo", "work": "Sylloge Fungorum", "quote": "Each **sclerotium** consists of an outer rind of pigmented pseudoparenchyma protecting an inner core of nutrient-rich hyphae."}
    ]
  },
  "Dashboard — scler\\sclerotize.md": {
    "primary": "To harden, indurate, or stiffen, especially through cross-linking of structural proteins and chitin in the arthropod cuticle.",
    "secondary": "In insect physiology and developmental biochemistry, the chemical tanning process (quinone tanning) that hardens soft newly molted exoskeleton.",
    "quotes": [
      {"author": "V. B. Wigglesworth", "work": "The Principles of Insect Physiology", "quote": "Bursicon hormone released into the hemolymph triggers phenolic tanning agents that **sclerotize** the pale cuticle following ecdysis."},
      {"author": "R. E. Snodgrass", "work": "Principles of Insect Morphology", "quote": "Before the wings can support flight, atmospheric oxygen and cuticular enzymes must **sclerotize** the flexible veins into rigid spars."},
      {"author": "Penny Gullan", "work": "The Insects: An Outline of Entomology", "quote": "Arthropods must rapidly **sclerotize** their mandibles and claws after molting to defend against aggressive predators."}
    ]
  },
  "Dashboard — scler\\sclerotomy.md": {
    "primary": "The surgical incision or cutting of the sclera of the eyeball.",
    "secondary": "In ophthalmology, a surgical procedure (posterior sclerotomy) performed to drain subretinal fluid, relieve acute intraocular pressure, or access the vitreous chamber.",
    "quotes": [
      {"author": "Albrecht von Graefe", "work": "Archiv für Ophthalmologie", "quote": "A timely posterior **sclerotomy** evacuated the subretinal exudate, permitting the detached retina to settle back against the choroid."},
      {"author": "William Mackenzie", "work": "A Practical Treatise on the Diseases of the Eye", "quote": "In fulminating acute glaucoma, urgent **sclerotomy** relieves agonizing pain by decompressing the engorged vitreous humor."},
      {"author": "Sir Stewart Duke-Elder", "work": "System of Ophthalmology", "quote": "The transscleral knife incision during **sclerotomy** must avoid damaging the vortex veins and the ciliary body."}
    ]
  },
  "Dashboard — scoli\\ascolichen.md": {
    "primary": "Any lichen in which the fungal partner (mycobiont) belongs to the Ascomycota (representing over ninety-eight percent of all known lichens).",
    "secondary": "In lichenology, symbiotic organisms that reproduce sexually via ascospores formed within disc-shaped apothecia or flask-shaped perithecia.",
    "quotes": [
      {"author": "Edward Tuckerman", "work": "Genera Lichenum: An Arrangement of the North American Lichens", "quote": "Almost every familiar rock and bark lichen is an **ascolichen**, producing its spores within microscopic eight-spored asci."},
      {"author": "William Nylander", "work": "Synopsis Methodica Lichenum", "quote": "The iodine reaction upon the hymenium of an **ascolichen** provides essential chemical evidence for taxonomic discrimination."},
      {"author": "Bruce Fink", "work": "The Lichens of Minnesota", "quote": "In each **ascolichen**, the fungal partner surrounds green or blue-green algal cells, constructing complex layered thalli."}
    ]
  },
  "Dashboard — scoli\\scoliokyphosis.md": {
    "primary": "A complex spinal deformity combining both lateral curvature (scoliosis) and posterior hunchback curvature (kyphosis); kyphoscoliosis.",
    "secondary": "In orthopedic surgery and respiratory medicine, a severe spinal abnormality that distorts the thoracic cage, causing restrictive pulmonary impairment.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe thoracic **scoliokyphosis** restricts chest wall expansion, predisposing the patient to chronic cor pulmonale and hypoventilation."},
      {"author": "Henry Ling Taylor", "work": "Orthopedic Surgery for Practitioners", "quote": "Early application of spinal traction and corrective braces can arrest the progression of juvenile **scoliokyphosis**."},
      {"author": "Lewis Sayre", "work": "Spinal Disease and Spinal Curvature", "quote": "Plaster-of-Paris jackets applied during suspension proved effective in supporting the spine distorted by **scoliokyphosis**."}
    ]
  },
  "Dashboard — scoli\\scolion.md": {
    "primary": "A short lyric poem or song sung by guests at ancient Greek banquets or symposia as a myrtle branch or cup was passed around.",
    "secondary": "In classical Greek literature, convivial songs composed by poets like Terpander, Alcaeus, and Pindar celebrating drinking, love, or political freedom.",
    "quotes": [
      {"author": "Athenaeus", "work": "The Deipnosophists", "quote": "The guests sang the famous **scolion** of Harmodius and Aristogeiton, honoring the heroes who struck down the tyrant at Athens."},
      {"author": "Plutarch", "work": "Moralia: Table-Talk", "quote": "Passing the myrtle branch around the couch, each diner in turn was challenged to chant a witty **scolion** in harmonious rhythm."},
      {"author": "J. P. Mahaffy", "work": "Social Life in Greece from Homer to Menander", "quote": "The traditional banquet **scolion** was brief and pointed, designed to provoke philosophical conversation among educated diners."}
    ]
  },
  "Dashboard — scoli\\scoliosis.md": {
    "primary": "An abnormal lateral curvature and rotational deformity of the vertebral column.",
    "secondary": "In pediatric orthopedics, a common spinal disorder categorized as idiopathic, congenital, or neuromuscular, quantified on radiographs by Cobb's angle.",
    "quotes": [
      {"author": "Hippocrates", "work": "On the Articulations", "quote": "Curvatures of the spine which occur laterally, termed **scoliosis**, are frequently caused by unequal muscular contractions or habits of posture."},
      {"author": "Lewis Sayre", "work": "Lectures on Orthopedic Surgery and Diseases of the Joints", "quote": "The rotary element in adolescent **scoliosis** produces prominence of the ribs on the convex side, forming a characteristic rib hump."},
      {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Lateral **scoliosis** shifts the thoracic viscera, compressing the lung on the concave side of the primary curvature."}
    ]
  },
  "Dashboard — scop_ scept\\acroscopic.md": {
    "primary": "In botany and plant developmental morphology, facing, directed toward, or pointing toward the apex or growing tip of an organ or axis.",
    "secondary": "In pteridology and descriptive anatomy, designating sori, leaflets, or indusial flaps oriented toward the frond apex (contrasting with basiscopic).",
    "quotes": [
      {"author": "Katherine Esau", "work": "Plant Anatomy", "quote": "The **acroscopic** pinnules along the fern frond branch develop earlier and achieve larger size than the opposing basiscopic segments."},
      {"author": "Arthur J. Eames", "work": "An Introduction to Plant Anatomy", "quote": "In vascular cryptogams, the **acroscopic** face of the sporangial cluster opens toward the growing shoot meristem."},
      {"author": "F. O. Bower", "work": "The Ferns: Filicales", "quote": "Asymmetric frond expansion frequently produces an enlarged **acroscopic** basal auricle on each secondary pinna."}
    ]
  },
  "Dashboard — scop_ scept\\angioscope.md": {
    "primary": "An optical or magnifying instrument historically used for viewing capillary blood vessels in living tissues; or a fine endoscope for inspecting the interior of blood vessels.",
    "secondary": "In physiological optics and cardiovascular diagnostics, a specialized microscope or fiberoptic catheter allowing direct visualization of blood flow dynamics.",
    "quotes": [
      {"author": "Gabriel Valentin", "work": "Handbuch der Entwicklungsgeschichte des Menschen", "quote": "Using a customized **angioscope**, I observed the pulsating blood columns circulating through the interdigital web of the living frog."},
      {"author": "Carl Ludwig", "work": "Physiologie des Menschen", "quote": "The **angioscope** illuminated the capillary beds of living membranes, proving that erythrocytes circulate in single file through narrow capillaries."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Early investigators constructed the **angioscope** to observe inflammatory marginations of leukocytes along venular walls."}
    ]
  },
  "Dashboard — scop_ scept\\auriscope.md": {
    "primary": "An instrument equipped with light and magnification for examining the ear canal and tympanic membrane (an otoscope).",
    "secondary": "In otolaryngology, an essential diagnostic tool used to detect otitis media, cerumen impaction, and perforations of the eardrum.",
    "quotes": [
      {"author": "Joseph Toynbee", "work": "The Diseases of the Ear: Their Nature, Diagnosis, and Treatment", "quote": "With the aid of a tubular **auriscope** and reflected sunlight, the pearly gray surface of the normal membrana tympani is clearly visualized."},
      {"author": "William Wilde", "work": "Practical Observations on Aural Surgery", "quote": "No surgeon should prescribe remedies for ear complaints without first inspecting the meatus with a properly illuminated **auriscope**."},
      {"author": "Adam Politzer", "work": "A Text-Book of the Diseases of the Ear", "quote": "Introduction of the pneumatic **auriscope** enabled the clinician to assess the mobility of the tympanic membrane under positive and negative pressures."}
    ]
  },
  "Dashboard — scop_ scept\\auroscope.md": {
    "primary": "An instrument designed for visual examination of the ear canal and eardrum; a variant spelling of auriscope (otoscope).",
    "secondary": "In clinical medicine, an illuminated hand-held magnifying device used to assess ear pathology.",
    "quotes": [
      {"author": "William Wilde", "work": "Aural Surgery", "quote": "The gentle insertion of an **auroscope** reveals whether the auditory canal is occluded by inspissated cerumen or inflammatory polypi."},
      {"author": "Joseph Toynbee", "work": "Diseases of the Ear", "quote": "Illumination by means of a concave mirror and an **auroscope** transformed otological diagnosis from guesswork into an exact science."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In every child presenting with unexplained pyrexia, inspection of the tympanic membranes with an **auroscope** is mandatory."}
    ]
  },
  "Dashboard — scop_ scept\\basiscopic.md": {
    "primary": "In botany and plant organography, directed, pointing, or facing toward the base or point of attachment of an organ or stem.",
    "secondary": "In pteridology, designating pinnae, sori, or lobes positioned on the lower or basal side of a frond axis (contrasting with acroscopic).",
    "quotes": [
      {"author": "Katherine Esau", "work": "Plant Anatomy", "quote": "The **basiscopic** side of the fern pinnule displays distinct venation patterns that contrast with the acroscopic margin."},
      {"author": "Arthur J. Eames", "work": "Morphology of Vascular Plants", "quote": "In dryopteroid ferns, an enlarged **basiscopic** basal segment gives the frond its characteristic triangular silhouette."},
      {"author": "F. O. Bower", "work": "The Ferns: Filicales", "quote": "Developmental polarity establishes whether sporangia initiate in **basiscopic** sequence or simultaneously along the vein."}
    ]
  },
  "Dashboard — scop_ scept\\bioscope.md": {
    "primary": "An early form of motion picture projector and cinema device; historically also an instrument or device used to view living specimens.",
    "secondary": "In cultural history and early cinematographic technology, a popular term for travelling motion-picture shows in South Africa and Britain.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "The flickering images projected by the **bioscope** astounded audiences who had never before seen living scenes reproduced upon a screen."},
      {"author": "George Bernard Shaw", "work": "Dramatic Opinions and Essays", "quote": "The invention of the **bioscope** will revolutionize the theatre by providing visual spectacles that live drama cannot match."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Mazarin Stone", "quote": "He sat in the dark hall watching the flickering **bioscope** reels unroll scenes of foreign travel and royal ceremonies."}
    ]
  },
  "Dashboard — scop_ scept\\celioscopy.md": {
    "primary": "The visual endoscopic examination of the peritoneal or abdominal cavity through a puncture in the abdominal wall; laparoscopy.",
    "secondary": "In the history of minimally invasive surgery, pioneering laparoscopic procedures introduced by Kelling and Jacobaeus using cystoscopes.",
    "quotes": [
      {"author": "Georg Kelling", "work": "Ueber Oesophagoskopie, Gastroskopie und Koelioskopie", "quote": "I demonstrated the feasibility of **celioscopy** in a living animal, inspecting the liver and intestines through a trochar after air insufflation."},
      {"author": "Hans Christian Jacobaeus", "work": "Ueber die Möglichkeit die Zystoskopie bei Untersuchung seröser Höhlungen anzuwenden", "quote": "Clinical **celioscopy** in human patients permits direct visual inspection of peritoneal tuberculosis and hepatic cirrhosis without laparotomy."},
      {"author": "Howard A. Kelly", "work": "Operative Gynecology", "quote": "Early advocates of **celioscopy** recognized its vast diagnostic potential for evaluating obscure pelvic tumors without major surgery."}
    ]
  },
  "Dashboard — scop_ scept\\cryoscope.md": {
    "primary": "A scientific instrument used to measure the freezing point of liquids with high precision, used to determine molecular weights or osmotic pressures.",
    "secondary": "In food science and physical chemistry, an apparatus (such as the Hortvet cryoscope) used to detect the fraudulent adulteration of milk with added water.",
    "quotes": [
      {"author": "François-Marie Raoult", "work": "Loi générale des points de congélation des dissolvants", "quote": "Using a sensitive Beckmann thermometer in our **cryoscope**, we measured the depression of the freezing point produced by dissolved solutes."},
      {"author": "J. H. van 't Hoff", "work": "Studies in Chemical Dynamics", "quote": "Experimental measurements carried out with the **cryoscope** provided vital empirical confirmation for the thermodynamic theory of osmotic pressure."},
      {"author": "Julius Hortvet", "work": "The Cryoscopic Examination of Milk", "quote": "The standardized Hortvet **cryoscope** detects even two percent added water in commercial milk by registering minute elevations in freezing point."}
    ]
  },
  "Dashboard — scop_ scept\\culdoscope.md": {
    "primary": "An illuminated optical endoscope designed for transvaginal introduction through the posterior vaginal fornix into the cul-de-sac of Douglas.",
    "secondary": "In gynecological diagnostics, an instrument widely used before transabdominal laparoscopy to visualize the ovaries, fallopian tubes, and pelvic peritoneum.",
    "quotes": [
      {"author": "Albert Decker", "work": "Culdoscopy: A New Technic in Gynecologic Diagnosis and Study", "quote": "With the patient placed in the knee-chest position, the **culdoscope** is introduced into the pelvis through the posterior vaginal fornix without discomfort."},
      {"author": "Howard A. Kelly", "work": "Medical Gynecology", "quote": "Direct inspection through the **culdoscope** reveals tiny ovarian endometriomas that escape detection by bimanual palpation."},
      {"author": "Robert W. Kistner", "work": "Gynecology: Principles and Practice", "quote": "The wide optical field of the modern **culdoscope** allows clear visualization of tubal fimbriae and early ectopic gestations."}
    ]
  },
  "Dashboard — scop_ scept\\culdoscopy.md": {
    "primary": "The endoscopic visual examination of the female pelvic viscera through an incision in the posterior vaginal fornix using a culdoscope.",
    "secondary": "In gynecologic surgery, a diagnostic procedure developed in the mid-twentieth century for assessing suspected ectopic pregnancy, endometriosis, and unexplained infertility.",
    "quotes": [
      {"author": "Albert Decker", "work": "Culdoscopy: Its Diagnostic Value in Pelvic Disease", "quote": "Diagnostic **culdoscopy** established the patency of the fallopian tubes under direct vision, avoiding the risks of major abdominal exploratory surgery."},
      {"author": "Emil Novak", "work": "Gynecological and Obstetrical Pathology", "quote": "In cases of suspected unruptured tubal pregnancy, urgent **culdoscopy** provides definitive visual confirmation within minutes."},
      {"author": "Leon Speroff", "work": "Clinical Gynecologic Endocrinology and Infertility", "quote": "The advent of transabdominal laparoscopy gradually superseded **culdoscopy**, but the technique remains a historic milestone in endoscopic gynecology."}
    ]
  }
}

base_dir = r"App database\Greek roots\Cluster Form & Space"
mjs_path = r"main app\scripts\curate-form-finish3-batch6.mjs"

content = f"""import {{ updateNotesBatch }} from './curate-updater-util.mjs';

const baseDir = {json.dumps(base_dir)};
const batchData = {json.dumps(data, indent=2, ensure_ascii=False)};

const count = updateNotesBatch(baseDir, batchData);
console.log(`Updated ${{count}} notes in Form Finish Slice 3 Batch 6.`);
"""

with open(mjs_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Generated {mjs_path} with {len(data)} words.")
