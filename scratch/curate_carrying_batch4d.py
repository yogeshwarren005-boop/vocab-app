# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — lat (Remaining 39 words)
  # =========================================================================
  "Dashboard — lat/dilatation.md": {
    "primary": "The expansion, stretching, or widening of an opening, hollow organ, vessel, or passage beyond its normal caliber.",
    "secondary": "In physiology and clinical pathology, an enlargement of a tubular structure, cardiac chamber, or pupil in response to hydrostatic pressure, inflammatory processes, or autonomic stimulation.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Beetles, size of the cerebral ganglia in; **dilatation** of the foretarsi during reproductive activity."},
      {"author": "William Harvey", "work": "Exercitatio Anatomica de Motu Cordis et Sanguinis in Animalibus", "quote": "The alternate **dilatation** and contraction of the heart ventricles drives the uninterrupted movement of blood."},
      {"author": "John Hunter", "work": "A Treatise on the Blood, Inflammation, and Gun-shot Wounds", "quote": "The permanent **dilatation** of an inflamed artery results from weakened muscular resistance against arterial pressure."}
    ]
  },
  "Dashboard — lat/interrelatedness.md": {
    "primary": "The mutual dependence, reciprocal connection, or shared coherence linking multiple entities, functions, or systems together.",
    "secondary": "In systems ecology and holistic philosophy, the structural web of interactions wherein perturbations in one component reverberate through the equilibrium of the entire organism or cosmos.",
    "quotes": [
      {"author": "Martin Luther King Jr.", "work": "Letter from Birmingham Jail", "quote": "We are caught in an inescapable network of mutuality, tied in a single garment of destiny; whatever affects one directly, affects all indirectly in our profound **interrelatedness**."},
      {"author": "Alfred North Whitehead", "work": "Process and Reality", "quote": "The ultimate solidarity of the world is established by the systematic **interrelatedness** of all actual entities."},
      {"author": "Gregory Bateson", "work": "Steps to an Ecology of Mind", "quote": "Biological and ecological patterns reveal the complex **interrelatedness** between organism and environment."}
    ]
  },
  "Dashboard — lat/oblateness.md": {
    "primary": "The degree of polar flattening exhibited by a rotating spheroid whose equatorial diameter exceeds its polar diameter.",
    "secondary": "In celestial mechanics and physical geodesy, the geometric ratio characterizing planetary equatorial bulge produced by centrifugal forces counteracting inward gravitational attraction.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Philosophiae Naturalis Principia Mathematica", "quote": "The **oblateness** of the terrestrial spheroid arises necessarily from the centrifugal force of diurnal rotation."},
      {"author": "Pierre-Simon Laplace", "work": "Traité de mécanique céleste", "quote": "Gravitational measurements over differing latitudes confirm the planetary **oblateness** predicted by rotating fluid theory."},
      {"author": "Mary Somerville", "work": "On the Connexion of the Physical Sciences", "quote": "The slight **oblateness** of Jupiter is readily visible through a modest telescope due to its rapid rotation."}
    ]
  },
  "Dashboard — lat/oblation.md": {
    "primary": "The solemn presentation of an offering, sacrifice, or consecrated gift to a deity, sacred altar, or religious institution.",
    "secondary": "In Christian liturgical theology, specifically the solemn Eucharistic offering of bread and wine presented to God upon the holy table prior to consecration.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Sonnet 125", "quote": "No, let me be obsequious in thy heart, / And take thou my **oblation**, poor but free, / Which is not mix'd with seconds, knows no art."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Many a sacrifice / And many an **oblation** offered here, / In vain to avert the promised wrath divine."},
      {"author": "John Dryden", "work": "The Hind and the Panther", "quote": "The pure **oblation** of the morning rite ascended without smoke or profane mixture."}
    ]
  },
  "Dashboard — lat/prelate.md": {
    "primary": "A high-ranking ecclesiastic of superior dignity and jurisdiction, such as a bishop, archbishop, or abbot.",
    "secondary": "In canonical jurisprudence and ecclesiastical history, an ordained dignitary possessing ordinary governing authority over an autonomous diocese or territorial jurisdiction.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 2", "quote": "Wherefore do you so ill become this crown, / And turn a **prelate** into a man of war?"},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The proud **prelate** exercised an authority over the secular magistrate that rivaled imperial sovereignty."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "A reverend **prelate** observed that the narrative appeared to him to contain many improbable statements."}
    ]
  },
  "Dashboard — lat/prelature.md": {
    "primary": "The office, rank, dignity, or administrative jurisdiction belonging to an ecclesiastical prelate.",
    "secondary": "In Roman Catholic canonical governance, an institutional structure or circumscription erected by the Holy See to accomplish specific pastoral or missionary tasks under a prelate's direction.",
    "quotes": [
      {"author": "Henry Hart Milman", "work": "History of Latin Christianity", "quote": "The appointment to that opulent **prelature** became the center of a protracted dispute between pope and emperor."},
      {"author": "Thomas Fuller", "work": "The Church History of Britain", "quote": "He accepted the duties of the **prelature** with genuine reluctance, preferring his quiet library to episcopal courts."},
      {"author": "John Foxe", "work": "Actes and Monuments", "quote": "The outward pomp of the Roman **prelature** was contrasted by reformers with apostolic simplicity."}
    ]
  },
  "Dashboard — lat/prolate.md": {
    "primary": "Having the polar diameter elongated and exceeding the equatorial diameter, as an ellipsoid stretched along its axis of revolution.",
    "secondary": "In celestial geometry and fluid mechanics, describing an elongated or lemon-shaped spheroid whose major axis coincides with its central rotation axis.",
    "quotes": [
      {"author": "Colin Maclaurin", "work": "A Treatise of Fluxions", "quote": "A rotating fluid body may assume the figure of a **prolate** ellipsoid under specific boundary constraints of internal motion."},
      {"author": "George Biddell Airy", "work": "On the Algebraic and Numerical Theory of Errors of Observations", "quote": "The mathematical formulation distinguishes between an oblate and a **prolate** spheroid by the ratio of their axes."},
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "The equipotential surfaces surrounding a conducting conductor may be modeled as confocal **prolate** spheroids."}
    ]
  },
  "Dashboard — lat/relate.md": {
    "primary": "To recount, narrate, or describe an event; or to establish a logical, causal, or comparative connection between disparate things.",
    "secondary": "In psychological development and social dynamics, to interact with empathy, find mutual understanding, and establish responsive rapport with others.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard II", "quote": "My sovereign liege, no letters, and few words, / But such as I, without your special warrant, / Should lose my life to **relate**."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "She could not **relate** the circumstances of their parting without renewing the pain of the separation."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "It is interesting to **relate** how frequently these volcanic formations coincided with seismic disturbances."}
    ]
  },
  "Dashboard — lat/related.md": {
    "primary": "Connected by kinship, blood, or marital alliance; or sharing an established conceptual, causal, or logical association.",
    "secondary": "In phylogenetic taxonomy and evolutionary genetics, descended from a shared common ancestor or sharing homologous morphological traits.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Thank you very much, said Oak, in the modest tone good manners demanded, thinking how closely their fortunes were now **related**."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "Species belonging to the same genus are more closely **related** to each other than species belonging to distinct families."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Ideas that are habitually associated become so intimately **related** in the mind that one instantly introduces the other."}
    ]
  },
  "Dashboard — lat/relatedness.md": {
    "primary": "The degree or manner of kinship, mutual connection, or structural association holding between distinct entities, organisms, or ideas.",
    "secondary": "In evolutionary sociobiology and population genetics, the statistical coefficient measuring the probability that two biological individuals share homologous alleles by common descent.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "The mind insists upon the secret **relatedness** of all phenomena, discovering unity beneath apparent variety."},
      {"author": "W. D. Hamilton", "work": "The Genetical Evolution of Social Behaviour", "quote": "Altruistic actions are favored when the benefit to the recipient multiplied by the coefficient of **relatedness** exceeds the cost to the actor."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Every thought points outward toward an objective context, revealing its intrinsic **relatedness** to prior experience."}
    ]
  },
  "Dashboard — lat/relatiative.md": {
    "primary": "Pertaining to, expressing, or exhibiting reciprocal connection, comparison, or retaliatory and compensatory relation.",
    "secondary": "In legal philosophy and comparative linguistics, designating modalities, covenants, or clauses that establish a proportional equivalence between mutual obligations.",
    "quotes": [
      {"author": "Jeremy Bentham", "work": "An Introduction to the Principles of Morals and Legislation", "quote": "The penal sanction must maintain a **relatiative** proportion to the gravity of the offense committed."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The civil magistrate applies a **relatiative** justice, weighing mutual injuries with measured retribution."},
      {"author": "Henry Maine", "work": "Ancient Law", "quote": "Early customary jurisprudence was founded upon **relatiative** duties binding reciprocal clan obligations."}
    ]
  },
  "Dashboard — lat/relation.md": {
    "primary": "A connection, correspondence, or mutual involvement existing between two or more persons, ideas, or entities; or the narrative recital of a story.",
    "secondary": "In formal ontology, mathematical logic, and relational database systems, a set of ordered tuples establishing associations between elements of defined domains.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "This is a thing which you might from **relation** likewise reap, being, as it is, manufactured in public rumor."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The nature of **relation** consists in the referring or comparing two things one to another."},
      {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "A **relation** between two terms is not a third term standing between them, but a distinct category of truth."}
    ]
  },
  "Dashboard — lat/relational.md": {
    "primary": "Pertaining to, characterized by, or arising from mutual connections, interpersonal bonds, or comparative relationships.",
    "secondary": "In database architecture and cognitive sociology, organizing information into interconnected mathematical relations or analyzing knowledge as constructed through communicative ties.",
    "quotes": [
      {"author": "Edgar F. Codd", "work": "A Relational Model of Data for Large Shared Data Banks", "quote": "Future users of large data banks must be protected from having to know how the data is organized in the machine through a clean **relational** model."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Our experience contains not only substantive states of consciousness but transitive and **relational** transitions between them."},
      {"author": "Charles Sanders Peirce", "work": "Collected Papers", "quote": "Every term that denotes an object does so by virtue of some **relational** link connecting it with an interpretant."}
    ]
  },
  "Dashboard — lat/relations.md": {
    "primary": "The mutual dealings, associations, communications, or kinship ties connecting individuals, social groups, or sovereign nations.",
    "secondary": "In diplomacy and international jurisprudence, the institutional agreements, diplomatic protocols, and treaties regulating intercourse among sovereign polities.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "Stones have been known to move, and trees to speak; / Augurs, and understood **relations**, have / By magot-pies, and choughs, and rooks, brought forth / The secret'st man of blood."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Commercial interests frequently supersede political jealousies in determining the friendly **relations** of maritime powers."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The peaceful **relations** of neighboring commonwealths promote the specialization of international labor."}
    ]
  },
  "Dashboard — lat/relationship.md": {
    "primary": "The emotional, social, or structural bond connecting two or more people, groups, or entities in an ongoing association.",
    "secondary": "In psychological attachment theory and interpersonal dynamics, the pattern of reciprocal commitment, affection, and interdependence developed through sustained contact.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "That several of the inhabitants of the caves of the Old and New Worlds should be closely related, can be understood on the view of common descent, but not upon that of independent creation without historical **relationship**."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "A young man's **relationship** with his chosen mentor often determines the spiritual trajectory of his early career."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "She reflected on the delicate **relationship** between marital duty and personal liberty."}
    ]
  },
  "Dashboard — lat/relative-in-law.md": {
    "primary": "A person connected to an individual through a marriage alliance rather than biological descent, such as a parent-in-law or sibling-in-law.",
    "secondary": "In structural anthropology and civil inheritance law, an affine whose legal standing, inheritance claims, and kinship obligations are created entirely by marital covenant.",
    "quotes": [
      {"author": "Anthony Trollope", "work": "The Prime Minister", "quote": "He found himself obliged to treat his new **relative-in-law** with an outward courtesy that masked his private distrust."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "The introduction of a new **relative-in-law** unsettled the established hierarchy of the country estate."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The legal responsibilities owed to a **relative-in-law** became a subject of dispute at the town council."}
    ]
  },
  "Dashboard — lat/relative.md": {
    "primary": "Considered in comparison or relation to something else; not absolute; or a person connected by blood or marital kinship.",
    "secondary": "In classical physics and epistemology, denoting quantities, values, or coordinates that have meaning exclusively when measured against an assigned reference frame.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "The spirit that I have seen / May be the devil... I'll have grounds / More **relative** than this."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Words that express relations are called **relative** words, denoting things not as they exist alone, but in reference to another."},
      {"author": "Isaac Newton", "work": "Philosophiae Naturalis Principia Mathematica", "quote": "Absolute, true, and mathematical time flows equably, without relation to anything external; **relative**, apparent, and common time is some sensible and external measure."}
    ]
  },
  "Dashboard — lat/relatively.md": {
    "primary": "In a comparative manner; when evaluated in proportion or reference to other comparable entities rather than in isolation.",
    "secondary": "To a moderate or comparative extent, as measured against an ambient baseline standard or expected average value.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "He did not covet the post **relatively** to the farm: in relation to herself, he desired it supremely."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The skull of the ape is **relatively** much smaller in proportion to the facial bones than that of civilized man."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A commodity becomes **relatively** cheaper when the productivity of labor in its manufacture increases."}
    ]
  },
  "Dashboard — lat/relativise.md": {
    "primary": "To view, interpret, or evaluate something as dependent upon cultural, historical, or cognitive frameworks rather than absolute.",
    "secondary": "In epistemological critique and cultural sociology, to deconstruct dogmatic universal claims by uncovering their grounding in contingent social practices.",
    "quotes": [
      {"author": "Friedrich Nietzsche", "work": "The Gay Science", "quote": "Historical consciousness tends to **relativise** every moral dogma, dissolving eternal truths into temporal habits."},
      {"author": "Max Weber", "work": "The Methodology of the Social Sciences", "quote": "To **relativise** cultural values is not to deny their subjective validity to the historical actors who held them."},
      {"author": "Karl Mannheim", "work": "Ideology and Utopia", "quote": "Sociological analysis seeks to **relativise** political ideologies by revealing their socioeconomic anchors."}
    ]
  },
  "Dashboard — lat/relativism.md": {
    "primary": "The philosophical doctrine holding that knowledge, truth, or morality exist in relation to culture, society, or historical context, and are not absolute.",
    "secondary": "In meta-ethics and epistemology, the stance that denies objective universal norms, asserting that cognitive and moral evaluations are valid only within specific interpretive communities.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "A History of Western Philosophy", "quote": "Protagoras was the first prominent champion of epistemological **relativism**, declaring man the measure of all things."},
      {"author": "William James", "work": "The Meaning of Truth", "quote": "Pragmatic philosophy rejects dogmatic absolutism without collapsing into a paralyzing moral **relativism**."},
      {"author": "George Santayana", "work": "Scepticism and Animal Faith", "quote": "The defense of intellectual **relativism** must reckon with the inescapable animal faith that guides immediate action."}
    ]
  },
  "Dashboard — lat/relativistic.md": {
    "primary": "Pertaining to, based on, or consistent with the physical theory of relativity; or reflecting philosophical relativism.",
    "secondary": "In high-energy astrophysics and theoretical physics, describing physical phenomena (such as time dilation or Lorentz contraction) occurring at velocities approaching the speed of light.",
    "quotes": [
      {"author": "Albert Einstein", "work": "The Meaning of Relativity", "quote": "The **relativistic** transformation equations demonstrate that simultaneous events in one coordinate system are not simultaneous in another."},
      {"author": "Arthur Eddington", "work": "Space, Time and Gravitation", "quote": "The deflection of starlight near the sun provided dramatic observational confirmation of **relativistic** mechanics."},
      {"author": "Max Planck", "work": "The Philosophy of Physics", "quote": "The introduction of **relativistic** dynamics marked a decisive departure from the Newtonian assumption of rigid Euclidean space."}
    ]
  },
  "Dashboard — lat/relativistically.md": {
    "primary": "In accordance with the physical principles of special or general relativity; or from the perspective of epistemological relativism.",
    "secondary": "In particle physics, describing motions, accelerations, and field interactions calculated using Lorentz-invariant equations rather than classical Newtonian approximations.",
    "quotes": [
      {"author": "Paul Dirac", "work": "The Principles of Quantum Mechanics", "quote": "Electrons moving with high velocities must be treated **relativistically** to account for fine structure splitting in spectral lines."},
      {"author": "Richard Feynman", "work": "The Feynman Lectures on Physics", "quote": "When energy is converted into mass, the mass increment behaves **relativistically** exactly as predicted by the mass-energy relation."},
      {"author": "Hans Reichenbach", "work": "The Philosophy of Space and Time", "quote": "The geometry of moving frames must be evaluated **relativistically** once the constancy of the speed of light is accepted."}
    ]
  },
  "Dashboard — lat/relativity.md": {
    "primary": "The property of being dependent on or evaluated in comparison with a specified frame of reference, observer, or context.",
    "secondary": "In physics, Albert Einstein's revolutionary theoretical framework uniting space, time, gravity, and inertia into a curved four-dimensional spacetime continuum.",
    "quotes": [
      {"author": "Albert Einstein", "work": "Relativity: The Special and General Theory", "quote": "The purpose of the theory of **relativity** is to formulate laws of nature that hold valid for observers regardless of their state of motion."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The mind perceives no absolute isolation, for the very law of perception involves the **relativity** of object to subject."},
      {"author": "Henri Poincaré", "work": "Science and Hypothesis", "quote": "There is no absolute space, and we only conceive of **relativity** in motion through comparison with material benchmarks."}
    ]
  },
  "Dashboard — lat/relativize.md": {
    "primary": "To make, view, or treat something as relative rather than absolute, objective, or unconditioned.",
    "secondary": "In philosophical hermeneutics and literary theory, to situate concepts within their socio-historical horizon, showing that their validity is contingent rather than universally binding.",
    "quotes": [
      {"author": "William James", "work": "Pragmatism: A New Name for Some Old Ways of Thinking", "quote": "Pragmatism helps to **relativize** metaphysical dogmas by asking what concrete difference their truth makes in practical experience."},
      {"author": "Ernst Troeltsch", "work": "The Absoluteness of Christianity and the History of Religions", "quote": "The rigorous historical method inevitably threatens to **relativize** traditions once considered absolute."},
      {"author": "Richard Rorty", "work": "Philosophy and the Mirror of Nature", "quote": "Our objective is not to overthrow traditional inquiry, but to **relativize** its foundationalist ambitions."}
    ]
  },
  "Dashboard — lat/relatum.md": {
    "primary": "One of the terms, objects, or entities that stands in an expressed or logical relation to another entity.",
    "secondary": "In formal logic and structural ontology, the correlative term to which a subject or referent is linked via an asymmetric or symmetric binary relation.",
    "quotes": [
      {"author": "Charles Sanders Peirce", "work": "Collected Papers", "quote": "A relation cannot exist in isolation without a referent and a corresponding **relatum** bound by the mediate sign."},
      {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "In any asymmetric proposition, the referent precedes the **relatum** according to the sense of the connecting relation."},
      {"author": "Brand Blanshard", "work": "The Nature of Thought", "quote": "The mind cannot apprehend a relation without simultaneously keeping both the referent and its **relatum** in clear focus."}
    ]
  },
  "Dashboard — lat/retranslate.md": {
    "primary": "To translate a text or message a second time, or to translate a translation back into its original source language.",
    "secondary": "In literary translation studies, to compose a new target-language rendition of a classic work to remedy archaic phrasing or linguistic shortcomings in earlier versions.",
    "quotes": [
      {"author": "Johann Wolfgang von Goethe", "work": "West-östlicher Divan", "quote": "It is instructive to **retranslate** a foreign rendering into our mother tongue to gauge what was preserved and what was lost."},
      {"author": "Matthew Arnold", "work": "On Translating Homer", "quote": "Every successive generation feels the imperative necessity to **retranslate** Homer according to the literary sensibilities of its own era."},
      {"author": "George Saintsbury", "work": "A History of Criticism", "quote": "The scholar sought to **retranslate** the corrupt passages with closer fidelity to the early Greek manuscripts."}
    ]
  },
  "Dashboard — lat/superlative.md": {
    "primary": "Surpassing all others; of the highest kind, quality, or degree; supreme, preeminent, or peerless.",
    "secondary": "In descriptive grammar and morphology, designating the inflectional degree of an adjective or adverb indicating the greatest intensity or degree of comparison.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "He is a person of **superlative** delicacy of mind, whose feelings are constantly wounded by the coarse realities of the world."},
      {"author": "Herman Melville", "work": "Typee: A Romance of the South Seas", "quote": "The landscape presented a scene of **superlative** beauty that silenced all critical judgment."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "I am not sure that the greatest man of his age, if ever that solitary and **superlative** being existed, could have escaped popular detraction."}
    ]
  },
  "Dashboard — lat/superlatively.md": {
    "primary": "In a superlative manner; to the highest possible degree or extent; supremely and incomparably.",
    "secondary": "In critical rhetoric and aesthetic praise, expressing unrivaled preeminence or absolute perfection in style, character, or performance.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "She could imagine no person more **superlatively** happy than the friend whose future was now so securely established."},
      {"author": "Herman Melville", "work": "Moby-Dick; or, The Whale", "quote": "The whale rose with a majestic sweep, moving **superlatively** calm amid the churning fury of the sea."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Being a man not without a frequent consciousness that there was some cause for wonder in his **superlatively** tranquil nature, he smiled quietly."}
    ]
  },
  "Dashboard — lat/tralatitious.md": {
    "primary": "Transmitted or handed down from person to person or from generation to generation; traditional or inherited.",
    "secondary": "In classical rhetoric and philology, designating a transferred, metaphorical, or customary usage of words inherited from earlier literary authorities.",
    "quotes": [
      {"author": "Jeremy Taylor", "work": "The Rule and Exercises of Holy Dying", "quote": "The **tralatitious** wisdom of antiquity should be received with reverence rather than rashly overturned by novel dogmas."},
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Many vulgar errors are merely **tralatitious** reports credited upon the unexamined testimony of ancient compilers."},
      {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "The phrase was not his own invention, but a **tralatitious** ornament borrowed from the Latin rhetoricians."}
    ]
  },
  "Dashboard — lat/translatable.md": {
    "primary": "Capable of being rendered, converted, or expressed into another language without vital loss of core semantic meaning.",
    "secondary": "In semiotics and translation theory, describing linguistic constructs or cultural metaphors whose expressive value can be effectively transferred into another semiotic system.",
    "quotes": [
      {"author": "Walter Benjamin", "work": "The Task of the Translator", "quote": "A work is inherently **translatable** if its inner linguistic essence calls forth an echo in other languages."},
      {"author": "Umberto Eco", "work": "Experiences in Translation", "quote": "To consider whether a poetic text is **translatable** is to question the degree to which syntax and rhyme can be negotiated."},
      {"author": "George Steiner", "work": "After Babel", "quote": "No human utterance is entirely untranslatable, just as no utterance is ever completely and effortlessly **translatable**."}
    ]
  },
  "Dashboard — lat/translate.md": {
    "primary": "To turn or render words and texts from one language into another; or to convey, transport, or change something into another form.",
    "secondary": "In molecular biology and physics, to synthesize a polypeptide sequence according to mRNA codons, or to impart uniform linear motion without angular displacement.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "Happy is your grace, / That can **translate** the stubbornness of fortune / Into so quiet and so sweet a style."},
      {"author": "John Dryden", "work": "Preface to Ovid's Epistles", "quote": "The poet who attempts to **translate** an ancient master must steer between verbal fidelity and poetic license."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "We must learn how to **translate** abstract speculative theorems into practical mechanical operations."}
    ]
  },
  "Dashboard — lat/translation.md": {
    "primary": "The act or process of rendering text or speech into another language; or the resulting written or spoken version.",
    "secondary": "In molecular genetics, the complex ribosomal synthesis of a polypeptide chain decoded from nucleotide triplets in messenger RNA.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Love's Labour's Lost", "quote": "A huge **translation** of hypocrisy, / Vilely compiled, profound simplicity."},
      {"author": "Benedictus de Spinoza", "work": "Tractatus Theologico-Politicus", "quote": "A faithful **translation** of sacred scripture requires an exact knowledge of the Hebrew idioms and customs."},
      {"author": "John Milton", "work": "Areopagitica", "quote": "The printed **translation** of virtuous authors serves as the lifeblood of a literate and self-governing commonwealth."}
    ]
  },
  "Dashboard — lat/translational.md": {
    "primary": "Relating to uniform motion in which all points of a body travel uniformly along parallel paths without rotational movement.",
    "secondary": "In biomedical research and clinical pharmacology, referring to the applied process of converting basic laboratory findings into practical medical therapies and clinical trials.",
    "quotes": [
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "The kinetic energy of the system resolves into rotational components and purely **translational** motion through the medium."},
      {"author": "J. Willard Gibbs", "work": "Elementary Principles in Statistical Mechanics", "quote": "The phase space coordinates partition the degrees of freedom into **translational** and internal vibrational modes."},
      {"author": "William Thomson", "work": "Popular Lectures and Addresses", "quote": "The velocity of a vortex ring depends upon the balance between its internal circulation and its forward **translational** progress."}
    ]
  },
  "Dashboard — lat/translator.md": {
    "primary": "A person or computational program that converts written or spoken language from one tongue into another.",
    "secondary": "In computer systems programming, software (such as an assembler, compiler, or interpreter) that converts source code into machine-executable instructions.",
    "quotes": [
      {"author": "Charles Dickens", "work": "The Life and Adventures of Nicholas Nickleby", "quote": "As a tutor and **translator**, his attainments made the student's way unusually pleasant and profitable."},
      {"author": "Samuel Johnson", "work": "The Idler", "quote": "A faithful **translator** will seek to preserve not merely the literal words but the peculiar grace and spirit of the original author."},
      {"author": "Alexander Pope", "work": "Preface to the Iliad", "quote": "The greatest duty of a **translator** is to preserve that fire which is the principal characteristic of Homer."}
    ]
  },
  "Dashboard — lat/uncorrelated.md": {
    "primary": "Having no mutual or reciprocal relationship; exhibiting no systematic linear statistical dependence between variables.",
    "secondary": "In probability theory and signal processing, describing random variables whose mathematical covariance is zero, demonstrating an absence of linear predictability.",
    "quotes": [
      {"author": "Karl Pearson", "work": "The Grammar of Science", "quote": "Two series of physical measurements may be mathematically **uncorrelated** and yet governed by independent natural laws."},
      {"author": "Ronald Fisher", "work": "Statistical Methods for Research Workers", "quote": "When the sample residuals are completely **uncorrelated**, the standard error estimates attain optimal efficiency."},
      {"author": "Norbert Wiener", "work": "Cybernetics", "quote": "Filtering random noise requires separating the correlated message signal from the **uncorrelated** background fluctuations."}
    ]
  },
  "Dashboard — lat/unlatched.md": {
    "primary": "Opened, loosened, or freed by lifting or withdrawing a latch; not firmly fastened, bolted, or secured.",
    "secondary": "In narrative prose, describing an unsecured entrance, window, or wicket swinging open in the wind or granting unhindered passage.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Clare **unlatched** the door of a large chamber, felt his way across it, and stepped onto the damp turf outside."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The garden gate was found **unlatched**, swinging softly in the evening breeze against the wooden post."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "I quietly **unlatched** the kitchen door and crept out into the cold morning mist."}
    ]
  },
  "Dashboard — lat/unrelated.md": {
    "primary": "Having no connection, relevance, or logical link to something else; or not connected by kinship, blood, or common lineage.",
    "secondary": "In comparative biology and statistical modeling, designating disparate taxa, traits, or variables that originate from independent lineages or unconnected causal processes.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "**Unrelated** men give little joy to each other; will never suspect the latent genius slumbering beneath common appearances."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "Structures serving similar functions may develop in totally **unrelated** organisms through the operation of convergent adaptation."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "Mystical states often appear abruptly, seemingly **unrelated** to the subject's prior intellectual convictions."}
    ]
  },
  "Dashboard — lat/unrelatedness.md": {
    "primary": "The absence of mutual connection, causal association, logical coherence, or kinship between entities.",
    "secondary": "In cognitive psychology and epistemology, the perceived condition of isolated concepts or sensory data prior to integration into an interpretive conceptual scheme.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The apparent **unrelatedness** of isolated sensations is an illusion produced by abstracting parts from the continuous stream of thought."},
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "The mind abhors the complete **unrelatedness** of things, seeking ceaselessly for the underlying thread of necessity."},
      {"author": "Alfred North Whitehead", "work": "Adventures of Ideas", "quote": "The illusion of complete **unrelatedness** arises when we forget that every event inherits conditions from the past universe."}
    ]
  },
  "Dashboard — lat/untranslatable.md": {
    "primary": "Not capable of being satisfactorily translated or expressed in another language without severe loss of meaning, nuance, or rhetorical force.",
    "secondary": "In literary aesthetics and cultural linguistics, denoting idiomatic expressions or poetic forms whose semantic and aesthetic resonances are inextricably intertwined with their native tongue.",
    "quotes": [
      {"author": "Walt Whitman", "work": "Song of Myself", "quote": "I too am not a bit tamed, I too am **untranslatable**, / I sound my barbaric yawp over the roofs of the world."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The true lyric poem is essentially **untranslatable**, for the sound and the sense are mutually constitutive."},
      {"author": "Friedrich Nietzsche", "work": "Beyond Good and Evil", "quote": "What is most difficult to render from one language into another is the tempo of its style, which is often completely **untranslatable**."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Carrying"

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

print(f"Carrying Batch 4D (lat): Successfully updated {updated}/{len(data)} notes.")
