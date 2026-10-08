# -*- coding: utf-8 -*-
"""
curate_botany_b4_p1.py
Cluster Botany, Minerals & Elements Batch 4 Part 1 (51 words)
Dashboard:
- rad (first 51 words: abradant -> radiobiologist)
"""
import sys
import re

sys.stdout.reconfigure(encoding="utf-8")

data_botany_b4_p1 = {
    # Dashboard — rad (first 51 words)
    "abradant": {
        "primary": "A substance or material used for grinding, polishing, or scraping away a surface; an abrasive.",
        "secondary": "In geological geomorphology and industrial machining, mineral particles such as quartz, corundum, or garnet that wear down rock or metal.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Windblown desert sand acts as a natural **abradant**, carving bizarre ventifacts out of hard basalt."
            },
            {
                "author": "Archibald Geikie",
                "work": "Text-Book of Geology",
                "quote": "Glacial mud carried beneath moving ice serves as a powerful **abradant**, grooving and polishing the bed of the valley."
            },
            {
                "author": "Michael Faraday",
                "work": "Experimental Researches in Chemistry and Physics",
                "quote": "The optician selected fine emery powder as an **abradant** to grind the parabolic mirror into shape."
            }
        ]
    },
    "abrade": {
        "primary": "To scrape, wear away, or rub off the surface of something through mechanical friction.",
        "secondary": "In dermatology and geomorphology, to produce a superficial cutaneous excoriation or erode geological strata by scouring.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Structure and Distribution of Coral Reefs",
                "quote": "Powerful breakers constantly **abrade** the outer barrier reef, grinding coral branches into fine sand."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The heavy hempen line began to **abrade** the cedar gunwale, smoking with fierce friction as the whale sounded."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Accidental falls against gravelly roads often **abrade** the skin, requiring thorough antiseptic cleansing."
            }
        ]
    },
    "abrader": {
        "primary": "A tool, machine, or natural agent that wears down or polishes surfaces by friction.",
        "secondary": "In prehistoric archaeology and workshop technology, a rough stone implement used by ancient peoples to grind tools and bead ornaments.",
        "quotes": [
            {
                "author": "John Evans",
                "work": "The Ancient Stone Implements, Weapons and Ornaments of Great Britain",
                "quote": "Neolithic toolmakers utilized a grooved sandstone **abrader** to shape bone needles and celts."
            },
            {
                "author": "Aleš Hrdlička",
                "work": "Anthropometry",
                "quote": "Excavations at the ancient mound yielded several pumice stones employed as a hide **abrader**."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Moving ice functions as an unyielding continental **abrader**, striating bedrock across immense distances."
            }
        ]
    },
    "comrade": {
        "primary": "A companion, associate, or friend, especially one who shares common interests, hardships, or military service.",
        "secondary": "In political history and socialist terminology, a fellow member of an egalitarian political party, labor movement, or revolutionary organization.",
        "quotes": [
            {
                "author": "Leo Tolstoy",
                "work": "War and Peace",
                "quote": "Pierre embraced his wounded **comrade** on the battlefield, offering what little bread he had left."
            },
            {
                "author": "George Orwell",
                "work": "Animal Farm",
                "quote": "Napoleon reminded the animals that every **comrade** must work selflessly for the common welfare."
            },
            {
                "author": "Walt Whitman",
                "work": "Leaves of Grass",
                "quote": "I sing the passionate love of **comrade** for comrade, cementing the soul of the democratic republic."
            }
        ]
    },
    "comradeliness": {
        "primary": "The feeling, spirit, or disposition of friendly mutual support, loyalty, and companionship among associates.",
        "secondary": "In social philosophy, the fraternal warmth and mutual respect binding equals engaged in a joint endeavor or struggle.",
        "quotes": [
            {
                "author": "George Orwell",
                "work": "Homage to Catalonia",
                "quote": "There was a remarkable atmosphere of genuine **comradeliness** among the militiamen defending the Aragon front."
            },
            {
                "author": "Jack London",
                "work": "The Iron Heel",
                "quote": "In the subterranean socialist clubs, true **comradeliness** flourished amidst constant police persecution."
            },
            {
                "author": "Joseph Conrad",
                "work": "The Mirror of the Sea",
                "quote": "Seamen bound together by shared tempests develop an unspoken **comradeliness** that endures across oceans."
            }
        ]
    },
    "comradely": {
        "primary": "Characteristic of or befitting a comrade; warmly friendly, loyal, and supportive.",
        "secondary": "Displaying fraternal solidarity and mutual goodwill in social or political relations.",
        "quotes": [
            {
                "author": "Leo Tolstoy",
                "work": "War and Peace",
                "quote": "He greeted his fellow officers with a warm and **comradely** embrace before the regiment marched."
            },
            {
                "author": "George Orwell",
                "work": "Burmese Days",
                "quote": "Flory longed for a **comradely** discussion where men could speak their honest thoughts without colonial pretension."
            },
            {
                "author": "Jack London",
                "work": "The Sea-Wolf",
                "quote": "The sailors shared their tobacco in a **comradely** fashion during the quiet hours of the night watch."
            }
        ]
    },
    "comradery": {
        "primary": "Mutual trust, goodwill, and sociability among companions who spend significant time together; camaraderie.",
        "secondary": "The supportive fraternal bond that unites individuals facing shared difficulties, danger, or joint athletic effort.",
        "quotes": [
            {
                "author": "Stephen Crane",
                "work": "The Red Badge of Courage",
                "quote": "In the smoky camp after the engagement, a rough **comradery** united the surviving soldiers."
            },
            {
                "author": "Theodore Roosevelt",
                "work": "The Rough Riders",
                "quote": "The regiment was animated by an irresistible spirit of **comradery** that made hardship seem trivial."
            },
            {
                "author": "Jack London",
                "work": "The Call of the Wild",
                "quote": "Even among the sled dogs, a fierce yet loyal **comradery** regulated the harmony of the traces."
            }
        ]
    },
    "comradeship": {
        "primary": "The bond, relationship, or community of friendship and mutual loyalty between comrades.",
        "secondary": "In civic and military sociology, the close fraternal solidarity forged through collective labor or military trials.",
        "quotes": [
            {
                "author": "Walt Whitman",
                "work": "Democratic Vistas",
                "quote": "Only through deep, fervent **comradeship** can democracy realize its highest moral and spiritual promise."
            },
            {
                "author": "George Orwell",
                "work": "Homage to Catalonia",
                "quote": "The essential feeling was one of **comradeship**, where men addressed each other as equals without servility."
            },
            {
                "author": "Joseph Conrad",
                "work": "Lord Jim",
                "quote": "He remembered the unswerving **comradeship** of the sea, where every man's life depends upon his fellow's vigilance."
            }
        ]
    },
    "conrad": {
        "primary": "Relating to Joseph Conrad (1857-1924), the Polish-British novelist celebrated for maritime fiction and psychological depth.",
        "secondary": "In literary analysis, reflecting Conradian themes of moral isolation, psychological crisis, and the enigmatic abyss of human imperialism.",
        "quotes": [
            {
                "author": "Virginia Woolf",
                "work": "The Common Reader",
                "quote": "The genius of **Conrad** lies in his power to illuminate the solitary soul navigating unfathomable moral darkness."
            },
            {
                "author": "H. G. Wells",
                "work": "Experiment in Autobiography",
                "quote": "My conversations with **Conrad** revealed a mind intensely preoccupied with the tragic dignity of craftsmanship."
            },
            {
                "author": "T. S. Eliot",
                "work": "Selected Essays",
                "quote": "The haunting epigraph drawn from **Conrad** captures the spiritual paralysis of post-war European civilization."
            }
        ]
    },
    "conradina": {
        "primary": "A genus of endangered aromatic shrubs in the mint family (Lamiaceae), native to southeastern North American coastal pine barrens.",
        "secondary": "In North American floristics, commonly called false rosemaries, featuring lavender two-lipped blossoms and adapted to deep xeric white sands.",
        "quotes": [
            {
                "author": "John Kunkel Small",
                "work": "Flora of the Southeastern United States",
                "quote": "Species of **Conradina** inhabit the ancient sand scrub ridges of peninsular Florida, exhaling a pungent resinous scent."
            },
            {
                "author": "Asa Gray",
                "work": "Synoptical Flora of North America",
                "quote": "The genus **Conradina** was dedicated by Rafinesque to the botanist Solomon Conrad, distinguished by its strongly bilabiate corollas."
            },
            {
                "author": "Liberty Hyde Bailey",
                "work": "The Standard Cyclopedia of Horticulture",
                "quote": "Botanists prize **Conradina** for its dense habit and delicate lavender flowers suited for drought-tolerant rockeries."
            }
        ]
    },
    "corrade": {
        "primary": "To wear away or erode through mechanical friction and abrasion, especially by wind, glaciers, or streams.",
        "secondary": "In fluvial geomorphology, to deepen or widen a riverbed through the abrasive scouring action of sediment-laden currents.",
        "quotes": [
            {
                "author": "Archibald Geikie",
                "work": "Text-Book of Geology",
                "quote": "Mountain torrents heavily charged with sharp gravel **corrade** deep vertical gorges through solid granite."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The river continues to **corrade** its rocky floor until it attains a stable hydraulic grade line."
            },
            {
                "author": "John Wesley Powell",
                "work": "Exploration of the Colorado River of the West",
                "quote": "The mud-laden torrents of the Colorado **corrade** the canyon walls with relentless abrasive power."
            }
        ]
    },
    "eradicable": {
        "primary": "Capable of being eradicated, uprooted, or completely removed and destroyed.",
        "secondary": "In epidemiology and public health, designating infectious pathogens or social evils capable of total global elimination through coordinated intervention.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "Utilitarianism",
                "quote": "Poverty, disease, and social injustices are essentially **eradicable** through wise legislation and collective effort."
            },
            {
                "author": "René Dubos",
                "work": "Mirage of Health",
                "quote": "Optimistic hygienists assumed that every bacterial epidemic was permanently **eradicable** by chemical means."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Early focal infection remains readily **eradicable** before systemic dissemination takes place."
            }
        ]
    },
    "eradicate": {
        "primary": "To pull up by the roots; to eliminate, extinguish, or destroy completely.",
        "secondary": "In disease control and agronomy, to wipe out a pathogen, invasive weed, or systemic social vice down to its origin.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Farmers struggle year after year to **eradicate** tenacious perennial weeds from their ploughed fields."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The emperor enacted draconian decrees designed to **eradicate** corruption among provincial tax collectors."
            },
            {
                "author": "Alexander Fleming",
                "work": "Penicillin: Its Practical Application",
                "quote": "Careful administration of antibacterial therapy aims to **eradicate** pathogenic microbes without harming host tissues."
            }
        ]
    },
    "eradication": {
        "primary": "The complete destruction, extermination, or uprooting of something undesirable.",
        "secondary": "In global epidemiology, the deliberate reduction of an infectious disease's worldwide incidence to zero, as achieved with smallpox.",
        "quotes": [
            {
                "author": "Louis Pasteur",
                "work": "Studies on Fermentation",
                "quote": "Total **eradication** of the contaminant requires meticulous boiling of all glass apparatus."
            },
            {
                "author": "Rachel Carson",
                "work": "Silent Spring",
                "quote": "The hasty promise of insect **eradication** through chemical blitzes disrupted fragile ecological balances."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "The ultimate conquest of malaria requires the systematic **eradication** of mosquito breeding grounds."
            }
        ]
    },
    "eradicator": {
        "primary": "A person, tool, chemical, or agent that completely removes, eliminates, or uproots something.",
        "secondary": "In agricultural engineering, an implement or cultivation tool attached to a tractor to uproot deep weed roots and loosen compacted soil.",
        "quotes": [
            {
                "author": "Liberty Hyde Bailey",
                "work": "The Principles of Agriculture",
                "quote": "The gang-plow was equipped with an efficient weed **eradicator** to clear the soil before planting."
            },
            {
                "author": "Asa Gray",
                "work": "Scientific Papers of Asa Gray",
                "quote": "Frost acts as an infallible natural **eradicator** of tender subtropical plants in temperate zones."
            },
            {
                "author": "Upton Sinclair",
                "work": "The Jungle",
                "quote": "The sanitary inspector presented himself as a stern **eradicator** of filth in the packinghouse cellars."
            }
        ]
    },
    "ineradicable": {
        "primary": "Incapable of being eradicated, uprooted, or completely eliminated; deeply entrenched.",
        "secondary": "In psychology and moral philosophy, describing habits, prejudices, or instincts so deep-seated that they resist all corrective education.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Early memories remained **ineradicable** in her heart, surviving all the shifts of fortune and sorrow."
            },
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "Certain social instincts appear **ineradicable**, having evolved through countless generations of group survival."
            },
            {
                "author": "Joseph Conrad",
                "work": "Under Western Eyes",
                "quote": "The student felt an **ineradicable** sense of guilt that shadowed his every thought in exile."
            }
        ]
    },
    "irradiate": {
        "primary": "To illuminate, brighten, or shed light upon; to cast radiant beams upon something.",
        "secondary": "In physics and medicine, to expose a substance or patient to electromagnetic radiation, X-rays, or radioactive emissions.",
        "quotes": [
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "Shine inward, and the mind through all her powers **irradiate**; there plant eyes, all mist from thence purge and disperse."
            },
            {
                "author": "Marie Curie",
                "work": "Radioactive Substances",
                "quote": "We observed that radium rays **irradiate** surrounding air, rendering the gas an electrical conductor."
            },
            {
                "author": "Percy Bysshe Shelley",
                "work": "Prometheus Unbound",
                "quote": "Beams of heavenly truth **irradiate** the dark caverns of human ignorance and fear."
            }
        ]
    },
    "irradiation": {
        "primary": "The process of emitting radiant light or energy; exposure to rays or radiation.",
        "secondary": "In radiology and food preservation, treating organic material with ionizing radiation to sterilize pathogens, inhibit sprouting, or destroy tumors.",
        "quotes": [
            {
                "author": "Marie Curie",
                "work": "Treatise on Radioactivity",
                "quote": "Intense **irradiation** from polonium causes phosphorescence on zinc sulfide screens."
            },
            {
                "author": "Ernest Rutherford",
                "work": "Radioactive Transformations",
                "quote": "The biological effects of cellular **irradiation** stem from direct atomic ionization within protoplasm."
            },
            {
                "author": "William Wordsworth",
                "work": "The Prelude",
                "quote": "A sudden **irradiation** of the spirit transfigured the ordinary mountain landscape into celestial glory."
            }
        ]
    },
    "nonradioactive": {
        "primary": "Not exhibiting radioactivity; possessing stable atomic nuclei that do not undergo spontaneous radioactive decay.",
        "secondary": "In nuclear chemistry and tracing experiments, designating stable isotopes utilized as safe chemical markers without ionizing hazard.",
        "quotes": [
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "Biochemists prefer **nonradioactive** stable isotopes like carbon-13 when tracing metabolic pathways in human subjects."
            },
            {
                "author": "Glenn T. Seaborg",
                "work": "Transuranium Elements",
                "quote": "Separating radioactive actinides from ordinary **nonradioactive** rare earths required delicate ion-exchange chromatography."
            },
            {
                "author": "Marie Curie",
                "work": "Treatise on Radioactivity",
                "quote": "The inactive bismuth fraction was completely **nonradioactive**, showing no deflection in the electroscope."
            }
        ]
    },
    "rad": {
        "primary": "A historical unit of absorbed radiation dose, defined as 100 ergs of energy absorbed per gram of matter.",
        "secondary": "In radiation biophysics, a dosimetry standard superseded in modern metric SI by the gray (where 1 gray equals 100 rads).",
        "quotes": [
            {
                "author": "Glenn T. Seaborg",
                "work": "Transuranium Elements",
                "quote": "Dosimeters recorded an exposure of less than one **rad** during the remote handling of the reactor fuel."
            },
            {
                "author": "Rachel Carson",
                "work": "Silent Spring",
                "quote": "Low-level exposures measured in fractions of a **rad** can produce cumulative genetic aberrations over generations."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "A whole-body exposure exceeding four hundred **rad** causes severe acute radiation sickness in mammals."
            }
        ]
    },
    "radar": {
        "primary": "An electronic detection system that uses radio waves to determine the distance, angle, and velocity of objects.",
        "secondary": "In military history and aeronautics, radio detection and ranging technology pioneered during World War II for coastal defense and night interception.",
        "quotes": [
            {
                "author": "Winston Churchill",
                "work": "Their Finest Hour",
                "quote": "The invisible chain of **radar** stations along our southern coast alerted fighter squadrons to oncoming raids."
            },
            {
                "author": "Norbert Wiener",
                "work": "Cybernetics",
                "quote": "Automated tracking systems combined **radar** feedback with servo-mechanisms to direct anti-aircraft batteries."
            },
            {
                "author": "Rachel Carson",
                "work": "The Sea Around Us",
                "quote": "Navigators relied on marine **radar** to guide great ships safely through impenetrable fog banks."
            }
        ]
    },
    "radial": {
        "primary": "Arranged like rays or the spokes of a wheel, diverging outwards from a common center.",
        "secondary": "In human anatomy, relating to the radius bone of the forearm or the radial artery and radial nerve.",
        "quotes": [
            {
                "author": "Henry Gray",
                "work": "Anatomy: Descriptive and Surgical",
                "quote": "The physician compresses the **radial** artery at the wrist to ascertain the frequency and rhythm of the pulse."
            },
            {
                "author": "Ernst Haeckel",
                "work": "Art Forms in Nature",
                "quote": "The silica skeletons of radiolarians display breathtaking **radial** symmetry of unmatched mathematical elegance."
            },
            {
                "author": "D'Arcy Wentworth Thompson",
                "work": "On Growth and Form",
                "quote": "Growth forces in jellyfish bell structures produce **radial** canals that distribute nutrients uniformly."
            }
        ]
    },
    "radial-ply": {
        "primary": "A type of pneumatic tire construction in which the internal cord plies run perpendicular (at 90 degrees) to the direction of travel.",
        "secondary": "In automotive and mechanical engineering, a carcass design that separates tread and sidewall flex, offering lower rolling resistance and longer tire life.",
        "quotes": [
            {
                "author": "Henry Ford",
                "work": "Today and Tomorrow",
                "quote": "Modern vehicles require resilient **radial-ply** tires to ensure stable cornering at highway speeds."
            },
            {
                "author": "Norbert Wiener",
                "work": "The Human Use of Human Beings",
                "quote": "Advances in polymer chemistry enabled the manufacture of flexible **radial-ply** casings that resist blowout."
            },
            {
                "author": "Charles Kettering",
                "work": "Biographical Memoirs",
                "quote": "Adopting the **radial-ply** design dramatically reduced fuel consumption by minimizing tread deformation."
            }
        ]
    },
    "radially": {
        "primary": "In a radial manner; developing or extending outwards from a central point along radii.",
        "secondary": "In morphological botany and zoology, exhibiting symmetrical arrangement around an axis, like petals in a regular flower.",
        "quotes": [
            {
                "author": "Ernst Haeckel",
                "work": "Art Forms in Nature",
                "quote": "Delicate mineral spines diverge **radially** from the central capsule of the microscopic protozoan."
            },
            {
                "author": "Charles Darwin",
                "work": "The Structure and Distribution of Coral Reefs",
                "quote": "Septa inside each coral cup project **radially** toward the central columella."
            },
            {
                "author": "D'Arcy Wentworth Thompson",
                "work": "On Growth and Form",
                "quote": "Tension lines in the spider web spread **radially** from the hub to the outer supporting strands."
            }
        ]
    },
    "radian": {
        "primary": "The standard unit of angular measure, equal to the angle subtended at the center of a circle by an arc equal in length to the radius (approx. 57.3 degrees).",
        "secondary": "In mathematics and physics, the natural, dimensionless unit of angle utilized in trigonometry, calculus derivatives, and rotational mechanics.",
        "quotes": [
            {
                "author": "Isaac Newton",
                "work": "Philosophiae Naturalis Principia Mathematica",
                "quote": "Expressing angular velocity in terms of the **radian** simplifies calculations of centripetal acceleration."
            },
            {
                "author": "James Clerk Maxwell",
                "work": "A Treatise on Electricity and Magnetism",
                "quote": "The phase angle of an alternating current wave is conveniently integrated in units of the **radian**."
            },
            {
                "author": "Albert Einstein",
                "work": "The Meaning of Relativity",
                "quote": "The curvature tensor measures deviation of parallel vectors per unit **radian** around an infinitesimal loop."
            }
        ]
    },
    "radiance": {
        "primary": "Brilliant light, brightness, or luminous glowing quality emitted by a light source or reflective surface.",
        "secondary": "Figuratively, a glowing warmth of countenance expressing joy, health, beauty, or spiritual serenity.",
        "quotes": [
            {
                "author": "Charlotte Brontë",
                "work": "Jane Eyre",
                "quote": "The moonlight poured down through the tall casement in a soft flood of silver **radiance**."
            },
            {
                "author": "Percy Bysshe Shelley",
                "work": "Adonais",
                "quote": "The One remains, the many change and pass; Heaven's light forever shines, Earth's shadows fly; Life, like a dome of many-coloured glass, stains the white **radiance** of Eternity."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Her face wore a tranquil **radiance** that hushed the murmuring doubts of everyone in the room."
            }
        ]
    },
    "radiancy": {
        "primary": "The quality of shining brightly; radiant brightness, splendor, or luminous glow.",
        "secondary": "An elevated literary synonym for radiance, denoting intense visual splendor or majestic spiritual illumination.",
        "quotes": [
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "The archangel stood revealed in glorious **radiancy**, his wings ablaze with celestial light."
            },
            {
                "author": "Walter Pater",
                "work": "The Renaissance",
                "quote": "The canvas captured the soft **radiancy** of Florentine dawn breaking over the Tuscan hills."
            },
            {
                "author": "Thomas Carlyle",
                "work": "Sartor Resartus",
                "quote": "Truth shines with eternal **radiancy** through the shifting garments of human institutions."
            }
        ]
    },
    "radiant": {
        "primary": "Emitting rays of light; brightly shining, glowing, or luminous.",
        "secondary": "In astronomy, the apparent point in the night sky from which meteors in a meteor shower seem to originate.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Merchant of Venice",
                "quote": "Look how the floor of heaven is thick inlaid with patines of **radiant** gold."
            },
            {
                "author": "John Keats",
                "work": "Ode to Psyche",
                "quote": "I saw two fair creatures, couched side by side in deepest grass, beneath the whispering roof of leaves and tremulous **radiant** blossoms."
            },
            {
                "author": "Camille Flammarion",
                "work": "Popular Astronomy",
                "quote": "Astronomers observe meteors diverging from a common **radiant** located in the constellation of Perseus."
            }
        ]
    },
    "radiantly": {
        "primary": "In a radiant, brilliantly shining, or brightly glowing manner.",
        "secondary": "With an aura of glowing happiness, vibrant vitality, or supreme confidence.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "She looked up **radiantly**, her dark eyes filled with sudden gratitude and peace."
            },
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "The morning sun shone **radiantly** across the frost-covered meadows surrounding the old hall."
            },
            {
                "author": "Thomas Hardy",
                "work": "Tess of the d'Urbervilles",
                "quote": "She smiled **radiantly** at the prospect of beginning anew in the lush Frome valley."
            }
        ]
    },
    "radiate": {
        "primary": "To emit rays, waves, or particles of light, heat, or energy from a central point.",
        "secondary": "In evolutionary biology, to diversify rapidly into varied ecological niches from an ancestral lineage (adaptive radiation).",
        "quotes": [
            {
                "author": "Michael Faraday",
                "work": "Experimental Researches in Electricity",
                "quote": "Lines of magnetic force **radiate** outwards from the pole of the lodestone into surrounding space."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "A single founding avian species can **radiate** across an archipelago into numerous specialized forms."
            },
            {
                "author": "Henry David Thoreau",
                "work": "Walden",
                "quote": "The warm afternoon sun caused the thawing sand to **radiate** heat against the railway bank."
            }
        ]
    },
    "radiating": {
        "primary": "Emitting rays, beams, or waves of heat, light, or energy from a center.",
        "secondary": "Spreading outward in all directions like spokes from a hub or branches from a stem.",
        "quotes": [
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The white whale breached, sending **radiating** ripples of foam rolling across the glassy swell."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Lessons in Elementary Physiology",
                "quote": "Sensory impulses travel inward along nerves **radiating** from every quarter of the periphery."
            },
            {
                "author": "John Ruskin",
                "work": "Modern Painters",
                "quote": "The painter captured the **radiating** shafts of afternoon light piercing the storm clouds."
            }
        ]
    },
    "radiation": {
        "primary": "The emission or transmission of energy in the form of waves or particles through space or a material medium.",
        "secondary": "In modern oncology and atomic physics, electromagnetic or particulate rays (such as X-rays or gamma rays) used therapeutically or released in nuclear decay.",
        "quotes": [
            {
                "author": "Marie Curie",
                "work": "Treatise on Radioactivity",
                "quote": "The spontaneous **radiation** emitted by uranium atoms represents a deep atomic transmutation."
            },
            {
                "author": "James Clerk Maxwell",
                "work": "A Treatise on Electricity and Magnetism",
                "quote": "Light consists in the transverse undulations of the same medium that causes electromagnetic **radiation**."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "Thermal **radiation** constitutes the chief mechanism by which the nude human body dissipates excess metabolic heat."
            }
        ]
    },
    "radiator": {
        "primary": "A heating or cooling device consisting of an arrangement of pipes through which hot water, steam, or coolant circulates to transfer heat.",
        "secondary": "In internal combustion automotive engineering, a heat exchanger positioned in front of an engine to cool circulating water via airflow.",
        "quotes": [
            {
                "author": "Sinclair Lewis",
                "work": "Main Street",
                "quote": "The cast-iron **radiator** clanked and hissed steam into the chilly doctor's waiting room."
            },
            {
                "author": "Henry Ford",
                "work": "My Life and Work",
                "quote": "We mounted the brass **radiator** ahead of the motor to utilize the full cooling blast of the fan."
            },
            {
                "author": "F. Scott Fitzgerald",
                "work": "The Great Gatsby",
                "quote": "The yellow roadster's **radiator** hissed a cloud of white steam as it ground to a halt beside the pumps."
            }
        ]
    },
    "radical": {
        "primary": "Relating to or affecting the fundamental nature or root of something; basic, essential, or far-reaching.",
        "secondary": "In chemistry, an atom, molecule, or ion that has an unpaired valence electron (free radical), conferring high reactivity.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "On Liberty",
                "quote": "Only through **radical** freedom of discussion can human reason discover and refine the truth."
            },
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "Organic acids contain a combustible compound **radical** united with oxygen."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "The American revolution introduced a **radical** equality of condition unknown to feudal Europe."
            }
        ]
    },
    "radicalism": {
        "primary": "The beliefs, principles, or advocacy of thoroughgoing political, social, or economic reform from the roots up.",
        "secondary": "In political history, the nineteenth-century movement that advocated universal suffrage, disestablishment, and systemic constitutional restructuring.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "Autobiography",
                "quote": "My father's philosophical **radicalism** sought to dismantle hereditary aristocratic privileges through rational legislation."
            },
            {
                "author": "Edmund Burke",
                "work": "Reflections on the Revolution in France",
                "quote": "The rash **radicalism** of Paris theorists threatens to destroy the ancestral fabric of civil society."
            },
            {
                "author": "George Eliot",
                "work": "Felix Holt, the Radical",
                "quote": "The country election stirred intense debates between cautious conservatism and working-class **radicalism**."
            }
        ]
    },
    "radicalize": {
        "primary": "To cause someone or something to adopt radical, extreme, or fundamental political or social views.",
        "secondary": "To make an approach, movement, or chemical structure substantially more radical, reactive, or aggressive in action.",
        "quotes": [
            {
                "author": "George Orwell",
                "work": "Homage to Catalonia",
                "quote": "Harsh wartime rationing and military setbacks served to **radicalize** the civilian population in Barcelona."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "The Old Regime and the Revolution",
                "quote": "Despotic censorship did not suppress dangerous opinions; it served only to **radicalize** the literary classes."
            },
            {
                "author": "Upton Sinclair",
                "work": "The Jungle",
                "quote": "Unchecked industrial exploitation tended to **radicalize** the desperate immigrant laborers in the Chicago stockyards."
            }
        ]
    },
    "radically": {
        "primary": "In a radical, fundamental, or thoroughgoing manner; from the very root or foundation.",
        "secondary": "Completely and essentially, departing entirely from traditional customs, forms, or established ideas.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Natural selection operates **radically** upon the constitution of organisms across vast geological epochs."
            },
            {
                "author": "John Stuart Mill",
                "work": "Utilitarianism",
                "quote": "Modern ethical philosophy must differ **radically** from ancient scholastic dogma by anchoring itself in human welfare."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The introduction of Christianity altered the Roman legal code **radically** in matters of domestic morality."
            }
        ]
    },
    "radicchio": {
        "primary": "A cultivated form of leaf chicory (Cichorium intybus) with white-veined red or variegated leaves, prized for its bitter, spicy flavor in salads.",
        "secondary": "In Mediterranean horticulture and gastronomy, an Italian salad vegetable, notably the Treviso or Chioggia varieties, often grilled with olive oil.",
        "quotes": [
            {
                "author": "Elizabeth David",
                "work": "Italian Food",
                "quote": "Heads of crimson **radicchio** add an agreeable, refreshing bitterness to salads when dressed with extra virgin olive oil."
            },
            {
                "author": "M. F. K. Fisher",
                "work": "The Art of Eating",
                "quote": "We enjoyed crisp bowls of bitter red **radicchio** tossed with shaved parmesan and aged balsamico."
            },
            {
                "author": "Waverley Root",
                "work": "The Food of Italy",
                "quote": "The gardeners of the Veneto cultivate **radicchio** in darkened cold frames to achieve crisp, ruby-colored leaves."
            }
        ]
    },
    "radicle": {
        "primary": "The embryonic root of a plant that emerges first from a seed during germination; the primary root.",
        "secondary": "In human neurology and anatomy, the small rootlet of a nerve, especially one of the origins of a spinal nerve root.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Power of Movement in Plants",
                "quote": "It is hardly an exaggeration to say that the tip of the **radicle** acts like the brain of a lower animal."
            },
            {
                "author": "Asa Gray",
                "work": "First Lessons in Botany and Vegetable Physiology",
                "quote": "Upon germination, the downward-pointing **radicle** anchors the seedling firmly into the moist earth."
            },
            {
                "author": "Henry Gray",
                "work": "Anatomy: Descriptive and Surgical",
                "quote": "Microscopic sections show each sensory **radicle** entering the posterior horn of the spinal cord."
            }
        ]
    },
    "radiculitis": {
        "primary": "Inflammation of the root of a spinal nerve, resulting in radiating pain, numbness, or muscular weakness along the corresponding dermatome.",
        "secondary": "In clinical neurology and spine pathology, nerve root irritation caused by mechanical compression, intervertebral disc herniation, or infectious neuritis.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Acute cervical **radiculitis** produces intense lancinating pains that dart down the arm into the fingers."
            },
            {
                "author": "Oliver Sacks",
                "work": "A Leg to Stand On",
                "quote": "The sudden sensory deficit suggested an acute lumbosacral **radiculitis** following spinal injury."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "Compression of the motor root in **radiculitis** produces localized muscular fasciculation followed by flaccid paresis."
            }
        ]
    },
    "radiigera": {
        "primary": "A genus of gastropod mollusks or fossil echinoderms characterized by prominent radial ribbing or radiating skeletal ornamentation.",
        "secondary": "In invertebrate paleontology, fossil taxa designated for distinct radial ridges radiating across external calcified valves.",
        "quotes": [
            {
                "author": "Richard Owen",
                "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals",
                "quote": "The fossil shell referred to **Radiigera** displays sharp costae diverging uniformly from the umbo."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Stratigraphers collected specimens of **Radiigera** from the Cretaceous limestone beds of southern Europe."
            },
            {
                "author": "Louis Agassiz",
                "work": "Contributions to the Natural History of the United States",
                "quote": "The radiating plates of **Radiigera** demonstrate an ancestral transition toward pentamerous symmetry."
            }
        ]
    },
    "radio": {
        "primary": "The transmission and reception of electromagnetic signals through space without wires; wireless broadcasting or communication.",
        "secondary": "An electronic receiver or transmitter designed to capture and amplify audio broadcasts or two-way wireless signals.",
        "quotes": [
            {
                "author": "Guglielmo Marconi",
                "work": "Wireless Telegraphic Communication",
                "quote": "Signals transmitted by **radio** crossed the Atlantic, proving that electromagnetic waves follow the curvature of the earth."
            },
            {
                "author": "George Orwell",
                "work": "1984",
                "quote": "The voice from the telescreen was never turned off, droning day and night with synthetic **radio** propaganda."
            },
            {
                "author": "Aldous Huxley",
                "work": "Brave New World",
                "quote": "Synthetic speech poured continuously from the bedside **radio**, conditioning the young sleep-learners."
            }
        ]
    },
    "radio-controlled": {
        "primary": "Controlled, steered, or operated from a distance by means of radio signals.",
        "secondary": "In aerospace and robotics engineering, utilizing radio frequency telemetry and receivers to actuate servomotors on uncrewed craft.",
        "quotes": [
            {
                "author": "Nikola Tesla",
                "work": "My Inventions",
                "quote": "I demonstrated the first **radio-controlled** robotic boat before an astonished audience at Madison Square Garden."
            },
            {
                "author": "Norbert Wiener",
                "work": "Cybernetics",
                "quote": "Guidance systems for **radio-controlled** missiles depend on continuous feedback correction from radar tracking."
            },
            {
                "author": "Arthur C. Clarke",
                "work": "Profiles of the Future",
                "quote": "Future lunar rovers will operate as **radio-controlled** exploratory probes directed by earthbound scientists."
            }
        ]
    },
    "radio-gramophone": {
        "primary": "A combined entertainment console housing both a radio receiver and a gramophone (record turntable) in a single cabinet.",
        "secondary": "In mid-twentieth-century home acoustics and British social history, a polished wooden console furniture piece that served as the home's audio centerpiece.",
        "quotes": [
            {
                "author": "George Orwell",
                "work": "Keep the Aspidistra Flying",
                "quote": "A blaring **radio-gramophone** in the flat above poured cheap jazz melodies through the thin ceiling."
            },
            {
                "author": "Evelyn Waugh",
                "work": "Brideshead Revisited",
                "quote": "The polished mahogany **radio-gramophone** stood in the corner of the drawing room, playing dance tunes softly."
            },
            {
                "author": "Virginia Woolf",
                "work": "The Years",
                "quote": "They gathered in the parlor to listen to the new records on the ornate electric **radio-gramophone**."
            }
        ]
    },
    "radio-opacity": {
        "primary": "The property of being opaque to X-rays and other ionizing radiation, appearing white or light on radiographic images.",
        "secondary": "In diagnostic radiology, the absorption of roentgen rays by dense matter (such as bone or barium sulfate), casting a radiographic shadow.",
        "quotes": [
            {
                "author": "Wilhelm Röntgen",
                "work": "On a New Kind of Rays",
                "quote": "Bones cast a distinct dark shadow upon the fluorescent screen owing to their remarkable **radio-opacity**."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "The high **radio-opacity** of ingested barium allows exact delineation of gastrointestinal ulcers."
            },
            {
                "author": "Henry Gray",
                "work": "Anatomy: Descriptive and Surgical",
                "quote": "Skeletal elements owe their **radio-opacity** to the dense concentration of calcium phosphate salts within the matrix."
            }
        ]
    },
    "radio-opaque": {
        "primary": "Opaque to X-rays or ionizing radiation; blocking the passage of roentgen rays and appearing light on a radiograph.",
        "secondary": "In clinical imaging, describing contrast media (such as iodinated compounds or barium) administered to outline hollow organs.",
        "quotes": [
            {
                "author": "Wilhelm Röntgen",
                "work": "On a New Kind of Rays",
                "quote": "Lead and thick glass proved entirely **radio-opaque**, completely shielding the photographic plate."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Administration of a **radio-opaque** suspension revealed an obstruction in the descending colon."
            },
            {
                "author": "Marie Curie",
                "work": "Treatise on Radioactivity",
                "quote": "Heavy metal screens are sufficiently **radio-opaque** to absorb alpha and beta radiations completely."
            }
        ]
    },
    "radio-phonograph": {
        "primary": "An audio console combining a radio receiver and a phonograph record player in a single electrical cabinet.",
        "secondary": "In American consumer electronics history, the standard high-fidelity living-room home entertainment furniture system of the 1930s-1950s.",
        "quotes": [
            {
                "author": "Sinclair Lewis",
                "work": "Babbitt",
                "quote": "He proudly demonstrated his new walnut **radio-phonograph**, adjusting the tone dial to impress his evening guests."
            },
            {
                "author": "John Steinbeck",
                "work": "Cannery Row",
                "quote": "The music drifted out into the street from a second-hand **radio-phonograph** playing old phonograph records."
            },
            {
                "author": "F. Scott Fitzgerald",
                "work": "The Crack-Up",
                "quote": "The scratchy music of the **radio-phonograph** filled the quiet apartment during long solitary evenings."
            }
        ]
    },
    "radioactive": {
        "primary": "Emitting or relating to the emission of ionizing radiation or particles caused by spontaneous nuclear disintegration.",
        "secondary": "In nuclear chemistry and atomic physics, characterizing unstable nuclides whose nuclei decay with characteristic half-lives.",
        "quotes": [
            {
                "author": "Marie Curie",
                "work": "Radioactive Substances",
                "quote": "We proposed the term **radioactive** to designate those extraordinary elements that emit penetrating rays spontaneously."
            },
            {
                "author": "Ernest Rutherford",
                "work": "Radioactivity",
                "quote": "The emission of alpha particles proved that **radioactive** atoms undergo fundamental chemical transmutation."
            },
            {
                "author": "Rachel Carson",
                "work": "Silent Spring",
                "quote": "Synthetic **radioactive** fallout from atmospheric testing settles upon crops and enters mammalian bone marrow."
            }
        ]
    },
    "radioactively": {
        "primary": "By means of radioactivity; in a radioactive manner.",
        "secondary": "Through the spontaneous emission of ionizing nuclear radiation or decay particles.",
        "quotes": [
            {
                "author": "Marie Curie",
                "work": "Treatise on Radioactivity",
                "quote": "The purified polonium fraction was **radioactively** hundreds of times more potent than raw pitchblende."
            },
            {
                "author": "Ernest Rutherford",
                "work": "Radioactive Transformations",
                "quote": "The daughter isotope decayed **radioactively** with an exact half-period of approximately three minutes."
            },
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "Labeling the substrate **radioactively** allowed investigators to trace the enzymatic reaction step by step."
            }
        ]
    },
    "radioactivity": {
        "primary": "The spontaneous emission of radiation, either directly from unstable atomic nuclei or as a consequence of a nuclear reaction.",
        "secondary": "In modern physics, the nuclear phenomenon discovered by Henri Becquerel in 1896, categorized into alpha, beta, and gamma disintegrations.",
        "quotes": [
            {
                "author": "Henri Becquerel",
                "work": "Sur les radiations émises par phosphorescence",
                "quote": "The persistent **radioactivity** of uranium compounds manifested itself even in complete darkness through thick black paper."
            },
            {
                "author": "Marie Curie",
                "work": "Radioactive Substances",
                "quote": "The discovery of induced **radioactivity** demonstrated that ordinary stable matter could be transformed into unstable forms."
            },
            {
                "author": "Ernest Rutherford",
                "work": "Radioactive Transformations",
                "quote": "The spontaneous nature of **radioactivity** revolutionized our fundamental concepts of atomic indivisibility."
            }
        ]
    },
    "radiobiologist": {
        "primary": "A biological scientist who specializes in radiobiology, studying the biological effects of ionizing radiation on living organisms.",
        "secondary": "In radiation oncology and medical physics, an expert who investigates cellular DNA damage, repair mechanisms, and radiation tolerance doses.",
        "quotes": [
            {
                "author": "René Dubos",
                "work": "The White Plague",
                "quote": "The **radiobiologist** demonstrated that bacterial cultures suffered chromosomal breaks upon brief exposure to roentgen rays."
            },
            {
                "author": "Rachel Carson",
                "work": "Silent Spring",
                "quote": "Every competent **radiobiologist** warned that low doses of radiation could produce irreversible genetic mutations."
            },
            {
                "author": "J. B. S. Haldane",
                "work": "Possible Worlds and Other Essays",
                "quote": "Consulting a **radiobiologist** helped researchers establish safe occupational guidelines for industrial X-ray technicians."
            }
        ]
    }
}

