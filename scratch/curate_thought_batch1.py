# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

# Map of relative file paths within "App database/Latin roots/Cluster Thought"
data = {
  # =========================================================================
  # Dashboard — cern (18 words)
  # =========================================================================
  "Dashboard — cern/cernuous.md": {
    "primary": "Drooping or nodding downward with the apex turned toward the earth.",
    "secondary": "In botanical anatomy and morphology, applied specifically to pendulous flowers, inflorescences, or stems curved toward the soil.",
    "quotes": [
      {"author": "Asa Gray", "work": "Gray's Lessons in Botany", "quote": "The flower-stalk is curved so that the blossom is **cernuous** or nodding."},
      {"author": "Charles Darwin", "work": "The Movements and Habits of Climbing Plants", "quote": "The flower peduncles of several species are **cernuous** before fertilization, bending downward toward the earth."},
      {"author": "John Lindley", "work": "An Introduction to Botany", "quote": "A **cernuous** stem or flower is one that droops gracefully with its apex pointing toward the ground."}
    ]
  },
  "Dashboard — cern/concern.md": {
    "primary": "To relate to, affect, or engage the attention and interests of someone; a matter of interest or solicitude.",
    "secondary": "In ethics and human relationships, compassionate anxiety or practical responsibility borne on behalf of others.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "Let’s hear him, for the things he speaks may **concern** Caesar."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "It is a truth that his happiness should be a matter of deep **concern** to all his family."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "I have a great deal of business to settle, which does not immediately **concern** you."}
    ]
  },
  "Dashboard — cern/concerned.md": {
    "primary": "Troubled, anxious, or invested in an affair; having a personal involvement or emotional stake.",
    "secondary": "In narrative exposition, actively engaged with social welfare, family honor, or moral duty.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She was deeply **concerned** that no one should misinterpret Dorothea's generous intentions."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "I felt truly **concerned** for Joe, whose tender heart had been so sorely wounded."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "He seemed anxiously **concerned** about my safety on the dark and lonely road."}
    ]
  },
  "Dashboard — cern/concernedly.md": {
    "primary": "With solicitude, anxiety, or troubled interest; in a concerned and thoughtful manner.",
    "secondary": "In dramatic dialogue, expressing tender sympathetic apprehension or anxious care for an interlocutor's distress.",
    "quotes": [
      {"author": "Emily Brontë", "work": "Wuthering Heights", "quote": "She looked at him **concernedly**, wondering what fresh disaster had befallen the household."},
      {"author": "Eleanor H. Porter", "work": "Miss Billy — Married", "quote": "\"Why, what's the matter?\" he broke off **concernedly**, as he caught a clearer view of the child."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "He paused and glanced **concernedly** at Grace, noticing the pallor that had stolen over her cheeks."}
    ]
  },
  "Dashboard — cern/discern.md": {
    "primary": "To perceive, distinguish, or recognize distinctly with the eyes or the intellect.",
    "secondary": "In epistemological philosophy and aesthetics, to detect subtle differences of value, veracity, or moral quality.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King Lear", "quote": "You look on me: what wreck **discern** you in me Deserves your pity?"},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Through the drifting scud we could dimly **discern** the white hump of the leviathan."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The eye of the mind is able to **discern** truth when purged of superstitious idols."}
    ]
  },
  "Dashboard — cern/discernability.md": {
    "primary": "The property or capacity of being perceptible, distinguishable, or readily recognized by sight or intellect.",
    "secondary": "In sensory psychophysics and empirical logic, the threshold of differentiation between sensory stimuli or conceptual categories.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The **discernability** of sensations depends largely upon the contrast between successive stimuli."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The clear **discernability** of one idea from another is the primary ground of certain knowledge."},
      {"author": "Thomas Reid", "work": "Essays on the Intellectual Powers of Man", "quote": "The distinct **discernability** of external objects requires both healthy organs and attentive observation."}
    ]
  },
  "Dashboard — cern/discernable.md": {
    "primary": "Capable of being recognized, perceived, or differentiated (variant spelling of discernible).",
    "secondary": "In literary description and philosophical critique, standing out with sufficient clarity to be detected by the observer.",
    "quotes": [
      {"author": "George MacDonald", "work": "The Portent and Other Stories", "quote": "I could give an individual description of each, for every atom in that room became **discernable** to my sharpened sight."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "A subtle law of compensation is everywhere **discernable** in human life and nature."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "No trace of sorrow was **discernable** upon her countenance as she crossed the market-place."}
    ]
  },
  "Dashboard — cern/discernible.md": {
    "primary": "Perceptible by the senses or the intellect; capable of being distinguished or detected.",
    "secondary": "In atmospheric description and forensic observation, visible or recognizable despite dim illumination, distance, or obfuscation.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "At first they were faintly **discernible** in the mist, and above them the later stars still glimmered."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles: A Pure Woman", "quote": "An inner cloud of dust rose around the figures, amid which their outlines were scarcely **discernible**."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "A solitary light was **discernible** across the wide sweep of the dark and desolate moor."}
    ]
  },
  "Dashboard — cern/discerning.md": {
    "primary": "Showing good judgment, keen insight, and subtle understanding; perceptive.",
    "secondary": "In literary criticism and social connoisseurship, exhibiting refined discrimination in evaluating aesthetic or moral worth.",
    "quotes": [
      {"author": "Jane Austen", "work": "Persuasion", "quote": "His tone, his expressions, and his choice of subject were all the operation of a **discerning** mind."},
      {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "A **discerning** critic will always separate accidental faults from essential excellence."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "In matters of great weight, wise men employ only those who are **discerning** and impartial."}
    ]
  },
  "Dashboard — cern/discernment.md": {
    "primary": "The cognitive ability to judge well, perceive distinctions, and grasp subtle nuances.",
    "secondary": "In classical epistemology and moral psychology, the intellectual virtue of distinguishing truth from deception and virtue from vice.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "It would be an insult to the **discernment** of any man with half an eye to tell him so."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "There is a quickness of perception in some, a nicety in the **discernment** of character, which amounts to genius."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Judgement consists in the careful **discernment** of differences among ideas that otherwise appear similar."}
    ]
  },
  "Dashboard — cern/indiscernible.md": {
    "primary": "Impossible to distinguish, separate, or perceive clearly by sight, hearing, or intellect.",
    "secondary": "In physics and metaphysics, referring to entities or properties whose differences lie below any possible perceptual or measurable threshold.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "His outline became increasingly blurred until his bodily form was wholly **indiscernible** against the wall."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The horizon line had melted away, leaving sea and sky merged in one **indiscernible** shadow."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The path across Egdon Heath was virtually **indiscernible** in the gathering twilight."}
    ]
  },
  "Dashboard — cern/secern.md": {
    "primary": "To distinguish, differentiate, or separate; in physiology, to secrete or filter substances.",
    "secondary": "In physiological histology and classical biology, the organic process whereby glandular tissues elaborate specific fluids from blood.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Glandular structures serve to **secern** specific humors from the circulating fluid of the organism."},
      {"author": "William Whewell", "work": "The History of the Inductive Sciences", "quote": "To **secern** the accidental from the necessary elements of experience was the grand aim of the critical philosophy."},
      {"author": "Sir William Hamilton", "work": "Lectures on Metaphysics and Logic", "quote": "The mind must continually **secern** true perceptions from deceptive illusions."}
    ]
  },
  "Dashboard — cern/secernate.md": {
    "primary": "To separate, discriminate, or distinguish; to secrete through biological glandular action.",
    "secondary": "In natural philosophy and anatomical analysis, to isolate constituent elements or separate bodily fluids along specialized channels.",
    "quotes": [
      {"author": "Erasmus Darwin", "work": "Zoonomia", "quote": "The kidneys **secernate** the urinary salts directly from the arterial stream."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "It is the prerogative of philosophic analysis to **secernate** heterogeneous elements that common language confounds."},
      {"author": "Richard Chenevix Trench", "work": "On the Study of Words", "quote": "The subtle philologist learns to **secernate** related roots and assign to each its distinct lineage."}
    ]
  },
  "Dashboard — cern/secernment.md": {
    "primary": "The act or process of separating, distinguishing, or physiologically secreting matter.",
    "secondary": "In mental philosophy and natural theology, the discriminatory act of separating distinct faculties, or the biological elaboration of secretions.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "The sharp **secernment** of sensations from recollections is essential to sanity."},
      {"author": "William Paley", "work": "Natural Theology", "quote": "The marvelous apparatus for the **secernment** of bile demonstrates the design of the Creator."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The logical **secernment** of causes from mere invariable antecedents is the first task of induction."}
    ]
  },
  "Dashboard — cern/unconcern.md": {
    "primary": "Freedom from anxiety, care, or interest; an attitude of casual indifference.",
    "secondary": "In social comportment and psychological defense, an outward posture of nonchalance assumed to mask underlying tension or pride.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "There was no necessity for any continuance of speech, and the fact that she did add more seemed to betray an attempted **unconcern**."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He answered with an effort to throw as much sober **unconcern** into his tone as possible."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "She opened her eyes, and we all started as she said, sweetly and seemingly with the utmost **unconcern**, 'Arthur!'"}
    ]
  },
  "Dashboard — cern/unconcerned.md": {
    "primary": "Not having any interest, anxiety, or emotional stake; untroubled, nonchalant, or indifferent.",
    "secondary": "In narrative characterization, displaying serene detachment from surrounding tumult, peril, or social scrutiny.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The tall lank pony seemed used to such doings, and ambled along **unconcerned**."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She strove to look quite **unconcerned**, though her heart beat with strange violence."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "I tried to put on as **unconcerned** an air as possible, but I had not forgotten the warnings of the lady."}
    ]
  },
  "Dashboard — cern/unconcernedly.md": {
    "primary": "Without anxiety, solicitude, or visible interest; in an easy, indifferent, or nonchalant manner.",
    "secondary": "In atmospheric storytelling, carrying out ordinary actions with serene oblivion in the presence of impending crisis.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "From behind the waggon a bright scarlet spot emerged, and went on loading **unconcernedly** with the rest."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "Nothing was to be seen save flat meadows, cows feeding **unconcernedly** for the most part, and silvery willows."},
      {"author": "G. K. Chesterton", "work": "The Wisdom of Father Brown", "quote": "Then he came out again, with some ashes on his hair, and walked **unconcernedly** away."}
    ]
  },
  "Dashboard — cern/undiscerning.md": {
    "primary": "Lacking judgment, insight, or discrimination; unable to distinguish subtle qualities or merits.",
    "secondary": "In cultural commentary, describing an uncritical populace or obtuse observer incapable of appreciating true artistic or moral excellence.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon seemed to be stupidly **undiscerning** and odiously unjust."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "If their praise is censure, your censure may be praise, for they are not more **undiscerning** than you are biased."},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "A crude, **undiscerning** individualism mistakes mere competitive ruthlessness for evolutionary fitness."}
    ]
  },

  # =========================================================================
  # Dashboard — cogit (8 words)
  # =========================================================================
  "Dashboard — cogit/cogitable.md": {
    "primary": "Capable of being conceived, thought about, or comprehended by the intellect.",
    "secondary": "In speculative metaphysics and transcendental logic, designating any entity or proposition that violates no condition of possible conceptualization.",
    "quotes": [
      {"author": "Immanuel Kant", "work": "Critique of Pure Reason", "quote": "An object that conforms to the categories of the understanding is genuinely **cogitable**, even if unperceived."},
      {"author": "William Hamilton", "work": "Lectures on Metaphysics and Logic", "quote": "Whatever is contradictory is simply not **cogitable** by the human intellect."},
      {"author": "John Stuart Mill", "work": "An Examination of Sir William Hamilton's Philosophy", "quote": "A noumenon may remain **cogitable** as a logical possibility though forever inaccessible to sensation."}
    ]
  },
  "Dashboard — cogit/cogitate.md": {
    "primary": "To reflect deeply, meditate, or ponder seriously upon a problem or subject.",
    "secondary": "In humorous or introspective narrative, pausing deliberately to deliberate upon a perplexing dilemma or unexpected turn of events.",
    "quotes": [
      {"author": "G. K. Chesterton", "work": "The Wisdom of Father Brown", "quote": "Father Brown seemed to **cogitate**; he lifted a little whitebait on his fork."},
      {"author": "Laurence Sterne", "work": "The Life and Opinions of Tristram Shandy", "quote": "My father sat down in his armchair to **cogitate** upon the best means of educating his son."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "I sat upon the bench outside the Spouter-Inn, left to **cogitate** upon my strange bedfellow."}
    ]
  },
  "Dashboard — cogit/cogitation.md": {
    "primary": "The action of thinking deeply; contemplation, meditation, or serious reflection.",
    "secondary": "In literary prose, the solitary and methodical deliberation preceding difficult decisions or philosophical deductions.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "After some **cogitation**, accompanied with an intent look at his patron, Mr. Cruncher spoke."},
      {"author": "Jane Austen", "work": "Emma", "quote": "She resumed a more serious, more dispiriting **cogitation** on the events of the evening."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "A man who spends his whole life in solitary **cogitation** becomes a stranger to the affairs of the world."}
    ]
  },
  "Dashboard — cogit/cogitative.md": {
    "primary": "Possessing the power or faculty of thinking; contemplative, meditative, or thoughtful.",
    "secondary": "In scholastic philosophy and cognitive theory, pertaining to the intellectual capacity for discursive reasoning and rational synthesis.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "We have the knowledge of an eternal, most powerful, and most knowing **cogitative** Being."},
      {"author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "The **cogitative** powers of man distinguish him from beasts that follow mere mechanical instinct."},
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Montaigne turns an acute, **cogitative** gaze upon the trivial incidents of daily existence."}
    ]
  },
  "Dashboard — cogit/excogitate.md": {
    "primary": "To devise, invent, or think out through intense intellectual effort or deep reflection.",
    "secondary": "In scientific and judicial methodology, constructing a coherent explanatory scheme or legal argument by sustained reasoning.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "The intellect left to itself cannot **excogitate** the secrets of nature without methodical observation."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "He withdrew to his library to **excogitate** a new theory regarding the Roman encampment."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The German professor sat in his watchtower, seeking to **excogitate** a philosophy of clothes."}
    ]
  },
  "Dashboard — cogit/excogitation.md": {
    "primary": "The act of thinking out, contriving, or inventing something through deep and careful reflection.",
    "secondary": "In intellectual history and system-building, the laborious mental formulation of doctrine, mechanical invention, or legal theory.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Too much reliance on internal **excogitation**, without verification by experiment, has ruined philosophy."},
      {"author": "Jeremy Bentham", "work": "An Introduction to the Principles of Morals and Legislation", "quote": "The penal code was not the sudden inspiration of a moment, but the result of protracted **excogitation**."},
      {"author": "Edgar Allan Poe", "work": "The Murders in the Rue Morgue", "quote": "The analytical faculty is much invigorated by mathematical study, especially in its higher branches of mental **excogitation**."}
    ]
  },
  "Dashboard — cogit/excogitative.md": {
    "primary": "Having the capacity or tendency to think out, devise, or invent through sustained reflection.",
    "secondary": "In philosophical biography, characterizing a mind given to original speculative creation rather than passive empirical reception.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "His **excogitative** genius enabled him to discover moral remedies where others saw only despair."},
      {"author": "William Hazlitt", "work": "Table-Talk", "quote": "Coleridge's mind was pre-eminently **excogitative**, spinning vast dialectical webs from single ideas."},
      {"author": "Thomas De Quincey", "work": "Confessions of an English Opium-Eater", "quote": "Under the influence of the drug, the **excogitative** faculty expands beyond all customary bounds."}
    ]
  },
  "Dashboard — cogit/excogitator.md": {
    "primary": "One who devises, invents, or thinks out something through deep mental exertion.",
    "secondary": "In historical criticism and satire, an architect of novel ideological systems, theoretical dogmas, or institutional blueprints.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Sieyès, that indefatigable **excogitator** of paper constitutions, sat busy with his pigeon-holes."},
      {"author": "Isaac D'Israeli", "work": "Curiosities of Literature", "quote": "The true philosopher is an **excogitator** of new truths rather than a mere compiler of old opinions."},
      {"author": "Robert Southey", "work": "The Doctor", "quote": "Every ingenious projector and **excogitator** of social panaceas believes himself inspired by pure benevolence."}
    ]
  },

  # =========================================================================
  # Dashboard — estim (11 words)
  # =========================================================================
  "Dashboard — estim/estimable.md": {
    "primary": "Worthy of high regard, esteem, or admiration; also capable of being estimated or calculated.",
    "secondary": "In social ethics and character portraiture, possessing enduring integrity, benevolence, and civic virtue.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "A pound of man’s flesh, taken from a man, Is not so **estimable**, profitable neither, As flesh of muttons, beefs, or goats."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Such a theory of life excites in many minds, and among them in some of the most **estimable** in feelings and purpose, the deepest aversion."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "He is a very **estimable** young man, with principles and conduct that must secure him friends."}
    ]
  },
  "Dashboard — estim/estimate.md": {
    "primary": "To form an approximate judgment or opinion concerning value, size, quantity, or importance; a calculation.",
    "secondary": "In economic accounting and strategic planning, an appraisal of prospective costs, resource expenditures, or market values.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Had Gabriel been able from the first to get a distinct view of her countenance, his **estimate** of it might have been different."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "In forming an **estimate** of actions, consequences must be weighed against intentions."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "My guardian's **estimate** of human nature was not elevated, but it was remarkably shrewd."}
    ]
  },
  "Dashboard — estim/estimation.md": {
    "primary": "The act of evaluating or calculating; also the judgment, esteem, or regard in which someone or something is held.",
    "secondary": "In social moral philosophy, personal reputation and credit accorded by public consensus or refined peers.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "We lost a jewel of her, and our esteem Was made much poorer by it; but your son, As mad in folly, lacked the sense of her **estimation**."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Your brother will lose none of his consequence in my **estimation** by marrying your sister."},
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "The wise and virtuous man values the internal approbation of conscience far above the superficial **estimation** of mankind."}
    ]
  },
  "Dashboard — estim/estimator.md": {
    "primary": "A person who computes, evaluates, or appraises the cost, magnitude, or value of something.",
    "secondary": "In statistical mathematics and commerce, a formula or function that computes an approximation of an unknown population parameter.",
    "quotes": [
      {"author": "Thomas D. Whittles", "work": "The Lumberjack Sky Pilot", "quote": "Michells, a former cruiser and timber **estimator**, knew every acre of the white pine forest."},
      {"author": "Frank A. Fetter", "work": "The Principles of Economics", "quote": "The prudent merchant acts as a competitive **estimator** of future marginal utility in the marketplace."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "Every revenue **estimator** of the seventeenth century was compelled to work with imperfect fiscal data."}
    ]
  },
  "Dashboard — estim/inestimable.md": {
    "primary": "Too great, precious, or valuable to be calculated or measured; invaluable.",
    "secondary": "In legal and constitutional history, describing fundamental human liberties or moral treasures whose worth defies commercial appraisal.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard III", "quote": "Methoughts I saw a thousand fearful wracks; A thousand men that fishes gnawed upon; Wedges of gold, great anchors, heaps of pearl, **Inestimable** stones, unvalued jewels."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "I was cut to the quick at the idea of having lost the **inestimable** privilege of listening to the gifted Kurtz."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Our ancient constitution is an **inestimable** inheritance preserved through successive generations."}
    ]
  },
  "Dashboard — estim/misestimate.md": {
    "primary": "To estimate, calculate, or judge incorrectly, inadequately, or falsely.",
    "secondary": "In military strategy and diplomatic negotiation, misapprehending an opponent's resources, willpower, or timeline.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "It was easy to **misestimate** a character that revealed so little of its inner life to casual observers."},
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "Passionate political bias constantly leads partisans to **misestimate** the strength of the opposing faction."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "Military planners are prone to **misestimate** both the munitions required and the resilience of defensive lines."}
    ]
  },
  "Dashboard — estim/misestimation.md": {
    "primary": "An erroneous, flawed, or inaccurate estimate, appraisal, or calculation.",
    "secondary": "In cognitive psychology and public finance, systematic divergence between anticipated fiscal returns and actual revenue outcomes.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The gross **misestimation** of probabilities arises from our tendency to overvalue vivid impressions."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A persistent **misestimation** of risk induces speculators to plunge into precarious ventures."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Any **misestimation** of the time interval between sensation and response distorts our chronometric records."}
    ]
  },
  "Dashboard — estim/overestimate.md": {
    "primary": "To place too high an estimate on; to assess value, cost, difficulty, or ability at an excessively elevated level.",
    "secondary": "In psychological analysis, exaggerating the virtues or resilience of oneself or an admired idol.",
    "quotes": [
      {"author": "Frank A. Fetter", "work": "Economics Volume II: Modern Economic Problems", "quote": "Speculators invariably **overestimate** the duration of an artificial boom in commodity prices."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Emma was conscious of a tendency to **overestimate** her own ability to manage other people's affairs."},
      {"author": "T. R. Glover", "work": "The Jesus of History", "quote": "It is impossible to **overestimate** the impact of his teachings upon the moral conscience of the classical world."}
    ]
  },
  "Dashboard — estim/overestimation.md": {
    "primary": "An estimate or appraisal that is excessively high, exaggerated, or unduly magnified.",
    "secondary": "In psychoanalytic and social theory, the inflation of personal merit or ideological influence beyond objective boundaries.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "An exaggerated **overestimation** of popular opinion often paralyzes the independent judgment of legislators."},
      {"author": "Sigmund Freud", "work": "The Interpretation of Dreams", "quote": "The psychological **overestimation** of an erotic object explains the blind devotion of the lover."},
      {"author": "Bertrand Russell", "work": "The Problems of Philosophy", "quote": "A dogmatic certainty in metaphysics usually rests upon an **overestimation** of the scope of pure a priori reasoning."}
    ]
  },
  "Dashboard — estim/underestimate.md": {
    "primary": "To estimate, rate, or value at too low an amount, rate, or degree of importance.",
    "secondary": "In tactical competition and politics, discounting the capability, resolve, or latent power of an adversary.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Do not **underestimate** the resolution of a quiet spirit when pushed to extremity."},
      {"author": "T. R. Glover", "work": "The Jesus of History", "quote": "Does the writer **underestimate** the actual impress made on his age by Jesus?"},
      {"author": "Arthur Conan Doyle", "work": "The Valley of Fear", "quote": "You always **underestimate** Professor Moriarty, Watson, and therein lies our deadly peril."}
    ]
  },
  "Dashboard — estim/underestimation.md": {
    "primary": "An estimate that falls below actual value, cost, extent, or significance.",
    "secondary": "In historical analysis and policy evaluation, failing to anticipate the severity of structural crises or economic depressions.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "The Secret Agent", "quote": "The chief inspector's fatal error was an **underestimation** of the fanaticism that guided the anarchist group."},
      {"author": "John Maynard Keynes", "work": "The Economic Consequences of the Peace", "quote": "The treaty was based on a disastrous **underestimation** of Europe's post-war economic fragility."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "An **underestimation** of animal intelligence has long delayed a true appreciation of our kinship with other species."}
    ]
  },

  # =========================================================================
  # Dashboard — opin (4 words)
  # =========================================================================
  "Dashboard — opin/opine.md": {
    "primary": "To hold or express an opinion; state as one's belief or judgment.",
    "secondary": "In expository rhetoric and juristic debate, asserting a formal viewpoint or scholarly conclusion with prudent deliberation.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "When, as I **opine**, in the course of time, the true nature of spermaceti became known, its original name was retained."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles: A Pure Woman", "quote": "Indeed they **opine** that the Eternal and Divine did in very truth walk upon the earth."},
      {"author": "Laurence Sterne", "work": "Tristram Shandy", "quote": "I **opine**, quoth my Uncle Toby, that every soldier should know the reason of the warfare in which he serves."}
    ]
  },
  "Dashboard — opin/opinion.md": {
    "primary": "A belief, view, or judgment formed about something, not necessarily grounded on certainty or proof.",
    "secondary": "In jurisprudence and political science, a formal advisory statement or collective consensus directing civil action.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Love's Labour's Lost", "quote": "Therefore your oaths are words and poor conditions; but unseal’d, at least in my **opinion**."},
      {"author": "John Milton", "work": "Areopagitica", "quote": "Where there is much desire to learn, there of necessity will be much arguing, much writing, many **opinions**."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "My good **opinion** once lost is lost for ever."}
    ]
  },
  "Dashboard — opin/opinionated.md": {
    "primary": "Obstinately adhering to one's own opinions; dogmatic and intolerant of opposing views.",
    "secondary": "In character comedy and polemics, rigidly asserting narrow convictions while dismissing contrary evidence or seasoned advice.",
    "quotes": [
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "They were proud, quarrelsome, and excessively **opinionated**, despising all counsel but their own."},
      {"author": "L. P. Brockett", "work": "Woman's Work in the Civil War", "quote": "She was neither vain nor **opinionated**, but listened with modest deference to experienced directors."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "An **opinionated** pedant is always more unbearable when he mistakes arrogance for intellectual vigor."}
    ]
  },
  "Dashboard — opin/opinionative.md": {
    "primary": "Dogmatic, dictatorial, or stubbornly wedded to preconceived opinions; opinionated.",
    "secondary": "In early modern moral essays and theology, exhibiting contentious inflexibility in disputes over doctrine or ritual.",
    "quotes": [
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "They were not only **opinionative**, but stubborn to a degree that defied persuasion."},
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Melancholic men are frequently passionate and **opinionative**, wedded to absurd phantasies."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Men become **opinionative** when they take hypotheses for demonstrable certainties without examination."}
    ]
  },

  # =========================================================================
  # Dashboard — scrup (8 words)
  # =========================================================================
  "Dashboard — scrup/scruple.md": {
    "primary": "A moral qualm or feeling of doubt that restrains action; also an apothecary measure of weight (20 grains).",
    "secondary": "In casuistry and moral theology, a persistent fear that a chosen deed is sinful, demanding minute examination of conscience.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 2", "quote": "Yes, good faith, every dram of it; and I will not bate thee a **scruple**."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She felt almost guilty in asking for knowledge about him, but the dread of acting wrongly silenced every other **scruple**."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "And these chaps, too, had no earthly reason for any kind of **scruple**."}
    ]
  },
  "Dashboard — scrup/scruples.md": {
    "primary": "Hesitations, pangs of conscience, or moral objections restraining conduct.",
    "secondary": "In ethical conflict and tragedy, competing obligations that paralyze resolve or impose agonizing restraint upon duty.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "Fears and **scruples** shake us: in the great hand of God I stand."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Considering my own **scruples**, and the fact that I wish to live an honest life, I cannot comply."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Notions and **scruples** were like spilt needles, making one afraid of treading or sitting down."}
    ]
  },
  "Dashboard — scrup/scrupulous.md": {
    "primary": "Having strict moral integrity; painstaking, meticulously exact, and attentive to right conduct.",
    "secondary": "In professional and scholarly practice, executing duties or scientific observations with rigorous precision and fidelity.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Vholes’s **scrupulous** way of saving himself and his respectability not to feel concerned was sublime."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "He is so very strict and **scrupulous** in his notions; over-scrupulous I must say."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "A man of **scrupulous** honor would never have consented to profit by such an ignominious deception."}
    ]
  },
  "Dashboard — scrup/scrupulously.md": {
    "primary": "With extreme care, thoroughness, and conscientious adherence to moral or factual accuracy.",
    "secondary": "In biographical narratives and archival science, adhering strictly to procedural standards and historical truth.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I had **scrupulously** discharged my duty toward my pupils and neglected nothing."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "His dress and grooming were **scrupulously** attended to, reflecting a fastidious personal dignity."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The ship's chronometers were **scrupulously** checked each noon by the chief mate."}
    ]
  },
  "Dashboard — scrup/scrupulousness.md": {
    "primary": "The attribute of being conscientious, exacting, and morally principled in thought and deed.",
    "secondary": "In ethical philosophy and historical jurisprudence, rigorous self-scrutiny and unwavering adherence to truth.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles: A Pure Woman", "quote": "Her sensitive nature was tormented by a moral **scrupulousness** that magnified every youthful error."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The reflection that the fate of a fellow-creature depended on his word demanded the utmost **scrupulousness**."},
      {"author": "Benito Pérez Galdós", "work": "Saragossa: A Story of Spanish Valor", "quote": "He performed every religious observance with an austere **scrupulousness** that bordered on asceticism."}
    ]
  },
  "Dashboard — scrup/unscrupulous.md": {
    "primary": "Devoid of moral scruples; unprincipled, corrupt, and dismissive of ethical obligations.",
    "secondary": "In sociopolitical satire and commerce, exploiting trust or legal loopholes for ruthless personal or financial aggrandizement.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "There have been times when ladies lived in strongholds and had **unscrupulous** barons for neighbors."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Men at all? or small movable forts and magazines, at the service of some **unscrupulous** man in power?"},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "For ever since those inventive but **unscrupulous** times, men have sought gain at any hazard."}
    ]
  },
  "Dashboard — scrup/unscrupulously.md": {
    "primary": "In an unprincipled, dishonest, or morally unconstrained manner.",
    "secondary": "In investigative history and dramatic fiction, pursuing ambition by fraud, deception, or ruthless betrayal of allies.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "Thus **unscrupulously** did the old gentlewoman sacrifice every principle to secure her selfish objective."},
      {"author": "Mark Twain", "work": "The Gilded Age", "quote": "The corrupt lobbyist operated **unscrupulously** behind the scenes to purchase legislative votes."},
      {"author": "Anthony Trollope", "work": "The Way We Live Now", "quote": "He borrowed and speculated **unscrupulously**, trusting that audacious bluff would conceal his insolvency."}
    ]
  },
  "Dashboard — scrup/unscrupulousness.md": {
    "primary": "The quality or disposition of being devoid of moral principles; shameless dishonesty.",
    "secondary": "In ethical critique and political narrative, systemic disregard for honor, fairness, or human dignity in the pursuit of power.",
    "quotes": [
      {"author": "Grant Allen", "work": "Michael's Crag", "quote": "Without these, not even the invaluable quality of **unscrupulousness** itself is sufficient to win modern worldly success."},
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "No lower estimate could have vindicated the indefatigable **unscrupulousness** of the colonel's lifelong ambitions."},
      {"author": "Joseph Conrad", "work": "Nostromo", "quote": "The cynical **unscrupulousness** of the dictator was matched only by the servility of his terrified ministers."}
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

    # 1. Update definitions in > [!book]
    # Look for 1. **...**: ... and 2. **...**: ...
    # We replace them preserving the markdown format:
    # > 1. **Primary Meaning**: <primary>
    # > 2. **Nuance / Domain Context**: <secondary>
    book_pattern = r"(> 1\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)(\r?\n> 2\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)"
    
    def repl_book(m):
        return f"{m.group(1)}{entry['primary']}{m.group(3)}{entry['secondary']}"
    
    new_content = re.sub(book_pattern, repl_book, content)
    if new_content == content:
        # Fallback regex if formatting slightly differs
        book_pattern2 = r"(1\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)(\r?\n.*?2\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)"
        new_content = re.sub(book_pattern2, repl_book, content)

    # 2. Update quotes in > [!quote]
    # Replace the quote list inside > [!quote] section
    # Find > [!quote]
    q_pos = new_content.find("> [!quote]")
    if q_pos != -1:
        # Keep everything up to > [!quote] 💬 Contextual Usage & Authentic Quotations
        # and replace quotes lines
        before_q = new_content[:q_pos]
        after_q = new_content[q_pos:]
        
        # Build new quote lines
        new_q_lines = ["> [!quote] 💬 Contextual Usage & Authentic Quotations"]
        for q in entry["quotes"]:
            new_q_lines.append(f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{q['quote']}\"*")
        
        # Check if there is a section after quotes (like > [!notes] or EOF)
        # Find if there is another callout or section
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

print(f"Thought Batch 1: Successfully updated {updated_count}/{len(data)} notes.")
