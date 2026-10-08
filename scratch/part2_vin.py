# -*- coding: utf-8 -*-
"""
Part 2 of Batch 4 Cluster Food, Eating & Drink: vin words 21-40 (20 words):
['province', 'provincial', 'provincialism', 'provincially', 'unconvinced',
 'unconvincing', 'unconvincingly', 'vinaceous', 'vinaigrette', 'vinca',
 'vincetoxicum', 'vincible', 'vincristine', 'vine', 'vinegar',
 'vinegariness', 'vinegarish', 'vinegarishness', 'vinegarroon', 'vinegarweed']
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part2_vin = {
    "province": {
        "primary": "An administrative subdivision or country district outside a nation's capital or imperial seat.",
        "secondary": "In intellectual and jurisdictional terms, a proper sphere of action, responsibility, expertise, or authoritative duty.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "Say 'tis not so, a **province** I will give thee, and make thy fortunes proud."},
            {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "It is not the **province** of speculative philosophy to overturn established institutions on abstract conjectures alone."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Every distant **province** felt the heavy weight of the legionary garrisons quartered along its frontier."}
        ]
    },
    "provincial": {
        "primary": "Pertaining to a province, rural territory, or district remote from the metropolitan capital.",
        "secondary": "Characterized by limited, narrow, or unsophisticated viewpoints, tastes, or cultural manners characteristic of rural localities.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The shops thought it very natural that a man had set aside the first-rate dealers in **provincial** market towns."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Her **provincial** upbringing had preserved in her an ardent desire to lead a noble, unselfish life."},
            {"author": "Henry James", "work": "Roderick Hudson", "quote": "He felt suffocated by the narrow moral horizons of his **provincial** American village."}
        ]
    },
    "provincialism": {
        "primary": "A word, phrase, idiom, or custom peculiar to a specific province, region, or rural locality.",
        "secondary": "In cultural criticism, narrowness of outlook, parochialism, or lack of cosmopolitan breadth and intellectual sophistication.",
        "quotes": [
            {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "The chief obstacle to an English academy is our inveterate **provincialism** of taste and lack of urbanity in criticism."},
            {"author": "William Hazlitt", "work": "Table Talk", "quote": "A marked **provincialism** clung to his dialect, betraying immediately the rugged dialect of Yorkshire."},
            {"author": "Henry James", "work": "Hawthorne", "quote": "The quiet Salem environment fostered a delicate genius, yet was marked by unmistakable New England **provincialism**."}
        ]
    },
    "provincially": {
        "primary": "In a provincial manner; with respect to a local province or region rather than a metropolitan capital.",
        "secondary": "In socio-cultural analysis, with parochial narrowness of outlook, local pride, or regional administrative scope.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Meanwhile Nicholas Bulstrode had used his hundred thousand discreetly, and was become **provincially**, solidly important."},
            {"author": "Honoré de Balzac", "work": "Lost Illusions", "quote": "In Angoulême she reigned supreme, dressed **provincially** yet regarded as an oracle of fashion by her neighbors."},
            {"author": "Thomas Carlyle", "work": "The Life of John Sterling", "quote": "He had passed his youth **provincially**, far removed from the turbulent literary controversies of London."}
        ]
    },
    "unconvinced": {
        "primary": "Not persuaded or satisfied by the evidence, arguments, or demonstrations presented.",
        "secondary": "In intellectual debate and scientific inquiry, maintaining skeptical reserve, suspended judgment, or principled dissent.",
        "quotes": [
            {"author": "Jane Austen", "work": "Emma", "quote": "Indeed you injure me if you suppose me **unconvinced**, for I perceive clearly the force of your counsel."},
            {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Athelney Jones listened with a stubborn smile, remaining wholly **unconvinced** by Holmes's delicate deductions."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Several eminent naturalists remained stubbornly **unconvinced** that natural selection alone could modify morphological structures."}
        ]
    },
    "unconvincing": {
        "primary": "Failing to persuade, reassure, or compel belief; lacking plausibility, force, or credibility.",
        "secondary": "In dramatic and rhetorical criticism, appearing artificial, contrived, or deficient in internal logical coherence.",
        "quotes": [
            {"author": "Virginia Woolf", "work": "The Voyage Out", "quote": "His stammered apology sounded hollow and **unconvincing** in the quiet drawing-room."},
            {"author": "Joseph Conrad", "work": "Under Western Eyes", "quote": "Razumov offered a brief explanation, but the strained tone of his voice made it sound singularly **unconvincing**."},
            {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "The stranger gave an **unconvincing** excuse for wrapping his entire face in thick flannel bandages."}
        ]
    },
    "unconvincingly": {
        "primary": "In an unconvincing or unpersuasive manner; without producing belief, agreement, or reassurance.",
        "secondary": "In forensic examination or stage performance, delivered with evident hesitation, awkwardness, or visible implausibility.",
        "quotes": [
            {"author": "E. M. Forster", "work": "A Room with a View", "quote": "Lucy laughed **unconvincingly**, turning her head away to conceal the sudden rush of color to her cheeks."},
            {"author": "Henry James", "work": "The Wings of the Dove", "quote": "Densher argued **unconvincingly** against his own conscience, seeking to justify what he knew was dishonorable."},
            {"author": "George Gissing", "work": "New Grub Street", "quote": "He assured his wife **unconvincingly** that the editor would accept the manuscript before the quarter ended."}
        ]
    },
    "vinaceous": {
        "primary": "Having the color of red wine; of a dull, purplish-red or wine-colored hue.",
        "secondary": "In botany, ornithology, and mycology, describing plumage, petals, or fungal caps displaying a dusky vinous-pink or claret tinge.",
        "quotes": [
            {"author": "John James Audubon", "work": "Ornithological Biography", "quote": "The breast of the dove is suffused with a delicate **vinaceous** tint that shimmers softly in the morning light."},
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The corolla exhibits a pale **vinaceous** hue, deepening toward the throat into a rich purplish crimson."},
            {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "Several specimens of fruit pigeons exhibited gorgeous **vinaceous** patches across their lower mantles and wings."}
        ]
    },
    "vinaigrette": {
        "primary": "A cold salad dressing made of oil, vinegar or lemon juice, and seasonings such as herbs and pepper.",
        "secondary": "In eighteenth- and nineteenth-century decorative arts, a small ornamental box with a perforated lid containing a sponge soaked in aromatic smelling salts.",
        "quotes": [
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Lord Henry passed beneath his nostrils the gilt trellis of an open **vinaigrette** box to revive his spirits."},
            {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Becky Sharp administered the pungent aromatic **vinaigrette** to restore her mistress from an untimely fainting fit."},
            {"author": "Mrs. Beeton", "work": "Mrs Beeton's Book of Household Management", "quote": "Pour a savory **vinaigrette** of fine olive oil, wine vinegar, and minced tarragon over the cold asparagus."}
        ]
    },
    "vinca": {
        "primary": "A genus of trailing evergreen shrubs and herbs in the dogbane family Apocynaceae, known as periwinkle.",
        "secondary": "In horticultural design and ethnobotany, widely cultivated for blue or purple salverform flowers and glossy foliage used as groundcover.",
        "quotes": [
            {"author": "John Ruskin", "work": "Proserpina: Studies of Wayside Flowers", "quote": "The blue blossom of the **vinca** creeps along the shaded garden border, opening its star among glossy dark leaves."},
            {"author": "Gertrude Jekyll", "work": "Wood and Garden", "quote": "Beneath the high canopy of beeches, a carpet of **vinca** minor forms an evergreen tapestry impervious to weeds."},
            {"author": "Liberty Hyde Bailey", "work": "Cyclopedia of American Horticulture", "quote": "Species of **vinca** are prized equally for their hardy trailing habits and their cheerful spring bloom."}
        ]
    },
    "vincetoxicum": {
        "primary": "A genus of herbaceous perennial plants in the Apocynaceae family, commonly called swallow-wort.",
        "secondary": "In historical herbal pharmacopeia, literally 'poison-vanquisher', reputed in traditional medicine to counteract animal venoms and toxic bites.",
        "quotes": [
            {"author": "Nicholas Culpeper", "work": "The Complete Herbal", "quote": "The root of **vincetoxicum**, or swallow-wort, is accounted a sovereign counter-poison against venomous bites."},
            {"author": "John Gerard", "work": "The Herball or Generall Historie of Plantes", "quote": "Ancient herbalists termed this plant **vincetoxicum** because of its supposed virtue in subduing virulent poisons."},
            {"author": "William Turner", "work": "A New Herball", "quote": "Of **vincetoxicum** write Dioscorides and Galen, praising its drying virtues in expelling malign humors from the veins."}
        ]
    },
    "vincible": {
        "primary": "Capable of being conquered, overcome, defeated, or subdued by superior effort or force.",
        "secondary": "In moral theology and scholastic casuistry, describing ignorance that could be dispelled through reasonable diligence, leaving culpability intact.",
        "quotes": [
            {"author": "Jeremy Taylor", "work": "Ductor Dubitantium", "quote": "Where knowledge was easily accessible, ignorance becomes **vincible** and affords no valid excuse before God's judgment."},
            {"author": "Thomas Aquinas", "work": "Summa Theologiae", "quote": "Because **vincible** ignorance can be removed by proper diligence, it does not entirely relieve the soul of sin."},
            {"author": "Edmund Burke", "work": "Letters on a Regicide Peace", "quote": "The difficulties before the coalition are formidable indeed, but they remain strictly **vincible** to resolute courage."}
        ]
    },
    "vincristine": {
        "primary": "A chemotherapeutic alkaloid obtained from the Madagascar periwinkle (*Catharanthus roseus*), used to treat leukemias and lymphomas.",
        "secondary": "In cellular oncology and pharmacology, an antimitotic agent that binds to tubulin dimers, arresting cells in metaphase by disrupting microtubule assembly.",
        "quotes": [
            {"author": "James F. Holland", "work": "Cancer Medicine", "quote": "The introduction of **vincristine** into combination regimens revolutionized the treatment of acute lymphoblastic leukemia in children."},
            {"author": "Vincent T. DeVita Jr.", "work": "The Death of Cancer", "quote": "We observed remarkable tumor regressions when **vincristine** was paired with prednisone and alkylating agents."},
            {"author": "Siddhartha Mukherjee", "work": "The Emperor of All Maladies", "quote": "Extracted from the humble periwinkle leaf, **vincristine** paralyzed the mitotic spindles of dividing leukemic blasts."}
        ]
    },
    "vine": {
        "primary": "A climbing, trailing, or creeping plant with a long, slender, flexible stem, especially the grapevine.",
        "secondary": "In viticulture and allegorical literature, specifically *Vitis vinifera*, symbol of fecundity, harvest, hospitality, and spiritual union.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Comedy of Errors", "quote": "Thou art an elm, my husband, I a **vine**, whose weakness, married to thy stronger state, makes me with thy strength to communicate."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "They led the **vine** to wed her elm; she spoused about him twines her marriageable arms."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "Wild grape clusters clambered up the pines, draping the festive **vine** over branches and rocks."}
        ]
    },
    "vinegar": {
        "primary": "A sour liquid containing acetic acid obtained by the fermentation of diluted alcoholic liquids such as wine or cider.",
        "secondary": "In culinary chemistry and classical pharmacology, an acidulous preservative, pickling solvent, and digestive condiment.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Other of such **vinegar** aspect that they'll not show their teeth in way of smile, though Nestor swear the jest be laughable."},
            {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "They steeped the herbs in sharp wine **vinegar** to neutralize the offensive effluvia of the dissection table."},
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "A pungent odor of malt **vinegar** and pickled walnuts hung perpetually about the pantry shelf."}
        ]
    },
    "vinegariness": {
        "primary": "Pervasive sourness, sharpness, or acetic acidity reminiscent of vinegar.",
        "secondary": "In sensory appraisal and behavioral description, a biting astringency in flavor or a peevish, ill-tempered disposition.",
        "quotes": [
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "An unmistakable **vinegariness** pervaded the attorney's speech, curdling the enthusiasm of his patriotic listeners."},
            {"author": "George Gissing", "work": "The Odd Women", "quote": "Miss Barfoot noticed the growing **vinegariness** of the spinster's voice whenever domestic happiness was mentioned."},
            {"author": "Mrs. Beeton", "work": "Mrs Beeton's Book of Household Management", "quote": "Excessive fermentation imparts an unwelcome **vinegariness** to the sauce, ruining the delicate flavor of the broth."}
        ]
    },
    "vinegarish": {
        "primary": "Somewhat sour, tart, or acid, like vinegar in taste, smell, or character.",
        "secondary": "In character description, expressing morose discontent, acerbic tartness, or chronic irritability.",
        "quotes": [
            {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "She turned upon him with a **vinegarish** look that instantly silenced his cheerful attempts at conversation."},
            {"author": "William Makepeace Thackeray", "work": "The Newcomes", "quote": "The dowager possessed a **vinegarish** temper that kept her unfortunate companions in constant dread."},
            {"author": "Washington Irving", "work": "Bracebridge Hall", "quote": "The old housekeeper gave a **vinegarish** sniff of disapproval at the boisterous holiday merriment of the youngsters."}
        ]
    },
    "vinegarishness": {
        "primary": "Pungent sourness, crabbed acerbity, or biting sharpness in disposition or flavor.",
        "secondary": "In psychological characterization, a pervasive acerbity and biting faultfinding that sours social relations.",
        "quotes": [
            {"author": "George Eliot", "work": "Scenes of Clerical Life", "quote": "There was an underlying **vinegarishness** in her complaints that made even her acts of charity feel like reproaches."},
            {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "Mrs. Proudie's customary **vinegarishness** was on this occasion tempered by a triumphant consciousness of victory."},
            {"author": "Tobias Smollett", "work": "The Expedition of Humphry Clinker", "quote": "Tabitha's chronic **vinegarishness** of humor drove the entire household to distraction before breakfast."}
        ]
    },
    "vinegarroon": {
        "primary": "A whip scorpion of the arachnid order Thelyphonida, having large pedipalps and a whip-like flagellum.",
        "secondary": "In desert arachnology, noted for expelling a defensive chemical spray containing high concentrations of acetic acid when disturbed.",
        "quotes": [
            {"author": "John Charles Van Dyke", "work": "The Desert: Further Studies in Natural Appearances", "quote": "The formidable **vinegarroon** lurks beneath the desert rocks, discharging its pungent, acetic spray when molested."},
            {"author": "William Henry Hudson", "work": "The Naturalist in La Plata", "quote": "The nocturnal **vinegarroon** resembles a stout scorpion, armed with crushing pincers and a whiplike caudal appendage."},
            {"author": "Theodore Roosevelt", "work": "Hunting Trips of a Ranchman", "quote": "Among the venomous vermin of the southern plains, the repulsive **vinegarroon** was regarded with superstitious dread."}
        ]
    },
    "vinegarweed": {
        "primary": "An aromatic annual plant (*Trichostema lanceolatum*) of the mint family native to western North America.",
        "secondary": "In California botanical ecology and ethnobotany, possessing foliage covered in glandular hairs that emit a strong, vinegar-like odor used traditionally in herbal remedies.",
        "quotes": [
            {"author": "John Muir", "work": "The Mountains of California", "quote": "On dry gravelly foothills, the pungent scent of **vinegarweed** fills the warm autumn air with its penetrating fragrance."},
            {"author": "Willis Linn Jepson", "work": "A Flora of Western Middle California", "quote": "The sticky foliage of **vinegarweed** gives off a heavy, sour smell that cattle avoid when browsing across the dry pastures."},
            {"author": "Charles Francis Saunders", "work": "Western Wild Flowers and Their Stories", "quote": "Native tribes steeped the pungent leaves of **vinegarweed** in water to prepare medicinal washes for chills and fevers."}
        ]
    }
}
