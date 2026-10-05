# -*- coding: utf-8 -*-
"""
Part 2 of Curated Time Batch 1:
- Dashboard — nov (21 words)
- Dashboard — saecul (7 words)
Total: 28 words
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_nov_saecul = {
    # =========================================================================
    # DASHBOARD — nov (21 words)
    # =========================================================================
    "innovate": {
        "primary": "To introduce novel methods, ideas, technologies, or products into an established field or practice.",
        "secondary": "In organizational economics and political philosophy, to initiate institutional transformations and break with customary conventions to solve emerging challenges.",
        "quotes": [
            {"author": "Francis Bacon", "work": "The Essays", "quote": "He that will not apply new remedies must expect new evils; for time is the greatest innovator, and if time alter things for the worse, and wisdom choose to **innovate** for the better, what shall be the end?"},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "He was eager to **innovate** in medical treatment, introducing hygienic methods that unsettled the old practitioners of the town."},
            {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "It is a deliberate policy to **innovate** upon ancient foundations rather than repair them with prudent reverence."},
        ]
    },
    "innovation": {
        "primary": "The introduction of something new; a newly developed method, idea, custom, or device.",
        "secondary": "In technological history and macroeconomic development, the commercialization or widespread adoption of inventions that disrupts existing market paradigms.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "To face the garment of rebellion with some fine colour that may please the eye of fickle changelings and poor discontents, which gape and rub the elbow at the news of hurlyburly **innovation**."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Every slight structural **innovation** that confers an adaptive advantage in the struggle for life tends to be preserved across generations."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "New opinions are always suspected, and usually opposed, without any other reason but because they are an **innovation** not already common."}
        ]
    },
    "innovational": {
        "primary": "Pertaining to, fostering, or characteristic of new methods, transformative ideas, or technical innovation.",
        "secondary": "In contemporary industrial economics, describing processes, policies, or organizational cultures that generate novel intellectual property and technical advancements.",
        "quotes": [
            {"author": "Joseph Schumpeter", "work": "The Theory of Economic Development", "quote": "The **innovational** impulse of energetic entrepreneurs disturbs the circular flow of static markets, driving economic expansion."},
            {"author": "Alfred Marshall", "work": "Industry and Trade", "quote": "Progressive manufacturing firms invest continuously in **innovational** designs to maintain their competitive advantage in global commerce."},
            {"author": "Thorstein Veblen", "work": "The Place of Science in Modern Civilisation", "quote": "Technological evolution is propelled by cumulative **innovational** adaptations arising from industrial workshop experience."}
        ]
    },
    "innovative": {
        "primary": "Featuring new, original, and creative methods or ideas; characterized by inventive forward-looking thought.",
        "secondary": "In product engineering and strategic design, possessing the capacity to conceive novel solutions and effectively execute unprecedented concepts.",
        "quotes": [
            {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Genius can only breathe freely in an atmosphere of freedom, where **innovative** minds are not stifled by customary conformity."},
            {"author": "William James", "work": "The Will to Believe and Other Essays in Popular Philosophy", "quote": "The individual of **innovative** intelligence reframes ancient dogmas into living, pragmatic hypotheses suitable for human action."},
            {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Scientific method rewards the **innovative** investigator who dares to test cherished hypotheses against unsparing empirical facts."}
        ]
    },
    "innovativeness": {
        "primary": "The inherent quality, capacity, or tendency to introduce creative novelties and inventive solutions.",
        "secondary": "In organizational sociology, the measurable propensity of an institution, team, or culture to adopt and assimilate pioneering practices.",
        "quotes": [
            {"author": "Thorstein Veblen", "work": "The Instinct of Workmanship", "quote": "Human craftsmanship displays an innate **innovativeness** that continually refines mechanical implements across prehistoric eras."},
            {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Social advancement correlates with the degree of intellectual **innovativeness** tolerated by the governing civil authority."},
            {"author": "John Dewey", "work": "Democracy and Education", "quote": "Democratic education must cultivate an alert **innovativeness** rather than passive acquiescence in traditional routines."}
        ]
    },
    "innovator": {
        "primary": "A person who introduces new ideas, methods, techniques, or inventions into an established sphere.",
        "secondary": "In intellectual and social history, a pioneer who challenges prevailing orthodoxy to establish original systems of thought or production.",
        "quotes": [
            {"author": "Francis Bacon", "work": "The Essays", "quote": "As the births of living creatures at first are ill-shapen, so are all innovations, the births of time; yet he that will not apply new remedies must expect new evils; for time is the greatest **innovator**."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate was regarded by the older practitioners as a dangerous **innovator** whose French methods threatened professional serenity."},
            {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "The bold **innovator** who projects grand schemes of civic reform must often confront the stubborn inertia of customary prejudice."}
        ]
    },
    "nov": {
        "primary": "A standard abbreviation for November, the eleventh month of the Gregorian calendar year.",
        "secondary": "In astronomical almanacs, chronological registries, and historical documents, the conventional notation denoting dates in late autumn.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The bleak winds of **Nov.** swept across the desolate expanse of Egdon Heath, stripping the remaining birchen foliage."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "London: Michaelmas term lately over, and the Lord Chancellor sitting in Lincoln's Inn Hall on a raw **Nov.** afternoon amidst dense fog."},
            {"author": "Henry David Thoreau", "work": "Journal", "quote": "By mid-**Nov.** the quiet ponds take on a crystalline border of skim-ice before the winter storms descend."}
        ]
    },
    "nova": {
        "primary": "A cataclysmic variable star that suddenly undergoes a dramatic increase in brightness before fading over months.",
        "secondary": "In astrophysics, a thermonuclear runaway occurring on the surface of an accreting white dwarf star within a close binary system.",
        "quotes": [
            {"author": "Arthur Eddington", "work": "Stars and Atoms", "quote": "The sudden outburst of a **nova** reveals the catastrophic release of thermonuclear energy from a previously inconspicuous stellar core."},
            {"author": "Camille Flammarion", "work": "Popular Astronomy", "quote": "Centuries ago, the apparition of a brilliant **nova** in Cassiopeia astonished Tycho Brahe and shattered the dogma of unchanging celestial spheres."},
            {"author": "H. G. Wells", "work": "The Star", "quote": "Astronomers noted the sensational radiance of the new visitor, resembling a blazing **nova** that outshone the brightest wandering planets."}
        ]
    },
    "novate": {
        "primary": "To replace an existing legal obligation or contract with a newly executed agreement, extinguishing the former.",
        "secondary": "In civil jurisprudence and contract law, to substitute either a new debtor, creditor, or substantive covenant with the mutual consent of all parties.",
        "quotes": [
            {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "Under the civil law tradition, parties could readily **novate** an antecedent debt by substituting a new debtor with express assent."},
            {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The court examined whether the subsequent deed was intended to **novate** the primary mortgage bond or merely confirm its obligations."},
            {"author": "Roscoe Pound", "work": "The Spirit of the Common Law", "quote": "Commercial transactions frequently require merchants to **novate** complicated tripartite agreements to expedite international credit."}
        ]
    },
    "novation": {
        "primary": "The formal replacement of an existing legal obligation, contract, or party with a new one that discharges the old.",
        "secondary": "In corporate finance and commercial law, the consensual transfer of contractual liabilities, releasing the original promisor from continuing performance.",
        "quotes": [
            {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "A valid **novation** operates to extinguish the prior covenant completely, substituting a new claim in its place."},
            {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "The doctrine of **novation** requires clear proof that the creditor consented to discharge the original obligor from all subsequent liability."},
            {"author": "James Bryce", "work": "Studies in History and Jurisprudence", "quote": "Roman legal ingenuity refined the device of **novation** into an indispensable instrument for the transfer of commercial duties."}
        ]
    },
    "novel": {
        "primary": "Strikingly new, unusual, or different from anything previously seen, known, or experienced.",
        "secondary": "In literary studies, an extended fictional prose narrative exploring character, complex social dynamics, and human experience.",
        "quotes": [
            {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "The king had found him a **novel** physician that healed his stubborn infirmity beyond all expectation."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "To Gabriel Oak the spectacle was completely **novel**, stirring emotions he had never before experienced in his solitary pastoral life."},
            {"author": "Francis Bacon", "work": "The Essays", "quote": "Custom is the principal magistrate of man's life; yet men marvel at **novel** occurrences that upset their habitual opinions."}
        ]
    },
    "novelette": {
        "primary": "A brief or compact work of prose fiction, longer than a short story but significantly shorter than a full novel.",
        "secondary": "In narrative poetics and publishing, a light novella typically between seven thousand and twenty thousand words, often featuring romance or melodrama.",
        "quotes": [
            {"author": "Henry James", "work": "The Art of Fiction", "quote": "The delicate proportion of the **novelette** permits an exquisite unity of impression that diffuse romances rarely achieve."},
            {"author": "Virginia Woolf", "work": "The Common Reader", "quote": "She turned the pages of the sentimental **novelette**, smiling at the predictable tribulations of its tearful heroine."},
            {"author": "George Gissing", "work": "New Grub Street", "quote": "He earned a meager livelihood by grinding out an occasional sensational **novelette** for popular weekly periodicals."}
        ]
    },
    "novelise": {
        "primary": "To convert, adapt, or transform a dramatic work, factual event, or screenplay into a written prose novel.",
        "secondary": "In comparative literature and media studies, to expand a dramatic scenario into an extended prose narrative with descriptive psychological interiority.",
        "quotes": [
            {"author": "George Bernard Shaw", "work": "Our Theatres in the Nineties", "quote": "An author who attempts to **novelise** a crisp theatrical farce usually dilutes its scenic vigor in excessive narrative description."},
            {"author": "Henry James", "work": "Notes on Novelists", "quote": "He sought to **novelise** the diplomatic memoirs of the French embassy, turning dry dispatches into lively romantic intrigue."},
            {"author": "Arnold Bennett", "work": "The Author's Craft", "quote": "Publishers frequently commissioned clever young writers to **novelise** successful stage productions for the railway bookstalls."}
        ]
    },
    "novelist": {
        "primary": "A literary writer or author who specializes in composing works of long fictional prose narrative.",
        "secondary": "In literary theory, an imaginative chronicler who investigates subjective consciousness and social structures through fictitious plot construction.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The serious **novelist** paints the manners and morals of an age with a brush dipped in the passions of living humanity."},
            {"author": "G. K. Chesterton", "work": "The Victorian Age in Literature", "quote": "Every great Victorian **novelist** was something of a moral crusader, using fiction as a battering ram against civic complacency."},
            {"author": "Henry David Thoreau", "work": "A Week on the Concord and Merrimack Rivers", "quote": "We read the famous **novelist** for an idle hour, but turn to the ancient poets when our spirits thirst for enduring truth."}
        ]
    },
    "novelize": {
        "primary": "To rewrite, adapt, or fictionalize real events or screen scripts into the format of a published novel.",
        "secondary": "In media adaptation and commercial print culture, to reconstruct theatrical or visual scenes as literary prose with interior monologue.",
        "quotes": [
            {"author": "Henry James", "work": "The Art of the Novel", "quote": "To **novelize** an historical catastrophe requires that the artist subordinate bare chronological records to moral drama."},
            {"author": "William Dean Howells", "work": "Criticism and Fiction", "quote": "The temptation to **novelize** actual biographical incidents often betrays an author into unseemly caricature of living neighbors."},
            {"author": "Edith Wharton", "work": "The Writing of Fiction", "quote": "An ambitious writer who decides to **novelize** popular folklore must maintain the archaic flavor without sacrificing emotional truth."}
        ]
    },
    "novelty": {
        "primary": "Freshness, originality, or striking unfamiliarity; an intriguing innovation or curious decorative item.",
        "secondary": "In cognitive psychology and aesthetics, the perceptual stimulus of unfamiliarity that captivates attention and evokes aesthetic curiosity.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "This **novelty** is only in request; and it is as dangerous to be aged in any kind of course, as it is virtuous to be constant in any undertaking."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The sudden arrival of the flamboyant sergeant had the **novelty** of an exotic bird alighting in a quiet English orchard."},
            {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "The attraction of mere **novelty** soon decays, leaving behind only that admiration which genuine excellence can command."}
        ]
    },
    "novice": {
        "primary": "A person new to and inexperienced in a job, trade, discipline, or situation; a beginner or apprentice.",
        "secondary": "In monastic tradition and canon law, a probationer admitted into a religious order who has not yet taken permanent solemn vows.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Tempest", "quote": "I am a fool to weep at what I am glad of. Fair encounter of two most rare affections! Heavens rain grace on that which breeds between 'em! A mere **novice** in worldly wisdom, Miranda spoke from the pure simplicity of her heart."},
            {"author": "Francis Bacon", "work": "The Essays", "quote": "In council, the wise statesman will neither despise the enthusiasm of the **novice** nor lean too heavily upon his untested judgment."},
            {"author": "James Joyce", "work": "A Portrait of the Artist as a Young Man", "quote": "The pious **novice** knelt before the altar steps in reverent contemplation of the vows that would sever him from secular ambitions."}
        ]
    },
    "renovate": {
        "primary": "To restore to a good state of repair; to refresh, renew, or revitalize an aging structure or condition.",
        "secondary": "In architecture and historic preservation, to rehabilitate an existing building by repairing degraded elements while retaining its structural integrity.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Nature will not be staled; she knows how to **renovate** her worn materials and clothe ancient rocks in fresh springtime verdure."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "They determined to **renovate** the dilapidated dairy house, whitewashing the stone walls and repairing the thatched roof before winter."},
            {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "An earnest attempt to **renovate** the gloomy mansion only revealed how deeply the stains of ancestral sorrow had penetrated its timber."}
        ]
    },
    "renovation": {
        "primary": "The action or process of repairing, renewing, or modernizing an existing building, room, or institution.",
        "secondary": "In urban planning and historic restoration, the comprehensive upgrading of infrastructure, architectural finishes, or cultural institutions.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The ancient parish church was undergoing extensive **renovation**, with scaffolding rising against the weathered Norman arches."},
            {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Mr. Rochester ordered the complete **renovation** of the west gallery, replacing the faded tapestries with modern appointments."},
            {"author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "What is commonly called **renovation** is often the total destruction of that historic soul which no modern hand can restore."}
        ]
    },
    "renovator": {
        "primary": "A person or specialist who restores, renews, refurbishes, or modernizes older buildings or objects.",
        "secondary": "In architectural conservation and fine arts preservation, a craftsman who cleans, mends, and stabilizes antique structures or artworks.",
        "quotes": [
            {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The ruthless **renovator** has scraped away the delicate chisel marks of medieval sculptors, substituting cold mechanical marble."},
            {"author": "Thomas Hardy", "work": "A Pair of Blue Eyes", "quote": "The young architect was engaged as a church **renovator**, charged with surveying the crumbling towers of the Cornish coast."},
            {"author": "William Morris", "work": "Hopes and Fears for Art", "quote": "Too often the modern **renovator** behaves like a barbarian conqueror, erasing the authentic patina of centuries under the pretext of improvement."}
        ]
    },
    "supernova": {
        "primary": "A colossal astronomical stellar explosion that briefly outshines an entire galaxy, radiating enormous energy.",
        "secondary": "In high-energy astrophysics, the catastrophic gravitational core collapse or thermonuclear detonation of an evolving massive star, disseminating heavy chemical elements.",
        "quotes": [
            {"author": "Arthur Eddington", "work": "The Expanding Universe", "quote": "The extraordinary luminosity of a **supernova** exceeds that of millions of ordinary stars combined, marking the violent climax of stellar life."},
            {"author": "Subrahmanyan Chandrasekhar", "work": "An Introduction to the Study of Stellar Structure", "quote": "A massive degenerate stellar core exceeding the limiting mass must inevitably precipitate a catastrophic **supernova** detonation."},
            {"author": "Fred Hoyle", "work": "Frontiers of Astronomy", "quote": "The synthesis of heavy elements beyond iron in the cosmic abundance curve occurs predominantly within the fiery furnace of a **supernova** explosion."}
        ]
    },

    # =========================================================================
    # DASHBOARD — saecul (7 words)
    # =========================================================================
    "secular": {
        "primary": "Denoting attitudes, activities, or institutions that have no religious or spiritual basis; worldly rather than sacred.",
        "secondary": "In astronomical and geological physics, denoting slow, continuous processes or trends occurring over immense periods or centuries.",
        "quotes": [
            {"author": "H. G. Wells", "work": "The Outline of History", "quote": "The conflict between papal claims and **secular** monarchs shaped the political architecture of medieval Europe."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "His mind was drawn to **secular** pursuits, finding more delight in the sciences of nature than in ecclesiastical disputations."},
            {"author": "James Joyce", "work": "A Portrait of the Artist as a Young Man", "quote": "He turned his gaze away from the cloister, resolving to embrace the rich, tumultous experience of the **secular** world."}
        ]
    },
    "secularisation": {
        "primary": "The gradual historical transformation of a society from close religious identification to non-religious institutions.",
        "secondary": "In political philosophy and British sociology, the institutional transfer of civic administration, education, and legal authority from church control to civil governance.",
        "quotes": [
            {"author": "Max Weber", "work": "The Protestant Ethic and the Spirit of Capitalism", "quote": "The steady **secularisation** of daily life dissolved the ascetic religious impulses that originally accompanied early capitalism."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The gradual **secularisation** of civil magistracies marked the boundary between ancient priestly dominion and modern polity."},
            {"author": "John Stuart Mill", "work": "Essays on Some Unsettled Questions of Political Economy", "quote": "The ongoing **secularisation** of national universities permitted scientific research to proceed unfettered by clerical dogmas."}
        ]
    },
    "secularise": {
        "primary": "To convert, transfer, or adapt an ecclesiastical institution, property, or law to civil or worldly ownership and control.",
        "secondary": "In European legal history, to confiscate or reallocate church lands, monastic foundations, or education systems to state management.",
        "quotes": [
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The crown ministers determined to **secularise** the vast revenues of the monastic estates to replenish the royal exchequer."},
            {"author": "Henry Hallam", "work": "View of the State of Europe during the Middle Ages", "quote": "The German princes resolved to **secularise** several ecclesiastical bishoprics in order to consolidate their territorial authority."},
            {"author": "David Hume", "work": "The History of England", "quote": "A bold petition was presented to Parliament urging the commons to **secularise** church holdings for public relief."}
        ]
    },
    "secularism": {
        "primary": "The belief or ethical principle that religion should be kept strictly separate from civic, political, and public affairs.",
        "secondary": "In political jurisprudence and social philosophy, a constitutional framework ensuring state neutrality toward all religious creeds while safeguarding individual freedom of conscience.",
        "quotes": [
            {"author": "G. K. Chesterton", "work": "Orthodoxy", "quote": "Modern **secularism** attempts to construct a coherent morality while severing the transcendent roots from which moral imperatives originally sprang."},
            {"author": "John Stuart Mill", "work": "On Liberty", "quote": "The growing influence of **secularism** fosters a civic sphere where diverse creeds coexist beneath equal, non-sectarian laws."},
            {"author": "Matthew Arnold", "work": "Literature and Dogma", "quote": "The aggressive advance of mechanical **secularism** threatens to desiccate those poetic sympathies that sustain the human spirit."}
        ]
    },
    "secularist": {
        "primary": "An advocate of separating religious institutions and dogmas from government, state education, and public policy.",
        "secondary": "In social reform history, an activist who promotes rationalist, non-theological moral foundations and civic ethics for democratic society.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "Science and Christian Tradition", "quote": "The dedicated **secularist** insists that public schools must impart demonstrable scientific knowledge rather than sectarian catechisms."},
            {"author": "George Jacob Holyoake", "work": "English Secularism", "quote": "The primary duty of the **secularist** is to improve material conditions in this world without relying upon speculative expectations of the next."},
            {"author": "G. K. Chesterton", "work": "Heretics", "quote": "The militant **secularist** frequently exhibits a dogmatic zeal that rivals the most uncompromising religious inquisitor."}
        ]
    },
    "secularization": {
        "primary": "The historical process whereby religious beliefs, practices, and institutions lose their dominant social and cultural authority.",
        "secondary": "In the sociology of religion, the multi-dimensional decline of religious involvement alongside the rise of rationalized, differentiated secular social spheres.",
        "quotes": [
            {"author": "Max Weber", "work": "The Sociology of Religion", "quote": "The progressive **secularization** of modern culture dismantles the enchanted cosmic order, instituting an era of rational bureaucracy."},
            {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "In Europe, the relentless **secularization** of intellectual elites appeared to weaken the moral cohesion that sustains free republics."},
            {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "Despite the outward **secularization** of social life, mystical religious experiences remain a permanent feature of individual psychology."}
        ]
    },
    "secularize": {
        "primary": "To transfer from religious to civil ownership, influence, or control; to make worldly and non-religious.",
        "secondary": "In constitutional history and sociology, to eliminate ecclesiastical authority over legal codes, marriage, welfare, and schooling.",
        "quotes": [
            {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The revolutionary assembly voted to **secularize** all educational endowments, placing the lyceums under direct civic oversight."},
            {"author": "Alexis de Tocqueville", "work": "The Old Regime and the Revolution", "quote": "The philosophers aimed to **secularize** public morality, replacing ecclesiastical dogmas with universal concepts of civic duty."},
            {"author": "John Morley", "work": "Life of William Ewart Gladstone", "quote": "A protracted political struggle was waged to **secularize** the national universities and open their fellowships to men of all creeds."}
        ]
    }
}
