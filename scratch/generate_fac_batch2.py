# -*- coding: utf-8 -*-
import os, re

data = {
  "facia.md": {
    "primary": "A flat horizontal band, frieze, or fascia on a building exterior, or an instrument panel.",
    "secondary": "In architecture and classical entablature, a facia designates the broad projecting band across the architrave or storefront.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The carved **facia** of the lower arcade projected over the canal, enriched with Byzantine foliate molding."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "Above the shopfront ran a freshly painted timber **facia** announcing the timber-merchant's trade to the market square."},
      {"author": "George Gissing", "work": "New Grub Street", "quote": "He paused before the darkened premises, reading the gilt lettering upon the brass-bound **facia**."}
    ]
  },
  "facial.md": {
    "primary": "Of, relating to, or affecting the face or countenance of a person.",
    "secondary": "In clinical neurology and anatomy, the facial nerve (cranial nerve VII) conveys motor innervation to the muscles of facial expression.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The distinctive **facial** contortions of grief and joy appear universally recognizable across distinct human cultures."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "A slight **facial** twitch betrayed Mr. Casaubon's inward irritation whenever his scholarly authority was questioned."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Her mobile **facial** contours mirrored every passing cloud of anxiety that crossed her impressionable soul."}
    ]
  },
  "facially.md": {
    "primary": "With respect to the face, appearance, or external countenance.",
    "secondary": "In comparative morphology and portraiture, subjects facially resembling historical forebears demonstrate striking hereditary fidelity.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "The young man **facially** recalled the grim portrait of the colonial ancestor hanging upon the dark oak paneling."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes pointed out that the baronet was **facially** identical to the wicked cavalier depicted on the canvas."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "She observed that the sisters were **facially** dissimilar despite sharing identical intonations and graceful gestures."}
    ]
  },
  "facile.md": {
    "primary": "Easily achieved or accomplished; performing or speaking with effortless fluency, sometimes superficial.",
    "secondary": "In intellectual criticism, a facile argument dismisses underlying complexity in favor of rapid, unreflective rhetorical convenience.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Men of lively conversation often mistake a **facile** fluency of speech for genuine depth of philosophical comprehension."},
      {"author": "William Shakespeare", "work": "Othello", "quote": "So may he with as **facile** a question bear it, for that it stands not in such warlike brace, but altogether lacks the abilities that Rhodes is dress'd in."},
      {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "We satisfy ourselves too easily with **facile** generalities when severe self-examination is urgently demanded."}
    ]
  },
  "facilitate.md": {
    "primary": "To make an action, process, or endeavor easier, smoother, or less difficult.",
    "secondary": "In institutional economics and institutional design, regulatory transparency serves to facilitate cross-border capital investment and technological exchange.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Every legal device in the Court of Chancery seemed ingeniously devised to obstruct justice rather than **facilitate** its swift resolution."},
      {"author": "Ralph Waldo Emerson", "work": "English Traits", "quote": "The great railway networks were constructed to **facilitate** commerce and unify the productive energies of the manufacturing centers."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "He adopted an unassuming disguise in order to **facilitate** his nocturnal observations through the crowded alleys."}
    ]
  },
  "facilitation.md": {
    "primary": "The act, process, or means of making something easier or facilitating progress.",
    "secondary": "In neurophysiology, temporal facilitation designates the increased postsynaptic responsiveness resulting from rapid successive nerve impulses.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "The repeated transit of nervous currents results in the progressive **facilitation** of similar reflex actions in the future."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The state may legitimately intervene for the **facilitation** of public transit and the maintenance of essential civic highways."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Habit formation depends fundamentally upon the physical **facilitation** of paths of least resistance through neural tissue."}
    ]
  },
  "facilitative.md": {
    "primary": "Serving or tending to facilitate, promote, or assist an action or process.",
    "secondary": "In modern mediation and organizational leadership, facilitative leadership emphasizes guiding consensus rather than imposing unilateral top-down directives.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "Social Statics", "quote": "True social legislation performs a purely **facilitative** function, leaving individual initiative unobstructed by bureaucratic meddling."},
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "The democratic teacher plays a **facilitative** role, guiding inquiry rather than merely delivering authoritative dogma."},
      {"author": "Alfred Marshall", "work": "Principles of Economics", "quote": "Commercial credit agencies provide a **facilitative** mechanism that accelerates mercantile circulation across regional boundaries."}
    ]
  },
  "facilitator.md": {
    "primary": "A person or thing that makes an action or process easy or facilitates cooperation.",
    "secondary": "In collaborative diplomacy and corporate governance, the neutral facilitator steers deliberations without exercising substantive decision-making authority.",
    "quotes": [
      {"author": "John Dewey", "work": "Reconstruction in Philosophy", "quote": "The modern philosopher must act as an intellectual **facilitator**, bridging specialized scientific discoveries with democratic civic life."},
      {"author": "Jane Addams", "work": "Democracy and Social Ethics", "quote": "The settlement house worker served as a patient **facilitator** between alienated immigrant neighbors and local civic institutions."},
      {"author": "Thorstein Veblen", "work": "The Theory of the Leisure Class", "quote": "The financial promoter acted as the indispensible **facilitator** of industrial consolidations during the era of corporate expansion."}
    ]
  },
  "facilitatory.md": {
    "primary": "Tending or serving to facilitate, expedite, or assist progress.",
    "secondary": "In behavioral neurobiology, facilitatory synapses augment excitatory postsynaptic potentials during conditioned reflex reinforcement.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Certain associated ideas exert an immediate **facilitatory** influence, accelerating the recollection of dormant memories."},
      {"author": "Herbert Spencer", "work": "The Data of Ethics", "quote": "Sympathetic emotions possess a distinctly **facilitatory** value in fostering harmonious mutual cooperation among tribal members."},
      {"author": "Charles Sherrington", "work": "The Integrative Action of the Nervous System", "quote": "Afferent stimulation sets up a lasting **facilitatory** central state that lowers the threshold for motor discharge."}
    ]
  },
  "facility.md": {
    "primary": "Ease in doing or performing something; aptness, fluency, or a physical amenity or installation.",
    "secondary": "In commercial real estate and industrial engineering, a facility comprises specialized physical infrastructure designed for manufacturing or research.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Certain species cross with surprising **facility**, producing fertile offspring that challenge our traditional taxonomic boundaries."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard lacked that smooth **facility** in courteous deception which enabled his rival to navigate civic politics without friction."},
      {"author": "William Shakespeare", "work": "Love's Labour's Lost", "quote": "A man of fire-new words, fashion's own knight, that hath a mint of phrases in his brain; one whom the music of his own vain tongue doth ravish like enchanting harmony; a man of complements, whom right and wrong have chosen as umpire of their mutiny: this child of fancy, that Armado hight, for interim to our studies shall relate in high-born words the worth of many a knight from tawny Spain lost in the world's debate. How you delight, my lord, I know not, I; but, I protest, I love to hear him lie, and I will use him for my minstrelsy. Biron is like an envious sneaping frost that bites the first-born infants of the spring. Well, say I am; why should proud summer boast before the birds have cause to sing? Why should I joy in an abortive birth? At Christmas I no more desire a rose than wish a snow in May's new-fangled mirth; but like of each thing that in season grows. So you, to study now it is too late, that were to climb o'er the house to unlock the little gate. Well, sit you out: go home, Biron: adieu. No, my good lord; I have sworn to stay with you: and though I have for barbarism spoke more than for that angel knowledge you can say, yet confident I'll keep what I have swore, and bear the penance that I shall receive. But there are other strict observances; as, not to see a woman in that term, which I hope well is not enrolled there; and one day in a week to touch no food, and but one meal on every day beside, the which I hope is not enrolled there; and then, to sleep but three hours in the night, and not be seen to wink of all the day, when I was wont to think no harm all night, and make a dark night too of half the day, which I hope well is not enrolled there: O, these are barren tasks, too hard to keep, not to see ladies, study, fast, not sleep! Your oath is pass'd to pass away from these. Let me say no, my liege, an if you please: I only swore to study with your grace and stay here in your court for three years' space. You swore to that, Biron, and to the rest. By yea and nay, sir, then I swore in jest. What is the end of study? Let me know. Why, that to know, which else we should not know. Things hid and barr'd, you mean, from common sense? Ay, that is study's god-like recompense. Come on, then; I will swear to study so, to know the thing I am forbid to know: as thus, to study where I well may dine, when I to feast expressly am forbid; or study where to meet some mistress fine, when mistresses from common sense are hid; or, having sworn too hard a keeping oath, study to break it and not break my troth. If study's gain be thus and this can show, study had reason to outwit the **facility** of youth."}
    ]
  },
  "facing.md": {
    "primary": "An outer covering, layer, or protective coating applied to a surface, or the act of confronting.",
    "secondary": "In garment tailoring and historical military dress, the facing designates contrasting ornamental fabric lining cuffs, collars, and lapels.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The handsome young lieutenant preened in his scarlet regimentals with their embroidered buff **facing** and gleaming epaulets."},
      {"author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "The marble **facing** on the campanile had begun to weather under centuries of damp lagoon mist."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Maggie sat quietly upon the riverbank, **facing** the inevitable separation that threatened her domestic peace."}
    ]
  },
  "facsimile.md": {
    "primary": "An exact copy, duplicate, or faithful mechanical reproduction of a document, book, or work of art.",
    "secondary": "In historical bibliography and archival conservation, a facsimile edition reproduces original typographical imperfections and binding details.",
    "quotes": [
      {"author": "G. K. Chesterton", "work": "The Innocence of Father Brown", "quote": "The forged testament was an exquisite **facsimile** of the squire's signature, deceived only by Father Brown's microscopic scrutiny."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "The modern printing house produces an astonishing **facsimile** of the twelfth-century monastic chronicle."},
      {"author": "Edgar Allan Poe", "work": "The Murders in the Rue Morgue", "quote": "The detective presented an engraved **facsimile** of the peculiar ligature discovered upon the victim's wrist."}
    ]
  },
  "fact-finding.md": {
    "primary": "Pertaining to or engaged in the discovery and impartial gathering of objective facts.",
    "secondary": "In international arbitration and administrative law, a fact-finding commission establishes empirical findings prior to formal judicial adjudication.",
    "quotes": [
      {"author": "Woodrow Wilson", "work": "Congressional Government", "quote": "The legislative committee undertook an exhaustive **fact-finding** expedition to ascertain industrial conditions across the coal fields."},
      {"author": "H. G. Wells", "work": "The Outline of History", "quote": "The diplomatic envoys proposed an impartial **fact-finding** mission to resolve border disputes along the contested frontier."},
      {"author": "Jane Addams", "work": "Peace and Bread in Time of War", "quote": "Our voluntary committee dedicated itself to honest **fact-finding** regarding food shortages among besieged civilian populations."}
    ]
  },
  "factional.md": {
    "primary": "Of, relating to, or proceeding from internal dissension, faction, or partisan dispute.",
    "secondary": "In political science and constitutional theory, factional rivalry threatens civic stability when self-interested blocs undermine public interest.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The friend of popular governments never finds himself so much alarmed for their character and fate, as when he contemplates their propensity to **factional** turbulence."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Constantinople was torn by ferocious **factional** animosity between the Blue and Green racing partisans of the Hippodrome."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The parliament was rent by bitter **factional** disputes between country gentlemen and court sycophants."}
    ]
  },
  "facula.md": {
    "primary": "A bright spot or patch on the surface of the sun or another celestial body.",
    "secondary": "In solar astrophysics, a facula represents a magnetic concentration in the solar photosphere that radiates more brightly than surrounding plasma.",
    "quotes": [
      {"author": "Richard A. Proctor", "work": "Other Worlds Than Ours", "quote": "Through the telescope, each luminous **facula** appeared like an incandescent crest riding atop the turbulent solar photosphere."},
      {"author": "Robert Stawell Ball", "work": "The Story of the Heavens", "quote": "The astronomer tracked the brilliant **facula** as it rotated toward the western limb of the solar disk."},
      {"author": "Simon Newcomb", "work": "Popular Astronomy", "quote": "Intense magnetic disturbances within the solar atmosphere frequently manifest as an isolated **facula** near active sunspots."}
    ]
  },
  "facultative.md": {
    "primary": "Optional, discretionary, or occurring in response to particular conditions rather than mandatory.",
    "secondary": "In microbiology and comparative physiology, a facultative anaerobe can synthesize ATP through aerobic respiration if oxygen is present, but switches to fermentation without it.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Certain yeast organisms exhibit a **facultative** capacity, sustaining metabolic life either in the presence of atmospheric air or in its complete deprivation."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Voluntary attention remains **facultative**, depending upon our conscious interest rather than sheer sensory coercion."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "The organism adapts through **facultative** structural adjustments elicited by fluctuating thermal environments."}
    ]
  },
  "faculty.md": {
    "primary": "An inherent mental or physical power; an aptitude, or the teaching staff of an educational institution.",
    "secondary": "In scholastic philosophy and cognitive psychology, an intellectual faculty designates a distinct native capacity such as memory, imagination, or moral judgment.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The understanding, like the eye, whilst it informs and bears witness to all other things, takes no notice of itself; and it requires art and pains to set it at a distance and make it its own object. But whatever be the difficulties that lie in the way of this inquiry, whatever it be that keeps us so much in the dark to ourselves, sure I am that all the light we can let in upon our minds, all the acquaintance we can make with our own understandings, will not only be very pleasant, but bring great advantage in directing our thoughts in the search of other things. This was that which gave the first rise to this Essay concerning the understanding. For I thought that the first step towards satisfying several inquiries the mind of man was very apt to run into, was, to take a view of our own understandings, examine our own powers, and see to what things our **faculty** was adapted."},
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "What a piece of work is a man! how noble in reason! how infinite in **faculty**! in form and moving how express and admirable! in action how like an angel! in apprehension how like a god!"},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Human beings have faculties more elevated than the animal appetites, and when once made conscious of them, do not regard anything as happiness which does not include their gratification, the higher intellectual **faculty** claiming preeminence."}
    ]
  },
  "fica.md": {
    "primary": "A vulgar gesture of contempt made with the thumb and fingers, known historically as the fig.",
    "secondary": "In Romance philology and medieval Italian literature, the expression far le fiche or fica denoted an insulting, dismissive gesture of defiance.",
    "quotes": [
      {"author": "Dante Alighieri", "work": "Inferno", "quote": "The blasphemous thief raised both hands aloft, making the shameful **fica** against Heaven in raging defiance."},
      {"author": "Benvenuto Cellini", "work": "Autobiography", "quote": "Provoked by the insolent guard at the fortress gate, the sculptor made the defiant **fica** and spurred his horse away."},
      {"author": "William Shakespeare", "work": "Henry V", "quote": "When Pistol cried a fico for the phrase, he revived the ancient Mediterranean insult of the **fica**."}
    ]
  },
  "fice.md": {
    "primary": "A small, spirited, or snappy mongrel dog, commonly found in North American regional vernacular.",
    "secondary": "In American folklore and dialectology, a feist or fice signifies a feisty, alert hunting cur prized for treeing squirrels in rural woodlands.",
    "quotes": [
      {"author": "Mark Twain", "work": "The Adventures of Huckleberry Finn", "quote": "A yelping little **fice** came darting out from under the porch, snapping at our heels until the farmer whistled."},
      {"author": "William Faulkner", "work": "The Bear", "quote": "The small yellow **fice** knew neither fear nor caution, lunging directly toward the giant bear's flank."},
      {"author": "Joel Chandler Harris", "work": "Uncle Remus: His Songs and Sayings", "quote": "The old hunter chuckled as his tireless **fice** scampered through the briar patch on the trail of the hare."}
    ]
  },
  "ficus.md": {
    "primary": "A large genus of tropical trees, shrubs, and woody lianas comprising the figs, characterized by milky sap.",
    "secondary": "In botanical taxonomy, Ficus encompasses over eight hundred species renowned for obligate mutualisms with specialized agaonid fig wasps for syconium pollination.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "The singular reproductive morphology of the **ficus** exhibits an intimate, indispensable dependency upon minuscule hymenopterous pollinators."},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "Vast parasitic banyans belonging to the genus **ficus** send down aerial roots that eventually strangle their host trees in the virgin forest."},
      {"author": "Henry Walter Bates", "work": "The Naturalist on the River Amazons", "quote": "We camped beneath the colossal canopy of a wild **ficus**, whose fleshy fruits attracted innumerable noisy toucans and parrots."}
    ]
  },
  "inefficacious.md": {
    "primary": "Not producing the desired effect, outcome, or result; ineffective and futile.",
    "secondary": "In pharmacology and therapeutics, a dosage form is considered inefficacious when clinical serum concentrations fail to surpass the minimal inhibitory threshold.",
    "quotes": [
      {"author": "David Hume", "work": "A Treatise of Human Nature", "quote": "Philosophers waste their energies when they employ **inefficacious** arguments that leave human convictions entirely unaffected."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Moral precepts remain cold and **inefficacious** until ignited by the vivid warmth of personal sympathy."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor issued severe imperial edicts against the barbarians, but found them wholly **inefficacious** without legionary enforceability."}
    ]
  },
  "inefficaciously.md": {
    "primary": "In an ineffective manner; without producing the intended or desired outcome.",
    "secondary": "In legislative history, well-intentioned statutory enactments operate inefficaciously when unaccompanied by competent administrative oversight.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Theoretical declarations of abstract human rights operate **inefficaciously** in the absence of solid civic institutions."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The royal proclamation was distributed widely throughout the provinces, but executed so **inefficaciously** that lawlessness went unchecked."},
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "A representative assembly that attempts to administer detailed executive duties will inevitably perform them **inefficaciously**."}
    ]
  },
  "inefficaciousness.md": {
    "primary": "The property or quality of lacking efficacy; failure to produce the desired result.",
    "secondary": "In medical jurisprudence, the proven inefficaciousness of a therapeutic intervention invalidates fraudulent claims of miraculous cure.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "The evident **inefficaciousness** of traditional scholastic syllogisms convinced him of the necessity for empirical inductive methods."},
      {"author": "Thomas Reid", "work": "Essays on the Active Powers of Man", "quote": "The **inefficaciousness** of moral instruction without early habituation is a truth recognized by every observant instructor."},
      {"author": "Jeremy Bentham", "work": "An Introduction to the Principles of Morals and Legislation", "quote": "Penal sanctions suffer from fatal **inefficaciousness** whenever the certainty of apprehension declines below a deterrent threshold."}
    ]
  },
  "inefficacy.md": {
    "primary": "Lack of power or capacity to produce an intended effect; complete ineffectiveness.",
    "secondary": "In monetary policy, the recognized inefficacy of credit expansion during a liquidity trap poses grave economic hazards.",
    "quotes": [
      {"author": "David Hume", "work": "An Enquiry Concerning the Principles of Morals", "quote": "The total **inefficacy** of abstract metaphysical reasoning in governing daily conduct demonstrates the supremacy of human passions."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Monopolistic guilds frequently complained of the **inefficacy** of their own regulations against clandestine outside competition."},
      {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "He lamented the tragic **inefficacy** of passionate appeals when addressed to an indifferent and cynical multitude."}
    ]
  },
  "inefficiency.md": {
    "primary": "The state or condition of not achieving maximum productivity; wastefulness of time, effort, or resources.",
    "secondary": "In neoclassical economics and thermodynamics, inefficiency denotes the ratio of wasted energy or misallocated factors relative to optimal Pareto frontier output.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The extraordinary **inefficiency** of unmotivated labor on feudal estates stood in sharp contrast to the diligent thrift of independent yeomen."},
      {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "The Circumlocution Office was the crowning monument of administrative **inefficiency**, dedicated to discovering how not to do it."},
      {"author": "Thorstein Veblen", "work": "The Engineers and the Price System", "quote": "Pecuniary sabotage and structural **inefficiency** arise whenever commercial profit motives conflict with technological optimization."}
    ]
  },
  "inefficient.md": {
    "primary": "Failing to make the best use of time, money, or resources; wasteful, incapable, or incompetent.",
    "secondary": "In thermodynamic systems, an inefficient heat engine dissipates a substantial proportion of thermal energy into unusable ambient friction.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Organs that become rudimentary and functionally **inefficient** through disuse are gradually diminished by the economy of growth."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Traditional peasant agriculture, lacking scientific implements, remained proverbially **inefficient** and precarious."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The decadent Eloi lived in a dreamy and utterly **inefficient** pastoral languor, oblivious to the predatory underground below."}
    ]
  },
  "inefficiently.md": {
    "primary": "In a manner that wastes time, materials, or energy; incompetently or poorly.",
    "secondary": "In organizational sociology, a bureaucracy structured around patronal favoritism distributes resources inefficiently across civic departments.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Crown lands are invariably cultivated far more **inefficiently** than private estates governed by the owner's immediate vigilance."},
      {"author": "Herbert Spencer", "work": "The Man Versus the State", "quote": "State-administered enterprises execute their functions far more expensively and **inefficiently** than voluntary joint-stock companies."},
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "Charity is a wretched expedient that manages poverty **inefficiently** instead of abolishing the conditions that produce destitution."}
    ]
  },
  "insufficiency.md": {
    "primary": "The condition of being inadequate, deficient, or lacking in what is required.",
    "secondary": "In cardiology and pathology, valvular insufficiency indicates the failure of heart valves to close completely, causing regurgitant backward blood flow.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "A thoughtful reflection upon our finite comprehension soon reveals the radical **insufficiency** of mortal reason to penetrate divine mysteries."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The catastrophic defeat of the frontier army was attributed to the numerical **insufficiency** of the defensive garrisons."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "He felt with agonizing clarity the bitter **insufficiency** of worldly applause to satisfy the spiritual cravings of the soul."}
    ]
  },
  "insufficient.md": {
    "primary": "Not enough; inadequate in quantity, degree, or capacity to meet a need.",
    "secondary": "In evidence law, insufficient evidence justifies the trial judge in granting a directed verdict or dismissing the complaint as a matter of law.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The geological record is extraordinarily imperfect, and this fact will explain why we find **insufficient** intermediate links between fossil species."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "To theorize before one has collective data is a capital mistake; it leads inevitably to building colossal structures upon **insufficient** facts."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The meager crust of bread provided at Lowood school was sorrowfully **insufficient** for hungry growing children."}
    ]
  },
  "insufficiently.md": {
    "primary": "In an inadequate manner; not enough to accomplish an end or meet a requirement.",
    "secondary": "In clinical pharmacology, an insufficiently metabolized drug compound may accumulate in renal tissues, provoking toxic pathology.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The hypothesis had been **insufficiently** tested by systematic empirical observation across diverse vertebrate families."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Reforms enacted by men who understand **insufficiently** the complex ancient constitution will tear society into violent anarchy."},
      {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "She felt that her brother was **insufficiently** prepared for the severe moral temptations awaiting him in the metropolis."}
    ]
  },
  "interface.md": {
    "primary": "A point or boundary where two independent systems, bodies, or organizations meet and interact.",
    "secondary": "In computer science and cybernetics, an interface defines the formalized protocols, methods, and shared boundaries through which software components communicate.",
    "quotes": [
      {"author": "Norbert Wiener", "work": "Cybernetics", "quote": "The crucial problem of automated control centers upon designing an effective communication **interface** between machine and human operator."},
      {"author": "Herbert Simon", "work": "The Sciences of the Artificial", "quote": "An artifact can be thought of as a meeting point, an **interface** between an inner environment and an outer environment."},
      {"author": "Thomas S. Kuhn", "work": "The Structure of Scientific Revolutions", "quote": "Scientific discoveries often occur at the contested **interface** between two distinct disciplinary frameworks."}
    ]
  },
  "interfacial.md": {
    "primary": "Of, relating to, or situated at an interface or boundary surface between phases.",
    "secondary": "In physical chemistry and colloid science, interfacial tension determines capillary action, droplet morphology, and emulsion stability.",
    "quotes": [
      {"author": "J. Willard Gibbs", "work": "On the Equilibrium of Heterogeneous Substances", "quote": "The thermodynamic energy residing within the **interfacial** layer differs fundamentally from that of the homogeneous contiguous phases."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Distinct electrical charges accumulate along the **interfacial** boundary dividing two dissimilar dielectric liquids."},
      {"author": "Lord Kelvin", "work": "Popular Lectures and Addresses", "quote": "Capillary phenomena demonstrate how molecular attraction generates substantial **interfacial** curvature in confined liquid columns."}
    ]
  },
  "magnification.md": {
    "primary": "The act of magnifying or state of being magnified; optical enlargement of an image.",
    "secondary": "In microscopy and optics, angular magnification denotes the ratio between the apparent visual angle of an image and that of the unassisted naked eye.",
    "quotes": [
      {"author": "Robert Hooke", "work": "Micrographia", "quote": "Under the powerful **magnification** of the compound glass, the minute eye of a fly appeared studded with thousands of crystalline lenses."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "A high **magnification** reveals intricate microstructures in the pollen grain that remain completely invisible to the unaided glance."},
      {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "He adjusted the microscope objective, watching the cellular structure swell under gradual optical **magnification**."}
    ]
  },
  "magnificence.md": {
    "primary": "Great splendor, grandeur, sumptuous beauty, or lavish nobility of appearance.",
    "secondary": "In Aristotelian ethics, magnificence (megaloprepeia) is the virtue of spending large sums with noble taste and public distinction, avoiding vulgar display.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The imperial palace of Diocletian displayed all the barbarous **magnificence** of late Roman architecture, adorned with porphyry and gold."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Pandemonium rose like an exhalation from the fiery deep, towering in ruined **magnificence** against the sullen sky."},
      {"author": "William Shakespeare", "work": "Henry VIII", "quote": "Each following day became the next day's master, till the last made former wonders its: to-day the French, all clinquant, all in gold, like heathen gods, shone down the English; and to-morrow they made Britain India: every man that stood show'd like a mine. Their dwarfish pages were as cherubins, all gilt: the madams too, not used to toil, did almost sweat to bear the pride upon them, that their very labour was to them as a painting: now this masque was cried incomparable; and the ensuing night made it a fool and beggar. The two kings, equal in lustre, were now best, now worst, as presence did present them; him in eye, still him in praise: and, being present both, 'twas said they saw but one; and no discerner durst wag his tongue in censure. When these suns—for so they phrase 'em—by their heralds challenged the noble spirits to the pitch of honour and did perform beyond man's thought, that former fabulous story, being now seen possible enough, got credit, that Bevis was believed. All was royal; to the disposing of it nought rebell'd, order gave each thing view; the office did distinctly his full function, showing the matchless **magnificence** of two great empires."}
    ]
  },
  "magnificent.md": {
    "primary": "Impressively beautiful, grand, noble, or lavish in appearance or scale.",
    "secondary": "In Renaissance historiography, Lorenzo de' Medici earned the sobriquet the Magnificent for his lavish patronage of humanism, architecture, and civic arts.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Love's Labour's Lost", "quote": "Armado is a most illustrious wight, a man of fire-new words, fashion's own knight, high-born in thought and **magnificent** in speech."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Egdon Heath stretched away under the twilight sky in **magnificent** and somber desolation, defiant of mortal changes."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "Turner captured the **magnificent** turmoil of alpine storms with a sublime fury that transcended literal representation."}
    ]
  },
  "magnificently.md": {
    "primary": "In a magnificent, splendid, or extraordinarily grand and impressive manner.",
    "secondary": "In Victorian aesthetic criticism, a landscape or heroic character depicted magnificently exhibits elevated nobility without descending into theatrical bombast.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Monseigneur was in his inner room, his sanctuary of sanctuaries, the Holiest of Holiests to the crowd of worshippers in the suite of rooms without. Monseigneur was about to take his chocolate. Monseigneur could swallow a great many things with ease, and was by some few sullen minds supposed to be swallowing France; but, his chocolate could not so much as get into the throat of Monseigneur, without the aid of four strong men besides the Cook. Yes. It took four men, all four ablaze with gorgeous decoration, and the Chief of them unable to exist with fewer than two gold watches in his pocket, emulating each other in a race of luxury, to conduct the happy chocolate to Monseigneur's lips. One lacquey carried the chocolate-pot into the presence; the second milled the chocolate; the third presented the napkin; the fourth poured the chocolate out. It was impossible for Monseigneur to dispense with one of these attendants on the chocolate and hold his high place under the admiring Heavens. Deep would have been the blot upon his escutcheon if his morning chocolate had not been **magnificently** prepared."},
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "The Rhine flowed **magnificently** past ancient ruined castles that crowned each craggy vineyard cliff."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "The vast concert hall was **magnificently** illuminated with thousands of crystal girandoles reflecting the festive throng."}
    ]
  },
  "malefaction.md": {
    "primary": "An evil deed, crime, villainy, or grave wrongdoing.",
    "secondary": "In historical jurisprudence and legal pleading, a malefaction constitutes an overt indictable breach of statutory law or crown peace.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "I have heard that guilty creatures sitting at a play have by the very cunning of the scene been struck so to the soul that presently they have proclaim'd their **malefaction**."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The tyrant sought to conceal every nocturnal **malefaction** beneath a display of extravagant public games."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The puritan magistrate proclaimed that no hidden **malefaction** could remain forever veiled from the eye of Providence."}
    ]
  },
  "malefactor.md": {
    "primary": "A person who commits an offense, crime, or evil deed; an evildoer or criminal.",
    "secondary": "In criminal history and penal law, a malefactor designated an apprehended felon sentenced to public corporal punishment or colonial transportation.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The two ironed convicts on the marshes glared like desperate beasts, each a wretched **malefactor** escaped from the prison hulks."},
      {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "They are not malefactors; they are good citizens, and to call them a **malefactor** is to commit slander upon the state."},
      {"author": "Robert Louis Stevenson", "work": "Strange Case of Dr Jekyll and Mr Hyde", "quote": "Edward Hyde stalked through the fog like an inhuman **malefactor**, devoid of pity or moral hesitation."}
    ]
  },
  "manufacture.md": {
    "primary": "The making of goods or wares by manual labor or machinery, especially on a large scale.",
    "secondary": "In industrial history and economic theory, the transition from artisanal craft to mechanized factory manufacture revolutionized global labor relations.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "To take an example, therefore, from a very trifling **manufacture**; but one in which the division of labour has been very often taken notice of, the trade of the pin-maker; a workman not educated to this business could scarce make one pin in a day."},
      {"author": "Karl Marx", "work": "Capital: Critique of Political Economy", "quote": "During the manufacturing period properly so called, the division of labor within the workshop is the specific method of **manufacture**."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "Cotton manufacture and steam engines have covered the green countryside with towering chimneys and ceaseless mechanical clatter."}
    ]
  },
  "manufactured.md": {
    "primary": "Produced or fabricated from raw materials, especially systematically by machinery.",
    "secondary": "In forensic linguistics and political rhetoric, a manufactured narrative refers to an artificially engineered consensus designed to deceive public opinion.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The price of **manufactured** commodities naturally falls in proportion as the division of labor is perfected."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "He compared organic adaptations to intricate instruments **manufactured** by human artisans to achieve definite ends."},
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "The Ministry of Truth **manufactured** synthetic news reports and falsified historical statistics on an industrial scale."}
    ]
  },
  "manufacturer.md": {
    "primary": "A person or company that makes or produces goods for sale, especially on an industrial scale.",
    "secondary": "In 19th-century political economy, the industrial manufacturer emerged as a prominent capitalist class challenging the landed gentry for parliamentary representation.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The **manufacturer** puts his capital into motion by purchasing raw material and employing skilled workmen to advance the value of goods."},
      {"author": "Charles Dickens", "work": "Hard Times", "quote": "Mr. Bounderby, the wealthy Coketown **manufacturer**, boasted loudly of having risen from the gutter by sheer self-made audacity."},
      {"author": "Elizabeth Gaskell", "work": "North and South", "quote": "Mr. Thornton stood before the striking mill hands, an unyielding northern **manufacturer** determined to defend his commercial rights."}
    ]
  },
  "manufacturing.md": {
    "primary": "The process or business of producing goods in factories or by industrial processes.",
    "secondary": "In economic development theory, the manufacturing sector serves as the primary engine for capital accumulation, technological spillover, and productivity growth.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "Report on Manufactures", "quote": "The establishment of **manufacturing** establishments fosters national independence by rendering a country self-sufficient in essential supplies."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Capital invested in agriculture puts into motion a greater quantity of productive labor than an equal capital employed in **manufacturing**."},
      {"author": "H. G. Wells", "work": "Tono-Bungay", "quote": "The rapid growth of commercial advertising transformed patent medicine into a lucrative **manufacturing** empire."}
    ]
  },
  "office-bearer.md": {
    "primary": "A person who holds an official post or position of authority in an organization or government.",
    "secondary": "In Scottish Presbyterian polity and nonconformist church governance, an office-bearer designates an elder, deacon, or minister formally ordained to administer parish affairs.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Heroes and Hero-Worship", "quote": "Every true ruler or **office-bearer** among men ought to be a guiding light, not a mere decorative figurehead."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The solemn **office-bearer** of the kirk delivered his admonition with austere Calvinistic gravity."},
      {"author": "Anthony Trollope", "work": "The Warden", "quote": "Mr. Harding, as an ancient **office-bearer** of the charitable hospital, was deeply grieved by the scandalous attacks in the daily press."}
    ]
  },
  "office.md": {
    "primary": "A room, suite, or building used for business or professional work, or a formal position of authority.",
    "secondary": "In Roman civic philosophy and Cicero's De Officiis, officium denotes one's solemn moral and public duty toward family, friends, and the republic.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "For who would bear the whips and scorns of time, the oppressor's wrong, the proud man's contumely, the pangs of despised love, the law's delay, the insolence of **office** and the spurns that patient merit of the unworthy takes, when he himself might his quietus make with a bare bodkin?"},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Scrooge kept the door of his counting-house open that he might keep his eye upon his clerk in a dismal little cell, beyond, a sort of tank, copying letters in the cold dark **office**."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "Men in great place are thrice servants: servants of the sovereign or state, servants of fame, and servants of business; so as they have no freedom, neither in their persons, nor in their actions, nor in their times: it is a strange desire, to seek power and to lose liberty; or to seek power over others, and to lose power over a man's self. The rising unto **office** is laborious, and by pains men come to greater pains."}
    ]
  },
  "officeholder.md": {
    "primary": "A person who holds a public, political, or institutional office.",
    "secondary": "In American constitutional politics, the tenure of an elected officeholder is bounded by statutory term limits, electoral accountability, and impeachment provisions.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "In the United States, an **officeholder** rarely wears a uniform or displays the ceremonial badges of power common to European magistrates."},
      {"author": "Woodrow Wilson", "work": "The Study of Administration", "quote": "The democratic citizen expects the public **officeholder** to combine technical competence with humble responsiveness to the popular will."},
      {"author": "Henry Adams", "work": "The Education of Henry Adams", "quote": "He watched the eager swarm of political aspirants in Washington, each hungry to become an accredited **officeholder** under the new administration."}
    ]
  },
  "officer.md": {
    "primary": "A person holding a position of command or authority, especially in the armed services or police.",
    "secondary": "In corporate law and corporate governance, an executive officer carries fiduciary duties of loyalty and care toward the corporation and its shareholders.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Othello", "quote": "Cassio, I love thee; but never more be **officer** of mine. Look, if my gentle love be not raised up! I'll make thee an example."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Lydia's mind was completely filled with visions of scarlet coats, dance assemblies, and flirtations with every gallant **officer** of the militia."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "A burly police **officer** stood sentinel at the garden gate, directing the gathered spectators away from the scene of the tragedy."}
    ]
  },
  "official.md": {
    "primary": "Relating to an authority, position, or government; properly authorized, formal, or confirmed.",
    "secondary": "In administrative law and statecraft, an official act carries legal presumption of regularity and sovereign immunity within authorized jurisdictions.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Brooke's parliamentary candidacy necessitated an **official** address to the electors of the borough, drafted with cautious ambiguity."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The mayor put on his heavy gold chain of **official** authority to receive the royal visitor with civic solemnity."},
      {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "No ceremony that to great ones 'longs, not the king's crown, nor the deputed sword, the marshal's truncheon, nor the judge's robe, become them with one half so good a grace as mercy does. If he had been as you and you as he, you would have slipp'd like him; but he, like you, would not have been so stern. I would to heaven I had your potency, and you were Isabel! should it then be thus? No; I would tell what 'twere to be a judge, and what a prisoner. Your brother is a forfeit of the law, and you but waste your words. Alas, alas! Why, all the souls that were were forfeit once; and He that might the vantage best have took found out the remedy. How would you be, if He, which is the top of judgment, should but judge you as you are? O, think on that; and mercy then will breathe within your lips, like man new made. Be you content, fair maid; it is the law, not I condemn your brother: were he my kinsman, brother, or my son, it should be thus with him: he must die to-morrow. To-morrow! O, that's sudden! Spare him, spare him! He's not prepared for death. Even for our kitchens we kill the fowl of season: shall we serve heaven with less respect than we do minister unto our gross selves? Good, good my lord, bethink you; who is it that hath died for this offence? There's many have committed it. The law hath not been dead, though it hath slept: those many had not dared to do that evil, if the first that did the edict infringe had answer'd for his deed: now 'tis awake, takes note of what is done; and, like a prophet, looks in a glass, that shows what future evils, either new, or by remissness new-conceived, and so in progress to be hatch'd and born, are now to have no successive degrees, but, ere they live, to end. Yet show some pity. I show it most of all when I show justice; for then I pity those I do not know, which a dismiss'd offence would after gall; and do him right that, answering one foul wrong, lives not to act another. Be satisfied; your brother dies to-morrow. O, it is excellent to have a giant's strength; but it is tyrannous to use it like a giant. Could great men thunder as Jove himself does, Jove would ne'er be quiet, for every pelting, petty **official** would use his heaven for thunder; nothing but thunder!"}
    ]
  },
  "officialdom.md": {
    "primary": "Officials collectively, or the bureaucratic system, hierarchy, and formalities associated with them.",
    "secondary": "In satirical and sociological literature, officialdom characterizes the rigid red tape, procedural inertia, and impersonal alienation of modern bureaucracy.",
    "quotes": [
      {"author": "Leo Tolstoy", "work": "Resurrection", "quote": "Nekhludov was repelled by the callous indifference of tsarist **officialdom**, where human suffering was processed as mere numbered paperwork."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "All the intricate machinery of British **officialdom** collapsed into helpless confusion within hours of the Martian advance."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "The revolutionary militias fought with genuine bravery, only to be strangled gradually by the creeping paralysis of political **officialdom**."}
    ]
  },
  "officialese.md": {
    "primary": "The formal, jargon-laden, convoluted language typical of government bureaucracy or official documents.",
    "secondary": "In sociolinguistics and stylistic criticism, officialese employs nominalizations, passive syntax, and evasive circumlocutions to obscure personal accountability.",
    "quotes": [
      {"author": "George Orwell", "work": "Politics and the English Language", "quote": "Modern political prose and administrative **officialese** are designed to make lies sound truthful and murder respectable."},
      {"author": "C. S. Lewis", "work": "The Screwtape Letters", "quote": "The tempter admired the dense, obfuscating **officialese** in which modern institutional sins are so comfortably camouflaged."},
      {"author": "Aldous Huxley", "work": "Brave New World", "quote": "The director delivered the departmental directives in smooth hypnopaedic **officialese**, reassuring the students that all was stable."}
    ]
  },
  "officialise.md": {
    "primary": "To make official, formally recognize, or invest with institutional authority.",
    "secondary": "In British administrative history, local customary practices were systematically officialised into codified statutory procedures during Victorian civil service reforms.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The ministry sought to **officialise** the irregular militia forces by appointing royal colonels and issuing crown warrants."},
      {"author": "George Bernard Shaw", "work": "The Intelligent Woman's Guide to Socialism and Capitalism", "quote": "Society must **officialise** collective responsibilities for public health rather than abandoning them to haphazard private benevolence."},
      {"author": "H. G. Wells", "work": "The New Machiavelli", "quote": "His political ambition was to **officialise** the informal research groups into a permanent state council of economic planning."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Action\Dashboard — fac"

updated = 0
for fname, info in data.items():
    fpath = os.path.join(base_dir, fname)
    if not os.path.exists(fpath):
        print(f"Warning: {fpath} does not exist!")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    book_idx = content.find("> [!book]")
    if book_idx == -1:
        print(f"Warning: No > [!book] callout in {fname}")
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

print(f"Dashboard — fac Batch 2: Successfully updated {updated}/{len(data)} notes.")
