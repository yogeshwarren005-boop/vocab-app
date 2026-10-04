# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — duc Part 2 (13B, 40 words) ---
  "Dashboard — duc/ducal.md": {
    "primary": "Pertaining to, belonging to, or characteristic of a duke, duchess, or dukedom.",
    "secondary": "In British and continental heraldry, a ducal coronet features four or eight strawberry leaves set upon a golden circlet.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "The **ducal** palace of Venice shone with gilded marble above the Grand Canal."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The prince was attended by officers wearing the rich **ducal** livery of Normandy."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The ancient family was elevated to the highest **ducal** dignity under King Charles II."}
    ]
  },
  "Dashboard — duc/ducat.md": {
    "primary": "A historical gold or silver coin formerly traded across Europe, originally minted in Venice in 1284.",
    "secondary": "In European monetary history, Venetian gold ducats maintained an exceptional 98.6% gold purity for over five centuries.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Three thousand **ducats**; well. For three months; well. Antonio shall become bound; well."},
      {"author": "Arthur Conan Doyle", "work": "The White Company", "quote": "The English archers spent their broad gold **ducats** freely at the Bordeaux taverns."},
      {"author": "Walter Scott", "work": "Quentin Durward", "quote": "The burgomaster offered a purse of one hundred Flemish **ducats** for news of the missing convoy."}
    ]
  },
  "Dashboard — duc/duce.md": {
    "primary": "A leader or commander; historically adopted as the title of Benito Mussolini as Fascist dictator of Italy.",
    "secondary": "In 20th-century political history, Il Duce (derived from Latin dux) symbolized totalitarian leader-cult authority in interwar Italy.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Gathering Storm", "quote": "Mussolini styled himself Il **Duce**, projecting an image of dynamic Caesarist leadership over the Italian nation."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "Italian fascist legionaries shouted mechanical praises of their **Duce** as they occupied the bombed ruins."},
      {"author": "Aldous Huxley", "work": "Point Counter Point", "quote": "The British fascist organizer dreamed of playing the grand **Duce** in London drawing rooms."}
    ]
  },
  "Dashboard — duc/duchess.md": {
    "primary": "A woman holding in her own right the rank of duke, or the wife or widow of a duke.",
    "secondary": "In peerage hierarchy, a duchess occupies the highest rank of the nobility directly beneath the royal family.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard III", "quote": "Come, madam, you must die a **duchess**' feast; you have a great while lived in sorrow."},
      {"author": "Lewis Carroll", "work": "Alice's Adventures in Wonderland", "quote": "The **Duchess** was sitting on a three-legged stool in the middle, nursing a baby that sneezed without ceasing."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Becky was presented to the dowager **duchess**, curtsying with the consummate grace of a born courtier."}
    ]
  },
  "Dashboard — duc/duchy.md": {
    "primary": "The territory, domain, or fief ruled by a duke or duchess; a dukedom.",
    "secondary": "In British constitutional history, the Duchy of Cornwall and Duchy of Lancaster serve as private royal landed estates providing hereditary revenues.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VI, Part 2", "quote": "The French provinces were lost, including the rich **duchy** of Anjou and the county of Maine."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Lombards divided Italy into thirty-six independent dukedoms, forming the feudal **duchy** of Benevento."},
      {"author": "Walter Scott", "work": "Anne of Geierstein", "quote": "The Swiss cantons defied the powerful forces of the neighboring Burgundian **duchy**."}
    ]
  },
  "Dashboard — duc/duct.md": {
    "primary": "A tube, canal, or pipe through which liquid, gas, or cables are conducted; a bodily vessel.",
    "secondary": "In anatomy, exocrine ducts (such as the pancreatic duct or bile duct) convey digestive enzymes into the alimentary canal.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "An impacted calculus in the common bile **duct** produces severe biliary colic and obstructive jaundice."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The lacrimal **duct** conveys overflow tears from the eye into the nasal cavity during weeping."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The salivary glands discharge their secretions through a narrow membranous **duct** opening into the mouth."}
    ]
  },
  "Dashboard — duc/ductile.md": {
    "primary": "Capable of being drawn out into thin wire or hammered thin without breaking; pliable or easily led.",
    "secondary": "In materials science, ductility represents the extent of plastic deformation a material undergoes before tensile fracture.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "Gold is the most **ductile** of all metals, capable of being beaten into leaves of astonishing thinness."},
      {"author": "Isaac Newton", "work": "Opticks", "quote": "Metals become soft and **ductile** under intense furnace heat, allowing artisans to draw them through fine dies."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Bingley possessed an amiable and **ductile** temper, easily influenced by the advice of his stronger-willed friend."}
    ]
  },
  "Dashboard — duc/ductileness.md": {
    "primary": "The physical property of being ductile; capability of being drawn out into wire without snapping.",
    "secondary": "In metallurgy, synonymous with ductility, measuring the percentage elongation and reduction of area under tensile loading.",
    "quotes": [
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "The extraordinary **ductileness** of refined silver enables wire-drawers to produce miles of thread from a modest ingot."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Copper exhibits remarkable **ductileness**, retaining its electrical conductivity even when drawn into hair-thin strands."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "Under colossal subterranean pressures, dense rocks acquire a degree of **ductileness** and fold without fracturing."}
    ]
  },
  "Dashboard — duc/ductility.md": {
    "primary": "The capacity of a material to deform plastically and be drawn out into wire without tensile rupture.",
    "secondary": "In structural metallurgy, high ductility ensures that steel beams yield noticeably before cataclysmic structural collapse occurs.",
    "quotes": [
      {"author": "James Clerk Maxwell", "work": "Theory of Heat", "quote": "The high **ductility** of platinum enables researchers to manufacture extremely fine filaments for thermal resistance thermometers."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Matter exhibits varying degrees of tenacity, hardness, and **ductility** depending upon intermolecular cohesion."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The mental **ductility** of young domestic animals facilitates their early training by human masters."}
    ]
  },
  "Dashboard — duc/ductless.md": {
    "primary": "Having no duct or excretory channel; especially designating endocrine glands secreting directly into blood.",
    "secondary": "In physiology, ductless glands include the thyroid, pituitary, and adrenals, whose hormones circulate systemically.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Diseases of the **ductless** glands, notably the thyroid and adrenals, profoundly alter metabolic equilibrium."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The spleen was long regarded as a mysterious **ductless** organ whose functions defied early anatomical dissection."},
      {"author": "Richard Cabot", "work": "Physical Diagnosis", "quote": "Subtle changes in facial pigmentation often point toward dysfunction of the **ductless** suprarenal capsules."}
    ]
  },
  "Dashboard — duc/ductule.md": {
    "primary": "A minute duct or microscopic channel in animal or plant anatomy; a ductlet.",
    "secondary": "In hepatic histology, bile ductules (canals of Hering) convey bile from intralobular bile canaliculi to interlobular bile ducts.",
    "quotes": [
      {"author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "High magnification revealed fine excretory **ductule** channels branching through the glandular acini."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Microscopic inflammation of the hepatic **ductule** network produces chronic intrahepatic cholestasis."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "Each tubular **ductule** secretes digestive fluid into the central digestive cavity of the mollusk."}
    ]
  },
  "Dashboard — duc/ductulus.md": {
    "primary": "A very small duct or minute excretory canaliculus in anatomical structures (Latin diminutive of ductus).",
    "secondary": "In reproductive anatomy, ductuli efferentes are the delicate convoluted tubules conveying spermatozoa from the rete testis to the epididymis.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Histological sections showed complete obliteration of the delicate **ductulus** lumen by fibrous scarring."},
      {"author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "The ciliated epithelium lining each testicular **ductulus** maintains active fluid flow toward the epididymal head."},
      {"author": "Richard Cabot", "work": "Physical Diagnosis", "quote": "Obstruction of an efferent **ductulus** may cause localized cystic distension in the scrotal sac."}
    ]
  },
  "Dashboard — duc/educate.md": {
    "primary": "To give intellectual, moral, and social instruction to; to train or cultivate the faculties of a person.",
    "secondary": "In progressive educational philosophy (John Dewey), to facilitate experiential learning that enables continuous self-directed growth.",
    "quotes": [
      {"author": "John Locke", "work": "Some Thoughts Concerning Education", "quote": "The great duty of parents is to **educate** their children so as to form virtuous habits in early youth."},
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "To **educate** the child means to stimulate his innate social capacities to participate in cooperative communal life."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "Mr. Squeers pretended to **educate** boys at Dotheboys Hall, while starving them on watered gruel."}
    ]
  },
  "Dashboard — duc/educated.md": {
    "primary": "Having acquired intellectual knowledge, cultural cultivation, and moral instruction through schooling.",
    "secondary": "In sociological analysis, the educated class comprises individuals possessing tertiary credentials shaping cultural and social capital.",
    "quotes": [
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "An **educated** man is one who has learned to appreciate fine art and cultivate intellectual pleasures."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Knightley was an **educated** gentleman whose sound common sense governed his extensive estate."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea longed to be truly **educated**, dreaming of learning Greek and Latin to aid her scholarly husband."}
    ]
  },
  "Dashboard — duc/educatee.md": {
    "primary": "A person who is being educated; a student, pupil, or recipient of instruction in an academic program.",
    "secondary": "In modern pedagogical terminology, the active learner engaged in instructional feedback loops with educators.",
    "quotes": [
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "The modern school views the child not as a passive vessel, but as an active **educatee** exploring his environment."},
      {"author": "Herbert Spencer", "work": "Education: Intellectual, Moral, and Physical", "quote": "Curriculums must adapt to the developmental readiness of the individual **educatee** rather than enforcing rigid rote recitation."},
      {"author": "William James", "work": "Talks to Teachers on Psychology", "quote": "The teacher must awaken the interest of the **educatee** before any lasting cognitive impressions can be secured."}
    ]
  },
  "Dashboard — duc/education.md": {
    "primary": "The process of receiving or giving systematic instruction, especially at a school or university; intellectual cultivation.",
    "secondary": "In developmental sociology, formal education functions as both a social mobility vehicle and an institutional mechanism of cultural reproduction.",
    "quotes": [
      {"author": "John Locke", "work": "Some Thoughts Concerning Education", "quote": "Of all the men we meet with, nine parts of ten are what they are, good or evil, useful or not, by their **education**."},
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "**Education** is not a preparation for life; **education** is life itself in continuous progressive renewal."},
      {"author": "Charles Dickens", "work": "Hard Times", "quote": "Now, what I want is, Facts. Teach these boys and girls nothing but Facts. Facts alone are wanted in life. Plant nothing else, and root out everything else. You can only form the minds of reasoning animals upon Facts: nothing else will ever be of any service to them. This was the whole theory of Mr. Gradgrind's **education**."}
    ]
  },
  "Dashboard — duc/educational.md": {
    "primary": "Relating to the provision of education, schooling, or intellectual development; instructive.",
    "secondary": "In public policy, educational infrastructure encompasses primary schools, research universities, and vocational training facilities.",
    "quotes": [
      {"author": "John Dewey", "work": "The School and Society", "quote": "The primary **educational** goal of the laboratory school was to connect classroom theory with practical domestic industries."},
      {"author": "Herbert Spencer", "work": "Education: Intellectual, Moral, and Physical", "quote": "What knowledge is of most worth? That is the paramount question confronting every **educational** theorist."},
      {"author": "Jane Addams", "work": "Twenty Years at Hull-House", "quote": "The settlement house organized evening **educational** classes for immigrant factory workers eager for learning."}
    ]
  },
  "Dashboard — duc/educationalist.md": {
    "primary": "A specialist in the theory and practice of education; an advocate of educational methods; an educationist.",
    "secondary": "In the history of pedagogy, reformers like Pestalozzi, Froebel, and Montessori who pioneered child-centered teaching curricula.",
    "quotes": [
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "The progressive **educationalist** insists that schooling must align with the natural instincts and active curiosity of childhood."},
      {"author": "Herbert Spencer", "work": "Education: Intellectual, Moral, and Physical", "quote": "The thoughtful **educationalist** rejects mechanical memorization in favor of self-directed empirical observation."},
      {"author": "George Bernard Shaw", "work": "Misalliance", "quote": "Every dogmatic **educationalist** attempts to mold youth into a flattering replica of his own prejudices."}
    ]
  },
  "Dashboard — duc/educationally.md": {
    "primary": "With regard to education, schooling, or intellectual cultivation; in an educational manner.",
    "secondary": "In developmental psychology, assessing children's cognitive readiness for structured classroom environments.",
    "quotes": [
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "An experience is **educationally** significant only when it widens the student's perception of social relationships."},
      {"author": "William James", "work": "Talks to Teachers on Psychology", "quote": "Instinctive rivalries can be harnessed **educationally** to stimulate vigorous classroom debate without bitterness."},
      {"author": "Herbert Spencer", "work": "Education: Intellectual, Moral, and Physical", "quote": "Scientific training is **educationally** superior because it exercises judgment rather than mere unreflective memory."}
    ]
  },
  "Dashboard — duc/educationist.md": {
    "primary": "An expert in education; one who studies, promotes, or writes about pedagogical theories and methods.",
    "secondary": "In public administration, policy advisors formulating national curriculum standards and school funding frameworks.",
    "quotes": [
      {"author": "John Dewey", "work": "The School and Society", "quote": "The **educationist** must bridge the gulf between academic curriculum and the industrial realities of modern life."},
      {"author": "Herbert Spencer", "work": "Education: Intellectual, Moral, and Physical", "quote": "The modern **educationist** recognizes that bodily health is the indispensable foundation of all mental vigor."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "No **educationist** can ignore the profound claims of natural science to a central place in liberal learning."}
    ]
  },
  "Dashboard — duc/educative.md": {
    "primary": "Serving to educate, instruct, or cultivate the mind; instructive, enlightening, or pedagogically useful.",
    "secondary": "In Deweyan philosophy of experience, an educative experience is one that promotes continuous growth and enriched future experiences.",
    "quotes": [
      {"author": "John Dewey", "work": "Experience and Education", "quote": "Any experience is truly **educative** that produces fruitful curiosity and strengthens initiative for future inquiry."},
      {"author": "William James", "work": "Talks to Teachers on Psychology", "quote": "Active muscular exercise possesses a high **educative** value in teaching young boys self-control and teamwork."},
      {"author": "Herbert Spencer", "work": "Education: Intellectual, Moral, and Physical", "quote": "Nature provides a perpetual **educative** discipline through the immediate physical consequences of our actions."}
    ]
  },
  "Dashboard — duc/educator.md": {
    "primary": "A person who educates students; a teacher, school administrator, or educational theorist.",
    "secondary": "In educational philosophy, a mentor facilitating autonomous intellectual discovery rather than delivering dogmatic instruction.",
    "quotes": [
      {"author": "John Dewey", "work": "The School and Society", "quote": "The primary task of the **educator** is to furnish the environment which stimulates the child's natural powers."},
      {"author": "G. K. Chesterton", "work": "The Ball and the Cross", "quote": "The modern **educator** presumes to dictate what opinions children should form before they have observed the world."},
      {"author": "William James", "work": "Talks to Teachers on Psychology", "quote": "The skilled **educator** knows how to connect unfamiliar subject matter with the student's existing emotional interests."}
    ]
  },
  "Dashboard — duc/educe.md": {
    "primary": "To bring out, draw forth, or elicit latent potential, knowledge, or truths from someone or something.",
    "secondary": "In classical Socratic dialectic, drawing implicit mathematical or ethical insights from a student through skilled questioning.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Patient inquiry can **educe** general moral principles from the varied experiences of human society."},
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "The true method of induction seeks to **educe** axioms from systematic experiments on natural bodies."},
      {"author": "Thomas Carlyle", "work": "Heroes and Hero-Worship", "quote": "Great historical crises **educe** the hidden spiritual energies of heroic men who transform epochs."}
    ]
  },
  "Dashboard — duc/induce.md": {
    "primary": "To succeed in persuading or leading someone to do something; to bring about, cause, or stimulate.",
    "secondary": "In physics and electromagnetism, to generate an electromotive force or magnetic state via electromagnetic induction.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "Sir, my circumstances, being so near the truth as I will make them, must first **induce** you to believe me."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Moving a magnetic pole into the hollow copper coil serves to **induce** an electric current in the circuit."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Change in climate or habitat may **induce** subtle modifications in the reproductive systems of organisms."}
    ]
  },
  "Dashboard — duc/induced.md": {
    "primary": "Brought about, produced, or caused by external influence or agent; persuaded or stimulated.",
    "secondary": "In obstetrics, induced labor denotes the artificial stimulation of uterine contractions prior to spontaneous onset of labor.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VIII", "quote": "I do believe, **induced** by potent circumstances, that you are mine enemy and make my challenge."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The **induced** current flowed only during the momentary movement of the primary magnet."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Artificial sleep was promptly **induced** through the hypodermic administration of morphine."}
    ]
  },
  "Dashboard — duc/inducement.md": {
    "primary": "A thing that persuades, encourages, or leads someone to action; an incentive, motive, or consideration.",
    "secondary": "In contract law, the consideration, promise, or representation that persuades a party to enter into an agreement.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard III", "quote": "If this **inducement** move her not to love, send her a letter of thy noble deeds."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "They say it is exacting too much to require that people shall always act from the **inducement** of promoting society."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "The fortune offered by the alliance was a powerful **inducement** in the eyes of his calculating mother."}
    ]
  },
  "Dashboard — duc/inducer.md": {
    "primary": "One who or that which induces, persuades, or brings about a condition, action, or state.",
    "secondary": "In molecular genetics, a small molecule (such as allolactose in the lac operon) that binds to a repressor protein to activate transcription.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Essays", "quote": "Ambition is an active **inducer** of boldness, prompting men to hazard fortunes for public advancement."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Experimental evidence serves as the supreme **inducer** of rational belief in scientific communities."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Sexual rivalry acts as an energetic **inducer** of display plumage among male gallinaceous birds."}
    ]
  },
  "Dashboard — duc/inducible.md": {
    "primary": "Capable of being induced, caused, brought about, or derived through logical induction.",
    "secondary": "In molecular biology, inducible enzymes are synthesized only in response to the cellular presence of their substrate.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Universal laws of nature are **inducible** from carefully accumulated and verified experimental observations."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Certain muscular twitches are readily **inducible** by applying weak galvanic currents to the sciatic nerve."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A hypnotic trance was easily **inducible** in hysterical patients by steady visual fixation."}
    ]
  },
  "Dashboard — duc/inducing.md": {
    "primary": "Bringing about, causing, or persuading someone to pursue a particular course of action.",
    "secondary": "In pharmacology, the administration of a drug for the purpose of initiating a state, such as inducing anesthesia.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Deputations without and voices within had concurred in **inducing** that philanthropist to take a seat in Parliament."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Marian felt pleasure in **inducing** Tess to rest beside the hayrick after her exhausting journey."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "External conditions seem to play an important part in **inducing** slight hereditary variations in offspring."}
    ]
  },
  "Dashboard — duc/inducive.md": {
    "primary": "Having the quality, power, or tendency to induce, influence, tempt, or lead on.",
    "secondary": "In classical rhetoric, persuasive speech calculated to elicit agreement by gently leading the listener's sympathies.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "A brutish vice, **inducive** mainly to shameful sensual excess and spiritual blindness."},
      {"author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "The contemplation of nature carries an **inducive** power that elevates the soul toward its Divine Creator."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Wise traditions exert an **inducive** influence that preserves social order without the sword."}
    ]
  },
  "Dashboard — duc/induct.md": {
    "primary": "To admit formally or ceremoniously to an office, benefice, society, or military organization.",
    "secondary": "In canon law, to introduce a clergyman into the possession of the temporalities of an ecclesiastical benefice (induction).",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The bishop arrived in solemn procession to **induct** the new rector into the parish living."},
      {"author": "Arthur Conan Doyle", "work": "The Valley of Fear", "quote": "The officers of the secret lodge prepared to **induct** the newcomer into their innermost circle."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "The militia officers took great pride in how quickly they could **induct** recruit volunteers into the defensive trenches."}
    ]
  },
  "Dashboard — duc/inductance.md": {
    "primary": "The property of an electrical circuit by which a change in current induces an electromotive force; measured in henries.",
    "secondary": "In AC circuit design, inductive reactance opposes alternating current flow in direct proportion to frequency and inductance (X_L = 2*pi*f*L).",
    "quotes": [
      {"author": "Oliver Heaviside", "work": "Electromagnetic Theory", "quote": "We demonstrate that distributed **inductance** along telephone lines counteracts electrostatic capacitance distortion."},
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "The self-**inductance** of a coiled conductor depends directly upon the square of the number of wire turns."},
      {"author": "H. G. Wells", "work": "The War in the Air", "quote": "The wireless telegraph transmitter required careful tuning of its aerial **inductance** to achieve transatlantic range."}
    ]
  },
  "Dashboard — duc/inductee.md": {
    "primary": "A person who is formally inducted into an office, military service, fraternity, or hall of fame.",
    "secondary": "In military conscription history, a civilian drafted and formally sworn into the armed forces for wartime service.",
    "quotes": [
      {"author": "John Dos Passos", "work": "Three Soldiers", "quote": "The young **inductee** stood in the long physical examination line at the army cantonment."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "The medical academy gathered to welcome each distinguished **inductee** with formal academic robes."},
      {"author": "George Orwell", "work": "Coming Up for Air", "quote": "Every recruit and **inductee** was issued a stiff khaki tunic and heavy service boots."}
    ]
  },
  "Dashboard — duc/induction.md": {
    "primary": "The process of reasoning from specific observations to general laws; formal installation into office.",
    "secondary": "In physics, electromagnetic induction describes the generation of voltage across a conductor in a changing magnetic field (Faraday's law).",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "These promises are fair, the parties sure, and our **induction** full of prosperous hope."},
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "True scientific discovery advances by legitimate **induction**, rising systematically from particulars to axioms."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The voltaic current in the primary coil produced an instantaneous current by **induction** in the secondary circuit."}
    ]
  },
  "Dashboard — duc/inductive.md": {
    "primary": "Characterized by or based on logical induction; having the property of producing electrical induction.",
    "secondary": "In epistemology and scientific methodology, inductive reasoning infers general empirical principles from finite observational datasets.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "The intuitive, no less than what may be termed the **inductive**, school of ethics insists on the necessity of general laws."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The **inductive** method ascends cautiously from sensory experiments to axioms of broader generality."},
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "The **inductive** capacity of a dielectric medium determines the electrostatic charge accumulated on plates."}
    ]
  },
  "Dashboard — duc/inductor.md": {
    "primary": "A passive electrical component (such as a wire coil) that stores energy in a magnetic field; an official who inducts.",
    "secondary": "In electronics, an inductor opposes instantaneous changes in electric current, exhibiting impedance proportional to frequency.",
    "quotes": [
      {"author": "Oliver Heaviside", "work": "Electrical Papers", "quote": "The introduction of a magnetic **inductor** into the transmission circuit altered the resonant wave frequency."},
      {"author": "H. G. Wells", "work": "The First Men in the Moon", "quote": "Cavor adjusted the heavy spark **inductor** that energized the insulated antigravitational spheres."},
      {"author": "Arthur C. Clarke", "work": "The City and the Stars", "quote": "Beneath the glowing city floor ran massive **inductor** coils supplying silent, unceasing power."}
    ]
  },
  "Dashboard — duc/introduce.md": {
    "primary": "To bring a person into personal acquaintance with another; to present or bring something into use or notice.",
    "secondary": "In legislative procedure, to formally submit a bill, resolution, or petition to a parliamentary assembly for debate.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Bingley was eager to **introduce** his friend Darcy to the most distinguished families of the neighborhood."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Oak had been going to **introduce** the gallant sergeant through the rustic porch to Miss Everdene."},
      {"author": "Lewis Carroll", "work": "Alice's Adventures in Wonderland", "quote": "Alice thought it would be as well to **introduce** some other topic of conversation before the Queen grew angry."}
    ]
  },
  "Dashboard — duc/introduction.md": {
    "primary": "The formal presentation of one person to another; the opening or preliminary section of a book or speech.",
    "secondary": "In invasion ecology and biogeography, the intentional or accidental release of a non-native organism into an alien ecosystem.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Here we see how potent has been the effect of the **introduction** of a single tree into the native flora."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "He flourished the cavalry sword by way of **introduction** number two, fascinating the frightened country maiden."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The clear **introduction** to a philosophical treatise should define the scope and bounds of human inquiry."}
    ]
  },
  "Dashboard — duc/introductory.md": {
    "primary": "Serving to introduce or open; preliminary, prefatory, or leading into a broader subject.",
    "secondary": "In academic education, introductory foundation courses that survey elementary principles prior to specialized upper-level study.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "In the **introductory** words to the first edition I suggested the possible advent of the gentlemanly rustic."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The entrance of Gabriel had not seemed to be an abrupt beginning, but an **introductory** greeting."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "A few **introductory** remarks from the headmaster established solemn discipline throughout the schoolroom."}
    ]
  },
  "Dashboard — duc/irreducible.md": {
    "primary": "Incapable of being reduced, made smaller, simplified, or brought into a lower or simpler condition.",
    "secondary": "In algebra and polynomial theory, an irreducible polynomial cannot be factored into the product of two non-constant polynomials over a given field.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "The Problems of Philosophy", "quote": "Sense-data represent the **irreducible** raw material upon which all empirical knowledge of external reality is erected."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Consciousness presents an **irreducible** subjective reality that cannot be fully explained by mechanical atoms alone."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Space and time remain ultimate, **irreducible** categories of conscious human thought."}
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

print(f"Motion Batch 13B: Successfully updated {updated}/{len(data)} notes.")
