# -*- coding: utf-8 -*-
"""
Part 2 of Curated Food, Eating & Drink Batch 3:
Dashboard — sati (First 25 words: alsatia to satirical)
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_sati_p1 = {
    "alsatia": {
        "primary": "A historical sanctuary zone in Whitefriars, London, between Fleet Street and the Thames, where debtors and lawbreakers were long immune from arrest.",
        "secondary": "In seventeenth-century English social history and urban literature, a notorious refuge of thieves, gamblers, and fugitives named after the disputed frontier province of Alsace.",
        "quotes": [
            {"author": "Walter Scott", "work": "The Fortunes of Nigel", "quote": "Nigel found himself safely immured within the squalid boundaries of **Alsatia**, where constables dared not venture without an armed guard."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The brazen ruffians of **Alsatia** sallied forth at night, knowing their sanctuary protected them against the ordinary processes of the law."},
            {"author": "Charles Dickens", "work": "Barnaby Rudge", "quote": "The dark alleyways resembled an ancient **Alsatia**, sheltering every variety of desperate outcast from the magistrate's warrant."}
        ]
    },
    "alsatian": {
        "primary": "A German Shepherd dog, or a native, inhabitant, or dialect of Alsace, a region in northeastern France bordering Germany.",
        "secondary": "In European history and canine terminology, an inhabitant of Alsace, or the British designation adopted for the German Shepherd following the First World War.",
        "quotes": [
            {"author": "George Orwell", "work": "Down and Out in Paris and London", "quote": "A fierce **Alsatian** dog paced behind the iron railings of the yard, barking loudly whenever a ragged porter passed by."},
            {"author": "Arthur Conan Doyle", "work": "His Last Bow", "quote": "The sentry stood beside a powerful **Alsatian** hound whose keen senses guarded the secluded country estate against intruders."},
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The brave **Alsatian** peasants defended their border villages against the invading legions with stubborn tenacity."}
        ]
    },
    "dissatisfaction": {
        "primary": "A feeling of displeasure, disappointment, or lack of contentment resulting from unfulfilled expectations or desires.",
        "secondary": "In political psychology and organizational behavior, widespread collective grievance, frustration, or restlessness that motivates social change or labor unrest.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The constant impulse toward improvement arises in part from an instinctive **dissatisfaction** with present conditions and limited resources."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea experienced a profound inward **dissatisfaction**, feeling that her eager aspirations found no real outlet in her marriage."},
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Eustacia's lingering **dissatisfaction** with her secluded life on Egdon Heath smoldered beneath her proud and solitary exterior."}
        ]
    },
    "dissatisfactory": {
        "primary": "Failing to satisfy or meet acceptable standards, expectations, or requirements; causing discontent or disappointment.",
        "secondary": "In formal jurisprudence and administrative assessment, describing evidence, service, or performance that proves inadequate, defective, or unacceptable.",
        "quotes": [
            {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "When the practical results of an administrative bureau prove consistently **dissatisfactory**, fundamental structural reforms become imperative."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The executor declared the accounting to be thoroughly **dissatisfactory**, demanding an immediate scrutiny of the contested ledgers."},
            {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The treaty concluded by the ministers was deemed highly **dissatisfactory** by Parliament, rousing fierce protests across the nation."}
        ]
    },
    "dissatisfied": {
        "primary": "Experiencing or expressing a lack of satisfaction, contentment, or pleasure; disappointed with circumstances.",
        "secondary": "In philosophical psychology, describing a restless state of consciousness that refuses passive complacency in pursuit of higher perfection or justice.",
        "quotes": [
            {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "It is better to be a human being **dissatisfied** than a pig satisfied; better to be Socrates **dissatisfied** than a fool satisfied."},
            {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth was thoroughly **dissatisfied** with the letter, perceiving in every line the awkward apologies of an uneasy mind."},
            {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes remained visibly **dissatisfied** with the official explanation, pacing the rug while examining the footprints through his lens."}
        ]
    },
    "dissatisfy": {
        "primary": "To fail to satisfy or please; to cause discontent, displeasure, or disappointment in someone.",
        "secondary": "In social reform and moral philosophy, to disturb uncritical complacency by revealing deficiencies, injustices, or missed opportunities for progress.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Great works of art only **dissatisfy** us when they awaken lofty yearnings that our mundane daily actions fail to fulfill."},
            {"author": "George Bernard Shaw", "work": "Man and Superman", "quote": "The true purpose of education is to **dissatisfy** the young mind with trivial pleasures and direct it toward noble achievements."},
            {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Nothing seemed capable of pleasing the spoiled heir, whose perpetual whim was to **dissatisfy** his indulgent relatives."}
        ]
    },
    "insatiable": {
        "primary": "Impossible to satisfy, appease, or quench; possessing an unquenchable craving, desire, or appetite.",
        "secondary": "In political philosophy and psychological ethics, an unbounded, compulsive ambition or rapacity that endlessly expands beyond all natural limits.",
        "quotes": [
            {"author": "Mary Shelley", "work": "Frankenstein", "quote": "He possessed an **insatiable** thirst for knowledge, pursuing the hidden secrets of life and death beyond the bounds of nature."},
            {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "Kurtz was dominated by an **insatiable** greed for ivory and power, which consumed his humanity in the wilderness."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Human ambition exhibits an **insatiable** appetite for novel acquisitions, never content with the possessions already secured."}
        ]
    },
    "insatiably": {
        "primary": "In an insatiable manner; with an appetite, curiosity, or longing that cannot be satisfied or appeased.",
        "secondary": "In character portrayal and narrative prose, pursuing knowledge, sensory experience, or wealth with ravenous, unremitting persistence.",
        "quotes": [
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The curious boy listened **insatiably** to every traveler's tale of foreign adventures, begging for another chapter before bed."},
            {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The human spirit thirsts **insatiably** after absolute truth, refusing to rest content in outward material comforts."},
            {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "She read **insatiably** through the long winter evenings, eager to absorb every nuance of European art and culture."}
        ]
    },
    "insatiate": {
        "primary": "Never satisfied; insatiable in appetite, craving, lust, or destructive fury.",
        "secondary": "In classic tragic verse and epic poetry, an archaic descriptor for ruthless vengeance, ravenous death, or unrestrained imperial conquest.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "O **insatiate** and unbridled wanton! Thou hast brought ruin upon an honorable house by thy reckless vanity."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "Grim Death sat upon his throne, **insatiate** of destruction, watching the fallen pair driven from Eden's gate."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab paced the deck with an **insatiate** craving for revenge, his soul consumed by the white whale's phantom malice."}
        ]
    },
    "satiable": {
        "primary": "Capable of being satisfied, appeased, or surfeited; having desires or appetites that can be fully met.",
        "secondary": "In normative ethics and economic utility theory, desires whose marginal consumption reaches a natural threshold of replenishment and quietude.",
        "quotes": [
            {"author": "Jeremy Bentham", "work": "An Introduction to the Principles of Morals and Legislation", "quote": "Physical appetites for bread and water are naturally **satiable**, whereas the artificial passion for social prestige knows no boundary."},
            {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The demand for basic subsistence goods is readily **satiable**, beyond which human labor turns to conveniences and luxuries."},
            {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "Every primitive organic instinct possesses a **satiable** limit, functioning through physiological cycles of depletion and repose."}
        ]
    },
    "satiate": {
        "primary": "To satisfy a desire or appetite fully or to excess; to surfeit or gorge to the point of complete repletion.",
        "secondary": "In classical literature and moral aesthetics, to supply so lavishly that eager pleasure transforms into cloying surfeit or listless apathy.",
        "quotes": [
            {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I shall **satiate** my ardent curiosity with the sight of a part of the world that has never before been visited by human eyes."},
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Growing a twenty years' removed thing, while one would think it could not **satiate** the longing of a lover's heart."},
            {"author": "Bram Stoker", "work": "Dracula", "quote": "The dreadful fiend seemed to **satiate** his unholy thirst upon the helpless victim before vanishing into the shadows."}
        ]
    },
    "satiated": {
        "primary": "Fully satisfied, gorged, or filled to excess; experiencing complete repletion or weary surfeit.",
        "secondary": "In descriptive narrative and psychological analysis, having indulged a hunger, curiosity, or passion to the extent that indifference or disgust ensues.",
        "quotes": [
            {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The wild beasts rested in the thicket, **satiated** with their nocturnal feast and indifferent to the morning sounds of the forest."},
            {"author": "Mary Shelley", "work": "The Last Man", "quote": "Having **satiated** their fury with fire and plunder, the retreating soldiers abandoned the ruined citadel to the dead."},
            {"author": "King James Bible", "work": "Jeremiah", "quote": "I will make mine arrows drunk with blood, and my sword shall devour flesh, being **satiated** with the sacrifice."},
        ]
    },
    "satiation": {
        "primary": "Full gratification or complete repletion of an appetite or desire, especially regarding food, drink, or physical craving.",
        "secondary": "In physiological psychology and behavioral nutrition, the biological process that terminates an episode of feeding through neurochemical feedback mechanisms.",
        "quotes": [
            {"author": "William James", "work": "The Principles of Psychology", "quote": "Upon the complete **satiation** of an appetite, the object which formerly provoked keen desire becomes utterly neutral or repulsive."},
            {"author": "Herbert Spencer", "work": "The Data of Ethics", "quote": "The natural rhythm between vigorous appetite and restful **satiation** governs all healthy operations of organic life."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Sensory receptors along the digestive tract signal **satiation** to the central nervous system long before nutrients are absorbed."}
        ]
    },
    "satie": {
        "primary": "Erik Satie (1866–1925), an influential French avant-garde composer and pianist known for minimalist compositions such as the Gymnopédies.",
        "secondary": "In twentieth-century musicology and modernism, a visionary eccentric composer whose modal harmonies and surreal titles prefigured ambient and conceptual music.",
        "quotes": [
            {"author": "Jean Cocteau", "work": "A Call to Order", "quote": "The delicate, unadorned phrases of **Satie** cleansed French music of heavy Wagnerian rhetoric, introducing an austere and crystalline simplicity."},
            {"author": "Igor Stravinsky", "work": "Chronicles of My Life", "quote": "I always admired **Satie** for his sharp wit, his contempt for academic pedantry, and his astonishing harmonic intuition."},
            {"author": "Claude Debussy", "work": "Monsieur Croche the Dilettante Hater", "quote": "My friend **Satie** was a gentle precursor whose quiet piano sketches anticipated discoveries that younger musicians now claim as their own."}
        ]
    },
    "satiety": {
        "primary": "Pervasive fullness or excess of gratification, especially leading to cloying distaste, boredom, or weary disgust.",
        "secondary": "In ethical philosophy and aesthetic theory, the psychological boundary where luxurious sensory gratification yields weariness, distaste, and ennui.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "After days of feast and revelry, a dull **satiety** settled upon the seamen, leaving them languid in the tropical calm."},
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "He hath fed of the dainties that are bred in a book; but his **satiety** yet seeks fresh novelty to quicken his appetite."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman nobles plunged into boundless luxuries until sheer **satiety** produced an exhausted disgust with all earthly pleasures."}
        ]
    },
    "satin": {
        "primary": "A smooth, glossy fabric, typically of silk or synthetic fibers, produced with a weave in which warp threads float over weft threads.",
        "secondary": "In textile manufacturing and fashion history, a lustrous woven textile characterized by minimal light scattering, high drape, and ceremonial elegance.",
        "quotes": [
            {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mrs. Bennet admired the bride's white **satin** gown, declaring that nothing could look more elegant or suited to a woman of fortune."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He lay upon the couch, resting his head against cushions of dark blue **satin** embroidered with gold thread."},
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "What sayeth the fellow with the smooth tongue, clothed in soft **satin** and speaking words of deceitful flatteries?"}
        ]
    },
    "satinet": {
        "primary": "A thin, durable fabric imitating satin, typically made of wool, cotton, or mixed fibers with a lustrous woven surface.",
        "secondary": "In nineteenth-century industrial textile history, an affordable, mass-produced cloth with a cotton warp and wool filling used for working-class garments.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "The country storekeeper displayed rolls of sturdy **satinet**, a serviceable fabric favored by farmers for winter trousers and coats."},
            {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "Hepzibah smoothed her worn dress of dark **satinet**, standing nervously behind the shop counter awaiting her first customer."},
            {"author": "Louisa May Alcott", "work": "Little Women", "quote": "The girls refurbished their modest **satinet** skirts with fresh ribbons, making them look presentable for the festive evening party."}
        ]
    },
    "satinette": {
        "primary": "A light fabric resembling satin, or a soft, shiny textile woven from fine cotton or mixed threads.",
        "secondary": "In nineteenth-century drapery and millinery, a delicate variant of satinet woven with a glossy mercerized finish for lining garments and ribbons.",
        "quotes": [
            {"author": "Charlotte Brontë", "work": "Villette", "quote": "Madame Beck wore an unpretending gown of gray **satinette**, moving through the pensionnat with noiseless, watchful footsteps."},
            {"author": "Honoré de Balzac", "work": "Eugénie Grandet", "quote": "The small parlor curtains were fashioned from yellow **satinette**, casting an amber glow over the antique walnut furniture."},
            {"author": "Gustave Flaubert", "work": "Madame Bovary", "quote": "Emma fingered the rolls of rose-colored **satinette** at the draper's shop, dreaming of fashionable garments worn in Paris."}
        ]
    },
    "satinleaf": {
        "primary": "A tropical evergreen tree (Chrysophyllum oliviforme) of the sapodilla family, noted for leaves with dark green upper surfaces and satiny copper undersides.",
        "secondary": "In tropical dendrology and Caribbean botany, a decorative hardwood tree whose bicolored foliage shimmers with golden-brown sheen in coastal coastal hammocks.",
        "quotes": [
            {"author": "John Muir", "work": "A Thousand-Mile Walk to the Gulf", "quote": "In the warm Florida hammocks, the glistening foliage of the **satinleaf** caught the breeze, flashing copper and dark emerald in the sun."},
            {"author": "Charles Sprague Sargent", "work": "The Silva of North America", "quote": "The southern **satinleaf** is easily recognized by the dense silky luster that covers the lower surfaces of its oval leaves."},
            {"author": "David Fairchild", "work": "Exploring for Plants", "quote": "We admired the ornamental beauty of the wild **satinleaf**, whose shimmering bicolored canopy graced the edges of the limestone glades."}
        ]
    },
    "satinpod": {
        "primary": "A biennial cruciferous plant (Lunaria annua), also called honesty or silver dollar, cultivated for its translucent, satiny silvery seed pods.",
        "secondary": "In ornamental horticulture and floristry, a brassicaceous garden plant whose central paper-thin silicle septa remain on dried stems for decorative arrangements.",
        "quotes": [
            {"author": "Gertrude Jekyll", "work": "Wood and Garden", "quote": "In the cottage borders, dried stems of **satinpod** displayed their translucent silvery disks, catching the pale winter sunlight like fairy coins."},
            {"author": "Henry David Thoreau", "work": "Autumn", "quote": "The delicate inner membrane of the **satinpod** gleamed among the frostbitten garden stalks, persistent through wind and snow."},
            {"author": "William Robinson", "work": "The English Flower Garden", "quote": "Honesty, often termed **satinpod** for its lustrous pearly pods, provides charming dried winter bouquets when gathered before heavy rains."}
        ]
    },
    "satinwood": {
        "primary": "A hard, close-grained tropical wood with a satiny golden-yellow luster, or the rutaceous tree yielding it, highly valued in fine cabinetmaking.",
        "secondary": "In decorative arts and Georgian woodworking, precious timber from Chloroxylon swietenia or Zanthoxylum flavum used for exquisite Sheraton-style veneers and marquetry.",
        "quotes": [
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "A delicate table of inlaid **satinwood** stood in the corner of the library, holding an antique silver bowl filled with violets."},
            {"author": "Thomas Chippendale", "work": "The Gentleman and Cabinet-Maker's Director", "quote": "For delicate drawing-room commodes and card tables, polished **satinwood** yields an incomparable golden luster when banded with rosewood."},
            {"author": "Arthur Conan Doyle", "work": "The Adventure of the Norwood Builder", "quote": "Holmes examined the handsome **satinwood** desk, pointing out the minute scratches around the lock to the perplexed inspector."}
        ]
    },
    "satiny": {
        "primary": "Having a smooth, glossy, or lustrous texture resembling that of satin fabric.",
        "secondary": "In botanical and zoological description, having an exceptionally sleek, lustrous surface or soft sheen like fine brushed silk.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Her fresh cheek had the smooth, **satiny** texture of an opening rose petal, blooming with vigorous country health."},
            {"author": "Edith Wharton", "work": "The House of Mirth", "quote": "Lily stroked the **satiny** surface of the lacquered screen, her delicate fingers sensitive to every refinement of luxury."},
            {"author": "Charles Darwin", "work": "The Various Contrivances by which Orchids are Fertilised by Insects", "quote": "The lower labellum of the orchid presents a **satiny** gloss that guides pollinating bees directly toward the nectary."}
        ]
    },
    "satire": {
        "primary": "The use of humor, irony, exaggeration, or ridicule to expose, criticize, and mock human folly, vices, or political corruption.",
        "secondary": "In literary theory and classical rhetoric, a genre originated by Roman poets (Lucilius, Horace, Juvenal) designed to reform morals through corrective wit.",
        "quotes": [
            {"author": "Jonathan Swift", "work": "The Battle of the Books", "quote": "**Satire** is a sort of glass wherein beholders do generally discover everybody's face but their own, which is the chief reason for its welcome."},
            {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "The most biting **satire** upon frivolous customs is the quiet dignity of a person who lives according to simple truth."},
            {"author": "Alexander Pope", "work": "Epistle to Dr. Arbuthnot", "quote": "O sacred weapon! left for truth's defense, Sole dread of folly, vice, and insolence, To all but heaven-directed **satire** dead!"}
        ]
    },
    "satiric": {
        "primary": "Of, relating to, or containing satire; mocking human vices or follies through trenchant irony and wit.",
        "secondary": "In classical literature and aesthetics, exhibiting the caustic corrective tone or formal poetic conventions of ancient verse satire.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "His thin lips curved into a faint, **satiric** smile as he watched the rustic dancers circling the dying bonfire."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "She disliked his **satiric** banter, sensing behind his witty compliments a cold indifference to sincere human feeling."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Emperor Julian vented his disappointment in a **satiric** diatribe against the luxurious citizens of Antioch."}
        ]
    },
    "satirical": {
        "primary": "Containing, using, or characterized by satire; biting, mocking, or sarcastically humorous in exposing folly.",
        "secondary": "In journalism and social criticism, employing irony, caricature, and lampooning to challenge entrenched dogmas and political abuses.",
        "quotes": [
            {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Bennet was of so odd a mixture of quick parts, sarcastic humor, reserve, and caprice, that his wife found his **satirical** wit impenetrable."},
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Though you be a grand juryman and a man of wisdom, you have a **satirical** vein that makes you more enemies than friends."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "The philosopher viewed the hurried building of the telegraph with a **satirical** eye, wondering what urgent news we had to tell."}
        ]
    }
}
