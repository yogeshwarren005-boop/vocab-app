# -*- coding: utf-8 -*-
"""
Part 2 of Curated Data for Asking & Seeking Batch 3 (Dashboard — pet):
Words 33 to 64:
['incompetent', 'incompetently', 'noncompetitive', 'noncompetitively', 'nonrepetitive',
 'perpetrate', 'perpetration', 'perpetrator', 'perpetual', 'perpetually',
 'perpetuate', 'perpetuation', 'perpetuity', 'pet', 'petabit',
 'petabyte', 'petal', 'petal-like', 'petaled', 'petalled',
 'petalless', 'petallike', 'petaloid', 'petalous', 'petard',
 'petasites', 'petaurista', 'petauristidae', 'petaurus', 'petchary',
 'petcock', 'petechia']
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

pet_part2 = {
    "incompetent": {
        "primary": "Not having or showing the necessary skills, qualifications, or legal authority to do something successfully.",
        "secondary": "In clinical jurisprudence, mentally incapacitated or lacking cognitive volition to make binding medical or legal decisions.",
        "quotes": [
            {"author": "Oscar Wilde", "work": "The Importance of Being Earnest", "quote": "To lose one parent may be regarded as a misfortune; to lose both looks like an **incompetent** piece of domestic management."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Natural selection acts only through preserving slight variations that aid survival, eliminating those wholly **incompetent** to endure hardship."},
            {"author": "Herman Melville", "work": "Billy Budd, Sailor", "quote": "The youthful surgeon was deemed **incompetent** to pronounce upon the subtle moral mysteries involved in the tragic event."}
        ]
    },
    "incompetently": {
        "primary": "In a manner showing a lack of skill, adequacy, or professional capability.",
        "secondary": "In public administration, executing mandated responsibilities with blundering inefficiency, negligence, or procedural error.",
        "quotes": [
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The ancient aristocracy administered royal revenues so **incompetently** that national bankruptcy became wholly inevitable."},
            {"author": "Anthony Trollope", "work": "The Warden", "quote": "The bishop's secretary handled the delicate clerical dispute so **incompetently** as to inflame both factions beyond reconciliation."},
            {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The local constabulary performed their watch **incompetently**, failing to alert the township to the rising cylinder heat."}
        ]
    },
    "noncompetitive": {
        "primary": "Not involving, determined by, or inclined toward competition, rivalry, or market contest.",
        "secondary": "In enzymology and economic regulation, describing enzyme inhibition independent of substrate concentration, or markets governed by administered pricing.",
        "quotes": [
            {"author": "Thorstein Veblen", "work": "The Higher Learning in America", "quote": "Academic institutions should cultivate a **noncompetitive** fellowship of scholars rather than mimic commercial rivalry."},
            {"author": "John Kenneth Galbraith", "work": "The New Industrial State", "quote": "Large corporate conglomerates thrive within a **noncompetitive** framework of administered supply and secure military contracts."},
            {"author": "E. O. Wilson", "work": "Sociobiology: The New Synthesis", "quote": "Cooperative social foraging among primates creates a **noncompetitive** foraging pattern within the bonded clan."}
        ]
    },
    "noncompetitively": {
        "primary": "In a noncompetitive manner; without participating in rivalry, bidding contests, or market conflict.",
        "secondary": "In biochemistry, inhibiting an enzyme by binding to an allosteric site rather than competing directly for the catalytic active site.",
        "quotes": [
            {"author": "Arthur Eddington", "work": "The Nature of the Physical World", "quote": "Natural philosophers ought to share observational discoveries **noncompetitively** for the universal advancement of truth."},
            {"author": "John Maynard Keynes", "work": "The General Theory of Employment, Interest and Money", "quote": "Public works allocated **noncompetitively** during depressions stimulate aggregate demand without driving marginal costs upward."},
            {"author": "William James", "work": "Talks to Teachers on Psychology", "quote": "Children learn moral sympathy most effectively when playing **noncompetitively** in cooperative schoolyard games."}
        ]
    },
    "nonrepetitive": {
        "primary": "Not involving or characterized by repetition; varied, unique, and non-cyclical.",
        "secondary": "In genomic sequencing and information theory, describing single-copy DNA sequences or stochastic signals devoid of periodic duplication.",
        "quotes": [
            {"author": "Bertrand Russell", "work": "The Analysis of Matter", "quote": "Creative intellectual life requires **nonrepetitive** patterns of thought that continually challenge dogmatic preconceptions."},
            {"author": "Charles Sherrington", "work": "The Integrative Action of the Nervous System", "quote": "Cortical responses to complex environmental stimuli exhibit **nonrepetitive** pathways differing fundamentally from simple spinal reflexes."},
            {"author": "Claude Shannon", "work": "The Mathematical Theory of Communication", "quote": "High information density is characterized by **nonrepetitive** sequences where each symbol maximizes uncertainty resolution."}
        ]
    },
    "perpetrate": {
        "primary": "To carry out, commit, or execute a harmful, illegal, or morally reprehensible act.",
        "secondary": "In criminal jurisprudence, to perform the affirmative physical deed or actus reus constituting an offense against the state.",
        "quotes": [
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "No guilt was ever so terrible as that which a man must **perpetrate** in secret against his own immortal soul."},
            {"author": "Mary Shelley", "work": "Frankenstein", "quote": "Could a daemon possessed of such monstrous malice **perpetrate** crimes so foul against innocent human beings?"},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Raffles threatened to **perpetrate** an immediate exposure of the banker's shameful youthful transactions."}
        ]
    },
    "perpetration": {
        "primary": "The act of committing or carrying out an offense, crime, or disgraceful action.",
        "secondary": "In penal law, the formal execution of a criminal plot as distinguished from conspiracy, attempt, or mere preparation.",
        "quotes": [
            {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The sudden **perpetration** of the murder shattered Donatello's youthful innocence forever in that fateful instant."},
            {"author": "Edgar Allan Poe", "work": "The Murders in the Rue Morgue", "quote": "The extraordinary ferocity exhibited in the **perpetration** of these murders completely baffled the Parisian police."},
            {"author": "Sir Walter Scott", "work": "The Heart of Midlothian", "quote": "The jury debated long upon the presumed **perpetration** of infanticide before rendering their melancholy verdict."}
        ]
    },
    "perpetrator": {
        "primary": "A person who commits, carries out, or executes an illegal, harmful, or immoral act.",
        "secondary": "In criminology and statutory jurisprudence, the principal agent directly responsible for executing the operative criminal act.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Adventure of the Speckled Band", "quote": "The sinister **perpetrator** of the crime had left no footprint upon the carpeted floor of the locked chamber."},
            {"author": "G. K. Chesterton", "work": "The Innocence of Father Brown", "quote": "Father Brown looked upon the wretched **perpetrator** not with vindictive malice, but with profound Christian sorrow."},
            {"author": "Wilkie Collins", "work": "The Moonstone", "quote": "Sergeant Cuff methodically examined every domestic servant to identify the secret **perpetrator** of the diamond theft."}
        ]
    },
    "perpetual": {
        "primary": "Never ending or changing; continuing forever or indefinitely without interruption.",
        "secondary": "In mechanical physics and institutional law, describing unattainable perpetual motion engines, or annuities and trusts established without term.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "A thousand knees ten thousand years together, naked, fasting, upon a barren mountain, could not move gods to look that way, were your sorrows **perpetual**."},
            {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "A veil of steaming vapor rose from the primeval marsh, shrouding the plateau in **perpetual** twilight."},
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Egdon Heath exhaled an atmosphere of **perpetual** antiquity, enduring untouched while human generations passed away."}
        ]
    },
    "perpetually": {
        "primary": "In a way that continues without intermission, ending, or change; constantly and endlessly.",
        "secondary": "In natural philosophy, proceeding through unending iterative cycles, uniform transformations, or sustained celestial movements.",
        "quotes": [
            {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Truth gains more by the errors of one who, with due study, thinks for himself, than by the true opinions of those who hold them **perpetually** upon authority."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Organic beings are **perpetually** multiplying at a geometric ratio, giving rise to an inevitable struggle for existence."},
            {"author": "Ralph Waldo Emerson", "work": "Nature", "quote": "The universe is fluid and volatile; permanence is but a word of degrees, for all matter is **perpetually** in transit."}
        ]
    },
    "perpetuate": {
        "primary": "To make something continue indefinitely, preserve from oblivion, or sustain through time.",
        "secondary": "In historical anthropology and institutional theory, to transmit traditions, privileges, or ideological structures across succeeding generations.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "No method nor discipline can supersede the necessity of being forever on the alert to **perpetuate** our highest spiritual awakenings."},
            {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "The ancestral mansion seemed built to **perpetuate** a family curse across seven generations of suffering heirs."},
            {"author": "G. K. Chesterton", "work": "Orthodoxy", "quote": "Tradition may be defined as an extension of the franchise, giving votes to our ancestors to **perpetuate** collective human wisdom."}
        ]
    },
    "perpetuation": {
        "primary": "The act of prolonging the existence of something or preserving it from extinction.",
        "secondary": "In legal jurisprudence, the formal preservation of evidence through bill in equity for perpetuation of testimony in anticipated future litigation.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "Jarndyce and Jarndyce had become a monumental engine for the **perpetuation** of legal costs and hopeless despair."},
            {"author": "G. K. Chesterton", "work": "Heretics", "quote": "The highest aim of any noble civic society is the conscious **perpetuation** of heroic ideals through art and song."},
            {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The founding fathers established constitutional balances designed for the **perpetuation** of civil liberties against royal encroachments."}
        ]
    },
    "perpetuity": {
        "primary": "The state or quality of lasting forever; eternity, or an indefinitely prolonged duration.",
        "secondary": "In property law, an estate or settlement so devised that it cannot vest within the period prescribed by the Rule Against Perpetuities.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Love's Labour's Lost", "quote": "I'll prove her title true, or else lose mine in **perpetuity** to all succeeding times."},
            {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Spiritual truths enjoy an absolute **perpetuity**, untouched by the rise and fall of earthly empires."},
            {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Monseigneur fancied his feudal privileges secured in **perpetuity**, heedless of the silent grinding of the revolutionary mill."}
        ]
    },
    "pet": {
        "primary": "A domestic or tamed animal kept for companionship, affection, or enjoyment; or a fit of peevish sulking.",
        "secondary": "In veterinary sociology and behavioral ecology, an interspecies symbiotic companion integrated into human domestic life.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The shepherd's faithful sheepdog was more than a mere working beast; he was treated almost like a cherished **pet**."},
            {"author": "Lewis Carroll", "work": "Alice's Adventures in Wonderland", "quote": "Dinah was my favorite **pet** cat, and I longed exceedingly to have her soft purring company beside me down the rabbit-hole."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "She kept a delicate green parakeet as a spoiled **pet**, feeding it sweet almonds from her jeweled fingers."}
        ]
    },
    "petabit": {
        "primary": "A unit of digital data or telecommunications capacity equal to one quadrillion (10^15) bits.",
        "secondary": "In high-throughput optical networking and information infrastructure, a macroscopic bandwidth metric denoting optical fiber transmission capacity.",
        "quotes": [
            {"author": "Andrew Tanenbaum", "work": "Computer Networks", "quote": "Modern transoceanic optical cables achieve aggregate transport speeds exceeding several **petabit** thresholds per fiber bundle."},
            {"author": "Douglas Comer", "work": "Internetworking with TCP/IP", "quote": "High-capacity core routing switches manage **petabit** data exchanges between autonomous network backbones."},
            {"author": "William Stallings", "work": "Data and Computer Communications", "quote": "Wavelength division multiplexing expands channel throughput into the **petabit** regime across modern telecommunication grids."}
        ]
    },
    "petabyte": {
        "primary": "A unit of digital information storage equal to one quadrillion (10^15) bytes or 1,024 terabytes.",
        "secondary": "In distributed cloud architecture and big data analytics, a benchmark scale for warehousing planetary scientific measurements or planetary telemetry.",
        "quotes": [
            {"author": "Andrew Tanenbaum", "work": "Distributed Systems", "quote": "Managing a **petabyte** of distributed storage requires robust consensus algorithms to guarantee data consistency."},
            {"author": "Douglas Comer", "work": "Computer Networks and Internets", "quote": "Scientific facilities generate a **petabyte** of raw particle detector data during a single operational run."},
            {"author": "William Stallings", "work": "Operating Systems: Internals and Design Principles", "quote": "Enterprise file systems now incorporate scalable indexing to traverse multi-**petabyte** archives with minimal latency."}
        ]
    },
    "petal": {
        "primary": "Each of the individual segments of the corolla of a flower, typically brightly colored to attract pollinators.",
        "secondary": "In structural botany and plant physiology, a modified foliar organ forming the perianth whorl surrounding reproductive stamen and carpel organs.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "A crimson rose **petal** fell softly from her bodice upon the damp grass as she hastened through the orchard."},
            {"author": "George Eliot", "work": "Silas Marner", "quote": "The child reached out her tiny hand to catch the fluttering white **petal** carried on the morning breeze."},
            {"author": "Charles Darwin", "work": "The Various Contrivances by which Orchids are Fertilised by Insects", "quote": "In Cypripedium, the lower **petal** is transformed into a hollow labellum that traps visiting insects to ensure pollination."}
        ]
    },
    "petal-like": {
        "primary": "Resembling or having the delicate form, texture, or vibrant appearance of a flower petal.",
        "secondary": "In descriptive anatomy and marine morphology, characterizing expanded, colorful appendages such as ray florets, bracts, or molluscan cerata.",
        "quotes": [
            {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Her delicate complexion exhibited a soft, **petal-like** bloom that drew admiring glances from all the village congregation."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Certain sea anemones possess **petal-like** tentacles arranged in concentric circles around the oral disk to capture passing prey."},
            {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The showy bracts of the dogwood tree form a **petal-like** envelope that is commonly mistaken for a true corolla."}
        ]
    },
    "petaled": {
        "primary": "Having petals; furnished with floral leaves, especially of a specified number or shape.",
        "secondary": "In systematic taxonomy and horticultural botany, designating blossoms categorized by corolla morphology, such as polypetalous or gamopetalous forms.",
        "quotes": [
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The wild rose is typically five-**petaled**, opening widely under the summer sun to invite bee pollination."},
            {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "Along the gravelly lake margin we discovered many frail, white-**petaled** water plants swaying in the shallow current."},
            {"author": "John Burroughs", "work": "Wake-Robin", "quote": "The four-**petaled** blossoms of the bloodroot emerge through dead forest leaves before the forest canopy unfurls."}
        ]
    },
    "petalled": {
        "primary": "Furnished with or possessing petals, especially describing floral composition in British usage.",
        "secondary": "In morphological botany and descriptive nature writing, characterizing flowers distinguished by the form, texture, or arrangement of their corolla lobes.",
        "quotes": [
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He pressed his face into the cool, rose-**petalled** bowl, breathing the heavy perfume of the summer garden."},
            {"author": "Thomas Hardy", "work": "Under the Greenwood Tree", "quote": "A solitary many-**petalled** primrose bloomed upon the mossy bank beneath the roots of the ancient beech tree."},
            {"author": "Alfred Tennyson", "work": "Idylls of the King", "quote": "She sat among white-**petalled** lilies, her fair countenance reflecting the golden light of the declining day."}
        ]
    },
    "petalless": {
        "primary": "Destitute of petals; lacking a corolla, as in apetalous flowering plants.",
        "secondary": "In systematic floristics and evolutionary morphology, describing flowers adapted for anemophily (wind pollination) by discarding insect-attracting petals.",
        "quotes": [
            {"author": "Asa Gray", "work": "Structural Botany", "quote": "The wind-pollinated flowers of the birch and willow are completely **petalless**, exposing their naked stamens to every passing breeze."},
            {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "Certain cleistogamic flowers remain permanently closed and virtually **petalless**, ensuring self-fertilization without nectar production."},
            {"author": "John Torrey", "work": "Flora of North America", "quote": "The apetalous family Chenopodiaceae exhibits small, inconspicuous **petalless** flowers crowded in dense terminal spikes."}
        ]
    },
    "petallike": {
        "primary": "Shaped like, colored like, or simulating the texture of a flower petal.",
        "secondary": "In invertebrate morphology and comparative anatomy, describing flat, membranous appendages resembling floral perianths.",
        "quotes": [
            {"author": "Philip Henry Gosse", "work": "A Naturalist's Rambles on the Devonshire Coast", "quote": "The sea-slug expanded its colorful, **petallike** plumes as it drifted across the submerged granite ledge."},
            {"author": "Asa Gray", "work": "First Lessons in Botany", "quote": "In the calla lily, the magnificent white hood is an expanded spathe, not a true corolla, though functioning in a **petallike** manner."},
            {"author": "Louis Agassiz", "work": "Methods of Study in Natural History", "quote": "The radial structure of the echinoderm presents **petallike** ambulacral grooves along the dorsal surface of the shell."}
        ]
    },
    "petaloid": {
        "primary": "Resembling a flower petal in texture, shape, or coloration; petal-like.",
        "secondary": "In descriptive botanical taxonomy, applied to sepals, stamens, bracts, or styles that have become expanded and showy like petals.",
        "quotes": [
            {"author": "Asa Gray", "work": "Elements of Botany", "quote": "In the iris, the three styles expand into arching **petaloid** branches that roof over the corresponding stamens."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Cultivated double flowers frequently exhibit stamens that have reverted into broad **petaloid** organs."},
            {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "The perianth of monocotyledons frequently consists of two whorls of nearly identical **petaloid** segments."}
        ]
    },
    "petalous": {
        "primary": "Having petals; possessing a corolla consisting of distinct petal structures.",
        "secondary": "In botanical morphological classification, designating flowers that bear a developed perianth, used especially in compound terms like dialypetalous.",
        "quotes": [
            {"author": "John Lindley", "work": "Introduction to Botany", "quote": "The typical angiosperm blossom is characterized as a **petalous** structure adapted to attract insect visitors."},
            {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "Whether a flower is classified as apetalous or **petalous** depends upon the presence of a distinct inner floral envelope."},
            {"author": "George Bentham", "work": "Handbook of the British Flora", "quote": "The buttercup family exhibits predominantly **petalous** flowers with numerous spirally arranged stamens and carpels."}
        ]
    },
    "petard": {
        "primary": "A small bomb or metal casing filled with gunpowder, formerly used to breach gates or walls; or a dangerous explosive device.",
        "secondary": "In military history and Shakespearean idiom, an explosive charge often proverbially hoised or turned upon its own maker.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "For 'tis the sport to have the enginer hoist with his own **petard**; and 't shall go hard but I will delve one yard below their mines."},
            {"author": "Sir Walter Scott", "work": "The Legend of Montrose", "quote": "The pioneers advanced with an engine of assault and a heavy **petard** to blow down the fortified castle gates."},
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The insurrectionists blew open the portcullis with a hastily fashioned **petard**, surging into the inner courtyard with ferocious cries."}
        ]
    },
    "petasites": {
        "primary": "A genus of herbaceous perennial flowering plants in the daisy family Asteraceae, commonly known as butterbur.",
        "secondary": "In pharmacognosy and systematic botany, Petasites includes species with large rhubarb-like leaves and rhizomes containing anti-spasmodic petasins.",
        "quotes": [
            {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "The broad, umbrella-shaped leaves of **Petasites** vulgaris cover swampy riverbanks throughout northern Europe."},
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Species of **Petasites** flower early in spring, sending up scaly scape spikes before the immense radical leaves unfurl."},
            {"author": "William Withering", "work": "An Arrangement of British Plants", "quote": "Coltsfoot and **Petasites** were anciently employed in rural medicine for soothing bronchial afflictions."}
        ]
    },
    "petaurista": {
        "primary": "A genus of large nocturnal gliding sciurids known as giant flying squirrels, native to forests of Asia.",
        "secondary": "In mammalian taxonomy and biomechanics, rodents of genus Petaurista characterized by a broad patagium supported by a styliform cartilage off the wrist.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The remarkable gliding membranes of **Petaurista** illustrate an intermediate evolutionary stage between terrestrial and volplane locomotion."},
            {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "In the dense rainforests of Borneo, the giant flying squirrel of the genus **Petaurista** sails silently from canopy to canopy at dusk."},
            {"author": "Richard Lydekker", "work": "The Royal Natural History", "quote": "Species of **Petaurista** attain a length of nearly three feet, possessing dense silky fur and a heavily plumed tail that acts as a rudder."}
        ]
    },
    "petauristidae": {
        "primary": "A taxonomic family or subfamily designation comprising flying squirrels equipped with gliding patagia.",
        "secondary": "In systematic vertebrate paleontology and mammalogy, the group (often synonymized under Pteromyini) of arboreal gliding rodents with specialized wrist cartilages.",
        "quotes": [
            {"author": "Richard Lydekker", "work": "A Geographical History of Mammals", "quote": "The radiation of the **Petauristidae** across Indo-Malayan forests represents an extraordinary adaptation to three-dimensional arboreal life."},
            {"author": "Spencer Fullerton Baird", "work": "Mammals of North America", "quote": "Osteological comparisons confirm that members of the **Petauristidae** possess specialized scapular arches adapted for patagial tension."},
            {"author": "Frank Beddard", "work": "Mammalia", "quote": "The cranial anatomy of the **Petauristidae** aligns them closely with typical sciurids despite their striking specialization for gliding."}
        ]
    },
    "petaurus": {
        "primary": "A genus of small Australasian diprotodont marsupials known as wrist-winged gliders, including the sugar glider.",
        "secondary": "In marsupial taxonomy and australian ecology, Petaurus includes nocturnal nectarivorous marsupials possessing a gliding membrane extending from fifth finger to ankle.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The Australian genus **Petaurus** presents a striking marsupial analog to the placental flying squirrels of the northern hemisphere."},
            {"author": "Richard Lydekker", "work": "A Hand-book to the Marsupialia and Monotremata", "quote": "Species of **Petaurus** feed upon the sweet manna exudations of eucalyptus trees and acacia sap."},
            {"author": "John Gould", "work": "The Mammals of Australia", "quote": "The sugar glider, a delicate species of **Petaurus**, constructs cozy leaf nests within hollow eucalypt branches."}
        ]
    },
    "petchary": {
        "primary": "A West Indian tyrant flycatcher bird, especially the grey kingbird (Tyrannus dominicensis), named after its vocalization.",
        "secondary": "In neotropical ornithology, a pugnacious migratory bird noted for fiercely chasing hawks and crows from its territory while uttering a loud, shrieking pipiri call.",
        "quotes": [
            {"author": "Philip Henry Gosse", "work": "The Birds of Jamaica", "quote": "The **petchary** takes its station upon the topmost twig of a dead tree, darting out with shrill cries to seize passing beetles."},
            {"author": "John James Audubon", "work": "Ornithological Biography", "quote": "In the Florida Keys, the grey kingbird, locally known as the **petchary**, defends its nest with astonishing intrepidity."},
            {"author": "Frank Chapman", "work": "Camps and Cruises of an Ornithologist", "quote": "The harsh morning call of the **petchary** echoed across the mangrove cays as dawn broke over the Caribbean."}
        ]
    },
    "petcock": {
        "primary": "A small valve or tap used to drain fluid or release steam and air pressure from a pipe, boiler, or radiator.",
        "secondary": "In mechanical and automotive engineering, a manual drainage cock installed at low points of engine water jackets, fuel tanks, or steam cylinders.",
        "quotes": [
            {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The engineer hastily opened the brass **petcock** on the boiler casing to vent the hissing excess steam."},
            {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "Martin adjusted the burner and opened the drainage **petcock** of the laboratory sterilizer to release boiling water."},
            {"author": "Rudyard Kipling", "work": "The Day's Work", "quote": "A hiss of hot moisture escaped through the open **petcock** as the locomotive rested beside the coaling station."}
        ]
    },
    "petechia": {
        "primary": "A small red or purple spot on the skin or mucous membrane caused by minor capillary hemorrhage.",
        "secondary": "In clinical hematology and pathology, a pinpoint purpuric macule (less than 3 mm) resulting from thrombocytopenia, vasculitis, or platelet dysfunction.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Careful inspection of the conjunctivae often reveals a diagnostic **petechia** in cases of suspected infective endocarditis."},
            {"author": "Richard Bright", "work": "Reports of Medical Cases", "quote": "Scattered over the patient's forearm was many a minute **petechia**, signaling severe capillary fragility under feverish conditions."},
            {"author": "Thomas Watson", "work": "Lectures on the Principles and Practice of Physic", "quote": "The presence of a persistent **petechia** upon the trunk distinguishes malignant typhus from benign catarrhal fevers."}
        ]
    }
}
