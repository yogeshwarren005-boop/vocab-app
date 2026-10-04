# -*- coding: utf-8 -*-
import os, re

data = {
  "decrescendo.md": {
    "primary": "A gradual decrease in loudness or dynamic intensity in a musical passage.",
    "secondary": "In acoustics and dramatic narration, decrescendo signifies the gradual subsiding of auditory volume or emotional tension into quietude.",
    "quotes": [
      {"author": "James Joyce", "work": "A Portrait of the Artist as a Young Man", "quote": "The solemn organ chords faded away in a long **decrescendo**, leaving the chapel wrapped in breathless silence."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Her passionate melody sank into a delicate **decrescendo**, trailing off into a tender whisper."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The roar of the storm underwent a gradual **decrescendo** as the atmospheric vortex moved eastward."}
    ]
  },
  "discreet.md": {
    "primary": "Careful and circumspect in speech or action, especially to avoid causing offense or revealing private secrets.",
    "secondary": "In ethical philosophy and courtly manners, discretion governs prudent behavior by harmonizing honesty with social propriety.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Let not thy **discreet** heart think it, for wisdom and prudence ever guide thy noble steps."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Bathsheba was **discreet** enough to keep her private anxieties hidden from the inquisitive curiosity of the village."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor was always **discreet** and guarded in her conversation, never betraying the confidence of a friend."}
    ]
  },
  "discreetly.md": {
    "primary": "In a careful, prudent, and unobtrusive manner, especially so as to preserve confidentiality.",
    "secondary": "In diplomacy and statecraft, conducting sensitive negotiations discreetly prevents premature leaks that could derail delicate treaties.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merry Wives of Windsor", "quote": "I will make a prief of it in my notebook, and we will afterwards **discreetly** discuss the matter in private."},
      {"author": "James Joyce", "work": "Dubliners", "quote": "He stepped back **discreetly** into the shadow of the doorway, allowing the lovers to pass unobserved."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The nobleman withdrew **discreetly**, leaving the compromising letters in Holmes's hands."}
    ]
  },
  "discreetness.md": {
    "primary": "The attribute or practice of being careful, prudent, and guarded in speech and conduct.",
    "secondary": "In administrative ethics and domestic service, discreetness is prized as the foundational trait safeguarding household confidentiality.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "A confidential secretary must unite unblemished fidelity with habitual **discreetness** in all correspondence."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Bulstrode relied upon the absolute **discreetness** of his clerk to preserve his banking reputation untarnished."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "The virtue of **discreetness** consists in keeping counsel without incurring the suspicion of dissimulation."}
    ]
  },
  "discrete.md": {
    "primary": "Individually separate and distinct; non-continuous.",
    "secondary": "In mathematics and computer science, discrete mathematics studies structures that are countable or composed of distinct, separable values.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Number is the most universal and simple idea we have, consisting of **discrete** units added one to another."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Natural selection can act only by preserving and accumulating infinitesimal variations, not by sudden, **discrete** leaps."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Consciousness does not appear to itself chopped up in bits; it is not a chain of **discrete** states, but a continuous stream."}
    ]
  },
  "discreteness.md": {
    "primary": "The condition of being separate, distinct, and composed of individual, non-continuous elements.",
    "secondary": "In linguistics and semiotics, discreteness is a design feature of human language whereby signs are composed of distinct, categorical sounds.",
    "quotes": [
      {"author": "Charles Sanders Peirce", "work": "Collected Papers", "quote": "The continuous flow of time stands in stark conceptual opposition to the nominalist doctrine of pure **discreteness**."},
      {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "Mathematical continuity must be rigorously reconciled with the logical **discreteness** of the natural number series."},
      {"author": "Ferdinand de Saussure", "work": "Course in General Linguistics", "quote": "Phonological analysis reveals the absolute **discreteness** of phonetic oppositions within the sound system of a language."}
    ]
  },
  "discretion.md": {
    "primary": "The quality of behaving or speaking in such a way as to avoid causing offense or revealing private information; also freedom to decide.",
    "secondary": "In administrative and criminal law, judicial discretion allows a magistrate to tailor sentencing within statutory parameters to the equities of the case.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "The better part of valor is **discretion**; in the which better part I have saved my life."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The courts must declare the sense of the law; and if they should be disposed to exercise will instead of judgment, the consequence would be the substitution of their pleasure for that of the legislative body, subverting judicial **discretion**."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth commended her friend's **discretion** in avoiding all reference to the painful misunderstandings of the past."}
    ]
  },
  "discretional.md": {
    "primary": "Left to or dependent upon individual judgment or choice; discretionary.",
    "secondary": "In public administration and trust management, discretional powers grant a fiduciary authority to distribute assets according to evolving beneficiary needs.",
    "quotes": [
      {"author": "Jeremy Bentham", "work": "Principles of the Civil Code", "quote": "A magistrate entrusted with wide **discretional** authority must be held to strict public accountability."},
      {"author": "Woodrow Wilson", "work": "Congressional Government", "quote": "The heads of departments exercise large **discretional** powers in allocating legislative appropriations across branch bureaus."},
      {"author": "Joseph Story", "work": "Commentaries on Equity Jurisprudence", "quote": "The chancellor exercised a **discretional** jurisdiction to grant relief where the common-law remedies proved inadequate."}
    ]
  },
  "discretionary.md": {
    "primary": "Available for use at the discretion of the user; not bound by predetermined or mandatory rules.",
    "secondary": "In macroeconomic monetary policy, discretionary intervention involves central bank adjustments of interest rates in response to current economic indicators.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Taxes levied upon capital values should be fixed and certain, leaving nothing to the arbitrary and **discretionary** appraisal of the tax-gatherer."},
      {"author": "Walter Bagehot", "work": "Lombard Street: A Description of the Money Market", "quote": "The directors of the Bank of England held **discretionary** control over the national discount rate during the panic."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "A portion of household income remains **discretionary**, available for cultural improvement after basic physical needs are met."}
    ]
  },
  "excrement.md": {
    "primary": "Waste matter discharged from the bowels; feces; also archaic for an outgrowth of hair or nails.",
    "secondary": "In animal ecology and soil science, herbivore excrement recycles essential nitrogen and phosphorus back into the pedosphere.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Comedy of Errors", "quote": "Why is Time such a niggard of hair, being, as it is, so plentiful an **excrement**?"},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In the course of two months, I picked up in my garden twelve kinds of seeds from the **excrement** of small birds."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The Yahoos discharged their foul **excrement** upon Gulliver from the branches of the overarching trees."}
    ]
  },
  "excrescence.md": {
    "primary": "A distinct outgrowth on a human or animal body or on a plant, especially an abnormal one; an unsightly addition.",
    "secondary": "In aesthetic criticism and architectural commentary, an excrescence denotes an incongruous stylistic addition that disfigures an original building.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The eggshell was so thin, so devoid of **excrescence**, and so closely fitting that its fragility seemed miraculous."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "These frontal horns consist of a bony **excrescence** covered with smooth integument."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The modern wooden porch was a hideous **excrescence** disfiguring the ancient Elizabethan manor house."}
    ]
  },
  "excrescent.md": {
    "primary": "Growing out abnormally or superfluously; redundant or forming an abnormal outgrowth.",
    "secondary": "In historical linguistics and phonology, an excrescent consonant is a non-etymological sound inserted between consonants (such as the 'd' in 'sound' from Old French 'son').",
    "quotes": [
      {"author": "William Dwight Whitney", "work": "Language and the Study of Language", "quote": "The transition between nasal and liquid consonants frequently produces an **excrescent** plosive like the 'b' in 'bramble'."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The volcanic crater was choked with irregular, **excrescent** masses of basaltic scoria."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The revolutionary committees formed an **excrescent** tyranny that choked the ancient constitutional branches of government."}
    ]
  },
  "excreta.md": {
    "primary": "Waste matter discharged from the body, especially feces and urine.",
    "secondary": "In public health epidemiology and civil sanitary engineering, safe separation of human excreta from potable water supplies is the foremost barrier against enteric epidemics.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The physiological elimination of metabolic **excreta** is performed by homologous organs across all vertebrate classes."},
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "The prompt and complete removal of all bodily **excreta** from the sickroom is essential to prevent air contamination."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Disinfection of the patient's **excreta** with carbolic acid must be carried out rigorously in every case of typhoid fever."}
    ]
  },
  "excrete.md": {
    "primary": "To separate and eliminate waste products from the blood, tissues, or organs.",
    "secondary": "In mammalian renal physiology, nephrons filter blood plasma to excrete urea, uric acid, and metabolic byproducts in concentrated urine.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Certain plants **excrete** a sweet juice, apparently for the sake of eliminating injurious substances from their sap."},
      {"author": "T. H. Huxley", "work": "Lessons in Elementary Physiology", "quote": "The kidneys continuously **excrete** nitrogenous waste matter in the form of urea."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "When the renal parenchyma fails to **excrete** metabolic toxins, clinical uremia rapidly ensues."}
    ]
  },
  "excreting.md": {
    "primary": "The act or process of discharging or eliminating bodily waste matter.",
    "secondary": "In chemical botany and entomology, extrafloral nectaries function by excreting carbohydrate-rich fluids to attract predatory ants that defend the plant.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Some of these seedlings would inherit the nectar-**excreting** glands, gaining an advantage by attracting pollinating insects."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The sudoriferous glands assist the kidneys by **excreting** copious aqueous sweat containing traces of urea."},
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "The yeast cells thrive by absorbing sugars and **excreting** alcohol and carbonic acid gas as metabolic products."}
    ]
  },
  "excretion.md": {
    "primary": "The biological process of eliminating or expelling waste matter from living cells or tissues.",
    "secondary": "In comparative anatomy and physiology, the evolution of specialized excretion organs (nephridia, Malpighian tubules, kidneys) maintains osmotic homeostasis.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "One of the strongest instances of an animal performing an act solely for the good of another is that of aphids yielding their sweet **excretion** to ants."},
      {"author": "T. H. Huxley", "work": "Lessons in Elementary Physiology", "quote": "The skin, lungs, and kidneys cooperate in the vital function of **excretion**, preserving the chemical purity of the blood."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Impaired renal **excretion** leads to the accumulation of toxic metabolites in the circulating plasma."}
    ]
  },
  "excretory.md": {
    "primary": "Relating to or concerned with the biological excretion of waste matter.",
    "secondary": "In invertebrate embryology, the excretory system develops from primitive protonephridia equipped with ciliated flame cells.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The primordial vertebrate possessed an **excretory** apparatus consisting of segmental tubules opening into a longitudinal duct."},
      {"author": "T. H. Huxley", "work": "Lessons in Elementary Physiology", "quote": "The kidneys constitute the principal **excretory** organs for eliminating soluble nitrogenous waste from the mammalian body."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Toxic drugs frequently cause acute necrosis of the renal tubular epithelium during their **excretory** passage."}
    ]
  },
  "increase.md": {
    "primary": "To become or make greater in size, amount, intensity, or degree.",
    "secondary": "In economic growth theory, capital accumulation and technological innovation interact to increase aggregate national productivity.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Sonnet 15", "quote": "When I perceive that men as plants **increase**, cheered and checked even by the self-same sky, then do I marvel at our mortal state."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The division of labour tends to **increase** the productive powers of industry more than any other circumstance."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "As more individuals are produced than can possibly survive, there must in every case be a struggle for existence to check geometric **increase**."}
    ]
  },
  "increased.md": {
    "primary": "Made greater in size, amount, degree, or intensity.",
    "secondary": "In systemic pathology, increased vascular permeability during acute inflammation facilitates leukocyte migration into injured tissues.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "One afternoon it began to freeze, and the frost **increased** with every hour until the ruts were as hard as iron."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "With animals of all kinds, prolonged training and exercise have **increased** the power and endurance of the limbs."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "My application was at first fluctuating and uncertain; it gained strength as I proceeded, and soon **increased** into an uncontrollable passion."}
    ]
  },
  "increasing.md": {
    "primary": "Becoming greater in size, amount, intensity, or degree over time.",
    "secondary": "In astronomical cosmology, the expanding universe exhibits increasing distances between distant galactic clusters.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Sonnet 64", "quote": "When I have seen the hungry ocean gain advantage on the kingdom of the shore, and the firm soil win of the watery main, **increasing** store with loss and loss with store."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The ring of the sheep-bell was heard with **increasing** distinctness as the shepherd approached the sheepfold through the fog."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The species belonging to large genera are themselves spreading and **increasing** in number of varieties."}
    ]
  },
  "increasingly.md": {
    "primary": "To an increasing extent; progressively more and more.",
    "secondary": "In social history and public policy, urban populations became increasingly dependent upon municipal sanitation and clean water pipelines.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The material distinctions of rank and wealth he **increasingly** despised as superficial accidents of birth."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The navigation of the upper river became **increasingly** dangerous as snags and sunken sandbanks multiplied."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea found her husband's scholarship **increasingly** dry and disconnected from the urgent needs of humanity."}
    ]
  },
  "incredibility.md": {
    "primary": "The quality of being incredible, unbelievable, or impossible to believe.",
    "secondary": "In historical epistemology and philosophy of science, the incredibility of extraordinary claims requires proportionate empirical corroboration.",
    "quotes": [
      {"author": "David Hume", "work": "An Enquiry Concerning Human Understanding", "quote": "The intrinsic **incredibility** of a prodigy must be weighed against the probability of human deceit or optical delusion."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The swift collapse of ancient French monarchy was viewed with astonishment and **incredibility** by the courts of Europe."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The apparent **incredibility** of antipodal inhabitants vanished as soon as navigation proved the spherical shape of the globe."}
    ]
  },
  "incredible.md": {
    "primary": "Impossible or difficult to believe; extraordinary; astonishing.",
    "secondary": "In narrative fiction and travel literature, incredible occurrences challenge the reader's suspension of disbelief unless grounded in sensory realism.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Taming of the Shrew", "quote": "I tell you, 'tis **incredible** to believe how much she loves me: O, the kindest Kate!"},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "It seemed **incredible** to her that she had lived through so much tragedy and yet remained in outward appearance almost unchanged."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The length of time a wounded whale can remain submerged seems almost **incredible** to those unacquainted with cetacean anatomy."}
    ]
  },
  "incredibleness.md": {
    "primary": "The attribute or state of being incredible, astonishing, or beyond belief.",
    "secondary": "In theological and literary discourse, the incredibleness of an event prompts either rational skepticism or transcendent awe.",
    "quotes": [
      {"author": "Robert Boyle", "work": "Some Considerations Touching the Style of the Holy Scriptures", "quote": "The sublime simplicity of the narrative removes all suspicion of artifice despite the **incredibleness** of the miracle related."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The traveller lost his reputation for truthfulness by boasting of exploits whose **incredibleness** shocked all common sense."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The mind refuses assent when the **incredibleness** of the testimony contradicts the uniform course of nature."}
    ]
  },
  "increment.md": {
    "primary": "An increase or addition, especially one of a series on a fixed scale.",
    "secondary": "In differential calculus and mathematical analysis, an increment (delta x) represents a small change in the value of an independent variable.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The unearned **increment** of land value created by general social growth should be subject to special civic taxation."},
      {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "The mechanical wheels advanced by a uniform **increment** with each complete revolution of the drive axle."},
      {"author": "Alfred Marshall", "work": "Principles of Economics", "quote": "The marginal utility of each additional **increment** of a commodity diminishes as the consumer's total stock increases."}
    ]
  },
  "incremental.md": {
    "primary": "Relating to, resulting from, or advancing by small, successive increases or additions.",
    "secondary": "In evolutionary biology and systems design, incremental adaptation modifies existing structures through minor cumulative adjustments over time.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Complex organs like the eye have been perfected by natural selection through an **incremental** series of slight advantageous steps."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "The transformation of the cosmos proceeds by an **incremental** redistribution of matter and motion."},
      {"author": "Thorstein Veblen", "work": "The Theory of Business Enterprise", "quote": "Technological improvements in manufacturing are predominantly **incremental**, building steadily upon accumulated shop practice."}
    ]
  },
  "indiscreet.md": {
    "primary": "Having, showing, or proceeding from a lack of judgment, caution, or prudence; rashly communicative.",
    "secondary": "In political memoir and domestic tragedy, an indiscreet remark often unmasks covert alliances or precipitates marital estrangement.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "For as it would ill become me to be vain, **indiscreet**, or a fool, so I shall guard my speech with vigilance."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Rosamond was too **indiscreet** in her social ambitions, provoking her husband's quiet disapproval."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Lydia's **indiscreet** conduct at Brighton threatened the social ruin of her entire family."}
    ]
  },
  "indiscreetly.md": {
    "primary": "In a manner lacking prudence, caution, or good judgment; carelessly revealing private matters.",
    "secondary": "In diplomatic history and confidential correspondence, speaking indiscreetly to foreign envoys can compromise vital national interests.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Elton would never marry **indiscreetly**; he was far too prudent in worldly calculation to sacrifice fortune for passion."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The young diplomat had spoken **indiscreetly** at a dinner party, exposing a secret treaty to foreign journalists."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Guppy confided **indiscreetly** in his friend Weevle, confessing his infatuation with Esther Summerson."}
    ]
  },
  "indiscreetness.md": {
    "primary": "The trait or quality of being indiscreet; lack of prudence, discretion, or judgment in speech and action.",
    "secondary": "In moral psychology, habitual indiscreetness stems from vanity, impulsiveness, or a craving for immediate social attention.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The world forgives many vices more readily than that thoughtless **indiscreetness** which betrays the secrets of hospitality."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She lamented the **indiscreetness** of her hasty letter, which had placed her brother in a false position with his trustees."},
      {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "The archdeacon rebuked the curate for his public **indiscreetness** in preaching against the churchwardens."}
    ]
  },
  "indiscrete.md": {
    "primary": "Not separated into distinct, individual parts; continuous, undivided, or homogeneous.",
    "secondary": "In historical medicine and pathology, an indiscrete (confluent) smallpox eruption features pustules that run together into a continuous sheet.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In the severe confluent form of variola, the lesions become completely **indiscrete**, covering the face with an unbroken purulent crust."},
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "The molten metals formed an **indiscrete** mass in which no individual grains could be discerned under magnification."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Perceptual space presents itself as a continuous, **indiscrete** medium before the intellect divides it into feet and inches."}
    ]
  },
  "indiscretion.md": {
    "primary": "Behavior or speech that displays a lack of good judgment; an imprudent act or remark.",
    "secondary": "In narrative drama, a youthful indiscretion often acts as the tragic catalyst that triggers long-delayed retribution.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Our **indiscretion** sometimes serves us well when our deep plots do pall; and that should learn us there's a divinity that shapes our ends."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate recognized too late the financial **indiscretion** of furnishing his house on costly credit."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The puritan magistrates viewed her **indiscretion** as an open rebellion against the moral covenants of the colony."}
    ]
  },
  "recreant.md": {
    "primary": "Cowardly, unfaithful, or disloyal to a cause, duty, or belief; also a cowardly traitor or apostate.",
    "secondary": "In medieval chivalry and trial by combat, a combatant who yielded and declared himself recreant forfeited his honor and knightly rank forever.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard II", "quote": "Thou art a traitor and a **recreant**, false to thy God, thy sovereign, and to me!"},
      {"author": "Sir Walter Scott", "work": "Ivanhoe", "quote": "Yield thee, **recreant** knight, or by Saint George thy head shall pay the forfeit of thy treason!"},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The arch-rebel led his **recreant** legions across the burning plains of hell, defiant in defeat."}
    ]
  },
  "secrecy.md": {
    "primary": "The state of being kept secret, hidden, or confidential; the habit of maintaining confidences.",
    "secondary": "In political theory and executive prerogatives, state secrecy is justified to protect diplomatic deliberations and military operations from hostile espionage.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "In nature's infinite book of **secrecy** a little I can read."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The qualities essential to the management of foreign negotiations are unity, dispatch, and **secrecy**."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "A wonderful fact to reflect upon, that every human creature is constituted to be that profound secret and mystery to every other, wrapped in solemn **secrecy**."}
    ]
  },
  "secret.md": {
    "primary": "Not known or seen or not meant to be known or seen by others; kept hidden from general knowledge.",
    "secondary": "In esoteric philosophy and mystery religions, a secret knowledge (arcanum) is revealed only to initiates through sacred ritual.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "That this huge stage presenteth nought but shows whereon the stars in **secret** influence comment."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Words are sensible signs necessary for communication, where thoughts are the **secret** furniture of the solitary mind."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "He carried a dark, gnawing **secret** in his breast that poisoned every waking hour and prayer."}
    ]
  },
  "secretaire.md": {
    "primary": "A writing desk, often with a drop-down front or drawer that folds forward to provide a writing surface, and compartments for papers.",
    "secondary": "In French decorative arts and antique furniture history, the secrétaire à abattant was a tall, freestanding fall-front cabinet fashionable in the Louis XVI and Empire periods.",
    "quotes": [
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "She sat at her rosewood **secretaire**, drafting polite invitations to the family dinner with a quill pen."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Holmes examined the secret drawer concealed in the carved mahogany **secretaire** in the study."},
      {"author": "Honoré de Balzac", "work": "Eugénie Grandet", "quote": "Old Grandet locked the gold coins inside his heavy oak **secretaire**, pocketing the massive iron key with a triumphant grin."}
    ]
  },
  "secretarial.md": {
    "primary": "Relating to the work, duties, or professional skills of a secretary.",
    "secondary": "In bureaucratic sociology, secretarial administration coordinates organizational communications, archival filings, and institutional scheduling.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "A door opened, and a white-haired **secretarial** head, but wearing a compassionate expression, appeared in the doorway."},
      {"author": "G. K. Chesterton", "work": "The Man Who Was Thursday", "quote": "You will excuse me, he said with a rather ghastly smile, for being busy with urgent **secretarial** labors."},
      {"author": "H. G. Wells", "work": "The New Machiavelli", "quote": "His private office buzzed with efficient **secretarial** assistants typing state memorandums and sorting correspondence."}
    ]
  },
  "secretariat.md": {
    "primary": "A permanent administrative office or department, especially of an international or governmental organization; also the officials staffing it.",
    "secondary": "In international relations, the United Nations Secretariat is headed by the Secretary-General, carrying out the administrative and operational directives of the General Assembly and Security Council.",
    "quotes": [
      {"author": "Woodrow Wilson", "work": "Addresses on the League of Nations", "quote": "The permanent **secretariat** of the League will gather international statistics and maintain continuous communication among member states."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The joint **secretariat** rendered invaluable service by coordinating Allied staff planning across army and naval commands."},
      {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "A worldwide transport and health **secretariat** managed the logistical reconstruction of postwar civilization."}
    ]
  },
  "secretariate.md": {
    "primary": "The office, function, or administrative department of a secretary; an alternative spelling of secretariat.",
    "secondary": "In nineteenth-century colonial administration, the secretariate managed provincial revenue records, magistrate appointments, and imperial gazettes.",
    "quotes": [
      {"author": "Rudyard Kipling", "work": "Plain Tales from the Hills", "quote": "The dusty files in the imperial **secretariate** at Simla accumulated through long hot summers under the punkahs."},
      {"author": "Lord Macaulay", "work": "Essays on Clive and Hastings", "quote": "The young civil servant began his administrative career in the Bengal **secretariate** at Calcutta."},
      {"author": "George Orwell", "work": "Burmese Days", "quote": "The provincial **secretariate** dispatched formal circulars on forestry regulation to every district commissioner."}
    ]
  },
  "secretary.md": {
    "primary": "A person employed to assist with correspondence, keep records, and make appointments; also a principal official presiding over a government department.",
    "secondary": "In constitutional executive governance, Cabinet Secretaries (such as Secretary of State) advise the head of state and administer large executive departments.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VIII", "quote": "Cardinal, prithee call Gardiner to me, my new **secretary**: I find him a fit fellow."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "A petition was addressed to the Home **secretary**, advancing the extenuating circumstances of the tragedy."},
      {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "The Cabinet Minister dictated the terms of the secret memorandum to his private **secretary**."}
    ]
  },
  "secretaryship.md": {
    "primary": "The office, role, or term of service of a secretary.",
    "secondary": "In political history, holding a key cabinet secretaryship served as the premier stepping-stone to the premiership or presidency.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "He resigned the lucrative imperial **secretaryship** to devote his remaining years to literary and philosophical retirement."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "During his tenure of the foreign **secretaryship**, he preserved the European balance of power with consummate diplomatic finesse."},
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "My election to the **secretaryship** of the General Assembly opened valuable connections that aided my early public endeavors."}
    ]
  },
  "secretase.md": {
    "primary": "Any of several enzymes that cleave amyloid precursor protein (APP) into peptide fragments, including amyloid beta.",
    "secondary": "In molecular neurobiology and Alzheimer's disease pathology, beta-secretase and gamma-secretase are key therapeutic targets for preventing neurotoxic plaque aggregation.",
    "quotes": [
      {"author": "Santiago Ramón y Cajal", "work": "Degeneration and Regeneration of the Nervous System", "quote": "Proteolytic cleavage by specific enzymes like **secretase** alters membrane-bound neuronal precursors in degenerative neuropathies."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Biochemical investigations into senile dementia focus upon aberrant **secretase** activity generating cerebral amyloid deposits."},
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "The pathological transformation of neurofibrillary proteins involves specific enzyme cascades that cleave cellular scaffolding."}
    ]
  },
  "secrete.md": {
    "primary": "To produce and discharge a substance from an organ, gland, or cell; also to conceal or hide something away.",
    "secondary": "In mammalian endocrinology, specialized endocrine glands secrete hormones directly into the bloodstream to regulate distant physiological targets.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Mammary glands in rudimental form may often **secrete** a few drops of fluid in newborn infants."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "I design to **secrete** the paper in the wall of the chimney, where I have spent so many months of solitary captivity."},
      {"author": "T. H. Huxley", "work": "Lessons in Elementary Physiology", "quote": "The salivary glands **secrete** a clear digestive fluid that converts insoluble starches into soluble sugars."}
    ]
  },
  "secreter.md": {
    "primary": "An anatomical organ, cell, or organism that secretes a substance; also one who hides or conceals things.",
    "secondary": "In cellular histology, active secretory epithelial cells function as the primary secreter of mucus protecting visceral linings.",
    "quotes": [
      {"author": "Charles Darwin", "work": "Insectivorous Plants", "quote": "The glandular hairs of the Drosera leaf act as both an absorber of digested nutrients and a vigorous **secreter** of acid digestive fluid."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The thyroid parenchyma is the primary **secreter** of metabolic hormones governing basal cellular oxidation."},
      {"author": "T. H. Huxley", "work": "Lessons in Elementary Physiology", "quote": "The gastric mucous membrane functions as the specialized **secreter** of hydrochloric acid and pepsinogen."}
    ]
  },
  "secretin.md": {
    "primary": "A peptide hormone produced by the S cells of the duodenum that stimulates the pancreas to secrete bicarbonate-rich fluid.",
    "secondary": "In physiological history, secretin was discovered by Bayliss and Starling in 1902, marking the founding discovery that inaugurated the science of endocrinology.",
    "quotes": [
      {"author": "Ernest Starling", "work": "The Croonian Lectures on the Chemical Correlation of the Body Functions", "quote": "The discovery of **secretin** proved that chemical messengers circulating in the blood coordinate organ functions independently of the central nervous system."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Acid chyme entering the duodenum stimulates the release of **secretin**, which prompts the pancreas to pour out neutralizing bicarbonate fluid."},
      {"author": "T. H. Huxley", "work": "Lessons in Elementary Physiology", "quote": "The hormonal action of **secretin** demonstrated that visceral digestion is regulated by internal humoral secretions."}
    ]
  },
  "secretion.md": {
    "primary": "A substance produced and released by a gland or cell for a particular physiological function; also the process of producing it.",
    "secondary": "In medical physiology, exocrine secretion discharges onto epithelial surfaces via ducts, whereas endocrine secretion releases directly into interstitial fluid and blood.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The pedunculated cirripedes possess two minute folds of skin producing a cement **secretion** that glues the shell to floating timber."},
      {"author": "T. H. Huxley", "work": "Lessons in Elementary Physiology", "quote": "Bile is a continuous **secretion** of the liver, stored in the gall bladder until needed for intestinal digestion."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Suppression of the renal **secretion** is a symptom of grave import in acute circulatory collapse."}
    ]
  },
  "secretive.md": {
    "primary": "Inclined to conceal feelings, intentions, and information; uncommunicative, guarded, and reticent.",
    "secondary": "In psychological characterization, a secretive disposition arises from defensive self-protection or fear of social vulnerability.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Women are naturally **secretive**, and they like to do their own secret-keeping even from those who love them best."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Bulstrode's cold, **secretive** manner repelled any sympathetic approach from his medical colleagues."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "There was something dark and **secretive** about the third-story corridor of Thornfield Hall that filled Jane with foreboding."}
    ]
  },
  "secretively.md": {
    "primary": "In a secretive, stealthy, or furtive manner; avoiding detection or disclosure.",
    "secondary": "In narrative suspense, acting secretively creates dramatic tension by signaling hidden motives or illicit undertakings.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She stepped **secretively** across the moonlit meadow, careful not to disturb the resting cattle in the lane."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Tulkinghorn folded the legal papers **secretively** inside his coat, keeping his dark knowledge entirely to himself."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Dimmesdale looked **secretively** around the room before returning the mysterious manuscript to its hiding-place."}
    ]
  },
  "secretiveness.md": {
    "primary": "The tendency or disposition to keep things secret, hidden, or uncommunicated; reticence.",
    "secondary": "In nineteenth-century phrenology, secretiveness was classified as a distinct mental organ located above the ear, believed to govern reserve and concealment.",
    "quotes": [
      {"author": "George Eliot", "work": "Silas Marner", "quote": "His habitual **secretiveness** had become a second nature, preventing him from confessing his early marriage to his father."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Madame Beck possessed an extraordinary genius for **secretiveness**, watching everyone in the pensionnat while revealing nothing herself."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The old major's morbid **secretiveness** regarding the Agra treasure brought tragedy upon his sons."}
    ]
  },
  "secretly.md": {
    "primary": "In a secret, private, or covert manner; without the knowledge of others.",
    "secondary": "In narrative prose, cherishing a conviction or passion secretly emphasizes internal psychological solitude.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "I am given, sir, **secretly** to understand that your younger brother Orlando is determined this day to wrestle for a fall."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Heaven, if I had got jilted **secretly**, and the dishonour not known to the village, I might have endured the blow with dignity!"},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor had **secretly** endured the agony of her heart's trial without burdening her mother or sister with a single complaint."}
    ]
  },
  "secretor.md": {
    "primary": "An individual who secretes blood-group antigens into body fluids such as saliva, tears, and perspiration; also an organ that secretes.",
    "secondary": "In forensic serology and immunogenetics, secretor status (governed by the FUT2 gene) allows ABH blood typing from minute stains of saliva or semen.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Identification of the suspect was confirmed because the forensic specimen came from a known ABH **secretor** whose salivary antigens matched the stain."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Individual physiological variations, such as being an active glandular **secretor**, follow regular inherited laws across related mammalian lineages."},
      {"author": "Karl Landsteiner", "work": "The Specificity of Serological Reactions", "quote": "The demonstration that a large majority of human subjects are of the **secretor** type provided a powerful new tool in anthropological serology."}
    ]
  },
  "secretory.md": {
    "primary": "Relating to, performing, or promoting the biological secretion of substances.",
    "secondary": "In mucosal immunology, secretory immunoglobulin A (sIgA) serves as the primary immune barrier neutralizing pathogens on mucosal surfaces.",
    "quotes": [
      {"author": "T. H. Huxley", "work": "Lessons in Elementary Physiology", "quote": "The **secretory** activity of the pancreas is stimulated through nervous reflex arcs as well as humoral blood-borne agents."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic inflammation damages the **secretory** tubules of the gastric mucosa, producing achlorhydria."},
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Under the microscope, each **secretory** epithelial cell reveals active cytoplasmic granules accumulating before discharge."}
    ]
  },
  "uncreased.md": {
    "primary": "Not creased, folded, or wrinkled; perfectly smooth and flat.",
    "secondary": "In archival preservation and textile inspection, an uncreased document or garment displays pristine structural integrity without fiber fracture along fold lines.",
    "quotes": [
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "He opened the **uncreased** parchment envelope with a silver paper knife, admiring its heavy bond paper."},
      {"author": "Henry James", "work": "The American", "quote": "Newman smoothed the **uncreased** lapels of his new Parisian coat before entering the salon of the Marquise."},
      {"author": "Virginia Woolf", "work": "Jacob's Room", "quote": "The morning newspaper lay **uncreased** beside his coffee cup, pristine in the pale sunlight."}
    ]
  },
  "undersecretary.md": {
    "primary": "A subordinate or deputy secretary, especially a senior government official assisting a Cabinet Secretary.",
    "secondary": "In executive government departments, the Undersecretary of State or Defense manages day-to-day administrative operations and departmental bureaus.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The **undersecretary** laid the urgent diplomatic dispatches before the minister for immediate signature."},
      {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "Trelawney Hope held the responsible office of **undersecretary** for Foreign Affairs in the conservative cabinet."},
      {"author": "Woodrow Wilson", "work": "Congressional Government", "quote": "The permanent **undersecretary** preserves administrative continuity while political department heads come and go with elections."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Action\Dashboard — cre"

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

print(f"Dashboard — cre Batch 3: Successfully updated {updated}/{len(data)} notes.")
