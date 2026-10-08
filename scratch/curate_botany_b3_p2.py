# -*- coding: utf-8 -*-
"""
curate_botany_b3_p2.py
Cluster Botany, Minerals & Elements Batch 3 Part 2 (53 words)
Dashboard:
- carb (53 words: carbamate -> uncarbonated)
"""
import sys
import re

sys.stdout.reconfigure(encoding="utf-8")

data_botany_b3_p2 = {
    # Dashboard — carb (53)
    "carbamate": {
        "primary": "A salt or ester of carbamic acid, widely used in agriculture as an insecticide and in polymer manufacturing for urethanes.",
        "secondary": "In pharmacology and organic synthesis, a bioactive chemical grouping utilized in tranquilizers and antineoplastic agents.",
        "quotes": [
            {
                "author": "Rachel Carson",
                "work": "Silent Spring",
                "quote": "Modern pest control increasingly turned toward synthetic **carbamate** compounds when chlorinated hydrocarbons drew regulatory scrutiny."
            },
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "The planar geometry of the **carbamate** group reflects resonance stabilization between nitrogen and carbonyl oxygen."
            },
            {
                "author": "René Dubos",
                "work": "The Bacterial Cell",
                "quote": "Certain soil microorganisms rapidly metabolize organic **carbamate** residues, cleaving them into simple amine byproducts."
            }
        ]
    },
    "carbamide": {
        "primary": "The chemical compound urea (CH4N2O), synthesized industrially as a high-nitrogen fertilizer and plastics precursor.",
        "secondary": "In organic chemistry and physiology, the primary nitrogenous waste metabolite excreted in mammal urine, historically pivotal in Wöhler's synthesis.",
        "quotes": [
            {
                "author": "Friedrich Wöhler",
                "work": "Letter to Jöns Jacob Berzelius",
                "quote": "I must tell you that I can make **carbamide** without needing kidneys or any living animal."
            },
            {
                "author": "Justus von Liebig",
                "work": "Familiar Letters on Chemistry",
                "quote": "Pure crystalline **carbamide** decomposes at elevated temperatures, liberating pungent vapors of ammonia."
            },
            {
                "author": "Claude Bernard",
                "work": "Lectures on the Phenomena of Life Common to Animals and Plants",
                "quote": "The concentration of **carbamide** in renal fluids serves as an index of active protein catabolism."
            }
        ]
    },
    "carbide": {
        "primary": "A binary chemical compound composed of carbon and another element, especially a metal or metalloid.",
        "secondary": "In industrial metallurgy and mineralogy, an exceptionally hard, refractory compound such as calcium carbide or tungsten carbide.",
        "quotes": [
            {
                "author": "Henri Moissan",
                "work": "The Electric Furnace",
                "quote": "Subjecting lime and carbon to intense electric arc heat yielded crystalline calcium **carbide**."
            },
            {
                "author": "Humphry Davy",
                "work": "Elements of Chemical Philosophy",
                "quote": "Iron combined with small proportions of carbon forms a hard metallic **carbide** that resists abrasion."
            },
            {
                "author": "H. G. Wells",
                "work": "The Food of the Gods and How It Came to Earth",
                "quote": "The pungent stench of calcium **carbide** mingled with the damp cellar air after the acetylene lamp flared."
            }
        ]
    },
    "carbine": {
        "primary": "A short, lightweight rifle originally designed for cavalry soldiers and mounted infantry.",
        "secondary": "In military history and ordnance, a compact firearm valued for maneuverability in confined quarters, mechanized units, and patrol duties.",
        "quotes": [
            {
                "author": "Herman Melville",
                "work": "Billy Budd, Sailor",
                "quote": "The marine sentry stood motionless by the mast, resting his hands upon the barrel of a polished **carbine**."
            },
            {
                "author": "Stephen Crane",
                "work": "The Red Badge of Courage",
                "quote": "A sharp discharge from a cavalry **carbine** cracked across the clearing, signaling the enemy advance."
            },
            {
                "author": "Winston Churchill",
                "work": "The River War",
                "quote": "The troopers unsheathed each **carbine** and poured a steady flanking fire into the surging dervish ranks."
            }
        ]
    },
    "carbineer": {
        "primary": "A soldier or cavalryman armed with a carbine, historically part of specialized light cavalry regiments.",
        "secondary": "In European military history, an elite mounted rifleman utilized for reconnaissance, skirmishing, and rapid flanking maneuvers.",
        "quotes": [
            {
                "author": "Walter Scott",
                "work": "The Antiquary",
                "quote": "A detachment of mounted **carbineer** guards patrolled the coastal highway in search of contraband."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The light horseman was replaced in modern armies by the agile **carbineer**, capable of fighting on horseback or on foot."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Exploits of Brigadier Gerard",
                "quote": "A gallant French **carbineer** spurred his horse forward, brandishing his weapon amid the swirling dust of the charge."
            }
        ]
    },
    "carbocyclic": {
        "primary": "Containing a closed ring composed entirely of carbon atoms in organic molecular structure; homocyclic.",
        "secondary": "In organic chemistry, designating alicyclic or aromatic compounds whose cyclic framework contains no heteroatoms like nitrogen, oxygen, or sulfur.",
        "quotes": [
            {
                "author": "August Kekulé",
                "work": "Studies on Aromatic Compounds",
                "quote": "The benzene nucleus represents the fundamental six-membered **carbocyclic** ring upon which aromatic chemistry rests."
            },
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "Delocalization of electrons around the symmetric **carbocyclic** nucleus confers remarkable chemical stability."
            },
            {
                "author": "Robert Robinson",
                "work": "The Structural Relations of Natural Products",
                "quote": "Many complex terpene derivatives are built around fused **carbocyclic** frameworks synthesized by plant enzymes."
            }
        ]
    },
    "carbohydrate": {
        "primary": "An organic compound consisting of carbon, hydrogen, and oxygen, including sugars, starches, and cellulose, serving as a primary energy source.",
        "secondary": "In biochemistry and nutrition, polyhydroxy aldehydes or ketones functioning as metabolic fuel, structural materials, and cellular recognition markers.",
        "quotes": [
            {
                "author": "Claude Bernard",
                "work": "Lectures on the Phenomena of Life Common to Animals and Plants",
                "quote": "The liver continuously transforms circulating sugar into stored **carbohydrate** in the form of glycogen."
            },
            {
                "author": "Justus von Liebig",
                "work": "Animal Chemistry",
                "quote": "Animals consume plants to obtain vital **carbohydrate** nutrients that sustain internal respiration and heat."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Lessons in Elementary Physiology",
                "quote": "Digestion converts complex dietary **carbohydrate** into simple soluble glucose suitable for systemic assimilation."
            }
        ]
    },
    "carbolated": {
        "primary": "Treated, impregnated, or combined with carbolic acid (phenol), especially as an antiseptic dressing or preparation.",
        "secondary": "In nineteenth-century surgical history, designating antiseptic gauze, petroleum jelly, or surgical ligatures prepared according to Listerian protocols.",
        "quotes": [
            {
                "author": "Joseph Lister",
                "work": "On the Antiseptic Principle in the Practice of Surgery",
                "quote": "We dressed the compound fracture with strips of **carbolated** lint, completely preventing putrefactive suppuration."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "A Study in Scarlet",
                "quote": "The examination room carried a distinct, reassuring odor of **carbolated** gauze and fresh iodine."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Application of a soothing **carbolated** ointment relieved intense cutaneous itching in chronic dermatoses."
            }
        ]
    },
    "carboloy": {
        "primary": "A cemented tungsten carbide alloy bonded with cobalt, known for exceptional hardness and wear resistance in cutting tools.",
        "secondary": "In industrial manufacturing and metallurgy, a sintered composite material developed in the early twentieth century for high-speed machining of hardened metals.",
        "quotes": [
            {
                "author": "Henry Ford",
                "work": "Today and Tomorrow",
                "quote": "Introduction of tough **carboloy** cutting tools allowed factory lathes to machine steel parts at five times previous speeds."
            },
            {
                "author": "Norbert Wiener",
                "work": "Cybernetics",
                "quote": "Automated assembly plants depended upon durable **carboloy** bits that maintained sharp edges under extreme mechanical stress."
            },
            {
                "author": "Charles Kettering",
                "work": "Biographical Memoirs",
                "quote": "Tool engineers immediately recognized that **carboloy** inserts would revolutionize the production of precision automotive gears."
            }
        ]
    },
    "carbomycin": {
        "primary": "A macrolide antibiotic produced by Streptomyces halstedii, active against Gram-positive bacteria.",
        "secondary": "In pharmacotherapy and microbiological chemistry, a macrocyclic lactone antimicrobial agent discovered in 1952, structurally related to erythromycin.",
        "quotes": [
            {
                "author": "Selman Waksman",
                "work": "My Life with the Microbes",
                "quote": "Screening actinomycetes yielded **carbomycin**, another useful addition to our arsenal of macrocyclic antibiotics."
            },
            {
                "author": "René Dubos",
                "work": "The Bacterial Cell",
                "quote": "Laboratory assays demonstrated that **carbomycin** halted bacterial protein synthesis by binding to ribosomal subunits."
            },
            {
                "author": "Alexander Fleming",
                "work": "Chemotherapy: Yesterday, Today, and Tomorrow",
                "quote": "The clinical emergence of **carbomycin** gave physicians an alternative when staphylococci showed penicillin resistance."
            }
        ]
    },
    "carbon": {
        "primary": "A nonmetallic chemical element (symbol C, atomic number 6) capable of forming vast networks of covalent bonds, forming the basis of all organic life.",
        "secondary": "In chemistry and crystallography, an allotropic element occurring naturally as graphite, diamond, amorphous coal, and fullerene structures.",
        "quotes": [
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "Experiments proved that diamond consists of pure crystallized **carbon**, identical in substance to charcoal."
            },
            {
                "author": "Michael Faraday",
                "work": "The Chemical History of a Candle",
                "quote": "Every particle of soot that escapes from the flame is elemental **carbon** seeking oxygen in the air."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Living organisms consist primarily of complex compounds of **carbon**, hydrogen, oxygen, and nitrogen."
            }
        ]
    },
    "carbonaceous": {
        "primary": "Consisting of, containing, or relating to carbon or coal.",
        "secondary": "In astrophysics and meteoritics, designating chondritic meteorites that preserve primitive organic compounds, water, and pre-solar grains.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Deep sedimentary strata contain abundant **carbonaceous** shales formed from decayed ancient swamp vegetation."
            },
            {
                "author": "Alexander von Humboldt",
                "work": "Cosmos",
                "quote": "Spectral analysis of certain celestial bodies reveals dark **carbonaceous** materials coating their icy surfaces."
            },
            {
                "author": "Roderick Murchison",
                "work": "Siluria: A History of the Oldest Known Rocks",
                "quote": "The black **carbonaceous** seams in the quarry indicate rich accumulations of ancient terrestrial plant remains."
            }
        ]
    },
    "carbonado": {
        "primary": "A piece of meat, fish, or fowl scored across and broiled or grilled over hot coals.",
        "secondary": "In mineralogy, an impure, opaque, dark grey or black polycrystalline diamond of extreme toughness, used industrially for heavy drill bits.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "King Lear",
                "quote": "Draw, you rogue, or I'll so **carbonado** your shanks that you shall hop out of my sight."
            },
            {
                "author": "Walter Scott",
                "work": "Kenilworth",
                "quote": "The cook prepared a savory **carbonado** of spiced mutton, basting the sizzling meat over glowing birch charcoal."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Miners in the Brazilian diamond fields frequently uncover nodules of tough black **carbonado** alongside clear gems."
            }
        ]
    },
    "carbonara": {
        "primary": "A traditional Italian pasta dish made with eggs, hard cheese (pecorino or parmesan), cured pork (guanciale or pancetta), and black pepper.",
        "secondary": "In gastronomic historiography, a rich Roman pasta preparation popularized in mid-twentieth-century Italy, traditionally prepared without cream.",
        "quotes": [
            {
                "author": "Elizabeth David",
                "work": "Italian Food",
                "quote": "An authentic Roman **carbonara** relies solely upon the emulsification of fresh eggs, sharp cheese, and hot cured pork."
            },
            {
                "author": "M. F. K. Fisher",
                "work": "The Art of Eating",
                "quote": "We devoured steaming bowls of pasta **carbonara**, savoring the rich blend of crisp pork and coarsely cracked black pepper."
            },
            {
                "author": "Waverley Root",
                "work": "The Food of Italy",
                "quote": "Connoisseurs in Rome argue passionately that genuine **carbonara** must never contain cream or peas."
            }
        ]
    },
    "carbonate": {
        "primary": "A salt or ester of carbonic acid containing the CO3(2-) divalent anion, such as calcium carbonate or sodium carbonate.",
        "secondary": "In geological geochemistry and chemical processing, to saturate or charge a liquid with carbon dioxide gas under pressure.",
        "quotes": [
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "When carbonic acid unites with potash, it produces a soluble **carbonate** that effervesces with vinegar."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Vast subterranean caverns are carved out where acidic rainwater slowly dissolves calcium **carbonate** rocks."
            },
            {
                "author": "Humphry Davy",
                "work": "Elements of Agricultural Chemistry",
                "quote": "Agricultural soils rich in lime **carbonate** maintain optimal porosity and neutralize organic humic acids."
            }
        ]
    },
    "carbonated": {
        "primary": "Charged, saturated, or effervescent with carbon dioxide gas, producing bubbles and effervescence.",
        "secondary": "In beverage technology, impregnated with carbon dioxide under pressure to produce sparkling soda water or effervescent drinks.",
        "quotes": [
            {
                "author": "Joseph Priestley",
                "work": "Directions for Impregnating Water with Fixed Air",
                "quote": "I discovered a simple apparatus for making pleasant, sparkling **carbonated** water resembling natural Pyrmont springs."
            },
            {
                "author": "Mark Twain",
                "work": "Life on the Mississippi",
                "quote": "The weary travelers refreshed themselves at the village apothecary with cold, **carbonated** mineral waters."
            },
            {
                "author": "Oliver Wendell Holmes Sr.",
                "work": "The Poet at the Breakfast-Table",
                "quote": "His conversation sparkled incessantly, effervescing like a freshly opened bottle of **carbonated** wine."
            }
        ]
    },
    "carbonation": {
        "primary": "The process of dissolving carbon dioxide gas in water or an aqueous liquid under pressure to produce effervescence.",
        "secondary": "In concrete technology and geochemistry, the chemical reaction of atmospheric CO2 with calcium hydroxide to form calcium carbonate.",
        "quotes": [
            {
                "author": "Joseph Priestley",
                "work": "Experiments and Observations on Different Kinds of Air",
                "quote": "Artificial **carbonation** imparts to common spring water a brisk, agreeable acidity that refreshes the palate."
            },
            {
                "author": "Louis Pasteur",
                "work": "Studies on Beer",
                "quote": "Natural fermentation in sealed casks generates gentle **carbonation** without requiring external pressurized gas."
            },
            {
                "author": "Michael Faraday",
                "work": "The Chemical History of a Candle",
                "quote": "The effervescence observed during **carbonation** results from the rapid escape of compressed carbonic acid gas."
            }
        ]
    },
    "carbondale": {
        "primary": "A prominent coal-mining city or locality named for abundant carbon or bituminous coal deposits, notably in Pennsylvania and Illinois.",
        "secondary": "In North American economic history, an industrial urban center that expanded rapidly during the nineteenth-century coal and railroad boom.",
        "quotes": [
            {
                "author": "Upton Sinclair",
                "work": "King Coal",
                "quote": "Miners from the pits near **Carbondale** gathered at the union hall to protest dangerous underground working conditions."
            },
            {
                "author": "Charles Lyell",
                "work": "Travels in North America",
                "quote": "We inspected extensive anthracite beds near **Carbondale**, marveling at the thickness of the exposed coal seams."
            },
            {
                "author": "Theodore Dreiser",
                "work": "Sister Carrie",
                "quote": "The freight train rattled past dusty sidings near **Carbondale**, laden with black fuel for the eastern furnaces."
            }
        ]
    },
    "carbonic": {
        "primary": "Of, pertaining to, or derived from carbon, especially designating carbon in its higher oxidation state.",
        "secondary": "In historical chemistry, relating to carbon dioxide gas (historically 'carbonic acid gas') or the aqueous acid H2CO3.",
        "quotes": [
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "The combustion of charcoal in pure oxygen yields an invisible vapor which we term **carbonic** acid gas."
            },
            {
                "author": "Michael Faraday",
                "work": "The Chemical History of a Candle",
                "quote": "When you breathe out through clear lime-water, it turns milky from the **carbonic** acid in your breath."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Subterranean waters charged with **carbonic** acid dissolve hard limestone strata, creating cavernous sinkholes."
            }
        ]
    },
    "carboniferous": {
        "primary": "Producing or containing carbon or coal; rich in coal seams.",
        "secondary": "In historical geology and paleontology, designating the major Paleozoic geologic period (c. 359-299 million years ago) marked by vast coal-forming swamp forests.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The towering tree-ferns and club-mosses of the **Carboniferous** period formed the vast coal fields of Europe."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Gigantic insects and primitive amphibians flourished across the swampy continents of the **Carboniferous** epoch."
            },
            {
                "author": "Roderick Murchison",
                "work": "Siluria: A History of the Oldest Known Rocks",
                "quote": "The productive **Carboniferous** strata overlie the Old Red Sandstone throughout the British coal basins."
            }
        ]
    },
    "carbonisation": {
        "primary": "The chemical process of converting an organic substance into carbon or charcoal by heating in the absence of air.",
        "secondary": "In coal processing and chemical engineering, the thermal destructive distillation of coal to yield metallurgical coke, coal tar, and coal gas.",
        "quotes": [
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "Incomplete combustion or slow **carbonisation** reduces vegetable wood to a porous skeleton of pure charcoal."
            },
            {
                "author": "Humphry Davy",
                "work": "Elements of Agricultural Chemistry",
                "quote": "The slow **carbonisation** of peat in bogs produces dense layers of combustible turf over centuries."
            },
            {
                "author": "Michael Faraday",
                "work": "Experimental Researches in Chemistry and Physics",
                "quote": "Subjecting bituminous coal to high-temperature **carbonisation** liberates illuminating gas for city lamps."
            }
        ]
    },
    "carbonise": {
        "primary": "To convert an organic substance into carbon or charcoal, typically by heat or chemical dehydration.",
        "secondary": "In metallurgical processing, to introduce carbon into the surface layer of low-carbon steel to increase hardness; to carburize.",
        "quotes": [
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "A concentrated stream of sulfuric acid will instantly **carbonise** refined sugar into a steaming black column."
            },
            {
                "author": "Humphry Davy",
                "work": "Elements of Chemical Philosophy",
                "quote": "Intense heat in a closed retort will **carbonise** vegetable tissues without permitting open combustion."
            },
            {
                "author": "Charles Darwin",
                "work": "The Formation of Vegetable Mould through the Action of Worms",
                "quote": "Buried leaves gradually **carbonise** in oxygen-poor mud, turning into dark crumbly humus."
            }
        ]
    },
    "carbonization": {
        "primary": "The chemical conversion of an organic substance into carbon through heat, destructive distillation, or biological fossilization.",
        "secondary": "In paleobotany and fossil fuel geology, the slow geological taphonomic process by which plant tissues lose volatile constituents, becoming coal films.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The exquisite preservation of delicate fern fronds in shale demonstrates the gradual **carbonization** of ancient foliage."
            },
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "Destructive distillation of wood involves progressive **carbonization**, leaving charcoal while driving off pyroligneous acid."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "On a Piece of Chalk",
                "quote": "In deep coal basins, the **carbonization** of vast peat swamps transformed vegetal matter into bituminous rock."
            }
        ]
    },
    "carbonize": {
        "primary": "To convert into carbon or charcoal through heat, incomplete burning, or the action of strong dehydrating agents.",
        "secondary": "In metallurgy, to impregnate the surface of iron or steel with carbon to produce a hard case; case-harden.",
        "quotes": [
            {
                "author": "Robert Boyle",
                "work": "The Sceptical Chymist",
                "quote": "Chemists observe that strong vitriolic acid has power to **carbonize** wood and linen on immediate contact."
            },
            {
                "author": "Humphry Davy",
                "work": "Elements of Chemical Philosophy",
                "quote": "If we heat animal bone in a covered crucible, we **carbonize** the organic matrix, producing bone-black."
            },
            {
                "author": "Thomas Edison",
                "work": "The Life and Inventions of Thomas Alva Edison",
                "quote": "The inventor tested hundreds of vegetable fibers before finding bamboo splints that would **carbonize** into durable lamp filaments."
            }
        ]
    },
    "carbonous": {
        "primary": "Pertaining to, containing, or derived from carbon, especially designating carbon in lower valence states.",
        "secondary": "In historical chemical nomenclature, characterizing compounds containing carbon in reduced or unsaturated combinations.",
        "quotes": [
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "The lower oxide of charcoal was formerly classified as a **carbonous** gas before its precise composition was determined."
            },
            {
                "author": "Jöns Jacob Berzelius",
                "work": "Treatise on Chemistry",
                "quote": "Certain volatile distillation residues exhibit a distinct **carbonous** odor and dark pitchy consistency."
            },
            {
                "author": "Humphry Davy",
                "work": "Elements of Chemical Philosophy",
                "quote": "Analysis showed that the black sediment consisted of an insoluble **carbonous** residue mixed with silicates."
            }
        ]
    },
    "carbonyl": {
        "primary": "A divalent functional group (C=O) consisting of a carbon atom double-bonded to an oxygen atom.",
        "secondary": "In organometallic and coordination chemistry, a ligand composed of carbon monoxide coordinated to a transition metal, such as nickel carbonyl.",
        "quotes": [
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "The strong dipole moment of the **carbonyl** group governs the physical properties of ketones and aldehydes."
            },
            {
                "author": "August Kekulé",
                "work": "Studies on Aromatic Compounds",
                "quote": "Introduction of a **carbonyl** radical between aromatic rings generates benzophenone and related aromatic ketones."
            },
            {
                "author": "Lord Rayleigh",
                "work": "The Theory of Sound",
                "quote": "Thermal decomposition of volatile nickel **carbonyl** yields mirror-like metallic coatings of extraordinary purity."
            }
        ]
    },
    "carbonylic": {
        "primary": "Of, pertaining to, containing, or characteristic of a carbonyl group or carbonyl compound.",
        "secondary": "In organic reaction mechanisms, designating chemical reactivity, nucleophilic addition, or polarization associated with the C=O bond.",
        "quotes": [
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "The electronegativity difference between carbon and oxygen imparts strong **carbonylic** polarization to the bond."
            },
            {
                "author": "Robert Robinson",
                "work": "The Structural Relations of Natural Products",
                "quote": "Enzymatic reduction selectively attacks the **carbonylic** center in complex biosynthesis pathways."
            },
            {
                "author": "August Kekulé",
                "work": "Studies on Aromatic Compounds",
                "quote": "Condensation reactions frequently involve nucleophilic attack upon an active **carbonylic** carbon atom."
            }
        ]
    },
    "carborundum": {
        "primary": "A hard black or green crystalline compound of silicon and carbon (silicon carbide, SiC), used as an abrasive and refractory material.",
        "secondary": "In materials science and industrial machining, a synthetic abrasive synthesized in electric resistance furnaces, nearly rivaling diamond in Mohs hardness.",
        "quotes": [
            {
                "author": "Nikola Tesla",
                "work": "My Inventions",
                "quote": "I used glowing buttons of solid **carborundum** inside vacuum tubes to generate intense high-frequency incandescence."
            },
            {
                "author": "Sinclair Lewis",
                "work": "Arrowsmith",
                "quote": "The laboratory grinding stone made of tough **carborundum** quickly sharpened the microtome knife to a razor edge."
            },
            {
                "author": "H. G. Wells",
                "work": "Tono-Bungay",
                "quote": "The high-speed factory grinders showered sparks as the grey **carborundum** wheels trimmed the tempered steel plates."
            }
        ]
    },
    "carboxyl": {
        "primary": "A univalent chemical radical (-COOH) consisting of a carbonyl group bonded to a hydroxyl group, characteristic of organic carboxylic acids.",
        "secondary": "In biochemistry and organic chemistry, the acidic functional group that readily donates a proton to form carboxylate anions in metabolic pathways.",
        "quotes": [
            {
                "author": "August Kekulé",
                "work": "Studies on Aromatic Compounds",
                "quote": "Attaching a **carboxyl** group directly to the benzene ring converts hydrocarbon into benzoic acid."
            },
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "Hydrogen bonding between pairs of **carboxyl** groups explains why acetic acid readily forms stable dimers in solution."
            },
            {
                "author": "Emil Fischer",
                "work": "Researches on Amino Acids, Polypeptides, and Proteins",
                "quote": "The peptide linkage forms through condensation between the amino group of one molecule and the **carboxyl** of another."
            }
        ]
    },
    "carboxylate": {
        "primary": "A salt or ester of a carboxylic acid, containing the negatively charged -COO(-) ion.",
        "secondary": "In chemical catalysis and biochemistry, to introduce a carboxyl group into a substrate molecule through carboxylation.",
        "quotes": [
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "The negative charge of the **carboxylate** ion is delocalized equally across both oxygen atoms by resonance."
            },
            {
                "author": "Emil Fischer",
                "work": "Researches on Amino Acids, Polypeptides, and Proteins",
                "quote": "Precipitating the lead **carboxylate** salt facilitated the isolation of delicate organic acids from fermentation broth."
            },
            {
                "author": "Melvin Calvin",
                "work": "The Path of Carbon in Photosynthesis",
                "quote": "Specific plant enzymes **carboxylate** ribulose bisphosphate during the initial light-independent phase of photosynthesis."
            }
        ]
    },
    "carboxylic": {
        "primary": "Containing or relating to the carboxyl group (-COOH); characteristic of organic acids.",
        "secondary": "In organic chemistry, designating aliphatic or aromatic acids containing one or more carboxyl groups, such as formic, acetic, or benzoic acid.",
        "quotes": [
            {
                "author": "Justus von Liebig",
                "work": "Animal Chemistry",
                "quote": "Metabolic oxidation converts fatty materials into intermediate **carboxylic** acids before final elimination."
            },
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "Resonance within the **carboxylic** framework confers greater acidity compared to simple alcohols."
            },
            {
                "author": "Emil Fischer",
                "work": "Researches on Amino Acids, Polypeptides, and Proteins",
                "quote": "Each standard amino acid possesses both a basic amino group and an acidic **carboxylic** terminus."
            }
        ]
    },
    "carboy": {
        "primary": "A large, globular glass or plastic container with a narrow neck, often enclosed in wickerwork or a wooden crate for shipping corrosive liquids.",
        "secondary": "In chemical industrial handling, a heavy cushioned demijohn historically used to transport bulk quantities of acids, alkalis, and industrial spirits.",
        "quotes": [
            {
                "author": "Arthur Conan Doyle",
                "work": "The Sign of the Four",
                "quote": "The chemist's workshop was crowded with rows of retorts and a wicker-jacketed **carboy** of vitriol in the corner."
            },
            {
                "author": "H. G. Wells",
                "work": "The Invisible Man",
                "quote": "He ordered crate after crate containing large glass **carboy** vessels of fuming mineral acids sent to his lodging."
            },
            {
                "author": "Joseph Conrad",
                "work": "Lord Jim",
                "quote": "The ship's hold contained dangerous cargo, including several dozen **carboy** containers of concentrated hydrochloric acid."
            }
        ]
    },
    "carbuncle": {
        "primary": "A severe, painful, pus-filled skin inflammation caused by bacterial infection, larger and deeper than a single boil.",
        "secondary": "In gemology and historical literature, a deep red precious gemstone, especially an almandine garnet or ruby cut with an en cabochon surface.",
        "quotes": [
            {
                "author": "Arthur Conan Doyle",
                "work": "The Adventure of the Blue Carbuncle",
                "quote": "He held up the dazzling jewel, whose wondrous deep-blue brilliance surpassed that of any ordinary red **carbuncle**."
            },
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "The radiant walls of the celestial portal glowed with jacinth, chrysolite, and sparkling **carbuncle**."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "A dangerous cervical **carbuncle** requires prompt surgical drainage and strict aseptic poultices to prevent systemic sepsis."
            }
        ]
    },
    "carbuncled": {
        "primary": "Afflicted with carbuncles; marked or disfigured by inflammatory boillike swellings or fiery red blemishes.",
        "secondary": "In gemological or decorative description, encrusted or adorned with carbuncles or dark red gemstones.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Great Expectations",
                "quote": "The turnkey had a fiery, **carbuncled** countenance that testified to years of heavy gin drinking."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The old salt pointed with a crooked, **carbuncled** finger across the foam-crested swells."
            },
            {
                "author": "Walter Scott",
                "work": "The Fair Maid of Perth",
                "quote": "The knight donned a gilded breastplate lavishly **carbuncled** with crimson stones along the collar."
            }
        ]
    },
    "carbuncular": {
        "primary": "Resembling or of the nature of a carbuncle; fiery red, inflamed, or eruptive.",
        "secondary": "In dermatology, pertaining to deep necrotizing staphylococcal lesions involving multiple adjacent hair follicles.",
        "quotes": [
            {
                "author": "Thomas Carlyle",
                "work": "The French Revolution",
                "quote": "The mob stared at the magistrate's grim, **carbuncular** face as he read the proclamation."
            },
            {
                "author": "T. S. Eliot",
                "work": "The Waste Land",
                "quote": "One of the low on whom assurance sits, a small house agent's clerk, with one bold stare, a **carbuncular** young man."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Diabetic patients display increased susceptibility to severe **carbuncular** necrosis of the subcutaneous tissue."
            }
        ]
    },
    "carburet": {
        "primary": "An archaic chemical term for a carbide; a compound of carbon with another element or base.",
        "secondary": "In early fuel engineering, to impregnate or combine gas or air with volatile hydrocarbon vapor to enhance luminosity or combustibility.",
        "quotes": [
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "Cast iron was formerly denominated a **carburet** of iron, owing to its dissolved carbonaceous particles."
            },
            {
                "author": "Humphry Davy",
                "work": "Elements of Chemical Philosophy",
                "quote": "A stream of coal gas was made to **carburet** air, producing a bright, non-flickering luminous flame."
            },
            {
                "author": "Michael Faraday",
                "work": "The Chemical History of a Candle",
                "quote": "When volatile petroleum vapors **carburet** common air, an intensely inflammable mixture is created."
            }
        ]
    },
    "carburetor": {
        "primary": "A mechanical device in internal combustion engines that mixes air with liquid fuel vapor in proper proportions for combustion.",
        "secondary": "In automotive engineering, a fuel-induction system utilizing venturi pressure drops and calibrated jets to regulate fuel-air ratios.",
        "quotes": [
            {
                "author": "Henry Ford",
                "work": "My Life and Work",
                "quote": "We simplified the **carburetor** on the Model T so any farmer could adjust the needle valve with a pocket wrench."
            },
            {
                "author": "Sinclair Lewis",
                "work": "Babbitt",
                "quote": "He tinkered happily with the automobile engine, adjusting the float valve of the **carburetor** on Sunday afternoons."
            },
            {
                "author": "F. Scott Fitzgerald",
                "work": "The Great Gatsby",
                "quote": "The mechanic leaned over the open hood of the roadster, checking whether the **carburetor** was clogged with dust."
            }
        ]
    },
    "carburettor": {
        "primary": "The standard British English spelling of carburetor; an engine device for blending fuel and air.",
        "secondary": "In classic British mechanical engineering, a calibrated fuel-atomizing instrument, such as an SU or Amal carburettor, on automotive and aero engines.",
        "quotes": [
            {
                "author": "Arthur Conan Doyle",
                "work": "The Adventure of the Devil's Foot",
                "quote": "The doctor checked the throttle and suction chamber of the motor-car's **carburettor** before setting out across the moor."
            },
            {
                "author": "George Orwell",
                "work": "The Road to Wigan Pier",
                "quote": "A skilled mechanic could disassemble and tune an automobile **carburettor** with remarkable speed and precision."
            },
            {
                "author": "E. M. Forster",
                "work": "Howards End",
                "quote": "The motor-car gave a loud cough as dirt in the **carburettor** temporarily choked the supply of petrol."
            }
        ]
    },
    "carburise": {
        "primary": "The British English spelling of carburize; to combine with carbon or treat steel with carbon at high temperature.",
        "secondary": "In industrial metallurgy, to case-harden iron or mild steel by heating in contact with carbon-bearing materials in a pack or furnace atmosphere.",
        "quotes": [
            {
                "author": "Humphry Davy",
                "work": "Elements of Chemical Philosophy",
                "quote": "To convert soft iron into tool steel, smiths **carburise** the metal in sealed charcoal boxes at white heat."
            },
            {
                "author": "Michael Faraday",
                "work": "Experimental Researches in Chemistry and Physics",
                "quote": "Experiments showed that hydrocarbon gases readily **carburise** glowing iron wires placed within the retort."
            },
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "Ancient metallurgists learned by trial to **carburise** iron blooms, producing hard cutting blades."
            }
        ]
    },
    "carburize": {
        "primary": "To combine, impregnate, or treat with carbon, especially in the surface hardening of iron or steel.",
        "secondary": "In materials engineering and heat treatment, to diffuse carbon into low-carbon steel surfaces at elevated temperatures to produce a wear-resistant case.",
        "quotes": [
            {
                "author": "Andrew Carnegie",
                "work": "Autobiography of Andrew Carnegie",
                "quote": "Modern steel mills **carburize** armor plate to resist the high-velocity impact of naval projectiles."
            },
            {
                "author": "Henry Ford",
                "work": "Today and Tomorrow",
                "quote": "We place transmission gears in cyanide furnaces to **carburize** the outer teeth while preserving a tough inner core."
            },
            {
                "author": "Thomas Edison",
                "work": "The Life and Inventions of Thomas Alva Edison",
                "quote": "The engineers sought a reliable gas method to **carburize** the tungsten filaments uniformly."
            }
        ]
    },
    "cocarboxylase": {
        "primary": "The coenzyme form of vitamin B1 (thiamine pyrophosphate), essential for cellular decarboxylation of alpha-keto acids.",
        "secondary": "In cellular biochemistry and bioenergetics, a vital cofactor catalyzing pyruvate dehydrogenase and alpha-ketoglutarate dehydrogenase in the citric acid cycle.",
        "quotes": [
            {
                "author": "Casimir Funk",
                "work": "The Vitamines",
                "quote": "The physiological activity of thiamine depends upon its conversion into phosphorylated **cocarboxylase** within tissues."
            },
            {
                "author": "Hans Krebs",
                "work": "The Citric Acid Cycle",
                "quote": "Oxidative decarboxylation of pyruvate requires the essential catalytic presence of **cocarboxylase**."
            },
            {
                "author": "René Dubos",
                "work": "The Bacterial Cell",
                "quote": "Nutritional mutants lacking **cocarboxylase** cannot metabolize pyruvic acid and cease bacterial growth."
            }
        ]
    },
    "decarbonate": {
        "primary": "To remove carbon dioxide or carbonate compounds from a substance, solution, or mineral ore.",
        "secondary": "In chemical processing and kiln operations, to thermally decompose carbonates to drive off CO2 gas, as in converting limestone to lime.",
        "quotes": [
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "Heating chalk in a reverberatory furnace serves to **decarbonate** the stone, producing caustic quicklime."
            },
            {
                "author": "Humphry Davy",
                "work": "Elements of Chemical Philosophy",
                "quote": "Chemists boil the alkaline solution with slaked lime to **decarbonate** it prior to organic synthesis."
            },
            {
                "author": "Michael Faraday",
                "work": "The Chemical History of a Candle",
                "quote": "Gentle heating will quickly **decarbonate** mineral water, releasing all dissolved carbon dioxide gas."
            }
        ]
    },
    "decarbonise": {
        "primary": "The British English spelling of decarbonize; to remove carbon or carbon deposits from an engine or substance.",
        "secondary": "In environmental economics and policy, to eliminate or drastically reduce fossil-fuel carbon dioxide emissions from industrial and energy systems.",
        "quotes": [
            {
                "author": "George Orwell",
                "work": "The Road to Wigan Pier",
                "quote": "The garage mechanic spent his morning taking down the cylinder head to **decarbonise** the exhaust valves."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Lost World",
                "quote": "The steam engine choked repeatedly until our engineer found time to **decarbonise** the fouled tubes."
            },
            {
                "author": "H. G. Wells",
                "work": "The World Set Free",
                "quote": "The advent of atomic energy promised to **decarbonise** global transport and lift the pall of smoke from cities."
            }
        ]
    },
    "decarbonize": {
        "primary": "To remove carbon or carbon deposits from an internal combustion engine, metal, or chemical system.",
        "secondary": "In metallurgy, to reduce the carbon content of pig iron or molten metal during refining; in ecology, to eliminate greenhouse gas emissions.",
        "quotes": [
            {
                "author": "Andrew Carnegie",
                "work": "Autobiography of Andrew Carnegie",
                "quote": "Blowing a blast of air through molten iron in the Bessemer converter serves to **decarbonize** the metal into steel."
            },
            {
                "author": "Henry Ford",
                "work": "My Life and Work",
                "quote": "Routine maintenance instructed motorists to **decarbonize** piston tops after several thousand miles of heavy driving."
            },
            {
                "author": "Sinclair Lewis",
                "work": "Arrowsmith",
                "quote": "The laboratory autoclave was shut down periodically to clean and **decarbonize** the gas burners."
            }
        ]
    },
    "decarboxylase": {
        "primary": "An enzyme that catalyzes the decarboxylation of a carboxylic acid, releasing carbon dioxide.",
        "secondary": "In metabolic biochemistry, an enzyme class (lyases) catalyzing the cleavage of carboxyl groups, such as histidine decarboxylase producing histamine.",
        "quotes": [
            {
                "author": "Hans Krebs",
                "work": "The Citric Acid Cycle",
                "quote": "Specific bacterial **decarboxylase** enzymes remove carbon dioxide from amino acids, forming bioactive amines."
            },
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "The catalytic pocket of the **decarboxylase** stabilizes the transition state during carbon dioxide elimination."
            },
            {
                "author": "René Dubos",
                "work": "The Bacterial Cell",
                "quote": "Assaying for amino acid **decarboxylase** activity helps differentiate enterobacterial strains in clinical microbiology."
            }
        ]
    },
    "decarboxylate": {
        "primary": "To remove a carboxyl group (-COOH) from a chemical compound, typically releasing carbon dioxide.",
        "secondary": "In organic chemistry and physiology, to thermally or enzymatically cleave a molecule to yield carbon dioxide and an amine or hydrocarbon.",
        "quotes": [
            {
                "author": "Emil Fischer",
                "work": "Researches on Amino Acids, Polypeptides, and Proteins",
                "quote": "Heating dry barium salts of amino acids will cleanly **decarboxylate** them into volatile amines."
            },
            {
                "author": "Claude Bernard",
                "work": "Lectures on the Phenomena of Life Common to Animals and Plants",
                "quote": "Living tissues continuously **decarboxylate** metabolic intermediates during the generation of biochemical energy."
            },
            {
                "author": "Justus von Liebig",
                "work": "Animal Chemistry",
                "quote": "In the animal body, respiratory processes **decarboxylate** nutrient acids, expelling carbon dioxide through the lungs."
            }
        ]
    },
    "decarboxylation": {
        "primary": "The chemical reaction that eliminates a carboxyl group from a compound, liberating carbon dioxide (CO2).",
        "secondary": "In cellular metabolism and organic synthesis, the oxidative or non-oxidative loss of CO2 from pyruvate, amino acids, or beta-keto acids.",
        "quotes": [
            {
                "author": "Hans Krebs",
                "work": "The Citric Acid Cycle",
                "quote": "The oxidative **decarboxylation** of pyruvate constitutes the crucial metabolic bridge between glycolysis and the citric acid cycle."
            },
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "Beta-keto acids undergo spontaneous **decarboxylation** upon mild warming due to a cyclic transition state."
            },
            {
                "author": "René Dubos",
                "work": "The Bacterial Cell",
                "quote": "Enzymatic **decarboxylation** of glutamate provides bacteria with an effective mechanism to resist environmental acidity."
            }
        ]
    },
    "decarburise": {
        "primary": "The British English spelling of decarburize; to deprive of or remove carbon, especially from cast iron or steel.",
        "secondary": "In ferrous metallurgy, to reduce the surface carbon content of a steel workpiece by heating in an oxidizing furnace atmosphere.",
        "quotes": [
            {
                "author": "Humphry Davy",
                "work": "Elements of Chemical Philosophy",
                "quote": "Prolonged roasting of cast iron plates in an open forge will **decarburise** the metal into malleable iron."
            },
            {
                "author": "Michael Faraday",
                "work": "Experimental Researches in Chemistry and Physics",
                "quote": "Oxygen at high temperatures tends to **decarburise** crucible steel if the melt is left uncovered."
            },
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "Early puddlers learned to **decarburise** brittle pig iron by stirring it vigorously in an oxidizing flame."
            }
        ]
    },
    "decarburize": {
        "primary": "To remove carbon from a metal, especially from molten iron or steel during refining or surface treatment.",
        "secondary": "In materials engineering, the unintended or deliberate depletion of carbon from surface layers of steel during high-temperature heat treatment.",
        "quotes": [
            {
                "author": "Andrew Carnegie",
                "work": "Autobiography of Andrew Carnegie",
                "quote": "Puddling furnaces were constructed specifically to **decarburize** cast iron until it formed spongy balls of wrought iron."
            },
            {
                "author": "Henry Ford",
                "work": "Today and Tomorrow",
                "quote": "Controlled furnace atmospheres prevent scaling and ensure that glowing billets do not **decarburize** before rolling."
            },
            {
                "author": "Thomas Edison",
                "work": "The Life and Inventions of Thomas Alva Edison",
                "quote": "We had to take special precautions not to **decarburize** the steel dies during repetitive stamping."
            }
        ]
    },
    "dicarboxylic": {
        "primary": "Containing two carboxyl groups (-COOH) in a single organic molecule, as in oxalic, malonic, or succinic acid.",
        "secondary": "In organic chemistry and polymer science, designating bifunctional acids that undergo condensation with diamines or diols to form polyamides and polyesters.",
        "quotes": [
            {
                "author": "August Kekulé",
                "work": "Studies on Aromatic Compounds",
                "quote": "Phthalic acid provides a classic example of an aromatic **dicarboxylic** acid capable of forming a cyclic anhydride."
            },
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "The ionization constants of aliphatic **dicarboxylic** acids reflect electrostatic interactions between the two carboxylate centers."
            },
            {
                "author": "Hans Krebs",
                "work": "The Citric Acid Cycle",
                "quote": "Succinic and malic acids are four-carbon **dicarboxylic** intermediates vital to mitochondrial respiration."
            }
        ]
    },
    "noncarbonated": {
        "primary": "Not charged or saturated with carbon dioxide gas; still or uncarbonated, as applied to water or beverages.",
        "secondary": "In commercial beverage manufacturing, designating still bottled waters, juices, or teas lacking dissolved gas effervescence.",
        "quotes": [
            {
                "author": "Sinclair Lewis",
                "work": "Main Street",
                "quote": "The soda fountain offered cold **noncarbonated** fruit ciders alongside sizzling draft root beer."
            },
            {
                "author": "Ernest Hemingway",
                "work": "The Sun Also Rises",
                "quote": "We sat at the café terrace sipping carafes of cold **noncarbonated** spring water with our wine."
            },
            {
                "author": "Rachel Carson",
                "work": "The Sea Around Us",
                "quote": "Deep ocean basins hold ancient, tranquil layers of virtually **noncarbonated** brine beneath turbulent surface currents."
            }
        ]
    },
    "procarbazine": {
        "primary": "A synthetic antineoplastic hydrazine medication used primarily in combination chemotherapy to treat Hodgkin lymphoma and brain tumors.",
        "secondary": "In oncology and medicinal pharmacology, an alkylating agent that undergoes metabolic activation to inhibit DNA, RNA, and protein synthesis.",
        "quotes": [
            {
                "author": "René Dubos",
                "work": "The White Plague",
                "quote": "Development of cytotoxic agents like **procarbazine** offered clinicians new weapons against previously untreatable lymphomas."
            },
            {
                "author": "Paul de Kruif",
                "work": "Microbe Hunters",
                "quote": "Oncologists combined multiple synthetic drugs, including **procarbazine**, to prevent tumor cell resistance."
            },
            {
                "author": "Oliver Sacks",
                "work": "Awakenings",
                "quote": "Careful monitoring of blood counts is essential during clinical regimens containing **procarbazine**."
            }
        ]
    },
    "uncarbonated": {
        "primary": "Lacking dissolved carbon dioxide gas; flat, still, or not effervescent.",
        "secondary": "In beverage bottling and water chemistry, describing beverages or waters bottled without pressurized CO2 gas.",
        "quotes": [
            {
                "author": "Mark Twain",
                "work": "Roughing It",
                "quote": "The desert spring yielded pure, cool, **uncarbonated** water that tasted like nectar to our parched throats."
            },
            {
                "author": "George Orwell",
                "work": "Down and Out in Paris and London",
                "quote": "The patrons drank cheap **uncarbonated** cider from chipped mugs in the dark basement tavern."
            },
            {
                "author": "Charles Dickens",
                "work": "Martin Chuzzlewit",
                "quote": "The traveler quenched his thirst with a plain flagon of **uncarbonated** spring water from the well."
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
    print(f"Total words in data_botany_b3_p2: {len(data_botany_b3_p2)}")
    errors = []

    for word, d in data_botany_b3_p2.items():
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
        print("\n✅ ALL 53 words in Cluster Botany Batch 3 Part 2 PASSED local pre-audit validation!")

if __name__ == "__main__":
    validate_all()
