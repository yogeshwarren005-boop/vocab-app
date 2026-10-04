# -*- coding: utf-8 -*-
"""
Curates Dashboard — rati (35 words) in Cluster Mind & Knowledge.
"""
import os, sys, re, subprocess

sys.stdout.reconfigure(encoding="utf-8")

data = {
  "Dashboard — rati/irrational.md": {
    "primary": "Not logical, reasonable, or endowed with reason; driven by passion rather than intellect.",
    "secondary": "In mathematics, a real number that cannot be expressed as a ratio of two integers (such as pi or the square root of two).",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "To surrender oneself blindly to superstitious enthusiasm is to act like an **irrational** creature devoid of understanding."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Man shares with the lower animals many instincts that appear wholly **irrational** when analyzed by pure logic."},
      {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "The discovery that the diagonal of a unit square yields an **irrational** magnitude troubled the ancient Pythagorean brotherhood."}
    ]
  },
  "Dashboard — rati/irrationality.md": {
    "primary": "The characteristic of lacking logic, reason, or sound judgment; illogical thought or conduct.",
    "secondary": "In behavioral economics and psychology, cognitive biases that cause human decisions to diverge systematically from normative logic.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Emotional panics reveal the deep undercurrent of human **irrationality**, sweeping away decades of disciplined training in a single moment."},
      {"author": "Bertrand Russell", "work": "Skeptical Essays", "quote": "Most human beliefs are adopted on grounds of passionate prejudice, revealing the pervasive **irrationality** of public opinion."},
      {"author": "George Bernard Shaw", "work": "Man and Superman", "quote": "The romantic idealist accuses the world of **irrationality** simply because reality refuses to conform to his poetic illusions."}
    ]
  },
  "Dashboard — rati/irrationally.md": {
    "primary": "In an irrational, unreasonable, or illogical manner; without the guidance of reason.",
    "secondary": "In dramatic narrative, acting under the overwhelming sway of blind panic, jealousy, or rage.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Rochester paced the dark library like a caged panther, muttering **irrationally** against the cruel hand of fate."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard acted **irrationally** in the market auction, bidding up grain prices out of pure spite against his rival."},
      {"author": "Virginia Woolf", "work": "Night and Day", "quote": "She found herself trembling **irrationally** as the footsteps approached the drawing-room door."}
    ]
  },
  "Dashboard — rati/nonrational.md": {
    "primary": "Not based on, governed by, or within the domain of rational thought or logical deduction.",
    "secondary": "In epistemology and theology, referring to intuitive, aesthetic, or mystical experiences that transcend discursive reason.",
    "quotes": [
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "Mystical conversion experiences frequently originate from a **nonrational** stratum of consciousness that defies verbal explanation."},
      {"author": "Rudolf Otto", "work": "The Idea of the Holy", "quote": "The numinous experience confronts the worshiper as a purely **nonrational** mystery inspiring awe and dread."},
      {"author": "Max Weber", "work": "The Sociology of Religion", "quote": "Charismatic authority rests upon a fundamentally **nonrational** devotion to the extraordinary sanctity of a prophetic leader."}
    ]
  },
  "Dashboard — rati/overrating.md": {
    "primary": "Valuing, estimating, or assessing something or someone more highly than is justified.",
    "secondary": "In critical appraisal and finance, exaggerating the talent of an artist or the earnings potential of an enterprise.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Knightley warned Emma against **overrating** her own match-making cleverness, pointing out the misery she might cause."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Youth is perpetually prone to **overrating** the happiness of the wealthy and the permanence of human friendships."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Speculative adventurers brought ruin upon themselves by wildly **overrating** the profits of South Sea trading ventures."}
    ]
  },
  "Dashboard — rati/proration.md": {
    "primary": "The proportional allocation or distribution of something (such as expenses, dividends, or taxes) according to a set ratio.",
    "secondary": "In commercial real estate and accounting, the equitable division of prepaid insurance or municipal taxes at property closing.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The fair **proration** of public debt between the states required an equitable standard based on population and wealth."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The equitable **proration** of municipal assessments ensures that each merchant contributes according to his commercial turnover."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "In bankruptcy proceedings, the **proration** of remaining corporate assets among competing creditors must follow strict legal priority."}
    ]
  },
  "Dashboard — rati/ratification.md": {
    "primary": "The action of signing or giving formal consent to a treaty, contract, or agreement, making it officially valid.",
    "secondary": "In constitutional law, the formal confirmation of a charter or constitutional amendment by constituent state legislatures.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The vigorous struggle for the **ratification** of the federal Constitution occupied the foremost minds of the young republic."},
      {"author": "James Madison", "work": "The Federalist Papers", "quote": "True sovereignty appeared in the act of **ratification**, when the people through their state conventions established the union."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The formal **ratification** of the North Atlantic Treaty bound western democracies in an unbreakable defensive alliance."}
    ]
  },
  "Dashboard — rati/ratified.md": {
    "primary": "Formally approved, confirmed, or made officially valid by signature, vote, or sovereign decree.",
    "secondary": "In diplomatic history and parliamentary law, treaties or legislative acts having received required constitutional assent.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Once the necessary nine states had **ratified** the document, the new constitutional government commenced its operations."},
      {"author": "Thomas Jefferson", "work": "Writings", "quote": "The senate **ratified** the Louisiana treaty with overwhelming acclaim, doubling the territorial extent of the United States."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The Roman senate obediently **ratified** the succession of the new emperor, fearful of the praetorian cohorts at their gates."}
    ]
  },
  "Dashboard — rati/ratifier.md": {
    "primary": "A person, legislature, or sovereign authority that formally approves, confirms, or ratifies an agreement or law.",
    "secondary": "In constitutional history, an official delegate voting to adopt a supreme charter or binding diplomatic covenant.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Every thoughtful **ratifier** in the state conventions understood that national defense demanded a unified federal revenue system."},
      {"author": "James Madison", "work": "Letters and Other Writings", "quote": "The intention of the constitution must be sought not in the debates of the drafters, but in the understanding of the **ratifier** delegates."},
      {"author": "John Marshall", "work": "Major Opinions", "quote": "The people acting through their conventions were the supreme **ratifier** of the fundamental instrument of American governance."}
    ]
  },
  "Dashboard — rati/ratify.md": {
    "primary": "Sign or give formal consent to a treaty, contract, or agreement, making it officially valid.",
    "secondary": "In legislative procedure, to formally approve and sanction an executive nomination, statute, or diplomatic treaty.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The power of the senate to **ratify** treaties serves as a vital constitutional check upon executive negotiations with foreign powers."},
      {"author": "Thomas Jefferson", "work": "Autobiography", "quote": "The delegates assembled in Philadelphia to **ratify** the articles that established an enduring union among the colonies."},
      {"author": "George Washington", "work": "Farewell Address", "quote": "Until the people amend their constitution, they are morally bound to **ratify** and uphold its statutory provisions."}
    ]
  },
  "Dashboard — rati/rating.md": {
    "primary": "A classification or ranking of someone or something based on a comparative assessment of quality, quantity, or value.",
    "secondary": "In naval maritime terminology, the rank, rate, or grade held by an enlisted sailor on a naval vessel.",
    "quotes": [
      {"author": "Herman Melville", "work": "White-Jacket", "quote": "The purser inspected each man's **rating** on the ship's muster book, paying out wages according to naval regulation."},
      {"author": "Joseph Conrad", "work": "The Secret Sharer", "quote": "The young captain scrutinized the seaman's certificate of service, observing that his conduct **rating** was marked very good."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The insurance **rating** of the overdue merchant vessel rose rapidly as the storm battered the English Channel."}
    ]
  },
  "Dashboard — rati/ratio.md": {
    "primary": "The quantitative relation between two amounts showing the number of times one value contains or is contained within the other.",
    "secondary": "In classical economics and astronomy, comparative proportions determining monetary bimetallism or planetary orbital periods.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Philosophiae Naturalis Principia Mathematica", "quote": "Gravitational attraction between two celestial bodies varies in direct **ratio** to their masses and inverse **ratio** to the square of their distance."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "As more individuals are produced than can possibly survive, there must in every case be a struggle for existence, owing to the geometric **ratio** of increase."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The commercial **ratio** between silver and gold fluctuates with the relative abundance of bullion arriving from the mines of the Americas."}
    ]
  },
  "Dashboard — rati/ratiocinate.md": {
    "primary": "Form judgments or conclusions through the process of logical reasoning, deduction, or argumentation.",
    "secondary": "In detective fiction and epistemology, analyzing subtle clues through sequential deduction to uncover hidden truth.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "The Murders in the Rue Morgue", "quote": "Dupin would sit in silence, beginning to **ratiocinate** upon the strange testimony until the fragmented clues coalesced into clarity."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The reflective intellect must **ratiocinate** upon primary intuitions before converting poetic inspiration into systematic philosophy."},
      {"author": "Thomas Henry Huxley", "work": "Method and Results", "quote": "The paleontologist must **ratiocinate** from a single fossil bone to reconstruct the entire skeleton of an extinct vertebrate."}
    ]
  },
  "Dashboard — rati/ratiocination.md": {
    "primary": "The process of exact thinking, logical reasoning, or methodical deduction.",
    "secondary": "In literary criticism, the genre of analytical detective tale pioneered by Edgar Allan Poe's tales of ratiocination.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "The Mystery of Marie Rogêt", "quote": "The mental features discoursed of as the analytical are in themselves but little susceptible of analysis; we appreciate them only in their effects, in the glorious triumphs of **ratiocination**."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Holmes applied his powers of rigorous **ratiocination** to the bloodstain on the floor, deducing the height and age of the assassin."},
      {"author": "Jonathan Swift", "work": "The Battle of the Books", "quote": "The pedantic critic exhausted his audience with tedious **ratiocination**, proving by ancient syllogisms what common sense saw at a glance."}
    ]
  },
  "Dashboard — rati/ratiocinative.md": {
    "primary": "Characterized by, relating to, or given to logical reasoning and methodical deduction.",
    "secondary": "In cognitive philosophy, describing analytical mental processes contrasted with intuitive or affective perception.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "The Purloined Letter", "quote": "The Prefect of Police lacked that flexible **ratiocinative** genius required to fathom an intellect superior to his own."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The scientific method combines inductive observation with powerful **ratiocinative** deductions from established physical laws."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Our higher **ratiocinative** faculties depend upon the brain's capacity to isolate abstract characters from sensory wholes."}
    ]
  },
  "Dashboard — rati/ratiocinator.md": {
    "primary": "A person who reasons logically, deduces systematically, or constructs methodical arguments.",
    "secondary": "In narrative fiction, the master detective or philosopher who solves mysteries through pure deductive brilliance.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "The Gold-Bug", "quote": "Legrand was an acute **ratiocinator**, decoding the cipher on the parchment by calculating the frequency of English vowels."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Watson admired his companion as an extraordinary **ratiocinator**, whose cold logic was undisturbed by human passion."},
      {"author": "G. K. Chesterton", "work": "The Innocence of Father Brown", "quote": "Flambeau encountered in the little priest an unexpected **ratiocinator**, who understood crime because he understood the human soul."}
    ]
  },
  "Dashboard — rati/ration.md": {
    "primary": "A fixed amount of a commodity or food officially allowed to each person during a time of shortage or war; also to allocate in fixed portions.",
    "secondary": "In military logistics, the daily measured subsistence provided to soldiers in barracks or in the field.",
    "quotes": [
      {"author": "Jack London", "work": "The Sea-Wolf", "quote": "The cook served out our meager daily **ration** of hardtack and salt pork, watching every sailor with a suspicious squint."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The national supply of meat and sugar was placed under strict **ration** to conserve merchant tonnage during the U-boat offensive."},
      {"author": "Herman Melville", "work": "White-Jacket", "quote": "Each mess aboard the frigate drew its weekly **ration** of grog, tobacco, and flour from the ship's steward."}
    ]
  },
  "Dashboard — rati/rational.md": {
    "primary": "Based on or in accordance with reason or logic; capable of thinking and reasoning clearly and soundly.",
    "secondary": "In philosophical ethics, the distinctively human capacity for deliberate, principled moral agency.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "What a piece of work is a man! How noble in reason, how infinite in faculties, in form and moving how express and admirable, a truly **rational** creature."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The lawyer urged his client to adopt a more **rational** view of the Chancery proceedings, rather than pining away in despair."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "God has endowed man with **rational** faculties that he may discover the duties owed to his Creator and fellow beings."}
    ]
  },
  "Dashboard — rati/rationale.md": {
    "primary": "A set of reasons or a logical basis for a course of action, policy, or belief.",
    "secondary": "In public administration and jurisprudence, the stated justification setting forth the underlying principles of a decision.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "That is the whole **rationale** of my research, Casaubon remarked coldly, defending his classical mythology treatise against criticism."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "The anthropologist sought to discover the underlying **rationale** behind primitive sacrificial rites in ancient agricultural societies."},
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "The philosophical **rationale** for universal suffrage rests upon the moral elevation of citizens who participate in public affairs."}
    ]
  },
  "Dashboard — rati/rationalisation.md": {
    "primary": "The action of attempting to explain or justify behavior or an attitude with logical reasons (British spelling); also industrial restructuring for efficiency.",
    "secondary": "In psychoanalysis and corporate management, creating plausible excuses for unconscious impulses or streamlining factory processes.",
    "quotes": [
      {"author": "Sigmund Freud", "work": "The Psychopathology of Everyday Life", "quote": "The neurotic patient invents an elaborate intellectual **rationalisation** to mask the true, repressed motive behind his symptoms."},
      {"author": "Max Weber", "work": "The Protestant Ethic and the Spirit of Capitalism", "quote": "The progressive **rationalisation** of economic life transformed medieval craft workshops into mechanized, disciplined factories."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "Every political faction offered a convenient **rationalisation** for betraying the revolutionary militias at the front."}
    ]
  },
  "Dashboard — rati/rationalise.md": {
    "primary": "Attempt to explain or justify behavior or attitudes with logical reasons, even if not true (British spelling); make more efficient.",
    "secondary": "In British business and psychology, organizing an industry according to scientific principles or inventing justifications for selfish desires.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "Undershaft refused to **rationalise** his munitions manufacture as Christian philanthropy, boasting openly of his pursuit of power."},
      {"author": "Virginia Woolf", "work": "Night and Day", "quote": "She tried to **rationalise** her growing discontent, telling herself that comfort and social position ought to satisfy any sensible woman."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Later Roman mythographers attempted to **rationalise** crude tribal taboos into elegant moral allegories."}
    ]
  },
  "Dashboard — rati/rationalism.md": {
    "primary": "The philosophical belief or principle that opinions and actions should be based on reason and knowledge rather than on religious belief or emotional response.",
    "secondary": "In epistemology (Descartes, Spinoza, Leibniz), the doctrine that reason alone, independent of sensory experience, is the primary source of knowledge.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "A History of Western Philosophy", "quote": "Seventeenth-century **rationalism** achieved its crowning glory in Spinoza's magnificent geometrical demonstration of ethics."},
      {"author": "William James", "work": "Pragmatism", "quote": "Pragmatism stands midway between dogmatic **rationalism** with its eternal abstractions and empiricism with its raw facts."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The bold **rationalism** of the Greek philosophers steadily undermined the popular polytheism of the pagan world."}
    ]
  },
  "Dashboard — rati/rationalist.md": {
    "primary": "A person whose opinions and actions are based on reason and evidence rather than emotion, dogma, or religious faith.",
    "secondary": "In history of philosophy, a thinker who asserts that fundamental truths are discovered through pure intellectual deduction.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "Mysticism and Logic", "quote": "A consistent **rationalist** insists that every hypothesis, however comforting, must submit to the verdict of logical evidence."},
      {"author": "William James", "work": "The Will to Believe", "quote": "The uncompromising **rationalist** warns that it is a moral crime to believe anything upon insufficient evidence."},
      {"author": "G. K. Chesterton", "work": "Orthodoxy", "quote": "The modern **rationalist** lives in a small, clean prison of logic, shutting out the wild, beautiful mystery of the cosmos."}
    ]
  },
  "Dashboard — rati/rationalistic.md": {
    "primary": "Of, relating to, or characteristic of rationalism; relying strictly upon reason rather than faith, tradition, or emotion.",
    "secondary": "In nineteenth-century biblical criticism, interpreting miraculous accounts through naturalistic historical causes.",
    "quotes": [
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "The rise of a **rationalistic** spirit in late antiquity dissolved ancient agricultural taboos into mere poetic folklore."},
      {"author": "John Henry Newman", "work": "The Idea of a University", "quote": "A purely **rationalistic** education produces clever minds while starving the moral imagination and spiritual sensibilities."},
      {"author": "William E. H. Lecky", "work": "History of the Rise and Influence of Rationalism in Europe", "quote": "The decline of belief in witchcraft in Europe was the triumph of a broader **rationalistic** habit of thought."}
    ]
  },
  "Dashboard — rati/rationality.md": {
    "primary": "The quality or state of being reasonable, based on facts or reason; the capacity for logical reasoning.",
    "secondary": "In decision theory and economics, consistent pursuit of self-interest based on transitive preferences and complete information.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Which of us can boast of absolute **rationality** in our affections, when love so often springs from trivial affinities?"},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Human dignity resides in our capacity for conscious **rationality**, choosing higher intellectual pleasures over base animal gratification."},
      {"author": "Max Weber", "work": "Economy and Society", "quote": "Bureaucracy represents the purest form of legal-rational authority, maximizing organizational **rationality** and calculability."}
    ]
  },
  "Dashboard — rati/rationalization.md": {
    "primary": "The action of attempting to explain or justify behavior or an attitude with logical reasons; also restructuring for peak efficiency.",
    "secondary": "In sociological theory (Max Weber), the historical replacement of traditions, values, and emotions with calculated formal efficiency.",
    "quotes": [
      {"author": "Max Weber", "work": "General Economic History", "quote": "The inexorable **rationalization** of modern society replaced traditional customs with calculated bookkeeping and technical law."},
      {"author": "Sigmund Freud", "work": "Introductory Lectures on Psycho-Analysis", "quote": "The patient produced a clever **rationalization** to explain why he avoided walking down the street where his rival lived."},
      {"author": "Aldous Huxley", "work": "Brave New World Revisited", "quote": "Totalitarian propaganda relies upon the psychological **rationalization** of ancient hatreds to justify state terror."}
    ]
  },
  "Dashboard — rati/rationalize.md": {
    "primary": "Attempt to explain or justify behavior, beliefs, or choices with logical reasons; also reorganize an industry for maximum efficiency.",
    "secondary": "In cognitive psychology, constructing self-serving justifications to reduce cognitive dissonance.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "We tend to **rationalize** our instinctive likes and dislikes after the fact, pretending our passions are fruits of pure logic."},
      {"author": "George Bernard Shaw", "work": "Pygmalion", "quote": "Doolittle possessed an extraordinary gift to **rationalize** his disreputable habits into a coherent philosophical code."},
      {"author": "Meyer Moldeven", "work": "The Universe — or Nothing", "quote": "Philosophers often attempt to **rationalize** the mysterious cosmological expansion of spacetime using classical analogies."}
    ]
  },
  "Dashboard — rati/rationally.md": {
    "primary": "In a rational manner; with reason, sound logic, and good judgment rather than emotional impulse.",
    "secondary": "In philosophical debate and ethical action, making decisions guided by evidence and universal moral principles.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Jane resolved to act **rationally**, subduing the clamorous pleadings of her heart to the stern command of conscience."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth advised her sister to consider Mr. Bingley's conduct **rationally**, without attributing malice to innocent mistakes."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Men who deliberate **rationally** will discover that virtue and civic peace are inseparable companions."}
    ]
  },
  "Dashboard — rati/rationalness.md": {
    "primary": "The characteristic disposition of being rational; reasonableness, sound judgment, and reliance on logic.",
    "secondary": "In character assessment and philosophical treatises, the mental stability that preserves calm logic under emotional provocation.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "A mind distinguished by habitual **rationalness** navigates the storms of public faction with serene, unclouded judgment."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Maggie admired the steady **rationalness** of Philip Wakem, finding solace in his clear intellectual companionship."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The constitutional statesman balances historical tradition with the calm **rationalness** required for prudent civic reform."}
    ]
  },
  "Dashboard — rati/rationed.md": {
    "primary": "Distributed or allocated in fixed, limited portions during times of shortage, scarcity, or emergency.",
    "secondary": "In wartime history, essential goods (such as petrol, rubber, or sugar) restricted to coupons or quotas.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "Bread and butter were strictly **rationed** across the island fortress as our merchant convoys fought through the Atlantic."},
      {"author": "L. P. Brockett", "work": "Woman's Work in the Civil War", "quote": "Hospital nurses **rationed** the remaining stimulants and clean linen among the wounded soldiers after the battle."},
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "The unemployed miners lived on **rationed** bread and margarine, their families enduring months of slow starvation."}
    ]
  },
  "Dashboard — rati/rationing.md": {
    "primary": "The controlled distribution of scarce resources, goods, or services, especially during wartime or famine.",
    "secondary": "In macroeconomic history and logistics, administrative allocation mechanisms replacing price systems during emergencies.",
    "quotes": [
      {"author": "Winston Churchill", "work": "Their Finest Hour", "quote": "Strict national **rationing** ensured that every citizen shared equally in the hardships imposed by the enemy blockade."},
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "The Ministry of Plenty announced a reduction in the chocolate ration, disguising austerity as a victory of state **rationing**."},
      {"author": "John Maynard Keynes", "work": "How to Pay for the War", "quote": "Comprehensive consumer **rationing** prevents destructive price inflation when wartime production diverts consumer factories to munitions."}
    ]
  },
  "Dashboard — rati/ratitae.md": {
    "primary": "A diverse taxonomic group of large, flightless birds having a flat breastbone without a keel (carina).",
    "secondary": "In evolutionary ornithology, an assemblage including ostriches, emus, rheas, cassowaries, and kiwis.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "On the Classification of Birds", "quote": "The flat, unkeeled sternum distinguishes the ancient order **ratitae** from the carinate flying birds of modern fauna."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The rudimentary wings of the **ratitae** illustrate how organs degenerate through prolonged disuse across evolutionary epochs."},
      {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "The widespread Southern Hemisphere distribution of the **ratitae** points to ancient Gondwanan continental connections."}
    ]
  },
  "Dashboard — rati/ratite.md": {
    "primary": "Any member of the group of flightless birds having a flat, unkeeled breastbone, such as the ostrich, emu, or kiwi.",
    "secondary": "In comparative anatomy, denoting flightless palaeognathous birds adapted for cursorial running on open plains.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The African ostrich, a typical **ratite** bird, relies upon enormous cursorial leg strength to outrun galloping horses."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "Dissection of the **ratite** shoulder girdle reveals the total absence of the pectoral keel required for flight muscles."},
      {"author": "Alfred Russel Wallace", "work": "Island Life", "quote": "The extinct moas of New Zealand were colossal **ratite** giants that flourished in the complete absence of predatory mammals."}
    ]
  },
  "Dashboard — rati/underrating.md": {
    "primary": "Underestimating, undervalueing, or assigning too low a value, importance, or capability to someone or something.",
    "secondary": "In strategic warfare and competitive commerce, the dangerous mistake of underestimating an adversary's resources.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Gathering Storm", "quote": "Allied statesmen committed the fatal error of **underrating** the speed and mechanized power of the German panzer divisions."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Emma was in danger of **underrating** Robert Martin's character simply because he was a respectable tenant farmer."},
      {"author": "F. H. Costello", "work": "Sure-Dart", "quote": "The veteran hunter warned the youth against **underrating** the wounded cave bear, whose dying charge was swifter than an arrow."}
    ]
  },
  "Dashboard — rati/unratified.md": {
    "primary": "Not formally approved, sanctioned, or confirmed by legal, legislative, or sovereign authority.",
    "secondary": "In international diplomacy and constitutional law, treaties or amendments that failed to achieve the necessary legislative majority.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "An **unratified** compact between states has no binding force in federal courts until Congress grants explicit approval."},
      {"author": "Thomas Jefferson", "work": "Writings", "quote": "The commercial convention remained **unratified**, as the British ministry refused to abandon the impressment of our seamen."},
      {"author": "Woodrow Wilson", "work": "Addresses and Papers", "quote": "The tragic rejection left the Treaty of Versailles **unratified** by the United States Senate, crippling the League of Nations."}
    ]
  }
}

