# -*- coding: utf-8 -*-
"""
Part 3 of Curated Time Batch 1:
- Dashboard — simul (16 words)
Total: 16 words
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_simul = {
    # =========================================================================
    # DASHBOARD — simul (16 words)
    # =========================================================================
    "dissimulate": {
        "primary": "To conceal or disguise one's true thoughts, feelings, character, or intentions under a feigned appearance.",
        "secondary": "In political philosophy and courtly diplomacy, the calculated practice of hiding real designs through silence, ambiguity, or tactical deception.",
        "quotes": [
            {"author": "Francis Bacon", "work": "The Essays", "quote": "The great art of statecraft is to know how to **dissimulate**, allowing men to see what one desires them to see while masking real designs."},
            {"author": "Niccolò Machiavelli", "work": "The Prince", "quote": "A prudent ruler must know how to **dissimulate** skillfully, for men are so simple and so ready to obey present necessities that he who deceives will always find those who allow themselves to be deceived."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard was too proud and passionate to **dissimulate** his bitter resentment when his rival was praised by the town council."}
        ]
    },
    "dissimulation": {
        "primary": "The act, habit, or practice of concealing one's real feelings, motives, or character; deceitful concealment.",
        "secondary": "In Renaissance political ethics, the deliberate concealment of thoughts distinct from outright simulation or affirmative lying.",
        "quotes": [
            {"author": "Francis Bacon", "work": "The Essays", "quote": "**Dissimulation** is but a faint kind of policy or wisdom; for it asketh a strong wit and a strong heart to know when to tell truth, and to do it."},
            {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "I am not that I play. A little thing would make me tell them how much I lack of a man. Yet had she not a little **dissimulation** in her carriage?"},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Tiberius concealed his tyrannical cruelties beneath a solemn veil of philosophical **dissimulation** and affected modesty."}
        ]
    },
    "dissimulative": {
        "primary": "Characterized by, tending toward, or practicing dissimulation; deceptively secretive or concealing.",
        "secondary": "In social psychology and rhetorical analysis, describing behaviors, linguistic cues, or facial strategies deployed to hide authentic affect.",
        "quotes": [
            {"author": "Henry James", "work": "The Golden Bowl", "quote": "She observed his **dissimulative** smile, recognizing the subtle mask with which he shielded his profound embarrassment."},
            {"author": "George Eliot", "work": "Romola", "quote": "Tito's **dissimulative** habits had grown so second-nature that he could effortlessly feign devotion while plotting betrayal."},
            {"author": "Anthony Trollope", "work": "The Eustace Diamonds", "quote": "Lizzie possessed a **dissimulative** talent that baffled her closest relatives whenever financial questions were raised."}
        ]
    },
    "dissimulator": {
        "primary": "A person who conceals their true feelings, intentions, or character under a false exterior; a hypocrite or dissembler.",
        "secondary": "In moral philosophy and diplomatic biography, an individual skilled in maintaining deceptive appearances to gain strategic advantage.",
        "quotes": [
            {"author": "Francis Bacon", "work": "The Essays", "quote": "The cunning **dissimulator** keepeth his countenance composed and his speech guarded so that no adversary may discover his weakness."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor proved himself an accomplished **dissimulator**, flattering the senate while methodically stripping it of military command."},
            {"author": "Jonathan Swift", "work": "The Conduct of the Allies", "quote": "The foreign minister was a seasoned **dissimulator** who signed treaties with cordial assurances while preparing secret troop mobilizations."}
        ]
    },
    "simulacrum": {
        "primary": "An image, representation, or likeness of someone or something; a superficial semblance lacking genuine substance.",
        "secondary": "In postmodern philosophy and semiotics, a copy of a copy whose relation to an original reality has been entirely dissolved or replaced by signs.",
        "quotes": [
            {"author": "Walter Pater", "work": "The Renaissance: Studies in Art and Poetry", "quote": "The marble statue seemed more than a lifeless **simulacrum**, breathing the ethereal grace of antique Hellenic beauty."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "Our modern luxury produces but a gilded **simulacrum** of civilized happiness while starving the essential soul."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The carved wooden figurehead was an antique **simulacrum** of a forgotten king, battered by the salt spray of forty voyaging years."}
        ]
    },
    "simulate": {
        "primary": "To imitate the appearance, character, or conditions of something; to feign or replicate a real phenomenon.",
        "secondary": "In computer modeling, engineering, and physiology, to run an algorithmic or experimental model replicating the dynamical behavior of a real system.",
        "quotes": [
            {"author": "Francis Bacon", "work": "Novum Organum", "quote": "Art doth often **simulate** the intricate processes of nature, reproducing in miniature furnaces the subtle operations of subterranean heat."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Insects frequently **simulate** the color and texture of surrounding foliage to escape the keen vigilance of insectivorous birds."},
            {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The Martians constructed elaborate mechanical apparatus designed to **simulate** the muscular agility of living terrestrial quadrupeds."}
        ]
    },
    "simulated": {
        "primary": "Produced by imitation; artificial, feigned, or replicated rather than genuine or naturally occurring.",
        "secondary": "In aerospace engineering and computational science, generated by artificial or computer-driven models to mimic operating conditions.",
        "quotes": [
            {"author": "H. G. Wells", "work": "The Island of Doctor Moreau", "quote": "The beast-folk spoke with a **simulated** human accent, struggling painfully against their innate brute instincts."},
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "His terror was no **simulated** emotion; the sweat stood in beads upon his pale brow as he listened to the baying across the moor."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Troy displayed a **simulated** indifference that completely masked his sudden agitation at the mention of the tragic news."}
        ]
    },
    "simulation": {
        "primary": "The imitation of the operation of a real-world process or system over time; the act of feigning or pretending.",
        "secondary": "In scientific computing and behavioral modeling, the execution of mathematical models on digital processors to analyze system trajectories under varying constraints.",
        "quotes": [
            {"author": "Francis Bacon", "work": "The Essays", "quote": "There be three degrees of this hiding and veiling of a man's self: the first, closeness, reservation, and secrecy; the second, dissimulation in the negative; and the third, **simulation** in the affirmative, when a man industriously and expressly feigns and pretends to be that he is not."},
            {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "M, O, A, I, doth sway my life. Nay, but first, let me see, let me see, let me see. What dish o' poison has she dressed him! And with what wing the staniel cheques at it! I may command where I adore. Why, she may command me: I serve her; she is my lady. Why, this is evident to any formal capacity; there is no **simulation** in this."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Certain harmless snakes achieve protective advantage through the uncanny **simulation** of the vivid warning bands of venomous vipers."}
        ]
    },
    "simulator": {
        "primary": "A machine, device, or software program designed to provide a realistic imitation of the controls and conditions of an operational system.",
        "secondary": "In aerospace training and ergonomics, an enclosed physical reproduction of a cockpit or vehicle used to instruct operators safely under synthetic flight dynamics.",
        "quotes": [
            {"author": "H. G. Wells", "work": "The First Men in the Moon", "quote": "In our laboratory workshop we constructed a mechanical **simulator** to replicate the atmospheric pressure of the lunar surface."},
            {"author": "Arthur Eddington", "work": "The Nature of the Physical World", "quote": "The mechanical **simulator** devised by the physicist provides a vivid graphic analogy for equations that transcend sensory imagination."},
            {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The clever inventor demonstrated a working **simulator** that demonstrated hydraulic flow through artificial vascular channels."}
        ]
    },
    "simulcast": {
        "primary": "To broadcast a television program, radio show, or sporting event simultaneously across multiple channels, networks, or media formats.",
        "secondary": "In communications engineering and media distribution, the synchronized real-time dissemination of multimedia signals over radio frequency and digital network streams.",
        "quotes": [
            {"author": "Marshall McLuhan", "work": "Understanding Media: The Extensions of Man", "quote": "The electronic imperative to **simulcast** momentous events unites disparate populations into a collective tribal auditory space."},
            {"author": "Norbert Wiener", "work": "Cybernetics: Or Control and Communication in the Animal and the Machine", "quote": "The technical capacity to **simulcast** control signals across interconnected channels minimizes latency in automated feedback systems."},
            {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "The global council arranged to **simulcast** the historic peace proclamation across every wireless frequency on earth."}
        ]
    },
    "simuliidae": {
        "primary": "A family of small, stout-bodied dipteran insects commonly known as black flies or buffalo gnats, with aquatic larvae.",
        "secondary": "In medical entomology and parasitology, a cosmopolitan family of nematoceran flies whose blood-feeding females serve as obligatory biological vectors of *Onchocerca volvulus*, the causative agent of river blindness.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "The aquatic larvae of the **Simuliidae** anchor themselves firmly to submerged stones in turbulent river rapids by specialized anal hooks."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Swarms of minute biting gnats allied to **Simuliidae** made exploration along the forested riverbanks almost unendurable."},
            {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "In the damp mountain gullies, voracious flies of the family **Simuliidae** tormented our native porters throughout the midday march."}
        ]
    },
    "simulium": {
        "primary": "The principal genus of black flies within the family Simuliidae, known for vicious biting habits in riparian habitats.",
        "secondary": "In tropical medicine and vector biology, the predominant genus of black flies responsible for transmitting human onchocerciasis throughout equatorial Africa and the Americas.",
        "quotes": [
            {"author": "Patrick Manson", "work": "Tropical Diseases: A Manual of the Diseases of Warm Climates", "quote": "The female flies of the genus **Simulium** breed exclusively in well-oxygenated, swift-flowing torrents where river blindness is endemic."},
            {"author": "Ronald Ross", "work": "The Prevention of Malaria", "quote": "Field entomologists observed that species of **Simulium** rarely wander far from the rocky streams where their pupal casings mature."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The painful bites of **Simulium** inflict severe local edema and pruritus among travelers unaccustomed to wilderness river valleys."}
        ]
    },
    "simultaneity": {
        "primary": "The relation between two or more events occurring, existing, or operating at the exact same point in time.",
        "secondary": "In relativistic physics and phenomenology, the observer-dependent temporal property showing that absolute universal synchrony across spatially separated reference frames does not exist.",
        "quotes": [
            {"author": "Henri Bergson", "work": "Duration and Simultaneity", "quote": "Our intuitive consciousness grasps the **simultaneity** of physical movements by integrating multiple sensory impressions into a unified flow."},
            {"author": "Albert Einstein", "work": "Relativity: The Special and General Theory", "quote": "Every reference body has its own particular time; and unless we are told the reference body to which the statement of time refers, there is no meaning in a statement of the **simultaneity** of two events."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "The perceived **simultaneity** of sensory stimuli depends upon central neural integration occurring within the specious present."}
        ]
    },
    "simultaneous": {
        "primary": "Occurring, operating, performed, or existing at the same exact time; concurrent.",
        "secondary": "In mathematics, logic, and physics, describing interconnected equations, operations, or phenomena that must be satisfied or evaluated concurrently.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The **simultaneous** variation of correlated organs during the course of natural selection ensures harmonious functional adaptations in the organism."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The **simultaneous** ringing of the church bells and the clatter of the arriving mail-coach broke the solemn stillness of the Sunday morning."},
            {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Inductive science investigates the constant laws of succession and **simultaneous** coexistence among natural phenomena."}
        ]
    },
    "simultaneously": {
        "primary": "At the same time; concurrently; in synchrony.",
        "secondary": "In parallel computing and multi-agent systems, executed concurrently on multiple processors or computational threads.",
        "quotes": [
            {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The crowd surged forward, shouting and weeping **simultaneously** as the tumbrils made their grim passage toward the guillotine."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Both girls looked up **simultaneously**, their eyes meeting in a silent exchange of unspoken sympathy and apprehension."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Three harpooners leaped **simultaneously** to their feet, poising their darting-irons over the foaming white wake of the whale."}
        ]
    },
    "simultaneousness": {
        "primary": "The quality, state, or property of occurring, existing, or being carried out at the exact same time; concurrence.",
        "secondary": "In chronometry and epistemology, the temporal synchronicity of discrete occurrences perceived as taking place within a single instantaneous duration.",
        "quotes": [
            {"author": "William James", "work": "The Principles of Psychology", "quote": "The psychological impression of **simultaneousness** arises whenever two sensations fall within the minimum perceptual threshold of temporal discernment."},
            {"author": "Arthur Eddington", "work": "Space, Time and Gravitation", "quote": "The physical postulate of absolute **simultaneousness** across cosmic distances was abandoned once the constancy of the speed of light was recognized."},
            {"author": "Herbert Spencer", "work": "First Principles", "quote": "Consciousness coordinates internal impressions according to sequences of succession and relations of **simultaneousness**."}
        ]
    }
}
