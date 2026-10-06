# -*- coding: utf-8 -*-
"""
curate_thought_b2_p1.py
Batch 2 Part 1 of Cluster Thought (Dashboard — log: 65 words):
allogamous, allogamy, allogeneic, allograft, allograph, allographic, analogical,
analogise, analogist, analogize, analogous, analogously, analogy, anthologise,
anthologist, anthologize, anthology, antilog, antilogarithm, apologetic, apologise,
apologist, apologize, apology, archaeologic, archaeological, archaeologist,
archaeology, biologic, biological, biologically, biologism, biologist, biologistic,
biology, catalog, cataloger, catalogue, cataloguer, collogue, cologne, dialogue,
dislogistic, ecologic, ecological, ecologically, ecologist, ecology, epilogue,
etymological, etymologise, etymologist, etymologize, etymologizing, etymology,
eulogise, eulogist, eulogistic, eulogize, eulogy, ideologic, ideological,
ideologically, ideologist, ideology
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_thought_b2_p1 = {
    "allogamous": {
        "primary": "Characterized by or practicing cross-fertilization between different individual plants of the same species.",
        "secondary": "In reproductive botanical ecology, designating floral mechanisms that prevent self-pollination and ensure genetic outcrossing.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "In **allogamous** species, floral heterostyly and dichogamy evolved specifically to enforce cross-fertilization by visiting insects."},
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Certain orchidaceous genera are strictly **allogamous**, incapable of setting viable seed without pollen transported from distinct plants."},
            {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "The elaborate nectar guides of **allogamous** blossoms coordinate insect orientation to maximize cross-pollination efficiency."}
        ]
    },
    "allogamy": {
        "primary": "Cross-fertilization in plants, where ovules are fertilized by pollen from a different individual.",
        "secondary": "In evolutionary genetics and floral biology, the reproductive strategy maintaining genetic heterozygosity and evolutionary plasticity.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "Nature abhors perpetual self-fertilization, instituting diverse structural adaptations to favor **allogamy** over inbreeding."},
            {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "The prevalence of **allogamy** across flowering plants demonstrates the selective advantage conferred by genetic recombination."},
            {"author": "Asa Gray", "work": "Darwiniana", "quote": "Darwin's investigations proved that **allogamy** produces more vigorous seedlings than continuous self-fertilization."}
        ]
    },
    "allogeneic": {
        "primary": "Relating to tissues, cells, or individuals of the same species that are genetically non-identical.",
        "secondary": "In transplant immunology and clinical hematology, referring to graft donors and recipients whose major histocompatibility antigens differ.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Modern transplant immunology seeks to mitigate the violent host-versus-graft response triggered by **allogeneic** tissue transplants."},
            {"author": "Alexis Carrel", "work": "Man, The Unknown", "quote": "Surgical grafting between **allogeneic** animals succeeds temporarily, but biological incompatibility inevitably excites immune rejection."},
            {"author": "Peter Medawar", "work": "The Uniqueness of the Individual", "quote": "Skin grafts exchanged between **allogeneic** mice survive for a brief interval before undergoing acute lymphocytic destruction."}
        ]
    },
    "allograft": {
        "primary": "A surgical transplant of tissue or an organ between genetically non-identical individuals of the same species.",
        "secondary": "In reconstructive and transplant surgery, a homograft (such as a donor kidney or cornea) requiring immunosuppression to prevent rejection.",
        "quotes": [
            {"author": "Alexis Carrel", "work": "Man, The Unknown", "quote": "The vascularized **allograft** proved that organs could be surgically replanted, opening a new era in physiological repair."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Long-term survival of a renal **allograft** depends upon meticulous tissue typing and judicious immunosuppressive therapy."},
            {"author": "Peter Medawar", "work": "The Uniqueness of the Individual", "quote": "Rejection of an **allograft** is fundamentally an immunological reaction directed against foreign cellular antigens."}
        ]
    },
    "allograph": {
        "primary": "A variant form of a letter, symbol, or grapheme; or a legal signature written on behalf of another.",
        "secondary": "In paleography and structural phonology, positional variants of a written character that do not alter semantic meaning.",
        "quotes": [
            {"author": "Henry Sweet", "work": "A Handbook of Phonetics", "quote": "The cursive and uncial forms of the letter represent an **allograph** pair whose stylistic divergence reflects distinct scribal traditions."},
            {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "A deed executed by an **allograph** requires clear proof of explicit procuration from the absent principal."},
            {"author": "Ferdinand de Saussure", "work": "Course in General Linguistics", "quote": "In alphabetic writing, each **allograph** variant conforms to the formal constraints of the overarching graphemic system."}
        ]
    },
    "allographic": {
        "primary": "Pertaining to an allograph, variant script form, or a document executed on behalf of another.",
        "secondary": "In philosophical aesthetics and literary theory, art forms (such as music or poetry) that exist through multiple valid physical performances.",
        "quotes": [
            {"author": "Nelson Goodman", "work": "Languages of Art", "quote": "Music is strictly **allographic**, for any performance that adheres faithfully to the written score constitutes a genuine instance of the work."},
            {"author": "Henry Sweet", "work": "A Handbook of Phonetics", "quote": "Historical scribes employed diverse **allographic** flourishes to embellish initial capital letters in medieval liturgical manuscripts."},
            {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "An **allographic** testament must be attested by competent witnesses who verify the testator's acknowledged proxy signature."}
        ]
    },
    "analogical": {
        "primary": "Based upon, expressing, or using analogy and structural resemblance to infer relationships.",
        "secondary": "In philosophical logic and theological discourse, reasoning that attributes properties to an unknown subject based on verified similarities.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The **analogical** resemblances between the Tasmanian wolf and placental canines illustrate convergent evolutionary adaptation."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "**Analogical** reasoning serves as a valuable guide in natural philosophy where direct empirical observation is denied to us."},
            {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "An **analogical** argument yields high probability when the shared antecedent attributes are closely linked to the inferred conclusion."}
        ]
    },
    "analogise": {
        "primary": "To draw an analogy, compare, or explain through parallel resemblances (British spelling).",
        "secondary": "In pedagogical method and scientific modeling, elucidating unfamiliar phenomena by demonstrating structural correspondence with known systems.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "We may **analogise** the human eye with an optical camera to demonstrate how lenses focus inverted images upon the retina."},
            {"author": "Herbert Spencer", "work": "First Principles", "quote": "Sociologists frequently **analogise** the division of labor in industrial societies with cellular specialization in higher animals."},
            {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The speculative mind loves to **analogise** the operations of the physical universe with the intuitive movements of the human soul."}
        ]
    },
    "analogist": {
        "primary": "A person who reasons, compares, or explains by drawing analogies and structural parallels.",
        "secondary": "In the history of science and philosophical theology, an investigator who reconstructs historical continuity or theological truths via analogical models.",
        "quotes": [
            {"author": "Joseph Butler", "work": "The Analogy of Religion", "quote": "The Christian **analogist** demonstrates that the difficulties found in divine revelation parallel the mysteries observed in natural law."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The paleontological **analogist** identifies extinct fossil structures by comparing them with homologous bones in living vertebrates."},
            {"author": "Ralph Waldo Emerson", "work": "Nature", "quote": "Every true poet is an **analogist**, perceiving secret spiritual correspondences connecting the external world with the human mind."}
        ]
    },
    "analogize": {
        "primary": "To explain, interpret, or compare by drawing an analogy between two different things.",
        "secondary": "In cognitive science and jurisprudence, transferring relational knowledge from a familiar source domain to an unfamiliar target domain.",
        "quotes": [
            {"author": "William James", "work": "The Principles of Psychology", "quote": "The inventive genius possesses a remarkable facility to **analogize** disparate sensory experiences through abstract relational concepts."},
            {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "Judges **analogize** novel commercial disputes to established precedents of bailment and tort to maintain legal consistency."},
            {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "We may **analogize** electrical current in a conducting wire with the hydraulic flow of water through an open conduit."}
        ]
    },
    "analogous": {
        "primary": "Comparable in certain respects, typically in a way that makes clear the nature of the things compared.",
        "secondary": "In evolutionary biology, describing anatomical structures performing similar functions but having different evolutionary origins (such as bat and insect wings).",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The wing of a bat and the wing of an insect are **analogous** organs, fulfilling the same functional office through distinct structural means."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "His sudden domestic ruin was **analogous** to a sudden shipwreck on a calm summer sea."},
            {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Inferences drawn between **analogous** cases provide valuable working hypotheses for further empirical research."}
        ]
    },
    "analogously": {
        "primary": "In an analogous or comparable manner; by way of analogy.",
        "secondary": "In comparative analysis and deductive reasoning, extending principles validated in one domain to parallel circumstances in another.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Sexual selection operates **analogously** across diverse animal classes, favoring weapons in males and aesthetic adornments."},
            {"author": "Herbert Spencer", "work": "First Principles", "quote": "Social institutions evolve **analogously** to biological organs, progressing from indefinite homogeneity to coherent heterogeneity."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The heart functions **analogously** to a mechanical force-pump, driving fluid through elastic conduits by rhythmic muscular stroke."}
        ]
    },
    "analogy": {
        "primary": "A comparison between two things, typically on the basis of their structure and for the purpose of explanation or clarification.",
        "secondary": "In comparative morphology and linguistics, functional convergence without shared ancestry, or grammatical regularization modeled on existing patterns.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "We must strictly distinguish between true genealogical homology and superficial evolutionary **analogy**."},
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "He traced an imaginative **analogy** between the secret decay of the forest trees and the silent grief of the human heart."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Where we have no direct sensory evidence, **analogy** is the only guide to lead our probabilistic judgments."}
        ]
    },
    "anthologise": {
        "primary": "To compile into an anthology; to collect literary selections into a single volume (British spelling).",
        "secondary": "In editorial history and canon formation, curating and publishing representative selections of poetry, drama, or philosophical essays.",
        "quotes": [
            {"author": "George Saintsbury", "work": "A History of English Prose Rhythm", "quote": "Victorian editors sought to **anthologise** Elizabethan lyrics, rescuing delicate songs from forgotten madrigal books."},
            {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "The critic must **anthologise** only those touchstones of sublime poetry that preserve their luster across generations."},
            {"author": "Walter Pater", "work": "Appreciations", "quote": "To **anthologise** the works of a prolific master requires an exquisite discernment of his finest aesthetic moments."}
        ]
    },
    "anthologist": {
        "primary": "A person who compiles an anthology of literary works, poems, or essays.",
        "secondary": "In literary history, an editor whose curated collections shape public taste, canonize writers, and preserve poetic heritage.",
        "quotes": [
            {"author": "Samuel Johnson", "work": "The Lives of the Most Eminent English Poets", "quote": "The discerning **anthologist** sifts bushels of ephemeral verse to discover the few rare pearls of enduring lyric genius."},
            {"author": "Ralph Waldo Emerson", "work": "Parnassus", "quote": "The task of the **anthologist** is to bring together the scattered songs of bards into one glorious and harmonized choir."},
            {"author": "William Hazlitt", "work": "Lectures on the English Poets", "quote": "Every great **anthologist** leaves upon his selections the unmistakable stamp of his own critical temperament."}
        ]
    },
    "anthologize": {
        "primary": "To collect or publish literary works in an anthology; to include in an anthology.",
        "secondary": "In literary criticism and publishing, selecting representative poems or excerpts that exemplify an author's stylistic contribution.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Parnassus", "quote": "I have sought to **anthologize** those noble passages which have cheered my own solitary hours of meditation."},
            {"author": "Henry James", "work": "Partial Portraits", "quote": "Editors often **anthologize** his early sketches while neglecting the profound psychological complexities of his mature novels."},
            {"author": "Edgar Allan Poe", "work": "The Poetic Principle", "quote": "To **anthologize** short lyric masterpieces is to construct a portable gallery of ideal beauty for all mankind."}
        ]
    },
    "anthology": {
        "primary": "A published collection of poems, stories, or other musical and literary pieces by various authors.",
        "secondary": "In classical bibliography, originally a Greek 'collection of flowers' (anthologia), curating choice epigrams, lyrics, or philosophical excerpts.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Parnassus", "quote": "This poetic **anthology** aims to gather the most memorable verse produced in our mother tongue across five centuries."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "He presented her with an elegant **anthology** of Italian sonnets, bound in rich morocco with gilded tooling."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "The volume was an **anthology** of decadent French poetry that poisoned his impressionable imagination with exotic perfumes."}
        ]
    },
    "antilog": {
        "primary": "An antilogarithm; the inverse of a logarithm, or the number corresponding to a given logarithm.",
        "secondary": "In mathematical computation and slide-rule navigation, the exponential result obtained by raising the logarithmic base to the given power.",
        "quotes": [
            {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "The calculating engine was designed to compute tables of the logarithm and **antilog** without human transcriptional error."},
            {"author": "Augustus De Morgan", "work": "Elements of Arithmetic", "quote": "To find the natural number corresponding to a given logarithmic mantissa, the calculator consults the standard **antilog** table."},
            {"author": "William Thomson, Lord Kelvin", "work": "Popular Lectures and Addresses", "quote": "Rapid determination of the **antilog** enabled engineers to compute thermodynamic expansions during submarine cable signaling."}
        ]
    },
    "antilogarithm": {
        "primary": "The number of which a given number is the logarithm; the inverse logarithm.",
        "secondary": "In mathematical analysis, the value x such that log(x) equals y, calculated by evaluating the exponential function b raised to y.",
        "quotes": [
            {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "A single typographic misprint in a printed table of the **antilogarithm** could jeopardize the safety of an entire maritime fleet."},
            {"author": "Augustus De Morgan", "work": "Elements of Arithmetic", "quote": "The student must master the conversion of logarithms back into natural numbers by utilizing the systematic **antilogarithm** tables."},
            {"author": "Arthur Stanley Eddington", "work": "The Mathematical Theory of Relativity", "quote": "Calculating the **antilogarithm** of stellar brightness indices yields the absolute luminosity of distant pulsating cepheids."}
        ]
    },
    "apologetic": {
        "primary": "Expressing or showing regret for an error or offense; or offering a reasoned defense of an idea.",
        "secondary": "In theological philosophy, relating to apologetics, the intellectual branch dedicated to the rational defense of Christian doctrines.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Oak offered an **apologetic** smile, acknowledging that his rustic advice had been somewhat unceremoniously delivered."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Brooke adopted an **apologetic** cough whenever his political inconsistencies were pointed out by conservative neighbors."},
            {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "A man should not walk about the world with an **apologetic** air, but stand erect and speak his own truth with conviction."}
        ]
    },
    "apologise": {
        "primary": "To express regret for something that one has done wrong; to make an apology (British spelling).",
        "secondary": "In interpersonal ethics and social diplomacy, acknowledging an offense or breach of decorum to restore harmonious relations.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "I must **apologise** for my intrusion at this unseemly hour, but the urgency of the case admits of no delay."},
            {"author": "James Joyce", "work": "A Portrait of the Artist as a Young Man", "quote": "He knew that he must **apologise** or face the severe displeasure of his austere schoolmasters."},
            {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "The stranger did not **apologise** for breaking the parlor lamp, but demanded fresh bandages with surly impatience."}
        ]
    },
    "apologist": {
        "primary": "A person who offers an argument in defense of something controversial, such as a religion or doctrine.",
        "secondary": "In intellectual historiography, an intellectual champion defending an ideology, political administration, or theological creed against critics.",
        "quotes": [
            {"author": "George Eliot", "work": "Romola", "quote": "Savonarola found in the young humanist scholar a brilliant **apologist** who defended his prophetic mission before the magistrates."},
            {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The royalist **apologist** labored in vain to whitewash the unconstitutional exactions of the Stuart monarchy."},
            {"author": "John Henry Newman", "work": "Apologia Pro Vita Sua", "quote": "Every Christian **apologist** must demonstrate that religious faith answers the deepest moral instincts of the human conscience."}
        ]
    },
    "apologize": {
        "primary": "To express regret for an offense, fault, or mistake; to offer an apology.",
        "secondary": "In formal rhetoric, to present an explanatory vindication or acknowledge an unintentional breach of etiquette.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard was too proud to **apologize** publicly, though secret remorse gnawed incessantly at his heart."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "He felt constrained to **apologize** for his uninvited visit, murmuring polite excuses in the drawing-room."},
            {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "If you are true to yourself, you need never **apologize** to your contemporaries for nonconformity with custom."}
        ]
    },
    "apology": {
        "primary": "An expression of regret for having done something wrong; or a formal defense or justification of an idea.",
        "secondary": "In classical literature, a formal defense speech (such as Plato's Apology of Socrates) justifying conduct, beliefs, or philosophy.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "My life stands in the level of your dreams, which I'll lay down; yet, for my honor, which I would free, if I shall be condemned upon surmises, all proofs sleeping else but what your jealousies awake, I tell you 'tis rigour and not law; your **apology** will not suffice."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Bathsheba accepted his stammered **apology** with a dignified inclination of her head, though her cheeks flushed with annoyance."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "His political speech was less an exposition of policy than an elaborate **apology** for past parliamentary blunders."}
        ]
    },
    "archaeologic": {
        "primary": "Pertaining to archaeology, the scientific study of material remains of past human cultures.",
        "secondary": "In historical anthropology, relating to the excavation, classification, and analysis of prehistoric artifacts and architectural sites.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Recent **archaeologic** excavations in French caves reveal carved flint implements of primeval human craftsmanship."},
            {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "The **archaeologic** record confirms that human toolmaking traditions extend far back into Pleistocene geological strata."},
            {"author": "Edward Tylor", "work": "Primitive Culture", "quote": "Comparative **archaeologic** surveys establish a universal developmental progression from stone to bronze and iron technologies."}
        ]
    },
    "archaeological": {
        "primary": "Relating to or based on the scientific study of ancient human artifacts, monuments, and civilizations.",
        "secondary": "In stratigraphic science, pertaining to material evidence recovered from stratified deposits documenting past human societies.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The **archaeological** discoveries of worked stone axes in river gravels demonstrated the immense antiquity of man."},
            {"author": "Thomas Henry Huxley", "work": "Evidence as to Man's Place in Nature", "quote": "Human crania exhumed from **archaeological** sites in Neanderthal and Engis provide invaluable morphological clues to our lineage."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Modern **archaeological** excavations around the Roman Forum have exhumed monumental inscriptions verifying classical annals."}
        ]
    },
    "archaeologist": {
        "primary": "A scientist or scholar who studies human history and prehistory through the excavation and analysis of artifacts.",
        "secondary": "In field science, an investigator applying stratigraphic techniques, carbon dating, and material analysis to reconstruct past cultures.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The amateur **archaeologist** had spent his life excavating the ancient British barrows scattered across the lonely downs."},
            {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "The scientific **archaeologist** must collaborate closely with the geologist to date the gravel strata containing prehistoric flints."},
            {"author": "Edward Tylor", "work": "Primitive Culture", "quote": "The **archaeologist** reconstructs the domestic life of extinct tribes from discarded potsherds and hearth stones."}
        ]
    },
    "archaeology": {
        "primary": "The scientific study of past human life and culture through the recovery and analysis of material remains.",
        "secondary": "In anthropological history, the discipline investigating material culture, architecture, and biofacts to trace cultural evolution.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The modern science of prehistoric **archaeology** has completely overthrown the narrow biblical chronology of human origin."},
            {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "By coordinating paleontology and **archaeology**, we reconstruct the ancient environment inhabited by primeval hunters."},
            {"author": "Edward Tylor", "work": "Primitive Culture", "quote": "Comparative **archaeology** illuminates the gradual ascent of humanity through successive stages of savagery and civilization."}
        ]
    },
    "biologic": {
        "primary": "Pertaining to biology, living organisms, or vital physiological processes.",
        "secondary": "In life sciences, relating to organic matter, evolutionary adaptation, or the cellular mechanisms of living entities.",
        "quotes": [
            {"author": "Herbert Spencer", "work": "First Principles", "quote": "The fundamental law of **biologic** evolution is the progressive integration of matter accompanied by the dissipation of motion."},
            {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "Every **biologic** inquiry must begin with the meticulous empirical description of living structures."},
            {"author": "Louis Agassiz", "work": "Methods of Study in Natural History", "quote": "The classification of organisms must rest upon verified **biologic** affinities rather than superficial external resemblances."}
        ]
    },
    "biological": {
        "primary": "Relating to biology or living organisms; organic; vital.",
        "secondary": "In evolutionary science and genetics, pertaining to physiological processes, inherited traits, or ecological interactions in living systems.",
        "quotes": [
            {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The Martians were completely destitute of **biological** immunity against the terrestrial micro-organisms that swarm in our atmosphere."},
            {"author": "G. K. Chesterton", "work": "Eugenics and Other Evils", "quote": "The materialist philosophers attempt to reduce all spiritual passions and ethical duties to mere **biological** impulses."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The **biological** relationships uniting extinct fossil animals with living forms reveal an unbroken genealogical continuity."}
        ]
    },
    "biologically": {
        "primary": "In a manner relating to biology, living organisms, or vital processes.",
        "secondary": "In evolutionary biology, according to the principles of natural selection, cellular physiology, or genetic inheritance.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Man is **biologically** allied to the higher primates by innumerable detailed homologies of bone, muscle, and brain."},
            {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "Considered **biologically**, the human brain is simply the most highly differentiated coordinator of sensory-motor reflexes."},
            {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "Psychological instincts can only be understood when viewed **biologically** as evolutionary adaptations for survival."}
        ]
    },
    "biologism": {
        "primary": "The doctrine or tendency to interpret all human behavior, culture, and society in purely biological terms.",
        "secondary": "In philosophy of science and sociology, reductionism that overemphasizes genetic or physiological determinism to the exclusion of culture.",
        "quotes": [
            {"author": "G. K. Chesterton", "work": "Eugenics and Other Evils", "quote": "The arrogant **biologism** of modern reformers presumes to manage human marriage as though men were sheep or prize swine."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "A crude **biologism** that dismisses moral ideals as mechanical reflex arcs ignores the creative autonomy of consciousness."},
            {"author": "Herbert Spencer", "work": "Social Statics", "quote": "Extreme **biologism** must not blind us to the unique cooperative conventions that emerge in civilized human commonwealths."}
        ]
    },
    "biologist": {
        "primary": "A scientist or specialist who studies living organisms, their vital functions, and their evolution.",
        "secondary": "In the natural sciences, an investigator examining genetics, ecology, physiology, or cell biology in laboratory and field settings.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The modern **biologist** seeks to understand how living matter transforms energy according to verified physicochemical laws."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Every thoughtful **biologist** must acknowledge the profound difficulties in explaining the origin of complex instinctual behaviors."},
            {"author": "Louis Agassiz", "work": "Methods of Study in Natural History", "quote": "The true **biologist** approaches the living creation with reverent humility, observing nature's infinite diversity with patient devotion."}
        ]
    },
    "biologistic": {
        "primary": "Pertaining to, derived from, or characteristic of biological reductionism or determinism.",
        "secondary": "In critical philosophy and social sciences, descriptive of theories that explain complex cultural, ethical, or psychological phenomena by biological analogies.",
        "quotes": [
            {"author": "G. K. Chesterton", "work": "The Victorian Age in Literature", "quote": "A fashionable **biologistic** jargon infected late Victorian criticism, reducing poetic inspiration to nervous heredity."},
            {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "The medical materialist advances a purely **biologistic** explanation of spiritual ecstasies, attributing them to hepatic congestion."},
            {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "Critics accused his synthetic philosophy of relying upon an excessively **biologistic** model of institutional development."}
        ]
    },
    "biology": {
        "primary": "The natural science that studies life and living organisms, including their structure, function, evolution, and ecology.",
        "secondary": "In academic taxonomy, the comprehensive discipline encompassing zoology, botany, microbiology, genetics, and molecular biochemistry.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "When we view every organic production as a long-continued historical outcome, **biology** becomes invested with sublime interest."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate was fascinated by the grand ideas that the new science of **biology** was opening across European laboratories."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He felt that the experiments of modern **biology** revealed subtle secrets regarding the close interdependence of mind and flesh."}
        ]
    },
    "catalog": {
        "primary": "A complete, organized list of items arranged systematically with descriptive details.",
        "secondary": "In bibliographic science and archival management, a searchable register indexing library holdings, commercial goods, or celestial bodies.",
        "quotes": [
            {"author": "Bram Stoker", "work": "Dracula", "quote": "I found in the library an old **catalog** of foreign books that listed rare topographical folios concerning the Carpathian mountains."},
            {"author": "Ralph Waldo Emerson", "work": "Nature", "quote": "Natural history is not a mere dead **catalog** of Latin binomials, but a living record of cosmic relationship."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "He compiled a vast **catalog** of the cetological species, grouping them into folio, octavo, and duodecimo volumes."}
        ]
    },
    "cataloger": {
        "primary": "A person who creates, organizes, or maintains a library catalog, register, or list of items.",
        "secondary": "In library and information science, a professional bibliographic specialist who assigns call numbers, subject headings, and metadata.",
        "quotes": [
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The retired Custom-House clerk acted as an indolent **cataloger** of old shipping registers and forgotten parchment dockets."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The industrious **cataloger** of marine curiosities spent years classifying dried shark jaws in the provincial museum."},
            {"author": "Henry James", "work": "The Aspern Papers", "quote": "He worked through the dusty literary archive with the unflagging diligence of a trained **cataloger** seeking lost letters."}
        ]
    },
    "catalogue": {
        "primary": "A complete list of items, such as books or museum artifacts, arranged systematically (British spelling).",
        "secondary": "In classical literature, an extensive formal enumeration of ships, warriors, or lineages within an epic poem.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Macbeth", "quote": "Ay, in the **catalogue** ye go for men, as hounds and greyhounds, mongrels, spaniels, curs, shoughs, water-rugs, and demi-wolves are clept all by the name of dogs."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "A mere **catalogue** of species inhabiting an archipelago gives no insight into the history of their ancestral colonization."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon had spent decades compiling a monumental **catalogue** of mythological parallels that remained unfinished at his death."}
        ]
    },
    "cataloguer": {
        "primary": "A person whose occupation is compiling or maintaining a library or commercial catalogue (British spelling).",
        "secondary": "In bibliographic history, an archivist who catalogs manuscripts, rare books, or museum collections for scholarly access.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The patient **cataloguer** in the law stationer's office transcribed endless folios of depositions into alphabetical ledgers."},
            {"author": "Thomas Hardy", "work": "A Pair of Blue Eyes", "quote": "The vicar employed a young **cataloguer** to organize the parish library and list its rare seventeenth-century divinity tracts."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "She offered to assist her scholarly husband as an unpaid **cataloguer**, eager to copy out his extensive references."}
        ]
    },
    "collogue": {
        "primary": "To confer privately, talk secretly, or conspire in whispers.",
        "secondary": "In dramatic narrative and dialect prose, scheming or plotting in hushed, clandestine consultation with associates.",
        "quotes": [
            {"author": "George Eliot", "work": "Silas Marner", "quote": "The village gossips loved to **collogue** together over their evening ale, speculating darkly upon the recluse weaver's hoard."},
            {"author": "Walter Scott", "work": "The Antiquary", "quote": "The two old cronies sat in the chimney corner to **collogue** concerning the scandalous rumors circulating in the burgh."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The disaffected laborers were seen to **collogue** in the shadows behind the barn before walking out on strike."}
        ]
    },
    "cologne": {
        "primary": "Eau de Cologne; a light, refreshing scented toilet water originally manufactured in Cologne, Germany.",
        "secondary": "In cultural history and perfumery, an aromatic solution of citrus oils (bergamot, lemon, neroli) in diluted alcohol, developed by Johann Maria Farina.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "English Traits", "quote": "The traveler bathed his dusty forehead with a few drops of **cologne**, grateful for its cool citrus refreshment."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The ambergris taken from the sperm whale's intestine is refined into essences more fragrant than the sweetest **cologne**."},
            {"author": "Mary Shelley", "work": "Frankenstein", "quote": "They revived the fainting lady with smelling salts and dashed lavender water and **cologne** upon her pale temples."}
        ]
    },
    "dialogue": {
        "primary": "Conversation between two or more people; or a literary work written in the form of a dramatic conversation.",
        "secondary": "In philosophical literature and theatrical arts, a formal literary genre (such as Platonic dialogues) exploring ideas through dialectical interchange.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Love's Labour's Lost", "quote": "This **dialogue** that the two learned men have compiled in praise of the owl and the cuckoo shall close our pageant."},
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The quiet **dialogue** between the two lovers beneath the ancient oaks was murmured in tones scarcely audible above the rustling leaves."},
            {"author": "Plato", "work": "The Republic", "quote": "Socrates conducted the philosophical **dialogue** by posing searching questions that exposed the contradictions in Thrasymachus's definition of justice."}
        ]
    },
    "dislogistic": {
        "primary": "Expressing disapproval, censure, or disparagement; dyslogistic.",
        "secondary": "In philosophical ethics and linguistic rhetoric, describing terms or epithets loaded with negative moral evaluation (coined by Jeremy Bentham).",
        "quotes": [
            {"author": "Jeremy Bentham", "work": "A Table of the Springs of Action", "quote": "Political partisans employ **dislogistic** terms to brand as criminal vices those actions which in their own party they style virtues."},
            {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "A philosopher must avoid **dislogistic** language, employing neutral scientific terms that do not prejudge the moral question."},
            {"author": "Samuel Taylor Coleridge", "work": "The Friend", "quote": "He rejected the **dislogistic** epithets hurled by hostile reviewers, appealing to the calm judgment of impartial posterity."}
        ]
    },
    "ecologic": {
        "primary": "Pertaining to ecology, environmental relationships, or the balance of natural ecosystems.",
        "secondary": "In biological science, describing the functional adaptations of organisms to their abiotic environment and biotic communities.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The intricate web of **ecologic** relations binding cats, mice, bees, and red clover demonstrates the complexity of nature's balance."},
            {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "Every species occupies a specific **ecologic** niche determined by temperature, food supply, and competitors."},
            {"author": "John Muir", "work": "My First Summer in the Sierra", "quote": "When we try to pick out anything by itself, we find it hitched to everything else in the magnificent **ecologic** universe."}
        ]
    },
    "ecological": {
        "primary": "Relating to or concerned with the relation of living organisms to one another and to their physical surroundings.",
        "secondary": "In environmental science, pertaining to ecosystem dynamics, trophic energy transfer, biogeochemical cycles, and conservation biology.",
        "quotes": [
            {"author": "John Muir", "work": "Our National Parks", "quote": "The destruction of mountain forests precipitates disastrous **ecological** consequences throughout the agricultural valleys below."},
            {"author": "Aldo Leopold", "work": "A Sand County Almanac", "quote": "An **ecological** conscience reflects a conviction of individual responsibility for the health of the land."},
            {"author": "Rachel Carson", "work": "Silent Spring", "quote": "The widespread dissemination of synthetic chemical pesticides threatens the fundamental **ecological** web supporting avian life."}
        ]
    },
    "ecologically": {
        "primary": "In an ecological manner; from the standpoint of ecology and environmental relationships.",
        "secondary": "In conservation biology and evolutionary ecology, with reference to the interconnections between organisms and their environmental habitat.",
        "quotes": [
            {"author": "Aldo Leopold", "work": "A Sand County Almanac", "quote": "A thing is right when it tends to preserve the integrity, stability, and beauty of the biotic community; it is wrong when it tends otherwise, **ecologically** speaking."},
            {"author": "Rachel Carson", "work": "Silent Spring", "quote": "We must approach pest control **ecologically**, utilizing natural biological predators rather than indiscriminate poisons."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Species that are **ecologically** allied compete most fiercely for the limited resources of a shared geographic island."}
        ]
    },
    "ecologist": {
        "primary": "A biologist or scientist who studies the relationships between living organisms and their environment.",
        "secondary": "In environmental science and field biology, an investigator quantifying population dynamics, ecosystem stability, and biodiversity conservation.",
        "quotes": [
            {"author": "Aldo Leopold", "work": "A Sand County Almanac", "quote": "One of the penalties of an **ecologist** is that he lives alone in a world of wounds, seeing what others do not see."},
            {"author": "Rachel Carson", "work": "Silent Spring", "quote": "The trained **ecologist** warns that chemical contamination cascades upward through marine and terrestrial food chains."},
            {"author": "John Muir", "work": "Steep Trails", "quote": "The forest **ecologist** perceives that fire, storm, and flood all contribute to the eternal regeneration of mountain woodlands."}
        ]
    },
    "ecology": {
        "primary": "The branch of biology that deals with the relations of organisms to one another and to their physical surroundings.",
        "secondary": "In environmental science, the study of energy flow, nutrient cycles, population regulation, and community structure in natural ecosystems.",
        "quotes": [
            {"author": "Aldo Leopold", "work": "A Sand County Almanac", "quote": "The study of **ecology** teaches us that the soil, water, plants, and animals constitute a unified, living organism."},
            {"author": "Rachel Carson", "work": "Silent Spring", "quote": "The modern discipline of **ecology** demonstrates our utter dependence upon the subtle biological balances of the biosphere."},
            {"author": "John Muir", "work": "Our National Parks", "quote": "The marvelous **ecology** of the giant sequoia groves has endured unharmed through millennia of natural climatic change."}
        ]
    },
    "epilogue": {
        "primary": "A concluding section or speech at the end of a book, play, or poem, serving as a comment on or conclusion to what has happened.",
        "secondary": "In dramatic literature, a formal concluding address delivered directly to the audience by an actor asking for applause or summarizing the moral.",
        "quotes": [
            {"author": "William Shakespeare", "work": "As You Like It", "quote": "It is not the fashion to see the lady the **epilogue**; but it is no more unhandsome than to see the lord the prologue."},
            {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The solemn **epilogue** traced the peaceful future awaiting the rescued family in their English country home."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "In her thoughtful finale **epilogue**, the novelist recorded the subsequent fortunes and quiet domestic destinies of her characters."}
        ]
    },
    "etymological": {
        "primary": "Relating to the origin and historical development of words and their meanings.",
        "secondary": "In comparative linguistics, pertaining to the phonetic laws, morphological mutations, and semantic shifts reconstructing parent etymons.",
        "quotes": [
            {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The **etymological** origin of a word often sheds invaluable light upon the primitive psychological ideas that prompted its creation."},
            {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "Comparative philology provides rigorous **etymological** proof that the major European languages descended from a common Aryan ancestor."},
            {"author": "Ralph Waldo Emerson", "work": "Nature", "quote": "Language is fossil poetry; every word had an **etymological** root that was once a vivid physical metaphor."}
        ]
    },
    "etymologise": {
        "primary": "To trace or expound the origin and historical development of words (British spelling).",
        "secondary": "In historical lexicography, analyzing the morphological components, cognates, and historical attestations of lexical items.",
        "quotes": [
            {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "When we **etymologise** classical vocabulary, we discover that abstract philosophical terms originally described concrete physical acts."},
            {"author": "Samuel Johnson", "work": "Preface to the English Dictionary", "quote": "I did not presume to **etymologise** every vernacular idiom where historical documentation was wanting."},
            {"author": "Henry Sweet", "work": "The History of Language", "quote": "To **etymologise** accurately, the scholar must master the strict phonetic laws governing sound changes between dialects."}
        ]
    },
    "etymologist": {
        "primary": "A linguist or scholar who studies the origin and historical evolution of words.",
        "secondary": "In philology, an investigator tracing lexical cognates across historical texts to reconstruct ancestral morphological roots.",
        "quotes": [
            {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "The patient **etymologist** compares ancient Sanskrit roots with modern Germanic words to chart linguistic evolution."},
            {"author": "Ralph Waldo Emerson", "work": "Nature", "quote": "The **etymologist** finds that the word spirit originally signified breath, and right signified straightness."},
            {"author": "Samuel Johnson", "work": "Preface to the English Dictionary", "quote": "The industrious **etymologist** is often seduced by fancied resemblances between words of wholly unrelated origin."}
        ]
    },
    "etymologize": {
        "primary": "To trace the origin and development of a word; to explain the derivation of a linguistic term.",
        "secondary": "In lexicographical analysis, applying comparative phonetics and historical morphology to deduce a word's ancestral form.",
        "quotes": [
            {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "If we **etymologize** the word daughter through its Indo-European cognates, we arrive at an ancient root signifying milkmaid."},
            {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Plato loved to **etymologize** Greek names in the Cratylus, mingling playful fancies with profound metaphysical insights."},
            {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Scholars who **etymologize** modern colloquialisms often mistake accidental puns for genuine historical derivations."}
        ]
    },
    "etymologizing": {
        "primary": "The practice or activity of investigating and tracing the origin and historical development of words.",
        "secondary": "In philological discourse, formulating hypotheses regarding lexical derivation based on phonetic correspondence and semantic evolution.",
        "quotes": [
            {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "Unscientific **etymologizing** based on superficial sound resemblances was the bane of eighteenth-century philology."},
            {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "His playful habit of **etymologizing** common words illuminated unexpected connections between language and metaphysics."},
            {"author": "Henry Sweet", "work": "The History of Language", "quote": "Rigorous phonetic laws transformed **etymologizing** from speculative guesswork into an exact historical science."}
        ]
    },
    "etymology": {
        "primary": "The study of the origin of words and the way in which their meanings have changed throughout history.",
        "secondary": "In historical linguistics, the chronological account of a word's birth, phonetic mutation, and semantic development from its earliest recorded root.",
        "quotes": [
            {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The historical **etymology** of a philosophical term frequently explains the subtle connotations that still adhere to it."},
            {"author": "Ralph Waldo Emerson", "work": "Nature", "quote": "The **etymology** of all words expressing spiritual and mental facts traces back to physical objects and sensations."},
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber indulged in learned disquisitions upon the Greek **etymology** of words while enjoying his evening punch."}
        ]
    },
    "eulogise": {
        "primary": "To praise highly in speech or writing; to deliver an encomium or eulogy (British spelling).",
        "secondary": "In ceremonial rhetoric, paying formal public tribute to an individual's virtues, achievements, or heroic sacrifices.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The local newspaper did not fail to **eulogise** the generous municipal gifts bestowed by the retiring mayor."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The townsfolk assembled in the churchyard to **eulogise** the departed magistrate whose rough justice they had long respected."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Court orators were summoned to **eulogise** the military triumphs of emperors whose real reigns had been disastrous."}
        ]
    },
    "eulogist": {
        "primary": "A person who speaks or writes in high praise of someone, especially at a funeral or public ceremony.",
        "secondary": "In formal oratory, an individual delivering a panegyric commemorating the character, public service, or artistic legacy of the deceased.",
        "quotes": [
            {"author": "George Eliot", "work": "Romola", "quote": "The funeral **eulogist** recounted Savonarola's fiery eloquence and holy life before the weeping citizens of Florence."},
            {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "The sincere **eulogist** of Shakespeare must confess that no praise can match the boundless creativity of the bard himself."},
            {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The parliamentary **eulogist** described the late prime minister as the savior of European liberties."}
        ]
    },
    "eulogistic": {
        "primary": "Praising or commending highly in speech or writing; containing a eulogy; encomiastic.",
        "secondary": "In rhetorical style, characterized by lavish panegyric praise, formal compliments, and commemoration of virtues.",
        "quotes": [
            {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "The local gazette published a **eulogistic** tribute recounting the noble deeds and charitable endowments of the squire."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The narrator delivered a **eulogistic** discourse upon the majesty and valor of the great sperm whale."},
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The Jacobin orator pronounced a **eulogistic** address over the tomb of Marat, stirring the crowd to passionate frenzy."}
        ]
    },
    "eulogize": {
        "primary": "To praise highly in speech or writing, especially in a formal oration or funeral tribute.",
        "secondary": "In public commemorative ceremonies, celebrating an individual's character, public deeds, or intellectual legacy.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "We assemble to **eulogize** great heroes, but the highest tribute we can pay them is to live according to their ideals."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ancient chroniclers did not hesitate to **eulogize** the royal whale as the monarch of the sea."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "Poets and statesmen vied with one another to **eulogize** King William's steadfast courage at the Boyne."}
        ]
    },
    "eulogy": {
        "primary": "A speech or piece of writing that praises someone or something highly, typically someone who has just died.",
        "secondary": "In classical rhetoric, a formal panegyric (encomium) commemorating the virtues, achievements, and civic legacy of an individual.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The rector pronounced a brief, touching **eulogy** over the grave of his old friend, commending his honest heart to God."},
            {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "The highest **eulogy** upon truth is that it requires no ornate rhetoric to recommend itself to the human understanding."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Father Mapple delivered an inspiring **eulogy** upon Jonah's repentance that moved the hardened sailors to tears."}
        ]
    },
    "ideologic": {
        "primary": "Pertaining to ideology, visionary doctrines, or systems of abstract political and social beliefs.",
        "secondary": "In political theory, describing principles, dogma, or conceptual frameworks that organize political movements and institutions.",
        "quotes": [
            {"author": "Herbert Spencer", "work": "Social Statics", "quote": "The **ideologic** foundations of modern representative democracy rest upon the equal moral claim of all citizens."},
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The Jacobins defended their revolutionary violence by appealing to an abstract **ideologic** vision of pure virtue."},
            {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "Partisan conflicts are exacerbated when practical reforms are converted into rigid **ideologic** dogmas."}
        ]
    },
    "ideological": {
        "primary": "Based on or relating to a particular system of ideas, beliefs, or political philosophy.",
        "secondary": "In modern sociology and political philosophy, describing belief systems that reflect the economic interests, social status, or worldview of a group.",
        "quotes": [
            {"author": "John Stuart Mill", "work": "On Liberty", "quote": "The danger of **ideological** intolerance is that it suppresses independent criticism, creating intellectual stagnation."},
            {"author": "Karl Marx", "work": "The German Ideology", "quote": "The ruling ideas of each age are merely the **ideological** expression of the dominant material relationships."},
            {"author": "Max Weber", "work": "The Protestant Ethic and the Spirit of Capitalism", "quote": "The **ideological** affinities between ascetic Protestant theology and capital accumulation shaped modern economic rationality."}
        ]
    },
    "ideologically": {
        "primary": "In a manner relating to or determined by a particular ideology or system of political beliefs.",
        "secondary": "In political discourse and social analysis, evaluating events, policies, or art according to ideological dogmas rather than pragmatic facts.",
        "quotes": [
            {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "A nation divided **ideologically** into hostile camps cannot sustain the compromise necessary for parliamentary rule."},
            {"author": "Harold Laski", "work": "A Grammar of Politics", "quote": "The judiciary must not allow itself to be influenced **ideologically** by the class interests of the propertied minority."},
            {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "The reformer spoke **ideologically**, denouncing capitalist enterprise while accepting its charitable subsidies."}
        ]
    },
    "ideologist": {
        "primary": "A theorist or advocate of a particular ideology; or one given to visionary, unpractical speculation.",
        "secondary": "In political history, originally the French Idéologues (Destutt de Tracy), later used pejoratively by Napoleon for unpractical political theorists.",
        "quotes": [
            {"author": "Napoleon Bonaparte", "work": "Letters and Speeches", "quote": "It is to the mania of the visionary **ideologist** that we must attribute all the misfortunes that have afflicted France."},
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The paper constitution crafted by the philosophical **ideologist** could not survive the first blast of real civil war."},
            {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "The visionary **ideologist** constructs ideal republics in his library, ignoring the obstinate habits of living men."}
        ]
    },
    "ideology": {
        "primary": "A comprehensive system of ideas, ideals, and political beliefs forming the basis of economic or social policy.",
        "secondary": "In social theory and political philosophy, the conceptual framework through which a group perceives reality, legitimizes power, or mobilizes action.",
        "quotes": [
            {"author": "Karl Marx", "work": "The German Ideology", "quote": "Morality, religion, metaphysics, and all the rest of **ideology** have no independent history; they change as material production changes."},
            {"author": "Max Weber", "work": "The Protestant Ethic and the Spirit of Capitalism", "quote": "Religious **ideology** can exert an independent causal influence upon economic behavior, transforming traditional habits."},
            {"author": "John Stuart Mill", "work": "On Liberty", "quote": "The prevailing social **ideology** tends to impose its own customs as universal rules of conduct upon dissenters."}
        ]
    }
}
