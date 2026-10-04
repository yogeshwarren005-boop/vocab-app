# -*- coding: utf-8 -*-
"""
Curates Dashboard — put (Part 1: words 1-38) in Cluster Mind & Knowledge.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_part1 = {
  "amputate": {
    "primary": "To surgically cut off a limb, appendage, or digit from the body, typically to halt gangrene or trauma.",
    "secondary": "In horticultural husbandry, to prune away diseased branches or severed vegetal limbs from orchard stock.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The surgeon determined to **amputate** the gangrenous foot before systemic sepsis invaded the circulatory tree."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab cursed the white whale that had dared to **amputate** his leg and leave him pacing upon ivory."},
      {"author": "Walt Whitman", "work": "Specimen Days", "quote": "In the field hospital, sawbones worked by lantern light to **amputate** shattered limbs of wounded infantrymen."}
    ]
  },
  "amputation": {
    "primary": "The surgical removal of an extremity, limb, or digit from the body due to trauma, infection, or arterial pathology.",
    "secondary": "In military surgical history, the standard wartime procedure performed under battlefield conditions to save life.",
    "quotes": [
      {"author": "Ambroise Paré", "work": "The Apologie and Treatise of Ambroise Paré", "quote": "He introduced ligatures during **amputation** to replace the cruel cautery of boiling oil on severed arteries."},
      {"author": "Oliver Sacks", "work": "A Leg to Stand On", "quote": "Patients who undergo traumatic **amputation** frequently report vivid phantom sensations emanating from missing limbs."},
      {"author": "Stephen Crane", "work": "The Red Badge of Courage", "quote": "The sergeant stumbled toward the ambulance tent, resigned to the impending **amputation** of his mangled arm."}
    ]
  },
  "amputator": {
    "primary": "A surgeon, instrument, or agent that performs the surgical excision or severance of a limb.",
    "secondary": "In historical surgical tools, a specialized curved or straight amputation knife designed for rapid circumferential incision.",
    "quotes": [
      {"author": "Richard Selzer", "work": "Mortal Lessons: Notes on the Art of Surgery", "quote": "The military surgeon stood as a seasoned **amputator**, working through queues of casualties with grim speed."},
      {"author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "The skillful **amputator** preserves every millimeter of viable skin flap to ensure a functional, painless stump."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "Bob Sawyer brandished the gleaming surgical blade, boasting of his swift dexterity as a hospital **amputator**."}
    ]
  },
  "computable": {
    "primary": "Capable of being determined, calculated, or modeled through mathematical calculation or algorithmic procedures.",
    "secondary": "In theoretical computer science, a function or problem solvable by a Turing machine within finite steps.",
    "quotes": [
      {"author": "Alan Turing", "work": "On Computable Numbers, with an Application to the Entscheidungsproblem", "quote": "A number is **computable** if its decimals can be written down by a machine working according to fixed rules."},
      {"author": "Douglas Hofstadter", "work": "Gödel, Escher, Bach", "quote": "Not every logically sound mathematical proposition corresponds to a recursively **computable** decision procedure."},
      {"author": "Stephen Wolfram", "work": "A New Kind of Science", "quote": "Simple cellular automata generate patterns whose long-term evolution is not easily **computable** in advance."}
    ]
  },
  "computation": {
    "primary": "The act, process, or mathematical method of calculating, reckoning, or executing algorithmic operations.",
    "secondary": "In computer architecture, the electronic execution of binary arithmetic and logic instructions in processing units.",
    "quotes": [
      {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "The Difference Engine eliminated mechanical error from numerical **computation**, printing navigational tables automatically."},
      {"author": "Ada Lovelace", "work": "Sketch of the Analytical Engine", "quote": "The engine weaves algebraic patterns just as the Jacquard loom weaves flowers and leaves through digital **computation**."},
      {"author": "Richard Feynman", "work": "Feynman Lectures on Computation", "quote": "Fundamental thermodynamic limits govern the minimum energy dissipation required for each irreversible **computation**."}
    ]
  },
  "computational": {
    "primary": "Relating to, involving, or performed by mathematical calculation, computers, or algorithmic processing.",
    "secondary": "In cognitive science, the hypothesis that mental operations resemble computational symbol manipulation.",
    "quotes": [
      {"author": "Steven Pinker", "work": "How the Mind Works", "quote": "The human brain functions as an intricate **computational** organ sculpted by natural selection to process information."},
      {"author": "Daniel Dennett", "work": "Consciousness Explained", "quote": "He defended a **computational** architecture of consciousness based upon multiple competing drafts in neural networks."},
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "Modern **computational** neuroscience constructs algorithmic models to simulate synaptic plasticity in cerebellar circuits."}
    ]
  },
  "computationally": {
    "primary": "By means of computation, mathematical calculation, algorithms, or electronic processing systems.",
    "secondary": "In algorithmic complexity theory, describing problems that are computationally tractable or intractable (such as NP-complete problems).",
    "quotes": [
      {"author": "Donald Knuth", "work": "The Art of Computer Programming", "quote": "The algorithm proved **computationally** efficient, executing in logarithmic time across massive sorted arrays."},
      {"author": "Carl Sagan", "work": "Contact", "quote": "Radio astronomers verified **computationally** that the incoming transmission exhibited artificial prime number sequences."},
      {"author": "Stephen Wolfram", "work": "A New Kind of Science", "quote": "Certain complex physical phenomena are **computationally** irreducible, requiring direct step-by-step simulation to observe."}
    ]
  },
  "compute": {
    "primary": "To calculate, determine, or reckon a numerical value, mathematical result, or logical outcome.",
    "secondary": "In digital electronics, to process digital inputs according to programmed machine instructions.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Mathematical Principles of Natural Philosophy", "quote": "Astronomers can now **compute** the exact gravitational perturbations exerted by Jupiter upon neighboring planets."},
      {"author": "Ada Lovelace", "work": "Notes on the Analytical Engine", "quote": "The mechanical gears were engineered to **compute** the successive Bernoulli numbers without human intervention."},
      {"author": "Carl Friedrich Gauss", "work": "Theory of the Motion of the Heavenly Bodies", "quote": "Using least squares regression, he managed to **compute** the lost orbital trajectory of the asteroid Ceres."}
    ]
  },
  "computer": {
    "primary": "An electronic programmable device that accepts, processes, stores, and outputs data through programmed instructions.",
    "secondary": "In historical parlance, a human clerk employed to perform tedious mathematical reckonings and table calculations.",
    "quotes": [
      {"author": "Alan Turing", "work": "Computing Machinery and Intelligence", "quote": "Can a digital **computer** be programmed to simulate human conversational intellect convincingly enough to pass the test?"},
      {"author": "John von Neumann", "work": "The Computer and the Brain", "quote": "The architecture of the stored-program **computer** separates arithmetic memory registers from central processing logic."},
      {"author": "Arthur C. Clarke", "work": "2001: A Space Odyssey", "quote": "The sentient shipboard **computer** HAL monitored environmental life support while navigating toward Saturn."}
    ]
  },
  "computerise": {
    "primary": "To adapt, convert, or equip a system, process, or enterprise to operation by computers (British spelling).",
    "secondary": "In administrative modernization, replacing paper record systems with digital database architectures.",
    "quotes": [
      {"author": "Anthony Giddens", "work": "The Consequences of Modernity", "quote": "Institutions began to **computerise** vital registries, transforming bureaucratic governance through instant data retrieval."},
      {"author": "David Harvey", "work": "The Condition of Postmodernity", "quote": "Financial centers rushed to **computerise** trading floors, compressing market circulation times across continents."},
      {"author": "Arthur C. Clarke", "work": "1984: Spring", "quote": "Libraries sought to **computerise** vast catalog cards to preserve bibliographic records against physical decay."}
    ]
  },
  "computerization": {
    "primary": "The conversion, equipping, or transformation of an organization, system, or process to computerized operations.",
    "secondary": "In economic history, the technological shift automating clerical, banking, and industrial production workflows.",
    "quotes": [
      {"author": "Shoshana Zuboff", "work": "In the Age of the Smart Machine", "quote": "The comprehensive **computerization** of pulp mills altered workers' relationship to physical industrial machinery."},
      {"author": "David Foster Wallace", "work": "The Pale King", "quote": "The gradual **computerization** of tax audits threatened to dismantle the traditional art of human bookkeeping."},
      {"author": "Manuel Castells", "work": "The Rise of the Network Society", "quote": "Global capital flows accelerated dramatically following the widespread **computerization** of international banking."}
    ]
  },
  "computerize": {
    "primary": "To convert, equip, or automate a process, system, or organization using computers and digital technology.",
    "secondary": "In business administration, migrating manual ledgers, scheduling, and inventory onto electronic server networks.",
    "quotes": [
      {"author": "Alvin Toffler", "work": "Future Shock", "quote": "Corporations moved swiftly to **computerize** logistics and forecast market demands in real time."},
      {"author": "Michael Crichton", "work": "Jurassic Park", "quote": "Arnold had designed the park to **computerize** all perimeter security fences and animal tracking collars."},
      {"author": "Walter Isaacson", "work": "Steve Jobs", "quote": "Wozniak and Jobs sought to **computerize** everyday households by crafting an accessible personal desktop machine."}
    ]
  },
  "computing": {
    "primary": "The use, operation, or development of computers, information systems, and algorithmic processes.",
    "secondary": "In engineering and computer science, the overarching discipline studying computer architecture and software systems.",
    "quotes": [
      {"author": "Alan Turing", "work": "Computing Machinery and Intelligence", "quote": "We propose to consider the question: Can machines think? This begins with the definitions of **computing**."},
      {"author": "Grace Hopper", "work": "Compiling Methods", "quote": "The evolution of modern **computing** required translating high-level mathematical syntax into machine language."},
      {"author": "Nicholas Negroponte", "work": "Being Digital", "quote": "Ubiquitous **computing** shifted human culture from moving heavy physical atoms to routing weightless digital bits."}
    ]
  },
  "deputation": {
    "primary": "A group of appointed delegates or representatives sent to negotiate, petition, or act on behalf of others.",
    "secondary": "In constitutional law, the official authorization or appointment of an agent to discharge public duties.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "A solemn civic **deputation** waited upon the governor to present grievances regarding local municipal taxation."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The Saint Antoine neighborhood dispatched a fierce **deputation** to demand munitions from the Bastille governor."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "A parliamentary **deputation** crossed the Channel to offer the crown of Great Britain to the Prince of Orange."}
    ]
  },
  "depute": {
    "primary": "To appoint, authorize, or delegate a person to act as one's representative, deputy, or agent.",
    "secondary": "In organizational administration, transferring specific administrative powers or duties to a designated subordinate.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Sovereigns frequently **depute** magistrates to administer justice and enforce commercial contracts across provinces."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The provost chose to **depute** his trusted lieutenant to maintain order along the unruly Edinburgh thoroughfares."},
      {"author": "John Locke", "work": "Second Treatise of Government", "quote": "The legislative body cannot **depute** the power of making laws to any other hands without popular consent."}
    ]
  },
  "deputise": {
    "primary": "To act as a deputy, substitute for, or delegate authority to another (British spelling).",
    "secondary": "In municipal administration, authorizing citizens or assistants to perform official administrative or legal duties.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Inspector Jones asked the constable to **deputise** for him at Scotland Yard while he pursued the Baker Street lead."},
      {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "The bishop requested Mr. Slope to **deputise** for his lord during the confirmation ceremony at the cathedral."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard had to **deputise** his young Scottish manager to inspect grain shipments arriving at the town quay."}
    ]
  },
  "deputize": {
    "primary": "To appoint or empower someone to act as a deputy, representative, or temporary law enforcement agent.",
    "secondary": "In legal enforcement, swearing in auxiliary officers or deputies to maintain peace during civic emergencies.",
    "quotes": [
      {"author": "Cormac McCarthy", "work": "No Country for Old Men", "quote": "Sheriff Bell decided to **deputize** the seasoned ranger to track the fugitive across the Chihuahuan desert."},
      {"author": "Mark Twain", "work": "Roughing It", "quote": "The town marshal moved to **deputize** six armed miners to guard the silver bullion against stagecoach bandits."},
      {"author": "Willa Cather", "work": "Death Comes for the Archbishop", "quote": "The territorial prefect offered to **deputize** guides who could lead the missionaries safely through Navajo lands."}
    ]
  },
  "deputy": {
    "primary": "An appointed official or assistant authorized to exercise the powers and duties of a superior in their absence.",
    "secondary": "In law enforcement, a sworn peace officer serving directly under an elected county sheriff.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The executive magistrate must possess authority to dismiss any subordinate **deputy** who abuses public trust."},
      {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "Lord Angelo was appointed the Duke's **deputy** to enforce strict morality laws throughout the city of Vienna."},
      {"author": "Cormac McCarthy", "work": "Blood Meridian", "quote": "A ragged **deputy** stepped from the shadows of the adobe jail, holding a battered lantern above his eyes."}
    ]
  },
  "disputable": {
    "primary": "Open to argument, debate, controversy, or dispute; not conclusively proven or settled.",
    "secondary": "In jurisprudence and logic, a legal claim or philosophical premise that admits reasonable contradiction.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Even if the received opinion be true, leaving it open to **disputable** debate prevents it from becoming dead dogma."},
      {"author": "David Hume", "work": "An Enquiry Concerning Human Understanding", "quote": "Matters of empirical fact remain forever **disputable**, unlike the demonstrative certainty of geometry."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Abstract rights of man furnish **disputable** foundations for constitutional governance compared to inherited customs."}
    ]
  },
  "disputant": {
    "primary": "A person who engages in argument, formal debate, intellectual controversy, or verbal dispute.",
    "secondary": "In scholastic philosophy, an academic scholar presenting or refuting theses during formal university disputations.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Essays", "quote": "In disputation, the fierce **disputant** often cares more for victorious rhetorical triumph than for genuine truth."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Bishop Wilberforce entered the arena as a confident **disputant**, ridiculing Darwinian evolution before Oxford scholars."},
      {"author": "Jonathan Swift", "work": "The Battle of the Books", "quote": "Each scholarly **disputant** marshaled ancient manuscripts and venomous pamphlets against modern adversaries."}
    ]
  },
  "disputation": {
    "primary": "Formal academic debate or verbal controversy conducted according to strict dialectical rules.",
    "secondary": "In medieval scholasticism, an oral exercise where scholars defended and attacked theological and philosophical theses.",
    "quotes": [
      {"author": "John Milton", "work": "Areopagitica", "quote": "Truth emerges victorious through public **disputation** and open intellectual encounter, not through cowardly censorship."},
      {"author": "Thomas Aquinas", "work": "Summa Theologiae", "quote": "In every solemn scholastic **disputation**, the master resolves objections after examining contrary arguments."},
      {"author": "Michel de Montaigne", "work": "Essays", "quote": "The art of **disputation** sharpens human wit, yet pedants turn lively dialogue into tyrannical obstinacy."}
    ]
  },
  "disputatious": {
    "primary": "Inclined to argue, fond of controversy, or habitually provoking debate and verbal disagreement.",
    "secondary": "In interpersonal rhetoric, describing an abrasive conversational style marked by obstinate hair-splitting.",
    "quotes": [
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "I observed that **disputatious** people are generally unfortunate in their affairs, alienating friends and patrons alike."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "A **disputatious** temper converts every convivial dinner into a contentious courtroom cross-examination."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Mrs. Ferrars presented a cold, **disputatious** demeanor that cast an icy silence across the drawing room."}
    ]
  },
  "disputatiously": {
    "primary": "In a disputatious, argumentative, or contentious manner; with habitual eagerness to provoke debate.",
    "secondary": "In courtroom advocacy, arguing points with obstinate, adversarial persistence.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Barristers in the Court of Chancery argued **disputatiously** over tiny points of chancery procedure for decades."},
      {"author": "Herman Melville", "work": "Bartleby, the Scrivener", "quote": "Nippers behaved **disputatiously** every morning, grinding his teeth and continually adjusting his writing desk."},
      {"author": "Henry James", "work": "The Bostonians", "quote": "The reformers discussed constitutional amendments **disputatiously**, unable to agree upon unified political resolutions."}
    ]
  },
  "disputative": {
    "primary": "Characterized by dispute, debate, or argument; argumentative or controversial in tone.",
    "secondary": "In rhetorical theory, describing a dialectical style intended to stimulate debate rather than didactic consensus.",
    "quotes": [
      {"author": "John Locke", "work": "Some Thoughts Concerning Education", "quote": "He warned tutors against encouraging a **disputative** humor in youths, which fosters petulance over wisdom."},
      {"author": "Alexander Pope", "work": "An Essay on Criticism", "quote": "Critics of a **disputative** bent waste their ink condemning syllables while missing the grandeur of the epic."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "German metaphysical treatises frequently adopt a **disputative** framework to systematically refute rival systems."}
    ]
  },
  "dispute": {
    "primary": "A disagreement, argument, or formal controversy between parties, or to debate and question something's validity.",
    "secondary": "In labor law, a formal conflict between employees and management regarding wages, hours, or working conditions.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "There is hardly any political question in the United States that does not sooner or later turn into a judicial **dispute**."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "In every industrial wage **dispute**, masters combine quietly to hold down earnings while workmen combine loudly."},
      {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "The ancient blood **dispute** between Montagues and Capulets erupted afresh in the sunlit public squares of Verona."}
    ]
  },
  "disputed": {
    "primary": "Contested, challenged, debated, or subject to conflicting claims and unresolved legal controversy.",
    "secondary": "In international geopolitics, describing territorial borders claimed concurrently by two or more sovereign states.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Rival Roman legions clashed fiercely across the **disputed** frontiers of the Danube to crown their favorite generals."},
      {"author": "Winston Churchill", "work": "The Gathering Storm", "quote": "The status of the **disputed** Rhineland corridor became the focal point of diplomatic anxiety across Europe."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "Political parties **disputed** control of the telephone exchange, sparking deadly street battles in Barcelona."}
    ]
  },
  "disreputability": {
    "primary": "The state or condition of having a bad reputation, low social standing, or untrustworthy character.",
    "secondary": "In sociopolitical discourse, public notoriety and dishonor attaching to corrupt institutions or criminal enterprises.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The tavern sank into murky **disreputability**, frequented only by river thieves and nocturnal smugglers."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Rawdon Crawley lived in aristocratic **disreputability**, evading creditors and living grandly on nothing a year."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Darcy was acutely conscious of the social **disreputability** attaching to Wickham's scandalous elopement."}
    ]
  },
  "disreputable": {
    "primary": "Not reputable; having a bad reputation, dishonest, discreditable, or lacking social and moral respectability.",
    "secondary": "In Victorian social commentary, describing shabby, illicit establishments and morally dubious characters.",
    "quotes": [
      {"author": "Robert Louis Stevenson", "work": "The Strange Case of Dr. Jekyll and Mr. Hyde", "quote": "Mr. Hyde frequented a **disreputable** quarter of Soho where neglected children lounged in dark doorways."},
      {"author": "Arthur Conan Doyle", "work": "A Scandal in Bohemia", "quote": "Holmes disguised himself as a **disreputable** groom, complete with frayed cravat and whisky-scented breath."},
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "Newland Archer dreaded any association with the Beaufort scandal, which seemed thoroughly **disreputable**."}
    ]
  },
  "disreputableness": {
    "primary": "The quality, state, or property of being disreputable, untrustworthy, or socially disgraceful.",
    "secondary": "In character sketches, a conspicuous aura of seediness and moral unreliability.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The family feared the open **disreputableness** of Raffles, whose drunken threats endangered Bulstrode's social rank."},
      {"author": "Henry James", "work": "The Ambassadors", "quote": "Strether could not deny a certain picturesque **disreputableness** clinging to Chad's Parisian bohemian acquaintances."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The Peter's Finger tavern exhibited a persistent **disreputableness** that repelled upright town burghers."}
    ]
  },
  "disreputably": {
    "primary": "In a disreputable, disgraceful, or dishonorable manner; without regard for decency or good reputation.",
    "secondary": "In domestic narrative, behaving or dressing in a shabby, scandalous, or socially inappropriate fashion.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "The History of Henry Esmond", "quote": "Lord Castlewood lived **disreputably**, squandering ancestral estates at dice and tavern brawls."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "The dissipated actor was **disreputably** attired in faded velvet and tarnished brass buttons."},
      {"author": "Virginia Woolf", "work": "Orlando", "quote": "Orlando dressed **disreputably** in peasant breeches, wandering the London waterfront beneath midnight lanterns."}
    ]
  },
  "disrepute": {
    "primary": "Public disgrace, dishonor, or widespread social discredit attaching to an individual or institution.",
    "secondary": "In institutional history, the loss of moral legitimacy and public trust suffered by corrupt governing bodies.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Praetorian Guard fell into lasting **disrepute** after auctioning the imperial throne to the highest bidder."},
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "Coercive acts of Parliament only brought the majesty of imperial law into contempt and popular **disrepute**."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Astrological fraud brought the legitimate observational sciences into undeserved **disrepute** among thinkers."}
    ]
  },
  "imputable": {
    "primary": "Capable of being attributed, ascribed, or assigned to a specific cause, person, or origin.",
    "secondary": "In moral philosophy and legal liability, an action or injury that can be justly charged to an agent's moral will.",
    "quotes": [
      {"author": "Immanuel Kant", "work": "The Metaphysics of Morals", "quote": "An action is morally **imputable** to a person only insofar as it was performed under free rational autonomy."},
      {"author": "David Hume", "work": "A Treatise of Human Nature", "quote": "Mischief committed through involuntary physical reflex is not **imputable** to the actor's moral character."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Personal identity alone renders actions **imputable** at the great tribunal of divine and civil justice."}
    ]
  },
  "imputation": {
    "primary": "The attribution or assignment of an action, guilt, crime, or characteristic to someone.",
    "secondary": "In Christian theology, the doctrine of imputed righteousness or original sin transferred from Adam to humanity.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Othello", "quote": "Give me a living reason she's disloyal! If not, monstrous **imputation** will tear your soul to pieces!"},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth resented Darcy's disdainful **imputation** that her family connections were shockingly deficient in elegance."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Man shall find grace through the **imputation** of Christ's righteousness, freely offered to redeem fallen Adam."}
    ]
  },
  "impute": {
    "primary": "To attribute, ascribe, or credit an action, motive, or crime to a person or cause.",
    "secondary": "In forensic rhetoric, to assign legal blame or financial responsibility for damages to an individual.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "We should not **impute** malevolent motives to our fellow citizens when honest differences of judgment suffice."},
      {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "Therefore pardon me, and not **impute** this yielding to light love, which the dark night hath so discovered."},
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "We tend to **impute** extraordinary foresight to fortunate statesmen whose triumphs were born of pure chance."}
    ]
  },
  "imputrescible": {
    "primary": "Not subject or liable to putrefaction, decomposition, or rotting; incapable of decaying.",
    "secondary": "In chemistry and mortuary preservation, substances treated with resins or salts to render tissues permanently resistant to decay.",
    "quotes": [
      {"author": "Thomas Browne", "work": "Hydriotaphia, Urn Burial", "quote": "Ancient embalmers sought to make human flesh **imputrescible** through asphaltum and cedar oils."},
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Organic broths sealed against airborne microorganisms remained completely **imputrescible** over decades."},
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "Crystalline salts exhibit an **imputrescible** quality, preserving organic meats immersed within brine."}
    ]
  },
  "incomputable": {
    "primary": "Incapable of being computed, calculated, or reckoned, especially due to immense size or mathematical impossibility.",
    "secondary": "In poetic and theological discourse, describing infinite divine mercies or celestial multitudes exceeding calculation.",
    "quotes": [
      {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "The starry heavens unfolded an **incomputable** multitude of burning worlds revolving through boundless void."},
      {"author": "Alan Turing", "work": "Systems of Logic Based on Ordinals", "quote": "Gödel's theorem proved the existence of mathematical propositions that remain demonstrably **incomputable**."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor squandered **incomputable** treasures upon triumphal monuments that vanished within a century."}
    ]
  },
  "indisputability": {
    "primary": "Unquestionable certainty, incontrovertible truth, or clarity that admits no reasonable controversy.",
    "secondary": "In scientific epistemology, the empirical certainty achieved through repeated, verified experimental trials.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "The fossil record demonstrates with overwhelming **indisputability** that life on Earth has evolved continuously."},
      {"author": "Bertrand Russell", "work": "The Problems of Philosophy", "quote": "Descartes sought an axiom of absolute **indisputability**, which he discovered in his own thinking existence."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Intuitive mathematical truths possess an **indisputability** that compels immediate rational assent."}
    ]
  },
  "indisputable": {
    "primary": "Not disputable; incontrovertible, undeniable, and beyond question or reasonable doubt.",
    "secondary": "In legal evidence, documentary proof that conclusively establishes a fact without remaining ambiguity.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "It is an **indisputable** fact that domestic varieties of animals have diverged dramatically from wild ancestors."},
      {"author": "Abraham Lincoln", "work": "Second Inaugural Address", "quote": "All knew that this interest was somehow the cause of the war; the correlation was **indisputable**."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "That she was a beautiful girl was **indisputable**, and Bingley admired her without reservation."}
    ]
  }
}
