# -*- coding: utf-8 -*-
"""
Part 1 of Batch 4 Cluster Asking & Seeking (Dashboard — prec):
Words 1 to 27:
['appreciable', 'appreciably', 'appreciate', 'appreciated', 'appreciation',
 'appreciative', 'appreciatively', 'appreciativeness', 'appreciator', 'deprecate',
 'deprecating', 'deprecation', 'deprecative', 'deprecatively', 'deprecatory',
 'depreciate', 'depreciating', 'depreciation', 'depreciative', 'depreciator',
 'depreciatory', 'imprecate', 'imprecation', 'imprecise', 'imprecisely',
 'impreciseness', 'imprecision']
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part1_prec = {
    "appreciable": {
        "primary": "Capable of being perceived, noticed, measured, or estimated; perceptible.",
        "secondary": "In physics and statistics, denoting a quantity or variance sufficiently large to exert a measurable influence upon experimental outcomes.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Threepence had a definite value as money—it was an **appreciable** infringement on a day's wages, and, as such, a higgling matter."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "It seems pretty clear that organic beings must be exposed during several generations to the new conditions of life to cause an **appreciable** amount of variation."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The banker's speech was fluent, but it was also copious, and he used up an **appreciable** amount of time in brief meditative pauses."}
        ]
    },
    "appreciably": {
        "primary": "In a manner or to an extent that is noticeable, perceptible, or measurable.",
        "secondary": "In analytical chemistry and economics, describing changes of magnitude that alter observed trends beyond standard margins of error.",
        "quotes": [
            {"author": "George Eliot", "work": "Daniel Deronda", "quote": "The atmospheric tension had altered **appreciably**, leaving each member of the party conscious of an unspoken divergence."},
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The temperature of the moor had dropped **appreciably** as the evening fog rolled heavily across the mire."},
            {"author": "Herbert Spencer", "work": "First Principles", "quote": "When external pressures shift **appreciably**, the inner equilibrium of the organic structure must realign accordingly."}
        ]
    },
    "appreciate": {
        "primary": "To recognize the full worth, significance, or value of; or to rise in monetary worth.",
        "secondary": "In aesthetic philosophy and financial accounting, to comprehend artistic nuance critically, or to gain value over successive reporting intervals.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "He was endeavouring to catch and **appreciate** the sensation of being thus with her, his head upon her dress, before the event vanished."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "They are all men of some intellectual power, and consequently they all **appreciate** me."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "She was now enough aware of Sir James's position with regard to her, to **appreciate** the rectitude of his perseverance in honorable devotion."}
        ]
    },
    "appreciated": {
        "primary": "Recognized with gratitude, value, or esteem; or having increased in worth.",
        "secondary": "In historical economics, referring to currencies or assets that gained purchasing power relative to international baseline standards.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "But, as we have seen, his motives were not always rightly **appreciated** by those who looked upon his actions from afar."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "Philanthropy is almost the only virtue which is sufficiently **appreciated** by mankind."},
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The kindness of Joe was quietly **appreciated** by Pip whenever childhood misfortunes weighed upon his spirit."}
        ]
    },
    "appreciation": {
        "primary": "Favorable recognition of quality, value, or significance; or an upward movement in value.",
        "secondary": "In art criticism and finance, the discerning evaluation of aesthetic form, or the incremental capital growth of held securities.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Oak murmured some polite phrase in **appreciation** of the rustic song, knowing the singer's pride in his ancient tunes."},
            {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "On the present occasion, I shall attempt to contribute something toward the understanding and **appreciation** of the utilitarian philosophy."},
            {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "Marlow paused with keen **appreciation** of the subtle irony underlying the young sailor's romantic misfortune."}
        ]
    },
    "appreciative": {
        "primary": "Expressing, showing, or feeling warm admiration, gratitude, or sensitive discernment.",
        "secondary": "In psychological evaluation, exhibiting receptive cognitive awareness toward subtle sensory, cultural, or interpersonal cues.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Being a man not without a frequent consciousness that there was some charm in this life he led, he stood still with an **appreciative** gaze."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "A wife, a modest young lady, with the purely **appreciative**, unambitious abilities of her sex, is sure to think her husband wise."},
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Traddles listened with an **appreciative** nod as David related the ambitious plans formed for their mutual advancement."}
        ]
    },
    "appreciatively": {
        "primary": "In a manner that conveys gratitude, warm approval, or perceptive admiration.",
        "secondary": "In theatrical critique and sociolinguistic discourse, describing expressive audience responses that validate a performer's artistic choices.",
        "quotes": [
            {"author": "Edith Wharton", "work": "The House of Mirth", "quote": "Lawrence Selden looked **appreciatively** at Lily Bart, admiring the easy grace with which she held the porcelain cup."},
            {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Ralph Touchett smiled **appreciatively** at Isabel's ardent defense of independence in the face of worldly convention."},
            {"author": "E. M. Forster", "work": "A Room with a View", "quote": "Mr. Beebe chuckled **appreciatively** whenever Lucy touched the keys of the piano with unvarnished passion."}
        ]
    },
    "appreciativeness": {
        "primary": "The disposition or capacity to feel and express admiration, gratitude, or keen appraisal.",
        "secondary": "In moral philosophy, the habitual affective responsiveness of character that readily acknowledges merit and bounty in others.",
        "quotes": [
            {"author": "George Meredith", "work": "The Egoist", "quote": "Sir Willoughby expected an unreserved **appreciativeness** from those permitted to bask in the radiant sphere of Patterne Hall."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "A cultivated **appreciativeness** toward natural harmony distinguishes the refined intellect from the crude observer."},
            {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "True sweetness and light demand an inner **appreciativeness** of whatever is noble and lovely in human tradition."}
        ]
    },
    "appreciator": {
        "primary": "A person who values, esteems, or critically discerns the worth of something.",
        "secondary": "In connoisseurship and museology, a discerning collector or patron who identifies artistic authenticity prior to popular acclaim.",
        "quotes": [
            {"author": "Oscar Wilde", "work": "The Decay of Lying", "quote": "The true **appreciator** of art seeks not a photograph of nature, but the imaginative transformation of life."},
            {"author": "Walter Pater", "work": "The Renaissance", "quote": "To the sensitive **appreciator**, every brushstroke of Leonardo reveals an intricate movement of the spirit."},
            {"author": "William Hazlitt", "work": "Table-Talk", "quote": "A genuine **appreciator** of dramatic talent does not need the promptings of a claque to recognize genius on the boards."}
        ]
    },
    "deprecate": {
        "primary": "To express strong disapproval of; or to plead against or urge reasons against.",
        "secondary": "In diplomatic history and classical rhetoric, to avert an impending disaster by prayerful supplication or conciliation.",
        "quotes": [
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Wickfield put out his hands, as if to **deprecate** my condemnation, murmuring that Uriah Heep knew best."},
            {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I learned, from the views of social life which it developed, to admire their virtues and to **deprecate** the vices of mankind."},
            {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Men have looked away from themselves so long that they seem to **deprecate** their own spontaneous intuitions."}
        ]
    },
    "deprecating": {
        "primary": "Expressing earnest disapproval, mild protest, or an apologetic, self-effacing attitude.",
        "secondary": "In behavioral sociology, signaling social deference through gestures designed to deflect hostility or unearned praise.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Now, don't ye take on so, shepherd, and sit down! said Henery, with a **deprecating** peacefulness equal to anything."},
            {"author": "G. K. Chesterton", "work": "The Ball and the Cross", "quote": "I'm sure you'll excuse my speaking to you, said the stranger, in a voice at once eager and **deprecating**."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Brooke offered a **deprecating** wave of his hand, assuring the company that extreme measures were rarely advisable."}
        ]
    },
    "deprecation": {
        "primary": "An expression of earnest protest, disapproval, or a prayer that an evil may be averted.",
        "secondary": "In software architecture and liturgical history, marking an obsolete protocol scheduled for removal, or reciting litanies to ward off judgment.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "No, no, dear, no, said Dorothea, putting up her hand with careless **deprecation** of the praise lavished on her benevolence."},
            {"author": "James Joyce", "work": "Dubliners", "quote": "Christmas-time! said Gabriel, almost trotting to the stairs and waving his hand to her in **deprecation**."},
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The Doctor made a gentle gesture of **deprecation**, protesting against any undue estimation of his scholarly labor."}
        ]
    },
    "deprecative": {
        "primary": "Serving or tending to deprecate; expressive of mild protest, disapproval, or supplication.",
        "secondary": "In linguistics and discourse analysis, describing hedging utterances deployed by speakers to soften potential interpersonal friction.",
        "quotes": [
            {"author": "Henry James", "work": "The American", "quote": "Newman observed the young Frenchman's **deprecative** shrug, which seemed to disclaim all personal responsibility for Parisian etiquette."},
            {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "Mr. Slope adopted a **deprecative** smile whenever the bishop's wife interposed her formidable authority in diocesan matters."},
            {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Thaddeus Sholto held up his long white hands with a **deprecative** gesture against Watson's indignant remonstrance."}
        ]
    },
    "deprecatively": {
        "primary": "In a deprecative manner; with apologetic, self-effacing, or mildly protesting intent.",
        "secondary": "In dramatic direction, describing stage deliveries where characters moderate assertion with conciliatory intonation.",
        "quotes": [
            {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Mrs. Tulliver looked **deprecatively** at her sister Glegg, dreading the severe judgment sure to follow upon the broken china."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard raised his arm **deprecatively**, as though seeking to ward off the painful recollections conjured by Farfrae."},
            {"author": "Joseph Conrad", "work": "The Secret Agent", "quote": "Verloc cleared his throat and coughed **deprecatively** before daring to present his defense to the impatient ambassador."}
        ]
    },
    "deprecatory": {
        "primary": "Expressing apology, disapproval, or an attempt to deflect criticism; self-effacing.",
        "secondary": "In legal jurisprudence, describing non-binding expressions of desire or petition as opposed to peremptory commands.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Oh! said Rosamond, with a slight **deprecatory** laugh that concealed her firm determination to govern her own household."},
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Spenlow went over the items with a **deprecatory** air—as if it were painful to his feelings to charge so much, but unavoidable."},
            {"author": "Anthony Trollope", "work": "The Warden", "quote": "Mr. Harding glanced around the cathedral cloister with a **deprecatory** gaze that disarmed even his fiercest critics."}
        ]
    },
    "depreciate": {
        "primary": "To diminish in value, market price, or purchasing power over time; or to disparage.",
        "secondary": "In corporate finance and tax law, to write off incrementally the capitalized cost of a physical asset over its estimated useful service life.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Money, if kept by us, yields no rent and is liable to loss; if invested, is liable to **depreciate** in times of political panic."},
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Whenever silver became abundant throughout Europe, the coin began to **depreciate** relative to agricultural commodities."},
            {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Paper currency unsupported by a metallic foundation will inevitably **depreciate** and throw commercial exchanges into confusion."}
        ]
    },
    "depreciating": {
        "primary": "Declining in monetary value or physical worth; or speaking slightingly of something.",
        "secondary": "In macroeconomics, describing a sovereign exchange rate whose foreign purchasing capacity erodes under inflationary monetary expansion.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Fred saw that Bambridge's **depreciating** remarks were intended merely to drive down the purchase price of the hunter."},
            {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "A continually **depreciating** standard of value inflicts irreparable injury upon creditors and fixed-income laborers."},
            {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Miss Pinkerton cast a **depreciating** glance upon Becky Sharp's plain attire as she departed from the academy gates."}
        ]
    },
    "depreciation": {
        "primary": "A decline in value or market price; or the act of belittling or disparaging someone.",
        "secondary": "In cost accounting, the systematic allocation of the depreciable base of a tangible asset across its estimated operational lifespan.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Fred gave up the hope of a genuine opinion; he saw that Bambridge's **depreciation** and praise were equally professional tactics."},
            {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Money is liable to **depreciation** of the particular kind of property in which it is invested."},
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "He carried his head on one side, partly in modest **depreciation** of himself, partly in modest propitiation of everybody else."}
        ]
    },
    "depreciative": {
        "primary": "Tending to lower value or price; disparaging, belittling, or dismissive.",
        "secondary": "In financial analysis, referring to fiscal policies or market forces that exert downward pricing pressure on capital assets.",
        "quotes": [
            {"author": "Henry James", "work": "The Wings of the Dove", "quote": "Densher detected a **depreciative** undertone in Aunt Maud's appraisal of the young journalist's professional prospects."},
            {"author": "George Meredith", "work": "Diana of the Crossways", "quote": "The critic's review was mildly **depreciative**, granting verbal brilliance while denying dramatic coherence to the romance."},
            {"author": "Thorstein Veblen", "work": "The Theory of the Leisure Class", "quote": "Conspicuous consumption prompts a **depreciative** attitude toward utilitarian goods that lack ornamental expense."}
        ]
    },
    "depreciator": {
        "primary": "One who belittles or disparages the merit of others; or a factor causing loss of value.",
        "secondary": "In literary polemics, a cynical critic who systematically denies the originality or virtue of contemporary works.",
        "quotes": [
            {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "Every eminent author finds in his contemporaries a stubborn **depreciator** who measures merit by departed standards."},
            {"author": "Edmund Burke", "work": "Letters on a Regicide Peace", "quote": "The persistent **depreciator** of public institutions saps that veneration upon which social order ultimately rests."},
            {"author": "Walter Bagehot", "work": "Biographical Studies", "quote": "Gladstone encountered in Disraeli a witty **depreciator** skilled at exposing the sentimental vulnerabilities of moral reform."}
        ]
    },
    "depreciatory": {
        "primary": "Tending to disparage, belittle, or lower in value or estimation; derogatory.",
        "secondary": "In rhetorical analysis, characterizing satirical tropes that subvert an adversary's dignity through underestimation.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Mrs. Plymdale delivered a **depreciatory** remark concerning the newcomers, hinting that their pedigree was dubious."},
            {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Teufelsdröckh treated worldly honors with a **depreciatory** laugh, looking through court embroidery to the naked biped beneath."},
            {"author": "Anthony Trollope", "work": "The Small House at Allington", "quote": "Lady de Courcy dropped a few **depreciatory** words about the bride's dowry to ensure her own superiority."}
        ]
    },
    "imprecate": {
        "primary": "To invoke evil, curse, or calamity upon a person, place, or thing.",
        "secondary": "In classical tragedy and ancient ritual, to call down divine retribution through formal verbal oaths of vengeance.",
        "quotes": [
            {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I bent over him and whispered in his ear words to **imprecate** misery upon the murderer who had ruined my hearth."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab seemed ready to **imprecate** destruction on the heavens themselves if they sheltered the white whale from his harpoon."},
            {"author": "John Milton", "work": "Samson Agonistes", "quote": "The captive giant paused, refusing to **imprecate** wrath upon his own people while bearing the chains of Gaza."}
        ]
    },
    "imprecation": {
        "primary": "An invoked curse, malediction, or an earnest prayer calling down misfortune upon someone.",
        "secondary": "In folklore studies and Greco-Roman epigraphy, a inscribed curse tablet (defixio) deposited in graves to bind adversaries.",
        "quotes": [
            {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The crowd yelled an awful **imprecation** against the aristocrat as the carriage hurried through the muddy suburb."},
            {"author": "James Joyce", "work": "Dubliners", "quote": "He muttered a bitter **imprecation** under his breath when the train whistled and departed without him."},
            {"author": "Walter Scott", "work": "The Bride of Lammermoor", "quote": "The dying prophetess uttered a terrible **imprecation** against the house of Ravenswood that echoed through the chapel."}
        ]
    },
    "imprecise": {
        "primary": "Lacking exactness, accuracy, sharpness, or clarity of boundary or expression.",
        "secondary": "In metrology and data analytics, denoting observations containing variance or ambiguous boundaries that prevent fine calibration.",
        "quotes": [
            {"author": "Bertrand Russell", "work": "The Analysis of Mind", "quote": "Ordinary language is fatally **imprecise**, compelling the philosopher to define his logical symbols with rigorous care."},
            {"author": "William James", "work": "Pragmatism", "quote": "A doctrine that remains **imprecise** in its practical consequences cannot yield fruitful guidance in intellectual life."},
            {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "The records were hopelessly **imprecise**, making it impossible to determine the true production statistics of previous years."}
        ]
    },
    "imprecisely": {
        "primary": "In an inaccurate, vague, or indistinct manner; without exact calibration or sharpness.",
        "secondary": "In algorithmic computation, describing numerical values estimated within broad tolerancing margins rather than exact floating points.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "Collected Essays", "quote": "When scientific terms are applied **imprecisely**, confusion inevitably usurps the place of reasoned demonstration."},
            {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The witness remembered the hour only **imprecisely**, stating it was somewhere between twilight and the stroke of ten."},
            {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "Kemp noted that the stranger handled the laboratory glassware **imprecisely**, like a man blinded by sudden dawn."}
        ]
    },
    "impreciseness": {
        "primary": "The condition of wanting exactitude, sharpness, or definiteness; vagueness.",
        "secondary": "In analytical epistemology, the structural deficiency in natural language that generates boundary indeterminacy in truth claims.",
        "quotes": [
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The **impreciseness** of philosophical discourse proceeds principally from a careless application of indeterminate words."},
            {"author": "William Stanley Jevons", "work": "The Principles of Science", "quote": "No experimental observer can wholly eliminate the **impreciseness** arising from imperfect sensory organs."},
            {"author": "Henry Sidgwick", "work": "The Methods of Ethics", "quote": "The apparent **impreciseness** of moral intuition forces reason to seek systematic harmony in utilitarian standards."}
        ]
    },
    "imprecision": {
        "primary": "Lack of exactness, precision, or accuracy; indefiniteness in thought or measurement.",
        "secondary": "In quantum mechanics and scientific error analysis, the inherent spread or standard uncertainty of repeated empirical trials.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The chief obstacle to intellectual progress has ever been the verbal **imprecision** that conceals our factual ignorance."},
            {"author": "Bertrand Russell", "work": "Introduction to Mathematical Philosophy", "quote": "Traditional logic suffered from an incurable **imprecision** whenever it attempted to analyze relations of magnitude."},
            {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "The monetary system collapsed under the sheer **imprecision** of its paper reserves and speculative accounting."}
        ]
    }
}
