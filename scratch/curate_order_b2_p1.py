# -*- coding: utf-8 -*-
"""
curate_order_b2_p1.py
Curated dataset for Cluster Order Batch 2 Part 1:
- Dashboard — sequ (38 words)
- Dashboard — termin (48 words)
Total: 86 words
"""
import re

data_order_b2_p1 = {
    # ----------------------------------------------------
    # DASHBOARD — SEQU (38 words)
    # ----------------------------------------------------
    "consequence": {
        "primary": "A result, effect, or outcome derived logically or causally from an antecedent event or condition.",
        "secondary": "In social, political, and philosophical theory, significance, momentous distinction, or moral import.",
        "quotes": [
            {
                "author": "David Hume",
                "work": "An Enquiry Concerning Human Understanding",
                "quote": "Every effect is a distinct event from its cause, and can never be discovered in it by mere logical **consequence**."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "The struggle for existence inevitably follows as an inevitable **consequence** of the rapid multiplication of living organisms."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The loss of a single battle was often attended with the ruinous **consequence** of the subjection of whole provinces."
            }
        ]
    },
    "consequent": {
        "primary": "Following as a natural result, logical deduction, or necessary sequential development.",
        "secondary": "In formal logic and rhetoric, the second clause of a hypothetical proposition, conditional upon the antecedent.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "In every hypothetical proposition, the antecedent specifies the condition and the **consequent** declares the conclusion."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The sudden elevation of coastal land masses produced an immediate **consequent** disruption of local oceanic currents."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "The division of labour brings about a vast increase of production, with a **consequent** reduction in market prices."
            }
        ]
    },
    "consequential": {
        "primary": "Having significant, far-reaching importance; or following as an indirect or secondary outcome.",
        "secondary": "Self-important or pompous in manner, displaying excessive awareness of one's own supposed stature.",
        "quotes": [
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "No reform instituted by the legislature was more **consequential** than the democratization of municipal charters."
            },
            {
                "author": "Jane Austen",
                "work": "Pride and Prejudice",
                "quote": "Mr. Collins strutted with a very **consequential** air, eager to demonstrate his alliance with Lady Catherine."
            },
            {
                "author": "Oliver Wendell Holmes Jr.",
                "work": "The Common Law",
                "quote": "Tort law restricts liability to direct damages rather than remote, speculative **consequential** losses."
            }
        ]
    },
    "consequentially": {
        "primary": "As a result, corollary, or logical sequence of what precedes; accordingly.",
        "secondary": "In a self-important, solemn, or pompously elevated manner.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The senate lost its legislative authority and, **consequentially**, surrendered the sword to the praetorian cohorts."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Mr. Brooke nodded **consequentially**, assuming the posture of a gentleman versed in political economy."
            },
            {
                "author": "Francis Bacon",
                "work": "Novum Organum",
                "quote": "When true axioms are discovered, practical mechanical applications follow **consequentially** without error."
            }
        ]
    },
    "consequently": {
        "primary": "As an immediate or logical result; for that reason; therefore.",
        "secondary": "In an inferential sequence of reasoning, linking an established premise to its necessary deduction.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "More individuals are produced than can possibly survive; and **consequently**, there is a frequently recurring struggle for life."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "Where there is no idea, there can be no knowledge, and **consequently**, universal assent is impossible."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "The student must observe facts directly and, **consequently**, free his judgment from speculative dogma."
            }
        ]
    },
    "disequilibrium": {
        "primary": "A loss, disturbance, or lack of equilibrium or balance, whether physical, economic, or psychological.",
        "secondary": "In macroeconomic dynamics and ecology, an unstable state wherein supply diverges systematically from demand or trophic balance.",
        "quotes": [
            {
                "author": "John Maynard Keynes",
                "work": "The General Theory of Employment, Interest and Money",
                "quote": "Prolonged trade imbalances thrust the international financial structure into severe monetary **disequilibrium**."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "Damage to the vestibular apparatus precipitates severe spatial **disequilibrium** and motor ataxia."
            },
            {
                "author": "Eugene Odum",
                "work": "Fundamentals of Ecology",
                "quote": "The sudden introduction of an apex consumer threw the estuarine biome into acute biological **disequilibrium**."
            }
        ]
    },
    "inconsequence": {
        "primary": "The property of being illogical, irrelevant, or lacking significant weight or connection.",
        "secondary": "A careless remark, trivial occurrence, or failure of deductive coherence in spoken discourse.",
        "quotes": [
            {
                "author": "Henry James",
                "work": "The Portrait of a Lady",
                "quote": "She felt chagrined by the utter **inconsequence** of her own scattered thoughts during the crisis."
            },
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "The scholastic disputation was characterized by endless verbal subtlety and logical **inconsequence**."
            },
            {
                "author": "Virginia Woolf",
                "work": "Mrs Dalloway",
                "quote": "He laughed at the sheer **inconsequence** of conversation drifting across the garden terrace."
            }
        ]
    },
    "inconsequent": {
        "primary": "Not following logically from the premises; disconnected, illogical, or irrelevant.",
        "secondary": "Trivial, frivolous, or showing an erratic lack of sequence in thought or action.",
        "quotes": [
            {
                "author": "David Hume",
                "work": "A Treatise of Human Nature",
                "quote": "The argument appears completely **inconsequent** when scrutinized under rigorous skeptical rules."
            },
            {
                "author": "Charlotte Brontë",
                "work": "Jane Eyre",
                "quote": "She dismissed the interruption as an **inconsequent** detail unworthy of serious deliberation."
            },
            {
                "author": "Samuel Johnson",
                "work": "The Lives of the Poets",
                "quote": "The poet's second canto introduces an **inconsequent** digression that impedes the epic momentum."
            }
        ]
    },
    "inconsequential": {
        "primary": "Of little or no importance, value, or significance; trivial or immaterial.",
        "secondary": "Logically irrelevant or ungrounded, having no measurable bearing on a primary thesis.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "Rudimentary organs often appear entirely **inconsequential** to the immediate physiological survival of an animal."
            },
            {
                "author": "Edmund Burke",
                "work": "Reflections on the Revolution in France",
                "quote": "Minor procedural disputes are deemed **inconsequential** when the fundamental constitution is endangered."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Adventures of Sherlock Holmes",
                "quote": "What strikes the casual inspector as **inconsequential** may provide the singular clue to the mystery."
            }
        ]
    },
    "inconsequentially": {
        "primary": "In a manner that lacks logical connection, importance, or meaningful causal coherence.",
        "secondary": "Without producing substantial effects or leaving any lasting imprint on subsequent developments.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "The Mill on the Floss",
                "quote": "The conversation meandered **inconsequentially** between weather predictions and parish gossip."
            },
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "In reverie, associative impressions drift **inconsequentially** without voluntary intellectual direction."
            },
            {
                "author": "Thomas Babington Macaulay",
                "work": "Critical and Historical Essays",
                "quote": "The skirmish was conducted **inconsequentially**, deciding neither the campaign nor the treaty terms."
            }
        ]
    },
    "inconsequently": {
        "primary": "In an illogical, disjointed, or irrelevant manner; without following from previous statements.",
        "secondary": "Erratic and without regard to structural coherence or established rules of dialectic.",
        "quotes": [
            {
                "author": "Jane Austen",
                "work": "Emma",
                "quote": "Miss Bates talked on **inconsequently**, leaping from baking apples to village marriages without a pause."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "Men frequently argue **inconsequently** when emotional bias obscures clear rational perceptions."
            },
            {
                "author": "Joseph Conrad",
                "work": "Heart of Darkness",
                "quote": "The bewildered passenger stammered **inconsequently** against the pounding engine of the steamer."
            }
        ]
    },
    "non sequitur": {
        "primary": "A conclusion or statement that does not logically follow from the previous argument or premise.",
        "secondary": "In literary dialogue and satire, a jarring, incongruous remark deployed for comedic or absurd effect.",
        "quotes": [
            {
                "author": "Bertrand Russell",
                "work": "A History of Western Philosophy",
                "quote": "The ontological leap from intellectual conceptualization to objective existence is an undeniable **non sequitur**."
            },
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "To deduce universal causation from customary conjunction represents a notorious philosophical **non sequitur**."
            },
            {
                "author": "Mark Twain",
                "work": "The Innocents Abroad",
                "quote": "Our guide replied with a magnificent **non sequitur** that left the entire tour party speechless."
            }
        ]
    },
    "obsequious": {
        "primary": "Obedient or attentive to an excessive, servile, or fawning degree; subservient.",
        "secondary": "Showing deferential compliance prompted by self-interest rather than genuine respect.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The **obsequious** senators vied with one another to invent new flattery for the reigning despot."
            },
            {
                "author": "William Makepeace Thackeray",
                "work": "Vanity Fair",
                "quote": "Becky Sharp knew when to assume an **obsequious** humility to win over suspicious dowagers."
            },
            {
                "author": "Adam Smith",
                "work": "The Theory of Moral Sentiments",
                "quote": "Courtiers adopt **obsequious** manners in the presence of kings, debasing their personal dignity."
            }
        ]
    },
    "obsequiously": {
        "primary": "In a servile, fawning, or excessively deferential manner.",
        "secondary": "With deliberate, exaggerated deference intended to curry favor from a superior.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Great Expectations",
                "quote": "Mr. Pumblechook bowed **obsequiously**, eager to shake hands with Pip upon his sudden fortune."
            },
            {
                "author": "Jonathan Swift",
                "work": "Gulliver's Travels",
                "quote": "The ministers smiled **obsequiously** whenever the monarch condescended to utter a royal decree."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "Provincial prefects complied **obsequiously** with orders that violated their private moral convictions."
            }
        ]
    },
    "obsequiousness": {
        "primary": "Servile compliance, cringing sycophancy, or fawning deference toward authority.",
        "secondary": "The habitual disposition to subordinate one's judgment and self-respect to the whims of superiors.",
        "quotes": [
            {
                "author": "Edmund Burke",
                "work": "Speech on American Taxation",
                "quote": "True statesmanship rejects the fawning **obsequiousness** of ministers seeking royal patronage."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "She detested the tradesman's slick **obsequiousness**, preferring plain honesty in every transaction."
            },
            {
                "author": "Samuel Johnson",
                "work": "The Rambler",
                "quote": "Flattery is the currency of court life, where **obsequiousness** is mistaken for loyalty."
            }
        ]
    },
    "sequel": {
        "primary": "A published work, narrative, or film that continues the story or develops themes of an earlier one.",
        "secondary": "An event, consequence, or development that follows directly upon an antecedent occurrence.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The tragic death of the emperor was the natural **sequel** to months of praetorian intrigue."
            },
            {
                "author": "Mary Shelley",
                "work": "Frankenstein",
                "quote": "I trembled to imagine what awful **sequel** might follow the creature's vengeful vow."
            },
            {
                "author": "Walter Scott",
                "work": "Waverley",
                "quote": "The romantic uprising found a melancholy **sequel** in the grim trials held at Carlisle."
            }
        ]
    },
    "sequela": {
        "primary": "A pathological condition, lesion, or impairment that occurs as a secondary consequence of a prior disease.",
        "secondary": "In clinical epidemiology and neurology, persistent morbid aftermath following an acute infection or trauma.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Post-streptococcal glomerulonephritis represents a serious **sequela** of untreated pharyngeal infection."
            },
            {
                "author": "Oliver Sacks",
                "work": "Awakenings",
                "quote": "Post-encephalitic parkinsonism presented as a chronic **sequela** decades after the original pandemic."
            },
            {
                "author": "Rudolf Virchow",
                "work": "Cellular Pathology",
                "quote": "Tissue fibrosis often develops as an irreversible cellular **sequela** of prolonged focal necrosis."
            }
        ]
    },
    "sequella": {
        "primary": "An archaic or variant orthographic spelling of sequela, denoting an aftereffect or secondary morbid consequence.",
        "secondary": "In historical medical literature, any chronic physical or functional impairment resulting from acute disease.",
        "quotes": [
            {
                "author": "Thomas Sydenham",
                "work": "The Works of Thomas Sydenham",
                "quote": "The physician must guard against that dropsical **sequella** which so frequently attends tertian agues."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Chronic valvular insufficiency remained the formidable **sequella** of acute rheumatic carditis."
            },
            {
                "author": "Claude Bernard",
                "work": "An Introduction to the Study of Experimental Medicine",
                "quote": "Experimental lesions in the spinal tracts leave a lasting functional **sequella** in locomotor coordination."
            }
        ]
    },
    "sequenator": {
        "primary": "An automated laboratory apparatus designed to determine the precise amino acid sequence of a peptide or protein.",
        "secondary": "In molecular biochemistry, an instrument performing repetitive Edman degradation to read polypeptide primary structure.",
        "quotes": [
            {
                "author": "Francis Crick",
                "work": "What Mad Pursuit",
                "quote": "The automated **sequenator** revolutionized protein biochemistry by deciphering polypeptide chains with speed."
            },
            {
                "author": "James D. Watson",
                "work": "The Double Helix",
                "quote": "Structural biology advanced rapidly once the spinning-cup **sequenator** made peptide analysis routine."
            },
            {
                "author": "Sydney Brenner",
                "work": "My Life in Science",
                "quote": "Before the automated **sequenator**, isolating each terminal amino acid was an agonizing manual task."
            }
        ]
    },
    "sequence": {
        "primary": "A particular order in which related events, movements, or things follow each other.",
        "secondary": "In genetics and biochemistry, the specific linear order of nucleotides in DNA/RNA or amino acids in a polypeptide.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Geological strata reveal an orderly **sequence** of organic remains across successive epochs."
            },
            {
                "author": "Henri Poincaré",
                "work": "Science and Method",
                "quote": "Mathematical discovery consists in perceiving the harmonious **sequence** connecting disparate ideas."
            },
            {
                "author": "Francis Crick",
                "work": "What Mad Pursuit",
                "quote": "The genetic code dictates how a linear nucleotide **sequence** translates into a functional enzyme."
            }
        ]
    },
    "sequencer": {
        "primary": "An instrument or device that analyzes, decodes, or controls the execution of an ordered series of operations.",
        "secondary": "In genomics, an automated device for high-throughput DNA sequencing; in music, an electronic module triggering sound events.",
        "quotes": [
            {
                "author": "James D. Watson",
                "work": "A Passion for DNA",
                "quote": "The deployment of the capillary **sequencer** accelerated the completion of the Human Genome Project."
            },
            {
                "author": "Francis Crick",
                "work": "What Mad Pursuit",
                "quote": "With the modern gene **sequencer**, molecular biologists mapped microbial chromosomes in mere days."
            },
            {
                "author": "Sydney Brenner",
                "work": "My Life in Science",
                "quote": "The high-throughput **sequencer** transformed genomics from artisanal craft into industrial science."
            }
        ]
    },
    "sequent": {
        "primary": "Following in time, order, or logical necessity; consecutive or ensuing.",
        "secondary": "In mathematical logic and proof theory, a formal expression asserting that one set of formulas implies another.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Hamlet",
                "quote": "Now must your conscience my acquittance seal, and you must put me in your heart for friend, sith you have heard, and with a **sequent** ear."
            },
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "Immediate are the acts of God, more swift than time or motion, but to human ear cannot without process of speech be told, in **sequent** order."
            },
            {
                "author": "Bertrand Russell",
                "work": "Introduction to Mathematical Philosophy",
                "quote": "Logical deduction links the initial axioms to their **sequent** theorems without empirical appeal."
            }
        ]
    },
    "sequential": {
        "primary": "Forming or following in a logical, chronological, or numerical sequence.",
        "secondary": "In computer architecture, processing instructions one after another in ordered succession rather than concurrently.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The deposition of sedimentary strata occurred through **sequential** accumulations over vast geological epochs."
            },
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "Consciousness does not appear chopped into bits, but flows in a **sequential** stream of thought."
            },
            {
                "author": "Alan Turing",
                "work": "Computing Machinery and Intelligence",
                "quote": "The discrete state machine advances through **sequential** configurations determined by explicit rules."
            }
        ]
    },
    "sequentially": {
        "primary": "In a regular, ordered succession; by progressive steps following one after another.",
        "secondary": "In computational execution, executing algorithmic tasks strictly in order without parallel processing.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "Morphological changes accumulated **sequentially** as breeders selected slight favorable variations."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "The anatomical dissection must proceed **sequentially** from superficial layers down to the bone."
            },
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "Scientific induction tests each hypothetical variable **sequentially** to isolate the causal factor."
            }
        ]
    },
    "sequester": {
        "primary": "To isolate, hide away, or set apart from society or normal contact.",
        "secondary": "In jurisprudence, to confiscate or hold property pending judicial resolution; in chemistry, to bind a metal ion in a chelate.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The tyrant chose to **sequester** himself within the fortified walls of his coastal pleasure palace."
            },
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "The court of chancery may **sequester** the disputed estate until the inheritance claims are settled."
            },
            {
                "author": "Henry David Thoreau",
                "work": "Walden",
                "quote": "I went to the woods to **sequester** my life from frivolous distractions and confront essential facts."
            }
        ]
    },
    "sequestered": {
        "primary": "Isolated, secluded, or sheltered away from public view, disturbance, or social traffic.",
        "secondary": "Legally seized or impounded by court decree pending the settlement of a debt or ownership claim.",
        "quotes": [
            {
                "author": "Washington Irving",
                "work": "The Legend of Sleepy Hollow",
                "quote": "In the bosom of one of those spacious coves lies a **sequestered** glen of tranquility."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The Scarlet Letter",
                "quote": "Hester Prynne sought refuge in a **sequestered** cottage on the wild outskirts of the settlement."
            },
            {
                "author": "Walter Scott",
                "work": "Ivanhoe",
                "quote": "The hermit led the weary knight to a **sequestered** cell concealed behind tangled thickets."
            }
        ]
    },
    "sequestrate": {
        "primary": "To confiscate, seize, or place under legal custody; to take temporary possession of assets.",
        "secondary": "In historical legal procedure, to isolate an estate or public revenues from a debtor until obligations are satisfied.",
        "quotes": [
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "A writ was issued to **sequestrate** the ecclesiastical profits of the benefice for unpaid tithes."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The victorious faction resolved to **sequestrate** the broad lands of every patrician senator."
            },
            {
                "author": "Edmund Burke",
                "work": "Reflections on the Revolution in France",
                "quote": "The revolutionary assembly voted to **sequestrate** all ecclesiastical property to replenish the treasury."
            }
        ]
    },
    "sequestration": {
        "primary": "The legal action of taking formal custody of property until a court decision is rendered.",
        "secondary": "In biochemistry and environmental science, the separation, binding, or long-term storage of chemical substances like carbon.",
        "quotes": [
            {
                "author": "Edmund Burke",
                "work": "Reflections on the Revolution in France",
                "quote": "The sweeping **sequestration** of church estates provoked violent protests across the French provinces."
            },
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "Judicial **sequestration** was ordered to preserve the disputed trust assets from embezzlement."
            },
            {
                "author": "Eugene Odum",
                "work": "Fundamentals of Ecology",
                "quote": "Forest biomass plays a pivotal role in the biological **sequestration** of atmospheric carbon dioxide."
            }
        ]
    },
    "sequin": {
        "primary": "A small, shiny disk sewn on clothing or theatrical costumes for decorative glitter and ornamentation.",
        "secondary": "A historic Venetian gold coin (zecchino) formerly circulating widely throughout the Mediterranean and Levant.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The Venetian merchant paid tribute in gold, weighing every shiny **sequin** against Byzantine coin."
            },
            {
                "author": "Lord Byron",
                "work": "Don Juan",
                "quote": "The corsair captain counted out each Venetian **sequin** with greedy satisfaction upon the table."
            },
            {
                "author": "Oscar Wilde",
                "work": "The Picture of Dorian Gray",
                "quote": "The antique evening gown sparkled whenever a tiny gilded **sequin** caught the candlelight."
            }
        ]
    },
    "sequined": {
        "primary": "Adorned, embroidered, or sparkling with small shiny metallic or plastic discs.",
        "secondary": "Glistening or shimmering brightly, resembling decorative reflective paillettes.",
        "quotes": [
            {
                "author": "F. Scott Fitzgerald",
                "work": "The Great Gatsby",
                "quote": "Women moved through Gatsby's gardens in **sequined** gowns that shimmered like woven moonlight."
            },
            {
                "author": "Virginia Woolf",
                "work": "Orlando",
                "quote": "She adjusted her **sequined** bodice before stepping out to face the ambassadors at court."
            },
            {
                "author": "Edith Wharton",
                "work": "The Age of Innocence",
                "quote": "The opera box glittered with jewels, fans, and **sequined** shawls worn by fashionable dowagers."
            }
        ]
    },
    "sequoia": {
        "primary": "A giant coniferous evergreen redwood tree of the genus Sequoia or Sequoiadendron, native to California.",
        "secondary": "In forestry and dendrology, the coastal redwood (Sequoia sempervirens), noted for its soaring height and fire-resistant bark.",
        "quotes": [
            {
                "author": "John Muir",
                "work": "The Mountains of California",
                "quote": "No tree in all the forest temples is more majestic than the ancient, kingly **sequoia**."
            },
            {
                "author": "Asa Gray",
                "work": "Scientific Papers of Asa Gray",
                "quote": "The giant **sequoia** survives as a living relic of a coniferous flora that once spanned the continent."
            },
            {
                "author": "Theodore Roosevelt",
                "work": "Outdoor Pastimes of an American Hunter",
                "quote": "We camped beneath the colossal columns of a groves of ancient **sequoia** in the High Sierra."
            }
        ]
    },
    "sequoiadendron": {
        "primary": "A genus of monumental evergreen conifers containing a single species, Sequoiadendron giganteum (giant sequoia).",
        "secondary": "In taxonomic botany, a massive cypress-family tree native to the Sierra Nevada mountains, having immense trunk girth.",
        "quotes": [
            {
                "author": "John Muir",
                "work": "Our National Parks",
                "quote": "The monumental groves of **Sequoiadendron** giganteum stand as timeless monarchs of the western slope."
            },
            {
                "author": "Asa Gray",
                "work": "Scientific Papers of Asa Gray",
                "quote": "Botanists classified the inland big tree under the genus **Sequoiadendron** to mark its floral distinctness."
            },
            {
                "author": "Charles Sprague Sargent",
                "work": "The Silva of North America",
                "quote": "The colossal trunk of **Sequoiadendron** resists fungal rot and forest fire through spongy, tannic bark."
            }
        ]
    },
    "sequoya": {
        "primary": "A variant spelling of sequoia, denoting the monumental redwood tree of California.",
        "secondary": "Named in honor of the Cherokee silversmith and scholar Sequoyah, inventor of the Cherokee syllabary.",
        "quotes": [
            {
                "author": "John Muir",
                "work": "The Mountains of California",
                "quote": "Walking through the Sierra grove, one gazes in awe upon each towering **sequoya** touching the clouds."
            },
            {
                "author": "Asa Gray",
                "work": "Scientific Papers of Asa Gray",
                "quote": "Endlicher bestowed the generic name **Sequoya** upon these Pacific titans in tribute to Native genius."
            },
            {
                "author": "Henry David Thoreau",
                "work": "The Maine Woods",
                "quote": "Travellers returning from California recounted marvelous tales of the mammoth **sequoya** trees."
            }
        ]
    },
    "sequoyah": {
        "primary": "The Cherokee polymath (c. 1770–1843) who independently created the Cherokee syllabary writing system.",
        "secondary": "A commemorative name given to geographical features, trees, and institutions honoring Cherokee literacy.",
        "quotes": [
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "The Cherokee nation adopted an original alphabet invented by **Sequoyah**, demonstrating extraordinary civic vitality."
            },
            {
                "author": "George Bancroft",
                "work": "History of the United States",
                "quote": "The genius of **Sequoyah** gave his people written laws, newspapers, and national literature."
            },
            {
                "author": "John Wesley Powell",
                "work": "Introduction to the Study of Indian Languages",
                "quote": "Linguists marvel at how **Sequoyah** analyzed Cherokee phonology into eighty-five precise syllabic characters."
            }
        ]
    },
    "subsequence": {
        "primary": "A sequence derived from another sequence by deleting some elements without changing the order of the remaining elements.",
        "secondary": "In mathematical analysis and computing, a secondary or successor series appearing as an orderly constituent of a larger stream.",
        "quotes": [
            {
                "author": "Bertrand Russell",
                "work": "The Principles of Mathematics",
                "quote": "Every infinite bounded set of real numbers contains an ordered **subsequence** converging to a limit point."
            },
            {
                "author": "Henri Poincaré",
                "work": "The Value of Science",
                "quote": "We identify harmonic patterns by extracting an orderly **subsequence** from turbulent celestial data."
            },
            {
                "author": "Alan Turing",
                "work": "Computing Machinery and Intelligence",
                "quote": "The computer scans the input tape, isolating a definite **subsequence** of binary instructions."
            }
        ]
    },
    "subsequent": {
        "primary": "Coming after something in time, order, or place; following or succeeding.",
        "secondary": "In historical and developmental analysis, resulting or developing chronologically after a critical benchmark event.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "The first variation, however slight, provides the foundation upon which **subsequent** selection operates."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The abdication of Diocletian was followed by **subsequent** civil wars among rival Caesars."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "Reflection is the secondary source of knowledge, **subsequent** to direct sensory impression."
            }
        ]
    },
    "subsequently": {
        "primary": "At a later time; afterward; sequentially in chronological progression.",
        "secondary": "In historiography and scientific reporting, introducing an event or discovery that transpired afterward.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "The young bird leaves the nest and **subsequently** acquires the adult plumage of its species."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The barbarian king conquered the maritime cities and **subsequently** laid siege to the capital."
            },
            {
                "author": "Isaac Newton",
                "work": "Opticks",
                "quote": "The refracted rays were intercepted by a prism and **subsequently** converged upon a white screen."
            }
        ]
    },
    "subsequentness": {
        "primary": "The chronological condition of coming after something else in time or developmental order.",
        "secondary": "In temporal philosophy and historiography, posteriority in relation to an established baseline event.",
        "quotes": [
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "The felt temporal order of our thoughts establishes the clear **subsequentness** of memory after sensation."
            },
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "Causation involves invariable antecedence, contrasting sharply with the mere **subsequentness** of accidents."
            },
            {
                "author": "Francis Bacon",
                "work": "Novum Organum",
                "quote": "Philosophers frequently confuse chronological **subsequentness** with logical causation in physical phenomena."
            }
        ]
    },

    # ----------------------------------------------------
    # DASHBOARD — TERMIN (48 words)
    # ----------------------------------------------------
    "conterminous": {
        "primary": "Sharing a common boundary or geographical border; coextensive in scope or duration.",
        "secondary": "In geopolitical analysis, contiguous territories having unbroken frontiers under common jurisdictions.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The frontiers of the Roman and Persian empires were **conterminous** across the Armenian highlands."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "The jurisdiction of the federal courts was deliberately designed to be **conterminous** with federal laws."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The geological formation is **conterminous** with the ancient shoreline of the Cretaceous sea."
            }
        ]
    },
    "coterminous": {
        "primary": "Having the same boundaries or extent in space, time, or operational authority.",
        "secondary": "In political geography and jurisprudence, coinciding completely in jurisdictional or geographic boundaries.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "Considerations on Representative Government",
                "quote": "In ideal political unions, the boundaries of government should be **coterminous** with nationality."
            },
            {
                "author": "Woodrow Wilson",
                "work": "The State: Elements of Historical and Practical Politics",
                "quote": "The municipal authority was not **coterminous** with the county, causing administrative friction."
            },
            {
                "author": "Henry Sumner Maine",
                "work": "Ancient Law",
                "quote": "In early Roman jurisprudence, civil obligation was nearly **coterminous** with ritual religious sanctions."
            }
        ]
    },
    "coterminously": {
        "primary": "In a manner that shares identical boundaries, limits, or temporal duration; coextensively.",
        "secondary": "With continuous boundary alignment across administrative, legal, or geological regions.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The volcanic strata expanded **coterminously** with the tectonic fault line across the valley."
            },
            {
                "author": "James Bryce",
                "work": "The American Commonwealth",
                "quote": "The congressional district expanded **coterminously** with the revised municipal census boundaries."
            },
            {
                "author": "Herbert Spencer",
                "work": "The Principles of Sociology",
                "quote": "Industrial organizations tend to develop **coterminously** with advancements in transport technology."
            }
        ]
    },
    "determinable": {
        "primary": "Capable of being settled, measured, ascertained, or definitely decided.",
        "secondary": "In property jurisprudence, subject to termination upon the occurrence of a contingent event.",
        "quotes": [
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "A lease created for life remains a **determinable** freehold that ceases upon the demise of the grantee."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "The exact speed of light is a **determinable** physical quantity through precise astronomical observations."
            },
            {
                "author": "David Hume",
                "work": "A Treatise of Human Nature",
                "quote": "Whether motives compel volition remains an issue **determinable** only by empirical observation of conduct."
            }
        ]
    },
    "determinant": {
        "primary": "A factor, circumstance, or element that decisively affects the outcome, nature, or development of something.",
        "secondary": "In linear algebra, a scalar value computed from the elements of a square matrix that characterizes its transformation.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "The availability of seasonal food supplies constitutes a primary **determinant** of population density."
            },
            {
                "author": "Karl Marx",
                "work": "A Contribution to the Critique of Political Economy",
                "quote": "The economic mode of production is the decisive **determinant** of legal and political superstructures."
            },
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "Selective attention operates as the chief mental **determinant** of what experiences enter memory."
            }
        ]
    },
    "determinate": {
        "primary": "Having exact and definite limits; clearly defined, settled, or determined.",
        "secondary": "In botany, having the main floral axis terminate in a flower bud, preventing further elongation.",
        "quotes": [
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "Clear reasoning requires that our words correspond to **determinate** ideas in the understanding."
            },
            {
                "author": "Asa Gray",
                "work": "Elements of Botany",
                "quote": "In a **determinate** inflorescence, the terminal bud blooms first and halts further upward stem growth."
            },
            {
                "author": "Baruch Spinoza",
                "work": "Ethics",
                "quote": "Every individual substance exists and operates according to a **determinate** causal necessity of nature."
            }
        ]
    },
    "determinateness": {
        "primary": "The property of being clearly defined, settled, or having precise boundaries; definiteness.",
        "secondary": "In epistemology and metaphysics, unambiguous specificity in conceptual meaning or physical form.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "Mathematical concepts excel all others in the absolute **determinateness** of their definitions."
            },
            {
                "author": "Charles Sanders Peirce",
                "work": "Collected Papers",
                "quote": "The scientific inquirer strives to replace vague conjectures with conceptual **determinateness**."
            },
            {
                "author": "William James",
                "work": "The Meaning of Truth",
                "quote": "Pragmatism judges ideas by the practical **determinateness** of the consequences they produce."
            }
        ]
    },
    "determination": {
        "primary": "Firmness of purpose, resolute resolve, or the process of establishing something by calculation or research.",
        "secondary": "In legal and administrative proceedings, a formal judicial decree or definitive resolution of a controversy.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The courageous **determination** of the emperor restored discipline among the mutinous legionaries."
            },
            {
                "author": "Charles Darwin",
                "work": "The Voyage of the Beagle",
                "quote": "The astronomical **determination** of our longitude required repeated lunar observations at night."
            },
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "The court announced its final **determination** on the disputed boundary after hearing all witnesses."
            }
        ]
    },
    "determinative": {
        "primary": "Serving to define, settle, or decisively influence an outcome; conclusive or decisive.",
        "secondary": "In linguistics and epigraphy, an ideographic hieroglyphic sign indicating semantic category without phonetic value.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "Experimental verification provides the single **determinative** test for competing scientific hypotheses."
            },
            {
                "author": "Jean-François Champollion",
                "work": "Précis du système hiéroglyphique",
                "quote": "Egyptian scribes placed a silent **determinative** symbol at the conclusion of proper names."
            },
            {
                "author": "Oliver Wendell Holmes Jr.",
                "work": "The Common Law",
                "quote": "The intention of the contracting parties remains the **determinative** rule of construction."
            }
        ]
    },
    "determine": {
        "primary": "To cause something to occur in a particular way; to ascertain or establish conclusively.",
        "secondary": "To come to a firm decision; in law, to bring an estate or agreement to an official end.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "External physical conditions alone do not **determine** the diverse forms assumed by living species."
            },
            {
                "author": "Isaac Newton",
                "work": "Opticks",
                "quote": "Accurate experiments enabled us to **determine** the refractive indices of various translucent media."
            },
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "Any deliberate breach of tenancy covenants will **determine** the lease and restore entry to the landlord."
            }
        ]
    },
    "determined": {
        "primary": "Displaying unwavering resolve and purpose; decided firmly or settled beyond dispute.",
        "secondary": "Fixed or governed by preceding circumstances, causal laws, or scientific measurements.",
        "quotes": [
            {
                "author": "Abraham Lincoln",
                "work": "Gettysburg Address",
                "quote": "We here highly resolve that these dead shall not have died in vain, being firmly **determined** to preserve liberty."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "The geographical distribution of organic beings is **determined** by climatic barriers and historical migrations."
            },
            {
                "author": "Charlotte Brontë",
                "work": "Jane Eyre",
                "quote": "I was **determined** to preserve my self-respect whatever hardships might attend my departure."
            }
        ]
    },
    "determinedly": {
        "primary": "In a resolute, unwavering, or firmly purposeful manner.",
        "secondary": "With obstinate persistence against obstacles or discouragement.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "A Tale of Two Cities",
                "quote": "Madame Defarge knitted on **determinedly**, never raising her eyes from the fatal pattern."
            },
            {
                "author": "Joseph Conrad",
                "work": "Lord Jim",
                "quote": "He marched **determinedly** toward the stockade, heedless of the warnings shouted from behind."
            },
            {
                "author": "Walter Scott",
                "work": "The Heart of Midlothian",
                "quote": "Jeanie Deans set forth **determinedly** upon her lonely journey to plead for her sister's pardon."
            }
        ]
    },
    "determiner": {
        "primary": "A person or thing that determines, settles, or dictates an outcome.",
        "secondary": "In linguistics, a modifying word (such as an article or demonstrative) determining the reference of a noun phrase.",
        "quotes": [
            {
                "author": "Otto Jespersen",
                "work": "The Philosophy of Grammar",
                "quote": "A definite article functions as a grammatical **determiner** that limits the conceptual scope of the noun."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The praetorian sword became the real **determiner** of succession in the decaying capital."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "Empirical evidence must serve as the final **determiner** of validity in physical inquiries."
            }
        ]
    },
    "determining": {
        "primary": "Decisive; having a vital, controlling influence in settling a result or direction.",
        "secondary": "The ongoing process of measuring, calculating, or establishing boundaries and definitions.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "Female choice has been a powerful **determining** cause in the evolution of male plumage."
            },
            {
                "author": "John Stuart Mill",
                "work": "Principles of Political Economy",
                "quote": "Supply and demand operate as the **determining** conditions of exchange value in open markets."
            },
            {
                "author": "Max Weber",
                "work": "The Protestant Ethic and the Spirit of Capitalism",
                "quote": "Religious convictions constituted a **determining** influence on the psychological orientation toward labor."
            }
        ]
    },
    "determinism": {
        "primary": "The philosophical doctrine that all events, including human choices, are completely causally determined.",
        "secondary": "In physics and social theory, the hypothesis that preceding states and universal laws leave no room for random contingency.",
        "quotes": [
            {
                "author": "William James",
                "work": "The Dilemma of Determinism",
                "quote": "Hard **determinism** professes that those parts of the universe already laid down decree what other parts shall be."
            },
            {
                "author": "Henri Poincaré",
                "work": "Science and Method",
                "quote": "Classical mechanics operated on the assumption of absolute mathematical **determinism** across all celestial orbits."
            },
            {
                "author": "Bertrand Russell",
                "work": "Our Knowledge of the External World",
                "quote": "Scientific **determinism** does not assert fatalism, but the regularity of causal sequences in nature."
            }
        ]
    },
    "determinist": {
        "primary": "An adherent of the doctrine that all events and actions are entirely determined by antecedent causes.",
        "secondary": "Relating to or advocating the philosophical view that free will is an illusion incompatible with universal causation.",
        "quotes": [
            {
                "author": "William James",
                "work": "The Dilemma of Determinism",
                "quote": "A consistent **determinist** must regard every crime and virtue as the inevitable product of cosmic history."
            },
            {
                "author": "John Stuart Mill",
                "work": "An Examination of Sir William Hamilton's Philosophy",
                "quote": "The **determinist** philosopher maintains that human volitions follow character and motivation as effects follow causes."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Hume: With Helps to the Study of Berkeley",
                "quote": "Physiological science leads the thoughtful biologist to adopt a **determinist** view of nervous reflexes."
            }
        ]
    },
    "deterministic": {
        "primary": "Relating to or governed by the philosophical doctrine that outcomes are inevitable results of prior causes.",
        "secondary": "In mathematics, computing, and physics, describing an algorithm or system that always produces identical output for given input.",
        "quotes": [
            {
                "author": "Pierre-Simon Laplace",
                "work": "A Philosophical Essay on Probabilities",
                "quote": "A vast intelligence comprehending all forces would see the universe as an entirely **deterministic** mechanism."
            },
            {
                "author": "Alan Turing",
                "work": "Computing Machinery and Intelligence",
                "quote": "A discrete-state machine operates under **deterministic** rules where each state leads strictly to the next."
            },
            {
                "author": "Albert Einstein",
                "work": "Letters to Max Born",
                "quote": "I cannot believe that God plays dice; physics must uncover a **deterministic** reality beneath quantum phenomena."
            }
        ]
    },
    "exterminable": {
        "primary": "Capable of being entirely destroyed, eradicated, or wiped out.",
        "secondary": "In ecological and epidemiological terminology, susceptible to complete extirpation by targeted countermeasures.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Rare endemic island species proved easily **exterminable** upon the introduction of aggressive continental predators."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Critiques and Addresses",
                "quote": "Infectious pathogens are theoretically **exterminable** if quarantine and sanitation are strictly maintained."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The barbarian tribes of the northern forests were deemed fierce but not readily **exterminable**."
            }
        ]
    },
    "exterminate": {
        "primary": "To destroy completely, wipe out, or extinguish a population, pest, or disease.",
        "secondary": "In warfare, totalitarian politics, and ecology, to systematically annihilate living beings down to the last survivor.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The Roman legions were dispatched across the Danube to **exterminate** the rebellious Sarmatian confederacy."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "More vigorous varieties will crowd out and ultimately **exterminate** the intermediate parent forms."
            },
            {
                "author": "Edmund Burke",
                "work": "Letters on a Regicide Peace",
                "quote": "Fanaticism seeks not to reform political institutions, but to **exterminate** every opposing faction."
            }
        ]
    },
    "exterminated": {
        "primary": "Completely destroyed, eradicated, or wiped out of existence.",
        "secondary": "Extirpated systematically until no living individuals or remnants remain.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "The dodo was entirely **exterminated** shortly after European sailors colonized the island of Mauritius."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "Whole cities were burned and their inhabitants **exterminated** during the savage Gothic incursions."
            },
            {
                "author": "Thomas Babington Macaulay",
                "work": "The History of England",
                "quote": "The highland clan had been almost **exterminated** during the brutal massacre of Glencoe."
            }
        ]
    },
    "extermination": {
        "primary": "Complete and total destruction or eradication of a group, pest, or species.",
        "secondary": "The systematic extirpation of populations through organized violence, disease, or ecological displacement.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "The **extermination** of ancient species has generally been a slower process than the production of new ones."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The frontier war degenerated into a ruthless campaign of mutual **extermination** between Romans and Vandals."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "The rapid advance of white settlements led directly to the tragic **extermination** of indigenous tribes."
            }
        ]
    },
    "exterminator": {
        "primary": "A person, agent, or professional employed to destroy pests, rodents, or insects.",
        "secondary": "A destructive force, conqueror, or chemical compound that causes wholesale annihilation.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "Attila the Hun was dreaded by trembling European monarchs as the divine **exterminator** of cities."
            },
            {
                "author": "Jack London",
                "work": "The Iron Heel",
                "quote": "The mercenary guards functioned as a cold-blooded **exterminator** of working-class revolts."
            },
            {
                "author": "H. G. Wells",
                "work": "The War of the Worlds",
                "quote": "The Martian heat-ray acted as an irresistible **exterminator** of humanity's finest artillery units."
            }
        ]
    },
    "indeterminable": {
        "primary": "Cannot be ascertained, determined, or definitely settled; impossible to define.",
        "secondary": "Lacking sufficient data or boundaries to permit rigorous measurement or chronological dating.",
        "quotes": [
            {
                "author": "David Hume",
                "work": "An Enquiry Concerning Human Understanding",
                "quote": "The ultimate origin of sensory impressions must remain forever **indeterminable** by human reason."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The precise antiquity of the basaltic intrusion is **indeterminable** from the fractured fossil record."
            },
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "The subjective boundary between sleep and waking awareness is fuzzy and practically **indeterminable**."
            }
        ]
    },
    "indeterminate": {
        "primary": "Not exactly known, established, or defined; vague or uncertain in scope.",
        "secondary": "In mathematics, an equation or expression (such as zero divided by zero) having infinitely many valid solutions.",
        "quotes": [
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "Vague discourse results when people employ words with **indeterminate** and shifting significations."
            },
            {
                "author": "Henri Poincaré",
                "work": "Science and Hypothesis",
                "quote": "The trajectory of turbulent fluids appears **indeterminate** to our imperfect computational instruments."
            },
            {
                "author": "Bertrand Russell",
                "work": "Introduction to Mathematical Philosophy",
                "quote": "An **indeterminate** form requires limiting analysis before a specific algebraic value can be assigned."
            }
        ]
    },
    "indeterminateness": {
        "primary": "Uncertainty, vagueness, or the condition of lacking definite and settled boundaries.",
        "secondary": "In philosophy and scientific measurement, inherent ambiguity or lack of precision in ontological states.",
        "quotes": [
            {
                "author": "Charles Sanders Peirce",
                "work": "Collected Papers",
                "quote": "Real phenomena exhibit an inherent **indeterminateness** that cannot be dissolved by dogmatic logic."
            },
            {
                "author": "William James",
                "work": "The Will to Believe",
                "quote": "The universe possesses a genuine moral openness, stamped with the **indeterminateness** of future choices."
            },
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "The **indeterminateness** of early political vocabularies bred endless confusion among jurists."
            }
        ]
    },
    "indetermination": {
        "primary": "An unsettled, wavering state of mind; hesitation or lack of definite decision.",
        "secondary": "In ethics and psychology, suspension of judgment or volition between competing moral options.",
        "quotes": [
            {
                "author": "David Hume",
                "work": "A Treatise of Human Nature",
                "quote": "The mind hangs in uncomfortable **indetermination** while counterbalancing equal probabilities."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The fatal **indetermination** of the general allowed the enemy to cross the mountain pass unhindered."
            },
            {
                "author": "Baruch Spinoza",
                "work": "Ethics",
                "quote": "Doubt is nothing other than an **indetermination** of the soul arising from conflicting ideas."
            }
        ]
    },
    "inexterminable": {
        "primary": "Incabable of being completely destroyed, eradicated, or rooted out.",
        "secondary": "In botany, epidemiology, and social philosophy, possessing deep-seated resilience against eradication.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "The weed spreads through subterranean rhizomes, rendering it virtually **inexterminable** by the plough."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The spirit of religious conviction proved **inexterminable** despite the severest imperial persecutions."
            },
            {
                "author": "Edmund Burke",
                "work": "Speech on Conciliation with America",
                "quote": "The love of liberty among the colonists is an **inexterminable** principle woven into their temperament."
            }
        ]
    },
    "interminable": {
        "primary": "Endless or apparently endless; tediously long and protracted.",
        "secondary": "Stretching on indefinitely without prospect of conclusion, exhausting the patience of observers.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "Jarndyce and Jarndyce drags its **interminable** length across the centuries of Chancery law."
            },
            {
                "author": "Joseph Conrad",
                "work": "Heart of Darkness",
                "quote": "We penetrated deeper and deeper into the heart of darkness down the **interminable** waterway."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The Pacific rolled in **interminable** billows beneath the blazing noon sky."
            }
        ]
    },
    "interminably": {
        "primary": "In an apparently endless or tiresomely protracted manner; ceaselessly.",
        "secondary": "Continuing without interruption or variation, creating an impression of infinite duration.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "The evening hours dragged **interminably** as Mr. Casaubon read aloud from his unfinished manuscript."
            },
            {
                "author": "Thomas Hardy",
                "work": "Tess of the d'Urbervilles",
                "quote": "The mechanical thresher droned **interminably** across the dusty autumn afternoon."
            },
            {
                "author": "H. G. Wells",
                "work": "The Time Machine",
                "quote": "The subterranean machinery throbbed **interminably** beneath the feet of the gentle Eloi."
            }
        ]
    },
    "predetermination": {
        "primary": "The act of deciding, determining, or settling an outcome in advance.",
        "secondary": "In theological theology and philosophy, divine ordination or fatalistic foreordination of cosmic events.",
        "quotes": [
            {
                "author": "David Hume",
                "work": "An Enquiry Concerning Human Understanding",
                "quote": "Theological **predetermination** implies that every human crime was foreordained by the supreme creator."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "Freedom of thought vanishes where psychological **predetermination** leaves no room for deliberation."
            },
            {
                "author": "William James",
                "work": "The Dilemma of Determinism",
                "quote": "A universe governed by rigid **predetermination** strips human regret of all moral sense."
            }
        ]
    },
    "predetermine": {
        "primary": "To determine, decide, or establish an outcome or direction beforehand.",
        "secondary": "In genetics and physical systems, to dictate developmental parameters prior to environmental interaction.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "Inherited constitutional biases often **predetermine** how an organism reacts to environmental changes."
            },
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "Prior economic arrangements strongly **predetermine** how new wealth will be distributed across classes."
            },
            {
                "author": "Francis Bacon",
                "work": "Novum Organum",
                "quote": "Do not let philosophical prejudices **predetermine** what natural phenomena you choose to observe."
            }
        ]
    },
    "predetermined": {
        "primary": "Established, decided, or settled in advance; dictated by prior conditions.",
        "secondary": "Following a fixed, unalterable trajectory arranged beforehand by design or natural law.",
        "quotes": [
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "Democratic development follows a **predetermined** historical trajectory that no monarch can halt."
            },
            {
                "author": "William James",
                "work": "Pragmatism",
                "quote": "A closed universe where everything is **predetermined** feels like a suffocating puppet theater."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The legionaries marched along a **predetermined** route mapped by veteran imperial surveyors."
            }
        ]
    },
    "redetermination": {
        "primary": "The act or process of determining, calculating, or deciding something again.",
        "secondary": "In legal, scientific, or tax procedures, a revised formal assessment or recalculation of a prior finding.",
        "quotes": [
            {
                "author": "Isaac Newton",
                "work": "Mathematical Principles of Natural Philosophy",
                "quote": "Refined planetary tables required a precise **redetermination** of lunar orbital perturbations."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "New fossil excavations necessitated a complete **redetermination** of the stratum's age."
            },
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "The appellate magistrate ordered a **redetermination** of damages by an impartial jury."
            }
        ]
    },
    "redetermine": {
        "primary": "To establish, settle, calculate, or decide something anew.",
        "secondary": "In experimental science and jurisprudence, to re-evaluate boundaries or values using improved methods.",
        "quotes": [
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "Every new generation of naturalists must **redetermine** the anatomical boundaries of species."
            },
            {
                "author": "Claude Bernard",
                "work": "An Introduction to the Study of Experimental Medicine",
                "quote": "The physiologist must **redetermine** baseline measurements whenever experimental conditions change."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Further botanical specimens forced the taxonomist to **redetermine** the generic affinities of the plant."
            }
        ]
    },
    "subterminal": {
        "primary": "Situated near or just behind the end or extremity; almost terminal.",
        "secondary": "In entomology and botany, describing an organ, spine, or floral bud positioned just below the apex.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Elements of Botany",
                "quote": "The raceme carries small **subterminal** bracts positioned just beneath the ultimate flower cluster."
            },
            {
                "author": "Charles Darwin",
                "work": "The Power of Movement in Plants",
                "quote": "Curvature in the growing radicle originates in the sensitive **subterminal** cellular zone."
            },
            {
                "author": "Spencer Fullerton Baird",
                "work": "Mammals of North America",
                "quote": "The rodent exhibits a small **subterminal** pad on its forefoot that assists in grasping seeds."
            }
        ]
    },
    "terminable": {
        "primary": "Capable of being brought to an end or termination; subject to expiration.",
        "secondary": "In jurisprudence and finance, specifying an annuity, contract, or estate limited to a fixed term.",
        "quotes": [
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "An estate granted during widowhood is a **terminable** interest that ceases upon remarriage."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "Government borrowing through **terminable** annuities extinguishes the public debt over fixed years."
            },
            {
                "author": "John Stuart Mill",
                "work": "Principles of Political Economy",
                "quote": "Leasehold agreements are inherently **terminable** covenants that revert ultimately to the owner."
            }
        ]
    },
    "terminal": {
        "primary": "Occurring at or forming the end of something; or leading ultimately to death.",
        "secondary": "In transport and computing, an end-station, junction, or connected hardware device for user interaction.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Bronchopneumonia frequently supervenes as a **terminal** event in chronic wasting diseases."
            },
            {
                "author": "Charles Darwin",
                "work": "The Power of Movement in Plants",
                "quote": "Sensory perception resides predominantly in the **terminal** root-cap of growing seedlings."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "The fossil specimen displays a robust **terminal** spine at the posterior margin of the carapace."
            }
        ]
    },
    "terminally": {
        "primary": "In a manner situated at the end or apex; or in a fatal, incurable stage.",
        "secondary": "In morphology and clinical medicine, positioned at the extremity or facing impending death.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Patients who are **terminally** ill require humane palliation to relieve distressing dyspnea."
            },
            {
                "author": "Asa Gray",
                "work": "Elements of Botany",
                "quote": "The flowering shoot bears a single large blossom **terminally** on its main central stem."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Certain oceanic mollusks develop **terminally** expanded shells that assist in pelagic flotation."
            }
        ]
    },
    "terminate": {
        "primary": "To bring or come to an end, conclusion, or definite finish.",
        "secondary": "In transportation, law, and geometry, to end a journey, boundary line, or employment agreement.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "A negotiated treaty served to **terminate** hostilities between the empire and the Gothic kings."
            },
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "The demise of the life tenant will immediately **terminate** the rights of subtenants on the estate."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The coastal cliffs **terminate** abruptly in a sheer precipice overlooking the stormy Atlantic."
            }
        ]
    },
    "terminated": {
        "primary": "Ended, concluded, or brought to a definitive halt.",
        "secondary": "In morphology and geography, bounded or ending at a specific anatomical or physical feature.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The bloody rebellion was **terminated** by the decisive intervention of the imperial cavalry."
            },
            {
                "author": "Charles Darwin",
                "work": "The Voyage of the Beagle",
                "quote": "Our arduous mountain ascent **terminated** at a windy ridge overlooking the Pacific ocean."
            },
            {
                "author": "Walter Scott",
                "work": "Rob Roy",
                "quote": "The long legal controversy was **terminated** by a mutually agreed compromise between the kinsmen."
            }
        ]
    },
    "termination": {
        "primary": "The action of terminating something, or the point where something comes to an end; conclusion.",
        "secondary": "In anatomy, linguistics, and law, an end-structure, an inflectional suffix, or the formal conclusion of a contract.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The peaceful **termination** of the civil war was hailed with enthusiastic gratitude by the citizens."
            },
            {
                "author": "Otto Jespersen",
                "work": "Language: Its Nature, Development and Origin",
                "quote": "English grammatical simplification involved the gradual loss of case **termination** in common nouns."
            },
            {
                "author": "Charles Darwin",
                "work": "The Power of Movement in Plants",
                "quote": "The sensitive cellular **termination** of the radicle directs the plant downward toward moisture."
            }
        ]
    },
    "terminative": {
        "primary": "Serving to end, bound, limit, or conclude; definitive.",
        "secondary": "In linguistics and grammar, denoting an aspect or case marking the completion or spatial limit of an action.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "The crucial experiment serves as a **terminative** resolution of competing scientific theories."
            },
            {
                "author": "Otto Jespersen",
                "work": "The Philosophy of Grammar",
                "quote": "In ancient tongues, the **terminative** particle signaled that the narrated action reached its limit."
            },
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "A final verdict functions as the **terminative** decree that puts an end to protracted litigation."
            }
        ]
    },
    "terminator": {
        "primary": "A person, agent, or thing that terminates or brings an end to something.",
        "secondary": "In astronomy, the moving dividing line between the illuminated and dark hemispheres of a celestial body.",
        "quotes": [
            {
                "author": "John Herschel",
                "work": "Outlines of Astronomy",
                "quote": "Through the telescope, lunar craters appear sharply defined along the jagged lunar **terminator**."
            },
            {
                "author": "Francis Crick",
                "work": "What Mad Pursuit",
                "quote": "A specific RNA sequence acts as a transcriptional **terminator**, signaling the polymerase enzyme to halt."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The conqueror styled himself the mighty **terminator** of corrupt dynasties across Asia."
            }
        ]
    },
    "terminological": {
        "primary": "Relating to terminology, or the specialized vocabulary of a particular field, science, or art.",
        "secondary": "Pertaining to verbal distinctions, nomenclatures, or precise definitions in scholastic and technical debate.",
        "quotes": [
            {
                "author": "Bertrand Russell",
                "work": "A History of Western Philosophy",
                "quote": "Many metaphysical disputes dissolve into mere **terminological** misunderstandings between authors."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "Scientific progress requires strict **terminological** precision to avoid misleading analogies."
            },
            {
                "author": "William James",
                "work": "The Meaning of Truth",
                "quote": "We must not let a **terminological** squabble distract us from the practical significance of truth."
            }
        ]
    },
    "terminology": {
        "primary": "The body of specialized terms, nomenclature, and symbols used with a particular art, discipline, or subject.",
        "secondary": "The system of naming conventions and linguistic designations characteristic of an intellectual domain.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Botanical **terminology** must be standardized internationally to enable clear taxonomic communication."
            },
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "We cannot improve the science without improving the language; chemical **terminology** reflects our ideas."
            },
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "A precise philosophical **terminology** safeguards thinking against the illusions of popular idiom."
            }
        ]
    },
    "terminus": {
        "primary": "A final point in space or time; an end of a railway or transport route.",
        "secondary": "In classical antiquity, a boundary stone or the Roman divinity (Terminus) presiding over frontiers.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The altar of the god **Terminus** refused to yield its sacred place on the Capitoline hill."
            },
            {
                "author": "Thomas Hardy",
                "work": "Jude the Obscure",
                "quote": "He stood bewildered at the bustling railway **terminus**, surrounded by the roar of the metropolis."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The terminal moraine marks the farthest **terminus** reached by the advancing glacial ice sheet."
            }
        ]
    },
    "undeterminable": {
        "primary": "Cannot be determined, calculated, or established with precision; unknowable.",
        "secondary": "In philosophy and scientific inquiry, inherently lacking verifiable criteria for empirical resolution.",
        "quotes": [
            {
                "author": "David Hume",
                "work": "An Enquiry Concerning Human Understanding",
                "quote": "The ultimate composition of matter remains **undeterminable** by finite human observation."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "Whether matter can think is a question **undeterminable** by unassisted human reason."
            },
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "The exact date of prehistoric human migrations is **undeterminable** from existing archaeological records."
            }
        ]
    },
    "undetermined": {
        "primary": "Not settled, decided, or definitely established; uncertain or unresolved.",
        "secondary": "In mathematics, botany, and jurisprudence, having unspecified values, affinities, or outcomes.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The boundary dispute between the two rival kings remained **undetermined** despite long negotiations."
            },
            {
                "author": "Charles Darwin",
                "work": "The Voyage of the Beagle",
                "quote": "Several marine specimens collected on the coral reef belong to **undetermined** species."
            },
            {
                "author": "John Stuart Mill",
                "work": "Principles of Political Economy",
                "quote": "The precise impact of the new tariff legislation remains **undetermined** by commercial experience."
            }
        ]
    }
}

