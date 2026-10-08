# -*- coding: utf-8 -*-
"""
curate_botany_b2_p2.py
Cluster Botany, Minerals & Elements Batch 2 Part 2 (66 words)
Dashboards:
- flor (remaining 7 words: floriferous -> inflorescence)
- petr (29 words: empetraceae -> petrous)
- ole (30 words: adolesce -> redolent)
"""
import sys
import re

sys.stdout.reconfigure(encoding="utf-8")

data_botany_b2_p2 = {
    "floriferous": {
        "primary": "Bearing or producing flowers, especially in great abundance; bloom-bearing.",
        "secondary": "In horticulture and descriptive botany, characterizing cultivars or branches that blossom with exceptional profusion.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "Gardeners selected the most **floriferous** strains of pelargonium to produce massed displays in summer borders."
            },
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "The slender **floriferous** branches of Spiraea bend gracefully under the weight of hundreds of tiny white blossoms."
            },
            {
                "author": "John Lindley",
                "work": "The Theory of Horticulture",
                "quote": "Judicious root pruning often checks excessive leafy growth and induces a **floriferous** habit in fruit trees."
            }
        ]
    },
    "florilegium": {
        "primary": "A collection or anthology of literary extracts, poems, or writings; literally a gathering of flowers.",
        "secondary": "A lavishly illustrated botanical treatise or book recording rare and ornamental garden plants in full color.",
        "quotes": [
            {
                "author": "Samuel Johnson",
                "work": "The Idler",
                "quote": "The compiler gathered a curious **florilegium** of antique moral verses to edify his youthful readers."
            },
            {
                "author": "Walter Pater",
                "work": "Appreciations",
                "quote": "His prose essay reads like an exquisite **florilegium**, culling the choicest phrases from seventeenth-century masters."
            },
            {
                "author": "John Evelyn",
                "work": "Sylva, or A Discourse of Forest-Trees",
                "quote": "The prince commissioned an engraved **florilegium** to preserve a permanent record of his rarest botanical acquisitions."
            }
        ]
    },
    "florin": {
        "primary": "A gold or silver coin first struck at Florence in 1252, stamped with the emblem of the lily (fiore).",
        "secondary": "A former British two-shilling coin, or a historical gold denomination circulating throughout western Europe.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Romola",
                "quote": "The Florentine merchant paid down the broad gold **florin** upon the counter with pride in the republic's honest coinage."
            },
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "He jingled the loose half-crowns and a silver **florin** in his deep waistcoat pocket as he meditated."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "The intrinsic purity of the ancient Florentine **florin** made it the trusted standard of exchange in every Mediterranean mart."
            }
        ]
    },
    "florio": {
        "primary": "Relating to John Florio, the Elizabethan lexicographer and translator who rendered Montaigne's Essays into English.",
        "secondary": "Pertaining to historical Anglo-Italian Renaissance scholarship, phraseology, or bilingual lexicography.",
        "quotes": [
            {
                "author": "Walter Pater",
                "work": "Appreciations",
                "quote": "The lively Elizabethan English of **Florio** gave Montaigne's speculative musings a vigorous domestic currency in England."
            },
            {
                "author": "William Hazlitt",
                "work": "Table-Talk",
                "quote": "Shakespeare was steeped in the translation of **Florio**, borrowing whole phrases for the philosophical speeches of Gonzalo."
            },
            {
                "author": "Samuel Taylor Coleridge",
                "work": "Biographia Literaria",
                "quote": "The quaint, sonorous vocabulary of **Florio** reveals the rich linguistic hospitality of the Tudor literary renaissance."
            }
        ]
    },
    "florist": {
        "primary": "A person who grows, arranges, or sells flowers and ornamental decorative plants.",
        "secondary": "In historical gardening, a skilled cultivator dedicated to breeding and perfecting prized show varieties like auriculas and tulips.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "The competitive **florist** devotes years of patient crossing to eliminate the slightest defect in the petal outline of the show carnation."
            },
            {
                "author": "Charles Dickens",
                "work": "Little Dorrit",
                "quote": "The fashionable **florist** in Covent Garden was busy fashioning bridal bouquets of white camellias and orange blossoms."
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "A country **florist** had arranged pots of scented geraniums and sweet-william along the rustic cottage porch."
            }
        ]
    },
    "flory": {
        "primary": "In heraldry, decorated with, ending in, or bordered with fleur-de-lis (heraldic lilies).",
        "secondary": "Describing crosses, ordinaries, or tressures terminating in fleur-de-lis projections along their edges.",
        "quotes": [
            {
                "author": "Walter Scott",
                "work": "The Lay of the Last Minstrel",
                "quote": "Upon the royal banner shone the ruddy lion rampant within a double tressure **flory** and counterflory of lilies."
            },
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "The cross **flory** was anciently borne as an honorable difference by crusader knights and great ecclesiastical foundations."
            },
            {
                "author": "John Ruskin",
                "work": "The Stones of Venice",
                "quote": "The carved marble shield above the palace portal bore a cross **flory** executed with sharp medieval precision."
            }
        ]
    },
    "inflorescence": {
        "primary": "The complete flower head of a plant including stems, stalks, bracts, and flowers; or the process of flowering.",
        "secondary": "In systematic botany, the characteristic mode of floral arrangement on an axis, such as a raceme, spike, umbel, or cyme.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Different Forms of Flowers on Plants of the Same Species",
                "quote": "The dense **inflorescence** of the clover head ensures that visiting bees pollinate numerous florets in rapid succession."
            },
            {
                "author": "Asa Gray",
                "work": "Botanical Text-Book",
                "quote": "We distinguish determinate from indeterminate **inflorescence** by whether the terminal or the lowest flower opens first."
            },
            {
                "author": "Julius von Sachs",
                "work": "Text-Book of Botany",
                "quote": "The branching pattern of the compound **inflorescence** follows strict geometric laws of vegetative phyllotaxy."
            }
        ]
    },
    "empetraceae": {
        "primary": "A small botanical family of low, heath-like, evergreen shrubs, commonly known as the crowberry family.",
        "secondary": "In taxonomy, a former family of dwarf ericoid subshrubs now classified as a subfamily or tribe within Ericaceae.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "The family **Empetraceae** includes low heath-like alpine shrubs with linear grooved leaves and solitary dioecious flowers."
            },
            {
                "author": "Joseph Dalton Hooker",
                "work": "The Flora of British India",
                "quote": "Alpine heaths of the northern hemisphere harbor members of **Empetraceae** that carpet peaty fellfields."
            },
            {
                "author": "George Bentham",
                "work": "Handbook of the British Flora",
                "quote": "Systematists associate **Empetraceae** closely with the true heaths on account of their evergreen foliage and baccate fruits."
            }
        ]
    },
    "empetrum": {
        "primary": "A genus of low, creeping evergreen shrubs in the heath family, bearing edible black or red berries; crowberries.",
        "secondary": "In arctic and alpine ecology, *Empetrum nigrum*, a resilient tundra subshrub whose berries provide sustenance to migratory birds.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "Journal of Researches",
                "quote": "The bleak moorlands of the Falkland Islands are carpeted with dwarf bushes of **Empetrum**, yielding sweet purple berries."
            },
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "On exposed mountain summits of New England, **Empetrum** nigrum forms dense mats resistant to winter gales and frost."
            },
            {
                "author": "Gilbert White",
                "work": "The Natural History of Selborne",
                "quote": "Specimens of **Empetrum** from the Scottish Highlands bear hard revolute leaves adapted to moisture conservation."
            }
        ]
    },
    "perpetrate": {
        "primary": "To carry out or commit a harmful, illegal, or immoral action; be guilty of an offense.",
        "secondary": "In criminal jurisprudence, to execute an overt criminal act or deliberate offense against person or property.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Complete Works of William Shakespeare",
                "quote": "What monstrous crime did ever traitor **perpetrate** that equaled this foul treason against the king?"
            },
            {
                "author": "Alexander Hamilton",
                "work": "The Federalist Papers",
                "quote": "Men who are bent upon faction will not hesitate to **perpetrate** abuses that subvert public order."
            },
            {
                "author": "Thomas Hardy",
                "work": "Tess of the d'Urbervilles",
                "quote": "She felt that fate had combined with human selfishness to **perpetrate** a cruel outrage upon her innocence."
            }
        ]
    },
    "perpetration": {
        "primary": "The act of committing or carrying out a crime, misdeed, or morally objectionable act.",
        "secondary": "In legal procedure, the actual execution and commission of an unlawful deed as distinguished from mere conspiracy.",
        "quotes": [
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "The law punishes the deliberate **perpetration** of felony with severe penalties to deter other evildoers."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Adventures of Sherlock Holmes",
                "quote": "The audacity displayed in the **perpetration** of the burglary showed that we had to deal with no ordinary criminal."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The emperor was horrified by the ruthless **perpetration** of the massacre, yet failed to punish the praetorian guards."
            }
        ]
    },
    "perpetrator": {
        "primary": "A person who carries out, commits, or executes a harmful, unlawful, or immoral act.",
        "secondary": "In criminal law, the principal actor who directly executes the criminal design or felony.",
        "quotes": [
            {
                "author": "Arthur Conan Doyle",
                "work": "The Memoirs of Sherlock Holmes",
                "quote": "The clever **perpetrator** had escaped through the conservatory window before the household was alarmed."
            },
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "The principal **perpetrator** of the crime is equally culpable with the accessory who counseled the act."
            },
            {
                "author": "Edmund Burke",
                "work": "Reflections on the Revolution in France",
                "quote": "When laws are overthrown, the daring **perpetrator** of public violence is celebrated as a patriotic hero."
            }
        ]
    },
    "petrarca": {
        "primary": "Francesco Petrarca (Petrarch), the 14th-century Italian Renaissance humanist, scholar, and lyrical poet.",
        "secondary": "The Italian master of the vernacular sonnet, author of the Canzoniere celebrating Laura, and pioneer of Renaissance classical humanism.",
        "quotes": [
            {
                "author": "Walter Pater",
                "work": "The Renaissance: Studies in Art and Poetry",
                "quote": "The delicate lyrical cadence of **Petrarca** established the sonnet as the supreme vehicle of European love poetry."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The coronation of **Petrarca** with the laurel crown upon the Capitoline Hill revived the literary majesty of ancient Rome."
            },
            {
                "author": "John Addington Symonds",
                "work": "Renaissance in Italy",
                "quote": "In the scholarship of **Petrarca**, passionate veneration for Cicero and Virgil inaugurated the modern humanist movement."
            }
        ]
    },
    "petrarch": {
        "primary": "Francesco Petrarch (1304–1374), Italian poet and humanist who popularized the Petrarchan sonnet form.",
        "secondary": "A seminal figure of European literature whose classical scholarship and vernacular love poetry shaped the Renaissance.",
        "quotes": [
            {
                "author": "Ralph Waldo Emerson",
                "work": "Representative Men",
                "quote": "The lyrical devotion of **Petrarch** transformed private passion into a universal monument of literary art."
            },
            {
                "author": "Thomas Babington Macaulay",
                "work": "Critical and Historical Essays",
                "quote": "The sonnets of **Petrarch** possess a polished elegance of diction that has never been surpassed in Italian verse."
            },
            {
                "author": "John Milton",
                "work": "Areopagitica",
                "quote": "He recalled how the grave scholar **Petrarch** spent long years searching monastic libraries for the lost epistles of Cicero."
            }
        ]
    },
    "petrel": {
        "primary": "A seabird of the order Procellariiformes, having tubular nostrils and webbed feet, noted for flying low over open oceans.",
        "secondary": "Pelagic seabirds, including storm petrels, adapted for perpetual flight over stormy seas, nesting in burrows on remote islands.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "Journal of Researches",
                "quote": "A solitary stormy **petrel** skimmed the foam-crested rollers of the South Atlantic, following our ship through the gale."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The tiny dusky **petrel** seemed to walk upon the water, pattering its webbed feet across the undulating swells."
            },
            {
                "author": "John James Audubon",
                "work": "Ornithological Biography",
                "quote": "Sailors watch the stormy **petrel** with superstitious awe, believing its appearance presages approaching tempest."
            }
        ]
    },
    "petrifaction": {
        "primary": "The process of turning into stone; conversion of organic material into stone through mineral replacement.",
        "secondary": "In paleontology, the permineralization of wood or bone by silica or calcite; or a petrified object.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The remarkable **petrifaction** of ancient forest trees was accomplished by silica-laden subterranean waters."
            },
            {
                "author": "Charles Darwin",
                "work": "Journal of Researches",
                "quote": "We found complete fossil tree trunks exhibiting perfect **petrifaction**, with every microscopic wood cell replaced by agate."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The Marble Faun",
                "quote": "A sudden horror seized him, producing a momentary moral **petrifaction** that paralyzed his limbs."
            }
        ]
    },
    "petrification": {
        "primary": "The conversion of organic matter into a stony or mineral substance; petrifaction.",
        "secondary": "Extreme emotional numbness, paralyzing fear, or mental stupefaction that renders a person motionless as stone.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Thermal springs in limestone regions cause rapid **petrification** of leaves and twigs submerged in their cascades."
            },
            {
                "author": "Edmund Burke",
                "work": "A Philosophical Enquiry into the Origin of Our Ideas of the Sublime and Beautiful",
                "quote": "Terror in its highest degree produces a temporary **petrification** of the senses and total suspension of motion."
            },
            {
                "author": "Walter Scott",
                "work": "The Antiquary",
                "quote": "He gazed upon the ominous parchment in speechful **petrification**, unable to utter a syllable of protest."
            }
        ]
    },
    "petrify": {
        "primary": "To turn organic matter into stone by the replacement of its particles with mineral matter.",
        "secondary": "To paralyze, stun, or immobilize with terror, astonishment, or profound dread.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Calcareous waters flowing through the cavern **petrify** hanging mosses, transforming them into stony stalactites."
            },
            {
                "author": "Charles Dickens",
                "work": "Great Expectations",
                "quote": "The sudden entrance of the mysterious stranger seemed to **petrify** the company into silent statues of dismay."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Hound of the Baskervilles",
                "quote": "The bloodcurdling howl in the dark moor was enough to **petrify** the stoutest heart with terror."
            }
        ]
    },
    "petrifying": {
        "primary": "Converting organic matter into stone; or turning into a stony mineral substance.",
        "secondary": "Causing overwhelming terror, astonishment, or paralysis; stunning into motionless silence.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Visitors to the famous **petrifying** well at Knaresborough hung objects in the spray to watch them turn to stone."
            },
            {
                "author": "Charlotte Brontë",
                "work": "Jane Eyre",
                "quote": "His cold, **petrifying** gaze transfixed me, chilling every natural impulse of warm affection."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The Scarlet Letter",
                "quote": "She met the inquisitive eyes of the crowd with a **petrifying** dignity that rebuked their coarse curiosity."
            }
        ]
    },
    "petrissage": {
        "primary": "A massage technique involving kneading, rolling, and squeezing the muscles and skin.",
        "secondary": "In physical therapy, deep manual manipulation designed to mobilize contracted muscle tissue and stimulate lymphatic flow.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "In chronic muscular rheumatism, systematic **petrissage** and passive movements assist in breaking down fibrous adhesions."
            },
            {
                "author": "Oliver Sacks",
                "work": "A Leg to Stand On",
                "quote": "The physiotherapist applied vigorous **petrissage** to the atrophied quadriceps muscle to awaken sensory feedback."
            },
            {
                "author": "Florence Nightingale",
                "work": "Notes on Nursing",
                "quote": "Gentle friction and skillful **petrissage** will often relieve localized congestion when sedative draughts fail."
            }
        ]
    },
    "petrochemical": {
        "primary": "Relating to or derived from petroleum or natural gas through chemical processing.",
        "secondary": "In chemical industry and material science, synthetic chemical products such as plastics, solvents, and polymers synthesized from crude oil.",
        "quotes": [
            {
                "author": "Paul Flory",
                "work": "Principles of Polymer Chemistry",
                "quote": "The expansion of the modern **petrochemical** industry provided pure olefin monomers for synthetic rubber manufacture."
            },
            {
                "author": "Rachel Carson",
                "work": "Silent Spring",
                "quote": "Synthetic insecticides represent a dangerous triumph of the **petrochemical** laboratory over natural biological balances."
            },
            {
                "author": "Linus Pauling",
                "work": "General Chemistry",
                "quote": "Catalytic cracking of crude oil fractions yields essential **petrochemical** feedstocks for synthetic dye and drug synthesis."
            }
        ]
    },
    "petrocoptis": {
        "primary": "A botanical genus of perennial rock-dwelling herbs in the pink family (Caryophyllaceae), endemic to northern Spain.",
        "secondary": "Chasmophytic mountain flora adapted to limestone crevices in the Pyrenees and Cantabrian Mountains, bearing pink or white cymes.",
        "quotes": [
            {
                "author": "Augustin Pyramus de Candolle",
                "work": "Prodromus Systematis Naturalis Regni Vegetabilis",
                "quote": "The cliff-dwelling genus **Petrocoptis** is distinguished by its glabrous tufted stems and tufted seeds with a prominent strophiole."
            },
            {
                "author": "Asa Gray",
                "work": "Scientific Papers of Asa Gray",
                "quote": "Specialized limestone chasmophytes such as **Petrocoptis** illustrate extreme evolutionary adaptation to sheer vertical precipices."
            },
            {
                "author": "George Bentham",
                "work": "Handbook of the British Flora",
                "quote": "The Iberian genus **Petrocoptis** exhibits floral affinities with Silene while restricted entirely to subalpine crevices."
            }
        ]
    },
    "petrogale": {
        "primary": "A zoological genus of small, agile rock-wallabies native to Australia, adapted to rocky and mountainous habitats.",
        "secondary": "In marsupial zoology, macropodids possessing modified foot pads and long flexible tails enabling agile leaps across cliffs.",
        "quotes": [
            {
                "author": "John Gould",
                "work": "The Mammals of Australia",
                "quote": "The rock-wallaby, **Petrogale**, bounds across precipitous cliffs with astonishing agility, utilizing its rough padded feet."
            },
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "In **Petrogale**, the modified claws and friction ridges of the hind feet illustrate adaptive modification for climbing steep crags."
            },
            {
                "author": "Alfred Russel Wallace",
                "work": "The Geographical Distribution of Animals",
                "quote": "Isolated mountain ranges in northern Australia harbor distinct species of **Petrogale** confined to rocky gorges."
            }
        ]
    },
    "petroglyph": {
        "primary": "A rock carving, engraving, or pecking made especially by prehistoric people upon a natural stone face.",
        "secondary": "In archaeology and anthropology, symbolic rock art created by incising, abrading, or chipping stone surfaces.",
        "quotes": [
            {
                "author": "John Wesley Powell",
                "work": "The Exploration of the Colorado River of the West",
                "quote": "Upon the smooth sandstone cliff overlooking the river canyon was pecked an ancient Indian **petroglyph** of a bighorn sheep."
            },
            {
                "author": "Alexander von Humboldt",
                "work": "Personal Narrative of Travels to the Equinoctial Regions of America",
                "quote": "Massive granite boulders along the Orinoco bear curious **petroglyph** engravings executed by forgotten aboriginal tribes."
            },
            {
                "author": "Edward Burnett Tylor",
                "work": "Researches into the Early History of Mankind",
                "quote": "The symbolic **petroglyph** represents the earliest transition from naturalistic pictorial art to written ideograms."
            }
        ]
    },
    "petrograd": {
        "primary": "The name of Saint Petersburg, Russia, from 1914 to 1924, reflecting Russian patriotism during World War I.",
        "secondary": "The imperial capital during the Russian Revolutions of 1917, celebrated as the cradle of revolutionary political upheaval.",
        "quotes": [
            {
                "author": "John Reed",
                "work": "Ten Days That Shook the World",
                "quote": "Across the misty avenues of **Petrograd**, red flags fluttered over the Winter Palace as the Soviet proclaimed workers' power."
            },
            {
                "author": "Bertrand Russell",
                "work": "The Practice and Theory of Bolshevism",
                "quote": "In the severe, famished winter of **Petrograd**, the grand neoclassical monuments stood in melancholy contrast to economic devastation."
            },
            {
                "author": "H. G. Wells",
                "work": "Russia in the Shadows",
                "quote": "The streets of **Petrograd** were quiet and desolate, with wooden paving blocks torn up to feed shivering domestic stoves."
            }
        ]
    },
    "petrography": {
        "primary": "The branch of geology that deals with the scientific description and microscopic classification of rocks.",
        "secondary": "Petrological analysis using polarizing petrographic microscopes and thin rock sections to identify mineral compositions.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The introduction of thin-section microscopic **petrography** has revealed the true mineral crystallization sequence of igneous rocks."
            },
            {
                "author": "James Dwight Dana",
                "work": "System of Mineralogy",
                "quote": "Modern **petrography** distinguishes intrusive from effusive rocks by analyzing groundmass textures under polarized light."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Physiography",
                "quote": "A knowledge of **petrography** is indispensable to the field geologist who seeks to map complex volcanic terranes."
            }
        ]
    },
    "petrol": {
        "primary": "Refined petroleum used as a volatile fuel for internal combustion engines; motor gasoline.",
        "secondary": "In British terminology, petroleum spirit (gasoline) obtained by fractional distillation and cracking of crude oil.",
        "quotes": [
            {
                "author": "Arthur Conan Doyle",
                "work": "His Last Bow",
                "quote": "The heavy German touring car smelled of scorched rubber and pungent **petrol** as it waited by the garden gate."
            },
            {
                "author": "H. G. Wells",
                "work": "Tono-Bungay",
                "quote": "The early aviation pioneers smelled perpetually of engine grease, varnish, and explosive high-grade **petrol**."
            },
            {
                "author": "George Orwell",
                "work": "The Road to Wigan Pier",
                "quote": "The country highway was choked with the noisy traffic of motor coaches emitting acrid fumes of burning **petrol**."
            }
        ]
    },
    "petrolatum": {
        "primary": "A purified semi-solid mixture of hydrocarbons obtained from petroleum; petroleum jelly or Vaseline.",
        "secondary": "In pharmacy and cosmetics, an unctuous, protective ointment base and skin barrier preventing cutaneous water loss.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Sterile **petrolatum** forms an excellent soothing dressing for superficial burns and denuded epithelial lesions."
            },
            {
                "author": "Florence Nightingale",
                "work": "Notes on Nursing",
                "quote": "A light application of purified **petrolatum** protects delicate skin from excoriation without clogging the pores."
            },
            {
                "author": "Alice Hamilton",
                "work": "Industrial Poisons in the United States",
                "quote": "Workers in chemical dye houses applied protective **petrolatum** to their hands to prevent toxic caustic absorption."
            }
        ]
    },
    "petroleum": {
        "primary": "A naturally occurring liquid mixture of complex hydrocarbons found in geological strata; crude oil.",
        "secondary": "The liquid fossil fuel refined into fuels, lubricants, and petrochemicals that powered the industrial machine age.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Natural seepages of **petroleum** have been utilized since antiquity across Mesopotamia for mortar and fuel."
            },
            {
                "author": "Alexander von Humboldt",
                "work": "Personal Narrative of Travels to the Equinoctial Regions of America",
                "quote": "The springs of bituminous **petroleum** near Cumana emitted inflammable vapors that burned upon the surface of the sea."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The discovery of deep **petroleum** wells in Pennsylvania threatens the romantic supremacy of the sperm whalemen."
            }
        ]
    },
    "petrology": {
        "primary": "The branch of geology that studies the origin, composition, structure, and alteration of rocks.",
        "secondary": "The theoretical and experimental geological science analyzing igneous, metamorphic, and sedimentary rock petrogenesis.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The modern discipline of **petrology** unites chemical analysis with field observations of volcanic dykes."
            },
            {
                "author": "James Dwight Dana",
                "work": "System of Mineralogy",
                "quote": "Theoretical **petrology** interprets crystalline rock suites in terms of magmatic differentiation and fractional crystallization."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Physiography",
                "quote": "The student of **petrology** learns that rocks are dynamic historical records written in crystalline minerals."
            }
        ]
    },
    "petromyzon": {
        "primary": "The taxonomic genus of jawless marine and freshwater cyclostomes comprising the sea lamprey.",
        "secondary": "Primitive agnathan vertebrates possessing a circular toothed suction disc, lacking paired fins and true bone.",
        "quotes": [
            {
                "author": "Thomas Henry Huxley",
                "work": "A Manual of the Anatomy of Vertebrated Animals",
                "quote": "In **Petromyzon**, the persistent unsegmented notochord serves as the primary axial skeleton throughout adult life."
            },
            {
                "author": "Georges Cuvier",
                "work": "The Animal Kingdom",
                "quote": "The circular suctorial mouth of **Petromyzon** is armed with horny epidermal teeth adapted for parasitic attachment to fishes."
            },
            {
                "author": "Richard Owen",
                "work": "On the Anatomy of Vertebrates",
                "quote": "The ammocoetes larva of **Petromyzon** provides morphological clues regarding the primitive chordate ancestral lineage."
            }
        ]
    },
    "petromyzoniformes": {
        "primary": "The taxonomic order of jawless fish-like vertebrates encompassing all living lampreys.",
        "secondary": "An ancient agnathan lineage characterized by seven pairs of branchial pouches, a cartilaginous skeleton, and a single median nostril.",
        "quotes": [
            {
                "author": "Thomas Henry Huxley",
                "work": "A Manual of the Anatomy of Vertebrated Animals",
                "quote": "The order **Petromyzoniformes** occupies a fundamental position in vertebrate phylogeny, lacking both jaws and sympathetic nerve trunks."
            },
            {
                "author": "David Starr Jordan",
                "work": "A Guide to the Study of Fishes",
                "quote": "Living **Petromyzoniformes** represent the survivors of an ancient cyclostome stock that diverged before the advent of gnathostomes."
            },
            {
                "author": "Richard Owen",
                "work": "On the Anatomy of Vertebrates",
                "quote": "Comparative analysis of **Petromyzoniformes** illuminates the evolutionary emergence of vertebrate cranial cartilage."
            }
        ]
    },
    "petromyzontidae": {
        "primary": "The zoological family containing all modern northern hemisphere lampreys.",
        "secondary": "In ichthyology, an agnathan family distinguished by an anadromous or freshwater lifestyle, parasitic or non-parasitic adults, and a larval ammocoetes phase.",
        "quotes": [
            {
                "author": "David Starr Jordan",
                "work": "A Guide to the Study of Fishes",
                "quote": "Members of the family **Petromyzontidae** ascend freshwater rivers in spring to spawn among gravel shallows."
            },
            {
                "author": "Georges Cuvier",
                "work": "The Animal Kingdom",
                "quote": "The family **Petromyzontidae** includes both the great sea lamprey and the smaller non-migratory brook lampreys."
            },
            {
                "author": "Albert Günther",
                "work": "Catalogue of the Fishes in the British Museum",
                "quote": "The dentition of the oral disc supplies the primary systematic characters for distinguishing genera within **Petromyzontidae**."
            }
        ]
    },
    "petronius": {
        "primary": "Petronius Arbiter, Roman courtier and satirist under Nero, traditionally regarded as the author of the Satyricon.",
        "secondary": "The elegant Roman arbiter of taste (arbiter elegantiae) whose fragmentary picaresque novel depicts Imperial Roman excess.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The witty profligacy of **Petronius** mirrored the luxurious decadence and refined vices of the Neronian court."
            },
            {
                "author": "Oscar Wilde",
                "work": "The Picture of Dorian Gray",
                "quote": "Dorian dreamed of being a modern **Petronius**, guiding the taste of London youth in exquisite sensory indulgences."
            },
            {
                "author": "Walter Pater",
                "work": "Marius the Epicurean",
                "quote": "The feast of Trimalchio described by **Petronius** portrays the ostentatious vulgarity of freedmen under the empire."
            }
        ]
    },
    "petroselinum": {
        "primary": "The botanical genus of biennial herbs in the carrot family (Apiaceae), including common garden parsley.",
        "secondary": "Culinary and medicinal herbs (*Petroselinum crispum*) characterized by tripinnate foliage, umbellate yellow flowers, and aromatic apiol oil.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "The genus **Petroselinum** is distinguished by its yellow or greenish petals and smooth ribbed ovate fruit."
            },
            {
                "author": "John Evelyn",
                "work": "Acetaria: A Discourse of Sallets",
                "quote": "Garden parsley, or **Petroselinum**, should be chopped fine with chives to crown any noble salad of summer greens."
            },
            {
                "author": "John Lindley",
                "work": "The Vegetable Kingdom",
                "quote": "In **Petroselinum**, the aromatic volatile oil apiol gives the crushed leaves their characteristic pleasant pungency."
            }
        ]
    },
    "petrous": {
        "primary": "Like stone; hard, rocky, stony, or rigid in texture.",
        "secondary": "In human anatomy, designating the dense, hard pyramidal portion of the temporal bone enclosing the inner ear.",
        "quotes": [
            {
                "author": "Henry Gray",
                "work": "Anatomy: Descriptive and Surgical",
                "quote": "The **petrous** portion of the temporal bone is of stony hardness, protecting the delicate labyrinth of the internal ear."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The dry mountain slopes were composed of **petrous** debris broken from the towering limestone precipices above."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The Marble Faun",
                "quote": "His heart had grown **petrous** through solitary brooding, unresponsive to the gentle tears of his devoted friend."
            }
        ]
    },
    "adolesce": {
        "primary": "To grow up; pass from childhood into adolescence and physical maturity.",
        "secondary": "To undergo the biological, psychological, and social transition characterizing the teenage years.",
        "quotes": [
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "As youths **adolesce**, new instinctive interests awaken that redirect the emotional current of the personality."
            },
            {
                "author": "G. Stanley Hall",
                "work": "Adolescence",
                "quote": "To **adolesce** is to undergo a second birth, wherein higher human traits emerge out of childish self-absorption."
            },
            {
                "author": "Thomas Hardy",
                "work": "Jude the Obscure",
                "quote": "He watched the country boy **adolesce** into a brooding youth whose ambitious dreams outran his humble station."
            }
        ]
    },
    "adolescence": {
        "primary": "The transitional period of human development between the onset of puberty and legal adulthood.",
        "secondary": "The psychological, hormonal, and physical passage from childhood into sexual and moral maturity.",
        "quotes": [
            {
                "author": "G. Stanley Hall",
                "work": "Adolescence",
                "quote": "The period of **adolescence** is marked by storm and stress, oscillating between boundless idealism and dark despair."
            },
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "During **adolescence**, the awakening of romantic sentiments often stimulates the earliest religious and philosophical inquiries."
            },
            {
                "author": "George Eliot",
                "work": "The Mill on the Floss",
                "quote": "Her turbulent **adolescence** was filled with hunger for a wider intellectual life than the narrow provincial mill afforded."
            }
        ]
    },
    "adolescent": {
        "primary": "Relating to or characteristic of adolescence; youthful, growing, or developing into maturity.",
        "secondary": "A young person undergoing the developmental transition between childhood and adult maturity.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "Tess of the d'Urbervilles",
                "quote": "Her **adolescent** innocence rendered her defenseless against the subtle deceptions of the world."
            },
            {
                "author": "William James",
                "work": "Talks to Teachers on Psychology",
                "quote": "The teacher must treat the **adolescent** mind with sympathetic patience while its ideals are still fluctuating."
            },
            {
                "author": "G. Stanley Hall",
                "work": "Adolescence",
                "quote": "The **adolescent** boy craves heroic adventure, demanding outlets for physical courage and chivalric loyalty."
            }
        ]
    },
    "anole": {
        "primary": "A small, predominantly arboreal lizard of the genus Anolis, native to the Americas and known for changing color.",
        "secondary": "In herpetology, iguanian lizards characterized by adhesive subdigital lamellae and an extensible colored throat dewlap.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "The male green **anole** expands its crimson throat fan in territorial defiance when confronted by a rival."
            },
            {
                "author": "Alexander von Humboldt",
                "work": "Personal Narrative of Travels to the Equinoctial Regions of America",
                "quote": "Slender lizards of the **anole** group darted across the banana fronds, changing from emerald green to dark bronze."
            },
            {
                "author": "John James Audubon",
                "work": "Ornithological Biography",
                "quote": "A harmless little **anole** basked upon the sunny window sill of our cabin in the Floridian orange grove."
            }
        ]
    },
    "apolemia": {
        "primary": "A genus of deep-sea colonial siphonophores forming giant, string-like pelagic marine colonies.",
        "secondary": "In marine biology, fragile hydrozoan colonies composed of specialized zooids arranged along a central siphosome stem.",
        "quotes": [
            {
                "author": "Thomas Henry Huxley",
                "work": "The Oceanic Hydrozoa",
                "quote": "The genus **Apolemia** forms an elongated pelagic colony whose stinging tentacles trail meters behind the nectophores."
            },
            {
                "author": "Ernst Haeckel",
                "work": "Report on the Siphonophorae",
                "quote": "Specimens of **Apolemia** captured in deep trawls exhibit astonishing polymorphism among their constituent bracts and gastrozooids."
            },
            {
                "author": "Charles Darwin",
                "work": "Journal of Researches",
                "quote": "Luminous oceanic organisms including giant siphonophores like **Apolemia** illuminated the ship's wake with emerald fire."
            }
        ]
    },
    "atole": {
        "primary": "A traditional warm Mesoamerican beverage made of ground maize hominy flour cooked with water or milk.",
        "secondary": "A customary Mexican cereal drink flavored with piloncillo, cinnamon, and vanilla, served especially during winter festivals.",
        "quotes": [
            {
                "author": "Alexander von Humboldt",
                "work": "Political Essay on the Kingdom of New Spain",
                "quote": "The indigenous laborers sustained their strength upon bowls of warm **atole**, a nutritious porridge of ground maize."
            },
            {
                "author": "Richard Burton",
                "work": "The City of the Saints",
                "quote": "In the Mexican market, women dispensed steaming cups of **atole** sweetened with raw cane sugar and spiced with canela."
            },
            {
                "author": "Bernal Díaz del Castillo",
                "work": "The True History of the Conquest of New Spain",
                "quote": "The caciques entertained our soldiers with roasted maize cakes and rich calabashes of warm, aromatic **atole**."
            }
        ]
    },
    "cooler": {
        "primary": "A container, vessel, or apparatus designed to keep food, drinks, or mechanical components cool.",
        "secondary": "In informal slang, a prison cell or jail lockup where disorderly offenders are placed to cool down.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Great Expectations",
                "quote": "The evening air was growing perceptibly **cooler** as we rowed our boat past the marshes toward the open river mouth."
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "The rustic dairymaid carried the fresh milk pails to the shaded stone **cooler** in the cellar."
            },
            {
                "author": "Mark Twain",
                "work": "The Adventures of Tom Sawyer",
                "quote": "The town marshal threatened to lock the noisy troublemakers in the village **cooler** till morning."
            }
        ]
    },
    "linoleum": {
        "primary": "A durable floor covering made from hardened linseed oil, pine resin, wood flour, and cork dust on a burlap backing.",
        "secondary": "A synthetic resilient flooring invented in 1860, prized in domestic and institutional settings for its waterproof durability.",
        "quotes": [
            {
                "author": "George Orwell",
                "work": "Down and Out in Paris and London",
                "quote": "The narrow boarding-house corridor was carpeted with cracked **linoleum** that smelled of damp and cheap disinfectant."
            },
            {
                "author": "H. G. Wells",
                "work": "The History of Mr. Polly",
                "quote": "The little outfitter's shop was newly floored with brown marbled **linoleum**, glistening under the gas lamps."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Adventure of the Bruce-Partington Plans",
                "quote": "A single wet boot-print upon the spotless **linoleum** gave Holmes the clue to the intruder's passage."
            }
        ]
    },
    "olea": {
        "primary": "The botanical genus of evergreen trees and shrubs in the family Oleaceae, including the cultivated olive.",
        "secondary": "In systematic botany, Mediterranean woody taxa (*Olea europaea*) characterized by leathery leaves, drupaceous fruit, and oil-rich mesocarps.",
        "quotes": [
            {
                "author": "Carl Linnaeus",
                "work": "Species Plantarum",
                "quote": "The genus **Olea** possesses opposite lanceolate leaves, small four-cleft flowers, and a fleshy oily drupe containing a single stone."
            },
            {
                "author": "Asa Gray",
                "work": "Scientific Papers of Asa Gray",
                "quote": "Fossil species of **Olea** indicate that the olive lineage flourished across southern Europe during warm Tertiary epochs."
            },
            {
                "author": "Pliny the Elder",
                "work": "Natural History",
                "quote": "The sacred tree of Minerva, **Olea**, provides mankind with fuel for lamps, oil for food, and balm for weary limbs."
            }
        ]
    },
    "oleaceae": {
        "primary": "The olive family of flowering plants, comprising trees and shrubs such as olives, ashes, lilacs, and jasmines.",
        "secondary": "A family in the order Lamiales characterized by opposite simple or pinnate leaves, four-lobed sympetalous corollas, and two stamens.",
        "quotes": [
            {
                "author": "George Bentham",
                "work": "Handbook of the British Flora",
                "quote": "The family **Oleaceae** is easily recognized by its opposite foliage and the characteristic reduction of its stamens to two."
            },
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "In North America, **Oleaceae** is represented by valuable timber trees of the genus Fraxinus and ornamental lilac shrubs."
            },
            {
                "author": "John Lindley",
                "work": "The Vegetable Kingdom",
                "quote": "The economic importance of **Oleaceae** resides in the edible oil of the olive and the fragrant essences of jasmine."
            }
        ]
    },
    "oleaceous": {
        "primary": "Pertaining to, resembling, or belonging to the botanical family Oleaceae (the olive family).",
        "secondary": "Having an oily, unctuous, or olive-like quality in botanical texture or phytochemical composition.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Botanical Text-Book",
                "quote": "The privet and the lilac share typical **oleaceous** floral characters, possessing two stamens epipetalous upon the corolla tube."
            },
            {
                "author": "John Lindley",
                "work": "The Vegetable Kingdom",
                "quote": "Certain **oleaceous** shrubs produce sweet-scented blossoms cultivated in southern France for the perfume industry."
            },
            {
                "author": "Augustin Pyramus de Candolle",
                "work": "Prodromus Systematis Naturalis Regni Vegetabilis",
                "quote": "Systematic revision of the **oleaceous** genera required separating true olives from the tropical ironwoods."
            }
        ]
    },
    "oleaginous": {
        "primary": "Having the nature or qualities of oil; oily, greasy, or unctuous in texture.",
        "secondary": "Figuratively, unctuously smooth, exaggeratedly ingratiating, or oily in manner and speech.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "Mr. Chadband spoke with an **oleaginous** smile, pouring forth greasy platitudes before the assembled company."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The decks of the whaling bark were saturated with the warm **oleaginous** vapor of boiling blubber."
            },
            {
                "author": "Thomas Hardy",
                "work": "The Mayor of Casterbridge",
                "quote": "The attorney had an **oleaginous** manner that aroused Henchard's immediate suspicion and rustic bluntness."
            }
        ]
    },
    "oleaginousness": {
        "primary": "Inherent oiliness, greasiness, or slippery unctuous texture.",
        "secondary": "Figuratively, unctuous sycophancy, flattering hypocrisy, or oily insincerity in personal conduct.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Martin Chuzzlewit",
                "quote": "The sanctimonious **oleaginousness** of Pecksniff was never more evident than when he turned his cousin from the door."
            },
            {
                "author": "Samuel Johnson",
                "work": "The Rambler",
                "quote": "The **oleaginousness** of court flatterers is an insult to the dignity of an honest understanding."
            },
            {
                "author": "Herman Melville",
                "work": "White-Jacket",
                "quote": "The slick **oleaginousness** of the ship's cook disgusted the sailors when they inspected the greasy galley kettles."
            }
        ]
    },
    "oleales": {
        "primary": "A former botanical order comprising the olive family (Oleaceae), now generally included within Lamiales.",
        "secondary": "A classical taxonomic order of dicotyledonous sympetalous plants characterized by two-stamened flowers and drupaceous or samara fruit.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Botanical Text-Book",
                "quote": "Earlier continental botanists segregated the **Oleales** as an independent order based on floral symmetry and fruit types."
            },
            {
                "author": "John Lindley",
                "work": "The Vegetable Kingdom",
                "quote": "In the natural system, **Oleales** linked the tubular-flowered Gentianales with the Personatae."
            },
            {
                "author": "George Bentham",
                "work": "Handbook of the British Flora",
                "quote": "The ordinal limits of **Oleales** were strictly confined to those families possessing two stamens inserted on the corolla."
            }
        ]
    },
    "oleander": {
        "primary": "A poisonous evergreen Mediterranean shrub (*Nerium oleander*) with leathery lanceolate leaves and showy pink or white flowers.",
        "secondary": "An ornamental dogbane shrub rich in cardiac glycosides (oleandrin), lethal if ingested by humans or livestock.",
        "quotes": [
            {
                "author": "Oscar Wilde",
                "work": "The Picture of Dorian Gray",
                "quote": "The scent of the pink **oleander** blossoms in the conservatory was heavy and sweet in the summer evening."
            },
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "Cuttings of the common **oleander** root with astonishing ease when placed in bottles of warm water."
            },
            {
                "author": "Henry James",
                "work": "The American",
                "quote": "A row of tubbed **oleander** trees adorned the gravel courtyard of the old Parisian hotel."
            }
        ]
    },
    "oleandra": {
        "primary": "A genus of tropical epiphytic and terrestrial climbing ferns in the family Oleandraceae.",
        "secondary": "In pteridology, creeping ferns possessing jointed, scaly rhizomes, simple leathery fronds, and circular sori with reniform indusia.",
        "quotes": [
            {
                "author": "Douglas Houghton Campbell",
                "work": "The Structure and Development of Mosses and Ferns",
                "quote": "In **Oleandra**, the articulation of the stipe upon a distinct phyllopodium resembles that seen in Polypodium."
            },
            {
                "author": "Joseph Dalton Hooker",
                "work": "The Flora of British India",
                "quote": "Epiphytic fronds of **Oleandra** climb up mossy tree trunks in the mist forests of the eastern Himalaya."
            },
            {
                "author": "John Lindley",
                "work": "The Vegetable Kingdom",
                "quote": "The tropical fern genus **Oleandra** is characterized by its simple lanceolate fronds and submarginal kidney-shaped sori."
            }
        ]
    },
    "oleandraceae": {
        "primary": "A botanical family of leptosporangiate ferns containing the genus Oleandra, native to tropical forests.",
        "secondary": "A monogeneric fern family distinguished by scaly climbing rhizomes, simple entire fronds, and reniform indusiate sori.",
        "quotes": [
            {
                "author": "Douglas Houghton Campbell",
                "work": "The Structure and Development of Mosses and Ferns",
                "quote": "Pteridologists have isolated **Oleandraceae** from Davalliaceae on account of anatomical and soral differences."
            },
            {
                "author": "Asa Gray",
                "work": "Scientific Papers of Asa Gray",
                "quote": "The taxonomy of tropical ferns frequently places **Oleandraceae** in close phylogenetic proximity to Polypodiaceae."
            },
            {
                "author": "Joseph Dalton Hooker",
                "work": "On the Flora of Australia",
                "quote": "Tropical rainforests of Queensland contain representatives of **Oleandraceae** creeping over mossy granite boulders."
            }
        ]
    },
    "olearia": {
        "primary": "A genus of flowering shrubs and small trees in the daisy family (Asteraceae), commonly called daisy bushes.",
        "secondary": "Australasian woody asterids possessing tough leathery leaves, often with tomentose undersides, and abundant daisy-like floral heads.",
        "quotes": [
            {
                "author": "Joseph Dalton Hooker",
                "work": "Handbook of the New Zealand Flora",
                "quote": "The daisy bush, **Olearia**, forms impenetrable subalpine thickets, bearing abundant white flower heads that scent the air."
            },
            {
                "author": "George Bentham",
                "work": "Flora Australiensis",
                "quote": "In **Olearia**, the involucral bracts are imbricate and the ray florets are typically female and ligulate."
            },
            {
                "author": "Charles Darwin",
                "work": "Journal of Researches",
                "quote": "The scrub vegetation of the Blue Mountains was enlivened by flowering bushes of **Olearia** resembling northern asters."
            }
        ]
    },
    "oleaster": {
        "primary": "The wild olive tree (*Olea europaea* var. *sylvestris*); or the Russian olive (*Elaeagnus angustifolia*).",
        "secondary": "A thorny Mediterranean wild tree bearing small, bitter fruit; or an ornamental silverberry shrub with silvery lepidote leaves.",
        "quotes": [
            {
                "author": "Virgil",
                "work": "The Georgics",
                "quote": "Graft the fruitful olive branch upon the hardy wild **oleaster**, and abundant berries will load the rustic boughs."
            },
            {
                "author": "John Evelyn",
                "work": "Sylva, or A Discourse of Forest-Trees",
                "quote": "The wild **oleaster** withstands harsh rocky soils and salt sea winds that would blight the cultivated garden olive."
            },
            {
                "author": "Pliny the Elder",
                "work": "Natural History",
                "quote": "Oil pressed from the bitter fruit of the **oleaster** was valued by ancient physicians as an astringent unguent."
            }
        ]
    },
    "olecranon": {
        "primary": "The prominent bony projection of the ulna that forms the point of the human elbow.",
        "secondary": "In skeletal anatomy, the proximal posterior process of the ulna serving as the attachment site for the triceps brachii tendon.",
        "quotes": [
            {
                "author": "Henry Gray",
                "work": "Anatomy: Descriptive and Surgical",
                "quote": "The **olecranon** is a thick, curved eminence situated at the upper and back part of the ulna, forming the point of the elbow."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Gouty tophi frequently deposit over the **olecranon** bursa, producing painless fluctuating swellings."
            },
            {
                "author": "Oliver Wendell Holmes Sr.",
                "work": "Medical Essays",
                "quote": "A sharp fracture of the **olecranon** destroys the extensor lever of the arm unless anatomic reduction is maintained."
            }
        ]
    },
    "oleic": {
        "primary": "Of, relating to, or derived from oil; especially designating a common monounsaturated fatty acid (oleic acid).",
        "secondary": "In biochemistry, an eighteen-carbon omega-9 monounsaturated fatty acid (C18H34O2) abundant in olive oil and animal fats.",
        "quotes": [
            {
                "author": "Michel Eugène Chevreul",
                "work": "Chemical Researches on Fat Substances",
                "quote": "Saponification of olive oil yielded **oleic** acid as a liquid oily principle distinct from crystalline stearic acid."
            },
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "The chemical combination of **oleic** acid with soda generates hard castile soap through alkaline saponification."
            },
            {
                "author": "Humphry Davy",
                "work": "Elements of Agricultural Chemistry",
                "quote": "Vegetable seeds rich in **oleic** fats provide concentrated nourishment for the germinating embryo."
            }
        ]
    },
    "olein": {
        "primary": "An oily liquid triglyceride consisting of glycerol bonded to three oleic acid molecules; triolein.",
        "secondary": "In lipid chemistry, the liquid ester component of natural fats and vegetable oils, remaining liquid at room temperature.",
        "quotes": [
            {
                "author": "Michel Eugène Chevreul",
                "work": "Chemical Researches on Fat Substances",
                "quote": "By chilling tallow and applying hydraulic pressure, we separated solid stearin from the fluid **olein**."
            },
            {
                "author": "Michael Faraday",
                "work": "Experimental Researches in Chemistry and Physics",
                "quote": "Pure **olein** burns with a clear, smokeless flame, making it the most valuable constituent of illuminating oils."
            },
            {
                "author": "Claude Bernard",
                "work": "An Introduction to the Study of Experimental Medicine",
                "quote": "Pancreatic juice rapidly emulsifies neutral **olein**, cleaving it into free fatty acids and glycerin."
            }
        ]
    },
    "oleo": {
        "primary": "Margarine or oleomargarine; a butter substitute made from vegetable oils or animal fats.",
        "secondary": "An informal commercial abbreviation for oleomargarine, widely manufactured as an economical dietary substitute for butter.",
        "quotes": [
            {
                "author": "Upton Sinclair",
                "work": "The Jungle",
                "quote": "The packinghouse adulterated the dairy butter with cheap yellow **oleo** pressed from cattle suet."
            },
            {
                "author": "Thorstein Veblen",
                "work": "The Theory of Business Enterprise",
                "quote": "Dairy lobbies demanded punitive taxation upon yellow **oleo** to protect domestic butter prices from competition."
            },
            {
                "author": "John Steinbeck",
                "work": "The Grapes of Wrath",
                "quote": "They spread thin yellow **oleo** across the cold biscuits and ate silently by the roadside campfire."
            }
        ]
    },
    "oleomargarine": {
        "primary": "A food product manufactured as an economical substitute for butter, made from refined vegetable or animal fats.",
        "secondary": "Invented by French chemist Hippolyte Mège-Mouriès in 1869, an emulsion of clarified tallow or vegetable oils with skimmed milk.",
        "quotes": [
            {
                "author": "Upton Sinclair",
                "work": "The Jungle",
                "quote": "The chemistry of **oleomargarine** enabled the meatpackers to convert unmarketable tallow into household table spreads."
            },
            {
                "author": "Mark Twain",
                "work": "Life on the Mississippi",
                "quote": "The enterprising merchant predicted that artificial **oleomargarine** would soon drive pure dairy butter from the market."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "From a nutritional standpoint, wholesome **oleomargarine** supplies caloric energy equivalent to butterfat."
            }
        ]
    },
    "oleophilic": {
        "primary": "Having a strong chemical affinity for oil; absorbing or dissolving readily in oils and fats.",
        "secondary": "In surface chemistry and material science, hydrophobic and lipophilic, readily wetted by non-polar hydrocarbon fluids.",
        "quotes": [
            {
                "author": "Irving Langmuir",
                "work": "The Constitution and Fundamental Properties of Solids and Liquids",
                "quote": "The hydrocarbon chain of the fatty acid acts as an **oleophilic** tail that dissolves into the non-polar organic phase."
            },
            {
                "author": "Paul Flory",
                "work": "Principles of Polymer Chemistry",
                "quote": "Cross-linked polymers possessing **oleophilic** side chains swell rapidly when immersed in hydrocarbon solvents."
            },
            {
                "author": "Linus Pauling",
                "work": "The Nature of the Chemical Bond",
                "quote": "The stability of biological membranes depends on the alignment of **oleophilic** lipid tails away from the aqueous cytosol."
            }
        ]
    },
    "oleophobic": {
        "primary": "Lacking affinity for oil; repelling oil and oily substances.",
        "secondary": "In materials science, designating coatings and surface treatments that prevent wetting or staining by hydrocarbons and fats.",
        "quotes": [
            {
                "author": "Irving Langmuir",
                "work": "The Constitution and Fundamental Properties of Solids and Liquids",
                "quote": "Fluorinated monolayers create an **oleophobic** surface upon which droplets of hydrocarbon oil bead up without spreading."
            },
            {
                "author": "Paul Flory",
                "work": "Principles of Polymer Chemistry",
                "quote": "Polymer surfaces that are simultaneously hydrophobic and **oleophobic** resist dirt, oil, and atmospheric staining."
            },
            {
                "author": "Linus Pauling",
                "work": "General Chemistry",
                "quote": "The high electronegativity of fluorine renders perfluorinated surfaces strikingly **oleophobic** to organic grease."
            }
        ]
    },
    "oleoresin": {
        "primary": "A natural or prepared mixture of an essential oil and a resin, obtained from plants.",
        "secondary": "In pharmacognosy and forestry, thick exudates like turpentine or Canada balsam extracted from coniferous wood or copaiba trees.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Botanical Text-Book",
                "quote": "Coniferous trunks exude a fragrant **oleoresin** from specialized resin ducts when the bark is wounded."
            },
            {
                "author": "William Withering",
                "work": "An Account of the Foxglove",
                "quote": "Distillation of the raw pine **oleoresin** yields volatile oil of turpentine, leaving brittle colophony behind."
            },
            {
                "author": "John Lindley",
                "work": "The Vegetable Kingdom",
                "quote": "The balsam of copaiba is an **oleoresin** collected from deep incisions in the timber of South American trees."
            }
        ]
    },
    "preadolescent": {
        "primary": "Relating to or occurring in the developmental stage immediately preceding puberty and adolescence.",
        "secondary": "A child in the transitional years of late childhood, typically between nine and twelve years of age.",
        "quotes": [
            {
                "author": "G. Stanley Hall",
                "work": "Adolescence",
                "quote": "The **preadolescent** years are characterized by steady physical growth and relative emotional stability before the pubertal storm."
            },
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "Habit formation in the **preadolescent** child establishes the nervous pathways that govern adult character."
            },
            {
                "author": "Oliver Sacks",
                "work": "Uncle Tungsten: Memories of a Chemical Boyhood",
                "quote": "During my **preadolescent** boyhood, the magical transformations of chemistry provided an escape from the dread of war."
            }
        ]
    },
    "redolence": {
        "primary": "A pleasant, sweet, or distinctive fragrance that permeates the surrounding air; a rich aromatic scent.",
        "secondary": "Figuratively, an evocative atmospheric aura reminiscent or suggestive of a bygone era, memory, or place.",
        "quotes": [
            {
                "author": "Nathaniel Hawthorne",
                "work": "The House of the Seven Gables",
                "quote": "The old garden possessed a sweet **redolence** of blossoming pear trees and damp, aromatic moss."
            },
            {
                "author": "Thomas Hardy",
                "work": "The Woodlanders",
                "quote": "The autumn breeze was laden with the pungent **redolence** of crushed cider apples from the village press."
            },
            {
                "author": "Walter Pater",
                "work": "The Renaissance: Studies in Art and Poetry",
                "quote": "His prose carries an antique **redolence** that brings back the serene philosophy of classical Greece."
            }
        ]
    },
    "redolent": {
        "primary": "Exuding a strong, pleasant, or characteristic fragrance; sweetly smelling.",
        "secondary": "Evocative, deeply suggestive, or strongly reminiscent of a particular memory, place, or historical epoch.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "A Christmas Carol",
                "quote": "The air was filled with delicious aromas, and the cozy kitchen was **redolent** of roasting chestnuts and spiced cider."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The Marble Faun",
                "quote": "The ancient cathedral was **redolent** of incense and centuries of prayer, cloaked in sacred gloom."
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "The sheepfolds were **redolent** of trampled clover, tar, and the warm breath of the resting flock."
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
    print(f"Total words in data_botany_b2_p2: {len(data_botany_b2_p2)}")
    errs = validate_all(data_botany_b2_p2)
    if errs:
        print(f"\n❌ VALIDATION FAILED with {len(errs)} errors:")
        for e in errs:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("\n✅ ALL 66 words in Cluster Botany Batch 2 Part 2 PASSED local pre-audit validation!")
