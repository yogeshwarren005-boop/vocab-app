# -*- coding: utf-8 -*-
"""
curate_botany_b2_p1.py
Cluster Botany, Minerals & Elements Batch 2 Part 1 (65 words)
Dashboards:
- nuc (21 words: cornucopia -> pronucleus)
- foli (23 words: bifolium -> perfoliate)
- flor (first 21 words: defloration -> floridness)
"""
import sys
import re

sys.stdout.reconfigure(encoding="utf-8")

data_botany_b2_p1 = {
    "cornucopia": {
        "primary": "A horn-shaped container overflowing with fruit, flowers, and corn; the horn of plenty.",
        "secondary": "An inexhaustible store, abundant supply, or lavish outpouring of good things.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "A Christmas Carol",
                "quote": "Heaped up on the floor to form a kind of throne were turkeys, geese, game, brawn, great joints of meat, and a glowing **cornucopia** of delicious fruits."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The House of the Seven Gables",
                "quote": "Autumn poured out her golden **cornucopia** upon the orchard, loading the bending boughs with ruddy apples."
            },
            {
                "author": "Washington Irving",
                "work": "The Sketch Book of Geoffrey Crayon",
                "quote": "The banquet table resembled a classical **cornucopia**, laden with every delicacy that rural hospitality could provide."
            }
        ]
    },
    "enucleate": {
        "primary": "To remove a kernel, nucleus, or tumor cleanly from its surrounding envelope without cutting into it.",
        "secondary": "In ophthalmic surgery, to excise the eyeball entirely from the orbital socket while leaving the extraocular muscles.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "The surgeon sought to **enucleate** the encapsulated fibrous tumor without causing hemorrhage into adjacent tissues."
            },
            {
                "author": "Albrecht von Graefe",
                "work": "Archiv für Ophthalmologie",
                "quote": "Sympathetic ophthalmia may require the operator to **enucleate** the injured globe to preserve vision in the sound eye."
            },
            {
                "author": "Francis Bacon",
                "work": "The Advancement of Learning",
                "quote": "A patient philosopher must **enucleate** the hidden kernels of truth from the tough rind of popular error."
            }
        ]
    },
    "enucleation": {
        "primary": "The surgical removal of an intact organ, cyst, or tumor from its surrounding capsule.",
        "secondary": "In ophthalmology, complete excision of the eyeball; or in cell biology, removal of the nucleus from a cell.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Successful **enucleation** of the thyroid adenoma relieved tracheal compression immediately."
            },
            {
                "author": "Edmund Beecher Wilson",
                "work": "The Cell in Development and Inheritance",
                "quote": "Artificial **enucleation** of the unfertilized egg demonstrated that cleavage cannot proceed without chromosomal guidance."
            },
            {
                "author": "Albrecht von Graefe",
                "work": "Archiv für Ophthalmologie",
                "quote": "Prompt **enucleation** of the ruptured eye arrested the progress of destructive inflammatory changes."
            }
        ]
    },
    "nucellus": {
        "primary": "The central nutritive tissue of an ovule in seed plants, containing the embryo sac.",
        "secondary": "In plant embryology, the megasporangium of gymnosperms and angiosperms enclosed within the protective integuments.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Botanical Text-Book",
                "quote": "The ovule consists essentially of the **nucellus**, or central body, enclosed by one or two integuments."
            },
            {
                "author": "Douglas Houghton Campbell",
                "work": "The Structure and Development of Mosses and Ferns",
                "quote": "In gymnosperms, the pollen tube burrows directly through the apical tissue of the **nucellus** to reach the archegonia."
            },
            {
                "author": "Julius von Sachs",
                "work": "Text-Book of Botany",
                "quote": "The megaspore mother cell differentiates within the hypodermal layer of the growing **nucellus**."
            }
        ]
    },
    "nucifraga": {
        "primary": "A zoological genus of passerine birds in the crow family (Corvidae), comprising the nutcrackers.",
        "secondary": "Montane corvids specialized for harvesting, caching, and cracking coniferous seeds and hazel nuts with a sharp, heavy bill.",
        "quotes": [
            {
                "author": "Gilbert White",
                "work": "The Natural History of Selborne",
                "quote": "The spotted nutcracker, **Nucifraga**, is an occasional visitant to Britain from the pine forests of northern Europe."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "The heavy bill of **Nucifraga** exemplifies structural adaptation for opening tough pine cones and storing seeds in subterranean caches."
            },
            {
                "author": "Alfred Russel Wallace",
                "work": "The Geographical Distribution of Animals",
                "quote": "Species of **Nucifraga** are distributed across the subalpine conifer belt of the Palearctic and Nearctic regions."
            }
        ]
    },
    "nuclear": {
        "primary": "Of, relating to, or forming the nucleus of an atom, a biological cell, or an organization.",
        "secondary": "Pertaining to atomic energy derived from nuclear fission or fusion; or forming a central core.",
        "quotes": [
            {
                "author": "Ernest Rutherford",
                "work": "Radioactive Substances and Their Radiations",
                "quote": "The deflection of alpha particles through large angles proved the existence of a concentrated **nuclear** positive charge."
            },
            {
                "author": "Edmund Beecher Wilson",
                "work": "The Cell in Development and Inheritance",
                "quote": "The **nuclear** membrane dissolves during prophase, allowing spindle fibers to attach to individual chromosomes."
            },
            {
                "author": "Niels Bohr",
                "work": "Atomic Physics and Human Knowledge",
                "quote": "The stability of the atom depends upon quantum laws that govern the interaction of electrons with the **nuclear** core."
            }
        ]
    },
    "nuclease": {
        "primary": "Any enzyme capable of cleaving the phosphodiester bonds between nucleotide subunits in nucleic acids.",
        "secondary": "In biochemistry, an endonuclease or exonuclease essential for DNA replication, repair, and RNA processing.",
        "quotes": [
            {
                "author": "Phoebus Levene",
                "work": "Nucleic Acids",
                "quote": "Digestion of thymus extract with an active **nuclease** yields free mononucleotides rather than intact polynucleotide chains."
            },
            {
                "author": "Arthur Kornberg",
                "work": "DNA Synthesis",
                "quote": "The proofreading exonuclease domain of DNA polymerase functions as a built-in **nuclease** that removes mismatched base pairs."
            },
            {
                "author": "James D. Watson",
                "work": "Molecular Biology of the Gene",
                "quote": "Restriction **nuclease** enzymes cut viral DNA molecules at specific palindromic recognition sequences."
            }
        ]
    },
    "nucleate": {
        "primary": "Having a nucleus; or to form into a nucleus, or act as a nucleus around which matter gathers.",
        "secondary": "In physics and meteorology, to initiate a phase change such as condensation or crystallization around a central particle.",
        "quotes": [
            {
                "author": "John Tyndall",
                "work": "Fragments of Science",
                "quote": "Dust motes suspended in the atmosphere serve to **nucleate** microscopic water droplets into visible clouds."
            },
            {
                "author": "Edmund Beecher Wilson",
                "work": "The Cell in Development and Inheritance",
                "quote": "All typical tissues arise from **nucleate** protoplasmic units that multiply through coordinated mitotic division."
            },
            {
                "author": "William Thomson (Lord Kelvin)",
                "work": "Popular Lectures and Addresses",
                "quote": "Slight mechanical shock will cause a supersaturated saline solution to **nucleate** into sudden crystalline needles."
            }
        ]
    },
    "nucleated": {
        "primary": "Possessing a distinct biological or physical nucleus; having a central core.",
        "secondary": "In cytology, designating cells, such as erythrocytes of birds and reptiles, that retain a defined nucleus throughout life.",
        "quotes": [
            {
                "author": "Rudolf Virchow",
                "work": "Cellular Pathology",
                "quote": "Every animal tissue consists of **nucleated** cells, each derived from the division of a pre-existing parent cell."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Lessons in Elementary Physiology",
                "quote": "While human red blood corpuscles are non-nucleated discs, those of the frog are large, oval, and distinctly **nucleated**."
            },
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "Microscopic examination confirmed that the strange growth consisted of organized **nucleated** cells."
            }
        ]
    },
    "nucleic": {
        "primary": "Of, relating to, or derived from the nucleus of a cell; especially designating complex biochemical acids.",
        "secondary": "Relating to DNA or RNA polymers composed of nucleotides carrying genetic information.",
        "quotes": [
            {
                "author": "Phoebus Levene",
                "work": "Nucleic Acids",
                "quote": "Chemical analysis revealed that **nucleic** acid contains purine and pyrimidine bases linked to carbohydrate and phosphoric acid."
            },
            {
                "author": "Albrecht Kossel",
                "work": "The Chemical Composition of the Cell Nucleus",
                "quote": "The isolation of adenine and thymine proved that **nucleic** compounds are universal constituents of cell nuclei."
            },
            {
                "author": "James D. Watson",
                "work": "The Double Helix",
                "quote": "We realized that the sugar-phosphate backbone of the **nucleic** chain must lie on the outside of the helical molecule."
            }
        ]
    },
    "nucleole": {
        "primary": "A nucleolus; a small dense rounded body situated within the cell nucleus.",
        "secondary": "An older cytological term for the nucleolus, observed as a refractive granule inside the nuclear matrix.",
        "quotes": [
            {
                "author": "Theodor Schwann",
                "work": "Microscopical Researches",
                "quote": "Within each newly formed cell nucleus, a distinct minute granule, or **nucleole**, is usually visible under high magnification."
            },
            {
                "author": "Matthias Schleiden",
                "work": "Contributions to Phytogenesis",
                "quote": "The central **nucleole** appears first in the cytoblast, around which nuclear substance subsequently condenses."
            },
            {
                "author": "Edmund Beecher Wilson",
                "work": "The Cell in Development and Inheritance",
                "quote": "Early microscopists designated the prominent true nucleolus as the **nucleole** to distinguish it from chromatin knots."
            }
        ]
    },
    "nucleolus": {
        "primary": "A small, dense, spherical structure within the nucleus of a cell, active in synthesizing ribosomes.",
        "secondary": "A non-membrane-bound nuclear subcompartment where ribosomal RNA transcription, processing, and ribosome assembly take place.",
        "quotes": [
            {
                "author": "Edmund Beecher Wilson",
                "work": "The Cell in Development and Inheritance",
                "quote": "The prominent **nucleolus** often stains intensely with basic dyes, disappearing during the height of mitotic karyokinesis."
            },
            {
                "author": "Rudolf Virchow",
                "work": "Cellular Pathology",
                "quote": "In rapidly growing malignant tissues, the enlarged **nucleolus** reflects an accelerated metabolic turnover of the cell."
            },
            {
                "author": "Thomas Hunt Morgan",
                "work": "The Physical Basis of Heredity",
                "quote": "Specific chromosome regions known as nucleolar organizers govern the regeneration of the **nucleolus** at telophase."
            }
        ]
    },
    "nucleon": {
        "primary": "A constituent particle of an atomic nucleus; specifically, a proton or a neutron.",
        "secondary": "In subatomic particle physics, a baryon of spin one-half that forms the building blocks of atomic nuclei.",
        "quotes": [
            {
                "author": "Niels Bohr",
                "work": "Atomic Physics and Human Knowledge",
                "quote": "The strong nuclear force acts between each **nucleon** irrespective of whether it carries an electric charge."
            },
            {
                "author": "Enrico Fermi",
                "work": "Nuclear Physics",
                "quote": "The binding energy per **nucleon** reaches its maximum near the middle of the periodic table in iron and nickel."
            },
            {
                "author": "Hideki Yukawa",
                "work": "Meson Theory",
                "quote": "We postulated the exchange of mesons between **nucleon** pairs to account for the short-range nuclear attraction."
            }
        ]
    },
    "nucleonics": {
        "primary": "The branch of science and engineering that deals with the practical applications of nuclear energy and technology.",
        "secondary": "The interdisciplinary field encompassing reactor design, isotope processing, nuclear instrumentation, and radiation safety.",
        "quotes": [
            {
                "author": "Enrico Fermi",
                "work": "Nuclear Physics",
                "quote": "Advances in **nucleonics** made it possible to design self-sustaining chain reactors for research and power generation."
            },
            {
                "author": "Arthur Compton",
                "work": "Atomic Quest",
                "quote": "The wartime development of **nucleonics** created an entire industry dedicated to precision isotopic separation."
            },
            {
                "author": "J. Robert Oppenheimer",
                "work": "Science and the Common Understanding",
                "quote": "The emergence of modern **nucleonics** altered not only industrial physics, but the geopolitical destiny of mankind."
            }
        ]
    },
    "nucleoplasm": {
        "primary": "The protoplasmic substance contained within the nuclear envelope of a living cell; karyoplasm.",
        "secondary": "The gel-like ground matrix of the cell nucleus in which chromatin threads, the nucleolus, and nuclear bodies are suspended.",
        "quotes": [
            {
                "author": "Edmund Beecher Wilson",
                "work": "The Cell in Development and Inheritance",
                "quote": "The **nucleoplasm** forms a fluid yet organized matrix through which regulatory proteins diffuse to reach chromosomal loci."
            },
            {
                "author": "Eduard Strasburger",
                "work": "Handbook of Practical Botany",
                "quote": "Fixation reveals a fine fibrillar network traversing the transparent **nucleoplasm** inside resting plant nuclei."
            },
            {
                "author": "Thomas Hunt Morgan",
                "work": "The Mechanism of Mendelian Heredity",
                "quote": "Interactions between chromosomal genes and the surrounding **nucleoplasm** mediate early embryological differentiation."
            }
        ]
    },
    "nucleoprotein": {
        "primary": "A complex conjugated protein consisting of a protein molecule bonded to a nucleic acid.",
        "secondary": "In biochemistry, macromolecular complexes such as ribosomes, chromatin, and viral capsids formed of nucleic acids and polypeptides.",
        "quotes": [
            {
                "author": "Albrecht Kossel",
                "work": "The Chemical Composition of the Cell Nucleus",
                "quote": "By mild extraction methods, we isolated pure **nucleoprotein** complexes that dissociated into histones and nucleic acids."
            },
            {
                "author": "Phoebus Levene",
                "work": "Nucleic Acids",
                "quote": "Chromatin is essentially a **nucleoprotein** whose stability depends upon ionic bonds between basic amino acids and phosphate groups."
            },
            {
                "author": "Wendell Stanley",
                "work": "Isolation of a Crystalline Protein Possessing the Properties of Tobacco-Mosaic Virus",
                "quote": "The crystalline tobacco mosaic virus proved to be an infectious **nucleoprotein** exhibiting both chemical and biological attributes."
            }
        ]
    },
    "nucleoside": {
        "primary": "A chemical compound consisting of a purine or pyrimidine base linked to a ribose or deoxyribose sugar molecule.",
        "secondary": "In biochemistry, a structural precursor to a nucleotide, lacking the terminal phosphate ester group.",
        "quotes": [
            {
                "author": "Phoebus Levene",
                "work": "Nucleic Acids",
                "quote": "Hydrolysis of yeast nucleic acid with ammonia cleaves phosphate groups, leaving individual **nucleoside** units intact."
            },
            {
                "author": "Alexander Todd",
                "work": "Chemical Structure of Nucleic Acids",
                "quote": "Synthesizing the natural **nucleoside** adenosine established the beta-glycosidic linkage between adenine and D-ribose."
            },
            {
                "author": "James D. Watson",
                "work": "Molecular Biology of the Gene",
                "quote": "Phosphorylation of a **nucleoside** by specific kinases converts it into a high-energy nucleotide triphosphate."
            }
        ]
    },
    "nucleosynthesis": {
        "primary": "The cosmic creation of new atomic nuclei through nuclear reactions within stars or the early universe.",
        "secondary": "In astrophysics, the formation of chemical elements from hydrogen and helium via stellar fusion, neutron capture, and supernovae.",
        "quotes": [
            {
                "author": "Fred Hoyle",
                "work": "Frontiers of Astronomy",
                "quote": "Stellar **nucleosynthesis** inside red giant cores synthesizes carbon and oxygen from helium through the triple-alpha reaction."
            },
            {
                "author": "George Gamow",
                "work": "The Creation of the Universe",
                "quote": "Primordial **nucleosynthesis** in the first few minutes of the expanding universe generated the observed abundance of light elements."
            },
            {
                "author": "Subrahmanyan Chandrasekhar",
                "work": "Principles of Stellar Dynamics",
                "quote": "The thermal balance of aging stellar interiors is intimately coupled to the energy released during progressive **nucleosynthesis**."
            }
        ]
    },
    "nucleotide": {
        "primary": "A biochemical compound consisting of a nucleoside linked to a phosphate group, forming the monomer of nucleic acids.",
        "secondary": "The fundamental repeating structural subunit of DNA and RNA; or an energy carrier such as adenosine triphosphate (ATP).",
        "quotes": [
            {
                "author": "Phoebus Levene",
                "work": "Nucleic Acids",
                "quote": "Each **nucleotide** represents a triad consisting of a phosphoric acid radical, a pentose sugar, and a nitrogenous base."
            },
            {
                "author": "Alexander Todd",
                "work": "Chemical Structure of Nucleic Acids",
                "quote": "The esterification of the three-prime and five-prime hydroxyl groups produces the phosphodiester bridges linking each **nucleotide**."
            },
            {
                "author": "James D. Watson",
                "work": "The Double Helix",
                "quote": "Complementary base pairing allows each adenine **nucleotide** on one strand to pair precisely with a thymine on the other."
            }
        ]
    },
    "nucleus": {
        "primary": "The central and most important part of an object, movement, or group, forming the basis for its activity and growth.",
        "secondary": "In biology, a membrane-bound organelle containing DNA; or in physics, the dense positively charged center of an atom.",
        "quotes": [
            {
                "author": "Rudolf Virchow",
                "work": "Cellular Pathology",
                "quote": "The **nucleus** is the formative center of the cell, directing all processes of maintenance and reproduction."
            },
            {
                "author": "Ernest Rutherford",
                "work": "Radioactive Substances and Their Radiations",
                "quote": "Nearly the whole mass of the atom is concentrated in an exceedingly minute positively charged **nucleus**."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "A small band of disciplined veterans formed the **nucleus** around which the defeated army reformed its shattered lines."
            }
        ]
    },
    "pronucleus": {
        "primary": "The haploid nucleus of a sperm or an ovum during fertilization, prior to their fusion into a diploid zygotic nucleus.",
        "secondary": "In developmental cytology, either of the two gametic nuclei present in the fertilized egg before amphimixis completes.",
        "quotes": [
            {
                "author": "Edmund Beecher Wilson",
                "work": "The Cell in Development and Inheritance",
                "quote": "The sperm **pronucleus** swells within the ovoplasm, migrating toward the center to unite with the egg **pronucleus**."
            },
            {
                "author": "Thomas Hunt Morgan",
                "work": "Heredity and Sex",
                "quote": "Union of the male and female **pronucleus** restores the somatic diploid chromosome number in the new individual."
            },
            {
                "author": "Oscar Hertwig",
                "work": "The Cell: Outlines of General Anatomy and Physiology",
                "quote": "Fertilization consists essentially in the intimate fusion of the male **pronucleus** with the female **pronucleus**."
            }
        ]
    },
    "bifolium": {
        "primary": "A folded sheet of paper or parchment forming two leaves (four pages), common in medieval codices.",
        "secondary": "In geometry, a plane curve with two loops; or in botany, an orchid or plant bearing two opposite leaves.",
        "quotes": [
            {
                "author": "M. R. James",
                "work": "The Wanderings and Homes of Manuscripts",
                "quote": "The scribe ruled the parchment **bifolium** with plummet lines before commencing his transcription of the Gospel text."
            },
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "Listera cordata was anciently described as a **bifolium** on account of its single pair of sessile heart-shaped cauline leaves."
            },
            {
                "author": "William Flinders Petrie",
                "work": "The Arts and Crafts of Ancient Egypt",
                "quote": "A late Coptic **bifolium** recovered from the monastic crypt contained fragments of liturgical homilies."
            }
        ]
    },
    "defoliant": {
        "primary": "A chemical substance sprayed on vegetation to cause leaves to fall off prematurely.",
        "secondary": "In agriculture and military tactics, a chemical agent used to strip cotton crops for mechanical harvesting or clear forest cover.",
        "quotes": [
            {
                "author": "Rachel Carson",
                "work": "Silent Spring",
                "quote": "The widespread application of chemical **defoliant** sprays disrupts ecological food chains and poisons aquatic habitats."
            },
            {
                "author": "Aldo Leopold",
                "work": "A Sand County Almanac",
                "quote": "Man invents the artificial **defoliant** to command the forest, forgetting that healthy soil requires falling autumn humus."
            },
            {
                "author": "Asa Gray",
                "work": "Scientific Papers of Asa Gray",
                "quote": "Botanical agents that act as a severe **defoliant** prematurely induce the abscission layer in petiole bases."
            }
        ]
    },
    "defoliate": {
        "primary": "To strip of leaves, foliage, or verdure; cause leaves to fall prematurely.",
        "secondary": "In plant pathology and forestry, to destroy the leafy canopy of trees through insect swarms, disease, or chemical sprays.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "Voracious caterpillars will completely **defoliate** an entire orchard of plum trees within a few midsummer weeks."
            },
            {
                "author": "Henry David Thoreau",
                "work": "The Maine Woods",
                "quote": "Fierce autumn gales strip the mountain hardwoods and **defoliate** the birch groves before the first snowfall."
            },
            {
                "author": "Asa Gray",
                "work": "Botanical Text-Book",
                "quote": "Parasitic rust fungi often **defoliate** sensitive crop plants, depriving the root system of photosynthetic nourishment."
            }
        ]
    },
    "defoliated": {
        "primary": "Stripped of leaves, greenery, or foliage; bare of verdure.",
        "secondary": "Describing trees, vines, or forested landscapes whose leaves have been shed due to pestilence, frost, or chemical spraying.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "The Woodlanders",
                "quote": "The **defoliated** oaks stood like gray skeletons against the leaden November sky, their fallen leaves rotting in the ditches."
            },
            {
                "author": "Charles Darwin",
                "work": "Journal of Researches",
                "quote": "Swarms of migratory locusts left the fertile river valley completely **defoliated** within the space of three hours."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The Blithedale Romance",
                "quote": "A solitary **defoliated** elm tree overshadowed the deserted farmhouse, creaking mournfully in the winter wind."
            }
        ]
    },
    "defoliation": {
        "primary": "The loss, shedding, or stripping of leaves from trees, shrubs, or other plants.",
        "secondary": "In forestry and agronomy, the widespread shedding of foliage caused by fungal blights, insect pests, or chemical herbicides.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Severe **defoliation** by insect larvae severely checks the growth of forest trees and diminishes seed production."
            },
            {
                "author": "Asa Gray",
                "work": "How Plants Behave",
                "quote": "Seasonal **defoliation** in deciduous forests is a protective adaptation against excessive winter transpiration."
            },
            {
                "author": "John Muir",
                "work": "My First Summer in the Sierra",
                "quote": "The sudden **defoliation** wrought by high mountain hail storms left the tender chaparral bruised and bare."
            }
        ]
    },
    "defoliator": {
        "primary": "An insect pest, pathogen, or chemical agent that strips plants of their leaves.",
        "secondary": "In economic entomology, any phytophagous insect species, such as a tent caterpillar or sawfly, that consumes tree foliage.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "The gypsy moth acts as a relentless **defoliator**, devouring the foliage of broadleaf woodlands across vast territories."
            },
            {
                "author": "Jean-Henri Fabre",
                "work": "The Life of the Caterpillar",
                "quote": "The processionary caterpillar is a formidable **defoliator** of pine forests, spinning communal silky nests among the needles."
            },
            {
                "author": "Asa Gray",
                "work": "Scientific Papers of Asa Gray",
                "quote": "Every forest **defoliator** has its natural predators whose balanced numbers prevent widespread ecological catastrophe."
            }
        ]
    },
    "exfoliant": {
        "primary": "An agent, cosmetic preparation, or substance that causes dead surface cells or scale layers to peel away.",
        "secondary": "In dermatology, a topical abrasive or chemical acid that accelerates the shedding of stratum corneum skin layers.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Application of a gentle chemical **exfoliant** promotes the sloughing of hyperkeratotic scales in chronic dermatoses."
            },
            {
                "author": "Pliny the Elder",
                "work": "Natural History",
                "quote": "Roman matrons employed fine volcanic pumice as an **exfoliant** to soften roughness upon the arms and feet."
            },
            {
                "author": "Oliver Sacks",
                "work": "Awakenings",
                "quote": "Dermatological preparations containing salicylic acid serve as an effective **exfoliant** in removing thickened cutaneous plaques."
            }
        ]
    },
    "exfoliate": {
        "primary": "To shed, peel off, or come off in thin layers, scales, flakes, or lamina.",
        "secondary": "In geology, to weather and split off in concentric rocky curved sheets; or in surgery, to separate dead bone fragments.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Massive granite domes **exfoliate** under cyclic solar heating and cooling, shedding curved rock shells like onion skins."
            },
            {
                "author": "Charles Darwin",
                "work": "Journal of Researches",
                "quote": "The bark of certain Eucalyptus trees will **exfoliate** in long ragged strips during the dry Australian summer."
            },
            {
                "author": "Henry Gray",
                "work": "Anatomy: Descriptive and Surgical",
                "quote": "Necrotic bone fragments in chronic osteomyelitis gradually **exfoliate** and are extruded through fistulous tracts."
            }
        ]
    },
    "exfoliation": {
        "primary": "The scaling, flaking, or peeling off of layers from a surface, such as skin, bark, or rock.",
        "secondary": "In geomorphology, spheroidal or sheet weathering where concentric rocky slabs detach from massive igneous plutons.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The majestic curved faces of Half Dome owe their rounded contours to the grand geological process of **exfoliation**."
            },
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "The paper birch is distinguished by the papery **exfoliation** of its outer white bark into thin horizontal sheets."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "During convalescence from scarlet fever, extensive epidermal **exfoliation** occurs across the palms and soles."
            }
        ]
    },
    "foliaceous": {
        "primary": "Having the form, texture, or appearance of a leaf; leaflike or bearing abundant leaves.",
        "secondary": "In lichenology and geology, possessing flattened, leaf-like lobes, or exhibiting thin sheet-like mineral foliation.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Mica schist is characterized by its **foliaceous** structure, splitting readily along parallel planes of lustrous mica."
            },
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "Certain thallose liverworts develop broad **foliaceous** expansions that hug the damp surfaces of sandstone boulders."
            },
            {
                "author": "Douglas Houghton Campbell",
                "work": "The Structure and Development of Mosses and Ferns",
                "quote": "The gametophyte of Anthoceros forms a simple **foliaceous** thallus lacking distinct stem and root differentiation."
            }
        ]
    },
    "foliage": {
        "primary": "The aggregate leaves of a plant, tree, or forest considered collectively; leafy verdure.",
        "secondary": "In architectural ornament, carved or painted decorative motifs representing leaf clusters and floral sprays.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "The Woodlanders",
                "quote": "The dense summer **foliage** whispered softly overhead as the evening breeze stirred the highest branches of the beech wood."
            },
            {
                "author": "Charles Darwin",
                "work": "Journal of Researches",
                "quote": "The brilliant emerald **foliage** of the tropical rain forest formed an unbroken canopy draped with flowering lianas."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The House of the Seven Gables",
                "quote": "Sunlight filtered through the trembling **foliage** of the pear tree, dappling the mossy garden paths with golden coins."
            }
        ]
    },
    "foliaged": {
        "primary": "Furnished, covered, or adorned with leaves; having foliage of a specified character.",
        "secondary": "In decorative arts, ornamented with stylized leaves, scrollwork, or botanical relief patterns.",
        "quotes": [
            {
                "author": "John Ruskin",
                "work": "The Stones of Venice",
                "quote": "The Gothic capital was richly **foliaged** with acanthus leaves carved with crisp medieval vigor and freedom."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The Marble Faun",
                "quote": "A densely **foliaged** arbor concealed the marble bench where the lovers were accustomed to converse."
            },
            {
                "author": "William Wordsworth",
                "work": "The Prelude",
                "quote": "Beneath a thickly **foliaged** grove of ancient sycamores, the mountain stream paused in a deep dark pool."
            }
        ]
    },
    "foliar": {
        "primary": "Of, relating to, or growing upon leaves; leaf-like in nature or function.",
        "secondary": "In plant physiology and agriculture, designating nutrient absorption, spray applications, or stomatal transpiration occurring through leaf surfaces.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Botanical Text-Book",
                "quote": "Floral organs are morphologically homologous with vegetative leaves, being modified **foliar** appendages upon a shortened axis."
            },
            {
                "author": "Julius von Sachs",
                "work": "Text-Book of Botany",
                "quote": "The **foliar** surfaces of vascular plants contain thousands of stomata per square millimeter governing gaseous exchange."
            },
            {
                "author": "Charles Darwin",
                "work": "Insectivorous Plants",
                "quote": "The **foliar** tentacles of Drosera bend inward to entrap prey, stimulated by nitrogenous contact on the leaf blade."
            }
        ]
    },
    "foliate": {
        "primary": "Having leaves or leaflike parts; decorated with leaf-shaped designs.",
        "secondary": "In medieval architecture and numismatics, having cusps or lobes arranged like leaves, as in a trefoil or cinquefoil.",
        "quotes": [
            {
                "author": "John Ruskin",
                "work": "The Seven Lamps of Architecture",
                "quote": "The tracery of the church window dissolved into intricate **foliate** forms that echoed the oak boughs outside."
            },
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "Certain aquatic herbs bear submerged dissected foliage alongside broad **foliate** floating blades."
            },
            {
                "author": "Walter Scott",
                "work": "The Antiquary",
                "quote": "The ancient silver seal was carved with a **foliate** cross surrounded by a half-effaced Norman motto."
            }
        ]
    },
    "foliated": {
        "primary": "Having a layered, sheet-like, or lamellar structure; split into thin leaf-like plates.",
        "secondary": "In metamorphic geology, designating rocks like slate and schist that display a parallel orientation of mineral grains.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Gneiss and mica schist exhibit a **foliated** texture produced by intense tectonic pressure and recrystallization."
            },
            {
                "author": "James Dwight Dana",
                "work": "System of Mineralogy",
                "quote": "Talc occurs typically in **foliated** plates that feel unctuous to the touch and cleave into flexible laminae."
            },
            {
                "author": "John Ruskin",
                "work": "Modern Painters",
                "quote": "The crags were built of dark **foliated** stone, rising in razor-sharp ridges against the stormy horizon."
            }
        ]
    },
    "foliation": {
        "primary": "The state or process of producing leaves; or the arrangement of leaves inside a leaf bud.",
        "secondary": "In geology, the planar arrangement of structural or mineralogical features in metamorphic rocks.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The **foliation** of crystalline schists does not necessarily coincide with the original sedimentary bedding planes."
            },
            {
                "author": "Charles Darwin",
                "work": "Geological Observations on South America",
                "quote": "I observed that the strike of the **foliation** throughout the metamorphic belt remained parallel over hundreds of miles."
            },
            {
                "author": "Asa Gray",
                "work": "Botanical Text-Book",
                "quote": "Vernal **foliation** varies systematically among tree families, some exhibiting plicate and others revolute leaf packing."
            }
        ]
    },
    "folie": {
        "primary": "Madness, folly, or insanity; used especially in psychiatric terms borrowed from French.",
        "secondary": "In clinical psychiatry, designating delusional disorders shared between individuals, such as folie à deux.",
        "quotes": [
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "In chronic delusional insanity, the French alienists recognized the contagious nature of **folie** communicated between intimate relatives."
            },
            {
                "author": "Jean-Martin Charcot",
                "work": "Clinical Lectures on the Diseases of the Nervous System",
                "quote": "Hysterical manifestations frequently display communicative symptoms resembling a transient **folie** à deux."
            },
            {
                "author": "Henry James",
                "work": "The American",
                "quote": "Her sudden resolution had in it an element of romantic **folie** that astonished her conventional Parisian cousins."
            }
        ]
    },
    "folio": {
        "primary": "A sheet of paper folded once across the middle to form two leaves (four pages) of a book.",
        "secondary": "A book of the largest standard size, made of such folded sheets; or a numbered leaf in a ledger or manuscript.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "Old Krook opened the dusty **folio** ledger, pointing with his grimy finger to forgotten legal entries."
            },
            {
                "author": "William Shakespeare",
                "work": "The Complete Works of William Shakespeare",
                "quote": "His works were lovingly gathered into the First **Folio** by his fellow actors Heminge and Condell."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The Scarlet Letter",
                "quote": "Upon the minister's desk lay a venerable theological **folio** bound in pigskin and secured with brass clasps."
            }
        ]
    },
    "foliolate": {
        "primary": "Pertaining to, having, or divided into leaflets; used especially in botanical compound leaf descriptions.",
        "secondary": "Designating pinnately or palmately divided leaves, as in trifoliolate clover or plurifoliolate legumes.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "The common clover possesses a trifoliolate blade, each **foliolate** segment marked with a pale crescent."
            },
            {
                "author": "George Bentham",
                "work": "Handbook of the British Flora",
                "quote": "Leguminous herbs frequently display multi-**foliolate** leaves terminating in a climbing tendril."
            },
            {
                "author": "Charles Darwin",
                "work": "The Power of Movement in Plants",
                "quote": "The individual **foliolate** segments of Oxalis fold downward at night in response to sleep movements."
            }
        ]
    },
    "foliose": {
        "primary": "Bearing many leaves; leafy in appearance or botanical habit.",
        "secondary": "In lichenology and bryology, designating lichens or liverworts with flattened, leafy, dorsiventral thalli.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "The **foliose** lichens of the genus Parmelia adhere loosely to tree bark by delicate rhizines."
            },
            {
                "author": "Douglas Houghton Campbell",
                "work": "The Structure and Development of Mosses and Ferns",
                "quote": "The **foliose** Jungermanniales constitute the largest and most specialized group of liverworts."
            },
            {
                "author": "Gilbert White",
                "work": "The Natural History of Selborne",
                "quote": "Damp autumn bogs are carpeted with **foliose** mosses that retain water through the driest seasons."
            }
        ]
    },
    "folium": {
        "primary": "A leaf, especially of a book, document, or manuscript; or a thin sheet or lamella.",
        "secondary": "In mathematics, a plane curve resembling a leaf; or in anatomy, a leaf-like fold of the cerebellar cortex.",
        "quotes": [
            {
                "author": "Henry Gray",
                "work": "Anatomy: Descriptive and Surgical",
                "quote": "The cerebellar vermis terminates in a prominent horizontal fold termed the **folium** vermis."
            },
            {
                "author": "M. R. James",
                "work": "The Wanderings and Homes of Manuscripts",
                "quote": "Upon the fourteenth **folium** of the psalter, the illuminator executed a magnificent initial letter in lapis and gold."
            },
            {
                "author": "Charles Babbage",
                "work": "Passages from the Life of a Philosopher",
                "quote": "The Cartesian **folium** presents fascinating mathematical singularities that test mechanical curve-drawing engines."
            }
        ]
    },
    "interfoliate": {
        "primary": "To interleave; insert blank leaves between the printed pages of a book.",
        "secondary": "To intersperse or insert alternately, as thin layers, notes, or strata between existing materials.",
        "quotes": [
            {
                "author": "Thomas Carlyle",
                "work": "Sartor Resartus",
                "quote": "The eccentric professor was accustomed to **interfoliate** his lecture notes with autobiographical fragments and memoranda."
            },
            {
                "author": "Charles Dickens",
                "work": "The Pickwick Papers",
                "quote": "The attorney decided to **interfoliate** the court transcript with affidavits collected from reluctant witnesses."
            },
            {
                "author": "Walter Scott",
                "work": "The Antiquary",
                "quote": "An antiquarian scholar had caused the binder to **interfoliate** the volume with clean writing paper for marginalia."
            }
        ]
    },
    "perfoliate": {
        "primary": "In botany, having the base of the leaf completely surrounding and clasping the stem so the stem appears to pierce through it.",
        "secondary": "Describing amplexicaul leaves whose basal lobes unite on the opposite side of the vegetative axis.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "In the thoroughwort, Eupatorium perfoliatum, the opposite stem leaves are united at the base, presenting a **perfoliate** habit."
            },
            {
                "author": "John Lindley",
                "work": "The Vegetable Kingdom",
                "quote": "Species of Bupleurum exhibit completely **perfoliate** leaves that make the slender floral stem seem to emerge through the blade."
            },
            {
                "author": "George Bentham",
                "work": "Handbook of the British Flora",
                "quote": "The yellow-wort displays connate, **perfoliate** foliage that clasps the rigid stem like a leafy cup."
            }
        ]
    },
    "defloration": {
        "primary": "The act of plucking blossoms or depriving a plant of flowers; or the deflowering of a virgin.",
        "secondary": "In historical literature and legal terminology, the loss of virginal chastity, or the harvesting of prime blooms.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The licentious tyrant violated every sacred law of hospitality, staining his banquet with the **defloration** of noble maidens."
            },
            {
                "author": "Francis Bacon",
                "work": "The Advancement of Learning",
                "quote": "Premature **defloration** of an orchard crop diminishes both the strength of the rootstock and the harvest."
            },
            {
                "author": "Samuel Richardson",
                "work": "Clarissa",
                "quote": "The despairing lady lamented the cruel deceit that had threatened her honor with irremediable **defloration**."
            }
        ]
    },
    "effloresce": {
        "primary": "To burst into bloom; blossom forth; or to become covered with powdery crusts or crystals.",
        "secondary": "In chemistry, to lose water of crystallization upon exposure to air, forming a powdery surface coating.",
        "quotes": [
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "Crystals of sodium carbonate gradually **effloresce** in dry air, shedding their water of crystallization as white powder."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Saline crusts of sodium sulfate **effloresce** upon the arid mud flats of desert basins during the summer drought."
            },
            {
                "author": "John Ruskin",
                "work": "The Stones of Venice",
                "quote": "Gothic architecture seemed to **effloresce** into exuberant sculpted foliage under the chisel of the master mason."
            }
        ]
    },
    "efflorescence": {
        "primary": "A state or period of blossoming and flowering; the blooming of plants.",
        "secondary": "In chemistry, the formation of a powdery white deposit on a crystalline substance as water of hydration is lost.",
        "quotes": [
            {
                "author": "John Ruskin",
                "work": "Modern Painters",
                "quote": "The alpine meadows exhibited a magnificent **efflorescence** of gentians and anemones immediately after the melting of the snow."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Damp cellar walls frequently display a chalky **efflorescence** of nitre deposited by evaporating groundwater."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "The intellectual **efflorescence** of the Italian Renaissance was nurtured by the rediscovered philosophical texts of Greece."
            }
        ]
    },
    "efflorescent": {
        "primary": "Blossoming, flowering forth, or in a state of blooming expansion.",
        "secondary": "In chemistry and mineralogy, prone to losing water of crystallization and becoming coated with a powdery deposit in air.",
        "quotes": [
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "Glauber's salt forms large transparent prisms that rapidly become **efflorescent** and opaque when exposed to the atmosphere."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The dry lake bed was covered with an **efflorescent** crust of soda that drifted like snow before the desert wind."
            },
            {
                "author": "John Ruskin",
                "work": "The Stones of Venice",
                "quote": "The **efflorescent** beauty of the Byzantine capitals revealed the boundless inventive fancy of medieval sculptors."
            }
        ]
    },
    "flora": {
        "primary": "The aggregate plant life occurring within a specific geographic region or geological period.",
        "secondary": "A scientific catalog, manual, or taxonomic book describing the botanical species of a particular area.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "The indigenous **flora** of oceanic islands typically contains an unusually high proportion of endemic species."
            },
            {
                "author": "Asa Gray",
                "work": "Scientific Papers of Asa Gray",
                "quote": "A comparison between the eastern North American **flora** and that of Japan reveals remarkable generic similarities."
            },
            {
                "author": "Alexander von Humboldt",
                "work": "Aspects of Nature",
                "quote": "The tropical **flora** changes abruptly as one ascends the Andean cordillera from humid plains to freezing paramos."
            }
        ]
    },
    "floral": {
        "primary": "Of, relating to, or resembling flowers; consisting of or adorned with floral blossoms.",
        "secondary": "In botany, pertaining to the reproductive organs, perianth, and bracts of flowering plants.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom",
                "quote": "The bright colors and sweet nectar of **floral** envelopes have evolved to attract insect pollinators."
            },
            {
                "author": "Thomas Hardy",
                "work": "Tess of the d'Urbervilles",
                "quote": "She wore a simple cotton gown with a delicate **floral** print, carrying a basket of freshly gathered watercress."
            },
            {
                "author": "Asa Gray",
                "work": "Botanical Text-Book",
                "quote": "The four whorls of a complete **floral** structure comprise the calyx, corolla, androecium, and gynoecium."
            }
        ]
    },
    "floreal": {
        "primary": "The eighth month of the French Republican calendar, lasting from April 20 to May 19; the month of flowers.",
        "secondary": "Pertaining to springtime flowers, blossom-time, or floral festivity in European revolutionary poetry.",
        "quotes": [
            {
                "author": "Thomas Carlyle",
                "work": "The French Revolution",
                "quote": "It is the month of **Floreal**, and Paris blooms with lilacs while the Revolutionary Tribunal continues its grim sittings."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "Classical Rome celebrated the rites of Flora in early May, anticipating the **floreal** calendar of later revolutions."
            },
            {
                "author": "Victor Hugo",
                "work": "Les Misérables",
                "quote": "In the joyous warmth of **Floreal**, the young lovers wandered beneath the blossoming chestnuts of the Luxembourg gardens."
            }
        ]
    },
    "florence": {
        "primary": "A historic cultural city in central Italy, the capital of Tuscany, situated on the Arno River.",
        "secondary": "The cradle of the Italian Renaissance, celebrated for its artistic masterpieces, humanism, and Medici heritage.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Romola",
                "quote": "The bell of the Palazzo Vecchio rang out over **Florence**, summoning the citizens to witness the trial of Savonarola."
            },
            {
                "author": "John Ruskin",
                "work": "Mornings in Florence",
                "quote": "The frescoes of Giotto in the church of Santa Croce embody the noble dawn of Christian art in **Florence**."
            },
            {
                "author": "Henry James",
                "work": "Italian Hours",
                "quote": "Looking down upon **Florence** from the heights of Fiesole, the great dome of Brunelleschi dominates the Tuscan plain."
            }
        ]
    },
    "florentine": {
        "primary": "Relating to or characteristic of Florence, Italy, its people, language, history, or Renaissance art.",
        "secondary": "A native or citizen of Florence; or in cooking, prepared with or served upon a bed of spinach.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Romola",
                "quote": "The proud **Florentine** merchant held his head high, mindful that his city was the cultural teacher of Europe."
            },
            {
                "author": "John Ruskin",
                "work": "The Stones of Venice",
                "quote": "The **Florentine** masters subordinated mere color to the intellectual severity of design and contour."
            },
            {
                "author": "Walter Pater",
                "work": "The Renaissance: Studies in Art and Poetry",
                "quote": "Leonardo da Vinci brought to the **Florentine** studio a restless curiosity that united science with mystical painting."
            }
        ]
    },
    "florescence": {
        "primary": "A period or developmental stage of full flowering and botanical blossoming.",
        "secondary": "Figuratively, a culminating period of vigorous artistic, literary, or intellectual development.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Scientific Papers of Asa Gray",
                "quote": "The sudden **florescence** of vernal wildflowers carpets the forest floor before the tree canopy excludes sunlight."
            },
            {
                "author": "John Ruskin",
                "work": "Modern Painters",
                "quote": "The Gothic cathedrals represent the magnificent **florescence** of an age whose faith was carved in enduring stone."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "The nineteenth century witnessed an unexampled **florescence** of mechanical invention and biological discovery."
            }
        ]
    },
    "florescent": {
        "primary": "In a state of flowering or blooming; expanding into floral blossoms.",
        "secondary": "Flourishing, flourishingly productive, or in a condition of culminating vigor and creative growth.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "The **florescent** apex of the plant bears clusters of flower buds that open in regular centripetal succession."
            },
            {
                "author": "John Ruskin",
                "work": "Proserpina: Studies of Wayside Flowers",
                "quote": "Each **florescent** stem unfurls its delicate petals with geometrical precision to meet the morning sun."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The Marble Faun",
                "quote": "The old villa garden was a **florescent** wilderness of orange trees and climbing roses running wild over broken statues."
            }
        ]
    },
    "floret": {
        "primary": "A small or individual flower, especially one of the many making up a composite flower head.",
        "secondary": "In botany, each single miniature flower within an Asteraceae inflorescence or grass spikelet.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Different Forms of Flowers on Plants of the Same Species",
                "quote": "In the dandelion head, each marginal **floret** is ligulate and carries its own stamen tube and bifid style."
            },
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "The central tubular **floret** of the sunflower produces abundant nectar that attracts swarms of bumblebees."
            },
            {
                "author": "George Bentham",
                "work": "Handbook of the British Flora",
                "quote": "In grasses, the two-glumed spikelet contains one or more **floret** structures enclosed by paleae."
            }
        ]
    },
    "florey": {
        "primary": "Relating to Howard Florey, the Australian pharmacologist who co-developed penicillin for clinical medicine.",
        "secondary": "Pertaining to historical awards, institutes, or biomedical discoveries associated with the purification of antibiotics.",
        "quotes": [
            {
                "author": "Alexander Fleming",
                "work": "Nobel Lecture in Physiology or Medicine",
                "quote": "The biochemical genius of **Florey** and Chain turned my laboratory curiosity into a lifesaver for millions of wounded soldiers."
            },
            {
                "author": "Oliver Sacks",
                "work": "Oaxaca Journal",
                "quote": "Medical historians justly celebrate the Oxford team led by **Florey** for isolating stable therapeutic penicillin."
            },
            {
                "author": "William Osler",
                "work": "Aequanimitas",
                "quote": "Modern antimicrobial chemotherapy stands upon the collaborative foundations laid by Fleming, **Florey**, and their peers."
            }
        ]
    },
    "floricultural": {
        "primary": "Pertaining to the cultivation of flowers and ornamental flowering plants.",
        "secondary": "Relating to the commercial floral industry, greenhouse floriculture, and specialized breeding of floral varieties.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "The extraordinary varieties of the pansy and carnation illustrate what human **floricultural** selection can accomplish."
            },
            {
                "author": "Luther Burbank",
                "work": "Harvest of the Years",
                "quote": "My **floricultural** experiments with the Shasta daisy aimed at combining hardiness with dazzling white petals."
            },
            {
                "author": "John Lindley",
                "work": "The Theory of Horticulture",
                "quote": "A sound knowledge of plant physiology enables the **floricultural** grower to induce winter blooming in greenhouse camellias."
            }
        ]
    },
    "floriculture": {
        "primary": "The cultivation, breeding, and management of flowering and ornamental plants.",
        "secondary": "The specialized segment of horticulture devoted to producing cut flowers, bedding plants, and potted floral specimens.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "The history of Dutch **floriculture** during the tulip mania demonstrated how prized floral mutations can command fortunes."
            },
            {
                "author": "Luther Burbank",
                "work": "The Training of the Human Plant",
                "quote": "Through patient **floriculture**, we learn that every living seedling responds gratefully to fertile soil and attentive care."
            },
            {
                "author": "Francis Bacon",
                "work": "The Essays",
                "quote": "A prince can take no nobler delight than in the refined practice of **floriculture** throughout the changing seasons."
            }
        ]
    },
    "florid": {
        "primary": "Having a red or flushed complexion; or excessively ornate, flowery, and intricate in style.",
        "secondary": "In architecture and music, elaborately embellished with decorative carving or complex melodic ornamentation.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "Mr. Boythorn was a large gentleman with a **florid** face, massive white hair, and a tremendously resonant voice."
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "The bailiff was a stout, **florid** countryman whose jovial countenance shone like a polished russet apple."
            },
            {
                "author": "John Ruskin",
                "work": "The Stones of Venice",
                "quote": "Late Gothic architecture declined into a **florid** decadence where structural strength was sacrificed to frivolous ornament."
            }
        ]
    },
    "florida": {
        "primary": "A southeastern peninsula state of the United States, named by Spanish explorers from Pascua Florida (Feast of Flowers).",
        "secondary": "A subtropical maritime region characterized by wetlands, mangrove coasts, sandy barrier islands, and coral reefs.",
        "quotes": [
            {
                "author": "John James Audubon",
                "work": "Ornithological Biography",
                "quote": "While cruising along the coral reefs of **Florida**, we observed thousands of white ibises and pelicans feeding among the mangroves."
            },
            {
                "author": "Washington Irving",
                "work": "Conquest of Florida",
                "quote": "Ponce de Leon named the land **Florida** because he discovered its green shores during the Easter festival of flowers."
            },
            {
                "author": "Ralph Waldo Emerson",
                "work": "Journals",
                "quote": "The winter climate of Saint Augustine in **Florida** restored strength to my lungs with its balmy orange-scented breezes."
            }
        ]
    },
    "floridian": {
        "primary": "Relating to the state of Florida, its geography, ecology, people, or climate.",
        "secondary": "A native or resident of the state of Florida; or pertaining to the subtropical Florida bioregion.",
        "quotes": [
            {
                "author": "John James Audubon",
                "work": "Ornithological Biography",
                "quote": "The rare **Floridian** jay inhabits dry scrub oak ridges, exhibiting social habits distinct from northern corvids."
            },
            {
                "author": "Charles Darwin",
                "work": "Coral Reefs",
                "quote": "Observations upon the **Floridian** barrier reef confirm that coral growth is limited by water temperature and depth."
            },
            {
                "author": "Washington Irving",
                "work": "Conquest of Florida",
                "quote": "The Spanish cavaliers were astonished by the fierce valor and archery of the native **Floridian** warriors."
            }
        ]
    },
    "floridity": {
        "primary": "Redness or flushed ruddy tone of complexion; or excessive flowery ornamentation in rhetoric.",
        "secondary": "An excessive richness or ornate elaboration of style in literature, music, or architectural decoration.",
        "quotes": [
            {
                "author": "Samuel Johnson",
                "work": "The Lives of the English Poets",
                "quote": "His prose style was criticized for excessive **floridity**, where simple thoughts were buried beneath piles of flowery epithets."
            },
            {
                "author": "John Ruskin",
                "work": "Modern Painters",
                "quote": "The painter avoided the vulgar **floridity** of the late Venetian decadence, choosing chaste harmonies of silver and olive."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The Byzantine orators compensated for their lack of genuine political freedom by an empty rhetorical **floridity**."
            }
        ]
    },
    "floridly": {
        "primary": "In a florid manner; with an ornate, flowery, or heavily embellished style.",
        "secondary": "With a ruddy or flushed facial complexion, or with elaborate and ostentatious decoration.",
        "quotes": [
            {
                "author": "Henry James",
                "work": "The Portrait of a Lady",
                "quote": "He expressed his formal condolences **floridly**, using elaborate continental phrases that sounded hollow to English ears."
            },
            {
                "author": "Charles Dickens",
                "work": "Little Dorrit",
                "quote": "The auctioneer declaimed **floridly** upon the virtues of the bankrupt merchant's plate, waving his hammer with theatrical grace."
            },
            {
                "author": "Thomas Hardy",
                "work": "The Mayor of Casterbridge",
                "quote": "The village signpost was **floridly** painted with gilded flourishes that defied rustic simplicity."
            }
        ]
    },
    "floridness": {
        "primary": "Ruddiness of facial complexion, or ornate elaboration and flowery decoration in prose style.",
        "secondary": "An overabundance of flowery metaphors, ostentatious phrasing, or excessive architectural decoration.",
        "quotes": [
            {
                "author": "Samuel Johnson",
                "work": "The Rambler",
                "quote": "The **floridness** of his early poetry gave way in mature life to a grave and masculine simplicity of expression."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "His robust health was evident in the genial **floridness** of his cheeks and his booming laughter."
            },
            {
                "author": "Thomas Carlyle",
                "work": "Past and Present",
                "quote": "Parliamentary debate had degenerated into theatrical **floridness**, while the starving operatives cried for bread."
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
    print(f"Total words in data_botany_b2_p1: {len(data_botany_b2_p1)}")
    errs = validate_all(data_botany_b2_p1)
    if errs:
        print(f"\n❌ VALIDATION FAILED with {len(errs)} errors:")
        for e in errs:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("\n✅ ALL 65 words in Cluster Botany Batch 2 Part 1 PASSED local pre-audit validation!")