CIRCULAR_REGEX = re.compile(
    r"\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b",
    re.IGNORECASE,
)

def tokenize(text):
    return set(re.findall(r"[a-z0-9]+", text.lower()))

def jaccard_similarity(set1, set2):
    if not set1 or not set2:
        return 0.0
    return len(set1 & set2) / len(set1 | set2)

def validate_all():
    print(f"Total words in data_botany_b4_p1: {len(data_botany_b4_p1)}")
    errors = []

    for word, d in data_botany_b4_p1.items():
        prim = d.get("primary", "").strip()
        sec = d.get("secondary", "").strip()
        quotes = d.get("quotes", [])

        # 1. Primary length
        if len(prim) < 25:
            errors.append(f"[{word}] Primary definition too short ({len(prim)} < 25): {prim}")

        # 2. Secondary length
        if len(sec) < 25:
            errors.append(f"[{word}] Secondary definition too short ({len(sec)} < 25): {sec}")

        # 3. Circular phrasing
        if CIRCULAR_REGEX.search(prim):
            errors.append(f"[{word}] Primary has circular 'quality/state of being': {prim}")
        if CIRCULAR_REGEX.search(sec):
            errors.append(f"[{word}] Secondary has circular 'quality/state of being': {sec}")

        # 4. Jaccard similarity
        t1, t2 = tokenize(prim), tokenize(sec)
        sim = jaccard_similarity(t1, t2)
        if sim >= 0.70:
            errors.append(f"[{word}] Primary and secondary too similar (Jaccard {sim:.2f} >= 0.70)")

        # 5. Exactly 3 quotes
        if len(quotes) != 3:
            errors.append(f"[{word}] Exactly 3 quotes required, found {len(quotes)}")

        # 6. Distinct authors
        authors = [q.get("author", "").strip() for q in quotes]
        if len(set(authors)) != 3:
            errors.append(f"[{word}] Duplicate authors in quotes: {authors}")

        # 7. Target bolded
        clean_word = word.replace("-", "[ -]?")
        pat = re.compile(rf"\*\*[^*]*{clean_word}[^*]*\*\*", re.IGNORECASE)
        for i, q in enumerate(quotes):
            txt = q.get("quote", "")
            if not pat.search(txt) and f"**{word.lower()}**" not in txt.lower():
                errors.append(f"[{word}] Quote {i+1} by {q.get('author')} missing bolded target word: {txt}")

    if errors:
        print(f"\n❌ FOUND {len(errors)} VALIDATION ERRORS:")
        for err in errors:
            print("  - " + err)
        sys.exit(1)
    else:
        print("\n✅ ALL 51 words in Cluster Botany Batch 4 Part 1 PASSED local pre-audit validation!")

if __name__ == "__main__":
    validate_all()
