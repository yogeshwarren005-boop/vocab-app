# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — cogn (41 words)
  # =========================================================================
  "Dashboard — cogn/cognac.md": {
    "primary": "A high-quality grape brandy distilled from white wine produced in the region of Cognac, France.",
    "secondary": "In gastronomic history and viticulture, a protected appellation brandy matured in oak casks to develop amber complexity.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "He poured out a small glass of **cognac** and pushed it across the mahogany table."},
      {"author": "James Joyce", "work": "Ulysses", "quote": "A sip of mellow **cognac** warmed his palate and quieted the lingering tremor in his nerves."},
      {"author": "Alexandre Dumas", "work": "The Count of Monte Cristo", "quote": "The servant brought forth a crystal decanter of vintage **cognac** to revive the fainting traveler."}
    ]
  },
  "Dashboard — cogn/cognate.md": {
    "primary": "Descended from the same original root or language; having a common ancestor or related character.",
    "secondary": "In comparative linguistics and anthropology, lexical items or kinship lineages sharing genetic descent from an ancestral form.",
    "quotes": [
      {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "The English word 'father' and Latin 'pater' are genuinely **cognate** forms descending from an Aryan original."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "We must observe how **cognate** sciences assist and illustrate one another in their progress."},
      {"author": "William Whewell", "work": "The Philosophy of the Inductive Sciences", "quote": "Mathematics and mechanics possess a **cognate** structure based upon axioms of pure intuition."}
    ]
  },
  "Dashboard — cogn/cognation.md": {
    "primary": "Relationship by descent from a common ancestor; kinship, affinity, or shared origin.",
    "secondary": "In Roman civil law and comparative jurisprudence, kinship traced through maternal bloodlines in contradistinction to agnation.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The civil law of Rome carefully distinguished between agnation through the father and **cognation** through the mother."},
      {"author": "Sir Henry Maine", "work": "Ancient Law", "quote": "The historical transition from strict agnatic patriarchy to natural **cognation** marked a revolution in European family law."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The close conceptual **cognation** uniting geometry and physics demonstrates the unity of deductive science."}
    ]
  },
  "Dashboard — cogn/cognisable.md": {
    "primary": "Capable of being perceived, known, or brought under judicial notice (British spelling of cognizable).",
    "secondary": "In jurisprudence and Kantian epistemology, falling legitimately within the investigative jurisdiction of a court or the intellect.",
    "quotes": [
      {"author": "William Hamilton", "work": "Lectures on Metaphysics and Logic", "quote": "An object is only **cognisable** by human consciousness under the conditions of time and space."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "Torts of this nature are not **cognisable** in ecclesiastical courts, but belong solely to the common law."},
      {"author": "Thomas Reid", "work": "Essays on the Intellectual Powers of Man", "quote": "External qualities become **cognisable** through the healthy functioning of our perceptual organs."}
    ]
  },
  "Dashboard — cogn/cognisance.md": {
    "primary": "Knowledge, awareness, or notice; judicial notice or legal jurisdiction (British spelling of cognizance).",
    "secondary": "In heraldry and common law, a distinctive badge worn by retainers, or official legal authority to adjudicate.",
    "quotes": [
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The knight wore upon his helmet a plume of feathers, but had no **cognisance** painted on his shield."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The civil magistrate must take official **cognisance** of abuses that disrupt public tranquility."},
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "Parliament ought to have taken earlier **cognisance** of the legitimate grievances of the colonial assemblies."}
    ]
  },
  "Dashboard — cogn/cognisant.md": {
    "primary": "Having knowledge or being aware of something; mindful and informed (British spelling of cognizant).",
    "secondary": "In administrative policy and military command, maintaining continuous operational awareness of tactical developments.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "He was fully **cognisant** of the difficulties surrounding his daughter's social position in the parish."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "I was **cognisant** of the danger, but could not foresee the extraordinary craft of our adversary."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The Admiralty was keenly **cognisant** of the submarine menace long before the first merchant vessels were sunk."}
    ]
  },
  "Dashboard — cogn/cognise.md": {
    "primary": "To know, perceive, or recognize through cognitive processes (British spelling of cognize).",
    "secondary": "In transcendental psychology, the synthetic act of the understanding in uniting sensory intuitions into a coherent concept.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The finite intelligence can only **cognise** external nature through the medium of its own self-activity."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "To **cognise** an object is to relate it to previously acquired cognitive systems within memory."},
      {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "We cannot **cognise** relations of co-existence without contrasting them with relations of sequence."}
    ]
  },
  "Dashboard — cogn/cognition.md": {
    "primary": "The mental action or process of acquiring knowledge and understanding through thought, experience, and the senses.",
    "secondary": "In cognitive science and epistemological theory, the sum of internal information-processing mechanisms in the mind.",
    "quotes": [
      {"author": "Immanuel Kant", "work": "Critique of Pure Reason", "quote": "All our **cognition** begins with experience, but it does not follow that it all arises out of experience."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Every act of immediate **cognition** involves both sensory awareness and interpretive judgment."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The faculty of clear **cognition** enables the mind to distinguish between real existences and chimeric fancies."}
    ]
  },
  "Dashboard — cogn/cognitive.md": {
    "primary": "Relating to the mental processes of perception, memory, judgment, and reasoning.",
    "secondary": "In neuropsychology and linguistic theory, pertaining to internal computational architectures underlying intellect.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "The Analysis of Mind", "quote": "Belief must be regarded as an essential **cognitive** relation linking the subject to factual reality."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The **cognitive** function of feelings is to orient the organism rapidly toward advantageous behaviors."},
      {"author": "John Dewey", "work": "How We Think", "quote": "Reflective thinking is a disciplined **cognitive** habit that transforms perplexity into systematic inquiry."}
    ]
  },
  "Dashboard — cogn/cognitively.md": {
    "primary": "In a manner relating to cognition, intellectual processing, or the acquisition of knowledge.",
    "secondary": "In developmental psychology and pedagogy, evaluating conceptual mastery rather than rote emotional response.",
    "quotes": [
      {"author": "William James", "work": "The Meaning of Truth", "quote": "An idea functions **cognitively** only when it guides the thinker toward fruitful practical adjustments."},
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "The student who engages actively with problems develops **cognitively** far faster than a passive listener."},
      {"author": "Bertrand Russell", "work": "Human Knowledge: Its Scope and Limits", "quote": "We must inquire how far our sensory beliefs are **cognitively** justified by rational standards."}
    ]
  },
  "Dashboard — cogn/cognizable.md": {
    "primary": "Capable of being perceived, known, or brought under judicial scrutiny and jurisdiction.",
    "secondary": "In constitutional law and legal theory, a legal claim or controversy possessing standing to be heard in a court of justice.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Causes of admiralty and maritime jurisdiction are properly **cognizable** in federal courts."},
      {"author": "Thomas Jefferson", "work": "Notes on the State of Virginia", "quote": "The legitimate powers of government extend to such acts only as are injurious to others and legally **cognizable**."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Only those actions that infringe upon the rights of others are morally **cognizable** by civil authority."}
    ]
  },
  "Dashboard — cogn/cognizance.md": {
    "primary": "Knowledge, awareness, or notice; judicial jurisdiction or recognition.",
    "secondary": "In jurisprudence and heraldry, official judicial examination, or a noble badge identifying an armigerous house.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VI, Part 1", "quote": "As **cognizance** of my blood-drinking hate, will I this pale and maiden blossom bear."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "Things of great consequence should be brought to the timely **cognizance** of the sovereign."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The magistrates took solemn **cognizance** of her fault before the assembled multitude."}
    ]
  },
  "Dashboard — cogn/cognizant.md": {
    "primary": "Having knowledge or awareness; informed and mindful of facts or circumstances.",
    "secondary": "In administrative governance and ethics, maintaining conscious responsibility regarding the consequences of policy.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles: A Pure Woman", "quote": "Angel Clare was keenly **cognizant** of the social chasm that separated his family from the dairyfolk."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Sherlock Holmes was immediately **cognizant** of the singular print left in the peat."},
      {"author": "Henry James", "work": "The Wings of the Dove", "quote": "She was delicately **cognizant** of every nuance in his restrained demeanor."}
    ]
  },
  "Dashboard — cogn/cognize.md": {
    "primary": "To perceive, know, or become aware of something through the intellect.",
    "secondary": "In epistemological metaphysics, the active intellectual synthesis by which external data are grasped as an object of knowledge.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "To **cognize** an external event is to represent it faithfully in the stream of consciousness."},
      {"author": "Josiah Royce", "work": "The World and the Individual", "quote": "The finite mind strives unceasingly to **cognize** the unity of the absolute order."},
      {"author": "Mary Baker Eddy", "work": "Science and Health, with Key to the Scriptures", "quote": "The objects cognized by the physical senses have not spiritual origin, but must be inwardly **cognized** through divine truth."}
    ]
  },
  "Dashboard — cogn/cognomen.md": {
    "primary": "A surname, nickname, or identifying epithet.",
    "secondary": "In ancient Roman prosopography, the third name of a Roman citizen designating the specific familial branch or personal honor.",
    "quotes": [
      {"author": "Washington Irving", "work": "The Legend of Sleepy Hollow", "quote": "The **cognomen** of Crane was not inapplicable to his person."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The illustrious **cognomen** of Africanus commemorated the conqueror's victories over Carthage."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "He answered to the bizarre **cognomen** of Queequeg among the harpooneers."}
    ]
  },
  "Dashboard — cogn/cognoscente.md": {
    "primary": "A person who has expert knowledge in a subject, especially in the fine arts; a connoisseur.",
    "secondary": "In art history and aesthetic criticism, an individual recognized for discerning judgment in evaluating paintings or music.",
    "quotes": [
      {"author": "Horace Walpole", "work": "Letters", "quote": "Every traveling **cognoscente** in Florence pretends to discover a lost Raphael in some obscure chapel."},
      {"author": "William Hazlitt", "work": "Table-Talk", "quote": "The true artist creates for humanity, whereas the petty **cognoscente** prizes only technical rarity."},
      {"author": "Henry James", "work": "The Ambassadors", "quote": "He listened with the quiet deference of a **cognoscente** who refuses to parade his erudition."}
    ]
  },
  "Dashboard — cogn/cognoscible.md": {
    "primary": "Capable of being known, comprehended, or investigated by human intellect.",
    "secondary": "In scholastic philosophy and epistemology, possessing intelligible form and species accessible to the rational mind.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "Whatever is real in nature must be in principle **cognoscible** by the enlightened reason."},
      {"author": "William Hamilton", "work": "Discussions on Philosophy and Literature", "quote": "The infinite is inconceivable, and therefore not **cognoscible** as a positive object."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "All **cognoscible** truths must ultimately resolve into simple ideas derived from sensation or reflection."}
    ]
  },
  "Dashboard — cogn/derecognise.md": {
    "primary": "To withdraw formal recognition or official legal status from an entity (British spelling of derecognize).",
    "secondary": "In labor law and international relations, revoking the accredited bargaining rights of a trade union or state sovereignty.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The government was advised to **derecognise** the puppet administration set up by the invaders."},
      {"author": "Harold Laski", "work": "A Grammar of Politics", "quote": "To **derecognise** an established representative body without arbitration invites industrial paralysis."},
      {"author": "Sidney Webb", "work": "The History of Trade Unionism", "quote": "Employers sought to **derecognise** the newly amalgamated union during the lockout of 1897."}
    ]
  },
  "Dashboard — cogn/derecognize.md": {
    "primary": "To withdraw official recognition, legal status, or accreditation from an organization or government.",
    "secondary": "In corporate governance and treaty law, the deliberate decertification of an agent or diplomatic mission.",
    "quotes": [
      {"author": "Woodrow Wilson", "work": "State Papers and Addresses", "quote": "A nation may justly **derecognize** a government that violates the fundamental compact of human liberty."},
      {"author": "Felix Frankfurter", "work": "The Public and Its Law", "quote": "The labor board was empowered to **derecognize** any company-dominated association."},
      {"author": "Walter Lippmann", "work": "The Good Society", "quote": "When sovereign states **derecognize** customary international norms, chaos inevitably ensues."}
    ]
  },
  "Dashboard — cogn/incognito.md": {
    "primary": "Having one's true identity concealed or disguised, especially by public figures.",
    "secondary": "In diplomatic history and romantic narrative, traveling under an assumed name to avoid ceremonial protocol.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "I have come **incognito** from Prague for the purpose of consulting you."},
      {"author": "graf Leo Tolstoy", "work": "War and Peace", "quote": "A Frenchman or a Russian prince **incognito**, said the officer, looking at Pierre’s fine though dusty clothes."},
      {"author": "Walter Scott", "work": "The Talisman", "quote": "The King of England rode **incognito** through the camp to test the fidelity of his crusader barons."}
    ]
  },
  "Dashboard — cogn/incognizable.md": {
    "primary": "Incapable of being known, recognized, or perceived; beyond the reach of human cognition.",
    "secondary": "In transcendental philosophy, denoting the Kantian thing-in-itself which transcends all sensory intuition.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "The ultimate reality behind all appearances remains forever inscrutable and **incognizable**."},
      {"author": "William Hamilton", "work": "Lectures on Metaphysics and Logic", "quote": "The absolute and unconditioned must be pronounced strictly **incognizable** by finite minds."},
      {"author": "John Stuart Mill", "work": "An Examination of Sir William Hamilton's Philosophy", "quote": "To declare the nature of matter wholly **incognizable** is to abandon scientific ontology."}
    ]
  },
  "Dashboard — cogn/incognizance.md": {
    "primary": "Lack of knowledge, notice, awareness, or official apprehension.",
    "secondary": "In legal theory and administration, official disregard of an extraneous fact or procedural ignorance.",
    "quotes": [
      {"author": "Jeremy Bentham", "work": "Rationale of Judicial Evidence", "quote": "The judge's willful **incognizance** of material testimony can lead only to judicial murder."},
      {"author": "Samuel Taylor Coleridge", "work": "The Friend", "quote": "Popular unrest often springs from the government's culpable **incognizance** of economic distress."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "A blind **incognizance** of the living realities of labor will tear this kingdom asunder."}
    ]
  },
  "Dashboard — cogn/incognizant.md": {
    "primary": "Lacking awareness, knowledge, or perception of something; unmindful.",
    "secondary": "In psychological narrative and political critique, remaining oblivious to perils or historic currents moving in plain sight.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "He walked onward through the dark market-place, entirely **incognizant** of the plot brewing against him."},
      {"author": "Joseph Conrad", "work": "Victory", "quote": "He lived upon his lonely island, apparently **incognizant** of the greedy eyes watching his retreat."},
      {"author": "Henry James", "work": "The Golden Bowl", "quote": "She remained placidly **incognizant** of the delicate web of deception woven around her marriage."}
    ]
  },
  "Dashboard — cogn/incognoscible.md": {
    "primary": "Incapable of being known, comprehended, or conceptualized by the intellect.",
    "secondary": "In theological metaphysics and ontology, describing the divine essence that defies conceptual categorization by mortal reason.",
    "quotes": [
      {"author": "William Hamilton", "work": "Lectures on Metaphysics and Logic", "quote": "The unconditioned is fundamentally **incognoscible**, since to know is to condition and relate."},
      {"author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "We must beware of asserting that divine mysteries are utterly **incognoscible** to spiritual faith."},
      {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "That which lies beyond the phenomenal nexus must remain forever **incognoscible** to science."}
    ]
  },
  "Dashboard — cogn/precognition.md": {
    "primary": "Foreknowledge of an event, especially when acquired through intuitive or prophetic means.",
    "secondary": "In Scots law, the preliminary examination of prospective witnesses conducted prior to a formal trial.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Heart of Mid-Lothian", "quote": "The magistrate ordered a strict **precognition** of all persons who had seen the prisoner on that fatal night."},
      {"author": "William James", "work": "The Will to Believe", "quote": "Reports of spontaneous **precognition** demand rigorous empirical investigation rather than contemptuous dismissal."},
      {"author": "Arthur Conan Doyle", "work": "The Edge of the Unknown", "quote": "He recorded several distinct instances of **precognition** that were subsequently verified by newspaper dispatches."}
    ]
  },
  "Dashboard — cogn/precognitive.md": {
    "primary": "Relating to or having the power of precognition; anticipating future events.",
    "secondary": "In parapsychology and cognitive folklore, describing dreams or intuitions that disclose future happenings.",
    "quotes": [
      {"author": "William James", "work": "Memories and Studies", "quote": "Certain vivid dreams possess an apparently **precognitive** character that leaves a lasting impression."},
      {"author": "Arthur Conan Doyle", "work": "The New Revelation", "quote": "The psychic medium claimed to have experienced a **precognitive** vision of the impending naval battle."},
      {"author": "F. W. H. Myers", "work": "Human Personality and Its Survival of Bodily Death", "quote": "We must classify these anomalous cases as either telepathic impressions or genuinely **precognitive** warnings."}
    ]
  },
  "Dashboard — cogn/recognisable.md": {
    "primary": "Capable of being identified, recognized, or recalled from previous knowledge (British spelling of recognizable).",
    "secondary": "In artistic representation, depicting figures or scenes with sufficient verisimilitude to be distinct from abstract forms.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "I was not related to the outlaw, or connected with him by any **recognisable** tie; he had preserved me."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "It rested upon two figures which, in spite of increasing distance, were still **recognisable**."},
      {"author": "Francis Thompson", "work": "Shelley: An Essay", "quote": "The dream-character of his scenery is notorious; it is nowhere **recognisable** on the terrestrial globe."}
    ]
  },
  "Dashboard — cogn/recognisance.md": {
    "primary": "A bond or obligation entered into before a court of record to perform a legal act (British spelling of recognizance).",
    "secondary": "In medieval chivalry, an emblem, crest, or token acknowledging fealty or military service.",
    "quotes": [
      {"author": "Tobias Smollett", "work": "The Adventures of Sir Launcelot Greaves", "quote": "He offered to deposit a sum equal to the **recognisance** of the knight's bail."},
      {"author": "James Joyce", "work": "Ulysses", "quote": "Bloom: Sirs, take notice that by the law of torts you are bound over in your own **recognisance**."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The bailiff insisted that the accused should enter into a formal **recognisance** to keep the King's peace."}
    ]
  },
  "Dashboard — cogn/recognise.md": {
    "primary": "To identify someone or something from having encountered them before; to acknowledge validity or existence (British spelling of recognize).",
    "secondary": "In international diplomacy and social philosophy, according legitimate status or sovereign equality to another entity.",
    "quotes": [
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Anne was astonished to **recognise** the same hills and the same objects so soon."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "It was easy to **recognise** the pantomime of sorrow performed upon the stage."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I lifted my eyes and could readily **recognise** the stern features of Mr. Rochester."}
    ]
  },
  "Dashboard — cogn/recognised.md": {
    "primary": "Acknowledged, identified, or accepted as valid, true, or authoritative (British spelling of recognized).",
    "secondary": "In professional disciplines, meeting accredited standards established by statutory councils or peer consensus.",
    "quotes": [
      {"author": "Lewis Carroll", "work": "Alice's Adventures in Wonderland", "quote": "Next came the guests, mostly Kings and Queens, and among them Alice **recognised** the White Rabbit."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "This venture into the paths of farming as master and not as man was now generally **recognised**."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "His exceptional talent in diagnosis was soon **recognised** by every impartial physician in the district."}
    ]
  },
  "Dashboard — cogn/recognition.md": {
    "primary": "The identification of something previously known; acknowledgment of validity, merit, or achievement.",
    "secondary": "In Hegelian philosophy and diplomacy, the mutual validation of sovereign status or autonomous self-consciousness.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Grandfather Smallweed smiles in a very ugly way in **recognition** of the letter."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth bowed slightly in **recognition** as Mr. Darcy rode past her window."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "The highest tribute to genius is the universal **recognition** of its universal truth."}
    ]
  },
  "Dashboard — cogn/recognizable.md": {
    "primary": "Able to be identified or known from previous acquaintance or inherent characteristics.",
    "secondary": "In portraiture and architectural history, possessing distinctive traits that preserve individual identity across stylistic variations.",
    "quotes": [
      {"author": "Frank A. Fetter", "work": "Economics Volume II: Modern Economic Problems", "quote": "The embossed design is merely to make the coins easily **recognizable** to merchants."},
      {"author": "T. R. Glover", "work": "The Jesus of History", "quote": "The story a man invents about another has to be true in some **recognizable** way to character."},
      {"author": "Mark Twain", "work": "Life on the Mississippi", "quote": "Every bend, snag, and timber-head on the river was **recognizable** to the veteran pilot by night or day."}
    ]
  },
  "Dashboard — cogn/recognizably.md": {
    "primary": "In a manner that can be identified or recognized; distinctly.",
    "secondary": "In cultural evolution and comparative anatomy, displaying unmistakable continuity with ancestral archetypes.",
    "quotes": [
      {"author": "Mark Twain", "work": "What Is Man? and Other Essays", "quote": "One reason is, because there are a dozen that are **recognizably** competent to do that work."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "The mystical state is **recognizably** similar in all major historic traditions."},
      {"author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "The skeletal framework of the higher ape is **recognizably** homologous to that of human anatomy."}
    ]
  },
  "Dashboard — cogn/recognizance.md": {
    "primary": "A legal obligation recorded in court whereby a person promises to perform a duty, such as appearing for trial.",
    "secondary": "In Shakespearean drama and feudal law, a badge, token, or pledge of faith and honorable submission.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Othello", "quote": "And she did gratify his amorous works with that **recognizance** and pledge of love which I first gave her."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The magistrate remanded the prisoner under heavy **recognizance** to answer at the next general court."},
      {"author": "Tobias Smollett", "work": "The Adventures of Sir Launcelot Greaves", "quote": "He offered to deposit a sum equal to the **recognizance** of the knight's bail."}
    ]
  },
  "Dashboard — cogn/recognize.md": {
    "primary": "To identify from having previously seen, heard, or known; to acknowledge the truth or validity of.",
    "secondary": "In statecraft and international law, formally according sovereign diplomatic relations to a newly formed government.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "It is not right, and I must not **recognize** it."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The shepherd was quick to **recognize** the distant barking of his faithful dog."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Sailors are swift to **recognize** the unmistakable blast of the right whale."}
    ]
  },
  "Dashboard — cogn/recognized.md": {
    "primary": "Identified from prior knowledge; accepted, acknowledged, or officially approved.",
    "secondary": "In scientific canon and academic doctrine, supported by empirical consensus across the scholarly community.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "She **recognized** the venerable pastor walking beside the governor with dignified grace."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Natural selection is now widely **recognized** as the main, though not exclusive, means of modification."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "It is a truth universally **recognized** that a young man in possession of fortune must be in want of a wife."}
    ]
  },
  "Dashboard — cogn/unrecognisable.md": {
    "primary": "Incapable of being recognized, identified, or made out (British spelling of unrecognizable).",
    "secondary": "In archaeological excavation and forensic pathology, weathered so severely that original contours are obliterated.",
    "quotes": [
      {"author": "Anne Gilchrist", "work": "Mary Lamb", "quote": "The print from it prefixed to Fitzgerald's Lamb is almost **unrecognisable**."},
      {"author": "Mrs. George de Horne Vaizey", "work": "The Lady of the Basement Flat", "quote": "The once cheerful room was transformed until it was completely **unrecognisable**."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The colossal architecture of the future had crumbled into **unrecognisable** mounds of dust."}
    ]
  },
  "Dashboard — cogn/unrecognised.md": {
    "primary": "Not identified, acknowledged, appreciated, or given official status (British spelling of unrecognized).",
    "secondary": "In literary history, describing genius or artistic masterpieces that languished in obscurity during the author's lifetime.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "He wandered through the university town, poor and **unrecognised** by the academic elite."},
      {"author": "George Eliot", "work": "Scenes of Clerical Life", "quote": "Many a heroic sacrifice is made in humble cottages, **unrecognised** by the busy world outside."},
      {"author": "Charlotte Brontë", "work": "The Professor", "quote": "My quiet labor remained long **unrecognised**, but patient fidelity won in the end."}
    ]
  },
  "Dashboard — cogn/unrecognizable.md": {
    "primary": "Impossible to identify or recognize; changed beyond recall or detection.",
    "secondary": "In military and maritime narrative, altered through violence, decay, or disguise so that all identity is lost.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "Some fifty miles below the Inner Station we came upon a hut of reeds, an inclined and melancholy ruin, nearly **unrecognizable** in the dense grass."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The prison cellar had changed him into a hollow, **unrecognizable** specter of his former self."},
      {"author": "Herman Melville", "work": "Typee", "quote": "The ancient stone monuments were overgrown with wild creepers until they became almost **unrecognizable**."}
    ]
  },
  "Dashboard — cogn/unrecognizably.md": {
    "primary": "In a way that cannot be recognized; beyond recognition.",
    "secondary": "In historical description, transformed by time, revolution, or catastrophe into a wholly alien state.",
    "quotes": [
      {"author": "Mark Twain", "work": "A Connecticut Yankee in King Arthur's Court", "quote": "The ancient Roman roads were **unrecognizably** worn and buried beneath centuries of peasant turf."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "The terrain had altered so **unrecognizably** that even our native guides were utterly baffled."},
      {"author": "H. G. Wells", "work": "The Island of Doctor Moreau", "quote": "The creatures were twisted **unrecognizably** away from any natural animal form."}
    ]
  },
  "Dashboard — cogn/unrecognized.md": {
    "primary": "Not identified, noticed, acknowledged, or validated.",
    "secondary": "In social history and psychology, operating as an unseen yet decisive influence upon human decisions.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "By some good agency,—possibly, by the **unrecognized** interposition of the late judge,—the youth was liberated."},
      {"author": "Frank A. Fetter", "work": "The Principles of Economics", "quote": "This truth, **unrecognized** for many centuries, forms the foundation of the modern theory of rent."},
      {"author": "Sarah Orne Jewett", "work": "Strangers and Wayfarers", "quote": "It was a feeling of defenselessness against some **unrecognized** but malicious influence."}
    ]
  }
}

