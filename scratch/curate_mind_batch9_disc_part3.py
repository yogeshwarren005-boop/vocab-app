# -*- coding: utf-8 -*-
"""
Curates Dashboard — disc (Part 3: words 105-154, 50 words) in Cluster Mind & Knowledge.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_part3 = {
  "discovery": {
    "primary": "The act, process, or finding of something previously unknown, hidden, or unperceived.",
    "secondary": "In legal procedure, the compulsory pretrial disclosure of relevant documents and evidence.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "Human knowledge and human power meet in one, for the **discovery** of causes opens the way to works."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "The **discovery** of fossil intermediates in ancient strata provided striking confirmation of descent with modification."},
      {"author": "Blackstone", "work": "Commentaries on the Laws of England", "quote": "Courts of equity exercise extensive jurisdiction to compel the **discovery** of concealed contracts."}
    ]
  },
  "discredit": {
    "primary": "To harm the good reputation of someone or something; to cause disbelief or doubt regarding truth.",
    "secondary": "In financial affairs, the loss of confidence or commercial creditworthiness in an enterprise.",
    "quotes": [
      {"author": "David Hume", "work": "An Enquiry Concerning Human Understanding", "quote": "No testimony is sufficient to establish a miracle unless its falsehood would **discredit** the universal order of nature."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The malicious rumors were circulated by courtiers eager to **discredit** the victorious general before the emperor."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Failing to honor the public debt would irreparably **discredit** the infant republic in European markets."}
    ]
  },
  "discreditable": {
    "primary": "Tending to bring disgrace, dishonor, or reproach upon someone; damaging to moral character.",
    "secondary": "In civic appraisal, actions or associations that violate recognized standards of public integrity.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth felt that Lydia's reckless elopement was a deeply **discreditable** catastrophe for the entire family."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The lawyer warned that any financial compromise with such scoundrels would prove highly **discreditable** in court."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Bulstrode lived in terror that the **discreditable** secrets of his early commercial life would be unmasked."}
    ]
  },
  "discreditably": {
    "primary": "In a manner that brings shame, dishonor, or discredit; disgracefully and reproachfully.",
    "secondary": "In critical narrative evaluation, conducting an office or duty with disgraceful failure of honor.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The ministry retreated **discreditably** from their declared policy when parliamentary opposition stiffened."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Rawdon Crawley had handled his gambling debts **discreditably**, leaving ruin in his wake across London clubs."},
      {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "The compromised colonel behaved **discreditably** when confronted with the evidence of his stolen treaty."}
    ]
  },
  "discredited": {
    "primary": "Having suffered a loss of reputation, trust, or authority; rejected as false or unreliable.",
    "secondary": "In the history of science, theories or hypotheses permanently discarded after empirical refutation.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "The Problems of Philosophy", "quote": "The medieval doctrine of phlogiston was utterly **discredited** once Lavoisier demonstrated the role of oxygen in combustion."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The **discredited** mercantile system rested upon the false premise that gold alone constituted national wealth."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Dogmatic doctrines that were once revered frequently become **discredited** superstitions to subsequent generations."}
    ]
  },
  "discreet": {
    "primary": "Careful and circumspect in speech or conduct, especially in order to maintain privacy or avoid embarrassment.",
    "secondary": "In design or diplomacy, attractively unobtrusive, subtle, and modestly understated.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "Love is a smoke made with the fume of sighs; being purged, a fire sparkling in lovers' eyes; being vexed, a sea nourished with loving tears. What is it else? A madness most **discreet**."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor was so **discreet** in her conversations that no observer could detect her inward grief."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Gilbert Osmond preserved a **discreet** silence concerning his true intentions toward Isabel Archer."}
    ]
  },
  "discreetly": {
    "primary": "In a prudent, circumspect, or secretive manner so as to avoid attention, offense, or indiscretion.",
    "secondary": "In social conduct, managing sensitive personal transactions without drawing public scrutiny.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Mrs. Fairfax managed the household affairs **discreetly**, never probing into Mr. Rochester's private sorrows."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The royal visitor stepped **discreetly** into 221B Baker Street, cloaked against the heavy London fog."},
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "Winston placed the diary **discreetly** inside the alcove where the telescreen could not scan its pages."}
    ]
  },
  "discreetness": {
    "primary": "The attribute of being prudent, circumspect, tactful, and reserved in speech and behavior.",
    "secondary": "In administrative service, the reliable capacity to protect confidential information and maintain privacy.",
    "quotes": [
      {"author": "Samuel Richardson", "work": "Clarissa", "quote": "Her remarkable **discreetness** won the admiration of even the most severe matrons in the county."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The Lilliputian treasurer commended the traveler's **discreetness** in avoiding political entanglements."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "Jeanie Deans spoke with sober **discreetness** when answering the magistrate's searching inquiries."}
    ]
  },
  "discrepancy": {
    "primary": "A noticeable lack of compatibility, agreement, or consistency between two or more facts or claims.",
    "secondary": "In financial auditing and scientific measurement, an unexplained divergence between observed and expected values.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "This apparent **discrepancy** between our theoretical expectations and the fossil record requires careful examination."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A wide **discrepancy** between market price and natural price always stimulates reallocation of capital."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes instantly detected a curious **discrepancy** between the witness's timeline and the station clock."}
    ]
  },
  "discrepant": {
    "primary": "Inconsistent, disagreeing, conflicting, or failing to correspond with standard evidence.",
    "secondary": "In philosophical logic and empirical analysis, propositions or data sets that cannot be mutually reconciled.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "When experimental observations yield **discrepant** results, natural philosophers must refine their instruments."},
      {"author": "David Hume", "work": "A Treatise of Human Nature", "quote": "The testimony of different witnesses on this event proved hopelessly **discrepant** upon critical scrutiny."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Ancient historians provide widely **discrepant** estimates of the barbarian cavalry assembled on the Danube."}
    ]
  },
  "discrete": {
    "primary": "Individually separate, distinct, discontinuous, or consisting of unconnected constituent parts.",
    "secondary": "In mathematics and digital computation, values or variables taking only distinct separate points rather than a continuum.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The mind perceives number by repeating the **discrete** idea of unity across individual perceptions."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Consciousness does not appear chopped up into **discrete** bits, but flows like a continuous stream."},
      {"author": "Bertrand Russell", "work": "Introduction to Mathematical Philosophy", "quote": "The arithmetic of natural numbers deals exclusively with **discrete** structural relations."}
    ]
  },
  "discreteness": {
    "primary": "The property of existing as distinct, discontinuous, or individually separate constituent parts.",
    "secondary": "In physics and quantum mechanics, the fundamental characteristic of energy existing in individual quanta.",
    "quotes": [
      {"author": "Charles Sanders Peirce", "work": "Collected Papers", "quote": "Continuity implies an endless unbroken flow, whereas **discreteness** marks isolated conceptual elements."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Sensory impressions possess an apparent **discreteness** only when dissected by analytical attention."},
      {"author": "Bertrand Russell", "work": "The Analysis of Matter", "quote": "Modern physics reveals that radiant energy exhibits both wave continuity and corpuscular **discreteness**."}
    ]
  },
  "discretion": {
    "primary": "The freedom or authority to decide what should be done in a particular situation; prudence and circumspection.",
    "secondary": "In jurisprudence, the judicial power to decide legal issues within principles of equity rather than rigid rules.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "The better part of valor is **discretion**, in the which better part I have saved my life."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The judiciary has neither force nor will, but merely judgment, exercising prudent **discretion** under the constitution."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Bennet left the choice of guests entirely to the **discretion** of his sensible eldest daughter."}
    ]
  },
  "discretional": {
    "primary": "Subject to, depending on, or exercised through individual judgment rather than mandatory rule.",
    "secondary": "In administrative governance, statutory authority that permits official options based on circumstance.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Magistrates must not transform limited **discretional** powers into arbitrary personal tyranny."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The colonial governor held extensive **discretional** authority to negotiate treaties with tribal leaders."},
      {"author": "Walter Bagehot", "work": "The English Constitution", "quote": "The crown preserves certain **discretional** prerogatives designed for national emergencies."}
    ]
  },
  "discretionary": {
    "primary": "Available for use or distribution at the discretion of an authorized person; not fixed by mandatory regulation.",
    "secondary": "In economics and corporate finance, expendable funds remaining after meeting essential operational commitments.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Prudent merchants maintain a reserve of **discretionary** capital to exploit unexpected market opportunities."},
      {"author": "Alexander Hamilton", "work": "Report on Manufactures", "quote": "The legislature appropriately granted **discretionary** funds to foster domestic industrial development."},
      {"author": "John Maynard Keynes", "work": "The General Theory of Employment, Interest and Money", "quote": "Household propensity to consume drops when **discretionary** income is curtailed by rising prices."}
    ]
  },
  "discriminable": {
    "primary": "Capable of being distinguished, recognized as distinct, or differentiated from others.",
    "secondary": "In sensory psychophysics, minimal sensory differences that human perceptual faculties can reliably detect.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Two musical pitches are barely **discriminable** when their frequencies differ by only a fraction of a cycle."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Simple sensory qualities must remain clearly **discriminable** if the understanding is to construct valid ideas."},
      {"author": "Bertrand Russell", "work": "Our Knowledge of the External World", "quote": "Physical objects present an infinite number of subtly **discriminable** perspectives to the observer."}
    ]
  },
  "discriminate": {
    "primary": "To recognize or perceive the clear distinction between things; to differentiate accurately.",
    "secondary": "In social ethics and civil rights law, to treat individuals unjustly or unequally on the basis of category.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "It is the true mark of philosophy to **discriminate** between real causes and accidental associations."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Cultivated intellects readily **discriminate** between higher intellectual pleasures and crude sensual gratifications."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Female birds exhibit extraordinary ability to **discriminate** subtle differences in male plumage and song."}
    ]
  },
  "discriminating": {
    "primary": "Having or showing refined taste, acute discernment, or perceptive judgment; distinguishing acutely.",
    "secondary": "In trade and tariff policy, duties or restrictions applied selectively against specific nations.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Knightley possessed a **discriminating** judgment that penetrated through social pretension."},
      {"author": "Henry James", "work": "The Art of Fiction", "quote": "The novelist appeals to the **discriminating** reader who appreciates psychological subtleties."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Retaliatory customs duties against foreign shipping were inherently **discriminating** in operation."}
    ]
  },
  "discrimination": {
    "primary": "The ability to recognize and understand fine distinctions; unjust prejudicial treatment of categories of people.",
    "secondary": "In legal constitutional doctrine, the unlawful denial of equal protection under civil statutes.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Intellectual culture consists in refining our powers of **discrimination** between essence and outward appearance."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Democratic equality gradually dissolves every social **discrimination** based solely on aristocratic birth."},
      {"author": "Frederick Douglass", "work": "Narrative of the Life of Frederick Douglass", "quote": "Legalized **discrimination** maintained the brutal system of bondage in southern plantations."}
    ]
  },
  "discriminative": {
    "primary": "Serving to distinguish, differentiate, or mark a characteristic difference between things.",
    "secondary": "In psychological conditioning, stimuli that signal whether a particular operant response will be reinforced.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "Genius displays a remarkably **discriminative** insight into the latent affinities of human thought."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Natural selection acts upon every **discriminative** variation that confers an advantage in survival."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The organism learns to recognize the **discriminative** cue before initiating the conditioned reaction."}
    ]
  },
  "discriminator": {
    "primary": "A person who or device which discerns, separates, differentiates, or distinguishes between entities.",
    "secondary": "In electronics and machine learning, a circuit or neural model that distinguishes valid signals from noise or fakes.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "The true experimenter acts as a patient **discriminator** between valid evidence and deceptive idols."},
      {"author": "Arthur Eddington", "work": "The Nature of the Physical World", "quote": "The laboratory apparatus functions as an objective physical **discriminator** of particle velocities."},
      {"author": "Norbert Wiener", "work": "Cybernetics", "quote": "The electronic **discriminator** evaluates incoming pulse frequencies to filter transmission distortion."}
    ]
  },
  "discriminatory": {
    "primary": "Characterized by, showing, or making unfair distinctions; displaying prejudicial bias against a group.",
    "secondary": "In constitutional law, policies that intentionally burden protected classes without compelling justification.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "The Subjection of Women", "quote": "Society cannot prosper while enforcing **discriminatory** restrictions against one half of humanity."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Any **discriminatory** law based on hereditary rank violates the core spirit of the republic."},
      {"author": "Frederick Douglass", "work": "My Bondage and My Freedom", "quote": "Free northern states still imposed cruel and **discriminatory** codes upon Black citizens."}
    ]
  },
  "discursive": {
    "primary": "Digressing from subject to subject; relating to reasoned discourse or argument rather than intuition.",
    "secondary": "In philosophical epistemology, knowledge acquired step by step through logical deduction.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Reason receives / And reason is her being, **discursive** or intuitive; / Discourse is oftest yours, the latter most is ours."},
      {"author": "Immanuel Kant", "work": "Critique of Pure Reason", "quote": "Human understanding is a **discursive** faculty that operates by means of concepts rather than direct intuition."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The essayist adopted a pleasingly **discursive** style, wandering gracefully from antiquity to modern verse."}
    ]
  },
  "discursively": {
    "primary": "In a digressive, rambling manner; by method of logical discourse and deductive reasoning.",
    "secondary": "In critical essay writing, progressing through varied associative reflections rather than a rigid thesis.",
    "quotes": [
      {"author": "Thomas De Quincey", "work": "Confessions of an English Opium-Eater", "quote": "He conversed **discursively**, leaping from German metaphysics to Persian poetry without pause."},
      {"author": "William Hazlitt", "work": "Table-Talk", "quote": "Montaigne writes **discursively**, exploring human nature through informal autobiographical digressions."},
      {"author": "Charles Lamb", "work": "Essays of Elia", "quote": "The old scholar chatted **discursively** about forgotten folios while pouring out tea for his guests."}
    ]
  },
  "discursiveness": {
    "primary": "The characteristic of digressing widely in speech or thought; progression by rational argument.",
    "secondary": "In literary composition, the deliberate stylistic tendency to wander through diverse topics.",
    "quotes": [
      {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "The **discursiveness** of the author's narrative often obscures the underlying unity of his moral theme."},
      {"author": "Henry James", "work": "Partial Portraits", "quote": "Turgenev disliked the sprawling **discursiveness** of certain contemporary French naturalists."},
      {"author": "Samuel Johnson", "work": "Lives of the Most Eminent English Poets", "quote": "Dryden's prefaces delight the reader through their intellectual energy despite occasional **discursiveness**."}
    ]
  },
  "discus": {
    "primary": "A heavy, disk-shaped object thrown for distance in athletic field competitions.",
    "secondary": "In classical antiquity and sculpture, the circular stone or bronze plate thrown in the ancient Olympic games.",
    "quotes": [
      {"author": "Homer", "work": "Iliad", "quote": "Polypoetes seized the heavy cast-iron **discus** and hurled it far beyond all rival marksmen."},
      {"author": "Virgil", "work": "Aeneid", "quote": "The Trojan youths exercised along the shore, competing with the flying **discus** and javelin."},
      {"author": "Alexander Pope", "work": "The Odyssey", "quote": "Ulysses rose in wrath and caught the ponderous **discus**, sending it whistling across the Phaeacian field."}
    ]
  },
  "discuss": {
    "primary": "To talk about something with another person or group in order to exchange ideas or reach a decision.",
    "secondary": "In medicine and historical usage, to disperse or dissipate a morbid tumor or bodily congestion.",
    "quotes": [
      {"author": "Plato", "work": "The Republic", "quote": "Let us calmly **discuss** whether justice is stronger and more profitable than injustice."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "The sisters retired to their room to **discuss** the unexpected arrival of Mr. Bingley at Netherfield."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "Prudent statesmen **discuss** matters privately before presenting treaties to public assemblies."}
    ]
  },
  "discussant": {
    "primary": "A person who takes part in a formal discussion, conference symposium, or academic panel.",
    "secondary": "In professional conventions, an invited commentator designated to critique a presented paper.",
    "quotes": [
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "Every active **discussant** in the democratic seminar contributes to the collective reconstruction of ideas."},
      {"author": "William James", "work": "The Meaning of Truth", "quote": "The philosophical **discussant** must define terms rigorously before debating the nature of pragmatic reality."},
      {"author": "Bertrand Russell", "work": "Skeptical Essays", "quote": "An impartial **discussant** weighs contradictory arguments without succumbing to theological dogmatism."}
    ]
  },
  "discussion": {
    "primary": "The action or process of talking about something in order to reach a decision or exchange ideas.",
    "secondary": "In parliamentary and judicial proceedings, the formal examination and debate of a legislative measure.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Complete liberty of contradicting and disproving our opinion is the very condition which justifies us in assuming its truth; in no other way can a being with human faculties have any rational assurance of being right, except through free **discussion**."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Public town hall **discussion** teaches citizens the practical art of self-governance."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "A prolonged family **discussion** followed regarding the prudent reduction of their annual expenditures."}
    ]
  },
  "indiscernible": {
    "primary": "Impossible to see, hear, or perceive clearly; indistinguishable from surroundings.",
    "secondary": "In philosophical metaphysics, entities sharing identical properties according to Leibniz's identity principle.",
    "quotes": [
      {"author": "Gottfried Wilhelm Leibniz", "work": "Monadology", "quote": "There are never in nature two beings which are precisely alike, for perfectly **indiscernible** substances cannot exist."},
      {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "The chemical tincture rendered his living bodily tissues completely transparent and **indiscernible** in air."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Through the dense Dartmoor mist, the distant trackway was wholly **indiscernible** to our eyes."}
    ]
  },
  "indiscipline": {
    "primary": "Lack of discipline, restraint, or obedience to rules; uncontrolled and disorderly behavior.",
    "secondary": "In military history, the breakdown of command structure and insubordination within armed forces.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The chronic **indiscipline** of the Roman legions along the Danube led directly to repeated frontier catastrophes."},
      {"author": "Winston Churchill", "work": "The River War", "quote": "Nothing destroys the cohesion of an army so swiftly as tolerated **indiscipline** among raw recruits."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "Revolutionary militias suffered gravely from military **indiscipline** during the early Aragon campaign."}
    ]
  },
  "indiscreet": {
    "primary": "Having, showing, or proceeding from a lack of prudence, good judgment, or secrecy.",
    "secondary": "In diplomatic relations, dangerously revealing confidential communications or intentions.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Lydia's **indiscreet** chatter at the dinner table threatened to expose private family arrangements."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip regretted his **indiscreet** confession to Herbert concerning his impossible adoration of Estella."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The young diplomat realized too late that an **indiscreet** word to the foreign agent had compromised the treaty."}
    ]
  },
  "indiscreetly": {
    "primary": "In an imprudent, unguarded, or careless manner, especially regarding secrets or sensitive matters.",
    "secondary": "In narrative characterization, divulging confidential intentions through thoughtless vanity.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Harriet spoke **indiscreetly** of Mr. Elton's visits, fostering baseless expectations of an imminent proposal."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Jos Sedley bragged **indiscreetly** about his military exploits before cynical officers at Brussels."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Countess Gemini revealed the secret **indiscreetly**, relishing the dramatic shock it produced upon Isabel."}
    ]
  },
  "indiscreetness": {
    "primary": "The attribute of lacking discretion, prudence, or caution in speech and conduct; imprudence.",
    "secondary": "In biographical assessment, habitual carelessness that damages personal alliances and social trust.",
    "quotes": [
      {"author": "Samuel Richardson", "work": "Clarissa", "quote": "Lovelace mocked the fatal **indiscreetness** of those who trusted his promises of marriage."},
      {"author": "Jonathan Swift", "work": "A Tale of a Tub", "quote": "The author condemned the reckless **indiscreetness** of young wits who satirized sacred institutions."},
      {"author": "Walter Scott", "work": "Waverley", "quote": "The chieftain chided Fergus Mac-Ivor for political **indiscreetness** that endangered the Highland rebellion."}
    ]
  },
  "indiscrete": {
    "primary": "Not separated into distinct parts; continuous, undivided, or homogeneous in composition.",
    "secondary": "In pathology and botany, lesions or pustules that run together into an undivided mass.",
    "quotes": [
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Primitive creation existed as an **indiscrete** chaos before the divine word divided light from darkness."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Pure space appears to the unassisted senses as an **indiscrete** and unbroken expanse."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Immediate sensory experience begins as a buzzing, **indiscrete** whole before intellectual categorization."}
    ]
  },
  "indiscretion": {
    "primary": "Behavior or speech that displays a lack of good judgment; an imprudent act or remark.",
    "secondary": "In ethical conduct, a minor social or moral lapse that exposes someone to public censure.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Lydia's reckless **indiscretion** in running away with Wickham brought disgrace upon her father's house."},
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "I recorded this early **indiscretion** frankly, wishing young tradesmen to avoid similar pitfalls of youth."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A momentary popular **indiscretion** must not be permitted to dismantle fundamental constitutional safeguards."}
    ]
  },
  "indiscriminate": {
    "primary": "Done at random or without careful judgment; making no distinctions; chaotic and promiscuous.",
    "secondary": "In military warfare, weapons deployment or bombardment that strikes combatants and noncombatants alike.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The barbarian horde indulged in **indiscriminate** slaughter of citizens throughout the captured capital."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "Nature does not preserve variations through **indiscriminate** chance, but through natural selection of the fittest."},
      {"author": "Rachel Carson", "work": "Silent Spring", "quote": "The **indiscriminate** aerial spraying of synthetic pesticides destroyed pollinating bees alongside targeted pests."}
    ]
  },
  "indiscriminately": {
    "primary": "In a random, haphazard manner without making distinctions or applying careful judgment.",
    "secondary": "In sociological analysis, applying rules or distributions uniformly without regard to merit or need.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Monarchs who bestow royal monopolies **indiscriminately** stifle domestic enterprise and trade."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Flattery showered **indiscriminately** upon the sovereign people corrupts civic integrity as surely as royal courtliness."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Pumice and volcanic ash were scattered **indiscriminately** across sea and shore after the eruption."}
    ]
  },
  "indiscriminating": {
    "primary": "Lacking the power or habit of making fine distinctions; uncritical and undiscerning.",
    "secondary": "In literary criticism, praise or admiration bestowed blindly without analytical discernment.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "An **indiscriminating** zeal for destruction leveled venerable institutions alongside real abuses."},
      {"author": "Jane Austen", "work": "Northanger Abbey", "quote": "Catherine was too simple and warm-hearted to possess an **indiscriminating** contempt for human foibles."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The provincial public read his shallow sermons with **indiscriminating** enthusiasm and piety."}
    ]
  },
  "interdisciplinary": {
    "primary": "Relating to or involving two or more academic disciplines or fields of study.",
    "secondary": "In scientific research methodology, collaborative integration of principles from multiple branches of knowledge.",
    "quotes": [
      {"author": "Norbert Wiener", "work": "Cybernetics", "quote": "Cybernetics developed from the **interdisciplinary** confluence of electrical engineering, neurology, and mathematical logic."},
      {"author": "Thomas Kuhn", "work": "The Structure of Scientific Revolutions", "quote": "Crisis in a mature science often provokes **interdisciplinary** debates that usher in a new paradigm."},
      {"author": "Carl Sagan", "work": "The Demon-Haunted World", "quote": "Astrobiology requires an intensely **interdisciplinary** cooperation among astronomers, biologists, and geologists."}
    ]
  },
  "rediscover": {
    "primary": "To discover something again after it has been forgotten, lost, or neglected.",
    "secondary": "In intellectual history, to re-evaluate classical or ancient knowledge with fresh understanding.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Renaissance scholars strove to **rediscover** the lost observational wisdom of ancient Greek investigators."},
      {"author": "John Muir", "work": "My First Summer in the Sierra", "quote": "In these wild mountain solitudes, weary wanderers **rediscover** their primordial kinship with nature."},
      {"author": "Bertrand Russell", "work": "A History of Western Philosophy", "quote": "Modern logicians had to **rediscover** through rigorous proofs principles that Leibniz had glimpsed centuries earlier."}
    ]
  },
  "rediscovery": {
    "primary": "The act or process of finding, uncovering, or recognizing something forgotten or lost again.",
    "secondary": "In the history of science, the independent identification of a forgotten principle or lost manuscript.",
    "quotes": [
      {"author": "Thomas Kuhn", "work": "The Structure of Scientific Revolutions", "quote": "The famous **rediscovery** of Mendel's laws in 1900 fundamentally transformed evolutionary biology."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **rediscovery** of the Justinian Pandects at Amalfi revived the study of Roman civil law across Europe."},
      {"author": "Carl Sagan", "work": "Cosmos", "quote": "The European Renaissance was catalyzed by the enthusiastic **rediscovery** of classical Alexandrian science."}
    ]
  },
  "undiscerning": {
    "primary": "Lacking judgment, insight, or the ability to perceive fine distinctions; unperceptive.",
    "secondary": "In aesthetic criticism, admiring vulgar artifice while remaining blind to genuine artistic beauty.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Sir John Middleton was an **undiscerning** host who valued good company solely by numbers and noise."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The **undiscerning** multitude applauds flamboyant rhetoric while passing over profound philosophical truth."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Isabel realized with sorrow that her husband regarded her mind as merely an **undiscerning** ornament."}
    ]
  },
  "undiscipline": {
    "primary": "Absence or lack of discipline, moral training, restraint, or self-control; wild insubordination.",
    "secondary": "In military history, the dangerous disorder resulting from lax officers and broken subordination.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Pervasive **undiscipline** among the praetorian cohorts precipitated the rapid decline of imperial authority."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Total freedom without moral restraint degenerates rapidly into political frenzy and domestic **undiscipline**."},
      {"author": "Walter Scott", "work": "Old Mortality", "quote": "The Covenanter army was weakened by doctrinal bickering and internal military **undiscipline**."}
    ]
  },
  "undisciplined": {
    "primary": "Lacking discipline, control, or moral training; unruly, disobedient, or unchecked.",
    "secondary": "In intellectual endeavors, thought characterized by sloppy reasoning and emotional bias.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Fred Vincy's genial good nature was accompanied by an **undisciplined** habit of financial extravagance."},
      {"author": "John Stuart Mill", "work": "Autobiography", "quote": "My father warned that an **undisciplined** intellect falls prey to romantic illusions and superstition."},
      {"author": "Thucydides", "work": "History of the Peloponnesian War", "quote": "The Athenian fleet was thrown into panic by the **undisciplined** shouting of inexperienced rowers."}
    ]
  },
  "undisclosed": {
    "primary": "Not revealed, made known, or publicly disclosed; kept secret or confidential.",
    "secondary": "In legal and commercial transactions, terms or liabilities deliberately hidden from contracting parties.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes kept certain vital clues strictly **undisclosed** until the final trap could be sprung on the moor."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Darcy's generous financial intervention in Lydia's wedding was meant to remain permanently **undisclosed**."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Lady Dedlock harbored an **undisclosed** secret that cast a shadow of dread over her noble existence."}
    ]
  },
  "undiscouraged": {
    "primary": "Not having lost heart, enthusiasm, or confidence; persevering steadfastly despite obstacles.",
    "secondary": "In heroic narrative and exploration, resolutely pushing forward through repeated perils and failures.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The botanist remained **undiscouraged** by drenching tropical downpours, collecting rare orchids along the river."},
      {"author": "Winston Churchill", "work": "The Gathering Storm", "quote": "The British people stood resolute and **undiscouraged** when facing the imminent menace of invasion."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The wild builder remains **undiscouraged** by winter frost, preparing his ground for spring planting."}
    ]
  },
  "undiscoverable": {
    "primary": "Impossible to find, detect, perceive, or ascertain through investigation or observation.",
    "secondary": "In natural philosophy and metaphysics, ultimate principles forever hidden beyond empirical inquiry.",
    "quotes": [
      {"author": "David Hume", "work": "An Enquiry Concerning Human Understanding", "quote": "The ultimate secret connection binding cause and effect remains forever **undiscoverable** by human reason."},
      {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "Moriarty's criminal organization was designed so cunningly that its master brain remained **undiscoverable**."},
      {"author": "Immanuel Kant", "work": "Critique of Pure Reason", "quote": "The thing-in-itself, stripped of all sensible appearances, is completely **undiscoverable** by our senses."}
    ]
  },
  "undiscovered": {
    "primary": "Not yet found, explored, detected, or brought to human knowledge; hidden or unknown.",
    "secondary": "In geography and celestial mechanics, uncharted lands or unobserved planets awaiting empirical identification.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "The **undiscovered** country from whose bourn / No traveller returns, puzzles the will."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The white whale swam in vast, **undiscovered** depths of the Pacific, unseen by harpooners."},
      {"author": "Carl Sagan", "work": "Cosmos", "quote": "Billions of planetary systems remain **undiscovered** in the sprawling spiral arms of our galaxy."}
    ]
  },
  "undiscriminating": {
    "primary": "Lacking discrimination, taste, or critical acumen; failing to recognize differences.",
    "secondary": "In natural theology and philosophy, destruction or bounty distributed blindly by physical forces.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "An **undiscriminating** predator devours larvae without regard to the subtle mimicry of their coloring."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "An **undiscriminating** appetite for novelty leads democratic societies to discard valuable traditions."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The mob unleashed **undiscriminating** violence against historic monuments of French architecture."}
    ]
  }
}
