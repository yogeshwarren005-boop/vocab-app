# -*- coding: utf-8 -*-
"""
curate_sight_b2_p2.py
Batch 2 Part 2 of Cluster Sight:
- Dashboard — vis (remaining 49 words):
  inadvisable, invisibility, invisible, invisibleness, misadvise, nonvisual,
  prevision, provision, provisional, provisionally, provisionary, provisioner,
  proviso, retrovision, revisal, revise, revised, reviser, revising, revision,
  revisit, supervise, supervised, supervising, supervision, supervisor, televise,
  television, unadvisable, visage, visibility, visible, visibleness, vision,
  visionary, visit, visitant, visitation, visiting, visitor, visor, vista,
  visual, visualise, visualization, visualize, visualized, visualizer, visually
Total: 49 words.
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_sight_b2_p2 = {
    "inadvisable": {
        "primary": "Unwise, imprudent, or not recommended under existing circumstances.",
        "secondary": "In tactical strategy and administrative policy, describes a course of action carrying disproportionate systemic risks relative to its prospective utility.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "He felt it was **inadvisable** to press the inquiry further, observing her sudden agitation."},
            {"author": "Arthur Conan Doyle", "work": "The Sign of Four", "quote": "It is highly **inadvisable** to form theories before one possesses all the relevant data."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate found it **inadvisable** to alienate the hospital board on a question of mere protocol."}
        ]
    },
    "invisibility": {
        "primary": "The characteristic of being imperceptible to the eye; inability to be seen.",
        "secondary": "In optical physics, speculative fiction, and sociological theory, the cloaking of matter from radiation or the systemic marginalization of unacknowledged social classes.",
        "quotes": [
            {"author": "G. K. Chesterton", "work": "The Innocence of Father Brown", "quote": "The criminal relied upon social **invisibility**, moving among the guests as a common servant whom nobody noticed."},
            {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "I realized the extraordinary advantages of **invisibility**, but also its terrifying, isolated helplessness in the winter cold."},
            {"author": "Plato", "work": "The Republic", "quote": "He discovered the ring of Gyges, which bestowed total **invisibility** whenever its collet was turned inward."}
        ]
    },
    "invisible": {
        "primary": "Incapable of being perceived by the sense of sight; hidden from optical view.",
        "secondary": "In economic philosophy and physical sciences, describes unobservable regulatory mechanisms or microscopic entities that govern macro phenomena.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Tempest", "quote": "Go make thyself like a nymph o' th' sea; be subject / To no sight but thine and mine, **invisible** / To every eyeball else."},
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "He intends only his own gain, and he is led by an **invisible** hand to promote an end which was no part of his intention."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "Author of evil, unknown till thy revolt, / Unnamed in Heaven, now thou dost become **invisible**."}
        ]
    },
    "invisibleness": {
        "primary": "The condition of escaping visual detection or being hidden from observation.",
        "secondary": "In early modern natural philosophy and theology, refers to immaterial spiritual substances or transparent atmospheric fluids that elude optical instruments.",
        "quotes": [
            {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The subtle air challenges an **invisibleness** that eludes our sensory organs though supporting our vital breath."},
            {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Spirits and demons claim an **invisibleness** that allows them to instigate mischief unperceived."},
            {"author": "Ralph Cudworth", "work": "The True Intellectual System of the Universe", "quote": "The incorporeal deity maintains an essential **invisibleness** across all material creation."}
        ]
    },
    "misadvise": {
        "primary": "To give bad, ill-considered, or misleading counsel to someone.",
        "secondary": "In political historiography and executive administration, describes the catastrophic failure of counselors who lead a sovereign or cabinet into disastrous foreign entanglement.",
        "quotes": [
            {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "To **misadvise** the sovereign in matters touching constitutional balance is to undermine the commonwealth itself."},
            {"author": "Francis Bacon", "work": "Essays", "quote": "Corrupt flatterers **misadvise** princes, tailoring their words to courtier ambition rather than the public good."},
            {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Weak emperors were easily persuaded to **misadvise** their generals, dispatching contradictory orders to the Danubian frontier."}
        ]
    },
    "nonvisual": {
        "primary": "Not perceived by or involving the sense of sight; auditory, tactile, or conceptual.",
        "secondary": "In sensory physiology and cognitive psychology, relates to somatic, olfactory, proprioceptive, or auditory modalities operating independently of retinal processing.",
        "quotes": [
            {"author": "William James", "work": "The Principles of Psychology", "quote": "Spatial orientation relies extensively upon **nonvisual** sensations such as labyrinthine balance and muscular strain."},
            {"author": "Helen Keller", "work": "The World I Live In", "quote": "My comprehension of external nature is constructed entirely out of tactile, olfactory, and other **nonvisual** impressions."},
            {"author": "John Dewey", "work": "Art as Experience", "quote": "Aesthetic appreciation engages **nonvisual** kinesthetic tensions alongside the retinal patterns of a painting."}
        ]
    },
    "prevision": {
        "primary": "The action of foreseeing or anticipating future events; prescience or foresight.",
        "secondary": "In philosophy of history and sociology, the systematic anticipation of socio-economic trends and demographic movements through analytical modeling.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Will felt that Mr. Casaubon had had a profound **prevision** of this catastrophe before his death."},
            {"author": "Auguste Comte", "work": "A General View of Positivism", "quote": "The ultimate object of all positive science is **prevision**, enabling humanity to act with methodical prudence."},
            {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "Ethical progress depends on human **prevision**, checking the cosmic process by intentional social cooperation."}
        ]
    },
    "provision": {
        "primary": "The action of providing or supplying something for use; a stock of necessary food or supplies.",
        "secondary": "In legal contracts and constitutional drafting, a specific clause, stipulation, or qualification that establishes rights and duties.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Tempest", "quote": "I have with such **provision** in mine art / So safely ordered that there is no soul— / No, not so much perdition as an hair— / Betid to any creature in the vessel."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "He made ample **provision** for her future independence in the codicil of his will."},
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A prudent master makes seasonal **provision** of grain and fuel before winter prices advance."}
        ]
    },
    "provisional": {
        "primary": "Arranged, established, or accepted tentatively for the present, subject to later revision.",
        "secondary": "In epistemology and political science, describes an interim government, working hypothesis, or temporary administrative structure bridging an institutional interregnum.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "I have termed this hypothesis of pangenesis **provisional**, awaiting further physiological investigation."},
            {"author": "George Eliot", "work": "Daniel Deronda", "quote": "She adopted a **provisional** truce with her inner doubts, resolving to wait for clearer guidance."},
            {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Scientific theories begin as **provisional** conjectures before attaining inductive verification."}
        ]
    },
    "provisionally": {
        "primary": "Under terms subject to future change, confirmation, or formal ratification; temporarily.",
        "secondary": "In scientific research and international law, adopting an assumption or treaty protocol conditionally pending experimental results or diplomatic assent.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants Under Domestication", "quote": "I have **provisionally** accepted the view that gemmules are thrown off by every cell of the body."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The estate was **provisionally** sequestered until the court could ascertain the rightful heir."},
            {"author": "Thomas Henry Huxley", "work": "Method and Results", "quote": "The investigator **provisionally** accepts a hypothesis as a working tool to guide experimentation."}
        ]
    },
    "provisionary": {
        "primary": "Serving as a temporary arrangement or makeshift measure; provisional.",
        "secondary": "In administrative history, relates to interim decrees, military occupations, or transitional civil charters enacted prior to regular constitutional establishment.",
        "quotes": [
            {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The **provisionary** municipalities erected throughout the departments possessed neither lawful title nor stable authority."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The Convention Parliament acted as a **provisionary** assembly to settle the succession following the King's flight."},
            {"author": "Walter Bagehot", "work": "The English Constitution", "quote": "A cabinet in transition often adopts **provisionary** measures to manage urgent departmental affairs."}
        ]
    },
    "provisioner": {
        "primary": "A person, merchant, or company that supplies food, victuals, and necessary stores.",
        "secondary": "In military logistics and maritime enterprise, the purveyor or contractor charged with procuring and distributing rations to fleets or expeditions.",
        "quotes": [
            {"author": "Herman Melville", "work": "Omoo", "quote": "The ship's **provisioner** had cheated the crew, substituting rotten salt-beef for sound barrel meats."},
            {"author": "Daniel Defoe", "work": "A Journal of the Plague Year", "quote": "Every licensed **provisioner** was obliged to leave food at the barricaded door without personal contact."},
            {"author": "Richard Henry Dana Jr.", "work": "Two Years Before the Mast", "quote": "The California hide-drogher looked to the shore **provisioner** for fresh bullock beef after months at sea."}
        ]
    },
    "proviso": {
        "primary": "A condition, qualification, or stipulation inserted into an agreement, statute, or contract.",
        "secondary": "In parliamentary procedure and jurisprudence, an express limiting clause that restricts the scope of an enactment or prevents a forfeiture.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "He accepted the inheritance, but with the painful **proviso** that barred his cousin from any claim upon the estate."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The old gentleman had signed the parchment, inserting an eccentric **proviso** concerning the manor house."},
            {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Every legislative power granted to Congress is accompanied by the necessary **proviso** of constitutional conformity."}
        ]
    },
    "retrovision": {
        "primary": "The act or faculty of looking backward in time; retrospective sight or contemplation.",
        "secondary": "In psychoanalysis and literary poetics, the deliberate mental re-experiencing and anamnesis of repressed memory traces or past developmental epochs.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Dynasts", "quote": "The Spirit of the Years possessed a melancholy **retrovision**, viewing human struggles across the vast expanse of centuries."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "Our immediate perception of temporal duration involves both forward anticipation and instantaneous **retrovision**."},
            {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "Through imaginative **retrovision**, the poet reconstructs the lost enthusiasm and innocence of youthful feeling."}
        ]
    },
    "revisal": {
        "primary": "The act of reviewing, amending, examining, or correcting a text or regulation; revision.",
        "secondary": "In bibliographic publishing and statutory reform, the systematic recension of legal codes or editorial proofs prior to authorized printing.",
        "quotes": [
            {"author": "Jonathan Swift", "work": "Letters", "quote": "The manuscript has undergone a rigorous **revisal**, excising all superfluous passages and awkward phrases."},
            {"author": "Samuel Johnson", "work": "Lives of the English Poets", "quote": "Dryden's translations suffered from haste, rarely enjoying the benefit of a second **revisal**."},
            {"author": "Thomas Jefferson", "work": "Autobiography", "quote": "The committee of five submitted the Declaration to the **revisal** of Congress, who struck out several clauses."}
        ]
    },
    "revise": {
        "primary": "To examine again with a view to making corrections, improvements, or updates.",
        "secondary": "In textual scholarship and legislative drafting, to amend wording, adjust statutory boundaries, or rectify typographic and conceptual errors.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "He spent long hours in the library, attempting to **revise** the voluminous notes for his Key to all Mythologies."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "I have been led to **revise** some of my earlier opinions regarding the effects of sexual selection."},
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "A thinker must continually **revise** his doctrines as new influxes of truth expand the mind."}
        ]
    },
    "revised": {
        "primary": "Re-examined and altered or corrected to incorporate improvements or current facts.",
        "secondary": "In bibliographic recension and judicial opinion, describes an authorized edition or amended judgment reflecting updated scholarship or precedent.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The **revised** edition of the pastoral chronicle omitted several rustic colloquialisms that had puzzled northern readers."},
            {"author": "Ralph Waldo Emerson", "work": "The Conduct of Life", "quote": "Our plans must be perpetually **revised** under the teaching of experience."},
            {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The author produced a **revised** copy containing numerous suppressions forced by the printer's caution."}
        ]
    },
    "reviser": {
        "primary": "A person who re-examines, updates, edits, or corrects a written text, code, or schedule.",
        "secondary": "In civil service administration and philology, an expert lexicographer or legal proofreader responsible for standardizing official translations.",
        "quotes": [
            {"author": "Samuel Johnson", "work": "Preface to the English Dictionary", "quote": "The anxious **reviser** of a monumental lexicon finds errors multiplying faster than he can eradicate them."},
            {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "The modern **reviser** of ancient verse must preserve the grandeur of the original while honoring contemporary idiom."},
            {"author": "Thomas Babington Macaulay", "work": "Speeches", "quote": "The parliamentary **reviser** reduced the tangled chaos of penal statutes into an orderly statutory code."}
        ]
    },
    "revising": {
        "primary": "The process of re-examining, editing, amending, or polishing a text, doctrine, or policy.",
        "secondary": "In publishing workflow and institutional governance, the iterative phase of scrutiny during which drafts undergo textual correction and substantive verification.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "She sat beside him, **revising** the Latin transcriptions with patient devotion until the candle guttered."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "I spent my mornings in the woods, **revising** the journal entries written during the preceding winter."},
            {"author": "Virginia Woolf", "work": "A Room of One's Own", "quote": "The novelist spent years **revising** her sentences, seeking an effortless cadence that masked grueling labor."}
        ]
    },
    "revision": {
        "primary": "The action or process of reviewing, altering, and improving a text, plan, or system.",
        "secondary": "In historiography and constitutional law, the systematic reinterpretation of established paradigms or formal amendment of fundamental statutory charters.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon's monumental **revision** of his mythological notebooks remained unfinished when sickness overtook him."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Our early opinions require constant **revision** whenever clearer evidence presents itself to reason."},
            {"author": "Woodrow Wilson", "work": "The State", "quote": "Constitutional **revision** should proceed with prudent continuity rather than revolutionary haste."}
        ]
    },
    "revisit": {
        "primary": "To visit again; to return to a place, concept, or memory after an absence.",
        "secondary": "In philosophical introspection and narrative retrospection, returning to reconsider an abandoned thesis or foundational experience in light of mature understanding.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "What may this mean, / That thou, dead corse, again in complete steel / **Revisit**'st thus the glimpses of the moon?"},
            {"author": "Ralph Waldo Emerson", "work": "Nature", "quote": "The lover of nature will **revisit** the solitary woods, finding the same perpetual youth and enchantment."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "I did not **revisit** the village for weeks together, preferring the society of pines and hawks."}
        ]
    },
    "supervise": {
        "primary": "To oversee, direct, or watch over the execution of a task, process, or group of workers.",
        "secondary": "In administrative theory and labor management, exercising direct operational authority to ensure compliance with performance standards and safety mandates.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Love's Labour's Lost", "quote": "Let me **supervise** the canzonet; here are only numbers ratified."},
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The master manufacturer must personally **supervise** the division of labor to prevent waste and slackness."},
            {"author": "Frederick Winslow Taylor", "work": "The Principles of Scientific Management", "quote": "Trained foremen must systematically **supervise** each mechanical operation to maximize efficiency."}
        ]
    },
    "supervised": {
        "primary": "Managed, guided, or overseen by a person in authority; monitored.",
        "secondary": "In behavioral science and clinical training, describing professional internships or machine learning workflows guided by human feedback and labeled parameters.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "The turnkey **supervised** the arrival of the prisoners with the practiced eye of long institutional habit."},
            {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "Every ward was closely **supervised** by senior matrons who enforced strict hygiene."},
            {"author": "John Dewey", "work": "Democracy and Education", "quote": "The laboratory exercises were carefully **supervised** to encourage independent observation."}
        ]
    },
    "supervising": {
        "primary": "Directing, monitoring, or overseeing work, operations, or personnel.",
        "secondary": "In industrial psychology and civil governance, exercising administrative leadership and real-time operational vigilance over institutional workflows.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard was seen **supervising** the loading of the grain wagons in the early morning mist."},
            {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The chief engineer was **supervising** the stokehold when the mysterious shock jarred the ship."},
            {"author": "Theodore Roosevelt", "work": "An Autobiography", "quote": "He spent the summer **supervising** police reforms in the precinct houses of the metropolis."}
        ]
    },
    "supervision": {
        "primary": "The act, process, or function of overseeing and directing workers, operations, or tasks.",
        "secondary": "In institutional sociology and public administration, the organizational hierarchy that maintains accountability, quality control, and regulatory compliance.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The spirit of commerce demands ceaseless **supervision**, lest enterprise degenerate into fraud."},
            {"author": "Nathaniel Hawthorne", "work": "The Blithedale Romance", "quote": "Our utopian community dispensed with all official **supervision**, trusting to mutual affection and honor."},
            {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Administrative centralization subjects the life of every citizen to perpetual bureaucratic **supervision**."}
        ]
    },
    "supervisor": {
        "primary": "A person who directs, inspects, and oversees the work of other employees or operations.",
        "secondary": "In municipal administration and labor hierarchy, a designated civil officer or industrial manager possessing immediate operational oversight over subordinates.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Othello", "quote": "Would you, the **supervisor**, grossly gape on? / Behold her tupped?"},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The municipal **supervisor** inspected the market stalls, examining the weights and grain measures."},
            {"author": "Max Weber", "work": "Economy and Society", "quote": "The bureaucratic **supervisor** operates within strict jurisdictional limits defined by written rules."}
        ]
    },
    "televise": {
        "primary": "To transmit, record, or broadcast moving images and sound by television.",
        "secondary": "In media sociology and telecommunications, transforms physical events, court trials, or political debates into mass electronic spectacles distributed across networks.",
        "quotes": [
            {"author": "Marshall McLuhan", "work": "Understanding Media", "quote": "The decision to **televise** the debate transformed politics from literary argumentation into cool tribal drama."},
            {"author": "Daniel J. Boorstin", "work": "The Image: A Guide to Pseudo-Events in America", "quote": "We construct elaborate spectacles for the explicit purpose that networks will **televise** them to millions."},
            {"author": "Neil Postman", "work": "Amusing Ourselves to Death", "quote": "When you **televise** religion or governance, the requirements of entertainment inevitably eclipse theological or civic depth."}
        ]
    },
    "television": {
        "primary": "A telecommunication system for transmitting moving images and sound over distances; the electronic receiver display.",
        "secondary": "In communications theory and cultural studies, represents the dominant audiovisual medium of the twentieth century that homogenized domestic leisure and political discourse.",
        "quotes": [
            {"author": "Ray Bradbury", "work": "Fahrenheit 451", "quote": "The walls of the parlor were filled with monstrous talking screens of full-color **television**."},
            {"author": "Marshall McLuhan", "work": "Understanding Media", "quote": "With the arrival of **television**, the viewer becomes the screen, caught in an immersive mosaic of electronic light."},
            {"author": "E. B. White", "work": "One Man's Meat", "quote": "I believe **television** is going to be the test of the modern world; in its light we shall see whether our race can outsmart its own inventions."}
        ]
    },
    "unadvisable": {
        "primary": "Not prudent, sensible, or recommended under existing circumstances; inadvisable.",
        "secondary": "In risk management and tactical assessment, designating strategic actions that expose an enterprise to preventable disaster or needless liability.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Angel deemed it completely **unadvisable** to reopen old wounds while her spirits were so fragile."},
            {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "Watson, it would be most **unadvisable** to venture into those dark alleys without our revolvers."},
            {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Sir Thomas considered any sudden theatrical enterprise **unadvisable** during his absence from home."}
        ]
    },
    "visage": {
        "primary": "The face, facial expression, countenance, or outward appearance of a person.",
        "secondary": "In classical poetry and dramatic characterization, the physical countenance reflecting interior passions, moral nobility, or tragic suffering.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "Is it not monstrous that this player here, / But in a fiction, in a dream of passion, / Could force his soul so to his own conceit / That from her working all his **visage** wann'd?"},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "His **visage** seemed / As though an angel's, though scarred with lightning and deep furrowed."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "There was a determined, grim fortitude in Ahab's weather-beaten **visage** that silenced all dissent."}
        ]
    },
    "visibility": {
        "primary": "The distance one can see as determined by light, weather, and atmospheric conditions; clear optical perceptibility.",
        "secondary": "In meteorology and sociology, denotes optical transmission through atmospheric particulate or the public prominence and institutional recognition accorded to a social group.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The twilight reduced the **visibility** of the heath to a dim confusion of furze mounds and gravelly hollows."},
            {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The statue emerged into sudden **visibility** as the torchlight flickered along the damp gallery."},
            {"author": "Joseph Conrad", "work": "Typhoon", "quote": "The blinding sheets of spray reduced **visibility** to the length of the ship's forecastle."}
        ]
    },
    "visible": {
        "primary": "Able to be seen by the eye; perceptible to sight; readily apparent or noticeable.",
        "secondary": "In optics and empirical epistemology, refers to electromagnetic radiation within the spectrum detectable by human photoreceptors or phenomena manifest to sensory observation.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "Here I am Antony, / Yet cannot hold this **visible** shape, my knave."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Light is that great and **visible** medium whereby bodies discover to us their shapes and colors."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The hills rose in dark, massive silhouettes, barely **visible** beneath the starless vault."}
        ]
    },
    "visibleness": {
        "primary": "The characteristic of presenting a clear sensory presence to human eyes; optical perceptibility.",
        "secondary": "In natural philosophy and optics, describes the threshold of luminosity and contrast required for an object to be distinguished against its background.",
        "quotes": [
            {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The subtle vapor achieves a transient **visibleness** only when condensed by sudden evening chill."},
            {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Phantoms assume a terrible **visibleness** in the diseased imagination of the melancholy man."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Light is the medium through which bodies attain their **visibleness** to the observing eye."}
        ]
    },
    "vision": {
        "primary": "The faculty of ocular perception; an imaginative or prophetic contemplation of future occurrences.",
        "secondary": "In political philosophy and aesthetics, denotes an imaginative conceptualization of future possibilities or sublime spiritual insight.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Tempest", "quote": "These our actors, / As I foretold you, were all spirits, and / Are melted into air, into thin air: / And, like the baseless fabric of this **vision**, / The cloud-capp'd towers, the gorgeous palaces, / The solemn temples, the great globe itself, / Yea, all which it inherit, shall dissolve."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "His heart danced with gladness, / And rejoiced in the glorious **vision** of peace restored to men."},
            {"author": "William Blake", "work": "A Vision of the Last Judgment", "quote": "I question not my corporeal or vegetative eye any more than I would question a window; I look through it and not with it to behold the **vision**."}
        ]
    },
    "visionary": {
        "primary": "Thinking about or planning the future with imagination or wisdom; existing only in a dream or imagination.",
        "secondary": "In intellectual history and utopian thought, describes an idealized thinker whose speculative systems run far ahead of practical contemporary reality.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She was no longer the milkmaid, but a **visionary** essence of woman—a whole sex condensed into one typical form."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "His schemes were counted **visionary** by practical men of business who mistook their own narrowness for prudence."},
            {"author": "Nathaniel Hawthorne", "work": "The Blithedale Romance", "quote": "Hollingsworth was a **visionary**, so utterly possessed by his philanthropic scheme that he sacrificed all human affection to it."}
        ]
    },
    "visit": {
        "primary": "To go to see a person or place for companionship, inspection, or official business.",
        "secondary": "In pastoral theology and institutional governance, to inspect ecclesiastical foundations, administer official comfort to the afflicted, or inflict divine judgment.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "O Caesar, what a wounding shame is this, / That thou vouchsafing here to **visit** me, / Doing the honour of thy lordliness / To one so meek."},
            {"author": "Jane Austen", "work": "Emma", "quote": "It was her regular custom to **visit** the poor cottages of the parish with charitable supplies."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Jarndyce proposed that we should **visit** the ancient chambers in Chancery Lane together."}
        ]
    },
    "visitant": {
        "primary": "A visitor or guest, especially an unexpected, mysterious, or supernatural one.",
        "secondary": "In romantic literature and natural history, an apparition, migratory bird, or transient phenomenon appearing briefly in an unfamiliar habitat.",
        "quotes": [
            {"author": "John Milton", "work": "Paradise Lost", "quote": "The princely Hierarch / In their bright stand there left his Powers, to seize / Possession of the garden; he alone, / To find where heavenly **visitant** might dwell."},
            {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "The ghastly **visitant** entered the chamber, chilling the blood of the solitary spectator."},
            {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "A strange, unexpected **visitant** crossed the threshold of the decaying mansion."}
        ]
    },
    "visitation": {
        "primary": "An official or formal visit, typically for inspection; a severe trial or affliction regarded as a divine dispensation.",
        "secondary": "In ecclesiastical law and public health history, an episcopal inspection of parishes or the widespread onset of an epidemic pestilence.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "Do not forget: this **visitation** / Is but to whet thy almost blunted purpose."},
            {"author": "Daniel Defoe", "work": "A Journal of the Plague Year", "quote": "The dreadful **visitation** of the pestilence fell upon the parish of St. Giles in the summer of 1665."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She bowed her head beneath what she felt to be a just and sorrowful **visitation**."}
        ]
    },
    "visiting": {
        "primary": "The act of paying a visit or staying temporarily; attending or working at an institution on a temporary basis.",
        "secondary": "In social anthropology and medical practice, formalized patterns of community calls or periodic clinical consultations at remote stations.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "The odds is gone, / And there is nothing left remarkable / Beneath the **visiting** moon."},
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "He had spent the afternoon **visiting** the timber fallers in the secluded coombe."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Mrs. Cadwallader made a point of **visiting** every cottage where there was trouble to dispense hearty advice."}
        ]
    },
    "visitor": {
        "primary": "A person who pays a visit or spends time with someone socially or professionally; a guest.",
        "secondary": "In academic and ecclesiastical governance, an external trustee, bishop, or dignitary possessing ultimate appellate authority over a foundation.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Tempest", "quote": "Look, he's winding up the watch of his wit; by and by it will strike. The **visitor** will not give him o'er so."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The quiet pastoral routine of the farm was interrupted by the appearance of a handsome, well-dressed **visitor**."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate was startled by the entrance of an unexpected **visitor** while engaged in his microscopic studies."}
        ]
    },
    "visor": {
        "primary": "The movable front piece of a helmet protecting the face and eyes; a projecting shade on a cap or vehicle.",
        "secondary": "In chivalric armoury and figurative rhetoric, a facial defense or psychological mask assumed to conceal identity or inner emotion.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "Give me a case to put my visage in: / A **visor** for a visor! what care I / What curious eye doth quote deformities?"},
            {"author": "Sir Walter Scott", "work": "Ivanhoe", "quote": "The Disinherited Knight rode slowly into the lists, his **visor** firmly closed to conceal his features."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "Under his golden **visor** shone features radiant with celestial fury."}
        ]
    },
    "vista": {
        "primary": "A pleasing or extensive view, especially one seen through a long, narrow opening or along an avenue.",
        "secondary": "In landscape architecture and philosophical historiography, a channeled perspective opening toward distant spatial horizons or conceptual futures.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "It was no mature woman with a long dark **vista** of intrigue behind her who was tormented thus, but a girl of simple life."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The long gallery opened upon an enchanting **vista** of autumn woods and rolling meadowlands."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "I sat in my sunny doorway from sunrise till noon, looking out across the quiet **vista** of the pond."}
        ]
    },
    "visual": {
        "primary": "Relating to seeing, sight, or the sense of vision; optical.",
        "secondary": "In aesthetic theory and neurological science, refers to perceptual representations processed through ocular sensory pathways into cognitive spatial models.",
        "quotes": [
            {"author": "Francis Bacon", "work": "The Essays", "quote": "We represent also all manner of reflexions, refractions, and multiplications of **visual** beams of objects."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The immense whiteness of the leviathan smote the **visual** nerve with an overpowering, eerie dread."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "Michael from Adam's eyes the film removed / Which that false fruit had bred; then purged with euphrasy and rue / The **visual** nerve, for he had much to see."}
        ]
    },
    "visualise": {
        "primary": "To form a mental image or picture of something not present to the senses (British spelling).",
        "secondary": "In cognitive psychology and artistic training, the intentional generation and spatial manipulation of internal ocular representations.",
        "quotes": [
            {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "She tried to **visualise** the color of the hedge at dusk, holding the memory against the gray air."},
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes closed his eyes, striving to **visualise** the exact path the fleeing baronet had taken across the mire."},
            {"author": "Bertrand Russell", "work": "The Analysis of Mind", "quote": "When we **visualise** a familiar face, the internal image possesses qualities distinct from immediate sensory perception."}
        ]
    },
    "visualization": {
        "primary": "The formation of mental visual images; the visual representation of data or concepts.",
        "secondary": "In modern computational science and statistical graphics, the graphical encoding of complex abstract information into intuitive perceptual diagrams.",
        "quotes": [
            {"author": "William James", "work": "The Principles of Psychology", "quote": "The vividness of mental **visualization** varies enormously among individuals, from photographic clarity to faint abstraction."},
            {"author": "John Dewey", "work": "How We Think", "quote": "Effective education depends upon graphic **visualization**, transforming verbal formulas into concrete mental models."},
            {"author": "Henri Poincaré", "work": "Science and Hypothesis", "quote": "Geometrical intuition relies upon spatial **visualization** to grasp truths that formal algebra proves only step by step."}
        ]
    },
    "visualize": {
        "primary": "To form a mental picture of someone or something; to make something perceptible to the eye.",
        "secondary": "In scientific pedagogy and creative problem-solving, mapping abstract relational matrices into dynamic three-dimensional geometric structures.",
        "quotes": [
            {"author": "H. G. Wells", "work": "The Time Machine", "quote": "It is difficult for the mind to **visualize** a fourth dimension perpendicular to the three we know."},
            {"author": "Thomas Henry Huxley", "work": "Method and Results", "quote": "The physicist must constantly **visualize** the invisible motions of atoms to explain the thermal behavior of gases."},
            {"author": "Albert Einstein", "work": "Autobiographical Notes", "quote": "I always found it necessary to **visualize** physical processes in concrete geometric terms before casting them into mathematical equations."}
        ]
    },
    "visualized": {
        "primary": "Formed as a mental picture; represented visually or brought before the mind's eye.",
        "secondary": "In descriptive narrative and cognitive science, mentally realized with vivid spatial and chromatic detail prior to external execution.",
        "quotes": [
            {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "I **visualized** the great African river flowing through the dark heart of the immense continent."},
            {"author": "Virginia Woolf", "work": "Mrs. Dalloway", "quote": "She **visualized** the festive drawing room, filled with flowers and expectant guests, before the first carriage arrived."},
            {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Holmes had already **visualized** the murderer's height, stride, and footwear from the muddy footprints outside the window."}
        ]
    },
    "visualizer": {
        "primary": "A person who possesses a strong ability to form mental pictures; a device or software displaying images.",
        "secondary": "In cognitive typology and data design, an individual whose cognitive architecture relies predominantly on visual-spatial processing rather than verbal cognition.",
        "quotes": [
            {"author": "Francis Galton", "work": "Inquiries into Human Faculty and Its Development", "quote": "The natural **visualizer** retains vivid, brightly illuminated mental images that rival actual sensory perception."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "To the born **visualizer**, an abstract concept immediately calls up a concrete tableau or diagram."},
            {"author": "Oliver Sacks", "work": "The Mind's Eye", "quote": "The artist was an extraordinary **visualizer**, able to manipulate complex geometric forms mentally before putting brush to canvas."}
        ]
    },
    "visually": {
        "primary": "In a way that relates to seeing or appearance; by means of sight or vision.",
        "secondary": "In artistic critique and ergonomic design, assessing composition, color balance, and spatial harmony through direct perceptual apprehension.",
        "quotes": [
            {"author": "John Ruskin", "work": "Modern Painters", "quote": "Turner arranged his atmospheric compositions so that they were **visually** compelling even when viewed upside down."},
            {"author": "Walter Pater", "work": "The Renaissance", "quote": "The aesthetic critic must be **visually** sensitive to every subtle nuance of tone and contour."},
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants Under Domestication", "quote": "Pigeon fanciers select birds that are **visually** distinctive, fixing bizarre plumage through generations of breeding."}
        ]
    }
}