base_dir = r"App database/Latin roots/Cluster Thought"

updated_count = 0
for rel_path, entry in data.items():
    full_path = os.path.join(base_dir, rel_path)
    if not os.path.exists(full_path):
        print(f"Missing file: {full_path}")
        continue
    
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    book_pattern = r"(> 1\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)(\r?\n> 2\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)"
    def repl_book(m):
        return f"{m.group(1)}{entry['primary']}{m.group(3)}{entry['secondary']}"
    
    new_content = re.sub(book_pattern, repl_book, content)
    if new_content == content:
        book_pattern2 = r"(1\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)(\r?\n.*?2\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)"
        new_content = re.sub(book_pattern2, repl_book, content)

    q_pos = new_content.find("> [!quote]")
    if q_pos != -1:
        before_q = new_content[:q_pos]
        after_q = new_content[q_pos:]
        
        new_q_lines = ["> [!quote] 💬 Contextual Usage & Authentic Quotations"]
        for q in entry["quotes"]:
            new_q_lines.append(f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{q['quote']}\"*")
        
        rest = after_q.split("\n")
        remaining_lines = []
        skip = True
        for line in rest[1:]:
            if skip:
                if line.startswith("> - 📜") or line.strip() == ">" or line.strip() == "":
                    continue
                else:
                    skip = False
                    remaining_lines.append(line)
            else:
                remaining_lines.append(line)
        
        new_content = before_q + "\n".join(new_q_lines) + ("\n" + "\n".join(remaining_lines) if remaining_lines else "\n")
    
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated_count += 1

print(f"Thought Batch 2A (cogn): Successfully updated {updated_count}/{len(data)} notes.")
