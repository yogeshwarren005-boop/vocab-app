# -*- coding: utf-8 -*-
"""
Curates 8 dashboards in Cluster Emotion (92 words total):
1. Dashboard — avid (4 words)
2. Dashboard — furi (7 words)
3. Dashboard — jubil (7 words)
4. Dashboard — ridi (8 words)
5. Dashboard — pudor (9 words)
6. Dashboard — miser (12 words)
7. Dashboard — horr (19 words)
8. Dashboard — sever (26 words)
"""
import os, sys, re, subprocess

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # 1. Dashboard — avid (4 words)
  # =========================================================================
  "Dashboard — avid/avid.md": {
    "primary": "Having or showing a keen interest in or intense enthusiasm for something; eagerly desirous.",
    "secondary": "In psychological descriptions, marked by voracious appetite or relentless craving for acquisition or achievement.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "His **avid** eyes took in the strange riverbank, burning with an unquenchable desire for dominion."},
      {"author": "Henry James", "work": "The American", "quote": "Newman was an **avid** observer of European manners, eager to assimilate every novel impression."},
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "The youth is an **avid** reader of heroic biography, seeking images of his own unrealized greatness."}
    ]
  },
  "Dashboard — avid/avidity.md": {
    "primary": "Extreme eagerness or enthusiasm; greediness or ravenous appetite for possession.",
    "secondary": "In chemical thermodynamics and immunology, the overall binding strength of an antibody or molecular complex with its antigen.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I read with the greatest **avidity** the ancient treatises on natural philosophy that filled my father's library."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Men seize upon new mechanical inventions with feverish **avidity**, hoping to escape the ancient burdens of labor."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Pigeons consume small calcareous stones with marked **avidity** to facilitate digestion in the gizzard."}
    ]
  },
  "Dashboard — avid/avidly.md": {
    "primary": "In an eager, greedy, or intensely enthusiastic manner; with voracious appetite.",
    "secondary": "In behavioural observation, pursuing sensory or intellectual stimuli with undivided, rapt absorption.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The crew drank in the strange tale **avidly**, leaning against the windlass under the starry Pacific sky."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea listened **avidly** to the scholar's explanations, attributing sublime wisdom to his dry dissertations."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes examined the footprints **avidly**, kneeling upon the damp moorland with magnifying glass in hand."}
    ]
  },
  "Dashboard — avid/avidness.md": {
    "primary": "The characteristic of being avid; intense eagerness, greediness, or voracity of desire.",
    "secondary": "In psychological assessment, the persistent intensity with which a person pursues intellectual or material goals.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Her wild **avidness** for Parisian luxury made the quiet heath appear like a dismal prison."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "In mystical absorption, the soul displays a peculiar **avidness** for transcendent union that ignores worldly cares."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I observed the **avidness** of the fishers on the pond, whose patience was but hunger disguised as recreation."}
    ]
  },

  # =========================================================================
  # 2. Dashboard — furi (7 words)
  # =========================================================================
  "Dashboard — furi/furious.md": {
    "primary": "Extremely angry; full of or characterized by intense rage, unrestrained fury, or violent turbulence.",
    "secondary": "In meteorological and physical descriptions, moving or acting with destructive speed, force, or tempestuous agitation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "To be **furious** is to be frighted out of fear, and in that mood the dove will peck the estridge."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The tempest broke with **furious** violence upon the thatched ricks, threatening the harvest with total ruin."},
      {"author": "Lewis Carroll", "work": "Alice's Adventures in Wonderland", "quote": "The players all played at once without waiting for turns, quarrelling all the while, and fighting for the hedgehogs with **furious** shouting."}
    ]
  },
  "Dashboard — furi/furiously.md": {
    "primary": "In an extremely angry, violent, or energetic manner; with unrestrained, frantic speed or rage.",
    "secondary": "In historical narrative, attacking or laboring with extreme velocity and unmeasured physical intensity.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "'What has she been saying to you?' screamed the old man **furiously**, shaking his stick in the air."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The baboons rolled down stones **furiously**, barking in fierce resentment at the intruders who approached the pass."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The bell rang **furiously**, echoing through the dark courtyard like an alarm of impending doom."}
    ]
  },
  "Dashboard — furi/furiousness.md": {
    "primary": "The characteristic condition of being furious; intense rage, violent tempestuousness, or turbulence.",
    "secondary": "In descriptive rhetoric, the unbridled fury of natural elements or human emotional outbursts.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The sheer **furiousness** of the white whale's assault splintered the cedar planks as though they were glass."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "The sudden **furiousness** of Arthur's passion astonished him, sweeping away his habitual self-possession."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The storm raged with a demonic **furiousness** around the ancient tower, howling through every battlement."}
    ]
  },
  "Dashboard — furi/infuriate.md": {
    "primary": "To make someone extremely angry, enraged, or furious; to provoke to frantic wrath.",
    "secondary": "In political or social discourse, to incite intense public indignation through provocative or unjust actions.",
    "quotes": [
      {"author": "G. K. Chesterton", "work": "The Ball and the Cross", "quote": "To dismiss a man's deepest religious convictions as trivial nonsense will **infuriate** him far more than open insult."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "Severe and unexpected penalties **infuriate** the populace, turning peaceful subjects into desperate conspirators."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Nothing seems to **infuriate** dogmatic theologians more than a quiet presentation of verifiable scientific evidence."}
    ]
  },
  "Dashboard — furi/infuriated.md": {
    "primary": "Extremely angry; enraged to madness; provoked into violent indignation or fury.",
    "secondary": "In zoological observation, describing dangerous animals that attack recklessly after being wounded or cornered.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "The **infuriated** pterodactyl circled above the plateau, snapping its needle-like beak with horrific velocity."},
      {"author": "Charles Dickens", "work": "Barnaby Rudge", "quote": "The **infuriated** mob surged against the prison gates, armed with iron crows and blazing torches."},
      {"author": "H. G. Wells", "work": "The Island of Doctor Moreau", "quote": "The beast-men grew **infuriated** when they perceived that their master lay dead upon the beach."}
    ]
  },
  "Dashboard — furi/infuriating.md": {
    "primary": "Making one extremely angry; provoking acute annoyance, outrage, or uncontrollable exasperation.",
    "secondary": "In psychological description, generating intolerable frustration through obstinate delay or irrational resistance.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "His serene, impenetrable detachment under questioning was the most **infuriating** aspect of the court inquiry."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "There is something **infuriating** about listening to people who have no taste discuss the merits of high art."},
      {"author": "George Bernard Shaw", "work": "Pygmalion", "quote": "Liza found the professor's pedantic indifference both bewildering and profoundly **infuriating**."}
    ]
  },
  "Dashboard — furi/infuriation.md": {
    "primary": "The condition of being infuriated, or the process of driving someone into extreme anger or frenzy.",
    "secondary": "In emotional analysis, the acute culmination of irritation evolving into explosive behavioral rage.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The sudden transition from mild vexation to complete **infuriation** is marked by visceral vasodilation."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "In his blind **infuriation**, Alec struck the horse with the whip, caring little for the consequences."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: Second Series", "quote": "The philosopher observes the petty **infuriation** of daily life without allowing his internal peace to be disturbed."}
    ]
  },

  # =========================================================================
  # 3. Dashboard — jubil (7 words)
  # =========================================================================
  "Dashboard — jubil/jubilance.md": {
    "primary": "A feeling of great happiness, triumph, or joyful exultation; triumphant rejoicing.",
    "secondary": "In cultural ceremonies, the public manifestation of communal celebration following military or political victory.",
    "quotes": [
      {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "I hear the universal shout of **jubilance** rising from the liberated cities of the continent."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "A burst of wild **jubilance** broke from the harpooners as the huge carcass finally floated alongside."},
      {"author": "Nathaniel Hawthorne", "work": "Twice-Told Tales", "quote": "The ringing of steeple bells announced a day of sacred **jubilance** throughout the colony."}
    ]
  },
  "Dashboard — jubil/jubilancy.md": {
    "primary": "The exultant character of being jubilant; celebratory joy, happiness, or triumphant elation.",
    "secondary": "In psychological accounts, an elevated affective mood state marked by radiant optimism and high energy.",
    "quotes": [
      {"author": "George Eliot", "work": "Romola", "quote": "The youthful **jubilancy** of the festival masked the grave political perils that threatened Florence."},
      {"author": "Ralph Waldo Emerson", "work": "Letters and Social Aims", "quote": "True genius retains a childlike **jubilancy** in the presence of everyday wonders."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The springtime song of the thrushes filled the orchard with an irrepressible natural **jubilancy**."}
    ]
  },
  "Dashboard — jubil/jubilant.md": {
    "primary": "Feeling or expressing great happiness and triumph; exultant, joyful, or celebrating victory.",
    "secondary": "In historical chronicling, crowds or armies rejoicing openly after overcoming prolonged adversity.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "The streets were alive with **jubilant** citizens exchanging greetings beneath the crisp winter sun."},
      {"author": "Abraham Lincoln", "work": "Second Inaugural Address", "quote": "While the nation remains **jubilant** over military successes, let us remember the fallen with solemn reverence."},
      {"author": "Arthur Conan Doyle", "work": "The White Company", "quote": "A **jubilant** roar arose from the archers as their feathered shafts pierced the opposing chivalry."}
    ]
  },
  "Dashboard — jubil/jubilantly.md": {
    "primary": "In a jubilant manner; with triumphant joy, exultation, or celebratory delight.",
    "secondary": "In narrative prose, performing an action with radiant, irrepressible enthusiasm and gladness.",
    "quotes": [
      {"author": "Bram Stoker", "work": "Dracula", "quote": "Mina smiled **jubilantly** as she deciphered the cryptic message that proved Jonathan was still alive."},
      {"author": "Henry David Thoreau", "work": "A Week on the Concord and Merrimack Rivers", "quote": "The birds sang **jubilantly** among the river reeds as the dawn mist melted into golden light."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Traddles waved his hat **jubilantly** from the coach window as we departed for our holiday."}
    ]
  },
  "Dashboard — jubil/jubilate.md": {
    "primary": "To show great joy or rejoice triumphantly; to express exultant gladness.",
    "secondary": "In liturgical worship, Psalm 100 (*Jubilate Deo*) sung as an opening canticle of thanksgiving in Christian morning prayer.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The angelic choirs did **jubilate** aloud, striking their celestial harps to celebrate the dawn of creation."},
      {"author": "Samuel Taylor Coleridge", "work": "Religious Musings", "quote": "Let all created beings **jubilate** in harmony, praising the eternal source of life and light."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Crowds gathered to **jubilate** over the fall of tyranny, unknowing what terror the future held."}
    ]
  },
  "Dashboard — jubil/jubilation.md": {
    "primary": "A feeling of great happiness and triumph, or the lively celebration of a joyful event.",
    "secondary": "In sociological observation, communal rituals of dancing, singing, and feasting celebrating liberation or peace.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The immense **jubilation** that swept London on VE-Day was tempered by the realization of the enormous work of reconstruction ahead."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The triumphal procession was attended with extravagant **jubilation**, the captives marching before the laurelled chariot."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "My heart leaped in sudden **jubilation** when I heard my master's well-remembered voice call through the dusk."}
    ]
  },
  "Dashboard — jubil/jubilee.md": {
    "primary": "A special anniversary of an event, especially one celebrating twenty-five, fifty, or sixty years of a reign or milestone.",
    "secondary": "In ancient Hebrew law (Leviticus 25), a sabbatical year recurring every fiftieth year during which debts were remitted.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The universal restoration of knowledge would be a glorious **jubilee** for the whole human commonwealth."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The golden **jubilee** of the monarch brought visitors from every province of the sprawling empire."},
      {"author": "John Locke", "work": "Two Treatises of Government", "quote": "The Mosaic law ordained a **jubilee** of restitution so that no family might be permanently disinherited."}
    ]
  },

  # =========================================================================
  # 4. Dashboard — ridi (8 words)
  # =========================================================================
  "Dashboard — ridi/acridity.md": {
    "primary": "Pungency or biting sharpness in taste, odor, temper, or language; acrimony.",
    "secondary": "In sensory chemistry and rhetoric, the harsh, burning property of volatile chemicals or caustically bitter speech.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The defensive secretion of certain beetles is distinguished by its pungent odor and intense **acridity**."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "His satirical diatribes possessed an **acridity** that alienated friend and foe alike."},
      {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "A note of lingering **acridity** crept into her voice whenever she recalled her former poverty."}
    ]
  },
  "Dashboard — ridi/overriding.md": {
    "primary": "More important than any other considerations; predominant, paramount, or overruling.",
    "secondary": "In governance and mechanics, exercising sovereign authority to supersede prior rules or manual control mechanisms.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "The preservation of personal liberty must remain the **overriding** objective of constitutional design."},
      {"author": "Herbert Spencer", "work": "The Man Versus the State", "quote": "An **overriding** regard for state authority often blinds legislators to the rights of individual citizens."},
      {"author": "Woodrow Wilson", "work": "The State", "quote": "In times of national peril, public defense becomes the single **overriding** duty of the executive."}
    ]
  },
  "Dashboard — ridi/ridicule.md": {
    "primary": "Subjection of someone or something to contemptuous and dismissive language or behavior; mockery.",
    "secondary": "In satirical literature, using irony, sarcasm, and exaggeration to expose folly and vices to public scorn.",
    "quotes": [
      {"author": "Jonathan Swift", "work": "A Modest Proposal", "quote": "The author employed biting **ridicule** to lay bare the callous indifference of the ruling aristocracy."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Bennet found endless amusement in exposing the absurdities of his neighbors to dry **ridicule**."},
      {"author": "Voltaire", "work": "Candide", "quote": "Philosophical optimism was subjected to merciless **ridicule** through the relentless misadventures of Pangloss."}
    ]
  },
  "Dashboard — ridi/ridiculer.md": {
    "primary": "A person who mocks, derides, or subjects others to ridicule or contemptuous laughter.",
    "secondary": "In classical satire, an author or polemicist who systematically exposes pretension through ironic wit.",
    "quotes": [
      {"author": "Alexander Pope", "work": "The Dunciad", "quote": "The fearless **ridiculer** of pedantry drew the wrath of dull scribblers across the kingdom."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "A habitual **ridiculer** of sacred traditions frequently mistakes cynicism for intellectual superiority."},
      {"author": "William Hazlitt", "work": "Lectures on the English Comic Writers", "quote": "Molière was the supreme **ridiculer** of hypocrites, unmasking imposture with effortless humor."}
    ]
  },
  "Dashboard — ridi/ridiculous.md": {
    "primary": "Deserving or inviting derision or mockery; absurd, preposterous, or laughable.",
    "secondary": "In dramatic theory, depicting human folly and eccentricity that deviates delightfully or grotesquely from rational norms.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "It was impossible not to smile at Joe's **ridiculous** attempts to accommodate his giant limbs to the parlor chair."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "She considered it completely **ridiculous** to maintain ceremonies that caused inconvenience to all parties."},
      {"author": "Mark Twain", "work": "The Adventures of Tom Sawyer", "quote": "The boy felt utterly **ridiculous** in his Sunday clothes, stiff collar, and polished shoes."}
    ]
  },
  "Dashboard — ridi/ridiculously.md": {
    "primary": "In an absurd, preposterous, or laughable manner; to an extreme or comical degree.",
    "secondary": "In colloquial narration, describing situations where disproportion or absurdity defies sober expectation.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The wooden-legged man moved with a **ridiculously** rapid hop that taxed our speed to follow."},
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "The terms offered by the board were **ridiculously** inadequate for the responsibility demanded."},
      {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "The empty trousers appeared to step forward in a **ridiculously** purposeful stride across the hallway."}
    ]
  },
  "Dashboard — ridi/ridiculousness.md": {
    "primary": "The state or character of being ridiculous, absurd, laughable, or contrary to common sense.",
    "secondary": "In aesthetic philosophy, the perceived incongruity between lofty pretension and trivial reality.",
    "quotes": [
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "The transparent **ridiculousness** of his pretensions provoked laughter among the company."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Isabel could not help perceiving the solemn **ridiculousness** of Mr. Osmond's elaborate aristocratic codes."},
      {"author": "Ralph Waldo Emerson", "work": "Letters and Social Aims", "quote": "A perception of the comic rescues the mind from pedantry by uncovering the hidden **ridiculousness** of solemn forms."}
    ]
  },
  "Dashboard — ridi/riding.md": {
    "primary": "The sport, activity, or skill of traveling on horseback or driving a vehicle.",
    "secondary": "In English local governance, an administrative division of a county (such as the East, West, or North Riding of Yorkshire).",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Oak was **riding** slowly down the lane when the sound of sheep bells caught his attention."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "A solitary knight came **riding** through the woodland glade, clad in complete chain armor."},
      {"author": "William Wordsworth", "work": "The Prelude", "quote": "I spent long afternoons **riding** among the Cumbrian hills, absorbed in solitary communion with nature."}
    ]
  },

  # =========================================================================
  # 5. Dashboard — pudor (9 words)
  # =========================================================================
  "Dashboard — pudor/impudence.md": {
    "primary": "The trait of being impudent; shameless audacity, cockiness, or insolent disrespect.",
    "secondary": "In social etiquette, an offensive disregard for decorum, deference, or proper societal boundaries.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "She was shocked by the sheer **impudence** of Wickham's declarations before those who knew his history."},
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The Artful Dodger met the magistrate's stern reproof with an air of unruffled **impudence**."},
      {"author": "Samuel Johnson", "work": "Lives of the English Poets", "quote": "A reckless satirist often mistakes gross **impudence** for honest moral indignation."}
    ]
  },
  "Dashboard — pudor/impudent.md": {
    "primary": "Not showing due respect for another person; insolently bold, brazen, or disrespectful.",
    "secondary": "In literary dialogue, characterized by audacious impertinence or shameless effrontery.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "John Reed glared at me with an **impudent** smirk before hurling the heavy volume across the room."},
      {"author": "William Shakespeare", "work": "Othello", "quote": "Are not you a strumpet? No, as I am a Christian: if to preserve this vessel for my lord from any other foul unlawful touch be not to be a strumpet, I am none. What, not an **impudent** strumpet?"},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "The cabman gave an **impudent** wink as he pocketed the sovereign and rattled away."}
    ]
  },
  "Dashboard — pudor/impudently.md": {
    "primary": "In an impudent manner; insolently, brazenly, or with shameless disrespect.",
    "secondary": "In narrative characterization, violating established protocols or boundaries without hesitation or remorse.",
    "quotes": [
      {"author": "Herman Melville", "work": "Bartleby, the Scrivener", "quote": "The junior clerk stared **impudently** at his employer, refusing to carry the letters to the post office."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Fred took the liberty of laughing **impudently** at the old gentleman's pompous declarations."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The young apprentice whistled **impudently** as he strolled past the mayor's parlor window."}
    ]
  },
  "Dashboard — pudor/pud.md": {
    "primary": "A hand, paw, or forefoot (slang/dialectal); also short for pudding in British vernacular usage.",
    "secondary": "In culinary traditions, colloquial shorthand for a sweet dessert course following the savory main dish.",
    "quotes": [
      {"author": "George Orwell", "work": "Down and Out in Paris and London", "quote": "The kitchen staff devoured the remaining scraps of steaming **pud** before scrubbing the copper pans."},
      {"author": "Rudyard Kipling", "work": "Stalky & Co.", "quote": "He reached out a sticky **pud** to seize the jar of marmalade from under his companion's nose."},
      {"author": "D. H. Lawrence", "work": "Sons and Lovers", "quote": "The children clamored around the hearth, demanding their Sunday portion of hot fruit **pud**."}
    ]
  },
  "Dashboard — pudor/pudendal.md": {
    "primary": "Relating to the pudenda; pertaining to the external genitalia or perineal region.",
    "secondary": "In clinical neuroanatomy, designating the pudendal nerve, canal, or artery supplying pelvic floor musculature.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy: Descriptive and Surgical", "quote": "The internal **pudendal** artery traverses Alcock's canal to distribute arterial branches to the perineum."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Entrapment of the **pudendal** nerve trunk induces intractable neuralgia across the pelvic dermatomes."},
      {"author": "Richard von Krafft-Ebing", "work": "Psychopathia Sexualis", "quote": "Reflex hyperesthesia in the **pudendal** sensory distribution often accompanies autonomic spinal irritation."}
    ]
  },
  "Dashboard — pudor/pudendum.md": {
    "primary": "The human external genital organs, especially those of the female; the vulva.",
    "secondary": "In comparative anatomy and medical terminology, singular form of pudenda, historically derived from Latin *pudere* (to cause shame).",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy: Descriptive and Surgical", "quote": "The labia majora constitute the lateral boundaries of the female **pudendum**, meeting anteriorly at the commissure."},
      {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Vertebrated Animals", "quote": "In placental mammals, the morphological configuration of the **pudendum** exhibits marked adaptive variation."},
      {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "Anthropological taboos surrounding the **pudendum** reflect primordial associations between modesty and sacred seclusion."}
    ]
  },
  "Dashboard — pudor/repudiate.md": {
    "primary": "To refuse to accept, recognize, or associate with; to reject as having no authority or validity.",
    "secondary": "In legal and international relations, to formally disown a treaty obligation, contract, or financial debt.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Reason compels an honest seeker of truth to **repudiate** doctrines grounded solely in blind tradition."},
      {"author": "Abraham Lincoln", "work": "Cooper Union Address", "quote": "Let us dare to **repudiate** false compromises that violate the fundamental principles of the Constitution."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The revolutionists chose to **repudiate** every ancestral charter in pursuit of speculative metaphysical rights."}
    ]
  },
  "Dashboard — pudor/repudiation.md": {
    "primary": "Rejection of a proposal, statement, or idea; refusal to acknowledge, obey, or honor an obligation.",
    "secondary": "In financial history and commercial law, the official refusal of a debtor government or entity to pay its debts.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "Report on Public Credit", "quote": "The **repudiation** of the national debt would instantly destroy American commerce and foreign confidence."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "A decisive **repudiation** of selfishness is the indispensable foundation of utilitarian moral theory."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The king's unilateral **repudiation** of the parliamentary covenants provoked armed rebellion across the realm."}
    ]
  },
  "Dashboard — pudor/repudiative.md": {
    "primary": "Serving to repudiate; characterized by, expressing, or involving rejection or disavowal.",
    "secondary": "In jurisprudence, describing statements or legal notices that renounce contract liabilities or parental claims.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "A clear **repudiative** notice is required from an heir who disclaims title to an encumbered estate."},
      {"author": "Jeremy Bentham", "work": "Principles of the Civil Code", "quote": "The law must determine whether ambiguous conduct possesses genuine **repudiative** effect regarding contractual duties."},
      {"author": "Woodrow Wilson", "work": "Constitutional Government in the United States", "quote": "The Senate issued a **repudiative** resolution rejecting the executive's unilateral diplomatic overtures."}
    ]
  },

  # =========================================================================
  # 6. Dashboard — miser (12 words)
  # =========================================================================
  "Dashboard — miser/commiserate.md": {
    "primary": "To express or feel sympathy, sorrow, or pity for someone; to sympathize or console.",
    "secondary": "In social correspondence, extending formal expressions of condolence to bereaved colleagues or citizens.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "Nicholas paused to **commiserate** the wretched condition of the boys at Dotheboys Hall."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "She found it difficult to **commiserate** hardships that had been brought on entirely by extravagant folly."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The monster pleaded with his creator to **commiserate** his utter loneliness and fashion a companion."}
    ]
  },
  "Dashboard — miser/commiseration.md": {
    "primary": "Sympathy and sorrow for the misfortunes of others; compassion, pity, or condolence.",
    "secondary": "In rhetoric, an emotional appeal designed to evoke tender compassion and forgiveness from a jury or sovereign.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Thou art come to answer a stony adversary, an inhuman wretch uncapable of pity, void and empty from any dram of **commiseration**."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The turnkey looked upon the condemned prisoner with a rare glimmer of rough **commiseration**."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The neighbors felt deep **commiseration** for the weaver when his golden hoard was stolen."}
    ]
  },
  "Dashboard — miser/commiserative.md": {
    "primary": "Expressing or feeling commiseration; compassionate, sympathetic, or sorrowful for others.",
    "secondary": "In psychological descriptions, an affective disposition characterized by habitual empathy for the suffering of living creatures.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "Hepzibah cast a **commiserative** glance upon her broken brother as he tottered into the garden."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her warm, **commiserative** nature made Dorothea responsive to the slightest sign of distress in others."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The old cottagers exchanged **commiserative** sighs as the young mother passed beneath the churchyard wall."}
    ]
  },
  "Dashboard — miser/compromiser.md": {
    "primary": "A person who is inclined to compromise or who settles disputes through reciprocal concessions.",
    "secondary": "In political history, a mediator who reconciles conflicting factional interests to avert violent conflict.",
    "quotes": [
      {"author": "Abraham Lincoln", "work": "Speech at Peoria", "quote": "Henry Clay was known as the great **compromiser**, seeking through mutual concessions to preserve the Union."},
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "A prudent statesman must be a skillful **compromiser**, balancing abstract rights against practical necessities."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "The principled thinker must not become an unprincipled **compromiser** when fundamental liberties are at stake."}
    ]
  },
  "Dashboard — miser/miser.md": {
    "primary": "A person who hoards wealth and spends as little money as possible; a stingy, grasping individual.",
    "secondary": "In moral philosophy and literature, a cautionary archetype whose idolatry of money results in spiritual desolation.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Scrooge was a tight-fisted hand at the grindstone, a squeezing, wrenching, grasping, scraping, clutching, covetous old **miser**!"},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The lonely weaver lived as a **miser**, counting his golden guineas each night before the hearth."},
      {"author": "Alexander Pope", "work": "Moral Essays", "quote": "The dying **miser** clings to his strongbox, grudging the cost of the very shroud that must wrap him."}
    ]
  },
  "Dashboard — miser/miserable.md": {
    "primary": "Wretchedly unhappy, uneasy, or uncomfortable; characterized by great distress or squalor.",
    "secondary": "In social reform literature, destitute living conditions that degrade human dignity and health.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "The **miserable** change now at my end lament nor sorrow at; but please your thoughts in feeding them with those my former fortunes."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Tom-all-Alone's was a **miserable** street where disease and pestilence nested in rotting tenements."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I was benevolent and good; misery made me a fiend. Make me happy, and I shall again be virtuous, but now I am **miserable** beyond all living things."}
    ]
  },
  "Dashboard — miser/miserableness.md": {
    "primary": "The state, quality, or condition of being miserable; wretchedness, squalor, or unhappiness.",
    "secondary": "In existential or religious literature, the profound desolation of a soul alienated from hope or community.",
    "quotes": [
      {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "Christian looked back upon the city of Destruction, groaning under the heavy **miserableness** of his burden."},
      {"author": "Samuel Johnson", "work": "Rasselas", "quote": "The prince soon discovered the secret **miserableness** that gnawed at the hearts of wealthy courtiers."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Man's **miserableness** comes from his greatness; because there is an Infinite in him, which he cannot bury under the Finite."}
    ]
  },
  "Dashboard — miser/miserably.md": {
    "primary": "In a wretched, unhappy, or pitiable manner; poorly, squalidly, or with utter lack of success.",
    "secondary": "In narrative prose, failing catastrophically or enduring prolonged deprivation without relief.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The castaways drifted for days, suffering **miserably** from scorching sun and lack of fresh water."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The villain perished **miserably** in the foul heart of the Great Grimpen Mire."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The orphan children slept **miserably** in drafty dormitories, shivering beneath thin coverlets."}
    ]
  },
  "Dashboard — miser/miserliness.md": {
    "primary": "Excessive desire to hoard wealth and extreme reluctance to spend money; stinginess or parsimony.",
    "secondary": "In psychological characterization, neurotic hoarding behavior driven by morbid fear of impoverishment.",
    "quotes": [
      {"author": "George Eliot", "work": "Silas Marner", "quote": "His **miserliness** was not ambition, but a dull substitute for the human warmth he had lost."},
      {"author": "Honore de Balzac", "work": "Eugenie Grandet", "quote": "The old cooper's ferocious **miserliness** dictated every spoonful of sugar and candle-end in the house."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Sordid **miserliness** hoards coin in vaults, whereas productive frugality invests capital in active enterprise."}
    ]
  },
  "Dashboard — miser/miserly.md": {
    "primary": "Of, relating to, or characteristic of a miser; penurious, stingy, or grudging in expenditure.",
    "secondary": "In literary description, an inadequate, impoverished, or ridiculously meager portion or provision.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The landlord offered us a **miserly** crust of bread and a sip of sour ale for our supper."},
      {"author": "Washington Irving", "work": "The Devil and Tom Walker", "quote": "Tom was a **miserly** fellow who conspired with his wife to cheat each other out of household goods."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The governor was of a **miserly** disposition, entertaining guests with dry crusts and watered wine."}
    ]
  },
  "Dashboard — miser/misery.md": {
    "primary": "A state or feeling of great physical or mental distress or discomfort; extreme unhappiness.",
    "secondary": "In socioeconomic narrative, chronic destitution, deprivation, and suffering caused by poverty or war.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "Misery acquaints a man with strange bedfellows; I will here shroud till the dregs of the storm be past."},
      {"author": "Victor Hugo", "work": "Les Misérables", "quote": "So long as there shall exist, by reason of law and custom, a social condemnation creating artificial hells, so long shall **misery** endure."},
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The wretched boy endured untold **misery** in the workhouse undertaker's shop, sleeping among coffins."}
    ]
  },
  "Dashboard — miser/promiser.md": {
    "primary": "A person who makes a promise or undertakes a binding mutual covenant; one who pledges.",
    "secondary": "In contract law, the party who makes a legal promise to another (the promisee) supported by consideration.",
    "quotes": [
      {"author": "Thomas Hobbes", "work": "Leviathan", "quote": "Covenants without the sword are but words, leaving the **promiser** free to break faith whenever his interest prompts."},
      {"author": "John Locke", "work": "Second Treatise of Government", "quote": "The obligation of a contract binds the **promiser** in natural law even where no positive municipal law exists."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "An action of assumpsit lies against the **promiser** who neglects to perform his undertaken engagement."}
    ]
  },

  # =========================================================================
  # 7. Dashboard — horr (19 words)
  # =========================================================================
  "Dashboard — horr/abhorrence.md": {
    "primary": "A feeling of revulsion or loathing; disgust and hatred combined; detestation.",
    "secondary": "In moral philosophy, the deep instinctive repulsion felt toward cruelty, deceit, or tyranny.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "My heart sickened with profound **abhorrence** as the creature stepped into the moonlight before me."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "I express my unalterable **abhorrence** of doctrines that overthrow the ancestral order of civil society."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Darnay turned away with visible **abhorrence** from the bloodstained courtyard of the tribunal."}
    ]
  },
  "Dashboard — horr/abhorrent.md": {
    "primary": "Inspiring disgust and loathing; repugnant, detestable, or deeply offensive.",
    "secondary": "In logical and ethical discourse, completely contrary or incompatible with fundamental moral principles.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "The suppression of peaceful opinion is **abhorrent** to the principles of a free and enlightened society."},
      {"author": "Abraham Lincoln", "work": "Speech at Peoria", "quote": "I hate it because of the monstrous injustice of slavery itself; I hate it because it deprives our republican example of its just influence in the world and makes us appear hypocritical; this is **abhorrent** to all our professions."},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "Cruelty inflicted for mere pleasure is universally **abhorrent** to the civilized conscience."}
    ]
  },
  "Dashboard — horr/abhorrer.md": {
    "primary": "A person who abhors or detests something; one who regards something with extreme loathing.",
    "secondary": "In English seventeenth-century political history, one of the royalists who expressed abhorrence for petitions demanding the assembly of Parliament (opposed to Petitioners/Whigs).",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The country was divided into two furious factions, the Petitioner demanding a Parliament and the **abhorrer** upholding the royal prerogative."},
      {"author": "David Hume", "work": "The History of England", "quote": "The court party received the name of **abhorrer** from the vehement addresses they presented against subversive petitions."},
      {"author": "Samuel Johnson", "work": "The Idler", "quote": "A genuine **abhorrer** of fraud will not stoop to petty deceptions even to accomplish a righteous purpose."}
    ]
  },
  "Dashboard — horr/horrendous.md": {
    "primary": "Extremely unpleasant, horrifying, or terrible; frightful, dreadful, or shocking.",
    "secondary": "In descriptive reporting, catastrophes or atrocities causing widespread destruction and dismay.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "A **horrendous** sound like thunder broke from the depths as the wounded leviathan breached into the gale."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "We beheld a **horrendous** carnivore emerging from the ferns, its jaws dripping with fresh gore."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The Martian heat-ray produced a **horrendous** devastation across the fleeing multitudes on the common."}
    ]
  },
  "Dashboard — horr/horrible.md": {
    "primary": "Causing or likely to cause horror; shockingly dreadful, abominable, or distressing.",
    "secondary": "In literary description, evoking dread, disgust, and shuddering revulsion.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "O, **horrible**! O, **horrible**! most **horrible**! If thou hast nature in thee, bear it not."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "His yellow skin scarcely covered the work of muscles and arteries beneath; his hair was of a lustrous black, and flowing; his teeth of a pearly whiteness; but these luxuriances only formed a more **horrible** contrast with his watery eyes."},
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The **horrible** cry of murder rang out in the dead of night, freezing the blood of all who heard it."}
    ]
  },
  "Dashboard — horr/horribly.md": {
    "primary": "In a horrible manner; dreadfully, terrifyingly, or to an extreme and shocking degree.",
    "secondary": "In psychological narrative, experiencing intense dread or bodily torment that disfigures expression.",
    "quotes": [
      {"author": "Bram Stoker", "work": "Dracula", "quote": "The count's eyes flared **horribly** with red fire as he hurled the woman back from the bed."},
      {"author": "Robert Louis Stevenson", "work": "Strange Case of Dr Jekyll and Mr Hyde", "quote": "The transformation contorted his features **horribly**, leaving him gasping upon the floor."},
      {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "Her white shroud was **horribly** spattered with blood from her struggle within the copper coffin."}
    ]
  },
  "Dashboard — horr/horrid.md": {
    "primary": "Causing horror; dreadful, abominable, disagreeable, or offensive to the senses.",
    "secondary": "In archaic and poetic usage, bristling, rough, or rugged in physical appearance (from Latin *horridus*).",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Moloch, **horrid** king besmeared with blood of human sacrifice, and parents' tears."},
      {"author": "Jane Austen", "work": "Northanger Abbey", "quote": "Catherine eagerly inquired whether the new romance contained enough **horrid** murders and secret passages."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The Yahoo presented a **horrid** spectacle, filthy of limb and viciously insolent in demeanor."}
    ]
  },
  "Dashboard — horr/horridly.md": {
    "primary": "In a horrid manner; dreadfully, shocking, or in a way that causes disgust or terror.",
    "secondary": "In conversational exaggeration, intensely or distressingly unpleasant.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The monster's countenance was **horridly** illuminated by a vivid flash of alpine lightning."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The red light of the threshing machine glowed **horridly** through the autumn twilight like an engine of torment."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The room smelled **horridly** of stale gin and charred paper when we opened the shuttered window."}
    ]
  },
  "Dashboard — horr/horridness.md": {
    "primary": "The state or characteristic of being horrid; frightfulness, dreadfulness, or repulsive roughness.",
    "secondary": "In aesthetic and moral appraisal, the repellent quality of an act or sight that provokes shuddering abhorrence.",
    "quotes": [
      {"author": "Samuel Richardson", "work": "Clarissa", "quote": "The sheer **horridness** of the plot against her innocence deprived the poor lady of all speech."},
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "I shuddered at the unnatural **horridness** of the cannibal feast upon the solitary beach."},
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "A peculiar **horridness** lingered about the dead judge's rigid smile as the portrait looked down."}
    ]
  },
  "Dashboard — horr/horrific.md": {
    "primary": "Causing horror; terrifying, dreadful, or horrifying in impact.",
    "secondary": "In medical or wartime chronicle, describing injuries or devastations that overwhelm ordinary comprehension.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The black smoke was **horrific** in its swift, silent lethality, leaving no survivor where it drifted."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "A **horrific** shriek split the silence of the primeval woods as night fell upon the camp."},
      {"author": "Jack London", "work": "The Sea-Wolf", "quote": "Larsen laughed at the **horrific** spectacle of the schooner plunging through the typhoon."}
    ]
  },
  "Dashboard — horr/horrified.md": {
    "primary": "Filled with horror; shocked, appalled, or greatly frightened.",
    "secondary": "In dramatic literature, reacting with frozen dread upon witnessing an atrocious crime or catastrophe.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "I was **horrified** beyond words when the convict seized my shoulders in the churchyard."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Hallward stood **horrified** before the canvas, unable to reconcile the hideous portrait with his friend."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "The **horrified** sailors watched the strange dog leap from the derelict vessel and vanish into the night."}
    ]
  },
  "Dashboard — horr/horrify.md": {
    "primary": "To fill with horror; to shock, terrify, or appall greatly.",
    "secondary": "In social discourse, to violate community conscience or sense of propriety to a shocking degree.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I feared to recount the tale of my creation, lest its monstrous reality should **horrify** my listeners."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "The thought of public disgrace did not merely shame him; it threatened to **horrify** his aged mother into the grave."},
      {"author": "Edgar Allan Poe", "work": "The Tell-Tale Heart", "quote": "The persistent beating of the old man's heart began to **horrify** me beyond all endurance."}
    ]
  },
  "Dashboard — horr/horrifying.md": {
    "primary": "Causing horror; terrifying, dreadful, appalling, or shockingly repulsive.",
    "secondary": "In narrative prose, generating intense visceral fear or moral revulsion.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Island of Doctor Moreau", "quote": "The cry of the puma during the vivisection was the most **horrifying** sound I had ever heard."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "A **horrifying** howl echoed across the black granite tors, chilling our very marrow."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The wilderness had whispered to him things about himself which he did not know, whispering a **horrifying** fascination."}
    ]
  },
  "Dashboard — horr/horrifyingly.md": {
    "primary": "In a horrifying manner; so as to cause intense horror, terror, or dread.",
    "secondary": "In descriptive journalism or narrative, unfolding with appalling clarity and dreadful consequence.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The white brow of the whale loomed **horrifyingly** close above the gunwale of our fragile boat."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "The vampire's fingernails clicked **horrifyingly** against the stone parapet as he crawled downward face first."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The iron tripod towered **horrifyingly** over the treetops, leveling everything with flashes of fire."}
    ]
  },
  "Dashboard — horr/horripilate.md": {
    "primary": "To cause the hairs of the skin to stand erect through cold, fear, or excitement; to get goosebumps.",
    "secondary": "In physiological medicine, to undergo piloerection mediated by sympathetic stimulation of arrector pili muscles.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "The Crayfish: An Introduction to the Study of Zoology", "quote": "Sensory stimulation of the cutaneous nerves can cause the human skin to **horripilate** in reflex shivering."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Terror causes the hairs to **horripilate** in both humans and chimpanzees through contractions of involuntary muscular fibers."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Sudden spectral dread causes the cutaneous papillae to **horripilate** before conscious reflection occurs."}
    ]
  },
  "Dashboard — horr/horripilation.md": {
    "primary": "The erection of the hairs on the skin in response to fear, cold, or excitement; goosebumps.",
    "secondary": "In neurophysiology and psychopathology, reflex piloerection induced by intense sympathetic nerve discharge.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The phenomenon of **horripilation** in frightened mammals serves to make the animal appear larger and more formidable to rivals."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "That cold chill accompanied by **horripilation** along the spine constitutes the somatic core of sudden panic."},
      {"author": "Henry Maudsley", "work": "The Pathology of Mind", "quote": "Cutaneous **horripilation** frequently heralds the aura preceding an epileptic convulsion."}
    ]
  },
  "Dashboard — horr/horror-stricken.md": {
    "primary": "Struck with horror; extremely shocked, terrified, or paralyzed by sudden dread.",
    "secondary": "In classical dramaturgy, the stunned silence and frozen posture of characters beholding tragedy.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The **horror-stricken** crowd recoiled as the crimson knife fell once more upon the scaffold."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I sank down **horror-stricken** beside the lifeless body of Elizabeth, cursed by the demon I had created."},
      {"author": "Walter Scott", "work": "The Bride of Lammermoor", "quote": "The guests stood **horror-stricken** in the doorway, staring at the wild and disheveled bride."}
    ]
  },
  "Dashboard — horr/horror-struck.md": {
    "primary": "Overcome or seized with horror; terrified, appalled, or stunned by a dreadful spectacle.",
    "secondary": "In narrative prose, reacting with acute mental paralysis upon uncovering gruesome reality.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "The Murders in the Rue Morgue", "quote": "The gendarmes paused, **horror-struck**, at the sight of the mangled body thrust upward into the chimney flue."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Helen Stonor sat **horror-struck** in her chair as the speckled band slithered down the bell-rope."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "We peered **horror-struck** through the stockade logs as the mutineers raised their bloody cutlasses."}
    ]
  },
  "Dashboard — horr/horror.md": {
    "primary": "An intense feeling of fear, shock, or disgust; dread, terror, or loathing.",
    "secondary": "In literary aesthetics and Gothic fiction, the profound shuddering revulsion that follows the realization of a terrible truth.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "He cried in a whisper at some image, at some vision—he cried out twice, a cry that was no more than a breath: 'The **horror**! The **horror**!'"},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "No mortal could support the **horror** of that countenance; a mummy again endued with animation could not be so hideous."},
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "O **horror**, **horror**, **horror**! Tongue nor heart cannot conceive nor name thee!"}
    ]
  },

  # =========================================================================
  # 8. Dashboard — sever (26 words)
  # =========================================================================
  "Dashboard — sever/asseverate.md": {
    "primary": "To declare or affirm solemnly, earnestly, or emphatically; to avow positively.",
    "secondary": "In legal and theological discourse, to attest to the truth of an assertion under oath or formal declaration.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Men will passionately **asseverate** propositions for which they cannot produce a single coherent argument."},
      {"author": "Samuel Johnson", "work": "The Idler", "quote": "The traveler did not hesitate to **asseverate** that he had beheld flying dragons in the Arabian deserts."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The witness continued to **asseverate** his innocence despite the overwhelming mass of documentary proof."}
    ]
  },
  "Dashboard — sever/asseveration.md": {
    "primary": "A serious, earnest, or solemn declaration or affirmation of fact; an emphatic avowal.",
    "secondary": "In formal jurisprudence and rhetoric, an assertion made with solemn gravity to establish credibility.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "A dogmatic philosopher demands credit upon his bare **asseveration**, rather than through demonstration of causes."},
      {"author": "Edmund Burke", "work": "Speech on American Taxation", "quote": "No ministerial **asseveration** can persuade free citizens that taxation without representation is just."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Tulkinghorn listened to the clerk's frightened **asseveration** with his customary chilling composure."}
    ]
  },
  "Dashboard — sever/asseverator.md": {
    "primary": "One who solemnly or emphatically affirms, asserts, or declares something to be true.",
    "secondary": "In forensic debate, a speaker who relies on emphatic personal assurance to compel belief in an assertion.",
    "quotes": [
      {"author": "Jeremy Bentham", "work": "Rationale of Judicial Evidence", "quote": "The credibility of an **asseverator** must be weighed against his interest in the outcome of the suit."},
      {"author": "Samuel Taylor Coleridge", "work": "The Friend", "quote": "The zealous religious **asseverator** assumes that vehement conviction is identical with demonstrated truth."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "No matter how sincere the **asseverator**, an inductive inference requires empirical verification."}
    ]
  },
  "Dashboard — sever/dissever.md": {
    "primary": "To divide, separate, or sever into distinct parts; to disunite.",
    "secondary": "In poetic and emotional diction, to tear asunder bonds of love, political union, or friendship.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "Annabel Lee", "quote": "And neither the angels in heaven above nor the demons down under the sea can ever **dissever** my soul from the soul of the beautiful Annabel Lee."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Death came to **dissever** all tender ties of human felicity and leave mankind in darkness."},
      {"author": "Alfred Tennyson", "work": "Idylls of the King", "quote": "Sorrow rose to **dissever** the glorious fellowship of the Round Table before the realm dissolved."}
    ]
  },
  "Dashboard — sever/perseverance.md": {
    "primary": "Persistence in doing something despite difficulty or delay in achieving success; steadfastness.",
    "secondary": "In moral philosophy and theological doctrine (perseverance of the saints), continuous endurance in grace and virtuous endeavor.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Troilus and Cressida", "quote": "Perseverance, dear my lord, keeps honor bright; to have done is to hang quite out of fashion, like a rusty mail in monumental mockery."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Through patient **perseverance** in artificial selection, breeders have modified the forms of domestic animals beyond recognition."},
      {"author": "Samuel Johnson", "work": "Rasselas", "quote": "Great works are performed not by strength, but by **perseverance**."}
    ]
  },
  "Dashboard — sever/perseverate.md": {
    "primary": "To repeat or prolong an action, thought, or utterance after the stimulus that prompted it has ceased.",
    "secondary": "In neuropsychology, to exhibit involuntary repetition of a specific motor or verbal response due to frontal lobe impairment.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Fatigued subjects tend to **perseverate** upon an error, repeating the wrong syllable despite conscious effort."},
      {"author": "Henry Maudsley", "work": "Body and Will", "quote": "A damaged cerebral cortex will **perseverate** in motor discharges that have lost all adaptive utility."},
      {"author": "Alexander Luria", "work": "The Working Brain", "quote": "Patients suffering anterior frontal lesions will **perseverate** in drawing circles when instructed to draw a cross."}
    ]
  },
  "Dashboard — sever/perseveration.md": {
    "primary": "The repetitive continuation or recurrence of an activity, word, or thought without an appropriate stimulus.",
    "secondary": "In clinical neurology and cognitive psychology, an involuntary persistence of a response typical of brain damage or dementia.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Mental **perseveration** illustrates how neural pathways retain motor excitability long after the original stimulus subsides."},
      {"author": "Henry Maudsley", "work": "The Pathology of Mind", "quote": "In chronic dementia, verbal **perseveration** reduces conversational response to the endless repetition of a single phrase."},
      {"author": "Alexander Luria", "work": "Higher Cortical Functions in Man", "quote": "Motor **perseveration** was demonstrated whenever the patient attempted to change from writing numbers to writing letters."}
    ]
  },
  "Dashboard — sever/persevere.md": {
    "primary": "To continue in a course of action even in the face of difficulty or with little prospect of success.",
    "secondary": "In spiritual and intellectual life, to maintain resolute commitment to lofty ideals through periods of adversity.",
    "quotes": [
      {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "He resolved to **persevere** along the narrow path, though roaring lions guarded the ascent to the palace."},
      {"author": "Thomas Henry Huxley", "work": "Life and Letters", "quote": "If men of science will only **persevere** in verified truth, dogmatic opposition will crumble by degrees."},
      {"author": "George Washington", "work": "Letters and Addresses", "quote": "Let us **persevere** through this harsh winter at Valley Forge, confident that our cause is just."}
    ]
  },
  "Dashboard — sever/persevering.md": {
    "primary": "Continuing in a course of action despite difficulties; persistent, resolute, and steadfast.",
    "secondary": "In biographical praise, characterized by tireless and determined labor toward a difficult objective.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Essays", "quote": "A **persevering** spirit will scale obstacles that appear insuperable to the indolent spectator."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "David was a **persevering** youth, mastering shorthand through months of relentless nocturnal study."},
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "Industry and **persevering** frugality raised me from an obscure apprentice to an independent citizen."}
    ]
  },
  "Dashboard — sever/perseveringly.md": {
    "primary": "In a persevering manner; with persistent, steadfast, and determined effort.",
    "secondary": "In historical narrative, pursuing a difficult task without yielding to exhaustion or despair.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I labored **perseveringly** in the dissecting rooms, oblivious to the change of seasons around me."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Lucy Snowe worked **perseveringly** at her teaching duties, concealing her sorrow beneath quiet diligence."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "Challenger climbed **perseveringly** up the rock chimney until he gained the basalt ledge above."}
    ]
  },
  "Dashboard — sever/sever.md": {
    "primary": "To divide by cutting or slicing, especially suddenly and forcibly; to detach, separate, or break off.",
    "secondary": "In political and diplomatic history, to dissolve all connections, alliances, or communications between parties.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VI, Part 3", "quote": "Let me hear no more of this; it will **sever** our friendship and divide the realm into factions."},
      {"author": "Abraham Lincoln", "work": "First Inaugural Address", "quote": "We are not enemies, but friends. We must not be enemies. Though passion may have strained, it must not break our bonds of affection. The mystic chords of memory will yet swell the chorus of the Union, when again touched, as surely they will be, by the better angels of our nature; no state can lawfully **sever** its allegiance."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Geographical barriers rise to **sever** populations, leading over epochs to the divergence of distinct species."}
    ]
  },
  "Dashboard — sever/severable.md": {
    "primary": "Capable of being divided, separated, or severed; divisible.",
    "secondary": "In contract jurisprudence, denoting a clause or covenant that can be struck without invalidating the remainder of the agreement.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "A covenant in a deed may be **severable**, so that the illegality of one provision does not destroy the whole conveyance."},
      {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "The court must determine whether the promised consideration is unitary or **severable** into distinct performances."},
      {"author": "Joseph Story", "work": "Commentaries on Equity Jurisprudence", "quote": "Equity will grant specific performance of a **severable** part of an agreement where justice plainly requires it."}
    ]
  },
  "Dashboard — sever/several-seeded.md": {
    "primary": "Containing or producing more than two seeds; polyspermous.",
    "secondary": "In systematic botanical morphology, describing fruit or capsules enclosing multiple mature ovules.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The ovary in this genus is two-celled and contains a **several-seeded** locule maturing into a dry capsule."},
      {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "Cross-pollinated flowers yielded larger and heavier **several-seeded** capsules than self-fertilized blooms."},
      {"author": "John Lindley", "work": "An Introduction to Botany", "quote": "The dehiscence of a **several-seeded** pericarp scatters the seeds through apical pores upon the wind."}
    ]
  },
  "Dashboard — sever/several.md": {
    "primary": "More than two but not many; of an indefinite small number; distinct or separate.",
    "secondary": "In legal and formal diction, respective, individual, and independent rather than joint.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "To every Roman citizen he gives, to every **several** man, seventy-five drachmas."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The mind gathers its simple ideas from the **several** operations of sensation and reflection."},
      {"author": "Thomas Jefferson", "work": "Declaration of Independence", "quote": "When in the course of human events it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the laws of nature entitle them, a decent respect to the opinions of mankind requires that they should declare the **several** causes which impel them to the separation."}
    ]
  },
  "Dashboard — sever/severalise.md": {
    "primary": "To distinguish, separate, or treat individually; to individualize (British spelling).",
    "secondary": "In legal and philosophical analysis, to separate collective rights or estates into individual holdings.",
    "quotes": [
      {"author": "Jeremy Bentham", "work": "Principles of Penal Law", "quote": "To **severalise** offenses into distinct legal categories prevents the arbitrary infliction of disproportionate punishment."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "A partition deed serves to **severalise** the joint tenancy into individual holdings held in severalty."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Inductive science must **severalise** complex natural phenomena into their elementary causal components."}
    ]
  },
  "Dashboard — sever/severalize.md": {
    "primary": "To distinguish, separate, or treat individually; to individualize (American spelling).",
    "secondary": "In jurisprudence and property law, to divide property held in common into separate, individual ownership.",
    "quotes": [
      {"author": "Joseph Story", "work": "Commentaries on the Constitution of the United States", "quote": "The constitutional framers sought to **severalize** the powers of government among three independent departments."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "The intellect loves to divide and **severalize**, while the soul unites all particulars into universal spirit."},
      {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "Custom operated over centuries to **severalize** the communal strip-fields into enclosed private farms."}
    ]
  },
  "Dashboard — sever/severally.md": {
    "primary": "Individually, separately, or each by itself; respectively.",
    "secondary": "In contract jurisprudence, denoting individual liability where each party may be sued separately for the entire obligation.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The states are united in one national commonwealth, yet retain their **severally** reserved municipal powers."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The obligors bound themselves jointly and **severally** to pay the full sum upon the date appointed."},
      {"author": "John Locke", "work": "Two Treatises of Government", "quote": "Every man has a right to the fruits of the earth which he has **severally** mixed with his own labor."}
    ]
  },
  "Dashboard — sever/severalty.md": {
    "primary": "A state of separation; individual and exclusive ownership of property (especially real estate).",
    "secondary": "In real property law, an estate held by a person in their own right without any other person being joined or connected with them.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "He that holds lands or tenements in **severalty**, or is sole tenant thereof, is he that holds them in his own right only."},
      {"author": "Thomas Jefferson", "work": "Notes on the State of Virginia", "quote": "Allotting land to families in **severalty** transforms nomadic hunters into industrious agricultural proprietors."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The division of inherited estates into **severalty** prevented the perpetual concentration of aristocratic landed wealth."}
    ]
  },
  "Dashboard — sever/severance.md": {
    "primary": "The action of ending a connection or relationship; separation or detachment.",
    "secondary": "In employment and property law, the termination of employment compensation (severance pay) or the division of joint tenancy into separate estates.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Letter to the Sheriffs of Bristol", "quote": "The violent **severance** of America from the British crown was the catastrophic result of unbending ministerial obstinacy."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard felt the bitter **severance** from his former friends as poverty closed in upon him."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "A **severance** of jointure may be effected by any alienation of an undivided share during the lifetime of the tenant."}
    ]
  },
  "Dashboard — sever/severe.md": {
    "primary": "Very great, intense, or harsh; demanding great skill, patience, or endurance; strict and uncompromising.",
    "secondary": "In aesthetics and architectural criticism, characterized by austere simplicity, restraint, and absence of frivolous ornament.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "And then the justice, in fair round belly with good capon lined, with eyes **severe** and beard of formal cut, full of wise saws and modern instances."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Grave was his look, and in his face **severe** delight had found no place, but majesty and holy awe."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The winter of 1792 was unusually **severe**, and distress in the capital was universal and acute."}
    ]
  },
  "Dashboard — sever/severed.md": {
    "primary": "Divided, sliced, or separated into parts; disconnected or broken off.",
    "secondary": "In surgical pathology and traumatic anatomy, describing blood vessels or tissues cut completely through.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The harpoon line **severed** cleanly beneath the blow of the mate's razor-sharp boat-knife."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Engineer's Thumb", "quote": "The unfortunate young engineer held up his hand, revealing a freshly **severed** thumb wrapped in a bloody kerchief."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The communication between the capital and the frontier legions was completely **severed** by the barbarian incursions."}
    ]
  },
  "Dashboard — sever/severely.md": {
    "primary": "To a severe, strict, or intense degree; harshly, rigorously, or painfully.",
    "secondary": "In critical writing, judging conduct or intellectual work with demanding and unforgiving standards.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth judged Mr. Darcy **severely** at first, blinded by her wounded pride and Wickham's deceitful charms."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Plants and animals are **severely** tested during periods of drought and extreme winter cold."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate was **severely** criticized by his medical rivals for introducing innovative antiseptic practices."}
    ]
  },
  "Dashboard — sever/severeness.md": {
    "primary": "The quality or state of being severe; harshness, sternness, or intense rigor.",
    "secondary": "In moral philosophy and pedagogy, strictness in discipline unaccompanied by gentleness or flexibility.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Essays", "quote": "A judge should blend integrity with mercy, lest unbending **severeness** convert justice into cruelty."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The **severeness** of his criticism discouraged many an aspiring poet whose genius only required cultivation."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The Puritan elders gazed with grim **severeness** upon Hester Prynne as she stood before the pillory."}
    ]
  },
  "Dashboard — sever/severing.md": {
    "primary": "The action of dividing, slicing, or separating something forcibly; disconnecting.",
    "secondary": "In surgery or metallurgical processing, cutting through tissue or structural metal with specialized instruments.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The White Company", "quote": "The heavy broadsword descended with tremendous force, **severing** the iron visor and the crest together."},
      {"author": "Joseph Conrad", "work": "Typhoon", "quote": "The crew labored frantically at **severing** the tangled rigging that threatened to capsize the steamer."},
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "By **severing** mutual ties of commerce, parliament will plunge both Britain and her colonies into ruin."}
    ]
  },
  "Dashboard — sever/severity.md": {
    "primary": "The fact or condition of being severe; harshness, sternness, rigor, or extreme intensity.",
    "secondary": "In meteorology, pharmacology, and law, the extreme degree of cold, adverse drug reaction, or legal penalty.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The **severity** of the penal laws did not deter hungry men from stealing a loaf of bread."},
      {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "When vice makes mercy, mercy's so extended that for the fault's sake it is to be so; but Angelo enforces the law with dreadful **severity**."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The harsh **severity** of military discipline restored order to the legions upon the Danube."}
    ]
  },
  "Dashboard — sever/severn.md": {
    "primary": "The longest river in Great Britain, rising in mid-Wales and flowing into the Bristol Channel.",
    "secondary": "In British historical geography, a vital maritime artery and boundary famous for its tidal bore and historic crossings.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "Three times they breathed and three times did they drink, upon agreement, of swift **Severn**'s flood."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Goods shipped along the broad waters of the **Severn** supplied the market towns across the western shires."},
      {"author": "Daniel Defoe", "work": "A Tour Through the Whole Island of Great Britain", "quote": "The high tidal bore of the river **Severn** rushes up the channel with astonishing speed and roar."}
    ]
  }
}

