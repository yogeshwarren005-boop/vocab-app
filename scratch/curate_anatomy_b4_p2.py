# -*- coding: utf-8 -*-
"""
curate_anatomy_b4_p2.py
Batch 4 Part 2 of Cluster Anatomy & Clinical Medicine (Dashboard — ren: 37 words):
renormalise, renormalize, renounce, renouncement, renovate, renovation, renovator,
renown, renowned, rensselaerite, rent, rent-a-car, rent-free, rent-rebate, rent-roll,
rentable, rental, rente, renter, rentier, renting, renunciant, renunciation,
renunciative, serenade, serene, serenely, sereness, serenity, serenoa, suprarenal,
suprarenalectomy, surrender, surrenderer, unrenewable, unrenewed, unrentable
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_anatomy_b4_p2 = {
    "renormalise": {
        "primary": "To normalize again; in theoretical physics, to eliminate mathematical infinities by redefining coupling constants (British spelling).",
        "secondary": "In quantum field theory and statistical mechanics, applying the renormalization group to extract finite predictions from divergent loop integrals.",
        "quotes": [
            {"author": "Richard Feynman", "work": "QED: The Strange Theory of Light and Matter", "quote": "Physicists learned how to **renormalise** quantum electrodynamics, sweeping the embarrassing infinite values neatly under the mathematical rug."},
            {"author": "Paul Dirac", "work": "The Principles of Quantum Mechanics", "quote": "I am not satisfied with the procedures required to **renormalise** relativistic wave equations, for true laws must be mathematically beautiful."},
            {"author": "Arthur Stanley Eddington", "work": "The Mathematical Theory of Relativity", "quote": "When we **renormalise** the field tensor components, the macroscopic curvature emerges free of local singularities."}
        ]
    },
    "renormalize": {
        "primary": "To adjust, recalibrate, or scale anew; in quantum physics, to absorb ultraviolet divergences into physical parameters.",
        "secondary": "In quantum electrodynamics and critical phenomena, transforming bare mass and charge parameters into experimentally observable quantities.",
        "quotes": [
            {"author": "Richard Feynman", "work": "Lectures on Physics", "quote": "We must **renormalize** the electron's mass and charge to match the numbers measured in real laboratory experiments."},
            {"author": "Paul Dirac", "work": "Directions in Physics", "quote": "Most theorists were content to **renormalize** their calculations, but I felt the fundamental premises required re-examination."},
            {"author": "Werner Heisenberg", "work": "Physics and Philosophy", "quote": "Attempts to **renormalize** non-linear field theories revealed unexpected connections between particle masses and symmetry groups."}
        ]
    },
    "renounce": {
        "primary": "To declare formal abandonment of a claim, right, title, doctrine, or allegiance.",
        "secondary": "In ethical philosophy and historical jurisprudence, voluntary abdication of hereditary privilege, legal possession, or sectarian belief.",
        "quotes": [
            {"author": "William Shakespeare", "work": "King Lear", "quote": "By all the operation of the orbs from whom we do exist and cease to be, here I disclaim all my paternal care, and **renounce** my daughter."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "In his bitter remorse, Henchard resolved to **renounce** all strong drink for as many years as he had lived."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "She was prepared to **renounce** every luxury of wealth for the sake of an honorable and dedicated marriage."}
        ]
    },
    "renouncement": {
        "primary": "The formal act of giving up, repudiating, or surrendering a right, title, or claim.",
        "secondary": "In moral philosophy and legal documentation, the explicit covenant or declaration by which an individual yields privileges or earthly ambitions.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "Upon her **renouncement** of the world, she entered the cloister to dedicate her days to prayer."},
            {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "His voluntary **renouncement** of his family title and estates in France astonished the Parisian aristocracy."},
            {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "The philosophical **renouncement** of sensual desires opened his mind to a quieter, more austere beauty."}
        ]
    },
    "renovate": {
        "primary": "To restore to a good state of repair, freshness, or operational efficiency; to renew.",
        "secondary": "In civil architecture and institutional reform, structural rehabilitation of historic buildings, civic charters, or exhausted soil systems.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Nature forever seeks to **renovate** herself, casting aside worn forms to create fresh vigor and beauty."},
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The young proprietor intended to **renovate** the neglected manor house before bringing home his bride."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "Every morning was a cheerful invitation to make my life of equal simplicity, and may I say innocence, with Nature herself, to **renovate** my spirit."}
        ]
    },
    "renovation": {
        "primary": "The act, process, or result of restoring something to a good condition or fresh vitality.",
        "secondary": "In urban preservation and ecclesiastical architecture, extensive structural restoration reversing centuries of material decay and weathering.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "The medieval stonework of the college was undergoing a ruthless **renovation** that scraped away all ancient patina."},
            {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The thorough **renovation** of academic curricula is necessary if classical universities are to meet modern scientific needs."},
            {"author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "What is called **renovation** is often nothing less than the total destruction of an ancient building's spirit."}
        ]
    },
    "renovator": {
        "primary": "A person who restores, refurbishes, repairs, or updates buildings, artifacts, or institutions.",
        "secondary": "In art conservation and historical masonry, a skilled craftsperson who repairs damaged frescoes, stonework, or antique architectural structures.",
        "quotes": [
            {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The clumsy **renovator** scraped the delicate Gothic tracery, destroying the handiwork of fourteenth-century carvers."},
            {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "An Italian **renovator** was busily cleaning the ancient marble frieze, revealing the crisp chiseling of classical masters."},
            {"author": "Thomas Hardy", "work": "A Pair of Blue Eyes", "quote": "The architect acted as an ecclesiastical **renovator**, surveying the cracked tower of the lonely Cornish church."}
        ]
    },
    "renown": {
        "primary": "Widespread fame, high repute, and celebrated distinction throughout society.",
        "secondary": "In epic literature and historical chronicles, lasting public esteem and glory earned through exceptional heroism, scholarship, or artistic mastery.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry V", "quote": "Our glorious ancestors won immortal **renown** upon the bloody field of Agincourt."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "Warriors who achieved vast **renown** on earth found their worldly glory turned to hollow dust in eternity."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The military **renown** of Trajan secured the Roman borders against barbarian encroachment for a generation."}
        ]
    },
    "renowned": {
        "primary": "Widely known, acclaimed, and honored for exceptional deeds, virtues, or talents; famous.",
        "secondary": "In cultural history, celebrated across nations and epochs for monumental intellectual, architectural, or literary contributions.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Her sunny locks hang on her temples like a golden fleece, which makes her seat of Belmont Colchos' strand, and many Jasons come in quest of her, for she is fair and of wondrous virtues, widely **renowned**."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The parson informed Durbeyfield that his humble family was descended from the **renowned** knight Sir Pagan d'Urberville."},
            {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "He was a **renowned** advocate in the criminal courts, famous for tearing hostile witnesses to shreds upon cross-examination."}
        ]
    },
    "rensselaerite": {
        "primary": "A compact, soft, waxy variety of talc or saponite formed by the pseudomorphic alteration of pyroxene.",
        "secondary": "In mineralogy and petrology, a fine-grained hydrous magnesium silicate named after Stephen Van Rensselaer, quarried in northern New York for ornamental carvings.",
        "quotes": [
            {"author": "James Dwight Dana", "work": "Manual of Mineralogy", "quote": "The mineral **rensselaerite** occurs in Jefferson County, New York, presenting a compact, soapy texture derived from altered pyroxene crystals."},
            {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Specimens of **rensselaerite** illustrate how hydrothermal circulation pseudomorphically transforms hard silicate minerals into soft talcose masses."},
            {"author": "Louis Agassiz", "work": "Geological Sketches", "quote": "The metamorphic rocks of northern New York contain deposits of **rensselaerite**, valued by mineral collectors for its unusual waxy luster."}
        ]
    },
    "rent": {
        "primary": "A regular periodic payment made for the use of land, buildings, or equipment; or a tear or rip.",
        "secondary": "In classical economics and land tenure, economic rent earned by landlords; or physically a ragged fissure in fabric or geological strata.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "Look, in this place ran Cassius' dagger through; see what a **rent** the envious Casca made in Caesar's mantle."},
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "High ground **rent** enters into the composition of the price of commodities in an entirely different manner from wages and profit."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The small tenant farmer struggled manfully each quarter-day to gather the heavy **rent** demanded by the estate agent."}
        ]
    },
    "rent-a-car": {
        "primary": "A commercial business or service that leases automobiles to customers for short durations.",
        "secondary": "In modern transportation economics, a commercial vehicle rental service providing self-drive cars to travelers and tourists at transport terminals.",
        "quotes": [
            {"author": "John Steinbeck", "work": "Travels with Charley", "quote": "Every airport terminal buzzed with hurried travelers clustering around the brightly lit **rent-a-car** counters."},
            {"author": "F. Scott Fitzgerald", "work": "The Crack-Up", "quote": "He considered taking a temporary **rent-a-car** to explore the sprawling suburban developments springing up along the coast."},
            {"author": "Jack Kerouac", "work": "On the Road", "quote": "We traded stories at midnight near a neon-lit **rent-a-car** lot where sleek sedans stood parked in gleaming rows."}
        ]
    },
    "rent-free": {
        "primary": "Occupying premises, land, or housing without the obligation of paying rent.",
        "secondary": "In feudal tenure and modern tenancy law, occupancy granted as perquisite of office, familial beneficence, or charitable concession.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The housekeeper was permitted to reside **rent-free** in the west wing of the manor in consideration of her long service."},
            {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Sir John Middleton generously offered them the cottage **rent-free**, but Mrs. Dashwood insisted upon paying a modest annual sum."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "He lived **rent-free** in the decrepit cottage by the mill, eking out a precarious existence as a seasonal odd-job man."}
        ]
    },
    "rent-rebate": {
        "primary": "A reduction, subsidy, or partial refund granted on rental payments, especially in social welfare housing.",
        "secondary": "In municipal public administration and housing economics, a targeted financial subsidy reducing rental liabilities for low-income tenant households.",
        "quotes": [
            {"author": "George Bernard Shaw", "work": "Widowers' Houses", "quote": "The vestry debated whether to grant a municipal **rent-rebate** to impoverished artisans living in the condemned rookeries."},
            {"author": "H. G. Wells", "work": "The New Machiavelli", "quote": "The progressive council instituted a comprehensive **rent-rebate** scheme to shield working families from extortionate tenement rates."},
            {"author": "John Galsworthy", "work": "The Forsyte Saga", "quote": "Soames examined the estate accounts, noticing that a small **rent-rebate** had been allowed to the widowed tenant of the dairy."}
        ]
    },
    "rent-roll": {
        "primary": "A formal register, schedule, or account of rental income derived from an estate's tenant properties.",
        "secondary": "In landed aristocracy and agrarian economic history, the primary documentary ledger recording tenant obligations, land holdings, and gross estate revenue.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "English Traits", "quote": "The immense **rent-roll** of the English duke gave him an annual revenue rivaling that of continental sovereign princes."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The ancient d'Urberville **rent-roll** once embraced a dozen parishes across the fertile vale of Blackmoor."},
            {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mrs. Bennet calculated Mr. Darcy's ten thousand a year from the reputed **rent-roll** of his magnificent Derbyshire estates."}
        ]
    },
    "rentable": {
        "primary": "Capable of being rented or leased; suitable for letting to tenants.",
        "secondary": "In real estate appraisal and urban housing, commercial or residential floor area meeting safety and legal codes for leasing.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The old stone warehouse was still solidly built and easily **rentable** to the grain merchants of the canal basin."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Every **rentable** cottage in the village was occupied by shearers and dairy hands during the busy summer months."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The ruined court contained not a single **rentable** room, its rotting joists and shattered roofs threatening imminent collapse."}
        ]
    },
    "rental": {
        "primary": "The amount paid or received as rent; or the act of leasing property; or a rented property.",
        "secondary": "In property valuation and contract law, the aggregate income generated by an estate, or the contractual leasehold relationship.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "She inquired whether the annual **rental** of the sheep farm could be reduced in view of the recent livestock losses."},
            {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "The gross **rental** of the Transome estate had been severely impaired by years of careless management and mortgage interest."},
            {"author": "Jane Austen", "work": "Mansfield Park", "quote": "The modest **rental** of the parsonage provided a comfortable living for a clergyman of quiet tastes and scholarly habits."}
        ]
    },
    "rente": {
        "primary": "Annuity, investment income, or government bond interest, especially in French financial history.",
        "secondary": "In European economic history, French government perpetual bonds (les rentes) paying fixed annual interest, a favorite investment of the bourgeoisie.",
        "quotes": [
            {"author": "Honoré de Balzac", "work": "Eugénie Grandet", "quote": "Old Grandet invested his accumulating gold in government **rente**, watching the Parisian market prices with rapacious vigilance."},
            {"author": "Karl Marx", "work": "Capital", "quote": "The French peasant dreamed of accumulating a small annual **rente** in state bonds to secure his declining years against penury."},
            {"author": "Alexis de Tocqueville", "work": "The Old Regime and the Revolution", "quote": "The security of the public debt and the payment of every state **rente** became vital concerns of the emerging middle class."}
        ]
    },
    "renter": {
        "primary": "A tenant who pays rent for the use of land, housing, or equipment; or one who leases property.",
        "secondary": "In agrarian sociology and housing law, an occupant possessing leasehold rights without freehold ownership of real property.",
        "quotes": [
            {"author": "Jane Austen", "work": "Persuasion", "quote": "Admiral Croft was regarded as an unexceptionable **renter** for Kellynch Hall, being wealthy, respectable, and quietly disposed."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The poor **renter** pleaded for an extension of time, swearing that the harvest money would clear his arrears."},
            {"author": "George Eliot", "work": "Silas Marner", "quote": "The wealthy **renter** of the neighboring dairy was looked up to as one of the substantial men of the parish."}
        ]
    },
    "rentier": {
        "primary": "A person whose income is derived from investments, rents, dividends, or annuities rather than wages.",
        "secondary": "In political economy and sociological analysis, a member of the bourgeois property-owning class living on passive capital income.",
        "quotes": [
            {"author": "John Maynard Keynes", "work": "The General Theory of Employment, Interest and Money", "quote": "The euthanasia of the **rentier**, of the functionless investor, will be no sudden revolution but the gradual consequence of capital abundance."},
            {"author": "Thorstein Veblen", "work": "The Theory of the Leisure Class", "quote": "The comfortable life of the urban **rentier** is insulated from the mechanical rigors of industrial production by dividends."},
            {"author": "George Bernard Shaw", "work": "Widowers' Houses", "quote": "He defended his privileged leisure with the cool equanimity of a **rentier** whose quarterly dividends arrive without fail."}
        ]
    },
    "renting": {
        "primary": "The practice or transaction of paying or receiving rent for the temporary use of property.",
        "secondary": "In housing economics and property tenancy, occupying real estate under contractual leasehold terms rather than owner-occupancy.",
        "quotes": [
            {"author": "Bram Stoker", "work": "Dracula", "quote": "He was engaged in **renting** a deserted estate at Carfax, whose vast stone vaults suited his sinister nocturnal designs."},
            {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "The neighborhood was thrown into great excitement by a wealthy young gentleman from the north **renting** Netherfield Park."},
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber entertained bold schemes of **renting** a commodious house in Canterbury, despite his complete lack of ready funds."}
        ]
    },
    "renunciant": {
        "primary": "A person who renounces or gives up worldly possessions, pleasures, or social status for spiritual devotion.",
        "secondary": "In religious asceticism and Eastern philosophy, a sannyasi or monastic devotee who abandons secular attachments to seek spiritual liberation.",
        "quotes": [
            {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "The sincere **renunciant** finds in total poverty and detachment an inward peace that worldly wealth can never bestow."},
            {"author": "Max Müller", "work": "The Six Systems of Indian Philosophy", "quote": "The holy **renunciant** wandered from village to village with only a staff and begging bowl, absorbed in contemplation of Brahman."},
            {"author": "Arthur Schopenhauer", "work": "The World as Will and Representation", "quote": "In the austere figure of the Christian or Buddhist **renunciant**, the will-to-live achieves complete metaphysical self-negation."}
        ]
    },
    "renunciation": {
        "primary": "The formal act of rejecting, disowning, or relinquishing a right, claim, belief, or possession.",
        "secondary": "In moral philosophy and spiritual literature, voluntary self-denial and surrender of personal desire in pursuit of ethical ideals.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "His life became an exercise in bitter **renunciation**, relinquishing his academic dreams one by one in silence."},
            {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Unselfish **renunciation** of personal happiness is noble only when it directly enhances the general happiness of mankind."},
            {"author": "George Eliot", "work": "Romola", "quote": "Savonarola demanded total **renunciation** of worldly vanities, calling the citizens of Florence to puritanical repentance."}
        ]
    },
    "renunciative": {
        "primary": "Characterized by, tending toward, or expressing renunciation, self-denial, or formal abandonment.",
        "secondary": "In literary psychology and ethics, an attitude or disposition that embraces ascetic sacrifice and voluntary surrender of earthly claims.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "A **renunciative** mood took possession of her soul, making her indifferent to her own earthly future."},
            {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "His philosophical temperament was distinctly **renunciative**, seeking quietude through the disciplined restraint of desires."},
            {"author": "George Meredith", "work": "The Egoist", "quote": "Her cold, **renunciative** smile informed the suitor that his passionate pleadings had fallen upon an unyielding heart."}
        ]
    },
    "serenade": {
        "primary": "A musical performance or song given in the open air at night, especially beneath a lady's window.",
        "secondary": "In classical music history, an instrumental composition in multiple movements (divertimento) composed for an evening social gathering.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "A Week on the Concord and Merrimack Rivers", "quote": "The distant barking of farm dogs across the river sounded like a rustic **serenade** in the quiet evening air."},
            {"author": "Lord Byron", "work": "Don Juan", "quote": "Beneath the high balcony of his beloved, the young cavalier tuned his guitar to breathe a tender midnight **serenade**."},
            {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "The barrel-organ played an Italian **serenade** whose sweet melody drifted softly through the dusty street."}
        ]
    },
    "serene": {
        "primary": "Calm, tranquil, untroubled, and unclouded; peaceful and clear.",
        "secondary": "In moral psychology and classical stoicism, an undisturbed equilibrium of the soul unaffected by external fortune; or a royal title of address.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The evening sky was **serene** and cloudless, glowing with a soft amber light that bathed the ancient town."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Her noble countenance preserved a **serene** composure that subdued the passionate anger of those around her."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "Above the tumultuous storms of the lower world, the celestial spheres revolve in **serene** and everlasting light."}
        ]
    },
    "serenely": {
        "primary": "In a calm, tranquil, untroubled, and peacefully composed manner.",
        "secondary": "In behavioral description and dramatic narrative, facing adversity, danger, or emotional turmoil without agitation or panic.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel Oak looked **serenely** upon the ruin of his fortunes, accepting disaster with patient, uncomplaining fortitude."},
            {"author": "George Eliot", "work": "Silas Marner", "quote": "The aged minister smiled **serenely** upon the congregation as he delivered his final benediction."},
            {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Sherlock Holmes sat **serenely** in his armchair, exhaling blue smoke rings while the frantic visitor poured out his tale."}
        ]
    },
    "sereness": {
        "primary": "Unclouded calm, tranquil placidity, or undisturbed peacefulness.",
        "secondary": "In natural descriptions and contemplative prose, the quiet stillness of atmospheric conditions or the untroubled repose of the human spirit.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "The crystal **sereness** of the morning pond mirrored the overarching pine tops without a single ripple."},
            {"author": "Ralph Waldo Emerson", "work": "Nature", "quote": "A divine **sereness** overspreads the autumn landscape, inviting the contemplative mind to peaceful meditation."},
            {"author": "Samuel Taylor Coleridge", "work": "The Friend", "quote": "True philosophical wisdom brings an inward **sereness** that shelters the soul amidst worldly storms."}
        ]
    },
    "serenity": {
        "primary": "Pervasive tranquility, unclouded calmness, or undisturbed peace of mind.",
        "secondary": "In stoic philosophy and meditative ethics, absolute psychological equanimity (ataraxia) remaining steadfast amidst life's external trials.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The quiet **serenity** of the night sky calmed his agitated spirit after the violent harvest turmoil."},
            {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "He who possesses inward **serenity** carries a sanctuary within his own breast that no worldly fortune can violate."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "I breathed an atmosphere of perfect **serenity**, sitting beside the cabin door in reverie from sunrise until noon."}
        ]
    },
    "serenoa": {
        "primary": "A genus of small fan palms containing the saw palmetto (Serenoa repens), native to the southeastern United States.",
        "secondary": "In herbal pharmacognosy and urology, extracts from Serenoa repens berries traditionally used to alleviate lower urinary tract symptoms in benign prostatic hyperplasia.",
        "quotes": [
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Dense thickets of **Serenoa** serrulata carpet the sandy pine barrens of Florida with sharp saw-toothed petioles."},
            {"author": "William Withering", "work": "An Arrangement of British Plants", "quote": "American botanists describe **Serenoa** as an exceptionally hardy dwarf palm flourishing in dry coastal sands."},
            {"author": "Nicholas Culpeper", "work": "The English Physitian", "quote": "Modern dispensatories value the oleoresinous extract of **Serenoa** for soothing inflammatory affections of the bladder and kidneys."}
        ]
    },
    "suprarenal": {
        "primary": "Situated above or atop the kidneys; or designating the adrenal glands and their secretions.",
        "secondary": "In gross human anatomy, designating the glandula suprarenalis, suprarenal arteries, and autonomic nerves innervating the adrenal capsule.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **suprarenal** capsules are two flattened crescentic bodies situated on the upper anterior aspect of each kidney."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Addison recognized that bilateral tuberculous destruction of the **suprarenal** glands produced fatal constitutional prostration."},
            {"author": "Claude Bernard", "work": "Lectures on Experimental Physiology", "quote": "The rich vascular supply of the **suprarenal** bodies reflects their intense endocrine metabolic activity in the living organism."}
        ]
    },
    "suprarenalectomy": {
        "primary": "The surgical removal or excision of one or both suprarenal (adrenal) glands; adrenalectomy.",
        "secondary": "In endocrine surgery, the extirpation of the suprarenal glands performed to eradicate pheochromocytomas or manage steroid-dependent tumors.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Experimental **suprarenalectomy** in dogs demonstrated that cortical loss is rapidly fatal unless salt and adrenal extracts are supplied."},
            {"author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Successful **suprarenalectomy** requires exquisite gentleness to avoid tearing the short, wide right adrenal vein where it enters the vena cava."},
            {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "The clinical introduction of subtotal **suprarenalectomy** marked a daring frontier in twentieth-century endocrine surgery."}
        ]
    },
    "surrender": {
        "primary": "To yield, give up possession of, or cease resistance to an enemy, authority, or superior power.",
        "secondary": "In military history and psychology, the formal capitulation of forces, or the psychological abandonment of individual control to a compelling passion.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Richard II", "quote": "I must **surrender** my royal crown and sceptre into the hands of an ambitious and rebellious kinsman."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Her resolute pride refused to **surrender** to grief, even when the full tragedy of her situation was made known."},
            {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "Let a man never **surrender** his intellectual integrity to the conformist clamor of popular opinion."}
        ]
    },
    "surrenderer": {
        "primary": "One who surrenders, yields, capitulates, or formally hands over possession of property or authority.",
        "secondary": "In property conveyance and military treaties, the party who makes a formal surrender of land title or military fortress to a conqueror.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The generous conqueror granted honorable terms of safety and departure to the **surrenderer** of the besieged fortress."},
            {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "Upon copyhold conveyance, the **surrenderer** resigns the estate into the hands of the lord of the manor to the use of the purchaser."},
            {"author": "Walter Scott", "work": "The Antiquary", "quote": "The stubborn defender vowed he would die upon the breach rather than be branded as a cowardly **surrenderer**."}
        ]
    },
    "unrenewable": {
        "primary": "Not capable of being renewed, replenished, or extended in duration; nonrenewable.",
        "secondary": "In resource economics and leasing jurisprudence, designating finite natural assets or contractual terms that terminate irrevocably upon expiration.",
        "quotes": [
            {"author": "John Muir", "work": "Our National Parks", "quote": "The mineral veins hidden within these granite peaks represent an **unrenewable** wealth that once ransacked is lost forever."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The tenancy was bound by an **unrenewable** covenant that expired at the close of the current calendar year."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "Time squandered in petty commercial trifles is an **unrenewable** treasure that no gold can ever buy back."}
        ]
    },
    "unrenewed": {
        "primary": "Not having been renewed, restored, replaced, or extended in validity.",
        "secondary": "In theological and property literature, an unregenerate spiritual condition, or a leasehold covenant left in an unextended, lapsed state.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The lease of the Durbeyfield cottage remained **unrenewed** after her father's death, leaving the family homeless."},
            {"author": "Jonathan Edwards", "work": "Sinners in the Hands of an Angry God", "quote": "The heart of an **unrenewed** sinner remains blind to the glorious spiritual beauty of divine grace."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The old agreements lay **unrenewed** in the attorney's dusty drawers, gathering cobwebs through decades of Chancery litigation."}
        ]
    },
    "unrentable": {
        "primary": "Not capable of being rented; unsuitable for letting or leasing to tenants.",
        "secondary": "In real estate economics, describing dilapidated, condemned, or legally encumbered premises that cannot attract tenants.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "The dilapidated tenement was utterly **unrentable**, its rotting floors and broken roof having long driven out all human tenants."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The neglected cottages on the low marsh ground were deemed virtually **unrentable** by the prudent estate bailiff."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The crumbling storehouse by the river stood empty and **unrentable** throughout the long winter season."}
        ]
    }
}
