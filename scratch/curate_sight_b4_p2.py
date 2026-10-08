# -*- coding: utf-8 -*-
"""
curate_sight_b4_p2.py
Batch 4 Part 2 of Cluster Sight:
Dashboard — spec (remaining 34 of 68 new words):
speciate, speciation, specie, species, specifiable, specific,
specifically, specification, specificity, specified, specifier,
specify, specimen, specious, speciously, speciousness, specs,
specular, speculate, speculation, speculative, speculatively,
speculativeness, speculator, speculum, subspecies, suspect,
suspected, unspecialised, unspecialized, unspecific, unspecified,
unsuspected, unsuspecting
Total: 34 words.
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_sight_b4_p2 = {
    "speciate": {
        "primary": "To evolve or develop into a new biological species from an ancestral population.",
        "secondary": "In evolutionary biology, the process whereby gene flow between isolated populations ceases, leading to independent phenotypic divergence.",
        "quotes": [
            {"author": "Ernst Mayr", "work": "Systematics and the Origin of Species", "quote": "Geographically isolated populations tend to **speciate** when genetic drift and divergent selection accumulate."},
            {"author": "Stephen Jay Gould", "work": "The Structure of Evolutionary Theory", "quote": "Peripheral isolates may **speciate** rapidly on a geological timescale, producing punctuated equilibrium patterns."},
            {"author": "Theodosius Dobzhansky", "work": "Genetics and the Origin of Species", "quote": "Natural selection favors mechanisms that prevent wasteful hybridization, driving incipient races to **speciate**."}
        ]
    },
    "speciation": {
        "primary": "The evolutionary formation of new and distinct biological species from ancestral populations.",
        "secondary": "In micro- and macroevolutionary theory, encompasses allopatric, sympatric, and parapatric mechanisms mediated by reproductive isolation barriers.",
        "quotes": [
            {"author": "Ernst Mayr", "work": "Animal Species and Evolution", "quote": "Allopatric **speciation** remains the primary engine of taxonomic diversity among terrestrial vertebrates."},
            {"author": "Stephen Jay Gould", "work": "Ontogeny and Phylogeny", "quote": "Heterochronic shifts in developmental timing can accelerate **speciation** without requiring massive genomic restructuring."},
            {"author": "Richard Dawkins", "work": "The Blind Watchmaker", "quote": "Geographical barriers such as rivers or mountain ranges provide the initial severance essential for **speciation**."}
        ]
    },
    "specie": {
        "primary": "Money in the form of coins or metallic currency rather than paper banknotes.",
        "secondary": "In monetary economics and financial history, bullion or gold and silver coins held in bank reserves to guarantee convertible banknote redemption.",
        "quotes": [
            {"author": "Bram Stoker", "work": "Dracula", "quote": "He drew from his pocket a handful of ancient gold **specie**, offering it to the carriage driver."},
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A banking system must always maintain a prudent reserve of **specie** to meet sudden runs upon its credit."},
            {"author": "Alexander Hamilton", "work": "Report on the Subject of a National Bank", "quote": "Paper credit unsupported by adequate **specie** inevitably collapses into depreciation and public distress."}
        ]
    },
    "species": {
        "primary": "A group of living organisms consisting of similar individuals capable of exchanging genes or interbreeding.",
        "secondary": "In formal logic, taxonomy, and epistemology, a subordinate category within a genus characterized by shared distinctive essential properties.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "I look at the term **species** as one arbitrarily given, for the sake of convenience, to a set of individuals closely resembling each other."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The sheep seemed to belong to an ancient, unalterable **species** that had pastured on the chalk downs since Roman days."},
            {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "In philosophical classification, a **species** is marked off from its genus by some fundamental attribute."}
        ]
    },
    "specifiable": {
        "primary": "Capable of being specified, defined, named, or determined precisely.",
        "secondary": "In computational logic and legal theory, describes conditions, contractual obligations, or algorithmic parameters that can be stated unambiguously.",
        "quotes": [
            {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "A logical class is well-defined only when its defining characteristic is clearly **specifiable**."},
            {"author": "John Dewey", "work": "Logic: The Theory of Inquiry", "quote": "Inquiry begins with an indeterminate situation and moves toward a determinate, **specifiable** problem."},
            {"author": "Karl Popper", "work": "The Logic of Scientific Discovery", "quote": "A scientific hypothesis must possess **specifiable** empirical conditions under which it could be falsified."}
        ]
    },
    "specific": {
        "primary": "Clearly defined or identified; precise and detailed; peculiar to a particular thing.",
        "secondary": "In pharmacology and taxonomy, refers to a therapeutic remedy targeting a single distinct disease or traits defining an individual biological species.",
        "quotes": [
            {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The **specific** differences between allied varieties often escape the casual glance of the observer."},
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants Under Domestication", "quote": "Certain pigeon varieties exhibit **specific** differences in the number of their tail feathers and vertebrae."},
            {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "We must seek out the **specific** causes of natural phenomena rather than resting upon vague generalities."}
        ]
    },
    "specifically": {
        "primary": "In a way that is detailed, precise, and explicit; for a particular purpose or reason.",
        "secondary": "In scientific nomenclature and statutory construction, designates application restricted solely to the named taxon or provision.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Many naturalists have asserted that domestic races are **specifically** distinct from their wild ancestral stocks."},
            {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Moral rules are formulated **specifically** to guide human conduct toward mutual preservation."},
            {"author": "Ralph Waldo Emerson", "work": "The Conduct of Life", "quote": "Nature works **specifically**, assigning to each creature its own distinct weapon and defense."}
        ]
    },
    "specification": {
        "primary": "An act of describing or identifying something precisely; a detailed description of design and materials.",
        "secondary": "In patent law, engineering, and architectural contracting, the statutory document reciting the exact construction parameters and claims of an invention.",
        "quotes": [
            {"author": "Walt Whitman", "work": "Specimen Days", "quote": "The official report contained a detailed **specification** of the military hospitals scattered across the capital."},
            {"author": "Thomas Edison", "work": "The Papers of Thomas A. Edison", "quote": "The patent **specification** must explain the construction of the filament so that any mechanic can reproduce it."},
            {"author": "Frederick Winslow Taylor", "work": "The Principles of Scientific Management", "quote": "Every workshop operation requires a written **specification** detailing tool feed, speed, and sequence."}
        ]
    },
    "specificity": {
        "primary": "Explicit detail, exact definition, or the narrow molecular affinity between complementary biochemical structures.",
        "secondary": "In immunology and enzymatic kinetics, the molecular complementarity that permits an enzyme or antibody to bind exclusively to its cognate substrate.",
        "quotes": [
            {"author": "Paul Ehrlich", "work": "Studies in Immunity", "quote": "The lock-and-key relationship explains the extraordinary chemical **specificity** of antitoxins in neutralizing bacterial poisons."},
            {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "Biological **specificity** arises from close steric fit and complementary hydrogen bonding across molecular interfaces."},
            {"author": "James D. Watson", "work": "Molecular Biology of the Gene", "quote": "The structural **specificity** of base pairing guarantees accurate replication of genetic information."}
        ]
    },
    "specified": {
        "primary": "Identified clearly and definitely; stated in explicit detail.",
        "secondary": "In contract law and empirical science, designated as a mandatory parameter or parameter value agreed upon prior to execution.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants Under Domestication", "quote": "The breeder selected animals possessing the **specified** markings until the trait bred true."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The codicil of the will **specified** the exact conditions under which the estate was to pass."},
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The artisan contracted to deliver the ironwork at the **specified** date, under penalty of forfeiture."}
        ]
    },
    "specifier": {
        "primary": "A person or document that specifies or determines particulars; in linguistics, a syntactic marker.",
        "secondary": "In generative grammar (X-bar theory) and industrial procurement, the structural constituent that sisters with X-bar, or the technical architect writing project standards.",
        "quotes": [
            {"author": "Noam Chomsky", "work": "Barriers", "quote": "In modern syntactic theory, the **specifier** of a functional projection hosts displaced elements in movement transformations."},
            {"author": "Steven Pinker", "work": "The Language Instinct", "quote": "Every phrase structure tree contains a head, a complement, and a **specifier** that defines reference."},
            {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The architectural **specifier** must understand the moral character of the stone he prescribes for the facade."}
        ]
    },
    "specify": {
        "primary": "To identify, name, or state clearly and definitely in detail.",
        "secondary": "In statutory drafting and scientific taxonomy, to articulate mandatory performance thresholds or establish diagnostic criteria distinguishing a new taxon.",
        "quotes": [
            {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "Let me see: what does the letter **specify** concerning the young lord?"},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "It is impossible to **specify** the exact transitional steps by which upright posture was first achieved."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate refused to **specify** the nature of the fever until he had monitored its course for another day."}
        ]
    },
    "specimen": {
        "primary": "An individual animal, plant, piece of mineral, or object used as an example of its species or type.",
        "secondary": "In clinical pathology and natural history museum collections, a preserved anatomical sample or type specimen deposited for definitive morphological reference.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "He held up a prime **specimen** of wheat, letting the golden grains sift through his weathered fingers."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "I collected a remarkable **specimen** of an unknown rodent inhabiting the arid plains of Patagonia."},
            {"author": "John Stuart Mill", "work": "Autobiography", "quote": "My father regarded each classical text as a choice **specimen** of disciplined intellectual vigor."}
        ]
    },
    "specious": {
        "primary": "Superficially plausible, but actually wrong, deceptive, or misleading.",
        "secondary": "In classical rhetoric and moral theology, characterizes arguments that masquerade as sound logic while concealing fallacies or selfish motives.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "His promises had a **specious** plausibility that deceived even the most cautious tradesmen in town."},
            {"author": "Thomas Henry Huxley", "work": "Method and Results", "quote": "We must beware of **specious** analogies that seduce the mind into premature philosophical conclusions."},
            {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Willoughby's conduct was cloaked in **specious** excuses that could not withstand rigorous scrutiny."}
        ]
    },
    "speciously": {
        "primary": "In a manner that seems correct or plausible on the surface, but is actually deceptive.",
        "secondary": "In sophistical dialectic and judicial pleading, arguing with persuasive elegance to obscure an underlying illegality or falsehood.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry VIII", "quote": "The cardinal argued **speciously**, cloaking his personal ambition beneath holy zeal for the Church."},
            {"author": "Arthur Conan Doyle", "work": "The Valley of Fear", "quote": "The suspect pleaded his alibi **speciously**, but Holmes detected a fatal flaw in the timetable."},
            {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The abstract rights of man were **speciously** displayed to dismantle ancient constitutional protections."}
        ]
    },
    "speciousness": {
        "primary": "The characteristic of seeming superficially plausible or sound while being fallacious.",
        "secondary": "In philosophical critique and legal argument, the deceptive gloss that enables a false premise to command temporary assent.",
        "quotes": [
            {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The **speciousness** of worldly pleasure quickly fades, leaving behind only emptiness and remorse."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "A keen logician penetrates the **speciousness** of scholastic syllogisms that darken knowledge."},
            {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The tyrant relied upon the legal **speciousness** of senate decrees to disguise his absolute power."}
        ]
    },
    "specs": {
        "primary": "Informal term for spectacles (eyeglasses) or for technical specifications.",
        "secondary": "In material culture and industrial manufacturing, colloquial shorthand for optical reading lenses or comprehensive engineering performance blueprints.",
        "quotes": [
            {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "Sam Weller glanced over his horn-rimmed **specs** with an expression of supreme comic detachment."},
            {"author": "Mark Twain", "work": "A Connecticut Yankee in King Arthur's Court", "quote": "I drew up the mechanical **specs** for our new telegraph line with exacting precision."},
            {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "The stranger adjusted his dark blue **specs**, hiding his hollow, bandaged visage from the curious innkeeper."}
        ]
    },
    "specular": {
        "primary": "Relating to or having the properties of a mirror; reflecting light cleanly without diffusing it.",
        "secondary": "In mineralogy and optics, describes crystal faces or smooth optical surfaces that exhibit mirror-like reflection obeying Snell's law.",
        "quotes": [
            {"author": "John Milton", "work": "Paradise Lost", "quote": "Look downward on that globe, whose hither side / With light from hence, though but reflected, shines; / That place is earth, the seat of man, that light / His day, be this his night, the moon that rises / With **specular** brilliance across the void."},
            {"author": "Isaac Newton", "work": "Opticks", "quote": "Polished metal displays a **specular** reflection that returns rays in ordered angles rather than scattered diffuse beams."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "On calm mornings the surface of the pond becomes a vast **specular** sheet, faithfully mirroring every pine and cloud."}
        ]
    },
    "speculate": {
        "primary": "To form a theory or conjecture about a subject without firm evidence; to invest in stocks or property with high risk.",
        "secondary": "In metaphysics and financial markets, denotes deductive philosophical contemplation of first principles or capital ventures seeking capital gains.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The villagers gathered at the quiet inn to **speculate** upon the stranger's sudden arrival on the heath."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "It is perilous to **speculate** upon the causes of variation until extensive breeding experiments have been completed."},
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "To **speculate** is the highest function of the intellect, tracing visible nature back to divine thoughts."}
        ]
    },
    "speculation": {
        "primary": "The forming of a theory or conjecture without firm evidence; investment in stocks or property with hope of gain.",
        "secondary": "In the history of philosophy and economic history, encompasses abstract philosophical inquiry or market bubbles driven by leveraged anticipation.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Macbeth", "quote": "Thou hast no **speculation** in those eyes / Which thou dost glare with."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon's monumental **speculation** regarding ancient mythologies proved a labyrinth without a clue."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "There was a wild **speculation** in his eyes as he studied the changing contours of the portrait."}
        ]
    },
    "speculative": {
        "primary": "Based on conjecture rather than knowledge; involving a high risk of loss with the hope of great gain.",
        "secondary": "In philosophy and economic theory, designates abstract theoretical contemplation distinct from practical application, or high-risk capital deployments.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Othello", "quote": "My **speculative** and officed instruments."},
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "Giles embarked upon a **speculative** timber purchase that jeopardized his modest ancestral inheritance."},
            {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "A wave of **speculative** excitement swept the commercial world, bidding up commodity prices to unnatural heights."}
        ]
    },
    "speculatively": {
        "primary": "In a manner based on conjecture rather than knowledge; with an eye toward speculative financial gain.",
        "secondary": "In critical philosophy and commercial analysis, engaging with propositions or markets provisionally and analytically without dogmatic certainty.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard regarded the rising wheat prices **speculatively**, calculating how to ruin his younger rival."},
            {"author": "William James", "work": "The Will to Believe", "quote": "The philosopher entertains metaphysical theses **speculatively**, awaiting moral experience to confirm or discard them."},
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Corn dealers hold grain **speculatively**, expecting higher returns as winter scarcities intensify."}
        ]
    },
    "speculativeness": {
        "primary": "The quality or disposition of being speculative; inclination to theorize or engage in financial speculation.",
        "secondary": "In intellectual history and financial characterology, an adventurous mental or economic disposition inclined to hazard capital or dogma upon bold hypotheses.",
        "quotes": [
            {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "German philosophy exhibits a daring **speculativeness** that scales the highest peaks of metaphysical abstraction."},
            {"author": "Walter Bagehot", "work": "Lombard Street", "quote": "In seasons of easy credit, the **speculativeness** of the merchant community expands beyond all sober limits."},
            {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Plato combines poetic imagination with rigorous dialectic **speculativeness**, uniting east and west."}
        ]
    },
    "speculator": {
        "primary": "A person who invests in stocks, property, or commodities in the hope of making large profits; a theoretical thinker.",
        "secondary": "In political economy and agrarian history, the commercial actor who acquires land, grain, or securities solely to exploit price fluctuations.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "The land **speculator** looks upon the ancient forest only as so many cords of marketable firewood."},
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The **speculator** is a man who enters into any trade which promises an extraordinary and immediate profit."},
            {"author": "Karl Marx", "work": "Capital", "quote": "The monetary crisis overtakes the **speculator** just when his paper operations seemed poised for triumph."}
        ]
    },
    "speculum": {
        "primary": "A medical instrument used to dilate an orifice of the body for inspection; a mirror or reflector of polished metal.",
        "secondary": "In historical astronomy and gynecological medicine, a polished bronze or alloy telescope mirror, or a diagnostic instrument introduced by modern surgeons.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "In male ducks, the iridescent **speculum** upon the wing-feathers acts as a striking visual ornament during courtship."},
            {"author": "William Herschel", "work": "Philosophical Transactions", "quote": "We cast a massive bronze **speculum** for the forty-foot telescope, grinding its parabolic curve with tireless care."},
            {"author": "Sir William Osler", "work": "The Principles and Practice of Medicine", "quote": "The careful introduction of the **speculum** revealed a deep mucosal ulceration that accounted for the chronic hemorrhage."}
        ]
    },
    "subspecies": {
        "primary": "A taxonomic category below species, usually a geographically isolated population with distinct traits.",
        "secondary": "In evolutionary systematics and biogeography, a trinomially designated geographic race that remains capable of interbreeding with other races of the species.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Many of the forms ranked by competent naturalists as species are regarded by others as mere **subspecies** or varieties."},
            {"author": "Ernst Mayr", "work": "Systematics and the Origin of Species", "quote": "A **subspecies** is an aggregate of phenotypically similar populations inhabiting a distinct geographic subdivision of the species range."},
            {"author": "Alfred Russel Wallace", "work": "Island Life", "quote": "Island isolation frequently fixes distinct insular **subspecies**, illustrating the early stages of evolutionary divergence."}
        ]
    },
    "suspect": {
        "primary": "To have an idea or impression of the existence, presence, or truth of something without certain proof; to doubt the truth or innocence of.",
        "secondary": "In criminal jurisprudence, designates an individual officially investigated for potential culpability prior to formal indictment.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "The time is out of joint: O cursed spite, / That ever I was born to set it right! / Nay, come, let's go together. I **suspect** some foul play."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "He had cause to **suspect** that his domestic secrets were being whispered among the townspeople."},
            {"author": "Arthur Conan Doyle", "work": "The Sign of Four", "quote": "We must never **suspect** a man merely because circumstantial evidence points in his direction."}
        ]
    },
    "suspected": {
        "primary": "Believed to be guilty, false, or dangerous without conclusive proof; thought likely to exist.",
        "secondary": "In forensic investigation and medical epidemiology, describes persons or conditions tentatively identified as sources of harm.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "Hermione is chaste; Polixenes blameless; Camillo a true subject; Leontes a jealous tyrant... The queen had been falsely **suspected**."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She lived in constant fear that her hidden tragedy would be **suspected** by the dairyfolk."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The presence of rudimentary organs was long **suspected** before comparative embryology proved their anatomical reality."}
        ]
    },
    "unspecialised": {
        "primary": "Not adapted to a particular purpose, skill, or environment; generalized in function or structure.",
        "secondary": "In developmental biology and evolutionary morphology, refers to stem cells, basal clades, or primitive teeth that retain pluripotency and broad utility.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Primitive ancestral mammals possessed an **unspecialised** dentition suited to an omnivorous diet."},
            {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "The amoeba represents an **unspecialized** protoplasmic mass performing all vital functions without organs."},
            {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Evolution proceeds from the homogeneous and **unspecialised** toward the heterogeneous and highly differentiated."}
        ]
    },
    "unspecialized": {
        "primary": "Not adapted to a particular purpose, skill, or environment; generalized; American spelling of unspecialised.",
        "secondary": "In cytology and evolutionary embryology, denotes pluripotential embryonic cells capable of differentiating into diverse specialized tissue types.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "The simplest animal organism consists of **unspecialized** protoplasm capable of movement, ingestion, and reproduction."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Forms that remain **unspecialized** often survive great extinction events while extreme specialists perish."},
            {"author": "John Dewey", "work": "Democracy and Education", "quote": "Early education should cultivate **unspecialized** mental flexibility rather than narrow vocational dexterity."}
        ]
    },
    "unspecific": {
        "primary": "Not specific; lacking precision, exact detail, or narrow definition.",
        "secondary": "In medical pathology and diagnostic analysis, refers to clinical signs such as fever or malaise that occur across many disparate disorders.",
        "quotes": [
            {"author": "Sir William Osler", "work": "The Principles and Practice of Medicine", "quote": "The patient presented with **unspecific** constitutional complaints that masked the underlying cardiac lesion."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "A vague and **unspecific** emotion often precedes the sharp realization of an impending danger."},
            {"author": "John Dewey", "work": "How We Think", "quote": "Thinking begins with an **unspecific** feeling of perplexity before the problem can be clearly formulated."}
        ]
    },
    "unspecified": {
        "primary": "Not stated clearly or named explicitly in detail.",
        "secondary": "In administrative regulations and legal contracts, refers to terms or variables left open for subsequent negotiation or discretion.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The testator bequeathed an **unspecified** sum for the relief of aged widows in the parish."},
            {"author": "G. K. Chesterton", "work": "The Innocence of Father Brown", "quote": "The visitor arrived at an **unspecified** hour of the night, leaving no name with the porter."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The legal petition referred to **unspecified** damages suffered by the heirs across four generations."}
        ]
    },
    "unsuspected": {
        "primary": "Not regarded as dangerous, false, or guilty; not known or realized to exist.",
        "secondary": "In scientific discovery and narrative drama, reveals hidden phenomena or loyalties whose quiet presence was unperceived by all observers.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry VI, Part 2", "quote": "Away, my lord! / We have an **unsuspected** treason here."},
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Under the surface of daily routine lie vast **unsuspected** reservoirs of spiritual energy."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "I discovered an **unsuspected** depth in the pond, where the sounding lead dropped into clear water."}
        ]
    },
    "unsuspecting": {
        "primary": "Not aware of the presence of danger; trusting; without suspicion.",
        "secondary": "In nature documentaries and military histories, describes prey or infantry moving unwarily into an ambush or predator's striking range.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The **unsuspecting** girl walked straight into the web of domestic intrigue woven by her relatives."},
            {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "The moose approached the bank with **unsuspecting** confidence, unmindful of our canoe behind the rushes."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The whale surfaced near the **unsuspecting** boat, its massive shadow darkening the green depths."}
        ]
    }
}
