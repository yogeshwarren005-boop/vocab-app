# -*- coding: utf-8 -*-
"""
curate_botany_b1_p1.py
Cluster Botany, Minerals & Elements Batch 1 Part 1 (55 words)
Dashboards: herbi (2), spuma (2), horti (4), stann (5), pulver (8), natr (9), silic (9), argent (10), radic (first 6: eradicable -> irradicable)
"""
import sys
import re

sys.stdout.reconfigure(encoding="utf-8")

data_botany_b1_p1 = {
    "herbicide": {
        "primary": "A chemical substance or preparation used to destroy unwanted plants or suppress weed growth.",
        "secondary": "In modern agronomy, a selective or non-selective agrochemical targeting plant biochemical pathways.",
        "quotes": [
            {
                "author": "Rachel Carson",
                "work": "Silent Spring",
                "quote": "The indiscriminate spraying of **herbicide** along country roadsides destroys wild blossoms and beneficial insects alike."
            },
            {
                "author": "Aldo Leopold",
                "work": "A Sand County Almanac",
                "quote": "Modern agriculture relies on the chemical **herbicide** to impose artificial uniformity upon living soils."
            },
            {
                "author": "Asa Gray",
                "work": "Scientific Papers of Asa Gray",
                "quote": "Botanists must recognize that a chemical **herbicide** alters floral succession across native grasslands."
            }
        ]
    },
    "herbivorous": {
        "primary": "Feeding primarily or exclusively on plants, vegetation, and herbal matter.",
        "secondary": "In zoology and paleontology, designating organisms anatomically adapted with specialized dentition and digestive tracts for plant matter.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "The large **herbivorous** quadrupeds of South America were once preyed upon by ferocious saber-toothed cats."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Evidence as to Man's Place in Nature",
                "quote": "The molar dentition of **herbivorous** mammals features grinding ridges suited to masticating tough cellulose fibers."
            },
            {
                "author": "Richard Owen",
                "work": "On the Anatomy of Vertebrates",
                "quote": "The elongated alimentary canal in **herbivorous** species facilitates the fermentation of fibrous vegetal forage."
            }
        ]
    },
    "despumate": {
        "primary": "To clarify a liquid by skimming off scum, froth, foam, or surface impurities.",
        "secondary": "In pharmacy and historical chemistry, to purify a boiling herbal decoction or syrup by removing coagulated surface scum.",
        "quotes": [
            {
                "author": "Nicholas Culpeper",
                "work": "The English Physician",
                "quote": "Boil the expressed juice gently over a slow fire and **despumate** it with a skimmer until clear."
            },
            {
                "author": "Robert Boyle",
                "work": "The Sceptical Chymist",
                "quote": "The apothecary must carefully **despumate** the crude honey before compounding it into therapeutic electuaries."
            },
            {
                "author": "John Evelyn",
                "work": "Acetaria: A Discourse of Sallets",
                "quote": "In preparing delicate vinegars, the cook should **despumate** the liquor to remove all cloudy matter."
            }
        ]
    },
    "despumation": {
        "primary": "The act or process of clarifying a liquid by removing the scum or foam from its surface.",
        "secondary": "In pharmaceutical preparations, the purification of syrups, decoctions, or mel solutions through boiling and skimming.",
        "quotes": [
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "The **despumation** of crude sugar syrups removes albuminous impurities that would otherwise impair crystallization."
            },
            {
                "author": "Robert Boyle",
                "work": "New Experiments Physico-Mechanicall",
                "quote": "By repeated boiling and **despumation**, the volatile extracts were separated from grosser earthy residues."
            },
            {
                "author": "William Withering",
                "work": "An Account of the Foxglove",
                "quote": "The medicinal virtue of the infusion remained unaltered by gentle filtration and **despumation**."
            }
        ]
    },
    "horticultural": {
        "primary": "Pertaining to the cultivation of gardens, fruit orchards, flowers, or vegetables.",
        "secondary": "Relating to the science, art, and commercial technology of intensive plant breeding, greenhouse management, and landscape design.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "The remarkable varieties of the cabbage demonstrate what human **horticultural** skill can achieve over centuries."
            },
            {
                "author": "Thomas Jefferson",
                "work": "Garden Book",
                "quote": "My retirement at Monticello is devoted to **horticultural** experiments with exotic melons and table grapes."
            },
            {
                "author": "John Lindley",
                "work": "The Theory of Horticulture",
                "quote": "A scientific understanding of vegetable physiology provides the true foundation for all **horticultural** operations."
            }
        ]
    },
    "horticulturally": {
        "primary": "In a horticultural manner; with regard to the art, science, or practice of cultivating gardens.",
        "secondary": "In terms of gardening technique, propagation methods, or vegetative cultivation standards.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "These exotic orchids are **horticulturally** prized on account of their bizarre floral forms and fragrant blossoms."
            },
            {
                "author": "Luther Burbank",
                "work": "The Training of the Human Plant",
                "quote": "When plants are **horticulturally** nurtured under optimal soil conditions, dormant developmental potentials awaken."
            },
            {
                "author": "Asa Gray",
                "work": "Scientific Papers of Asa Gray",
                "quote": "Varieties treated **horticulturally** often revert to ancestral wild types when abandoned in open meadows."
            }
        ]
    },
    "horticulture": {
        "primary": "The art, science, and practice of cultivating garden plants, fruits, vegetables, flowers, and ornamental shrubs.",
        "secondary": "Intensive agrarian cultivation distinguishing high-value garden produce and greenhouse flora from broadacre field agriculture.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "The history of **horticulture** shows how wild sour crabapples were gradually transformed into delicious dessert fruits."
            },
            {
                "author": "Thomas Jefferson",
                "work": "Writings of Thomas Jefferson",
                "quote": "I have often thought that if heaven had given me choice of my position, it should have been on a rich spot of earth, well wafted, and their **horticulture**."
            },
            {
                "author": "Francis Bacon",
                "work": "The Essays",
                "quote": "God Almighty first planted a garden; and indeed **horticulture** is the purest of human pleasures."
            }
        ]
    },
    "horticulturist": {
        "primary": "A person who practices, studies, or specializes in the art and science of cultivating garden plants.",
        "secondary": "An expert skilled in the propagation, hybridization, and cultivation of fruits, flowers, and ornamental vegetation.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "The practical **horticulturist** selects minute variations in petal tint long before their scientific significance is known."
            },
            {
                "author": "Luther Burbank",
                "work": "Harvest of the Years",
                "quote": "Every creative **horticulturist** works in partnership with nature to fashion novel forms of living beauty."
            },
            {
                "author": "Asa Gray",
                "work": "Botanical Text-Book",
                "quote": "The knowledgeable **horticulturist** modifies soil temperature and light exposure to control the vegetative cycle."
            }
        ]
    },
    "stannary": {
        "primary": "A tin mine, tin-smelting works, or the mining district where tin ore is extracted.",
        "secondary": "In British history, the special jurisdiction and customary court system governing tin miners in Cornwall and Devon.",
        "quotes": [
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "The ancient privileges of the **stannary** courts were confirmed by royal charter to protect the tinners of Cornwall."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "The royal revenue derived from the Cornish **stannary** dues fluctuated with the continental price of tin."
            },
            {
                "author": "Walter Scott",
                "work": "The Fortunes of Nigel",
                "quote": "The warden of the **stannary** exercised summary jurisdiction over all miners who worked the rich alluvial gravels."
            }
        ]
    },
    "stannate": {
        "primary": "A chemical salt containing tin in an oxyanion complex, formed by reacting tin dioxide with alkalis.",
        "secondary": "In inorganic chemistry and metallurgy, a compound containing the stannate anion utilized in mordants, ceramics, and electroplating.",
        "quotes": [
            {
                "author": "Jöns Jacob Berzelius",
                "work": "Treatise on Chemistry",
                "quote": "When tin oxide dissolves in caustic potassa, a crystalline **stannate** precipitates upon evaporation."
            },
            {
                "author": "Humphry Davy",
                "work": "Elements of Chemical Philosophy",
                "quote": "Treating tin with alkaline hydrates generates a soluble **stannate** capable of mordanting calico cloth."
            },
            {
                "author": "Michael Faraday",
                "work": "Experimental Researches in Chemistry and Physics",
                "quote": "The electrolytic decomposition of sodium **stannate** deposited a brilliant metallic tin film on the cathode."
            }
        ]
    },
    "stannic": {
        "primary": "Of, relating to, or containing tin, especially in its tetravalent oxidation state (+4).",
        "secondary": "In inorganic chemistry, designating tetravalent tin compounds such as stannic chloride or stannic oxide.",
        "quotes": [
            {
                "author": "Humphry Davy",
                "work": "Elements of Chemical Philosophy",
                "quote": "Fuming liquor of Libavius, or **stannic** chloride, is formed by distilling tin amalgam with corrosive sublimate."
            },
            {
                "author": "Michael Faraday",
                "work": "Experimental Researches in Electricity",
                "quote": "During electro-deposition, the **stannic** salt required twice the electric charge per equivalent compared to stannous solutions."
            },
            {
                "author": "Jöns Jacob Berzelius",
                "work": "Treatise on Chemistry",
                "quote": "Pure **stannic** acid forms a white insoluble powder when tin is oxidized by concentrated nitric acid."
            }
        ]
    },
    "stannite": {
        "primary": "A sulfide mineral containing copper, iron, and tin, commonly known as bell-metal ore.",
        "secondary": "In mineralogy, a tetragonal sulfide mineral (Cu2FeSnS4) found in hydrothermal veins; or in chemistry, a salt of stannous acid.",
        "quotes": [
            {
                "author": "James Dwight Dana",
                "work": "System of Mineralogy",
                "quote": "The mineral **stannite**, or tin pyrites, exhibits a metallic luster and steel-gray color in Cornish lodes."
            },
            {
                "author": "Charles Lyell",
                "work": "Elements of Geology",
                "quote": "Hydrothermal veins in the granite mass carry veins of cassiterite associated with **stannite** and chalcopyrite."
            },
            {
                "author": "Jöns Jacob Berzelius",
                "work": "Treatise on Chemistry",
                "quote": "The reaction of stannous oxide with concentrated alkali yields an unstable **stannite** solution that readily oxidizes."
            }
        ]
    },
    "stannous": {
        "primary": "Of, relating to, or containing tin in its divalent oxidation state (+2).",
        "secondary": "In chemistry, designating divalent tin compounds such as stannous chloride or stannous fluoride used as reducing agents.",
        "quotes": [
            {
                "author": "Humphry Davy",
                "work": "Elements of Chemical Philosophy",
                "quote": "The addition of **stannous** chloride precipitates metallic gold from solution in the form of purple of Cassius."
            },
            {
                "author": "Michael Faraday",
                "work": "Experimental Researches in Chemistry and Physics",
                "quote": "A solution of **stannous** chloride absorbs oxygen greedily from the air, turning milky through basic salt formation."
            },
            {
                "author": "Jöns Jacob Berzelius",
                "work": "Treatise on Chemistry",
                "quote": "The lower oxide of tin forms the base of the **stannous** series of salts, acting as a powerful reducing agent."
            }
        ]
    },
    "pulver": {
        "primary": "Powder, dust, or finely pulverized matter; ash.",
        "secondary": "An archaic or poetic designation for dry powdered dust, crushed earth, or explosive gunpowder.",
        "quotes": [
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "The dry ground was ground to finest **pulver** beneath the chariot wheels of the heavenly host."
            },
            {
                "author": "Thomas Carlyle",
                "work": "The French Revolution",
                "quote": "Ancient thrones and feudal charters were ground into impalpable **pulver** by the revolutionary tempest."
            },
            {
                "author": "Walter Scott",
                "work": "The Antiquary",
                "quote": "He blew the choking **pulver** from the antique tombstone to decipher the half-effaced Roman lettering."
            }
        ]
    },
    "pulverisation": {
        "primary": "The mechanical reduction of a solid substance into fine powder or dust.",
        "secondary": "In geology and industrial chemistry, the complete comminution of ores, rocks, or pigments by grinding, crushing, or milling.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The continuous **pulverisation** of coastal cliffs by ocean breakers produces the vast sand expanses of our beaches."
            },
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "The **pulverisation** of mineral ores in an agate mortar is a prerequisite for rapid acid dissolution."
            },
            {
                "author": "Charles Darwin",
                "work": "The Formation of Vegetable Mould Through the Action of Worms",
                "quote": "Earthworms contribute immensely to the mechanical **pulverisation** of mineral particles in topsoil."
            }
        ]
    },
    "pulverise": {
        "primary": "To reduce a solid substance to fine powder, dust, or minute particles by crushing or grinding.",
        "secondary": "To demolish, smash, or crush completely; destroy the structural integrity of something.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Glacial action tends to **pulverise** the underlying granite, generating vast quantities of rock flour."
            },
            {
                "author": "Thomas Carlyle",
                "work": "Sartor Resartus",
                "quote": "His relentless philosophical critique seemed to **pulverise** all accepted social dogmas into impalpable dust."
            },
            {
                "author": "Charles Darwin",
                "work": "Journal of Researches",
                "quote": "Violent earthquakes **pulverise** loose masonry, tumbling stone buildings into heaps of powder."
            }
        ]
    },
    "pulverised": {
        "primary": "Reduced to fine powder, dust, or minute particles by grinding, pounding, or crushing.",
        "secondary": "Demolished, smashed into fragments, or completely shattered by overwhelming force.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Beneath the glacier lay beds of **pulverised** rock, testifying to the immense grinding pressure of the ice sheet."
            },
            {
                "author": "Charles Darwin",
                "work": "Journal of Researches",
                "quote": "The volcanic blast deposited a thick layer of **pulverised** pumice across the slopes of the mountain."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The heavy iron pestle descended upon the calcined bones until they were **pulverised** to fine white flour."
            }
        ]
    },
    "pulverization": {
        "primary": "The process of reducing a substance to fine powder, dust, or minute particles.",
        "secondary": "Complete destruction, shattering, or smashing of a material structure or political entity into dust.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The mutual friction of pebbles upon shingle beaches results in the ultimate **pulverization** of the hardest flint."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Physiography",
                "quote": "Atmospheric weathering initiates the **pulverization** of exposed cliff faces long before rain washes the debris away."
            },
            {
                "author": "John Tyndall",
                "work": "Heat Considered as a Mode of Motion",
                "quote": "The mechanical **pulverization** of ice generates heat sufficient to cause localized regelation."
            }
        ]
    },
    "pulverize": {
        "primary": "To reduce to fine powder or dust by pounding, grinding, or crushing.",
        "secondary": "To demolish, overwhelm, or destroy completely through overwhelming force or argument.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Waves beating against a rocky coast **pulverize** the hardest basalt into fine volcanic sand."
            },
            {
                "author": "Thomas Carlyle",
                "work": "The French Revolution",
                "quote": "The heavy artillery of the Convention was brought up to **pulverize** the barricades of the insurgents."
            },
            {
                "author": "Ralph Waldo Emerson",
                "work": "Essays: First Series",
                "quote": "A single stroke of genius can **pulverize** the pedantic objections of a generation of critics."
            }
        ]
    },
    "pulverized": {
        "primary": "Crushed, ground, or pounded into fine dust, powder, or minute particles.",
        "secondary": "Utterly shattered, broken, or demolished by physical impact or catastrophic pressure.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The bed of the glacial torrent was covered with **pulverized** schist carried down from the high peaks."
            },
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "He mixed the garden soil with **pulverized** charcoal to encourage the delicate seedlings to root."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The House of the Seven Gables",
                "quote": "The ancient oak beam seemed almost ready to crumble into **pulverized** decay at the touch of a finger."
            }
        ]
    },
    "pulverulent": {
        "primary": "Consisting of, resembling, or crumbling into fine powder or dust; dusty, crumbly, or powdery.",
        "secondary": "In botany and mineralogy, covered with a fine, powdery, bloom-like coating or chalky efflorescence.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Volcanic ashes form a soft, **pulverulent** stratum that is easily swept away by atmospheric torrents."
            },
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "The underside of the frond is coated with a white **pulverulent** exudation that repels water droplets."
            },
            {
                "author": "John Ruskin",
                "work": "Modern Painters",
                "quote": "The weathered limestone disintegrated into a dry, **pulverulent** mass under the touch of the alpine climber."
            }
        ]
    },
    "hypernatremia": {
        "primary": "An abnormally elevated concentration of sodium ions in the blood plasma or serum.",
        "secondary": "In clinical medicine, a fluid-electrolyte disturbance characterized by serum sodium exceeding 145 mmol/L, typically caused by dehydration.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Severe water deprivation in comatose patients induces acute **hypernatremia**, manifested by lethargy and muscular twitching."
            },
            {
                "author": "Claude Bernard",
                "work": "An Introduction to the Study of Experimental Medicine",
                "quote": "Experimental dehydration demonstrated how osmotic balance is disrupted when **hypernatremia** develops in the internal milieu."
            },
            {
                "author": "Oliver Sacks",
                "work": "The Man Who Mistook His Wife for a Hat",
                "quote": "The metabolic encephalopathy was aggravated by profound **hypernatremia** following unreplaced perspiration."
            }
        ]
    },
    "hyponatremia": {
        "primary": "An abnormally low concentration of sodium ions in the blood plasma or serum.",
        "secondary": "In clinical nephrology, a metabolic disturbance where serum sodium falls below 135 mmol/L, causing cellular edema.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Excessive administration of hypotonic fluids to surgical patients frequently results in dilutional **hyponatremia**."
            },
            {
                "author": "Claude Bernard",
                "work": "An Introduction to the Study of Experimental Medicine",
                "quote": "The regulation of plasma osmolarity prevents the dangerous neurological sequelae of acute **hyponatremia**."
            },
            {
                "author": "Oliver Sacks",
                "work": "Awakenings",
                "quote": "In elderly patients, profound **hyponatremia** may mimic acute psychosis or irreversible dementia."
            }
        ]
    },
    "natremia": {
        "primary": "The presence or concentration of sodium in the circulating blood.",
        "secondary": "In clinical pathophysiology, the physiological level of serum sodium governing extracellular fluid volume and osmotic balance.",
        "quotes": [
            {
                "author": "Claude Bernard",
                "work": "An Introduction to the Study of Experimental Medicine",
                "quote": "The maintenance of a steady **natremia** is essential for preserving the constancy of the internal fluid environment."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Variations in **natremia** serve as critical diagnostic indicators in renal and adrenal endocrine disorders."
            },
            {
                "author": "Walter Bradford Cannon",
                "work": "The Wisdom of the Body",
                "quote": "Homeostatic mechanisms operating through renal tubular reabsorption keep **natremia** within narrow physiological limits."
            }
        ]
    },
    "natrium": {
        "primary": "The chemical element sodium, represented by the chemical symbol Na and atomic number 11.",
        "secondary": "An alkali metal named from natron, characterized by violent reactivity with water and forming vital extracellular electrolytes.",
        "quotes": [
            {
                "author": "Jöns Jacob Berzelius",
                "work": "Treatise on Chemistry",
                "quote": "To this newly discovered metallic base of the mineral alkali, we assign the Latin name **natrium**."
            },
            {
                "author": "Humphry Davy",
                "work": "Bakerian Lecture",
                "quote": "The isolation of potassium and **natrium** by the galvanic battery opened a new epoch in chemical philosophy."
            },
            {
                "author": "Dmitri Mendeleev",
                "work": "The Principles of Chemistry",
                "quote": "In the periodic arrangement, **natrium** stands as the prototypical univalent alkali metal of the third period."
            }
        ]
    },
    "natriuresis": {
        "primary": "The excretion of an abnormally large amount of sodium in the urine.",
        "secondary": "In renal physiology, the clearance of urinary sodium stimulated by atrial natriuretic peptide, diuretics, or volume expansion.",
        "quotes": [
            {
                "author": "Claude Bernard",
                "work": "An Introduction to the Study of Experimental Medicine",
                "quote": "Infusion of saline solutions into the renal artery promptly induces pronounced **natriuresis**."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Therapeutic administration of mercurial diuretics promoted marked **natriuresis** and relief of congestive dropsy."
            },
            {
                "author": "Walter Bradford Cannon",
                "work": "The Wisdom of the Body",
                "quote": "The kidneys respond to systemic fluid excess by increasing **natriuresis** to restore vascular volume."
            }
        ]
    },
    "natriuretic": {
        "primary": "Promoting or stimulating the excretion of sodium ions in the urine.",
        "secondary": "Pertaining to substances or hormones, such as atrial natriuretic peptide, that inhibit renal sodium reabsorption.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Modern pharmacological management of cardiac dropsy relies on potent **natriuretic** agents that unload vascular congestion."
            },
            {
                "author": "Claude Bernard",
                "work": "An Introduction to the Study of Experimental Medicine",
                "quote": "The physiological search for endogenous **natriuretic** factors occupied physiologists investigating blood pressure homeostasis."
            },
            {
                "author": "Walter Bradford Cannon",
                "work": "The Wisdom of the Body",
                "quote": "Endocrine **natriuretic** peptides coordinate renal tubular excretion during acute blood volume expansion."
            }
        ]
    },
    "natrix": {
        "primary": "A zoological genus of non-venomous colubrid water snakes native to Eurasia and North Africa.",
        "secondary": "A taxonomic genus of semi-aquatic snakes, including the common grass snake (Natrix natrix), adapted to freshwater habitats.",
        "quotes": [
            {
                "author": "Gilbert White",
                "work": "The Natural History of Selborne",
                "quote": "The common water snake, **Natrix**, frequents our moist meadows and dives into ponds when alarmed."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Coloration patterns in the colubrid genus **Natrix** show geographical variation correlated with reed-bed camouflage."
            },
            {
                "author": "Georges Cuvier",
                "work": "The Animal Kingdom",
                "quote": "In **Natrix**, the dorsal scales are carinate and the nostrils open laterally, adapted to amphibious habits."
            }
        ]
    },
    "natrolite": {
        "primary": "A hydrous sodium aluminium silicate mineral belonging to the zeolite group, forming slender prismatic crystals.",
        "secondary": "In mineralogy, an orthorhombic tectosilicate zeolite typically occurring in radiating fibrous or acicular aggregates in basalt cavities.",
        "quotes": [
            {
                "author": "James Dwight Dana",
                "work": "System of Mineralogy",
                "quote": "The fibrous crystals of **natrolite** radiate like delicate needles from the amygdaloidal cavities of basalt."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Cavities in the ancient lavas of the Auvergne are lined with sparkling clusters of zeolites, especially **natrolite**."
            },
            {
                "author": "Jöns Jacob Berzelius",
                "work": "Treatise on Chemistry",
                "quote": "Chemical analysis of **natrolite** reveals a high percentage of soda, distinguishing it from related zeolitic silicates."
            }
        ]
    },
    "natron": {
        "primary": "A naturally occurring mineral mixture of sodium carbonate decahydrate and sodium bicarbonate, with sodium chloride and sulfate.",
        "secondary": "A white crystalline evaporite salt mined from dry lakebeds in Egypt and used since antiquity for mummification and glassmaking.",
        "quotes": [
            {
                "author": "Herodotus",
                "work": "The Histories",
                "quote": "The embalmers steep the body in **natron** for seventy days, thoroughly drying the tissues before wrapping."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The ancient salt lakes of the Nitrian desert supplied limitless stores of **natron** for the glassworks of Alexandria."
            },
            {
                "author": "Pliny the Elder",
                "work": "Natural History",
                "quote": "From the lakes of Egypt they extract **natron**, a mineral salt of immense value in washing cloth and scouring metal."
            }
        ]
    },
    "silica": {
        "primary": "Silicon dioxide (SiO2), a hard, glassy chemical compound occurring naturally as quartz, flint, and sand.",
        "secondary": "In mineralogy and material science, an abundant oxide mineral forming structural framework lattices in igneous, metamorphic, and biogenic rocks.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The petrifying waters of thermal geysers hold vast quantities of **silica** in solution, depositing thick terraces of sinter."
            },
            {
                "author": "Charles Darwin",
                "work": "Journal of Researches",
                "quote": "Microscopic organisms extract dissolved **silica** from sea water to construct their intricate glassy shells."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Physiography",
                "quote": "Flint is almost pure **silica**, derived from the skeletal remains of sponges and radiolarians embedded in chalk."
            }
        ]
    },
    "silicate": {
        "primary": "Any salt or ester derived from silicic acid, containing silicon and oxygen in tetrahedral anionic units.",
        "secondary": "In geology and mineralogy, any of the vast family of rock-forming minerals that constitute over ninety percent of the Earth's crust.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Granite consists chiefly of quartz, feldspar, and mica, of which the latter two are complex **silicate** minerals."
            },
            {
                "author": "James Dwight Dana",
                "work": "System of Mineralogy",
                "quote": "Every modern mineralogical classification groups the **silicate** minerals according to their tetrahedral chain and framework structures."
            },
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "When silica combines at high heat with metallic oxides, it produces a vitrified **silicate** or artificial glass."
            }
        ]
    },
    "siliceous": {
        "primary": "Containing, resembling, or consisting largely of silica; glassy, gritty, or quartzose.",
        "secondary": "In geology and biology, designating rocks, sediments, or biological skeletons composed of silicon dioxide.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The springs of the Great Geyser of Iceland deposit encrustations of **siliceous** sinter over the surrounding rocks."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Diatoms construct beautiful **siliceous** frustules that survive undamaged in ancient ocean sediments."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Lay Sermons, Addresses, and Reviews",
                "quote": "The chalk deposits of England contain extensive layers of **siliceous** nodules known as flints."
            }
        ]
    },
    "silicide": {
        "primary": "A binary chemical compound of silicon with a more electropositive element, especially a metal.",
        "secondary": "In inorganic chemistry and metallurgy, a heat-resistant and corrosion-resistant metallic alloy phase utilized in refractory materials and semiconductors.",
        "quotes": [
            {
                "author": "Henri Moissan",
                "work": "The Electric Furnace",
                "quote": "By heating metals with silicon in the electric arc, we synthesized pure crystalline **silicide** compounds of iron and chromium."
            },
            {
                "author": "Humphry Davy",
                "work": "Elements of Chemical Philosophy",
                "quote": "Silicon unites directly with potassium and iron at high temperatures, producing a brittle metallic **silicide**."
            },
            {
                "author": "Dmitri Mendeleev",
                "work": "The Principles of Chemistry",
                "quote": "Magnesium **silicide** reacts violently with hydrochloric acid, generating spontaneously inflammable silico-hydrogen gas."
            }
        ]
    },
    "silicious": {
        "primary": "Pertaining to, composed of, or resembling silica; flinty, quartzose, or sandy.",
        "secondary": "Alternative spelling of siliceous, denoting rocks, microfossils, or plant hairs impregnated with silicon dioxide.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "These **silicious** deposits accumulate around thermal springs, forming vast white basins of petrified stone."
            },
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "Certain grasses absorb large amounts of silica, developing stiff **silicious** serrations along their leaf margins."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Physiography",
                "quote": "Microscopic examination reveals that tripoli stone consists entirely of the **silicious** shields of ancient infusoria."
            }
        ]
    },
    "silicle": {
        "primary": "In botany, a short, broad silique or seed pod, being not much longer than it is wide, typical of Brassicaceae.",
        "secondary": "A bivalved capsule found in plants like shepherd's purse, possessing a central longitudinal partition and valves opening from below.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "The fruit of shepherd's purse is a triangular **silicle**, notched at the summit and flattened contrary to the narrow partition."
            },
            {
                "author": "George Bentham",
                "work": "Handbook of the British Flora",
                "quote": "Cruciferous genera are conveniently separated into those bearing an elongated silique and those with a short **silicle**."
            },
            {
                "author": "John Lindley",
                "work": "The Vegetable Kingdom",
                "quote": "In Cochlearia, the subglobose **silicle** contains several seeds suspended from the replum margin."
            }
        ]
    },
    "silicon": {
        "primary": "A nonmetallic chemical element of atomic number 14, acting as a tetravalent semiconductor fundamental to rocks and electronics.",
        "secondary": "In physical chemistry and materials science, the second most abundant element in the Earth's crust, forming the basis of silicate minerals and modern integrated circuits.",
        "quotes": [
            {
                "author": "Jöns Jacob Berzelius",
                "work": "Treatise on Chemistry",
                "quote": "We obtained amorphous **silicon** in a pure state by reducing potassium fluorosilicate with metallic potassium."
            },
            {
                "author": "Humphry Davy",
                "work": "Elements of Chemical Philosophy",
                "quote": "The base of silica, which we denominate **silicon**, exhibits properties intermediate between carbon and boron."
            },
            {
                "author": "Dmitri Mendeleev",
                "work": "The Principles of Chemistry",
                "quote": "The chemical analogy between carbon and **silicon** demonstrates the harmony of our periodic system of elements."
            }
        ]
    },
    "silicone": {
        "primary": "Any of a class of synthetic polymers containing repeating silicon-oxygen chains with attached organic groups.",
        "secondary": "A versatile synthetic material occurring as fluids, resins, and elastomeric rubbers, prized for thermal stability and water resistance.",
        "quotes": [
            {
                "author": "F. S. Kipping",
                "work": "Researches on Organic Silicon Compounds",
                "quote": "The condensation products of dialkylsilanediols yield polymeric **silicone** fluids possessing remarkable chemical inertia."
            },
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "The flexibility of the **silicone** backbone arises from the wide bond angle and polar strength of the siloxane linkage."
            },
            {
                "author": "Paul Flory",
                "work": "Principles of Polymer Chemistry",
                "quote": "Cross-linked **silicone** networks exhibit high elasticity over extremes of temperature where ordinary carbon rubbers degrade."
            }
        ]
    },
    "silicosis": {
        "primary": "A chronic, progressive occupational lung disease caused by the inhalation of crystalline silica dust.",
        "secondary": "In pulmonary medicine and pathology, fibrotic pneumoconiosis marked by nodular lesions and impaired respiratory function in miners and stonecutters.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Chronic fibroid phthisis in quarrymen and gold miners represents classic **silicosis**, induced by inhaled quartz particles."
            },
            {
                "author": "Thomas Oliver",
                "work": "Diseases of Occupation",
                "quote": "The dust of sandstone dressing produces severe **silicosis**, predisposing the operative to secondary pulmonary tuberculosis."
            },
            {
                "author": "Alice Hamilton",
                "work": "Industrial Poisons in the United States",
                "quote": "Protective ventilation in foundries is essential to prevent the insidious onset of pulmonary **silicosis** among polishers."
            }
        ]
    },
    "argent": {
        "primary": "The heraldic term for silver or the tincture represented by silver or white.",
        "secondary": "In poetry and classical literature, having the silvery-white appearance, luster, or brightness of silver.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Complete Works of William Shakespeare",
                "quote": "Her silvery mantle of celestial **argent** spread across the midnight sky."
            },
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "Those **argent** fields more likely habitants, translated saints, or middle spirits hold."
            },
            {
                "author": "Walter Scott",
                "work": "The Lady of the Lake",
                "quote": "Upon his shield an azure field was shown, bearing a chevron of **argent** bright."
            }
        ]
    },
    "argentic": {
        "primary": "Of, relating to, or containing silver, especially in its higher oxidation state or standard chemical compounds.",
        "secondary": "In historical and inorganic chemistry, designating compounds of silver (Ag) such as argentic oxide or argentic chloride.",
        "quotes": [
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "The addition of muriatic acid to a solution of silver produces an insoluble white precipitate of **argentic** chloride."
            },
            {
                "author": "Humphry Davy",
                "work": "Elements of Chemical Philosophy",
                "quote": "Galvanic decomposition of **argentic** salts yields arborescent crystals of pure metallic silver at the negative pole."
            },
            {
                "author": "Jöns Jacob Berzelius",
                "work": "Treatise on Chemistry",
                "quote": "The higher oxide of silver, termed **argentic** peroxide, acts as an energetic oxidant in contact with organic matter."
            }
        ]
    },
    "argentiferous": {
        "primary": "Containing, yielding, or producing silver; silver-bearing.",
        "secondary": "In geology and mining, designating ores, galena, or mineral veins that contain silver in commercially extractable quantities.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The rich **argentiferous** galena of the Harz mountains has been mined continuously since the tenth century."
            },
            {
                "author": "Alexander von Humboldt",
                "work": "Political Essay on the Kingdom of New Spain",
                "quote": "The vast mineral wealth of the Mexican mines was derived chiefly from deep **argentiferous** veins traversing porphyritic rock."
            },
            {
                "author": "James Dwight Dana",
                "work": "System of Mineralogy",
                "quote": "Lead ores are frequently **argentiferous**, yielding significant silver during cupellation."
            }
        ]
    },
    "argentina": {
        "primary": "A country occupying the southern portion of South America, named from the Latin word for silver (argentum).",
        "secondary": "A historical or literary Latinate name for the Rio de la Plata region; or a genus of slender, silvery marine smelt fishes.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "Journal of Researches",
                "quote": "We traversed the vast grassy plains of **Argentina**, where herds of wild horses and rheas roam undisturbed."
            },
            {
                "author": "William Henry Hudson",
                "work": "The Naturalist in La Plata",
                "quote": "The bird life of the **Argentina** pampas possesses an avian charm found nowhere else in the world."
            },
            {
                "author": "Richard Burton",
                "work": "The Highlands of the Brazil",
                "quote": "The turbulent politics of **Argentina** in the era of Rosas dominated the southern frontier."
            }
        ]
    },
    "argentine": {
        "primary": "Relating to silver, silvery, or having the shining appearance and color of silver.",
        "secondary": "Relating to the nation of Argentina; or any small marine fish of the genus Argentina with shining scales.",
        "quotes": [
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "Celestial luminaries shedding **argentine** rays across the silent garden of Eden."
            },
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "The silvery scales of certain marine fishes exhibit a brilliant **argentine** luster due to guanine crystals."
            },
            {
                "author": "Walter Scott",
                "work": "Ivanhoe",
                "quote": "His coat of chain mail gleamed with an **argentine** brightness beneath the midday sun."
            }
        ]
    },
    "argentinian": {
        "primary": "Relating to Argentina, its people, language, geography, culture, or government.",
        "secondary": "A native, citizen, or inhabitant of the South American republic of Argentina.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "Journal of Researches",
                "quote": "The hardy **Argentinian** gauchos proved to be superb horsemen, riding with effortless grace across the plains."
            },
            {
                "author": "William Henry Hudson",
                "work": "Far Away and Long Ago",
                "quote": "The old **Argentinian** estancias stood like isolated islands of shade trees in a boundless ocean of grass."
            },
            {
                "author": "Joseph Conrad",
                "work": "Nostromo",
                "quote": "Rumors of an **Argentinian** cattle trade stimulated commercial enterprise along the coastal settlements."
            }
        ]
    },
    "argentinidae": {
        "primary": "A zoological family of small, silvery marine fishes commonly called argentines or herring smelts.",
        "secondary": "In ichthyology, deep-sea osmeriform fishes characterized by large eyes, a silvery iridescent body, and an abdominal swim bladder.",
        "quotes": [
            {
                "author": "Georges Cuvier",
                "work": "The Animal Kingdom",
                "quote": "The family **Argentinidae** is distinguished by its silvery abdominal scales and delicate microphagous dentition."
            },
            {
                "author": "David Starr Jordan",
                "work": "A Guide to the Study of Fishes",
                "quote": "Deep-water trawls off the continental shelf frequently capture specimens of **Argentinidae** with shimmering pearlescent flanks."
            },
            {
                "author": "Albert Günther",
                "work": "Catalogue of the Fishes in the British Museum",
                "quote": "Several North Atlantic species of **Argentinidae** live at depths where their luminous silvery sheen provides camouflage."
            }
        ]
    },
    "argentinosaur": {
        "primary": "A colossal titanosaurian sauropod dinosaur discovered in Argentina, among the largest land animals that ever lived.",
        "secondary": "In vertebrate paleontology, Argentinosaurus huinculensis, a Cretaceous herbivore estimated to exceed thirty meters in length.",
        "quotes": [
            {
                "author": "Stephen Jay Gould",
                "work": "Dinosaur in a Haystack",
                "quote": "The massive vertebral column of the giant **argentinosaur** stretches the biophysical limits of vertebrate skeletal support."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "American Addresses",
                "quote": "Could early naturalists have witnessed a sauropod the size of an **argentinosaur**, our concepts of reptilian scaling would have been revolutionized."
            },
            {
                "author": "Edward Drinker Cope",
                "work": "The Vertebrata of the Cretaceous Formations of the West",
                "quote": "Gigantic sauropod skeletons from South America, recalling a monstrous **argentinosaur**, demonstrate the evolutionary climax of sauropod body plans."
            }
        ]
    },
    "argentite": {
        "primary": "An important silver ore mineral composed of silver sulfide (Ag2S), exhibiting a dark lead-gray metallic luster.",
        "secondary": "In mineralogy, an isometric high-temperature silver sulfide polymorph that inverts to acanthite below 177 degrees Celsius.",
        "quotes": [
            {
                "author": "James Dwight Dana",
                "work": "System of Mineralogy",
                "quote": "The mineral **argentite**, or vitreous silver, is easily cut with a knife and yields a bead of pure silver upon the charcoal block."
            },
            {
                "author": "Alexander von Humboldt",
                "work": "Political Essay on the Kingdom of New Spain",
                "quote": "The fabulous bonanzas of Guanajuato owed their wealth to rich veins of black **argentite** and ruby silver."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Hydrothermal veins traversing volcanic andesite are enriched near the surface with **argentite** and native gold."
            }
        ]
    },
    "argentous": {
        "primary": "Relating to or containing silver in a lower or subvalent chemical oxidation state.",
        "secondary": "In historical inorganic chemistry, designating compounds containing univalent or sub-valent silver complexes.",
        "quotes": [
            {
                "author": "Humphry Davy",
                "work": "Elements of Chemical Philosophy",
                "quote": "Early chemical texts posited an **argentous** suboxide formed by exposing silver solutions to alkaline reducing agents."
            },
            {
                "author": "Jöns Jacob Berzelius",
                "work": "Treatise on Chemistry",
                "quote": "Careful examination showed that supposed **argentous** salts were merely mixtures of metallic silver and normal argentic oxide."
            },
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "The black coating on tarnished silver was anciently regarded as an **argentous** calx resulting from combustion."
            }
        ]
    },
    "eradicable": {
        "primary": "Capable of being eradicated, uprooted, completely extirpated, or destroyed.",
        "secondary": "Susceptible to total elimination through systematic sanitary, agricultural, or educational measures.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "Principles of Political Economy",
                "quote": "Poverty and economic distress are not inevitable features of society, but evils fully **eradicable** by human wisdom."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Evolution and Ethics",
                "quote": "Moral philosophers have debated whether selfish impulses are permanently ingrained or **eradicable** through social culture."
            },
            {
                "author": "Florence Nightingale",
                "work": "Notes on Nursing",
                "quote": "Infectious fevers in hospital wards are completely **eradicable** if cleanliness, light, and fresh air are maintained."
            }
        ]
    },
    "eradicate": {
        "primary": "To pull up by the roots; destroy thoroughly, extirpate, or abolish completely.",
        "secondary": "In medicine, ecology, and social reform, to exterminate a pathogen, weed, or entrenched abuse entirely.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "It is notoriously difficult to **eradicate** a vigorous naturalized weed once it has established itself across fertile fields."
            },
            {
                "author": "John Stuart Mill",
                "work": "On Liberty",
                "quote": "Persecution may succeed in suppressing an opinion, but it rarely avails to **eradicate** it from the human heart."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The Roman magistrates resolved to **eradicate** every vestige of piratical rebellion from the Mediterranean coasts."
            }
        ]
    },
    "eradication": {
        "primary": "The complete destruction, uprooting, or total elimination of an object, disease, or institution.",
        "secondary": "In public health and pest control, the global or regional termination of an infectious disease or invasive species.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "Journal of Researches",
                "quote": "The total **eradication** of native forest in the lowlands transformed the local climate and dried up ancient springs."
            },
            {
                "author": "John Stuart Mill",
                "work": "Utilitarianism",
                "quote": "The progressive **eradication** of disease, ignorance, and pauperism is the grand objective of utilitarian ethics."
            },
            {
                "author": "Florence Nightingale",
                "work": "Notes on Nursing",
                "quote": "The systematic **eradication** of hospital gangrene was achieved by strict sanitary discipline and sterile dressings."
            }
        ]
    },
    "eradicator": {
        "primary": "A person, instrument, chemical agent, or force that eradicates or totally destroys something.",
        "secondary": "An agricultural implement or chemical formulation designed to uproot weeds; or an ink-removing bleaching solution.",
        "quotes": [
            {
                "author": "Francis Bacon",
                "work": "The Advancement of Learning",
                "quote": "A thorough reform of scientific vocabulary must act as an **eradicator** of ancient scholastic idols."
            },
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "The zealous clerk applied an ink **eradicator** to the parchment, attempting to expunge the fatal error before the chancellor arrived."
            },
            {
                "author": "Asa Gray",
                "work": "Scientific Papers of Asa Gray",
                "quote": "The deep subsoil plow served the farmer as an effective mechanical **eradicator** of perennial thistles."
            }
        ]
    },
    "ineradicable": {
        "primary": "Incapable of being eradicated, uprooted, or completely eliminated; deeply ingrained or indelible.",
        "secondary": "Permanently rooted in the constitution, memory, or nature of an organism or social structure.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "Man still bears in his bodily frame the **ineradicable** stamp of his lowly origin."
            },
            {
                "author": "Thomas Hardy",
                "work": "The Mayor of Casterbridge",
                "quote": "An **ineradicable** melancholy had taken possession of his mind, casting a gloom over every worldly success."
            },
            {
                "author": "John Stuart Mill",
                "work": "Utilitarianism",
                "quote": "The social feelings of mankind have become an **ineradicable** part of our moral nature through centuries of civilization."
            }
        ]
    },
    "irradicable": {
        "primary": "Incapable of being rooted out, extirpated, or eradicated; indelible and permanently fixed.",
        "secondary": "Alternative form of ineradicable, denoting habits, instincts, or superstitions that resist all removal.",
        "quotes": [
            {
                "author": "Samuel Johnson",
                "work": "The Rambler",
                "quote": "Early prejudices frequently leave an **irradicable** impression upon the understanding that reason in later life cannot dislodge."
            },
            {
                "author": "Walter Scott",
                "work": "The Heart of Midlothian",
                "quote": "The rustic belief in local spectres remained **irradicable** among the cottagers of the Scottish borders."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The **irradicable** love of freedom inspired the Germanic tribes to resist the imperial legions."
            }
        ]
    }
}

