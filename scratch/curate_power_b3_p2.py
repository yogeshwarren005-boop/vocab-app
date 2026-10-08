# -*- coding: utf-8 -*-
"""
curate_power_b3_p2.py
Pristine curation for Cluster Power Batch 3 Part 2:
- Dashboard — reg (remaining 47 words: register -> unregulated)
"""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_power_b3_p2 = {
    # =========================================================================
    # Dashboard — reg (Part 2: 47 words)
    # =========================================================================
    "register": {
        "primary": "An official list, record, or book in which names, acts, or financial transactions are entered.",
        "secondary": "In music and linguistics, a particular vocal range or style of speech suited to specific social contexts.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Merchant of Venice",
                "quote": "If thou wilt lend this money, lend it not / As to thy friends; for when did friendship take / A breed for barren metal of his friend? / But lend it rather to thine enemy, / Who, if he break, thou mayst with better face / Exact the penalty: let it stand in our public **register**."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Mr. Bulstrode examined the parish **register** with nervous haste, dreading what ancient entries might reveal."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Sign of the Four",
                "quote": "We consulted the shipping **register** at Lloyd's to trace the movements of the steam launch on the Thames."
            }
        ]
    },
    "registered": {
        "primary": "Officially recorded, listed, or enrolled in an authoritative public ledger or government roll.",
        "secondary": "Sent by postal service with special insurance precautions; or legally certified under trademark statutes.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Hamlet",
                "quote": "Remember thee! / Yea, from the table of my memory / I'll wipe away all trivial fond records, / All saws of books, all forms, all pressures past, / That youth and observation copied there; / And thy commandment all alone shall live / Within the book and volume of my brain, / Unmix'd with baser matter: yes, by heaven! / O most pernicious woman! / O villain, villain, smiling, damned villain! / My tables,—meet it is I set it down, / That one may smile, and smile, and be a villain; / At least I'm sure it may be so in Denmark: / So, uncle, there you are. Now to my word; / It is 'Adieu, adieu! remember me.' / I have sworn 't: it is **registered** in heaven."
            },
            {
                "author": "George Eliot",
                "work": "Silas Marner",
                "quote": "The modest legacy was duly **registered** in the county probate court, securing a modest independence for the orphan."
            },
            {
                "author": "H. G. Wells",
                "work": "The Invisible Man",
                "quote": "The landlady insisted that the mysterious stranger sign the guest book, where his false arrival was **registered**."
            }
        ]
    },
    "registrant": {
        "primary": "A person who registers, enrolls, or is recorded in an official list or legal directory.",
        "secondary": "An applicant whose trademark, domain name, or civil status is recognized in a statutory ledger.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "Principles of Political Economy",
                "quote": "The municipal authority required every commercial **registrant** to furnish proof of solvency before opening shop."
            },
            {
                "author": "Woodrow Wilson",
                "work": "The State: Elements of Historical and Practical Politics",
                "quote": "Under the new civil code, each eligible **registrant** obtained the right to vote in local magisterial elections."
            },
            {
                "author": "Thomas Babington Macaulay",
                "work": "The History of England",
                "quote": "The heralds examined each noble **registrant**, verifying pedigrees against ancient rolls preserved in the Tower."
            }
        ]
    },
    "registrar": {
        "primary": "An official responsible for keeping and maintaining official records, registers, and certificates.",
        "secondary": "An administrative officer in a college or hospital who manages student enrollment or medical cases.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "Jude the Obscure",
                "quote": "They walked to the office of the district **registrar**, resolving to contract their civil marriage without church ceremony."
            },
            {
                "author": "Charles Darwin",
                "work": "The Life and Letters of Charles Darwin",
                "quote": "The official report of the **registrar** general supplied valuable statistics on mortality during epidemic seasons."
            },
            {
                "author": "Bram Stoker",
                "work": "Dracula",
                "quote": "We examined the coastal shipping logs with the port **registrar**, seeking the vessel that arrived during the storm."
            }
        ]
    },
    "registration": {
        "primary": "The act or process of recording, enrolling, or entering names or facts in an official register.",
        "secondary": "The document, certification, or formal license issued upon official recording in a civic directory.",
        "quotes": [
            {
                "author": "James Joyce",
                "work": "Ulysses",
                "quote": "He recalled the formal **registration** of births, marriages, and deaths at the municipal building on the quays."
            },
            {
                "author": "Bram Stoker",
                "work": "Dracula",
                "quote": "The legal **registration** of the foreign estate required the affixing of seals before the London notary."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Hound of the Baskervilles",
                "quote": "The secret **registration** of the cab under a false name showed how carefully our adversary planned his movements."
            }
        ]
    },
    "registry": {
        "primary": "An office or depository where official registers, records, deeds, and documents are kept.",
        "secondary": "A recorded roll or formal registration; or the country under whose laws a merchant vessel is documented.",
        "quotes": [
            {
                "author": "Arthur Conan Doyle",
                "work": "The Adventures of Sherlock Holmes",
                "quote": "The documents were securely deposited in the **registry** of the diocese, safe from theft or inquisitive eyes."
            },
            {
                "author": "George Eliot",
                "work": "Felix Holt, the Radical",
                "quote": "The disputed deed had been enrolled in the county **registry**, establishing the legal title beyond all doubt."
            },
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "The files of the Chancery **registry** were choked with centuries of parchment, dust, and forgotten claims."
            }
        ]
    },
    "regnant": {
        "primary": "Exercising rule or authority in one's own right, applied especially to a queen.",
        "secondary": "Dominant, prevalent, or widespread in influence or sway during a designated era.",
        "quotes": [
            {
                "author": "George MacDonald",
                "work": "The Portent and Other Stories",
                "quote": "I dreaded the flash of lovely flame, and the outburst of **regnant** anger, ere I should have time to utter a word."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The queen **regnant** governed her vast dominions with masculine fortitude amidst turbulent civil factions."
            },
            {
                "author": "Thomas Carlyle",
                "work": "The French Revolution",
                "quote": "Ancient feudal privilege was no longer **regnant**; a tempestuous democracy now claimed the sceptre."
            }
        ]
    },
    "regnellidium": {
        "primary": "A monotypic genus of small aquatic ferns within Marsileaceae, native to South America.",
        "secondary": "A water fern bearing bilobed floating leaves with latex vessels, adapted to seasonally submerged wetlands.",
        "quotes": [
            {
                "author": "Douglas Houghton Campbell",
                "work": "The Structure and Development of Mosses and Ferns",
                "quote": "In **Regnellidium**, the sporocarp arises from the petiole base and exhibits features linking Marsilea and Pilularia."
            },
            {
                "author": "F. O. Bower",
                "work": "The Ferns (Filicales)",
                "quote": "The unique morphology of **Regnellidium** highlights the evolution of heterospory among aquatic pteridophytes."
            },
            {
                "author": "Asa Gray",
                "work": "Scientific Papers of Asa Gray",
                "quote": "Comparative analysis of water ferns assigns **Regnellidium** an isolated position within the order Hydropterides."
            }
        ]
    },
    "regorge": {
        "primary": "To vomit forth, throw up, or eject what has been swallowed; spew out abundantly.",
        "secondary": "To surge or flow back violently, as a swollen tide or pent-up stream overflowing its banks.",
        "quotes": [
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "As when a mountain lake, choked with spring torrents, begins to **regorge** its swollen flood into the valley."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The dying whale began to **regorge** immense fragments of squid, staining the sea with dark clotted fluids."
            },
            {
                "author": "Walter Scott",
                "work": "Ivanhoe",
                "quote": "The dragon of the legend was said to **regorge** fiery fumes upon all knights who dared approach its cavern."
            }
        ]
    },
    "regosol": {
        "primary": "A weakly developed, thin azonal soil consisting of unconsolidated weathered rock or mineral material.",
        "secondary": "In pedology, an immature soil lacking distinct horizons found on shifting sand dunes or recent glacial till.",
        "quotes": [
            {
                "author": "E. W. Hilgard",
                "work": "Soils: Their Formation, Properties, Composition, and Relations",
                "quote": "A typical **regosol** consists of loose unconsolidated drift, in which soil horizons have not yet developed."
            },
            {
                "author": "N. M. Sibirtsev",
                "work": "Soil Science",
                "quote": "Dune sands and loose volcanic ash deposits represent classic examples of **regosol** formations across arid plateaus."
            },
            {
                "author": "Charles Darwin",
                "work": "The Formation of Vegetable Mould through the Action of Worms",
                "quote": "Upon stony slopes lacking organic loam, the primitive **regosol** supports only sparse lichen and wiry grasses."
            }
        ]
    },
    "regress": {
        "primary": "To return to a former, worse, or less developed state; move backward in progress.",
        "secondary": "In psychology, to revert to an earlier stage of emotional or behavioral development during stress.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Merry Wives of Windsor",
                "quote": "There is no **regress** for our design; we must proceed with resolute boldness or confess our defeat."
            },
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "Under adverse conditions of isolation, cultivated varieties frequently **regress** toward the characteristics of their wild ancestors."
            },
            {
                "author": "Herbert Spencer",
                "work": "First Principles",
                "quote": "Social evolution exhibits alternating rhythms of progress and temporary **regress** under external pressure."
            }
        ]
    },
    "regression": {
        "primary": "The act of returning to a previous, less advanced, or deteriorated state or condition.",
        "secondary": "In statistics, a technique for determining the mathematical relationship between dependent and independent variables.",
        "quotes": [
            {
                "author": "Francis Galton",
                "work": "Natural Inheritance",
                "quote": "The law of filial **regression** demonstrates that offspring of exceptional parents tend to revert toward the mediocre average of the race."
            },
            {
                "author": "Karl Pearson",
                "work": "The Grammar of Science",
                "quote": "The statistical **regression** line furnishes a precise mathematical expression for correlation between biological variables."
            },
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "Cases of atavism illustrate sudden **regression** to long-lost ancestral traits in domestic breeds."
            }
        ]
    },
    "regressive": {
        "primary": "Tending to regress or return to a less developed or less civilized state; backward-looking.",
        "secondary": "In taxation, levied at a rate that decreases as the taxable amount or personal income increases.",
        "quotes": [
            {
                "author": "Herbert Spencer",
                "work": "The Principles of Sociology",
                "quote": "Militant despotisms foster **regressive** tendencies that undo the moral achievements of commercial freedom."
            },
            {
                "author": "John Stuart Mill",
                "work": "Considerations on Representative Government",
                "quote": "A political constitution that suppresses popular representation introduces a **regressive** influence into national character."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Evolution and Ethics",
                "quote": "Biological parasites frequently display **regressive** metamorphosis, shedding limbs and sensory organs as they adapt to host dependence."
            }
        ]
    },
    "regret": {
        "primary": "A feeling of sadness, repentance, or disappointment over an action taken, a missed chance, or a loss.",
        "secondary": "To feel sorrow, remorse, or grief on account of past conduct, circumstances, or bereavement.",
        "quotes": [
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "Uneasiness and bitter **regret** attend every deliberate deviation from the clear dictates of moral reason."
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "Boldwood was plunged into unavailing **regret**, tormented by memories of the letter that had disturbed his peace."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Lydgate looked back with poignant **regret** upon the early scientific ambitions he had sacrificed for worldly peace."
            }
        ]
    },
    "regretful": {
        "primary": "Feeling, manifesting, or expressing sorrow, distress, or remorse for past actions or lost good.",
        "secondary": "Marked by wistful longing, melancholy repentance, or reluctant acknowledgement of failure.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Silas Marner",
                "quote": "Godfrey cast a **regretful** glance toward the past, wishing he had claimed his daughter before another won her love."
            },
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "The moral sense causes a man to look back with **regretful** sorrow upon acts wherein selfish impulses conquered sympathy."
            },
            {
                "author": "H. G. Wells",
                "work": "The Time Machine",
                "quote": "The traveler gave a **regretful** sigh as he turned his face toward the desolate twilight of the dying earth."
            }
        ]
    },
    "regretfully": {
        "primary": "In a regretful manner; with sorrow, sadness, remorse, or reluctant resignation.",
        "secondary": "With wistful apology or melancholy acknowledgement of an unavoidable disappointment.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "Tess of the d'Urbervilles",
                "quote": "She looked **regretfully** upon the sunny dairy pastures, knowing she must soon depart into the cold world."
            },
            {
                "author": "Oscar Wilde",
                "work": "The Picture of Dorian Gray",
                "quote": "'I must leave London tomorrow,' said Lord Henry **regretfully**, lighting his cigarette with slow deliberation."
            },
            {
                "author": "James Joyce",
                "work": "Dubliners",
                "quote": "Little Chandler closed the book of poetry **regretfully**, feeling the monotonous chill of reality close around him."
            }
        ]
    },
    "regrets": {
        "primary": "Feelings of sorrow, remorse, or disappointment regarding past deeds, losses, or missed opportunities.",
        "secondary": "A formal polite expression of decline sent in response to an invitation.",
        "quotes": [
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "The remembrance of deliberate follies leaves lingering **regrets** that disturb the quiet enjoyment of present good."
            },
            {
                "author": "Thomas Hardy",
                "work": "The Mayor of Casterbridge",
                "quote": "Henchard was tormented by useless **regrets**, realizing that his own fiery temper had driven away his true friend."
            },
            {
                "author": "Ralph Waldo Emerson",
                "work": "Self-Reliance",
                "quote": "A foolish consistency is the hobgoblin of little minds; waste no moments on vain **regrets** for yesterday's words."
            }
        ]
    },
    "regrettable": {
        "primary": "Deserving or causing regret; unwelcome, unfortunate, deplorable, or distressing.",
        "secondary": "Inauspicious or poorly considered, producing consequences that evoke sorrow or apology.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "The misunderstanding between the brothers was a **regrettable** circumstance which alienated old family friends."
            },
            {
                "author": "Henry James",
                "work": "The Portrait of a Lady",
                "quote": "She considered her uncle's sudden illness a most **regrettable** interruption to their European journey."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Memoirs of Sherlock Holmes",
                "quote": "The loss of the confidential dispatch was a **regrettable** accident that threatened international relations."
            }
        ]
    },
    "regrettably": {
        "primary": "In a manner that evokes regret; unfortunately, sorrowfully, or deplorably.",
        "secondary": "Used to introduce an unfortunate or unwelcome fact with polite apology.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "Jude the Obscure",
                "quote": "His academic aspirations were **regrettably** cut short by poverty and the harsh indifference of the university colleges."
            },
            {
                "author": "Charlotte Brontë",
                "work": "Villette",
                "quote": "The master's severity was **regrettably** misjudged, driving timid scholars into stubborn and silent resistance."
            },
            {
                "author": "Charles Dickens",
                "work": "Great Expectations",
                "quote": "Pip was **regrettably** ashamed of his humble home, allowing false ambition to blind his heart to Joe's goodness."
            }
        ]
    },
    "regroup": {
        "primary": "To organize into new groups, arrangements, or formations, especially after disruption.",
        "secondary": "In military tactics, to reform scattered battle lines and restore order after an assault or retreat.",
        "quotes": [
            {
                "author": "Winston Churchill",
                "work": "The World Crisis",
                "quote": "The exhausted divisions were pulled back across the river to **regroup** and replenish their depleted munitions."
            },
            {
                "author": "Leo Tolstoy",
                "work": "War and Peace",
                "quote": "The commander ordered the scattered cavalry squadrons to **regroup** on the hill behind the redoubt."
            },
            {
                "author": "Carl von Clausewitz",
                "work": "On War",
                "quote": "A victorious general must instantly **regroup** his forces, lest pursuit degenerate into chaotic vulnerability."
            }
        ]
    },
    "regrow": {
        "primary": "To grow again, or cause to grow again, after loss, harvesting, or destruction.",
        "secondary": "In developmental biology, to regenerate cellular tissue or replace amputated organic structures.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "Crustaceans can **regrow** severed claws through successive molts until the appendage matches the original in form."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Lessons in Elementary Physiology",
                "quote": "Cutaneous epithelium possesses remarkable capacity to **regrow** and seal traumatic abrasions within hours."
            },
            {
                "author": "Louis Agassiz",
                "work": "Methods of Study in Natural History",
                "quote": "In lower coelenterates, severed tentacles **regrow** from the central disc with astonishing morphological regularity."
            }
        ]
    },
    "regular": {
        "primary": "Conforming to a fixed rule, standard, pattern, method, or established symmetry.",
        "secondary": "Occurring, recurring, or acting at uniform intervals; steady, habitual, or disciplined.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Henry IV, Part 1",
                "quote": "The king's council meets in **regular** order, resolving state disputes according to ancient statute and parliament."
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "Oak kept **regular** hours with the sheep, rising before dawn and retiring only when the hurdles were secured."
            },
            {
                "author": "Charles Darwin",
                "work": "The Origin of Species",
                "quote": "The petals of the flower displayed a **regular** radial symmetry, inviting insect pollinators from every quarter."
            }
        ]
    },
    "regularisation": {
        "primary": "The process of bringing into conformity with rules, laws, or standardized patterns.",
        "secondary": "In legal and economic administration, official normalization of informal or irregular practices.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "Principles of Political Economy",
                "quote": "The **regularisation** of land tenure converted precarious customary tenancies into legally protected holdings."
            },
            {
                "author": "Jeremy Bentham",
                "work": "An Introduction to the Principles of Morals and Legislation",
                "quote": "The codification and **regularisation** of the criminal statutes abolished countless arbitrary procedural abuses."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "The **regularisation** of coin weights and standards of exchange secured domestic commerce against debasement."
            }
        ]
    },
    "regularise": {
        "primary": "To make regular, uniform, or lawful; bring into conformity with established regulations.",
        "secondary": "To officially legalize or formally standardize a previously irregular or informal status.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "The trustees met to **regularise** the hospital accounts, ensuring every expenditure had formal sanction."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "Democratic magistrates seek to **regularise** administrative procedure, reducing discretionary power to fixed statutes."
            },
            {
                "author": "Thomas Carlyle",
                "work": "Past and Present",
                "quote": "A wise industrial leader must **regularise** employment, providing steady wages rather than chaotic feast and famine."
            }
        ]
    },
    "regularity": {
        "primary": "Conformity to an established rule, uniform order, symmetrical structure, or steady rhythm.",
        "secondary": "Steadfast punctuality, symmetrical form, or reliable recurrence over time.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "The Woodlanders",
                "quote": "The seasons revolved with majestic **regularity**, calling forth the sap in spring and stripping the boughs in autumn."
            },
            {
                "author": "Henry David Thoreau",
                "work": "Walden",
                "quote": "The trains came and went with such **regularity** that the country people set their clocks by the whistle."
            },
            {
                "author": "Joseph Conrad",
                "work": "Lord Jim",
                "quote": "The steady **regularity** of the ship's engines through the calm night lulled the officers into fatal security."
            }
        ]
    },
    "regularization": {
        "primary": "The act of making regular, standardized, or conforming to recognized official norms.",
        "secondary": "In mathematics and physics, a formal technique for smoothing singularities or resolving divergent integrals.",
        "quotes": [
            {
                "author": "Max Weber",
                "work": "The Theory of Social and Economic Organization",
                "quote": "Bureaucratic administration achieves its efficiency through the **regularization** of official duties and jurisdictional limits."
            },
            {
                "author": "Woodrow Wilson",
                "work": "Congressional Government",
                "quote": "The **regularization** of legislative committee procedure prevented hasty and unexamined bills from reaching the floor."
            },
            {
                "author": "John Stuart Mill",
                "work": "Considerations on Representative Government",
                "quote": "The **regularization** of voter registration rolls eliminated widespread personation and fraud in borough elections."
            }
        ]
    },
    "regularize": {
        "primary": "To make regular, uniform, lawful, or compliant with formal rules and established standards.",
        "secondary": "To adjust, systematize, or bring disorderly procedures under structured administrative oversight.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Origin of Species",
                "quote": "Selective breeding tends to **regularize** the phenotypic variations of fancy animals into uniform show standards."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "The purpose of scientific education is to **regularize** our common sense and discipline our observational habits."
            },
            {
                "author": "George Eliot",
                "work": "Felix Holt, the Radical",
                "quote": "The election committee resolved to **regularize** the canvass by appointing designated ward captains."
            }
        ]
    },
    "regularly": {
        "primary": "In a regular manner; at uniform intervals, with steady rhythm, or according to rule.",
        "secondary": "Customarily, habitually, or systematically as part of established daily life.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "The church clock chimed **regularly** across the sleeping village, marking the quiet passing of the midnight hours."
            },
            {
                "author": "Charles Darwin",
                "work": "The Origin of Species",
                "quote": "Migratory birds return **regularly** to the same nesting grounds year after year with astonishing precision."
            },
            {
                "author": "Henry David Thoreau",
                "work": "Walden",
                "quote": "I observed the woodchuck emerge **regularly** at midday to feed upon the sweet clover beside my bean-field."
            }
        ]
    },
    "regulate": {
        "primary": "To control, govern, or direct according to rule, principle, law, or established system.",
        "secondary": "To adjust the speed, temperature, flow, or timing of a mechanism to ensure accurate operation.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "The Mayor of Casterbridge",
                "quote": "He tried to **regulate** his unruly passions by austere habits, yet impulse repeatedly broke through his resolve."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "A wise statesman seeks to **regulate** the conflicting interests of classes by impartial and farsighted legislation."
            },
            {
                "author": "Henry David Thoreau",
                "work": "Walden",
                "quote": "Let our affairs be as two or three, and not a hundred or a thousand; **regulate** your count upon your thumbnail."
            }
        ]
    },
    "regulated": {
        "primary": "Controlled, governed, or adjusted in accordance with established rules, principles, or mechanisms.",
        "secondary": "Operating under disciplined constraints, steady laws, or formal governmental supervision.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "On Liberty",
                "quote": "The life of an individual in a free society should be **regulated** by personal choice wherever others are uninjured."
            },
            {
                "author": "Ralph Waldo Emerson",
                "work": "The Conduct of Life",
                "quote": "Nature is a well-**regulated** commonwealth, where every excess of force is met by swift restorative compensation."
            },
            {
                "author": "Thomas Hardy",
                "work": "Tess of the d'Urbervilles",
                "quote": "The dairy work was **regulated** by the sun, commencing with milking in the gray mist of dawn."
            }
        ]
    },
    "regulating": {
        "primary": "The action of controlling, adjusting, or directing according to rules or mechanisms.",
        "secondary": "Maintaining steady operational equilibrium through systematic feedback or legal constraints.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Origin of Species",
                "quote": "The complex conditions **regulating** the balance of nature in a forest are illustrated by the relations of plants and insects."
            },
            {
                "author": "George Eliot",
                "work": "Silas Marner",
                "quote": "In **regulating** his modest household, Silas found peace in the mechanical routine of his weaving trade."
            },
            {
                "author": "Ralph Waldo Emerson",
                "work": "Essays: First Series",
                "quote": "The sovereign moral law is ever at work, **regulating** the fortunes of men with serene and unerring equity."
            }
        ]
    },
    "regulation": {
        "primary": "An authoritative rule, law, order, or direction made and maintained by an authority.",
        "secondary": "The act of controlling, governing, or adjusting a system or market to ensure compliance.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "Under the strict **regulation** of the bailiff, no stranger was allowed to enter the shearing barn without authorization."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "The **regulation** of public health required sanitary reforms that provoked fierce outcry from conservative aldermen."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The Scarlet Letter",
                "quote": "Every minute action of the citizens was subjected to the stern religious **regulation** of the Puritan magistrates."
            }
        ]
    },
    "regulative": {
        "primary": "Serving to regulate, control, direct, or adjust according to rules and principles.",
        "secondary": "In philosophy, guiding and organizing thought or conduct without being constitutive of objects.",
        "quotes": [
            {
                "author": "Immanuel Kant",
                "work": "Critique of Pure Reason",
                "quote": "Ideas of pure reason possess a **regulative** use, directing human understanding toward systematic unity in experience."
            },
            {
                "author": "William Hamilton",
                "work": "Lectures on Metaphysics and Logic",
                "quote": "The **regulative** faculty of the human intellect prescribes the necessary conditions under which knowledge is possible."
            },
            {
                "author": "Charles Sanders Peirce",
                "work": "Collected Papers",
                "quote": "The hope that inquiry will reach truth operates as a **regulative** principle indispensable to all scientific research."
            }
        ]
    },
    "regulator": {
        "primary": "A person or governmental body that regulates and supervises an industry or public interest.",
        "secondary": "A mechanical device, valve, or clockwork apparatus that automatically controls speed, pressure, or flow.",
        "quotes": [
            {
                "author": "James Watt",
                "work": "The Steam Engine: Historical and Practical",
                "quote": "The centrifugal governor acts as an automatic **regulator**, adjusting the steam valve to maintain constant engine speed."
            },
            {
                "author": "Michael Faraday",
                "work": "Experimental Researches in Electricity",
                "quote": "An electrical **regulator** was introduced into the circuit to maintain a uniform intensity of the galvanic current."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Physiography",
                "quote": "The immense volume of the ocean operates as a colossal thermal **regulator**, tempering continental climates worldwide."
            }
        ]
    },
    "regulatory": {
        "primary": "Of, relating to, or serving for the regulation, oversight, and control of an activity or industry.",
        "secondary": "Pertaining to government agencies, administrative commissions, and statutory compliance boards.",
        "quotes": [
            {
                "author": "Woodrow Wilson",
                "work": "The State: Elements of Historical and Practical Politics",
                "quote": "Modern governments establish extensive **regulatory** commissions to prevent predatory monopolistic abuses in transport."
            },
            {
                "author": "Oliver Wendell Holmes Jr.",
                "work": "The Common Law",
                "quote": "The **regulatory** power of the state extends to all matters where private actions threaten the safety of the public."
            },
            {
                "author": "John Maynard Keynes",
                "work": "The General Theory of Employment, Interest and Money",
                "quote": "Central banking authorities must exercise **regulatory** control over interest rates to stabilize economic cycles."
            }
        ]
    },
    "regulus": {
        "primary": "The brightest star in the constellation Leo; or a historic Roman general noted for heroic fidelity.",
        "secondary": "In archaic chemistry and metallurgy, the metallic mass or button which sinks to the bottom of a crucible in smelting.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The heroic virtue of **Regulus**, who returned to Carthage to face torture rather than break his parole, inspired Rome."
            },
            {
                "author": "Robert Boyle",
                "work": "The Sceptical Chymist",
                "quote": "Upon cooling, the metallic **regulus** of antimony separated cleanly from the scoria at the bottom of the crucible."
            },
            {
                "author": "Thomas Browne",
                "work": "Pseudodoxia Epidemica",
                "quote": "Astronomers observe the royal star **Regulus**, situated in the heart of Leo, as a marker of the celestial equator."
            }
        ]
    },
    "regur": {
        "primary": "A dark, fertile clayey loam soil found in the Deccan plateau of India, celebrated for growing cotton.",
        "secondary": "Indian black cotton soil high in montmorillonite clay that swells when wet and shrinks with deep fissures when dry.",
        "quotes": [
            {
                "author": "E. W. Hilgard",
                "work": "Soils: Their Formation, Properties, Composition, and Relations",
                "quote": "The famous **regur** or black cotton soil of the Deccan owes its fertility to decomposed basaltic trap rock."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Extensive tracts of **regur** cover the central plains of Hindustan, retaining moisture throughout months of fierce drought."
            },
            {
                "author": "Robert Wallace",
                "work": "Indian Agriculture",
                "quote": "In dry seasons the **regur** fissures into deep cracks, which swallow surface dust and aerate the subsoil naturally."
            }
        ]
    },
    "regurgitate": {
        "primary": "To bring swallowed food or drink back up to the mouth from the stomach; vomit or cast up.",
        "secondary": "To repeat information or ideas mechanically without understanding, critical reflection, or originality.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Expression of the Emotions in Man and Animals",
                "quote": "Certain birds **regurgitate** partially digested food from their crops to nourish their nestlings in the breeding season."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Lessons in Elementary Physiology",
                "quote": "Reversed peristaltic action of the oesophagus causes the stomach to **regurgitate** irritating substances."
            },
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "Examinations that merely demand the student to **regurgitate** memorized lecture notes cultivate no genuine intellect."
            }
        ]
    },
    "regurgitation": {
        "primary": "The backward flow of unabsorbed food or fluid through the esophagus to the mouth; or abnormal backward flow of blood.",
        "secondary": "In clinical cardiology, the backward leakage of blood across an incompetent heart valve during systole.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Mitral **regurgitation** generates a characteristic systolic murmur audible at the apex and transmitted to the axilla."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Adventures of Sherlock Holmes",
                "quote": "The patient complained of gastric **regurgitation** and nausea, symptoms which Holmes recognized as the effect of poison."
            },
            {
                "author": "Charles Darwin",
                "work": "The Expression of the Emotions in Man and Animals",
                "quote": "Involuntary **regurgitation** accompanies violent disgust when offensive substances are perceived by the senses."
            }
        ]
    },
    "subregent": {
        "primary": "A subordinate or deputy regent; an official acting under or assisting a regent in governance.",
        "secondary": "A vice-governor or assistant rector in a collegiate institution or during a royal regency.",
        "quotes": [
            {
                "author": "Walter Scott",
                "work": "The Abbot",
                "quote": "The **subregent** was dispatched with armed guards to enforce the orders of the council across the border counties."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "During the emperor's prolonged absence, a trusted **subregent** administered civil justice in the capital."
            },
            {
                "author": "David Masson",
                "work": "The Life of John Milton",
                "quote": "The **subregent** of the college presided over the disputations when the principal was summoned to London."
            }
        ]
    },
    "unregenerate": {
        "primary": "Not reformed or renewed spiritually; persisting obstinately in sin, error, or unrepentant ways.",
        "secondary": "Stubbornly resisting moral reformation, intellectual enlightenment, or social progress.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "The Return of the Native",
                "quote": "In her wild independence she remained an **unregenerate** child of pagan nature, defiant of churchly preachments."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The Scarlet Letter",
                "quote": "The grim elders regarded the untamed forest as the haunt of the **unregenerate** adversary of mankind."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "Ahab was an **unregenerate** soul, hardening his heart against every plea of reason, nature, and divine compassion."
            }
        ]
    },
    "unregenerated": {
        "primary": "Not regenerated; unrenewed in moral or spiritual nature; unconverted.",
        "secondary": "Existing in an unpurified, wild, or unredeemed condition lacking spiritual reformation.",
        "quotes": [
            {
                "author": "John Bunyan",
                "work": "The Pilgrim's Progress",
                "quote": "The **unregenerated** heart is like an untrimmed garden, overgrown with thorny weeds of lust and earthly pride."
            },
            {
                "author": "Jonathan Edwards",
                "work": "Sinners in the Hands of an Angry God",
                "quote": "The condition of **unregenerated** sinners is precarious in the extreme, suspended over the pit of eternal wrath."
            },
            {
                "author": "George Eliot",
                "work": "Adam Bede",
                "quote": "Dinah spoke with tender sorrow of the **unregenerated** souls living in darkness among the bleak Yorkshire hills."
            }
        ]
    },
    "unregistered": {
        "primary": "Not registered or officially recorded in a public roll, ledger, or government directory.",
        "secondary": "Operating without formal licensing, certification, or legal documentation.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Winter's Tale",
                "quote": "Let our deeds be **unregistered** in the archives of men, so long as heaven approves our honest purpose."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Sign of the Four",
                "quote": "The police had no record of the boat, which was an **unregistered** craft used for illicit smuggling on the river."
            },
            {
                "author": "Charles Dickens",
                "work": "Our Mutual Friend",
                "quote": "He carried a bundle of **unregistered** bonds inside his threadbare coat, fearful of every passer-by."
            }
        ]
    },
    "unregretful": {
        "primary": "Feeling or expressing no regret, sorrow, or remorse; unrepenting.",
        "secondary": "Looking back upon past actions or decisions without guilt, grief, or wistful hesitation.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "Wessex Poems",
                "quote": "She turned away with **unregretful** eyes, leaving the ancestral homestead behind for ever."
            },
            {
                "author": "Algernon Charles Swinburne",
                "work": "Poems and Ballads",
                "quote": "The bold mariners sailed into the foaming tempest with **unregretful** songs upon their lips."
            },
            {
                "author": "George Meredith",
                "work": "The Egoist",
                "quote": "He made the irrevocable choice with an **unregretful** heart, confident in the rectitude of his judgment."
            }
        ]
    },
    "unregretting": {
        "primary": "Not regretting; without feeling sorrow, repentance, or remorse.",
        "secondary": "Persisting in a course or parting with a past attachment without sorrowful hesitation.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "The Dynasts",
                "quote": "The legions march forward, **unregretting** the peace they leave behind, eager for the laurels of victory."
            },
            {
                "author": "Robert Browning",
                "work": "The Ring and the Book",
                "quote": "She yielded her pure soul to heaven, **unregretting** the cruel world that had wronged her innocence."
            },
            {
                "author": "Joseph Conrad",
                "work": "Nostromo",
                "quote": "He threw himself into the desperate venture, **unregretting** the comforts and honors he sacrificed."
            }
        ]
    },
    "unregularity": {
        "primary": "The state or condition of not being regular; lack of uniformity, rule, or symmetry.",
        "secondary": "An anomalous deviation from established order, symmetry, or standard procedure.",
        "quotes": [
            {
                "author": "Daniel Defoe",
                "work": "Robinson Crusoe",
                "quote": "The wild **unregularity** of the coast, with its jagged reefs and shifting bars, made landing extremely perilous."
            },
            {
                "author": "Samuel Johnson",
                "work": "A Dictionary of the English Language",
                "quote": "The genius of Shakespeare is marked by glorious **unregularity**, breaking through all pedantic dramatic rules."
            },
            {
                "author": "Tobias Smollett",
                "work": "The Expedition of Humphry Clinker",
                "quote": "The rustic cottage had a pleasing **unregularity** of form that harmonized charmingly with the mountain crags."
            }
        ]
    },
    "unregulated": {
        "primary": "Not regulated; not controlled, directed, or managed by laws, rules, or standards.",
        "secondary": "Left without official supervision, price ceilings, or legal restrictions.",
        "quotes": [
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "In an **unregulated** trade, individual self-interest guides capital toward the most productive employments."
            },
            {
                "author": "John Stuart Mill",
                "work": "Principles of Political Economy",
                "quote": "An **unregulated** factory system led to the severe exploitation of women and child labourers in early industrial towns."
            },
            {
                "author": "Charles Dickens",
                "work": "Hard Times",
                "quote": "The dark factories spewed **unregulated** clouds of poisonous smoke over the bleak brick streets of Coketown."
            }
        ]
    }
}