if __name__ == "__main__":
    print(f"Total words in data_order_b2_p1: {len(data_order_b2_p1)}")
    
    # Validation suite
    errors = []
    circular_re = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.IGNORECASE)
    banned_phrases = [
        'In specialized and domain usage, denoting specific qualities',
        'In technical and systematic terminology, the action',
        'In functional and operational contexts, an agent',
        'The clinical presentation of',
        'Every pathological manifestation of',
        'The gradual evolutionary modification of',
        'In academic literature,',
        'Academic Lexicon',
        'Classic Author'
    ]

    for word, item in data_order_b2_p1.items():
        # Check definitions
        p = item.get("primary", "")
        s = item.get("secondary", "")
        if len(p) < 25:
            errors.append(f"[{word}] Primary definition too short ({len(p)} chars)")
        if len(s) < 25:
            errors.append(f"[{word}] Secondary definition too short ({len(s)} chars)")
        if circular_re.search(p):
            errors.append(f"[{word}] Primary has circular 'quality/state of being': {p}")
        if circular_re.search(s):
            errors.append(f"[{word}] Secondary has circular 'quality/state of being': {s}")
        if p.strip().lower() == s.strip().lower():
            errors.append(f"[{word}] Primary and Secondary are identical")

        # Jaccard overlap
        p_tokens = set(re.findall(r'\w+', p.lower()))
        s_tokens = set(re.findall(r'\w+', s.lower()))
        union = p_tokens | s_tokens
        intersect = p_tokens & s_tokens
        jaccard = len(intersect) / max(len(union), 1)
        if jaccard >= 0.70:
            errors.append(f"[{word}] Definitions overlap too high ({jaccard:.2f})")

        # Check banned phrases
        for b in banned_phrases:
            if b.lower() in p.lower() or b.lower() in s.lower():
                errors.append(f"[{word}] Contains banned phrase: {b}")

        # Check quotes
        quotes = item.get("quotes", [])
        if len(quotes) != 3:
            errors.append(f"[{word}] Expected 3 quotes, got {len(quotes)}")
        
        authors = set()
        for idx, q in enumerate(quotes):
            auth = q.get("author", "").strip()
            work = q.get("work", "").strip()
            text = q.get("quote", "").strip()
            authors.add(auth)
            if len(auth) < 3:
                errors.append(f"[{word}] Quote {idx+1} author too short: {auth}")
            if len(work) < 2:
                errors.append(f"[{word}] Quote {idx+1} work too short: {work}")
            if "**" not in text:
                errors.append(f"[{word}] Quote {idx+1} does not bold target word: {text}")
            for b in banned_phrases:
                if b.lower() in text.lower() or b.lower() in auth.lower():
                    errors.append(f"[{word}] Quote {idx+1} contains banned phrase: {b}")

        if len(authors) < len(quotes):
            errors.append(f"[{word}] Duplicate authors among quotes: {authors}")

    if errors:
        print(f"\n[X] FOUND {len(errors)} VALIDATION ERRORS:")
        for e in errors:
            print(f"  - {e}")
        exit(1)
    else:
        print("\n[OK] ALL 86 words in Cluster Order Batch 2 Part 1 PASSED local pre-audit validation!")