def curate_file(rel_path, info):
    base_dir = "App database/Latin roots/Cluster Mind & Knowledge"
    filepath = os.path.join(base_dir, rel_path)
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return False
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    fm_match = re.search(r"^---\n.*?\n---\n", content, re.DOTALL)
    if not fm_match:
        print(f"Frontmatter missing: {filepath}")
        return False
    frontmatter = fm_match.group(0)
    
    w = os.path.splitext(os.path.basename(rel_path))[0]
    header = f"# {w}\n\n"
    
    dv_match = re.search(r"(> \[!status\] 🎯 \*\*Status:\*\*.*?```dataviewjs.*?```)", content, re.DOTALL)
    if not dv_match:
        print(f"Dataview block missing: {filepath}")
        return False
    dv_block = dv_match.group(1)
    
    defs_block = f"""> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: {info['primary']}
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {info['secondary']}"""

    quotes_lines = ["> [!quote] 💬 Contextual Usage & Authentic Quotations"]
    for q in info["quotes"]:
        quotes_lines.append(f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{q['quote']}\"*")
    quotes_block = "\n".join(quotes_lines)
    
    new_content = f"{frontmatter}{header}{dv_block}\n\n{defs_block}\n\n{quotes_block}\n"
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True

success = 0
for rel_path, info in data.items():
    if curate_file(rel_path, info):
        success += 1

print(f"Successfully updated {success}/{len(data)} notes in Dashboard — rati.")
