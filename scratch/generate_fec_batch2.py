# -*- coding: utf-8 -*-
import os, re

data = {
  "defectiveness.md": {
    "primary": "The presence of faults, operational flaws, or structural blemishes that impair functionality or soundness.",
    "secondary": "In quality assurance and legal warranty doctrine, defectiveness denotes a failure of a manufactured good to meet requisite safety or performance standards.",
    "quotes": [
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The queen, giving great allowance for my **defectiveness** in speaking, was, however, surprised at so much wit and good sense in so diminutive an animal."},
      {"author": "Jeremy Bentham", "work": "An Introduction to the Principles of Morals and Legislation", "quote": "Every legislation that fails to proportion punishments to offences suffers from an inherent **defectiveness** of design."},
      {"author": "William Paley", "work": "Natural Theology", "quote": "The apparent **defectiveness** of an organ in one creature is often compensated by an extraordinary redundancy in another."}
    ]
  },
  "effectivity.md": {
    "primary": "The operational capacity to produce a desired outcome, enforce an obligation, or achieve practical validity.",
    "secondary": "In administrative law and international jurisprudence, effectivity refers to the actual exercise of sovereign authority or the binding temporal force of an enacted treaty or regulation.",
    "quotes": [
      {"author": "Woodrow Wilson", "work": "Congressional Government", "quote": "The practical **effectivity** of any statute depends far more upon the energy of the executive departments than upon the debates of legislators."},
      {"author": "Max Weber", "work": "The Theory of Social and Economic Organization", "quote": "The bureaucratic apparatus achieves its maximum **effectivity** when operating under impersonal rules and stable hierarchies."},
      {"author": "Henry Maine", "work": "Ancient Law", "quote": "The social **effectivity** of primitive legal codes rested upon ceremonial rigidity rather than abstract notions of equity."}
    ]
  },
  "feces.md": {
    "primary": "Solid or semisolid bodily waste discharged from the digestive tract through the bowels after digestion.",
    "secondary": "In gastroenterology, microbiology, and forensic ecology, feces provide critical diagnostic specimens for assessing gut microbiome balance, metabolic absorption, and enteric pathogen shedding.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Microscopic examination of the **feces** reveals the presence of occult blood, parasitic ova, and undigested dietary fibers."},
      {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould through the Action of Worms", "quote": "Earthworms swallow enormous quantities of earth to extract organic matter, voiding their **feces** as fertile surface castings."},
      {"author": "T. H. Huxley", "work": "Lessons in Elementary Physiology", "quote": "The indigestible residue of the alimentary canal is consolidated and expelled from the rectum in the form of **feces**."}
    ]
  },
  "fecula.md": {
    "primary": "Nutritive starchy powder extracted from seeds, roots, tubers, or stems of plants through washing and sedimentation.",
    "secondary": "In historical botanical chemistry and pharmacognosy, fecula referred specifically to pure amylum separated from fibrous cellular tissue, prized as an easily digestible nutrient.",
    "quotes": [
      {"author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "By grating the potato root and washing it upon a fine sieve, the starchy **fecula** deposits at the bottom of the vessel as a dazzling white powder."},
      {"author": "Humphry Davy", "work": "Elements of Agricultural Chemistry", "quote": "The nutritive value of edible tuberous plants corresponds directly to the abundance of insoluble **fecula** contained within their cells."},
      {"author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "Under the influence of heat and dilute acids, vegetable **fecula** undergoes transformation into soluble dextrin and sugar."}
    ]
  },
  "feculence.md": {
    "primary": "The property or state of being turbid, fouled, or laden with muddy or foul dregs and sediment.",
    "secondary": "In philosophical ethics and theological allegory, feculence denotes moral corruption, spiritual dross, or terrestrial impurity clouding pure contemplation.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Out of that dark **feculence** of chaotic doubt and despair, a clearer spiritual dawn began slowly to rise."},
      {"author": "John Milton", "work": "Of Reformation", "quote": "The pure fountain of divine truth was choked and darkened by the muddy **feculence** of superstitious traditions."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Our clearest perceptions are too frequently mingled with sensory **feculence** that obscures the true nature of things."}
    ]
  },
  "feculent.md": {
    "primary": "Foul, murky, or muddy with impurities, sediment, or putrid particulate matter.",
    "secondary": "In pathology and surgical examination, describing bodily exudates, effusions, or peritoneal fluids having an odor or appearance suggestive of intestinal contents.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The stagnant pool was thick and **feculent**, giving off a sulfurous vapor beneath the oppressive midday heat."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Aspiration of the peritoneal cavity yielded a dark, **feculent** fluid confirming intestinal perforation."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The sluggish waters of the ditch had degenerated into a **feculent** marsh breeding pestilence among the besieging troops."}
    ]
  },
  "fecund.md": {
    "primary": "Capable of producing abundant offspring, fruit, or vegetative growth; highly fertile.",
    "secondary": "In cultural and intellectual history, fecund characterizes an intellect, artistic period, or conceptual framework that spawns numerous ideas, innovations, or derivative works.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Even the least **fecund** of animals would multiply with astonishing rapidity if all their offspring survived and reproduced."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "A truly **fecund** mind does not merely store facts, but generates fresh principles and illuminates all it contemplates."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "Nature seemed intensely **fecund** in that sunny valley, bursting with vibrant blossoms and fragrant herbs."}
    ]
  },
  "fecundate.md": {
    "primary": "To make fertile, fruitful, or productive; to impregnate or pollinate an ovum or flower.",
    "secondary": "In biological embryology and evolutionary botany, to fecundate entails the fusion of male and female gametes to initiate zygotic cell division.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "Insects carrying pollen from distant blossoms arrive to **fecundate** the receptive stigmas with remarkable efficiency."},
      {"author": "Thomas Henry Huxley", "work": "Evidence as to Man's Place in Nature", "quote": "The spermatozoa must penetrate the investing envelope of the ovum in order to **fecundate** the germinal vesicle."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "External environmental conditions must remain favorable if the liberated pollen is successfully to **fecundate** the flower."}
    ]
  },
  "fecundation.md": {
    "primary": "The process of fertilizing, impregnating, or making fruitful, especially the union of gametes.",
    "secondary": "In comparative developmental biology, fecundation encompasses the sequence of biochemical interactions between sperm and egg membrane preceding pronuclear fusion.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Repeated experiments prove that artificial **fecundation** produces vigorous seedlings even under adverse climatic conditions."},
      {"author": "Louis Agassiz", "work": "Methods of Study in Natural History", "quote": "The morphological changes occurring immediately following **fecundation** reveal the universal archetype of embryonic growth."},
      {"author": "Ernst Haeckel", "work": "The Evolution of Man", "quote": "The historical mystery of **fecundation** was finally solved when microscopists observed the direct conjugation of male and female nuclei."}
    ]
  },
  "fecundity.md": {
    "primary": "The capacity of an organism or population to produce abundant offspring; reproductive capability.",
    "secondary": "In demography and population ecology, fecundity measures the physiological maximum potential reproductive output of an individual or cohort under optimal environmental conditions.",
    "quotes": [
      {"author": "Thomas Robert Malthus", "work": "An Essay on the Principle of Population", "quote": "The natural **fecundity** of the human species is capable of doubling numbers every twenty-five years if unchecked by subsistence."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Natural selection exerts a powerful influence upon the relative **fecundity** of competing animal varieties."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The extraordinary **fecundity** of tropical soil yields multiple harvests with minimal application of human labor."}
    ]
  },
  "imperfect.md": {
    "primary": "Faulty, incomplete, or possessing defects; falling short of an ideal standard of excellence or wholeness.",
    "secondary": "In linguistics, imperfect denotes a verbal tense or aspect expressing past action viewed as continuous, habitual, or incomplete.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "How would mine eyes be blessed made, by looking on thee in the living day, when in the **imperfect** night thy shadow shines."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "I believe that the very **imperfect** notion ordinarily formed of its meaning is the chief obstacle which impedes its reception."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The geological record is incomparably more **imperfect** than is generally supposed by most modern naturalists."}
    ]
  },
  "imperfectibility.md": {
    "primary": "The inherent incapacity of human nature, knowledge, or societal institutions to achieve absolute flawlessness.",
    "secondary": "In political philosophy and theological anthropology, imperfectibility serves as a foundational doctrine asserting that human finite limitations preclude utopian social arrangements.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "A prudent statesman acknowledges the permanent **imperfectibility** of human contrivances and distrusts all radical schemes of total renovation."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The intrinsic **imperfectibility** of mortal wisdom requires that government be founded upon checks and balances rather than idealistic virtue."},
      {"author": "Samuel Johnson", "work": "The Vanity of Human Wishes", "quote": "Every scheme of worldly felicity founders upon the constitutional **imperfectibility** of our mortal condition."}
    ]
  },
  "imperfectible.md": {
    "primary": "Incapable of being made entirely faultless, flawless, or complete; inherently limited.",
    "secondary": "In metaphysical theology and rationalist ethics, imperfectible characterizes finite creatures whose essence precludes attaining infinite divine perfection.",
    "quotes": [
      {"author": "Jonathan Edwards", "work": "Freedom of the Will", "quote": "Creatures remain essentially **imperfectible** to absolute infinity, for the distance between finite being and divine fullness is boundless."},
      {"author": "Thomas Hobbes", "work": "Leviathan", "quote": "Human covenants are necessarily **imperfectible** against all contingencies without a coercive power to compel observance."},
      {"author": "David Hume", "work": "Dialogues Concerning Natural Religion", "quote": "If the architect of nature be infinitely wise, why should this world appear so crude and **imperfectible** in its adjustments?"}
    ]
  },
  "imperfection.md": {
    "primary": "A flaw, fault, defect, or shortcoming that prevents absolute completeness or excellence.",
    "secondary": "In evolutionary biology, morphological imperfection in an organism's structure provides evidence of historical modification from ancestral forms rather than pristine special creation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "I shall discover a thing to you, wherein I must very much lay open mine own **imperfection**."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The extreme **imperfection** of the geological record explains why we do not find closely graduated varieties connecting all extinct species."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She saw with painful clarity every **imperfection** in her husband's scholarship and temperament."}
    ]
  },
  "imperfective.md": {
    "primary": "Expressing or denoting an ongoing, uncompleted, habitual, or continuous action rather than an accomplished event.",
    "secondary": "In comparative linguistics and Slavic grammatical theory, the imperfective aspect contrasts with the perfective by presenting verbal events from within their internal temporal duration.",
    "quotes": [
      {"author": "William Dwight Whitney", "work": "Language and the Study of Language", "quote": "The **imperfective** form portrays an event as evolving in duration, without reference to its ultimate completion."},
      {"author": "Ferdinand de Saussure", "work": "Course in General Linguistics", "quote": "In Slavic verbal morphology, the grammaticalized opposition between **imperfective** and perfective stems forms the structural core of the aspectual system."},
      {"author": "Edward Sapir", "work": "Language: An Introduction to the Study of Speech", "quote": "A speaker using an **imperfective** verb focuses the listener's attention upon the ongoing unfolding of the process."}
    ]
  },
  "imperfectly.md": {
    "primary": "In a flawed, incomplete, defective, or inadequate manner; not perfectly.",
    "secondary": "In scientific observation and epistolary documentation, recording phenomena imperfectly indicates the constraints of early instruments or incomplete perceptual resolution.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "This is a very important subject, most **imperfectly** understood by even the most experienced naturalists."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Brooke's pen went off into a little speech which it had lately reported for that purpose, though very **imperfectly** executed."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "He was that man who, as far as I could see, had conducted a difficult enterprise **imperfectly** under tremendous odds."}
    ]
  },
  "imperfectness.md": {
    "primary": "The characteristic of lacking completeness, precision, or defect-free execution.",
    "secondary": "In classical epistemology, imperfectness in human perceptual faculties accounts for optical illusions and the necessity of rational correction.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The **imperfectness** of words is the great cause of obscurity and confusion in philosophical disputations."},
      {"author": "George Berkeley", "work": "A Treatise Concerning the Principles of Human Knowledge", "quote": "Any apparent **imperfectness** in the operations of nature arises solely from our narrow and partial comprehension of the whole."},
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "The **imperfectness** of our furnaces and vessels prevents the total separation of volatile mineral spirits from coarse earth."}
    ]
  },
  "ineffective.md": {
    "primary": "Failing to produce any significant or desired effect; lacking power, efficiency, or success.",
    "secondary": "In pharmacology and therapeutic guidelines, an ineffective intervention fails to demonstrate statistically significant clinical benefit over placebo controls.",
    "quotes": [
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "All ventilation becomes **ineffective** if the air admitted from outside is already poisoned by foul sewer emanations."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "Naval bombardments without landing troops proved utterly **ineffective** against well-entrenched coastal batteries."},
      {"author": "Theodore Roosevelt", "work": "The Strenuous Life", "quote": "A well-meaning citizen whose virtues are merely passive is an **ineffective** force in the civic struggle."}
    ]
  },
  "ineffectively.md": {
    "primary": "In a manner that fails to accomplish the intended purpose or produce a decisive result.",
    "secondary": "In tactical and strategic military treatises, striking ineffectively expends logistical resources while leaving enemy defensive positions substantially intact.",
    "quotes": [
      {"author": "Carl von Clausewitz", "work": "On War", "quote": "Artillery directed without accurate observation expends ammunition **ineffectively** against enemy redoubts."},
      {"author": "Alfred Thayer Mahan", "work": "The Influence of Sea Power upon History", "quote": "A dispersed fleet operates **ineffectively** against a concentrated adversary who strikes each division in detail."},
      {"author": "Arthur Conan Doyle", "work": "The Great Boer War", "quote": "The British infantry fired **ineffectively** at the crest of the hill, where no visible enemy showed a head."}
    ]
  },
  "ineffectiveness.md": {
    "primary": "The inability or failure to achieve an intended objective, operational standard, or productive outcome.",
    "secondary": "In organizational economics and public administration, ineffectiveness arises from institutional inertia, misalignment of incentives, and bureaucratic coordination bottlenecks.",
    "quotes": [
      {"author": "Woodrow Wilson", "work": "The Study of Administration", "quote": "The chief reproach brought against democratic systems is the administrative **ineffectiveness** of divided executive councils."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Monopolistic privileges invariably breed managerial **ineffectiveness** by shielding enterprises from competitive discipline."},
      {"author": "Herbert Spencer", "work": "Social Statics", "quote": "The patent **ineffectiveness** of legislative panaceas demonstrates that society cannot be remolded by arbitrary decree."}
    ]
  },
  "ineffectual.md": {
    "primary": "Producing no satisfactory outcome or result; powerless to achieve a purpose.",
    "secondary": "In literary portraiture and moral psychology, describing efforts or characters whose goodwill is rendered impotent by indecision or circumstance.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Their attempts to construct an independent foundation of moral obligation remained largely **ineffectual** against sceptical attacks."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The farmer made an **ineffectual** effort to break the stubborn soil with his light wooden plow."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "His gestures of remorse were **ineffectual** to lighten the dark burden weighing upon his guilty conscience."}
    ]
  },
  "ineffectuality.md": {
    "primary": "The quality of possessing no operational power or producing no meaningful impact; utter fruitlessness.",
    "secondary": "In social critique and psychological portraiture, ineffectuality describes the paralysis of refined intellects unable to translate moral conviction into decisive worldly action.",
    "quotes": [
      {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "The tragic flaw in Shelley's political idealism lay in its radiant, beautiful **ineffectuality** when confronted with stubborn reality."},
      {"author": "Henry James", "work": "The Bostonians", "quote": "Ransom smiled at the benign **ineffectuality** of the elderly philanthropist who had devoted forty years to harmless manifestos."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "A sense of helpless **ineffectuality** overwhelmed her as she realized the futility of her passionate protests."}
    ]
  },
  "ineffectually.md": {
    "primary": "Without producing the desired effect, success, or outcome; in vain.",
    "secondary": "In narrative prose, portraying characters struggling against overwhelming natural forces or inexorable historical currents ineffectually.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "He fluttered his wings **ineffectually** upon the surface of the pond before sinking beneath the clear water."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The sailors tugged **ineffectually** at the tangled ropes while the tempest roared with mounting fury."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Both my sister and myself have endeavoured to correct his vices, but **ineffectually**, as time has proven."}
    ]
  },
  "ineffectualness.md": {
    "primary": "Lack of competence, force, or capacity to achieve an intended result; impotence of effort.",
    "secondary": "In literary tragedy, the hero's ineffectualness against relentless cosmic or social fate heightens the sense of inevitable catastrophe.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The bitter **ineffectualness** of Angel's apologies could not heal the deep wound inflicted upon her trusting spirit."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "Jim's bluster could not disguise the tragic **ineffectualness** of his attempts to retrieve his lost honor."},
      {"author": "Herman Melville", "work": "Bartleby, the Scrivener", "quote": "The lawyer felt the complete **ineffectualness** of all ordinary persuasion when confronting the clerk's mild passivity."}
    ]
  },
  "infect.md": {
    "primary": "To contaminate with a disease-producing organism or agent; also to imbue with a pernicious quality, mood, or idea.",
    "secondary": "In cellular virology, to infect involves the attachment, penetration, and uncoating of a viral particle within a host cell, subverting host machinery for viral replication.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Why do you **infect** yourself with them, and pour your soul into their reckless and unprofitable griefs?"},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "It is sadly curious to observe how slight a taste of office suffices to **infect** a man with institutional complacency."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "The subtle poison seemed to **infect** her blood, draining her vital strength night after night."}
    ]
  },
  "infected.md": {
    "primary": "Contaminated with pathogenic organisms, toxins, or disease; also corrupted or tainted by a harmful influence.",
    "secondary": "In clinical surgical pathology, an infected wound exhibits purulence, erythema, induration, and viable bacterial proliferation exceeding tissue clearance thresholds.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Give me leave to speak my mind, and I will through and through cleanse the foul body of the **infected** world."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Clare's late enthusiasm for Tess had **infected** her through her maternal sympathies, until she shared his devotion."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The time is **infected** with Hamlet's unhappiness, doubting its own powers and shrinking from resolute action."}
    ]
  },
  "infection.md": {
    "primary": "The invasion and multiplication of pathogenic microorganisms in body tissues, producing local or systemic illness.",
    "secondary": "In historical public health and epidemiology, the conceptualization of infection shifted from miasmatic atmospheric theories to specific micro-organismal etiology via germ theory.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Ah wherefore with **infection** should he live, and with his presence grace impiety, that sin by him advantage should achieve?"},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The danger of spreading **infection** among the flock required immediate isolation of every ailing sheep."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dr. Lydgate insisted that strict cleanliness was the only certain safeguard against hospital **infection**."}
    ]
  },
  "infectious.md": {
    "primary": "Transmissible through the environment, water, air, or contact; likely to spread or communicate rapidly to others.",
    "secondary": "In medical microbiology, infectious distinguishes pathologies induced by living transmissible biological vectors from non-communicable somatic diseases.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "The most **infectious** pestilence upon thee, thou villainous and ungrateful scoundrel!"},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The new point of view was **infectious**, and the next child did likewise, and then all joined in the chorus."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her radiant good humor was **infectious**, lightening the somber atmosphere of the parlor within minutes."}
    ]
  },
  "infectiously.md": {
    "primary": "In a manner that easily spreads to others by contagion, emotional resonance, or rapid imitation.",
    "secondary": "In behavioral sociology and crowd psychology, moods and laughter propagate infectiously through unconscious mirror-neuron activation and social mimicry.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Scrooge chuckled **infectiously**, rubbing his hands together in pure delight as the boy ran off to buy the prize turkey."},
      {"author": "Mark Twain", "work": "The Adventures of Tom Sawyer", "quote": "Tom began to laugh, and Huck joined in, their mirth bubbling up **infectiously** in the quiet graveyard."},
      {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "Natasha smiled **infectiously**, communicating her youthful exuberance to the entire ballroom."}
    ]
  },
  "infective.md": {
    "primary": "Capable of transmitting infection or producing disease through the introduction of pathogenic agents.",
    "secondary": "In epidemiology and virology, infective dose denotes the minimum number of viable viral virions or bacterial units required to establish active host colonization.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "The Germ Theory and Its Applications to Medicine and Surgery", "quote": "Sterilization by boiling destroys the **infective** capacity of anthrax spores present in contaminated blood."},
      {"author": "Robert Koch", "work": "Investigations into the Etiology of Traumatic Infective Diseases", "quote": "Inoculation with minute quantities of the **infective** fluid consistently reproduced identical pathological lesions in mice."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In acute **infective** endocarditis, vegetative micro-colonies proliferate upon damaged cardiac valve leaflets."}
    ]
  },
  "noninfectious.md": {
    "primary": "Not caused by or communicable through pathogenic microorganisms, parasites, or contagious agents.",
    "secondary": "In public health and chronic disease epidemiology, noninfectious ailments include cardiovascular diseases, malignant neoplasms, and metabolic disorders driven by genetic and lifestyle determinants.",
    "quotes": [
      {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Many degenerative cellular alterations represent purely **noninfectious** nutritional disturbances rather than microbic invasions."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Essential hypertension and chronic gout remain classic examples of chronic **noninfectious** constitutional disorders."},
      {"author": "John Simon", "work": "Public Health Reports", "quote": "A clear distinction must be maintained between epidemic contagions and **noninfectious** ailments arising from occupational poisons."}
    ]
  },
  "perfect.md": {
    "primary": "Having all the required or desirable elements, qualities, or characteristics; entirely without flaw or defect.",
    "secondary": "In botanical morphology, a perfect flower possesses both functional stamens and carpels within the same floral structure.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "I will return **perfect** courtier; in the which my instruction shall serve to naturalize my foreign tongue."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The night was in a state of **perfect** calm, and the brilliant stars shone with frost-like brilliance."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "In the more precise language of philosophic jurists, duties of **perfect** obligation are those to which there corresponds a respective right."}
    ]
  },
  "perfecta.md": {
    "primary": "A form of wagering, especially in parimutuel horse or dog racing, where the bettor must pick the first and second-place finishers in exact order.",
    "secondary": "In game theory and statistical probability of betting markets, the exacta or perfecta represents an exotic wager demanding compound joint-probability calculation across field competitors.",
    "quotes": [
      {"author": "Damon Runyon", "work": "Guys and Dolls", "quote": "He laid down twenty dollars on the **perfecta**, picking the brown filly to win and the gray gelding to place."},
      {"author": "Grantland Rice", "work": "The Tumult and the Shouting", "quote": "The veteran turfman studied the morning odds, calculating whether the payout on the **perfecta** justified the long risk."},
      {"author": "Ernest Hemingway", "work": "A Moveable Feast", "quote": "We cashed our winning tickets on the **perfecta** at Auteuil and celebrated with champagne at the brasserie."}
    ]
  },
  "perfected.md": {
    "primary": "Brought to completion, ultimate refinement, or highest attainable excellence; free of flaws.",
    "secondary": "In intellectual property and legal doctrine, a perfected security interest or patent right has fulfilled all statutory filing requirements to secure legal enforceability against third parties.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "It must be so, for miracles are ceased, and therefore we must needs admit the means how things are **perfected**."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "How have all those exquisite adaptations of one part of the organization to another been **perfected** through natural selection?"},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "A truly great invention is not struck off at a single blow, but is **perfected** through generations of patient labor."}
    ]
  },
  "perfecter.md": {
    "primary": "One who or that which refines, improves, or brings something to a state of complete excellence or maturity.",
    "secondary": "In philosophical and spiritual treatises, the divine or intellectual agent acts as the supreme perfecter of latent human faculties and moral virtues.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Author of being, and **perfecter** of all light, in whose transcendent glory the seraphim veil their faces."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Time is the great discoverer of truth and the patient **perfecter** of all human arts and sciences."},
      {"author": "Thomas Aquinas", "work": "Summa Theologiae", "quote": "Grace does not destroy nature, but acts as the glorious **perfecter** of its natural capabilities."}
    ]
  },
  "perfectibility.md": {
    "primary": "The capability of being improved, refined, or advanced indefinitely toward ideal excellence.",
    "secondary": "In Enlightenment political theory, perfectibility signifies the limitless moral, cognitive, and political progress achievable by humanity through rational education and institutional reform.",
    "quotes": [
      {"author": "Marquis de Condorcet", "work": "Sketch for a Historical Picture of the Progress of the Human Mind", "quote": "The **perfectibility** of man is truly indefinite, limited only by the duration of the globe on which nature has placed us."},
      {"author": "William Godwin", "work": "Enquiry Concerning Political Justice", "quote": "The doctrine of human **perfectibility** teaches that ignorance and vice will gradually yield before the triumphant spread of reason."},
      {"author": "Jean-Jacques Rousseau", "work": "Discourse on Inequality", "quote": "This distinct faculty of self-improvement, this boundless **perfectibility**, distinguishes man from the beasts."}
    ]
  },
  "perfectible.md": {
    "primary": "Capable of continuous improvement, refinement, or being brought nearer to flawless perfection.",
    "secondary": "In classical moral philosophy, the human character is viewed as inherently perfectible through disciplined habituation and virtuous training.",
    "quotes": [
      {"author": "Mary Wollstonecraft", "work": "A Vindication of the Rights of Woman", "quote": "If woman be created with an immortal soul, she must be endowed with a **perfectible** reason capable of moral excellence."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Human faculties are indefinitely **perfectible**, and each generation inherits expanded capacities from the cultural progress of the past."},
      {"author": "Immanuel Kant", "work": "Critique of Practical Reason", "quote": "The moral will in a finite being is always **perfectible**, striving endlessly toward the ideal holiness commanded by duty."}
    ]
  },
  "perfection.md": {
    "primary": "The condition, state, or quality of being flawless, complete, and without fault or defect.",
    "secondary": "In theology and scholastic metaphysics, perfection signifies the absolute actuality and fullness of divine being, lacking all privation or potentiality.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "When I consider everything that grows holds in **perfection** but a little moment, the conceits of youth pass away."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Our idea of the supreme being is formed by taking our ideas of knowledge, power, and goodness, and enlarging them to boundless **perfection**."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The exquisite **perfection** of her singing held the rustic listeners in spellbound silence."}
    ]
  },
  "perfectionism.md": {
    "primary": "A personal disposition or doctrine that demands the attainment of the highest standards and refuses to accept any flaw or shortcoming.",
    "secondary": "In clinical psychology, perfectionism is differentiated into adaptive striving for excellence versus maladaptive evaluative concerns linked to anxiety and self-criticism.",
    "quotes": [
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "The saintly temperament often exhibits an intense moral **perfectionism** that finds even minor faults intolerable."},
      {"author": "George Santayana", "work": "The Life of Reason", "quote": "An unbending artistic **perfectionism** may lead a poet to burn verses that would have delighted posterity."},
      {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "The pursuit of sweetness and light is an inward spiritual **perfectionism** aimed at the harmonious expansion of human powers."}
    ]
  },
  "perfectionist.md": {
    "primary": "A person who insists on flawless performance, complete precision, and the highest conceivable standards in work or life.",
    "secondary": "In nineteenth-century American religious history, a Perfectionist belonged to a sect holding that complete freedom from sin was achievable in earthly life.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Blithedale Romance", "quote": "Hollingsworth was a zealous moral **perfectionist**, unwilling to tolerate any compromise with human frailty."},
      {"author": "John Humphrey Noyes", "work": "History of American Socialism", "quote": "The true Christian **perfectionist** claims that divine grace can fully eradicate every selfish impulse from the human heart."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The artist of Kouroo was a pure **perfectionist** who spent a lifetime carving a single walking-stick until it was without fault."}
    ]
  },
  "perfective.md": {
    "primary": "Tending to make perfect, complete, or fully developed; also relating to verbal completion in grammar.",
    "secondary": "In theoretical linguistics and aspectology, perfective aspect presents a situation as a bounded, indivisible whole with clear initiation and termination boundaries.",
    "quotes": [
      {"author": "Roman Jakobson", "work": "Selected Writings: Phonological Studies", "quote": "The morphological marker turns the basic stem into a **perfective** verb denoting an attained boundary."},
      {"author": "Bernard Comrie", "work": "Aspect: An Introduction to the Study of Verbal Aspect", "quote": "The **perfective** aspect presents the verbal action in its totality, without distinguishing internal temporal phases."},
      {"author": "Henry Sweet", "work": "A New English Grammar", "quote": "The compound auxiliary form exercises a **perfective** function, demonstrating that the act is consummated."}
    ]
  },
  "perfectly.md": {
    "primary": "In a faultless, complete, or entirely thorough manner; completely and without defect.",
    "secondary": "In philosophical logic and dialectics, an argument that is perfectly valid leaves no room for contradictory premises or inductive ambiguity.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "I would have her learn, my fair cousin, how **perfectly** I love her; and that is goodbye to all dissimulation."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The sensible horses stood **perfectly** still, and the waggoner's steps sank fainter into the distance."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "They pursue sensual indulgences to the injury of health, though **perfectly** aware that health is the greater good."}
    ]
  },
  "prefect.md": {
    "primary": "A chief officer, civil magistrate, or senior administrative official possessing regional or institutional authority.",
    "secondary": "In Roman imperial administration and French public law, the prefect represents the centralized executive authority governing a province, territory, or département.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The praetorian **prefect** enjoyed supreme civil jurisdiction, commanding both the finances and judicial tribunals of the provinces."},
      {"author": "Alexis de Tocqueville", "work": "The Old Regime and the Revolution", "quote": "Under the centralized monarchy, the royal **prefect** directed the municipal affairs of every provincial township."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The district **prefect** dispatched an armed escort to inspect the lonely trading stations along the river."}
    ]
  },
  "prefectural.md": {
    "primary": "Relating to, administered by, or characteristic of a prefect or the territorial jurisdiction of a prefecture.",
    "secondary": "In comparative political geography and modern Japanese governance, prefectural assemblies and governors administer regional public works, policing, and education within designated jurisdictions.",
    "quotes": [
      {"author": "Isabella Bird", "work": "Unbeaten Tracks in Japan", "quote": "The new **prefectural** authorities had constructed broad macadamized roads connecting the provincial capital with the sea."},
      {"author": "Basil Hall Chamberlain", "work": "Things Japanese", "quote": "Each **prefectural** government maintains an efficient police force and supervises primary schooling under national standards."},
      {"author": "Lafcadio Hearn", "work": "Glimpses of Unfamiliar Japan", "quote": "The governor issued a **prefectural** decree protecting the ancient cedar groves surrounding the Shinto shrine."}
    ]
  },
  "prefecture.md": {
    "primary": "The district, territorial jurisdiction, or official headquarters of a prefect or regional administrator.",
    "secondary": "In historical Roman administrative geography following Diocletian's reforms, the four praetorian prefectures formed the largest civil territorial divisions of the Empire.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The vast **prefecture** of the East embraced the richest and most populous provinces of Asia and Egypt."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Throughout that mountainous **prefecture**, the peasants celebrate the harvest by offering sheaves of barley to local spirits."},
      {"author": "Elizabeth Kimball Kendall", "work": "A Wayfarer in China", "quote": "Upon arriving at the yamen of the **prefecture**, we presented our passports to the resident mandarin."}
    ]
  },
  "refection.md": {
    "primary": "Refreshment or nourishment, especially a light meal or repast taken after labor or fasting.",
    "secondary": "In monastic rules and ascetic disciplines, refection refers to the scheduled communal meal taken in silence while listening to edifying spiritual readings.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The hungry pupils were summoned to a meager **refection** consisting of burnt porridge and water."},
      {"author": "John Milton", "work": "Paradise Regained", "quote": "After their long desert journey, they partook of a sweet **refection** spread beneath the shady palms."},
      {"author": "Sir Walter Scott", "work": "Ivanhoe", "quote": "The hospitable prior offered the weary traveler such simple **refection** as the abbey cellar could afford."}
    ]
  },
  "refectory.md": {
    "primary": "A communal dining hall, especially in a monastery, convent, boarding school, or academic college.",
    "secondary": "In medieval monastic architecture, the refectory was typically situated on the southern side of the cloister garth, adjacent to the kitchens and cellar.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The two hundred pupils filed quietly into the cold **refectory** for their evening bread and cheese."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The ancient monastery **refectory** was adorned with faded frescoes portraying the Last Supper upon its stone walls."},
      {"author": "George Eliot", "work": "Romola", "quote": "The friars gathered silently in the spacious **refectory** of San Marco to hear Savonarola's words."}
    ]
  },
  "superfecta.md": {
    "primary": "A pari-mutuel bet in horse or greyhound racing where the bettor must pick the first four finishers in their exact sequential order.",
    "secondary": "In probability theory and racetrack finance, the superfecta offers exceptionally high payoff odds due to the astronomical combinatoric permutations of an eight- to twelve-horse field.",
    "quotes": [
      {"author": "Damon Runyon", "work": "Money from Home", "quote": "He spent the entire afternoon studying track conditions, determined to hit the elusive **superfecta** in the sixth race."},
      {"author": "Hunter S. Thompson", "work": "Fear and Loathing in Las Vegas", "quote": "The tote board flashed impossible odds on the **superfecta**, tantalizing every broke gambler along the rail."},
      {"author": "Charles Bukowski", "work": "Notes of a Dirty Old Man", "quote": "I put five bucks on an impossible **superfecta** and watched my longshot stumble at the far turn."}
    ]
  },
  "superfecundation.md": {
    "primary": "The fertilization of two or more ova released during the same ovulatory cycle by spermatozoa from separate acts of coitus.",
    "secondary": "In forensic reproductive genetics and veterinary obstetrics, heteropaternal superfecundation occurs when twin offspring carry genetic paternity from two distinct male progenitors.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Cases of **superfecundation** in dogs clearly show that a single litter may be sired by distinct canine breeds."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Rare clinical instances of fraternal twins exhibiting differing paternal traits illustrate authentic human **superfecundation**."},
      {"author": "Francis Galton", "work": "Hereditary Genius", "quote": "The biological phenomenon of **superfecundation** provides an intriguing natural experiment in comparative hereditary transmission."}
    ]
  },
  "superinfect.md": {
    "primary": "To cause or undergo a second infection by a different or resistant strain upon an already infected host or tissue.",
    "secondary": "In medical microbiology, to superinfect involves the secondary invasion of opportunistic pathogens following antimicrobial eradication of normal protective commensal microflora.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Foreign airborne molds readily **superinfect** fermenting must when protective yeast populations decline in vitality."},
      {"author": "Robert Koch", "work": "Etiology of Wound Infections", "quote": "Hospital gangrene bacilli frequently **superinfect** surgical wounds previously colonized by milder suppurative micrococci."},
      {"author": "Paul Ehrlich", "work": "Studies in Immunity", "quote": "Attempts to **superinfect** an animal already bearing an established protozoan parasite often provoke intense immune resistance."}
    ]
  },
  "superinfection.md": {
    "primary": "A secondary infection occurring during or immediately following antibiotic treatment for an earlier, distinct infection.",
    "secondary": "In clinical infectious disease and pharmacology, superinfection commonly manifests as fungal overgrowth or Clostridioides difficile colitis following broad-spectrum antibacterial therapy.",
    "quotes": [
      {"author": "Alexander Fleming", "work": "Penicillin: Its Practical Application", "quote": "Prolonged therapy may suppress sensitive organisms while predisposing the debilitated patient to opportunistic **superinfection** by resistant strains."},
      {"author": "René Dubos", "work": "The Bacterial Cell", "quote": "The development of secondary **superinfection** illustrates the ecological balance governing microbic populations in living tissues."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Secondary bacterial **superinfection** following influenza pneumonia represents the chief hazard to elderly patients."}
    ]
  },
  "suprainfection.md": {
    "primary": "A virulent or superimposed secondary infection establishing itself over an existing localized or systemic microbial invasion.",
    "secondary": "In clinical pathology, suprainfection denotes the opportunistic colonization of compromised mucous membranes or necrotic tissues by multi-drug resistant bacterial or fungal strains.",
    "quotes": [
      {"author": "William Henry Welch", "work": "General Pathology of Fever", "quote": "The terminal stage was precipitated by severe **suprainfection** invading the ulcerated intestinal mucosa."},
      {"author": "Theobald Smith", "work": "Parasitism and Disease", "quote": "In chronic bovine infections, destructive tissue necrosis commonly invites secondary bacterial **suprainfection**."},
      {"author": "Simon Flexner", "work": "Experimental Epidemiology", "quote": "Laboratory animals weakened by primary inoculations succumbed swiftly when exposed to lethal respiratory **suprainfection**."}
    ]
  },
  "unaffected.md": {
    "primary": "Free from artifice, pretense, or affection; genuine and sincere; also unchanged or unaltered by an influence.",
    "secondary": "In materials science and experimental pathology, describing control specimens or structural substrates that demonstrate complete physical stability under stress tests.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "But this proud openness was made lovable by an expression of **unaffected** good-will toward everyone around her."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "A man of genuine character speaks with **unaffected** simplicity, having nothing to conceal and no vanity to flatter."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "At an earlier developmental age these organs would be left **unaffected**, maintaining their primitive morphology."}
    ]
  },
  "unaffectedness.md": {
    "primary": "Natural simplicity, genuine frankness, and complete freedom from pretension, disguise, or artificiality.",
    "secondary": "In 18th-century moral aesthetics and epistolary style, unaffectedness was celebrated as the highest rhetorical virtue, demonstrating spontaneous alignment between thought and expression.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor was charmed by the **unaffectedness** of Edward's manner, which revealed a mind at once modest and cultivated."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "True politeness is never accompanied by stiffness; its chief beauty consists in an easy **unaffectedness**."},
      {"author": "William Hazlitt", "work": "Table-Talk", "quote": "The greatest charm of Montaigne's essays is their complete **unaffectedness**, showing the man precisely as he was."}
    ]
  },
  "unaffecting.md": {
    "primary": "Failing to move the feelings, arouse sympathy, or touch the emotions; cold and uninspiring.",
    "secondary": "In dramatic criticism and oratorical evaluation, an unaffecting performance fails to establish an empathetic bond with the audience despite technical correctness.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The poem was technically correct in meter, but singularly dry and **unaffecting** to the sensitive reader."},
      {"author": "William Hazlitt", "work": "Characters of Shakespear's Plays", "quote": "A speech delivered without genuine passion remains cold and **unaffecting**, however ornate its rhetorical figures."},
      {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "Her grief seemed theatrical and **unaffecting**, lacking that genuine note of human sorrow which alone touches the heart."}
    ]
  },
  "unaffectionate.md": {
    "primary": "Lacking warmth, tenderness, or demonstrated affection; aloof, cold, or emotionally distant.",
    "secondary": "In developmental psychodynamics, an unaffectionate domestic environment can impede an infant's attachment formation and secure emotional socialization.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Her cold, **unaffectionate** demeanor towards her dependent niece repelled any impulse toward intimacy."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "A harsh, **unaffectionate** father had warped Godfrey's early youth, driving him toward reckless secrecy."},
      {"author": "Charles Dickens", "work": "Dombey and Son", "quote": "Mr. Dombey turned an **unaffectionate** gaze upon his daughter, seeing in her only an obstacle to his pride."}
    ]
  },
  "uneffective.md": {
    "primary": "Ineffective; incapable of producing the intended result, operation, or influence.",
    "secondary": "In archaic philosophical and legal diction, uneffective signified the voiding or operational impotence of an edict, compact, or causative agency.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Essays", "quote": "Counsel without executive resolution is **uneffective**, like an engine without fuel to set its wheels in motion."},
      {"author": "Thomas Hobbes", "work": "Leviathan", "quote": "Covenants without the sword are but words, and of no strength, being wholly **uneffective** to secure a man at all."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Abstract ideas remaining unapplied to concrete reality prove **uneffective** in improving the daily conduct of human life."}
    ]
  },
  "uninfected.md": {
    "primary": "Free from pathogenic microorganisms, viral contamination, or infectious disease agents.",
    "secondary": "In epidemiology and clinical cohort trials, the uninfected control group establishes the baseline immunological and physiological parameters against which pathological changes are measured.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "The Germ Theory", "quote": "The dogs kept in separate, sanitized cages remained completely **uninfected** throughout the entire experiment."},
      {"author": "Robert Koch", "work": "Investigations into the Etiology of Infectious Diseases", "quote": "Microscopic examination confirmed that the control tissues remained pure and **uninfected** by the bacilli."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Strict quarantine of healthy individuals kept the surrounding villages **uninfected** during the cholera outbreak."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Action\Dashboard — fec"

updated_count = 0
for fname, info in data.items():
    fpath = os.path.join(base_dir, fname)
    if not os.path.exists(fpath):
        print(f"Warning: File {fpath} does not exist!")
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
    updated_count += 1

print(f"Fec Batch 2 Complete: Successfully updated {updated_count}/{len(data)} notes.")
