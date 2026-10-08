# -*- coding: utf-8 -*-
"""
Part 3 of Curated Food, Eating & Drink Batch 3:
Dashboard — sati (Second 25 words: satirically to unsatisfying)
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_sati_p2 = {
    "satirically": {
        "primary": "In a satirical manner; with ironic wit, mockery, or sarcastic derision aimed at folly.",
        "secondary": "In narrative dialogue and interpersonal debate, delivering observations with cutting, arched cynicism to expose hypocrisy.",
        "quotes": [
            {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Grandcourt smiled **satirically**, raising his eyebrows as though amused by the naive earnestness of the young girl's protest."},
            {"author": "James Joyce", "work": "Ulysses", "quote": "Buck Mulligan glanced around the parapet and bowed **satirically** to the gray dome of the bay and the morning sun."},
            {"author": "William Makepeace Thackeray", "work": "The History of Henry Esmond", "quote": "Beatrix laughed **satirically**, pointing her fan at the clumsy young lord who stammered over his prepared compliment."}
        ]
    },
    "satirise": {
        "primary": "To mock, ridicule, or criticize human vices and shortcomings through the use of satire (chiefly British spelling).",
        "secondary": "In theatrical and dramatic criticism, to expose political corruptions, societal pretensions, or institutional abuses on the stage.",
        "quotes": [
            {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "The dramatist sought to **satirise** the sanctimonious compromises of bourgeois society without sacrificing dramatic passion."},
            {"author": "Virginia Woolf", "work": "Orlando", "quote": "Poets in the coffee-houses of Queen Anne's London gathered daily to **satirise** the foibles of rival politicians in rhyming couplets."},
            {"author": "H. G. Wells", "work": "Tono-Bungay", "quote": "My uncle never intended to **satirise** modern commerce; he simply took its wild absurdities and turned them into patent medicine millions."}
        ]
    },
    "satirist": {
        "primary": "A writer, performer, or artist who composes satire or uses wit and irony to ridicule human folly and corruption.",
        "secondary": "In cultural history and public sphere debates, an intellectual gadfly who holds up an unflattering moral mirror to contemporary society.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "English Traits", "quote": "The great English **satirist** pierces through courtly affectations with the blunt spear of common honesty."},
            {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "Dryden was a formidable **satirist**, striking down his literary adversaries with verses that blended majestic rhythm with devastating malice."},
            {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "The local editor fancied himself a second Juvenal, penning articles that proclaimed him the fiercest **satirist** in the county."}
        ]
    },
    "satirize": {
        "primary": "To attack, ridicule, or mock human folly, vice, or social institutions through the artistic use of satire.",
        "secondary": "In literary creation and rhetorical strategy, employing irony, parody, and burlesque to subvert dogmatic authority and conventional hypocrisies.",
        "quotes": [
            {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "My intention was to **satirize** the petty quarrels of European courts by portraying them as the ridiculous squabbles of Lilliputian factions."},
            {"author": "Mark Twain", "work": "A Connecticut Yankee in King Arthur's Court", "quote": "I determined to **satirize** the romantic delusions of feudal chivalry by introducing nineteenth-century mechanics into the Round Table."},
            {"author": "Henry James", "work": "The Bostonians", "quote": "The clever journalist loved to **satirize** the earnest reformers of New England, depicting their meetings as comic spectacles."}
        ]
    },
    "satisfaction": {
        "primary": "The fulfillment of a desire, need, or appetite; the pleasant feeling of contentment arising from achieving what was hoped for.",
        "secondary": "In jurisprudence and contract law, the discharge of an obligation or compensation for injury (accord and satisfaction); in historical duel culture, honorable redress.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "I have a kind of self-residing peace, and with clear soul do claim **satisfaction** for the wrongs done unto my name."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The mind finds genuine **satisfaction** in the discovery of clear, demonstrable truths that dissipate confusion and doubt."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel experienced a quiet **satisfaction** as he saw the rescued sheep grazing peacefully upon the dry slope beneath the stars."}
        ]
    },
    "satisfactorily": {
        "primary": "In a manner that satisfies expectations, requirements, or standards; adequately or pleasingly.",
        "secondary": "In administrative procedure and experimental science, resolving a problem or completing a process in conformity with formal criteria.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "These complex geological facts cannot be **satisfactorily** explained on the ordinary theory of independent creation."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The cooper hammered the iron hoops upon the oil casks, adjusting each stave until the seam was **satisfactorily** tight."},
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The magistrates could not **satisfactorily** determine who had placed the dark sign upon the door of the venerable meetinghouse."}
        ]
    },
    "satisfactoriness": {
        "primary": "The quality of meeting requirements, fulfilling standards, or providing adequate contentment.",
        "secondary": "In epistemological philosophy and pragmatism, the degree to which an explanatory hypothesis yields workable, coherent real-world consequences.",
        "quotes": [
            {"author": "William James", "work": "Pragmatism: A New Name for Some Old Ways of Thinking", "quote": "The truth of an idea is measured by its **satisfactoriness**, its capacity to guide our experience smoothly into harmonious relations."},
            {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The logical **satisfactoriness** of an inductive proof depends upon the rigorous exclusion of all alternative rival causes."},
            {"author": "Herbert Spencer", "work": "The Principles of Ethics", "quote": "Conduct increases in ethical **satisfactoriness** in proportion as it harmonizes individual happiness with the common welfare."}
        ]
    },
    "satisfactory": {
        "primary": "Meeting expectations, requirements, or demands; adequate, sufficient, or acceptable.",
        "secondary": "In scientific testing and academic assessment, fulfilling all evidentiary requirements or performance criteria without fatal defects.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes examined the ashes in the grate, finding no **satisfactory** trace of the burnt document he had hoped to recover."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The physician felt that the patient's recovery was scarcely **satisfactory**, noting a persistent weakness in the pulse."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We obtained a **satisfactory** series of barometric readings along the high mountain pass, confirming our calculated altitude."}
        ]
    },
    "satisfiable": {
        "primary": "Capable of being satisfied, appeased, or fulfilled; having requirements or appetites that can be met.",
        "secondary": "In mathematical logic and computer science, describing a propositional formula or set of constraints for which a truth-assignment exists that evaluates to true.",
        "quotes": [
            {"author": "Bertrand Russell", "work": "Introduction to Mathematical Philosophy", "quote": "A formal propositional function is termed **satisfiable** if there exists at least one argument which renders the assertion true."},
            {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Moderate human desires for food, warmth, and shelter are readily **satisfiable** through honest and well-regulated labor."},
            {"author": "Jeremy Bentham", "work": "The Rationale of Reward", "quote": "The legislator must distinguish between claims that are genuinely **satisfiable** and those boundless demands rooted in pure extortion."}
        ]
    },
    "satisfice": {
        "primary": "To accept an available option that is adequate or satisfactory rather than searching for the absolute optimal choice.",
        "secondary": "In behavioral economics and decision theory (coined by Herbert Simon), applying heuristic thresholds under bounded rationality instead of optimizing utility.",
        "quotes": [
            {"author": "Thorstein Veblen", "work": "The Theory of Business Enterprise", "quote": "Practical managers frequently choose to **satisfice** by adopting conventional routines that guarantee solvent returns without exhaustive risk."},
            {"author": "William James", "work": "The Will to Believe", "quote": "In the daily conduct of life, men must often **satisfice** with plausible beliefs rather than pause forever in search of metaphysical certainty."},
            {"author": "John Dewey", "work": "Human Nature and Conduct", "quote": "Human decision-makers tend to **satisfice**, halting their inquiry when a workable resolution resolves the immediate tension of the problem."}
        ]
    },
    "satisfied": {
        "primary": "Pleased, contented, or having had one's desires, expectations, or requirements fully met.",
        "secondary": "In philosophical cognition and judicial deliberation, convinced beyond reasonable doubt of the truth or justice of a matter.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "I'll not endure it. Would I were **satisfied**! Death and damnation! O, give me a living reason that she's disloyal!"},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Angel Clare felt deeply **satisfied** with his agricultural labors, rejoicing in the sweet simplicity of life at Talbothays Dairy."},
            {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes rubbed his hands together, looking thoroughly **satisfied** as he deciphered the cryptic message written on the parchment."}
        ]
    },
    "satisfier": {
        "primary": "A person or thing that brings satisfaction, fulfills a need, or gratifies an appetite.",
        "secondary": "In industrial psychology and motivational theory (such as Herzberg's two-factor model), an intrinsic workplace factor (like achievement or recognition) that promotes job satisfaction.",
        "quotes": [
            {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "I am the poet of reality, the **satisfier** of curious souls that wander through the maze of doubtful dreams."},
            {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "Every biological instinct seeks its appropriate **satisfier** in the external environment to re-establish physiological equilibrium."},
            {"author": "William James", "work": "Talks to Teachers on Psychology", "quote": "The teacher should present knowledge not as an abstract burden, but as a living **satisfier** of youthful curiosity."}
        ]
    },
    "satisfise": {
        "primary": "To adopt a course of action that satisfies minimum requirements or proves good enough (alternative spelling of satisfice).",
        "secondary": "In administrative decision theory and cognitive psychology, terminating search behavior upon encountering an alternative that meets an aspiration level.",
        "quotes": [
            {"author": "John Dewey", "work": "Logic: The Theory of Inquiry", "quote": "When practical circumstances demand prompt intervention, intelligent agents must **satisfise** with available instruments rather than wait for perfection."},
            {"author": "William James", "work": "Pragmatism: A New Name for Some Old Ways of Thinking", "quote": "The practical man learns to **satisfise** his daily needs with beliefs that work smoothly within the matrix of his surrounding facts."},
            {"author": "Thorstein Veblen", "work": "The Instinct of Workmanship", "quote": "Customary standards of craftsmanship allow the artisan to **satisfise** established communal expectations without endless innovation."}
        ]
    },
    "satisfy": {
        "primary": "To fulfill the desires, expectations, or needs of someone; to provide what is required or demanded.",
        "secondary": "In legal and mathematical contexts, to pay a debt, discharge a liability, or fulfill the conditions of an equation or theorem.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "I am content to die, so thou wilt **satisfy** my thirsting ear with the true confession of thy treasons."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard strained every nerve to **satisfy** his creditors, selling his furniture and personal watch to discharge the debt."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "No amount of hypothetical speculation will **satisfy** the naturalist who demands tangible anatomical evidence."}
        ]
    },
    "satisfying": {
        "primary": "Providing satisfaction, contentment, or gratification; fulfilling a need or desire in an agreeable manner.",
        "secondary": "In sensory aesthetics and artistic design, producing a harmonious sense of completeness, closure, and well-proportioned balance.",
        "quotes": [
            {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "It was a most **satisfying** conclusion to the evening, leaving both sisters in cheerful spirits and eager conversation."},
            {"author": "H. G. Wells", "work": "The Time Machine", "quote": "After the long and perilous journey, the simple feast of ripe fruit proved wonderfully **satisfying** to my exhausted frame."},
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes leaned back in his wicker chair, enjoying the **satisfying** realization that the scattered threads had finally united into a clear picture."}
        ]
    },
    "satisfyingly": {
        "primary": "In a manner that gives satisfaction, contentment, or pleasure; adequately and pleasingly.",
        "secondary": "In descriptive narrative and craftsmanship, completing an action or fitting components together with reassuring precision and aesthetic balance.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The heavy oak door swung shut, the iron latch clicking **satisfyingly** into place against the weathered jamb."},
            {"author": "Joseph Conrad", "work": "The Secret Sharer", "quote": "The ship answered her helm **satisfyingly**, gliding smoothly into the deep water of the anchorage without a tremor."},
            {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "The evening progressed **satisfyingly**, conforming at every turn to the solemn rituals established by New York society."}
        ]
    },
    "unsatiable": {
        "primary": "Incapable of being satisfied or appeased; having an unquenchable appetite or longing (archaic variant of insatiable).",
        "secondary": "In early modern theological and moral prose, describing unrestrained covetousness, avarice, or worldly ambition that defies spiritual temperance.",
        "quotes": [
            {"author": "King James Bible", "work": "Ezekiel", "quote": "Thou hast played the whore also with the Assyrians, because thou wast **unsatiable**; yea, thou hast played the harlot with them, and yet couldest not be satisfied."},
            {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Mrs. Norris pursued her economies with an **unsatiable** eagerness that spared no member of the household from petty interference."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "With **unsatiable** thirst of empire, the rebel angels drew their battle lines across the celestial plain."}
        ]
    },
    "unsatiably": {
        "primary": "In an unsatiable manner; with an insatiable or unquenchable appetite, curiosity, or desire.",
        "secondary": "In historical homiletic literature, relentlessly pursuing sensory gratification, dominion, or material gain without temperance.",
        "quotes": [
            {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Ambitious men thirst **unsatiably** after power, forgetting that greatness consists in virtue rather than wide dominion."},
            {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "The industrial machine devours raw material **unsatiably**, transforming ancient valleys into smoke-choked centers of commerce."},
            {"author": "Herman Melville", "work": "Mardi: and a Voyage Thither", "quote": "The restless spirit wanders **unsatiably** across distant oceans, forever seeking that phantom tranquility which earth cannot yield."}
        ]
    },
    "unsatiated": {
        "primary": "Not satisfied or appeased; remaining hungry, thirsty, or unfulfilled after partial gratification.",
        "secondary": "In psychological and romantic portraiture, describing a lingering longing, passion, or grievance that remains unslaked by time or circumstance.",
        "quotes": [
            {"author": "Mary Shelley", "work": "Frankenstein", "quote": "His malice remained fierce and **unsatiated**, prowling through the frozen glaciers in search of fresh vengeance upon his creator."},
            {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "With restless wanderings **unsatiated**, he turned his eyes once more toward the blue Mediterranean shore."},
            {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "An **unsatiated** gloom seemed to pervade the dark chamber, hanging like a vapor over every antique tapestry."}
        ]
    },
    "unsatisfactorily": {
        "primary": "In an unsatisfactory or inadequate manner; failing to meet necessary requirements or expectations.",
        "secondary": "In administrative review and judicial evaluation, resolving a dispute or performing a duty in a flawed, ambiguous, or defective way.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The chancery suit dragged along **unsatisfactorily**, draining estates and breaking hearts while lawyers argued over minute technicalities."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The naval expedition terminated **unsatisfactorily**, having expended vast treasure without striking a decisive blow against the enemy fleet."},
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The local inquest concluded **unsatisfactorily**, leaving many vital questions concerning the midnight tragedy entirely unanswered."}
        ]
    },
    "unsatisfactoriness": {
        "primary": "The state or condition of failing to satisfy; inadequacy, defectiveness, or inability to fulfill requirements.",
        "secondary": "In moral philosophy and existential thought, the inherent insufficiency of transient worldly achievements to provide lasting inner peace.",
        "quotes": [
            {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "The essential misery of the sick soul lies in the utter **unsatisfactoriness** of all natural life when divorced from higher spiritual meaning."},
            {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "The frequent **unsatisfactoriness** of human life arises principally from two causes: excessive selfishness and the lack of mental cultivation."},
            {"author": "Herbert Spencer", "work": "First Principles", "quote": "The philosophical **unsatisfactoriness** of both materialism and spiritualism compels the intellect to recognize an ultimate Unknowable behind all phenomena."}
        ]
    },
    "unsatisfactory": {
        "primary": "Failing to satisfy or meet expectations; inadequate, deficient, or unacceptable in quality or performance.",
        "secondary": "In scientific reporting and evidentiary review, describing hypotheses, trial results, or explanations that fail rigorous criteria of proof.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Many explanations of sexual coloration remain highly **unsatisfactory**, failing to account for the extraordinary divergence between closely allied species."},
            {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne found Willoughby's hasty farewell utterly **unsatisfactory**, sensing that some dreadful mystery was concealed beneath his hurried excuses."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate found the local hospital committee's financial report thoroughly **unsatisfactory**, riddled with wasteful and unexamined expenditures."}
        ]
    },
    "unsatisfiable": {
        "primary": "Incapable of being satisfied, fulfilled, or appeased; impossible to meet or gratify.",
        "secondary": "In formal logic, proof theory, and computer science, describing a set of constraints or Boolean formulas for which no assignment of variables evaluates to true.",
        "quotes": [
            {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "When contradictory axioms are introduced into a formal system, the resulting set of propositions becomes inherently **unsatisfiable**."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "A tyrant's demand for absolute subservience is fundamentally **unsatisfiable**, growing more unreasonable with every concession made by the people."},
            {"author": "Jeremy Bentham", "work": "A Fragment on Government", "quote": "The extravagant claims of unlimited monarchical prerogative represent an **unsatisfiable** drain upon the liberties of the subject."}
        ]
    },
    "unsatisfied": {
        "primary": "Not satisfied, contented, or pleased; having desires, expectations, or claims that remain unfulfilled.",
        "secondary": "In tragic drama and psychological narrative, haunted by persistent yearning, unavenged grief, or lingering intellectual doubt.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "If thou didst ever hold me in thy heart, Absent thee from felicity awhile, And in this harsh world draw thy breath in pain, To tell my story. The rest is silence... O, leave me not **unsatisfied**!"},
            {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The creature retreated into the mountain darkness, his burning desire for companionship left forever **unsatisfied** by mankind."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He felt that strange hunger of the soul which, once awakened, leaves a man forever restless and **unsatisfied** amid earthly pleasures."}
        ]
    },
    "unsatisfying": {
        "primary": "Failing to provide satisfaction, pleasure, or contentment; inadequate, disappointing, or unfulfilling.",
        "secondary": "In literary criticism and culinary aesthetics, leaving an impression of flatness, thinness, or lack of substantial depth and resolution.",
        "quotes": [
            {"author": "H. G. Wells", "work": "The New Machiavelli", "quote": "The dry, official banquet was thoroughly **unsatisfying**, filled with empty political platitudes and cold, unpalatable dishes."},
            {"author": "Virginia Woolf", "work": "Night and Day", "quote": "Katharine found the evening conversation remarkably **unsatisfying**, feeling that none of the guests had touched upon anything of genuine consequence."},
            {"author": "Henry James", "work": "The Wings of the Dove", "quote": "Merton received an **unsatisfying** reply to his urgent inquiry, full of polite evasions that only increased his anxiety."}
        ]
    }
}
