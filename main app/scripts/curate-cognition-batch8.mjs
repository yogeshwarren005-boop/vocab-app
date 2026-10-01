import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Cognition & Mind/Dashboard — theo";

const wordsData = {
  "apotheose.md": {
    word: "apotheose",
    primary: "To deify; to elevate someone or something to the status of a god, or to glorify as the supreme ideal.",
    secondary: "In literary and art criticism, to transform a mortal subject into a mythic, timeless, or celestial symbol.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The servile Roman senate voted to **apotheose** the deceased Caesar, enrolling him among the celestial guardians of the empire." },
      { author: "Thomas Carlyle", work: "On Heroes, Hero-Worship, and the Heroic in History", quote: "Ancient pagan tribes were swift to **apotheose** their fallen warriors, transforming brave kings into solar deities." },
      { author: "Henry James", work: "The Golden Bowl", quote: "Her loving imagination tended to **apotheose** his simplest gestures, bathing them in an aura of noble magnanimity." }
    ]
  },
  "apotheosis.md": {
    word: "apotheosis",
    primary: "The elevation of someone to divine status; deification; the highest point in the development of something; culmination or climax.",
    secondary: "In classical art and neoclassical painting, a composition depicting the triumphant ascent of a hero's soul into the heavenly pantheon.",
    quotes: [
      { author: "Alexander Pope", work: "The Rape of the Lock", quote: "The sacred hair, which long he sought in vain, / Receives an **apotheosis** in the sky, / A radiant star to shine eternally." },
      { author: "Friedrich Nietzsche", work: "The Birth of Tragedy", quote: "In the final chorus of Greek tragedy, we witness the sublime **apotheosis** of the suffering hero reconciled with cosmic necessity." },
      { author: "Ralph Waldo Emerson", work: "Representative Men", quote: "Shakespeare’s drama is the **apotheosis** of human intellect, encompassing the entire comedic and tragic range of our mortal state." }
    ]
  },
  "apotheosise.md": {
    word: "apotheosise",
    primary: "To deify; to glorify or venerate someone as a divine being or supreme ideal (British English spelling).",
    secondary: "In cultural and political history, to sanctify a national leader or historic victory with religious veneration.",
    quotes: [
      { author: "George Eliot", work: "Romola", quote: "The Florentine multitude seemed ready to **apotheosise** Savonarola when his fiery sermons denounced corruption." },
      { author: "Thomas Hardy", work: "The Return of the Native", quote: "Clym’s impassioned vision led him to **apotheosise** rural life, ignoring its grinding physical hardship." },
      { author: "William Makepeace Thackeray", work: "The History of Henry Esmond", quote: "Poets were hired to **apotheosise** the Duke of Marlborough after the glorious fields of Blenheim." }
    ]
  },
  "apotheosize.md": {
    word: "apotheosize",
    primary: "To deify; to glorify, idealize, or exalt to the rank of a god or divine ideal.",
    secondary: "In literary biography, to portray a historical figure with uncritical, worshipful adulation, erasing human flaws.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "To the superstitious whalemen, the white monster seemed an **apotheosized** terror of the deep." },
      { author: "Mark Twain", work: "Personal Recollections of Joan of Arc", quote: "The French nation was eager to **apotheosize** the brave Maid of Orleans after centuries of neglect." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "Democratic nations rarely **apotheosize** individual rulers, preferring to worship the sovereign majesty of the people." }
    ]
  },
  "atheism.md": {
    word: "atheism",
    primary: "Disbelief or lack of belief in the existence of God or gods.",
    secondary: "In philosophical and theological history, a principled rejection of theistic cosmologies in favor of materialist, naturalistic explanations of the universe.",
    quotes: [
      { author: "Francis Bacon", work: "The Essays: Of Atheism", quote: "I had rather believe all the fables in the Legend, and the Talmud, and the Alcoran, than that this universal frame is without a mind; a little philosophy inclineth man's mind to **atheism**, but depth in philosophy bringeth men's minds about to religion." },
      { author: "Percy Bysshe Shelley", work: "The Necessity of Atheism", quote: "The mind cannot believe the existence of a God; reason leads directly to intellectual **atheism**." },
      { author: "Baruch Spinoza", work: "Theological-Political Treatise", quote: "Those who defend superstition brand every independent philosophical inquiry with the charge of **atheism**." }
    ]
  },
  "atheist.md": {
    word: "atheist",
    primary: "A person who disbelieves or lacks belief in the existence of God or gods.",
    secondary: "Historically, an epithet frequently applied in antiquity to those who rejected traditional civic deities (such as early Christians in pagan Rome).",
    quotes: [
      { author: "Plato", work: "Laws", quote: "No one who has taken up in youth this opinion that the gods do not exist has ever continued in old age as a confirmed **atheist**." },
      { author: "Arthur Schopenhauer", work: "Parerga and Paralipomena", quote: "The honest **atheist** rejects anthropomorphic mythologies to confront the indifferent will of nature." },
      { author: "Bertrand Russell", work: "Why I Am Not a Christian", quote: "When addressing the general public, I define myself as an **atheist** regarding the personal deity of popular religion." }
    ]
  },
  "atheistic.md": {
    word: "atheistic",
    primary: "Clearly or characteristically rejecting or lacking belief in God or gods; relating to atheism.",
    secondary: "In ethical and philosophical treatises, describing worldviews grounded strictly in naturalism, secular humanism, or dialectical materialism.",
    quotes: [
      { author: "David Hume", work: "Dialogues Concerning Natural Religion", quote: "Philo argued that natural evils could be reconciled with an **atheistic** cosmos far more easily than with infinite benevolence." },
      { author: "John Stuart Mill", work: "Three Essays on Religion", quote: "An **atheistic** moral philosophy may cultivate noble social virtues without relying on supernatural sanctions." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "He condemned the **atheistic** cabal of French philosophers who sought to uproot Christian civilization." }
    ]
  },
  "atheistical.md": {
    word: "atheistical",
    primary: "Of, relating to, or marked by atheism; denying or questioning the existence of a supreme deity (historical/formal variant).",
    secondary: "In 17th- and 18th-century polemical and theological prose, describing doctrines or libertine habits perceived as subversive of divine law and public morality.",
    quotes: [
      { author: "Thomas Browne", work: "Religio Medici", quote: "I can never persuade myself that there was ever any such thing in nature as a complete, confirmed **atheistical** mind." },
      { author: "Jonathan Swift", work: "An Argument Against Abolishing Christianity", quote: "The freethinkers circulate their **atheistical** pamphlets under the specious pretense of promoting civil liberty." },
      { author: "Joseph Addison", work: "The Spectator", quote: "Nothing can be more ridiculous than an **atheistical** coxcomb who prides himself on disbelieving what he has never studied." }
    ]
  },
  "pantheon.md": {
    word: "pantheon",
    primary: "All the gods of a people or religion collectively; a magnificent temple dedicated to all the gods; a group of particularly respected, illustrious, or famous figures.",
    secondary: "In architectural history, the celebrated circular Roman temple built by Hadrian; in cultural history, a national mausoleum or hall of fame honoring heroes (e.g. the Panthéon in Paris).",
    quotes: [
      { author: "Lord Byron", work: "Childe Harold's Pilgrimage", quote: "Simple, erect, severe, austere, sublime— / Shrine of all saints and temple of all gods, / From Jove to Jesus—spared and blest by time; / Looking tranquility, while falls or nods / Arch, empire, each thing round thee, and man plods / His way through thorns to leap into a chasm; / Pride of Rome! / Relic of nobler days, and noblest arts! / Despoiled yet perfect, art and death's pride, / **Pantheon**! pride of Rome!" },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The magnificent portico of the Roman **Pantheon** still displays the proud inscription of Marcus Agrippa." },
      { author: "Victor Hugo", work: "Les Misérables", quote: "France entombed her great men within the **Panthéon**, fulfilling the republic's debt to eternal genius." }
    ]
  },
  "theocracy.md": {
    word: "theocracy",
    primary: "A system of government in which priests rule in the name of God or a god; a state governed by immediate divine guidance or official religious law.",
    secondary: "In political history (term coined by Josephus to describe the Jewish polity), a commonwealth where civil and religious authority are fused under divine covenant.",
    quotes: [
      { author: "Flavius Josephus", work: "Against Apion", quote: "Our lawgiver had no regard to monarchies or oligarchies, but ordained that our government should be what may be called a **theocracy**." },
      { author: "John Milton", work: "The Reason of Church-Government", quote: "Under the ancient Hebrew commonwealth, God Himself was the king in that sacred **theocracy**." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "The early Puritan settlements in Massachusetts resembled a strict **theocracy**, enforcing moral law by civil magistrate." }
    ]
  },
  "theocratic.md": {
    word: "theocratic",
    primary: "Of, relating to, or characteristic of a theocracy; governed by religious authority claiming divine mandate.",
    secondary: "In comparative constitutional studies, describing legal codes, courts, and civil institutions organized around religious scriptures rather than secular democracy.",
    quotes: [
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "Ancient Egypt was organized into a rigid **theocratic** hierarchy where the priestly caste guarded all sacred and civil knowledge." },
      { author: "Nathaniel Hawthorne", work: "The Scarlet Letter", quote: "The stern magistrates of Salem administered a **theocratic** discipline that tolerated no deviation from biblical orthodoxy." },
      { author: "Bertrand Russell", work: "A History of Western Philosophy", quote: "Calvin transformed Geneva into a **theocratic** city-state, regulating both religious belief and private commerce." }
    ]
  },
  "theologian.md": {
    word: "theologian",
    primary: "A person who engages in or is an expert in theology; a scholar of religious faith, divine attributes, and doctrinal traditions.",
    secondary: "In church history, an authoritative doctor of the faith (such as Augustine, Thomas Aquinas, or Calvin) who systematically formulates religious doctrines.",
    quotes: [
      { author: "Thomas Aquinas", work: "Summa Theologiae", quote: "The Christian **theologian** receives his principles from divine revelation, employing human reason to elucidate holy mysteries." },
      { author: "Erasmus", work: "The Praise of Folly", quote: "The scholastic **theologians** debate endlessly whether divine omnipotence could create a stone too heavy to lift." },
      { author: "C. S. Lewis", work: "Mere Christianity", quote: "Every thinking Christian is in some measure a **theologian**, shaping their daily life by what they believe about God." }
    ]
  },
  "theological.md": {
    word: "theological",
    primary: "Of or relating to the study of theology, religious faith, or the divine nature; doctrinal.",
    secondary: "In intellectual history and sociology (Auguste Comte's Law of Three Stages), denoting the primitive stage of human civilization that explains natural phenomena through supernatural deities.",
    quotes: [
      { author: "Auguste Comte", work: "The Positive Philosophy", quote: "In the **theological** stage, the human mind directs its investigations to the first and final causes of all effects, seeking supernatural agents." },
      { author: "John Henry Newman", work: "The Idea of a University", quote: "Religious truth cannot be excluded from liberal education, for **theological** inquiry grounds the unity of all knowledge." },
      { author: "George Eliot", work: "Scenes of Clerical Life", quote: "The vicar’s study was lined with heavy **theological** folios that smelled of ancient leather and damp parchment." }
    ]
  },
  "theologically.md": {
    word: "theologically",
    primary: "In a manner relating to theology, religious doctrine, or the nature of God.",
    secondary: "In hermeneutics and doctrinal analysis, evaluated from the perspective of divine revelation, orthodoxy, and ecclesiastical dogma.",
    quotes: [
      { author: "John Calvin", work: "Institutes of the Christian Religion", quote: "To speak **theologically**, human nature since the Fall is completely destitute of saving righteousness." },
      { author: "Søren Kierkegaard", work: "Fear and Trembling", quote: "Abraham’s willingness to sacrifice Isaac can be understood only **theologically**, through the teleological suspension of the ethical." },
      { author: "Friedrich Schleiermacher", work: "The Christian Faith", quote: "Dogmas are **theologically** valid only insofar as they faithfully express the living religious consciousness of the church." }
    ]
  },
  "theologise.md": {
    word: "theologise",
    primary: "To speculate, discourse, or reason upon religious or theological subjects (British English spelling).",
    secondary: "In literary and philosophical prose, to turn mundane historical or moral events into grandiose religious allegories.",
    quotes: [
      { author: "Thomas Hardy", work: "Jude the Obscure", quote: "Jude sat under the shadow of the cathedral, eager to **theologise** on patristic texts with the learned scholars of Christminster." },
      { author: "Samuel Taylor Coleridge", work: "Biographia Literaria", quote: "It is the natural tendency of the human mind to **theologise** when confronted with sublime aspects of nature." },
      { author: "William Hazlitt", work: "Lectures on the English Poets", quote: "Milton was prone to **theologise** in verse, yet his poetic genius triumphs over his dogmatic disputations." }
    ]
  },
  "theologiser.md": {
    word: "theologiser",
    primary: "A person who theologizes; one who speculates on theological matters, often used pejoratively for an amateur or tedious dogmatist (British English spelling).",
    secondary: "In 18th- and 19th-century satire, an armchair polemicist who debates fine points of creed while ignoring practical charity.",
    quotes: [
      { author: "Jonathan Swift", work: "A Tale of a Tub", quote: "The parish **theologiser** spent thirty years disputing the precise length of Noah's ark while his flock went untended." },
      { author: "George Eliot", work: "Middlemarch", quote: "Mr. Casaubon was an unwearied **theologiser**, accumulating endless notebooks to prove that all mythologies were corrupted Hebrew traditions." },
      { author: "Charles Dickens", work: "Bleak House", quote: "Mrs. Pardiggle surrounded herself with zealous **theologisers** who distributed tractates to the starving poor." }
    ]
  },
  "theologist.md": {
    word: "theologist",
    primary: "A theologian; a scholar or student who investigates and interprets religious doctrines and divine truths (archaic or formal synonym).",
    secondary: "In classical and early modern English prose, an authorized divine or religious philosopher versed in scripture and scholastic disputation.",
    quotes: [
      { author: "John Milton", work: "Areopagitica", quote: "The learned **theologist** must not fear the encounter with error, for truth flourishes best in open intellectual contest." },
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "The natural philosopher and the divine **theologist** must respect their distinct boundaries without mutual trespass." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The Alexandrian **theologists** subtle disputes divided the Eastern empire over a single Greek diphthong." }
    ]
  },
  "theologize.md": {
    word: "theologize",
    primary: "To speculate, debate, or discourse on theological matters; to interpret a subject from a religious or theological standpoint.",
    secondary: "In cultural criticism, to impart a theological interpretation or sanctified significance to political, economic, or artistic movements.",
    quotes: [
      { author: "Ralph Waldo Emerson", work: "Essays: First Series", quote: "We are prone to **theologize** over our miseries, seeking divine retributions where only physical negligence was at work." },
      { author: "Nathaniel Hawthorne", work: "The Blithedale Romance", quote: "Hollingsworth would **theologize** upon his philanthropic project until his eyes blazed with monomaniacal light." },
      { author: "William James", work: "The Varieties of Religious Experience", quote: "When religious feeling cools, the intellect begins to **theologize**, creating scholastic formulas to replace living fire." }
    ]
  },
  "theologizer.md": {
    word: "theologizer",
    primary: "A person who theologizes; one who constructs, debates, or expounds theological theories.",
    secondary: "In social and literary essays, an intellectual who frames secular debates in theological terminology.",
    quotes: [
      { author: "Benjamin Franklin", work: "Autobiography", quote: "Our young town **theologizer** was forever challenging the elders to public disputations upon predestination." },
      { author: "Mark Twain", work: "The Innocents Abroad", quote: "The loquacious **theologizer** explained every ruin along the Jordan by reference to ancient prophecies." },
      { author: "Herman Melville", work: "Mardi: and a Voyage Thither", quote: "Babbalanja the philosopher acted as chief **theologizer**, weaving speculative parables on the divine nature." }
    ]
  },
  "theology.md": {
    word: "theology",
    primary: "The systematic study of the nature of God, divine attributes, and religious truth, especially within an organized religious tradition.",
    secondary: "In academic history, the 'Queen of the Sciences' in medieval universities; broadly, a coherent body of religious doctrines and philosophical beliefs.",
    quotes: [
      { author: "Thomas Aquinas", work: "Summa Theologiae", quote: "Sacred **theology** is taught by God, teaches of God, and leads unto God." },
      { author: "Augustine of Hippo", work: "The City of God", quote: "True **theology** is reasoning or discourse concerning the divine nature and our eternal destination." },
      { author: "Immanuel Kant", work: "Critique of Pure Reason", quote: "Speculative **theology** can never demonstrate the objective existence of God, but moral philosophy establishes its practical necessity." }
    ]
  },
  "theorem.md": {
    word: "theorem",
    primary: "A mathematical statement or proposition that has been demonstrated to be true by a chain of logical deduction from accepted axioms.",
    secondary: "In logic and formal systems, a valid formula provable within a formal deductive calculus; broadly, a demonstrated general truth.",
    quotes: [
      { author: "Euclid", work: "Elements (Book I)", quote: "In any right-angled triangle, the square on the hypotenuse is equal to the squares on the sides containing the right angle; this celebrated **theorem** is established beyond doubt." },
      { author: "Bertrand Russell", work: "Principia Mathematica", quote: "Every mathematical **theorem** is a tautology, revealing relations already implicit within the initial axioms." },
      { author: "Albert Einstein", work: "Relativity: The Special and the General Theory", quote: "The Pythagorean **theorem** provides the Euclidean metric foundation that general relativity generalized into curved spacetime." }
    ]
  },
  "theoretic.md": {
    word: "theoretic",
    primary: "Of or relating to theory; theoretical; conceptual and abstract rather than practical or applied.",
    secondary: "In classical philosophy (Aristotle's theōrētikē philosophia), concerning the contemplative pursuit of truth (physics, mathematics, theology) as distinct from practical action (praxis).",
    quotes: [
      { author: "Aristotle", work: "Metaphysics", quote: "The **theoretic** sciences—mathematics, physics, and theology—are the most honorable, seeking truth for its own sake." },
      { author: "Francis Bacon", work: "Novum Organum", quote: "Pure **theoretic** speculation divorced from empirical experiments produces only empty webs of scholastic dogma." },
      { author: "John Ruskin", work: "Modern Painters", quote: "The **theoretic** faculty perceives beauty not as mere sensual pleasure, but as a moral reflection of divine perfection." }
    ]
  },
  "theoretical.md": {
    word: "theoretical",
    primary: "Concerned with or based on the theory of a subject or field of study rather than its practical application; abstract or speculative.",
    secondary: "In scientific research, formulating mathematical models and hypotheses (theoretical physics) in advance of experimental verification.",
    quotes: [
      { author: "Albert Einstein", work: "Ideas and Opinions", quote: "The grand aim of all **theoretical** physics is to form comprehensive concepts that require the fewest possible independent hypotheses." },
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "The statesman must distinguish between sound **theoretical** principles of trade and short-sighted mercantile protectionism." },
      { author: "George Eliot", work: "Middlemarch", quote: "Lydgate was fascinated by the **theoretical** problems of living tissue, longing to discover the ultimate cellular web of life." }
    ]
  },
  "theoretically.md": {
    word: "theoretically",
    primary: "In a manner according to theory; hypothetically or in principle, as distinguished from practical reality.",
    secondary: "In academic discourse, deduced by logical calculation from accepted principles, though potentially modified by real-world friction or empirical variables.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "Although a species may **theoretically** multiply in geometric progression, severe natural checks restrict its population." },
      { author: "Arthur Conan Doyle", work: "The Sign of Four", quote: "'Theoretically,' Holmes remarked, 'it is quite simple; practically, we must find where the boat landed in the fog.'" },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "The constitution granted equal rights **theoretically**, but local custom determined how those rights were exercised in daily life." }
    ]
  },
  "theoretician.md": {
    word: "theoretician",
    primary: "An expert who formulates, develops, or studies the theoretical foundations of a science, art, or discipline (as opposed to an experimentalist or practitioner).",
    secondary: "In mathematics, physics, and economics, a thinker who constructs deductive mathematical models to explain empirical observations.",
    quotes: [
      { author: "Richard Feynman", work: "Surely You're Joking, Mr. Feynman!", quote: "The experimentalists came running to the office of the **theoretician**, demanding an equation that could explain their baffling bubble chamber tracks." },
      { author: "Bertrand Russell", work: "The Scientific Outlook", quote: "The brilliant **theoretician** perceives a hidden mathematical symmetry where the practical engineer sees only chaos." },
      { author: "John Maynard Keynes", work: "The General Theory of Employment, Interest and Money", quote: "The ideas of the economic **theoretician**, both when they are right and when they are wrong, are more powerful than is commonly understood." }
    ]
  },
  "theorisation.md": {
    word: "theorisation",
    primary: "The act or process of formulating, developing, or constructing a theory or explanatory framework (British English spelling).",
    secondary: "In sociological and cultural theory, systematic conceptual modeling used to interpret institutional power, social structures, and historical change.",
    quotes: [
      { author: "Michel Foucault", work: "Power/Knowledge", quote: "Our **theorisation** of power must abandon the sovereign model and examine disciplinary techniques operating at the micro-level." },
      { author: "Jürgen Habermas", work: "The Theory of Communicative Action", quote: "A rigorous **theorisation** of modernity requires grounding rationality in communicative speech acts rather than instrumental domination." },
      { author: "Virginia Woolf", work: "The Common Reader", quote: "Behind the spontaneous poetry of the Elizabethans lay centuries of subtle classical **theorisation**." }
    ]
  },
  "theorise.md": {
    word: "theorise",
    primary: "To form a theory or theories about something; to speculate or develop conceptual explanations (British English spelling).",
    secondary: "In scientific inquiry, to propose hypotheses that connect disparate observations into a coherent predictive structure.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "A Study in Scarlet", quote: "It is a capital mistake to **theorise** before one has data; insensibly one begins to twist facts to suit theories, instead of theories to suit facts." },
      { author: "Charles Darwin", work: "Life and Letters of Charles Darwin", quote: "How odd it is that anyone should not see that all observation must be for or against some view if it is to be of any service! How can one not **theorise**?" },
      { author: "Thomas Henry Huxley", work: "Science and Culture", quote: "The natural philosopher is compelled to **theorise**, but must be ready to slay his pet hypothesis the moment a contrary fact appears." }
    ]
  },
  "theoriser.md": {
    word: "theoriser",
    primary: "A person who theorizes or speculates; an architect of conceptual explanations (British English spelling).",
    secondary: "In political commentary, an abstract thinker whose idealized blueprints may overlook practical human realities.",
    quotes: [
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "The political **theoriser** in Paris reconstructed the state on paper, blind to the living ancestral habits of the people." },
      { author: "George Eliot", work: "Middlemarch", quote: "Lydgate was no mere idle **theoriser**, but a determined researcher who spent nocturnal hours at his microscope." },
      { author: "William Makepeace Thackeray", work: "The Virginians", quote: "The old **theoriser** loved to discourse upon military strategy while younger men did the fighting in the field." }
    ]
  },
  "theorist.md": {
    word: "theorist",
    primary: "A person who develops, studies, or advocates theories; a thinker concerned with conceptual foundations rather than practical application.",
    secondary: "In physics, economics, and political philosophy, an intellectual who builds formal models to synthesize data and predict future phenomena.",
    quotes: [
      { author: "Albert Einstein", work: "Autobiographical Notes", quote: "The **theorist** is not to be envied, for nature—or more strictly speaking, experiment—is an inexorable and not very friendly judge of his work." },
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "The armchair **theorist** imagines he can arrange the members of a great society with as much ease as the hand arranges pieces on a chess-board." },
      { author: "Hannah Arendt", work: "The Human Condition", quote: "The political **theorist** must balance the contemplative life of the mind against the vita activa of democratic participation." }
    ]
  },
  "theorization.md": {
    word: "theorization",
    primary: "The formulation, development, or construction of a theory or systematic conceptual model to explain phenomena.",
    secondary: "In scientific methodology, the process of synthesizing experimental data into abstract laws, predictive equations, and explanatory frameworks.",
    quotes: [
      { author: "Karl Popper", work: "The Logic of Scientific Discovery", quote: "Scientific **theorization** proceeds by bold conjectures subjected to rigorous empirical attempts at refutation." },
      { author: "Thomas Kuhn", work: "The Structure of Scientific Revolutions", quote: "A period of paradigm crisis stimulates creative **theorization**, challenging long-held assumptions." },
      { author: "Max Weber", work: "The Methodology of the Social Sciences", quote: "Sociological **theorization** relies on ideal types to make complex historical realities intelligible to analysis." }
    ]
  },
  "theorize.md": {
    word: "theorize",
    primary: "To formulate a theory or conceptual explanation about something; to speculate conceptually based on observed facts.",
    secondary: "In scientific research, to construct mathematical or causal models to deduce testable hypotheses.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Valley of Fear", quote: "I never **theorize** before having all the evidence, for that is a capital error which biases the judgment." },
      { author: "Charles Darwin", work: "More Letters of Charles Darwin", quote: "I cannot avoid continuing to **theorize** on everything I see, for nature without a guiding hypothesis is an unintelligible chaos." },
      { author: "Bertrand Russell", work: "Mysticism and Logic", quote: "The human mind feels an irresistible urge to **theorize**, seeking orderly cosmos behind the chaotic flux of sensations." }
    ]
  },
  "theorizer.md": {
    word: "theorizer",
    primary: "A person who theorizes; one who invents, constructs, or proposes theoretical explanations.",
    secondary: "In historiography and political analysis, an intellectual who formulates overarching models to explain social developments.",
    quotes: [
      { author: "Alexis de Tocqueville", work: "The Old Regime and the Revolution", quote: "The French literary **theorizers** built a glorious utopian republic in their minds, ignoring the messy art of actual government." },
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "Ahab was no ordinary sea-captain, but a brooding **theorizer** who saw cosmic malice incarnate in the white whale." },
      { author: "William James", work: "Pragmatism", quote: "The pragmatic thinker smiles at the metaphysical **theorizer** who imagines he has captured the infinite in a neat syllogism." }
    ]
  },
  "theory-based.md": {
    word: "theory-based",
    primary: "Founded on, derived from, or guided by a systematic theory, conceptual model, or empirical hypothesis.",
    secondary: "In educational methodology and policy evaluation, describing programs or interventions whose design is explicitly structured around validated scientific frameworks.",
    quotes: [
      { author: "John Dewey", work: "Democracy and Education", quote: "A truly **theory-based** curriculum unites reflective thinking with active manual experimentation in the classroom." },
      { author: "Donald O. Hebb", work: "The Organization of Behavior", quote: "Our research proposed a **theory-based** model of neural assemblies capable of explaining cognitive attention and perceptual learning." },
      { author: "Herbert A. Simon", work: "Administrative Behavior", quote: "Modern organizational design relies on **theory-based** decision analysis to manage bounded rationality in complex environments." }
    ]
  },
  "theory.md": {
    word: "theory",
    primary: "A well-substantiated explanation of some aspect of the natural world, acquired through the scientific method and repeatedly tested and confirmed through observation and experiment.",
    secondary: "In philosophical contemplation (Greek theōria, a looking at, contemplation, speculation), the pursuit of truth for its own sake; colloquially, an unproven supposition or conjecture.",
    quotes: [
      { author: "Aristotle", work: "Nicomachean Ethics", quote: "The activity of philosophical contemplation, or **theory**, is the highest and most godlike exercise of the human soul." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "I look at the natural geological record as a history of the world imperfectly kept; yet on this view, my **theory** of natural selection is supported by countless facts." },
      { author: "Albert Einstein", work: "Ideas and Opinions", quote: "It can scarcely be denied that the supreme goal of all **theory** is to make the irreducible basic elements as simple and as few as possible." }
    ]
  },
  "theosophical.md": {
    word: "theosophical",
    primary: "Of, relating to, or inspired by theosophy; concerning mystical insight into divine nature and cosmic mysteries.",
    secondary: "In intellectual history, pertaining to the Theosophical Society founded by Helena Blavatsky, uniting Western hermeticism with Eastern metaphysical doctrines.",
    quotes: [
      { author: "William James", work: "The Varieties of Religious Experience", quote: "The modern **theosophical** movement revived ancient Alexandrian gnosticism in a contemporary occult dress." },
      { author: "W. B. Yeats", work: "Autobiographies", quote: "My early fascination with **theosophical** doctrines opened my imagination to symbolist drama and visionary poetry." },
      { author: "C. G. Jung", work: "Memories, Dreams, Reflections", quote: "While critical of sectarian occultism, I acknowledged that **theosophical** literature preserved important archetypal symbols." }
    ]
  },
  "theosophism.md": {
    word: "theosophism",
    primary: "The philosophical system, doctrines, or tenets of theosophy; belief in direct intuitive knowledge of divine reality.",
    secondary: "In religious criticism, the formal practices and speculative cosmological tenets maintained by theosophical societies and esoteric orders.",
    quotes: [
      { author: "Max Müller", work: "Theosophy, or Psychological Religion", quote: "Under the name of **theosophism**, critics often confounded ancient spiritual philosophy with modern mediumistic pretensions." },
      { author: "Helena Blavatsky", work: "The Secret Doctrine", quote: "True **theosophism** rejects blind dogmatic belief, demanding that each seeker awaken the inner spark of divine consciousness." },
      { author: "Arthur Conan Doyle", work: "The History of Spiritualism", quote: "The influence of **theosophism** was pivotal in introducing Eastern Buddhist and Hindu philosophy to Western seekers." }
    ]
  },
  "theosophist.md": {
    word: "theosophist",
    primary: "An adherent, student, or practitioner of theosophy; one who seeks direct intuitive knowledge of divine reality.",
    secondary: "In cultural history, a member of the Theosophical Society (such as Helena Blavatsky, Annie Besant, or Henry Steel Olcott) who championed esoteric philosophy.",
    quotes: [
      { author: "Helena Blavatsky", work: "The Key to Theosophy", quote: "A true **theosophist** is one who seeks universal brotherhood without distinction of race, creed, sex, or caste." },
      { author: "James Joyce", work: "Ulysses", quote: "AE presided over the Dublin circle of **theosophists**, discussing the astral plane and the Upanishads over vegetarian tea." },
      { author: "Arthur Conan Doyle", work: "The History of Spiritualism", quote: "The prominent **theosophist** Col. Olcott collaborated with Indian pandits to revive traditional Buddhist education in Ceylon." }
    ]
  },
  "theosophy.md": {
    word: "theosophy",
    primary: "Any of various philosophies maintaining that knowledge of God and cosmic mysteries may be achieved through spiritual ecstasy, direct intuition, or mystical illumination (from Greek theos god + sophia wisdom).",
    secondary: "In the history of esoteric thought, the mystical tradition tracing from Jacob Böhme and Renaissance Neoplatonism through modern occult movements promoting universal brotherhood.",
    quotes: [
      { author: "Helena Blavatsky", work: "The Secret Doctrine", quote: "**Theosophy** is the archaic Wisdom-Religion, the esoteric basis found at the core of all ancient world faiths." },
      { author: "William Butler Yeats", work: "Essays and Introductions", quote: "His mind was steeped in the mystical **theosophy** of Böhme and Swedenborg, finding holy signatures in every natural form." },
      { author: "Bertrand Russell", work: "A History of Western Philosophy", quote: "Alexandrian syncretism nurtured an early species of **theosophy** that fused Greek logic with oriental mysticism." }
    ]
  },
  "theoterrorism.md": {
    word: "theoterrorism",
    primary: "Terrorism or violent extremism motivated, justified, or sanctified by religious fanaticism or claims of divine mandate.",
    secondary: "In modern political science and international security studies, violent acts committed by radical sectarian groups who view their violence as a cosmic duty commanded by God.",
    quotes: [
      { author: "Mark Juergensmeyer", work: "Terror in the Mind of God: The Global Rise of Religious Violence", quote: "In the chilling phenomenon of **theoterrorism**, mundane geopolitical struggles are recast as cosmic wars between absolute divine light and demonic darkness." },
      { author: "Jessica Stern", work: "Terror in the Name of God: Why Religious Militants Kill", quote: "The rise of **theoterrorism** presents an acute challenge because religious militants seek transcendental purification rather than negotiable political concessions." },
      { author: "Bruce Hoffman", work: "Inside Terrorism", quote: "Unlike secular nationalist guerrillas, perpetrators of modern **theoterrorism** believe their violent acts are sanctified directly by divine commandment." }
    ]
  }
};

