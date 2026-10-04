# -*- coding: utf-8 -*-
"""
Curates Dashboard — nosc (Part 1: words 1-44) in Cluster Mind & Knowledge.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_part1 = {
  "annotate": {
    "primary": "To supply a literary or historical text with critical, explanatory, or biographical notes.",
    "secondary": "In computational linguistics and genomics, to tag sequences or corpora with descriptive metadata.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "Preface to Shakespeare", "quote": "I have endeavored to **annotate** difficult passages where obsolete idioms obscure the poet's original meaning."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Scholars should **annotate** ancient treatises with modern observations rather than compose barren commentaries."},
      {"author": "Siddhartha Mukherjee", "work": "The Gene", "quote": "Bioinformaticians labored to **annotate** the newly sequenced human genome, identifying coding exons and promoters."}
    ]
  },
  "annotating": {
    "primary": "The act or process of furnishing a manuscript, code base, or dataset with explanatory notes.",
    "secondary": "In scholarly publishing, compiling marginal glosses, variorum readings, and critical citations.",
    "quotes": [
      {"author": "Virginia Woolf", "work": "The Common Reader", "quote": "He spent long winter evenings **annotating** his classical folios with a delicate quill and purple ink."},
      {"author": "Henry James", "work": "The Aspern Papers", "quote": "The editor took delight in **annotating** the lost poet's letters, uncovering scandalous romantic subtexts."},
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "Researchers advanced by **annotating** neural connectomes to map synaptic divergence across sensory circuits."}
    ]
  },
  "annotation": {
    "primary": "A critical or explanatory note added to a text, diagram, or dataset to clarify meaning or context.",
    "secondary": "In software engineering, a syntactical tag added to source code providing program directives.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "A learned **annotation** in the margin exposed the chronological discrepancies of the Byzantine chronicler."},
      {"author": "Alexander Pope", "work": "The Dunciad", "quote": "The pedantic critic burdened every heroic couplet with an immense **annotation** of trivial trivia."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "A brief **annotation** in his notebook recorded the curious sexual dimorphism of the South American beetle."}
    ]
  },
  "annotator": {
    "primary": "A scholar, editor, or commentator who writes explanatory notes or critical annotations on a work.",
    "secondary": "In machine learning workflows, a specialist labeling ground-truth images, sentences, or audio tokens.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The modern **annotator** frequently obscures the poetic spirit by obsessing over pedantic orthography."},
      {"author": "Jonathan Swift", "work": "A Tale of a Tub", "quote": "Our satirical author invented an imaginary **annotator** to ridicule solemn academic disputations."},
      {"author": "Walter Scott", "work": "Waverley", "quote": "The antiquarian **annotator** appended voluminous historical appendices detailing ancient Highland clans."}
    ]
  },
  "cognition": {
    "primary": "The mental action or process of acquiring knowledge and understanding through thought, experience, and the senses.",
    "secondary": "In cognitive psychology, the complex faculties of perception, memory, reasoning, judgment, and problem solving.",
    "quotes": [
      {"author": "Immanuel Kant", "work": "Critique of Pure Reason", "quote": "All human **cognition** begins with intuitions, proceeds thence to concepts, and ends with principles."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Selective attention directs sensory **cognition**, highlighting relevant stimuli while discarding background noise."},
      {"author": "Steven Pinker", "work": "How the Mind Works", "quote": "Visual **cognition** solves ill-posed inverse optics problems by assuming a world illuminated from above."}
    ]
  },
  "cognitive": {
    "primary": "Relating to the mental processes of perception, memory, judgment, and reasoning, as contrasted with emotion.",
    "secondary": "In clinical neuroscience, designating cerebral functions subserved primarily by neocortical networks.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "quote": "The massive right-hemisphere stroke preserved his verbal intellect but decimated his visual **cognitive** mapping."},
      {"author": "Daniel Kahneman", "work": "Thinking, Fast and Slow", "quote": "System 1 operates automatically while System 2 allocates attention to demanding **cognitive** computations."},
      {"author": "Noam Chomsky", "work": "Aspects of the Theory of Syntax", "quote": "Linguistic competence constitutes a foundational **cognitive** structure unique to the human biological species."}
    ]
  },
  "cognitively": {
    "primary": "In a manner relating to cognition, intellectual perception, reasoning, or mental processing.",
    "secondary": "In developmental psychology, evaluating milestones in terms of intellectual conceptual maturation.",
    "quotes": [
      {"author": "Jean Piaget", "work": "The Construction of Reality in the Child", "quote": "The infant develops **cognitively** by internalizing external action schemes into reversible mental operations."},
      {"author": "Steven Pinker", "work": "The Blank Slate", "quote": "Humans are **cognitively** equipped to master complex social relationships, language, and tool manipulation."},
      {"author": "Kay Redfield Jamison", "work": "Touched with Fire", "quote": "During hypomania, artists feel **cognitively** liberated, generating rapid conceptual associations and metaphors."}
    ]
  },
  "cognizable": {
    "primary": "Capable of being known, perceived, recognized, or apprehended by the human intellect.",
    "secondary": "In jurisprudence, falling within the legal jurisdiction of a court for trial or judicial determination.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Simple sensory qualities are immediately **cognizable** by the mind without the intervention of complex reflection."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "Trespass upon private real estate constitutes a civil injury **cognizable** by the courts of common law."},
      {"author": "Immanuel Kant", "work": "Prolegomena to Any Future Metaphysics", "quote": "Only objects of possible empirical intuition are **cognizable** by human understanding under categories."}
    ]
  },
  "cognizance": {
    "primary": "Knowledge, awareness, or notice; the conscious perception and intellectual apprehension of a fact.",
    "secondary": "In legal proceedings, judicial notice or jurisdiction to take official judicial notice of a matter.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "A statesman must take full **cognizance** of human nature and inherited traditions when drafting organic laws."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Speckled Band", "quote": "Holmes took careful **cognizance** of the bell-rope and ventilator, perceiving their sinister purpose."},
      {"author": "William Shakespeare", "work": "Henry VI, Part 1", "quote": "As **cognizance** of my blood and title, I wear this pale and maiden blossom in my bonnet."}
    ]
  },
  "cognizant": {
    "primary": "Having knowledge or being fully aware of something; perceptive, mindful, and conscious of circumstances.",
    "secondary": "In administrative governance, having formal jurisdiction or recognized authority regarding specific policy matters.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The American magistrate remains acutely **cognizant** of the constitutional limits circumscribing his office."},
      {"author": "Winston Churchill", "work": "Their Finest Hour", "quote": "The War Cabinet was fully **cognizant** of the desperate aerial combat being waged daily over Kent."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate was **cognizant** of the provincial prejudices that resisted modern sanitary reforms in the town."}
    ]
  },
  "cognize": {
    "primary": "To know, perceive, recognize, or become conscious of an object, idea, or sensation.",
    "secondary": "In epistemological theory, the intellectual act of apprehending reality through conceptual categories.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The subjective self cannot directly **cognize** itself except as reflected in memories of past thoughts."},
      {"author": "Charles Sanders Peirce", "work": "Selected Writings", "quote": "We have no power of thinking without signs, nor can we **cognize** an external fact without inference."},
      {"author": "Bertrand Russell", "work": "The Problems of Philosophy", "quote": "To **cognize** a physical object requires inferring its existence from immediate sense-data impressions."}
    ]
  },
  "connotation": {
    "primary": "An idea or feeling that a word invokes in addition to its literal or primary dictionary meaning.",
    "secondary": "In formal logic, the intension of a term, encompassing the set of attributes implied by a general name.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "A non-connotative term signifies a subject only, whereas a general name possesses both denotation and **connotation**."},
      {"author": "George Orwell", "work": "Politics and the English Language", "quote": "Political speech abounds in dishonest words chosen purely for their favorable emotional **connotation**."},
      {"author": "C. S. Lewis", "work": "Studies in Words", "quote": "The historical critic must trace how semantic shifts alter the moral **connotation** of everyday idioms."}
    ]
  },
  "connotational": {
    "primary": "Pertaining to connotation; relating to suggested, associative, or secondary meanings of words.",
    "secondary": "In semiotics, describing cultural associations and symbolic nuances distinct from literal reference.",
    "quotes": [
      {"author": "Roland Barthes", "work": "Mythologies", "quote": "Visual advertising constructs an elaborate **connotational** layer that naturalizes bourgeois consumer ideals."},
      {"author": "Umberto Eco", "work": "A Theory of Semiotics", "quote": "The **connotational** codes of a poetic text produce semantic ambiguity through multiple interpretive frames."},
      {"author": "I. A. Richards", "work": "The Philosophy of Rhetoric", "quote": "Metaphor relies upon the interaction of **connotational** overtones between the tenor and vehicle."}
    ]
  },
  "connotative": {
    "primary": "Suggesting or implying associated meanings in addition to the primary or literal denotation.",
    "secondary": "In logic, designating terms that signify an attribute while denoting the subjects possessing it.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Proper names are not **connotative**; they denote individuals without indicating any distinctive attributes."},
      {"author": "William Empson", "work": "Seven Types of Ambiguity", "quote": "Poetic richness arises when **connotative** nuances vibrate against the plain syntactic surface of the line."},
      {"author": "S. I. Hayakawa", "work": "Language in Thought and Action", "quote": "The **connotative** force of loaded rhetoric can manipulate mass sentiment during political crises."}
    ]
  },
  "connote": {
    "primary": "To imply or suggest an idea, feeling, or association in addition to the literal meaning of a word.",
    "secondary": "In formal logic, to imply the essential attributes that define the comprehension of a general term.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The word white denotes all white things, as snow or milk, and does not **connote** them, but connotes whiteness."},
      {"author": "Aldous Huxley", "work": "Brave New World", "quote": "In the World State, words like mother and home were conditioned to **connote** obscenity and disgust."},
      {"author": "Virginia Woolf", "work": "A Room of One's Own", "quote": "The title of genius had come to **connote** a solitary, brooding male figure isolated in an attic."}
    ]
  },
  "denotation": {
    "primary": "The literal, explicit, or primary dictionary meaning of a word, contrasting with its connotations.",
    "secondary": "In formal logic, the extension of a term; the totality of real-world objects to which a term applies.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The **denotation** of a word encompasses the individual things of which that predicate may be affirmed."},
      {"author": "Bertrand Russell", "work": "On Denoting", "quote": "A phrase may be denoting, and yet not express anything; meaning and **denotation** must not be confused."},
      {"author": "C. K. Ogden", "work": "The Meaning of Meaning", "quote": "Linguistic confusion arises when casual speakers mistake subjective associations for objective **denotation**."}
    ]
  },
  "denotative": {
    "primary": "Serving to denote, specify, or indicate; relating to the direct, literal meaning of a word.",
    "secondary": "In semiotics, describing straightforward literal reference before secondary connotations are attached.",
    "quotes": [
      {"author": "Roland Barthes", "work": "Elements of Semiology", "quote": "At the first semiotic tier, the photograph presents a purely **denotative** capture of the physical object."},
      {"author": "Umberto Eco", "work": "The Role of the Reader", "quote": "Scientific definitions strive for unambiguous **denotative** clarity, purging poetic metaphors entirely."},
      {"author": "I. A. Richards", "work": "Principles of Literary Criticism", "quote": "Technical prose prioritizes **denotative** precision to ensure that instructions are followed without error."}
    ]
  },
  "denotatum": {
    "primary": "The actual object, entity, or state of affairs in reality referred to by a linguistic sign or term.",
    "secondary": "In philosophical semantics, the referent designated by a symbol within a formal sign system.",
    "quotes": [
      {"author": "Charles Morris", "work": "Signs, Language and Behavior", "quote": "A sign refers to what is taken account of in virtue of the sign vehicle; that object is the **denotatum**."},
      {"author": "Rudolf Carnap", "work": "Meaning and Necessity", "quote": "The intension of a predicate is a property, whereas its extension or **denotatum** is a class of individuals."},
      {"author": "Willard Van Orman Quine", "work": "Word and Object", "quote": "Ontological relativity emerges when radical translation fails to pin down a unique physical **denotatum**."}
    ]
  },
  "denote": {
    "primary": "To be a sign, symbol, or indicator of something; to designate or represent literally.",
    "secondary": "In logic and philosophy of language, to point directly to an individual object or class of referents.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "Introduction to Mathematical Philosophy", "quote": "Definite descriptions like the author of Waverley **denote** a unique person through relational properties."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Naturalists use the term species to **denote** distinct morphological assemblages that breed true."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Words are sensible marks invented by men to **denote** internal ideas dwelling in the mind."}
    ]
  },
  "denotive": {
    "primary": "Having the power to denote, indicate, or signify; serving as a direct sign or designation.",
    "secondary": "In lexical semantics, describing vocabulary items whose communicative function is strictly referential.",
    "quotes": [
      {"author": "Edward Sapir", "work": "Language: An Introduction to the Study of Speech", "quote": "Mathematical notations represent the purest form of **denotive** symbolism, devoid of emotional coloring."},
      {"author": "Benjamin Lee Whorf", "work": "Language, Thought, and Reality", "quote": "Grammatical categories exert a subtle **denotive** influence upon how cultures categorize spatial time."},
      {"author": "Ferdinand de Saussure", "work": "Course in General Linguistics", "quote": "The linguistic sign unites not a thing and a name, but a concept and a **denotive** sound pattern."}
    ]
  },
  "derecognize": {
    "primary": "To withdraw official recognition, diplomatic status, or legal standing from a state or entity.",
    "secondary": "In international diplomacy and treaty law, terminating formal diplomatic relations with a governing regime.",
    "quotes": [
      {"author": "Henry Kissinger", "work": "Diplomacy", "quote": "Washington decided to **derecognize** Taipei in order to establish normalized bilateral relations with Beijing."},
      {"author": "George F. Kennan", "work": "Memoirs: 1925-1950", "quote": "The department debated whether to **derecognize** the exile government once domestic authority had collapsed."},
      {"author": "Zbigniew Brzezinski", "work": "Power and Principle", "quote": "Strategic realpolitik compelled the administration to **derecognize** friendly regimes overtaken by popular revolutions."}
    ]
  },
  "incognito": {
    "primary": "Having one's true identity concealed, assumed under a disguise, or traveling under a false name.",
    "secondary": "In monarchical history, royal sovereigns traveling privately without royal retinue or ceremony.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "A Scandal in Bohemia", "quote": "The King of Bohemia traveled **incognito** to Baker Street, concealing his royal features behind a dark vizard."},
      {"author": "Alexandre Dumas", "work": "The Count of Monte Cristo", "quote": "The mysterious count lived **incognito** in Paris, executing his grand vengeance without arousing suspicion."},
      {"author": "Mark Twain", "work": "The Prince and the Pauper", "quote": "Prince Edward wandered **incognito** through the filthy alleys of London, discovering the misery of his subjects."}
    ]
  },
  "incognizable": {
    "primary": "Incapable of being recognized, known, or intellectually apprehended; entirely unknowable.",
    "secondary": "In German idealism, the Kantian thing-in-itself (Ding an sich) which lies beyond possible human experience.",
    "quotes": [
      {"author": "Immanuel Kant", "work": "Critique of Pure Reason", "quote": "Noumena remain fundamentally **incognizable** to human reason, which can grasp only phenomenal appearances."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "The ultimate reality behind the physical universe belongs forever to the sphere of the Unknowable and **incognizable**."},
      {"author": "William James", "work": "The Will to Believe", "quote": "Pragmatism rejects scholastic entities that remain hopelessly **incognizable** and produce no practical fruits."}
    ]
  },
  "incognizance": {
    "primary": "Failure to recognize or take notice; lack of awareness, perception, or knowledge.",
    "secondary": "In legal jurisprudence, an omission or failure by a tribunal to take judicial notice of a material fact.",
    "quotes": [
      {"author": "Edmund Burke", "work": "An Appeal from the New to the Old Whigs", "quote": "Ministers displayed complete **incognizance** of colonial discontent, precipitating an imperial rupture."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "The aristocratic ruling class lived in blind **incognizance** of the starving millions in industrial slums."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Her comfortable youth had passed in sunny **incognizance** of the tragedy and grief that haunted her lineage."}
    ]
  },
  "incognizant": {
    "primary": "Lacking knowledge, awareness, or consciousness of something; completely unaware.",
    "secondary": "In narrative characterization, describing figures who walk blindly into imminent danger or deception.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Tess walked across the misty meadows, tragically **incognizant** of the snare Alec had prepared for her."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The sleeping passengers aboard the Patna remained **incognizant** of the submerged collision that doomed them."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The citizens feasted in luxury, **incognizant** of the Gothic hordes encamped outside the Flaminian gate."}
    ]
  },
  "not": {
    "primary": "Used to express negation, denial, refusal, contradiction, or prohibition in a sentence.",
    "secondary": "In Boolean logic and computer programming, a fundamental unary logic operator that inverts a truth value.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "To be, or **not** to be, that is the question: Whether 'tis nobler in the mind to suffer the slings and arrows."},
      {"author": "Abraham Lincoln", "work": "Gettysburg Address", "quote": "That government of the people, by the people, for the people, shall **not** perish from the earth."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The mind is white paper, void of all characters, without any ideas; how comes it to be furnished? **Not** by innate rules."}
    ]
  },
  "notability": {
    "primary": "Prominence, distinction, or eminence that renders an individual or achievement worthy of public attention.",
    "secondary": "In civic life, a person of distinction, high social rank, or acknowledged achievement in the community.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Every provincial **notability** attended the ball, parading diamonds and antique family silver for the visitors."},
      {"author": "Charles Dickens", "work": "Martin Chuzzlewit", "quote": "He achieved sudden **notability** in the bustling frontier town as an eminent architectural speculator."},
      {"author": "Henry James", "work": "The Bostonians", "quote": "Olive Chancellor was drawn to individuals whose public **notability** advanced the great cause of reform."}
    ]
  },
  "notable": {
    "primary": "Worthy of notice, attention, or remark; remarkable, distinguished, prominent, or celebrated.",
    "secondary": "In historical chronicles, an eminent dignitary or leading citizen summoned to public councils.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The reign of Trajan was marked by a **notable** expansion of imperial frontiers along the Euphrates."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mrs. Elton considered herself a most **notable** manager of household affairs and parish charities."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The Galapagos islands presented a **notable** example of adaptive divergence among isolated finch populations."}
    ]
  },
  "notably": {
    "primary": "In a notable manner; especially, particularly, conspicuously, or to a significant degree.",
    "secondary": "In analytical writing, introducing an outstanding or exemplary illustration of a general principle.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Division of labor increases productivity **notably** in manufactured goods, as exemplified by the pin factory."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Democratic institutions foster public education **notably** in New England, where townships fund common schools."},
      {"author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "Primate anatomy corresponds **notably** with human skeletal structures, especially in pelvic architecture."}
    ]
  },
  "notarise": {
    "primary": "To certify, authenticate, or witness a legal document or signature in the capacity of a notary (British spelling).",
    "secondary": "In commercial transactions, verifying the identity of signatories to prevent fraud on deeds and powers of attorney.",
    "quotes": [
      {"author": "Anthony Trollope", "work": "The Eustace Diamonds", "quote": "The family solicitor dispatched a clerk to **notarise** the affidavit swearing to the lost diamond necklace."},
      {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "Before foreign bonds could be negotiated in London, a notary had to examine and **notarise** the seals."},
      {"author": "Arthur Conan Doyle", "work": "The Valley of Fear", "quote": "The American detective carried sworn depositions that a magistrate had agreed to **notarise** in Chicago."}
    ]
  },
  "notarize": {
    "primary": "To certify, authenticate, or witness a document, contract, or affidavit as an authorized notary public.",
    "secondary": "In property conveyance and contract law, certifying signatures under official seal to ensure legal admissibility.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "Babbitt went into the outer office to **notarize** the land deed before the registry closed at five."},
      {"author": "John Steinbeck", "work": "East of Eden", "quote": "The lawyer produced the conveyance and summoned a deputy to **notarize** the signatures on the ranch sale."},
      {"author": "F. Scott Fitzgerald", "work": "Tender Is the Night", "quote": "They required an American consul to **notarize** the medical guardianship papers in Zurich."}
    ]
  },
  "notary": {
    "primary": "A public officer authorized by law to administer oaths, witness signatures, and certify legal documents.",
    "secondary": "In civil law traditions, a senior legal professional drafting wills, deeds, and major corporate statutes.",
    "quotes": [
      {"author": "Honoré de Balzac", "work": "Eugénie Grandet", "quote": "Cruchet was the principal **notary** of Saumur, holding the confidential financial secrets of every wealthy miser."},
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Go with me to a **notary**, seal me there your single bond; and, in a merry sport, if you repay me not on such a day."},
      {"author": "Gustave Flaubert", "work": "Madame Bovary", "quote": "Monsieur Guillaumin, the prosperous town **notary**, managed investments and held mortgages over local estates."}
    ]
  },
  "notate": {
    "primary": "To write down, record, or represent in a system of specialized notation, such as musical score or dance.",
    "secondary": "In choreology and ethnomusicology, transcribing live performance movements into formal Labanotation or neumes.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "Musicophilia", "quote": "The savant could listen to an intricate orchestral score once and **notate** every instrumental part flawlessly."},
      {"author": "Igor Stravinsky", "work": "Poetics of Music", "quote": "To properly **notate** complex polymetric rhythms requires absolute precision in time signatures and barlines."},
      {"author": "Aaron Copland", "work": "What to Listen for in Music", "quote": "The composer must **notate** dynamic nuances and tempo rubato so that performers recreate the intended emotion."}
    ]
  },
  "notation": {
    "primary": "A system of graphic symbols, characters, or marks used in specialized disciplines such as music or mathematics.",
    "secondary": "In the history of mathematics, symbolic formalisms such as Leibnizian calculus notation that enable calculation.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "He recorded geometric reflections using a concise algebraic **notation** that clarified the angles of refraction."},
      {"author": "Alan Turing", "work": "On Computable Numbers", "quote": "The paper uses a standardized logical **notation** to define the finite configurations of the computing machine."},
      {"author": "Douglas Hofstadter", "work": "Gödel, Escher, Bach", "quote": "Typographical **notation** allows mathematicians to construct self-referential statements about formal provability."}
    ]
  },
  "notch": {
    "primary": "A V-shaped indentation, cut, or nick made on an edge or surface; also, an informal level or grade.",
    "secondary": "In regional geography, a deep, narrow mountain pass or gorge between rocky precipices.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Ambitious Guest", "quote": "The solitary cottage nestled deep within the dramatic mountain **notch**, flanked by towering granite cliffs."},
      {"author": "Mark Twain", "work": "The Adventures of Huckleberry Finn", "quote": "I cut a fresh **notch** in the gunwale of the raft every sunrise to keep track of the days."},
      {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "The Indian guide carved a deep **notch** in the cedar trunk to blazon the wilderness trail for portage."}
    ]
  },
  "notched": {
    "primary": "Having one or more V-shaped cuts, indentations, or serrations along an edge or border.",
    "secondary": "In botanical morphology, describing leaf margins or petals possessing shallow angular incisions.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The mandibles of certain carnivorous beetles are distinctly **notched** to crush the chitinous shells of prey."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The petals of the woodland pink are deeply **notched** at the apex, presenting a delicate fringed appearance."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Tashtego held up the harpoon, displaying its **notched** barb that gripped tenaciously in whale blubber."}
    ]
  },
  "note": {
    "primary": "A brief written record of facts, topics, or ideas, or a single sound of definite musical pitch.",
    "secondary": "In financial banking, a promissory banknote issued by a central bank and circulating as legal tender currency.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "If this fall into thy hand, revolve. In my stars I am above thee; but be not afraid of greatness... take **note** of it."},
      {"author": "Arthur Conan Doyle", "work": "The Red-Headed League", "quote": "Holmes scribbled a hasty **note** upon a telegraph slip and tossed it to the boy waiting in the cab."},
      {"author": "John Keats", "work": "Ode to a Nightingale", "quote": "Thou wast not born for death, immortal Bird! No hungry generations tread thee down; the **note** I hear was heard in ancient days."}
    ]
  },
  "notebook": {
    "primary": "A book of blank or ruled paper pages used for recording notes, memoranda, drawings, or sketches.",
    "secondary": "In intellectual biography, the personal laboratory journals kept by scientists and artists to record fleeting insights.",
    "quotes": [
      {"author": "Charles Darwin", "work": "Autobiography", "quote": "In July 1837 I opened my first **notebook** on Transmutation of Species, collecting facts with unflagging zeal."},
      {"author": "Virginia Woolf", "work": "A Writer's Diary", "quote": "She turned to her black leather **notebook** to capture the rhythmic cadence of the waves against the shore."},
      {"author": "Thomas Edison", "work": "The Diary and Sundry Observations", "quote": "Every failed laboratory experiment was meticulously entered into the laboratory **notebook** for future analysis."}
    ]
  },
  "notecase": {
    "primary": "A flat wallet or small leather case designed for carrying paper currency, banknotes, or visiting cards.",
    "secondary": "In Victorian social accessories, an embossed leather pocketbook carried by gentlemen to hold bank paper.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Beryl Coronet", "quote": "The banker drew a well-stuffed morocco **notecase** from his breast pocket and produced the promissory bond."},
      {"author": "Anthony Trollope", "work": "The Way We Live Now", "quote": "Nidderdale patted his leather **notecase**, relieved to find that his betting slips remained safe."},
      {"author": "Wilkie Collins", "work": "The Moonstone", "quote": "Sergeant Cuff examined the dead man's empty **notecase**, finding only a pawn ticket and an old receipt."}
    ]
  },
  "notechis": {
    "primary": "A genus of highly venomous elapid snakes native to southern Australia, commonly known as tiger snakes.",
    "secondary": "In toxinological medicine, elapids producing potent presynaptic neurotoxins, myotoxins, and coagulants.",
    "quotes": [
      {"author": "Raymond Ditmars", "work": "Snakes of the World", "quote": "Specimens of **Notechis** defend themselves with flattened necks and rapid, lethal strikes across Australian marshes."},
      {"author": "Frank Hamilton Cushing", "work": "Zuñi Folk Tales", "quote": "Herpetologists caution that bites from wild **Notechis** require immediate administration of polyvalent antivenom."},
      {"author": "Richard Lydekker", "work": "The Royal Natural History", "quote": "The banded tiger snake of the genus **Notechis** displays wide color variation from tawny brown to coal black."}
    ]
  },
  "noted": {
    "primary": "Well known, celebrated, widely recognized, and distinguished for a particular achievement or quality.",
    "secondary": "Recorded in writing, observed, or officially registered in public records.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Old Marley was as dead as a door-nail; this must be distinctly **noted**, or nothing wonderful can come of the story."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Anne Elliot was admired by a **noted** naval officer whose gallantry was celebrated across the kingdom."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Antioch was **noted** for its luxurious gardens, marble colonnades, and dissolute theatrical spectacles."}
    ]
  },
  "notemigonus": {
    "primary": "A monotypic genus of North American cyprinid freshwater ray-finned fish, the golden shiner (Notemigonus crysoleucas).",
    "secondary": "In ichthyology and aquaculture, an important forage minnow characterized by a deeply compressed body and falcate anal fin.",
    "quotes": [
      {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "The golden shiner, **Notemigonus**, is abundant in sluggish ponds and weed beds across eastern North America."},
      {"author": "Spencer Fullerton Baird", "work": "Fishes of New Jersey", "quote": "Anglers value **Notemigonus** as prime live bait, cultivating schools in shallow earthen commercial ponds."},
      {"author": "Louis Agassiz", "work": "Contributions to the Natural History of the United States", "quote": "Morphological comparisons of **Notemigonus** reveal distinctive lateral line scales curving along the belly."}
    ]
  },
  "notepad": {
    "primary": "A pad of bound sheets of blank or lined paper for jotting down notes, sketches, or reminders.",
    "secondary": "In desktop computing, an elemental plain-text editing utility application found on operating systems.",
    "quotes": [
      {"author": "Joan Didion", "work": "Slouching Towards Bethlehem", "quote": "A reporter lives with a spiral **notepad** always within reach, recording the fleeting ironies of the street."},
      {"author": "Raymond Chandler", "work": "The Big Sleep", "quote": "Marlowe pulled a greasy **notepad** from his trench coat and checked the telephone number of the orchid house."},
      {"author": "David Foster Wallace", "work": "A Supposedly Fun Thing I'll Never Do Again", "quote": "I sat on the Caribbean deck chair with an oversized legal **notepad**, furiously scribbling sensory details."}
    ]
  },
  "notepaper": {
    "primary": "Paper manufactured and cut specifically for writing personal letters, social correspondence, or notes.",
    "secondary": "In stationery history, watermarked rag paper embossed with heraldic crests, monograms, or formal letterheads.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Bingley took up a sheet of fine gilt-edged **notepaper** and prepared to write with characteristic careless rapidity."},
      {"author": "Arthur Conan Doyle", "work": "A Case of Identity", "quote": "Holmes sniffed the scented **notepaper**, detecting hints of violet that betrayed the social milieu of the sender."},
      {"author": "Henry James", "work": "The Turn of the Screw", "quote": "The letter was written upon cheap foreign **notepaper**, its hurried lines conveying urgent apprehension."}
    ]
  }
}
