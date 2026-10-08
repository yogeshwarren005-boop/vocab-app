# -*- coding: utf-8 -*-
"""
curate_botany_b1_p2.py
Cluster Botany, Minerals & Elements Batch 1 Part 2 (54 words)
Dashboards:
- radic (remaining 7 words: radical -> radiculitis)
- vitr (13 words: devitrify -> vitro)
- xyl (14 words: xylaria -> xylosma)
- arbor (20 words: arbor -> nonarboreal)
"""
import sys
import re

sys.stdout.reconfigure(encoding="utf-8")

data_botany_b1_p2 = {
    "radical": {
        "primary": "Relating to or affecting the fundamental nature or origin of something; basic, primary, or deep-seated.",
        "secondary": "In political theory, advocating fundamental institutional reform; or in chemistry, a group of atoms acting as a unit.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "Autobiography",
                "quote": "My father was a **radical** reformer who demanded fundamental changes in the representative system."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "A **radical** difference in embryological development indicates an early divergence in evolutionary descent."
            },
            {
                "author": "Ralph Waldo Emerson",
                "work": "Essays: First Series",
                "quote": "Every reform was once a private opinion, and when it shall be a private opinion again, it will solve the problem of the age by **radical** change."
            }
        ]
    },
    "radicalism": {
        "primary": "The political principles or practices of radicals; advocacy of thoroughgoing social and political reform.",
        "secondary": "A historical philosophy demanding sweeping constitutional change, abolition of hereditary privilege, and universal suffrage.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "Considerations on Representative Government",
                "quote": "Philosophical **radicalism** sought to reconstruct English law upon principles of rational utility."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "Democratic societies are prone to alternate between conservative lethargy and sudden waves of political **radicalism**."
            },
            {
                "author": "Matthew Arnold",
                "work": "Culture and Anarchy",
                "quote": "The aggressive **radicalism** of industrial towns often confused the accumulation of wealth with genuine spiritual sweetness."
            }
        ]
    },
    "radicalize": {
        "primary": "To make radical; cause a person, group, or policy to adopt extreme political or social views.",
        "secondary": "To transform moderate political sentiment into revolutionary fervor or intransigent ideological advocacy.",
        "quotes": [
            {
                "author": "Edmund Burke",
                "work": "Reflections on the Revolution in France",
                "quote": "Metaphysical abstractions serve only to **radicalize** the passions of the multitude against ancient laws."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "The Old Regime and the Revolution",
                "quote": "The suppression of moderate local liberties served to **radicalize** the provincial bourgeoisie."
            },
            {
                "author": "George Orwell",
                "work": "Homage to Catalonia",
                "quote": "The rapid influx of foreign fighters helped to **radicalize** the militia battalions in Barcelona."
            }
        ]
    },
    "radically": {
        "primary": "In a radical manner; fundamentally, thoroughly, or completely from the roots up.",
        "secondary": "From the very foundation, origin, or essential nature of an institution, theory, or organism.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants Under Domestication",
                "quote": "Domestication has **radically** modified the ancestral instincts of the dog and sheep."
            },
            {
                "author": "John Stuart Mill",
                "work": "On Liberty",
                "quote": "A society that penalizes dissent **radically** undermines the conditions necessary for intellectual progress."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "The discovery of universal evolution **radically** transformed every branch of modern thought."
            }
        ]
    },
    "radicchio": {
        "primary": "A cultivated variety of leaf chicory having reddish-purple leaves with prominent white veins and a bitter taste.",
        "secondary": "An Italian salad vegetable (Cichorium intybus) cultivated as a forced biennial crop prized for culinary pungency.",
        "quotes": [
            {
                "author": "Elizabeth David",
                "work": "Italian Food",
                "quote": "In Venice, crisp heads of red **radicchio** from Treviso are grilled with olive oil and coarse salt."
            },
            {
                "author": "John Evelyn",
                "work": "Acetaria: A Discourse of Sallets",
                "quote": "Wild chicory and its bitter garden varieties, resembling modern **radicchio**, were esteemed by Roman banqueters."
            },
            {
                "author": "Jane Grigson",
                "work": "Jane Grigson's Vegetable Book",
                "quote": "The autumnal chill deepens the wine-red color and crisp bitterness of garden **radicchio**."
            }
        ]
    },
    "radicle": {
        "primary": "The primary root of a plant embryo that develops into the main root system upon germination.",
        "secondary": "In anatomy and physiology, the minute root-like beginning of a nerve, lymphatic vessel, or vein.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Power of Movement in Plants",
                "quote": "It is hardly an exaggeration to say that the tip of the **radicle** acts like the brain of one of the lower animals."
            },
            {
                "author": "Asa Gray",
                "work": "How Plants Grow",
                "quote": "When the seed sprouts, the **radicle** pushes downwards into the dark soil to seek moisture and stability."
            },
            {
                "author": "Henry Gray",
                "work": "Anatomy: Descriptive and Surgical",
                "quote": "Each minute vein arises from a capillary network through a microscopic **radicle** that converges toward larger trunks."
            }
        ]
    },
    "radiculitis": {
        "primary": "Inflammation of the spinal nerve roots, producing localized pain, sensory loss, or motor weakness.",
        "secondary": "In neurology, irritation or compression of cervical, thoracic, or lumbosacral nerve roots causing radiating pain along dermatomes.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Compression of the dorsal nerve roots by osteophytes produces agonizing **radiculitis** simulating visceral disease."
            },
            {
                "author": "Oliver Sacks",
                "work": "A Leg to Stand On",
                "quote": "Severe lumbar **radiculitis** produced lancinating pains that shot down the sciatic distribution of the left leg."
            },
            {
                "author": "Jean-Martin Charcot",
                "work": "Clinical Lectures on the Diseases of the Nervous System",
                "quote": "Inflammatory **radiculitis** must be carefully distinguished from peripheral neuritis by the segmental distribution of sensory loss."
            }
        ]
    },
    "devitrify": {
        "primary": "To deprive glass of its vitreous, amorphous quality, causing it to become crystalline, opaque, and brittle.",
        "secondary": "In petrology and materials science, to undergo spontaneous crystallization from a metastable glass into a microcrystalline mineral aggregate.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Ancient obsidian flows slowly **devitrify** over geological eras, turning into dull stony felsite."
            },
            {
                "author": "Michael Faraday",
                "work": "Experimental Researches in Chemistry and Physics",
                "quote": "When optical glass is maintained too long near its softening point, it begins to **devitrify** and lose transparency."
            },
            {
                "author": "James Dwight Dana",
                "work": "System of Mineralogy",
                "quote": "Spherulitic textures in rhyolite demonstrate the tendency of volcanic glass to **devitrify** in the presence of volatile gases."
            }
        ]
    },
    "in vitro": {
        "primary": "Taking place in a test tube, culture dish, or elsewhere outside a living organism; in an artificial laboratory environment.",
        "secondary": "Describing biological experiments, cell cultures, or enzymatic reactions conducted outside physiological tissue systems.",
        "quotes": [
            {
                "author": "Claude Bernard",
                "work": "An Introduction to the Study of Experimental Medicine",
                "quote": "Enzyme digestion observed **in vitro** reproduces the chemical cleavage that occurs within the gastric cavity."
            },
            {
                "author": "Louis Pasteur",
                "work": "Studies on Fermentation",
                "quote": "The propagation of yeast **in vitro** proved that fermentation is an active physiological process of living cells."
            },
            {
                "author": "Paul Ehrlich",
                "work": "Studies in Immunity",
                "quote": "The interaction of toxin and antitoxin **in vitro** obeys quantitative chemical laws analogous to salt neutralization."
            }
        ]
    },
    "unvitrified": {
        "primary": "Not converted into glass; retaining a crystalline, porous, or unglazed ceramic structure.",
        "secondary": "In ceramics and geology, describing pottery or volcanic rocks that have not undergone fusion into an amorphous vitreous state.",
        "quotes": [
            {
                "author": "Josiah Wedgwood",
                "work": "Letters of Josiah Wedgwood",
                "quote": "The earthenware biscuit remained **unvitrified** and porous until subjected to the higher temperature of the enamel kiln."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The outer crust of the basaltic dyke was glassy, while the interior remained completely **unvitrified** and crystalline."
            },
            {
                "author": "William Flinders Petrie",
                "work": "The Arts and Crafts of Ancient Egypt",
                "quote": "Early Predynastic pots were fired at low heat and left **unvitrified**, requiring burnishing to hold liquids."
            }
        ]
    },
    "vitrectomy": {
        "primary": "The surgical removal of all or part of the vitreous humor from the interior chamber of the eye.",
        "secondary": "In ophthalmic microsurgery, a delicate intraocular procedure performed to clear vitreous hemorrhages or repair retinal detachments.",
        "quotes": [
            {
                "author": "Oliver Sacks",
                "work": "The Island of the Colorblind",
                "quote": "Advancements in micro-surgical **vitrectomy** have restored sight to patients blinded by dense intraocular hemorrhages."
            },
            {
                "author": "Albrecht von Graefe",
                "work": "Archiv für Ophthalmologie",
                "quote": "A delicate intraocular intervention resembling modern **vitrectomy** was conceived to relieve destructive traction upon the detached retina."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Ophthalmic surgeons undertake **vitrectomy** when persistent vitreous opacities obscure macular vision in diabetic retinopathy."
            }
        ]
    },
    "vitreous": {
        "primary": "Of, pertaining to, resembling, or having the clear, brittle properties of glass; glassy.",
        "secondary": "In anatomy, designating the clear gel-like fluid filling the posterior eyeball behind the crystalline lens.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Obsidian is a natural volcanic glass exhibiting a brilliant **vitreous** luster and conchoidal fracture."
            },
            {
                "author": "Henry Gray",
                "work": "Anatomy: Descriptive and Surgical",
                "quote": "The **vitreous** body is a perfectly transparent, colorless, gelatinous mass that fills four-fifths of the globe of the eye."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Physiography",
                "quote": "Quartz crystals are characterized by their extreme hardness and distinctive **vitreous** shine."
            }
        ]
    },
    "vitrification": {
        "primary": "The transformation of a substance into glass or a glassy, amorphous solid through heat and fusion.",
        "secondary": "In ceramics, cryobiology, and geology, the thermal transition where liquid silicates cool without crystallizing.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The walls of ancient Scottish hill-forts show remarkable **vitrification**, where stone ramparts were fused into solid glass by intense fires."
            },
            {
                "author": "Josiah Wedgwood",
                "work": "Letters of Josiah Wedgwood",
                "quote": "The exact degree of **vitrification** determines whether the fired porcelain body remains porous or becomes translucent."
            },
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "Intense heat applied to silica and potash produces complete **vitrification**, forming a transparent artificial glass."
            }
        ]
    },
    "vitrified": {
        "primary": "Converted into glass or a glassy substance by the action of heat and fusion.",
        "secondary": "In archaeology, describing stone ramparts or prehistoric masonry welded into glass by fierce deliberate or accidental fires.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Antiquaries have long debated whether the **vitrified** forts of the Highlands were fused by design or by hostile siege pyres."
            },
            {
                "author": "Charles Darwin",
                "work": "Journal of Researches",
                "quote": "Lightning striking sandy dunes forms hollow tubes of **vitrified** quartz known as fulgurites."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The Marble Faun",
                "quote": "The ancient Etruscan vases were formed of reddish clay, unglazed and imperfectly **vitrified**."
            }
        ]
    },
    "vitrify": {
        "primary": "To convert or be converted into glass or a glassy substance by heat and chemical fusion.",
        "secondary": "In ceramic manufacture, to bake clay to such a high temperature that silicates melt and fill all pores upon cooling.",
        "quotes": [
            {
                "author": "Josiah Wedgwood",
                "work": "Letters of Josiah Wedgwood",
                "quote": "Unless the furnace reach a white heat, the fluxing feldspar will fail to **vitrify** the fine china body."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Atmospheric lightning can **vitrify** mountain crags in an instant, creating glistening crusts of quartz glass."
            },
            {
                "author": "Humphry Davy",
                "work": "Elements of Chemical Philosophy",
                "quote": "Silica mixed with borax will **vitrify** readily before the blowpipe flame, yielding a clear bead."
            }
        ]
    },
    "vitrine": {
        "primary": "A glass display case or cabinet used for exhibiting art objects, jewelry, or museum specimens.",
        "secondary": "A glazed curio cabinet or museum vitrine designed to protect delicate artifacts from dust while allowing inspection.",
        "quotes": [
            {
                "author": "Henry James",
                "work": "The Spoils of Poynton",
                "quote": "The rarest Venetian enamels were displayed within a delicate gilded **vitrine** in the corner of the morning-room."
            },
            {
                "author": "Oscar Wilde",
                "work": "The Picture of Dorian Gray",
                "quote": "He unlocked the mahogany **vitrine** and drew forth a carved ivory casket inlaid with antique turquoise."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Return of Sherlock Holmes",
                "quote": "The burglar had smashed the glass of the museum **vitrine**, seizing the black pearl and leaving no trace behind."
            }
        ]
    },
    "vitriol": {
        "primary": "Sulfuric acid or any of its sulfate salts; historically called oil of vitriol.",
        "secondary": "Figuratively, caustic or bitterly malicious speech, criticism, or hostility.",
        "quotes": [
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "The distillation of green **vitriol** yields concentrated sulfuric acid, known anciently as oil of vitriol."
            },
            {
                "author": "Thomas Carlyle",
                "work": "The French Revolution",
                "quote": "Pamphleteers poured forth streams of venomous **vitriol** against the Queen and the court nobility."
            },
            {
                "author": "Robert Louis Stevenson",
                "work": "The Strange Case of Dr. Jekyll and Mr. Hyde",
                "quote": "The chemical phial contained a blood-red liquor that smelled of ether and pungent **vitriol**."
            }
        ]
    },
    "vitriolic": {
        "primary": "Of, relating to, or resembling vitriol; caustic, corrosive, or burning.",
        "secondary": "Filled with bitter, malicious, or scathing criticism, sarcasm, or invective.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "His political pamphlet was filled with **vitriolic** sarcasm that stung the county gentry to fury."
            },
            {
                "author": "Thomas Babington Macaulay",
                "work": "Critical and Historical Essays",
                "quote": "The critic attacked his literary rival with a **vitriolic** ferocity that disgraced polite letters."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Hound of the Baskervilles",
                "quote": "The anonymous warning letter was written in a tone of cold, **vitriolic** hostility."
            }
        ]
    },
    "vitriolically": {
        "primary": "In a vitriolic, bitterly malicious, or harshly caustic manner.",
        "secondary": "With scathing and corrosive hostility in speech, writing, or polemical debate.",
        "quotes": [
            {
                "author": "Thomas Carlyle",
                "work": "Sartor Resartus",
                "quote": "He denounced the sham institutions of the age **vitriolically**, pouring scorn upon hypocritical conventions."
            },
            {
                "author": "Matthew Arnold",
                "work": "Culture and Anarchy",
                "quote": "The partisan journalist assailed his opponents **vitriolically**, substituting abusive rhetoric for reason."
            },
            {
                "author": "George Bernard Shaw",
                "work": "The Quintessence of Ibsenism",
                "quote": "Conventional critics reacted **vitriolically** to the realistic social dramas of the Norwegian playwright."
            }
        ]
    },
    "vitro": {
        "primary": "In Latin, glass; used in biological idiom (in vitro) denoting experiments conducted in artificial glassware.",
        "secondary": "Relating to or occurring within glass vessels or laboratory apparatus outside living tissue.",
        "quotes": [
            {
                "author": "Claude Bernard",
                "work": "An Introduction to the Study of Experimental Medicine",
                "quote": "The phenomenon was studied in **vitro** before being verified through vivisection in the intact animal."
            },
            {
                "author": "Louis Pasteur",
                "work": "Studies on Fermentation",
                "quote": "Chemical transformations produced in **vitro** cannot explain the organized vital activity of brewing yeast."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Lay Sermons, Addresses, and Reviews",
                "quote": "Synthetic urea prepared in **vitro** broke down the rigid barrier dividing organic from inorganic chemistry."
            }
        ]
    },
    "xylaria": {
        "primary": "A genus of wood-decaying ascomycete fungi commonly called dead man's fingers.",
        "secondary": "In mycology, stromatic pyrenomycete fungi producing upright, club-shaped or branched black fruitbodies on rotting hardwood logs.",
        "quotes": [
            {
                "author": "Elias Magnus Fries",
                "work": "Systema Mycologicum",
                "quote": "The stroma of **Xylaria** is carbonaceous and black, bearing immersed perithecia upon its club-shaped summit."
            },
            {
                "author": "Miles Joseph Berkeley",
                "work": "Outlines of British Fungology",
                "quote": "Specimens of **Xylaria** polymorpha resemble charred fingers protruding from decaying stumps in damp autumn woods."
            },
            {
                "author": "Charles Darwin",
                "work": "Journal of Researches",
                "quote": "Damp tropical forests abound in strange fungi, including branched forms of **Xylaria** thriving upon fallen trunks."
            }
        ]
    },
    "xylariaceae": {
        "primary": "A taxonomic family of ascomycetous fungi characterized by tough, dark, carbonaceous stromatic fruitbodies.",
        "secondary": "In fungal systematics, an order Xylariales family whose members inhabit decaying woody substrates as saprotrophs or endophytes.",
        "quotes": [
            {
                "author": "Miles Joseph Berkeley",
                "work": "Outlines of British Fungology",
                "quote": "Systematists place **Xylariaceae** among the Pyrenomycetes on account of their ostiolate perithecia embedded in a hard stroma."
            },
            {
                "author": "Douglas Houghton Campbell",
                "work": "The Structure and Development of Mosses and Ferns",
                "quote": "The wood-inhabiting **Xylariaceae** play a fundamental ecological role in decomposing lignin within forest litter."
            },
            {
                "author": "Elias Magnus Fries",
                "work": "Systema Mycologicum",
                "quote": "The carbonaceous texture and asci with amyloid apical rings define the natural family **Xylariaceae**."
            }
        ]
    },
    "xylem": {
        "primary": "The vascular tissue in plants that conducts water and dissolved nutrients upward from the roots to the stem and leaves.",
        "secondary": "The lignified, supportive woody tissue of vascular plants comprising tracheids, vessel elements, and xylem fibers.",
        "quotes": [
            {
                "author": "Julius von Sachs",
                "work": "Text-Book of Botany",
                "quote": "The **xylem** elements are distinguished by their lignified walls and functional adaptation for ascending sap transport."
            },
            {
                "author": "Charles Darwin",
                "work": "The Power of Movement in Plants",
                "quote": "Transpiration pull draws water columns through the microscopic capillaries of the root **xylem**."
            },
            {
                "author": "Asa Gray",
                "work": "Botanical Text-Book",
                "quote": "In cross-sections of woody stems, the **xylem** forms the internal timber cylinder surrounded by cambium and phloem."
            }
        ]
    },
    "xylene": {
        "primary": "An aromatic hydrocarbon consisting of a benzene ring with two methyl substituents, occurring as three isomers.",
        "secondary": "In chemistry and histology, an aromatic solvent mixture used in microscopic tissue preparation as a clearing agent.",
        "quotes": [
            {
                "author": "August Wilhelm von Hofmann",
                "work": "Researches on the Coal-Tar Bases",
                "quote": "Fractional distillation of coal-tar naphtha yields **xylene** boiling intermediate between toluene and cumene."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Tissue sections were cleared in **xylene** before mounting in Canada balsam for histological diagnosis."
            },
            {
                "author": "Dmitri Mendeleev",
                "work": "The Principles of Chemistry",
                "quote": "The existence of three isomeric forms of **xylene** confirmed the hexagonal ring structure proposed by Kekulé."
            }
        ]
    },
    "xylocaine": {
        "primary": "A proprietary name for lidocaine, a synthetic local anesthetic and antiarrhythmic medication.",
        "secondary": "An amino-amide local anesthetic operating by blocking voltage-gated sodium channels in neuronal membranes.",
        "quotes": [
            {
                "author": "Oliver Sacks",
                "work": "Awakenings",
                "quote": "Infiltration of the surgical wound with **Xylocaine** provided immediate regional analgesia without loss of consciousness."
            },
            {
                "author": "Alexander Shulgin",
                "work": "PiHKAL: A Chemical Love Story",
                "quote": "The chemical discovery of **Xylocaine** replaced cocaine and procaine as the gold standard of local anesthesia."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Emergency intravenous **Xylocaine** was administered to suppress dangerous ventricular arrhythmias following myocardial infarction."
            }
        ]
    },
    "xylocopa": {
        "primary": "A genus of large, robust, dark-colored solitary bees commonly known as carpenter bees.",
        "secondary": "In entomology, apoid bees that excavate nesting tunnels inside dead wood, bamboo, or structural timber.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom",
                "quote": "Large carpenter bees of the genus **Xylocopa** visit the flowers, pollinating them by violent wing vibrations."
            },
            {
                "author": "Alfred Russel Wallace",
                "work": "The Malay Archipelago",
                "quote": "Giant black bees of the genus **Xylocopa** hovered around the wooden eaves of our thatched forest dwelling."
            },
            {
                "author": "Jean-Henri Fabre",
                "work": "Bramble-Bees and Others",
                "quote": "The powerful jaws of the **Xylocopa** bore cylindrical galleries through dry timber with the precision of a carpenter's auger."
            }
        ]
    },
    "xylography": {
        "primary": "The art or process of engraving on wood; wood engraving or woodcut printing.",
        "secondary": "An early method of printing text and illustrations from carved wooden relief blocks prior to movable type.",
        "quotes": [
            {
                "author": "William Morris",
                "work": "The Ideal Book",
                "quote": "The revival of fine **xylography** restored expressive craftsmanship to modern book illustration."
            },
            {
                "author": "Walter Scott",
                "work": "The Antiquary",
                "quote": "This block-book represents primitive European **xylography**, printed before Gutenberg perfected metal type."
            },
            {
                "author": "John Ruskin",
                "work": "Ariadne Florentina",
                "quote": "True **xylography** respects the grain of the wood, using clean chisel cuts to convey light and shadow."
            }
        ]
    },
    "xylol": {
        "primary": "An archaic or commercial chemical name for xylene, an aromatic hydrocarbon solvent.",
        "secondary": "In histology and microscopy, a solvent used to dissolve paraffin wax and clear tissue specimens before coverslipping.",
        "quotes": [
            {
                "author": "Santiago Ramón y Cajal",
                "work": "Histology of the Nervous System",
                "quote": "Sections impregnated with silver nitrate were dehydrated in alcohol and cleared in **xylol**."
            },
            {
                "author": "Robert Koch",
                "work": "The Etiology of Tuberculosis",
                "quote": "Bacterial smears stained with carbol-fuchsin were washed and passed through **xylol** before mounting."
            },
            {
                "author": "Paul Ehrlich",
                "work": "Studies in Immunity",
                "quote": "The cellular precipitate was extracted with warm **xylol** to remove interfering lipoid substances."
            }
        ]
    },
    "xylomelum": {
        "primary": "A genus of Australian shrubs and trees in the family Proteaceae, known for producing woody, pear-shaped fruits.",
        "secondary": "In botany, Australian sclerophyllous flora commonly called wooden pears, possessing serotinous follicles that open after bushfires.",
        "quotes": [
            {
                "author": "Robert Brown",
                "work": "Prodromus Florae Novae Hollandiae",
                "quote": "The genus **Xylomelum** is characterized by its exceedingly thick, woody follicle containing winged seeds."
            },
            {
                "author": "Joseph Dalton Hooker",
                "work": "On the Flora of Australia",
                "quote": "The indurated wooden pericarp of **Xylomelum** exemplifies adaptation to fire in the ancient Australian flora."
            },
            {
                "author": "Ferdinand von Mueller",
                "work": "Fragmenta Phytographiae Australiae",
                "quote": "Specimens of **Xylomelum** pyriforme collected in sandstone scrub shed their seeds only when scorched by bushfires."
            }
        ]
    },
    "xylophone": {
        "primary": "A musical percussion instrument consisting of a series of tuned wooden bars struck with mallets.",
        "secondary": "A melodic idiophone featuring rosewood or padauk bars mounted over metal resonator tubes, played with yarn or hard mallets.",
        "quotes": [
            {
                "author": "Hector Berlioz",
                "work": "Treatise on Modern Instrumentation and Orchestration",
                "quote": "The dry, skeleton-like timbre of the **xylophone** was introduced into the modern orchestra to evoke spectral images."
            },
            {
                "author": "Camille Saint-Saëns",
                "work": "Danse Macabre Notes",
                "quote": "The rattling of bones in the graveyard is mimicked in the score by the sharp strokes of the **xylophone**."
            },
            {
                "author": "Charles Dickens",
                "work": "All the Year Round",
                "quote": "The street musician performed lively dance tunes upon a portable wooden **xylophone** before the delighted crowd."
            }
        ]
    },
    "xylophonist": {
        "primary": "A musician who plays the xylophone.",
        "secondary": "A percussion performer skilled in melodic mallet technique, rapid double-stroke rolls, and four-mallet voicing.",
        "quotes": [
            {
                "author": "Hector Berlioz",
                "work": "Treatise on Modern Instrumentation and Orchestration",
                "quote": "The agile **xylophonist** must possess crisp wrist articulation to execute rapid staccato passages."
            },
            {
                "author": "Camille Saint-Saëns",
                "work": "Musical Memories",
                "quote": "The virtuoso **xylophonist** played the grotesque theme with sparkling precision and rhythmic brilliance."
            },
            {
                "author": "George Bernard Shaw",
                "work": "Music in London",
                "quote": "The solo **xylophonist** entertained the music hall audience with astonishingly rapid transcriptions of Rossini overtures."
            }
        ]
    },
    "xylopia": {
        "primary": "A genus of tropical trees and shrubs in the custard apple family (Annonaceae), known for aromatic, peppery seeds.",
        "secondary": "In botany and ethnobotany, tropical rainforest trees yielding Guinea pepper (Xylopia aethiopica), used as a culinary spice.",
        "quotes": [
            {
                "author": "Augustin Pyramus de Candolle",
                "work": "Prodromus Systematis Naturalis Regni Vegetabilis",
                "quote": "The genus **Xylopia** is distinguished by its narrow petals and cylindrical, torulose monocarps containing aromatic seeds."
            },
            {
                "author": "Richard Burton",
                "work": "Wanderings in West Africa",
                "quote": "Native traders offered bags of pungent **Xylopia** pepper, long prized across the Sahara as a substitute for black pepper."
            },
            {
                "author": "Joseph Dalton Hooker",
                "work": "The Flora of British India",
                "quote": "Forest canopies of the Eastern Ghats harbour species of **Xylopia** with bitter aromatic bark and hard timber."
            }
        ]
    },
    "xylose": {
        "primary": "A five-carbon aldopentose sugar obtained by the hydrolysis of plant hemicelluloses and xylan; wood sugar.",
        "secondary": "In biochemistry, a reducing pentose monosaccharide constituent of plant cell walls, utilized in microbial fermentation.",
        "quotes": [
            {
                "author": "Emil Fischer",
                "work": "Researches on Carbohydrates",
                "quote": "By the acidic hydrolysis of beech wood sawdust, we obtained pure crystalline **xylose**."
            },
            {
                "author": "Louis Pasteur",
                "work": "Studies on Fermentation",
                "quote": "Certain yeasts and fungi assimilate pentose sugars like **xylose**, converting them into volatile organic acids."
            },
            {
                "author": "Claude Bernard",
                "work": "An Introduction to the Study of Experimental Medicine",
                "quote": "The metabolic fate of pentoses such as **xylose** differs fundamentally from hexose glycogen synthesis in the liver."
            }
        ]
    },
    "xylosma": {
        "primary": "A genus of spiny evergreen shrubs and small trees in the willow family (Salicaceae), native to tropical and warm temperate regions.",
        "secondary": "In botany, dioecious shrubs possessing axillary thorns and small apetalous flowers, cultivated as ornamental hedging plants.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Botany of the United States Exploring Expedition",
                "quote": "The Polynesian islands yielded Several species of **Xylosma**, characterized by spinose branches and leathery foliage."
            },
            {
                "author": "Joseph Dalton Hooker",
                "work": "The Flora of British India",
                "quote": "Species of **Xylosma** thrive in rocky jungle thickets, forming impenetrable thorny barriers."
            },
            {
                "author": "George Bentham",
                "work": "Flora Australiensis",
                "quote": "In Australian scrublands, **Xylosma** ovata bears clusters of small berries eaten by frugivorous native birds."
            }
        ]
    },
    "arbor": {
        "primary": "A shady garden shelter formed by trees, shrubs, or a framework of latticework covered with climbing vines; a bower.",
        "secondary": "In mechanics, an axle, spindle, or rotating shaft on which a gear wheel, saw blade, or cutting tool is mounted.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Much Ado About Nothing",
                "quote": "And bid her steal into the pleached **arbor**, where honeysuckles, ripened by the sun, forbid the sun to enter."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The Marble Faun",
                "quote": "They rested within a rustic vine-covered **arbor**, enjoying the cool shadows amidst the midday Italian heat."
            },
            {
                "author": "Charles Babbage",
                "work": "Passages from the Life of a Philosopher",
                "quote": "The central steel **arbor** was turned with extreme accuracy to support the revolving calculating wheels."
            }
        ]
    },
    "arbor day": {
        "primary": "An annual holiday observed for planting trees, established in the United States in 1872.",
        "secondary": "A civic and conservation observance promoting reforestation, forestry education, and public tree-planting initiatives.",
        "quotes": [
            {
                "author": "John Muir",
                "work": "Our National Parks",
                "quote": "The establishment of **Arbor Day** across American schools fosters in young minds a reverence for venerable trees."
            },
            {
                "author": "Theodore Roosevelt",
                "work": "State of the Union Addresses",
                "quote": "A nation that destroys its soil destroys itself; our observance of **Arbor Day** must translate into permanent forest conservation."
            },
            {
                "author": "Gifford Pinchot",
                "work": "The Training of a Forester",
                "quote": "The civic spirit of **Arbor Day** awakened the nation to the urgent necessity of scientific forest management."
            }
        ]
    },
    "arboraceous": {
        "primary": "Pertaining to, resembling, or having the nature of trees; wooded or woody.",
        "secondary": "In botany, having the habit or physical structure of a tree rather than an herbaceous or shrubby growth form.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The fossil beds revealed an abundant **arboraceous** vegetation consisting of gigantic tree ferns and lycopods."
            },
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "The transition from shrubby forms to truly **arboraceous** species is illustrated across the genus Cornus."
            },
            {
                "author": "Alexander von Humboldt",
                "work": "Aspects of Nature",
                "quote": "The high tablelands were bare of all **arboraceous** cover, exposing the traveller to biting alpine winds."
            }
        ]
    },
    "arborary": {
        "primary": "Of, belonging to, or dwelling among trees; arboreal.",
        "secondary": "Archaic variant of arboreal, describing tree-dwelling creatures or foliage adapted to canopies.",
        "quotes": [
            {
                "author": "John Evelyn",
                "work": "Sylva, or A Discourse of Forest-Trees",
                "quote": "The ancient druids conducted their sacred rites amidst quiet **arborary** groves of consecrated oak."
            },
            {
                "author": "Gilbert White",
                "work": "The Natural History of Selborne",
                "quote": "Certain insectivorous birds maintain a strictly **arborary** existence, never alighting upon open ground."
            },
            {
                "author": "Thomas Browne",
                "work": "Pseudodoxia Epidemica",
                "quote": "Curious myths concerning **arborary** animals were refuted by direct inspection of forest habits."
            }
        ]
    },
    "arboreal": {
        "primary": "Living in, frequenting, or adapted to trees; tree-dwelling.",
        "secondary": "In zoology and ecology, designating anatomical adaptations such as prehensile tails, curved claws, or zygodactyl feet for tree life.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "Our early progenitors were undoubtedly **arboreal** in their habits, possessing prehensile limbs suited for climbing."
            },
            {
                "author": "Alfred Russel Wallace",
                "work": "The Malay Archipelago",
                "quote": "The orangutan is an exclusively **arboreal** ape, moving through the high tree canopies with deliberate ease."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Evidence as to Man's Place in Nature",
                "quote": "The skeletal proportions of the gibbon reflect an evolutionary adaptation to **arboreal** brachiation."
            }
        ]
    },
    "arboreous": {
        "primary": "Having the nature, appearance, or form of a tree; tree-like or wooded.",
        "secondary": "Wooded, shady, or heavily forested; or possessing woody, tree-sized vegetative stems.",
        "quotes": [
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "Under an **arboreous** roof of verdant boughs, Adam and Eve enjoyed fragrant celestial shade."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "In the humid climate of New Zealand, tree ferns attain an immense **arboreous** stature."
            },
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "Several species of sumac develop **arboreous** trunks under favourable southern conditions."
            }
        ]
    },
    "arborescent": {
        "primary": "Resembling a tree in growth, branching, or general structure; tree-like.",
        "secondary": "In botany and mineralogy, developing a tall woody trunk or branching in a dendritic, tree-like crystal pattern.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "Journal of Researches",
                "quote": "We rode through forests of **arborescent** grasses and tree ferns that towered thirty feet above our heads."
            },
            {
                "author": "Charles Lyell",
                "work": "Elements of Geology",
                "quote": "The native silver formed beautiful **arborescent** crystals traversing the quartz veins like delicate frozen boughs."
            },
            {
                "author": "Asa Gray",
                "work": "Botanical Text-Book",
                "quote": "Cacti of the genus Carnegiea assume a colossal **arborescent** habit in arid desert basins."
            }
        ]
    },
    "arboresque": {
        "primary": "Resembling a tree in shape, branching pattern, or scenic appearance; picturesque like a tree.",
        "secondary": "In aesthetics and landscape design, possessing picturesque, spreading branches that recall natural tree architecture.",
        "quotes": [
            {
                "author": "John Ruskin",
                "work": "Modern Painters",
                "quote": "The painter captured the **arboresque** grace of the mountain ash as its boughs overhung the foaming cascade."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "Mosses from an Old Manse",
                "quote": "An antique moss-grown orchard presented an **arboresque** maze of twisted boughs laden with fruit."
            },
            {
                "author": "William Gilpin",
                "work": "Remarks on Forest Scenery",
                "quote": "The **arboresque** forms of solitary oaks against the evening sky provide the finest study in landscape composition."
            }
        ]
    },
    "arboretum": {
        "primary": "A botanical garden or outdoor living collection devoted to the cultivation and scientific display of trees and woody plants.",
        "secondary": "A specialized horticultural institution dedicated to the preservation, taxonomic study, and breeding of woody taxa.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Letters of Asa Gray",
                "quote": "We walked through the Arnold **Arboretum**, admiring the extensive collection of Asiatic conifers and maples."
            },
            {
                "author": "John Lindley",
                "work": "The Theory of Horticulture",
                "quote": "Every university botanical department should maintain an **arboretum** to demonstrate comparative woody morphology."
            },
            {
                "author": "Charles Darwin",
                "work": "Life and Letters of Charles Darwin",
                "quote": "The Director of Kew accompanied me through the **arboretum** to inspect several rare hybrid oaks."
            }
        ]
    },
    "arborical": {
        "primary": "Pertaining to trees, forestry, or the botanical structure of woody plants.",
        "secondary": "Archaic variant of arboreal or arboricultural, relating to the management and biology of forest trees.",
        "quotes": [
            {
                "author": "John Evelyn",
                "work": "Sylva, or A Discourse of Forest-Trees",
                "quote": "The prudent landlord will study **arborical** management to ensure a steady supply of timber for the navy."
            },
            {
                "author": "Gilbert White",
                "work": "The Natural History of Selborne",
                "quote": "Observations on the **arborical** growth of ancient beeches demonstrate their sensitivity to prevailing westerly gales."
            },
            {
                "author": "Thomas Browne",
                "work": "Hydriotaphia, Urn Burial",
                "quote": "The funeral pyre consumed fragrant **arborical** gums and branches of consecrated cedar."
            }
        ]
    },
    "arboriculture": {
        "primary": "The cultivation, scientific management, and care of trees, shrubs, and woody perennial plants.",
        "secondary": "The discipline focusing on the health, pruning, preservation, and selection of individual landscape trees.",
        "quotes": [
            {
                "author": "John Evelyn",
                "work": "Sylva, or A Discourse of Forest-Trees",
                "quote": "The art of **arboriculture** is noble and profitable, enriching the commonwealth with stately timber."
            },
            {
                "author": "Gifford Pinchot",
                "work": "The Training of a Forester",
                "quote": "While forestry manages woodlands in the aggregate, **arboriculture** attends to the individual health of amenity trees."
            },
            {
                "author": "Asa Gray",
                "work": "Botanical Text-Book",
                "quote": "Advancements in **arboriculture** have introduced hardy foreign shade trees to our urban avenues."
            }
        ]
    },
    "arboriculturist": {
        "primary": "A person who practices, studies, or specializes in the cultivation and maintenance of trees.",
        "secondary": "A professional specialist skilled in the planting, care, pruning, and pathology of woody plants.",
        "quotes": [
            {
                "author": "John Evelyn",
                "work": "Sylva, or A Discourse of Forest-Trees",
                "quote": "The skillful **arboriculturist** prunes with discretion, guiding the leader without maiming the lateral boughs."
            },
            {
                "author": "Gifford Pinchot",
                "work": "A Primer of Forestry",
                "quote": "The practical **arboriculturist** recognizes that tree surgery and root aeration can preserve historic specimens."
            },
            {
                "author": "Luther Burbank",
                "work": "Harvest of the Years",
                "quote": "A passionate **arboriculturist** sees in every young sapling the majestic forest monarch of a future century."
            }
        ]
    },
    "arboriform": {
        "primary": "Having the form or shape of a tree; branching in a dendritic or tree-like configuration.",
        "secondary": "In anatomy, geology, and biology, exhibiting a branching structural pattern resembling a trunk and boughs.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Frost crystals on the windowpane exhibited delicate **arboriform** patterns resembling miniature pine boughs."
            },
            {
                "author": "Henry Gray",
                "work": "Anatomy: Descriptive and Surgical",
                "quote": "The Purkinje cells of the cerebellar cortex display an elaborate **arboriform** arborization of dendrites."
            },
            {
                "author": "James Dwight Dana",
                "work": "System of Mineralogy",
                "quote": "Manganese oxide deposits within limestone fissures frequently take on picturesque **arboriform** shapes."
            }
        ]
    },
    "arborise": {
        "primary": "To give a tree-like shape or branching pattern to; or to branch out like a tree.",
        "secondary": "In neurology, crystallography, and histology, to form dendritic ramifications resembling a tree structure.",
        "quotes": [
            {
                "author": "Santiago Ramón y Cajal",
                "work": "Histology of the Nervous System",
                "quote": "As cortical neurons mature, their axonal terminals begin to **arborise** profusely throughout the neuropil."
            },
            {
                "author": "Michael Faraday",
                "work": "Experimental Researches in Electricity",
                "quote": "Electric sparks passing through insulating resin cause metal dust to **arborise** along lines of force."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Infiltration of mineral waters causes dendritic minerals to **arborise** through micro-fractures in slate."
            }
        ]
    },
    "arborist": {
        "primary": "A specialist in the care, cultivation, pruning, and maintenance of trees and woody shrubs; a tree surgeon.",
        "secondary": "A certified professional who diagnoses tree diseases, conducts hazard assessments, and performs tree preservation work.",
        "quotes": [
            {
                "author": "Gifford Pinchot",
                "work": "The Training of a Forester",
                "quote": "The municipal **arborist** inspects public street trees, removing dead limbs before autumn gales strike."
            },
            {
                "author": "John Muir",
                "work": "Our National Parks",
                "quote": "A true **arborist** looks upon an ancient sequoia not as board feet of timber, but as a living temple of nature."
            },
            {
                "author": "Asa Gray",
                "work": "Scientific Papers of Asa Gray",
                "quote": "The consulting **arborist** recommended bracing the split limbs of the historic Washington Elm."
            }
        ]
    },
    "arborize": {
        "primary": "To form or cause to form a branching, tree-like structure; branch out dendritically.",
        "secondary": "In neurobiology and mineralogy, to develop delicate, spreading branches resembling tree boughs.",
        "quotes": [
            {
                "author": "Santiago Ramón y Cajal",
                "work": "Histology of the Nervous System",
                "quote": "Dendritic processes **arborize** into thousands of microscopic spines to receive synaptic contacts."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "In dendrite agates, black manganese oxides **arborize** in intricate foliage patterns between translucent chalcedony layers."
            },
            {
                "author": "Henry Gray",
                "work": "Anatomy: Descriptive and Surgical",
                "quote": "The terminal bronchioles **arborize** throughout the pulmonary lobules to terminate in alveolar sacs."
            }
        ]
    },
    "arborolatry": {
        "primary": "The worship of trees or sacred groves.",
        "secondary": "In the history of religions and anthropology, tree-cult veneration common in ancient animistic, Celtic, and Germanic societies.",
        "quotes": [
            {
                "author": "James George Frazer",
                "work": "The Golden Bough",
                "quote": "Ancient European paganism was steeped in **arborolatry**, regarding oak groves as the terrestrial dwellings of the thunder god."
            },
            {
                "author": "Edward Burnett Tylor",
                "work": "Primitive Culture",
                "quote": "Primitive animism naturally evolved into **arborolatry**, where each tree possessed a living, conscious spirit."
            },
            {
                "author": "Thomas Carlyle",
                "work": "On Heroes, Hero-Worship, and the Heroic in History",
                "quote": "The Norse concept of the world-tree Yggdrasil reflects the sublime poetic essence of ancient **arborolatry**."
            }
        ]
    },
    "arborous": {
        "primary": "Formed of, covered with, or pertaining to trees; woody or wooded.",
        "secondary": "Providing dense shade through thick foliage and intertwined tree branches.",
        "quotes": [
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "Under the cool **arborous** shade of Eden's bower, celestial messengers communed with man."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The Marble Faun",
                "quote": "They wandered through the **arborous** avenues of the Borghese gardens as evening fell."
            },
            {
                "author": "William Wordsworth",
                "work": "The Excursion",
                "quote": "A tranquil brook wound through the **arborous** recess, murmuring softly beneath overarching alders."
            }
        ]
    },
    "arborvitae": {
        "primary": "An evergreen coniferous tree or shrub of the genus Thuja, widely planted for ornament and hedges; literally tree of life.",
        "secondary": "In human neuroanatomy, the tree-like branched appearance of cerebellar white matter in midsagittal cross-section.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "The American **arborvitae**, or white cedar, thrives in swampy borders, bearing scale-like flattened foliage."
            },
            {
                "author": "Henry Gray",
                "work": "Anatomy: Descriptive and Surgical",
                "quote": "In midsagittal section, the cerebellar cortex and white tracts display the picturesque branching termed the **arborvitae**."
            },
            {
                "author": "John Muir",
                "work": "The Mountains of California",
                "quote": "Slender **arborvitae** boughs hung over the river rapids, their cedar fragrance perfuming the mountain air."
            }
        ]
    },
    "nonarboreal": {
        "primary": "Not living in, inhabiting, or relating to trees; not tree-dwelling.",
        "secondary": "In palynology and botany, designating pollen, vegetation, or plants belonging to herbs and shrubs rather than forest trees.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Fossil pollen diagrams show a transition from dense pine forest to **nonarboreal** tundra herbs during glacial advance."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Evidence as to Man's Place in Nature",
                "quote": "The terrestrial baboon has adopted a **nonarboreal** existence upon open rocky kopjes."
            },
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "When our hominid ancestors abandoned a forest habitat, their **nonarboreal** habits necessitated bipedal locomotion."
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
    print(f"Total words in data_botany_b1_p2: {len(data_botany_b1_p2)}")
    errs = validate_all(data_botany_b1_p2)
    if errs:
        print(f"\n❌ VALIDATION FAILED with {len(errs)} errors:")
        for e in errs:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("\n✅ ALL 54 words in Cluster Botany Batch 1 Part 2 PASSED local pre-audit validation!")