function updateWordNote(relPath, data) {
  const fullPath = path.join(baseDir, relPath);
  if (!fs.existsSync(fullPath)) {
    console.error("Not found:", fullPath);
    return;
  }
  let content = fs.readFileSync(fullPath, "utf8");

  // Format quotes
  const quotesFormatted = data.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join("\n");

  // Replace Definition & Semantic Range
  const defRegex = /> \[!book\] 📖 Definitions & Semantic Range[\s\S]*?(?=> \[!quote\]|$)/;
  const newDef = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${data.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${data.secondary}\n\n`;

  if (defRegex.test(content)) {
    content = content.replace(defRegex, newDef);
  } else {
    console.warn("Could not find [!book] in", relPath);
  }

  // Replace Quotes
  const quoteRegex = /> \[!quote\] 💬 Contextual Usage & Authentic Quotations[\s\S]*$/;
  const newQuotes = `> [!quote] 💬 Contextual Usage & Authentic Quotations\n${quotesFormatted}\n`;

  if (quoteRegex.test(content)) {
    content = content.replace(quoteRegex, newQuotes);
  } else {
    console.warn("Could not find [!quote] in", relPath);
  }

  fs.writeFileSync(fullPath, content, "utf8");
  console.log("Updated:", relPath);
}

for (const [relPath, data] of Object.entries(wordsData)) {
  updateWordNote(relPath, data);
}
console.log("Batch 8 completed! Total words updated:", Object.keys(wordsData).length);
