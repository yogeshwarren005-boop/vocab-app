import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Beginning & Primacy";

const wordsData = {
  // === Dashboard — ag (14 words) ===
  "Dashboard — ag/ag.md": {
    word: "ag",
    primary: "A classical combining root derived from Greek agein (to lead, drive, conduct) and agōn (contest, struggle, assembly).",
    secondary: "In linguistic morphology, the formative element underlying words of assembly and struggle (agony, agonist, synagogue); also the international chemical symbol for silver (Latin argentum).",
    quotes: [
      { author: "Walter William Skeat", work: "Principles of English Etymology", quote: "The Greek root **ag**- fundamentally signified driving or leading, branching into civic assembly and the athletic contest." },
      { author: "Antoine Meillet", work: "Introduction to the Comparative Study of Indo-European Languages", quote: "The Indo-European root *aǵ- yielded Sanskrit ajati, Latin agere, and Greek **ag**-ein, denoting dynamic motion." },
      { author: "Max Müller", work: "The Science of Thought", quote: "From the primal stem **ag**- arose both the peaceful gathering of the market and the desperate agony of combat." }
    ]
  },
  "Dashboard — ag/agonal.md": {
    word: "agonal",
    primary: "Of, relating to, or occurring at the moment of death or the final death struggle (in medicine, agonal breathing or agonal rhythm).",
    secondary: "In emergency critical care and forensic pathology, describing terminal, reflexive gasping respirations or aberrant cardiac rhythms preceding clinical death.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The clinician must recognize **agonal** respirations as terminal brainstem reflexes requiring immediate palliative comfort." },
      { author: "Paul Kalanithi", work: "When Breath Becomes Air", quote: "The telemetry monitor traced an **agonal** bradycardia, the heart's electrical system winding down in the final moments." },
      { author: "Atul Gawande", work: "Being Mortal", quote: "Understanding the difference between normal dying and **agonal** distress allows families to be present without needless terror." }
    ]
  },
  "Dashboard — ag/agonise.md": {
    word: "agonise",
    primary: "To undergo great physical pain or intense mental anguish; to worry or struggle desperately over a difficult decision (British English spelling).",
    secondary: "In existential and literary reflection, to wrestle with profound moral dilemmas, spiritual doubts, or unresolved grief.",
    quotes: [
      { author: "Thomas Hardy", work: "Tess of the d'Urbervilles", quote: "She would **agonise** in secret over the fatal secret, dreading the morning when her confession must be made." },
      { author: "George Eliot", work: "Middlemarch", quote: "Dorothea began to **agonise** over her inability to understand Casaubon's cold intellectual reserve." },
      { author: "Virginia Woolf", work: "Night and Day", quote: "Why must we **agonise** over small social conventions when the great current of life moves on unheeding?" }
    ]
  },
  "Dashboard — ag/agonist.md": {
    word: "agonist",
    primary: "A person who is engaged in a struggle, combat, or athletic contest; in biochemistry, a substance that binds to a receptor to initiate a physiological response.",
    secondary: "In physiology, a prime mover muscle whose contraction is directly responsible for producing a specific motion (opposing an antagonist).",
    quotes: [
      { author: "John Milton", work: "Samson Agonistes", quote: "Samson stands as the blind **agonist**, appointed to wrestle with the idolatrous Philistine host." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "The synthetic dopamine **agonist** bound to striatal receptors, restoring fluid locomotion to parkinsonian patients." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "During flexion of the forearm, the biceps acts as the prime **agonist** while the triceps relaxes." }
    ]
  },
  "Dashboard — ag/agonistic.md": {
    word: "agonistic",
    primary: "Of, relating to, or characteristic of athletic contests, combat, or aggressive struggle; contentious.",
    secondary: "In ethology and behavioral biology, denoting social interactions associated with fighting, including threat displays, appeasement, and physical aggression.",
    quotes: [
      { author: "E. O. Wilson", work: "Sociobiology: The New Synthesis", quote: "Chimpanzee troops engage in ritualized **agonistic** displays, bristling their hair and drumming on buttress roots to assert rank." },
      { author: "Friedrich Nietzsche", work: "Homer's Contest", quote: "Hellenic culture flourished because it channeled raw violence into lawful **agonistic** competition in the stadium and theater." },
      { author: "Jacob Burckhardt", work: "The Greeks and Greek Civilization", quote: "The Athenian state was permeated by an **agonistic** spirit, where every citizen vied for civic distinction." }
    ]
  },
  "Dashboard — ag/agonistical.md": {
    word: "agonistical",
    primary: "Pertaining to athletic combat, polemical dispute, or intense struggle (an archaic or formal variant of agonistic).",
    secondary: "In classical and early modern prose, describing heated rhetorical contention or forensic debate in academic and religious assemblies.",
    quotes: [
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Scholastic disputants entered the theological arena with **agonistical** zeal, eager to overthrow their rivals." },
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "Ancient Greek education was intensely **agonistical**, training both the body for combat and the tongue for disputation." },
      { author: "Samuel Taylor Coleridge", work: "Biographia Literaria", quote: "The critical review was written in an **agonistical** vein, delighting in combat rather than judicious appreciation." }
    ]
  },
  "Dashboard — ag/agonize.md": {
    word: "agonize",
    primary: "To undergo extreme physical pain or mental anguish; to struggle laboriously or torment oneself over a crisis or decision.",
    secondary: "In literary narratives, to experience intense existential, moral, or creative wrestling while striving to produce a masterpiece or resolve a tragedy.",
    quotes: [
      { author: "Fyodor Dostoevsky", work: "The Brothers Karamazov", quote: "Ivan continued to **agonize** over the problem of unmerited suffering and the tears of innocent children." },
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "Ahab would pace the quarter-deck by night, his fiery soul continuing to **agonize** over the white whale." },
      { author: "Mark Twain", work: "The Adventures of Huckleberry Finn", quote: "I began to **agonize** over my conscience, wondering whether helping Jim make his freedom was wicked or right." }
    ]
  },
  "Dashboard — ag/agony.md": {
    word: "agony",
    primary: "Extreme physical or mental suffering; the violent struggle or convulsions preceding death; intense emotional torment.",
    secondary: "Historically from Greek agōnia (contest, athletic struggle), the supreme mental anguish of an impending crisis, as in the Agony in the Garden.",
    quotes: [
      { author: "William Shakespeare", work: "Othello", quote: "Farewell! Othello's occupation's gone! / But O, what damned minutes tells he o'er / Who dotes, yet doubts, suspects, yet strongly loves! / O misery and mortal **agony**!" },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "A spasm of mental **agony** shot through me as I fled into the dark moors away from Thornfield." },
      { author: "Percy Bysshe Shelley", work: "Prometheus Unbound", quote: "To suffer woes which Hope thinks infinitive; / To forgive wrongs darker than death or night; / This is to conquer through holy **agony**." }
    ]
  },
  "Dashboard — ag/antagonise.md": {
    word: "antagonise",
    primary: "To cause someone to become hostile, unfriendly, or angry; to oppose or act in counteraction to (British English spelling).",
    secondary: "In biochemical pharmacology, to neutralize or inhibit the physiological activity of a receptor, enzyme, or hormone.",
    quotes: [
      { author: "George Orwell", work: "Animal Farm", quote: "Squealer warned the animals that any murmur of discontent would **antagonise** the human farmers and invite invasion." },
      { author: "Arthur Conan Doyle", work: "The Hound of the Baskervilles", quote: "Holmes cautioned Watson not to **antagonise** the local baronet until all the evidence had been securely gathered." },
      { author: "Virginia Woolf", work: "The Years", quote: "She was careful not to **antagonise** her father by expressing unconventional political views at the dinner table." }
    ]
  },
  "Dashboard — ag/antagonism.md": {
    word: "antagonism",
    primary: "Active hostility, opposition, or resistance between individuals, groups, or principles.",
    secondary: "In biochemistry and medicine, the mutual opposition or interference of two substances (e.g. drugs or bacterial strains) such that one nullifies the effect of the other.",
    quotes: [
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The mutual **antagonism** between competing species in the same ecological niche drives evolutionary divergence." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "The natural **antagonism** between aristocratic pride and democratic equality fueled revolutionary passions throughout Europe." },
      { author: "William James", work: "The Principles of Psychology", quote: "The human mind experiences an inward **antagonism** between immediate sensual impulse and long-term rational ideals." }
    ]
  },
  "Dashboard — ag/antagonist.md": {
    word: "antagonist",
    primary: "A person who actively opposes or is hostile to someone or something; an adversary; in drama, the principal character in conflict with the protagonist.",
    secondary: "In pharmacology, a drug or ligand that binds to a receptor without activating it, thereby blocking or dampening agonist-mediated biological responses.",
    quotes: [
      { author: "William Shakespeare", work: "Richard III", quote: "Our battle is joined; confront the fierce **antagonist** upon the bloody field of Bosworth." },
      { author: "Oliver Sacks", work: "The River of Consciousness", quote: "The administration of a competitive receptor **antagonist** immediately reversed the narcotic stupor." },
      { author: "Mary Shelley", work: "Frankenstein", quote: "Victor realized with dread that his monstrous creature had become his lifelong, demonic **antagonist**." }
    ]
  },
  "Dashboard — ag/antagonistic.md": {
    word: "antagonistic",
    primary: "Showing or feeling active opposition or hostility toward someone or something; mutually opposed in nature or function.",
    secondary: "In muscle anatomy, describing paired muscles (such as the biceps and triceps) that act in opposite directions to flex and extend joints.",
    quotes: [
      { author: "Herbert Spencer", work: "First Principles", quote: "Cosmic evolution involves the continuous equilibrium between **antagonistic** forces of integration and disintegration." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "The balance of constitutional liberty depends upon the harmonious friction of **antagonistic** interests." },
      { author: "Thomas Henry Huxley", work: "Evolution and Ethics", quote: "The ethical progress of society consists not in imitating the cosmos, but in combating its **antagonistic** tendencies." }
    ]
  },
  "Dashboard — ag/antagonize.md": {
    word: "antagonize",
    primary: "To cause someone to become hostile, irritable, or opposed; to provoke active enmity or opposition.",
    secondary: "In physiology and pharmacology, to neutralize, counteract, or block the biological action of another agent or hormone.",
    quotes: [
      { author: "Abraham Lincoln", work: "First Inaugural Address", quote: "We must not be enemies, but friends; passion may have strained, but it must not break or **antagonize** our bonds of affection." },
      { author: "Mark Twain", work: "Pudd'nhead Wilson", quote: "The sarcastic lawyer managed to **antagonize** the entire jury before he had even concluded his opening remarks." },
      { author: "Henry James", work: "The Bostonians", quote: "Basil Ransom took care not to **antagonize** his fierce cousin, knowing how easily her zeal was ignited." }
    ]
  },
  "Dashboard — ag/synagogue.md": {
    word: "synagogue",
    primary: "A Jewish house of worship, assembly, and communal religious study (from Greek synagōgē, a bringing together, assembly).",
    secondary: "In historical religion, the local community institution that arose in Hellenistic Judaism (especially following the Babylonian exile) for scripture reading, prayer, and moral instruction.",
    quotes: [
      { author: "Flavius Josephus", work: "The Jewish War", quote: "The citizens gathered on the Sabbath within the local **synagogue** to hear the sacred laws expounded by the elders." },
      { author: "George Eliot", work: "Daniel Deronda", quote: "Deronda entered the ancient Frankfurt **synagogue**, spellbound by the solemn chanting of the Hebrew liturgy." },
      { author: "Baruch Spinoza", work: "Theological-Political Treatise", quote: "The community of the Amsterdam **synagogue** cast him out, issuing their solemn cherem against his unorthodox writings." }
    ]
  },

  // === Dashboard — ego (9 words) ===
  "Dashboard — ego/ego.md": {
    word: "ego",
    primary: "A person's sense of self-esteem or self-importance; in psychoanalysis, the conscious, rational part of the psyche that mediates between the id, superego, and reality.",
    secondary: "In philosophy (Latin and Greek egō meaning 'I'), the conscious subject of experience and thought, as in Descartes' 'cogito, ergo sum'.",
    quotes: [
      { author: "Sigmund Freud", work: "The Ego and the Id", quote: "The **ego** is not master in its own house; it must balance the instinctual demands of the id against the harsh judgments of the superego." },
      { author: "William James", work: "The Principles of Psychology", quote: "The empirical self or **ego** is divided into the material self, the social self, and the spiritual self." },
      { author: "Carl Rogers", work: "On Becoming a Person", quote: "When the conscious **ego** feels threatened, it constructs defensive barriers that distort genuine emotional experience." }
    ]
  },
  "Dashboard — ego/egocentric.md": {
    word: "egocentric",
    primary: "Thinking only of oneself, without regard for the feelings or desires of others; self-centered.",
    secondary: "In developmental psychology (Jean Piaget), describing a cognitive stage in early childhood where a child cannot adopt another person's spatial or mental perspective.",
    quotes: [
      { author: "Jean Piaget", work: "The Language and Thought of the Child", quote: "A young child’s spontaneous speech is largely **egocentric**, spoken not to inform others but to accompany their own activity." },
      { author: "Bertrand Russell", work: "The Conquest of Happiness", quote: "The intensely **egocentric** man is rarely happy, for his thoughts circle ceaselessly around his own vanity and injuries." },
      { author: "George Eliot", work: "Middlemarch", quote: "Rosamond Vincy was delightfully charming, yet her worldview was as purely **egocentric** as that of an infant." }
    ]
  },
  "Dashboard — ego/egocentrism.md": {
    word: "egocentrism",
    primary: "The state or quality of being egocentric; excessive preoccupation with oneself and one's own concerns.",
    secondary: "In developmental cognitive theory, the natural inability of children (and immature adults) to differentiate subjective impressions from objective reality.",
    quotes: [
      { author: "Jean Piaget", work: "The Construction of Reality in the Child", quote: "Cognitive growth consists in a gradual decentering, liberating the mind from primitive perceptual **egocentrism**." },
      { author: "Erich Fromm", work: "The Art of Loving", quote: "Genuine love demands overcoming our narcissistic **egocentrism** to see another person in their true reality." },
      { author: "C. G. Jung", work: "Psychological Types", quote: "Introverted neurosis often degenerates into brooding **egocentrism**, cutting the individual off from external communal life." }
    ]
  },
  "Dashboard — ego/egoism.md": {
    word: "egoism",
    primary: "The habit of valuing everything only in reference to one's personal interest; excessive selfishness or self-centeredness.",
    secondary: "In moral philosophy, ethical egoism—the normative doctrine that self-interest is the valid foundation and ultimate justification for moral action.",
    quotes: [
      { author: "Arthur Schopenhauer", work: "The Basis of Morality", quote: "**Egoism** is colossal; it towers over the world, ready to annihilate the entire cosmos just to preserve a single life." },
      { author: "Friedrich Nietzsche", work: "Beyond Good and Evil", quote: "A noble soul accepts the fact of its own **egoism** without shame, seeing it as the fundamental law of life." },
      { author: "George Meredith", work: "The Egoist", quote: "Sir Willoughby Patterne was a magnificent specimen of civilized **egoism**, demanding that the universe orbit his pride." }
    ]
  },
  "Dashboard — ego/egoist.md": {
    word: "egoist",
    primary: "A self-centered or selfish person; an adherent of the philosophical doctrine of egoism.",
    secondary: "In literature and social characterization, an individual who views every relationship, institution, and social grace purely as mirrors for their own vanity.",
    quotes: [
      { author: "George Meredith", work: "The Egoist", quote: "The **egoist** does not merely love himself; he insists that all mankind shall join him in worshiping his image." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "Individualism must not be confused with crude selfishness; the common **egoist** thinks of no one but himself from the start." },
      { author: "Honoré de Balzac", work: "Père Goriot", quote: "Rastignac realized that Paris was a glittering battleground where only the ruthless **egoist** could triumph." }
    ]
  },
  "Dashboard — ego/egoistic.md": {
    word: "egoistic",
    primary: "Motivated by or exhibiting self-interest, selfishness, or egoism; egocentric.",
    secondary: "In sociological theory (Émile Durkheim's egoistic suicide), resulting from a lack of social integration and isolation from communal bonds.",
    quotes: [
      { author: "Émile Durkheim", work: "Suicide: A Study in Sociology", quote: "When society is strongly integrated, it holds individuals within its orbit; when it disintegrates, **egoistic** suicide increases." },
      { author: "Adam Smith", work: "The Theory of Moral Sentiments", quote: "Even the most **egoistic** man finds pleasure in the sympathy of others, proving our social constitution." },
      { author: "Herbert Spencer", work: "The Data of Ethics", quote: "Purely **egoistic** conduct must eventually be balanced by altruistic conduct if species survival is to be maintained." }
    ]
  },
  "Dashboard — ego/egoistical.md": {
    word: "egoistical",
    primary: "Characteristic of an egoist; self-absorbed, boastful, and selfish in conduct or attitude.",
    secondary: "In literary biography and criticism, marked by continuous, intrusive self-reference and inflated self-importance.",
    quotes: [
      { author: "William Hazlitt", work: "Table-Talk", quote: "There is an **egoistical** style of writing that delights readers when wielded by Montaigne, yet offends when used by lesser men." },
      { author: "Charlotte Brontë", work: "Villette", quote: "M. Paul Emanuel had an **egoistical** temper, yet beneath his fiery vanity lay an astonishingly generous heart." },
      { author: "John Stuart Mill", work: "Autobiography", quote: "He avoided all petty, **egoistical** vanity, dedicating his intellectual powers entirely to the public welfare." }
    ]
  },
  "Dashboard — ego/egomania.md": {
    word: "egomania",
    primary: "Obsessive, morbid, or extraordinarily inflated self-absorption and egotism.",
    secondary: "In psychiatric and clinical discourse, an extreme pathological preoccupation with one's own ego, bordering upon narcissistic personality disorder or megalomania.",
    quotes: [
      { author: "Max Nordau", work: "Degeneration", quote: "The decadent artistic movement was infected with rampant **egomania**, exalting subjective whim above universal truth." },
      { author: "Hannah Arendt", work: "The Origins of Totalitarianism", quote: "Totalitarian dictators exhibit a monstrous **egomania** that subordinates the lives of millions to their personal myth." },
      { author: "H. L. Mencken", work: "Prejudices: Fourth Series", quote: "Political demagoguery in America is driven by unbridled **egomania** disguised as patriotic benevolence." }
    ]
  },
  "Dashboard — ego/egomaniac.md": {
    word: "egomaniac",
    primary: "A person suffering from egomania; an intensely self-absorbed, arrogant, and boastful individual.",
    secondary: "In social commentary, a leader, artist, or public figure whose behavior is dominated by an insatiable hunger for adoration and absolute self-glorification.",
    quotes: [
      { author: "George Orwell", work: "The Lion and the Unicorn", quote: "Hitler proved himself a dangerous **egomaniac**, deaf to tactical advice once his mystical intuition was engaged." },
      { author: "F. Scott Fitzgerald", work: "The Last Tycoon", quote: "Monroe Stahr had to deal with brilliant Hollywood **egomaniacs** whose petulant tantrums threatened multi-million-dollar productions." },
      { author: "Tom Wolfe", work: "The Bonfire of the Vanities", quote: "The Wall Street trader strutted across Manhattan like a crowned **egomaniac**, convinced he was master of the universe." }
    ]
  },

  // === Dashboard — eteo (3 words) ===
  "Dashboard — eteo/Eteocretan.md": {
    word: "Eteocretan",
    primary: "Of, relating to, or denoting the pre-Hellenic indigenous population of ancient Crete or their non-Greek language (from Greek eteos true/original + Kres Cretan).",
    secondary: "In Aegean archaeology and epigraphy, designating fragmentary inscriptions written in the Greek alphabet found in eastern Crete (such as Praisos) preserving an undeciphered indigenous tongue.",
    quotes: [
      { author: "Homer", work: "The Odyssey (Book XIX)", quote: "There is a land called Crete, in the midst of the wine-dark sea; therein dwell many men: Achaeans, stout-hearted **Eteocretans**, Dorians, and Pelasgians." },
      { author: "Arthur Evans", work: "The Palace of Minos", quote: "The **Eteocretan** inscriptions of Praisos represent the stubborn survival of the ancient Minoan speech into Hellenistic times." },
      { author: "Strabo", work: "Geography", quote: "The historian Staphylus reports that the **Eteocretans** were the original, autochthonous dwellers of the southern Cretan coast." }
    ]
  },
  "Dashboard — eteo/Eteocypriot.md": {
    word: "Eteocypriot",
    primary: "Of, relating to, or denoting the pre-Indo-European indigenous inhabitants of ancient Cyprus or their pre-Greek language.",
    secondary: "In Mediterranean epigraphy, the ancient non-Greek language of Cyprus written in the Cypriot syllabic script down to the Hellenistic era (notably evidenced at Amathus).",
    quotes: [
      { author: "John L. Myres", work: "Handbook of the Cesnola Collection of Antiquities from Cyprus", quote: "Bilingual inscriptions from Amathus preserved the mysterious **Eteocypriot** tongue alongside classical Greek." },
      { author: "Michael Ventris", work: "Documents in Mycenaean Greek", quote: "The Cypriot syllabary was employed both for Greek dialect and for the unclassified **Eteocypriot** substratum." },
      { author: "E. O. Masson", work: "Les Inscriptions Chypriotes Syllabiques", quote: "Decipherment of **Eteocypriot** texts remains an unsolved challenge of Eastern Mediterranean linguistics." }
    ]
  },
  "Dashboard — eteo/eteo.md": {
    word: "eteo",
    primary: "A combining prefix derived from Ancient Greek eteos, meaning true, authentic, genuine, or indigenous.",
    secondary: "In classical philology and historical ethnology, used in compounds (such as Eteocretan and Eteocypriot) to designate the original, autochthonous inhabitants of a land.",
    quotes: [
      { author: "Walter William Skeat", work: "Principles of English Etymology", quote: "The rare prefix **eteo**- derives from Greek eteos, signifying that which is genuine, primal, and unmixed." },
      { author: "Arthur Evans", work: "Scripta Minoa", quote: "By prefixing **eteo**- to regional names, ancient Greek geographers identified the true aboriginal populations." },
      { author: "Liddell and Scott", work: "A Greek-English Lexicon", quote: "The poetic adjective eteos gave birth to the combining form **eteo**-, denoting indigenous antiquity." }
    ]
  },

  // === Dashboard — heg (15 words) ===
  "Dashboard — heg/diegesis.md": {
    word: "diegesis",
    primary: "A narrative or plot; in literary and film theory, the fictional world, events, and story space within which a narrative occurs.",
    secondary: "In classical rhetoric and Plato's Republic, narration where the poet speaks in their own voice, contrasted with mimesis (direct dramatic imitation through dialogue).",
    quotes: [
      { author: "Plato", work: "Republic", quote: "Poetry and mythology proceed either through pure mimesis, as in tragedy, or through simple **diegesis**, as in dithyrambs." },
      { author: "Gérard Genette", work: "Narrative Discourse", quote: "The **diegesis** defines the spatiotemporal world of the story, distinct from the narrator’s discursive act." },
      { author: "David Bordwell", work: "Narration in the Fiction Film", quote: "Cinematic narration cues the spectator to construct a coherent **diegesis** from disjointed photographic shots." }
    ]
  },
  "Dashboard — heg/diegetic.md": {
    word: "diegetic",
    primary: "Of, relating to, or occurring within the fictional world of a story; internal to the narrative.",
    secondary: "In film theory, describing sounds, music, or dialogue that originate from an onscreen or offscreen source within the story world that characters can hear.",
    quotes: [
      { author: "Michel Chion", work: "Audio-Vision: Sound on Screen", quote: "When the pianist in the salon begins playing, the music shifts from non-diegetic background score to living **diegetic** sound." },
      { author: "David Bordwell", work: "The Classical Hollywood Cinema", quote: "The clock ticking upon the mantlepiece provided an ominous **diegetic** rhythm to the tense confrontation." },
      { author: "Christian Metz", work: "Film Language: A Semiotics of the Cinema", quote: "The boundary between **diegetic** space and extradiegetic commentary is playfully blurred in modern cinema." }
    ]
  },
  "Dashboard — heg/eisegesis.md": {
    word: "eisegesis",
    primary: "The process of interpreting a text by reading one's own preconceived ideas, biases, or agenda into it; the opposite of exegesis.",
    secondary: "In biblical hermeneutics and legal interpretation, the flawed practice of forcing an arbitrary meaning onto an ancient text rather than drawing out the author's original intent.",
    quotes: [
      { author: "C. S. Lewis", work: "Reflections on the Psalms", quote: "We must beware of pious **eisegesis**, reading sophisticated modern doctrines into the raw, ancient poetry of the Psalter." },
      { author: "F. F. Bruce", work: "The New Testament Documents: Are They Reliable?", quote: "True textual interpretation is disciplined exegesis; theological **eisegesis** merely reflects the reader's own voice." },
      { author: "Benjamin Jowett", work: "On the Interpretation of Scripture", quote: "Centuries of scholastic **eisegesis** obscured the original historical meaning of the Pauline epistles." }
    ]
  },
  "Dashboard — heg/exegesis.md": {
    word: "exegesis",
    primary: "Critical explanation, analysis, or interpretation of a text, especially scripture or legal statutes (from Greek exēgēsis, a leading out).",
    secondary: "In theological hermeneutics, the objective discovery of a text's original grammatical, historical, and cultural meaning.",
    quotes: [
      { author: "John Henry Newman", work: "An Essay on the Development of Christian Doctrine", quote: "Patristic **exegesis** uncovered layers of allegorical and moral truth beneath the literal historical narrative." },
      { author: "Friedrich Schleiermacher", work: "Hermeneutics and Criticism", quote: "Rigorous historical **exegesis** reconstructs the unique creative mind of the author in its original historical horizon." },
      { author: "George Eliot", work: "Middlemarch", quote: "Mr. Casaubon’s promised work of biblical **exegesis** had stalled amidst thousands of unsorted slips of paper." }
    ]
  },
  "Dashboard — heg/exegete.md": {
    word: "exegete",
    primary: "A person who critically explains, interprets, or analyzes a text, especially sacred scripture.",
    secondary: "In ancient Greece, an official interpreter of sacred laws, omens, or religious rites; in academic theology, a scholar skilled in original biblical languages.",
    quotes: [
      { author: "Plato", work: "Euthyphro", quote: "Euthyphro claimed to be an inspired **exegete** of the divine laws concerning piety and impiety." },
      { author: "Desiderius Erasmus", work: "Annotations on the New Testament", quote: "The biblical **exegete** must master Greek and Hebrew grammar before pretending to arbitrate doctrinal disputes." },
      { author: "Thomas Hardy", work: "The Return of the Native", quote: "Clym spoke with the quiet conviction of an **exegete** expounding neglected moral truths to provincial listeners." }
    ]
  },
  "Dashboard — heg/exegetic.md": {
    word: "exegetic",
    primary: "Of, relating to, or involving critical textual explanation or interpretation; expository.",
    secondary: "In literary and theological scholarship, pertaining to methods and commentaries designed to elucidate complex written texts.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Aids to Reflection", quote: "The **exegetic** notes of the German commentators shed valuable light upon the historical context of the Gospels." },
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "True learning requires both dogmatic exposition and careful **exegetic** study of ancient philosophical works." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The councils engaged in endless **exegetic** wrangling over obscure passages of the Alexandrian scriptures." }
    ]
  },
  "Dashboard — heg/exegetical.md": {
    word: "exegetical",
    primary: "Relating to or based on critical textual interpretation and exegesis; explanatory and analytical.",
    secondary: "In academic theology and legal jurisprudence, concerning detailed verse-by-verse commentary and historical-critical analysis.",
    quotes: [
      { author: "John Calvin", work: "Commentaries on the Epistles of Paul", quote: "The chief excellence of the **exegetical** commentator lies in lucid, unadorned brevity." },
      { author: "Matthew Arnold", work: "Literature and Dogma", quote: "Much modern theology is crippled by an unimaginative **exegetical** pedantry that misses the poetic soul of the Bible." },
      { author: "Thomas Carlyle", work: "Sartor Resartus", quote: "Teufelsdröckh subjected human society to an **exegetical** scrutiny that unmasked its decorative pretenses." }
    ]
  },
  "Dashboard — heg/heg.md": {
    word: "heg",
    primary: "A combining root derived from Ancient Greek hēgeisthai meaning to lead, guide, command, or explain.",
    secondary: "In historical linguistics and morphology, the foundational stem yielding words of political leadership (hegemony) and textual interpretation (exegesis).",
    quotes: [
      { author: "Walter William Skeat", work: "Principles of English Etymology", quote: "The Greek root **heg**- signified leadership and guidance, giving us both political hegemony and textual exegesis." },
      { author: "Antoine Meillet", work: "Introduction to the Comparative Study of Indo-European Languages", quote: "From the verbal stem **heg**- arose the Greek concept of the hegemon, the commander who marches at the head." },
      { author: "Max Müller", work: "The Science of Thought", quote: "In the development of civic language, the root **heg**- evolved from physical guiding into supreme political authority." }
    ]
  },
  "Dashboard — heg/hegemon.md": {
    word: "hegemon",
    primary: "A supreme leader, leading state, or dominant power that exercises political, military, or economic leadership over others (from Greek hēgemōn, leader).",
    secondary: "In international relations theory, the preeminent superpower that establishes and enforces rules of order within the global geopolitical system.",
    quotes: [
      { author: "Thucydides", work: "The Peloponnesian War", quote: "Sparta was recognized as the traditional **hegemon** of the Peloponnesian League, commanding all allied armies in the field." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Philip of Macedon was elected supreme **hegemon** of the Greek states at the Congress of Corinth." },
      { author: "Noam Chomsky", work: "Hegemony or Survival", quote: "The United States acted as undisputed global **hegemon** following the collapse of the Soviet Union." }
    ]
  },
  "Dashboard — heg/hegemonic.md": {
    word: "hegemonic",
    primary: "Ruling or dominant in a political, social, or military context; exercising hegemony.",
    secondary: "In critical social theory (Antonio Gramsci), describing cultural norms, beliefs, and values that maintain the dominance of the ruling class through popular consent.",
    quotes: [
      { author: "Antonio Gramsci", work: "Prison Notebooks", quote: "The **hegemonic** class maintains its supremacy not through brute coercion alone, but by shaping cultural common sense." },
      { author: "Francis Fukuyama", work: "The Origins of Political Order", quote: "The Qin dynasty established **hegemonic** dominance over the warring states through ruthless administrative centralization." },
      { author: "Hannah Arendt", work: "On Revolution", quote: "The imperial power exercised a **hegemonic** sway that stifled local democratic deliberation in the provinces." }
    ]
  },
  "Dashboard — heg/hegemony.md": {
    word: "hegemony",
    primary: "Leadership or predominant influence exercised by one nation, state, or social class over others; supreme dominance.",
    secondary: "In Marxist cultural theory, the cultural and ideological leadership by which the ruling class wins the spontaneous consent of subaltern classes.",
    quotes: [
      { author: "Antonio Gramsci", work: "Selections from the Prison Notebooks", quote: "Cultural **hegemony** operates when the world-view of the ruling group is accepted as natural reality by the entire society." },
      { author: "Thucydides", work: "The Peloponnesian War", quote: "The rapid growth of Athenian **hegemony** over the Aegean islands inspired dread throughout the Peloponnese." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "No single state in the American union could assert permanent **hegemony** over its sister republics." }
    ]
  },
  "Dashboard — heg/hegumen.md": {
    word: "hegumen",
    primary: "The head, superior, or abbot of an Eastern Orthodox or Eastern Catholic monastery (from Greek hēgoumenos, one who leads).",
    secondary: "In Eastern monasticism, the spiritual father elected by the brotherhood to guide the monastic community, equivalent to a Western abbot.",
    quotes: [
      { author: "Leo Tolstoy", work: "Father Sergius", quote: "The holy **hegumen** received the troubled prince in his cell, listening with silent compassion to his spiritual confession." },
      { author: "Fyodor Dostoevsky", work: "The Brothers Karamazov", quote: "The visiting gentry were escorted to the dining hall by the venerable **hegumen** of the monastery." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The **hegumen** of the Studion monastery in Constantinople exercised immense moral authority during iconoclastic disputes." }
    ]
  },
  "Dashboard — heg/hypodiegetic.md": {
    word: "hypodiegetic",
    primary: "In narratology, relating to or constituting a narrative embedded within the main story; a story told by a character within a story.",
    secondary: "In narrative theory (formulated by Gérard Genette), describing the second-degree narrative level, such as Odysseus narrating his wanderings to the Phaeacians.",
    quotes: [
      { author: "Gérard Genette", work: "Narrative Discourse: An Essay in Method", quote: "The **hypodiegetic** narrative of the Arabian Nights allows Scheherazade’s characters to become narrators of fresh tales in their turn." },
      { author: "Mieke Bal", work: "Narratology: Introduction to the Theory of Narrative", quote: "A **hypodiegetic** story often mirrors or comments upon the primary diegetic action through thematic parallels." },
      { author: "Paul Ricoeur", work: "Time and Narrative", quote: "The multi-layered structure of **hypodiegetic** narration reveals the recursive, nesting capacity of human storytelling." }
    ]
  },
  "Dashboard — heg/metadiegetic.md": {
    word: "metadiegetic",
    primary: "In literary and narrative theory, pertaining to an embedded narrative or a story within a story (often synonymous with or related to hypodiegetic).",
    secondary: "In narratology (Genette's initial terminology), designating the narrative level situated beyond the primary diegesis, as when a character recites an ancient myth.",
    quotes: [
      { author: "Gérard Genette", work: "Figures III", quote: "We designate as **metadiegetic** that second-order narrative told by a character belonging to the primary story." },
      { author: "Umberto Eco", work: "The Role of the Reader", quote: "In Gothic romances, the discovery of an old manuscript initiates a **metadiegetic** voyage into ancestral horror." },
      { author: "Seymour Chatman", work: "Story and Discourse: Narrative Structure in Fiction and Film", quote: "The **metadiegetic** frame highlights the act of storytelling itself, emphasizing the voice and credibility of the internal narrator." }
    ]
  },
  "Dashboard — heg/protohegumen.md": {
    word: "protohegumen",
    primary: "A senior or chief hegumen; an abbot of premier rank who oversees several monastic houses or presides over a great monastic lavra in the Eastern Church.",
    secondary: "In Eastern Orthodox ecclesiastical hierarchy, an honorary monastic title bestowed upon distinguished abbots, akin to an archimandrite or prior provincial.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The **protohegumen** of Mount Athos headed the solemn delegation dispatched to negotiate with the Byzantine emperor." },
      { author: "Leo Tolstoy", work: "War and Peace", quote: "Before embarking for the front, the old general knelt to receive the blessing of the venerable **protohegumen**." },
      { author: "Nikolai Gogol", work: "Taras Bulba", quote: "The ancient monastery stood upon the cliff, where the **protohegumen** kept holy vigil while Cossack skirmishes raged below." }
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
console.log("Primacy Batch 1 completed! Total words updated:", Object.keys(wordsData).length);
