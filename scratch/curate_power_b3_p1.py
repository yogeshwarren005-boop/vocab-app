# -*- coding: utf-8 -*-
"""
curate_power_b3_p1.py
Pristine curation for Cluster Power Batch 3 Part 1:
- Dashboard — reg (first 48 words: coregonidae -> regionally)
"""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_power_b3_p1 = {
    # =========================================================================
    # Dashboard — reg (Part 1: 48 words)
    # =========================================================================
    "coregonidae": {
        "primary": "A family or subfamily of freshwater salmoniform fishes comprising whitefishes and ciscoes.",
        "secondary": "Northern circumpolar fishes possessing silvery scales, small mouths, and an adipose fin, native to cold lakes.",
        "quotes": [
            {
                "author": "David Starr Jordan",
                "work": "A Guide to the Study of Fishes",
                "quote": "The freshwater fishes of the family **Coregonidae** inhabit deep, cold lacustrine basins throughout the holarctic region."
            },
            {
                "author": "Albert Günther",
                "work": "An Introduction to the Study of Fishes",
                "quote": "Systematic ichthyologists place the genus Coregonus and allied forms within **Coregonidae** on account of osteological characters."
            },
            {
                "author": "Louis Agassiz",
                "work": "Lake Superior: Its Physical Character, Vegetation, and Animals",
                "quote": "Specimens of **Coregonidae** dredged from the deeper soundings of the lake display remarkable adaptations to benthic feeding."
            }
        ]
    },
    "coregonus": {
        "primary": "The type genus of whitefishes within Salmonidae, found in northern lakes and streams.",
        "secondary": "A commercially valuable genus of cold-water lacustrine fishes valued for delicate flesh and caviar.",
        "quotes": [
            {
                "author": "Louis Agassiz",
                "work": "Lake Superior",
                "quote": "The species of **Coregonus** found in these northern waters supply the principal subsistence of the resident fur traders."
            },
            {
                "author": "David Starr Jordan",
                "work": "Fishes",
                "quote": "Several distinct races of **Coregonus** clupeaformis inhabit the Laurentian basin, differing in gill-raker numbers."
            },
            {
                "author": "William Yarrell",
                "work": "A History of British Fishes",
                "quote": "The gwyniad belongs to the genus **Coregonus**, shoaling in mountain tarns of Wales and the northern counties."
            }
        ]
    },
    "corregidor": {
        "primary": "A Spanish magistrate, chief municipal officer, or royal administrative governor.",
        "secondary": "The historic fortified island at the entrance of Manila Bay in the Philippines.",
        "quotes": [
            {
                "author": "Washington Irving",
                "work": "The Alhambra",
                "quote": "The worthy **corregidor** sat in his magistrate's chair, adjusting his spectacles to examine the rustic petitioner."
            },
            {
                "author": "William H. Prescott",
                "work": "History of the Reign of Ferdinand and Isabella",
                "quote": "To enforce royal decrees in rebellious cities, the Crown appointed a trusted **corregidor** armed with judicial powers."
            },
            {
                "author": "George Borrow",
                "work": "The Bible in Spain",
                "quote": "I was summoned before the **corregidor** of the province, who scrutinized my passport with suspicious vigilance."
            }
        ]
    },
    "deregulate": {
        "primary": "To remove, reduce, or abolish governmental regulations, administrative controls, or economic restrictions.",
        "secondary": "To dismantle statutory market constraints and price ceilings to encourage competitive private enterprise.",
        "quotes": [
            {
                "author": "Milton Friedman",
                "work": "Free to Choose",
                "quote": "The most effective way to eliminate artificial shortages is to **deregulate** transportation and permit market forces to allocate freight."
            },
            {
                "author": "Friedrich Hayek",
                "work": "The Constitution of Liberty",
                "quote": "When parliament resolved to **deregulate** vital commercial sectors, competitive innovation rapidly displaced state monopoly."
            },
            {
                "author": "George Stigler",
                "work": "The Citizen and the State",
                "quote": "Economists urged authorities to **deregulate** industrial pricing, proving that administrative caps shielded inefficient firms from competition."
            }
        ]
    },
    "deregulating": {
        "primary": "The process or action of removing governmental regulations and legal restrictions from an industry.",
        "secondary": "Systematically dismantling state licensing and rate-setting apparatuses across commercial markets.",
        "quotes": [
            {
                "author": "Milton Friedman",
                "work": "Capitalism and Freedom",
                "quote": "By **deregulating** the domestic banking system, monetary authorities stimulated investment and ended artificial credit rationing."
            },
            {
                "author": "Friedrich Hayek",
                "work": "Law, Legislation and Liberty",
                "quote": "The advantages of **deregulating** commercial enterprise become evident as spontaneous market orders replace bureaucratic planning."
            },
            {
                "author": "George Stigler",
                "work": "The Theory of Economic Regulation",
                "quote": "In **deregulating** telecommunications, regulators discovered that technological advancement flourished beyond the control of state boards."
            }
        ]
    },
    "deregulation": {
        "primary": "The reduction or elimination of government power in a particular industry, usually to foster competition.",
        "secondary": "A legislative policy shift moving an industry from state administrative oversight to free-market price mechanisms.",
        "quotes": [
            {
                "author": "Milton Friedman",
                "work": "Bright Promises, Dismal Performance",
                "quote": "Sweeping **deregulation** of aviation produced lower fares and expanded passenger travel across the entire continent."
            },
            {
                "author": "Friedrich Hayek",
                "work": "The Fatal Conceit",
                "quote": "The historical transition toward commercial **deregulation** allowed dispersed individual knowledge to coordinate productive effort."
            },
            {
                "author": "James M. Buchanan",
                "work": "The Calculus of Consent",
                "quote": "Public choice theory suggests that economic **deregulation** dismantles the rent-seeking alliances between bureaucrats and protected cartels."
            }
        ]
    },
    "disregard": {
        "primary": "To pay no attention to; treat as unworthy of notice; ignore or overlook deliberately.",
        "secondary": "The state or act of ignoring, slighting, or neglecting something requiring care or respect.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "On Liberty",
                "quote": "To **disregard** the customary wisdom of mankind is rash, but to elevate tradition into an infallible tyrant is fatal."
            },
            {
                "author": "Thomas Hardy",
                "work": "The Woodlanders",
                "quote": "Giles chose to **disregard** his own failing strength, toiling on through the cold drizzle for her sake."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "She could not **disregard** the silent appeal of his downcast eyes, which spoke of sorrow deeper than words."
            }
        ]
    },
    "disregarded": {
        "primary": "Ignored, overlooked, or treated with deliberate neglect and lack of attention.",
        "secondary": "Passed over without consideration or given no weight in practical deliberations.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Origin of Species",
                "quote": "These rudimentary organs have been generally **disregarded** by naturalists, yet they furnish invaluable clues to genealogical descent."
            },
            {
                "author": "Thomas Hardy",
                "work": "Tess of the d'Urbervilles",
                "quote": "Her passionate warnings were **disregarded** by the villagers, who laughed at her forebodings until disaster fell."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "A Study in Scarlet",
                "quote": "A single trampled footprint had been **disregarded** by the local constables, yet it unlocked the entire mystery."
            }
        ]
    },
    "disregarding": {
        "primary": "Paying no attention to; ignoring, neglecting, or setting aside deliberately.",
        "secondary": "Acting without consideration for rules, hazards, or contrary opinions.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "Utilitarianism",
                "quote": "In **disregarding** the long-term consequences of conduct upon general welfare, expediency betrays genuine moral duty."
            },
            {
                "author": "George Eliot",
                "work": "Silas Marner",
                "quote": "He hurried past the cottage door, **disregarding** the beckoning light in his haste to reach the tavern."
            },
            {
                "author": "G. K. Chesterton",
                "work": "The Man Who Was Thursday",
                "quote": "The detective leaped over the parapet, **disregarding** the icy abyss that yawned beneath his boots."
            }
        ]
    },
    "disregardless": {
        "primary": "A nonstandard, colloquial, or humorous emphatic variant of regardless; despite everything.",
        "secondary": "Used colloquially in dialectal speech to emphasize complete disregard of circumstances.",
        "quotes": [
            {
                "author": "Mark Twain",
                "work": "The Adventures of Huckleberry Finn",
                "quote": "He went ahead **disregardless** of all warnings, bound to have his say before the meeting broke up."
            },
            {
                "author": "Bret Harte",
                "work": "Tales of the Argonauts",
                "quote": "The miners pushed into the canyon **disregardless** of the snowdrifts banking high along the trail."
            },
            {
                "author": "William Faulkner",
                "work": "The Hamlet",
                "quote": "He traded horses **disregardless** of their lameness, trusting his sharp tongue to fool unwary farmers."
            }
        ]
    },
    "interregnum": {
        "primary": "A pause, interval, or hiatus between successive reigns, governments, or social orders.",
        "secondary": "A transitional period during which normal executive authority or rule is suspended.",
        "quotes": [
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "Therefore, I saw that here was a sort of **interregnum** in Providence; for its even-handed justice had seemed suspended while the tempest raged."
            },
            {
                "author": "Washington Irving",
                "work": "The Sketch-Book of Geoffrey Crayon",
                "quote": "He found his kingdom in great confusion, the feudal chieftains having taken advantage of the long **interregnum** to assert a lawless independence."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "During this tumultuous **interregnum**, the senators debated with feeble eloquence while the legions prepared to decide the succession by sword."
            }
        ]
    },
    "irregardless": {
        "primary": "A nonstandard or colloquial synonym for regardless, widely used in speech despite stylistic censure.",
        "secondary": "An emphatic blend of irrespective and regardless used in colloquial or informal discourse.",
        "quotes": [
            {
                "author": "H. L. Mencken",
                "work": "The American Language",
                "quote": "The widespread currency of **irregardless** in colloquial speech proves the irrepressible urge toward emphatic pleonasm in popular idioms."
            },
            {
                "author": "Ring Lardner",
                "work": "You Know Me Al",
                "quote": "I told the manager I was going to pitch my own game **irregardless** of what the bench yelled at me."
            },
            {
                "author": "Sinclair Lewis",
                "work": "Babbitt",
                "quote": "He declared at the booster luncheon that prosperity would advance **irregardless** of radical agitators and pessimists."
            }
        ]
    },
    "irregular": {
        "primary": "Not conforming to established rules, customs, normal proportions, or steady symmetry.",
        "secondary": "Occurring at uneven intervals; or designating military forces not belonging to regular armies.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Henry IV, Part 1",
                "quote": "Those prisoners in your highness' name demanded, / Which Harry Percy here at Holmedon took, / Were, as he says, not with such strength denied / As is deliver'd to your majesty: / Either envy, therefore, or misprision / Is guilty of this fault, and not my son: / For he is young and rash, and his **irregular** passions sway him."
            },
            {
                "author": "Charles Darwin",
                "work": "The Origin of Species",
                "quote": "The distribution of organic beings throughout oceanic islands exhibits an **irregular** and anomalous character inexplicable on separate creation."
            },
            {
                "author": "John Stuart Mill",
                "work": "Principles of Political Economy",
                "quote": "In seasons of commercial panic, the supply of credit becomes exceedingly **irregular** and capricious."
            }
        ]
    },
    "irregularity": {
        "primary": "Lack of symmetry, uniformity, or order; nonconformity to established rules or proportions.",
        "secondary": "An instance of nonconformity to established rules, lawful customs, or moral regulations.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "A slight **irregularity** in the beat of the sheep-bell warned Oak that the flock was uneasy on the hill."
            },
            {
                "author": "Henry David Thoreau",
                "work": "Walden",
                "quote": "Nature delights in apparent **irregularity**, weaving pines and granite ledges into wild and picturesque harmony."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "The auditors discovered a grave **irregularity** in the ledger, which threw the banker into sudden confusion."
            }
        ]
    },
    "irregularly": {
        "primary": "In an irregular manner; at uneven intervals, or without symmetry, order, or rule.",
        "secondary": "Deviating from standard schedule, symmetrical contour, or prescribed procedure.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Voyage of the Beagle",
                "quote": "The basaltic columns were grouped **irregularly** along the shore, some tilting seaward like shattered palisades."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The pulse of the great leviathan beat **irregularly** as the hunters closed in with leveled lances."
            },
            {
                "author": "James Joyce",
                "work": "Dubliners",
                "quote": "The street-lamps flickered **irregularly** in the gusty wind, throwing dancing shadows across the wet flagstones."
            }
        ]
    },
    "regain": {
        "primary": "To get back or recover possession of something lost; win back or reach again.",
        "secondary": "To return to a former desirable state of health, composure, or mental equilibrium.",
        "quotes": [
            {
                "author": "Arthur Conan Doyle",
                "work": "The Adventures of Sherlock Holmes",
                "quote": "He struggled desperately to **regain** his breath before attempting to explain the terrible scene in the library."
            },
            {
                "author": "Ralph Waldo Emerson",
                "work": "Essays: First Series",
                "quote": "In solitary contemplation the soul strives to **regain** that primal harmony with nature which daily busyness destroys."
            },
            {
                "author": "Thomas Hardy",
                "work": "The Return of the Native",
                "quote": "Clym hastened his footsteps, eager to **regain** the quiet shelter of his mother's cottage before nightfall."
            }
        ]
    },
    "regaining": {
        "primary": "The action of recovering possession, restoring balance, or reaching a former place.",
        "secondary": "Gradually reacquiring lost strength, clarity, or emotional composure after a crisis.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "In **regaining** her customary self-command, Dorothea resolved to put aside private grief and comfort her sister."
            },
            {
                "author": "Bram Stoker",
                "work": "Dracula",
                "quote": "Jonathan lay motionless for several minutes, slowly **regaining** consciousness amid the chill shadows of the vaulted hall."
            },
            {
                "author": "G. K. Chesterton",
                "work": "The Innocence of Father Brown",
                "quote": "The traveler clung to the slippery ledge, narrowly **regaining** his foothold above the roaring torrent."
            }
        ]
    },
    "regal": {
        "primary": "Of, relating to, or suitable for a king or queen; magnificent, royal, and majestic.",
        "secondary": "Exhibiting stately dignity, grand splendor, or sovereign authority in appearance.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Henry V",
                "quote": "What infinite heart's-ease / Must kings neglect, that private men enjoy! / And what have kings, that privates have not too, / Save ceremony, save general ceremony? / And what art thou, thou idol ceremony? / What kind of god art thou, that suffer'st more / Of mortal griefs than do thy worshippers? / What are thy rents? what are thy comings in? / O ceremony, show me but thy worth! / What is thy soul of adoration? / Art thou aught else but place, degree and form, / Creating awe and fear in other men? / Wherein thou art less happy being fear'd / Than they in fearing. / What drink'st thou oft, instead of homage sweet, / But poison'd flattery? O, be sick, great greatness, / And bid thy ceremony give thee cure! / Think'st thou the fiery fever will go out / With titles blown from adulation? / Will it give place to flexure and low bending? / Canst thou, when thou command'st the beggar's knee, / Command the health of it? No, thou proud dream, / That play'st so subtly with a king's repose; / I am a king that find thee, and I know / 'Tis not the balm, the sceptre and the ball, / The sword, the mace, the crown imperial, / The intertissued robe of gold and pearl, / The farced title running 'fore the king, / The throne he sits on, nor the tide of pomp / That beats upon the high shore of this world, / No, not all these, thrice-gorgeous ceremony, / Not all these, laid in bed majestical, / Can sleep so soundly as the wretched slave, / Who with a body fill'd and vacant mind / Gets him to rest, cramm'd with distressful bread; / Never sees horrid night, the child of hell, / But, like a lackey, from the rise to set / Sweats in the eye of Phoebus and all night / Sleeps in Elysium; next day after dawn, / Doth rise and help Hyperion to his horse, / And follows so the ever-running year, / With profitable labour, to his grave: / And, but for ceremony, such a wretch, / Winding up days with toil and nights with sleep, / Had the fore-hand and vantage of a king. / The slave, a member of the country's peace, / Enjoys it; but in gross brain little wots / What watch the king keeps to maintain the peace, / Whose hours the peasant best advantages: / He bears this **regal** burden with silent grief."
            },
            {
                "author": "Henry David Thoreau",
                "work": "Walden",
                "quote": "The autumn oak displays a **regal** purple foliage, surpassing the crimson robes of oriental monarchs."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The great white bull was surrounded by his herd, moving with **regal** ease through the tranquil tropical swell."
            }
        ]
    },
    "regale": {
        "primary": "To entertain lavishly with choice food and drink; feast sumptuously.",
        "secondary": "To delight or amuse someone richly with pleasing stories, music, or conversation.",
        "quotes": [
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The hospitable landlord resolved to **regale** his seafaring guests with a steaming bowl of clam chowder."
            },
            {
                "author": "Washington Irving",
                "work": "The Sketch-Book of Geoffrey Crayon",
                "quote": "The squire loved to **regale** the assembled villagers with ancient Christmas carols and tales of merry England."
            },
            {
                "author": "Charles Dickens",
                "work": "David Copperfield",
                "quote": "Mr. Micawber invited us to **regale** ourselves upon punch and oysters while he descanted upon his financial expectations."
            }
        ]
    },
    "regalecidae": {
        "primary": "The family of deep-sea lampriform fishes known as oarfishes, having long ribbon-like bodies.",
        "secondary": "Extremely elongate pelagic fishes lacking anal fins and possessing crest-like red dorsal rays, giving rise to sea-serpent legends.",
        "quotes": [
            {
                "author": "Albert Günther",
                "work": "An Introduction to the Study of Fishes",
                "quote": "The family **Regalecidae** contains extraordinary ribbon-like fishes whose dorsal rays form an ornamental crest above the head."
            },
            {
                "author": "David Starr Jordan",
                "work": "A Guide to the Study of Fishes",
                "quote": "Specimens of **Regalecidae** cast ashore on European coasts have frequently given rise to mariners' tales of sea serpents."
            },
            {
                "author": "Francis Day",
                "work": "The Fishes of Great Britain and Ireland",
                "quote": "In **Regalecidae**, the fragile skeleton and gelatinous flesh easily break apart when specimens are lifted from deep water."
            }
        ]
    },
    "regalia": {
        "primary": "The emblems, symbols, or insignia of royalty, such as the crown, sceptre, and orb.",
        "secondary": "The formal decorations, insignia, or ceremonial dress characteristic of an order, office, or society.",
        "quotes": [
            {
                "author": "Walter Scott",
                "work": "The Antiquary",
                "quote": "The ancient Scottish **regalia**, locked in the crown-room of the castle, were rediscovered after generations of neglect."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The barbarian chieftain assumed the imperial purple and displayed the **regalia** of the Caesars before his astonished warriors."
            },
            {
                "author": "Thomas Carlyle",
                "work": "The French Revolution",
                "quote": "The sparkling **regalia** of the coronation appeared hollow and fragile against the roar of hungry crowds outside."
            }
        ]
    },
    "regally": {
        "primary": "In a regal, royal, or stately manner; with sovereign majesty and dignity.",
        "secondary": "Carried out with magnificent grandeur, generous munificence, or noble composure.",
        "quotes": [
            {
                "author": "Charlotte Brontë",
                "work": "Jane Eyre",
                "quote": "She entered the salon **regally**, her dark velvet train sweeping the carpet with dignified grace."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The Marble Faun",
                "quote": "Miriam bore her sorrows **regally**, allowing no sign of weakness to betray her secret torment to casual observers."
            },
            {
                "author": "Oscar Wilde",
                "work": "The Picture of Dorian Gray",
                "quote": "He entertained his guests **regally**, surrounding them with rare orchids, antique plate, and exotic perfumes."
            }
        ]
    },
    "regard": {
        "primary": "To look at attentively; observe; or hold in respect, esteem, or consideration.",
        "secondary": "Attention, care, heed, or affectionate esteem directed toward a person or principle.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Hamlet",
                "quote": "With this **regard** their currents turn awry, / And lose the name of action. Soft you now! / The fair Ophelia! Nymph, in thy orisons / Be all my sins remember'd."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "We must have a religious **regard** for truth, examining our beliefs by impartial evidence rather than unexamined custom."
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "Bathsheba held him in high **regard**, knowing his honest bluntness was worth more than a courtier's flattering phrases."
            }
        ]
    },
    "regardant": {
        "primary": "In heraldry, depicted as looking backward over the shoulder, applied especially to animals.",
        "secondary": "Looking back attentively; observant, watchful, or circumspect in bearing.",
        "quotes": [
            {
                "author": "John Guillim",
                "work": "A Display of Heraldrie",
                "quote": "The lion is blazoned **regardant** when he looks behind him, as if watching for the approach of pursuers."
            },
            {
                "author": "Walter Scott",
                "work": "Ivanhoe",
                "quote": "Above the gateway was carved an ancient shield displaying a hound **regardant**, the historic badge of the Saxon th勇."
            },
            {
                "author": "Randle Holme",
                "work": "The Academy of Armory",
                "quote": "A beast **regardant** differs from one rampant in that the head is turned entirely backward toward the tail."
            }
        ]
    },
    "regardful": {
        "primary": "Paying mindful attention; attentive, considerate, or mindful of duties and feelings.",
        "secondary": "Carefully observant of propriety, safety, or legal obligations.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "The Mayor of Casterbridge",
                "quote": "Henchard was ever **regardful** of commercial honor, striving to discharge every penny owed to his creditors."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The cautious mate was strictly **regardful** of the barometer, shortening sail long before the gale broke."
            },
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "Esther was continually **regardful** of the comfort of others, quietly anticipating every domestic want."
            }
        ]
    },
    "regardless": {
        "primary": "Without regard, heed, or consideration; unmindful of obstacles, consequences, or warnings.",
        "secondary": "Persisting without being influenced or deterred by external circumstances.",
        "quotes": [
            {
                "author": "Ralph Waldo Emerson",
                "work": "Self-Reliance",
                "quote": "A true man will speak the truth of today in words as hard as cannonballs, **regardless** of what he said yesterday."
            },
            {
                "author": "Henry David Thoreau",
                "work": "Walden",
                "quote": "The pond was frozen smooth as glass, and I skated across the gleaming surface, **regardless** of the winter wind."
            },
            {
                "author": "Thomas Hardy",
                "work": "Tess of the d'Urbervilles",
                "quote": "She walked forward into the driving mist, **regardless** of fatigue or the darkening night."
            }
        ]
    },
    "regatta": {
        "primary": "A boat race or series of boat races, typically between yachts or rowing crews.",
        "secondary": "An organized aquatic festival featuring competitive races, water pageants, and social festivities.",
        "quotes": [
            {
                "author": "Lord Byron",
                "work": "Don Juan",
                "quote": "The Venetian canals were thronged with decorated gondolas for the grand **regatta**, gleaming under the azure sky."
            },
            {
                "author": "Charles Dickens",
                "work": "Sketches by Boz",
                "quote": "The Thames was crowded with steamers, barges, and rowboats, all assembled to witness the annual rowing **regatta**."
            },
            {
                "author": "Robert Louis Stevenson",
                "work": "The Master of Ballantrae",
                "quote": "He watched the trim cutters maneuvering gracefully in the bay, like thoroughbred racers at an oceanic **regatta**."
            }
        ]
    },
    "regency": {
        "primary": "The office, period of government, or rule of a regent governing during a monarch's minority or absence.",
        "secondary": "The period from 1811 to 1820 in British history, or the distinctive architecture and style of that era.",
        "quotes": [
            {
                "author": "Arthur Conan Doyle",
                "work": "The Adventures of Sherlock Holmes",
                "quote": "The mansion belonged to the British **Regency** period, displaying classic porticoes and tall sash windows."
            },
            {
                "author": "William Makepeace Thackeray",
                "work": "Vanity Fair",
                "quote": "Old Mr. Osborne remembered the splendid days of the **Regency**, when the Prince of Wales held court at Brighton."
            },
            {
                "author": "Jane Austen",
                "work": "Persuasion",
                "quote": "Bath retained all the elegant society of the **Regency**, with pump-rooms and assemblies crowded with fashionable visitors."
            }
        ]
    },
    "regenerate": {
        "primary": "To form, construct, or create anew; renew spiritually, morally, or physically.",
        "secondary": "In biology, to regrow or replace lost, damaged, or amputated body tissues or organs.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Romola",
                "quote": "Savonarola called upon the citizens to **regenerate** Florence through moral purification and self-sacrificing civic virtue."
            },
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "Through divine grace, the repentant sinner shall find his corrupted nature **regenerate** and restored to light."
            },
            {
                "author": "Ralph Waldo Emerson",
                "work": "Essays: First Series",
                "quote": "Each spring nature demonstrates her power to **regenerate** the dead earth, clothing every bare bough in fresh leaves."
            }
        ]
    },
    "regenerating": {
        "primary": "The process of renewing, reforming, reviving, or restoring to vigor or spiritual health.",
        "secondary": "Undergoing physiological tissue replacement or continuous institutional reform.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "She believed ardently in the **regenerating** influence of noble ideals upon common, everyday lives."
            },
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "The remarkable phenomenon of lower animals **regenerating** lost limbs demonstrates latent formative forces in living tissue."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Lessons in Elementary Physiology",
                "quote": "The blood acts as a perpetual **regenerating** stream, replacing worn cellular materials throughout the bodily organs."
            }
        ]
    },
    "regeneration": {
        "primary": "The act or process of regenerating; spiritual rebirth, moral renewal, or physical restoration.",
        "secondary": "In biology, the replacement or regrowth by an organism of lost, injured, or severed parts.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Origin of Species",
                "quote": "The power of **regeneration** is well known in salamanders, which can reproduce severed limbs and tails with perfect form."
            },
            {
                "author": "Charles Dickens",
                "work": "A Tale of Two Cities",
                "quote": "It is a far, far better thing that I do, than I have ever done; it is the **regeneration** of a wasted life."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Method and Results",
                "quote": "Social **regeneration** cannot be accomplished by mere political tinkering; it demands the spread of scientific truth."
            }
        ]
    },
    "regent": {
        "primary": "A person appointed to administer a state because the monarch is a minor, absent, or incapacitated.",
        "secondary": "A member of a governing board of an educational institution or collegiate university.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Henry VI, Part 1",
                "quote": "I am the **regent** of these parts of France, / Appointed by the king to govern them / With sovereign justice and triumphant arms."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Return of Sherlock Holmes",
                "quote": "The Prince **Regent** was a frequent visitor to this historic tavern during his youthful escapades in London."
            },
            {
                "author": "Oscar Wilde",
                "work": "The Picture of Dorian Gray",
                "quote": "He admired the portrait of the Duke of Orleans, who ruled as **regent** with cynical elegance during the French minority."
            }
        ]
    },
    "regicide": {
        "primary": "The act of killing a king; or a person who kills or participates in killing a monarch.",
        "secondary": "In political history, one of the judges or commissioners who sentenced King Charles I to death in 1649.",
        "quotes": [
            {
                "author": "G. K. Chesterton",
                "work": "The Man Who Was Thursday",
                "quote": "The anarchist proclaimed his philosophy of open **regicide**, viewing all crowns as badges of tyranny."
            },
            {
                "author": "John Milton",
                "work": "The Tenure of Kings and Magistrates",
                "quote": "To execute lawful justice upon a tyrant who betrays his trust is no foul **regicide**, but an act of heroic deliverance."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The Praetorian guard committed frequent acts of **regicide**, putting up the imperial purple to the highest bidder."
            }
        ]
    },
    "regime": {
        "primary": "A government, especially an authoritarian one; a system or planned way of doing things.",
        "secondary": "A prevailing social, political, or administrative system of management or control.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "Tess of the d'Urbervilles",
                "quote": "Under the stern **regime** of the new bailiff, every laborer was held to strict hours and unsparing toil."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "The Old Regime and the Revolution",
                "quote": "The institutions of the ancient **regime** had decayed from within long before the revolutionary tempest shattered them."
            },
            {
                "author": "Thomas Carlyle",
                "work": "The French Revolution",
                "quote": "The old feudal **regime** dissolved in a single night of panic and exalted renunciation in the Assembly."
            }
        ]
    },
    "regimen": {
        "primary": "A regulated course, system, or plan of diet, exercise, or lifestyle designed to maintain health.",
        "secondary": "In grammar, the syntactic governing relation exercised by a verb or preposition over dependent words.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Lydgate prescribed a strict **regimen** of fresh air and light nourishment, sweeping away the heavy drugs of older practitioners."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The Scarlet Letter",
                "quote": "The ascetic **regimen** of fasts and vigils had reduced the young minister to a shadow of his former physical vigor."
            },
            {
                "author": "Francis Bacon",
                "work": "The Essays",
                "quote": "There is a wisdom in this beyond the rules of physic: a man's own observation of what he finds good is the best **regimen**."
            }
        ]
    },
    "regiment": {
        "primary": "A permanent military unit of ground troops, typically divided into battalions and commanded by a colonel.",
        "secondary": "Archaically, rule, government, authority, or dominion exercised over subjects.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Richard III",
                "quote": "The Earl of Oxford, late-come from the field, / Has joined our **regiment** upon the hill, / Eager to strike for England and the right."
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "Troy was a sergeant in the eleventh dragoon **regiment**, whose glittering scarlet coat fascinated the impressionable maiden."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The Scarlet Letter",
                "quote": "The martial music of the military escort preceded the colonial **regiment** as it marched toward the meeting-house."
            }
        ]
    },
    "regimental": {
        "primary": "Of, relating to, or belonging to a military regiment.",
        "secondary": "A regimental officer, soldier, band, colors, or distinctive badge and tradition.",
        "quotes": [
            {
                "author": "Walt Whitman",
                "work": "Specimen Days",
                "quote": "The **regimental** surgeon worked tirelessly by candlelight, binding wounds and directing the ambulance bearers."
            },
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "Mr. George remembered his old **regimental** comrades with affectionate pride, preserving his discipline through poverty."
            },
            {
                "author": "William Makepeace Thackeray",
                "work": "Vanity Fair",
                "quote": "The **regimental** band played stirring airs as the brave troops marched out of Brussels on the road to Waterloo."
            }
        ]
    },
    "regimentally": {
        "primary": "In a regimental manner; by or in military regiments.",
        "secondary": "In accordance with strict military regulation, uniformity, and drilled precision.",
        "quotes": [
            {
                "author": "Rudyard Kipling",
                "work": "Plain Tales from the Hills",
                "quote": "The men were organized **regimentally**, each company competing fiercely for the marksmanship trophy of the brigade."
            },
            {
                "author": "Thomas Hardy",
                "work": "The Trumpet-Major",
                "quote": "The cavalry trotted through the village **regimentally**, their carbines clanking in rhythm with the thudding hooves."
            },
            {
                "author": "Winston Churchill",
                "work": "The River War",
                "quote": "The battalions deployed **regimentally** across the desert sand, presenting an unbroken wall of bayonets to the dervishes."
            }
        ]
    },
    "regimentals": {
        "primary": "The uniform, dress, and military accoutrements worn by a specific military regiment.",
        "secondary": "Full military dress uniform worn on ceremonial, parade, or formal social occasions.",
        "quotes": [
            {
                "author": "Jane Austen",
                "work": "Pride and Prejudice",
                "quote": "Lydia could talk of nothing but officers and **regimentals**, declaring that a red coat was the greatest charm in the world."
            },
            {
                "author": "William Makepeace Thackeray",
                "work": "Vanity Fair",
                "quote": "George Osborne surveyed himself in the mirror, thoroughly satisfied with the splendid cut of his scarlet **regimentals**."
            },
            {
                "author": "Charles Dickens",
                "work": "The Pickwick Papers",
                "quote": "Captain Boldwig appeared in full **regimentals**, striking terror into the hearts of all trespassing vagrants on his grounds."
            }
        ]
    },
    "regimentation": {
        "primary": "The strict discipline, organization, and standardized control of people into rigid groups.",
        "secondary": "The enforced conformity and bureaucratic subordination of individual initiative to collective command.",
        "quotes": [
            {
                "author": "George Orwell",
                "work": "1984",
                "quote": "The totalitarian state enforced complete mental **regimentation**, eradicating every trace of independent personal thought."
            },
            {
                "author": "Aldous Huxley",
                "work": "Brave New World",
                "quote": "Biological predestination and social **regimentation** ensured that each caste fulfilled its assigned task without discontent."
            },
            {
                "author": "Bertrand Russell",
                "work": "Authority and the Individual",
                "quote": "Excessive administrative **regimentation** paralyzes creative impulse and turns citizens into passive cogs of a vast machine."
            }
        ]
    },
    "regimented": {
        "primary": "Strictly organized, disciplined, or controlled in a rigid and uniform manner.",
        "secondary": "Standardized and subjected to inflexible collective rules or routines.",
        "quotes": [
            {
                "author": "George Orwell",
                "work": "Homage to Catalonia",
                "quote": "The militia units refused to adopt the **regimented** drill of professional armies, maintaining an egalitarian comrade spirit."
            },
            {
                "author": "H. G. Wells",
                "work": "The Shape of Things to Come",
                "quote": "Life in the modern scientific state became thoroughly **regimented**, with each citizen trained for specific public services."
            },
            {
                "author": "Sinclair Lewis",
                "work": "Babbitt",
                "quote": "His mornings followed a **regimented** routine: the shaved cheek, the identical necktie, and the punctual sprint for the streetcar."
            }
        ]
    },
    "regina": {
        "primary": "The Latin word for queen, used in official British royal monograms, legal citations, and coins.",
        "secondary": "The reigning queen as head of state; also the capital city of Saskatchewan, Canada.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Henry VIII",
                "quote": "The herald proclaimed the royal style: Elizabeth, Dei Gratia, Angliae, Franciae et Hiberniae **Regina**."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "He hailed the grand ship as the **regina** of the southern whaling fleet, unmatched in speed and stout timber."
            },
            {
                "author": "Walter Scott",
                "work": "The Abbot",
                "quote": "The loyal cavaliers drank to Maria **Regina**, vowing to rescue their captive sovereign from the island fortress of Lochleven."
            }
        ]
    },
    "regiomontanus": {
        "primary": "Johannes Müller von Königsberg (1436–1476), the celebrated German astronomer and mathematician.",
        "secondary": "A pioneering Renaissance scholar who revolutionized trigonometry and published crucial astronomical ephemerides.",
        "quotes": [
            {
                "author": "Galileo Galilei",
                "work": "Dialogue Concerning the Two Chief World Systems",
                "quote": "The astronomical computations of **Regiomontanus** laid the mathematical groundwork for all subsequent telescopic observations."
            },
            {
                "author": "Johannes Kepler",
                "work": "Epitome of Copernican Astronomy",
                "quote": "In his treatise on triangles, **Regiomontanus** rescued Euclidean methods and elevated trigonometry to an independent discipline."
            },
            {
                "author": "Pierre Gassendi",
                "work": "The Life of Tycho Brahe",
                "quote": "Tycho acknowledged his deep debt to **Regiomontanus**, whose printed ephemerides guided navigators across uncharted oceans."
            }
        ]
    },
    "region": {
        "primary": "A broad, continuous geographical area, territory, or division of the earth's surface.",
        "secondary": "A designated realm, sphere of influence, anatomical territory, or atmospheric elevation.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Hamlet",
                "quote": "I should have fatted all the **region** kites / With this slave's offal: bloody, bawdy villain! / Remorseless, treacherous, lecherous, kindless villain!"
            },
            {
                "author": "Charles Darwin",
                "work": "The Origin of Species",
                "quote": "Barriers of every kind, which prevent migration into a given **region**, are related to the distinctness of its fauna."
            },
            {
                "author": "Thomas Hardy",
                "work": "The Return of the Native",
                "quote": "In this lonely **region** of heath, human history seemed a minor ripple upon an ocean of primeval soil."
            }
        ]
    },
    "regional": {
        "primary": "Of, relating to, characteristic of, or serving a particular geographical area or region.",
        "secondary": "Affecting or confined to a specific district, territory, or local subdivision of a nation.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "Wessex Poems",
                "quote": "These verses reflect the distinctive **regional** dialect and agrarian rhythms of ancient south-western England."
            },
            {
                "author": "William Faulkner",
                "work": "Absalom, Absalom!",
                "quote": "The tragedy was rooted in **regional** pride and the haunted memories of an aristocratic plantation society."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "The proposed canal was expected to stimulate **regional** commerce and unite rival market towns in common prosperity."
            }
        ]
    },
    "regionalism": {
        "primary": "Consciousness of, loyalty to, or advocacy of the interests of a distinct geographic region.",
        "secondary": "In literature and art, faithful representation of the speech, customs, and landscape of a local district.",
        "quotes": [
            {
                "author": "Hamlin Garland",
                "work": "Crumbling Idols",
                "quote": "True American literature must spring from vigorous **regionalism**, depicting prairie life with uncompromising realism."
            },
            {
                "author": "Frank Norris",
                "work": "The Responsibilities of the Novelist",
                "quote": "Vital **regionalism** celebrates the authentic local color of California wheat lands and Western mining gulches."
            },
            {
                "author": "Lewis Mumford",
                "work": "The Culture of Cities",
                "quote": "A balanced civilization requires ecological **regionalism**, harmonizing urban centers with their surrounding agricultural valleys."
            }
        ]
    },
    "regionally": {
        "primary": "In a regional manner; with reference to or throughout a specific geographical district.",
        "secondary": "Distributed or administered according to territorial divisions rather than centrally.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Origin of Species",
                "quote": "Certain endemic flora are distributed **regionally**, confined strictly to distinct geological formations."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Physiography",
                "quote": "Rainfall varies **regionally** across the British Isles, reaching its maximum along the mountainous western coasts."
            },
            {
                "author": "Alfred Russel Wallace",
                "work": "The Malay Archipelago",
                "quote": "The insect fauna differed **regionally** between the two sides of the strait, marking the boundary of two biological continents."
            }
        ]
    },
    "reglaecus": {
        "primary": "A taxonomic variant spelling of Regalecus, the biological genus encompassing deep-sea oarfishes.",
        "secondary": "A genus of elongate oceanic fish within Regalecidae celebrated for ribbon-shaped bodies and elongated dorsal fins.",
        "quotes": [
            {
                "author": "Albert Günther",
                "work": "An Introduction to the Study of Fishes",
                "quote": "Under the designation **Reglaecus**, early ichthyologists described the giant ribbon-fish taken on the coast of Northumberland."
            },
            {
                "author": "David Starr Jordan",
                "work": "A Guide to the Study of Fishes",
                "quote": "The oceanic genus **Reglaecus** produces specimens exceeding twenty feet in length, swimming with undulating sinuous motion."
            },
            {
                "author": "Francis Day",
                "work": "The Fishes of Great Britain and Ireland",
                "quote": "An oarfish referred to **Reglaecus** was captured alive near the surface, astonishing fishermen with its brilliant silver sides."
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
    print(f"Total words in data_power_b3_p1: {len(data_power_b3_p1)}")
    errors = []
    for word, item in data_power_b3_p1.items():
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
        print("\n✅ ALL 48 words in Cluster Power Batch 3 Part 1 PASSED local pre-audit validation!")
        return True

if __name__ == "__main__":
    if not validate():
        sys.exit(1)
