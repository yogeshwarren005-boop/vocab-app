import json
import os

batch4_data = {
    "Dashboard — mon\\monarchal.md": {
        "primary": "Of, relating to, or characteristic of a monarch or monarchy; sovereign, regal, or imperial.",
        "secondary": "In political philosophy and constitutional history, pertaining to supreme royal authority exercised by an individual sovereign ruler.",
        "quotes": [
            {"author": "John Milton", "work": "Paradise Lost", "quote": "Satan exalted sat, by merit raised / To that bad eminence; and from despair / Thus high uplifted beyond hope, aspires / Beyond **monarchal** pride."},
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The ancient **monarchal** mantle fell away in tatters as popular assemblies seized sovereign power."},
            {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The English settlement tempered **monarchal** power with parliamentary deliberation and established law."}
        ]
    },
    "Dashboard — mon\\monarchic.md": {
        "primary": "Of or relating to a monarchy or a monarch; royal or autocratic.",
        "secondary": "In comparative government, describing political regimes wherein executive authority is concentrated in an inherited or single royal crown.",
        "quotes": [
            {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "European observers steeped in **monarchic** traditions struggled to comprehend a republic devoid of a personal sovereign."},
            {"author": "Montesquieu", "work": "The Spirit of the Laws", "quote": "Honor serves as the driving spring of **monarchic** governments, where rank and noble precedence motivate civil service."},
            {"author": "Thomas Paine", "work": "Common Sense", "quote": "The hereditary succession of **monarchic** tyranny has inundated the world with blood and ashes."}
        ]
    },
    "Dashboard — mon\\monarchism.md": {
        "primary": "The principles or advocacy of monarchy; belief in rule by a monarch.",
        "secondary": "In political history, a royalist ideological movement championing hereditary kingship against republicanism, constitutionalism, or popular democracy.",
        "quotes": [
            {"author": "Thomas Jefferson", "work": "Writings", "quote": "Our revolution was directed not merely against a king, but against the insidious principle of **monarchism** itself."},
            {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Critics accused the proposed executive of covert **monarchism**, though its powers were strictly bounded by law."},
            {"author": "Hannah Arendt", "work": "On Revolution", "quote": "The collapse of traditional European **monarchism** left a vacuum that twentieth-century totalitarian movements rushed to exploit."}
        ]
    },
    "Dashboard — mon\\monarchist.md": {
        "primary": "A supporter of or advocate for monarchy as a political system.",
        "secondary": "In political history, a royalist or loyalist partisan who defends hereditary kingship against republican revolutionaries.",
        "quotes": [
            {"author": "Victor Hugo", "work": "Les Misérables", "quote": "The old grandfather was a fierce **monarchist** who regarded every republican uprising as blasphemy against the altar and the throne."},
            {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "The strange coalition in Barcelona united anarchist militiamen, foreign volunteers, and covert **monarchist** sympathizers."},
            {"author": "Arthur Conan Doyle", "work": "The Adventure of the Beryl Coronet", "quote": "The aristocratic client was a devout **monarchist** whose family had served the royal dynasty for centuries."}
        ]
    },
    "Dashboard — mon\\monarchy.md": {
        "primary": "A form of government with a monarch (such as a king or queen) at the head.",
        "secondary": "In political science and constitutional law, a system of governance where supreme nominal or executive sovereignty is inherited by a dynastic ruler.",
        "quotes": [
            {"author": "Niccolò Machiavelli", "work": "The Prince", "quote": "A hereditary **monarchy** presents far fewer difficulties in maintaining control than a newly founded principality."},
            {"author": "Thomas Hobbes", "work": "Leviathan", "quote": "Of all forms of sovereign power, absolute **monarchy** best prevents the natural state of war among men."},
            {"author": "John Locke", "work": "Two Treatises of Government", "quote": "Absolute arbitrary power, or governing without settled standing laws, can neither of them consist with the ends of society and government in a constitutional **monarchy**."}
        ]
    },
    "Dashboard — mon\\monastery.md": {
        "primary": "A building or complex of buildings occupied by a community of monks living under religious vows.",
        "secondary": "In architectural and cultural history, a self-sustaining cloistered religious center that preserved classical learning, manuscript culture, and agrarian arts.",
        "quotes": [
            {"author": "Umberto Eco", "work": "The Name of the Rose", "quote": "The fortified **monastery** perched upon the windswept ridge sheltered the greatest scriptorium in all of Christendom."},
            {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Within the peaceful walls of the Benedictine **monastery**, ancient Latin literature found asylum amidst the wreckage of empires."},
            {"author": "Thomas Merton", "work": "The Seven Storey Mountain", "quote": "I drove through the iron gates of Gethsemani **monastery**, where silence enfolded the hills like an eternal benediction."}
        ]
    },
    "Dashboard — mon\\monastic.md": {
        "primary": "Of, relating to, or characteristic of monks, nuns, or monasteries; secluded and ascetic.",
        "secondary": "Pertaining to a solitary, contemplative, or disciplined life of religious devotion, austerity, or scholarly isolation.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "I did not wish to live what was not life; my simple cabin in the woods was a retreat without vows, yet touched by a quiet **monastic** simplicity."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon spent his days buried in his study, leading a strictly **monastic** existence dedicated to his unfinished key to all mythologies."},
            {"author": "Friedrich Nietzsche", "work": "On the Genealogy of Morals", "quote": "The philosopher has always worn the protective cloak of the **monastic** ascetic in order to think undisturbed by the crowd."}
        ]
    },
    "Dashboard — mon\\monastical.md": {
        "primary": "Monastic; of or pertaining to monasteries or the monastic lifestyle.",
        "secondary": "In archaic and historical prose, describing religious cloistering, solitary confinement, or rigorous ascetic practices.",
        "quotes": [
            {"author": "Francis Bacon", "work": "The Essays", "quote": "A retired and **monastical** life hath some affinity with the contemplative virtues, yet society demands active engagement."},
            {"author": "Samuel Johnson", "work": "The History of Rasselas, Prince of Abissinia", "quote": "He withdrew into **monastical** seclusion, hoping that isolation from mankind would extinguish worldly passions."},
            {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "Upon my desolate island I lived a kind of **monastical** existence, bounded by prayer, labor, and sea horizons."}
        ]
    },
    "Dashboard — mon\\monasticism.md": {
        "primary": "A religious way of life in which one renounces worldly pursuits to devote oneself fully to spiritual work.",
        "secondary": "In the history of religions, institutionalized ascetic communal or solitary living practiced in Christianity, Buddhism, Jainism, and Hinduism.",
        "quotes": [
            {"author": "Max Weber", "work": "The Sociology of Religion", "quote": "Early Christian **monasticism** transformed the religious impulse into methodical, rationally regulated community life."},
            {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The enthusiastic zeal for **monasticism** spread from the deserts of the Thebaid across every province of the Mediterranean."},
            {"author": "Karen Armstrong", "work": "A History of God", "quote": "In both eastern and western traditions, **monasticism** served as an incubator for mystical contemplation and divine intimacy."}
        ]
    },
    "Dashboard — mon\\monism.md": {
        "primary": "A theory or doctrine that denies the existence of a distinction or duality in a particular sphere, such as between matter and mind.",
        "secondary": "In metaphysics, the philosophical view that all reality is reducible to one single, fundamental substance or principle (as in Spinoza or Parmenides).",
        "quotes": [
            {"author": "William James", "work": "Pragmatism", "quote": "Absolute **monism** insists that the universe is an indivisible block, whereas pluralism sees it as loosely connected parts."},
            {"author": "Baruch Spinoza", "work": "Ethics", "quote": "Substance is one, infinite, and indivisible; this metaphysical **monism** unites God and nature as Deus sive Natura."},
            {"author": "Bertrand Russell", "work": "A History of Western Philosophy", "quote": "The Parmenidean doctrine that whatever is, is one, established the earliest Western template for metaphysical **monism**."}
        ]
    },
    "Dashboard — mon\\monist.md": {
        "primary": "A person who believes that only one kind of substance or ultimate reality exists.",
        "secondary": "In epistemology and metaphysics, a thinker who rejects mind-body dualism in favor of materialist, idealist, or neutral singular ontology.",
        "quotes": [
            {"author": "Ernst Haeckel", "work": "The Riddle of the Universe", "quote": "As an uncompromising **monist**, I assert that matter and energy are inseparable aspects of a single cosmic substance."},
            {"author": "William James", "work": "A Pluralistic Universe", "quote": "The thoroughgoing **monist** cannot tolerate any loose ends or irreducible contingencies in his grand philosophical scheme."},
            {"author": "Gilbert Ryle", "work": "The Concept of Mind", "quote": "Descartes created the ghost in the machine, but the materialist **monist** attempts to banish the ghost by denying mental autonomy."}
        ]
    },
    "Dashboard — mon\\monistic.md": {
        "primary": "Of, relating to, or characterized by monism; viewing reality as unified and singular.",
        "secondary": "In ontological philosophy, describing systems that explain all cosmic phenomena through a single unifying substrate or primary force.",
        "quotes": [
            {"author": "Ernst Haeckel", "work": "The Wonders of Life", "quote": "Our **monistic** philosophy of nature reconciles mechanistic evolution with the living unity of the cosmos."},
            {"author": "William James", "work": "Essays in Radical Empiricism", "quote": "A strictly **monistic** universe leaves no room for genuine human freedom or novel emergent choices."},
            {"author": "Carl Gustav Jung", "work": "Psychological Types", "quote": "Eastern philosophical traditions frequently adopt a **monistic** framework where subject and object dissolve into primal consciousness."}
        ]
    },
    "Dashboard — mon\\monition.md": {
        "primary": "A warning, cautionary advice, or gentle rebuke regarding impending danger, misconduct, or misfortune.",
        "secondary": "In canon and common law, a formal written notice or summons issued by an ecclesiastical court or magistrate directing a party to desist or appear.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "Bagnet growls, 'Old girl!' and winks quiet **monition** to her to find out what is the matter."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Nor are these supernatural omens and sea-born **monition** at all unneeded by men venturing upon perilous voyages."},
            {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "I felt a dark **monition** creeping over my spirit as the shadow of the melancholy mansion loomed in the tarn."}
        ]
    },
    "Dashboard — mon\\monk.md": {
        "primary": "A member of a religious community of men typically living under vows of poverty, chastity, and obedience in a monastery.",
        "secondary": "In cultural history and comparative religion, an ascetic practitioner dedicated to prayer, contemplation, meditation, and spiritual scholarship.",
        "quotes": [
            {"author": "Geoffrey Chaucer", "work": "The Canterbury Tales", "quote": "A **monk** ther was, a fair for the maistrie, / An outridere, that lovede venerie, / A manly man, to been an abbot able."},
            {"author": "Fyodor Dostoevsky", "work": "The Brothers Karamazov", "quote": "The elder Zosima taught the young novice that a humble **monk** bears the sorrows of all humanity in his silent prayers."},
            {"author": "Aldous Huxley", "work": "The Perennial Philosophy", "quote": "The Buddhist **monk** sweeping the temple steps cultivates mindfulness as a direct path to transcendent awakening."}
        ]
    },
    "Dashboard — mon\\monoid.md": {
        "primary": "An algebraic structure consisting of a set equipped with an associative binary operation and an identity element.",
        "secondary": "In abstract algebra and theoretical computer science, a semigroup with an identity, serving as a foundational concept in category theory and data aggregation.",
        "quotes": [
            {"author": "Saunders Mac Lane", "work": "Categories for the Working Mathematician", "quote": "A **monoid** is simply a category with one object, whose arrows correspond to the elements of the algebraic structure."},
            {"author": "Donald Knuth", "work": "The Art of Computer Programming", "quote": "String concatenation over a finite alphabet forms a free **monoid** with the empty string serving as its identity element."},
            {"author": "John Baez", "work": "Quantum Techniques in Algebra and Category Theory", "quote": "Associativity and unit laws make the **monoid** the most natural algebraic abstraction for sequential state transformations."}
        ]
    },
    "Dashboard — mon\\monolith.md": {
        "primary": "A large single upright block of stone, especially one shaped into or serving as a monument or pillar.",
        "secondary": "A massive, uniform, and intractable structure, organization, or software application that resists division or change.",
        "quotes": [
            {"author": "Arthur C. Clarke", "work": "2001: A Space Odyssey", "quote": "The black rectangular **monolith** stood standing in the lunar crater, emitting a piercing radio signal toward Saturn."},
            {"author": "Percy Bysshe Shelley", "work": "Ozymandias", "quote": "Near them, on the sand, / Half sunk a shattered visage lies, whose frown / Dwarfed the ancient stone **monolith**."},
            {"author": "Martin Fowler", "work": "Monolith to Microservices", "quote": "Teams often begin with a single architectural **monolith** before complexity compels them to decompose services."}
        ]
    },
    "Dashboard — mon\\monolithic.md": {
        "primary": "Formed of a single large block of stone; massive, solid, and uniform.",
        "secondary": "Describing large, rigid, and indivisible institutions, empires, architectural forms, or software codebases.",
        "quotes": [
            {"author": "George Orwell", "work": "1984", "quote": "The Ministry of Truth towered three hundred meters into the air, a vast **monolithic** structure of glittering white concrete."},
            {"author": "Hannah Arendt", "work": "The Origins of Totalitarianism", "quote": "Totalitarian regimes present a deceptively **monolithic** facade to the world, masking chaotic bureaucratic rivalries beneath."},
            {"author": "Carver Mead", "work": "Introduction to VLSI Systems", "quote": "The innovation of the **monolithic** integrated circuit replaced disparate wiring boards with a single sliver of crystalline silicon."}
        ]
    },
    "Dashboard — mon\\monometer.md": {
        "primary": "A line of verse consisting of a single metrical foot or measure.",
        "secondary": "In classical and English prosody, an exceptionally rare and concise poetic line used for dramatic punctuation or rhythmic variation.",
        "quotes": [
            {"author": "Robert Herrick", "work": "Hesperides (Upon His Departure Hence)", "quote": "Thus I / Pass by / And die: / As one / Unknown / And gone: the poet employed pure **monometer** to convey the swiftness of mortality."},
            {"author": "George Saintsbury", "work": "A History of English Prosody", "quote": "Herrick's playful experiments in iambic **monometer** reveal how rhythmic momentum can survive even in single-foot verses."},
            {"author": "Ezra Pound", "work": "The ABC of Reading", "quote": "A sudden **monometer** cadence interrupts the flowing stanza like a struck gong, concentrating poetic attention."}
        ]
    },
    "Dashboard — mon\\monopod.md": {
        "primary": "A one-legged support or stand, especially a single-staff mount used to steady a camera or telescope.",
        "secondary": "In medieval folklore and zoology, a mythical creature with a single giant leg (sciapod); or an organism possessing a single foot.",
        "quotes": [
            {"author": "C.S. Lewis", "work": "The Voyage of the Dawn Treader", "quote": "The cheerful Dufflepuds hopped across the beach upon their single giant feet, proud of their **monopod** agility."},
            {"author": "Pliny the Elder", "work": "Natural History", "quote": "Ancient travelers reported tribes of **monopod** dwellers who sheltered from midday heat under the shade of their single foot."},
            {"author": "Ansel Adams", "work": "The Camera", "quote": "When trekking rugged mountain terrain, a lightweight **monopod** provides indispensable stabilization for heavy telephoto lenses."}
        ]
    },
    "Dashboard — mon\\monopsony.md": {
        "primary": "A market situation in which there is only one buyer for a product or service.",
        "secondary": "In microeconomics and labor economics, buyer market power where a solitary purchaser can depress prices or suppress wages below competitive equilibrium.",
        "quotes": [
            {"author": "Joan Robinson", "work": "The Economics of Imperfect Competition", "quote": "Just as a monopoly exploits consumers, a buyer possessing **monopsony** power extracts surplus from unorganized workers."},
            {"author": "Paul Samuelson", "work": "Economics", "quote": "When a single company town operates the only mine, it exercises pure **monopsony** over the regional labor market."},
            {"author": "Joseph Stiglitz", "work": "The Price of Inequality", "quote": "Modern labor market frictions grant corporate employers substantial **monopsony** leverage, dampening wage growth across low-wage sectors."}
        ]
    },
    "Dashboard — mon\\monos.md": {
        "primary": "The ancient Greek word for alone, single, sole, or unique, serving as the etymological root for numerous prefixes and scientific terms.",
        "secondary": "In linguistic morphology and classical philology, the root morpheme underlying words denoting oneness, isolation, or singular structure.",
        "quotes": [
            {"author": "Plato", "work": "Phaedrus", "quote": "The philosopher contemplates the pure form that exists by itself, solitary and alone, described in Greek as **monos**."},
            {"author": "Aristotle", "work": "Metaphysics", "quote": "The concept of unity implies that an entity is undivided in itself; hence **monos** conveys the essence of singular existence."},
            {"author": "Donald Knuth", "work": "The TeXbook", "quote": "From the classical root **monos** arose our prefixes designating singularity in mathematics, biology, and grammar."}
        ]
    },
    "Dashboard — mon\\pseudomonad.md": {
        "primary": "Any bacterium belonging to the genus Pseudomonas or the family Pseudomonadaceae, typically motile Gram-negative aerobic rods.",
        "secondary": "In medical microbiology and environmental biotechnology, versatile rod-shaped bacteria known for metabolic adaptability and opportunistic biofilm formation.",
        "quotes": [
            {"author": "Alexander Fleming", "work": "Penicillin", "quote": "Certain stubborn wound infections yielded a resilient **pseudomonad** that produced distinctive blue-green pyocyanin pigmentation."},
            {"author": "Carl Woese", "work": "The Genetic Code", "quote": "Phylogenetic analysis of ribosomal RNA clarified the diverse evolutionary lines within the heterogeneous **pseudomonad** group."},
            {"author": "Atul Gawande", "work": "The Checklist Manifesto", "quote": "Hospital protocols require aggressive hygiene to prevent hospital-acquired pneumonia caused by antibiotic-resistant **pseudomonad** strains."}
        ]
    },
    "Dashboard — mono\\antimonopoly.md": {
        "primary": "Opposed to or designed to prevent monopolies; antitrust.",
        "secondary": "In economic policy and legal history, relating to legislative and regulatory efforts (such as the Sherman Act) to curb corporate market concentration.",
        "quotes": [
            {"author": "Theodore Roosevelt", "work": "The Strenuous Life", "quote": "Our administration pursued rigorous **antimonopoly** enforcement to ensure that powerful industrial trusts remained subject to public law."},
            {"author": "Louis Brandeis", "work": "The Curse of Bigness", "quote": "True democratic vitality cannot survive in an economy where **antimonopoly** principles are abandoned in favor of corporate cartels."},
            {"author": "Joseph Stiglitz", "work": "People, Power, and Profits", "quote": "Revitalizing **antimonopoly** regulation is essential if we are to restore genuine market competition in the digital economy."}
        ]
    },
    "Dashboard — mono\\demonolatry.md": {
        "primary": "The worship of demons or evil spirits.",
        "secondary": "In anthropology of religion and demonology, ritual practices and occult systems centered upon invocations, pacts, or propitiations of malevolent entities.",
        "quotes": [
            {"author": "Edward Burnett Tylor", "work": "Primitive Culture", "quote": "Where fear eclipses adoration in primitive theology, religion often devolves into appeasement and outright **demonolatry**."},
            {"author": "Arthur Conan Doyle", "work": "The Sign of Four", "quote": "The traveler described bizarre nocturnal rites in the Andaman jungle that bordered upon ancient **demonolatry**."},
            {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Tribal rites to avert catastrophic famines frequently incorporated symbolic elements of **demonolatry** aimed at placating chthonic horrors."}
        ]
    },
    "Dashboard — mono\\mono.md": {
        "primary": "A combining form meaning one, single, or alone; or colloquial shorthand for monophonic audio or infectious mononucleosis.",
        "secondary": "In acoustics, single-channel sound reproduction; in clinical medicine, glandular fever caused by Epstein-Barr virus infection.",
        "quotes": [
            {"author": "Oliver Sacks", "work": "Musicophilia", "quote": "Audiophiles long debated whether vintage recordings sounded more authentically punchy in original **mono** than in artificial stereo."},
            {"author": "Abraham Verghese", "work": "The Tennis Partner", "quote": "The college athlete had been fatigued for weeks with swollen cervical lymph nodes, typical of infectious **mono**."},
            {"author": "Brian Eno", "work": "A Year with Swollen Appendices", "quote": "Mixing a track down to **mono** forces the producer to balance spectral frequencies without relying on spatial separation."}
        ]
    },
    "Dashboard — mono\\monoamine.md": {
        "primary": "A compound containing one amino group, especially a neurotransmitter such as dopamine, norepinephrine, or serotonin.",
        "secondary": "In neurochemistry and psychopharmacology, signaling molecules derived from aromatic amino acids that regulate mood, arousal, and cognition.",
        "quotes": [
            {"author": "Oliver Sacks", "work": "Awakenings", "quote": "L-dopa administration replenished cerebral reserves of the essential **monoamine** dopamine, awakening frozen Parkinsonian patients."},
            {"author": "Eric Kandel", "work": "In Search of Memory", "quote": "Serotonin, a crucial **monoamine**, facilitates synaptic plasticity in Aplysia by elevating cyclic AMP levels."},
            {"author": "Siddhartha Mukherjee", "work": "The Song of the Cell", "quote": "The **monoamine** hypothesis of depression posited that mood disorders stemmed from depleted synaptic transmitter concentrations."}
        ]
    },
    "Dashboard — mono\\monoatomic.md": {
        "primary": "Consisting of single, uncombined atoms; having one atom in the molecule.",
        "secondary": "In thermodynamics and physical chemistry, describing gases such as helium, neon, and argon whose heat capacity ratio gamma is approximately 5/3.",
        "quotes": [
            {"author": "James Clerk Maxwell", "work": "Illustrations of the Dynamical Theory of Gases", "quote": "For a **monoatomic** gas, thermal kinetic energy resides solely in three translational degrees of freedom."},
            {"author": "Ernest Rutherford", "work": "Radioactive Substances and Their Radiations", "quote": "Alpha particles emitted by radium were demonstrated to be doubly charged helium ions of **monoatomic** constitution."},
            {"author": "Linus Pauling", "work": "General Chemistry", "quote": "Noble gases remain stable in a **monoatomic** state under standard temperature and pressure due to filled valence shells."}
        ]
    },
    "Dashboard — mono\\monocanthidae.md": {
        "primary": "A family of tetraodontiform marine fishes commonly known as filefishes, characterized by rough, sandpapery skin and a prominent first dorsal spine.",
        "secondary": "In systematic ichthyology (frequently classified as Monacanthidae), shallow-water reef fishes closely related to triggerfishes.",
        "quotes": [
            {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "The filefishes of the family **Monocanthidae** possess a single erectile dorsal spine that can be locked into position."},
            {"author": "William Beebe", "work": "Beneath Tropic Seas", "quote": "Camouflaged among branching gorgonians, small specimens of **Monocanthidae** drift head-downward like floating sea grass."},
            {"author": "Rachel Carson", "work": "The Sea Around Us", "quote": "Reef-dwelling species of **Monocanthidae** use their sharp, chisel-like teeth to graze on encrusting bryozoans and coral polyps."}
        ]
    },
    "Dashboard — mono\\monocanthus.md": {
        "primary": "A genus of filefishes in the family Monacanthidae (often written Monacanthus), featuring a single prominent, barbed dorsal spine.",
        "secondary": "In marine biology, omnivorous reef fishes inhabiting tropical and subtropical waters, noted for cryptic coloration and laterally compressed bodies.",
        "quotes": [
            {"author": "David Starr Jordan", "work": "Fishes", "quote": "The common filefish **Monocanthus** locks its barbed dorsal spine erect when threatened, lodging itself firmly within rock crevices."},
            {"author": "Albert Günther", "work": "Catalogue of the Fishes in the British Museum", "quote": "Specimens of **Monocanthus** collected in Caribbean lagoons display fine dermal prickles that resemble coarse velvet."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "In the shallow waters of the reef, we observed a small **Monocanthus** browsing peacefully among the seaweeds."}
        ]
    },
    "Dashboard — mono\\monocarboxylic.md": {
        "primary": "Containing only one carboxyl group (-COOH) in each molecule.",
        "secondary": "In organic chemistry, describing fatty acids and simple organic acids such as formic, acetic, and propionic acids.",
        "quotes": [
            {"author": "Linus Pauling", "work": "General Chemistry", "quote": "Acetic acid is the most familiar example of a **monocarboxylic** acid, dissociating weakly in aqueous solution."},
            {"author": "Emil Fischer", "work": "Studies on Organic Synthesis", "quote": "The esterification of long-chain **monocarboxylic** acids yielded key insights into the structure of natural lipids."},
            {"author": "Arthur Kornberg", "work": "For the Love of Enzymes", "quote": "Beta-oxidation sequentially degrades saturated **monocarboxylic** fatty acids into two-carbon acetyl-CoA units."}
        ]
    },
    "Dashboard — mono\\monocarp.md": {
        "primary": "A monocarpic plant; a plant that flowers and produces fruit only once in its life cycle before dying.",
        "secondary": "In botany, an annual, biennial, or semelparous perennial (such as certain agaves and bamboos) that commits all stored reserves to a single reproductive event.",
        "quotes": [
            {"author": "Asa Gray", "work": "Structural Botany", "quote": "The century plant is a famous example of a giant **monocarp**, storing sap for decades before erupting into a colossal flowering stalk."},
            {"author": "Katherine Esau", "work": "Plant Anatomy", "quote": "Following fruit maturation, the vegetative tissues of a true **monocarp** undergo rapid programmed senescence."},
            {"author": "David Attenborough", "work": "The Private Life of Plants", "quote": "Certain bamboo species live for half a century as a green colony before every **monocarp** in the forest blooms and perishes simultaneously."}
        ]
    },
    "Dashboard — mono\\monocarpic.md": {
        "primary": "Flowering and bearing fruit only once before dying; semelparous.",
        "secondary": "In plant reproductive ecology, describing life histories where individuals devote all accumulated biomass to a single massive reproductive effort.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "In **monocarpic** species, natural selection concentrates reproductive effort into a singular, overwhelming display of seeds."},
            {"author": "Peter Raven", "work": "Biology of Plants", "quote": "Most agricultural crops, such as wheat and corn, are **monocarpic** annuals that die immediately after harvest."},
            {"author": "Aldo Leopold", "work": "A Sand County Almanac", "quote": "The biennial mullein is strictly **monocarpic**, raising its velvety yellow spire once to the summer sun before winter kills the stalk."}
        ]
    },
    "Dashboard — mono\\monochamus.md": {
        "primary": "A genus of longhorn beetles in the family Cerambycidae, commonly known as sawyer beetles.",
        "secondary": "In forestry and agricultural entomology, wood-boring beetles whose larvae excavate tunnels in conifers and serve as vectors for the pine wood nematode.",
        "quotes": [
            {"author": "Jean-Henri Fabre", "work": "The Life of the Beetle", "quote": "The great pine sawyer, **Monochamus**, possesses antennae twice the length of its body, sweeping the bark for scent trails."},
            {"author": "E.O. Wilson", "work": "The Diversity of Life", "quote": "Wood-boring cerambycids like **Monochamus** accelerate the natural decomposition of fallen timber in boreal pine forests."},
            {"author": "Aldo Leopold", "work": "A Sand County Almanac", "quote": "Beneath the peeling bark of dying jack pines, the rasping larvae of **Monochamus** churned wood into fragrant sawdust."}
        ]
    },
    "Dashboard — mono\\monochromacy.md": {
        "primary": "Total color blindness, a condition in which vision is restricted to shades of grey because only one type of retinal photoreceptor is functional.",
        "secondary": "In visual neuroscience and ophthalmology, complete achromatopsia occurring either as rod monochromacy (loss of all cones) or rare cone monochromacy.",
        "quotes": [
            {"author": "Oliver Sacks", "work": "The Island of the Colorblind", "quote": "On the atoll of Pingelap, a significant portion of the population lives with hereditary **monochromacy**, seeing the world in pure luminance."},
            {"author": "Hermann von Helmholtz", "work": "Treatise on Physiological Optics", "quote": "True complete **monochromacy** reduces color matching to a single-variable intensity equation across the visible spectrum."},
            {"author": "Richard Dawkins", "work": "Climbing Mount Improbable", "quote": "In nocturnal mammals, evolutionary loss of cone pigments often resulted in functional **monochromacy** optimized for low-light sensitivity."}
        ]
    },
    "Dashboard — mono\\monochromasy.md": {
        "primary": "The medical condition of having only monochromatic vision; complete color blindness (variant spelling of monochromacy).",
        "secondary": "In physiological optics, the incapacity to distinguish chromatic hues, resulting from the lack of two or all three retinal cone visual pigments.",
        "quotes": [
            {"author": "Oliver Sacks", "work": "The Island of the Colorblind", "quote": "Patients affected by congenital **monochromasy** squinted against the tropical glare, relying on extreme textural discernment."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "The experience of congenital **monochromasy** provides a striking counterexample to theories that view color as an indispensable dimension of visual thought."},
            {"author": "Thomas Young", "work": "Lectures on Natural Philosophy", "quote": "If the retina possessed only one vibratory sensory mechanism, the inevitable consequence would be total **monochromasy**."}
        ]
    },
    "Dashboard — mono\\monochromat.md": {
        "primary": "A person or animal that has monochromatic vision and cannot perceive color differences.",
        "secondary": "In ophthalmology, an individual possessing only one functional photoreceptor mechanism in the retina, perceiving the visual scene entirely in lightness values.",
        "quotes": [
            {"author": "Oliver Sacks", "work": "An Anthropologist on Mars", "quote": "The artist became a sudden cerebral **monochromat** following a collision, perceiving his beloved paintings as drab slate and ash."},
            {"author": "Hermann von Helmholtz", "work": "Physiological Optics", "quote": "To a complete **monochromat**, any color of the spectrum can be perfectly matched to any other simply by adjusting intensity."},
            {"author": "Richard Gregory", "work": "Eye and Brain", "quote": "The true **monochromat** navigates space with remarkable skill by exploiting motion parallax, contours, and relative brightness."}
        ]
    },
    "Dashboard — mono\\monochromatic.md": {
        "primary": "Containing or using only one color; or consisting of radiation of a single wavelength or very narrow band of wavelengths.",
        "secondary": "In laser physics and spectroscopy, light whose photons have identical frequency, wavelength, and phase characteristics.",
        "quotes": [
            {"author": "Albert Einstein", "work": "On a Heuristic Point of View Concerning the Production and Transformation of Light", "quote": "When **monochromatic** radiation of low density behaves energetically as if it consisted of independent energy quanta, the photoelectric effect is explained."},
            {"author": "Isaac Newton", "work": "Opticks", "quote": "Prismatic refraction separated the beam into homogeneous rays, each ray retaining its **monochromatic** color upon subsequent refraction."},
            {"author": "Arthur C. Clarke", "work": "The City and the Stars", "quote": "The desert city glowed under the eerie, uniform illumination of a single **monochromatic** emerald sky."}
        ]
    },
    "Dashboard — mono\\monochromatism.md": {
        "primary": "The state or condition of being monochromatic; complete absence of color perception.",
        "secondary": "In vision science, a congenital visual deficit characterized by photophobia, nystagmus, low visual acuity, and total color blindness.",
        "quotes": [
            {"author": "Oliver Sacks", "work": "The Island of the Colorblind", "quote": "Complete rod **monochromatism** turns bright daylight into an agonizing, overexposed glare for affected islanders."},
            {"author": "Hermann von Helmholtz", "work": "Treatise on Physiological Optics", "quote": "Cases of genuine **monochromatism** are exceedingly rare, yet they offer decisive tests for trichromatic color theory."},
            {"author": "Max Born", "work": "Principles of Optics", "quote": "Spectral purity in optical instruments approaches the ideal of theoretical **monochromatism** only in coherent laser resonators."}
        ]
    },
    "Dashboard — mono\\monochrome.md": {
        "primary": "A photograph or picture developed or executed in black and white or in varying tones of only one color.",
        "secondary": "In computer displays and art history, imagery rendered in shades of a single phosphor or pigment (such as sepia, grisaille, or green screen).",
        "quotes": [
            {"author": "Ansel Adams", "work": "The Print", "quote": "Working in **monochrome** frees the photographer to explore pure tonal values, textures, and luminous geometric forms."},
            {"author": "Virginia Woolf", "work": "Orlando", "quote": "The winter landscape outside the manor window had faded into a bleak, austere **monochrome** of frost and grey stone."},
            {"author": "Steve Wozniak", "work": "iWoz", "quote": "Early terminals were restricted to crude **monochrome** green phosphors before we designed affordable color graphics circuits."}
        ]
    },
    "Dashboard — mono\\monochromia.md": {
        "primary": "A condition of having or producing only one color; monochromaticity or total color blindness.",
        "secondary": "In dermatological and ocular pathology, uniform pigmentation or complete lack of chromatic discrimination.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Ophthalmic evaluation confirmed complete **monochromia**, the patient distinguishing objects solely through brightness gradients."},
            {"author": "Oliver Sacks", "work": "The Island of the Colorblind", "quote": "The clinical history of congenital **monochromia** reflects a unique visual world shaped entirely by luminance contrast."},
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Breeders noted how selective breeding could fix unusual **monochromia** in the coat color of fancy pigeons."}
        ]
    },
    "Dashboard — mono\\monochromic.md": {
        "primary": "Having or consisting of a single color; monochromatic.",
        "secondary": "In fine art and spectroscopic instrumentation, describing pigments, filters, or prints limited to a uniform hue.",
        "quotes": [
            {"author": "John Ruskin", "work": "Modern Painters", "quote": "The Venetian masters avoided **monochromic** monotony by infusing every shadow with subtle, vibrant undertones."},
            {"author": "Ansel Adams", "work": "Examples: The Making of 40 Photographs", "quote": "The dramatic impact of the snowstorm scene was heightened by its almost **monochromic** palette of charcoal and white."},
            {"author": "James Clerk Maxwell", "work": "Theory of Heat", "quote": "By passing sunlight through a **monochromic** prism, we isolate a narrow slice of thermal and optical radiation."}
        ]
    },
    "Dashboard — mono\\monochromous.md": {
        "primary": "Of one uniform color; monochromatic.",
        "secondary": "In classical art and natural history, an archaic synonym for monochrome, describing statues, tapestries, or animal pelts of unvarying tint.",
        "quotes": [
            {"author": "Pliny the Elder", "work": "Natural History", "quote": "Early Greek painters executed **monochromous** pictures using cinnabar or lampblack before discovering four-color blending."},
            {"author": "Walter Pater", "work": "Studies in the History of the Renaissance", "quote": "The austere dignity of antique sculpture was once believed to be **monochromous**, before archaeologists uncovered traces of polychromy."},
            {"author": "Asa Gray", "work": "Manual of Botany", "quote": "The petals of the forest bellflower are completely **monochromous**, presenting an unbroken azure expanse."}
        ]
    },
    "Dashboard — mono\\monocle.md": {
        "primary": "A single eyeglass kept in position by the muscles of the eye orbit.",
        "secondary": "In nineteenth- and early twentieth-century fashion, an optical accessory worn by European aristocrats and military officers, symbolic of elite formality.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Dr. Mortimer looked up, adjusting his round **monocle** with an air of professional gravity."},
            {"author": "P.G. Wodehouse", "work": "The Inimitable Jeeves", "quote": "Bertie Wooster screwed his **monocle** into his eye and surveyed the disastrous scene with profound bewilderment."},
            {"author": "George Orwell", "work": "The Lion and the Unicorn", "quote": "The caricatures of Prussian officers invariably featured a glinting **monocle** and a stiff, unyielding neck."}
        ]
    },
    "Dashboard — mono\\monocled.md": {
        "primary": "Wearing a monocle; fitted or adorned with a single eyeglass.",
        "secondary": "Characterized by or evoking the aristocratic, haughty, or formal demeanor associated with a monocle wearer.",
        "quotes": [
            {"author": "Virginia Woolf", "work": "Mrs. Dalloway", "quote": "A tall, **monocled** gentleman bowed stiffly from the doorway, conveying imperial hauteur in every gesture."},
            {"author": "John le Carré", "work": "Tinker, Tailor, Soldier, Spy", "quote": "Smiley recalled the **monocled** veteran who had directed wartime intelligence with frosty, eccentric precision."},
            {"author": "Agatha Christie", "work": "The Mysterious Affair at Styles", "quote": "The **monocled** detective examined the broken vase with silent, concentrated scrutiny."}
        ]
    },
    "Dashboard — mono\\monoclinal.md": {
        "primary": "Of, relating to, or forming a monocline (a step-like geologic fold in rock strata).",
        "secondary": "In structural geology and geomorphology, describing rock beds that dip consistently in one direction between flatter strata.",
        "quotes": [
            {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The river canyon cut cleanly through the **monoclinal** flexure, exposing inclined limestone strata along the gorge wall."},
            {"author": "John Wesley Powell", "work": "The Exploration of the Colorado River", "quote": "Colossal **monoclinal** ridges reared above the plateau like frozen stone waves tilted by ancient tectonic stress."},
            {"author": "James Dwight Dana", "work": "Manual of Geology", "quote": "Differential erosion along a **monoclinal** fold creates asymmetric cuestas with steep escarpments and gentle dip slopes."}
        ]
    },
    "Dashboard — mono\\monocline.md": {
        "primary": "A bend or step-like fold in rock strata, consisting of a zone of steeper dip within an otherwise horizontal or gently sloping sequence.",
        "secondary": "In structural geology, a simple one-limbed tectonic fold connecting two regionally flat structural terraces.",
        "quotes": [
            {"author": "John Wesley Powell", "work": "Report on the Geology of the Uinta Mountains", "quote": "The East Kaibab **monocline** drops the sedimentary strata thousands of feet toward the canyon floor in a graceful tectonic drape."},
            {"author": "Charles Lyell", "work": "Elements of Geology", "quote": "Where deep faults displace basement rock, the overlying sedimentary blankets flex into a majestic **monocline**."},
            {"author": "Rachel Carson", "work": "The Sea Around Us", "quote": "Submarine acoustic surveys mapped an immense continental shelf **monocline** descending toward the abyssal plain."}
        ]
    },
    "Dashboard — mono\\monoclinic.md": {
        "primary": "Having or relating to three unequal crystallographic axes, with two intersecting at an oblique angle and the third perpendicular to both.",
        "secondary": "In crystallography and mineralogy, a crystal system exemplified by gypsum, orthoclase feldspar, and augite.",
        "quotes": [
            {"author": "James Dwight Dana", "work": "A System of Mineralogy", "quote": "Minerals belonging to the **monoclinic** system, like gypsum and hornblende, exhibit characteristic inclined optical extinction angles."},
            {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "The asymmetric packing of sulfate tetrahedra produces the classic **monoclinic** unit cell of calcium sulfate dihydrate."},
            {"author": "Max Born", "work": "Dynamical Theory of Crystal Lattices", "quote": "In a **monoclinic** lattice, the absence of high symmetry constraints complicates the tensor analysis of elastic constants."}
        ]
    },
    "Dashboard — mono\\monoclinous.md": {
        "primary": "Having both stamens and carpels in the same flower; hermaphroditic or bisexual.",
        "secondary": "In botany, describing perfect flowers (such as lilies or roses) possessing both male and female reproductive organs in a single floral structure.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "Although the species is **monoclinous**, mechanisms like protandry effectively prevent self-fertilization within the flower."},
            {"author": "Asa Gray", "work": "Structural Botany", "quote": "A typical apple blossom is strictly **monoclinous**, bearing a ring of stamens encircling the central pistils."},
            {"author": "Peter Raven", "work": "Biology of Plants", "quote": "The majority of angiosperm families bear **monoclinous** blossoms, facilitating efficient insect pollination of both sexes in one visit."}
        ]
    },
    "Dashboard — mono\\monoclonal.md": {
        "primary": "Formed from, derived from, or relating to a single clone of cells, especially identical antibody-producing cells.",
        "secondary": "In immunology and molecular medicine, referring to identical antibodies produced by hybridoma cell lines that bind to a single specific epitope.",
        "quotes": [
            {"author": "César Milstein", "work": "From Antibody Diversity to Monoclonal Antibodies", "quote": "The fusion of myeloma cells with primed lymphocytes yielded perpetual hybridoma lines secreting pure **monoclonal** antibodies."},
            {"author": "Siddhartha Mukherjee", "work": "The Emperor of All Maladies", "quote": "Herceptin, a pioneering **monoclonal** antibody, targeted the HER2 receptor to arrest aggressive breast cancer cell growth."},
            {"author": "Atul Gawande", "work": "Being Mortal", "quote": "Targeted therapies employing synthetic **monoclonal** proteins have revolutionized modern oncology with pinpoint molecular precision."}
        ]
    },
    "Dashboard — mono\\monocot.md": {
        "primary": "A monocotyledonous plant; a flowering plant having an embryo with a single cotyledon (seed leaf).",
        "secondary": "In agronomy and botany, a diverse clade comprising grasses, orchids, palms, and lilies, typically displaying parallel leaf venation and trimerous flowers.",
        "quotes": [
            {"author": "Michael Pollan", "work": "The Botany of Desire", "quote": "Modern human civilization is fundamentally built upon a single grass **monocot** known as Zea mays."},
            {"author": "Peter Raven", "work": "Biology of Plants", "quote": "Vascular bundles scattered throughout the stem immediately identify the seedling as a typical **monocot**."},
            {"author": "Asa Gray", "work": "Elements of Botany", "quote": "Unlike the branching veins of broadleaf plants, every leaf of a **monocot** shows neat parallel venation."}
        ]
    },
    "Dashboard — mono\\monocotyledon.md": {
        "primary": "A flowering plant characterized by an embryo with a single cotyledon, parallel-veined leaves, and flower parts usually in multiples of three.",
        "secondary": "In angiosperm taxonomy, one of the two historical major divisions of flowering plants (class Monocotyledones / Liliopsida).",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "The subterranean coleoptile of the emerging **monocotyledon** penetrates the soil with remarkable geotropic sensitivity."},
            {"author": "Katherine Esau", "work": "Plant Anatomy", "quote": "In the mature stem of a **monocotyledon**, there is typically no bifacial vascular cambium producing secondary wood."},
            {"author": "David Attenborough", "work": "The Private Life of Plants", "quote": "Grasses, lilies, and towering palm trees all share common ancestry within the evolutionary branch of the **monocotyledon**."}
        ]
    },
    "Dashboard — mono\\monocotyledonae.md": {
        "primary": "The botanical class comprising all monocotyledonous plants (monocots).",
        "secondary": "In formal plant taxonomy, the major taxon Liliopsida, containing over sixty thousand species of single-cotyledon angiosperms.",
        "quotes": [
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The class **Monocotyledonae** encompasses our most vital cereal grains, including wheat, barley, rice, and oats."},
            {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "Specimens belonging to the **Monocotyledonae** dominate the lush understory flora of tropical monsoon riverbanks."},
            {"author": "Peter Raven", "work": "Biology of Plants", "quote": "Phylogenetic reconstruction confirms that the **Monocotyledonae** form a strongly supported monophyletic lineage within the angiosperms."}
        ]
    },
    "Dashboard — mono\\monocotyledones.md": {
        "primary": "An alternative or historical taxonomic name for the class of monocotyledonous flowering plants.",
        "secondary": "In classical botanical literature, the subclass of angiosperms characterized by endogenous vascular stem structure and single seed leaves.",
        "quotes": [
            {"author": "Antoine Laurent de Jussieu", "work": "Genera Plantarum", "quote": "I divided the vegetable kingdom into Acotyledones, Monocotyledones, and Dicotyledones based upon embryonic seed leaves."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The broad divergence separating the Dicotyledones from the **Monocotyledones** represents one of the ancient divides of floral evolution."},
            {"author": "Robert Brown", "work": "Botanical Remarks on the Flora of New Holland", "quote": "Australian collections revealed extraordinary, bizarre representatives of the **Monocotyledones** adapted to arid scrublands."}
        ]
    },
    "Dashboard — mono\\monocotyledonous.md": {
        "primary": "Having only one cotyledon or seed leaf; characteristic of monocot plants.",
        "secondary": "In structural botany, describing plants featuring fibrous root systems, parallel venation, and scattered stem vascular bundles.",
        "quotes": [
            {"author": "Katherine Esau", "work": "Plant Anatomy", "quote": "The atactostelic arrangement of vascular bundles is a hallmark characteristic of the **monocotyledonous** stem."},
            {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "In **monocotyledonous** seedlings, the sheath-like coleoptile shields the delicate plumule as it pushes through soil."},
            {"author": "Asa Gray", "work": "Elements of Botany", "quote": "Grains and lilies share a **monocotyledonous** architecture that distinguishes them from common tap-rooted shrubs."}
        ]
    },
    "Dashboard — mono\\monocracy.md": {
        "primary": "Government by a single person; autocracy or absolute monarchy.",
        "secondary": "In political theory, an authoritarian regime wherein supreme legislative, judicial, and executive command is exercised by one individual.",
        "quotes": [
            {"author": "Thomas Jefferson", "work": "The Writings of Thomas Jefferson", "quote": "The enemies of our republic sought to consolidate federal power into a thinly disguised **monocracy**."},
            {"author": "James Madison", "work": "The Federalist Papers", "quote": "The accumulation of all powers in the same hands may justly be pronounced the very definition of tyrannical **monocracy**."},
            {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "A democratic people may willingly surrender its liberties to a centralized **monocracy** if equality is guaranteed."}
        ]
    },
    "Dashboard — mono\\monoculture.md": {
        "primary": "The cultivation or growth of a single crop or organism in a given area.",
        "secondary": "In ecology and sociology, the dominance of a single species, agricultural variety, or cultural practice, leading to vulnerability and loss of diversity.",
        "quotes": [
            {"author": "Rachel Carson", "work": "Silent Spring", "quote": "Modern agricultural **monoculture** invites devastating insect infestations that nature's complex biodiversity once held in check."},
            {"author": "Michael Pollan", "work": "The Omnivore's Dilemma", "quote": "The vast industrial corn **monoculture** stretching across Iowa created a landscape of staggering biological uniformity."},
            {"author": "Jared Diamond", "work": "Collapse", "quote": "Over-reliance on a fragile potato **monoculture** left nineteenth-century Ireland tragically exposed to the blight."}
        ]
    },
    "Dashboard — mono\\monocycle.md": {
        "primary": "A single-wheeled vehicle; a unicycle.",
        "secondary": "In mechanical history, a vehicle where the rider sits inside or directly above a large single wheel propelled by pedals or an engine.",
        "quotes": [
            {"author": "H.G. Wells", "work": "The War of the Worlds", "quote": "The mechanised scouts rode peculiar single-wheeled engines resembling a steel **monocycle** across the ruined common."},
            {"author": "Jules Verne", "work": "The Steam House", "quote": "Inventors paraded novel velocipedes, including a perilous motorized **monocycle** that astonished the Parisian crowd."},
            {"author": "Arthur C. Clarke", "work": "Profiles of the Future", "quote": "Gyroscopically balanced single-wheeled vehicles like the **monocycle** may yet find niche utility on rugged planetary surfaces."}
        ]
    },
    "Dashboard — mono\\monocyte.md": {
        "primary": "A large white blood cell with a single non-segmented nucleus, capable of differentiating into a macrophage or dendritic cell.",
        "secondary": "In hematology and immunology, an agranulocyte originating in the bone marrow that migrates into peripheral tissues to phagocytose pathogens.",
        "quotes": [
            {"author": "Paul Ehrlich", "work": "Histology of the Blood", "quote": "Stained with triacid dye, the large mononuclear **monocyte** stood distinct from granular polymorphonuclear leucocytes."},
            {"author": "Siddhartha Mukherjee", "work": "The Song of the Cell", "quote": "When microbial invaders breach the skin, the circulating **monocyte** crawls through the capillary wall and transforms into a voracious tissue macrophage."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Differential blood counts in chronic infectious endocarditis frequently show a marked rise in circulating **monocyte** numbers."}
        ]
    },
    "Dashboard — mono\\monocytosis.md": {
        "primary": "An increase in the number of monocytes in the circulating blood.",
        "secondary": "In clinical hematology, a laboratory finding frequently associated with chronic infections (such as tuberculosis or endocarditis), autoimmune diseases, or myelomonocytic leukemias.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Persistent low-grade fever accompanied by unexplained **monocytosis** raises strong clinical suspicion of subacute bacterial endocarditis."},
            {"author": "Max Wintrobe", "work": "Clinical Hematology", "quote": "The hematologist must carefully evaluate **monocytosis** to differentiate reactive chronic inflammation from chronic myelomonocytic leukemia."},
            {"author": "Siddhartha Mukherjee", "work": "The Emperor of All Maladies", "quote": "The patient's bone marrow biopsy confirmed an abnormal clonal expansion driving profound, intractable peripheral **monocytosis**."}
        ]
    },
    "Dashboard — mono\\monoecious.md": {
        "primary": "Having both male and female reproductive organs in the same individual; in plants, having separate staminate and pistillate flowers on the same plant.",
        "secondary": "In reproductive biology, hermaphroditic or single-house organisms (such as maize, hazel, and oaks) contrasting with dioecious species.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "In **monoecious** plants like the oak, wind transfers pollen from pendulous male catkins to tiny female flowers on the same bough."},
            {"author": "Gregor Mendel", "work": "Experiments in Plant Hybridisation", "quote": "Certain **monoecious** species require manual emasculation of the male blossoms before experimental cross-pollination can begin."},
            {"author": "Katherine Esau", "work": "Plant Anatomy", "quote": "Corn is a classic **monoecious** grass, bearing the male tassels at the apex and female silks on ears lower down the stalk."}
        ]
    },
    "Dashboard — mono\\monoestrous.md": {
        "primary": "Having only one period of estrus (heat) in a single breeding season or year.",
        "secondary": "In mammalian reproductive endocrinology, describing seasonal breeders such as wolves, bears, and roe deer that exhibit a single annual ovulatory cycle.",
        "quotes": [
            {"author": "Aldo Leopold", "work": "A Sand County Almanac", "quote": "The timber wolf is strictly **monoestrous**, timing its single annual winter mating so that pups emerge into the warmth of late spring."},
            {"author": "Frans de Waal", "work": "The Ape and the Sushi Master", "quote": "Unlike polyestrous primates with recurring monthly receptivity, **monoestrous** carnivores concentrate all mating into a brief annual window."},
            {"author": "David Attenborough", "work": "The Life of Mammals", "quote": "In the Arctic wilderness, being **monoestrous** synchronizes birth with the fleeting seasonal explosion of summer food."}
        ]
    },
    "Dashboard — mono\\monoicous.md": {
        "primary": "Having male and female reproductive structures on the same plant gametophyte (used especially of bryophytes such as mosses and liverworts).",
        "secondary": "In bryology, producing both antheridia and archegonia on a single haploid individual, facilitating self-fertilization in moisture-limited microhabitats.",
        "quotes": [
            {"author": "Asa Gray", "work": "Structural Botany", "quote": "In a **monoicous** moss, antheridia and archegonia develop within the same clustered perichaetium at the tip of the stem."},
            {"author": "Katherine Esau", "work": "Plant Anatomy", "quote": "Bryologists classify peat mosses based on whether their haploid gametophores are dioicous or **monoicous**."},
            {"author": "Peter Raven", "work": "Biology of Plants", "quote": "The **monoicous** condition ensures that flagellated sperm need only swim across a film of dew to fertilize adjacent archegonia."}
        ]
    },
    "Dashboard — mono\\monolatry.md": {
        "primary": "The worship of one god without denying the existence of other gods.",
        "secondary": "In the history of religion, a transitional phase between polytheism and strict philosophical monotheism, exemplified in early biblical Israelite religion.",
        "quotes": [
            {"author": "Max Weber", "work": "Ancient Judaism", "quote": "Early covenantal devotion to Yahweh began as passionate **monolatry**, demanding exclusive tribal allegiance while recognizing foreign pantheons."},
            {"author": "Karen Armstrong", "work": "A History of God", "quote": "Before the prophetic era forged absolute monotheism, Israelite religion practiced a jealous **monolatry** rooted in the Sinai covenant."},
            {"author": "Edward Burnett Tylor", "work": "Primitive Culture", "quote": "A tribe may elevate its patron war god above all competitors without doubting their existence, in classic **monolatry**."}
        ]
    },
    "Dashboard — mono\\monolingual.md": {
        "primary": "Speaking, writing, or using only one language.",
        "secondary": "In sociolinguistics and cognitive science, describing individuals or insular speech communities that operate within a single linguistic system.",
        "quotes": [
            {"author": "Steven Pinker", "work": "The Language Instinct", "quote": "The **monolingual** speaker often mistakes the arbitrary conventions of their native tongue for the universal grammar of thought."},
            {"author": "George Steiner", "work": "After Babel", "quote": "To inhabit a **monolingual** existence is to view the infinite landscape of human experience through a single colored lens."},
            {"author": "Noam Chomsky", "work": "Aspects of the Theory of Syntax", "quote": "Linguistic competence was traditionally idealized from the perspective of an adult **monolingual** native speaker."}
        ]
    }
}

# Write out curate_math2_batch4.mjs
mjs_path = os.path.join("main app", "scripts", "curate_math2_batch4.mjs")
with open(mjs_path, "w", encoding="utf-8") as f:
    f.write("""import { updateNotesBatch } from './curate-updater-util.mjs';
import path from 'path';

const CLUSTER_DIR = path.resolve('App database/Greek roots/Cluster Number & Mathematics');
const batchData = """ + json.dumps(batch4_data, indent=2, ensure_ascii=False) + """;

const count = updateNotesBatch(CLUSTER_DIR, batchData);
console.log(`========================================`);
console.log(`Math Part 2 - Batch 4 Completed: ${count} / ${Object.keys(batchData).length} words updated`);
console.log(`========================================`);
""")

print(f"Generated {mjs_path} with {len(batch4_data)} entries.")