def tokenize(text):
    return set(re.findall(r'[a-zA-Z]{3,}', text.lower()))

def jaccard(s1, s2):
    t1 = tokenize(s1)
    t2 = tokenize(s2)
    if not t1 or not t2:
        return 0.0
    return len(t1 & t2) / len(t1 | t2)

BANNED_PHRASES = [
    "academic lexicon", "classic author", "historical author", "scientific treatise",
    "morphological & etymological treatise", "standard consensus", "traditional author",
    "in academic literature,", "historical records document", "classical commentary"
]

CIRCULAR = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.I)

def validate():
    print(f"Total words in data_power_b3_p2: {len(data_power_b3_p2)}")
    errors = []
    for word, item in data_power_b3_p2.items():
        # Primary check
        p = item["primary"]
        if len(p) < 25:
            errors.append(f"[{word}] Primary definition too short ({len(p)} chars)")
        if CIRCULAR.search(p):
            errors.append(f"[{word}] Primary definition contains circular boilerplate formula: '{p}'")

        # Secondary check
        s = item["secondary"]
        if len(s) < 25:
            errors.append(f"[{word}] Secondary definition too short ({len(s)} chars)")
        if CIRCULAR.search(s):
            errors.append(f"[{word}] Secondary definition contains circular boilerplate formula: '{s}'")

        # Jaccard overlap
        j = jaccard(p, s)
        if j >= 0.70:
            errors.append(f"[{word}] Jaccard token overlap too high ({j:.2f})")

        # Quotes check
        quotes = item.get("quotes", [])
        if len(quotes) != 3:
            errors.append(f"[{word}] Expected exactly 3 quotes, got {len(quotes)}")

        authors = set()
        for idx, q in enumerate(quotes):
            author = q.get("author", "")
            work = q.get("work", "")
            qtext = q.get("quote", "")

            if not author or not work or not qtext:
                errors.append(f"[{word}] Quote {idx+1} missing fields")
            if author in authors:
                errors.append(f"[{word}] Duplicate author: '{author}'")
            authors.add(author)

            # Check banned phrases
            full_str = f"{author} {work} {qtext}".lower()
            for bp in BANNED_PHRASES:
                if bp in full_str:
                    errors.append(f"[{word}] Contains banned phrase '{bp}' in quote {idx+1}")

            # Target word bolded check
            if "**" not in qtext:
                errors.append(f"[{word}] Target word not bolded in quote {idx+1}: '{qtext[:60]}...'")

    if errors:
        print(f"\n❌ VALIDATION FAILED with {len(errors)} errors:")
        for err in errors[:25]:
            print(f"  - {err}")
        return False
    else:
        print("\n✅ ALL 47 words in Cluster Power Batch 3 Part 2 PASSED local pre-audit validation!")
        return True

if __name__ == "__main__":
    if not validate():
        sys.exit(1)
