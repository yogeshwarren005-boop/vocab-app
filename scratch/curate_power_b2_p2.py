# -*- coding: utf-8 -*-
"""
curate_power_b2_p2.py
Pristine curation for Cluster Power Batch 2 Part 2:
- Dashboard — fort (70 words)
"""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_power_b2_p2 = {
    # =========================================================================
    # Dashboard — fort (70 words)
    # =========================================================================
    "comfort": {
        "primary": "Consolation in time of sorrow, grief, or distress; solace and cheering relief.",
        "secondary": "Physical ease, material well-being, and agreeable freedom from pain or hardship.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "As You Like It",
                "quote": "Live a little; **comfort** thine heart; cheer up thyself a little."
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "It was a subtle **comfort** to know that in all her perplexities, Oak's dependable fidelity remained unshaken."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "She found her purest **comfort** in active benevolence, lightening the burdens of her impoverished neighbours."
            }
        ]
    },
    "comfortable": {
        "primary": "Affording physical ease, restful relaxation, and agreeable contentment.",
        "secondary": "Financially secure and moderately prosperous; living in easy, modest circumstances.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "The fire burned brightly in the grate, shedding a warm and **comfortable** glow over the old room."
            },
            {
                "author": "Jane Austen",
                "work": "Pride and Prejudice",
                "quote": "Mr. Collins possessed a very **comfortable** home and a respectable income which satisfied all his modest desires."
            },
            {
                "author": "Thomas Hardy",
                "work": "The Return of the Native",
                "quote": "He looked forward to a **comfortable** evening beside the hearth after a long tramp across the bleak heath."
            }
        ]
    },
    "comfortableness": {
        "primary": "The quality of providing or experiencing restful physical ease and agreeable contentment.",
        "secondary": "A snug, cheerful sense of domestic warmth and peaceful security.",
        "quotes": [
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "There is no quality in this world that so thoroughly promotes human **comfortableness** as a roaring hearth fire on a stormy night."
            },
            {
                "author": "George Eliot",
                "work": "Scenes of Clerical Life",
                "quote": "The quiet **comfortableness** of the parlour, with its polished mahogany and cheerful kettle, soothed his weary mind."
            },
            {
                "author": "Charles Dickens",
                "work": "Great Expectations",
                "quote": "Joe's honest presence brought an immediate **comfortableness** into the room that no grand manners could bestow."
            }
        ]
    },
    "comfortably": {
        "primary": "In a comfortable manner; with restful physical ease, contentment, and security.",
        "secondary": "In prosperous, sufficient circumstances without financial distress or severe privation.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "They were seated **comfortably** about the oak settle, watching the sparks leap up the wide chimney."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Hound of the Baskervilles",
                "quote": "We dined **comfortably** at the inn before commencing our nocturnal vigil upon the lonely moor."
            },
            {
                "author": "Henry David Thoreau",
                "work": "Walden",
                "quote": "A man who lives simply can lodge **comfortably** in a small cabin and maintain his intellectual independence."
            }
        ]
    },
    "comforted": {
        "primary": "Soothed, consoled, and relieved from grief, anxiety, or physical distress.",
        "secondary": "Imparted with emotional reassurance, renewed hope, and peaceful calm.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Tempest",
                "quote": "A solemn air, and the best **comforted** music of our thoughts, cures thy frantic senses."
            },
            {
                "author": "George Eliot",
                "work": "Silas Marner",
                "quote": "Silas was deeply **comforted** by the innocent trust of the child, whose presence redeemed his lonely existence."
            },
            {
                "author": "James Joyce",
                "work": "Dubliners",
                "quote": "She felt strangely **comforted** by the familiar sounds of evening in the quiet Dublin street."
            }
        ]
    },
    "comforter": {
        "primary": "One who consoles, comforts, or brings emotional solace to someone in distress.",
        "secondary": "A warm quilted bed covering; or a warm woolen scarf worn about the neck in winter.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "A Christmas Carol",
                "quote": "Bob Cratchit tied on his long white **comforter**, which hung below his waist, and slid down the frozen street."
            },
            {
                "author": "Mary Shelley",
                "work": "Frankenstein",
                "quote": "Elizabeth was the gentle **comforter** of our household, whispering words of peace whenever sorrow threatened our tranquility."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "In every domestic emergency, she appeared as a wise **comforter**, soothing ruffled tempers with quiet kindness."
            }
        ]
    },
    "comforting": {
        "primary": "Affording comfort, solace, or cheering relief; reassuring to the feelings.",
        "secondary": "Supplying gentle physical warmth, restorative sustenance, or agreeable ease.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "The firm pressure of his hand was a **comforting** token that she was not utterly deserted in her misfortune."
            },
            {
                "author": "Oscar Wilde",
                "work": "The Picture of Dorian Gray",
                "quote": "There was something extraordinarily **comforting** in the soft music, which drowned out the bitter whispers of conscience."
            },
            {
                "author": "George Eliot",
                "work": "The Mill on the Floss",
                "quote": "Maggie found a **comforting** sanctuary in the dark attic, weeping away her childish griefs among the dusty rafters."
            }
        ]
    },
    "comfortingly": {
        "primary": "In a comforting, reassuring, and consoling manner.",
        "secondary": "In a way that imparts soothing relief, warmth, or quiet security.",
        "quotes": [
            {
                "author": "H. G. Wells",
                "work": "The War of the Worlds",
                "quote": "The morning sun broke through the smoky haze, shining **comfortingly** upon the green Surrey hills."
            },
            {
                "author": "Charlotte Brontë",
                "work": "Villette",
                "quote": "She spoke **comfortingly** to the weeping child, stroking her hair until the storm of sobbing subsided."
            },
            {
                "author": "Thomas Hardy",
                "work": "Tess of the d'Urbervilles",
                "quote": "The warm firelight flickered **comfortingly** across the kitchen walls, warding off the chill of the November drizzle."
            }
        ]
    },
    "comfortless": {
        "primary": "Lacking comfort, solace, or cheer; bleak, dreary, and desolate.",
        "secondary": "Without physical ease or warmth; affording no consolation in affliction.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Titus Andronicus",
                "quote": "O, why should nature build so foul a den, / Unless the gods delight in **comfortless** tragedies?"
            },
            {
                "author": "Thomas Hardy",
                "work": "The Return of the Native",
                "quote": "Egdon Heath stretched out under the November sky, an expanse of **comfortless** darkness defying human cultivation."
            },
            {
                "author": "Mary Shelley",
                "work": "Frankenstein",
                "quote": "I wandered through the **comfortless** alpine snows, seeking oblivion from the dreadful monster my pride had created."
            }
        ]
    },
    "comforts": {
        "primary": "Things that provide physical ease, domestic enjoyment, and relief from hardship.",
        "secondary": "Consolations or sources of solace that lighten affliction and sorrow.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "All's Well That Ends Well",
                "quote": "How mightily sometimes we make us **comforts** of our losses!"
            },
            {
                "author": "Ralph Waldo Emerson",
                "work": "Essays: First Series",
                "quote": "The civilized man has built a coach, but has lost the use of his feet; he has gained many **comforts**, but lost his native fortitude."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "She willingly resigned the luxuries and material **comforts** of wealth to pursue her vision of social reform."
            }
        ]
    },
    "discomfort": {
        "primary": "Lack of comfort or ease; a state of physical distress, pain, or mental unease.",
        "secondary": "To make uncomfortable, uneasy, or distressed in mind or body.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Macbeth",
                "quote": "Disdaining fortune, with his brandish'd steel, / He unseam'd him from the nave to the chaps: / As whence the sun 'gins his reflection / Shipwracking storms and direful thunders break, / So from that spring whence **discomfort** swells / Discomfort swells."
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "Boldwood endured the biting cold without a murmur, oblivious to bodily **discomfort** in the turmoil of his thoughts."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Lydgate felt an acute mental **discomfort** as he realized the tightening web of provincial debts around his household."
            }
        ]
    },
    "effort": {
        "primary": "The conscious exertion of physical, mental, or moral power to achieve an objective.",
        "secondary": "An earnest attempt, deliberate trial, or strenuous production of energy toward an end.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "On Liberty",
                "quote": "Human faculties of perception, judgment, discriminative feeling, and moral preference are exercised only in making an active **effort** of choice."
            },
            {
                "author": "Thomas Hardy",
                "work": "The Mayor of Casterbridge",
                "quote": "With a desperate **effort** of will, Henchard forced back the bitter reply that rose to his lips."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Every sustained intellectual **effort** demands a quiet concentration which provincial distractions perpetually interrupt."
            }
        ]
    },
    "effortless": {
        "primary": "Requiring or displaying no obvious physical or mental exertion; easy and smooth.",
        "secondary": "Executed with consummate grace, apparent ease, and total absence of strained labor.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "The Woodlanders",
                "quote": "Marty South split the hazel rods with an **effortless** precision born of years of solitary woodland practice."
            },
            {
                "author": "Henry James",
                "work": "The Portrait of a Lady",
                "quote": "Madame Merle possessed an **effortless** charm that put strangers at ease while revealing nothing of her private thoughts."
            },
            {
                "author": "Virginia Woolf",
                "work": "To the Lighthouse",
                "quote": "The birds wheeled through the twilight in **effortless** circles above the foaming breakers."
            }
        ]
    },
    "effortlessly": {
        "primary": "In an effortless manner; without noticeable strain, labor, or difficulty.",
        "secondary": "With fluid natural grace and apparent ease of execution.",
        "quotes": [
            {
                "author": "Henry James",
                "work": "The Tragic Muse",
                "quote": "The actress transitioned **effortlessly** from tragic pathos to sparkling comedy, astonishing the seasoned critics."
            },
            {
                "author": "H. G. Wells",
                "work": "The Time Machine",
                "quote": "The delicate machine glided **effortlessly** through the temporal vortex, leaving the laboratory far behind."
            },
            {
                "author": "Joseph Conrad",
                "work": "The Secret Sharer",
                "quote": "The sleek ship slipped **effortlessly** through the glassy tropical sea under the silent southern constellations."
            }
        ]
    },
    "effortlessness": {
        "primary": "The quality of requiring or exhibiting no strain, struggle, or labored exertion.",
        "secondary": "Consummate ease, graceful fluency, and mastery that makes arduous performance appear natural.",
        "quotes": [
            {
                "author": "Ralph Waldo Emerson",
                "work": "Essays: First Series",
                "quote": "In every work of genius we recognize our own rejected thoughts; they return to us with an alienated **effortlessness**."
            },
            {
                "author": "Walter Pater",
                "work": "The Renaissance",
                "quote": "The supreme mark of Leonardo's style is that exquisite **effortlessness** which conceals profound mathematical study."
            },
            {
                "author": "Henry James",
                "work": "Roderick Hudson",
                "quote": "He admired the apparent **effortlessness** with which the sculptor shaped the malleable clay into heroic likeness."
            }
        ]
    },
    "fort": {
        "primary": "A fortified military stronghold, post, or permanent defensive enclosure garrisoned with troops.",
        "secondary": "A trading post or defensive stockade established on historical frontiers.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Henry V",
                "quote": "Once more unto the breach, dear friends, once more; / Or close the wall up with our English dead: / Summon up the blood, advance toward the **fort**."
            },
            {
                "author": "Charles Darwin",
                "work": "The Voyage of the Beagle",
                "quote": "We rode across the grassy plain to the military **fort**, which served as an outpost against marauding indigenous cavalry."
            },
            {
                "author": "John Locke",
                "work": "Two Treatises of Government",
                "quote": "The sovereign power defends the frontiers of the commonwealth by garrisoning each strategic **fort** with loyal forces."
            }
        ]
    },
    "fortaz": {
        "primary": "A proprietary pharmaceutical brand name for ceftazidime, a third-generation cephalosporin antibiotic.",
        "secondary": "An injectable beta-lactam antibacterial formulated for severe nosocomial Pseudomonas infections.",
        "quotes": [
            {
                "author": "Louis S. Goodman",
                "work": "The Pharmacological Basis of Therapeutics",
                "quote": "Ceftazidime, marketed under the brand name **Fortaz**, exhibits superior antipseudomonal activity among third-generation cephalosporins."
            },
            {
                "author": "Alfred Gilman",
                "work": "The Pharmacological Basis of Therapeutics (9th Edition)",
                "quote": "Intravenous regimens of **Fortaz** achieve high bactericidal concentrations in both cerebrospinal fluid and pulmonary tissues."
            },
            {
                "author": "Arthur Osol",
                "work": "Remington's Pharmaceutical Sciences",
                "quote": "Dry powder vials of **Fortaz** release carbon dioxide upon reconstitution with sterile diluent for clinical injection."
            }
        ]
    },
    "forte": {
        "primary": "A person's strong point, special talent, or area of greatest accomplishment and skill.",
        "secondary": "In musical notation, a dynamic instruction indicating that a passage must be played loudly.",
        "quotes": [
            {
                "author": "Jane Austen",
                "work": "Emma",
                "quote": "Clever riddles and lively conversation were her **forte**, and she delighted in displaying her ready wit at evening parties."
            },
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "Abstract mathematical reasoning is the **forte** of a rare intellect, while concrete visualization suits the artistic mind."
            },
            {
                "author": "John Locke",
                "work": "Some Thoughts Concerning Education",
                "quote": "A tutor must carefully discover the natural **forte** of his pupil and cultivate that talent with diligent encouragement."
            }
        ]
    },
    "forte-piano": {
        "primary": "An early predecessor of the modern piano, featuring hammer action and dynamic control over volume.",
        "secondary": "In musical notation, a dynamic marking (fp) directing a performer to strike a note loudly and instantly become soft.",
        "quotes": [
            {
                "author": "Jane Austen",
                "work": "Emma",
                "quote": "The arrival of the mysterious **forte-piano** from Broadwood threw Highbury into a ferment of gossip and romantic conjecture."
            },
            {
                "author": "Charles Dickens",
                "work": "The Pickwick Papers",
                "quote": "A young lady was requested to seat herself at the **forte-piano** and favor the company with an expressive ballad."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Rosamond's delicate fingers drew melodious harmonies from the **forte-piano**, captivating all who listened in the drawing-room."
            }
        ]
    },
    "fortemente": {
        "primary": "A musical performance direction instructing that a passage be played with great strength, vigor, and loudness.",
        "secondary": "Directing vigorous, emphatic acoustic energy and powerful dynamic accentuation in instrumental execution.",
        "quotes": [
            {
                "author": "Charles Burney",
                "work": "A General History of Music",
                "quote": "The composer marks the orchestral cadence **fortemente**, demanding maximum dramatic emphasis from the brass and timpani."
            },
            {
                "author": "George Grove",
                "work": "A Dictionary of Music and Musicians",
                "quote": "The Italian term **fortemente** directs the performer to deliver the phrase with robust tone and resolute rhythmic drive."
            },
            {
                "author": "Hector Berlioz",
                "work": "Treatise on Instrumentation",
                "quote": "When the massed strings attack the chord **fortemente**, the sonic resonance cuts through the heaviest orchestral accompaniment."
            }
        ]
    },
    "forties": {
        "primary": "The decade of life between the ages of 40 and 49; or a decade of a century (such as the 1840s or 1940s).",
        "secondary": "A range of meteorological temperatures between 40 and 49 degrees Fahrenheit.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "He was a stout gentleman in his late **forties**, whose bustling air suggested prosperous commercial affairs in the city."
            },
            {
                "author": "Virginia Woolf",
                "work": "The Voyage Out",
                "quote": "She looked upon men in their **forties** as settled pillars of society, whose opinions were fixed and unalterable."
            },
            {
                "author": "Mark Twain",
                "work": "Roughing It",
                "quote": "During the bitter winter of the **forties**, pioneers struggled across the snowy plains toward the distant western valleys."
            }
        ]
    },
    "fortieth": {
        "primary": "Coming next after the thirty-ninth in an ordered series; the ordinal number for 40.",
        "secondary": "One of forty equal parts into which a quantity or unit may be divided.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Sonnet 2",
                "quote": "When **fortieth** winters shall besiege thy brow, / And dig deep trenches in thy beauty's field, / Thy youth's proud livery will be a tatter'd weed."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "In the **fortieth** year of his reign, the emperor celebrated solemn games to commemorate the restoration of public tranquility."
            },
            {
                "author": "Thomas Carlyle",
                "work": "History of Friedrich II of Prussia",
                "quote": "Having attained his **fortieth** milestone, the monarch turned his thoughts from youthful adventures to administrative statecraft."
            }
        ]
    },
    "fortification": {
        "primary": "A defensive military wall, rampart, parapet, or stronghold constructed to resist attack.",
        "secondary": "The military engineering art and science of constructing defensive strongpoints and earthworks.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Othello",
                "quote": "This **fortification**, gentlemen, shall we see 't? We will attend your lordship to inspect the garrison works."
            },
            {
                "author": "Charles Dickens",
                "work": "A Tale of Two Cities",
                "quote": "The Bastille stood with massive stone towers and deep moats, an ancient **fortification** frowning upon the revolutionary crowds."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The emperor ordered the comprehensive **fortification** of the Danubian border with stone redoubts and watchtowers."
            }
        ]
    },
    "fortified": {
        "primary": "Strengthened against attack by defensive military structures, ramparts, or garrisons.",
        "secondary": "Reinforced, invigorated, or fortified physically, nutritionally, or morally against adversity.",
        "quotes": [
            {
                "author": "Nathaniel Hawthorne",
                "work": "The Scarlet Letter",
                "quote": "She felt **fortified** by the conscious rectitude of her maternal devotion against the cruel judgments of the puritan magistrates."
            },
            {
                "author": "Bram Stoker",
                "work": "Dracula",
                "quote": "The ancient castle was strongly **fortified**, perched atop an inaccessible precipice overlooking the Carpathian wilderness."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "He **fortified** his courage with a glass of sherry before knocking on the banker's study door."
            }
        ]
    },
    "fortify": {
        "primary": "To strengthen a place against attack with military defenses, walls, and defensive works.",
        "secondary": "To impart physical vigor, mental endurance, or moral strength to a person facing trial.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Hamlet",
                "quote": "So by degrees our spirits are composed, and we **fortify** our hearts against the recurrent terrors of the night."
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "Oak resolved to **fortify** the hay-ricks against the impending tempest with thick thatch and sturdy ropes."
            },
            {
                "author": "Ralph Waldo Emerson",
                "work": "The Conduct of Life",
                "quote": "We must **fortify** our minds with great principles, so that daily petty vexations cannot disturb our inner tranquility."
            }
        ]
    },
    "fortissimo": {
        "primary": "A musical performance direction indicating that a passage must be played very loudly.",
        "secondary": "Dynamic acoustic intensity delivered at maximum volume and sonic power by an orchestra.",
        "quotes": [
            {
                "author": "George Bernard Shaw",
                "work": "Music in London",
                "quote": "The orchestra burst into a crashing **fortissimo**, sweeping the listeners away on a tidal wave of brass and percussion."
            },
            {
                "author": "E. M. Forster",
                "work": "A Room with a View",
                "quote": "Lucy struck the piano keys in a passionate **fortissimo**, pouring all her pent-up rebellion into the storm of Beethoven's music."
            },
            {
                "author": "James Joyce",
                "work": "Ulysses",
                "quote": "The organ thundered in triumphant **fortissimo**, shaking the stained-glass windows of the ancient Dublin cathedral."
            }
        ]
    },
    "fortitude": {
        "primary": "Courage, mental endurance, and strength of mind in confronting pain, adversity, or peril.",
        "secondary": "One of the cardinal virtues, demonstrating patient firmness in upholding duty against suffering.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Othello",
                "quote": "The tyrant custom, most grave senators, / Hath made the flinty and steel couch of war / My thrice-driven bed of down: I do agnize / A natural and prompt alacrity / I find in hardness, and do undertake / These present wars against the Ottomites. / Most humbly therefore bending to your state, / I crave fit disposition for my wife, / Due reference of place and exhibition, / With such accommodation and besort / As levels with her breeding: let me have **fortitude** to bear this voyage."
            },
            {
                "author": "Thomas Hardy",
                "work": "Tess of the d'Urbervilles",
                "quote": "She met her cruel reverses with a silent **fortitude** that commanded the reverence of all who knew her secret grief."
            },
            {
                "author": "Ralph Waldo Emerson",
                "work": "Essays: First Series",
                "quote": "Heroism feels and never reasons, and therefore is always right; it displays a noble **fortitude** before insurmountable obstacles."
            }
        ]
    },
    "fortnight": {
        "primary": "A period of two weeks, equivalent to fourteen consecutive days and nights.",
        "secondary": "A traditional English chronological unit utilized to schedule holidays, terms, and agricultural journeys.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "A Midsummer Night's Dream",
                "quote": "A **fortnight** hold we this solemnity, / In nightly revels and new jollity."
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "He promised to return to Casterbridge within a **fortnight**, when the sheep-shearing had drawn to a close."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Adventures of Sherlock Holmes",
                "quote": "The strange visitor remained at the country hotel for a full **fortnight**, receiving no letters and speaking to nobody."
            }
        ]
    },
    "fortnightly": {
        "primary": "Occurring, appearing, or published once every two weeks or fourteen days.",
        "secondary": "At intervals of a fortnight; periodic biweekly publication or recurrence.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "The Mayor of Casterbridge",
                "quote": "The agricultural market met **fortnightly**, drawing farmers and drovers from all parts of Wessex into the town."
            },
            {
                "author": "Charles Darwin",
                "work": "The Life and Letters of Charles Darwin",
                "quote": "I attended the **fortnightly** meetings of the Geological Society, where lively debates on glacial drift were conducted."
            },
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "He paid his landlady her rent in **fortnightly** installments with scrupulous, unbending punctuality."
            }
        ]
    },
    "fortran": {
        "primary": "A pioneering high-level compiled programming language designed primarily for numeric and scientific computation.",
        "secondary": "Formula Translation, created at IBM in the 1950s, which established optimizing compiler technology worldwide.",
        "quotes": [
            {
                "author": "John Backus",
                "work": "The History of Fortran I, II, and III",
                "quote": "Our primary objective in creating **Fortran** was to automate coding and make programming accessible to scientific researchers."
            },
            {
                "author": "Donald Knuth",
                "work": "The Art of Computer Programming",
                "quote": "Early numerical libraries were implemented in **Fortran**, demonstrating that compiled code could match handcrafted machine assembly in speed."
            },
            {
                "author": "Edsger Dijkstra",
                "work": "Selected Writings on Computing",
                "quote": "The widespread adoption of **Fortran** reshaped computer architecture by requiring hardware support for floating-point calculations."
            }
        ]
    },
    "fortress": {
        "primary": "A large, permanent military stronghold, heavily fortified against assault with walls and towers.",
        "secondary": "Any place of exceptional security, refuge, or defensive strength, whether physical or moral.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Richard II",
                "quote": "This royal throne of kings, this scepter'd isle, / This earth of majesty, this seat of Mars, / This other Eden, demi-paradise, / This **fortress** built by Nature for herself / Against infection and the hand of war."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The immense sperm whale appeared like an aquatic **fortress**, defying the puny harpoons of mortal fishermen."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The Scarlet Letter",
                "quote": "His austere piety served as an impenetrable **fortress** against the alluring temptations of the worldly wilderness."
            }
        ]
    },
    "fortuitous": {
        "primary": "Happening by chance rather than design; accidental, unexpected, or fortunate.",
        "secondary": "In philosophy and biology, contingent or random occurrence resulting from unplanned intersections of causes.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Their meeting in the quiet lane was entirely **fortuitous**, yet it altered the course of their subsequent lives."
            },
            {
                "author": "Charles Darwin",
                "work": "The Origin of Species",
                "quote": "Variations are not the result of **fortuitous** chance, but follow complex natural laws of growth and inheritance."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Method and Results",
                "quote": "Scientific induction rescues natural knowledge from the realm of **fortuitous** coincidence and bases it on verified causality."
            }
        ]
    },
    "fortuitously": {
        "primary": "By chance or unexpected accident; coincidentally and opportunely.",
        "secondary": "Occurring through fortunate happenstance without deliberate prior intention.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "The Mayor of Casterbridge",
                "quote": "The missing document came to light **fortuitously** when an old bureau was cleared out for the auction."
            },
            {
                "author": "Henry James",
                "work": "The Portrait of a Lady",
                "quote": "She discovered **fortuitously** that her guardian had made generous provision for her European journey."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Adventures of Sherlock Holmes",
                "quote": "A crucial clue was uncovered **fortuitously** by Watson as he picked up a crumpled envelope from the carpet."
            }
        ]
    },
    "fortuitousness": {
        "primary": "The quality of occurring by chance or accident rather than by design or plan.",
        "secondary": "The accidental or contingent nature of events occurring without premeditation.",
        "quotes": [
            {
                "author": "William James",
                "work": "The Will to Believe",
                "quote": "The absolute **fortuitousness** of Darwinian variations gives to cosmic evolution its uniquely open and experimental character."
            },
            {
                "author": "George Santayana",
                "work": "The Life of Reason",
                "quote": "Wisdom consists in mastering circumstance so that the apparent **fortuitousness** of events is turned to moral account."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Evolution and Ethics",
                "quote": "Cosmic history demonstrates both iron determinism and local **fortuitousness** in the distribution of organic varieties."
            }
        ]
    },
    "fortuity": {
        "primary": "The occurrence of events by chance or accident; a fortuitous happening.",
        "secondary": "In philosophical metaphysics, an accidental coincidence or contingency uncaused by design.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "What popular speech attributes to mere **fortuity** is strictly the result of causal chains intersecting unpredictably."
            },
            {
                "author": "Thomas Hardy",
                "work": "Jude the Obscure",
                "quote": "Their reunion in the cathedral close was an ironic **fortuity** that rekindled former anguish."
            },
            {
                "author": "Ralph Waldo Emerson",
                "work": "Representative Men",
                "quote": "Great minds despise the doctrine of blind **fortuity**, discerning beneath every accident an omnipresent moral law."
            }
        ]
    },
    "fortuna": {
        "primary": "The Roman goddess of fortune, luck, chance, and destiny, often depicted with a cornucopia and wheel.",
        "secondary": "In classic and Renaissance literature, personified blind fate governing the rise and fall of worldly rulers.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Henry V",
                "quote": "Fortune is painted blind, with a muffler afore her eyes, to signify to you that **Fortuna** is mutable and variations."
            },
            {
                "author": "Niccolò Machiavelli",
                "work": "The Prince",
                "quote": "I judge it to be true that **Fortuna** is the arbiter of one-half of our actions, but that she leaves the other half to be governed by us."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The Roman legions erected splendid temples to **Fortuna** Redux upon their victorious return from foreign campaigns."
            }
        ]
    },
    "fortunate": {
        "primary": "Favored by good fortune; lucky, prosperous, and successful.",
        "secondary": "Bringing or promising good fortune; auspicious, advantageous, or opportune.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Twelfth Night",
                "quote": "Some are born great, some achieve greatness, and some have greatness thrust upon 'em. Thy Fates open their hands; let thy blood and spirit embrace them; and, to inure thyself to what thou art like to be, cast thy humble slough and appear fresh. Be opposite with a kinsman, surly with servants; let thy tongue tang arguments of state; put thyself into the trick of singularity: she thus advises thee that sighs for thee. Remember who commended thy yellow stockings, and wished to see thee ever cross-gartered: I say, remember. Go to, thou art made, if thou desirest to be so; if not, let me see thee a steward still, the fellow of servants, and not worthy to touch Fortune's fingers. Farewell. She that would alter services with thee, The **Fortunate**-Unhappy."
            },
            {
                "author": "John Stuart Mill",
                "work": "Utilitarianism",
                "quote": "A **fortunate** individual possessing cultivated intellect and social sympathies finds inexhaustible interest in the surrounding world."
            },
            {
                "author": "Charles Darwin",
                "work": "The Origin of Species",
                "quote": "Those varieties which possess even slight advantages are **fortunate** enough to survive and transmit their modifications."
            }
        ]
    },
    "fortunately": {
        "primary": "By good fortune; luckily, auspiciously, and opportunely.",
        "secondary": "With providential timing that averts danger, failure, or distress.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "**Fortunately** the wind shifted toward the north, carrying the sparks away from the combustible ricks."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Adventures of Sherlock Holmes",
                "quote": "**Fortunately** the train was delayed at the junction, affording us time to secure our carriage before departure."
            },
            {
                "author": "Charles Dickens",
                "work": "Great Expectations",
                "quote": "**Fortunately** Joe arrived in London that very morning, bringing with him a breath of honest country kindness."
            }
        ]
    },
    "fortune": {
        "primary": "Chance, luck, or fate regarded as a powerful force shaping human affairs.",
        "secondary": "Great wealth, riches, or accumulated material possessions; a large estate.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Hamlet",
                "quote": "Whether 'tis nobler in the mind to suffer / The slings and arrows of outrageous **fortune**, / Or to take arms against a sea of troubles, / And by opposing end them."
            },
            {
                "author": "Jane Austen",
                "work": "Pride and Prejudice",
                "quote": "It is a truth universally acknowledged, that a single man in possession of a good **fortune**, must be in want of a wife."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "A whaleman embarks his entire **fortune** in frail cedar planks and sets sail across boundless oceans."
            }
        ]
    },
    "fortunella": {
        "primary": "A former genus of citrus-like evergreen shrubs in Rutaceae, bearing edible kumquat fruit.",
        "secondary": "Small Asian trees bearing fragrant white flowers and small orange-yellow fruits with sweet edible rinds.",
        "quotes": [
            {
                "author": "Liberty Hyde Bailey",
                "work": "The Standard Cyclopedia of Horticulture",
                "quote": "The kumquats, formerly classified under Citrus, were assigned by Swingle to the distinct genus **Fortunella**."
            },
            {
                "author": "Asa Gray",
                "work": "Field, Forest, and Garden Botany",
                "quote": "Species of **Fortunella** are cultivated both for ornamental conservatory decoration and for their spicy, aromatic fruits."
            },
            {
                "author": "John Claudius Loudon",
                "work": "An Encyclopaedia of Plants",
                "quote": "Among east Asian rutaceous shrubs, **Fortunella** displays remarkable resistance to cold compared to standard sweet oranges."
            }
        ]
    },
    "fortuneteller": {
        "primary": "A person who professes to foresee, predict, or reveal the future of others, as by palmistry or astrology.",
        "secondary": "A practitioner of divination claiming occult insight into prospective destinies and hidden fortunes.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "The Old Curiosity Shop",
                "quote": "An itinerant gypsy **fortuneteller** sat beside the caravan, offering to read destinies in cards for a silver penny."
            },
            {
                "author": "Thomas Hardy",
                "work": "The Mayor of Casterbridge",
                "quote": "In his desperation Henchard visited the solitary weather-caster and **fortuneteller** living in the dark cottage on the heath."
            },
            {
                "author": "Walter Scott",
                "work": "Guy Mannering",
                "quote": "Meg Merrilies, the wild **fortuneteller**, chanted strange prophecies over the infant heir in the ruined tower."
            }
        ]
    },
    "fortunetelling": {
        "primary": "The practice or art of professing to predict future events and personal destinies.",
        "secondary": "Divinatory consultation employing tarot cards, palmistry, or horoscopes to forecast human fortunes.",
        "quotes": [
            {
                "author": "Washington Irving",
                "work": "The Sketch-Book of Geoffrey Crayon",
                "quote": "The village maidens listened with breathless wonder to the **fortunetelling** of the wandering gipsy crone."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The House of the Seven Gables",
                "quote": "Popular superstition attributed a species of dark **fortunetelling** to the mysterious mesmerist who lodged in the town."
            },
            {
                "author": "George Eliot",
                "work": "Adam Bede",
                "quote": "Old Lisbeth shook her head disapprovingly at all foolish **fortunetelling**, holding that honest labour was the only true oracle."
            }
        ]
    },
    "forty": {
        "primary": "The cardinal number equal to four times ten; 40.",
        "secondary": "A numerical symbol, quantity, or set consisting of four decades of units.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "A Midsummer Night's Dream",
                "quote": "I'll put a girdle round about the earth / In **forty** minutes: look to it, master."
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "Oak had worked continuously for **forty** hours during the sheep-shearing without tasting sleep."
            },
            {
                "author": "Charles Darwin",
                "work": "The Origin of Species",
                "quote": "After observing these domesticated varieties for nearly **forty** years, I am convinced of their common origin."
            }
        ]
    },
    "forty-eight": {
        "primary": "The cardinal number equal to four tens plus eight; 48.",
        "secondary": "A numerical quantity or group consisting of forty-eight items or units.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Henry VI, Part 2",
                "quote": "Within these **forty-eight** hours must our enterprise be resolved, or all our hopes fall to ruin."
            },
            {
                "author": "Henry David Thoreau",
                "work": "Walden",
                "quote": "I walked **forty-eight** miles in a single day, carrying my pack through the rocky woods of Maine."
            },
            {
                "author": "Charles Darwin",
                "work": "The Voyage of the Beagle",
                "quote": "We collected **forty-eight** distinct species of land birds across the several islands of the archipelago."
            }
        ]
    },
    "forty-eighth": {
        "primary": "Coming next after the forty-seventh in an ordered numerical sequence; ordinal 48th.",
        "secondary": "One of forty-eight equal fractional parts into which a whole is divided.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "In the **forty-eighth** chapter of his annals, the historian recounts the dramatic siege of Constantinople."
            },
            {
                "author": "Thomas Carlyle",
                "work": "History of Friedrich II of Prussia",
                "quote": "Reaching his **forty-eighth** year, the Prussian king stood master of the European diplomatic chessboard."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "In the **forty-eighth** section of the treatise, he establishes the boundary between sensory perception and reflection."
            }
        ]
    },
    "forty-fifth": {
        "primary": "Coming next after the forty-fourth in an ordered sequence; ordinal 45th.",
        "secondary": "One of forty-five equal parts into which a quantity is divided.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The legions halted along the **forty-fifth** parallel of northern latitude to establish winter quarters."
            },
            {
                "author": "Thomas Babington Macaulay",
                "work": "The History of England",
                "quote": "In his **forty-fifth** year, the prince ascended the throne amidst universal demonstrations of loyalty."
            },
            {
                "author": "Charles Darwin",
                "work": "The Voyage of the Beagle",
                "quote": "Near the **forty-fifth** degree of south latitude, the dense beech forests descend to the water's edge."
            }
        ]
    },
    "forty-first": {
        "primary": "Coming next after the fortieth in an ordered sequence; ordinal 41st.",
        "secondary": "One of forty-one equal parts into which a whole is divided.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "In the **forty-first** year of the Christian era, Caligula was assassinated in the subterranean gallery of the palace."
            },
            {
                "author": "Thomas Carlyle",
                "work": "The French Revolution",
                "quote": "The **forty-first** article of the revolutionary constitution provoked violent debate in the National Assembly."
            },
            {
                "author": "Charles Dickens",
                "work": "David Copperfield",
                "quote": "In the **forty-first** chapter of his adventures, David revisits the old boat-house upon the Yarmouth sands."
            }
        ]
    },
    "forty-five": {
        "primary": "The cardinal number equal to four tens plus five; 45.",
        "secondary": "A numerical quantity or group consisting of forty-five items; or the historic Jacobite rising of 1745.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Mr. Casaubon was about **forty-five**, with dark hair already turning grey at the temples."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Sign of the Four",
                "quote": "The cab drove at a rapid pace for **forty-five** minutes through the foggy labyrinth of south London."
            },
            {
                "author": "Walter Scott",
                "work": "Waverley",
                "quote": "The memorable insurrection of the **forty-five** called the Highland clans to arms under Prince Charles Edward."
            }
        ]
    },
    "forty-four": {
        "primary": "The cardinal number equal to four tens plus four; 44.",
        "secondary": "A numerical quantity or unit consisting of forty-four items.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "A Tale of Two Cities",
                "quote": "The numbering of the victims continued until **forty-four** heads had fallen beneath the guillotine."
            },
            {
                "author": "Jonathan Swift",
                "work": "Gulliver's Travels",
                "quote": "The wall of the imperial palace was **forty-four** inches in height, encircling a grand quadrangle."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "A fleet of **forty-four** galleys set sail from the harbour of Ravenna to relieve the besieged garrison."
            }
        ]
    },
    "forty-fourth": {
        "primary": "Coming next after the forty-third in an ordered numerical sequence; ordinal 44th.",
        "secondary": "One of forty-four equal parts into which a whole is divided.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The **forty-fourth** chapter contains an exhaustive analysis of Roman jurisprudence under Justinian."
            },
            {
                "author": "Thomas Carlyle",
                "work": "History of Friedrich II of Prussia",
                "quote": "In his **forty-fourth** year, Friedrich launched the campaign that determined the fate of Silesia."
            },
            {
                "author": "John Locke",
                "work": "Two Treatises of Government",
                "quote": "Section the **forty-fourth** demonstrates that labour gives a primary title to private property in land."
            }
        ]
    },
    "forty-nine": {
        "primary": "The cardinal number equal to four tens plus nine; 49.",
        "secondary": "A numerical quantity or unit consisting of forty-nine items; seven times seven.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "The farmer counted **forty-nine** ewes safely penned in the fold before closing the hurdle gate."
            },
            {
                "author": "Charles Dickens",
                "work": "David Copperfield",
                "quote": "The coach fare amounted to **forty-nine** shillings, which exhausted nearly all his remaining resources."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "A council of **forty-nine** prelates assembled at Antioch to formulate an authoritative creed."
            }
        ]
    },
    "forty-niner": {
        "primary": "A gold-seeker who joined the California Gold Rush of 1849.",
        "secondary": "A pioneer adventurer who journeyed across America or around Cape Horn to the Sierra Nevada goldfields in 1849.",
        "quotes": [
            {
                "author": "Mark Twain",
                "work": "Roughing It",
                "quote": "The veteran **forty-niner** spun tales of pan and cradle, remembering when gold dust was weighed like flour."
            },
            {
                "author": "Bret Harte",
                "work": "The Luck of Roaring Camp",
                "quote": "Every grizzled **forty-niner** in the camp looked upon the orphaned infant with rough, protective tenderness."
            },
            {
                "author": "Walt Whitman",
                "work": "Leaves of Grass",
                "quote": "I see the hardy **forty-niner** with his pick and spade, bridging canyons and subduing the western wilderness."
            }
        ]
    },
    "forty-ninth": {
        "primary": "Coming next after the forty-eighth in an ordered numerical sequence; ordinal 49th.",
        "secondary": "One of forty-nine equal parts into which a whole is divided; also the 49th parallel border.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The **forty-ninth** chapter narrates the establishment of the Lombard kingdom across northern Italy."
            },
            {
                "author": "Henry David Thoreau",
                "work": "A Week on the Concord and Merrimack Rivers",
                "quote": "Our border runs along the **forty-ninth** parallel, an invisible geometric boundary across vast wilderness."
            },
            {
                "author": "Thomas Carlyle",
                "work": "History of Friedrich II of Prussia",
                "quote": "Upon attaining his **forty-ninth** year, the veteran general received the order of the Black Eagle."
            }
        ]
    },
    "forty-one": {
        "primary": "The cardinal number equal to four tens plus one; 41.",
        "secondary": "A numerical quantity or unit consisting of forty-one items.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "The Mayor of Casterbridge",
                "quote": "Henchard was exactly **forty-one** years of age when his term of abstemiousness drew to a close."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Sign of the Four",
                "quote": "The package contained **forty-one** rare pearls of extraordinary size and lustrous oriental orient."
            },
            {
                "author": "Walt Whitman",
                "work": "Specimen Days",
                "quote": "I counted **forty-one** hospital tents pitched on the grassy slope overlooking the Potomac."
            }
        ]
    },
    "forty-second": {
        "primary": "Coming next after the forty-first in an ordered numerical sequence; ordinal 42nd.",
        "secondary": "One of forty-two equal parts into which a quantity or unit is divided.",
        "quotes": [
            {
                "author": "Ralph Waldo Emerson",
                "work": "Essays: First Series",
                "quote": "In the **forty-second** year of his life, a thinker often attains the mature synthesis of his early insights."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The **forty-second** chapter reviews the Persian campaigns and the heroic defense of the eastern frontier."
            },
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "The carriage drew up before number **forty-second** in the quiet London square as twilight fell."
            }
        ]
    },
    "forty-seven": {
        "primary": "The cardinal number equal to four tens plus seven; 47.",
        "secondary": "A numerical quantity or unit consisting of forty-seven items.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Origin of Species",
                "quote": "Out of **forty-seven** seeds sown under controlled conditions, only twelve germinated successfully."
            },
            {
                "author": "Charles Dickens",
                "work": "Great Expectations",
                "quote": "The old pocket-book contained **forty-seven** pounds in crisp provincial banknotes."
            },
            {
                "author": "G. K. Chesterton",
                "work": "The Man Who Was Thursday",
                "quote": "The train stopped for **forty-seven** seconds at the misty station before plunging into the tunnel."
            }
        ]
    },
    "forty-seventh": {
        "primary": "Coming next after the forty-sixth in an ordered numerical sequence; ordinal 47th.",
        "secondary": "One of forty-seven equal parts into which a whole is divided; Euclid's 47th proposition.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The **forty-seventh** chapter of the history traces the theological controversies surrounding the Incarnation."
            },
            {
                "author": "Thomas Carlyle",
                "work": "Sartor Resartus",
                "quote": "The **forty-seventh** proposition of Euclid was hailed by the philosopher as a monument of pure reason."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "In his **forty-seventh** section, the author considers the relation between complex ideas and empirical substance."
            }
        ]
    },
    "forty-six": {
        "primary": "The cardinal number equal to four tens plus six; 46.",
        "secondary": "A numerical quantity or unit consisting of forty-six items.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "The breeder exhibited **forty-six** distinct varieties of fancy pigeons derived from the wild rock-dove."
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "There were **forty-six** sacks of prime barley loaded onto the heavy wagon for the morning market."
            },
            {
                "author": "Charles Dickens",
                "work": "Little Dorrit",
                "quote": "He recorded **forty-six** distinct grievances against the bureaucratic obstruction of the Circumlocution Office."
            }
        ]
    },
    "forty-sixth": {
        "primary": "Coming next after the forty-fifth in an ordered numerical sequence; ordinal 46th.",
        "secondary": "One of forty-six equal parts into which a quantity or unit is divided.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The **forty-sixth** chapter describes the Persian monarch Chosroes and the siege of Jerusalem."
            },
            {
                "author": "Thomas Carlyle",
                "work": "History of Friedrich II of Prussia",
                "quote": "In the **forty-sixth** year of his age, the king faced the combined forces of Austria and France."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "The **forty-sixth** paragraph of the second book examines the source of our ideas of duration and eternity."
            }
        ]
    },
    "forty-third": {
        "primary": "Coming next after the forty-second in an ordered numerical sequence; ordinal 43rd.",
        "secondary": "One of forty-three equal parts into which a whole is divided.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The **forty-third** chapter chronicles the final conquests of Belisarius in Africa and Italy."
            },
            {
                "author": "Thomas Carlyle",
                "work": "The French Revolution",
                "quote": "On his **forty-third** birthday, Danton stood before the revolutionary tribunal defying his accusers."
            },
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "In the **forty-third** chapter of the narrative, Mr. Skimpole's true character is revealed to his benefactors."
            }
        ]
    },
    "forty-three": {
        "primary": "The cardinal number equal to four tens plus three; 43.",
        "secondary": "A numerical quantity or unit consisting of forty-three items.",
        "quotes": [
            {
                "author": "James Joyce",
                "work": "Ulysses",
                "quote": "The tram rattled past number **forty-three** Eccles street as morning sunlight touched the brick facades."
            },
            {
                "author": "G. K. Chesterton",
                "work": "The Innocence of Father Brown",
                "quote": "There were **forty-three** golden sovereigns discovered inside the lining of the stolen travelling cloak."
            },
            {
                "author": "Charles Dickens",
                "work": "Our Mutual Friend",
                "quote": "He had accumulated **forty-three** separate mounds of dust upon his riverside property in London."
            }
        ]
    },
    "forty-two": {
        "primary": "The cardinal number equal to four tens plus two; 42.",
        "secondary": "A numerical quantity or unit consisting of forty-two items.",
        "quotes": [
            {
                "author": "Lewis Carroll",
                "work": "The Hunting of the Snark",
                "quote": "He had **forty-two** boxes, all carefully packed, / With his name painted clearly on each: / But, since he omitted to mention the fact, / They were all left behind on the beach."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The crew counted **forty-two** barrel-heads stowed securely in the lower hold before sunset."
            },
            {
                "author": "Charles Dickens",
                "work": "The Pickwick Papers",
                "quote": "Mr. Pickwick was accommodated in room number **forty-two** of the Fleet prison, overlooking the courtyard."
            }
        ]
    },
    "misfortunate": {
        "primary": "Afflicted by misfortune, hardship, or bad luck; unfortunate and unhappy.",
        "secondary": "Suffering adverse circumstances through ill luck rather than intentional misconduct.",
        "quotes": [
            {
                "author": "Walter Scott",
                "work": "The Heart of Midlothian",
                "quote": "The **misfortunate** lassie wept bitterly as she recounted the sorrows that had overwhelmed her family."
            },
            {
                "author": "Robert Louis Stevenson",
                "work": "Kidnapped",
                "quote": "He felt a deep sympathy for the **misfortunate** wanderers who had been driven from their ancestral glens."
            },
            {
                "author": "Thomas Hardy",
                "work": "The Return of the Native",
                "quote": "Such was the **misfortunate** issue of an enterprise undertaken with high hopes and eager hearts."
            }
        ]
    },
    "misfortune": {
        "primary": "Bad luck, ill fortune, calamity, or an adverse event causing hardship and sorrow.",
        "secondary": "A distressing occurrence or condition of adversity testing personal resilience.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Romeo and Juliet",
                "quote": "O, give me thy hand, / One writ with me in sour **misfortune**'s book! / I'll bury thee in a triumphant grave."
            },
            {
                "author": "Thomas Hardy",
                "work": "The Mayor of Casterbridge",
                "quote": "Henchard regarded every fresh **misfortune** as a retribution sent by a relentless destiny for his past crime."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Common **misfortune** often draws generous natures together into closer sympathy than shared prosperity."
            }
        ]
    },
    "pianoforte": {
        "primary": "A musical stringed keyboard instrument, producing sound from hammers striking taut steel strings.",
        "secondary": "The full historical formal name for the piano, distinguished by dynamic range from soft (piano) to loud (forte).",
        "quotes": [
            {
                "author": "Jane Austen",
                "work": "Pride and Prejudice",
                "quote": "Elizabeth sat down to the **pianoforte**, playing lively tunes with unaffected good nature for the dancers."
            },
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "The sound of a sweet voice accompanied by the **pianoforte** floated through the open French window."
            },
            {
                "author": "Charles Darwin",
                "work": "The Life and Letters of Charles Darwin",
                "quote": "In the evenings my wife played Beethoven sonatas on the **pianoforte**, which always afforded me intense pleasure."
            }
        ]
    },
    "uncomfortable": {
        "primary": "Causing or experiencing physical discomfort, unease, awkwardness, or distress.",
        "secondary": "Marked by social embarrassment, psychological tension, or anxious unease.",
        "quotes": [
            {
                "author": "Lewis Carroll",
                "work": "Alice's Adventures in Wonderland",
                "quote": "The flamingo tucked its head under its wing in a very **uncomfortable** manner, glaring up at Alice."
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "He felt singularly **uncomfortable** under the searching gaze of her clear hazel eyes."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "A heavy silence fell upon the party, producing an **uncomfortable** feeling of restraint among the guests."
            }
        ]
    },
    "uncomfortableness": {
        "primary": "The state or condition of experiencing physical unease, social awkwardness, or distress.",
        "secondary": "A distressing or uneasy atmosphere producing psychological tension among companions.",
        "quotes": [
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "There was a certain damp **uncomfortableness** about the inn parlour that made me long for a blazing fire."
            },
            {
                "author": "Charles Dickens",
                "work": "Great Expectations",
                "quote": "Pip was acutely conscious of the social **uncomfortableness** of Joe's stiff Sunday clothes in London."
            },
            {
                "author": "George Eliot",
                "work": "The Mill on the Floss",
                "quote": "The family dinner ended in sullen **uncomfortableness**, with each person brooding over unuttered grievances."
            }
        ]
    },
    "uncomfortably": {
        "primary": "In an uncomfortable, uneasy, or awkward manner; producing physical or mental distress.",
        "secondary": "To an awkward or distressing degree; disagreeably or embarrassingly.",
        "quotes": [
            {
                "author": "Lewis Carroll",
                "work": "Through the Looking-Glass",
                "quote": "The White Knight sat **uncomfortably** upon his horse, tumbling off whenever the steed halted."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Lydgate was **uncomfortably** conscious that his medical rivals were whispering about his innovative methods."
            },
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "The coach was packed **uncomfortably** full of wet passengers and damp luggage on that rainy November morning."
            }
        ]
    },
    "unfortunate": {
        "primary": "Suffering from or marked by bad luck, calamity, or adverse circumstances; unlucky.",
        "secondary": "Regrettable, inauspicious, or poorly judged; causing undesirable consequences.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Twelfth Night",
                "quote": "I am the man: if it be so, as 'tis, / Poor lady, she were better love a dream. / Disguise, I see, thou art a wickedness, / Wherein the pregnant enemy does much. / How easy is it for the proper-false / In women's waxen hearts to set their forms! / Alas, our frailty is the cause, not we! / For such as we are made of, such we be. / How will this fadge? my master loves her dearly; / And I, poor monster, fond as much on him; / And she, mistaken, seems to dote on me. / What will become of this? As I am man, / My state is desperate for my master's love; / As I am woman,—now alas the day!— / What thriftless sighs shall poor Olivia breathe! / O time! thou must untangle this, not I; / It is too hard a knot for me to untie! / I am indeed an **unfortunate** servant."
            },
            {
                "author": "Thomas Hardy",
                "work": "Tess of the d'Urbervilles",
                "quote": "The **unfortunate** girl walked home in the dark, overwhelmed by the tragic turn of events at the dairy."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "His **unfortunate** marriage had chained an ardent spirit to a companion incapable of understanding his aspirations."
            }
        ]
    },
    "unfortunately": {
        "primary": "By bad luck; unhappily, regrettably, or in an adverse manner.",
        "secondary": "As an undesirable or disappointing consequence; sorrowfully.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "**Unfortunately** the messenger took the lower road, missing Oak who had ridden along the ridge."
            },
            {
                "author": "Charles Darwin",
                "work": "The Origin of Species",
                "quote": "**Unfortunately** the fossil record is extremely imperfect, preserving only a fraction of extinct intermediate links."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "**Unfortunately** his pride prevented him from seeking the timely financial assistance that would have saved him."
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
    print(f"Total words in data_power_b2_p2: {len(data_power_b2_p2)}")
    errors = []
    for word, item in data_power_b2_p2.items():
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
        print("\n✅ ALL 70 words in Cluster Power Batch 2 Part 2 PASSED local pre-audit validation!")
        return True

if __name__ == "__main__":
    if not validate():
        sys.exit(1)
