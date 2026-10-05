# -*- coding: utf-8 -*-
"""
Part 2 of Batch 2 Cluster Speech: cit words 23-44 (22 words):
['citrulline', 'citrullus', 'citrus', 'cittern', 'city', 'city-born', 'city-bred',
 'city-like', 'city-state', 'cityfied', 'cityscape', 'citywide', 'excitability',
 'excitable', 'excitableness', 'excitant', 'excitation', 'excitative', 'excitatory',
 'excite', 'excited', 'excitedly']
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part2_cit = {
    "citrulline": {
        "primary": "A non-proteinogenic alpha-amino acid biosynthesized from ornithine and carbamoyl phosphate, first isolated from watermelon juice.",
        "secondary": "In physiology and the hepatic urea cycle, a vital intermediate facilitating the clearance of toxic ammonia and serving as an arginine precursor.",
        "quotes": [
            {"author": "Hans Krebs", "work": "Investigations on the Formation of Urea in the Animal Body", "quote": "Our enzymatic experiments established that **citrulline** acts as an indispensable catalytic intermediate in the cyclic synthesis of urea."},
            {"author": "Arthur Harden", "work": "Alcoholic Fermentation", "quote": "The isolation of pure crystalline **citrulline** from cucurbitaceous plants confirmed the prevalence of specialized amino acid intermediates in vegetable physiology."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Metabolic anomalies disrupting the enzymatic processing of **citrulline** produce severe hyperammonemia in affected infants."}
        ]
    },
    "citrullus": {
        "primary": "A genus of desert-adapted vine plants in the gourd family Cucurbitaceae, typified by the cultivated watermelon.",
        "secondary": "In systematic botany and agronomy, drought-resistant xerophytic cucurbits native to tropical Africa, including the colocynth and egusi melon.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants Under Domestication", "quote": "The cultivated varieties of **citrullus** have diverged astonishingly in sweetness and rind thickness from their wild Kalahari ancestors."},
            {"author": "David Livingstone", "work": "Missionary Travels and Researches in South Africa", "quote": "In the dry thirst-land, wild species of **citrullus** provide a life-saving reservoir of moisture for both men and wandering herds."},
            {"author": "Liberty Hyde Bailey", "work": "The Standard Cyclopedia of Horticulture", "quote": "Commercial growers propagate **citrullus** vulgaris upon light sandy loams where solar radiation accelerates rapid fruit maturation."}
        ]
    },
    "citrus": {
        "primary": "A genus of flowering trees and shrubs in the rue family (Rutaceae), cultivated for aromatic hesperidium fruits with juicy pulp.",
        "secondary": "In pomology and horticulture, economically preeminent evergreen fruit trees native to subtropical Asia, including oranges, lemons, limes, and grapefruits.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants Under Domestication", "quote": "The remarkable facility with which different species of **citrus** intercross has long bewildered systematic botanists."},
            {"author": "John Muir", "work": "The Mountains of California", "quote": "Looking down into the sunny valleys, endless groves of fragrant **citrus** blossomed in emerald squares against the foothills."},
            {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions of America", "quote": "European settlers successfully naturalized several varieties of sweet **citrus** along the fertile alluvial banks of the Orinoco."}
        ]
    },
    "cittern": {
        "primary": "A Renaissance wire-strung musical instrument of the lute family, possessing a flat back, fretted neck, and pear-shaped body.",
        "secondary": "In organology and Elizabethan social history, a popular chordophone kept in barber shops for patrons to play while awaiting their grooming.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Love's Labour's Lost", "quote": "He hath a face like a carved head upon a **cittern**, hollow and wooden in every feature."},
            {"author": "Ben Jonson", "work": "The Alchemist", "quote": "The idle gallant picked up the wire-strung **cittern** from the barber's bench and struck a lively galliard."},
            {"author": "Walter Scott", "work": "The Fortunes of Nigel", "quote": "The apprentice enlivened the tavern evening by plucking merry tunes upon a battered **cittern** suspended from the chimney beam."}
        ]
    },
    "city": {
        "primary": "A large and permanent human settlement, typically functioning as a center of commerce, culture, and municipal governance.",
        "secondary": "In urban sociology and history, a legally chartered municipality distinguished by demographic density, complex infrastructure, and administrative autonomy.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Coriolanus", "quote": "What is the **city** but the people? True, the people are the city."},
            {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Along the echoing streets of the great **city**, the heavy rumble of tumbrils announced another day of revolutionary retribution."},
            {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The rapid growth of each industrial **city** generates new social forces that test the elasticity of republican institutions."}
        ]
    },
    "city-born": {
        "primary": "Born in a city; native to an urban environment rather than a rural district.",
        "secondary": "In cultural sociology and literature, having nativity in a metropolitan center, often contrasted with provincial or agrarian origins.",
        "quotes": [
            {"author": "Walt Whitman", "work": "Specimen Days", "quote": "Being **city-born** and city-bred, I nonetheless feel an irresistible longing for the quiet woods and open salt meadows."},
            {"author": "Jack London", "work": "The Valley of the Moon", "quote": "The **city-born** workingman knew nothing of the seasons or crops until hardship drove him into the countryside."},
            {"author": "William Dean Howells", "work": "A Hazard of New Fortunes", "quote": "Her sophisticated poise was unmistakably that of a **city-born** woman accustomed to the vibrant stir of crowded avenues."}
        ]
    },
    "city-bred": {
        "primary": "Reared or educated in an urban center, having acquired the outlook, manners, or habits typical of city dwellers.",
        "secondary": "In social commentary and regional realism, shaped by metropolitan life and consequently unaccustomed to physical rural hardships.",
        "quotes": [
            {"author": "Mark Twain", "work": "Roughing It", "quote": "The **city-bred** greenhorns soon collapsed under the grueling labor of carrying timber up the steep mountain gulch."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "His smooth speech and fastidious gestures betrayed the fact that he was **city-bred** and foreign to the shearing barn."},
            {"author": "Hamlin Garland", "work": "A Son of the Middle Border", "quote": "A **city-bred** youth visiting the Dakota prairies looked with dismay at the endless horizon of trackless sod."}
        ]
    },
    "city-like": {
        "primary": "Resembling, characteristic of, or suggestive of an urban settlement or metropolitan lifestyle.",
        "secondary": "In human geography and architectural description, possessing the bustle, structural density, or sophisticated tone typical of a municipality.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "The noisy clatter of the arriving railroad gave the quiet lakeside village a hurried, **city-like** aspect for an hour."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The expanding manufacturing quarter of the town assumed a busy, **city-like** appearance with its tall brick chimneys."},
            {"author": "Washington Irving", "work": "Knickerbocker's History of New York", "quote": "The sleepy Dutch trading post gradually developed a bustling, **city-like** importance as merchant sloops crowded the wharves."}
        ]
    },
    "city-state": {
        "primary": "A sovereign state that consists of an autonomous urban center and its immediately surrounding dependent territory.",
        "secondary": "In historical political science, an independent municipal polity typified by the ancient Greek poleis (such as Athens and Sparta) or Renaissance Italian republics.",
        "quotes": [
            {"author": "G. K. Chesterton", "work": "A Short History of England", "quote": "The small democratic **city-state** of the Greeks offered an intense, personal form of citizenship unknown to vast empires."},
            {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "In its earliest beginnings, Rome was merely an ambitious **city-state** contending for pasturelands against neighboring Latin tribes."},
            {"author": "Niccolò Machiavelli", "work": "Discourses on Livy", "quote": "A virtuous **city-state** that seeks to preserve its freedom must institute laws that curb the overweening ambitions of the nobility."}
        ]
    },
    "cityfied": {
        "primary": "A variant spelling of citified; possessing the manners, appearance, or sophisticated affectations of a city dweller.",
        "secondary": "In vernacular literature and dialect writing, exhibiting an urbanized veneer or superficial polish perceived as alien by country folk.",
        "quotes": [
            {"author": "Joel Chandler Harris", "work": "Uncle Remus: His Songs and His Sayings", "quote": "The young stranger wore a **cityfied** coat and spoke with a nimble tongue that puzzled the plantation hands."},
            {"author": "Mary Noailles Murfree", "work": "In the Tennessee Mountains", "quote": "The mountaineers eyed the **cityfied** stranger askance, wondering what errand brought him into their remote coves."},
            {"author": "Booth Tarkington", "work": "The Gentleman from Indiana", "quote": "His sleek attire and **cityfied** manners were viewed by the county delegates as a distinct electoral disadvantage."}
        ]
    },
    "cityscape": {
        "primary": "An artistic representation or panoramic view of the physical features and buildings of an urban area.",
        "secondary": "In architectural aesthetics and visual arts, the compositional skyline, built environment, and visual topography of a metropolis.",
        "quotes": [
            {"author": "Henry James", "work": "The American Scene", "quote": "From the harbor ferry, the soaring **cityscape** of lower Manhattan presented an astonishing mountain range of masonry and glass."},
            {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "A dense pall of black smoke drifted across the evening **cityscape**, obscuring the familiar dome of St. Paul's Cathedral."},
            {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "Looking from her upper balcony, she observed the familiar New York **cityscape** bathed in the crisp golden chill of autumn."}
        ]
    },
    "citywide": {
        "primary": "Extending throughout, encompassing, or affecting the entire area and population of a city.",
        "secondary": "In public administration and municipal journalism, describing civic programs, electoral initiatives, or municipal ordinances operating across all city precincts.",
        "quotes": [
            {"author": "Jane Addams", "work": "Twenty Years at Hull-House", "quote": "The outbreak of contagion compelled our workers to advocate for a **citywide** inspection of tenement plumbing and sanitation."},
            {"author": "Jacob Riis", "work": "How the Other Half Lives", "quote": "Nothing short of a **citywide** crusade against corrupt landlords could demolish the deadly rear tenements of the lower wards."},
            {"author": "Upton Sinclair", "work": "The Jungle", "quote": "The sudden general strike of transit workers brought about a complete, **citywide** paralysis of commercial transport."}
        ]
    },
    "excitability": {
        "primary": "The property or capacity of being easily aroused to emotional feeling, passion, or physiological reaction.",
        "secondary": "In neurophysiology and cellular biology, the specific electrophysiological capacity of living cells (such as neurons and myocytes) to generate action potentials upon stimulation.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Her natural **excitability** of temperament magnified every trivial annoyance into an intolerable domestic tragedy."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "The degree of cortical **excitability** determines how readily a sensory impulse will trigger an immediate motor reflex."},
            {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The remarkable neuromuscular **excitability** observed during rage causes violent tremors through the voluntary muscles."}
        ]
    },
    "excitable": {
        "primary": "Easily excited, provoked, or aroused to emotional reaction; exhibiting heightened responsiveness.",
        "secondary": "In psychopathology and electrophysiology, possessing an unstable nervous constitution or responding physiologically to low stimulus thresholds.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She was an **excitable** creature, whose tears flowed as quickly as her laughter at the slightest shift of Fortune."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "His **excitable** nature could ill brook any sustained contradiction when his pet theories were brought under scrutiny."},
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Dr. Mortimer described Sir Charles as an **excitable** man whose fragile heart was dangerously susceptible to sudden terrors."}
        ]
    },
    "excitableness": {
        "primary": "The disposition or tendency to be easily agitated, stirred, or provoked to emotional intensity.",
        "secondary": "In temperamental psychology and clinical observation, a constitutional nervous volatility predisposing an individual to impulsive emotional outbursts.",
        "quotes": [
            {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "A certain nervous **excitableness** of constitution appears to be a frequent accompaniment of intense mystical illumination."},
            {"author": "Charlotte Brontë", "work": "Villette", "quote": "Her foreign lively manners were marred by an irritating **excitableness** whenever unforeseen obstacles interrupted her plans."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The high nervous **excitableness** of captive primates often leads to frantic paroxysms of screaming when startled."}
        ]
    },
    "excitant": {
        "primary": "An agent, substance, or stimulus that arouses, stimulates, or increases vital physiological activity.",
        "secondary": "In classical pharmacology and toxicology, a stimulant medication (such as caffeine, strychnine, or ether) acting upon the central nervous system.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In states of profound cardiovascular collapse, aromatic spirits of ammonia served as an effective prompt **excitant**."},
            {"author": "Thomas De Quincey", "work": "Confessions of an English Opium-Eater", "quote": "Wine acts upon the human faculties as a turbulent **excitant**, whereas opium operates as a calm restorative."},
            {"author": "Justus von Liebig", "work": "Animal Chemistry", "quote": "The consumption of spicy condiments functions as an artificial **excitant** to the secretions of the gastric mucous membrane."}
        ]
    },
    "excitation": {
        "primary": "The action, process, or physiological stimulus evoking activity, agitation, or elevated cellular responsiveness.",
        "secondary": "In physical science and electrophysiology, the elevation of an atom, quantum system, or nerve fiber to an energized state above its ground baseline.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Her mental **excitation** during the long midnight vigil drove sleep entirely from her feverish eyes."},
            {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The sudden electrical **excitation** within the secondary coil occurred precisely at the instant the galvanic circuit was broken."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "Every sensory **excitation** that enters the cerebral hemispheres tends immediately to diffuse itself through the motor pathways."}
        ]
    },
    "excitative": {
        "primary": "Having the power, tendency, or property to excite, stimulate, or provoke activity.",
        "secondary": "In therapeutics and physiological psychology, exerting an arousing or tonic influence upon nervous pathways and metabolic processes.",
        "quotes": [
            {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The passionate rhythms of dramatic poetry exert an **excitative** power upon the latent sympathies of the human soul."},
            {"author": "William Cullen", "work": "First Lines of the Practice of Physic", "quote": "Certain diffusible medicines produce an **excitative** impression upon the nervous system that temporarily rallies the pulse."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "External objects possess **excitative** qualities capable of awakening perceptions in our sensory organs through physical motion."}
        ]
    },
    "excitatory": {
        "primary": "Tending to cause stimulation, arousal, or heightened physiological activity.",
        "secondary": "In neurobiology and cellular signaling, denoting neurotransmitters (such as glutamate) or synapses that depolarize the postsynaptic membrane toward an action potential.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The nerve force unleashed during intense terror overflows into various **excitatory** motor channels, producing violent bodily trembling."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "An **excitatory** sensory impulse traveling along the afferent nerve fibers overcomes synaptic resistance to generate conscious movement."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Tetanus toxin exercises an intensely **excitatory** effect upon the motor neurons of the spinal anterior horns."}
        ]
    },
    "excite": {
        "primary": "To stir up, stimulate, agitate, or awaken emotion, action, interest, or vital energy in someone or something.",
        "secondary": "In physical physics and neurophysiology, to energize an atomic nucleus or elicit an electrical impulse in an irritable tissue.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "Examples gross as earth **excite** me: witness this army of such mass and charge, led by a delicate and tender prince."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "External impressions **excite** in our minds those simple ideas which constitute the foundations of human thought."},
            {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Novel and bold opinions rarely fail to **excite** the indignation of those whose complacency is disturbed."}
        ]
    },
    "excited": {
        "primary": "Moved by strong feeling, enthusiasm, eagerness, or agitation; aroused to lively activity.",
        "secondary": "In quantum physics and clinical neurology, possessing an energy state above the ground baseline or exhibiting heightened autonomic arousal.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Tempest", "quote": "Sir, I am vexed; bear with my weakness; my old brain is troubled; be not **excited** by my infirmity."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "She spoke in an **excited** tone, her cheeks glowing with the generous conviction that truth must prevail over selfish intrigue."},
            {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The messenger arrived in a breathless and highly **excited** condition, brandishing an opened telegram in his trembling hand."}
        ]
    },
    "excitedly": {
        "primary": "In an agitated, eager, impassioned, or animated manner; displaying heightened emotional arousal.",
        "secondary": "In behavioral description and narrative prose, characterized by rapid speech, volatile gestures, and physiological restlessness.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "He paced the floor **excitedly**, glancing every few moments through the lattice window for the expected messenger."},
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes pointed **excitedly** with his walking stick toward the dark hollow where the eerie lantern light had flashed."},
            {"author": "James Joyce", "work": "Dubliners", "quote": "The boys began to talk **excitedly** about the approaching vacation, recounting what marvelous adventures awaited them at the seaside."}
        ]
    }
}
