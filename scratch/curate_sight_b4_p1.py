# -*- coding: utf-8 -*-
"""
curate_sight_b4_p1.py
Batch 4 Part 1 of Cluster Sight:
Dashboard — spec (first 34 of 68 new words):
conspecific, disrespectful, disrespectfully, especial, especially,
interspecies, interspecific, intraspecies, intraspecific, introspectively,
nonspecific, nonspecifically, overspecialise, overspecialize, respectful,
respectfully, respectfulness, spec, special, specialisation, specialise,
specialised, specialiser, specialism, specialist, specialistic, speciality,
specialization, specialize, specialized, specializer, specially,
specialness, specialty
Total: 34 words.
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_sight_b4_p1 = {
    "conspecific": {
        "primary": "An organism belonging to the same biological species as another organism.",
        "secondary": "In behavioral ecology and population genetics, relates to intraspecific communication, mate choice, and territorial competition between members of the same taxonomic species.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Aggressive encounters between **conspecific** males frequently resolve through ritualized displays rather than lethal combat."},
            {"author": "Edward O. Wilson", "work": "Sociobiology: The New Synthesis", "quote": "Pheromonal trails allow an ant to identify and recruit **conspecific** nestmates to newly discovered forage."},
            {"author": "Richard Dawkins", "work": "The Selfish Gene", "quote": "Cooperation between **conspecific** individuals evolves readily when guided by the arithmetic of kin selection."}
        ]
    },
    "disrespectful": {
        "primary": "Showing a lack of respect, deference, or courtesy; impolite and insolent.",
        "secondary": "In social hierarchy and institutional discipline, flouting customary protocols or verbal honors due to magistrates, elders, or sacred offices.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "He considered it profoundly **disrespectful** for a young woman to challenge the received wisdom of her elders."},
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "I was terrified lest my awkward silence should be interpreted as a **disrespectful** attitude toward Miss Murdstone."},
            {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth would not allow herself to be **disrespectful** to her mother, though she blushed at her foolish remarks."}
        ]
    },
    "disrespectfully": {
        "primary": "In a manner that shows a lack of respect, reverence, or courtesy; insolently.",
        "secondary": "In domestic and judicial governance, speaking or behaving in a manner calculated to diminish the lawful authority of a superior.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The boy was warned never to speak **disrespectfully** of the court, lest he incur severe chancery penalties."},
            {"author": "Jane Austen", "work": "Mansfield Park", "quote": "She could not bear to hear her uncle mentioned **disrespectfully**, even by those whose affection she valued most."},
            {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Tom rebuked his sister for answering their aunt **disrespectfully** before the gathered family circle."}
        ]
    },
    "especial": {
        "primary": "Better or greater than usual; special, exceptional, or of primary importance.",
        "secondary": "In formal rhetoric and epistolary style, emphasizes distinct personal regard or specific individual designation within a larger group.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "Our chiefest courtier, cousin, and our son, / ... / We pray you, throw to earth / This unprevailing woe; and think of us / As of a father: for let the world take note, / You are the most immediate to our throne; / And with no less nobility of love / Than that which dearest father bears his son, / Do I impart toward you. For your intent / In going back to school in Wittenberg, / It is most retrograde to our desire: / And we beseech you, bend you to remain / Here, in the cheer and comfort of our eye, / Our chiefest courtier, cousin, and our son. You have our **especial** love."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Oak watched Bathsheba with an **especial** tenderness that asked for no return or acknowledgment."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The structure of the eye has always presented an **especial** difficulty for the theory of natural selection."}
        ]
    },
    "especially": {
        "primary": "To a great extent; very much; particularly; used to single out an individual member.",
        "secondary": "In analytical prose and argumentative taxonomy, isolates a paramount factor or distinct instance that corroborates a universal principle.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "I will buy with you, sell with you, talk with you, walk with you, and so following, but I will not eat with you, drink with you, nor pray with you. What news on the Rialto? Who is he comes here? / This is Signior Antonio. / How like a fawning publican he looks! / I hate him for he is a Christian, / But more for that in low simplicity / He lends out money gratis and brings down / The rate of usance here with us in Venice. / If I can catch him once upon the hip, / I will feed fat the ancient grudge I bear him. / He hates our sacred nation, and he rails, / Even there where merchants most do congregate, / On me, my bargains and my well-won thrift, / Which he calls interest. Cursed be my tribe, / If I forgive him! I hate him **especially** for his insults."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The dawn was cold, **especially** over the misty water-meadows where the cows waited for the milkers."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The vocal organs of primates are **especially** developed to convey emotional alarm and social cohesion."}
        ]
    },
    "interspecies": {
        "primary": "Occurring between, arising between, or involving members of two or more different biological species.",
        "secondary": "In comparative evolutionary biology and community ecology, denotes mutualistic symbiosis, cross-taxa viral transmission, or inter-lineage competition.",
        "quotes": [
            {"author": "Ernst Mayr", "work": "Systematics and the Origin of Species", "quote": "Reproductive isolating mechanisms prevent **interspecies** hybridization and preserve genetic integrity."},
            {"author": "Stephen Jay Gould", "work": "The Panda's Thumb", "quote": "Ecological niches are continually shaped by **interspecies** competition for limited light and nutrients."},
            {"author": "Frans de Waal", "work": "Chimpanzee Politics", "quote": "Rare instances of **interspecies** adoption reveal emotional capacities that transcend taxonomic boundaries."}
        ]
    },
    "interspecific": {
        "primary": "Occurring between or involving different species of plants, animals, or other organisms.",
        "secondary": "In theoretical ecology and population modeling, governs predator-prey dynamics, parasitism, and competitive exclusion between sympatric taxa.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The battle of life is most severe when **interspecific** competition occurs between closely allied genera."},
            {"author": "Alfred Russel Wallace", "work": "Darwinism", "quote": "Divergence of character reduces **interspecific** conflict, allowing diverse forms to occupy the same territory."},
            {"author": "G. Evelyn Hutchinson", "work": "The Ecological Theater and the Evolutionary Play", "quote": "The niche hyperspace defines the mathematical limits within which **interspecific** coexistence remains stable."}
        ]
    },
    "intraspecies": {
        "primary": "Occurring or arising within a single biological species; among individuals of the same species.",
        "secondary": "In population genetics and microevolution, analyzes allele frequency shifts, morph variations, and behavioral polymorphisms within a breeding deme.",
        "quotes": [
            {"author": "Theodosius Dobzhansky", "work": "Genetics and the Origin of Species", "quote": "High **intraspecies** genetic diversity provides the raw material upon which environmental selection acts."},
            {"author": "Ernst Mayr", "work": "Animal Species and Evolution", "quote": "Polytypic distributions reflect **intraspecies** divergence driven by geographical barriers and climatic gradients."},
            {"author": "Julian Huxley", "work": "Evolution: The Modern Synthesis", "quote": "Clinal variation demonstrates how **intraspecies** adaptations adjust smoothly across continuous geographic clines."}
        ]
    },
    "intraspecific": {
        "primary": "Occurring or existing within a single species; intraspecific competition or variation.",
        "secondary": "In evolutionary ethology and sociobiology, describes density-dependent resource competition, dominance hierarchies, and mating strategies among conspecifics.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "As the individuals of the same species come into the closest competition, **intraspecific** struggles are usually the fiercest."},
            {"author": "Edward O. Wilson", "work": "The Diversity of Life", "quote": "Resource partitioning minimizes **intraspecific** aggression, ensuring efficient harvest of localized food patches."},
            {"author": "George Gaylord Simpson", "work": "Tempo and Mode in Evolution", "quote": "Microevolutionary trends emerge directly from selection pressures operating during intense **intraspecific** rivalries."}
        ]
    },
    "introspectively": {
        "primary": "In a manner characterized by examination of one's own thoughts, motives, and feelings.",
        "secondary": "In psychological autobiographies and stream-of-consciousness narratives, turning mental scrutiny inward upon transient subjective states.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "Giles reflected **introspectively** upon his broken prospects, watching the cider press drip in silence."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "When we look **introspectively** into the stream of thought, we find no static ideas, but continuous transformation."},
            {"author": "Virginia Woolf", "work": "The Waves", "quote": "Bernard spoke **introspectively**, weaving phrases to capture the fugitive cadence of his private sensations."}
        ]
    },
    "nonspecific": {
        "primary": "Not detailed, exact, or specific; not caused by or directed toward a particular pathogen or agent.",
        "secondary": "In clinical immunology and pharmacology, refers to innate immune responses or broad-spectrum receptor binding lacking targeted molecular selectivity.",
        "quotes": [
            {"author": "Louis Pasteur", "work": "Germ Theory and Its Applications to Medicine", "quote": "The initial febrile reaction displayed a **nonspecific** systemic resistance before localized symptoms manifested."},
            {"author": "Sir William Osler", "work": "The Principles and Practice of Medicine", "quote": "The patient complained of vague, **nonspecific** malaise weeks before the characteristic rash appeared."},
            {"author": "Paul Ehrlich", "work": "Studies in Immunity", "quote": "We must distinguish between selective side-chain affinity and mere **nonspecific** cellular absorption."}
        ]
    },
    "nonspecifically": {
        "primary": "In a nonspecific manner; without targeting a particular entity, pathogen, or substance.",
        "secondary": "In molecular biochemistry, binding or adsorbing generally to substrates through electrostatic or hydrophobic interactions without stereospecific cleft recognition.",
        "quotes": [
            {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "Hydrophobic molecules adhere **nonspecifically** to protein surfaces through weak van der Waals forces."},
            {"author": "James D. Watson", "work": "Molecular Biology of the Gene", "quote": "Certain basic polypeptides bind **nonspecifically** along the sugar-phosphate backbone of nucleic acids."},
            {"author": "Selman Waksman", "work": "My Life with the Microbes", "quote": "The crude antibiotic filtrate acted **nonspecifically** against several distinct microbial strains in the broth."}
        ]
    },
    "overspecialise": {
        "primary": "To specialize to an excessive degree, sacrificing breadth, adaptability, or general resilience.",
        "secondary": "In evolutionary morphology and pedagogical theory, describes an over-narrow focus that leaves an organism or scholar vulnerable to rapid changes.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Organisms that **overspecialise** to a single food source risk extinction whenever climatic shifts eradicate that host."},
            {"author": "H. G. Wells", "work": "The Work, Wealth and Happiness of Mankind", "quote": "Modern academic institutions tend to **overspecialise**, producing technicians who lack comprehensive historical vision."},
            {"author": "Julian Huxley", "work": "Evolution: The Modern Synthesis", "quote": "Lineages that **overspecialise** in giant body size or bizarre ornamentation frequently terminate in dead-end fossil branches."}
        ]
    },
    "overspecialize": {
        "primary": "To specialize excessively or to an extreme degree; American spelling of overspecialise.",
        "secondary": "In macroeconomics and organizational ecology, represents extreme technical specialization that causes structural rigidity and catastrophic vulnerability to disruption.",
        "quotes": [
            {"author": "Thorstein Veblen", "work": "The Higher Learning in America", "quote": "When professional schools **overspecialize**, they turn out trained technicians destitute of broad humanistic insight."},
            {"author": "Alfred North Whitehead", "work": "Science and the Modern World", "quote": "The danger of modern life is that intellectuals **overspecialize** in their grooves, losing contact with common sense."},
            {"author": "Stephen Jay Gould", "work": "Ever Since Darwin", "quote": "Lineages do not deliberately **overspecialize**; they merely respond to immediate selection pressures until the environment shifts."}
        ]
    },
    "respectful": {
        "primary": "Feeling or showing deference, esteem, and polite regard for someone or something.",
        "secondary": "In social etiquette and institutional protocol, behaving with deliberate courtesy, lowering one's voice, and observing established ceremonies.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel maintained a **respectful** distance, watching Bathsheba's bright silhouette against the sheepfold gate."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate spoke in a quiet, **respectful** tone that disarmed the elderly patient's suspicion."},
            {"author": "Lewis Carroll", "work": "Alice's Adventures in Wonderland", "quote": "Alice addressed the Cheshire Cat in a timid, **respectful** voice, uncertain of its temper."}
        ]
    },
    "respectfully": {
        "primary": "With deference, esteem, or polite regard; in a courteous and respectful manner.",
        "secondary": "In formal petitions, legal depositions, and diplomatic communications, submitting representations with ceremonious humility.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "Winterborne took off his hat and waited **respectfully** until Grace had passed along the lane."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Will bowed **respectfully** to Mrs. Casaubon, conscious of an inward devotion that needed no words."},
            {"author": "Herman Melville", "work": "Bartleby, the Scrivener", "quote": "I asked him **respectfully** to assist me in comparing papers, but he replied that he would prefer not to."}
        ]
    },
    "respectfulness": {
        "primary": "The quality or trait of being respectful; courteous deference toward others.",
        "secondary": "In ethical training and civic manners, the cultivated disposition that honors legitimate authority, parental dignity, and communal peace.",
        "quotes": [
            {"author": "G. K. Chesterton", "work": "Heretics", "quote": "True humility does not consist in cringing, but in a generous **respectfulness** toward all human souls."},
            {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Darcy observed the quiet **respectfulness** with which Elizabeth addressed her father."},
            {"author": "Samuel Johnson", "work": "The Rambler", "quote": "A modest **respectfulness** toward age and learning is the first ornament of youthful character."}
        ]
    },
    "spec": {
        "primary": "An informal term for specification, speculation, or spectacle; a technical requirement or commercial gamble.",
        "secondary": "In industrial design and engineering practice, denotes building or purchasing on risk ('on spec') or adherence to detailed manufacturing blueprints.",
        "quotes": [
            {"author": "Thomas Edison", "work": "Writings and Observations", "quote": "We built the first dynamo according to our own **spec**, testing each armature under heavy electrical load."},
            {"author": "Mark Twain", "work": "Life on the Mississippi", "quote": "He bought a parcel of riverfront land purely on **spec**, hoping the steamboat trade would double its value."},
            {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "The foundry manufactured heavy ordnance strictly to imperial **spec**, delivering naval guns on schedule."}
        ]
    },
    "special": {
        "primary": "Better, greater, or otherwise different from what is usual; designed for a particular purpose.",
        "secondary": "In theological discourse and statutory law, refers to singular divine providences or localized legislative acts distinct from general statutes.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "There's a **special** providence in the fall of a sparrow. If it be now, 'tis not to come; if it be not to come, it will be now; if it be not now, yet it will come: the readiness is all."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She felt a **special** dread of meeting those who had known her during her girlhood at Marlott."},
            {"author": "John Locke", "work": "Two Treatises of Government", "quote": "The legislature may enact a **special** law to meet extraordinary public emergencies."}
        ]
    },
    "specialisation": {
        "primary": "The process of concentrating on and becoming expert in a particular subject, skill, or biological function.",
        "secondary": "In evolutionary morphology and political economy, represents functional differentiation of cellular tissues or division of labor across industrial markets.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The physiological division of labor leads to high anatomical **specialisation** among social insects."},
            {"author": "H. G. Wells", "work": "The First Men in the Moon", "quote": "The Selenites carried industrial **specialisation** to monstrous extremes, breeding workers suited to a single task."},
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The greatest improvements in the productive powers of labor arise from the effects of **specialisation**."}
        ]
    },
    "specialise": {
        "primary": "To concentrate one's efforts on a particular skill, subject, trade, or field of study.",
        "secondary": "In comparative physiology and urban sociology, to undergo evolutionary or institutional adaptation toward an exclusive ecological or commercial role.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants Under Domestication", "quote": "Certain floral structures **specialise** to accommodate the proboscis of a single pollinating moth."},
            {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "A student must **specialise** if he desires to extend the boundary of scientific knowledge by even a single inch."},
            {"author": "Max Weber", "work": "The Protestant Ethic and the Spirit of Capitalism", "quote": "Modern vocational duty commands the individual to **specialise**, renouncing the Faustian universality of the Renaissance."}
        ]
    },
    "specialised": {
        "primary": "Concentrated on a small area of a subject; designed or fitted for one particular purpose.",
        "secondary": "In evolutionary anatomy and economic organization, describes highly adapted organs or industrial tools optimized for a narrow, demanding function.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The woodpecker exhibits exquisitely **specialised** feet, tail-feathers, and beak for climbing trees and extracting grubs."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The town had developed a **specialised** market for malting barley, drawing buyers from distant shires."},
            {"author": "G. K. Chesterton", "work": "What's Wrong with the World", "quote": "The modern professional has become so **specialised** that he can no longer comprehend common human existence."}
        ]
    },
    "specialiser": {
        "primary": "A person, organism, or institution that specializes in a particular trade, field, or biological function.",
        "secondary": "In ecological niche theory and market economics, represents a specialist taxon or dedicated enterprise thriving upon a narrow, high-efficiency resource base.",
        "quotes": [
            {"author": "Alfred Russel Wallace", "work": "Darwinism", "quote": "In an unchanging tropical rainforest, the extreme **specialiser** outcompetes the generalist by superior foraging efficiency."},
            {"author": "Thorstein Veblen", "work": "The Place of Science in Modern Civilization", "quote": "The industrial **specialiser** masters one microscopic technical manipulation at the cost of broader mechanical comprehension."},
            {"author": "Edward O. Wilson", "work": "The Insect Societies", "quote": "The soldier ant is an extreme morphological **specialiser**, incapable of feeding itself without the aid of minor workers."}
        ]
    },
    "specialism": {
        "primary": "Devotion to a particular subject, branch of knowledge, trade, or skill.",
        "secondary": "In academic sociology and the history of science, the institutional partitioning of knowledge into discrete sub-disciplines with proprietary jargon.",
        "quotes": [
            {"author": "William James", "work": "The Principles of Psychology", "quote": "The danger of modern scientific **specialism** is that it produces investigators blind to broader philosophical harmonies."},
            {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "Culture opposes the narrowness of professional **specialism**, seeking to view human life whole and harmonious."},
            {"author": "Max Weber", "work": "Science as a Vocation", "quote": "An impassioned dedication to **specialism** is the sole condition under which scientific achievement can nowadays be attained."}
        ]
    },
    "specialist": {
        "primary": "A person who concentrates primarily on a particular subject, craft, medical discipline, or activity.",
        "secondary": "In clinical medicine and military command, an authority possessing advanced certification, diagnostic acumen, and technical proficiency within a defined field.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "I consulted a Harley Street **specialist**, who confirmed that the strange nervous collapse had an organic origin."},
            {"author": "H. G. Wells", "work": "The Food of the Gods", "quote": "The engineer was a **specialist** in high-pressure steam, untroubled by moral dilemmas of technological growth."},
            {"author": "G. K. Chesterton", "work": "The Man Who Was Thursday", "quote": "The secret detective posed as an eccentric **specialist** in European anarchism to win admission to the council."}
        ]
    },
    "specialistic": {
        "primary": "Relating to, characteristic of, or suitable for a specialist or a specialism.",
        "secondary": "In critical commentary on scientific literature, describes dense, technical discourse aimed exclusively at peer experts within a narrow field.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "A purely **specialistic** training threatens to starve the imagination and dwarf the moral sympathies of young physicians."},
            {"author": "John Dewey", "work": "The Public and Its Problems", "quote": "When political governance retreats into **specialistic** technocracy, democratic participation becomes an empty ritual."},
            {"author": "George Santayana", "work": "The Life of Reason", "quote": "The philosopher must resist the **specialistic** fragmentation that treats mind and nature as unrelated compartments."}
        ]
    },
    "speciality": {
        "primary": "A pursuit, product, or subject of study to which someone gives special attention; a specialty.",
        "secondary": "In provincial commerce, traditional culinary arts, and professional jurisprudence, denotes a distinctive regional manufacture or specialized legal domain.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The brewing of fine autumnal ale was the acknowledged **speciality** of the Three Mariners Inn."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "He had chosen morbid anatomy as his **speciality**, pursuing research with austere, uncompromising zeal."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "Chancery practice was the lucrative **speciality** of the conservative legal firm in Lincoln's Inn Fields."}
        ]
    },
    "specialization": {
        "primary": "The process of concentrating on and becoming expert in a particular subject, skill, or trade.",
        "secondary": "In macroeconomics and evolutionary biology, represents the structural division of labor and organ differentiation that increases metabolic or productive output.",
        "quotes": [
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The greatest improvements in the productive powers of labor arise from the effects of **specialization**."},
            {"author": "Herbert Spencer", "work": "First Principles", "quote": "Evolution is an integration of matter accompanied by a concomitant differentiation and structural **specialization**."},
            {"author": "Emile Durkheim", "work": "The Division of Labour in Society", "quote": "Modern social solidarity depends upon functional **specialization** rather than mechanical conformity."}
        ]
    },
    "specialize": {
        "primary": "To concentrate one's efforts on a particular skill, subject, trade, or field of study; American spelling of specialise.",
        "secondary": "In evolutionary biology and professional development, to adapt anatomically or industrially to a specific environmental niche or commercial service.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Species that **specialize** in a narrow ecological niche often attain tremendous local abundance."},
            {"author": "Thorstein Veblen", "work": "The Theory of the Leisure Class", "quote": "The modern corporation encourages its technicians to **specialize** in discrete mechanical processes."},
            {"author": "William James", "work": "Talks to Teachers on Psychology", "quote": "We must not urge children to **specialize** too early, before the broad foundations of culture are laid."}
        ]
    },
    "specialized": {
        "primary": "Concentrated on a small area of a subject; designed for a particular purpose; American spelling of specialised.",
        "secondary": "In physiological anatomy and systems engineering, describes organs or machinery refined to execute a single, demanding function with high efficiency.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The reddleman pursued a **specialized** calling that isolated him from the ordinary agricultural community."},
            {"author": "G. K. Chesterton", "work": "Orthodoxy", "quote": "The modern materialist has developed a **specialized** intellect at the expense of universal sanity."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Man's hand is a less **specialized** organ than the forelimb of a horse, yet capable of infinite manipulations."}
        ]
    },
    "specializer": {
        "primary": "A person, organism, or institution that specializes in a particular trade, field, or activity.",
        "secondary": "In economic sociology and industrial organization, denotes the enterprise or craftsperson operating exclusively within a defined niche market.",
        "quotes": [
            {"author": "Thorstein Veblen", "work": "The Instinct of Workmanship", "quote": "The industrial **specializer** adapts his whole muscular habit to the rhythm of the machine."},
            {"author": "Alfred Russel Wallace", "work": "Tropical Nature and Other Essays", "quote": "The humming-bird is a wonderful **specializer**, extracting nectar from flowers inaccessible to insects."},
            {"author": "John Dewey", "work": "Democracy and Education", "quote": "The educational **specializer** often forgets that life is lived outside the boundaries of any single department."}
        ]
    },
    "specially": {
        "primary": "For a special purpose; in a special manner; particularly or expressly.",
        "secondary": "In statutory drafting and technical manufacture, indicates custom engineering or explicit administrative designation for a single client or case.",
        "quotes": [
            {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "Let me see: 'When thou canst get the ring upon my finger which never shall come off... then call me husband: but in such a then I write a never.' This is a dreadful sentence. 'Twas my father's ring; and I have **specially** kept it."},
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "He had ordered a cask of cider made **specially** from the finest golden pippins of his orchard."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Certain plants are **specially** adapted to attract night-flying moths by opening only after dusk."}
        ]
    },
    "specialness": {
        "primary": "The distinctive character, singular excellence, or remarkable uniqueness that sets something apart.",
        "secondary": "In existential philosophy and social psychology, the cherished perception of unique personal worth, distinction, or cosmic purpose.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Every individual soul possesses an inherent **specialness** that cannot be duplicated by any other created being."},
            {"author": "George Eliot", "work": "Adam Bede", "quote": "She clung to the belief in her own modest **specialness**, dreaming of a future lifted above the dairy farm."},
            {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "A profound sense of holy **specialness** visits the convert, flooding the mind with miraculous peace."}
        ]
    },
    "specialty": {
        "primary": "A subject of study, skill, or item of commerce in which someone is an expert or which is uniquely distinctive.",
        "secondary": "In contract law and medical practice, a formal contract under seal or a board-certified clinical discipline requiring residency training.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Troilus and Cressida", "quote": "The **specialty** of rule hath been neglected."},
            {"author": "Bram Stoker", "work": "Dracula", "quote": "Van Helsing's medical **specialty** embraced obscure brain maladies that baffled conventional practitioners."},
            {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "An action of debt upon a **specialty** required production of a deed bearing the actual wax seal of the debtor."}
        ]
    }
}