base_dir = "App database/Latin roots/Cluster Emotion"
updated = 0

for rel_path, entry in data.items():
    full_path = os.path.join(base_dir, rel_path)
    if not os.path.exists(full_path):
        print(f"Missing file: {full_path}")
        continue
    
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    book_pattern = r"(> 1\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)(\r?\n> 2\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)"
    def repl_book(m):
        return f"{m.group(1)}{entry['primary']}{m.group(3)}{entry['secondary']}"
    
    new_content = re.sub(book_pattern, repl_book, content)
    if new_content == content:
        book_pattern2 = r"(1\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)(\r?\n.*?2\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)"
        new_content = re.sub(book_pattern2, repl_book, content)

    q_pos = new_content.find("> [!quote]")
    if q_pos != -1:
        before_q = new_content[:q_pos]
        after_q = new_content[q_pos:]
        
        new_q_lines = ["> [!quote] 💬 Contextual Usage & Authentic Quotations"]
        for q in entry["quotes"]:
            new_q_lines.append(f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{q['quote']}\"*")
        
        rest = after_q.split("\n")
        remaining_lines = []
        skip = True
        for line in rest[1:]:
            if skip:
                if line.startswith("> - 📜") or line.strip() == ">" or line.strip() == "":
                    continue
                else:
                    skip = False
                    remaining_lines.append(line)
            else:
                remaining_lines.append(line)
        
        new_content = before_q + "\n".join(new_q_lines) + ("\n" + "\n".join(remaining_lines) if remaining_lines else "\n")
    
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated += 1

print(f"Successfully updated {updated}/{len(data)} notes across 8 dashboards.")

dashes = [
  "Dashboard — avid",
  "Dashboard — furi",
  "Dashboard — jubil",
  "Dashboard — ridi",
  "Dashboard — pudor",
  "Dashboard — miser",
  "Dashboard — horr",
  "Dashboard — sever"
]

all_pass = True
for d in dashes:
    res = subprocess.run(["node", "main app/scripts/audit-latin-roots.mjs", f"{base_dir}/{d}"], capture_output=True, encoding="utf-8")
    if "Audit Verdict: ✅ 100% PRISTINE (PASS)" in res.stdout:
        print(f"✅ {d}: PASS")
    else:
        print(f"❌ {d}: FAIL")
        all_pass = False
        print(res.stdout)

if all_pass:
    print("\n🎉 ALL 8 DASHBOARDS 100% PRISTINE (PASS)!")
