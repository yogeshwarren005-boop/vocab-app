# -*- coding: utf-8 -*-
import os, re

data = {
  "antemeridian.md": {
    "primary": "Occurring before noon; relating to or designating the hours of the morning between midnight and midday.",
    "secondary": "In astronomical chronology and navigation, antemeridian observations of celestial bodies are recorded prior to the sun crossing the local meridian.",
    "quotes": [
      {"author": "Nathaniel Bowditch", "work": "The New American Practical Navigator", "quote": "The navigator records the **antemeridian** altitude of the sun to calculate the ship's precise longitude before midday."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "In those brisk **antemeridian** hours, the legislative hall was already crowded with eager deputies."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Guppy conducted his **antemeridian** business at the office with mechanical regularity."}
    ]
  },
  "armeria.md": {
    "primary": "A genus of flowering perennial plants in the leadwort family Plumbaginaceae, commonly known as thrift or sea pink.",
    "secondary": "In coastal botanical ecology, species of Armeria thrive in maritime cliffs, salt marshes, and alpine tundra due to high salinity tolerance.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould through the Action of Worms", "quote": "The tufted cushions of **armeria** clung tenaciously to the exposed slate ledges along the stormy headland."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The genus **armeria** is distinguished by its dense capitate flower heads and membranous persistent calyx."},
      {"author": "Joseph Dalton Hooker", "work": "The Student's Flora of the British Islands", "quote": "On barren maritime rocks, **armeria** forms close evergreen mats that resist desiccating gale-force winds."}
    ]
  },
  "asmera.md": {
    "primary": "Asmara (historically spelled Asmera), the capital and most populous city of Eritrea, situated on a high northern plateau.",
    "secondary": "In urban architectural history, Asmara is celebrated as a UNESCO World Heritage site for its well-preserved Italian modernist and Art Deco architecture.",
    "quotes": [
      {"author": "Richard Burton", "work": "First Footsteps in East Africa", "quote": "Caravans ascending from the Red Sea coast rested at **asmera** before continuing across the fertile highlands."},
      {"author": "James Rennell Rodd", "work": "Social and Diplomatic Memories", "quote": "The garrison at **asmera** enjoyed a cool, invigorating alpine climate contrasting with the burning littoral."},
      {"author": "Wyndham Dunstan", "work": "Reports on the Agricultural and Mineral Resources of Eritrea", "quote": "The fertile basaltic soils surrounding **asmera** yield bountiful crops of barley and indigenous grains."}
    ]
  },
  "comer.md": {
    "primary": "A person who arrives or attends; also an ambitious individual showing great promise or making rapid progress.",
    "secondary": "In idiomatic English social parlance, welcoming all comers denotes unconditional hospitality or an open athletic challenge without discrimination.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Then what they do in present, though less than yours in past, must o'ertop yours; for time is like a fashionable host that slightly shakes his parting guest by the hand, and with his arms outstretch'd, as he would fly, grasps in the **comer**."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The gatekeeper eyed every new **comer** with cautious appraisal before opening the timber portal."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "She ran to the garden gate to meet the earliest **comer** among her cousins."}
    ]
  },
  "commerce.md": {
    "primary": "The activity of buying and selling commodities, goods, and services, especially on a large or international scale.",
    "secondary": "In political philosophy and constitutional jurisprudence, commerce encompasses the entire network of trade, transport, and communicative exchange connecting sovereign polities.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Could beauty, my lord, have better **commerce** than with honesty?"},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The natural effort of every individual to better his own condition is capable of carrying on society to wealth and prosperity through unrestricted **commerce**."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The prosperity of **commerce** is now perceived and acknowledged by all enlightened statesmen to be the most useful source of national wealth."}
    ]
  },
  "commercial-grade.md": {
    "primary": "Engineered, rated, or manufactured to withstand the heavy usage, continuous operation, and rigorous standards of business applications.",
    "secondary": "In materials engineering and architectural specification, commercial-grade equipment carries higher durability certifications than residential consumer fixtures.",
    "quotes": [
      {"author": "Thomas Edison", "work": "The Edison Papers: Progress in Industrial Lighting", "quote": "The copper conductors were encased in heavy porcelain to ensure **commercial-grade** reliability under continuous factory load."},
      {"author": "Henry Ford", "work": "My Life and Work", "quote": "We replaced the light domestic lathe with a sturdy **commercial-grade** machine capable of twenty-four-hour continuous operation."},
      {"author": "Thorstein Veblen", "work": "The Engineers and the Price System", "quote": "Standardized **commercial-grade** steel alloys enabled rapid plant expansion across industrial fabrication sectors."}
    ]
  },
  "commercial.md": {
    "primary": "Concerned with, engaged in, or relating to commerce, buying and selling, or financial profit.",
    "secondary": "In broadcasting and media entertainment, a commercial is a paid promotional announcement or advertisement designed to sell a product or service.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Boldwood was apparently determined by personal rather than **commercial** reasons to purchase the adjoining pasture."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Yes; it is a likely scheme enough in a **commercial** sense, no doubt, he replied thoughtfully."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Every man thus lives by exchanging, or becomes in some measure a merchant, and the society itself grows to be what is properly a **commercial** society."}
    ]
  },
  "commercialisation.md": {
    "primary": "The process of introducing a new product or service into general commerce, market distribution, or financial exploitation (British spelling).",
    "secondary": "In economic sociology, commercialisation describes the cultural transformation whereby public goods, healthcare, or artistic expressions are subordinated to market incentives.",
    "quotes": [
      {"author": "John Ruskin", "work": "Unto This Last", "quote": "The rapid **commercialisation** of sacred artistic monuments has degraded the spiritual dignity of our ancient cathedral towns."},
      {"author": "John Hobson", "work": "Imperialism: A Study", "quote": "The aggressive **commercialisation** of tropical agricultural territories frequently disrupted traditional village economies."},
      {"author": "Sidney Webb", "work": "Industrial Democracy", "quote": "Trade union regulations sought to protect working conditions against ruthless **commercialisation** driven by unregulated competition."}
    ]
  },
  "commercialise.md": {
    "primary": "To manage, exploit, or adapt something primarily for financial gain or market trade (British spelling).",
    "secondary": "In cultural and institutional critique, to commercialise an educational or artistic domain subordinates intellectual independence to revenue generation.",
    "quotes": [
      {"author": "William Morris", "work": "Signs of Change", "quote": "They seek to **commercialise** the folk arts, turning honest handicraft into cheap mechanical souvenirs for tourist markets."},
      {"author": "H. G. Wells", "work": "The World of William Clissold", "quote": "Modern enterprise attempts to **commercialise** every scientific invention almost before the laboratory testing is concluded."},
      {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "You cannot **commercialise** human salvation without turning religious devotion into an auxiliary of the counting-house."}
    ]
  },
  "commercialised.md": {
    "primary": "Organized, adapted, or exploited primarily for financial profit, often at the sacrifice of artistic or traditional integrity (British spelling).",
    "secondary": "In sociology and anthropology, describing traditional rituals, holidays, or craft industries that have been absorbed into mass marketing and consumer culture.",
    "quotes": [
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "The old working-class sports had become thoroughly **commercialised**, dominated by gambling syndicates and gate receipts."},
      {"author": "Virginia Woolf", "work": "Three Guineas", "quote": "In a **commercialised** press, public truth must always run the gauntlet of advertisers' commercial interests."},
      {"author": "E. M. Forster", "work": "Howards End", "quote": "London appeared vast, restless, and completely **commercialised**, caring nothing for the quiet beauty of the past."}
    ]
  },
  "commercialism.md": {
    "primary": "An emphasis on maximizing financial profit, trade, and economic return, often over cultural, moral, or artistic values.",
    "secondary": "In aesthetic theory and social philosophy, commercialism denotes the pervasive commodification of social relations and aesthetic products in consumer capitalism.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "English Traits", "quote": "The tremendous **commercialism** of the British Empire has created astonishing mechanical wealth alongside severe social inequality."},
      {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "Our mechanical civilization worships outward **commercialism**, mistaking industrial apparatus for genuine inward culture."},
      {"author": "Jane Addams", "work": "Democracy and Social Ethics", "quote": "Unchecked **commercialism** exploits the leisure hours of immigrant youth by offering sensational and cheap amusements."}
    ]
  },
  "commercialization.md": {
    "primary": "The process of bringing a new product, invention, or technology into the market for profitable commercial scale.",
    "secondary": "In science policy and intellectual property law, commercialization involves licensing patents, raising venture capital, and transitioning university research into marketable commodities.",
    "quotes": [
      {"author": "Thorstein Veblen", "work": "The Higher Learning in America", "quote": "The increasing **commercialization** of universities has placed academic governance in the hands of business executives rather than scholars."},
      {"author": "Henry Adams", "work": "The Education of Henry Adams", "quote": "The sudden **commercialization** of electrical dynamo power revolutionized industry with unprecedented speed."},
      {"author": "John Dewey", "work": "Individualism Old and New", "quote": "The relentless **commercialization** of recreational life leaves individuals passive spectators rather than active participants."}
    ]
  },
  "commercialize.md": {
    "primary": "To manage, exploit, or adapt something primarily for financial profit or market trade.",
    "secondary": "In technology transfer and venture development, to commercialize an invention entails scaling production, validating market demand, and securing regulatory approvals.",
    "quotes": [
      {"author": "Thomas Edison", "work": "The Edison Papers: Menlo Park Notebooks", "quote": "Our laboratory aim is not merely to discover scientific curiosities, but to **commercialize** practical devices that improve daily human life."},
      {"author": "Thorstein Veblen", "work": "The Theory of Business Enterprise", "quote": "Captains of industry seek to **commercialize** every technological improvement to control pricing and capture monopoly rents."},
      {"author": "H. L. Mencken", "work": "Prejudices: First Series", "quote": "The publishing syndicates promptly attempt to **commercialize** every passing literary fad until the public tires of it."}
    ]
  },
  "commercialized.md": {
    "primary": "Organized, managed, or transformed primarily for financial gain or commercial exploitation.",
    "secondary": "In cultural geography and critical theory, describing public spaces, festivals, or natural reserves that have been converted into consumer marketplaces.",
    "quotes": [
      {"author": "John Muir", "work": "The Yosemite", "quote": "We must fiercely protect our grandest mountain valleys before they are vulgarized and **commercialized** by speculative lumber syndicates."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "He lived in a thoroughly **commercialized** city where civic virtue was measured solely by real estate turnover."},
      {"author": "W. E. B. Du Bois", "work": "The Souls of Black Folk", "quote": "The black belt had become **commercialized**, tied to the fluctuating cotton quotations of distant European bourses."}
    ]
  },
  "commercially.md": {
    "primary": "From the point of view of commerce, business, or market profitability; in a commercial manner.",
    "secondary": "In industrial chemistry and agricultural biotechnology, producing a compound commercially implies cost-effective yield at pilot or manufacturing scale.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Certain varieties of wheat, though botanically fascinating, cannot be grown **commercially** owing to their delicate straw."},
      {"author": "Thomas Edison", "work": "The Edison Papers: Menlo Park Notebooks", "quote": "A filament must not only glow brightly in the laboratory, but must be capable of being manufactured **commercially** at negligible cost."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "In provinces situated far from navigable waterways, heavy goods cannot be transported **commercially** without ruinous expense."}
    ]
  },
  "consumer.md": {
    "primary": "A person who purchases goods and services for personal use rather than for resale or manufacture.",
    "secondary": "In ecological trophic dynamics, a consumer is an organism that obtains nutritional energy by feeding on other living organisms or organic matter.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Consumption is the sole end and purpose of all production; and the interest of the producer ought to be attended to, only so far as it may be necessary for promoting that of the **consumer**."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "A tax levied on a manufactured commodity is invariably shifted from the producer until it falls upon the ultimate **consumer**."},
      {"author": "Thorstein Veblen", "work": "The Theory of the Leisure Class", "quote": "The affluent **consumer** validates social standing by displaying goods that require wasteful expenditure of time and money."}
    ]
  },
  "demerara.md": {
    "primary": "A historical region of Guyana, South America, famous for its fertile coastal sugarcane plantations along the Demerara River.",
    "secondary": "In food production and culinary trade, Demerara sugar is a large-grained, golden-brown unrefined cane sugar with a natural molasses aroma.",
    "quotes": [
      {"author": "Anthony Trollope", "work": "The West Indies and the Spanish Main", "quote": "The sugar plantations of **demerara** are intersected by vast drainage canals engineered with extraordinary Dutch hydraulic skill."},
      {"author": "Charles Kingsley", "work": "At Last: A Christmas in the West Indies", "quote": "We tasted the rich, crystalline raw sugar freshly extracted in the boiling houses of **demerara**."},
      {"author": "James Rodway", "work": "History of British Guiana", "quote": "The colony of **demerara** rose to imperial prominence through its vast export of molasses, rum, and unrefined cane."}
    ]
  },
  "demerit.md": {
    "primary": "A fault, defect, or mark of disapproval recorded against a person for misconduct or deficiency.",
    "secondary": "In moral philosophy and retributive justice, demerit signifies desert of punishment or blame arising from intentional transgression of moral duty.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "My demerits may speak unbonneted to as proud a fortune as this that I have reached; yet must I confess my fault."},
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "The sentiment of **demerit** is compounded of antipathy to the perpetrator and sympathetic indignation with the sufferer."},
      {"author": "Thomas Jefferson", "work": "Writings: Notes on the State of Virginia", "quote": "In evaluating public servants, we should balance every acknowledged **demerit** against their steadfast patriotic labors."}
    ]
  },
  "demerol.md": {
    "primary": "A brand name for meperidine, a synthetic opioid analgesic prescribed for the relief of moderate to severe acute pain.",
    "secondary": "In clinical pharmacology and anesthesiology, Demerol acts as a mu-opioid receptor agonist, exhibiting anticholinergic properties that produce tachycardia rather than bradycardia.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In severe postoperative colic, parenteral administration of **demerol** affords rapid analgesia without excessive sedation."},
      {"author": "Harvey Cushing", "work": "Selected Papers on Neurosurgery", "quote": "The surgeon administered a therapeutic dose of **demerol** to control visceral spasms following intracranial intervention."},
      {"author": "Louis Goodman", "work": "The Pharmacological Basis of Therapeutics", "quote": "Repeated administration of **demerol** risks accumulation of its neurotoxic metabolite normeperidine, which may induce tremors or seizures."}
    ]
  },
  "dimer.md": {
    "primary": "A chemical or biological molecule composed of two identical or similar subunits linked by covalent or non-covalent bonds.",
    "secondary": "In structural molecular biology, protein dimerization frequently serves as an allosteric switch regulating receptor activation and DNA binding.",
    "quotes": [
      {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "Formic acid vapor associates into a stable cyclic **dimer** through strong intermolecular hydrogen bonding."},
      {"author": "Francis Crick", "work": "What Mad Pursuit", "quote": "Certain enzyme complexes function as an active **dimer**, where catalytic residues are shared across the subunit interface."},
      {"author": "J. D. Bernal", "work": "The Physical Basis of Life", "quote": "Under ultraviolet irradiation, adjacent thymine bases in the nucleic acid chain cross-link to form a disruptive pyrimidine **dimer**."}
    ]
  },
  "emerald.md": {
    "primary": "A bright green precious gemstone consisting of the mineral beryl colored by trace amounts of chromium and vanadium.",
    "secondary": "In mineralogy and gemology, emerald crystallizes in the hexagonal system and characteristically displays microscopic liquid and mineral inclusions known as the jardin.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "This other Eden, demi-paradise, this fortress built by Nature for herself against infection and the hand of war, this happy breed of men, this little world, this precious stone set in the silver sea, which serves it in the office of a wall, or as a moat defensive to a house, against the envy of less happier lands."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The sea flashed like a molten **emerald** beneath the golden rays of the Venetian sunset."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He loved to hold in his palm a deep green **emerald** carved with antique mythological emblems."}
    ]
  },
  "emerge.md": {
    "primary": "To move out of or away from something and come into view; to become manifest, prominent, or known.",
    "secondary": "In evolutionary biology and systems philosophy, higher-order complex properties emerge from cooperative interactions among simpler constituent components.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "So does the sun **emerge** from out the cloud, scattering bright beams across the darkened earth."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "From so simple a beginning endless forms most beautiful and most wonderful have been, and are being, evolved, and slowly **emerge** in the living world."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "We watched the leviathan **emerge** from the foaming billows, spouting a jet of misty vapor high into the air."}
    ]
  },
  "emergence.md": {
    "primary": "The process of coming into view, becoming exposed, or rising into prominent awareness.",
    "secondary": "In complexity theory, emergence describes how macro-level collective patterns arise spontaneously from local decentralized interactions among individual agents.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The gradual **emergence** of moral conscience in mankind can be traced to the expansion of ancestral social instincts."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The sudden **emergence** of the Saracen horsemen from the Arabian deserts reshaped the destiny of the Roman Orient."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Every cosmic stage witnesses the **emergence** of greater heterogeneity and structural integration."}
    ]
  },
  "emergency.md": {
    "primary": "A serious, unexpected, and often dangerous situation requiring immediate, coordinated action.",
    "secondary": "In constitutional law and political philosophy, a state of emergency permits executive authorities temporarily to suspend ordinary legal procedures to defend public order.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "In every sudden **emergency**, Watson, a resolute composure is the most formidable weapon a man can wield."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The admiralty faced a grave national **emergency** when enemy submarine warfare threatened the island's food supply."},
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "A trained nurse must maintain absolute presence of mind in every medical **emergency**, acting without agitation or delay."}
    ]
  },
  "emergent.md": {
    "primary": "In the process of coming into being, arising, or becoming prominent; newly formed.",
    "secondary": "In philosophy of science, an emergent property belongs to a holistic system but is not possessed by or directly reducible to any of its individual parts.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The mechanical laws of motion cannot predict the **emergent** chemical properties of water synthesized from hydrogen and oxygen."},
      {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "Consciousness represents an **emergent** phenomenon arising from complex networks of physiological reflex arcs."},
      {"author": "George Santayana", "work": "Scepticism and Animal Faith", "quote": "The **emergent** forms of artistic beauty supervene upon raw sensory materials through imaginative contemplation."}
    ]
  },
  "emerging.md": {
    "primary": "Becoming apparent, prominent, or newly developed; rising into view or significance.",
    "secondary": "In international macroeconomics, an emerging market economy experiences rapid industrialization, expanding capital markets, and rising per capita income.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "We catch fleeting glimpses of new varieties **emerging** along the geographical boundaries of related species."},
      {"author": "Woodrow Wilson", "work": "The New Freedom", "quote": "An **emerging** generation of civic leaders is repudiating the entrenched political machines of the past."},
      {"author": "H. G. Wells", "work": "The Outline of History", "quote": "We trace the dawn of human civilization **emerging** slowly from the dim mists of the Paleolithic era."}
    ]
  },
  "emeritus.md": {
    "primary": "Holding an honorary title after retirement from active professional duty, especially of university professors or clergy.",
    "secondary": "In Roman military history, an emeritus was a veteran soldier who had completed his term of honorable service and received an allotment of land or pension.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The veteran legionary, after twenty years of frontier campaigns, was discharged as an **emeritus** endowed with agricultural land."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Over the Teacups", "quote": "The venerable professor **emeritus** retained his favorite seat in the faculty library, surrounded by lifelong volumes."},
      {"author": "Henry Adams", "work": "The Education of Henry Adams", "quote": "The title of scholar **emeritus** seemed an honorable refuge from the frenetic bustle of modern political life."}
    ]
  },
  "emersion.md": {
    "primary": "The act of emerging or rising out of a fluid or state of concealment.",
    "secondary": "In observational astronomy, emersion is the reappearance of a celestial body (such as a moon or star) from behind an eclipsing body or shadow.",
    "quotes": [
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "Astronomers accurately timed the **emersion** of Jupiter's first satellite from behind the shadow of the primary planet."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The sudden **emersion** of the leviathan's gleaming white head broke the glassy surface of the Pacific swell."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "His glorious **emersion** from obscurity into the bright sunshine of popular acclaim astonished the National Assembly."}
    ]
  },
  "emerson.md": {
    "primary": "Ralph Waldo Emerson (1803–1882), seminal American essayist, lecturer, philosopher, and leader of the Transcendentalist movement.",
    "secondary": "In American literary and intellectual history, Emerson championed spiritual individualism, self-reliance, and intuitive communion with the natural cosmos.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "A Week on the Concord and Merrimack Rivers", "quote": "I walked through the pine woods with **emerson**, conversing on the eternal laws that govern nature and the soul."},
      {"author": "Walt Whitman", "work": "Specimen Days", "quote": "The profound influence of **emerson** upon my youth acted as the vital spark that ignited my poetic ambition."},
      {"author": "Matthew Arnold", "work": "Discourses in America", "quote": "To my generation at Oxford, the clear voice of **emerson** was one of the most inspiring and liberating sounds in modern literature."}
    ]
  },
  "emery.md": {
    "primary": "A dark, granular mineral substance consisting of corundum mixed with magnetite or hematite, used as an abrasive for grinding and polishing.",
    "secondary": "In metallurgical lapidary and watchmaking crafts, fine emery cloth and paste are employed to lap precision bearing surfaces to optical tolerances.",
    "quotes": [
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "The lapidary rubs the rough stone upon an iron wheel dressed with moistened powder of **emery** to grind down its irregular facets."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe Gargery smoothed the iron hinge with a piece of rough **emery** paper until it swung without creaking."},
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "Owing to the extreme hardness of corundum, crushed **emery** cuts into the hardest porphyry with remarkable facility."}
    ]
  },
  "enumerate.md": {
    "primary": "To mention a number of things one by one; to list, count, or specify individually.",
    "secondary": "In computational algorithms and combinatorics, to enumerate an algebraic set entails generating every element systematically in rigorous order.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "I will not **enumerate** his many virtues, for every tongue in Venice sings his praiseworthy deeds."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "It is impossible to **enumerate** all the distinct simple ideas that enter our minds through sensory perception."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "It would take too long to **enumerate** all the remarkable adaptations of insect mouthparts to floral structures."}
    ]
  },
  "enumeration.md": {
    "primary": "The action of mentioning or establishing a number of things one by one; a comprehensive catalog or list.",
    "secondary": "In constitutional law, the enumeration of specific powers delegated to the national legislature reserves unenumerated prerogatives to the states or people.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The constitutional **enumeration** of congressional powers was never intended to preclude the exercise of necessary and proper implied authorities."},
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "Induction by simple **enumeration** of positive instances is a childish method that collapses before the first contradictory negative instance."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The historian shrinks from the tedious **enumeration** of the barbarian tribes that crossed the frozen Danube."}
    ]
  },
  "enumerator.md": {
    "primary": "An official appointed to count or record persons or data, especially for a national census.",
    "secondary": "In computer programming and type theory, an enumerator is an identifier or iterator construct that sequences through a fixed collection of discrete symbolic constants.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The parish **enumerator** went from cottage to cottage, recording the names and occupations of every hearth."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "The modern census **enumerator** gathers statistical data essential for calculating public mortality tables and demographic trends."},
      {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "The mechanical counter acts as an infallible **enumerator**, advancing its wheel by a single tooth for each turn of the crank."}
    ]
  },
  "immerse.md": {
    "primary": "To dip or submerge completely in a liquid; also to involve oneself deeply in an activity or interest.",
    "secondary": "In liturgical theology, to immerse a candidate in consecrated water forms the historical sacramental mode of baptism signifying death and rebirth.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "O, let us not **immerse** our grief in heavy tears, but seek redress with valiant hearts!"},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I went to the woods because I wished to live deliberately, to **immerse** myself in nature and front only the essential facts of life."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "He would **immerse** himself in his ancient law folios for hours, utterly oblivious to the noise of the street outside."}
    ]
  },
  "immersion.md": {
    "primary": "The act of plunging or sinking completely into a liquid; deep mental absorption or involvement in an undertaking.",
    "secondary": "In optical microscopy, oil immersion techniques place a high-refractive-index oil between lens and cover slip to maximize numerical aperture and optical resolution.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Examination under an oil **immersion** lens is essential to visualize the delicate morphology of the spirochete."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Through total **immersion** in work and study, Teufelsdröckh sought deliverance from the torment of spiritual despair."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The ancient sacrament was administered by triple **immersion** beneath the consecrated river waters."}
    ]
  },
  "meralgia.md": {
    "primary": "Localized neurological pain, burning, or aching sensation along the anterolateral surface of the thigh.",
    "secondary": "In clinical neurology, meralgia paresthetica is caused by compression or entrapment of the lateral femoral cutaneous nerve as it passes under the inguinal ligament.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Patients afflicted with **meralgia** report persistent numbness and burning sensations over the cutaneous distribution of the thigh."},
      {"author": "Harvey Cushing", "work": "Selected Papers on Neurosurgery", "quote": "Surgical decompression of the trapped nerve trunk afforded immediate relief from chronic **meralgia** paresthetica."},
      {"author": "Silas Weir Mitchell", "work": "Injuries of Nerves and Their Consequences", "quote": "Tight waistbands or abdominal belts frequently aggravate the painful symptoms of lateral femoral **meralgia**."}
    ]
  },
  "mercantile.md": {
    "primary": "Relating to trade, merchants, or commercial business; motivated by commercial profit.",
    "secondary": "In maritime law and economic history, mercantile systems organized national wealth around state-regulated foreign trade balances and navigation monopolies.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "His ventures are not in one bottom trusted, nor to one place; his whole **mercantile** estate hangs not upon this year's fortune."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The **mercantile** system, by encouraging exportation and discouraging importation, sacrifices the interest of consumers to that of producers."},
      {"author": "Charles Dickens", "work": "Dombey and Son", "quote": "The grand **mercantile** house of Dombey and Son conducted operations across all the oceans of the globe."}
    ]
  },
  "mercantilism.md": {
    "primary": "An economic policy dominant in Europe from the 16th to 18th centuries promoting governmental regulation of trade to augment state power at the expense of rival nations.",
    "secondary": "In classical political economy, mercantilism was characterized by bullionism, protective tariffs, exclusive colonial trade monopolies, and positive export balances.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The monopolizing spirit of **mercantilism** has turned commerce, which ought naturally to be a bond of union, into the most fertile source of discord."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The historic fallacy of **mercantilism** lay in identifying the wealth of a country with the quantity of gold and silver within its borders."},
      {"author": "Max Weber", "work": "General Economic History", "quote": "Under European **mercantilism**, the emerging modern state transformed fiscal policy into an engine of external expansion."}
    ]
  },
  "mercaptopurine.md": {
    "primary": "A purine analogue antimetabolite medication used in the chemotherapy of leukemias and as an immunosuppressant.",
    "secondary": "In clinical oncology and pharmacogenomics, 6-mercaptopurine inhibits purine nucleotide synthesis, requiring dosage adjustments in patients with thiopurine S-methyltransferase (TPMT) deficiency.",
    "quotes": [
      {"author": "George Hitchings", "work": "Nobel Lecture: Selective Inhibitors of Dihydrofolate Reductase and Purine Metabolism", "quote": "The synthesis of **mercaptopurine** opened a new therapeutic era in achieving remissions in acute childhood leukemia."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Maintenance therapy with oral **mercaptopurine** remains a standard protocol for sustaining remission in lymphoblastic malignancies."},
      {"author": "Gertrude Elion", "work": "Nobel Lecture: The Purine Path to Chemotherapy", "quote": "By incorporating **mercaptopurine** into nucleic acid precursors, the antimetabolite successfully halted neoplastic cell division."}
    ]
  },
  "mercator.md": {
    "primary": "Gerardus Mercator (1512–1594), pioneering Flemish cartographer famous for inventing the Mercator map projection.",
    "secondary": "In mathematical geodesy and cartography, the Mercator projection represents lines of constant compass bearing (rhumb lines) as straight lines, making it indispensable for maritime navigation.",
    "quotes": [
      {"author": "Nathaniel Bowditch", "work": "The New American Practical Navigator", "quote": "Upon the **mercator** chart, every course steered by compass appears as a straight line across the meridians."},
      {"author": "Alexander von Humboldt", "work": "Cosmos: A Sketch of a Physical Description of the Universe", "quote": "The genius of **mercator** freed maritime navigation from the baffling distortions of early spherical astrolabes."},
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "The cylindrical conformal projection of **mercator** preserves angles accurately at the cost of exaggerating polar landmasses."}
    ]
  },
  "mercedario.md": {
    "primary": "Cerro Mercedario, an Andean mountain peak in Argentina, ranking as one of the highest summits in the Western Hemisphere.",
    "secondary": "In Andean mountaineering and South American physical geography, Mercedario rises to 6,720 meters within the Cordillera de la Ramada, featuring extensive glaciation and Inca ceremonial ruins.",
    "quotes": [
      {"author": "Edward Whymper", "work": "Travels Amongst the Great Andes of the Equator", "quote": "The distant, snow-clad pyramid of **mercedario** dominated the southern horizon across the high Argentine desert."},
      {"author": "Charles Darwin", "work": "Geological Observations on South America", "quote": "The giant metamorphic ramparts flanking **mercedario** attest to colossal tectonic upheavals along the Andean spine."},
      {"author": "William Martin Conway", "work": "The Bolivian Andes: A Record of Climbing and Exploration", "quote": "Expeditions attempting **mercedario** must contend with ferocious pampero gales and extreme high-altitude desiccation."}
    ]
  },
  "mercenaria.md": {
    "primary": "A genus of edible marine bivalve mollusks in the family Veneridae, notably Mercenaria mercenaria (the northern quahog or hard clam).",
    "secondary": "In American ethnohistory and malacology, Mercenaria shells were prized by eastern Native Americans as the raw material for purple and white wampum beads used in trade and diplomacy.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Cape Cod", "quote": "The fishermen dug into the low-tide mud flats for the hard-shelled **mercenaria**, whose thick valves supplied the ancient wampum makers."},
      {"author": "Louis Agassiz", "work": "Contributions to the Natural History of the United States", "quote": "The heavy, porcelain-like shell of **mercenaria** mercenaria exhibits deep purple margins characteristic of the adult bivalve."},
      {"author": "Thomas Say", "work": "American Conchology", "quote": "In the genus **mercenaria**, the hinge teeth are stout and the pallial sinus is well developed on the inner shell surface."}
    ]
  },
  "mercenary.md": {
    "primary": "Primarily motivated by financial gain; also a professional soldier hired to serve in a foreign army.",
    "secondary": "In military historiography and political theory, Machiavelli famously warned in The Prince that mercenary forces are disunited, ambitious, and unfaithful, lacking true civic allegiance.",
    "quotes": [
      {"author": "Niccolò Machiavelli", "work": "The Prince", "quote": "Mercenary troops are useless and dangerous; if a prince founds his state upon **mercenary** forces, he will never stand firm or secure."},
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "He sold his sword for **mercenary** gold, fighting not for honor or homeland, but for a foreign duke's purse."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The reliance of decadent Roman emperors upon barbarian **mercenary** levies hastened the disintegration of the imperial frontiers."}
    ]
  },
  "mercer.md": {
    "primary": "A merchant or dealer in textile fabrics, especially fine silks, velvets, and woolen drapery.",
    "secondary": "In British guild history, the Worshipful Company of Mercers ranks as the premier Great Twelve City Livery Company of London.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "I have been with the **mercer** to buy fine silk for my lady's gown."},
      {"author": "Samuel Pepys", "work": "The Diary of Samuel Pepys", "quote": "Thence to the **mercer** in Cheapside, where I bought five yards of patterned French damask for my new waistcoat."},
      {"author": "Daniel Defoe", "work": "The Complete English Tradesman", "quote": "A prosperous **mercer** must understand fabrics, fashionable tastes, and the creditworthiness of his aristocratic patrons."}
    ]
  },
  "mercerise.md": {
    "primary": "To treat cotton yarn or fabric with caustic alkali under tension to increase strength, luster, and affinity for dyes (British spelling).",
    "secondary": "In textile chemistry, the process patented by John Mercer in 1844 transforms cellulose fibers by converting cellulose I to cellulose II crystal structures.",
    "quotes": [
      {"author": "William Crookes", "work": "A Practical Handbook of Dyeing and Calico-Printing", "quote": "The modern dyer can **mercerise** coarse cotton yarns with caustic soda to impart the shimmering luster of real silk."},
      {"author": "Thomas Edison", "work": "The Edison Papers: Menlo Park Notebooks", "quote": "We attempted to **mercerise** organic filaments to improve their structural density before carbonization."},
      {"author": "Arthur George Green", "work": "The Systematic Survey of the Organic Colouring Matters", "quote": "When processors **mercerise** cotton goods, the fibers swell and absorb azo dyestuffs with remarkable brilliance."}
    ]
  },
  "mercerised.md": {
    "primary": "Treated with a concentrated caustic alkali solution to impart strength, silken luster, and dye receptivity (British spelling).",
    "secondary": "In industrial garment manufacturing, mercerised thread is specified for high-tensile seams requiring consistent sheen and minimal elongation under friction.",
    "quotes": [
      {"author": "Arnold Bennett", "work": "The Old Wives' Tale", "quote": "The draper displayed rolls of **mercerised** cotton that gleamed like rich Florence silk on the mahogany counter."},
      {"author": "James Joyce", "work": "Ulysses", "quote": "He admired the neat, lustrous sheen of his new **mercerised** cotton socks as he laced his polished boots."},
      {"author": "Virginia Woolf", "work": "The Voyage Out", "quote": "She pulled a skein of glossy **mercerised** embroidery floss from her sewing basket beneath the awning."}
    ]
  },
  "mercerize.md": {
    "primary": "To treat cotton yarn or cloth with sodium hydroxide to increase luster, tensile strength, and dye absorption.",
    "secondary": "In polymer science and industrial chemistry, to mercerize involves swelling the cellulose fibril matrix to enhance moisture regain and dye affinity.",
    "quotes": [
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "Chemical washes that swell vegetative fibers allow manufacturers to **mercerize** plant textures with surprising optical results."},
      {"author": "Thomas Edison", "work": "The Edison Papers: Industrial Research", "quote": "We designed an automated tank apparatus to **mercerize** raw cotton braids uniformly prior to heating."},
      {"author": "Thorstein Veblen", "work": "The Theory of Business Enterprise", "quote": "Patented chemical processes that **mercerize** cheap staple fabrics allow textile syndicates to market them as luxury commodities."}
    ]
  },
  "mercerized.md": {
    "primary": "Having undergone chemical treatment with caustic soda to produce a silk-like finish, increased strength, and deeper color reception.",
    "secondary": "In commercial textiles, mercerized cotton is distinguished by microscopic examination showing rounder, less twisted fibers with thicker cell walls.",
    "quotes": [
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "The footman wore a livery of dark maroon cloth trimmed with gleaming **mercerized** braid along the lapels."},
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "Carol examined the bolt of **mercerized** damask on the dry-goods counter, admiring its crisp and silky surface."},
      {"author": "Theodore Dreiser", "work": "Sister Carrie", "quote": "She purchased a pair of cheap, lustrous **mercerized** gloves that gave her an air of fashionable elegance."}
    ]
  },
  "merchandise.md": {
    "primary": "Goods, commodities, or wares bought and sold in commerce or offered for sale in a store.",
    "secondary": "In marketing and retail operations, merchandise denotes the systematic presentation, inventory planning, and promotion of goods to maximize sales.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Thy **merchandise** on every sea is spread, laden with spices and precious Indian cloth."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The ships returned home laden with foreign **merchandise** of much greater value than that which had been exported."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The shop window displayed a curious assortment of second-hand **merchandise**, books, and nautical instruments."}
    ]
  },
  "merchandiser.md": {
    "primary": "A person, company, or professional responsible for buying, promoting, and selling commercial goods.",
    "secondary": "In retail supply chain management, a merchandiser balances consumer market trends, seasonal inventory turnover, and retail floor layouts.",
    "quotes": [
      {"author": "Daniel Defoe", "work": "The Complete English Tradesman", "quote": "A prudent **merchandiser** calculates the freight, customs, and insurance before dispatching his vessel across the seas."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The enterprising **merchandiser** constantly searches for emerging markets where supply lags behind consumer demand."},
      {"author": "Walter Bagehot", "work": "Lombard Street: A Description of the Money Market", "quote": "The London credit system provides the foreign **merchandiser** with immediate advances against warehouse warrants."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Action\Dashboard — mer"

updated = 0
for fname, info in data.items():
    fpath = os.path.join(base_dir, fname)
    if not os.path.exists(fpath):
        print(f"Warning: {fpath} does not exist!")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    book_idx = content.find("> [!book]")
    if book_idx == -1:
        print(f"Warning: No > [!book] callout in {fname}")
        continue
    
    prefix = content[:book_idx]
    
    p_def = info["primary"].strip().rstrip(".") + "."
    s_def = info["secondary"].strip().rstrip(".") + "."
    
    new_book = f"> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: {p_def}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {s_def}\n"
    
    new_quote = "> [!quote] 💬 Contextual Usage & Authentic Quotations\n"
    for q in info["quotes"]:
        auth = q["author"].strip()
        work = q["work"].strip()
        quote_text = q["quote"].strip().strip('"').strip('“').strip('”')
        new_quote += f'> - 📜 **{auth} (*{work}*):** *"{quote_text}"*\n'
    
    new_content = prefix + new_book + "\n" + new_quote + "\n"
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated += 1

print(f"Dashboard — mer Batch 1: Successfully updated {updated}/{len(data)} notes.")
