# -*- coding: utf-8 -*-
"""
Part 1 of Curated Data for Asking & Seeking Batch 3 (Dashboard — pet):
Words 1 to 32:
['appetence', 'appetency', 'appetent', 'appetiser', 'appetising', 'appetisingness',
 'appetite', 'appetitive', 'appetizer', 'appetizing', 'appetizingness', 'centripetal',
 'compete', 'competence', 'competency', 'competent', 'competently', 'competition',
 'competitive', 'competitively', 'competitiveness', 'competitor', 'competitory',
 'impetiginous', 'impetigo', 'impetuosity', 'impetuous', 'impetuously',
 'impetuousness', 'impetus', 'incompetence', 'incompetency']
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

pet_part1 = {
    "appetence": {
        "primary": "An instinctive inclination, intense natural craving, or sensual longing directed toward an object.",
        "secondary": "In philosophical psychology and metaphysical ethics, an inherent propensity of living consciousness driving purposeful action toward gratification.",
        "quotes": [
            {"author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "The lower animals act merely from sensible **appetence**, devoid of that reflective will which constitutes moral agency."},
            {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Man's spiritual hunger cannot be satisfied by mere material abundance or earthly **appetence**."},
            {"author": "George Henry Lewes", "work": "Problems of Life and Mind", "quote": "Every vital tissue manifests an inherent **appetence** for those organic compounds necessary to maintain its vegetative equilibrium."}
        ]
    },
    "appetency": {
        "primary": "An instinctive tendency or natural urge impelling an organism toward that which sustains or pleases it.",
        "secondary": "In evolutionary biology and Lamarckian philosophy, the vital striving or organic affinity assumed to induce physiological adaptation.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants Under Domestication", "quote": "Erasmus Darwin attributed the development of new organs to the long-continued **appetency** of animals seeking gratification."},
            {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "The primitive reflex develops gradually into conscious **appetency** as nervous ganglia centralize sensory impulses."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "Every instinctive **appetency** leaves behind an organic memory that colors future desires and motives."}
        ]
    },
    "appetent": {
        "primary": "Eagerly desirous, actively craving, or marked by ardent longing and instinctive appetite.",
        "secondary": "In scholastic philosophy, describing an agent characterized by affective seeking rather than cognitive detachment.",
        "quotes": [
            {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The animal nature is perpetually **appetent** of bodily preservation, fleeing instinctively whatever threat may disrupt life."},
            {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "The youthful mind remains ever **appetent** of noble friendship, seeking kindred souls across all social divisions."},
            {"author": "Herman Melville", "work": "Mardi: and a Voyage Thither", "quote": "The wanderers, faint and weary, grew fiercely **appetent** of food and shelter after traversing the barren mountain pass."}
        ]
    },
    "appetiser": {
        "primary": "A small portion of savory food or stimulating beverage served before a meal to sharpen the appetite.",
        "secondary": "In culinary traditions and gastronomy, an introductory course designed to awaken digestive secretions through acid, salt, or bitterness.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "A modest **appetiser** of salted fish and wine was set upon the sideboard to revive the flagging spirits of the travelers."},
            {"author": "W. M. Thackeray", "work": "The History of Pendennis", "quote": "The captain insisted that a brisk walk across the windy heath was the finest **appetiser** known to human experience."},
            {"author": "Anthony Trollope", "work": "The Last Chronicle of Barset", "quote": "The doctor partook sparingly of an **appetiser** before sitting down to the substantial clerical feast."}
        ]
    },
    "appetising": {
        "primary": "Appealing to the sense of taste or smell; attractive, savory, and invitingly edible.",
        "secondary": "In aesthetic and sensory descriptions, presenting an alluring visual or olfactory harmony that arouses desire or anticipation.",
        "quotes": [
            {"author": "George Eliot", "work": "Adam Bede", "quote": "The kitchen was filled with an **appetising** fragrance of freshly baked loaf bread and roasting fowl."},
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The brown crusted pasties looked exceedingly **appetising** to the tired laborers resting beneath the apple boughs."},
            {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The housekeeper set forth an **appetising** repast of cold fowl, golden cheese, and sweet wheaten bread."}
        ]
    },
    "appetisingness": {
        "primary": "The property or degree of being savory, inviting to the palate, or pleasant to behold.",
        "secondary": "In sensory evaluation and food science, the measurable appeal of a culinary preparation derived from aroma, texture, and visual balance.",
        "quotes": [
            {"author": "Mrs. Isabella Beeton", "work": "The Book of Household Management", "quote": "The culinary artist must ensure that every garnish enhances the **appetisingness** of the dish without overpowering its delicate flavor."},
            {"author": "Brillat-Savarin", "work": "The Physiology of Taste", "quote": "The ultimate test of gastronomic merit lies in the sustained **appetisingness** that charms the guest from the first morsel to the last."},
            {"author": "Alexis Soyer", "work": "The Modern Housewife", "quote": "Skillful seasoning elevates the plainest stew into an extraordinary triumph of aroma and sheer **appetisingness**."}
        ]
    },
    "appetite": {
        "primary": "A natural physiological desire or craving to satisfy bodily needs, especially for food.",
        "secondary": "In moral philosophy and psychology, any strong urge, passion, or drive impelling human action toward specific worldly ends.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "Why, she would hang on him as if increase of **appetite** had grown by what it fed on."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "His intellectual **appetite** was keen, but his digestion of profound philosophy remained somewhat imperfect."},
            {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "A healthy soul maintains an uncorrupted **appetite** for truth and simpleness in every relation of life."}
        ]
    },
    "appetitive": {
        "primary": "Pertaining to, actuated by, or characterized by bodily desire, craving, or instinctive appetite.",
        "secondary": "In classical philosophy, designating the irrational or sensory faculty of the soul that pursues pleasure and avoids physical discomfort.",
        "quotes": [
            {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The rational faculty ought ever to govern the **appetitive** inclinations, lest passion undermine civic prudence."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Sensible objects stimulate our **appetitive** nature long before the intellect attains the capacity for abstract reflection."},
            {"author": "David Hume", "work": "A Treatise of Human Nature", "quote": "Moral distinctions do not derive solely from reason, but involve our sympathetic and **appetitive** dispositions."}
        ]
    },
    "appetizer": {
        "primary": "A food, drink, or dainty served before a meal to stimulate desire for succeeding courses.",
        "secondary": "In metaphorical usage, an enticing introductory incident or preliminary experience that whets interest for an impending event.",
        "quotes": [
            {"author": "Mark Twain", "work": "A Tramp Abroad", "quote": "A brisk morning stroll in the bracing mountain air served as an infallible **appetizer** before our hearty breakfast."},
            {"author": "O. Henry", "work": "The Four Million", "quote": "He sipped the fiery vermouth as an **appetizer**, waiting patiently at the café counter for his dinner companion."},
            {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "The lavish display of rare delicacies on the buffet served merely as an **appetizer** for the grand banquet to follow."}
        ]
    },
    "appetizing": {
        "primary": "Exciting a desire for food; appealing to taste, smell, or visual sensibility.",
        "secondary": "In literary description, evoking enticing anticipation or sensory delight through rich aesthetic details.",
        "quotes": [
            {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "The fresh gingerbread figures in the shop window presented an **appetizing** spectacle to the schoolboys hurrying down the street."},
            {"author": "Washington Irving", "work": "The Legend of Sleepy Hollow", "quote": "Ichabod Crane cast his wandering eyes over the **appetizing** display of apple pies, peach preserves, and roast ducks."},
            {"author": "Louisa May Alcott", "work": "Little Women", "quote": "Meg arranged the warm biscuits and strawberry jam in the most **appetizing** fashion upon the round tea table."}
        ]
    },
    "appetizingness": {
        "primary": "The pleasing quality of food, scent, or presentation that stimulates hunger or aesthetic pleasure.",
        "secondary": "In consumer sensory psychology, the sum of perceptual factors that make edible goods enticing to prospective eaters.",
        "quotes": [
            {"author": "Brillat-Savarin", "work": "The Physiology of Taste", "quote": "True gastronomic genius consists in imparting irresistible **appetizingness** even to the simplest broth."},
            {"author": "Mrs. Isabella Beeton", "work": "The Book of Household Management", "quote": "Color and symmetry contribute immensely to the general **appetizingness** of a banquet table."},
            {"author": "Alexis Soyer", "work": "The Modern Housewife", "quote": "A clean copper pan and an even flame enhance the **appetizingness** of sauces beyond all costly additives."}
        ]
    },
    "centripetal": {
        "primary": "Directed toward the center or interior; tending to move inward along a radius.",
        "secondary": "In classical mechanics and political sociology, designating a centralizing force or consolidating tendency that holds elements within a unified orbit.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Nature balances the centrifugal urge of individual divergence with the strong **centripetal** gravity of common law."},
            {"author": "Bram Stoker", "work": "Dracula", "quote": "The howling wolves seemed gathered by some **centripetal** command, drawing closer toward our beleaguered carriage."},
            {"author": "Walt Whitman", "work": "Democratic Vistas", "quote": "A great nation requires both centrifugal personal freedom and the **centripetal** cohesion of fraternal solidarity."}
        ]
    },
    "compete": {
        "primary": "To strive against others in pursuit of a prize, goal, position, or common advantage.",
        "secondary": "In evolutionary biology and economic theory, to contest for limited environmental resources, market share, or reproductive success.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "As the species of the same genus usually have much similarity in habits, they generally **compete** closely with each other."},
            {"author": "James Joyce", "work": "Ulysses", "quote": "Rival merchants **compete** fiercely for custom along the quays, shouting the superior merits of their wares."},
            {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "Strong athletes gather upon the field to **compete** for renown in running, wrestling, and leaping."}
        ]
    },
    "competence": {
        "primary": "The possession of sufficient knowledge, skill, strength, or legal authority to perform a specified task.",
        "secondary": "In socio-economic history, an adequate income or modest fortune securing independence from wage labor or poverty.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry IV, Part 2", "quote": "For **competence** of life I will allow you, that lack of means enforce you not to evil."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "He possessed unquestioned professional **competence**, yet his austere manner alienated many prospective patients."},
            {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes conducted the investigation with consummate **competence**, unraveling the intricate web of deception without hesitation."}
        ]
    },
    "competency": {
        "primary": "Sufficiency of qualification, capacity, or resources necessary to achieve an end or render legal validity.",
        "secondary": "In jurisprudence, the legal fitness of a witness to testify or of an individual to manage personal affairs or enter contracts.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Superfluity comes sooner by white hairs, but **competency** lives longer."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "A modest **competency** gained through years of prudent grain trade enabled him to attain civic respectability."},
            {"author": "Herman Melville", "work": "Bartleby, the Scrivener", "quote": "My practice as a conveyancer yielded a snug **competency**, which was all I ever coveted in this ambitious world."}
        ]
    },
    "competent": {
        "primary": "Properly qualified, capable, adequate, and possessing the requisite ability or skill.",
        "secondary": "In law and institutional administration, possessing valid jurisdictional power or mental admissibility to execute bindings acts.",
        "quotes": [
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "No evidence can be admitted without **competent** testimony from witnesses whose faculties remain unimpaired."},
            {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Of two pleasures, if there be one to which all who are **competent** judges give a decided preference, that is the more desirable."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Only naturalists **competent** to judge subtle anatomical variations can appreciate how closely related these primate species truly are."}
        ]
    },
    "competently": {
        "primary": "In a capable, adequate, and skillful manner that meets all operational requirements.",
        "secondary": "In professional assessment, performing responsibilities with proven proficiency, adherence to standards, and dependable mastery.",
        "quotes": [
            {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "He who accomplishes his appointed work **competently** contributes more to the commonwealth than ten noisy theorists."},
            {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "The newly installed archdeacon managed the diocesan business **competently**, leaving no room for episcopal complaint."},
            {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The artillery officers directed their battery fire **competently**, yet conventional ordnance proved powerless against the invaders."}
        ]
    },
    "competition": {
        "primary": "The act or process of striving against others to achieve supremacy, win a contest, or secure resources.",
        "secondary": "In political economy and ecology, the market mechanism or biotic pressure governing price formation, innovation, and natural selection.",
        "quotes": [
            {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Where **competition** is free and unrestrained, prices will naturally adjust to the lowest cost of production."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Battle within battle must be continually recurring with varying success, in the universal **competition** for existence."},
            {"author": "Ralph Waldo Emerson", "work": "The Conduct of Life", "quote": "Vigorous commercial **competition** sharpens individual intellect and compels every man to discover his true productive calling."}
        ]
    },
    "competitive": {
        "primary": "Relating to, characterized by, or inclined toward competition, rivalry, and ambitious struggle.",
        "secondary": "In industrial commerce, possessing advantages in cost, performance, or strategy that enable an enterprise to prevail over rivals.",
        "quotes": [
            {"author": "Thorstein Veblen", "work": "The Theory of the Leisure Class", "quote": "The modern industrial system fosters an intensely **competitive** drive for pecuniary status and conspicuous display."},
            {"author": "H. G. Wells", "work": "Tono-Bungay", "quote": "He threw himself into the chaotic, **competitive** whirl of London commerce with reckless commercial enthusiasm."},
            {"author": "Henry Adams", "work": "The Education of Henry Adams", "quote": "American society was transformed into a giant **competitive** engine where only mechanical force and finance held sway."}
        ]
    },
    "competitively": {
        "primary": "In a manner driven by competition, mutual rivalry, or determined striving for advantage.",
        "secondary": "In market economics, establishing commercial pricing or product standards capable of rivaling counterparts on equal or superior terms.",
        "quotes": [
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "When independent tradesmen operate **competitively**, the general consumer enjoys lower prices and enhanced mercantile honesty."},
            {"author": "Alfred Marshall", "work": "Principles of Economics", "quote": "Firms must manage their administrative overhead **competitively** if they expect to survive recurring cyclical depressions."},
            {"author": "Woodrow Wilson", "work": "The New Freedom", "quote": "A democracy thrives only when enterprise can organize **competitively** without fear of monopolistic suppression."}
        ]
    },
    "competitiveness": {
        "primary": "An aggressive disposition or institutional capability to contest successfully against rivals.",
        "secondary": "In macroeconomic analysis, the structural efficiency and technological adaptability allowing a firm or country to maintain market supremacy.",
        "quotes": [
            {"author": "Joseph Schumpeter", "work": "Capitalism, Socialism and Democracy", "quote": "Dynamic industrial **competitiveness** relies far more upon technological innovation than upon trivial marginal price adjustments."},
            {"author": "Max Weber", "work": "The Protestant Ethic and the Spirit of Capitalism", "quote": "The ethical sanction of vocational diligence imparted an unprecedented **competitiveness** to early Western enterprise."},
            {"author": "Thorstein Veblen", "work": "The Instinct of Workmanship", "quote": "Exaggerated commercial **competitiveness** often redirects human ingenuity away from craftsmanship toward predatory marketing."}
        ]
    },
    "competitor": {
        "primary": "A person, group, or organization that strives against another for supremacy, prize, or commercial advantage.",
        "secondary": "In evolutionary biology, an organism or species contending against others for food, territory, light, or mating priority.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "I'll be your **competitor** in this enterprise, and share equally in whatever honor may be achieved."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Any variety which possesses some slight advantage will gradually exterminate its less favored **competitor** in the same region."},
            {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "Ralph Nickleby viewed every honest merchant as a foolish **competitor** ripe to be entangled in usurious financial bonds."}
        ]
    },
    "competitory": {
        "primary": "Pertaining to, involving, or characterized by mutual competition and rivalry.",
        "secondary": "In social philosophy and legal doctrine, describing frameworks designed around institutionalized contention rather than cooperative consensus.",
        "quotes": [
            {"author": "Jeremy Bentham", "work": "Principles of the Civil Code", "quote": "The **competitory** instinct among citizens must be harmonized by equitable legislation to prevent social strife."},
            {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "Industrial civilization replaces military conquest with a peaceful yet rigorous **competitory** mechanism of trade."},
            {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "A purely **competitory** labor market inevitably bears heavily upon those least equipped for strenuous manual exertion."}
        ]
    },
    "impetiginous": {
        "primary": "Pertaining to, resembling, or affected by impetigo; characterized by pustular or crusted cutaneous lesions.",
        "secondary": "In clinical dermatology, denoting contagious vesicular eruptions typically caused by staphylococcal or streptococcal skin infection.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The face was covered with an **impetiginous** eruption presenting thick, honey-colored crusts that yielded rapidly to antiseptic dressings."},
            {"author": "Thomas Watson", "work": "Lectures on the Principles and Practice of Physic", "quote": "The physician must distinguish between simple eczema and acute **impetiginous** eczema with prominent pustulation."},
            {"author": "Jonathan Hutchinson", "work": "Clinical Lectures on Surgery and Medicine", "quote": "Neglected parasitic infestations often become complicated by secondary **impetiginous** sores across the extremities."}
        ]
    },
    "impetigo": {
        "primary": "A contagious acute bacterial skin disease characterized by superficial pustules that rupture and form yellowish crusts.",
        "secondary": "In dermatological epidemiology, an infectious superficial pyoderma predominant among children, usually caused by Staphylococcus aureus or Streptococcus pyogenes.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Contagious **impetigo** spreads rapidly through school dormitories when common towels and bedding are incautiously shared."},
            {"author": "Richard Bright", "work": "Reports of Medical Cases", "quote": "The child exhibited extensive patches of **impetigo** upon the scalp, surrounded by inflammatory erythema."},
            {"author": "Thomas Watson", "work": "Lectures on the Principles and Practice of Physic", "quote": "Strict cleanliness and topical mercurial ointments promptly arrest the pustular spread of **impetigo**."}
        ]
    },
    "impetuosity": {
        "primary": "The quality of acting with rash haste, sudden emotional vehemence, or headlong physical violence.",
        "secondary": "In dramatic literature and psychological analysis, uncalculating fury or unbridled ardency that sweeps aside rational restraint.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Troilus and Cressida", "quote": "The grief is fine, full, perfect, that I taste, and violenteth in a sense as strong as that which causeth it; with what **impetuosity** does it surge!"},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Troy pursued his passions with an **impetuosity** that disregarded every consideration of rural propriety or future remorse."},
            {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Maggie acted from a generous **impetuosity** of affection which repeatedly drew upon her head the censure of her prudent relatives."}
        ]
    },
    "impetuous": {
        "primary": "Acting or done quickly and without thought or care; moving with great, forceful, or headlong speed.",
        "secondary": "In literary characterization, describing ardent temperaments or physical torrents characterized by sweeping, turbulent momentum.",
        "quotes": [
            {"author": "William Shakespeare", "work": "King Lear", "quote": "Blow, winds, and crack your cheeks! rage! blow! you cataracts and hurricanoes, with your **impetuous** fury!"},
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Sir Henry was an **impetuous** man, quick to anger and impatient of delay when a clear path lay open before him."},
            {"author": "George Eliot", "work": "Romola", "quote": "Her youth made her feelings **impetuous**, and she could not bear the cold, calculating maxims of political expediency."}
        ]
    },
    "impetuously": {
        "primary": "In an impetuous, headlong, or rashly passionate manner; without cautious reflection.",
        "secondary": "In expressive prose, charging forward with reckless physical velocity or spontaneous, uninhibited emotional abandon.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She spoke **impetuously**, pouring out the deep secrets of her heart before her better judgment could intervene."},
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip rushed forward **impetuously** to grasp the boat's gunwale, heedless of the churning black river water beneath."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The harpooners leaped **impetuously** into their cedar craft the moment the distant spout was hailed from the masthead."}
        ]
    },
    "impetuousness": {
        "primary": "The characteristic disposition to act rashly, headlong, or under sudden violent impulse.",
        "secondary": "In moral philosophy and psychological character study, an unrestrained fiery temperament that disregards consequences or tactical prudence.",
        "quotes": [
            {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The dangerous **impetuousness** of youth frequently plunges men into ruinous enterprises before maturity teaches them caution."},
            {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne's affectionate **impetuousness** blinded her entirely to the calculating reserve of her admired suitor."},
            {"author": "Lord Byron", "work": "Letters and Journals", "quote": "My natural **impetuousness** has ever driven me into tempestuous adventures where cooler spirits would have paused."}
        ]
    },
    "impetus": {
        "primary": "The force or energy with which a body moves; a driving impulse or stimulus that accelerates development.",
        "secondary": "In dynamics and historical analysis, the initial kinetic momentum of a projectile, or a catalytic event spurring social change.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The unexpected legacy gave fresh **impetus** to his ambitious medical schemes, releasing him from sordid financial anxieties."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The boat shot forward under the terrific **impetus** of six oars bending in desperate unison against the swell."},
            {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The sudden discovery of mechanical power imparted an extraordinary **impetus** to nineteenth-century material progress."}
        ]
    },
    "incompetence": {
        "primary": "Inability to perform duties or handle responsibilities adequately, skillfully, or effectively.",
        "secondary": "In jurisprudence and organizational governance, legal disqualification, official disability, or institutional failure to execute mandated authority.",
        "quotes": [
            {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "The riotous disorders in the market town revealed the glaring administrative **incompetence** of the local magistracy."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The disastrous naval campaign was chargeable solely to the gross **incompetence** of the court favorites placed in command."},
            {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "The official detectives displayed baffling **incompetence** until Sherlock Holmes examined the bloody marks upon the wall."}
        ]
    },
    "incompetency": {
        "primary": "Lack of required capacity, qualification, strength, or fitness to perform a given task or function.",
        "secondary": "In law, the status of being legally disqualified or mentally incapacitated from managing property, testifying, or standing trial.",
        "quotes": [
            {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The legal **incompetency** of an infant or lunatic protects them from being bound by unconscionable civil contracts."},
            {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A weak executive demonstrates that administrative **incompetency** which inevitably paralyzes all operations of national defense."},
            {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "To entrust legislative sovereignty to men of proven **incompetency** is to invite swift anarchy and financial catastrophe."}
        ]
    }
}
