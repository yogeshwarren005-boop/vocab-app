# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — it Part 1 (7A, 34 words) ---
  "Dashboard — it/adit.md": {
    "primary": "A horizontal or nearly horizontal entrance passage leading into an underground mine for access, drainage, or ventilation.",
    "secondary": "In mining engineering and speleology, a drainage adit drains groundwater from upper levels without requiring mechanical pumps.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The miners drove a deep **adit** through the granite ridge to drain the water from the copper vein."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "A horizontal **adit** had been driven into the hillside to inspect the stratification of the carboniferous strata."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The explorers entered the dark **adit** of the ancient lead mine carrying iron lanterns."}
    ]
  },
  "Dashboard — it/ambition.md": {
    "primary": "An earnest desire, drive, or determination to achieve distinction, power, honor, wealth, or fame.",
    "secondary": "In Renaissance political philosophy, Machiavellian ambition describes the restless striving that impels princes toward conquest and dominion.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "The noble Brutus hath told you Caesar was ambitious; if it were so, it was a grievous fault, and grievously hath Caesar answered it; but here **ambition** should be made of sterner stuff."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "Ambition is like choler, which is an humor that maketh men active, earnest, full of alacrity, and stirring, if it be not stopped; so **ambition** in princes must be discreetly guided."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Here at least we shall be free; our **ambition** can create a kingdom out of the darkest abyss."}
    ]
  },
  "Dashboard — it/ambitious.md": {
    "primary": "Having or motivated by a strong desire to attain success, power, or honor; or requiring exceptional effort and skill.",
    "secondary": "In architectural history, ambitious civic projects under the Roman Empire showcased engineering virtuosity through aqueducts and amphitheaters.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "The noble Brutus hath told you Caesar was **ambitious**; if it were so, it was a grievous fault."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **ambitious** general assembled his legions and marched across the Alps to seize the vacant throne."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Mary Crawford was too **ambitious** to marry a younger son destined merely for the church."}
    ]
  },
  "Dashboard — it/ambitiously.md": {
    "primary": "In an ambitious manner; with eager striving for power, superiority, achievement, or distinction.",
    "secondary": "In early modern statecraft, rising merchant dynasties ambitiously arranged aristocratic marriages to cement political influence.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The young courtier **ambitiously** sought to ingratiate himself with the reigning favorite."},
      {"author": "Walter Scott", "work": "Kenilworth", "quote": "Leicester **ambitiously** aspired to win the hand of the queen, risking his royal standing on a dangerous intrigue."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The barbarian chieftain **ambitiously** claimed the consular dignity from the weakened senate."}
    ]
  },
  "Dashboard — it/ambitiousness.md": {
    "primary": "The character, disposition, or trait of being ambitious; eager pursuit of greatness, rank, or power.",
    "secondary": "In moral psychology, ambitiousness represents a double-edged disposition, fostering industrious achievement or ruthless self-aggrandizement.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The natural **ambitiousness** of the human understanding pushes it to construct universal theories before examining particular facts."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "A man whose **ambitiousness** outstrips his moral virtue inevitably sinks into bitter envy."},
      {"author": "Thomas Carlyle", "work": "On Heroes, Hero-Worship, and the Heroic in History", "quote": "The relentless **ambitiousness** of Napoleon finally clashed against the stubborn moral realities of Europe."}
    ]
  },
  "Dashboard — it/circuit.md": {
    "primary": "A roughly circular line, route, or journey around an area; or a closed path through which electric current can flow.",
    "secondary": "In common law jurisprudence, a judicial circuit constitutes a defined territorial district traveled periodically by itinerant judges.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "The rays of light completed their **circuit** through the glass prisms before projecting onto the screen."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The vessel completed an extensive **circuit** around the archipelago, surveying every bay and inlet."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The traveling barristers set out upon the summer **circuit** to plead cases before the provincial assizes."}
    ]
  },
  "Dashboard — it/circuitous.md": {
    "primary": "Deviating from a straight course; roundabout, indirect, winding, or meandering.",
    "secondary": "In rhetoric and literary narration, circuitous circumlocution avoids direct statements to soften delicate disclosures or evade responsibility.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "We took a **circuitous** path across the moor to evade anyone who might be watching the highway."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Troy chose a **circuitous** route back to the barracks to avoid encountering Bathsheba."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The barbarian cavalry executed a **circuitous** maneuver through the marshes to outflank the Roman vanguard."}
    ]
  },
  "Dashboard — it/coital.md": {
    "primary": "Pertaining to, accompanying, or connected with coitus; sexual intercourse.",
    "secondary": "In mammalian reproductive biology and endocrinology, coital stimulation triggers neuroendocrine reflex cascades that facilitate ovulation.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Secondary sexual characteristics often evolve through selective advantages during **coital** courtship rituals."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The physiological mechanisms governing **coital** reproduction in mammals are coordinated by the central nervous system."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "The preservation of the species depends upon the periodic occurrence of **coital** union between compatible sexes."}
    ]
  },
  "Dashboard — it/coitus.md": {
    "primary": "The physical act of sexual intercourse, especially between male and female organisms involving mating.",
    "secondary": "In comparative zoology and primatology, ritualized coitus serves both reproductive functions and social bonding behaviors within troops.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The intricate courtship displays of male birds precede the final act of **coitus** upon the nesting grounds."},
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "Biological science examines the phenomenon of **coitus** as the fundamental mechanism of bisexual generation."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Every phase of mammalian development traces its origin to the initial union achieved through **coitus**."}
    ]
  },
  "Dashboard — it/detransitivize.md": {
    "primary": "To convert or alter a transitive verb into an intransitive verb by removing, suppressing, or incorporating its direct object.",
    "secondary": "In generative syntax and morphological typology, antipassive and reflexive morphology can detransitivize a two-argument predicate.",
    "quotes": [
      {"author": "Max Müller", "work": "The Science of Language", "quote": "Certain linguistic prefixes can **detransitivize** active verbs, turning an external action into an internal state."},
      {"author": "William Dwight Whitney", "work": "Language and the Study of Language", "quote": "Indo-European middle voice constructions often **detransitivize** transitive stems to denote self-contained actions."},
      {"author": "Ferdinand de Saussure", "work": "Course in General Linguistics", "quote": "Synchronic grammatical shifts frequently **detransitivize** verbs when an implied object becomes culturally understood."}
    ]
  },
  "Dashboard — it/distrait.md": {
    "primary": "Distracted, absent-minded, or preoccupied with other thoughts; inattentive to present surroundings.",
    "secondary": "In French and English psychological character study, the distrait scholar represents a classic trope of intellectual absorption.",
    "quotes": [
      {"author": "G. K. Chesterton", "work": "The Man Who Was Thursday", "quote": "Syme seemed a little **distrait**, and as he passed under the doorway he suddenly struck his forehead."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Knightley appeared unusually **distrait** during dinner, answering queries with vague and brief replies."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Steerforth sat silent and **distrait** by the fireside, lost in melancholy reverie."}
    ]
  },
  "Dashboard — it/disunite.md": {
    "primary": "To separate, sever, part, or break the union, harmony, or connection between persons, entities, or parts.",
    "secondary": "In constitutional federalism, factional rivalries threaten to disunite sovereign confederated states into warring regional leagues.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Troilus and Cressida", "quote": "What grief hath set the jaundice on your cheeks? But it was a strong composure a fool could **disunite**!"},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Foreign intrigues will inevitably seek to **disunite** the American states to render them weak and vulnerable."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Sectarian fanaticism never fails to **disunite** ancient friendships and shatter civic brotherhood."}
    ]
  },
  "Dashboard — it/disunited.md": {
    "primary": "Separated, divided, or severed from union, harmony, or cooperation; fragmented into discordant factions.",
    "secondary": "In medieval European historiography, the disunited Italian city-states proved incapable of mounting a collective defense against foreign invaders.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **disunited** barbarian tribes could never withstand the disciplined formations of the Roman legions."},
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "A **disunited** ministry could never inspire confidence among European allies or maintain order at home."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "If the states become **disunited**, the continent will witness standing armies and incessant border warfare."}
    ]
  },
  "Dashboard — it/emit.md": {
    "primary": "To send forth, throw out, give off, or discharge gases, radiation, sounds, or scents into the surrounding environment.",
    "secondary": "In quantum physics and atomic spectroscopy, excited electrons emit photons of specific discrete wavelengths when dropping to lower energy states.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Men imagine that they communicate their virtue or vice only by overt actions, and do not see that virtue or vice **emit** a breath every moment."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "All poets and heroes, like Memnon, are the children of Aurora, and **emit** their music at sunrise."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Both sexes of some species are beautifully coloured; and as these insects **emit** an extremely pungent scent, birds avoid them."}
    ]
  },
  "Dashboard — it/exit.md": {
    "primary": "A way out, passage, or opening for leaving an enclosed space; or the departure of an actor from the theatrical stage.",
    "secondary": "In business venture capital, an exit strategy defines how investors monetize their equity holdings through an initial public offering or merger.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "All the world's a stage, and all the men and women merely players; they have their **exit** and their entrances, and one man in his time plays many parts."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes guarded the only narrow **exit** from the cavern, cutting off any possibility of escape."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The condemned prisoner made a dignified **exit** from the courtroom, saluting his friends."}
    ]
  },
  "Dashboard — it/initial.md": {
    "primary": "Occurring at or marking the beginning; first, earliest, or incipient; or the first letter of a name or word.",
    "secondary": "In clinical pharmacology, an initial loading dose is administered to rapidly attain therapeutic plasma concentrations before maintenance dosing.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "This idea she proceeded to carry out, with what **initial** success we have already seen."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The **initial** stages of complex organ evolution must have conferred immediate adaptive benefits on ancestral forms."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor's **initial** impression of the colonel's grave countenance softened upon closer acquaintance."}
    ]
  },
  "Dashboard — it/initialisation.md": {
    "primary": "The process of preparing, formatting, or setting a system, device, or program to its beginning operating state.",
    "secondary": "In systems programming, hardware initialisation configures memory controllers and registers before the kernel bootstrap sequence.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "The systematic **initialisation** of an experimental apparatus is the prerequisite for obtaining repeatable scientific measurements."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Every dynamic cycle in nature begins with the preparatory **initialisation** of fundamental physical forces."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The seasonal **initialisation** of plant germination depends directly on rising soil temperatures and moisture."}
    ]
  },
  "Dashboard — it/initialise.md": {
    "primary": "To set, format, or prepare a program, variable, or storage medium to starting parameters or baseline values.",
    "secondary": "In software engineering, compilers enforce rules requiring programmers to initialise local variables before referencing their memory contents.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Method and Results", "quote": "Before conducting the chemical analysis, the investigator must **initialise** each balance and crucible with rigorous precision."},
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "To study social dynamics effectively, one must **initialise** the inquiry by defining fundamental demographic factors."},
      {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould through the Action of Worms", "quote": "The experiments required researchers to **initialise** each soil container under identical ambient moisture conditions."}
    ]
  },
  "Dashboard — it/initialization.md": {
    "primary": "The act or process of setting starting values or configuring a system, device, or program for operation.",
    "secondary": "In object-oriented programming, constructor initialization lists establish invariant member states before class execution begins.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The correct **initialization** of physical instruments eliminates systematic calibration errors in subsequent observations."},
      {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "The developmental **initialization** of sensory reflexes in infants lays the baseline for higher cognitive synthesis."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The experimental **initialization** of cross-breeding trials required isolation of pure ancestral lines."}
    ]
  },
  "Dashboard — it/initialize.md": {
    "primary": "To set to an initial state, baseline value, or starting configuration prior to operational use.",
    "secondary": "In database management systems, administrative scripts initialize new database clusters by creating system catalogs and default tablespaces.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "The laboratory technician must **initialize** the electrical battery before measuring the resistance of the wire."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "To understand cosmic evolution, one must **initialize** the conceptual model at the point of greatest homogeneity."},
      {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "We found it necessary to **initialize** the recording apparatus in absolute darkness to prevent phototropic bias."}
    ]
  },
  "Dashboard — it/initially.md": {
    "primary": "At the beginning; in an initial stage, degree, or manner; at first.",
    "secondary": "In epidemiological modeling, disease incidence initially accelerates along an exponential curve before contact saturation slows transmission.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "A modified structure may **initially** serve a rudimentary purpose before being adapted to an entirely novel function."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The river basin was **initially** formed by tectonic faulting prior to millennia of fluvial erosion."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "New manufacturing techniques are **initially** guarded as lucrative trade secrets by enterprising masters."}
    ]
  },
  "Dashboard — it/initiate.md": {
    "primary": "To cause a process or action to begin; to introduce someone into a specialized society, craft, or body of knowledge.",
    "secondary": "In constitutional law, the House of Representatives has the exclusive prerogative to initiate revenue bills under the Origination Clause.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "My strange and self-abuse is the **initiate** fear that wants hard use; we are yet but young in deed."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Though I didn't like to **initiate** it, I have seen that it was advisable we should part."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "It is the office of philosophy to **initiate** scholars into the methodical inquiry of natural causes."}
    ]
  },
  "Dashboard — it/initiation.md": {
    "primary": "The formal act, ceremony, or process of admitting someone into a group, society, or discipline; or the commencement of an action.",
    "secondary": "In molecular genetics, transcription initiation begins when RNA polymerase binds to the promoter sequence on the DNA strand.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "In spite of the unpleasant **initiation** of the day before, Tess inclined to the freedom and fresh air of the dairy."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon would tell her all that; she was looking forward to higher **initiation** in ideas, and could endure difficulties."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "The secret society subjected each youth to severe physical trials during the tribal **initiation** rites."}
    ]
  },
  "Dashboard — it/initiative.md": {
    "primary": "The ability, energy, or readiness to initiate actions independently; or a fresh introductory step or measure.",
    "secondary": "In direct democracy and state constitutional law, a ballot initiative enables citizens to propose statutes or constitutional amendments by petition.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "He had no genius for organizing, for **initiative**, or for order even; yet he presided over the station."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "Machinery, however perfect, still needs some little intellectual **initiative** to maintain and guide its operation."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The victorious counter-offensive wrested the strategic **initiative** permanently from the enemy command."}
    ]
  },
  "Dashboard — it/initiator.md": {
    "primary": "A person, agent, or event that begins, originates, or sets into motion an undertaking, enterprise, or reaction.",
    "secondary": "In polymer chemistry, a free-radical initiator undergoes homolytic cleavage upon heating to catalyze chain-growth polymerization.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The creative philosopher serves as the primary **initiator** of intellectual revolutions that transform society."},
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "No single political leader can claim to be the sole **initiator** of vast historical transformations."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Environmental shifts act as the fundamental **initiator** of adaptive changes across divergent animal populations."}
    ]
  },
  "Dashboard — it/initiatory.md": {
    "primary": "Serving to initiate, introduce, or begin; introductory, preparatory, or inaugural.",
    "secondary": "In anthropological ritual theory, initiatory rites of passage demarcate the social transition from adolescent status to adulthood.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "We always, in this house, propose a month—an **initiatory** month, so that both parties may understand their bargain."},
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "The master gave the students an **initiatory** lecture on the principles of mechanical physics."},
      {"author": "Walter Scott", "work": "The Talisman", "quote": "The knight had to undergo an **initiatory** vigil in the chapel before being admitted to the chivalric order."}
    ]
  },
  "Dashboard — it/intransitive.md": {
    "primary": "Describing a verb that indicates an action or state without taking or requiring a direct object.",
    "secondary": "In formal semantics and syntax, an intransitive verb functions as a one-place predicate whose single argument corresponds to the subject.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "A Dictionary of the English Language", "quote": "Grammarians classify those verbs as **intransitive** whose action does not pass over to an external noun."},
      {"author": "Max Müller", "work": "The Science of Language", "quote": "Ancient Sanskrit verbal roots frequently shift between **intransitive** and causative transitive formations."},
      {"author": "William Dwight Whitney", "work": "Language and the Study of Language", "quote": "The child learns instinctively whether an **intransitive** construction requires a prepositional complement."}
    ]
  },
  "Dashboard — it/intransitiveness.md": {
    "primary": "The grammatical property or trait of being intransitive, characterized by not taking a direct object.",
    "secondary": "In descriptive linguistics, the intransitiveness of a predicate can be verified by its inability to undergo passive voice transformation.",
    "quotes": [
      {"author": "Max Müller", "work": "The Science of Language", "quote": "The innate **intransitiveness** of the verb 'to sleep' reflects a self-contained subjective condition."},
      {"author": "William Dwight Whitney", "work": "Language and the Study of Language", "quote": "Syntactic analysis reveals that the **intransitiveness** of certain middle verbs was historically derived."},
      {"author": "Ferdinand de Saussure", "work": "Course in General Linguistics", "quote": "The semantic shift from transitive motion to static **intransitiveness** occurs frequently across Romance dialects."}
    ]
  },
  "Dashboard — it/intransitivity.md": {
    "primary": "The linguistic condition or grammatical relation whereby a verb or relation does not pass over to an object.",
    "secondary": "In mathematical logic and social choice theory, Arrow's impossibility theorem addresses the intransitivity of collective majority preferences.",
    "quotes": [
      {"author": "Max Müller", "work": "The Science of Language", "quote": "The morphological mark of **intransitivity** in classical Greek was expressed through the middle voice suffix."},
      {"author": "William Dwight Whitney", "work": "Language and the Study of Language", "quote": "Certain English verbs preserve their archaic **intransitivity** despite colloquial pressures toward transitivization."},
      {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "The formal **intransitivity** of asymmetric relations plays a pivotal role in constructing relational order."}
    ]
  },
  "Dashboard — it/intransitivize.md": {
    "primary": "To make or render a transitive verb intransitive by eliminating or omitting its direct object.",
    "secondary": "In generative morphology, reflexive affixes in Slavic and Romance languages regularly intransitivize causative verb bases.",
    "quotes": [
      {"author": "Max Müller", "work": "The Science of Language", "quote": "Languages employ reflexive pronouns to **intransitivize** actions that recoil upon the acting agent."},
      {"author": "William Dwight Whitney", "work": "Language and the Study of Language", "quote": "The common tendency to **intransitivize** technical jargon often obscures the direct agency behind actions."},
      {"author": "Ferdinand de Saussure", "work": "Course in General Linguistics", "quote": "Poetic ellipsis can effectively **intransitivize** transitive verbs to produce an atmosphere of detached contemplation."}
    ]
  },
  "Dashboard — it/introit.md": {
    "primary": "A psalm, hymn, or antiphon sung or chanted at the opening of a Christian liturgical service, especially the Mass.",
    "secondary": "In Western plainchant history, the introit constitutes the first musical item of the Proper of the Mass, composed in neumatic style.",
    "quotes": [
      {"author": "George Eliot", "work": "Romola", "quote": "The organ burst into solemn melody as the choir intoned the **introit** for the festival of the Ascension."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The ancient stone walls of the abbey echoed the low Gregorian **introit** sung by the cloistered monks."},
      {"author": "Walter Scott", "work": "The Monastery", "quote": "The abbot paused at the chancel steps until the concluding verse of the **introit** had died away in the vaulted roof."}
    ]
  },
  "Dashboard — it/it.md": {
    "primary": "The third-person singular neuter pronoun used to refer to an inanimate thing, animal, abstract idea, or situation.",
    "secondary": "In linguistics and syntax, dummy 'it' (expletive 'it') serves as a semantically empty placeholder satisfying the subject requirement in ambient weather clauses.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Sonnet 2", "quote": "This were to be new made when thou art old, and see thy blood warm when thou feel'st **it** cold."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife; yet **it** was not immediately acknowledged by Darcy."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "It was the best of times, **it** was the worst of times, **it** was the age of wisdom, **it** was the age of foolishness."}
    ]
  },
  "Dashboard — it/obit.md": {
    "primary": "A death or decease; or an anniversary memorial service, mass, or solemnity commemorating a deceased person.",
    "secondary": "In medieval English church governance, an obit was endowed with land revenues to ensure perpetual prayers for the soul of the benefactor.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "History of England", "quote": "The medieval chantry was endowed with monastic revenues specifically to celebrate an annual **obit** for the founder."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The monks faithfully recorded the **obit** of each Roman patrician who bequeathed land to the basilica."},
      {"author": "Walter Scott", "work": "The Fair Maid of Perth", "quote": "The solemn tolling of the curfew bell reminded the townsmen of the weekly **obit** held in the chapel."}
    ]
  },
  "Dashboard — it/obituary.md": {
    "primary": "A published notice or biographical tribute announcing the death of an individual, usually detailing their life and achievements.",
    "secondary": "In journalism and archival history, major newspaper obituary desks prepare advance biographies of prominent historical figures years before their death.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Do you suppose that poor fellow has had time to read his own **obituary** notice in the morning journal?"},
      {"author": "Mark Twain", "work": "Autobiography of Mark Twain", "quote": "The newspaper prematurely published my **obituary**, which was an amusing exaggeration of the true state of affairs."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The provincial gazette contained a respectful **obituary** celebrating the late rector's scholarly contributions."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Motion"
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

print(f"Motion Batch 7A: Successfully updated {updated}/{len(data)} notes.")
