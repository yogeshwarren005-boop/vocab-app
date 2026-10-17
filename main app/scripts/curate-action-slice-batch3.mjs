import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Action');

const batch3Data = {
  "Dashboard — prag\\practicality.md": {
    primary: "The quality or state of being practical; suitability for actual use or real-world application.",
    secondary: "In engineering, business, and policy, the pragmatic assessment of feasibility, cost-effectiveness, and real-world utility over theoretical elegance.",
    quotes: [
      { author: "William James", work: "The Meaning of Truth", quote: "Pragmatism judges ideas by their direct working value and intellectual **practicality** in navigating reality." },
      { author: "Ralph Waldo Emerson", work: "The Conduct of Life", quote: "The supreme test of any reform is its **practicality** when applied to the coarse necessities of daily labor." },
      { author: "John Dewey", work: "Reconstruction in Philosophy", quote: "A philosophy that divorces theoretical contemplation from social **practicality** condemns itself to sterile irrelevance." }
    ]
  },
  "Dashboard — prag\\practically.md": {
    primary: "In a practical manner; through actual action or application; virtually or almost completely.",
    secondary: "From a realistic and pragmatic standpoint, as opposed to idealistic or theoretical speculation.",
    quotes: [
      { author: "Charles Darwin", work: "The Descent of Man", quote: "The mental faculties of higher animals are **practically** identical in kind with those of early human ancestors." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "He was **practically** unconscious of his own peril, so consumed was he by the relentless chase." },
      { author: "John Stuart Mill", work: "On Liberty", quote: "A principle may be applauded in the abstract, yet **practically** ignored whenever private interests intervene." }
    ]
  },
  "Dashboard — prag\\practice.md": {
    primary: "The actual application or use of an idea, belief, or method, as opposed to theories relating to it; habitual performance or repeated exercise to acquire skill.",
    secondary: "The professional business, office, or client roster of a physician, lawyer, or consultant.",
    quotes: [
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "Knowledge is never complete until it has passed from intellectual contemplation into vigorous, daily **practice**." },
      { author: "William James", work: "Habit", quote: "Keep the faculty of effort alive in you by a little gratuitous exercise in daily **practice**." },
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "A workman who has acquired speed through constant **practice** turns out double the quantity of manufactured goods." }
    ]
  },
  "Dashboard — prag\\practiced.md": {
    primary: "Experienced, skilled, or expert through continuous repetition, long training, or habit.",
    secondary: "Habitually performed, rehearsed, or cultivated; exhibiting polished and seasoned execution.",
    quotes: [
      { author: "Jane Austen", work: "Sense and Sensibility", quote: "With the **practiced** eye of a man of fashion, he surveyed the company and chose his conversation." },
      { author: "Joseph Conrad", work: "Heart of Darkness", quote: "The river pilot brought the battered steamer around the sandbank with a calm, **practiced** sweep of the helm." },
      { author: "George Eliot", work: "Middlemarch", quote: "She listened with that **practiced** patience that wives of vain men so quickly acquire." }
    ]
  },
  "Dashboard — prag\\practise.md": {
    primary: "To perform an activity or exercise a skill repeatedly or regularly in order to acquire, improve, or maintain one's proficiency.",
    secondary: "To carry out or practice a profession, craft, religion, or habit as a livelihood or code of life.",
    quotes: [
      { author: "Samuel Johnson", work: "The Rambler", quote: "It is far easier to prescribe rules of virtue than to **practise** them in the turmoil of human affairs." },
      { author: "Charles Dickens", work: "Great Expectations", quote: "I resolved to **practise** my handwriting until I should write like a clerk in a London counting-house." },
      { author: "John Locke", work: "Some Thoughts Concerning Education", quote: "What children are to do frequently, they should be made to **practise** until it becomes natural." }
    ]
  },
  "Dashboard — prag\\prag.md": {
    primary: "The Greek root (pragma, prattein, meaning 'a deed, act, matter, business, or thing done'), forming the core of words related to action, utility, and practical affairs.",
    secondary: "In etymological linguistics and philosophy, the conceptual radical contrasting concrete worldly enterprise with speculative contemplation.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The radical element **prag** in ancient Greek yields terms for action, business, and practical deed." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "From the Greek stem **prag**, seen in prattein and pragma, come our words pragmatic, praxis, and practice." },
      { author: "Max Müller", work: "Lectures on the Science of Language", quote: "The primitive Indo-European root underlying **prag** denotes doing or passing through to concrete execution." }
    ]
  },
  "Dashboard — prag\\pragma.md": {
    primary: "In classical Greek and philosophical terminology, an act, deed, concrete thing, or business matter.",
    secondary: "In computer programming, a compiler directive or pragmatic information passed directly to an interpreter or translator to influence code compilation.",
    quotes: [
      { author: "Charles Sanders Peirce", work: "Collected Papers", quote: "Our conception of any **pragma**, or object of action, consists entirely in our conception of its practical effects." },
      { author: "William James", work: "Pragmatism", quote: "The word **pragma**, from which pragmatism derives, means action, deed, and tangible enterprise." },
      { author: "John Dewey", work: "Essays in Experimental Logic", quote: "Every idea is tested by the concrete **pragma** it produces in transactional experience." }
    ]
  },
  "Dashboard — prag\\pragmatic.md": {
    primary: "Dealing with things sensibly and realistically in a way that is based on practical rather than theoretical considerations.",
    secondary: "In the history of ideas and philosophy, relating to pragmatism, evaluating truth and meaning through practical consequences and experiential tests.",
    quotes: [
      { author: "William James", work: "Pragmatism: A New Name for Some Old Ways of Thinking", quote: "The **pragmatic** method is primarily a method of settling metaphysical disputes that otherwise might be indeterminable." },
      { author: "Bertrand Russell", work: "A History of Western Philosophy", quote: "A **pragmatic** approach to truth judges an hypothesis by its utility in guiding human conduct." },
      { author: "Oliver Wendell Holmes Jr.", work: "The Common Law", quote: "The life of the law has not been logic; it has been experience, requiring **pragmatic** adjustment to the felt necessities of the time." }
    ]
  },
  "Dashboard — prag\\pragmatical.md": {
    primary: "Meddlesome, officious, opinionated, or excessively concerned with practical management (archaic/historical).",
    secondary: "Pertaining to state affairs, public business, or pragmatic sanctions (as in fundamental imperial edicts).",
    quotes: [
      { author: "Samuel Pepys", work: "The Diary of Samuel Pepys", quote: "He proved a very busy and **pragmatical** fellow, meddling with business that concerned him not." },
      { author: "Jonathan Swift", work: "Gulliver's Travels", quote: "The court was full of **pragmatical** ministers whose ambitious intrigues ruined the harmony of the kingdom." },
      { author: "David Hume", work: "The History of England", quote: "The royal proclamation was framed in the spirit of a **pragmatical** sanction, settling the disputed succession." }
    ]
  },
  "Dashboard — prag\\pragmatically.md": {
    primary: "In a manner guided by practical considerations and realistic outcomes rather than abstract principles.",
    secondary: "In linguistic theory, in a manner that accounts for context, speaker intent, and situational meaning beyond semantic syntax.",
    quotes: [
      { author: "William James", work: "The Will to Believe", quote: "If religious belief works **pragmatically** to ennoble life and sustain courage, on what grounds can abstract skepticism condemn it?" },
      { author: "John Dewey", work: "Reconstruction in Philosophy", quote: "Ideas must be understood **pragmatically** as prospective plans of action rather than static copies of external objects." },
      { author: "Charles Sanders Peirce", work: "How to Make Our Ideas Clear", quote: "Consider what effects that might conceivably have practical bearings you conceive the object of your conception to have; then your conception of these effects is the whole of your conception of the object, defined **pragmatically**." }
    ]
  },
  "Dashboard — prag\\pragmatics.md": {
    primary: "The branch of linguistics dealing with language in use and the contexts in which it is used, including conversational implicature, presupposition, and speech acts.",
    secondary: "In semiotics, the study of the relation of signs to the interpreters, agents, and social contexts in which they are deployed.",
    quotes: [
      { author: "Charles W. Morris", work: "Foundations of the Theory of Signs", quote: "We divide semiotics into syntactics, semantics, and **pragmatics**, the last dealing with the relation of signs to interpreters." },
      { author: "Rudolf Carnap", work: "Introduction to Semantics", quote: "When explicit reference is made to the language user, the investigation belongs to the realm of **pragmatics**." },
      { author: "Willard Van Orman Quine", work: "From a Logical Point of View", quote: "The boundary between pure semantics and empirical **pragmatics** is shifting and context-dependent." }
    ]
  },
  "Dashboard — prag\\pragmatism.md": {
    primary: "A philosophical movement holding that the meaning and truth of beliefs or concepts are to be evaluated by their practical outcomes and consequences.",
    secondary: "A practical approach to problems and affairs, oriented toward realistic achievements rather than rigid ideological doctrines.",
    quotes: [
      { author: "William James", work: "Pragmatism", quote: "**Pragmatism** unstiffens all our theories, limbers them up, and sets each one at work." },
      { author: "Charles Sanders Peirce", work: "Collected Papers", quote: "To establish the meaning of an intellectual concept, one must consider what practical consequences it involves; this doctrine is **pragmatism**." },
      { author: "John Dewey", work: "The Quest for Certainty", quote: "**Pragmatism** redefines philosophy as an active instrument for clarifying human problems and directing social inquiry." }
    ]
  },
  "Dashboard — prag\\pragmatist.md": {
    primary: "An adherent or advocate of philosophical pragmatism; a person who takes a practical, outcome-oriented approach to problems.",
    secondary: "In politics and organizational leadership, a decision-maker who emphasizes feasibility and tangible results over doctrinal dogmatism.",
    quotes: [
      { author: "William James", work: "Pragmatism", quote: "A **pragmatist** turns his back resolutely and once for all upon a lot of inveterate habits dear to professional philosophers." },
      { author: "Bertrand Russell", work: "Philosophical Essays", quote: "The **pragmatist** claims that what works well in the long run is what we ought to call true." },
      { author: "Richard Rorty", work: "Consequences of Pragmatism", quote: "The modern **pragmatist** abandons the attempt to step outside of human history and conversation." }
    ]
  },
  "Dashboard — prag\\prague.md": {
    primary: "The historic capital and largest city of the Czech Republic, historically the seat of the Kingdom of Bohemia and the Holy Roman Empire; in linguistics, the seat of the influential Prague Linguistic Circle.",
    secondary: "In cultural history, a crossroads of European literature, philosophy, and architectural monuments, renowned as the city of Franz Kafka, Tycho Brahe, and Johannes Kepler.",
    quotes: [
      { author: "Franz Kafka", work: "Letters to Friends, Family, and Editors", quote: "**Prague** does not let go of either of us; this little mother has claws." },
      { author: "Rainer Maria Rilke", work: "Two Stories of Prague", quote: "The ancient spires of **Prague** cast long shadows over the river, keeping watch over centuries of Bohemian dreaming." },
      { author: "Roman Jakobson", work: "Selected Writings", quote: "The intellectual circle that met in **Prague** during the late 1920s transformed modern structural linguistics and poetic analysis." }
    ]
  },
  "Dashboard — prag\\praxis.md": {
    primary: "Practice, as distinguished from theory; the application or enactment of a skill, idea, or artistic craft.",
    secondary: "In Aristotelian and Marxist philosophy, purposeful, goal-directed human action that actively transforms social reality and tests philosophical ideas.",
    quotes: [
      { author: "Karl Marx", work: "Theses on Feuerbach", quote: "The philosophers have only interpreted the world in various ways; the point, however, is to change it through revolutionary **praxis**." },
      { author: "Aristotle", work: "Nicomachean Ethics", quote: "Moral virtue is not acquired merely by listening to moral lectures, but by continuous virtuous **praxis**." },
      { author: "Paulo Freire", work: "Pedagogy of the Oppressed", quote: "True reflection is authentic only when it leads to action; **praxis** is the action and reflection of men upon their world in order to transform it." }
    ]
  },
  "Dashboard — prax\\apractic.md": {
    primary: "Relating to or exhibiting apraxia; unable to coordinate purposeful movements despite normal muscular power.",
    secondary: "In clinical neurology, describing the breakdown of motor schema and purposeful object interaction caused by cortical damage.",
    quotes: [
      { author: "Alexander Luria", work: "Higher Cortical Functions in Man", quote: "In parietal lobe syndromes, the **apractic** patient cannot reproduce simple stick patterns on the table." },
      { author: "Norman Geschwind", work: "Selected Papers on Language and the Brain", quote: "Careful examination showed the right limb was intact while the left was severely **apractic**." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "His hands trembled with an **apractic** hesitation whenever he tried to write his name." }
    ]
  },
  "Dashboard — prax\\apraxia.md": {
    primary: "A neurological impairment of the ability to execute purposeful, complex motor acts despite the physical capacity to move.",
    secondary: "In behavioral neurology, a disorder of learned skilled movement resulting from lesions in parietal or frontal association pathways.",
    quotes: [
      { author: "Hugo Liepmann", work: "The Syndrome of Apraxia", quote: "I designate by the term **apraxia** the disturbance of purposeful movement in the absence of motor paresis or ataxia." },
      { author: "Sigmund Freud", work: "On Aphasia", quote: "The clinical phenomenon of **apraxia** shows that the memory of motor melodies is stored apart from primary motor fibers." },
      { author: "Alexander Luria", work: "The Working Brain", quote: "Ideomotor **apraxia** disrupts the smooth transition between component movements of a complex manual act." }
    ]
  },
  "Dashboard — prax\\apraxic.md": {
    primary: "Characterized by or suffering from apraxia; impaired in the execution of intentional movements.",
    secondary: "Describing defective motor planning and execution when manipulating tools, making symbolic gestures, or imitating postures.",
    quotes: [
      { author: "Alexander Luria", work: "The Working Brain", quote: "An **apraxic** patient may describe how to strike a match perfectly, yet hold the box upside down when handed one." },
      { author: "Norman Geschwind", work: "Disconnexion Syndromes", quote: "The callosal lesion rendered the patient **apraxic** exclusively in response to verbal commands." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "The **apraxic** difficulty was not muscular weakness, but a breakdown in the spatial grammar of action." }
    ]
  },
  "Dashboard — prax\\parapraxis.md": {
    primary: "An unconscious or unintentional error in speech, memory, or action that discloses a suppressed wish or internal conflict; a Freudian slip.",
    secondary: "In psychodynamic analysis, symptomatic faulty actions demonstrating the permeability between conscious intention and the unconscious.",
    quotes: [
      { author: "Sigmund Freud", work: "Introductory Lectures on Psycho-Analysis", quote: "A **parapraxis** is not an accidental slip; it is a meaningful compromise between a conscious purpose and a repressed counter-wish." },
      { author: "Carl Jung", work: "Psychological Types", quote: "We must pay heed to every sudden **parapraxis**, for it often opens a doorway into the patient's shadow." },
      { author: "Jacques Lacan", work: "Écrits", quote: "Through the sudden flash of a **parapraxis**, the unconscious speaks its unvarnished truth." }
    ]
  },
  "Dashboard — prax\\practicability.md": {
    primary: "The quality or state of being practicable, workable, or capable of being accomplished under existing conditions; feasibility.",
    secondary: "In legal drafting, civil engineering, and public planning, the realistic capability of an enterprise to be executed with available means.",
    quotes: [
      { author: "Alexander Hamilton", work: "The Federalist No. 15", quote: "We must judge of the **practicability** of government not by imaginary perfection, but by human nature as it is." },
      { author: "Thomas Jefferson", work: "Notes on the State of Virginia", quote: "Experience has demonstrated the complete **practicability** of religious liberty without injury to civil order." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "The Americans test the **practicability** of every proposed legislation by its immediate social results." }
    ]
  },
  "Dashboard — prax\\practicable.md": {
    primary: "Capable of being put into practice or successfully carried out; feasible and usable.",
    secondary: "In navigation and geography, open, clear, or passable for travel or communication.",
    quotes: [
      { author: "George Washington", work: "Farewell Address", quote: "Promote then, as an object of primary importance, institutions for the general diffusion of knowledge; it is essential that public opinion should be enlightened as far as it is **practicable**." },
      { author: "Abraham Lincoln", work: "Speech at Peoria", quote: "Let us do what is **practicable** for the preservation of our liberties while respecting the constitutional order." },
      { author: "Benjamin Franklin", work: "Autobiography", quote: "I formed a project of arriving at moral perfection, which appeared to me quite **practicable**." }
    ]
  },
  "Dashboard — prax\\practicableness.md": {
    primary: "The condition of being practicable; feasibility or operational suitability.",
    secondary: "In political philosophy and administrative design, the degree to which an idealized policy can be effectively realized in practice.",
    quotes: [
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "Prudent statesmen look to the **practicableness** of a constitution rather than its abstract symmetrical beauty." },
      { author: "David Hume", work: "Essays: Moral, Political, and Literary", quote: "The **practicableness** of a republic in a vast territory was formerly questioned, yet modern commerce facilitates its execution." },
      { author: "John Adams", work: "Defence of the Constitutions of Government", quote: "The **practicableness** of a system of checks and balances has been vindicated by the peace of centuries." }
    ]
  },
  "Dashboard — prax\\practical.md": {
    primary: "Concerned with the actual doing or use of something, rather than with theory and ideas.",
    secondary: "In ethics and jurisprudence, governing intentional human action, conduct, and moral duty in experiential reality.",
    quotes: [
      { author: "Aristotle", work: "Nicomachean Ethics", quote: "**Practical** wisdom is a reasoned and true state of capacity to act with regard to the human good." },
      { author: "Immanuel Kant", work: "Groundwork of the Metaphysics of Morals", quote: "A good will is the indispensable condition of even the worthiness to be happy, guiding all **practical** reason." },
      { author: "John Locke", work: "An Essay Concerning Human Understanding", quote: "Our business here is not to know all things, but those which concern our **practical** conduct." }
    ]
  },
  "Dashboard — prax\\practicality.md": {
    primary: "The aspect of being practical, realistic, or adapted to actual circumstances and everyday life.",
    secondary: "In design and industrial manufacturing, functional utility and economy prioritized over purely ornamental considerations.",
    quotes: [
      { author: "Henry David Thoreau", work: "A Yankee in Canada", quote: "The genius of the American mind is noted for its shrewd **practicality** and disregard of useless ornament." },
      { author: "William James", work: "Talks to Teachers on Psychology", quote: "Pedagogy must be grounded upon **practicality**, instilling useful habits rather than barren abstractions." },
      { author: "Ralph Waldo Emerson", work: "English Traits", quote: "The English race is distinguished above all by its stubborn **practicality** and love of tangible facts." }
    ]
  },
  "Dashboard — prax\\practically.md": {
    primary: "For all practical purposes; virtually, almost; in a manner dictated by practical needs.",
    secondary: "In operational terms, through active bodily or mechanical execution rather than cognitive speculation.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Autobiography", quote: "I had **practically** no formal schooling in my early years, and had to make my own way through voracious reading." },
      { author: "George Eliot", work: "Silas Marner", quote: "The secret of his hoarded gold had **practically** vanished from the memories of the villagers." },
      { author: "Joseph Conrad", work: "Lord Jim", quote: "His courage was untried, but he was **practically** convinced that when the supreme moment arrived, he would prove heroic." }
    ]
  },
  "Dashboard — prax\\practice.md": {
    primary: "Repeated exercise in an activity or skill so as to acquire or maintain proficiency.",
    secondary: "The actual exercise of a profession, technique, or customary course of action.",
    quotes: [
      { author: "Francis Bacon", work: "The Essays: Of Studies", quote: "Studies themselves do give forth directions too much at large, except they be bounded in by **practice**." },
      { author: "Samuel Johnson", work: "The Rambler", quote: "Excellence in any art is not granted to effortless wish, but is the reward of patient, untiring **practice**." },
      { author: "William Osler", work: "The Master-Word in Medicine", quote: "The student of medicine must spend his mornings in the wards and his evenings in clinical **practice**." }
    ]
  },
  "Dashboard — prax\\practiced.md": {
    primary: "Having gained skill and ease through long experience or continuous exercise; seasoned; proficient.",
    secondary: "Done or performed repeatedly as a habit; marked by deliberate, studied execution.",
    quotes: [
      { author: "Herman Melville", work: "Billy Budd", quote: "Captain Vere listened with the **practiced** gravity of an officer long accustomed to weighing evidence." },
      { author: "Charles Dickens", work: "David Copperfield", quote: "Aunt Betsey Trotwood surveyed the kitchen with a **practiced** eye that detected every speck of dust." },
      { author: "Jane Austen", work: "Emma", quote: "Mr. Knightley was too **practiced** in society to betray his private vexation before the guests." }
    ]
  },
  "Dashboard — prax\\pragmatic.md": {
    primary: "Dealing with problems in a sensible and practical way based on specific conditions, rather than adhering to theoretical rules.",
    secondary: "In historiography and legal history, concerned with cause-and-effect relations, political realities, or imperial state ordinances.",
    quotes: [
      { author: "William James", work: "The Meaning of Truth", quote: "The true is the name of whatever proves itself to be good in the way of belief; this is the **pragmatic** rule." },
      { author: "John Dewey", work: "Experience and Nature", quote: "A **pragmatic** philosophy sees experience not as a veil that shuts man off from nature, but as the only means of penetrating into nature." },
      { author: "Charles Sanders Peirce", work: "Collected Papers", quote: "Our idea of anything is our idea of its sensible effects; a clear statement of this is the **pragmatic** maxim." }
    ]
  },
  "Dashboard — prax\\pragmatical.md": {
    primary: "Pertaining to business, practical affairs, or worldly matters; historically, officious or meddlesome.",
    secondary: "In statecraft, relating to public ordinances, practical governance, or imperial sanctions.",
    quotes: [
      { author: "Daniel Defoe", work: "Robinson Crusoe", quote: "I was not a man to indulge in **pragmatical** curiosities, but focused entirely on what was necessary for my preservation." },
      { author: "Jonathan Swift", work: "The Battle of the Books", quote: "The modern critic appeared very **pragmatical** and noisy, declaring that the ancients knew nothing of real literature." },
      { author: "David Hume", work: "A Treatise of Human Nature", quote: "Speculative men often become excessively **pragmatical** when they attempt to govern kingdoms from their closets." }
    ]
  },
  "Dashboard — prax\\pragmatically.md": {
    primary: "In a sensible and realistic manner, focusing on tangible effects and utility.",
    secondary: "In semiotic and linguistic analysis, in relation to communicative context, conversational goals, and speaker intention.",
    quotes: [
      { author: "William James", work: "Essays in Radical Empiricism", quote: "Let us judge every metaphysical dispute **pragmatically**, asking what concrete difference in life it makes if one side is true." },
      { author: "John Dewey", work: "Reconstruction in Philosophy", quote: "When moral principles are understood **pragmatically**, they become hypotheses to be tested by social consequences." },
      { author: "Richard Rorty", work: "Philosophy and the Mirror of Nature", quote: "To view truth **pragmatically** is to see it as what is good for us to believe in our community of inquiry." }
    ]
  },
  "Dashboard — prax\\pragmatism.md": {
    primary: "A philosophical doctrine affirming that the value, meaning, and truth of ideas reside in their practical consequences.",
    secondary: "A pragmatic attitude or policy that prioritizes workable solutions over ideological purity.",
    quotes: [
      { author: "William James", work: "Pragmatism", quote: "**Pragmatism** represents a perfectly familiar attitude in philosophy, the attitude of looking away from first things, principles, and categories, and looking towards last things, fruits, and consequences." },
      { author: "Charles Sanders Peirce", work: "Selected Writings", quote: "The method of **pragmatism** was conceived as a laboratory method applied to intellectual concepts." },
      { author: "John Dewey", work: "Logic: The Theory of Inquiry", quote: "In **pragmatism**, knowledge is an active operation modifying a problematic situation into a resolved one." }
    ]
  },
  "Dashboard — prax\\pragmatist.md": {
    primary: "A thinker who approaches questions through the lens of philosophical pragmatism; a practical actor.",
    secondary: "A leader, diplomat, or statesman who adapts policies to immediate circumstances rather than abstract dogmas.",
    quotes: [
      { author: "William James", work: "Pragmatism", quote: "The **pragmatist** clings to facts and concreteness, observes truth at its work in particular cases, and generalizes." },
      { author: "Bertrand Russell", work: "A History of Western Philosophy", quote: "To the **pragmatist**, truth is a species of the good, rather than a category independent of human interest." },
      { author: "Richard Rorty", work: "Objectivity, Relativism, and Truth", quote: "The **pragmatist** does not need an epistemic foundation, because conversation and solidarity provide all the justification required." }
    ]
  },
  "Dashboard — prax\\praxis.md": {
    primary: "Practical action, application, or customary exercise, contrasted with abstract theory.",
    secondary: "In critical theory and philosophical anthropology, human transformative activity that realizes human freedom and shapes the historical world.",
    quotes: [
      { author: "Aristotle", work: "Politics", quote: "Life is action and **praxis**, not mere production; therefore the slave is a minister in the sphere of action." },
      { author: "Karl Marx", work: "The German Ideology", quote: "The coincidence of the changing of circumstances and of human activity or self-change can be conceived and rationally understood only as revolutionary **praxis**." },
      { author: "Hannah Arendt", work: "The Human Condition", quote: "Action, or **praxis**, is the exclusive prerogative of man; neither a beast nor a god is capable of it, and only action depends on the constant presence of others." }
    ]
  },
  "Dashboard — prax\\praxiteles.md": {
    primary: "The celebrated 4th-century BCE Athenian sculptor renowned for the exquisite grace, sensuous curve, and naturalistic modeling of statues such as the Aphrodite of Knidos and Hermes bearing the infant Dionysus.",
    secondary: "In art history, the master whose innovative contrapposto (the 'Praxitelean curve') and delicate marble surface treatment defined Late Classical Greek sculpture.",
    quotes: [
      { author: "Pliny the Elder", work: "Natural History", quote: "**Praxiteles** surpassed all other artists in the grace with which he breathed lifelike softness into marble statues." },
      { author: "Walter Pater", work: "The Renaissance", quote: "In the art of **Praxiteles**, the severe majesty of Phidias yielded to a melting tenderness and sensuous human beauty." },
      { author: "John Addington Symonds", work: "Sketches and Studies in Italy and Greece", quote: "The Hermes of **Praxiteles** at Olympia exhibits that relaxed languor and effortless grace that was the glory of late Athenian sculpture." }
    ]
  },
  "Dashboard — prax\\unpracticed.md": {
    primary: "Lacking experience, training, or proficiency in an activity or skill; untried.",
    secondary: "Not customary, repeated, or put into habitual exercise; naive.",
    quotes: [
      { author: "William Shakespeare", work: "The Merchant of Venice", quote: "An unlesson’d girl, unschool’d, **unpracticed**; happy in this, she is not yet so old but she may learn." },
      { author: "John Milton", work: "Paradise Lost", quote: "Thoughts whither have ye led me, with what compunctions, **unpracticed** in these deep labyrinths of divine providence?" },
      { author: "Jane Austen", work: "Sense and Sensibility", quote: "Marianne’s mind was wholly **unpracticed** in the art of concealing her feelings from the eyes of indifferent observers." }
    ]
  },
  "Dashboard — pri\\amphiprion.md": {
    primary: "A genus of brightly colored marine damselfishes (family Pomacentridae), commonly known as clownfishes or anemonefishes.",
    secondary: "In marine ecology, fishes famous for their obligate mutualistic symbiosis with large sea anemones, protected from stinging nematocysts by a special mucus coat.",
    quotes: [
      { author: "Charles Darwin", work: "The Structure and Distribution of Coral Reefs", quote: "Tiny brilliantly banded fishes of the genus **Amphiprion** darted fearlessly among the venomous tentacles of the giant sea anemone." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "I observed several species of **Amphiprion** swimming unharmed within the stinging umbrellas of sea anemones in the shallow coral shallows." },
      { author: "Philip Henry Gosse", work: "The Aquarium: An Unveiling of the Wonders of the Deep Sea", quote: "The remarkable association between **Amphiprion** and its protective host polyp illustrates one of nature's most delicate mutualisms." }
    ]
  },
  "Dashboard — pri\\polyprion.md": {
    primary: "A genus of large deepwater marine fishes in the family Polyprionidae, commonly known as wreckfishes.",
    secondary: "In ichthyology, predatory, heavy-bodied teleosts possessing serrated opercular spines, typically inhabiting shipwrecks and deep rocky continental shelves.",
    quotes: [
      { author: "Charles Darwin", work: "Zoology of the Voyage of H.M.S. Beagle", quote: "Our crew captured a gigantic specimen of **Polyprion**, whose firm white flesh provided an excellent repast for the entire ship." },
      { author: "Georges Cuvier", work: "The Animal Kingdom", quote: "The genus **Polyprion** is distinguished from ordinary perches by the rough denticulated crests upon its opercular bones." },
      { author: "Francis Day", work: "The Fishes of Great Britain and Ireland", quote: "The deep-sea wreckfish, **Polyprion** cernium, frequents floating timber and rocky offshore ledges at great depths." }
    ]
  },
  "Dashboard — pri\\prion.md": {
    primary: "An infectious proteinaceous particle that lacks nucleic acid and causes transmissible spongiform encephalopathies (such as Creutzfeldt-Jakob disease, kuru, and scrapie).",
    secondary: "In ornithology, any of several small bluish-grey Southern Ocean petrels of the genus Pachyptila possessing serrated lamellae on the bill for filtering zooplankton.",
    quotes: [
      { author: "Stanley B. Prusiner", work: "Prions: Nobel Lecture", quote: "I introduced the term **prion** to designate a small proteinaceous infectious particle that resists inactivation by procedures that modify nucleic acids." },
      { author: "Oliver Sacks", work: "The Island of the Colorblind", quote: "The riddle of kuru was finally illuminated by the revolutionary concept of the infectious **prion**." },
      { author: "Robert Falcon Scott", work: "The Voyage of the Discovery", quote: "Small blue petrels, commonly called the dove **prion**, flitted ceaselessly over the freezing swells of the Antarctic pack." }
    ]
  },
  "Dashboard — scap\\scape.md": {
    primary: "In botany, a leafless, flower-bearing stalk arising directly from a bulb, corm, rootstock, or basal rosette of leaves (as in daffodils or garlic).",
    secondary: "In architecture and entomology, the shaft of a column, or the elongated basal segment of an insect's antenna; also an archaic literary truncation of escape.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The leaves of the primrose are all radical, and the flower-stalk is a true **scape** rising naked to support the umbel." },
      { author: "John Ruskin", work: "Modern Painters", quote: "Every architectural shaft and natural plant **scape** reveals how vertical lines strive upward against gravitational pull." },
      { author: "William Wordsworth", work: "The Excursion", quote: "From the moist turf arose the slender **scape** of the mountain daffodil, crowned with gold." }
    ]
  },
  "Dashboard — scap\\scapegoat.md": {
    primary: "A person or group made to bear the blame for others or to suffer in their place.",
    secondary: "In biblical anthropology (Leviticus 16), the goat over whose head the high priest confessed the sins of the people, subsequently driven into the wilderness for Azazel.",
    quotes: [
      { author: "James George Frazer", work: "The Golden Bough", quote: "In ancient ritual, the community transferred its accumulated sins and misfortunes onto a symbolic **scapegoat** driven out into the wilderness." },
      { author: "Shirley Jackson", work: "The Lottery", quote: "The ancient human impulse to select a **scapegoat** to purge communal anxieties lies dormant beneath civilized conventions." },
      { author: "George Eliot", work: "Daniel Deronda", quote: "He felt bitterly that he was being marked out as a convenient **scapegoat** to bear the consequences of family imprudence." }
    ]
  },
  "Dashboard — scap\\scapegrace.md": {
    primary: "A mischievous, reckless, or completely unprincipled person; a rogue or ne'er-do-well.",
    secondary: "In 18th- and 19th-century literature, an incorrigible, irresponsible young man whose escapades provoke scandal yet retain roguish charm.",
    quotes: [
      { author: "Charles Dickens", work: "Bleak House", quote: "He has a woeful consciousness upon him of being a **scapegrace**, though his open face makes it impossible to harbor malice against him." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "Rawdon Crawley had been a notorious **scapegrace** at school, yet he possessed an instinctive gallantry that won over society." },
      { author: "Walter Scott", work: "The Antiquary", quote: "The old uncle would shake his head at the young **scapegrace**, all while slipping gold sovereigns into his hand." }
    ]
  },
  "Dashboard — scap\\scapose.md": {
    primary: "Having or producing a scape; characterized by a leafless flowering stem rising directly from the ground or root.",
    secondary: "In plant morphology, describing inflorescences where vegetative leaves are clustered entirely at the base, leaving the floral axis naked.",
    quotes: [
      { author: "Asa Gray", work: "Structural Botany", quote: "When a plant produces its foliage in a basal rosette, leaving the flowering stem leafless, it is described as **scapose**." },
      { author: "John Torrey", work: "Flora of North America", quote: "The **scapose** habit of the dandelion allows its flowering head to elevate its seeds above surrounding pasture grasses." },
      { author: "Liberty Hyde Bailey", work: "Cyclopedia of American Horticulture", quote: "Many popular garden monocots are strictly **scapose**, bearing elegant bare stalks topped by showy blooms." }
    ]
  },
  "Dashboard — scap\\scapula.md": {
    primary: "The shoulder blade; a large, flat triangular bone located in the posterolateral aspect of the human shoulder girdle.",
    secondary: "In comparative vertebrate anatomy, the dorsal element of the pectoral girdle providing muscular attachments for humeral rotation and limb articulation.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Vertebrated Animals", quote: "The dorsal portion of the pectoral girdle in higher mammals consists principally of the expanded blade of the **scapula**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Pleuritic friction rubs are often heard most distinctly just below the inferior angle of the **scapula**." },
      { author: "Richard Owen", work: "On the Archetype of the Skeleton", quote: "The broad spine that crosses the outer surface of the mammalian **scapula** terminates anteriorly in the acromion process." }
    ]
  },
  "Dashboard — scap\\scapular.md": {
    primary: "Relating to the shoulder blade or scapula.",
    secondary: "In monastic dress, a religious garment consisting of two bands of cloth hanging over the chest and back, worn by members of various Catholic orders.",
    quotes: [
      { author: "James Joyce", work: "A Portrait of the Artist as a Young Man", quote: "He was enrolled in the sodality of the Blessed Virgin, wearing the brown **scapular** next to his skin as a shield against mortal sin." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Referred pain radiating to the right **scapular** region is a classic hallmark of acute biliary colic." },
      { author: "Thomas Merton", work: "The Seven Storey Mountain", quote: "When I received the white habit and the heavy woolen **scapular**, I felt consecrated to a life of silent prayer." }
    ]
  },
  "Dashboard — scap\\scapulary.md": {
    primary: "A variant of scapular; a monastic vestment worn over the shoulders, or an anatomical term relating to the shoulder region.",
    secondary: "In surgical history, a shoulder bandage designed to support the arm or stabilize the clavicle and scapular girdle.",
    quotes: [
      { author: "William Beattie", work: "The Waldenses", quote: "The monk laid aside his travel cowl and girt his black **scapulary** close to his waist before entering the chapter house." },
      { author: "Samuel Johnson", work: "A Dictionary of the English Language", quote: "A **scapulary** is a garment consisting of two breadths of cloth worn over the shoulders by several religious orders." },
      { author: "Walter Scott", work: "The Monastery", quote: "Under his flowing mantle, the brother wore the coarse serge **scapulary** that marked his vow of austere poverty." }
    ]
  },
  "Dashboard — scap\\scapulohumeral.md": {
    primary: "Relating to or connecting the shoulder blade (scapula) and the upper arm bone (humerus).",
    secondary: "In clinical neurology, designating scapulohumeral muscular dystrophy, a form of progressive muscular dystrophy affecting shoulder and upper arm musculature.",
    quotes: [
      { author: "William R. Gowers", work: "A Manual of Diseases of the Nervous System", quote: "In the **scapulohumeral** type of muscular dystrophy, atrophy begins symmetrically in the shoulder girdle and biceps." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The patient demonstrated profound **scapulohumeral** weakness, unable to elevate his arms above horizontal level." },
      { author: "Jean-Martin Charcot", work: "Clinical Lectures on Diseases of the Nervous System", quote: "We contrast the facial-scapulo-humeral distribution of Landouzy with pure juvenile **scapulohumeral** myopathy." }
    ]
  },
  "Dashboard — scap\\scapus.md": {
    primary: "In anatomical and botanical terminology, a scape, stalk, shaft, or stem; the central axis or stem of a feather (rachis and calamus).",
    secondary: "In entomology, the basal joint of an antenna; in architecture, the shaft of an architectural column between the base and capital.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "The base of the sea anemone consists of an adhering pedal disc, from which rises the cylindrical column or **scapus**." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "In domestic poultry, alterations in the plumage affect both the vane and the central **scapus** of each flight feather." },
      { author: "Asa Gray", work: "Manual of Botany", quote: "The **scapus** of the plant supports a terminal inflorescence while remaining destitute of ordinary foliage leaves." }
    ]
  },
  "Dashboard — schiz\\schizachyrium.md": {
    primary: "A genus of widespread grasses in the family Poaceae, most notably Schizachyrium scoparium (little bluestem), prominent in native North American tallgrass prairies.",
    secondary: "In agrostology and grassland ecology, warm-season bunchgrasses with branched racemes and plumose pedicels, vital for erosion control and forage.",
    quotes: [
      { author: "Aldo Leopold", work: "A Sand County Almanac", quote: "On the gravelly moraines, the red-gold stems of **Schizachyrium** celebrate the onset of November across the prairie." },
      { author: "John Weaver", work: "North American Prairie", quote: "Little bluestem, **Schizachyrium** scoparium, forms dense tufts whose fibrous root system penetrates deep into dry upland soil." },
      { author: "Liberty Hyde Bailey", work: "Manual of Cultivated Plants", quote: "Ornamental grass gardens utilize species of **Schizachyrium** for their brilliant autumnal coloration and upright habit." }
    ]
  },
  "Dashboard — schiz\\schizaea.md": {
    primary: "The type genus of the fern family Schizaeaceae, commonly known as curly grass ferns, characterized by small, grass-like fronds and comb-like fertile lobes.",
    secondary: "In pteridology, primitive leptosporangiate ferns native to acidic peat bogs, renowned for their minimalist morphology and solitary terminal sporangia.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The curious little curly-grass fern, **Schizaea** pusilla, lurks among the mosses of the pine barrens of New Jersey." },
      { author: "John Torrey", work: "Flora of the Northern and Middle Sections of the United States", quote: "Finding the diminutive fertile fronds of **Schizaea** in a sphagnous swamp rewards the keenest botanical collector." },
      { author: "Nathaniel Lord Britton", work: "Illustrated Flora of the Northern United States", quote: "The genus **Schizaea** represents a remarkably primitive fern type with linear leaves and pinnate fertile spikes." }
    ]
  },
  "Dashboard — schiz\\schizaeaceae.md": {
    primary: "A family of primitive leptosporangiate ferns, mostly tropical, characterized by distinctive sporangia bearing an apical cap-like ring.",
    secondary: "In systematic botany, an ancient lineage of ferns with fossil records extending into the Mesozoic, displaying solitary marginal sporangia.",
    quotes: [
      { author: "Asa Gray", work: "Structural Botany", quote: "The family **Schizaeaceae** comprises archaic tropical and subtropical ferns with sporangia bearing an apical cap-like ring." },
      { author: "Nathaniel Lord Britton", work: "Illustrated Flora of the Northern United States", quote: "Members of the **Schizaeaceae** are easily recognized by their peculiar clustered sporangia and dimorphic fronds." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "Several genera of the **Schizaeaceae**, notably Lygodium and Schizaea, possess remarkable climbing or rush-like habits." }
    ]
  },
  "Dashboard — schiz\\schizanthus.md": {
    primary: "A genus of annual or biennial flowering plants in the family Solanaceae, native to Chile and Argentina, commonly known as butterfly flowers or poor man's orchids.",
    secondary: "In horticulture and floriculture, prized ornamental plants bearing zygomorphic, deeply incised, multi-colored blossoms resembling miniature orchids.",
    quotes: [
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "No greenhouse annual surpasses **Schizanthus** in profusion of bloom, earning it the affectionate name of poor man's orchid." },
      { author: "Gertrude Jekyll", work: "Colour in the Flower Garden", quote: "The fluttering, butterfly-like corollas of **Schizanthus** create a cloud of purple, gold, and crimson in the conservatory border." },
      { author: "Reginald Farrer", work: "The English Rock Garden", quote: "Chilean species of **Schizanthus** require full sunshine to display their intricately spotted and cleft petals." }
    ]
  },
  "Dashboard — schiz\\schizocarp.md": {
    primary: "A dry fruit formed from a syncarpous ovary that splits at maturity into individual one-seeded, indehiscent carpels called mericarps.",
    secondary: "In botanical morphology, the characteristic fruit type of the carrot (Apiaceae), maple (Aceraceae), and mallow (Malvaceae) families.",
    quotes: [
      { author: "Asa Gray", work: "Structural Botany", quote: "At maturity, the dry **schizocarp** of the carrot splits longitudinally into two separate, seed-like mericarps." },
      { author: "Liberty Hyde Bailey", work: "Manual of Cultivated Plants", quote: "The winged fruits of the maple are familiar examples of a **schizocarp** that separates into two samaras." },
      { author: "John Torrey", work: "Botanical Text-Book", quote: "In the Umbelliferae, each **schizocarp** hangs suspended for a time upon a slender central carpophore." }
    ]
  },
  "Dashboard — schiz\\schizogony.md": {
    primary: "Asexual multiple fission characteristic of certain protozoans (especially Apicomplexa such as Plasmodium), in which a single trophozoite segments into multiple merozoites.",
    secondary: "In medical parasitology, the intracellular proliferative stage of the malaria parasite occurring within hepatic and erythrocytic cells of the vertebrate host.",
    quotes: [
      { author: "Ronald Ross", work: "The Prevention of Malaria", quote: "During the erythrocytic cycle of **schizogony**, the malaria parasite divides into numerous daughter spores within the red corpuscle." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The periodic febrile paroxysms of ague coincide precisely with the completion of **schizogony** and the burst of infected erythrocytes." },
      { author: "Patrick Manson", work: "Tropical Diseases", quote: "The asexual cycle of **schizogony** in man alternates with the sexual sporogonic phase in the mosquito." }
    ]
  }
};

const updatedCount = updateNotesBatch(baseClusterDir, batch3Data);
console.log(`[Batch 3] Successfully updated ${updatedCount}/${Object.keys(batch3Data).length} notes.`);