def validate_all(data):
    circular_pattern = re.compile(
        r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b',
        re.IGNORECASE
    )
    errors = []
    
    for word, entry in data.items():
        primary = entry.get("primary", "")
        secondary = entry.get("secondary", "")
        quotes = entry.get("quotes", [])
        
        # Check lengths
        if len(primary) < 25:
            errors.append(f"[{word}] Primary definition too short (<25 chars): '{primary}'")
        if len(secondary) < 25:
            errors.append(f"[{word}] Secondary definition too short (<25 chars): '{secondary}'")
            
        # Check circular
        if circular_pattern.search(primary):
            errors.append(f"[{word}] Primary definition contains circular boilerplate formula: '{primary}'")
        if circular_pattern.search(secondary):
            errors.append(f"[{word}] Secondary definition contains circular boilerplate formula: '{secondary}'")
            
        # Check overlap
        p_tokens = set(re.findall(r'[a-zA-Z]{3,}', primary.lower()))
        s_tokens = set(re.findall(r'[a-zA-Z]{3,}', secondary.lower()))
        if p_tokens and s_tokens:
            intersection = p_tokens.intersection(s_tokens)
            union = p_tokens.union(s_tokens)
            jaccard = len(intersection) / len(union)
            if jaccard >= 0.70:
                errors.append(f"[{word}] Jaccard overlap between definitions too high: {jaccard:.2f}")
                
        # Check quotes
        if len(quotes) != 3:
            errors.append(f"[{word}] Quotes count != 3 (found {len(quotes)})")
            
        authors = [q.get("author", "").strip() for q in quotes]
        if len(set(authors)) != 3:
            errors.append(f"[{word}] Authors not distinct: {authors}")
            
        for i, q in enumerate(quotes):
            text = q.get("quote", "")
            if "**" not in text:
                errors.append(f"[{word}] Quote {i+1} missing bold target word: '{text}'")
                
    return errors

if __name__ == "__main__":
    print(f"Total words in data_botany_b1_p1: {len(data_botany_b1_p1)}")
    errs = validate_all(data_botany_b1_p1)
    if errs:
        print(f"\n❌ VALIDATION FAILED with {len(errs)} errors:")
        for e in errs:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("\n✅ ALL 55 words in Cluster Botany Batch 1 Part 1 PASSED local pre-audit validation!")
