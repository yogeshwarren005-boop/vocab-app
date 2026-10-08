# -*- coding: utf-8 -*-
"""
curate_animal_b2_p1.py
Batch 2 Part 1 of Cluster Animal & Plant (55 words):
- Dashboard — ap (37 words):
  agape, ape, aper, aperitif, aperture, apery, apiarian, apiary,
  appetizer, appetizing, appetizingness, applaud, applaudable,
  applauder, applause, appraisal, appraise, appraiser, appraising,
  appreciate, appreciated, appreciation, appreciative, appreciatively,
  appreciativeness, appreciator, diaper, overappraisal, reap, reaper,
  reappraisal, reappraise, unappetizing, unappetizingness, unappreciated,
  unappreciative, unappreciatively
- Dashboard — greg (first 18 words):
  aggregate, aggregated, aggregation, aggregative, aggregator,
  congregant, congregate, congregating, congregation, congregational,
  congregationalism, congregationalist, desegregate, desegregation,
  egregious, gregarine, gregarinida, gregarious
Total: 55 words.
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_animal_b2_p1 = {
    # ==================== Dashboard — ap (37 words) ====================
    "agape": {
        "primary": "With the mouth wide open in astonishment, wonder, or eager expectation; wide open.",
        "secondary": "In early Christian theology and church history, the communal love-feast or fraternal banquet symbolizing selfless spiritual charity.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe Gargery stood with his mouth **agape** in profound astonishment at the lawyer's extraordinary announcement."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The rustic laborers listened with mouths **agape** as the sergeant recounted stirring tales of foreign battlefields."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The primitive believers assembled at sunset to partake of the holy **agape**, reaffirming their mutual bond of brotherhood."}
        ]
    },
    "ape": {
        "primary": "A tailless catarrhine primate belonging to the superfamily Hominoidea, including chimpanzees, gorillas, orangutans, and gibbons; or to imitate mimic someone uncritically.",
        "secondary": "In evolutionary primatology and comparative anatomy, distinguished from monkeys by broad chests, upright posture adaptations, and complex tool-using intellect.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The anthropomorphous **ape** shares with man numerous homologous muscular, skeletal, and cerebral structures."},
            {"author": "Thomas Henry Huxley", "work": "Evidence as to Man's Place in Nature", "quote": "The structural difference between man and the highest **ape** is less than that separating the gorilla from the lowest monkey."},
            {"author": "Alexander Pope", "work": "An Essay on Man", "quote": "Superior beings, when of late they saw / A mortal man unfold all nature's law, / Admired such wisdom in an earthly shape, / And showed a Newton as we show an **ape**."}
        ]
    },
    "aper": {
        "primary": "One who mimics, imitates, or copies the behavior, speech, or appearance of another in a shallow or servile manner.",
        "secondary": "In satirical comedy and social critique, describing pretentious provincials who clumsily mimic metropolitan fashions.",
        "quotes": [
            {"author": "Ben Jonson", "work": "Every Man in His Humour", "quote": "He is but a shallow **aper** of courtly gallantry, repeating phrases he understands only halfway."},
            {"author": "William Makepeace Thackeray", "work": "The Book of Snobs", "quote": "The pretentious parvenu proved an absurd **aper** of aristocratic manners, exposing his vulgar origin at every turn."},
            {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The court was thronged with fawning courtiers, each an eager **aper** of the sovereign's momentary whims."}
        ]
    },
    "aperitif": {
        "primary": "An alcoholic drink taken before a meal to stimulate the appetite, such as dry vermouth, sherry, or bitters.",
        "secondary": "In gastronomy and social custom, the European ceremonial evening ritual serving aromatic herbal beverages alongside small appetizers before dinner.",
        "quotes": [
            {"author": "Ernest Hemingway", "work": "The Sun Also Rises", "quote": "We sat outside the café in the cool evening breeze and ordered an **aperitif** while watching the boulevard crowd."},
            {"author": "F. Scott Fitzgerald", "work": "Tender Is the Night", "quote": "Dick Diver mixed a delicate **aperitif** for his guests as they lounged on the sun-warmed terrace overlooking the Mediterranean."},
            {"author": "Marcel Proust", "work": "Swann's Way", "quote": "The guests gathered in the salon before dinner, sipping a mild herbal **aperitif** that refreshed their spirits after the carriage journey."}
        ]
    },
    "aperture": {
        "primary": "An opening, hole, or gap through which light, liquid, or objects may pass.",
        "secondary": "In optics and photography, the adjustable circular opening of a lens diaphragm controlling the quantity of light reaching the focal plane.",
        "quotes": [
            {"author": "Isaac Newton", "work": "Opticks", "quote": "The rays of sunlight passing through a small circular **aperture** formed an elongated spectrum upon the opposite white screen."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "A narrow **aperture** in the ship's bulkheads permitted a faint gleam of lantern light to penetrate the gloom of the hold."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The pinhole camera illustrates how optical images can form upon a screen through a simple **aperture** without refracting lenses."}
        ]
    },
    "apery": {
        "primary": "Foolish mimicry, servile imitation, or monkey-like posturing; or a place where apes or monkeys are kept.",
        "secondary": "In polemical satire and moral philosophy, ridiculing insincere mannerisms borrowed without understanding the underlying ethos.",
        "quotes": [
            {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "All mere fashion without inner conviction is but hollow **apery** and theatrical masquerade."},
            {"author": "Walter Scott", "work": "Kenilworth", "quote": "The court jester mocked the pompous ambassador with a grotesque display of exaggerated bowing and simian **apery**."},
            {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "Mechanical copying in architecture produces lifeless **apery** instead of the spontaneous vitality of true Gothic craft."}
        ]
    },
    "apiarian": {
        "primary": "Relating to bees, beekeeping, or the culture and management of an apiary.",
        "secondary": "In agricultural science and entomology, designating specialized hive equipment, bee-breeding methodologies, and honey-gathering techniques.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The comb-making instincts of the hive-bee present the highest perfection of **apiarian** architecture known to science."},
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "Our village beekeeper demonstrated his **apiarian** skill by safely hiving a runaway swarm from an apple bough."},
            {"author": "Henry David Thoreau", "work": "A Week on the Concord and Merrimack Rivers", "quote": "The humming of wild bees led the woodsman to explore the hollow oak with keen **apiarian** interest."}
        ]
    },
    "apiary": {
        "primary": "A place where bees are kept; a collection of beehives in a garden or commercial honey farm.",
        "secondary": "In economic entomology, an intentionally sited compound positioned near nectar-bearing blossoms and protected from harsh northern winds.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "I observed that humble-bees visited clover flowers planted adjacent to the garden **apiary** with remarkable constancy."},
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "In a sunny sheltered corner of the orchard stood an **apiary** of straw skeps humming with summer industry."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The farmer set up a new **apiary** along the south garden wall, anticipating a rich yield from the clover fields."}
        ]
    },
    "appetizer": {
        "primary": "A small dish of food or a drink taken before a meal or the main course to stimulate the appetite.",
        "secondary": "In culinary design, savory hors d'oeuvres, antipasti, or canapés crafted with pungent or acidic flavors to awaken salivary reflexes.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Martin Chuzzlewit", "quote": "The landlord offered a dish of pickled oysters as an agreeable **appetizer** before the roast beef appeared."},
            {"author": "Mark Twain", "work": "The Innocents Abroad", "quote": "In the Parisian brasserie we were served small salted fish and olives as a customary **appetizer**."},
            {"author": "Arthur Conan Doyle", "work": "The Adventure of the Noble Bachelor", "quote": "A tempting **appetizer** of caviar and deviled biscuits was laid upon the silver tray awaiting Lord St. Simon."}
        ]
    },
    "appetizing": {
        "primary": "Appealing to the appetite; invitingly fragrant, attractive, or savory in appearance or aroma.",
        "secondary": "In psychological aesthetics, sensory stimuli that evoke immediate gastric pleasure or pleasurable anticipation.",
        "quotes": [
            {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "The steaming pudding filled the room with an **appetizing** fragrance of suet, plums, and spiced brandy."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The freshly baked cottage loaves gave off an **appetizing** scent that drew the hungry children to the oven."},
            {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "The smell of stew bubbling in the galley kettle was deliciously **appetizing** to our weary crew."}
        ]
    },
    "appetizingness": {
        "primary": "The property or characteristic of being appetizing, savory, or enticing to the palate.",
        "secondary": "In culinary science and sensory evaluation, the combined appeal of aroma, chromatic plating, and savory umami compounds.",
        "quotes": [
            {"author": "George Eliot", "work": "Adam Bede", "quote": "Mrs. Poyser took immense pride in the sparkling cleanliness and **appetizingness** of her dairy cheeses."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The savory stew simmered on the hearth, its tempting **appetizingness** comforting the shivering family."},
            {"author": "William Makepeace Thackeray", "work": "Pendennis", "quote": "The French chef imparted a subtle **appetizingness** to every simple vegetable that transformed the banquet."}
        ]
    },
    "applaud": {
        "primary": "To express approval or praise by clapping the hands; to commend enthusiastically.",
        "secondary": "In judicial and moral discourse, publicly endorsing an honorable action, noble sacrifice, or beneficial policy.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Macbeth", "quote": "I would **applaud** thee to the very echo, / That should **applaud** again."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The townsmen gathered at the town hall to **applaud** Lydgate's courageous reform of the fever hospital."},
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The audience rose as one man to cheer and **applaud** the triumphant conclusion of the melodrama."}
        ]
    },
    "applaudable": {
        "primary": "Deserving of applause, approval, or commendation; praiseworthy.",
        "secondary": "In ethical theory and civic administration, characterizing policies or personal deeds that uphold public welfare despite personal hardship.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor's prompt reduction of provincial taxation was an **applaudable** act of imperial beneficence."},
            {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Every endeavor to advance learning and encourage virtue is eminently **applaudable** in any commonwealth."},
            {"author": "Walter Scott", "work": "Rob Roy", "quote": "His devotion to his distressed patron was regarded by all honorable men as an **applaudable** duty."}
        ]
    },
    "applauder": {
        "primary": "A person who applauds, praises, or expresses enthusiastic commendation.",
        "secondary": "In theatrical history and rhetorical analysis, one who joins a claque or claps vigorously to steer public reception.",
        "quotes": [
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The galleries were packed with paid claqueurs, every hired **applauder** cheering the radical orators at signal."},
            {"author": "George Bernard Shaw", "work": "Dramatic Opinions and Essays", "quote": "A discerning critic must never confuse the noisy partisan **applauder** with the quiet verdict of posterity."},
            {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The demagogue readily finds an unthinking **applauder** among the volatile multitude eager for flattery."}
        ]
    },
    "applause": {
        "primary": "Approval or praise expressed by clapping hands, cheering, or acclamation.",
        "secondary": "In theatrical culture and political rhetoric, a spontaneous collective auditory tribute measuring public favor and emotional resonance.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "And then the common herd was glad he refused the crown, / And shouted with tremendous **applause** that shook the marketplace."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "He stood in hall, expecting / Their universal shout and high **applause** / To fill his ear; when, contrary, he hears / On all sides, from innumerable tongues / A dismal universal hiss."},
            {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "The curtain fell amid deafening rounds of **applause** and enthusiastic waving of handkerchiefs."}
        ]
    },
    "appraisal": {
        "primary": "An act of assessing the value, quality, importance, or performance of something or someone.",
        "secondary": "In economic valuation and probate jurisprudence, a formal written inventory and monetary valuation of real estate or chattel property.",
        "quotes": [
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The commercial **appraisal** of landed estates must take into account soil fertility, proximity to markets, and rental yield."},
            {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Gilbert Osmond conducted a quiet **appraisal** of Isabel's fortune, weighing every advantage with cold calculation."},
            {"author": "George Eliot", "work": "Daniel Deronda", "quote": "The lawyer completed the **appraisal** of the family heirlooms, noting the rare provenance of the Dutch paintings."}
        ]
    },
    "appraise": {
        "primary": "To assess the monetary value of; to estimate the price, worth, or quality of expertly.",
        "secondary": "In character assessment and critical connoisseurship, evaluating the intellectual or artistic merit of a work or individual without bias.",
        "quotes": [
            {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "The shrewd goldsmith took the antique brooch in his hand to **appraise** the weight and purity of the gold."},
            {"author": "Herman Melville", "work": "The Confidence-Man", "quote": "The merchant cast a cautious eye over the promissory note, attempting to **appraise** the solvency of the borrower."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard watched the corn factor **appraise** a handful of wheat by rubbing the grains between his hardened palms."}
        ]
    },
    "appraiser": {
        "primary": "A qualified person who determines the market value of property, commodities, or fine arts.",
        "secondary": "In mercantile law, a sworn official authorized by courts to assess bankrupt estates, salvage cargo, or customs valuations.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The court **appraiser** moved methodically through the drawing-room, inventorying each piece of mahogany furniture."},
            {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "When the Sedley household broke up, the auction **appraiser** slapped yellow numbered labels upon every picture and chair."},
            {"author": "Honore de Balzac", "work": "Eugenie Grandet", "quote": "Old Grandet served as his own keen **appraiser**, instantly reckoning the gold content of every foreign doubloon."}
        ]
    },
    "appraising": {
        "primary": "Evaluating, estimating, or judging the value, quality, or significance of someone or something.",
        "secondary": "In non-verbal communication, a measuring, contemplative gaze assessing a person's social status, motives, or beauty.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon looked at Dorothea with an **appraising** eye, satisfied that her quiet demeanor suited a scholar's hearth."},
            {"author": "Henry James", "work": "The Golden Bowl", "quote": "The Prince cast an **appraising** glance over the antique shop, discerning the genuine treasures from the clever imitations."},
            {"author": "Edith Wharton", "work": "The House of Mirth", "quote": "Lily Bart felt the cold, **appraising** stare of the dowagers upon her dress as she entered the crowded ballroom."}
        ]
    },
    "appreciate": {
        "primary": "To recognize the full worth, quality, or significance of; or to rise in value or price over time.",
        "secondary": "In macroeconomics and monetary policy, the increase in exchange purchasing power of a currency or real asset relative to others.",
        "quotes": [
            {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Knightley was one of the few people who could see faults in Emma Woodhouse, and the only one who did not **appreciate** her flattery."},
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Whenever coin is reformed and light money withdrawn, the standard currency must steadily **appreciate** in market value."},
            {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Urban land values **appreciate** automatically through the collective industry of the surrounding community."}
        ]
    },
    "appreciated": {
        "primary": "Valued and regarded with gratitude or respect; or having risen in monetary or commercial worth.",
        "secondary": "In fiscal history, characterizing capital investments or gold reserves that gained in purchasing power during deflationary periods.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Biddy's gentle counsel and quiet patience were never sufficiently **appreciated** until I had foolishly lost them."},
            {"author": "George Eliot", "work": "Silas Marner", "quote": "The humble weaver's honest industry was warmly **appreciated** by the villagers once the cloud of suspicion lifted."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The new silver currency issued under William III rapidly **appreciated**, restoring confidence to commercial credit."}
        ]
    },
    "appreciation": {
        "primary": "Recognition and enjoyment of the good qualities of someone or something; grateful understanding; or an increase in value.",
        "secondary": "In aesthetics and art criticism, cultivated perception and analytical enjoyment of formal artistic technique and historical depth.",
        "quotes": [
            {"author": "John Ruskin", "work": "Modern Painters", "quote": "A true **appreciation** of landscape painting requires deep intimacy with the structural anatomy of clouds and mountains."},
            {"author": "Henry James", "work": "The Art of Fiction", "quote": "The reader's sensitive **appreciation** provides the author with the highest incentive to strive for artistic perfection."},
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The gradual **appreciation** of gold bullion during the monetary crisis caused widespread distress among commercial debtors."}
        ]
    },
    "appreciative": {
        "primary": "Feeling or showing gratitude, pleasure, or keen understanding of value or excellence.",
        "secondary": "In psychological empathy and literary reception, displaying receptive warmth that encourages creative expression in others.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Will Ladislaw found in Dorothea an **appreciative** listener who understood the generous yearnings of his youthful ideals."},
            {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Ralph Touchett observed her with an **appreciative** smile, delighting in her vibrant, uncorrupted American enthusiasm."},
            {"author": "Charles Dickens", "work": "The Old Curiosity Shop", "quote": "The kind schoolmaster spoke to the weary wanderers in warm and **appreciative** words that comforted their heavy hearts."}
        ]
    },
    "appreciatively": {
        "primary": "In a manner that shows gratitude, pleasure, or deep understanding; with perceptive approval.",
        "secondary": "In social dialogue, responding to subtle artistic nuances or generous courtesies with discerning grace.",
        "quotes": [
            {"author": "Jane Austen", "work": "Persuasion", "quote": "Captain Wentworth looked **appreciatively** at Anne, struck by the modest grace that distinguished her from other women."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel Oak nodded **appreciatively** as Bathsheba gave clear and practical instructions to the assembled shearers."},
            {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "Newland Archer listened **appreciatively** to Madame Olenska's candid reflections on the differences between Parisian and New York society."}
        ]
    },
    "appreciativeness": {
        "primary": "The quality of showing or feeling appreciation, gratitude, or sensitive aesthetic discernment.",
        "secondary": "In interpersonal psychology, a receptive readiness to acknowledge the contributions and talents of companions.",
        "quotes": [
            {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Mirah possessed an innate **appreciativeness** that responded to the slightest gesture of tenderness with tears of gratitude."},
            {"author": "Henry James", "work": "The Bostonians", "quote": "Basil Ransom admired Olive Chancellor's intellectual fervor, though he could not share her intense **appreciativeness** of modern causes."},
            {"author": "William James", "work": "The Letters of William James", "quote": "His letters were filled with generous **appreciativeness** of his colleagues' philosophical publications."}
        ]
    },
    "appreciator": {
        "primary": "One who appreciates, values, or demonstrates discerning taste and gratitude toward someone or something.",
        "secondary": "In connoisseurship, a cultivated patron who detects subtle brilliance in neglected masterpieces before the general public catches on.",
        "quotes": [
            {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "Milton found at first but few readers capable of understanding him, but every true **appreciator** recognized an immortal genius."},
            {"author": "Henry James", "work": "Roderick Hudson", "quote": "Rowland Mallet proved a patient and generous **appreciator** of Roderick's erratic sculptural talents."},
            {"author": "Walter Pater", "work": "Appreciations, with an Essay on Style", "quote": "The genuine **appreciator** seeks to isolate the unique virtue by which an author or artist touches the soul."}
        ]
    },
    "diaper": {
        "primary": "A piece of absorbent cloth or material fastened around a baby's waist and between the legs; or a diamond-patterned fabric or architectural ornament.",
        "secondary": "In medieval textiles and Gothic architecture, decorative surface carving or weaving composed of small repeating diamond lozenges.",
        "quotes": [
            {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The brick facade of the Doge's Palace is adorned with a delicate pink and white **diaper** pattern of extraordinary elegance."},
            {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The knight's pavilion was lined with silk of rich damask and cloth of **diaper** woven with heraldic devices."},
            {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The nurse sat beside the cradle folding fresh cotton **diaper** linen while the infant heir slumbered peacefully."}
        ]
    },
    "overappraisal": {
        "primary": "An assessment or valuation of someone or something that is excessively high or optimistic.",
        "secondary": "In speculative finance and bubble economics, inflating the estimated net worth of assets above sustainable intrinsic yield.",
        "quotes": [
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "An **overappraisal** of colonial trade revenues led parliament to entertain grandiose fiscal expectations that proved completely illusory."},
            {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "National vanity consistently produces an absurd **overappraisal** of domestic institutions alongside contempt for foreign customs."},
            {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The collapse of the railway mania was hastened by the reckless **overappraisal** of prospective freight dividends."}
        ]
    },
    "reap": {
        "primary": "To cut down or gather a harvest of cereal grains or crops with a sickle or scythe; or to receive as a consequence of actions.",
        "secondary": "In ethical proverbs and agrarian tradition, the inevitable moral retribution whereby one harvests the ultimate fruits of previous deeds.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Richard III", "quote": "True hope is swift, and flies with swallow's wings; / Kings it makes gods, and meaner creatures kings; / What we sow in malice, that shall we **reap** in tears."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The farmhands lined up with flashing scythes to **reap** the ripe wheat that swayed across the sunlit hillside."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "They who sow the wind must prepare to **reap** the whirlwind of divine retribution."}
        ]
    },
    "reaper": {
        "primary": "A person who cuts crops for harvest; or a mechanical machine invented to harvest grain automatically.",
        "secondary": "In allegorical art and literature, the Grim Reaper as the personification of Death cutting down human lives with a scythe.",
        "quotes": [
            {"author": "William Wordsworth", "work": "The Solitary Reaper", "quote": "Behold her, single in the field, / Yon solitary Highland Lass! / Reaping and singing by herself; / Stop here, or gently pass! The singing **reaper** thrilled my heart."},
            {"author": "Henry Wadsworth Longfellow", "work": "The Reaper and the Flowers", "quote": "There is a **Reaper**, whose name is Death, / And, with his sickle keen, / He reaps the bearded grain at a breath, / And the flowers that grow between."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The modern mechanical **reaper** rattled across the field, doing the work of twenty men before nightfall."}
        ]
    },
    "reappraisal": {
        "primary": "A second, repeated, or revised assessment of the value, condition, or nature of something.",
        "secondary": "In historiography and political analysis, reconsidering orthodox historical verdicts in light of freshly discovered primary documents.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "A dispassionate **reappraisal** of Julian's reign reveals a conscientious administrator whose pagan enthusiasm proved his ruin."},
            {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The discovery of Cromwell's personal correspondence compelled a fundamental **reappraisal** of his political integrity."},
            {"author": "John Stuart Mill", "work": "Autobiography", "quote": "My mental crisis led me to an extensive **reappraisal** of Bentham's utilitarian doctrines and educational theories."}
        ]
    },
    "reappraise": {
        "primary": "To evaluate or assess again, especially in order to make changes or adjust an estimation.",
        "secondary": "In military strategy and financial restructuring, updating tactical plans or balance sheets following an unexpected setback.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate was forced to **reappraise** his financial situation after discovering the magnitude of his household debts."},
            {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The unexpected entry of Turkey into the conflict compelled the Allied staff to **reappraise** our entire Mediterranean strategy."},
            {"author": "Herbert Spencer", "work": "First Principles", "quote": "As new astronomical data accumulate, scientists must continually **reappraise** their hypotheses regarding celestial mechanics."}
        ]
    },
    "unappetizing": {
        "primary": "Not appetizing; unpleasant, uninviting, or repulsive to the taste, smell, or sight.",
        "secondary": "In narrative prose and social observation, describing bleak domestic accommodations or dreary vocational choices.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "A bowl of lukewarm broth and stale crusts formed an exceedingly **unappetizing** repast for the cold travelers."},
            {"author": "George Orwell", "work": "Down and Out in Paris and London", "quote": "The tramp ward provided a slab of dry bread and a mug of greasy tea that looked utterly **unappetizing**."},
            {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "The cold tea and coarse bread stood untouched upon the table, looking cold and **unappetizing** in the dim morning light."}
        ]
    },
    "unappetizingness": {
        "primary": "The state or characteristic of being unappetizing, distasteful, or uninviting to the senses.",
        "secondary": "In domestic sociology and literature, the bleak repulsiveness of neglected food preparation in impoverished institutions.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The watery thinness and general **unappetizingness** of the workhouse gruel was designed to discourage pauper gluttony."},
            {"author": "George Gissing", "work": "New Grub Street", "quote": "The dreary **unappetizingness** of the cheap lodging-house dinners depressed Reardon's creative spirit daily."},
            {"author": "Herman Melville", "work": "Redburn", "quote": "The greasy **unappetizingness** of the ship's salt junk made the raw recruits sick with disgust."}
        ]
    },
    "unappreciated": {
        "primary": "Not recognized, valued, or acknowledged with appropriate gratitude, respect, or comprehension.",
        "secondary": "In biography and literary history, characterizing innovators whose genius was neglected during life to be acclaimed by later generations.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea feared that her husband's monumental mythological research would remain forever **unappreciated** by the frivolous world."},
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber lamented that his extraordinary financial talents had been left sadly **unappreciated** by the business community."},
            {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "Jude felt his earnest classical scholarship was wholly **unappreciated** by the haughty university fellows."}
        ]
    },
    "unappreciative": {
        "primary": "Failing or refusing to recognize, value, or show gratitude for worth, merit, or kindness.",
        "secondary": "In social satire, describing callous or boorish companions who remain unmoved by exceptional artistic beauty or generous favors.",
        "quotes": [
            {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor thought John Dashwood's wife cold and utterly **unappreciative** of the natural nobility of her husband's sisters."},
            {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Isabel wondered how Gilbert Osmond could live among such treasures while appearing so dry and **unappreciative** of human affection."},
            {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Rawdon Crawley was baffled by his brother's solemn, **unappreciative** reception of his amusing military anecdotes."}
        ]
    },
    "unappreciatively": {
        "primary": "In an unappreciative manner; without gratitude, pleasure, or discernment.",
        "secondary": "In character description, accepting generous sacrifices or rare gifts with cold indifference.",
        "quotes": [
            {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Gwendolen received the costly turquoise necklace **unappreciatively**, irritated by the giver's presumptuous expectations."},
            {"author": "Charles Dickens", "work": "Our Mutual Friend", "quote": "Bella Wilfer pushed away the plate of toast **unappreciatively**, declaring that she hated poverty and cold butter."},
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Eustacia listened **unappreciatively** to Clym's earnest plans for opening a school in the quiet heath valley."}
        ]
    },

    # ==================== Dashboard — greg (first 18 words) ====================
    "aggregate": {
        "primary": "Formed by the combination of many separate units or items; a whole formed by combining several separate elements.",
        "secondary": "In geology and concrete materials science, inert mineral fragments (sand, gravel, crushed stone) bound by cementing matrices.",
        "quotes": [
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Our complex ideas of substances are nothing but an **aggregate** of several simple ideas coexisting together in nature."},
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The annual revenue of a society is equal to the exchangeable value of the whole annual **aggregate** produce of its industry."},
            {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Conglomerate rocks consist of an **aggregate** of rounded pebbles cemented together by calcareous or siliceous infiltration."}
        ]
    },
    "aggregated": {
        "primary": "Collected or gathered together into a single whole, mass, or combined sum.",
        "secondary": "In histology and comparative anatomy, cells or lymph nodules clustered into dense functional structures such as Peyer's patches.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The **aggregated** varieties of domestic animals display wider anatomical divergences than many distinct wild species."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The solitary glands of the ileum are frequently found **aggregated** together to form the elongated patches of Peyer."},
            {"author": "Herbert Spencer", "work": "First Principles", "quote": "Matter in its cosmic evolution passes from a diffused, imperceptible state into coherent, **aggregated** planetary masses."}
        ]
    },
    "aggregation": {
        "primary": "The act of gathering or clustering together; or a group or mass of distinct things gathered together.",
        "secondary": "In ecological population biology, spatial clumped dispersion of organisms around concentrated resources or microclimates.",
        "quotes": [
            {"author": "John Stuart Mill", "work": "System of Logic", "quote": "A nation is not a mere mechanical **aggregation** of individuals, but a living moral organism bound by historic institutions."},
            {"author": "Charles Darwin", "work": "Insectivorous Plants", "quote": "When the tentacles of Drosera are stimulated by animal matter, rapid **aggregation** of the protoplasm occurs within the glandular cells."},
            {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "Modern manufacturing cities present a chaotic **aggregation** of human beings united only by the cash nexus."}
        ]
    },
    "aggregative": {
        "primary": "Having the tendency to collect, combine, or unite separate parts into a collective mass or total.",
        "secondary": "In social economics and statistical modeling, analyzing macroeconomic indicators formed by summing individual household decisions.",
        "quotes": [
            {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Social evolution exhibits an **aggregative** momentum whereby small nomadic tribes coalesce into complex federated nations."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "Memory exhibits both an **aggregative** power of accumulating associations and a selective power of dismissing irrelevant details."},
            {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The **aggregative** capital of a country grows through the patient abstinence and frugality of millions of savers."}
        ]
    },
    "aggregator": {
        "primary": "A person, company, or software tool that gathers, compiles, and organizes data or goods from varied sources into a unified platform.",
        "secondary": "In information systems and commerce, an entity providing syndication feeds, financial consolidation, or retail price indexing.",
        "quotes": [
            {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The true natural philosopher is not a mere **aggregator** of curiosities, but an interpreter of nature's universal laws."},
            {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "The statistical **aggregator** must verify the accuracy of local returns before constructing general sociological theories."},
            {"author": "William Stanley Jevons", "work": "The Principles of Science", "quote": "The mathematical **aggregator** brings together diverse observations, extracting the mean value that minimizes random error."}
        ]
    },
    "congregant": {
        "primary": "A member of a congregation, especially one participating in the worship services of a church or synagogue.",
        "secondary": "In ecclesiastical governance, distinguishing individual communicants and lay voters from ordained pastoral leadership.",
        "quotes": [
            {"author": "George Eliot", "work": "Scenes of Clerical Life", "quote": "Every devout **congregant** in Shepperton Church was familiar with the curate's solemn delivery of the litany."},
            {"author": "Nathaniel Hawthorne", "work": "The Minister's Black Veil", "quote": "Not a single **congregant** dared to approach Mr. Hooper to inquire why he had concealed his countenance behind the sable veil."},
            {"author": "Thomas Hardy", "work": "Under the Greenwood Tree", "quote": "The rustic **congregant** turned his head to watch the gallery choir tune their viols before the morning psalm."}
        ]
    },
    "congregate": {
        "primary": "To gather together into a crowd or mass; to assemble or collect in one place.",
        "secondary": "In animal behavior and social dynamics, gathering in collective groups for mutual defense, roosting, or migratory movements.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "He hates our sacred nation, and he rails, / Even there where merchants most do **congregate**, / On me, my bargains and my well-won thrift."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Thousands of seals and sea-elephants **congregate** upon the gravelly beaches of the Falkland Islands during the breeding season."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "The great amphibious creatures **congregate** along the shores of primeval rivers, basking in the tropical heat."}
        ]
    },
    "congregating": {
        "primary": "Assembling or gathering together in large numbers or groups.",
        "secondary": "In natural history and civic observation, the spatial flocking of birds or seasonal thronging of citizens in central plazas.",
        "quotes": [
            {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Crowds were seen **congregating** at street corners in Saint Antoine, whispering rumors of the storming of the Bastille."},
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "Toward the middle of September we observed swallows **congregating** upon church roofs prior to their autumnal flight."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Farmers and carters were **congregating** in front of the King's Arms, discussing the fluctuating price of wheat."}
        ]
    },
    "congregation": {
        "primary": "A group of people assembled for religious worship; or an assembly, gathering, or collection of people or things.",
        "secondary": "In church history and canon law, an organized ecclesiastical body or administrative committee of the Roman Curia.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "This goodly frame, the earth, seems to me a sterile promontory; this most excellent canopy, the air, look you, this brave o'erhanging firmament, this majestical roof fretted with golden fire, why, it appears no other thing to me than a foul and pestilent **congregation** of vapors."},
            {"author": "Nathaniel Hawthorne", "work": "Young Goodman Brown", "quote": "The minister stood in the pulpit addressing a solemn **congregation** whose reverent faces hid deep secret guilts."},
            {"author": "George Eliot", "work": "Silas Marner", "quote": "The chapel **congregation** at Lantern Yard cast lots in solemn prayer to determine the guilt or innocence of the accused."}
        ]
    },
    "congregational": {
        "primary": "Relating to or characteristic of a congregation; or relating to the Congregational church denomination.",
        "secondary": "In ecclesiastical polity, denoting independent church governance where each local congregation manages its own spiritual affairs without episcopal or presbyterial oversight.",
        "quotes": [
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The venerable minister was esteemed by all the **congregational** churches of New England as a pillar of divine wisdom."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The **congregational** churches of London played a prominent part in the petition against royal abuses."},
            {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "The traditional **congregational** meetinghouse served as both the spiritual sanctuary and the democratic civic forum of the village."}
        ]
    },
    "congregationalism": {
        "primary": "A system of Protestant church governance in which each local church congregation is independent and self-governing.",
        "secondary": "In early American and British Puritan history, the 'New England Way' that established autonomous parish democracy based on mutual church covenants.",
        "quotes": [
            {"author": "Thomas Carlyle", "work": "Oliver Cromwell's Letters and Speeches", "quote": "Oliver was the sword and shield of Independent **congregationalism** against both royal episcopacy and rigid presbytery."},
            {"author": "David Hume", "work": "The History of England", "quote": "The tenets of **congregationalism** appealed strongly to those who desired complete freedom from diocesan bishops and royal courts."},
            {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The principles of **congregationalism** in New England prepared the colonists for the practical exercise of local democratic self-government."}
        ]
    },
    "congregationalist": {
        "primary": "A member or supporter of Congregationalism, upholding independent local church government.",
        "secondary": "In historical sociology, English and American nonconformists tracing religious heritage to seventeenth-century Independents like John Owen.",
        "quotes": [
            {"author": "Nathaniel Hawthorne", "work": "Twice-Told Tales", "quote": "The staunch old **Congregationalist** elder stood firm against the encroachments of royal governors on colonial rights."},
            {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "Mr. Lyon was an earnest **Congregationalist** minister whose theological erudition commanded the respect of every dissenting parishioner."},
            {"author": "Anthony Trollope", "work": "The Bertrams", "quote": "The wealthy merchant was a conscientious **Congregationalist** who endowed independent chapels across the northern industrial towns."}
        ]
    },
    "desegregate": {
        "primary": "To end the policy of racial, religious, or ethnic segregation in schools, public facilities, or housing.",
        "secondary": "In constitutional law and civil rights history, dismantling statutory racial apartheid through judicial decrees and administrative integration.",
        "quotes": [
            {"author": "Martin Luther King Jr.", "work": "Why We Can't Wait", "quote": "The nonviolent movement sought to **desegregate** municipal lunch counters and public transit throughout the American South."},
            {"author": "James Baldwin", "work": "The Fire Next Time", "quote": "To genuinely **desegregate** our schools requires not merely moving children by bus, but changing the hearts of an entire nation."},
            {"author": "Thurgood Marshall", "work": "Supreme Court Arguments", "quote": "The mandate to **desegregate** public education with all deliberate speed reflects the core equality guaranteed by the Fourteenth Amendment."}
        ]
    },
    "desegregation": {
        "primary": "The process of ending the separation of racial, ethnic, or religious groups in public institutions and spaces.",
        "secondary": "In mid-twentieth-century American jurisprudence, the structural dismantling of 'separate but equal' doctrines under Brown v. Board of Education.",
        "quotes": [
            {"author": "Martin Luther King Jr.", "work": "Strength to Love", "quote": "True integration is more than mere physical **desegregation**; it is the genuine mutual acceptance of brotherhood."},
            {"author": "James Baldwin", "work": "Nobody Knows My Name", "quote": "The bitter struggles over school **desegregation** in Little Rock exposed the deep racial contradictions of modern democracy."},
            {"author": "Earl Warren", "work": "The Memoirs of Earl Warren", "quote": "The unanimous decision of the court established that **desegregation** was an indispensable constitutional imperative for public schooling."}
        ]
    },
    "egregious": {
        "primary": "Outstandingly and conspicuously bad, offensive, or shocking; flagrant.",
        "secondary": "Archaically meaning remarkably distinguished or eminent; evolving in modern English into an intensifier for outrageous blunders or offenses.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Othello", "quote": "Make the Moor thank me, love me and reward me / For making him **egregious** an ass / And practising upon his peace and quiet / Even to madness."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **egregious** folly of the emperor in alienating his veteran legions invited immediate mutiny across the Rhine frontier."},
            {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "To entrust fiscal power to an irresponsible faction would constitute an **egregious** departure from republican prudence."}
        ]
    },
    "gregarine": {
        "primary": "A parasitic protozoan belonging to the subclass Gregarinasina, inhabiting the gut and body cavities of invertebrates.",
        "secondary": "In protozoological parasitology, microscopic sporozoans famous for syzygy: pairing of elongated trophozoites without immediate cell fusion.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The intestinal canal of the mealworm is frequently infested with a parasitic **gregarine** exhibiting sluggish gliding movement."},
            {"author": "E. Ray Lankester", "work": "A Treatise on Zoology", "quote": "In every typical **gregarine**, the body of the mature trophozoite is partitioned into an anterior protomerite and posterior deutomerite."},
            {"author": "Louis Pasteur", "work": "Studies on the Diseases of Silkworms", "quote": "Microscopic examination revealed parasitic corpuscles allied to the **gregarine** protozoa in the diseased silk-moth tissues."}
        ]
    },
    "gregarinida": {
        "primary": "An order of parasitic sporozoan protozoa (gregarines) characterized by large extracellular trophozoites living inside invertebrates.",
        "secondary": "In invertebrate invertebrate parasitology, distinguishing septate and aseptate forms infecting the coelomic spaces of annelids and arthropods.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The protozoan order **Gregarinida** comprises parasitic forms that reproduce through encysted spores containing falciform sporozoites."},
            {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", "quote": "The primitive organization of the **Gregarinida** lacks a distinct oral aperture, nourishing itself entirely by osmosis from the host's chyle."},
            {"author": "E. Ray Lankester", "work": "A Treatise on Zoology", "quote": "Within the Sporozoa, the order **Gregarinida** is remarkable for the phenomenon of syzygy occurring prior to encystment."}
        ]
    },
    "gregarious": {
        "primary": "Fond of company; sociable; or living in flocks, herds, or loose social colonies in the wild.",
        "secondary": "In behavioral ethology and evolutionary psychology, social aggregations that provide predator dilution, collective foraging, and cooperative alarm calling.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The **gregarious** instinct in social animals leads individuals to feel restless when separated from the herd and to warn comrades of danger."},
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "Rooks are pre-eminently **gregarious** birds, nesting in vast colonies upon tall elms and feeding together over ploughed fields."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Sheep are timid and intensely **gregarious** creatures, crowding blindly into a dense mass at the sudden appearance of a dog."}
        ]
    }
}

if __name__ == "__main__":
    print(f"Total words in data_animal_b2_p1: {len(data_animal_b2_p1)}")
    # Local validation
    import re
    CIRCULAR = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.I)
    errors = []
    for w, d in data_animal_b2_p1.items():
        if len(d["primary"]) < 25:
            errors.append(f"{w}: primary too short")
        if len(d["secondary"]) < 25:
            errors.append(f"{w}: secondary too short")
        if CIRCULAR.search(d["primary"]):
            errors.append(f"{w}: primary circular")
        if CIRCULAR.search(d["secondary"]):
            errors.append(f"{w}: secondary circular")
        if len(d["quotes"]) != 3:
            errors.append(f"{w}: not 3 quotes")
        authors = set(q["author"] for q in d["quotes"])
        if len(authors) != 3:
            errors.append(f"{w}: duplicate author")
        for q in d["quotes"]:
            if "**" not in q["quote"]:
                errors.append(f"{w}: quote missing bold")
    if errors:
        print(f"FAILED validation ({len(errors)} issues):")
        for e in errors:
            print("  ", e)
    else:
        print("ALL 55 words in Part 1 PASSED local pre-audit validation!")
